# where_to_eat

A simple python script to find somewhere to eat

## Why ?

Struggling to find somewhere to eat and always eating at the same restaurant ? I am !


Use this simple script to find a restaurant. It will also ensure you do not always go to the same place over and over

## Installing

You just need Python 3.x

## Usage

Use the following command line

````
    python yum.py
````

The default behaviour of the script is to choose a restaurant which is not
in the last 5 you visited. However you can customize this behaviour to add more (or less) restaurants

````
    python yum.py -l=10
    python yum.py --limit=10
````

Show possible arguments :
````
    python yum.py -h
    python yum.py --help
````
#TODO 

Load restaurants from a csv file instead of directly in the script

## Author

Alexi Coard (alexicoard@gmail.com)
