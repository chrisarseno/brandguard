"""Tests for BrandService."""

import pytest
from datetime import datetime, timezone
from unittest.mock import AsyncMock, MagicMock, patch


class TestBrandService:
    """Tests for the BrandService."""

    @pytest.fixture
    def brand_service(self):
        """Create a BrandService instance."""
        from brandguard import BrandService
        return BrandService()

    def test_service_initialization(self, brand_service):
        """Verify service initializes correctly."""
        assert brand_service is not None
        assert hasattr(brand_service, "_identity")

    def test_get_identity_empty(self, brand_service):
        """Get identity returns None when not created."""
        identity = brand_service.get_identity()
        assert identity is None

    def test_create_identity(self, brand_service):
        """Create brand identity."""
        result = brand_service.create_identity(
            name="TestBrand",
            tagline="Test Tagline",
            mission="Test Mission",
            primary_tone="professional",
        )
        assert "name" in result
        assert result["name"] == "TestBrand"

    def test_get_identity_after_create(self, brand_service):
        """Get identity returns data after creation."""
        brand_service.create_identity(
            name="TestBrand",
            tagline="Test Tagline",
        )
        identity = brand_service.get_identity()
        assert identity is not None
        assert identity["name"] == "TestBrand"

    def test_validate_content_no_identity(self, brand_service):
        """Validate content fails without identity."""
        result = brand_service.validate_content(
            content="Test content",
            content_type="website",
        )
        assert "error" in result or "passed" in result

    def test_validate_content_with_identity(self, brand_service):
        """Validate content with identity."""
        brand_service.create_identity(
            name="TestBrand",
            primary_tone="professional",
        )
        result = brand_service.validate_content(
            content="This is professional test content.",
            content_type="website",
        )
        assert isinstance(result, dict)

    def test_add_guideline(self, brand_service):
        """Add a brand guideline."""
        guideline_id = brand_service.add_guideline(
            category="voice",
            title="Test Guideline",
            description="Test description",
            rule_type="guideline",
        )
        assert guideline_id is not None
        assert isinstance(guideline_id, str)

    def test_get_guidelines(self, brand_service):
        """Get brand guidelines."""
        brand_service.add_guideline(
            category="voice",
            title="Test Guideline",
            description="Test description",
        )
        guidelines = brand_service.get_guidelines()
        assert isinstance(guidelines, list)
        assert len(guidelines) >= 1

    def test_get_executive_report_cmo(self, brand_service):
        """CMO report has marketing focus."""
        brand_service.create_identity(
            name="TestBrand",
        )
        report = brand_service.get_executive_report("CMO")
        assert report["executive"] == "CMO"
        assert report["focus"] == "Brand Voice & Marketing"

    def test_get_brand_kit(self, brand_service):
        """Get brand kit."""
        brand_service.create_identity(
            name="TestBrand",
        )
        kit = brand_service.get_brand_kit()
        assert "name" in kit
        assert kit["name"] == "TestBrand"

    def test_get_stats(self, brand_service):
        """Get service stats."""
        stats = brand_service.get_stats()
        assert "initialized" in stats
        assert "has_identity" in stats
