import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.QtCore import QObject, pyqtSignal
from GUI import Ui_MainWindow  # Import your generated GUI code here

# Create a class to handle SD card operations
class SDCardManager(QObject):
    folder_read_signal = pyqtSignal(list)

    def __init__(self):
        super().__init__()

    def read_folders(self, sd_card_path):
        # Simulate reading folders from the SD card by listing the contents of the specified folder
        # You would replace this with actual code to read folders from the SD card
        import os
        if os.path.exists(sd_card_path) and os.path.isdir(sd_card_path):
            folders = [f for f in os.listdir(sd_card_path) if os.path.isdir(os.path.join(sd_card_path, f))]
            self.folder_read_signal.emit(folders)

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Connect GUI signals to methods
        self.pushButton.clicked.connect(self.read_sd_card_folders)
        self.tableWidget.itemClicked.connect(self.access_folder)

        # Create an instance of the SDCardManager
        self.sd_card_manager = SDCardManager()
        self.sd_card_manager.folder_read_signal.connect(self.display_folders)

    def read_sd_card_folders(self):
        # Specify the root directory of the SD card
        sd_card_path = "d:"  # Replace with the actual path to your SD card
        self.sd_card_manager.read_folders(sd_card_path)

    def display_folders(self, folders):
        # Display the folders in the table widget
        self.tableWidget.setRowCount(len(folders))
        for i, folder in enumerate(folders):
            item = QTableWidgetItem(folder)  # Create a QTableWidgetItem
            self.tableWidget.setItem(i, 0, item)

    def access_folder(self, item):
        # Get the folder name from the clicked item
        folder_name = item.text()
        # Perform actions to access the folder (e.g., open it)
        print(f"Accessing folder: {folder_name}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())
