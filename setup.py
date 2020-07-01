import cx_Freeze

executables = [cx_Freeze.Executable(script="jogo.py", icon = "assets/alfabetoIcon.ico")]
cx_Freeze.setup(
    name = "Caça Alfabeto",
    options = {"build_exe":{"packages":["pygame"]
    , "include_files": ["assets"] 
    }},
    executables = executables 
)