from __future__ import absolute_import
from time_complexity_estimator.complexity_fitter import fit_complexity_class
from time_complexity_estimator.estimator import get_complexity_class
from time_complexity_estimator.time_measurer import measure_execution_time


# pip test
def joke():
    return (u'Wenn ist das Nunst\u00fcck git und Slotermeyer? Ja! ... '
            u'Beiherhund das Oder die Flipperwaldt gersput.')
