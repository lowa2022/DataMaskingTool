# Data Masking Tool

## Overview

This program is designed to anonymize sensitive data from CSV files by masking personally identifiable information (PII) such as names, addresses, Social Security Numbers (SSN), driver’s license numbers, and other confidential details. The program ensures that data can still be used for testing, analysis, or sharing without exposing private information.

## Features

- Supports multiple locales: en_IN, en_US, es_ES, en_PH
- Configurable data masking via `config.ini`
- Option to preserve certain data fields such as age, VIN make/model, and null values
- Ensures unique identifiers remain consistent across different datasets
- Can delete original files after processing (configurable option)
- Provides flexible column mapping for CSV files
- Supports data obfuscation while maintaining data integrity for testing and development
- Generates the masked file as `fake_originalfilename.csv`

## Configuration

The program reads settings from a `config.ini` file, which allows customization of data masking behavior. Below are some key configuration options:

### General Settings

- **Locale**: Defines the regional settings for anonymized data.
- **Header**: Indicates whether the CSV has a header.
- **WriteHeaderInOutput**: Specifies whether the output CSV should include a header.
- **PreserveIds**: If enabled, keeps original IDs unchanged.
- **PreserveAge**: Ensures that the age field remains unchanged while anonymizing other data.
- **PreserveEmailDomain**: Retains the domain part of email addresses (e.g., @example.com).
- **PreserveVINMakeModel**: Ensures vehicle information remains accurate while anonymizing other details.
- **PreserveNulls**: Keeps null values unchanged in the output dataset.
- **UniquenessPreservation**: Ensures consistency for key identifiers such as Id, SSN, Email, Phone, etc.
- **DeleteOriginalFile**: Option to remove the original input file after processing.

### Mappings

This section defines how columns in the CSV map to known data fields. Example:

```
Id = id
First = first
Last = last
Street = street
City = city
State = state
Zip = zip
DOB = date
SSN = ssn
Gender = gender
Email = email
Phone = phone
Drivers license = drivers_license
Policy Number = Policy_Number
Claim number = Claim_Number
VIN = VIN
TIN = TIN
User ID = userid
License Plate = license_plate
```

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
2. Update `config.ini` as needed to define column mappings and masking preferences.
3. Run the script:

```bash
python datamask.py
```

4. The anonymized file will be saved as `fake_originalfilename.csv` in the output directory.

## Example

### Input CSV (`input.csv`)

```
id,first,last,ssn,email,phone
1,John,Doe,123-45-6789,john.doe@example.com,555-1234
2,Jane,Smith,987-65-4321,jane.smith@example.com,555-5678
```

### Processed Output CSV (`fake_input.csv`)

```
id,first,last,ssn,email,phone
1,Alice,Brown,XXX-XX-XXXX,alice.brown@example.com,555-0000
2,Bob,Johnson,XXX-XX-XXXX,bob.johnson@example.com,555-1111
```

## Contributing

If you'd like to improve the tool, feel free to fork the repository and submit a pull request.

