# blender-vrc-tools
VRC向けのBlenderアドオン

## バージョンについて
v2.0

v{メジャーバージョン}.{マイナーバージョン・バグフィックス}

1. メジャーバージョン：レイアウト変更を伴う機能追加、または、使用するライブラリ群の変更、更新
1. マイナーバージョン：メジャーバージョンの変更外の機能追加、バグの修正単位（コード改善含む）

## 機能一覧
* ボーン名称置換
* シェイプキーに「vrc.」を一律付与
* Maya Quiche_v.2系のfbxデータの補完
1. ボーン構造が、「Armature->Armature(ボーン)->Hips」になってしまう現象の「Armature(ボーン)」削除
2. シェイプキーに「vrc.」を一律付与



## 使用方法

### インストール
1. ダウンロード：https://github.com/Himakuma/blender-vrc-tools/releases

2. ダウンロードファイルを解凍（「src」配下を使用）

3. 「File->User Preferences」をクリック

![インストール](https://github.com/Himakuma/blender-vrc-tools/blob/master/doc/img/install_0100.jpg "使用方法")


4. 「Add-ons」タグを選択、「Install Add-on from File」をクリック

![インストール](https://github.com/Himakuma/blender-vrc-tools/blob/master/doc/img/install_0200.jpg "使用方法")

5. 「Install Add-on from File」をクリック、ダウンロードした「vrc_tools.py」を選択

![インストール](https://github.com/Himakuma/blender-vrc-tools/blob/master/doc/img/install_0300.jpg "使用方法")

6. アドオンの一覧に表示される

![インストール](https://github.com/Himakuma/blender-vrc-tools/blob/master/doc/img/install_0400.jpg "使用方法")

7. チェックをつけて、アドオンを有効化

![インストール](https://github.com/Himakuma/blender-vrc-tools/blob/master/doc/img/install_0500.jpg "使用方法")

## 機能使用方法

### ボーン名称の置換
1. 「Object Mode」でモデルのアーマチュアを選択すると、「Tools」に「VRCTools->Bone Rename All」が有効になるのでクリック

![実行](https://github.com/Himakuma/blender-vrc-tools/blob/master/doc/img/run_0100.jpg "使用方法")

2. ダイアログ画面が表示される

![実行](https://github.com/Himakuma/blender-vrc-tools/blob/master/doc/img/run_0200.jpg "使用方法")

3. 「検索方式」を選択

![実行](https://github.com/Himakuma/blender-vrc-tools/blob/master/doc/img/run_0300.jpg "使用方法")

4. 「検索文字列」、「置き換え文字列」を入力して、「OK」をクリックで、ボーンの名称を置換

![実行](https://github.com/Himakuma/blender-vrc-tools/blob/master/doc/img/run_0400.jpg "使用方法")


### シェイプキーに「vrc.」を一律付与
1. 「Object Mode」でモデルのメッシュを選択すると、「Tools」に「VRCTools->ShapeKey Add Vrc Prefix」が有効になるのでクリック

![実行](https://github.com/Himakuma/blender-vrc-tools/blob/master/doc/img/ShapeKeyAddVrcPrefix_0100.jpg "使用方法")


### Maya Quiche_v.2系のfbxデータの補完
1. 「Object Mode」でモデルのメッシュを選択すると、「Tools」に「VRCTools->Maya(Quiche_v.2~ fbx)」が有効になるのでクリック

※このツイートの処理を自動化　https://twitter.com/muta_shinki/status/1042296181437558784

![実行](https://github.com/Himakuma/blender-vrc-tools/blob/master/doc/img/Maya_Quiche_v.2fbx__0100.jpg "使用方法")

