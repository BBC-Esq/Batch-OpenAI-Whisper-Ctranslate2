import os
import glob
import subprocess
from PySide6.QtWidgets import QApplication, QMainWindow, QCheckBox, QGridLayout, QPushButton, QFileDialog, QWidget, QLabel, QComboBox

# Define model and output options as constants
MODEL_OPTIONS = ["", "--model large-v2", "--model large-v1", "--model medium.en", "--model medium", 
                 "--model base.en", "--model base", "--model small.en", "--model small", 
                 "--model tiny.en", "--model tiny"]
OUTPUT_OPTIONS = ["", "--output_format txt", "--output_format vtt", "--output_format srt"]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.model_combo = QComboBox()
        self.model_combo.addItems(MODEL_OPTIONS)
        self.model_combo.setCurrentIndex(0)

        self.format_combo = QComboBox()
        self.format_combo.addItems(OUTPUT_OPTIONS)
        self.format_combo.setCurrentIndex(0)

        self.process_subdirs_checkbox = QCheckBox("Include subdirectories")
        self.choose_directory_button = QPushButton("Choose Directory")
        self.choose_directory_button.clicked.connect(self.choose_directory)
        self.process_button = QPushButton("Process Files")
        self.process_button.clicked.connect(self.process_files)
        self.status_label = QLabel("")

        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Batch Processing GUI")
        layout = QGridLayout()

        # Adding widgets to the layout
        layout.addWidget(QLabel("Choose Model"), 0, 0)
        layout.addWidget(self.model_combo, 1, 0)

        layout.addWidget(QLabel("Output Format"), 0, 1)
        layout.addWidget(self.format_combo, 1, 1)

        layout.addWidget(self.process_subdirs_checkbox, 2, 0, 1, 2)
        layout.addWidget(self.choose_directory_button, 3, 0)
        layout.addWidget(self.process_button, 3, 1)
        layout.addWidget(self.status_label, 4, 0, 1, 2)

        self.setCentralWidget(QWidget())
        self.centralWidget().setLayout(layout)

    def choose_directory(self):
        self.directory_path = QFileDialog.getExistingDirectory(self, "Choose Directory")

    def process_files(self):
        if not hasattr(self, 'directory_path'):
            self.status_label.setText("No directory chosen.")
            return

        model = self.model_combo.currentText()
        output_format = self.format_combo.currentText()

        file_extensions = ["*.wav", "*.mp3", "*.wma"]
        search_path = self.directory_path
        if self.process_subdirs_checkbox.isChecked():
            search_path = os.path.join(self.directory_path, "**")

        file_paths = []
        for extension in file_extensions:
            file_paths.extend(glob.glob(os.path.join(search_path, extension), recursive=True))

        total_files = len(file_paths)
        processed_files = 0
        for file_path in file_paths:
            command = f"whisperx \"{file_path}\" {model} {output_format}"
            subprocess.call(command, shell=True)
            processed_files += 1
            self.status_label.setText(f"Processed {processed_files} out of {total_files} files.")

if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec()
