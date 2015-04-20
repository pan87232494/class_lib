import bs4
from bs4 import BeautifulSoup
from bs4 import element
import django.utils.encoding
import re

class Strip_tag_with_proper_action:

    #user should input with BeautifulSoup section(class bs4.element.Tag), then init your operation to each tag, for web scrab use
    #please help improve it. Thanks
    #tag_replace_hash is tag : two element array tag_name:[ string_insert_before, string_insert_after]

    #tag section like <div> <tr> test <i> iiiiii</i> </tr>bbbb</div>
    #hash can be {
    # u'b':['',''],
    # u'tr':['','\n'],
    # u'div':['\n','\n'],
    # u'i':[''','''],
    #}

    def __init_(tag_replace_hash):
        self.tag_replace_hash=tag_replace_hash
    
    def  handle_each_tag(tag_section,tag_replace_hash):
        #if you want to add restrtion for logic, add here
        return tag_replace_hash[tag_section][0]+strip_tag_in_contents(tag_section)+tag_replace_hash[tag_section][1]

    def strip_tag_in_contents(soup_contents,tag_replace_hash):

        try:
            if not isinstance(list,text_string_seg_list):
                pass
        except UnboundLocalError:
            # if text_string_seg_list not exist, for recuirve function call
            text_string_seg_list = []
    
        for i in soup_contents.contents:

            if isinstance(i, bs4.element.Tag):
                text_string_seg_list.append(handle_each_tag(i.contents))

             else:
                # elif isinstance(i,bs4.element.NavigableString):
                text_string_seg_list.append(django.utils.encoding.smart_bytes(i, strings_only=False, errors='strict').replace("\n", " "))
    
        text_string = "".join(text_string_seg_list)
        return text_string

