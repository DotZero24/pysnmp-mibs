_Q='hpnicfDot11RadioElementRadioNum'
_P='not-accessible'
_O='invalidie'
_N='unknownfailure'
_M='cleartxt'
_L='dot11ac'
_K='dot11an'
_J='dot11gn'
_I='dot11g'
_H='dot11b'
_G='dot11a'
_F='hpnicfDot11APElementIndex'
_E='ext'
_D='read-only'
_C='HPN-ICF-DOT11-REF-MIB'
_B='none'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hpnicfDot11=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75))
if mibBuilder.loadTexts:hpnicfDot11.setRevisions(('2010-01-07 20:00','2009-05-07 20:00','2007-06-21 20:00','2007-04-27 20:00','2006-05-10 19:00'))
class HpnicfDot11ObjectIDType(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
class HpnicfDot11RadioScopeType(TextualConvention,Integer32):status=_A
class HpnicfDot11RadioType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,8,16,32,64)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,4),('dot11n',8),(_J,16),(_K,32),(_L,64)))
class HpnicfDot11RadioType2(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,8,16,32)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,4),(_K,8),(_J,16),(_L,32)))
class HpnicfDot11MACModeType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('split',1),('localtunnel',2),('localbridge',3),('fatAP',4)))
class HpnicfDot11ChannelScopeType(TextualConvention,Integer32):status=_A
class HpnicfDot11NotifyReasonType(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
class HpnicfDot11SSIDStringType(TextualConvention,OctetString):status=_A
class HpnicfDot11ServicePolicyIDType(TextualConvention,Integer32):status=_A
class HpnicfDot11SSIDEncryptModeType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),('cipher',2),(_E,3)))
class HpnicfDot11PreambleType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('long',1),('short',2)))
class HpnicfDot11TxPwrLevelScopeType(TextualConvention,Integer32):status=_A
class HpnicfDot11RFModeType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('manual',1),('auto',2)))
class HpnicfDot11TunnelSecSchemType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),('dtls',2),('ipsec',3)))
class HpnicfDot11SecIEStatusType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_B,1),('rsn',2),('wpa',3),('all',4),(_E,5)))
class HpnicfDot11CipherType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,16,32,64,128)));namedValues=NamedValues(*((_B,1),('wep40',2),('tkip',4),('aesccmp',16),('wep104',32),('wpisms4',64),('wep128',128)))
class HpnicfDot11AuthenType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_B,1),('opensystem',2),('sharedkey',3),('all',4)))
class HpnicfDot11AKMType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_B,1),('psk',2),('dot1x',3),(_E,4)))
class HpnicfDot11AssocFailType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_N,1),('toomanyassoc',2),(_O,3),('unsupportedrate',4),('unsupportedpwrcap',5),('unsupportedcap',6)))
class HpnicfDot11AuthorFailType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_N,1),(_O,2),('rsnieversionunsupported',3),('wpaieversionunsupported',4),('groupcipherinvalid',5),('pairwisecipherinvalid',6),('akminvalid',7)))
class HpnicfDot11QosAcType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('acbk',1),('acbe',2),('acvi',3),('acvo',4)))
class HpnicfDot11RadioElementIndex(TextualConvention,Unsigned32):status=_A
class HpnicfDot11WorkMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('normal',1),('monitor',2),('hybrid',3)))
class HpnicfDot11CirMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('static',1),('dynamic',2)))
class HpnicfDot11SaIntfDevType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('microwave',1),('microwaveInverter',2),('bluetooth',3),('fixedFreqOthers',4),('fixedFreqCordlessPhone',5),('fixedFreqVideo',6),('fixedFreqAudio',7),('freqHopperOthers',8),('freqHopperCordlessBase',9),('freqHopperCordlessNetwork',10),('freqHopperXbox',11),('genericInterferer',12)))
class HpnicfDot11TruthValueCM(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('dot11false',0),('dot11true',1)))
_HpnicfDot11Common_ObjectIdentity=ObjectIdentity
hpnicfDot11Common=_HpnicfDot11Common_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,12))
_HpnicfDot11ElementGroup_ObjectIdentity=ObjectIdentity
hpnicfDot11ElementGroup=_HpnicfDot11ElementGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,12,1))
_HpnicfDot11APElementTable_Object=MibTable
hpnicfDot11APElementTable=_HpnicfDot11APElementTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,12,1,1))
if mibBuilder.loadTexts:hpnicfDot11APElementTable.setStatus(_A)
_HpnicfDot11APElementEntry_Object=MibTableRow
hpnicfDot11APElementEntry=_HpnicfDot11APElementEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,12,1,1,1))
hpnicfDot11APElementEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:hpnicfDot11APElementEntry.setStatus(_A)
_HpnicfDot11APElementIndex_Type=Integer32
_HpnicfDot11APElementIndex_Object=MibTableColumn
hpnicfDot11APElementIndex=_HpnicfDot11APElementIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,12,1,1,1,1),_HpnicfDot11APElementIndex_Type())
hpnicfDot11APElementIndex.setMaxAccess(_P)
if mibBuilder.loadTexts:hpnicfDot11APElementIndex.setStatus(_A)
_HpnicfDot11APElementTemplateName_Type=OctetString
_HpnicfDot11APElementTemplateName_Object=MibTableColumn
hpnicfDot11APElementTemplateName=_HpnicfDot11APElementTemplateName_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,12,1,1,1,2),_HpnicfDot11APElementTemplateName_Type())
hpnicfDot11APElementTemplateName.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11APElementTemplateName.setStatus(_A)
_HpnicfDot11APElementSerialID_Type=OctetString
_HpnicfDot11APElementSerialID_Object=MibTableColumn
hpnicfDot11APElementSerialID=_HpnicfDot11APElementSerialID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,12,1,1,1,3),_HpnicfDot11APElementSerialID_Type())
hpnicfDot11APElementSerialID.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11APElementSerialID.setStatus(_A)
_HpnicfDot11APElementModelAlias_Type=OctetString
_HpnicfDot11APElementModelAlias_Object=MibTableColumn
hpnicfDot11APElementModelAlias=_HpnicfDot11APElementModelAlias_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,12,1,1,1,4),_HpnicfDot11APElementModelAlias_Type())
hpnicfDot11APElementModelAlias.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11APElementModelAlias.setStatus(_A)
_HpnicfDot11RadioElementTable_Object=MibTable
hpnicfDot11RadioElementTable=_HpnicfDot11RadioElementTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,12,1,2))
if mibBuilder.loadTexts:hpnicfDot11RadioElementTable.setStatus(_A)
_HpnicfDot11RadioElementEntry_Object=MibTableRow
hpnicfDot11RadioElementEntry=_HpnicfDot11RadioElementEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,12,1,2,1))
hpnicfDot11RadioElementEntry.setIndexNames((0,_C,_F),(0,_C,_Q))
if mibBuilder.loadTexts:hpnicfDot11RadioElementEntry.setStatus(_A)
_HpnicfDot11RadioElementRadioNum_Type=Unsigned32
_HpnicfDot11RadioElementRadioNum_Object=MibTableColumn
hpnicfDot11RadioElementRadioNum=_HpnicfDot11RadioElementRadioNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,12,1,2,1,1),_HpnicfDot11RadioElementRadioNum_Type())
hpnicfDot11RadioElementRadioNum.setMaxAccess(_P)
if mibBuilder.loadTexts:hpnicfDot11RadioElementRadioNum.setStatus(_A)
_HpnicfDot11RadioElementRadioPolicy_Type=OctetString
_HpnicfDot11RadioElementRadioPolicy_Object=MibTableColumn
hpnicfDot11RadioElementRadioPolicy=_HpnicfDot11RadioElementRadioPolicy_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,12,1,2,1,2),_HpnicfDot11RadioElementRadioPolicy_Type())
hpnicfDot11RadioElementRadioPolicy.setMaxAccess('read-write')
if mibBuilder.loadTexts:hpnicfDot11RadioElementRadioPolicy.setStatus(_A)
_HpnicfDot11RadioElementRadioIndex_Type=Unsigned32
_HpnicfDot11RadioElementRadioIndex_Object=MibTableColumn
hpnicfDot11RadioElementRadioIndex=_HpnicfDot11RadioElementRadioIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,12,1,2,1,3),_HpnicfDot11RadioElementRadioIndex_Type())
hpnicfDot11RadioElementRadioIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11RadioElementRadioIndex.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'HpnicfDot11ObjectIDType':HpnicfDot11ObjectIDType,'HpnicfDot11RadioScopeType':HpnicfDot11RadioScopeType,'HpnicfDot11RadioType':HpnicfDot11RadioType,'HpnicfDot11RadioType2':HpnicfDot11RadioType2,'HpnicfDot11MACModeType':HpnicfDot11MACModeType,'HpnicfDot11ChannelScopeType':HpnicfDot11ChannelScopeType,'HpnicfDot11NotifyReasonType':HpnicfDot11NotifyReasonType,'HpnicfDot11SSIDStringType':HpnicfDot11SSIDStringType,'HpnicfDot11ServicePolicyIDType':HpnicfDot11ServicePolicyIDType,'HpnicfDot11SSIDEncryptModeType':HpnicfDot11SSIDEncryptModeType,'HpnicfDot11PreambleType':HpnicfDot11PreambleType,'HpnicfDot11TxPwrLevelScopeType':HpnicfDot11TxPwrLevelScopeType,'HpnicfDot11RFModeType':HpnicfDot11RFModeType,'HpnicfDot11TunnelSecSchemType':HpnicfDot11TunnelSecSchemType,'HpnicfDot11SecIEStatusType':HpnicfDot11SecIEStatusType,'HpnicfDot11CipherType':HpnicfDot11CipherType,'HpnicfDot11AuthenType':HpnicfDot11AuthenType,'HpnicfDot11AKMType':HpnicfDot11AKMType,'HpnicfDot11AssocFailType':HpnicfDot11AssocFailType,'HpnicfDot11AuthorFailType':HpnicfDot11AuthorFailType,'HpnicfDot11QosAcType':HpnicfDot11QosAcType,'HpnicfDot11RadioElementIndex':HpnicfDot11RadioElementIndex,'HpnicfDot11WorkMode':HpnicfDot11WorkMode,'HpnicfDot11CirMode':HpnicfDot11CirMode,'HpnicfDot11SaIntfDevType':HpnicfDot11SaIntfDevType,'HpnicfDot11TruthValueCM':HpnicfDot11TruthValueCM,'hpnicfDot11':hpnicfDot11,'hpnicfDot11Common':hpnicfDot11Common,'hpnicfDot11ElementGroup':hpnicfDot11ElementGroup,'hpnicfDot11APElementTable':hpnicfDot11APElementTable,'hpnicfDot11APElementEntry':hpnicfDot11APElementEntry,_F:hpnicfDot11APElementIndex,'hpnicfDot11APElementTemplateName':hpnicfDot11APElementTemplateName,'hpnicfDot11APElementSerialID':hpnicfDot11APElementSerialID,'hpnicfDot11APElementModelAlias':hpnicfDot11APElementModelAlias,'hpnicfDot11RadioElementTable':hpnicfDot11RadioElementTable,'hpnicfDot11RadioElementEntry':hpnicfDot11RadioElementEntry,_Q:hpnicfDot11RadioElementRadioNum,'hpnicfDot11RadioElementRadioPolicy':hpnicfDot11RadioElementRadioPolicy,'hpnicfDot11RadioElementRadioIndex':hpnicfDot11RadioElementRadioIndex})