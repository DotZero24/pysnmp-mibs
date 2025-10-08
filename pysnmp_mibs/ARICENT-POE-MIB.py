#
# PySNMP MIB module ARICENT-POE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/aricent/ARICENT-POE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:32:29 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, MacAddress, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "RowStatus", "TextualConvention")
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
mibBuilder.exportSymbols("ARICENT-POE-MIB", fspoe=fspoe, fsPoePdMacPort=fsPoePdMacPort, PYSNMP_MODULE_ID=fspoe, fsPoeMacEntry=fsPoeMacEntry, fsPoePdMacRowStatus=fsPoePdMacRowStatus, fsPoeMacTable=fsPoeMacTable, fsPoeSystem=fsPoeSystem, fsPoeGlobalAdminStatus=fsPoeGlobalAdminStatus, fsPoePdMacAddress=fsPoePdMacAddress)
