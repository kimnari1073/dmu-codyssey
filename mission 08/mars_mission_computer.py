import platform
import json
import random
import time
import threading
import os

try:
    import psutil
except ImportError:
    raise ImportError("psutil 라이브러리를 설치해주세요. (pip install psutil)")

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
        with open('mars_mission_log.txt', 'a', encoding='utf-8') as log_file:
            log_file.write(log_message + '\n')
        return self.env_values

# MissionComputer 클래스 정의
class MissionComputer:
    def __init__(self):
        self.ds = DummySensor()
        self.env_values = self.ds.set_env()

        self.data_history = {
            'mars_base_internal_temperature': [],
            'mars_base_external_temperature': [],
            'mars_base_internal_humidity': [],
            'mars_base_external_illuminance': [],
            'mars_base_internal_co2': [],
            'mars_base_internal_oxygen': []
        }

        self.running = True
        self.input_event = threading.Event()

        self.settings = self.load_settings()  # ✅ settings 초기화

    def load_settings(self):
        default_settings = {
            "Operating System": True,
            "OS Version": True,
            "CPU Type": True,
            "CPU Core Count": True,
            "Total Memory (GB)": True,
            "CPU Usage (%)": True,
            "Memory Usage (%)": True
        }

        if os.path.exists("setting.txt"):
            try:
                with open("setting.txt", "r") as f:
                    return json.load(f)
            except Exception as e:
                print(f"[설정 파일 오류] 기본 설정을 사용합니다. 오류: {e}")
                return default_settings
        return default_settings

    def stop(self):
        self.running = False
        print("\nSystem stopped...")

    def calculate_average(self):
        avg_values = {}
        for key, values in self.data_history.items():
            avg_values[key] = sum(values) / len(values) if values else None

        print("\n======== 5-Minute Average Values ========")
        print(json.dumps(avg_values, indent=4))
        print("===========================================\n")

    def get_user_input(self):
        user_input = input("\nPress 'q' to stop or press 'Enter' to continue: ").strip().lower()
        if user_input == 'q':
            self.stop()
        self.input_event.set()

    def get_sensor_data(self):
        start_time = time.time()

        while self.running:
            self.env_values = self.ds.set_env()

            for key in self.env_values:
                self.data_history[key].append(self.env_values[key])
                if len(self.data_history[key]) > 60:
                    self.data_history[key].pop(0)

            print(json.dumps(self.env_values, indent=4))

            if time.time() - start_time >= 300:
                self.calculate_average()
                start_time = time.time()

            self.input_event.clear()
            input_thread = threading.Thread(target=self.get_user_input)
            input_thread.daemon = True
            input_thread.start()

            if not self.input_event.wait(timeout=5):
                print("\nNo input received, continuing...")

    def get_mission_computer_info(self):
        try:
            all_info = {
                "Operating System": platform.system(),
                "OS Version": platform.version(),
                "CPU Type": platform.processor(),
                "CPU Core Count": psutil.cpu_count(logical=False),
                "Total Memory (GB)": round(psutil.virtual_memory().total / (1024 ** 3), 2)
            }
            info = {k: v for k, v in all_info.items() if self.settings.get(k, True)}
            print("\n=== Mission Computer Info ===")
            print(json.dumps(info, indent=4))
            print("=============================\n")
            return info
        except Exception as e:
            print(f"시스템 정보 오류: {e}")
            return {}

    def get_mission_computer_load(self):
        try:
            all_load = {
                "CPU Usage (%)": psutil.cpu_percent(interval=1),
                "Memory Usage (%)": psutil.virtual_memory().percent
            }
            load = {k: v for k, v in all_load.items() if self.settings.get(k, True)}
            print("\n=== Mission Computer Load ===")
            print(json.dumps(load, indent=4))
            print("==============================\n")
            return load
        except Exception as e:
            print(f"시스템 부하 오류: {e}")
            return {}

if __name__ == "__main__":
    runComputer = MissionComputer()
    runComputer.get_mission_computer_info()
    runComputer.get_mission_computer_load()

