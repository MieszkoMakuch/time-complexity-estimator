## Install
```bash
pip install git+https://mieszko_makuch@bitbucket.org/mieszko_makuch/time-complexity-estimator.git
```
## Usage

Let's say you would like to compute time complexity of simple function that sorts list - `bubble_sort`.
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
    bubble_sort: Predicted time complexity: O(n^2), estimated time = -0.00038 + 2E-07*n^2
        Estimated time for 10^6 elements: [ 203242.87944452] [sec]
        Estimated no elements for 1 sec: 2218.58068214
    ```

###**Note** that:
- initializer must take one argument - number of elements
- initializer must return only one argument
- function which will be tested must take only one argument
- function which will be tested cannot mutate input data. In our case bubble_sort cannot sort the list in-place, that's why this line `l = lst[:]  # create a copy of lst`is necessary





# Programowanie w jezyku Python 2016/2017 zadanie 2

W celu oszacowania czasu wykonania programu kuszące jest czasem zalozyc liniowa złożoność obliczeniowa.
Czas sortowania możemy oszacować monotonicznej listy na 17.9 us dla 1000 elementów:

```bash
python -m timeit -s "s = list(range(1000))" "sorted(s)"
100000 loops, best of 3: 17.9 usec per loop
```


Próbując uogólnić ten wynik na listę składająca sie z 10^6 elementów spodziewalibyśmy się wyniku okolo 18 ms. Dokonując pomiaru otrzymujemy jednak czas o około 35% większy:

```bash
python -m timeit -s "s = list(range(1000000))" "sorted(s)"
10 loops, best of 3: 24.5 msec per loop
```


Przygotuj program do automatycznego wyznaczania złożoności obliczeniowej.

Program ten powinien otrzymywać na wejściu:
 -  Inicjalizacje odpowiednich struktur
 - Funkcje lub klase odpowiedzialna za wykonanie algorytmu
 - Kod odpowiedzialny za posprzątanie

Jako wynik powinniśmy otrzymać:
 - Informacje o przypuszczalnej klasie złożoności obliczeniowej ( O(n), O(n log(n)), O(n^2))
 - Funkcje umożliwiające przewidywanie jaki będzie czas wykonania programu dla zadanej wielkości problemu
 - Funkcję umożliwiającą przewidywanie jaki jest maksymalny rozmiar problemu obliczeniowego dla zadanego czasu

Wyznaczanie złożoności niektórych algorytmów może trwać bardzo długo. Aby umożliwić wykonanie programu w rozsądnym czasie program powinien posiadać ograniczenie w postaci parametru “timeout” ustawionego domyślnie na 30 sekund. W przypadku nie otrzymania ostatecznego wyniku w założonym czasie program powinien zwrócić wynik cząstkowy (np “złożoność gorsza niż O(n)”).

Program powinien dać się zainstalować jako pakiet pip bezpośrednio z repozytorium (np używając komendy
`pip install git+https://github.com/AGHPythonCourse2017/zad01-grzanka.git`)

Program powinien wykorzystywać następujące elementy:
 - Logger
 - dekoratory
 - własne wyjątki

Program powinien przejść test flake8 (zgodność z PEP8).

Za wykonania zadania mozna zdobyc maksymalnie 0.9 punktu.

Dodatkowo trzeba wykonać trzy recenzje rozwiązań zadania nr 1 i umieścić w repozytorium w pliku review.txt odnośniki do odpowiednich “Pull request”. Ten fragment zadania umożliwia zdobycie maksymalnie 0.1 punktu.

Tresc zadania w Google Drive: https://goo.gl/r87sPE

Termin oddania zadania: 8 maja 2017, 20:00
