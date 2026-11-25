def calculate_booking_cost(nights, nightly_rate_cents):
    """Calculate the total room charge from the stay length and nightly rate."""
    if type(nights) is not int or type(nightly_rate_cents) is not int:
        raise TypeError("invalid argument type")
    
    if not 1 <= nights <= 30 or nightly_rate_cents < 0:
        raise ValueError("argument outside permitted range")
    
    charged_nights = nights - 1 if nights >= 7 else nights

    return charged_nights * nightly_rate_cents
