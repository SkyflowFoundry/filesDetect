# filesDetect

**A demo tool to remove sensitive information from a supplied file using the Skyflow Detect (NER-based) API.**

This script leverages the Skyflow Detect API to demonstrate the power of Skyflow’s API-first approach for securely de-identifying sensitive data from various file formats.

## Supported File Types

The script supports deidentification of the following file types:

- **Documents**: `pdf`, `doc`, `docx`, `txt`, `json`, `xml`, `csv`, `xls`, `xlsx`, `ppt`, `pptx`
- **Images**: `bmp`, `jpeg`, `jpg`, `png`, `tif`, `tiff`
- **Audio**: `mp3`, `wav`

### Skyflow Detect Endpoint Used

The tool interacts with the following Skyflow Detect API endpoint:

```
{{url}}/v1/detect/deidentify/file
```

## Pre-Setup Tasks

Before running the tool, please complete the following setup steps:

1. **Skyflow Account Setup**

   - Ensure you have a Skyflow Try Environment account. If not contact Skyflow and we can create one for you.

2. **Login to Skyflow Studio**

   - Log in as a vault owner or administrator.

3. **Create a Service Account**

   - Navigate to your account and create a new **Service Account**. This account will be used by the script to interact with Skyflow APIs.
   - The service account MUST have the following assignments and roles:
     - **Assignment**: Account-Level Role - _"Account Admin"_
     - **Assignment**: Workspace-Level Role - _"Vault Creator"_ and _"Workspace Admin"_
   - Save the settings and generate a **credentials.json** file. This file will be required when running the script.

4. **Edit Configuration Parameters**
   - In the `filesDetect` repository, locate the file: **`detect_params.json`**.
   - Update **all** the relevant parameter values to match your Skyflow account and environment settings.
   - Specify the location of the _Common_Files_Directory_ in the parameters file. The script relies on common functions from this directory.

## Running the Tool

Once setup is complete, you can run the `filesDetect2.0` deidentifier script. Sample files are available in the `detectSampleFiles` directory for testing.

1. Open your terminal.
2. Navigate to the `filesDetect` directory.
3. Run the following command:

   ```bash
   python3 filesDetect2.0.py
   ```

4. Follow the on-screen prompts to process your files.

## Sample Files

This repository includes a collection of sample files located in the **`detectSampleFiles`** directory. Use these for testing and to see the Skyflow Detect tool in action.

## Notes

- Ensure your `credentials.json` file is correctly configured before running the script.
- Make sure the `detect_params.json` file is updated with accurate values for your Skyflow environment.
