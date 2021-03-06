import json
from unreal import (
    AssetRegistryHelpers
)

asset_registry = AssetRegistryHelpers.get_asset_registry()
# get all assets
all_assets = asset_registry.get_assets_by_path('/Game', recursive=True)
# filter for skeleton assets
print(json.dumps([(str(asset.object_path), str(asset.asset_name), {"StaticMesh": "MESH", "SkeletalMesh": "ARMATURE", "AnimSequence": "ACTION"}[str(asset.asset_class)]) for asset in all_assets if str(asset.asset_class) in ["StaticMesh", "SkeletalMesh", "AnimSequence"]]))