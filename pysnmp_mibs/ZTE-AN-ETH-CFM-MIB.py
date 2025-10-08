#
# PySNMP MIB module ZTE-AN-ETH-CFM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/zte/ZTE-AN-ETH-CFM-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:10:32 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, MacAddress, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "MacAddress", "TruthValue", "DisplayString")
zxAn, = mibBuilder.importSymbols("ZTE-AN-TC-MIB", "zxAn")
zxAnEthCfmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3902, 1015, 60))
zxAnEthCfmMIB.setRevisions(('2007-01-24 00:00',))
if mibBuilder.loadTexts: zxAnEthCfmMIB.setLastUpdated('200701240000Z')
if mibBuilder.loadTexts: zxAnEthCfmMIB.setOrganization('IEEE 802.1 Working Group')
dot1agNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 0))
dot1agMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1))
dot1agCfmMd = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 1))
dot1agCfmMa = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 2))
dot1agCfmMep = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3))
dot1agCfmGloPara = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 4))
class InterfaceIndexOrZero(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class VlanIdOrNone(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 4094), )
class VlanId(TextualConvention, Integer32):
    reference = 'IEEE Std 802.1Q 2003 Edition, Virtual Bridged Local Area Networks.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 4094)

class Dot1agCfmMaintDomainNameType(TextualConvention, Integer32):
    reference = '802.1ag clause 21.6.5, Table 21-19'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("none", 1), ("dnsLikeName", 2), ("macAddressAndUint", 3), ("charString", 4))

class Dot1agCfmMaintDomainName(TextualConvention, OctetString):
    reference = '802.1ag clause 21.6.5'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 80)

class Dot1agCfmMaintAssocNameType(TextualConvention, Integer32):
    reference = '802.1ag clause 21.6.5.4, Table 21-20'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("primaryVid", 1), ("charString", 2), ("unsignedInt16", 3), ("rfc2865VpnId", 4))

class Dot1agCfmMaintAssocName(TextualConvention, OctetString):
    reference = '802.1ag clauses 21.6.5.4, 21.6.5.5, 21.6.5.6'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 80)

class Dot1agCfmMDLevel(TextualConvention, Integer32):
    reference = '802.1ag clauses 18.3, 21.4.1'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 7)

class Dot1agCfmMpDirection(TextualConvention, Integer32):
    reference = '802.1ag clauses 12.14.6.3.2:c'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("down", 1), ("up", 2))

class Dot1agCfmHighestDefectPri(TextualConvention, Integer32):
    reference = '802.1ag clause 20.1.2, 12.14.7.7.2:c and 20.33.9'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("none", 0), ("defRDICCM", 1), ("defMACstatus", 2), ("defRemoteCCM", 3), ("defErrorCCM", 4), ("defXconCCM", 5))

class Dot1agCfmLowestAlarmPri(TextualConvention, Integer32):
    reference = '802.1ag clause 12.14.7.1.3:k and 20.9.5'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("allDef", 1), ("macRemErrXcon", 2), ("remErrXcon", 3), ("errXcon", 4), ("xcon", 5), ("noXcon", 6))

class Dot1agCfmSessionId(TextualConvention, Unsigned32):
    reference = '802.1ag clauses 3.19 and 19.2.1'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 128)

class Dot1agCfmMhfCreation(TextualConvention, Integer32):
    reference = '802.1ag clause 12.14.5.1.3:c and 22.2.3'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("defMHFnone", 1), ("defMHFdefault", 2), ("defMHFexplicit", 3), ("defMHFdefer", 4))

class Dot1agCfmIdPermission(TextualConvention, Integer32):
    reference = '802.1ag clause 12.14.6.1.3:d and 21.5.3'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("sendIdNone", 1), ("sendIdChassis", 2), ("sendIdManage", 3), ("sendIdChassisManage", 4), ("sendIdDefer", 5))

class Dot1agCfmSpeed(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("fastSpeed", 0), ("slowSpeed", 1))

class Dot1agCfmCcmInterval(TextualConvention, Integer32):
    reference = '802.1ag clauses 12.14.6.1.3:e, 20.8.1 and 21.6.1.3'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("intervalInvalid", 0), ("interval300Hz", 1), ("interval10ms", 2), ("interval100ms", 3), ("interval1s", 4), ("interval10s", 5), ("interval1min", 6), ("interval10min", 7))

class Dot1agCfmFngState(TextualConvention, Integer32):
    reference = '802.1ag clause 12.14.7.1.3:f and 20.35'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("fngReset", 1), ("fngDefect", 2), ("fngReportDefect", 3), ("fngDefectReported", 4), ("fngDefectClearing", 5))

class Dot1agCfmRelayActionFieldValue(TextualConvention, Integer32):
    reference = '802.1ag clauses 12.14.7.5.3:g, 20.36.2.5, 21.9.5, and Table 21-27'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("rlyHit", 1), ("rlyFdb", 2), ("rlyMpdb", 3))

class Dot1agCfmIngressActionFieldValue(TextualConvention, Integer32):
    reference = '802.1ag clauses 12.14.7.5.3:g, 20.36.2.6, 21.9.8.1, and Table 21-30 '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("ingOk", 1), ("ingDown", 2), ("ingBlocked", 3), ("ingVid", 4))

class Dot1agCfmEgressActionFieldValue(TextualConvention, Integer32):
    reference = '802.1ag clauses 12.14.7.5.3:o, 20.36.2.10, 21.9.9.1, and Table 21-32'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("egrOK", 1), ("egrDown", 2), ("egrBlocked", 3), ("egrVid", 4))

class Dot1afCfmIndexIntegerNextFree(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class Dot1agCfmMepDefects(TextualConvention, Bits):
    reference = '802.1ag clauses 12.14.7.1.3:o, 12.14.7.1.3:p, 12.14.7.1.3:q, 12.14.7.1.3:r, and 12.14.7.1.3:s.'
    status = 'current'
    namedValues = NamedValues(("bDefRDICCM", 0), ("bDefMACstatus", 1), ("bDefRemoteCCM", 2), ("bDefErrorCCM", 3), ("bDefXconCCM", 4))

class Dot1agCfmLbrTransId(TextualConvention, Unsigned32):
    reference = ' '
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class Dot1agCfmProtectType(TextualConvention, Integer32):
    reference = ''
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("maProtectNothing", 1), ("cfmMaProtectVlan", 2), ("cfmMaProtectTunnel", 3), ("cfmMaProtectPort", 4), ("cfmMaProtectLink", 5))

class Dot1agCfmTunnel(TextualConvention, Unsigned32):
    reference = ' '
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class Dot1agCfmClientLevel(TextualConvention, Unsigned32):
    reference = ' '
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

dot1agCfmMdTableNextIndex = MibScalar((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 1, 1), Dot1afCfmIndexIntegerNextFree()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMdTableNextIndex.setStatus('current')
dot1agCfmMdTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 1, 2), )
if mibBuilder.loadTexts: dot1agCfmMdTable.setStatus('current')
dot1agCfmMdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 1, 2, 1), ).setIndexNames((0, "ZTE-AN-ETH-CFM-MIB", "dot1agCfmMdIndex"))
if mibBuilder.loadTexts: dot1agCfmMdEntry.setStatus('current')
dot1agCfmMdIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 128)))
if mibBuilder.loadTexts: dot1agCfmMdIndex.setStatus('current')
dot1agCfmMdFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 1, 2, 1, 2), Dot1agCfmMaintDomainNameType().clone('charString')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMdFormat.setStatus('current')
dot1agCfmMdName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 1, 2, 1, 3), Dot1agCfmMaintDomainName().clone('DEFAULT')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMdName.setStatus('current')
dot1agCfmMdMdLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 1, 2, 1, 4), Dot1agCfmMDLevel()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMdMdLevel.setStatus('current')
dot1agCfmMdMhfCreation = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 1, 2, 1, 5), Dot1agCfmMhfCreation().clone('defMHFnone')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMdMhfCreation.setStatus('current')
dot1agCfmMdMhfIdPermission = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 1, 2, 1, 6), Dot1agCfmIdPermission().clone('sendIdNone')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMdMhfIdPermission.setStatus('current')
dot1agCfmMdMaTableNextIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 1, 2, 1, 7), Dot1afCfmIndexIntegerNextFree()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMdMaTableNextIndex.setStatus('current')
dot1agCfmMdRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 1, 2, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMdRowStatus.setStatus('current')
dot1agCfmMaTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 2, 1), )
if mibBuilder.loadTexts: dot1agCfmMaTable.setStatus('current')
dot1agCfmMaEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 2, 1, 1), ).setIndexNames((0, "ZTE-AN-ETH-CFM-MIB", "dot1agCfmMdIndex"), (0, "ZTE-AN-ETH-CFM-MIB", "dot1agCfmMaIndex"))
if mibBuilder.loadTexts: dot1agCfmMaEntry.setStatus('current')
dot1agCfmMaIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 2, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 128)))
if mibBuilder.loadTexts: dot1agCfmMaIndex.setStatus('current')
dot1agCfmMaPrimaryVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 2, 1, 1, 2), VlanIdOrNone()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMaPrimaryVlanId.setStatus('current')
dot1agCfmMaFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 2, 1, 1, 3), Dot1agCfmMaintAssocNameType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMaFormat.setStatus('current')
dot1agCfmMaName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 2, 1, 1, 4), Dot1agCfmMaintAssocName()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMaName.setStatus('current')
dot1agCfmMaMhfCreation = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 2, 1, 1, 5), Dot1agCfmMhfCreation().clone('defMHFdefer')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMaMhfCreation.setStatus('current')
dot1agCfmMaIdPermission = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 2, 1, 1, 6), Dot1agCfmIdPermission().clone('sendIdDefer')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMaIdPermission.setStatus('current')
dot1agCfmMaCcmInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 2, 1, 1, 7), Dot1agCfmCcmInterval().clone('interval1s')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMaCcmInterval.setStatus('current')
dot1agCfmMaRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 2, 1, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMaRowStatus.setStatus('current')
dot1agCfmMASpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 2, 1, 1, 9), Dot1agCfmSpeed()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMASpeed.setStatus('current')
dot1agCfmMAProtect = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 2, 1, 1, 10), Dot1agCfmProtectType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMAProtect.setStatus('current')
dot1agCfmMATunnel = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 2, 1, 1, 11), Dot1agCfmTunnel()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMATunnel.setStatus('current')
dot1agCfmMaVlanListTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 2, 2), )
if mibBuilder.loadTexts: dot1agCfmMaVlanListTable.setStatus('current')
dot1agCfmMaVlanListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 2, 2, 1), ).setIndexNames((0, "ZTE-AN-ETH-CFM-MIB", "dot1agCfmMdIndex"), (0, "ZTE-AN-ETH-CFM-MIB", "dot1agCfmMaIndex"), (0, "ZTE-AN-ETH-CFM-MIB", "dot1agCfmMaVlanListIdentifier"))
if mibBuilder.loadTexts: dot1agCfmMaVlanListEntry.setStatus('current')
dot1agCfmMaVlanListIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 2, 2, 1, 1), VlanId())
if mibBuilder.loadTexts: dot1agCfmMaVlanListIdentifier.setStatus('current')
dot1agCfmMaVlanListRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 2, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMaVlanListRowStatus.setStatus('current')
dot1agCfmMaMepListTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 2, 3), )
if mibBuilder.loadTexts: dot1agCfmMaMepListTable.setStatus('current')
dot1agCfmMaMepListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 2, 3, 1), ).setIndexNames((0, "ZTE-AN-ETH-CFM-MIB", "dot1agCfmMdIndex"), (0, "ZTE-AN-ETH-CFM-MIB", "dot1agCfmMaIndex"), (0, "ZTE-AN-ETH-CFM-MIB", "dot1agCfmMaMepListSessionId"))
if mibBuilder.loadTexts: dot1agCfmMaMepListEntry.setStatus('current')
dot1agCfmMaMepListSessionId = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 2, 3, 1, 1), Dot1agCfmSessionId())
if mibBuilder.loadTexts: dot1agCfmMaMepListSessionId.setStatus('current')
dot1agCfmMaMepListRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 2, 3, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMaMepListRowStatus.setStatus('current')
dot1agCfmMepTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1), )
if mibBuilder.loadTexts: dot1agCfmMepTable.setStatus('current')
dot1agCfmMepEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1), ).setIndexNames((0, "ZTE-AN-ETH-CFM-MIB", "dot1agCfmMdIndex"), (0, "ZTE-AN-ETH-CFM-MIB", "dot1agCfmMaIndex"), (0, "ZTE-AN-ETH-CFM-MIB", "dot1agCfmSessionId"))
if mibBuilder.loadTexts: dot1agCfmMepEntry.setStatus('current')
dot1agCfmSessionId = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 1), Dot1agCfmSessionId())
if mibBuilder.loadTexts: dot1agCfmSessionId.setStatus('current')
dot1agCfmMepIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 2), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepIfIndex.setStatus('current')
dot1agCfmMepDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 3), Dot1agCfmMpDirection()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepDirection.setStatus('current')
dot1agCfmMepPrimaryVid = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepPrimaryVid.setStatus('current')
dot1agCfmMepActive = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 5), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepActive.setStatus('current')
dot1agCfmMepFngState = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 6), Dot1agCfmFngState().clone('fngReset')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepFngState.setStatus('current')
dot1agCfmMepCciEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 7), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepCciEnabled.setStatus('current')
dot1agCfmMepCcmLtmPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepCcmLtmPriority.setStatus('current')
dot1agCfmMepMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 9), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepMacAddress.setStatus('current')
dot1agCfmMepLowPrDef = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 10), Dot1agCfmLowestAlarmPri().clone('macRemErrXcon')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepLowPrDef.setStatus('current')
dot1agCfmMepHighestPrDefect = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 11), Dot1agCfmHighestDefectPri()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepHighestPrDefect.setStatus('current')
dot1agCfmMepDefects = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 12), Dot1agCfmMepDefects()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepDefects.setStatus('current')
dot1agCfmMepCciSentCcms = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepCciSentCcms.setStatus('current')
dot1agCfmMepId = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 14), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepId.setStatus('current')
dot1agCfmMepMEPAttachType = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 15), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepMEPAttachType.setStatus('current')
dot1agCfmMepTunnelId = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 16), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepTunnelId.setStatus('current')
dot1agCfmMepLMFlage = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 17), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepLMFlage.setStatus('current')
dot1agCfmMepDMFlage = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 18), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepDMFlage.setStatus('current')
dot1agCfmMepPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 19), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepPortName.setStatus('current')
dot1agCfmMepLbrIn = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepLbrIn.setStatus('current')
dot1agCfmMepLbrInOutOfOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepLbrInOutOfOrder.setStatus('current')
dot1agCfmMepLbrBadMsdu = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepLbrBadMsdu.setStatus('current')
dot1agCfmMepLtmNextSeqNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 23), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepLtmNextSeqNumber.setStatus('current')
dot1agCfmMepUnexpLtrIn = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepUnexpLtrIn.setStatus('current')
dot1agCfmMepLbrOut = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepLbrOut.setStatus('current')
dot1agCfmMepRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 26), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepRowStatus.setStatus('current')
dot1agCfmMepCcCheckFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 27), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepCcCheckFlag.setStatus('current')
dot1agCfmMepComplexFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 28), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepComplexFlag.setStatus('current')
dot1agCfmMepclientLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 29), Dot1agCfmClientLevel()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepclientLevel.setStatus('current')
dot1agCfmMepAISSendFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 30), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepAISSendFlag.setStatus('current')
dot1agCfmMepAISEnableFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 31), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepAISEnableFlag.setStatus('current')
dot1agCfmMepLCKEnableFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 32), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepLCKEnableFlag.setStatus('current')
dot1agCfmMepTxFCf = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 33), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepTxFCf.setStatus('current')
dot1agCfmMepRxFCb = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 34), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepRxFCb.setStatus('current')
dot1agCfmMepTxFCb = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 35), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepTxFCb.setStatus('current')
dot1agCfmMepRxFCl = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 36), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepRxFCl.setStatus('current')
dot1agCfmMepNearLost = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 37), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepNearLost.setStatus('current')
dot1agCfmMepFarLost = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 38), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepFarLost.setStatus('current')
dot1agCfmMepDaly = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 39), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepDaly.setStatus('current')
dot1agCfmMepDalyAve = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 40), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepDalyAve.setStatus('current')
dot1agCfmMepDalyChg = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 41), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepDalyChg.setStatus('current')
dot1agCfmMepDalyChgAve = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 42), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepDalyChgAve.setStatus('current')
dot1agCfmMepTransmitLbmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 43), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepTransmitLbmStatus.setStatus('current')
dot1agCfmMepTransmitLbmDestMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 44), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepTransmitLbmDestMacAddress.setStatus('current')
dot1agCfmMepTransmitLbmDestSessionId = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 45), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepTransmitLbmDestSessionId.setStatus('current')
dot1agCfmMepTransmitLbmDestIsSessionId = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 46), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepTransmitLbmDestIsSessionId.setStatus('current')
dot1agCfmMepTransmitLbmDestMepId = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 47), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepTransmitLbmDestMepId.setStatus('current')
dot1agCfmMepTransmitLbmDestIsMepId = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 48), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepTransmitLbmDestIsMepId.setStatus('current')
dot1agCfmMepTransmitLbmMessages = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 49), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepTransmitLbmMessages.setStatus('current')
dot1agCfmMepTransmitLbmDataTlv = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 50), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1500))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepTransmitLbmDataTlv.setStatus('current')
dot1agCfmMepTransmitLbmVlanPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 51), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepTransmitLbmVlanPriority.setStatus('current')
dot1agCfmMepTransmitLbmVlanDropEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 52), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepTransmitLbmVlanDropEnable.setStatus('current')
dot1agCfmMepTransmitLbmResultOK = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 53), TruthValue().clone('true')).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepTransmitLbmResultOK.setStatus('current')
dot1agCfmMepTransmitLbmSeqNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 54), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepTransmitLbmSeqNumber.setStatus('current')
dot1agCfmMepTransmitLtmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 55), TruthValue().clone('true')).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepTransmitLtmStatus.setStatus('current')
dot1agCfmMepTransmitLtmFlags = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 56), Bits().clone(namedValues=NamedValues(("useFDBonly", 0)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepTransmitLtmFlags.setStatus('current')
dot1agCfmMepTransmitLtmTargetMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 57), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepTransmitLtmTargetMacAddress.setStatus('current')
dot1agCfmMepTransmitLtmTargetSessionId = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 58), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepTransmitLtmTargetSessionId.setStatus('current')
dot1agCfmMepTransmitLtmTargetIsSessionId = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 59), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepTransmitLtmTargetIsSessionId.setStatus('current')
dot1agCfmMepTransmitLtmTargetMepId = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 60), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepTransmitLtmTargetMepId.setStatus('current')
dot1agCfmMepTransmitLtmTargetIsMepId = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 61), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepTransmitLtmTargetIsMepId.setStatus('current')
dot1agCfmMepTransmitLtmTtl = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 62), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(64)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepTransmitLtmTtl.setStatus('current')
dot1agCfmMepTransmitLtmResult = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 63), TruthValue().clone('true')).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepTransmitLtmResult.setStatus('current')
dot1agCfmMepTransmitLtmSeqNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 64), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmMepTransmitLtmSeqNumber.setStatus('current')
dot1agCfmMepTransmitLtmEgressIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 1, 1, 65), OctetString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepTransmitLtmEgressIdentifier.setStatus('current')
dot1agCfmLtrTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 2), )
if mibBuilder.loadTexts: dot1agCfmLtrTable.setStatus('current')
dot1agCfmLtrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 2, 1), ).setIndexNames((0, "ZTE-AN-ETH-CFM-MIB", "dot1agCfmMdIndex"), (0, "ZTE-AN-ETH-CFM-MIB", "dot1agCfmMaIndex"), (0, "ZTE-AN-ETH-CFM-MIB", "dot1agCfmSessionId"), (0, "ZTE-AN-ETH-CFM-MIB", "dot1agCfmLtrSeqNumber"), (0, "ZTE-AN-ETH-CFM-MIB", "dot1agCfmLtrReceiveOrder"))
if mibBuilder.loadTexts: dot1agCfmLtrEntry.setStatus('current')
dot1agCfmLtrSeqNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)))
if mibBuilder.loadTexts: dot1agCfmLtrSeqNumber.setStatus('current')
dot1agCfmLtrReceiveOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: dot1agCfmLtrReceiveOrder.setStatus('current')
dot1agCfmLtrTtl = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmLtrTtl.setStatus('current')
dot1agCfmLtrForwarded = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 2, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmLtrForwarded.setStatus('current')
dot1agCfmLtrTerminalMep = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 2, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmLtrTerminalMep.setStatus('current')
dot1agCfmLtrLastEgressIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 2, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmLtrLastEgressIdentifier.setStatus('current')
dot1agCfmLtrNextEgressIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 2, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmLtrNextEgressIdentifier.setStatus('current')
dot1agCfmLtrRelay = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 2, 1, 8), Dot1agCfmRelayActionFieldValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmLtrRelay.setStatus('current')
dot1agCfmLtrIngress = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 2, 1, 9), Dot1agCfmIngressActionFieldValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmLtrIngress.setStatus('current')
dot1agCfmLtrIngressMac = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 2, 1, 10), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmLtrIngressMac.setStatus('current')
dot1agCfmLtrEgress = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 2, 1, 11), Dot1agCfmEgressActionFieldValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmLtrEgress.setStatus('current')
dot1agCfmLtrEgressMac = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 2, 1, 12), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmLtrEgressMac.setStatus('current')
dot1agCfmMepDbTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 3), )
if mibBuilder.loadTexts: dot1agCfmMepDbTable.setStatus('current')
dot1agCfmMepDbEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 3, 1), ).setIndexNames((0, "ZTE-AN-ETH-CFM-MIB", "dot1agCfmMdIndex"), (0, "ZTE-AN-ETH-CFM-MIB", "dot1agCfmMaIndex"), (0, "ZTE-AN-ETH-CFM-MIB", "dot1agCfmMepDbRSessionId"))
if mibBuilder.loadTexts: dot1agCfmMepDbEntry.setStatus('current')
dot1agCfmMepDbRSessionId = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 3, 1, 1), Dot1agCfmSessionId())
if mibBuilder.loadTexts: dot1agCfmMepDbRSessionId.setStatus('current')
dot1agCfmMepDbMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 3, 1, 2), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepDbMacAddress.setStatus('current')
dot1agCfmMepDbRdi = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 3, 1, 3), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepDbRdi.setStatus('current')
dot1agCfmMepDbId = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 3, 1, 4), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepDbId.setStatus('current')
dot1agCfmMepDbRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 3, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1agCfmMepDbRowStatus.setStatus('current')
dot1agCfmLbrInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 4))
dot1agCfmLbrTransId = MibScalar((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 4, 1), Dot1agCfmLbrTransId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmLbrTransId.setStatus('current')
dot1agCfmLbrPrintInfo = MibScalar((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 4, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1agCfmLbrPrintInfo.setStatus('current')
dot1agCfmMipTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 5), )
if mibBuilder.loadTexts: dot1agCfmMipTable.setStatus('current')
dot1agCfmMipEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 5, 1), ).setIndexNames((0, "ZTE-AN-ETH-CFM-MIB", "dot1agCfmMdIndex"), (0, "ZTE-AN-ETH-CFM-MIB", "dot1agCfmMaIndex"), (0, "ZTE-AN-ETH-CFM-MIB", "dot1agCfmMipSessionId"))
if mibBuilder.loadTexts: dot1agCfmMipEntry.setStatus('current')
dot1agCfmMipSessionId = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 5, 1, 1), Unsigned32())
if mibBuilder.loadTexts: dot1agCfmMipSessionId.setStatus('current')
dot1agCfmMipName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 5, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1agCfmMipName.setStatus('current')
dot1agCfmMipPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 3, 5, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1agCfmMipPortName.setStatus('current')
dot1agCfmGlobalIsEnable = MibScalar((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 1, 4, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1agCfmGlobalIsEnable.setStatus('current')
dot1agCfmFaultAlarm = NotificationType((1, 3, 6, 1, 4, 1, 3902, 1015, 60, 0, 1)).setObjects(("ZTE-AN-ETH-CFM-MIB", "dot1agCfmMepHighestPrDefect"))
if mibBuilder.loadTexts: dot1agCfmFaultAlarm.setStatus('current')
mibBuilder.exportSymbols("ZTE-AN-ETH-CFM-MIB", dot1agCfmMepPrimaryVid=dot1agCfmMepPrimaryVid, dot1agCfmMepTransmitLbmDestIsMepId=dot1agCfmMepTransmitLbmDestIsMepId, dot1agCfmMaIndex=dot1agCfmMaIndex, dot1agCfmMepDefects=dot1agCfmMepDefects, dot1agCfmMepDbTable=dot1agCfmMepDbTable, dot1agCfmMepTransmitLtmEgressIdentifier=dot1agCfmMepTransmitLtmEgressIdentifier, dot1agCfmMdMhfCreation=dot1agCfmMdMhfCreation, dot1agCfmMepHighestPrDefect=dot1agCfmMepHighestPrDefect, dot1agCfmMASpeed=dot1agCfmMASpeed, dot1agCfmLtrForwarded=dot1agCfmLtrForwarded, dot1agCfmSessionId=dot1agCfmSessionId, dot1agCfmLtrRelay=dot1agCfmLtrRelay, dot1agCfmMep=dot1agCfmMep, Dot1agCfmMDLevel=Dot1agCfmMDLevel, dot1agCfmMepDbRowStatus=dot1agCfmMepDbRowStatus, dot1agCfmMipPortName=dot1agCfmMipPortName, Dot1agCfmLowestAlarmPri=Dot1agCfmLowestAlarmPri, dot1agCfmLbrInfo=dot1agCfmLbrInfo, dot1agCfmMaMepListRowStatus=dot1agCfmMaMepListRowStatus, Dot1agCfmIngressActionFieldValue=Dot1agCfmIngressActionFieldValue, dot1agCfmLtrNextEgressIdentifier=dot1agCfmLtrNextEgressIdentifier, dot1agCfmMepIfIndex=dot1agCfmMepIfIndex, dot1agCfmMepTransmitLbmDestMepId=dot1agCfmMepTransmitLbmDestMepId, dot1agCfmMepTransmitLbmResultOK=dot1agCfmMepTransmitLbmResultOK, Dot1agCfmEgressActionFieldValue=Dot1agCfmEgressActionFieldValue, dot1agCfmMepCcmLtmPriority=dot1agCfmMepCcmLtmPriority, dot1agCfmMipSessionId=dot1agCfmMipSessionId, Dot1agCfmMaintAssocName=Dot1agCfmMaintAssocName, dot1agCfmMepLMFlage=dot1agCfmMepLMFlage, dot1agCfmGlobalIsEnable=dot1agCfmGlobalIsEnable, dot1agCfmMepRxFCl=dot1agCfmMepRxFCl, dot1agCfmMdName=dot1agCfmMdName, dot1agCfmMepTunnelId=dot1agCfmMepTunnelId, Dot1agCfmTunnel=Dot1agCfmTunnel, dot1agCfmLtrIngress=dot1agCfmLtrIngress, dot1agCfmMepUnexpLtrIn=dot1agCfmMepUnexpLtrIn, dot1agCfmMepMEPAttachType=dot1agCfmMepMEPAttachType, Dot1agCfmMhfCreation=Dot1agCfmMhfCreation, Dot1agCfmMaintDomainNameType=Dot1agCfmMaintDomainNameType, dot1agCfmMepFarLost=dot1agCfmMepFarLost, dot1agCfmMepDbEntry=dot1agCfmMepDbEntry, dot1agCfmMepEntry=dot1agCfmMepEntry, dot1agCfmMepTransmitLtmTargetMepId=dot1agCfmMepTransmitLtmTargetMepId, Dot1agCfmIdPermission=Dot1agCfmIdPermission, dot1agCfmLbrPrintInfo=dot1agCfmLbrPrintInfo, Dot1agCfmMaintAssocNameType=Dot1agCfmMaintAssocNameType, Dot1agCfmSpeed=Dot1agCfmSpeed, VlanId=VlanId, dot1agCfmMaMepListTable=dot1agCfmMaMepListTable, dot1agCfmLtrIngressMac=dot1agCfmLtrIngressMac, dot1agCfmMaMepListEntry=dot1agCfmMaMepListEntry, dot1agCfmLbrTransId=dot1agCfmLbrTransId, dot1agCfmMd=dot1agCfmMd, dot1agCfmMepTransmitLtmTargetMacAddress=dot1agCfmMepTransmitLtmTargetMacAddress, dot1agCfmMepDbRdi=dot1agCfmMepDbRdi, Dot1agCfmFngState=Dot1agCfmFngState, dot1agCfmMepTransmitLbmDestIsSessionId=dot1agCfmMepTransmitLbmDestIsSessionId, dot1agCfmLtrTtl=dot1agCfmLtrTtl, dot1agMIBObjects=dot1agMIBObjects, dot1agCfmMepDalyChgAve=dot1agCfmMepDalyChgAve, dot1agCfmMdMdLevel=dot1agCfmMdMdLevel, dot1agCfmMepCciEnabled=dot1agCfmMepCciEnabled, dot1agCfmMaEntry=dot1agCfmMaEntry, Dot1agCfmMaintDomainName=Dot1agCfmMaintDomainName, dot1agCfmMepTransmitLbmStatus=dot1agCfmMepTransmitLbmStatus, dot1agCfmMaTable=dot1agCfmMaTable, dot1agCfmMepTransmitLtmResult=dot1agCfmMepTransmitLtmResult, Dot1afCfmIndexIntegerNextFree=Dot1afCfmIndexIntegerNextFree, dot1agCfmMepTransmitLbmDataTlv=dot1agCfmMepTransmitLbmDataTlv, dot1agCfmLtrEntry=dot1agCfmLtrEntry, dot1agCfmMepActive=dot1agCfmMepActive, dot1agCfmMepDbId=dot1agCfmMepDbId, Dot1agCfmMpDirection=Dot1agCfmMpDirection, Dot1agCfmCcmInterval=Dot1agCfmCcmInterval, Dot1agCfmMepDefects=Dot1agCfmMepDefects, dot1agCfmMdMaTableNextIndex=dot1agCfmMdMaTableNextIndex, dot1agCfmMepAISSendFlag=dot1agCfmMepAISSendFlag, dot1agCfmMepPortName=dot1agCfmMepPortName, dot1agCfmMepTxFCf=dot1agCfmMepTxFCf, dot1agCfmLtrEgressMac=dot1agCfmLtrEgressMac, dot1agCfmMepDMFlage=dot1agCfmMepDMFlage, dot1agCfmMaVlanListIdentifier=dot1agCfmMaVlanListIdentifier, dot1agCfmMdEntry=dot1agCfmMdEntry, dot1agCfmMepDalyAve=dot1agCfmMepDalyAve, dot1agCfmMepTransmitLbmDestSessionId=dot1agCfmMepTransmitLbmDestSessionId, dot1agCfmFaultAlarm=dot1agCfmFaultAlarm, dot1agCfmGloPara=dot1agCfmGloPara, dot1agCfmMaIdPermission=dot1agCfmMaIdPermission, dot1agCfmMepTransmitLtmTargetSessionId=dot1agCfmMepTransmitLtmTargetSessionId, dot1agCfmLtrReceiveOrder=dot1agCfmLtrReceiveOrder, dot1agCfmMepTxFCb=dot1agCfmMepTxFCb, dot1agCfmMepTransmitLbmVlanPriority=dot1agCfmMepTransmitLbmVlanPriority, Dot1agCfmClientLevel=Dot1agCfmClientLevel, dot1agCfmMaPrimaryVlanId=dot1agCfmMaPrimaryVlanId, dot1agCfmMepLtmNextSeqNumber=dot1agCfmMepLtmNextSeqNumber, dot1agCfmMepclientLevel=dot1agCfmMepclientLevel, dot1agCfmMipEntry=dot1agCfmMipEntry, dot1agCfmMdTable=dot1agCfmMdTable, zxAnEthCfmMIB=zxAnEthCfmMIB, dot1agCfmMepDbMacAddress=dot1agCfmMepDbMacAddress, dot1agCfmMepDaly=dot1agCfmMepDaly, dot1agCfmMepDbRSessionId=dot1agCfmMepDbRSessionId, Dot1agCfmLbrTransId=Dot1agCfmLbrTransId, dot1agCfmMepTransmitLbmVlanDropEnable=dot1agCfmMepTransmitLbmVlanDropEnable, dot1agCfmMepTransmitLtmStatus=dot1agCfmMepTransmitLtmStatus, PYSNMP_MODULE_ID=zxAnEthCfmMIB, dot1agCfmLtrTerminalMep=dot1agCfmLtrTerminalMep, dot1agCfmMaVlanListTable=dot1agCfmMaVlanListTable, dot1agCfmLtrEgress=dot1agCfmLtrEgress, dot1agCfmMipName=dot1agCfmMipName, Dot1agCfmRelayActionFieldValue=Dot1agCfmRelayActionFieldValue, dot1agCfmMATunnel=dot1agCfmMATunnel, dot1agCfmMepFngState=dot1agCfmMepFngState, dot1agCfmMa=dot1agCfmMa, dot1agCfmMaMepListSessionId=dot1agCfmMaMepListSessionId, dot1agCfmMaCcmInterval=dot1agCfmMaCcmInterval, dot1agCfmMaVlanListEntry=dot1agCfmMaVlanListEntry, dot1agCfmMaName=dot1agCfmMaName, dot1agCfmMepLbrInOutOfOrder=dot1agCfmMepLbrInOutOfOrder, dot1agCfmMepLbrOut=dot1agCfmMepLbrOut, dot1agCfmMepId=dot1agCfmMepId, dot1agCfmMdTableNextIndex=dot1agCfmMdTableNextIndex, dot1agCfmMepComplexFlag=dot1agCfmMepComplexFlag, dot1agCfmMepRowStatus=dot1agCfmMepRowStatus, dot1agCfmMepCcCheckFlag=dot1agCfmMepCcCheckFlag, dot1agCfmMipTable=dot1agCfmMipTable, dot1agCfmMepTransmitLtmTargetIsSessionId=dot1agCfmMepTransmitLtmTargetIsSessionId, dot1agCfmLtrLastEgressIdentifier=dot1agCfmLtrLastEgressIdentifier, dot1agNotifications=dot1agNotifications, dot1agCfmMepTransmitLbmSeqNumber=dot1agCfmMepTransmitLbmSeqNumber, dot1agCfmMepMacAddress=dot1agCfmMepMacAddress, dot1agCfmMepTransmitLtmTargetIsMepId=dot1agCfmMepTransmitLtmTargetIsMepId, dot1agCfmMaRowStatus=dot1agCfmMaRowStatus, dot1agCfmMepNearLost=dot1agCfmMepNearLost, dot1agCfmMepTransmitLtmSeqNumber=dot1agCfmMepTransmitLtmSeqNumber, dot1agCfmMdFormat=dot1agCfmMdFormat, dot1agCfmMepRxFCb=dot1agCfmMepRxFCb, dot1agCfmMepLowPrDef=dot1agCfmMepLowPrDef, VlanIdOrNone=VlanIdOrNone, Dot1agCfmProtectType=Dot1agCfmProtectType, Dot1agCfmSessionId=Dot1agCfmSessionId, dot1agCfmMdRowStatus=dot1agCfmMdRowStatus, dot1agCfmMaMhfCreation=dot1agCfmMaMhfCreation, dot1agCfmMepTransmitLtmFlags=dot1agCfmMepTransmitLtmFlags, dot1agCfmMAProtect=dot1agCfmMAProtect, dot1agCfmMepDalyChg=dot1agCfmMepDalyChg, dot1agCfmMepLbrBadMsdu=dot1agCfmMepLbrBadMsdu, dot1agCfmMepTransmitLbmDestMacAddress=dot1agCfmMepTransmitLbmDestMacAddress, dot1agCfmMaFormat=dot1agCfmMaFormat, dot1agCfmMepCciSentCcms=dot1agCfmMepCciSentCcms, dot1agCfmLtrSeqNumber=dot1agCfmLtrSeqNumber, dot1agCfmLtrTable=dot1agCfmLtrTable, dot1agCfmMepTransmitLtmTtl=dot1agCfmMepTransmitLtmTtl, dot1agCfmMdIndex=dot1agCfmMdIndex, dot1agCfmMepAISEnableFlag=dot1agCfmMepAISEnableFlag, dot1agCfmMepLbrIn=dot1agCfmMepLbrIn, dot1agCfmMaVlanListRowStatus=dot1agCfmMaVlanListRowStatus, InterfaceIndexOrZero=InterfaceIndexOrZero, dot1agCfmMepDirection=dot1agCfmMepDirection, dot1agCfmMepLCKEnableFlag=dot1agCfmMepLCKEnableFlag, dot1agCfmMepTable=dot1agCfmMepTable, Dot1agCfmHighestDefectPri=Dot1agCfmHighestDefectPri, dot1agCfmMepTransmitLbmMessages=dot1agCfmMepTransmitLbmMessages, dot1agCfmMdMhfIdPermission=dot1agCfmMdMhfIdPermission)
