from datetime import datetime, timedelta

from db_init import global_init, create_session
from db_class import User, Jobs

db_name = "database.db"
session_factory = global_init(db_name)
session = create_session(session_factory)

def add_users():
    colonists = [
        User(
            surname="Watney",
            name="Mark",
            age=35,
            position="engineer",
            speciality="mechanic",
            address="module_2",
            email="watney_mark@mars.org",
            hashed_password="mechanic"
        ),
        User(
            surname="Lewis",
            name="Melissa",
            age=40,
            position="commander",
            speciality="biologist",
            address="module_3",
            email="lewis_melissa@mars.org",
            hashed_password="biologist"
        ),
        User(
            surname="Martinez",
            name="Rick",
            age=30,
            position="pilot",
            speciality="navigator",
            address="module_1",
            email="martinez_rick@mars.org",
            hashed_password="navigator"
        )
    ]

    for colonist in colonists:
        session.add(colonist)

    session.commit()

def add_job():
    jobs = [
        Jobs(
            team_leader=1,
            job="Deployment of residential modules 1 and 2",
            work_size=15,
            collaborators="2, 3",
            start_date=datetime.now(),
            is_finished=False
        ),
        Jobs(
            team_leader=2,
            job="Exploration of mineral resources",
            work_size=25,
            collaborators="4, 5",
            start_date=datetime.now() - timedelta(days=2),
            is_finished=True
        ),
        Jobs(
            team_leader=3,
            job="Analysis of atmospheric air samples",
            work_size=10,
            collaborators="6",
            start_date=datetime.now() - timedelta(days=5),
            is_finished=False
        ),
        Jobs(
            team_leader=1,
            job="Repair of equipment in module 3",
            work_size=8,
            collaborators="2",
            start_date=datetime.now() - timedelta(days=1),
            is_finished=True
        )
    ]

    for job in jobs:
        session.add(job)

    session.commit()


if __name__ == "__main__":
    add_users()
    add_job()