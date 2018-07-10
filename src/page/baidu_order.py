import requests
from conftest import baidu_url
class Baidu_Order():
    def baidu_order(self):
        post_paramer={"body":{"source":"65429","shop":{"id":"40288a475a6394ff015a64b2d3680003","name":"测试店铺_解忧杂货","baidu_shop_id":"1922769788"},"order":{"order_id":"15103068902971","order_index":"1","send_immediately":1,"send_time":"1","send_fee":500,"package_fee":1400,"discount_fee":0,"total_fee":3510,"shop_fee":3058,"user_fee":3510,"commission":452,"pay_type":2,"pay_status":2,"need_invoice":1,"invoice_title":"优粮科技公司","remark":"不吃醋,不吃辣","delivery_party":2,"create_time":"1510306890"},"user":{"name":"haha","phone":"18210532386","gender":2,"address":"九台庄园 1234","coord":{"longitude":116.396917,"latitude":40.082207}},"products":[{"product_id":"0602892","upc":"","product_name":"8元水果切","product_price":800,"product_amount":2,"product_fee":1600,"package_price":100,"package_amount":"1","package_fee":200,"total_fee":1800,"product_custom_index":"2149209576_0_0"},{"product_id":"1700015","upc":"","product_name":"卤土豆片","product_price":10,"product_amount":1,"product_fee":10,"package_price":100,"package_amount":"12","package_fee":1200,"total_fee":1210,"product_custom_index":"2148560619_0_0"}],"discount":[]},"cmd":"order.create","sign":"CFE0B3A7FC8C39A1DA1138ACC8494ED2","source":"65429","ticket":"F728BA63-A238-9659-04D0-D668D692C473","timestamp":1510306984,"version":"2"}
        r=requests.post(baidu_url,json=post_paramer)
        #如果返回40*或者50*，抛出异常；如果是返回200，则raise_for_status()并不会抛出异常。
        r.raise_for_status()
        #因为要用返回值里的内容做断言，所以返回response即可，然后用例里assert "error" in r.baidu_order()
        # 如果拿response封装为一个方法，那么又会执行一次发送请求，会执行两次发送请求
        return r.text


# r=Baidu_Order()
# r.baidu_order()