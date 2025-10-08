#
# PySNMP MIB module HP-ICF-SLOT-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hp/HP-ICF-SLOT-STATS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:07:47 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
hpSwitchStatistics, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitchStatistics")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("HP-ICF-SLOT-STATS-MIB", PYSNMP_MODULE_ID=hpicfSlotStatsMIB, hpicfSlotStatsModuleHwModel=hpicfSlotStatsModuleHwModel, hpicfSlotStatsModuleCpuStatTable=hpicfSlotStatsModuleCpuStatTable, hpicfSlotStatsModuleCpuStatCurrentPercent=hpicfSlotStatsModuleCpuStatCurrentPercent, hpicfModuleSlotStatsReadOnlyCompliance1=hpicfModuleSlotStatsReadOnlyCompliance1, hpicfSlotStatsConformance=hpicfSlotStatsConformance, hpicfSlotStatsObjects=hpicfSlotStatsObjects, hpicfSlotStatsGroup=hpicfSlotStatsGroup, hpicfSlotStatsFullCompliance1=hpicfSlotStatsFullCompliance1, hpicfSlotStatsCompliances=hpicfSlotStatsCompliances, hpicfSlotStatsModuleCpuStatAveragePercent=hpicfSlotStatsModuleCpuStatAveragePercent, hpicfSlotStatsMIB=hpicfSlotStatsMIB, hpicfSlotStatsModuleSerialNum=hpicfSlotStatsModuleSerialNum, hpicfSlotStatsModuleCpuStatEntry=hpicfSlotStatsModuleCpuStatEntry, hpicfSlotStatsGroups=hpicfSlotStatsGroups, hpicfSlotStatsModuleCpuStatUpdateFrequency=hpicfSlotStatsModuleCpuStatUpdateFrequency)
