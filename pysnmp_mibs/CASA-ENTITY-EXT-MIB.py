#
# PySNMP MIB module CASA-ENTITY-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/casa/CASA-ENTITY-EXT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:14:57 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
casa, = mibBuilder.importSymbols("CASA-MIB", "casa")
entPhysicalEntry, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalEntry")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("CASA-ENTITY-EXT-MIB", casaModuleTotalFreeMem=casaModuleTotalFreeMem, casaModuleTotalMemAllocated=casaModuleTotalMemAllocated, casaModuleCpuMemMib=casaModuleCpuMemMib, casaCmtsCpuMemGroups=casaCmtsCpuMemGroups, casaCmtsCpuMemGroup=casaCmtsCpuMemGroup, casaModuleCpuMemTable=casaModuleCpuMemTable, casaModuleCpuMemEntry=casaModuleCpuMemEntry, casaModuleCpuMemObjects=casaModuleCpuMemObjects, casaMgmt=casaMgmt, casaCmtsCpuMemCompliances=casaCmtsCpuMemCompliances, casaModuleTotalAllocatableMem=casaModuleTotalAllocatableMem, casaCmtsCpuMemCompliance=casaCmtsCpuMemCompliance, PYSNMP_MODULE_ID=casaModuleCpuMemMib, casaModuleTotalCpuUtilization=casaModuleTotalCpuUtilization)
