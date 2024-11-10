# Usando rangos para modificar listas


nums = [1, 2, 3, 4, 5]

# Esto es posible, pero no se comporta de manera muy intuitiva
nums[1:3] = [0, 0, 0, 0, 0]
# range(1, 5) -> [1, 2, 3, 4]
print(nums)

