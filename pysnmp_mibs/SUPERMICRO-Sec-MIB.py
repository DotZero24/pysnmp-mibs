#
# PySNMP MIB module SUPERMICRO-Sec-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/supermicro/SUPERMICRO-Sec-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:57:43 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
fsSec = ModuleIdentity((1, 3, 6, 1, 4, 1, 10876, 101, 2, 64))
fsSec.setRevisions(('2012-09-05 00:00',))
if mibBuilder.loadTexts: fsSec.setLastUpdated('201209050000Z')
if mibBuilder.loadTexts: fsSec.setOrganization('Super Micro Computer Inc.')
fsSecSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 10876, 101, 2, 64, 1))
fsSecDebugOption = MibScalar((1, 3, 6, 1, 4, 1, 10876, 101, 2, 64, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsSecDebugOption.setStatus('current')
mibBuilder.exportSymbols("SUPERMICRO-Sec-MIB", fsSecDebugOption=fsSecDebugOption, PYSNMP_MODULE_ID=fsSec, fsSecSystem=fsSecSystem, fsSec=fsSec)
