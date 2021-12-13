#Ignore these lines:
from bs4 import BeautifulSoup
import requests
import re
import widgets as wd

# please run at least once before changing anything

#SETTINGS------------------------
# enter your clash royale player tag below
PlayerTag = 'QJJLUCUJ0'
# enter how you want to display each chest below
SilverChest = "🪙"
GoldChest = "🌕"
GiantChest = "🗿"
MagicChest = "🔮"
EpicChest = "⚛️"
GoldCrate = "🏦"
LegendaryChest = "💎"
MegaLightningChest = "⚡️"
# enter how often you want this widget to update
MinutesToReload = "20"
# enter text to display under chests (optional
ExtraText = " 🔺                                                           "
#--------------------------------

#PD: this widget requires an internet connection to update

#PPD: This script may break if deckshop.pro decides to restrict access

#PPPD: text allignment may vary in preview and widget

#WARNING! DO NOT CHANGE THE NEXT PART OF THE CODE UNLESS YOU KNOW WHAT YOU'RE DOING
html_text = requests.get(f'https://www.deckshop.pro/spy/player/{PlayerTag}').text
soup = BeautifulSoup(html_text)
var1 = (soup.find("div", {"class": "flex flex-wrap items-center gap-3"}))
var2 = str(var1.findChildren)
#Chest1 = var2[115: ]

ChestName0 = re.search('src="/img/chests/(.+?).png"/>', var2).group(1)
WordCut = var2.find('</span>') + 7
var2 = var2[WordCut : ]

ChestName1 = re.search('src="/img/chests/(.+?).png"/>', var2).group(1)
WordCut = var2.find('</span>') + 7
var2 = var2[WordCut : ]

ChestName2 = re.search('src="/img/chests/(.+?).png"/>', var2).group(1)
WordCut = var2.find('</span>') + 7
var2 = var2[WordCut : ]

ChestName3 = re.search('src="/img/chests/(.+?).png"/>', var2).group(1)
WordCut = var2.find('</span>') + 7
var2 = var2[WordCut : ]

ChestName4 = re.search('src="/img/chests/(.+?).png"/>', var2).group(1)
WordCut = var2.find('</span>') + 7
var2 = var2[WordCut : ]

ChestName5 = re.search('src="/img/chests/(.+?).png"/>', var2).group(1)
WordCut = var2.find('</span>') + 7
var2 = var2[WordCut : ]

ChestName6 = re.search('src="/img/chests/(.+?).png"/>', var2).group(1)
WordCut = var2.find('</span>') + 7
var2 = var2[WordCut : ]

ChestName7 = re.search('src="/img/chests/(.+?).png"/>', var2).group(1)
WordCut = var2.find('</span>') + 7
var2 = var2[WordCut : ]

ChestName8 = re.search('src="/img/chests/(.+?).png"/>', var2).group(1)
WordCut = var2.find('</span>') + 7
var2 = var2[WordCut : ]

Total = (f'{ChestName0}  {ChestName1}  {ChestName2}  {ChestName3}  {ChestName4}  {ChestName5}  {ChestName6}  {ChestName7}  {ChestName8}')
Emojis = Total.replace("silver", SilverChest)
Emojis = Emojis.replace("gold", GoldChest)
Emojis = Emojis.replace("-crate", "Error")
Emojis = Emojis.replace(GoldChest + "Error", GoldCrate)
Emojis = Emojis.replace("magical", MagicChest)
Emojis = Emojis.replace("giant", GiantChest)
Emojis = Emojis.replace("mlc", MegaLightningChest)
Emojis = Emojis.replace("legendary", LegendaryChest)
Emojis = Emojis.replace("epic", EpicChest)

#Widget Creation
def hello_world():
    title = str(Emojis)
    
    
    
    subtitle = str(ExtraText)
    return title, subtitle
posts = hello_world()
widget = wd.Widget()

title = wd.Text(posts[0])
subtitle = wd.Text(posts[1])

layouts = [widget.small_layout, widget.medium_layout, widget.large_layout]
for l in layouts:
    l.add_row([title])
    l.add_row([subtitle])
# reload in x minutes
wd.schedule_next_reload(60 * float(MinutesToReload)) 
wd.show_widget(widget)