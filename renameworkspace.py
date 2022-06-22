#!/bin/python3
import os

# Get workspace names
x = os.popen('gsettings get org.gnome.desktop.wm.preferences workspace-names').read()

# Get current workspace index 
current_workspace = int(os.popen("xdotool get_desktop").read())

# Create an python array from x
workspaces = x[1:-2].replace("'","").split(", ")
current_name = workspaces[current_workspace]

# Ask for new label
new_name = os.popen(f"zenity --entry --entry-text='{current_name}' --title='Workspace label' --text='New label'").read()

if(new_name == ''):
    print("User cancelled the input, returning..")
else:
    # Set new label in array ([0:-1] to remove \n)
    workspaces[current_workspace] = new_name[0:-1]

    # Apply changes
    os.system(f'gsettings set org.gnome.desktop.wm.preferences workspace-names "{str(workspaces)}"')

    # just to 'debug'
    print(f'gsettings set org.gnome.desktop.wm.preferences workspace-names "{str(workspaces)}"')
