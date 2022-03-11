import xml.etree.ElementTree as ET


def parse_nmaprun_xml(fname):
    xml_tree = ET.parse(fname)
    root = xml_tree.getroot()
    outports = []
    for child in root:
        for nmap_child in root.iter(child.tag):
            if nmap_child.tag == "host":
                for elem in nmap_child:
                    if elem.tag == "ports":
                        for ports in elem:
                            if ports.tag == "port":
                                for port in ports:
                                    port = {
                                        "port_id": ports.attrib["portid"],
                                        "protocol": ports.attrib["protocol"],
                                        "service_name": port.attrib["name"] if "name" in port.attrib else None}
                                outports.append(port)
    return outports
