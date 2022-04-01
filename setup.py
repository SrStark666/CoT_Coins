from cx_Freeze import setup, Executable

#instalação de dependências
dependencies_instalation = {"packages": ["requests"], "includes": ["colorama"], "includes": ["time"], "includes": ["os"]}

# Apenas para programas com interface gráfica
"""base = None
if sys.platform == "win32":
    base = "Win32GUI"
"""

setup(
    name = "Cotação Moedas",
    version = "0.1",
    description = "Programa feito para exercício",
    options = {"build_exe": dependencies_instalation},
    executables = [Executable("CoT.py")]
)