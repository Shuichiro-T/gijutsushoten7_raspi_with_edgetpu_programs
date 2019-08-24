import os
import argparse
import shutil
import cv2


def video_2_images(input_video, output_dir, trimming):

    #ディレクトリが無い場合は作成する
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    #トリミング指定がある場合はトリミングを行う。
    start_x, start_y, size_x , size_y = 0,0,0,0
    if not trimming == '0,0,0,0':
        array = trimming.split(',')
        if(not len(array) == 4):
            print('トリミングの指定の仕方が間違っています。例）　100,100,50,50')
            return 
        start_x = int(array[0])
        start_y = int(array[1])
        size_x = int(array[2])
        size_y = int(array[3])

    count = 0

    #OpenCVで動画をキャプチャする
    capture = cv2.VideoCapture(input_video)

    if not capture.isOpened():
        print('動画ファイルが開けませんでした')
        return 

    while(True):
        #動画からフレームを読込
        ret, frame = capture.read() 
        if ret == False:  #フレームの残りがあるか
            break

        #フレームのサイズを取得
        height, width = frame.shape[:2]
 
        #トリミングの指定があった場合はサイズを指定する
        if size_x == 0:
            size_x = width
        if size_y == 0:
            size_y = height

        #フレームを保存する
        filename = output_dir + '/%s.png' % str(count).zfill(6)
    
        cv2.imwrite(filename, frame[start_y : start_y + size_y, start_x : start_x + size_x])
        print(filename + ' is Saved.')
 
        count += 1

    capture.release()

def main():

    parser = argparse.ArgumentParser(description='動画を画像に変換するプログラムです。')
    parser.add_argument('-i','--input_video', help='変換される動画のパス')
    parser.add_argument('-o','--output_dir', help='画像を出力するディレクトリ')
    parser.add_argument('-t','--trimming', help='画像をトリミングする位置とサイズ'
         + '  左上を基準として、開始位置のX座標、開始位置のY座標、トリミングするX方向のサイズ、トリミングするY方向のサイズ'
         + 'をカンマ区切りで指定する。' 
         + '例）　100,100,50,50'
        , required=False, default='0,0,0,0')

    args = parser.parse_args()

    video_2_images(args.input_video, args.output_dir, args.trimming)

if __name__ == "__main__":
    main()