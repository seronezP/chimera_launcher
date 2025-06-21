import customtkinter
from customtkinter import CTkFrame


class App:
    def __init__(self, launch_callback):
        self.app = customtkinter.CTk()
        self.app.title("Chimera Launcher")
        self.app.geometry("600x340")

        frame_1 = CTkFrame(master=self.app, width=500, height=300)
        frame_1.place(x=130, y=50)

        self.entry_1 = customtkinter.CTkEntry(
            self.app,
            placeholder_text="Enter Your Name",
            width=120,
            height=30
        )
        self.entry_1.place(x=300, y=220)

        self.combobox_var = customtkinter.StringVar(value="Select Version")
        self.combobox = customtkinter.CTkComboBox(
            self.app,
            width=120,
            height=30,
            variable=self.combobox_var
        )
        self.combobox.place(x=300, y=260)

        button_1 = customtkinter.CTkButton(
            self.app,
            text="Launch",
            fg_color="#1a1a1a",
            width=120,
            height=30,
            command=launch_callback
        )
        button_1.place(x=300, y=300)

    def set_version_options(self, versions):
        """Устанавливает варианты версий в комбобокс"""
        self.combobox.configure(values=versions)

    def get_selected_version(self):
        """Возвращает выбранную версию"""
        return self.combobox_var.get()

    def get_username(self):
        """Возвращает введенное имя пользователя"""
        return self.entry_1.get().strip()

    def run(self):
        """Запускает главный цикл приложения"""
        self.app.mainloop()