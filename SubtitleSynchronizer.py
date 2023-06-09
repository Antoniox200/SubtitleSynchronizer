import os
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QDragEnterEvent, QDropEvent, QDrag

class FFSubSyncGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Subtitle Synchronizer")
        self.resize(800, 600)  # Set the default size of the window to 800x600

        self.layout = QVBoxLayout()

        self.label_video = QLabel('Drag and Drop Video File Here')
        self.label_video.setAcceptDrops(True)
        self.label_video.setFrameStyle(QLabel.Panel | QLabel.Sunken)
        self.label_video.setAlignment(Qt.AlignCenter)
        self.label_video.dragEnterEvent = self.dragEnterEvent
        self.label_video.dropEvent = self.dropEvent_video

        self.layout.addWidget(self.label_video)

        self.label_unsync_sub = QLabel('Drag and Drop Unsync Subtitle File Here')
        self.label_unsync_sub.setAcceptDrops(True)
        self.label_unsync_sub.setFrameStyle(QLabel.Panel | QLabel.Sunken)
        self.label_unsync_sub.setAlignment(Qt.AlignCenter)
        self.label_unsync_sub.dragEnterEvent = self.dragEnterEvent
        self.label_unsync_sub.dropEvent = self.dropEvent_unsync_sub

        self.layout.addWidget(self.label_unsync_sub)

        self.sync_button = QPushButton('Sync')
        self.sync_button.clicked.connect(self.sync_subtitles)

        self.layout.addWidget(self.sync_button)

        self.setLayout(self.layout)

        self.video_file = None
        self.unsync_sub = None

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            super().dragEnterEvent(event)

    def dropEvent_video(self, event: QDropEvent):
        if event.mimeData().hasUrls():
            url: QUrl = event.mimeData().urls()[0]
            self.video_file = url.toLocalFile()
            self.label_video.setText(self.video_file)

    def dropEvent_unsync_sub(self, event: QDropEvent):
        if event.mimeData().hasUrls():
            url: QUrl = event.mimeData().urls()[0]
            self.unsync_sub = url.toLocalFile()
            self.label_unsync_sub.setText(self.unsync_sub)

    def sync_subtitles(self):
        if self.video_file and self.unsync_sub:
            output_dir = os.path.dirname(self.unsync_sub)
            base_name = os.path.basename(self.unsync_sub)
            output_sub = os.path.join(output_dir, f'synchronized{base_name}')  # Append "synchronized" to the original filename

            try:
                subprocess.call(["ffsubsync", self.video_file, "-i", self.unsync_sub, "-o", output_sub])
                print(f'Synchronized subtitle file has been saved to {output_sub}')
            except Exception as e:
                print(f'Error: {str(e)}')
        else:
            print('Please provide valid Video file and Unsync Subtitle file.')


app = QApplication([])
window = FFSubSyncGUI()
window.show()
app.exec_()
