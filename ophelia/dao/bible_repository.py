from .base_service import BaseService
from ophelia.models import BibleVerse
from .connection import get_session
from datetime import datetime

class BibleRespository(BaseService):

    def get_chapter(self, book, chapter):
        verses = self._session.query(BibleVerse).filter_by(
            book=book, chapter=chapter)
        
        if(verses in (None, "", [])): 
            return "Not found"
        
        result = ""
        for v in verses:
            result += str(v.verse)+" "+v.content+"\n"
        return result
    
    def get_verse(self, book, chapter, verse):

        result = self._session.query(BibleVerse).filter_by(
            book=book, chapter=chapter, verse=verse)
        print(result)

        if(result == None):
            return "Not found"

        return result.first().content
    
    def search(self, search_text):
        verses = self._session.query(BibleVerse).filter(
            BibleVerse.content.ilike(search_text)).get()
        
        print(verses)
        if(verses in (None, "", [])): 
            return "Not found"
        
        result = ""

        for v in verses:
            result +=  v.book+" "+v.chapter+ ": "+str(v.verse) +": "+v.content+"\n"
        print(result)
        return result