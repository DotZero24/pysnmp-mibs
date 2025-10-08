#
# PySNMP MIB module QTECH-BFD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/qtech/QTECH-BFD-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:06:29 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
InetPortNumber, InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetPortNumber", "InetAddressType", "InetAddress")
qtechMgmt, = mibBuilder.importSymbols("QTECH-SMI", "qtechMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter32, iso, TimeTicks, MibIdentifier, Integer32, Bits, mib_2, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter32", "iso", "TimeTicks", "MibIdentifier", "Integer32", "Bits", "mib-2", "IpAddress")
DisplayString, TimeStamp, RowStatus, StorageType, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TimeStamp", "RowStatus", "StorageType", "TruthValue", "TextualConvention")
class QtechBfdSessIndexTC(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class QtechBfdIntervalTC(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class QtechBfdMultiplierTC(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 255)

class QtechBfdDiagTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("noDiagnostic", 0), ("controlDetectionTimeExpired", 1), ("echoFunctionFailed", 2), ("neighborSignaledSessionDown", 3), ("forwardingPlaneReset", 4), ("pathDown", 5), ("concatenatedPathDown", 6), ("administrativelyDown", 7), ("reverseConcatenatedPathDown", 8))

class QtechBfdSessTypeTC(TextualConvention, Integer32):
    reference = 'Katz, D. and D. Ward, Bidirectional Forwarding Detection (BFD), RFC 5880, June 2010. Katz, D. and D. Ward, Bidirectional Forwarding Detection (BFD) for IPv4 and IPv6 (Single Hop), RFC 5881, June 2010. Katz, D. and D. Ward, Bidirectional Forwarding Detection (BFD) for Multihop Paths, RFC 5883, June 2010.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("singleHop", 1), ("multiHopTotallyArbitraryPaths", 2), ("multiHopOutOfBandSignaling", 3), ("multiHopUnidirectionalLinks", 4), ("multiPointHead", 5), ("multiPointTail", 6))

class QtechBfdSessOperModeTC(TextualConvention, Integer32):
    reference = 'Katz, D. and D. Ward, Bidirectional Forwarding Detection (BFD), RFC 5880, June 2010.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("asyncModeWEchoFunction", 1), ("asynchModeWOEchoFunction", 2), ("demandModeWEchoFunction", 3), ("demandModeWOEchoFunction", 4))

class QtechBfdCtrlDestPortNumberTC(TextualConvention, Unsigned32):
    reference = 'Use of port 3784 from Katz, D. and D. Ward, Bidirectional Forwarding Detection (BFD) for IPv4 and IPv6 (Single Hop), RFC 5881, June 2010. Use of port 4784 from Katz, D. and D. Ward, Bidirectional Forwarding Detection (BFD) for IPv4 and IPv6 (Single Hop), RFC 5881, June 2010.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class QtechBfdCtrlSourcePortNumberTC(TextualConvention, Unsigned32):
    reference = 'Port 49152..65535 (RFC5881)'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class QtechBfdSessStateTC(TextualConvention, Integer32):
    reference = 'RFC 5880 - Bidirectional Forwarding Detection (BFD), Katz, D., Ward, D., June 2010.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("adminDown", 1), ("down", 2), ("init", 3), ("up", 4), ("failing", 5))

class QtechBfdSessAuthenticationTypeTC(TextualConvention, Integer32):
    reference = 'Sections 4.2 - 4.4 from Katz, D. and D. Ward, Bidirectional Forwarding Detection (BFD), RFC 5880, June 2010.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(-1, 0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("noAuthentication", -1), ("reserved", 0), ("simplePassword", 1), ("keyedMD5", 2), ("meticulousKeyedMD5", 3), ("keyedSHA1", 4), ("meticulousKeyedSHA1", 5))

class QtechBfdSessionAuthenticationKeyTC(TextualConvention, OctetString):
    reference = 'RFC5880, Sections 4.2 - 4.4'
    status = 'current'
    displayHint = '1x '
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 252)

qtechBfdMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48))
qtechBfdMIB.setRevisions(('2012-04-14 12:00',))
if mibBuilder.loadTexts: qtechBfdMIB.setLastUpdated('201204141200Z')
if mibBuilder.loadTexts: qtechBfdMIB.setOrganization('Qtech Networks Co.,Ltd.')
qtechBfdNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 0))
qtechBfdObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1))
qtechBfdConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 2))
qtechBfdScalarObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 1))
qtechBfdAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qtechBfdAdminStatus.setStatus('current')
qtechBfdSessNotificationsEnable = MibScalar((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qtechBfdSessNotificationsEnable.setStatus('current')
qtechBfdSessTable = MibTable((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2), )
if mibBuilder.loadTexts: qtechBfdSessTable.setStatus('current')
qtechBfdSessEntry = MibTableRow((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1), ).setIndexNames((0, "QTECH-BFD-MIB", "qtechBfdSessIndex"))
if mibBuilder.loadTexts: qtechBfdSessEntry.setStatus('current')
qtechBfdSessIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 1), QtechBfdSessIndexTC())
if mibBuilder.loadTexts: qtechBfdSessIndex.setStatus('current')
qtechBfdSessVersionNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qtechBfdSessVersionNumber.setStatus('current')
qtechBfdSessType = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 3), QtechBfdSessTypeTC()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qtechBfdSessType.setStatus('current')
qtechBfdSessDiscriminator = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: qtechBfdSessDiscriminator.setStatus('current')
qtechBfdSessRemoteDiscr = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 5), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 4294967295), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: qtechBfdSessRemoteDiscr.setStatus('current')
qtechBfdSessDestinationUdpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 6), QtechBfdCtrlDestPortNumberTC()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qtechBfdSessDestinationUdpPort.setStatus('current')
qtechBfdSessSourceUdpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 7), QtechBfdCtrlSourcePortNumberTC()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qtechBfdSessSourceUdpPort.setStatus('current')
qtechBfdSessEchoSourceUdpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 8), InetPortNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qtechBfdSessEchoSourceUdpPort.setStatus('current')
qtechBfdSessAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("stop", 1), ("start", 2))).clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qtechBfdSessAdminStatus.setStatus('current')
qtechBfdSessState = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 10), QtechBfdSessStateTC().clone(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: qtechBfdSessState.setStatus('current')
qtechBfdSessRemoteHeardFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 11), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: qtechBfdSessRemoteHeardFlag.setStatus('current')
qtechBfdSessDiag = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 12), QtechBfdDiagTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qtechBfdSessDiag.setStatus('current')
qtechBfdSessOperMode = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 13), QtechBfdSessOperModeTC()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qtechBfdSessOperMode.setStatus('current')
qtechBfdSessDemandModeDesiredFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 14), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qtechBfdSessDemandModeDesiredFlag.setStatus('current')
qtechBfdSessControlPlaneIndepFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 15), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qtechBfdSessControlPlaneIndepFlag.setStatus('current')
qtechBfdSessMultipointFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 16), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qtechBfdSessMultipointFlag.setStatus('current')
qtechBfdSessInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 17), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qtechBfdSessInterface.setStatus('current')
qtechBfdSessSrcAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 18), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qtechBfdSessSrcAddrType.setStatus('current')
qtechBfdSessSrcAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 19), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qtechBfdSessSrcAddr.setStatus('current')
qtechBfdSessDstAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 20), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qtechBfdSessDstAddrType.setStatus('current')
qtechBfdSessDstAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 21), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qtechBfdSessDstAddr.setStatus('current')
qtechBfdSessGTSM = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 22), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qtechBfdSessGTSM.setStatus('current')
qtechBfdSessGTSMTTL = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 23), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qtechBfdSessGTSMTTL.setStatus('current')
qtechBfdSessDesiredMinTxInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 24), QtechBfdIntervalTC()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qtechBfdSessDesiredMinTxInterval.setStatus('current')
qtechBfdSessReqMinRxInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 25), QtechBfdIntervalTC()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qtechBfdSessReqMinRxInterval.setStatus('current')
qtechBfdSessReqMinEchoRxInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 26), QtechBfdIntervalTC()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qtechBfdSessReqMinEchoRxInterval.setStatus('current')
qtechBfdSessDetectMult = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 27), QtechBfdMultiplierTC()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qtechBfdSessDetectMult.setStatus('current')
qtechBfdSessNegotiatedInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 28), QtechBfdIntervalTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qtechBfdSessNegotiatedInterval.setStatus('current')
qtechBfdSessNegotiatedEchoInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 29), QtechBfdIntervalTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qtechBfdSessNegotiatedEchoInterval.setStatus('current')
qtechBfdSessNegotiatedDetectMult = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 30), QtechBfdMultiplierTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qtechBfdSessNegotiatedDetectMult.setStatus('current')
qtechBfdSessAuthPresFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 31), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qtechBfdSessAuthPresFlag.setStatus('current')
qtechBfdSessAuthenticationType = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 32), QtechBfdSessAuthenticationTypeTC().clone(-1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qtechBfdSessAuthenticationType.setStatus('current')
qtechBfdSessAuthenticationKeyID = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 33), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 255), )).clone(-1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qtechBfdSessAuthenticationKeyID.setStatus('current')
qtechBfdSessAuthenticationKey = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 34), QtechBfdSessionAuthenticationKeyTC()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qtechBfdSessAuthenticationKey.setStatus('current')
qtechBfdSessStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 35), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qtechBfdSessStorageType.setStatus('current')
qtechBfdSessRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 2, 1, 36), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qtechBfdSessRowStatus.setStatus('current')
qtechBfdSessPerfTable = MibTable((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 3), )
if mibBuilder.loadTexts: qtechBfdSessPerfTable.setStatus('current')
qtechBfdSessPerfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 3, 1), )
qtechBfdSessEntry.registerAugmentions(("QTECH-BFD-MIB", "qtechBfdSessPerfEntry"))
qtechBfdSessPerfEntry.setIndexNames(*qtechBfdSessEntry.getIndexNames())
if mibBuilder.loadTexts: qtechBfdSessPerfEntry.setStatus('current')
qtechBfdSessPerfCtrlPktIn = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 3, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qtechBfdSessPerfCtrlPktIn.setStatus('current')
qtechBfdSessPerfCtrlPktOut = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qtechBfdSessPerfCtrlPktOut.setStatus('current')
qtechBfdSessPerfCtrlPktDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qtechBfdSessPerfCtrlPktDrop.setStatus('current')
qtechBfdSessPerfCtrlPktDropLastTime = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 3, 1, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qtechBfdSessPerfCtrlPktDropLastTime.setStatus('current')
qtechBfdSessPerfEchoPktIn = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qtechBfdSessPerfEchoPktIn.setStatus('current')
qtechBfdSessPerfEchoPktOut = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qtechBfdSessPerfEchoPktOut.setStatus('current')
qtechBfdSessPerfEchoPktDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qtechBfdSessPerfEchoPktDrop.setStatus('current')
qtechBfdSessPerfEchoPktDropLastTime = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 3, 1, 8), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qtechBfdSessPerfEchoPktDropLastTime.setStatus('current')
qtechBfdSessUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 3, 1, 9), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qtechBfdSessUpTime.setStatus('current')
qtechBfdSessPerfLastSessDownTime = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 3, 1, 10), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qtechBfdSessPerfLastSessDownTime.setStatus('current')
qtechBfdSessPerfLastCommLostDiag = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 3, 1, 11), QtechBfdDiagTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qtechBfdSessPerfLastCommLostDiag.setStatus('current')
qtechBfdSessPerfSessUpCount = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 3, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qtechBfdSessPerfSessUpCount.setStatus('current')
qtechBfdSessPerfDiscTime = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 3, 1, 13), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qtechBfdSessPerfDiscTime.setStatus('current')
qtechBfdSessPerfCtrlPktInHC = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 3, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qtechBfdSessPerfCtrlPktInHC.setStatus('current')
qtechBfdSessPerfCtrlPktOutHC = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 3, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qtechBfdSessPerfCtrlPktOutHC.setStatus('current')
qtechBfdSessPerfCtrlPktDropHC = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 3, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qtechBfdSessPerfCtrlPktDropHC.setStatus('current')
qtechBfdSessPerfEchoPktInHC = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 3, 1, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qtechBfdSessPerfEchoPktInHC.setStatus('current')
qtechBfdSessPerfEchoPktOutHC = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 3, 1, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qtechBfdSessPerfEchoPktOutHC.setStatus('current')
qtechBfdSessPerfEchoPktDropHC = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 3, 1, 19), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qtechBfdSessPerfEchoPktDropHC.setStatus('current')
qtechBfdSessDiscMapTable = MibTable((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 4), )
if mibBuilder.loadTexts: qtechBfdSessDiscMapTable.setStatus('current')
qtechBfdSessDiscMapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 4, 1), ).setIndexNames((0, "QTECH-BFD-MIB", "qtechBfdSessDiscriminator"))
if mibBuilder.loadTexts: qtechBfdSessDiscMapEntry.setStatus('current')
qtechBfdSessDiscMapIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 4, 1, 1), QtechBfdSessIndexTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qtechBfdSessDiscMapIndex.setStatus('current')
qtechBfdSessDiscMapStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 4, 1, 2), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qtechBfdSessDiscMapStorageType.setStatus('current')
qtechBfdSessDiscMapRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 4, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qtechBfdSessDiscMapRowStatus.setStatus('current')
qtechBfdSessIpMapTable = MibTable((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 5), )
if mibBuilder.loadTexts: qtechBfdSessIpMapTable.setStatus('current')
qtechBfdSessIpMapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 5, 1), ).setIndexNames((0, "QTECH-BFD-MIB", "qtechBfdSessInterface"), (0, "QTECH-BFD-MIB", "qtechBfdSessSrcAddrType"), (0, "QTECH-BFD-MIB", "qtechBfdSessSrcAddr"), (0, "QTECH-BFD-MIB", "qtechBfdSessDstAddrType"), (0, "QTECH-BFD-MIB", "qtechBfdSessDstAddr"))
if mibBuilder.loadTexts: qtechBfdSessIpMapEntry.setStatus('current')
qtechBfdSessIpMapIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 5, 1, 1), QtechBfdSessIndexTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qtechBfdSessIpMapIndex.setStatus('current')
qtechBfdSessIpMapStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 5, 1, 2), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qtechBfdSessIpMapStorageType.setStatus('current')
qtechBfdSessIpMapRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 1, 5, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qtechBfdSessIpMapRowStatus.setStatus('current')
qtechBfdSessUp = NotificationType((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 0, 1)).setObjects(("QTECH-BFD-MIB", "qtechBfdSessDiag"), ("QTECH-BFD-MIB", "qtechBfdSessDiag"))
if mibBuilder.loadTexts: qtechBfdSessUp.setStatus('current')
qtechBfdSessDown = NotificationType((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 0, 2)).setObjects(("QTECH-BFD-MIB", "qtechBfdSessDiag"), ("QTECH-BFD-MIB", "qtechBfdSessDiag"))
if mibBuilder.loadTexts: qtechBfdSessDown.setStatus('current')
qtechBfdGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 2, 1))
qtechBfdCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 2, 2))
qtechBfdModuleFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 2, 2, 1)).setObjects(("QTECH-BFD-MIB", "qtechBfdSessionGroup"), ("QTECH-BFD-MIB", "qtechBfdSessionReadOnlyGroup"), ("QTECH-BFD-MIB", "qtechBfdSessionPerfGroup"), ("QTECH-BFD-MIB", "qtechBfdNotificationGroup"), ("QTECH-BFD-MIB", "qtechBfdSessionPerfHCGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qtechBfdModuleFullCompliance = qtechBfdModuleFullCompliance.setStatus('current')
qtechBfdModuleReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 2, 2, 2)).setObjects(("QTECH-BFD-MIB", "qtechBfdSessionGroup"), ("QTECH-BFD-MIB", "qtechBfdSessionReadOnlyGroup"), ("QTECH-BFD-MIB", "qtechBfdSessionPerfGroup"), ("QTECH-BFD-MIB", "qtechBfdNotificationGroup"), ("QTECH-BFD-MIB", "qtechBfdSessionPerfHCGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qtechBfdModuleReadOnlyCompliance = qtechBfdModuleReadOnlyCompliance.setStatus('current')
qtechBfdSessionGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 2, 1, 1)).setObjects(("QTECH-BFD-MIB", "qtechBfdAdminStatus"), ("QTECH-BFD-MIB", "qtechBfdSessNotificationsEnable"), ("QTECH-BFD-MIB", "qtechBfdSessVersionNumber"), ("QTECH-BFD-MIB", "qtechBfdSessType"), ("QTECH-BFD-MIB", "qtechBfdSessDestinationUdpPort"), ("QTECH-BFD-MIB", "qtechBfdSessSourceUdpPort"), ("QTECH-BFD-MIB", "qtechBfdSessEchoSourceUdpPort"), ("QTECH-BFD-MIB", "qtechBfdSessAdminStatus"), ("QTECH-BFD-MIB", "qtechBfdSessOperMode"), ("QTECH-BFD-MIB", "qtechBfdSessDemandModeDesiredFlag"), ("QTECH-BFD-MIB", "qtechBfdSessControlPlaneIndepFlag"), ("QTECH-BFD-MIB", "qtechBfdSessMultipointFlag"), ("QTECH-BFD-MIB", "qtechBfdSessInterface"), ("QTECH-BFD-MIB", "qtechBfdSessSrcAddrType"), ("QTECH-BFD-MIB", "qtechBfdSessSrcAddr"), ("QTECH-BFD-MIB", "qtechBfdSessDstAddrType"), ("QTECH-BFD-MIB", "qtechBfdSessDstAddr"), ("QTECH-BFD-MIB", "qtechBfdSessGTSM"), ("QTECH-BFD-MIB", "qtechBfdSessGTSMTTL"), ("QTECH-BFD-MIB", "qtechBfdSessDesiredMinTxInterval"), ("QTECH-BFD-MIB", "qtechBfdSessReqMinRxInterval"), ("QTECH-BFD-MIB", "qtechBfdSessReqMinEchoRxInterval"), ("QTECH-BFD-MIB", "qtechBfdSessDetectMult"), ("QTECH-BFD-MIB", "qtechBfdSessAuthPresFlag"), ("QTECH-BFD-MIB", "qtechBfdSessAuthenticationType"), ("QTECH-BFD-MIB", "qtechBfdSessAuthenticationKeyID"), ("QTECH-BFD-MIB", "qtechBfdSessAuthenticationKey"), ("QTECH-BFD-MIB", "qtechBfdSessStorageType"), ("QTECH-BFD-MIB", "qtechBfdSessRowStatus"), ("QTECH-BFD-MIB", "qtechBfdSessDiscMapStorageType"), ("QTECH-BFD-MIB", "qtechBfdSessDiscMapRowStatus"), ("QTECH-BFD-MIB", "qtechBfdSessIpMapStorageType"), ("QTECH-BFD-MIB", "qtechBfdSessIpMapRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qtechBfdSessionGroup = qtechBfdSessionGroup.setStatus('current')
qtechBfdSessionReadOnlyGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 2, 1, 2)).setObjects(("QTECH-BFD-MIB", "qtechBfdSessDiscriminator"), ("QTECH-BFD-MIB", "qtechBfdSessRemoteDiscr"), ("QTECH-BFD-MIB", "qtechBfdSessState"), ("QTECH-BFD-MIB", "qtechBfdSessRemoteHeardFlag"), ("QTECH-BFD-MIB", "qtechBfdSessDiag"), ("QTECH-BFD-MIB", "qtechBfdSessNegotiatedInterval"), ("QTECH-BFD-MIB", "qtechBfdSessNegotiatedEchoInterval"), ("QTECH-BFD-MIB", "qtechBfdSessNegotiatedDetectMult"), ("QTECH-BFD-MIB", "qtechBfdSessDiscMapIndex"), ("QTECH-BFD-MIB", "qtechBfdSessIpMapIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qtechBfdSessionReadOnlyGroup = qtechBfdSessionReadOnlyGroup.setStatus('current')
qtechBfdSessionPerfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 2, 1, 3)).setObjects(("QTECH-BFD-MIB", "qtechBfdSessPerfCtrlPktIn"), ("QTECH-BFD-MIB", "qtechBfdSessPerfCtrlPktOut"), ("QTECH-BFD-MIB", "qtechBfdSessPerfCtrlPktDrop"), ("QTECH-BFD-MIB", "qtechBfdSessPerfCtrlPktDropLastTime"), ("QTECH-BFD-MIB", "qtechBfdSessPerfEchoPktIn"), ("QTECH-BFD-MIB", "qtechBfdSessPerfEchoPktOut"), ("QTECH-BFD-MIB", "qtechBfdSessPerfEchoPktDrop"), ("QTECH-BFD-MIB", "qtechBfdSessPerfEchoPktDropLastTime"), ("QTECH-BFD-MIB", "qtechBfdSessUpTime"), ("QTECH-BFD-MIB", "qtechBfdSessPerfLastSessDownTime"), ("QTECH-BFD-MIB", "qtechBfdSessPerfLastCommLostDiag"), ("QTECH-BFD-MIB", "qtechBfdSessPerfSessUpCount"), ("QTECH-BFD-MIB", "qtechBfdSessPerfDiscTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qtechBfdSessionPerfGroup = qtechBfdSessionPerfGroup.setStatus('current')
qtechBfdSessionPerfHCGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 2, 1, 4)).setObjects(("QTECH-BFD-MIB", "qtechBfdSessPerfCtrlPktInHC"), ("QTECH-BFD-MIB", "qtechBfdSessPerfCtrlPktOutHC"), ("QTECH-BFD-MIB", "qtechBfdSessPerfCtrlPktDropHC"), ("QTECH-BFD-MIB", "qtechBfdSessPerfEchoPktInHC"), ("QTECH-BFD-MIB", "qtechBfdSessPerfEchoPktOutHC"), ("QTECH-BFD-MIB", "qtechBfdSessPerfEchoPktDropHC"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qtechBfdSessionPerfHCGroup = qtechBfdSessionPerfHCGroup.setStatus('current')
qtechBfdNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 48, 2, 1, 5)).setObjects(("QTECH-BFD-MIB", "qtechBfdSessUp"), ("QTECH-BFD-MIB", "qtechBfdSessDown"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qtechBfdNotificationGroup = qtechBfdNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("QTECH-BFD-MIB", qtechBfdSessType=qtechBfdSessType, qtechBfdSessState=qtechBfdSessState, qtechBfdObjects=qtechBfdObjects, QtechBfdSessStateTC=QtechBfdSessStateTC, qtechBfdSessStorageType=qtechBfdSessStorageType, qtechBfdSessDstAddrType=qtechBfdSessDstAddrType, qtechBfdSessDiscMapTable=qtechBfdSessDiscMapTable, qtechBfdScalarObjects=qtechBfdScalarObjects, qtechBfdSessGTSM=qtechBfdSessGTSM, qtechBfdSessPerfCtrlPktDropHC=qtechBfdSessPerfCtrlPktDropHC, qtechBfdSessPerfEchoPktDrop=qtechBfdSessPerfEchoPktDrop, qtechBfdSessDiscMapEntry=qtechBfdSessDiscMapEntry, qtechBfdSessPerfEchoPktIn=qtechBfdSessPerfEchoPktIn, QtechBfdIntervalTC=QtechBfdIntervalTC, qtechBfdSessPerfTable=qtechBfdSessPerfTable, qtechBfdCompliances=qtechBfdCompliances, qtechBfdSessPerfCtrlPktIn=qtechBfdSessPerfCtrlPktIn, qtechBfdSessionGroup=qtechBfdSessionGroup, qtechBfdModuleReadOnlyCompliance=qtechBfdModuleReadOnlyCompliance, qtechBfdSessUpTime=qtechBfdSessUpTime, qtechBfdSessNotificationsEnable=qtechBfdSessNotificationsEnable, qtechBfdConformance=qtechBfdConformance, qtechBfdAdminStatus=qtechBfdAdminStatus, qtechBfdSessSourceUdpPort=qtechBfdSessSourceUdpPort, QtechBfdSessOperModeTC=QtechBfdSessOperModeTC, qtechBfdSessDesiredMinTxInterval=qtechBfdSessDesiredMinTxInterval, qtechBfdSessRowStatus=qtechBfdSessRowStatus, qtechBfdNotifications=qtechBfdNotifications, qtechBfdSessionReadOnlyGroup=qtechBfdSessionReadOnlyGroup, qtechBfdSessDstAddr=qtechBfdSessDstAddr, qtechBfdSessReqMinEchoRxInterval=qtechBfdSessReqMinEchoRxInterval, qtechBfdSessPerfCtrlPktOutHC=qtechBfdSessPerfCtrlPktOutHC, qtechBfdSessSrcAddrType=qtechBfdSessSrcAddrType, qtechBfdSessEchoSourceUdpPort=qtechBfdSessEchoSourceUdpPort, qtechBfdSessAdminStatus=qtechBfdSessAdminStatus, qtechBfdSessPerfEchoPktInHC=qtechBfdSessPerfEchoPktInHC, qtechBfdSessDiscMapRowStatus=qtechBfdSessDiscMapRowStatus, QtechBfdDiagTC=QtechBfdDiagTC, qtechBfdSessDiscMapStorageType=qtechBfdSessDiscMapStorageType, qtechBfdSessIpMapStorageType=qtechBfdSessIpMapStorageType, qtechBfdSessAuthenticationKey=qtechBfdSessAuthenticationKey, qtechBfdSessPerfEchoPktOutHC=qtechBfdSessPerfEchoPktOutHC, QtechBfdSessionAuthenticationKeyTC=QtechBfdSessionAuthenticationKeyTC, QtechBfdSessAuthenticationTypeTC=QtechBfdSessAuthenticationTypeTC, qtechBfdSessIpMapIndex=qtechBfdSessIpMapIndex, qtechBfdSessPerfEchoPktOut=qtechBfdSessPerfEchoPktOut, QtechBfdCtrlSourcePortNumberTC=QtechBfdCtrlSourcePortNumberTC, qtechBfdSessPerfCtrlPktInHC=qtechBfdSessPerfCtrlPktInHC, qtechBfdSessAuthenticationKeyID=qtechBfdSessAuthenticationKeyID, qtechBfdSessInterface=qtechBfdSessInterface, qtechBfdSessIpMapEntry=qtechBfdSessIpMapEntry, qtechBfdSessDown=qtechBfdSessDown, qtechBfdSessUp=qtechBfdSessUp, qtechBfdSessDiag=qtechBfdSessDiag, qtechBfdGroups=qtechBfdGroups, qtechBfdSessEntry=qtechBfdSessEntry, qtechBfdSessAuthenticationType=qtechBfdSessAuthenticationType, qtechBfdSessPerfCtrlPktOut=qtechBfdSessPerfCtrlPktOut, qtechBfdSessGTSMTTL=qtechBfdSessGTSMTTL, qtechBfdSessTable=qtechBfdSessTable, qtechBfdSessReqMinRxInterval=qtechBfdSessReqMinRxInterval, qtechBfdSessPerfSessUpCount=qtechBfdSessPerfSessUpCount, qtechBfdSessDiscMapIndex=qtechBfdSessDiscMapIndex, qtechBfdSessIpMapTable=qtechBfdSessIpMapTable, qtechBfdSessDemandModeDesiredFlag=qtechBfdSessDemandModeDesiredFlag, qtechBfdSessPerfEchoPktDropHC=qtechBfdSessPerfEchoPktDropHC, qtechBfdSessionPerfHCGroup=qtechBfdSessionPerfHCGroup, qtechBfdModuleFullCompliance=qtechBfdModuleFullCompliance, qtechBfdSessIndex=qtechBfdSessIndex, qtechBfdSessRemoteDiscr=qtechBfdSessRemoteDiscr, qtechBfdSessSrcAddr=qtechBfdSessSrcAddr, qtechBfdSessOperMode=qtechBfdSessOperMode, PYSNMP_MODULE_ID=qtechBfdMIB, qtechBfdSessRemoteHeardFlag=qtechBfdSessRemoteHeardFlag, QtechBfdSessTypeTC=QtechBfdSessTypeTC, QtechBfdCtrlDestPortNumberTC=QtechBfdCtrlDestPortNumberTC, qtechBfdSessIpMapRowStatus=qtechBfdSessIpMapRowStatus, qtechBfdSessPerfEntry=qtechBfdSessPerfEntry, qtechBfdMIB=qtechBfdMIB, qtechBfdSessDestinationUdpPort=qtechBfdSessDestinationUdpPort, qtechBfdSessPerfEchoPktDropLastTime=qtechBfdSessPerfEchoPktDropLastTime, qtechBfdSessControlPlaneIndepFlag=qtechBfdSessControlPlaneIndepFlag, qtechBfdSessPerfCtrlPktDrop=qtechBfdSessPerfCtrlPktDrop, QtechBfdMultiplierTC=QtechBfdMultiplierTC, qtechBfdSessPerfLastSessDownTime=qtechBfdSessPerfLastSessDownTime, qtechBfdSessNegotiatedDetectMult=qtechBfdSessNegotiatedDetectMult, qtechBfdSessNegotiatedInterval=qtechBfdSessNegotiatedInterval, QtechBfdSessIndexTC=QtechBfdSessIndexTC, qtechBfdSessPerfDiscTime=qtechBfdSessPerfDiscTime, qtechBfdSessDetectMult=qtechBfdSessDetectMult, qtechBfdSessAuthPresFlag=qtechBfdSessAuthPresFlag, qtechBfdSessDiscriminator=qtechBfdSessDiscriminator, qtechBfdSessVersionNumber=qtechBfdSessVersionNumber, qtechBfdSessPerfCtrlPktDropLastTime=qtechBfdSessPerfCtrlPktDropLastTime, qtechBfdSessNegotiatedEchoInterval=qtechBfdSessNegotiatedEchoInterval, qtechBfdSessPerfLastCommLostDiag=qtechBfdSessPerfLastCommLostDiag, qtechBfdNotificationGroup=qtechBfdNotificationGroup, qtechBfdSessMultipointFlag=qtechBfdSessMultipointFlag, qtechBfdSessionPerfGroup=qtechBfdSessionPerfGroup)
