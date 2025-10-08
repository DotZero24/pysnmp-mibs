#
# PySNMP MIB module CISCO-VISM-PORT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-VISM-PORT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:13:51 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
vismPort, = mibBuilder.importSymbols("BASIS-MIB", "vismPort")
ciscoWan, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWan")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoVismPortMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 150, 92))
ciscoVismPortMIB.setRevisions(('2003-10-16 00:00',))
if mibBuilder.loadTexts: ciscoVismPortMIB.setLastUpdated('200310160000Z')
if mibBuilder.loadTexts: ciscoVismPortMIB.setOrganization('Cisco Systems, Inc.')
vismPortCnfGrp = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 2, 1))
vismPortCnfGrpTable = MibTable((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 2, 1, 1), )
if mibBuilder.loadTexts: vismPortCnfGrpTable.setStatus('current')
vismPortCnfGrpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 2, 1, 1, 1), ).setIndexNames((0, "CISCO-VISM-PORT-MIB", "vismPortNum"))
if mibBuilder.loadTexts: vismPortCnfGrpEntry.setStatus('current')
vismPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 2, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismPortNum.setStatus('current')
vismPortRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 2, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("add", 1), ("del", 2), ("mod", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vismPortRowStatus.setStatus('current')
vismPortLineNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 2, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 8))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vismPortLineNum.setStatus('current')
vismPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 2, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("voIP", 1), ("userPort", 2))).clone('voIP')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vismPortType.setStatus('current')
vismPortDs0ConfigBitMap = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 2, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16777215))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vismPortDs0ConfigBitMap.setStatus('current')
vismPortSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 2, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 5651320)).clone(5651320)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vismPortSpeed.setStatus('current')
vismPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 2, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("notConfigured", 1), ("active", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vismPortState.setStatus('current')
ciscoVismPortMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 92, 2))
ciscoVismPortMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 92, 2, 1))
ciscoVismPortMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 92, 2, 2))
ciscoVismPortCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 92, 2, 2, 1)).setObjects(("CISCO-VISM-PORT-MIB", "ciscoVismPortGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVismPortCompliance = ciscoVismPortCompliance.setStatus('current')
ciscoVismPortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 92, 2, 1, 1)).setObjects(("CISCO-VISM-PORT-MIB", "vismPortNum"), ("CISCO-VISM-PORT-MIB", "vismPortRowStatus"), ("CISCO-VISM-PORT-MIB", "vismPortLineNum"), ("CISCO-VISM-PORT-MIB", "vismPortType"), ("CISCO-VISM-PORT-MIB", "vismPortDs0ConfigBitMap"), ("CISCO-VISM-PORT-MIB", "vismPortSpeed"), ("CISCO-VISM-PORT-MIB", "vismPortState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVismPortGroup = ciscoVismPortGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-VISM-PORT-MIB", vismPortType=vismPortType, vismPortDs0ConfigBitMap=vismPortDs0ConfigBitMap, vismPortCnfGrpEntry=vismPortCnfGrpEntry, vismPortRowStatus=vismPortRowStatus, vismPortSpeed=vismPortSpeed, vismPortCnfGrpTable=vismPortCnfGrpTable, ciscoVismPortGroup=ciscoVismPortGroup, vismPortNum=vismPortNum, ciscoVismPortMIBConformance=ciscoVismPortMIBConformance, vismPortState=vismPortState, ciscoVismPortMIB=ciscoVismPortMIB, ciscoVismPortMIBGroups=ciscoVismPortMIBGroups, vismPortLineNum=vismPortLineNum, vismPortCnfGrp=vismPortCnfGrp, PYSNMP_MODULE_ID=ciscoVismPortMIB, ciscoVismPortMIBCompliances=ciscoVismPortMIBCompliances, ciscoVismPortCompliance=ciscoVismPortCompliance)
