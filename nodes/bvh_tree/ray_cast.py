import bpy
from ... base_types.node import AnimationNode

class RayCastBVHTreeNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_RayCastBVHTreeNode"
    bl_label = "Ray Cast BVHTree"

    def create(self):
        self.inputs.new("an_BVHTreeSocket", "BVHTree", "bvhTree")
        self.inputs.new("an_VectorSocket", "Ray Start", "start")
        self.inputs.new("an_VectorSocket", "Ray Direction", "direction")
        self.outputs.new("an_VectorSocket", "Location", "location")
        self.outputs.new("an_VectorSocket", "Normal", "normal")

    def getExecutionCode(self):
        yield "location, normal, _, _ = bvhTree.ray_cast(start, direction)"
        yield "if location is None:"
        yield "    location = mathutils.Vector((0, 0, 0))"
        yield "    normal = mathutils.Vector((0, 0, 0))"

    def getUsedModules(self):
        return ["mathutils"]
