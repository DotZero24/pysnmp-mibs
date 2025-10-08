#
# PySNMP MIB module FUJITSU-LLDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/fujitsu/FUJITSU-LLDP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:12:22 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
fssProtocols, = mibBuilder.importSymbols("FSS-COMMON-SMI", "fssProtocols")
protocolsProtocolName, protocolsProtocolEntry = mibBuilder.importSymbols("FUJITSU-PROTOCOLS-MIB", "protocolsProtocolName", "protocolsProtocolEntry")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, Counter64, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "Counter64", "TimeTicks", "Gauge32")
RowStatus, DateAndTime, TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DateAndTime", "TextualConvention", "TruthValue", "DisplayString")
fssLLDP = ModuleIdentity((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 1100, 1100))
fssLLDP.setRevisions(('2016-11-03 00:00',))
if mibBuilder.loadTexts: fssLLDP.setLastUpdated('201611030000Z')
if mibBuilder.loadTexts: fssLLDP.setOrganization('@ORGANIZATION')
class UnsignedByte(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class UnsignedShort(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class InetAddressIP(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(16, 16), )
class String(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

protocolsProtocolFssLLDPTable = MibTable((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 1100, 1100, 1), )
if mibBuilder.loadTexts: protocolsProtocolFssLLDPTable.setStatus('current')
protocolsProtocolFssLLDPEntry = MibTableRow((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 1100, 1100, 1, 1), )
protocolsProtocolEntry.registerAugmentions(("FUJITSU-LLDP-MIB", "protocolsProtocolFssLLDPEntry"))
protocolsProtocolFssLLDPEntry.setIndexNames(*protocolsProtocolEntry.getIndexNames())
if mibBuilder.loadTexts: protocolsProtocolFssLLDPEntry.setStatus('current')
lldp_instanceGlobal_configAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 1100, 1100, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1))).clone('enable')).setLabel("lldp-instanceGlobal-configAdminStatus").setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldp_instanceGlobal_configAdminStatus.setStatus('current')
lldp_instanceGlobal_configMsgTxInterval = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 1100, 1100, 1, 1, 2), UnsignedShort().subtype(subtypeSpec=ValueRangeConstraint(5, 32768)).clone(30)).setLabel("lldp-instanceGlobal-configMsgTxInterval").setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldp_instanceGlobal_configMsgTxInterval.setStatus('current')
lldp_instanceGlobal_configMsgTxHoldMultiplier = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 1100, 1100, 1, 1, 3), UnsignedByte().subtype(subtypeSpec=ValueRangeConstraint(2, 10)).clone(4)).setLabel("lldp-instanceGlobal-configMsgTxHoldMultiplier").setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldp_instanceGlobal_configMsgTxHoldMultiplier.setStatus('current')
lldp_instancePortTable = MibTable((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 1100, 1100, 2), ).setLabel("lldp-instancePortTable")
if mibBuilder.loadTexts: lldp_instancePortTable.setStatus('current')
lldp_instancePortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 1100, 1100, 2, 1), ).setLabel("lldp-instancePortEntry").setIndexNames((0, "FUJITSU-PROTOCOLS-MIB", "protocolsProtocolName"), (0, "FUJITSU-LLDP-MIB", "lldp-instancePortIfIndex"))
if mibBuilder.loadTexts: lldp_instancePortEntry.setStatus('current')
lldp_instancePortIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 1100, 1100, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setLabel("lldp-instancePortIfIndex")
if mibBuilder.loadTexts: lldp_instancePortIfIndex.setStatus('current')
lldp_instancePortAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 1100, 1100, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("disable", 0), ("txandrx", 1), ("txonly", 2), ("rxonly", 3))).clone('txandrx')).setLabel("lldp-instancePortAdminStatus").setMaxAccess("readcreate")
if mibBuilder.loadTexts: lldp_instancePortAdminStatus.setStatus('current')
lldp_instancePortRowstatus = MibScalar((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 1100, 1100, 2, 1, 3), RowStatus()).setLabel("lldp-instancePortRowstatus").setMaxAccess("readcreate")
if mibBuilder.loadTexts: lldp_instancePortRowstatus.setStatus('current')
mibBuilder.exportSymbols("FUJITSU-LLDP-MIB", UnsignedShort=UnsignedShort, lldp_instancePortIfIndex=lldp_instancePortIfIndex, lldp_instancePortAdminStatus=lldp_instancePortAdminStatus, UnsignedByte=UnsignedByte, InetAddressIP=InetAddressIP, PYSNMP_MODULE_ID=fssLLDP, fssLLDP=fssLLDP, protocolsProtocolFssLLDPTable=protocolsProtocolFssLLDPTable, protocolsProtocolFssLLDPEntry=protocolsProtocolFssLLDPEntry, lldp_instanceGlobal_configAdminStatus=lldp_instanceGlobal_configAdminStatus, lldp_instanceGlobal_configMsgTxInterval=lldp_instanceGlobal_configMsgTxInterval, lldp_instancePortEntry=lldp_instancePortEntry, lldp_instancePortTable=lldp_instancePortTable, lldp_instancePortRowstatus=lldp_instancePortRowstatus, String=String, lldp_instanceGlobal_configMsgTxHoldMultiplier=lldp_instanceGlobal_configMsgTxHoldMultiplier)
