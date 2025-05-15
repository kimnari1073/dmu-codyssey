import zipfile
import itertools
import string
import time
import multiprocessing
import os

zip_filename = 'emergency_storage_key.zip'
charset = string.ascii_lowercase + string.digits  # 총 36글자
max_length = 6
found_flag = multiprocessing.Value('b', False)
attempts_counter = multiprocessing.Value('i', 0)

def try_passwords(start_chars):
    try:
        zip_file = zipfile.ZipFile(zip_filename)
    except FileNotFoundError:
        print("[오류] ZIP 파일이 존재하지 않습니다.")
        return

    start_time = time.time()

    for pwd_tuple in itertools.product(charset, repeat=max_length - 1):
        if found_flag.value:
            return
        password = start_chars + ''.join(pwd_tuple)
        with attempts_counter.get_lock():
            attempts_counter.value += 1
            if attempts_counter.value % 10000 == 0:
                elapsed = time.time() - start_time
                print(f"[진행중] {attempts_counter.value}회 시도됨, 경과: {elapsed:.2f}초, 현재: {password}")
        try:
            zip_file.extractall(pwd=bytes(password, 'utf-8'))
            with found_flag.get_lock():
                found_flag.value = True
            print(f"[성공] 비밀번호: {password}")
            with open("password.txt", "w") as f:
                f.write(password)
            return
        except:
            continue

def unlock_zip():
    print("[*] 병렬 해제 시도 시작...")
    start_time = time.time()

    processes = []
    for c in charset:
        p = multiprocessing.Process(target=try_passwords, args=(c,))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    elapsed = time.time() - start_time
    if found_flag.value:
        print(f"[완료] 성공적으로 해제됨. 총 시도: {attempts_counter.value}, 소요 시간: {elapsed:.2f}초")
    else:
        print("[실패] 비밀번호를 찾지 못했습니다.")

if __name__ == "__main__":
    unlock_zip()
