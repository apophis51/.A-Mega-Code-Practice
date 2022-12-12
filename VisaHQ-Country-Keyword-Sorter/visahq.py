import re
import openpyxl
wu = openpyxl.load_workbook('angola.xlsx')
sheet = wu['angola']
keyword_list = ["age","long","time","validity","duration","process","processing","afghan","albania","algeria","andorra","angola","antigua and barbuda","argentina","armenia","australia","austria","azerbaijan","bahamas","bahrain","bangladesh","barbados","belarus","belgium","belize","benin","bhutan","bolivia","bosnia and herzegovina","botswana","brazil","brunei","bulgaria","burkina faso","burundi","ivory coast","cabo verde","cambodia","cameroon","canad","central african republic","chad","chile","china","colombia","comoros","congo","costa rica","croatia","cuba","cyprus","czech","congo","denmark","djibouti","dominica","dominican republic","ecuador","egypt","el salvador","equatorial guinea","eritrea","estonia","ethiopia","fiji","finland","france","gabon","gambia","georgia","germany","ghana","greece","grenada","guatemala","guinea","guyana","haiti","holy see","honduras","hungary","iceland","india","indonesia","iran","iraq","ireland","israel","italy","jamaica","japan","jordan","kazakhstan","kenya","kiribati","kuwait","kyrgyzstan","laos","latvia","lebanon","lesotho","liberia","libya","liechtenstein","lithuania","luxembourg","madagascar","malawi","malaysia","maldives","mali","malta","marshall islands","mauritania","mauritius","mexico","micronesia","moldova","monaco","mongolia","montenegro","morocco","mozambique","myanmar","namibia","nauru","nepal","netherlands","new zealand","nicaragua","niger","nigeria","north korea","north macedonia","norway","oman","pakistan","palau","palestine state","panama","papua new guinea","paraguay","peru","filip","philippines","poland","portug","qatar","romania","russia","rwanda","saint kitts and nevis","saint lucia","saint vincent and the grenadines","samoa","san marino","sao tome and principe","saudi arabia","senegal","serbia","seychelles","sierra leone","singapore","slovakia","slovenia","solomon islands","somalia","south africa","south korea","south sudan","spain","sri lanka","sudan","suriname","sweden","switzerland","syria","tajikistan","tanzania","thailand","timor-leste","togo","tonga","trinidad and tobago","tunisia","turkey","turkmenistan","tuvalu","uganda","ukraine","united arab emirates","uae","uk","british","united kingdom","united states of america","us","american","uruguay","uzbekistan","vanuatu","venezuela","vietnam","yemen","zambia","zimbabwe"]

#while tracker < 1:
for keyword in keyword_list:   #loop through the entire list
    current_row = 2  #we start the sheet from the second row
    while current_row < 1276:
        visa_column = 'a' + str(current_row)    #column a is name of visa
        keyword_column = 'b' + str(current_row)    #column b is keyword
        volume_column = 'k' + str(current_row)    #colomn k is global volume
        match = re.search(keyword, (sheet[keyword_column].value))
        s = (sheet[keyword_column].value)
        s = sorted(s.split(), key=str.lower) # ref is https://docs.python.org/3/howto/sorting.html
        if match is not None:
            #print the value stored in each row from that column
            print((sheet[visa_column].value),',',keyword,',',(sheet[keyword_column].value) , ',',
            (sheet[volume_column].value),',',s)
            current_row = current_row + 1
        else:
            current_row = current_row + 1


