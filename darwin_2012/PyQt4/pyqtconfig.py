# Copyright (c) 2011 Riverbank Computing Limited <info@riverbankcomputing.com>
# 
# This file is part of PyQt.
# 
# This file may be used under the terms of the GNU General Public
# License versions 2.0 or 3.0 as published by the Free Software
# Foundation and appearing in the files LICENSE.GPL2 and LICENSE.GPL3
# included in the packaging of this file.  Alternatively you may (at
# your option) use any later version of the GNU General Public
# License if such license has been publicly approved by Riverbank
# Computing Limited (or its successors, if any) and the KDE Free Qt
# Foundation. In addition, as a special exception, Riverbank gives you
# certain additional rights. These rights are described in the Riverbank
# GPL Exception version 1.1, which can be found in the file
# GPL_EXCEPTION.txt in this package.
# 
# If you are unsure which license is appropriate for your use, please
# contact the sales department at sales@riverbankcomputing.com.
# 
# This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
# WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.
#
# This module is intended to be used by the configuration scripts of extension
# modules that %Import PyQt4 modules.


import sipconfig


# These are installation specific values created when PyQt4 was configured.
_pkg_config = {
    'pyqt_bin_dir':      '/private/tmp/BUILD/install/Frameworks/Python.framework/Versions/Current/bin',
    'pyqt_config_args':  'LIBDIR_QT=/private/tmp/BUILD/install/lib INCDIR_QT=/private/tmp/BUILD/install/include MOC=/private/tmp/BUILD/install/bin/moc -q /private/tmp/BUILD/install/bin/qmake -w --no-designer-plugin --confirm-license -b /private/tmp/BUILD/install/Frameworks/Python.framework/Versions/Current/bin -d /private/tmp/BUILD/install/Frameworks/Python.framework/Versions/Current/lib/python2.6/site-packages -v /private/tmp/BUILD/install/Frameworks/Python.framework/Versions/Current/share/sip',
    'pyqt_mod_dir':      '/private/tmp/BUILD/install/Frameworks/Python.framework/Versions/Current/lib/python2.6/site-packages/PyQt4',
    'pyqt_modules':      'QtCore QtGui QtHelp QtMultimedia QtNetwork QtOpenGL QtSql QtSvg QtTest QtXml QtXmlPatterns QtDesigner',
    'pyqt_sip_dir':      '/private/tmp/BUILD/install/Frameworks/Python.framework/Versions/Current/share/sip',
    'pyqt_sip_flags':    '-x VendorID -t WS_MACX -x PyQt_Accessibility -x PyQt_NoPrintRangeBug -t Qt_4_7_1 -x Py_v3 -g',
    'pyqt_version':      0x040806,
    'pyqt_version_str':  '4.8.6',
    'qt_data_dir':       '/private/tmp/BUILD/install',
    'qt_dir':            '/private/tmp/BUILD/install',
    'qt_edition':        'free',
    'qt_framework':      0,
    'qt_inc_dir':        '/private/tmp/BUILD/install/include',
    'qt_lib_dir':        '/private/tmp/BUILD/install/lib',
    'qt_threaded':       1,
    'qt_version':        0x040701,
    'qt_winconfig':      'shared'
}

_default_macros = {
    'AIX_SHLIB':                '',
    'AR':                       'ar cq',
    'CC':                       'gcc',
    'CFLAGS':                   '-pipe',
    'CFLAGS_CONSOLE':           '',
    'CFLAGS_DEBUG':             '-g',
    'CFLAGS_EXCEPTIONS_OFF':    '',
    'CFLAGS_EXCEPTIONS_ON':     '',
    'CFLAGS_MT':                '',
    'CFLAGS_MT_DBG':            '',
    'CFLAGS_MT_DLL':            '',
    'CFLAGS_MT_DLLDBG':         '',
    'CFLAGS_RELEASE':           '-O2',
    'CFLAGS_RTTI_OFF':          '',
    'CFLAGS_RTTI_ON':           '',
    'CFLAGS_SHLIB':             '-fPIC',
    'CFLAGS_STL_OFF':           '',
    'CFLAGS_STL_ON':            '',
    'CFLAGS_THREAD':            '',
    'CFLAGS_WARN_OFF':          '-w',
    'CFLAGS_WARN_ON':           '-Wall -W',
    'CHK_DIR_EXISTS':           'test -d',
    'CONFIG':                   'qt warn_on release app_bundle incremental global_init_link_order lib_version_first plugin_no_soname link_prl',
    'COPY':                     'cp -f',
    'CXX':                      'g++',
    'CXXFLAGS':                 '-pipe',
    'CXXFLAGS_CONSOLE':         '',
    'CXXFLAGS_DEBUG':           '-g',
    'CXXFLAGS_EXCEPTIONS_OFF':  '',
    'CXXFLAGS_EXCEPTIONS_ON':   '',
    'CXXFLAGS_MT':              '',
    'CXXFLAGS_MT_DBG':          '',
    'CXXFLAGS_MT_DLL':          '',
    'CXXFLAGS_MT_DLLDBG':       '',
    'CXXFLAGS_RELEASE':         '-O2',
    'CXXFLAGS_RTTI_OFF':        '',
    'CXXFLAGS_RTTI_ON':         '',
    'CXXFLAGS_SHLIB':           '-fPIC',
    'CXXFLAGS_STL_OFF':         '',
    'CXXFLAGS_STL_ON':          '',
    'CXXFLAGS_THREAD':          '',
    'CXXFLAGS_WARN_OFF':        '-w',
    'CXXFLAGS_WARN_ON':         '-Wall -W',
    'DEFINES':                  '',
    'DEL_FILE':                 'rm -f',
    'EXTENSION_PLUGIN':         '',
    'EXTENSION_SHLIB':          'dylib',
    'INCDIR':                   '',
    'INCDIR_OPENGL':            '/System/Library/Frameworks/OpenGL.framework/Headers 	/System/Library/Frameworks/AGL.framework/Headers/',
    'INCDIR_QT':                '/private/tmp/BUILD/install/include',
    'INCDIR_X11':               '',
    'LFLAGS':                   '-headerpad_max_install_names',
    'LFLAGS_CONSOLE':           '',
    'LFLAGS_CONSOLE_DLL':       '',
    'LFLAGS_DEBUG':             '',
    'LFLAGS_DLL':               '',
    'LFLAGS_OPENGL':            '',
    'LFLAGS_PLUGIN':            '-single_module -dynamiclib',
    'LFLAGS_RELEASE':           '',
    'LFLAGS_RPATH':             '',
    'LFLAGS_SHLIB':             '-single_module -dynamiclib',
    'LFLAGS_SONAME':            '-install_name ',
    'LFLAGS_THREAD':            '',
    'LFLAGS_WINDOWS':           '',
    'LFLAGS_WINDOWS_DLL':       '',
    'LIB':                      '',
    'LIBDIR':                   '',
    'LIBDIR_OPENGL':            '',
    'LIBDIR_QT':                '/private/tmp/BUILD/install/lib',
    'LIBDIR_X11':               '',
    'LIBS':                     '',
    'LIBS_CONSOLE':             '',
    'LIBS_CORE':                '',
    'LIBS_GUI':                 '',
    'LIBS_NETWORK':             '',
    'LIBS_OPENGL':              '-framework OpenGL -framework AGL',
    'LIBS_RT':                  '',
    'LIBS_RTMT':                '',
    'LIBS_THREAD':              '',
    'LIBS_WEBKIT':              '',
    'LIBS_WINDOWS':             '',
    'LIBS_X11':                 '',
    'LINK':                     'g++',
    'LINK_SHLIB':               'g++',
    'LINK_SHLIB_CMD':           '',
    'MAKEFILE_GENERATOR':       'UNIX',
    'MKDIR':                    'mkdir -p',
    'MOC':                      '/private/tmp/BUILD/install/bin/moc',
    'RANLIB':                   'ranlib -s',
    'RPATH':                    '',
    'STRIP':                    ''
}


class Configuration(sipconfig.Configuration):
    """The class that represents PyQt configuration values.
    """
    def __init__(self, sub_cfg=None):
        """Initialise an instance of the class.

        sub_cfg is the list of sub-class configurations.  It should be None
        when called normally.
        """
        if sub_cfg:
            cfg = sub_cfg
        else:
            cfg = []

        cfg.append(_pkg_config)

        sipconfig.Configuration.__init__(self, cfg)


class QtCoreModuleMakefile(sipconfig.SIPModuleMakefile):
    """The Makefile class for modules that %Import QtCore.
    """
    def __init__(self, *args, **kw):
        """Initialise an instance of a module Makefile.
        """
        if "qt" not in kw:
            kw["qt"] = ["QtCore"]

        sipconfig.SIPModuleMakefile.__init__(self, *args, **kw)


class QtGuiModuleMakefile(QtCoreModuleMakefile):
    """The Makefile class for modules that %Import QtGui.
    """
    def __init__(self, *args, **kw):
        """Initialise an instance of a module Makefile.
        """
        if "qt" not in kw:
            kw["qt"] = ["QtCore", "QtGui"]

        QtCoreModuleMakefile.__init__(self, *args, **kw)


class QtHelpModuleMakefile(QtGuiModuleMakefile):
    """The Makefile class for modules that %Import QtHelp.
    """
    def __init__(self, *args, **kw):
        """Initialise an instance of a module Makefile.
        """
        if "qt" not in kw:
            kw["qt"] = ["QtCore", "QtGui", "QtHelp"]

        QtGuiModuleMakefile.__init__(self, *args, **kw)


class QtMultimediaModuleMakefile(QtGuiModuleMakefile):
    """The Makefile class for modules that %Import QtMultimedia.
    """
    def __init__(self, *args, **kw):
        """Initialise an instance of a module Makefile.
        """
        if "qt" not in kw:
            kw["qt"] = ["QtCore", "QtGui", "QtMultimedia"]

        QtGuiModuleMakefile.__init__(self, *args, **kw)


class QtNetworkModuleMakefile(QtCoreModuleMakefile):
    """The Makefile class for modules that %Import QtNetwork.
    """
    def __init__(self, *args, **kw):
        """Initialise an instance of a module Makefile.
        """
        if "qt" not in kw:
            kw["qt"] = ["QtCore", "QtNetwork"]

        QtCoreModuleMakefile.__init__(self, *args, **kw)


class QtDeclarativeModuleMakefile(QtNetworkModuleMakefile):
    """The Makefile class for modules that %Import QtDeclarative.
    """
    def __init__(self, *args, **kw):
        """Initialise an instance of a module Makefile.
        """
        if "qt" not in kw:
            kw["qt"] = ["QtCore", "QtGui", "QtNetwork", "QtDeclarative"]

        QtNetworkModuleMakefile.__init__(self, *args, **kw)


class QtAssistantModuleMakefile(QtNetworkModuleMakefile):
    """The Makefile class for modules that %Import QtAssistant.
    """
    def __init__(self, *args, **kw):
        """Initialise an instance of a module Makefile.
        """
        if "qt" not in kw:
            kw["qt"] = ["QtCore", "QtGui", "QtNetwork", "QtAssistant"]

        QtNetworkModuleMakefile.__init__(self, *args, **kw)


class QtOpenGLModuleMakefile(QtGuiModuleMakefile):
    """The Makefile class for modules that %Import QtOpenGL.
    """
    def __init__(self, *args, **kw):
        """Initialise an instance of a module Makefile.
        """
        kw["opengl"] = 1

        if "qt" not in kw:
            kw["qt"] = ["QtCore", "QtGui", "QtOpenGL"]

        QtGuiModuleMakefile.__init__(self, *args, **kw)


class QtScriptModuleMakefile(QtCoreModuleMakefile):
    """The Makefile class for modules that %Import QtScript.
    """
    def __init__(self, *args, **kw):
        """Initialise an instance of a module Makefile.
        """
        if "qt" not in kw:
            kw["qt"] = ["QtCore", "QtScript"]

        QtCoreModuleMakefile.__init__(self, *args, **kw)


class QtScriptToolsModuleMakefile(QtScriptModuleMakefile):
    """The Makefile class for modules that %Import QtScriptTools.
    """
    def __init__(self, *args, **kw):
        """Initialise an instance of a module Makefile.
        """
        if "qt" not in kw:
            kw["qt"] = ["QtCore", "QtGui", "QtScript", "QtScriptTools"]

        QtScriptModuleMakefile.__init__(self, *args, **kw)


class QtSqlModuleMakefile(QtGuiModuleMakefile):
    """The Makefile class for modules that %Import QtSql.
    """
    def __init__(self, *args, **kw):
        """Initialise an instance of a module Makefile.
        """
        if "qt" not in kw:
            kw["qt"] = ["QtCore", "QtGui", "QtSql"]

        QtGuiModuleMakefile.__init__(self, *args, **kw)


class QtSvgModuleMakefile(QtGuiModuleMakefile):
    """The Makefile class for modules that %Import QtSvg.
    """
    def __init__(self, *args, **kw):
        """Initialise an instance of a module Makefile.
        """
        if "qt" not in kw:
            kw["qt"] = ["QtCore", "QtGui", "QtSvg"]

        QtGuiModuleMakefile.__init__(self, *args, **kw)


class QtTestModuleMakefile(QtGuiModuleMakefile):
    """The Makefile class for modules that %Import QtTest.
    """
    def __init__(self, *args, **kw):
        """Initialise an instance of a module Makefile.
        """
        if "qt" not in kw:
            kw["qt"] = ["QtCore", "QtGui", "QtTest"]

        QtGuiModuleMakefile.__init__(self, *args, **kw)


class QtWebKitModuleMakefile(QtNetworkModuleMakefile):
    """The Makefile class for modules that %Import QtWebKit.
    """
    def __init__(self, *args, **kw):
        """Initialise an instance of a module Makefile.
        """
        if "qt" not in kw:
            kw["qt"] = ["QtCore", "QtGui", "QtNetwork", "QtWebKit"]

        QtNetworkModuleMakefile.__init__(self, *args, **kw)


class QtXmlModuleMakefile(QtCoreModuleMakefile):
    """The Makefile class for modules that %Import QtXml.
    """
    def __init__(self, *args, **kw):
        """Initialise an instance of a module Makefile.
        """
        if "qt" not in kw:
            kw["qt"] = ["QtCore", "QtXml"]

        QtCoreModuleMakefile.__init__(self, *args, **kw)


class QtXmlPatternsModuleMakefile(QtCoreModuleMakefile):
    """The Makefile class for modules that %Import QtXmlPatterns.
    """
    def __init__(self, *args, **kw):
        """Initialise an instance of a module Makefile.
        """
        if "qt" not in kw:
            kw["qt"] = ["QtCore", "QtXmlPatterns"]

        QtCoreModuleMakefile.__init__(self, *args, **kw)


class phononModuleMakefile(QtGuiModuleMakefile):
    """The Makefile class for modules that %Import phonon.
    """
    def __init__(self, *args, **kw):
        """Initialise an instance of a module Makefile.
        """
        if "qt" not in kw:
            kw["qt"] = ["QtCore", "QtGui", "phonon"]

        QtGuiModuleMakefile.__init__(self, *args, **kw)


class QtDesignerModuleMakefile(QtGuiModuleMakefile):
    """The Makefile class for modules that %Import QtDesigner.
    """
    def __init__(self, *args, **kw):
        """Initialise an instance of a module Makefile.
        """
        if "qt" not in kw:
            kw["qt"] = ["QtCore", "QtGui", "QtDesigner"]

        QtGuiModuleMakefile.__init__(self, *args, **kw)


class QAxContainerModuleMakefile(QtGuiModuleMakefile):
    """The Makefile class for modules that %Import QAxContainer.
    """
    def __init__(self, *args, **kw):
        """Initialise an instance of a module Makefile.
        """
        if "qt" not in kw:
            kw["qt"] = ["QtCore", "QtGui", "QAxContainer"]

        QtGuiModuleMakefile.__init__(self, *args, **kw)
