import re

class Cleaner:

    def normalize_text(self, raw: str) -> str:
        cleaned = re.sub(r'(?m)^(From|Subject|Organization|Lines|Reply-To|NNTP-Posting-Host|Distribution):.*$', '',
                         raw)

        cleaned = re.sub(r'(?m)^>.*$', '', cleaned)


        cleaned = cleaned.replace("\r\n", " ").replace("\n", " ")


        cleaned = re.sub(r'\s+', ' ', cleaned)


        cleaned = cleaned.strip()

        return cleaned