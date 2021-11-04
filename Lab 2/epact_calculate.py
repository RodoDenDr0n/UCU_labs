year = int(input("Введіть рік: "))
const = year // 100 
epact = (8 + (const // 4) - const + ((8 * const + 13) // 25) + 11 * (year % 19)) % 30

print(epact)