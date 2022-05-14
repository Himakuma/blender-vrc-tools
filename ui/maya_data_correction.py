import bpy

from ..utils.shapekey import ShapekeyUtils


class KUMATTASS_OT_maya_data_correction(bpy.types.Operator):
    bl_idname = "kumatta_ss.maya_data_correction"
    bl_label = "Maya(Quiche v.2)"
    bl_description = "Maya Data Correction"

    @classmethod
    def poll(self, context):
        return context.active_object.type == 'ARMATURE'

    # プラグインの処理
    def execute(self, context):
        oldMode = context.active_object.mode
        bpy.ops.object.mode_set(mode='EDIT')

        # Armature直下のボーン名が、”Armature”だった場合、削除
        editBones = context.active_object.data.edit_bones
        for editBone in editBones:
            if not editBone.parent and editBone.name == 'Armature':
                for childEditBone in editBone.children:
                    childEditBone.parent = None
                    editBones.remove(editBone)
                break

        # シェイプキー名にプレフィックスを付ける
        for childObject in context.active_object.children:
            if childObject.type != "MESH" or not childObject.data.shape_keys:
                continue
            ShapekeyUtils.add_prefix(childObject, "vrc.")
            shapeKey = childObject.data.shape_keys.key_blocks["vrc.Basis"]
            shapeKey.name = "Basis"
            ShapekeyUtils.move_key(childObject, "Basis", 0)
            ShapekeyUtils.move_key(childObject, "vrc.blink_left", 1)
            ShapekeyUtils.move_key(childObject, "vrc.blink_right", 2)
            ShapekeyUtils.move_key(childObject, "vrc.lowerlid_left", 3)
            ShapekeyUtils.move_key(childObject, "vrc.lowerlid_right", 4)

        bpy.ops.object.mode_set(mode=oldMode)
        return {'FINISHED'}
