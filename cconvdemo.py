#!/usr/bin/env python3

# import sys
# from PyQt5.QtCore import QObject
# from PyQt5.QtGui import QGuiApplication
# from PySide2.QtWidgets import QApplication
# from PyQt5.QtQml import QQmlApplicationEngine
# from PyQt5.QtCore import QUrl, pyqtProperty, pyqtSlot, pyqtSignal, QVariant

import sys
from PySide2.QtWidgets import QApplication
from PyQt5.QtCore import QObject
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QUrl, pyqtProperty, pyqtSlot, pyqtSignal, QVariant

from csine import Sine
from cpulse import Pulse
from ccosine import Cosine
from cimpulse import Impulse
from cgaussian import Gaussian
from cexponential import Exponential


class CconvDemo(QObject):
    def __init__(self):
        QObject.__init__(self)
        
        self.sine_y, self.sine_t = [], []
        self.pulse_y, self.pulse_t = [], []
        self.cosine_y, self.cosine_t = [], []
        self.impulse_y, self.impulse_t = [], []
        self.gaussian_y, self.gaussian_t = [], []
        self.exponential_y, self.exponential_t = [], []
        
        self.getx_y, self.getx_t = [], []
        self.getx_y, self.getx_t = [], []
        
        self.geth_y, self.geth_t = [], []
        self.geth_y, self.geth_t = [], []
           
        self.sineObj = Sine()
        self.pulseObj = Pulse()
        self.cosineObj = Cosine()
        self.impulseObj = Impulse()
        self.gaussianObj = Gaussian()        
        self.exponentialObj = Exponential()
        
        
    ###############################   Pulse Signal  ##########################
    ########################################################################## 
         
    pulse_y_sig = pyqtSignal(list)
    pulse_t_sig = pyqtSignal(list)
    
    def setPulse_y(self, pulse):
        if self.pulse_y != pulse:
            self.pulse_y = pulse
        self.pulse_y_sig.emit(self.pulse_y)
    
    def getPulse_y(self):
        return self.pulse_y
    
    def setPulse_t(self, t):
        if self.pulse_t != t:
            self.pulse_t = t
        self.pulse_t_sig.emit(self.pulse_t)
    
    def getPulse_t(self):
        return self.pulse_t
    
    @pyqtSlot(int, int, int)
    def pul(self, amplitude, width , delay):
        self.pulseObj.pulse(amplitude, width, delay)
        self.setPulse_y(self.pulseObj.y.tolist())
        self.setPulse_t(self.pulseObj.t.tolist())
    
    # pyqt properties
    sig_pul_y = pyqtProperty(list, getPulse_y, notify=pulse_y_sig)
    sig_pul_t = pyqtProperty(list, getPulse_t, notify=pulse_t_sig)    
        
    ###############################   Sine Signal  ###########################
    ##########################################################################
    
    sine_y_sig = pyqtSignal(list)
    sine_t_sig = pyqtSignal(list)
    
    def setSine_y(self, sine):
        if self.sine_y != sine:
            self.sine_y = sine
        self.sine_y_sig.emit(self.sine_y)
    
    def getSine_y(self):
        return self.sine_y
    
    def setSine_t(self, t):
        if self.sine_t != t:
            self.sine_t = t
        self.sine_t_sig.emit(self.sine_t)
    
    def getSine_t(self):
        return self.sine_t
    
    @pyqtSlot(int, int, int, int, int)
    def sin(self, amplitude, period, phase, length, delay):
        self.sineObj.sine(amplitude, period, phase, length, delay)
        self.setSine_y(self.sineObj.y.tolist())
        self.setSine_t(self.sineObj.t.tolist())
    
    # pyqt properties
    sig_sin_y = pyqtProperty(list, getSine_y, notify=sine_y_sig)
    sig_sin_t = pyqtProperty(list, getSine_t, notify=sine_t_sig)
    
    ##############################   Cosine Signal  ##########################
    ##########################################################################
    cosine_y_sig = pyqtSignal(list)
    cosine_t_sig = pyqtSignal(list)
    
    def setCosine_y(self, cos):
        if self.cosine_y != cos:
            self.cosine_y = cos
        self.cosine_y_sig.emit(self.cosine_y)
        
    def getCosine_y(self):
        return self.cosine_y
    
    def setCosine_t(self, t):
        if self.cosine_t != t:
            self.cosine_t = t 
        self.cosine_t_sig.emit(self.cosine_t)
        
    def getCosine_t(self):
        return self.cosine_t
    
    # get cosine parameters (amp, period, phase, length, delay)
    @pyqtSlot(int, int, int, int, int)
    def cos(self, amplitude, period, phase, length, delay):
        self.cosineObj.cosine(amplitude, period, phase, length, delay)
        self.setCosine_y(self.cosineObj.y.tolist())
        self.setCosine_t(self.cosineObj.t.tolist())
              
    # pyqt properties
    sig_cos_y = pyqtProperty(list, getCosine_y, notify=cosine_y_sig)
    sig_cos_t = pyqtProperty(list, getCosine_t, notify=cosine_t_sig)
    
    ##############################   Gaussian Signal  ##########################
    ##########################################################################
         
    gaussian_y_sig = pyqtSignal(list)
    gaussian_t_sig = pyqtSignal(list)
    
    def setGaussian_y(self, gaus):
        if self.gaussian_y != gaus:
            self.gaussian_y = gaus
        self.gaussian_y_sig.emit(self.gaussian_y)
    
    def getGaussian_y(self):
        return self.gaussian_y
    
    def setGaussian_t(self, t):
        if self.gaussian_t != t:
            self.gaussian_t = t
        self.gaussian_t_sig.emit(self.gaussian_t)
    
    def getGaussian_t(self):
        return self.gaussian_t
    
    @pyqtSlot(int, float, int, int)
    def gauss(self, scalingFactor, expConstant, length, delay):
        self.gaussianObj.gaussian(scalingFactor, expConstant, length, delay)
        self.setGaussian_y(self.gaussianObj.y.tolist())
        self.setGaussian_t(self.gaussianObj.t.tolist())
    
    # pyqt properties
    sig_gaus_y = pyqtProperty(list, getGaussian_y, notify=gaussian_y_sig)
    sig_gaus_t = pyqtProperty(list, getGaussian_t, notify=gaussian_t_sig)  
    
    ###########################   Exponential Signal  ########################
    ##########################################################################
         
    exponential_y_sig = pyqtSignal(list)
    exponential_t_sig = pyqtSignal(list)
    
    def setExponential_y(self, expo):
        if self.exponential_y != expo:
            self.exponential_y = expo
        self.exponential_y_sig.emit(self.exponential_y)
    
    def getExponential_y(self):
        return self.exponential_y
    
    def setExponential_t(self, t):
        if self.exponential_t != t:
            self.exponential_t = t
        self.exponential_t_sig.emit(self.exponential_t)
    
    def getExponential_t(self):
        return self.exponential_t
    
    @pyqtSlot(int, float, int, int, str)
    def expo(self, scalingFactor, expConstant, length, delay, causality):
        self.exponentialObj.exponential(scalingFactor,expConstant, length, delay, causality)
        self.setExponential_y(self.exponentialObj.y.tolist())
        self.setExponential_t(self.exponentialObj.t.tolist())
    
    # pyqt properties
    sig_exp_y = pyqtProperty(list, getExponential_y, notify=exponential_y_sig)
    sig_exp_t = pyqtProperty(list, getExponential_t, notify=exponential_t_sig)
    
    ############################  GET_X_SIGNAL  ##############################
    ##########################################################################
     
    getx_y_sig = pyqtSignal(list);
    getx_t_sig = pyqtSignal(list);
    
    
    def setGetx_y(self, getx):
        if self.getx_y != getx:
            self.getx_y = getx
        self.getx_y_sig.emit(self.getx_y)
    
    def getGetx_y(self):
        return self.getx_y
    
    def setGetx_t(self, t):
        if self.getx_t != t:
            self.getx_t = t
        self.getx_t_sig.emit(self.getx_t)
    
    def getGetx_t(self):
        return self.getx_t
     
    @pyqtSlot(list, list)
    def getxx(self,y , t):
        self.setGetx_y(y)
        self.setGetx_t(t)
        
    sig_getx_y = pyqtProperty(list, getGetx_y, notify=getx_y_sig)
    sig_getx_t = pyqtProperty(list, getGetx_t, notify=getx_t_sig)  
    
    ############################  GET_H_SIGNAL  ##############################
    ##########################################################################
     
    geth_y_sig = pyqtSignal(list);
    geth_t_sig = pyqtSignal(list);
    
    
    def setGeth_y(self, geth):
        if self.geth_y != geth:
            self.geth_y = geth
        self.geth_y_sig.emit(self.geth_y)
    
    def getGeth_y(self):
        return self.geth_y
    
    def setGeth_t(self, t):
        if self.geth_t != t:
            self.geth_t = t
        self.geth_t_sig.emit(self.geth_t)
    
    def getGeth_t(self):
        return self.geth_t
     
    @pyqtSlot(list, list)
    def gethh(self,y , t):
        self.setGeth_y(y)
        self.setGeth_t(t)
        
    sig_geth_y = pyqtProperty(list, getGeth_y, notify=geth_y_sig)
    sig_geth_t = pyqtProperty(list, getGeth_t, notify=geth_t_sig)
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()
    ccdemo = CconvDemo()
    #ccdemo.cos(5, 14, 0, 10, 0)
    engine.rootContext().setContextProperty("ccdemo",ccdemo)
    engine.load(QUrl("Cconvdemo.qml"))
    sys.exit(app.exec_())

