#!/usr/bin/env python3

import argparse
from pathlib import Path

class Config:
    def __init__(self, args):
        self.domain = args.domain
        self.subdomain = args.subdomain
        self.https = args.https
        self.job = args.job
        self.proxy = args.proxy
        
        # Create output directory with domain-specific subdirectory
        self.output = Path("scans") / self.job / self.domain

        proto = "https" if self.https else "http"
        host = f"{self.subdomain}.{self.domain}" if self.subdomain else self.domain
        self.target_url = f"{proto}://{host}"
        self.target_host = host

        self.output.mkdir(parents=True, exist_ok=True)

    @staticmethod
    def from_args():
        p = argparse.ArgumentParser(description="Modular Enumeration Framework")
        p.add_argument("-d", "--domain", help="Single domain/IP to scan")
        p.add_argument("-t", "--targets", help="File containing list of domains/IPs, one per line")
        p.add_argument("-s", "--subdomain", help="Subdomain to prepend to domain")
        p.add_argument("--http", dest="https", action="store_false", help="Use HTTP instead of HTTPS")
        p.add_argument("-j", "--job", required=True, help="Job name for organizing scans")
        p.add_argument("--proxy", help="Proxy URL (e.g., http://127.0.0.1:8080)")
        
        args = p.parse_args()
        
        # Validate that either domain or targets file is provided
        if not args.domain and not args.targets:
            p.error("Either --domain or --targets must be provided")
        
        if args.domain and args.targets:
            p.error("Cannot use both --domain and --targets, choose one")
        
        # If targets file provided, create a config for each target
        if args.targets:
            if not Path(args.targets).exists():
                p.error(f"Targets file not found: {args.targets}")
            
            configs = []
            with open(args.targets) as f:
                for line_num, line in enumerate(f, 1):
                    target = line.strip()
                    # Skip empty lines and comments
                    if target and not target.startswith('#'):
                        # Create a modified args object for this specific target
                        target_args = argparse.Namespace(**vars(args))
                        target_args.domain = target
                        target_args.subdomain = None  # Don't combine subdomain with targets file
                        try:
                            configs.append(Config(target_args))
                        except Exception as e:
                            print(f"Warning: Skipping invalid target on line {line_num}: {target} ({e})")
            
            if not configs:
                p.error(f"No valid targets found in {args.targets}")
            
            return configs
        else:
            # Single target mode
            return [Config(args)]
