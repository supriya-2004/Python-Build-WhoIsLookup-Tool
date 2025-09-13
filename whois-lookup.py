import argparse
import sys
import whois

#Performs a WHOIS lookup and returns the registrar name.
def get_registrar(domain):

    try:
        w = whois.whois(domain)
        registrar = w.registrar
        if isinstance(registrar, list):
            return registrar[0]
        return registrar
    except Exception as e:
        return f"Error: {e}"

#Main function to parse command-line arguments and perform lookups.
def main():

    parser = argparse.ArgumentParser(
        description="Perform WHOIS lookups for domains.",
        epilog="Example: python whois_lookup.py google.com wikipedia.org"
    )
    
    # Optional argument to read domains from a file
    parser.add_argument(
        '-f', '--file',
        type=str,
        help="Path to a file containing a list of domains, one per line."
    )
    
    # Positional argument for domains on the command line
    parser.add_argument(
        'domains',
        nargs='*', # Allows zero or more arguments
        help="Space-separated list of domains to look up."
    )

    args = parser.parse_args()
    all_domains = []

    # Case 1: Read domains from a file
    if args.file:
        try:
            with open(args.file, 'r') as f:
                all_domains.extend([line.strip() for line in f if line.strip()])
        except FileNotFoundError:
            print(f"Error: The file '{args.file}' was not found.")
            sys.exit(1)
    
    # Case 2: Read domains from the command line
    if args.domains:
        all_domains.extend(args.domains)

    # If no domains were provided at all, print usage and exit
    if not all_domains:
        parser.print_help()
        sys.exit(1)

    print("--- WHOIS Registrar Lookup ---")
    for domain in all_domains:
        registrar_name = get_registrar(domain)
        print(f"Domain: {domain} -> Registrar: {registrar_name}")
    print("--- Lookup Complete ---")

if __name__ == "__main__":
    main()