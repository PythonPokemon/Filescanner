from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup

class FileAnalyzerApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        file_chooser = FileChooserIconView()
        file_chooser.bind(on_submit=self.analyze_file)
        layout.add_widget(file_chooser)

        self.info_label = Label(text="Dateiinformationen werden hier angezeigt")
        layout.add_widget(self.info_label)

        return layout

    def analyze_file(self, instance, value, *args):
        file_path = value

        file_info = self.get_file_info(file_path)

        popup_layout = BoxLayout(orientation='vertical')
        popup_layout.add_widget(Label(text=file_info))

        popup = Popup(title="Dateiinformationen", content=popup_layout, size_hint=(None, None), size=(300, 200))
        popup.open()

    def get_file_info(self, file_path):
        # Hier könntest du den Code einfügen, der das Dateiformat und den Datentyp der ausgewählten Datei ermittelt.
        # Beispielhaft wird hier die Dateiendung als Dateityp verwendet.
        file_type = file_path.split('.')[-1] if '.' in file_path else 'Unbekannt'

        return f"Dateipfad: {file_path}\nDateityp: {file_type}"

if __name__ == '__main__':
    FileAnalyzerApp().run()
