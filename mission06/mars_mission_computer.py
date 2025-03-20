import random


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

    def get_env(self):
        log_message = (
            f"화성 기지 내부 온도: {self.env_values['mars_base_internal_temperature']:.2f}도, "
            f"화성 기지 외부 온도: {self.env_values['mars_base_external_temperature']:.2f}도, "
            f"화성 기지 내부 습도: {self.env_values['mars_base_internal_humidity']:.2f}%, "
            f"화성 기지 외부 광량: {self.env_values['mars_base_external_illuminance']:.2f} W/m2, "
            f"화성 기지 내부 이산화탄소 농도: {self.env_values['mars_base_internal_co2']:.2f}%, "
            f"화성 기지 내부 산소 농도: {self.env_values['mars_base_internal_oxygen']:.2f}%"
        )


    def get_env(self):
        # 시간 대신 "테스트 실행 시간" 텍스트 사용
        log_message = (
            f"테스트 실행 시간, "
            f"화성 기지 내부 온도: {self.env_values['mars_base_internal_temperature']:.2f}도, "
            f"화성 기지 외부 온도: {self.env_values['mars_base_external_temperature']:.2f}도, "
            f"화성 기지 내부 습도: {self.env_values['mars_base_internal_humidity']:.2f}%, "
            f"화성 기지 외부 광량: {self.env_values['mars_base_external_illuminance']:.2f} W/m2, "
            f"화성 기지 내부 이산화탄소 농도: {self.env_values['mars_base_internal_co2']:.2f}%, "
            f"화성 기지 내부 산소 농도: {self.env_values['mars_base_internal_oxygen']:.2f}%"
        )

        # 파일에 로그 작성 (추가 모드 사용)
        with open('mars_mission_log.txt', 'a', encoding='utf-8') as log_file:
            log_file.write(log_message + '\n')

        # 터미널에도 출력
        print(log_message)

        return self.env_values

# 인스턴스 생성
ds = DummySensor()

# set_env() 호출 → 랜덤 값 설정
ds.set_env()

# get_env() 호출 → 값 출력
env_data = ds.get_env()

# 출력 확인
for key, value in env_data.items():
    print(f"{key}: {value:.2f}")
