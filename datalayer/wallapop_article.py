class WallapopArticle:
    def __init__(self, id, title, description, price, currency, location, allows_shipping, url):
        self._id = id
        self._title = title
        self._description = description
        self._price = price
        self._currency = currency
        self._location = location
        self._allows_shipping = allows_shipping
        self._url = url

    @classmethod
    def load_from_json(cls, json_data):
        return cls(
            json_data.get('id', ''),
            json_data.get('title', ''),
            json_data.get('description', ''),
            json_data.get('price', {}).get('amount', 0),
            json_data.get('price', {}).get('currency', 'EUR'),
            json_data.get('location', {}).get('city', 'Desconocida'),
            json_data.get('shipping', {}).get('user_allows_shipping', False),
            json_data.get('web_slug', '')
        )

    def get_id(self):
        return self._id

    def get_title(self):
        return self._title

    def get_description(self):
        return self._description

    def get_price(self):
        return self._price

    def get_currency(self):
        return self._currency

    def get_location(self):
        return self._location

    def get_allows_shipping(self):
        return self._allows_shipping

    def get_url(self):
        return self._url

    def __eq__(self, article):
        return self.get_id() == article.get_id()

    def __str__(self):
        return f"Article(id={self._id}, title='{self._title}', " \
               f"price={self._price} {self._currency}, url='{self._url}')"
