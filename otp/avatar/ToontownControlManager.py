from direct.controls import ControlManager
from direct.showbase.InputStateGlobal import inputState

class ToontownControlManager(ControlManager.ControlManager):
    wantWASD = base.wantWASD
    
    def __init__(self, enable=True, passMessagesThrough = False):
        self.passMessagesThrough = passMessagesThrough
        self.inputStateTokens = []
        self.WASDTurnTokens = []
        self.__WASDTurn = True
        self.controls = {}
        self.currentControls = None
        self.currentControlsName = None
        self.isEnabled = 0
        if enable:
            self.enable()
        self.forceAvJumpToken = None
        self.inputToDisable = []
    
    def enable(self):
        assert self.notify.debugCall(id(self))

        if self.isEnabled:
            assert self.notify.debug('already isEnabled')
            return
        
        self.isEnabled = 1

        # keep track of what we do on the inputState so we can undo it later on
        #self.inputStateTokens = []
        ist = self.inputStateTokens
        ist.append(inputState.watch("run", 'runningEvent', "running-on", "running-off"))
        
        ist.append(inputState.watch("forward", "force-forward", "force-forward-stop"))
        
        
        ist.append(inputState.watchWithModifiers("reverse", "mouse4", inputSource=inputState.Mouse))
        
        if self.wantWASD:
            ist.append(inputState.watchWithModifiers("turnLeft", "arrow_left", inputSource=inputState.ArrowKeys))
            ist.append(inputState.watch("turnLeft", "mouse-look_left", "mouse-look_left-done"))
            ist.append(inputState.watch("turnLeft", "force-turnLeft", "force-turnLeft-stop"))
            
            ist.append(inputState.watchWithModifiers("turnRight", "arrow_right", inputSource=inputState.ArrowKeys))
            ist.append(inputState.watch("turnRight", "mouse-look_right", "mouse-look_right-done"))
            ist.append(inputState.watch("turnRight", "force-turnRight", "force-turnRight-stop"))

            ist.append(inputState.watchWithModifiers("forward", "w", inputSource=inputState.WASD))
            ist.append(inputState.watchWithModifiers("reverse", "s", inputSource=inputState.WASD))

            self.setWASDTurn(self.__WASDTurn)
        else:
            ist.append(inputState.watchWithModifiers("forward", "arrow_up", inputSource=inputState.ArrowKeys))
            ist.append(inputState.watchWithModifiers("reverse", "arrow_down", inputSource=inputState.ArrowKeys))
            ist.append(inputState.watchWithModifiers("turnLeft", "arrow_left", inputSource=inputState.ArrowKeys))
            ist.append(inputState.watch("turnLeft", "mouse-look_left", "mouse-look_left-done"))
            ist.append(inputState.watch("turnLeft", "force-turnLeft", "force-turnLeft-stop"))
            
            ist.append(inputState.watchWithModifiers("turnRight", "arrow_right", inputSource=inputState.ArrowKeys))
            ist.append(inputState.watch("turnRight", "mouse-look_right", "mouse-look_right-done"))
            ist.append(inputState.watch("turnRight", "force-turnRight", "force-turnRight-stop"))

        # Jump controls
        if self.wantWASD:
            ist.append(inputState.watchWithModifiers("jump", "shift"))
        else:
            ist.append(inputState.watch("jump", "control", "control-up"))
        
        if self.currentControls:
            self.currentControls.enableAvatarControls()
            
            
    def setWASDTurn(self, turn):
        self.__WASDTurn = turn

        if not self.isEnabled:
            return
        
        turnLeftWASDSet = inputState.isSet("turnLeft", inputSource=inputState.WASD)
        turnRightWASDSet = inputState.isSet("turnRight", inputSource=inputState.WASD)
        slideLeftWASDSet = inputState.isSet("slideLeft", inputSource=inputState.WASD)
        slideRightWASDSet = inputState.isSet("slideRight", inputSource=inputState.WASD)

        for token in self.WASDTurnTokens:
            token.release()

        if turn:
            self.WASDTurnTokens = (
                inputState.watchWithModifiers("turnLeft", "a", inputSource=inputState.WASD),
                inputState.watchWithModifiers("turnRight", "d", inputSource=inputState.WASD),
                )

            inputState.set("turnLeft", slideLeftWASDSet, inputSource=inputState.WASD)
            inputState.set("turnRight", slideRightWASDSet, inputSource=inputState.WASD)

            inputState.set("slideLeft", False, inputSource=inputState.WASD)
            inputState.set("slideRight", False, inputSource=inputState.WASD)

        else:
            self.WASDTurnTokens = (
                inputState.watchWithModifiers("slideLeft", "a", inputSource=inputState.WASD),
                inputState.watchWithModifiers("slideRight", "d", inputSource=inputState.WASD),
                )

            inputState.set("slideLeft", turnLeftWASDSet, inputSource=inputState.WASD)
            inputState.set("slideRight", turnRightWASDSet, inputSource=inputState.WASD)
                
            inputState.set("turnLeft", False, inputSource=inputState.WASD)
            inputState.set("turnRight", False, inputSource=inputState.WASD)