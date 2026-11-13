import numpy as np 
import timeit  
rng = np.random.default_rng(42) 
sample_size=100_000#changed the sample size from 1000_000 to 100_000
latency_ms = rng.uniform(5, 250, sample_size) 
def loop_version(): 
    result = []  
    for value in latency_ms: 
        seconds = value / 1000.0 
        result.append(seconds ** 2) 
    return result 
def vectorized_version(): 
    seconds = latency_ms / 1000.0 
    return seconds ** 2 
loop_time = timeit.timeit(loop_version, number=1) 
vector_time = timeit.timeit(vectorized_version, number=3) / 3 
result = vectorized_version() 
print("First five squared latency values:", result[:5]) 
print(f"Loop time: {loop_time:.4f} s") 
print(f"Vectorized time: {vector_time:.4f} s") 
print(f"Approximate speed-up: {loop_time/vector_time:.1f}x")