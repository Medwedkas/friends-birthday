import time


class Birthday:
    def get_person(self):
        print("Что вам напомнить?")
        text = str(input())
        return text

    def get_date(self):
        print("Через какое время вам напомнить?")
        local_time = float(input())
        local_time = local_time * 60
        time.sleep(local_time)
        return local_time

    def osnov(self):
        print("Через какое время вам напомнить?")
        text = str(input())
        local_time = float(input())
        local_time = local_time * 60
        time.sleep(local_time)


obj = Birthday()
