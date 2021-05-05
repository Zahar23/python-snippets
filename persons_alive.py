"""
Given a list of people with their birth and death years (all between 1900 and 2000),
find the year with the most number of people alive.
"""

from pprint import pprint

persons = [(1900, 1910), (1905, 1920), (1907, 1918), (1920, 1925)]

years_slices = []
for p in persons:
    years_slices.append((p[0], '+1'))
    years_slices.append((p[1], '-1'))

sorted_slices = sorted(years_slices, key=lambda year: year[0])

currently_alive = 0
results = []
for ss in sorted_slices:
    if ss[1] == '+1':
        currently_alive = currently_alive + 1
        results.append((ss[0], currently_alive))
    else:
        currently_alive = currently_alive - 1
pprint(results)

years_slices = []
for p in persons:
    years_slices.append((p[0], 1))
    years_slices.append((p[1], -1))

sorted_slices = sorted(years_slices, key=lambda y: y[0])

currently_alive = 0
results = []
for yy in sorted_slices:
    currently_alive = currently_alive + yy[1]
    if yy[1] > 0:
        results.append((yy[0], currently_alive))
pprint(max(results, key=lambda r: r[1]))



