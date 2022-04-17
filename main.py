import subprocess
import os
import re
import sys


# check codes
# apps = {
#     'pycharm': 'PyCharm Community Edition',
#     'notes': '@explorer.exe shell:appsFolder\Microsoft.MicrosoftStickyNotes_8wekyb3d8bbwe!App',
#     'notepad': 'notepad',
#     'explorer': 'explorer',
#     'downloads': '@explorer.exe shell:Downloads',
#     'docs': '@explorer.exe shell:AppDataDocuments',
#     'apps': '@explorer.exe shell:appsFolder\ '
# }
# check = os.system(f"Run shell:{apps['Microsoft To Do']}")
class Main:
    def __init__(self):
        self.apps: dict = {}  # contain all the apps and paths

    def get_all_apps(self):
        data = subprocess.Popen(['powershell', 'get-StartApps'], stdout=subprocess.PIPE)
        raw_data = data.communicate()[0]
        raw_data = raw_data.decode('UTF-8', errors='ignore')
        return raw_data

    def load_data(self, raw_data: str):
        for i in raw_data.split('\n')[3:]:
            a = re.split(r'\s{2,}', i)
            if len(a) >= 2:
                self.apps[a[0].strip()] = a[1].strip().replace('\r', '')

    def app_path(self, input_var: str) -> str:
        for key in self.apps.keys():
            if input_var.lower() == key.lower():
                return self.apps[key]
        return None

    @staticmethod
    def execute(app_name: str):
        os.system(f"@explorer.exe shell:appsFolder\{app_name}")

    def print_app_info(self):
        print('\n'.join([i for i in self.apps.keys()]))


if __name__ == '__main__':
    input_var = sys.argv[1]
    input_var = input_var.split("//")[-1].replace('/', '')
    input_var = input_var.replace('%20', ' ')
    run = Main()
    app_data = run.get_all_apps()
    run.load_data(app_data)
    if input_var:
        print("coming")
        app_path = run.app_path(input_var)
        if app_path:
            run.execute(app_path)
        else:
            print("not coming")
            run.print_app_info()
    else:
        run.print_app_info()
# test = 'spotify'
