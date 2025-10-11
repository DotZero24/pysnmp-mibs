import contextlib
from pathlib import Path

from pysmi.codegen import PySnmpCodeGen
from pysmi.compiler import MibCompiler
from pysmi.parser import SmiStarParser
from pysmi.reader import FileReader
from pysmi.searcher import PyFileSearcher, PyPackageSearcher, StubSearcher
from pysmi.writer import PyFileWriter
from pysmi.debug import set_logger, Debug

# set_logger(Debug('compiler', 'reader', 'lexer', 'parser', 'codegen', 'writer'))

inputMibs = []
baseDirectories = ["/usr/share/snmp/mibs", "./mibs"]
srcDirectories = ["/usr/share/snmp/mibs", "./mibs"]

dstDirectory = "./pysnmp_mibs"

for src in baseDirectories:
    for mibFile in Path(src).rglob("*MIB*"):
        if mibFile not in inputMibs:
            inputMibs.append(str(mibFile.name).replace(".txt", ""))
    for mibDir in Path(src).rglob("*/"):
        if mibDir not in srcDirectories:
            srcDirectories.append(str(mibDir))

# Initialize compiler infrastructure
mibCompiler = MibCompiler(SmiStarParser(), PySnmpCodeGen(), PyFileWriter(dstDirectory))

# search for source MIBs here
mibCompiler.add_sources(*[FileReader(x) for x in srcDirectories])

# check compiled MIBs in our own productions
mibCompiler.add_searchers(PyFileSearcher(dstDirectory))
# ...and at default PySNMP MIBs packages
mibCompiler.add_searchers(*[PyPackageSearcher(x) for x in PySnmpCodeGen.defaultMibPackages])

# never recompile MIBs with MACROs
mibCompiler.add_searchers(StubSearcher(*PySnmpCodeGen.baseMibs))

# run [possibly recursive] MIB compilation
for i, inputMib in enumerate(inputMibs):
    try:
        with contextlib.redirect_stdout(None):
            result = mibCompiler.compile(
                inputMib,
                rebuild=True,
            )
        not_done = {k: v for k, v in result.items() if v not in ("compiled", "untouched", "unprocessed")}
        if not_done:
            print(f"Compiled {inputMib}: {not_done}")
            print(f"Compiled {i} MIBs {100 * i / len(inputMibs):.2f}%", end="\r")

        print(f"Compiled {inputMib} {100 * i / len(inputMibs):.2f}%", end="                           \r")

    except Exception as e:
        print(f"Error: {e}")
        continue
