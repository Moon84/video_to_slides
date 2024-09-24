Here's the English translation of the summary:

# Video Slide Extraction and Transcription Software

## Main Functions

1. Extract slides from videos：  extract slides based on Python-OpenCV；
2. Delete repeat slides：
    - based on opencv differentiation；
    - Perform OCR（easyOCR） on extracted text from each slides，compare slides， delete continues slides
5. Transcribe video audio to text by Whisper；seperate text based on timestamp of each slides；
6. Generate PowerPoint presentations containing slides and transcribed text

## Software Structure

### Main Modules

1. `capture_slides_bg_modeling`: Extract slides from videos using background modeling
2. `convert_slides_to_ppt`: Convert extracted slides to PowerPoint presentations
3. `video_whisper`: Transcribe video audio using the Whisper model (implemented in an external file)
4. `remove_duplicates`: Remove duplicate slide images (implemented in an external file)

### Auxiliary Functions

- `resize_image_frame`: Resize image frames

## Workflow

1. Parse command-line arguments to get video path and output directory
2. Use background modeling algorithm (KNN or GMG) to extract slides from the video
3. Remove duplicate slide images
4. Transcribe video audio to text using the Whisper model
5. Perform OCR on extracted slides
6. Combine slide images and corresponding transcribed text into a PowerPoint presentation

## Main Libraries Used

- OpenCV (cv2): For video processing and background modeling
- EasyOCR: For image text recognition
- python-pptx: For creating PowerPoint presentations
- Whisper: For audio transcription (implemented in an external module)

## Notes

- The software supports various video formats, including avi, mp4, mpeg, mkv, and flv
- Users can customize input video and output directory through command-line arguments
- Background modeling algorithms and related parameters can be adjusted as needed




以下是这个软件的结构和功能的英文总结，使用markdown格式：

# 视频幻灯片提取和转录软件

## 主要功能

1. 从视频中提取幻灯片
2. 对提取的幻灯片进行OCR处理
3. 将视频音频转录为文本
4. 生成包含幻灯片和转录文本的PowerPoint演示文稿

## 软件结构

### 主要模块

1. `capture_slides_bg_modeling`: 使用背景建模提取视频中的幻灯片
2. `convert_slides_to_ppt`: 将提取的幻灯片转换为PowerPoint演示文稿
3. `video_whisper`: 使用Whisper模型进行视频音频转录（在外部文件中实现）
4. `remove_duplicates`: 移除重复的幻灯片图像（在外部文件中实现）

### 辅助函数

- `resize_image_frame`: 调整图像帧的大小

## 工作流程

1. 解析命令行参数，获取视频路径和输出目录
2. 使用背景建模算法（KNN或GMG）从视频中提取幻灯片
3. 移除重复的幻灯片图像
4. 使用Whisper模型将视频音频转录为文本
5. 对提取的幻灯片进行OCR处理
6. 将幻灯片图像和相应的转录文本合并到PowerPoint演示文稿中

## 使用的主要库

- OpenCV (cv2): 用于视频处理和背景建模
- EasyOCR: 用于图像文本识别
- python-pptx: 用于创建PowerPoint演示文稿
- Whisper: 用于音频转录（在外部模块中实现）

## 注意事项

- 该软件支持多种视频格式，包括avi、mp4、mpeg、mkv和flv
- 用户可以通过命令行参数自定义输入视频和输出目录
- 背景建模算法和相关参数可以根据需要进行调整
