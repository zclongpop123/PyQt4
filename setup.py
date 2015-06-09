#========================================
# author: changlong.zang
#   mail: zclongpop@163.com
#   date: Tue, 09 Jun 2015 10:49:09
#========================================
import string, os, inspect, tempfile
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
THIS_DIR     = os.path.dirname(inspect.getfile(inspect.currentframe()))
MAYA_APP_DIR = os.path.join(os.environ.get('USERPROFILE'), 'Documents', 'maya')

SETUP_MEL_PATH = os.path.join(MAYA_APP_DIR or THIS_DIR, 'scripts', 'userSetup.mel')
MEL_STRING_DATA = string.replace("python(\"import imp;imp.load_source('temp', '%s')\");"%os.path.join(THIS_DIR, 'userSetup.py'), '\\', '/')

with open(SETUP_MEL_PATH, 'w') as f:
    f.write(MEL_STRING_DATA)

os.system('explorer.exe %s'%os.path.normcase(os.path.dirname(SETUP_MEL_PATH)))