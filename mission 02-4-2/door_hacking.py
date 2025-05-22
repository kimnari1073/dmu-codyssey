def caesar_cipher_decode(target_text):
    dictionary = ["secret", "login", "admin", "hello", "apple", "world", "guest", "pass"]
    results = []

    for shift in range(1, 26):
        decoded = ''
        for ch in target_text:
            if 'a' <= ch <= 'z':
                decoded += chr((ord(ch) - ord('a') - shift) % 26 + ord('a'))
            elif '0' <= ch <= '9':
                decoded += chr((ord(ch) - ord('0') - shift) % 10 + ord('0'))
            else:
                decoded += ch

        print(f"{shift:2d}: {decoded}")
        results.append(decoded)

        # 보너스: 사전 키워드 발견 시 자동 저장
        for word in dictionary:
            if word in decoded:
                print(f"\n[자동 저장] 키워드 '{word}' 발견됨 → result.txt에 저장합니다.")
                try:
                    with open("result.txt", "w") as f:
                        f.write(decoded)
                    print("저장 완료.")
                except Exception as e:
                    print(f"파일 저장 중 오류 발생: {e}")
                return

    # 사용자 수동 선택
    try:
        choice = int(input("\n해독된 번호를 입력하세요: "))
        if 1 <= choice <= 25:
            final_result = results[choice - 1]
            with open("result.txt", "w") as f:
                f.write(final_result)
            print("result.txt에 저장 완료.")
        else:
            print("잘못된 번호입니다.")
    except Exception as e:
        print(f"입력 또는 저장 중 오류 발생: {e}")

# 메인 실행
def main():
    try:
        with open("password.txt", "r") as f:
            password = f.read().strip()
            if len(password) != 6:
                print("암호는 정확히 6자리여야 합니다.")
                return
            caesar_cipher_decode(password)
    except FileNotFoundError:
        print("password.txt 파일을 찾을 수 없습니다.")
    except Exception as e:
        print(f"파일 읽기 중 오류 발생: {e}")

# 실행
if __name__ == "__main__":
    main()
