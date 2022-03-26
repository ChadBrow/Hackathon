
from data import FOCUS_GROUPS

for i in FOCUS_GROUPS:
    print(FOCUS_GROUPS[i].performance)
for i in FOCUS_GROUPS:
    FOCUS_GROUPS[i].update()

for i in FOCUS_GROUPS:
    print(FOCUS_GROUPS[i].performance)