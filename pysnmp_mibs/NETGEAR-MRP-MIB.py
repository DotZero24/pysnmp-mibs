#
# PySNMP MIB module NETGEAR-MRP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/netgear/NETGEAR-MRP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:28:37 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ng7000managedswitch, = mibBuilder.importSymbols("NETGEAR-REF-MIB", "ng7000managedswitch")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Integer32, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Counter64, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Counter64", "Bits", "TimeTicks", "IpAddress")
DisplayString, MacAddress, TimeInterval, RowStatus, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TimeInterval", "RowStatus", "TruthValue", "TextualConvention")
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
mibBuilder.exportSymbols("NETGEAR-MRP-MIB", agentDot1qMrpPort=agentDot1qMrpPort, agentDot1qPortMrpJoinTime=agentDot1qPortMrpJoinTime, fastPathMRP=fastPathMRP, agentDot1qPortMrpLeaveAllTime=agentDot1qPortMrpLeaveAllTime, agentDot1qPortMrpTable=agentDot1qPortMrpTable, agentDot1qPortMrpLeaveTime=agentDot1qPortMrpLeaveTime, agentDot1qMrpMxrp=agentDot1qMrpMxrp, agentDot1qMrp=agentDot1qMrp, agentDot1qPortMrpEntry=agentDot1qPortMrpEntry, PYSNMP_MODULE_ID=fastPathMRP)
