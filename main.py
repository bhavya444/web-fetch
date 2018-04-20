from domain import get_domain_name
from general import create_directory, write_file
from ip_address import get_ip_address
from nmap import get_nmap
from robots_txt import get_robots_txt
from whois import get_whois

ROOT_DIRS = 'websites'
create_directory(ROOT_DIRS)


def gather_info(name, url):
    
    domain_name = get_domain_name(url)
    ip_address = get_ip_address(domain_name)
    nmap = get_nmap('-F', ip_address)
    robots_txt = get_robots_txt(url)
    whois = get_whois(domain_name)
    print("Done\n")

    
    create_report(name, nmap, robots_txt, whois)
    print("Information for " + name + " saved in Websites/" + name + " Folder\n")


def create_report(name, nmap, robots_txt, whois):
    project_dir = ROOT_DIRS + '/' + name
    create_directory(project_dir)
    write_file(project_dir + '/nmap.txt', nmap)
    write_file(project_dir + '/robots-txt.txt', robots_txt)
    write_file(project_dir + '/whois.txt', whois)


print("Enter the name of project")
name = input()
print("\nEnter the full URL")
url = input()

gather_info(name, url)

