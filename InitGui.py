#***************************************************************************
#*    Copyright (C) 2024 
#*    This library is free software
#***************************************************************************

import os
import sys
import FreeCAD
import FreeCADGui

class ShapedSteelShowCommand:
    def GetResources(self):
        from Init import module_path
        return { 
          'Pixmap': os.path.join(module_path, 'icons', "ShapedSteel.svg"),
          'MenuText': "ShapedSteel",
          'ToolTip': "Show/Hide ShapedSteel"}

    def IsActive(self):
        import ShapedSteel
        ShapedSteel
        return True

    def Activated(self):
        try:
          import ShapedSteel
          ShapedSteel.main.d.show()
        except Exception as e:
          FreeCAD.Console.PrintError(str(e) + "\n")

    def IsActive(self):
        import ShapedSteel
        #
        return not FreeCAD.ActiveDocument is None

class ShapedSteelWB(FreeCADGui.Workbench):
    def __init__(self):
        from Init import module_path
        self.__class__.Icon = os.path.join(module_path, 'icons', "ShapedSteel.svg")
        self.__class__.MenuText = "ShapedSteel"
        self.__class__.ToolTip = "ShapedSteel by Pascal"

    def Initialize(self):
        self.commandList = ["ShapedSteel_Show"]
        self.appendToolbar("&ShapedSteel", self.commandList)
        self.appendMenu("&ShapedSteel", self.commandList)

    def Activated(self):
        import ShapedSteel
        ShapedSteel
        return

    def Deactivated(self):
        return

    def ContextMenu(self, recipient):
        return

    def GetClassName(self): 
        return "Gui::PythonWorkbench"
    
FreeCADGui.addWorkbench(ShapedSteelWB())
FreeCADGui.addCommand("ShapedSteel_Show", ShapedSteelShowCommand())    

