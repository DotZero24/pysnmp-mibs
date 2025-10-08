#
# PySNMP MIB module MSFT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/microsoft/MSFT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:17:00 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
microsoft = MibIdentifier((1, 3, 6, 1, 4, 1, 311))
software = MibIdentifier((1, 3, 6, 1, 4, 1, 311, 1))
systems = MibIdentifier((1, 3, 6, 1, 4, 1, 311, 1, 1))
os = MibIdentifier((1, 3, 6, 1, 4, 1, 311, 1, 1, 3))
windowsNT = MibIdentifier((1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1))
windows = MibIdentifier((1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 2))
workstation = MibIdentifier((1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1))
server = MibIdentifier((1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 2))
dc = MibIdentifier((1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 3))
mibBuilder.exportSymbols("MSFT-MIB", server=server, software=software, systems=systems, os=os, windowsNT=windowsNT, workstation=workstation, microsoft=microsoft, dc=dc, windows=windows)
