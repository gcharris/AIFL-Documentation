{pkgs}: {
  deps = [
    pkgs.fltk14
    pkgs.libffi
    pkgs.bash
    pkgs.python39Packages.flask
    pkgs.openssh
    pkgs.rustc
    pkgs.pkg-config
    pkgs.openssl
    pkgs.libxcrypt
    pkgs.libiconv
    pkgs.cargo
  ];
}
