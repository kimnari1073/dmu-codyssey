import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton,
    QVBoxLayout, QGridLayout, QLineEdit
)
from PyQt5.QtCore import Qt


class IPhoneCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('iPhone Style Calculator')
        self.setFixedSize(360, 540)
        self.init_ui()

    def init_ui(self):
        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.display.setStyleSheet("""
            font-size: 36px;
            padding: 15px;
            border: none;
            background-color: #000;
            color: #fff;
        """)
        self.display.setFixedHeight(80)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.display)

        buttons = [
            ['AC', '+/-', '%', '÷'],
            ['7', '8', '9', '×'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '=']
        ]

        grid = QGridLayout()
        grid.setSpacing(10)

        for row, row_values in enumerate(buttons):
            col_offset = 0
            for col, text in enumerate(row_values):
                button = QPushButton(text)
                button.setFixedHeight(70)

                if text in ['÷', '×', '-', '+', '=']:
                    color = '#f57c00'  # 오렌지색 (연산자)
                    text_color = 'white'
                elif text in ['AC', '+/-', '%']:
                    color = '#a5a5a5'  # 회색 (기능키)
                    text_color = 'black'
                else:
                    color = '#333333'  # 숫자키
                    text_color = 'white'

                button.setStyleSheet(f"""
                    background-color: {color};
                    color: {text_color};
                    font-size: 24px;
                    border-radius: 35px;
                """)

                # 0 버튼은 두 칸 차지
                if text == '0':
                    button.setFixedWidth(150)
                    grid.addWidget(button, row, col, 1, 2)
                    col_offset = 1  # 다음 버튼 오른쪽으로 한 칸 밀기
                else:
                    button.setFixedWidth(70)
                    grid.addWidget(button, row, col + col_offset)

                button.clicked.connect(self.on_button_click)

        main_layout.addLayout(grid)
        self.setLayout(main_layout)

    def on_button_click(self):
        sender = self.sender()
        self.display.setText(self.display.text() + sender.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = IPhoneCalculator()
    calc.show()
    sys.exit(app.exec_())
