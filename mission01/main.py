# main.py mission 01
print('Hello Mars')

problem_lines=[]
output_file = 'problematic_logs.txt'

try:
    with open('mission_computer_main.log', 'r', encoding='utf-8') as log_file:
        log_contents = log_file.readlines()
    
    # mission_computer_main.log 파일 출력 & "Oxygen tank" 단어 포함 시 배열 저장
    for line in log_contents:
        print(line.strip()) 
        if 'Oxygen tank' in line:
            problem_lines.append(line)

    # "Oxygen tank"단어가 포함된 문장을 별도의 파일에 저장.
    if problem_lines:
        with open(output_file, 'w', encoding='utf-8') as output:
            output.writelines(problem_lines)
        print(f"문제가 되는 부분을 '{output_file}'에 저장했습니다.")
        print("문제가 되는 부분은 다음과 같습니다:")
        for line in problem_lines:
            print(line)
    else:
        print("문제가 되는 로그 항목이 없습니다.")
except FileNotFoundError :
    print('Error: mission_computer_main.log 파일을 찾을 수 없습니다.')
except Exception as e:
    print(f'Error: 알 수 없는 오류가 발생했습니다. ({e})')
    
#역순 출력
with open('mission_computer_main.log','r',encoding='utf-8') as log_file:
    lines = log_file.readlines()  

print("출력 결과를 시간의 역순으로 정렬해서 출력한다.")
for line in reversed(lines):
    print(line.strip())  
