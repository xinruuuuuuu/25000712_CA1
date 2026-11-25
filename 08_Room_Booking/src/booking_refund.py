def is_refundable(hours_before_checkin, flexible_rate):
    """Determine whether the cancellation time and rate allow a refund."""
    if type(hours_before_checkin) is not int or type(flexible_rate) is not bool:
        raise TypeError("invalid argument type")
    
    if hours_before_checkin < 0:
        raise ValueError("argument outside permitted range")
    
    return flexible_rate and hours_before_checkin > 48
