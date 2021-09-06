import math
import sys

import gpxpy
import gpxpy.gpx

lat = 35.0279123
lon = 135.783464

def main(gpx_file_path,lat,lon):
    """
    gpx_file_path[str]:GPXファイルのパス
    lat[float]:緯度
    lon[float]:経度
    """
    gpx_file = open(gpx_file_path,"r")
    gpx = gpxpy.parse(gpx_file)

    min_distance = 1000000000

    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                distance = math.sqrt((point.latitude-lat)**2 + (point.longitude-lon)**2)
                if distance < min_distance:
                    min_distance = distance
                    min_distance_time = point.time

    print("入力された位置情報が存在するであろう時間",min_distance_time)
    gpx_file.close()

if __name__ == "__main__":
    args = sys.argv
    if len(args) != 4:
        print("引数の数が正しくありません")
    else:
        main(gpx_file_path=args[1],lat=float(args[2]),lon=float(args[3]))