def binary_array_to_number(arr):
  return sum(val * 2 ** i for i, val in (enumerate(reversed(arr))))
