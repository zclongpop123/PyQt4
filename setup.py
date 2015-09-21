#========================================
# author: changlong.zang
#   mail: zclongpop@163.com
#   date: Tue, 09 Jun 2015 10:49:09
#========================================
import string, os, inspect, tempfile
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
THIS_DIR     = os.path.dirname(inspect.getfile(inspect.currentframe())) or os.getcwd()
SETUP_MEL_DIR = os.path.join(os.path.expanduser('~'), 'Documents', 'maya', 'scripts')

SETUP_MEL_PATH = os.path.join(SETUP_MEL_DIR or THIS_DIR, 'userSetup.mel')
MEL_STRING_DATA = string.replace("python(\"import imp;imp.load_source('temp', '%s')\");"%os.path.join(THIS_DIR, 'userSetup.py'), '\\', '/')

with open(SETUP_MEL_PATH, 'w') as f:
    f.write(MEL_STRING_DATA)

os.system('explorer.exe %s'%os.path.normcase(os.path.dirname(SETUP_MEL_PATH)))