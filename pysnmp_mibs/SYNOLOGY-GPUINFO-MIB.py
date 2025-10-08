#
# PySNMP MIB module SYNOLOGY-GPUINFO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/synology/SYNOLOGY-GPUINFO-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:56:30 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Integer32, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Counter64, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Counter64", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
gpuInfo = ModuleIdentity((1, 3, 6, 1, 4, 1, 6574, 108))
gpuInfo.setRevisions(('2018-12-03 00:00',))
if mibBuilder.loadTexts: gpuInfo.setLastUpdated('201812030000Z')
if mibBuilder.loadTexts: gpuInfo.setOrganization('www.synology.com')
synology = MibIdentifier((1, 3, 6, 1, 4, 1, 6574))
gpuInfoSupported = MibScalar((1, 3, 6, 1, 4, 1, 6574, 108, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gpuInfoSupported.setStatus('current')
gpuUtilization = MibScalar((1, 3, 6, 1, 4, 1, 6574, 108, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gpuUtilization.setStatus('current')
gpuMemoryUtilization = MibScalar((1, 3, 6, 1, 4, 1, 6574, 108, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gpuMemoryUtilization.setStatus('current')
gpuMemoryFree = MibScalar((1, 3, 6, 1, 4, 1, 6574, 108, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gpuMemoryFree.setStatus('current')
gpuMemoryUsed = MibScalar((1, 3, 6, 1, 4, 1, 6574, 108, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gpuMemoryUsed.setStatus('current')
gpuMemoryTotal = MibScalar((1, 3, 6, 1, 4, 1, 6574, 108, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gpuMemoryTotal.setStatus('current')
gpuInfoConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 108, 7))
gpuInfoCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 108, 7, 1))
gpuInfoGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 108, 7, 2))
gpuInfoCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6574, 108, 7, 1, 1)).setObjects(("SYNOLOGY-GPUINFO-MIB", "gpuInfoGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    gpuInfoCompliance = gpuInfoCompliance.setStatus('current')
gpuInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6574, 108, 7, 2, 1)).setObjects(("SYNOLOGY-GPUINFO-MIB", "gpuInfoSupported"), ("SYNOLOGY-GPUINFO-MIB", "gpuUtilization"), ("SYNOLOGY-GPUINFO-MIB", "gpuMemoryUtilization"), ("SYNOLOGY-GPUINFO-MIB", "gpuMemoryFree"), ("SYNOLOGY-GPUINFO-MIB", "gpuMemoryUsed"), ("SYNOLOGY-GPUINFO-MIB", "gpuMemoryTotal"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    gpuInfoGroup = gpuInfoGroup.setStatus('current')
mibBuilder.exportSymbols("SYNOLOGY-GPUINFO-MIB", gpuInfoConformance=gpuInfoConformance, gpuInfoGroup=gpuInfoGroup, gpuUtilization=gpuUtilization, PYSNMP_MODULE_ID=gpuInfo, gpuInfoGroups=gpuInfoGroups, gpuMemoryUsed=gpuMemoryUsed, gpuMemoryFree=gpuMemoryFree, gpuInfo=gpuInfo, gpuInfoCompliances=gpuInfoCompliances, gpuMemoryUtilization=gpuMemoryUtilization, gpuInfoSupported=gpuInfoSupported, gpuInfoCompliance=gpuInfoCompliance, gpuMemoryTotal=gpuMemoryTotal, synology=synology)
