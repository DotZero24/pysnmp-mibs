#
# PySNMP MIB module HPN-ICF-PROT-PRIORITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hp/HPN-ICF-PROT-PRIORITY-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:03:02 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
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
mibBuilder.exportSymbols("HPN-ICF-PROT-PRIORITY-MIB", hpnicfPPriPriorityVlaue=hpnicfPPriPriorityVlaue, PYSNMP_MODULE_ID=hpnicfProtocolPriority, hpnicfPPriRowStatus=hpnicfPPriRowStatus, hpnicfPPriProtocolType=hpnicfPPriProtocolType, hpnicfPPri=hpnicfPPri, hpnicfProtocolPriorityEntry=hpnicfProtocolPriorityEntry, hpnicfPPriPriorityType=hpnicfPPriPriorityType, hpnicfProtocolPriorityTable=hpnicfProtocolPriorityTable, hpnicfProtocolPriority=hpnicfProtocolPriority, hpnicfProtocolPriorityObjects=hpnicfProtocolPriorityObjects)
