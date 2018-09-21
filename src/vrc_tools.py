import bpy
import re
import collections

bl_info = {
    "name": "VRCTools",
    "author": "Himakuma(kumatta_ss)",
    "version": (2, 0),
    "blender": (2, 79, 0),
    "location": "",
    "description": "VRCTools",
    "warning": "",
    "support": "COMMUNITY",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Object"
}

# ベースメニュー
class UI(bpy.types.Panel):
    bl_label = "VRCTools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_category = "Tools"
  
    def draw(self, context):
        self.layout.label(text="Bone")
        self.layout.operator("kumatta_ss.bone_rename_all")
        self.layout.label(text="Mesh")
        self.layout.operator("kumatta_ss.shapekey_add_vrc_prefix")
        self.layout.label(text="Correction")
        self.layout.operator("kumatta_ss.maya_data_correction")


# Bone名称置換
class BoneRenameAll(bpy.types.Operator):
    bl_idname = "kumatta_ss.bone_rename_all"  # 識別用のID
    bl_label = "Bone Rename All"              # ボタン名称
    bl_description = "Bone Rename All"        # 説明

    searchModes = [
        ("Forward", "前方一致", ""),
        ("Backward", "後方一致", ""),
        ("Perfect", "完全一致", ""),
    ]

    # ダイアログ用のプロパティ
    replaceStr = bpy.props.StringProperty(name="検索文字列")
    replaceToStr = bpy.props.StringProperty(name="置き換え文字列")
    searchMode = bpy.props.EnumProperty(name="検索方式", description="", default='Forward', items=searchModes)

    # 活性制御
    @classmethod
    def poll(self, context):
        obj = context.active_object
        return obj and obj.type == 'ARMATURE'

    # プラグインの処理
    def execute(self, context):
        if len(self.replaceStr) == 0:
            return {'FINISHED'}

        regStr = re.escape(self.replaceStr)
        if self.searchMode == "Forward":
            regStr = "^" + re.escape(self.replaceStr)

        elif self.searchMode == "Backward":
            regStr = re.escape(self.replaceStr) + "$"

        for boneData in bpy.context.active_object.data.bones:
            if re.search(regStr, boneData.name):
                boneData.name = re.sub(regStr, self.replaceToStr, boneData.name)

        
        print(type(bpy.context.active_object.data))
        # 成功時の返却
        return {'FINISHED'}

    # ダイアログ処理
    def invoke(self, context, event):
        # クラス変数をダイアログのプロパティとして指定
        return context.window_manager.invoke_props_dialog(self)

# シェイプキーの移動
def moveShapeKey(shapeKeys, keyName, toIndex):
    nowIndex = shapeKeys.key_blocks.find(keyName)
    if nowIndex == toIndex:
        return

    moveType = 'UP'
    rangeCount = nowIndex - toIndex
    if nowIndex < toIndex:
        moveType = 'DOWN'
        rangeCount = toIndex - nowIndex

    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.context.object.active_shape_key_index = nowIndex
    for i in range(rangeCount):
        bpy.ops.object.shape_key_move(type=moveType)


# シェイプキーの名称変換
def shapeKeyAddVrcPrefix(objData):
    shapeKeys = objData.data.shape_keys
    if shapeKeys:
        vrcPrefix = re.compile("^" + re.escape("vrc."))
        for shapeKeyIndex, shapeData in enumerate(shapeKeys.key_blocks):
            if not vrcPrefix.match(shapeData.name):
                shapeData.name = "vrc." + shapeData.name
        bpy.context.scene.objects.active = objData    
        moveShapeKey(shapeKeys, "vrc.Basis", 0)
        moveShapeKey(shapeKeys, "vrc.blink_left", 1)
        moveShapeKey(shapeKeys, "vrc.blink_right", 2)
        moveShapeKey(shapeKeys, "vrc.lowerlid_left", 3)
        moveShapeKey(shapeKeys, "vrc.lowerlid_right", 4)

# Maya Quiche_v.2系のfbx 変換
class MayaDataCorrection(bpy.types.Operator):
    bl_idname = "kumatta_ss.maya_data_correction"
    bl_label = "Maya(Quiche_v.2~ fbx)"
    bl_description = "Maya Data Correction"

    # 活性制御
    @classmethod
    def poll(self, context):
        obj = context.active_object
        return obj and obj.type == 'MESH'

    # プラグインの処理
    def execute(self, context):
        for objectData in bpy.data.objects.values():
            if objectData.type == 'ARMATURE':
                bpy.context.scene.objects.active = objectData
                bpy.ops.object.mode_set(mode='EDIT')
                for boneData in objectData.data.edit_bones:
                    if not boneData.parent and boneData.name == 'Armature':
                        for childrenBoneData in boneData.children:
                            childrenBoneData.parent = None
                        objectData.data.edit_bones.remove(boneData)
                        break
            elif objectData.type == 'MESH':
                shapeKeyAddVrcPrefix(objectData)
        bpy.ops.object.mode_set(mode='OBJECT')

        # 成功時の返却
        return {'FINISHED'}

# シェイプキーにプレフィックスを付与
class ShapeKeysVrcRename(bpy.types.Operator):
    bl_idname = "kumatta_ss.shapekey_add_vrc_prefix"
    bl_label = "ShapeKey Add Vrc Prefix"
    bl_description = "ShapeKey Add Vrc Prefix"

    # 活性制御
    @classmethod
    def poll(self, context):
        obj = context.active_object
        return obj and obj.type == 'MESH'

    # プラグインの処理
    def execute(self, context):
        bpy.ops.object.mode_set(mode='OBJECT')
        for objectData in bpy.data.objects.values():
            if objectData.type == 'MESH':
                shapeKeyAddVrcPrefix(objectData)

        # 成功時の返却
        return {'FINISHED'}






classes = (
    UI,
    BoneRenameAll,
    MayaDataCorrection,
    ShapeKeysVrcRename
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()

