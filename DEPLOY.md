# Edge-TTS-API 部署说明

## 仓库已创建
仓库地址：`https://github.com/tyj2001/edge-tts-api`

## Railway 部署
1. 访问 https://railway.app
2. 用 GitHub 登录
3. 点击 "New Project" → "Deploy from GitHub repo"
4. 选择 `tyj2001/edge-tts-api`
5. Railway 会自动检测 Python 项目并部署

部署完成后 API 地址格式：
```
https://xxx.railway.app/tts?text=四一班&voice=zh-CN-XiaoxiaoNeural
```

## 可用音色
- `zh-CN-XiaoxiaoNeural` - 晓晓（女声）
- `zh-CN-YunxiNeural` - 云希（男声）
- `zh-CN-YunyangNeural` - 云扬（新闻腔）
- `zh-CN-XiaoyiNeural` - 小艺（女声）
