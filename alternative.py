from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.uix.image import Image

class FileAnalyzerApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        file_chooser = FileChooserListView()
        file_chooser.bind(on_submit=self.analyze_file)
        layout.add_widget(file_chooser)

        self.info_label = Label(text="Dateiinformationen werden hier angezeigt")
        layout.add_widget(self.info_label)

        return layout

    def analyze_file(self, instance, value):
        file_path = value[0]

        file_info = self.get_file_info(file_path)

        popup_layout = BoxLayout(orientation='vertical')
        popup_layout.add_widget(Image(source=file_path))
        popup_layout.add_widget(Label(text=file_info))

        popup = Popup(title="Dateiinformationen", content=popup_layout, size_hint=(None, None), size=(400, 400))
        popup.open()

    def get_file_info(self, file_path):
        # Hier könntest du den Code einfügen, der das Dateiformat und den Datentyp der ausgewählten Datei ermittelt.
        # Zum Beispiel könntest du die Bibliothek `python-magic` verwenden, um den Dateityp zu bestimmen.
        # Bitte installiere zuerst die Bibliothek mit `pip install python-magic`.
        import magic
        mime = magic.Magic(mime=True)
        file_type = mime.from_file(file_path)

        return f"Dateipfad: {file_path}\nDateityp: {file_type}"

if __name__ == '__main__':
    FileAnalyzerApp().run()
