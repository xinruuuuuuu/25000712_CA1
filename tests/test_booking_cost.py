import pytest
from src.booking_cost import calculate_booking_cost

@pytest.mark.parametrize(
    "nights, nightly_rate_cents, expected",
    [
        (1, 10000, 10000),  
        (6, 10000, 60000),  
        (7, 10000, 70000),  
        (30, 10000, 300000), 
        (5, 0, 0), 
    ],
)

def test_valid_booking_inputs_returns_expected_cost(
    nights, nightly_rate_cents, expected
):
    # Act
    result = calculate_booking_cost(nights, nightly_rate_cents)

    # Assert
    assert result == expected

@pytest.mark.parametrize(
    "nights, nightly_rate_cents",
    [
        (0, 10000),
        (-1, 10000),
        (31, 10000),
        (5, -1),
    ],
)
def test_out_of_range_inputs_raises_value_error(nights, nightly_rate_cents):
    # Act and Assert
    with pytest.raises(ValueError):
        calculate_booking_cost(nights, nightly_rate_cents)