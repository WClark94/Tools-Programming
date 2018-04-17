import maya.cmds as mc

cU = mc.currentUnit(f=True, query= True, l = True)

myWin = mc.window(title = "Scale Helper", wh = (512,512))
col = mc.columnLayout(adjustableColumn = True)

#MenuBar
mc.menuBarLayout()
mc.menu(label = "Help", helpMenu = True)
mc.menuItem(label = "Help on Scale Helper", command="helpMenuCmd()")

mc.text(label = "Current Unit: ")
mc.text(label = cU)

mc.button(label = "Close", command = "closeWindow()")
mc.button(label = "Reference Cube", command = "createCube()")

mc.showWindow(myWin)

def closeWindow():
    mc.deleteUI(myWin,window=True)
    
def createCube():
    mc.polyCube(w=100,h=100,d=100,sx=100,sy=100,sz=100)
    
def helpMenuCmd():
    mc.launch(web = "https://github.com/WClark94/Tools-Programming/blob/master/Maya%20Tools/Scaling%20Tool/README.md")