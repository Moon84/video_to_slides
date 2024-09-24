import cv2
import os
import time
import sys


def capture_slides_frame_diff(video_path, output_dir_path, MIN_PERCENT_THRESH=0.06, ELAPSED_FRAME_THRESH=85):
    '''
        这个函数的功能是在当采用framediff模式的时候，进行抓取。。。。
    '''

    prev_frame = None
    curr_frame = None
    screenshots_count = 0
    capture_frame = False
    frame_elapsed = 0

    # Initialize kernel.
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7,7))  ## 这段代码将创建一个大小为7x7的椭圆形结构元素，并将其赋值给变量kernel


    # Capture video frames
    cap = cv2.VideoCapture(video_path)  ## 根据video_path打开视频文件或摄像头，并将返回的VideoCapture对象赋值给变量cap

    if not cap.isOpened():                                ##报错
        print('Unable to open video file: ', video_path)
        sys.exit()
    
    
    success, first_frame = cap.read()  ##读取第一帧图像

    print("Take Frame differencing model for Background Subtraction")
    print('---'*10)


    start = time.time()

    # The 1st frame should always be present in the output directory.
    # Hence capture and save the 1st frame.
    if success:
        # Convert frame to grayscale.
        first_frame_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)

        prev_frame = first_frame_gray
        
        screenshots_count+=1

        filename = f"{screenshots_count:03}.png"
        out_file_path = os.path.join(output_dir_path, filename)
        print(f"Saving file at: {out_file_path}")

        # Save frame.
        cv2.imwrite(out_file_path, first_frame)
        
    
    # Loop over subsequent frames.
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        curr_frame = frame_gray


        if (prev_frame is not None) and (curr_frame is not None):
            frame_diff = cv2.absdiff(curr_frame, prev_frame)
            _, frame_diff = cv2.threshold(frame_diff, 80, 255, cv2.THRESH_BINARY)

            # Perform dilation to capture motion.
            frame_diff = cv2.dilate(frame_diff, kernel)

            # Compute the percentage of non-zero pixels in the frame.
            p_non_zero = (cv2.countNonZero(frame_diff) / (1.0 * frame_gray.size)) * 100

            if p_non_zero>=MIN_PERCENT_THRESH and not capture_frame:
                capture_frame = True
            
            elif capture_frame:
                frame_elapsed+=1

            if frame_elapsed >= ELAPSED_FRAME_THRESH:
                capture_frame = False
                frame_elapsed=0

                screenshots_count+=1

                filename = f"{screenshots_count:03}.png"
                out_file_path = os.path.join(output_dir_path, filename)
                print(f"Saving file at: {out_file_path}")

                cv2.imwrite(out_file_path, frame)
                
                
        prev_frame = curr_frame
    
    end_time = time.time()
    print('***'*10,'\n')
    print("Statistics:")
    print('---'*5)
    print(f'Total Time taken: {round(end_time-start, 3)} secs')
    print(f'Total Screenshots captured: {screenshots_count}')
    print('---'*10,'\n')

    cap.release()
