echo "Hello World"

# echo is basically just a print function

___________________________________________________________________________

set msg="hello world"
echo %msg%

#set creates a variable, then we need % on either side of the variable to call it

___________________________________________________________________________

help dir
#typing help and then calling a function will explain that function

___________________________________________________________________________

doskey sublime="C:\Program Files\Sublime Text\sublime_text.exe"

# doskey and add an application filepath as a variable. Then type in the variable name to open the application

___________________________________________________________________________

type D:\VFX\assets_and_courses\courses\Advanced_python_course\1_Tools\python_scripts\001_test.py

#type and then a path with a document will display everything inside

___________________________________________________________________________

md D:\VFX\assets_and_courses\courses\Advanced_python_course\assets

#md allows us to create a new directory, adding folders when we need them

___________________________________________________________________________

move D:\VFX\assets_and_courses\courses\Advanced_python_course\old_folder\mermaid_image.jpg D:\VFX\assets_and_courses\courses\Advanced_python_course\new_folder\mermaid_image.jpg

#move then add the initial location, then add the new location, the item will move

___________________________________________________________________________

copy D:\VFX\assets_and_courses\courses\Advanced_python_course\hello_world.txt D:\VFX\assets_and_courses\courses\Advanced_python_course\goodbye_world.txt

#copy then add filepath, and also new filepath with new name at the end. Will duplicate it

___________________________________________________________________________

del D:\VFX\assets_and_courses\courses\Advanced_python_course\hello_world.txt

#deletes item described in the filepath

___________________________________________________________________________

cd r"C:\Program Files\RawTherapee\5.9\rawtherapee.exe"
start rawtherapee.exe

#gives a filepath to the application and then uses the start function to execute it

___________________________________________________________________________

taskkill /PID 9764

#kills a task using process ID (PID), which is labelled in task manager

___________________________________________________________________________

python D:\VFX\assets_and_courses\courses\Advanced_python_course\1_Tools\python_scripts\001_test.py

#python plus a filepath to a python application will execute the python script