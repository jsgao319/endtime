from yunpian_python_sdk.model import constant as YC
from yunpian_python_sdk.ypclient import YunpianClient
# 初始化client,apikey作为所有请求的默认值
clnt = YunpianClient('1f72317602ff1631e5b889358d107603')
param = {YC.MOBILE:'17319366584',YC.TEXT:'您的验证码是12345'}
r = clnt.sms().single_send(param)
# 获取返回结果, 返回码:r.code(),返回码描述:r.msg(),API结果:r.data(),其他说明:r.detail(),调用异常:r.exception()
# 短信:clnt.sms() 账户:clnt.user() 签名:clnt.sign() 模版:clnt.tpl() 语音:clnt.voice() 流量:clnt.flow()