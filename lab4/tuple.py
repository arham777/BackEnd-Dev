# Immutable

def convert_seconds(sec):
    hours= sec // 3600
    minutes = (sec - hours * 3600) // 60
    remaining_sec = sec - hours *3600 - minutes * 60
    return hours, minutes, remaining_sec

result = convert_seconds(5000)
print(type(result))
print(result)

# result.pop() =>  cant be change as it is immutable

hours , minutes , seconds = convert_seconds(5000) # Unpacking
print(hours, minutes, seconds)
print(hours, minutes)
