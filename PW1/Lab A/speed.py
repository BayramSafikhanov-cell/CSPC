import time
from decay import simulate_loop, simulate

N0 = 200000

start = time.perf_counter()
simulate_loop(N0, 0.4)
loop_time = time.perf_counter() - start

start = time.perf_counter()
simulate(N0, 0.4)
numpy_time = time.perf_counter() - start

print(f"loop:  {loop_time:.4f} s")
print(f"numpy: {numpy_time:.4f} s")
print(f"speed-up: {loop_time / numpy_time:.1f}x faster")