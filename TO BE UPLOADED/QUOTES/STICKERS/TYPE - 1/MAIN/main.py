'''
ab fonts ka random ya kram se ek bahara se variable lete ue differnet fonts lene h
kafi sare quotes ko text list me dalna hai aur randomly nikalna hai
150 images bna ke selected nikalni hai
'''

'''
background me circle - purple , transparency low

'''

from PIL import Image , ImageDraw, ImageFont
from random import randint
fonts = ['11S0BLTI.TTF', '12tonsushi.ttf', '8bitlim.ttf', 'Aaargh.ttf', 'ABBERANC.TTF', 'ABEAKRG.TTF', 'abscib__.ttf', 'absci___.ttf', 'accid__.ttf', 'Action Man Bold.ttf', 'Action_Force.ttf', 'ADD-JAZZ.TTF', 'AdineKirnberg-Script.ttf', 'Adventure.ttf', 'Advokat Modern.ttf', 'Aerovias Brasil NF.ttf', 'aggstock.ttf', 'Aileenation.ttf', 'AIR_____.TTF', 'AldotheApache.ttf', 'ALEXA.TTF', 'Alice and the Wicked Monster.ttf', 'ALIEESBI.TTF', 'ALIEESB_.TTF', 'ALIEESI_.TTF', 'ALIEES__.TTF', 'ALIEN5.TTF', 'Aliquam.ttf', 'AliquamREG.ttf', 'AliquamRit.ttf', 'Aliquamulti.ttf', 'AllCaps.ttf', 'Alpha Thin.ttf', 'AmazOOSTROVFine.ttf', 'American Captain.ttf', 'ANDOVER_.TTF', 'AnkeHand.ttf', 'annifont.ttf', 'ap.ttf', 'ARCHBLC_.TTF', 'arialbd.ttf', 'ARMOPB__.TTF', 'Artbrush.ttf', 'Atlantic_Cruise-Demo.ttf', 'ATOMIC__.TTF', 'ATROX.TTF', 'autobahn.ttf', 'AZRAEL__.TTF', 'BabelSans-Bold.ttf', 'BabelSans-BoldOblique.ttf', 'BabelSans-Oblique.ttf', 'BabelSans.ttf', 'Backpack_PersonalUse.ttf', 'BADABB__.TTF', 'BankGothic-Regular DB.ttf', 'BankGothic-Regular.ttf', 'basictitlefont.ttf', 'BastardusSans.ttf', 'Battleground.ttf', 'BAUERG__.TTF', 'BEBAS.TTF', 'BEBAS__.TTF', 'BEBAS___.TTF', 'belizarius.ttf', 'BENNB___.TTF', 'big_noodle_titling.ttf', 'big_noodle_titling_oblique.ttf', 'black.ttf', 'Blacklisted.ttf', 'BLACKOUT.TTF', 'BLOODY.TTF', 'bluebold.ttf', 'bluecond.ttf', 'BLUEHIGD.TTF', 'bluehigh.ttf', 'BNMachine.ttf', 'bobcaygr.ttf', 'bold.ttf', 'BOLIDEMF.TTF', 'Bombing.ttf', 'boston.ttf', 'bottix.ttf', 'BOTTRBB_.TTF', 'BOTTRBRG.TTF', 'bradybun.ttf', 'bronic.ttf', 'BRUSHCUT.TTF', 'Brushstrike trial.ttf', 'BUBBLEBO.TTF', 'budeasym.ttf', 'Buran USSR.ttf', 'Buran USSR_0.ttf', 'cartoonist_kooky.ttf', 'Champagne & Limousines Bold.ttf', 'charbb_reg.ttf', 'CHERI___.TTF', 'CHICM___.TTF', 'CHICSA__.TTF', 'chinese rocks rg.ttf', 'CHINESER.ttf', 'CHINESETAKEAWAY.ttf', 'ClearLine_PERSONAL_USE_ONLY.ttf', 'Colors Of Autumn.ttf', 'COMEN___.TTF', 'COMEP___.TTF', 'Comic Book.ttf', 'Comicv2b.ttf', 'Comicv2bi.ttf', 'Comicv2c.ttf', 'coolvetica rg.ttf', 'Copper Canyon WBW.ttf', 'corbel.ttf', 'corbelb.ttf', 'corbeli.ttf', 'corbelz.ttf', 'COUTURE-Bold.ttf', 'CREABBB_.TTF', 'CREABBRG.TTF', 'Crimes Times Six.ttf', 'criticized.ttf', 'DAELC___.TTF', 'Dark Ministry.ttf', 'DEADJIM.TTF', 'Deadly Inked.ttf', 'deathrattlebb_reg.ttf', 'DHF Story Brush.ttf', 'DIMITRI_.TTF', 'distortion_of_the_brain_and_mind.ttf', 'DistTh__.ttf', 'djcourag.ttf', 'DK Face Your Fears.ttf', 'edo.ttf', 'engebold.ttf', 'FAKEP___.TTF', 'FAREWELL.TTF', 'Florsn02.ttf', 'FONT.TTF', 'Forque.ttf', 'Freshman.ttf', 'Friday13v12.ttf', 'FUNDR___.TTF', 'gadugib.ttf', 'GOLONG.TTF', 'Gotham Nights.ttf', 'GROBOLD_0.TTF', 'GrutchGrotesk-CondensedLight.ttf', 'HACKED.ttf', 'Harabara.ttf', 'hawkmooncondital.ttf', 'HEADOH_.TTF', 'helsinki.ttf', 'HONEJ___.ttf', 'HoneyScript-SemiBold.ttf', 'HOOKED.TTF', 'Hursheys.ttf', 'impact.ttf', 'IRON MAN OF WAR 002 NCV.ttf', 'jampact.ttf', 'Jedi.ttf', 'KataBidalanBold.ttf', 'KENYAN.TTF', 'KINGRICH.TTF', 'kirsty__.ttf', 'Kitchenpolice.TTF', 'KLEPTOCR.TTF', 'Korner Deli NF.ttf', 'kr1.ttf', 'KRAVET__.TTF', 'krazynights.ttf', 'land-v2.ttf', 'Laser Rod.ttf', 'later_on.ttf', 'LeelaUIb.ttf', 'LeviReBrushed.ttf', 'libelsuit.ttf', 'Lobster-Regular.ttf', 'LOKICOLA.TTF', 'Long_Shot.ttf', 'LOVEA___.TTF', 'LT Oksana Bold.ttf', 'ltromatic bold.ttf', 'lucid.ttf', 'MAGNUM__.TTF', 'mangat.ttf', 'MankSans-Medium.ttf', 'Mathematical Pi 1.ttf', 'medium.ttf', 'medra___.ttf', 'Minecraftia-Regular.ttf', 'Monotoon KK.ttf', 'Moon Flower Bold.ttf', 'Moon Flower.ttf', 'Moscoso.ttf', 'Mouser.ttf', 'nerdproof.ttf', 'nevis.ttf', 'NFS_by_JLTV.ttf', 'NHL Ducks.ttf', 'NICKODE1.TTF', 'NIOBRG__.TTF', 'Nirmala.ttf', 'NirmalaB.ttf', 'novem___.ttf', 'ObelixProB-cyr.ttf', 'OLIVERSB.TTF', 'OpenSans-Semibold.ttf', 'OperationalAmplifier.ttf', 'Opificio.ttf', 'Opificio_Bold.ttf', 'overhead.ttf', 'Ozonelayer.ttf', 'Pacifico.ttf', 'pakenham.ttf', 'panicbuttonbb_ital.ttf', 'panicbuttonbb_reg.ttf', 'Permanent.ttf', 'Phantomime.ttf', 'POLOBM__.TTF', 'PORNSA__.TTF', 'PRICEDOW.TTF', 'pricedown bl_0.ttf', 'PRIMER.ttf', 'PRIMERB.ttf', 'PUSSSA__.TTF', 'PUSSS___.TTF', 'Qiroff.ttf', 'RADIOSTA.TTF', 'RAPHAEL_.TTF', 'ratio___.ttf', 'REVOLUTION.ttf', 'Righteous-Regular.ttf', 'ROCKYAOE.TTF', 'ROTHWELL.TTF', 'SamdanCondensed.ttf', 'Schluber.ttf', 'segoeuib.ttf', 'SelznickNormal.ttf', 'seriously.ttf', 'SF Arch Rival Bold.ttf', 'SF Atarian System.ttf', 'SF Buttacup Lettering Bold Oblique.ttf', 'SF Buttacup Lettering Bold.ttf', 'SF Buttacup Lettering.ttf', 'SF Cartoonist Hand SC Bold Italic.ttf', 'SF Cartoonist Hand.ttf', 'SF Collegiate Solid.ttf', 'SF Espresso Shack Bold Italic.ttf', 'SF Espresso Shack Bold.ttf', 'SF Foxboro Script Bold.ttf', 'SF Foxboro Script Extended Bold.ttf', 'SF Foxboro Script.ttf', 'SF Grunge Sans Bold Italic.ttf', 'SF Grunge Sans Bold.ttf', 'SF Grunge Sans Italic.ttf', 'SF Grunge Sans SC Italic.ttf', 'SF Grunge Sans SC.ttf', 'SF Hollywood Hills Bold Italic.ttf', 'SF Hollywood Hills Bold.ttf', 'SF Iron Gothic Bold Oblique.ttf', 'SF Juggernaut Condensed Italic.ttf', 'SF Juggernaut Condensed.ttf', 'SF Laundromatic Bold Oblique.ttf', 'SF Movie Poster Bold Italic.ttf', 'SF Movie Poster Bold.ttf', 'SF New Republic.ttf', 'SF Old Republic Bold.ttf', 'SF Old Republic SC Bold Italic.ttf', 'SF Old Republic SC Bold.ttf', 'SF Speakeasy Oblique.ttf', 'SF Speakeasy.ttf', 'SF Sports Night NS Upright.ttf', 'SF Sports Night NS.ttf', 'SF Toontime B Italic.ttf', 'SF Toontime B.ttf', 'SF Willamette Bold Italic.ttf', 'SF Willamette Bold.ttf', 'SF Willamette.ttf', 'SHLOP.TTF', 'SkarpaLt.ttf', 'slender.ttf', 'Slim Extreme.ttf', 'Slimania Bold.ttf', 'Snowstorm Kraft.ttf', 'Snowstorm Kraft_0.ttf', 'Something Strange.ttf', 'SOVIET4.TTF', 'spacefr.ttf', 'spacefri.ttf', 'Sparkler-demo.ttf', 'SPEEM___.TTF', 'Square.ttf', 'SQUEALER.TTF', 'squitcher.ttf', 'srgt6pack.ttf', 'steelfib.ttf', 'steelfis.ttf', 'stentiga.ttf', 'STEREOHI.TTF', 'Streamster.ttf', 'tahoma.ttf', 'TalkingToTheMoon.ttf', 'Tall Film Fine.ttf', 'Tall Film Oblique.ttf', 'Tall Film.ttf', 'Tall Films Expanded Oblique.ttf', 'Tall Films Expanded.ttf', 'Tall Films Fine Oblique.ttf', 'talldark.ttf', 'TAPEWORM.TTF', 'telegrafico_by_ficod.ttf', 'TequilaSunrise-Regular.ttf', 'thin.ttf', 'Timeline.ttf', 'TOMMY__.TTF', 'True Lies.ttf', 'tussle.ttf', 'Ubuntu-B.ttf', 'UltraCondensedSansSerif.ttf', 'UNICORN.TTF', 'Unrealised.ttf', 'Untidy Italic Skrawl.ttf', 'updik___.ttf', 'upheavtt.ttf', 'Vanadine Bold.ttf', 'vantage.ttf', 'Vegetable.ttf', 'verdana.ttf', 'verdanab.ttf', 'vikingsquadboldital.ttf', 'vikingsquadcond.ttf', 'VIOLATIO.TTF', 'visitor2.ttf', 'viva01.ttf', 'waltographUI.ttf', 'Waukegan LDO Black Oblique.ttf', 'Waukegan LDO Black.ttf', 'weaver.ttf', 'webster.ttf', 'WELTRON2.TTF', 'WELTSP__.TTF', 'WETPM___.TTF', 'Wolf in the City Light.ttf', 'Write2.ttf', 'wunderbar.ttf', 'wyldb.ttf', 'wyldt.ttf', 'X-rayTed.TTF', 'X-rayTed_s.TTF', 'XO.TTF', 'YanoneKaffeesatz-Bold.ttf', 'YanoneKaffeesatz-Light.ttf', 'YanoneKaffeesatz-Regular.ttf', 'YanoneKaffeesatz-Thin.ttf', 'YARDSALE.TTF', 'Yearsupplyoffairycakes.ttf', 'Yellowc.ttf', 'yesterdaysmeal.ttf', 'yonder.ttf', 'yukari.ttf', 'zeldadxt.ttf', 'zephyrea.ttf', 'zephyreg.ttf', 'ZITZ____.TTF', 'ZUDJI___.TTF']
font_id = randint(0 , 363)
myfont = ImageFont.truetype('fonts\\'+fonts[font_id],250)
quotes = ["Every twenty years I reinvent myself.","I have time to fix this.","Fearlessness is the mother of reinvention.","This is your year to sparkle.","Be your own person, be unique.","Still fit into high school earrings.","I made a choice about business.","You got to nourish to flourish.","What's the stop sign mean again?","Change what you are complaining about.","Don’t wait for opportunity. Create it!","A decision was made, I complied.","I live my best life now.","I'm figuring it out by myself.","Recipe for failure. Changed my ingredients.","Talking without action is just complaining.","Stay patient and trust your journey.","I am this now and always.","I stopped getting my piano tuned.","Be young while you still can.","Associate with people who inspire you.","I learned mechanics in rocket league.","Every problem has a creative solution.","Someone has to do the paperwork.","Lost in wilderness, he found himself.","Normal is boring, weird is fun.","Boisterous gas freed, relief, remorse, pride!","Nothing to declare. Much to remember.","Lovers gonna love, haters gonna hate.","Sharp new yellow pencil. Limitless potential.","Spongebob is my one true love.","Apathetic prophet makes a pathetic profit.","Lost my wallet, found my desires.","Insomnia gives me time to think.","Married, till fatness do us part.","Say something nice or don't talk.","Coffee before art, goodbye straight lines.","I got it from my mama.","Painfully, he changed is to was.","Protect your dreams from your nightmare.","Lightning hides the color of night.","Honestly, all crows are not ravens.","Sorry soldier, shoes sold in pairs.","Love hurts because it holds hearts.","Voyager still transmitted, but Earth didn’t.","Seed becomes a tree, son becomes stranger.","Power does not pardon, power punishes.","I asked, you answered in silence.","Sometimes pretty birds cannot sing well.","Tripped over luck, stumbled upon tragedy.","Recover never really ends, does it?"]
l_quotes = len(quotes)

img = Image.new('RGBA',(5000,5000),color=(255,2,2,0))
for i in range(20):
    font_id = randint(0 , 363)
    myfont = ImageFont.truetype('fonts\\'+fonts[font_id],250)
    
    draw = ImageDraw.Draw(img)
    x,y,z = randint(0,255) ,randint(0,255) ,randint(0,255)

    text = quotes[randint(0,l_quotes-1)]
    # x,y,z = randint(0,255) ,randint(0,255) ,randint(0,255)
    # text_x , text_y , text_z  = randint(0,255) , randint(0,255) , randint(0,255)
    draw.rectangle([(0,0),(5000,666)],fill=(x,y,z,180),outline=(x,y,z),width=50)
    draw.text((2500,470),text,fill = 'white',anchor='md',font=myfont)
    
    text = quotes[randint(0,l_quotes-1)]
    # x,y,z = randint(0,255) ,randint(0,255) ,randint(0,255)
    # text_x , text_y , text_z  = randint(0,255) , randint(0,255) , randint(0,255)
    draw.rectangle([(0,866),(5000,1532)],fill=(x,y,z,180),outline=(x,y,z),width=50)
    draw.text((2500,1336),text,fill = 'white',anchor='md',font=myfont)
    
    text = quotes[randint(0,l_quotes-1)]
    # x,y,z = randint(0,255) ,randint(0,255) ,randint(0,255)
    # text_x , text_y , text_z  = randint(0,255) , randint(0,255) , randint(0,255)
    draw.rectangle([(0,1732),(5000,2398)],fill=(x,y,z,180),outline=(x,y,z),width=50)
    draw.text((2500,2202),text,fill = 'white',anchor='md',font=myfont)
    
    text = quotes[randint(0,l_quotes-1)]
    # x,y,z = randint(0,255) ,randint(0,255) ,randint(0,255)
    # text_x , text_y , text_z  = randint(0,255) , randint(0,255) , randint(0,255)
    draw.rectangle([(0,2598),(5000,3264)],fill=(x,y,z,180),outline=(x,y,z),width=50)
    draw.text((2500,3068),text,fill = 'white',anchor='md',font=myfont)
    
    text = quotes[randint(0,l_quotes-1)]
    # x,y,z = randint(0,255) ,randint(0,255) ,randint(0,255)
    # text_x , text_y , text_z  = randint(0,255) , randint(0,255) , randint(0,255)
    draw.rectangle([(0,3464),(5000,4130)],fill=(x,y,z,180),outline=(x,y,z),width=50)
    draw.text((2500,3934),text,fill = 'white',anchor='md',font=myfont)
    
    text = quotes[randint(0,l_quotes-1)]
    # x,y,z = randint(0,255) ,randint(0,255) ,randint(0,255)
    # text_x , text_y , text_z  = randint(0,255) , randint(0,255) , randint(0,255)
    draw.rectangle([(0,4330),(5000,5000)],fill=(x,y,z,180),outline=(x,y,z),width=50)
    draw.text((2500,4800),text,fill = 'white',anchor='md',font=myfont)
    
    img.save('q'+str(i)+'.png')
    img = Image.new('RGBA',(5000,5000),color=(255,2,2,0))