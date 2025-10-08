#
# PySNMP MIB module QTECH-SPAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/qtech/QTECH-SPAN-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:06:31 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
qtechMgmt, = mibBuilder.importSymbols("QTECH-SMI", "qtechMgmt")
IfIndex, ConfigStatus = mibBuilder.importSymbols("QTECH-TC", "IfIndex", "ConfigStatus")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
qtechSPANMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 23))
qtechSPANMIB.setRevisions(('2002-03-20 00:00',))
if mibBuilder.loadTexts: qtechSPANMIB.setLastUpdated('200203200000Z')
if mibBuilder.loadTexts: qtechSPANMIB.setOrganization('Qtech Networks Co.,Ltd.')
qtechSPANMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 23, 1))
qtechSPANSessionNum = MibScalar((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 23, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qtechSPANSessionNum.setStatus('current')
qtechSPANTable = MibTable((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 23, 1, 2), )
if mibBuilder.loadTexts: qtechSPANTable.setStatus('current')
qtechSPANEntry = MibTableRow((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 23, 1, 2, 1), ).setIndexNames((0, "QTECH-SPAN-MIB", "qtechSPANSession"), (0, "QTECH-SPAN-MIB", "qtechSPANIfIndex"))
if mibBuilder.loadTexts: qtechSPANEntry.setStatus('current')
qtechSPANSession = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 23, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qtechSPANSession.setStatus('current')
qtechSPANIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 23, 1, 2, 1, 2), IfIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qtechSPANIfIndex.setStatus('current')
qtechSPANIfRole = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 23, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("span-desc", 1), ("span-src-rx", 2), ("span-src-tx", 3), ("span-src-all", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qtechSPANIfRole.setStatus('current')
qtechSPANEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 23, 1, 2, 1, 4), ConfigStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qtechSPANEntryStatus.setStatus('current')
qtechSPANMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 23, 3))
qtechSPANMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 23, 3, 1))
qtechSPANMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 23, 3, 2))
qtechSPANMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 23, 3, 1, 1)).setObjects(("QTECH-SPAN-MIB", "qtechSPANMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qtechSPANMIBCompliance = qtechSPANMIBCompliance.setStatus('current')
qtechSPANMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 23, 3, 2, 1)).setObjects(("QTECH-SPAN-MIB", "qtechSPANSession"), ("QTECH-SPAN-MIB", "qtechSPANIfIndex"), ("QTECH-SPAN-MIB", "qtechSPANIfRole"), ("QTECH-SPAN-MIB", "qtechSPANEntryStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qtechSPANMIBGroup = qtechSPANMIBGroup.setStatus('current')
mibBuilder.exportSymbols("QTECH-SPAN-MIB", qtechSPANSessionNum=qtechSPANSessionNum, qtechSPANSession=qtechSPANSession, qtechSPANIfRole=qtechSPANIfRole, qtechSPANMIBGroups=qtechSPANMIBGroups, qtechSPANMIBObjects=qtechSPANMIBObjects, qtechSPANIfIndex=qtechSPANIfIndex, qtechSPANMIBGroup=qtechSPANMIBGroup, qtechSPANMIBConformance=qtechSPANMIBConformance, qtechSPANEntryStatus=qtechSPANEntryStatus, PYSNMP_MODULE_ID=qtechSPANMIB, qtechSPANTable=qtechSPANTable, qtechSPANMIBCompliances=qtechSPANMIBCompliances, qtechSPANEntry=qtechSPANEntry, qtechSPANMIBCompliance=qtechSPANMIBCompliance, qtechSPANMIB=qtechSPANMIB)
