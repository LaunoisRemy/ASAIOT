import serial
from threading import Thread
import csv

ser = serial.Serial('/dev/ttyACM0',115200)

class Identif(Thread):
    def __init__(self):
            Thread.__init__(self)
            self.userId = 0
            self.name=""

    def run(self):
            while True :
                    lecture_id = ser.readline()
                    print(lecture_id)
                    self.userId = 1
                    
                    #self.userId = 0
                    """
			with open('users.csv','r') as file :
				str_id =""
				dico={}
				users=file.readline()
				users=users.strip()
				data_id=users.split(";")
				for line in file:
					line=line.strip()
					if(re.search(r'^[0-9x]{35}',line)):
						str_id += line #string de tous les ids
					if(re.search(r'^[A-Z0-9x ]{35};[a-zA-Z]+;[a-zA-Z]+',line)):
						data = line.split(";")
						dico[data[0]]={ data_id[1]: data[1], data_id[2]: data[2]}

			file.closed
        	
        	"""
			# lecture_id = ser.readLine()
                        #      	if (lecture_id in str_id):
                        #self.userId = 1
                        #self.name = dico[lecture_id]
                        
