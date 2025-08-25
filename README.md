# Resume Generator

The source code for generating my resume.

## Setup

### System Dependencies

On Debian

```bash
sudo apt update && sudo apt install -y pandoc texlive-latex-extra
```

### Python

1. Install UV

```bash
curl https://astral.sh/uv/install.sh | sh
```

2. Install python version

```bash
uv python install 3.11
uv python pin 3.11
```

3. Install dependencies

```bash
uv sync
```

### Build

The resume can be built using the provided makefile.

```bash
make build
```
