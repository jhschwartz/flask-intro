from flask import request, render_template
from app import app, db
from .forms import HelloForm

@app.route('/hi')
def hi():
	return('hello, world!\n')

@app.route('/new', methods=['GET', 'POST'])
def new():
	form = HelloForm(request.form)

	if request.method == 'GET':
		return render_template('new.html', form=form)

	elif request.method == 'POST' and form.validate:
		#  --- PART NUMBER ONE ---
		# Here you have incoming data submitted through a form!
		# You can access components of a form through form.IDENTIFIER.data
		# So for example to get a name you could do 
		# 				name = form.name.data
		# In the default setup for this tutorial, only name and icecream_fav are available
		# 
		# Instructions: use form data to insert things into the database, and display a success message.
		# Watch out! If a name already exists you will want to use update() not insert().
		# See examples and the jakedb source code for help.
		# ------------------------

		jake = db.get(name='Jake') # example usage - replace with your code

@app.route('/favorites')
def favs():
	return render_template('favorites.html', data=db.all())

# --- PART NUMBER TWO ---
# Create the template favorites.html that will use the data provided from the 
# database to display all people and ice cream preferences in the database.
