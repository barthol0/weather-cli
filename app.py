import requests
import bs4


def main():
    print_header()
    loc = input("What's your location? ")
    html = get_html_from_web(loc)
    get_weather_from_html(html)


def print_header():
    print('--------------------')
    print('      WEATHER-CLI')
    print('--------------------')


def get_html_from_web(loc):
    url = 'https://www.wunderground.com/weather/gb/{}'.format(loc)
    response = requests.get(url)
    return response.text


def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    loc = soup.find(class_='city-header').find('h1').get_text()
    condition = soup.find(class_='condition-icon').get_text()
    temp = soup.find(class_='wu-unit-temperature').find(class_='wu-value').get_text()
    scale = soup.find(class_='wu-unit-temperature').find(class_='wu-label').get_text()

    loc = cleanup_text(loc)
    condition = cleanup_text(condition)
    temp = cleanup_text(temp)
    scale = cleanup_text(scale)
    print(loc, condition, temp, scale)


def cleanup_text(text: str):
    if not text:
        return text

    text = text.strip()
    return text  


if __name__ == '__main__':
    main()