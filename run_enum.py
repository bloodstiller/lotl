#!/usr/bin/env python3
from config import Config
from utils.logging import setup_logger
from modules import katana, nikto, nmap, nuclei, waymore, whatweb, wpscan 

def main():
    configs = Config.from_args()  # Returns a list of one or more configs
    
    total_targets = len(configs)
    print(f"\n{'='*60}")
    print(f"Starting enumeration job with {total_targets} target(s)")
    print(f"{'='*60}\n")
    
    for idx, cfg in enumerate(configs, 1):
        log = setup_logger(cfg)
        
        print(f"\n{'='*60}")
        print(f"Target {idx}/{total_targets}: {cfg.domain}")
        print(f"{'='*60}\n")
        
        log.info(f"Starting enumeration ({idx}/{total_targets})")
        log.info(f"Target: {cfg.target_url}")
        
        if cfg.proxy:
            log.info(f"Using proxy: {cfg.proxy}")
        
        # Check dependencies (uncomment when implemented)
        # check_dependencies(log)
        
        # Run all enumeration modules
        nmap.run(cfg, log)
        nikto.run(cfg, log)
        
        tech = whatweb.run(cfg, log)
        
        # Conditional module based on detected technology
        if "wordpress" in tech:
            wpscan.run(cfg, log)
        
        katana.run(cfg, log)    
        nuclei.run(cfg, log)
        waymore.run(cfg, log)
        
        log.info(f"Enumeration completed for {cfg.domain}")
    
    print(f"\n{'='*60}")
    print(f"All targets completed! Results in: scans/")
    print(f"{'='*60}\n")

if __name__ == "__main__":
    main()
