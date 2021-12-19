# 行政区画の境界のポリゴン抽出プログラム
[Linked Open Addresses Japan](https://uedayou.net/loa/)が提供する JSON データから境界ポリゴンを抽出する。

## 階層
階層は下記の通り。
```bash
│  prefecture_polygon.py
│  README.md
├─areas
│      東京都.json
│      東京都世田谷区.json
│      東京都中央区.json
│      ...
└─extracted_polygons
        東京都.json
        東京都世田谷区.json
        東京都中央区.json
        東京都中野区.json
        ...
```
### areas
Linked Open Addresses Japan から取得した JSON ファイルを設置する。

### extracted_polygons
境界ポリゴンが下記の JSON ファイルで保存される。
```json
[
    {
        "lat": 24.284078400000002,
        "lng": 153.97357438
    },
    {
        "lat": 24.28297405,
        "lng": 153.97858222
    },
    {
        "lat": 24.282955490000003,
        "lng": 153.97858711
    },
    ...
]
```

### prefecture_polygon.py
areas 内のファイルから境界ポリゴンを抽出加工し extracted_polygons に保存する。

