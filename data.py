from mtgsdk import Card
from mtgsdk import Set
#from mtgsdk import Type
#from mtgsdk import Supertype
#from mtgsdk import Subtype
#from mtgsdk import Changelog
import json as j
import pandas as pd

cards = Card.where(language='english').all()

card_data = []
for card in cards:
    card_list = []
    name = card.name
    mana_cost = card.mana_cost
    cmc = card.cmc
    colors = card.colors
    color_identity = card.color_identity
    card_type = card.type
    text = card.text
    flavor = card.flavor
    power = card.power
    toughness = card.toughness
    loyalty = card.loyalty
    rarity = card.rarity
    release = card.release_date
    legalities = card.legalities
    set_name = card.set_name
    card_list = [name,mana_cost,cmc,co1lors,color_identity,card_type,text,flavor,power,toughness,loyalty,rarity,release,legalities,set_name]
    card_data.append(card_list)

csv_df = pd.DataFrame(card_data, columns =["name","mana_cost","cmc", "colors", "color_identity", "type", "text", "flavor","power","toughness","loyalty","rarity","release", "legalities", "set_name"])

csv_df.to_csv('test3.csv')
