#
# PySNMP MIB module BDCOM-MEMORY-POOL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/bdcom/BDCOM-MEMORY-POOL-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:42:07 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
Percent, = mibBuilder.importSymbols("BDCOM-QOS-PIB-MIB", "Percent")
bdMgmt, = mibBuilder.importSymbols("BDCOM-SMI", "bdMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
bdcomMemoryPoolMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3320, 9, 48))
bdcomMemoryPoolMIB.setRevisions(('2003-10-16 00:00',))
if mibBuilder.loadTexts: bdcomMemoryPoolMIB.setLastUpdated('200310160000Z')
if mibBuilder.loadTexts: bdcomMemoryPoolMIB.setOrganization('BDCOM, Inc.')
class BDCOMMemoryPoolTypes(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 65535)

bdcomMemoryPoolObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3320, 9, 48, 1))
bdcomMemoryPoolTable = MibTable((1, 3, 6, 1, 4, 1, 3320, 9, 48, 1, 1), )
if mibBuilder.loadTexts: bdcomMemoryPoolTable.setStatus('current')
bdcomMemoryPoolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3320, 9, 48, 1, 1, 1), ).setIndexNames((0, "BDCOM-MEMORY-POOL-MIB", "bdcomMemoryPoolType"))
if mibBuilder.loadTexts: bdcomMemoryPoolEntry.setStatus('current')
bdcomMemoryPoolType = MibTableColumn((1, 3, 6, 1, 4, 1, 3320, 9, 48, 1, 1, 1, 1), BDCOMMemoryPoolTypes())
if mibBuilder.loadTexts: bdcomMemoryPoolType.setStatus('current')
bdcomMemoryPoolName = MibTableColumn((1, 3, 6, 1, 4, 1, 3320, 9, 48, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdcomMemoryPoolName.setStatus('current')
bdcomMemoryPoolAlternate = MibTableColumn((1, 3, 6, 1, 4, 1, 3320, 9, 48, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdcomMemoryPoolAlternate.setStatus('current')
bdcomMemoryPoolValid = MibTableColumn((1, 3, 6, 1, 4, 1, 3320, 9, 48, 1, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdcomMemoryPoolValid.setStatus('current')
bdcomMemoryPoolUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 3320, 9, 48, 1, 1, 1, 5), Gauge32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: bdcomMemoryPoolUsed.setStatus('current')
bdcomMemoryPoolFree = MibTableColumn((1, 3, 6, 1, 4, 1, 3320, 9, 48, 1, 1, 1, 6), Gauge32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: bdcomMemoryPoolFree.setStatus('current')
bdcomMemoryPoolLargestFree = MibTableColumn((1, 3, 6, 1, 4, 1, 3320, 9, 48, 1, 1, 1, 7), Gauge32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: bdcomMemoryPoolLargestFree.setStatus('current')
bdcomMemoryPoolUtilizationTable = MibTable((1, 3, 6, 1, 4, 1, 3320, 9, 48, 1, 2), )
if mibBuilder.loadTexts: bdcomMemoryPoolUtilizationTable.setStatus('current')
bdcomMemoryPoolUtilizationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3320, 9, 48, 1, 2, 1), )
bdcomMemoryPoolEntry.registerAugmentions(("BDCOM-MEMORY-POOL-MIB", "bdcomMemoryPoolUtilizationEntry"))
bdcomMemoryPoolUtilizationEntry.setIndexNames(*bdcomMemoryPoolEntry.getIndexNames())
if mibBuilder.loadTexts: bdcomMemoryPoolUtilizationEntry.setStatus('current')
bdcomMemoryPoolUtilization1Min = MibTableColumn((1, 3, 6, 1, 4, 1, 3320, 9, 48, 1, 2, 1, 1), Percent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdcomMemoryPoolUtilization1Min.setStatus('current')
bdcomMemoryPoolUtilization5Min = MibTableColumn((1, 3, 6, 1, 4, 1, 3320, 9, 48, 1, 2, 1, 2), Percent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdcomMemoryPoolUtilization5Min.setStatus('current')
bdcomMemoryPoolUtilization10Min = MibTableColumn((1, 3, 6, 1, 4, 1, 3320, 9, 48, 1, 2, 1, 3), Percent()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bdcomMemoryPoolUtilization10Min.setStatus('current')
bdcomMemoryPoolNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 3320, 9, 48, 2))
bdcomMemoryPoolConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 3320, 9, 48, 3))
bdcomMemoryPoolCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 3320, 9, 48, 3, 1))
bdcomMemoryPoolGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 3320, 9, 48, 3, 2))
bdcomMemoryPoolCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 3320, 9, 48, 3, 1, 1)).setObjects(("BDCOM-MEMORY-POOL-MIB", "bdcomMemoryPoolGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bdcomMemoryPoolCompliance = bdcomMemoryPoolCompliance.setStatus('deprecated')
bdcomMemoryPoolComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 3320, 9, 48, 3, 1, 2)).setObjects(("BDCOM-MEMORY-POOL-MIB", "bdcomMemoryPoolGroup"), ("BDCOM-MEMORY-POOL-MIB", "bdcomMemoryPoolUtilizationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bdcomMemoryPoolComplianceRev1 = bdcomMemoryPoolComplianceRev1.setStatus('current')
bdcomMemoryPoolGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3320, 9, 48, 3, 2, 1)).setObjects(("BDCOM-MEMORY-POOL-MIB", "bdcomMemoryPoolName"), ("BDCOM-MEMORY-POOL-MIB", "bdcomMemoryPoolAlternate"), ("BDCOM-MEMORY-POOL-MIB", "bdcomMemoryPoolValid"), ("BDCOM-MEMORY-POOL-MIB", "bdcomMemoryPoolUsed"), ("BDCOM-MEMORY-POOL-MIB", "bdcomMemoryPoolFree"), ("BDCOM-MEMORY-POOL-MIB", "bdcomMemoryPoolLargestFree"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bdcomMemoryPoolGroup = bdcomMemoryPoolGroup.setStatus('current')
bdcomMemoryPoolUtilizationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3320, 9, 48, 3, 2, 2)).setObjects(("BDCOM-MEMORY-POOL-MIB", "bdcomMemoryPoolUtilization1Min"), ("BDCOM-MEMORY-POOL-MIB", "bdcomMemoryPoolUtilization5Min"), ("BDCOM-MEMORY-POOL-MIB", "bdcomMemoryPoolUtilization10Min"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bdcomMemoryPoolUtilizationGroup = bdcomMemoryPoolUtilizationGroup.setStatus('current')
mibBuilder.exportSymbols("BDCOM-MEMORY-POOL-MIB", bdcomMemoryPoolObjects=bdcomMemoryPoolObjects, bdcomMemoryPoolUtilizationGroup=bdcomMemoryPoolUtilizationGroup, bdcomMemoryPoolUsed=bdcomMemoryPoolUsed, bdcomMemoryPoolUtilizationTable=bdcomMemoryPoolUtilizationTable, bdcomMemoryPoolUtilization5Min=bdcomMemoryPoolUtilization5Min, bdcomMemoryPoolGroups=bdcomMemoryPoolGroups, bdcomMemoryPoolFree=bdcomMemoryPoolFree, bdcomMemoryPoolNotifications=bdcomMemoryPoolNotifications, bdcomMemoryPoolUtilization10Min=bdcomMemoryPoolUtilization10Min, bdcomMemoryPoolUtilization1Min=bdcomMemoryPoolUtilization1Min, bdcomMemoryPoolValid=bdcomMemoryPoolValid, bdcomMemoryPoolGroup=bdcomMemoryPoolGroup, BDCOMMemoryPoolTypes=BDCOMMemoryPoolTypes, bdcomMemoryPoolEntry=bdcomMemoryPoolEntry, bdcomMemoryPoolType=bdcomMemoryPoolType, bdcomMemoryPoolAlternate=bdcomMemoryPoolAlternate, bdcomMemoryPoolName=bdcomMemoryPoolName, bdcomMemoryPoolConformance=bdcomMemoryPoolConformance, bdcomMemoryPoolTable=bdcomMemoryPoolTable, bdcomMemoryPoolComplianceRev1=bdcomMemoryPoolComplianceRev1, bdcomMemoryPoolMIB=bdcomMemoryPoolMIB, bdcomMemoryPoolLargestFree=bdcomMemoryPoolLargestFree, bdcomMemoryPoolCompliance=bdcomMemoryPoolCompliance, PYSNMP_MODULE_ID=bdcomMemoryPoolMIB, bdcomMemoryPoolUtilizationEntry=bdcomMemoryPoolUtilizationEntry, bdcomMemoryPoolCompliances=bdcomMemoryPoolCompliances)
