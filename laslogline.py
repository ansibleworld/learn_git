import re
from typing import Optional

def parse_login_event(log_line: str) -> Optional[dict[str, str]]:
    if not isinstance(log_line , str):
        raise TypeError
    pattern = r"user: '(?P<username>.*?)'.*?status:'(?P<status>.*?)'"
    matchs = re.search(pattern , log_line)
    if matchs:
        return matchs.groupdict()
    else:
        return None