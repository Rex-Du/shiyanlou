class Redis:
    def __init__(self):
        self.cache = dict()

    def get(self, key):
        return self.cache.get(key)

    def set(self, key, value):
        self.cache[key] = value


redis = Redis()


class Image:
    def __init__(self, name):
        self.name = name

    @property
    def url(self):
        return 'http://www.rexdu.club'


class ImageProxy:
    def __init__(self, image):
        self.image = image

    @property
    def url(self):
        addr = redis.get(self.image.name)
        if addr:
            print("Set url in redis cache!")
            return addr
        else:
            print("Get url from redis cache!")
            redis.set(self.image.name, self.image.url)
            return self.image.url


class Page:
    def __init__(self, image):
        self.image = image

    def render(self):
        print(self.image.url)


image = Image('logo')
image_proxy = ImageProxy(image)
page = Page(image_proxy)

page.render()
print('==================')
page.render()
