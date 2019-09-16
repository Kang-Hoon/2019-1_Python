# 스크립트 모드입니다.
#

import time
now = time.time()
thisYear = int(1970 + now//(365*24*3600))
print("올해는 " + str(thisYear)+"입니다.")
