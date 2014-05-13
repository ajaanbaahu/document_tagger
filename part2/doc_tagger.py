import sys, re
import os

directory=str(raw_input("Enter the source folder"))

title_search = re.compile(r'(title:\s*)(?P<title>.*([^s].*))', re.IGNORECASE)

author_search=re.compile(r'(author:\s*)(?P<author>.*)',re.IGNORECASE)
translator_search=re.compile(r'(translator:\s*)(?P<translator>.*)',re.IGNORECASE)
illustrator_search=re.compile(r'(illustrator:\s*)(?P<illustrator>.*)',re.IGNORECASE)



search_st=str(raw_input("Enter the word to search :"))
search_st2=str(raw_input("Enter the word to search :"))
search_st3=str(raw_input("Enter the word to search :"))

for fl in (os.listdir(directory)):  #for each item that appears in the directory
    if fl.endswith('.txt'):       #if it's a text file

	
        #print 'Processing {0}.'.format(fl)
		
		
        fl_path = os.path.join(directory, fl) #the full path to the file is the directory plus
        #

        #
        with open(fl_path, 'r') as f:
              #open the file as f
            data=f.read()
            output1="Search for '%s' gave %s"% (search_st, data.count(search_st))
            output2="Search for '%s' gave %s"% (search_st2, data.count(search_st))
            output3="Search for '%s' gave %s"% (search_st3, data.count(search_st))

            title=re.search(title_search,data).group('title')
            author=re.search(author_search,data)
            translator=re.search(translator_search,data)
            illustrator=re.search(illustrator_search,data)
            if author:
                author=author.group('author')
            if translator:
                translator=translator.group('translator')
            if illustrator:
                illustrator=illustrator.group('illustrator')

            print "Title of doc %s" % title
            print "Author of doc %s" % author
            print "Translator of doc %s" % translator
            print "Illustrator of doc %s" % illustrator


            print output1
            print output2
            print output3

            print '*'*40
