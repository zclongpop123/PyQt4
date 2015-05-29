#========================================
# author: changlong.zang
#   mail: zclongpop@163.com
#   date: Fri, 10 Apr 2015 14:40:05
#========================================
import sys, inspect, os.path, re, maya.cmds
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
QT_ROOT_PATH = os.path.dirname(inspect.getfile(inspect.currentframe()))

#- get maya version
Maya_product = maya.cmds.about(p=True)
Maya_version = re.search('\d+$', Maya_product).group()

#- get matched pyqt path
Qt_path = os.path.normcase(os.path.join(QT_ROOT_PATH, '%s_%s'%(sys.platform, Maya_version)))

#- add pyqt path to system path
Qt_path in sys.path or sys.path.append(Qt_path)