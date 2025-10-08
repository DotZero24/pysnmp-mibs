#
# PySNMP MIB module HPN-ICF-DOT11-REF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hp/HPN-ICF-DOT11-REF-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:09:45 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hpnicfDot11 = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75))
hpnicfDot11.setRevisions(('2010-01-07 20:00', '2009-05-07 20:00', '2007-06-21 20:00', '2007-04-27 20:00', '2006-05-10 19:00',))
if mibBuilder.loadTexts: hpnicfDot11.setLastUpdated('201001072000Z')
if mibBuilder.loadTexts: hpnicfDot11.setOrganization('')
class HpnicfDot11ObjectIDType(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 127)

class HpnicfDot11RadioScopeType(TextualConvention, Integer32):
    status = 'current'

class HpnicfDot11RadioType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4, 8, 16, 32, 64))
    namedValues = NamedValues(("dot11a", 1), ("dot11b", 2), ("dot11g", 4), ("dot11n", 8), ("dot11gn", 16), ("dot11an", 32), ("dot11ac", 64))

class HpnicfDot11RadioType2(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4, 8, 16, 32))
    namedValues = NamedValues(("dot11a", 1), ("dot11b", 2), ("dot11g", 4), ("dot11an", 8), ("dot11gn", 16), ("dot11ac", 32))

class HpnicfDot11MACModeType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("split", 1), ("localtunnel", 2), ("localbridge", 3), ("fatAP", 4))

class HpnicfDot11ChannelScopeType(TextualConvention, Integer32):
    status = 'current'

class HpnicfDot11NotifyReasonType(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class HpnicfDot11SSIDStringType(TextualConvention, OctetString):
    status = 'current'

class HpnicfDot11ServicePolicyIDType(TextualConvention, Integer32):
    status = 'current'

class HpnicfDot11SSIDEncryptModeType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("cleartxt", 1), ("cipher", 2), ("ext", 3))

class HpnicfDot11PreambleType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("long", 1), ("short", 2))

class HpnicfDot11TxPwrLevelScopeType(TextualConvention, Integer32):
    status = 'current'

class HpnicfDot11RFModeType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("manual", 1), ("auto", 2))

class HpnicfDot11TunnelSecSchemType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("cleartxt", 1), ("dtls", 2), ("ipsec", 3))

class HpnicfDot11SecIEStatusType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("none", 1), ("rsn", 2), ("wpa", 3), ("all", 4), ("ext", 5))

class HpnicfDot11CipherType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4, 16, 32, 64, 128))
    namedValues = NamedValues(("none", 1), ("wep40", 2), ("tkip", 4), ("aesccmp", 16), ("wep104", 32), ("wpisms4", 64), ("wep128", 128))

class HpnicfDot11AuthenType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("none", 1), ("opensystem", 2), ("sharedkey", 3), ("all", 4))

class HpnicfDot11AKMType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("none", 1), ("psk", 2), ("dot1x", 3), ("ext", 4))

class HpnicfDot11AssocFailType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("unknownfailure", 1), ("toomanyassoc", 2), ("invalidie", 3), ("unsupportedrate", 4), ("unsupportedpwrcap", 5), ("unsupportedcap", 6))

class HpnicfDot11AuthorFailType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("unknownfailure", 1), ("invalidie", 2), ("rsnieversionunsupported", 3), ("wpaieversionunsupported", 4), ("groupcipherinvalid", 5), ("pairwisecipherinvalid", 6), ("akminvalid", 7))

class HpnicfDot11QosAcType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("acbk", 1), ("acbe", 2), ("acvi", 3), ("acvo", 4))

class HpnicfDot11RadioElementIndex(TextualConvention, Unsigned32):
    status = 'current'

class HpnicfDot11WorkMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("normal", 1), ("monitor", 2), ("hybrid", 3))

class HpnicfDot11CirMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("static", 1), ("dynamic", 2))

class HpnicfDot11SaIntfDevType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("microwave", 1), ("microwaveInverter", 2), ("bluetooth", 3), ("fixedFreqOthers", 4), ("fixedFreqCordlessPhone", 5), ("fixedFreqVideo", 6), ("fixedFreqAudio", 7), ("freqHopperOthers", 8), ("freqHopperCordlessBase", 9), ("freqHopperCordlessNetwork", 10), ("freqHopperXbox", 11), ("genericInterferer", 12))

class HpnicfDot11TruthValueCM(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("dot11false", 0), ("dot11true", 1))

hpnicfDot11Common = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 12))
hpnicfDot11ElementGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 12, 1))
hpnicfDot11APElementTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 12, 1, 1), )
if mibBuilder.loadTexts: hpnicfDot11APElementTable.setStatus('current')
hpnicfDot11APElementEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 12, 1, 1, 1), ).setIndexNames((0, "HPN-ICF-DOT11-REF-MIB", "hpnicfDot11APElementIndex"))
if mibBuilder.loadTexts: hpnicfDot11APElementEntry.setStatus('current')
hpnicfDot11APElementIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 12, 1, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: hpnicfDot11APElementIndex.setStatus('current')
hpnicfDot11APElementTemplateName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 12, 1, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot11APElementTemplateName.setStatus('current')
hpnicfDot11APElementSerialID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 12, 1, 1, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot11APElementSerialID.setStatus('current')
hpnicfDot11APElementModelAlias = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 12, 1, 1, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot11APElementModelAlias.setStatus('current')
hpnicfDot11RadioElementTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 12, 1, 2), )
if mibBuilder.loadTexts: hpnicfDot11RadioElementTable.setStatus('current')
hpnicfDot11RadioElementEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 12, 1, 2, 1), ).setIndexNames((0, "HPN-ICF-DOT11-REF-MIB", "hpnicfDot11APElementIndex"), (0, "HPN-ICF-DOT11-REF-MIB", "hpnicfDot11RadioElementRadioNum"))
if mibBuilder.loadTexts: hpnicfDot11RadioElementEntry.setStatus('current')
hpnicfDot11RadioElementRadioNum = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 12, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: hpnicfDot11RadioElementRadioNum.setStatus('current')
hpnicfDot11RadioElementRadioPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 12, 1, 2, 1, 2), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfDot11RadioElementRadioPolicy.setStatus('current')
hpnicfDot11RadioElementRadioIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 12, 1, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDot11RadioElementRadioIndex.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-DOT11-REF-MIB", HpnicfDot11ObjectIDType=HpnicfDot11ObjectIDType, hpnicfDot11RadioElementRadioPolicy=hpnicfDot11RadioElementRadioPolicy, hpnicfDot11RadioElementEntry=hpnicfDot11RadioElementEntry, HpnicfDot11CipherType=HpnicfDot11CipherType, HpnicfDot11TxPwrLevelScopeType=HpnicfDot11TxPwrLevelScopeType, HpnicfDot11TruthValueCM=HpnicfDot11TruthValueCM, HpnicfDot11AssocFailType=HpnicfDot11AssocFailType, HpnicfDot11TunnelSecSchemType=HpnicfDot11TunnelSecSchemType, HpnicfDot11MACModeType=HpnicfDot11MACModeType, HpnicfDot11SecIEStatusType=HpnicfDot11SecIEStatusType, hpnicfDot11RadioElementRadioIndex=hpnicfDot11RadioElementRadioIndex, HpnicfDot11SSIDEncryptModeType=HpnicfDot11SSIDEncryptModeType, HpnicfDot11RadioType2=HpnicfDot11RadioType2, hpnicfDot11RadioElementRadioNum=hpnicfDot11RadioElementRadioNum, hpnicfDot11APElementModelAlias=hpnicfDot11APElementModelAlias, hpnicfDot11Common=hpnicfDot11Common, hpnicfDot11APElementSerialID=hpnicfDot11APElementSerialID, hpnicfDot11ElementGroup=hpnicfDot11ElementGroup, HpnicfDot11CirMode=HpnicfDot11CirMode, hpnicfDot11=hpnicfDot11, HpnicfDot11NotifyReasonType=HpnicfDot11NotifyReasonType, hpnicfDot11APElementEntry=hpnicfDot11APElementEntry, HpnicfDot11ChannelScopeType=HpnicfDot11ChannelScopeType, HpnicfDot11AuthenType=HpnicfDot11AuthenType, hpnicfDot11APElementTable=hpnicfDot11APElementTable, HpnicfDot11QosAcType=HpnicfDot11QosAcType, HpnicfDot11RadioType=HpnicfDot11RadioType, hpnicfDot11APElementIndex=hpnicfDot11APElementIndex, hpnicfDot11APElementTemplateName=hpnicfDot11APElementTemplateName, HpnicfDot11PreambleType=HpnicfDot11PreambleType, HpnicfDot11ServicePolicyIDType=HpnicfDot11ServicePolicyIDType, hpnicfDot11RadioElementTable=hpnicfDot11RadioElementTable, HpnicfDot11AuthorFailType=HpnicfDot11AuthorFailType, HpnicfDot11RadioElementIndex=HpnicfDot11RadioElementIndex, HpnicfDot11SaIntfDevType=HpnicfDot11SaIntfDevType, HpnicfDot11RFModeType=HpnicfDot11RFModeType, HpnicfDot11AKMType=HpnicfDot11AKMType, PYSNMP_MODULE_ID=hpnicfDot11, HpnicfDot11SSIDStringType=HpnicfDot11SSIDStringType, HpnicfDot11RadioScopeType=HpnicfDot11RadioScopeType, HpnicfDot11WorkMode=HpnicfDot11WorkMode)
