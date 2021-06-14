[![Tested on Python 3.9.5](https://img.shields.io/badge/Tested%20-Python%203.9.5-blue.svg?logo=python)](https://www.python.org/downloads)
[![Code Size](https://img.shields.io/github/languages/code-size/Tes3awy/subnetting?color=green)](https://github.com/Tes3awy/subnetting)
[![License](https://img.shields.io/github/license/Tes3awy/subnetting)](https://github.com/Tes3awy/subnetting)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# IPv4 Subnet Calculator in Python3

## Table of Contents

1. [Getting Started](#getting-started)
2. [Installation](#installation)
3. [How it works?](#how-it-works)
4. [Previews](#previews)

### Getting Started

```bash
│   main.py
│   subnetting.py
│   export_subnets.py
│   requirements.txt
│   README.md
│   .gitignore
│
└───assets
        preview.png
```

---

### Installation

```bash
$ git clone https://github.com/Tes3awy/subnetting.git
$ cd subnetting
$ pip install -r requirements.txt --user
```

**OR**

1. Download from [Releases](https://github.com/Tes3awy/subnetting/releases/tag/v1.0).
2. `cd` into `subnetting` directory.
3. Run `path_to\subnetting> pip install -r requirements.txt --user` in terminal.

---

### How it works?

**Windows**

```powershell
path_to\subnetting> python main.py
```

**macOS or Linux**

```bash
$ python3 main.py
```

You will be prompted to enter _comma-seperated_ network subnet(s) in [CIDR notation](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#CIDR_notation) representation:

```bash
- Enter network subnet(s) in CIDR Notation (comma-seperated): 10.0.0.0/8, 172.16.0.0/16, 192.168.1.0/24
```

Then, you will be prompted to enter a name for the Excel file and the sheet within the Excel file that will hold all subnetting data _(Both have default values)_:

```bash
- Enter network subnet(s) in CIDR Notation (comma-seperated): 10.0.0.0/8, 172.16.0.0/16, 192.168.1.0/24
- Name of Excel file w/o file extension? [Default IP-Schema.xlsx]:
- Worksheet name? [Default IP Schema Worksheet]:
```

> Abbreviations <br /> **w/o: Without**

Voila :sparkles: You have an Excel file that includes all required data about each subnet.

```bash
Please check IP-Schema-<EIGHT_CHARS_HASH>_<TODAYS_DATE>.xlsx in current working directory.
```

---

### Previews

**Terminal**
![Python CLI](assets/subnetting-cli.png)

**Excel File**
![Excel Preview](assets/preview.png)
