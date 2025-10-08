#
# PySNMP MIB module CISCO-SDWAN-PROBE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-SDWAN-PROBE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:23:40 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, TextualConvention = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt", "TextualConvention")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, Counter64, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "Counter64", "TimeTicks", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("CISCO-SDWAN-PROBE-MIB", UnsignedByte=UnsignedByte, DestinationIp=DestinationIp, probeGatewaySubAppId=probeGatewaySubAppId, probeGatewayLocalColor=probeGatewayLocalColor, probeApplicationsLatency=probeApplicationsLatency, probeApplicationsApp=probeApplicationsApp, Ipv4Prefix=Ipv4Prefix, probeApplicationsExitType=probeApplicationsExitType, probeApplicationsAppType=probeApplicationsAppType, probeApplicationsGwSysIp=probeApplicationsGwSysIp, probeLocalSubAppId=probeLocalSubAppId, cSdwanProbeApplicationsGroup=cSdwanProbeApplicationsGroup, probeApplicationsEntry=probeApplicationsEntry, String=String, probeLocalTable=probeLocalTable, probeGatewayAppId=probeGatewayAppId, VpnId=VpnId, probeLocalVpnId=probeLocalVpnId, probeGatewayLoss=probeGatewayLoss, DirectionEnum=DirectionEnum, InetAddressIP=InetAddressIP, probeApplicationsVpnId=probeApplicationsVpnId, probeGatewayGwSysIp=probeGatewayGwSysIp, ConfdString=ConfdString, probeApplicationsTable=probeApplicationsTable, probeGatewayVpnId=probeGatewayVpnId, probeApplicationsLoss=probeApplicationsLoss, probeGatewayApp=probeGatewayApp, probeGatewayEntry=probeGatewayEntry, cSdwanProbeGatewayGroup=cSdwanProbeGatewayGroup, ActionDataEnum=ActionDataEnum, probeLocalEntry=probeLocalEntry, probeLocalAppType=probeLocalAppType, ciscoSdwanProbeMIBCompliance=ciscoSdwanProbeMIBCompliance, ciscoSdwanProbeMIBConform=ciscoSdwanProbeMIBConform, TcpFlags=TcpFlags, probeLocalInterface=probeLocalInterface, probeLocalLoss=probeLocalLoss, ColorList=ColorList, probeApplicationsSubAppId=probeApplicationsSubAppId, probeApplicationsInterface=probeApplicationsInterface, DataPolicyDirectionEnum=DataPolicyDirectionEnum, PYSNMP_MODULE_ID=ciscoSdwanProbeMIB, probeApplicationsAppId=probeApplicationsAppId, ciscoSdwanProbeMIBCompliances=ciscoSdwanProbeMIBCompliances, probeGatewayLatency=probeGatewayLatency, probeLocalApp=probeLocalApp, probeLocalLatency=probeLocalLatency, FnfMonitorEnum=FnfMonitorEnum, probeGatewayAppType=probeGatewayAppType, NotificationSeverity=NotificationSeverity, cSdwanProbeLocalGroup=cSdwanProbeLocalGroup, ciscoSdwanProbeMIBObjects=ciscoSdwanProbeMIBObjects, ciscoSdwanProbeMIBGroups=ciscoSdwanProbeMIBGroups, UnsignedShort=UnsignedShort, ciscoSdwanProbeMIB=ciscoSdwanProbeMIB, probeApplicationsLocalColor=probeApplicationsLocalColor, probeLocalAppId=probeLocalAppId, probeGatewayRemoteColor=probeGatewayRemoteColor, probeGatewayTable=probeGatewayTable, TransportProtocol=TransportProtocol, SourceIp=SourceIp, probeApplicationsRemoteColor=probeApplicationsRemoteColor)
