from time_complexity_estimator.estimator import estimate_time_complexity

msg, time_fun, n_elements_fun = estimate_time_complexity(module_name="example_input",
                                                         file_path="example_input.py",
                                                         initializer_name="bubble_sort_initializer",
                                                         fun_to_test_name="bubble_sort",
                                                         timeout_after=5)
print(msg)
print("    Estimated time for 10^6 elements: " + str(time_fun(10 ** 6)) + " [sec]")
print("    Estimated no elements for 1 sec: " + str(n_elements_fun(1)))
