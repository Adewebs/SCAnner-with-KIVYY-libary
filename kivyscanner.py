import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.lang import Builder
from pyzbar.pyzbar import decode
import cv2

kivy.require("1.11.1")

Builder.load_string('''
<CameraApp>:
    orientation: 'vertical'
    Camera:
        id: camera
        resolution: (640, 480)
        play: True
    Button:
        text: 'Capture QR Code'
        on_press: root.capture()
    Label:
        id: result_label
        text: 'QR Code Result: '
''')

class CameraApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.camera = Camera(resolution=(640, 480), play=True)
        self.capture_button = Button(text='Click Capture QR Code', on_press=self.capture)
        self.result_label = Label(text='QR Code Result: ')
        self.layout.add_widget(self.camera)
        self.layout.add_widget(self.capture_button)
        self.layout.add_widget(self.result_label)

        return self.layout

    def capture(self, *args):
        # Capture the image
        image_path = "captured_image.jpg"
        self.camera.export_to_png(image_path)

        # Decode the QR code
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        qr_codes = decode(image)

        # Display the result
        if qr_codes:
            qr_data = qr_codes[0].data.decode('utf-8')
            self.result_label.text = f'QR Code Result: {qr_data}'
            print  (qr_data)
        else:
            self.result_label.text = 'No QR Code found'

if __name__ == '__main__':
    CameraApp().run()
