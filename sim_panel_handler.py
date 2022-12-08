############################
# **** IMPORT SECTION **** #
############################
import sys
import os
import linuxcnc
import hal, hal_glib

from PyQt5 import QtCore, QtWidgets, QtGui

#from qtvcp.widgets.mdi_line import MDILine as MDI_WIDGET
#from qtvcp.widgets.stylesheeteditor import  StyleSheetEditor as SSE
#from qtvcp.lib.keybindings import Keylookup
from qtvcp.core import Status, Action, Info

# Set up logging
from qtvcp import logger
LOG = logger.getLogger(__name__)

# Set the log level for this module
#LOG.setLevel(logger.INFO) # One of DEBUG, INFO, WARNING, ERROR, CRITICAL

###########################################
# **** instantiate libraries section **** #
###########################################

STATUS = Status()
ACTION = Action()
INFO = Info()

###################################
# **** HANDLER CLASS SECTION **** #
###################################

class HandlerClass:

    ########################
    # **** INITIALIZE **** #
    ########################
    # widgets allows access to  widgets from the qtvcp files
    # at this point the widgets and hal pins are not instantiated
    def __init__(self, halcomp,widgets,paths):
        self.hal = halcomp
        self.w = widgets
        self.PATHS = paths
        #self.current_mode = (None,None)
        
    ##########################################
    # Special Functions called from QTSCREEN
    ##########################################

    ########################
    # callbacks from STATUS #
    ########################

    def updateIncrementPin(self, incr):
        self.jog_increment.set(incr)

    #######################
    # callbacks from form #
    #######################

    def btn_zero_all_clicked(self):
        command = "G10 L20 P0 X0 Y0 Z0"
        ACTION.CALL_MDI(command)
        if self.last_loaded_program:
            self.w.progressBar.setValue(0)
            self.add_status("Loaded program file {}".format(self.last_loaded_program))
            ACTION.OPEN_PROGRAM(self.last_loaded_program)

    #####################
    # general functions #
    #####################

    #####################
    # KEY BINDING CALLS #
    #####################

    ###########################
    # **** closing event **** #
    ###########################

    ##############################
    # required class boiler code #
    ##############################

    def __getitem__(self, item):
        return getattr(self, item)
    def __setitem__(self, item, value):
        return setattr(self, item, value)

################################
# required handler boiler code #
################################

def get_handlers(halcomp,widgets,paths):
     return [HandlerClass(halcomp,widgets,paths)]
