#
# PySNMP MIB module CAMBIUM-NETWORKS-IPV6-ND-RA-GUARD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cambium/CAMBIUM-NETWORKS-IPV6-ND-RA-GUARD-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:39:48 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dot1qTpFdbPort, dot1qStaticUnicastEntry, dot1qTpFdbEntry, PortList, VlanIdOrNone, dot1qVlanStaticEntry = mibBuilder.importSymbols("Q-BRIDGE-MIB", "dot1qTpFdbPort", "dot1qStaticUnicastEntry", "dot1qTpFdbEntry", "PortList", "VlanIdOrNone", "dot1qVlanStaticEntry")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter32, iso, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter32", "iso", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, MacAddress, RowStatus, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "RowStatus", "TruthValue", "TextualConvention")
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
mibBuilder.exportSymbols("CAMBIUM-NETWORKS-IPV6-ND-RA-GUARD-MIB", cnRAGuardIfCfgEntry=cnRAGuardIfCfgEntry, cnRAGuardIfCfgPolicy=cnRAGuardIfCfgPolicy, PYSNMP_MODULE_ID=cnRAGuardMib, cnRAGuardIfCfgIfIndex=cnRAGuardIfCfgIfIndex, cnRAGuardIfCounter=cnRAGuardIfCounter, RAGuardPolicy=RAGuardPolicy, cnRAGuardIfCfg=cnRAGuardIfCfg, cnRAGuardMib=cnRAGuardMib, cnRAGuardIfCfgTable=cnRAGuardIfCfgTable)
