_Am='ccasEMGroupRev2'
_Al='ccasEMGroup'
_Ak='ccasGeneralInfoGroup'
_Aj='ccasGrpEMTmDelayVoice'
_Ai='ccasGrpEMTmPttRcv'
_Ah='ccasGrpEMTmPttXmt'
_Ag='ccasGrpEMCfgAutoGainControl'
_Af='ccasXgcpCfgCotToneCo2'
_Ae='ccasXgcpCfgCotToneCo1'
_Ad='ccasGrpCfgServiceType'
_Ac='ccasVoiceCfgRegionalTone'
_Ab='ccasVoiceCfgInterDigitTimeOut'
_Aa='ccasVoiceCfgInitialDigitTimeOut'
_AZ='ccasVoiceCfgConnectionNumber'
_AY='ccasVoiceCfgConnectionMode'
_AX='ccasVoiceCfgEchoCancelCoverage'
_AW='ccasVoiceCfgEchoCancelEnable'
_AV='ccasVoiceCfgOutAttn'
_AU='ccasVoiceCfgInGain'
_AT='ccasVoiceCfgMusicOnHoldThreshold'
_AS='ccasVoiceCfgNonLinearProcEnable'
_AR='ccasVoiceCfgNoiseRegEnable'
_AQ='ccasGrpABCDCfgUnusedBits'
_AP='ccasGrpABCDCfgInvertBits'
_AO='ccasGrpStaTmPulseInterDigitDuration'
_AN='ccasGrpStaTmPulseRate'
_AM='ccasGrpStaTmInterDigitDuration'
_AL='ccasGrpStaTmDigitDuration'
_AK='ccasGrpStaCfgDialType'
_AJ='ccasGrpStaCfgNumberRings'
_AI='ccasGrpLineTmPulseInterDigitDuration'
_AH='ccasGrpLineTmPulseRate'
_AG='ccasGrpLineTmInterDigitDuration'
_AF='ccasGrpLineTmDigitDuration'
_AE='ccasGrpLineCfgDialType'
_AD='ccasGrpLineCfgSupDisconnect'
_AC='ccasGrpLineCfgNumberRings'
_AB='ccasDs1IfCfgDs0ChannelsConfigurable'
_AA='ccasChannelStatusEntry'
_A9='ccasGrpStaTmEntry'
_A8='ccasGrpLineTmEntry'
_A7='ccasGrpEMTmEntry'
_A6='TruthValue'
_A5='DisplayString'
_A4='ccasEMGroupRev1'
_A3='ccasGrpEMTmLmrTeardown'
_A2='ccasGrpEMTmVoiceHangover'
_A1='ccasGrpEMCfgLmrECap'
_A0='ccasGrpEMCfgLmrMCap'
_z='ccasChannelStatusXmitSignalBits'
_y='ccasChannelStatusInfoType'
_x='ccasChannelStatusBusyOut'
_w='ccasChannelStatusRecvSignalBits'
_v='ccasChannelCfgBusyOut'
_u='ccasChannelCfgTimeSlot'
_t='ccasChannelCfgGroup'
_s='ccasChannelCfgDS1IfIndex'
_r='ccasGrpCfgRowStatus'
_q='ccasGrpCfgDs0Channels'
_p='ccasGrpCfgType'
_o='seconds'
_n='pulses per second'
_m='pulse'
_l='dtmf'
_k='OctetString'
_j='ccasXgcpCfgGroup'
_i='ccasChannelInfoGroup'
_h='ccasGeneralInfoGroupRev1'
_g='deprecated'
_f='ccasGrpEMTmPulseInterDigitDuration'
_e='ccasGrpEMTmPulseRate'
_d='ccasGrpEMTmInterDigitDuration'
_c='ccasGrpEMTmDigitDuration'
_b='ccasGrpEMTmMinDelayPulseWidth'
_a='ccasGrpEMTmMaxDelayDuration'
_Z='ccasGrpEMTmDelayStart'
_Y='ccasGrpEMTmMaxWinkDuration'
_X='ccasGrpEMTmMaxWinkWaitDuration'
_W='ccasGrpEMTmClearWaitDuration'
_V='ccasGrpEMCfgDnisAni'
_U='ccasGrpEMCfgDialType'
_T='aBit'
_S='bBit'
_R='cBit'
_Q='dBit'
_P='read-create'
_O='ccasVoiceGroup'
_N='ccasCustomABCDGroup'
_M='ccasStaGroup'
_L='ccasLineGroup'
_K='ccasIfDS1Group'
_J='Bits'
_I='ccasGrpCfgIndex'
_H='read-only'
_G='ifIndex'
_F='IF-MIB'
_E='milliseconds'
_D='Integer32'
_C='read-write'
_B='current'
_A='CISCO-CAS-IF-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_k,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CountryCode,=mibBuilder.importSymbols('CISCO-TC','CountryCode')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_F,'InterfaceIndex',_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_J,'Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_A5,'PhysAddress','RowStatus','TextualConvention',_A6)
ciscoCasIfMIB=ModuleIdentity((1,3,6,1,4,1,9,9,85))
if mibBuilder.loadTexts:ciscoCasIfMIB.setRevisions(('2004-10-13 00:00','2004-09-30 00:00','2004-01-15 00:00','2003-04-18 00:00','2002-10-02 00:00','1999-01-18 00:00'))
_CcasIfObjects_ObjectIdentity=ObjectIdentity
ccasIfObjects=_CcasIfObjects_ObjectIdentity((1,3,6,1,4,1,9,9,85,1))
_CcasDS1Objects_ObjectIdentity=ObjectIdentity
ccasDS1Objects=_CcasDS1Objects_ObjectIdentity((1,3,6,1,4,1,9,9,85,1,1))
_CcasDs1IfCfgTable_Object=MibTable
ccasDs1IfCfgTable=_CcasDs1IfCfgTable_Object((1,3,6,1,4,1,9,9,85,1,1,1))
if mibBuilder.loadTexts:ccasDs1IfCfgTable.setStatus(_B)
_CcasDs1IfCfgEntry_Object=MibTableRow
ccasDs1IfCfgEntry=_CcasDs1IfCfgEntry_Object((1,3,6,1,4,1,9,9,85,1,1,1,1))
ccasDs1IfCfgEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:ccasDs1IfCfgEntry.setStatus(_B)
class _CcasDs1IfCfgDs0ChannelsConfigurable_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_CcasDs1IfCfgDs0ChannelsConfigurable_Type.__name__=_k
_CcasDs1IfCfgDs0ChannelsConfigurable_Object=MibTableColumn
ccasDs1IfCfgDs0ChannelsConfigurable=_CcasDs1IfCfgDs0ChannelsConfigurable_Object((1,3,6,1,4,1,9,9,85,1,1,1,1,1),_CcasDs1IfCfgDs0ChannelsConfigurable_Type())
ccasDs1IfCfgDs0ChannelsConfigurable.setMaxAccess(_H)
if mibBuilder.loadTexts:ccasDs1IfCfgDs0ChannelsConfigurable.setStatus(_B)
_CcasGrpObjects_ObjectIdentity=ObjectIdentity
ccasGrpObjects=_CcasGrpObjects_ObjectIdentity((1,3,6,1,4,1,9,9,85,1,2))
_CcasGrpGeneralObjects_ObjectIdentity=ObjectIdentity
ccasGrpGeneralObjects=_CcasGrpGeneralObjects_ObjectIdentity((1,3,6,1,4,1,9,9,85,1,2,1))
_CcasGrpCfgTable_Object=MibTable
ccasGrpCfgTable=_CcasGrpCfgTable_Object((1,3,6,1,4,1,9,9,85,1,2,1,1))
if mibBuilder.loadTexts:ccasGrpCfgTable.setStatus(_B)
_CcasGrpCfgEntry_Object=MibTableRow
ccasGrpCfgEntry=_CcasGrpCfgEntry_Object((1,3,6,1,4,1,9,9,85,1,2,1,1,1))
ccasGrpCfgEntry.setIndexNames((0,_F,_G),(0,_A,_I))
if mibBuilder.loadTexts:ccasGrpCfgEntry.setStatus(_B)
class _CcasGrpCfgIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30))
_CcasGrpCfgIndex_Type.__name__=_D
_CcasGrpCfgIndex_Object=MibTableColumn
ccasGrpCfgIndex=_CcasGrpCfgIndex_Object((1,3,6,1,4,1,9,9,85,1,2,1,1,1,1),_CcasGrpCfgIndex_Type())
ccasGrpCfgIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ccasGrpCfgIndex.setStatus(_B)
class _CcasGrpCfgType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27)));namedValues=NamedValues(*(('emWinkStart',1),('emWinkStartFgd',2),('emImmedStart',3),('emDelayDial',4),('fxsLoopStart',5),('fxsGroundStart',6),('sasLoopStart',7),('sasGroundStart',8),('r2Analog',9),('r2Digital',10),('r2Pulse',11),('p7',12),('fxoLoopStart',13),('fxoGroundStart',14),('fgdOS',15),('nullSignaling',16),('r1Itu',17),('r1Modified',18),('r1Turkey',19),('fgdEANA',20),('emMelImmedStart',21),('emMelWink',22),('emMelDelayDial',23),('fxsMelcas',24),('fxoMelcas',25),('extsig',26),('emLmr',27)))
_CcasGrpCfgType_Type.__name__=_D
_CcasGrpCfgType_Object=MibTableColumn
ccasGrpCfgType=_CcasGrpCfgType_Object((1,3,6,1,4,1,9,9,85,1,2,1,1,1,2),_CcasGrpCfgType_Type())
ccasGrpCfgType.setMaxAccess(_P)
if mibBuilder.loadTexts:ccasGrpCfgType.setStatus(_B)
class _CcasGrpCfgDs0Channels_Type(OctetString):defaultHexValue='00000000';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_CcasGrpCfgDs0Channels_Type.__name__=_k
_CcasGrpCfgDs0Channels_Object=MibTableColumn
ccasGrpCfgDs0Channels=_CcasGrpCfgDs0Channels_Object((1,3,6,1,4,1,9,9,85,1,2,1,1,1,3),_CcasGrpCfgDs0Channels_Type())
ccasGrpCfgDs0Channels.setMaxAccess(_P)
if mibBuilder.loadTexts:ccasGrpCfgDs0Channels.setStatus(_B)
_CcasGrpCfgRowStatus_Type=RowStatus
_CcasGrpCfgRowStatus_Object=MibTableColumn
ccasGrpCfgRowStatus=_CcasGrpCfgRowStatus_Object((1,3,6,1,4,1,9,9,85,1,2,1,1,1,4),_CcasGrpCfgRowStatus_Type())
ccasGrpCfgRowStatus.setMaxAccess(_P)
if mibBuilder.loadTexts:ccasGrpCfgRowStatus.setStatus(_B)
class _CcasGrpCfgServiceType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('none',1),('casServSw56',2),('casServModem',3),('casServAuto',4),('sgcp',5),('mgcp',6),('other',7),('trunkingService',8),('h248',9),('ds0xconn',10),('xgcp',11)))
_CcasGrpCfgServiceType_Type.__name__=_D
_CcasGrpCfgServiceType_Object=MibTableColumn
ccasGrpCfgServiceType=_CcasGrpCfgServiceType_Object((1,3,6,1,4,1,9,9,85,1,2,1,1,1,5),_CcasGrpCfgServiceType_Type())
ccasGrpCfgServiceType.setMaxAccess(_P)
if mibBuilder.loadTexts:ccasGrpCfgServiceType.setStatus(_B)
_CcasGrpEMObjects_ObjectIdentity=ObjectIdentity
ccasGrpEMObjects=_CcasGrpEMObjects_ObjectIdentity((1,3,6,1,4,1,9,9,85,1,2,2))
_CcasGrpEMCfgTable_Object=MibTable
ccasGrpEMCfgTable=_CcasGrpEMCfgTable_Object((1,3,6,1,4,1,9,9,85,1,2,2,1))
if mibBuilder.loadTexts:ccasGrpEMCfgTable.setStatus(_B)
_CcasGrpEMCfgEntry_Object=MibTableRow
ccasGrpEMCfgEntry=_CcasGrpEMCfgEntry_Object((1,3,6,1,4,1,9,9,85,1,2,2,1,1))
ccasGrpEMCfgEntry.setIndexNames((0,_F,_G),(0,_A,_I))
if mibBuilder.loadTexts:ccasGrpEMCfgEntry.setStatus(_B)
class _CcasGrpEMCfgDialType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_l,1),(_m,2),('mf',3)))
_CcasGrpEMCfgDialType_Type.__name__=_D
_CcasGrpEMCfgDialType_Object=MibTableColumn
ccasGrpEMCfgDialType=_CcasGrpEMCfgDialType_Object((1,3,6,1,4,1,9,9,85,1,2,2,1,1,1),_CcasGrpEMCfgDialType_Type())
ccasGrpEMCfgDialType.setMaxAccess(_C)
if mibBuilder.loadTexts:ccasGrpEMCfgDialType.setStatus(_B)
class _CcasGrpEMCfgDnisAni_Type(Bits):namedValues=NamedValues(*(('incomingDnis',0),('incomingAni',1),('outgoingDnis',2),('outgoingAni',3)))
_CcasGrpEMCfgDnisAni_Type.__name__=_J
_CcasGrpEMCfgDnisAni_Object=MibTableColumn
ccasGrpEMCfgDnisAni=_CcasGrpEMCfgDnisAni_Object((1,3,6,1,4,1,9,9,85,1,2,2,1,1,2),_CcasGrpEMCfgDnisAni_Type())
ccasGrpEMCfgDnisAni.setMaxAccess(_C)
if mibBuilder.loadTexts:ccasGrpEMCfgDnisAni.setStatus(_B)
class _CcasGrpEMCfgLmrMCap_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('inact',1),('audio',2),('dial',3)))
_CcasGrpEMCfgLmrMCap_Type.__name__=_D
_CcasGrpEMCfgLmrMCap_Object=MibTableColumn
ccasGrpEMCfgLmrMCap=_CcasGrpEMCfgLmrMCap_Object((1,3,6,1,4,1,9,9,85,1,2,2,1,1,3),_CcasGrpEMCfgLmrMCap_Type())
ccasGrpEMCfgLmrMCap.setMaxAccess(_C)
if mibBuilder.loadTexts:ccasGrpEMCfgLmrMCap.setStatus(_B)
class _CcasGrpEMCfgLmrECap_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(4,5,6)));namedValues=NamedValues(*(('seize',4),('voice',5),('inactive',6)))
_CcasGrpEMCfgLmrECap_Type.__name__=_D
_CcasGrpEMCfgLmrECap_Object=MibTableColumn
ccasGrpEMCfgLmrECap=_CcasGrpEMCfgLmrECap_Object((1,3,6,1,4,1,9,9,85,1,2,2,1,1,4),_CcasGrpEMCfgLmrECap_Type())
ccasGrpEMCfgLmrECap.setMaxAccess(_C)
if mibBuilder.loadTexts:ccasGrpEMCfgLmrECap.setStatus(_B)
class _CcasGrpEMCfgAutoGainControl_Type(TruthValue):defaultValue=2
_CcasGrpEMCfgAutoGainControl_Type.__name__=_A6
_CcasGrpEMCfgAutoGainControl_Object=MibTableColumn
ccasGrpEMCfgAutoGainControl=_CcasGrpEMCfgAutoGainControl_Object((1,3,6,1,4,1,9,9,85,1,2,2,1,1,5),_CcasGrpEMCfgAutoGainControl_Type())
ccasGrpEMCfgAutoGainControl.setMaxAccess(_C)
if mibBuilder.loadTexts:ccasGrpEMCfgAutoGainControl.setStatus(_B)
_CcasGrpEMTmTable_Object=MibTable
ccasGrpEMTmTable=_CcasGrpEMTmTable_Object((1,3,6,1,4,1,9,9,85,1,2,2,2))
if mibBuilder.loadTexts:ccasGrpEMTmTable.setStatus(_B)
_CcasGrpEMTmEntry_Object=MibTableRow
ccasGrpEMTmEntry=_CcasGrpEMTmEntry_Object((1,3,6,1,4,1,9,9,85,1,2,2,2,1))
if mibBuilder.loadTexts:ccasGrpEMTmEntry.setStatus(_B)
class _CcasGrpEMTmClearWaitDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(200,2000))
_CcasGrpEMTmClearWaitDuration_Type.__name__=_D
_CcasGrpEMTmClearWaitDuration_Object=MibTableColumn
ccasGrpEMTmClearWaitDuration=_CcasGrpEMTmClearWaitDuration_Object((1,3,6,1,4,1,9,9,85,1,2,2,2,1,1),_CcasGrpEMTmClearWaitDuration_Type())
ccasGrpEMTmClearWaitDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:ccasGrpEMTmClearWaitDuration.setStatus(_B)
if mibBuilder.loadTexts:ccasGrpEMTmClearWaitDuration.setUnits(_E)
class _CcasGrpEMTmMaxWinkWaitDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,5000))
_CcasGrpEMTmMaxWinkWaitDuration_Type.__name__=_D
_CcasGrpEMTmMaxWinkWaitDuration_Object=MibTableColumn
ccasGrpEMTmMaxWinkWaitDuration=_CcasGrpEMTmMaxWinkWaitDuration_Object((1,3,6,1,4,1,9,9,85,1,2,2,2,1,2),_CcasGrpEMTmMaxWinkWaitDuration_Type())
ccasGrpEMTmMaxWinkWaitDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:ccasGrpEMTmMaxWinkWaitDuration.setStatus(_B)
if mibBuilder.loadTexts:ccasGrpEMTmMaxWinkWaitDuration.setUnits(_E)
class _CcasGrpEMTmMaxWinkDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,3000))
_CcasGrpEMTmMaxWinkDuration_Type.__name__=_D
_CcasGrpEMTmMaxWinkDuration_Object=MibTableColumn
ccasGrpEMTmMaxWinkDuration=_CcasGrpEMTmMaxWinkDuration_Object((1,3,6,1,4,1,9,9,85,1,2,2,2,1,3),_CcasGrpEMTmMaxWinkDuration_Type())
ccasGrpEMTmMaxWinkDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:ccasGrpEMTmMaxWinkDuration.setStatus(_B)
if mibBuilder.loadTexts:ccasGrpEMTmMaxWinkDuration.setUnits(_E)
class _CcasGrpEMTmDelayStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,2000))
_CcasGrpEMTmDelayStart_Type.__name__=_D
_CcasGrpEMTmDelayStart_Object=MibTableColumn
ccasGrpEMTmDelayStart=_CcasGrpEMTmDelayStart_Object((1,3,6,1,4,1,9,9,85,1,2,2,2,1,4),_CcasGrpEMTmDelayStart_Type())
ccasGrpEMTmDelayStart.setMaxAccess(_C)
if mibBuilder.loadTexts:ccasGrpEMTmDelayStart.setStatus(_B)
if mibBuilder.loadTexts:ccasGrpEMTmDelayStart.setUnits(_E)
class _CcasGrpEMTmMaxDelayDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,5000))
_CcasGrpEMTmMaxDelayDuration_Type.__name__=_D
_CcasGrpEMTmMaxDelayDuration_Object=MibTableColumn
ccasGrpEMTmMaxDelayDuration=_CcasGrpEMTmMaxDelayDuration_Object((1,3,6,1,4,1,9,9,85,1,2,2,2,1,5),_CcasGrpEMTmMaxDelayDuration_Type())
ccasGrpEMTmMaxDelayDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:ccasGrpEMTmMaxDelayDuration.setStatus(_B)
if mibBuilder.loadTexts:ccasGrpEMTmMaxDelayDuration.setUnits(_E)
class _CcasGrpEMTmMinDelayPulseWidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(140,5000))
_CcasGrpEMTmMinDelayPulseWidth_Type.__name__=_D
_CcasGrpEMTmMinDelayPulseWidth_Object=MibTableColumn
ccasGrpEMTmMinDelayPulseWidth=_CcasGrpEMTmMinDelayPulseWidth_Object((1,3,6,1,4,1,9,9,85,1,2,2,2,1,6),_CcasGrpEMTmMinDelayPulseWidth_Type())
ccasGrpEMTmMinDelayPulseWidth.setMaxAccess(_C)
if mibBuilder.loadTexts:ccasGrpEMTmMinDelayPulseWidth.setStatus(_B)
if mibBuilder.loadTexts:ccasGrpEMTmMinDelayPulseWidth.setUnits(_E)
class _CcasGrpEMTmDigitDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,500))
_CcasGrpEMTmDigitDuration_Type.__name__=_D
_CcasGrpEMTmDigitDuration_Object=MibTableColumn
ccasGrpEMTmDigitDuration=_CcasGrpEMTmDigitDuration_Object((1,3,6,1,4,1,9,9,85,1,2,2,2,1,7),_CcasGrpEMTmDigitDuration_Type())
ccasGrpEMTmDigitDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:ccasGrpEMTmDigitDuration.setStatus(_B)
if mibBuilder.loadTexts:ccasGrpEMTmDigitDuration.setUnits(_E)
class _CcasGrpEMTmInterDigitDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,500))
_CcasGrpEMTmInterDigitDuration_Type.__name__=_D
_CcasGrpEMTmInterDigitDuration_Object=MibTableColumn
ccasGrpEMTmInterDigitDuration=_CcasGrpEMTmInterDigitDuration_Object((1,3,6,1,4,1,9,9,85,1,2,2,2,1,8),_CcasGrpEMTmInterDigitDuration_Type())
ccasGrpEMTmInterDigitDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:ccasGrpEMTmInterDigitDuration.setStatus(_B)
if mibBuilder.loadTexts:ccasGrpEMTmInterDigitDuration.setUnits(_E)
class _CcasGrpEMTmPulseRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,20))
_CcasGrpEMTmPulseRate_Type.__name__=_D
_CcasGrpEMTmPulseRate_Object=MibTableColumn
ccasGrpEMTmPulseRate=_CcasGrpEMTmPulseRate_Object((1,3,6,1,4,1,9,9,85,1,2,2,2,1,9),_CcasGrpEMTmPulseRate_Type())
ccasGrpEMTmPulseRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ccasGrpEMTmPulseRate.setStatus(_B)
if mibBuilder.loadTexts:ccasGrpEMTmPulseRate.setUnits(_n)
class _CcasGrpEMTmPulseInterDigitDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,1000))
_CcasGrpEMTmPulseInterDigitDuration_Type.__name__=_D
_CcasGrpEMTmPulseInterDigitDuration_Object=MibTableColumn
ccasGrpEMTmPulseInterDigitDuration=_CcasGrpEMTmPulseInterDigitDuration_Object((1,3,6,1,4,1,9,9,85,1,2,2,2,1,10),_CcasGrpEMTmPulseInterDigitDuration_Type())
ccasGrpEMTmPulseInterDigitDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:ccasGrpEMTmPulseInterDigitDuration.setStatus(_B)
if mibBuilder.loadTexts:ccasGrpEMTmPulseInterDigitDuration.setUnits(_E)
class _CcasGrpEMTmVoiceHangover_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_CcasGrpEMTmVoiceHangover_Type.__name__=_D
_CcasGrpEMTmVoiceHangover_Object=MibTableColumn
ccasGrpEMTmVoiceHangover=_CcasGrpEMTmVoiceHangover_Object((1,3,6,1,4,1,9,9,85,1,2,2,2,1,11),_CcasGrpEMTmVoiceHangover_Type())
ccasGrpEMTmVoiceHangover.setMaxAccess(_C)
if mibBuilder.loadTexts:ccasGrpEMTmVoiceHangover.setStatus(_B)
if mibBuilder.loadTexts:ccasGrpEMTmVoiceHangover.setUnits(_E)
class _CcasGrpEMTmLmrTeardown_Type(Integer32):defaultValue=1800;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(5,60000))
_CcasGrpEMTmLmrTeardown_Type.__name__=_D
_CcasGrpEMTmLmrTeardown_Object=MibTableColumn
ccasGrpEMTmLmrTeardown=_CcasGrpEMTmLmrTeardown_Object((1,3,6,1,4,1,9,9,85,1,2,2,2,1,12),_CcasGrpEMTmLmrTeardown_Type())
ccasGrpEMTmLmrTeardown.setMaxAccess(_C)
if mibBuilder.loadTexts:ccasGrpEMTmLmrTeardown.setStatus(_B)
if mibBuilder.loadTexts:ccasGrpEMTmLmrTeardown.setUnits(_o)
class _CcasGrpEMTmPttXmt_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30))
_CcasGrpEMTmPttXmt_Type.__name__=_D
_CcasGrpEMTmPttXmt_Object=MibTableColumn
ccasGrpEMTmPttXmt=_CcasGrpEMTmPttXmt_Object((1,3,6,1,4,1,9,9,85,1,2,2,2,1,13),_CcasGrpEMTmPttXmt_Type())
ccasGrpEMTmPttXmt.setMaxAccess(_C)
if mibBuilder.loadTexts:ccasGrpEMTmPttXmt.setStatus(_B)
if mibBuilder.loadTexts:ccasGrpEMTmPttXmt.setUnits('minutes')
class _CcasGrpEMTmPttRcv_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30))
_CcasGrpEMTmPttRcv_Type.__name__=_D
_CcasGrpEMTmPttRcv_Object=MibTableColumn
ccasGrpEMTmPttRcv=_CcasGrpEMTmPttRcv_Object((1,3,6,1,4,1,9,9,85,1,2,2,2,1,14),_CcasGrpEMTmPttRcv_Type())
ccasGrpEMTmPttRcv.setMaxAccess(_C)
if mibBuilder.loadTexts:ccasGrpEMTmPttRcv.setStatus(_B)
if mibBuilder.loadTexts:ccasGrpEMTmPttRcv.setUnits('minutes')
class _CcasGrpEMTmDelayVoice_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1500))
_CcasGrpEMTmDelayVoice_Type.__name__=_D
_CcasGrpEMTmDelayVoice_Object=MibTableColumn
ccasGrpEMTmDelayVoice=_CcasGrpEMTmDelayVoice_Object((1,3,6,1,4,1,9,9,85,1,2,2,2,1,15),_CcasGrpEMTmDelayVoice_Type())
ccasGrpEMTmDelayVoice.setMaxAccess(_H)
if mibBuilder.loadTexts:ccasGrpEMTmDelayVoice.setStatus(_B)
if mibBuilder.loadTexts:ccasGrpEMTmDelayVoice.setUnits(_E)
_CcasGrpLineObjects_ObjectIdentity=ObjectIdentity
ccasGrpLineObjects=_CcasGrpLineObjects_ObjectIdentity((1,3,6,1,4,1,9,9,85,1,2,3))
_CcasGrpLineCfgTable_Object=MibTable
ccasGrpLineCfgTable=_CcasGrpLineCfgTable_Object((1,3,6,1,4,1,9,9,85,1,2,3,1))
if mibBuilder.loadTexts:ccasGrpLineCfgTable.setStatus(_B)
_CcasGrpLineCfgEntry_Object=MibTableRow
ccasGrpLineCfgEntry=_CcasGrpLineCfgEntry_Object((1,3,6,1,4,1,9,9,85,1,2,3,1,1))
ccasGrpLineCfgEntry.setIndexNames((0,_F,_G),(0,_A,_I))
if mibBuilder.loadTexts:ccasGrpLineCfgEntry.setStatus(_B)
class _CcasGrpLineCfgNumberRings_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_CcasGrpLineCfgNumberRings_Type.__name__=_D
_CcasGrpLineCfgNumberRings_Object=MibTableColumn
ccasGrpLineCfgNumberRings=_CcasGrpLineCfgNumberRings_Object((1,3,6,1,4,1,9,9,85,1,2,3,1,1,1),_CcasGrpLineCfgNumberRings_Type())
ccasGrpLineCfgNumberRings.setMaxAccess(_C)
if mibBuilder.loadTexts:ccasGrpLineCfgNumberRings.setStatus(_B)
if mibBuilder.loadTexts:ccasGrpLineCfgNumberRings.setUnits('rings')
_CcasGrpLineCfgSupDisconnect_Type=TruthValue
_CcasGrpLineCfgSupDisconnect_Object=MibTableColumn
ccasGrpLineCfgSupDisconnect=_CcasGrpLineCfgSupDisconnect_Object((1,3,6,1,4,1,9,9,85,1,2,3,1,1,2),_CcasGrpLineCfgSupDisconnect_Type())
ccasGrpLineCfgSupDisconnect.setMaxAccess(_C)
if mibBuilder.loadTexts:ccasGrpLineCfgSupDisconnect.setStatus(_B)
class _CcasGrpLineCfgDialType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_l,1),(_m,2)))
_CcasGrpLineCfgDialType_Type.__name__=_D
_CcasGrpLineCfgDialType_Object=MibTableColumn
ccasGrpLineCfgDialType=_CcasGrpLineCfgDialType_Object((1,3,6,1,4,1,9,9,85,1,2,3,1,1,3),_CcasGrpLineCfgDialType_Type())
ccasGrpLineCfgDialType.setMaxAccess(_C)
if mibBuilder.loadTexts:ccasGrpLineCfgDialType.setStatus(_B)
_CcasGrpLineTmTable_Object=MibTable
ccasGrpLineTmTable=_CcasGrpLineTmTable_Object((1,3,6,1,4,1,9,9,85,1,2,3,2))
if mibBuilder.loadTexts:ccasGrpLineTmTable.setStatus(_B)
_CcasGrpLineTmEntry_Object=MibTableRow
ccasGrpLineTmEntry=_CcasGrpLineTmEntry_Object((1,3,6,1,4,1,9,9,85,1,2,3,2,1))
if mibBuilder.loadTexts:ccasGrpLineTmEntry.setStatus(_B)
class _CcasGrpLineTmDigitDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,500))
_CcasGrpLineTmDigitDuration_Type.__name__=_D
_CcasGrpLineTmDigitDuration_Object=MibTableColumn
ccasGrpLineTmDigitDuration=_CcasGrpLineTmDigitDuration_Object((1,3,6,1,4,1,9,9,85,1,2,3,2,1,1),_CcasGrpLineTmDigitDuration_Type())
ccasGrpLineTmDigitDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:ccasGrpLineTmDigitDuration.setStatus(_B)
if mibBuilder.loadTexts:ccasGrpLineTmDigitDuration.setUnits(_E)
class _CcasGrpLineTmInterDigitDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,500))
_CcasGrpLineTmInterDigitDuration_Type.__name__=_D
_CcasGrpLineTmInterDigitDuration_Object=MibTableColumn
ccasGrpLineTmInterDigitDuration=_CcasGrpLineTmInterDigitDuration_Object((1,3,6,1,4,1,9,9,85,1,2,3,2,1,2),_CcasGrpLineTmInterDigitDuration_Type())
ccasGrpLineTmInterDigitDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:ccasGrpLineTmInterDigitDuration.setStatus(_B)
if mibBuilder.loadTexts:ccasGrpLineTmInterDigitDuration.setUnits(_E)
class _CcasGrpLineTmPulseRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,20))
_CcasGrpLineTmPulseRate_Type.__name__=_D
_CcasGrpLineTmPulseRate_Object=MibTableColumn
ccasGrpLineTmPulseRate=_CcasGrpLineTmPulseRate_Object((1,3,6,1,4,1,9,9,85,1,2,3,2,1,3),_CcasGrpLineTmPulseRate_Type())
ccasGrpLineTmPulseRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ccasGrpLineTmPulseRate.setStatus(_B)
if mibBuilder.loadTexts:ccasGrpLineTmPulseRate.setUnits(_n)
class _CcasGrpLineTmPulseInterDigitDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,1000))
_CcasGrpLineTmPulseInterDigitDuration_Type.__name__=_D
_CcasGrpLineTmPulseInterDigitDuration_Object=MibTableColumn
ccasGrpLineTmPulseInterDigitDuration=_CcasGrpLineTmPulseInterDigitDuration_Object((1,3,6,1,4,1,9,9,85,1,2,3,2,1,4),_CcasGrpLineTmPulseInterDigitDuration_Type())
ccasGrpLineTmPulseInterDigitDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:ccasGrpLineTmPulseInterDigitDuration.setStatus(_B)
if mibBuilder.loadTexts:ccasGrpLineTmPulseInterDigitDuration.setUnits(_E)
_CcasGrpStaObjects_ObjectIdentity=ObjectIdentity
ccasGrpStaObjects=_CcasGrpStaObjects_ObjectIdentity((1,3,6,1,4,1,9,9,85,1,2,4))
_CcasGrpStaCfgTable_Object=MibTable
ccasGrpStaCfgTable=_CcasGrpStaCfgTable_Object((1,3,6,1,4,1,9,9,85,1,2,4,1))
if mibBuilder.loadTexts:ccasGrpStaCfgTable.setStatus(_B)
_CcasGrpStaCfgEntry_Object=MibTableRow
ccasGrpStaCfgEntry=_CcasGrpStaCfgEntry_Object((1,3,6,1,4,1,9,9,85,1,2,4,1,1))
ccasGrpStaCfgEntry.setIndexNames((0,_F,_G),(0,_A,_I))
if mibBuilder.loadTexts:ccasGrpStaCfgEntry.setStatus(_B)
class _CcasGrpStaCfgNumberRings_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_CcasGrpStaCfgNumberRings_Type.__name__=_D
_CcasGrpStaCfgNumberRings_Object=MibTableColumn
ccasGrpStaCfgNumberRings=_CcasGrpStaCfgNumberRings_Object((1,3,6,1,4,1,9,9,85,1,2,4,1,1,1),_CcasGrpStaCfgNumberRings_Type())
ccasGrpStaCfgNumberRings.setMaxAccess(_C)
if mibBuilder.loadTexts:ccasGrpStaCfgNumberRings.setStatus(_B)
if mibBuilder.loadTexts:ccasGrpStaCfgNumberRings.setUnits('rings')
class _CcasGrpStaCfgDialType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_l,1),(_m,2)))
_CcasGrpStaCfgDialType_Type.__name__=_D
_CcasGrpStaCfgDialType_Object=MibTableColumn
ccasGrpStaCfgDialType=_CcasGrpStaCfgDialType_Object((1,3,6,1,4,1,9,9,85,1,2,4,1,1,2),_CcasGrpStaCfgDialType_Type())
ccasGrpStaCfgDialType.setMaxAccess(_C)
if mibBuilder.loadTexts:ccasGrpStaCfgDialType.setStatus(_B)
_CcasGrpStaTmTable_Object=MibTable
ccasGrpStaTmTable=_CcasGrpStaTmTable_Object((1,3,6,1,4,1,9,9,85,1,2,4,2))
if mibBuilder.loadTexts:ccasGrpStaTmTable.setStatus(_B)
_CcasGrpStaTmEntry_Object=MibTableRow
ccasGrpStaTmEntry=_CcasGrpStaTmEntry_Object((1,3,6,1,4,1,9,9,85,1,2,4,2,1))
if mibBuilder.loadTexts:ccasGrpStaTmEntry.setStatus(_B)
class _CcasGrpStaTmDigitDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,500))
_CcasGrpStaTmDigitDuration_Type.__name__=_D
_CcasGrpStaTmDigitDuration_Object=MibTableColumn
ccasGrpStaTmDigitDuration=_CcasGrpStaTmDigitDuration_Object((1,3,6,1,4,1,9,9,85,1,2,4,2,1,1),_CcasGrpStaTmDigitDuration_Type())
ccasGrpStaTmDigitDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:ccasGrpStaTmDigitDuration.setStatus(_B)
if mibBuilder.loadTexts:ccasGrpStaTmDigitDuration.setUnits(_E)
class _CcasGrpStaTmInterDigitDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,500))
_CcasGrpStaTmInterDigitDuration_Type.__name__=_D
_CcasGrpStaTmInterDigitDuration_Object=MibTableColumn
ccasGrpStaTmInterDigitDuration=_CcasGrpStaTmInterDigitDuration_Object((1,3,6,1,4,1,9,9,85,1,2,4,2,1,2),_CcasGrpStaTmInterDigitDuration_Type())
ccasGrpStaTmInterDigitDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:ccasGrpStaTmInterDigitDuration.setStatus(_B)
if mibBuilder.loadTexts:ccasGrpStaTmInterDigitDuration.setUnits(_E)
class _CcasGrpStaTmPulseRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,20))
_CcasGrpStaTmPulseRate_Type.__name__=_D
_CcasGrpStaTmPulseRate_Object=MibTableColumn
ccasGrpStaTmPulseRate=_CcasGrpStaTmPulseRate_Object((1,3,6,1,4,1,9,9,85,1,2,4,2,1,3),_CcasGrpStaTmPulseRate_Type())
ccasGrpStaTmPulseRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ccasGrpStaTmPulseRate.setStatus(_B)
if mibBuilder.loadTexts:ccasGrpStaTmPulseRate.setUnits(_n)
class _CcasGrpStaTmPulseInterDigitDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,1000))
_CcasGrpStaTmPulseInterDigitDuration_Type.__name__=_D
_CcasGrpStaTmPulseInterDigitDuration_Object=MibTableColumn
ccasGrpStaTmPulseInterDigitDuration=_CcasGrpStaTmPulseInterDigitDuration_Object((1,3,6,1,4,1,9,9,85,1,2,4,2,1,4),_CcasGrpStaTmPulseInterDigitDuration_Type())
ccasGrpStaTmPulseInterDigitDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:ccasGrpStaTmPulseInterDigitDuration.setStatus(_B)
if mibBuilder.loadTexts:ccasGrpStaTmPulseInterDigitDuration.setUnits(_E)
_CcasGrpABCDObjects_ObjectIdentity=ObjectIdentity
ccasGrpABCDObjects=_CcasGrpABCDObjects_ObjectIdentity((1,3,6,1,4,1,9,9,85,1,2,5))
_CcasGrpABCDCfgTable_Object=MibTable
ccasGrpABCDCfgTable=_CcasGrpABCDCfgTable_Object((1,3,6,1,4,1,9,9,85,1,2,5,1))
if mibBuilder.loadTexts:ccasGrpABCDCfgTable.setStatus(_B)
_CcasGrpABCDCfgEntry_Object=MibTableRow
ccasGrpABCDCfgEntry=_CcasGrpABCDCfgEntry_Object((1,3,6,1,4,1,9,9,85,1,2,5,1,1))
ccasGrpABCDCfgEntry.setIndexNames((0,_F,_G),(0,_A,_I))
if mibBuilder.loadTexts:ccasGrpABCDCfgEntry.setStatus(_B)
class _CcasGrpABCDCfgInvertBits_Type(Bits):namedValues=NamedValues(*((_Q,0),(_R,1),(_S,2),(_T,3)))
_CcasGrpABCDCfgInvertBits_Type.__name__=_J
_CcasGrpABCDCfgInvertBits_Object=MibTableColumn
ccasGrpABCDCfgInvertBits=_CcasGrpABCDCfgInvertBits_Object((1,3,6,1,4,1,9,9,85,1,2,5,1,1,1),_CcasGrpABCDCfgInvertBits_Type())
ccasGrpABCDCfgInvertBits.setMaxAccess(_C)
if mibBuilder.loadTexts:ccasGrpABCDCfgInvertBits.setStatus(_B)
class _CcasGrpABCDCfgUnusedBits_Type(Bits):namedValues=NamedValues(*((_Q,0),(_R,1),(_S,2),(_T,3)))
_CcasGrpABCDCfgUnusedBits_Type.__name__=_J
_CcasGrpABCDCfgUnusedBits_Object=MibTableColumn
ccasGrpABCDCfgUnusedBits=_CcasGrpABCDCfgUnusedBits_Object((1,3,6,1,4,1,9,9,85,1,2,5,1,1,2),_CcasGrpABCDCfgUnusedBits_Type())
ccasGrpABCDCfgUnusedBits.setMaxAccess(_C)
if mibBuilder.loadTexts:ccasGrpABCDCfgUnusedBits.setStatus(_B)
_CcasChannelObjects_ObjectIdentity=ObjectIdentity
ccasChannelObjects=_CcasChannelObjects_ObjectIdentity((1,3,6,1,4,1,9,9,85,1,3))
_CcasChannelCfgTable_Object=MibTable
ccasChannelCfgTable=_CcasChannelCfgTable_Object((1,3,6,1,4,1,9,9,85,1,3,1))
if mibBuilder.loadTexts:ccasChannelCfgTable.setStatus(_B)
_CcasChannelCfgEntry_Object=MibTableRow
ccasChannelCfgEntry=_CcasChannelCfgEntry_Object((1,3,6,1,4,1,9,9,85,1,3,1,1))
ccasChannelCfgEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:ccasChannelCfgEntry.setStatus(_B)
_CcasChannelCfgDS1IfIndex_Type=InterfaceIndex
_CcasChannelCfgDS1IfIndex_Object=MibTableColumn
ccasChannelCfgDS1IfIndex=_CcasChannelCfgDS1IfIndex_Object((1,3,6,1,4,1,9,9,85,1,3,1,1,1),_CcasChannelCfgDS1IfIndex_Type())
ccasChannelCfgDS1IfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:ccasChannelCfgDS1IfIndex.setStatus(_B)
class _CcasChannelCfgGroup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30))
_CcasChannelCfgGroup_Type.__name__=_D
_CcasChannelCfgGroup_Object=MibTableColumn
ccasChannelCfgGroup=_CcasChannelCfgGroup_Object((1,3,6,1,4,1,9,9,85,1,3,1,1,2),_CcasChannelCfgGroup_Type())
ccasChannelCfgGroup.setMaxAccess(_H)
if mibBuilder.loadTexts:ccasChannelCfgGroup.setStatus(_B)
class _CcasChannelCfgTimeSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,31))
_CcasChannelCfgTimeSlot_Type.__name__=_D
_CcasChannelCfgTimeSlot_Object=MibTableColumn
ccasChannelCfgTimeSlot=_CcasChannelCfgTimeSlot_Object((1,3,6,1,4,1,9,9,85,1,3,1,1,3),_CcasChannelCfgTimeSlot_Type())
ccasChannelCfgTimeSlot.setMaxAccess(_H)
if mibBuilder.loadTexts:ccasChannelCfgTimeSlot.setStatus(_B)
_CcasChannelCfgBusyOut_Type=TruthValue
_CcasChannelCfgBusyOut_Object=MibTableColumn
ccasChannelCfgBusyOut=_CcasChannelCfgBusyOut_Object((1,3,6,1,4,1,9,9,85,1,3,1,1,4),_CcasChannelCfgBusyOut_Type())
ccasChannelCfgBusyOut.setMaxAccess(_C)
if mibBuilder.loadTexts:ccasChannelCfgBusyOut.setStatus(_B)
_CcasChannelStatusTable_Object=MibTable
ccasChannelStatusTable=_CcasChannelStatusTable_Object((1,3,6,1,4,1,9,9,85,1,3,2))
if mibBuilder.loadTexts:ccasChannelStatusTable.setStatus(_B)
_CcasChannelStatusEntry_Object=MibTableRow
ccasChannelStatusEntry=_CcasChannelStatusEntry_Object((1,3,6,1,4,1,9,9,85,1,3,2,1))
if mibBuilder.loadTexts:ccasChannelStatusEntry.setStatus(_B)
class _CcasChannelStatusRecvSignalBits_Type(Bits):namedValues=NamedValues(*((_Q,0),(_R,1),(_S,2),(_T,3)))
_CcasChannelStatusRecvSignalBits_Type.__name__=_J
_CcasChannelStatusRecvSignalBits_Object=MibTableColumn
ccasChannelStatusRecvSignalBits=_CcasChannelStatusRecvSignalBits_Object((1,3,6,1,4,1,9,9,85,1,3,2,1,1),_CcasChannelStatusRecvSignalBits_Type())
ccasChannelStatusRecvSignalBits.setMaxAccess(_H)
if mibBuilder.loadTexts:ccasChannelStatusRecvSignalBits.setStatus(_B)
_CcasChannelStatusBusyOut_Type=TruthValue
_CcasChannelStatusBusyOut_Object=MibTableColumn
ccasChannelStatusBusyOut=_CcasChannelStatusBusyOut_Object((1,3,6,1,4,1,9,9,85,1,3,2,1,2),_CcasChannelStatusBusyOut_Type())
ccasChannelStatusBusyOut.setMaxAccess(_H)
if mibBuilder.loadTexts:ccasChannelStatusBusyOut.setStatus(_B)
class _CcasChannelStatusInfoType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('unknown',1),('speech',2),('data56',3),('audio31',4),('audio7',5),('video',6),('fax',7),('modem',8)))
_CcasChannelStatusInfoType_Type.__name__=_D
_CcasChannelStatusInfoType_Object=MibTableColumn
ccasChannelStatusInfoType=_CcasChannelStatusInfoType_Object((1,3,6,1,4,1,9,9,85,1,3,2,1,3),_CcasChannelStatusInfoType_Type())
ccasChannelStatusInfoType.setMaxAccess(_H)
if mibBuilder.loadTexts:ccasChannelStatusInfoType.setStatus(_B)
class _CcasChannelStatusXmitSignalBits_Type(Bits):namedValues=NamedValues(*((_Q,0),(_R,1),(_S,2),(_T,3)))
_CcasChannelStatusXmitSignalBits_Type.__name__=_J
_CcasChannelStatusXmitSignalBits_Object=MibTableColumn
ccasChannelStatusXmitSignalBits=_CcasChannelStatusXmitSignalBits_Object((1,3,6,1,4,1,9,9,85,1,3,2,1,4),_CcasChannelStatusXmitSignalBits_Type())
ccasChannelStatusXmitSignalBits.setMaxAccess(_H)
if mibBuilder.loadTexts:ccasChannelStatusXmitSignalBits.setStatus(_B)
_CcasVoiceCfgObjects_ObjectIdentity=ObjectIdentity
ccasVoiceCfgObjects=_CcasVoiceCfgObjects_ObjectIdentity((1,3,6,1,4,1,9,9,85,1,4))
_CcasVoiceCfgTable_Object=MibTable
ccasVoiceCfgTable=_CcasVoiceCfgTable_Object((1,3,6,1,4,1,9,9,85,1,4,1))
if mibBuilder.loadTexts:ccasVoiceCfgTable.setStatus(_B)
_CcasVoiceCfgEntry_Object=MibTableRow
ccasVoiceCfgEntry=_CcasVoiceCfgEntry_Object((1,3,6,1,4,1,9,9,85,1,4,1,1))
ccasVoiceCfgEntry.setIndexNames((0,_F,_G),(0,_A,_I))
if mibBuilder.loadTexts:ccasVoiceCfgEntry.setStatus(_B)
_CcasVoiceCfgNoiseRegEnable_Type=TruthValue
_CcasVoiceCfgNoiseRegEnable_Object=MibTableColumn
ccasVoiceCfgNoiseRegEnable=_CcasVoiceCfgNoiseRegEnable_Object((1,3,6,1,4,1,9,9,85,1,4,1,1,1),_CcasVoiceCfgNoiseRegEnable_Type())
ccasVoiceCfgNoiseRegEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:ccasVoiceCfgNoiseRegEnable.setStatus(_B)
_CcasVoiceCfgNonLinearProcEnable_Type=TruthValue
_CcasVoiceCfgNonLinearProcEnable_Object=MibTableColumn
ccasVoiceCfgNonLinearProcEnable=_CcasVoiceCfgNonLinearProcEnable_Object((1,3,6,1,4,1,9,9,85,1,4,1,1,2),_CcasVoiceCfgNonLinearProcEnable_Type())
ccasVoiceCfgNonLinearProcEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:ccasVoiceCfgNonLinearProcEnable.setStatus(_B)
class _CcasVoiceCfgMusicOnHoldThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-70,-30))
_CcasVoiceCfgMusicOnHoldThreshold_Type.__name__=_D
_CcasVoiceCfgMusicOnHoldThreshold_Object=MibTableColumn
ccasVoiceCfgMusicOnHoldThreshold=_CcasVoiceCfgMusicOnHoldThreshold_Object((1,3,6,1,4,1,9,9,85,1,4,1,1,3),_CcasVoiceCfgMusicOnHoldThreshold_Type())
ccasVoiceCfgMusicOnHoldThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:ccasVoiceCfgMusicOnHoldThreshold.setStatus(_B)
if mibBuilder.loadTexts:ccasVoiceCfgMusicOnHoldThreshold.setUnits('dBm')
class _CcasVoiceCfgInGain_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-6,14))
_CcasVoiceCfgInGain_Type.__name__=_D
_CcasVoiceCfgInGain_Object=MibTableColumn
ccasVoiceCfgInGain=_CcasVoiceCfgInGain_Object((1,3,6,1,4,1,9,9,85,1,4,1,1,4),_CcasVoiceCfgInGain_Type())
ccasVoiceCfgInGain.setMaxAccess(_C)
if mibBuilder.loadTexts:ccasVoiceCfgInGain.setStatus(_B)
if mibBuilder.loadTexts:ccasVoiceCfgInGain.setUnits('dB')
class _CcasVoiceCfgOutAttn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,14))
_CcasVoiceCfgOutAttn_Type.__name__=_D
_CcasVoiceCfgOutAttn_Object=MibTableColumn
ccasVoiceCfgOutAttn=_CcasVoiceCfgOutAttn_Object((1,3,6,1,4,1,9,9,85,1,4,1,1,5),_CcasVoiceCfgOutAttn_Type())
ccasVoiceCfgOutAttn.setMaxAccess(_C)
if mibBuilder.loadTexts:ccasVoiceCfgOutAttn.setStatus(_B)
if mibBuilder.loadTexts:ccasVoiceCfgOutAttn.setUnits('dB')
_CcasVoiceCfgEchoCancelEnable_Type=TruthValue
_CcasVoiceCfgEchoCancelEnable_Object=MibTableColumn
ccasVoiceCfgEchoCancelEnable=_CcasVoiceCfgEchoCancelEnable_Object((1,3,6,1,4,1,9,9,85,1,4,1,1,6),_CcasVoiceCfgEchoCancelEnable_Type())
ccasVoiceCfgEchoCancelEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:ccasVoiceCfgEchoCancelEnable.setStatus(_B)
class _CcasVoiceCfgEchoCancelCoverage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('echoCanceller8ms',1),('echoCanceller16ms',2),('echoCanceller24ms',3),('echoCanceller32ms',4),('echoCanceller64ms',5),('echoCanceller128ms',6)))
_CcasVoiceCfgEchoCancelCoverage_Type.__name__=_D
_CcasVoiceCfgEchoCancelCoverage_Object=MibTableColumn
ccasVoiceCfgEchoCancelCoverage=_CcasVoiceCfgEchoCancelCoverage_Object((1,3,6,1,4,1,9,9,85,1,4,1,1,7),_CcasVoiceCfgEchoCancelCoverage_Type())
ccasVoiceCfgEchoCancelCoverage.setMaxAccess(_C)
if mibBuilder.loadTexts:ccasVoiceCfgEchoCancelCoverage.setStatus(_B)
class _CcasVoiceCfgConnectionMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('normal',1),('trunk',2),('plar',3)))
_CcasVoiceCfgConnectionMode_Type.__name__=_D
_CcasVoiceCfgConnectionMode_Object=MibTableColumn
ccasVoiceCfgConnectionMode=_CcasVoiceCfgConnectionMode_Object((1,3,6,1,4,1,9,9,85,1,4,1,1,8),_CcasVoiceCfgConnectionMode_Type())
ccasVoiceCfgConnectionMode.setMaxAccess(_C)
if mibBuilder.loadTexts:ccasVoiceCfgConnectionMode.setStatus(_B)
class _CcasVoiceCfgConnectionNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CcasVoiceCfgConnectionNumber_Type.__name__=_A5
_CcasVoiceCfgConnectionNumber_Object=MibTableColumn
ccasVoiceCfgConnectionNumber=_CcasVoiceCfgConnectionNumber_Object((1,3,6,1,4,1,9,9,85,1,4,1,1,9),_CcasVoiceCfgConnectionNumber_Type())
ccasVoiceCfgConnectionNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:ccasVoiceCfgConnectionNumber.setStatus(_B)
class _CcasVoiceCfgInitialDigitTimeOut_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,120))
_CcasVoiceCfgInitialDigitTimeOut_Type.__name__=_D
_CcasVoiceCfgInitialDigitTimeOut_Object=MibTableColumn
ccasVoiceCfgInitialDigitTimeOut=_CcasVoiceCfgInitialDigitTimeOut_Object((1,3,6,1,4,1,9,9,85,1,4,1,1,10),_CcasVoiceCfgInitialDigitTimeOut_Type())
ccasVoiceCfgInitialDigitTimeOut.setMaxAccess(_C)
if mibBuilder.loadTexts:ccasVoiceCfgInitialDigitTimeOut.setStatus(_B)
if mibBuilder.loadTexts:ccasVoiceCfgInitialDigitTimeOut.setUnits(_o)
class _CcasVoiceCfgInterDigitTimeOut_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,120))
_CcasVoiceCfgInterDigitTimeOut_Type.__name__=_D
_CcasVoiceCfgInterDigitTimeOut_Object=MibTableColumn
ccasVoiceCfgInterDigitTimeOut=_CcasVoiceCfgInterDigitTimeOut_Object((1,3,6,1,4,1,9,9,85,1,4,1,1,11),_CcasVoiceCfgInterDigitTimeOut_Type())
ccasVoiceCfgInterDigitTimeOut.setMaxAccess(_C)
if mibBuilder.loadTexts:ccasVoiceCfgInterDigitTimeOut.setStatus(_B)
if mibBuilder.loadTexts:ccasVoiceCfgInterDigitTimeOut.setUnits(_o)
_CcasVoiceCfgRegionalTone_Type=CountryCode
_CcasVoiceCfgRegionalTone_Object=MibTableColumn
ccasVoiceCfgRegionalTone=_CcasVoiceCfgRegionalTone_Object((1,3,6,1,4,1,9,9,85,1,4,1,1,12),_CcasVoiceCfgRegionalTone_Type())
ccasVoiceCfgRegionalTone.setMaxAccess(_C)
if mibBuilder.loadTexts:ccasVoiceCfgRegionalTone.setStatus(_B)
_CcasXgcpCfgObjects_ObjectIdentity=ObjectIdentity
ccasXgcpCfgObjects=_CcasXgcpCfgObjects_ObjectIdentity((1,3,6,1,4,1,9,9,85,1,5))
_CcasXgcpCfgTable_Object=MibTable
ccasXgcpCfgTable=_CcasXgcpCfgTable_Object((1,3,6,1,4,1,9,9,85,1,5,1))
if mibBuilder.loadTexts:ccasXgcpCfgTable.setStatus(_B)
_CcasXgcpCfgEntry_Object=MibTableRow
ccasXgcpCfgEntry=_CcasXgcpCfgEntry_Object((1,3,6,1,4,1,9,9,85,1,5,1,1))
ccasXgcpCfgEntry.setIndexNames((0,_F,_G),(0,_A,_I))
if mibBuilder.loadTexts:ccasXgcpCfgEntry.setStatus(_B)
class _CcasXgcpCfgCotToneCo1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(280,3800))
_CcasXgcpCfgCotToneCo1_Type.__name__=_D
_CcasXgcpCfgCotToneCo1_Object=MibTableColumn
ccasXgcpCfgCotToneCo1=_CcasXgcpCfgCotToneCo1_Object((1,3,6,1,4,1,9,9,85,1,5,1,1,1),_CcasXgcpCfgCotToneCo1_Type())
ccasXgcpCfgCotToneCo1.setMaxAccess(_C)
if mibBuilder.loadTexts:ccasXgcpCfgCotToneCo1.setStatus(_B)
if mibBuilder.loadTexts:ccasXgcpCfgCotToneCo1.setUnits('hertz')
class _CcasXgcpCfgCotToneCo2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(280,3800))
_CcasXgcpCfgCotToneCo2_Type.__name__=_D
_CcasXgcpCfgCotToneCo2_Object=MibTableColumn
ccasXgcpCfgCotToneCo2=_CcasXgcpCfgCotToneCo2_Object((1,3,6,1,4,1,9,9,85,1,5,1,1,2),_CcasXgcpCfgCotToneCo2_Type())
ccasXgcpCfgCotToneCo2.setMaxAccess(_C)
if mibBuilder.loadTexts:ccasXgcpCfgCotToneCo2.setStatus(_B)
if mibBuilder.loadTexts:ccasXgcpCfgCotToneCo2.setUnits('hertz')
_CcasIfMIBConformance_ObjectIdentity=ObjectIdentity
ccasIfMIBConformance=_CcasIfMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,85,3))
_CcasIfMIBCompliances_ObjectIdentity=ObjectIdentity
ccasIfMIBCompliances=_CcasIfMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,85,3,1))
_CcasIfMIBGroups_ObjectIdentity=ObjectIdentity
ccasIfMIBGroups=_CcasIfMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,85,3,2))
ccasGrpEMCfgEntry.registerAugmentions((_A,_A7))
ccasGrpEMTmEntry.setIndexNames(*ccasGrpEMCfgEntry.getIndexNames())
ccasGrpLineCfgEntry.registerAugmentions((_A,_A8))
ccasGrpLineTmEntry.setIndexNames(*ccasGrpLineCfgEntry.getIndexNames())
ccasGrpStaCfgEntry.registerAugmentions((_A,_A9))
ccasGrpStaTmEntry.setIndexNames(*ccasGrpStaCfgEntry.getIndexNames())
ccasChannelCfgEntry.registerAugmentions((_A,_AA))
ccasChannelStatusEntry.setIndexNames(*ccasChannelCfgEntry.getIndexNames())
ccasIfDS1Group=ObjectGroup((1,3,6,1,4,1,9,9,85,3,2,1))
ccasIfDS1Group.setObjects((_A,_AB))
if mibBuilder.loadTexts:ccasIfDS1Group.setStatus(_B)
ccasGeneralInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,85,3,2,2))
ccasGeneralInfoGroup.setObjects(*((_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z)))
if mibBuilder.loadTexts:ccasGeneralInfoGroup.setStatus('obsolete')
ccasEMGroup=ObjectGroup((1,3,6,1,4,1,9,9,85,3,2,3))
ccasEMGroup.setObjects(*((_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f)))
if mibBuilder.loadTexts:ccasEMGroup.setStatus(_g)
ccasLineGroup=ObjectGroup((1,3,6,1,4,1,9,9,85,3,2,4))
ccasLineGroup.setObjects(*((_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI)))
if mibBuilder.loadTexts:ccasLineGroup.setStatus(_B)
ccasStaGroup=ObjectGroup((1,3,6,1,4,1,9,9,85,3,2,5))
ccasStaGroup.setObjects(*((_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO)))
if mibBuilder.loadTexts:ccasStaGroup.setStatus(_B)
ccasCustomABCDGroup=ObjectGroup((1,3,6,1,4,1,9,9,85,3,2,6))
ccasCustomABCDGroup.setObjects(*((_A,_AP),(_A,_AQ)))
if mibBuilder.loadTexts:ccasCustomABCDGroup.setStatus(_B)
ccasVoiceGroup=ObjectGroup((1,3,6,1,4,1,9,9,85,3,2,7))
ccasVoiceGroup.setObjects(*((_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_Ab),(_A,_Ac)))
if mibBuilder.loadTexts:ccasVoiceGroup.setStatus(_B)
ccasGeneralInfoGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,85,3,2,8))
ccasGeneralInfoGroupRev1.setObjects(*((_A,_p),(_A,_q),(_A,_Ad),(_A,_r)))
if mibBuilder.loadTexts:ccasGeneralInfoGroupRev1.setStatus(_B)
ccasChannelInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,85,3,2,9))
ccasChannelInfoGroup.setObjects(*((_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z)))
if mibBuilder.loadTexts:ccasChannelInfoGroup.setStatus(_B)
ccasXgcpCfgGroup=ObjectGroup((1,3,6,1,4,1,9,9,85,3,2,10))
ccasXgcpCfgGroup.setObjects(*((_A,_Ae),(_A,_Af)))
if mibBuilder.loadTexts:ccasXgcpCfgGroup.setStatus(_B)
ccasEMGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,85,3,2,11))
ccasEMGroupRev1.setObjects(*((_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3)))
if mibBuilder.loadTexts:ccasEMGroupRev1.setStatus(_g)
ccasEMGroupRev2=ObjectGroup((1,3,6,1,4,1,9,9,85,3,2,12))
ccasEMGroupRev2.setObjects(*((_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_Ag),(_A,_Ah),(_A,_Ai),(_A,_Aj)))
if mibBuilder.loadTexts:ccasEMGroupRev2.setStatus(_B)
ccasIfMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,85,3,1,1))
ccasIfMIBCompliance.setObjects(*((_A,_K),(_A,_Ak),(_A,_Al),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:ccasIfMIBCompliance.setStatus('obsolete')
ccasIfMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,85,3,1,2))
ccasIfMIBComplianceRev1.setObjects(*((_A,_K),(_A,_h),(_A,_A4),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_i),(_A,_j)))
if mibBuilder.loadTexts:ccasIfMIBComplianceRev1.setStatus(_g)
ccasIfMIBComplianceRev2=ModuleCompliance((1,3,6,1,4,1,9,9,85,3,1,3))
ccasIfMIBComplianceRev2.setObjects(*((_A,_K),(_A,_h),(_A,_A4),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_i),(_A,_j)))
if mibBuilder.loadTexts:ccasIfMIBComplianceRev2.setStatus(_g)
ccasIfMIBComplianceRev3=ModuleCompliance((1,3,6,1,4,1,9,9,85,3,1,4))
ccasIfMIBComplianceRev3.setObjects(*((_A,_K),(_A,_h),(_A,_Am),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_i),(_A,_j)))
if mibBuilder.loadTexts:ccasIfMIBComplianceRev3.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoCasIfMIB':ciscoCasIfMIB,'ccasIfObjects':ccasIfObjects,'ccasDS1Objects':ccasDS1Objects,'ccasDs1IfCfgTable':ccasDs1IfCfgTable,'ccasDs1IfCfgEntry':ccasDs1IfCfgEntry,_AB:ccasDs1IfCfgDs0ChannelsConfigurable,'ccasGrpObjects':ccasGrpObjects,'ccasGrpGeneralObjects':ccasGrpGeneralObjects,'ccasGrpCfgTable':ccasGrpCfgTable,'ccasGrpCfgEntry':ccasGrpCfgEntry,_I:ccasGrpCfgIndex,_p:ccasGrpCfgType,_q:ccasGrpCfgDs0Channels,_r:ccasGrpCfgRowStatus,_Ad:ccasGrpCfgServiceType,'ccasGrpEMObjects':ccasGrpEMObjects,'ccasGrpEMCfgTable':ccasGrpEMCfgTable,'ccasGrpEMCfgEntry':ccasGrpEMCfgEntry,_U:ccasGrpEMCfgDialType,_V:ccasGrpEMCfgDnisAni,_A0:ccasGrpEMCfgLmrMCap,_A1:ccasGrpEMCfgLmrECap,_Ag:ccasGrpEMCfgAutoGainControl,'ccasGrpEMTmTable':ccasGrpEMTmTable,_A7:ccasGrpEMTmEntry,_W:ccasGrpEMTmClearWaitDuration,_X:ccasGrpEMTmMaxWinkWaitDuration,_Y:ccasGrpEMTmMaxWinkDuration,_Z:ccasGrpEMTmDelayStart,_a:ccasGrpEMTmMaxDelayDuration,_b:ccasGrpEMTmMinDelayPulseWidth,_c:ccasGrpEMTmDigitDuration,_d:ccasGrpEMTmInterDigitDuration,_e:ccasGrpEMTmPulseRate,_f:ccasGrpEMTmPulseInterDigitDuration,_A2:ccasGrpEMTmVoiceHangover,_A3:ccasGrpEMTmLmrTeardown,_Ah:ccasGrpEMTmPttXmt,_Ai:ccasGrpEMTmPttRcv,_Aj:ccasGrpEMTmDelayVoice,'ccasGrpLineObjects':ccasGrpLineObjects,'ccasGrpLineCfgTable':ccasGrpLineCfgTable,'ccasGrpLineCfgEntry':ccasGrpLineCfgEntry,_AC:ccasGrpLineCfgNumberRings,_AD:ccasGrpLineCfgSupDisconnect,_AE:ccasGrpLineCfgDialType,'ccasGrpLineTmTable':ccasGrpLineTmTable,_A8:ccasGrpLineTmEntry,_AF:ccasGrpLineTmDigitDuration,_AG:ccasGrpLineTmInterDigitDuration,_AH:ccasGrpLineTmPulseRate,_AI:ccasGrpLineTmPulseInterDigitDuration,'ccasGrpStaObjects':ccasGrpStaObjects,'ccasGrpStaCfgTable':ccasGrpStaCfgTable,'ccasGrpStaCfgEntry':ccasGrpStaCfgEntry,_AJ:ccasGrpStaCfgNumberRings,_AK:ccasGrpStaCfgDialType,'ccasGrpStaTmTable':ccasGrpStaTmTable,_A9:ccasGrpStaTmEntry,_AL:ccasGrpStaTmDigitDuration,_AM:ccasGrpStaTmInterDigitDuration,_AN:ccasGrpStaTmPulseRate,_AO:ccasGrpStaTmPulseInterDigitDuration,'ccasGrpABCDObjects':ccasGrpABCDObjects,'ccasGrpABCDCfgTable':ccasGrpABCDCfgTable,'ccasGrpABCDCfgEntry':ccasGrpABCDCfgEntry,_AP:ccasGrpABCDCfgInvertBits,_AQ:ccasGrpABCDCfgUnusedBits,'ccasChannelObjects':ccasChannelObjects,'ccasChannelCfgTable':ccasChannelCfgTable,'ccasChannelCfgEntry':ccasChannelCfgEntry,_s:ccasChannelCfgDS1IfIndex,_t:ccasChannelCfgGroup,_u:ccasChannelCfgTimeSlot,_v:ccasChannelCfgBusyOut,'ccasChannelStatusTable':ccasChannelStatusTable,_AA:ccasChannelStatusEntry,_w:ccasChannelStatusRecvSignalBits,_x:ccasChannelStatusBusyOut,_y:ccasChannelStatusInfoType,_z:ccasChannelStatusXmitSignalBits,'ccasVoiceCfgObjects':ccasVoiceCfgObjects,'ccasVoiceCfgTable':ccasVoiceCfgTable,'ccasVoiceCfgEntry':ccasVoiceCfgEntry,_AR:ccasVoiceCfgNoiseRegEnable,_AS:ccasVoiceCfgNonLinearProcEnable,_AT:ccasVoiceCfgMusicOnHoldThreshold,_AU:ccasVoiceCfgInGain,_AV:ccasVoiceCfgOutAttn,_AW:ccasVoiceCfgEchoCancelEnable,_AX:ccasVoiceCfgEchoCancelCoverage,_AY:ccasVoiceCfgConnectionMode,_AZ:ccasVoiceCfgConnectionNumber,_Aa:ccasVoiceCfgInitialDigitTimeOut,_Ab:ccasVoiceCfgInterDigitTimeOut,_Ac:ccasVoiceCfgRegionalTone,'ccasXgcpCfgObjects':ccasXgcpCfgObjects,'ccasXgcpCfgTable':ccasXgcpCfgTable,'ccasXgcpCfgEntry':ccasXgcpCfgEntry,_Ae:ccasXgcpCfgCotToneCo1,_Af:ccasXgcpCfgCotToneCo2,'ccasIfMIBConformance':ccasIfMIBConformance,'ccasIfMIBCompliances':ccasIfMIBCompliances,'ccasIfMIBCompliance':ccasIfMIBCompliance,'ccasIfMIBComplianceRev1':ccasIfMIBComplianceRev1,'ccasIfMIBComplianceRev2':ccasIfMIBComplianceRev2,'ccasIfMIBComplianceRev3':ccasIfMIBComplianceRev3,'ccasIfMIBGroups':ccasIfMIBGroups,_K:ccasIfDS1Group,_Ak:ccasGeneralInfoGroup,_Al:ccasEMGroup,_L:ccasLineGroup,_M:ccasStaGroup,_N:ccasCustomABCDGroup,_O:ccasVoiceGroup,_h:ccasGeneralInfoGroupRev1,_i:ccasChannelInfoGroup,_j:ccasXgcpCfgGroup,_A4:ccasEMGroupRev1,_Am:ccasEMGroupRev2})