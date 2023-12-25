import subprocess
from PyQt6.QtWidgets import QApplication, QMainWindow, QPlainTextEdit, QVBoxLayout, QWidget, QPushButton

class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.text_area = QPlainTextEdit()
        layout = QVBoxLayout()
        layout.addWidget(self.text_area)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        run_button = QPushButton("Run Konid")
        run_button.clicked.connect(self.run_code)
        layout.addWidget(run_button)

    def run_code(self):
        code = self.text_area.toPlainText()
        process = subprocess.Popen(["python", "-c", code], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
      
        print("Khorooji:", output.decode())
        print("Error:", error.decode())

if __name__ == "__main__":
    app = QApplication([])
    editor = TextEditor()
    editor.show()
    app.exec()