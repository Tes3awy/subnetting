[![Tested on Python 3.6+](https://img.shields.io/badge/Python%203.6+-blue.svg?logo=python&logoColor=white)](https://www.python.org/downloads)
[![Code Size](https://img.shields.io/github/languages/code-size/Tes3awy/subnetting?color=green)](https://github.com/Tes3awy/subnetting)
[![Contributors](https://img.shields.io/github/contributors/Tes3awy/subnetting)](https://github.com/Tes3awy/subnetting/graphs/contributors)
[![Release Date](https://img.shields.io/github/release-date/Tes3awy/subnetting)](https://github.com/Tes3awy/subnetting/releases)
[![Commit Activity](https://img.shields.io/github/commit-activity/m/Tes3awy/subnetting)](https://github.com/Tes3awy/subnetting/commits/main)
![Languages Count](https://img.shields.io/github/languages/count/Tes3awy/subnetting)
![Top Language](https://img.shields.io/github/languages/top/Tes3awy/subnetting)
[![Stars](https://img.shields.io/github/stars/Tes3awy/subnetting)](https://github.com/Tes3awy/subnetting/stargazers)
[![Forks](https://img.shields.io/github/forks/Tes3awy/subnetting)](https://github.com/Tes3awy/subnetting/network/members)
[![Open Issues](https://img.shields.io/github/issues/Tes3awy/subnetting)](https://github.com/Tes3awy/subnetting/issues)
[![Closed PR](https://img.shields.io/github/issues-pr-closed/Tes3awy/subnetting)](https://github.com/Tes3awy/subnetting/pulls?q=is%3Apr+is%3Aclosed)
[![License](https://img.shields.io/github/license/Tes3awy/subnetting)](https://github.com/Tes3awy/subnetting/blob/main/LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Pre-Commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

# Advanced IPv4 Subnet Calculator in Python3

## Table of Contents

1. [Getting Started](#getting-started)
2. [Installation](#installation)
3. [How it works?](#how-it-works)
4. [SVI Configuration Template](#svi-configuration-template)
5. [Previews](#previews)

### Getting Started

```bash
│   main.py
│   read_subnets.py
│   subnetting.py
│   export_subnets.py
│   parse_excel.py
│   svi_generator.py
│   svi.j2
│   subnets.csv
│   requirements.txt
│   README.md
│   .pre-commit-config.yaml
│   .gitignore
│   LICENSE
│
└───assets
        preview.png
        subnets-csv.png
        subnetting-cli.png
        svi-template.png
        svi.png
```

---

### Installation

```bash
$ git clone https://github.com/Tes3awy/subnetting.git
$ cd subnetting
$ pip install -r requirements.txt --user
```

**OR**

1. Download the latest release from [Releases](https://github.com/Tes3awy/subnetting/releases/).
2. Extract `subnetting.zip` file.
3. `cd` into `subnetting` directory.
4. Run `path_to\subnetting> pip install -r requirements.txt --user` in terminal.

---

### How it works?

**Windows**

```powershell
path_to\subnetting> python main.py
```

**macOS or Unix**

```bash
$ python3 main.py
```

You will be prompted to enter the name of the CSV file containing input subnets, the gateway, a name for the Excel file to be created. _(All inputs have default values)_.

> A `subnets.csv` file can be found in the repo. This file is an entry point to get started using this program. It's prepopulated with three different subnets. _(Class A, B, and C)_.

```bash
- CSV file [subnets.csv]:
- The gateway, first or last IP Address [0/1] [0]:
- Excel file to create [New-Schema.xlsx]:
```

Voila :sparkles: You have an Excel file that includes all required data about each subnet.

```bash
Please check New-Schema_<TODAYS_DATE>.xlsx in current working directory.
```

> **Default behaviors:**

> 1. CIDR notation with no prefix length will be handled as /32. <br /> - For example, if you enter `10.0.0.1` without a prefix length in the CSV file, the script will handle it like `10.0.0.1/32`.

> 2. The header line **`Subnets in CIDR Notation`** within the `subnets.csv` file is automatically skipped. So, there is no need to manually remove it.

> 3. The gateway input accepts 0 or 1 **ONLY** [Defaults to 0]. 0 picks the first IP address of the subnet, while 1 picks the last IP address.

---

### SVI Configuration Template

Finally, if you have a L3 switch and you want to create [SVI interfaces](https://en.wikipedia.org/wiki/Switch_virtual_interface) of the created subnets on that switch, you can run:

```bash
$ python parse_excel.py --file <EXCEL_FILE_NAME>.xlsx
```

This Python script will generate a configuration file that includes all VLANs and their SVI interfaces.

> **NOTE:** Make sure you add the VLAN ID and VLAN Name in all the cells in the generated Excel file before running `parse_excel.py` script. _Otherwise, VLAN ID and VLAN Name will be NaN_ in the generated configuration file.

---

### Previews

**Terminal**
![Python CLI](assets/subnetting-cli.png)
_Elapsed time is about 9 seconds in here because a CIDR notation like 10.0.0.0/8 is a little bit extensive to process._

**CSV File (Input File)**
![CSV File](assets/subnets-csv.png)

**Excel File (Output File)**
![Excel Preview](assets/preview.png)

**python parse_excel.py -f <EXCEL_FILE_NAME>.xlsx**
![SVI CLI](assets/svi.png)

**SVI Template**
![SVI Template](assets/svi-template.png)
