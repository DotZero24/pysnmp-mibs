_i='hwVoPeerConfigCallerPermitNum'
_h='hwVoVoIPPeerConfigIndex'
_g='deprecated'
_f='hwVoPOTSPeerConfigIndex'
_e='private'
_d='subscriber'
_c='network'
_b='international'
_a='abbreviated'
_Z='h323-t38'
_Y='sip-t38'
_X='nonstandard-compatible'
_W='read-only'
_V='hwVoPeerConfigIndex'
_U='g729r8'
_T='reserved'
_S='national'
_R='default'
_Q='g729'
_P='g711u'
_O='g711a'
_N='voice'
_M='g711ulaw'
_L='g711alaw'
_K='unknown'
_J='HUAWEI-VO-DIAL-CONTROL-MIB'
_I='OctetString'
_H='g729a'
_G='g723r63'
_F='g723r53'
_E='enable'
_D='disable'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
voice,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB',_N)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hwVoiceDialControlMIB=ModuleIdentity((1,3,6,1,4,1,2011,5,25,1,5))
if mibBuilder.loadTexts:hwVoiceDialControlMIB.setRevisions(('2004-04-08 13:45',))
class EntryStatus(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('valid',1),('createRequest',2),('underCreation',3),('invalid',4)))
_HwVoPeerObjects_ObjectIdentity=ObjectIdentity
hwVoPeerObjects=_HwVoPeerObjects_ObjectIdentity((1,3,6,1,4,1,2011,5,25,1,5,1))
_HwVoPeerCommonConfigTable_Object=MibTable
hwVoPeerCommonConfigTable=_HwVoPeerCommonConfigTable_Object((1,3,6,1,4,1,2011,5,25,1,5,1,1))
if mibBuilder.loadTexts:hwVoPeerCommonConfigTable.setStatus(_A)
_HwVoPeerCommonConfigEntry_Object=MibTableRow
hwVoPeerCommonConfigEntry=_HwVoPeerCommonConfigEntry_Object((1,3,6,1,4,1,2011,5,25,1,5,1,1,1))
hwVoPeerCommonConfigEntry.setIndexNames((0,_J,_V))
if mibBuilder.loadTexts:hwVoPeerCommonConfigEntry.setStatus(_A)
class _HwVoPeerConfigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HwVoPeerConfigIndex_Type.__name__=_C
_HwVoPeerConfigIndex_Object=MibTableColumn
hwVoPeerConfigIndex=_HwVoPeerConfigIndex_Object((1,3,6,1,4,1,2011,5,25,1,5,1,1,1,1),_HwVoPeerConfigIndex_Type())
hwVoPeerConfigIndex.setMaxAccess(_W)
if mibBuilder.loadTexts:hwVoPeerConfigIndex.setStatus(_A)
class _HwVoPeerConfigType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('pots',1),('voip',2),('vofr',3)))
_HwVoPeerConfigType_Type.__name__=_C
_HwVoPeerConfigType_Object=MibTableColumn
hwVoPeerConfigType=_HwVoPeerConfigType_Object((1,3,6,1,4,1,2011,5,25,1,5,1,1,1,2),_HwVoPeerConfigType_Type())
hwVoPeerConfigType.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoPeerConfigType.setStatus(_A)
class _HwVoPeerConfigDesPattern_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_HwVoPeerConfigDesPattern_Type.__name__=_I
_HwVoPeerConfigDesPattern_Object=MibTableColumn
hwVoPeerConfigDesPattern=_HwVoPeerConfigDesPattern_Object((1,3,6,1,4,1,2011,5,25,1,5,1,1,1,3),_HwVoPeerConfigDesPattern_Type())
hwVoPeerConfigDesPattern.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoPeerConfigDesPattern.setStatus(_A)
class _HwVoPeerConfigCodec1st_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_O,1),(_P,2),(_F,3),(_G,4),(_Q,5),(_H,6),(_R,7)))
_HwVoPeerConfigCodec1st_Type.__name__=_C
_HwVoPeerConfigCodec1st_Object=MibTableColumn
hwVoPeerConfigCodec1st=_HwVoPeerConfigCodec1st_Object((1,3,6,1,4,1,2011,5,25,1,5,1,1,1,4),_HwVoPeerConfigCodec1st_Type())
hwVoPeerConfigCodec1st.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoPeerConfigCodec1st.setStatus(_A)
class _HwVoPeerConfigCodec2st_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_O,1),(_P,2),(_F,3),(_G,4),(_Q,5),(_H,6),(_R,7)))
_HwVoPeerConfigCodec2st_Type.__name__=_C
_HwVoPeerConfigCodec2st_Object=MibTableColumn
hwVoPeerConfigCodec2st=_HwVoPeerConfigCodec2st_Object((1,3,6,1,4,1,2011,5,25,1,5,1,1,1,5),_HwVoPeerConfigCodec2st_Type())
hwVoPeerConfigCodec2st.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoPeerConfigCodec2st.setStatus(_A)
class _HwVoPeerConfigCodec3st_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_O,1),(_P,2),(_F,3),(_G,4),(_Q,5),(_H,6),(_R,7)))
_HwVoPeerConfigCodec3st_Type.__name__=_C
_HwVoPeerConfigCodec3st_Object=MibTableColumn
hwVoPeerConfigCodec3st=_HwVoPeerConfigCodec3st_Object((1,3,6,1,4,1,2011,5,25,1,5,1,1,1,6),_HwVoPeerConfigCodec3st_Type())
hwVoPeerConfigCodec3st.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoPeerConfigCodec3st.setStatus(_A)
class _HwVoPeerConfigCodec4st_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_O,1),(_P,2),(_F,3),(_G,4),(_Q,5),(_H,6),(_R,7)))
_HwVoPeerConfigCodec4st_Type.__name__=_C
_HwVoPeerConfigCodec4st_Object=MibTableColumn
hwVoPeerConfigCodec4st=_HwVoPeerConfigCodec4st_Object((1,3,6,1,4,1,2011,5,25,1,5,1,1,1,7),_HwVoPeerConfigCodec4st_Type())
hwVoPeerConfigCodec4st.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoPeerConfigCodec4st.setStatus(_A)
class _HwVoPeerConfigIpPreced_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HwVoPeerConfigIpPreced_Type.__name__=_C
_HwVoPeerConfigIpPreced_Object=MibTableColumn
hwVoPeerConfigIpPreced=_HwVoPeerConfigIpPreced_Object((1,3,6,1,4,1,2011,5,25,1,5,1,1,1,8),_HwVoPeerConfigIpPreced_Type())
hwVoPeerConfigIpPreced.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoPeerConfigIpPreced.setStatus(_A)
class _HwVoPeerConfigShutDown_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_HwVoPeerConfigShutDown_Type.__name__=_C
_HwVoPeerConfigShutDown_Object=MibTableColumn
hwVoPeerConfigShutDown=_HwVoPeerConfigShutDown_Object((1,3,6,1,4,1,2011,5,25,1,5,1,1,1,9),_HwVoPeerConfigShutDown_Type())
hwVoPeerConfigShutDown.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoPeerConfigShutDown.setStatus(_A)
class _HwVoPeerConfigVADSwitch_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_HwVoPeerConfigVADSwitch_Type.__name__=_C
_HwVoPeerConfigVADSwitch_Object=MibTableColumn
hwVoPeerConfigVADSwitch=_HwVoPeerConfigVADSwitch_Object((1,3,6,1,4,1,2011,5,25,1,5,1,1,1,10),_HwVoPeerConfigVADSwitch_Type())
hwVoPeerConfigVADSwitch.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoPeerConfigVADSwitch.setStatus(_A)
class _HwVoPeerConfigDtmfRelay_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,12)));namedValues=NamedValues(*(('h245Alphanumeric',1),(_N,2),('sip',12)))
_HwVoPeerConfigDtmfRelay_Type.__name__=_C
_HwVoPeerConfigDtmfRelay_Object=MibTableColumn
hwVoPeerConfigDtmfRelay=_HwVoPeerConfigDtmfRelay_Object((1,3,6,1,4,1,2011,5,25,1,5,1,1,1,11),_HwVoPeerConfigDtmfRelay_Type())
hwVoPeerConfigDtmfRelay.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoPeerConfigDtmfRelay.setStatus(_A)
class _HwVoPeerConfigFaxLevel_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,60))
_HwVoPeerConfigFaxLevel_Type.__name__=_C
_HwVoPeerConfigFaxLevel_Object=MibTableColumn
hwVoPeerConfigFaxLevel=_HwVoPeerConfigFaxLevel_Object((1,3,6,1,4,1,2011,5,25,1,5,1,1,1,12),_HwVoPeerConfigFaxLevel_Type())
hwVoPeerConfigFaxLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoPeerConfigFaxLevel.setStatus(_A)
class _HwVoPeerConfigFaxRate_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('r14400',1),('r2400',2),('r4800',3),('r9600',4),(_D,5),(_N,6)))
_HwVoPeerConfigFaxRate_Type.__name__=_C
_HwVoPeerConfigFaxRate_Object=MibTableColumn
hwVoPeerConfigFaxRate=_HwVoPeerConfigFaxRate_Object((1,3,6,1,4,1,2011,5,25,1,5,1,1,1,13),_HwVoPeerConfigFaxRate_Type())
hwVoPeerConfigFaxRate.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoPeerConfigFaxRate.setStatus(_A)
class _HwVoPeerConfigFaxLocalTrainParam_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HwVoPeerConfigFaxLocalTrainParam_Type.__name__=_C
_HwVoPeerConfigFaxLocalTrainParam_Object=MibTableColumn
hwVoPeerConfigFaxLocalTrainParam=_HwVoPeerConfigFaxLocalTrainParam_Object((1,3,6,1,4,1,2011,5,25,1,5,1,1,1,14),_HwVoPeerConfigFaxLocalTrainParam_Type())
hwVoPeerConfigFaxLocalTrainParam.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoPeerConfigFaxLocalTrainParam.setStatus(_A)
class _HwVoPeerConfigFaxProtocol_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_X,1),('t38',2),('pcm',3),(_Y,4),(_Z,5)))
_HwVoPeerConfigFaxProtocol_Type.__name__=_C
_HwVoPeerConfigFaxProtocol_Object=MibTableColumn
hwVoPeerConfigFaxProtocol=_HwVoPeerConfigFaxProtocol_Object((1,3,6,1,4,1,2011,5,25,1,5,1,1,1,15),_HwVoPeerConfigFaxProtocol_Type())
hwVoPeerConfigFaxProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoPeerConfigFaxProtocol.setStatus(_A)
class _HwVoPeerConfigFaxT38HighRedunPackNumber_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_HwVoPeerConfigFaxT38HighRedunPackNumber_Type.__name__=_C
_HwVoPeerConfigFaxT38HighRedunPackNumber_Object=MibTableColumn
hwVoPeerConfigFaxT38HighRedunPackNumber=_HwVoPeerConfigFaxT38HighRedunPackNumber_Object((1,3,6,1,4,1,2011,5,25,1,5,1,1,1,16),_HwVoPeerConfigFaxT38HighRedunPackNumber_Type())
hwVoPeerConfigFaxT38HighRedunPackNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoPeerConfigFaxT38HighRedunPackNumber.setStatus(_A)
class _HwVoPeerConfigFaxT38LowRedunPackNumber_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_HwVoPeerConfigFaxT38LowRedunPackNumber_Type.__name__=_C
_HwVoPeerConfigFaxT38LowRedunPackNumber_Object=MibTableColumn
hwVoPeerConfigFaxT38LowRedunPackNumber=_HwVoPeerConfigFaxT38LowRedunPackNumber_Object((1,3,6,1,4,1,2011,5,25,1,5,1,1,1,17),_HwVoPeerConfigFaxT38LowRedunPackNumber_Type())
hwVoPeerConfigFaxT38LowRedunPackNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoPeerConfigFaxT38LowRedunPackNumber.setStatus(_A)
class _HwVoPeerConfigFaxSendNSFSwitch_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_HwVoPeerConfigFaxSendNSFSwitch_Type.__name__=_C
_HwVoPeerConfigFaxSendNSFSwitch_Object=MibTableColumn
hwVoPeerConfigFaxSendNSFSwitch=_HwVoPeerConfigFaxSendNSFSwitch_Object((1,3,6,1,4,1,2011,5,25,1,5,1,1,1,18),_HwVoPeerConfigFaxSendNSFSwitch_Type())
hwVoPeerConfigFaxSendNSFSwitch.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoPeerConfigFaxSendNSFSwitch.setStatus(_A)
class _HwVoPeerConfigFaxSupportMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4)));namedValues=NamedValues(*(('rtp',1),('vt',2),('sip-udp',4)))
_HwVoPeerConfigFaxSupportMode_Type.__name__=_C
_HwVoPeerConfigFaxSupportMode_Object=MibTableColumn
hwVoPeerConfigFaxSupportMode=_HwVoPeerConfigFaxSupportMode_Object((1,3,6,1,4,1,2011,5,25,1,5,1,1,1,19),_HwVoPeerConfigFaxSupportMode_Type())
hwVoPeerConfigFaxSupportMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoPeerConfigFaxSupportMode.setStatus(_A)
class _HwVoPeerConfigFaxTrainMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('local',1),('ppp',2)))
_HwVoPeerConfigFaxTrainMode_Type.__name__=_C
_HwVoPeerConfigFaxTrainMode_Object=MibTableColumn
hwVoPeerConfigFaxTrainMode=_HwVoPeerConfigFaxTrainMode_Object((1,3,6,1,4,1,2011,5,25,1,5,1,1,1,20),_HwVoPeerConfigFaxTrainMode_Type())
hwVoPeerConfigFaxTrainMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoPeerConfigFaxTrainMode.setStatus(_A)
class _HwVoPeerConfigFaxRelay_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ecm',1),('noecm',2)))
_HwVoPeerConfigFaxRelay_Type.__name__=_C
_HwVoPeerConfigFaxRelay_Object=MibTableColumn
hwVoPeerConfigFaxRelay=_HwVoPeerConfigFaxRelay_Object((1,3,6,1,4,1,2011,5,25,1,5,1,1,1,21),_HwVoPeerConfigFaxRelay_Type())
hwVoPeerConfigFaxRelay.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoPeerConfigFaxRelay.setStatus(_A)
_HwVoPeerConfigRowStatus_Type=EntryStatus
_HwVoPeerConfigRowStatus_Object=MibTableColumn
hwVoPeerConfigRowStatus=_HwVoPeerConfigRowStatus_Object((1,3,6,1,4,1,2011,5,25,1,5,1,1,1,22),_HwVoPeerConfigRowStatus_Type())
hwVoPeerConfigRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoPeerConfigRowStatus.setStatus(_A)
class _HwVoPeerConfigFaxPassthroughMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,3)));namedValues=NamedValues(*((_K,0),(_L,1),(_M,3)))
_HwVoPeerConfigFaxPassthroughMode_Type.__name__=_C
_HwVoPeerConfigFaxPassthroughMode_Object=MibTableColumn
hwVoPeerConfigFaxPassthroughMode=_HwVoPeerConfigFaxPassthroughMode_Object((1,3,6,1,4,1,2011,5,25,1,5,1,1,1,23),_HwVoPeerConfigFaxPassthroughMode_Type())
hwVoPeerConfigFaxPassthroughMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoPeerConfigFaxPassthroughMode.setStatus(_A)
class _HwVoPeerConfigPriority_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_HwVoPeerConfigPriority_Type.__name__=_C
_HwVoPeerConfigPriority_Object=MibTableColumn
hwVoPeerConfigPriority=_HwVoPeerConfigPriority_Object((1,3,6,1,4,1,2011,5,25,1,5,1,1,1,24),_HwVoPeerConfigPriority_Type())
hwVoPeerConfigPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoPeerConfigPriority.setStatus(_A)
class _HwVoPeerConfigAuthorizationLevel_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9))
_HwVoPeerConfigAuthorizationLevel_Type.__name__=_C
_HwVoPeerConfigAuthorizationLevel_Object=MibTableColumn
hwVoPeerConfigAuthorizationLevel=_HwVoPeerConfigAuthorizationLevel_Object((1,3,6,1,4,1,2011,5,25,1,5,1,1,1,25),_HwVoPeerConfigAuthorizationLevel_Type())
hwVoPeerConfigAuthorizationLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoPeerConfigAuthorizationLevel.setStatus(_A)
class _HwVoPeerConfigDescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HwVoPeerConfigDescription_Type.__name__=_I
_HwVoPeerConfigDescription_Object=MibTableColumn
hwVoPeerConfigDescription=_HwVoPeerConfigDescription_Object((1,3,6,1,4,1,2011,5,25,1,5,1,1,1,26),_HwVoPeerConfigDescription_Type())
hwVoPeerConfigDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoPeerConfigDescription.setStatus(_A)
class _HwVoPeerConfigCallingNumberType_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_a,1),(_b,2),(_S,3),(_c,4),(_T,5),(_d,6),(_K,7)))
_HwVoPeerConfigCallingNumberType_Type.__name__=_C
_HwVoPeerConfigCallingNumberType_Object=MibTableColumn
hwVoPeerConfigCallingNumberType=_HwVoPeerConfigCallingNumberType_Object((1,3,6,1,4,1,2011,5,25,1,5,1,1,1,27),_HwVoPeerConfigCallingNumberType_Type())
hwVoPeerConfigCallingNumberType.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoPeerConfigCallingNumberType.setStatus(_A)
class _HwVoPeerConfigCalledNumberType_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_a,1),(_b,2),(_S,3),(_c,4),(_T,5),(_d,6),(_K,7)))
_HwVoPeerConfigCalledNumberType_Type.__name__=_C
_HwVoPeerConfigCalledNumberType_Object=MibTableColumn
hwVoPeerConfigCalledNumberType=_HwVoPeerConfigCalledNumberType_Object((1,3,6,1,4,1,2011,5,25,1,5,1,1,1,28),_HwVoPeerConfigCalledNumberType_Type())
hwVoPeerConfigCalledNumberType.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoPeerConfigCalledNumberType.setStatus(_A)
class _HwVoPeerConfigCallingNumberingPlan_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('data',1),('isdn',2),(_S,3),(_e,4),(_T,5),('telex',6),(_K,7)))
_HwVoPeerConfigCallingNumberingPlan_Type.__name__=_C
_HwVoPeerConfigCallingNumberingPlan_Object=MibTableColumn
hwVoPeerConfigCallingNumberingPlan=_HwVoPeerConfigCallingNumberingPlan_Object((1,3,6,1,4,1,2011,5,25,1,5,1,1,1,29),_HwVoPeerConfigCallingNumberingPlan_Type())
hwVoPeerConfigCallingNumberingPlan.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoPeerConfigCallingNumberingPlan.setStatus(_A)
class _HwVoPeerConfigCalledNumberingPlan_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('data',1),('isdn',2),(_S,3),(_e,4),(_T,5),('telex',6),(_K,7)))
_HwVoPeerConfigCalledNumberingPlan_Type.__name__=_C
_HwVoPeerConfigCalledNumberingPlan_Object=MibTableColumn
hwVoPeerConfigCalledNumberingPlan=_HwVoPeerConfigCalledNumberingPlan_Object((1,3,6,1,4,1,2011,5,25,1,5,1,1,1,30),_HwVoPeerConfigCalledNumberingPlan_Type())
hwVoPeerConfigCalledNumberingPlan.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoPeerConfigCalledNumberingPlan.setStatus(_A)
class _HwVoPeerConfigSelectStop_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_HwVoPeerConfigSelectStop_Type.__name__=_C
_HwVoPeerConfigSelectStop_Object=MibTableColumn
hwVoPeerConfigSelectStop=_HwVoPeerConfigSelectStop_Object((1,3,6,1,4,1,2011,5,25,1,5,1,1,1,31),_HwVoPeerConfigSelectStop_Type())
hwVoPeerConfigSelectStop.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoPeerConfigSelectStop.setStatus(_A)
class _HwVoPeerConfigCallingNumSubstRule_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HwVoPeerConfigCallingNumSubstRule_Type.__name__=_C
_HwVoPeerConfigCallingNumSubstRule_Object=MibTableColumn
hwVoPeerConfigCallingNumSubstRule=_HwVoPeerConfigCallingNumSubstRule_Object((1,3,6,1,4,1,2011,5,25,1,5,1,1,1,32),_HwVoPeerConfigCallingNumSubstRule_Type())
hwVoPeerConfigCallingNumSubstRule.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoPeerConfigCallingNumSubstRule.setStatus(_A)
class _HwVoPeerConfigCalledNumSubstRule_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HwVoPeerConfigCalledNumSubstRule_Type.__name__=_C
_HwVoPeerConfigCalledNumSubstRule_Object=MibTableColumn
hwVoPeerConfigCalledNumSubstRule=_HwVoPeerConfigCalledNumSubstRule_Object((1,3,6,1,4,1,2011,5,25,1,5,1,1,1,33),_HwVoPeerConfigCalledNumSubstRule_Type())
hwVoPeerConfigCalledNumSubstRule.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoPeerConfigCalledNumSubstRule.setStatus(_A)
class _HwVoPeerConfigMaxCall_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HwVoPeerConfigMaxCall_Type.__name__=_C
_HwVoPeerConfigMaxCall_Object=MibTableColumn
hwVoPeerConfigMaxCall=_HwVoPeerConfigMaxCall_Object((1,3,6,1,4,1,2011,5,25,1,5,1,1,1,34),_HwVoPeerConfigMaxCall_Type())
hwVoPeerConfigMaxCall.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoPeerConfigMaxCall.setStatus(_A)
_HwVoPOTSPeerConfigTable_Object=MibTable
hwVoPOTSPeerConfigTable=_HwVoPOTSPeerConfigTable_Object((1,3,6,1,4,1,2011,5,25,1,5,1,2))
if mibBuilder.loadTexts:hwVoPOTSPeerConfigTable.setStatus(_A)
_HwVoPOTSPeerConfigEntry_Object=MibTableRow
hwVoPOTSPeerConfigEntry=_HwVoPOTSPeerConfigEntry_Object((1,3,6,1,4,1,2011,5,25,1,5,1,2,1))
hwVoPOTSPeerConfigEntry.setIndexNames((0,_J,_f))
if mibBuilder.loadTexts:hwVoPOTSPeerConfigEntry.setStatus(_A)
class _HwVoPOTSPeerConfigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HwVoPOTSPeerConfigIndex_Type.__name__=_C
_HwVoPOTSPeerConfigIndex_Object=MibTableColumn
hwVoPOTSPeerConfigIndex=_HwVoPOTSPeerConfigIndex_Object((1,3,6,1,4,1,2011,5,25,1,5,1,2,1,1),_HwVoPOTSPeerConfigIndex_Type())
hwVoPOTSPeerConfigIndex.setMaxAccess(_W)
if mibBuilder.loadTexts:hwVoPOTSPeerConfigIndex.setStatus(_A)
class _HwVoPOTSPeerConfigCancelTruncateEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_HwVoPOTSPeerConfigCancelTruncateEnable_Type.__name__=_C
_HwVoPOTSPeerConfigCancelTruncateEnable_Object=MibTableColumn
hwVoPOTSPeerConfigCancelTruncateEnable=_HwVoPOTSPeerConfigCancelTruncateEnable_Object((1,3,6,1,4,1,2011,5,25,1,5,1,2,1,2),_HwVoPOTSPeerConfigCancelTruncateEnable_Type())
hwVoPOTSPeerConfigCancelTruncateEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoPOTSPeerConfigCancelTruncateEnable.setStatus(_g)
class _HwVoPOTSPeerConfigPrefix_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_HwVoPOTSPeerConfigPrefix_Type.__name__=_I
_HwVoPOTSPeerConfigPrefix_Object=MibTableColumn
hwVoPOTSPeerConfigPrefix=_HwVoPOTSPeerConfigPrefix_Object((1,3,6,1,4,1,2011,5,25,1,5,1,2,1,3),_HwVoPOTSPeerConfigPrefix_Type())
hwVoPOTSPeerConfigPrefix.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoPOTSPeerConfigPrefix.setStatus(_A)
class _HwVoPOTSPeerConfigPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,6))
_HwVoPOTSPeerConfigPort_Type.__name__=_I
_HwVoPOTSPeerConfigPort_Object=MibTableColumn
hwVoPOTSPeerConfigPort=_HwVoPOTSPeerConfigPort_Object((1,3,6,1,4,1,2011,5,25,1,5,1,2,1,4),_HwVoPOTSPeerConfigPort_Type())
hwVoPOTSPeerConfigPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoPOTSPeerConfigPort.setStatus(_A)
class _HwVoPOTSPeerConfigSendNumber_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,31))
_HwVoPOTSPeerConfigSendNumber_Type.__name__=_C
_HwVoPOTSPeerConfigSendNumber_Object=MibTableColumn
hwVoPOTSPeerConfigSendNumber=_HwVoPOTSPeerConfigSendNumber_Object((1,3,6,1,4,1,2011,5,25,1,5,1,2,1,5),_HwVoPOTSPeerConfigSendNumber_Type())
hwVoPOTSPeerConfigSendNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoPOTSPeerConfigSendNumber.setStatus(_A)
_HwVoVoIPPeerConfigTable_Object=MibTable
hwVoVoIPPeerConfigTable=_HwVoVoIPPeerConfigTable_Object((1,3,6,1,4,1,2011,5,25,1,5,1,3))
if mibBuilder.loadTexts:hwVoVoIPPeerConfigTable.setStatus(_A)
_HwVoVoIPPeerConfigEntry_Object=MibTableRow
hwVoVoIPPeerConfigEntry=_HwVoVoIPPeerConfigEntry_Object((1,3,6,1,4,1,2011,5,25,1,5,1,3,1))
hwVoVoIPPeerConfigEntry.setIndexNames((0,_J,_h))
if mibBuilder.loadTexts:hwVoVoIPPeerConfigEntry.setStatus(_A)
class _HwVoVoIPPeerConfigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HwVoVoIPPeerConfigIndex_Type.__name__=_C
_HwVoVoIPPeerConfigIndex_Object=MibTableColumn
hwVoVoIPPeerConfigIndex=_HwVoVoIPPeerConfigIndex_Object((1,3,6,1,4,1,2011,5,25,1,5,1,3,1,1),_HwVoVoIPPeerConfigIndex_Type())
hwVoVoIPPeerConfigIndex.setMaxAccess(_W)
if mibBuilder.loadTexts:hwVoVoIPPeerConfigIndex.setStatus(_A)
class _HwVoVoIPPeerConfigSessionTargetType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ipv4',1),('ras',2),(_K,3)))
_HwVoVoIPPeerConfigSessionTargetType_Type.__name__=_C
_HwVoVoIPPeerConfigSessionTargetType_Object=MibTableColumn
hwVoVoIPPeerConfigSessionTargetType=_HwVoVoIPPeerConfigSessionTargetType_Object((1,3,6,1,4,1,2011,5,25,1,5,1,3,1,2),_HwVoVoIPPeerConfigSessionTargetType_Type())
hwVoVoIPPeerConfigSessionTargetType.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoVoIPPeerConfigSessionTargetType.setStatus(_A)
_HwVoVoIPPeerConfigSessionTarget_Type=IpAddress
_HwVoVoIPPeerConfigSessionTarget_Object=MibTableColumn
hwVoVoIPPeerConfigSessionTarget=_HwVoVoIPPeerConfigSessionTarget_Object((1,3,6,1,4,1,2011,5,25,1,5,1,3,1,3),_HwVoVoIPPeerConfigSessionTarget_Type())
hwVoVoIPPeerConfigSessionTarget.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoVoIPPeerConfigSessionTarget.setStatus(_A)
class _HwVoVoIPPeerConfigFastSwitch_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_HwVoVoIPPeerConfigFastSwitch_Type.__name__=_C
_HwVoVoIPPeerConfigFastSwitch_Object=MibTableColumn
hwVoVoIPPeerConfigFastSwitch=_HwVoVoIPPeerConfigFastSwitch_Object((1,3,6,1,4,1,2011,5,25,1,5,1,3,1,4),_HwVoVoIPPeerConfigFastSwitch_Type())
hwVoVoIPPeerConfigFastSwitch.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoVoIPPeerConfigFastSwitch.setStatus(_A)
class _HwVoVoIPPeerConfigTunnelSwitch_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_HwVoVoIPPeerConfigTunnelSwitch_Type.__name__=_C
_HwVoVoIPPeerConfigTunnelSwitch_Object=MibTableColumn
hwVoVoIPPeerConfigTunnelSwitch=_HwVoVoIPPeerConfigTunnelSwitch_Object((1,3,6,1,4,1,2011,5,25,1,5,1,3,1,5),_HwVoVoIPPeerConfigTunnelSwitch_Type())
hwVoVoIPPeerConfigTunnelSwitch.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoVoIPPeerConfigTunnelSwitch.setStatus(_A)
class _HwVoVoIPPeerConfigTeachPrefix_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_HwVoVoIPPeerConfigTeachPrefix_Type.__name__=_I
_HwVoVoIPPeerConfigTeachPrefix_Object=MibTableColumn
hwVoVoIPPeerConfigTeachPrefix=_HwVoVoIPPeerConfigTeachPrefix_Object((1,3,6,1,4,1,2011,5,25,1,5,1,3,1,6),_HwVoVoIPPeerConfigTeachPrefix_Type())
hwVoVoIPPeerConfigTeachPrefix.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoVoIPPeerConfigTeachPrefix.setStatus(_A)
class _HwVoVoIPPeerConfigSendRing_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_HwVoVoIPPeerConfigSendRing_Type.__name__=_C
_HwVoVoIPPeerConfigSendRing_Object=MibTableColumn
hwVoVoIPPeerConfigSendRing=_HwVoVoIPPeerConfigSendRing_Object((1,3,6,1,4,1,2011,5,25,1,5,1,3,1,7),_HwVoVoIPPeerConfigSendRing_Type())
hwVoVoIPPeerConfigSendRing.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoVoIPPeerConfigSendRing.setStatus(_A)
_HwVoPeerDefaultConfigObjects_ObjectIdentity=ObjectIdentity
hwVoPeerDefaultConfigObjects=_HwVoPeerDefaultConfigObjects_ObjectIdentity((1,3,6,1,4,1,2011,5,25,1,5,1,4))
class _HwVoPeerDefaultConfigCancelTrun_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_HwVoPeerDefaultConfigCancelTrun_Type.__name__=_C
_HwVoPeerDefaultConfigCancelTrun_Object=MibScalar
hwVoPeerDefaultConfigCancelTrun=_HwVoPeerDefaultConfigCancelTrun_Object((1,3,6,1,4,1,2011,5,25,1,5,1,4,1),_HwVoPeerDefaultConfigCancelTrun_Type())
hwVoPeerDefaultConfigCancelTrun.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoPeerDefaultConfigCancelTrun.setStatus(_g)
class _HwVoPeerDefaultConfig1STCodecLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_U,0),(_L,1),(_G,2),(_F,3),(_M,4),(_H,5)))
_HwVoPeerDefaultConfig1STCodecLevel_Type.__name__=_C
_HwVoPeerDefaultConfig1STCodecLevel_Object=MibScalar
hwVoPeerDefaultConfig1STCodecLevel=_HwVoPeerDefaultConfig1STCodecLevel_Object((1,3,6,1,4,1,2011,5,25,1,5,1,4,2),_HwVoPeerDefaultConfig1STCodecLevel_Type())
hwVoPeerDefaultConfig1STCodecLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoPeerDefaultConfig1STCodecLevel.setStatus(_A)
class _HwVoPeerDefaultConfig2NDCodecLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_U,0),(_L,1),(_G,2),(_F,3),(_M,4),(_H,5)))
_HwVoPeerDefaultConfig2NDCodecLevel_Type.__name__=_C
_HwVoPeerDefaultConfig2NDCodecLevel_Object=MibScalar
hwVoPeerDefaultConfig2NDCodecLevel=_HwVoPeerDefaultConfig2NDCodecLevel_Object((1,3,6,1,4,1,2011,5,25,1,5,1,4,3),_HwVoPeerDefaultConfig2NDCodecLevel_Type())
hwVoPeerDefaultConfig2NDCodecLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoPeerDefaultConfig2NDCodecLevel.setStatus(_A)
class _HwVoPeerDefaultConfig3RDCodecLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_U,0),(_L,1),(_G,2),(_F,3),(_M,4),(_H,5)))
_HwVoPeerDefaultConfig3RDCodecLevel_Type.__name__=_C
_HwVoPeerDefaultConfig3RDCodecLevel_Object=MibScalar
hwVoPeerDefaultConfig3RDCodecLevel=_HwVoPeerDefaultConfig3RDCodecLevel_Object((1,3,6,1,4,1,2011,5,25,1,5,1,4,4),_HwVoPeerDefaultConfig3RDCodecLevel_Type())
hwVoPeerDefaultConfig3RDCodecLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoPeerDefaultConfig3RDCodecLevel.setStatus(_A)
class _HwVoPeerDefaultConfig4THCodecLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_U,0),(_L,1),(_G,2),(_F,3),(_M,4),(_H,5)))
_HwVoPeerDefaultConfig4THCodecLevel_Type.__name__=_C
_HwVoPeerDefaultConfig4THCodecLevel_Object=MibScalar
hwVoPeerDefaultConfig4THCodecLevel=_HwVoPeerDefaultConfig4THCodecLevel_Object((1,3,6,1,4,1,2011,5,25,1,5,1,4,5),_HwVoPeerDefaultConfig4THCodecLevel_Type())
hwVoPeerDefaultConfig4THCodecLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoPeerDefaultConfig4THCodecLevel.setStatus(_A)
class _HwVoPeerDefaultConfigVADOn_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_HwVoPeerDefaultConfigVADOn_Type.__name__=_C
_HwVoPeerDefaultConfigVADOn_Object=MibScalar
hwVoPeerDefaultConfigVADOn=_HwVoPeerDefaultConfigVADOn_Object((1,3,6,1,4,1,2011,5,25,1,5,1,4,6),_HwVoPeerDefaultConfigVADOn_Type())
hwVoPeerDefaultConfigVADOn.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoPeerDefaultConfigVADOn.setStatus(_A)
class _HwVoPeerDefaultConfigFaxTransmitLevel_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,60))
_HwVoPeerDefaultConfigFaxTransmitLevel_Type.__name__=_C
_HwVoPeerDefaultConfigFaxTransmitLevel_Object=MibScalar
hwVoPeerDefaultConfigFaxTransmitLevel=_HwVoPeerDefaultConfigFaxTransmitLevel_Object((1,3,6,1,4,1,2011,5,25,1,5,1,4,7),_HwVoPeerDefaultConfigFaxTransmitLevel_Type())
hwVoPeerDefaultConfigFaxTransmitLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoPeerDefaultConfigFaxTransmitLevel.setStatus(_A)
class _HwVoPeerDefaultConfigFaxLocalTrain_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HwVoPeerDefaultConfigFaxLocalTrain_Type.__name__=_C
_HwVoPeerDefaultConfigFaxLocalTrain_Object=MibScalar
hwVoPeerDefaultConfigFaxLocalTrain=_HwVoPeerDefaultConfigFaxLocalTrain_Object((1,3,6,1,4,1,2011,5,25,1,5,1,4,8),_HwVoPeerDefaultConfigFaxLocalTrain_Type())
hwVoPeerDefaultConfigFaxLocalTrain.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoPeerDefaultConfigFaxLocalTrain.setStatus(_A)
class _HwVoPeerDefaultConfigFaxProtocol_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_X,1),('t38',2),(_Z,3),(_Y,4),('pcm-alaw',5),('pcm-ulaw',6)))
_HwVoPeerDefaultConfigFaxProtocol_Type.__name__=_C
_HwVoPeerDefaultConfigFaxProtocol_Object=MibScalar
hwVoPeerDefaultConfigFaxProtocol=_HwVoPeerDefaultConfigFaxProtocol_Object((1,3,6,1,4,1,2011,5,25,1,5,1,4,9),_HwVoPeerDefaultConfigFaxProtocol_Type())
hwVoPeerDefaultConfigFaxProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoPeerDefaultConfigFaxProtocol.setStatus(_A)
class _HwVoPeerDefaultConfigFaxHSRedundancy_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_HwVoPeerDefaultConfigFaxHSRedundancy_Type.__name__=_C
_HwVoPeerDefaultConfigFaxHSRedundancy_Object=MibScalar
hwVoPeerDefaultConfigFaxHSRedundancy=_HwVoPeerDefaultConfigFaxHSRedundancy_Object((1,3,6,1,4,1,2011,5,25,1,5,1,4,10),_HwVoPeerDefaultConfigFaxHSRedundancy_Type())
hwVoPeerDefaultConfigFaxHSRedundancy.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoPeerDefaultConfigFaxHSRedundancy.setStatus(_A)
class _HwVoPeerDefaultConfigFaxLSRedundancy_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_HwVoPeerDefaultConfigFaxLSRedundancy_Type.__name__=_C
_HwVoPeerDefaultConfigFaxLSRedundancy_Object=MibScalar
hwVoPeerDefaultConfigFaxLSRedundancy=_HwVoPeerDefaultConfigFaxLSRedundancy_Object((1,3,6,1,4,1,2011,5,25,1,5,1,4,11),_HwVoPeerDefaultConfigFaxLSRedundancy_Type())
hwVoPeerDefaultConfigFaxLSRedundancy.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoPeerDefaultConfigFaxLSRedundancy.setStatus(_A)
class _HwVoPeerDefaultConfigFaxBaudrate_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,3,5,7,8)));namedValues=NamedValues(*((_D,0),('b2400',2),('b4800',3),('b9600',5),('b14400',7),(_N,8)))
_HwVoPeerDefaultConfigFaxBaudrate_Type.__name__=_C
_HwVoPeerDefaultConfigFaxBaudrate_Object=MibScalar
hwVoPeerDefaultConfigFaxBaudrate=_HwVoPeerDefaultConfigFaxBaudrate_Object((1,3,6,1,4,1,2011,5,25,1,5,1,4,12),_HwVoPeerDefaultConfigFaxBaudrate_Type())
hwVoPeerDefaultConfigFaxBaudrate.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoPeerDefaultConfigFaxBaudrate.setStatus(_A)
class _HwVoPeerDefaultConfigFaxNSF_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_HwVoPeerDefaultConfigFaxNSF_Type.__name__=_C
_HwVoPeerDefaultConfigFaxNSF_Object=MibScalar
hwVoPeerDefaultConfigFaxNSF=_HwVoPeerDefaultConfigFaxNSF_Object((1,3,6,1,4,1,2011,5,25,1,5,1,4,13),_HwVoPeerDefaultConfigFaxNSF_Type())
hwVoPeerDefaultConfigFaxNSF.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoPeerDefaultConfigFaxNSF.setStatus(_A)
class _HwVoPeerDefaultConfigFaxSupportMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('rtp',1),('vt',2)))
_HwVoPeerDefaultConfigFaxSupportMode_Type.__name__=_C
_HwVoPeerDefaultConfigFaxSupportMode_Object=MibScalar
hwVoPeerDefaultConfigFaxSupportMode=_HwVoPeerDefaultConfigFaxSupportMode_Object((1,3,6,1,4,1,2011,5,25,1,5,1,4,14),_HwVoPeerDefaultConfigFaxSupportMode_Type())
hwVoPeerDefaultConfigFaxSupportMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoPeerDefaultConfigFaxSupportMode.setStatus(_A)
class _HwVoPeerDefaultConfigFaxTrainMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ppp',1),('local',2)))
_HwVoPeerDefaultConfigFaxTrainMode_Type.__name__=_C
_HwVoPeerDefaultConfigFaxTrainMode_Object=MibScalar
hwVoPeerDefaultConfigFaxTrainMode=_HwVoPeerDefaultConfigFaxTrainMode_Object((1,3,6,1,4,1,2011,5,25,1,5,1,4,15),_HwVoPeerDefaultConfigFaxTrainMode_Type())
hwVoPeerDefaultConfigFaxTrainMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoPeerDefaultConfigFaxTrainMode.setStatus(_A)
class _HwVoPeerDefaultConfigFaxECM_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_D,2)))
_HwVoPeerDefaultConfigFaxECM_Type.__name__=_C
_HwVoPeerDefaultConfigFaxECM_Object=MibScalar
hwVoPeerDefaultConfigFaxECM=_HwVoPeerDefaultConfigFaxECM_Object((1,3,6,1,4,1,2011,5,25,1,5,1,4,16),_HwVoPeerDefaultConfigFaxECM_Type())
hwVoPeerDefaultConfigFaxECM.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoPeerDefaultConfigFaxECM.setStatus(_A)
_HwVoPeerConfigCallerPermitNumTable_Object=MibTable
hwVoPeerConfigCallerPermitNumTable=_HwVoPeerConfigCallerPermitNumTable_Object((1,3,6,1,4,1,2011,5,25,1,5,1,5))
if mibBuilder.loadTexts:hwVoPeerConfigCallerPermitNumTable.setStatus(_A)
_HwVoPeerConfigCallerPermitNumEntry_Object=MibTableRow
hwVoPeerConfigCallerPermitNumEntry=_HwVoPeerConfigCallerPermitNumEntry_Object((1,3,6,1,4,1,2011,5,25,1,5,1,5,1))
hwVoPeerConfigCallerPermitNumEntry.setIndexNames((0,_J,_V),(0,_J,_i))
if mibBuilder.loadTexts:hwVoPeerConfigCallerPermitNumEntry.setStatus(_A)
class _HwVoPeerConfigCallerPermitNum_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_HwVoPeerConfigCallerPermitNum_Type.__name__=_I
_HwVoPeerConfigCallerPermitNum_Object=MibTableColumn
hwVoPeerConfigCallerPermitNum=_HwVoPeerConfigCallerPermitNum_Object((1,3,6,1,4,1,2011,5,25,1,5,1,5,1,1),_HwVoPeerConfigCallerPermitNum_Type())
hwVoPeerConfigCallerPermitNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoPeerConfigCallerPermitNum.setStatus(_A)
_HwVoPeerConfigCallerPermitNumRowStatus_Type=EntryStatus
_HwVoPeerConfigCallerPermitNumRowStatus_Object=MibTableColumn
hwVoPeerConfigCallerPermitNumRowStatus=_HwVoPeerConfigCallerPermitNumRowStatus_Object((1,3,6,1,4,1,2011,5,25,1,5,1,5,1,2),_HwVoPeerConfigCallerPermitNumRowStatus_Type())
hwVoPeerConfigCallerPermitNumRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoPeerConfigCallerPermitNumRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_J,**{'EntryStatus':EntryStatus,'hwVoiceDialControlMIB':hwVoiceDialControlMIB,'hwVoPeerObjects':hwVoPeerObjects,'hwVoPeerCommonConfigTable':hwVoPeerCommonConfigTable,'hwVoPeerCommonConfigEntry':hwVoPeerCommonConfigEntry,_V:hwVoPeerConfigIndex,'hwVoPeerConfigType':hwVoPeerConfigType,'hwVoPeerConfigDesPattern':hwVoPeerConfigDesPattern,'hwVoPeerConfigCodec1st':hwVoPeerConfigCodec1st,'hwVoPeerConfigCodec2st':hwVoPeerConfigCodec2st,'hwVoPeerConfigCodec3st':hwVoPeerConfigCodec3st,'hwVoPeerConfigCodec4st':hwVoPeerConfigCodec4st,'hwVoPeerConfigIpPreced':hwVoPeerConfigIpPreced,'hwVoPeerConfigShutDown':hwVoPeerConfigShutDown,'hwVoPeerConfigVADSwitch':hwVoPeerConfigVADSwitch,'hwVoPeerConfigDtmfRelay':hwVoPeerConfigDtmfRelay,'hwVoPeerConfigFaxLevel':hwVoPeerConfigFaxLevel,'hwVoPeerConfigFaxRate':hwVoPeerConfigFaxRate,'hwVoPeerConfigFaxLocalTrainParam':hwVoPeerConfigFaxLocalTrainParam,'hwVoPeerConfigFaxProtocol':hwVoPeerConfigFaxProtocol,'hwVoPeerConfigFaxT38HighRedunPackNumber':hwVoPeerConfigFaxT38HighRedunPackNumber,'hwVoPeerConfigFaxT38LowRedunPackNumber':hwVoPeerConfigFaxT38LowRedunPackNumber,'hwVoPeerConfigFaxSendNSFSwitch':hwVoPeerConfigFaxSendNSFSwitch,'hwVoPeerConfigFaxSupportMode':hwVoPeerConfigFaxSupportMode,'hwVoPeerConfigFaxTrainMode':hwVoPeerConfigFaxTrainMode,'hwVoPeerConfigFaxRelay':hwVoPeerConfigFaxRelay,'hwVoPeerConfigRowStatus':hwVoPeerConfigRowStatus,'hwVoPeerConfigFaxPassthroughMode':hwVoPeerConfigFaxPassthroughMode,'hwVoPeerConfigPriority':hwVoPeerConfigPriority,'hwVoPeerConfigAuthorizationLevel':hwVoPeerConfigAuthorizationLevel,'hwVoPeerConfigDescription':hwVoPeerConfigDescription,'hwVoPeerConfigCallingNumberType':hwVoPeerConfigCallingNumberType,'hwVoPeerConfigCalledNumberType':hwVoPeerConfigCalledNumberType,'hwVoPeerConfigCallingNumberingPlan':hwVoPeerConfigCallingNumberingPlan,'hwVoPeerConfigCalledNumberingPlan':hwVoPeerConfigCalledNumberingPlan,'hwVoPeerConfigSelectStop':hwVoPeerConfigSelectStop,'hwVoPeerConfigCallingNumSubstRule':hwVoPeerConfigCallingNumSubstRule,'hwVoPeerConfigCalledNumSubstRule':hwVoPeerConfigCalledNumSubstRule,'hwVoPeerConfigMaxCall':hwVoPeerConfigMaxCall,'hwVoPOTSPeerConfigTable':hwVoPOTSPeerConfigTable,'hwVoPOTSPeerConfigEntry':hwVoPOTSPeerConfigEntry,_f:hwVoPOTSPeerConfigIndex,'hwVoPOTSPeerConfigCancelTruncateEnable':hwVoPOTSPeerConfigCancelTruncateEnable,'hwVoPOTSPeerConfigPrefix':hwVoPOTSPeerConfigPrefix,'hwVoPOTSPeerConfigPort':hwVoPOTSPeerConfigPort,'hwVoPOTSPeerConfigSendNumber':hwVoPOTSPeerConfigSendNumber,'hwVoVoIPPeerConfigTable':hwVoVoIPPeerConfigTable,'hwVoVoIPPeerConfigEntry':hwVoVoIPPeerConfigEntry,_h:hwVoVoIPPeerConfigIndex,'hwVoVoIPPeerConfigSessionTargetType':hwVoVoIPPeerConfigSessionTargetType,'hwVoVoIPPeerConfigSessionTarget':hwVoVoIPPeerConfigSessionTarget,'hwVoVoIPPeerConfigFastSwitch':hwVoVoIPPeerConfigFastSwitch,'hwVoVoIPPeerConfigTunnelSwitch':hwVoVoIPPeerConfigTunnelSwitch,'hwVoVoIPPeerConfigTeachPrefix':hwVoVoIPPeerConfigTeachPrefix,'hwVoVoIPPeerConfigSendRing':hwVoVoIPPeerConfigSendRing,'hwVoPeerDefaultConfigObjects':hwVoPeerDefaultConfigObjects,'hwVoPeerDefaultConfigCancelTrun':hwVoPeerDefaultConfigCancelTrun,'hwVoPeerDefaultConfig1STCodecLevel':hwVoPeerDefaultConfig1STCodecLevel,'hwVoPeerDefaultConfig2NDCodecLevel':hwVoPeerDefaultConfig2NDCodecLevel,'hwVoPeerDefaultConfig3RDCodecLevel':hwVoPeerDefaultConfig3RDCodecLevel,'hwVoPeerDefaultConfig4THCodecLevel':hwVoPeerDefaultConfig4THCodecLevel,'hwVoPeerDefaultConfigVADOn':hwVoPeerDefaultConfigVADOn,'hwVoPeerDefaultConfigFaxTransmitLevel':hwVoPeerDefaultConfigFaxTransmitLevel,'hwVoPeerDefaultConfigFaxLocalTrain':hwVoPeerDefaultConfigFaxLocalTrain,'hwVoPeerDefaultConfigFaxProtocol':hwVoPeerDefaultConfigFaxProtocol,'hwVoPeerDefaultConfigFaxHSRedundancy':hwVoPeerDefaultConfigFaxHSRedundancy,'hwVoPeerDefaultConfigFaxLSRedundancy':hwVoPeerDefaultConfigFaxLSRedundancy,'hwVoPeerDefaultConfigFaxBaudrate':hwVoPeerDefaultConfigFaxBaudrate,'hwVoPeerDefaultConfigFaxNSF':hwVoPeerDefaultConfigFaxNSF,'hwVoPeerDefaultConfigFaxSupportMode':hwVoPeerDefaultConfigFaxSupportMode,'hwVoPeerDefaultConfigFaxTrainMode':hwVoPeerDefaultConfigFaxTrainMode,'hwVoPeerDefaultConfigFaxECM':hwVoPeerDefaultConfigFaxECM,'hwVoPeerConfigCallerPermitNumTable':hwVoPeerConfigCallerPermitNumTable,'hwVoPeerConfigCallerPermitNumEntry':hwVoPeerConfigCallerPermitNumEntry,_i:hwVoPeerConfigCallerPermitNum,'hwVoPeerConfigCallerPermitNumRowStatus':hwVoPeerConfigCallerPermitNumRowStatus})