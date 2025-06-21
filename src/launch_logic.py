import minecraft_launcher_lib
import subprocess
import threading
from random import choice

# Константы
MINECRAFT_DIRECTORY = '/Users/stepanlukoyanov/seronez/chimera_laucnher/.minecraft'
UUID = '1'


class Launcher:
    def __init__(self):
        # Получаем список версий при инициализации
        version_list = minecraft_launcher_lib.utils.get_version_list()
        self.version_ids = [version['id'] for version in version_list]

    def launch_minecraft(self, version_id, username):
        """Запускает Minecraft с указанными параметрами"""
        # Убедимся, что версия установлена
        minecraft_launcher_lib.install.install_minecraft_version(
            versionid=version_id,
            minecraft_directory=MINECRAFT_DIRECTORY
        )

        # Настройки для запуска
        options = {
            'username': username,
            'uuid': UUID,
            'token': '',
        }

        # Запускаем Minecraft в отдельном потоке
        minecraft_thread = threading.Thread(
            target=self._run_minecraft,
            args=(version_id, options))
        minecraft_thread.start()

    def _run_minecraft(self, version_id, options):
        """Внутренний метод для запуска Minecraft"""
        command = minecraft_launcher_lib.command.get_minecraft_command(
            version=version_id,
            minecraft_directory=MINECRAFT_DIRECTORY,
            options=options
        )
        subprocess.call(command)