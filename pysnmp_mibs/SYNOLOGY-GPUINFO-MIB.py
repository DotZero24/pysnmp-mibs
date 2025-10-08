#
# PySNMP MIB module SYNOLOGY-GPUINFO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/synology/SYNOLOGY-GPUINFO-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:56:53 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, enterprises, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, Counter64, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "Counter64", "TimeTicks", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("SYNOLOGY-GPUINFO-MIB", PYSNMP_MODULE_ID=gpuInfo, gpuInfo=gpuInfo, gpuInfoGroups=gpuInfoGroups, gpuMemoryUsed=gpuMemoryUsed, gpuInfoGroup=gpuInfoGroup, gpuInfoSupported=gpuInfoSupported, synology=synology, gpuUtilization=gpuUtilization, gpuInfoCompliance=gpuInfoCompliance, gpuInfoCompliances=gpuInfoCompliances, gpuMemoryTotal=gpuMemoryTotal, gpuMemoryUtilization=gpuMemoryUtilization, gpuMemoryFree=gpuMemoryFree, gpuInfoConformance=gpuInfoConformance)
