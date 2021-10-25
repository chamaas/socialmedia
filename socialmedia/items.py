import scrapy


class LivreItem(scrapy.Item):
    # define the fields for your item here like:
     author = scrapy.Field()
     rate=scrapy.Field()
     reviews_number=scrapy.Field()
     summary=scrapy.Field()



class Posts_Insta_Item(scrapy.Item):
    post_link=scrapy.Field()
    comments=scrapy.Field()
    Likes=scrapy.Field()
    date_pub=scrapy.Field()
    titre=scrapy.Field()
    nom_hash=scrapy.Field()
    nombre_posts_hash=scrapy.Field()
    url=scrapy.Field()
    description=scrapy.Field()
    related_post=scrapy.Field()
    compte=scrapy.Field()
    date_debut=scrapy.Field()
    date_fin=scrapy.Field
class Insta_Item_Semaine(scrapy.Item):
    hash=scrapy.Field()
    nb_posts=scrapy.Field()
    Query=scrapy.Field()
  