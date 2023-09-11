# zip the string till the end missing place filled with None

import itertools

print(list(itertools.zip_longest('vijay','jayavel')))
print(list(itertools.zip_longest('vijay','jayavel',fillvalue='@')))