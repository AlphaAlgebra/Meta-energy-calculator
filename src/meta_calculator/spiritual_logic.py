def calculate_h(faith_level, community_size=1):
    """
    Calculates H (Spiritual Energy). 
    Faith is a scale of 1-100.
    """
    base_spiritual_constant = 10**7 # Your 'metaphorical novel' baseline
    h = (faith_level * base_spiritual_constant) * community_size

    return h
