import requests
from conftest import elm_url
class Elm_Order():
    def elm_order(self):
        post_paramer ={"requestId":"200015698900989850","type":10,"appId":58137347,"message":"{\"id\":\"3024215297464790246\",\"orderId\":\"3024215297464790246\",\"address\":\"南京总医院南京总医院 住院部9楼7床\",\"createdAt\":\"2018-06-05T06:09:10\",\"activeAt\":\"2018-06-05T06:09:10\",\"deliverFee\":7.88,\"deliverTime\":\"2018-06-05T11:00:00\",\"description\":\"\",\"groups\":[{\"name\":\"1号篮子\",\"type\":\"normal\",\"items\":[{\"id\":1270064924,\"skuId\":200000071746483098,\"name\":\"鸡蛋羹\",\"categoryId\":1,\"price\":7.0,\"quantity\":1,\"total\":7.0,\"additions\":[],\"newSpecs\":[],\"attributes\":[],\"extendCode\":\"\",\"barCode\":\"\",\"weight\":1.0,\"userPrice\":0.0,\"shopPrice\":0.0,\"vfoodId\":1265353105},{\"id\":1236985288,\"skuId\":200000037872935834,\"name\":\"小秘制红烧肉\",\"categoryId\":1,\"price\":18.0,\"quantity\":1,\"total\":18.0,\"additions\":[],\"newSpecs\":[],\"attributes\":[],\"extendCode\":\"0203216\",\"barCode\":\"\",\"weight\":1.0,\"userPrice\":0.0,\"shopPrice\":0.0,\"vfoodId\":1235735637}]},{\"name\":\"其它费用\",\"type\":\"extra\",\"items\":[{\"id\":-70000,\"skuId\":-1,\"name\":\"餐盒\",\"categoryId\":102,\"price\":2.0,\"quantity\":1,\"total\":2.0,\"additions\":[],\"newSpecs\":null,\"attributes\":null,\"extendCode\":\"\",\"barCode\":\"\",\"weight\":null,\"userPrice\":0.0,\"shopPrice\":0.0,\"vfoodId\":0}]}],\"invoice\":null,\"book\":true,\"onlinePaid\":true,\"railwayAddress\":null,\"phoneList\":[\"18210532386\"],\"shopId\":155821482,\"shopName\":\"应用_菜品_优粮测试店铺\",\"daySn\":1,\"status\":\"unprocessed\",\"refundStatus\":\"noRefund\",\"userId\":261336699,\"totalPrice\":18.88,\"originalPrice\":34.88,\"consignee\":\"汤(先生)\",\"deliveryGeo\":\"118.80913312,32.04167602\",\"deliveryPoiAddress\":\"南京总医院南京总医院 住院部9楼7床\",\"invoiced\":false,\"income\":10.5,\"serviceRate\":0.15,\"serviceFee\":-3.5,\"hongbao\":0.0,\"packageFee\":2.0,\"activityTotal\":-16.0,\"shopPart\":-12.0,\"elemePart\":-4.0,\"downgraded\":false,\"vipDeliveryFeeDiscount\":0.0,\"openId\":\"8ab334455d2fbb43015d34e4c8ed1fd8\",\"secretPhoneExpireTime\":null,\"orderActivities\":[{\"categoryId\":12,\"name\":\"在线支付立减优惠\",\"amount\":-9.0,\"elemePart\":0.0,\"restaurantPart\":-9.0,\"familyPart\":0.0,\"id\":1128375833,\"orderAllPartiesPartList\":[{\"partName\":\"商家补贴\",\"partAmount\":\"9.0\"}]},{\"categoryId\":15,\"name\":\"商家代金券抵扣\",\"amount\":-7.0,\"elemePart\":-4.0,\"restaurantPart\":-3.0,\"familyPart\":0.0,\"id\":400000739464181997,\"orderAllPartiesPartList\":[]}],\"invoiceType\":null,\"taxpayerId\":\"\",\"coldBoxFee\":0.0,\"cancelOrderDescription\":null,\"cancelOrderCreatedAt\":null,\"orderCommissions\":[]}","shopId":156870405,"timestamp":1528150151480,"signature":"425D4E2950F57DD7BB3A5D86375C5467","userId":249698004053764774}
        r=requests.post(elm_url,json=post_paramer)
        # 如果返回40*或者50*，抛出异常；如果是返回200，则raise_for_status()并不会抛出异常。
        r.raise_for_status()
        # 因为要用返回值里的内容做断言，所以返回response即可，然后用例里assert "error" in r.elm_order()
        # 如果拿response封装为一个方法，那么又会执行一次发送请求，会执行两次发送请求
        return r.text

r=Elm_Order()
r.elm_order()








