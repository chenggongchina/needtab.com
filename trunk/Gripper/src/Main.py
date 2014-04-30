# -*- coding: gbk -*- 
'''
Created on 2010-11-25

@author: cg
'''
from Grippers import *
import threading

class TaskThread(threading.Thread):
    
    def __init__(self,gripper):
        threading.Thread.__init__(self)
        self.gripper = gripper
    
    def run(self):
        self.gripper.start()

if __name__ == '__main__':

    grippers = []
    grippers.append(TaskThread(ccjt.CcjtGripper()))
    grippers.append(TaskThread(gtpcn.GtpCnGripper()))
    grippers.append(TaskThread(jitapu.JitapuGripper()))
    grippers.append(TaskThread(woaijt.WoaiGuitarGripper()))
    grippers.append(TaskThread(yf66.Yf66Gripper()))
    for gripper in grippers:
        gripper.start()

    