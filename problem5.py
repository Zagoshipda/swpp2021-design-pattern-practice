import time


class Counselor:
    def __init__(self):
        self.busy = False

    def talk(self):
        print("I am ready to talk")


class PhoneCall:
    def __init__(self, current_time='weekdays'):
        self.counselors = [Counselor(), Counselor()]
        self.current_time = current_time

    def talk(self):
        if self.current_time == 'weekdays':
            # TODO: fill this function
            # If you want, you can add time.sleep(0.1) before you call talk() in Counselor
            # to simulate the waiting time.
            if not self.counselors[0].busy:
                self.counselors[0].busy = True
                self.counselors[0].talk()
            elif not self.counselors[1].busy:
                self.counselors[1].busy = True
                self.counselors[1].talk()
            else:
                print("No available counselor")

        else:
            time.sleep(0.1)
            print('Counselor will not talk to you')


if __name__ == "__main__":
    p = PhoneCall('weekdays')
    p.talk()
    p.talk()
    p.talk()

    p = PhoneCall('weekend')
    p.talk()

    """
    Expected Output

    > I am ready to talk
    > I am ready to talk
    > No available counselor
    > Counselor will not talk to you

    """
