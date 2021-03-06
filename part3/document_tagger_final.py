import sys, re
import os



def metadata_extract(data):
    title_search = re.compile(r'(title:\s*)(?P<title>.*([^s].*))', re.IGNORECASE)
    author_search=re.compile(r'(author:\s*)(?P<author>.*)',re.IGNORECASE)
    translator_search=re.compile(r'(translator:\s*)(?P<translator>.*)',re.IGNORECASE)
    illustrator_search=re.compile(r'(illustrator:\s*)(?P<illustrator>.*)',re.IGNORECASE)

    title=re.search(title_search,data)
    author=re.search(author_search,data)
    translator=re.search(translator_search,data)
    illustrator=re.search(illustrator_search,data)

    if title:
        title=title.group('title')

    if author:
        author=author.group('author')
    if translator:
        translator=translator.group('translator')
    if illustrator:
        illustrator=illustrator.group('illustrator')

    return title,author,translator,illustrator

def count_keywords(key,data):

    return data.count(key)


def open_doc(input_dir):
    count=0

    print input_dir
    for fl in (os.listdir(input_dir)):
        if fl.endswith('.txt'):
            fl_path=os.path.join(input_dir,fl)

            with open(fl_path,'r') as f:
                data=f.read()

                return data


def main():
    
    input_dir=str(raw_input("Enter the source dir: "))
    key1=str(raw_input("Enter word to search: "))
    key2=str(raw_input("Enter word to search: "))
    key3=str(raw_input("Enter word to search: "))
    for fl in (os.listdir(input_dir)):
        if fl.endswith('.txt'):
            fl_path=os.path.join(input_dir,fl)

            with open(fl_path,'r') as f:
                data=f.read()



    #dir = "texts"



    # dat=open_doc(dir)

            print metadata_extract(data)
            print "Your search for %s returned: %s" % (key1,count_keywords(key1,data))
            print "Your search for %s returned: %s" % (key2,count_keywords(key2,data=data))
            print "Your search for %s returned: %s" % (key3,count_keywords(key3,data=data))

if __name__=="__main__":
    main()

