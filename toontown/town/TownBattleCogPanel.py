from pandac.PandaModules import *
from toontown.battle import BattleProps
from toontown.toonbase import ToontownGlobals
from toontown.toonbase.ToontownBattleGlobals import *
from direct.directnotify import DirectNotifyGlobal
import string
from toontown.suit import Suit
from direct.gui.DirectGui import *
from pandac.PandaModules import *
from toontown.toonbase import TTLocalizer

class TownBattleCogPanel(DirectFrame):
    notify = DirectNotifyGlobal.directNotify.newCategory('TownBattleCogPanel')
    healthColors = (Vec4(0, 1, 0, 1),
     Vec4(1, 1, 0, 1),
     Vec4(1, 0.5, 0, 1),
     Vec4(1, 0, 0, 1),
     Vec4(0.3, 0.3, 0.3, 1))
    healthGlowColors = (Vec4(0.25, 1, 0.25, 0.5),
     Vec4(1, 1, 0.25, 0.5),
     Vec4(1, 0.5, 0.25, 0.5),
     Vec4(1, 0.25, 0.25, 0.5),
     Vec4(0.3, 0.3, 0.3, 0))
    
    def __init__(self, id):
        gui = loader.loadModel('phase_3.5/models/gui/battle_gui')
        DirectFrame.__init__(self, relief=None, image=gui.find('**/ToonBtl_Status_BG'), image_color=Vec4(0.5, 0.5, 0.5, 0.7))
        self.setScale(0.8)
        self.initialiseoptions(TownBattleCogPanel)
        self.levelText = DirectLabel(parent=self, text='', pos=(-0.06, 0, -0.075), text_scale=0.055)
        self.healthBar = None
        self.healthBarGlow = None
        self.hpChangeEvent = None
        self.head = None
        self.maxHP = None
        self.currHP = None
        self.generateHealthBar()
        self.hide()
        gui.removeNode()
        return
        
    def setLevelText(self, level):
        print 'setLevelText'
        self.levelText['text'] = 'Level '+ str(level)

    def setSuitHead(self, suitName):
        print 'setSuitHead'
        self.head = Suit.attachSuitHead(self, suitName)
        self.head.setX(0.1)
        self.head.setZ(0.01)
        print 'end of setSuitHead'
        
    def generateHealthBar(self):
        print 'generateHealthBar'
        model = loader.loadModel('phase_3.5/models/gui/matching_game_gui')
        button = model.find('**/minnieCircle')
        model.removeNode()
        button.setScale(0.5)
        button.setH(180.0)
        button.setColor(self.healthColors[0])
        button.reparentTo(self)
        button.setX(-0.08)
        button.setZ(0.02)
        self.healthBar = button
        glow = BattleProps.globalPropPool.getProp('glow')
        glow.reparentTo(self.healthBar)
        glow.setScale(0.28)
        glow.setPos(-0.005, 0.01, 0.015)
        glow.setColor(self.healthGlowColors[0])
        button.flattenLight()
        self.healthBarGlow = glow
        self.healthBar.hide()
        self.healthCondition = 0 
        print 'done gerating healthbar'

    def updateHealthBar(self, hp, forceUpdate = 0):
        if hp > self.currHP:
            hp = self.currHP
        self.currHP -= hp
        health = float(self.currHP) / float(self.maxHP)
        if health > 0.95:
            condition = 0
        elif health > 0.7:
            condition = 1
        elif health > 0.3:
            condition = 2
        elif health > 0.05:
            condition = 3
        elif health > 0.0:
            condition = 4
        else:
            condition = 5
        if self.healthCondition != condition or forceUpdate:
            self.healthBar.setColor(self.healthColors[condition], 1)
            self.healthBarGlow.setColor(self.healthGlowColors[condition], 1)        
            self.healthCondition = condition

    def setMaxHp(self, hp):
        self.healthBar.show()
        self.maxHP = hp

    def setHp(self, hp):
        print 'setHp'
        self.currHP = hp
        self.updateHealthBar(hp)

    def show(self):
        DirectFrame.show(self)
        
    def cleanup(self):
        self.ignoreAll()
        DirectFrame.destroy(self)