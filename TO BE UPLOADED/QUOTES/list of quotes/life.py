'''

'''

file = open("life.txt", "w") 
import urllib.request , urllib.parse , urllib.error

for j in range(20):
    try:
        if(j==0):
            asle_url = 'https://www.goodreads.com/quotes/tag/life-quotes'
        else:
            asle_url = 'https://www.goodreads.com/quotes/tag/life-quotes'+"?page="+str(j+1)
        response = urllib.request.urlopen(asle_url)
        webContent = response.read().decode('UTF-8')


        lines = webContent.split('\n')
        for i in range(len(lines)):
            if('class="quoteText"' in lines[i]):

                # print(lines[i+1],"\n") # quote
                if("&ldquo;" in lines[i+1]):
                    lines[i+1] = lines[i+1].replace('&ldquo;','')
                if("&rdquo;" in lines[i+1]):
                    lines[i+1] = lines[i+1].replace('&rdquo;','')
                if("<br />" in lines[i+1]):
                    lines[i+1] = lines[i+1].replace('<br />','')
                if("      " in lines[i+1]):
                    lines[i+1] = lines[i+1].replace('      ','') 
                file.write(lines[i+1]+'\n')
                # quote done

                # print(lines[i+4],"\n") # author
                if("," in lines[i+4]):
                    lines[i+4] = lines[i+4].replace(',','')
                if("    " in lines[i+4]):
                    lines[i+4] = lines[i+4].replace('    ','')
                file.write(lines[i+4]+'\n')
                # author done
        print(str(j+1)+" page ho gya")
    except UnicodeEncodeError:
        print(str(j+1)+" page pe error hai")
        continue
file.close()