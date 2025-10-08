#
# PySNMP MIB module FS-BFD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/fscom/FS-BFD-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:01:11 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
fsMgmt, = mibBuilder.importSymbols("FS-SMI", "fsMgmt")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
InetPortNumber, InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetPortNumber", "InetAddressType", "InetAddress")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Gauge32, MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, Counter64, TimeTicks, mib_2 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "Counter64", "TimeTicks", "mib-2")
RowStatus, TextualConvention, StorageType, TruthValue, TimeStamp, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "StorageType", "TruthValue", "TimeStamp", "DisplayString")
class FSBfdSessIndexTC(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class FSBfdIntervalTC(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class FSBfdMultiplierTC(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 255)

class FSBfdDiagTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("noDiagnostic", 0), ("controlDetectionTimeExpired", 1), ("echoFunctionFailed", 2), ("neighborSignaledSessionDown", 3), ("forwardingPlaneReset", 4), ("pathDown", 5), ("concatenatedPathDown", 6), ("administrativelyDown", 7), ("reverseConcatenatedPathDown", 8))

class FSBfdSessTypeTC(TextualConvention, Integer32):
    reference = 'Katz, D. and D. Ward, Bidirectional Forwarding Detection (BFD), RFC 5880, June 2010. Katz, D. and D. Ward, Bidirectional Forwarding Detection (BFD) for IPv4 and IPv6 (Single Hop), RFC 5881, June 2010. Katz, D. and D. Ward, Bidirectional Forwarding Detection (BFD) for Multihop Paths, RFC 5883, June 2010.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("singleHop", 1), ("multiHopTotallyArbitraryPaths", 2), ("multiHopOutOfBandSignaling", 3), ("multiHopUnidirectionalLinks", 4), ("multiPointHead", 5), ("multiPointTail", 6))

class FSBfdSessOperModeTC(TextualConvention, Integer32):
    reference = 'Katz, D. and D. Ward, Bidirectional Forwarding Detection (BFD), RFC 5880, June 2010.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("asyncModeWEchoFunction", 1), ("asynchModeWOEchoFunction", 2), ("demandModeWEchoFunction", 3), ("demandModeWOEchoFunction", 4))

class FSBfdCtrlDestPortNumberTC(TextualConvention, Unsigned32):
    reference = 'Use of port 3784 from Katz, D. and D. Ward, Bidirectional Forwarding Detection (BFD) for IPv4 and IPv6 (Single Hop), RFC 5881, June 2010. Use of port 4784 from Katz, D. and D. Ward, Bidirectional Forwarding Detection (BFD) for IPv4 and IPv6 (Single Hop), RFC 5881, June 2010.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class FSBfdCtrlSourcePortNumberTC(TextualConvention, Unsigned32):
    reference = 'Port 49152..65535 (RFC5881)'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class FSBfdSessStateTC(TextualConvention, Integer32):
    reference = 'RFC 5880 - Bidirectional Forwarding Detection (BFD), Katz, D., Ward, D., June 2010.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("adminDown", 1), ("down", 2), ("init", 3), ("up", 4), ("failing", 5))

class FSBfdSessAuthenticationTypeTC(TextualConvention, Integer32):
    reference = 'Sections 4.2 - 4.4 from Katz, D. and D. Ward, Bidirectional Forwarding Detection (BFD), RFC 5880, June 2010.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(-1, 0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("noAuthentication", -1), ("reserved", 0), ("simplePassword", 1), ("keyedMD5", 2), ("meticulousKeyedMD5", 3), ("keyedSHA1", 4), ("meticulousKeyedSHA1", 5))

class FSBfdSessionAuthenticationKeyTC(TextualConvention, OctetString):
    reference = 'RFC5880, Sections 4.2 - 4.4'
    status = 'current'
    displayHint = '1x '
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 252)

fsBfdMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48))
fsBfdMIB.setRevisions(('2012-04-14 12:00',))
if mibBuilder.loadTexts: fsBfdMIB.setLastUpdated('201204141200Z')
if mibBuilder.loadTexts: fsBfdMIB.setOrganization('FS.COM Inc..')
fsBfdNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 0))
fsBfdObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1))
fsBfdConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 2))
fsBfdScalarObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 1))
fsBfdAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsBfdAdminStatus.setStatus('current')
fsBfdSessNotificationsEnable = MibScalar((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsBfdSessNotificationsEnable.setStatus('current')
fsBfdSessTable = MibTable((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2), )
if mibBuilder.loadTexts: fsBfdSessTable.setStatus('current')
fsBfdSessEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1), ).setIndexNames((0, "FS-BFD-MIB", "fsBfdSessIndex"))
if mibBuilder.loadTexts: fsBfdSessEntry.setStatus('current')
fsBfdSessIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 1), FSBfdSessIndexTC())
if mibBuilder.loadTexts: fsBfdSessIndex.setStatus('current')
fsBfdSessVersionNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fsBfdSessVersionNumber.setStatus('current')
fsBfdSessType = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 3), FSBfdSessTypeTC()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fsBfdSessType.setStatus('current')
fsBfdSessDiscriminator = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsBfdSessDiscriminator.setStatus('current')
fsBfdSessRemoteDiscr = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 5), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 4294967295), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsBfdSessRemoteDiscr.setStatus('current')
fsBfdSessDestinationUdpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 6), FSBfdCtrlDestPortNumberTC()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fsBfdSessDestinationUdpPort.setStatus('current')
fsBfdSessSourceUdpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 7), FSBfdCtrlSourcePortNumberTC()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fsBfdSessSourceUdpPort.setStatus('current')
fsBfdSessEchoSourceUdpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 8), InetPortNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fsBfdSessEchoSourceUdpPort.setStatus('current')
fsBfdSessAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("stop", 1), ("start", 2))).clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fsBfdSessAdminStatus.setStatus('current')
fsBfdSessState = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 10), FSBfdSessStateTC().clone(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsBfdSessState.setStatus('current')
fsBfdSessRemoteHeardFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 11), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsBfdSessRemoteHeardFlag.setStatus('current')
fsBfdSessDiag = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 12), FSBfdDiagTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsBfdSessDiag.setStatus('current')
fsBfdSessOperMode = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 13), FSBfdSessOperModeTC()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fsBfdSessOperMode.setStatus('current')
fsBfdSessDemandModeDesiredFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 14), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fsBfdSessDemandModeDesiredFlag.setStatus('current')
fsBfdSessControlPlaneIndepFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 15), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fsBfdSessControlPlaneIndepFlag.setStatus('current')
fsBfdSessMultipointFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 16), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fsBfdSessMultipointFlag.setStatus('current')
fsBfdSessInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 17), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fsBfdSessInterface.setStatus('current')
fsBfdSessSrcAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 18), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fsBfdSessSrcAddrType.setStatus('current')
fsBfdSessSrcAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 19), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fsBfdSessSrcAddr.setStatus('current')
fsBfdSessDstAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 20), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fsBfdSessDstAddrType.setStatus('current')
fsBfdSessDstAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 21), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fsBfdSessDstAddr.setStatus('current')
fsBfdSessGTSM = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 22), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fsBfdSessGTSM.setStatus('current')
fsBfdSessGTSMTTL = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 23), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fsBfdSessGTSMTTL.setStatus('current')
fsBfdSessDesiredMinTxInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 24), FSBfdIntervalTC()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fsBfdSessDesiredMinTxInterval.setStatus('current')
fsBfdSessReqMinRxInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 25), FSBfdIntervalTC()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fsBfdSessReqMinRxInterval.setStatus('current')
fsBfdSessReqMinEchoRxInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 26), FSBfdIntervalTC()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fsBfdSessReqMinEchoRxInterval.setStatus('current')
fsBfdSessDetectMult = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 27), FSBfdMultiplierTC()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fsBfdSessDetectMult.setStatus('current')
fsBfdSessNegotiatedInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 28), FSBfdIntervalTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsBfdSessNegotiatedInterval.setStatus('current')
fsBfdSessNegotiatedEchoInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 29), FSBfdIntervalTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsBfdSessNegotiatedEchoInterval.setStatus('current')
fsBfdSessNegotiatedDetectMult = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 30), FSBfdMultiplierTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsBfdSessNegotiatedDetectMult.setStatus('current')
fsBfdSessAuthPresFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 31), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fsBfdSessAuthPresFlag.setStatus('current')
fsBfdSessAuthenticationType = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 32), FSBfdSessAuthenticationTypeTC().clone(-1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fsBfdSessAuthenticationType.setStatus('current')
fsBfdSessAuthenticationKeyID = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 33), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 255), )).clone(-1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fsBfdSessAuthenticationKeyID.setStatus('current')
fsBfdSessAuthenticationKey = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 34), FSBfdSessionAuthenticationKeyTC()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fsBfdSessAuthenticationKey.setStatus('current')
fsBfdSessStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 35), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fsBfdSessStorageType.setStatus('current')
fsBfdSessRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 36), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fsBfdSessRowStatus.setStatus('current')
fsBfdSessIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 37), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fsBfdSessIfName.setStatus('current')
fsBfdSessIfDes = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 2, 1, 38), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fsBfdSessIfDes.setStatus('current')
fsBfdSessPerfTable = MibTable((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 3), )
if mibBuilder.loadTexts: fsBfdSessPerfTable.setStatus('current')
fsBfdSessPerfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 3, 1), )
fsBfdSessEntry.registerAugmentions(("FS-BFD-MIB", "fsBfdSessPerfEntry"))
fsBfdSessPerfEntry.setIndexNames(*fsBfdSessEntry.getIndexNames())
if mibBuilder.loadTexts: fsBfdSessPerfEntry.setStatus('current')
fsBfdSessPerfCtrlPktIn = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 3, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsBfdSessPerfCtrlPktIn.setStatus('current')
fsBfdSessPerfCtrlPktOut = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsBfdSessPerfCtrlPktOut.setStatus('current')
fsBfdSessPerfCtrlPktDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsBfdSessPerfCtrlPktDrop.setStatus('current')
fsBfdSessPerfCtrlPktDropLastTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 3, 1, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsBfdSessPerfCtrlPktDropLastTime.setStatus('current')
fsBfdSessPerfEchoPktIn = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsBfdSessPerfEchoPktIn.setStatus('current')
fsBfdSessPerfEchoPktOut = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsBfdSessPerfEchoPktOut.setStatus('current')
fsBfdSessPerfEchoPktDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsBfdSessPerfEchoPktDrop.setStatus('current')
fsBfdSessPerfEchoPktDropLastTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 3, 1, 8), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsBfdSessPerfEchoPktDropLastTime.setStatus('current')
fsBfdSessUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 3, 1, 9), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsBfdSessUpTime.setStatus('current')
fsBfdSessPerfLastSessDownTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 3, 1, 10), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsBfdSessPerfLastSessDownTime.setStatus('current')
fsBfdSessPerfLastCommLostDiag = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 3, 1, 11), FSBfdDiagTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsBfdSessPerfLastCommLostDiag.setStatus('current')
fsBfdSessPerfSessUpCount = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 3, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsBfdSessPerfSessUpCount.setStatus('current')
fsBfdSessPerfDiscTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 3, 1, 13), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsBfdSessPerfDiscTime.setStatus('current')
fsBfdSessPerfCtrlPktInHC = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 3, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsBfdSessPerfCtrlPktInHC.setStatus('current')
fsBfdSessPerfCtrlPktOutHC = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 3, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsBfdSessPerfCtrlPktOutHC.setStatus('current')
fsBfdSessPerfCtrlPktDropHC = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 3, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsBfdSessPerfCtrlPktDropHC.setStatus('current')
fsBfdSessPerfEchoPktInHC = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 3, 1, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsBfdSessPerfEchoPktInHC.setStatus('current')
fsBfdSessPerfEchoPktOutHC = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 3, 1, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsBfdSessPerfEchoPktOutHC.setStatus('current')
fsBfdSessPerfEchoPktDropHC = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 3, 1, 19), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsBfdSessPerfEchoPktDropHC.setStatus('current')
fsBfdSessDiscMapTable = MibTable((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 4), )
if mibBuilder.loadTexts: fsBfdSessDiscMapTable.setStatus('current')
fsBfdSessDiscMapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 4, 1), ).setIndexNames((0, "FS-BFD-MIB", "fsBfdSessDiscriminator"))
if mibBuilder.loadTexts: fsBfdSessDiscMapEntry.setStatus('current')
fsBfdSessDiscMapIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 4, 1, 1), FSBfdSessIndexTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsBfdSessDiscMapIndex.setStatus('current')
fsBfdSessDiscMapStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 4, 1, 2), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fsBfdSessDiscMapStorageType.setStatus('current')
fsBfdSessDiscMapRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 4, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fsBfdSessDiscMapRowStatus.setStatus('current')
fsBfdSessIpMapTable = MibTable((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 5), )
if mibBuilder.loadTexts: fsBfdSessIpMapTable.setStatus('current')
fsBfdSessIpMapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 5, 1), ).setIndexNames((0, "FS-BFD-MIB", "fsBfdSessInterface"), (0, "FS-BFD-MIB", "fsBfdSessSrcAddrType"), (0, "FS-BFD-MIB", "fsBfdSessSrcAddr"), (0, "FS-BFD-MIB", "fsBfdSessDstAddrType"), (0, "FS-BFD-MIB", "fsBfdSessDstAddr"))
if mibBuilder.loadTexts: fsBfdSessIpMapEntry.setStatus('current')
fsBfdSessIpMapIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 5, 1, 1), FSBfdSessIndexTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsBfdSessIpMapIndex.setStatus('current')
fsBfdSessIpMapStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 5, 1, 2), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fsBfdSessIpMapStorageType.setStatus('current')
fsBfdSessIpMapRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 1, 5, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fsBfdSessIpMapRowStatus.setStatus('current')
fsBfdSessUp = NotificationType((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 0, 1)).setObjects(("FS-BFD-MIB", "fsBfdSessDiag"), ("FS-BFD-MIB", "fsBfdSessDiag"), ("FS-BFD-MIB", "fsBfdSessInterface"), ("FS-BFD-MIB", "fsBfdSessIfName"), ("FS-BFD-MIB", "fsBfdSessIfDes"))
if mibBuilder.loadTexts: fsBfdSessUp.setStatus('current')
fsBfdSessDown = NotificationType((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 0, 2)).setObjects(("FS-BFD-MIB", "fsBfdSessDiag"), ("FS-BFD-MIB", "fsBfdSessDiag"), ("FS-BFD-MIB", "fsBfdSessInterface"), ("FS-BFD-MIB", "fsBfdSessIfName"), ("FS-BFD-MIB", "fsBfdSessIfDes"))
if mibBuilder.loadTexts: fsBfdSessDown.setStatus('current')
fsBfdGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 2, 1))
fsBfdCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 2, 2))
fsBfdModuleFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 2, 2, 1)).setObjects(("FS-BFD-MIB", "fsBfdSessionGroup"), ("FS-BFD-MIB", "fsBfdSessionReadOnlyGroup"), ("FS-BFD-MIB", "fsBfdSessionPerfGroup"), ("FS-BFD-MIB", "fsBfdNotificationGroup"), ("FS-BFD-MIB", "fsBfdSessionPerfHCGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fsBfdModuleFullCompliance = fsBfdModuleFullCompliance.setStatus('current')
fsBfdModuleReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 2, 2, 2)).setObjects(("FS-BFD-MIB", "fsBfdSessionGroup"), ("FS-BFD-MIB", "fsBfdSessionReadOnlyGroup"), ("FS-BFD-MIB", "fsBfdSessionPerfGroup"), ("FS-BFD-MIB", "fsBfdNotificationGroup"), ("FS-BFD-MIB", "fsBfdSessionPerfHCGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fsBfdModuleReadOnlyCompliance = fsBfdModuleReadOnlyCompliance.setStatus('current')
fsBfdSessionGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 2, 1, 1)).setObjects(("FS-BFD-MIB", "fsBfdAdminStatus"), ("FS-BFD-MIB", "fsBfdSessNotificationsEnable"), ("FS-BFD-MIB", "fsBfdSessVersionNumber"), ("FS-BFD-MIB", "fsBfdSessType"), ("FS-BFD-MIB", "fsBfdSessDestinationUdpPort"), ("FS-BFD-MIB", "fsBfdSessSourceUdpPort"), ("FS-BFD-MIB", "fsBfdSessEchoSourceUdpPort"), ("FS-BFD-MIB", "fsBfdSessAdminStatus"), ("FS-BFD-MIB", "fsBfdSessOperMode"), ("FS-BFD-MIB", "fsBfdSessDemandModeDesiredFlag"), ("FS-BFD-MIB", "fsBfdSessControlPlaneIndepFlag"), ("FS-BFD-MIB", "fsBfdSessMultipointFlag"), ("FS-BFD-MIB", "fsBfdSessInterface"), ("FS-BFD-MIB", "fsBfdSessSrcAddrType"), ("FS-BFD-MIB", "fsBfdSessSrcAddr"), ("FS-BFD-MIB", "fsBfdSessDstAddrType"), ("FS-BFD-MIB", "fsBfdSessDstAddr"), ("FS-BFD-MIB", "fsBfdSessGTSM"), ("FS-BFD-MIB", "fsBfdSessGTSMTTL"), ("FS-BFD-MIB", "fsBfdSessDesiredMinTxInterval"), ("FS-BFD-MIB", "fsBfdSessReqMinRxInterval"), ("FS-BFD-MIB", "fsBfdSessReqMinEchoRxInterval"), ("FS-BFD-MIB", "fsBfdSessDetectMult"), ("FS-BFD-MIB", "fsBfdSessAuthPresFlag"), ("FS-BFD-MIB", "fsBfdSessAuthenticationType"), ("FS-BFD-MIB", "fsBfdSessAuthenticationKeyID"), ("FS-BFD-MIB", "fsBfdSessAuthenticationKey"), ("FS-BFD-MIB", "fsBfdSessStorageType"), ("FS-BFD-MIB", "fsBfdSessRowStatus"), ("FS-BFD-MIB", "fsBfdSessDiscMapStorageType"), ("FS-BFD-MIB", "fsBfdSessDiscMapRowStatus"), ("FS-BFD-MIB", "fsBfdSessIpMapStorageType"), ("FS-BFD-MIB", "fsBfdSessIpMapRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fsBfdSessionGroup = fsBfdSessionGroup.setStatus('current')
fsBfdSessionReadOnlyGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 2, 1, 2)).setObjects(("FS-BFD-MIB", "fsBfdSessDiscriminator"), ("FS-BFD-MIB", "fsBfdSessRemoteDiscr"), ("FS-BFD-MIB", "fsBfdSessState"), ("FS-BFD-MIB", "fsBfdSessRemoteHeardFlag"), ("FS-BFD-MIB", "fsBfdSessDiag"), ("FS-BFD-MIB", "fsBfdSessNegotiatedInterval"), ("FS-BFD-MIB", "fsBfdSessNegotiatedEchoInterval"), ("FS-BFD-MIB", "fsBfdSessNegotiatedDetectMult"), ("FS-BFD-MIB", "fsBfdSessDiscMapIndex"), ("FS-BFD-MIB", "fsBfdSessIpMapIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fsBfdSessionReadOnlyGroup = fsBfdSessionReadOnlyGroup.setStatus('current')
fsBfdSessionPerfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 2, 1, 3)).setObjects(("FS-BFD-MIB", "fsBfdSessPerfCtrlPktIn"), ("FS-BFD-MIB", "fsBfdSessPerfCtrlPktOut"), ("FS-BFD-MIB", "fsBfdSessPerfCtrlPktDrop"), ("FS-BFD-MIB", "fsBfdSessPerfCtrlPktDropLastTime"), ("FS-BFD-MIB", "fsBfdSessPerfEchoPktIn"), ("FS-BFD-MIB", "fsBfdSessPerfEchoPktOut"), ("FS-BFD-MIB", "fsBfdSessPerfEchoPktDrop"), ("FS-BFD-MIB", "fsBfdSessPerfEchoPktDropLastTime"), ("FS-BFD-MIB", "fsBfdSessUpTime"), ("FS-BFD-MIB", "fsBfdSessPerfLastSessDownTime"), ("FS-BFD-MIB", "fsBfdSessPerfLastCommLostDiag"), ("FS-BFD-MIB", "fsBfdSessPerfSessUpCount"), ("FS-BFD-MIB", "fsBfdSessPerfDiscTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fsBfdSessionPerfGroup = fsBfdSessionPerfGroup.setStatus('current')
fsBfdSessionPerfHCGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 2, 1, 4)).setObjects(("FS-BFD-MIB", "fsBfdSessPerfCtrlPktInHC"), ("FS-BFD-MIB", "fsBfdSessPerfCtrlPktOutHC"), ("FS-BFD-MIB", "fsBfdSessPerfCtrlPktDropHC"), ("FS-BFD-MIB", "fsBfdSessPerfEchoPktInHC"), ("FS-BFD-MIB", "fsBfdSessPerfEchoPktOutHC"), ("FS-BFD-MIB", "fsBfdSessPerfEchoPktDropHC"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fsBfdSessionPerfHCGroup = fsBfdSessionPerfHCGroup.setStatus('current')
fsBfdNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 48, 2, 1, 5)).setObjects(("FS-BFD-MIB", "fsBfdSessUp"), ("FS-BFD-MIB", "fsBfdSessDown"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fsBfdNotificationGroup = fsBfdNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("FS-BFD-MIB", fsBfdSessAuthenticationKeyID=fsBfdSessAuthenticationKeyID, fsBfdGroups=fsBfdGroups, fsBfdModuleFullCompliance=fsBfdModuleFullCompliance, fsBfdSessDiag=fsBfdSessDiag, fsBfdSessNegotiatedEchoInterval=fsBfdSessNegotiatedEchoInterval, fsBfdSessNotificationsEnable=fsBfdSessNotificationsEnable, fsBfdSessDstAddrType=fsBfdSessDstAddrType, fsBfdSessState=fsBfdSessState, fsBfdSessionPerfGroup=fsBfdSessionPerfGroup, fsBfdSessVersionNumber=fsBfdSessVersionNumber, fsBfdNotifications=fsBfdNotifications, FSBfdSessTypeTC=FSBfdSessTypeTC, fsBfdSessNegotiatedDetectMult=fsBfdSessNegotiatedDetectMult, fsBfdSessDiscMapEntry=fsBfdSessDiscMapEntry, fsBfdSessType=fsBfdSessType, fsBfdSessNegotiatedInterval=fsBfdSessNegotiatedInterval, fsBfdSessInterface=fsBfdSessInterface, FSBfdCtrlDestPortNumberTC=FSBfdCtrlDestPortNumberTC, FSBfdSessStateTC=FSBfdSessStateTC, FSBfdSessIndexTC=FSBfdSessIndexTC, fsBfdMIB=fsBfdMIB, fsBfdSessPerfEchoPktDrop=fsBfdSessPerfEchoPktDrop, fsBfdSessIfDes=fsBfdSessIfDes, fsBfdSessIpMapStorageType=fsBfdSessIpMapStorageType, fsBfdSessPerfCtrlPktIn=fsBfdSessPerfCtrlPktIn, fsBfdSessionReadOnlyGroup=fsBfdSessionReadOnlyGroup, fsBfdSessPerfCtrlPktInHC=fsBfdSessPerfCtrlPktInHC, fsBfdSessIpMapTable=fsBfdSessIpMapTable, fsBfdSessIpMapIndex=fsBfdSessIpMapIndex, fsBfdSessDemandModeDesiredFlag=fsBfdSessDemandModeDesiredFlag, fsBfdCompliances=fsBfdCompliances, FSBfdDiagTC=FSBfdDiagTC, fsBfdSessPerfEchoPktOut=fsBfdSessPerfEchoPktOut, fsBfdSessIndex=fsBfdSessIndex, fsBfdSessRowStatus=fsBfdSessRowStatus, fsBfdSessPerfEntry=fsBfdSessPerfEntry, fsBfdSessMultipointFlag=fsBfdSessMultipointFlag, fsBfdSessEchoSourceUdpPort=fsBfdSessEchoSourceUdpPort, fsBfdSessUp=fsBfdSessUp, fsBfdSessDetectMult=fsBfdSessDetectMult, fsBfdSessPerfLastCommLostDiag=fsBfdSessPerfLastCommLostDiag, fsBfdSessPerfCtrlPktDropLastTime=fsBfdSessPerfCtrlPktDropLastTime, fsBfdSessPerfDiscTime=fsBfdSessPerfDiscTime, fsBfdConformance=fsBfdConformance, fsBfdSessRemoteHeardFlag=fsBfdSessRemoteHeardFlag, fsBfdSessControlPlaneIndepFlag=fsBfdSessControlPlaneIndepFlag, fsBfdSessPerfCtrlPktOut=fsBfdSessPerfCtrlPktOut, fsBfdSessionGroup=fsBfdSessionGroup, fsBfdSessAuthenticationType=fsBfdSessAuthenticationType, fsBfdSessReqMinEchoRxInterval=fsBfdSessReqMinEchoRxInterval, fsBfdAdminStatus=fsBfdAdminStatus, fsBfdSessEntry=fsBfdSessEntry, fsBfdSessGTSM=fsBfdSessGTSM, fsBfdSessGTSMTTL=fsBfdSessGTSMTTL, fsBfdSessPerfLastSessDownTime=fsBfdSessPerfLastSessDownTime, fsBfdSessPerfEchoPktInHC=fsBfdSessPerfEchoPktInHC, FSBfdMultiplierTC=FSBfdMultiplierTC, fsBfdSessDesiredMinTxInterval=fsBfdSessDesiredMinTxInterval, fsBfdSessPerfSessUpCount=fsBfdSessPerfSessUpCount, fsBfdSessTable=fsBfdSessTable, fsBfdSessPerfCtrlPktDropHC=fsBfdSessPerfCtrlPktDropHC, fsBfdSessPerfEchoPktDropHC=fsBfdSessPerfEchoPktDropHC, fsBfdSessDiscMapRowStatus=fsBfdSessDiscMapRowStatus, fsBfdSessDiscriminator=fsBfdSessDiscriminator, fsBfdSessOperMode=fsBfdSessOperMode, fsBfdNotificationGroup=fsBfdNotificationGroup, fsBfdSessSrcAddr=fsBfdSessSrcAddr, FSBfdSessAuthenticationTypeTC=FSBfdSessAuthenticationTypeTC, fsBfdSessDstAddr=fsBfdSessDstAddr, fsBfdSessDiscMapIndex=fsBfdSessDiscMapIndex, fsBfdSessSrcAddrType=fsBfdSessSrcAddrType, fsBfdSessIpMapEntry=fsBfdSessIpMapEntry, fsBfdSessIfName=fsBfdSessIfName, fsBfdSessRemoteDiscr=fsBfdSessRemoteDiscr, fsBfdSessAuthPresFlag=fsBfdSessAuthPresFlag, fsBfdSessReqMinRxInterval=fsBfdSessReqMinRxInterval, fsBfdSessAdminStatus=fsBfdSessAdminStatus, fsBfdSessAuthenticationKey=fsBfdSessAuthenticationKey, fsBfdSessPerfTable=fsBfdSessPerfTable, fsBfdSessPerfCtrlPktOutHC=fsBfdSessPerfCtrlPktOutHC, fsBfdSessDiscMapTable=fsBfdSessDiscMapTable, FSBfdSessionAuthenticationKeyTC=FSBfdSessionAuthenticationKeyTC, fsBfdSessSourceUdpPort=fsBfdSessSourceUdpPort, fsBfdSessUpTime=fsBfdSessUpTime, fsBfdSessStorageType=fsBfdSessStorageType, FSBfdSessOperModeTC=FSBfdSessOperModeTC, FSBfdIntervalTC=FSBfdIntervalTC, fsBfdSessDestinationUdpPort=fsBfdSessDestinationUdpPort, fsBfdSessPerfEchoPktDropLastTime=fsBfdSessPerfEchoPktDropLastTime, fsBfdModuleReadOnlyCompliance=fsBfdModuleReadOnlyCompliance, fsBfdObjects=fsBfdObjects, fsBfdSessIpMapRowStatus=fsBfdSessIpMapRowStatus, fsBfdSessPerfEchoPktOutHC=fsBfdSessPerfEchoPktOutHC, fsBfdSessDiscMapStorageType=fsBfdSessDiscMapStorageType, fsBfdScalarObjects=fsBfdScalarObjects, fsBfdSessPerfCtrlPktDrop=fsBfdSessPerfCtrlPktDrop, fsBfdSessPerfEchoPktIn=fsBfdSessPerfEchoPktIn, FSBfdCtrlSourcePortNumberTC=FSBfdCtrlSourcePortNumberTC, PYSNMP_MODULE_ID=fsBfdMIB, fsBfdSessionPerfHCGroup=fsBfdSessionPerfHCGroup, fsBfdSessDown=fsBfdSessDown)
