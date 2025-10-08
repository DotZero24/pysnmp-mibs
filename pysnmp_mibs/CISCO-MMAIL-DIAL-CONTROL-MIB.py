#
# PySNMP MIB module CISCO-MMAIL-DIAL-CONTROL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-MMAIL-DIAL-CONTROL-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:28:45 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
cCallHistoryIndex, = mibBuilder.importSymbols("CISCO-DIAL-CONTROL-MIB", "cCallHistoryIndex")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
CvcGUid, = mibBuilder.importSymbols("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "CvcGUid")
callActiveSetupTime, AbsoluteCounter32, callActiveIndex = mibBuilder.importSymbols("DIAL-CONTROL-MIB", "callActiveSetupTime", "AbsoluteCounter32", "callActiveIndex")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
ciscoMediaMailDialControlMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 102))
ciscoMediaMailDialControlMIB.setRevisions(('2002-02-25 00:00',))
if mibBuilder.loadTexts: ciscoMediaMailDialControlMIB.setLastUpdated('200202250000Z')
if mibBuilder.loadTexts: ciscoMediaMailDialControlMIB.setOrganization('Cisco Systems, Inc.')
class CmmImgResolution(TextualConvention, Integer32):
    reference = 'RFC2301: Section 4.5.2 Encoding and Resolution.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(2, 3, 4))
    namedValues = NamedValues(("standard", 2), ("fine", 3), ("superFine", 4))

class CmmImgResolutionOrTransparent(TextualConvention, Integer32):
    reference = 'RFC2301: Section 4.5.2 Encoding and Resolution.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("transparent", 1), ("standard", 2), ("fine", 3), ("superFine", 4))

class CmmImgEncoding(TextualConvention, Integer32):
    reference = 'RFC2301: Section 1.3 Overview of this draft. ITU-T Rec. T.4 (MH - Modified Huffman). ITU-T Rec. T.4 (MR - Modified READ). ITU-T Rec. T.6 (MRR - Modified MR). '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(2, 3, 4))
    namedValues = NamedValues(("modifiedHuffman", 2), ("modifiedREAD", 3), ("modifiedMR", 4))

class CmmImgEncodingOrTransparent(TextualConvention, Integer32):
    reference = 'RFC2301: Section 1.3 Overview of this draft. ITU-T Rec. T.4 (MH - Modified Huffman). ITU-T Rec. T.4 (MR - Modified READ). ITU-T Rec. T.6 (MRR - Modified MR). '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("transparent", 1), ("modifiedHuffman", 2), ("modifiedREAD", 3), ("modifiedMR", 4))

class CmmFaxHeadingString(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 80)

cmmdcMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 102, 1))
cmmPeer = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 1))
cmmCallActive = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 2))
cmmCallHistory = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 3))
cmmFaxGeneralCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 4))
cmmIpPeerCfgTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 1, 1), )
if mibBuilder.loadTexts: cmmIpPeerCfgTable.setStatus('current')
cmmIpPeerCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cmmIpPeerCfgEntry.setStatus('current')
cmmIpPeerCfgSessionProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("smtp", 1))).clone('smtp')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmmIpPeerCfgSessionProtocol.setStatus('current')
cmmIpPeerCfgSessionTarget = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 1, 1, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmmIpPeerCfgSessionTarget.setStatus('current')
cmmIpPeerCfgImgEncodingType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 1, 1, 1, 3), CmmImgEncodingOrTransparent().clone('transparent')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmmIpPeerCfgImgEncodingType.setStatus('current')
cmmIpPeerCfgImgResolution = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 1, 1, 1, 4), CmmImgResolutionOrTransparent().clone('transparent')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmmIpPeerCfgImgResolution.setStatus('current')
cmmIpPeerCfgMsgDispoNotification = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 1, 1, 1, 5), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmmIpPeerCfgMsgDispoNotification.setStatus('current')
cmmIpPeerCfgDeliStatNotification = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 1, 1, 1, 6), Bits().clone(namedValues=NamedValues(("success", 0), ("failure", 1), ("delayed", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmmIpPeerCfgDeliStatNotification.setStatus('current')
cmmIpCallActiveTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 2, 1), )
if mibBuilder.loadTexts: cmmIpCallActiveTable.setStatus('current')
cmmIpCallActiveEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 2, 1, 1), ).setIndexNames((0, "DIAL-CONTROL-MIB", "callActiveSetupTime"), (0, "DIAL-CONTROL-MIB", "callActiveIndex"))
if mibBuilder.loadTexts: cmmIpCallActiveEntry.setStatus('current')
cmmIpCallActiveConnectionId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 2, 1, 1, 1), CvcGUid()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmmIpCallActiveConnectionId.setStatus('current')
cmmIpCallActiveRemoteIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 2, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmmIpCallActiveRemoteIPAddress.setStatus('current')
cmmIpCallActiveSessionProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("smtp", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmmIpCallActiveSessionProtocol.setStatus('current')
cmmIpCallActiveSessionTarget = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 2, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmmIpCallActiveSessionTarget.setStatus('current')
cmmIpCallActiveMessageId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 2, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmmIpCallActiveMessageId.setStatus('current')
cmmIpCallActiveAccountId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 2, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmmIpCallActiveAccountId.setStatus('current')
cmmIpCallActiveImgEncodingType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 2, 1, 1, 7), CmmImgEncoding()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmmIpCallActiveImgEncodingType.setStatus('current')
cmmIpCallActiveImgResolution = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 2, 1, 1, 8), CmmImgResolution()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmmIpCallActiveImgResolution.setStatus('current')
cmmIpCallActiveAcceptMimeTypes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 2, 1, 1, 9), AbsoluteCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmmIpCallActiveAcceptMimeTypes.setStatus('current')
cmmIpCallActiveDiscdMimeTypes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 2, 1, 1, 10), AbsoluteCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmmIpCallActiveDiscdMimeTypes.setStatus('current')
cmmIpCallActiveNotification = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 2, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("mdn", 2), ("dsn", 3), ("dsnMdn", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmmIpCallActiveNotification.setStatus('current')
cmmIpCallHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 3, 1), )
if mibBuilder.loadTexts: cmmIpCallHistoryTable.setStatus('current')
cmmIpCallHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 3, 1, 1), ).setIndexNames((0, "CISCO-DIAL-CONTROL-MIB", "cCallHistoryIndex"))
if mibBuilder.loadTexts: cmmIpCallHistoryEntry.setStatus('current')
cmmIpCallHistoryConnectionId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 3, 1, 1, 1), CvcGUid()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmmIpCallHistoryConnectionId.setStatus('current')
cmmIpCallHistoryRemoteIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 3, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmmIpCallHistoryRemoteIPAddress.setStatus('current')
cmmIpCallHistorySessionProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("smtp", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmmIpCallHistorySessionProtocol.setStatus('current')
cmmIpCallHistorySessionTarget = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 3, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmmIpCallHistorySessionTarget.setStatus('current')
cmmIpCallHistoryMessageId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 3, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmmIpCallHistoryMessageId.setStatus('current')
cmmIpCallHistoryAccountId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 3, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmmIpCallHistoryAccountId.setStatus('current')
cmmIpCallHistoryImgEncodingType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 3, 1, 1, 7), CmmImgEncoding()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmmIpCallHistoryImgEncodingType.setStatus('current')
cmmIpCallHistoryImgResolution = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 3, 1, 1, 8), CmmImgResolution()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmmIpCallHistoryImgResolution.setStatus('current')
cmmIpCallHistoryAcceptMimeTypes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 3, 1, 1, 9), AbsoluteCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmmIpCallHistoryAcceptMimeTypes.setStatus('current')
cmmIpCallHistoryDiscdMimeTypes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 3, 1, 1, 10), AbsoluteCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmmIpCallHistoryDiscdMimeTypes.setStatus('current')
cmmIpCallHistoryNotification = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 3, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("mdn", 2), ("dsn", 3), ("dsnMdn", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmmIpCallHistoryNotification.setStatus('current')
cmmFaxCfgCalledSubscriberId = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 4, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmmFaxCfgCalledSubscriberId.setStatus('current')
cmmFaxCfgXmitSubscriberId = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 4, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmmFaxCfgXmitSubscriberId.setStatus('current')
cmmFaxCfgRightHeadingString = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 4, 3), CmmFaxHeadingString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmmFaxCfgRightHeadingString.setStatus('current')
cmmFaxCfgCenterHeadingString = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 4, 4), CmmFaxHeadingString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmmFaxCfgCenterHeadingString.setStatus('current')
cmmFaxCfgLeftHeadingString = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 4, 5), CmmFaxHeadingString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmmFaxCfgLeftHeadingString.setStatus('current')
cmmFaxCfgCovergPageControl = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 4, 6), Bits().clone(namedValues=NamedValues(("coverPageEnable", 0), ("coverPageCtlByEmail", 1), ("coverPageDetailEnable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmmFaxCfgCovergPageControl.setStatus('current')
cmmFaxCfgCovergPageComment = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 4, 7), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmmFaxCfgCovergPageComment.setStatus('current')
cmmFaxCfgFaxProfile = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 102, 1, 4, 8), Bits().clone(namedValues=NamedValues(("profileS", 0), ("profileF", 1), ("profileJ", 2), ("profileC", 3), ("profileL", 4), ("profileM", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmmFaxCfgFaxProfile.setStatus('current')
cmmdcMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 102, 3))
cmmdcMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 102, 3, 1))
cmmdcMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 102, 3, 2))
cmmdcMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 102, 3, 1, 1)).setObjects(("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmdcPeerCfgGroup"), ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmIpCallGeneralGroup"), ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmIpCallImageGroup"), ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmFaxGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmmdcMIBCompliance = cmmdcMIBCompliance.setStatus('current')
cmmdcPeerCfgGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 102, 3, 2, 1)).setObjects(("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmIpPeerCfgSessionProtocol"), ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmIpPeerCfgSessionTarget"), ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmIpPeerCfgImgEncodingType"), ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmIpPeerCfgImgResolution"), ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmIpPeerCfgMsgDispoNotification"), ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmIpPeerCfgDeliStatNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmmdcPeerCfgGroup = cmmdcPeerCfgGroup.setStatus('current')
cmmIpCallGeneralGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 102, 3, 2, 2)).setObjects(("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmIpCallActiveConnectionId"), ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmIpCallActiveRemoteIPAddress"), ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmIpCallActiveSessionProtocol"), ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmIpCallActiveSessionTarget"), ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmIpCallActiveMessageId"), ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmIpCallActiveAccountId"), ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmIpCallActiveAcceptMimeTypes"), ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmIpCallActiveDiscdMimeTypes"), ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmIpCallActiveNotification"), ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmIpCallHistoryConnectionId"), ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmIpCallHistoryRemoteIPAddress"), ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmIpCallHistorySessionProtocol"), ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmIpCallHistorySessionTarget"), ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmIpCallHistoryMessageId"), ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmIpCallHistoryAccountId"), ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmIpCallHistoryAcceptMimeTypes"), ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmIpCallHistoryDiscdMimeTypes"), ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmIpCallHistoryNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmmIpCallGeneralGroup = cmmIpCallGeneralGroup.setStatus('current')
cmmIpCallImageGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 102, 3, 2, 3)).setObjects(("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmIpCallActiveImgEncodingType"), ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmIpCallActiveImgResolution"), ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmIpCallHistoryImgEncodingType"), ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmIpCallHistoryImgResolution"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmmIpCallImageGroup = cmmIpCallImageGroup.setStatus('current')
cmmFaxGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 102, 3, 2, 4)).setObjects(("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmFaxCfgCalledSubscriberId"), ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmFaxCfgXmitSubscriberId"), ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmFaxCfgRightHeadingString"), ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmFaxCfgCenterHeadingString"), ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmFaxCfgLeftHeadingString"), ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmFaxCfgCovergPageControl"), ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmFaxCfgCovergPageComment"), ("CISCO-MMAIL-DIAL-CONTROL-MIB", "cmmFaxCfgFaxProfile"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmmFaxGroup = cmmFaxGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-MMAIL-DIAL-CONTROL-MIB", cmmIpPeerCfgEntry=cmmIpPeerCfgEntry, cmmIpCallHistoryRemoteIPAddress=cmmIpCallHistoryRemoteIPAddress, cmmFaxCfgLeftHeadingString=cmmFaxCfgLeftHeadingString, ciscoMediaMailDialControlMIB=ciscoMediaMailDialControlMIB, cmmIpPeerCfgTable=cmmIpPeerCfgTable, CmmImgResolutionOrTransparent=CmmImgResolutionOrTransparent, cmmIpCallActiveAccountId=cmmIpCallActiveAccountId, cmmFaxCfgCovergPageComment=cmmFaxCfgCovergPageComment, CmmFaxHeadingString=CmmFaxHeadingString, cmmdcMIBConformance=cmmdcMIBConformance, cmmIpCallActiveMessageId=cmmIpCallActiveMessageId, cmmFaxCfgCovergPageControl=cmmFaxCfgCovergPageControl, cmmIpCallHistoryMessageId=cmmIpCallHistoryMessageId, cmmIpCallHistoryAccountId=cmmIpCallHistoryAccountId, cmmIpCallActiveImgEncodingType=cmmIpCallActiveImgEncodingType, cmmIpCallActiveSessionProtocol=cmmIpCallActiveSessionProtocol, cmmCallHistory=cmmCallHistory, cmmIpCallActiveNotification=cmmIpCallActiveNotification, cmmIpCallHistoryAcceptMimeTypes=cmmIpCallHistoryAcceptMimeTypes, cmmIpPeerCfgDeliStatNotification=cmmIpPeerCfgDeliStatNotification, cmmIpCallHistoryConnectionId=cmmIpCallHistoryConnectionId, cmmIpCallHistoryEntry=cmmIpCallHistoryEntry, CmmImgEncoding=CmmImgEncoding, cmmIpCallActiveTable=cmmIpCallActiveTable, cmmIpCallActiveAcceptMimeTypes=cmmIpCallActiveAcceptMimeTypes, cmmIpCallActiveRemoteIPAddress=cmmIpCallActiveRemoteIPAddress, cmmIpCallHistoryTable=cmmIpCallHistoryTable, CmmImgResolution=CmmImgResolution, cmmIpCallHistoryImgEncodingType=cmmIpCallHistoryImgEncodingType, cmmIpCallHistoryNotification=cmmIpCallHistoryNotification, cmmIpPeerCfgMsgDispoNotification=cmmIpPeerCfgMsgDispoNotification, cmmFaxCfgXmitSubscriberId=cmmFaxCfgXmitSubscriberId, cmmdcMIBCompliances=cmmdcMIBCompliances, cmmdcMIBCompliance=cmmdcMIBCompliance, cmmdcMIBObjects=cmmdcMIBObjects, CmmImgEncodingOrTransparent=CmmImgEncodingOrTransparent, cmmFaxGroup=cmmFaxGroup, cmmIpCallActiveSessionTarget=cmmIpCallActiveSessionTarget, cmmIpCallHistoryImgResolution=cmmIpCallHistoryImgResolution, cmmIpCallImageGroup=cmmIpCallImageGroup, cmmFaxCfgRightHeadingString=cmmFaxCfgRightHeadingString, cmmdcPeerCfgGroup=cmmdcPeerCfgGroup, cmmIpCallActiveImgResolution=cmmIpCallActiveImgResolution, cmmdcMIBGroups=cmmdcMIBGroups, cmmIpCallActiveDiscdMimeTypes=cmmIpCallActiveDiscdMimeTypes, cmmFaxCfgCenterHeadingString=cmmFaxCfgCenterHeadingString, cmmCallActive=cmmCallActive, cmmFaxCfgFaxProfile=cmmFaxCfgFaxProfile, PYSNMP_MODULE_ID=ciscoMediaMailDialControlMIB, cmmIpPeerCfgSessionTarget=cmmIpPeerCfgSessionTarget, cmmIpPeerCfgImgResolution=cmmIpPeerCfgImgResolution, cmmIpCallHistoryDiscdMimeTypes=cmmIpCallHistoryDiscdMimeTypes, cmmFaxCfgCalledSubscriberId=cmmFaxCfgCalledSubscriberId, cmmIpPeerCfgSessionProtocol=cmmIpPeerCfgSessionProtocol, cmmIpCallHistorySessionTarget=cmmIpCallHistorySessionTarget, cmmFaxGeneralCfg=cmmFaxGeneralCfg, cmmIpPeerCfgImgEncodingType=cmmIpPeerCfgImgEncodingType, cmmIpCallGeneralGroup=cmmIpCallGeneralGroup, cmmIpCallActiveEntry=cmmIpCallActiveEntry, cmmPeer=cmmPeer, cmmIpCallHistorySessionProtocol=cmmIpCallHistorySessionProtocol, cmmIpCallActiveConnectionId=cmmIpCallActiveConnectionId)
