import requests
import bs4


def main():
    print_header()
    location = input("What's your location? ")
    html = get_html_from_web(location)


def print_header():
    print('--------------------')
    print('      WEATHER-CLI')
    print('--------------------')


def get_html_from_web(location):
    url = 'https://www.wunderground.com/weather/gb/{}'.format(location)
    response = requests.get(url)
    return response


def get_weather_from_html(html):
    # cityCss = '.region-content-header h1'
    # weatherScaleCss = '.wu-unit-temperature.wu-label'
    # weatherTempCss = '.wu-unit-temperature.wu-value'
    # weatherConditionCss = '.condition-icon'

    soup = bs4.BeautifulSoup(html, 'html.parser')
    loc = soup.find(class_='region-content-header').find('h1').get_text()
    condition = soup.find(class_='condition-icon').get_text()
    temp = soup.find(class_='wu-unit-temperature').find(class_='wu-value').get_text()
    scale = soup.find(class_='wu-unit-temperature').find(class_='wu-label').get_text()


if __name__ == '__main__':
    main()