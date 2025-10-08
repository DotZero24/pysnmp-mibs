#
# PySNMP MIB module RADLAN-PIM-BSR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/radlan/RADLAN-PIM-BSR-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:40:54 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
IANAipRouteProtocol, = mibBuilder.importSymbols("IANA-RTPROTO-MIB", "IANAipRouteProtocol")
InterfaceIndexOrZero, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "InterfaceIndex")
InetAddressPrefixLength, InetVersion, InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressPrefixLength", "InetVersion", "InetAddressType", "InetAddress")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "RowStatus", "TextualConvention")
class AdminStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("adminStatusUp", 1), ("adminStatusDown", 2))

class OperStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("operStatusUp", 1), ("operStatusDown", 2), ("operStatusGoingUp", 3), ("operStatusGoingDown", 4), ("operStatusActFailed", 5))

rlPimBsrCandidateRPTable = MibTable((1, 3, 6, 1, 4, 1, 89, 220), )
if mibBuilder.loadTexts: rlPimBsrCandidateRPTable.setStatus('current')
rlPimBsrCandidateRPEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 220, 1), ).setIndexNames((0, "RADLAN-PIM-BSR-MIB", "rlPimBsrCandidateRPAddressType"), (0, "RADLAN-PIM-BSR-MIB", "rlPimBsrCandidateRPAddress"))
if mibBuilder.loadTexts: rlPimBsrCandidateRPEntry.setStatus('current')
rlPimBsrCandidateRPAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 220, 1, 1), InetAddressType())
if mibBuilder.loadTexts: rlPimBsrCandidateRPAddressType.setStatus('current')
rlPimBsrCandidateRPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 220, 1, 2), InetAddress().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(8, 8), ValueSizeConstraint(16, 16), )))
if mibBuilder.loadTexts: rlPimBsrCandidateRPAddress.setStatus('current')
rlPimBsrCandidateRPGroupPrefixList = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 220, 1, 3), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlPimBsrCandidateRPGroupPrefixList.setStatus('current')
rlPimBsrCandidateRPBidir = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 220, 1, 5), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlPimBsrCandidateRPBidir.setStatus('current')
rlPimBsrCandidateRPAdvTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 220, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPimBsrCandidateRPAdvTimer.setStatus('current')
rlPimBsrCandidateRPPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 220, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(192)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlPimBsrCandidateRPPriority.setStatus('current')
rlPimBsrCandidateRPAdvInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 220, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 26214)).clone(60)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlPimBsrCandidateRPAdvInterval.setStatus('current')
rlPimBsrCandidateRPHoldtime = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 220, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(150)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlPimBsrCandidateRPHoldtime.setStatus('current')
rlPimBsrCandidateRPStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 220, 1, 10), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlPimBsrCandidateRPStatus.setStatus('current')
mibBuilder.exportSymbols("RADLAN-PIM-BSR-MIB", rlPimBsrCandidateRPPriority=rlPimBsrCandidateRPPriority, rlPimBsrCandidateRPHoldtime=rlPimBsrCandidateRPHoldtime, rlPimBsrCandidateRPGroupPrefixList=rlPimBsrCandidateRPGroupPrefixList, rlPimBsrCandidateRPAddress=rlPimBsrCandidateRPAddress, AdminStatus=AdminStatus, rlPimBsrCandidateRPStatus=rlPimBsrCandidateRPStatus, rlPimBsrCandidateRPEntry=rlPimBsrCandidateRPEntry, rlPimBsrCandidateRPTable=rlPimBsrCandidateRPTable, rlPimBsrCandidateRPAdvInterval=rlPimBsrCandidateRPAdvInterval, rlPimBsrCandidateRPBidir=rlPimBsrCandidateRPBidir, rlPimBsrCandidateRPAddressType=rlPimBsrCandidateRPAddressType, OperStatus=OperStatus, rlPimBsrCandidateRPAdvTimer=rlPimBsrCandidateRPAdvTimer)
