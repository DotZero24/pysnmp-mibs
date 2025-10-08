#
# PySNMP MIB module BDCOM-MEMORY-POOL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/bdcom/BDCOM-MEMORY-POOL-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:22:46 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
Percent, = mibBuilder.importSymbols("BDCOM-QOS-PIB-MIB", "Percent")
bdMgmt, = mibBuilder.importSymbols("BDCOM-SMI", "bdMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
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
mibBuilder.exportSymbols("BDCOM-MEMORY-POOL-MIB", bdcomMemoryPoolGroups=bdcomMemoryPoolGroups, bdcomMemoryPoolTable=bdcomMemoryPoolTable, bdcomMemoryPoolUtilizationGroup=bdcomMemoryPoolUtilizationGroup, bdcomMemoryPoolValid=bdcomMemoryPoolValid, PYSNMP_MODULE_ID=bdcomMemoryPoolMIB, bdcomMemoryPoolMIB=bdcomMemoryPoolMIB, bdcomMemoryPoolEntry=bdcomMemoryPoolEntry, bdcomMemoryPoolUtilizationTable=bdcomMemoryPoolUtilizationTable, bdcomMemoryPoolUtilizationEntry=bdcomMemoryPoolUtilizationEntry, bdcomMemoryPoolObjects=bdcomMemoryPoolObjects, bdcomMemoryPoolFree=bdcomMemoryPoolFree, bdcomMemoryPoolType=bdcomMemoryPoolType, BDCOMMemoryPoolTypes=BDCOMMemoryPoolTypes, bdcomMemoryPoolNotifications=bdcomMemoryPoolNotifications, bdcomMemoryPoolComplianceRev1=bdcomMemoryPoolComplianceRev1, bdcomMemoryPoolUtilization5Min=bdcomMemoryPoolUtilization5Min, bdcomMemoryPoolUsed=bdcomMemoryPoolUsed, bdcomMemoryPoolName=bdcomMemoryPoolName, bdcomMemoryPoolCompliance=bdcomMemoryPoolCompliance, bdcomMemoryPoolConformance=bdcomMemoryPoolConformance, bdcomMemoryPoolUtilization1Min=bdcomMemoryPoolUtilization1Min, bdcomMemoryPoolAlternate=bdcomMemoryPoolAlternate, bdcomMemoryPoolGroup=bdcomMemoryPoolGroup, bdcomMemoryPoolLargestFree=bdcomMemoryPoolLargestFree, bdcomMemoryPoolUtilization10Min=bdcomMemoryPoolUtilization10Min, bdcomMemoryPoolCompliances=bdcomMemoryPoolCompliances)
