_A2='mgreceptacleShutdownDuration'
_A1='upsmgConfigSysShutDuration'
_A0='mgreceptacleShutoffTimer'
_z='mgreceptacleBootUpDuration'
_y='mgreceptacleRestartDelay'
_x='default'
_w='saterday'
_v='friday'
_u='thursday'
_t='wednesday'
_s='tuesday'
_r='monday'
_q='sunday'
_p='mgreceptacleIndexc'
_o='closed'
_n='upsmgEnvironmentIndex'
_m='mgsensorNum'
_l='mgalarmNum'
_k='mgoutputPhaseIndex'
_j='mginputIndex'
_i='upsmgConfigSensorIndex'
_h='mgcontrolDayIndex'
_g='mgreceptacleIndexb'
_f='mgdeviceIndex'
_e='mgmanagerIndex'
_d='NotificationType'
_c='mgextAlarmUID'
_b='mgreceptacleToggleDuration'
_a='mgreceptacleToggleDelay'
_Z='completed'
_Y='inprogressinups'
_X='started'
_W='stop'
_V='schedule'
_U='last'
_T='off'
_S='other'
_R='mgreceptacleOffDelay'
_Q='mgreceptacleOnDelay'
_P='mgextAlarmIndex'
_O='mgreceptacleState'
_N='start'
_M='nothing'
_L='upsmgBatteryLevel'
_K='upsmgBatteryRemainingTime'
_J='none'
_I='mgreceptacleIndex'
_H='DisplayString'
_G='yes'
_F='no'
_E='MG-SNMP-UPS-MIB'
_D='Integer32'
_C='read-only'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier',_d,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_d,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','TextualConvention')
_MerlinGerin_ObjectIdentity=ObjectIdentity
merlinGerin=_MerlinGerin_ObjectIdentity((1,3,6,1,4,1,705))
_Upsmg_ObjectIdentity=ObjectIdentity
upsmg=_Upsmg_ObjectIdentity((1,3,6,1,4,1,705,1))
_UpsmgIdent_ObjectIdentity=ObjectIdentity
upsmgIdent=_UpsmgIdent_ObjectIdentity((1,3,6,1,4,1,705,1,1))
class _UpsmgIdentFamilyName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_UpsmgIdentFamilyName_Type.__name__=_H
_UpsmgIdentFamilyName_Object=MibScalar
upsmgIdentFamilyName=_UpsmgIdentFamilyName_Object((1,3,6,1,4,1,705,1,1,1),_UpsmgIdentFamilyName_Type())
upsmgIdentFamilyName.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgIdentFamilyName.setStatus(_A)
class _UpsmgIdentModelName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_UpsmgIdentModelName_Type.__name__=_H
_UpsmgIdentModelName_Object=MibScalar
upsmgIdentModelName=_UpsmgIdentModelName_Object((1,3,6,1,4,1,705,1,1,2),_UpsmgIdentModelName_Type())
upsmgIdentModelName.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgIdentModelName.setStatus(_A)
class _UpsmgIdentRevisionLevel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_UpsmgIdentRevisionLevel_Type.__name__=_H
_UpsmgIdentRevisionLevel_Object=MibScalar
upsmgIdentRevisionLevel=_UpsmgIdentRevisionLevel_Object((1,3,6,1,4,1,705,1,1,3),_UpsmgIdentRevisionLevel_Type())
upsmgIdentRevisionLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgIdentRevisionLevel.setStatus(_A)
class _UpsmgIdentFirmwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_UpsmgIdentFirmwareVersion_Type.__name__=_H
_UpsmgIdentFirmwareVersion_Object=MibScalar
upsmgIdentFirmwareVersion=_UpsmgIdentFirmwareVersion_Object((1,3,6,1,4,1,705,1,1,4),_UpsmgIdentFirmwareVersion_Type())
upsmgIdentFirmwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgIdentFirmwareVersion.setStatus(_A)
class _UpsmgIdentUserID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_UpsmgIdentUserID_Type.__name__=_H
_UpsmgIdentUserID_Object=MibScalar
upsmgIdentUserID=_UpsmgIdentUserID_Object((1,3,6,1,4,1,705,1,1,5),_UpsmgIdentUserID_Type())
upsmgIdentUserID.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgIdentUserID.setStatus(_A)
class _UpsmgIdentInstallationDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_UpsmgIdentInstallationDate_Type.__name__=_H
_UpsmgIdentInstallationDate_Object=MibScalar
upsmgIdentInstallationDate=_UpsmgIdentInstallationDate_Object((1,3,6,1,4,1,705,1,1,6),_UpsmgIdentInstallationDate_Type())
upsmgIdentInstallationDate.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgIdentInstallationDate.setStatus(_A)
class _UpsmgIdentSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_UpsmgIdentSerialNumber_Type.__name__=_H
_UpsmgIdentSerialNumber_Object=MibScalar
upsmgIdentSerialNumber=_UpsmgIdentSerialNumber_Object((1,3,6,1,4,1,705,1,1,7),_UpsmgIdentSerialNumber_Type())
upsmgIdentSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgIdentSerialNumber.setStatus(_A)
_UpsmgManagement_ObjectIdentity=ObjectIdentity
upsmgManagement=_UpsmgManagement_ObjectIdentity((1,3,6,1,4,1,705,1,2))
_UpsmgManagersNum_Type=Integer32
_UpsmgManagersNum_Object=MibScalar
upsmgManagersNum=_UpsmgManagersNum_Object((1,3,6,1,4,1,705,1,2,1),_UpsmgManagersNum_Type())
upsmgManagersNum.setMaxAccess(_C)
if mibBuilder.loadTexts:upsmgManagersNum.setStatus(_A)
_UpsmgManagersTable_Object=MibTable
upsmgManagersTable=_UpsmgManagersTable_Object((1,3,6,1,4,1,705,1,2,2))
if mibBuilder.loadTexts:upsmgManagersTable.setStatus(_A)
_UpsmgManagersEntry_Object=MibTableRow
upsmgManagersEntry=_UpsmgManagersEntry_Object((1,3,6,1,4,1,705,1,2,2,1))
upsmgManagersEntry.setIndexNames((0,_E,_e))
if mibBuilder.loadTexts:upsmgManagersEntry.setStatus(_A)
class _MgmanagerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_MgmanagerIndex_Type.__name__=_D
_MgmanagerIndex_Object=MibTableColumn
mgmanagerIndex=_MgmanagerIndex_Object((1,3,6,1,4,1,705,1,2,2,1,1),_MgmanagerIndex_Type())
mgmanagerIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:mgmanagerIndex.setStatus(_A)
_MgmanagerDeviceNumber_Type=Integer32
_MgmanagerDeviceNumber_Object=MibTableColumn
mgmanagerDeviceNumber=_MgmanagerDeviceNumber_Object((1,3,6,1,4,1,705,1,2,2,1,2),_MgmanagerDeviceNumber_Type())
mgmanagerDeviceNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:mgmanagerDeviceNumber.setStatus(_A)
class _MgmanagerNMSType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('umclient',1),('decnetview',2),('umview',3),('dview',4),('hpopenview',5),('sunnetmanager',6),('novellnms',7),('ibmnetview',8),(_S,9),('autolearning',10)))
_MgmanagerNMSType_Type.__name__=_D
_MgmanagerNMSType_Object=MibTableColumn
mgmanagerNMSType=_MgmanagerNMSType_Object((1,3,6,1,4,1,705,1,2,2,1,3),_MgmanagerNMSType_Type())
mgmanagerNMSType.setMaxAccess(_B)
if mibBuilder.loadTexts:mgmanagerNMSType.setStatus(_A)
class _MgmanagerCommType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_S,1),('invalid',2),('cmip',3),('snmpv1',4),('snmpv2',5)))
_MgmanagerCommType_Type.__name__=_D
_MgmanagerCommType_Object=MibTableColumn
mgmanagerCommType=_MgmanagerCommType_Object((1,3,6,1,4,1,705,1,2,2,1,4),_MgmanagerCommType_Type())
mgmanagerCommType.setMaxAccess(_B)
if mibBuilder.loadTexts:mgmanagerCommType.setStatus(_A)
class _MgmanagerDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_MgmanagerDescr_Type.__name__=_H
_MgmanagerDescr_Object=MibTableColumn
mgmanagerDescr=_MgmanagerDescr_Object((1,3,6,1,4,1,705,1,2,2,1,5),_MgmanagerDescr_Type())
mgmanagerDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:mgmanagerDescr.setStatus(_A)
_MgmanagerAddress_Type=IpAddress
_MgmanagerAddress_Object=MibTableColumn
mgmanagerAddress=_MgmanagerAddress_Object((1,3,6,1,4,1,705,1,2,2,1,6),_MgmanagerAddress_Type())
mgmanagerAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:mgmanagerAddress.setStatus(_A)
class _MgmanagerCommunity_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_MgmanagerCommunity_Type.__name__=_H
_MgmanagerCommunity_Object=MibTableColumn
mgmanagerCommunity=_MgmanagerCommunity_Object((1,3,6,1,4,1,705,1,2,2,1,7),_MgmanagerCommunity_Type())
mgmanagerCommunity.setMaxAccess(_B)
if mibBuilder.loadTexts:mgmanagerCommunity.setStatus(_A)
_MgmanagerSeverityLevel_Type=Integer32
_MgmanagerSeverityLevel_Object=MibTableColumn
mgmanagerSeverityLevel=_MgmanagerSeverityLevel_Object((1,3,6,1,4,1,705,1,2,2,1,8),_MgmanagerSeverityLevel_Type())
mgmanagerSeverityLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:mgmanagerSeverityLevel.setStatus(_A)
class _MgmanagerTrapAck_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('mgack',1),('mgnoack',2),('stdnomg',3),('mgacks',4),('cpqnoack',5)))
_MgmanagerTrapAck_Type.__name__=_D
_MgmanagerTrapAck_Object=MibTableColumn
mgmanagerTrapAck=_MgmanagerTrapAck_Object((1,3,6,1,4,1,705,1,2,2,1,9),_MgmanagerTrapAck_Type())
mgmanagerTrapAck.setMaxAccess(_B)
if mibBuilder.loadTexts:mgmanagerTrapAck.setStatus(_A)
_UpsmgReceptacle_ObjectIdentity=ObjectIdentity
upsmgReceptacle=_UpsmgReceptacle_ObjectIdentity((1,3,6,1,4,1,705,1,3))
_UpsmgReceptaclesNum_Type=Integer32
_UpsmgReceptaclesNum_Object=MibScalar
upsmgReceptaclesNum=_UpsmgReceptaclesNum_Object((1,3,6,1,4,1,705,1,3,1),_UpsmgReceptaclesNum_Type())
upsmgReceptaclesNum.setMaxAccess(_C)
if mibBuilder.loadTexts:upsmgReceptaclesNum.setStatus(_A)
_UpsmgReceptaclesTable_Object=MibTable
upsmgReceptaclesTable=_UpsmgReceptaclesTable_Object((1,3,6,1,4,1,705,1,3,2))
if mibBuilder.loadTexts:upsmgReceptaclesTable.setStatus(_A)
_UpsmgReceptaclesEntry_Object=MibTableRow
upsmgReceptaclesEntry=_UpsmgReceptaclesEntry_Object((1,3,6,1,4,1,705,1,3,2,1))
upsmgReceptaclesEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:upsmgReceptaclesEntry.setStatus(_A)
class _MgreceptacleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_MgreceptacleIndex_Type.__name__=_D
_MgreceptacleIndex_Object=MibTableColumn
mgreceptacleIndex=_MgreceptacleIndex_Object((1,3,6,1,4,1,705,1,3,2,1,1),_MgreceptacleIndex_Type())
mgreceptacleIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:mgreceptacleIndex.setStatus(_A)
_MgreceptacleLevel_Type=Integer32
_MgreceptacleLevel_Object=MibTableColumn
mgreceptacleLevel=_MgreceptacleLevel_Object((1,3,6,1,4,1,705,1,3,2,1,2),_MgreceptacleLevel_Type())
mgreceptacleLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:mgreceptacleLevel.setStatus(_A)
class _MgreceptacleType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_MgreceptacleType_Type.__name__=_H
_MgreceptacleType_Object=MibTableColumn
mgreceptacleType=_MgreceptacleType_Object((1,3,6,1,4,1,705,1,3,2,1,3),_MgreceptacleType_Type())
mgreceptacleType.setMaxAccess(_B)
if mibBuilder.loadTexts:mgreceptacleType.setStatus(_A)
class _MgreceptacleIdent_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_MgreceptacleIdent_Type.__name__=_H
_MgreceptacleIdent_Object=MibTableColumn
mgreceptacleIdent=_MgreceptacleIdent_Object((1,3,6,1,4,1,705,1,3,2,1,4),_MgreceptacleIdent_Type())
mgreceptacleIdent.setMaxAccess(_B)
if mibBuilder.loadTexts:mgreceptacleIdent.setStatus(_A)
class _MgreceptacleState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('manualON',1),('manualOFF',2),('normalON',3),('normalOFF',4),('controlON',5),('controlOFF',6),('scheduleON',7),('scheduleOFF',8)))
_MgreceptacleState_Type.__name__=_D
_MgreceptacleState_Object=MibTableColumn
mgreceptacleState=_MgreceptacleState_Object((1,3,6,1,4,1,705,1,3,2,1,5),_MgreceptacleState_Type())
mgreceptacleState.setMaxAccess(_C)
if mibBuilder.loadTexts:mgreceptacleState.setStatus(_A)
_MgreceptacleReceptacle_Type=Integer32
_MgreceptacleReceptacle_Object=MibTableColumn
mgreceptacleReceptacle=_MgreceptacleReceptacle_Object((1,3,6,1,4,1,705,1,3,2,1,6),_MgreceptacleReceptacle_Type())
mgreceptacleReceptacle.setMaxAccess(_B)
if mibBuilder.loadTexts:mgreceptacleReceptacle.setStatus(_A)
_MgreceptaclePowerCons_Type=Integer32
_MgreceptaclePowerCons_Object=MibTableColumn
mgreceptaclePowerCons=_MgreceptaclePowerCons_Object((1,3,6,1,4,1,705,1,3,2,1,7),_MgreceptaclePowerCons_Type())
mgreceptaclePowerCons.setMaxAccess(_B)
if mibBuilder.loadTexts:mgreceptaclePowerCons.setStatus(_A)
_MgreceptacleOverload_Type=Integer32
_MgreceptacleOverload_Object=MibTableColumn
mgreceptacleOverload=_MgreceptacleOverload_Object((1,3,6,1,4,1,705,1,3,2,1,8),_MgreceptacleOverload_Type())
mgreceptacleOverload.setMaxAccess(_B)
if mibBuilder.loadTexts:mgreceptacleOverload.setStatus(_A)
_MgreceptacleAutonomy_Type=Integer32
_MgreceptacleAutonomy_Object=MibTableColumn
mgreceptacleAutonomy=_MgreceptacleAutonomy_Object((1,3,6,1,4,1,705,1,3,2,1,9),_MgreceptacleAutonomy_Type())
mgreceptacleAutonomy.setMaxAccess(_B)
if mibBuilder.loadTexts:mgreceptacleAutonomy.setStatus(_A)
_UpsmgConfig_ObjectIdentity=ObjectIdentity
upsmgConfig=_UpsmgConfig_ObjectIdentity((1,3,6,1,4,1,705,1,4))
class _UpsmgConfigBatteryInstalled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_UpsmgConfigBatteryInstalled_Type.__name__=_D
_UpsmgConfigBatteryInstalled_Object=MibScalar
upsmgConfigBatteryInstalled=_UpsmgConfigBatteryInstalled_Object((1,3,6,1,4,1,705,1,4,1),_UpsmgConfigBatteryInstalled_Type())
upsmgConfigBatteryInstalled.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgConfigBatteryInstalled.setStatus(_A)
_UpsmgConfigNominalBatteryVoltage_Type=Integer32
_UpsmgConfigNominalBatteryVoltage_Object=MibScalar
upsmgConfigNominalBatteryVoltage=_UpsmgConfigNominalBatteryVoltage_Object((1,3,6,1,4,1,705,1,4,2),_UpsmgConfigNominalBatteryVoltage_Type())
upsmgConfigNominalBatteryVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgConfigNominalBatteryVoltage.setStatus(_A)
_UpsmgConfigNominalBatteryTime_Type=Integer32
_UpsmgConfigNominalBatteryTime_Object=MibScalar
upsmgConfigNominalBatteryTime=_UpsmgConfigNominalBatteryTime_Object((1,3,6,1,4,1,705,1,4,3),_UpsmgConfigNominalBatteryTime_Type())
upsmgConfigNominalBatteryTime.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgConfigNominalBatteryTime.setStatus(_A)
_UpsmgConfigNominalRechargeTime_Type=Integer32
_UpsmgConfigNominalRechargeTime_Object=MibScalar
upsmgConfigNominalRechargeTime=_UpsmgConfigNominalRechargeTime_Object((1,3,6,1,4,1,705,1,4,4),_UpsmgConfigNominalRechargeTime_Type())
upsmgConfigNominalRechargeTime.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgConfigNominalRechargeTime.setStatus(_A)
_UpsmgConfigMinRechargeLevel_Type=Integer32
_UpsmgConfigMinRechargeLevel_Object=MibScalar
upsmgConfigMinRechargeLevel=_UpsmgConfigMinRechargeLevel_Object((1,3,6,1,4,1,705,1,4,5),_UpsmgConfigMinRechargeLevel_Type())
upsmgConfigMinRechargeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgConfigMinRechargeLevel.setStatus(_A)
_UpsmgConfigMaxRechargeTime_Type=Integer32
_UpsmgConfigMaxRechargeTime_Object=MibScalar
upsmgConfigMaxRechargeTime=_UpsmgConfigMaxRechargeTime_Object((1,3,6,1,4,1,705,1,4,6),_UpsmgConfigMaxRechargeTime_Type())
upsmgConfigMaxRechargeTime.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgConfigMaxRechargeTime.setStatus(_A)
_UpsmgConfigLowBatteryTime_Type=Integer32
_UpsmgConfigLowBatteryTime_Object=MibScalar
upsmgConfigLowBatteryTime=_UpsmgConfigLowBatteryTime_Object((1,3,6,1,4,1,705,1,4,7),_UpsmgConfigLowBatteryTime_Type())
upsmgConfigLowBatteryTime.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgConfigLowBatteryTime.setStatus(_A)
_UpsmgConfigLowBatteryLevel_Type=Integer32
_UpsmgConfigLowBatteryLevel_Object=MibScalar
upsmgConfigLowBatteryLevel=_UpsmgConfigLowBatteryLevel_Object((1,3,6,1,4,1,705,1,4,8),_UpsmgConfigLowBatteryLevel_Type())
upsmgConfigLowBatteryLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgConfigLowBatteryLevel.setStatus(_A)
class _UpsmgConfigAutoRestart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('always',1),('never',2),('onmain',3)))
_UpsmgConfigAutoRestart_Type.__name__=_D
_UpsmgConfigAutoRestart_Object=MibScalar
upsmgConfigAutoRestart=_UpsmgConfigAutoRestart_Object((1,3,6,1,4,1,705,1,4,9),_UpsmgConfigAutoRestart_Type())
upsmgConfigAutoRestart.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgConfigAutoRestart.setStatus(_A)
_UpsmgConfigShutdownTimer_Type=Integer32
_UpsmgConfigShutdownTimer_Object=MibScalar
upsmgConfigShutdownTimer=_UpsmgConfigShutdownTimer_Object((1,3,6,1,4,1,705,1,4,10),_UpsmgConfigShutdownTimer_Type())
upsmgConfigShutdownTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgConfigShutdownTimer.setStatus(_A)
_UpsmgConfigSysShutDuration_Type=Integer32
_UpsmgConfigSysShutDuration_Object=MibScalar
upsmgConfigSysShutDuration=_UpsmgConfigSysShutDuration_Object((1,3,6,1,4,1,705,1,4,11),_UpsmgConfigSysShutDuration_Type())
upsmgConfigSysShutDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgConfigSysShutDuration.setStatus(_A)
_UpsmgConfigVARating_Type=Integer32
_UpsmgConfigVARating_Object=MibScalar
upsmgConfigVARating=_UpsmgConfigVARating_Object((1,3,6,1,4,1,705,1,4,12),_UpsmgConfigVARating_Type())
upsmgConfigVARating.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgConfigVARating.setStatus(_A)
_UpsmgConfigLowTransfer_Type=Integer32
_UpsmgConfigLowTransfer_Object=MibScalar
upsmgConfigLowTransfer=_UpsmgConfigLowTransfer_Object((1,3,6,1,4,1,705,1,4,13),_UpsmgConfigLowTransfer_Type())
upsmgConfigLowTransfer.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgConfigLowTransfer.setStatus(_A)
_UpsmgConfigHighTransfer_Type=Integer32
_UpsmgConfigHighTransfer_Object=MibScalar
upsmgConfigHighTransfer=_UpsmgConfigHighTransfer_Object((1,3,6,1,4,1,705,1,4,14),_UpsmgConfigHighTransfer_Type())
upsmgConfigHighTransfer.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgConfigHighTransfer.setStatus(_A)
_UpsmgConfigOutputNominalVoltage_Type=Integer32
_UpsmgConfigOutputNominalVoltage_Object=MibScalar
upsmgConfigOutputNominalVoltage=_UpsmgConfigOutputNominalVoltage_Object((1,3,6,1,4,1,705,1,4,15),_UpsmgConfigOutputNominalVoltage_Type())
upsmgConfigOutputNominalVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgConfigOutputNominalVoltage.setStatus(_A)
_UpsmgConfigOutputNominalCurrent_Type=Integer32
_UpsmgConfigOutputNominalCurrent_Object=MibScalar
upsmgConfigOutputNominalCurrent=_UpsmgConfigOutputNominalCurrent_Object((1,3,6,1,4,1,705,1,4,16),_UpsmgConfigOutputNominalCurrent_Type())
upsmgConfigOutputNominalCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgConfigOutputNominalCurrent.setStatus(_A)
_UpsmgConfigOutputNomFrequency_Type=Integer32
_UpsmgConfigOutputNomFrequency_Object=MibScalar
upsmgConfigOutputNomFrequency=_UpsmgConfigOutputNomFrequency_Object((1,3,6,1,4,1,705,1,4,17),_UpsmgConfigOutputNomFrequency_Type())
upsmgConfigOutputNomFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgConfigOutputNomFrequency.setStatus(_A)
class _UpsmgConfigByPassType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),('relay',2),('static',3)))
_UpsmgConfigByPassType_Type.__name__=_D
_UpsmgConfigByPassType_Object=MibScalar
upsmgConfigByPassType=_UpsmgConfigByPassType_Object((1,3,6,1,4,1,705,1,4,18),_UpsmgConfigByPassType_Type())
upsmgConfigByPassType.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgConfigByPassType.setStatus(_A)
class _UpsmgConfigAlarmAudible_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_UpsmgConfigAlarmAudible_Type.__name__=_D
_UpsmgConfigAlarmAudible_Object=MibScalar
upsmgConfigAlarmAudible=_UpsmgConfigAlarmAudible_Object((1,3,6,1,4,1,705,1,4,19),_UpsmgConfigAlarmAudible_Type())
upsmgConfigAlarmAudible.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgConfigAlarmAudible.setStatus(_A)
_UpsmgConfigAlarmTimeDelay_Type=Integer32
_UpsmgConfigAlarmTimeDelay_Object=MibScalar
upsmgConfigAlarmTimeDelay=_UpsmgConfigAlarmTimeDelay_Object((1,3,6,1,4,1,705,1,4,20),_UpsmgConfigAlarmTimeDelay_Type())
upsmgConfigAlarmTimeDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgConfigAlarmTimeDelay.setStatus(_A)
_UpsmgConfigDevicesNum_Type=Integer32
_UpsmgConfigDevicesNum_Object=MibScalar
upsmgConfigDevicesNum=_UpsmgConfigDevicesNum_Object((1,3,6,1,4,1,705,1,4,21),_UpsmgConfigDevicesNum_Type())
upsmgConfigDevicesNum.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgConfigDevicesNum.setStatus(_A)
_UpsmgConfigDevicesTable_Object=MibTable
upsmgConfigDevicesTable=_UpsmgConfigDevicesTable_Object((1,3,6,1,4,1,705,1,4,22))
if mibBuilder.loadTexts:upsmgConfigDevicesTable.setStatus(_A)
_UpsmgConfigDevicesEntry_Object=MibTableRow
upsmgConfigDevicesEntry=_UpsmgConfigDevicesEntry_Object((1,3,6,1,4,1,705,1,4,22,1))
upsmgConfigDevicesEntry.setIndexNames((0,_E,_f))
if mibBuilder.loadTexts:upsmgConfigDevicesEntry.setStatus(_A)
class _MgdeviceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_MgdeviceIndex_Type.__name__=_D
_MgdeviceIndex_Object=MibTableColumn
mgdeviceIndex=_MgdeviceIndex_Object((1,3,6,1,4,1,705,1,4,22,1,1),_MgdeviceIndex_Type())
mgdeviceIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:mgdeviceIndex.setStatus(_A)
_MgdeviceReceptacleNum_Type=Integer32
_MgdeviceReceptacleNum_Object=MibTableColumn
mgdeviceReceptacleNum=_MgdeviceReceptacleNum_Object((1,3,6,1,4,1,705,1,4,22,1,2),_MgdeviceReceptacleNum_Type())
mgdeviceReceptacleNum.setMaxAccess(_B)
if mibBuilder.loadTexts:mgdeviceReceptacleNum.setStatus(_A)
class _MgdeviceIdent_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_MgdeviceIdent_Type.__name__=_H
_MgdeviceIdent_Object=MibTableColumn
mgdeviceIdent=_MgdeviceIdent_Object((1,3,6,1,4,1,705,1,4,22,1,3),_MgdeviceIdent_Type())
mgdeviceIdent.setMaxAccess(_B)
if mibBuilder.loadTexts:mgdeviceIdent.setStatus(_A)
_MgdeviceVaRating_Type=Integer32
_MgdeviceVaRating_Object=MibTableColumn
mgdeviceVaRating=_MgdeviceVaRating_Object((1,3,6,1,4,1,705,1,4,22,1,4),_MgdeviceVaRating_Type())
mgdeviceVaRating.setMaxAccess(_B)
if mibBuilder.loadTexts:mgdeviceVaRating.setStatus(_A)
_MgdeviceSequenceOff_Type=Integer32
_MgdeviceSequenceOff_Object=MibTableColumn
mgdeviceSequenceOff=_MgdeviceSequenceOff_Object((1,3,6,1,4,1,705,1,4,22,1,5),_MgdeviceSequenceOff_Type())
mgdeviceSequenceOff.setMaxAccess(_B)
if mibBuilder.loadTexts:mgdeviceSequenceOff.setStatus(_A)
_MgdeviceSequenceOn_Type=Integer32
_MgdeviceSequenceOn_Object=MibTableColumn
mgdeviceSequenceOn=_MgdeviceSequenceOn_Object((1,3,6,1,4,1,705,1,4,22,1,6),_MgdeviceSequenceOn_Type())
mgdeviceSequenceOn.setMaxAccess(_B)
if mibBuilder.loadTexts:mgdeviceSequenceOn.setStatus(_A)
_MgdeviceShutdownDuration_Type=Integer32
_MgdeviceShutdownDuration_Object=MibTableColumn
mgdeviceShutdownDuration=_MgdeviceShutdownDuration_Object((1,3,6,1,4,1,705,1,4,22,1,7),_MgdeviceShutdownDuration_Type())
mgdeviceShutdownDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:mgdeviceShutdownDuration.setStatus(_A)
_MgdeviceBootUpDuration_Type=Integer32
_MgdeviceBootUpDuration_Object=MibTableColumn
mgdeviceBootUpDuration=_MgdeviceBootUpDuration_Object((1,3,6,1,4,1,705,1,4,22,1,8),_MgdeviceBootUpDuration_Type())
mgdeviceBootUpDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:mgdeviceBootUpDuration.setStatus(_A)
_UpsmgConfigReceptaclesTable_Object=MibTable
upsmgConfigReceptaclesTable=_UpsmgConfigReceptaclesTable_Object((1,3,6,1,4,1,705,1,4,23))
if mibBuilder.loadTexts:upsmgConfigReceptaclesTable.setStatus(_A)
_UpsmgConfigReceptaclesEntry_Object=MibTableRow
upsmgConfigReceptaclesEntry=_UpsmgConfigReceptaclesEntry_Object((1,3,6,1,4,1,705,1,4,23,1))
upsmgConfigReceptaclesEntry.setIndexNames((0,_E,_g))
if mibBuilder.loadTexts:upsmgConfigReceptaclesEntry.setStatus(_A)
class _MgreceptacleIndexb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_MgreceptacleIndexb_Type.__name__=_D
_MgreceptacleIndexb_Object=MibTableColumn
mgreceptacleIndexb=_MgreceptacleIndexb_Object((1,3,6,1,4,1,705,1,4,23,1,1),_MgreceptacleIndexb_Type())
mgreceptacleIndexb.setMaxAccess(_C)
if mibBuilder.loadTexts:mgreceptacleIndexb.setStatus(_A)
class _MgreceptacleStateTurnOn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('on',1),(_T,2),(_U,3),(_V,4)))
_MgreceptacleStateTurnOn_Type.__name__=_D
_MgreceptacleStateTurnOn_Object=MibTableColumn
mgreceptacleStateTurnOn=_MgreceptacleStateTurnOn_Object((1,3,6,1,4,1,705,1,4,23,1,2),_MgreceptacleStateTurnOn_Type())
mgreceptacleStateTurnOn.setMaxAccess(_B)
if mibBuilder.loadTexts:mgreceptacleStateTurnOn.setStatus(_A)
class _MgreceptacleStateMainReturn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('on',1),(_T,2),(_U,3),(_V,4)))
_MgreceptacleStateMainReturn_Type.__name__=_D
_MgreceptacleStateMainReturn_Object=MibTableColumn
mgreceptacleStateMainReturn=_MgreceptacleStateMainReturn_Object((1,3,6,1,4,1,705,1,4,23,1,3),_MgreceptacleStateMainReturn_Type())
mgreceptacleStateMainReturn.setMaxAccess(_B)
if mibBuilder.loadTexts:mgreceptacleStateMainReturn.setStatus(_A)
class _MgreceptacleStateDischarge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('on',1),(_T,2),(_U,3),(_V,4)))
_MgreceptacleStateDischarge_Type.__name__=_D
_MgreceptacleStateDischarge_Object=MibTableColumn
mgreceptacleStateDischarge=_MgreceptacleStateDischarge_Object((1,3,6,1,4,1,705,1,4,23,1,4),_MgreceptacleStateDischarge_Type())
mgreceptacleStateDischarge.setMaxAccess(_B)
if mibBuilder.loadTexts:mgreceptacleStateDischarge.setStatus(_A)
_MgreceptacleShutoffLevel_Type=Integer32
_MgreceptacleShutoffLevel_Object=MibTableColumn
mgreceptacleShutoffLevel=_MgreceptacleShutoffLevel_Object((1,3,6,1,4,1,705,1,4,23,1,5),_MgreceptacleShutoffLevel_Type())
mgreceptacleShutoffLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:mgreceptacleShutoffLevel.setStatus(_A)
_MgreceptacleShutoffTimer_Type=Integer32
_MgreceptacleShutoffTimer_Object=MibTableColumn
mgreceptacleShutoffTimer=_MgreceptacleShutoffTimer_Object((1,3,6,1,4,1,705,1,4,23,1,6),_MgreceptacleShutoffTimer_Type())
mgreceptacleShutoffTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:mgreceptacleShutoffTimer.setStatus(_A)
_MgreceptacleRestartLevel_Type=Integer32
_MgreceptacleRestartLevel_Object=MibTableColumn
mgreceptacleRestartLevel=_MgreceptacleRestartLevel_Object((1,3,6,1,4,1,705,1,4,23,1,7),_MgreceptacleRestartLevel_Type())
mgreceptacleRestartLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:mgreceptacleRestartLevel.setStatus(_A)
_MgreceptacleRestartDelay_Type=Integer32
_MgreceptacleRestartDelay_Object=MibTableColumn
mgreceptacleRestartDelay=_MgreceptacleRestartDelay_Object((1,3,6,1,4,1,705,1,4,23,1,8),_MgreceptacleRestartDelay_Type())
mgreceptacleRestartDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:mgreceptacleRestartDelay.setStatus(_A)
_MgreceptacleShutdownDuration_Type=Integer32
_MgreceptacleShutdownDuration_Object=MibTableColumn
mgreceptacleShutdownDuration=_MgreceptacleShutdownDuration_Object((1,3,6,1,4,1,705,1,4,23,1,9),_MgreceptacleShutdownDuration_Type())
mgreceptacleShutdownDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:mgreceptacleShutdownDuration.setStatus(_A)
_MgreceptacleBootUpDuration_Type=Integer32
_MgreceptacleBootUpDuration_Object=MibTableColumn
mgreceptacleBootUpDuration=_MgreceptacleBootUpDuration_Object((1,3,6,1,4,1,705,1,4,23,1,10),_MgreceptacleBootUpDuration_Type())
mgreceptacleBootUpDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:mgreceptacleBootUpDuration.setStatus(_A)
_UpsmgConfigExtAlarmNum_Type=Integer32
_UpsmgConfigExtAlarmNum_Object=MibScalar
upsmgConfigExtAlarmNum=_UpsmgConfigExtAlarmNum_Object((1,3,6,1,4,1,705,1,4,24),_UpsmgConfigExtAlarmNum_Type())
upsmgConfigExtAlarmNum.setMaxAccess(_C)
if mibBuilder.loadTexts:upsmgConfigExtAlarmNum.setStatus(_A)
_UpsmgConfigExtAlarmTable_Object=MibTable
upsmgConfigExtAlarmTable=_UpsmgConfigExtAlarmTable_Object((1,3,6,1,4,1,705,1,4,25))
if mibBuilder.loadTexts:upsmgConfigExtAlarmTable.setStatus(_A)
_UpsmgConfigExtAlarmEntry_Object=MibTableRow
upsmgConfigExtAlarmEntry=_UpsmgConfigExtAlarmEntry_Object((1,3,6,1,4,1,705,1,4,25,1))
upsmgConfigExtAlarmEntry.setIndexNames((0,_E,_P))
if mibBuilder.loadTexts:upsmgConfigExtAlarmEntry.setStatus(_A)
class _MgextAlarmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_MgextAlarmIndex_Type.__name__=_D
_MgextAlarmIndex_Object=MibTableColumn
mgextAlarmIndex=_MgextAlarmIndex_Object((1,3,6,1,4,1,705,1,4,25,1,1),_MgextAlarmIndex_Type())
mgextAlarmIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:mgextAlarmIndex.setStatus(_A)
class _MgextAlarmUID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_MgextAlarmUID_Type.__name__=_H
_MgextAlarmUID_Object=MibTableColumn
mgextAlarmUID=_MgextAlarmUID_Object((1,3,6,1,4,1,705,1,4,25,1,2),_MgextAlarmUID_Type())
mgextAlarmUID.setMaxAccess(_B)
if mibBuilder.loadTexts:mgextAlarmUID.setStatus(_A)
class _UpsmgConfigEmergencyTestFail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_UpsmgConfigEmergencyTestFail_Type.__name__=_D
_UpsmgConfigEmergencyTestFail_Object=MibScalar
upsmgConfigEmergencyTestFail=_UpsmgConfigEmergencyTestFail_Object((1,3,6,1,4,1,705,1,4,26),_UpsmgConfigEmergencyTestFail_Type())
upsmgConfigEmergencyTestFail.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgConfigEmergencyTestFail.setStatus(_A)
class _UpsmgConfigEmergencyOnByPass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_UpsmgConfigEmergencyOnByPass_Type.__name__=_D
_UpsmgConfigEmergencyOnByPass_Object=MibScalar
upsmgConfigEmergencyOnByPass=_UpsmgConfigEmergencyOnByPass_Object((1,3,6,1,4,1,705,1,4,27),_UpsmgConfigEmergencyOnByPass_Type())
upsmgConfigEmergencyOnByPass.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgConfigEmergencyOnByPass.setStatus(_A)
class _UpsmgConfigEmergencyOverload_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_UpsmgConfigEmergencyOverload_Type.__name__=_D
_UpsmgConfigEmergencyOverload_Object=MibScalar
upsmgConfigEmergencyOverload=_UpsmgConfigEmergencyOverload_Object((1,3,6,1,4,1,705,1,4,28),_UpsmgConfigEmergencyOverload_Type())
upsmgConfigEmergencyOverload.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgConfigEmergencyOverload.setStatus(_A)
_UpsmgConfigControlDayTable_Object=MibTable
upsmgConfigControlDayTable=_UpsmgConfigControlDayTable_Object((1,3,6,1,4,1,705,1,4,29))
if mibBuilder.loadTexts:upsmgConfigControlDayTable.setStatus(_A)
_UpsmgConfigControlDayEntry_Object=MibTableRow
upsmgConfigControlDayEntry=_UpsmgConfigControlDayEntry_Object((1,3,6,1,4,1,705,1,4,29,1))
upsmgConfigControlDayEntry.setIndexNames((0,_E,_h))
if mibBuilder.loadTexts:upsmgConfigControlDayEntry.setStatus(_A)
class _MgcontrolDayIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_MgcontrolDayIndex_Type.__name__=_D
_MgcontrolDayIndex_Object=MibTableColumn
mgcontrolDayIndex=_MgcontrolDayIndex_Object((1,3,6,1,4,1,705,1,4,29,1,1),_MgcontrolDayIndex_Type())
mgcontrolDayIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:mgcontrolDayIndex.setStatus(_A)
_MgcontrolDayOn_Type=Integer32
_MgcontrolDayOn_Object=MibTableColumn
mgcontrolDayOn=_MgcontrolDayOn_Object((1,3,6,1,4,1,705,1,4,29,1,2),_MgcontrolDayOn_Type())
mgcontrolDayOn.setMaxAccess(_B)
if mibBuilder.loadTexts:mgcontrolDayOn.setStatus(_A)
_MgcontrolDayOff_Type=Integer32
_MgcontrolDayOff_Object=MibTableColumn
mgcontrolDayOff=_MgcontrolDayOff_Object((1,3,6,1,4,1,705,1,4,29,1,3),_MgcontrolDayOff_Type())
mgcontrolDayOff.setMaxAccess(_B)
if mibBuilder.loadTexts:mgcontrolDayOff.setStatus(_A)
_UpsmgConfigLowBooster_Type=Integer32
_UpsmgConfigLowBooster_Object=MibScalar
upsmgConfigLowBooster=_UpsmgConfigLowBooster_Object((1,3,6,1,4,1,705,1,4,30),_UpsmgConfigLowBooster_Type())
upsmgConfigLowBooster.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgConfigLowBooster.setStatus(_A)
_UpsmgConfigHighBooster_Type=Integer32
_UpsmgConfigHighBooster_Object=MibScalar
upsmgConfigHighBooster=_UpsmgConfigHighBooster_Object((1,3,6,1,4,1,705,1,4,31),_UpsmgConfigHighBooster_Type())
upsmgConfigHighBooster.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgConfigHighBooster.setStatus(_A)
_UpsmgConfigLowFader_Type=Integer32
_UpsmgConfigLowFader_Object=MibScalar
upsmgConfigLowFader=_UpsmgConfigLowFader_Object((1,3,6,1,4,1,705,1,4,32),_UpsmgConfigLowFader_Type())
upsmgConfigLowFader.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgConfigLowFader.setStatus(_A)
_UpsmgConfigHighFader_Type=Integer32
_UpsmgConfigHighFader_Object=MibScalar
upsmgConfigHighFader=_UpsmgConfigHighFader_Object((1,3,6,1,4,1,705,1,4,33),_UpsmgConfigHighFader_Type())
upsmgConfigHighFader.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgConfigHighFader.setStatus(_A)
_UpsmgConfigEnvironmentTable_Object=MibTable
upsmgConfigEnvironmentTable=_UpsmgConfigEnvironmentTable_Object((1,3,6,1,4,1,705,1,4,34))
if mibBuilder.loadTexts:upsmgConfigEnvironmentTable.setStatus(_A)
_UpsmgConfigEnvironmentEntry_Object=MibTableRow
upsmgConfigEnvironmentEntry=_UpsmgConfigEnvironmentEntry_Object((1,3,6,1,4,1,705,1,4,34,1))
upsmgConfigEnvironmentEntry.setIndexNames((0,_E,_i))
if mibBuilder.loadTexts:upsmgConfigEnvironmentEntry.setStatus(_A)
class _UpsmgConfigSensorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,50))
_UpsmgConfigSensorIndex_Type.__name__=_D
_UpsmgConfigSensorIndex_Object=MibTableColumn
upsmgConfigSensorIndex=_UpsmgConfigSensorIndex_Object((1,3,6,1,4,1,705,1,4,34,1,1),_UpsmgConfigSensorIndex_Type())
upsmgConfigSensorIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:upsmgConfigSensorIndex.setStatus(_A)
class _UpsmgConfigSensorName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,42))
_UpsmgConfigSensorName_Type.__name__=_H
_UpsmgConfigSensorName_Object=MibTableColumn
upsmgConfigSensorName=_UpsmgConfigSensorName_Object((1,3,6,1,4,1,705,1,4,34,1,2),_UpsmgConfigSensorName_Type())
upsmgConfigSensorName.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgConfigSensorName.setStatus(_A)
_UpsmgConfigTemperatureLow_Type=Integer32
_UpsmgConfigTemperatureLow_Object=MibTableColumn
upsmgConfigTemperatureLow=_UpsmgConfigTemperatureLow_Object((1,3,6,1,4,1,705,1,4,34,1,3),_UpsmgConfigTemperatureLow_Type())
upsmgConfigTemperatureLow.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgConfigTemperatureLow.setStatus(_A)
_UpsmgConfigTemperatureHigh_Type=Integer32
_UpsmgConfigTemperatureHigh_Object=MibTableColumn
upsmgConfigTemperatureHigh=_UpsmgConfigTemperatureHigh_Object((1,3,6,1,4,1,705,1,4,34,1,4),_UpsmgConfigTemperatureHigh_Type())
upsmgConfigTemperatureHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgConfigTemperatureHigh.setStatus(_A)
_UpsmgConfigTemperatureHysteresis_Type=Integer32
_UpsmgConfigTemperatureHysteresis_Object=MibTableColumn
upsmgConfigTemperatureHysteresis=_UpsmgConfigTemperatureHysteresis_Object((1,3,6,1,4,1,705,1,4,34,1,5),_UpsmgConfigTemperatureHysteresis_Type())
upsmgConfigTemperatureHysteresis.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgConfigTemperatureHysteresis.setStatus(_A)
_UpsmgConfigHumidityLow_Type=Integer32
_UpsmgConfigHumidityLow_Object=MibTableColumn
upsmgConfigHumidityLow=_UpsmgConfigHumidityLow_Object((1,3,6,1,4,1,705,1,4,34,1,6),_UpsmgConfigHumidityLow_Type())
upsmgConfigHumidityLow.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgConfigHumidityLow.setStatus(_A)
_UpsmgConfigHumidityHigh_Type=Integer32
_UpsmgConfigHumidityHigh_Object=MibTableColumn
upsmgConfigHumidityHigh=_UpsmgConfigHumidityHigh_Object((1,3,6,1,4,1,705,1,4,34,1,7),_UpsmgConfigHumidityHigh_Type())
upsmgConfigHumidityHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgConfigHumidityHigh.setStatus(_A)
_UpsmgConfigHumidityHysteresis_Type=Integer32
_UpsmgConfigHumidityHysteresis_Object=MibTableColumn
upsmgConfigHumidityHysteresis=_UpsmgConfigHumidityHysteresis_Object((1,3,6,1,4,1,705,1,4,34,1,8),_UpsmgConfigHumidityHysteresis_Type())
upsmgConfigHumidityHysteresis.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgConfigHumidityHysteresis.setStatus(_A)
class _UpsmgConfigInput1Name_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,22))
_UpsmgConfigInput1Name_Type.__name__=_H
_UpsmgConfigInput1Name_Object=MibTableColumn
upsmgConfigInput1Name=_UpsmgConfigInput1Name_Object((1,3,6,1,4,1,705,1,4,34,1,9),_UpsmgConfigInput1Name_Type())
upsmgConfigInput1Name.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgConfigInput1Name.setStatus(_A)
class _UpsmgConfigInput1ClosedLabel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,18))
_UpsmgConfigInput1ClosedLabel_Type.__name__=_H
_UpsmgConfigInput1ClosedLabel_Object=MibTableColumn
upsmgConfigInput1ClosedLabel=_UpsmgConfigInput1ClosedLabel_Object((1,3,6,1,4,1,705,1,4,34,1,10),_UpsmgConfigInput1ClosedLabel_Type())
upsmgConfigInput1ClosedLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgConfigInput1ClosedLabel.setStatus(_A)
class _UpsmgConfigInput1OpenLabel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,18))
_UpsmgConfigInput1OpenLabel_Type.__name__=_H
_UpsmgConfigInput1OpenLabel_Object=MibTableColumn
upsmgConfigInput1OpenLabel=_UpsmgConfigInput1OpenLabel_Object((1,3,6,1,4,1,705,1,4,34,1,11),_UpsmgConfigInput1OpenLabel_Type())
upsmgConfigInput1OpenLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgConfigInput1OpenLabel.setStatus(_A)
class _UpsmgConfigInput2Name_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,22))
_UpsmgConfigInput2Name_Type.__name__=_H
_UpsmgConfigInput2Name_Object=MibTableColumn
upsmgConfigInput2Name=_UpsmgConfigInput2Name_Object((1,3,6,1,4,1,705,1,4,34,1,12),_UpsmgConfigInput2Name_Type())
upsmgConfigInput2Name.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgConfigInput2Name.setStatus(_A)
class _UpsmgConfigInput2ClosedLabel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,18))
_UpsmgConfigInput2ClosedLabel_Type.__name__=_H
_UpsmgConfigInput2ClosedLabel_Object=MibTableColumn
upsmgConfigInput2ClosedLabel=_UpsmgConfigInput2ClosedLabel_Object((1,3,6,1,4,1,705,1,4,34,1,13),_UpsmgConfigInput2ClosedLabel_Type())
upsmgConfigInput2ClosedLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgConfigInput2ClosedLabel.setStatus(_A)
class _UpsmgConfigInput2OpenLabel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,18))
_UpsmgConfigInput2OpenLabel_Type.__name__=_H
_UpsmgConfigInput2OpenLabel_Object=MibTableColumn
upsmgConfigInput2OpenLabel=_UpsmgConfigInput2OpenLabel_Object((1,3,6,1,4,1,705,1,4,34,1,14),_UpsmgConfigInput2OpenLabel_Type())
upsmgConfigInput2OpenLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgConfigInput2OpenLabel.setStatus(_A)
_UpsmgBattery_ObjectIdentity=ObjectIdentity
upsmgBattery=_UpsmgBattery_ObjectIdentity((1,3,6,1,4,1,705,1,5))
_UpsmgBatteryRemainingTime_Type=Integer32
_UpsmgBatteryRemainingTime_Object=MibScalar
upsmgBatteryRemainingTime=_UpsmgBatteryRemainingTime_Object((1,3,6,1,4,1,705,1,5,1),_UpsmgBatteryRemainingTime_Type())
upsmgBatteryRemainingTime.setMaxAccess(_C)
if mibBuilder.loadTexts:upsmgBatteryRemainingTime.setStatus(_A)
_UpsmgBatteryLevel_Type=Integer32
_UpsmgBatteryLevel_Object=MibScalar
upsmgBatteryLevel=_UpsmgBatteryLevel_Object((1,3,6,1,4,1,705,1,5,2),_UpsmgBatteryLevel_Type())
upsmgBatteryLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:upsmgBatteryLevel.setStatus(_A)
_UpsmgBatteryRechargeTime_Type=Integer32
_UpsmgBatteryRechargeTime_Object=MibScalar
upsmgBatteryRechargeTime=_UpsmgBatteryRechargeTime_Object((1,3,6,1,4,1,705,1,5,3),_UpsmgBatteryRechargeTime_Type())
upsmgBatteryRechargeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:upsmgBatteryRechargeTime.setStatus(_A)
_UpsmgBatteryRechargeLevel_Type=Integer32
_UpsmgBatteryRechargeLevel_Object=MibScalar
upsmgBatteryRechargeLevel=_UpsmgBatteryRechargeLevel_Object((1,3,6,1,4,1,705,1,5,4),_UpsmgBatteryRechargeLevel_Type())
upsmgBatteryRechargeLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:upsmgBatteryRechargeLevel.setStatus(_A)
_UpsmgBatteryVoltage_Type=Integer32
_UpsmgBatteryVoltage_Object=MibScalar
upsmgBatteryVoltage=_UpsmgBatteryVoltage_Object((1,3,6,1,4,1,705,1,5,5),_UpsmgBatteryVoltage_Type())
upsmgBatteryVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:upsmgBatteryVoltage.setStatus(_A)
_UpsmgBatteryCurrent_Type=Integer32
_UpsmgBatteryCurrent_Object=MibScalar
upsmgBatteryCurrent=_UpsmgBatteryCurrent_Object((1,3,6,1,4,1,705,1,5,6),_UpsmgBatteryCurrent_Type())
upsmgBatteryCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:upsmgBatteryCurrent.setStatus(_A)
_UpsmgBatteryTemperature_Type=Integer32
_UpsmgBatteryTemperature_Object=MibScalar
upsmgBatteryTemperature=_UpsmgBatteryTemperature_Object((1,3,6,1,4,1,705,1,5,7),_UpsmgBatteryTemperature_Type())
upsmgBatteryTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:upsmgBatteryTemperature.setStatus(_A)
_UpsmgBatteryFullRechargeTime_Type=Integer32
_UpsmgBatteryFullRechargeTime_Object=MibScalar
upsmgBatteryFullRechargeTime=_UpsmgBatteryFullRechargeTime_Object((1,3,6,1,4,1,705,1,5,8),_UpsmgBatteryFullRechargeTime_Type())
upsmgBatteryFullRechargeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:upsmgBatteryFullRechargeTime.setStatus(_A)
class _UpsmgBatteryFaultBattery_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_UpsmgBatteryFaultBattery_Type.__name__=_D
_UpsmgBatteryFaultBattery_Object=MibScalar
upsmgBatteryFaultBattery=_UpsmgBatteryFaultBattery_Object((1,3,6,1,4,1,705,1,5,9),_UpsmgBatteryFaultBattery_Type())
upsmgBatteryFaultBattery.setMaxAccess(_C)
if mibBuilder.loadTexts:upsmgBatteryFaultBattery.setStatus(_A)
class _UpsmgBatteryNoBattery_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_UpsmgBatteryNoBattery_Type.__name__=_D
_UpsmgBatteryNoBattery_Object=MibScalar
upsmgBatteryNoBattery=_UpsmgBatteryNoBattery_Object((1,3,6,1,4,1,705,1,5,10),_UpsmgBatteryNoBattery_Type())
upsmgBatteryNoBattery.setMaxAccess(_C)
if mibBuilder.loadTexts:upsmgBatteryNoBattery.setStatus(_A)
class _UpsmgBatteryReplacement_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_UpsmgBatteryReplacement_Type.__name__=_D
_UpsmgBatteryReplacement_Object=MibScalar
upsmgBatteryReplacement=_UpsmgBatteryReplacement_Object((1,3,6,1,4,1,705,1,5,11),_UpsmgBatteryReplacement_Type())
upsmgBatteryReplacement.setMaxAccess(_C)
if mibBuilder.loadTexts:upsmgBatteryReplacement.setStatus(_A)
class _UpsmgBatteryUnavailableBattery_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_UpsmgBatteryUnavailableBattery_Type.__name__=_D
_UpsmgBatteryUnavailableBattery_Object=MibScalar
upsmgBatteryUnavailableBattery=_UpsmgBatteryUnavailableBattery_Object((1,3,6,1,4,1,705,1,5,12),_UpsmgBatteryUnavailableBattery_Type())
upsmgBatteryUnavailableBattery.setMaxAccess(_C)
if mibBuilder.loadTexts:upsmgBatteryUnavailableBattery.setStatus(_A)
class _UpsmgBatteryNotHighCharge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_UpsmgBatteryNotHighCharge_Type.__name__=_D
_UpsmgBatteryNotHighCharge_Object=MibScalar
upsmgBatteryNotHighCharge=_UpsmgBatteryNotHighCharge_Object((1,3,6,1,4,1,705,1,5,13),_UpsmgBatteryNotHighCharge_Type())
upsmgBatteryNotHighCharge.setMaxAccess(_C)
if mibBuilder.loadTexts:upsmgBatteryNotHighCharge.setStatus(_A)
class _UpsmgBatteryLowBattery_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_UpsmgBatteryLowBattery_Type.__name__=_D
_UpsmgBatteryLowBattery_Object=MibScalar
upsmgBatteryLowBattery=_UpsmgBatteryLowBattery_Object((1,3,6,1,4,1,705,1,5,14),_UpsmgBatteryLowBattery_Type())
upsmgBatteryLowBattery.setMaxAccess(_C)
if mibBuilder.loadTexts:upsmgBatteryLowBattery.setStatus(_A)
class _UpsmgBatteryChargerFault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_UpsmgBatteryChargerFault_Type.__name__=_D
_UpsmgBatteryChargerFault_Object=MibScalar
upsmgBatteryChargerFault=_UpsmgBatteryChargerFault_Object((1,3,6,1,4,1,705,1,5,15),_UpsmgBatteryChargerFault_Type())
upsmgBatteryChargerFault.setMaxAccess(_C)
if mibBuilder.loadTexts:upsmgBatteryChargerFault.setStatus(_A)
class _UpsmgBatteryLowCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_UpsmgBatteryLowCondition_Type.__name__=_D
_UpsmgBatteryLowCondition_Object=MibScalar
upsmgBatteryLowCondition=_UpsmgBatteryLowCondition_Object((1,3,6,1,4,1,705,1,5,16),_UpsmgBatteryLowCondition_Type())
upsmgBatteryLowCondition.setMaxAccess(_C)
if mibBuilder.loadTexts:upsmgBatteryLowCondition.setStatus(_A)
class _UpsmgBatteryLowRecharge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_UpsmgBatteryLowRecharge_Type.__name__=_D
_UpsmgBatteryLowRecharge_Object=MibScalar
upsmgBatteryLowRecharge=_UpsmgBatteryLowRecharge_Object((1,3,6,1,4,1,705,1,5,17),_UpsmgBatteryLowRecharge_Type())
upsmgBatteryLowRecharge.setMaxAccess(_C)
if mibBuilder.loadTexts:upsmgBatteryLowRecharge.setStatus(_A)
_UpsmgInput_ObjectIdentity=ObjectIdentity
upsmgInput=_UpsmgInput_ObjectIdentity((1,3,6,1,4,1,705,1,6))
_UpsmgInputPhaseNum_Type=Integer32
_UpsmgInputPhaseNum_Object=MibScalar
upsmgInputPhaseNum=_UpsmgInputPhaseNum_Object((1,3,6,1,4,1,705,1,6,1),_UpsmgInputPhaseNum_Type())
upsmgInputPhaseNum.setMaxAccess(_C)
if mibBuilder.loadTexts:upsmgInputPhaseNum.setStatus(_A)
_UpsmgInputPhaseTable_Object=MibTable
upsmgInputPhaseTable=_UpsmgInputPhaseTable_Object((1,3,6,1,4,1,705,1,6,2))
if mibBuilder.loadTexts:upsmgInputPhaseTable.setStatus(_A)
_UpsmgInputPhaseEntry_Object=MibTableRow
upsmgInputPhaseEntry=_UpsmgInputPhaseEntry_Object((1,3,6,1,4,1,705,1,6,2,1))
upsmgInputPhaseEntry.setIndexNames((0,_E,_j))
if mibBuilder.loadTexts:upsmgInputPhaseEntry.setStatus(_A)
class _MginputIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_MginputIndex_Type.__name__=_D
_MginputIndex_Object=MibTableColumn
mginputIndex=_MginputIndex_Object((1,3,6,1,4,1,705,1,6,2,1,1),_MginputIndex_Type())
mginputIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:mginputIndex.setStatus(_A)
_MginputVoltage_Type=Integer32
_MginputVoltage_Object=MibTableColumn
mginputVoltage=_MginputVoltage_Object((1,3,6,1,4,1,705,1,6,2,1,2),_MginputVoltage_Type())
mginputVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:mginputVoltage.setStatus(_A)
_MginputFrequency_Type=Integer32
_MginputFrequency_Object=MibTableColumn
mginputFrequency=_MginputFrequency_Object((1,3,6,1,4,1,705,1,6,2,1,3),_MginputFrequency_Type())
mginputFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:mginputFrequency.setStatus(_A)
_MginputMinimumVoltage_Type=Integer32
_MginputMinimumVoltage_Object=MibTableColumn
mginputMinimumVoltage=_MginputMinimumVoltage_Object((1,3,6,1,4,1,705,1,6,2,1,4),_MginputMinimumVoltage_Type())
mginputMinimumVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:mginputMinimumVoltage.setStatus(_A)
_MginputMaximumVoltage_Type=Integer32
_MginputMaximumVoltage_Object=MibTableColumn
mginputMaximumVoltage=_MginputMaximumVoltage_Object((1,3,6,1,4,1,705,1,6,2,1,5),_MginputMaximumVoltage_Type())
mginputMaximumVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:mginputMaximumVoltage.setStatus(_A)
_MginputCurrent_Type=Integer32
_MginputCurrent_Object=MibTableColumn
mginputCurrent=_MginputCurrent_Object((1,3,6,1,4,1,705,1,6,2,1,6),_MginputCurrent_Type())
mginputCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:mginputCurrent.setStatus(_A)
class _UpsmgInputBadStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_UpsmgInputBadStatus_Type.__name__=_D
_UpsmgInputBadStatus_Object=MibScalar
upsmgInputBadStatus=_UpsmgInputBadStatus_Object((1,3,6,1,4,1,705,1,6,3),_UpsmgInputBadStatus_Type())
upsmgInputBadStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:upsmgInputBadStatus.setStatus(_A)
class _UpsmgInputLineFailCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),('outoftolvolt',2),('outoftolfreq',3),('utilityoff',4)))
_UpsmgInputLineFailCause_Type.__name__=_D
_UpsmgInputLineFailCause_Object=MibScalar
upsmgInputLineFailCause=_UpsmgInputLineFailCause_Object((1,3,6,1,4,1,705,1,6,4),_UpsmgInputLineFailCause_Type())
upsmgInputLineFailCause.setMaxAccess(_C)
if mibBuilder.loadTexts:upsmgInputLineFailCause.setStatus(_A)
_UpsmgOutput_ObjectIdentity=ObjectIdentity
upsmgOutput=_UpsmgOutput_ObjectIdentity((1,3,6,1,4,1,705,1,7))
_UpsmgOutputPhaseNum_Type=Integer32
_UpsmgOutputPhaseNum_Object=MibScalar
upsmgOutputPhaseNum=_UpsmgOutputPhaseNum_Object((1,3,6,1,4,1,705,1,7,1),_UpsmgOutputPhaseNum_Type())
upsmgOutputPhaseNum.setMaxAccess(_C)
if mibBuilder.loadTexts:upsmgOutputPhaseNum.setStatus(_A)
_UpsmgOutputPhaseTable_Object=MibTable
upsmgOutputPhaseTable=_UpsmgOutputPhaseTable_Object((1,3,6,1,4,1,705,1,7,2))
if mibBuilder.loadTexts:upsmgOutputPhaseTable.setStatus(_A)
_UpsmgOutputPhaseEntry_Object=MibTableRow
upsmgOutputPhaseEntry=_UpsmgOutputPhaseEntry_Object((1,3,6,1,4,1,705,1,7,2,1))
upsmgOutputPhaseEntry.setIndexNames((0,_E,_k))
if mibBuilder.loadTexts:upsmgOutputPhaseEntry.setStatus(_A)
class _MgoutputPhaseIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_MgoutputPhaseIndex_Type.__name__=_D
_MgoutputPhaseIndex_Object=MibTableColumn
mgoutputPhaseIndex=_MgoutputPhaseIndex_Object((1,3,6,1,4,1,705,1,7,2,1,1),_MgoutputPhaseIndex_Type())
mgoutputPhaseIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:mgoutputPhaseIndex.setStatus(_A)
_MgoutputVoltage_Type=Integer32
_MgoutputVoltage_Object=MibTableColumn
mgoutputVoltage=_MgoutputVoltage_Object((1,3,6,1,4,1,705,1,7,2,1,2),_MgoutputVoltage_Type())
mgoutputVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:mgoutputVoltage.setStatus(_A)
_MgoutputFrequency_Type=Integer32
_MgoutputFrequency_Object=MibTableColumn
mgoutputFrequency=_MgoutputFrequency_Object((1,3,6,1,4,1,705,1,7,2,1,3),_MgoutputFrequency_Type())
mgoutputFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:mgoutputFrequency.setStatus(_A)
_MgoutputLoadPerPhase_Type=Integer32
_MgoutputLoadPerPhase_Object=MibTableColumn
mgoutputLoadPerPhase=_MgoutputLoadPerPhase_Object((1,3,6,1,4,1,705,1,7,2,1,4),_MgoutputLoadPerPhase_Type())
mgoutputLoadPerPhase.setMaxAccess(_C)
if mibBuilder.loadTexts:mgoutputLoadPerPhase.setStatus(_A)
_MgoutputCurrent_Type=Integer32
_MgoutputCurrent_Object=MibTableColumn
mgoutputCurrent=_MgoutputCurrent_Object((1,3,6,1,4,1,705,1,7,2,1,5),_MgoutputCurrent_Type())
mgoutputCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:mgoutputCurrent.setStatus(_A)
class _UpsmgOutputOnBattery_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_UpsmgOutputOnBattery_Type.__name__=_D
_UpsmgOutputOnBattery_Object=MibScalar
upsmgOutputOnBattery=_UpsmgOutputOnBattery_Object((1,3,6,1,4,1,705,1,7,3),_UpsmgOutputOnBattery_Type())
upsmgOutputOnBattery.setMaxAccess(_C)
if mibBuilder.loadTexts:upsmgOutputOnBattery.setStatus(_A)
class _UpsmgOutputOnByPass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_UpsmgOutputOnByPass_Type.__name__=_D
_UpsmgOutputOnByPass_Object=MibScalar
upsmgOutputOnByPass=_UpsmgOutputOnByPass_Object((1,3,6,1,4,1,705,1,7,4),_UpsmgOutputOnByPass_Type())
upsmgOutputOnByPass.setMaxAccess(_C)
if mibBuilder.loadTexts:upsmgOutputOnByPass.setStatus(_A)
class _UpsmgOutputUnavailableByPass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_UpsmgOutputUnavailableByPass_Type.__name__=_D
_UpsmgOutputUnavailableByPass_Object=MibScalar
upsmgOutputUnavailableByPass=_UpsmgOutputUnavailableByPass_Object((1,3,6,1,4,1,705,1,7,5),_UpsmgOutputUnavailableByPass_Type())
upsmgOutputUnavailableByPass.setMaxAccess(_C)
if mibBuilder.loadTexts:upsmgOutputUnavailableByPass.setStatus(_A)
class _UpsmgOutputNoByPass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_UpsmgOutputNoByPass_Type.__name__=_D
_UpsmgOutputNoByPass_Object=MibScalar
upsmgOutputNoByPass=_UpsmgOutputNoByPass_Object((1,3,6,1,4,1,705,1,7,6),_UpsmgOutputNoByPass_Type())
upsmgOutputNoByPass.setMaxAccess(_C)
if mibBuilder.loadTexts:upsmgOutputNoByPass.setStatus(_A)
class _UpsmgOutputUtilityOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_UpsmgOutputUtilityOff_Type.__name__=_D
_UpsmgOutputUtilityOff_Object=MibScalar
upsmgOutputUtilityOff=_UpsmgOutputUtilityOff_Object((1,3,6,1,4,1,705,1,7,7),_UpsmgOutputUtilityOff_Type())
upsmgOutputUtilityOff.setMaxAccess(_C)
if mibBuilder.loadTexts:upsmgOutputUtilityOff.setStatus(_A)
class _UpsmgOutputOnBoost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_UpsmgOutputOnBoost_Type.__name__=_D
_UpsmgOutputOnBoost_Object=MibScalar
upsmgOutputOnBoost=_UpsmgOutputOnBoost_Object((1,3,6,1,4,1,705,1,7,8),_UpsmgOutputOnBoost_Type())
upsmgOutputOnBoost.setMaxAccess(_C)
if mibBuilder.loadTexts:upsmgOutputOnBoost.setStatus(_A)
class _UpsmgOutputInverterOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_UpsmgOutputInverterOff_Type.__name__=_D
_UpsmgOutputInverterOff_Object=MibScalar
upsmgOutputInverterOff=_UpsmgOutputInverterOff_Object((1,3,6,1,4,1,705,1,7,9),_UpsmgOutputInverterOff_Type())
upsmgOutputInverterOff.setMaxAccess(_C)
if mibBuilder.loadTexts:upsmgOutputInverterOff.setStatus(_A)
class _UpsmgOutputOverLoad_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_UpsmgOutputOverLoad_Type.__name__=_D
_UpsmgOutputOverLoad_Object=MibScalar
upsmgOutputOverLoad=_UpsmgOutputOverLoad_Object((1,3,6,1,4,1,705,1,7,10),_UpsmgOutputOverLoad_Type())
upsmgOutputOverLoad.setMaxAccess(_C)
if mibBuilder.loadTexts:upsmgOutputOverLoad.setStatus(_A)
class _UpsmgOutputOverTemp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_UpsmgOutputOverTemp_Type.__name__=_D
_UpsmgOutputOverTemp_Object=MibScalar
upsmgOutputOverTemp=_UpsmgOutputOverTemp_Object((1,3,6,1,4,1,705,1,7,11),_UpsmgOutputOverTemp_Type())
upsmgOutputOverTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:upsmgOutputOverTemp.setStatus(_A)
_UpsmgOutputOnBuck_Type=Integer32
_UpsmgOutputOnBuck_Object=MibScalar
upsmgOutputOnBuck=_UpsmgOutputOnBuck_Object((1,3,6,1,4,1,705,1,7,12),_UpsmgOutputOnBuck_Type())
upsmgOutputOnBuck.setMaxAccess(_C)
if mibBuilder.loadTexts:upsmgOutputOnBuck.setStatus(_A)
_UpsmgEnviron_ObjectIdentity=ObjectIdentity
upsmgEnviron=_UpsmgEnviron_ObjectIdentity((1,3,6,1,4,1,705,1,8))
_UpsmgEnvironAmbientTemp_Type=Integer32
_UpsmgEnvironAmbientTemp_Object=MibScalar
upsmgEnvironAmbientTemp=_UpsmgEnvironAmbientTemp_Object((1,3,6,1,4,1,705,1,8,1),_UpsmgEnvironAmbientTemp_Type())
upsmgEnvironAmbientTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:upsmgEnvironAmbientTemp.setStatus(_A)
_UpsmgEnvironAmbientHumidity_Type=Integer32
_UpsmgEnvironAmbientHumidity_Object=MibScalar
upsmgEnvironAmbientHumidity=_UpsmgEnvironAmbientHumidity_Object((1,3,6,1,4,1,705,1,8,2),_UpsmgEnvironAmbientHumidity_Type())
upsmgEnvironAmbientHumidity.setMaxAccess(_C)
if mibBuilder.loadTexts:upsmgEnvironAmbientHumidity.setStatus(_A)
_UpsmgEnvironExtAlarmTable_Object=MibTable
upsmgEnvironExtAlarmTable=_UpsmgEnvironExtAlarmTable_Object((1,3,6,1,4,1,705,1,8,3))
if mibBuilder.loadTexts:upsmgEnvironExtAlarmTable.setStatus(_A)
_UpsmgEnvironExtAlarmEntry_Object=MibTableRow
upsmgEnvironExtAlarmEntry=_UpsmgEnvironExtAlarmEntry_Object((1,3,6,1,4,1,705,1,8,3,1))
upsmgEnvironExtAlarmEntry.setIndexNames((0,_E,_l))
if mibBuilder.loadTexts:upsmgEnvironExtAlarmEntry.setStatus(_A)
class _MgalarmNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_MgalarmNum_Type.__name__=_D
_MgalarmNum_Object=MibTableColumn
mgalarmNum=_MgalarmNum_Object((1,3,6,1,4,1,705,1,8,3,1,1),_MgalarmNum_Type())
mgalarmNum.setMaxAccess(_C)
if mibBuilder.loadTexts:mgalarmNum.setStatus(_A)
class _MgalarmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('inactive',2)))
_MgalarmState_Type.__name__=_D
_MgalarmState_Object=MibTableColumn
mgalarmState=_MgalarmState_Object((1,3,6,1,4,1,705,1,8,3,1,2),_MgalarmState_Type())
mgalarmState.setMaxAccess(_C)
if mibBuilder.loadTexts:mgalarmState.setStatus(_A)
_UpsmgEnvironSensorNum_Type=Integer32
_UpsmgEnvironSensorNum_Object=MibScalar
upsmgEnvironSensorNum=_UpsmgEnvironSensorNum_Object((1,3,6,1,4,1,705,1,8,4),_UpsmgEnvironSensorNum_Type())
upsmgEnvironSensorNum.setMaxAccess(_C)
if mibBuilder.loadTexts:upsmgEnvironSensorNum.setStatus(_A)
_UpsmgEnvironSensorTable_Object=MibTable
upsmgEnvironSensorTable=_UpsmgEnvironSensorTable_Object((1,3,6,1,4,1,705,1,8,5))
if mibBuilder.loadTexts:upsmgEnvironSensorTable.setStatus(_A)
_UpsmgEnvironSensorEntry_Object=MibTableRow
upsmgEnvironSensorEntry=_UpsmgEnvironSensorEntry_Object((1,3,6,1,4,1,705,1,8,5,1))
upsmgEnvironSensorEntry.setIndexNames((0,_E,_m))
if mibBuilder.loadTexts:upsmgEnvironSensorEntry.setStatus(_A)
class _MgsensorNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_MgsensorNum_Type.__name__=_D
_MgsensorNum_Object=MibTableColumn
mgsensorNum=_MgsensorNum_Object((1,3,6,1,4,1,705,1,8,5,1,1),_MgsensorNum_Type())
mgsensorNum.setMaxAccess(_C)
if mibBuilder.loadTexts:mgsensorNum.setStatus(_A)
_MgsensorTemp_Type=Integer32
_MgsensorTemp_Object=MibTableColumn
mgsensorTemp=_MgsensorTemp_Object((1,3,6,1,4,1,705,1,8,5,1,2),_MgsensorTemp_Type())
mgsensorTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:mgsensorTemp.setStatus(_A)
_MgsensorHumidity_Type=Integer32
_MgsensorHumidity_Object=MibTableColumn
mgsensorHumidity=_MgsensorHumidity_Object((1,3,6,1,4,1,705,1,8,5,1,3),_MgsensorHumidity_Type())
mgsensorHumidity.setMaxAccess(_C)
if mibBuilder.loadTexts:mgsensorHumidity.setStatus(_A)
_UpsmgEnvironmentNum_Type=Integer32
_UpsmgEnvironmentNum_Object=MibScalar
upsmgEnvironmentNum=_UpsmgEnvironmentNum_Object((1,3,6,1,4,1,705,1,8,6),_UpsmgEnvironmentNum_Type())
upsmgEnvironmentNum.setMaxAccess(_C)
if mibBuilder.loadTexts:upsmgEnvironmentNum.setStatus(_A)
_UpsmgEnvironmentSensorTable_Object=MibTable
upsmgEnvironmentSensorTable=_UpsmgEnvironmentSensorTable_Object((1,3,6,1,4,1,705,1,8,7))
if mibBuilder.loadTexts:upsmgEnvironmentSensorTable.setStatus(_A)
_UpsmgEnvironmentSensorEntry_Object=MibTableRow
upsmgEnvironmentSensorEntry=_UpsmgEnvironmentSensorEntry_Object((1,3,6,1,4,1,705,1,8,7,1))
upsmgEnvironmentSensorEntry.setIndexNames((0,_E,_n))
if mibBuilder.loadTexts:upsmgEnvironmentSensorEntry.setStatus(_A)
class _UpsmgEnvironmentIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_UpsmgEnvironmentIndex_Type.__name__=_D
_UpsmgEnvironmentIndex_Object=MibTableColumn
upsmgEnvironmentIndex=_UpsmgEnvironmentIndex_Object((1,3,6,1,4,1,705,1,8,7,1,1),_UpsmgEnvironmentIndex_Type())
upsmgEnvironmentIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:upsmgEnvironmentIndex.setStatus(_A)
class _UpsmgEnvironmentComFailure_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_UpsmgEnvironmentComFailure_Type.__name__=_D
_UpsmgEnvironmentComFailure_Object=MibTableColumn
upsmgEnvironmentComFailure=_UpsmgEnvironmentComFailure_Object((1,3,6,1,4,1,705,1,8,7,1,2),_UpsmgEnvironmentComFailure_Type())
upsmgEnvironmentComFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:upsmgEnvironmentComFailure.setStatus(_A)
_UpsmgEnvironmentTemperature_Type=Integer32
_UpsmgEnvironmentTemperature_Object=MibTableColumn
upsmgEnvironmentTemperature=_UpsmgEnvironmentTemperature_Object((1,3,6,1,4,1,705,1,8,7,1,3),_UpsmgEnvironmentTemperature_Type())
upsmgEnvironmentTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:upsmgEnvironmentTemperature.setStatus(_A)
class _UpsmgEnvironmentTemperatureLow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_UpsmgEnvironmentTemperatureLow_Type.__name__=_D
_UpsmgEnvironmentTemperatureLow_Object=MibTableColumn
upsmgEnvironmentTemperatureLow=_UpsmgEnvironmentTemperatureLow_Object((1,3,6,1,4,1,705,1,8,7,1,4),_UpsmgEnvironmentTemperatureLow_Type())
upsmgEnvironmentTemperatureLow.setMaxAccess(_C)
if mibBuilder.loadTexts:upsmgEnvironmentTemperatureLow.setStatus(_A)
class _UpsmgEnvironmentTemperatureHigh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_UpsmgEnvironmentTemperatureHigh_Type.__name__=_D
_UpsmgEnvironmentTemperatureHigh_Object=MibTableColumn
upsmgEnvironmentTemperatureHigh=_UpsmgEnvironmentTemperatureHigh_Object((1,3,6,1,4,1,705,1,8,7,1,5),_UpsmgEnvironmentTemperatureHigh_Type())
upsmgEnvironmentTemperatureHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:upsmgEnvironmentTemperatureHigh.setStatus(_A)
_UpsmgEnvironmentHumidity_Type=Integer32
_UpsmgEnvironmentHumidity_Object=MibTableColumn
upsmgEnvironmentHumidity=_UpsmgEnvironmentHumidity_Object((1,3,6,1,4,1,705,1,8,7,1,6),_UpsmgEnvironmentHumidity_Type())
upsmgEnvironmentHumidity.setMaxAccess(_C)
if mibBuilder.loadTexts:upsmgEnvironmentHumidity.setStatus(_A)
class _UpsmgEnvironmentHumidityLow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_UpsmgEnvironmentHumidityLow_Type.__name__=_D
_UpsmgEnvironmentHumidityLow_Object=MibTableColumn
upsmgEnvironmentHumidityLow=_UpsmgEnvironmentHumidityLow_Object((1,3,6,1,4,1,705,1,8,7,1,7),_UpsmgEnvironmentHumidityLow_Type())
upsmgEnvironmentHumidityLow.setMaxAccess(_C)
if mibBuilder.loadTexts:upsmgEnvironmentHumidityLow.setStatus(_A)
class _UpsmgEnvironmentHumidityHigh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_UpsmgEnvironmentHumidityHigh_Type.__name__=_D
_UpsmgEnvironmentHumidityHigh_Object=MibTableColumn
upsmgEnvironmentHumidityHigh=_UpsmgEnvironmentHumidityHigh_Object((1,3,6,1,4,1,705,1,8,7,1,8),_UpsmgEnvironmentHumidityHigh_Type())
upsmgEnvironmentHumidityHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:upsmgEnvironmentHumidityHigh.setStatus(_A)
class _UpsmgEnvironmentInput1State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_o,1),('open',2)))
_UpsmgEnvironmentInput1State_Type.__name__=_D
_UpsmgEnvironmentInput1State_Object=MibTableColumn
upsmgEnvironmentInput1State=_UpsmgEnvironmentInput1State_Object((1,3,6,1,4,1,705,1,8,7,1,9),_UpsmgEnvironmentInput1State_Type())
upsmgEnvironmentInput1State.setMaxAccess(_C)
if mibBuilder.loadTexts:upsmgEnvironmentInput1State.setStatus(_A)
class _UpsmgEnvironmentInput2State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_o,1),('open',2)))
_UpsmgEnvironmentInput2State_Type.__name__=_D
_UpsmgEnvironmentInput2State_Object=MibTableColumn
upsmgEnvironmentInput2State=_UpsmgEnvironmentInput2State_Object((1,3,6,1,4,1,705,1,8,7,1,10),_UpsmgEnvironmentInput2State_Type())
upsmgEnvironmentInput2State.setMaxAccess(_C)
if mibBuilder.loadTexts:upsmgEnvironmentInput2State.setStatus(_A)
_UpsmgControl_ObjectIdentity=ObjectIdentity
upsmgControl=_UpsmgControl_ObjectIdentity((1,3,6,1,4,1,705,1,9))
_UpsmgControlReceptaclesTable_Object=MibTable
upsmgControlReceptaclesTable=_UpsmgControlReceptaclesTable_Object((1,3,6,1,4,1,705,1,9,1))
if mibBuilder.loadTexts:upsmgControlReceptaclesTable.setStatus(_A)
_UpsmgControlReceptaclesEntry_Object=MibTableRow
upsmgControlReceptaclesEntry=_UpsmgControlReceptaclesEntry_Object((1,3,6,1,4,1,705,1,9,1,1))
upsmgControlReceptaclesEntry.setIndexNames((0,_E,_p))
if mibBuilder.loadTexts:upsmgControlReceptaclesEntry.setStatus(_A)
class _MgreceptacleIndexc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_MgreceptacleIndexc_Type.__name__=_D
_MgreceptacleIndexc_Object=MibTableColumn
mgreceptacleIndexc=_MgreceptacleIndexc_Object((1,3,6,1,4,1,705,1,9,1,1,1),_MgreceptacleIndexc_Type())
mgreceptacleIndexc.setMaxAccess(_C)
if mibBuilder.loadTexts:mgreceptacleIndexc.setStatus(_A)
_MgreceptacleOnDelay_Type=Integer32
_MgreceptacleOnDelay_Object=MibTableColumn
mgreceptacleOnDelay=_MgreceptacleOnDelay_Object((1,3,6,1,4,1,705,1,9,1,1,2),_MgreceptacleOnDelay_Type())
mgreceptacleOnDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:mgreceptacleOnDelay.setStatus(_A)
class _MgreceptacleOnCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_N,2),(_W,3)))
_MgreceptacleOnCtrl_Type.__name__=_D
_MgreceptacleOnCtrl_Object=MibTableColumn
mgreceptacleOnCtrl=_MgreceptacleOnCtrl_Object((1,3,6,1,4,1,705,1,9,1,1,3),_MgreceptacleOnCtrl_Type())
mgreceptacleOnCtrl.setMaxAccess(_B)
if mibBuilder.loadTexts:mgreceptacleOnCtrl.setStatus(_A)
class _MgreceptacleOnStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),(_X,2),(_Y,3),(_Z,4)))
_MgreceptacleOnStatus_Type.__name__=_D
_MgreceptacleOnStatus_Object=MibTableColumn
mgreceptacleOnStatus=_MgreceptacleOnStatus_Object((1,3,6,1,4,1,705,1,9,1,1,4),_MgreceptacleOnStatus_Type())
mgreceptacleOnStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mgreceptacleOnStatus.setStatus(_A)
_MgreceptacleOffDelay_Type=Integer32
_MgreceptacleOffDelay_Object=MibTableColumn
mgreceptacleOffDelay=_MgreceptacleOffDelay_Object((1,3,6,1,4,1,705,1,9,1,1,5),_MgreceptacleOffDelay_Type())
mgreceptacleOffDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:mgreceptacleOffDelay.setStatus(_A)
class _MgreceptacleOffCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_N,2),(_W,3)))
_MgreceptacleOffCtrl_Type.__name__=_D
_MgreceptacleOffCtrl_Object=MibTableColumn
mgreceptacleOffCtrl=_MgreceptacleOffCtrl_Object((1,3,6,1,4,1,705,1,9,1,1,6),_MgreceptacleOffCtrl_Type())
mgreceptacleOffCtrl.setMaxAccess(_B)
if mibBuilder.loadTexts:mgreceptacleOffCtrl.setStatus(_A)
class _MgreceptacleOffStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),(_X,2),(_Y,3),(_Z,4)))
_MgreceptacleOffStatus_Type.__name__=_D
_MgreceptacleOffStatus_Object=MibTableColumn
mgreceptacleOffStatus=_MgreceptacleOffStatus_Object((1,3,6,1,4,1,705,1,9,1,1,7),_MgreceptacleOffStatus_Type())
mgreceptacleOffStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mgreceptacleOffStatus.setStatus(_A)
_MgreceptacleToggleDelay_Type=Integer32
_MgreceptacleToggleDelay_Object=MibTableColumn
mgreceptacleToggleDelay=_MgreceptacleToggleDelay_Object((1,3,6,1,4,1,705,1,9,1,1,8),_MgreceptacleToggleDelay_Type())
mgreceptacleToggleDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:mgreceptacleToggleDelay.setStatus(_A)
class _MgreceptacleToggleCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_N,2),(_W,3)))
_MgreceptacleToggleCtrl_Type.__name__=_D
_MgreceptacleToggleCtrl_Object=MibTableColumn
mgreceptacleToggleCtrl=_MgreceptacleToggleCtrl_Object((1,3,6,1,4,1,705,1,9,1,1,9),_MgreceptacleToggleCtrl_Type())
mgreceptacleToggleCtrl.setMaxAccess(_B)
if mibBuilder.loadTexts:mgreceptacleToggleCtrl.setStatus(_A)
class _MgreceptacleToggleStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),(_X,2),(_Y,3),(_Z,4)))
_MgreceptacleToggleStatus_Type.__name__=_D
_MgreceptacleToggleStatus_Object=MibTableColumn
mgreceptacleToggleStatus=_MgreceptacleToggleStatus_Object((1,3,6,1,4,1,705,1,9,1,1,10),_MgreceptacleToggleStatus_Type())
mgreceptacleToggleStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mgreceptacleToggleStatus.setStatus(_A)
_MgreceptacleToggleDuration_Type=Integer32
_MgreceptacleToggleDuration_Object=MibTableColumn
mgreceptacleToggleDuration=_MgreceptacleToggleDuration_Object((1,3,6,1,4,1,705,1,9,1,1,11),_MgreceptacleToggleDuration_Type())
mgreceptacleToggleDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:mgreceptacleToggleDuration.setStatus(_A)
class _UpsmgControlDayOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_q,1),(_r,2),(_s,3),(_t,4),(_u,5),(_v,6),(_w,7),(_J,8)))
_UpsmgControlDayOff_Type.__name__=_D
_UpsmgControlDayOff_Object=MibScalar
upsmgControlDayOff=_UpsmgControlDayOff_Object((1,3,6,1,4,1,705,1,9,2),_UpsmgControlDayOff_Type())
upsmgControlDayOff.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgControlDayOff.setStatus(_A)
class _UpsmgControlDayOn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_q,1),(_r,2),(_s,3),(_t,4),(_u,5),(_v,6),(_w,7),(_J,8)))
_UpsmgControlDayOn_Type.__name__=_D
_UpsmgControlDayOn_Object=MibScalar
upsmgControlDayOn=_UpsmgControlDayOn_Object((1,3,6,1,4,1,705,1,9,3),_UpsmgControlDayOn_Type())
upsmgControlDayOn.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgControlDayOn.setStatus(_A)
_UpsmgTest_ObjectIdentity=ObjectIdentity
upsmgTest=_UpsmgTest_ObjectIdentity((1,3,6,1,4,1,705,1,10))
class _UpsmgTestBatterySchedule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('unknown',1),('weekly',2),('monthly',3),('atturnon',4),(_J,5),('dayly',6)))
_UpsmgTestBatterySchedule_Type.__name__=_D
_UpsmgTestBatterySchedule_Object=MibScalar
upsmgTestBatterySchedule=_UpsmgTestBatterySchedule_Object((1,3,6,1,4,1,705,1,10,1),_UpsmgTestBatterySchedule_Type())
upsmgTestBatterySchedule.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgTestBatterySchedule.setStatus(_A)
class _UpsmgTestDiagnostics_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_x,1),(_N,2)))
_UpsmgTestDiagnostics_Type.__name__=_D
_UpsmgTestDiagnostics_Object=MibScalar
upsmgTestDiagnostics=_UpsmgTestDiagnostics_Object((1,3,6,1,4,1,705,1,10,2),_UpsmgTestDiagnostics_Type())
upsmgTestDiagnostics.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgTestDiagnostics.setStatus(_A)
class _UpsmgTestDiagResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('success',1),('failed',2),(_J,3)))
_UpsmgTestDiagResult_Type.__name__=_D
_UpsmgTestDiagResult_Object=MibScalar
upsmgTestDiagResult=_UpsmgTestDiagResult_Object((1,3,6,1,4,1,705,1,10,3),_UpsmgTestDiagResult_Type())
upsmgTestDiagResult.setMaxAccess(_C)
if mibBuilder.loadTexts:upsmgTestDiagResult.setStatus(_A)
class _UpsmgTestBatteryCalibration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_x,1),(_N,2)))
_UpsmgTestBatteryCalibration_Type.__name__=_D
_UpsmgTestBatteryCalibration_Object=MibScalar
upsmgTestBatteryCalibration=_UpsmgTestBatteryCalibration_Object((1,3,6,1,4,1,705,1,10,4),_UpsmgTestBatteryCalibration_Type())
upsmgTestBatteryCalibration.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgTestBatteryCalibration.setStatus(_A)
_UpsmgTestLastCalibration_Type=Integer32
_UpsmgTestLastCalibration_Object=MibScalar
upsmgTestLastCalibration=_UpsmgTestLastCalibration_Object((1,3,6,1,4,1,705,1,10,5),_UpsmgTestLastCalibration_Type())
upsmgTestLastCalibration.setMaxAccess(_C)
if mibBuilder.loadTexts:upsmgTestLastCalibration.setStatus(_A)
_UpsmgTestIndicators_Type=Integer32
_UpsmgTestIndicators_Object=MibScalar
upsmgTestIndicators=_UpsmgTestIndicators_Object((1,3,6,1,4,1,705,1,10,6),_UpsmgTestIndicators_Type())
upsmgTestIndicators.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgTestIndicators.setStatus(_A)
class _UpsmgTestCommandLine_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_UpsmgTestCommandLine_Type.__name__=_H
_UpsmgTestCommandLine_Object=MibScalar
upsmgTestCommandLine=_UpsmgTestCommandLine_Object((1,3,6,1,4,1,705,1,10,7),_UpsmgTestCommandLine_Type())
upsmgTestCommandLine.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgTestCommandLine.setStatus(_A)
class _UpsmgTestCommandReady_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_UpsmgTestCommandReady_Type.__name__=_D
_UpsmgTestCommandReady_Object=MibScalar
upsmgTestCommandReady=_UpsmgTestCommandReady_Object((1,3,6,1,4,1,705,1,10,8),_UpsmgTestCommandReady_Type())
upsmgTestCommandReady.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgTestCommandReady.setStatus(_A)
class _UpsmgTestResponseLine_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_UpsmgTestResponseLine_Type.__name__=_H
_UpsmgTestResponseLine_Object=MibScalar
upsmgTestResponseLine=_UpsmgTestResponseLine_Object((1,3,6,1,4,1,705,1,10,9),_UpsmgTestResponseLine_Type())
upsmgTestResponseLine.setMaxAccess(_C)
if mibBuilder.loadTexts:upsmgTestResponseLine.setStatus(_A)
class _UpsmgTestResponseReady_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_UpsmgTestResponseReady_Type.__name__=_D
_UpsmgTestResponseReady_Object=MibScalar
upsmgTestResponseReady=_UpsmgTestResponseReady_Object((1,3,6,1,4,1,705,1,10,10),_UpsmgTestResponseReady_Type())
upsmgTestResponseReady.setMaxAccess(_C)
if mibBuilder.loadTexts:upsmgTestResponseReady.setStatus(_A)
class _UpsmgTestBatteryResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('msuccess',1),('mfailed',2),('ssuccess',3),('sfailed',4),(_J,5)))
_UpsmgTestBatteryResult_Type.__name__=_D
_UpsmgTestBatteryResult_Object=MibScalar
upsmgTestBatteryResult=_UpsmgTestBatteryResult_Object((1,3,6,1,4,1,705,1,10,11),_UpsmgTestBatteryResult_Type())
upsmgTestBatteryResult.setMaxAccess(_C)
if mibBuilder.loadTexts:upsmgTestBatteryResult.setStatus(_A)
_UpsmgTraps_ObjectIdentity=ObjectIdentity
upsmgTraps=_UpsmgTraps_ObjectIdentity((1,3,6,1,4,1,705,1,11))
_UpsmgAgent_ObjectIdentity=ObjectIdentity
upsmgAgent=_UpsmgAgent_ObjectIdentity((1,3,6,1,4,1,705,1,12))
_UpsmgAgentIpaddress_Type=IpAddress
_UpsmgAgentIpaddress_Object=MibScalar
upsmgAgentIpaddress=_UpsmgAgentIpaddress_Object((1,3,6,1,4,1,705,1,12,1),_UpsmgAgentIpaddress_Type())
upsmgAgentIpaddress.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgAgentIpaddress.setStatus(_A)
_UpsmgAgentSubnetMask_Type=IpAddress
_UpsmgAgentSubnetMask_Object=MibScalar
upsmgAgentSubnetMask=_UpsmgAgentSubnetMask_Object((1,3,6,1,4,1,705,1,12,2),_UpsmgAgentSubnetMask_Type())
upsmgAgentSubnetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgAgentSubnetMask.setStatus(_A)
_UpsmgAgentDefGateway_Type=IpAddress
_UpsmgAgentDefGateway_Object=MibScalar
upsmgAgentDefGateway=_UpsmgAgentDefGateway_Object((1,3,6,1,4,1,705,1,12,3),_UpsmgAgentDefGateway_Type())
upsmgAgentDefGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgAgentDefGateway.setStatus(_A)
_UpsmgAgentBaudRate_Type=Integer32
_UpsmgAgentBaudRate_Object=MibScalar
upsmgAgentBaudRate=_UpsmgAgentBaudRate_Object((1,3,6,1,4,1,705,1,12,4),_UpsmgAgentBaudRate_Type())
upsmgAgentBaudRate.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgAgentBaudRate.setStatus(_A)
_UpsmgAgentPollRate_Type=Integer32
_UpsmgAgentPollRate_Object=MibScalar
upsmgAgentPollRate=_UpsmgAgentPollRate_Object((1,3,6,1,4,1,705,1,12,5),_UpsmgAgentPollRate_Type())
upsmgAgentPollRate.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgAgentPollRate.setStatus(_A)
class _UpsmgAgentType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('deviceEth',1),('deviceTR',2),('proxyEth',3),('proxyTR',4),(_S,5)))
_UpsmgAgentType_Type.__name__=_D
_UpsmgAgentType_Object=MibScalar
upsmgAgentType=_UpsmgAgentType_Object((1,3,6,1,4,1,705,1,12,6),_UpsmgAgentType_Type())
upsmgAgentType.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgAgentType.setStatus(_A)
_UpsmgAgentTrapAlarmDelay_Type=Integer32
_UpsmgAgentTrapAlarmDelay_Object=MibScalar
upsmgAgentTrapAlarmDelay=_UpsmgAgentTrapAlarmDelay_Object((1,3,6,1,4,1,705,1,12,7),_UpsmgAgentTrapAlarmDelay_Type())
upsmgAgentTrapAlarmDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgAgentTrapAlarmDelay.setStatus(_A)
_UpsmgAgentTrapAlarmRetry_Type=Integer32
_UpsmgAgentTrapAlarmRetry_Object=MibScalar
upsmgAgentTrapAlarmRetry=_UpsmgAgentTrapAlarmRetry_Object((1,3,6,1,4,1,705,1,12,8),_UpsmgAgentTrapAlarmRetry_Type())
upsmgAgentTrapAlarmRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgAgentTrapAlarmRetry.setStatus(_A)
class _UpsmgAgentReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('reset',1),(_M,2)))
_UpsmgAgentReset_Type.__name__=_D
_UpsmgAgentReset_Object=MibScalar
upsmgAgentReset=_UpsmgAgentReset_Object((1,3,6,1,4,1,705,1,12,9),_UpsmgAgentReset_Type())
upsmgAgentReset.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgAgentReset.setStatus(_A)
class _UpsmgAgentFactReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('reset',1),(_M,2)))
_UpsmgAgentFactReset_Type.__name__=_D
_UpsmgAgentFactReset_Object=MibScalar
upsmgAgentFactReset=_UpsmgAgentFactReset_Object((1,3,6,1,4,1,705,1,12,10),_UpsmgAgentFactReset_Type())
upsmgAgentFactReset.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgAgentFactReset.setStatus(_A)
_UpsmgAgentMibVersion_Type=Integer32
_UpsmgAgentMibVersion_Object=MibScalar
upsmgAgentMibVersion=_UpsmgAgentMibVersion_Object((1,3,6,1,4,1,705,1,12,11),_UpsmgAgentMibVersion_Type())
upsmgAgentMibVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:upsmgAgentMibVersion.setStatus(_A)
class _UpsmgAgentFirmwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_UpsmgAgentFirmwareVersion_Type.__name__=_H
_UpsmgAgentFirmwareVersion_Object=MibScalar
upsmgAgentFirmwareVersion=_UpsmgAgentFirmwareVersion_Object((1,3,6,1,4,1,705,1,12,12),_UpsmgAgentFirmwareVersion_Type())
upsmgAgentFirmwareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:upsmgAgentFirmwareVersion.setStatus(_A)
_UpsmgAgentCommUPS_Type=Integer32
_UpsmgAgentCommUPS_Object=MibScalar
upsmgAgentCommUPS=_UpsmgAgentCommUPS_Object((1,3,6,1,4,1,705,1,12,13),_UpsmgAgentCommUPS_Type())
upsmgAgentCommUPS.setMaxAccess(_C)
if mibBuilder.loadTexts:upsmgAgentCommUPS.setStatus(_A)
_UpsmgAgentTrapAck_Type=Integer32
_UpsmgAgentTrapAck_Object=MibScalar
upsmgAgentTrapAck=_UpsmgAgentTrapAck_Object((1,3,6,1,4,1,705,1,12,14),_UpsmgAgentTrapAck_Type())
upsmgAgentTrapAck.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgAgentTrapAck.setStatus(_A)
class _UpsmgAgentAutoLearning_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_UpsmgAgentAutoLearning_Type.__name__=_D
_UpsmgAgentAutoLearning_Object=MibScalar
upsmgAgentAutoLearning=_UpsmgAgentAutoLearning_Object((1,3,6,1,4,1,705,1,12,15),_UpsmgAgentAutoLearning_Type())
upsmgAgentAutoLearning.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgAgentAutoLearning.setStatus(_A)
class _UpsmgAgentBootP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_UpsmgAgentBootP_Type.__name__=_D
_UpsmgAgentBootP_Object=MibScalar
upsmgAgentBootP=_UpsmgAgentBootP_Object((1,3,6,1,4,1,705,1,12,16),_UpsmgAgentBootP_Type())
upsmgAgentBootP.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgAgentBootP.setStatus(_A)
class _UpsmgAgentTFTP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_UpsmgAgentTFTP_Type.__name__=_D
_UpsmgAgentTFTP_Object=MibScalar
upsmgAgentTFTP=_UpsmgAgentTFTP_Object((1,3,6,1,4,1,705,1,12,17),_UpsmgAgentTFTP_Type())
upsmgAgentTFTP.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgAgentTFTP.setStatus(_A)
_UpsmgAgentTrapSignature_Type=Integer32
_UpsmgAgentTrapSignature_Object=MibScalar
upsmgAgentTrapSignature=_UpsmgAgentTrapSignature_Object((1,3,6,1,4,1,705,1,12,18),_UpsmgAgentTrapSignature_Type())
upsmgAgentTrapSignature.setMaxAccess(_C)
if mibBuilder.loadTexts:upsmgAgentTrapSignature.setStatus(_A)
_UpsmgRemote_ObjectIdentity=ObjectIdentity
upsmgRemote=_UpsmgRemote_ObjectIdentity((1,3,6,1,4,1,705,1,13))
_UpsmgRemoteOnBattery_Type=Integer32
_UpsmgRemoteOnBattery_Object=MibScalar
upsmgRemoteOnBattery=_UpsmgRemoteOnBattery_Object((1,3,6,1,4,1,705,1,13,1),_UpsmgRemoteOnBattery_Type())
upsmgRemoteOnBattery.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgRemoteOnBattery.setStatus(_A)
_UpsmgRemoteIpAddress_Type=IpAddress
_UpsmgRemoteIpAddress_Object=MibScalar
upsmgRemoteIpAddress=_UpsmgRemoteIpAddress_Object((1,3,6,1,4,1,705,1,13,2),_UpsmgRemoteIpAddress_Type())
upsmgRemoteIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:upsmgRemoteIpAddress.setStatus(_A)
upsmgBatteryFault=NotificationType((1,3,6,1,4,1,705,1,11,0,1))
if mibBuilder.loadTexts:upsmgBatteryFault.setStatus('')
upsmgBatteryOK=NotificationType((1,3,6,1,4,1,705,1,11,0,2))
if mibBuilder.loadTexts:upsmgBatteryOK.setStatus('')
upsmgBatteryReplacementIndicated=NotificationType((1,3,6,1,4,1,705,1,11,0,3))
if mibBuilder.loadTexts:upsmgBatteryReplacementIndicated.setStatus('')
upsmgBatteryReplaceNotIndicated=NotificationType((1,3,6,1,4,1,705,1,11,0,4))
if mibBuilder.loadTexts:upsmgBatteryReplaceNotIndicated.setStatus('')
upsmgAtLowBattery=NotificationType((1,3,6,1,4,1,705,1,11,0,5))
upsmgAtLowBattery.setObjects(*((_E,_K),(_E,_L)))
if mibBuilder.loadTexts:upsmgAtLowBattery.setStatus('')
upsmgFromLowBattery=NotificationType((1,3,6,1,4,1,705,1,11,0,6))
upsmgFromLowBattery.setObjects(*((_E,_K),(_E,_L)))
if mibBuilder.loadTexts:upsmgFromLowBattery.setStatus('')
upsmgChargerFault=NotificationType((1,3,6,1,4,1,705,1,11,0,7))
if mibBuilder.loadTexts:upsmgChargerFault.setStatus('')
upsmgChargerOK=NotificationType((1,3,6,1,4,1,705,1,11,0,8))
if mibBuilder.loadTexts:upsmgChargerOK.setStatus('')
upsmgAtLowCondition=NotificationType((1,3,6,1,4,1,705,1,11,0,9))
upsmgAtLowCondition.setObjects(*((_E,_K),(_E,_L)))
if mibBuilder.loadTexts:upsmgAtLowCondition.setStatus('')
upsmgFromLowCondition=NotificationType((1,3,6,1,4,1,705,1,11,0,10))
upsmgFromLowCondition.setObjects(*((_E,_K),(_E,_L)))
if mibBuilder.loadTexts:upsmgFromLowCondition.setStatus('')
upsmgOnBattery=NotificationType((1,3,6,1,4,1,705,1,11,0,11))
upsmgOnBattery.setObjects(*((_E,_K),(_E,_L)))
if mibBuilder.loadTexts:upsmgOnBattery.setStatus('')
upsmgReturnFromBattery=NotificationType((1,3,6,1,4,1,705,1,11,0,12))
upsmgReturnFromBattery.setObjects(*((_E,_K),(_E,_L)))
if mibBuilder.loadTexts:upsmgReturnFromBattery.setStatus('')
upsmgOnByPass=NotificationType((1,3,6,1,4,1,705,1,11,0,13))
if mibBuilder.loadTexts:upsmgOnByPass.setStatus('')
upsmgReturnFromByPass=NotificationType((1,3,6,1,4,1,705,1,11,0,14))
if mibBuilder.loadTexts:upsmgReturnFromByPass.setStatus('')
upsmgByPassUnavailable=NotificationType((1,3,6,1,4,1,705,1,11,0,15))
if mibBuilder.loadTexts:upsmgByPassUnavailable.setStatus('')
upsmgByPassAvailable=NotificationType((1,3,6,1,4,1,705,1,11,0,16))
if mibBuilder.loadTexts:upsmgByPassAvailable.setStatus('')
upsmgUtilityFailure=NotificationType((1,3,6,1,4,1,705,1,11,0,17))
if mibBuilder.loadTexts:upsmgUtilityFailure.setStatus('')
upsmgUtilityRestored=NotificationType((1,3,6,1,4,1,705,1,11,0,18))
if mibBuilder.loadTexts:upsmgUtilityRestored.setStatus('')
upsmgOnBoost=NotificationType((1,3,6,1,4,1,705,1,11,0,19))
if mibBuilder.loadTexts:upsmgOnBoost.setStatus('')
upsmgReturnFromBoost=NotificationType((1,3,6,1,4,1,705,1,11,0,20))
if mibBuilder.loadTexts:upsmgReturnFromBoost.setStatus('')
upsmgOverLoad=NotificationType((1,3,6,1,4,1,705,1,11,0,21))
if mibBuilder.loadTexts:upsmgOverLoad.setStatus('')
upsmgLoadOK=NotificationType((1,3,6,1,4,1,705,1,11,0,22))
if mibBuilder.loadTexts:upsmgLoadOK.setStatus('')
upsmgOverTemperature=NotificationType((1,3,6,1,4,1,705,1,11,0,23))
if mibBuilder.loadTexts:upsmgOverTemperature.setStatus('')
upsmgTemperatureOK=NotificationType((1,3,6,1,4,1,705,1,11,0,24))
if mibBuilder.loadTexts:upsmgTemperatureOK.setStatus('')
upsmgOnToStart=NotificationType((1,3,6,1,4,1,705,1,11,0,25))
upsmgOnToStart.setObjects(*((_E,_I),(_E,_O),(_E,_Q),(_E,_y)))
if mibBuilder.loadTexts:upsmgOnToStart.setStatus('')
upsmgOnAbort=NotificationType((1,3,6,1,4,1,705,1,11,0,26))
upsmgOnAbort.setObjects(*((_E,_I),(_E,_Q)))
if mibBuilder.loadTexts:upsmgOnAbort.setStatus('')
upsmgOnInProgress=NotificationType((1,3,6,1,4,1,705,1,11,0,27))
upsmgOnInProgress.setObjects(*((_E,_I),(_E,_O),(_E,_z)))
if mibBuilder.loadTexts:upsmgOnInProgress.setStatus('')
upsmgOnComplete=NotificationType((1,3,6,1,4,1,705,1,11,0,28))
upsmgOnComplete.setObjects(*((_E,_I),(_E,_Q)))
if mibBuilder.loadTexts:upsmgOnComplete.setStatus('')
upsmgOffToStart=NotificationType((1,3,6,1,4,1,705,1,11,0,29))
upsmgOffToStart.setObjects(*((_E,_I),(_E,_O),(_E,_R),(_E,_A0),(_E,_A1)))
if mibBuilder.loadTexts:upsmgOffToStart.setStatus('')
upsmgOffAbort=NotificationType((1,3,6,1,4,1,705,1,11,0,30))
upsmgOffAbort.setObjects(*((_E,_I),(_E,_R)))
if mibBuilder.loadTexts:upsmgOffAbort.setStatus('')
upsmgOffInProgress=NotificationType((1,3,6,1,4,1,705,1,11,0,31))
upsmgOffInProgress.setObjects(*((_E,_I),(_E,_O),(_E,_A2)))
if mibBuilder.loadTexts:upsmgOffInProgress.setStatus('')
upsmgOffComplete=NotificationType((1,3,6,1,4,1,705,1,11,0,32))
upsmgOffComplete.setObjects(*((_E,_I),(_E,_R)))
if mibBuilder.loadTexts:upsmgOffComplete.setStatus('')
upsmgToggleToStart=NotificationType((1,3,6,1,4,1,705,1,11,0,33))
upsmgToggleToStart.setObjects(*((_E,_I),(_E,_a)))
if mibBuilder.loadTexts:upsmgToggleToStart.setStatus('')
upsmgToggleAbort=NotificationType((1,3,6,1,4,1,705,1,11,0,34))
upsmgToggleAbort.setObjects(*((_E,_I),(_E,_a)))
if mibBuilder.loadTexts:upsmgToggleAbort.setStatus('')
upsmgToggleInProgress=NotificationType((1,3,6,1,4,1,705,1,11,0,35))
upsmgToggleInProgress.setObjects(*((_E,_I),(_E,_b)))
if mibBuilder.loadTexts:upsmgToggleInProgress.setStatus('')
upsmgToggleComplete=NotificationType((1,3,6,1,4,1,705,1,11,0,36))
upsmgToggleComplete.setObjects(*((_E,_I),(_E,_b)))
if mibBuilder.loadTexts:upsmgToggleComplete.setStatus('')
upsmgCommunicationFailure=NotificationType((1,3,6,1,4,1,705,1,11,0,37))
if mibBuilder.loadTexts:upsmgCommunicationFailure.setStatus('')
upsmgCommunicationRestored=NotificationType((1,3,6,1,4,1,705,1,11,0,38))
if mibBuilder.loadTexts:upsmgCommunicationRestored.setStatus('')
upsmgInputBad=NotificationType((1,3,6,1,4,1,705,1,11,0,39))
if mibBuilder.loadTexts:upsmgInputBad.setStatus('')
upsmgInputOK=NotificationType((1,3,6,1,4,1,705,1,11,0,40))
if mibBuilder.loadTexts:upsmgInputOK.setStatus('')
upsmgBatteryUnavailable=NotificationType((1,3,6,1,4,1,705,1,11,0,41))
if mibBuilder.loadTexts:upsmgBatteryUnavailable.setStatus('')
upsmgBatteryAvailable=NotificationType((1,3,6,1,4,1,705,1,11,0,42))
if mibBuilder.loadTexts:upsmgBatteryAvailable.setStatus('')
upsmgAtLowRecharge=NotificationType((1,3,6,1,4,1,705,1,11,0,43))
upsmgAtLowRecharge.setObjects(*((_E,_K),(_E,_L)))
if mibBuilder.loadTexts:upsmgAtLowRecharge.setStatus('')
upsmgFromLowRecharge=NotificationType((1,3,6,1,4,1,705,1,11,0,44))
upsmgFromLowRecharge.setObjects(*((_E,_K),(_E,_L)))
if mibBuilder.loadTexts:upsmgFromLowRecharge.setStatus('')
upsmgDiagnosticTestFail=NotificationType((1,3,6,1,4,1,705,1,11,0,45))
if mibBuilder.loadTexts:upsmgDiagnosticTestFail.setStatus('')
upsmgDiagnosticTestOK=NotificationType((1,3,6,1,4,1,705,1,11,0,46))
if mibBuilder.loadTexts:upsmgDiagnosticTestOK.setStatus('')
upsmgBatteryTestOK=NotificationType((1,3,6,1,4,1,705,1,11,0,47))
if mibBuilder.loadTexts:upsmgBatteryTestOK.setStatus('')
upsmgBatteryTestFail=NotificationType((1,3,6,1,4,1,705,1,11,0,48))
if mibBuilder.loadTexts:upsmgBatteryTestFail.setStatus('')
upsmgExternalAlarmActive=NotificationType((1,3,6,1,4,1,705,1,11,0,49))
upsmgExternalAlarmActive.setObjects(*((_E,_P),(_E,_c)))
if mibBuilder.loadTexts:upsmgExternalAlarmActive.setStatus('')
upsmgExternalAlarmInactive=NotificationType((1,3,6,1,4,1,705,1,11,0,50))
upsmgExternalAlarmInactive.setObjects(*((_E,_P),(_E,_c)))
if mibBuilder.loadTexts:upsmgExternalAlarmInactive.setStatus('')
upsmgOnBuck=NotificationType((1,3,6,1,4,1,705,1,11,0,51))
if mibBuilder.loadTexts:upsmgOnBuck.setStatus('')
upsmgReturnFromBuck=NotificationType((1,3,6,1,4,1,705,1,11,0,52))
if mibBuilder.loadTexts:upsmgReturnFromBuck.setStatus('')
upsmgEnvironComFailure=NotificationType((1,3,6,1,4,1,705,1,11,0,53))
if mibBuilder.loadTexts:upsmgEnvironComFailure.setStatus('')
upsmgEnvironComOK=NotificationType((1,3,6,1,4,1,705,1,11,0,54))
if mibBuilder.loadTexts:upsmgEnvironComOK.setStatus('')
upsmgEnvironTemperatureLow=NotificationType((1,3,6,1,4,1,705,1,11,0,55))
if mibBuilder.loadTexts:upsmgEnvironTemperatureLow.setStatus('')
upsmgEnvironTemperatureHigh=NotificationType((1,3,6,1,4,1,705,1,11,0,56))
if mibBuilder.loadTexts:upsmgEnvironTemperatureHigh.setStatus('')
upsmgEnvironTemperatureOK=NotificationType((1,3,6,1,4,1,705,1,11,0,57))
if mibBuilder.loadTexts:upsmgEnvironTemperatureOK.setStatus('')
upsmgEnvironHumidityLow=NotificationType((1,3,6,1,4,1,705,1,11,0,58))
if mibBuilder.loadTexts:upsmgEnvironHumidityLow.setStatus('')
upsmgEnvironHumidityHigh=NotificationType((1,3,6,1,4,1,705,1,11,0,59))
if mibBuilder.loadTexts:upsmgEnvironHumidityHigh.setStatus('')
upsmgEnvironHumidityOK=NotificationType((1,3,6,1,4,1,705,1,11,0,60))
if mibBuilder.loadTexts:upsmgEnvironHumidityOK.setStatus('')
upsmgEnvironInput1Closed=NotificationType((1,3,6,1,4,1,705,1,11,0,61))
if mibBuilder.loadTexts:upsmgEnvironInput1Closed.setStatus('')
upsmgEnvironInput1Open=NotificationType((1,3,6,1,4,1,705,1,11,0,62))
if mibBuilder.loadTexts:upsmgEnvironInput1Open.setStatus('')
upsmgEnvironInput2Closed=NotificationType((1,3,6,1,4,1,705,1,11,0,63))
if mibBuilder.loadTexts:upsmgEnvironInput2Closed.setStatus('')
upsmgEnvironInput2Open=NotificationType((1,3,6,1,4,1,705,1,11,0,64))
if mibBuilder.loadTexts:upsmgEnvironInput2Open.setStatus('')
upsRedundancyLost=NotificationType((1,3,6,1,4,1,705,1,11,0,65))
if mibBuilder.loadTexts:upsRedundancyLost.setStatus('')
upsRedundancyOK=NotificationType((1,3,6,1,4,1,705,1,11,0,66))
if mibBuilder.loadTexts:upsRedundancyOK.setStatus('')
upsProtectionLost=NotificationType((1,3,6,1,4,1,705,1,11,0,67))
if mibBuilder.loadTexts:upsProtectionLost.setStatus('')
upsProtectionOK=NotificationType((1,3,6,1,4,1,705,1,11,0,68))
if mibBuilder.loadTexts:upsProtectionOK.setStatus('')
mibBuilder.exportSymbols(_E,**{'merlinGerin':merlinGerin,'upsmg':upsmg,'upsmgIdent':upsmgIdent,'upsmgIdentFamilyName':upsmgIdentFamilyName,'upsmgIdentModelName':upsmgIdentModelName,'upsmgIdentRevisionLevel':upsmgIdentRevisionLevel,'upsmgIdentFirmwareVersion':upsmgIdentFirmwareVersion,'upsmgIdentUserID':upsmgIdentUserID,'upsmgIdentInstallationDate':upsmgIdentInstallationDate,'upsmgIdentSerialNumber':upsmgIdentSerialNumber,'upsmgManagement':upsmgManagement,'upsmgManagersNum':upsmgManagersNum,'upsmgManagersTable':upsmgManagersTable,'upsmgManagersEntry':upsmgManagersEntry,_e:mgmanagerIndex,'mgmanagerDeviceNumber':mgmanagerDeviceNumber,'mgmanagerNMSType':mgmanagerNMSType,'mgmanagerCommType':mgmanagerCommType,'mgmanagerDescr':mgmanagerDescr,'mgmanagerAddress':mgmanagerAddress,'mgmanagerCommunity':mgmanagerCommunity,'mgmanagerSeverityLevel':mgmanagerSeverityLevel,'mgmanagerTrapAck':mgmanagerTrapAck,'upsmgReceptacle':upsmgReceptacle,'upsmgReceptaclesNum':upsmgReceptaclesNum,'upsmgReceptaclesTable':upsmgReceptaclesTable,'upsmgReceptaclesEntry':upsmgReceptaclesEntry,_I:mgreceptacleIndex,'mgreceptacleLevel':mgreceptacleLevel,'mgreceptacleType':mgreceptacleType,'mgreceptacleIdent':mgreceptacleIdent,_O:mgreceptacleState,'mgreceptacleReceptacle':mgreceptacleReceptacle,'mgreceptaclePowerCons':mgreceptaclePowerCons,'mgreceptacleOverload':mgreceptacleOverload,'mgreceptacleAutonomy':mgreceptacleAutonomy,'upsmgConfig':upsmgConfig,'upsmgConfigBatteryInstalled':upsmgConfigBatteryInstalled,'upsmgConfigNominalBatteryVoltage':upsmgConfigNominalBatteryVoltage,'upsmgConfigNominalBatteryTime':upsmgConfigNominalBatteryTime,'upsmgConfigNominalRechargeTime':upsmgConfigNominalRechargeTime,'upsmgConfigMinRechargeLevel':upsmgConfigMinRechargeLevel,'upsmgConfigMaxRechargeTime':upsmgConfigMaxRechargeTime,'upsmgConfigLowBatteryTime':upsmgConfigLowBatteryTime,'upsmgConfigLowBatteryLevel':upsmgConfigLowBatteryLevel,'upsmgConfigAutoRestart':upsmgConfigAutoRestart,'upsmgConfigShutdownTimer':upsmgConfigShutdownTimer,_A1:upsmgConfigSysShutDuration,'upsmgConfigVARating':upsmgConfigVARating,'upsmgConfigLowTransfer':upsmgConfigLowTransfer,'upsmgConfigHighTransfer':upsmgConfigHighTransfer,'upsmgConfigOutputNominalVoltage':upsmgConfigOutputNominalVoltage,'upsmgConfigOutputNominalCurrent':upsmgConfigOutputNominalCurrent,'upsmgConfigOutputNomFrequency':upsmgConfigOutputNomFrequency,'upsmgConfigByPassType':upsmgConfigByPassType,'upsmgConfigAlarmAudible':upsmgConfigAlarmAudible,'upsmgConfigAlarmTimeDelay':upsmgConfigAlarmTimeDelay,'upsmgConfigDevicesNum':upsmgConfigDevicesNum,'upsmgConfigDevicesTable':upsmgConfigDevicesTable,'upsmgConfigDevicesEntry':upsmgConfigDevicesEntry,_f:mgdeviceIndex,'mgdeviceReceptacleNum':mgdeviceReceptacleNum,'mgdeviceIdent':mgdeviceIdent,'mgdeviceVaRating':mgdeviceVaRating,'mgdeviceSequenceOff':mgdeviceSequenceOff,'mgdeviceSequenceOn':mgdeviceSequenceOn,'mgdeviceShutdownDuration':mgdeviceShutdownDuration,'mgdeviceBootUpDuration':mgdeviceBootUpDuration,'upsmgConfigReceptaclesTable':upsmgConfigReceptaclesTable,'upsmgConfigReceptaclesEntry':upsmgConfigReceptaclesEntry,_g:mgreceptacleIndexb,'mgreceptacleStateTurnOn':mgreceptacleStateTurnOn,'mgreceptacleStateMainReturn':mgreceptacleStateMainReturn,'mgreceptacleStateDischarge':mgreceptacleStateDischarge,'mgreceptacleShutoffLevel':mgreceptacleShutoffLevel,_A0:mgreceptacleShutoffTimer,'mgreceptacleRestartLevel':mgreceptacleRestartLevel,_y:mgreceptacleRestartDelay,_A2:mgreceptacleShutdownDuration,_z:mgreceptacleBootUpDuration,'upsmgConfigExtAlarmNum':upsmgConfigExtAlarmNum,'upsmgConfigExtAlarmTable':upsmgConfigExtAlarmTable,'upsmgConfigExtAlarmEntry':upsmgConfigExtAlarmEntry,_P:mgextAlarmIndex,_c:mgextAlarmUID,'upsmgConfigEmergencyTestFail':upsmgConfigEmergencyTestFail,'upsmgConfigEmergencyOnByPass':upsmgConfigEmergencyOnByPass,'upsmgConfigEmergencyOverload':upsmgConfigEmergencyOverload,'upsmgConfigControlDayTable':upsmgConfigControlDayTable,'upsmgConfigControlDayEntry':upsmgConfigControlDayEntry,_h:mgcontrolDayIndex,'mgcontrolDayOn':mgcontrolDayOn,'mgcontrolDayOff':mgcontrolDayOff,'upsmgConfigLowBooster':upsmgConfigLowBooster,'upsmgConfigHighBooster':upsmgConfigHighBooster,'upsmgConfigLowFader':upsmgConfigLowFader,'upsmgConfigHighFader':upsmgConfigHighFader,'upsmgConfigEnvironmentTable':upsmgConfigEnvironmentTable,'upsmgConfigEnvironmentEntry':upsmgConfigEnvironmentEntry,_i:upsmgConfigSensorIndex,'upsmgConfigSensorName':upsmgConfigSensorName,'upsmgConfigTemperatureLow':upsmgConfigTemperatureLow,'upsmgConfigTemperatureHigh':upsmgConfigTemperatureHigh,'upsmgConfigTemperatureHysteresis':upsmgConfigTemperatureHysteresis,'upsmgConfigHumidityLow':upsmgConfigHumidityLow,'upsmgConfigHumidityHigh':upsmgConfigHumidityHigh,'upsmgConfigHumidityHysteresis':upsmgConfigHumidityHysteresis,'upsmgConfigInput1Name':upsmgConfigInput1Name,'upsmgConfigInput1ClosedLabel':upsmgConfigInput1ClosedLabel,'upsmgConfigInput1OpenLabel':upsmgConfigInput1OpenLabel,'upsmgConfigInput2Name':upsmgConfigInput2Name,'upsmgConfigInput2ClosedLabel':upsmgConfigInput2ClosedLabel,'upsmgConfigInput2OpenLabel':upsmgConfigInput2OpenLabel,'upsmgBattery':upsmgBattery,_K:upsmgBatteryRemainingTime,_L:upsmgBatteryLevel,'upsmgBatteryRechargeTime':upsmgBatteryRechargeTime,'upsmgBatteryRechargeLevel':upsmgBatteryRechargeLevel,'upsmgBatteryVoltage':upsmgBatteryVoltage,'upsmgBatteryCurrent':upsmgBatteryCurrent,'upsmgBatteryTemperature':upsmgBatteryTemperature,'upsmgBatteryFullRechargeTime':upsmgBatteryFullRechargeTime,'upsmgBatteryFaultBattery':upsmgBatteryFaultBattery,'upsmgBatteryNoBattery':upsmgBatteryNoBattery,'upsmgBatteryReplacement':upsmgBatteryReplacement,'upsmgBatteryUnavailableBattery':upsmgBatteryUnavailableBattery,'upsmgBatteryNotHighCharge':upsmgBatteryNotHighCharge,'upsmgBatteryLowBattery':upsmgBatteryLowBattery,'upsmgBatteryChargerFault':upsmgBatteryChargerFault,'upsmgBatteryLowCondition':upsmgBatteryLowCondition,'upsmgBatteryLowRecharge':upsmgBatteryLowRecharge,'upsmgInput':upsmgInput,'upsmgInputPhaseNum':upsmgInputPhaseNum,'upsmgInputPhaseTable':upsmgInputPhaseTable,'upsmgInputPhaseEntry':upsmgInputPhaseEntry,_j:mginputIndex,'mginputVoltage':mginputVoltage,'mginputFrequency':mginputFrequency,'mginputMinimumVoltage':mginputMinimumVoltage,'mginputMaximumVoltage':mginputMaximumVoltage,'mginputCurrent':mginputCurrent,'upsmgInputBadStatus':upsmgInputBadStatus,'upsmgInputLineFailCause':upsmgInputLineFailCause,'upsmgOutput':upsmgOutput,'upsmgOutputPhaseNum':upsmgOutputPhaseNum,'upsmgOutputPhaseTable':upsmgOutputPhaseTable,'upsmgOutputPhaseEntry':upsmgOutputPhaseEntry,_k:mgoutputPhaseIndex,'mgoutputVoltage':mgoutputVoltage,'mgoutputFrequency':mgoutputFrequency,'mgoutputLoadPerPhase':mgoutputLoadPerPhase,'mgoutputCurrent':mgoutputCurrent,'upsmgOutputOnBattery':upsmgOutputOnBattery,'upsmgOutputOnByPass':upsmgOutputOnByPass,'upsmgOutputUnavailableByPass':upsmgOutputUnavailableByPass,'upsmgOutputNoByPass':upsmgOutputNoByPass,'upsmgOutputUtilityOff':upsmgOutputUtilityOff,'upsmgOutputOnBoost':upsmgOutputOnBoost,'upsmgOutputInverterOff':upsmgOutputInverterOff,'upsmgOutputOverLoad':upsmgOutputOverLoad,'upsmgOutputOverTemp':upsmgOutputOverTemp,'upsmgOutputOnBuck':upsmgOutputOnBuck,'upsmgEnviron':upsmgEnviron,'upsmgEnvironAmbientTemp':upsmgEnvironAmbientTemp,'upsmgEnvironAmbientHumidity':upsmgEnvironAmbientHumidity,'upsmgEnvironExtAlarmTable':upsmgEnvironExtAlarmTable,'upsmgEnvironExtAlarmEntry':upsmgEnvironExtAlarmEntry,_l:mgalarmNum,'mgalarmState':mgalarmState,'upsmgEnvironSensorNum':upsmgEnvironSensorNum,'upsmgEnvironSensorTable':upsmgEnvironSensorTable,'upsmgEnvironSensorEntry':upsmgEnvironSensorEntry,_m:mgsensorNum,'mgsensorTemp':mgsensorTemp,'mgsensorHumidity':mgsensorHumidity,'upsmgEnvironmentNum':upsmgEnvironmentNum,'upsmgEnvironmentSensorTable':upsmgEnvironmentSensorTable,'upsmgEnvironmentSensorEntry':upsmgEnvironmentSensorEntry,_n:upsmgEnvironmentIndex,'upsmgEnvironmentComFailure':upsmgEnvironmentComFailure,'upsmgEnvironmentTemperature':upsmgEnvironmentTemperature,'upsmgEnvironmentTemperatureLow':upsmgEnvironmentTemperatureLow,'upsmgEnvironmentTemperatureHigh':upsmgEnvironmentTemperatureHigh,'upsmgEnvironmentHumidity':upsmgEnvironmentHumidity,'upsmgEnvironmentHumidityLow':upsmgEnvironmentHumidityLow,'upsmgEnvironmentHumidityHigh':upsmgEnvironmentHumidityHigh,'upsmgEnvironmentInput1State':upsmgEnvironmentInput1State,'upsmgEnvironmentInput2State':upsmgEnvironmentInput2State,'upsmgControl':upsmgControl,'upsmgControlReceptaclesTable':upsmgControlReceptaclesTable,'upsmgControlReceptaclesEntry':upsmgControlReceptaclesEntry,_p:mgreceptacleIndexc,_Q:mgreceptacleOnDelay,'mgreceptacleOnCtrl':mgreceptacleOnCtrl,'mgreceptacleOnStatus':mgreceptacleOnStatus,_R:mgreceptacleOffDelay,'mgreceptacleOffCtrl':mgreceptacleOffCtrl,'mgreceptacleOffStatus':mgreceptacleOffStatus,_a:mgreceptacleToggleDelay,'mgreceptacleToggleCtrl':mgreceptacleToggleCtrl,'mgreceptacleToggleStatus':mgreceptacleToggleStatus,_b:mgreceptacleToggleDuration,'upsmgControlDayOff':upsmgControlDayOff,'upsmgControlDayOn':upsmgControlDayOn,'upsmgTest':upsmgTest,'upsmgTestBatterySchedule':upsmgTestBatterySchedule,'upsmgTestDiagnostics':upsmgTestDiagnostics,'upsmgTestDiagResult':upsmgTestDiagResult,'upsmgTestBatteryCalibration':upsmgTestBatteryCalibration,'upsmgTestLastCalibration':upsmgTestLastCalibration,'upsmgTestIndicators':upsmgTestIndicators,'upsmgTestCommandLine':upsmgTestCommandLine,'upsmgTestCommandReady':upsmgTestCommandReady,'upsmgTestResponseLine':upsmgTestResponseLine,'upsmgTestResponseReady':upsmgTestResponseReady,'upsmgTestBatteryResult':upsmgTestBatteryResult,'upsmgTraps':upsmgTraps,'upsmgBatteryFault':upsmgBatteryFault,'upsmgBatteryOK':upsmgBatteryOK,'upsmgBatteryReplacementIndicated':upsmgBatteryReplacementIndicated,'upsmgBatteryReplaceNotIndicated':upsmgBatteryReplaceNotIndicated,'upsmgAtLowBattery':upsmgAtLowBattery,'upsmgFromLowBattery':upsmgFromLowBattery,'upsmgChargerFault':upsmgChargerFault,'upsmgChargerOK':upsmgChargerOK,'upsmgAtLowCondition':upsmgAtLowCondition,'upsmgFromLowCondition':upsmgFromLowCondition,'upsmgOnBattery':upsmgOnBattery,'upsmgReturnFromBattery':upsmgReturnFromBattery,'upsmgOnByPass':upsmgOnByPass,'upsmgReturnFromByPass':upsmgReturnFromByPass,'upsmgByPassUnavailable':upsmgByPassUnavailable,'upsmgByPassAvailable':upsmgByPassAvailable,'upsmgUtilityFailure':upsmgUtilityFailure,'upsmgUtilityRestored':upsmgUtilityRestored,'upsmgOnBoost':upsmgOnBoost,'upsmgReturnFromBoost':upsmgReturnFromBoost,'upsmgOverLoad':upsmgOverLoad,'upsmgLoadOK':upsmgLoadOK,'upsmgOverTemperature':upsmgOverTemperature,'upsmgTemperatureOK':upsmgTemperatureOK,'upsmgOnToStart':upsmgOnToStart,'upsmgOnAbort':upsmgOnAbort,'upsmgOnInProgress':upsmgOnInProgress,'upsmgOnComplete':upsmgOnComplete,'upsmgOffToStart':upsmgOffToStart,'upsmgOffAbort':upsmgOffAbort,'upsmgOffInProgress':upsmgOffInProgress,'upsmgOffComplete':upsmgOffComplete,'upsmgToggleToStart':upsmgToggleToStart,'upsmgToggleAbort':upsmgToggleAbort,'upsmgToggleInProgress':upsmgToggleInProgress,'upsmgToggleComplete':upsmgToggleComplete,'upsmgCommunicationFailure':upsmgCommunicationFailure,'upsmgCommunicationRestored':upsmgCommunicationRestored,'upsmgInputBad':upsmgInputBad,'upsmgInputOK':upsmgInputOK,'upsmgBatteryUnavailable':upsmgBatteryUnavailable,'upsmgBatteryAvailable':upsmgBatteryAvailable,'upsmgAtLowRecharge':upsmgAtLowRecharge,'upsmgFromLowRecharge':upsmgFromLowRecharge,'upsmgDiagnosticTestFail':upsmgDiagnosticTestFail,'upsmgDiagnosticTestOK':upsmgDiagnosticTestOK,'upsmgBatteryTestOK':upsmgBatteryTestOK,'upsmgBatteryTestFail':upsmgBatteryTestFail,'upsmgExternalAlarmActive':upsmgExternalAlarmActive,'upsmgExternalAlarmInactive':upsmgExternalAlarmInactive,'upsmgOnBuck':upsmgOnBuck,'upsmgReturnFromBuck':upsmgReturnFromBuck,'upsmgEnvironComFailure':upsmgEnvironComFailure,'upsmgEnvironComOK':upsmgEnvironComOK,'upsmgEnvironTemperatureLow':upsmgEnvironTemperatureLow,'upsmgEnvironTemperatureHigh':upsmgEnvironTemperatureHigh,'upsmgEnvironTemperatureOK':upsmgEnvironTemperatureOK,'upsmgEnvironHumidityLow':upsmgEnvironHumidityLow,'upsmgEnvironHumidityHigh':upsmgEnvironHumidityHigh,'upsmgEnvironHumidityOK':upsmgEnvironHumidityOK,'upsmgEnvironInput1Closed':upsmgEnvironInput1Closed,'upsmgEnvironInput1Open':upsmgEnvironInput1Open,'upsmgEnvironInput2Closed':upsmgEnvironInput2Closed,'upsmgEnvironInput2Open':upsmgEnvironInput2Open,'upsRedundancyLost':upsRedundancyLost,'upsRedundancyOK':upsRedundancyOK,'upsProtectionLost':upsProtectionLost,'upsProtectionOK':upsProtectionOK,'upsmgAgent':upsmgAgent,'upsmgAgentIpaddress':upsmgAgentIpaddress,'upsmgAgentSubnetMask':upsmgAgentSubnetMask,'upsmgAgentDefGateway':upsmgAgentDefGateway,'upsmgAgentBaudRate':upsmgAgentBaudRate,'upsmgAgentPollRate':upsmgAgentPollRate,'upsmgAgentType':upsmgAgentType,'upsmgAgentTrapAlarmDelay':upsmgAgentTrapAlarmDelay,'upsmgAgentTrapAlarmRetry':upsmgAgentTrapAlarmRetry,'upsmgAgentReset':upsmgAgentReset,'upsmgAgentFactReset':upsmgAgentFactReset,'upsmgAgentMibVersion':upsmgAgentMibVersion,'upsmgAgentFirmwareVersion':upsmgAgentFirmwareVersion,'upsmgAgentCommUPS':upsmgAgentCommUPS,'upsmgAgentTrapAck':upsmgAgentTrapAck,'upsmgAgentAutoLearning':upsmgAgentAutoLearning,'upsmgAgentBootP':upsmgAgentBootP,'upsmgAgentTFTP':upsmgAgentTFTP,'upsmgAgentTrapSignature':upsmgAgentTrapSignature,'upsmgRemote':upsmgRemote,'upsmgRemoteOnBattery':upsmgRemoteOnBattery,'upsmgRemoteIpAddress':upsmgRemoteIpAddress})