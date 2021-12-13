import random

adjective = [
	"Big",
	"Small",
	"Beautiful",
	"Ugly",
	"Lonely",
	"Friendly",
	"Furious",
	"Fast",
	"Slow",
	"Living",
	"Dead",
	"Strange",
	"Wonderful",
	"Honorable",
	"Faithful",
	"Pure",
	"Bright",
	"Shining",
	"Fragile",
	"Electric",
	"Honest",
	"Curious",
	"Lucky",
	"Wicked",
	"Spectacular",
	"Generous",
	"Amazing",
	"Courageous",
	"Majestic",
	"Crazy",
	"Independant",
	"Evil",
	"Eternal",
	"Pointless",
	"Meaningful",
	"Obedient",
	"Insane",
	"Fortunate",
	"Mysterious",
	"Funny"
]

noun = [
	"Ocean",
	"Queen",
	"King",
	"Mistake",
	"Life",
	"Spirit",
	"Light",
	"Home",
	"Ghost",
	"Friend",
	"Man",
	"Woman",
	"Child",
	"Prison",
	"Dust",
	"Day",
	"Night",
	"Revolution",
	"Discovery",
	"Beast",
	"War",
	"Fire",
	"Flame",
	"Motion",
	"Opportunity",
	"Wound",
	"Redemption",
	"Signal",
	"Wave",
	"Storm",
	"Coast",
	"Process",
	"Justice",
	"Breathe",
	"Choice"
]

def name_image():
	return str(random.choice(adjective) + " " + random.choice(noun) + ".png")