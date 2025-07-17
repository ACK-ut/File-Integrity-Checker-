from app.scan import *

print("---------------------------------")
print("WELCOME TO FILE INTEGRITY CHECKER")
print("---------------------------------")

print("*****************")
print(" ----  !    ---- ")
print("!---   !   !     ")
print("!      !   !     ")
print("!      !    ---- ")
print("*****************")



class SettingsYamlVars:
    settingsYamlArray = Scan.yaml('app/settings/settings.yaml')

    # pathToScan = settingsYamlArray['pathToScan']
    pathToScan = input(" PUT YOUR PATH: ")
    filesListWithHashesTextFilePath = settingsYamlArray['filesListWithHashesTextFilePath']