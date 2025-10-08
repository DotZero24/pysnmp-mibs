#
# PySNMP MIB module CISCO-STACKMAKER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-STACKMAKER-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:13:35 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoStackMakerMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 59))
if mibBuilder.loadTexts: ciscoStackMakerMIB.setLastUpdated('9610311200Z')
if mibBuilder.loadTexts: ciscoStackMakerMIB.setOrganization('Cisco Systems, Inc.')
ciscoStackMakerMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 59, 1))
ciscoStackMakerConf = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 59, 1, 1))
csmStackName = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 59, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csmStackName.setStatus('current')
csmClearStackTable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 59, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("clearTable", 1), ("noClearTable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csmClearStackTable.setStatus('current')
csmStackTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 59, 1, 1, 3), )
if mibBuilder.loadTexts: csmStackTable.setStatus('current')
csmStackEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 59, 1, 1, 3, 1), ).setIndexNames((0, "CISCO-STACKMAKER-MIB", "csmStackIndex"))
if mibBuilder.loadTexts: csmStackEntry.setStatus('current')
csmStackIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 59, 1, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32)))
if mibBuilder.loadTexts: csmStackIndex.setStatus('current')
csmStackIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 59, 1, 1, 3, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: csmStackIpAddress.setStatus('current')
ciscoStackMakerMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 59, 3))
ciscoStackMakerMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 59, 3, 1))
ciscoStackMakerMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 59, 3, 2))
ciscoStackMakerMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 59, 3, 1, 1)).setObjects(("CISCO-STACKMAKER-MIB", "ciscoStackMakerBasicGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoStackMakerMIBCompliance = ciscoStackMakerMIBCompliance.setStatus('current')
ciscoStackMakerBasicGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 59, 3, 2, 1)).setObjects(("CISCO-STACKMAKER-MIB", "csmStackName"), ("CISCO-STACKMAKER-MIB", "csmClearStackTable"), ("CISCO-STACKMAKER-MIB", "csmStackIpAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoStackMakerBasicGroup = ciscoStackMakerBasicGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-STACKMAKER-MIB", csmStackEntry=csmStackEntry, ciscoStackMakerMIB=ciscoStackMakerMIB, csmStackIndex=csmStackIndex, ciscoStackMakerConf=ciscoStackMakerConf, csmStackName=csmStackName, ciscoStackMakerMIBConformance=ciscoStackMakerMIBConformance, ciscoStackMakerMIBCompliances=ciscoStackMakerMIBCompliances, ciscoStackMakerMIBGroups=ciscoStackMakerMIBGroups, ciscoStackMakerBasicGroup=ciscoStackMakerBasicGroup, ciscoStackMakerMIBCompliance=ciscoStackMakerMIBCompliance, csmStackTable=csmStackTable, csmStackIpAddress=csmStackIpAddress, csmClearStackTable=csmClearStackTable, PYSNMP_MODULE_ID=ciscoStackMakerMIB, ciscoStackMakerMIBObjects=ciscoStackMakerMIBObjects)
