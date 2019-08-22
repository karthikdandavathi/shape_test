from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

class ShapeTest:
    def __init__(self,url):
        self.url = url
        self.browser = self.setup()
        self.content = self.browser.find_element_by_xpath('//*[@id="content"]/div/div').text
        self.images = self.browser.find_elements_by_tag_name('img')
        self.image_links = self.get_image_links()

    def setup(self):
        self.opts = Options()
        self.opts.set_headless()
        browser = Firefox(options=self.opts)
        browser.get(self.url)
        return browser

    def find_longest_word(self,content):
        #finding longest word in content
        longest_word = ""
        word_list = content.split(' ')
        for word in word_list:
            longest_word = max(word,longest_word)
        return longest_word


    def is_atleast(self,threshold):
        if len(self.find_longest_word(self.content)) >= threshold:
            return True
        return False

    def get_image_links(self):
        image_links = []
        for image in self.images:
            image_links.append(image.get_attribute("src"))
        return image_links

    def check_for_punisher(self,punisher):
        if punisher in self.image_links:
            return True
        return False

if __name__ == '__main__':
    url = "https://the-internet.herokuapp.com/dynamic_content"
    shape_test = ShapeTest(url)

    # checks if longest word is greater than 10 characters
    print(shape_test.is_atleast(10))

    #prints longest word
    print(shape_test.find_longest_word(shape_test.content))

    #checks for punisher image in the content
    print(shape_test.check_for_punisher('https://the-internet.herokuapp.com/img/avatars/Original-Facebook-Geek-Profile-Avatar-3.jpg'))
