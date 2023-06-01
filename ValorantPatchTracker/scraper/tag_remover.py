from bs4 import BeautifulSoup, NavigableString, Comment


class TagRemover:
    def __init__(self) -> None:
        pass
    
    def remove_tag_by_class(self, div_main: NavigableString, tag_name: str, tag_class: str):
        '''Remove tags by class.'''
        element = div_main.find(tag_name, class_=tag_class)
        if element is None:
            pass
        else:
            element.decompose()
            
    def remove_tag_by_text(self, div_main: NavigableString, tag_name:str, text: str):
        '''Remove h2 tags by text.'''
        elements = div_main.find_all(tag_name)
        for element in elements:
            if element.text.strip() == text:
                element.decompose()
                
    def remove_tag(self, div_main: NavigableString, tag: str):
        '''Remove a tag'''
        for element in div_main(tag):
            element.decompose()