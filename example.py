from pyconfig import ConfigStore

conf = ConfigStore("vestub", {"url":"http://vestub.com"}, True)
print(conf.get("url"))
conf.set("Title", "Social Media for Idea Owners and Investors")
conf.set("Tags", "Tech, Investors, Social Media")
conf.set("Tags.Topic", "Python")
conf.set({"Subject.Topic":"English"})
print(conf.all())
print(conf.path)

conf.delete("url")
print(conf.all())
