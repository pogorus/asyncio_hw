import aiohttp
import asyncio
import more_itertools


BASE_URL = 'https://swapi.dev/api'


async def get_person(person_id):
    session = aiohttp.ClientSession()
    response = await session.get(f'{BASE_URL}/people/{person_id}')
    response_json = await response.json()
    await session.close()
    return response_json


async def get_persons(person_ids):
    for person_ids_chunk in more_itertools.chunked(person_ids, 10):
        for person_id in person_ids_chunk:
            person = await asyncio.create_task(get_person(person_id))
            if person != {'detail': 'Not found'}:
                person['id'] = person_id
                yield person


async def get_object_name(url):
    session = aiohttp.ClientSession()
    response = await session.get(url)
    response_json = await response.json()
    await session.close()
    if response_json.get('name'):
        return response_json.get('name')
    elif response_json.get('title'):
        return response_json.get('title')


async def get_objects_names(person, attr):
    tasks = [asyncio.create_task(get_object_name(url)) for url in person.get(attr)]
    names = await asyncio.gather(*tasks)
    names_str = ', '.join(names)
    return names_str
