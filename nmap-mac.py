import nmap3
from prettytable import PrettyTable

def get_hostname(host_data):
    if isinstance(host_data, dict) and "hostname" in host_data:
        return host_data["hostname"][0]["name"]
    return "Unknown"

def get_mac_address(mac_data):
    if isinstance(mac_data, list) and len(mac_data) > 0:
        mac_info = mac_data[0]
        if "addr" in mac_info:
            return mac_info["addr"]
    return "Unknown"

def scan_network(target):
    nmap = nmap3.Nmap()
    results = nmap.scan_top_ports(target)
    host_list = []
    for host, host_data in results.items():
        if host != "runtime" and host != "stats" and host != "task_results":
            hostname = get_hostname(host_data)
            mac_address = get_mac_address(host_data.get("addresses", {}).get("mac", []))
            host_list.append((host, hostname, mac_address))

    table = PrettyTable(["IP Address", "Hostname", "MAC Address"])
    for host, hostname, mac_address in host_list:
        table.add_row([host, hostname, mac_address])

    print(table)

if __name__ == "__main__":
    target = input("Enter the target IP range or hostnames to scan: ")
    scan_network(target)
