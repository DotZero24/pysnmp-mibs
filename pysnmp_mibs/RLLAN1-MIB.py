#
# PySNMP MIB module RLLAN1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/radlan/RLLAN1-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:40:26 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
VlanId, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, MacAddress, RowStatus, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "RowStatus", "TruthValue", "TextualConvention")
rlLan1 = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 224))
rlLan1.setRevisions(('2015-06-30 00:00',))
if mibBuilder.loadTexts: rlLan1.setLastUpdated('201506300000Z')
if mibBuilder.loadTexts: rlLan1.setOrganization('MARVELL')
class GroupId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 1279)

class GroupIdList(TextualConvention, OctetString):
    status = 'current'

class VlanIdOrNone(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4094)

rlLan1STagEtherType = MibScalar((1, 3, 6, 1, 4, 1, 89, 224, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2).clone(hexValue="88A8")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLan1STagEtherType.setStatus('current')
rlLan1CPVlanId = MibScalar((1, 3, 6, 1, 4, 1, 89, 224, 2), VlanIdOrNone()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLan1CPVlanId.setStatus('current')
rlLan1CPVlanCos = MibScalar((1, 3, 6, 1, 4, 1, 89, 224, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLan1CPVlanCos.setStatus('current')
rlLan1x86Port = MibScalar((1, 3, 6, 1, 4, 1, 89, 224, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLan1x86Port.setStatus('current')
rlLan1CPVlanMulticastMappingVlanId = MibScalar((1, 3, 6, 1, 4, 1, 89, 224, 5), VlanIdOrNone()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLan1CPVlanMulticastMappingVlanId.setStatus('current')
rlLan1NonCPVlanMulticastMappingVlanId = MibScalar((1, 3, 6, 1, 4, 1, 89, 224, 6), VlanIdOrNone()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLan1NonCPVlanMulticastMappingVlanId.setStatus('current')
rlLan1x86VlanMappingTable = MibTable((1, 3, 6, 1, 4, 1, 89, 224, 7), )
if mibBuilder.loadTexts: rlLan1x86VlanMappingTable.setStatus('current')
rlLan1x86VlanMappingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 224, 7, 1), ).setIndexNames((0, "RLLAN1-MIB", "rlLan1x86VlanMappingVlanId"))
if mibBuilder.loadTexts: rlLan1x86VlanMappingEntry.setStatus('current')
rlLan1x86VlanMappingVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 224, 7, 1, 1), VlanId())
if mibBuilder.loadTexts: rlLan1x86VlanMappingVlanId.setStatus('current')
rlLan1x86VlanMappingGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 224, 7, 1, 2), GroupId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLan1x86VlanMappingGroupId.setStatus('current')
rlLan1x86VlanMappingRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 224, 7, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlLan1x86VlanMappingRowStatus.setStatus('current')
rlLan1x86MacMappingTable = MibTable((1, 3, 6, 1, 4, 1, 89, 224, 8), )
if mibBuilder.loadTexts: rlLan1x86MacMappingTable.setStatus('current')
rlLan1x86MacMappingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 224, 8, 1), ).setIndexNames((0, "RLLAN1-MIB", "rlLan1x86MacMappingDstMacAddress"))
if mibBuilder.loadTexts: rlLan1x86MacMappingEntry.setStatus('current')
rlLan1x86MacMappingDstMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 224, 8, 1, 1), MacAddress())
if mibBuilder.loadTexts: rlLan1x86MacMappingDstMacAddress.setStatus('current')
rlLan1x86MacMappingVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 224, 8, 1, 2), VlanId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLan1x86MacMappingVlanId.setStatus('current')
rlLan1x86MacMappingRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 224, 8, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlLan1x86MacMappingRowStatus.setStatus('current')
rlLan1x86ModulePortTable = MibTable((1, 3, 6, 1, 4, 1, 89, 224, 9), )
if mibBuilder.loadTexts: rlLan1x86ModulePortTable.setStatus('current')
rlLan1x86ModulePortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 224, 9, 1), ).setIndexNames((0, "RLLAN1-MIB", "rlLan1x86ModulePortIfIndex"))
if mibBuilder.loadTexts: rlLan1x86ModulePortEntry.setStatus('current')
rlLan1x86ModulePortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 224, 9, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000)))
if mibBuilder.loadTexts: rlLan1x86ModulePortIfIndex.setStatus('current')
rlLan1x86ModulePortCPAllowed = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 224, 9, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLan1x86ModulePortCPAllowed.setStatus('current')
rlLan1x86ModulePortCPUntaggedAllowed = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 224, 9, 1, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLan1x86ModulePortCPUntaggedAllowed.setStatus('current')
rlLan1x86ModulePortMulticastBroadcastAllowedVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 224, 9, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("cp", 2), ("noncp", 3))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLan1x86ModulePortMulticastBroadcastAllowedVlan.setStatus('current')
rlLan1x86ModulePortIngressGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 224, 9, 1, 5), GroupId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLan1x86ModulePortIngressGroupId.setStatus('current')
rlLan1x86ModulePortEgressGroupIdList = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 224, 9, 1, 6), GroupIdList().clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLan1x86ModulePortEgressGroupIdList.setStatus('current')
mibBuilder.exportSymbols("RLLAN1-MIB", rlLan1CPVlanMulticastMappingVlanId=rlLan1CPVlanMulticastMappingVlanId, rlLan1x86ModulePortEntry=rlLan1x86ModulePortEntry, rlLan1x86ModulePortIngressGroupId=rlLan1x86ModulePortIngressGroupId, rlLan1x86VlanMappingGroupId=rlLan1x86VlanMappingGroupId, rlLan1STagEtherType=rlLan1STagEtherType, rlLan1x86VlanMappingRowStatus=rlLan1x86VlanMappingRowStatus, rlLan1x86ModulePortIfIndex=rlLan1x86ModulePortIfIndex, rlLan1x86MacMappingDstMacAddress=rlLan1x86MacMappingDstMacAddress, GroupIdList=GroupIdList, rlLan1CPVlanId=rlLan1CPVlanId, rlLan1x86MacMappingEntry=rlLan1x86MacMappingEntry, rlLan1x86MacMappingRowStatus=rlLan1x86MacMappingRowStatus, rlLan1CPVlanCos=rlLan1CPVlanCos, rlLan1=rlLan1, rlLan1x86ModulePortMulticastBroadcastAllowedVlan=rlLan1x86ModulePortMulticastBroadcastAllowedVlan, rlLan1x86ModulePortEgressGroupIdList=rlLan1x86ModulePortEgressGroupIdList, rlLan1x86Port=rlLan1x86Port, rlLan1x86ModulePortTable=rlLan1x86ModulePortTable, rlLan1x86MacMappingTable=rlLan1x86MacMappingTable, VlanIdOrNone=VlanIdOrNone, rlLan1x86MacMappingVlanId=rlLan1x86MacMappingVlanId, PYSNMP_MODULE_ID=rlLan1, rlLan1NonCPVlanMulticastMappingVlanId=rlLan1NonCPVlanMulticastMappingVlanId, rlLan1x86ModulePortCPAllowed=rlLan1x86ModulePortCPAllowed, GroupId=GroupId, rlLan1x86VlanMappingTable=rlLan1x86VlanMappingTable, rlLan1x86VlanMappingEntry=rlLan1x86VlanMappingEntry, rlLan1x86ModulePortCPUntaggedAllowed=rlLan1x86ModulePortCPUntaggedAllowed, rlLan1x86VlanMappingVlanId=rlLan1x86VlanMappingVlanId)
