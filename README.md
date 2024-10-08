# filesDetect

A demo tool to remove sensitive information from a supplied file using the Skyflow Detect (NLP based) API.

This intends to show the power of the Skyflow API first approach, using the Skyflow Detect endpoints to remove sensitive data from a file

Before running the tool, you need to perform pre-setup tasks
You need to have a Skyflow Try environment account (login)

Login to your Skyflow Studio (assuminng you are a vault owener or administrator)

Create a Skyflow Account level "**Service Account**"
The service account MUST have the following Assignments & Roles:

- Assignment: Account-Level Role: "Account Admin"
- Assignment: Workspace-level Role: "Vault Creator" and "Workspace Admin"
- "SAVE" the settings and generate a **credentials.json** file. (You will be requested to provide this file when the script runs!)
- Note: You need to use this generated credentials.json file and not the one supplied in this repo which is just a container.

In the "filesDetect" repo, there is a primary settings file: **detect_params.json**
Edit this file and change **ALL** the relevant parameter values to the ones associated with your Skyflow Account and environment.
Make sure you identify the location of the "Common_Files_Directory" in the parameters file. The script uses common funcitons from this directory.

Detect File types supported by this script are:
mp3,wav,pdf,txt,json,jpg,jpeg,tif,tiff,png,bmp

All done! You are ready to run the filesDetect (deidentifier).
This repo comes with a series of sample files which you can run in the "detectSampletFiles" directory.

Now run the genefile detector: filesDetect.py and follow the prompts.

> python3 filesDetect.py
