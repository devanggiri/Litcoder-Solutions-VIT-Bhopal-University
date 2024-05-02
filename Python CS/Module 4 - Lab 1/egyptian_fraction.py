def egyptian_fraction(numerator, denominator):
    result = []

    while numerator != 0:
        unit_fraction_denominator = (denominator + numerator - 1) // numerator
        result.append(unit_fraction_denominator)

        numerator = numerator * unit_fraction_denominator - denominator
        denominator = denominator * unit_fraction_denominator

    return result

# Example usage:
numerator = 6
denominator = 14

result = egyptian_fraction(numerator, denominator)
print(*result)
