from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
class ShapeTest:
    def __init__(self,url):
        self.url = url
        self.browser = self.setup()
        self.content = self.browser.find_element_by_xpath('//*[@id="content"]/div/div').text
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
        images = self.browser.find_elements_by_tag_name('img')
        for image in images:
            image_links.append(image.get_attribute("src"))
        return self.image_links

    def check_for_punisher(self,punisher):
        if punisher in self.image_links:
            return True
        return False

    def print_all_image_names(self):
        for img in self.image_links:
            pass




    def rand_name(self):
        name = ' '.join([name_words[random.randint(0, len(name_words))] for i in range(2)])
        return name

if __name__ == '__main__':
    url = "https://the-internet.herokuapp.com/dynamic_content"
    shape_test = ShapeTest(url)
    print(shape_test.content)

    # checks if longest word is greater than 10 characters
    print(shape_test.is_atleast(10))

    #prints longest word
    print(shape_test.find_longest_word(shape_test.content))

    #checks for punisher image in the content and prints image names
    print(shape_test.check_for_punisher('https://the-internet.herokuapp.com/img/avatars/Original-Facebook-Geek-Profile-Avatar-3.jpg'))
