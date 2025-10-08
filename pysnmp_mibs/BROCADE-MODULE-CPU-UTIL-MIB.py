#
# PySNMP MIB module BROCADE-MODULE-CPU-UTIL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/brocade/BROCADE-MODULE-CPU-UTIL-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:15:24 2025
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
mibBuilder.exportSymbols("BROCADE-MODULE-CPU-UTIL-MIB", bcsiModuleCpuUtil100thPercent=bcsiModuleCpuUtil100thPercent, bcsiModuleCpuUtilConformance=bcsiModuleCpuUtilConformance, PYSNMP_MODULE_ID=brocadeModuleCpuUtilMIB, bcsiModuleCpuUtilizationGroup=bcsiModuleCpuUtilizationGroup, bcsiModuleCpuUtilNotifications=bcsiModuleCpuUtilNotifications, bcsiModuleCpuUtilCompliance=bcsiModuleCpuUtilCompliance, bcsiModuleCpuUtilSlotNum=bcsiModuleCpuUtilSlotNum, bcsiModuleCpuUtilTable=bcsiModuleCpuUtilTable, bcsiModuleCpuUtilGroups=bcsiModuleCpuUtilGroups, brocadeModuleCpuUtilMIB=brocadeModuleCpuUtilMIB, bcsiModuleCpuUtilObjects=bcsiModuleCpuUtilObjects, bcsiModuleCpuUtilEntry=bcsiModuleCpuUtilEntry, bcsiModuleCpuUtilInterval=bcsiModuleCpuUtilInterval, bcsiModuleCpuUtilCompliances=bcsiModuleCpuUtilCompliances)
