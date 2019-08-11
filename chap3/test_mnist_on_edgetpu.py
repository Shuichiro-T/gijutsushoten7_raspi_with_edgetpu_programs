import argparse
import re
import numpy
from edgetpu.classification.engine import ClassificationEngine


# mnist.npzからテスト用画像を抽出する
def LoadData(file_path):
    with numpy.load(file_path) as f:
      # -1の部分を好きな数にすると実行する数を変更できる（最大60000）
      return f['x_train'][0:-1]

# テキストファイルからラベルを読み込む
def ReadLabelFile(file_path):
  with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
  ret = {}
  for line in lines:
    pair = re.split(r'[:\s]+', line.strip(), maxsplit=1)
    ret[int(pair[0])] = pair[1].strip()
  return ret

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument(
    '--model', help='TensorFlow Liteモデルのファイルパス', required=True)
  parser.add_argument(
    '--label', help='ラベルファイルのファイルパス', required=True)
  parser.add_argument(
    '--npz', help='mnist.npzのファイルパス', required=True)
  parser.add_argument(
    '--print', help='結果を標準出力へ出力するか否か', type=bool,default=False, required=False)

  args = parser.parse_args()

  # ラベルの読み込み
  labels = ReadLabelFile(args.label)
  # モデルを読込、エンジンを初期化する
  engine = ClassificationEngine(args.model)
  
  count = 0
  # mnist.npzを読込読み込んだ分、画像分類を実行する
  for input_tensor in LoadData(args.npz):
    results = engine.ClassifyWithInputTensor(input_tensor=input_tensor.flatten(), threshold=0.1, top_k=3)
    # 出力オプションが真だった場合は結果を出力する
    if(args.print):
      print('-----------{0:6}----------'.format(count))

      for result in results:
        print(labels[result[0]], end="")
        print('  Score : ', result[1])
    count += 1

if __name__ == '__main__':
  main()
