from pygame import mixer
from datetime import datetime
from time import time


print("This is a alarm for water remider, eye exercise and physical activity")
def soundonloop(file, stopper):
     mixer.init()
     mixer.music.load(file)
     mixer.music.play()
     while True:
          _input_of_user=input()
          if _input_of_user==stopper:
               mixer.music.stop()
               break

def log_now(msg):
     with open("log.txt","a") as f:
          f.write(f"{msg} {datetime.now()}\n")

if __name__=='__main__':
     init_water=time()
     init_eyes=time()
     init_exercise=time()
     watersec=40*60
     eyessec=30*60
     exersec=35*60

     while True:
          if time()-init_water>watersec:
               print("Water drinking time. Type 'drank' to stop the alarm")
               soundonloop("sample.mp3","drank")
               init_water=time()
               log_now("Water drank at")
          if time()-init_eyes>eyessec:
               print("Eyes exercise time. Type 'eydone' to stop the alarm")
               soundonloop("sample.mp3","eydone")
               init_eyes=time()
               log_now("Eye exercise done at")
          if time()-init_exercise>exersec:
               print("Physical exercise time.Type 'phdone' to stop the alarm")
               soundonloop("sample.mp3","phdone")
               init_exercise=time()
               log_now("Physical activity done at")
