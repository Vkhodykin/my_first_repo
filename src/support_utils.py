from typing import Callable, Any, Generator



def create_id_generator(id_gen=0) -> Generator[int, Any, Any]:
    """
    Генератор последовательных ID
    """

    last_id = id_gen

    while True:
        last_id += 1
        yield last_id