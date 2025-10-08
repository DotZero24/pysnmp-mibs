#
# PySNMP MIB module HP-ICF-SLOT-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hp/HP-ICF-SLOT-STATS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:02:09 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
hpSwitchStatistics, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitchStatistics")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hpicfSlotStatsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 20))
hpicfSlotStatsMIB.setRevisions(('2012-01-05 00:00',))
if mibBuilder.loadTexts: hpicfSlotStatsMIB.setLastUpdated('201201050000Z')
if mibBuilder.loadTexts: hpicfSlotStatsMIB.setOrganization('HP Networking')
hpicfSlotStatsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 20, 1))
hpicfSlotStatsConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 20, 2))
hpicfSlotStatsModuleCpuStatTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 20, 1, 1), )
if mibBuilder.loadTexts: hpicfSlotStatsModuleCpuStatTable.setStatus('current')
hpicfSlotStatsModuleCpuStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 20, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: hpicfSlotStatsModuleCpuStatEntry.setStatus('current')
hpicfSlotStatsModuleHwModel = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 20, 1, 1, 1, 1), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSlotStatsModuleHwModel.setStatus('current')
hpicfSlotStatsModuleSerialNum = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 20, 1, 1, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSlotStatsModuleSerialNum.setStatus('current')
hpicfSlotStatsModuleCpuStatCurrentPercent = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 20, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSlotStatsModuleCpuStatCurrentPercent.setStatus('current')
hpicfSlotStatsModuleCpuStatAveragePercent = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 20, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSlotStatsModuleCpuStatAveragePercent.setStatus('current')
hpicfSlotStatsModuleCpuStatUpdateFrequency = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 20, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSlotStatsModuleCpuStatUpdateFrequency.setStatus('current')
hpicfSlotStatsGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 20, 2, 1))
hpicfSlotStatsCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 20, 2, 2))
hpicfSlotStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 20, 2, 1, 1)).setObjects(("HP-ICF-SLOT-STATS-MIB", "hpicfSlotStatsModuleHwModel"), ("HP-ICF-SLOT-STATS-MIB", "hpicfSlotStatsModuleSerialNum"), ("HP-ICF-SLOT-STATS-MIB", "hpicfSlotStatsModuleCpuStatCurrentPercent"), ("HP-ICF-SLOT-STATS-MIB", "hpicfSlotStatsModuleCpuStatAveragePercent"), ("HP-ICF-SLOT-STATS-MIB", "hpicfSlotStatsModuleCpuStatUpdateFrequency"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSlotStatsGroup = hpicfSlotStatsGroup.setStatus('current')
hpicfSlotStatsFullCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 20, 2, 2, 1)).setObjects(("HP-ICF-SLOT-STATS-MIB", "hpicfSlotStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSlotStatsFullCompliance1 = hpicfSlotStatsFullCompliance1.setStatus('current')
hpicfModuleSlotStatsReadOnlyCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9, 20, 2, 2, 2)).setObjects(("HP-ICF-SLOT-STATS-MIB", "hpicfSlotStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfModuleSlotStatsReadOnlyCompliance1 = hpicfModuleSlotStatsReadOnlyCompliance1.setStatus('current')
mibBuilder.exportSymbols("HP-ICF-SLOT-STATS-MIB", hpicfModuleSlotStatsReadOnlyCompliance1=hpicfModuleSlotStatsReadOnlyCompliance1, hpicfSlotStatsModuleSerialNum=hpicfSlotStatsModuleSerialNum, hpicfSlotStatsObjects=hpicfSlotStatsObjects, PYSNMP_MODULE_ID=hpicfSlotStatsMIB, hpicfSlotStatsModuleCpuStatEntry=hpicfSlotStatsModuleCpuStatEntry, hpicfSlotStatsModuleCpuStatUpdateFrequency=hpicfSlotStatsModuleCpuStatUpdateFrequency, hpicfSlotStatsGroup=hpicfSlotStatsGroup, hpicfSlotStatsModuleCpuStatAveragePercent=hpicfSlotStatsModuleCpuStatAveragePercent, hpicfSlotStatsConformance=hpicfSlotStatsConformance, hpicfSlotStatsCompliances=hpicfSlotStatsCompliances, hpicfSlotStatsMIB=hpicfSlotStatsMIB, hpicfSlotStatsGroups=hpicfSlotStatsGroups, hpicfSlotStatsModuleHwModel=hpicfSlotStatsModuleHwModel, hpicfSlotStatsModuleCpuStatCurrentPercent=hpicfSlotStatsModuleCpuStatCurrentPercent, hpicfSlotStatsFullCompliance1=hpicfSlotStatsFullCompliance1, hpicfSlotStatsModuleCpuStatTable=hpicfSlotStatsModuleCpuStatTable)
