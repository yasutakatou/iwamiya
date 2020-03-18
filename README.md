# iwamiya

自己紹介を文字起こしからの、**宮本さん度、岩田さん度を分類してマッチングすると強いチームが作れる**はず。なんてったってレジェンドな宮本さん、岩田さんの相性なんだもの。

![iwamiya](https://github.com/yasutakatou/iwamiya/blob/pic/iwamiya.gif)

## やりかた

Webサーバーからindex.htmlを読み込んで、各項目の**record**を押すと音声認識が始まります。<br>テーマに従って語ってください。

![iwamiya](https://github.com/yasutakatou/iwamiya/blob/pic/iwamiya2.gif)

全部埋めたら**判定**を押して診断結果を見てみましょう。


## 動かし方


fasttextを使ってモデルを作成し、pythonの引数に食わせます。


```
python3 iwamiya.py 1.bin 2.bin 3.bin
```

