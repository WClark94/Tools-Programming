import maya.cmds as mc
import OptionsWindowBaseClass

class scaleHelperTool(OptionsWindowBaseClass.OptionsWindow):
    
    def __init__(self):
        OptionsWindowBaseClass.OptionsWindow.__init__(self)
        self.title="Scale Helper Tool" # rename the tool
        self.actionName="Create Scale Ruler" # rename action button
        self.applyName="Delete Scale Ruler" # rename apply name
        self.freezeName="Freeze Transforms" # create name for freeze button
        self.historyName="Delete History" # create name for history deelte button
        
    def displayOptions(self):
        col = mc.columnLayout(adjustableColumn = True) #create column layout for text/extra buttons
        cU = mc.currentUnit(f=True, query= True, l = True) # get the current units in maya session
        self.staticText = mc.text(label = "Current Unit: ") # static text 
        self.unitText = mc.text(label=cU) # create text based on the current units in maya session
        
        mc.separator(h=20, style="none") # separator to make the GUI better
        
        mc.button(label=self.freezeName,height=self.commonBtnSize[1],command=self.freezeBtnCmd) # create a freeze transform button
        mc.button(label=self.historyName, height=self.commonBtnSize[1],command=self.historyBtnCmd) # create a history delete button
        
        mc.setParent(self.optionsForm)
        
        
    def actionCmd(self,*args): # Create a plane, move it off origin by 1, rotate by 90 in X-axis and make it unselectable
        mc.polyPlane(w=100,h=100,sx=100,sy=100, n="cubey")
        mc.move(0,0,1)
        mc.rotate(90,0,0)
        mc.toggle(st=True,te=True)
        
    def applyBtnCmd(self,*args): # delete the plane
        mc.delete("cubey")
        
    def freezeBtnCmd(self,*args): # freeze transforms of selected objects
        selection = mc.ls(sl=1)
        for obj in selection:
            mc.makeIdentity(a=1,t=1,r=1,s=1,n=0,pn=1)
            
    def historyBtnCmd(self,*args): # delete history of selected objects
        selection = mc.ls(sl=1)
        for obj in selection:
            mc.delete(obj, ch=1)

win = scaleHelperTool()
win.create() # create the window
