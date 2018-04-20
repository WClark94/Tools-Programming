import maya.cmds as mc

# Get Current Units used by Maya
cU = mc.currentUnit(f=True, query= True, l = True)

#Make Window and layouts
myWin = mc.window(title = "Scale Helper")
col = mc.columnLayout(adjustableColumn = True)

#MenuBar
mc.menuBarLayout()
mc.menu(label = "Help", helpMenu = True)
mc.menuItem(label = "Help on Scale Helper", command="helpMenuCmd()")

# text for displaying maya's current units
mc.text(label = "Current Unit: ")
mc.text(label = cU)

mc.separator(h=20, style="none")

mc.rowLayout(nc = 4, cw=[6,121])
# buttons
mc.button(label = "Close", command = "closeWindow()")
mc.button(label = "Reference Cube", command = "createCube()")
mc.button(label = "Delete History", command="deleteHistory()")
mc.button(label = "Freeze Transforms", command = "freezeTrans()")
#mc.button(label="Change Units To Centimeter", command="currentUnitChange()")

#show window
mc.showWindow(myWin)

# Command Functions
def closeWindow():
    mc.deleteUI(myWin,window=True)
    
def createCube():
    mc.polyCube(w=100,h=100,sx=100,sy=100,sz=100)
    
def helpMenuCmd():
    mc.launch(web = "https://github.com/WClark94/Tools-Programming/blob/master/Maya%20Tools/Scaling%20Tool/README.md")
    
def deleteHistory():
    selection = mc.ls(sl=1)
    for obj in selection:
        mc.delete(obj, ch=1)

def freezeTrans():
    selection = mc.ls(sl=1)
    for obj in selection:
        mc.makeIdentity(a=1,t=1,r=1,s=1,n=0,pn=1)
        
#def currentUnitChange():
#    mc.currentUnit(l="cm")