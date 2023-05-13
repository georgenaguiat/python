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
        return self

    def enroll(self):
        if self.is_reward_member:
            print('User already a member')
            return self

        self.is_reward_member = True
        self.gold_card_points = 200
        return self

    def spend_points(self, amount):
        if amount > self.gold_card_points:
            print('Not enough gold card points')
            return self
        
        self.gold_card_points -= amount
        return self


person = User('Brian', 'Smith', 'brianemail@gmail.com', 21)
person1 = User('Casper', 'Ghost', 'casperemail@yahoo.con', 200)
# person.enroll()
# person.enroll()
# person1.enroll()
# person.spend_points(50)
# person1.spend_points(80)
# person.display_info()
# person1.display_info()
person.display_info().enroll().spend_points(50).display_info()
person1.enroll().spend_points(80).display_info()
