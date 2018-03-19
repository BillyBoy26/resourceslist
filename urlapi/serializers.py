

def serializeHtml(response):
    urldatas = {}
    title = response.html.find('title', first=True)
    if title is not None:
        urldatas['title'] = title.text

    sitename = response.html.find('meta[property=og\:site_name]', first=True)
    if sitename is not None:
        urldatas['sitename'] = sitename.attrs['content']

    description = response.html.find('meta[property=og\:description]', first=True)
    if description is not None:
        urldatas['description'] = description.attrs['content']

    image = response.html.find('meta[property=og\:image]', first=True)
    if image is not None:
        urldatas['imageurl'] = image.attrs['content']

    return urldatas
