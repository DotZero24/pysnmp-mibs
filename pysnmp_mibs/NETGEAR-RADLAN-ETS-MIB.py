#
# PySNMP MIB module NETGEAR-RADLAN-ETS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/netgear/NETGEAR-RADLAN-ETS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:50:41 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
InterfaceIndexOrZero, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "InterfaceIndex")
Percents, rnd = mibBuilder.importSymbols("NETGEAR-RADLAN-MIB", "Percents", "rnd")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, RowPointer, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "RowPointer", "TruthValue", "DisplayString")
rlEtsMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 4526, 17, 201))
if mibBuilder.loadTexts: rlEtsMib.setLastUpdated('201003210000Z')
if mibBuilder.loadTexts: rlEtsMib.setOrganization('Marvell Computer Communications Ltd.')
class EtsPriorityGroupType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 15))
    namedValues = NamedValues(("priorityGroup0", 0), ("priorityGroup1", 1), ("priorityGroup2", 2), ("priorityGroup3", 3), ("priorityGroup4", 4), ("priorityGroup5", 5), ("priorityGroup6", 6), ("priorityGroup7", 7), ("priorityGroup15", 15))

class EtsAdminStatusReasonType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("ok", 1), ("too-many-groups", 2), ("too-many-queues", 3), ("not-highest-queue", 4))

rlEtsFeatureStatus = MibScalar((1, 3, 6, 1, 4, 1, 4526, 17, 201, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlEtsFeatureStatus.setStatus('current')
rlEtsPriorityGroupMappingTable = MibTable((1, 3, 6, 1, 4, 1, 4526, 17, 201, 2), )
if mibBuilder.loadTexts: rlEtsPriorityGroupMappingTable.setStatus('current')
rlEtsPriorityGroupMappingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4526, 17, 201, 2, 1), ).setIndexNames((0, "NETGEAR-RADLAN-ETS-MIB", "rlEtsPriorityGroupMapping8021QPrio"))
if mibBuilder.loadTexts: rlEtsPriorityGroupMappingEntry.setStatus('current')
rlEtsPriorityGroupMapping8021QPrio = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 17, 201, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)))
if mibBuilder.loadTexts: rlEtsPriorityGroupMapping8021QPrio.setStatus('current')
rlEtsPriorityGroupMappingAdminPG = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 17, 201, 2, 1, 2), EtsPriorityGroupType().clone('priorityGroup15')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlEtsPriorityGroupMappingAdminPG.setStatus('current')
rlEtsPriorityGroupMappingOperPG = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 17, 201, 2, 1, 3), EtsPriorityGroupType().clone('priorityGroup15')).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlEtsPriorityGroupMappingOperPG.setStatus('current')
rlEtsPriorityGroupMappingStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 17, 201, 2, 1, 4), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlEtsPriorityGroupMappingStatus.setStatus('current')
rlEtsPriorityGroupMappingProblemReason = MibScalar((1, 3, 6, 1, 4, 1, 4526, 17, 201, 3), EtsAdminStatusReasonType().clone('ok')).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlEtsPriorityGroupMappingProblemReason.setStatus('current')
rlEtsPriorityGroupMappingProblemIndex = MibScalar((1, 3, 6, 1, 4, 1, 4526, 17, 201, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlEtsPriorityGroupMappingProblemIndex.setStatus('current')
rlEtsPriorityGroupBwAlloc = MibScalar((1, 3, 6, 1, 4, 1, 4526, 17, 201, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlEtsPriorityGroupBwAlloc.setStatus('current')
mibBuilder.exportSymbols("NETGEAR-RADLAN-ETS-MIB", rlEtsPriorityGroupMappingEntry=rlEtsPriorityGroupMappingEntry, rlEtsPriorityGroupMappingAdminPG=rlEtsPriorityGroupMappingAdminPG, rlEtsPriorityGroupMappingStatus=rlEtsPriorityGroupMappingStatus, rlEtsPriorityGroupMappingProblemIndex=rlEtsPriorityGroupMappingProblemIndex, rlEtsPriorityGroupMappingProblemReason=rlEtsPriorityGroupMappingProblemReason, rlEtsPriorityGroupBwAlloc=rlEtsPriorityGroupBwAlloc, EtsPriorityGroupType=EtsPriorityGroupType, EtsAdminStatusReasonType=EtsAdminStatusReasonType, rlEtsPriorityGroupMapping8021QPrio=rlEtsPriorityGroupMapping8021QPrio, rlEtsFeatureStatus=rlEtsFeatureStatus, rlEtsPriorityGroupMappingTable=rlEtsPriorityGroupMappingTable, PYSNMP_MODULE_ID=rlEtsMib, rlEtsPriorityGroupMappingOperPG=rlEtsPriorityGroupMappingOperPG, rlEtsMib=rlEtsMib)
