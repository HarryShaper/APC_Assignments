#12.SHELL

#1A) MAKE TEST FOLDER

md D:\VFX\assets_and_courses\courses\Advanced_python_course\test

#_________________________________________________________________________

#1B) MAKE A .PY FILE WITH TEXT INSIDE


#_________________________________________________________________________


#1C) RENAME .PY FILE

ren D:\VFX\assets_and_courses\courses\Advanced_python_course\test_print.py new_test_print.py

#_________________________________________________________________________


#1D) LIST WHAT IS IN THE SHELL_TEST_DIRECTORY WITH PERMISSION INCLUDED


icacls D:\VFX\assets_and_courses\courses\Advanced_python_course\shell_test ##Checks permissions
icacls D:\VFX\assets_and_courses\courses\Advanced_python_course\shell_test /grant "harry shaper":r ##Grants permission to my user

type "D:\VFX\assets_and_courses\courses\Advanced_python_course\shell_test"

#_________________________________________________________________________

#1E) Execute the python file and call the simple print

doskey test="D:\VFX\assets_and_courses\courses\Advanced_python_course\shell_test\test.py" ##Makes "test" into a call function for the .py file

#_________________________________________________________________________

#1F) Execute the python file and call the simple print

del D:\VFX\assets_and_courses\courses\Advanced_python_course\shell_test\test.py ##Remove the python file
rmdir D:\VFX\assets_and_courses\courses\Advanced_python_course\shell_test\test_folder ##Remove a directory

#_________________________________________________________________________

#2a) Starts a DCC of your choice

Nuke.bat

#2b) Adds custom scripts path