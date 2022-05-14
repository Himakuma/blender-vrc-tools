import re
import bpy


class BoneUtils:
    @staticmethod
    def replace_name(regStr: str, newStr: str):
        """現在選択しているオブジェクトのボーン名を置き換え
        Args:
            regStr: 正規表現
            replaceStr: 置き換え文字列
        """
        for boneData in bpy.context.active_object.data.bones:
            if re.search(regStr, boneData.name):
                boneData.name = re.sub(regStr, newStr, boneData.name)
