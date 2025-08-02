_d='radioTotalEntry'
_c='wtnSnapshotEntry'
_b='wtnInfoEntry'
_a='wtnStatusEntry'
_Z='accessible-for-notify'
_Y='unused14'
_X='unused13'
_W='unused12'
_V='mcChannelFail'
_U='iduOduLinkFail'
_T='oduEquipFail'
_S='iduEquipFail'
_R='unused7'
_Q='unused6'
_P='unused5'
_O='rxEbnoAlarm'
_N='rxBerAlarm'
_M='oduTempAlert'
_L='iduOOL'
_K='rssiDeviation'
_J='wtnRadioIfIndex'
_I='serviceAffected'
_H='Bits'
_G='read-only'
_F='Integer32'
_E='wtnServiceAffected'
_D='wtnTrapCondition'
_C='read-write'
_B='ZHONE-PHY-WTN-RADIO-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_H,'Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp','TruthValue')
SkyZhoneRadioChannelNumber,SkyZhoneScientificNotation=mibBuilder.importSymbols('ZHONE-RADIO-TC-MIB','SkyZhoneRadioChannelNumber','SkyZhoneScientificNotation')
zhoneModules,zhoneRadio=mibBuilder.importSymbols('Zhone','zhoneModules','zhoneRadio')
ZhoneAdminString,=mibBuilder.importSymbols('Zhone-TC','ZhoneAdminString')
zhonePhyWtnRadio=ModuleIdentity((1,3,6,1,4,1,5504,6,106))
if mibBuilder.loadTexts:zhonePhyWtnRadio.setRevisions(('2001-07-11 13:00','2001-06-07 14:14','2001-05-18 10:02','2000-11-24 08:18','2000-11-21 15:35','2000-11-03 09:44'))
_WtnConfigTable_Object=MibTable
wtnConfigTable=_WtnConfigTable_Object((1,3,6,1,4,1,5504,5,8,1))
if mibBuilder.loadTexts:wtnConfigTable.setStatus(_A)
_WtnConfigEntry_Object=MibTableRow
wtnConfigEntry=_WtnConfigEntry_Object((1,3,6,1,4,1,5504,5,8,1,1))
wtnConfigEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:wtnConfigEntry.setStatus(_A)
_WtnRadioIfIndex_Type=InterfaceIndex
_WtnRadioIfIndex_Object=MibTableColumn
wtnRadioIfIndex=_WtnRadioIfIndex_Object((1,3,6,1,4,1,5504,5,8,1,1,1),_WtnRadioIfIndex_Type())
wtnRadioIfIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:wtnRadioIfIndex.setStatus(_A)
_WtnActiveChannelNumber_Type=SkyZhoneRadioChannelNumber
_WtnActiveChannelNumber_Object=MibTableColumn
wtnActiveChannelNumber=_WtnActiveChannelNumber_Object((1,3,6,1,4,1,5504,5,8,1,1,2),_WtnActiveChannelNumber_Type())
wtnActiveChannelNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:wtnActiveChannelNumber.setStatus(_A)
_WtnActiveTransmitFrequency_Type=SkyZhoneScientificNotation
_WtnActiveTransmitFrequency_Object=MibTableColumn
wtnActiveTransmitFrequency=_WtnActiveTransmitFrequency_Object((1,3,6,1,4,1,5504,5,8,1,1,3),_WtnActiveTransmitFrequency_Type())
wtnActiveTransmitFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:wtnActiveTransmitFrequency.setStatus(_A)
if mibBuilder.loadTexts:wtnActiveTransmitFrequency.setUnits('Hz')
_WtnStandbyChannelNumber_Type=SkyZhoneRadioChannelNumber
_WtnStandbyChannelNumber_Object=MibTableColumn
wtnStandbyChannelNumber=_WtnStandbyChannelNumber_Object((1,3,6,1,4,1,5504,5,8,1,1,4),_WtnStandbyChannelNumber_Type())
wtnStandbyChannelNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:wtnStandbyChannelNumber.setStatus(_A)
_WtnStandbyTransmitFrequency_Type=SkyZhoneScientificNotation
_WtnStandbyTransmitFrequency_Object=MibTableColumn
wtnStandbyTransmitFrequency=_WtnStandbyTransmitFrequency_Object((1,3,6,1,4,1,5504,5,8,1,1,5),_WtnStandbyTransmitFrequency_Type())
wtnStandbyTransmitFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:wtnStandbyTransmitFrequency.setStatus(_A)
if mibBuilder.loadTexts:wtnStandbyTransmitFrequency.setUnits('Hz')
_WtnAutoChannelSwitchEnable_Type=TruthValue
_WtnAutoChannelSwitchEnable_Object=MibTableColumn
wtnAutoChannelSwitchEnable=_WtnAutoChannelSwitchEnable_Object((1,3,6,1,4,1,5504,5,8,1,1,6),_WtnAutoChannelSwitchEnable_Type())
wtnAutoChannelSwitchEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:wtnAutoChannelSwitchEnable.setStatus(_A)
class _WtnChannelSeparation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('na',0),('s1232MHz',1),('s1200MHz',2),('s1008MHz',3)))
_WtnChannelSeparation_Type.__name__=_F
_WtnChannelSeparation_Object=MibTableColumn
wtnChannelSeparation=_WtnChannelSeparation_Object((1,3,6,1,4,1,5504,5,8,1,1,7),_WtnChannelSeparation_Type())
wtnChannelSeparation.setMaxAccess(_C)
if mibBuilder.loadTexts:wtnChannelSeparation.setStatus(_A)
_WtnRadioAmplifiersEnable_Type=TruthValue
_WtnRadioAmplifiersEnable_Object=MibTableColumn
wtnRadioAmplifiersEnable=_WtnRadioAmplifiersEnable_Object((1,3,6,1,4,1,5504,5,8,1,1,8),_WtnRadioAmplifiersEnable_Type())
wtnRadioAmplifiersEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:wtnRadioAmplifiersEnable.setStatus(_A)
_WtnRxBERThresh_Type=SkyZhoneScientificNotation
_WtnRxBERThresh_Object=MibTableColumn
wtnRxBERThresh=_WtnRxBERThresh_Object((1,3,6,1,4,1,5504,5,8,1,1,9),_WtnRxBERThresh_Type())
wtnRxBERThresh.setMaxAccess(_C)
if mibBuilder.loadTexts:wtnRxBERThresh.setStatus(_A)
_WtnRxBERHysteresisWindow_Type=SkyZhoneScientificNotation
_WtnRxBERHysteresisWindow_Object=MibTableColumn
wtnRxBERHysteresisWindow=_WtnRxBERHysteresisWindow_Object((1,3,6,1,4,1,5504,5,8,1,1,10),_WtnRxBERHysteresisWindow_Type())
wtnRxBERHysteresisWindow.setMaxAccess(_C)
if mibBuilder.loadTexts:wtnRxBERHysteresisWindow.setStatus(_A)
class _WtnAntennaSize_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,6)));namedValues=NamedValues(*(('oneFoot',1),('twoFeet',2),('fourFeet',4),('sixFeet',6)))
_WtnAntennaSize_Type.__name__=_F
_WtnAntennaSize_Object=MibTableColumn
wtnAntennaSize=_WtnAntennaSize_Object((1,3,6,1,4,1,5504,5,8,1,1,11),_WtnAntennaSize_Type())
wtnAntennaSize.setMaxAccess(_C)
if mibBuilder.loadTexts:wtnAntennaSize.setStatus(_A)
if mibBuilder.loadTexts:wtnAntennaSize.setUnits('feet')
class _WtnIduOduCableLength_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,300))
_WtnIduOduCableLength_Type.__name__=_F
_WtnIduOduCableLength_Object=MibTableColumn
wtnIduOduCableLength=_WtnIduOduCableLength_Object((1,3,6,1,4,1,5504,5,8,1,1,12),_WtnIduOduCableLength_Type())
wtnIduOduCableLength.setMaxAccess(_C)
if mibBuilder.loadTexts:wtnIduOduCableLength.setStatus(_A)
if mibBuilder.loadTexts:wtnIduOduCableLength.setUnits('feet')
class _WtnRssiThresh_Type(Integer32):defaultValue=-80;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-99,-30))
_WtnRssiThresh_Type.__name__=_F
_WtnRssiThresh_Object=MibTableColumn
wtnRssiThresh=_WtnRssiThresh_Object((1,3,6,1,4,1,5504,5,8,1,1,13),_WtnRssiThresh_Type())
wtnRssiThresh.setMaxAccess(_C)
if mibBuilder.loadTexts:wtnRssiThresh.setStatus(_A)
if mibBuilder.loadTexts:wtnRssiThresh.setUnits('dB')
class _WtnRssiHysteresisWindow_Type(Integer32):defaultValue=10
_WtnRssiHysteresisWindow_Type.__name__=_F
_WtnRssiHysteresisWindow_Object=MibTableColumn
wtnRssiHysteresisWindow=_WtnRssiHysteresisWindow_Object((1,3,6,1,4,1,5504,5,8,1,1,14),_WtnRssiHysteresisWindow_Type())
wtnRssiHysteresisWindow.setMaxAccess(_C)
if mibBuilder.loadTexts:wtnRssiHysteresisWindow.setStatus(_A)
if mibBuilder.loadTexts:wtnRssiHysteresisWindow.setUnits('dB')
_WtnTrapsEnable_Type=TruthValue
_WtnTrapsEnable_Object=MibTableColumn
wtnTrapsEnable=_WtnTrapsEnable_Object((1,3,6,1,4,1,5504,5,8,1,1,15),_WtnTrapsEnable_Type())
wtnTrapsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:wtnTrapsEnable.setStatus(_A)
class _WtnOduLoopback_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('loopbackOn',1),('loopbackOff',2)))
_WtnOduLoopback_Type.__name__=_F
_WtnOduLoopback_Object=MibTableColumn
wtnOduLoopback=_WtnOduLoopback_Object((1,3,6,1,4,1,5504,5,8,1,1,16),_WtnOduLoopback_Type())
wtnOduLoopback.setMaxAccess(_C)
if mibBuilder.loadTexts:wtnOduLoopback.setStatus(_A)
_WtnOduIdentifier_Type=SnmpAdminString
_WtnOduIdentifier_Object=MibTableColumn
wtnOduIdentifier=_WtnOduIdentifier_Object((1,3,6,1,4,1,5504,5,8,1,1,17),_WtnOduIdentifier_Type())
wtnOduIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:wtnOduIdentifier.setStatus(_A)
class _WtnTxLevel_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,45))
_WtnTxLevel_Type.__name__=_F
_WtnTxLevel_Object=MibTableColumn
wtnTxLevel=_WtnTxLevel_Object((1,3,6,1,4,1,5504,5,8,1,1,18),_WtnTxLevel_Type())
wtnTxLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:wtnTxLevel.setStatus(_A)
if mibBuilder.loadTexts:wtnTxLevel.setUnits('dB')
_WtnStatusTable_Object=MibTable
wtnStatusTable=_WtnStatusTable_Object((1,3,6,1,4,1,5504,5,8,2))
if mibBuilder.loadTexts:wtnStatusTable.setStatus(_A)
_WtnStatusEntry_Object=MibTableRow
wtnStatusEntry=_WtnStatusEntry_Object((1,3,6,1,4,1,5504,5,8,2,1))
if mibBuilder.loadTexts:wtnStatusEntry.setStatus(_A)
class _WtnCriticalAlarmStatus_Type(Bits):namedValues=NamedValues(*((_K,0),(_L,1),(_M,2),(_N,3),(_O,4),(_P,5),(_Q,6),(_R,7),(_S,8),(_T,9),(_U,10),(_V,11),(_W,12),(_X,13),(_Y,14),(_I,15)))
_WtnCriticalAlarmStatus_Type.__name__=_H
_WtnCriticalAlarmStatus_Object=MibTableColumn
wtnCriticalAlarmStatus=_WtnCriticalAlarmStatus_Object((1,3,6,1,4,1,5504,5,8,2,1,1),_WtnCriticalAlarmStatus_Type())
wtnCriticalAlarmStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:wtnCriticalAlarmStatus.setStatus(_A)
_WtnCriticalAlarmStatusLastChange_Type=TimeStamp
_WtnCriticalAlarmStatusLastChange_Object=MibTableColumn
wtnCriticalAlarmStatusLastChange=_WtnCriticalAlarmStatusLastChange_Object((1,3,6,1,4,1,5504,5,8,2,1,2),_WtnCriticalAlarmStatusLastChange_Type())
wtnCriticalAlarmStatusLastChange.setMaxAccess(_G)
if mibBuilder.loadTexts:wtnCriticalAlarmStatusLastChange.setStatus(_A)
class _WtnMinorAlarmStatus_Type(Bits):namedValues=NamedValues(*((_K,0),(_L,1),(_M,2),(_N,3),(_O,4),(_P,5),(_Q,6),(_R,7),(_S,8),(_T,9),(_U,10),(_V,11),(_W,12),(_X,13),(_Y,14),(_I,15)))
_WtnMinorAlarmStatus_Type.__name__=_H
_WtnMinorAlarmStatus_Object=MibTableColumn
wtnMinorAlarmStatus=_WtnMinorAlarmStatus_Object((1,3,6,1,4,1,5504,5,8,2,1,3),_WtnMinorAlarmStatus_Type())
wtnMinorAlarmStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:wtnMinorAlarmStatus.setStatus(_A)
_WtnMinorAlarmStatusLastChange_Type=TimeStamp
_WtnMinorAlarmStatusLastChange_Object=MibTableColumn
wtnMinorAlarmStatusLastChange=_WtnMinorAlarmStatusLastChange_Object((1,3,6,1,4,1,5504,5,8,2,1,4),_WtnMinorAlarmStatusLastChange_Type())
wtnMinorAlarmStatusLastChange.setMaxAccess(_G)
if mibBuilder.loadTexts:wtnMinorAlarmStatusLastChange.setStatus(_A)
_WtnOduTemperature_Type=Integer32
_WtnOduTemperature_Object=MibTableColumn
wtnOduTemperature=_WtnOduTemperature_Object((1,3,6,1,4,1,5504,5,8,2,1,5),_WtnOduTemperature_Type())
wtnOduTemperature.setMaxAccess(_G)
if mibBuilder.loadTexts:wtnOduTemperature.setStatus(_A)
_WtnReceiveFrequency_Type=SkyZhoneScientificNotation
_WtnReceiveFrequency_Object=MibTableColumn
wtnReceiveFrequency=_WtnReceiveFrequency_Object((1,3,6,1,4,1,5504,5,8,2,1,6),_WtnReceiveFrequency_Type())
wtnReceiveFrequency.setMaxAccess(_G)
if mibBuilder.loadTexts:wtnReceiveFrequency.setStatus(_A)
if mibBuilder.loadTexts:wtnReceiveFrequency.setUnits('Hz')
_WtnInfoTable_Object=MibTable
wtnInfoTable=_WtnInfoTable_Object((1,3,6,1,4,1,5504,5,8,3))
if mibBuilder.loadTexts:wtnInfoTable.setStatus(_A)
_WtnInfoEntry_Object=MibTableRow
wtnInfoEntry=_WtnInfoEntry_Object((1,3,6,1,4,1,5504,5,8,3,1))
if mibBuilder.loadTexts:wtnInfoEntry.setStatus(_A)
_WtnOduSerialNumber_Type=ZhoneAdminString
_WtnOduSerialNumber_Object=MibTableColumn
wtnOduSerialNumber=_WtnOduSerialNumber_Object((1,3,6,1,4,1,5504,5,8,3,1,1),_WtnOduSerialNumber_Type())
wtnOduSerialNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:wtnOduSerialNumber.setStatus(_A)
_WtnOduMfgCLEICode_Type=ZhoneAdminString
_WtnOduMfgCLEICode_Object=MibTableColumn
wtnOduMfgCLEICode=_WtnOduMfgCLEICode_Object((1,3,6,1,4,1,5504,5,8,3,1,2),_WtnOduMfgCLEICode_Type())
wtnOduMfgCLEICode.setMaxAccess(_G)
if mibBuilder.loadTexts:wtnOduMfgCLEICode.setStatus(_A)
_WtnSnapshotTable_Object=MibTable
wtnSnapshotTable=_WtnSnapshotTable_Object((1,3,6,1,4,1,5504,5,8,4))
if mibBuilder.loadTexts:wtnSnapshotTable.setStatus(_A)
_WtnSnapshotEntry_Object=MibTableRow
wtnSnapshotEntry=_WtnSnapshotEntry_Object((1,3,6,1,4,1,5504,5,8,4,1))
if mibBuilder.loadTexts:wtnSnapshotEntry.setStatus(_A)
class _WtnRSSI_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-90,0))
_WtnRSSI_Type.__name__=_F
_WtnRSSI_Object=MibTableColumn
wtnRSSI=_WtnRSSI_Object((1,3,6,1,4,1,5504,5,8,4,1,1),_WtnRSSI_Type())
wtnRSSI.setMaxAccess(_G)
if mibBuilder.loadTexts:wtnRSSI.setStatus(_A)
if mibBuilder.loadTexts:wtnRSSI.setUnits('dBm')
class _WtnTSSI_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,45))
_WtnTSSI_Type.__name__=_F
_WtnTSSI_Object=MibTableColumn
wtnTSSI=_WtnTSSI_Object((1,3,6,1,4,1,5504,5,8,4,1,2),_WtnTSSI_Type())
wtnTSSI.setMaxAccess(_G)
if mibBuilder.loadTexts:wtnTSSI.setStatus(_A)
if mibBuilder.loadTexts:wtnTSSI.setUnits('dBm')
_WtnRxBerFloat_Type=SkyZhoneScientificNotation
_WtnRxBerFloat_Object=MibTableColumn
wtnRxBerFloat=_WtnRxBerFloat_Object((1,3,6,1,4,1,5504,5,8,4,1,3),_WtnRxBerFloat_Type())
wtnRxBerFloat.setMaxAccess(_G)
if mibBuilder.loadTexts:wtnRxBerFloat.setStatus(_A)
_WtnRcvEbNoFloat_Type=SkyZhoneScientificNotation
_WtnRcvEbNoFloat_Object=MibTableColumn
wtnRcvEbNoFloat=_WtnRcvEbNoFloat_Object((1,3,6,1,4,1,5504,5,8,4,1,4),_WtnRcvEbNoFloat_Type())
wtnRcvEbNoFloat.setMaxAccess(_G)
if mibBuilder.loadTexts:wtnRcvEbNoFloat.setStatus(_A)
_WtnTrapData_ObjectIdentity=ObjectIdentity
wtnTrapData=_WtnTrapData_ObjectIdentity((1,3,6,1,4,1,5504,5,8,5))
_WtnTraps_ObjectIdentity=ObjectIdentity
wtnTraps=_WtnTraps_ObjectIdentity((1,3,6,1,4,1,5504,5,8,5,0))
class _WtnTrapCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('conditionPresent',1),('conditionCleared',2)))
_WtnTrapCondition_Type.__name__=_F
_WtnTrapCondition_Object=MibScalar
wtnTrapCondition=_WtnTrapCondition_Object((1,3,6,1,4,1,5504,5,8,5,1),_WtnTrapCondition_Type())
wtnTrapCondition.setMaxAccess(_Z)
if mibBuilder.loadTexts:wtnTrapCondition.setStatus(_A)
class _WtnServiceAffected_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),('serviceNotAffected',2)))
_WtnServiceAffected_Type.__name__=_F
_WtnServiceAffected_Object=MibScalar
wtnServiceAffected=_WtnServiceAffected_Object((1,3,6,1,4,1,5504,5,8,5,2),_WtnServiceAffected_Type())
wtnServiceAffected.setMaxAccess(_Z)
if mibBuilder.loadTexts:wtnServiceAffected.setStatus(_A)
_RadioTotalTable_Object=MibTable
radioTotalTable=_RadioTotalTable_Object((1,3,6,1,4,1,5504,5,8,6))
if mibBuilder.loadTexts:radioTotalTable.setStatus(_A)
_RadioTotalEntry_Object=MibTableRow
radioTotalEntry=_RadioTotalEntry_Object((1,3,6,1,4,1,5504,5,8,6,1))
if mibBuilder.loadTexts:radioTotalEntry.setStatus(_A)
_RadioTotalES_Type=Gauge32
_RadioTotalES_Object=MibTableColumn
radioTotalES=_RadioTotalES_Object((1,3,6,1,4,1,5504,5,8,6,1,1),_RadioTotalES_Type())
radioTotalES.setMaxAccess(_C)
if mibBuilder.loadTexts:radioTotalES.setStatus(_A)
_RadioTotalSES_Type=Gauge32
_RadioTotalSES_Object=MibTableColumn
radioTotalSES=_RadioTotalSES_Object((1,3,6,1,4,1,5504,5,8,6,1,2),_RadioTotalSES_Type())
radioTotalSES.setMaxAccess(_C)
if mibBuilder.loadTexts:radioTotalSES.setStatus(_A)
_RadioTotalUAS_Type=Gauge32
_RadioTotalUAS_Object=MibTableColumn
radioTotalUAS=_RadioTotalUAS_Object((1,3,6,1,4,1,5504,5,8,6,1,3),_RadioTotalUAS_Type())
radioTotalUAS.setMaxAccess(_C)
if mibBuilder.loadTexts:radioTotalUAS.setStatus(_A)
wtnConfigEntry.registerAugmentions((_B,_a))
wtnStatusEntry.setIndexNames(*wtnConfigEntry.getIndexNames())
wtnConfigEntry.registerAugmentions((_B,_b))
wtnInfoEntry.setIndexNames(*wtnConfigEntry.getIndexNames())
wtnConfigEntry.registerAugmentions((_B,_c))
wtnSnapshotEntry.setIndexNames(*wtnConfigEntry.getIndexNames())
wtnConfigEntry.registerAugmentions((_B,_d))
radioTotalEntry.setIndexNames(*wtnConfigEntry.getIndexNames())
wtnIduEquipFailCritical=NotificationType((1,3,6,1,4,1,5504,5,8,5,0,1))
wtnIduEquipFailCritical.setObjects(*((_B,_D),(_B,_E)))
if mibBuilder.loadTexts:wtnIduEquipFailCritical.setStatus(_A)
wtnIduEquipFail=NotificationType((1,3,6,1,4,1,5504,5,8,5,0,2))
wtnIduEquipFail.setObjects(*((_B,_D),(_B,_E)))
if mibBuilder.loadTexts:wtnIduEquipFail.setStatus(_A)
wtnIduOduLinkFailCritical=NotificationType((1,3,6,1,4,1,5504,5,8,5,0,3))
wtnIduOduLinkFailCritical.setObjects(*((_B,_D),(_B,_E)))
if mibBuilder.loadTexts:wtnIduOduLinkFailCritical.setStatus(_A)
wtnIduOduLinkFail=NotificationType((1,3,6,1,4,1,5504,5,8,5,0,4))
wtnIduOduLinkFail.setObjects(*((_B,_D),(_B,_E)))
if mibBuilder.loadTexts:wtnIduOduLinkFail.setStatus(_A)
wtnIduOutOfLockCritical=NotificationType((1,3,6,1,4,1,5504,5,8,5,0,5))
wtnIduOutOfLockCritical.setObjects(*((_B,_D),(_B,_E)))
if mibBuilder.loadTexts:wtnIduOutOfLockCritical.setStatus(_A)
wtnIduOutOfLock=NotificationType((1,3,6,1,4,1,5504,5,8,5,0,6))
wtnIduOutOfLock.setObjects(*((_B,_D),(_B,_E)))
if mibBuilder.loadTexts:wtnIduOutOfLock.setStatus(_A)
wtnMcChannelFailCritical=NotificationType((1,3,6,1,4,1,5504,5,8,5,0,7))
wtnMcChannelFailCritical.setObjects(*((_B,_D),(_B,_E)))
if mibBuilder.loadTexts:wtnMcChannelFailCritical.setStatus(_A)
wtnMcChannelFail=NotificationType((1,3,6,1,4,1,5504,5,8,5,0,8))
wtnMcChannelFail.setObjects(*((_B,_D),(_B,_E)))
if mibBuilder.loadTexts:wtnMcChannelFail.setStatus(_A)
wtnOduEquipFailCritical=NotificationType((1,3,6,1,4,1,5504,5,8,5,0,9))
wtnOduEquipFailCritical.setObjects(*((_B,_D),(_B,_E)))
if mibBuilder.loadTexts:wtnOduEquipFailCritical.setStatus(_A)
wtnOduEquipFail=NotificationType((1,3,6,1,4,1,5504,5,8,5,0,10))
wtnOduEquipFail.setObjects(*((_B,_D),(_B,_E)))
if mibBuilder.loadTexts:wtnOduEquipFail.setStatus(_A)
wtnOduTempAlertCritical=NotificationType((1,3,6,1,4,1,5504,5,8,5,0,11))
wtnOduTempAlertCritical.setObjects(*((_B,_D),(_B,_E)))
if mibBuilder.loadTexts:wtnOduTempAlertCritical.setStatus(_A)
wtnOduTempAlert=NotificationType((1,3,6,1,4,1,5504,5,8,5,0,12))
wtnOduTempAlert.setObjects(*((_B,_D),(_B,_E)))
if mibBuilder.loadTexts:wtnOduTempAlert.setStatus(_A)
wtnRSSIDeviation=NotificationType((1,3,6,1,4,1,5504,5,8,5,0,13))
wtnRSSIDeviation.setObjects(*((_B,_D),(_B,_E)))
if mibBuilder.loadTexts:wtnRSSIDeviation.setStatus(_A)
wtnBerAlarm=NotificationType((1,3,6,1,4,1,5504,5,8,5,0,14))
wtnBerAlarm.setObjects(*((_B,_D),(_B,_E)))
if mibBuilder.loadTexts:wtnBerAlarm.setStatus(_A)
wtnEbNoAlarm=NotificationType((1,3,6,1,4,1,5504,5,8,5,0,15))
wtnEbNoAlarm.setObjects(*((_B,_D),(_B,_E)))
if mibBuilder.loadTexts:wtnEbNoAlarm.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'wtnConfigTable':wtnConfigTable,'wtnConfigEntry':wtnConfigEntry,_J:wtnRadioIfIndex,'wtnActiveChannelNumber':wtnActiveChannelNumber,'wtnActiveTransmitFrequency':wtnActiveTransmitFrequency,'wtnStandbyChannelNumber':wtnStandbyChannelNumber,'wtnStandbyTransmitFrequency':wtnStandbyTransmitFrequency,'wtnAutoChannelSwitchEnable':wtnAutoChannelSwitchEnable,'wtnChannelSeparation':wtnChannelSeparation,'wtnRadioAmplifiersEnable':wtnRadioAmplifiersEnable,'wtnRxBERThresh':wtnRxBERThresh,'wtnRxBERHysteresisWindow':wtnRxBERHysteresisWindow,'wtnAntennaSize':wtnAntennaSize,'wtnIduOduCableLength':wtnIduOduCableLength,'wtnRssiThresh':wtnRssiThresh,'wtnRssiHysteresisWindow':wtnRssiHysteresisWindow,'wtnTrapsEnable':wtnTrapsEnable,'wtnOduLoopback':wtnOduLoopback,'wtnOduIdentifier':wtnOduIdentifier,'wtnTxLevel':wtnTxLevel,'wtnStatusTable':wtnStatusTable,_a:wtnStatusEntry,'wtnCriticalAlarmStatus':wtnCriticalAlarmStatus,'wtnCriticalAlarmStatusLastChange':wtnCriticalAlarmStatusLastChange,'wtnMinorAlarmStatus':wtnMinorAlarmStatus,'wtnMinorAlarmStatusLastChange':wtnMinorAlarmStatusLastChange,'wtnOduTemperature':wtnOduTemperature,'wtnReceiveFrequency':wtnReceiveFrequency,'wtnInfoTable':wtnInfoTable,_b:wtnInfoEntry,'wtnOduSerialNumber':wtnOduSerialNumber,'wtnOduMfgCLEICode':wtnOduMfgCLEICode,'wtnSnapshotTable':wtnSnapshotTable,_c:wtnSnapshotEntry,'wtnRSSI':wtnRSSI,'wtnTSSI':wtnTSSI,'wtnRxBerFloat':wtnRxBerFloat,'wtnRcvEbNoFloat':wtnRcvEbNoFloat,'wtnTrapData':wtnTrapData,'wtnTraps':wtnTraps,'wtnIduEquipFailCritical':wtnIduEquipFailCritical,'wtnIduEquipFail':wtnIduEquipFail,'wtnIduOduLinkFailCritical':wtnIduOduLinkFailCritical,'wtnIduOduLinkFail':wtnIduOduLinkFail,'wtnIduOutOfLockCritical':wtnIduOutOfLockCritical,'wtnIduOutOfLock':wtnIduOutOfLock,'wtnMcChannelFailCritical':wtnMcChannelFailCritical,'wtnMcChannelFail':wtnMcChannelFail,'wtnOduEquipFailCritical':wtnOduEquipFailCritical,'wtnOduEquipFail':wtnOduEquipFail,'wtnOduTempAlertCritical':wtnOduTempAlertCritical,'wtnOduTempAlert':wtnOduTempAlert,'wtnRSSIDeviation':wtnRSSIDeviation,'wtnBerAlarm':wtnBerAlarm,'wtnEbNoAlarm':wtnEbNoAlarm,_D:wtnTrapCondition,_E:wtnServiceAffected,'radioTotalTable':radioTotalTable,_d:radioTotalEntry,'radioTotalES':radioTotalES,'radioTotalSES':radioTotalSES,'radioTotalUAS':radioTotalUAS,'zhonePhyWtnRadio':zhonePhyWtnRadio})