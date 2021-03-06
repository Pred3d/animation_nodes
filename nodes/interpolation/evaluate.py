import bpy
from ... base_types.node import AnimationNode

class EvaluateInterpolationNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_EvaluateInterpolationNode"
    bl_label = "Evaluate Interpolation"

    def create(self):
        self.width = 150
        self.inputs.new("an_FloatSocket", "Position", "position").setRange(0, 1)
        self.inputs.new("an_InterpolationSocket", "Interpolation", "interpolation").defaultDrawType = "PROPERTY_ONLY"
        self.outputs.new("an_FloatSocket", "Value", "value")

    def getExecutionCode(self):
        return "value = interpolation[0](max(min(position, 1.0), 0.0), interpolation[1])"
