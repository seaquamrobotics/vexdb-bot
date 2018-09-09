import re

TEAMID_REGEXP = "\d+[A-z]*"


def find_team_id(message):
    """Finds a valid team name in a message string, or None if one couldn't be
    found."""
    team_match = re.search(TEAMID_REGEXP, message)
    if team_match:
        return team_match.group(0)
    else:
        return None
