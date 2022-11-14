import requests


def getter(url, querystring, headers):

	return requests.request("GET", url, headers = headers, params = querystring)


def get_coins():

	url = "https://coinranking1.p.rapidapi.com/coins"

	querystring = {"referenceCurrencyUuid":"yhjMzLPhuIDl","timePeriod":"24h","tiers[0]":"1","orderBy":"marketCap","orderDirection":"desc","limit":"50","offset":"0"}

	headers = {
		"X-RapidAPI-Key": "RAPIDAPI_KEY", 
		"X-RapidAPI-Host": "coinranking1.p.rapidapi.com"
	}
	return getter(url, querystring, headers)


