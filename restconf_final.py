import json
import requests
requests.packages.urllib3.disable_warnings()

# Router IP Address is 10.0.15.189
api_url = "https://10.0.15.189/restconf/data/ietf-interfaces:interfaces/interface=Loopback64070184"

# the RESTCONF HTTP headers, including the Accept and Content-Type
# Two YANG data formats (JSON and XML) work with RESTCONF 
headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json",
}
basicauth = ("admin", "cisco")


def create():
    yangConfig = {
        "ietf-interfaces:interface": {
            "name": "Loopback64070184",
            "description": "Added by RESTCONF",
            "type": "iana-if-type:softwareLoopback",
            "enabled": True,
            "ietf-ip:ipv4": {
                "address": [
                    {
                        "ip": "172.30.184.1",
                        "netmask": "255.255.255.0"
                    }
                ]
            },
            "ietf-ip:ipv6": {}
        }
}

    resp = requests.put(
        api_url, 
        data=json.dumps(yangConfig), 
        auth=basicauth, 
        headers=headers, 
        verify=False
        )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        return "Interface loopback 64070184 is created successfully"
    else:
        print('Error. Status Code: {}'.format(resp.status_code))


def delete():
    resp = requests.delete(
        api_url, 
        auth=basicauth, 
        headers=headers, 
        verify=False
        )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        return "Interface loopback 64070184 is deleted successfully"
    else:
        print('Error. Status Code: {}'.format(resp.status_code))


def enable():
    yangConfig = {
        "ietf-interfaces:interface": {
            "name": "Loopback64070184",
            "enabled": True
        }
    }

    resp = requests.put(
        api_url, 
        data=json.dumps(yangConfig), 
        auth=basicauth, 
        headers=headers, 
        verify=False
        )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        return "Interface loopback 64070184 is enabled successfully"
    else:
        print('Error. Status Code: {}'.format(resp.status_code))
        return "Cannot enable: Interface loopback 64070184"


def disable():
    yangConfig = {
        "ietf-interfaces:interface": {
            "name": "Loopback64070184",
            "enabled": False
        }
    }

    resp = requests.put(
        api_url, 
        data=json.dumps(yangConfig), 
        auth=basicauth, 
        headers=headers, 
        verify=False
        )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        return "Interface loopback 64070184 is shutdowned successfully"
    else:
        print('Error. Status Code: {}'.format(resp.status_code))


def status():
    api_url_status = "<!!!REPLACEME with URL of RESTCONF Operational API!!!>"

    resp = requests.<!!!REPLACEME with the proper HTTP Method!!!>(
        <!!!REPLACEME with URL!!!>, 
        auth=basicauth, 
        headers=<!!!REPLACEME with HTTP Header!!!>, 
        verify=False
        )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        response_json = resp.json()
        admin_status = <!!!REPLACEME!!!>
        oper_status = <!!!REPLACEME!!!>
        if admin_status == 'up' and oper_status == 'up':
            return "<!!!REPLACEME with proper message!!!>"
        elif admin_status == 'down' and oper_status == 'down':
            return "<!!!REPLACEME with proper message!!!>"
    elif(resp.status_code == 404):
        print("STATUS NOT FOUND: {}".format(resp.status_code))
        return "<!!!REPLACEME with proper message!!!>"
    else:
        print('Error. Status Code: {}'.format(resp.status_code))
