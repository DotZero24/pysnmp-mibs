#
# PySNMP MIB module CAMBIUM-NETWORKS-IPV6-ND-RA-GUARD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cambium/CAMBIUM-NETWORKS-IPV6-ND-RA-GUARD-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:06:31 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
PortList, dot1qVlanStaticEntry, dot1qTpFdbPort, VlanIdOrNone, dot1qTpFdbEntry, dot1qStaticUnicastEntry = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList", "dot1qVlanStaticEntry", "dot1qTpFdbPort", "VlanIdOrNone", "dot1qTpFdbEntry", "dot1qStaticUnicastEntry")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, MacAddress, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "MacAddress", "TruthValue", "DisplayString")
cnRAGuardMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 17713, 24, 9))
cnRAGuardMib.setRevisions(('2021-11-28 00:00', '2021-04-09 00:00',))
if mibBuilder.loadTexts: cnRAGuardMib.setLastUpdated('202111280000Z')
if mibBuilder.loadTexts: cnRAGuardMib.setOrganization('Cambium Networks, Inc.')
class RAGuardPolicy(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("router", 0), ("host", 1))

cnRAGuardIfCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 17713, 24, 9, 1))
cnRAGuardIfCfgTable = MibTable((1, 3, 6, 1, 4, 1, 17713, 24, 9, 1, 1), )
if mibBuilder.loadTexts: cnRAGuardIfCfgTable.setStatus('current')
cnRAGuardIfCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 17713, 24, 9, 1, 1, 1), ).setIndexNames((0, "CAMBIUM-NETWORKS-IPV6-ND-RA-GUARD-MIB", "cnRAGuardIfCfgIfIndex"))
if mibBuilder.loadTexts: cnRAGuardIfCfgEntry.setStatus('current')
cnRAGuardIfCfgIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 24, 9, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 52)))
if mibBuilder.loadTexts: cnRAGuardIfCfgIfIndex.setStatus('current')
cnRAGuardIfCfgPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 24, 9, 1, 1, 1, 2), RAGuardPolicy().clone('router')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnRAGuardIfCfgPolicy.setStatus('current')
cnRAGuardIfCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 17713, 24, 9, 1, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnRAGuardIfCounter.setStatus('current')
mibBuilder.exportSymbols("CAMBIUM-NETWORKS-IPV6-ND-RA-GUARD-MIB", cnRAGuardIfCfgPolicy=cnRAGuardIfCfgPolicy, cnRAGuardIfCfgTable=cnRAGuardIfCfgTable, PYSNMP_MODULE_ID=cnRAGuardMib, cnRAGuardIfCounter=cnRAGuardIfCounter, cnRAGuardIfCfgEntry=cnRAGuardIfCfgEntry, cnRAGuardMib=cnRAGuardMib, RAGuardPolicy=RAGuardPolicy, cnRAGuardIfCfgIfIndex=cnRAGuardIfCfgIfIndex, cnRAGuardIfCfg=cnRAGuardIfCfg)
