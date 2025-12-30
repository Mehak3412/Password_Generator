import random
import string
import argparse
import sys


class password_generator:

    def __init__(self):
        self.lowercase=string.ascii_lowercase
        self.uppercase=string.ascii_uppercase
        self.digits=string.digits
        self.symbols=string.punctuation

    def generate(self, length=12, use_uppercase=True, use_digits=True, use_symbols=True, exclude_similar=False):

        if length < 4:
            raise ValueError("Password length should be at least 4 characters.")
        
        char_pool=self.lowercase

        if use_uppercase:
            char_pool+=self.uppercase
        if use_digits:
            char_pool+=self.digits
        if use_symbols:
            char_pool+=self.symbols

        if exclude_similar:
            similar_chars='il1Lo0O'
            char_pool=''.join(c for c in char_pool if c not in similar_chars)

        password=[]
        if use_uppercase:
            password.append(random.choice(self.uppercase))  
        if use_digits:
            password.append(random.choice(self.digits))
        if use_symbols:
            password.append(random.choice(self.symbols))
        password.append(random.choice(self.lowercase))


        remaining_length=length-len(password)
        password.extend(random.choices(char_pool, k=remaining_length))


        random.shuffle(password)
        return ''.join(password)
    
    def generate_multiple(self, count=5, **kwargs):
        return [self.generate(**kwargs) for _ in range(count)]
    

def main():
    parser=argparse.ArgumentParser(description="Generate secure passwords.")
    parser.add_argument("--length", type=int, default=12, help="Length of the password")
    parser.add_argument("--count", type=int, default=5, help="Number of passwords to generate")
    parser.add_argument("--no-uppercase", action="store_true", help="Exclude uppercase letters")
    parser.add_argument("--no-digits", action="store_true", help="Exclude digits")
    parser.add_argument("--no-symbols", action="store_true", help="Exclude symbols")
    parser.add_argument("--exclude-similar", action="store_true", help="Exclude similar characters")

    args=parser.parse_args()

    generator=password_generator()
    
    if args.count == 1:
        print(generator.generate(
            length=args.length,
            use_uppercase=not args.no_uppercase,
            use_digits=not args.no_digits,
            use_symbols=not args.no_symbols,
            exclude_similar=args.exclude_similar
        ))
    else:
        for password in generator.generate_multiple(
            count=args.count,
            length=args.length,
            use_uppercase=not args.no_uppercase,
            use_digits=not args.no_digits,
            use_symbols=not args.no_symbols,
            exclude_similar=args.exclude_similar
        ):
            print(password)

if __name__ == "__main__":
    main()