# ETL Pipeline

Takes json files and removes duplicates, empty cells then uploads it to a SQLite3 database

## Table of Contents

* [Overview](#Overview)
* [Installation](#Installation)
* [Usage](#Usage)

## Overview

This software will take in as many json files via the command line you give it and for each file it will remove any duplicate rows or empty cells using pandas. Then it will take each dataFrame to upload each one into a seperate SQLite3 table labbled data0, data1 .etc

## Installation

Install the software to your local system using GitHub clone

* Navigate to the Code button
* Copy the URL either SSH or HTTPS
* Open termial and navigate to the directory the clone will go in
* Write git clone and paste the URl

```bash
  $ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

* Deleted the json files

## Usage

After installation you will be able to use the software for your own files.

* Needs a command line input of a json file. You can input multiple json file

```bash
$ python3 ETL.pipeline.py name.json name.json
```

* Program will then create data.sqlite to store the tables
* Then will create each table 

## Buy Me A Coffee

If you have learnt anything or like it, please consider supporting me.
Anything is appreciated!

![Buy Me A Coffee][2]

[1]: https://www.buymeacoffee.com/tylerbbrown
[2]: https://cdn.buymeacoffee.com/buttons/default-orange.png
