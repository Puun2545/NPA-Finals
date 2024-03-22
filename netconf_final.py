from ncclient import manager
import xmltodict

m = manager.connect(
    host="10.0.15.189",
    port=830,
    username="admin",
    password="cisco",
    hostkey_verify=False
    )

def create():
    netconf_config = """
    <config>
        <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
            <interface>
                <name>Loopback64070184</name>
                <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:softwareLoopback</type>
                <enabled>true</enabled>
                <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                    <address>
                        <ip>172.30.184.1</ip>
                        <netmask>255.255.255.0</netmask>
                    </address>
                </ipv4>
            </interface>
        </interfaces>
    </config>
    """

    try:
        netconf_reply = netconf_edit_config(netconf_config)
        xml_data = netconf_reply.xml
        print(xml_data)
        if '<ok/>' in xml_data:
            return "Interface loopback 64070184 is created successfully"
    except:
        print("Error!")
        return "Cannot create: Interface loopback 64070184"


def delete():
    netconf_config = """
    <config>
        <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
            <interface operation="delete">
                <name>Loopback64070184</name>
            </interface>
        </interfaces>
    </config> 
    """

    try:
        netconf_reply = netconf_edit_config(netconf_config)
        xml_data = netconf_reply.xml
        print(xml_data)
        if '<ok/>' in xml_data:
            return "Interface loopback 64070184 is deleted successfully"
    except:
        print("Error!")
        return "Cannot delete: Interface loopback 64070184"


def enable():
    netconf_config = """
    <config>
        <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
            <interface>
                <name>Loopback64070184</name>
                <enabled>true</enabled>
            </interface>
        </interfaces>
    </config>
    """

    try:
        netconf_reply = netconf_edit_config(netconf_config)
        xml_data = netconf_reply.xml
        print(xml_data)
        if '<ok/>' in xml_data:
            return "Interface loopback 64070184 is enabled"
    except:
        print("Error!")
        return "Cannot enable: Interface loopback 64070184"


def disable():
    netconf_config = """
    <config>
        <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
            <interface>
                <name>Loopback64070184</name>
                <enabled>false</enabled>
            </interface>
        </interfaces>
    </config>
    """

    try:
        netconf_reply = netconf_edit_config(netconf_config)
        xml_data = netconf_reply.xml
        print(xml_data)
        if '<ok/>' in xml_data:
            return "Interface loopback 64070184 is disabled"
    except:
        print("Error!")
        return "Cannot disable: Interface loopback 64070184"

def netconf_edit_config(netconf_config):
    return  m.edit_config(target='running', config=netconf_config)


def status():
    netconf_filter = """
    <filter>
        <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
            <interface>
                <name>Loopback64070184</name>
            </interface>
        </interfaces-state>
    </filter>
    """

    try:
        # Use Netconf operational operation to get interfaces-state information
        netconf_reply = m.get(filter=netconf_filter)
        print(netconf_reply)
        netconf_reply_dict = xmltodict.parse(netconf_reply.xml)

        # if there data return from netconf_reply_dict is not null, the operation-state of interface loopback is returned
        if netconf_reply_dict['rpc-reply']['data'] is not None:
            # extract admin_status and oper_status from netconf_reply_dict
            admin_status = 'up' if netconf_reply_dict['rpc-reply']['data']['interfaces-state']['interface']['admin-status'] else 'down'
            oper_status = 'up' if netconf_reply_dict['rpc-reply']['data']['interfaces-state']['interface']['oper-status'] else 'down'
            if admin_status == 'up' and oper_status == 'up':
                return "Interface loopback 64070184 is enabled"
            elif admin_status == 'down' and oper_status == 'down':
                return "Interface loopback 64070184 is disabled"
        else: # no operation-state data
            return "No Interface loopback 64070184"
    except:
       print("Error!")


# test the functions
# print(create())
# print(disable())
# print(disable())
# print(enable())
# print(enable())
# print(status())
# print(disable())
# print(status())
# print(delete())
