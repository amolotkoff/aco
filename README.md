# pconf
Python configurator for my projects
File settings.json must be in same folder as main.py script

*Example of settings.json*
```json
{
	"meta": {
		"path": "./settings.json"
	},
	"settings": {
		"default": {
			"cache" : {
				"default": {
					"cache": "aiocache.SimpleMemoryCache",
					"serializer": {
						"class": "aiocache.serializers.StringSerializer"
					}
				}
			},
			"bot": {
				"token": ""
			},
			"moex": {
				"host": "iss.moex.com",
				"securities_path": "iss/engines/stock/markets/shares/boards/{board}/securities.json?iss.meta=off&iss.only=securities",
				"security_path": "iss/engines/stock/markets/shares/securities/{ticker}.json?iss.meta=off&iss.only=securities"
			}
		},
		"dev": {},
		"prod": {}
	}
}
```
