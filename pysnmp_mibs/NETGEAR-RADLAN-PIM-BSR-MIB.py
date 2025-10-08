#
# PySNMP MIB module NETGEAR-RADLAN-PIM-BSR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/netgear/NETGEAR-RADLAN-PIM-BSR-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:50:31 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
IANAipRouteProtocol, = mibBuilder.importSymbols("IANA-RTPROTO-MIB", "IANAipRouteProtocol")
InterfaceIndexOrZero, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "InterfaceIndex")
InetVersion, InetAddressPrefixLength, InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetVersion", "InetAddressPrefixLength", "InetAddressType", "InetAddress")
rnd, = mibBuilder.importSymbols("NETGEAR-RADLAN-MIB", "rnd")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "DisplayString", "TextualConvention")
class AdminStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("adminStatusUp", 1), ("adminStatusDown", 2))

class OperStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("operStatusUp", 1), ("operStatusDown", 2), ("operStatusGoingUp", 3), ("operStatusGoingDown", 4), ("operStatusActFailed", 5))

rlPimBsrCandidateRPTable = MibTable((1, 3, 6, 1, 4, 1, 4526, 17, 220), )
if mibBuilder.loadTexts: rlPimBsrCandidateRPTable.setStatus('current')
rlPimBsrCandidateRPEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4526, 17, 220, 1), ).setIndexNames((0, "NETGEAR-RADLAN-PIM-BSR-MIB", "rlPimBsrCandidateRPAddressType"), (0, "NETGEAR-RADLAN-PIM-BSR-MIB", "rlPimBsrCandidateRPAddress"))
if mibBuilder.loadTexts: rlPimBsrCandidateRPEntry.setStatus('current')
rlPimBsrCandidateRPAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 17, 220, 1, 1), InetAddressType())
if mibBuilder.loadTexts: rlPimBsrCandidateRPAddressType.setStatus('current')
rlPimBsrCandidateRPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 17, 220, 1, 2), InetAddress().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(8, 8), ValueSizeConstraint(16, 16), )))
if mibBuilder.loadTexts: rlPimBsrCandidateRPAddress.setStatus('current')
rlPimBsrCandidateRPGroupPrefixList = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 17, 220, 1, 3), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlPimBsrCandidateRPGroupPrefixList.setStatus('current')
rlPimBsrCandidateRPBidir = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 17, 220, 1, 5), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlPimBsrCandidateRPBidir.setStatus('current')
rlPimBsrCandidateRPAdvTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 17, 220, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPimBsrCandidateRPAdvTimer.setStatus('current')
rlPimBsrCandidateRPPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 17, 220, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(192)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlPimBsrCandidateRPPriority.setStatus('current')
rlPimBsrCandidateRPAdvInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 17, 220, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 26214)).clone(60)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlPimBsrCandidateRPAdvInterval.setStatus('current')
rlPimBsrCandidateRPHoldtime = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 17, 220, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(150)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlPimBsrCandidateRPHoldtime.setStatus('current')
rlPimBsrCandidateRPStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 17, 220, 1, 10), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlPimBsrCandidateRPStatus.setStatus('current')
mibBuilder.exportSymbols("NETGEAR-RADLAN-PIM-BSR-MIB", rlPimBsrCandidateRPAddress=rlPimBsrCandidateRPAddress, rlPimBsrCandidateRPAdvTimer=rlPimBsrCandidateRPAdvTimer, rlPimBsrCandidateRPAdvInterval=rlPimBsrCandidateRPAdvInterval, rlPimBsrCandidateRPBidir=rlPimBsrCandidateRPBidir, rlPimBsrCandidateRPAddressType=rlPimBsrCandidateRPAddressType, rlPimBsrCandidateRPTable=rlPimBsrCandidateRPTable, rlPimBsrCandidateRPStatus=rlPimBsrCandidateRPStatus, rlPimBsrCandidateRPHoldtime=rlPimBsrCandidateRPHoldtime, rlPimBsrCandidateRPEntry=rlPimBsrCandidateRPEntry, OperStatus=OperStatus, rlPimBsrCandidateRPPriority=rlPimBsrCandidateRPPriority, rlPimBsrCandidateRPGroupPrefixList=rlPimBsrCandidateRPGroupPrefixList, AdminStatus=AdminStatus)
