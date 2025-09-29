inventory_list = []
header = ''

# 파일 읽기 예외 처리 (파일이 존재하지 않을 경우 대비)
try:
    with open('Mars_Base_Inventory_List.csv', 'r', encoding='utf-8') as file:
        header = file.readline().strip()  # 헤더 저장
        for line in file:
            data = line.strip().split(',')
            try:
                inventory_list.append({
                    'Substance': data[0],
                    'Weight (g/cm³)': data[1],
                    'Specific Gravity': data[2],
                    'Strength': data[3],
                    'Flammability': float(data[4])  # 변환 오류 방지
                })
            except (IndexError, ValueError):  # 데이터 부족 또는 숫자 변환 오류 방지
                continue
except FileNotFoundError:
    print("❌ 파일을 찾을 수 없습니다: Mars_Base_Inventory_List.csv")
    exit()

# 인화성 지수에 따른 정렬 (내림차순)
sorted_inventory = sorted(inventory_list, key=lambda x: x['Flammability'], reverse=True)

# 인화성 지수(flammability)가 0.7 이상인 항목을 필터링
flammable_items = [item for item in sorted_inventory if item['Flammability'] >= 0.7]

# 파일 쓰기 예외 처리
try:
    with open('Mars_Base_Inventory_danger.csv', 'w', encoding='utf-8') as file:
        file.write(header + "\n")
        for item in flammable_items:
            file.write(f"{item['Substance']},{item['Weight (g/cm³)']},{item['Specific Gravity']},{item['Strength']},{item['Flammability']}\n")
except IOError:
    print("❌ 파일을 저장하는 중 오류가 발생했습니다.")
    
    
#보너스 문제
try:
    with open('Mars_Base_Inventory_List.bin', 'wb') as bin_file:
        for item in sorted_inventory:
            try:
                # 데이터를 ','로 연결 후 바이트 변환하여 저장
                line = f"{item['Substance']},{item['Weight (g/cm³)']},{item['Specific Gravity']},{item['Strength']},{item['Flammability']}\n"
                bin_file.write(line.encode('utf-8'))
            except Exception as e:
                print(f"데이터 변환 오류: {e}")
except Exception as e:
    print(f"파일 저장 오류: {e}")

# 2. 이진 파일에서 읽어서 출력
try:
    with open('Mars_Base_Inventory_List.bin', 'rb') as bin_file:
        binary_data = bin_file.read()
        decoded_data = binary_data.decode('utf-8')  # 바이트를 문자열로 변환
        lines = decoded_data.strip().split("\n")  # 줄 단위로 리스트 변환

        print("=== 이진 파일에서 읽은 데이터 ===")
        for line in lines:
            print(line)
except Exception as e:
    print(f"파일 읽기 오류: {e}")