inventory_list = []
header = ''
with open('Mars_Base_Inventory_List.csv', 'r', encoding='utf-8') as file:
    header = file.readline()  # 헤더 저장
    for line in file:
        print(line) #파일 각 줄을 프린트
        data = line.strip().split(',')
        inventory_list.append({
            'Substance': data[0],
            'Weight (g/cm³)': data[1],
            'Specific Gravity': data[2],
            'Strength': data[3],
            'Flammability': data[4]
        })

# 인화성 지수에 따른 정렬 (내림차순)
sorted_inventory = sorted(inventory_list, key=lambda x: x['Flammability'], reverse=True)

# 인화성 지수(flammability)가 0.7 이상인 항목을 필터링
flammable_items = [item for item in sorted_inventory if float(item['Flammability']) >= 0.7]

with open('Mars_Base_Inventory_danger.csv', 'w', encoding='utf-8') as file:
    file.write(header)

    # 인화성 지수가 0.7 이상인 항목 출력 & 파일 저장
    for item in flammable_items:
        print(f"{item['Substance']},{item['Weight (g/cm³)']},{item['Specific Gravity']},{item['Strength']},{item['Flammability']}\n")
        file.write(f"{item['Substance']},{item['Weight (g/cm³)']},{item['Specific Gravity']},{item['Strength']},{item['Flammability']}\n")


