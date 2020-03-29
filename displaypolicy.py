# -*- coding: UTF-8 -*-

MAXLEN = 4096

def default_policy(item):
    parse_mode = 'html'
    disable_web_page_preview = 'True'
    #disable_notification = 'Ture'
    
    maxlen = 600
    po = ""
    po = '<b>' + item['title'] + '</b>'
    po += '\n\n'
    
    if len(item['paragraphs']) > maxlen:
        # Post the link only.
        po += '<a href=\"' + item['link'] + '\">Link</a>\n\n'
        # If there is exceed the limit, enable web page preview.
        disable_web_page_preview = 'False'
    else:
        po += item['paragraphs']
    
    po += item['time']
    po += '\n'
    po += item['source']
    
    assert len(po) < MAXLEN
    
    return po, parse_mode, disable_web_page_preview