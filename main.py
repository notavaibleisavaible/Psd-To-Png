import os
import glob
import subprocess
import time

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


if input(f'{colors.FAIL}ALL FILES IN THE FOLDER WILL BE REPLACED, MAKE SURE YOU ARE USING A COPY! TYPE {colors.BOLD}>YES<{colors.ENDC}{colors.FAIL} TO CONTINUE (all caps){colors.ENDC}\n') == 'YES':
    pass
else:
    quit()


DIR = input("Please Input The Files Folder > ")

files = glob.glob(f"./{DIR}/**", recursive=True)

# im not proud of whatever this is
def clean(i):
    if i.endswith('.psd'):
        pass
    else:
        files.remove(i)

for i in files:
    for i in files:
        clean(i)

amount = 0
os.system('clear')
for i in files:
    amount = amount + 1
    subprocess.run(f'psd-tools export {i} {i}.png', shell=True, capture_output=True)
    time.sleep(0.1)
    os.system(f'rm {i}')
    print(f'{colors.OKGREEN}Processed {colors.BOLD}{i}{colors.ENDC}{colors.OKGREEN} ...{colors.ENDC}')

print(f'{colors.OKGREEN}Successfully processed {colors.BOLD}{amount}{colors.ENDC}{colors.OKGREEN} files!{colors.ENDC}')