import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def scrape_streamly_metadata(url):
    options = Options()
    options.headless = True
    options.add_arguement
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    metadata_mapping = {
        "title": '//meta[@property="og:title"]',
        "source_synopsis": '//meta[@name="description"]',
        "source_content_tags": '//meta[@name="keywords"]',
        "source_content_type": '//meta[@property="og:type"]',
        "source_feature_image": '//meta[@property="og:image"]',
        "source_authors": "",
        "source_category": "",
        "source_published_date": "",
        "source_modified_date": "",
        "source_content_issponsored": "",
        "source_content_label": "",
    }

    scraped_data = {}
    for key, xpath in metadata_mapping.items():
        if xpath:
            element = driver.find_element_by_xpath(xpath)
            scraped_data[key] = element.get_attribute("content")
        else:
            scraped_data[key] = ""

    # Scrape the number of views and likes using their corresponding XPaths
    views_xpath = "/html/body/div[1]/div/main/div/div[1]/div[2]/div/div[2]/div[1]/div/div[3]/div[1]/div[1]/div/span"
    likes_xpath = "/html/body/div[1]/div/main/div/div[1]/div[2]/div/div[2]/div[1]/div/div[3]/div[1]/div[1]/button/span"

    views_element = driver.find_element_by_xpath(views_xpath)
    likes_element = driver.find_element_by_xpath(likes_xpath)

    scraped_data["views"] = views_element.text
    scraped_data["likes"] = likes_element.text

    driver.quit()

    return scraped_data


if __name__ == "__main__":
    url = "https://streamly.video/video/child-refugee-turned-tech-mogul"
    result = scrape_streamly_metadata(url)
    json_result = json.dumps(result, indent=2)
    print(json_result)
