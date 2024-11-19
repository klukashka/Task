from bs4 import BeautifulSoup
import httpx
import logging
import os
import random
import pandas as pd
import time
from task_2.exception_handler import handle_errors
from task_2 import settings


logger = logging.getLogger("streamLogger")


@handle_errors(logger=logger)
def gather_names(session: httpx.Client, url: str) -> list[str]:
    """Get all animal names from the given url and its children"""
    next_url = url
    all_names = []

    while True:
        r = session.get(next_url, headers=settings.headers)
        time.sleep(random.randrange(2, 5))

        if r.status_code != 200:
            raise ConnectionError("Failed to load the source page")

        soup = BeautifulSoup(r.text, "lxml")

        try:
            next_url = settings.domain + soup.find("a", string="Следующая страница")["href"]
        except Exception as e:
            raise Exception(f"Failed to load the next url with exception: {e}") from e

        blocks = soup.find_all("div", class_="mw-category mw-category-columns")

        if not blocks:
            raise Exception("Failed to get the main block with names")

        main_block = blocks[-1]

        names = [li.text for li in main_block.find_all("li")]
        last_name = names[-1]

        logger.info(f"Gather another batch of names: [{len(names)}]. Last name: [{last_name}]")

        all_names.extend(names)

        if last_name[0].lower() not in settings.rus_chars:
            logger.info("Successfully stopping...")
            logger.info("Save already gathered names")
            return all_names

        if random.random() > 0.95:
            logger.info("Random sleep. Parser will not be detected")
            time.sleep(random.randrange(4, 16))


def count_names(data: list[str]) -> dict[str: int]:
    """Count number of animals beginning with each letter"""
    animals_count = {char.upper(): 0 for char in settings.rus_chars}

    for word in data:
        if word.lower()[0] in settings.rus_chars:
            animals_count[word[0]] += 1

    return animals_count


def save_to_csv(content: dict[str: int]) -> None:
    logger.info("Saving to .csv...")

    path = os.path.join(settings.BASE_DIR, "beasts.csv")

    df = pd.DataFrame(list(content.items()), columns=["Word", "Count"])
    df.to_csv(path, index=False, encoding='utf-8')


def main() -> None:
    logger.info("Start...")

    session = httpx.Client()
    data = gather_names(session=session, url=settings.start_url)
    names = count_names(data)
    save_to_csv(names)


if __name__ == "__main__":
    main()
