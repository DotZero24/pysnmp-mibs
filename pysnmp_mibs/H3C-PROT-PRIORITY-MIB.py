#
# PySNMP MIB module H3C-PROT-PRIORITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/h3c/H3C-PROT-PRIORITY-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:10:18 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
h3cProtocolPriority = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 37))
h3cProtocolPriority.setRevisions(('2005-01-17 16:33',))
if mibBuilder.loadTexts: h3cProtocolPriority.setLastUpdated('200501171633Z')
if mibBuilder.loadTexts: h3cProtocolPriority.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
h3cProtocolPriorityObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 37, 1))
h3cPPri = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 37, 1, 1))
h3cProtocolPriorityTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 37, 1, 1, 1), )
if mibBuilder.loadTexts: h3cProtocolPriorityTable.setStatus('current')
h3cProtocolPriorityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 37, 1, 1, 1, 1), ).setIndexNames((0, "H3C-PROT-PRIORITY-MIB", "h3cPPriProtocolType"))
if mibBuilder.loadTexts: h3cProtocolPriorityEntry.setStatus('current')
h3cPPriProtocolType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 37, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("ospf", 1), ("telnet", 2), ("snmp", 3), ("icmp", 4), ("bgp", 5), ("ldp", 6))))
if mibBuilder.loadTexts: h3cPPriProtocolType.setStatus('current')
h3cPPriPriorityType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 37, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ipPrecedence", 1), ("dscp", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cPPriPriorityType.setStatus('current')
h3cPPriPriorityVlaue = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 37, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 63))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cPPriPriorityVlaue.setStatus('current')
h3cPPriRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 37, 1, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cPPriRowStatus.setStatus('current')
mibBuilder.exportSymbols("H3C-PROT-PRIORITY-MIB", h3cPPriPriorityType=h3cPPriPriorityType, h3cPPriPriorityVlaue=h3cPPriPriorityVlaue, h3cProtocolPriorityEntry=h3cProtocolPriorityEntry, h3cProtocolPriority=h3cProtocolPriority, h3cPPriRowStatus=h3cPPriRowStatus, h3cProtocolPriorityObjects=h3cProtocolPriorityObjects, h3cProtocolPriorityTable=h3cProtocolPriorityTable, PYSNMP_MODULE_ID=h3cProtocolPriority, h3cPPriProtocolType=h3cPPriProtocolType, h3cPPri=h3cPPri)
