# grbl_motion.py
# Motion control utilities for GRBL
#
# The MIT License (MIT)
# 
# Copyright (c) 2016 Evil Mad Scientist Laboratories
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import grbl_serial
import inkex

class GrblMotion(object):
        def __init__(self, port, stepsPerInch, penUpPosition, penDownPosition):
                self.port = port
                self.stepsPerInch = stepsPerInch
                self.penUpPosition = penUpPosition
                self.penDownPosition = penDownPosition
                
        def IsPausePressed(self):
	        if (self.port is not None):
		        return False; # TODO

        def sendPenUp(self, PenDelay):
	        if (self.port is not None):
		        strOutput = 'M3 S' + str(self.penUpPosition) + '\r'
		        self.port.command(strOutput)
		        strOutput = 'G4 P' + str(PenDelay/1000.0) + '\r'
		        self.port.command(strOutput)

        def sendPenDown(self, PenDelay):
	        if (self.port is not None):
		        strOutput = 'M3 S' + str(self.penDownPosition) + '\r'
		        self.port.command(strOutput)
		        strOutput = 'G4 P' + str(PenDelay/1000.0) + '\r'
		        self.port.command(strOutput)

        def doXYMove(self, deltaX, deltaY, duration):
	        if (self.port is not None):
                        moveX = deltaX/self.stepsPerInch*25.4
                        moveY = -deltaY/self.stepsPerInch*25.4
                        maxMove = max(abs(moveX), abs(moveY))
                        rate = int(maxMove/(duration/60000.0))
		        strOutput = 'G1 F' + str(rate) + ' X'+str(moveX) + ' Y'+str(moveY) + '\r'
		        self.port.command(strOutput)
