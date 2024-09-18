# Installation 

## Prerequisites

- Mendix Studio Pro 10.12.x or later (Windows only)
- an existing Mendix project
- Download a [release](https://github.com/mxlint/mxlint-extension/releases)

> The following two steps are needed for now because MxLint Extension is still in Beta. One day you will not need to do these anymore as an end-user. 

### Allow unsigned code

MxLint-CLI is not signed yet. The extension automatically downloads the CLI and other dependencies. To allow CLI to run you must

- Open `Powershell` as `Administrator` and then run:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
```
- After that reboot your machine

Above should only be needed once.

### Enable Developer extensions in Studio Pro

Mendix Studio needs to be started with a special flag. To enable this:

- Create a shortcut to your Mendix Studio Pro if you don't have it on your desktop already
- Right click on the shortcut and choose `Properties`
- In the `Target`, append the following string ` --enable-extension-development` after the double quote. Make sure to have a space after this right most double quote.

Now your Studio pro is ready to use Extensions.

## Steps

The following must be done for each project you want to add this extension:

- Create a directory called `extensions` inside of your project directory
- Unpack the zipfile into the `extensions` directory. You will see a directory at `$project/extensions/MxLintExtension`
- Open Mendix Studio pro with extension development flag
- Open your app
