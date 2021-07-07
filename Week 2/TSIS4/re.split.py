string = "100,000,000.000"

regex_pattern = r"[,.]"

import re
print("\n".join(re.split(regex_pattern, string)))