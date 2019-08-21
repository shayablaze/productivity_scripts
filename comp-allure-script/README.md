# installation and setup
- Clone this repository
- install the requirements
- insert into the folder 'config' your 2 allure csv reports. Name them 'before.csv' and 'after.csv'. 

# How to use the script

#### step 1:
```sh
$ python two_reports.py
```
#### step 2:
Go to folder 'results' and you should see two excels. One displays what improved, meaning a test that failed in "before.csv" but passed in 'after.csv' and the other excel, what is a regression(the opposite). 