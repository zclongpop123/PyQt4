PyQt4 for Maya 2012 - 2016
=
将 userSetup.mel 放到  我的文档/maya/scripts 文件夹下（不需要放到版本内的文件夹里面）。
Exp：C:\Users\zangchanglong\Documents\maya\scripts


将 userSetup.mel 文件里的 userSetup.py 路径改为本文件夹路径。
Exp: //bjserver2/WScriptsTool/rig/PyQt4/userSetup.py


maya/201x/scripts 里面如果有 userSetup.mel， maya/scripts 里面的 userSetup.mel 便会对此版本失效。
Exp：C:\Users\zangchanglong\Documents\maya\2015-x64\scripts
 

如果原本有个人的 userSetup.mel, 只需要把里面的mel复制过去就好。注意测试格式是否正确。
