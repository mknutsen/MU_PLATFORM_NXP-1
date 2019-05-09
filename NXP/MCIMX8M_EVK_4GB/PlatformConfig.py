import os

#
#==========================================================================
# PLATFORM BUILD ENVIRONMENT CONFIGURATION
#
SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
WORKSPACE_PATH = os.path.dirname(os.path.dirname(SCRIPT_PATH))
REQUIRED_REPOS = ('MU_BASECORE','Silicon/ARM/NXP', 'Common/MU','Common/MU_TIANO', 'Common/MU_OEM_SAMPLE','Silicon/ARM/MU_TIANO')
PROJECT_SCOPE = ('imxfamily', 'imx8')

MODULE_PKGS = ('MU_BASECORE','Silicon/ARM/NXP', 'Common/MU','Common/MU_TIANO', 'Common/MU_OEM_SAMPLE','Silicon/ARM/MU_TIANO')
MODULE_PKG_PATHS = os.pathsep.join(os.path.join(WORKSPACE_PATH, pkg_name) for pkg_name in MODULE_PKGS)
