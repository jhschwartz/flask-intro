################################
### DO NOT EDIT FOR TUTORIAL ###
################################

# imports
from app.jakedb import JakeDB

# create the database (note that this is already done for you in the exercises)
db = JakeDB('data1234.json')

# insert some stuff
db.insert(name='Jake', favorite='Mint Chip', dogs='2', year='Sophomore')
db.insert(name='John', dogs='7')
db.insert(name='Sam', tshirt='medium')

# modify something
db.update(name='Jake', year='Junior')

# add a field
db.update(name='Jake', phone='1234')

# get jake as a python dictionary
jake = db.get(name='Jake')

# get jake's number of dogs
num = db.get(name='Jake')['dogs']

# get the whole database as a python dictionary
everyone = db.get_all()

# delete jake
db.delete(name='Jake')

# check if Jake exists - will return False
jake_exists = db.exists(name='Jake')

# clear the database
db.delete_all()
