_AB='voiceIfDtmfTransportBasicGroupVer1'
_AA='voiceIfCodecGroupVer1'
_A9='voiceIfBasicGroupVer1'
_A8='voiceIfDtmfEnforceDefaultEvents'
_A7='voiceIfDtmfPayloadType'
_A6='voiceIfDtmfTransport'
_A5='voiceIfSignalLimiterLevel'
_A4='voiceIfG723VoiceActivityDetectionEnable'
_A3='voiceIfG729VoiceActivityDetectionEnable'
_A2='voiceIfNlpThresholdLevel'
_A1='voiceIfBaseOutputGainOffset'
_A0='voiceIfBaseInputGainOffset'
_z='voiceIfBaseOutputGain'
_y='voiceIfBaseInputGain'
_x='voiceIfUserOutputGainOffset'
_w='voiceIfUserInputGainOffset'
_v='voiceIfBaseGainConfigurationSource'
_u='voiceIfG711ComfortNoiseGenerationEnable'
_t='voiceIfEchoCancellationEnable'
_s='voiceIfG711VoiceActivityDetectionEnable'
_r='voiceIfMaxJitterBufferLength'
_q='voiceIfTargetJitterBufferLength'
_p='voiceIfAdaptativeJitterBufferEnable'
_o='voiceIfCodecG72640kbpsMaxPTime'
_n='voiceIfCodecG72640kbpsMinPTime'
_m='voiceIfCodecG72640kbpsPayloadType'
_l='voiceIfCodecG72640kbpsEnable'
_k='voiceIfCodecG72632kbpsMaxPTime'
_j='voiceIfCodecG72632kbpsMinPTime'
_i='voiceIfCodecG72632kbpsPayloadType'
_h='voiceIfCodecG72632kbpsEnable'
_g='voiceIfCodecG72624kbpsMaxPTime'
_f='voiceIfCodecG72624kbpsMinPTime'
_e='voiceIfCodecG72624kbpsPayloadType'
_d='voiceIfCodecG72624kbpsEnable'
_c='voiceIfCodecG72616kbpsMaxPTime'
_b='voiceIfCodecG72616kbpsMinPTime'
_a='voiceIfCodecG72616kbpsPayloadType'
_Z='voiceIfCodecG72616kbpsEnable'
_Y='voiceIfCodecG729MaxPTime'
_X='voiceIfCodecG729MinPTime'
_W='voiceIfCodecG729Enable'
_V='voiceIfCodecG723MaxPTime'
_U='voiceIfCodecG723MinPTime'
_T='voiceIfCodecG723Enable'
_S='voiceIfCodecPcmaMaxPTime'
_R='voiceIfCodecPcmaMinPTime'
_Q='voiceIfCodecPcmaEnable'
_P='voiceIfCodecPcmuMaxPTime'
_O='voiceIfCodecPcmuMinPTime'
_N='voiceIfCodecPcmuEnable'
_M='voiceIfCodecPreferred'
_L='MxFloatingPoint'
_K='ifIndex'
_J='IF-MIB'
_I='deprecated'
_H='MxEnableState'
_G='enable'
_F='disable'
_E='Integer32'
_D='Unsigned32'
_C='MX-VOICEIF-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_J,_K)
mediatrixConfig,=mibBuilder.importSymbols('MX-SMI','mediatrixConfig')
MxEnableState,MxFloatingPoint=mibBuilder.importSymbols('MX-TC',_H,_L)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
voiceIfMIB=ModuleIdentity((1,3,6,1,4,1,4935,15,30))
if mibBuilder.loadTexts:voiceIfMIB.setRevisions(('2009-08-31 00:00','2009-04-06 00:00','2009-04-01 00:00','2009-02-11 00:00','2008-11-07 00:00','2008-04-08 00:00','2007-10-10 00:00','2007-07-04 00:00','2006-03-06 00:00','2005-07-18 00:00','2005-03-17 00:00','2004-05-25 00:00','2004-04-13 00:00','2003-11-10 00:00','2003-08-12 00:00','2003-08-06 00:00','2003-07-24 00:00','2003-07-21 00:00','2003-06-20 00:00','2003-05-21 00:00','2003-05-01 00:00','2003-04-01 00:00','2003-02-11 00:00','2003-01-16 00:00','2002-12-19 00:00','2002-09-16 00:00','2002-08-30 00:00','2002-08-12 00:00','2002-07-31 00:00','2002-06-06 00:00','2002-04-26 00:00','2002-01-11 00:00','2001-08-22 00:00'))
_VoiceIfMIBObjects_ObjectIdentity=ObjectIdentity
voiceIfMIBObjects=_VoiceIfMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,15,30,1))
class _VoiceIfAllowDtmfOobRecovery_Type(MxEnableState):defaultValue=0
_VoiceIfAllowDtmfOobRecovery_Type.__name__=_H
_VoiceIfAllowDtmfOobRecovery_Object=MibScalar
voiceIfAllowDtmfOobRecovery=_VoiceIfAllowDtmfOobRecovery_Object((1,3,6,1,4,1,4935,15,30,1,5),_VoiceIfAllowDtmfOobRecovery_Type())
voiceIfAllowDtmfOobRecovery.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfAllowDtmfOobRecovery.setStatus(_A)
_VoiceIfTable_Object=MibTable
voiceIfTable=_VoiceIfTable_Object((1,3,6,1,4,1,4935,15,30,1,10))
if mibBuilder.loadTexts:voiceIfTable.setStatus(_A)
_VoiceIfEntry_Object=MibTableRow
voiceIfEntry=_VoiceIfEntry_Object((1,3,6,1,4,1,4935,15,30,1,10,1))
voiceIfEntry.setIndexNames((0,_J,_K))
if mibBuilder.loadTexts:voiceIfEntry.setStatus(_A)
class _VoiceIfAdaptativeJitterBufferEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_VoiceIfAdaptativeJitterBufferEnable_Type.__name__=_E
_VoiceIfAdaptativeJitterBufferEnable_Object=MibTableColumn
voiceIfAdaptativeJitterBufferEnable=_VoiceIfAdaptativeJitterBufferEnable_Object((1,3,6,1,4,1,4935,15,30,1,10,1,5),_VoiceIfAdaptativeJitterBufferEnable_Type())
voiceIfAdaptativeJitterBufferEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfAdaptativeJitterBufferEnable.setStatus(_A)
class _VoiceIfTargetJitterBufferLength_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,300))
_VoiceIfTargetJitterBufferLength_Type.__name__=_D
_VoiceIfTargetJitterBufferLength_Object=MibTableColumn
voiceIfTargetJitterBufferLength=_VoiceIfTargetJitterBufferLength_Object((1,3,6,1,4,1,4935,15,30,1,10,1,6),_VoiceIfTargetJitterBufferLength_Type())
voiceIfTargetJitterBufferLength.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfTargetJitterBufferLength.setStatus(_A)
class _VoiceIfMaxJitterBufferLength_Type(Unsigned32):defaultValue=125;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,300))
_VoiceIfMaxJitterBufferLength_Type.__name__=_D
_VoiceIfMaxJitterBufferLength_Object=MibTableColumn
voiceIfMaxJitterBufferLength=_VoiceIfMaxJitterBufferLength_Object((1,3,6,1,4,1,4935,15,30,1,10,1,7),_VoiceIfMaxJitterBufferLength_Type())
voiceIfMaxJitterBufferLength.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfMaxJitterBufferLength.setStatus(_A)
class _VoiceIfG711VoiceActivityDetectionEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),('transparent',1),('conservative',2)))
_VoiceIfG711VoiceActivityDetectionEnable_Type.__name__=_E
_VoiceIfG711VoiceActivityDetectionEnable_Object=MibTableColumn
voiceIfG711VoiceActivityDetectionEnable=_VoiceIfG711VoiceActivityDetectionEnable_Object((1,3,6,1,4,1,4935,15,30,1,10,1,10),_VoiceIfG711VoiceActivityDetectionEnable_Type())
voiceIfG711VoiceActivityDetectionEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfG711VoiceActivityDetectionEnable.setStatus(_A)
class _VoiceIfEchoCancellationEnable_Type(MxEnableState):defaultValue=1
_VoiceIfEchoCancellationEnable_Type.__name__=_H
_VoiceIfEchoCancellationEnable_Object=MibTableColumn
voiceIfEchoCancellationEnable=_VoiceIfEchoCancellationEnable_Object((1,3,6,1,4,1,4935,15,30,1,10,1,11),_VoiceIfEchoCancellationEnable_Type())
voiceIfEchoCancellationEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfEchoCancellationEnable.setStatus(_A)
class _VoiceIfG711ComfortNoiseGenerationEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),('whiteNoise',1),('customNoise',2)))
_VoiceIfG711ComfortNoiseGenerationEnable_Type.__name__=_E
_VoiceIfG711ComfortNoiseGenerationEnable_Object=MibTableColumn
voiceIfG711ComfortNoiseGenerationEnable=_VoiceIfG711ComfortNoiseGenerationEnable_Object((1,3,6,1,4,1,4935,15,30,1,10,1,12),_VoiceIfG711ComfortNoiseGenerationEnable_Type())
voiceIfG711ComfortNoiseGenerationEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfG711ComfortNoiseGenerationEnable.setStatus(_A)
class _VoiceIfBaseGainConfigurationSource_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('useCustomConfiguration',0),('useDefaultCountryConfiguration',1)))
_VoiceIfBaseGainConfigurationSource_Type.__name__=_E
_VoiceIfBaseGainConfigurationSource_Object=MibTableColumn
voiceIfBaseGainConfigurationSource=_VoiceIfBaseGainConfigurationSource_Object((1,3,6,1,4,1,4935,15,30,1,10,1,17),_VoiceIfBaseGainConfigurationSource_Type())
voiceIfBaseGainConfigurationSource.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfBaseGainConfigurationSource.setStatus(_I)
class _VoiceIfUserInputGainOffset_Type(MxFloatingPoint):defaultValue=OctetString('0')
_VoiceIfUserInputGainOffset_Type.__name__=_L
_VoiceIfUserInputGainOffset_Object=MibTableColumn
voiceIfUserInputGainOffset=_VoiceIfUserInputGainOffset_Object((1,3,6,1,4,1,4935,15,30,1,10,1,20),_VoiceIfUserInputGainOffset_Type())
voiceIfUserInputGainOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfUserInputGainOffset.setStatus(_A)
class _VoiceIfUserOutputGainOffset_Type(MxFloatingPoint):defaultValue=OctetString('0')
_VoiceIfUserOutputGainOffset_Type.__name__=_L
_VoiceIfUserOutputGainOffset_Object=MibTableColumn
voiceIfUserOutputGainOffset=_VoiceIfUserOutputGainOffset_Object((1,3,6,1,4,1,4935,15,30,1,10,1,21),_VoiceIfUserOutputGainOffset_Type())
voiceIfUserOutputGainOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfUserOutputGainOffset.setStatus(_A)
class _VoiceIfBaseInputGain_Type(Unsigned32):defaultValue=5785;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_VoiceIfBaseInputGain_Type.__name__=_D
_VoiceIfBaseInputGain_Object=MibTableColumn
voiceIfBaseInputGain=_VoiceIfBaseInputGain_Object((1,3,6,1,4,1,4935,15,30,1,10,1,22),_VoiceIfBaseInputGain_Type())
voiceIfBaseInputGain.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfBaseInputGain.setStatus(_I)
class _VoiceIfBaseOutputGain_Type(Unsigned32):defaultValue=2052;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_VoiceIfBaseOutputGain_Type.__name__=_D
_VoiceIfBaseOutputGain_Object=MibTableColumn
voiceIfBaseOutputGain=_VoiceIfBaseOutputGain_Object((1,3,6,1,4,1,4935,15,30,1,10,1,23),_VoiceIfBaseOutputGain_Type())
voiceIfBaseOutputGain.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfBaseOutputGain.setStatus(_I)
class _VoiceIfBaseInputGainOffset_Type(MxFloatingPoint):defaultValue=OctetString('0')
_VoiceIfBaseInputGainOffset_Type.__name__=_L
_VoiceIfBaseInputGainOffset_Object=MibTableColumn
voiceIfBaseInputGainOffset=_VoiceIfBaseInputGainOffset_Object((1,3,6,1,4,1,4935,15,30,1,10,1,24),_VoiceIfBaseInputGainOffset_Type())
voiceIfBaseInputGainOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfBaseInputGainOffset.setStatus(_I)
class _VoiceIfBaseOutputGainOffset_Type(MxFloatingPoint):defaultValue=OctetString('0')
_VoiceIfBaseOutputGainOffset_Type.__name__=_L
_VoiceIfBaseOutputGainOffset_Object=MibTableColumn
voiceIfBaseOutputGainOffset=_VoiceIfBaseOutputGainOffset_Object((1,3,6,1,4,1,4935,15,30,1,10,1,25),_VoiceIfBaseOutputGainOffset_Type())
voiceIfBaseOutputGainOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfBaseOutputGainOffset.setStatus(_I)
class _VoiceIfNlpThresholdLevel_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_VoiceIfNlpThresholdLevel_Type.__name__=_D
_VoiceIfNlpThresholdLevel_Object=MibTableColumn
voiceIfNlpThresholdLevel=_VoiceIfNlpThresholdLevel_Object((1,3,6,1,4,1,4935,15,30,1,10,1,35),_VoiceIfNlpThresholdLevel_Type())
voiceIfNlpThresholdLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfNlpThresholdLevel.setStatus(_I)
class _VoiceIfG729VoiceActivityDetectionEnable_Type(MxEnableState):defaultValue=1
_VoiceIfG729VoiceActivityDetectionEnable_Type.__name__=_H
_VoiceIfG729VoiceActivityDetectionEnable_Object=MibTableColumn
voiceIfG729VoiceActivityDetectionEnable=_VoiceIfG729VoiceActivityDetectionEnable_Object((1,3,6,1,4,1,4935,15,30,1,10,1,50),_VoiceIfG729VoiceActivityDetectionEnable_Type())
voiceIfG729VoiceActivityDetectionEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfG729VoiceActivityDetectionEnable.setStatus(_A)
class _VoiceIfG723VoiceActivityDetectionEnable_Type(MxEnableState):defaultValue=1
_VoiceIfG723VoiceActivityDetectionEnable_Type.__name__=_H
_VoiceIfG723VoiceActivityDetectionEnable_Object=MibTableColumn
voiceIfG723VoiceActivityDetectionEnable=_VoiceIfG723VoiceActivityDetectionEnable_Object((1,3,6,1,4,1,4935,15,30,1,10,1,80),_VoiceIfG723VoiceActivityDetectionEnable_Type())
voiceIfG723VoiceActivityDetectionEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfG723VoiceActivityDetectionEnable.setStatus(_A)
class _VoiceIfSignalLimiterLevel_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_VoiceIfSignalLimiterLevel_Type.__name__=_E
_VoiceIfSignalLimiterLevel_Object=MibTableColumn
voiceIfSignalLimiterLevel=_VoiceIfSignalLimiterLevel_Object((1,3,6,1,4,1,4935,15,30,1,10,1,90),_VoiceIfSignalLimiterLevel_Type())
voiceIfSignalLimiterLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfSignalLimiterLevel.setStatus(_A)
_VoiceIfCodecTable_Object=MibTable
voiceIfCodecTable=_VoiceIfCodecTable_Object((1,3,6,1,4,1,4935,15,30,1,20))
if mibBuilder.loadTexts:voiceIfCodecTable.setStatus(_A)
_VoiceIfCodecEntry_Object=MibTableRow
voiceIfCodecEntry=_VoiceIfCodecEntry_Object((1,3,6,1,4,1,4935,15,30,1,20,1))
voiceIfCodecEntry.setIndexNames((0,_J,_K))
if mibBuilder.loadTexts:voiceIfCodecEntry.setStatus(_A)
class _VoiceIfCodecPreferred_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('pcmu',1),('pcma',2),('g723',3),('g729',4),('g726-16kbps',5),('g726-24kbps',6),('g726-32kbps',7),('g726-40kbps',8)))
_VoiceIfCodecPreferred_Type.__name__=_E
_VoiceIfCodecPreferred_Object=MibTableColumn
voiceIfCodecPreferred=_VoiceIfCodecPreferred_Object((1,3,6,1,4,1,4935,15,30,1,20,1,1),_VoiceIfCodecPreferred_Type())
voiceIfCodecPreferred.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfCodecPreferred.setStatus(_A)
class _VoiceIfCodecPcmuEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_VoiceIfCodecPcmuEnable_Type.__name__=_E
_VoiceIfCodecPcmuEnable_Object=MibTableColumn
voiceIfCodecPcmuEnable=_VoiceIfCodecPcmuEnable_Object((1,3,6,1,4,1,4935,15,30,1,20,1,5),_VoiceIfCodecPcmuEnable_Type())
voiceIfCodecPcmuEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfCodecPcmuEnable.setStatus(_A)
class _VoiceIfCodecPcmuMinPTime_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,10),ValueRangeConstraint(20,20),ValueRangeConstraint(30,30),ValueRangeConstraint(40,40),ValueRangeConstraint(50,50),ValueRangeConstraint(60,60),ValueRangeConstraint(70,70),ValueRangeConstraint(80,80),ValueRangeConstraint(90,90),ValueRangeConstraint(100,100))
_VoiceIfCodecPcmuMinPTime_Type.__name__=_D
_VoiceIfCodecPcmuMinPTime_Object=MibTableColumn
voiceIfCodecPcmuMinPTime=_VoiceIfCodecPcmuMinPTime_Object((1,3,6,1,4,1,4935,15,30,1,20,1,6),_VoiceIfCodecPcmuMinPTime_Type())
voiceIfCodecPcmuMinPTime.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfCodecPcmuMinPTime.setStatus(_A)
class _VoiceIfCodecPcmuMaxPTime_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,10),ValueRangeConstraint(20,20),ValueRangeConstraint(30,30),ValueRangeConstraint(40,40),ValueRangeConstraint(50,50),ValueRangeConstraint(60,60),ValueRangeConstraint(70,70),ValueRangeConstraint(80,80),ValueRangeConstraint(90,90),ValueRangeConstraint(100,100))
_VoiceIfCodecPcmuMaxPTime_Type.__name__=_D
_VoiceIfCodecPcmuMaxPTime_Object=MibTableColumn
voiceIfCodecPcmuMaxPTime=_VoiceIfCodecPcmuMaxPTime_Object((1,3,6,1,4,1,4935,15,30,1,20,1,7),_VoiceIfCodecPcmuMaxPTime_Type())
voiceIfCodecPcmuMaxPTime.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfCodecPcmuMaxPTime.setStatus(_A)
class _VoiceIfCodecPcmaEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_VoiceIfCodecPcmaEnable_Type.__name__=_E
_VoiceIfCodecPcmaEnable_Object=MibTableColumn
voiceIfCodecPcmaEnable=_VoiceIfCodecPcmaEnable_Object((1,3,6,1,4,1,4935,15,30,1,20,1,11),_VoiceIfCodecPcmaEnable_Type())
voiceIfCodecPcmaEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfCodecPcmaEnable.setStatus(_A)
class _VoiceIfCodecPcmaMinPTime_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,10),ValueRangeConstraint(20,20),ValueRangeConstraint(30,30),ValueRangeConstraint(40,40),ValueRangeConstraint(50,50),ValueRangeConstraint(60,60),ValueRangeConstraint(70,70),ValueRangeConstraint(80,80),ValueRangeConstraint(90,90),ValueRangeConstraint(100,100))
_VoiceIfCodecPcmaMinPTime_Type.__name__=_D
_VoiceIfCodecPcmaMinPTime_Object=MibTableColumn
voiceIfCodecPcmaMinPTime=_VoiceIfCodecPcmaMinPTime_Object((1,3,6,1,4,1,4935,15,30,1,20,1,12),_VoiceIfCodecPcmaMinPTime_Type())
voiceIfCodecPcmaMinPTime.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfCodecPcmaMinPTime.setStatus(_A)
class _VoiceIfCodecPcmaMaxPTime_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,10),ValueRangeConstraint(20,20),ValueRangeConstraint(30,30),ValueRangeConstraint(40,40),ValueRangeConstraint(50,50),ValueRangeConstraint(60,60),ValueRangeConstraint(70,70),ValueRangeConstraint(80,80),ValueRangeConstraint(90,90),ValueRangeConstraint(100,100))
_VoiceIfCodecPcmaMaxPTime_Type.__name__=_D
_VoiceIfCodecPcmaMaxPTime_Object=MibTableColumn
voiceIfCodecPcmaMaxPTime=_VoiceIfCodecPcmaMaxPTime_Object((1,3,6,1,4,1,4935,15,30,1,20,1,13),_VoiceIfCodecPcmaMaxPTime_Type())
voiceIfCodecPcmaMaxPTime.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfCodecPcmaMaxPTime.setStatus(_A)
class _VoiceIfCodecG723Enable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),('g723-53kbs',1),('g723-63kbs',2)))
_VoiceIfCodecG723Enable_Type.__name__=_E
_VoiceIfCodecG723Enable_Object=MibTableColumn
voiceIfCodecG723Enable=_VoiceIfCodecG723Enable_Object((1,3,6,1,4,1,4935,15,30,1,20,1,17),_VoiceIfCodecG723Enable_Type())
voiceIfCodecG723Enable.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfCodecG723Enable.setStatus(_A)
class _VoiceIfCodecG723MinPTime_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,30),ValueRangeConstraint(60,60),ValueRangeConstraint(90,90),ValueRangeConstraint(120,120))
_VoiceIfCodecG723MinPTime_Type.__name__=_D
_VoiceIfCodecG723MinPTime_Object=MibTableColumn
voiceIfCodecG723MinPTime=_VoiceIfCodecG723MinPTime_Object((1,3,6,1,4,1,4935,15,30,1,20,1,18),_VoiceIfCodecG723MinPTime_Type())
voiceIfCodecG723MinPTime.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfCodecG723MinPTime.setStatus(_A)
class _VoiceIfCodecG723MaxPTime_Type(Unsigned32):defaultValue=120;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,30),ValueRangeConstraint(60,60),ValueRangeConstraint(90,90),ValueRangeConstraint(120,120))
_VoiceIfCodecG723MaxPTime_Type.__name__=_D
_VoiceIfCodecG723MaxPTime_Object=MibTableColumn
voiceIfCodecG723MaxPTime=_VoiceIfCodecG723MaxPTime_Object((1,3,6,1,4,1,4935,15,30,1,20,1,19),_VoiceIfCodecG723MaxPTime_Type())
voiceIfCodecG723MaxPTime.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfCodecG723MaxPTime.setStatus(_A)
class _VoiceIfCodecG729Enable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_VoiceIfCodecG729Enable_Type.__name__=_E
_VoiceIfCodecG729Enable_Object=MibTableColumn
voiceIfCodecG729Enable=_VoiceIfCodecG729Enable_Object((1,3,6,1,4,1,4935,15,30,1,20,1,23),_VoiceIfCodecG729Enable_Type())
voiceIfCodecG729Enable.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfCodecG729Enable.setStatus(_A)
class _VoiceIfCodecG729MinPTime_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,10),ValueRangeConstraint(20,20),ValueRangeConstraint(30,30),ValueRangeConstraint(40,40),ValueRangeConstraint(50,50),ValueRangeConstraint(60,60),ValueRangeConstraint(70,70),ValueRangeConstraint(80,80),ValueRangeConstraint(90,90),ValueRangeConstraint(100,100))
_VoiceIfCodecG729MinPTime_Type.__name__=_D
_VoiceIfCodecG729MinPTime_Object=MibTableColumn
voiceIfCodecG729MinPTime=_VoiceIfCodecG729MinPTime_Object((1,3,6,1,4,1,4935,15,30,1,20,1,24),_VoiceIfCodecG729MinPTime_Type())
voiceIfCodecG729MinPTime.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfCodecG729MinPTime.setStatus(_A)
class _VoiceIfCodecG729MaxPTime_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,10),ValueRangeConstraint(20,20),ValueRangeConstraint(30,30),ValueRangeConstraint(40,40),ValueRangeConstraint(50,50),ValueRangeConstraint(60,60),ValueRangeConstraint(70,70),ValueRangeConstraint(80,80),ValueRangeConstraint(90,90),ValueRangeConstraint(100,100))
_VoiceIfCodecG729MaxPTime_Type.__name__=_D
_VoiceIfCodecG729MaxPTime_Object=MibTableColumn
voiceIfCodecG729MaxPTime=_VoiceIfCodecG729MaxPTime_Object((1,3,6,1,4,1,4935,15,30,1,20,1,25),_VoiceIfCodecG729MaxPTime_Type())
voiceIfCodecG729MaxPTime.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfCodecG729MaxPTime.setStatus(_A)
class _VoiceIfCodecG72616kbpsEnable_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_VoiceIfCodecG72616kbpsEnable_Type.__name__=_E
_VoiceIfCodecG72616kbpsEnable_Object=MibTableColumn
voiceIfCodecG72616kbpsEnable=_VoiceIfCodecG72616kbpsEnable_Object((1,3,6,1,4,1,4935,15,30,1,20,1,50),_VoiceIfCodecG72616kbpsEnable_Type())
voiceIfCodecG72616kbpsEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfCodecG72616kbpsEnable.setStatus(_A)
class _VoiceIfCodecG72616kbpsPayloadType_Type(Unsigned32):defaultValue=97;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(96,127))
_VoiceIfCodecG72616kbpsPayloadType_Type.__name__=_D
_VoiceIfCodecG72616kbpsPayloadType_Object=MibTableColumn
voiceIfCodecG72616kbpsPayloadType=_VoiceIfCodecG72616kbpsPayloadType_Object((1,3,6,1,4,1,4935,15,30,1,20,1,55),_VoiceIfCodecG72616kbpsPayloadType_Type())
voiceIfCodecG72616kbpsPayloadType.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfCodecG72616kbpsPayloadType.setStatus(_A)
class _VoiceIfCodecG72616kbpsMinPTime_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,10),ValueRangeConstraint(20,20),ValueRangeConstraint(30,30),ValueRangeConstraint(40,40),ValueRangeConstraint(50,50),ValueRangeConstraint(60,60),ValueRangeConstraint(70,70),ValueRangeConstraint(80,80),ValueRangeConstraint(90,90),ValueRangeConstraint(100,100))
_VoiceIfCodecG72616kbpsMinPTime_Type.__name__=_D
_VoiceIfCodecG72616kbpsMinPTime_Object=MibTableColumn
voiceIfCodecG72616kbpsMinPTime=_VoiceIfCodecG72616kbpsMinPTime_Object((1,3,6,1,4,1,4935,15,30,1,20,1,60),_VoiceIfCodecG72616kbpsMinPTime_Type())
voiceIfCodecG72616kbpsMinPTime.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfCodecG72616kbpsMinPTime.setStatus(_A)
class _VoiceIfCodecG72616kbpsMaxPTime_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,10),ValueRangeConstraint(20,20),ValueRangeConstraint(30,30),ValueRangeConstraint(40,40),ValueRangeConstraint(50,50),ValueRangeConstraint(60,60),ValueRangeConstraint(70,70),ValueRangeConstraint(80,80),ValueRangeConstraint(90,90),ValueRangeConstraint(100,100))
_VoiceIfCodecG72616kbpsMaxPTime_Type.__name__=_D
_VoiceIfCodecG72616kbpsMaxPTime_Object=MibTableColumn
voiceIfCodecG72616kbpsMaxPTime=_VoiceIfCodecG72616kbpsMaxPTime_Object((1,3,6,1,4,1,4935,15,30,1,20,1,65),_VoiceIfCodecG72616kbpsMaxPTime_Type())
voiceIfCodecG72616kbpsMaxPTime.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfCodecG72616kbpsMaxPTime.setStatus(_A)
class _VoiceIfCodecG72624kbpsEnable_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_VoiceIfCodecG72624kbpsEnable_Type.__name__=_E
_VoiceIfCodecG72624kbpsEnable_Object=MibTableColumn
voiceIfCodecG72624kbpsEnable=_VoiceIfCodecG72624kbpsEnable_Object((1,3,6,1,4,1,4935,15,30,1,20,1,70),_VoiceIfCodecG72624kbpsEnable_Type())
voiceIfCodecG72624kbpsEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfCodecG72624kbpsEnable.setStatus(_A)
class _VoiceIfCodecG72624kbpsPayloadType_Type(Unsigned32):defaultValue=98;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(96,127))
_VoiceIfCodecG72624kbpsPayloadType_Type.__name__=_D
_VoiceIfCodecG72624kbpsPayloadType_Object=MibTableColumn
voiceIfCodecG72624kbpsPayloadType=_VoiceIfCodecG72624kbpsPayloadType_Object((1,3,6,1,4,1,4935,15,30,1,20,1,75),_VoiceIfCodecG72624kbpsPayloadType_Type())
voiceIfCodecG72624kbpsPayloadType.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfCodecG72624kbpsPayloadType.setStatus(_A)
class _VoiceIfCodecG72624kbpsMinPTime_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,10),ValueRangeConstraint(20,20),ValueRangeConstraint(30,30),ValueRangeConstraint(40,40),ValueRangeConstraint(50,50),ValueRangeConstraint(60,60),ValueRangeConstraint(70,70),ValueRangeConstraint(80,80),ValueRangeConstraint(90,90),ValueRangeConstraint(100,100))
_VoiceIfCodecG72624kbpsMinPTime_Type.__name__=_D
_VoiceIfCodecG72624kbpsMinPTime_Object=MibTableColumn
voiceIfCodecG72624kbpsMinPTime=_VoiceIfCodecG72624kbpsMinPTime_Object((1,3,6,1,4,1,4935,15,30,1,20,1,80),_VoiceIfCodecG72624kbpsMinPTime_Type())
voiceIfCodecG72624kbpsMinPTime.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfCodecG72624kbpsMinPTime.setStatus(_A)
class _VoiceIfCodecG72624kbpsMaxPTime_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,10),ValueRangeConstraint(20,20),ValueRangeConstraint(30,30),ValueRangeConstraint(40,40),ValueRangeConstraint(50,50),ValueRangeConstraint(60,60),ValueRangeConstraint(70,70),ValueRangeConstraint(80,80),ValueRangeConstraint(90,90),ValueRangeConstraint(100,100))
_VoiceIfCodecG72624kbpsMaxPTime_Type.__name__=_D
_VoiceIfCodecG72624kbpsMaxPTime_Object=MibTableColumn
voiceIfCodecG72624kbpsMaxPTime=_VoiceIfCodecG72624kbpsMaxPTime_Object((1,3,6,1,4,1,4935,15,30,1,20,1,85),_VoiceIfCodecG72624kbpsMaxPTime_Type())
voiceIfCodecG72624kbpsMaxPTime.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfCodecG72624kbpsMaxPTime.setStatus(_A)
class _VoiceIfCodecG72632kbpsEnable_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_VoiceIfCodecG72632kbpsEnable_Type.__name__=_E
_VoiceIfCodecG72632kbpsEnable_Object=MibTableColumn
voiceIfCodecG72632kbpsEnable=_VoiceIfCodecG72632kbpsEnable_Object((1,3,6,1,4,1,4935,15,30,1,20,1,90),_VoiceIfCodecG72632kbpsEnable_Type())
voiceIfCodecG72632kbpsEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfCodecG72632kbpsEnable.setStatus(_A)
class _VoiceIfCodecG72632kbpsPayloadType_Type(Unsigned32):defaultValue=99;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(96,127))
_VoiceIfCodecG72632kbpsPayloadType_Type.__name__=_D
_VoiceIfCodecG72632kbpsPayloadType_Object=MibTableColumn
voiceIfCodecG72632kbpsPayloadType=_VoiceIfCodecG72632kbpsPayloadType_Object((1,3,6,1,4,1,4935,15,30,1,20,1,100),_VoiceIfCodecG72632kbpsPayloadType_Type())
voiceIfCodecG72632kbpsPayloadType.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfCodecG72632kbpsPayloadType.setStatus(_A)
class _VoiceIfCodecG72632kbpsMinPTime_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,10),ValueRangeConstraint(20,20),ValueRangeConstraint(30,30),ValueRangeConstraint(40,40),ValueRangeConstraint(50,50),ValueRangeConstraint(60,60),ValueRangeConstraint(70,70),ValueRangeConstraint(80,80),ValueRangeConstraint(90,90),ValueRangeConstraint(100,100))
_VoiceIfCodecG72632kbpsMinPTime_Type.__name__=_D
_VoiceIfCodecG72632kbpsMinPTime_Object=MibTableColumn
voiceIfCodecG72632kbpsMinPTime=_VoiceIfCodecG72632kbpsMinPTime_Object((1,3,6,1,4,1,4935,15,30,1,20,1,105),_VoiceIfCodecG72632kbpsMinPTime_Type())
voiceIfCodecG72632kbpsMinPTime.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfCodecG72632kbpsMinPTime.setStatus(_A)
class _VoiceIfCodecG72632kbpsMaxPTime_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,10),ValueRangeConstraint(20,20),ValueRangeConstraint(30,30),ValueRangeConstraint(40,40),ValueRangeConstraint(50,50),ValueRangeConstraint(60,60),ValueRangeConstraint(70,70),ValueRangeConstraint(80,80),ValueRangeConstraint(90,90),ValueRangeConstraint(100,100))
_VoiceIfCodecG72632kbpsMaxPTime_Type.__name__=_D
_VoiceIfCodecG72632kbpsMaxPTime_Object=MibTableColumn
voiceIfCodecG72632kbpsMaxPTime=_VoiceIfCodecG72632kbpsMaxPTime_Object((1,3,6,1,4,1,4935,15,30,1,20,1,110),_VoiceIfCodecG72632kbpsMaxPTime_Type())
voiceIfCodecG72632kbpsMaxPTime.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfCodecG72632kbpsMaxPTime.setStatus(_A)
class _VoiceIfCodecG72640kbpsEnable_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_VoiceIfCodecG72640kbpsEnable_Type.__name__=_E
_VoiceIfCodecG72640kbpsEnable_Object=MibTableColumn
voiceIfCodecG72640kbpsEnable=_VoiceIfCodecG72640kbpsEnable_Object((1,3,6,1,4,1,4935,15,30,1,20,1,115),_VoiceIfCodecG72640kbpsEnable_Type())
voiceIfCodecG72640kbpsEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfCodecG72640kbpsEnable.setStatus(_A)
class _VoiceIfCodecG72640kbpsPayloadType_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(96,127))
_VoiceIfCodecG72640kbpsPayloadType_Type.__name__=_D
_VoiceIfCodecG72640kbpsPayloadType_Object=MibTableColumn
voiceIfCodecG72640kbpsPayloadType=_VoiceIfCodecG72640kbpsPayloadType_Object((1,3,6,1,4,1,4935,15,30,1,20,1,120),_VoiceIfCodecG72640kbpsPayloadType_Type())
voiceIfCodecG72640kbpsPayloadType.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfCodecG72640kbpsPayloadType.setStatus(_A)
class _VoiceIfCodecG72640kbpsMinPTime_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,10),ValueRangeConstraint(20,20),ValueRangeConstraint(30,30),ValueRangeConstraint(40,40),ValueRangeConstraint(50,50),ValueRangeConstraint(60,60),ValueRangeConstraint(70,70),ValueRangeConstraint(80,80),ValueRangeConstraint(90,90),ValueRangeConstraint(100,100))
_VoiceIfCodecG72640kbpsMinPTime_Type.__name__=_D
_VoiceIfCodecG72640kbpsMinPTime_Object=MibTableColumn
voiceIfCodecG72640kbpsMinPTime=_VoiceIfCodecG72640kbpsMinPTime_Object((1,3,6,1,4,1,4935,15,30,1,20,1,125),_VoiceIfCodecG72640kbpsMinPTime_Type())
voiceIfCodecG72640kbpsMinPTime.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfCodecG72640kbpsMinPTime.setStatus(_A)
class _VoiceIfCodecG72640kbpsMaxPTime_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,10),ValueRangeConstraint(20,20),ValueRangeConstraint(30,30),ValueRangeConstraint(40,40),ValueRangeConstraint(50,50),ValueRangeConstraint(60,60),ValueRangeConstraint(70,70),ValueRangeConstraint(80,80),ValueRangeConstraint(90,90),ValueRangeConstraint(100,100))
_VoiceIfCodecG72640kbpsMaxPTime_Type.__name__=_D
_VoiceIfCodecG72640kbpsMaxPTime_Object=MibTableColumn
voiceIfCodecG72640kbpsMaxPTime=_VoiceIfCodecG72640kbpsMaxPTime_Object((1,3,6,1,4,1,4935,15,30,1,20,1,130),_VoiceIfCodecG72640kbpsMaxPTime_Type())
voiceIfCodecG72640kbpsMaxPTime.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfCodecG72640kbpsMaxPTime.setStatus(_A)
_VoiceIfDtmfTransportTable_Object=MibTable
voiceIfDtmfTransportTable=_VoiceIfDtmfTransportTable_Object((1,3,6,1,4,1,4935,15,30,1,30))
if mibBuilder.loadTexts:voiceIfDtmfTransportTable.setStatus(_A)
_VoiceIfDtmfTransportEntry_Object=MibTableRow
voiceIfDtmfTransportEntry=_VoiceIfDtmfTransportEntry_Object((1,3,6,1,4,1,4935,15,30,1,30,1))
voiceIfDtmfTransportEntry.setIndexNames((0,_J,_K))
if mibBuilder.loadTexts:voiceIfDtmfTransportEntry.setStatus(_A)
class _VoiceIfDtmfTransport_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('inBand',0),('outOfBandUsingRtp',1),('outOfBandUsingSignalingProtocol',2),('signalingProtocolDependent',3)))
_VoiceIfDtmfTransport_Type.__name__=_E
_VoiceIfDtmfTransport_Object=MibTableColumn
voiceIfDtmfTransport=_VoiceIfDtmfTransport_Object((1,3,6,1,4,1,4935,15,30,1,30,1,1),_VoiceIfDtmfTransport_Type())
voiceIfDtmfTransport.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfDtmfTransport.setStatus(_A)
class _VoiceIfDtmfPayloadType_Type(Unsigned32):defaultValue=96;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(96,127))
_VoiceIfDtmfPayloadType_Type.__name__=_D
_VoiceIfDtmfPayloadType_Object=MibTableColumn
voiceIfDtmfPayloadType=_VoiceIfDtmfPayloadType_Object((1,3,6,1,4,1,4935,15,30,1,30,1,5),_VoiceIfDtmfPayloadType_Type())
voiceIfDtmfPayloadType.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfDtmfPayloadType.setStatus(_A)
class _VoiceIfDtmfEnforceDefaultEvents_Type(MxEnableState):defaultValue=1
_VoiceIfDtmfEnforceDefaultEvents_Type.__name__=_H
_VoiceIfDtmfEnforceDefaultEvents_Object=MibTableColumn
voiceIfDtmfEnforceDefaultEvents=_VoiceIfDtmfEnforceDefaultEvents_Object((1,3,6,1,4,1,4935,15,30,1,30,1,55),_VoiceIfDtmfEnforceDefaultEvents_Type())
voiceIfDtmfEnforceDefaultEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfDtmfEnforceDefaultEvents.setStatus(_A)
_VoiceIfDtmfDetectionTable_Object=MibTable
voiceIfDtmfDetectionTable=_VoiceIfDtmfDetectionTable_Object((1,3,6,1,4,1,4935,15,30,1,40))
if mibBuilder.loadTexts:voiceIfDtmfDetectionTable.setStatus(_A)
_VoiceIfDtmfDetectionEntry_Object=MibTableRow
voiceIfDtmfDetectionEntry=_VoiceIfDtmfDetectionEntry_Object((1,3,6,1,4,1,4935,15,30,1,40,1))
voiceIfDtmfDetectionEntry.setIndexNames((0,_J,_K))
if mibBuilder.loadTexts:voiceIfDtmfDetectionEntry.setStatus(_A)
class _VoiceIfDtmfDetectionRiseTimeCriteria_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('checkSr',100),('confirmSnr',200)))
_VoiceIfDtmfDetectionRiseTimeCriteria_Type.__name__=_E
_VoiceIfDtmfDetectionRiseTimeCriteria_Object=MibTableColumn
voiceIfDtmfDetectionRiseTimeCriteria=_VoiceIfDtmfDetectionRiseTimeCriteria_Object((1,3,6,1,4,1,4935,15,30,1,40,1,10),_VoiceIfDtmfDetectionRiseTimeCriteria_Type())
voiceIfDtmfDetectionRiseTimeCriteria.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfDtmfDetectionRiseTimeCriteria.setStatus(_A)
class _VoiceIfDtmfDetectionMaxPowerThreshold_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-20,1))
_VoiceIfDtmfDetectionMaxPowerThreshold_Type.__name__=_E
_VoiceIfDtmfDetectionMaxPowerThreshold_Object=MibTableColumn
voiceIfDtmfDetectionMaxPowerThreshold=_VoiceIfDtmfDetectionMaxPowerThreshold_Object((1,3,6,1,4,1,4935,15,30,1,40,1,20),_VoiceIfDtmfDetectionMaxPowerThreshold_Type())
voiceIfDtmfDetectionMaxPowerThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfDtmfDetectionMaxPowerThreshold.setStatus(_A)
class _VoiceIfDtmfDetectionMinPowerThreshold_Type(Integer32):defaultValue=-30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-45,-10))
_VoiceIfDtmfDetectionMinPowerThreshold_Type.__name__=_E
_VoiceIfDtmfDetectionMinPowerThreshold_Object=MibTableColumn
voiceIfDtmfDetectionMinPowerThreshold=_VoiceIfDtmfDetectionMinPowerThreshold_Object((1,3,6,1,4,1,4935,15,30,1,40,1,30),_VoiceIfDtmfDetectionMinPowerThreshold_Type())
voiceIfDtmfDetectionMinPowerThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfDtmfDetectionMinPowerThreshold.setStatus(_A)
class _VoiceIfDtmfDetectionBreakPowerThreshold_Type(Integer32):defaultValue=-32;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-45,-12))
_VoiceIfDtmfDetectionBreakPowerThreshold_Type.__name__=_E
_VoiceIfDtmfDetectionBreakPowerThreshold_Object=MibTableColumn
voiceIfDtmfDetectionBreakPowerThreshold=_VoiceIfDtmfDetectionBreakPowerThreshold_Object((1,3,6,1,4,1,4935,15,30,1,40,1,40),_VoiceIfDtmfDetectionBreakPowerThreshold_Type())
voiceIfDtmfDetectionBreakPowerThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfDtmfDetectionBreakPowerThreshold.setStatus(_A)
class _VoiceIfDtmfDetectionPositiveTwist_Type(Unsigned32):defaultValue=6;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_VoiceIfDtmfDetectionPositiveTwist_Type.__name__=_D
_VoiceIfDtmfDetectionPositiveTwist_Object=MibTableColumn
voiceIfDtmfDetectionPositiveTwist=_VoiceIfDtmfDetectionPositiveTwist_Object((1,3,6,1,4,1,4935,15,30,1,40,1,50),_VoiceIfDtmfDetectionPositiveTwist_Type())
voiceIfDtmfDetectionPositiveTwist.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfDtmfDetectionPositiveTwist.setStatus(_A)
class _VoiceIfDtmfDetectionNegativeTwist_Type(Unsigned32):defaultValue=9;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_VoiceIfDtmfDetectionNegativeTwist_Type.__name__=_D
_VoiceIfDtmfDetectionNegativeTwist_Object=MibTableColumn
voiceIfDtmfDetectionNegativeTwist=_VoiceIfDtmfDetectionNegativeTwist_Object((1,3,6,1,4,1,4935,15,30,1,40,1,60),_VoiceIfDtmfDetectionNegativeTwist_Type())
voiceIfDtmfDetectionNegativeTwist.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfDtmfDetectionNegativeTwist.setStatus(_A)
class _VoiceIfDtmfDetectionMinDuration_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,5000))
_VoiceIfDtmfDetectionMinDuration_Type.__name__=_D
_VoiceIfDtmfDetectionMinDuration_Object=MibTableColumn
voiceIfDtmfDetectionMinDuration=_VoiceIfDtmfDetectionMinDuration_Object((1,3,6,1,4,1,4935,15,30,1,40,1,70),_VoiceIfDtmfDetectionMinDuration_Type())
voiceIfDtmfDetectionMinDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfDtmfDetectionMinDuration.setStatus(_A)
_VoiceIfConformance_ObjectIdentity=ObjectIdentity
voiceIfConformance=_VoiceIfConformance_ObjectIdentity((1,3,6,1,4,1,4935,15,30,2))
_VoiceIfCompliances_ObjectIdentity=ObjectIdentity
voiceIfCompliances=_VoiceIfCompliances_ObjectIdentity((1,3,6,1,4,1,4935,15,30,2,1))
_VoiceIfGroups_ObjectIdentity=ObjectIdentity
voiceIfGroups=_VoiceIfGroups_ObjectIdentity((1,3,6,1,4,1,4935,15,30,2,2))
voiceIfCodecGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,15,30,2,2,1))
voiceIfCodecGroupVer1.setObjects(*((_C,_M),(_C,_N),(_C,_O),(_C,_P),(_C,_Q),(_C,_R),(_C,_S),(_C,_T),(_C,_U),(_C,_V),(_C,_W),(_C,_X),(_C,_Y),(_C,_Z),(_C,_a),(_C,_b),(_C,_c),(_C,_d),(_C,_e),(_C,_f),(_C,_g),(_C,_h),(_C,_i),(_C,_j),(_C,_k),(_C,_l),(_C,_m),(_C,_n),(_C,_o)))
if mibBuilder.loadTexts:voiceIfCodecGroupVer1.setStatus(_A)
voiceIfBasicGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,15,30,2,2,2))
voiceIfBasicGroupVer1.setObjects(*((_C,_p),(_C,_q),(_C,_r),(_C,_s),(_C,_t),(_C,_u),(_C,_v),(_C,_w),(_C,_x),(_C,_y),(_C,_z),(_C,_A0),(_C,_A1),(_C,_A2),(_C,_A3),(_C,_A4),(_C,_A5)))
if mibBuilder.loadTexts:voiceIfBasicGroupVer1.setStatus(_A)
voiceIfDtmfTransportBasicGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,15,30,2,2,3))
voiceIfDtmfTransportBasicGroupVer1.setObjects(*((_C,_A6),(_C,_A7),(_C,_A8)))
if mibBuilder.loadTexts:voiceIfDtmfTransportBasicGroupVer1.setStatus(_A)
voiceIfComplVer1=ModuleCompliance((1,3,6,1,4,1,4935,15,30,2,1,1))
voiceIfComplVer1.setObjects(*((_C,_A9),(_C,_AA),(_C,_AB)))
if mibBuilder.loadTexts:voiceIfComplVer1.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'voiceIfMIB':voiceIfMIB,'voiceIfMIBObjects':voiceIfMIBObjects,'voiceIfAllowDtmfOobRecovery':voiceIfAllowDtmfOobRecovery,'voiceIfTable':voiceIfTable,'voiceIfEntry':voiceIfEntry,_p:voiceIfAdaptativeJitterBufferEnable,_q:voiceIfTargetJitterBufferLength,_r:voiceIfMaxJitterBufferLength,_s:voiceIfG711VoiceActivityDetectionEnable,_t:voiceIfEchoCancellationEnable,_u:voiceIfG711ComfortNoiseGenerationEnable,_v:voiceIfBaseGainConfigurationSource,_w:voiceIfUserInputGainOffset,_x:voiceIfUserOutputGainOffset,_y:voiceIfBaseInputGain,_z:voiceIfBaseOutputGain,_A0:voiceIfBaseInputGainOffset,_A1:voiceIfBaseOutputGainOffset,_A2:voiceIfNlpThresholdLevel,_A3:voiceIfG729VoiceActivityDetectionEnable,_A4:voiceIfG723VoiceActivityDetectionEnable,_A5:voiceIfSignalLimiterLevel,'voiceIfCodecTable':voiceIfCodecTable,'voiceIfCodecEntry':voiceIfCodecEntry,_M:voiceIfCodecPreferred,_N:voiceIfCodecPcmuEnable,_O:voiceIfCodecPcmuMinPTime,_P:voiceIfCodecPcmuMaxPTime,_Q:voiceIfCodecPcmaEnable,_R:voiceIfCodecPcmaMinPTime,_S:voiceIfCodecPcmaMaxPTime,_T:voiceIfCodecG723Enable,_U:voiceIfCodecG723MinPTime,_V:voiceIfCodecG723MaxPTime,_W:voiceIfCodecG729Enable,_X:voiceIfCodecG729MinPTime,_Y:voiceIfCodecG729MaxPTime,_Z:voiceIfCodecG72616kbpsEnable,_a:voiceIfCodecG72616kbpsPayloadType,_b:voiceIfCodecG72616kbpsMinPTime,_c:voiceIfCodecG72616kbpsMaxPTime,_d:voiceIfCodecG72624kbpsEnable,_e:voiceIfCodecG72624kbpsPayloadType,_f:voiceIfCodecG72624kbpsMinPTime,_g:voiceIfCodecG72624kbpsMaxPTime,_h:voiceIfCodecG72632kbpsEnable,_i:voiceIfCodecG72632kbpsPayloadType,_j:voiceIfCodecG72632kbpsMinPTime,_k:voiceIfCodecG72632kbpsMaxPTime,_l:voiceIfCodecG72640kbpsEnable,_m:voiceIfCodecG72640kbpsPayloadType,_n:voiceIfCodecG72640kbpsMinPTime,_o:voiceIfCodecG72640kbpsMaxPTime,'voiceIfDtmfTransportTable':voiceIfDtmfTransportTable,'voiceIfDtmfTransportEntry':voiceIfDtmfTransportEntry,_A6:voiceIfDtmfTransport,_A7:voiceIfDtmfPayloadType,_A8:voiceIfDtmfEnforceDefaultEvents,'voiceIfDtmfDetectionTable':voiceIfDtmfDetectionTable,'voiceIfDtmfDetectionEntry':voiceIfDtmfDetectionEntry,'voiceIfDtmfDetectionRiseTimeCriteria':voiceIfDtmfDetectionRiseTimeCriteria,'voiceIfDtmfDetectionMaxPowerThreshold':voiceIfDtmfDetectionMaxPowerThreshold,'voiceIfDtmfDetectionMinPowerThreshold':voiceIfDtmfDetectionMinPowerThreshold,'voiceIfDtmfDetectionBreakPowerThreshold':voiceIfDtmfDetectionBreakPowerThreshold,'voiceIfDtmfDetectionPositiveTwist':voiceIfDtmfDetectionPositiveTwist,'voiceIfDtmfDetectionNegativeTwist':voiceIfDtmfDetectionNegativeTwist,'voiceIfDtmfDetectionMinDuration':voiceIfDtmfDetectionMinDuration,'voiceIfConformance':voiceIfConformance,'voiceIfCompliances':voiceIfCompliances,'voiceIfComplVer1':voiceIfComplVer1,'voiceIfGroups':voiceIfGroups,_AA:voiceIfCodecGroupVer1,_A9:voiceIfBasicGroupVer1,_AB:voiceIfDtmfTransportBasicGroupVer1})