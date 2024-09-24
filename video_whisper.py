import whisper
from moviepy.editor import VideoFileClip
import os
import json
import argparse

def extract_audio(video_path, audio_path):
    """从视频中提取音频"""
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path)
    video.close()

def transcribe_audio(audio_path, model_name="base"):
    """使用 Whisper 转录音频"""
    model = whisper.load_model(model_name)
    result = model.transcribe(audio_path)
    return result

def format_timestamp(seconds):
    """将秒数格式化为时:分:秒"""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:05.2f}"

def save_transcription(transcription, output_path):
    """保存转录结果为JSON格式"""
    json_output = []
    for segment in transcription['segments']:
        json_output.append({
            "start_time": format_timestamp(segment['start']),
            "end_time": format_timestamp(segment['end']),
            "text": segment['text'].strip()
        })
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(json_output, f, ensure_ascii=False, indent=2)

def video_whisper(video_path, output_dir_path, model):
    # 创建临时音频文件
    temp_audio = "temp_audio.wav"
    
    try:
        print("正在从视频中提取音频...")
        extract_audio(video_path, temp_audio)
        
        print("正在转录音频...")
        transcription = transcribe_audio(temp_audio, model)
        
        print("正在保存转录结果...")
        output_path = os.path.join(output_dir_path, "transcription.json")
        save_transcription(transcription, output_path)
        
        print(f"转录完成。结果已保存到: {output_dir_path}")
    finally:
        # 清理临时文件
        if os.path.exists(temp_audio):
            os.remove(temp_audio)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="使用 Whisper 将视频转录为带时间戳的 JSON 文件")
    parser.add_argument("video_path", help="输入视频文件的路径")
    # parser.add_argument("-o", "--output", default="", help="输出 JSON 文件的路径 (默认: transcription.json)")
    parser.add_argument("-m", "--model", default="base", choices=["tiny", "base", "small", "medium", "large"], help="Whisper 模型大小 (默认: base)")
    parser.add_argument("-d", "--output_dir_path", default="./project/Neural_Networks_Overview/out_put", help="输出 JSON 文件的路径 (默认: 根文件夹下)")
    args = parser.parse_args()
    video_path = args.video_path
    output_dir_path = args.output_dir_path
    model = args.model

    if not os.path.exists(video_path):
        print(f"错误：找不到视频文件 '{video_path}'")
        print("请检查文件路径是否正确，并确保文件名没有拼写错误。")
    else:
        video_whisper(video_path, output_dir_path, model)