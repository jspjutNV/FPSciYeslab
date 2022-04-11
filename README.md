# Variable frame time in FPSci

This folder contains a [FPSci](github.com/NVLabs/FPSci) user study that spawns 80 targets in 8 blocks of 10. 
Each target is eliminated with 1 click and a centering target precedes each real target.

## How to run

1. Double click `setup.bat`, which is a script to set up the experiment by downloading the required version of FPSci, and copy the experiment configuration files into the right location. `setup.sh` is the bash equivalent if you prefer that.
2. Double click `RunFPSci.bat` or double click on `FirstPersonScience.exe` inside the `FPSci` directory (created by the download and extract in the script).
3. After the experiment, there will be a results file in the results directory (inside the `FPSci` directory) that you can analyze, or provide to the esports research team for analysis.
4. (optional) If something goes wrong and you need to start over, you can delete the `FPSci` directory, and return to step 1 above.

## For developers and experiment designers

Users or people running the experiment don't need to worry about this part. As a developer or experiment designer, all of the needed configs are in the `configs` directory. The configs are copied into the downloaded FPSci build for the experiment by the `setup.sh` script.

A development workflow may include the following shell commands intermingled with editing config files (under `configs`).

* `update.bat` - Copies the configs from `configs/` to `FPSci` to prepare to test
* `RunFPSci.bat` - Runs the experiment

If you need to use a different version of FPSci, you can update the version number in `setup.sh` and run it again. You may need to delete the `FPSci` directory and contents to prevent conflicting file versions. **Warning:** If you have captured data you want to hold on to, you should back it up somewhere else to avoid losing it.

While you can choose to generate any configs you want, sometimes it's helpful to use a script to generate the experiment config and possibly the user config.

If you want to switch to developer mode while testing, you can edit the `startupConfig.Any` to set the `developerMode = true;`. We encourage any version run for users to have `developerMode = false;`.

### Additional data files

Since it's not recommended to commit large files to a git repository if you can help it, we recommend using another host for non-text data files to be used in your experiment. For models, you can do this by zipping up your model, and hosting it on some cloud storage. If you have a direct download link, then you can have the `setup.bat` and `setup.sh` script grab the file.

If you use google drive, you will want to make sure that everyone you want to be able to download the data files is permissioned on the file. An easy way to do this is to make it publicly readable, which is okay for non-proprietary data files. Google Drive treats files over 100MB different than files less than 100MB. If your file is less than 100MB, the following style of script should work.

In `setup.sh`:

```
# Grab audio files from google drive
# https://drive.google.com/file/d/1SDP-C92P10plMKlTpX43hmNywsxsodTk/view?usp=sharing
curl -L "https://docs.google.com/uc?export=download&id=1SDP-C92P10plMKlTpX43hmNywsxsodTk" > FPSci/sound/ding100by10.zip
unzip FPSci/sound/ding100by10.zip -d FPSci/sound/
```

In `setup.bat`:

```
@REM Grab audio files from google drive
echo Downloading additional data files
@REM https://drive.google.com/file/d/1SDP-C92P10plMKlTpX43hmNywsxsodTk/view?usp=sharing
curl -L "https://docs.google.com/uc?export=download&id=1SDP-C92P10plMKlTpX43hmNywsxsodTk" > FPSci\sound\ding100by10.zip
tar -xf FPSci\sound\ding100by10.zip -C FPSci\sound\
```

Be sure to update the id to match the set of characters in the google drive link between `https://drive.google.com/file/d/` and `/view?usp=sharing`. The above example extracts the files from the `.zip` because audio cannot be loaded from within a `.zip`, but `.obj` and other files can be loaded directly from a `.zip`, and you can use the `.zip` as a folder in describing the path to the files.
