import subprocess
import os
import time

def check_drivers_update():
    try:
        print("Проверка обновлений драйверов...")
        command = "control.exe update"
        subprocess.run(command, shell=True)
        print("Процесс проверки обновлений драйверов запущен.")
    except Exception as e:
        print(f"Ошибка при запуске проверки обновлений драйверов: {e}")

def check_system_file_integrity():
    try:
        print("Проверка целостности системных файлов...")
        result = subprocess.run(["sfc", "/scannow"], capture_output=True, text=True)
        
        # Обработка результатов
        if result.returncode == 0:
            print("Проверка завершена успешно: ошибок не обнаружено.")
        else:
            print("При проверке были обнаружены ошибки:")
            for line in result.stdout.splitlines():
                if "ошибок" in line or "не удаётся" in line:
                    print(line)
        
        # Альтернативный вывод из журнала CBS
        cbs_log_path = r"C:\Windows\Logs\CBS\CBS.log"
        print("Результаты также могут быть найдены в журнале CBS по адресу:", cbs_log_path)

    except Exception as e:
        print(f"Ошибка при запуске проверки целостности файлов: {e}")

def set_power_scheme_high_performance():
    try:
        print("Настройка схемы электропитания на режим высокой производительности...")
        subprocess.run("powercfg /setactive SCHEME_MIN", shell=True)
        print("Схема электропитания изменена на высокий производительность.")
    except Exception as e:
        print(f"Ошибка при изменении схемы электропитания: {e}")

def open_task_manager():
    try:
        print("Открытие Диспетчера задач...")
        subprocess.Popen("taskmgr", shell=True)
        time.sleep(2)  # Задержка в 2 секунды
    except Exception as e:
        print(f"Ошибка при открытии Диспетчера задач: {e}")

def open_system_properties():
    try:
        print("Открытие свойств Компьютера...")
        subprocess.Popen("sysdm.cpl", shell=True)
        time.sleep(2)  # Задержка в 2 секунды
    except Exception as e:
        print(f"Ошибка при открытии свойств Компьютера: {e}")

def open_device_manager():
    try:
        print("Открытие Диспетчера устройств...")
        subprocess.Popen("devmgmt.msc", shell=True)
        time.sleep(2)  # Задержка в 2 секунды
    except Exception as e:
        print(f"Ошибка при открытии Диспетчера устройств: {e}")

if __name__ == "__main__":
    set_power_scheme_high_performance()
    check_drivers_update()
    check_system_file_integrity()
    # Открываем различные элементы с задержкой
    open_task_manager()
    open_system_properties()
    open_device_manager()
    os.system("pause")








