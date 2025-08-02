_B2='pktcInternationalGroup'
_B1='pktcNcsGroup'
_B0='pktcSigGroup'
_A_='pktcSigDevToneFreqRepeatCount'
_Az='pktcSigDevToneFreqOffDuration'
_Ay='pktcSigDevToneFreqOnDuration'
_Ax='pktcSigDevToneFreqAmpModePrtg'
_Aw='pktcSigDevToneFreqMode'
_Av='pktcSigDevToneFourthFreqValue'
_Au='pktcSigDevToneThirdFreqValue'
_At='pktcSigDevToneSecondFreqValue'
_As='pktcSigDevToneFirstFreqValue'
_Ar='pktcSigDevToneSteady'
_Aq='pktcSigDevToneWholeToneRepeatCount'
_Ap='pktcSigDevToneDbLevel'
_Ao='pktcSigPulseSignalRepeatCount'
_An='pktcSigPulseSignalPulseInterval'
_Am='pktcSigPulseSignalDuration'
_Al='pktcSigPulseSignalDbLevel'
_Ak='pktcSigPulseSignalFrequency'
_Aj='pktcSigPowerRingFrequency'
_Ai='pktcSigDevVmwiDTASAfterLR'
_Ah='pktcSigDevVmwiFskAfterRPAS'
_Ag='pktcSigDevVmwiFskAfterDTAS'
_Af='pktcSigDevCIDDTASAfterLR'
_Ae='pktcSigDevCIDRingAfterFSK'
_Ad='pktcSigDevCIDFskAfterRPAS'
_Ac='pktcSigDevCIDFskAfterDTAS'
_Ab='pktcSigDevCIDFskAfterRing'
_Aa='pktcSigDevCIDMode'
_AZ='pktcSigDevCallerIdSigProtocol'
_AY='pktcSigDevRingCadence'
_AX='pktcNcsEndPntConfigPulseDialMaxBreakTime'
_AW='pktcNcsEndPntConfigPulseDialMinBreakTime'
_AV='pktcNcsEndPntConfigPulseDialMaxMakeTime'
_AU='pktcNcsEndPntConfigPulseDialMinMakeTime'
_AT='pktcNcsEndPntConfigPulseDialInterdigitTime'
_AS='pktcNcsEndPntConfigMaxHookFlash'
_AR='pktcNcsEndPntConfigMinHookFlash'
_AQ='pktcNcsEndPntStatusError'
_AP='pktcNcsEndPntStatusCallIpAddress'
_AO='pktcNcsEndPntStatusCallIpAddressType'
_AN='pktcNcsEndPntConfigCallWaitingDelay'
_AM='pktcNcsEndPntConfigCallWaitingMaxRep'
_AL='pktcNcsEndPntConfigStatus'
_AK='pktcNcsEndPntConfigThist'
_AJ='pktcNcsEndPntConfigLongDurationKeepAlive'
_AI='pktcNcsEndPntConfigRtoInit'
_AH='pktcNcsEndPntConfigRtoMax'
_AG='pktcNcsEndPntConfigTdmax'
_AF='pktcNcsEndPntConfigTdmin'
_AE='pktcNcsEndPntConfigTdinit'
_AD='pktcNcsEndPntConfigMWD'
_AC='pktcNcsEndPntConfigMax2QEnable'
_AB='pktcNcsEndPntConfigMax1QEnable'
_AA='pktcNcsEndPntConfigMax2'
_A9='pktcNcsEndPntConfigMax1'
_A8='pktcNcsEndPntConfigTSMax'
_A7='pktcNcsEndPntConfigStutterDialToneTO'
_A6='pktcNcsEndPntConfigReorderToneTO'
_A5='pktcNcsEndPntConfigRingBackTO'
_A4='pktcNcsEndPntConfigRingingTO'
_A3='pktcNcsEndPntConfigOffHookWarnToneTO'
_A2='pktcNcsEndPntConfigMessageWaitingTO'
_A1='pktcNcsEndPntConfigDialToneTO'
_A0='pktcNcsEndPntConfigBusyToneTO'
_z='pktcNcsEndPntConfigCriticalDialTO'
_y='pktcNcsEndPntConfigPartialDialTO'
_x='pktcNcsEndPntConfigCallAgentUdpPort'
_w='pktcNcsEndPntConfigCallAgentId'
_v='pktcSigDefNcsReceiveUdpPort'
_u='pktcSignalingVendorExtension'
_t='pktcSignalingVersion'
_s='pktcSignalingType'
_r='pktcSigDevVmwiMode'
_q='pktcSigDefMediaStreamDscp'
_p='pktcSigDefCallSigDscp'
_o='pktcSigDevRsCadence'
_n='pktcSigDevRgCadence'
_m='pktcSigDevR7Cadence'
_l='pktcSigDevR6Cadence'
_k='pktcSigDevR5Cadence'
_j='pktcSigDevR4Cadence'
_i='pktcSigDevR3Cadence'
_h='pktcSigDevR2Cadence'
_g='pktcSigDevR1Cadence'
_f='pktcSigDevR0Cadence'
_e='pktcSigDevSilenceSuppression'
_d='pktcSigDevEchoCancellation'
_c='pktcSigDevCodecMax'
_b='pktcSigDevToneNumber'
_a='pktcSigDevRingCadenceIndex'
_Z='lrAsETS'
_Y='rpAsETS'
_X='dtAsETS'
_W='pktcSigPulseSignalType'
_V='pktcSignalingIndex'
_U='pktcSigDevCodecType'
_T='pktcSigDevCodecComboIndex'
_S='reserved'
_R='SnmpAdminString'
_Q='ifIndex'
_P='IF-MIB'
_O='pktcSigDevToneType'
_N='TenthdBm'
_M='TruthValue'
_L='InetPortNumber'
_K='Dscp'
_J='not-accessible'
_I='read-only'
_H='Integer32'
_G='seconds'
_F='Milliseconds'
_E='read-create'
_D='read-write'
_C='Unsigned32'
_B='PKTC-EXCENTIS-SIG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Dscp,=mibBuilder.importSymbols('DIFFSERV-DSCP-TC',_K)
excentis,=mibBuilder.importSymbols('EXCENTIS-MIB','excentis')
ifIndex,=mibBuilder.importSymbols(_P,_Q)
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType',_L)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_R)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'iso','mib-2')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_M)
pktcExcentisSigMib=ModuleIdentity((1,3,6,1,4,1,7432,2))
if mibBuilder.loadTexts:pktcExcentisSigMib.setRevisions(('2005-09-09 00:00',))
class TenthdBm(TextualConvention,Integer32):status=_A;displayHint='d-1'
class PktcCodecType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*(('other',1),('unknown',2),('g729',3),(_S,4),('g729E',5),('pcmu',6),('g726at32',7),('g728',8),('pcma',9),('g726at16',10),('g726at24',11),('g726at40',12),('ilbc',13),('bv16',14)))
class PktcRingCadence(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,36))
class PktcSigType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),(_S,2),('ncs',3)))
_PktcSigNotification_ObjectIdentity=ObjectIdentity
pktcSigNotification=_PktcSigNotification_ObjectIdentity((1,3,6,1,4,1,7432,2,0))
_PktcSigMibObjects_ObjectIdentity=ObjectIdentity
pktcSigMibObjects=_PktcSigMibObjects_ObjectIdentity((1,3,6,1,4,1,7432,2,1))
_PktcSigDevConfigObjects_ObjectIdentity=ObjectIdentity
pktcSigDevConfigObjects=_PktcSigDevConfigObjects_ObjectIdentity((1,3,6,1,4,1,7432,2,1,1))
_PktcSigDevCodecTable_Object=MibTable
pktcSigDevCodecTable=_PktcSigDevCodecTable_Object((1,3,6,1,4,1,7432,2,1,1,1))
if mibBuilder.loadTexts:pktcSigDevCodecTable.setStatus(_A)
_PktcSigDevCodecEntry_Object=MibTableRow
pktcSigDevCodecEntry=_PktcSigDevCodecEntry_Object((1,3,6,1,4,1,7432,2,1,1,1,1))
pktcSigDevCodecEntry.setIndexNames((0,_B,_T),(0,_B,_U))
if mibBuilder.loadTexts:pktcSigDevCodecEntry.setStatus(_A)
class _PktcSigDevCodecComboIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_PktcSigDevCodecComboIndex_Type.__name__=_C
_PktcSigDevCodecComboIndex_Object=MibTableColumn
pktcSigDevCodecComboIndex=_PktcSigDevCodecComboIndex_Object((1,3,6,1,4,1,7432,2,1,1,1,1,1),_PktcSigDevCodecComboIndex_Type())
pktcSigDevCodecComboIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:pktcSigDevCodecComboIndex.setStatus(_A)
_PktcSigDevCodecType_Type=PktcCodecType
_PktcSigDevCodecType_Object=MibTableColumn
pktcSigDevCodecType=_PktcSigDevCodecType_Object((1,3,6,1,4,1,7432,2,1,1,1,1,2),_PktcSigDevCodecType_Type())
pktcSigDevCodecType.setMaxAccess(_J)
if mibBuilder.loadTexts:pktcSigDevCodecType.setStatus(_A)
class _PktcSigDevCodecMax_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_PktcSigDevCodecMax_Type.__name__=_C
_PktcSigDevCodecMax_Object=MibTableColumn
pktcSigDevCodecMax=_PktcSigDevCodecMax_Object((1,3,6,1,4,1,7432,2,1,1,1,1,3),_PktcSigDevCodecMax_Type())
pktcSigDevCodecMax.setMaxAccess(_I)
if mibBuilder.loadTexts:pktcSigDevCodecMax.setStatus(_A)
_PktcSigDevEchoCancellation_Type=TruthValue
_PktcSigDevEchoCancellation_Object=MibScalar
pktcSigDevEchoCancellation=_PktcSigDevEchoCancellation_Object((1,3,6,1,4,1,7432,2,1,1,2),_PktcSigDevEchoCancellation_Type())
pktcSigDevEchoCancellation.setMaxAccess(_I)
if mibBuilder.loadTexts:pktcSigDevEchoCancellation.setStatus(_A)
_PktcSigDevSilenceSuppression_Type=TruthValue
_PktcSigDevSilenceSuppression_Object=MibScalar
pktcSigDevSilenceSuppression=_PktcSigDevSilenceSuppression_Object((1,3,6,1,4,1,7432,2,1,1,3),_PktcSigDevSilenceSuppression_Type())
pktcSigDevSilenceSuppression.setMaxAccess(_I)
if mibBuilder.loadTexts:pktcSigDevSilenceSuppression.setStatus(_A)
class _PktcSigDevCallerIdSigProtocol_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fsk',1),('dtmf',2)))
_PktcSigDevCallerIdSigProtocol_Type.__name__=_H
_PktcSigDevCallerIdSigProtocol_Object=MibScalar
pktcSigDevCallerIdSigProtocol=_PktcSigDevCallerIdSigProtocol_Object((1,3,6,1,4,1,7432,2,1,1,4),_PktcSigDevCallerIdSigProtocol_Type())
pktcSigDevCallerIdSigProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcSigDevCallerIdSigProtocol.setStatus(_A)
_PktcSigDevR0Cadence_Type=PktcRingCadence
_PktcSigDevR0Cadence_Object=MibScalar
pktcSigDevR0Cadence=_PktcSigDevR0Cadence_Object((1,3,6,1,4,1,7432,2,1,1,5),_PktcSigDevR0Cadence_Type())
pktcSigDevR0Cadence.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcSigDevR0Cadence.setStatus(_A)
_PktcSigDevR1Cadence_Type=PktcRingCadence
_PktcSigDevR1Cadence_Object=MibScalar
pktcSigDevR1Cadence=_PktcSigDevR1Cadence_Object((1,3,6,1,4,1,7432,2,1,1,6),_PktcSigDevR1Cadence_Type())
pktcSigDevR1Cadence.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcSigDevR1Cadence.setStatus(_A)
_PktcSigDevR2Cadence_Type=PktcRingCadence
_PktcSigDevR2Cadence_Object=MibScalar
pktcSigDevR2Cadence=_PktcSigDevR2Cadence_Object((1,3,6,1,4,1,7432,2,1,1,7),_PktcSigDevR2Cadence_Type())
pktcSigDevR2Cadence.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcSigDevR2Cadence.setStatus(_A)
_PktcSigDevR3Cadence_Type=PktcRingCadence
_PktcSigDevR3Cadence_Object=MibScalar
pktcSigDevR3Cadence=_PktcSigDevR3Cadence_Object((1,3,6,1,4,1,7432,2,1,1,8),_PktcSigDevR3Cadence_Type())
pktcSigDevR3Cadence.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcSigDevR3Cadence.setStatus(_A)
_PktcSigDevR4Cadence_Type=PktcRingCadence
_PktcSigDevR4Cadence_Object=MibScalar
pktcSigDevR4Cadence=_PktcSigDevR4Cadence_Object((1,3,6,1,4,1,7432,2,1,1,9),_PktcSigDevR4Cadence_Type())
pktcSigDevR4Cadence.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcSigDevR4Cadence.setStatus(_A)
_PktcSigDevR5Cadence_Type=PktcRingCadence
_PktcSigDevR5Cadence_Object=MibScalar
pktcSigDevR5Cadence=_PktcSigDevR5Cadence_Object((1,3,6,1,4,1,7432,2,1,1,10),_PktcSigDevR5Cadence_Type())
pktcSigDevR5Cadence.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcSigDevR5Cadence.setStatus(_A)
_PktcSigDevR6Cadence_Type=PktcRingCadence
_PktcSigDevR6Cadence_Object=MibScalar
pktcSigDevR6Cadence=_PktcSigDevR6Cadence_Object((1,3,6,1,4,1,7432,2,1,1,11),_PktcSigDevR6Cadence_Type())
pktcSigDevR6Cadence.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcSigDevR6Cadence.setStatus(_A)
_PktcSigDevR7Cadence_Type=PktcRingCadence
_PktcSigDevR7Cadence_Object=MibScalar
pktcSigDevR7Cadence=_PktcSigDevR7Cadence_Object((1,3,6,1,4,1,7432,2,1,1,12),_PktcSigDevR7Cadence_Type())
pktcSigDevR7Cadence.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcSigDevR7Cadence.setStatus(_A)
_PktcSigDevRgCadence_Type=PktcRingCadence
_PktcSigDevRgCadence_Object=MibScalar
pktcSigDevRgCadence=_PktcSigDevRgCadence_Object((1,3,6,1,4,1,7432,2,1,1,13),_PktcSigDevRgCadence_Type())
pktcSigDevRgCadence.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcSigDevRgCadence.setStatus(_A)
_PktcSigDevRsCadence_Type=PktcRingCadence
_PktcSigDevRsCadence_Object=MibScalar
pktcSigDevRsCadence=_PktcSigDevRsCadence_Object((1,3,6,1,4,1,7432,2,1,1,14),_PktcSigDevRsCadence_Type())
pktcSigDevRsCadence.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcSigDevRsCadence.setStatus(_A)
class _PktcSigDefCallSigDscp_Type(Dscp):defaultValue=0
_PktcSigDefCallSigDscp_Type.__name__=_K
_PktcSigDefCallSigDscp_Object=MibScalar
pktcSigDefCallSigDscp=_PktcSigDefCallSigDscp_Object((1,3,6,1,4,1,7432,2,1,1,15),_PktcSigDefCallSigDscp_Type())
pktcSigDefCallSigDscp.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcSigDefCallSigDscp.setStatus(_A)
class _PktcSigDefMediaStreamDscp_Type(Dscp):defaultValue=0
_PktcSigDefMediaStreamDscp_Type.__name__=_K
_PktcSigDefMediaStreamDscp_Object=MibScalar
pktcSigDefMediaStreamDscp=_PktcSigDefMediaStreamDscp_Object((1,3,6,1,4,1,7432,2,1,1,16),_PktcSigDefMediaStreamDscp_Type())
pktcSigDefMediaStreamDscp.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcSigDefMediaStreamDscp.setStatus(_A)
_PktcSigCapabilityTable_Object=MibTable
pktcSigCapabilityTable=_PktcSigCapabilityTable_Object((1,3,6,1,4,1,7432,2,1,1,17))
if mibBuilder.loadTexts:pktcSigCapabilityTable.setStatus(_A)
_PktcSigCapabilityEntry_Object=MibTableRow
pktcSigCapabilityEntry=_PktcSigCapabilityEntry_Object((1,3,6,1,4,1,7432,2,1,1,17,1))
pktcSigCapabilityEntry.setIndexNames((0,_B,_V))
if mibBuilder.loadTexts:pktcSigCapabilityEntry.setStatus(_A)
class _PktcSignalingIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_PktcSignalingIndex_Type.__name__=_C
_PktcSignalingIndex_Object=MibTableColumn
pktcSignalingIndex=_PktcSignalingIndex_Object((1,3,6,1,4,1,7432,2,1,1,17,1,1),_PktcSignalingIndex_Type())
pktcSignalingIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:pktcSignalingIndex.setStatus(_A)
_PktcSignalingType_Type=PktcSigType
_PktcSignalingType_Object=MibTableColumn
pktcSignalingType=_PktcSignalingType_Object((1,3,6,1,4,1,7432,2,1,1,17,1,2),_PktcSignalingType_Type())
pktcSignalingType.setMaxAccess(_I)
if mibBuilder.loadTexts:pktcSignalingType.setStatus(_A)
_PktcSignalingVersion_Type=SnmpAdminString
_PktcSignalingVersion_Object=MibTableColumn
pktcSignalingVersion=_PktcSignalingVersion_Object((1,3,6,1,4,1,7432,2,1,1,17,1,3),_PktcSignalingVersion_Type())
pktcSignalingVersion.setMaxAccess(_I)
if mibBuilder.loadTexts:pktcSignalingVersion.setStatus(_A)
_PktcSignalingVendorExtension_Type=SnmpAdminString
_PktcSignalingVendorExtension_Object=MibTableColumn
pktcSignalingVendorExtension=_PktcSignalingVendorExtension_Object((1,3,6,1,4,1,7432,2,1,1,17,1,4),_PktcSignalingVendorExtension_Type())
pktcSignalingVendorExtension.setMaxAccess(_I)
if mibBuilder.loadTexts:pktcSignalingVendorExtension.setStatus(_A)
class _PktcSigDefNcsReceiveUdpPort_Type(InetPortNumber):defaultValue=2427;subtypeSpec=InetPortNumber.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1025,65535))
_PktcSigDefNcsReceiveUdpPort_Type.__name__=_L
_PktcSigDefNcsReceiveUdpPort_Object=MibScalar
pktcSigDefNcsReceiveUdpPort=_PktcSigDefNcsReceiveUdpPort_Object((1,3,6,1,4,1,7432,2,1,1,18),_PktcSigDefNcsReceiveUdpPort_Type())
pktcSigDefNcsReceiveUdpPort.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcSigDefNcsReceiveUdpPort.setStatus(_A)
class _PktcSigPowerRingFrequency_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('f20Hz',1),('f25Hz',2),('f33Point33Hz',3),('f50Hz',4),('f15Hz',5),('f16Hz',6),('f22Hz',7),('f23Hz',8),('f45Hz',9)))
_PktcSigPowerRingFrequency_Type.__name__=_H
_PktcSigPowerRingFrequency_Object=MibScalar
pktcSigPowerRingFrequency=_PktcSigPowerRingFrequency_Object((1,3,6,1,4,1,7432,2,1,1,19),_PktcSigPowerRingFrequency_Type())
pktcSigPowerRingFrequency.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcSigPowerRingFrequency.setStatus(_A)
if mibBuilder.loadTexts:pktcSigPowerRingFrequency.setUnits('Hertz')
_PktcSigPulseSignalTable_Object=MibTable
pktcSigPulseSignalTable=_PktcSigPulseSignalTable_Object((1,3,6,1,4,1,7432,2,1,1,20))
if mibBuilder.loadTexts:pktcSigPulseSignalTable.setStatus(_A)
_PktcSigPulseSignalEntry_Object=MibTableRow
pktcSigPulseSignalEntry=_PktcSigPulseSignalEntry_Object((1,3,6,1,4,1,7432,2,1,1,20,1))
pktcSigPulseSignalEntry.setIndexNames((0,_B,_W))
if mibBuilder.loadTexts:pktcSigPulseSignalEntry.setStatus(_A)
class _PktcSigPulseSignalType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('initialRing',1),('pulseLoopClose',2),('pulseLoopOpen',3),('enableMeterPulse',4),('meterPulseBurst',5),('pulseNoBattery',6),('pulseNormalPolarity',7),('pulseReducedBattery',8),('pulseReversePolarity',9)))
_PktcSigPulseSignalType_Type.__name__=_H
_PktcSigPulseSignalType_Object=MibTableColumn
pktcSigPulseSignalType=_PktcSigPulseSignalType_Object((1,3,6,1,4,1,7432,2,1,1,20,1,1),_PktcSigPulseSignalType_Type())
pktcSigPulseSignalType.setMaxAccess(_J)
if mibBuilder.loadTexts:pktcSigPulseSignalType.setStatus(_A)
class _PktcSigPulseSignalFrequency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('twentyfive',1),('twelvethousand',2),('sixteenthousand',3)))
_PktcSigPulseSignalFrequency_Type.__name__=_H
_PktcSigPulseSignalFrequency_Object=MibTableColumn
pktcSigPulseSignalFrequency=_PktcSigPulseSignalFrequency_Object((1,3,6,1,4,1,7432,2,1,1,20,1,2),_PktcSigPulseSignalFrequency_Type())
pktcSigPulseSignalFrequency.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcSigPulseSignalFrequency.setStatus(_A)
if mibBuilder.loadTexts:pktcSigPulseSignalFrequency.setUnits('Hertz')
class _PktcSigPulseSignalDbLevel_Type(TenthdBm):defaultValue=-135;subtypeSpec=TenthdBm.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-350,0))
_PktcSigPulseSignalDbLevel_Type.__name__=_N
_PktcSigPulseSignalDbLevel_Object=MibTableColumn
pktcSigPulseSignalDbLevel=_PktcSigPulseSignalDbLevel_Object((1,3,6,1,4,1,7432,2,1,1,20,1,3),_PktcSigPulseSignalDbLevel_Type())
pktcSigPulseSignalDbLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcSigPulseSignalDbLevel.setStatus(_A)
if mibBuilder.loadTexts:pktcSigPulseSignalDbLevel.setUnits('dBm')
class _PktcSigPulseSignalDuration_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5000))
_PktcSigPulseSignalDuration_Type.__name__=_C
_PktcSigPulseSignalDuration_Object=MibTableColumn
pktcSigPulseSignalDuration=_PktcSigPulseSignalDuration_Object((1,3,6,1,4,1,7432,2,1,1,20,1,4),_PktcSigPulseSignalDuration_Type())
pktcSigPulseSignalDuration.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcSigPulseSignalDuration.setStatus(_A)
if mibBuilder.loadTexts:pktcSigPulseSignalDuration.setUnits(_F)
class _PktcSigPulseSignalPulseInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5000))
_PktcSigPulseSignalPulseInterval_Type.__name__=_C
_PktcSigPulseSignalPulseInterval_Object=MibTableColumn
pktcSigPulseSignalPulseInterval=_PktcSigPulseSignalPulseInterval_Object((1,3,6,1,4,1,7432,2,1,1,20,1,5),_PktcSigPulseSignalPulseInterval_Type())
pktcSigPulseSignalPulseInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcSigPulseSignalPulseInterval.setStatus(_A)
if mibBuilder.loadTexts:pktcSigPulseSignalPulseInterval.setUnits(_F)
_PktcSigPulseSignalRepeatCount_Type=Unsigned32
_PktcSigPulseSignalRepeatCount_Object=MibTableColumn
pktcSigPulseSignalRepeatCount=_PktcSigPulseSignalRepeatCount_Object((1,3,6,1,4,1,7432,2,1,1,20,1,6),_PktcSigPulseSignalRepeatCount_Type())
pktcSigPulseSignalRepeatCount.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcSigPulseSignalRepeatCount.setStatus(_A)
class _PktcSigDevCIDMode_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('duringRingingETS',1),(_X,2),(_Y,3),(_Z,4),('lrETS',5)))
_PktcSigDevCIDMode_Type.__name__=_H
_PktcSigDevCIDMode_Object=MibScalar
pktcSigDevCIDMode=_PktcSigDevCIDMode_Object((1,3,6,1,4,1,7432,2,1,1,21),_PktcSigDevCIDMode_Type())
pktcSigDevCIDMode.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcSigDevCIDMode.setStatus(_A)
class _PktcSigDevCIDFskAfterRing_Type(Unsigned32):defaultValue=550;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,2000))
_PktcSigDevCIDFskAfterRing_Type.__name__=_C
_PktcSigDevCIDFskAfterRing_Object=MibScalar
pktcSigDevCIDFskAfterRing=_PktcSigDevCIDFskAfterRing_Object((1,3,6,1,4,1,7432,2,1,1,22),_PktcSigDevCIDFskAfterRing_Type())
pktcSigDevCIDFskAfterRing.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcSigDevCIDFskAfterRing.setStatus(_A)
if mibBuilder.loadTexts:pktcSigDevCIDFskAfterRing.setUnits(_F)
class _PktcSigDevCIDFskAfterDTAS_Type(Unsigned32):defaultValue=50;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(45,500))
_PktcSigDevCIDFskAfterDTAS_Type.__name__=_C
_PktcSigDevCIDFskAfterDTAS_Object=MibScalar
pktcSigDevCIDFskAfterDTAS=_PktcSigDevCIDFskAfterDTAS_Object((1,3,6,1,4,1,7432,2,1,1,23),_PktcSigDevCIDFskAfterDTAS_Type())
pktcSigDevCIDFskAfterDTAS.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcSigDevCIDFskAfterDTAS.setStatus(_A)
if mibBuilder.loadTexts:pktcSigDevCIDFskAfterDTAS.setUnits(_F)
class _PktcSigDevCIDFskAfterRPAS_Type(Unsigned32):defaultValue=650;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,800))
_PktcSigDevCIDFskAfterRPAS_Type.__name__=_C
_PktcSigDevCIDFskAfterRPAS_Object=MibScalar
pktcSigDevCIDFskAfterRPAS=_PktcSigDevCIDFskAfterRPAS_Object((1,3,6,1,4,1,7432,2,1,1,24),_PktcSigDevCIDFskAfterRPAS_Type())
pktcSigDevCIDFskAfterRPAS.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcSigDevCIDFskAfterRPAS.setStatus(_A)
if mibBuilder.loadTexts:pktcSigDevCIDFskAfterRPAS.setUnits(_F)
class _PktcSigDevCIDRingAfterFSK_Type(Unsigned32):defaultValue=250;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,500))
_PktcSigDevCIDRingAfterFSK_Type.__name__=_C
_PktcSigDevCIDRingAfterFSK_Object=MibScalar
pktcSigDevCIDRingAfterFSK=_PktcSigDevCIDRingAfterFSK_Object((1,3,6,1,4,1,7432,2,1,1,25),_PktcSigDevCIDRingAfterFSK_Type())
pktcSigDevCIDRingAfterFSK.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcSigDevCIDRingAfterFSK.setStatus(_A)
if mibBuilder.loadTexts:pktcSigDevCIDRingAfterFSK.setUnits(_F)
class _PktcSigDevCIDDTASAfterLR_Type(Unsigned32):defaultValue=250;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,655))
_PktcSigDevCIDDTASAfterLR_Type.__name__=_C
_PktcSigDevCIDDTASAfterLR_Object=MibScalar
pktcSigDevCIDDTASAfterLR=_PktcSigDevCIDDTASAfterLR_Object((1,3,6,1,4,1,7432,2,1,1,26),_PktcSigDevCIDDTASAfterLR_Type())
pktcSigDevCIDDTASAfterLR.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcSigDevCIDDTASAfterLR.setStatus(_A)
if mibBuilder.loadTexts:pktcSigDevCIDDTASAfterLR.setUnits(_F)
class _PktcSigDevVmwiMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_X,1),(_Y,2),(_Z,3),('osi',4),('lrETS',5)))
_PktcSigDevVmwiMode_Type.__name__=_H
_PktcSigDevVmwiMode_Object=MibScalar
pktcSigDevVmwiMode=_PktcSigDevVmwiMode_Object((1,3,6,1,4,1,7432,2,1,1,27),_PktcSigDevVmwiMode_Type())
pktcSigDevVmwiMode.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcSigDevVmwiMode.setStatus(_A)
class _PktcSigDevVmwiFskAfterDTAS_Type(Unsigned32):defaultValue=50;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(45,500))
_PktcSigDevVmwiFskAfterDTAS_Type.__name__=_C
_PktcSigDevVmwiFskAfterDTAS_Object=MibScalar
pktcSigDevVmwiFskAfterDTAS=_PktcSigDevVmwiFskAfterDTAS_Object((1,3,6,1,4,1,7432,2,1,1,28),_PktcSigDevVmwiFskAfterDTAS_Type())
pktcSigDevVmwiFskAfterDTAS.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcSigDevVmwiFskAfterDTAS.setStatus(_A)
if mibBuilder.loadTexts:pktcSigDevVmwiFskAfterDTAS.setUnits(_F)
class _PktcSigDevVmwiFskAfterRPAS_Type(Unsigned32):defaultValue=650;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,800))
_PktcSigDevVmwiFskAfterRPAS_Type.__name__=_C
_PktcSigDevVmwiFskAfterRPAS_Object=MibScalar
pktcSigDevVmwiFskAfterRPAS=_PktcSigDevVmwiFskAfterRPAS_Object((1,3,6,1,4,1,7432,2,1,1,29),_PktcSigDevVmwiFskAfterRPAS_Type())
pktcSigDevVmwiFskAfterRPAS.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcSigDevVmwiFskAfterRPAS.setStatus(_A)
if mibBuilder.loadTexts:pktcSigDevVmwiFskAfterRPAS.setUnits(_F)
class _PktcSigDevVmwiDTASAfterLR_Type(Unsigned32):defaultValue=250;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,655))
_PktcSigDevVmwiDTASAfterLR_Type.__name__=_C
_PktcSigDevVmwiDTASAfterLR_Object=MibScalar
pktcSigDevVmwiDTASAfterLR=_PktcSigDevVmwiDTASAfterLR_Object((1,3,6,1,4,1,7432,2,1,1,30),_PktcSigDevVmwiDTASAfterLR_Type())
pktcSigDevVmwiDTASAfterLR.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcSigDevVmwiDTASAfterLR.setStatus(_A)
if mibBuilder.loadTexts:pktcSigDevVmwiDTASAfterLR.setUnits(_F)
_PktcSigDevRingCadenceTable_Object=MibTable
pktcSigDevRingCadenceTable=_PktcSigDevRingCadenceTable_Object((1,3,6,1,4,1,7432,2,1,1,31))
if mibBuilder.loadTexts:pktcSigDevRingCadenceTable.setStatus(_A)
_PktcSigDevRingCadenceEntry_Object=MibTableRow
pktcSigDevRingCadenceEntry=_PktcSigDevRingCadenceEntry_Object((1,3,6,1,4,1,7432,2,1,1,31,1))
pktcSigDevRingCadenceEntry.setIndexNames((0,_B,_a))
if mibBuilder.loadTexts:pktcSigDevRingCadenceEntry.setStatus(_A)
class _PktcSigDevRingCadenceIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_PktcSigDevRingCadenceIndex_Type.__name__=_C
_PktcSigDevRingCadenceIndex_Object=MibTableColumn
pktcSigDevRingCadenceIndex=_PktcSigDevRingCadenceIndex_Object((1,3,6,1,4,1,7432,2,1,1,31,1,1),_PktcSigDevRingCadenceIndex_Type())
pktcSigDevRingCadenceIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:pktcSigDevRingCadenceIndex.setStatus(_A)
_PktcSigDevRingCadence_Type=PktcRingCadence
_PktcSigDevRingCadence_Object=MibTableColumn
pktcSigDevRingCadence=_PktcSigDevRingCadence_Object((1,3,6,1,4,1,7432,2,1,1,31,1,2),_PktcSigDevRingCadence_Type())
pktcSigDevRingCadence.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcSigDevRingCadence.setStatus(_A)
_PktcSigDevToneTable_Object=MibTable
pktcSigDevToneTable=_PktcSigDevToneTable_Object((1,3,6,1,4,1,7432,2,1,1,32))
if mibBuilder.loadTexts:pktcSigDevToneTable.setStatus(_A)
_PktcSigDevToneEntry_Object=MibTableRow
pktcSigDevToneEntry=_PktcSigDevToneEntry_Object((1,3,6,1,4,1,7432,2,1,1,32,1))
pktcSigDevToneEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:pktcSigDevToneEntry.setStatus(_A)
class _PktcSigDevToneType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21)));namedValues=NamedValues(*(('busy',1),('confirmation',2),('dial',3),('messageWaiting',4),('offHookWarning',5),('ringBack',6),('reOrder',7),('stutterdial',8),('callWaiting1',9),('callWaiting2',10),('callWaiting3',11),('callWaiting4',12),('alertingSignal',13),('specialDial',14),('specialInfo',15),('release',16),('congestion',17),('userDefined1',18),('userDefined2',19),('userDefined3',20),('userDefined4',21)))
_PktcSigDevToneType_Type.__name__=_H
_PktcSigDevToneType_Object=MibTableColumn
pktcSigDevToneType=_PktcSigDevToneType_Object((1,3,6,1,4,1,7432,2,1,1,32,1,1),_PktcSigDevToneType_Type())
pktcSigDevToneType.setMaxAccess(_J)
if mibBuilder.loadTexts:pktcSigDevToneType.setStatus(_A)
class _PktcSigDevToneWholeToneRepeatCount_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5000))
_PktcSigDevToneWholeToneRepeatCount_Type.__name__=_C
_PktcSigDevToneWholeToneRepeatCount_Object=MibTableColumn
pktcSigDevToneWholeToneRepeatCount=_PktcSigDevToneWholeToneRepeatCount_Object((1,3,6,1,4,1,7432,2,1,1,32,1,2),_PktcSigDevToneWholeToneRepeatCount_Type())
pktcSigDevToneWholeToneRepeatCount.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcSigDevToneWholeToneRepeatCount.setStatus(_A)
_PktcSigDevToneSteady_Type=TruthValue
_PktcSigDevToneSteady_Object=MibTableColumn
pktcSigDevToneSteady=_PktcSigDevToneSteady_Object((1,3,6,1,4,1,7432,2,1,1,32,1,3),_PktcSigDevToneSteady_Type())
pktcSigDevToneSteady.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcSigDevToneSteady.setStatus(_A)
_PktcSigDevMultiFreqToneTable_Object=MibTable
pktcSigDevMultiFreqToneTable=_PktcSigDevMultiFreqToneTable_Object((1,3,6,1,4,1,7432,2,1,1,33))
if mibBuilder.loadTexts:pktcSigDevMultiFreqToneTable.setStatus(_A)
_PktcSigDevMultiFreqToneEntry_Object=MibTableRow
pktcSigDevMultiFreqToneEntry=_PktcSigDevMultiFreqToneEntry_Object((1,3,6,1,4,1,7432,2,1,1,33,1))
pktcSigDevMultiFreqToneEntry.setIndexNames((0,_B,_O),(0,_B,_b))
if mibBuilder.loadTexts:pktcSigDevMultiFreqToneEntry.setStatus(_A)
class _PktcSigDevToneNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_PktcSigDevToneNumber_Type.__name__=_C
_PktcSigDevToneNumber_Object=MibTableColumn
pktcSigDevToneNumber=_PktcSigDevToneNumber_Object((1,3,6,1,4,1,7432,2,1,1,33,1,1),_PktcSigDevToneNumber_Type())
pktcSigDevToneNumber.setMaxAccess(_J)
if mibBuilder.loadTexts:pktcSigDevToneNumber.setStatus(_A)
class _PktcSigDevToneFirstFreqValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4000))
_PktcSigDevToneFirstFreqValue_Type.__name__=_C
_PktcSigDevToneFirstFreqValue_Object=MibTableColumn
pktcSigDevToneFirstFreqValue=_PktcSigDevToneFirstFreqValue_Object((1,3,6,1,4,1,7432,2,1,1,33,1,2),_PktcSigDevToneFirstFreqValue_Type())
pktcSigDevToneFirstFreqValue.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcSigDevToneFirstFreqValue.setStatus(_A)
class _PktcSigDevToneSecondFreqValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4000))
_PktcSigDevToneSecondFreqValue_Type.__name__=_C
_PktcSigDevToneSecondFreqValue_Object=MibTableColumn
pktcSigDevToneSecondFreqValue=_PktcSigDevToneSecondFreqValue_Object((1,3,6,1,4,1,7432,2,1,1,33,1,3),_PktcSigDevToneSecondFreqValue_Type())
pktcSigDevToneSecondFreqValue.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcSigDevToneSecondFreqValue.setStatus(_A)
class _PktcSigDevToneThirdFreqValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4000))
_PktcSigDevToneThirdFreqValue_Type.__name__=_C
_PktcSigDevToneThirdFreqValue_Object=MibTableColumn
pktcSigDevToneThirdFreqValue=_PktcSigDevToneThirdFreqValue_Object((1,3,6,1,4,1,7432,2,1,1,33,1,4),_PktcSigDevToneThirdFreqValue_Type())
pktcSigDevToneThirdFreqValue.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcSigDevToneThirdFreqValue.setStatus(_A)
class _PktcSigDevToneFourthFreqValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4000))
_PktcSigDevToneFourthFreqValue_Type.__name__=_C
_PktcSigDevToneFourthFreqValue_Object=MibTableColumn
pktcSigDevToneFourthFreqValue=_PktcSigDevToneFourthFreqValue_Object((1,3,6,1,4,1,7432,2,1,1,33,1,5),_PktcSigDevToneFourthFreqValue_Type())
pktcSigDevToneFourthFreqValue.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcSigDevToneFourthFreqValue.setStatus(_A)
class _PktcSigDevToneFreqMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('firstModulatedBySecond',1),('summation',2)))
_PktcSigDevToneFreqMode_Type.__name__=_H
_PktcSigDevToneFreqMode_Object=MibTableColumn
pktcSigDevToneFreqMode=_PktcSigDevToneFreqMode_Object((1,3,6,1,4,1,7432,2,1,1,33,1,6),_PktcSigDevToneFreqMode_Type())
pktcSigDevToneFreqMode.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcSigDevToneFreqMode.setStatus(_A)
class _PktcSigDevToneFreqAmpModePrtg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_PktcSigDevToneFreqAmpModePrtg_Type.__name__=_H
_PktcSigDevToneFreqAmpModePrtg_Object=MibTableColumn
pktcSigDevToneFreqAmpModePrtg=_PktcSigDevToneFreqAmpModePrtg_Object((1,3,6,1,4,1,7432,2,1,1,33,1,7),_PktcSigDevToneFreqAmpModePrtg_Type())
pktcSigDevToneFreqAmpModePrtg.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcSigDevToneFreqAmpModePrtg.setStatus(_A)
class _PktcSigDevToneDbLevel_Type(TenthdBm):defaultValue=-40;subtypeSpec=TenthdBm.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-250,-30))
_PktcSigDevToneDbLevel_Type.__name__=_N
_PktcSigDevToneDbLevel_Object=MibTableColumn
pktcSigDevToneDbLevel=_PktcSigDevToneDbLevel_Object((1,3,6,1,4,1,7432,2,1,1,33,1,8),_PktcSigDevToneDbLevel_Type())
pktcSigDevToneDbLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcSigDevToneDbLevel.setStatus(_A)
if mibBuilder.loadTexts:pktcSigDevToneDbLevel.setUnits('dBm')
class _PktcSigDevToneFreqOnDuration_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5000))
_PktcSigDevToneFreqOnDuration_Type.__name__=_C
_PktcSigDevToneFreqOnDuration_Object=MibTableColumn
pktcSigDevToneFreqOnDuration=_PktcSigDevToneFreqOnDuration_Object((1,3,6,1,4,1,7432,2,1,1,33,1,9),_PktcSigDevToneFreqOnDuration_Type())
pktcSigDevToneFreqOnDuration.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcSigDevToneFreqOnDuration.setStatus(_A)
class _PktcSigDevToneFreqOffDuration_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5000))
_PktcSigDevToneFreqOffDuration_Type.__name__=_C
_PktcSigDevToneFreqOffDuration_Object=MibTableColumn
pktcSigDevToneFreqOffDuration=_PktcSigDevToneFreqOffDuration_Object((1,3,6,1,4,1,7432,2,1,1,33,1,10),_PktcSigDevToneFreqOffDuration_Type())
pktcSigDevToneFreqOffDuration.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcSigDevToneFreqOffDuration.setStatus(_A)
class _PktcSigDevToneFreqRepeatCount_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5000))
_PktcSigDevToneFreqRepeatCount_Type.__name__=_C
_PktcSigDevToneFreqRepeatCount_Object=MibTableColumn
pktcSigDevToneFreqRepeatCount=_PktcSigDevToneFreqRepeatCount_Object((1,3,6,1,4,1,7432,2,1,1,33,1,11),_PktcSigDevToneFreqRepeatCount_Type())
pktcSigDevToneFreqRepeatCount.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcSigDevToneFreqRepeatCount.setStatus(_A)
_PktcNcsEndPntConfigObjects_ObjectIdentity=ObjectIdentity
pktcNcsEndPntConfigObjects=_PktcNcsEndPntConfigObjects_ObjectIdentity((1,3,6,1,4,1,7432,2,1,2))
_PktcNcsEndPntConfigTable_Object=MibTable
pktcNcsEndPntConfigTable=_PktcNcsEndPntConfigTable_Object((1,3,6,1,4,1,7432,2,1,2,1))
if mibBuilder.loadTexts:pktcNcsEndPntConfigTable.setStatus(_A)
_PktcNcsEndPntConfigEntry_Object=MibTableRow
pktcNcsEndPntConfigEntry=_PktcNcsEndPntConfigEntry_Object((1,3,6,1,4,1,7432,2,1,2,1,1))
pktcNcsEndPntConfigEntry.setIndexNames((0,_P,_Q))
if mibBuilder.loadTexts:pktcNcsEndPntConfigEntry.setStatus(_A)
class _PktcNcsEndPntConfigCallAgentId_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,255))
_PktcNcsEndPntConfigCallAgentId_Type.__name__=_R
_PktcNcsEndPntConfigCallAgentId_Object=MibTableColumn
pktcNcsEndPntConfigCallAgentId=_PktcNcsEndPntConfigCallAgentId_Object((1,3,6,1,4,1,7432,2,1,2,1,1,1),_PktcNcsEndPntConfigCallAgentId_Type())
pktcNcsEndPntConfigCallAgentId.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcNcsEndPntConfigCallAgentId.setStatus(_A)
class _PktcNcsEndPntConfigCallAgentUdpPort_Type(InetPortNumber):defaultValue=2727;subtypeSpec=InetPortNumber.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1025,65535))
_PktcNcsEndPntConfigCallAgentUdpPort_Type.__name__=_L
_PktcNcsEndPntConfigCallAgentUdpPort_Object=MibTableColumn
pktcNcsEndPntConfigCallAgentUdpPort=_PktcNcsEndPntConfigCallAgentUdpPort_Object((1,3,6,1,4,1,7432,2,1,2,1,1,2),_PktcNcsEndPntConfigCallAgentUdpPort_Type())
pktcNcsEndPntConfigCallAgentUdpPort.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcNcsEndPntConfigCallAgentUdpPort.setStatus(_A)
class _PktcNcsEndPntConfigPartialDialTO_Type(Unsigned32):defaultValue=16
_PktcNcsEndPntConfigPartialDialTO_Type.__name__=_C
_PktcNcsEndPntConfigPartialDialTO_Object=MibTableColumn
pktcNcsEndPntConfigPartialDialTO=_PktcNcsEndPntConfigPartialDialTO_Object((1,3,6,1,4,1,7432,2,1,2,1,1,3),_PktcNcsEndPntConfigPartialDialTO_Type())
pktcNcsEndPntConfigPartialDialTO.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcNcsEndPntConfigPartialDialTO.setStatus(_A)
if mibBuilder.loadTexts:pktcNcsEndPntConfigPartialDialTO.setUnits(_G)
class _PktcNcsEndPntConfigCriticalDialTO_Type(Unsigned32):defaultValue=4
_PktcNcsEndPntConfigCriticalDialTO_Type.__name__=_C
_PktcNcsEndPntConfigCriticalDialTO_Object=MibTableColumn
pktcNcsEndPntConfigCriticalDialTO=_PktcNcsEndPntConfigCriticalDialTO_Object((1,3,6,1,4,1,7432,2,1,2,1,1,4),_PktcNcsEndPntConfigCriticalDialTO_Type())
pktcNcsEndPntConfigCriticalDialTO.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcNcsEndPntConfigCriticalDialTO.setStatus(_A)
if mibBuilder.loadTexts:pktcNcsEndPntConfigCriticalDialTO.setUnits(_G)
class _PktcNcsEndPntConfigBusyToneTO_Type(Unsigned32):defaultValue=30
_PktcNcsEndPntConfigBusyToneTO_Type.__name__=_C
_PktcNcsEndPntConfigBusyToneTO_Object=MibTableColumn
pktcNcsEndPntConfigBusyToneTO=_PktcNcsEndPntConfigBusyToneTO_Object((1,3,6,1,4,1,7432,2,1,2,1,1,5),_PktcNcsEndPntConfigBusyToneTO_Type())
pktcNcsEndPntConfigBusyToneTO.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcNcsEndPntConfigBusyToneTO.setStatus(_A)
if mibBuilder.loadTexts:pktcNcsEndPntConfigBusyToneTO.setUnits(_G)
class _PktcNcsEndPntConfigDialToneTO_Type(Unsigned32):defaultValue=16
_PktcNcsEndPntConfigDialToneTO_Type.__name__=_C
_PktcNcsEndPntConfigDialToneTO_Object=MibTableColumn
pktcNcsEndPntConfigDialToneTO=_PktcNcsEndPntConfigDialToneTO_Object((1,3,6,1,4,1,7432,2,1,2,1,1,6),_PktcNcsEndPntConfigDialToneTO_Type())
pktcNcsEndPntConfigDialToneTO.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcNcsEndPntConfigDialToneTO.setStatus(_A)
if mibBuilder.loadTexts:pktcNcsEndPntConfigDialToneTO.setUnits(_G)
class _PktcNcsEndPntConfigMessageWaitingTO_Type(Unsigned32):defaultValue=16
_PktcNcsEndPntConfigMessageWaitingTO_Type.__name__=_C
_PktcNcsEndPntConfigMessageWaitingTO_Object=MibTableColumn
pktcNcsEndPntConfigMessageWaitingTO=_PktcNcsEndPntConfigMessageWaitingTO_Object((1,3,6,1,4,1,7432,2,1,2,1,1,7),_PktcNcsEndPntConfigMessageWaitingTO_Type())
pktcNcsEndPntConfigMessageWaitingTO.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcNcsEndPntConfigMessageWaitingTO.setStatus(_A)
if mibBuilder.loadTexts:pktcNcsEndPntConfigMessageWaitingTO.setUnits(_G)
class _PktcNcsEndPntConfigOffHookWarnToneTO_Type(Unsigned32):defaultValue=0
_PktcNcsEndPntConfigOffHookWarnToneTO_Type.__name__=_C
_PktcNcsEndPntConfigOffHookWarnToneTO_Object=MibTableColumn
pktcNcsEndPntConfigOffHookWarnToneTO=_PktcNcsEndPntConfigOffHookWarnToneTO_Object((1,3,6,1,4,1,7432,2,1,2,1,1,8),_PktcNcsEndPntConfigOffHookWarnToneTO_Type())
pktcNcsEndPntConfigOffHookWarnToneTO.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcNcsEndPntConfigOffHookWarnToneTO.setStatus(_A)
if mibBuilder.loadTexts:pktcNcsEndPntConfigOffHookWarnToneTO.setUnits(_G)
class _PktcNcsEndPntConfigRingingTO_Type(Unsigned32):defaultValue=180
_PktcNcsEndPntConfigRingingTO_Type.__name__=_C
_PktcNcsEndPntConfigRingingTO_Object=MibTableColumn
pktcNcsEndPntConfigRingingTO=_PktcNcsEndPntConfigRingingTO_Object((1,3,6,1,4,1,7432,2,1,2,1,1,9),_PktcNcsEndPntConfigRingingTO_Type())
pktcNcsEndPntConfigRingingTO.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcNcsEndPntConfigRingingTO.setStatus(_A)
if mibBuilder.loadTexts:pktcNcsEndPntConfigRingingTO.setUnits(_G)
class _PktcNcsEndPntConfigRingBackTO_Type(Unsigned32):defaultValue=180
_PktcNcsEndPntConfigRingBackTO_Type.__name__=_C
_PktcNcsEndPntConfigRingBackTO_Object=MibTableColumn
pktcNcsEndPntConfigRingBackTO=_PktcNcsEndPntConfigRingBackTO_Object((1,3,6,1,4,1,7432,2,1,2,1,1,10),_PktcNcsEndPntConfigRingBackTO_Type())
pktcNcsEndPntConfigRingBackTO.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcNcsEndPntConfigRingBackTO.setStatus(_A)
if mibBuilder.loadTexts:pktcNcsEndPntConfigRingBackTO.setUnits(_G)
class _PktcNcsEndPntConfigReorderToneTO_Type(Unsigned32):defaultValue=30
_PktcNcsEndPntConfigReorderToneTO_Type.__name__=_C
_PktcNcsEndPntConfigReorderToneTO_Object=MibTableColumn
pktcNcsEndPntConfigReorderToneTO=_PktcNcsEndPntConfigReorderToneTO_Object((1,3,6,1,4,1,7432,2,1,2,1,1,11),_PktcNcsEndPntConfigReorderToneTO_Type())
pktcNcsEndPntConfigReorderToneTO.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcNcsEndPntConfigReorderToneTO.setStatus(_A)
if mibBuilder.loadTexts:pktcNcsEndPntConfigReorderToneTO.setUnits(_G)
class _PktcNcsEndPntConfigStutterDialToneTO_Type(Unsigned32):defaultValue=16
_PktcNcsEndPntConfigStutterDialToneTO_Type.__name__=_C
_PktcNcsEndPntConfigStutterDialToneTO_Object=MibTableColumn
pktcNcsEndPntConfigStutterDialToneTO=_PktcNcsEndPntConfigStutterDialToneTO_Object((1,3,6,1,4,1,7432,2,1,2,1,1,12),_PktcNcsEndPntConfigStutterDialToneTO_Type())
pktcNcsEndPntConfigStutterDialToneTO.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcNcsEndPntConfigStutterDialToneTO.setStatus(_A)
if mibBuilder.loadTexts:pktcNcsEndPntConfigStutterDialToneTO.setUnits(_G)
class _PktcNcsEndPntConfigTSMax_Type(Unsigned32):defaultValue=20
_PktcNcsEndPntConfigTSMax_Type.__name__=_C
_PktcNcsEndPntConfigTSMax_Object=MibTableColumn
pktcNcsEndPntConfigTSMax=_PktcNcsEndPntConfigTSMax_Object((1,3,6,1,4,1,7432,2,1,2,1,1,13),_PktcNcsEndPntConfigTSMax_Type())
pktcNcsEndPntConfigTSMax.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcNcsEndPntConfigTSMax.setStatus(_A)
class _PktcNcsEndPntConfigMax1_Type(Unsigned32):defaultValue=5
_PktcNcsEndPntConfigMax1_Type.__name__=_C
_PktcNcsEndPntConfigMax1_Object=MibTableColumn
pktcNcsEndPntConfigMax1=_PktcNcsEndPntConfigMax1_Object((1,3,6,1,4,1,7432,2,1,2,1,1,14),_PktcNcsEndPntConfigMax1_Type())
pktcNcsEndPntConfigMax1.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcNcsEndPntConfigMax1.setStatus(_A)
class _PktcNcsEndPntConfigMax2_Type(Unsigned32):defaultValue=7
_PktcNcsEndPntConfigMax2_Type.__name__=_C
_PktcNcsEndPntConfigMax2_Object=MibTableColumn
pktcNcsEndPntConfigMax2=_PktcNcsEndPntConfigMax2_Object((1,3,6,1,4,1,7432,2,1,2,1,1,15),_PktcNcsEndPntConfigMax2_Type())
pktcNcsEndPntConfigMax2.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcNcsEndPntConfigMax2.setStatus(_A)
class _PktcNcsEndPntConfigMax1QEnable_Type(TruthValue):defaultValue=1
_PktcNcsEndPntConfigMax1QEnable_Type.__name__=_M
_PktcNcsEndPntConfigMax1QEnable_Object=MibTableColumn
pktcNcsEndPntConfigMax1QEnable=_PktcNcsEndPntConfigMax1QEnable_Object((1,3,6,1,4,1,7432,2,1,2,1,1,16),_PktcNcsEndPntConfigMax1QEnable_Type())
pktcNcsEndPntConfigMax1QEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcNcsEndPntConfigMax1QEnable.setStatus(_A)
class _PktcNcsEndPntConfigMax2QEnable_Type(TruthValue):defaultValue=1
_PktcNcsEndPntConfigMax2QEnable_Type.__name__=_M
_PktcNcsEndPntConfigMax2QEnable_Object=MibTableColumn
pktcNcsEndPntConfigMax2QEnable=_PktcNcsEndPntConfigMax2QEnable_Object((1,3,6,1,4,1,7432,2,1,2,1,1,17),_PktcNcsEndPntConfigMax2QEnable_Type())
pktcNcsEndPntConfigMax2QEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcNcsEndPntConfigMax2QEnable.setStatus(_A)
class _PktcNcsEndPntConfigMWD_Type(Unsigned32):defaultValue=600
_PktcNcsEndPntConfigMWD_Type.__name__=_C
_PktcNcsEndPntConfigMWD_Object=MibTableColumn
pktcNcsEndPntConfigMWD=_PktcNcsEndPntConfigMWD_Object((1,3,6,1,4,1,7432,2,1,2,1,1,18),_PktcNcsEndPntConfigMWD_Type())
pktcNcsEndPntConfigMWD.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcNcsEndPntConfigMWD.setStatus(_A)
if mibBuilder.loadTexts:pktcNcsEndPntConfigMWD.setUnits(_G)
class _PktcNcsEndPntConfigTdinit_Type(Unsigned32):defaultValue=15
_PktcNcsEndPntConfigTdinit_Type.__name__=_C
_PktcNcsEndPntConfigTdinit_Object=MibTableColumn
pktcNcsEndPntConfigTdinit=_PktcNcsEndPntConfigTdinit_Object((1,3,6,1,4,1,7432,2,1,2,1,1,19),_PktcNcsEndPntConfigTdinit_Type())
pktcNcsEndPntConfigTdinit.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcNcsEndPntConfigTdinit.setStatus(_A)
if mibBuilder.loadTexts:pktcNcsEndPntConfigTdinit.setUnits(_G)
class _PktcNcsEndPntConfigTdmin_Type(Unsigned32):defaultValue=15
_PktcNcsEndPntConfigTdmin_Type.__name__=_C
_PktcNcsEndPntConfigTdmin_Object=MibTableColumn
pktcNcsEndPntConfigTdmin=_PktcNcsEndPntConfigTdmin_Object((1,3,6,1,4,1,7432,2,1,2,1,1,20),_PktcNcsEndPntConfigTdmin_Type())
pktcNcsEndPntConfigTdmin.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcNcsEndPntConfigTdmin.setStatus(_A)
if mibBuilder.loadTexts:pktcNcsEndPntConfigTdmin.setUnits(_G)
class _PktcNcsEndPntConfigTdmax_Type(Unsigned32):defaultValue=600
_PktcNcsEndPntConfigTdmax_Type.__name__=_C
_PktcNcsEndPntConfigTdmax_Object=MibTableColumn
pktcNcsEndPntConfigTdmax=_PktcNcsEndPntConfigTdmax_Object((1,3,6,1,4,1,7432,2,1,2,1,1,21),_PktcNcsEndPntConfigTdmax_Type())
pktcNcsEndPntConfigTdmax.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcNcsEndPntConfigTdmax.setStatus(_A)
if mibBuilder.loadTexts:pktcNcsEndPntConfigTdmax.setUnits(_G)
class _PktcNcsEndPntConfigRtoMax_Type(Unsigned32):defaultValue=4
_PktcNcsEndPntConfigRtoMax_Type.__name__=_C
_PktcNcsEndPntConfigRtoMax_Object=MibTableColumn
pktcNcsEndPntConfigRtoMax=_PktcNcsEndPntConfigRtoMax_Object((1,3,6,1,4,1,7432,2,1,2,1,1,22),_PktcNcsEndPntConfigRtoMax_Type())
pktcNcsEndPntConfigRtoMax.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcNcsEndPntConfigRtoMax.setStatus(_A)
if mibBuilder.loadTexts:pktcNcsEndPntConfigRtoMax.setUnits(_G)
class _PktcNcsEndPntConfigRtoInit_Type(Unsigned32):defaultValue=200
_PktcNcsEndPntConfigRtoInit_Type.__name__=_C
_PktcNcsEndPntConfigRtoInit_Object=MibTableColumn
pktcNcsEndPntConfigRtoInit=_PktcNcsEndPntConfigRtoInit_Object((1,3,6,1,4,1,7432,2,1,2,1,1,23),_PktcNcsEndPntConfigRtoInit_Type())
pktcNcsEndPntConfigRtoInit.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcNcsEndPntConfigRtoInit.setStatus(_A)
if mibBuilder.loadTexts:pktcNcsEndPntConfigRtoInit.setUnits('milliseconds')
class _PktcNcsEndPntConfigLongDurationKeepAlive_Type(Unsigned32):defaultValue=60
_PktcNcsEndPntConfigLongDurationKeepAlive_Type.__name__=_C
_PktcNcsEndPntConfigLongDurationKeepAlive_Object=MibTableColumn
pktcNcsEndPntConfigLongDurationKeepAlive=_PktcNcsEndPntConfigLongDurationKeepAlive_Object((1,3,6,1,4,1,7432,2,1,2,1,1,24),_PktcNcsEndPntConfigLongDurationKeepAlive_Type())
pktcNcsEndPntConfigLongDurationKeepAlive.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcNcsEndPntConfigLongDurationKeepAlive.setStatus(_A)
if mibBuilder.loadTexts:pktcNcsEndPntConfigLongDurationKeepAlive.setUnits('minutes')
class _PktcNcsEndPntConfigThist_Type(Unsigned32):defaultValue=30
_PktcNcsEndPntConfigThist_Type.__name__=_C
_PktcNcsEndPntConfigThist_Object=MibTableColumn
pktcNcsEndPntConfigThist=_PktcNcsEndPntConfigThist_Object((1,3,6,1,4,1,7432,2,1,2,1,1,25),_PktcNcsEndPntConfigThist_Type())
pktcNcsEndPntConfigThist.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcNcsEndPntConfigThist.setStatus(_A)
if mibBuilder.loadTexts:pktcNcsEndPntConfigThist.setUnits(_G)
_PktcNcsEndPntConfigStatus_Type=RowStatus
_PktcNcsEndPntConfigStatus_Object=MibTableColumn
pktcNcsEndPntConfigStatus=_PktcNcsEndPntConfigStatus_Object((1,3,6,1,4,1,7432,2,1,2,1,1,26),_PktcNcsEndPntConfigStatus_Type())
pktcNcsEndPntConfigStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcNcsEndPntConfigStatus.setStatus(_A)
class _PktcNcsEndPntConfigCallWaitingMaxRep_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_PktcNcsEndPntConfigCallWaitingMaxRep_Type.__name__=_C
_PktcNcsEndPntConfigCallWaitingMaxRep_Object=MibTableColumn
pktcNcsEndPntConfigCallWaitingMaxRep=_PktcNcsEndPntConfigCallWaitingMaxRep_Object((1,3,6,1,4,1,7432,2,1,2,1,1,27),_PktcNcsEndPntConfigCallWaitingMaxRep_Type())
pktcNcsEndPntConfigCallWaitingMaxRep.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcNcsEndPntConfigCallWaitingMaxRep.setStatus(_A)
class _PktcNcsEndPntConfigCallWaitingDelay_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_PktcNcsEndPntConfigCallWaitingDelay_Type.__name__=_C
_PktcNcsEndPntConfigCallWaitingDelay_Object=MibTableColumn
pktcNcsEndPntConfigCallWaitingDelay=_PktcNcsEndPntConfigCallWaitingDelay_Object((1,3,6,1,4,1,7432,2,1,2,1,1,28),_PktcNcsEndPntConfigCallWaitingDelay_Type())
pktcNcsEndPntConfigCallWaitingDelay.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcNcsEndPntConfigCallWaitingDelay.setStatus(_A)
if mibBuilder.loadTexts:pktcNcsEndPntConfigCallWaitingDelay.setUnits(_G)
_PktcNcsEndPntStatusCallIpAddressType_Type=InetAddressType
_PktcNcsEndPntStatusCallIpAddressType_Object=MibTableColumn
pktcNcsEndPntStatusCallIpAddressType=_PktcNcsEndPntStatusCallIpAddressType_Object((1,3,6,1,4,1,7432,2,1,2,1,1,29),_PktcNcsEndPntStatusCallIpAddressType_Type())
pktcNcsEndPntStatusCallIpAddressType.setMaxAccess(_I)
if mibBuilder.loadTexts:pktcNcsEndPntStatusCallIpAddressType.setStatus(_A)
_PktcNcsEndPntStatusCallIpAddress_Type=InetAddress
_PktcNcsEndPntStatusCallIpAddress_Object=MibTableColumn
pktcNcsEndPntStatusCallIpAddress=_PktcNcsEndPntStatusCallIpAddress_Object((1,3,6,1,4,1,7432,2,1,2,1,1,30),_PktcNcsEndPntStatusCallIpAddress_Type())
pktcNcsEndPntStatusCallIpAddress.setMaxAccess(_I)
if mibBuilder.loadTexts:pktcNcsEndPntStatusCallIpAddress.setStatus(_A)
class _PktcNcsEndPntStatusError_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('operational',1),('noSecurityAssociation',2),('disconnected',3)))
_PktcNcsEndPntStatusError_Type.__name__=_H
_PktcNcsEndPntStatusError_Object=MibTableColumn
pktcNcsEndPntStatusError=_PktcNcsEndPntStatusError_Object((1,3,6,1,4,1,7432,2,1,2,1,1,31),_PktcNcsEndPntStatusError_Type())
pktcNcsEndPntStatusError.setMaxAccess(_I)
if mibBuilder.loadTexts:pktcNcsEndPntStatusError.setStatus(_A)
class _PktcNcsEndPntConfigMinHookFlash_Type(Unsigned32):defaultValue=300;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,1550))
_PktcNcsEndPntConfigMinHookFlash_Type.__name__=_C
_PktcNcsEndPntConfigMinHookFlash_Object=MibTableColumn
pktcNcsEndPntConfigMinHookFlash=_PktcNcsEndPntConfigMinHookFlash_Object((1,3,6,1,4,1,7432,2,1,2,1,1,32),_PktcNcsEndPntConfigMinHookFlash_Type())
pktcNcsEndPntConfigMinHookFlash.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcNcsEndPntConfigMinHookFlash.setStatus(_A)
if mibBuilder.loadTexts:pktcNcsEndPntConfigMinHookFlash.setUnits(_F)
class _PktcNcsEndPntConfigMaxHookFlash_Type(Unsigned32):defaultValue=800;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,1550))
_PktcNcsEndPntConfigMaxHookFlash_Type.__name__=_C
_PktcNcsEndPntConfigMaxHookFlash_Object=MibTableColumn
pktcNcsEndPntConfigMaxHookFlash=_PktcNcsEndPntConfigMaxHookFlash_Object((1,3,6,1,4,1,7432,2,1,2,1,1,33),_PktcNcsEndPntConfigMaxHookFlash_Type())
pktcNcsEndPntConfigMaxHookFlash.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcNcsEndPntConfigMaxHookFlash.setStatus(_A)
if mibBuilder.loadTexts:pktcNcsEndPntConfigMaxHookFlash.setUnits(_F)
class _PktcNcsEndPntConfigPulseDialInterdigitTime_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,1500))
_PktcNcsEndPntConfigPulseDialInterdigitTime_Type.__name__=_C
_PktcNcsEndPntConfigPulseDialInterdigitTime_Object=MibTableColumn
pktcNcsEndPntConfigPulseDialInterdigitTime=_PktcNcsEndPntConfigPulseDialInterdigitTime_Object((1,3,6,1,4,1,7432,2,1,2,1,1,34),_PktcNcsEndPntConfigPulseDialInterdigitTime_Type())
pktcNcsEndPntConfigPulseDialInterdigitTime.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcNcsEndPntConfigPulseDialInterdigitTime.setStatus(_A)
if mibBuilder.loadTexts:pktcNcsEndPntConfigPulseDialInterdigitTime.setUnits(_F)
class _PktcNcsEndPntConfigPulseDialMinMakeTime_Type(Unsigned32):defaultValue=25;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,200))
_PktcNcsEndPntConfigPulseDialMinMakeTime_Type.__name__=_C
_PktcNcsEndPntConfigPulseDialMinMakeTime_Object=MibTableColumn
pktcNcsEndPntConfigPulseDialMinMakeTime=_PktcNcsEndPntConfigPulseDialMinMakeTime_Object((1,3,6,1,4,1,7432,2,1,2,1,1,35),_PktcNcsEndPntConfigPulseDialMinMakeTime_Type())
pktcNcsEndPntConfigPulseDialMinMakeTime.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcNcsEndPntConfigPulseDialMinMakeTime.setStatus(_A)
if mibBuilder.loadTexts:pktcNcsEndPntConfigPulseDialMinMakeTime.setUnits(_F)
class _PktcNcsEndPntConfigPulseDialMaxMakeTime_Type(Unsigned32):defaultValue=55;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,200))
_PktcNcsEndPntConfigPulseDialMaxMakeTime_Type.__name__=_C
_PktcNcsEndPntConfigPulseDialMaxMakeTime_Object=MibTableColumn
pktcNcsEndPntConfigPulseDialMaxMakeTime=_PktcNcsEndPntConfigPulseDialMaxMakeTime_Object((1,3,6,1,4,1,7432,2,1,2,1,1,36),_PktcNcsEndPntConfigPulseDialMaxMakeTime_Type())
pktcNcsEndPntConfigPulseDialMaxMakeTime.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcNcsEndPntConfigPulseDialMaxMakeTime.setStatus(_A)
if mibBuilder.loadTexts:pktcNcsEndPntConfigPulseDialMaxMakeTime.setUnits(_F)
class _PktcNcsEndPntConfigPulseDialMinBreakTime_Type(Unsigned32):defaultValue=45;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,200))
_PktcNcsEndPntConfigPulseDialMinBreakTime_Type.__name__=_C
_PktcNcsEndPntConfigPulseDialMinBreakTime_Object=MibTableColumn
pktcNcsEndPntConfigPulseDialMinBreakTime=_PktcNcsEndPntConfigPulseDialMinBreakTime_Object((1,3,6,1,4,1,7432,2,1,2,1,1,37),_PktcNcsEndPntConfigPulseDialMinBreakTime_Type())
pktcNcsEndPntConfigPulseDialMinBreakTime.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcNcsEndPntConfigPulseDialMinBreakTime.setStatus(_A)
if mibBuilder.loadTexts:pktcNcsEndPntConfigPulseDialMinBreakTime.setUnits(_F)
class _PktcNcsEndPntConfigPulseDialMaxBreakTime_Type(Unsigned32):defaultValue=75;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,200))
_PktcNcsEndPntConfigPulseDialMaxBreakTime_Type.__name__=_C
_PktcNcsEndPntConfigPulseDialMaxBreakTime_Object=MibTableColumn
pktcNcsEndPntConfigPulseDialMaxBreakTime=_PktcNcsEndPntConfigPulseDialMaxBreakTime_Object((1,3,6,1,4,1,7432,2,1,2,1,1,38),_PktcNcsEndPntConfigPulseDialMaxBreakTime_Type())
pktcNcsEndPntConfigPulseDialMaxBreakTime.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcNcsEndPntConfigPulseDialMaxBreakTime.setStatus(_A)
if mibBuilder.loadTexts:pktcNcsEndPntConfigPulseDialMaxBreakTime.setUnits(_F)
_PktcSigConformance_ObjectIdentity=ObjectIdentity
pktcSigConformance=_PktcSigConformance_ObjectIdentity((1,3,6,1,4,1,7432,2,2))
_PktcSigCompliances_ObjectIdentity=ObjectIdentity
pktcSigCompliances=_PktcSigCompliances_ObjectIdentity((1,3,6,1,4,1,7432,2,2,1))
_PktcSigGroups_ObjectIdentity=ObjectIdentity
pktcSigGroups=_PktcSigGroups_ObjectIdentity((1,3,6,1,4,1,7432,2,2,2))
pktcSigGroup=ObjectGroup((1,3,6,1,4,1,7432,2,2,2,1))
pktcSigGroup.setObjects(*((_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v)))
if mibBuilder.loadTexts:pktcSigGroup.setStatus(_A)
pktcNcsGroup=ObjectGroup((1,3,6,1,4,1,7432,2,2,2,2))
pktcNcsGroup.setObjects(*((_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ)))
if mibBuilder.loadTexts:pktcNcsGroup.setStatus(_A)
pktcInternationalGroup=ObjectGroup((1,3,6,1,4,1,7432,2,2,2,3))
pktcInternationalGroup.setObjects(*((_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_Ah),(_B,_Ai),(_B,_Aj),(_B,_Ak),(_B,_Al),(_B,_Am),(_B,_An),(_B,_Ao),(_B,_Ap),(_B,_Aq),(_B,_Ar),(_B,_As),(_B,_At),(_B,_Au),(_B,_Av),(_B,_Aw),(_B,_Ax),(_B,_Ay),(_B,_Az),(_B,_A_)))
if mibBuilder.loadTexts:pktcInternationalGroup.setStatus(_A)
pktcSigBasicCompliance=ModuleCompliance((1,3,6,1,4,1,7432,2,2,1,1))
pktcSigBasicCompliance.setObjects(*((_B,_B0),(_B,_B1),(_B,_B2)))
if mibBuilder.loadTexts:pktcSigBasicCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_N:TenthdBm,'PktcCodecType':PktcCodecType,'PktcRingCadence':PktcRingCadence,'PktcSigType':PktcSigType,'pktcExcentisSigMib':pktcExcentisSigMib,'pktcSigNotification':pktcSigNotification,'pktcSigMibObjects':pktcSigMibObjects,'pktcSigDevConfigObjects':pktcSigDevConfigObjects,'pktcSigDevCodecTable':pktcSigDevCodecTable,'pktcSigDevCodecEntry':pktcSigDevCodecEntry,_T:pktcSigDevCodecComboIndex,_U:pktcSigDevCodecType,_c:pktcSigDevCodecMax,_d:pktcSigDevEchoCancellation,_e:pktcSigDevSilenceSuppression,_AZ:pktcSigDevCallerIdSigProtocol,_f:pktcSigDevR0Cadence,_g:pktcSigDevR1Cadence,_h:pktcSigDevR2Cadence,_i:pktcSigDevR3Cadence,_j:pktcSigDevR4Cadence,_k:pktcSigDevR5Cadence,_l:pktcSigDevR6Cadence,_m:pktcSigDevR7Cadence,_n:pktcSigDevRgCadence,_o:pktcSigDevRsCadence,_p:pktcSigDefCallSigDscp,_q:pktcSigDefMediaStreamDscp,'pktcSigCapabilityTable':pktcSigCapabilityTable,'pktcSigCapabilityEntry':pktcSigCapabilityEntry,_V:pktcSignalingIndex,_s:pktcSignalingType,_t:pktcSignalingVersion,_u:pktcSignalingVendorExtension,_v:pktcSigDefNcsReceiveUdpPort,_Aj:pktcSigPowerRingFrequency,'pktcSigPulseSignalTable':pktcSigPulseSignalTable,'pktcSigPulseSignalEntry':pktcSigPulseSignalEntry,_W:pktcSigPulseSignalType,_Ak:pktcSigPulseSignalFrequency,_Al:pktcSigPulseSignalDbLevel,_Am:pktcSigPulseSignalDuration,_An:pktcSigPulseSignalPulseInterval,_Ao:pktcSigPulseSignalRepeatCount,_Aa:pktcSigDevCIDMode,_Ab:pktcSigDevCIDFskAfterRing,_Ac:pktcSigDevCIDFskAfterDTAS,_Ad:pktcSigDevCIDFskAfterRPAS,_Ae:pktcSigDevCIDRingAfterFSK,_Af:pktcSigDevCIDDTASAfterLR,_r:pktcSigDevVmwiMode,_Ag:pktcSigDevVmwiFskAfterDTAS,_Ah:pktcSigDevVmwiFskAfterRPAS,_Ai:pktcSigDevVmwiDTASAfterLR,'pktcSigDevRingCadenceTable':pktcSigDevRingCadenceTable,'pktcSigDevRingCadenceEntry':pktcSigDevRingCadenceEntry,_a:pktcSigDevRingCadenceIndex,_AY:pktcSigDevRingCadence,'pktcSigDevToneTable':pktcSigDevToneTable,'pktcSigDevToneEntry':pktcSigDevToneEntry,_O:pktcSigDevToneType,_Aq:pktcSigDevToneWholeToneRepeatCount,_Ar:pktcSigDevToneSteady,'pktcSigDevMultiFreqToneTable':pktcSigDevMultiFreqToneTable,'pktcSigDevMultiFreqToneEntry':pktcSigDevMultiFreqToneEntry,_b:pktcSigDevToneNumber,_As:pktcSigDevToneFirstFreqValue,_At:pktcSigDevToneSecondFreqValue,_Au:pktcSigDevToneThirdFreqValue,_Av:pktcSigDevToneFourthFreqValue,_Aw:pktcSigDevToneFreqMode,_Ax:pktcSigDevToneFreqAmpModePrtg,_Ap:pktcSigDevToneDbLevel,_Ay:pktcSigDevToneFreqOnDuration,_Az:pktcSigDevToneFreqOffDuration,_A_:pktcSigDevToneFreqRepeatCount,'pktcNcsEndPntConfigObjects':pktcNcsEndPntConfigObjects,'pktcNcsEndPntConfigTable':pktcNcsEndPntConfigTable,'pktcNcsEndPntConfigEntry':pktcNcsEndPntConfigEntry,_w:pktcNcsEndPntConfigCallAgentId,_x:pktcNcsEndPntConfigCallAgentUdpPort,_y:pktcNcsEndPntConfigPartialDialTO,_z:pktcNcsEndPntConfigCriticalDialTO,_A0:pktcNcsEndPntConfigBusyToneTO,_A1:pktcNcsEndPntConfigDialToneTO,_A2:pktcNcsEndPntConfigMessageWaitingTO,_A3:pktcNcsEndPntConfigOffHookWarnToneTO,_A4:pktcNcsEndPntConfigRingingTO,_A5:pktcNcsEndPntConfigRingBackTO,_A6:pktcNcsEndPntConfigReorderToneTO,_A7:pktcNcsEndPntConfigStutterDialToneTO,_A8:pktcNcsEndPntConfigTSMax,_A9:pktcNcsEndPntConfigMax1,_AA:pktcNcsEndPntConfigMax2,_AB:pktcNcsEndPntConfigMax1QEnable,_AC:pktcNcsEndPntConfigMax2QEnable,_AD:pktcNcsEndPntConfigMWD,_AE:pktcNcsEndPntConfigTdinit,_AF:pktcNcsEndPntConfigTdmin,_AG:pktcNcsEndPntConfigTdmax,_AH:pktcNcsEndPntConfigRtoMax,_AI:pktcNcsEndPntConfigRtoInit,_AJ:pktcNcsEndPntConfigLongDurationKeepAlive,_AK:pktcNcsEndPntConfigThist,_AL:pktcNcsEndPntConfigStatus,_AM:pktcNcsEndPntConfigCallWaitingMaxRep,_AN:pktcNcsEndPntConfigCallWaitingDelay,_AO:pktcNcsEndPntStatusCallIpAddressType,_AP:pktcNcsEndPntStatusCallIpAddress,_AQ:pktcNcsEndPntStatusError,_AR:pktcNcsEndPntConfigMinHookFlash,_AS:pktcNcsEndPntConfigMaxHookFlash,_AT:pktcNcsEndPntConfigPulseDialInterdigitTime,_AU:pktcNcsEndPntConfigPulseDialMinMakeTime,_AV:pktcNcsEndPntConfigPulseDialMaxMakeTime,_AW:pktcNcsEndPntConfigPulseDialMinBreakTime,_AX:pktcNcsEndPntConfigPulseDialMaxBreakTime,'pktcSigConformance':pktcSigConformance,'pktcSigCompliances':pktcSigCompliances,'pktcSigBasicCompliance':pktcSigBasicCompliance,'pktcSigGroups':pktcSigGroups,_B0:pktcSigGroup,_B1:pktcNcsGroup,_B2:pktcInternationalGroup})