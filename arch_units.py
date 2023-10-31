import math

# my first recurtion!
def reduce(vals, factor= 2):
    while vals[0] % factor == 0 and vals[1] % factor == 0:
        vals[0], vals[1] = vals[0] / factor, vals[1] / factor
        reduce(vals)
    else:
        vals[0], vals[1] = int(vals[0]), int(vals[1])
        return vals
    

def frac(val, denominator = 16, factor= 2):
    denominator = 1 / denominator
    int_val = int(val) # will always be a floor
    remainder = (val - int_val)
    ceiling_val = math.ceil(remainder / denominator)
    floor_val = math.floor(remainder / denominator)
    if remainder % denominator == 0:
        remainder, denominator = reduce([remainder * 1 / denominator, 1 / denominator], factor)
        if remainder == 1 and denominator == 1:
            return str(int_val + 1) + 'in. '
        else:
            return str(int_val) + '-' + str(int(remainder)) + '/' + str(denominator) + 'in'
    elif abs(remainder - floor_val * denominator) > abs(remainder - ceiling_val * denominator):
        ceiling_val, denominator = reduce([ceiling_val, 1 / denominator], factor)
        if ceiling_val == 1 and denominator == 1:
            return str(int_val + 1) + 'in. ' + str(abs((ceiling_val / denominator) - remainder)) + 'in. over true val'
        else:
            return str(int_val) + '-' + str(ceiling_val) + '/' + str(denominator) + 'in, ' + str(abs((ceiling_val / denominator) - remainder)) + 'in. over true val'
    elif abs(remainder - ceiling_val * denominator) > abs(remainder - floor_val * denominator):
        floor_val, denominator = reduce([floor_val, 1 / denominator], factor)
        if floor_val == 1 and denominator == 1:
            return str(int_val + 1) + 'in. '  + str(abs((floor_val / denominator) - remainder)) + 'in. under true val'
        else:
            return str(int_val) + '-' + str(floor_val) + '/' + str(denominator) + 'in, ' + str(abs((floor_val / denominator) - remainder)) + 'in. under true val'
    else:
        return 'error :('
        

def arch(val, denominator= 16, factor= 2):
    feet = int(val) // 12
    inches = val - (feet * 12)
    if inches == 0:
        return str(int(feet)) + 'ft'
    else:
        return str(int(feet)) + 'ft ' + frac(inches, denominator, factor)
    

arch(111.98)