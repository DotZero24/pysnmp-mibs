#
# PySNMP MIB module BROCADE-MODULE-MEM-UTIL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/brocade/BROCADE-MODULE-MEM-UTIL-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:07:09 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
bcsiModules, = mibBuilder.importSymbols("Brocade-REG-MIB", "bcsiModules")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, Unsigned32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "Unsigned32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("BROCADE-MODULE-MEM-UTIL-MIB", bcsiModuleMemUtilCompliance=bcsiModuleMemUtilCompliance, PYSNMP_MODULE_ID=brocadeModuleMemUtilMIB, bcsiModuleMemUtilTable=bcsiModuleMemUtilTable, bcsiModuleMemUtilizationGroup=bcsiModuleMemUtilizationGroup, bcsiModuleMemAvailable=bcsiModuleMemAvailable, bcsiModuleMemUtilCompliances=bcsiModuleMemUtilCompliances, bcsiModuleMemUtilNotifications=bcsiModuleMemUtilNotifications, bcsiModuleMemTotal=bcsiModuleMemTotal, bcsiModuleMemUtil100thPercent=bcsiModuleMemUtil100thPercent, brocadeModuleMemUtilMIB=brocadeModuleMemUtilMIB, bcsiModuleMemUtilGroups=bcsiModuleMemUtilGroups, bcsiModuleMemUtilObjects=bcsiModuleMemUtilObjects, bcsiModuleMemUtilSlotNum=bcsiModuleMemUtilSlotNum, bcsiModuleMemUtilEntry=bcsiModuleMemUtilEntry, bcsiModuleMemUtilConformance=bcsiModuleMemUtilConformance)
