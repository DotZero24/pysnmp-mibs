#
# PySNMP MIB module CISCO-SDWAN-PROBE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-SDWAN-PROBE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:11:32 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, TextualConvention = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt", "TextualConvention")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Integer32, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Counter64, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Counter64", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSdwanProbeMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 1008))
ciscoSdwanProbeMIB.setRevisions(('2021-03-01 00:00',))
if mibBuilder.loadTexts: ciscoSdwanProbeMIB.setLastUpdated('202106140000Z')
if mibBuilder.loadTexts: ciscoSdwanProbeMIB.setOrganization('Cisco Systems Inc.')
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

class Ipv4Prefix(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1d.1d.1d.1d/1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(5, 5)
    fixedLength = 5

class InetAddressIP(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(16, 16), )
class String(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class DestinationIp(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class SourceIp(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class TcpFlags(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("syn", 0))

class DataPolicyDirectionEnum(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("from-service", 0), ("from-tunnel", 1), ("all", 2))

class DirectionEnum(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("in", 0), ("out", 1))

class TransportProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("transport-tcp", 0), ("transport-udp", 1))

class ActionDataEnum(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("accept", 0), ("drop", 1))

class FnfMonitorEnum(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("ipv4", 0), ("ipv6", 1), ("both", 2))

class ColorList(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class NotificationSeverity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("critical", 1), ("major", 2), ("minor", 3))

class VpnId(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65530)

ciscoSdwanProbeMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 1008, 1))
ciscoSdwanProbeMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 1008, 3))
probeApplicationsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 2), )
if mibBuilder.loadTexts: probeApplicationsTable.setStatus('current')
probeApplicationsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 2, 1), ).setIndexNames((0, "CISCO-SDWAN-PROBE-MIB", "probeApplicationsVpnId"), (0, "CISCO-SDWAN-PROBE-MIB", "probeApplicationsAppType"), (0, "CISCO-SDWAN-PROBE-MIB", "probeApplicationsAppId"))
if mibBuilder.loadTexts: probeApplicationsEntry.setStatus('current')
probeApplicationsVpnId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: probeApplicationsVpnId.setStatus('current')
probeApplicationsAppType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("cxp-app-type-unset", 0), ("cxp-app-type-app-id", 1), ("cxp-app-type-app-grp", 2), ("cxp-app-type-svc-area", 3), ("cxp-app-type-region", 4), ("cxp-app-type-custom-app-grp", 5))))
if mibBuilder.loadTexts: probeApplicationsAppType.setStatus('current')
probeApplicationsAppId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 2, 1, 3), Unsigned32())
if mibBuilder.loadTexts: probeApplicationsAppId.setStatus('current')
probeApplicationsSubAppId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 2, 1, 4), Unsigned32())
if mibBuilder.loadTexts: probeApplicationsSubAppId.setStatus('current')
probeApplicationsApp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 2, 1, 5), String().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: probeApplicationsApp.setStatus('current')
probeApplicationsExitType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("cxp-exit-unset", 0), ("cxp-exit-gateway", 1), ("cxp-exit-local", 2), ("cxp-exit-uncomputed", 3), ("cxp-exit-none", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: probeApplicationsExitType.setStatus('current')
probeApplicationsGwSysIp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 2, 1, 7), InetAddressIP()).setMaxAccess("readonly")
if mibBuilder.loadTexts: probeApplicationsGwSysIp.setStatus('current')
probeApplicationsInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 2, 1, 8), String().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: probeApplicationsInterface.setStatus('current')
probeApplicationsLatency = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 2, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: probeApplicationsLatency.setStatus('current')
probeApplicationsLoss = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 2, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: probeApplicationsLoss.setStatus('current')
probeApplicationsRemoteColor = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22))).clone(namedValues=NamedValues(("default", 1), ("mpls", 2), ("metro-ethernet", 3), ("biz-internet", 4), ("public-internet", 5), ("lte", 6), ("threeG", 7), ("red", 8), ("green", 9), ("blue", 10), ("gold", 11), ("silver", 12), ("bronze", 13), ("custom1", 14), ("custom2", 15), ("custom3", 16), ("private1", 17), ("private2", 18), ("private3", 19), ("private4", 20), ("private5", 21), ("private6", 22)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: probeApplicationsRemoteColor.setStatus('current')
probeApplicationsLocalColor = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 2, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22))).clone(namedValues=NamedValues(("default", 1), ("mpls", 2), ("metro-ethernet", 3), ("biz-internet", 4), ("public-internet", 5), ("lte", 6), ("threeG", 7), ("red", 8), ("green", 9), ("blue", 10), ("gold", 11), ("silver", 12), ("bronze", 13), ("custom1", 14), ("custom2", 15), ("custom3", 16), ("private1", 17), ("private2", 18), ("private3", 19), ("private4", 20), ("private5", 21), ("private6", 22)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: probeApplicationsLocalColor.setStatus('current')
probeLocalTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 3), )
if mibBuilder.loadTexts: probeLocalTable.setStatus('current')
probeLocalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 3, 1), ).setIndexNames((0, "CISCO-SDWAN-PROBE-MIB", "probeLocalVpnId"), (0, "CISCO-SDWAN-PROBE-MIB", "probeLocalAppType"), (0, "CISCO-SDWAN-PROBE-MIB", "probeLocalAppId"), (0, "CISCO-SDWAN-PROBE-MIB", "probeLocalSubAppId"), (0, "CISCO-SDWAN-PROBE-MIB", "probeLocalInterface"))
if mibBuilder.loadTexts: probeLocalEntry.setStatus('current')
probeLocalVpnId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 3, 1, 1), Unsigned32())
if mibBuilder.loadTexts: probeLocalVpnId.setStatus('current')
probeLocalAppType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("cxp-app-type-unset", 0), ("cxp-app-type-app-id", 1), ("cxp-app-type-app-grp", 2), ("cxp-app-type-svc-area", 3), ("cxp-app-type-region", 4), ("cxp-app-type-custom-app-grp", 5))))
if mibBuilder.loadTexts: probeLocalAppType.setStatus('current')
probeLocalAppId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 3, 1, 3), Unsigned32())
if mibBuilder.loadTexts: probeLocalAppId.setStatus('current')
probeLocalSubAppId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 3, 1, 4), Unsigned32())
if mibBuilder.loadTexts: probeLocalSubAppId.setStatus('current')
probeLocalInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 3, 1, 5), String().subtype(subtypeSpec=ValueSizeConstraint(1, 128)))
if mibBuilder.loadTexts: probeLocalInterface.setStatus('current')
probeLocalApp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 3, 1, 6), String().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: probeLocalApp.setStatus('current')
probeLocalLatency = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 3, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: probeLocalLatency.setStatus('current')
probeLocalLoss = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 3, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: probeLocalLoss.setStatus('current')
probeGatewayTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 4), )
if mibBuilder.loadTexts: probeGatewayTable.setStatus('current')
probeGatewayEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 4, 1), ).setIndexNames((0, "CISCO-SDWAN-PROBE-MIB", "probeGatewayVpnId"), (0, "CISCO-SDWAN-PROBE-MIB", "probeGatewayAppType"), (0, "CISCO-SDWAN-PROBE-MIB", "probeGatewayAppId"))
if mibBuilder.loadTexts: probeGatewayEntry.setStatus('current')
probeGatewayVpnId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 4, 1, 1), Unsigned32())
if mibBuilder.loadTexts: probeGatewayVpnId.setStatus('current')
probeGatewayAppType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("cxp-app-type-unset", 0), ("cxp-app-type-app-id", 1), ("cxp-app-type-app-grp", 2), ("cxp-app-type-svc-area", 3), ("cxp-app-type-region", 4), ("cxp-app-type-custom-app-grp", 5))))
if mibBuilder.loadTexts: probeGatewayAppType.setStatus('current')
probeGatewayAppId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 4, 1, 3), Unsigned32())
if mibBuilder.loadTexts: probeGatewayAppId.setStatus('current')
probeGatewaySubAppId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 4, 1, 4), Unsigned32())
if mibBuilder.loadTexts: probeGatewaySubAppId.setStatus('current')
probeGatewayGwSysIp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 4, 1, 5), InetAddressIP()).setMaxAccess("readonly")
if mibBuilder.loadTexts: probeGatewayGwSysIp.setStatus('current')
probeGatewayApp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 4, 1, 6), String().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: probeGatewayApp.setStatus('current')
probeGatewayLatency = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 4, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: probeGatewayLatency.setStatus('current')
probeGatewayLoss = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 4, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: probeGatewayLoss.setStatus('current')
probeGatewayRemoteColor = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 4, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22))).clone(namedValues=NamedValues(("default", 1), ("mpls", 2), ("metro-ethernet", 3), ("biz-internet", 4), ("public-internet", 5), ("lte", 6), ("threeG", 7), ("red", 8), ("green", 9), ("blue", 10), ("gold", 11), ("silver", 12), ("bronze", 13), ("custom1", 14), ("custom2", 15), ("custom3", 16), ("private1", 17), ("private2", 18), ("private3", 19), ("private4", 20), ("private5", 21), ("private6", 22)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: probeGatewayRemoteColor.setStatus('current')
probeGatewayLocalColor = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1008, 1, 4, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22))).clone(namedValues=NamedValues(("default", 1), ("mpls", 2), ("metro-ethernet", 3), ("biz-internet", 4), ("public-internet", 5), ("lte", 6), ("threeG", 7), ("red", 8), ("green", 9), ("blue", 10), ("gold", 11), ("silver", 12), ("bronze", 13), ("custom1", 14), ("custom2", 15), ("custom3", 16), ("private1", 17), ("private2", 18), ("private3", 19), ("private4", 20), ("private5", 21), ("private6", 22)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: probeGatewayLocalColor.setStatus('current')
ciscoSdwanProbeMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 1008, 3, 1))
ciscoSdwanProbeMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 1008, 3, 2))
ciscoSdwanProbeMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 1008, 3, 1, 1)).setObjects(("CISCO-SDWAN-PROBE-MIB", "cSdwanProbeApplicationsGroup"), ("CISCO-SDWAN-PROBE-MIB", "cSdwanProbeLocalGroup"), ("CISCO-SDWAN-PROBE-MIB", "cSdwanProbeGatewayGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSdwanProbeMIBCompliance = ciscoSdwanProbeMIBCompliance.setStatus('current')
cSdwanProbeApplicationsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 1008, 3, 2, 1)).setObjects(("CISCO-SDWAN-PROBE-MIB", "probeApplicationsApp"), ("CISCO-SDWAN-PROBE-MIB", "probeApplicationsExitType"), ("CISCO-SDWAN-PROBE-MIB", "probeApplicationsGwSysIp"), ("CISCO-SDWAN-PROBE-MIB", "probeApplicationsInterface"), ("CISCO-SDWAN-PROBE-MIB", "probeApplicationsLatency"), ("CISCO-SDWAN-PROBE-MIB", "probeApplicationsLoss"), ("CISCO-SDWAN-PROBE-MIB", "probeApplicationsLocalColor"), ("CISCO-SDWAN-PROBE-MIB", "probeApplicationsRemoteColor"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSdwanProbeApplicationsGroup = cSdwanProbeApplicationsGroup.setStatus('current')
cSdwanProbeLocalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 1008, 3, 2, 2)).setObjects(("CISCO-SDWAN-PROBE-MIB", "probeLocalApp"), ("CISCO-SDWAN-PROBE-MIB", "probeLocalLatency"), ("CISCO-SDWAN-PROBE-MIB", "probeLocalLoss"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSdwanProbeLocalGroup = cSdwanProbeLocalGroup.setStatus('current')
cSdwanProbeGatewayGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 1008, 3, 2, 3)).setObjects(("CISCO-SDWAN-PROBE-MIB", "probeGatewayApp"), ("CISCO-SDWAN-PROBE-MIB", "probeGatewayLatency"), ("CISCO-SDWAN-PROBE-MIB", "probeGatewayLoss"), ("CISCO-SDWAN-PROBE-MIB", "probeGatewayLocalColor"), ("CISCO-SDWAN-PROBE-MIB", "probeGatewayRemoteColor"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSdwanProbeGatewayGroup = cSdwanProbeGatewayGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-SDWAN-PROBE-MIB", probeGatewayLoss=probeGatewayLoss, probeApplicationsAppType=probeApplicationsAppType, probeGatewayVpnId=probeGatewayVpnId, SourceIp=SourceIp, probeApplicationsSubAppId=probeApplicationsSubAppId, probeApplicationsInterface=probeApplicationsInterface, probeGatewayTable=probeGatewayTable, UnsignedByte=UnsignedByte, probeLocalEntry=probeLocalEntry, probeGatewaySubAppId=probeGatewaySubAppId, probeGatewayAppId=probeGatewayAppId, ColorList=ColorList, NotificationSeverity=NotificationSeverity, probeApplicationsLocalColor=probeApplicationsLocalColor, cSdwanProbeLocalGroup=cSdwanProbeLocalGroup, probeLocalVpnId=probeLocalVpnId, probeApplicationsGwSysIp=probeApplicationsGwSysIp, cSdwanProbeGatewayGroup=cSdwanProbeGatewayGroup, probeGatewayRemoteColor=probeGatewayRemoteColor, DirectionEnum=DirectionEnum, probeLocalApp=probeLocalApp, probeLocalTable=probeLocalTable, VpnId=VpnId, DataPolicyDirectionEnum=DataPolicyDirectionEnum, probeGatewayEntry=probeGatewayEntry, probeApplicationsLoss=probeApplicationsLoss, ActionDataEnum=ActionDataEnum, probeLocalLoss=probeLocalLoss, probeApplicationsEntry=probeApplicationsEntry, ciscoSdwanProbeMIBConform=ciscoSdwanProbeMIBConform, DestinationIp=DestinationIp, probeGatewayLatency=probeGatewayLatency, cSdwanProbeApplicationsGroup=cSdwanProbeApplicationsGroup, UnsignedShort=UnsignedShort, ciscoSdwanProbeMIB=ciscoSdwanProbeMIB, FnfMonitorEnum=FnfMonitorEnum, probeApplicationsLatency=probeApplicationsLatency, probeLocalInterface=probeLocalInterface, ciscoSdwanProbeMIBCompliance=ciscoSdwanProbeMIBCompliance, probeApplicationsExitType=probeApplicationsExitType, ciscoSdwanProbeMIBGroups=ciscoSdwanProbeMIBGroups, probeGatewayApp=probeGatewayApp, probeLocalAppType=probeLocalAppType, TcpFlags=TcpFlags, probeGatewayAppType=probeGatewayAppType, probeApplicationsRemoteColor=probeApplicationsRemoteColor, probeLocalLatency=probeLocalLatency, ConfdString=ConfdString, probeApplicationsAppId=probeApplicationsAppId, probeGatewayGwSysIp=probeGatewayGwSysIp, probeGatewayLocalColor=probeGatewayLocalColor, probeLocalSubAppId=probeLocalSubAppId, InetAddressIP=InetAddressIP, probeApplicationsVpnId=probeApplicationsVpnId, ciscoSdwanProbeMIBObjects=ciscoSdwanProbeMIBObjects, PYSNMP_MODULE_ID=ciscoSdwanProbeMIB, Ipv4Prefix=Ipv4Prefix, probeApplicationsTable=probeApplicationsTable, probeLocalAppId=probeLocalAppId, String=String, probeApplicationsApp=probeApplicationsApp, TransportProtocol=TransportProtocol, ciscoSdwanProbeMIBCompliances=ciscoSdwanProbeMIBCompliances)
