#
# PySNMP MIB module CAMBIUM-NETWORKS-DYNAMIC-ARP-INSPECTION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cambium/CAMBIUM-NETWORKS-DYNAMIC-ARP-INSPECTION-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:39:45 2025
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
cnDaiMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2076, 110))
cnDaiMib.setRevisions(('2022-02-17 00:00', '2019-03-07 00:00',))
if mibBuilder.loadTexts: cnDaiMib.setLastUpdated('202202170000Z')
if mibBuilder.loadTexts: cnDaiMib.setOrganization('Cambium Networks, Inc.')
class TrustState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("untrusted", 0), ("trusted", 1))

class VlanId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 4094)

class AdminStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

cnDaiGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 2076, 110, 1))
cnDaiVlanCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 2076, 110, 2))
cnDaiIfCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 2076, 110, 3))
cnDaiDebugFlag = MibScalar((1, 3, 6, 1, 4, 1, 2076, 110, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnDaiDebugFlag.setStatus('current')
cnDaiVlanCfgTable = MibTable((1, 3, 6, 1, 4, 1, 2076, 110, 2, 1), )
if mibBuilder.loadTexts: cnDaiVlanCfgTable.setStatus('current')
cnDaiVlanCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2076, 110, 2, 1, 1), ).setIndexNames((0, "CAMBIUM-NETWORKS-DYNAMIC-ARP-INSPECTION-MIB", "cnDaiVlanCfgVlanId"))
if mibBuilder.loadTexts: cnDaiVlanCfgEntry.setStatus('current')
cnDaiVlanCfgVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 2076, 110, 2, 1, 1, 1), VlanId())
if mibBuilder.loadTexts: cnDaiVlanCfgVlanId.setStatus('current')
cnDaiVlanCfgDaiAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2076, 110, 2, 1, 1, 2), AdminStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnDaiVlanCfgDaiAdminStatus.setStatus('current')
cnDaiVlanForwarded = MibTableColumn((1, 3, 6, 1, 4, 1, 2076, 110, 2, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnDaiVlanForwarded.setStatus('current')
cnDaiVlanDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 2076, 110, 2, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnDaiVlanDropped.setStatus('current')
cnDaiVlanInvalidProtocolData = MibTableColumn((1, 3, 6, 1, 4, 1, 2076, 110, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnDaiVlanInvalidProtocolData.setStatus('current')
cnDaiVlanSrcMacValidationFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 2076, 110, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnDaiVlanSrcMacValidationFailures.setStatus('current')
cnDaiVlanIpValidationFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 2076, 110, 2, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnDaiVlanIpValidationFailures.setStatus('current')
cnDaiVlanDhcpBindingsPermitted = MibTableColumn((1, 3, 6, 1, 4, 1, 2076, 110, 2, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnDaiVlanDhcpBindingsPermitted.setStatus('current')
cnDaiVlanDhcpBindingsDenied = MibTableColumn((1, 3, 6, 1, 4, 1, 2076, 110, 2, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnDaiVlanDhcpBindingsDenied.setStatus('current')
cnDaiVlanStaticBindingsPermitted = MibTableColumn((1, 3, 6, 1, 4, 1, 2076, 110, 2, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnDaiVlanStaticBindingsPermitted.setStatus('current')
cnDaiVlanStaticBindingsDenied = MibTableColumn((1, 3, 6, 1, 4, 1, 2076, 110, 2, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnDaiVlanStaticBindingsDenied.setStatus('current')
cnDaiVlanCfgRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2076, 110, 2, 1, 1, 12), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnDaiVlanCfgRowStatus.setStatus('current')
cnDaiIfCfgTable = MibTable((1, 3, 6, 1, 4, 1, 2076, 110, 3, 1), )
if mibBuilder.loadTexts: cnDaiIfCfgTable.setStatus('current')
cnDaiIfCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2076, 110, 3, 1, 1), ).setIndexNames((0, "CAMBIUM-NETWORKS-DYNAMIC-ARP-INSPECTION-MIB", "cnDaiIfCfgIfIndex"))
if mibBuilder.loadTexts: cnDaiIfCfgEntry.setStatus('current')
cnDaiIfCfgIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2076, 110, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 60)))
if mibBuilder.loadTexts: cnDaiIfCfgIfIndex.setStatus('current')
cnDaiIfCfgTrustState = MibTableColumn((1, 3, 6, 1, 4, 1, 2076, 110, 3, 1, 1, 2), TrustState().clone('untrusted')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnDaiIfCfgTrustState.setStatus('current')
mibBuilder.exportSymbols("CAMBIUM-NETWORKS-DYNAMIC-ARP-INSPECTION-MIB", cnDaiVlanCfgTable=cnDaiVlanCfgTable, AdminStatus=AdminStatus, cnDaiVlanIpValidationFailures=cnDaiVlanIpValidationFailures, cnDaiDebugFlag=cnDaiDebugFlag, cnDaiIfCfgTable=cnDaiIfCfgTable, cnDaiVlanSrcMacValidationFailures=cnDaiVlanSrcMacValidationFailures, TrustState=TrustState, cnDaiVlanCfg=cnDaiVlanCfg, cnDaiMib=cnDaiMib, cnDaiVlanCfgEntry=cnDaiVlanCfgEntry, cnDaiVlanDhcpBindingsDenied=cnDaiVlanDhcpBindingsDenied, cnDaiVlanCfgRowStatus=cnDaiVlanCfgRowStatus, cnDaiVlanCfgVlanId=cnDaiVlanCfgVlanId, cnDaiIfCfgIfIndex=cnDaiIfCfgIfIndex, cnDaiVlanInvalidProtocolData=cnDaiVlanInvalidProtocolData, PYSNMP_MODULE_ID=cnDaiMib, cnDaiVlanForwarded=cnDaiVlanForwarded, cnDaiVlanStaticBindingsPermitted=cnDaiVlanStaticBindingsPermitted, cnDaiVlanDropped=cnDaiVlanDropped, cnDaiVlanStaticBindingsDenied=cnDaiVlanStaticBindingsDenied, cnDaiIfCfgEntry=cnDaiIfCfgEntry, cnDaiGlobal=cnDaiGlobal, VlanId=VlanId, cnDaiIfCfgTrustState=cnDaiIfCfgTrustState, cnDaiVlanDhcpBindingsPermitted=cnDaiVlanDhcpBindingsPermitted, cnDaiVlanCfgDaiAdminStatus=cnDaiVlanCfgDaiAdminStatus, cnDaiIfCfg=cnDaiIfCfg)
