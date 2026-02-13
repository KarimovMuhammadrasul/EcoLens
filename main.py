from fastapi import FastAPI,UploadFile,File
from engine import InferenceEngine
import cv2,base64

app=FastAPI()
eng=InferenceEngine()

@app.post("/analyze")
async def analyze(file:UploadFile=File(...)):
    b=await file.read()
    objs,img=eng.process(b)
    
    if not objs:return {"labels":"None","info":"No objects found.","img":None}

    msg=await eng.get_guide(objs)
    _,buf=cv2.imencode('.jpg',img)
    s=base64.b64encode(buf).decode('utf-8')
    
    return {
        "labels":", ".join(objs),
        "info":msg,
        "img":s
    }

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="127.0.0.1",port=8100)