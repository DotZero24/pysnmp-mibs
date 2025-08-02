_Ae='cAtmTrunkAal5ConnStatsMIBGroup'
_Ad='cAtmTrunkAal1ConnStatsMIBGroup'
_Ac='cAtmTrunkCidConnStatsMIBGroup'
_Ab='cAtmTrunkAal5MIBGroup'
_Aa='cAtmTrunkAal1MIBGroup'
_AZ='cAtmTrunkCidMIBGroup'
_AY='catmtAal5CounterClear'
_AX='catmtAal5LastResetTime'
_AW='catmtAal5NoByteAlignErrorFrames'
_AV='catmtAal5InvalidLongFrames'
_AU='catmtAal5InvalidShortFrames'
_AT='catmtAal5AbortSeqFrames'
_AS='catmtAal5InvalidFCSFrames'
_AR='catmtAal5EncBytesRxFromTDM'
_AQ='catmtAal5EncBytesTxToTDM'
_AP='catmtAal5FramesRxFromTDM'
_AO='catmtAal5FramesTxToTDM'
_AN='catmtAal5RcvdOctets'
_AM='catmtAal5SentOctets'
_AL='catmtAal5RcvdPackets'
_AK='catmtAal5SentPackets'
_AJ='catmtAal1CounterClear'
_AI='catmtAal1LastResetTime'
_AH='catmtAal1Jitter'
_AG='catmtAal1RxPayloadBytes'
_AF='catmtAal1TxPayloadBytes'
_AE='catmtAal1RxCells'
_AD='catmtAal1TxCells'
_AC='catmtCidCounterClear'
_AB='catmtCidLastResetTime'
_AA='catmtCidNx64RASTimeOutFrames'
_A9='catmtCidNx64NoByteAlignErrorFrames'
_A8='catmtCidNx64InvalidLongFrames'
_A7='catmtCidNx64InvalidShortFrames'
_A6='catmtCidNx64AbortSeqFrames'
_A5='catmtCidNx64InvalidFCSFrames'
_A4='catmtCidNx64EncBytesRxFromTDM'
_A3='catmtCidNx64EncBytesTxToTDM'
_A2='catmtCidNx64FramesRxFromTDM'
_A1='catmtCidNx64FramesTxToTDM'
_A0='catmtCidConnRDICnts'
_z='catmtCidConnAISCnts'
_y='catmtCidExtRAICnts'
_x='catmtCidExtAISCnts'
_w='catmtCidJitter'
_v='catmtCidLostPackets'
_u='catmtCidRcvdOctets'
_t='catmtCidSentOctets'
_s='catmtCidRcvdPackets'
_r='catmtCidSentPackets'
_q='catmtAal5RowStatus'
_p='catmtAal5Nx64Profile'
_o='catmtAal5Ds0GroupIndex'
_n='catmtAal5Ds1'
_m='catmtAal1RowStatus'
_l='catmtAal1Nx64Profile'
_k='catmtAal1Ds0GroupIndex'
_j='catmtAal1Ds1'
_i='catmtCidRowStatus'
_h='catmtCidRepetitionResult'
_g='catmtCidRepetitionOwner'
_f='catmtCidRepetition'
_e='catmtCidStateBitMap'
_d='catmtCidNx64Profile'
_c='catmtCidNx64Enable'
_b='catmtCidVBDCodec'
_a='catmtCidVoiceCodec'
_Z='catmtCidProfileNumber'
_Y='catmtCidProfileType'
_X='catmtCidDs0GroupIndex'
_W='catmtCidDs1'
_V='TruthValue'
_U='Gauge32'
_T='ConfigIterator'
_S='catmtAal5Vci'
_R='catmtAal5Vpi'
_Q='catmtAal1Vci'
_P='catmtAal1Vpi'
_O='read-write'
_N='catmtCid'
_M='catmtCidVci'
_L='catmtCidVpi'
_K='bytes'
_J='packets'
_I='not-accessible'
_H='Unsigned32'
_G='ifIndex'
_F='IF-MIB'
_E='Integer32'
_D='read-create'
_C='read-only'
_B='CISCO-ATM-TRUNK-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
BulkConfigResult,ConfigIterator=mibBuilder.importSymbols('CISCO-TC','BulkConfigResult',_T)
CiscoAal2ProfileNumber,CiscoAal2ProfileType=mibBuilder.importSymbols('CISCO-VOICE-AALX-PROFILE-MIB','CiscoAal2ProfileNumber','CiscoAal2ProfileType')
CvcCoderTypeRate,CvcSpeechCoderRate=mibBuilder.importSymbols('CISCO-VOICE-COMMON-DIAL-CONTROL-MIB','CvcCoderTypeRate','CvcSpeechCoderRate')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_F,'InterfaceIndex',_G)
OwnerString,=mibBuilder.importSymbols('RMON-MIB','OwnerString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_U,_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp',_V)
ciscoAtmTrunkMIB=ModuleIdentity((1,3,6,1,4,1,9,9,351))
if mibBuilder.loadTexts:ciscoAtmTrunkMIB.setRevisions(('2003-07-18 00:00',))
class Counter32SinceReset(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CAtmTrunkMIBNotifications_ObjectIdentity=ObjectIdentity
cAtmTrunkMIBNotifications=_CAtmTrunkMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,351,0))
_CAtmTrunkMIBObjects_ObjectIdentity=ObjectIdentity
cAtmTrunkMIBObjects=_CAtmTrunkMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,351,1))
_CAtmTrunkCidConfig_ObjectIdentity=ObjectIdentity
cAtmTrunkCidConfig=_CAtmTrunkCidConfig_ObjectIdentity((1,3,6,1,4,1,9,9,351,1,1))
_CatmtCidTable_Object=MibTable
catmtCidTable=_CatmtCidTable_Object((1,3,6,1,4,1,9,9,351,1,1,1))
if mibBuilder.loadTexts:catmtCidTable.setStatus(_A)
_CatmtCidEntry_Object=MibTableRow
catmtCidEntry=_CatmtCidEntry_Object((1,3,6,1,4,1,9,9,351,1,1,1,1))
catmtCidEntry.setIndexNames((0,_F,_G),(0,_B,_L),(0,_B,_M),(0,_B,_N))
if mibBuilder.loadTexts:catmtCidEntry.setStatus(_A)
class _CatmtCidVpi_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_CatmtCidVpi_Type.__name__=_H
_CatmtCidVpi_Object=MibTableColumn
catmtCidVpi=_CatmtCidVpi_Object((1,3,6,1,4,1,9,9,351,1,1,1,1,1),_CatmtCidVpi_Type())
catmtCidVpi.setMaxAccess(_I)
if mibBuilder.loadTexts:catmtCidVpi.setStatus(_A)
class _CatmtCidVci_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CatmtCidVci_Type.__name__=_H
_CatmtCidVci_Object=MibTableColumn
catmtCidVci=_CatmtCidVci_Object((1,3,6,1,4,1,9,9,351,1,1,1,1,2),_CatmtCidVci_Type())
catmtCidVci.setMaxAccess(_I)
if mibBuilder.loadTexts:catmtCidVci.setStatus(_A)
class _CatmtCid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8,255))
_CatmtCid_Type.__name__=_E
_CatmtCid_Object=MibTableColumn
catmtCid=_CatmtCid_Object((1,3,6,1,4,1,9,9,351,1,1,1,1,3),_CatmtCid_Type())
catmtCid.setMaxAccess(_I)
if mibBuilder.loadTexts:catmtCid.setStatus(_A)
_CatmtCidDs1_Type=InterfaceIndex
_CatmtCidDs1_Object=MibTableColumn
catmtCidDs1=_CatmtCidDs1_Object((1,3,6,1,4,1,9,9,351,1,1,1,1,4),_CatmtCidDs1_Type())
catmtCidDs1.setMaxAccess(_D)
if mibBuilder.loadTexts:catmtCidDs1.setStatus(_A)
class _CatmtCidDs0GroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30))
_CatmtCidDs0GroupIndex_Type.__name__=_E
_CatmtCidDs0GroupIndex_Object=MibTableColumn
catmtCidDs0GroupIndex=_CatmtCidDs0GroupIndex_Object((1,3,6,1,4,1,9,9,351,1,1,1,1,5),_CatmtCidDs0GroupIndex_Type())
catmtCidDs0GroupIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:catmtCidDs0GroupIndex.setStatus(_A)
_CatmtCidProfileType_Type=CiscoAal2ProfileType
_CatmtCidProfileType_Object=MibTableColumn
catmtCidProfileType=_CatmtCidProfileType_Object((1,3,6,1,4,1,9,9,351,1,1,1,1,6),_CatmtCidProfileType_Type())
catmtCidProfileType.setMaxAccess(_D)
if mibBuilder.loadTexts:catmtCidProfileType.setStatus(_A)
_CatmtCidProfileNumber_Type=CiscoAal2ProfileNumber
_CatmtCidProfileNumber_Object=MibTableColumn
catmtCidProfileNumber=_CatmtCidProfileNumber_Object((1,3,6,1,4,1,9,9,351,1,1,1,1,7),_CatmtCidProfileNumber_Type())
catmtCidProfileNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:catmtCidProfileNumber.setStatus(_A)
_CatmtCidVoiceCodec_Type=CvcSpeechCoderRate
_CatmtCidVoiceCodec_Object=MibTableColumn
catmtCidVoiceCodec=_CatmtCidVoiceCodec_Object((1,3,6,1,4,1,9,9,351,1,1,1,1,8),_CatmtCidVoiceCodec_Type())
catmtCidVoiceCodec.setMaxAccess(_D)
if mibBuilder.loadTexts:catmtCidVoiceCodec.setStatus(_A)
_CatmtCidVBDCodec_Type=CvcCoderTypeRate
_CatmtCidVBDCodec_Object=MibTableColumn
catmtCidVBDCodec=_CatmtCidVBDCodec_Object((1,3,6,1,4,1,9,9,351,1,1,1,1,9),_CatmtCidVBDCodec_Type())
catmtCidVBDCodec.setMaxAccess(_D)
if mibBuilder.loadTexts:catmtCidVBDCodec.setStatus(_A)
class _CatmtCidNx64Enable_Type(TruthValue):defaultValue=2
_CatmtCidNx64Enable_Type.__name__=_V
_CatmtCidNx64Enable_Object=MibTableColumn
catmtCidNx64Enable=_CatmtCidNx64Enable_Object((1,3,6,1,4,1,9,9,351,1,1,1,1,10),_CatmtCidNx64Enable_Type())
catmtCidNx64Enable.setMaxAccess(_D)
if mibBuilder.loadTexts:catmtCidNx64Enable.setStatus(_A)
class _CatmtCidNx64Profile_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CatmtCidNx64Profile_Type.__name__=_E
_CatmtCidNx64Profile_Object=MibTableColumn
catmtCidNx64Profile=_CatmtCidNx64Profile_Object((1,3,6,1,4,1,9,9,351,1,1,1,1,11),_CatmtCidNx64Profile_Type())
catmtCidNx64Profile.setMaxAccess(_D)
if mibBuilder.loadTexts:catmtCidNx64Profile.setStatus(_A)
class _CatmtCidStateBitMap_Type(Bits):namedValues=NamedValues(*(('pvcAdminDown',0),('pvcFailure',1),('extAIS',2),('extRAI',3),('aal2ConnAIS',4),('aal2ConnRDI',5),('lineAlarm',6)))
_CatmtCidStateBitMap_Type.__name__='Bits'
_CatmtCidStateBitMap_Object=MibTableColumn
catmtCidStateBitMap=_CatmtCidStateBitMap_Object((1,3,6,1,4,1,9,9,351,1,1,1,1,12),_CatmtCidStateBitMap_Type())
catmtCidStateBitMap.setMaxAccess(_C)
if mibBuilder.loadTexts:catmtCidStateBitMap.setStatus(_A)
class _CatmtCidRepetition_Type(ConfigIterator):defaultValue=1
_CatmtCidRepetition_Type.__name__=_T
_CatmtCidRepetition_Object=MibTableColumn
catmtCidRepetition=_CatmtCidRepetition_Object((1,3,6,1,4,1,9,9,351,1,1,1,1,13),_CatmtCidRepetition_Type())
catmtCidRepetition.setMaxAccess(_D)
if mibBuilder.loadTexts:catmtCidRepetition.setStatus(_A)
_CatmtCidRepetitionOwner_Type=OwnerString
_CatmtCidRepetitionOwner_Object=MibTableColumn
catmtCidRepetitionOwner=_CatmtCidRepetitionOwner_Object((1,3,6,1,4,1,9,9,351,1,1,1,1,14),_CatmtCidRepetitionOwner_Type())
catmtCidRepetitionOwner.setMaxAccess(_D)
if mibBuilder.loadTexts:catmtCidRepetitionOwner.setStatus(_A)
_CatmtCidRepetitionResult_Type=BulkConfigResult
_CatmtCidRepetitionResult_Object=MibTableColumn
catmtCidRepetitionResult=_CatmtCidRepetitionResult_Object((1,3,6,1,4,1,9,9,351,1,1,1,1,15),_CatmtCidRepetitionResult_Type())
catmtCidRepetitionResult.setMaxAccess(_C)
if mibBuilder.loadTexts:catmtCidRepetitionResult.setStatus(_A)
_CatmtCidRowStatus_Type=RowStatus
_CatmtCidRowStatus_Object=MibTableColumn
catmtCidRowStatus=_CatmtCidRowStatus_Object((1,3,6,1,4,1,9,9,351,1,1,1,1,16),_CatmtCidRowStatus_Type())
catmtCidRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:catmtCidRowStatus.setStatus(_A)
_CAtmTrunkCidConnStats_ObjectIdentity=ObjectIdentity
cAtmTrunkCidConnStats=_CAtmTrunkCidConnStats_ObjectIdentity((1,3,6,1,4,1,9,9,351,1,2))
_CatmtCidStatsTable_Object=MibTable
catmtCidStatsTable=_CatmtCidStatsTable_Object((1,3,6,1,4,1,9,9,351,1,2,1))
if mibBuilder.loadTexts:catmtCidStatsTable.setStatus(_A)
_CatmtCidStatsEntry_Object=MibTableRow
catmtCidStatsEntry=_CatmtCidStatsEntry_Object((1,3,6,1,4,1,9,9,351,1,2,1,1))
catmtCidStatsEntry.setIndexNames((0,_F,_G),(0,_B,_L),(0,_B,_M),(0,_B,_N))
if mibBuilder.loadTexts:catmtCidStatsEntry.setStatus(_A)
_CatmtCidSentPackets_Type=Counter32SinceReset
_CatmtCidSentPackets_Object=MibTableColumn
catmtCidSentPackets=_CatmtCidSentPackets_Object((1,3,6,1,4,1,9,9,351,1,2,1,1,1),_CatmtCidSentPackets_Type())
catmtCidSentPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:catmtCidSentPackets.setStatus(_A)
if mibBuilder.loadTexts:catmtCidSentPackets.setUnits(_J)
_CatmtCidRcvdPackets_Type=Counter32SinceReset
_CatmtCidRcvdPackets_Object=MibTableColumn
catmtCidRcvdPackets=_CatmtCidRcvdPackets_Object((1,3,6,1,4,1,9,9,351,1,2,1,1,2),_CatmtCidRcvdPackets_Type())
catmtCidRcvdPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:catmtCidRcvdPackets.setStatus(_A)
if mibBuilder.loadTexts:catmtCidRcvdPackets.setUnits(_J)
_CatmtCidSentOctets_Type=Counter32SinceReset
_CatmtCidSentOctets_Object=MibTableColumn
catmtCidSentOctets=_CatmtCidSentOctets_Object((1,3,6,1,4,1,9,9,351,1,2,1,1,3),_CatmtCidSentOctets_Type())
catmtCidSentOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:catmtCidSentOctets.setStatus(_A)
if mibBuilder.loadTexts:catmtCidSentOctets.setUnits(_K)
_CatmtCidRcvdOctets_Type=Counter32SinceReset
_CatmtCidRcvdOctets_Object=MibTableColumn
catmtCidRcvdOctets=_CatmtCidRcvdOctets_Object((1,3,6,1,4,1,9,9,351,1,2,1,1,4),_CatmtCidRcvdOctets_Type())
catmtCidRcvdOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:catmtCidRcvdOctets.setStatus(_A)
if mibBuilder.loadTexts:catmtCidRcvdOctets.setUnits(_K)
_CatmtCidLostPackets_Type=Counter32SinceReset
_CatmtCidLostPackets_Object=MibTableColumn
catmtCidLostPackets=_CatmtCidLostPackets_Object((1,3,6,1,4,1,9,9,351,1,2,1,1,5),_CatmtCidLostPackets_Type())
catmtCidLostPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:catmtCidLostPackets.setStatus(_A)
if mibBuilder.loadTexts:catmtCidLostPackets.setUnits(_J)
class _CatmtCidJitter_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CatmtCidJitter_Type.__name__=_U
_CatmtCidJitter_Object=MibTableColumn
catmtCidJitter=_CatmtCidJitter_Object((1,3,6,1,4,1,9,9,351,1,2,1,1,6),_CatmtCidJitter_Type())
catmtCidJitter.setMaxAccess(_C)
if mibBuilder.loadTexts:catmtCidJitter.setStatus(_A)
if mibBuilder.loadTexts:catmtCidJitter.setUnits('milliseconds')
_CatmtCidExtAISCnts_Type=Counter32SinceReset
_CatmtCidExtAISCnts_Object=MibTableColumn
catmtCidExtAISCnts=_CatmtCidExtAISCnts_Object((1,3,6,1,4,1,9,9,351,1,2,1,1,7),_CatmtCidExtAISCnts_Type())
catmtCidExtAISCnts.setMaxAccess(_C)
if mibBuilder.loadTexts:catmtCidExtAISCnts.setStatus(_A)
_CatmtCidExtRAICnts_Type=Counter32SinceReset
_CatmtCidExtRAICnts_Object=MibTableColumn
catmtCidExtRAICnts=_CatmtCidExtRAICnts_Object((1,3,6,1,4,1,9,9,351,1,2,1,1,8),_CatmtCidExtRAICnts_Type())
catmtCidExtRAICnts.setMaxAccess(_C)
if mibBuilder.loadTexts:catmtCidExtRAICnts.setStatus(_A)
_CatmtCidConnAISCnts_Type=Counter32SinceReset
_CatmtCidConnAISCnts_Object=MibTableColumn
catmtCidConnAISCnts=_CatmtCidConnAISCnts_Object((1,3,6,1,4,1,9,9,351,1,2,1,1,9),_CatmtCidConnAISCnts_Type())
catmtCidConnAISCnts.setMaxAccess(_C)
if mibBuilder.loadTexts:catmtCidConnAISCnts.setStatus(_A)
_CatmtCidConnRDICnts_Type=Counter32SinceReset
_CatmtCidConnRDICnts_Object=MibTableColumn
catmtCidConnRDICnts=_CatmtCidConnRDICnts_Object((1,3,6,1,4,1,9,9,351,1,2,1,1,10),_CatmtCidConnRDICnts_Type())
catmtCidConnRDICnts.setMaxAccess(_C)
if mibBuilder.loadTexts:catmtCidConnRDICnts.setStatus(_A)
_CatmtCidNx64FramesTxToTDM_Type=Counter32SinceReset
_CatmtCidNx64FramesTxToTDM_Object=MibTableColumn
catmtCidNx64FramesTxToTDM=_CatmtCidNx64FramesTxToTDM_Object((1,3,6,1,4,1,9,9,351,1,2,1,1,11),_CatmtCidNx64FramesTxToTDM_Type())
catmtCidNx64FramesTxToTDM.setMaxAccess(_C)
if mibBuilder.loadTexts:catmtCidNx64FramesTxToTDM.setStatus(_A)
_CatmtCidNx64FramesRxFromTDM_Type=Counter32SinceReset
_CatmtCidNx64FramesRxFromTDM_Object=MibTableColumn
catmtCidNx64FramesRxFromTDM=_CatmtCidNx64FramesRxFromTDM_Object((1,3,6,1,4,1,9,9,351,1,2,1,1,12),_CatmtCidNx64FramesRxFromTDM_Type())
catmtCidNx64FramesRxFromTDM.setMaxAccess(_C)
if mibBuilder.loadTexts:catmtCidNx64FramesRxFromTDM.setStatus(_A)
_CatmtCidNx64EncBytesTxToTDM_Type=Counter32SinceReset
_CatmtCidNx64EncBytesTxToTDM_Object=MibTableColumn
catmtCidNx64EncBytesTxToTDM=_CatmtCidNx64EncBytesTxToTDM_Object((1,3,6,1,4,1,9,9,351,1,2,1,1,13),_CatmtCidNx64EncBytesTxToTDM_Type())
catmtCidNx64EncBytesTxToTDM.setMaxAccess(_C)
if mibBuilder.loadTexts:catmtCidNx64EncBytesTxToTDM.setStatus(_A)
_CatmtCidNx64EncBytesRxFromTDM_Type=Counter32SinceReset
_CatmtCidNx64EncBytesRxFromTDM_Object=MibTableColumn
catmtCidNx64EncBytesRxFromTDM=_CatmtCidNx64EncBytesRxFromTDM_Object((1,3,6,1,4,1,9,9,351,1,2,1,1,14),_CatmtCidNx64EncBytesRxFromTDM_Type())
catmtCidNx64EncBytesRxFromTDM.setMaxAccess(_C)
if mibBuilder.loadTexts:catmtCidNx64EncBytesRxFromTDM.setStatus(_A)
_CatmtCidNx64InvalidFCSFrames_Type=Counter32SinceReset
_CatmtCidNx64InvalidFCSFrames_Object=MibTableColumn
catmtCidNx64InvalidFCSFrames=_CatmtCidNx64InvalidFCSFrames_Object((1,3,6,1,4,1,9,9,351,1,2,1,1,15),_CatmtCidNx64InvalidFCSFrames_Type())
catmtCidNx64InvalidFCSFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:catmtCidNx64InvalidFCSFrames.setStatus(_A)
_CatmtCidNx64AbortSeqFrames_Type=Counter32SinceReset
_CatmtCidNx64AbortSeqFrames_Object=MibTableColumn
catmtCidNx64AbortSeqFrames=_CatmtCidNx64AbortSeqFrames_Object((1,3,6,1,4,1,9,9,351,1,2,1,1,16),_CatmtCidNx64AbortSeqFrames_Type())
catmtCidNx64AbortSeqFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:catmtCidNx64AbortSeqFrames.setStatus(_A)
_CatmtCidNx64InvalidShortFrames_Type=Counter32SinceReset
_CatmtCidNx64InvalidShortFrames_Object=MibTableColumn
catmtCidNx64InvalidShortFrames=_CatmtCidNx64InvalidShortFrames_Object((1,3,6,1,4,1,9,9,351,1,2,1,1,17),_CatmtCidNx64InvalidShortFrames_Type())
catmtCidNx64InvalidShortFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:catmtCidNx64InvalidShortFrames.setStatus(_A)
_CatmtCidNx64InvalidLongFrames_Type=Counter32SinceReset
_CatmtCidNx64InvalidLongFrames_Object=MibTableColumn
catmtCidNx64InvalidLongFrames=_CatmtCidNx64InvalidLongFrames_Object((1,3,6,1,4,1,9,9,351,1,2,1,1,18),_CatmtCidNx64InvalidLongFrames_Type())
catmtCidNx64InvalidLongFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:catmtCidNx64InvalidLongFrames.setStatus(_A)
_CatmtCidNx64NoByteAlignErrorFrames_Type=Counter32SinceReset
_CatmtCidNx64NoByteAlignErrorFrames_Object=MibTableColumn
catmtCidNx64NoByteAlignErrorFrames=_CatmtCidNx64NoByteAlignErrorFrames_Object((1,3,6,1,4,1,9,9,351,1,2,1,1,19),_CatmtCidNx64NoByteAlignErrorFrames_Type())
catmtCidNx64NoByteAlignErrorFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:catmtCidNx64NoByteAlignErrorFrames.setStatus(_A)
_CatmtCidNx64RASTimeOutFrames_Type=Counter32SinceReset
_CatmtCidNx64RASTimeOutFrames_Object=MibTableColumn
catmtCidNx64RASTimeOutFrames=_CatmtCidNx64RASTimeOutFrames_Object((1,3,6,1,4,1,9,9,351,1,2,1,1,20),_CatmtCidNx64RASTimeOutFrames_Type())
catmtCidNx64RASTimeOutFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:catmtCidNx64RASTimeOutFrames.setStatus(_A)
_CatmtCidLastResetTime_Type=TimeStamp
_CatmtCidLastResetTime_Object=MibTableColumn
catmtCidLastResetTime=_CatmtCidLastResetTime_Object((1,3,6,1,4,1,9,9,351,1,2,1,1,21),_CatmtCidLastResetTime_Type())
catmtCidLastResetTime.setMaxAccess(_C)
if mibBuilder.loadTexts:catmtCidLastResetTime.setStatus(_A)
_CatmtCidCounterClear_Type=TruthValue
_CatmtCidCounterClear_Object=MibTableColumn
catmtCidCounterClear=_CatmtCidCounterClear_Object((1,3,6,1,4,1,9,9,351,1,2,1,1,22),_CatmtCidCounterClear_Type())
catmtCidCounterClear.setMaxAccess(_O)
if mibBuilder.loadTexts:catmtCidCounterClear.setStatus(_A)
_CAtmTrunkAal1Config_ObjectIdentity=ObjectIdentity
cAtmTrunkAal1Config=_CAtmTrunkAal1Config_ObjectIdentity((1,3,6,1,4,1,9,9,351,1,3))
_CatmtAal1Table_Object=MibTable
catmtAal1Table=_CatmtAal1Table_Object((1,3,6,1,4,1,9,9,351,1,3,1))
if mibBuilder.loadTexts:catmtAal1Table.setStatus(_A)
_CatmtAal1Entry_Object=MibTableRow
catmtAal1Entry=_CatmtAal1Entry_Object((1,3,6,1,4,1,9,9,351,1,3,1,1))
catmtAal1Entry.setIndexNames((0,_F,_G),(0,_B,_P),(0,_B,_Q))
if mibBuilder.loadTexts:catmtAal1Entry.setStatus(_A)
class _CatmtAal1Vpi_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_CatmtAal1Vpi_Type.__name__=_H
_CatmtAal1Vpi_Object=MibTableColumn
catmtAal1Vpi=_CatmtAal1Vpi_Object((1,3,6,1,4,1,9,9,351,1,3,1,1,1),_CatmtAal1Vpi_Type())
catmtAal1Vpi.setMaxAccess(_I)
if mibBuilder.loadTexts:catmtAal1Vpi.setStatus(_A)
class _CatmtAal1Vci_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CatmtAal1Vci_Type.__name__=_H
_CatmtAal1Vci_Object=MibTableColumn
catmtAal1Vci=_CatmtAal1Vci_Object((1,3,6,1,4,1,9,9,351,1,3,1,1,2),_CatmtAal1Vci_Type())
catmtAal1Vci.setMaxAccess(_I)
if mibBuilder.loadTexts:catmtAal1Vci.setStatus(_A)
_CatmtAal1Ds1_Type=InterfaceIndex
_CatmtAal1Ds1_Object=MibTableColumn
catmtAal1Ds1=_CatmtAal1Ds1_Object((1,3,6,1,4,1,9,9,351,1,3,1,1,3),_CatmtAal1Ds1_Type())
catmtAal1Ds1.setMaxAccess(_D)
if mibBuilder.loadTexts:catmtAal1Ds1.setStatus(_A)
class _CatmtAal1Ds0GroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30))
_CatmtAal1Ds0GroupIndex_Type.__name__=_E
_CatmtAal1Ds0GroupIndex_Object=MibTableColumn
catmtAal1Ds0GroupIndex=_CatmtAal1Ds0GroupIndex_Object((1,3,6,1,4,1,9,9,351,1,3,1,1,4),_CatmtAal1Ds0GroupIndex_Type())
catmtAal1Ds0GroupIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:catmtAal1Ds0GroupIndex.setStatus(_A)
class _CatmtAal1Nx64Profile_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CatmtAal1Nx64Profile_Type.__name__=_E
_CatmtAal1Nx64Profile_Object=MibTableColumn
catmtAal1Nx64Profile=_CatmtAal1Nx64Profile_Object((1,3,6,1,4,1,9,9,351,1,3,1,1,5),_CatmtAal1Nx64Profile_Type())
catmtAal1Nx64Profile.setMaxAccess(_D)
if mibBuilder.loadTexts:catmtAal1Nx64Profile.setStatus(_A)
_CatmtAal1RowStatus_Type=RowStatus
_CatmtAal1RowStatus_Object=MibTableColumn
catmtAal1RowStatus=_CatmtAal1RowStatus_Object((1,3,6,1,4,1,9,9,351,1,3,1,1,6),_CatmtAal1RowStatus_Type())
catmtAal1RowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:catmtAal1RowStatus.setStatus(_A)
_CAtmTrunkAal1ConnStats_ObjectIdentity=ObjectIdentity
cAtmTrunkAal1ConnStats=_CAtmTrunkAal1ConnStats_ObjectIdentity((1,3,6,1,4,1,9,9,351,1,4))
_CatmtAal1StatsTable_Object=MibTable
catmtAal1StatsTable=_CatmtAal1StatsTable_Object((1,3,6,1,4,1,9,9,351,1,4,1))
if mibBuilder.loadTexts:catmtAal1StatsTable.setStatus(_A)
_CatmtAal1StatsEntry_Object=MibTableRow
catmtAal1StatsEntry=_CatmtAal1StatsEntry_Object((1,3,6,1,4,1,9,9,351,1,4,1,1))
catmtAal1StatsEntry.setIndexNames((0,_F,_G),(0,_B,_P),(0,_B,_Q))
if mibBuilder.loadTexts:catmtAal1StatsEntry.setStatus(_A)
_CatmtAal1TxCells_Type=Counter32SinceReset
_CatmtAal1TxCells_Object=MibTableColumn
catmtAal1TxCells=_CatmtAal1TxCells_Object((1,3,6,1,4,1,9,9,351,1,4,1,1,1),_CatmtAal1TxCells_Type())
catmtAal1TxCells.setMaxAccess(_C)
if mibBuilder.loadTexts:catmtAal1TxCells.setStatus(_A)
_CatmtAal1RxCells_Type=Counter32SinceReset
_CatmtAal1RxCells_Object=MibTableColumn
catmtAal1RxCells=_CatmtAal1RxCells_Object((1,3,6,1,4,1,9,9,351,1,4,1,1,2),_CatmtAal1RxCells_Type())
catmtAal1RxCells.setMaxAccess(_C)
if mibBuilder.loadTexts:catmtAal1RxCells.setStatus(_A)
_CatmtAal1TxPayloadBytes_Type=Counter32SinceReset
_CatmtAal1TxPayloadBytes_Object=MibTableColumn
catmtAal1TxPayloadBytes=_CatmtAal1TxPayloadBytes_Object((1,3,6,1,4,1,9,9,351,1,4,1,1,3),_CatmtAal1TxPayloadBytes_Type())
catmtAal1TxPayloadBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:catmtAal1TxPayloadBytes.setStatus(_A)
_CatmtAal1RxPayloadBytes_Type=Counter32SinceReset
_CatmtAal1RxPayloadBytes_Object=MibTableColumn
catmtAal1RxPayloadBytes=_CatmtAal1RxPayloadBytes_Object((1,3,6,1,4,1,9,9,351,1,4,1,1,4),_CatmtAal1RxPayloadBytes_Type())
catmtAal1RxPayloadBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:catmtAal1RxPayloadBytes.setStatus(_A)
_CatmtAal1Jitter_Type=Gauge32
_CatmtAal1Jitter_Object=MibTableColumn
catmtAal1Jitter=_CatmtAal1Jitter_Object((1,3,6,1,4,1,9,9,351,1,4,1,1,5),_CatmtAal1Jitter_Type())
catmtAal1Jitter.setMaxAccess(_C)
if mibBuilder.loadTexts:catmtAal1Jitter.setStatus(_A)
_CatmtAal1LastResetTime_Type=TimeStamp
_CatmtAal1LastResetTime_Object=MibTableColumn
catmtAal1LastResetTime=_CatmtAal1LastResetTime_Object((1,3,6,1,4,1,9,9,351,1,4,1,1,6),_CatmtAal1LastResetTime_Type())
catmtAal1LastResetTime.setMaxAccess(_C)
if mibBuilder.loadTexts:catmtAal1LastResetTime.setStatus(_A)
_CatmtAal1CounterClear_Type=TruthValue
_CatmtAal1CounterClear_Object=MibTableColumn
catmtAal1CounterClear=_CatmtAal1CounterClear_Object((1,3,6,1,4,1,9,9,351,1,4,1,1,7),_CatmtAal1CounterClear_Type())
catmtAal1CounterClear.setMaxAccess(_O)
if mibBuilder.loadTexts:catmtAal1CounterClear.setStatus(_A)
_CAtmTrunkAal5Config_ObjectIdentity=ObjectIdentity
cAtmTrunkAal5Config=_CAtmTrunkAal5Config_ObjectIdentity((1,3,6,1,4,1,9,9,351,1,5))
_CatmtAal5Table_Object=MibTable
catmtAal5Table=_CatmtAal5Table_Object((1,3,6,1,4,1,9,9,351,1,5,1))
if mibBuilder.loadTexts:catmtAal5Table.setStatus(_A)
_CatmtAal5Entry_Object=MibTableRow
catmtAal5Entry=_CatmtAal5Entry_Object((1,3,6,1,4,1,9,9,351,1,5,1,1))
catmtAal5Entry.setIndexNames((0,_F,_G),(0,_B,_R),(0,_B,_S))
if mibBuilder.loadTexts:catmtAal5Entry.setStatus(_A)
class _CatmtAal5Vpi_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_CatmtAal5Vpi_Type.__name__=_H
_CatmtAal5Vpi_Object=MibTableColumn
catmtAal5Vpi=_CatmtAal5Vpi_Object((1,3,6,1,4,1,9,9,351,1,5,1,1,1),_CatmtAal5Vpi_Type())
catmtAal5Vpi.setMaxAccess(_I)
if mibBuilder.loadTexts:catmtAal5Vpi.setStatus(_A)
class _CatmtAal5Vci_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CatmtAal5Vci_Type.__name__=_H
_CatmtAal5Vci_Object=MibTableColumn
catmtAal5Vci=_CatmtAal5Vci_Object((1,3,6,1,4,1,9,9,351,1,5,1,1,2),_CatmtAal5Vci_Type())
catmtAal5Vci.setMaxAccess(_I)
if mibBuilder.loadTexts:catmtAal5Vci.setStatus(_A)
_CatmtAal5Ds1_Type=InterfaceIndex
_CatmtAal5Ds1_Object=MibTableColumn
catmtAal5Ds1=_CatmtAal5Ds1_Object((1,3,6,1,4,1,9,9,351,1,5,1,1,3),_CatmtAal5Ds1_Type())
catmtAal5Ds1.setMaxAccess(_D)
if mibBuilder.loadTexts:catmtAal5Ds1.setStatus(_A)
class _CatmtAal5Ds0GroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30))
_CatmtAal5Ds0GroupIndex_Type.__name__=_E
_CatmtAal5Ds0GroupIndex_Object=MibTableColumn
catmtAal5Ds0GroupIndex=_CatmtAal5Ds0GroupIndex_Object((1,3,6,1,4,1,9,9,351,1,5,1,1,4),_CatmtAal5Ds0GroupIndex_Type())
catmtAal5Ds0GroupIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:catmtAal5Ds0GroupIndex.setStatus(_A)
class _CatmtAal5Nx64Profile_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CatmtAal5Nx64Profile_Type.__name__=_E
_CatmtAal5Nx64Profile_Object=MibTableColumn
catmtAal5Nx64Profile=_CatmtAal5Nx64Profile_Object((1,3,6,1,4,1,9,9,351,1,5,1,1,5),_CatmtAal5Nx64Profile_Type())
catmtAal5Nx64Profile.setMaxAccess(_D)
if mibBuilder.loadTexts:catmtAal5Nx64Profile.setStatus(_A)
_CatmtAal5RowStatus_Type=RowStatus
_CatmtAal5RowStatus_Object=MibTableColumn
catmtAal5RowStatus=_CatmtAal5RowStatus_Object((1,3,6,1,4,1,9,9,351,1,5,1,1,6),_CatmtAal5RowStatus_Type())
catmtAal5RowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:catmtAal5RowStatus.setStatus(_A)
_CAtmTrunkAal5ConnStats_ObjectIdentity=ObjectIdentity
cAtmTrunkAal5ConnStats=_CAtmTrunkAal5ConnStats_ObjectIdentity((1,3,6,1,4,1,9,9,351,1,6))
_CatmtAal5StatsTable_Object=MibTable
catmtAal5StatsTable=_CatmtAal5StatsTable_Object((1,3,6,1,4,1,9,9,351,1,6,1))
if mibBuilder.loadTexts:catmtAal5StatsTable.setStatus(_A)
_CatmtAal5StatsEntry_Object=MibTableRow
catmtAal5StatsEntry=_CatmtAal5StatsEntry_Object((1,3,6,1,4,1,9,9,351,1,6,1,1))
catmtAal5StatsEntry.setIndexNames((0,_F,_G),(0,_B,_R),(0,_B,_S))
if mibBuilder.loadTexts:catmtAal5StatsEntry.setStatus(_A)
_CatmtAal5SentPackets_Type=Counter32SinceReset
_CatmtAal5SentPackets_Object=MibTableColumn
catmtAal5SentPackets=_CatmtAal5SentPackets_Object((1,3,6,1,4,1,9,9,351,1,6,1,1,1),_CatmtAal5SentPackets_Type())
catmtAal5SentPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:catmtAal5SentPackets.setStatus(_A)
if mibBuilder.loadTexts:catmtAal5SentPackets.setUnits(_J)
_CatmtAal5RcvdPackets_Type=Counter32SinceReset
_CatmtAal5RcvdPackets_Object=MibTableColumn
catmtAal5RcvdPackets=_CatmtAal5RcvdPackets_Object((1,3,6,1,4,1,9,9,351,1,6,1,1,2),_CatmtAal5RcvdPackets_Type())
catmtAal5RcvdPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:catmtAal5RcvdPackets.setStatus(_A)
if mibBuilder.loadTexts:catmtAal5RcvdPackets.setUnits(_J)
_CatmtAal5SentOctets_Type=Counter32SinceReset
_CatmtAal5SentOctets_Object=MibTableColumn
catmtAal5SentOctets=_CatmtAal5SentOctets_Object((1,3,6,1,4,1,9,9,351,1,6,1,1,3),_CatmtAal5SentOctets_Type())
catmtAal5SentOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:catmtAal5SentOctets.setStatus(_A)
if mibBuilder.loadTexts:catmtAal5SentOctets.setUnits(_K)
_CatmtAal5RcvdOctets_Type=Counter32SinceReset
_CatmtAal5RcvdOctets_Object=MibTableColumn
catmtAal5RcvdOctets=_CatmtAal5RcvdOctets_Object((1,3,6,1,4,1,9,9,351,1,6,1,1,4),_CatmtAal5RcvdOctets_Type())
catmtAal5RcvdOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:catmtAal5RcvdOctets.setStatus(_A)
if mibBuilder.loadTexts:catmtAal5RcvdOctets.setUnits(_K)
_CatmtAal5FramesTxToTDM_Type=Counter32SinceReset
_CatmtAal5FramesTxToTDM_Object=MibTableColumn
catmtAal5FramesTxToTDM=_CatmtAal5FramesTxToTDM_Object((1,3,6,1,4,1,9,9,351,1,6,1,1,5),_CatmtAal5FramesTxToTDM_Type())
catmtAal5FramesTxToTDM.setMaxAccess(_C)
if mibBuilder.loadTexts:catmtAal5FramesTxToTDM.setStatus(_A)
_CatmtAal5FramesRxFromTDM_Type=Counter32SinceReset
_CatmtAal5FramesRxFromTDM_Object=MibTableColumn
catmtAal5FramesRxFromTDM=_CatmtAal5FramesRxFromTDM_Object((1,3,6,1,4,1,9,9,351,1,6,1,1,6),_CatmtAal5FramesRxFromTDM_Type())
catmtAal5FramesRxFromTDM.setMaxAccess(_C)
if mibBuilder.loadTexts:catmtAal5FramesRxFromTDM.setStatus(_A)
_CatmtAal5EncBytesTxToTDM_Type=Counter32SinceReset
_CatmtAal5EncBytesTxToTDM_Object=MibTableColumn
catmtAal5EncBytesTxToTDM=_CatmtAal5EncBytesTxToTDM_Object((1,3,6,1,4,1,9,9,351,1,6,1,1,7),_CatmtAal5EncBytesTxToTDM_Type())
catmtAal5EncBytesTxToTDM.setMaxAccess(_C)
if mibBuilder.loadTexts:catmtAal5EncBytesTxToTDM.setStatus(_A)
_CatmtAal5EncBytesRxFromTDM_Type=Counter32SinceReset
_CatmtAal5EncBytesRxFromTDM_Object=MibTableColumn
catmtAal5EncBytesRxFromTDM=_CatmtAal5EncBytesRxFromTDM_Object((1,3,6,1,4,1,9,9,351,1,6,1,1,8),_CatmtAal5EncBytesRxFromTDM_Type())
catmtAal5EncBytesRxFromTDM.setMaxAccess(_C)
if mibBuilder.loadTexts:catmtAal5EncBytesRxFromTDM.setStatus(_A)
_CatmtAal5InvalidFCSFrames_Type=Counter32SinceReset
_CatmtAal5InvalidFCSFrames_Object=MibTableColumn
catmtAal5InvalidFCSFrames=_CatmtAal5InvalidFCSFrames_Object((1,3,6,1,4,1,9,9,351,1,6,1,1,9),_CatmtAal5InvalidFCSFrames_Type())
catmtAal5InvalidFCSFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:catmtAal5InvalidFCSFrames.setStatus(_A)
_CatmtAal5AbortSeqFrames_Type=Counter32SinceReset
_CatmtAal5AbortSeqFrames_Object=MibTableColumn
catmtAal5AbortSeqFrames=_CatmtAal5AbortSeqFrames_Object((1,3,6,1,4,1,9,9,351,1,6,1,1,10),_CatmtAal5AbortSeqFrames_Type())
catmtAal5AbortSeqFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:catmtAal5AbortSeqFrames.setStatus(_A)
_CatmtAal5InvalidShortFrames_Type=Counter32SinceReset
_CatmtAal5InvalidShortFrames_Object=MibTableColumn
catmtAal5InvalidShortFrames=_CatmtAal5InvalidShortFrames_Object((1,3,6,1,4,1,9,9,351,1,6,1,1,11),_CatmtAal5InvalidShortFrames_Type())
catmtAal5InvalidShortFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:catmtAal5InvalidShortFrames.setStatus(_A)
_CatmtAal5InvalidLongFrames_Type=Counter32SinceReset
_CatmtAal5InvalidLongFrames_Object=MibTableColumn
catmtAal5InvalidLongFrames=_CatmtAal5InvalidLongFrames_Object((1,3,6,1,4,1,9,9,351,1,6,1,1,12),_CatmtAal5InvalidLongFrames_Type())
catmtAal5InvalidLongFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:catmtAal5InvalidLongFrames.setStatus(_A)
_CatmtAal5NoByteAlignErrorFrames_Type=Counter32SinceReset
_CatmtAal5NoByteAlignErrorFrames_Object=MibTableColumn
catmtAal5NoByteAlignErrorFrames=_CatmtAal5NoByteAlignErrorFrames_Object((1,3,6,1,4,1,9,9,351,1,6,1,1,13),_CatmtAal5NoByteAlignErrorFrames_Type())
catmtAal5NoByteAlignErrorFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:catmtAal5NoByteAlignErrorFrames.setStatus(_A)
_CatmtAal5LastResetTime_Type=TimeStamp
_CatmtAal5LastResetTime_Object=MibTableColumn
catmtAal5LastResetTime=_CatmtAal5LastResetTime_Object((1,3,6,1,4,1,9,9,351,1,6,1,1,14),_CatmtAal5LastResetTime_Type())
catmtAal5LastResetTime.setMaxAccess(_C)
if mibBuilder.loadTexts:catmtAal5LastResetTime.setStatus(_A)
_CatmtAal5CounterClear_Type=TruthValue
_CatmtAal5CounterClear_Object=MibTableColumn
catmtAal5CounterClear=_CatmtAal5CounterClear_Object((1,3,6,1,4,1,9,9,351,1,6,1,1,15),_CatmtAal5CounterClear_Type())
catmtAal5CounterClear.setMaxAccess(_O)
if mibBuilder.loadTexts:catmtAal5CounterClear.setStatus(_A)
_CAtmTrunkMIBConformance_ObjectIdentity=ObjectIdentity
cAtmTrunkMIBConformance=_CAtmTrunkMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,351,2))
_CAtmTrunkMIBCompliances_ObjectIdentity=ObjectIdentity
cAtmTrunkMIBCompliances=_CAtmTrunkMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,351,2,1))
_CAtmTrunkMIBGroups_ObjectIdentity=ObjectIdentity
cAtmTrunkMIBGroups=_CAtmTrunkMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,351,2,2))
cAtmTrunkCidMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,351,2,2,1))
cAtmTrunkCidMIBGroup.setObjects(*((_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i)))
if mibBuilder.loadTexts:cAtmTrunkCidMIBGroup.setStatus(_A)
cAtmTrunkAal1MIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,351,2,2,2))
cAtmTrunkAal1MIBGroup.setObjects(*((_B,_j),(_B,_k),(_B,_l),(_B,_m)))
if mibBuilder.loadTexts:cAtmTrunkAal1MIBGroup.setStatus(_A)
cAtmTrunkAal5MIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,351,2,2,3))
cAtmTrunkAal5MIBGroup.setObjects(*((_B,_n),(_B,_o),(_B,_p),(_B,_q)))
if mibBuilder.loadTexts:cAtmTrunkAal5MIBGroup.setStatus(_A)
cAtmTrunkCidConnStatsMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,351,2,2,4))
cAtmTrunkCidConnStatsMIBGroup.setObjects(*((_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC)))
if mibBuilder.loadTexts:cAtmTrunkCidConnStatsMIBGroup.setStatus(_A)
cAtmTrunkAal1ConnStatsMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,351,2,2,5))
cAtmTrunkAal1ConnStatsMIBGroup.setObjects(*((_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ)))
if mibBuilder.loadTexts:cAtmTrunkAal1ConnStatsMIBGroup.setStatus(_A)
cAtmTrunkAal5ConnStatsMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,351,2,2,6))
cAtmTrunkAal5ConnStatsMIBGroup.setObjects(*((_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY)))
if mibBuilder.loadTexts:cAtmTrunkAal5ConnStatsMIBGroup.setStatus(_A)
cAtmTrunkMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,351,2,1,1))
cAtmTrunkMIBCompliance.setObjects(*((_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae)))
if mibBuilder.loadTexts:cAtmTrunkMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'Counter32SinceReset':Counter32SinceReset,'ciscoAtmTrunkMIB':ciscoAtmTrunkMIB,'cAtmTrunkMIBNotifications':cAtmTrunkMIBNotifications,'cAtmTrunkMIBObjects':cAtmTrunkMIBObjects,'cAtmTrunkCidConfig':cAtmTrunkCidConfig,'catmtCidTable':catmtCidTable,'catmtCidEntry':catmtCidEntry,_L:catmtCidVpi,_M:catmtCidVci,_N:catmtCid,_W:catmtCidDs1,_X:catmtCidDs0GroupIndex,_Y:catmtCidProfileType,_Z:catmtCidProfileNumber,_a:catmtCidVoiceCodec,_b:catmtCidVBDCodec,_c:catmtCidNx64Enable,_d:catmtCidNx64Profile,_e:catmtCidStateBitMap,_f:catmtCidRepetition,_g:catmtCidRepetitionOwner,_h:catmtCidRepetitionResult,_i:catmtCidRowStatus,'cAtmTrunkCidConnStats':cAtmTrunkCidConnStats,'catmtCidStatsTable':catmtCidStatsTable,'catmtCidStatsEntry':catmtCidStatsEntry,_r:catmtCidSentPackets,_s:catmtCidRcvdPackets,_t:catmtCidSentOctets,_u:catmtCidRcvdOctets,_v:catmtCidLostPackets,_w:catmtCidJitter,_x:catmtCidExtAISCnts,_y:catmtCidExtRAICnts,_z:catmtCidConnAISCnts,_A0:catmtCidConnRDICnts,_A1:catmtCidNx64FramesTxToTDM,_A2:catmtCidNx64FramesRxFromTDM,_A3:catmtCidNx64EncBytesTxToTDM,_A4:catmtCidNx64EncBytesRxFromTDM,_A5:catmtCidNx64InvalidFCSFrames,_A6:catmtCidNx64AbortSeqFrames,_A7:catmtCidNx64InvalidShortFrames,_A8:catmtCidNx64InvalidLongFrames,_A9:catmtCidNx64NoByteAlignErrorFrames,_AA:catmtCidNx64RASTimeOutFrames,_AB:catmtCidLastResetTime,_AC:catmtCidCounterClear,'cAtmTrunkAal1Config':cAtmTrunkAal1Config,'catmtAal1Table':catmtAal1Table,'catmtAal1Entry':catmtAal1Entry,_P:catmtAal1Vpi,_Q:catmtAal1Vci,_j:catmtAal1Ds1,_k:catmtAal1Ds0GroupIndex,_l:catmtAal1Nx64Profile,_m:catmtAal1RowStatus,'cAtmTrunkAal1ConnStats':cAtmTrunkAal1ConnStats,'catmtAal1StatsTable':catmtAal1StatsTable,'catmtAal1StatsEntry':catmtAal1StatsEntry,_AD:catmtAal1TxCells,_AE:catmtAal1RxCells,_AF:catmtAal1TxPayloadBytes,_AG:catmtAal1RxPayloadBytes,_AH:catmtAal1Jitter,_AI:catmtAal1LastResetTime,_AJ:catmtAal1CounterClear,'cAtmTrunkAal5Config':cAtmTrunkAal5Config,'catmtAal5Table':catmtAal5Table,'catmtAal5Entry':catmtAal5Entry,_R:catmtAal5Vpi,_S:catmtAal5Vci,_n:catmtAal5Ds1,_o:catmtAal5Ds0GroupIndex,_p:catmtAal5Nx64Profile,_q:catmtAal5RowStatus,'cAtmTrunkAal5ConnStats':cAtmTrunkAal5ConnStats,'catmtAal5StatsTable':catmtAal5StatsTable,'catmtAal5StatsEntry':catmtAal5StatsEntry,_AK:catmtAal5SentPackets,_AL:catmtAal5RcvdPackets,_AM:catmtAal5SentOctets,_AN:catmtAal5RcvdOctets,_AO:catmtAal5FramesTxToTDM,_AP:catmtAal5FramesRxFromTDM,_AQ:catmtAal5EncBytesTxToTDM,_AR:catmtAal5EncBytesRxFromTDM,_AS:catmtAal5InvalidFCSFrames,_AT:catmtAal5AbortSeqFrames,_AU:catmtAal5InvalidShortFrames,_AV:catmtAal5InvalidLongFrames,_AW:catmtAal5NoByteAlignErrorFrames,_AX:catmtAal5LastResetTime,_AY:catmtAal5CounterClear,'cAtmTrunkMIBConformance':cAtmTrunkMIBConformance,'cAtmTrunkMIBCompliances':cAtmTrunkMIBCompliances,'cAtmTrunkMIBCompliance':cAtmTrunkMIBCompliance,'cAtmTrunkMIBGroups':cAtmTrunkMIBGroups,_AZ:cAtmTrunkCidMIBGroup,_Aa:cAtmTrunkAal1MIBGroup,_Ab:cAtmTrunkAal5MIBGroup,_Ac:cAtmTrunkCidConnStatsMIBGroup,_Ad:cAtmTrunkAal1ConnStatsMIBGroup,_Ae:cAtmTrunkAal5ConnStatsMIBGroup})