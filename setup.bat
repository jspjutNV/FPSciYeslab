set FPSCI_VERSION=v22.04.01

@REM Get FPSci build
echo Downloading FPSci
curl -LO https://github.com/NVlabs/FPSci/releases/download/%FPSCI_VERSION%/FPSci.%FPSCI_VERSION%.zip
echo Extracting FPSci
mkdir FPSci
tar -xf FPSci.%FPSCI_VERSION%.zip -C FPSci\
echo Removing FPSci zip
del FPSci.%FPSCI_VERSION%.zip

@REM Copy configs over

echo Copying configs over
xcopy configs\*.Any FPSci\ /Y
xcopy model\sphere.* FPSci\model\target\ /Y

echo Copying scene files over
xcopy scene\*.Scene.Any FPSci\scene\ /Y
xcopy material\*.UniversalMaterial.Any FPSci\material\ /Y
