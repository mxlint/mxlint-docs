# Update CLI

Often mxlint-cli is updated before the extension is refreshed to the latest mxlint-cli version. When the mxlint-extension is started, it ensures there's an mxlint-cli executable called `mxlint-local` present under `$project_dir/.mendix-cache`. If it's absent, the default version is downloaded from Github.

## Override

You can use the latest version (assuming it's compatible) with the extension by following the steps:

- Download the CLI binary from [mxlint-cli releases](https://github.com/mxlint/mxlint-cli/releases) (You need the one with name that ends with windows-amd64.exe for windows)
- You will find a file with name `mxlint-local.exe` in `$project_dir/.mendix-cache/` directory. Delete `mxlint-local.exe`
- Copy or move the new mxlint-cli to `$project_dir/.mendix-cache`. Make sure it's called `mxlint-local.exe`

No need to restart Mendix studio pro

## Reset

If the new version of mxlint-cli is not compatible with your extension, you can reset it by deleting `$project_dir/.mendix-cache/mxlint-local.exe`. After that restart Mendix studio pro. The default mxlint-cli version will be automatically downloaded again.
