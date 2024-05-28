from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.list import MDList, OneLineListItem
import pyrebase

firebaseConfig = {
    'apiKey': "AIzaSyA3gOHi9Q6aHQ5seN5S9bbNmQpPQFMGXFs",
    'authDomain': "magnus-c4b38.firebaseapp.com",
    'databaseURL': "https://magnus-c4b38-default-rtdb.firebaseio.com",
    'projectId': "magnus-c4b38",
    'storageBucket': "magnus-c4b38.appspot.com",
    'messagingSenderId': "458576341456",
    'appId': "1:458576341456:web:6117f4a9160b8667b8f1d5"
}

class MainApp(MDApp):
    def build(self):
        self.title = "Publicações App"
        
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.input_field = MDTextField(
            hint_text="Escreva sua publicação...",
            multiline=False
        )
        self.layout.add_widget(self.input_field)
        
        self.submit_button = MDRaisedButton(
            text="Publicar",
            on_release=self.save_post
        )
        self.layout.add_widget(self.submit_button)
        
        self.posts_list = MDList()
        self.layout.add_widget(self.posts_list)
        
        self.firebase = pyrebase.initialize_app(firebaseConfig)
        self.db = self.firebase.database()
        self.load_posts()
        
        return self.layout
    
    def save_post(self, instance):
        post_text = self.input_field.text
        if post_text:
            self.add_post_to_list(post_text)
            self.save_post_to_db(post_text)
            self.input_field.text = ""
    
    def add_post_to_list(self, post_text):
        self.posts_list.add_widget(OneLineListItem(text=post_text))
    
    def save_post_to_db(self, post_text):
        self.db.child("posts").push({"text": post_text})
    
    def load_posts(self):
        posts = self.db.child("posts").get()
        if posts.val():  # Verifica se há dados válidos
            for post in posts.each():
                self.add_post_to_list(post.val()["text"])

if __name__ == "__main__":
    MainApp().run()
