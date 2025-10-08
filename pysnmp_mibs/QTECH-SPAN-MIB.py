#
# PySNMP MIB module QTECH-SPAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/qtech/QTECH-SPAN-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:14:37 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
qtechMgmt, = mibBuilder.importSymbols("QTECH-SMI", "qtechMgmt")
IfIndex, ConfigStatus = mibBuilder.importSymbols("QTECH-TC", "IfIndex", "ConfigStatus")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("QTECH-SPAN-MIB", qtechSPANSession=qtechSPANSession, qtechSPANSessionNum=qtechSPANSessionNum, qtechSPANEntryStatus=qtechSPANEntryStatus, qtechSPANMIBCompliance=qtechSPANMIBCompliance, PYSNMP_MODULE_ID=qtechSPANMIB, qtechSPANMIBObjects=qtechSPANMIBObjects, qtechSPANEntry=qtechSPANEntry, qtechSPANMIBConformance=qtechSPANMIBConformance, qtechSPANMIBGroups=qtechSPANMIBGroups, qtechSPANMIBGroup=qtechSPANMIBGroup, qtechSPANIfRole=qtechSPANIfRole, qtechSPANIfIndex=qtechSPANIfIndex, qtechSPANTable=qtechSPANTable, qtechSPANMIBCompliances=qtechSPANMIBCompliances, qtechSPANMIB=qtechSPANMIB)
