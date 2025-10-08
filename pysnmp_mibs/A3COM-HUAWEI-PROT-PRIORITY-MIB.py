#
# PySNMP MIB module A3COM-HUAWEI-PROT-PRIORITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/a3com/A3COM-HUAWEI-PROT-PRIORITY-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:33:26 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
h3cCommon, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cCommon")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
h3cProtocolPriority = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 37))
h3cProtocolPriority.setRevisions(('2005-01-17 16:33',))
if mibBuilder.loadTexts: h3cProtocolPriority.setLastUpdated('200501171633Z')
if mibBuilder.loadTexts: h3cProtocolPriority.setOrganization('Huawei 3Com Technologies Co., Ltd.')
h3cProtocolPriorityObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 37, 1))
h3cPPri = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 37, 1, 1))
h3cProtocolPriorityTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 37, 1, 1, 1), )
if mibBuilder.loadTexts: h3cProtocolPriorityTable.setStatus('current')
h3cProtocolPriorityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 37, 1, 1, 1, 1), ).setIndexNames((0, "A3COM-HUAWEI-PROT-PRIORITY-MIB", "h3cPPriProtocolType"))
if mibBuilder.loadTexts: h3cProtocolPriorityEntry.setStatus('current')
h3cPPriProtocolType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 37, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("ospf", 1), ("telnet", 2), ("snmp", 3), ("icmp", 4), ("bgp", 5), ("ldp", 6))))
if mibBuilder.loadTexts: h3cPPriProtocolType.setStatus('current')
h3cPPriPriorityType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 37, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ipPrecedence", 1), ("dscp", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cPPriPriorityType.setStatus('current')
h3cPPriPriorityVlaue = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 37, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 63))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cPPriPriorityVlaue.setStatus('current')
h3cPPriRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 37, 1, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cPPriRowStatus.setStatus('current')
mibBuilder.exportSymbols("A3COM-HUAWEI-PROT-PRIORITY-MIB", h3cProtocolPriorityEntry=h3cProtocolPriorityEntry, h3cProtocolPriorityTable=h3cProtocolPriorityTable, h3cProtocolPriorityObjects=h3cProtocolPriorityObjects, h3cPPriPriorityType=h3cPPriPriorityType, h3cProtocolPriority=h3cProtocolPriority, h3cPPri=h3cPPri, h3cPPriProtocolType=h3cPPriProtocolType, h3cPPriRowStatus=h3cPPriRowStatus, h3cPPriPriorityVlaue=h3cPPriPriorityVlaue, PYSNMP_MODULE_ID=h3cProtocolPriority)
