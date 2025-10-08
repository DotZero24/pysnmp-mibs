#
# PySNMP MIB module CAMBIUM-NETWORKS-DYNAMIC-ARP-INSPECTION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cambium/CAMBIUM-NETWORKS-DYNAMIC-ARP-INSPECTION-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:06:25 2025
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
mibBuilder.exportSymbols("CAMBIUM-NETWORKS-DYNAMIC-ARP-INSPECTION-MIB", cnDaiVlanStaticBindingsDenied=cnDaiVlanStaticBindingsDenied, cnDaiVlanForwarded=cnDaiVlanForwarded, cnDaiDebugFlag=cnDaiDebugFlag, cnDaiVlanInvalidProtocolData=cnDaiVlanInvalidProtocolData, cnDaiIfCfgIfIndex=cnDaiIfCfgIfIndex, cnDaiGlobal=cnDaiGlobal, VlanId=VlanId, cnDaiVlanCfgVlanId=cnDaiVlanCfgVlanId, cnDaiVlanDhcpBindingsPermitted=cnDaiVlanDhcpBindingsPermitted, cnDaiVlanCfgTable=cnDaiVlanCfgTable, cnDaiVlanSrcMacValidationFailures=cnDaiVlanSrcMacValidationFailures, cnDaiVlanDropped=cnDaiVlanDropped, cnDaiIfCfgTrustState=cnDaiIfCfgTrustState, cnDaiIfCfgEntry=cnDaiIfCfgEntry, cnDaiVlanCfgEntry=cnDaiVlanCfgEntry, cnDaiVlanCfgRowStatus=cnDaiVlanCfgRowStatus, cnDaiIfCfgTable=cnDaiIfCfgTable, cnDaiVlanIpValidationFailures=cnDaiVlanIpValidationFailures, TrustState=TrustState, cnDaiMib=cnDaiMib, PYSNMP_MODULE_ID=cnDaiMib, cnDaiVlanCfg=cnDaiVlanCfg, cnDaiIfCfg=cnDaiIfCfg, cnDaiVlanStaticBindingsPermitted=cnDaiVlanStaticBindingsPermitted, cnDaiVlanDhcpBindingsDenied=cnDaiVlanDhcpBindingsDenied, cnDaiVlanCfgDaiAdminStatus=cnDaiVlanCfgDaiAdminStatus, AdminStatus=AdminStatus)
