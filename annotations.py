from requests_html import HTMLSession

headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}
url = 'https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=object+detection+in+aerial+image+&btnG=&oq=ob'

session = HTMLSession()
response=session.get('https://python.org/')

print(response)