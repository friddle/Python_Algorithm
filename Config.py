import ConfigParser

config	=	ConfigParser.ConfigParser()
config.readfp(open('config.ini'))
print config.get("information","Name")
