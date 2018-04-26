import http.client, urllib.request, urllib.parse, urllib.error, base64, json

def runner(address):
    subscription_key = '2b1942bdbed34148934ee58f46be1121'
    uri_base = 'api.cognitive.azure.cn/vision/v1.0'
    headers = {
        # Request headers.
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': subscription_key,
    }
    params = urllib.parse.urlencode({
        # Request parameters. All of them are optional.
        'visualFeatures': 'Categories,Description,Color',
        'language': 'en',
    })
    # Replace the three dots below with the URL of a JPEG image of a celebrity.
    #body = "{'url':'https://upload.wikimedia.org/wikipedia/commons/1/12/Broadway_and_Times_Square_by_night.jpg'}"
    body = {'url':address}
    body=str(body)
    try:
        # Execute the REST API call and get the response.
        conn = http.client.HTTPSConnection('api.cognitive.azure.cn')
        conn.request("POST", "/vision/v1.0/analyze?%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read().decode('utf-8')
        # 'data' contains the JSON data. The following formats the JSON data for display.
        parsed = json.loads(data)
        print("Response:")
        print(json.dumps(parsed, sort_keys=True, indent=2))
        conn.close()
        return str(json.dumps(parsed, sort_keys=True, indent=2))

    except Exception as e:
        print('Error:')
        print(e)

if __name__ == '__main__':
    runner()