import bpy
import re

bl_info = {
    "name": "VRCTools",
    "author": "Himakuma(kumatta_ss)",
    "version": (1, 0),
    "blender": (2, 79, 0),
    "location": "",
    "description": "VRCTools",
    "warning": "",
    "support": "COMMUNITY",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Object"
}

class UI(bpy.types.Panel):
    bl_label = "VRCTools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_category = "Tools"
  
    def draw(self, context):
        self.layout.operator("kumatta_ss.bone_rename_all")

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
        if len(self.replaceStr) == 0 :
            return {'FINISHED'}

        regStr = re.escape(self.replaceStr)
        if self.searchMode == "Forward" :
            regStr = "^" + re.escape(self.replaceStr)

        elif self.searchMode == "Backward" :
            regStr = re.escape(self.replaceStr) + "$"

        for boneData in bpy.context.active_object.data.bones:
            if re.search(regStr, boneData.name) :
                boneData.name = re.sub(regStr, self.replaceToStr, boneData.name)

        # 成功時の返却
        return {'FINISHED'}

    # ダイアログ処理
    def invoke(self, context, event):
        # クラス変数をダイアログのプロパティとして指定
        return context.window_manager.invoke_props_dialog(self)


classes = (
    UI,
    BoneRenameAll
)


def register():
    print("Bone Rename All ON")
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    print("Bone Rename All OFF")
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()

