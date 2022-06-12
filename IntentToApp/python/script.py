import subprocess
import os
import sys

package = "com.thinkseedsystems.intenttoapp"
javaClass = "IntentListeners"


commands = [
    { 'intent': 'com.thinkseedsystems.intent.BTTest1', 'operation': 'Fetches the list of devices connected over A2DP' },
    { 'intent': 'com.thinkseedsystems.intent.BTTest2', 'operation': 'Fetches the list of devices connected over HFP' },
    { 'intent': 'com.thinkseedsystems.intent.BTTest3', 'operation': 'Fetches the list of devices connected over HEADSET' },
    { 'intent': 'com.thinkseedsystems.intent.BTTest4', 'operation': 'Fetches the list of devices connected over HID' },
]

if len(commands) > 0:
    print ("intent: operation")
    i = 0
    for command in commands:
        i = i + 1
        print(str(i) + ". " + command.get("intent") + ": " + command.get("operation"))

    operation = input("Select testcase: ")

    if int (operation) < len(commands):
        print("adb shell am broadcast -a " + commands[int(operation) + 1]['intent'] + " -n " + package + "/." + javaClass)
        os.system("adb shell am broadcast -a " + commands[int(operation) + 1]['intent'] + " -n " + package + "/." + javaClass)

