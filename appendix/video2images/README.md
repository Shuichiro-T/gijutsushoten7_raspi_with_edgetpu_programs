# 動画・画像変換ツール

# 必要な実行環境
 * Python3

# 機能
動画から各フレームを画像として抜き出す。トリミングが必要であれば同時に行う。

# 使い方

## 必要なライブラリのインストール

```cmd
$ pip install -r requirements.txt
```

## 実行方法
```cmd
$ python3 Video2Images.py --input_video=(InputVideoPath)  --output_dir=(OutputDirectoryPath)
```

### パラメータ

| パラメータ名 | 必須か | 内容 | 例 |
|:-----------|:------------|:------------|:------------|
| input_video        |必須 | 入力にする動画のパス | ./IMG20010.mov |
| OutputDirectoryPath|必須 | 画像を出力するディレクトリパス。存在しないパスの場合作成する。 | ./images |
| trimming           | オプション | トリミングをする場合指定する。左上を基準として、開始位置のX座標、開始位置のY座標、トリミングするX方向のサイズ、トリミングするY方向のサイズをカンマ区切りで指定する。| 100,100,50,50 |