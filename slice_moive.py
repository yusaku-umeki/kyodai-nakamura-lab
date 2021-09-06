import os
import shutil
import sys

import ffmpeg


def main(moive_path,time_interval):
    """
    moive_path[str]:分割する動画ファイルのパス
    time_interval[float]:分割する時間（秒）
    """
    width = 800 #画像横幅

    if os.path.isdir("img"):
        shutil.rmtree("img")
    os.makedirs("img")

    (
        ffmpeg
        .input(moive_path)
        .filter('scale', width, -1)
        .output('img/%05d.jpg', r=1/time_interval,f="image2")
        .run()
    )

if __name__ == "__main__":
    args = sys.argv
    if len(args) != 3:
        print("引数の数が正しくありません")
    else:
        main(moive_path=args[1],time_interval=float(args[2]))