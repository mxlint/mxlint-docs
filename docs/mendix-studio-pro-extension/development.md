# Development

## Libraries/References

We try to keep the number of dependencies to a minimum. But sometimes it is handy to re-use existing projects.

- [MxLintExtension](https://github.com/mxlint/mxlint-extension) source code
- [Pico CSS](https://picocss.com/docs) to help with styling.

## OSX (MacOS)

- [Visual Studio Code](https://code.visualstudio.com/)
- [Mendix Studio Pro 10.12.2](https://marketplace.mendix.com/link/studiopro)
- [dotNet core SDK vscode](https://dot.net/core-sdk-vscode)
- C# dev kit VSCode extension (inside of VSCode)

### Build

```bash
make

```

### Test

- Open Mendix Studio Pro with `--enable-extension-development` flag: `/Applications/Studio\ Pro\ 10.12.2.41995-Beta.app/Contents/MacOS/studiopro --enable-extension-development`
- Open local project located in `resources/App`

## Windows

- [Visual Studio 2022](https://visualstudio.microsoft.com/)
- [Mendix Studio Pro 10.12.2](https://marketplace.mendix.com/link/studiopro)

Open `Powershell` as `Administrator` and run the following command:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
```


### Build

- Run the script to build:
```powershell
.\dev\build-windows.ps1
```

### Test

- Open studiopro.exe with `--enable-extension-development` flag.
- Open local project located in `resources/App`
