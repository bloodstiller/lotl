# Batch Enumeration Tool To Get A Good (L)ay (O)f (T)he (L)and. 

LOTL is a  Python-based modular framework for automated web application and network enumeration. Run multiple security scanning tools against single or multiple targets with centralized logging and optional proxy support.

## Features

- **Modular Design**: Each tool runs as a separate module
- **Multi-Target Support**: Scan single targets or bulk scan from a file
- **Proxy Support**: Route all traffic through Burp Suite or other proxies
- **Comprehensive Logging**: Detailed logs for each target with color-coded console output
- **Organized Output**: Results automatically organized by job name and target

## Required Tools

The following tools must be installed and available in your PATH:

- **nmap** - Network scanner
- **nikto** - Web server scanner
- **whatweb** - Web technology identifier
- **katana** - Web crawler
- **nuclei** - Vulnerability scanner
- **waymore** - Wayback machine URL fetcher
- **wpscan** - WordPress scanner (optional, requires API token)

### Installation Commands

```bash
# Ubuntu/Debian
sudo apt install nmap nikto

# Go-based tools (install Go first if needed)
go install github.com/projectdiscovery/katana/cmd/katana@latest
go install github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest

# Python tools
pip install waymore

# WhatWeb
git clone https://github.com/urbanadventurer/WhatWeb.git
cd WhatWeb
sudo make install

# WPScan (Ruby-based)
gem install wpscan
```

## Installation

```bash
git clone <repository-url>
cd enumeration-framework
pip install -r requirements.txt
```

## Usage

### Single Target

```bash
python3 run_enum.py -d example.com -j job_name
```

### Multiple Targets

Create a file with one domain/IP per line:

```
example.com
192.168.1.100
target3.com
# This is a comment and will be ignored
another-target.com
```

Then run:

```bash
python3 run_enum.py -t targets.txt -j job_name
```

### Additional Options

```bash
# Use HTTP instead of HTTPS
python3 run_enum.py -d example.com -j job_name --http

# Scan a subdomain
python3 run_enum.py -d example.com -s www -j job_name

# Use a proxy (Burp Suite)
python3 run_enum.py -d example.com -j job_name --proxy http://127.0.0.1:8080

# Combine options
python3 run_enum.py -t targets.txt -j bulk_scan --proxy http://127.0.0.1:8080
```

## Output Structure

Results are organized in the `scans/` directory:

```
scans/
└── job_name/
    ├── example.com/
    │   ├── nmap/
    │   │   ├── tcp.nmap
    │   │   ├── tcp.xml
    │   │   └── udp.nmap
    │   ├── nikto/
    │   │   └── nikto.txt
    │   ├── whatweb/
    │   │   └── tech.txt
    │   ├── katana/
    │   │   └── katana.txt
    │   ├── nuclei/
    │   │   └── nuclei.txt
    │   ├── waymore/
    │   │   └── waymoreURLS.txt
    │   ├── wpscan/
    │   │   └── wpscan.txt
    │   └── example.com.log
    └── target2.com/
        └── ...
```

## Configuration

### WPScan API Token

For WPScan to work with vulnerability detection, set your API token:

```bash
export WPSCAN_API_TOKEN="your-token-here"
```

Get a free token at: https://wpscan.com/

### Nuclei Templates

By default, nuclei looks for templates at `~/nuclei-templates/http`. To use a custom path:

```bash
export NUCLEI_TEMPLATES="/path/to/nuclei-templates"
```

## Modules

The framework runs the following tools in order:

1. **Nmap** - TCP and UDP port scanning with service detection
2. **Nikto** - Web vulnerability scanning
3. **WhatWeb** - Technology detection (triggers WPScan if WordPress detected)
4. **WPScan** - WordPress-specific scanning (conditional)
5. **Katana** - Web crawling to discover URLs
6. **Nuclei** - Vulnerability scanning with templates
7. **Waymore** - Historical URL discovery via Wayback Machine

## Logs

Each target generates its own detailed log file with timestamps and color-coded output:

- **Green [+]**: Informational messages
- **Yellow [!]**: Warnings
- **Red [-]**: Errors

Console output shows INFO level, while log files contain DEBUG level details including full command output.

## Contributing

To add a new module:

1. Create a new file in `modules/your_tool.py`
2. Implement a `run(cfg, log)` function
3. Import and call it in `run_enum.py`

Example module structure:

```python
#!/usr/bin/env python3
from utils.runner import run as run_command

def run(cfg, log):
    log.info("Running YourTool")
    out = cfg.output / "yourtool"
    out.mkdir(exist_ok=True)

    cmd = ["yourtool", "-target", cfg.target_url]
    
    if cfg.proxy:
        cmd.extend(["--proxy", cfg.proxy])
    
    run_command(cmd, log)
```

## Notes

- Nmap requires sudo/root privileges for certain scan types
- Some tools may take a long time to complete on large targets
- The framework runs tools sequentially (not in parallel)
- All commands are logged with full output for debugging


## TODO 
- [ ] Integrate multithreading/parallelism. 
- [ ] Create other modules. 
- [ ] Create option to parse nmap results to then trigger further scans e.g. if it finds ssh it will trigger all safe enumeration ssh scripts to run. 
- [ ] Integrate option to pipe waymore results into nuclei and run DAST. 
- [ ] Integrate webapp & infra switches so that a predefined set of tools run dependant on what type of test it is. 
- [ ] Trigger nuclei playbooks depending on test type.


