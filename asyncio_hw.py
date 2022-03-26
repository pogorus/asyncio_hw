import asyncio

from database import db, PG_DSN, Person
import sw_api


async def main():
    await db.set_bind(PG_DSN)
    await db.gino.create_all()
    async for person in sw_api.get_persons(range(1, 11)):
        person_data = {'id': person.get('id'),
                       'birth_year': person.get('birth_year'),
                       'eye_color': person.get('eye_color'),
                       'films': await sw_api.get_objects_names(person, 'films'),
                       'gender': person.get('gender'),
                       'hair_color': person.get('hair_color'),
                       'height': person.get('height'),
                       'homeworld': await sw_api.get_object_name(person.get('homeworld')),
                       'mass': person.get('mass'),
                       'name': person.get('name'),
                       'skin_color': person.get('skin_color'),
                       'species': await sw_api.get_objects_names(person, 'species'),
                       'starships': await sw_api.get_objects_names(person, 'starships'),
                       'vehicles': await sw_api.get_objects_names(person, 'vehicles'),
                       }
        await Person.create(**person_data)

    print(await Person.get(1).to_dict())
    print(await Person.get(7).to_dict())
    await db.pop_bind().close()


asyncio.run(main())
