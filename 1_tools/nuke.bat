::  ******    FIRST BATCH PROGRAM FOR NUKE     ****
::  ***   MADE BY: HARRY SHAPER - SHAPERVFX.COM  **

:: OPENS NUKE

::*********************************

@echo off


:: PATH


:: set Nuke Version Variable
set "NUKE_VERSION=16.0"

::Set Variable + other
set "NUKE_PLUG_IN_PATH=C:\Program Files\Nuke16.0v1\plugins;%NUKE_PLUG_IN_PATH%"

:: Set custom scripts path
set "SCRIPT_PATH=D:\VFX\assets_and_courses\courses\Advanced_python_course\1_Tools\python_scripts\"


:: Start Nuke
start "" "C:\Program Files\Nuke16.0v1\Nuke16.0.exe"

:: close command promp
exit