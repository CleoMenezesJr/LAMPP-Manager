from requests import get

class CheckRelease:
    current_version = 'v0.0.3'
    
    @classmethod
    def _getInformation(cls):
        with get('https://api.github.com/repos/CleoMenezes/LAMPP-Manager/releases') as releases:
            cls.release = releases.json()[0]['tag_name']

    @classmethod
    def checkRelease(cls):
        cls._getInformation()
        if cls.current_version == cls.release:
            return False
        else:
            return True
        
