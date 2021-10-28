from datetime import datetime
import win10toast


def get_name():
    print("введите Имя и Фамилия именинника, дату дня рождения")
    name = str(input())
    return name


def get_date():
    print("введите дату, когда вам напомнить про день рождения в формате dd/mm/YY H:M:S")
    date_reminder = str(input())
    return date_reminder


def date_timer():
    name = get_name()
    date_reminder = get_date()
    while True:
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        if dt_string == date_reminder:
            toaster = win10toast.ToastNotifier()
            toaster.show_toast("Скоро день рождения ", name, )
            break


date_timer()
