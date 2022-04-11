@REM Copy configs over

echo Copying configs over
xcopy configs\*.Any FPSci\ /Y
xcopy model\sphere.* FPSci\model\target\ /Y