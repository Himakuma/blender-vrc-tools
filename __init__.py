import sys
import re
import importlib

import bpy

from .ui.bone_rename_all import KUMATTASS_OT_bone_rename_all
from .ui.maya_data_correction import KUMATTASS_OT_maya_data_correction
from .ui.shapekeys_vrc_rename import KUMATTASS_OT_shapekeys_vrc_rename


bl_info = {
    "name": "VRCTools",
    "author": "Himakuma(kumatta_ss)",
    "version": (3, 0),
    "blender": (2, 93, 0),
    "location": "",
    "description": "VRCTools",
    "warning": "",
    "wiki_url": "",
    "category": "Object",
}


class KUMATTA_VIEW_PT_VRCTOOLS(bpy.types.Panel):
    bl_label = "VRCTools"

    # 表示領域設定
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Tool"

    def draw(self, context):
        self.layout.label(text="Bone")
        self.layout.operator(str(KUMATTASS_OT_bone_rename_all.bl_idname))

        self.layout.label(text="Mesh")
        self.layout.operator(str(KUMATTASS_OT_shapekeys_vrc_rename.bl_idname))

        self.layout.label(text="Correction")
        self.layout.operator(str(KUMATTASS_OT_maya_data_correction.bl_idname))


uiClasses = {
    KUMATTA_VIEW_PT_VRCTOOLS,
    KUMATTASS_OT_bone_rename_all,
    KUMATTASS_OT_maya_data_correction,
    KUMATTASS_OT_shapekeys_vrc_rename
}


def register():
    reloadModule = []
    for moduleKey in sys.modules.keys():
        if re.search("^blender-vrc-tools", moduleKey):
            reloadModule.append(moduleKey)

    for moduleName in reloadModule:
        importlib.reload(sys.modules[moduleName])

    for cls in uiClasses:
        if hasattr(cls, "translation_dict"):
            bpy.app.translations.register(cls.__name__, cls.translation_dict)

        bpy.utils.register_class(cls)


def unregister():
    for cls in uiClasses:
        if hasattr(cls, "translation_dict"):
            bpy.app.translations.unregister(cls.__name__)

        bpy.utils.unregister_class(cls)
        del cls


if __name__ == "__main__":
    register()
