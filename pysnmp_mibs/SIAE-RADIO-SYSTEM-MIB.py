_z='sspParameterType'
_y='not-accessible'
_x='linkE1vsSTM1CapacityStm1'
_w='Stm1IndexOrZero'
_v='stm1BulkChanIndex'
_u='stm1BulkPolIndex'
_t='combinedRadioDuplexFreqId'
_s='combinedRadioFreqChannelId'
_r='linkChannelSpacing'
_q='linkDuplexFreqId'
_p='linkFreqChannelId'
_o='BitsPerSymbol'
_n='unknown'
_m='radioChannelSpacing'
_l='radioDuplexFreqId'
_k='radioFreqChannelId'
_j='tdmPolIndex'
_i='highGain'
_h='highThroughput'
_g='linkChIndex'
_f='xpicChPolIndex'
_e='baseBandLoop'
_d='InterfaceIndexOrZero'
_c='radioSettingsLabel'
_b='reset'
_a='strong'
_Z='normal'
_Y='active'
_X='xpicIndex'
_W='equipIpSnmpAgentAddress'
_V='SIAE-EQUIP-MIB'
_U='on'
_T='linkAcmProfileId'
_S='cleared'
_R='trapEnable'
_Q='trapDisable'
_P='radioSettingsIndex'
_O='notActive'
_N='DisplayString'
_M='linkPolIndex'
_L='radioIndex'
_K='linkIndex'
_J='enable'
_I='disable'
_H='AlarmSeverityCode'
_G='deprecated'
_F='read-create'
_E='SIAE-RADIO-SYSTEM-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB',_d)
AlarmSeverityCode,AlarmStatus,alarmTrap=mibBuilder.importSymbols('SIAE-ALARM-MIB',_H,'AlarmStatus','alarmTrap')
equipIpSnmpAgentAddress,=mibBuilder.importSymbols(_V,_W)
siaeMib,=mibBuilder.importSymbols('SIAE-TREE-MIB','siaeMib')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_N,'PhysAddress','RowStatus','StorageType','TextualConvention')
radioSystem=ModuleIdentity((1,3,6,1,4,1,3373,1103,80))
if mibBuilder.loadTexts:radioSystem.setRevisions(('2018-08-23 00:00','2018-05-22 00:00','2018-02-08 00:00','2016-12-20 00:00','2016-09-13 00:00','2016-07-14 00:00','2016-02-29 00:00','2015-09-15 00:00','2015-06-18 00:00','2015-03-23 00:00','2014-11-05 00:00','2014-09-16 00:00','2014-04-01 00:00'))
class ChannelSpacing(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)));namedValues=NamedValues(*(('bw3M5Hz',0),('bw7Mhz',1),('bw14MHz',2),('bw28MHz',3),('bw56MHz',4),('bw40MHz',5),('bw112MHz',6),('bw250Mhz',7),('bw500Mhz',8),('bw750Mhz',9),('bw1000Mhz',10),('bw10Mhz',11),('bw20Mhz',12),('bw30Mhz',13),('bw50Mhz',14),('bw60Mhz',15),('bw80Mhz',16),('bw2000Mhz',17),('bw62M5hz',18),('bw125Mhz',19),('bw1500Mhz',20)))
class ModulationMap(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('modBPSK',0),('mod4QAM',1),('mod8PSK',2),('mod16QAM',3),('mod32QAM',4),('mod64QAM',5),('mod128QAM',6),('mod256QAM',7),('mod512QAM',8),('mod1024QAM',9),('mod2048QAM',10),('mod4096QAM',11)))
class ConfigMismatchReason(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('securityMismatch',0),('frequencyFailMismatch',1),('frequencyAlertMismatch',2),('ptxMismatch',3),('channelSpacingAndModulationMismatch',4),('remoteConfigurationMismatch',5),('acmMismatch',6),('profileSetMismatch',7)))
class RadioCapability(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('reserved',0),('trafficSquelch',1),(_e,2),('maxPower',3),('carrierOnly',4),('iQLoop',5),('rfLoopGivenMod',6),('rfLoopAnyMod',7),('iQLoopAtRxFreq',8),('atpcMinPower',9),('echoCanceler',10)))
class BitsPerSymbol(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('bpsBPSK',1),('bps4QAM',2),('bps8PSK',3),('bps16QAM',4),('bps32QAM',5),('bps64QAM',6),('bps128QAM',7),('bps256QAM',8),('bps512QAM',9),('bps1024QAM',10),('bps2048QAM',11),('bps4096QAM',12)))
class Stm1IndexOrZero(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RadioSystemMibVersion_Type=Integer32
_RadioSystemMibVersion_Object=MibScalar
radioSystemMibVersion=_RadioSystemMibVersion_Object((1,3,6,1,4,1,3373,1103,80,1),_RadioSystemMibVersion_Type())
radioSystemMibVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:radioSystemMibVersion.setStatus(_A)
_RadioTable_Object=MibTable
radioTable=_RadioTable_Object((1,3,6,1,4,1,3373,1103,80,2))
if mibBuilder.loadTexts:radioTable.setStatus(_A)
_RadioEntry_Object=MibTableRow
radioEntry=_RadioEntry_Object((1,3,6,1,4,1,3373,1103,80,2,1))
radioEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:radioEntry.setStatus(_A)
_RadioIndex_Type=Integer32
_RadioIndex_Object=MibTableColumn
radioIndex=_RadioIndex_Object((1,3,6,1,4,1,3373,1103,80,2,1,1),_RadioIndex_Type())
radioIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:radioIndex.setStatus(_A)
class _RadioLabel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RadioLabel_Type.__name__=_N
_RadioLabel_Object=MibTableColumn
radioLabel=_RadioLabel_Object((1,3,6,1,4,1,3373,1103,80,2,1,2),_RadioLabel_Type())
radioLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:radioLabel.setStatus(_A)
class _RadioType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('analogRadio',2),('digitalRadio',3),('xpicRadio',4)))
_RadioType_Type.__name__=_C
_RadioType_Object=MibTableColumn
radioType=_RadioType_Object((1,3,6,1,4,1,3373,1103,80,2,1,3),_RadioType_Type())
radioType.setMaxAccess(_B)
if mibBuilder.loadTexts:radioType.setStatus(_A)
_RadioIfIndex_Type=InterfaceIndexOrZero
_RadioIfIndex_Object=MibTableColumn
radioIfIndex=_RadioIfIndex_Object((1,3,6,1,4,1,3373,1103,80,2,1,4),_RadioIfIndex_Type())
radioIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:radioIfIndex.setStatus(_A)
_RadioStorageType_Type=StorageType
_RadioStorageType_Object=MibTableColumn
radioStorageType=_RadioStorageType_Object((1,3,6,1,4,1,3373,1103,80,2,1,5),_RadioStorageType_Type())
radioStorageType.setMaxAccess(_B)
if mibBuilder.loadTexts:radioStorageType.setStatus(_A)
_XpicTable_Object=MibTable
xpicTable=_XpicTable_Object((1,3,6,1,4,1,3373,1103,80,3))
if mibBuilder.loadTexts:xpicTable.setStatus(_A)
_XpicEntry_Object=MibTableRow
xpicEntry=_XpicEntry_Object((1,3,6,1,4,1,3373,1103,80,3,1))
xpicEntry.setIndexNames((0,_E,_X))
if mibBuilder.loadTexts:xpicEntry.setStatus(_A)
_XpicIndex_Type=Integer32
_XpicIndex_Object=MibTableColumn
xpicIndex=_XpicIndex_Object((1,3,6,1,4,1,3373,1103,80,3,1,1),_XpicIndex_Type())
xpicIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:xpicIndex.setStatus(_A)
_XpicRadioIdx_Type=Integer32
_XpicRadioIdx_Object=MibTableColumn
xpicRadioIdx=_XpicRadioIdx_Object((1,3,6,1,4,1,3373,1103,80,3,1,2),_XpicRadioIdx_Type())
xpicRadioIdx.setMaxAccess(_F)
if mibBuilder.loadTexts:xpicRadioIdx.setStatus(_A)
_XpicRowstatus_Type=RowStatus
_XpicRowstatus_Object=MibTableColumn
xpicRowstatus=_XpicRowstatus_Object((1,3,6,1,4,1,3373,1103,80,3,1,3),_XpicRowstatus_Type())
xpicRowstatus.setMaxAccess(_F)
if mibBuilder.loadTexts:xpicRowstatus.setStatus(_A)
_XpicChTable_Object=MibTable
xpicChTable=_XpicChTable_Object((1,3,6,1,4,1,3373,1103,80,4))
if mibBuilder.loadTexts:xpicChTable.setStatus(_A)
_XpicChEntry_Object=MibTableRow
xpicChEntry=_XpicChEntry_Object((1,3,6,1,4,1,3373,1103,80,4,1))
xpicChEntry.setIndexNames((0,_E,_X),(0,_E,_f))
if mibBuilder.loadTexts:xpicChEntry.setStatus(_A)
class _XpicChPolIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_XpicChPolIndex_Type.__name__=_C
_XpicChPolIndex_Object=MibTableColumn
xpicChPolIndex=_XpicChPolIndex_Object((1,3,6,1,4,1,3373,1103,80,4,1,1),_XpicChPolIndex_Type())
xpicChPolIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:xpicChPolIndex.setStatus(_A)
_XpicChRadioIdx_Type=Integer32
_XpicChRadioIdx_Object=MibTableColumn
xpicChRadioIdx=_XpicChRadioIdx_Object((1,3,6,1,4,1,3373,1103,80,4,1,2),_XpicChRadioIdx_Type())
xpicChRadioIdx.setMaxAccess(_F)
if mibBuilder.loadTexts:xpicChRadioIdx.setStatus(_A)
_XpicChRowstatus_Type=RowStatus
_XpicChRowstatus_Object=MibTableColumn
xpicChRowstatus=_XpicChRowstatus_Object((1,3,6,1,4,1,3373,1103,80,4,1,3),_XpicChRowstatus_Type())
xpicChRowstatus.setMaxAccess(_F)
if mibBuilder.loadTexts:xpicChRowstatus.setStatus(_A)
_LinkAvailableIndex_Type=Integer32
_LinkAvailableIndex_Object=MibScalar
linkAvailableIndex=_LinkAvailableIndex_Object((1,3,6,1,4,1,3373,1103,80,5),_LinkAvailableIndex_Type())
linkAvailableIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:linkAvailableIndex.setStatus(_A)
_LinkTable_Object=MibTable
linkTable=_LinkTable_Object((1,3,6,1,4,1,3373,1103,80,6))
if mibBuilder.loadTexts:linkTable.setStatus(_A)
_LinkEntry_Object=MibTableRow
linkEntry=_LinkEntry_Object((1,3,6,1,4,1,3373,1103,80,6,1))
linkEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:linkEntry.setStatus(_A)
_LinkIndex_Type=Integer32
_LinkIndex_Object=MibTableColumn
linkIndex=_LinkIndex_Object((1,3,6,1,4,1,3373,1103,80,6,1,1),_LinkIndex_Type())
linkIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:linkIndex.setStatus(_A)
class _LinkType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('radio1p0',1),('radio1p1HS',2),('radio1p1FD',3),('radio2p0Xpic',4),('radio2p2XpicHS',5),('radio2p2XpicFD',6),('radioNp1',7),('radio1p0XpicH',8),('radio1p0XpicV',9)))
_LinkType_Type.__name__=_C
_LinkType_Object=MibTableColumn
linkType=_LinkType_Object((1,3,6,1,4,1,3373,1103,80,6,1,2),_LinkType_Type())
linkType.setMaxAccess(_F)
if mibBuilder.loadTexts:linkType.setStatus(_A)
class _LinkLabel_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_LinkLabel_Type.__name__=_N
_LinkLabel_Object=MibTableColumn
linkLabel=_LinkLabel_Object((1,3,6,1,4,1,3373,1103,80,6,1,3),_LinkLabel_Type())
linkLabel.setMaxAccess(_F)
if mibBuilder.loadTexts:linkLabel.setStatus(_A)
class _LinkIfIndex_Type(InterfaceIndexOrZero):defaultValue=0
_LinkIfIndex_Type.__name__=_d
_LinkIfIndex_Object=MibTableColumn
linkIfIndex=_LinkIfIndex_Object((1,3,6,1,4,1,3373,1103,80,6,1,4),_LinkIfIndex_Type())
linkIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:linkIfIndex.setStatus(_A)
_LinkRowstatus_Type=RowStatus
_LinkRowstatus_Object=MibTableColumn
linkRowstatus=_LinkRowstatus_Object((1,3,6,1,4,1,3373,1103,80,6,1,5),_LinkRowstatus_Type())
linkRowstatus.setMaxAccess(_F)
if mibBuilder.loadTexts:linkRowstatus.setStatus(_A)
_LinkChTable_Object=MibTable
linkChTable=_LinkChTable_Object((1,3,6,1,4,1,3373,1103,80,7))
if mibBuilder.loadTexts:linkChTable.setStatus(_A)
_LinkChEntry_Object=MibTableRow
linkChEntry=_LinkChEntry_Object((1,3,6,1,4,1,3373,1103,80,7,1))
linkChEntry.setIndexNames((0,_E,_K),(0,_E,_g))
if mibBuilder.loadTexts:linkChEntry.setStatus(_A)
_LinkChIndex_Type=Integer32
_LinkChIndex_Object=MibTableColumn
linkChIndex=_LinkChIndex_Object((1,3,6,1,4,1,3373,1103,80,7,1,1),_LinkChIndex_Type())
linkChIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:linkChIndex.setStatus(_A)
_LinkChRadioIdx_Type=Integer32
_LinkChRadioIdx_Object=MibTableColumn
linkChRadioIdx=_LinkChRadioIdx_Object((1,3,6,1,4,1,3373,1103,80,7,1,2),_LinkChRadioIdx_Type())
linkChRadioIdx.setMaxAccess(_F)
if mibBuilder.loadTexts:linkChRadioIdx.setStatus(_A)
class _LinkChRadioSettingsIdx_Type(Integer32):defaultValue=0
_LinkChRadioSettingsIdx_Type.__name__=_C
_LinkChRadioSettingsIdx_Object=MibTableColumn
linkChRadioSettingsIdx=_LinkChRadioSettingsIdx_Object((1,3,6,1,4,1,3373,1103,80,7,1,3),_LinkChRadioSettingsIdx_Type())
linkChRadioSettingsIdx.setMaxAccess(_F)
if mibBuilder.loadTexts:linkChRadioSettingsIdx.setStatus(_A)
_LinkChRowstatus_Type=RowStatus
_LinkChRowstatus_Object=MibTableColumn
linkChRowstatus=_LinkChRowstatus_Object((1,3,6,1,4,1,3373,1103,80,7,1,4),_LinkChRowstatus_Type())
linkChRowstatus.setMaxAccess(_F)
if mibBuilder.loadTexts:linkChRowstatus.setStatus(_A)
_LinkSettingsTable_Object=MibTable
linkSettingsTable=_LinkSettingsTable_Object((1,3,6,1,4,1,3373,1103,80,8))
if mibBuilder.loadTexts:linkSettingsTable.setStatus(_A)
_LinkSettingsEntry_Object=MibTableRow
linkSettingsEntry=_LinkSettingsEntry_Object((1,3,6,1,4,1,3373,1103,80,8,1))
linkSettingsEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:linkSettingsEntry.setStatus(_A)
_LinkBandwidthAndModulation_Type=Integer32
_LinkBandwidthAndModulation_Object=MibTableColumn
linkBandwidthAndModulation=_LinkBandwidthAndModulation_Object((1,3,6,1,4,1,3373,1103,80,8,1,1),_LinkBandwidthAndModulation_Type())
linkBandwidthAndModulation.setMaxAccess(_F)
if mibBuilder.loadTexts:linkBandwidthAndModulation.setStatus(_A)
class _LinkAcmEngineEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_LinkAcmEngineEnable_Type.__name__=_C
_LinkAcmEngineEnable_Object=MibTableColumn
linkAcmEngineEnable=_LinkAcmEngineEnable_Object((1,3,6,1,4,1,3373,1103,80,8,1,2),_LinkAcmEngineEnable_Type())
linkAcmEngineEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:linkAcmEngineEnable.setStatus(_A)
_LinkTxUpperProfile_Type=Integer32
_LinkTxUpperProfile_Object=MibTableColumn
linkTxUpperProfile=_LinkTxUpperProfile_Object((1,3,6,1,4,1,3373,1103,80,8,1,3),_LinkTxUpperProfile_Type())
linkTxUpperProfile.setMaxAccess(_F)
if mibBuilder.loadTexts:linkTxUpperProfile.setStatus(_A)
_LinkTxLowerProfile_Type=Integer32
_LinkTxLowerProfile_Object=MibTableColumn
linkTxLowerProfile=_LinkTxLowerProfile_Object((1,3,6,1,4,1,3373,1103,80,8,1,4),_LinkTxLowerProfile_Type())
linkTxLowerProfile.setMaxAccess(_F)
if mibBuilder.loadTexts:linkTxLowerProfile.setStatus(_A)
class _LinkId_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_LinkId_Type.__name__=_C
_LinkId_Object=MibTableColumn
linkId=_LinkId_Object((1,3,6,1,4,1,3373,1103,80,8,1,5),_LinkId_Type())
linkId.setMaxAccess(_F)
if mibBuilder.loadTexts:linkId.setStatus(_A)
class _LinkTxPwrThresh_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,15))
_LinkTxPwrThresh_Type.__name__=_C
_LinkTxPwrThresh_Object=MibTableColumn
linkTxPwrThresh=_LinkTxPwrThresh_Object((1,3,6,1,4,1,3373,1103,80,8,1,6),_LinkTxPwrThresh_Type())
linkTxPwrThresh.setMaxAccess(_F)
if mibBuilder.loadTexts:linkTxPwrThresh.setStatus(_A)
class _LinkRxPwrThresh_Type(Integer32):defaultValue=-70;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-99,-40))
_LinkRxPwrThresh_Type.__name__=_C
_LinkRxPwrThresh_Object=MibTableColumn
linkRxPwrThresh=_LinkRxPwrThresh_Object((1,3,6,1,4,1,3373,1103,80,8,1,7),_LinkRxPwrThresh_Type())
linkRxPwrThresh.setMaxAccess(_F)
if mibBuilder.loadTexts:linkRxPwrThresh.setStatus(_A)
class _LinkSynchSetupProtocolEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_LinkSynchSetupProtocolEnable_Type.__name__=_C
_LinkSynchSetupProtocolEnable_Object=MibTableColumn
linkSynchSetupProtocolEnable=_LinkSynchSetupProtocolEnable_Object((1,3,6,1,4,1,3373,1103,80,8,1,8),_LinkSynchSetupProtocolEnable_Type())
linkSynchSetupProtocolEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:linkSynchSetupProtocolEnable.setStatus(_A)
class _LinkProfilesSetSelection_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_h,1),(_i,2)))
_LinkProfilesSetSelection_Type.__name__=_C
_LinkProfilesSetSelection_Object=MibTableColumn
linkProfilesSetSelection=_LinkProfilesSetSelection_Object((1,3,6,1,4,1,3373,1103,80,8,1,9),_LinkProfilesSetSelection_Type())
linkProfilesSetSelection.setMaxAccess(_F)
if mibBuilder.loadTexts:linkProfilesSetSelection.setStatus(_A)
class _LinkXpicControlProcedure_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_LinkXpicControlProcedure_Type.__name__=_C
_LinkXpicControlProcedure_Object=MibTableColumn
linkXpicControlProcedure=_LinkXpicControlProcedure_Object((1,3,6,1,4,1,3373,1103,80,8,1,10),_LinkXpicControlProcedure_Type())
linkXpicControlProcedure.setMaxAccess(_F)
if mibBuilder.loadTexts:linkXpicControlProcedure.setStatus(_A)
_RadioSettingsTable_Object=MibTable
radioSettingsTable=_RadioSettingsTable_Object((1,3,6,1,4,1,3373,1103,80,9))
if mibBuilder.loadTexts:radioSettingsTable.setStatus(_A)
_RadioSettingsEntry_Object=MibTableRow
radioSettingsEntry=_RadioSettingsEntry_Object((1,3,6,1,4,1,3373,1103,80,9,1))
radioSettingsEntry.setIndexNames((0,_E,_P))
if mibBuilder.loadTexts:radioSettingsEntry.setStatus(_A)
_RadioSettingsIndex_Type=Integer32
_RadioSettingsIndex_Object=MibTableColumn
radioSettingsIndex=_RadioSettingsIndex_Object((1,3,6,1,4,1,3373,1103,80,9,1,1),_RadioSettingsIndex_Type())
radioSettingsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:radioSettingsIndex.setStatus(_A)
_RadioSettingsRowStatus_Type=RowStatus
_RadioSettingsRowStatus_Object=MibTableColumn
radioSettingsRowStatus=_RadioSettingsRowStatus_Object((1,3,6,1,4,1,3373,1103,80,9,1,2),_RadioSettingsRowStatus_Type())
radioSettingsRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:radioSettingsRowStatus.setStatus(_A)
class _RadioSettingsLabel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RadioSettingsLabel_Type.__name__=_N
_RadioSettingsLabel_Object=MibTableColumn
radioSettingsLabel=_RadioSettingsLabel_Object((1,3,6,1,4,1,3373,1103,80,9,1,3),_RadioSettingsLabel_Type())
radioSettingsLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:radioSettingsLabel.setStatus(_A)
class _RadioTxFrequency_Type(Integer32):defaultValue=0
_RadioTxFrequency_Type.__name__=_C
_RadioTxFrequency_Object=MibTableColumn
radioTxFrequency=_RadioTxFrequency_Object((1,3,6,1,4,1,3373,1103,80,9,1,4),_RadioTxFrequency_Type())
radioTxFrequency.setMaxAccess(_F)
if mibBuilder.loadTexts:radioTxFrequency.setStatus(_A)
class _RadioDuplexFrequency_Type(Integer32):defaultValue=-2
_RadioDuplexFrequency_Type.__name__=_C
_RadioDuplexFrequency_Object=MibTableColumn
radioDuplexFrequency=_RadioDuplexFrequency_Object((1,3,6,1,4,1,3373,1103,80,9,1,5),_RadioDuplexFrequency_Type())
radioDuplexFrequency.setMaxAccess(_F)
if mibBuilder.loadTexts:radioDuplexFrequency.setStatus(_A)
_RadioTxAttenuation_Type=Integer32
_RadioTxAttenuation_Object=MibTableColumn
radioTxAttenuation=_RadioTxAttenuation_Object((1,3,6,1,4,1,3373,1103,80,9,1,6),_RadioTxAttenuation_Type())
radioTxAttenuation.setMaxAccess(_F)
if mibBuilder.loadTexts:radioTxAttenuation.setStatus(_A)
class _RadioAtpcManual_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_J,2),('enable-min-power',3)))
_RadioAtpcManual_Type.__name__=_C
_RadioAtpcManual_Object=MibTableColumn
radioAtpcManual=_RadioAtpcManual_Object((1,3,6,1,4,1,3373,1103,80,9,1,7),_RadioAtpcManual_Type())
radioAtpcManual.setMaxAccess(_F)
if mibBuilder.loadTexts:radioAtpcManual.setStatus(_A)
class _RadioAtpcPwrHigh_Type(Integer32):defaultValue=-40
_RadioAtpcPwrHigh_Type.__name__=_C
_RadioAtpcPwrHigh_Object=MibTableColumn
radioAtpcPwrHigh=_RadioAtpcPwrHigh_Object((1,3,6,1,4,1,3373,1103,80,9,1,8),_RadioAtpcPwrHigh_Type())
radioAtpcPwrHigh.setMaxAccess(_F)
if mibBuilder.loadTexts:radioAtpcPwrHigh.setStatus(_A)
class _RadioAtpcPwrLow_Type(Integer32):defaultValue=-60
_RadioAtpcPwrLow_Type.__name__=_C
_RadioAtpcPwrLow_Object=MibTableColumn
radioAtpcPwrLow=_RadioAtpcPwrLow_Object((1,3,6,1,4,1,3373,1103,80,9,1,9),_RadioAtpcPwrLow_Type())
radioAtpcPwrLow.setMaxAccess(_F)
if mibBuilder.loadTexts:radioAtpcPwrLow.setStatus(_A)
class _RadioAtpcRange_Type(Integer32):defaultValue=0
_RadioAtpcRange_Type.__name__=_C
_RadioAtpcRange_Object=MibTableColumn
radioAtpcRange=_RadioAtpcRange_Object((1,3,6,1,4,1,3373,1103,80,9,1,10),_RadioAtpcRange_Type())
radioAtpcRange.setMaxAccess(_F)
if mibBuilder.loadTexts:radioAtpcRange.setStatus(_A)
_RadioFreqTableSelection_Type=ChannelSpacing
_RadioFreqTableSelection_Object=MibTableColumn
radioFreqTableSelection=_RadioFreqTableSelection_Object((1,3,6,1,4,1,3373,1103,80,9,1,11),_RadioFreqTableSelection_Type())
radioFreqTableSelection.setMaxAccess(_F)
if mibBuilder.loadTexts:radioFreqTableSelection.setStatus(_A)
_TdmSettingsTable_Object=MibTable
tdmSettingsTable=_TdmSettingsTable_Object((1,3,6,1,4,1,3373,1103,80,10))
if mibBuilder.loadTexts:tdmSettingsTable.setStatus(_A)
_TdmSettingsEntry_Object=MibTableRow
tdmSettingsEntry=_TdmSettingsEntry_Object((1,3,6,1,4,1,3373,1103,80,10,1))
tdmSettingsEntry.setIndexNames((0,_E,_K),(0,_E,_j))
if mibBuilder.loadTexts:tdmSettingsEntry.setStatus(_A)
_TdmPolIndex_Type=Integer32
_TdmPolIndex_Object=MibTableColumn
tdmPolIndex=_TdmPolIndex_Object((1,3,6,1,4,1,3373,1103,80,10,1,1),_TdmPolIndex_Type())
tdmPolIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:tdmPolIndex.setStatus(_A)
class _TdmE1Channel_Type(Integer32):defaultValue=0
_TdmE1Channel_Type.__name__=_C
_TdmE1Channel_Object=MibTableColumn
tdmE1Channel=_TdmE1Channel_Object((1,3,6,1,4,1,3373,1103,80,10,1,2),_TdmE1Channel_Type())
tdmE1Channel.setMaxAccess(_D)
if mibBuilder.loadTexts:tdmE1Channel.setStatus(_A)
class _TdmE1Framer_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_TdmE1Framer_Type.__name__=_C
_TdmE1Framer_Object=MibTableColumn
tdmE1Framer=_TdmE1Framer_Object((1,3,6,1,4,1,3373,1103,80,10,1,3),_TdmE1Framer_Type())
tdmE1Framer.setMaxAccess(_D)
if mibBuilder.loadTexts:tdmE1Framer.setStatus(_A)
_RadioCapabilitiesTable_Object=MibTable
radioCapabilitiesTable=_RadioCapabilitiesTable_Object((1,3,6,1,4,1,3373,1103,80,11))
if mibBuilder.loadTexts:radioCapabilitiesTable.setStatus(_A)
_RadioCapabilitiesEntry_Object=MibTableRow
radioCapabilitiesEntry=_RadioCapabilitiesEntry_Object((1,3,6,1,4,1,3373,1103,80,11,1))
radioCapabilitiesEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:radioCapabilitiesEntry.setStatus(_A)
_RadioCapabilitiesCapability_Type=RadioCapability
_RadioCapabilitiesCapability_Object=MibTableColumn
radioCapabilitiesCapability=_RadioCapabilitiesCapability_Object((1,3,6,1,4,1,3373,1103,80,11,1,1),_RadioCapabilitiesCapability_Type())
radioCapabilitiesCapability.setMaxAccess(_B)
if mibBuilder.loadTexts:radioCapabilitiesCapability.setStatus(_A)
_RadioCapabilitiesTxMinFrequency_Type=Integer32
_RadioCapabilitiesTxMinFrequency_Object=MibTableColumn
radioCapabilitiesTxMinFrequency=_RadioCapabilitiesTxMinFrequency_Object((1,3,6,1,4,1,3373,1103,80,11,1,2),_RadioCapabilitiesTxMinFrequency_Type())
radioCapabilitiesTxMinFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:radioCapabilitiesTxMinFrequency.setStatus(_A)
_RadioCapabilitiesTxMaxFrequency_Type=Integer32
_RadioCapabilitiesTxMaxFrequency_Object=MibTableColumn
radioCapabilitiesTxMaxFrequency=_RadioCapabilitiesTxMaxFrequency_Object((1,3,6,1,4,1,3373,1103,80,11,1,3),_RadioCapabilitiesTxMaxFrequency_Type())
radioCapabilitiesTxMaxFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:radioCapabilitiesTxMaxFrequency.setStatus(_A)
_RadioCapabilitiesStepFrequency_Type=Integer32
_RadioCapabilitiesStepFrequency_Object=MibTableColumn
radioCapabilitiesStepFrequency=_RadioCapabilitiesStepFrequency_Object((1,3,6,1,4,1,3373,1103,80,11,1,4),_RadioCapabilitiesStepFrequency_Type())
radioCapabilitiesStepFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:radioCapabilitiesStepFrequency.setStatus(_A)
_RadioCapabilitiesMinPtxNominalValue_Type=Integer32
_RadioCapabilitiesMinPtxNominalValue_Object=MibTableColumn
radioCapabilitiesMinPtxNominalValue=_RadioCapabilitiesMinPtxNominalValue_Object((1,3,6,1,4,1,3373,1103,80,11,1,5),_RadioCapabilitiesMinPtxNominalValue_Type())
radioCapabilitiesMinPtxNominalValue.setMaxAccess(_B)
if mibBuilder.loadTexts:radioCapabilitiesMinPtxNominalValue.setStatus(_A)
_RadioCapabilitiesMaxPtxNominalValue_Type=Integer32
_RadioCapabilitiesMaxPtxNominalValue_Object=MibTableColumn
radioCapabilitiesMaxPtxNominalValue=_RadioCapabilitiesMaxPtxNominalValue_Object((1,3,6,1,4,1,3373,1103,80,11,1,6),_RadioCapabilitiesMaxPtxNominalValue_Type())
radioCapabilitiesMaxPtxNominalValue.setMaxAccess(_B)
if mibBuilder.loadTexts:radioCapabilitiesMaxPtxNominalValue.setStatus(_A)
_RadioCapabilitiesExtendedMinPwr_Type=Integer32
_RadioCapabilitiesExtendedMinPwr_Object=MibTableColumn
radioCapabilitiesExtendedMinPwr=_RadioCapabilitiesExtendedMinPwr_Object((1,3,6,1,4,1,3373,1103,80,11,1,7),_RadioCapabilitiesExtendedMinPwr_Type())
radioCapabilitiesExtendedMinPwr.setMaxAccess(_B)
if mibBuilder.loadTexts:radioCapabilitiesExtendedMinPwr.setStatus(_A)
_RadioStatusTable_Object=MibTable
radioStatusTable=_RadioStatusTable_Object((1,3,6,1,4,1,3373,1103,80,12))
if mibBuilder.loadTexts:radioStatusTable.setStatus(_A)
_RadioStatusEntry_Object=MibTableRow
radioStatusEntry=_RadioStatusEntry_Object((1,3,6,1,4,1,3373,1103,80,12,1))
radioStatusEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:radioStatusEntry.setStatus(_A)
_RadioCurrentDuplexFrequency_Type=Integer32
_RadioCurrentDuplexFrequency_Object=MibTableColumn
radioCurrentDuplexFrequency=_RadioCurrentDuplexFrequency_Object((1,3,6,1,4,1,3373,1103,80,12,1,1),_RadioCurrentDuplexFrequency_Type())
radioCurrentDuplexFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:radioCurrentDuplexFrequency.setStatus(_A)
_RadioTxChannelSpacing_Type=Integer32
_RadioTxChannelSpacing_Object=MibTableColumn
radioTxChannelSpacing=_RadioTxChannelSpacing_Object((1,3,6,1,4,1,3373,1103,80,12,1,2),_RadioTxChannelSpacing_Type())
radioTxChannelSpacing.setMaxAccess(_B)
if mibBuilder.loadTexts:radioTxChannelSpacing.setStatus(_A)
_RadioPrx_Type=Integer32
_RadioPrx_Object=MibTableColumn
radioPrx=_RadioPrx_Object((1,3,6,1,4,1,3373,1103,80,12,1,3),_RadioPrx_Type())
radioPrx.setMaxAccess(_B)
if mibBuilder.loadTexts:radioPrx.setStatus(_A)
_RadioPtx_Type=Integer32
_RadioPtx_Object=MibTableColumn
radioPtx=_RadioPtx_Object((1,3,6,1,4,1,3373,1103,80,12,1,4),_RadioPtx_Type())
radioPtx.setMaxAccess(_B)
if mibBuilder.loadTexts:radioPtx.setStatus(_A)
_RadioNormalizedMse_Type=Integer32
_RadioNormalizedMse_Object=MibTableColumn
radioNormalizedMse=_RadioNormalizedMse_Object((1,3,6,1,4,1,3373,1103,80,12,1,5),_RadioNormalizedMse_Type())
radioNormalizedMse.setMaxAccess(_B)
if mibBuilder.loadTexts:radioNormalizedMse.setStatus(_A)
class _RadioRxActiveStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_Y,2)))
_RadioRxActiveStatus_Type.__name__=_C
_RadioRxActiveStatus_Object=MibTableColumn
radioRxActiveStatus=_RadioRxActiveStatus_Object((1,3,6,1,4,1,3373,1103,80,12,1,6),_RadioRxActiveStatus_Type())
radioRxActiveStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:radioRxActiveStatus.setStatus(_A)
class _RadioTxActiveStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_Y,2)))
_RadioTxActiveStatus_Type.__name__=_C
_RadioTxActiveStatus_Object=MibTableColumn
radioTxActiveStatus=_RadioTxActiveStatus_Object((1,3,6,1,4,1,3373,1103,80,12,1,7),_RadioTxActiveStatus_Type())
radioTxActiveStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:radioTxActiveStatus.setStatus(_A)
_RadioCableOpenAlarm_Type=AlarmStatus
_RadioCableOpenAlarm_Object=MibTableColumn
radioCableOpenAlarm=_RadioCableOpenAlarm_Object((1,3,6,1,4,1,3373,1103,80,12,1,8),_RadioCableOpenAlarm_Type())
radioCableOpenAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:radioCableOpenAlarm.setStatus(_A)
_RadioCableShortAlarm_Type=AlarmStatus
_RadioCableShortAlarm_Object=MibTableColumn
radioCableShortAlarm=_RadioCableShortAlarm_Object((1,3,6,1,4,1,3373,1103,80,12,1,9),_RadioCableShortAlarm_Type())
radioCableShortAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:radioCableShortAlarm.setStatus(_A)
_RadioInvalidFrequencyAlarm_Type=AlarmStatus
_RadioInvalidFrequencyAlarm_Object=MibTableColumn
radioInvalidFrequencyAlarm=_RadioInvalidFrequencyAlarm_Object((1,3,6,1,4,1,3373,1103,80,12,1,10),_RadioInvalidFrequencyAlarm_Type())
radioInvalidFrequencyAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:radioInvalidFrequencyAlarm.setStatus(_A)
_RadioBaseBandRxAlarm_Type=AlarmStatus
_RadioBaseBandRxAlarm_Object=MibTableColumn
radioBaseBandRxAlarm=_RadioBaseBandRxAlarm_Object((1,3,6,1,4,1,3373,1103,80,12,1,11),_RadioBaseBandRxAlarm_Type())
radioBaseBandRxAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:radioBaseBandRxAlarm.setStatus(_A)
_RadioModulatorFailAlarm_Type=AlarmStatus
_RadioModulatorFailAlarm_Object=MibTableColumn
radioModulatorFailAlarm=_RadioModulatorFailAlarm_Object((1,3,6,1,4,1,3373,1103,80,12,1,12),_RadioModulatorFailAlarm_Type())
radioModulatorFailAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:radioModulatorFailAlarm.setStatus(_A)
_RadioDemodulatorFailAlarm_Type=AlarmStatus
_RadioDemodulatorFailAlarm_Object=MibTableColumn
radioDemodulatorFailAlarm=_RadioDemodulatorFailAlarm_Object((1,3,6,1,4,1,3373,1103,80,12,1,13),_RadioDemodulatorFailAlarm_Type())
radioDemodulatorFailAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:radioDemodulatorFailAlarm.setStatus(_A)
_RadioRxPowerLowAlarm_Type=AlarmStatus
_RadioRxPowerLowAlarm_Object=MibTableColumn
radioRxPowerLowAlarm=_RadioRxPowerLowAlarm_Object((1,3,6,1,4,1,3373,1103,80,12,1,14),_RadioRxPowerLowAlarm_Type())
radioRxPowerLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:radioRxPowerLowAlarm.setStatus(_A)
_RadioTxPowerLowAlarm_Type=AlarmStatus
_RadioTxPowerLowAlarm_Object=MibTableColumn
radioTxPowerLowAlarm=_RadioTxPowerLowAlarm_Object((1,3,6,1,4,1,3373,1103,80,12,1,15),_RadioTxPowerLowAlarm_Type())
radioTxPowerLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:radioTxPowerLowAlarm.setStatus(_A)
_RadioRemDemodulatorFailAlarm_Type=AlarmStatus
_RadioRemDemodulatorFailAlarm_Object=MibTableColumn
radioRemDemodulatorFailAlarm=_RadioRemDemodulatorFailAlarm_Object((1,3,6,1,4,1,3373,1103,80,12,1,16),_RadioRemDemodulatorFailAlarm_Type())
radioRemDemodulatorFailAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:radioRemDemodulatorFailAlarm.setStatus(_A)
_RadioVcoFailAlarm_Type=AlarmStatus
_RadioVcoFailAlarm_Object=MibTableColumn
radioVcoFailAlarm=_RadioVcoFailAlarm_Object((1,3,6,1,4,1,3373,1103,80,12,1,17),_RadioVcoFailAlarm_Type())
radioVcoFailAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:radioVcoFailAlarm.setStatus(_A)
_RadioRxIFAgcAlarm_Type=AlarmStatus
_RadioRxIFAgcAlarm_Object=MibTableColumn
radioRxIFAgcAlarm=_RadioRxIFAgcAlarm_Object((1,3,6,1,4,1,3373,1103,80,12,1,18),_RadioRxIFAgcAlarm_Type())
radioRxIFAgcAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:radioRxIFAgcAlarm.setStatus(_A)
_RadioTxIFAgcAlarm_Type=AlarmStatus
_RadioTxIFAgcAlarm_Object=MibTableColumn
radioTxIFAgcAlarm=_RadioTxIFAgcAlarm_Object((1,3,6,1,4,1,3373,1103,80,12,1,19),_RadioTxIFAgcAlarm_Type())
radioTxIFAgcAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:radioTxIFAgcAlarm.setStatus(_A)
_RadioIduOduCommunicationAlarm_Type=AlarmStatus
_RadioIduOduCommunicationAlarm_Object=MibTableColumn
radioIduOduCommunicationAlarm=_RadioIduOduCommunicationAlarm_Object((1,3,6,1,4,1,3373,1103,80,12,1,20),_RadioIduOduCommunicationAlarm_Type())
radioIduOduCommunicationAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:radioIduOduCommunicationAlarm.setStatus(_A)
_RadioOduIduCommunicationAlarm_Type=AlarmStatus
_RadioOduIduCommunicationAlarm_Object=MibTableColumn
radioOduIduCommunicationAlarm=_RadioOduIduCommunicationAlarm_Object((1,3,6,1,4,1,3373,1103,80,12,1,21),_RadioOduIduCommunicationAlarm_Type())
radioOduIduCommunicationAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:radioOduIduCommunicationAlarm.setStatus(_A)
_RadioLocalOduAlarmSynthesis_Type=AlarmStatus
_RadioLocalOduAlarmSynthesis_Object=MibTableColumn
radioLocalOduAlarmSynthesis=_RadioLocalOduAlarmSynthesis_Object((1,3,6,1,4,1,3373,1103,80,12,1,22),_RadioLocalOduAlarmSynthesis_Type())
radioLocalOduAlarmSynthesis.setMaxAccess(_B)
if mibBuilder.loadTexts:radioLocalOduAlarmSynthesis.setStatus(_A)
_RadioRemoteOduAlarmSynthesis_Type=AlarmStatus
_RadioRemoteOduAlarmSynthesis_Object=MibTableColumn
radioRemoteOduAlarmSynthesis=_RadioRemoteOduAlarmSynthesis_Object((1,3,6,1,4,1,3373,1103,80,12,1,23),_RadioRemoteOduAlarmSynthesis_Type())
radioRemoteOduAlarmSynthesis.setMaxAccess(_B)
if mibBuilder.loadTexts:radioRemoteOduAlarmSynthesis.setStatus(_A)
_RadioConfigMismatchAlarm_Type=AlarmStatus
_RadioConfigMismatchAlarm_Object=MibTableColumn
radioConfigMismatchAlarm=_RadioConfigMismatchAlarm_Object((1,3,6,1,4,1,3373,1103,80,12,1,24),_RadioConfigMismatchAlarm_Type())
radioConfigMismatchAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:radioConfigMismatchAlarm.setStatus(_A)
_RadioConfigAlarmReason_Type=ConfigMismatchReason
_RadioConfigAlarmReason_Object=MibTableColumn
radioConfigAlarmReason=_RadioConfigAlarmReason_Object((1,3,6,1,4,1,3373,1103,80,12,1,25),_RadioConfigAlarmReason_Type())
radioConfigAlarmReason.setMaxAccess(_B)
if mibBuilder.loadTexts:radioConfigAlarmReason.setStatus(_A)
_RadioRxQualityLowAlarm_Type=AlarmStatus
_RadioRxQualityLowAlarm_Object=MibTableColumn
radioRxQualityLowAlarm=_RadioRxQualityLowAlarm_Object((1,3,6,1,4,1,3373,1103,80,12,1,26),_RadioRxQualityLowAlarm_Type())
radioRxQualityLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:radioRxQualityLowAlarm.setStatus(_A)
_RadioRxQualityWarningAlarm_Type=AlarmStatus
_RadioRxQualityWarningAlarm_Object=MibTableColumn
radioRxQualityWarningAlarm=_RadioRxQualityWarningAlarm_Object((1,3,6,1,4,1,3373,1103,80,12,1,27),_RadioRxQualityWarningAlarm_Type())
radioRxQualityWarningAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:radioRxQualityWarningAlarm.setStatus(_A)
_RadioXpd_Type=Integer32
_RadioXpd_Object=MibTableColumn
radioXpd=_RadioXpd_Object((1,3,6,1,4,1,3373,1103,80,12,1,28),_RadioXpd_Type())
radioXpd.setMaxAccess(_B)
if mibBuilder.loadTexts:radioXpd.setStatus(_A)
_RadioXpicAlarm_Type=AlarmStatus
_RadioXpicAlarm_Object=MibTableColumn
radioXpicAlarm=_RadioXpicAlarm_Object((1,3,6,1,4,1,3373,1103,80,12,1,29),_RadioXpicAlarm_Type())
radioXpicAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:radioXpicAlarm.setStatus(_A)
_RadioMaintTable_Object=MibTable
radioMaintTable=_RadioMaintTable_Object((1,3,6,1,4,1,3373,1103,80,13))
if mibBuilder.loadTexts:radioMaintTable.setStatus(_A)
_RadioMaintEntry_Object=MibTableRow
radioMaintEntry=_RadioMaintEntry_Object((1,3,6,1,4,1,3373,1103,80,13,1))
radioMaintEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:radioMaintEntry.setStatus(_A)
class _RadioTxStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('transmitterOff',1),('transmitterOn',2),('permanentOff',3)))
_RadioTxStatus_Type.__name__=_C
_RadioTxStatus_Object=MibTableColumn
radioTxStatus=_RadioTxStatus_Object((1,3,6,1,4,1,3373,1103,80,13,1,1),_RadioTxStatus_Type())
radioTxStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:radioTxStatus.setStatus(_A)
class _RadioCarrierOnly_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('carrierOnlyOff',1),('carrierOnlyOn',2)))
_RadioCarrierOnly_Type.__name__=_C
_RadioCarrierOnly_Object=MibTableColumn
radioCarrierOnly=_RadioCarrierOnly_Object((1,3,6,1,4,1,3373,1103,80,13,1,2),_RadioCarrierOnly_Type())
radioCarrierOnly.setMaxAccess(_D)
if mibBuilder.loadTexts:radioCarrierOnly.setStatus(_A)
class _RadioLoop_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,6,7,8,9)));namedValues=NamedValues(*(('loopOff',1),('rfLoop',2),('iqLoop',3),(_e,4),('rfLoopAtFixedMod',6),('baseBandLoopEthSquelch',7),('rfLoopAtFixedModEthSquelch',8),('iqloopEthSquelch',9)))
_RadioLoop_Type.__name__=_C
_RadioLoop_Object=MibTableColumn
radioLoop=_RadioLoop_Object((1,3,6,1,4,1,3373,1103,80,13,1,3),_RadioLoop_Type())
radioLoop.setMaxAccess(_D)
if mibBuilder.loadTexts:radioLoop.setStatus(_A)
class _RadioRFLoopTestResult_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('testNone',0),('testRunning',1),('testNotPossible',2),('testPassed',3),('testFail',4),('testInterrupted',5)))
_RadioRFLoopTestResult_Type.__name__=_C
_RadioRFLoopTestResult_Object=MibTableColumn
radioRFLoopTestResult=_RadioRFLoopTestResult_Object((1,3,6,1,4,1,3373,1103,80,13,1,4),_RadioRFLoopTestResult_Type())
radioRFLoopTestResult.setMaxAccess(_B)
if mibBuilder.loadTexts:radioRFLoopTestResult.setStatus(_A)
class _RadioRFLoopTestPercTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_RadioRFLoopTestPercTime_Type.__name__=_C
_RadioRFLoopTestPercTime_Object=MibTableColumn
radioRFLoopTestPercTime=_RadioRFLoopTestPercTime_Object((1,3,6,1,4,1,3373,1103,80,13,1,5),_RadioRFLoopTestPercTime_Type())
radioRFLoopTestPercTime.setMaxAccess(_B)
if mibBuilder.loadTexts:radioRFLoopTestPercTime.setStatus(_A)
class _RadioRtPsuOff_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('rtPsuOff',1),('rtPsuOn',2)))
_RadioRtPsuOff_Type.__name__=_C
_RadioRtPsuOff_Object=MibTableColumn
radioRtPsuOff=_RadioRtPsuOff_Object((1,3,6,1,4,1,3373,1103,80,13,1,6),_RadioRtPsuOff_Type())
radioRtPsuOff.setMaxAccess(_D)
if mibBuilder.loadTexts:radioRtPsuOff.setStatus(_A)
class _RadioLom_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_RadioLom_Type.__name__=_C
_RadioLom_Object=MibTableColumn
radioLom=_RadioLom_Object((1,3,6,1,4,1,3373,1103,80,13,1,7),_RadioLom_Type())
radioLom.setMaxAccess(_D)
if mibBuilder.loadTexts:radioLom.setStatus(_A)
class _RadioXpic_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_RadioXpic_Type.__name__=_C
_RadioXpic_Object=MibTableColumn
radioXpic=_RadioXpic_Object((1,3,6,1,4,1,3373,1103,80,13,1,8),_RadioXpic_Type())
radioXpic.setMaxAccess(_D)
if mibBuilder.loadTexts:radioXpic.setStatus(_A)
_RadioFrequencyTable_Object=MibTable
radioFrequencyTable=_RadioFrequencyTable_Object((1,3,6,1,4,1,3373,1103,80,14))
if mibBuilder.loadTexts:radioFrequencyTable.setStatus(_A)
_RadioFreqTabEntry_Object=MibTableRow
radioFreqTabEntry=_RadioFreqTabEntry_Object((1,3,6,1,4,1,3373,1103,80,14,1))
radioFreqTabEntry.setIndexNames((0,_E,_L),(0,_E,_k))
if mibBuilder.loadTexts:radioFreqTabEntry.setStatus(_A)
_RadioFreqChannelId_Type=Integer32
_RadioFreqChannelId_Object=MibTableColumn
radioFreqChannelId=_RadioFreqChannelId_Object((1,3,6,1,4,1,3373,1103,80,14,1,1),_RadioFreqChannelId_Type())
radioFreqChannelId.setMaxAccess(_B)
if mibBuilder.loadTexts:radioFreqChannelId.setStatus(_A)
_RadioFreqChannelNum_Type=Integer32
_RadioFreqChannelNum_Object=MibTableColumn
radioFreqChannelNum=_RadioFreqChannelNum_Object((1,3,6,1,4,1,3373,1103,80,14,1,2),_RadioFreqChannelNum_Type())
radioFreqChannelNum.setMaxAccess(_B)
if mibBuilder.loadTexts:radioFreqChannelNum.setStatus(_A)
_RadioFreqValue_Type=Integer32
_RadioFreqValue_Object=MibTableColumn
radioFreqValue=_RadioFreqValue_Object((1,3,6,1,4,1,3373,1103,80,14,1,3),_RadioFreqValue_Type())
radioFreqValue.setMaxAccess(_B)
if mibBuilder.loadTexts:radioFreqValue.setStatus(_A)
_RadioDuplexFrequencyTable_Object=MibTable
radioDuplexFrequencyTable=_RadioDuplexFrequencyTable_Object((1,3,6,1,4,1,3373,1103,80,15))
if mibBuilder.loadTexts:radioDuplexFrequencyTable.setStatus(_A)
_RadioDuplexFreqEntry_Object=MibTableRow
radioDuplexFreqEntry=_RadioDuplexFreqEntry_Object((1,3,6,1,4,1,3373,1103,80,15,1))
radioDuplexFreqEntry.setIndexNames((0,_E,_L),(0,_E,_l))
if mibBuilder.loadTexts:radioDuplexFreqEntry.setStatus(_A)
_RadioDuplexFreqId_Type=Integer32
_RadioDuplexFreqId_Object=MibTableColumn
radioDuplexFreqId=_RadioDuplexFreqId_Object((1,3,6,1,4,1,3373,1103,80,15,1,1),_RadioDuplexFreqId_Type())
radioDuplexFreqId.setMaxAccess(_B)
if mibBuilder.loadTexts:radioDuplexFreqId.setStatus(_A)
_RadioDuplexFreqValue_Type=Integer32
_RadioDuplexFreqValue_Object=MibTableColumn
radioDuplexFreqValue=_RadioDuplexFreqValue_Object((1,3,6,1,4,1,3373,1103,80,15,1,2),_RadioDuplexFreqValue_Type())
radioDuplexFreqValue.setMaxAccess(_B)
if mibBuilder.loadTexts:radioDuplexFreqValue.setStatus(_A)
_RadioModulationTable_Object=MibTable
radioModulationTable=_RadioModulationTable_Object((1,3,6,1,4,1,3373,1103,80,16))
if mibBuilder.loadTexts:radioModulationTable.setStatus(_A)
_RadioModulationEntry_Object=MibTableRow
radioModulationEntry=_RadioModulationEntry_Object((1,3,6,1,4,1,3373,1103,80,16,1))
radioModulationEntry.setIndexNames((0,_E,_L),(0,_E,_m))
if mibBuilder.loadTexts:radioModulationEntry.setStatus(_A)
_RadioChannelSpacing_Type=ChannelSpacing
_RadioChannelSpacing_Object=MibTableColumn
radioChannelSpacing=_RadioChannelSpacing_Object((1,3,6,1,4,1,3373,1103,80,16,1,1),_RadioChannelSpacing_Type())
radioChannelSpacing.setMaxAccess(_B)
if mibBuilder.loadTexts:radioChannelSpacing.setStatus(_A)
_RadioModulationMap_Type=ModulationMap
_RadioModulationMap_Object=MibTableColumn
radioModulationMap=_RadioModulationMap_Object((1,3,6,1,4,1,3373,1103,80,16,1,2),_RadioModulationMap_Type())
radioModulationMap.setMaxAccess(_B)
if mibBuilder.loadTexts:radioModulationMap.setStatus(_A)
_RadioRefModulationMap_Type=ModulationMap
_RadioRefModulationMap_Object=MibTableColumn
radioRefModulationMap=_RadioRefModulationMap_Object((1,3,6,1,4,1,3373,1103,80,16,1,3),_RadioRefModulationMap_Type())
radioRefModulationMap.setMaxAccess(_B)
if mibBuilder.loadTexts:radioRefModulationMap.setStatus(_A)
_LinkStatusTable_Object=MibTable
linkStatusTable=_LinkStatusTable_Object((1,3,6,1,4,1,3373,1103,80,17))
if mibBuilder.loadTexts:linkStatusTable.setStatus(_A)
_LinkStatusEntry_Object=MibTableRow
linkStatusEntry=_LinkStatusEntry_Object((1,3,6,1,4,1,3373,1103,80,17,1))
linkStatusEntry.setIndexNames((0,_E,_K),(0,_E,_M))
if mibBuilder.loadTexts:linkStatusEntry.setStatus(_A)
class _LinkPolIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_LinkPolIndex_Type.__name__=_C
_LinkPolIndex_Object=MibTableColumn
linkPolIndex=_LinkPolIndex_Object((1,3,6,1,4,1,3373,1103,80,17,1,1),_LinkPolIndex_Type())
linkPolIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:linkPolIndex.setStatus(_A)
_LinkAcmRxProfile_Type=Integer32
_LinkAcmRxProfile_Object=MibTableColumn
linkAcmRxProfile=_LinkAcmRxProfile_Object((1,3,6,1,4,1,3373,1103,80,17,1,2),_LinkAcmRxProfile_Type())
linkAcmRxProfile.setMaxAccess(_B)
if mibBuilder.loadTexts:linkAcmRxProfile.setStatus(_A)
_LinkAcmTxProfile_Type=Integer32
_LinkAcmTxProfile_Object=MibTableColumn
linkAcmTxProfile=_LinkAcmTxProfile_Object((1,3,6,1,4,1,3373,1103,80,17,1,3),_LinkAcmTxProfile_Type())
linkAcmTxProfile.setMaxAccess(_B)
if mibBuilder.loadTexts:linkAcmTxProfile.setStatus(_A)
class _LinkAcmRxProfileLabel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_LinkAcmRxProfileLabel_Type.__name__=_N
_LinkAcmRxProfileLabel_Object=MibTableColumn
linkAcmRxProfileLabel=_LinkAcmRxProfileLabel_Object((1,3,6,1,4,1,3373,1103,80,17,1,4),_LinkAcmRxProfileLabel_Type())
linkAcmRxProfileLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:linkAcmRxProfileLabel.setStatus(_A)
class _LinkAcmTxProfileLabel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_LinkAcmTxProfileLabel_Type.__name__=_N
_LinkAcmTxProfileLabel_Object=MibTableColumn
linkAcmTxProfileLabel=_LinkAcmTxProfileLabel_Object((1,3,6,1,4,1,3373,1103,80,17,1,5),_LinkAcmTxProfileLabel_Type())
linkAcmTxProfileLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:linkAcmTxProfileLabel.setStatus(_A)
_LinkAcmRxModulation_Type=BitsPerSymbol
_LinkAcmRxModulation_Object=MibTableColumn
linkAcmRxModulation=_LinkAcmRxModulation_Object((1,3,6,1,4,1,3373,1103,80,17,1,6),_LinkAcmRxModulation_Type())
linkAcmRxModulation.setMaxAccess(_B)
if mibBuilder.loadTexts:linkAcmRxModulation.setStatus(_A)
_LinkAcmTxModulation_Type=BitsPerSymbol
_LinkAcmTxModulation_Object=MibTableColumn
linkAcmTxModulation=_LinkAcmTxModulation_Object((1,3,6,1,4,1,3373,1103,80,17,1,7),_LinkAcmTxModulation_Type())
linkAcmTxModulation.setMaxAccess(_B)
if mibBuilder.loadTexts:linkAcmTxModulation.setStatus(_A)
class _LinkAcmRxCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_n,0),(_Z,1),(_a,2)))
_LinkAcmRxCode_Type.__name__=_C
_LinkAcmRxCode_Object=MibTableColumn
linkAcmRxCode=_LinkAcmRxCode_Object((1,3,6,1,4,1,3373,1103,80,17,1,8),_LinkAcmRxCode_Type())
linkAcmRxCode.setMaxAccess(_B)
if mibBuilder.loadTexts:linkAcmRxCode.setStatus(_A)
class _LinkAcmTxCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_n,0),(_Z,1),(_a,2)))
_LinkAcmTxCode_Type.__name__=_C
_LinkAcmTxCode_Object=MibTableColumn
linkAcmTxCode=_LinkAcmTxCode_Object((1,3,6,1,4,1,3373,1103,80,17,1,9),_LinkAcmTxCode_Type())
linkAcmTxCode.setMaxAccess(_B)
if mibBuilder.loadTexts:linkAcmTxCode.setStatus(_A)
class _LinkTxETHCapacity_Type(Integer32):defaultValue=0
_LinkTxETHCapacity_Type.__name__=_C
_LinkTxETHCapacity_Object=MibTableColumn
linkTxETHCapacity=_LinkTxETHCapacity_Object((1,3,6,1,4,1,3373,1103,80,17,1,10),_LinkTxETHCapacity_Type())
linkTxETHCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:linkTxETHCapacity.setStatus(_A)
class _LinkRxETHCapacity_Type(Integer32):defaultValue=0
_LinkRxETHCapacity_Type.__name__=_C
_LinkRxETHCapacity_Object=MibTableColumn
linkRxETHCapacity=_LinkRxETHCapacity_Object((1,3,6,1,4,1,3373,1103,80,17,1,11),_LinkRxETHCapacity_Type())
linkRxETHCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:linkRxETHCapacity.setStatus(_A)
class _LinkTxTDMCapacity_Type(Integer32):defaultValue=0
_LinkTxTDMCapacity_Type.__name__=_C
_LinkTxTDMCapacity_Object=MibTableColumn
linkTxTDMCapacity=_LinkTxTDMCapacity_Object((1,3,6,1,4,1,3373,1103,80,17,1,12),_LinkTxTDMCapacity_Type())
linkTxTDMCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:linkTxTDMCapacity.setStatus(_A)
class _LinkRxTDMCapacity_Type(Integer32):defaultValue=0
_LinkRxTDMCapacity_Type.__name__=_C
_LinkRxTDMCapacity_Object=MibTableColumn
linkRxTDMCapacity=_LinkRxTDMCapacity_Object((1,3,6,1,4,1,3373,1103,80,17,1,13),_LinkRxTDMCapacity_Type())
linkRxTDMCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:linkRxTDMCapacity.setStatus(_A)
class _LinkRescueModulation_Type(BitsPerSymbol):defaultValue=2
_LinkRescueModulation_Type.__name__=_o
_LinkRescueModulation_Object=MibTableColumn
linkRescueModulation=_LinkRescueModulation_Object((1,3,6,1,4,1,3373,1103,80,17,1,14),_LinkRescueModulation_Type())
linkRescueModulation.setMaxAccess(_B)
if mibBuilder.loadTexts:linkRescueModulation.setStatus(_A)
_LinkReducedCapacityAlarm_Type=AlarmStatus
_LinkReducedCapacityAlarm_Object=MibTableColumn
linkReducedCapacityAlarm=_LinkReducedCapacityAlarm_Object((1,3,6,1,4,1,3373,1103,80,17,1,15),_LinkReducedCapacityAlarm_Type())
linkReducedCapacityAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:linkReducedCapacityAlarm.setStatus(_A)
_LinkLinkTelemetryFailAlarm_Type=AlarmStatus
_LinkLinkTelemetryFailAlarm_Object=MibTableColumn
linkLinkTelemetryFailAlarm=_LinkLinkTelemetryFailAlarm_Object((1,3,6,1,4,1,3373,1103,80,17,1,16),_LinkLinkTelemetryFailAlarm_Type())
linkLinkTelemetryFailAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:linkLinkTelemetryFailAlarm.setStatus(_A)
_LinkIdMismatchAlarm_Type=AlarmStatus
_LinkIdMismatchAlarm_Object=MibTableColumn
linkIdMismatchAlarm=_LinkIdMismatchAlarm_Object((1,3,6,1,4,1,3373,1103,80,17,1,17),_LinkIdMismatchAlarm_Type())
linkIdMismatchAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:linkIdMismatchAlarm.setStatus(_A)
_LinkRadioEocAlarm_Type=AlarmStatus
_LinkRadioEocAlarm_Object=MibTableColumn
linkRadioEocAlarm=_LinkRadioEocAlarm_Object((1,3,6,1,4,1,3373,1103,80,17,1,18),_LinkRadioEocAlarm_Type())
linkRadioEocAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:linkRadioEocAlarm.setStatus(_A)
_LinkSetupMismatchAlarm_Type=AlarmStatus
_LinkSetupMismatchAlarm_Object=MibTableColumn
linkSetupMismatchAlarm=_LinkSetupMismatchAlarm_Object((1,3,6,1,4,1,3373,1103,80,17,1,19),_LinkSetupMismatchAlarm_Type())
linkSetupMismatchAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:linkSetupMismatchAlarm.setStatus(_A)
_LinkRescueSetupAlarm_Type=AlarmStatus
_LinkRescueSetupAlarm_Object=MibTableColumn
linkRescueSetupAlarm=_LinkRescueSetupAlarm_Object((1,3,6,1,4,1,3373,1103,80,17,1,20),_LinkRescueSetupAlarm_Type())
linkRescueSetupAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:linkRescueSetupAlarm.setStatus(_A)
_LinkXpicProcedureBlockAlarm_Type=AlarmStatus
_LinkXpicProcedureBlockAlarm_Object=MibTableColumn
linkXpicProcedureBlockAlarm=_LinkXpicProcedureBlockAlarm_Object((1,3,6,1,4,1,3373,1103,80,17,1,21),_LinkXpicProcedureBlockAlarm_Type())
linkXpicProcedureBlockAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:linkXpicProcedureBlockAlarm.setStatus(_A)
_LinkXpicRemTxOffAlarm_Type=AlarmStatus
_LinkXpicRemTxOffAlarm_Object=MibTableColumn
linkXpicRemTxOffAlarm=_LinkXpicRemTxOffAlarm_Object((1,3,6,1,4,1,3373,1103,80,17,1,22),_LinkXpicRemTxOffAlarm_Type())
linkXpicRemTxOffAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:linkXpicRemTxOffAlarm.setStatus(_A)
_LinkRemoteIduAlarmSynthesis_Type=AlarmStatus
_LinkRemoteIduAlarmSynthesis_Object=MibTableColumn
linkRemoteIduAlarmSynthesis=_LinkRemoteIduAlarmSynthesis_Object((1,3,6,1,4,1,3373,1103,80,17,1,23),_LinkRemoteIduAlarmSynthesis_Type())
linkRemoteIduAlarmSynthesis.setMaxAccess(_B)
if mibBuilder.loadTexts:linkRemoteIduAlarmSynthesis.setStatus(_A)
_LinkNotMatchingRadiosAlarm_Type=AlarmStatus
_LinkNotMatchingRadiosAlarm_Object=MibTableColumn
linkNotMatchingRadiosAlarm=_LinkNotMatchingRadiosAlarm_Object((1,3,6,1,4,1,3373,1103,80,17,1,24),_LinkNotMatchingRadiosAlarm_Type())
linkNotMatchingRadiosAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:linkNotMatchingRadiosAlarm.setStatus(_A)
class _LinkConfigurationInProgress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_Y,2)))
_LinkConfigurationInProgress_Type.__name__=_C
_LinkConfigurationInProgress_Object=MibTableColumn
linkConfigurationInProgress=_LinkConfigurationInProgress_Object((1,3,6,1,4,1,3373,1103,80,17,1,25),_LinkConfigurationInProgress_Type())
linkConfigurationInProgress.setMaxAccess(_B)
if mibBuilder.loadTexts:linkConfigurationInProgress.setStatus(_A)
_LinkXpd_Type=Integer32
_LinkXpd_Object=MibTableColumn
linkXpd=_LinkXpd_Object((1,3,6,1,4,1,3373,1103,80,17,1,26),_LinkXpd_Type())
linkXpd.setMaxAccess(_B)
if mibBuilder.loadTexts:linkXpd.setStatus(_G)
_LinkTfcTable_Object=MibTable
linkTfcTable=_LinkTfcTable_Object((1,3,6,1,4,1,3373,1103,80,18))
if mibBuilder.loadTexts:linkTfcTable.setStatus(_G)
_LinkTfcEntry_Object=MibTableRow
linkTfcEntry=_LinkTfcEntry_Object((1,3,6,1,4,1,3373,1103,80,18,1))
linkTfcEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:linkTfcEntry.setStatus(_G)
class _LinkTfcAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_O,0),(_b,1)))
_LinkTfcAction_Type.__name__=_C
_LinkTfcAction_Object=MibTableColumn
linkTfcAction=_LinkTfcAction_Object((1,3,6,1,4,1,3373,1103,80,18,1,1),_LinkTfcAction_Type())
linkTfcAction.setMaxAccess(_F)
if mibBuilder.loadTexts:linkTfcAction.setStatus(_G)
class _LinkTfcControl_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_LinkTfcControl_Type.__name__=_C
_LinkTfcControl_Object=MibTableColumn
linkTfcControl=_LinkTfcControl_Object((1,3,6,1,4,1,3373,1103,80,18,1,2),_LinkTfcControl_Type())
linkTfcControl.setMaxAccess(_F)
if mibBuilder.loadTexts:linkTfcControl.setStatus(_G)
class _LinkTfcWatchWindow_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_LinkTfcWatchWindow_Type.__name__=_C
_LinkTfcWatchWindow_Object=MibTableColumn
linkTfcWatchWindow=_LinkTfcWatchWindow_Object((1,3,6,1,4,1,3373,1103,80,18,1,3),_LinkTfcWatchWindow_Type())
linkTfcWatchWindow.setMaxAccess(_F)
if mibBuilder.loadTexts:linkTfcWatchWindow.setStatus(_G)
class _LinkTfcAlarmThreshold_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_LinkTfcAlarmThreshold_Type.__name__=_C
_LinkTfcAlarmThreshold_Object=MibTableColumn
linkTfcAlarmThreshold=_LinkTfcAlarmThreshold_Object((1,3,6,1,4,1,3373,1103,80,18,1,4),_LinkTfcAlarmThreshold_Type())
linkTfcAlarmThreshold.setMaxAccess(_F)
if mibBuilder.loadTexts:linkTfcAlarmThreshold.setStatus(_G)
_LinkTfcAlarm_Type=AlarmStatus
_LinkTfcAlarm_Object=MibTableColumn
linkTfcAlarm=_LinkTfcAlarm_Object((1,3,6,1,4,1,3373,1103,80,18,1,5),_LinkTfcAlarm_Type())
linkTfcAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:linkTfcAlarm.setStatus(_G)
_LinkTfcRowStatus_Type=RowStatus
_LinkTfcRowStatus_Object=MibTableColumn
linkTfcRowStatus=_LinkTfcRowStatus_Object((1,3,6,1,4,1,3373,1103,80,18,1,6),_LinkTfcRowStatus_Type())
linkTfcRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:linkTfcRowStatus.setStatus(_G)
_LinkMaintTable_Object=MibTable
linkMaintTable=_LinkMaintTable_Object((1,3,6,1,4,1,3373,1103,80,19))
if mibBuilder.loadTexts:linkMaintTable.setStatus(_A)
_LinkMaintEntry_Object=MibTableRow
linkMaintEntry=_LinkMaintEntry_Object((1,3,6,1,4,1,3373,1103,80,19,1))
linkMaintEntry.setIndexNames((0,_E,_K),(0,_E,_M))
if mibBuilder.loadTexts:linkMaintEntry.setStatus(_A)
class _LinkBerStart_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('restart',1),('stop',2)))
_LinkBerStart_Type.__name__=_C
_LinkBerStart_Object=MibTableColumn
linkBerStart=_LinkBerStart_Object((1,3,6,1,4,1,3373,1103,80,19,1,1),_LinkBerStart_Type())
linkBerStart.setMaxAccess(_D)
if mibBuilder.loadTexts:linkBerStart.setStatus(_A)
class _LinkBaseBandLom_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_LinkBaseBandLom_Type.__name__=_C
_LinkBaseBandLom_Object=MibTableColumn
linkBaseBandLom=_LinkBaseBandLom_Object((1,3,6,1,4,1,3373,1103,80,19,1,2),_LinkBaseBandLom_Type())
linkBaseBandLom.setMaxAccess(_D)
if mibBuilder.loadTexts:linkBaseBandLom.setStatus(_A)
class _LinkFadeMarginMeasure_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_LinkFadeMarginMeasure_Type.__name__=_C
_LinkFadeMarginMeasure_Object=MibTableColumn
linkFadeMarginMeasure=_LinkFadeMarginMeasure_Object((1,3,6,1,4,1,3373,1103,80,19,1,3),_LinkFadeMarginMeasure_Type())
linkFadeMarginMeasure.setMaxAccess(_D)
if mibBuilder.loadTexts:linkFadeMarginMeasure.setStatus(_G)
class _LinkXpicControlProcedureReset_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_O,0),(_b,1)))
_LinkXpicControlProcedureReset_Type.__name__=_C
_LinkXpicControlProcedureReset_Object=MibTableColumn
linkXpicControlProcedureReset=_LinkXpicControlProcedureReset_Object((1,3,6,1,4,1,3373,1103,80,19,1,4),_LinkXpicControlProcedureReset_Type())
linkXpicControlProcedureReset.setMaxAccess(_D)
if mibBuilder.loadTexts:linkXpicControlProcedureReset.setStatus(_A)
_LinkBerTable_Object=MibTable
linkBerTable=_LinkBerTable_Object((1,3,6,1,4,1,3373,1103,80,20))
if mibBuilder.loadTexts:linkBerTable.setStatus(_A)
_LinkBerEntry_Object=MibTableRow
linkBerEntry=_LinkBerEntry_Object((1,3,6,1,4,1,3373,1103,80,20,1))
linkBerEntry.setIndexNames((0,_E,_K),(0,_E,_M))
if mibBuilder.loadTexts:linkBerEntry.setStatus(_A)
_LinkBerErrorCounterH_Type=Counter32
_LinkBerErrorCounterH_Object=MibTableColumn
linkBerErrorCounterH=_LinkBerErrorCounterH_Object((1,3,6,1,4,1,3373,1103,80,20,1,1),_LinkBerErrorCounterH_Type())
linkBerErrorCounterH.setMaxAccess(_B)
if mibBuilder.loadTexts:linkBerErrorCounterH.setStatus(_A)
_LinkBerErrorCounterL_Type=Counter32
_LinkBerErrorCounterL_Object=MibTableColumn
linkBerErrorCounterL=_LinkBerErrorCounterL_Object((1,3,6,1,4,1,3373,1103,80,20,1,2),_LinkBerErrorCounterL_Type())
linkBerErrorCounterL.setMaxAccess(_B)
if mibBuilder.loadTexts:linkBerErrorCounterL.setStatus(_A)
_LinkBerDataCounterH_Type=Counter32
_LinkBerDataCounterH_Object=MibTableColumn
linkBerDataCounterH=_LinkBerDataCounterH_Object((1,3,6,1,4,1,3373,1103,80,20,1,3),_LinkBerDataCounterH_Type())
linkBerDataCounterH.setMaxAccess(_B)
if mibBuilder.loadTexts:linkBerDataCounterH.setStatus(_A)
_LinkBerDataCounterL_Type=Counter32
_LinkBerDataCounterL_Object=MibTableColumn
linkBerDataCounterL=_LinkBerDataCounterL_Object((1,3,6,1,4,1,3373,1103,80,20,1,4),_LinkBerDataCounterL_Type())
linkBerDataCounterL.setMaxAccess(_B)
if mibBuilder.loadTexts:linkBerDataCounterL.setStatus(_A)
_LinkBerSyncLossAlarm_Type=AlarmStatus
_LinkBerSyncLossAlarm_Object=MibTableColumn
linkBerSyncLossAlarm=_LinkBerSyncLossAlarm_Object((1,3,6,1,4,1,3373,1103,80,20,1,5),_LinkBerSyncLossAlarm_Type())
linkBerSyncLossAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:linkBerSyncLossAlarm.setStatus(_A)
_LinkBerSyncLossAlarmCounter_Type=Integer32
_LinkBerSyncLossAlarmCounter_Object=MibTableColumn
linkBerSyncLossAlarmCounter=_LinkBerSyncLossAlarmCounter_Object((1,3,6,1,4,1,3373,1103,80,20,1,6),_LinkBerSyncLossAlarmCounter_Type())
linkBerSyncLossAlarmCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:linkBerSyncLossAlarmCounter.setStatus(_A)
_LinkBerElapsedTime_Type=Integer32
_LinkBerElapsedTime_Object=MibTableColumn
linkBerElapsedTime=_LinkBerElapsedTime_Object((1,3,6,1,4,1,3373,1103,80,20,1,7),_LinkBerElapsedTime_Type())
linkBerElapsedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:linkBerElapsedTime.setStatus(_A)
_LinkAcmTable_Object=MibTable
linkAcmTable=_LinkAcmTable_Object((1,3,6,1,4,1,3373,1103,80,21))
if mibBuilder.loadTexts:linkAcmTable.setStatus(_A)
_LinkAcmEntry_Object=MibTableRow
linkAcmEntry=_LinkAcmEntry_Object((1,3,6,1,4,1,3373,1103,80,21,1))
linkAcmEntry.setIndexNames((0,_E,_K),(0,_E,_M),(0,_E,_T))
if mibBuilder.loadTexts:linkAcmEntry.setStatus(_A)
_LinkAcmProfileId_Type=Integer32
_LinkAcmProfileId_Object=MibTableColumn
linkAcmProfileId=_LinkAcmProfileId_Object((1,3,6,1,4,1,3373,1103,80,21,1,1),_LinkAcmProfileId_Type())
linkAcmProfileId.setMaxAccess(_B)
if mibBuilder.loadTexts:linkAcmProfileId.setStatus(_A)
_LinkAcmProfileModulation_Type=BitsPerSymbol
_LinkAcmProfileModulation_Object=MibTableColumn
linkAcmProfileModulation=_LinkAcmProfileModulation_Object((1,3,6,1,4,1,3373,1103,80,21,1,2),_LinkAcmProfileModulation_Type())
linkAcmProfileModulation.setMaxAccess(_B)
if mibBuilder.loadTexts:linkAcmProfileModulation.setStatus(_A)
class _LinkAcmProfileCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Z,1),(_a,2)))
_LinkAcmProfileCode_Type.__name__=_C
_LinkAcmProfileCode_Object=MibTableColumn
linkAcmProfileCode=_LinkAcmProfileCode_Object((1,3,6,1,4,1,3373,1103,80,21,1,3),_LinkAcmProfileCode_Type())
linkAcmProfileCode.setMaxAccess(_B)
if mibBuilder.loadTexts:linkAcmProfileCode.setStatus(_A)
_LinkAcmProfileCapacity_Type=Integer32
_LinkAcmProfileCapacity_Object=MibTableColumn
linkAcmProfileCapacity=_LinkAcmProfileCapacity_Object((1,3,6,1,4,1,3373,1103,80,21,1,4),_LinkAcmProfileCapacity_Type())
linkAcmProfileCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:linkAcmProfileCapacity.setStatus(_A)
class _LinkAcmProfileLabel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_LinkAcmProfileLabel_Type.__name__=_N
_LinkAcmProfileLabel_Object=MibTableColumn
linkAcmProfileLabel=_LinkAcmProfileLabel_Object((1,3,6,1,4,1,3373,1103,80,21,1,5),_LinkAcmProfileLabel_Type())
linkAcmProfileLabel.setMaxAccess(_D)
if mibBuilder.loadTexts:linkAcmProfileLabel.setStatus(_A)
class _LinkAcmProfileEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_LinkAcmProfileEnable_Type.__name__=_C
_LinkAcmProfileEnable_Object=MibTableColumn
linkAcmProfileEnable=_LinkAcmProfileEnable_Object((1,3,6,1,4,1,3373,1103,80,21,1,6),_LinkAcmProfileEnable_Type())
linkAcmProfileEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:linkAcmProfileEnable.setStatus(_A)
class _LinkAcmMaxTDMCapacity_Type(Integer32):defaultValue=0
_LinkAcmMaxTDMCapacity_Type.__name__=_C
_LinkAcmMaxTDMCapacity_Object=MibTableColumn
linkAcmMaxTDMCapacity=_LinkAcmMaxTDMCapacity_Object((1,3,6,1,4,1,3373,1103,80,21,1,7),_LinkAcmMaxTDMCapacity_Type())
linkAcmMaxTDMCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:linkAcmMaxTDMCapacity.setStatus(_G)
_LinkAcmPowerScaling_Type=Integer32
_LinkAcmPowerScaling_Object=MibTableColumn
linkAcmPowerScaling=_LinkAcmPowerScaling_Object((1,3,6,1,4,1,3373,1103,80,21,1,8),_LinkAcmPowerScaling_Type())
linkAcmPowerScaling.setMaxAccess(_B)
if mibBuilder.loadTexts:linkAcmPowerScaling.setStatus(_G)
_LinkAcmDownshiftThreshold_Type=Integer32
_LinkAcmDownshiftThreshold_Object=MibTableColumn
linkAcmDownshiftThreshold=_LinkAcmDownshiftThreshold_Object((1,3,6,1,4,1,3373,1103,80,21,1,9),_LinkAcmDownshiftThreshold_Type())
linkAcmDownshiftThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:linkAcmDownshiftThreshold.setStatus(_A)
_LinkAcmUpshiftThreshold_Type=Integer32
_LinkAcmUpshiftThreshold_Object=MibTableColumn
linkAcmUpshiftThreshold=_LinkAcmUpshiftThreshold_Object((1,3,6,1,4,1,3373,1103,80,21,1,10),_LinkAcmUpshiftThreshold_Type())
linkAcmUpshiftThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:linkAcmUpshiftThreshold.setStatus(_A)
class _LinkAcmActiveProfile_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_S,1),('activeRx',2),('activeTx',3),('activeBoth',4)))
_LinkAcmActiveProfile_Type.__name__=_C
_LinkAcmActiveProfile_Object=MibTableColumn
linkAcmActiveProfile=_LinkAcmActiveProfile_Object((1,3,6,1,4,1,3373,1103,80,21,1,11),_LinkAcmActiveProfile_Type())
linkAcmActiveProfile.setMaxAccess(_B)
if mibBuilder.loadTexts:linkAcmActiveProfile.setStatus(_A)
_LinkAcmTDMCapacity_Type=Integer32
_LinkAcmTDMCapacity_Object=MibTableColumn
linkAcmTDMCapacity=_LinkAcmTDMCapacity_Object((1,3,6,1,4,1,3373,1103,80,21,1,12),_LinkAcmTDMCapacity_Type())
linkAcmTDMCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:linkAcmTDMCapacity.setStatus(_A)
_LinkAcmETHCapacity_Type=Integer32
_LinkAcmETHCapacity_Object=MibTableColumn
linkAcmETHCapacity=_LinkAcmETHCapacity_Object((1,3,6,1,4,1,3373,1103,80,21,1,13),_LinkAcmETHCapacity_Type())
linkAcmETHCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:linkAcmETHCapacity.setStatus(_A)
_LinkAcmAtpcRxPowerScaling_Type=Integer32
_LinkAcmAtpcRxPowerScaling_Object=MibTableColumn
linkAcmAtpcRxPowerScaling=_LinkAcmAtpcRxPowerScaling_Object((1,3,6,1,4,1,3373,1103,80,21,1,14),_LinkAcmAtpcRxPowerScaling_Type())
linkAcmAtpcRxPowerScaling.setMaxAccess(_B)
if mibBuilder.loadTexts:linkAcmAtpcRxPowerScaling.setStatus(_G)
_LinkAcmPowerRange_Type=Integer32
_LinkAcmPowerRange_Object=MibTableColumn
linkAcmPowerRange=_LinkAcmPowerRange_Object((1,3,6,1,4,1,3373,1103,80,21,1,15),_LinkAcmPowerRange_Type())
linkAcmPowerRange.setMaxAccess(_B)
if mibBuilder.loadTexts:linkAcmPowerRange.setStatus(_G)
_LinkProTable_Object=MibTable
linkProTable=_LinkProTable_Object((1,3,6,1,4,1,3373,1103,80,22))
if mibBuilder.loadTexts:linkProTable.setStatus(_G)
_LinkProEntry_Object=MibTableRow
linkProEntry=_LinkProEntry_Object((1,3,6,1,4,1,3373,1103,80,22,1))
linkProEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:linkProEntry.setStatus(_G)
class _LinkProProtectionTxChIdx_Type(Integer32):defaultValue=0
_LinkProProtectionTxChIdx_Type.__name__=_C
_LinkProProtectionTxChIdx_Object=MibTableColumn
linkProProtectionTxChIdx=_LinkProProtectionTxChIdx_Object((1,3,6,1,4,1,3373,1103,80,22,1,1),_LinkProProtectionTxChIdx_Type())
linkProProtectionTxChIdx.setMaxAccess(_F)
if mibBuilder.loadTexts:linkProProtectionTxChIdx.setStatus(_G)
class _LinkProProtectionRxChIdx_Type(Integer32):defaultValue=0
_LinkProProtectionRxChIdx_Type.__name__=_C
_LinkProProtectionRxChIdx_Object=MibTableColumn
linkProProtectionRxChIdx=_LinkProProtectionRxChIdx_Object((1,3,6,1,4,1,3373,1103,80,22,1,2),_LinkProProtectionRxChIdx_Type())
linkProProtectionRxChIdx.setMaxAccess(_F)
if mibBuilder.loadTexts:linkProProtectionRxChIdx.setStatus(_G)
class _LinkProTxWtrTime_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,12))
_LinkProTxWtrTime_Type.__name__=_C
_LinkProTxWtrTime_Object=MibTableColumn
linkProTxWtrTime=_LinkProTxWtrTime_Object((1,3,6,1,4,1,3373,1103,80,22,1,3),_LinkProTxWtrTime_Type())
linkProTxWtrTime.setMaxAccess(_F)
if mibBuilder.loadTexts:linkProTxWtrTime.setStatus(_G)
class _LinkProRxWtrTime_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,12))
_LinkProRxWtrTime_Type.__name__=_C
_LinkProRxWtrTime_Object=MibTableColumn
linkProRxWtrTime=_LinkProRxWtrTime_Object((1,3,6,1,4,1,3373,1103,80,22,1,4),_LinkProRxWtrTime_Type())
linkProRxWtrTime.setMaxAccess(_F)
if mibBuilder.loadTexts:linkProRxWtrTime.setStatus(_G)
class _LinkProTxSwitchedChIdx_Type(Integer32):defaultValue=0
_LinkProTxSwitchedChIdx_Type.__name__=_C
_LinkProTxSwitchedChIdx_Object=MibTableColumn
linkProTxSwitchedChIdx=_LinkProTxSwitchedChIdx_Object((1,3,6,1,4,1,3373,1103,80,22,1,5),_LinkProTxSwitchedChIdx_Type())
linkProTxSwitchedChIdx.setMaxAccess(_B)
if mibBuilder.loadTexts:linkProTxSwitchedChIdx.setStatus(_G)
class _LinkProRxSwitchedChIdx_Type(Integer32):defaultValue=0
_LinkProRxSwitchedChIdx_Type.__name__=_C
_LinkProRxSwitchedChIdx_Object=MibTableColumn
linkProRxSwitchedChIdx=_LinkProRxSwitchedChIdx_Object((1,3,6,1,4,1,3373,1103,80,22,1,6),_LinkProRxSwitchedChIdx_Type())
linkProRxSwitchedChIdx.setMaxAccess(_B)
if mibBuilder.loadTexts:linkProRxSwitchedChIdx.setStatus(_G)
class _LinkProTxRevertive_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_LinkProTxRevertive_Type.__name__=_C
_LinkProTxRevertive_Object=MibTableColumn
linkProTxRevertive=_LinkProTxRevertive_Object((1,3,6,1,4,1,3373,1103,80,22,1,7),_LinkProTxRevertive_Type())
linkProTxRevertive.setMaxAccess(_F)
if mibBuilder.loadTexts:linkProTxRevertive.setStatus(_G)
class _LinkProRxRevertive_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_LinkProRxRevertive_Type.__name__=_C
_LinkProRxRevertive_Object=MibTableColumn
linkProRxRevertive=_LinkProRxRevertive_Object((1,3,6,1,4,1,3373,1103,80,22,1,8),_LinkProRxRevertive_Type())
linkProRxRevertive.setMaxAccess(_F)
if mibBuilder.loadTexts:linkProRxRevertive.setStatus(_G)
class _LinkProExtraTraffic_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_LinkProExtraTraffic_Type.__name__=_C
_LinkProExtraTraffic_Object=MibTableColumn
linkProExtraTraffic=_LinkProExtraTraffic_Object((1,3,6,1,4,1,3373,1103,80,22,1,9),_LinkProExtraTraffic_Type())
linkProExtraTraffic.setMaxAccess(_F)
if mibBuilder.loadTexts:linkProExtraTraffic.setStatus(_G)
_LinkProRowStatus_Type=RowStatus
_LinkProRowStatus_Object=MibTableColumn
linkProRowStatus=_LinkProRowStatus_Object((1,3,6,1,4,1,3373,1103,80,22,1,10),_LinkProRowStatus_Type())
linkProRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:linkProRowStatus.setStatus(_G)
_LinkProMaintTable_Object=MibTable
linkProMaintTable=_LinkProMaintTable_Object((1,3,6,1,4,1,3373,1103,80,23))
if mibBuilder.loadTexts:linkProMaintTable.setStatus(_G)
_LinkProMaintEntry_Object=MibTableRow
linkProMaintEntry=_LinkProMaintEntry_Object((1,3,6,1,4,1,3373,1103,80,23,1))
linkProMaintEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:linkProMaintEntry.setStatus(_G)
class _LinkProMaintTxLockout_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_LinkProMaintTxLockout_Type.__name__=_C
_LinkProMaintTxLockout_Object=MibTableColumn
linkProMaintTxLockout=_LinkProMaintTxLockout_Object((1,3,6,1,4,1,3373,1103,80,23,1,1),_LinkProMaintTxLockout_Type())
linkProMaintTxLockout.setMaxAccess(_D)
if mibBuilder.loadTexts:linkProMaintTxLockout.setStatus(_G)
class _LinkProMaintRxLockout_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_LinkProMaintRxLockout_Type.__name__=_C
_LinkProMaintRxLockout_Object=MibTableColumn
linkProMaintRxLockout=_LinkProMaintRxLockout_Object((1,3,6,1,4,1,3373,1103,80,23,1,2),_LinkProMaintRxLockout_Type())
linkProMaintRxLockout.setMaxAccess(_D)
if mibBuilder.loadTexts:linkProMaintRxLockout.setStatus(_G)
class _LinkProMaintTxForced_Type(Integer32):defaultValue=0
_LinkProMaintTxForced_Type.__name__=_C
_LinkProMaintTxForced_Object=MibTableColumn
linkProMaintTxForced=_LinkProMaintTxForced_Object((1,3,6,1,4,1,3373,1103,80,23,1,3),_LinkProMaintTxForced_Type())
linkProMaintTxForced.setMaxAccess(_D)
if mibBuilder.loadTexts:linkProMaintTxForced.setStatus(_G)
class _LinkProMaintRxForced_Type(Integer32):defaultValue=0
_LinkProMaintRxForced_Type.__name__=_C
_LinkProMaintRxForced_Object=MibTableColumn
linkProMaintRxForced=_LinkProMaintRxForced_Object((1,3,6,1,4,1,3373,1103,80,23,1,4),_LinkProMaintRxForced_Type())
linkProMaintRxForced.setMaxAccess(_D)
if mibBuilder.loadTexts:linkProMaintRxForced.setStatus(_G)
class _LinkProMaintTxWtrReset_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_U,2)))
_LinkProMaintTxWtrReset_Type.__name__=_C
_LinkProMaintTxWtrReset_Object=MibTableColumn
linkProMaintTxWtrReset=_LinkProMaintTxWtrReset_Object((1,3,6,1,4,1,3373,1103,80,23,1,5),_LinkProMaintTxWtrReset_Type())
linkProMaintTxWtrReset.setMaxAccess(_D)
if mibBuilder.loadTexts:linkProMaintTxWtrReset.setStatus(_G)
class _LinkProMaintRxWtrReset_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_U,2)))
_LinkProMaintRxWtrReset_Type.__name__=_C
_LinkProMaintRxWtrReset_Object=MibTableColumn
linkProMaintRxWtrReset=_LinkProMaintRxWtrReset_Object((1,3,6,1,4,1,3373,1103,80,23,1,6),_LinkProMaintRxWtrReset_Type())
linkProMaintRxWtrReset.setMaxAccess(_D)
if mibBuilder.loadTexts:linkProMaintRxWtrReset.setStatus(_G)
_LinkCapabilitiesTable_Object=MibTable
linkCapabilitiesTable=_LinkCapabilitiesTable_Object((1,3,6,1,4,1,3373,1103,80,24))
if mibBuilder.loadTexts:linkCapabilitiesTable.setStatus(_G)
_LinkCapabilitiesEntry_Object=MibTableRow
linkCapabilitiesEntry=_LinkCapabilitiesEntry_Object((1,3,6,1,4,1,3373,1103,80,24,1))
linkCapabilitiesEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:linkCapabilitiesEntry.setStatus(_G)
_LinkCapabilitiesCapability_Type=RadioCapability
_LinkCapabilitiesCapability_Object=MibTableColumn
linkCapabilitiesCapability=_LinkCapabilitiesCapability_Object((1,3,6,1,4,1,3373,1103,80,24,1,1),_LinkCapabilitiesCapability_Type())
linkCapabilitiesCapability.setMaxAccess(_B)
if mibBuilder.loadTexts:linkCapabilitiesCapability.setStatus(_G)
_LinkCapabilitiesTxMinFrequency_Type=Integer32
_LinkCapabilitiesTxMinFrequency_Object=MibTableColumn
linkCapabilitiesTxMinFrequency=_LinkCapabilitiesTxMinFrequency_Object((1,3,6,1,4,1,3373,1103,80,24,1,2),_LinkCapabilitiesTxMinFrequency_Type())
linkCapabilitiesTxMinFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:linkCapabilitiesTxMinFrequency.setStatus(_G)
_LinkCapabilitiesTxMaxFrequency_Type=Integer32
_LinkCapabilitiesTxMaxFrequency_Object=MibTableColumn
linkCapabilitiesTxMaxFrequency=_LinkCapabilitiesTxMaxFrequency_Object((1,3,6,1,4,1,3373,1103,80,24,1,3),_LinkCapabilitiesTxMaxFrequency_Type())
linkCapabilitiesTxMaxFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:linkCapabilitiesTxMaxFrequency.setStatus(_G)
_LinkCapabilitiesStepFrequency_Type=Integer32
_LinkCapabilitiesStepFrequency_Object=MibTableColumn
linkCapabilitiesStepFrequency=_LinkCapabilitiesStepFrequency_Object((1,3,6,1,4,1,3373,1103,80,24,1,4),_LinkCapabilitiesStepFrequency_Type())
linkCapabilitiesStepFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:linkCapabilitiesStepFrequency.setStatus(_G)
_LinkCapabilitiesMinPtxNominalValue_Type=Integer32
_LinkCapabilitiesMinPtxNominalValue_Object=MibTableColumn
linkCapabilitiesMinPtxNominalValue=_LinkCapabilitiesMinPtxNominalValue_Object((1,3,6,1,4,1,3373,1103,80,24,1,5),_LinkCapabilitiesMinPtxNominalValue_Type())
linkCapabilitiesMinPtxNominalValue.setMaxAccess(_B)
if mibBuilder.loadTexts:linkCapabilitiesMinPtxNominalValue.setStatus(_G)
_LinkCapabilitiesMaxPtxNominalValue_Type=Integer32
_LinkCapabilitiesMaxPtxNominalValue_Object=MibTableColumn
linkCapabilitiesMaxPtxNominalValue=_LinkCapabilitiesMaxPtxNominalValue_Object((1,3,6,1,4,1,3373,1103,80,24,1,6),_LinkCapabilitiesMaxPtxNominalValue_Type())
linkCapabilitiesMaxPtxNominalValue.setMaxAccess(_B)
if mibBuilder.loadTexts:linkCapabilitiesMaxPtxNominalValue.setStatus(_G)
_LinkCapabilitiesExtendedMinPwr_Type=Integer32
_LinkCapabilitiesExtendedMinPwr_Object=MibTableColumn
linkCapabilitiesExtendedMinPwr=_LinkCapabilitiesExtendedMinPwr_Object((1,3,6,1,4,1,3373,1103,80,24,1,7),_LinkCapabilitiesExtendedMinPwr_Type())
linkCapabilitiesExtendedMinPwr.setMaxAccess(_B)
if mibBuilder.loadTexts:linkCapabilitiesExtendedMinPwr.setStatus(_G)
_LinkFrequencyTable_Object=MibTable
linkFrequencyTable=_LinkFrequencyTable_Object((1,3,6,1,4,1,3373,1103,80,25))
if mibBuilder.loadTexts:linkFrequencyTable.setStatus(_G)
_LinkFreqTabEntry_Object=MibTableRow
linkFreqTabEntry=_LinkFreqTabEntry_Object((1,3,6,1,4,1,3373,1103,80,25,1))
linkFreqTabEntry.setIndexNames((0,_E,_K),(0,_E,_p))
if mibBuilder.loadTexts:linkFreqTabEntry.setStatus(_G)
_LinkFreqChannelId_Type=Integer32
_LinkFreqChannelId_Object=MibTableColumn
linkFreqChannelId=_LinkFreqChannelId_Object((1,3,6,1,4,1,3373,1103,80,25,1,1),_LinkFreqChannelId_Type())
linkFreqChannelId.setMaxAccess(_B)
if mibBuilder.loadTexts:linkFreqChannelId.setStatus(_G)
_LinkFreqChannelNum_Type=Integer32
_LinkFreqChannelNum_Object=MibTableColumn
linkFreqChannelNum=_LinkFreqChannelNum_Object((1,3,6,1,4,1,3373,1103,80,25,1,2),_LinkFreqChannelNum_Type())
linkFreqChannelNum.setMaxAccess(_B)
if mibBuilder.loadTexts:linkFreqChannelNum.setStatus(_G)
_LinkFreqValue_Type=Integer32
_LinkFreqValue_Object=MibTableColumn
linkFreqValue=_LinkFreqValue_Object((1,3,6,1,4,1,3373,1103,80,25,1,3),_LinkFreqValue_Type())
linkFreqValue.setMaxAccess(_B)
if mibBuilder.loadTexts:linkFreqValue.setStatus(_G)
_LinkDuplexFrequencyTable_Object=MibTable
linkDuplexFrequencyTable=_LinkDuplexFrequencyTable_Object((1,3,6,1,4,1,3373,1103,80,26))
if mibBuilder.loadTexts:linkDuplexFrequencyTable.setStatus(_G)
_LinkDuplexFreqEntry_Object=MibTableRow
linkDuplexFreqEntry=_LinkDuplexFreqEntry_Object((1,3,6,1,4,1,3373,1103,80,26,1))
linkDuplexFreqEntry.setIndexNames((0,_E,_K),(0,_E,_q))
if mibBuilder.loadTexts:linkDuplexFreqEntry.setStatus(_G)
_LinkDuplexFreqId_Type=Integer32
_LinkDuplexFreqId_Object=MibTableColumn
linkDuplexFreqId=_LinkDuplexFreqId_Object((1,3,6,1,4,1,3373,1103,80,26,1,1),_LinkDuplexFreqId_Type())
linkDuplexFreqId.setMaxAccess(_B)
if mibBuilder.loadTexts:linkDuplexFreqId.setStatus(_G)
_LinkDuplexFreqValue_Type=Integer32
_LinkDuplexFreqValue_Object=MibTableColumn
linkDuplexFreqValue=_LinkDuplexFreqValue_Object((1,3,6,1,4,1,3373,1103,80,26,1,2),_LinkDuplexFreqValue_Type())
linkDuplexFreqValue.setMaxAccess(_B)
if mibBuilder.loadTexts:linkDuplexFreqValue.setStatus(_G)
_LinkModulationTable_Object=MibTable
linkModulationTable=_LinkModulationTable_Object((1,3,6,1,4,1,3373,1103,80,27))
if mibBuilder.loadTexts:linkModulationTable.setStatus(_A)
_LinkModulationEntry_Object=MibTableRow
linkModulationEntry=_LinkModulationEntry_Object((1,3,6,1,4,1,3373,1103,80,27,1))
linkModulationEntry.setIndexNames((0,_E,_K),(0,_E,_r))
if mibBuilder.loadTexts:linkModulationEntry.setStatus(_A)
_LinkChannelSpacing_Type=ChannelSpacing
_LinkChannelSpacing_Object=MibTableColumn
linkChannelSpacing=_LinkChannelSpacing_Object((1,3,6,1,4,1,3373,1103,80,27,1,1),_LinkChannelSpacing_Type())
linkChannelSpacing.setMaxAccess(_B)
if mibBuilder.loadTexts:linkChannelSpacing.setStatus(_A)
_LinkModulationMap_Type=ModulationMap
_LinkModulationMap_Object=MibTableColumn
linkModulationMap=_LinkModulationMap_Object((1,3,6,1,4,1,3373,1103,80,27,1,2),_LinkModulationMap_Type())
linkModulationMap.setMaxAccess(_B)
if mibBuilder.loadTexts:linkModulationMap.setStatus(_A)
_LinkRefModulationMap_Type=ModulationMap
_LinkRefModulationMap_Object=MibTableColumn
linkRefModulationMap=_LinkRefModulationMap_Object((1,3,6,1,4,1,3373,1103,80,27,1,3),_LinkRefModulationMap_Type())
linkRefModulationMap.setMaxAccess(_B)
if mibBuilder.loadTexts:linkRefModulationMap.setStatus(_A)
_CombinedRadioCapabilitiesTable_Object=MibTable
combinedRadioCapabilitiesTable=_CombinedRadioCapabilitiesTable_Object((1,3,6,1,4,1,3373,1103,80,28))
if mibBuilder.loadTexts:combinedRadioCapabilitiesTable.setStatus(_A)
_CombinedRadioCapabilitiesEntry_Object=MibTableRow
combinedRadioCapabilitiesEntry=_CombinedRadioCapabilitiesEntry_Object((1,3,6,1,4,1,3373,1103,80,28,1))
combinedRadioCapabilitiesEntry.setIndexNames((0,_E,_P))
if mibBuilder.loadTexts:combinedRadioCapabilitiesEntry.setStatus(_A)
_CombinedRadioCapabilitiesCapability_Type=RadioCapability
_CombinedRadioCapabilitiesCapability_Object=MibTableColumn
combinedRadioCapabilitiesCapability=_CombinedRadioCapabilitiesCapability_Object((1,3,6,1,4,1,3373,1103,80,28,1,1),_CombinedRadioCapabilitiesCapability_Type())
combinedRadioCapabilitiesCapability.setMaxAccess(_B)
if mibBuilder.loadTexts:combinedRadioCapabilitiesCapability.setStatus(_A)
_CombinedRadioCapabilitiesTxMinFrequency_Type=Integer32
_CombinedRadioCapabilitiesTxMinFrequency_Object=MibTableColumn
combinedRadioCapabilitiesTxMinFrequency=_CombinedRadioCapabilitiesTxMinFrequency_Object((1,3,6,1,4,1,3373,1103,80,28,1,2),_CombinedRadioCapabilitiesTxMinFrequency_Type())
combinedRadioCapabilitiesTxMinFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:combinedRadioCapabilitiesTxMinFrequency.setStatus(_A)
_CombinedRadioCapabilitiesTxMaxFrequency_Type=Integer32
_CombinedRadioCapabilitiesTxMaxFrequency_Object=MibTableColumn
combinedRadioCapabilitiesTxMaxFrequency=_CombinedRadioCapabilitiesTxMaxFrequency_Object((1,3,6,1,4,1,3373,1103,80,28,1,3),_CombinedRadioCapabilitiesTxMaxFrequency_Type())
combinedRadioCapabilitiesTxMaxFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:combinedRadioCapabilitiesTxMaxFrequency.setStatus(_A)
_CombinedRadioCapabilitiesStepFrequency_Type=Integer32
_CombinedRadioCapabilitiesStepFrequency_Object=MibTableColumn
combinedRadioCapabilitiesStepFrequency=_CombinedRadioCapabilitiesStepFrequency_Object((1,3,6,1,4,1,3373,1103,80,28,1,4),_CombinedRadioCapabilitiesStepFrequency_Type())
combinedRadioCapabilitiesStepFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:combinedRadioCapabilitiesStepFrequency.setStatus(_A)
_CombinedRadioCapabilitiesMinPtxNominalValue_Type=Integer32
_CombinedRadioCapabilitiesMinPtxNominalValue_Object=MibTableColumn
combinedRadioCapabilitiesMinPtxNominalValue=_CombinedRadioCapabilitiesMinPtxNominalValue_Object((1,3,6,1,4,1,3373,1103,80,28,1,5),_CombinedRadioCapabilitiesMinPtxNominalValue_Type())
combinedRadioCapabilitiesMinPtxNominalValue.setMaxAccess(_B)
if mibBuilder.loadTexts:combinedRadioCapabilitiesMinPtxNominalValue.setStatus(_A)
_CombinedRadioCapabilitiesMaxPtxNominalValue_Type=Integer32
_CombinedRadioCapabilitiesMaxPtxNominalValue_Object=MibTableColumn
combinedRadioCapabilitiesMaxPtxNominalValue=_CombinedRadioCapabilitiesMaxPtxNominalValue_Object((1,3,6,1,4,1,3373,1103,80,28,1,6),_CombinedRadioCapabilitiesMaxPtxNominalValue_Type())
combinedRadioCapabilitiesMaxPtxNominalValue.setMaxAccess(_B)
if mibBuilder.loadTexts:combinedRadioCapabilitiesMaxPtxNominalValue.setStatus(_A)
_CombinedRadioCapabilitiesExtendedMinPwr_Type=Integer32
_CombinedRadioCapabilitiesExtendedMinPwr_Object=MibTableColumn
combinedRadioCapabilitiesExtendedMinPwr=_CombinedRadioCapabilitiesExtendedMinPwr_Object((1,3,6,1,4,1,3373,1103,80,28,1,7),_CombinedRadioCapabilitiesExtendedMinPwr_Type())
combinedRadioCapabilitiesExtendedMinPwr.setMaxAccess(_B)
if mibBuilder.loadTexts:combinedRadioCapabilitiesExtendedMinPwr.setStatus(_A)
_CombinedRadioFrequencyTable_Object=MibTable
combinedRadioFrequencyTable=_CombinedRadioFrequencyTable_Object((1,3,6,1,4,1,3373,1103,80,29))
if mibBuilder.loadTexts:combinedRadioFrequencyTable.setStatus(_A)
_CombinedRadioFreqTabEntry_Object=MibTableRow
combinedRadioFreqTabEntry=_CombinedRadioFreqTabEntry_Object((1,3,6,1,4,1,3373,1103,80,29,1))
combinedRadioFreqTabEntry.setIndexNames((0,_E,_P),(0,_E,_s))
if mibBuilder.loadTexts:combinedRadioFreqTabEntry.setStatus(_A)
_CombinedRadioFreqChannelId_Type=Integer32
_CombinedRadioFreqChannelId_Object=MibTableColumn
combinedRadioFreqChannelId=_CombinedRadioFreqChannelId_Object((1,3,6,1,4,1,3373,1103,80,29,1,1),_CombinedRadioFreqChannelId_Type())
combinedRadioFreqChannelId.setMaxAccess(_B)
if mibBuilder.loadTexts:combinedRadioFreqChannelId.setStatus(_A)
_CombinedRadioFreqChannelNum_Type=Integer32
_CombinedRadioFreqChannelNum_Object=MibTableColumn
combinedRadioFreqChannelNum=_CombinedRadioFreqChannelNum_Object((1,3,6,1,4,1,3373,1103,80,29,1,2),_CombinedRadioFreqChannelNum_Type())
combinedRadioFreqChannelNum.setMaxAccess(_B)
if mibBuilder.loadTexts:combinedRadioFreqChannelNum.setStatus(_A)
_CombinedRadioFreqValue_Type=Integer32
_CombinedRadioFreqValue_Object=MibTableColumn
combinedRadioFreqValue=_CombinedRadioFreqValue_Object((1,3,6,1,4,1,3373,1103,80,29,1,3),_CombinedRadioFreqValue_Type())
combinedRadioFreqValue.setMaxAccess(_B)
if mibBuilder.loadTexts:combinedRadioFreqValue.setStatus(_A)
_CombinedRadioDuplexFrequencyTable_Object=MibTable
combinedRadioDuplexFrequencyTable=_CombinedRadioDuplexFrequencyTable_Object((1,3,6,1,4,1,3373,1103,80,30))
if mibBuilder.loadTexts:combinedRadioDuplexFrequencyTable.setStatus(_A)
_CombinedRadioDuplexFreqEntry_Object=MibTableRow
combinedRadioDuplexFreqEntry=_CombinedRadioDuplexFreqEntry_Object((1,3,6,1,4,1,3373,1103,80,30,1))
combinedRadioDuplexFreqEntry.setIndexNames((0,_E,_P),(0,_E,_t))
if mibBuilder.loadTexts:combinedRadioDuplexFreqEntry.setStatus(_A)
_CombinedRadioDuplexFreqId_Type=Integer32
_CombinedRadioDuplexFreqId_Object=MibTableColumn
combinedRadioDuplexFreqId=_CombinedRadioDuplexFreqId_Object((1,3,6,1,4,1,3373,1103,80,30,1,1),_CombinedRadioDuplexFreqId_Type())
combinedRadioDuplexFreqId.setMaxAccess(_B)
if mibBuilder.loadTexts:combinedRadioDuplexFreqId.setStatus(_A)
_CombinedRadioDuplexFreqValue_Type=Integer32
_CombinedRadioDuplexFreqValue_Object=MibTableColumn
combinedRadioDuplexFreqValue=_CombinedRadioDuplexFreqValue_Object((1,3,6,1,4,1,3373,1103,80,30,1,2),_CombinedRadioDuplexFreqValue_Type())
combinedRadioDuplexFreqValue.setMaxAccess(_B)
if mibBuilder.loadTexts:combinedRadioDuplexFreqValue.setStatus(_A)
_CombinedRadioPowerScalingTable_Object=MibTable
combinedRadioPowerScalingTable=_CombinedRadioPowerScalingTable_Object((1,3,6,1,4,1,3373,1103,80,31))
if mibBuilder.loadTexts:combinedRadioPowerScalingTable.setStatus(_A)
_CombinedRadioPowerScalingEntry_Object=MibTableRow
combinedRadioPowerScalingEntry=_CombinedRadioPowerScalingEntry_Object((1,3,6,1,4,1,3373,1103,80,31,1))
combinedRadioPowerScalingEntry.setIndexNames((0,_E,_P),(0,_E,_T))
if mibBuilder.loadTexts:combinedRadioPowerScalingEntry.setStatus(_A)
_CombinedRadioPowerScaling_Type=Integer32
_CombinedRadioPowerScaling_Object=MibTableColumn
combinedRadioPowerScaling=_CombinedRadioPowerScaling_Object((1,3,6,1,4,1,3373,1103,80,31,1,1),_CombinedRadioPowerScaling_Type())
combinedRadioPowerScaling.setMaxAccess(_B)
if mibBuilder.loadTexts:combinedRadioPowerScaling.setStatus(_A)
_CombinedRadioAtpcRxPowerScaling_Type=Integer32
_CombinedRadioAtpcRxPowerScaling_Object=MibTableColumn
combinedRadioAtpcRxPowerScaling=_CombinedRadioAtpcRxPowerScaling_Object((1,3,6,1,4,1,3373,1103,80,31,1,2),_CombinedRadioAtpcRxPowerScaling_Type())
combinedRadioAtpcRxPowerScaling.setMaxAccess(_B)
if mibBuilder.loadTexts:combinedRadioAtpcRxPowerScaling.setStatus(_A)
_CombinedRadioPowerRange_Type=Integer32
_CombinedRadioPowerRange_Object=MibTableColumn
combinedRadioPowerRange=_CombinedRadioPowerRange_Object((1,3,6,1,4,1,3373,1103,80,31,1,3),_CombinedRadioPowerRange_Type())
combinedRadioPowerRange.setMaxAccess(_B)
if mibBuilder.loadTexts:combinedRadioPowerRange.setStatus(_A)
_Stm1BulkMappingTable_Object=MibTable
stm1BulkMappingTable=_Stm1BulkMappingTable_Object((1,3,6,1,4,1,3373,1103,80,32))
if mibBuilder.loadTexts:stm1BulkMappingTable.setStatus(_A)
_Stm1BulkMappingEntry_Object=MibTableRow
stm1BulkMappingEntry=_Stm1BulkMappingEntry_Object((1,3,6,1,4,1,3373,1103,80,32,1))
stm1BulkMappingEntry.setIndexNames((0,_E,_K),(0,_E,_u),(0,_E,_v))
if mibBuilder.loadTexts:stm1BulkMappingEntry.setStatus(_A)
_Stm1BulkPolIndex_Type=Integer32
_Stm1BulkPolIndex_Object=MibTableColumn
stm1BulkPolIndex=_Stm1BulkPolIndex_Object((1,3,6,1,4,1,3373,1103,80,32,1,1),_Stm1BulkPolIndex_Type())
stm1BulkPolIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:stm1BulkPolIndex.setStatus(_A)
_Stm1BulkChanIndex_Type=Integer32
_Stm1BulkChanIndex_Object=MibTableColumn
stm1BulkChanIndex=_Stm1BulkChanIndex_Object((1,3,6,1,4,1,3373,1103,80,32,1,2),_Stm1BulkChanIndex_Type())
stm1BulkChanIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:stm1BulkChanIndex.setStatus(_A)
class _Stm1BulkChannel_Type(Stm1IndexOrZero):defaultValue=0
_Stm1BulkChannel_Type.__name__=_w
_Stm1BulkChannel_Object=MibTableColumn
stm1BulkChannel=_Stm1BulkChannel_Object((1,3,6,1,4,1,3373,1103,80,32,1,3),_Stm1BulkChannel_Type())
stm1BulkChannel.setMaxAccess(_D)
if mibBuilder.loadTexts:stm1BulkChannel.setStatus(_A)
_LinkE1vsSTM1CapacityTable_Object=MibTable
linkE1vsSTM1CapacityTable=_LinkE1vsSTM1CapacityTable_Object((1,3,6,1,4,1,3373,1103,80,33))
if mibBuilder.loadTexts:linkE1vsSTM1CapacityTable.setStatus(_A)
_LinkE1vsSTM1CapacityEntry_Object=MibTableRow
linkE1vsSTM1CapacityEntry=_LinkE1vsSTM1CapacityEntry_Object((1,3,6,1,4,1,3373,1103,80,33,1))
linkE1vsSTM1CapacityEntry.setIndexNames((0,_E,_K),(0,_E,_T),(0,_E,_x))
if mibBuilder.loadTexts:linkE1vsSTM1CapacityEntry.setStatus(_A)
_LinkE1vsSTM1CapacityStm1_Type=Integer32
_LinkE1vsSTM1CapacityStm1_Object=MibTableColumn
linkE1vsSTM1CapacityStm1=_LinkE1vsSTM1CapacityStm1_Object((1,3,6,1,4,1,3373,1103,80,33,1,1),_LinkE1vsSTM1CapacityStm1_Type())
linkE1vsSTM1CapacityStm1.setMaxAccess(_y)
if mibBuilder.loadTexts:linkE1vsSTM1CapacityStm1.setStatus(_A)
_LinkE1vsSTM1CapacityE1_Type=Integer32
_LinkE1vsSTM1CapacityE1_Object=MibTableColumn
linkE1vsSTM1CapacityE1=_LinkE1vsSTM1CapacityE1_Object((1,3,6,1,4,1,3373,1103,80,33,1,2),_LinkE1vsSTM1CapacityE1_Type())
linkE1vsSTM1CapacityE1.setMaxAccess(_B)
if mibBuilder.loadTexts:linkE1vsSTM1CapacityE1.setStatus(_A)
_LinkTfcV2Table_Object=MibTable
linkTfcV2Table=_LinkTfcV2Table_Object((1,3,6,1,4,1,3373,1103,80,34))
if mibBuilder.loadTexts:linkTfcV2Table.setStatus(_A)
_LinkTfcV2Entry_Object=MibTableRow
linkTfcV2Entry=_LinkTfcV2Entry_Object((1,3,6,1,4,1,3373,1103,80,34,1))
linkTfcV2Entry.setIndexNames((0,_E,_K),(0,_E,_M))
if mibBuilder.loadTexts:linkTfcV2Entry.setStatus(_A)
class _LinkTfcV2Action_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_O,0),(_b,1)))
_LinkTfcV2Action_Type.__name__=_C
_LinkTfcV2Action_Object=MibTableColumn
linkTfcV2Action=_LinkTfcV2Action_Object((1,3,6,1,4,1,3373,1103,80,34,1,1),_LinkTfcV2Action_Type())
linkTfcV2Action.setMaxAccess(_F)
if mibBuilder.loadTexts:linkTfcV2Action.setStatus(_A)
class _LinkTfcV2Control_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_LinkTfcV2Control_Type.__name__=_C
_LinkTfcV2Control_Object=MibTableColumn
linkTfcV2Control=_LinkTfcV2Control_Object((1,3,6,1,4,1,3373,1103,80,34,1,2),_LinkTfcV2Control_Type())
linkTfcV2Control.setMaxAccess(_F)
if mibBuilder.loadTexts:linkTfcV2Control.setStatus(_A)
class _LinkTfcV2WatchWindow_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_LinkTfcV2WatchWindow_Type.__name__=_C
_LinkTfcV2WatchWindow_Object=MibTableColumn
linkTfcV2WatchWindow=_LinkTfcV2WatchWindow_Object((1,3,6,1,4,1,3373,1103,80,34,1,3),_LinkTfcV2WatchWindow_Type())
linkTfcV2WatchWindow.setMaxAccess(_F)
if mibBuilder.loadTexts:linkTfcV2WatchWindow.setStatus(_A)
class _LinkTfcV2AlarmThreshold_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_LinkTfcV2AlarmThreshold_Type.__name__=_C
_LinkTfcV2AlarmThreshold_Object=MibTableColumn
linkTfcV2AlarmThreshold=_LinkTfcV2AlarmThreshold_Object((1,3,6,1,4,1,3373,1103,80,34,1,4),_LinkTfcV2AlarmThreshold_Type())
linkTfcV2AlarmThreshold.setMaxAccess(_F)
if mibBuilder.loadTexts:linkTfcV2AlarmThreshold.setStatus(_A)
_LinkTfcV2Alarm_Type=AlarmStatus
_LinkTfcV2Alarm_Object=MibTableColumn
linkTfcV2Alarm=_LinkTfcV2Alarm_Object((1,3,6,1,4,1,3373,1103,80,34,1,5),_LinkTfcV2Alarm_Type())
linkTfcV2Alarm.setMaxAccess(_B)
if mibBuilder.loadTexts:linkTfcV2Alarm.setStatus(_A)
_LinkTfcV2RowStatus_Type=RowStatus
_LinkTfcV2RowStatus_Object=MibTableColumn
linkTfcV2RowStatus=_LinkTfcV2RowStatus_Object((1,3,6,1,4,1,3373,1103,80,34,1,6),_LinkTfcV2RowStatus_Type())
linkTfcV2RowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:linkTfcV2RowStatus.setStatus(_A)
_LinkProV2Table_Object=MibTable
linkProV2Table=_LinkProV2Table_Object((1,3,6,1,4,1,3373,1103,80,35))
if mibBuilder.loadTexts:linkProV2Table.setStatus(_A)
_LinkProV2Entry_Object=MibTableRow
linkProV2Entry=_LinkProV2Entry_Object((1,3,6,1,4,1,3373,1103,80,35,1))
linkProV2Entry.setIndexNames((0,_E,_K),(0,_E,_M))
if mibBuilder.loadTexts:linkProV2Entry.setStatus(_A)
class _LinkProV2ProtectionTxChIdx_Type(Integer32):defaultValue=0
_LinkProV2ProtectionTxChIdx_Type.__name__=_C
_LinkProV2ProtectionTxChIdx_Object=MibTableColumn
linkProV2ProtectionTxChIdx=_LinkProV2ProtectionTxChIdx_Object((1,3,6,1,4,1,3373,1103,80,35,1,1),_LinkProV2ProtectionTxChIdx_Type())
linkProV2ProtectionTxChIdx.setMaxAccess(_F)
if mibBuilder.loadTexts:linkProV2ProtectionTxChIdx.setStatus(_A)
class _LinkProV2ProtectionRxChIdx_Type(Integer32):defaultValue=0
_LinkProV2ProtectionRxChIdx_Type.__name__=_C
_LinkProV2ProtectionRxChIdx_Object=MibTableColumn
linkProV2ProtectionRxChIdx=_LinkProV2ProtectionRxChIdx_Object((1,3,6,1,4,1,3373,1103,80,35,1,2),_LinkProV2ProtectionRxChIdx_Type())
linkProV2ProtectionRxChIdx.setMaxAccess(_F)
if mibBuilder.loadTexts:linkProV2ProtectionRxChIdx.setStatus(_A)
class _LinkProV2TxWtrTime_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,12))
_LinkProV2TxWtrTime_Type.__name__=_C
_LinkProV2TxWtrTime_Object=MibTableColumn
linkProV2TxWtrTime=_LinkProV2TxWtrTime_Object((1,3,6,1,4,1,3373,1103,80,35,1,3),_LinkProV2TxWtrTime_Type())
linkProV2TxWtrTime.setMaxAccess(_F)
if mibBuilder.loadTexts:linkProV2TxWtrTime.setStatus(_A)
class _LinkProV2RxWtrTime_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,12))
_LinkProV2RxWtrTime_Type.__name__=_C
_LinkProV2RxWtrTime_Object=MibTableColumn
linkProV2RxWtrTime=_LinkProV2RxWtrTime_Object((1,3,6,1,4,1,3373,1103,80,35,1,4),_LinkProV2RxWtrTime_Type())
linkProV2RxWtrTime.setMaxAccess(_F)
if mibBuilder.loadTexts:linkProV2RxWtrTime.setStatus(_A)
class _LinkProV2TxSwitchedChIdx_Type(Integer32):defaultValue=0
_LinkProV2TxSwitchedChIdx_Type.__name__=_C
_LinkProV2TxSwitchedChIdx_Object=MibTableColumn
linkProV2TxSwitchedChIdx=_LinkProV2TxSwitchedChIdx_Object((1,3,6,1,4,1,3373,1103,80,35,1,5),_LinkProV2TxSwitchedChIdx_Type())
linkProV2TxSwitchedChIdx.setMaxAccess(_B)
if mibBuilder.loadTexts:linkProV2TxSwitchedChIdx.setStatus(_A)
class _LinkProV2RxSwitchedChIdx_Type(Integer32):defaultValue=0
_LinkProV2RxSwitchedChIdx_Type.__name__=_C
_LinkProV2RxSwitchedChIdx_Object=MibTableColumn
linkProV2RxSwitchedChIdx=_LinkProV2RxSwitchedChIdx_Object((1,3,6,1,4,1,3373,1103,80,35,1,6),_LinkProV2RxSwitchedChIdx_Type())
linkProV2RxSwitchedChIdx.setMaxAccess(_B)
if mibBuilder.loadTexts:linkProV2RxSwitchedChIdx.setStatus(_A)
class _LinkProV2TxRevertive_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_LinkProV2TxRevertive_Type.__name__=_C
_LinkProV2TxRevertive_Object=MibTableColumn
linkProV2TxRevertive=_LinkProV2TxRevertive_Object((1,3,6,1,4,1,3373,1103,80,35,1,7),_LinkProV2TxRevertive_Type())
linkProV2TxRevertive.setMaxAccess(_F)
if mibBuilder.loadTexts:linkProV2TxRevertive.setStatus(_A)
class _LinkProV2RxRevertive_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_LinkProV2RxRevertive_Type.__name__=_C
_LinkProV2RxRevertive_Object=MibTableColumn
linkProV2RxRevertive=_LinkProV2RxRevertive_Object((1,3,6,1,4,1,3373,1103,80,35,1,8),_LinkProV2RxRevertive_Type())
linkProV2RxRevertive.setMaxAccess(_F)
if mibBuilder.loadTexts:linkProV2RxRevertive.setStatus(_A)
class _LinkProV2ExtraTraffic_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_LinkProV2ExtraTraffic_Type.__name__=_C
_LinkProV2ExtraTraffic_Object=MibTableColumn
linkProV2ExtraTraffic=_LinkProV2ExtraTraffic_Object((1,3,6,1,4,1,3373,1103,80,35,1,9),_LinkProV2ExtraTraffic_Type())
linkProV2ExtraTraffic.setMaxAccess(_F)
if mibBuilder.loadTexts:linkProV2ExtraTraffic.setStatus(_A)
_LinkProV2RowStatus_Type=RowStatus
_LinkProV2RowStatus_Object=MibTableColumn
linkProV2RowStatus=_LinkProV2RowStatus_Object((1,3,6,1,4,1,3373,1103,80,35,1,10),_LinkProV2RowStatus_Type())
linkProV2RowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:linkProV2RowStatus.setStatus(_A)
_LinkProMaintV2Table_Object=MibTable
linkProMaintV2Table=_LinkProMaintV2Table_Object((1,3,6,1,4,1,3373,1103,80,36))
if mibBuilder.loadTexts:linkProMaintV2Table.setStatus(_A)
_LinkProMaintV2Entry_Object=MibTableRow
linkProMaintV2Entry=_LinkProMaintV2Entry_Object((1,3,6,1,4,1,3373,1103,80,36,1))
linkProMaintV2Entry.setIndexNames((0,_E,_K),(0,_E,_M))
if mibBuilder.loadTexts:linkProMaintV2Entry.setStatus(_A)
class _LinkProMaintV2TxLockout_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_LinkProMaintV2TxLockout_Type.__name__=_C
_LinkProMaintV2TxLockout_Object=MibTableColumn
linkProMaintV2TxLockout=_LinkProMaintV2TxLockout_Object((1,3,6,1,4,1,3373,1103,80,36,1,1),_LinkProMaintV2TxLockout_Type())
linkProMaintV2TxLockout.setMaxAccess(_D)
if mibBuilder.loadTexts:linkProMaintV2TxLockout.setStatus(_A)
class _LinkProMaintV2RxLockout_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_LinkProMaintV2RxLockout_Type.__name__=_C
_LinkProMaintV2RxLockout_Object=MibTableColumn
linkProMaintV2RxLockout=_LinkProMaintV2RxLockout_Object((1,3,6,1,4,1,3373,1103,80,36,1,2),_LinkProMaintV2RxLockout_Type())
linkProMaintV2RxLockout.setMaxAccess(_D)
if mibBuilder.loadTexts:linkProMaintV2RxLockout.setStatus(_A)
class _LinkProMaintV2TxForced_Type(Integer32):defaultValue=0
_LinkProMaintV2TxForced_Type.__name__=_C
_LinkProMaintV2TxForced_Object=MibTableColumn
linkProMaintV2TxForced=_LinkProMaintV2TxForced_Object((1,3,6,1,4,1,3373,1103,80,36,1,3),_LinkProMaintV2TxForced_Type())
linkProMaintV2TxForced.setMaxAccess(_D)
if mibBuilder.loadTexts:linkProMaintV2TxForced.setStatus(_A)
class _LinkProMaintV2RxForced_Type(Integer32):defaultValue=0
_LinkProMaintV2RxForced_Type.__name__=_C
_LinkProMaintV2RxForced_Object=MibTableColumn
linkProMaintV2RxForced=_LinkProMaintV2RxForced_Object((1,3,6,1,4,1,3373,1103,80,36,1,4),_LinkProMaintV2RxForced_Type())
linkProMaintV2RxForced.setMaxAccess(_D)
if mibBuilder.loadTexts:linkProMaintV2RxForced.setStatus(_A)
class _LinkProMaintV2TxWtrReset_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_U,2)))
_LinkProMaintV2TxWtrReset_Type.__name__=_C
_LinkProMaintV2TxWtrReset_Object=MibTableColumn
linkProMaintV2TxWtrReset=_LinkProMaintV2TxWtrReset_Object((1,3,6,1,4,1,3373,1103,80,36,1,5),_LinkProMaintV2TxWtrReset_Type())
linkProMaintV2TxWtrReset.setMaxAccess(_D)
if mibBuilder.loadTexts:linkProMaintV2TxWtrReset.setStatus(_A)
class _LinkProMaintV2RxWtrReset_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_U,2)))
_LinkProMaintV2RxWtrReset_Type.__name__=_C
_LinkProMaintV2RxWtrReset_Object=MibTableColumn
linkProMaintV2RxWtrReset=_LinkProMaintV2RxWtrReset_Object((1,3,6,1,4,1,3373,1103,80,36,1,6),_LinkProMaintV2RxWtrReset_Type())
linkProMaintV2RxWtrReset.setMaxAccess(_D)
if mibBuilder.loadTexts:linkProMaintV2RxWtrReset.setStatus(_A)
_SspTable_Object=MibTable
sspTable=_SspTable_Object((1,3,6,1,4,1,3373,1103,80,37))
if mibBuilder.loadTexts:sspTable.setStatus(_A)
_SspEntry_Object=MibTableRow
sspEntry=_SspEntry_Object((1,3,6,1,4,1,3373,1103,80,37,1))
sspEntry.setIndexNames((0,_E,_K),(0,_E,_M),(0,_E,_z))
if mibBuilder.loadTexts:sspEntry.setStatus(_A)
class _SspParameterType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('localAdminStatus',1),('localOperStatus',2),('remoteAdminStatus',3)))
_SspParameterType_Type.__name__=_C
_SspParameterType_Object=MibTableColumn
sspParameterType=_SspParameterType_Object((1,3,6,1,4,1,3373,1103,80,37,1,1),_SspParameterType_Type())
sspParameterType.setMaxAccess(_y)
if mibBuilder.loadTexts:sspParameterType.setStatus(_A)
class _SspLinkBandwidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*(('sspBw3p5Mhz',0),('sspBw7MHz',1),('sspBw14MHz',2),('sspBw28MHz',3),('sspBw56MHz',4),('sspBw10MHz',5),('sspBw20MHz',6),('sspBw30MHz',7),('sspBw40MHz',8),('sspBw50MHz',9),('sspBw112Mhz',10),('sspBw250Mhz',11),('sspBw500Mhz',12),('sspBw750Mhz',13),('sspBw1Ghz',14),('sspBw60MHz',15),('sspBw80MHz',16)))
_SspLinkBandwidth_Type.__name__=_C
_SspLinkBandwidth_Object=MibTableColumn
sspLinkBandwidth=_SspLinkBandwidth_Object((1,3,6,1,4,1,3373,1103,80,37,1,2),_SspLinkBandwidth_Type())
sspLinkBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:sspLinkBandwidth.setStatus(_A)
class _SspLinkModulation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('sspModBPSK',1),('sspMod4QAM',2),('sspMod8PSK',3),('sspMod16QAM',4),('sspMod32QAM',5),('sspMod64QAM',6),('sspMod128QAM',7),('sspMod256QAM',8),('sspMod512QAM',9),('sspMod1024QAM',10),('sspMod2048QAM',11),('sspMod4096QAM',12)))
_SspLinkModulation_Type.__name__=_C
_SspLinkModulation_Object=MibTableColumn
sspLinkModulation=_SspLinkModulation_Object((1,3,6,1,4,1,3373,1103,80,37,1,3),_SspLinkModulation_Type())
sspLinkModulation.setMaxAccess(_B)
if mibBuilder.loadTexts:sspLinkModulation.setStatus(_A)
class _SspLinkAcmEngineEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_SspLinkAcmEngineEnable_Type.__name__=_C
_SspLinkAcmEngineEnable_Object=MibTableColumn
sspLinkAcmEngineEnable=_SspLinkAcmEngineEnable_Object((1,3,6,1,4,1,3373,1103,80,37,1,4),_SspLinkAcmEngineEnable_Type())
sspLinkAcmEngineEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:sspLinkAcmEngineEnable.setStatus(_A)
_SspLinkTxUpperProfile_Type=Integer32
_SspLinkTxUpperProfile_Object=MibTableColumn
sspLinkTxUpperProfile=_SspLinkTxUpperProfile_Object((1,3,6,1,4,1,3373,1103,80,37,1,5),_SspLinkTxUpperProfile_Type())
sspLinkTxUpperProfile.setMaxAccess(_B)
if mibBuilder.loadTexts:sspLinkTxUpperProfile.setStatus(_A)
_SspLinkTxLowerProfile_Type=Integer32
_SspLinkTxLowerProfile_Object=MibTableColumn
sspLinkTxLowerProfile=_SspLinkTxLowerProfile_Object((1,3,6,1,4,1,3373,1103,80,37,1,6),_SspLinkTxLowerProfile_Type())
sspLinkTxLowerProfile.setMaxAccess(_B)
if mibBuilder.loadTexts:sspLinkTxLowerProfile.setStatus(_A)
class _SspLinkSynchSetupProtocolEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_SspLinkSynchSetupProtocolEnable_Type.__name__=_C
_SspLinkSynchSetupProtocolEnable_Object=MibTableColumn
sspLinkSynchSetupProtocolEnable=_SspLinkSynchSetupProtocolEnable_Object((1,3,6,1,4,1,3373,1103,80,37,1,7),_SspLinkSynchSetupProtocolEnable_Type())
sspLinkSynchSetupProtocolEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:sspLinkSynchSetupProtocolEnable.setStatus(_A)
class _SspLinkProfilesSetSelection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_h,1),(_i,2)))
_SspLinkProfilesSetSelection_Type.__name__=_C
_SspLinkProfilesSetSelection_Object=MibTableColumn
sspLinkProfilesSetSelection=_SspLinkProfilesSetSelection_Object((1,3,6,1,4,1,3373,1103,80,37,1,8),_SspLinkProfilesSetSelection_Type())
sspLinkProfilesSetSelection.setMaxAccess(_B)
if mibBuilder.loadTexts:sspLinkProfilesSetSelection.setStatus(_A)
_SspTdmE1Channel_Type=Integer32
_SspTdmE1Channel_Object=MibTableColumn
sspTdmE1Channel=_SspTdmE1Channel_Object((1,3,6,1,4,1,3373,1103,80,37,1,9),_SspTdmE1Channel_Type())
sspTdmE1Channel.setMaxAccess(_B)
if mibBuilder.loadTexts:sspTdmE1Channel.setStatus(_A)
_SspTdmStm1Channel_Type=Integer32
_SspTdmStm1Channel_Object=MibTableColumn
sspTdmStm1Channel=_SspTdmStm1Channel_Object((1,3,6,1,4,1,3373,1103,80,37,1,10),_SspTdmStm1Channel_Type())
sspTdmStm1Channel.setMaxAccess(_B)
if mibBuilder.loadTexts:sspTdmStm1Channel.setStatus(_A)
_RadioLoopCapabilityTable_Object=MibTable
radioLoopCapabilityTable=_RadioLoopCapabilityTable_Object((1,3,6,1,4,1,3373,1103,80,38))
if mibBuilder.loadTexts:radioLoopCapabilityTable.setStatus(_A)
_RadioLoopCapabilityEntry_Object=MibTableRow
radioLoopCapabilityEntry=_RadioLoopCapabilityEntry_Object((1,3,6,1,4,1,3373,1103,80,38,1))
radioLoopCapabilityEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:radioLoopCapabilityEntry.setStatus(_A)
_RadioLoopRfGroup_Type=Integer32
_RadioLoopRfGroup_Object=MibTableColumn
radioLoopRfGroup=_RadioLoopRfGroup_Object((1,3,6,1,4,1,3373,1103,80,38,1,1),_RadioLoopRfGroup_Type())
radioLoopRfGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:radioLoopRfGroup.setStatus(_A)
_RadioLoopIqGroup_Type=Integer32
_RadioLoopIqGroup_Object=MibTableColumn
radioLoopIqGroup=_RadioLoopIqGroup_Object((1,3,6,1,4,1,3373,1103,80,38,1,2),_RadioLoopIqGroup_Type())
radioLoopIqGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:radioLoopIqGroup.setStatus(_A)
_RadioLoopBaseBandGroup_Type=Integer32
_RadioLoopBaseBandGroup_Object=MibTableColumn
radioLoopBaseBandGroup=_RadioLoopBaseBandGroup_Object((1,3,6,1,4,1,3373,1103,80,38,1,3),_RadioLoopBaseBandGroup_Type())
radioLoopBaseBandGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:radioLoopBaseBandGroup.setStatus(_A)
_RadioRxBerThresholdTable_Object=MibTable
radioRxBerThresholdTable=_RadioRxBerThresholdTable_Object((1,3,6,1,4,1,3373,1103,80,39))
if mibBuilder.loadTexts:radioRxBerThresholdTable.setStatus(_A)
_RadioRxBerThresholdEntry_Object=MibTableRow
radioRxBerThresholdEntry=_RadioRxBerThresholdEntry_Object((1,3,6,1,4,1,3373,1103,80,39,1))
radioRxBerThresholdEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:radioRxBerThresholdEntry.setStatus(_A)
class _RadioRxBerThresholdStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('nonValid',1),('valid',2)))
_RadioRxBerThresholdStatus_Type.__name__=_C
_RadioRxBerThresholdStatus_Object=MibTableColumn
radioRxBerThresholdStatus=_RadioRxBerThresholdStatus_Object((1,3,6,1,4,1,3373,1103,80,39,1,1),_RadioRxBerThresholdStatus_Type())
radioRxBerThresholdStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:radioRxBerThresholdStatus.setStatus(_A)
_RadioNominalRxBerThreshold_Type=Integer32
_RadioNominalRxBerThreshold_Object=MibTableColumn
radioNominalRxBerThreshold=_RadioNominalRxBerThreshold_Object((1,3,6,1,4,1,3373,1103,80,39,1,2),_RadioNominalRxBerThreshold_Type())
radioNominalRxBerThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:radioNominalRxBerThreshold.setStatus(_A)
_RadioMeasuredRxBerThreshold_Type=Integer32
_RadioMeasuredRxBerThreshold_Object=MibTableColumn
radioMeasuredRxBerThreshold=_RadioMeasuredRxBerThreshold_Object((1,3,6,1,4,1,3373,1103,80,39,1,3),_RadioMeasuredRxBerThreshold_Type())
radioMeasuredRxBerThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:radioMeasuredRxBerThreshold.setStatus(_A)
_RadioEchoCancelerTable_Object=MibTable
radioEchoCancelerTable=_RadioEchoCancelerTable_Object((1,3,6,1,4,1,3373,1103,80,40))
if mibBuilder.loadTexts:radioEchoCancelerTable.setStatus(_A)
_RadioEchoCancelerEntry_Object=MibTableRow
radioEchoCancelerEntry=_RadioEchoCancelerEntry_Object((1,3,6,1,4,1,3373,1103,80,40,1))
radioEchoCancelerEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:radioEchoCancelerEntry.setStatus(_A)
class _RadioEchoCancelerFunctionEn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_RadioEchoCancelerFunctionEn_Type.__name__=_C
_RadioEchoCancelerFunctionEn_Object=MibTableColumn
radioEchoCancelerFunctionEn=_RadioEchoCancelerFunctionEn_Object((1,3,6,1,4,1,3373,1103,80,40,1,1),_RadioEchoCancelerFunctionEn_Type())
radioEchoCancelerFunctionEn.setMaxAccess(_D)
if mibBuilder.loadTexts:radioEchoCancelerFunctionEn.setStatus(_A)
class _RadioEchoCancelerCableLenMin_Type(Integer32):defaultValue=0
_RadioEchoCancelerCableLenMin_Type.__name__=_C
_RadioEchoCancelerCableLenMin_Object=MibTableColumn
radioEchoCancelerCableLenMin=_RadioEchoCancelerCableLenMin_Object((1,3,6,1,4,1,3373,1103,80,40,1,2),_RadioEchoCancelerCableLenMin_Type())
radioEchoCancelerCableLenMin.setMaxAccess(_D)
if mibBuilder.loadTexts:radioEchoCancelerCableLenMin.setStatus(_A)
class _RadioEchoCancelerCableLenMax_Type(Integer32):defaultValue=300
_RadioEchoCancelerCableLenMax_Type.__name__=_C
_RadioEchoCancelerCableLenMax_Object=MibTableColumn
radioEchoCancelerCableLenMax=_RadioEchoCancelerCableLenMax_Object((1,3,6,1,4,1,3373,1103,80,40,1,3),_RadioEchoCancelerCableLenMax_Type())
radioEchoCancelerCableLenMax.setMaxAccess(_D)
if mibBuilder.loadTexts:radioEchoCancelerCableLenMax.setStatus(_A)
class _RadioEchoCancelerDelayLine1_Type(Integer32):defaultValue=0
_RadioEchoCancelerDelayLine1_Type.__name__=_C
_RadioEchoCancelerDelayLine1_Object=MibTableColumn
radioEchoCancelerDelayLine1=_RadioEchoCancelerDelayLine1_Object((1,3,6,1,4,1,3373,1103,80,40,1,4),_RadioEchoCancelerDelayLine1_Type())
radioEchoCancelerDelayLine1.setMaxAccess(_D)
if mibBuilder.loadTexts:radioEchoCancelerDelayLine1.setStatus(_A)
class _RadioEchoCancelerDelayLine2_Type(Integer32):defaultValue=0
_RadioEchoCancelerDelayLine2_Type.__name__=_C
_RadioEchoCancelerDelayLine2_Object=MibTableColumn
radioEchoCancelerDelayLine2=_RadioEchoCancelerDelayLine2_Object((1,3,6,1,4,1,3373,1103,80,40,1,5),_RadioEchoCancelerDelayLine2_Type())
radioEchoCancelerDelayLine2.setMaxAccess(_D)
if mibBuilder.loadTexts:radioEchoCancelerDelayLine2.setStatus(_A)
class _RadioEchoCancStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('disabled',0),('uncalibrated',1),('calibrating',2),('calibrated',3),('fail',4),('unavailable',5)))
_RadioEchoCancStatus_Type.__name__=_C
_RadioEchoCancStatus_Object=MibTableColumn
radioEchoCancStatus=_RadioEchoCancStatus_Object((1,3,6,1,4,1,3373,1103,80,40,1,6),_RadioEchoCancStatus_Type())
radioEchoCancStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:radioEchoCancStatus.setStatus(_A)
class _RadioEchoCancStart_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('stop',0),('start',1)))
_RadioEchoCancStart_Type.__name__=_C
_RadioEchoCancStart_Object=MibTableColumn
radioEchoCancStart=_RadioEchoCancStart_Object((1,3,6,1,4,1,3373,1103,80,40,1,7),_RadioEchoCancStart_Type())
radioEchoCancStart.setMaxAccess(_D)
if mibBuilder.loadTexts:radioEchoCancStart.setStatus(_A)
class _RadioRemDemodulatorFailAlarmSeverityCode_Type(AlarmSeverityCode):defaultValue=21
_RadioRemDemodulatorFailAlarmSeverityCode_Type.__name__=_H
_RadioRemDemodulatorFailAlarmSeverityCode_Object=MibScalar
radioRemDemodulatorFailAlarmSeverityCode=_RadioRemDemodulatorFailAlarmSeverityCode_Object((1,3,6,1,4,1,3373,1103,80,50),_RadioRemDemodulatorFailAlarmSeverityCode_Type())
radioRemDemodulatorFailAlarmSeverityCode.setMaxAccess(_D)
if mibBuilder.loadTexts:radioRemDemodulatorFailAlarmSeverityCode.setStatus(_A)
class _RadioRxActiveStatusTrapNotification_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_RadioRxActiveStatusTrapNotification_Type.__name__=_C
_RadioRxActiveStatusTrapNotification_Object=MibScalar
radioRxActiveStatusTrapNotification=_RadioRxActiveStatusTrapNotification_Object((1,3,6,1,4,1,3373,1103,80,51),_RadioRxActiveStatusTrapNotification_Type())
radioRxActiveStatusTrapNotification.setMaxAccess(_D)
if mibBuilder.loadTexts:radioRxActiveStatusTrapNotification.setStatus(_A)
class _RadioTxActiveStatusTrapNotification_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_RadioTxActiveStatusTrapNotification_Type.__name__=_C
_RadioTxActiveStatusTrapNotification_Object=MibScalar
radioTxActiveStatusTrapNotification=_RadioTxActiveStatusTrapNotification_Object((1,3,6,1,4,1,3373,1103,80,52),_RadioTxActiveStatusTrapNotification_Type())
radioTxActiveStatusTrapNotification.setMaxAccess(_D)
if mibBuilder.loadTexts:radioTxActiveStatusTrapNotification.setStatus(_A)
class _RadioCableOpenAlarmSeverityCode_Type(AlarmSeverityCode):defaultValue=5
_RadioCableOpenAlarmSeverityCode_Type.__name__=_H
_RadioCableOpenAlarmSeverityCode_Object=MibScalar
radioCableOpenAlarmSeverityCode=_RadioCableOpenAlarmSeverityCode_Object((1,3,6,1,4,1,3373,1103,80,53),_RadioCableOpenAlarmSeverityCode_Type())
radioCableOpenAlarmSeverityCode.setMaxAccess(_D)
if mibBuilder.loadTexts:radioCableOpenAlarmSeverityCode.setStatus(_A)
class _RadioCableShortAlarmSeverityCode_Type(AlarmSeverityCode):defaultValue=5
_RadioCableShortAlarmSeverityCode_Type.__name__=_H
_RadioCableShortAlarmSeverityCode_Object=MibScalar
radioCableShortAlarmSeverityCode=_RadioCableShortAlarmSeverityCode_Object((1,3,6,1,4,1,3373,1103,80,54),_RadioCableShortAlarmSeverityCode_Type())
radioCableShortAlarmSeverityCode.setMaxAccess(_D)
if mibBuilder.loadTexts:radioCableShortAlarmSeverityCode.setStatus(_A)
class _RadioInvalidFrequencyAlarmSeverityCode_Type(AlarmSeverityCode):defaultValue=5
_RadioInvalidFrequencyAlarmSeverityCode_Type.__name__=_H
_RadioInvalidFrequencyAlarmSeverityCode_Object=MibScalar
radioInvalidFrequencyAlarmSeverityCode=_RadioInvalidFrequencyAlarmSeverityCode_Object((1,3,6,1,4,1,3373,1103,80,55),_RadioInvalidFrequencyAlarmSeverityCode_Type())
radioInvalidFrequencyAlarmSeverityCode.setMaxAccess(_D)
if mibBuilder.loadTexts:radioInvalidFrequencyAlarmSeverityCode.setStatus(_A)
class _RadioBaseBandRxAlarmSeverityCode_Type(AlarmSeverityCode):defaultValue=5
_RadioBaseBandRxAlarmSeverityCode_Type.__name__=_H
_RadioBaseBandRxAlarmSeverityCode_Object=MibScalar
radioBaseBandRxAlarmSeverityCode=_RadioBaseBandRxAlarmSeverityCode_Object((1,3,6,1,4,1,3373,1103,80,56),_RadioBaseBandRxAlarmSeverityCode_Type())
radioBaseBandRxAlarmSeverityCode.setMaxAccess(_D)
if mibBuilder.loadTexts:radioBaseBandRxAlarmSeverityCode.setStatus(_A)
class _RadioModulatorFailAlarmSeverityCode_Type(AlarmSeverityCode):defaultValue=21
_RadioModulatorFailAlarmSeverityCode_Type.__name__=_H
_RadioModulatorFailAlarmSeverityCode_Object=MibScalar
radioModulatorFailAlarmSeverityCode=_RadioModulatorFailAlarmSeverityCode_Object((1,3,6,1,4,1,3373,1103,80,57),_RadioModulatorFailAlarmSeverityCode_Type())
radioModulatorFailAlarmSeverityCode.setMaxAccess(_D)
if mibBuilder.loadTexts:radioModulatorFailAlarmSeverityCode.setStatus(_A)
class _RadioDemodulatorFailAlarmSeverityCode_Type(AlarmSeverityCode):defaultValue=5
_RadioDemodulatorFailAlarmSeverityCode_Type.__name__=_H
_RadioDemodulatorFailAlarmSeverityCode_Object=MibScalar
radioDemodulatorFailAlarmSeverityCode=_RadioDemodulatorFailAlarmSeverityCode_Object((1,3,6,1,4,1,3373,1103,80,58),_RadioDemodulatorFailAlarmSeverityCode_Type())
radioDemodulatorFailAlarmSeverityCode.setMaxAccess(_D)
if mibBuilder.loadTexts:radioDemodulatorFailAlarmSeverityCode.setStatus(_A)
class _RadioRxPowerLowAlarmSeverityCode_Type(AlarmSeverityCode):defaultValue=21
_RadioRxPowerLowAlarmSeverityCode_Type.__name__=_H
_RadioRxPowerLowAlarmSeverityCode_Object=MibScalar
radioRxPowerLowAlarmSeverityCode=_RadioRxPowerLowAlarmSeverityCode_Object((1,3,6,1,4,1,3373,1103,80,59),_RadioRxPowerLowAlarmSeverityCode_Type())
radioRxPowerLowAlarmSeverityCode.setMaxAccess(_D)
if mibBuilder.loadTexts:radioRxPowerLowAlarmSeverityCode.setStatus(_A)
class _RadioTxPowerLowAlarmSeverityCode_Type(AlarmSeverityCode):defaultValue=5
_RadioTxPowerLowAlarmSeverityCode_Type.__name__=_H
_RadioTxPowerLowAlarmSeverityCode_Object=MibScalar
radioTxPowerLowAlarmSeverityCode=_RadioTxPowerLowAlarmSeverityCode_Object((1,3,6,1,4,1,3373,1103,80,60),_RadioTxPowerLowAlarmSeverityCode_Type())
radioTxPowerLowAlarmSeverityCode.setMaxAccess(_D)
if mibBuilder.loadTexts:radioTxPowerLowAlarmSeverityCode.setStatus(_A)
class _RadioVcoFailAlarmSeverityCode_Type(AlarmSeverityCode):defaultValue=5
_RadioVcoFailAlarmSeverityCode_Type.__name__=_H
_RadioVcoFailAlarmSeverityCode_Object=MibScalar
radioVcoFailAlarmSeverityCode=_RadioVcoFailAlarmSeverityCode_Object((1,3,6,1,4,1,3373,1103,80,61),_RadioVcoFailAlarmSeverityCode_Type())
radioVcoFailAlarmSeverityCode.setMaxAccess(_D)
if mibBuilder.loadTexts:radioVcoFailAlarmSeverityCode.setStatus(_A)
class _RadioRxIFAgcAlarmSeverityCode_Type(AlarmSeverityCode):defaultValue=21
_RadioRxIFAgcAlarmSeverityCode_Type.__name__=_H
_RadioRxIFAgcAlarmSeverityCode_Object=MibScalar
radioRxIFAgcAlarmSeverityCode=_RadioRxIFAgcAlarmSeverityCode_Object((1,3,6,1,4,1,3373,1103,80,62),_RadioRxIFAgcAlarmSeverityCode_Type())
radioRxIFAgcAlarmSeverityCode.setMaxAccess(_D)
if mibBuilder.loadTexts:radioRxIFAgcAlarmSeverityCode.setStatus(_A)
class _RadioTxIFAgcAlarmSeverityCode_Type(AlarmSeverityCode):defaultValue=5
_RadioTxIFAgcAlarmSeverityCode_Type.__name__=_H
_RadioTxIFAgcAlarmSeverityCode_Object=MibScalar
radioTxIFAgcAlarmSeverityCode=_RadioTxIFAgcAlarmSeverityCode_Object((1,3,6,1,4,1,3373,1103,80,63),_RadioTxIFAgcAlarmSeverityCode_Type())
radioTxIFAgcAlarmSeverityCode.setMaxAccess(_D)
if mibBuilder.loadTexts:radioTxIFAgcAlarmSeverityCode.setStatus(_A)
class _RadioIduOduCommunicationAlarmSeverityCode_Type(AlarmSeverityCode):defaultValue=5
_RadioIduOduCommunicationAlarmSeverityCode_Type.__name__=_H
_RadioIduOduCommunicationAlarmSeverityCode_Object=MibScalar
radioIduOduCommunicationAlarmSeverityCode=_RadioIduOduCommunicationAlarmSeverityCode_Object((1,3,6,1,4,1,3373,1103,80,64),_RadioIduOduCommunicationAlarmSeverityCode_Type())
radioIduOduCommunicationAlarmSeverityCode.setMaxAccess(_D)
if mibBuilder.loadTexts:radioIduOduCommunicationAlarmSeverityCode.setStatus(_A)
class _RadioOduIduCommunicationAlarmSeverityCode_Type(AlarmSeverityCode):defaultValue=3
_RadioOduIduCommunicationAlarmSeverityCode_Type.__name__=_H
_RadioOduIduCommunicationAlarmSeverityCode_Object=MibScalar
radioOduIduCommunicationAlarmSeverityCode=_RadioOduIduCommunicationAlarmSeverityCode_Object((1,3,6,1,4,1,3373,1103,80,65),_RadioOduIduCommunicationAlarmSeverityCode_Type())
radioOduIduCommunicationAlarmSeverityCode.setMaxAccess(_D)
if mibBuilder.loadTexts:radioOduIduCommunicationAlarmSeverityCode.setStatus(_A)
class _RadioLocalOduAlarmSynthesisSeverityCode_Type(AlarmSeverityCode):defaultValue=18
_RadioLocalOduAlarmSynthesisSeverityCode_Type.__name__=_H
_RadioLocalOduAlarmSynthesisSeverityCode_Object=MibScalar
radioLocalOduAlarmSynthesisSeverityCode=_RadioLocalOduAlarmSynthesisSeverityCode_Object((1,3,6,1,4,1,3373,1103,80,66),_RadioLocalOduAlarmSynthesisSeverityCode_Type())
radioLocalOduAlarmSynthesisSeverityCode.setMaxAccess(_D)
if mibBuilder.loadTexts:radioLocalOduAlarmSynthesisSeverityCode.setStatus(_A)
class _RadioRemoteOduAlarmSynthesisSeverityCode_Type(AlarmSeverityCode):defaultValue=18
_RadioRemoteOduAlarmSynthesisSeverityCode_Type.__name__=_H
_RadioRemoteOduAlarmSynthesisSeverityCode_Object=MibScalar
radioRemoteOduAlarmSynthesisSeverityCode=_RadioRemoteOduAlarmSynthesisSeverityCode_Object((1,3,6,1,4,1,3373,1103,80,67),_RadioRemoteOduAlarmSynthesisSeverityCode_Type())
radioRemoteOduAlarmSynthesisSeverityCode.setMaxAccess(_D)
if mibBuilder.loadTexts:radioRemoteOduAlarmSynthesisSeverityCode.setStatus(_A)
class _RadioConfigMismatchAlarmSeverityCode_Type(AlarmSeverityCode):defaultValue=21
_RadioConfigMismatchAlarmSeverityCode_Type.__name__=_H
_RadioConfigMismatchAlarmSeverityCode_Object=MibScalar
radioConfigMismatchAlarmSeverityCode=_RadioConfigMismatchAlarmSeverityCode_Object((1,3,6,1,4,1,3373,1103,80,68),_RadioConfigMismatchAlarmSeverityCode_Type())
radioConfigMismatchAlarmSeverityCode.setMaxAccess(_D)
if mibBuilder.loadTexts:radioConfigMismatchAlarmSeverityCode.setStatus(_A)
class _RadioPrxHysteresisValue_Type(Integer32):defaultValue=3
_RadioPrxHysteresisValue_Type.__name__=_C
_RadioPrxHysteresisValue_Object=MibScalar
radioPrxHysteresisValue=_RadioPrxHysteresisValue_Object((1,3,6,1,4,1,3373,1103,80,69),_RadioPrxHysteresisValue_Type())
radioPrxHysteresisValue.setMaxAccess(_D)
if mibBuilder.loadTexts:radioPrxHysteresisValue.setStatus(_A)
class _RadioPtxHysteresisValue_Type(Integer32):defaultValue=3
_RadioPtxHysteresisValue_Type.__name__=_C
_RadioPtxHysteresisValue_Object=MibScalar
radioPtxHysteresisValue=_RadioPtxHysteresisValue_Object((1,3,6,1,4,1,3373,1103,80,70),_RadioPtxHysteresisValue_Type())
radioPtxHysteresisValue.setMaxAccess(_D)
if mibBuilder.loadTexts:radioPtxHysteresisValue.setStatus(_A)
class _RadioPrxHysteresisValueTrapNotification_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_RadioPrxHysteresisValueTrapNotification_Type.__name__=_C
_RadioPrxHysteresisValueTrapNotification_Object=MibScalar
radioPrxHysteresisValueTrapNotification=_RadioPrxHysteresisValueTrapNotification_Object((1,3,6,1,4,1,3373,1103,80,71),_RadioPrxHysteresisValueTrapNotification_Type())
radioPrxHysteresisValueTrapNotification.setMaxAccess(_D)
if mibBuilder.loadTexts:radioPrxHysteresisValueTrapNotification.setStatus(_A)
class _RadioPtxHysteresisValueTrapNotification_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_RadioPtxHysteresisValueTrapNotification_Type.__name__=_C
_RadioPtxHysteresisValueTrapNotification_Object=MibScalar
radioPtxHysteresisValueTrapNotification=_RadioPtxHysteresisValueTrapNotification_Object((1,3,6,1,4,1,3373,1103,80,72),_RadioPtxHysteresisValueTrapNotification_Type())
radioPtxHysteresisValueTrapNotification.setMaxAccess(_D)
if mibBuilder.loadTexts:radioPtxHysteresisValueTrapNotification.setStatus(_A)
class _RadioRxQualityLowAlarmSeverityCode_Type(AlarmSeverityCode):defaultValue=21
_RadioRxQualityLowAlarmSeverityCode_Type.__name__=_H
_RadioRxQualityLowAlarmSeverityCode_Object=MibScalar
radioRxQualityLowAlarmSeverityCode=_RadioRxQualityLowAlarmSeverityCode_Object((1,3,6,1,4,1,3373,1103,80,73),_RadioRxQualityLowAlarmSeverityCode_Type())
radioRxQualityLowAlarmSeverityCode.setMaxAccess(_D)
if mibBuilder.loadTexts:radioRxQualityLowAlarmSeverityCode.setStatus(_A)
class _RadioRxQualityWarningAlarmSeverityCode_Type(AlarmSeverityCode):defaultValue=21
_RadioRxQualityWarningAlarmSeverityCode_Type.__name__=_H
_RadioRxQualityWarningAlarmSeverityCode_Object=MibScalar
radioRxQualityWarningAlarmSeverityCode=_RadioRxQualityWarningAlarmSeverityCode_Object((1,3,6,1,4,1,3373,1103,80,74),_RadioRxQualityWarningAlarmSeverityCode_Type())
radioRxQualityWarningAlarmSeverityCode.setMaxAccess(_D)
if mibBuilder.loadTexts:radioRxQualityWarningAlarmSeverityCode.setStatus(_A)
class _LinkReducedCapacityAlarmSeverityCode_Type(AlarmSeverityCode):defaultValue=19
_LinkReducedCapacityAlarmSeverityCode_Type.__name__=_H
_LinkReducedCapacityAlarmSeverityCode_Object=MibScalar
linkReducedCapacityAlarmSeverityCode=_LinkReducedCapacityAlarmSeverityCode_Object((1,3,6,1,4,1,3373,1103,80,75),_LinkReducedCapacityAlarmSeverityCode_Type())
linkReducedCapacityAlarmSeverityCode.setMaxAccess(_D)
if mibBuilder.loadTexts:linkReducedCapacityAlarmSeverityCode.setStatus(_A)
class _LinkLinkTelemetryFailAlarmSeverityCode_Type(AlarmSeverityCode):defaultValue=5
_LinkLinkTelemetryFailAlarmSeverityCode_Type.__name__=_H
_LinkLinkTelemetryFailAlarmSeverityCode_Object=MibScalar
linkLinkTelemetryFailAlarmSeverityCode=_LinkLinkTelemetryFailAlarmSeverityCode_Object((1,3,6,1,4,1,3373,1103,80,76),_LinkLinkTelemetryFailAlarmSeverityCode_Type())
linkLinkTelemetryFailAlarmSeverityCode.setMaxAccess(_D)
if mibBuilder.loadTexts:linkLinkTelemetryFailAlarmSeverityCode.setStatus(_A)
class _LinkIdMismatchAlarmSeverityCode_Type(AlarmSeverityCode):defaultValue=5
_LinkIdMismatchAlarmSeverityCode_Type.__name__=_H
_LinkIdMismatchAlarmSeverityCode_Object=MibScalar
linkIdMismatchAlarmSeverityCode=_LinkIdMismatchAlarmSeverityCode_Object((1,3,6,1,4,1,3373,1103,80,77),_LinkIdMismatchAlarmSeverityCode_Type())
linkIdMismatchAlarmSeverityCode.setMaxAccess(_D)
if mibBuilder.loadTexts:linkIdMismatchAlarmSeverityCode.setStatus(_A)
class _LinkRadioEocAlarmSeverityCode_Type(AlarmSeverityCode):defaultValue=21
_LinkRadioEocAlarmSeverityCode_Type.__name__=_H
_LinkRadioEocAlarmSeverityCode_Object=MibScalar
linkRadioEocAlarmSeverityCode=_LinkRadioEocAlarmSeverityCode_Object((1,3,6,1,4,1,3373,1103,80,78),_LinkRadioEocAlarmSeverityCode_Type())
linkRadioEocAlarmSeverityCode.setMaxAccess(_D)
if mibBuilder.loadTexts:linkRadioEocAlarmSeverityCode.setStatus(_A)
class _LinkSetupMismatchAlarmSeverityCode_Type(AlarmSeverityCode):defaultValue=3
_LinkSetupMismatchAlarmSeverityCode_Type.__name__=_H
_LinkSetupMismatchAlarmSeverityCode_Object=MibScalar
linkSetupMismatchAlarmSeverityCode=_LinkSetupMismatchAlarmSeverityCode_Object((1,3,6,1,4,1,3373,1103,80,79),_LinkSetupMismatchAlarmSeverityCode_Type())
linkSetupMismatchAlarmSeverityCode.setMaxAccess(_D)
if mibBuilder.loadTexts:linkSetupMismatchAlarmSeverityCode.setStatus(_A)
class _LinkRescueSetupAlarmSeverityCode_Type(AlarmSeverityCode):defaultValue=6
_LinkRescueSetupAlarmSeverityCode_Type.__name__=_H
_LinkRescueSetupAlarmSeverityCode_Object=MibScalar
linkRescueSetupAlarmSeverityCode=_LinkRescueSetupAlarmSeverityCode_Object((1,3,6,1,4,1,3373,1103,80,80),_LinkRescueSetupAlarmSeverityCode_Type())
linkRescueSetupAlarmSeverityCode.setMaxAccess(_D)
if mibBuilder.loadTexts:linkRescueSetupAlarmSeverityCode.setStatus(_A)
class _LinkXpicProcedureBlockAlarmSeverityCode_Type(AlarmSeverityCode):defaultValue=21
_LinkXpicProcedureBlockAlarmSeverityCode_Type.__name__=_H
_LinkXpicProcedureBlockAlarmSeverityCode_Object=MibScalar
linkXpicProcedureBlockAlarmSeverityCode=_LinkXpicProcedureBlockAlarmSeverityCode_Object((1,3,6,1,4,1,3373,1103,80,81),_LinkXpicProcedureBlockAlarmSeverityCode_Type())
linkXpicProcedureBlockAlarmSeverityCode.setMaxAccess(_D)
if mibBuilder.loadTexts:linkXpicProcedureBlockAlarmSeverityCode.setStatus(_A)
class _LinkXpicRemTxOffAlarmAlarmSeverityCode_Type(AlarmSeverityCode):defaultValue=21
_LinkXpicRemTxOffAlarmAlarmSeverityCode_Type.__name__=_H
_LinkXpicRemTxOffAlarmAlarmSeverityCode_Object=MibScalar
linkXpicRemTxOffAlarmAlarmSeverityCode=_LinkXpicRemTxOffAlarmAlarmSeverityCode_Object((1,3,6,1,4,1,3373,1103,80,82),_LinkXpicRemTxOffAlarmAlarmSeverityCode_Type())
linkXpicRemTxOffAlarmAlarmSeverityCode.setMaxAccess(_D)
if mibBuilder.loadTexts:linkXpicRemTxOffAlarmAlarmSeverityCode.setStatus(_A)
_LinkLocalIduAlarmSynthesis_Type=AlarmStatus
_LinkLocalIduAlarmSynthesis_Object=MibScalar
linkLocalIduAlarmSynthesis=_LinkLocalIduAlarmSynthesis_Object((1,3,6,1,4,1,3373,1103,80,83),_LinkLocalIduAlarmSynthesis_Type())
linkLocalIduAlarmSynthesis.setMaxAccess(_B)
if mibBuilder.loadTexts:linkLocalIduAlarmSynthesis.setStatus(_A)
class _LinkLocalIduAlarmSynthesisSeverityCode_Type(AlarmSeverityCode):defaultValue=18
_LinkLocalIduAlarmSynthesisSeverityCode_Type.__name__=_H
_LinkLocalIduAlarmSynthesisSeverityCode_Object=MibScalar
linkLocalIduAlarmSynthesisSeverityCode=_LinkLocalIduAlarmSynthesisSeverityCode_Object((1,3,6,1,4,1,3373,1103,80,84),_LinkLocalIduAlarmSynthesisSeverityCode_Type())
linkLocalIduAlarmSynthesisSeverityCode.setMaxAccess(_D)
if mibBuilder.loadTexts:linkLocalIduAlarmSynthesisSeverityCode.setStatus(_A)
class _LinkRemoteIduAlarmSynthesisSeverityCode_Type(AlarmSeverityCode):defaultValue=18
_LinkRemoteIduAlarmSynthesisSeverityCode_Type.__name__=_H
_LinkRemoteIduAlarmSynthesisSeverityCode_Object=MibScalar
linkRemoteIduAlarmSynthesisSeverityCode=_LinkRemoteIduAlarmSynthesisSeverityCode_Object((1,3,6,1,4,1,3373,1103,80,85),_LinkRemoteIduAlarmSynthesisSeverityCode_Type())
linkRemoteIduAlarmSynthesisSeverityCode.setMaxAccess(_D)
if mibBuilder.loadTexts:linkRemoteIduAlarmSynthesisSeverityCode.setStatus(_A)
class _LinkTfcAlarmSeverityCode_Type(AlarmSeverityCode):defaultValue=20
_LinkTfcAlarmSeverityCode_Type.__name__=_H
_LinkTfcAlarmSeverityCode_Object=MibScalar
linkTfcAlarmSeverityCode=_LinkTfcAlarmSeverityCode_Object((1,3,6,1,4,1,3373,1103,80,86),_LinkTfcAlarmSeverityCode_Type())
linkTfcAlarmSeverityCode.setMaxAccess(_D)
if mibBuilder.loadTexts:linkTfcAlarmSeverityCode.setStatus(_A)
class _LinkBerSyncLossAlarmSeverityCode_Type(AlarmSeverityCode):defaultValue=5
_LinkBerSyncLossAlarmSeverityCode_Type.__name__=_H
_LinkBerSyncLossAlarmSeverityCode_Object=MibScalar
linkBerSyncLossAlarmSeverityCode=_LinkBerSyncLossAlarmSeverityCode_Object((1,3,6,1,4,1,3373,1103,80,87),_LinkBerSyncLossAlarmSeverityCode_Type())
linkBerSyncLossAlarmSeverityCode.setMaxAccess(_D)
if mibBuilder.loadTexts:linkBerSyncLossAlarmSeverityCode.setStatus(_A)
class _LinkNotMatchingRadiosAlarmSeverityCode_Type(AlarmSeverityCode):defaultValue=21
_LinkNotMatchingRadiosAlarmSeverityCode_Type.__name__=_H
_LinkNotMatchingRadiosAlarmSeverityCode_Object=MibScalar
linkNotMatchingRadiosAlarmSeverityCode=_LinkNotMatchingRadiosAlarmSeverityCode_Object((1,3,6,1,4,1,3373,1103,80,88),_LinkNotMatchingRadiosAlarmSeverityCode_Type())
linkNotMatchingRadiosAlarmSeverityCode.setMaxAccess(_D)
if mibBuilder.loadTexts:linkNotMatchingRadiosAlarmSeverityCode.setStatus(_A)
class _ChannelSpacingSelection_Type(Bits):defaultBinValue='11';namedValues=NamedValues(*(('etsi',0),('fcc',1)))
_ChannelSpacingSelection_Type.__name__='Bits'
_ChannelSpacingSelection_Object=MibScalar
channelSpacingSelection=_ChannelSpacingSelection_Object((1,3,6,1,4,1,3373,1103,80,89),_ChannelSpacingSelection_Type())
channelSpacingSelection.setMaxAccess(_D)
if mibBuilder.loadTexts:channelSpacingSelection.setStatus(_A)
class _FadeMarginMeasure_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_FadeMarginMeasure_Type.__name__=_C
_FadeMarginMeasure_Object=MibScalar
fadeMarginMeasure=_FadeMarginMeasure_Object((1,3,6,1,4,1,3373,1103,80,90),_FadeMarginMeasure_Type())
fadeMarginMeasure.setMaxAccess(_D)
if mibBuilder.loadTexts:fadeMarginMeasure.setStatus(_A)
class _LinkConfigurationInProgressTrapNotification_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_LinkConfigurationInProgressTrapNotification_Type.__name__=_C
_LinkConfigurationInProgressTrapNotification_Object=MibScalar
linkConfigurationInProgressTrapNotification=_LinkConfigurationInProgressTrapNotification_Object((1,3,6,1,4,1,3373,1103,80,91),_LinkConfigurationInProgressTrapNotification_Type())
linkConfigurationInProgressTrapNotification.setMaxAccess(_D)
if mibBuilder.loadTexts:linkConfigurationInProgressTrapNotification.setStatus(_A)
class _RadioXpicAlarmSeverityCode_Type(AlarmSeverityCode):defaultValue=5
_RadioXpicAlarmSeverityCode_Type.__name__=_H
_RadioXpicAlarmSeverityCode_Object=MibScalar
radioXpicAlarmSeverityCode=_RadioXpicAlarmSeverityCode_Object((1,3,6,1,4,1,3373,1103,80,92),_RadioXpicAlarmSeverityCode_Type())
radioXpicAlarmSeverityCode.setMaxAccess(_D)
if mibBuilder.loadTexts:radioXpicAlarmSeverityCode.setStatus(_A)
radioPrxChange=NotificationType((1,3,6,1,4,1,3373,1103,0,8001))
radioPrxChange.setObjects(*((_V,_W),(_E,_L),(_E,_c),(_E,'radioPrx')))
if mibBuilder.loadTexts:radioPrxChange.setStatus(_A)
radioPtxChange=NotificationType((1,3,6,1,4,1,3373,1103,0,8002))
radioPtxChange.setObjects(*((_V,_W),(_E,_L),(_E,_c),(_E,'radioPtx')))
if mibBuilder.loadTexts:radioPtxChange.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'ChannelSpacing':ChannelSpacing,'ModulationMap':ModulationMap,'ConfigMismatchReason':ConfigMismatchReason,'RadioCapability':RadioCapability,_o:BitsPerSymbol,_w:Stm1IndexOrZero,'radioPrxChange':radioPrxChange,'radioPtxChange':radioPtxChange,'radioSystem':radioSystem,'radioSystemMibVersion':radioSystemMibVersion,'radioTable':radioTable,'radioEntry':radioEntry,_L:radioIndex,'radioLabel':radioLabel,'radioType':radioType,'radioIfIndex':radioIfIndex,'radioStorageType':radioStorageType,'xpicTable':xpicTable,'xpicEntry':xpicEntry,_X:xpicIndex,'xpicRadioIdx':xpicRadioIdx,'xpicRowstatus':xpicRowstatus,'xpicChTable':xpicChTable,'xpicChEntry':xpicChEntry,_f:xpicChPolIndex,'xpicChRadioIdx':xpicChRadioIdx,'xpicChRowstatus':xpicChRowstatus,'linkAvailableIndex':linkAvailableIndex,'linkTable':linkTable,'linkEntry':linkEntry,_K:linkIndex,'linkType':linkType,'linkLabel':linkLabel,'linkIfIndex':linkIfIndex,'linkRowstatus':linkRowstatus,'linkChTable':linkChTable,'linkChEntry':linkChEntry,_g:linkChIndex,'linkChRadioIdx':linkChRadioIdx,'linkChRadioSettingsIdx':linkChRadioSettingsIdx,'linkChRowstatus':linkChRowstatus,'linkSettingsTable':linkSettingsTable,'linkSettingsEntry':linkSettingsEntry,'linkBandwidthAndModulation':linkBandwidthAndModulation,'linkAcmEngineEnable':linkAcmEngineEnable,'linkTxUpperProfile':linkTxUpperProfile,'linkTxLowerProfile':linkTxLowerProfile,'linkId':linkId,'linkTxPwrThresh':linkTxPwrThresh,'linkRxPwrThresh':linkRxPwrThresh,'linkSynchSetupProtocolEnable':linkSynchSetupProtocolEnable,'linkProfilesSetSelection':linkProfilesSetSelection,'linkXpicControlProcedure':linkXpicControlProcedure,'radioSettingsTable':radioSettingsTable,'radioSettingsEntry':radioSettingsEntry,_P:radioSettingsIndex,'radioSettingsRowStatus':radioSettingsRowStatus,_c:radioSettingsLabel,'radioTxFrequency':radioTxFrequency,'radioDuplexFrequency':radioDuplexFrequency,'radioTxAttenuation':radioTxAttenuation,'radioAtpcManual':radioAtpcManual,'radioAtpcPwrHigh':radioAtpcPwrHigh,'radioAtpcPwrLow':radioAtpcPwrLow,'radioAtpcRange':radioAtpcRange,'radioFreqTableSelection':radioFreqTableSelection,'tdmSettingsTable':tdmSettingsTable,'tdmSettingsEntry':tdmSettingsEntry,_j:tdmPolIndex,'tdmE1Channel':tdmE1Channel,'tdmE1Framer':tdmE1Framer,'radioCapabilitiesTable':radioCapabilitiesTable,'radioCapabilitiesEntry':radioCapabilitiesEntry,'radioCapabilitiesCapability':radioCapabilitiesCapability,'radioCapabilitiesTxMinFrequency':radioCapabilitiesTxMinFrequency,'radioCapabilitiesTxMaxFrequency':radioCapabilitiesTxMaxFrequency,'radioCapabilitiesStepFrequency':radioCapabilitiesStepFrequency,'radioCapabilitiesMinPtxNominalValue':radioCapabilitiesMinPtxNominalValue,'radioCapabilitiesMaxPtxNominalValue':radioCapabilitiesMaxPtxNominalValue,'radioCapabilitiesExtendedMinPwr':radioCapabilitiesExtendedMinPwr,'radioStatusTable':radioStatusTable,'radioStatusEntry':radioStatusEntry,'radioCurrentDuplexFrequency':radioCurrentDuplexFrequency,'radioTxChannelSpacing':radioTxChannelSpacing,'radioPrx':radioPrx,'radioPtx':radioPtx,'radioNormalizedMse':radioNormalizedMse,'radioRxActiveStatus':radioRxActiveStatus,'radioTxActiveStatus':radioTxActiveStatus,'radioCableOpenAlarm':radioCableOpenAlarm,'radioCableShortAlarm':radioCableShortAlarm,'radioInvalidFrequencyAlarm':radioInvalidFrequencyAlarm,'radioBaseBandRxAlarm':radioBaseBandRxAlarm,'radioModulatorFailAlarm':radioModulatorFailAlarm,'radioDemodulatorFailAlarm':radioDemodulatorFailAlarm,'radioRxPowerLowAlarm':radioRxPowerLowAlarm,'radioTxPowerLowAlarm':radioTxPowerLowAlarm,'radioRemDemodulatorFailAlarm':radioRemDemodulatorFailAlarm,'radioVcoFailAlarm':radioVcoFailAlarm,'radioRxIFAgcAlarm':radioRxIFAgcAlarm,'radioTxIFAgcAlarm':radioTxIFAgcAlarm,'radioIduOduCommunicationAlarm':radioIduOduCommunicationAlarm,'radioOduIduCommunicationAlarm':radioOduIduCommunicationAlarm,'radioLocalOduAlarmSynthesis':radioLocalOduAlarmSynthesis,'radioRemoteOduAlarmSynthesis':radioRemoteOduAlarmSynthesis,'radioConfigMismatchAlarm':radioConfigMismatchAlarm,'radioConfigAlarmReason':radioConfigAlarmReason,'radioRxQualityLowAlarm':radioRxQualityLowAlarm,'radioRxQualityWarningAlarm':radioRxQualityWarningAlarm,'radioXpd':radioXpd,'radioXpicAlarm':radioXpicAlarm,'radioMaintTable':radioMaintTable,'radioMaintEntry':radioMaintEntry,'radioTxStatus':radioTxStatus,'radioCarrierOnly':radioCarrierOnly,'radioLoop':radioLoop,'radioRFLoopTestResult':radioRFLoopTestResult,'radioRFLoopTestPercTime':radioRFLoopTestPercTime,'radioRtPsuOff':radioRtPsuOff,'radioLom':radioLom,'radioXpic':radioXpic,'radioFrequencyTable':radioFrequencyTable,'radioFreqTabEntry':radioFreqTabEntry,_k:radioFreqChannelId,'radioFreqChannelNum':radioFreqChannelNum,'radioFreqValue':radioFreqValue,'radioDuplexFrequencyTable':radioDuplexFrequencyTable,'radioDuplexFreqEntry':radioDuplexFreqEntry,_l:radioDuplexFreqId,'radioDuplexFreqValue':radioDuplexFreqValue,'radioModulationTable':radioModulationTable,'radioModulationEntry':radioModulationEntry,_m:radioChannelSpacing,'radioModulationMap':radioModulationMap,'radioRefModulationMap':radioRefModulationMap,'linkStatusTable':linkStatusTable,'linkStatusEntry':linkStatusEntry,_M:linkPolIndex,'linkAcmRxProfile':linkAcmRxProfile,'linkAcmTxProfile':linkAcmTxProfile,'linkAcmRxProfileLabel':linkAcmRxProfileLabel,'linkAcmTxProfileLabel':linkAcmTxProfileLabel,'linkAcmRxModulation':linkAcmRxModulation,'linkAcmTxModulation':linkAcmTxModulation,'linkAcmRxCode':linkAcmRxCode,'linkAcmTxCode':linkAcmTxCode,'linkTxETHCapacity':linkTxETHCapacity,'linkRxETHCapacity':linkRxETHCapacity,'linkTxTDMCapacity':linkTxTDMCapacity,'linkRxTDMCapacity':linkRxTDMCapacity,'linkRescueModulation':linkRescueModulation,'linkReducedCapacityAlarm':linkReducedCapacityAlarm,'linkLinkTelemetryFailAlarm':linkLinkTelemetryFailAlarm,'linkIdMismatchAlarm':linkIdMismatchAlarm,'linkRadioEocAlarm':linkRadioEocAlarm,'linkSetupMismatchAlarm':linkSetupMismatchAlarm,'linkRescueSetupAlarm':linkRescueSetupAlarm,'linkXpicProcedureBlockAlarm':linkXpicProcedureBlockAlarm,'linkXpicRemTxOffAlarm':linkXpicRemTxOffAlarm,'linkRemoteIduAlarmSynthesis':linkRemoteIduAlarmSynthesis,'linkNotMatchingRadiosAlarm':linkNotMatchingRadiosAlarm,'linkConfigurationInProgress':linkConfigurationInProgress,'linkXpd':linkXpd,'linkTfcTable':linkTfcTable,'linkTfcEntry':linkTfcEntry,'linkTfcAction':linkTfcAction,'linkTfcControl':linkTfcControl,'linkTfcWatchWindow':linkTfcWatchWindow,'linkTfcAlarmThreshold':linkTfcAlarmThreshold,'linkTfcAlarm':linkTfcAlarm,'linkTfcRowStatus':linkTfcRowStatus,'linkMaintTable':linkMaintTable,'linkMaintEntry':linkMaintEntry,'linkBerStart':linkBerStart,'linkBaseBandLom':linkBaseBandLom,'linkFadeMarginMeasure':linkFadeMarginMeasure,'linkXpicControlProcedureReset':linkXpicControlProcedureReset,'linkBerTable':linkBerTable,'linkBerEntry':linkBerEntry,'linkBerErrorCounterH':linkBerErrorCounterH,'linkBerErrorCounterL':linkBerErrorCounterL,'linkBerDataCounterH':linkBerDataCounterH,'linkBerDataCounterL':linkBerDataCounterL,'linkBerSyncLossAlarm':linkBerSyncLossAlarm,'linkBerSyncLossAlarmCounter':linkBerSyncLossAlarmCounter,'linkBerElapsedTime':linkBerElapsedTime,'linkAcmTable':linkAcmTable,'linkAcmEntry':linkAcmEntry,_T:linkAcmProfileId,'linkAcmProfileModulation':linkAcmProfileModulation,'linkAcmProfileCode':linkAcmProfileCode,'linkAcmProfileCapacity':linkAcmProfileCapacity,'linkAcmProfileLabel':linkAcmProfileLabel,'linkAcmProfileEnable':linkAcmProfileEnable,'linkAcmMaxTDMCapacity':linkAcmMaxTDMCapacity,'linkAcmPowerScaling':linkAcmPowerScaling,'linkAcmDownshiftThreshold':linkAcmDownshiftThreshold,'linkAcmUpshiftThreshold':linkAcmUpshiftThreshold,'linkAcmActiveProfile':linkAcmActiveProfile,'linkAcmTDMCapacity':linkAcmTDMCapacity,'linkAcmETHCapacity':linkAcmETHCapacity,'linkAcmAtpcRxPowerScaling':linkAcmAtpcRxPowerScaling,'linkAcmPowerRange':linkAcmPowerRange,'linkProTable':linkProTable,'linkProEntry':linkProEntry,'linkProProtectionTxChIdx':linkProProtectionTxChIdx,'linkProProtectionRxChIdx':linkProProtectionRxChIdx,'linkProTxWtrTime':linkProTxWtrTime,'linkProRxWtrTime':linkProRxWtrTime,'linkProTxSwitchedChIdx':linkProTxSwitchedChIdx,'linkProRxSwitchedChIdx':linkProRxSwitchedChIdx,'linkProTxRevertive':linkProTxRevertive,'linkProRxRevertive':linkProRxRevertive,'linkProExtraTraffic':linkProExtraTraffic,'linkProRowStatus':linkProRowStatus,'linkProMaintTable':linkProMaintTable,'linkProMaintEntry':linkProMaintEntry,'linkProMaintTxLockout':linkProMaintTxLockout,'linkProMaintRxLockout':linkProMaintRxLockout,'linkProMaintTxForced':linkProMaintTxForced,'linkProMaintRxForced':linkProMaintRxForced,'linkProMaintTxWtrReset':linkProMaintTxWtrReset,'linkProMaintRxWtrReset':linkProMaintRxWtrReset,'linkCapabilitiesTable':linkCapabilitiesTable,'linkCapabilitiesEntry':linkCapabilitiesEntry,'linkCapabilitiesCapability':linkCapabilitiesCapability,'linkCapabilitiesTxMinFrequency':linkCapabilitiesTxMinFrequency,'linkCapabilitiesTxMaxFrequency':linkCapabilitiesTxMaxFrequency,'linkCapabilitiesStepFrequency':linkCapabilitiesStepFrequency,'linkCapabilitiesMinPtxNominalValue':linkCapabilitiesMinPtxNominalValue,'linkCapabilitiesMaxPtxNominalValue':linkCapabilitiesMaxPtxNominalValue,'linkCapabilitiesExtendedMinPwr':linkCapabilitiesExtendedMinPwr,'linkFrequencyTable':linkFrequencyTable,'linkFreqTabEntry':linkFreqTabEntry,_p:linkFreqChannelId,'linkFreqChannelNum':linkFreqChannelNum,'linkFreqValue':linkFreqValue,'linkDuplexFrequencyTable':linkDuplexFrequencyTable,'linkDuplexFreqEntry':linkDuplexFreqEntry,_q:linkDuplexFreqId,'linkDuplexFreqValue':linkDuplexFreqValue,'linkModulationTable':linkModulationTable,'linkModulationEntry':linkModulationEntry,_r:linkChannelSpacing,'linkModulationMap':linkModulationMap,'linkRefModulationMap':linkRefModulationMap,'combinedRadioCapabilitiesTable':combinedRadioCapabilitiesTable,'combinedRadioCapabilitiesEntry':combinedRadioCapabilitiesEntry,'combinedRadioCapabilitiesCapability':combinedRadioCapabilitiesCapability,'combinedRadioCapabilitiesTxMinFrequency':combinedRadioCapabilitiesTxMinFrequency,'combinedRadioCapabilitiesTxMaxFrequency':combinedRadioCapabilitiesTxMaxFrequency,'combinedRadioCapabilitiesStepFrequency':combinedRadioCapabilitiesStepFrequency,'combinedRadioCapabilitiesMinPtxNominalValue':combinedRadioCapabilitiesMinPtxNominalValue,'combinedRadioCapabilitiesMaxPtxNominalValue':combinedRadioCapabilitiesMaxPtxNominalValue,'combinedRadioCapabilitiesExtendedMinPwr':combinedRadioCapabilitiesExtendedMinPwr,'combinedRadioFrequencyTable':combinedRadioFrequencyTable,'combinedRadioFreqTabEntry':combinedRadioFreqTabEntry,_s:combinedRadioFreqChannelId,'combinedRadioFreqChannelNum':combinedRadioFreqChannelNum,'combinedRadioFreqValue':combinedRadioFreqValue,'combinedRadioDuplexFrequencyTable':combinedRadioDuplexFrequencyTable,'combinedRadioDuplexFreqEntry':combinedRadioDuplexFreqEntry,_t:combinedRadioDuplexFreqId,'combinedRadioDuplexFreqValue':combinedRadioDuplexFreqValue,'combinedRadioPowerScalingTable':combinedRadioPowerScalingTable,'combinedRadioPowerScalingEntry':combinedRadioPowerScalingEntry,'combinedRadioPowerScaling':combinedRadioPowerScaling,'combinedRadioAtpcRxPowerScaling':combinedRadioAtpcRxPowerScaling,'combinedRadioPowerRange':combinedRadioPowerRange,'stm1BulkMappingTable':stm1BulkMappingTable,'stm1BulkMappingEntry':stm1BulkMappingEntry,_u:stm1BulkPolIndex,_v:stm1BulkChanIndex,'stm1BulkChannel':stm1BulkChannel,'linkE1vsSTM1CapacityTable':linkE1vsSTM1CapacityTable,'linkE1vsSTM1CapacityEntry':linkE1vsSTM1CapacityEntry,_x:linkE1vsSTM1CapacityStm1,'linkE1vsSTM1CapacityE1':linkE1vsSTM1CapacityE1,'linkTfcV2Table':linkTfcV2Table,'linkTfcV2Entry':linkTfcV2Entry,'linkTfcV2Action':linkTfcV2Action,'linkTfcV2Control':linkTfcV2Control,'linkTfcV2WatchWindow':linkTfcV2WatchWindow,'linkTfcV2AlarmThreshold':linkTfcV2AlarmThreshold,'linkTfcV2Alarm':linkTfcV2Alarm,'linkTfcV2RowStatus':linkTfcV2RowStatus,'linkProV2Table':linkProV2Table,'linkProV2Entry':linkProV2Entry,'linkProV2ProtectionTxChIdx':linkProV2ProtectionTxChIdx,'linkProV2ProtectionRxChIdx':linkProV2ProtectionRxChIdx,'linkProV2TxWtrTime':linkProV2TxWtrTime,'linkProV2RxWtrTime':linkProV2RxWtrTime,'linkProV2TxSwitchedChIdx':linkProV2TxSwitchedChIdx,'linkProV2RxSwitchedChIdx':linkProV2RxSwitchedChIdx,'linkProV2TxRevertive':linkProV2TxRevertive,'linkProV2RxRevertive':linkProV2RxRevertive,'linkProV2ExtraTraffic':linkProV2ExtraTraffic,'linkProV2RowStatus':linkProV2RowStatus,'linkProMaintV2Table':linkProMaintV2Table,'linkProMaintV2Entry':linkProMaintV2Entry,'linkProMaintV2TxLockout':linkProMaintV2TxLockout,'linkProMaintV2RxLockout':linkProMaintV2RxLockout,'linkProMaintV2TxForced':linkProMaintV2TxForced,'linkProMaintV2RxForced':linkProMaintV2RxForced,'linkProMaintV2TxWtrReset':linkProMaintV2TxWtrReset,'linkProMaintV2RxWtrReset':linkProMaintV2RxWtrReset,'sspTable':sspTable,'sspEntry':sspEntry,_z:sspParameterType,'sspLinkBandwidth':sspLinkBandwidth,'sspLinkModulation':sspLinkModulation,'sspLinkAcmEngineEnable':sspLinkAcmEngineEnable,'sspLinkTxUpperProfile':sspLinkTxUpperProfile,'sspLinkTxLowerProfile':sspLinkTxLowerProfile,'sspLinkSynchSetupProtocolEnable':sspLinkSynchSetupProtocolEnable,'sspLinkProfilesSetSelection':sspLinkProfilesSetSelection,'sspTdmE1Channel':sspTdmE1Channel,'sspTdmStm1Channel':sspTdmStm1Channel,'radioLoopCapabilityTable':radioLoopCapabilityTable,'radioLoopCapabilityEntry':radioLoopCapabilityEntry,'radioLoopRfGroup':radioLoopRfGroup,'radioLoopIqGroup':radioLoopIqGroup,'radioLoopBaseBandGroup':radioLoopBaseBandGroup,'radioRxBerThresholdTable':radioRxBerThresholdTable,'radioRxBerThresholdEntry':radioRxBerThresholdEntry,'radioRxBerThresholdStatus':radioRxBerThresholdStatus,'radioNominalRxBerThreshold':radioNominalRxBerThreshold,'radioMeasuredRxBerThreshold':radioMeasuredRxBerThreshold,'radioEchoCancelerTable':radioEchoCancelerTable,'radioEchoCancelerEntry':radioEchoCancelerEntry,'radioEchoCancelerFunctionEn':radioEchoCancelerFunctionEn,'radioEchoCancelerCableLenMin':radioEchoCancelerCableLenMin,'radioEchoCancelerCableLenMax':radioEchoCancelerCableLenMax,'radioEchoCancelerDelayLine1':radioEchoCancelerDelayLine1,'radioEchoCancelerDelayLine2':radioEchoCancelerDelayLine2,'radioEchoCancStatus':radioEchoCancStatus,'radioEchoCancStart':radioEchoCancStart,'radioRemDemodulatorFailAlarmSeverityCode':radioRemDemodulatorFailAlarmSeverityCode,'radioRxActiveStatusTrapNotification':radioRxActiveStatusTrapNotification,'radioTxActiveStatusTrapNotification':radioTxActiveStatusTrapNotification,'radioCableOpenAlarmSeverityCode':radioCableOpenAlarmSeverityCode,'radioCableShortAlarmSeverityCode':radioCableShortAlarmSeverityCode,'radioInvalidFrequencyAlarmSeverityCode':radioInvalidFrequencyAlarmSeverityCode,'radioBaseBandRxAlarmSeverityCode':radioBaseBandRxAlarmSeverityCode,'radioModulatorFailAlarmSeverityCode':radioModulatorFailAlarmSeverityCode,'radioDemodulatorFailAlarmSeverityCode':radioDemodulatorFailAlarmSeverityCode,'radioRxPowerLowAlarmSeverityCode':radioRxPowerLowAlarmSeverityCode,'radioTxPowerLowAlarmSeverityCode':radioTxPowerLowAlarmSeverityCode,'radioVcoFailAlarmSeverityCode':radioVcoFailAlarmSeverityCode,'radioRxIFAgcAlarmSeverityCode':radioRxIFAgcAlarmSeverityCode,'radioTxIFAgcAlarmSeverityCode':radioTxIFAgcAlarmSeverityCode,'radioIduOduCommunicationAlarmSeverityCode':radioIduOduCommunicationAlarmSeverityCode,'radioOduIduCommunicationAlarmSeverityCode':radioOduIduCommunicationAlarmSeverityCode,'radioLocalOduAlarmSynthesisSeverityCode':radioLocalOduAlarmSynthesisSeverityCode,'radioRemoteOduAlarmSynthesisSeverityCode':radioRemoteOduAlarmSynthesisSeverityCode,'radioConfigMismatchAlarmSeverityCode':radioConfigMismatchAlarmSeverityCode,'radioPrxHysteresisValue':radioPrxHysteresisValue,'radioPtxHysteresisValue':radioPtxHysteresisValue,'radioPrxHysteresisValueTrapNotification':radioPrxHysteresisValueTrapNotification,'radioPtxHysteresisValueTrapNotification':radioPtxHysteresisValueTrapNotification,'radioRxQualityLowAlarmSeverityCode':radioRxQualityLowAlarmSeverityCode,'radioRxQualityWarningAlarmSeverityCode':radioRxQualityWarningAlarmSeverityCode,'linkReducedCapacityAlarmSeverityCode':linkReducedCapacityAlarmSeverityCode,'linkLinkTelemetryFailAlarmSeverityCode':linkLinkTelemetryFailAlarmSeverityCode,'linkIdMismatchAlarmSeverityCode':linkIdMismatchAlarmSeverityCode,'linkRadioEocAlarmSeverityCode':linkRadioEocAlarmSeverityCode,'linkSetupMismatchAlarmSeverityCode':linkSetupMismatchAlarmSeverityCode,'linkRescueSetupAlarmSeverityCode':linkRescueSetupAlarmSeverityCode,'linkXpicProcedureBlockAlarmSeverityCode':linkXpicProcedureBlockAlarmSeverityCode,'linkXpicRemTxOffAlarmAlarmSeverityCode':linkXpicRemTxOffAlarmAlarmSeverityCode,'linkLocalIduAlarmSynthesis':linkLocalIduAlarmSynthesis,'linkLocalIduAlarmSynthesisSeverityCode':linkLocalIduAlarmSynthesisSeverityCode,'linkRemoteIduAlarmSynthesisSeverityCode':linkRemoteIduAlarmSynthesisSeverityCode,'linkTfcAlarmSeverityCode':linkTfcAlarmSeverityCode,'linkBerSyncLossAlarmSeverityCode':linkBerSyncLossAlarmSeverityCode,'linkNotMatchingRadiosAlarmSeverityCode':linkNotMatchingRadiosAlarmSeverityCode,'channelSpacingSelection':channelSpacingSelection,'fadeMarginMeasure':fadeMarginMeasure,'linkConfigurationInProgressTrapNotification':linkConfigurationInProgressTrapNotification,'radioXpicAlarmSeverityCode':radioXpicAlarmSeverityCode})