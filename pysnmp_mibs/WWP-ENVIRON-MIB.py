_l='wwpEnvDryContactCloseStateCount'
_k='wwpEnvDryContactCloseStateName'
_j='wwpEnvDryContactOpenStateCount'
_i='wwpEnvDryContactOpenStateName'
_h='wwpEnvDoorState'
_g='wwpEnvPortalPowerSource'
_f='wwpEnvPortalBatteryCondition'
_e='wwpEnvPortalBatteryVoltageLevel'
_d='wwpEnvPortalBatteryStatus'
_c='wwpPowerSwitchingOp'
_b='wwpEnvTempSensorLowThreshold'
_a='wwpEnvTempSensorHighThreshold'
_Z='wwpEnvTempSensorValue'
_Y='wwpEnvTempSensorState'
_X='wwpEnvFanModuleState'
_W='wwpEnvPowerSupplyType'
_V='wwpEnvPowerSupplyState'
_U='wwpEnvPortBankId'
_T='normal'
_S='wwpEnvTempSensorNum'
_R='notSupported'
_Q='installedAndNotOperating'
_P='installedAndOperating'
_O='notInstalled'
_N='infoNotAvailable'
_M='disable'
_L='enable'
_K='degrees Celsius'
_J='rpm'
_I='wwpEnvFanModuleNum'
_H='wwpEnvPowerSupplyNum'
_G='DisplayString'
_F='TruthValue'
_E='WWP-ENVIRON-MIB'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention',_F)
wwpModules,=mibBuilder.importSymbols('WWP-SMI','wwpModules')
wwpEnvironMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,13))
if mibBuilder.loadTexts:wwpEnvironMIB.setRevisions(('2003-04-28 00:00','2003-03-11 00:00','2001-04-03 17:00'))
class PortList(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_WwpEnvironMIBObjects_ObjectIdentity=ObjectIdentity
wwpEnvironMIBObjects=_WwpEnvironMIBObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,13,1))
_WwpEnviron_ObjectIdentity=ObjectIdentity
wwpEnviron=_WwpEnviron_ObjectIdentity((1,3,6,1,4,1,6141,2,13,1,1))
_WwpEnvBatteryModule_ObjectIdentity=ObjectIdentity
wwpEnvBatteryModule=_WwpEnvBatteryModule_ObjectIdentity((1,3,6,1,4,1,6141,2,13,1,1,1))
class _WwpEnvBattStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('presentAndWorking',1),('presentButNotWorking',2),('notPresent',3)))
_WwpEnvBattStatus_Type.__name__=_C
_WwpEnvBattStatus_Object=MibScalar
wwpEnvBattStatus=_WwpEnvBattStatus_Object((1,3,6,1,4,1,6141,2,13,1,1,1,1),_WwpEnvBattStatus_Type())
wwpEnvBattStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpEnvBattStatus.setStatus(_A)
_WwpEnvPowerSupplyModule_ObjectIdentity=ObjectIdentity
wwpEnvPowerSupplyModule=_WwpEnvPowerSupplyModule_ObjectIdentity((1,3,6,1,4,1,6141,2,13,1,1,2))
_WwpEnvPowerTable_Object=MibTable
wwpEnvPowerTable=_WwpEnvPowerTable_Object((1,3,6,1,4,1,6141,2,13,1,1,2,1))
if mibBuilder.loadTexts:wwpEnvPowerTable.setStatus(_A)
_WwpEnvPowerEntry_Object=MibTableRow
wwpEnvPowerEntry=_WwpEnvPowerEntry_Object((1,3,6,1,4,1,6141,2,13,1,1,2,1,1))
wwpEnvPowerEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:wwpEnvPowerEntry.setStatus(_A)
class _WwpEnvPowerSupplyNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_WwpEnvPowerSupplyNum_Type.__name__=_C
_WwpEnvPowerSupplyNum_Object=MibTableColumn
wwpEnvPowerSupplyNum=_WwpEnvPowerSupplyNum_Object((1,3,6,1,4,1,6141,2,13,1,1,2,1,1,1),_WwpEnvPowerSupplyNum_Type())
wwpEnvPowerSupplyNum.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpEnvPowerSupplyNum.setStatus(_A)
class _WwpEnvPowerSupplyState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3),(_Q,4)))
_WwpEnvPowerSupplyState_Type.__name__=_C
_WwpEnvPowerSupplyState_Object=MibTableColumn
wwpEnvPowerSupplyState=_WwpEnvPowerSupplyState_Object((1,3,6,1,4,1,6141,2,13,1,1,2,1,1,2),_WwpEnvPowerSupplyState_Type())
wwpEnvPowerSupplyState.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpEnvPowerSupplyState.setStatus(_A)
class _WwpEnvPowerSupplyType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('ac-dc',1),('dc-dc',2),(_R,3),('highOutput',4),('external',5)))
_WwpEnvPowerSupplyType_Type.__name__=_C
_WwpEnvPowerSupplyType_Object=MibTableColumn
wwpEnvPowerSupplyType=_WwpEnvPowerSupplyType_Object((1,3,6,1,4,1,6141,2,13,1,1,2,1,1,3),_WwpEnvPowerSupplyType_Type())
wwpEnvPowerSupplyType.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpEnvPowerSupplyType.setStatus(_A)
class _WwpEnvPowerSupplyRedundancy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('redundant',1),('notRedundant',2),(_R,3)))
_WwpEnvPowerSupplyRedundancy_Type.__name__=_C
_WwpEnvPowerSupplyRedundancy_Object=MibTableColumn
wwpEnvPowerSupplyRedundancy=_WwpEnvPowerSupplyRedundancy_Object((1,3,6,1,4,1,6141,2,13,1,1,2,1,1,4),_WwpEnvPowerSupplyRedundancy_Type())
wwpEnvPowerSupplyRedundancy.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpEnvPowerSupplyRedundancy.setStatus(_A)
class _WwpEnvRedPowerSupplyNotifEnabled_Type(TruthValue):defaultValue=1
_WwpEnvRedPowerSupplyNotifEnabled_Type.__name__=_F
_WwpEnvRedPowerSupplyNotifEnabled_Object=MibScalar
wwpEnvRedPowerSupplyNotifEnabled=_WwpEnvRedPowerSupplyNotifEnabled_Object((1,3,6,1,4,1,6141,2,13,1,1,2,2),_WwpEnvRedPowerSupplyNotifEnabled_Type())
wwpEnvRedPowerSupplyNotifEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpEnvRedPowerSupplyNotifEnabled.setStatus('deprecated')
_WwpEnvFanModule_ObjectIdentity=ObjectIdentity
wwpEnvFanModule=_WwpEnvFanModule_ObjectIdentity((1,3,6,1,4,1,6141,2,13,1,1,3))
_WwpEnvFanModuleTable_Object=MibTable
wwpEnvFanModuleTable=_WwpEnvFanModuleTable_Object((1,3,6,1,4,1,6141,2,13,1,1,3,1))
if mibBuilder.loadTexts:wwpEnvFanModuleTable.setStatus(_A)
_WwpEnvFanModuleEntry_Object=MibTableRow
wwpEnvFanModuleEntry=_WwpEnvFanModuleEntry_Object((1,3,6,1,4,1,6141,2,13,1,1,3,1,1))
wwpEnvFanModuleEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:wwpEnvFanModuleEntry.setStatus(_A)
class _WwpEnvFanModuleNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_WwpEnvFanModuleNum_Type.__name__=_C
_WwpEnvFanModuleNum_Object=MibTableColumn
wwpEnvFanModuleNum=_WwpEnvFanModuleNum_Object((1,3,6,1,4,1,6141,2,13,1,1,3,1,1,1),_WwpEnvFanModuleNum_Type())
wwpEnvFanModuleNum.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpEnvFanModuleNum.setStatus(_A)
class _WwpEnvFanModuleState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3),(_Q,4)))
_WwpEnvFanModuleState_Type.__name__=_C
_WwpEnvFanModuleState_Object=MibTableColumn
wwpEnvFanModuleState=_WwpEnvFanModuleState_Object((1,3,6,1,4,1,6141,2,13,1,1,3,1,1,2),_WwpEnvFanModuleState_Type())
wwpEnvFanModuleState.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpEnvFanModuleState.setStatus(_A)
class _WwpEnvFanAvgSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_WwpEnvFanAvgSpeed_Type.__name__=_C
_WwpEnvFanAvgSpeed_Object=MibTableColumn
wwpEnvFanAvgSpeed=_WwpEnvFanAvgSpeed_Object((1,3,6,1,4,1,6141,2,13,1,1,3,1,1,3),_WwpEnvFanAvgSpeed_Type())
wwpEnvFanAvgSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpEnvFanAvgSpeed.setStatus(_A)
if mibBuilder.loadTexts:wwpEnvFanAvgSpeed.setUnits(_J)
class _WwpEnvFanCurrentSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_WwpEnvFanCurrentSpeed_Type.__name__=_C
_WwpEnvFanCurrentSpeed_Object=MibTableColumn
wwpEnvFanCurrentSpeed=_WwpEnvFanCurrentSpeed_Object((1,3,6,1,4,1,6141,2,13,1,1,3,1,1,4),_WwpEnvFanCurrentSpeed_Type())
wwpEnvFanCurrentSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpEnvFanCurrentSpeed.setStatus(_A)
if mibBuilder.loadTexts:wwpEnvFanCurrentSpeed.setUnits(_J)
class _WwpEnvFanMinSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_WwpEnvFanMinSpeed_Type.__name__=_C
_WwpEnvFanMinSpeed_Object=MibTableColumn
wwpEnvFanMinSpeed=_WwpEnvFanMinSpeed_Object((1,3,6,1,4,1,6141,2,13,1,1,3,1,1,5),_WwpEnvFanMinSpeed_Type())
wwpEnvFanMinSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpEnvFanMinSpeed.setStatus(_A)
if mibBuilder.loadTexts:wwpEnvFanMinSpeed.setUnits(_J)
class _WwpEnvFanModuleNotifEnabled_Type(TruthValue):defaultValue=1
_WwpEnvFanModuleNotifEnabled_Type.__name__=_F
_WwpEnvFanModuleNotifEnabled_Object=MibScalar
wwpEnvFanModuleNotifEnabled=_WwpEnvFanModuleNotifEnabled_Object((1,3,6,1,4,1,6141,2,13,1,1,3,2),_WwpEnvFanModuleNotifEnabled_Type())
wwpEnvFanModuleNotifEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpEnvFanModuleNotifEnabled.setStatus(_A)
_WwpEnvTempSensor_ObjectIdentity=ObjectIdentity
wwpEnvTempSensor=_WwpEnvTempSensor_ObjectIdentity((1,3,6,1,4,1,6141,2,13,1,1,4))
_WwpEnvTempSensorTable_Object=MibTable
wwpEnvTempSensorTable=_WwpEnvTempSensorTable_Object((1,3,6,1,4,1,6141,2,13,1,1,4,1))
if mibBuilder.loadTexts:wwpEnvTempSensorTable.setStatus(_A)
_WwpEnvTempSensorEntry_Object=MibTableRow
wwpEnvTempSensorEntry=_WwpEnvTempSensorEntry_Object((1,3,6,1,4,1,6141,2,13,1,1,4,1,1))
wwpEnvTempSensorEntry.setIndexNames((0,_E,_S))
if mibBuilder.loadTexts:wwpEnvTempSensorEntry.setStatus(_A)
class _WwpEnvTempSensorNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_WwpEnvTempSensorNum_Type.__name__=_C
_WwpEnvTempSensorNum_Object=MibTableColumn
wwpEnvTempSensorNum=_WwpEnvTempSensorNum_Object((1,3,6,1,4,1,6141,2,13,1,1,4,1,1,1),_WwpEnvTempSensorNum_Type())
wwpEnvTempSensorNum.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpEnvTempSensorNum.setStatus(_A)
_WwpEnvTempSensorValue_Type=Integer32
_WwpEnvTempSensorValue_Object=MibTableColumn
wwpEnvTempSensorValue=_WwpEnvTempSensorValue_Object((1,3,6,1,4,1,6141,2,13,1,1,4,1,1,2),_WwpEnvTempSensorValue_Type())
wwpEnvTempSensorValue.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpEnvTempSensorValue.setStatus(_A)
if mibBuilder.loadTexts:wwpEnvTempSensorValue.setUnits(_K)
_WwpEnvTempSensorHighThreshold_Type=Integer32
_WwpEnvTempSensorHighThreshold_Object=MibTableColumn
wwpEnvTempSensorHighThreshold=_WwpEnvTempSensorHighThreshold_Object((1,3,6,1,4,1,6141,2,13,1,1,4,1,1,3),_WwpEnvTempSensorHighThreshold_Type())
wwpEnvTempSensorHighThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpEnvTempSensorHighThreshold.setStatus(_A)
if mibBuilder.loadTexts:wwpEnvTempSensorHighThreshold.setUnits(_K)
_WwpEnvTempSensorLowThreshold_Type=Integer32
_WwpEnvTempSensorLowThreshold_Object=MibTableColumn
wwpEnvTempSensorLowThreshold=_WwpEnvTempSensorLowThreshold_Object((1,3,6,1,4,1,6141,2,13,1,1,4,1,1,4),_WwpEnvTempSensorLowThreshold_Type())
wwpEnvTempSensorLowThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpEnvTempSensorLowThreshold.setStatus(_A)
if mibBuilder.loadTexts:wwpEnvTempSensorLowThreshold.setUnits(_K)
class _WwpEnvTempSensorState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('higherThanThreshold',0),(_T,1),('lowerThanThreshold',2)))
_WwpEnvTempSensorState_Type.__name__=_C
_WwpEnvTempSensorState_Object=MibTableColumn
wwpEnvTempSensorState=_WwpEnvTempSensorState_Object((1,3,6,1,4,1,6141,2,13,1,1,4,1,1,5),_WwpEnvTempSensorState_Type())
wwpEnvTempSensorState.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpEnvTempSensorState.setStatus(_A)
class _WwpEnvTempNotifEnabled_Type(TruthValue):defaultValue=1
_WwpEnvTempNotifEnabled_Type.__name__=_F
_WwpEnvTempNotifEnabled_Object=MibScalar
wwpEnvTempNotifEnabled=_WwpEnvTempNotifEnabled_Object((1,3,6,1,4,1,6141,2,13,1,1,4,2),_WwpEnvTempNotifEnabled_Type())
wwpEnvTempNotifEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpEnvTempNotifEnabled.setStatus(_A)
_WwpEnvPortPowerMgmt_ObjectIdentity=ObjectIdentity
wwpEnvPortPowerMgmt=_WwpEnvPortPowerMgmt_ObjectIdentity((1,3,6,1,4,1,6141,2,13,1,1,5))
_WwpPortPowerMgmtTable_Object=MibTable
wwpPortPowerMgmtTable=_WwpPortPowerMgmtTable_Object((1,3,6,1,4,1,6141,2,13,1,1,5,1))
if mibBuilder.loadTexts:wwpPortPowerMgmtTable.setStatus(_A)
_WwpPortPowerMgmtEntry_Object=MibTableRow
wwpPortPowerMgmtEntry=_WwpPortPowerMgmtEntry_Object((1,3,6,1,4,1,6141,2,13,1,1,5,1,1))
wwpPortPowerMgmtEntry.setIndexNames((0,_E,_U))
if mibBuilder.loadTexts:wwpPortPowerMgmtEntry.setStatus(_A)
class _WwpEnvPortBankId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_WwpEnvPortBankId_Type.__name__=_C
_WwpEnvPortBankId_Object=MibTableColumn
wwpEnvPortBankId=_WwpEnvPortBankId_Object((1,3,6,1,4,1,6141,2,13,1,1,5,1,1,1),_WwpEnvPortBankId_Type())
wwpEnvPortBankId.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpEnvPortBankId.setStatus(_A)
_WwpEnvPortMap_Type=PortList
_WwpEnvPortMap_Object=MibTableColumn
wwpEnvPortMap=_WwpEnvPortMap_Object((1,3,6,1,4,1,6141,2,13,1,1,5,1,1,2),_WwpEnvPortMap_Type())
wwpEnvPortMap.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpEnvPortMap.setStatus(_A)
class _WwpEnvPortBankOn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('off',0),('on',1)))
_WwpEnvPortBankOn_Type.__name__=_C
_WwpEnvPortBankOn_Object=MibTableColumn
wwpEnvPortBankOn=_WwpEnvPortBankOn_Object((1,3,6,1,4,1,6141,2,13,1,1,5,1,1,3),_WwpEnvPortBankOn_Type())
wwpEnvPortBankOn.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpEnvPortBankOn.setStatus(_A)
_WwpEnvNotif_ObjectIdentity=ObjectIdentity
wwpEnvNotif=_WwpEnvNotif_ObjectIdentity((1,3,6,1,4,1,6141,2,13,1,1,6))
class _WwpPowerSwitchingOp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('acToBattery',1),('bateryToAC',2)))
_WwpPowerSwitchingOp_Type.__name__=_C
_WwpPowerSwitchingOp_Object=MibScalar
wwpPowerSwitchingOp=_WwpPowerSwitchingOp_Object((1,3,6,1,4,1,6141,2,13,1,1,6,1),_WwpPowerSwitchingOp_Type())
wwpPowerSwitchingOp.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpPowerSwitchingOp.setStatus(_A)
_WwpEnvPortalBatteryModule_ObjectIdentity=ObjectIdentity
wwpEnvPortalBatteryModule=_WwpEnvPortalBatteryModule_ObjectIdentity((1,3,6,1,4,1,6141,2,13,1,1,7))
class _WwpEnvPortalBatteryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('present',1),('missing',2)))
_WwpEnvPortalBatteryStatus_Type.__name__=_C
_WwpEnvPortalBatteryStatus_Object=MibScalar
wwpEnvPortalBatteryStatus=_WwpEnvPortalBatteryStatus_Object((1,3,6,1,4,1,6141,2,13,1,1,7,1),_WwpEnvPortalBatteryStatus_Type())
wwpEnvPortalBatteryStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpEnvPortalBatteryStatus.setStatus(_A)
class _WwpEnvPortalBatteryVoltageLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),('low',2)))
_WwpEnvPortalBatteryVoltageLevel_Type.__name__=_C
_WwpEnvPortalBatteryVoltageLevel_Object=MibScalar
wwpEnvPortalBatteryVoltageLevel=_WwpEnvPortalBatteryVoltageLevel_Object((1,3,6,1,4,1,6141,2,13,1,1,7,2),_WwpEnvPortalBatteryVoltageLevel_Type())
wwpEnvPortalBatteryVoltageLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpEnvPortalBatteryVoltageLevel.setStatus(_A)
class _WwpEnvPortalBatteryCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('good',1),('bad',2)))
_WwpEnvPortalBatteryCondition_Type.__name__=_C
_WwpEnvPortalBatteryCondition_Object=MibScalar
wwpEnvPortalBatteryCondition=_WwpEnvPortalBatteryCondition_Object((1,3,6,1,4,1,6141,2,13,1,1,7,3),_WwpEnvPortalBatteryCondition_Type())
wwpEnvPortalBatteryCondition.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpEnvPortalBatteryCondition.setStatus(_A)
class _WwpEnvPortalPowerSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('primaryPower',1),('battery',2)))
_WwpEnvPortalPowerSource_Type.__name__=_C
_WwpEnvPortalPowerSource_Object=MibScalar
wwpEnvPortalPowerSource=_WwpEnvPortalPowerSource_Object((1,3,6,1,4,1,6141,2,13,1,1,7,4),_WwpEnvPortalPowerSource_Type())
wwpEnvPortalPowerSource.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpEnvPortalPowerSource.setStatus(_A)
class _WwpEnvBatteryNormalStateName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_WwpEnvBatteryNormalStateName_Type.__name__=_G
_WwpEnvBatteryNormalStateName_Object=MibScalar
wwpEnvBatteryNormalStateName=_WwpEnvBatteryNormalStateName_Object((1,3,6,1,4,1,6141,2,13,1,1,7,5),_WwpEnvBatteryNormalStateName_Type())
wwpEnvBatteryNormalStateName.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpEnvBatteryNormalStateName.setStatus(_A)
class _WwpEnvBatteryLowStateName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_WwpEnvBatteryLowStateName_Type.__name__=_G
_WwpEnvBatteryLowStateName_Object=MibScalar
wwpEnvBatteryLowStateName=_WwpEnvBatteryLowStateName_Object((1,3,6,1,4,1,6141,2,13,1,1,7,6),_WwpEnvBatteryLowStateName_Type())
wwpEnvBatteryLowStateName.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpEnvBatteryLowStateName.setStatus(_A)
class _WwpEnvBatteryGoodStateName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_WwpEnvBatteryGoodStateName_Type.__name__=_G
_WwpEnvBatteryGoodStateName_Object=MibScalar
wwpEnvBatteryGoodStateName=_WwpEnvBatteryGoodStateName_Object((1,3,6,1,4,1,6141,2,13,1,1,7,7),_WwpEnvBatteryGoodStateName_Type())
wwpEnvBatteryGoodStateName.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpEnvBatteryGoodStateName.setStatus(_A)
class _WwpEnvBatteryBadStateName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_WwpEnvBatteryBadStateName_Type.__name__=_G
_WwpEnvBatteryBadStateName_Object=MibScalar
wwpEnvBatteryBadStateName=_WwpEnvBatteryBadStateName_Object((1,3,6,1,4,1,6141,2,13,1,1,7,8),_WwpEnvBatteryBadStateName_Type())
wwpEnvBatteryBadStateName.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpEnvBatteryBadStateName.setStatus(_A)
class _WwpEnvBatteryPresentStateName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_WwpEnvBatteryPresentStateName_Type.__name__=_G
_WwpEnvBatteryPresentStateName_Object=MibScalar
wwpEnvBatteryPresentStateName=_WwpEnvBatteryPresentStateName_Object((1,3,6,1,4,1,6141,2,13,1,1,7,9),_WwpEnvBatteryPresentStateName_Type())
wwpEnvBatteryPresentStateName.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpEnvBatteryPresentStateName.setStatus(_A)
class _WwpEnvBatteryMissingStateName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_WwpEnvBatteryMissingStateName_Type.__name__=_G
_WwpEnvBatteryMissingStateName_Object=MibScalar
wwpEnvBatteryMissingStateName=_WwpEnvBatteryMissingStateName_Object((1,3,6,1,4,1,6141,2,13,1,1,7,10),_WwpEnvBatteryMissingStateName_Type())
wwpEnvBatteryMissingStateName.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpEnvBatteryMissingStateName.setStatus(_A)
class _WwpEnvBatteryPowerPrimaryStateName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_WwpEnvBatteryPowerPrimaryStateName_Type.__name__=_G
_WwpEnvBatteryPowerPrimaryStateName_Object=MibScalar
wwpEnvBatteryPowerPrimaryStateName=_WwpEnvBatteryPowerPrimaryStateName_Object((1,3,6,1,4,1,6141,2,13,1,1,7,11),_WwpEnvBatteryPowerPrimaryStateName_Type())
wwpEnvBatteryPowerPrimaryStateName.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpEnvBatteryPowerPrimaryStateName.setStatus(_A)
class _WwpEnvBatteryPowerBatteryStateName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_WwpEnvBatteryPowerBatteryStateName_Type.__name__=_G
_WwpEnvBatteryPowerBatteryStateName_Object=MibScalar
wwpEnvBatteryPowerBatteryStateName=_WwpEnvBatteryPowerBatteryStateName_Object((1,3,6,1,4,1,6141,2,13,1,1,7,12),_WwpEnvBatteryPowerBatteryStateName_Type())
wwpEnvBatteryPowerBatteryStateName.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpEnvBatteryPowerBatteryStateName.setStatus(_A)
class _WwpEnvBatteryLowStateNotifEnabled_Type(TruthValue):defaultValue=1
_WwpEnvBatteryLowStateNotifEnabled_Type.__name__=_F
_WwpEnvBatteryLowStateNotifEnabled_Object=MibScalar
wwpEnvBatteryLowStateNotifEnabled=_WwpEnvBatteryLowStateNotifEnabled_Object((1,3,6,1,4,1,6141,2,13,1,1,7,13),_WwpEnvBatteryLowStateNotifEnabled_Type())
wwpEnvBatteryLowStateNotifEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpEnvBatteryLowStateNotifEnabled.setStatus(_A)
class _WwpEnvBatteryBadStateNotifEnabled_Type(TruthValue):defaultValue=1
_WwpEnvBatteryBadStateNotifEnabled_Type.__name__=_F
_WwpEnvBatteryBadStateNotifEnabled_Object=MibScalar
wwpEnvBatteryBadStateNotifEnabled=_WwpEnvBatteryBadStateNotifEnabled_Object((1,3,6,1,4,1,6141,2,13,1,1,7,14),_WwpEnvBatteryBadStateNotifEnabled_Type())
wwpEnvBatteryBadStateNotifEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpEnvBatteryBadStateNotifEnabled.setStatus(_A)
class _WwpEnvBatteryMissingStateNotifEnabled_Type(TruthValue):defaultValue=1
_WwpEnvBatteryMissingStateNotifEnabled_Type.__name__=_F
_WwpEnvBatteryMissingStateNotifEnabled_Object=MibScalar
wwpEnvBatteryMissingStateNotifEnabled=_WwpEnvBatteryMissingStateNotifEnabled_Object((1,3,6,1,4,1,6141,2,13,1,1,7,15),_WwpEnvBatteryMissingStateNotifEnabled_Type())
wwpEnvBatteryMissingStateNotifEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpEnvBatteryMissingStateNotifEnabled.setStatus(_A)
class _WwpEnvBatteryPowerNotifEnabled_Type(TruthValue):defaultValue=1
_WwpEnvBatteryPowerNotifEnabled_Type.__name__=_F
_WwpEnvBatteryPowerNotifEnabled_Object=MibScalar
wwpEnvBatteryPowerNotifEnabled=_WwpEnvBatteryPowerNotifEnabled_Object((1,3,6,1,4,1,6141,2,13,1,1,7,16),_WwpEnvBatteryPowerNotifEnabled_Type())
wwpEnvBatteryPowerNotifEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpEnvBatteryPowerNotifEnabled.setStatus(_A)
class _WwpEnvBatteryPeriodicTrapsTimer_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8760))
_WwpEnvBatteryPeriodicTrapsTimer_Type.__name__=_C
_WwpEnvBatteryPeriodicTrapsTimer_Object=MibScalar
wwpEnvBatteryPeriodicTrapsTimer=_WwpEnvBatteryPeriodicTrapsTimer_Object((1,3,6,1,4,1,6141,2,13,1,1,7,17),_WwpEnvBatteryPeriodicTrapsTimer_Type())
wwpEnvBatteryPeriodicTrapsTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpEnvBatteryPeriodicTrapsTimer.setStatus(_A)
class _WwpEnvBatteryPowerUpTrapsEnable_Type(TruthValue):defaultValue=2
_WwpEnvBatteryPowerUpTrapsEnable_Type.__name__=_F
_WwpEnvBatteryPowerUpTrapsEnable_Object=MibScalar
wwpEnvBatteryPowerUpTrapsEnable=_WwpEnvBatteryPowerUpTrapsEnable_Object((1,3,6,1,4,1,6141,2,13,1,1,7,18),_WwpEnvBatteryPowerUpTrapsEnable_Type())
wwpEnvBatteryPowerUpTrapsEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpEnvBatteryPowerUpTrapsEnable.setStatus(_A)
_WwpEnvDoorModule_ObjectIdentity=ObjectIdentity
wwpEnvDoorModule=_WwpEnvDoorModule_ObjectIdentity((1,3,6,1,4,1,6141,2,13,1,1,8))
class _WwpEnvDoorState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('open',1),('close',2)))
_WwpEnvDoorState_Type.__name__=_C
_WwpEnvDoorState_Object=MibScalar
wwpEnvDoorState=_WwpEnvDoorState_Object((1,3,6,1,4,1,6141,2,13,1,1,8,1),_WwpEnvDoorState_Type())
wwpEnvDoorState.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpEnvDoorState.setStatus(_A)
class _WwpEnvDoorNotifEnabled_Type(TruthValue):defaultValue=1
_WwpEnvDoorNotifEnabled_Type.__name__=_F
_WwpEnvDoorNotifEnabled_Object=MibScalar
wwpEnvDoorNotifEnabled=_WwpEnvDoorNotifEnabled_Object((1,3,6,1,4,1,6141,2,13,1,1,8,2),_WwpEnvDoorNotifEnabled_Type())
wwpEnvDoorNotifEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpEnvDoorNotifEnabled.setStatus(_A)
_WwpEnvDryContactModule_ObjectIdentity=ObjectIdentity
wwpEnvDryContactModule=_WwpEnvDryContactModule_ObjectIdentity((1,3,6,1,4,1,6141,2,13,1,1,9))
class _WwpEnvDryContactOpenStateName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_WwpEnvDryContactOpenStateName_Type.__name__=_G
_WwpEnvDryContactOpenStateName_Object=MibScalar
wwpEnvDryContactOpenStateName=_WwpEnvDryContactOpenStateName_Object((1,3,6,1,4,1,6141,2,13,1,1,9,1),_WwpEnvDryContactOpenStateName_Type())
wwpEnvDryContactOpenStateName.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpEnvDryContactOpenStateName.setStatus(_A)
class _WwpEnvDryContactOpenStateChgAccumulate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_WwpEnvDryContactOpenStateChgAccumulate_Type.__name__=_C
_WwpEnvDryContactOpenStateChgAccumulate_Object=MibScalar
wwpEnvDryContactOpenStateChgAccumulate=_WwpEnvDryContactOpenStateChgAccumulate_Object((1,3,6,1,4,1,6141,2,13,1,1,9,2),_WwpEnvDryContactOpenStateChgAccumulate_Type())
wwpEnvDryContactOpenStateChgAccumulate.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpEnvDryContactOpenStateChgAccumulate.setStatus(_A)
_WwpEnvDryContactOpenStateCount_Type=Counter32
_WwpEnvDryContactOpenStateCount_Object=MibScalar
wwpEnvDryContactOpenStateCount=_WwpEnvDryContactOpenStateCount_Object((1,3,6,1,4,1,6141,2,13,1,1,9,3),_WwpEnvDryContactOpenStateCount_Type())
wwpEnvDryContactOpenStateCount.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpEnvDryContactOpenStateCount.setStatus(_A)
class _WwpEnvDryContactOpenStateNotifEnabled_Type(TruthValue):defaultValue=1
_WwpEnvDryContactOpenStateNotifEnabled_Type.__name__=_F
_WwpEnvDryContactOpenStateNotifEnabled_Object=MibScalar
wwpEnvDryContactOpenStateNotifEnabled=_WwpEnvDryContactOpenStateNotifEnabled_Object((1,3,6,1,4,1,6141,2,13,1,1,9,4),_WwpEnvDryContactOpenStateNotifEnabled_Type())
wwpEnvDryContactOpenStateNotifEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpEnvDryContactOpenStateNotifEnabled.setStatus(_A)
class _WwpEnvDryContactCloseStateName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_WwpEnvDryContactCloseStateName_Type.__name__=_G
_WwpEnvDryContactCloseStateName_Object=MibScalar
wwpEnvDryContactCloseStateName=_WwpEnvDryContactCloseStateName_Object((1,3,6,1,4,1,6141,2,13,1,1,9,5),_WwpEnvDryContactCloseStateName_Type())
wwpEnvDryContactCloseStateName.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpEnvDryContactCloseStateName.setStatus(_A)
class _WwpEnvDryContactCloseStateChgAccumulate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_WwpEnvDryContactCloseStateChgAccumulate_Type.__name__=_C
_WwpEnvDryContactCloseStateChgAccumulate_Object=MibScalar
wwpEnvDryContactCloseStateChgAccumulate=_WwpEnvDryContactCloseStateChgAccumulate_Object((1,3,6,1,4,1,6141,2,13,1,1,9,6),_WwpEnvDryContactCloseStateChgAccumulate_Type())
wwpEnvDryContactCloseStateChgAccumulate.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpEnvDryContactCloseStateChgAccumulate.setStatus(_A)
_WwpEnvDryContactCloseStateCount_Type=Counter32
_WwpEnvDryContactCloseStateCount_Object=MibScalar
wwpEnvDryContactCloseStateCount=_WwpEnvDryContactCloseStateCount_Object((1,3,6,1,4,1,6141,2,13,1,1,9,7),_WwpEnvDryContactCloseStateCount_Type())
wwpEnvDryContactCloseStateCount.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpEnvDryContactCloseStateCount.setStatus(_A)
class _WwpEnvDryContactCloseStateNotifEnabled_Type(TruthValue):defaultValue=1
_WwpEnvDryContactCloseStateNotifEnabled_Type.__name__=_F
_WwpEnvDryContactCloseStateNotifEnabled_Object=MibScalar
wwpEnvDryContactCloseStateNotifEnabled=_WwpEnvDryContactCloseStateNotifEnabled_Object((1,3,6,1,4,1,6141,2,13,1,1,9,8),_WwpEnvDryContactCloseStateNotifEnabled_Type())
wwpEnvDryContactCloseStateNotifEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpEnvDryContactCloseStateNotifEnabled.setStatus(_A)
_WwpEnvRFModule_ObjectIdentity=ObjectIdentity
wwpEnvRFModule=_WwpEnvRFModule_ObjectIdentity((1,3,6,1,4,1,6141,2,13,1,1,10))
class _WwpEnvRFModuleState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_WwpEnvRFModuleState_Type.__name__=_C
_WwpEnvRFModuleState_Object=MibScalar
wwpEnvRFModuleState=_WwpEnvRFModuleState_Object((1,3,6,1,4,1,6141,2,13,1,1,10,1),_WwpEnvRFModuleState_Type())
wwpEnvRFModuleState.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpEnvRFModuleState.setStatus(_A)
_WwpEnvRFModuleSignalDetect_Type=TruthValue
_WwpEnvRFModuleSignalDetect_Object=MibScalar
wwpEnvRFModuleSignalDetect=_WwpEnvRFModuleSignalDetect_Object((1,3,6,1,4,1,6141,2,13,1,1,10,2),_WwpEnvRFModuleSignalDetect_Type())
wwpEnvRFModuleSignalDetect.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpEnvRFModuleSignalDetect.setStatus(_A)
_WwpEnvironMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
wwpEnvironMIBNotificationPrefix=_WwpEnvironMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,6141,2,13,2))
_WwpEnvironMIBNotifications_ObjectIdentity=ObjectIdentity
wwpEnvironMIBNotifications=_WwpEnvironMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6141,2,13,2,0))
_WwpEnvironMIBConformance_ObjectIdentity=ObjectIdentity
wwpEnvironMIBConformance=_WwpEnvironMIBConformance_ObjectIdentity((1,3,6,1,4,1,6141,2,13,3))
_WwpEnvironMIBCompliances_ObjectIdentity=ObjectIdentity
wwpEnvironMIBCompliances=_WwpEnvironMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6141,2,13,3,1))
_WwpEnvironMIBGroups_ObjectIdentity=ObjectIdentity
wwpEnvironMIBGroups=_WwpEnvironMIBGroups_ObjectIdentity((1,3,6,1,4,1,6141,2,13,3,2))
wwpEnvPowerSupplyStatusNotification=NotificationType((1,3,6,1,4,1,6141,2,13,2,0,1))
wwpEnvPowerSupplyStatusNotification.setObjects(*((_E,_H),(_E,_V),(_E,_W)))
if mibBuilder.loadTexts:wwpEnvPowerSupplyStatusNotification.setStatus(_A)
wwpEnvFanModuleNotification=NotificationType((1,3,6,1,4,1,6141,2,13,2,0,2))
wwpEnvFanModuleNotification.setObjects(*((_E,_I),(_E,_X)))
if mibBuilder.loadTexts:wwpEnvFanModuleNotification.setStatus(_A)
wwpEnvTempNotification=NotificationType((1,3,6,1,4,1,6141,2,13,2,0,3))
wwpEnvTempNotification.setObjects(*((_E,_Y),(_E,_Z),(_E,_a),(_E,_b)))
if mibBuilder.loadTexts:wwpEnvTempNotification.setStatus(_A)
wwpEnvPowerSwitchNotification=NotificationType((1,3,6,1,4,1,6141,2,13,2,0,4))
wwpEnvPowerSwitchNotification.setObjects((_E,_c))
if mibBuilder.loadTexts:wwpEnvPowerSwitchNotification.setStatus(_A)
wwpEnvPortalBatteryStatusNotification=NotificationType((1,3,6,1,4,1,6141,2,13,2,0,5))
wwpEnvPortalBatteryStatusNotification.setObjects((_E,_d))
if mibBuilder.loadTexts:wwpEnvPortalBatteryStatusNotification.setStatus(_A)
wwpEnvPortalBatteryVoltageLevelNotification=NotificationType((1,3,6,1,4,1,6141,2,13,2,0,6))
wwpEnvPortalBatteryVoltageLevelNotification.setObjects((_E,_e))
if mibBuilder.loadTexts:wwpEnvPortalBatteryVoltageLevelNotification.setStatus(_A)
wwpEnvPortalBatteryConditionNotification=NotificationType((1,3,6,1,4,1,6141,2,13,2,0,7))
wwpEnvPortalBatteryConditionNotification.setObjects((_E,_f))
if mibBuilder.loadTexts:wwpEnvPortalBatteryConditionNotification.setStatus(_A)
wwpEnvPortalPowerSourceNotification=NotificationType((1,3,6,1,4,1,6141,2,13,2,0,8))
wwpEnvPortalPowerSourceNotification.setObjects((_E,_g))
if mibBuilder.loadTexts:wwpEnvPortalPowerSourceNotification.setStatus(_A)
wwpEnvDoorStateChgNotification=NotificationType((1,3,6,1,4,1,6141,2,13,2,0,9))
wwpEnvDoorStateChgNotification.setObjects((_E,_h))
if mibBuilder.loadTexts:wwpEnvDoorStateChgNotification.setStatus(_A)
wwpEnvDryContactOpenStateNotification=NotificationType((1,3,6,1,4,1,6141,2,13,2,0,10))
wwpEnvDryContactOpenStateNotification.setObjects(*((_E,_i),(_E,_j)))
if mibBuilder.loadTexts:wwpEnvDryContactOpenStateNotification.setStatus(_A)
wwpEnvDryContactCloseStateNotification=NotificationType((1,3,6,1,4,1,6141,2,13,2,0,11))
wwpEnvDryContactCloseStateNotification.setObjects(*((_E,_k),(_E,_l)))
if mibBuilder.loadTexts:wwpEnvDryContactCloseStateNotification.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'PortList':PortList,'wwpEnvironMIB':wwpEnvironMIB,'wwpEnvironMIBObjects':wwpEnvironMIBObjects,'wwpEnviron':wwpEnviron,'wwpEnvBatteryModule':wwpEnvBatteryModule,'wwpEnvBattStatus':wwpEnvBattStatus,'wwpEnvPowerSupplyModule':wwpEnvPowerSupplyModule,'wwpEnvPowerTable':wwpEnvPowerTable,'wwpEnvPowerEntry':wwpEnvPowerEntry,_H:wwpEnvPowerSupplyNum,_V:wwpEnvPowerSupplyState,_W:wwpEnvPowerSupplyType,'wwpEnvPowerSupplyRedundancy':wwpEnvPowerSupplyRedundancy,'wwpEnvRedPowerSupplyNotifEnabled':wwpEnvRedPowerSupplyNotifEnabled,'wwpEnvFanModule':wwpEnvFanModule,'wwpEnvFanModuleTable':wwpEnvFanModuleTable,'wwpEnvFanModuleEntry':wwpEnvFanModuleEntry,_I:wwpEnvFanModuleNum,_X:wwpEnvFanModuleState,'wwpEnvFanAvgSpeed':wwpEnvFanAvgSpeed,'wwpEnvFanCurrentSpeed':wwpEnvFanCurrentSpeed,'wwpEnvFanMinSpeed':wwpEnvFanMinSpeed,'wwpEnvFanModuleNotifEnabled':wwpEnvFanModuleNotifEnabled,'wwpEnvTempSensor':wwpEnvTempSensor,'wwpEnvTempSensorTable':wwpEnvTempSensorTable,'wwpEnvTempSensorEntry':wwpEnvTempSensorEntry,_S:wwpEnvTempSensorNum,_Z:wwpEnvTempSensorValue,_a:wwpEnvTempSensorHighThreshold,_b:wwpEnvTempSensorLowThreshold,_Y:wwpEnvTempSensorState,'wwpEnvTempNotifEnabled':wwpEnvTempNotifEnabled,'wwpEnvPortPowerMgmt':wwpEnvPortPowerMgmt,'wwpPortPowerMgmtTable':wwpPortPowerMgmtTable,'wwpPortPowerMgmtEntry':wwpPortPowerMgmtEntry,_U:wwpEnvPortBankId,'wwpEnvPortMap':wwpEnvPortMap,'wwpEnvPortBankOn':wwpEnvPortBankOn,'wwpEnvNotif':wwpEnvNotif,_c:wwpPowerSwitchingOp,'wwpEnvPortalBatteryModule':wwpEnvPortalBatteryModule,_d:wwpEnvPortalBatteryStatus,_e:wwpEnvPortalBatteryVoltageLevel,_f:wwpEnvPortalBatteryCondition,_g:wwpEnvPortalPowerSource,'wwpEnvBatteryNormalStateName':wwpEnvBatteryNormalStateName,'wwpEnvBatteryLowStateName':wwpEnvBatteryLowStateName,'wwpEnvBatteryGoodStateName':wwpEnvBatteryGoodStateName,'wwpEnvBatteryBadStateName':wwpEnvBatteryBadStateName,'wwpEnvBatteryPresentStateName':wwpEnvBatteryPresentStateName,'wwpEnvBatteryMissingStateName':wwpEnvBatteryMissingStateName,'wwpEnvBatteryPowerPrimaryStateName':wwpEnvBatteryPowerPrimaryStateName,'wwpEnvBatteryPowerBatteryStateName':wwpEnvBatteryPowerBatteryStateName,'wwpEnvBatteryLowStateNotifEnabled':wwpEnvBatteryLowStateNotifEnabled,'wwpEnvBatteryBadStateNotifEnabled':wwpEnvBatteryBadStateNotifEnabled,'wwpEnvBatteryMissingStateNotifEnabled':wwpEnvBatteryMissingStateNotifEnabled,'wwpEnvBatteryPowerNotifEnabled':wwpEnvBatteryPowerNotifEnabled,'wwpEnvBatteryPeriodicTrapsTimer':wwpEnvBatteryPeriodicTrapsTimer,'wwpEnvBatteryPowerUpTrapsEnable':wwpEnvBatteryPowerUpTrapsEnable,'wwpEnvDoorModule':wwpEnvDoorModule,_h:wwpEnvDoorState,'wwpEnvDoorNotifEnabled':wwpEnvDoorNotifEnabled,'wwpEnvDryContactModule':wwpEnvDryContactModule,_i:wwpEnvDryContactOpenStateName,'wwpEnvDryContactOpenStateChgAccumulate':wwpEnvDryContactOpenStateChgAccumulate,_j:wwpEnvDryContactOpenStateCount,'wwpEnvDryContactOpenStateNotifEnabled':wwpEnvDryContactOpenStateNotifEnabled,_k:wwpEnvDryContactCloseStateName,'wwpEnvDryContactCloseStateChgAccumulate':wwpEnvDryContactCloseStateChgAccumulate,_l:wwpEnvDryContactCloseStateCount,'wwpEnvDryContactCloseStateNotifEnabled':wwpEnvDryContactCloseStateNotifEnabled,'wwpEnvRFModule':wwpEnvRFModule,'wwpEnvRFModuleState':wwpEnvRFModuleState,'wwpEnvRFModuleSignalDetect':wwpEnvRFModuleSignalDetect,'wwpEnvironMIBNotificationPrefix':wwpEnvironMIBNotificationPrefix,'wwpEnvironMIBNotifications':wwpEnvironMIBNotifications,'wwpEnvPowerSupplyStatusNotification':wwpEnvPowerSupplyStatusNotification,'wwpEnvFanModuleNotification':wwpEnvFanModuleNotification,'wwpEnvTempNotification':wwpEnvTempNotification,'wwpEnvPowerSwitchNotification':wwpEnvPowerSwitchNotification,'wwpEnvPortalBatteryStatusNotification':wwpEnvPortalBatteryStatusNotification,'wwpEnvPortalBatteryVoltageLevelNotification':wwpEnvPortalBatteryVoltageLevelNotification,'wwpEnvPortalBatteryConditionNotification':wwpEnvPortalBatteryConditionNotification,'wwpEnvPortalPowerSourceNotification':wwpEnvPortalPowerSourceNotification,'wwpEnvDoorStateChgNotification':wwpEnvDoorStateChgNotification,'wwpEnvDryContactOpenStateNotification':wwpEnvDryContactOpenStateNotification,'wwpEnvDryContactCloseStateNotification':wwpEnvDryContactCloseStateNotification,'wwpEnvironMIBConformance':wwpEnvironMIBConformance,'wwpEnvironMIBCompliances':wwpEnvironMIBCompliances,'wwpEnvironMIBGroups':wwpEnvironMIBGroups})