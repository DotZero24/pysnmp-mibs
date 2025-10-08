#
# PySNMP MIB module NETGEAR-MRP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/netgear/NETGEAR-MRP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:51:28 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ng7000managedswitch, = mibBuilder.importSymbols("NETGEAR-REF-MIB", "ng7000managedswitch")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, Counter64, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "Counter64", "TimeTicks", "Gauge32")
RowStatus, TextualConvention, TimeInterval, MacAddress, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "TimeInterval", "MacAddress", "TruthValue", "DisplayString")
fastPathMRP = ModuleIdentity((1, 3, 6, 1, 4, 1, 4526, 10, 60))
fastPathMRP.setRevisions(('2011-04-29 00:00', '2011-01-26 00:00', '2010-10-31 00:00',))
if mibBuilder.loadTexts: fastPathMRP.setLastUpdated('201104290000Z')
if mibBuilder.loadTexts: fastPathMRP.setOrganization('Netgear Inc')
agentDot1qMrp = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 10, 60, 1))
agentDot1qMrpMxrp = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 10, 60, 2))
agentDot1qPortMrpTable = MibTable((1, 3, 6, 1, 4, 1, 4526, 10, 60, 1, 1), )
if mibBuilder.loadTexts: agentDot1qPortMrpTable.setStatus('current')
agentDot1qPortMrpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4526, 10, 60, 1, 1, 1), ).setIndexNames((0, "NETGEAR-MRP-MIB", "agentDot1qMrpPort"))
if mibBuilder.loadTexts: agentDot1qPortMrpEntry.setStatus('current')
agentDot1qMrpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 10, 60, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: agentDot1qMrpPort.setStatus('current')
agentDot1qPortMrpJoinTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 10, 60, 1, 1, 1, 2), TimeInterval().clone(20)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDot1qPortMrpJoinTime.setStatus('current')
agentDot1qPortMrpLeaveTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 10, 60, 1, 1, 1, 3), TimeInterval().clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDot1qPortMrpLeaveTime.setStatus('current')
agentDot1qPortMrpLeaveAllTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 10, 60, 1, 1, 1, 4), TimeInterval().clone(1000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDot1qPortMrpLeaveAllTime.setStatus('current')
mibBuilder.exportSymbols("NETGEAR-MRP-MIB", agentDot1qMrpMxrp=agentDot1qMrpMxrp, agentDot1qPortMrpLeaveTime=agentDot1qPortMrpLeaveTime, agentDot1qPortMrpLeaveAllTime=agentDot1qPortMrpLeaveAllTime, PYSNMP_MODULE_ID=fastPathMRP, agentDot1qPortMrpTable=agentDot1qPortMrpTable, agentDot1qMrp=agentDot1qMrp, fastPathMRP=fastPathMRP, agentDot1qPortMrpEntry=agentDot1qPortMrpEntry, agentDot1qMrpPort=agentDot1qMrpPort, agentDot1qPortMrpJoinTime=agentDot1qPortMrpJoinTime)
