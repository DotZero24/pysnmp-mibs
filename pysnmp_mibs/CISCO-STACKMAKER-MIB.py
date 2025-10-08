#
# PySNMP MIB module CISCO-STACKMAKER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-STACKMAKER-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:26:39 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("CISCO-STACKMAKER-MIB", csmClearStackTable=csmClearStackTable, PYSNMP_MODULE_ID=ciscoStackMakerMIB, ciscoStackMakerMIBConformance=ciscoStackMakerMIBConformance, ciscoStackMakerMIBGroups=ciscoStackMakerMIBGroups, ciscoStackMakerMIB=ciscoStackMakerMIB, csmStackName=csmStackName, ciscoStackMakerConf=ciscoStackMakerConf, ciscoStackMakerMIBObjects=ciscoStackMakerMIBObjects, csmStackIpAddress=csmStackIpAddress, ciscoStackMakerBasicGroup=ciscoStackMakerBasicGroup, csmStackIndex=csmStackIndex, ciscoStackMakerMIBCompliances=ciscoStackMakerMIBCompliances, csmStackTable=csmStackTable, ciscoStackMakerMIBCompliance=ciscoStackMakerMIBCompliance, csmStackEntry=csmStackEntry)
