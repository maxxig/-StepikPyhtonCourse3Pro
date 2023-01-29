from functools import lru_cache
import sys
@lru_cache(typed=True)
def sort_w_cache(str):
    return ''.join(sorted(l.strip())    )

for l in sys.stdin:
    print(sort_w_cache(l))

print(sort_w_cache.cache_info())