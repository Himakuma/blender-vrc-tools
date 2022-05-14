import re
import bpy


class ShapekeyUtils:

    @staticmethod
    def add_prefix(meshData: bpy.types.Object, prefix: str):
        """シェイプキーにプレフィックスを付与
        Args:
            meshData: メッシュオブジェクト
            prefix: プレフィックス
        """
        # シェイプキーが存在しない場合、無視
        if not meshData.data.shape_keys:
            return

        regPrefix = re.compile("^" + re.escape(prefix))
        for shapeKey in meshData.data.shape_keys.key_blocks:
            if not re.search(regPrefix, shapeKey.name):
                shapeKey.name = prefix + shapeKey.name

    @staticmethod
    def move_key(meshData: bpy.types.Object,
                 shapeKeyName: str, moveIndex: int):
        """シェイプキーの位置を変更
        Args:
            meshData: メッシュオブジェクト
            shapeKeyName: シェイプキー名
            moveIndex: 移動先
        """

        # シェイプキーが存在しない場合、無視
        if not meshData.data.shape_keys:
            return

        # すでに指定の位置にある場合、終了
        nowIndex = meshData.data.shape_keys.key_blocks.find(shapeKeyName)
        if moveIndex == nowIndex:
            return

        oldMode = bpy.ontext.active_object.mode
        oldActiveObject = bpy.context.view_layer.objects.active

        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.context.view_layer.objects.active = meshData

        if nowIndex < moveIndex:
            moveMode = "DOWN"
            rangeCount = moveIndex = nowIndex
        else:
            moveMode = "UP"
            rangeCount = nowIndex - moveIndex

        meshData.active_shape_key_index = nowIndex
        for i in range(rangeCount):
            bpy.ops.object.shape_key_move(type=moveMode)

        bpy.ops.object.mode_set(mode=oldMode)
        bpy.context.view_layer.objects.active = oldActiveObject
