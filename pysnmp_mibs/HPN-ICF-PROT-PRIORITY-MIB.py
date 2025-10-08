#
# PySNMP MIB module HPN-ICF-PROT-PRIORITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hp/HPN-ICF-PROT-PRIORITY-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:09:10 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
hpnicfProtocolPriority = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 37))
hpnicfProtocolPriority.setRevisions(('2005-01-17 16:33',))
if mibBuilder.loadTexts: hpnicfProtocolPriority.setLastUpdated('200501171633Z')
if mibBuilder.loadTexts: hpnicfProtocolPriority.setOrganization('')
hpnicfProtocolPriorityObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 37, 1))
hpnicfPPri = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 37, 1, 1))
hpnicfProtocolPriorityTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 37, 1, 1, 1), )
if mibBuilder.loadTexts: hpnicfProtocolPriorityTable.setStatus('current')
hpnicfProtocolPriorityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 37, 1, 1, 1, 1), ).setIndexNames((0, "HPN-ICF-PROT-PRIORITY-MIB", "hpnicfPPriProtocolType"))
if mibBuilder.loadTexts: hpnicfProtocolPriorityEntry.setStatus('current')
hpnicfPPriProtocolType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 37, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("ospf", 1), ("telnet", 2), ("snmp", 3), ("icmp", 4), ("bgp", 5), ("ldp", 6))))
if mibBuilder.loadTexts: hpnicfPPriProtocolType.setStatus('current')
hpnicfPPriPriorityType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 37, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ipPrecedence", 1), ("dscp", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfPPriPriorityType.setStatus('current')
hpnicfPPriPriorityVlaue = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 37, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 63))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfPPriPriorityVlaue.setStatus('current')
hpnicfPPriRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 37, 1, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfPPriRowStatus.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-PROT-PRIORITY-MIB", hpnicfPPriPriorityVlaue=hpnicfPPriPriorityVlaue, hpnicfProtocolPriority=hpnicfProtocolPriority, hpnicfPPri=hpnicfPPri, hpnicfPPriProtocolType=hpnicfPPriProtocolType, hpnicfProtocolPriorityObjects=hpnicfProtocolPriorityObjects, hpnicfProtocolPriorityEntry=hpnicfProtocolPriorityEntry, hpnicfPPriPriorityType=hpnicfPPriPriorityType, hpnicfPPriRowStatus=hpnicfPPriRowStatus, hpnicfProtocolPriorityTable=hpnicfProtocolPriorityTable, PYSNMP_MODULE_ID=hpnicfProtocolPriority)
