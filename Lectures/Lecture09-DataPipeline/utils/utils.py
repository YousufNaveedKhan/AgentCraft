def calculate_percentage(obtained, total):
    """Yeh percentage calculate karta hai."""
    return (obtained / total) * 100

def get_status(percentage):
    """Yeh percentage 50 ya ussay zyada hogi tou Pass/Fail return krega."""
    return "Pass" if percentage >= 50 else "Fail"