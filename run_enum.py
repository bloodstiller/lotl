#!/usr/bin/env python3
from config import Config
from utils.logging import setup_logger
from modules import katana, nikto, nmap, nuclei, waymore, whatweb, wpscan 

def main():
    cfg = Config.from_args()
    log = setup_logger(cfg)

    log.info("Starting enumeration")
    log.info(f"Target: {cfg.target_url}")

    #check_dependencies(log)

    nmap.run(cfg, log)
    #nikto.run(cfg, log)

    #tech = whatweb.run(cfg, log)
#
   # if "wordpress" in tech:
   #     wpscan.run(cfg, log)
 
   #katana.run(cfg, log)    
   # nuclei.run(cfg, log)
   # waymore.run(cfg, log)
    

    log.info("Enumeration completed")

if __name__ == "__main__":
    main()
