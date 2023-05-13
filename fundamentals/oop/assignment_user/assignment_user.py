class User:

    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_reward_member = False
        self.gold_card_points = 0

    def display_info(self):
        print('----------------------------------')
        print(f'First Name: {self.first_name}')
        print(f'Last Name: {self.last_name}')
        print(f'Email: {self.email}')
        print(f'Age: {self.age}')
        print(f'Member: {self.is_reward_member}')
        print(f'Reward: {self.gold_card_points}')

    def enroll(self):
        if self.is_reward_member:
            print('User already a member')
            return False
        else:
            self.is_reward_member = True
            self.gold_card_points = 200
            return True

    def spend_points(self, amount):
        if amount > self.gold_card_points:
            print('Not enough gold card points')
        else:
            self.gold_card_points -= amount

person = User('Brian', 'Smith', 'test@gmail.com', 21)
person.display_info()
person.enroll()
person.display_info()
person.spend_points(200)
person.display_info()
person.enroll()
person.spend_points(250)