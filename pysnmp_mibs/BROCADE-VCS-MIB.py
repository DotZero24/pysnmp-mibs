#
# PySNMP MIB module BROCADE-VCS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/brocade/BROCADE-VCS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:06:47 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
bcsiModules, = mibBuilder.importSymbols("Brocade-REG-MIB", "bcsiModules")
FcWwn, = mibBuilder.importSymbols("Brocade-TC", "FcWwn")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, Unsigned32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "Unsigned32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
brocadeVcsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1588, 3, 1, 6))
brocadeVcsMIB.setRevisions(('2015-04-08 00:00',))
if mibBuilder.loadTexts: brocadeVcsMIB.setLastUpdated('201504080000Z')
if mibBuilder.loadTexts: brocadeVcsMIB.setOrganization('Brocade Communications Systems Inc.')
brocadeVcsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 1))
brocadeVcsMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 2))
class VcsConfigMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("local", 1), ("distributed", 2))

class VcsOperationMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("fabricCluster", 1), ("logicalChassis", 2))

class VcsIdentifier(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 8192)

class VcsRbridgeId(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 239)

class VcsClusterCondition(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("good", 1), ("degraded", 2), ("error", 3))

vcsConfigMode = MibScalar((1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 1, 1), VcsConfigMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcsConfigMode.setStatus('current')
vcsModeOfOperation = MibScalar((1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 1, 2), VcsOperationMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcsModeOfOperation.setStatus('current')
vcsIdentifier = MibScalar((1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 1, 3), VcsIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcsIdentifier.setStatus('current')
vcsVirtualIpV4Address = MibScalar((1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 1, 4), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcsVirtualIpV4Address.setStatus('current')
vcsVirtualIpV6Address = MibScalar((1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 1, 5), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcsVirtualIpV6Address.setStatus('current')
vcsVirtualIpAssociatedRbridgeId = MibScalar((1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 1, 6), VcsRbridgeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcsVirtualIpAssociatedRbridgeId.setStatus('current')
vcsVirtualIpInterfaceId = MibScalar((1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcsVirtualIpInterfaceId.setStatus('current')
vcsVirtualIpV4OperStatus = MibScalar((1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcsVirtualIpV4OperStatus.setStatus('current')
vcsVirtualIpV6OperStatus = MibScalar((1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcsVirtualIpV6OperStatus.setStatus('current')
vcsNumNodesInCluster = MibScalar((1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcsNumNodesInCluster.setStatus('current')
vcsClusterCondition = MibScalar((1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 1, 11), VcsClusterCondition()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcsClusterCondition.setStatus('current')
vcsFabricIslTable = MibTable((1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 1, 12), )
if mibBuilder.loadTexts: vcsFabricIslTable.setStatus('current')
vcsFabricIslEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 1, 12, 1), ).setIndexNames((0, "BROCADE-VCS-MIB", "vcsFabricIslIndex"))
if mibBuilder.loadTexts: vcsFabricIslEntry.setStatus('current')
vcsFabricIslIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 1, 12, 1, 1), Unsigned32())
if mibBuilder.loadTexts: vcsFabricIslIndex.setStatus('current')
vcsFabricIslIntfName = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 1, 12, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcsFabricIslIntfName.setStatus('current')
vcsFabricIslNbrIntfName = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 1, 12, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcsFabricIslNbrIntfName.setStatus('current')
vcsFabricIslNbrWWN = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 1, 12, 1, 4), FcWwn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcsFabricIslNbrWWN.setStatus('current')
vcsFabricIslNbrName = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 1, 12, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcsFabricIslNbrName.setStatus('current')
vcsFabricIslBW = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 1, 12, 1, 6), Unsigned32()).setUnits('megabytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: vcsFabricIslBW.setStatus('current')
vcsFabricIslIsTrunk = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 1, 12, 1, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcsFabricIslIsTrunk.setStatus('current')
brocadeVcsConformanceGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 2, 1))
brocadeVcsCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 2, 2))
brocadeVcsCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 2, 2, 1)).setObjects(("BROCADE-VCS-MIB", "brocadeVcsObjectsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    brocadeVcsCompliance = brocadeVcsCompliance.setStatus('current')
brocadeVcsObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 2, 1, 1)).setObjects(("BROCADE-VCS-MIB", "vcsConfigMode"), ("BROCADE-VCS-MIB", "vcsModeOfOperation"), ("BROCADE-VCS-MIB", "vcsIdentifier"), ("BROCADE-VCS-MIB", "vcsVirtualIpV4Address"), ("BROCADE-VCS-MIB", "vcsVirtualIpV6Address"), ("BROCADE-VCS-MIB", "vcsVirtualIpAssociatedRbridgeId"), ("BROCADE-VCS-MIB", "vcsVirtualIpInterfaceId"), ("BROCADE-VCS-MIB", "vcsVirtualIpV4OperStatus"), ("BROCADE-VCS-MIB", "vcsVirtualIpV6OperStatus"), ("BROCADE-VCS-MIB", "vcsNumNodesInCluster"), ("BROCADE-VCS-MIB", "vcsClusterCondition"), ("BROCADE-VCS-MIB", "vcsFabricIslIndex"), ("BROCADE-VCS-MIB", "vcsFabricIslIntfName"), ("BROCADE-VCS-MIB", "vcsFabricIslNbrIntfName"), ("BROCADE-VCS-MIB", "vcsFabricIslNbrWWN"), ("BROCADE-VCS-MIB", "vcsFabricIslNbrName"), ("BROCADE-VCS-MIB", "vcsFabricIslBW"), ("BROCADE-VCS-MIB", "vcsFabricIslIsTrunk"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    brocadeVcsObjectsGroup = brocadeVcsObjectsGroup.setStatus('current')
mibBuilder.exportSymbols("BROCADE-VCS-MIB", brocadeVcsObjectsGroup=brocadeVcsObjectsGroup, VcsIdentifier=VcsIdentifier, VcsConfigMode=VcsConfigMode, vcsFabricIslBW=vcsFabricIslBW, vcsFabricIslTable=vcsFabricIslTable, vcsFabricIslIntfName=vcsFabricIslIntfName, VcsOperationMode=VcsOperationMode, vcsVirtualIpV4OperStatus=vcsVirtualIpV4OperStatus, vcsNumNodesInCluster=vcsNumNodesInCluster, vcsConfigMode=vcsConfigMode, vcsVirtualIpV4Address=vcsVirtualIpV4Address, vcsFabricIslIsTrunk=vcsFabricIslIsTrunk, VcsClusterCondition=VcsClusterCondition, vcsClusterCondition=vcsClusterCondition, vcsFabricIslNbrIntfName=vcsFabricIslNbrIntfName, VcsRbridgeId=VcsRbridgeId, vcsFabricIslEntry=vcsFabricIslEntry, vcsModeOfOperation=vcsModeOfOperation, vcsIdentifier=vcsIdentifier, brocadeVcsCompliances=brocadeVcsCompliances, brocadeVcsMIBConformance=brocadeVcsMIBConformance, vcsVirtualIpV6OperStatus=vcsVirtualIpV6OperStatus, PYSNMP_MODULE_ID=brocadeVcsMIB, brocadeVcsCompliance=brocadeVcsCompliance, brocadeVcsMIB=brocadeVcsMIB, vcsFabricIslNbrName=vcsFabricIslNbrName, brocadeVcsMIBObjects=brocadeVcsMIBObjects, brocadeVcsConformanceGroups=brocadeVcsConformanceGroups, vcsVirtualIpV6Address=vcsVirtualIpV6Address, vcsVirtualIpAssociatedRbridgeId=vcsVirtualIpAssociatedRbridgeId, vcsFabricIslNbrWWN=vcsFabricIslNbrWWN, vcsVirtualIpInterfaceId=vcsVirtualIpInterfaceId, vcsFabricIslIndex=vcsFabricIslIndex)
