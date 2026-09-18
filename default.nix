

with import <nixpkgs> { };

pkgs.mkShell {
  name = "impurePythonEnv";
  buildInputs = [
    # Python interpreter and the uv package manager. uv creates and manages
    # its own virtual environment in ./.venv (see .python-version and
    # pyproject.toml for the pinned interpreter and dependencies).
    python3
    uv

    # In order to compile binary extensions (e.g. psycopg2, Pillow), the
    # Python dependencies need the following packages installed locally:
    taglib
    openssl
    git
    libxml2
    libxslt
    libzip
    zlib
    postgresql_17
  ];

  shellHook = ''
    unset SOURCE_DATE_EPOCH
    uv sync
    source .venv/bin/activate
  '';
}
