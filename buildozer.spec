[app]

# (str) Title of your application
title = My Kivy App

# (str) Package name
package.name = mykivyapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py is located
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = spec

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (list) List of service to declare
#services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

# (str) The entry point of your application
entrypoint = main.py

# (str) The architecture to target
#android.arch = armeabi-v7a
# (str) Custom source folders for requirements
# Set custom source folders for any requirement to be build from your own sources.
# The source folder must contain a __init__.py or a path to the repository (github or mercurial).
# e.g. requirements.source.kivy = ../kivy
# requirements.source.my_package = git@github.com:my_account/my_package

# (bool) Enable debug mode
#android.debug = 1

# (str) The release configuration to use
#android.release = 1
