"""
Brandguard - Brand Suite.

Provides brand guidelines, asset management, and consistency enforcement.
Enables brand-aligned content creation and marketing material validation.
"""

from brandguard.core import (
    BrandAssetType,
    BrandTone,
    BrandVoice,
    ColorPalette,
    Typography,
    BrandAsset,
    BrandGuideline,
    BrandIdentity,
)
from brandguard.guidelines import (
    GuidelineManager,
    GuidelineValidator,
    ConsistencyChecker,
)
from brandguard.assets import (
    AssetManager,
    AssetLibrary,
)
from brandguard.service import BrandService

__all__ = [
    # Core
    "BrandAssetType",
    "BrandTone",
    "BrandVoice",
    "ColorPalette",
    "Typography",
    "BrandAsset",
    "BrandGuideline",
    "BrandIdentity",
    # Guidelines
    "GuidelineManager",
    "GuidelineValidator",
    "ConsistencyChecker",
    # Assets
    "AssetManager",
    "AssetLibrary",
    # Service
    "BrandService",
]
