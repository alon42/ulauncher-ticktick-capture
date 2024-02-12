# ulauncher-ticktick-capture

> [ulauncher](https://ulauncher.io/) Extension to capture an idea in your [Ticktick](https://ticktick.com/) inbox.

## Features

- write idea and store it into ticktick

# thanks
This code is based on 
https://github.com/pascalbe-dev/ulauncher-todoist-capture

I thanks `Pascal Betting` for it

## Requirements

- [ulauncher 5](https://ulauncher.io/)
- Python > 3

## Installation

Open ulauncher preferences window -> extensions -> add extension and paste the following url:

`https://github.com/alon42/ulauncher-ticktick-capture.git`

## Configuration

- Before usage you need to configure your ticktick API token in plugin preferences. Find or create your API token [here](https://app.ticktick.com/app/settings/integrations/developer).

## Contribution

Please refer to [the contribution guidelines](./CONTRIBUTING.md)

## Local development

### Requirements

- `less` package installed
- `inotify-tools` package installed

### Steps

1. Clone the repo `git clone https://github.com/alon42/ulauncher-ticktick-capture.git`
2. Cd into the folder `cd ulauncher-ticktick-capture`
3. Watch and deploy your extension locally for simple developing and testing in parallel `./watch-and-deploy.sh` (this will restart ulauncher without extensions and deploy this extension at the beginning and each time a file in this directory changes)
4. go to "extentions" section in ulauncher, you will have there instruction for how to start the extention in dev,
 get out of "extentions" screen, get back, and WHALLA, you see your extention dev
5. Check the extension log `less /tmp/ulauncher-extension.log +F`
6. Check ulauncher dev log `less /tmp/ulauncher.log +F`
