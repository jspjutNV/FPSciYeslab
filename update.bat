@REM Copy configs over

echo Copying configs over
xcopy configs\*.Any FPSci\ /Y
xcopy model\sphere.* FPSci\model\target\ /Y

echo Copying scene files over
xcopy scene\*.Scene.Any FPSci\scene\ /Y
xcopy material\*.UniversalMaterial.Any FPSci\material\ /Y