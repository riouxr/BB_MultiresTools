# BB Multires Tools

A Blender addon that simplifies the management of Multires modifiers across multiple objects.

## Features

- **Automatic Collection Organization**: Quickly move all objects with Multires modifiers into a dedicated "Multires" collection
- **Batch Modifier Control**: Toggle Multires modifier visibility on/off for all objects at once
- **Optimal Display Toggle**: Switch optimal display settings for all Multires modifiers simultaneously
- **Non-Destructive**: Objects remain in their original collections while being added to the Multires collection

## Installation

### Blender 4.0+

1. Download the addon files (`__init__.py` and `blender_manifest.toml`)
2. In Blender, go to `Edit > Preferences > Add-ons`
3. Click `Install...` and select the addon folder or zip file
4. Enable "BB Multires Tools" in the add-ons list

### Blender 3.0-3.6

The addon is compatible with Blender 3.0+, though the `blender_manifest.toml` file is only required for Blender 4.0+.

## Usage

The addon adds a new panel in the 3D Viewport sidebar:

1. Open the 3D Viewport
2. Press `N` to open the sidebar
3. Navigate to the "Tool" tab
4. Find the "BB Multires Tools" panel

### Panel Controls

#### Move to Collection
Scans your entire scene for any mesh objects that have Multires modifiers and adds them to a special "Multires" collection. Objects will remain in their existing collections.

#### Modifier ON/OFF
Toggles the viewport visibility of all Multires modifiers in the Multires collection. Useful for improving viewport performance when working on other aspects of your scene.

#### Display ON/OFF
Toggles the optimal display setting for all Multires modifiers. This controls whether the subdivision surface is displayed optimally or shows only control edges.

## Requirements

- Blender 3.0.0 or higher
- Blender 4.0.0 or higher (recommended)

## Technical Details

### How It Works

- Creates a dedicated "Multires" collection in your scene
- Links objects to this collection without removing them from existing collections
- Operates on all Multires modifiers found in objects within the Multires collection
- Handles both `use_optimal_display` and `show_only_control_edges` attributes for compatibility

### Collection Management

The addon uses a non-destructive approach: objects with Multires modifiers are added to the "Multires" collection while remaining in their original collections. This allows you to maintain your existing scene organization while benefiting from centralized Multires management.

## Troubleshooting

**Q: The buttons don't seem to do anything**
- Make sure you've clicked "Move to Collection" first to populate the Multires collection

**Q: Some objects aren't being detected**
- Only mesh objects with Multires modifiers are detected
- Make sure your objects actually have the Multires modifier applied

**Q: I don't see the panel**
- Press `N` in the 3D Viewport to show the sidebar
- Navigate to the "Tool" tab
- Make sure the addon is enabled in Preferences

## License

GPL-3.0-or-later

## Credits

Created by Blender Bob with assistance from ChatGPT

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## Changelog

### Version 1.1.1
- Fixed collection linking to prevent duplicate link attempts
- Improved error handling for object linking
- Added proper checks before linking objects to collection

### Version 1.0.0
- Initial release
- Basic Multires collection management
- Viewport visibility toggle
- Optimal display toggle
