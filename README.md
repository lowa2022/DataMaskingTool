# Data Masking Tool

## Overview
This program anonymizes sensitive data from CSV files by masking personally identifiable information (PII) such as names, addresses, Social Security Numbers (SSN), driver's license numbers, and other confidential details. It generates fake data while maintaining the integrity of the original dataset. This helps in testing, analysis, and sharing data without exposing private information.

## Features
- Supports multiple locales: `en_IN`, `en_US`, `es_ES`, `en_PH`
- Configurable data masking via `config.ini`
- Option to preserve certain data fields (e.g., age, VIN make/model, null values)
- Ensures unique identifiers remain consistent across different datasets
- Option to delete original files after processing
- Flexible column mapping for CSV files
- Supports data obfuscation while maintaining data integrity for testing and development

## Input & Output
- The program prompts you to input a filename when you run it with the command: `python datamask.py`.
- After inputting a filename (e.g., `tenthousand.csv`), the program processes the data and generates a fake file with the prefix `fake_` (e.g., `fake_tenthousand.csv`).

## Sample Files
For demonstration purposes, two sample files are provided in the repository:
- `ten.csv`: A sample file with 10 data entries.
- `tenthousand.csv`: A sample file with 1,000 data entries.

## Configuration
The program reads settings from a `config.ini` file to customize data masking behavior. Key settings include:
- **Locale**: Defines the regional settings for anonymized data.
- **PreserveAge, PreserveEmailDomain, etc.**: Options to retain certain data fields while anonymizing others.
- **UniquenessPreservation**: Ensures consistency for key identifiers like `Id`, `SSN`, `Email`, and `Phone`.
- **DeleteOriginalFile**: Option to remove the original input file after processing.

## Installation
Clone the repository:

```bash
git clone https://github.com/lowa2022/DataMaskingTool.git
```

Navigate to the project folder:

```bash
cd DataMaskingTool
```

Install dependencies (if any):

```bash
pip install -r requirements.txt
```

## Usage
1. Place the CSV file you want to anonymize in the designated input directory.
2. Update `config.ini` to define column mappings and masking preferences.
3. Run the script:

```bash
python datamask.py
```

4. Enter the filename (e.g., `tenthousand.csv`) when prompted.
5. The anonymized file will be saved with the prefix `fake_` (e.g., `fake_tenthousand.csv`) in the output directory.

## Example

**Input CSV (`tenthousand.csv`)**

| id  | first  | last   | ssn         | email                   | phone     |
| --- | ------ | ------ | ----------- | ----------------------- | --------- |
| 1   | John   | Doe    | 123-45-6789 | john.doe@example.com     | 555-1234  |
| 2   | Jane   | Smith  | 987-65-4321 | jane.smith@example.com   | 555-5678  |

**Processed Output CSV (`fake_tenthousand.csv`)**

| id  | first  | last   | ssn         | email                   | phone     |
| --- | ------ | ------ | ----------- | ----------------------- | --------- |
| 1   | Alice  | Brown  | XXX-XX-XXXX | alice.brown@example.com  | 555-0000  |
| 2   | Bob    | Johnson| XXX-XX-XXXX | bob.johnson@example.com  | 555-1111  |

## Contributing
Feel free to fork the repository and submit a pull request if you'd like to improve the tool.

## License
This project is open-source and available under the MIT License.
```
