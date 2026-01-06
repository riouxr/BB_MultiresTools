bl_info = {
    "name": "BB Multires Tools",
    "author": "Blender Bob & Claude.ai",
    "version": (1, 1, 1),
    "blender": (3, 0, 0),
    "location": "View3D > Sidebar > Tool",
    "category": "Object",
    "description": "Tools for managing Multires modifiers. Includes moving all Multires meshes into a 'Multires' collection and toggling visibility/display."
}

import bpy

COLLECTION_NAME = "Multires"


# ---------------------------------------------------------
# Helpers
# ---------------------------------------------------------

def get_or_create_multires_collection():
    col = bpy.data.collections.get(COLLECTION_NAME)
    if not col:
        col = bpy.data.collections.new(COLLECTION_NAME)
        bpy.context.scene.collection.children.link(col)
    return col


def iter_multires_modifiers():
    col = bpy.data.collections.get(COLLECTION_NAME)
    if not col:
        return []
    for obj in col.all_objects:
        for mod in obj.modifiers:
            if mod.type == 'MULTIRES':
                yield mod


# ---------------------------------------------------------
# Operators
# ---------------------------------------------------------

class MULTIRES_OT_move_to_collection(bpy.types.Operator):
    bl_idname = "object.multires_move_to_collection"
    bl_label = "Move to Collection"
    bl_description = "Find all meshes with Multires modifiers and add them to the 'Multires' collection (without removing them from existing collections)"

    def execute(self, context):

        target_col = get_or_create_multires_collection()
        count = 0

        for obj in bpy.data.objects:
            if obj.type != 'MESH':
                continue

            if any(mod.type == 'MULTIRES' for mod in obj.modifiers):

                # >>> FIX IS HERE <<<
                if obj.name not in target_col.objects:
                    try:
                        target_col.objects.link(obj)
                    except RuntimeError:
                        # already linked (fails silently)
                        pass
                # >>> END FIX <<<

                count += 1

        self.report({'INFO'}, f"Added {count} objects to 'Multires' collection")
        return {'FINISHED'}



class MULTIRES_OT_toggle_visibility(bpy.types.Operator):
    bl_idname = "object.multires_toggle_visibility"
    bl_label = "Modifier ON/OFF"

    def execute(self, context):
        mods = list(iter_multires_modifiers())
        if not mods:
            self.report({'INFO'}, "No Multires modifiers found in collection 'Multires'")
            return {'CANCELLED'}

        target = not mods[0].show_viewport
        for mod in mods:
            mod.show_viewport = target

        return {'FINISHED'}


class MULTIRES_OT_toggle_optimal(bpy.types.Operator):
    bl_idname = "object.multires_toggle_optimal_display"
    bl_label = "Display ON/OFF"

    def execute(self, context):
        mods = list(iter_multires_modifiers())
        if not mods:
            self.report({'INFO'}, "No Multires modifiers found in collection 'Multires'")
            return {'CANCELLED'}

        first = mods[0]
        current = (
            getattr(first, "use_optimal_display", None)
            if hasattr(first, "use_optimal_display")
            else getattr(first, "show_only_control_edges", False)
        )
        target = not bool(current)

        for mod in mods:
            if hasattr(mod, "use_optimal_display"):
                mod.use_optimal_display = target
            if hasattr(mod, "show_only_control_edges"):
                mod.show_only_control_edges = target

        return {'FINISHED'}


# ---------------------------------------------------------
# UI Panel
# ---------------------------------------------------------

class MULTIRES_PT_panel(bpy.types.Panel):
    bl_label = "BB Multires Tools"
    bl_idname = "MULTIRES_PT_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Tool"

    def draw(self, context):
        layout = self.layout

        layout.label(text="Affects all objects in the 'Multires' collection.", icon='INFO')

        col = layout.column(align=True)

        # NEW BUTTON - ABOVE EVERYTHING
        col.operator("object.multires_move_to_collection", text="Move to Collection")

        col.separator()

        col.operator("object.multires_toggle_visibility", text="Modifier ON/OFF")
        col.operator("object.multires_toggle_optimal_display", text="Display ON/OFF")


# ---------------------------------------------------------
# Registration
# ---------------------------------------------------------

classes = (
    MULTIRES_OT_move_to_collection,
    MULTIRES_OT_toggle_visibility,
    MULTIRES_OT_toggle_optimal,
    MULTIRES_PT_panel,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
