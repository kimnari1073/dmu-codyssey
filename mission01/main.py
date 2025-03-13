# main.py mission 01
print('Hello Mars')

output_file = 'problematic_logs.txt'
try:
    with open('mission_computer_main.log', 'r', encoding='utf-8') as log_file:
        log_contents = log_file.read()
    # 문제되는 부분만 필터링 (예: "Oxygen tank unstable" 또는 "Oxygen tank explosion" 같은 줄)
    problem_lines = [line for line in log_contents if 'Oxygen tank' in line]

    # 문제되는 부분을 별도의 파일에 저장.
    if problem_lines:
        with open(output_file, 'w', encoding='utf-8') as output:
            output.writelines(problem_lines)
        print(f"문제가 되는 부분을 '{output_file}'에 저장했습니다.")
    else:
        print("문제가 되는 로그 항목이 없습니다.")
except FileNotFoundError:
    print('Error: mission_computer_main.log 파일을 찾을 수 없습니다.')
except Exception as e:
    print(f'Error: 알 수 없는 오류가 발생했습니다. ({e})')
    
print(log_contents)

#출력 결과를 시간의 역순으로 정렬해서 출력한다. 
with open('mission_computer_main.log','r',encoding='utf-8') as log_file:
    lines = log_file.readlines()  

for line in reversed(lines):
    print(line.strip())  

#출력 결과 중 문제가 되는 부분만 따로 파일로 저장한다. 
