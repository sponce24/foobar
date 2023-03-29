#####################################
#   Level 2 - Elevator Maintenance  #
#           27/03/2023              #
#####################################
# Elevator versions are represented by a series of numbers, divided up into major, minor and revision integers.
# New versions of an elevator increase the major number, e.g. 1, 2, 3, and so on.
# When new features are added to an elevator without being a complete new version,
# a second number named "minor" can be used to represent those new additions, e.g. 1.0, 1.1, 1.2, etc.
# Small fixes or maintenance work can be represented by a third number named "revision", e.g. 1.1.1, 1.1.2, 1.2.0, and so on.
# The number zero can be used as a major for pre-release versions of elevators, e.g. 0.1, 0.5, 0.9.2, etc
# (Commander Lambda is careful to always beta test her new technology, with her loyal henchmen as subjects!).
#
# Given a list of elevator versions represented as strings, write a function solution(l)
# that returns the same list sorted in ascending order by major, minor, and revision number so that you can identify the current elevator version.
# The versions in list l will always contain major numbers, but minor and revision numbers are optional.
# If the version contains a revision number, then it will also have a minor number.

# For example, given the list l as ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"], the function solution(l)
# would return the list ["1.0", "1.0.2", "1.0.12", "1.1.2", "1.3.3"].
# If two or more versions are equivalent but one version contains more numbers than the others, then these versions must be sorted
# ascending based on how many numbers they have, e.g ["1", "1.0", "1.0.0"].
# The number of elements in the list l will be at least 1 and will not exceed 100.
####################################

def solution(l):
  n = len(l)
  array = {}
  array.setdefault('major', [])
  array.setdefault('minor', [])
  array.setdefault('revision', [])
  for ii in range(n):
    tmp = l[ii]
    ncar = len(tmp)
    point = 0
    point_pos = 0
    for jj in range(ncar):
      car = tmp[jj]
      if car == '.':
        if point == 0:
          array['major'].append(int(tmp[point_pos:jj]))
        if point == 1:
          array['minor'].append(int(tmp[point_pos:jj]))
        point += 1
        point_pos = jj + 1
    if point == 2:
      array['revision'].append(int(tmp[point_pos:]))
    if point == 1:
      array['minor'].append(int(tmp[point_pos:jj+1]))
      array['revision'].append(-1)
    if point == 0:
      array['major'].append(int(tmp[point_pos:jj+1]))
      array['minor'].append(-1)
      array['revision'].append(-1)

  sort_maj = sorted(range(len(array['major'])), key=array['major'].__getitem__)

  start = 0
  min_array = []
  min_index = []
  global_sort = []
  for ii in range(n):
    if array['major'][sort_maj[ii]] == array['major'][sort_maj[start]]:
      min_array.append(array['minor'][sort_maj[ii]])
      min_index.append(sort_maj[ii])
    else:
      sort_min = sorted(range(len(min_array)), key=min_array.__getitem__)
      start = ii
      for jj in range(len(min_array)):
        global_sort.append(min_index[sort_min[jj]])
      min_array = []
      min_index = []
      min_array.append(array['minor'][sort_maj[ii]])
      min_index.append(sort_maj[ii])
    if ii == n-1:
      sort_min = sorted(range(len(min_array)), key=min_array.__getitem__)
      start = ii
      for jj in range(len(min_array)):
        global_sort.append(min_index[sort_min[jj]])

  start = 0
  min_array = []
  min_index = []
  global_sort2 = []
  for ii in range(n):
    if array['minor'][global_sort[ii]] == array['minor'][global_sort[start]]:
      min_array.append(array['revision'][global_sort[ii]])
      min_index.append(global_sort[ii])
    else:
      sort_min = sorted(range(len(min_array)), key=min_array.__getitem__)
      start = ii
      for jj in range(len(min_array)):
        global_sort2.append(min_index[sort_min[jj]])
      min_array = []
      min_index = []
      min_array.append(array['revision'][global_sort[ii]])
      min_index.append(global_sort[ii])
    if ii == n-1:
      sort_min = sorted(range(len(min_array)), key=min_array.__getitem__)
      start = ii
      for jj in range(len(min_array)):
        global_sort2.append(min_index[sort_min[jj]])

  sol = []
  for ii in range(n):
    sol.append(l[global_sort2[ii]])

  return sol

# For testing
#  for ii in range(n):
#    print(l[global_sort2[ii]])
#solution(["1.1.2", "3.0", "2.3.3", "1.0.12", "1.0.2", "2.1.3"])
#solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"])


