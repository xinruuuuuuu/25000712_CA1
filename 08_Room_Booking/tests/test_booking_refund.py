import pytest
from src.booking_refund import is_refundable


@pytest.mark.parametrize(
    "hours_before_checkin, flexible_rate, expected",
    [
        (48, True, True),
        (49, True, True),
        (100, True, True),
        (47, True, False),
        (0, True, False),
        (48, False, False),
        (100, False, False),
    ],
)
def test_valid_refund_inputs_returns_expected_bool(
    hours_before_checkin, flexible_rate, expected
):
    # Act
    result = is_refundable(hours_before_checkin, flexible_rate)

    # Assert
    assert result is expected


@pytest.mark.parametrize(
    "hours_before_checkin, flexible_rate",
    [
        (-1, True),
        (-10, False),
    ],
)
def test_negative_hours_raises_value_error(hours_before_checkin, flexible_rate):
    # Act and Assert
    with pytest.raises(ValueError):
        is_refundable(hours_before_checkin, flexible_rate)


@pytest.mark.parametrize(
    "hours_before_checkin, flexible_rate",
    [
        ("48", True),
        (48.5, True),
        (True, True),
        (48, "True"),
        (48, 1),
    ],
)
def test_invalid_argument_types_raises_type_error(
    hours_before_checkin, flexible_rate
):
    # Act and Assert
    with pytest.raises(TypeError):
        is_refundable(hours_before_checkin, flexible_rate)