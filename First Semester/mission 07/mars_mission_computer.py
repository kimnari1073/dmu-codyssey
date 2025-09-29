import time
from datetime import datetime
import random
import json
import threading

# DummySensor 클래스 정의
class DummySensor:
    def __init__(self):
        self.env_values = {
            'mars_base_internal_temperature': None,
            'mars_base_external_temperature': None,
            'mars_base_internal_humidity': None,
            'mars_base_external_illuminance': None,
            'mars_base_internal_co2': None,
            'mars_base_internal_oxygen': None
        }

    def set_env(self):
        self.env_values['mars_base_internal_temperature'] = random.uniform(18, 30)
        self.env_values['mars_base_external_temperature'] = random.uniform(0, 21)
        self.env_values['mars_base_internal_humidity'] = random.uniform(50, 60)
        self.env_values['mars_base_external_illuminance'] = random.uniform(500, 715)
        self.env_values['mars_base_internal_co2'] = random.uniform(0.02, 0.1)
        self.env_values['mars_base_internal_oxygen'] = random.uniform(4, 7)
        
        return self.env_values

    def get_env(self):
        log_message = json.dumps(self.env_values, indent=4)

        # 파일에 로그 작성
        with open('mars_mission_log.txt', 'a', encoding='utf-8') as log_file:
            log_file.write(log_message + '\n')

        return self.env_values

# MissionComputer 클래스 정의
class MissionComputer:
    def __init__(self):
        self.ds = DummySensor()
        self.env_values = self.ds.set_env()

        # 최근 5분 데이터를 저장할 리스트 (최대 길이 60개 → 5초마다 값 갱신)
        self.data_history = {
            'mars_base_internal_temperature': [],
            'mars_base_external_temperature': [],
            'mars_base_internal_humidity': [],
            'mars_base_external_illuminance': [],
            'mars_base_internal_co2': [],
            'mars_base_internal_oxygen': []
        }

        self.running = True
        self.input_event = threading.Event()  # 입력 상태 관리

    def stop(self):
        """출력 중단"""
        self.running = False
        print("\nSystem stopped...")

    def calculate_average(self):
        """5분 평균 값 출력"""
        avg_values = {}
        for key, values in self.data_history.items():
            if values:
                avg_values[key] = sum(values) / len(values)
            else:
                avg_values[key] = None

        print("\n======== 5-Minute Average Values ========")
        print(json.dumps(avg_values, indent=4))
        print("===========================================\n")

    def get_user_input(self):
        """입력 받기 (별도 스레드에서 처리)"""
        user_input = input("\nPress 'q' to stop or press 'Enter' to continue: ").strip().lower()
        if user_input == 'q':
            self.stop()

        self.input_event.set()  # 입력 상태를 True로 설정

    def get_sensor_data(self):
        start_time = time.time()

        while self.running:
            # DummySensor에서 값 가져오기
            self.env_values = self.ds.set_env()

            # 최근 값 저장 (최대 60개 유지)
            for key in self.env_values:
                self.data_history[key].append(self.env_values[key])
                if len(self.data_history[key]) > 60:  # 60개까지만 유지
                    self.data_history[key].pop(0)

            # json 형태로 화면에 출력
            json_data = json.dumps(self.env_values, indent=4)
            print(json_data)

            # 5분마다 평균 출력
            if time.time() - start_time >= 300:  # 300초 = 5분
                self.calculate_average()
                start_time = time.time()

            # ✅ 입력 감지 (별도 스레드에서 처리)
            self.input_event.clear()
            input_thread = threading.Thread(target=self.get_user_input)
            input_thread.daemon = True
            input_thread.start()

            # 입력 대기 (5초 대기 후 다음 루프로 이동)
            if not self.input_event.wait(timeout=5):
                print("\nNo input received, continuing...")

# 인스턴스 생성 및 실행
if __name__ == "__main__":
    RunComputer = MissionComputer()
    RunComputer.get_sensor_data()
