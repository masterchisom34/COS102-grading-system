score = int(input("enter your score (<=100)")

def get_grade(score):
    """Returns grade and remark based on score."""
    if 70 <= score <= 100:
        return 'A', 'Excellent'
    elif 60 <= score < 70:
        return 'B', 'Very Good'
    elif 50 <= score < 60:
        return 'C', 'Good'
    elif 45 <= score < 50:
        return 'D', 'Fair'
    elif 40 <= score < 45:
        return 'E', 'Pass'
    elif 0 <= score < 40:
        return 'F', 'Fail'
    else:
        return None, 'Invalid Score'

