#
# PySNMP MIB module WWP-LEOS-PING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/ciena/WWP-LEOS-PING-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:04:02 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
AddressFamilyNumbers, = mibBuilder.importSymbols("IANA-ADDRESS-FAMILY-NUMBERS-MIB", "AddressFamilyNumbers")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
wwpModulesLeos, = mibBuilder.importSymbols("WWP-SMI", "wwpModulesLeos")
wwpLeosPingMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6141, 2, 60, 19))
wwpLeosPingMIB.setRevisions(('2012-04-02 00:00', '2001-07-03 12:57',))
if mibBuilder.loadTexts: wwpLeosPingMIB.setLastUpdated('201204020000Z')
if mibBuilder.loadTexts: wwpLeosPingMIB.setOrganization('Ciena, Inc')
class PingFailCause(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17))
    namedValues = NamedValues(("unknownHost", 1), ("socketError", 2), ("bindError", 3), ("connectError", 4), ("missingHost", 5), ("asyncError", 6), ("nonBlockError", 7), ("mcastError", 8), ("ttlError", 9), ("mcastTtlError", 10), ("outputError", 11), ("unreachableError", 12), ("isAlive", 13), ("txRx", 14), ("commandCompleted", 15), ("noStatus", 16), ("sendRecvMismatch", 17))

class PingState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("idle", 1), ("pinging", 2), ("pingComplete", 3), ("failed", 4))

wwpLeosPingMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 19, 1))
wwpLeosPingDelay = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 19, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosPingDelay.setStatus('current')
wwpLeosPingPacketSize = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 19, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1464)).clone(56)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosPingPacketSize.setStatus('current')
wwpLeosPingActivate = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 19, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosPingActivate.setStatus('current')
wwpLeosPingAddrType = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 19, 1, 4), AddressFamilyNumbers()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosPingAddrType.setStatus('current')
wwpLeosPingAddr = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 19, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosPingAddr.setStatus('current')
wwpLeosPingPacketCount = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 19, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosPingPacketCount.setStatus('current')
wwpLeosPingPacketTimeout = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 19, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosPingPacketTimeout.setStatus('current')
wwpLeosPingSentPackets = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 19, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosPingSentPackets.setStatus('current')
wwpLeosPingReceivedPackets = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 19, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosPingReceivedPackets.setStatus('current')
wwpLeosPingFailCause = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 19, 1, 10), PingFailCause()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosPingFailCause.setStatus('current')
wwpLeosPingState = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 19, 1, 11), PingState().clone('idle')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosPingState.setStatus('current')
wwpLeosPingUntilStopped = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 19, 1, 12), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosPingUntilStopped.setStatus('current')
wwpLeosPingInetAddrType = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 19, 1, 13), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosPingInetAddrType.setStatus('current')
mibBuilder.exportSymbols("WWP-LEOS-PING-MIB", wwpLeosPingDelay=wwpLeosPingDelay, PYSNMP_MODULE_ID=wwpLeosPingMIB, wwpLeosPingAddrType=wwpLeosPingAddrType, wwpLeosPingSentPackets=wwpLeosPingSentPackets, wwpLeosPingPacketSize=wwpLeosPingPacketSize, wwpLeosPingPacketTimeout=wwpLeosPingPacketTimeout, wwpLeosPingReceivedPackets=wwpLeosPingReceivedPackets, wwpLeosPingInetAddrType=wwpLeosPingInetAddrType, wwpLeosPingPacketCount=wwpLeosPingPacketCount, PingState=PingState, wwpLeosPingUntilStopped=wwpLeosPingUntilStopped, wwpLeosPingMIB=wwpLeosPingMIB, PingFailCause=PingFailCause, wwpLeosPingState=wwpLeosPingState, wwpLeosPingFailCause=wwpLeosPingFailCause, wwpLeosPingActivate=wwpLeosPingActivate, wwpLeosPingMIBObjects=wwpLeosPingMIBObjects, wwpLeosPingAddr=wwpLeosPingAddr)
