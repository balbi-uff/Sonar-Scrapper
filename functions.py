from bs4 import BeautifulSoup
import requests

def get_soup_from_file(filename):
    """
    Get the soup from the file
    """
    try:
        with open(filename, 'r', encoding="utf-8") as file:
            soup = BeautifulSoup(file, 'html.parser')
            return soup
    except Exception as e:
        print(e)
        return None

def get_discrepancy_list(soup):
    """
    Get the data from the soup
    """
    discrepancy_dict = {}
    try:
        discrepancy_list = soup.find_all('div', {'class': 'issues-workspace-list-item'})
        actual_file = discrepancy_list[0].find('div', {'class': 'component-name text-ellipsis'}).text
        c = 0
        for discrepancy in discrepancy_list:
            try:
                actual_file = discrepancy.find('div', {'class': 'component-name text-ellipsis'}).text
                discrepancy_dict[actual_file] = {}
                c = 0
            except AttributeError:
                pass
            finally:
                discrepancy_dict[actual_file][c] = discrepancy.find('span', {'title': 'Line Number'}).text
                c += 1
        return discrepancy_dict
    except Exception as e:
        print(e)
        return None

def print_dict(dict):
    """
    Print the discrepancies
    """
    for key, value in dict.items():
        print(key)
        for _, subvalue in value.items():
            print("\t" + subvalue[1:])
    return None


def print_discrepancies(filename):
    """
    Print the discrepancies
    """
    soup = get_soup_from_file(filename)
    discrepancy_dictionary = get_discrepancy_list(soup)
    print_dict(discrepancy_dictionary)
    return None

def write_discrepancies(filename):
    """
    Write the discrepancies to a file
    """
    soup = get_soup_from_file(filename)
    discrepancy_dictionary = get_discrepancy_list(soup)
    with open('discrepancies2.txt', 'w') as file:
        for key, value in discrepancy_dictionary.items():
            file.write(key)
            for _, subvalue in value.items():
                file.write("\n")
                file.write("\t" + subvalue[1:])
            file.write("\n")
    return None

