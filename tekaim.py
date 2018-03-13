#!/usr/bin/env python3

"""
tekaim - Simple screenshot uploader using maim and teknik.io
"""

from datetime import datetime
import json
import re
import subprocess
import sys

VERSION = "1.0.0"

def main(argv):
    """main"""
    # check arguments
    if '-h' in argv or '--help' in argv:
        print('tekaim v' + VERSION)
        print('Run without arguments to capture a screenshot and upload to teknik.io')
        print('https://github.com/IvanFon/tekaim')
        print('Made by Ivan Fonseca\n<3')
        return

    # load settings file
    with open('config.json', 'r') as config_file:
        config = config_file.read()
    # strip comments
    config = re.sub(r'^\s*//.*$', '', config, flags=re.MULTILINE)
    config = json.loads(config)

    # create screenshots directory if it doesn't already exist
    subprocess.call('mkdir -p ' + config['dir'], shell=True)

    # get filename
    filename = datetime.now().strftime(config['filename']) + config['format']

    # cd command
    cd_cmd = 'cd ' + config['dir'] + ' && '

    # build screenshot command
    screenshot_args = config['screenshot']['args'].replace('${file}', filename)
    screenshot_cmd = cd_cmd + config['screenshot']['bin'] + ' ' + screenshot_args

    # build upload command
    upload_args = config['upload']['args'].replace('${file}', filename)
    upload_args = upload_args.replace('${host}', config['host'])
    upload_cmd = cd_cmd + config['upload']['bin'] + ' ' + upload_args

    # take screenshot
    subprocess.call(screenshot_cmd, shell=True)

    # upload and capture response
    out_raw = subprocess.check_output(upload_cmd, shell=True)
    out = json.loads(out_raw)
    print('File uploaded to: ' + out['result']['url'])

if __name__ == "__main__":
    main(sys.argv)
