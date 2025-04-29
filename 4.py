with open('CdSe_CdZnS Core_Shell.txt', 'r') as file:
    lines = file.readlines()

frequencies = []
amplitudes = []
for line in lines:
    parts = line.strip().replace(',', '.').split()
    if len(parts) >= 2:
        frequencies.append(float(parts[0]))
        amplitudes.append(float(parts[1]))

reflected_amplitudes = [-a for a in amplitudes]

sum_amplitudes = 0.0
count = 0
for a in reflected_amplitudes:
    sum_amplitudes += a
    count += 1
mean = sum_amplitudes / count

sum_squared_diff = 0.0
for a in reflected_amplitudes:
    diff = a - mean
    sum_squared_diff += diff * diff
variance = sum_squared_diff / count
std_deviation = variance ** 0.5  

print("Срзнач:" , mean )
print("Срквоткл:" , std_deviation)
