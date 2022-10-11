from gingerit.gingerit import GingerIt
import json
text="i luv u"
parser = GingerIt()
js=json.load(parser.parse(text))
print(js)