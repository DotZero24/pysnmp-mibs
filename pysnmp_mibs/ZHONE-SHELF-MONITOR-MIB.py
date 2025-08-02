_AA='zhoneTrapFlashCardStatusChange'
_A9='zhoneTrapCardVersionCheck'
_A8='zhoneTrapCardStatusChange'
_A7='zhoneTrapShelfStatusChange'
_A6='zhoneCardLinkToBkplaneStatus'
_A5='cardReboot'
_A4='cardFaultResets'
_A3='cardAdminResets'
_A2='cardState'
_A1='cardFeatureBits'
_A0='cardCLEICode'
_z='cardSerialNumber'
_y='cardEepromVersion'
_x='cardLineType'
_w='cardSubType'
_v='cardType'
_u='shelfTemperatureStatus'
_t='shelfTemperatureLowThreshold'
_s='shelfTemperatureHighThreshold'
_r='shelfTemperatureLocation'
_q='shelfTemperature'
_p='shelfFanLowSpeedThreshold'
_o='shelfFanLocation'
_n='shelfFanSpeed'
_m='shelfPowerResets'
_l='shelfFaultResets'
_k='shelfAdminResets'
_j='shelfLedStatus'
_i='shelfCardStatus'
_h='shelfAlarmContactsStatus'
_g='shelfFanTrayStatus'
_f='shelfBPowerStatus'
_e='shelfAPowerStatus'
_d='shelfFeatureBits'
_c='shelfSlotCount'
_b='shelfFanTrayRevisionCode'
_a='shelfFanTraySerialNumber'
_Z='shelfBkplaneRevisionCode'
_Y='shelfBkplaneSerialNumber'
_X='shelfMonitorRevisionCode'
_W='shelfMonitorSerialNumber'
_V='shelfMfgCLEICode'
_U='accessible-for-notify'
_T='shelfTemperatureIndex'
_S='not-accessible'
_R='shelfFanIndex'
_Q='zhoneSlotIndex'
_P='cardVersion'
_O='zhoneFlashCardStatusChange'
_N='zhoneCardStatusLastChange'
_M='zhoneShelfStatusLastChange'
_L='zhoneCardStatus'
_K='zhoneShelfStatus'
_J='Bits'
_I='OctetString'
_H='powerNotOk'
_G='powerOk'
_F='zhoneShelfIndex'
_E='Zhone'
_D='Integer32'
_C='read-only'
_B='ZHONE-SHELF-MONITOR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_J,'Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp','TruthValue')
zhoneModules,zhoneShelf,zhoneShelfIndex,zhoneSlotIndex=mibBuilder.importSymbols(_E,'zhoneModules','zhoneShelf',_F,_Q)
ZhoneAdminString,ZhoneCardLineType,ZhoneCardType=mibBuilder.importSymbols('Zhone-TC','ZhoneAdminString','ZhoneCardLineType','ZhoneCardType')
zhoneShelfMonitorModule=ModuleIdentity((1,3,6,1,4,1,5504,6,7))
if mibBuilder.loadTexts:zhoneShelfMonitorModule.setRevisions(('2011-12-02 11:14','2011-05-24 10:25','2010-08-10 15:08','2006-08-31 10:58','2004-05-11 22:03','2003-10-28 15:31','2003-09-17 18:56','2003-07-16 16:30','2002-08-19 10:02','2002-07-09 10:36','2002-05-28 18:08','2002-02-12 09:54','2001-09-10 18:34','2001-09-10 16:16','2000-10-24 16:18','2000-10-13 16:42','2000-09-27 16:25','2000-09-12 11:26'))
_ShelfDataTable_Object=MibTable
shelfDataTable=_ShelfDataTable_Object((1,3,6,1,4,1,5504,3,2,1))
if mibBuilder.loadTexts:shelfDataTable.setStatus(_A)
_ShelfDataEntry_Object=MibTableRow
shelfDataEntry=_ShelfDataEntry_Object((1,3,6,1,4,1,5504,3,2,1,1))
shelfDataEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:shelfDataEntry.setStatus(_A)
_ShelfMfgCLEICode_Type=ZhoneAdminString
_ShelfMfgCLEICode_Object=MibTableColumn
shelfMfgCLEICode=_ShelfMfgCLEICode_Object((1,3,6,1,4,1,5504,3,2,1,1,1),_ShelfMfgCLEICode_Type())
shelfMfgCLEICode.setMaxAccess(_C)
if mibBuilder.loadTexts:shelfMfgCLEICode.setStatus(_A)
_ShelfMonitorSerialNumber_Type=ZhoneAdminString
_ShelfMonitorSerialNumber_Object=MibTableColumn
shelfMonitorSerialNumber=_ShelfMonitorSerialNumber_Object((1,3,6,1,4,1,5504,3,2,1,1,2),_ShelfMonitorSerialNumber_Type())
shelfMonitorSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:shelfMonitorSerialNumber.setStatus(_A)
_ShelfMonitorRevisionCode_Type=ZhoneAdminString
_ShelfMonitorRevisionCode_Object=MibTableColumn
shelfMonitorRevisionCode=_ShelfMonitorRevisionCode_Object((1,3,6,1,4,1,5504,3,2,1,1,3),_ShelfMonitorRevisionCode_Type())
shelfMonitorRevisionCode.setMaxAccess(_C)
if mibBuilder.loadTexts:shelfMonitorRevisionCode.setStatus(_A)
_ShelfBkplaneSerialNumber_Type=ZhoneAdminString
_ShelfBkplaneSerialNumber_Object=MibTableColumn
shelfBkplaneSerialNumber=_ShelfBkplaneSerialNumber_Object((1,3,6,1,4,1,5504,3,2,1,1,4),_ShelfBkplaneSerialNumber_Type())
shelfBkplaneSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:shelfBkplaneSerialNumber.setStatus(_A)
_ShelfBkplaneRevisionCode_Type=ZhoneAdminString
_ShelfBkplaneRevisionCode_Object=MibTableColumn
shelfBkplaneRevisionCode=_ShelfBkplaneRevisionCode_Object((1,3,6,1,4,1,5504,3,2,1,1,5),_ShelfBkplaneRevisionCode_Type())
shelfBkplaneRevisionCode.setMaxAccess(_C)
if mibBuilder.loadTexts:shelfBkplaneRevisionCode.setStatus(_A)
_ShelfFanTraySerialNumber_Type=ZhoneAdminString
_ShelfFanTraySerialNumber_Object=MibTableColumn
shelfFanTraySerialNumber=_ShelfFanTraySerialNumber_Object((1,3,6,1,4,1,5504,3,2,1,1,6),_ShelfFanTraySerialNumber_Type())
shelfFanTraySerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:shelfFanTraySerialNumber.setStatus(_A)
_ShelfFanTrayRevisionCode_Type=ZhoneAdminString
_ShelfFanTrayRevisionCode_Object=MibTableColumn
shelfFanTrayRevisionCode=_ShelfFanTrayRevisionCode_Object((1,3,6,1,4,1,5504,3,2,1,1,7),_ShelfFanTrayRevisionCode_Type())
shelfFanTrayRevisionCode.setMaxAccess(_C)
if mibBuilder.loadTexts:shelfFanTrayRevisionCode.setStatus(_A)
_ShelfSlotCount_Type=Integer32
_ShelfSlotCount_Object=MibTableColumn
shelfSlotCount=_ShelfSlotCount_Object((1,3,6,1,4,1,5504,3,2,1,1,8),_ShelfSlotCount_Type())
shelfSlotCount.setMaxAccess(_C)
if mibBuilder.loadTexts:shelfSlotCount.setStatus(_A)
class _ShelfFeatureBits_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ShelfFeatureBits_Type.__name__=_I
_ShelfFeatureBits_Object=MibTableColumn
shelfFeatureBits=_ShelfFeatureBits_Object((1,3,6,1,4,1,5504,3,2,1,1,9),_ShelfFeatureBits_Type())
shelfFeatureBits.setMaxAccess(_C)
if mibBuilder.loadTexts:shelfFeatureBits.setStatus(_A)
_ShelfFanTrayType_Type=ZhoneCardType
_ShelfFanTrayType_Object=MibTableColumn
shelfFanTrayType=_ShelfFanTrayType_Object((1,3,6,1,4,1,5504,3,2,1,1,10),_ShelfFanTrayType_Type())
shelfFanTrayType.setMaxAccess(_C)
if mibBuilder.loadTexts:shelfFanTrayType.setStatus(_A)
_ShelfIOAlarmBoardPresent_Type=TruthValue
_ShelfIOAlarmBoardPresent_Object=MibTableColumn
shelfIOAlarmBoardPresent=_ShelfIOAlarmBoardPresent_Object((1,3,6,1,4,1,5504,3,2,1,1,11),_ShelfIOAlarmBoardPresent_Type())
shelfIOAlarmBoardPresent.setMaxAccess(_C)
if mibBuilder.loadTexts:shelfIOAlarmBoardPresent.setStatus(_A)
_ShelfStatusTable_Object=MibTable
shelfStatusTable=_ShelfStatusTable_Object((1,3,6,1,4,1,5504,3,2,2))
if mibBuilder.loadTexts:shelfStatusTable.setStatus(_A)
_ShelfStatusEntry_Object=MibTableRow
shelfStatusEntry=_ShelfStatusEntry_Object((1,3,6,1,4,1,5504,3,2,2,1))
shelfStatusEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:shelfStatusEntry.setStatus(_A)
class _ShelfAPowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_ShelfAPowerStatus_Type.__name__=_D
_ShelfAPowerStatus_Object=MibTableColumn
shelfAPowerStatus=_ShelfAPowerStatus_Object((1,3,6,1,4,1,5504,3,2,2,1,1),_ShelfAPowerStatus_Type())
shelfAPowerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:shelfAPowerStatus.setStatus(_A)
class _ShelfBPowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_ShelfBPowerStatus_Type.__name__=_D
_ShelfBPowerStatus_Object=MibTableColumn
shelfBPowerStatus=_ShelfBPowerStatus_Object((1,3,6,1,4,1,5504,3,2,2,1,2),_ShelfBPowerStatus_Type())
shelfBPowerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:shelfBPowerStatus.setStatus(_A)
class _ShelfTemperatureStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('normal',1),('aboveNormal',2),('belowNormal',3)))
_ShelfTemperatureStatus_Type.__name__=_D
_ShelfTemperatureStatus_Object=MibTableColumn
shelfTemperatureStatus=_ShelfTemperatureStatus_Object((1,3,6,1,4,1,5504,3,2,2,1,3),_ShelfTemperatureStatus_Type())
shelfTemperatureStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:shelfTemperatureStatus.setStatus(_A)
class _ShelfFanTrayStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('operational',1),('partiallyOperational',2),('notOperational',3)))
_ShelfFanTrayStatus_Type.__name__=_D
_ShelfFanTrayStatus_Object=MibTableColumn
shelfFanTrayStatus=_ShelfFanTrayStatus_Object((1,3,6,1,4,1,5504,3,2,2,1,4),_ShelfFanTrayStatus_Type())
shelfFanTrayStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:shelfFanTrayStatus.setStatus(_A)
class _ShelfAlarmContactsStatus_Type(Bits):namedValues=NamedValues(*(('contactAlarm0',0),('contactAlarm1',1),('contactAlarm2',2),('contactAlarm3',3)))
_ShelfAlarmContactsStatus_Type.__name__=_J
_ShelfAlarmContactsStatus_Object=MibTableColumn
shelfAlarmContactsStatus=_ShelfAlarmContactsStatus_Object((1,3,6,1,4,1,5504,3,2,2,1,5),_ShelfAlarmContactsStatus_Type())
shelfAlarmContactsStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:shelfAlarmContactsStatus.setStatus(_A)
_ShelfCardStatus_Type=OctetString
_ShelfCardStatus_Object=MibTableColumn
shelfCardStatus=_ShelfCardStatus_Object((1,3,6,1,4,1,5504,3,2,2,1,6),_ShelfCardStatus_Type())
shelfCardStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:shelfCardStatus.setStatus(_A)
class _ShelfLedStatus_Type(Bits):namedValues=NamedValues(*(('battAPower',0),('battBPower',1),('fanAlarm',2),('minorAlarm',3),('majorAlarm',4),('criticalAlarm',5)))
_ShelfLedStatus_Type.__name__=_J
_ShelfLedStatus_Object=MibTableColumn
shelfLedStatus=_ShelfLedStatus_Object((1,3,6,1,4,1,5504,3,2,2,1,7),_ShelfLedStatus_Type())
shelfLedStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:shelfLedStatus.setStatus(_A)
_ShelfAdminResets_Type=Gauge32
_ShelfAdminResets_Object=MibTableColumn
shelfAdminResets=_ShelfAdminResets_Object((1,3,6,1,4,1,5504,3,2,2,1,8),_ShelfAdminResets_Type())
shelfAdminResets.setMaxAccess(_C)
if mibBuilder.loadTexts:shelfAdminResets.setStatus(_A)
_ShelfFaultResets_Type=Gauge32
_ShelfFaultResets_Object=MibTableColumn
shelfFaultResets=_ShelfFaultResets_Object((1,3,6,1,4,1,5504,3,2,2,1,9),_ShelfFaultResets_Type())
shelfFaultResets.setMaxAccess(_C)
if mibBuilder.loadTexts:shelfFaultResets.setStatus(_A)
_ShelfPowerResets_Type=Gauge32
_ShelfPowerResets_Object=MibTableColumn
shelfPowerResets=_ShelfPowerResets_Object((1,3,6,1,4,1,5504,3,2,2,1,10),_ShelfPowerResets_Type())
shelfPowerResets.setMaxAccess(_C)
if mibBuilder.loadTexts:shelfPowerResets.setStatus(_A)
class _ShelfCPowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_ShelfCPowerStatus_Type.__name__=_D
_ShelfCPowerStatus_Object=MibTableColumn
shelfCPowerStatus=_ShelfCPowerStatus_Object((1,3,6,1,4,1,5504,3,2,2,1,11),_ShelfCPowerStatus_Type())
shelfCPowerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:shelfCPowerStatus.setStatus(_A)
class _ShelfDPowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_ShelfDPowerStatus_Type.__name__=_D
_ShelfDPowerStatus_Object=MibTableColumn
shelfDPowerStatus=_ShelfDPowerStatus_Object((1,3,6,1,4,1,5504,3,2,2,1,12),_ShelfDPowerStatus_Type())
shelfDPowerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:shelfDPowerStatus.setStatus(_A)
_ShelfBatteryAVoltage_Type=ZhoneAdminString
_ShelfBatteryAVoltage_Object=MibTableColumn
shelfBatteryAVoltage=_ShelfBatteryAVoltage_Object((1,3,6,1,4,1,5504,3,2,2,1,13),_ShelfBatteryAVoltage_Type())
shelfBatteryAVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:shelfBatteryAVoltage.setStatus(_A)
_ShelfBatteryBVoltage_Type=ZhoneAdminString
_ShelfBatteryBVoltage_Object=MibTableColumn
shelfBatteryBVoltage=_ShelfBatteryBVoltage_Object((1,3,6,1,4,1,5504,3,2,2,1,14),_ShelfBatteryBVoltage_Type())
shelfBatteryBVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:shelfBatteryBVoltage.setStatus(_A)
_ShelfChassisReturnVoltage_Type=ZhoneAdminString
_ShelfChassisReturnVoltage_Object=MibTableColumn
shelfChassisReturnVoltage=_ShelfChassisReturnVoltage_Object((1,3,6,1,4,1,5504,3,2,2,1,15),_ShelfChassisReturnVoltage_Type())
shelfChassisReturnVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:shelfChassisReturnVoltage.setStatus(_A)
_ShelfFanTable_Object=MibTable
shelfFanTable=_ShelfFanTable_Object((1,3,6,1,4,1,5504,3,2,3))
if mibBuilder.loadTexts:shelfFanTable.setStatus(_A)
_ShelfFanEntry_Object=MibTableRow
shelfFanEntry=_ShelfFanEntry_Object((1,3,6,1,4,1,5504,3,2,3,1))
shelfFanEntry.setIndexNames((0,_E,_F),(0,_B,_R))
if mibBuilder.loadTexts:shelfFanEntry.setStatus(_A)
class _ShelfFanIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_ShelfFanIndex_Type.__name__=_D
_ShelfFanIndex_Object=MibTableColumn
shelfFanIndex=_ShelfFanIndex_Object((1,3,6,1,4,1,5504,3,2,3,1,1),_ShelfFanIndex_Type())
shelfFanIndex.setMaxAccess(_S)
if mibBuilder.loadTexts:shelfFanIndex.setStatus(_A)
_ShelfFanSpeed_Type=Integer32
_ShelfFanSpeed_Object=MibTableColumn
shelfFanSpeed=_ShelfFanSpeed_Object((1,3,6,1,4,1,5504,3,2,3,1,2),_ShelfFanSpeed_Type())
shelfFanSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:shelfFanSpeed.setStatus(_A)
_ShelfFanLocation_Type=ZhoneAdminString
_ShelfFanLocation_Object=MibTableColumn
shelfFanLocation=_ShelfFanLocation_Object((1,3,6,1,4,1,5504,3,2,3,1,3),_ShelfFanLocation_Type())
shelfFanLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:shelfFanLocation.setStatus(_A)
_ShelfFanLowSpeedThreshold_Type=Integer32
_ShelfFanLowSpeedThreshold_Object=MibTableColumn
shelfFanLowSpeedThreshold=_ShelfFanLowSpeedThreshold_Object((1,3,6,1,4,1,5504,3,2,3,1,4),_ShelfFanLowSpeedThreshold_Type())
shelfFanLowSpeedThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:shelfFanLowSpeedThreshold.setStatus(_A)
_ShelfTemperatureTable_Object=MibTable
shelfTemperatureTable=_ShelfTemperatureTable_Object((1,3,6,1,4,1,5504,3,2,4))
if mibBuilder.loadTexts:shelfTemperatureTable.setStatus(_A)
_ShelfTemperatureEntry_Object=MibTableRow
shelfTemperatureEntry=_ShelfTemperatureEntry_Object((1,3,6,1,4,1,5504,3,2,4,1))
shelfTemperatureEntry.setIndexNames((0,_E,_F),(0,_B,_T))
if mibBuilder.loadTexts:shelfTemperatureEntry.setStatus(_A)
class _ShelfTemperatureIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_ShelfTemperatureIndex_Type.__name__=_D
_ShelfTemperatureIndex_Object=MibTableColumn
shelfTemperatureIndex=_ShelfTemperatureIndex_Object((1,3,6,1,4,1,5504,3,2,4,1,1),_ShelfTemperatureIndex_Type())
shelfTemperatureIndex.setMaxAccess(_S)
if mibBuilder.loadTexts:shelfTemperatureIndex.setStatus(_A)
_ShelfTemperature_Type=Integer32
_ShelfTemperature_Object=MibTableColumn
shelfTemperature=_ShelfTemperature_Object((1,3,6,1,4,1,5504,3,2,4,1,2),_ShelfTemperature_Type())
shelfTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:shelfTemperature.setStatus(_A)
_ShelfTemperatureLocation_Type=ZhoneAdminString
_ShelfTemperatureLocation_Object=MibTableColumn
shelfTemperatureLocation=_ShelfTemperatureLocation_Object((1,3,6,1,4,1,5504,3,2,4,1,3),_ShelfTemperatureLocation_Type())
shelfTemperatureLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:shelfTemperatureLocation.setStatus(_A)
_ShelfTemperatureHighThreshold_Type=Integer32
_ShelfTemperatureHighThreshold_Object=MibTableColumn
shelfTemperatureHighThreshold=_ShelfTemperatureHighThreshold_Object((1,3,6,1,4,1,5504,3,2,4,1,4),_ShelfTemperatureHighThreshold_Type())
shelfTemperatureHighThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:shelfTemperatureHighThreshold.setStatus(_A)
_ShelfTemperatureLowThreshold_Type=Integer32
_ShelfTemperatureLowThreshold_Object=MibTableColumn
shelfTemperatureLowThreshold=_ShelfTemperatureLowThreshold_Object((1,3,6,1,4,1,5504,3,2,4,1,5),_ShelfTemperatureLowThreshold_Type())
shelfTemperatureLowThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:shelfTemperatureLowThreshold.setStatus(_A)
_ShelfCardTable_Object=MibTable
shelfCardTable=_ShelfCardTable_Object((1,3,6,1,4,1,5504,3,2,5))
if mibBuilder.loadTexts:shelfCardTable.setStatus(_A)
_ShelfCardEntry_Object=MibTableRow
shelfCardEntry=_ShelfCardEntry_Object((1,3,6,1,4,1,5504,3,2,5,1))
shelfCardEntry.setIndexNames((0,_E,_F),(0,_E,_Q))
if mibBuilder.loadTexts:shelfCardEntry.setStatus(_A)
_CardType_Type=ZhoneCardType
_CardType_Object=MibTableColumn
cardType=_CardType_Object((1,3,6,1,4,1,5504,3,2,5,1,1),_CardType_Type())
cardType.setMaxAccess(_C)
if mibBuilder.loadTexts:cardType.setStatus(_A)
_CardSubType_Type=ZhoneCardType
_CardSubType_Object=MibTableColumn
cardSubType=_CardSubType_Object((1,3,6,1,4,1,5504,3,2,5,1,2),_CardSubType_Type())
cardSubType.setMaxAccess(_C)
if mibBuilder.loadTexts:cardSubType.setStatus(_A)
_CardLineType_Type=ZhoneCardLineType
_CardLineType_Object=MibTableColumn
cardLineType=_CardLineType_Object((1,3,6,1,4,1,5504,3,2,5,1,3),_CardLineType_Type())
cardLineType.setMaxAccess(_C)
if mibBuilder.loadTexts:cardLineType.setStatus(_A)
_CardVersion_Type=ZhoneAdminString
_CardVersion_Object=MibTableColumn
cardVersion=_CardVersion_Object((1,3,6,1,4,1,5504,3,2,5,1,4),_CardVersion_Type())
cardVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:cardVersion.setStatus(_A)
_CardEepromVersion_Type=ZhoneAdminString
_CardEepromVersion_Object=MibTableColumn
cardEepromVersion=_CardEepromVersion_Object((1,3,6,1,4,1,5504,3,2,5,1,5),_CardEepromVersion_Type())
cardEepromVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:cardEepromVersion.setStatus(_A)
_CardSerialNumber_Type=ZhoneAdminString
_CardSerialNumber_Object=MibTableColumn
cardSerialNumber=_CardSerialNumber_Object((1,3,6,1,4,1,5504,3,2,5,1,6),_CardSerialNumber_Type())
cardSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cardSerialNumber.setStatus(_A)
_CardCLEICode_Type=ZhoneAdminString
_CardCLEICode_Object=MibTableColumn
cardCLEICode=_CardCLEICode_Object((1,3,6,1,4,1,5504,3,2,5,1,7),_CardCLEICode_Type())
cardCLEICode.setMaxAccess(_C)
if mibBuilder.loadTexts:cardCLEICode.setStatus(_A)
class _CardFeatureBits_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_CardFeatureBits_Type.__name__=_I
_CardFeatureBits_Object=MibTableColumn
cardFeatureBits=_CardFeatureBits_Object((1,3,6,1,4,1,5504,3,2,5,1,8),_CardFeatureBits_Type())
cardFeatureBits.setMaxAccess(_C)
if mibBuilder.loadTexts:cardFeatureBits.setStatus(_A)
class _CardState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('cardStateNone',0),('cardStateBooting',1),('cardStatePost',2),('cardStateLoading',3),('cardStateConfiguring',4),('cardStateRunning',5),('cardStateResetHold',6),('cardStateDumping',7),('cardStateFault',8),('cardStateReset',9),('cardNotPresent',10),('cardNotProvisioned',11)))
_CardState_Type.__name__=_D
_CardState_Object=MibTableColumn
cardState=_CardState_Object((1,3,6,1,4,1,5504,3,2,5,1,9),_CardState_Type())
cardState.setMaxAccess(_C)
if mibBuilder.loadTexts:cardState.setStatus(_A)
_CardAdminResets_Type=Gauge32
_CardAdminResets_Object=MibTableColumn
cardAdminResets=_CardAdminResets_Object((1,3,6,1,4,1,5504,3,2,5,1,10),_CardAdminResets_Type())
cardAdminResets.setMaxAccess(_C)
if mibBuilder.loadTexts:cardAdminResets.setStatus(_A)
_CardFaultResets_Type=Gauge32
_CardFaultResets_Object=MibTableColumn
cardFaultResets=_CardFaultResets_Object((1,3,6,1,4,1,5504,3,2,5,1,11),_CardFaultResets_Type())
cardFaultResets.setMaxAccess(_C)
if mibBuilder.loadTexts:cardFaultResets.setStatus(_A)
_CardReboot_Type=TruthValue
_CardReboot_Object=MibTableColumn
cardReboot=_CardReboot_Object((1,3,6,1,4,1,5504,3,2,5,1,12),_CardReboot_Type())
cardReboot.setMaxAccess('read-write')
if mibBuilder.loadTexts:cardReboot.setStatus(_A)
class _ZhoneShelfStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35)));namedValues=NamedValues(*(('leftOutletTempOverLimit',1),('leftOutletTempNormal',2),('rightOutletTempOverLimit',3),('rightOutletTempNormal',4),('powerSupplyAFailure',5),('powerSupplyAOK',6),('powerSupplyBFailure',7),('powerSupplyBOK',8),('fanSpeedError',9),('shelfControllerFault',10),('tempOverLimit',11),('tempUnderLimit',12),('tempNormal',13),('fanPowerSupplyAFailure',14),('fanPowerSupplyAOK',15),('fanPowerSupplyBFailure',16),('fanPowerSupplyBOK',17),('fanTrayAdded',18),('fanTrayRemoved',19),('fanSpeedOK',20),('fanAFailure',21),('fanAOK',22),('fanBFailure',23),('fanBOK',24),('fanPowerSupplyCFailure',25),('fanPowerSupplyCOK',26),('fanPowerSupplyDFailure',27),('fanPowerSupplyDOK',28),('shelfControllerCleared',29),('fanCFailure',30),('fanCOK',31),('fanDFailure',32),('fanDOK',33),('fanEFailure',34),('fanEOK',35)))
_ZhoneShelfStatus_Type.__name__=_D
_ZhoneShelfStatus_Object=MibScalar
zhoneShelfStatus=_ZhoneShelfStatus_Object((1,3,6,1,4,1,5504,3,2,7),_ZhoneShelfStatus_Type())
zhoneShelfStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneShelfStatus.setStatus(_A)
class _ZhoneCardStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('cardRemoved',1),('cardAdded',2),('cardTimeoutError',3),('cardFaultError',4),('cardReset',5),('cardRunning',6)))
_ZhoneCardStatus_Type.__name__=_D
_ZhoneCardStatus_Object=MibScalar
zhoneCardStatus=_ZhoneCardStatus_Object((1,3,6,1,4,1,5504,3,2,8),_ZhoneCardStatus_Type())
zhoneCardStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneCardStatus.setStatus(_A)
_ZhoneShelfStatusLastChange_Type=TimeStamp
_ZhoneShelfStatusLastChange_Object=MibScalar
zhoneShelfStatusLastChange=_ZhoneShelfStatusLastChange_Object((1,3,6,1,4,1,5504,3,2,10),_ZhoneShelfStatusLastChange_Type())
zhoneShelfStatusLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneShelfStatusLastChange.setStatus(_A)
_ZhoneCardStatusLastChange_Type=TimeStamp
_ZhoneCardStatusLastChange_Object=MibScalar
zhoneCardStatusLastChange=_ZhoneCardStatusLastChange_Object((1,3,6,1,4,1,5504,3,2,11),_ZhoneCardStatusLastChange_Type())
zhoneCardStatusLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneCardStatusLastChange.setStatus(_A)
_ZhoneTrapShelfMonitorV2Traps_ObjectIdentity=ObjectIdentity
zhoneTrapShelfMonitorV2Traps=_ZhoneTrapShelfMonitorV2Traps_ObjectIdentity((1,3,6,1,4,1,5504,3,2,12))
if mibBuilder.loadTexts:zhoneTrapShelfMonitorV2Traps.setStatus(_A)
class _ZhoneFlashCardStatusChange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('flashCardPort1Installed',1),('flashCardPort1Removed',2),('flashCardPort2Installed',3),('flashCardPort2Removed',4)))
_ZhoneFlashCardStatusChange_Type.__name__=_D
_ZhoneFlashCardStatusChange_Object=MibScalar
zhoneFlashCardStatusChange=_ZhoneFlashCardStatusChange_Object((1,3,6,1,4,1,5504,3,2,16),_ZhoneFlashCardStatusChange_Type())
zhoneFlashCardStatusChange.setMaxAccess(_U)
if mibBuilder.loadTexts:zhoneFlashCardStatusChange.setStatus(_A)
class _ZhoneCardLinkToBkplaneStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('cardToBkpLinkNotPresent',1),('cardToBkpLinkPresent',2)))
_ZhoneCardLinkToBkplaneStatus_Type.__name__=_D
_ZhoneCardLinkToBkplaneStatus_Object=MibScalar
zhoneCardLinkToBkplaneStatus=_ZhoneCardLinkToBkplaneStatus_Object((1,3,6,1,4,1,5504,3,2,17),_ZhoneCardLinkToBkplaneStatus_Type())
zhoneCardLinkToBkplaneStatus.setMaxAccess(_U)
if mibBuilder.loadTexts:zhoneCardLinkToBkplaneStatus.setStatus(_A)
zhoneShelfStatusGroup=ObjectGroup((1,3,6,1,4,1,5504,3,2,13))
zhoneShelfStatusGroup.setObjects(*((_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_O),(_B,_t),(_B,_u)))
if mibBuilder.loadTexts:zhoneShelfStatusGroup.setStatus(_A)
zhoneStatusLastChangeGroup=ObjectGroup((1,3,6,1,4,1,5504,3,2,14))
zhoneStatusLastChangeGroup.setObjects(*((_B,_M),(_B,_N)))
if mibBuilder.loadTexts:zhoneStatusLastChangeGroup.setStatus(_A)
zhoneCardStatusGroup=ObjectGroup((1,3,6,1,4,1,5504,3,2,15))
zhoneCardStatusGroup.setObjects(*((_B,_v),(_B,_w),(_B,_x),(_B,_P),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5)))
if mibBuilder.loadTexts:zhoneCardStatusGroup.setStatus(_A)
zhoneTrapShelfStatusChange=NotificationType((1,3,6,1,4,1,5504,3,2,12,2))
zhoneTrapShelfStatusChange.setObjects((_B,_K))
if mibBuilder.loadTexts:zhoneTrapShelfStatusChange.setStatus(_A)
zhoneTrapCardStatusChange=NotificationType((1,3,6,1,4,1,5504,3,2,12,3))
zhoneTrapCardStatusChange.setObjects((_B,_L))
if mibBuilder.loadTexts:zhoneTrapCardStatusChange.setStatus(_A)
zhoneTrapCardVersionCheck=NotificationType((1,3,6,1,4,1,5504,3,2,12,4))
zhoneTrapCardVersionCheck.setObjects((_B,_P))
if mibBuilder.loadTexts:zhoneTrapCardVersionCheck.setStatus(_A)
zhoneTrapFlashCardStatusChange=NotificationType((1,3,6,1,4,1,5504,3,2,12,5))
zhoneTrapFlashCardStatusChange.setObjects((_B,_O))
if mibBuilder.loadTexts:zhoneTrapFlashCardStatusChange.setStatus(_A)
zhoneTrapCardToBkplaneStatusChange=NotificationType((1,3,6,1,4,1,5504,3,2,12,6))
zhoneTrapCardToBkplaneStatusChange.setObjects((_B,_A6))
if mibBuilder.loadTexts:zhoneTrapCardToBkplaneStatusChange.setStatus(_A)
zhoneTrapShelfMonitorGroup=NotificationGroup((1,3,6,1,4,1,5504,3,2,12,1))
zhoneTrapShelfMonitorGroup.setObjects(*((_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA)))
if mibBuilder.loadTexts:zhoneTrapShelfMonitorGroup.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'shelfDataTable':shelfDataTable,'shelfDataEntry':shelfDataEntry,_V:shelfMfgCLEICode,_W:shelfMonitorSerialNumber,_X:shelfMonitorRevisionCode,_Y:shelfBkplaneSerialNumber,_Z:shelfBkplaneRevisionCode,_a:shelfFanTraySerialNumber,_b:shelfFanTrayRevisionCode,_c:shelfSlotCount,_d:shelfFeatureBits,'shelfFanTrayType':shelfFanTrayType,'shelfIOAlarmBoardPresent':shelfIOAlarmBoardPresent,'shelfStatusTable':shelfStatusTable,'shelfStatusEntry':shelfStatusEntry,_e:shelfAPowerStatus,_f:shelfBPowerStatus,_u:shelfTemperatureStatus,_g:shelfFanTrayStatus,_h:shelfAlarmContactsStatus,_i:shelfCardStatus,_j:shelfLedStatus,_k:shelfAdminResets,_l:shelfFaultResets,_m:shelfPowerResets,'shelfCPowerStatus':shelfCPowerStatus,'shelfDPowerStatus':shelfDPowerStatus,'shelfBatteryAVoltage':shelfBatteryAVoltage,'shelfBatteryBVoltage':shelfBatteryBVoltage,'shelfChassisReturnVoltage':shelfChassisReturnVoltage,'shelfFanTable':shelfFanTable,'shelfFanEntry':shelfFanEntry,_R:shelfFanIndex,_n:shelfFanSpeed,_o:shelfFanLocation,_p:shelfFanLowSpeedThreshold,'shelfTemperatureTable':shelfTemperatureTable,'shelfTemperatureEntry':shelfTemperatureEntry,_T:shelfTemperatureIndex,_q:shelfTemperature,_r:shelfTemperatureLocation,_s:shelfTemperatureHighThreshold,_t:shelfTemperatureLowThreshold,'shelfCardTable':shelfCardTable,'shelfCardEntry':shelfCardEntry,_v:cardType,_w:cardSubType,_x:cardLineType,_P:cardVersion,_y:cardEepromVersion,_z:cardSerialNumber,_A0:cardCLEICode,_A1:cardFeatureBits,_A2:cardState,_A3:cardAdminResets,_A4:cardFaultResets,_A5:cardReboot,_K:zhoneShelfStatus,_L:zhoneCardStatus,_M:zhoneShelfStatusLastChange,_N:zhoneCardStatusLastChange,'zhoneTrapShelfMonitorV2Traps':zhoneTrapShelfMonitorV2Traps,'zhoneTrapShelfMonitorGroup':zhoneTrapShelfMonitorGroup,_A7:zhoneTrapShelfStatusChange,_A8:zhoneTrapCardStatusChange,_A9:zhoneTrapCardVersionCheck,_AA:zhoneTrapFlashCardStatusChange,'zhoneTrapCardToBkplaneStatusChange':zhoneTrapCardToBkplaneStatusChange,'zhoneShelfStatusGroup':zhoneShelfStatusGroup,'zhoneStatusLastChangeGroup':zhoneStatusLastChangeGroup,'zhoneCardStatusGroup':zhoneCardStatusGroup,_O:zhoneFlashCardStatusChange,_A6:zhoneCardLinkToBkplaneStatus,'zhoneShelfMonitorModule':zhoneShelfMonitorModule})