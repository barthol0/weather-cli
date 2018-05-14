import requests


def main():
    print_header()
    location = input("What's your location? ")
    get_html_from_web(location)


def print_header():
    print('--------------------')
    print('      WEATHER-CLI')
    print('--------------------')


def get_html_from_web(location):
    url = 'https://www.wunderground.com/weather/gb/{}'.format(location)
    response = requests.get(url)
    print(response.status_code)


if __name__ == '__main__':
    main()