#
# PySNMP MIB module LANCOM-ACL-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/lancom/LANCOM-ACL-MGMT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:43:25 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
fastPath, = mibBuilder.importSymbols("LANCOM-REF-MIB", "fastPath")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "RowStatus", "TextualConvention")
aclMgmtGroup = ModuleIdentity((1, 3, 6, 1, 4, 1, 2356, 16, 1, 62))
aclMgmtGroup.setRevisions(('2015-12-11 00:00',))
if mibBuilder.loadTexts: aclMgmtGroup.setLastUpdated('201512110000Z')
if mibBuilder.loadTexts: aclMgmtGroup.setOrganization('Broadcom ')
class AclMgmtServiceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("allType", 0), ("telnet", 1), ("http", 2), ("https", 3), ("snmp", 4), ("ssh", 5), ("tftp", 6), ("sntp", 7))

class AclMgmtActionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("permit", 0), ("deny", 1))

aclMgmtEnable = MibScalar((1, 3, 6, 1, 4, 1, 2356, 16, 1, 62, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aclMgmtEnable.setStatus('current')
aclMgmtActiveListName = MibScalar((1, 3, 6, 1, 4, 1, 2356, 16, 1, 62, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aclMgmtActiveListName.setStatus('current')
aclMgmtListTable = MibTable((1, 3, 6, 1, 4, 1, 2356, 16, 1, 62, 3), )
if mibBuilder.loadTexts: aclMgmtListTable.setStatus('current')
aclMgmtListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2356, 16, 1, 62, 3, 1), ).setIndexNames((0, "LANCOM-ACL-MGMT-MIB", "aclMgmtListName"), (0, "LANCOM-ACL-MGMT-MIB", "aclMgmtListPriority"))
if mibBuilder.loadTexts: aclMgmtListEntry.setStatus('current')
aclMgmtListName = MibTableColumn((1, 3, 6, 1, 4, 1, 2356, 16, 1, 62, 3, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aclMgmtListName.setStatus('current')
aclMgmtListPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2356, 16, 1, 62, 3, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aclMgmtListPriority.setStatus('current')
aclMgmtListIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2356, 16, 1, 62, 3, 1, 3), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aclMgmtListIfIndex.setStatus('current')
aclMgmtListIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2356, 16, 1, 62, 3, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aclMgmtListIpAddr.setStatus('current')
aclMgmtListIpNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 2356, 16, 1, 62, 3, 1, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aclMgmtListIpNetMask.setStatus('current')
aclMgmtListService = MibTableColumn((1, 3, 6, 1, 4, 1, 2356, 16, 1, 62, 3, 1, 6), AclMgmtServiceType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aclMgmtListService.setStatus('current')
aclMgmtListAction = MibTableColumn((1, 3, 6, 1, 4, 1, 2356, 16, 1, 62, 3, 1, 7), AclMgmtActionType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aclMgmtListAction.setStatus('current')
aclMgmtListRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2356, 16, 1, 62, 3, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aclMgmtListRowStatus.setStatus('current')
aclMgmtListVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 2356, 16, 1, 62, 3, 1, 9), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aclMgmtListVlanId.setStatus('current')
aclRuleIsConflict = MibTableColumn((1, 3, 6, 1, 4, 1, 2356, 16, 1, 62, 3, 1, 10), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aclRuleIsConflict.setStatus('current')
aclMgmtTrapInfo = NotificationType((1, 3, 6, 1, 4, 1, 2356, 16, 1, 62, 4)).setObjects(("LANCOM-ACL-MGMT-MIB", "aclMgmtTrapReason"))
if mibBuilder.loadTexts: aclMgmtTrapInfo.setStatus('current')
aclMgmtTrapReason = MibScalar((1, 3, 6, 1, 4, 1, 2356, 16, 1, 62, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aclMgmtTrapReason.setStatus('current')
mibBuilder.exportSymbols("LANCOM-ACL-MGMT-MIB", aclMgmtListIpNetMask=aclMgmtListIpNetMask, aclMgmtTrapReason=aclMgmtTrapReason, aclMgmtTrapInfo=aclMgmtTrapInfo, aclMgmtListName=aclMgmtListName, aclMgmtListRowStatus=aclMgmtListRowStatus, aclMgmtListPriority=aclMgmtListPriority, aclMgmtListIfIndex=aclMgmtListIfIndex, aclMgmtGroup=aclMgmtGroup, aclMgmtListIpAddr=aclMgmtListIpAddr, aclMgmtActiveListName=aclMgmtActiveListName, aclMgmtListVlanId=aclMgmtListVlanId, aclMgmtListAction=aclMgmtListAction, aclMgmtEnable=aclMgmtEnable, AclMgmtServiceType=AclMgmtServiceType, aclMgmtListEntry=aclMgmtListEntry, aclRuleIsConflict=aclRuleIsConflict, AclMgmtActionType=AclMgmtActionType, aclMgmtListTable=aclMgmtListTable, aclMgmtListService=aclMgmtListService, PYSNMP_MODULE_ID=aclMgmtGroup)
