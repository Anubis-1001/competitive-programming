def countDigitOne(n):
    power = 1
    ones_count = 0
    while( power <= n ):
        trimmed_num = n // power
        current_digit = trimmed_num % 10
        ones_count += ( trimmed_num // 10 ) * power
        if ( current_digit > 1 ):
            ones_count += power
        else:
            ones_count += current_digit * ( n % power + 1 )

        power*=10
    return ones_count

print( countDigitOne( 13 ) )
print( countDigitOne( 0 ) )
