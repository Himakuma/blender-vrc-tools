import bpy
from bpy.props import (  # noqa
    EnumProperty,
    StringProperty,
)

import re
from ..utils.bone import BoneUtils


class KUMATTASS_OT_bone_rename_all(bpy.types.Operator):

    bl_idname = "kumattass.bone_rename_all"
    bl_label = "Bone Rename All"
    bl_description = "Bone rename"

    translation_dict = {
        "ja_JP": {
            ("*", "Forward match"): "前方一致",
            ("*", "Backward match"): "後方一致",
            ("*", "Exact match"): "部分一致",
            ("*", "Regular expression"): "正規表現",
        }
    }

    searchModes = [
        ("Forward", "Forward match", ""),
        ("Backward", "Backward match", ""),
        ("Perfect", "Exact match", ""),
        ("RegularExpression", "Regular expression", "")
    ]

    search_str: StringProperty(name="Search", default="")  # noqa
    new_str: StringProperty(name="Replacement", default="")  # noqa
    mode: EnumProperty(
        name="Mode", description="", default='Forward', items=searchModes)  # noqa

    @classmethod
    def poll(self, context):
        return context.active_object.type == 'MESH'

    def execute(self, context):
        if len(self.search_str) == 0:
            return {'FINISHED'}

        modeStr = str(self.mode)
        regStr = self.convert_reg_str(modeStr, str(self.search_str))
        BoneUtils.replace_name(regStr, self.new_str)

        return {'FINISHED'}

    def invoke(self, context, event):
        # ダイアログ
        return context.window_manager.invoke_props_dialog(self)

    def convert_reg_str(modeStr: str, searchStr: str) -> str:
        """モードに合わせて、検索文字列を正規表現に変換
        Args:
            modeStr: モード
            searchStr: 検索文字列
        """

        if modeStr == "RegularExpression":
            return searchStr
        else:
            regStr = re.escape(searchStr)

        if modeStr == "Forward":
            return "^" + regStr
        elif modeStr == "Backward":
            return regStr + "$"

        return ""
