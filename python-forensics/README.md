# Gods
- https://github.com/cclgroupltd

## Xml
- https://github.com/martinblech/xmltodict/blob/master/xmltodict.py

# Zip

How to parse a zipped file with multiprocessing?
- https://stackoverflow.com/questions/73465509/how-to-parse-a-zipped-file-with-multiprocessing

Multithreaded File Unzipping in Python
- https://superfastpython.com/multithreaded-unzip-files/#How_to_Unzip_Files_Concurrently

# Tips

## Controll flow

`def do_one():
  pass

def do_two():
  pass

def do_default():
  pass

actions = {1: do_one, 2: do_two}

actions = actions.get(x, do_default)
action(x)`
