#
# PySNMP MIB module CISCO-MGX82XX-RPM-SUBIF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-MGX82XX-RPM-SUBIF-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:16:02 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
rpmPort, = mibBuilder.importSymbols("BASIS-MIB", "rpmPort")
ciscoWan, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWan")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoMgx82xxRpmSubIfMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 150, 60))
ciscoMgx82xxRpmSubIfMIB.setRevisions(('2002-09-08 00:00',))
if mibBuilder.loadTexts: ciscoMgx82xxRpmSubIfMIB.setLastUpdated('200209080000Z')
if mibBuilder.loadTexts: ciscoMgx82xxRpmSubIfMIB.setOrganization('Cisco Systems, Inc.')
rpmPortTable = MibTable((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 9, 1, 1), )
if mibBuilder.loadTexts: rpmPortTable.setStatus('current')
rpmPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 9, 1, 1, 1), ).setIndexNames((0, "CISCO-MGX82XX-RPM-SUBIF-MIB", "rpmPortSlotNum"), (0, "CISCO-MGX82XX-RPM-SUBIF-MIB", "rpmPortSubInterface"))
if mibBuilder.loadTexts: rpmPortEntry.setStatus('current')
rpmPortSlotNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 9, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rpmPortSlotNum.setStatus('current')
rpmPortInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 9, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rpmPortInterface.setStatus('current')
rpmPortSubInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 9, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rpmPortSubInterface.setStatus('current')
rpmPortRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 9, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("add", 1), ("del", 2), ("mod", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rpmPortRowStatus.setStatus('current')
rpmPortIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 9, 1, 1, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rpmPortIpAddress.setStatus('current')
rpmPortSubNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 9, 1, 1, 1, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rpmPortSubNetMask.setStatus('current')
rpmPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 9, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notConfigured", 1), ("active", 2), ("failed", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rpmPortState.setStatus('current')
cmrSubIfMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 60, 2))
cmrSubIfMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 60, 2, 1))
cmrSubIfMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 60, 2, 2))
cmrSubIfMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 60, 2, 1, 1)).setObjects(("CISCO-MGX82XX-RPM-SUBIF-MIB", "cmrSubIfMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmrSubIfMIBCompliance = cmrSubIfMIBCompliance.setStatus('current')
cmrSubIfMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 60, 2, 2, 1)).setObjects(("CISCO-MGX82XX-RPM-SUBIF-MIB", "rpmPortSlotNum"), ("CISCO-MGX82XX-RPM-SUBIF-MIB", "rpmPortInterface"), ("CISCO-MGX82XX-RPM-SUBIF-MIB", "rpmPortSubInterface"), ("CISCO-MGX82XX-RPM-SUBIF-MIB", "rpmPortRowStatus"), ("CISCO-MGX82XX-RPM-SUBIF-MIB", "rpmPortIpAddress"), ("CISCO-MGX82XX-RPM-SUBIF-MIB", "rpmPortSubNetMask"), ("CISCO-MGX82XX-RPM-SUBIF-MIB", "rpmPortState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmrSubIfMIBGroup = cmrSubIfMIBGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-MGX82XX-RPM-SUBIF-MIB", rpmPortInterface=rpmPortInterface, PYSNMP_MODULE_ID=ciscoMgx82xxRpmSubIfMIB, cmrSubIfMIBCompliance=cmrSubIfMIBCompliance, rpmPortEntry=rpmPortEntry, rpmPortRowStatus=rpmPortRowStatus, rpmPortSubNetMask=rpmPortSubNetMask, rpmPortTable=rpmPortTable, cmrSubIfMIBCompliances=cmrSubIfMIBCompliances, cmrSubIfMIBGroups=cmrSubIfMIBGroups, cmrSubIfMIBGroup=cmrSubIfMIBGroup, rpmPortState=rpmPortState, rpmPortSubInterface=rpmPortSubInterface, ciscoMgx82xxRpmSubIfMIB=ciscoMgx82xxRpmSubIfMIB, rpmPortSlotNum=rpmPortSlotNum, cmrSubIfMIBConformance=cmrSubIfMIBConformance, rpmPortIpAddress=rpmPortIpAddress)
