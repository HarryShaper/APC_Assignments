'''*************************************************
content      Section 2: Style
			 Personal notes for section 2

version      0.0.1
date   		 14-12-2025

author       Harry Shaper <harryshaper@gmail.com>

*************************************************'''

#1. Import globals 
	#Seperate variable types with a new line
	#Import by importance. First for the OS, then third party plug-ins, then bespoke items

#2. Define Variables
	#Constants should be all uppercase                          ----- FILE_PATH = D:/ASSETS
	#Variables should be snakecase and avoid special characters ----- first_name = "Harry Shaper"
	#Make names unique and descriptive. Avoid tempting, temporrary names like "x"
	#Avoid reserved keywords like "Type" or "File"
	#Group Variables in a clean looking table format for readability

#3. Functions
	#Follows most rules of creating variables
	#Good functions only trigger one specific action - short, simple and clear
	#Function names should be specific and indicate what they will do
	#Sub-divide functions into groups (Main functions/press events/change-trigger evens/create object)
	#Add annotations to describe kwargs and args. Overall, this clarifies our code, but don't use it on every function
	#Consider adding a default argument if there is an opitional input or a common input

#4. Documentation
	#Forms of explanatation in forms of (Wiki's, PDF's, ReadME's, Annotations, Comments, etc)
	#Highly neglected aspect of coding.
	#Clear documentation can make new users easily understand what it happening and prevents hours of debugging
	#Write good code, then the documentation only needs to focus on the core components

#5. Comments
	#Summmarize content, 
	#Does the comment provide necessary information? -Ask yourself this
	#Inline comments are written on the same line. Good to note exceptions, provide example or explain something
	#Docstring is a google-style comments. Useful for complex or heavy functions. Uses triple qoutations for convention
	#help(FUNCTIONNAME) will return the docstring. Docstrings are essentially documentation, not just a comment
	#FUNCTION.__doc__ will return the docstring. Docstrings are saved as a unique piece of information

#6. Best practices
	#Make comments after your code works, otherwise you will need to maintain during development
	#One statement per line is clear and readable


