import cv2
from ultralytics import YOLO
import ollama
import numpy as np

class InferenceEngine:
    def __init__(self):
        self.m=YOLO("yolov10n.pt")
        self.m.to('mps') 
        
    def process(self,b):
        n=np.frombuffer(b,np.uint8)
        img=cv2.imdecode(n,cv2.IMREAD_COLOR)
        res=self.m(img,conf=0.3,verbose=False)
        
        if not res[0].boxes:return None,img
        
        objs=[]
        for x in res[0].boxes:
            lbl=res[0].names[int(x.cls[0])]
            if lbl not in objs:objs.append(lbl)
            
        return objs,res[0].plot()

    async def get_guide(self,items):
        s=", ".join(items)
        p=f"Expert sustainability agent. User found: {s}. Explain disposal (Recycle, Landfill, or Hazard) for each based on global standards. Keep under 50 words."
        try:
            r=ollama.chat(model='llama3.2-vision:11b-instruct-q4_K_M',messages=[{'role':'user','content':p}])
            return r['message']['content']
        except Exception as e:return f"Error: {str(e)}"