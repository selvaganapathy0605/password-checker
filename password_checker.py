import requests #it allows make a request to get data
import hashlib
import sys

def api(passcode):
    url="https://api.pwnedpasswords.com/range/"+ passcode
    r=requests.get(url)
    if r.status_code !=200:
        raise RuntimeError(f'Error:{r.status_code}.Try again!')
    return r

def password_leaks_count(hashes,hash_count):
    hashes=(lines.split(":") for lines in hashes.text.splitlines())
    for h,count in hashes:
        if h==hash_count:
            return count
    return 0

def check(password):
    sha1password=hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first_5char=sha1password[:5]
    tail=sha1password[5:]
    res=api(first_5char)
    return password_leaks_count(res,tail)

def main(args):
    for password in args:
        count=check(password)
        if count:
            print(f'{password} was found {count} times.Try new password')
        else:
            print(f'{password} was good.Carry on!')
    return 'Done' 
if __name__=='__main__':
    sys.exit(main(sys.argv[1:]))