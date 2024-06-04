## Acronym

This is a tiny terminal application used to help me memorise acronyms and their
phrases. It was also a chance to brush up on my programming, as it had been a
few months.

Acronym sets are created and configured using [YAML](https://yaml.org) — a
language that I found to be pretty ergonomic when creating my own GitHub issue
templates.

### Installation

1. Clone the repository:

```console
git clone https://github.com/elijahblackmore/acronym.git
```

2. Navigate to the directory cloned from this repository:

```console
cd acronym
```

3. Install the package using `pip`:

```console
pip install .
```

### Usage

Ensure that you have your `acronym.yaml` file located at
`~/.config/acronym/acronym.yaml` with the correct structure.

Here is an example that you can modify:

```yaml
sets:
  - title: "Networking"
    acronyms:
      DNS: "Domain Name Service"
      IMAP: "Internet Message Access Protocol"
      CIDR: "Classless Inter-Domain Routing"
  - title: "Shell scripting"
    acronyms:
      POSIX: "Portable Operating System Interface"
      GREP: "Global Regular Expression Print"
      CD: "Change Directory"
```

Run the application using the following command:

```console
acronym
```
