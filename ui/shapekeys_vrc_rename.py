import bpy

from ..utils.shapekey import ShapekeyUtils


class KUMATTASS_OT_shapekeys_vrc_rename(bpy.types.Operator):
    bl_idname = "kumatta_ss.shapekeys_vrc_rename"
    bl_label = "ShapeKey Add VRC Prefix"
    bl_description = "ShapeKey Add VRC Prefix"

    @classmethod
    def poll(self, context):
        return context.active_object.type == 'MESH'

    # プラグインの処理
    def execute(self, context):
        oldMode = context.active_object.mode
        bpy.ops.object.mode_set(mode='OBJECT')

        # シェイプキー名にプレフィックスを付ける
        meshObject = context.active_object
        if meshObject.type == "MESH" and meshObject.data.shape_keys:
            ShapekeyUtils.add_prefix(meshObject, "vrc.")
            shapeKey = meshObject.data.shape_keys.key_blocks["vrc.Basis"]
            shapeKey.name = "Basis"
            ShapekeyUtils.move_key(meshObject, "Basis", 0)
            ShapekeyUtils.move_key(meshObject, "vrc.blink_left", 1)
            ShapekeyUtils.move_key(meshObject, "vrc.blink_right", 2)
            ShapekeyUtils.move_key(meshObject, "vrc.lowerlid_left", 3)
            ShapekeyUtils.move_key(meshObject, "vrc.lowerlid_right", 4)

        bpy.ops.object.mode_set(mode=oldMode)
        return {'FINISHED'}
