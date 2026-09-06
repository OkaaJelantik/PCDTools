{ pkgs, lib, config, inputs, ... }:
{
  languages.python = {
    enable = true;
    package = pkgs.python3.withPackages (ps: [
      ps.numpy
      ps.matplotlib
      ps.opencv4
      ps.pillow
      ps.seaborn
      ps.pandas
      ps.jupyterlab
      ps.ipykernel
      ps.ipywidgets
      ps.ipympl
    ]);
    venv.enable = true;
  };
  packages = with pkgs; [
    stdenv.cc.cc.lib
    pkg-config
  ];
  processes.jupyter.exec = "jupyter lab";
  env.LD_LIBRARY_PATH = "${pkgs.stdenv.cc.cc.lib}/lib";
  enterShell = ''
    echo "✅ Env Ready!"
  '';
}
