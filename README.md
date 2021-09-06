# ku-nakamura-lab

## 準備
- Pythonの環境を整える
- 仮想環境を生成して有効化した後に、必要なライブラリ（requirements.txt）を読み込む
- ffmpegをインストールする（slice_movie.pyを使う場合）
```python
pip install -r requirements.txt
```

## get_trackpt_by_location.py
GPXファイルと位置情報Xから、Xが存在するであろう時区間を出力する。
```python
python get_trackpt_by_location.py [GPXファイルのパス] [緯度] [経度]
```
例
```python
python get_trackpt_by_location.py data/hoge.gpx 35.0279123 135.783464
```

## slice_moive.py
動画を指定の時区間で連番静止画に切り出す。
```python
python slice_moive.py [分割する動画ファイルのパス] [分割する時間（秒）]
```
例
```
python slice_moive.py data/hoge.mp4 1
```