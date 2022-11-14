from rapidapi.get_coins import get_coins
import json


def main():
	obj = get_coins()
	obj = json.loads(obj.text)
	btc = obj.get('data').get('coins')[0]
	with open('test.txt', 'w', encoding = 'utf-8') as log:
		json.dump(btc, log, indent = 4)


if __name__ == '__main__':
	try:
		main()
	except BaseException as er:
		print(er)
