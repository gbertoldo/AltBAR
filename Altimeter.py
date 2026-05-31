import math
import numpy as np
import os
import subprocess

# Define the flag for Windows
# This flag is specific to the Windows API
CREATE_NO_WINDOW = 0x08000000

class FlightData:
    def __init__(self):
        self.apogee         = 0.0
        self.basePressure   = 0.0
        self.apogeePressure = 0.0
        self.baseAltitude   = 0.0
        self.apogeeAltitude = 0.0
        self.t = np.array([])
        self.h = np.array([])
        self.H = np.array([])
        self.p = np.array([])

class Altimeter:
    def __init__(self, observer):
        self.clear()
        self.observer = observer
        pass

    def clear(self):
        self.dataFlight = FlightData()  
       
    def getReport(self):
        rep=[]
        rep.append("#")
        rep.append("# AltBAR")
        rep.append("#")
        rep.append("# Apogeu (m): %9.2f"%(self.dataFlight.apogee))
        rep.append("#")
        rep.append("#    t (s)    h (m)")
        for i in range(0,len(self.dataFlight.t)):
            rep.append("%9.3f %9.2f"%(self.dataFlight.t[i], self.dataFlight.h[i]))
        txt = ""
        for item in rep:
            txt = txt + item + "\n"
        return txt

    def processFlightData(self):

        fd = FlightData()

        fname = 'flight_data_true.txt'
        lines = []
        with open(fname, 'r') as file:
            for line in file:
                lines.append(line.rstrip('\n').replace(',','.'))

        fd.basePressure   = float(lines[1])
        fd.apogeePressure = float(lines[2])
        time = []
        pressure = []
        i = 6
        while (i < len(lines)):
            time.append(0.192*(i-6))
            try:
                pressure.append(float(lines[i]))
            except:
                pass
            i=i+1
        fd.t = np.array(time)
        fd.p = np.array(pressure)
        
        fd.baseAltitude   = self.pressureToAltitude(fd.basePressure)
        fd.apogeeAltitude = self.pressureToAltitude(fd.apogeePressure)
        fd.apogee = fd.apogeeAltitude-fd.baseAltitude
        H = []
        h = []
        for i in range(0,len(pressure)):
            H.append(self.pressureToAltitude(pressure[i]))
            h.append(H[-1]-fd.baseAltitude)
        fd.H = np.array(H)
        fd.h = np.array(h)
        return fd    

    def pressureToAltitude(self,P):
        Tb=288.15
        Lb=-0.0065
        R=8.31432
        g=9.80665
        M=0.0289644
        Pb=101325.0
        h=(Tb/Lb)*(math.pow(P/Pb,-R*Lb/(g*M))-1)
        return h
   
    def removeFiles(self):
        ifiles = ["eeprom_contents.txt", "eeprom_contents.bin", "flight_data_true.txt", "flight_data_raw.txt", "timestamps.txt"]
        for item in ifiles:
            if os.path.exists(item):
                os.remove(item)

    def readEEPROM(self):
        commands =[]       
        commands.append(["./bin/avrdude.exe", "-C", "./bin/avrdude.conf", "-c", "usbasp", "-p", "attiny85", "-B", "31.25", "-P", "usb", "-b", "19200", "-U", "eeprom:r:eeprom_contents.bin:r"])
        commands.append(["./bin/avrdude.exe", "-C", "./bin/avrdude.conf", "-c", "usbasp", "-p", "attiny85", "-B", "31.25", "-P", "usb", "-b", "19200", "-U", "eeprom:r:eeprom_contents.txt:h"])
        return self.runCommands(commands)

    def runGraphGenerator(self):
        if ((not os.path.exists("eeprom_contents.txt")) or (not os.path.exists("eeprom_contents.bin")) ):
            return False
        exeName = "GraphGenerator.exe"
        exePath = os.path.join(os.getcwd(),"bin")
        command = os.path.join(exePath, exeName)
        return self.runCommands([command])

    def getData(self):
        self.dataFlight = self.processFlightData()
        return [self.dataFlight.t,self.dataFlight.h]
    
    def extractData(self):
        self.removeFiles()

        isSuccess = self.readEEPROM()
        if not isSuccess:
            return
        isSuccess = self.runGraphGenerator()
        if not isSuccess:
            return

    def clearEEPROM(self):
        exeName = "empty.bin"
        exePath = os.path.join(os.getcwd(),"bin")
        binfile = os.path.join(exePath, exeName)
        commands =[]
        commands.append(["./bin/avrdude.exe", "-c", "usbasp", "-p", "attiny85", "-U", "eeprom:w:"+binfile+":r"])
        return self.runCommands(commands)

    def writeFirmware(self):
        exeName = "MainDev.hex"
        exePath = os.path.join(os.getcwd(),"bin")
        binfile = os.path.join(exePath, exeName)
        commands =[]
        commands.append(["./bin/avrdude.exe", "-C", "./bin/avrdude.conf", "-c", "usbasp", "-p", "attiny85", "-B", "31.25", "-P", "usb", "-b", "19200", "-e", "-U", "flash:w:"+binfile+":i"])
        return self.runCommands(commands)

    def runCommands(self, commands):
        isSuccess = True
        for cmd in commands:
            cmdtxt = "Comando:"
            for item in cmd:
                cmdtxt = cmdtxt + " " + item
            cmdtxt = cmdtxt + "\n"

            self.observer.notify(cmdtxt)
 
            try:
                process = subprocess.Popen(
                    cmd, 
                    stdout=subprocess.PIPE, 
                    stderr=subprocess.STDOUT, 
                    text=True, 
                    bufsize=1,
                    creationflags=CREATE_NO_WINDOW
                )
                # Read output line by line
                for line in process.stdout:
                    self.observer.notify(line)
                            
                process.stdout.close()
                process.wait()
            except:
                self.observer.notify("\nFalha ao executar o comando\n")
                process.stdout.close()
                process.wait()
                isSuccess = False
                return isSuccess
        return isSuccess