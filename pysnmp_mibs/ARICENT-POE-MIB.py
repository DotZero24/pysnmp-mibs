#
# PySNMP MIB module ARICENT-POE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/aricent/ARICENT-POE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:56:46 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
MacAddress, RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "RowStatus", "TextualConvention", "DisplayString")
fspoe = ModuleIdentity((1, 3, 6, 1, 4, 1, 2076, 103))
fspoe.setRevisions(('2012-09-05 00:00',))
if mibBuilder.loadTexts: fspoe.setLastUpdated('201209050000Z')
if mibBuilder.loadTexts: fspoe.setOrganization('ARICENT COMMUNICATIONS SOFTWARE')
fsPoeSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 2076, 103, 1))
fsPoeGlobalAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 2076, 103, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("start", 1), ("shutdown", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsPoeGlobalAdminStatus.setStatus('current')
fsPoeMacTable = MibTable((1, 3, 6, 1, 4, 1, 2076, 103, 1, 2), )
if mibBuilder.loadTexts: fsPoeMacTable.setStatus('current')
fsPoeMacEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2076, 103, 1, 2, 1), ).setIndexNames((0, "ARICENT-POE-MIB", "fsPoePdMacAddress"))
if mibBuilder.loadTexts: fsPoeMacEntry.setStatus('current')
fsPoePdMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2076, 103, 1, 2, 1, 1), MacAddress())
if mibBuilder.loadTexts: fsPoePdMacAddress.setStatus('current')
fsPoePdMacPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2076, 103, 1, 2, 1, 2), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsPoePdMacPort.setStatus('current')
fsPoePdMacRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2076, 103, 1, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fsPoePdMacRowStatus.setStatus('current')
mibBuilder.exportSymbols("ARICENT-POE-MIB", fsPoeMacEntry=fsPoeMacEntry, fsPoePdMacPort=fsPoePdMacPort, PYSNMP_MODULE_ID=fspoe, fsPoePdMacAddress=fsPoePdMacAddress, fsPoePdMacRowStatus=fsPoePdMacRowStatus, fsPoeGlobalAdminStatus=fsPoeGlobalAdminStatus, fsPoeSystem=fsPoeSystem, fsPoeMacTable=fsPoeMacTable, fspoe=fspoe)
