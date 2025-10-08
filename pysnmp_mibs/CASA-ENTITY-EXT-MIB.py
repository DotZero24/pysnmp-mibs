#
# PySNMP MIB module CASA-ENTITY-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/casa/CASA-ENTITY-EXT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:06:43 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
casa, = mibBuilder.importSymbols("CASA-MIB", "casa")
entPhysicalEntry, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalEntry")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
casaModuleCpuMemMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 20858, 10, 13))
if mibBuilder.loadTexts: casaModuleCpuMemMib.setLastUpdated('200809040922Z')
if mibBuilder.loadTexts: casaModuleCpuMemMib.setOrganization('Casa Systems Inc')
casaMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 20858, 10))
casaModuleCpuMemObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 20858, 10, 13, 1))
casaModuleCpuMemTable = MibTable((1, 3, 6, 1, 4, 1, 20858, 10, 13, 1, 1), )
if mibBuilder.loadTexts: casaModuleCpuMemTable.setStatus('current')
casaModuleCpuMemEntry = MibTableRow((1, 3, 6, 1, 4, 1, 20858, 10, 13, 1, 1, 1), )
entPhysicalEntry.registerAugmentions(("CASA-ENTITY-EXT-MIB", "casaModuleCpuMemEntry"))
casaModuleCpuMemEntry.setIndexNames(*entPhysicalEntry.getIndexNames())
if mibBuilder.loadTexts: casaModuleCpuMemEntry.setStatus('current')
casaModuleTotalAllocatableMem = MibTableColumn((1, 3, 6, 1, 4, 1, 20858, 10, 13, 1, 1, 1, 1), Unsigned32()).setUnits('KBytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: casaModuleTotalAllocatableMem.setStatus('current')
casaModuleTotalMemAllocated = MibTableColumn((1, 3, 6, 1, 4, 1, 20858, 10, 13, 1, 1, 1, 2), Unsigned32()).setUnits('KBytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: casaModuleTotalMemAllocated.setStatus('current')
casaModuleTotalFreeMem = MibTableColumn((1, 3, 6, 1, 4, 1, 20858, 10, 13, 1, 1, 1, 3), Unsigned32()).setUnits('KBytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: casaModuleTotalFreeMem.setStatus('current')
casaModuleTotalCpuUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 20858, 10, 13, 1, 1, 1, 4), Unsigned32()).setUnits('%').setMaxAccess("readonly")
if mibBuilder.loadTexts: casaModuleTotalCpuUtilization.setStatus('current')
casaCmtsCpuMemGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 20858, 10, 13, 2))
casaCmtsCpuMemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 20858, 10, 13, 2, 1)).setObjects(("CASA-ENTITY-EXT-MIB", "casaModuleTotalAllocatableMem"), ("CASA-ENTITY-EXT-MIB", "casaModuleTotalMemAllocated"), ("CASA-ENTITY-EXT-MIB", "casaModuleTotalFreeMem"), ("CASA-ENTITY-EXT-MIB", "casaModuleTotalCpuUtilization"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    casaCmtsCpuMemGroup = casaCmtsCpuMemGroup.setStatus('current')
casaCmtsCpuMemCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 20858, 10, 13, 3))
casaCmtsCpuMemCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 20858, 10, 13, 3, 1)).setObjects(("CASA-CABLE-CPUMEMINFO-MIB", "casaCmtsCpuMemGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    casaCmtsCpuMemCompliance = casaCmtsCpuMemCompliance.setStatus('current')
mibBuilder.exportSymbols("CASA-ENTITY-EXT-MIB", casaModuleCpuMemEntry=casaModuleCpuMemEntry, casaCmtsCpuMemCompliances=casaCmtsCpuMemCompliances, casaModuleCpuMemMib=casaModuleCpuMemMib, casaCmtsCpuMemCompliance=casaCmtsCpuMemCompliance, casaModuleTotalFreeMem=casaModuleTotalFreeMem, casaModuleTotalCpuUtilization=casaModuleTotalCpuUtilization, PYSNMP_MODULE_ID=casaModuleCpuMemMib, casaModuleCpuMemTable=casaModuleCpuMemTable, casaModuleTotalMemAllocated=casaModuleTotalMemAllocated, casaCmtsCpuMemGroups=casaCmtsCpuMemGroups, casaModuleCpuMemObjects=casaModuleCpuMemObjects, casaCmtsCpuMemGroup=casaCmtsCpuMemGroup, casaMgmt=casaMgmt, casaModuleTotalAllocatableMem=casaModuleTotalAllocatableMem)
