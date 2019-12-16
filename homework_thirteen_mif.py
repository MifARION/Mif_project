import asyncio
import numpy as np


async def sum_elements():
    with open('in_<1>.dat', 'r') as my_file:
        await asyncio.sleep(1)
        lines = my_file.readlines()
        first_line = int(lines[0])
        second_line = lines[-1].split()
        list_number = [float(num) for num in second_line]
        if first_line == 1:
            result_one = sum(list_number)
            print(f'{result_one} sum_elements complete!')
            await asyncio.sleep(1)
            return result_one


async def multiplication():
    with open('in_<2>.dat', 'r') as my_file:
        await asyncio.sleep(1)
        lines = my_file.readlines()
        first_line = int(lines[0])
        second_line = lines[-1].split()
        list_number = [float(num) for num in second_line]
        if first_line == 2:
            result_two = np.prod(list_number)
            print(f'{result_two} multi complete!')
            await asyncio.sleep(1)
            return result_two


async def sum_of_squares():
    with open('in_<3>.dat', 'r') as my_file:
        lines = my_file.readlines()
        first_line = int(lines[0])
        second_line = lines[-1].split()
        list_number = [float(num) for num in second_line]
        if first_line == 3:
            await asyncio.sleep(1)
            result_three = sum(np.array(list_number) ** 2)
            print(f'{result_three} sum_squares complete!')
            return result_three


async def sum_all():
    result = await multiplication() + await sum_of_squares() + await sum_elements()
    with open('out.dat', 'w') as file_out:
        file_out.write(str(result))
        print('save complete!')
        # await asyncio.sleep(1)


async def main():
    task3 = asyncio.create_task(sum_of_squares())
    task1 = asyncio.create_task(sum_elements())        # начиная с версии 3.6 asyncio.ensure_future и create_task одно
    task2 = asyncio.create_task(multiplication())                                                             # и тоже
    task4 = asyncio.create_task(sum_all())
    await asyncio.gather(task1, task2, task3, task4)


if __name__ == '__main__':

    # loop = asyncio.get_event_loop()        начиная с версии пайтона 3.6 эту всю конструкцию можно заменить на run
    # loop.run_until_complete(main())

    asyncio.run(main())