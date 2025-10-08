#
# PySNMP MIB module HM2-PLATFORM-MRP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hirschmann/HM2-PLATFORM-MRP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:56:12 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hm2PlatformMibs, = mibBuilder.importSymbols("HM2-TC-MIB", "hm2PlatformMibs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TimeInterval, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TimeInterval", "TextualConvention", "DisplayString")
hm2PlatformMRP = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 12, 60))
hm2PlatformMRP.setRevisions(('2013-04-10 00:00',))
if mibBuilder.loadTexts: hm2PlatformMRP.setLastUpdated('201304100000Z')
if mibBuilder.loadTexts: hm2PlatformMRP.setOrganization('Hirschmann Automation and Control GmbH')
hm2AgentDot1qMrp = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 12, 60, 1))
hm2AgentDot1qMrpMxrp = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 12, 60, 2))
hm2AgentDot1qPortMrpTable = MibTable((1, 3, 6, 1, 4, 1, 248, 12, 60, 1, 1), )
if mibBuilder.loadTexts: hm2AgentDot1qPortMrpTable.setStatus('current')
hm2AgentDot1qPortMrpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 12, 60, 1, 1, 1), ).setIndexNames((0, "HM2-PLATFORM-MRP-MIB", "hm2AgentDot1qMrpPort"))
if mibBuilder.loadTexts: hm2AgentDot1qPortMrpEntry.setStatus('current')
hm2AgentDot1qMrpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 60, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: hm2AgentDot1qMrpPort.setStatus('current')
hm2AgentDot1qPortMrpJoinTime = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 60, 1, 1, 1, 2), TimeInterval().subtype(subtypeSpec=ValueRangeConstraint(10, 100)).clone(20)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentDot1qPortMrpJoinTime.setStatus('current')
hm2AgentDot1qPortMrpLeaveTime = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 60, 1, 1, 1, 3), TimeInterval().subtype(subtypeSpec=ValueRangeConstraint(20, 600)).clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentDot1qPortMrpLeaveTime.setStatus('current')
hm2AgentDot1qPortMrpLeaveAllTime = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 60, 1, 1, 1, 4), TimeInterval().subtype(subtypeSpec=ValueRangeConstraint(200, 6000)).clone(1000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentDot1qPortMrpLeaveAllTime.setStatus('current')
mibBuilder.exportSymbols("HM2-PLATFORM-MRP-MIB", hm2AgentDot1qPortMrpTable=hm2AgentDot1qPortMrpTable, hm2AgentDot1qPortMrpEntry=hm2AgentDot1qPortMrpEntry, hm2AgentDot1qMrpMxrp=hm2AgentDot1qMrpMxrp, hm2AgentDot1qMrp=hm2AgentDot1qMrp, hm2AgentDot1qPortMrpJoinTime=hm2AgentDot1qPortMrpJoinTime, hm2AgentDot1qPortMrpLeaveAllTime=hm2AgentDot1qPortMrpLeaveAllTime, hm2PlatformMRP=hm2PlatformMRP, hm2AgentDot1qMrpPort=hm2AgentDot1qMrpPort, PYSNMP_MODULE_ID=hm2PlatformMRP, hm2AgentDot1qPortMrpLeaveTime=hm2AgentDot1qPortMrpLeaveTime)
