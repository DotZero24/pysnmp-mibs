#
# PySNMP MIB module BROCADE-MODULE-MEM-UTIL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/brocade/BROCADE-MODULE-MEM-UTIL-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:15:50 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
bcsiModules, = mibBuilder.importSymbols("Brocade-REG-MIB", "bcsiModules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
brocadeModuleMemUtilMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1588, 3, 1, 13))
brocadeModuleMemUtilMIB.setRevisions(('2018-05-29 12:00', '2016-11-25 00:00',))
if mibBuilder.loadTexts: brocadeModuleMemUtilMIB.setLastUpdated('201805291200Z')
if mibBuilder.loadTexts: brocadeModuleMemUtilMIB.setOrganization('Extreme Networks, Inc.')
bcsiModuleMemUtilNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 3, 1, 13, 0))
bcsiModuleMemUtilObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 3, 1, 13, 1))
bcsiModuleMemUtilConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 3, 1, 13, 2))
bcsiModuleMemUtilTable = MibTable((1, 3, 6, 1, 4, 1, 1588, 3, 1, 13, 1, 1), )
if mibBuilder.loadTexts: bcsiModuleMemUtilTable.setStatus('current')
bcsiModuleMemUtilEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1588, 3, 1, 13, 1, 1, 1), ).setIndexNames((0, "BROCADE-MODULE-MEM-UTIL-MIB", "bcsiModuleMemUtilSlotNum"))
if mibBuilder.loadTexts: bcsiModuleMemUtilEntry.setStatus('current')
bcsiModuleMemUtilSlotNum = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 3, 1, 13, 1, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: bcsiModuleMemUtilSlotNum.setStatus('current')
bcsiModuleMemTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 3, 1, 13, 1, 1, 1, 2), Unsigned32()).setUnits('kilo Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: bcsiModuleMemTotal.setStatus('current')
bcsiModuleMemAvailable = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 3, 1, 13, 1, 1, 1, 3), Gauge32()).setUnits('kilo Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: bcsiModuleMemAvailable.setStatus('current')
bcsiModuleMemUtil100thPercent = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 3, 1, 13, 1, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcsiModuleMemUtil100thPercent.setStatus('current')
bcsiModuleMemUtilCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 3, 1, 13, 2, 1))
bcsiModuleMemUtilGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 3, 1, 13, 2, 2))
bcsiModuleMemUtilCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1588, 3, 1, 13, 2, 1, 1)).setObjects(("BROCADE-MODULE-MEM-UTIL-MIB", "bcsiModuleMemUtilizationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcsiModuleMemUtilCompliance = bcsiModuleMemUtilCompliance.setStatus('current')
bcsiModuleMemUtilizationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1588, 3, 1, 13, 2, 2, 1)).setObjects(("BROCADE-MODULE-MEM-UTIL-MIB", "bcsiModuleMemUtilSlotNum"), ("BROCADE-MODULE-MEM-UTIL-MIB", "bcsiModuleMemTotal"), ("BROCADE-MODULE-MEM-UTIL-MIB", "bcsiModuleMemAvailable"), ("BROCADE-MODULE-MEM-UTIL-MIB", "bcsiModuleMemUtil100thPercent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcsiModuleMemUtilizationGroup = bcsiModuleMemUtilizationGroup.setStatus('current')
mibBuilder.exportSymbols("BROCADE-MODULE-MEM-UTIL-MIB", bcsiModuleMemAvailable=bcsiModuleMemAvailable, bcsiModuleMemUtilizationGroup=bcsiModuleMemUtilizationGroup, bcsiModuleMemTotal=bcsiModuleMemTotal, bcsiModuleMemUtilNotifications=bcsiModuleMemUtilNotifications, bcsiModuleMemUtilTable=bcsiModuleMemUtilTable, bcsiModuleMemUtilSlotNum=bcsiModuleMemUtilSlotNum, bcsiModuleMemUtilCompliance=bcsiModuleMemUtilCompliance, bcsiModuleMemUtilConformance=bcsiModuleMemUtilConformance, brocadeModuleMemUtilMIB=brocadeModuleMemUtilMIB, PYSNMP_MODULE_ID=brocadeModuleMemUtilMIB, bcsiModuleMemUtilEntry=bcsiModuleMemUtilEntry, bcsiModuleMemUtilGroups=bcsiModuleMemUtilGroups, bcsiModuleMemUtil100thPercent=bcsiModuleMemUtil100thPercent, bcsiModuleMemUtilCompliances=bcsiModuleMemUtilCompliances, bcsiModuleMemUtilObjects=bcsiModuleMemUtilObjects)
