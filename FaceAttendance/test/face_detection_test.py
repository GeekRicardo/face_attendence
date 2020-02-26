from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException 
from tencentcloud.iai.v20180301 import iai_client, models 
try: 
    cred = credential.Credential("AKIDJURAfzrvcTBeroQ0EC0e3DBuRikbHTSC", "e5GB1g5E8mCMG3cv0pPlrjT7YkmZ9U25") 
    httpProfile = HttpProfile()
    httpProfile.endpoint = "iai.tencentcloudapi.com"

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = iai_client.IaiClient(cred, "ap-guangzhou", clientProfile) 

    req = models.DetectFaceRequest()
    params = '{"Url":"https://wechat.sshug.cn:21243/static/face_imgs/face_detect/tmp.jpg"}'
    req.from_json_string(params)

    resp = client.DetectFace(req) 
    print(resp.to_json_string()) 

except TencentCloudSDKException as err: 
    print(err)