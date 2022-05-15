# blender-vrc-tools
VRC向けのBlenderアドオン

## バージョンについて
v3.0

v{メジャーバージョン}.{マイナーバージョン・バグフィックス}

1. メジャーバージョン：レイアウト変更を伴う機能追加、または、使用するライブラリ群の変更、更新
1. マイナーバージョン：メジャーバージョンの変更外の機能追加、バグの修正単位（コード改善含む）

## 機能一覧
* ボーン名の部分置換（前方一致、後方一致、完全一致、正規表現）
* シェイプキーに「vrc.」を一括付与
* Maya キッシュ v.2系のfbxデータ補完
    - ボーン構造が、「Armature->Armature(ボーン)->Hips」の場合、「Armature(ボーン)」削除
    - シェイプキーに「vrc.」を一括付与



## 使用方法

### インストール
1. ダウンロード：https://github.com/Himakuma/blender-vrc-tools/releases

2. ダウンロードファイルを解凍（「src」配下を使用）

3. 「Edit->Preferences」を押下

![インストール](https://github.com/Himakuma/blender-vrc-tools/blob/master/doc/image/001.jpg "使用方法")


4. 「Add-ons」タグを選択、「Install」を押下して、ダウンロードした「blender-vrc-tools.zip」を選択

![インストール](https://github.com/Himakuma/blender-vrc-tools/blob/master/doc/image/002.jpg "使用方法")


5. アドオンの一覧に表示される「VRCTools」を、チェックをして有効化

![インストール](https://github.com/Himakuma/blender-vrc-tools/blob/master/doc/image/003.jpg "使用方法")

6. 「Tool」に「VRCTools」が表示される

![インストール](https://github.com/Himakuma/blender-vrc-tools/blob/master/doc/image/004.jpg "使用方法")


## 操作方法

### ボーン名の部分置換（前方一致、後方一致、完全一致、正規表現）

1. モデルを選択すると、「Bone Rename All」が有効になるので、押下

![インストール](https://github.com/Himakuma/blender-vrc-tools/blob/master/doc/image/005.jpg "使用方法")

2. 表示されたダイアログに、「検索文字列」、「置換文字列」、「検索方式」を入力して、「OK」を押下

![インストール](https://github.com/Himakuma/blender-vrc-tools/blob/master/doc/image/006.jpg "使用方法")



<br>


### シェイプキーに「vrc.」を一括付与
1. モデルのメッシュを選択すると、「ShapeKey Add VRC Prefix」が有効になるので、押下

![インストール](https://github.com/Himakuma/blender-vrc-tools/blob/master/doc/image/007.jpg "使用方法")

<br>

### Maya キッシュ v.2系のfbxデータ補完
1. モデルを選択すると、「Maya(Quiche v.2)」が有効になるのでクリック

※このツイートの処理を自動化　https://twitter.com/muta_shinki/status/1042296181437558784

![インストール](https://github.com/Himakuma/blender-vrc-tools/blob/master/doc/image/008.jpg "使用方法")

