from settings import Settings
# from SimModule import Sim
files_to_update=["main.py","settings.json", "version.json","configs/configs.py", "tags.json"]
sim_uart=1
sim_tx = 20
sim_rx = 21


# sim_rx = 5
sim_baud=115200

clock_sqw = 5
clock_scl = 7
clock_sda   = 6
# alarm = {'am':5,'pm':15,'min':58}
alarm = Settings('alarm').get
def alarm_handler():
    print('Clock Alarmed')
def alarm_handler():
    print('\n  +++++ Alarm Pass Function Triggered! ++++\n')
    try:
        sim = Sim()
        ts = sim.datetime()
        sim.sendSMS(message=f'\n          {ts} Alarm Is Triggered \n')
    except:
        try:
            sim = Sim()
            ts = sim.datetime()
            sim.sendSMS(message=f'{ts} Alarm Is Triggered')
        except:
            print('cant send message')
    

scanStart = 6
scanEnd = 18
daytimeEnd = 19
daytimeStart = 5

batteryPin = 0
BatteryMotorPin = 1 # Green Pin 4
ledsignalPin = 8 # Green Pin 4

myPhoneNumber="919876543210"
whatsapp_key="2890524"
rootpath = 'configs/'            

wifiSSID = 'HGW-5DF528'
wifipassword = 'dayosfamilys'

groundPin = 10
servoPin= 9
feederpin = 9
gatePin = 2
doorPin = 5 # RDM6300 rx
rdm6300Pin = 5 # RDM6300 rx
# doorPin = 21 # RDM6300 rx
doorservoPin = 3 # Buzzer
buzzerPin = 3


# groundPin=10
# y = Pin(groundPin, Pin.OUT)
# gatePin = 2



 # old is 8

# extraServoPin = 1
# 32k
# clock_sqw = 4
# clock_scl = 9
# clock_sda   = 6

# clock_scl = 9
# clock_sda   = 6

# clockpin = 1 # To power the CLock with 3.3v

# motordriver = 1 # not used 
# motordriver = 1 # not used 
# # for ESP32
# clock_sqw = 13
# clock_scl = 12
# clock_sda   = 14


# sim_tx = 32 #blue
# sim_rx = 33












