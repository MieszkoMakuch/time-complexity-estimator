# Time complexity estimator

Time complexity estimator written in python 3. Provides tools to estimate functions time complexity from execution time.

## Install
```bash
pip install time_complexity_estimator
```
## Examples
You can find a couple of examples in time_complexity_estimator/examples

```bash
git clone https://mieszko_makuch@bitbucket.org/mieszko_makuch/time-complexity-estimator.git

cd time-complexity-estimator/time_complexity_estimator/examples/

# Run basic_run.py or example_run.py
python basic_run.py
python example_run.py
```
For `basic_run.py` you should see something like this:
```bash
bubble_sort: Could not perform all measurements. Predicted time complexity: O(n^2), estimated time = -0.00011 + 1.5E-07*n^2
    Estimated time for 10^6 elements: [ 154102.68140071] [sec]
    Estimated no elements for 1 sec: 2547.53310879
```


## Usage

Let's say you would like to compute time complexity of simple function that sorts list - `bubble_sort`:
```python
def bubble_sort(lst):
    l = lst[:]  # create a copy of lst
    n = len(l)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, n):
            if l[i - 1] > l[i]:
                l[i], l[i - 1] = l[i - 1:i + 1]
                swapped = True
    return l
```
To do this:
1. Write a function which will provide some random data - in this case random list of n elements - e.g. `bubble_sort_initializer`:
    ```python
    import random
    
    def bubble_sort_initializer(n):
        return [random.randint(-10000, 10000) for _ in range(n)]
    ```
2. Put `bubble_sort` and `bubble_sort_initializer` to one file e.g. `input.py`
3. Create a script e.g. `run.py`:
    ```python
    from time_complexity_estimator.estimator import estimate_time_complexity


    msg, time_fun, n_elements_fun = estimate_time_complexity(module_name="input",
                                                             file_path="input.py",
                                                             initializer_name="bubble_sort_initializer",
                                                             fun_to_test_name="bubble_sort",
                                                             timeout_after=5)
    print(msg)
    print("    Estimated time for 10^6 elements: " + str(time_fun(10 ** 6)) + " [sec]")
    print("    Estimated no elements for 1 sec: " + str(n_elements_fun(1)))
    ```
    Output:
    ```
    bubble_sort: Predicted time complexity: O(n^2), estimated time = -0.00011 + 1.9E-07*n^2
    	Estimated time for 10^6 elements: [ 191506.10531756] [sec]
    	Estimated no elements for 1 sec: 2285
    ```

### **Note** that:
- initializer must take one argument - number of elements
- initializer must return only one argument
- function which will be tested must take only one argument
- function which will be tested cannot mutate input data. In our case bubble_sort cannot sort the list in-place, that's why this line `l = lst[:]  # create a copy of lst`is necessary

# Compatibility
Python 3, numpy, scipy is required. 