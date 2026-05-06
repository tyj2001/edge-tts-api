from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import edge_tts
import tempfile
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 可用音色列表
VOICES = {
    # 中文女声
    "zh-CN-XiaoxiaoNeural": "晓晓（女声，温柔）",
    "zh-CN-YunxiNeural": "云希（男声）",
    "zh-CN-XiaoyiNeural": "小艺（女声）",
    "zh-CN-YunyangNeural": "云扬（男声，新闻）",
    "zh-CN-liaoning-XiaobearNeural": "小熊（辽宁话）",
    # 英文
    "en-US-AriaNeural": "Aria（英文女声）",
    "en-GB-SoniaNeural": "Sonia（英文女声）",
}

@app.get("/")
async def root():
    return {"message": "Edge TTS API", "voices": VOICES}

@app.get("/voices")
async def voices():
    return {"voices": VOICES}

@app.get("/tts")
async def tts(text: str = Query(...), voice: str = Query("zh-CN-XiaoxiaoNeural")):
    if voice not in VOICES:
        return {"error": f"voice '{voice}' not found. Available: {list(VOICES.keys())}"}
    
    try:
        # 生成音频
        communicate = edge_tts.Communicate(text, voice)
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        temp_path = temp_file.name
        temp_file.close()
        
        await communicate.save(temp_path)
        
        # 返回文件
        return FileResponse(temp_path, media_type="audio/mpeg", filename="tts.mp3")
    except Exception as e:
        return {"error": str(e)}
    finally:
        # 清理临时文件
        if os.path.exists(temp_path):
            try:
                os.remove(temp_path)
            except:
                pass

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
