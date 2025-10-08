#
# PySNMP MIB module CISCO-SDWAN-APP-ROUTE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-SDWAN-APP-ROUTE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:16:30 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Integer32, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Counter64, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Counter64", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSdwanAppRouteMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 1001))
ciscoSdwanAppRouteMIB.setRevisions(('2021-01-26 00:00',))
if mibBuilder.loadTexts: ciscoSdwanAppRouteMIB.setLastUpdated('202101260000Z')
if mibBuilder.loadTexts: ciscoSdwanAppRouteMIB.setOrganization('Cisco Systems, Inc. ')
class UnsignedByte(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class UnsignedShort(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class ConfdString(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class String(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class InetAddressIP(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1d.'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(16, 16), )
ciscoSdwanAppRouteMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1))
ciscoSdwanAppRouteMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 1001, 3))
appRouteStatisticsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 2), )
if mibBuilder.loadTexts: appRouteStatisticsTable.setStatus('current')
appRouteStatisticsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 2, 1), ).setIndexNames((0, "CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsSrcIp"), (0, "CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsDstIp"), (0, "CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsProto"), (0, "CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsSrcPort"), (0, "CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsDstPort"))
if mibBuilder.loadTexts: appRouteStatisticsEntry.setStatus('current')
appRouteStatisticsSrcIp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 2, 1, 1), InetAddressIP())
if mibBuilder.loadTexts: appRouteStatisticsSrcIp.setStatus('current')
appRouteStatisticsDstIp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 2, 1, 2), InetAddressIP())
if mibBuilder.loadTexts: appRouteStatisticsDstIp.setStatus('current')
appRouteStatisticsProto = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("gre", 1), ("ipsec", 2))))
if mibBuilder.loadTexts: appRouteStatisticsProto.setStatus('current')
appRouteStatisticsSrcPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 2, 1, 4), UnsignedShort())
if mibBuilder.loadTexts: appRouteStatisticsSrcPort.setStatus('current')
appRouteStatisticsDstPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 2, 1, 5), UnsignedShort())
if mibBuilder.loadTexts: appRouteStatisticsDstPort.setStatus('current')
appRouteStatisticsRemoteSystemIp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 2, 1, 6), InetAddressIP()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appRouteStatisticsRemoteSystemIp.setStatus('current')
appRouteStatisticsLocalColor = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22))).clone(namedValues=NamedValues(("default", 1), ("mpls", 2), ("metroEthernet", 3), ("bizInternet", 4), ("publicInternet", 5), ("lte", 6), ("threeG", 7), ("red", 8), ("green", 9), ("blue", 10), ("gold", 11), ("silver", 12), ("bronze", 13), ("custom1", 14), ("custom2", 15), ("custom3", 16), ("private1", 17), ("private2", 18), ("private3", 19), ("private4", 20), ("private5", 21), ("private6", 22)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: appRouteStatisticsLocalColor.setStatus('current')
appRouteStatisticsRemoteColor = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22))).clone(namedValues=NamedValues(("default", 1), ("mpls", 2), ("metroEthernet", 3), ("bizInternet", 4), ("publicInternet", 5), ("lte", 6), ("threeG", 7), ("red", 8), ("green", 9), ("blue", 10), ("gold", 11), ("silver", 12), ("bronze", 13), ("custom1", 14), ("custom2", 15), ("custom3", 16), ("private1", 17), ("private2", 18), ("private3", 19), ("private4", 20), ("private5", 21), ("private6", 22)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: appRouteStatisticsRemoteColor.setStatus('current')
appRouteStatisticsAppProbeClassTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 5), )
if mibBuilder.loadTexts: appRouteStatisticsAppProbeClassTable.setStatus('current')
appRouteStatisticsAppProbeClassEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 5, 1), ).setIndexNames((0, "CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsSrcIp"), (0, "CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsDstIp"), (0, "CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsProto"), (0, "CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsSrcPort"), (0, "CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsDstPort"), (0, "CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsAppProbeClassName"))
if mibBuilder.loadTexts: appRouteStatisticsAppProbeClassEntry.setStatus('current')
appRouteStatisticsAppProbeClassName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 5, 1, 1), String().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: appRouteStatisticsAppProbeClassName.setStatus('current')
appRouteStatisticsAppProbeClassMeanLoss = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 5, 1, 2), UnsignedByte()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appRouteStatisticsAppProbeClassMeanLoss.setStatus('current')
appRouteStatisticsAppProbeClassMeanLatency = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 5, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appRouteStatisticsAppProbeClassMeanLatency.setStatus('current')
appRouteStatisticsAppProbeClassMeanJitter = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 5, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appRouteStatisticsAppProbeClassMeanJitter.setStatus('current')
appRouteStatisticsAppProbeClassIntervalTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 6), )
if mibBuilder.loadTexts: appRouteStatisticsAppProbeClassIntervalTable.setStatus('current')
appRouteStatisticsAppProbeClassIntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 6, 1), ).setIndexNames((0, "CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsSrcIp"), (0, "CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsDstIp"), (0, "CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsProto"), (0, "CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsSrcPort"), (0, "CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsDstPort"), (0, "CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsAppProbeClassName"), (0, "CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsAppProbeClassIntervalIndex"))
if mibBuilder.loadTexts: appRouteStatisticsAppProbeClassIntervalEntry.setStatus('current')
appRouteStatisticsAppProbeClassIntervalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 6, 1, 1), UnsignedByte())
if mibBuilder.loadTexts: appRouteStatisticsAppProbeClassIntervalIndex.setStatus('current')
appRouteStatisticsAppProbeClassIntervalTotalPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 6, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appRouteStatisticsAppProbeClassIntervalTotalPackets.setStatus('current')
appRouteStatisticsAppProbeClassIntervalLoss = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 6, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appRouteStatisticsAppProbeClassIntervalLoss.setStatus('current')
appRouteStatisticsAppProbeClassIntervalAverageLatency = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 6, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appRouteStatisticsAppProbeClassIntervalAverageLatency.setStatus('current')
appRouteStatisticsAppProbeClassIntervalAverageJitter = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 6, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appRouteStatisticsAppProbeClassIntervalAverageJitter.setStatus('current')
appRouteStatisticsAppProbeClassIntervalTxDataPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 6, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appRouteStatisticsAppProbeClassIntervalTxDataPkts.setStatus('current')
appRouteStatisticsAppProbeClassIntervalRxDataPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 6, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appRouteStatisticsAppProbeClassIntervalRxDataPkts.setStatus('current')
appRouteStatisticsAppProbeClassIntervalIpv6TxDataPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 6, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appRouteStatisticsAppProbeClassIntervalIpv6TxDataPkts.setStatus('current')
appRouteStatisticsAppProbeClassIntervalIpv6RxDataPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 6, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appRouteStatisticsAppProbeClassIntervalIpv6RxDataPkts.setStatus('current')
appRouteSlaClassTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 4), )
if mibBuilder.loadTexts: appRouteSlaClassTable.setStatus('current')
appRouteSlaClassEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 4, 1), ).setIndexNames((0, "CISCO-SDWAN-APP-ROUTE-MIB", "appRouteSlaClassIndex"))
if mibBuilder.loadTexts: appRouteSlaClassEntry.setStatus('current')
appRouteSlaClassIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 4, 1, 1), UnsignedByte())
if mibBuilder.loadTexts: appRouteSlaClassIndex.setStatus('current')
appRouteSlaClassName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 4, 1, 2), String()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appRouteSlaClassName.setStatus('current')
appRouteSlaClassLoss = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 4, 1, 3), UnsignedByte()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appRouteSlaClassLoss.setStatus('current')
appRouteSlaClassLatency = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 4, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appRouteSlaClassLatency.setStatus('current')
appRouteSlaClassJitter = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 4, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appRouteSlaClassJitter.setStatus('current')
ciscoSdwanAppRouteMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 1001, 3, 1))
ciscoSdwanAppRouteMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 1001, 3, 2))
ciscoSdwanAppRouteMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 1001, 3, 1, 1)).setObjects(("CISCO-SDWAN-APP-ROUTE-MIB", "cSdwanAppRouteStatisticsGroup"), ("CISCO-SDWAN-APP-ROUTE-MIB", "cSdwanAppRouteStatisticsAppProbeClassGroup"), ("CISCO-SDWAN-APP-ROUTE-MIB", "cSdwanAppRouteStatisticsAppProbeClassIntervalGroup"), ("CISCO-SDWAN-APP-ROUTE-MIB", "cSdwanAppRouteSlaClassGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSdwanAppRouteMIBCompliance = ciscoSdwanAppRouteMIBCompliance.setStatus('current')
cSdwanAppRouteStatisticsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 1001, 3, 2, 1)).setObjects(("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsRemoteSystemIp"), ("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsLocalColor"), ("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsRemoteColor"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSdwanAppRouteStatisticsGroup = cSdwanAppRouteStatisticsGroup.setStatus('current')
cSdwanAppRouteStatisticsAppProbeClassGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 1001, 3, 2, 2)).setObjects(("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsAppProbeClassName"), ("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsAppProbeClassMeanLoss"), ("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsAppProbeClassMeanLatency"), ("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsAppProbeClassMeanJitter"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSdwanAppRouteStatisticsAppProbeClassGroup = cSdwanAppRouteStatisticsAppProbeClassGroup.setStatus('current')
cSdwanAppRouteStatisticsAppProbeClassIntervalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 1001, 3, 2, 3)).setObjects(("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsAppProbeClassIntervalTotalPackets"), ("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsAppProbeClassIntervalLoss"), ("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsAppProbeClassIntervalAverageLatency"), ("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsAppProbeClassIntervalAverageJitter"), ("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsAppProbeClassIntervalTxDataPkts"), ("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsAppProbeClassIntervalRxDataPkts"), ("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsAppProbeClassIntervalIpv6TxDataPkts"), ("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsAppProbeClassIntervalIpv6RxDataPkts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSdwanAppRouteStatisticsAppProbeClassIntervalGroup = cSdwanAppRouteStatisticsAppProbeClassIntervalGroup.setStatus('current')
cSdwanAppRouteSlaClassGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 1001, 3, 2, 4)).setObjects(("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteSlaClassName"), ("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteSlaClassLoss"), ("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteSlaClassLatency"), ("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteSlaClassJitter"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSdwanAppRouteSlaClassGroup = cSdwanAppRouteSlaClassGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-SDWAN-APP-ROUTE-MIB", appRouteStatisticsAppProbeClassIntervalAverageJitter=appRouteStatisticsAppProbeClassIntervalAverageJitter, UnsignedByte=UnsignedByte, appRouteStatisticsAppProbeClassMeanLoss=appRouteStatisticsAppProbeClassMeanLoss, appRouteStatisticsAppProbeClassIntervalTxDataPkts=appRouteStatisticsAppProbeClassIntervalTxDataPkts, ciscoSdwanAppRouteMIBCompliances=ciscoSdwanAppRouteMIBCompliances, appRouteStatisticsRemoteColor=appRouteStatisticsRemoteColor, appRouteStatisticsAppProbeClassIntervalLoss=appRouteStatisticsAppProbeClassIntervalLoss, appRouteStatisticsDstPort=appRouteStatisticsDstPort, cSdwanAppRouteSlaClassGroup=cSdwanAppRouteSlaClassGroup, appRouteStatisticsDstIp=appRouteStatisticsDstIp, appRouteStatisticsLocalColor=appRouteStatisticsLocalColor, appRouteStatisticsAppProbeClassIntervalRxDataPkts=appRouteStatisticsAppProbeClassIntervalRxDataPkts, cSdwanAppRouteStatisticsAppProbeClassGroup=cSdwanAppRouteStatisticsAppProbeClassGroup, appRouteStatisticsSrcPort=appRouteStatisticsSrcPort, appRouteStatisticsProto=appRouteStatisticsProto, appRouteStatisticsAppProbeClassMeanLatency=appRouteStatisticsAppProbeClassMeanLatency, PYSNMP_MODULE_ID=ciscoSdwanAppRouteMIB, appRouteStatisticsAppProbeClassName=appRouteStatisticsAppProbeClassName, appRouteStatisticsAppProbeClassIntervalIndex=appRouteStatisticsAppProbeClassIntervalIndex, appRouteStatisticsAppProbeClassIntervalIpv6TxDataPkts=appRouteStatisticsAppProbeClassIntervalIpv6TxDataPkts, UnsignedShort=UnsignedShort, appRouteStatisticsTable=appRouteStatisticsTable, appRouteSlaClassTable=appRouteSlaClassTable, appRouteSlaClassEntry=appRouteSlaClassEntry, cSdwanAppRouteStatisticsAppProbeClassIntervalGroup=cSdwanAppRouteStatisticsAppProbeClassIntervalGroup, ciscoSdwanAppRouteMIBObjects=ciscoSdwanAppRouteMIBObjects, appRouteSlaClassLoss=appRouteSlaClassLoss, appRouteStatisticsRemoteSystemIp=appRouteStatisticsRemoteSystemIp, appRouteStatisticsAppProbeClassIntervalEntry=appRouteStatisticsAppProbeClassIntervalEntry, ConfdString=ConfdString, ciscoSdwanAppRouteMIBConform=ciscoSdwanAppRouteMIBConform, appRouteStatisticsEntry=appRouteStatisticsEntry, appRouteStatisticsAppProbeClassMeanJitter=appRouteStatisticsAppProbeClassMeanJitter, appRouteSlaClassName=appRouteSlaClassName, appRouteSlaClassIndex=appRouteSlaClassIndex, cSdwanAppRouteStatisticsGroup=cSdwanAppRouteStatisticsGroup, appRouteStatisticsAppProbeClassTable=appRouteStatisticsAppProbeClassTable, InetAddressIP=InetAddressIP, ciscoSdwanAppRouteMIBCompliance=ciscoSdwanAppRouteMIBCompliance, appRouteSlaClassLatency=appRouteSlaClassLatency, appRouteStatisticsAppProbeClassIntervalTable=appRouteStatisticsAppProbeClassIntervalTable, ciscoSdwanAppRouteMIBGroups=ciscoSdwanAppRouteMIBGroups, appRouteStatisticsAppProbeClassIntervalTotalPackets=appRouteStatisticsAppProbeClassIntervalTotalPackets, appRouteStatisticsAppProbeClassIntervalIpv6RxDataPkts=appRouteStatisticsAppProbeClassIntervalIpv6RxDataPkts, appRouteStatisticsAppProbeClassEntry=appRouteStatisticsAppProbeClassEntry, String=String, ciscoSdwanAppRouteMIB=ciscoSdwanAppRouteMIB, appRouteSlaClassJitter=appRouteSlaClassJitter, appRouteStatisticsSrcIp=appRouteStatisticsSrcIp, appRouteStatisticsAppProbeClassIntervalAverageLatency=appRouteStatisticsAppProbeClassIntervalAverageLatency)
