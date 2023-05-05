import requests
from lxml import html


def scrape_streamly_metadata(url):
    response = requests.get(url)
    tree = html.fromstring(response.content)


    metadata_mapping = {
        'title': '//meta[@property="og:title"]/@content',
        'source_synopsis': '//meta[@name="description"]/@content',
        'source_content_tags': '//meta[@name="keywords"]/@content',
        'source_content_type': '//meta[@property="og:type"]/@content',
        'source_feature_image': '//meta[@property="og:image"]/@content',
        'source_authors': '',
        'source_category': '',
        'source_published_date': '',
        'source_modified_date': '',
        'source_content_issponsored': '',
        'source_content_label': '',
        }

    scraped_data = {}
    for key, xpath in metadata_mapping.items():
        if xpath:
            scraped_data[key] = tree.xpath(xpath)[0] if tree.xpath(xpath) else ''
        else:
            scraped_data[key] = ''


    # Scrape the number of views and likes using their corresponding XPaths
    views_xpath = '/html/body/div[1]/div/main/div/div[1]/div[2]/div/div[2]/div[1]/div/div[3]/div[1]/div[1]/div/span'
    likes_xpath =  '/html/body/div[1]/div/main/div/div[1]/div[2]/div/div[2]/div[1]/div/div[3]/div[1]/div[1]/button/span'

    scraped_data['views'] = tree.xpath(views_xpath)[0] if tree.xpath(views_xpath) else ''
    scraped_data['likes'] = tree.xpath(likes_xpath)[0] if tree.xpath(likes_xpath) else ''

    return scraped_data


if __name__ == "__main__":
    url = "https://streamly.video/video/child-refugee-turned-tech-mogul"
    result = scrape_streamly_metadata(url)
    print(result)
