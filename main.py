from app.main_operations import *
from app.settings_yaml_vars import *

while True:
    # OPERATION CHOICE
    choiceOfOperation = input('FIC>> ')

    # OPERATION EXECUTION
    if choiceOfOperation=="help":
        MainOperations.help()
    elif choiceOfOperation=="init":
        print("The hashes of the files : ")
        MainOperations.init(SettingsYamlVars.pathToScan, SettingsYamlVars.filesListWithHashesTextFilePath)
    elif choiceOfOperation=="update":
        MainOperations.update(SettingsYamlVars.pathToScan, SettingsYamlVars.filesListWithHashesTextFilePath)
    elif choiceOfOperation=="exit":
        print('You may rest and have some tea.........!')

        print("      ---------      ")
        print("      !       !      ")
        print("   ---------------   ")
        print("       @    @        ")
        print("         <           ")
        print("         O           ")
        break
    elif choiceOfOperation=="":
        pass
    else:
        print("Unknown option, type help to show all avaible commands.")