import random
from faker import Faker
from tasks.models import Category, Event, Participant

fake = Faker()

# Create fake categories
def create_categories(n=5):
    categories = []
    for _ in range(n):
        category = Category.objects.create(
            name=fake.word().capitalize(),
            description=fake.text()
        )
        categories.append(category)
    return categories

# Create fake events
def create_events(categories, n=10):
    events = []
    for _ in range(n):
        event = Event.objects.create(
            name=fake.catch_phrase(),
            description=fake.text(),
            date=fake.date_between(start_date='-30d', end_date='+30d'),
            location=fake.city(),
            status=random.choice(['PENDING', 'IN_PROGRESS', 'COMPLETED']),
            category=random.choice(categories),
        )
        events.append(event)
    return events

# Create fake participants
def create_participants(events, n=20):
    for _ in range(n):
        participant = Participant.objects.create(
            name=fake.name(),
            email=fake.unique.email(),
        )
        # Assign random events to the participant
        participant.event.add(*random.sample(events, random.randint(1, 3)))

def populate_database():
    print("Populating database with fake data...")
    categories = create_categories()
    events = create_events(categories)
    create_participants(events)
    print("Database populated successfully.")

if __name__ == '__main__':
    populate_database()
