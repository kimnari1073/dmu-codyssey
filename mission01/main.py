# main.py

def main():
    print('Hello Mars')
    
    try:
        with open('mission_computer_main.log', 'r', encoding='utf-8') as log_file:
            log_contents = log_file.read()
            print(log_contents)
    except FileNotFoundError:
        print('Error: mission_computer_main.log 파일을 찾을 수 없습니다.')
    except PermissionError:
        print('Error: 파일에 접근할 권한이 없습니다.')
    except Exception as e:
        print(f'Error: 알 수 없는 오류가 발생했습니다. ({e})')

if __name__ == '__main__':
    main()