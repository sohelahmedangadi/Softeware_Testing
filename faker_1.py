from faker import Faker

fake_data = Faker()

for _ in range(5):
    print(fake_data.name())

for _ in range(5):
    print(fake_data.email())