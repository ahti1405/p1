import asyncio
import httpx
from bs4 import BeautifulSoup


word = 'Помидоры (свежие)'
url = 'https://fitaudit.ru/food'


async def main():

    async with httpx.AsyncClient() as client:

        r1 = await client.get(url)
        soup = BeautifulSoup(r1.text, 'lxml')
        next_url = soup.find('a', title=word)['href']
        r2 = await client.get(next_url)
        soup = BeautifulSoup(r2.text, 'lxml')
        p = soup.find('p', class_='him_bx__wrap')
        data = p.find_all('span', class_='js__msr_cc')

        calories = int(data[-6].text.split()[0])
        jiry = float(data[-5].text.split()[0].replace(',', '.'))
        belki = float(data[-4].text.split()[0].replace(',', '.'))
        uglevody = float(data[-3].text.split()[0].replace(',', '.'))
        voda = float(data[-2].text.split()[0].replace(',', '.'))
        zola = float(data[-1].text.split()[0].replace(',', '.'))

        # output = [calories, jiry, belki, uglevody, voda, zola]

        output = {
            'calories': calories,
            'jiry': jiry,
            'belki': belki,
            'uglevody': uglevody,
            'voda': voda,
            'zola': zola
        }
        print(output)


asyncio.run(main())
