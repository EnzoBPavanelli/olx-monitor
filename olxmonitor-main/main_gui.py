import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QTextEdit, QLabel
from PyQt5.QtCore import QThread, pyqtSignal
from main import rodar_monitoramento  # você vai mover a função principal para `main.py`

class MonitorThread(QThread):
    update = pyqtSignal(str)

    def run(self):
        self.running = True
        self.update.emit("🟢 Monitoramento iniciado...\n")
        while self.running:
            self.update.emit("🔁 Executando verificação OLX...\n")
            rodar_monitoramento(self.update)  # passa função de log
            for i in range(60):  # aguarda 60 segundos no total (ajustável)
                if not self.running:
                    break
                time.sleep(1)

    def stop(self):
        self.running = False
        self.quit()
        self.wait()

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('OLX Monitor')
        self.resize(400, 300)

        self.status_label = QLabel("Status:")
        self.text_area = QTextEdit()
        self.text_area.setReadOnly(True)

        self.start_button = QPushButton("Iniciar")
        self.stop_button = QPushButton("Parar")
        self.stop_button.setEnabled(False)

        self.start_button.clicked.connect(self.start_monitoring)
        self.stop_button.clicked.connect(self.stop_monitoring)

        layout = QVBoxLayout()
        layout.addWidget(self.status_label)
        layout.addWidget(self.text_area)
        layout.addWidget(self.start_button)
        layout.addWidget(self.stop_button)
        self.setLayout(layout)

        self.thread = MonitorThread()
        self.thread.update.connect(self.log)

    def start_monitoring(self):
        self.thread.start()
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)

    def stop_monitoring(self):
        self.thread.stop()
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)
        self.log("⛔ Monitoramento parado.\n")

    def log(self, text):
        self.text_area.append(text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())
