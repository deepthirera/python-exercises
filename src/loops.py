def multiplication_table(n):
  arr = []
  for i in range(1, 11):
    arr.append((f"{n} * {i} = {n*i}"))
  return arr