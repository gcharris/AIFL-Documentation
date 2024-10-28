{pkgs}: {
  deps = [
    pkgs.python312
    pkgs.python312Packages.mkdocs
    pkgs.python312Packages.mkdocs-material
    pkgs.python312Packages.pymdown-extensions
    pkgs.python312Packages.mkdocstrings
  ];
}