以下是该程序架构的解析和markdown格式的说明文档：

# 幻灯片捕获和PPT生成程序

## 1. 程序概述

这个程序主要用于从视频中捕获幻灯片，并将捕获的幻灯片转换为PowerPoint演示文稿。它还包括了音频转录和OCR文本识别功能。

## 2. 主要功能模块

### 2.1 幻灯片捕获 (`capture_slides_bg_modeling`)

- 使用背景建模算法（GMG或KNN）从视频中提取幻灯片。
- 可以设置各种参数来调整捕获的灵敏度。
- 将捕获的幻灯片保存为图像文件。

### 2.2 重复幻灯片移除 (`remove_duplicates`)

- 移除重复或相似的幻灯片图像。

### 2.3 音频转录 (`video_whisper`)

- 使用Whisper模型将视频的音频内容转录为文本。

### 2.4 幻灯片转PPT (`convert_slides_to_ppt`)

- 将捕获的幻灯片图像转换为PowerPoint演示文稿。
- 使用OCR识别幻灯片中的文本。
- 将音频转录内容添加到PPT的备注中。

## 3. 主要函数说明

### 3.1 `resize_image_frame(frame, resize_width)`

调整图像帧的大小，保持宽高比。

### 3.2 `capture_slides_bg_modeling(video_path, output_dir_path, type_bgsub, history, threshold, min_percent_thresh, max_percent_thresh)`

使用背景建模方法捕获视频中的幻灯片。

参数：
- `video_path`: 视频文件路径
- `output_dir_path`: 输出目录路径
- `type_bgsub`: 背景建模算法类型（'GMG'或'KNN'）
- `history`: 背景建模的历史帧数
- `threshold`: 前景/背景分割阈值
- `min_percent_thresh`: 判断是否存在运动的阈值
- `max_percent_thresh`: 判断运动是否停止的阈值

### 3.3 `convert_slides_to_ppt(output_dir_path)`

将捕获的幻灯片图像转换为PPT文件。

- 使用EasyOCR进行文本识别
- 删除重复的幻灯片
- 将音频转录内容添加到PPT备注中

## 4. 使用流程

1. 设置输入视频路径和输出目录
2. 调用`capture_slides_bg_modeling`捕获幻灯片
3. 使用`remove_duplicates`移除重复幻灯片
4. 调用`video_whisper`进行音频转录
5. 最后使用`convert_slides_to_ppt`生成PPT文件

## 5. 依赖库

- OpenCV (cv2)
- EasyOCR
- python-pptx
- Whisper (用于音频转录)

## 6. 注意事项

- 确保已安装所有必要的依赖库
- 可能需要根据不同的视频内容调整参数以获得最佳结果
- OCR和音频转录的准确性可能因视频质量而异