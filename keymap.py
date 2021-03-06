import bpy

addon_keymaps = []

def register():
    if not canRegisterKeymaps(): return

    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name = "Node Editor", space_type = "NODE_EDITOR")

    # Open the ctrl-A search menu
    kmi = km.keymap_items.new("an.node_search", type = "A", value = "PRESS", ctrl = True)

    # Open the context sensitive pie menu
    kmi = km.keymap_items.new("wm.call_menu_pie", type = "W", value = "PRESS")
    kmi.properties.name = "an.context_pie"

    # Move view to subprogram nodes
    kmi = km.keymap_items.new("an.move_view_to_subprogram", type = "TAB", value = "PRESS")

    # Selection Pie Menu
    kmi = km.keymap_items.new("wm.call_menu_pie", type = "E", value = "PRESS")
    kmi.properties.name = "an.selection_pie"

    # Floating Advanced Panel
    kmi = km.keymap_items.new("an.floation_advanced_panel", type = "U", value = "PRESS")

    addon_keymaps.append(km)

def unregister():
    if not canRegisterKeymaps(): return

    wm = bpy.context.window_manager
    for km in addon_keymaps:
        for kmi in km.keymap_items:
            km.keymap_items.remove(kmi)
        wm.keyconfigs.addon.keymaps.remove(km)
    addon_keymaps.clear()

def canRegisterKeymaps():
    return not bpy.app.background
