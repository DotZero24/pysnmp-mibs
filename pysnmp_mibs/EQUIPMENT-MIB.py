_m='swExternalAlarmStackingMessage'
_l='swExternalAlarmMessage'
_k='swStackRoleChangeType'
_j='swStackTopologyType'
_i='swEquipPowerSavingPortIndex'
_h='normal'
_g='alarming'
_f='master'
_e='working'
_d='OctetString'
_c='accessible-for-notify'
_b='swExternalAlarmStackingChannel'
_a='swExternalAlarmStackingUnitIndex'
_Z='not-accessible'
_Y='read-create'
_X='swExternalAlarmChannel'
_W='stand-alone'
_V='swPowerStatus'
_U='swUnitMgmtMacAddr'
_T='auto'
_S='swFanID'
_R='swFanUnitIndex'
_Q='swTimeRangeMgmtRangeName'
_P='TIMERANGE-MIB'
_O='swTemperatureCurrent'
_N='swTemperSensorID'
_M='swPowerID'
_L='swPowerUnitIndex'
_K='swTemperatureUnitIndex'
_J='other'
_I='swUnitMgmtId'
_H='DisplayString'
_G='disabled'
_F='enabled'
_E='read-only'
_D='read-write'
_C='Integer32'
_B='EQUIPMENT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_d,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AgentNotifyLevel,dlink_common_mgmt=mibBuilder.importSymbols('DLINK-ID-REC-MIB','AgentNotifyLevel','dlink-common-mgmt')
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_H,'PhysAddress','RowStatus','TextualConvention','TruthValue')
swTimeRangeMgmtRangeName,=mibBuilder.importSymbols(_P,_Q)
swEquipmentMIB=ModuleIdentity((1,3,6,1,4,1,171,12,11))
class MacAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_SwEquipment_ObjectIdentity=ObjectIdentity
swEquipment=_SwEquipment_ObjectIdentity((1,3,6,1,4,1,171,12,11,1))
class _SwEquipmentCapacity_Type(Bits):namedValues=NamedValues(*(('fanCapable',0),('redundantPowerCapable',1),('tempteratureDetection',2),('stackingCapable',3),('chassisCapable',4)))
_SwEquipmentCapacity_Type.__name__='Bits'
_SwEquipmentCapacity_Object=MibScalar
swEquipmentCapacity=_SwEquipmentCapacity_Object((1,3,6,1,4,1,171,12,11,1,1),_SwEquipmentCapacity_Type())
swEquipmentCapacity.setMaxAccess(_E)
if mibBuilder.loadTexts:swEquipmentCapacity.setStatus(_A)
class _SwFanTrapState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_SwFanTrapState_Type.__name__=_C
_SwFanTrapState_Object=MibScalar
swFanTrapState=_SwFanTrapState_Object((1,3,6,1,4,1,171,12,11,1,4),_SwFanTrapState_Type())
swFanTrapState.setMaxAccess(_D)
if mibBuilder.loadTexts:swFanTrapState.setStatus(_A)
class _SwPowerTrapState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_SwPowerTrapState_Type.__name__=_C
_SwPowerTrapState_Object=MibScalar
swPowerTrapState=_SwPowerTrapState_Object((1,3,6,1,4,1,171,12,11,1,5),_SwPowerTrapState_Type())
swPowerTrapState.setMaxAccess(_D)
if mibBuilder.loadTexts:swPowerTrapState.setStatus(_A)
_SwPowerTable_Object=MibTable
swPowerTable=_SwPowerTable_Object((1,3,6,1,4,1,171,12,11,1,6))
if mibBuilder.loadTexts:swPowerTable.setStatus(_A)
_SwPowerEntry_Object=MibTableRow
swPowerEntry=_SwPowerEntry_Object((1,3,6,1,4,1,171,12,11,1,6,1))
swPowerEntry.setIndexNames((0,_B,_L),(0,_B,_M))
if mibBuilder.loadTexts:swPowerEntry.setStatus(_A)
class _SwPowerUnitIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwPowerUnitIndex_Type.__name__=_C
_SwPowerUnitIndex_Object=MibTableColumn
swPowerUnitIndex=_SwPowerUnitIndex_Object((1,3,6,1,4,1,171,12,11,1,6,1,1),_SwPowerUnitIndex_Type())
swPowerUnitIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:swPowerUnitIndex.setStatus(_A)
class _SwPowerID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwPowerID_Type.__name__=_C
_SwPowerID_Object=MibTableColumn
swPowerID=_SwPowerID_Object((1,3,6,1,4,1,171,12,11,1,6,1,2),_SwPowerID_Type())
swPowerID.setMaxAccess(_E)
if mibBuilder.loadTexts:swPowerID.setStatus(_A)
class _SwPowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_J,0),('lowVoltage',1),('overCurrent',2),(_e,3),('fail',4),('connect',5),('disconnect',6)))
_SwPowerStatus_Type.__name__=_C
_SwPowerStatus_Object=MibTableColumn
swPowerStatus=_SwPowerStatus_Object((1,3,6,1,4,1,171,12,11,1,6,1,3),_SwPowerStatus_Type())
swPowerStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:swPowerStatus.setStatus(_A)
_SwFanTable_Object=MibTable
swFanTable=_SwFanTable_Object((1,3,6,1,4,1,171,12,11,1,7))
if mibBuilder.loadTexts:swFanTable.setStatus(_A)
_SwFanEntry_Object=MibTableRow
swFanEntry=_SwFanEntry_Object((1,3,6,1,4,1,171,12,11,1,7,1))
swFanEntry.setIndexNames((0,_B,_R),(0,_B,_S))
if mibBuilder.loadTexts:swFanEntry.setStatus(_A)
class _SwFanUnitIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwFanUnitIndex_Type.__name__=_C
_SwFanUnitIndex_Object=MibTableColumn
swFanUnitIndex=_SwFanUnitIndex_Object((1,3,6,1,4,1,171,12,11,1,7,1,1),_SwFanUnitIndex_Type())
swFanUnitIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:swFanUnitIndex.setStatus(_A)
class _SwFanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwFanID_Type.__name__=_C
_SwFanID_Object=MibTableColumn
swFanID=_SwFanID_Object((1,3,6,1,4,1,171,12,11,1,7,1,2),_SwFanID_Type())
swFanID.setMaxAccess(_E)
if mibBuilder.loadTexts:swFanID.setStatus(_A)
class _SwFanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_J,0),(_e,1),('fail',2),('speed-0',3),('speed-low',4),('speed-middle',5),('speed-high',6)))
_SwFanStatus_Type.__name__=_C
_SwFanStatus_Object=MibTableColumn
swFanStatus=_SwFanStatus_Object((1,3,6,1,4,1,171,12,11,1,7,1,3),_SwFanStatus_Type())
swFanStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:swFanStatus.setStatus(_A)
class _SwFanPostion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_J,1),('left',2),('right',3),('back',4),('cpu',5)))
_SwFanPostion_Type.__name__=_C
_SwFanPostion_Object=MibTableColumn
swFanPostion=_SwFanPostion_Object((1,3,6,1,4,1,171,12,11,1,7,1,4),_SwFanPostion_Type())
swFanPostion.setMaxAccess(_E)
if mibBuilder.loadTexts:swFanPostion.setStatus(_A)
class _SwFanNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwFanNumber_Type.__name__=_C
_SwFanNumber_Object=MibTableColumn
swFanNumber=_SwFanNumber_Object((1,3,6,1,4,1,171,12,11,1,7,1,5),_SwFanNumber_Type())
swFanNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:swFanNumber.setStatus(_A)
class _SwFanSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwFanSpeed_Type.__name__=_C
_SwFanSpeed_Object=MibTableColumn
swFanSpeed=_SwFanSpeed_Object((1,3,6,1,4,1,171,12,11,1,7,1,6),_SwFanSpeed_Type())
swFanSpeed.setMaxAccess(_E)
if mibBuilder.loadTexts:swFanSpeed.setStatus(_A)
_SwTemperatureTable_Object=MibTable
swTemperatureTable=_SwTemperatureTable_Object((1,3,6,1,4,1,171,12,11,1,8))
if mibBuilder.loadTexts:swTemperatureTable.setStatus(_A)
_SwTemperatureEntry_Object=MibTableRow
swTemperatureEntry=_SwTemperatureEntry_Object((1,3,6,1,4,1,171,12,11,1,8,1))
swTemperatureEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:swTemperatureEntry.setStatus(_A)
class _SwTemperatureUnitIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwTemperatureUnitIndex_Type.__name__=_C
_SwTemperatureUnitIndex_Object=MibTableColumn
swTemperatureUnitIndex=_SwTemperatureUnitIndex_Object((1,3,6,1,4,1,171,12,11,1,8,1,1),_SwTemperatureUnitIndex_Type())
swTemperatureUnitIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:swTemperatureUnitIndex.setStatus(_A)
class _SwTemperatureCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-500,500))
_SwTemperatureCurrent_Type.__name__=_C
_SwTemperatureCurrent_Object=MibTableColumn
swTemperatureCurrent=_SwTemperatureCurrent_Object((1,3,6,1,4,1,171,12,11,1,8,1,2),_SwTemperatureCurrent_Type())
swTemperatureCurrent.setMaxAccess(_E)
if mibBuilder.loadTexts:swTemperatureCurrent.setStatus(_A)
class _SwTemperatureHighThresh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-500,500))
_SwTemperatureHighThresh_Type.__name__=_C
_SwTemperatureHighThresh_Object=MibTableColumn
swTemperatureHighThresh=_SwTemperatureHighThresh_Object((1,3,6,1,4,1,171,12,11,1,8,1,3),_SwTemperatureHighThresh_Type())
swTemperatureHighThresh.setMaxAccess(_D)
if mibBuilder.loadTexts:swTemperatureHighThresh.setStatus(_A)
class _SwTemperatureLowThresh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-500,500))
_SwTemperatureLowThresh_Type.__name__=_C
_SwTemperatureLowThresh_Object=MibTableColumn
swTemperatureLowThresh=_SwTemperatureLowThresh_Object((1,3,6,1,4,1,171,12,11,1,8,1,4),_SwTemperatureLowThresh_Type())
swTemperatureLowThresh.setMaxAccess(_D)
if mibBuilder.loadTexts:swTemperatureLowThresh.setStatus(_A)
_SwUnitMgmt_ObjectIdentity=ObjectIdentity
swUnitMgmt=_SwUnitMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,11,1,9))
class _SwUnitStackingVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwUnitStackingVersion_Type.__name__=_C
_SwUnitStackingVersion_Object=MibScalar
swUnitStackingVersion=_SwUnitStackingVersion_Object((1,3,6,1,4,1,171,12,11,1,9,1),_SwUnitStackingVersion_Type())
swUnitStackingVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:swUnitStackingVersion.setStatus(_A)
class _SwUnitMaxSupportedUnits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwUnitMaxSupportedUnits_Type.__name__=_C
_SwUnitMaxSupportedUnits_Object=MibScalar
swUnitMaxSupportedUnits=_SwUnitMaxSupportedUnits_Object((1,3,6,1,4,1,171,12,11,1,9,2),_SwUnitMaxSupportedUnits_Type())
swUnitMaxSupportedUnits.setMaxAccess(_E)
if mibBuilder.loadTexts:swUnitMaxSupportedUnits.setStatus(_A)
class _SwUnitNumOfUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwUnitNumOfUnit_Type.__name__=_C
_SwUnitNumOfUnit_Object=MibScalar
swUnitNumOfUnit=_SwUnitNumOfUnit_Object((1,3,6,1,4,1,171,12,11,1,9,3),_SwUnitNumOfUnit_Type())
swUnitNumOfUnit.setMaxAccess(_E)
if mibBuilder.loadTexts:swUnitNumOfUnit.setStatus(_A)
_SwUnitMgmtTable_Object=MibTable
swUnitMgmtTable=_SwUnitMgmtTable_Object((1,3,6,1,4,1,171,12,11,1,9,4))
if mibBuilder.loadTexts:swUnitMgmtTable.setStatus(_A)
_SwUnitMgmtEntry_Object=MibTableRow
swUnitMgmtEntry=_SwUnitMgmtEntry_Object((1,3,6,1,4,1,171,12,11,1,9,4,1))
swUnitMgmtEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:swUnitMgmtEntry.setStatus(_A)
class _SwUnitMgmtId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,13))
_SwUnitMgmtId_Type.__name__=_C
_SwUnitMgmtId_Object=MibTableColumn
swUnitMgmtId=_SwUnitMgmtId_Object((1,3,6,1,4,1,171,12,11,1,9,4,1,1),_SwUnitMgmtId_Type())
swUnitMgmtId.setMaxAccess(_E)
if mibBuilder.loadTexts:swUnitMgmtId.setStatus(_A)
_SwUnitMgmtMacAddr_Type=MacAddress
_SwUnitMgmtMacAddr_Object=MibTableColumn
swUnitMgmtMacAddr=_SwUnitMgmtMacAddr_Object((1,3,6,1,4,1,171,12,11,1,9,4,1,2),_SwUnitMgmtMacAddr_Type())
swUnitMgmtMacAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:swUnitMgmtMacAddr.setStatus(_A)
class _SwUnitMgmtStartPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwUnitMgmtStartPort_Type.__name__=_C
_SwUnitMgmtStartPort_Object=MibTableColumn
swUnitMgmtStartPort=_SwUnitMgmtStartPort_Object((1,3,6,1,4,1,171,12,11,1,9,4,1,3),_SwUnitMgmtStartPort_Type())
swUnitMgmtStartPort.setMaxAccess(_E)
if mibBuilder.loadTexts:swUnitMgmtStartPort.setStatus(_A)
class _SwUnitMgmtPortRange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwUnitMgmtPortRange_Type.__name__=_C
_SwUnitMgmtPortRange_Object=MibTableColumn
swUnitMgmtPortRange=_SwUnitMgmtPortRange_Object((1,3,6,1,4,1,171,12,11,1,9,4,1,4),_SwUnitMgmtPortRange_Type())
swUnitMgmtPortRange.setMaxAccess(_E)
if mibBuilder.loadTexts:swUnitMgmtPortRange.setStatus(_A)
class _SwUnitMgmtFrontPanelLedStatus_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SwUnitMgmtFrontPanelLedStatus_Type.__name__=_d
_SwUnitMgmtFrontPanelLedStatus_Object=MibTableColumn
swUnitMgmtFrontPanelLedStatus=_SwUnitMgmtFrontPanelLedStatus_Object((1,3,6,1,4,1,171,12,11,1,9,4,1,5),_SwUnitMgmtFrontPanelLedStatus_Type())
swUnitMgmtFrontPanelLedStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:swUnitMgmtFrontPanelLedStatus.setStatus(_A)
class _SwUnitMgmtCtrlMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_J,1),(_T,2),(_W,3),(_f,4),('slave',5)))
_SwUnitMgmtCtrlMode_Type.__name__=_C
_SwUnitMgmtCtrlMode_Object=MibTableColumn
swUnitMgmtCtrlMode=_SwUnitMgmtCtrlMode_Object((1,3,6,1,4,1,171,12,11,1,9,4,1,6),_SwUnitMgmtCtrlMode_Type())
swUnitMgmtCtrlMode.setMaxAccess(_D)
if mibBuilder.loadTexts:swUnitMgmtCtrlMode.setStatus(_A)
class _SwUnitMgmtCurrentMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_J,1),(_T,2),(_W,3),(_f,4),('slave',5),('backup-master',6)))
_SwUnitMgmtCurrentMode_Type.__name__=_C
_SwUnitMgmtCurrentMode_Object=MibTableColumn
swUnitMgmtCurrentMode=_SwUnitMgmtCurrentMode_Object((1,3,6,1,4,1,171,12,11,1,9,4,1,7),_SwUnitMgmtCurrentMode_Type())
swUnitMgmtCurrentMode.setMaxAccess(_E)
if mibBuilder.loadTexts:swUnitMgmtCurrentMode.setStatus(_A)
class _SwUnitMgmtVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SwUnitMgmtVersion_Type.__name__=_H
_SwUnitMgmtVersion_Object=MibTableColumn
swUnitMgmtVersion=_SwUnitMgmtVersion_Object((1,3,6,1,4,1,171,12,11,1,9,4,1,8),_SwUnitMgmtVersion_Type())
swUnitMgmtVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:swUnitMgmtVersion.setStatus(_A)
class _SwUnitMgmtModuleName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SwUnitMgmtModuleName_Type.__name__=_H
_SwUnitMgmtModuleName_Object=MibTableColumn
swUnitMgmtModuleName=_SwUnitMgmtModuleName_Object((1,3,6,1,4,1,171,12,11,1,9,4,1,9),_SwUnitMgmtModuleName_Type())
swUnitMgmtModuleName.setMaxAccess(_E)
if mibBuilder.loadTexts:swUnitMgmtModuleName.setStatus(_A)
class _SwUnitMgmtPromVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SwUnitMgmtPromVersion_Type.__name__=_H
_SwUnitMgmtPromVersion_Object=MibTableColumn
swUnitMgmtPromVersion=_SwUnitMgmtPromVersion_Object((1,3,6,1,4,1,171,12,11,1,9,4,1,10),_SwUnitMgmtPromVersion_Type())
swUnitMgmtPromVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:swUnitMgmtPromVersion.setStatus(_A)
class _SwUnitMgmtFirmwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SwUnitMgmtFirmwareVersion_Type.__name__=_H
_SwUnitMgmtFirmwareVersion_Object=MibTableColumn
swUnitMgmtFirmwareVersion=_SwUnitMgmtFirmwareVersion_Object((1,3,6,1,4,1,171,12,11,1,9,4,1,11),_SwUnitMgmtFirmwareVersion_Type())
swUnitMgmtFirmwareVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:swUnitMgmtFirmwareVersion.setStatus(_A)
class _SwUnitMgmtHardwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SwUnitMgmtHardwareVersion_Type.__name__=_H
_SwUnitMgmtHardwareVersion_Object=MibTableColumn
swUnitMgmtHardwareVersion=_SwUnitMgmtHardwareVersion_Object((1,3,6,1,4,1,171,12,11,1,9,4,1,12),_SwUnitMgmtHardwareVersion_Type())
swUnitMgmtHardwareVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:swUnitMgmtHardwareVersion.setStatus(_A)
class _SwUnitMgmtPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,63))
_SwUnitMgmtPriority_Type.__name__=_C
_SwUnitMgmtPriority_Object=MibTableColumn
swUnitMgmtPriority=_SwUnitMgmtPriority_Object((1,3,6,1,4,1,171,12,11,1,9,4,1,13),_SwUnitMgmtPriority_Type())
swUnitMgmtPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:swUnitMgmtPriority.setStatus(_A)
class _SwUnitMgmtUserSetState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_T,2),('user',3)))
_SwUnitMgmtUserSetState_Type.__name__=_C
_SwUnitMgmtUserSetState_Object=MibTableColumn
swUnitMgmtUserSetState=_SwUnitMgmtUserSetState_Object((1,3,6,1,4,1,171,12,11,1,9,4,1,14),_SwUnitMgmtUserSetState_Type())
swUnitMgmtUserSetState.setMaxAccess(_E)
if mibBuilder.loadTexts:swUnitMgmtUserSetState.setStatus(_A)
class _SwUnitMgmtExistState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('exist',1),('no-exist',2)))
_SwUnitMgmtExistState_Type.__name__=_C
_SwUnitMgmtExistState_Object=MibTableColumn
swUnitMgmtExistState=_SwUnitMgmtExistState_Object((1,3,6,1,4,1,171,12,11,1,9,4,1,15),_SwUnitMgmtExistState_Type())
swUnitMgmtExistState.setMaxAccess(_E)
if mibBuilder.loadTexts:swUnitMgmtExistState.setStatus(_A)
class _SwUnitMgmtBoxId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*(('box-1',1),('box-2',2),('box-3',3),('box-4',4),('box-5',5),('box-6',6),('box-7',7),('box-8',8),('box-9',9),('box-10',10),('box-11',11),('box-12',12),(_T,13)))
_SwUnitMgmtBoxId_Type.__name__=_C
_SwUnitMgmtBoxId_Object=MibTableColumn
swUnitMgmtBoxId=_SwUnitMgmtBoxId_Object((1,3,6,1,4,1,171,12,11,1,9,4,1,16),_SwUnitMgmtBoxId_Type())
swUnitMgmtBoxId.setMaxAccess(_D)
if mibBuilder.loadTexts:swUnitMgmtBoxId.setStatus(_A)
_SwUnitMgmtSerialNumber_Type=DisplayString
_SwUnitMgmtSerialNumber_Object=MibTableColumn
swUnitMgmtSerialNumber=_SwUnitMgmtSerialNumber_Object((1,3,6,1,4,1,171,12,11,1,9,4,1,17),_SwUnitMgmtSerialNumber_Type())
swUnitMgmtSerialNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:swUnitMgmtSerialNumber.setStatus(_A)
class _SwUnitTopology_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_W,1),('duplex-chain',2),('duplex-ring',3),('star',4),('unstable',5)))
_SwUnitTopology_Type.__name__=_C
_SwUnitTopology_Object=MibScalar
swUnitTopology=_SwUnitTopology_Object((1,3,6,1,4,1,171,12,11,1,9,5),_SwUnitTopology_Type())
swUnitTopology.setMaxAccess(_E)
if mibBuilder.loadTexts:swUnitTopology.setStatus(_A)
class _SwUnitStackMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_SwUnitStackMode_Type.__name__=_C
_SwUnitStackMode_Object=MibScalar
swUnitStackMode=_SwUnitStackMode_Object((1,3,6,1,4,1,171,12,11,1,9,6),_SwUnitStackMode_Type())
swUnitStackMode.setMaxAccess(_D)
if mibBuilder.loadTexts:swUnitStackMode.setStatus(_A)
class _SwUnitStackForceMasterRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_SwUnitStackForceMasterRole_Type.__name__=_C
_SwUnitStackForceMasterRole_Object=MibScalar
swUnitStackForceMasterRole=_SwUnitStackForceMasterRole_Object((1,3,6,1,4,1,171,12,11,1,9,7),_SwUnitStackForceMasterRole_Type())
swUnitStackForceMasterRole.setMaxAccess(_D)
if mibBuilder.loadTexts:swUnitStackForceMasterRole.setStatus(_A)
class _SwUnitStackTrapState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_SwUnitStackTrapState_Type.__name__=_C
_SwUnitStackTrapState_Object=MibScalar
swUnitStackTrapState=_SwUnitStackTrapState_Object((1,3,6,1,4,1,171,12,11,1,9,8),_SwUnitStackTrapState_Type())
swUnitStackTrapState.setMaxAccess(_D)
if mibBuilder.loadTexts:swUnitStackTrapState.setStatus(_A)
class _SwUnitStackLogState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_SwUnitStackLogState_Type.__name__=_C
_SwUnitStackLogState_Object=MibScalar
swUnitStackLogState=_SwUnitStackLogState_Object((1,3,6,1,4,1,171,12,11,1,9,9),_SwUnitStackLogState_Type())
swUnitStackLogState.setMaxAccess(_D)
if mibBuilder.loadTexts:swUnitStackLogState.setStatus(_A)
_SwExternalAlarmTable_Object=MibTable
swExternalAlarmTable=_SwExternalAlarmTable_Object((1,3,6,1,4,1,171,12,11,1,10))
if mibBuilder.loadTexts:swExternalAlarmTable.setStatus(_A)
_SwExternalAlarmEntry_Object=MibTableRow
swExternalAlarmEntry=_SwExternalAlarmEntry_Object((1,3,6,1,4,1,171,12,11,1,10,1))
swExternalAlarmEntry.setIndexNames((0,_B,_X))
if mibBuilder.loadTexts:swExternalAlarmEntry.setStatus(_A)
_SwExternalAlarmChannel_Type=Integer32
_SwExternalAlarmChannel_Object=MibTableColumn
swExternalAlarmChannel=_SwExternalAlarmChannel_Object((1,3,6,1,4,1,171,12,11,1,10,1,1),_SwExternalAlarmChannel_Type())
swExternalAlarmChannel.setMaxAccess(_E)
if mibBuilder.loadTexts:swExternalAlarmChannel.setStatus(_A)
class _SwExternalAlarmMessage_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_SwExternalAlarmMessage_Type.__name__=_H
_SwExternalAlarmMessage_Object=MibTableColumn
swExternalAlarmMessage=_SwExternalAlarmMessage_Object((1,3,6,1,4,1,171,12,11,1,10,1,2),_SwExternalAlarmMessage_Type())
swExternalAlarmMessage.setMaxAccess(_D)
if mibBuilder.loadTexts:swExternalAlarmMessage.setStatus(_A)
class _SwExternalAlarmStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_g,1),(_h,2)))
_SwExternalAlarmStatus_Type.__name__=_C
_SwExternalAlarmStatus_Object=MibTableColumn
swExternalAlarmStatus=_SwExternalAlarmStatus_Object((1,3,6,1,4,1,171,12,11,1,10,1,3),_SwExternalAlarmStatus_Type())
swExternalAlarmStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:swExternalAlarmStatus.setStatus(_A)
_SwEquipmentPowerSaving_ObjectIdentity=ObjectIdentity
swEquipmentPowerSaving=_SwEquipmentPowerSaving_ObjectIdentity((1,3,6,1,4,1,171,12,11,1,11))
class _SwEquipPowerSavingLinkDetectState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_SwEquipPowerSavingLinkDetectState_Type.__name__=_C
_SwEquipPowerSavingLinkDetectState_Object=MibScalar
swEquipPowerSavingLinkDetectState=_SwEquipPowerSavingLinkDetectState_Object((1,3,6,1,4,1,171,12,11,1,11,1),_SwEquipPowerSavingLinkDetectState_Type())
swEquipPowerSavingLinkDetectState.setMaxAccess(_D)
if mibBuilder.loadTexts:swEquipPowerSavingLinkDetectState.setStatus(_A)
class _SwEquipPowerSavingLenDetect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_SwEquipPowerSavingLenDetect_Type.__name__=_C
_SwEquipPowerSavingLenDetect_Object=MibScalar
swEquipPowerSavingLenDetect=_SwEquipPowerSavingLenDetect_Object((1,3,6,1,4,1,171,12,11,1,11,2),_SwEquipPowerSavingLenDetect_Type())
swEquipPowerSavingLenDetect.setMaxAccess(_D)
if mibBuilder.loadTexts:swEquipPowerSavingLenDetect.setStatus(_A)
class _SwEquipPowerSavingHiberState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_SwEquipPowerSavingHiberState_Type.__name__=_C
_SwEquipPowerSavingHiberState_Object=MibScalar
swEquipPowerSavingHiberState=_SwEquipPowerSavingHiberState_Object((1,3,6,1,4,1,171,12,11,1,11,3),_SwEquipPowerSavingHiberState_Type())
swEquipPowerSavingHiberState.setMaxAccess(_D)
if mibBuilder.loadTexts:swEquipPowerSavingHiberState.setStatus(_A)
class _SwEquipPowerSavingPortLEDState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_SwEquipPowerSavingPortLEDState_Type.__name__=_C
_SwEquipPowerSavingPortLEDState_Object=MibScalar
swEquipPowerSavingPortLEDState=_SwEquipPowerSavingPortLEDState_Object((1,3,6,1,4,1,171,12,11,1,11,4),_SwEquipPowerSavingPortLEDState_Type())
swEquipPowerSavingPortLEDState.setMaxAccess(_D)
if mibBuilder.loadTexts:swEquipPowerSavingPortLEDState.setStatus(_A)
class _SwEquipPowerSavingPortState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_SwEquipPowerSavingPortState_Type.__name__=_C
_SwEquipPowerSavingPortState_Object=MibScalar
swEquipPowerSavingPortState=_SwEquipPowerSavingPortState_Object((1,3,6,1,4,1,171,12,11,1,11,5),_SwEquipPowerSavingPortState_Type())
swEquipPowerSavingPortState.setMaxAccess(_D)
if mibBuilder.loadTexts:swEquipPowerSavingPortState.setStatus(_A)
_SwEquipPowerSavingScheduleCtrl_ObjectIdentity=ObjectIdentity
swEquipPowerSavingScheduleCtrl=_SwEquipPowerSavingScheduleCtrl_ObjectIdentity((1,3,6,1,4,1,171,12,11,1,11,6))
_SwEquipPowerSavingHibernationTable_Object=MibTable
swEquipPowerSavingHibernationTable=_SwEquipPowerSavingHibernationTable_Object((1,3,6,1,4,1,171,12,11,1,11,6,1))
if mibBuilder.loadTexts:swEquipPowerSavingHibernationTable.setStatus(_A)
_SwEquipPowerSavingHibernationEntry_Object=MibTableRow
swEquipPowerSavingHibernationEntry=_SwEquipPowerSavingHibernationEntry_Object((1,3,6,1,4,1,171,12,11,1,11,6,1,1))
swEquipPowerSavingHibernationEntry.setIndexNames((0,_P,_Q))
if mibBuilder.loadTexts:swEquipPowerSavingHibernationEntry.setStatus(_A)
_SwEquipPowerSavingHiberRowStatus_Type=RowStatus
_SwEquipPowerSavingHiberRowStatus_Object=MibTableColumn
swEquipPowerSavingHiberRowStatus=_SwEquipPowerSavingHiberRowStatus_Object((1,3,6,1,4,1,171,12,11,1,11,6,1,1,100),_SwEquipPowerSavingHiberRowStatus_Type())
swEquipPowerSavingHiberRowStatus.setMaxAccess(_Y)
if mibBuilder.loadTexts:swEquipPowerSavingHiberRowStatus.setStatus(_A)
_SwEquipPowerSavingPortLedTable_Object=MibTable
swEquipPowerSavingPortLedTable=_SwEquipPowerSavingPortLedTable_Object((1,3,6,1,4,1,171,12,11,1,11,6,2))
if mibBuilder.loadTexts:swEquipPowerSavingPortLedTable.setStatus(_A)
_SwEquipPowerSavingPortLedEntry_Object=MibTableRow
swEquipPowerSavingPortLedEntry=_SwEquipPowerSavingPortLedEntry_Object((1,3,6,1,4,1,171,12,11,1,11,6,2,1))
swEquipPowerSavingPortLedEntry.setIndexNames((0,_P,_Q))
if mibBuilder.loadTexts:swEquipPowerSavingPortLedEntry.setStatus(_A)
_SwEquipPowerSavingPortLedRowStatus_Type=RowStatus
_SwEquipPowerSavingPortLedRowStatus_Object=MibTableColumn
swEquipPowerSavingPortLedRowStatus=_SwEquipPowerSavingPortLedRowStatus_Object((1,3,6,1,4,1,171,12,11,1,11,6,2,1,100),_SwEquipPowerSavingPortLedRowStatus_Type())
swEquipPowerSavingPortLedRowStatus.setMaxAccess(_Y)
if mibBuilder.loadTexts:swEquipPowerSavingPortLedRowStatus.setStatus(_A)
_SwEquipPowerSavingPortTable_Object=MibTable
swEquipPowerSavingPortTable=_SwEquipPowerSavingPortTable_Object((1,3,6,1,4,1,171,12,11,1,11,6,3))
if mibBuilder.loadTexts:swEquipPowerSavingPortTable.setStatus(_A)
_SwEquipPowerSavingPortEntry_Object=MibTableRow
swEquipPowerSavingPortEntry=_SwEquipPowerSavingPortEntry_Object((1,3,6,1,4,1,171,12,11,1,11,6,3,1))
swEquipPowerSavingPortEntry.setIndexNames((0,_B,_i),(0,_P,_Q))
if mibBuilder.loadTexts:swEquipPowerSavingPortEntry.setStatus(_A)
_SwEquipPowerSavingPortIndex_Type=Integer32
_SwEquipPowerSavingPortIndex_Object=MibTableColumn
swEquipPowerSavingPortIndex=_SwEquipPowerSavingPortIndex_Object((1,3,6,1,4,1,171,12,11,1,11,6,3,1,1),_SwEquipPowerSavingPortIndex_Type())
swEquipPowerSavingPortIndex.setMaxAccess(_Z)
if mibBuilder.loadTexts:swEquipPowerSavingPortIndex.setStatus(_A)
_SwEquipPowerSavingPortRowStatus_Type=RowStatus
_SwEquipPowerSavingPortRowStatus_Object=MibTableColumn
swEquipPowerSavingPortRowStatus=_SwEquipPowerSavingPortRowStatus_Object((1,3,6,1,4,1,171,12,11,1,11,6,3,1,100),_SwEquipPowerSavingPortRowStatus_Type())
swEquipPowerSavingPortRowStatus.setMaxAccess(_Y)
if mibBuilder.loadTexts:swEquipPowerSavingPortRowStatus.setStatus(_A)
_SwEquipEeeMgmt_ObjectIdentity=ObjectIdentity
swEquipEeeMgmt=_SwEquipEeeMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,11,1,11,20))
_SwEquipEeeState_Type=PortList
_SwEquipEeeState_Object=MibScalar
swEquipEeeState=_SwEquipEeeState_Object((1,3,6,1,4,1,171,12,11,1,11,20,1),_SwEquipEeeState_Type())
swEquipEeeState.setMaxAccess(_D)
if mibBuilder.loadTexts:swEquipEeeState.setStatus(_A)
_SwEquipmentTemperatureCtrl_ObjectIdentity=ObjectIdentity
swEquipmentTemperatureCtrl=_SwEquipmentTemperatureCtrl_ObjectIdentity((1,3,6,1,4,1,171,12,11,1,12))
class _SwTemperatureTrapState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_SwTemperatureTrapState_Type.__name__=_C
_SwTemperatureTrapState_Object=MibScalar
swTemperatureTrapState=_SwTemperatureTrapState_Object((1,3,6,1,4,1,171,12,11,1,12,1),_SwTemperatureTrapState_Type())
swTemperatureTrapState.setMaxAccess(_D)
if mibBuilder.loadTexts:swTemperatureTrapState.setStatus(_A)
class _SwTemperatureLogState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_SwTemperatureLogState_Type.__name__=_C
_SwTemperatureLogState_Object=MibScalar
swTemperatureLogState=_SwTemperatureLogState_Object((1,3,6,1,4,1,171,12,11,1,12,2),_SwTemperatureLogState_Type())
swTemperatureLogState.setMaxAccess(_D)
if mibBuilder.loadTexts:swTemperatureLogState.setStatus(_A)
_SwEquipmentLEDCtrl_ObjectIdentity=ObjectIdentity
swEquipmentLEDCtrl=_SwEquipmentLEDCtrl_ObjectIdentity((1,3,6,1,4,1,171,12,11,1,13))
class _SwEquipmentPortLEDState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_SwEquipmentPortLEDState_Type.__name__=_C
_SwEquipmentPortLEDState_Object=MibScalar
swEquipmentPortLEDState=_SwEquipmentPortLEDState_Object((1,3,6,1,4,1,171,12,11,1,13,1),_SwEquipmentPortLEDState_Type())
swEquipmentPortLEDState.setMaxAccess(_D)
if mibBuilder.loadTexts:swEquipmentPortLEDState.setStatus(_A)
_SwExternalAlarmStackingTable_Object=MibTable
swExternalAlarmStackingTable=_SwExternalAlarmStackingTable_Object((1,3,6,1,4,1,171,12,11,1,15))
if mibBuilder.loadTexts:swExternalAlarmStackingTable.setStatus(_A)
_SwExternalAlarmStackingEntry_Object=MibTableRow
swExternalAlarmStackingEntry=_SwExternalAlarmStackingEntry_Object((1,3,6,1,4,1,171,12,11,1,15,1))
swExternalAlarmStackingEntry.setIndexNames((0,_B,_a),(0,_B,_b))
if mibBuilder.loadTexts:swExternalAlarmStackingEntry.setStatus(_A)
_SwExternalAlarmStackingUnitIndex_Type=Integer32
_SwExternalAlarmStackingUnitIndex_Object=MibTableColumn
swExternalAlarmStackingUnitIndex=_SwExternalAlarmStackingUnitIndex_Object((1,3,6,1,4,1,171,12,11,1,15,1,1),_SwExternalAlarmStackingUnitIndex_Type())
swExternalAlarmStackingUnitIndex.setMaxAccess(_Z)
if mibBuilder.loadTexts:swExternalAlarmStackingUnitIndex.setStatus(_A)
_SwExternalAlarmStackingChannel_Type=Integer32
_SwExternalAlarmStackingChannel_Object=MibTableColumn
swExternalAlarmStackingChannel=_SwExternalAlarmStackingChannel_Object((1,3,6,1,4,1,171,12,11,1,15,1,2),_SwExternalAlarmStackingChannel_Type())
swExternalAlarmStackingChannel.setMaxAccess(_Z)
if mibBuilder.loadTexts:swExternalAlarmStackingChannel.setStatus(_A)
class _SwExternalAlarmStackingMessage_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_SwExternalAlarmStackingMessage_Type.__name__=_H
_SwExternalAlarmStackingMessage_Object=MibTableColumn
swExternalAlarmStackingMessage=_SwExternalAlarmStackingMessage_Object((1,3,6,1,4,1,171,12,11,1,15,1,3),_SwExternalAlarmStackingMessage_Type())
swExternalAlarmStackingMessage.setMaxAccess(_D)
if mibBuilder.loadTexts:swExternalAlarmStackingMessage.setStatus(_A)
class _SwExternalAlarmStackingStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_g,1),(_h,2)))
_SwExternalAlarmStackingStatus_Type.__name__=_C
_SwExternalAlarmStackingStatus_Object=MibTableColumn
swExternalAlarmStackingStatus=_SwExternalAlarmStackingStatus_Object((1,3,6,1,4,1,171,12,11,1,15,1,4),_SwExternalAlarmStackingStatus_Type())
swExternalAlarmStackingStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:swExternalAlarmStackingStatus.setStatus(_A)
_SwEquipmentNotify_ObjectIdentity=ObjectIdentity
swEquipmentNotify=_SwEquipmentNotify_ObjectIdentity((1,3,6,1,4,1,171,12,11,2))
_SwEquipmentNotifyMgmt_ObjectIdentity=ObjectIdentity
swEquipmentNotifyMgmt=_SwEquipmentNotifyMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,11,2,1))
_SwEquipUnitNotifyMgmt_ObjectIdentity=ObjectIdentity
swEquipUnitNotifyMgmt=_SwEquipUnitNotifyMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,11,2,1,1))
_SwUnitInsertSeverity_Type=AgentNotifyLevel
_SwUnitInsertSeverity_Object=MibScalar
swUnitInsertSeverity=_SwUnitInsertSeverity_Object((1,3,6,1,4,1,171,12,11,2,1,1,1),_SwUnitInsertSeverity_Type())
swUnitInsertSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:swUnitInsertSeverity.setStatus(_A)
_SwUnitRemoveSeverity_Type=AgentNotifyLevel
_SwUnitRemoveSeverity_Object=MibScalar
swUnitRemoveSeverity=_SwUnitRemoveSeverity_Object((1,3,6,1,4,1,171,12,11,2,1,1,2),_SwUnitRemoveSeverity_Type())
swUnitRemoveSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:swUnitRemoveSeverity.setStatus(_A)
_SwUnitFailureSeverity_Type=AgentNotifyLevel
_SwUnitFailureSeverity_Object=MibScalar
swUnitFailureSeverity=_SwUnitFailureSeverity_Object((1,3,6,1,4,1,171,12,11,2,1,1,3),_SwUnitFailureSeverity_Type())
swUnitFailureSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:swUnitFailureSeverity.setStatus(_A)
_SwEquipPowerNotifyMgmt_ObjectIdentity=ObjectIdentity
swEquipPowerNotifyMgmt=_SwEquipPowerNotifyMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,11,2,1,2))
_SwPowerStatusChgSeverity_Type=AgentNotifyLevel
_SwPowerStatusChgSeverity_Object=MibScalar
swPowerStatusChgSeverity=_SwPowerStatusChgSeverity_Object((1,3,6,1,4,1,171,12,11,2,1,2,1),_SwPowerStatusChgSeverity_Type())
swPowerStatusChgSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:swPowerStatusChgSeverity.setStatus(_A)
_SwPowerFailureSeverity_Type=AgentNotifyLevel
_SwPowerFailureSeverity_Object=MibScalar
swPowerFailureSeverity=_SwPowerFailureSeverity_Object((1,3,6,1,4,1,171,12,11,2,1,2,2),_SwPowerFailureSeverity_Type())
swPowerFailureSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:swPowerFailureSeverity.setStatus(_A)
_SwPowerRecoverSeverity_Type=AgentNotifyLevel
_SwPowerRecoverSeverity_Object=MibScalar
swPowerRecoverSeverity=_SwPowerRecoverSeverity_Object((1,3,6,1,4,1,171,12,11,2,1,2,3),_SwPowerRecoverSeverity_Type())
swPowerRecoverSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:swPowerRecoverSeverity.setStatus(_A)
_SwEquipFanNotifyMgmt_ObjectIdentity=ObjectIdentity
swEquipFanNotifyMgmt=_SwEquipFanNotifyMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,11,2,1,3))
_SwFanFailureSeverity_Type=AgentNotifyLevel
_SwFanFailureSeverity_Object=MibScalar
swFanFailureSeverity=_SwFanFailureSeverity_Object((1,3,6,1,4,1,171,12,11,2,1,3,1),_SwFanFailureSeverity_Type())
swFanFailureSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:swFanFailureSeverity.setStatus(_A)
_SwFanRecoverSeverity_Type=AgentNotifyLevel
_SwFanRecoverSeverity_Object=MibScalar
swFanRecoverSeverity=_SwFanRecoverSeverity_Object((1,3,6,1,4,1,171,12,11,2,1,3,2),_SwFanRecoverSeverity_Type())
swFanRecoverSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:swFanRecoverSeverity.setStatus(_A)
_SwEquipTemperatureNotifyMgmt_ObjectIdentity=ObjectIdentity
swEquipTemperatureNotifyMgmt=_SwEquipTemperatureNotifyMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,11,2,1,4))
_SwHighTemperatureSeverity_Type=AgentNotifyLevel
_SwHighTemperatureSeverity_Object=MibScalar
swHighTemperatureSeverity=_SwHighTemperatureSeverity_Object((1,3,6,1,4,1,171,12,11,2,1,4,1),_SwHighTemperatureSeverity_Type())
swHighTemperatureSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:swHighTemperatureSeverity.setStatus(_A)
_SwHighTemperatureRecoverSeverity_Type=AgentNotifyLevel
_SwHighTemperatureRecoverSeverity_Object=MibScalar
swHighTemperatureRecoverSeverity=_SwHighTemperatureRecoverSeverity_Object((1,3,6,1,4,1,171,12,11,2,1,4,2),_SwHighTemperatureRecoverSeverity_Type())
swHighTemperatureRecoverSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:swHighTemperatureRecoverSeverity.setStatus(_A)
_SwLowTemperatureSeverity_Type=AgentNotifyLevel
_SwLowTemperatureSeverity_Object=MibScalar
swLowTemperatureSeverity=_SwLowTemperatureSeverity_Object((1,3,6,1,4,1,171,12,11,2,1,4,3),_SwLowTemperatureSeverity_Type())
swLowTemperatureSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:swLowTemperatureSeverity.setStatus(_A)
_SwLowTemperatureRecoverSeverity_Type=AgentNotifyLevel
_SwLowTemperatureRecoverSeverity_Object=MibScalar
swLowTemperatureRecoverSeverity=_SwLowTemperatureRecoverSeverity_Object((1,3,6,1,4,1,171,12,11,2,1,4,4),_SwLowTemperatureRecoverSeverity_Type())
swLowTemperatureRecoverSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:swLowTemperatureRecoverSeverity.setStatus(_A)
_SwEquipmentNotification_ObjectIdentity=ObjectIdentity
swEquipmentNotification=_SwEquipmentNotification_ObjectIdentity((1,3,6,1,4,1,171,12,11,2,2))
_SwEquipUnitNotification_ObjectIdentity=ObjectIdentity
swEquipUnitNotification=_SwEquipUnitNotification_ObjectIdentity((1,3,6,1,4,1,171,12,11,2,2,1))
_SwEquipUnitNotifyPrefix_ObjectIdentity=ObjectIdentity
swEquipUnitNotifyPrefix=_SwEquipUnitNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,171,12,11,2,2,1,0))
_SwEquipPowerNotification_ObjectIdentity=ObjectIdentity
swEquipPowerNotification=_SwEquipPowerNotification_ObjectIdentity((1,3,6,1,4,1,171,12,11,2,2,2))
_SwEquipPowerNotifyPerfix_ObjectIdentity=ObjectIdentity
swEquipPowerNotifyPerfix=_SwEquipPowerNotifyPerfix_ObjectIdentity((1,3,6,1,4,1,171,12,11,2,2,2,0))
_SwEquipFanNotification_ObjectIdentity=ObjectIdentity
swEquipFanNotification=_SwEquipFanNotification_ObjectIdentity((1,3,6,1,4,1,171,12,11,2,2,3))
_SwEquipFanNotifyPrefix_ObjectIdentity=ObjectIdentity
swEquipFanNotifyPrefix=_SwEquipFanNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,171,12,11,2,2,3,0))
_SwEquipTemperatureNotification_ObjectIdentity=ObjectIdentity
swEquipTemperatureNotification=_SwEquipTemperatureNotification_ObjectIdentity((1,3,6,1,4,1,171,12,11,2,2,4))
_SwEquipTemperatureNotifyPrefix_ObjectIdentity=ObjectIdentity
swEquipTemperatureNotifyPrefix=_SwEquipTemperatureNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,171,12,11,2,2,4,0))
_SwEquipExternalAlarmNotification_ObjectIdentity=ObjectIdentity
swEquipExternalAlarmNotification=_SwEquipExternalAlarmNotification_ObjectIdentity((1,3,6,1,4,1,171,12,11,2,2,5))
_SwEquipExternalAlarmNotifyPrefix_ObjectIdentity=ObjectIdentity
swEquipExternalAlarmNotifyPrefix=_SwEquipExternalAlarmNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,171,12,11,2,2,5,0))
_SwNotificationBindings_ObjectIdentity=ObjectIdentity
swNotificationBindings=_SwNotificationBindings_ObjectIdentity((1,3,6,1,4,1,171,12,11,2,3))
_SwEquipTemperNotifyBindings_ObjectIdentity=ObjectIdentity
swEquipTemperNotifyBindings=_SwEquipTemperNotifyBindings_ObjectIdentity((1,3,6,1,4,1,171,12,11,2,3,1))
_SwTemperSensorID_Type=Integer32
_SwTemperSensorID_Object=MibScalar
swTemperSensorID=_SwTemperSensorID_Object((1,3,6,1,4,1,171,12,11,2,3,1,1),_SwTemperSensorID_Type())
swTemperSensorID.setMaxAccess(_c)
if mibBuilder.loadTexts:swTemperSensorID.setStatus(_A)
_SwEquipUnitNotifyBindings_ObjectIdentity=ObjectIdentity
swEquipUnitNotifyBindings=_SwEquipUnitNotifyBindings_ObjectIdentity((1,3,6,1,4,1,171,12,11,2,3,2))
class _SwStackTopologyType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('chain',1),('ring',2)))
_SwStackTopologyType_Type.__name__=_C
_SwStackTopologyType_Object=MibScalar
swStackTopologyType=_SwStackTopologyType_Object((1,3,6,1,4,1,171,12,11,2,3,2,1),_SwStackTopologyType_Type())
swStackTopologyType.setMaxAccess(_c)
if mibBuilder.loadTexts:swStackTopologyType.setStatus(_A)
class _SwStackRoleChangeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('backup-to-master',1),('slave-to-master',2)))
_SwStackRoleChangeType_Type.__name__=_C
_SwStackRoleChangeType_Object=MibScalar
swStackRoleChangeType=_SwStackRoleChangeType_Object((1,3,6,1,4,1,171,12,11,2,3,2,2),_SwStackRoleChangeType_Type())
swStackRoleChangeType.setMaxAccess(_c)
if mibBuilder.loadTexts:swStackRoleChangeType.setStatus(_A)
swUnitInsert=NotificationType((1,3,6,1,4,1,171,12,11,2,2,1,0,1))
swUnitInsert.setObjects(*((_B,_I),(_B,_U)))
if mibBuilder.loadTexts:swUnitInsert.setStatus(_A)
swUnitRemove=NotificationType((1,3,6,1,4,1,171,12,11,2,2,1,0,2))
swUnitRemove.setObjects(*((_B,_I),(_B,_U)))
if mibBuilder.loadTexts:swUnitRemove.setStatus(_A)
swUnitFailure=NotificationType((1,3,6,1,4,1,171,12,11,2,2,1,0,3))
swUnitFailure.setObjects((_B,_I))
if mibBuilder.loadTexts:swUnitFailure.setStatus(_A)
swUnitTPChange=NotificationType((1,3,6,1,4,1,171,12,11,2,2,1,0,4))
swUnitTPChange.setObjects(*((_B,_j),(_B,_I),(_B,_U)))
if mibBuilder.loadTexts:swUnitTPChange.setStatus(_A)
swUnitRoleChange=NotificationType((1,3,6,1,4,1,171,12,11,2,2,1,0,5))
swUnitRoleChange.setObjects(*((_B,_k),(_B,_I)))
if mibBuilder.loadTexts:swUnitRoleChange.setStatus(_A)
swPowerStatusChg=NotificationType((1,3,6,1,4,1,171,12,11,2,2,2,0,1))
swPowerStatusChg.setObjects(*((_B,_L),(_B,_M),(_B,_V)))
if mibBuilder.loadTexts:swPowerStatusChg.setStatus(_A)
swPowerFailure=NotificationType((1,3,6,1,4,1,171,12,11,2,2,2,0,2))
swPowerFailure.setObjects(*((_B,_L),(_B,_M),(_B,_V)))
if mibBuilder.loadTexts:swPowerFailure.setStatus(_A)
swPowerRecover=NotificationType((1,3,6,1,4,1,171,12,11,2,2,2,0,3))
swPowerRecover.setObjects(*((_B,_L),(_B,_M),(_B,_V)))
if mibBuilder.loadTexts:swPowerRecover.setStatus(_A)
swFanFailure=NotificationType((1,3,6,1,4,1,171,12,11,2,2,3,0,1))
swFanFailure.setObjects(*((_B,_R),(_B,_S)))
if mibBuilder.loadTexts:swFanFailure.setStatus(_A)
swFanRecover=NotificationType((1,3,6,1,4,1,171,12,11,2,2,3,0,2))
swFanRecover.setObjects(*((_B,_R),(_B,_S)))
if mibBuilder.loadTexts:swFanRecover.setStatus(_A)
swHighTemperature=NotificationType((1,3,6,1,4,1,171,12,11,2,2,4,0,1))
swHighTemperature.setObjects(*((_B,_K),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:swHighTemperature.setStatus(_A)
swHighTemperatureRecover=NotificationType((1,3,6,1,4,1,171,12,11,2,2,4,0,2))
swHighTemperatureRecover.setObjects(*((_B,_K),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:swHighTemperatureRecover.setStatus(_A)
swLowTemperature=NotificationType((1,3,6,1,4,1,171,12,11,2,2,4,0,3))
swLowTemperature.setObjects(*((_B,_K),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:swLowTemperature.setStatus(_A)
swLowTemperatureRecover=NotificationType((1,3,6,1,4,1,171,12,11,2,2,4,0,4))
swLowTemperatureRecover.setObjects(*((_B,_K),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:swLowTemperatureRecover.setStatus(_A)
swExternalAlarm=NotificationType((1,3,6,1,4,1,171,12,11,2,2,5,0,1))
swExternalAlarm.setObjects(*((_B,_X),(_B,_l)))
if mibBuilder.loadTexts:swExternalAlarm.setStatus(_A)
swExternalAlarmStacking=NotificationType((1,3,6,1,4,1,171,12,11,2,2,5,0,2))
swExternalAlarmStacking.setObjects(*((_B,_a),(_B,_b),(_B,_m)))
if mibBuilder.loadTexts:swExternalAlarmStacking.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'MacAddress':MacAddress,'swEquipmentMIB':swEquipmentMIB,'swEquipment':swEquipment,'swEquipmentCapacity':swEquipmentCapacity,'swFanTrapState':swFanTrapState,'swPowerTrapState':swPowerTrapState,'swPowerTable':swPowerTable,'swPowerEntry':swPowerEntry,_L:swPowerUnitIndex,_M:swPowerID,_V:swPowerStatus,'swFanTable':swFanTable,'swFanEntry':swFanEntry,_R:swFanUnitIndex,_S:swFanID,'swFanStatus':swFanStatus,'swFanPostion':swFanPostion,'swFanNumber':swFanNumber,'swFanSpeed':swFanSpeed,'swTemperatureTable':swTemperatureTable,'swTemperatureEntry':swTemperatureEntry,_K:swTemperatureUnitIndex,_O:swTemperatureCurrent,'swTemperatureHighThresh':swTemperatureHighThresh,'swTemperatureLowThresh':swTemperatureLowThresh,'swUnitMgmt':swUnitMgmt,'swUnitStackingVersion':swUnitStackingVersion,'swUnitMaxSupportedUnits':swUnitMaxSupportedUnits,'swUnitNumOfUnit':swUnitNumOfUnit,'swUnitMgmtTable':swUnitMgmtTable,'swUnitMgmtEntry':swUnitMgmtEntry,_I:swUnitMgmtId,_U:swUnitMgmtMacAddr,'swUnitMgmtStartPort':swUnitMgmtStartPort,'swUnitMgmtPortRange':swUnitMgmtPortRange,'swUnitMgmtFrontPanelLedStatus':swUnitMgmtFrontPanelLedStatus,'swUnitMgmtCtrlMode':swUnitMgmtCtrlMode,'swUnitMgmtCurrentMode':swUnitMgmtCurrentMode,'swUnitMgmtVersion':swUnitMgmtVersion,'swUnitMgmtModuleName':swUnitMgmtModuleName,'swUnitMgmtPromVersion':swUnitMgmtPromVersion,'swUnitMgmtFirmwareVersion':swUnitMgmtFirmwareVersion,'swUnitMgmtHardwareVersion':swUnitMgmtHardwareVersion,'swUnitMgmtPriority':swUnitMgmtPriority,'swUnitMgmtUserSetState':swUnitMgmtUserSetState,'swUnitMgmtExistState':swUnitMgmtExistState,'swUnitMgmtBoxId':swUnitMgmtBoxId,'swUnitMgmtSerialNumber':swUnitMgmtSerialNumber,'swUnitTopology':swUnitTopology,'swUnitStackMode':swUnitStackMode,'swUnitStackForceMasterRole':swUnitStackForceMasterRole,'swUnitStackTrapState':swUnitStackTrapState,'swUnitStackLogState':swUnitStackLogState,'swExternalAlarmTable':swExternalAlarmTable,'swExternalAlarmEntry':swExternalAlarmEntry,_X:swExternalAlarmChannel,_l:swExternalAlarmMessage,'swExternalAlarmStatus':swExternalAlarmStatus,'swEquipmentPowerSaving':swEquipmentPowerSaving,'swEquipPowerSavingLinkDetectState':swEquipPowerSavingLinkDetectState,'swEquipPowerSavingLenDetect':swEquipPowerSavingLenDetect,'swEquipPowerSavingHiberState':swEquipPowerSavingHiberState,'swEquipPowerSavingPortLEDState':swEquipPowerSavingPortLEDState,'swEquipPowerSavingPortState':swEquipPowerSavingPortState,'swEquipPowerSavingScheduleCtrl':swEquipPowerSavingScheduleCtrl,'swEquipPowerSavingHibernationTable':swEquipPowerSavingHibernationTable,'swEquipPowerSavingHibernationEntry':swEquipPowerSavingHibernationEntry,'swEquipPowerSavingHiberRowStatus':swEquipPowerSavingHiberRowStatus,'swEquipPowerSavingPortLedTable':swEquipPowerSavingPortLedTable,'swEquipPowerSavingPortLedEntry':swEquipPowerSavingPortLedEntry,'swEquipPowerSavingPortLedRowStatus':swEquipPowerSavingPortLedRowStatus,'swEquipPowerSavingPortTable':swEquipPowerSavingPortTable,'swEquipPowerSavingPortEntry':swEquipPowerSavingPortEntry,_i:swEquipPowerSavingPortIndex,'swEquipPowerSavingPortRowStatus':swEquipPowerSavingPortRowStatus,'swEquipEeeMgmt':swEquipEeeMgmt,'swEquipEeeState':swEquipEeeState,'swEquipmentTemperatureCtrl':swEquipmentTemperatureCtrl,'swTemperatureTrapState':swTemperatureTrapState,'swTemperatureLogState':swTemperatureLogState,'swEquipmentLEDCtrl':swEquipmentLEDCtrl,'swEquipmentPortLEDState':swEquipmentPortLEDState,'swExternalAlarmStackingTable':swExternalAlarmStackingTable,'swExternalAlarmStackingEntry':swExternalAlarmStackingEntry,_a:swExternalAlarmStackingUnitIndex,_b:swExternalAlarmStackingChannel,_m:swExternalAlarmStackingMessage,'swExternalAlarmStackingStatus':swExternalAlarmStackingStatus,'swEquipmentNotify':swEquipmentNotify,'swEquipmentNotifyMgmt':swEquipmentNotifyMgmt,'swEquipUnitNotifyMgmt':swEquipUnitNotifyMgmt,'swUnitInsertSeverity':swUnitInsertSeverity,'swUnitRemoveSeverity':swUnitRemoveSeverity,'swUnitFailureSeverity':swUnitFailureSeverity,'swEquipPowerNotifyMgmt':swEquipPowerNotifyMgmt,'swPowerStatusChgSeverity':swPowerStatusChgSeverity,'swPowerFailureSeverity':swPowerFailureSeverity,'swPowerRecoverSeverity':swPowerRecoverSeverity,'swEquipFanNotifyMgmt':swEquipFanNotifyMgmt,'swFanFailureSeverity':swFanFailureSeverity,'swFanRecoverSeverity':swFanRecoverSeverity,'swEquipTemperatureNotifyMgmt':swEquipTemperatureNotifyMgmt,'swHighTemperatureSeverity':swHighTemperatureSeverity,'swHighTemperatureRecoverSeverity':swHighTemperatureRecoverSeverity,'swLowTemperatureSeverity':swLowTemperatureSeverity,'swLowTemperatureRecoverSeverity':swLowTemperatureRecoverSeverity,'swEquipmentNotification':swEquipmentNotification,'swEquipUnitNotification':swEquipUnitNotification,'swEquipUnitNotifyPrefix':swEquipUnitNotifyPrefix,'swUnitInsert':swUnitInsert,'swUnitRemove':swUnitRemove,'swUnitFailure':swUnitFailure,'swUnitTPChange':swUnitTPChange,'swUnitRoleChange':swUnitRoleChange,'swEquipPowerNotification':swEquipPowerNotification,'swEquipPowerNotifyPerfix':swEquipPowerNotifyPerfix,'swPowerStatusChg':swPowerStatusChg,'swPowerFailure':swPowerFailure,'swPowerRecover':swPowerRecover,'swEquipFanNotification':swEquipFanNotification,'swEquipFanNotifyPrefix':swEquipFanNotifyPrefix,'swFanFailure':swFanFailure,'swFanRecover':swFanRecover,'swEquipTemperatureNotification':swEquipTemperatureNotification,'swEquipTemperatureNotifyPrefix':swEquipTemperatureNotifyPrefix,'swHighTemperature':swHighTemperature,'swHighTemperatureRecover':swHighTemperatureRecover,'swLowTemperature':swLowTemperature,'swLowTemperatureRecover':swLowTemperatureRecover,'swEquipExternalAlarmNotification':swEquipExternalAlarmNotification,'swEquipExternalAlarmNotifyPrefix':swEquipExternalAlarmNotifyPrefix,'swExternalAlarm':swExternalAlarm,'swExternalAlarmStacking':swExternalAlarmStacking,'swNotificationBindings':swNotificationBindings,'swEquipTemperNotifyBindings':swEquipTemperNotifyBindings,_N:swTemperSensorID,'swEquipUnitNotifyBindings':swEquipUnitNotifyBindings,_j:swStackTopologyType,_k:swStackRoleChangeType})