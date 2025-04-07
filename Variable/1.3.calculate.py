# integer
print( 50 * 2 )
print( 1/500 )
print( 4 * 3 - 1 )
print( 3.14 * 2 * 200 )
print( 1.0/20 )

# The following (sau đây) expressions are more complicated calculations.
# Ignore them if tou haven't learned anything about each type.

# Decimal: more accurate(chính xác) than float
import decimal
print(decimal.Decimal(9876) + decimal.Decimal("54321.012345678987654321"))

# Fraction (phân số)
import fractions
print(fractions.Fraction(1,3)) # 1/3
print(fractions.Fraction(4,6)) # 2/3
print(3 * fractions.Fraction(1, 3)) # 1

# Complex (Tổ hợp)
print(3-4j)
print(3-4J)
print(complex(3,-4))
print(3 + 1J * 3j)