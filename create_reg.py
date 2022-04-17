import winreg
import os
from shutil import copyfile

try:
    reg = winreg.ConnectRegistry(None, winreg.HKEY_CLASSES_ROOT)
    key = winreg.CreateKeyEx(reg, 'openapp')
    winreg.SetValue(key, None, winreg.REG_SZ, 'URL:openapp Protocol')
    winreg.SetValueEx(key, 'URL Protocol', 0, winreg.REG_SZ, '')
    shell = winreg.CreateKeyEx(key, 'shell')
    open = winreg.CreateKeyEx(shell, 'open')
    command = winreg.CreateKeyEx(open, 'command')
    var = os.environ["ProgramFiles"]
    app_path = os.path.join(var, 'openapp')
    folder = os.mkdir(app_path)
    exe_path = os.path.join(app_path, 'main.exe')
    copyfile('./dist/main.exe', exe_path)
    winreg.SetValue(command, None, winreg.REG_SZ, f'"{exe_path}" "%1"')

    winreg.FlushKey(key)
except Exception as e:
    print(e)
