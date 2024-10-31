{ pkgs }: {
  deps = [
    pkgs.dig
    pkgs.python39
    pkgs.python39Packages.mkdocs
  ];
}