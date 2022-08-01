# Email address parser
This project is a CLI (command-line interface) application that performs operations on email addresses read from multiple files. It has originally been created as a recruitment task for a Python backend internship and uses the OOP paradigm and argparse.

## Usage
Put the files you want to parse in the emails subdirectory and make the script location your current working directory. Now you're ready to go! Run main.py with one of commands provided below. Currently, the program can parse text and .csv files. It will parse all the files for email addresses, rejecting duplicates and invalid ones. No packages outside the standard library are needed. Python 3.10 is recommended.  

## Commands
### 1. Show incorrect emails (`--incorrect-emails`, `-ic`)
Print the number of invalid email addresses, then one invalid address per line.
### 2. Search emails by text (`--search str`, `-s str`)
Search for the string argument in loaded email addresses. Print the number of found emails, then one found address per line.
### 3. Group emails by domain (`--group-by-domain`, `-gbd`)
Group emails by domain. Then order groups, addresses within groups alphabetically and print them, one per line.
### 4. Find emails that are not in the log file (`--find-emails-not-in-logs path_to_log_file`, `-feil path_to_log_file`)
Find loaded emails not in the provided log file. Print the number of found emails, then one found address per line.'

## Examples of use
Sample commands and outputs are provided below:
###
```
python main.py -ic

10 INVALID EMAILS:
        nernserhickle.biz
        wyman.com
        ynolanjones.com
        com
        @hegmann.info
        com
        com
        brad84gmail.com
        yahoo.com
        .com
```
###
```
python main.py --search agustin

5 EMAILS FOUND WITH 'agustin' PHRASE:
        marquardt.agustina@bins.org
        agustin.dare@kreiger.biz
        agustin16@gmail.com
        agustin.ziemann@hilpert.info
        agustina.reilly@yahoo.com
```
###
```
python main.py --group-by-domain 

Domain abbott.com (1):
        daphnee04@abbott.com
Domain abernathy.com (1):
        gutkowski.jeramie@abernathy.com
...
...
...
Domain zieme.com (1):
        boehm.janiya@zieme.com
Domain zulauf.com (3):
        angelita65@zulauf.com
        dthompson@zulauf.com
        luciano04@zulauf.com
```
###
```
python main.py -feil email-sent.logs

240 EMAILS NOT SENT:
        abogisich@skiles.com
        addie.okon@oconnell.com
        aditya.murazik@gorczany.com
        ...
        ...
        ...
        zack63@padberg.info
        zlangworth@gmail.com
        zoe.schmitt@keebler.com
```
