# tekaim
A simple tool to take and upload screenshots to teknik.io

## Installation

### Arch Linux

tekaim is available on the AUR. You can either install it with `makepkg` or your preferred AUR helper:

```
yay -S tekaim
pikaur -S tekaim
trizen -S tekaim
etc
```

### Other Linux Distro's

tekaim depends on Python 3+, `maim`, `curl`, and `xclip`. Ensure you have these installed beforehand. At this time, tekaim only supports Linux.

Go to the [latest release](https://github.com/IvanFon/tekaim/releases/latest) and download `tekaim-X.Y.Z.tar.gz`, then use the following commands to untar and install it:

```
tar -xf tekaim-X.Y.Z.tar.gx
cd tekaim
python setup.py install
```

The final command may require `sudo` permissions to install.

## Usage

Run `tekaim` and make a selection. After a few seconds, the URL to your uploaded image will appear. By default, tekaim will upload to [teknik.io](https://www.teknik.io/). The URL will also be copied to your clipboard.

Screenshots are saved to `~/.tekaim/screenshots/` and image links and deletion links are saved to `~/.tekaim/history/`.

### Arguments

- '-f': take screenshot of entire desktop
- '-d': developer mode
  - load config from same directory as executable
  - print debug info

### Configuration

By default, tekaim's config file is stored in `~/.config/tekaim/config.json`. The config file supports single-line, C-style comments. The default config file has a comment explaining each option.

If the config file is missing, tekaim should automatically download the default file from this repository. If you need the default config for whatever reason, it can be found [here](https://github.com/IvanFon/tekaim/blob/master/config.json).

## Dependencies

By default, tekaim depends on [maim](https://github.com/naelstrof/maim) for screenshots, [curl](https://github.com/curl/curl) for uploading, and [xclip](https://github.com/astrand/xclip) to copy to your clipboard. If you want to use something different, you can configure commands and arguments in `config.json`.
