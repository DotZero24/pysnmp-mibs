#
# PySNMP MIB module BROCADE-MODULE-CPU-UTIL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/brocade/BROCADE-MODULE-CPU-UTIL-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:06:56 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
bcsiModules, = mibBuilder.importSymbols("Brocade-REG-MIB", "bcsiModules")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
brocadeModuleCpuUtilMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1588, 3, 1, 12))
brocadeModuleCpuUtilMIB.setRevisions(('2018-05-29 12:00', '2016-11-25 00:00',))
if mibBuilder.loadTexts: brocadeModuleCpuUtilMIB.setLastUpdated('201805291200Z')
if mibBuilder.loadTexts: brocadeModuleCpuUtilMIB.setOrganization('Extreme Networks, Inc.')
bcsiModuleCpuUtilNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 3, 1, 12, 0))
bcsiModuleCpuUtilObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 3, 1, 12, 1))
bcsiModuleCpuUtilConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 3, 1, 12, 2))
bcsiModuleCpuUtilTable = MibTable((1, 3, 6, 1, 4, 1, 1588, 3, 1, 12, 1, 1), )
if mibBuilder.loadTexts: bcsiModuleCpuUtilTable.setStatus('current')
bcsiModuleCpuUtilEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1588, 3, 1, 12, 1, 1, 1), ).setIndexNames((0, "BROCADE-MODULE-CPU-UTIL-MIB", "bcsiModuleCpuUtilSlotNum"), (0, "BROCADE-MODULE-CPU-UTIL-MIB", "bcsiModuleCpuUtilInterval"))
if mibBuilder.loadTexts: bcsiModuleCpuUtilEntry.setStatus('current')
bcsiModuleCpuUtilSlotNum = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 3, 1, 12, 1, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: bcsiModuleCpuUtilSlotNum.setStatus('current')
bcsiModuleCpuUtilInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 3, 1, 12, 1, 1, 1, 2), Integer32())
if mibBuilder.loadTexts: bcsiModuleCpuUtilInterval.setStatus('current')
bcsiModuleCpuUtil100thPercent = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 3, 1, 12, 1, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcsiModuleCpuUtil100thPercent.setStatus('current')
bcsiModuleCpuUtilCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 3, 1, 12, 2, 1))
bcsiModuleCpuUtilGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 3, 1, 12, 2, 2))
bcsiModuleCpuUtilCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1588, 3, 1, 12, 2, 1, 1)).setObjects(("BROCADE-MODULE-CPU-UTIL-MIB", "bcsiModuleCpuUtilizationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcsiModuleCpuUtilCompliance = bcsiModuleCpuUtilCompliance.setStatus('current')
bcsiModuleCpuUtilizationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1588, 3, 1, 12, 2, 2, 1)).setObjects(("BROCADE-MODULE-CPU-UTIL-MIB", "bcsiModuleCpuUtilSlotNum"), ("BROCADE-MODULE-CPU-UTIL-MIB", "bcsiModuleCpuUtilInterval"), ("BROCADE-MODULE-CPU-UTIL-MIB", "bcsiModuleCpuUtil100thPercent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcsiModuleCpuUtilizationGroup = bcsiModuleCpuUtilizationGroup.setStatus('current')
mibBuilder.exportSymbols("BROCADE-MODULE-CPU-UTIL-MIB", brocadeModuleCpuUtilMIB=brocadeModuleCpuUtilMIB, bcsiModuleCpuUtilObjects=bcsiModuleCpuUtilObjects, bcsiModuleCpuUtil100thPercent=bcsiModuleCpuUtil100thPercent, bcsiModuleCpuUtilGroups=bcsiModuleCpuUtilGroups, bcsiModuleCpuUtilEntry=bcsiModuleCpuUtilEntry, bcsiModuleCpuUtilCompliance=bcsiModuleCpuUtilCompliance, bcsiModuleCpuUtilNotifications=bcsiModuleCpuUtilNotifications, bcsiModuleCpuUtilCompliances=bcsiModuleCpuUtilCompliances, bcsiModuleCpuUtilizationGroup=bcsiModuleCpuUtilizationGroup, bcsiModuleCpuUtilTable=bcsiModuleCpuUtilTable, bcsiModuleCpuUtilSlotNum=bcsiModuleCpuUtilSlotNum, PYSNMP_MODULE_ID=brocadeModuleCpuUtilMIB, bcsiModuleCpuUtilInterval=bcsiModuleCpuUtilInterval, bcsiModuleCpuUtilConformance=bcsiModuleCpuUtilConformance)
