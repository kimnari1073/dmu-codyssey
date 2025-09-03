# pip install sounddevice scipy

import os
import datetime
import sounddevice as sd
from scipy.io.wavfile import write


class Recorder:
    def __init__(self, folder='records', samplerate=44100, duration=5):
        self.folder = folder
        self.samplerate = samplerate
        self.duration = duration
        self.ensure_folder_exists()

    def ensure_folder_exists(self):
        if not os.path.exists(self.folder):
            os.makedirs(self.folder)

    def record_audio(self):
        print('녹음을 시작합니다...')
        try:
            audio_data = sd.rec(int(self.duration * self.samplerate), samplerate=self.samplerate, channels=1, dtype='int16')
            sd.wait()
            filename = self.get_timestamp_filename()
            filepath = os.path.join(self.folder, filename)
            write(filepath, self.samplerate, audio_data)
            print(f'녹음이 완료되었습니다: {filepath}')
        except Exception as e:
            print(f'녹음 중 오류 발생: {e}')

    def get_timestamp_filename(self):
        now = datetime.datetime.now()
        return now.strftime('%Y%m%d-%H%M%S') + '.wav'

    def list_files_by_date_range(self, start_date, end_date):
        print(f'{start_date} ~ {end_date} 사이의 파일을 찾습니다.')
        try:
            file_list = os.listdir(self.folder)
            for filename in sorted(file_list):
                if filename.endswith('.wav'):
                    date_part = filename.split('.')[0]
                    try:
                        file_date = datetime.datetime.strptime(date_part, '%Y%m%d-%H%M%S').date()
                        if start_date <= file_date <= end_date:
                            print(filename)
                    except ValueError:
                        continue
        except Exception as e:
            print(f'파일 목록 조회 중 오류: {e}')


def main():
    recorder = Recorder()

    # 녹음 실행
    recorder.record_audio()

    # 보너스 과제 예시: 2025년 5월 20일 ~ 2025년 5월 22일 사이 파일 보기
    try:
        start = datetime.date(2025, 5, 20)
        end = datetime.date(2025, 5, 22)
        recorder.list_files_by_date_range(start, end)
    except Exception as e:
        print(f'날짜 범위 처리 중 오류: {e}')


if __name__ == '__main__':
    main()
