import maya.cmds as mc
import OptionsWindowBaseClass

class scaleHelperTool(OptionsWindowBaseClass.OptionsWindow):
    
    def __init__(self):
        OptionsWindowBaseClass.OptionsWindow.__init__(self)
        self.title="Scale Helper Tool"
        self.actionName="Create Reference Cube"
        self.applyName="Delete Reference Cube"
        self.freezeName="Freeze Transforms"
        self.historyName="Delete History"
        
    def displayOptions(self):
        col = mc.columnLayout(adjustableColumn = True)
        cU = mc.currentUnit(f=True, query= True, l = True)
        self.staticText = mc.text(label = "Current Unit: ")
        self.unitText = mc.text(label=cU)
        
        mc.separator(h=20, style="none")
        
        mc.button(label=self.freezeName,height=self.commonBtnSize[1],command=self.freezeBtnCmd)
        mc.button(label=self.historyName, height=self.commonBtnSize[1],command=self.historyBtnCmd)
        
        mc.setParent(self.optionsForm)
        
        
    def actionCmd(self,*args):
        cubey = mc.polyCube(w=100,h=100,sx=100,sy=100,sz=100)
        
    def applyBtnCmd(self,*args):
        mc.delete(cubey)
        
    def freezeBtnCmd(self,*args):
        selection = mc.ls(sl=1)
        for obj in selection:
            mc.makeIdentity(a=1,t=1,r=1,s=1,n=0,pn=1)
            
    def historyBtnCmd(self,*args):
        selection = mc.ls(sl=1)
        for obj in selection:
            mc.delete(obj, ch=1)

win = scaleHelperTool()
win.create()