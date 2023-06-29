let
  pkgs = import <nixpkgs> { };
  pname = "priceloop-api";
  vsextensions = (with pkgs.vscode-extensions; [
    ms-azuretools.vscode-docker
    ms-python.python
    ms-vsliveshare.vsliveshare
    redhat.vscode-yaml
    streetsidesoftware.code-spell-checker
    vscodevim.vim
    matangover.mypy
    charliermarsh.ruff
  ]) ++ pkgs.vscode-utils.extensionsFromVscodeMarketplace [
    {
      publisher = "42Crunch";
      name = "vscode-openapi";
      version = "4.18.4";
      sha256 = "sha256-lv4dUJDOFPemvS8YTD12/PjeTevWhR76Ex8qHjQH3vY=";
    }
    {
          publisher = "ms-python";
          name = "black-formatter";
          version = "2023.3.11731009";
          sha256 = "sha256-7Lgf5euGHeE5UqPzrJS1bTEBpNIpQE0rNRRi8r3wZ+o=";
    }
  ]; 
  vscode-nocode-plugins-ape = pkgs.vscode-with-extensions.override {
    vscodeExtensions = vsextensions;
  };
in
pkgs.mkShell rec {
  buildInputs = with pkgs; [
    git
    awscli2
    aws-vault

    ruff
    mypy
    black

    python311
    python311Packages.pip
    python311Packages.virtualenv
    python311Packages.numpy
    python311Packages.pandas

    vscode-nocode-plugins-ape

  ];

  shellHook = ''
    echo "--- Welcome to ${pname}! ---"
    echo "Run the following to setup your environment"
    echo "python -m venv .venv"
    echo "source .venv/bin/activate"
    echo "pip install -r requirements.txt"
  '';
}
