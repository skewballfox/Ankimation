import markdown
from bs4 import BeautifulSoup
import re
import genanki


def get_soup(file_name):
    html=markdown.markdown(open(file_name).read())
    soup = BeautifulSoup(html,'html.parser')
    return soup

def get_outline(soup):
    outline=soup.find_all(re.compile('^h[2-6]$'))#could make this way more efficient for partial matches
    return outline
    


def get_section(soup,outline, section_name):
    print ("starting get_section for ", section_name )
    section=[]
    section_start=soup.find(section_name.name,text=section_name.text)
    #if not the last item in the list, set the next section
    section_end=(outline[outline.index(section_name)+1] if True else None)
    for item in section_start.next_siblings:
        if item==section_end:
            break
        elif type(item) == type(section_name):
            section.append(item)
            print(item)
            print(type(item))
    return section

def set_text(line,q_set=None):
    """
    This Frankenstien's monster serves two purposes: create a dictionary
    of questions if none exist or creates a list of cards if it does
    needs to be refactored, this only exist until I can """
    print("starting set_question for ", line)
    if q_set is None:
        q_set={}
        formatter="{}"
        q_flag=True
    else:
        c_set=[]
        line="//"+line
        formatter=''
        q_flag=False
        print("yeet")
    delimiters=("//","@@","$$","!!", "££")
    splitter='|'.join(map(re.escape,delimiters))
    text_sets=[(s+formatter) for s in re.split(splitter,line) if s!='']
    print(text_sets)
    #get the indexes for the delimiters to determine their order
    #use the indexes to sort the delimters
    #also removes the delimiters not found in string
    indexes=[(d,line.find(d)) for d in delimiters if line.find(d)!=-1]
    n=0
    print(indexes)
    term=text_sets[0]
    front=''
    #sort using second column, use order as key for dictionary of text
    while indexes:
        k=min(indexes, key = lambda t: t[1])
        if q_flag is True:
            print(k[0])
            print(text_sets[n])
            q_set[k[0]]=text_sets[n]
        else:
            if k[0]=="//":
                front=q_set[k[0]].format(text_sets[n])+"?"
            elif k[0]=="$$":
                #using this to make cloze deletion card
                front=q_set[k[0]].replace("()","{}").format(term,"{{"+text_sets[n]+"}}")
                c_set.append(("cloze",front,None))    
            else:
                back=q_set[k[0]].format(text_sets[n])
                c_set.append(("reversible_model",front,back))
        n+=1
        indexes.pop(indexes.index(k))
    if q_flag is True:
        print(q_set)
        return q_set
    else:
        print(c_set)
        return c_set

"""def set_text(line, q_set):
    print("starting set text for: ", line)
    delimiters=("@@","$$","!!", "££")
    splitter='|'.join(map(re.escape,delimiters))
    done_flag=False
    front_text=re.split(splitter,line)
    print(front_text)
    while done_flag is False:
 """       
            
    
    

def build_deck(soup, outline):
    print("starting build_deck")
    deck_name=outline[0].text
    n=0
    end_section=False
    while end_section is False:
        deck_set=[]
        section=get_section(soup, outline, outline[n])
        for line in section:
            print(line.text, type(line.text))
            if (line.text).startswith("//"):
                q_set=set_text(line.text)
            else:
                cards=set_text(line.text,q_set)
                print(cards)
                deck_set+=cards
        n+=1
        for i in deck_set:
            print(i)
        if n==2:
            end_section=True
            

if __name__=="__main__":
    soup=get_soup("/home/daedalus/gdrive/Notes/HTML5.md")
    outline=get_outline(soup)
    build_deck(soup,outline)