#
# PySNMP MIB module CISCO-IPSLA-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-IPSLA-TC-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:31:41 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIpSlaTCMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 624))
ciscoIpSlaTCMIB.setRevisions(('2007-03-23 00:00',))
if mibBuilder.loadTexts: ciscoIpSlaTCMIB.setLastUpdated('200703230000Z')
if mibBuilder.loadTexts: ciscoIpSlaTCMIB.setOrganization('Cisco Systems, Inc.')
class IpSlaOperType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("icmpEcho", 1), ("udpEcho", 2), ("tcpConnect", 3), ("udpJitter", 4), ("icmpJitter", 5))

class IpSlaCodecType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("notApplicable", 0), ("g711ulaw", 1), ("g711alaw", 2), ("g729a", 3))

class IpSlaReactVar(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24))
    namedValues = NamedValues(("rtt", 1), ("jitterSDAvg", 2), ("jitterDSAvg", 3), ("packetLossSD", 4), ("packetLossDS", 5), ("mos", 6), ("timeout", 7), ("connectionLoss", 8), ("verifyError", 9), ("jitterAvg", 10), ("icpif", 11), ("packetMIA", 12), ("packetLateArrival", 13), ("packetOutOfSequence", 14), ("maxOfPositiveSD", 15), ("maxOfNegativeSD", 16), ("maxOfPositiveDS", 17), ("maxOfNegativeDS", 18), ("successivePacketLoss", 19), ("maxOfLatencyDS", 20), ("maxOfLatencySD", 21), ("latencyDSAvg", 22), ("latencySDAvg", 23), ("packetLoss", 24))

mibBuilder.exportSymbols("CISCO-IPSLA-TC-MIB", IpSlaCodecType=IpSlaCodecType, IpSlaReactVar=IpSlaReactVar, IpSlaOperType=IpSlaOperType, PYSNMP_MODULE_ID=ciscoIpSlaTCMIB, ciscoIpSlaTCMIB=ciscoIpSlaTCMIB)
