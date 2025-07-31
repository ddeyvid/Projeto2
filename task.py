from numpy import array, mean, std

tempos_ciclo = array([5.5, 5.7, 5.9, 6.0, 5.8, 5.6, 5.7, 7.2, 4.8])
print(tempos_ciclo[(tempos_ciclo < mean(tempos_ciclo) - 2 * std(tempos_ciclo)) | (tempos_ciclo > mean(tempos_ciclo) + 2 * std(tempos_ciclo))])