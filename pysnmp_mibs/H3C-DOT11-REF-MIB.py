#
# PySNMP MIB module H3C-DOT11-REF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/h3c/H3C-DOT11-REF-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:22:40 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
h3cDot11 = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75))
h3cDot11.setRevisions(('2016-03-11 18:00', '2010-01-07 20:00', '2009-05-07 20:00', '2007-06-21 20:00', '2007-04-27 20:00', '2006-05-10 19:00',))
if mibBuilder.loadTexts: h3cDot11.setLastUpdated('201603111800Z')
if mibBuilder.loadTexts: h3cDot11.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
class H3cDot11ObjectIDType(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 127)

class H3cDot11RadioScopeType(TextualConvention, Integer32):
    status = 'current'

class H3cDot11RadioType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4, 8, 16, 32, 64, 128))
    namedValues = NamedValues(("dot11a", 1), ("dot11b", 2), ("dot11g", 4), ("dot11n", 8), ("dot11gn", 16), ("dot11an", 32), ("dot11ac", 64), ("dot11gac", 128))

class H3cDot11RadioType2(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4, 8, 16, 32, 64))
    namedValues = NamedValues(("dot11a", 1), ("dot11b", 2), ("dot11g", 4), ("dot11an", 8), ("dot11gn", 16), ("dot11ac", 32), ("dot11gac", 64))

class H3cDot11MACModeType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("split", 1), ("localtunnel", 2), ("localbridge", 3), ("fatAP", 4))

class H3cDot11ChannelScopeType(TextualConvention, Integer32):
    status = 'current'

class H3cDot11NotifyReasonType(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class H3cDot11SSIDStringType(TextualConvention, OctetString):
    status = 'current'

class H3cDot11ServicePolicyIDType(TextualConvention, Integer32):
    status = 'current'

class H3cDot11SSIDEncryptModeType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("cleartxt", 1), ("cipher", 2), ("ext", 3))

class H3cDot11PreambleType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("long", 1), ("short", 2))

class H3cDot11TxPwrLevelScopeType(TextualConvention, Integer32):
    status = 'current'

class H3cDot11RFModeType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("manual", 1), ("auto", 2))

class H3cDot11TunnelSecSchemType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("cleartxt", 1), ("dtls", 2), ("ipsec", 3))

class H3cDot11SecIEStatusType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("none", 1), ("rsn", 2), ("wpa", 3), ("all", 4), ("ext", 5))

class H3cDot11CipherType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4, 16, 32, 64, 128))
    namedValues = NamedValues(("none", 1), ("wep40", 2), ("tkip", 4), ("aesccmp", 16), ("wep104", 32), ("wpisms4", 64), ("wep128", 128))

class H3cDot11AuthenType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("none", 1), ("opensystem", 2), ("sharedkey", 3), ("all", 4))

class H3cDot11AKMType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("none", 1), ("psk", 2), ("dot1x", 3), ("ext", 4))

class H3cDot11AssocFailType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("unknownfailure", 1), ("toomanyassoc", 2), ("invalidie", 3), ("unsupportedrate", 4), ("unsupportedpwrcap", 5), ("unsupportedcap", 6))

class H3cDot11AuthorFailType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("unknownfailure", 1), ("invalidie", 2), ("rsnieversionunsupported", 3), ("wpaieversionunsupported", 4), ("groupcipherinvalid", 5), ("pairwisecipherinvalid", 6), ("akminvalid", 7))

class H3cDot11QosAcType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("acbk", 1), ("acbe", 2), ("acvi", 3), ("acvo", 4))

class H3cDot11RadioElementIndex(TextualConvention, Unsigned32):
    status = 'current'

class H3cDot11WorkMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("normal", 1), ("monitor", 2), ("hybrid", 3))

class H3cDot11CirMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("static", 1), ("dynamic", 2))

class H3cDot11SaIntfDevType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("microwave", 1), ("microwaveInverter", 2), ("bluetooth", 3), ("fixedFreqOthers", 4), ("fixedFreqCordlessPhone", 5), ("fixedFreqVideo", 6), ("fixedFreqAudio", 7), ("freqHopperOthers", 8), ("freqHopperCordlessBase", 9), ("freqHopperCordlessNetwork", 10), ("freqHopperXbox", 11), ("genericInterferer", 12))

class H3cDot11TruthValueCM(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("dot11false", 0), ("dot11true", 1))

h3cDot11Common = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 12))
h3cDot11ElementGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 12, 1))
h3cDot11APElementTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 12, 1, 1), )
if mibBuilder.loadTexts: h3cDot11APElementTable.setStatus('current')
h3cDot11APElementEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 12, 1, 1, 1), ).setIndexNames((0, "H3C-DOT11-REF-MIB", "h3cDot11APElementIndex"))
if mibBuilder.loadTexts: h3cDot11APElementEntry.setStatus('current')
h3cDot11APElementIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 12, 1, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: h3cDot11APElementIndex.setStatus('current')
h3cDot11APElementTemplateName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 12, 1, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11APElementTemplateName.setStatus('current')
h3cDot11APElementSerialID = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 12, 1, 1, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11APElementSerialID.setStatus('current')
h3cDot11APElementModelAlias = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 12, 1, 1, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11APElementModelAlias.setStatus('current')
h3cDot11RadioElementTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 12, 1, 2), )
if mibBuilder.loadTexts: h3cDot11RadioElementTable.setStatus('current')
h3cDot11RadioElementEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 12, 1, 2, 1), ).setIndexNames((0, "H3C-DOT11-REF-MIB", "h3cDot11APElementIndex"), (0, "H3C-DOT11-REF-MIB", "h3cDot11RadioElementRadioNum"))
if mibBuilder.loadTexts: h3cDot11RadioElementEntry.setStatus('current')
h3cDot11RadioElementRadioNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 12, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: h3cDot11RadioElementRadioNum.setStatus('current')
h3cDot11RadioElementRadioPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 12, 1, 2, 1, 2), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cDot11RadioElementRadioPolicy.setStatus('current')
h3cDot11RadioElementRadioIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 75, 12, 1, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDot11RadioElementRadioIndex.setStatus('current')
mibBuilder.exportSymbols("H3C-DOT11-REF-MIB", h3cDot11RadioElementRadioPolicy=h3cDot11RadioElementRadioPolicy, h3cDot11=h3cDot11, H3cDot11CipherType=H3cDot11CipherType, H3cDot11TunnelSecSchemType=H3cDot11TunnelSecSchemType, h3cDot11APElementEntry=h3cDot11APElementEntry, H3cDot11PreambleType=H3cDot11PreambleType, H3cDot11TxPwrLevelScopeType=H3cDot11TxPwrLevelScopeType, H3cDot11RadioType=H3cDot11RadioType, H3cDot11RadioScopeType=H3cDot11RadioScopeType, H3cDot11ChannelScopeType=H3cDot11ChannelScopeType, H3cDot11SecIEStatusType=H3cDot11SecIEStatusType, PYSNMP_MODULE_ID=h3cDot11, H3cDot11NotifyReasonType=H3cDot11NotifyReasonType, H3cDot11AssocFailType=H3cDot11AssocFailType, H3cDot11SSIDStringType=H3cDot11SSIDStringType, h3cDot11RadioElementEntry=h3cDot11RadioElementEntry, H3cDot11AuthenType=H3cDot11AuthenType, H3cDot11TruthValueCM=H3cDot11TruthValueCM, h3cDot11APElementSerialID=h3cDot11APElementSerialID, H3cDot11RFModeType=H3cDot11RFModeType, h3cDot11APElementModelAlias=h3cDot11APElementModelAlias, h3cDot11APElementTable=h3cDot11APElementTable, H3cDot11ObjectIDType=H3cDot11ObjectIDType, H3cDot11SaIntfDevType=H3cDot11SaIntfDevType, h3cDot11APElementTemplateName=h3cDot11APElementTemplateName, h3cDot11RadioElementTable=h3cDot11RadioElementTable, h3cDot11RadioElementRadioNum=h3cDot11RadioElementRadioNum, h3cDot11APElementIndex=h3cDot11APElementIndex, H3cDot11ServicePolicyIDType=H3cDot11ServicePolicyIDType, H3cDot11AKMType=H3cDot11AKMType, h3cDot11ElementGroup=h3cDot11ElementGroup, h3cDot11Common=h3cDot11Common, H3cDot11AuthorFailType=H3cDot11AuthorFailType, H3cDot11RadioType2=H3cDot11RadioType2, H3cDot11WorkMode=H3cDot11WorkMode, H3cDot11CirMode=H3cDot11CirMode, H3cDot11RadioElementIndex=H3cDot11RadioElementIndex, H3cDot11QosAcType=H3cDot11QosAcType, H3cDot11SSIDEncryptModeType=H3cDot11SSIDEncryptModeType, H3cDot11MACModeType=H3cDot11MACModeType, h3cDot11RadioElementRadioIndex=h3cDot11RadioElementRadioIndex)
