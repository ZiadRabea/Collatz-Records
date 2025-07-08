def get_first_three_stage_numbers(stage):
    n = 2 ** stage
    return [(k + 1) * n - 1 for k in range(3)]
    
stage = 10000  # you can change this value to test different stages
print(f"First 3 numbers at stage {stage}: {get_first_three_stage_numbers(stage)}")
