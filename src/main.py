from app_gui import App
from launch_logic import Launcher
from random import choice


def main():
    # Создаем экземпляры классов
    launcher = Launcher()

    def launch_callback():
        username = app.get_username()
        version_id = app.get_selected_version()

        if not username:
            print("Please enter your name")
            return

        if version_id == "Select Version":
            # Автоматический выбор версии, если не выбрана
            version_id = choice(launcher.version_ids)
            print(f"Auto-selected version: {version_id}")

        launcher.launch_minecraft(version_id, username)

    app = App(launch_callback)

    app.set_version_options(launcher.version_ids)
    # Запускаем GUI
    app.run()


if __name__ == "__main__":
    main()