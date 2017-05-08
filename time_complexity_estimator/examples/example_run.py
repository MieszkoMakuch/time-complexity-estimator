from time_complexity_estimator.estimator import estimate_time_complexity


def run_time_complexity(function_name, timeout_after=5):
    initializer_name = function_name + "_initializer"

    message, estimated_time, estimated_n_elements = estimate_time_complexity("example_input", "example_input.py",
                                                                             initializer_name, function_name,
                                                                             timeout_after=timeout_after)
    print(message)
    for i in range(1, 9):
        print("    Estimated time for 10^" + str(i) + " elements: " + str(estimated_time(10 ** i)) + " [sec]")

    init_time = 0.00001
    for i in range(1, 9):
        time = init_time * 10 ** i
        print("    Estimated no elements for " + str(time) + " sec: " + str(estimated_n_elements(time)))


# first_element
run_time_complexity("first_element")

# find_max
run_time_complexity("find_max")

# sorted
run_time_complexity("sorted_wrapper")

# bubble_sort
run_time_complexity("bubble_sort")

# cubic_function
run_time_complexity("cubic_function")

# permute
run_time_complexity("permute", timeout_after=70)
