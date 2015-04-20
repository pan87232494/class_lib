# class_lib
my class lib
for class strip_tag_with_proper action:
purpose, to remove some tag, but not all tag, from web scrab result. 
For example you want some xml data, you just want to remove some html tag, and replace with correct "\n" or " ".



    #user should input with BeautifulSoup section(class bs4.element.Tag), then init your operation to each tag, for web scrab use
    #please help improve it. Thanks
    #tag_replace_hash is tag : two elements array tag_name:[ string_insert_before, string_insert_after]

    #tag section like <div> <tr> test <i> iiiiii</i> </tr>bbbb</div>
    #hash can be {
    # u'b':['',''],
    # u'tr':['','\n'],
    # u'div':['\n','\n'],
    # u'i':[''','''],
    #}
