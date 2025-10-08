#
# PySNMP MIB module CISCO-IF-LOOPBACK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-IF-LOOPBACK-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:24:20 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
ciscoIfLoopbackMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 9399))
ciscoIfLoopbackMIB.setRevisions(('2001-11-15 00:00',))
if mibBuilder.loadTexts: ciscoIfLoopbackMIB.setLastUpdated('200111150000Z')
if mibBuilder.loadTexts: ciscoIfLoopbackMIB.setOrganization('Cisco Systems, Inc.')
ciscoIfLoopbackMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9399, 1))
ciscoIfLoopbackConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9399, 1, 1))
cifLConfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 9399, 1, 1, 1), )
if mibBuilder.loadTexts: cifLConfTable.setStatus('current')
cifLConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 9399, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cifLConfEntry.setStatus('current')
cifLLoopback = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9399, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("farEndLineLoopback", 1), ("farEndPayloadLoopback", 2), ("remoteLineLoopback", 3), ("remotePayloadLoopback", 4), ("localLoopback", 5)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cifLLoopback.setStatus('current')
cifLLoopbackStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9399, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("completed", 1), ("inProgress", 2), ("clockOutOfSync", 3), ("failed", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cifLLoopbackStatus.setStatus('current')
cifLFELoopbackDeviceAndCode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9399, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17))).clone(namedValues=NamedValues(("nonLatchOCUwith1", 1), ("nonLatchOCUwithout1", 2), ("nonLatchCSU", 3), ("nonLatchDSU", 4), ("latchDS0Drop", 5), ("latchDS0Line", 6), ("latchOCU", 7), ("latchCSU", 8), ("latchDSU", 9), ("latchHL96", 10), ("v54PN127Polynomial", 11), ("lineInband", 12), ("lineLoopbackESF", 13), ("payloadLoopbackESF", 14), ("noCode", 15), ("lineLoopbackFEAC", 16), ("smartJackInband", 17)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cifLFELoopbackDeviceAndCode.setStatus('current')
cifLRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9399, 1, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cifLRowStatus.setStatus('current')
ciscoIfLoopbackMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9399, 8))
ciscoIfLoopbackMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9399, 8, 1))
ciscoIfLoopbackMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9399, 8, 2))
ciscoIfLoopbackMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 9399, 8, 1, 1)).setObjects(("CISCO-IF-LOOPBACK-MIB", "ciscoIfLoopbackGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfLoopbackMIBCompliance = ciscoIfLoopbackMIBCompliance.setStatus('current')
ciscoIfLoopbackGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 9399, 8, 2, 1)).setObjects(("CISCO-IF-LOOPBACK-MIB", "cifLLoopback"), ("CISCO-IF-LOOPBACK-MIB", "cifLLoopbackStatus"), ("CISCO-IF-LOOPBACK-MIB", "cifLFELoopbackDeviceAndCode"), ("CISCO-IF-LOOPBACK-MIB", "cifLRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfLoopbackGroup = ciscoIfLoopbackGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-IF-LOOPBACK-MIB", ciscoIfLoopbackConfig=ciscoIfLoopbackConfig, ciscoIfLoopbackMIBObjects=ciscoIfLoopbackMIBObjects, ciscoIfLoopbackMIBGroups=ciscoIfLoopbackMIBGroups, ciscoIfLoopbackMIBConformance=ciscoIfLoopbackMIBConformance, cifLLoopback=cifLLoopback, cifLLoopbackStatus=cifLLoopbackStatus, PYSNMP_MODULE_ID=ciscoIfLoopbackMIB, ciscoIfLoopbackMIBCompliances=ciscoIfLoopbackMIBCompliances, ciscoIfLoopbackMIBCompliance=ciscoIfLoopbackMIBCompliance, ciscoIfLoopbackGroup=ciscoIfLoopbackGroup, cifLConfEntry=cifLConfEntry, ciscoIfLoopbackMIB=ciscoIfLoopbackMIB, cifLRowStatus=cifLRowStatus, cifLConfTable=cifLConfTable, cifLFELoopbackDeviceAndCode=cifLFELoopbackDeviceAndCode)
