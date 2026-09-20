import pytest
from src.contact_validator import is_valid_email, is_valid_phone, mask_email, normalize_phone


def test_is_valid_email_true():
    """Test a well-formed email."""
    # Arrange
    email = "student@lpu.in"

    # Act
    result = is_valid_email(email)

    # Assert
    assert result == True


def test_is_valid_email_type_error():
    """Test that a non-string input raises TypeError."""
    with pytest.raises(TypeError):
        is_valid_email(12345)


def test_is_valid_phone_true():
    """Test a well-formed phone number with dashes."""
    # Arrange
    phone = "555-123-4567"

    # Act
    result = is_valid_phone(phone)

    # Assert
    assert result == True


def test_is_valid_phone_type_error():
    """Test that a non-string phone input raises TypeError."""
    with pytest.raises(TypeError):
        is_valid_phone(5551234567)


def test_mask_email_basic():
    """Test masking a typical email address."""
    # Arrange
    email = "priya@example.com"

    # Act
    result = mask_email(email)

    # Assert
    assert result == "pr***@example.com"


def test_mask_email_short_local_part():
    """Test masking an email with a one-character local part."""
    assert mask_email("a@example.com") == "a@example.com"


def test_mask_email_invalid():
    """Test that masking an invalid email raises ValueError."""
    with pytest.raises(ValueError):
        mask_email("invalid")


def test_normalize_phone():
    """Test removing dashes from a valid phone number."""
    assert normalize_phone("555-123-4567") == "5551234567"
