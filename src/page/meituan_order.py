import requests
from conftest import meituan_url
class Meituan_Order():
    def meituan_order(self):
        post_paramer=dict(app_poi_code="test_poi_01",
            caution="多来几袋番茄酱 多来几袋番茄酱，谢谢 其中两个多放尖椒，谢谢",
            city_id="999999",
            ctime="1528700400",
            day_seq="1",
            delivery_time="0",
            detail="\"[{\"app_food_code\":\"1534343\",\"box_num\":1,\"box_price\":0,\"food_discount\":1,\"food_name\":\"FS1\",\"food_property\":\"热,特辣\",\"price\":3,\"quantity\":1,\"sku_id\":\"1534343\",\"spec\":\"大份\",\"unit\":\"份\"},{\"app_food_code\":\"1534343\",\"box_num\":10,\"box_price\":0,\"food_discount\":1,\"food_name\":\"FS1\",\"food_property\":\"热,特辣\",\"price\":1,\"quantity\":5,\"sku_id\":\"1534343\",\"spec\":\"小份\",\"unit\":\"份\"}]\"",
            wm_order_id_view="24581032571314888",
            wm_poi_name="t_13qCOLH5",
            wm_poi_address="南极洲04号站",
            wm_poi_phone="4009208801",
            recipient_address="色金拉 (1234)",
            recipient_phone="18210532386",
            recipient_name="张(先生)",
            shipping_fee="0.01",
            total="8.01",
            original_price="8.01",
            shipper_phone="\"\"",
            status="2",
            has_invoiced="0",
            invoice_title="\"\"",
            utime="1509337095",is_third_shipping="0",pay_type="2",latitude="29.774492",longitude="95.36927",
            extras="[]",taxpayer_id="",order_id="6810571663",avg_send_time="2400.0")
        r=requests.post(meituan_url,data=post_paramer)
        #如果返回40*或者50*，抛出异常；如果是返回200，则raise_for_status()并不会抛出异常。
        r.raise_for_status()
        #print(r.text)
        # 因为要用返回值里的内容做断言，所以返回response即可，然后用例里assert "error" in r.meituan_order()
        # 如果拿response封装为一个方法，那么又会执行一次发送请求，会执行两次发送请求
        return r.text

# r=Meituan_Order()
# r.meituan_order()