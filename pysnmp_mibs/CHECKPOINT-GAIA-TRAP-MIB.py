_c='chkpntGaiaNotificationGroup'
_b='chkpntGaiaTrapGroup'
_a='chkpntRAIDVolumeStateTrap'
_Z='chkpntBiosTrap'
_Y='chkpntSystemConfigurationSaveTrap'
_X='chkpntSystemConfigurationChangeTrap'
_W='chkpntPowerSupplyTrap'
_V='chkpntVoltageTrap'
_U='chkpntFanSpeedTrap'
_T='chkpntTempertureTrap'
_S='chkpntGaiaTrapBladeId'
_R='chkpntGaiaTrapChassisId'
_Q='Integer32'
_P='voltageSensorValue'
_O='voltageSensorName'
_N='tempertureSensorValue'
_M='tempertureSensorName'
_L='raidVolumeState'
_K='raidVolumeFlags'
_J='powerSupplyStatus'
_I='powerSupplyIndex'
_H='fanSpeedSensorValue'
_G='fanSpeedSensorName'
_F='chkpntGaiaTrapOID'
_E='chkpntGaiaTrapMsgText'
_D='read-only'
_C='CHECKPOINT-MIB'
_B='current'
_A='CHECKPOINT-GAIA-TRAP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fanSpeedSensorName,fanSpeedSensorValue,powerSupplyIndex,powerSupplyStatus,raidVolumeFlags,raidVolumeState,tempertureSensorName,tempertureSensorValue,voltageSensorName,voltageSensorValue=mibBuilder.importSymbols(_C,_G,_H,_I,_J,_K,_L,_M,_N,_O,_P)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_Q,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
chkpntGaiaTrapMibModule=ModuleIdentity((1,3,6,1,4,1,2620,1,3000,0,0))
if mibBuilder.loadTexts:chkpntGaiaTrapMibModule.setRevisions(('2010-05-10 14:31',))
_Checkpoint_ObjectIdentity=ObjectIdentity
checkpoint=_Checkpoint_ObjectIdentity((1,3,6,1,4,1,2620))
_Products_ObjectIdentity=ObjectIdentity
products=_Products_ObjectIdentity((1,3,6,1,4,1,2620,1))
_Svn_ObjectIdentity=ObjectIdentity
svn=_Svn_ObjectIdentity((1,3,6,1,4,1,2620,1,6))
_SvnPerf_ObjectIdentity=ObjectIdentity
svnPerf=_SvnPerf_ObjectIdentity((1,3,6,1,4,1,2620,1,6,7))
_RaidInfo_ObjectIdentity=ObjectIdentity
raidInfo=_RaidInfo_ObjectIdentity((1,3,6,1,4,1,2620,1,6,7,6))
_RaidVolumeTable_ObjectIdentity=ObjectIdentity
raidVolumeTable=_RaidVolumeTable_ObjectIdentity((1,3,6,1,4,1,2620,1,6,7,6,1))
_RaidVolumeEntry_ObjectIdentity=ObjectIdentity
raidVolumeEntry=_RaidVolumeEntry_ObjectIdentity((1,3,6,1,4,1,2620,1,6,7,6,1,1))
_RaidVolumeState_Type=DisplayString
_RaidVolumeState_Object=MibScalar
raidVolumeState=_RaidVolumeState_Object((1,3,6,1,4,1,2620,1,6,7,6,1,1,6),_RaidVolumeState_Type())
raidVolumeState.setMaxAccess(_D)
if mibBuilder.loadTexts:raidVolumeState.setStatus(_B)
_RaidVolumeFlags_Type=DisplayString
_RaidVolumeFlags_Object=MibScalar
raidVolumeFlags=_RaidVolumeFlags_Object((1,3,6,1,4,1,2620,1,6,7,6,1,1,7),_RaidVolumeFlags_Type())
raidVolumeFlags.setMaxAccess(_D)
if mibBuilder.loadTexts:raidVolumeFlags.setStatus(_B)
_SensorInfo_ObjectIdentity=ObjectIdentity
sensorInfo=_SensorInfo_ObjectIdentity((1,3,6,1,4,1,2620,1,6,7,8))
_TempertureSensorTable_ObjectIdentity=ObjectIdentity
tempertureSensorTable=_TempertureSensorTable_ObjectIdentity((1,3,6,1,4,1,2620,1,6,7,8,1))
_TempertureSensorEntry_ObjectIdentity=ObjectIdentity
tempertureSensorEntry=_TempertureSensorEntry_ObjectIdentity((1,3,6,1,4,1,2620,1,6,7,8,1,1))
_TempertureSensorName_Type=DisplayString
_TempertureSensorName_Object=MibScalar
tempertureSensorName=_TempertureSensorName_Object((1,3,6,1,4,1,2620,1,6,7,8,1,1,2),_TempertureSensorName_Type())
tempertureSensorName.setMaxAccess(_D)
if mibBuilder.loadTexts:tempertureSensorName.setStatus(_B)
_TempertureSensorValue_Type=DisplayString
_TempertureSensorValue_Object=MibScalar
tempertureSensorValue=_TempertureSensorValue_Object((1,3,6,1,4,1,2620,1,6,7,8,1,1,3),_TempertureSensorValue_Type())
tempertureSensorValue.setMaxAccess(_D)
if mibBuilder.loadTexts:tempertureSensorValue.setStatus(_B)
_FanSpeedSensorTable_ObjectIdentity=ObjectIdentity
fanSpeedSensorTable=_FanSpeedSensorTable_ObjectIdentity((1,3,6,1,4,1,2620,1,6,7,8,2))
_FanSpeedSensorEntry_ObjectIdentity=ObjectIdentity
fanSpeedSensorEntry=_FanSpeedSensorEntry_ObjectIdentity((1,3,6,1,4,1,2620,1,6,7,8,2,1))
_FanSpeedSensorName_Type=DisplayString
_FanSpeedSensorName_Object=MibScalar
fanSpeedSensorName=_FanSpeedSensorName_Object((1,3,6,1,4,1,2620,1,6,7,8,2,1,2),_FanSpeedSensorName_Type())
fanSpeedSensorName.setMaxAccess(_D)
if mibBuilder.loadTexts:fanSpeedSensorName.setStatus(_B)
_FanSpeedSensorValue_Type=DisplayString
_FanSpeedSensorValue_Object=MibScalar
fanSpeedSensorValue=_FanSpeedSensorValue_Object((1,3,6,1,4,1,2620,1,6,7,8,2,1,3),_FanSpeedSensorValue_Type())
fanSpeedSensorValue.setMaxAccess(_D)
if mibBuilder.loadTexts:fanSpeedSensorValue.setStatus(_B)
_VoltageSensorTable_ObjectIdentity=ObjectIdentity
voltageSensorTable=_VoltageSensorTable_ObjectIdentity((1,3,6,1,4,1,2620,1,6,7,8,3))
_VoltageSensorEntry_ObjectIdentity=ObjectIdentity
voltageSensorEntry=_VoltageSensorEntry_ObjectIdentity((1,3,6,1,4,1,2620,1,6,7,8,3,1))
_VoltageSensorName_Type=DisplayString
_VoltageSensorName_Object=MibScalar
voltageSensorName=_VoltageSensorName_Object((1,3,6,1,4,1,2620,1,6,7,8,3,1,2),_VoltageSensorName_Type())
voltageSensorName.setMaxAccess(_D)
if mibBuilder.loadTexts:voltageSensorName.setStatus(_B)
_VoltageSensorValue_Type=DisplayString
_VoltageSensorValue_Object=MibScalar
voltageSensorValue=_VoltageSensorValue_Object((1,3,6,1,4,1,2620,1,6,7,8,3,1,3),_VoltageSensorValue_Type())
voltageSensorValue.setMaxAccess(_D)
if mibBuilder.loadTexts:voltageSensorValue.setStatus(_B)
_PowerSupplyInfo_ObjectIdentity=ObjectIdentity
powerSupplyInfo=_PowerSupplyInfo_ObjectIdentity((1,3,6,1,4,1,2620,1,6,7,9))
_PowerSupplyTable_ObjectIdentity=ObjectIdentity
powerSupplyTable=_PowerSupplyTable_ObjectIdentity((1,3,6,1,4,1,2620,1,6,7,9,1))
_PowerSupplyEntry_ObjectIdentity=ObjectIdentity
powerSupplyEntry=_PowerSupplyEntry_ObjectIdentity((1,3,6,1,4,1,2620,1,6,7,9,1,1))
_PowerSupplyIndex_Type=DisplayString
_PowerSupplyIndex_Object=MibScalar
powerSupplyIndex=_PowerSupplyIndex_Object((1,3,6,1,4,1,2620,1,6,7,9,1,1,2),_PowerSupplyIndex_Type())
powerSupplyIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:powerSupplyIndex.setStatus(_B)
_PowerSupplyStatus_Type=DisplayString
_PowerSupplyStatus_Object=MibScalar
powerSupplyStatus=_PowerSupplyStatus_Object((1,3,6,1,4,1,2620,1,6,7,9,1,1,3),_PowerSupplyStatus_Type())
powerSupplyStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:powerSupplyStatus.setStatus(_B)
_ChkpntGaiaTrap_ObjectIdentity=ObjectIdentity
chkpntGaiaTrap=_ChkpntGaiaTrap_ObjectIdentity((1,3,6,1,4,1,2620,1,3000))
_ChkpntGaiaTrapInfo_ObjectIdentity=ObjectIdentity
chkpntGaiaTrapInfo=_ChkpntGaiaTrapInfo_ObjectIdentity((1,3,6,1,4,1,2620,1,3000,0))
_ChkpntGaiaTrapOID_Type=DisplayString
_ChkpntGaiaTrapOID_Object=MibScalar
chkpntGaiaTrapOID=_ChkpntGaiaTrapOID_Object((1,3,6,1,4,1,2620,1,3000,0,10),_ChkpntGaiaTrapOID_Type())
chkpntGaiaTrapOID.setMaxAccess(_D)
if mibBuilder.loadTexts:chkpntGaiaTrapOID.setStatus(_B)
_ChkpntGaiaTrapMsgText_Type=DisplayString
_ChkpntGaiaTrapMsgText_Object=MibScalar
chkpntGaiaTrapMsgText=_ChkpntGaiaTrapMsgText_Object((1,3,6,1,4,1,2620,1,3000,0,12),_ChkpntGaiaTrapMsgText_Type())
chkpntGaiaTrapMsgText.setMaxAccess(_D)
if mibBuilder.loadTexts:chkpntGaiaTrapMsgText.setStatus(_B)
class _ChkpntGaiaTrapChassisId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ChkpntGaiaTrapChassisId_Type.__name__=_Q
_ChkpntGaiaTrapChassisId_Object=MibScalar
chkpntGaiaTrapChassisId=_ChkpntGaiaTrapChassisId_Object((1,3,6,1,4,1,2620,1,3000,0,15),_ChkpntGaiaTrapChassisId_Type())
chkpntGaiaTrapChassisId.setMaxAccess(_D)
if mibBuilder.loadTexts:chkpntGaiaTrapChassisId.setStatus(_B)
class _ChkpntGaiaTrapBladeId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ChkpntGaiaTrapBladeId_Type.__name__=_Q
_ChkpntGaiaTrapBladeId_Object=MibScalar
chkpntGaiaTrapBladeId=_ChkpntGaiaTrapBladeId_Object((1,3,6,1,4,1,2620,1,3000,0,16),_ChkpntGaiaTrapBladeId_Type())
chkpntGaiaTrapBladeId.setMaxAccess(_D)
if mibBuilder.loadTexts:chkpntGaiaTrapBladeId.setStatus(_B)
_ChkpntGaiaTrapDisk_ObjectIdentity=ObjectIdentity
chkpntGaiaTrapDisk=_ChkpntGaiaTrapDisk_ObjectIdentity((1,3,6,1,4,1,2620,1,3000,2))
_ChkpntGaiaTrapRAID_ObjectIdentity=ObjectIdentity
chkpntGaiaTrapRAID=_ChkpntGaiaTrapRAID_ObjectIdentity((1,3,6,1,4,1,2620,1,3000,2,1))
_ChkpntGaiaTrapHWSensor_ObjectIdentity=ObjectIdentity
chkpntGaiaTrapHWSensor=_ChkpntGaiaTrapHWSensor_ObjectIdentity((1,3,6,1,4,1,2620,1,3000,5))
_ChkpntGaiaTrapTempertureSensor_ObjectIdentity=ObjectIdentity
chkpntGaiaTrapTempertureSensor=_ChkpntGaiaTrapTempertureSensor_ObjectIdentity((1,3,6,1,4,1,2620,1,3000,5,1))
_ChkpntGaiaTrapFanSpeedSensor_ObjectIdentity=ObjectIdentity
chkpntGaiaTrapFanSpeedSensor=_ChkpntGaiaTrapFanSpeedSensor_ObjectIdentity((1,3,6,1,4,1,2620,1,3000,5,2))
_ChkpntGaiaTrapVoltageSensor_ObjectIdentity=ObjectIdentity
chkpntGaiaTrapVoltageSensor=_ChkpntGaiaTrapVoltageSensor_ObjectIdentity((1,3,6,1,4,1,2620,1,3000,5,3))
_ChkpntGaiaTrapPowerSupplySensor_ObjectIdentity=ObjectIdentity
chkpntGaiaTrapPowerSupplySensor=_ChkpntGaiaTrapPowerSupplySensor_ObjectIdentity((1,3,6,1,4,1,2620,1,3000,5,4))
_ChkpntGaiaTrapConfiguration_ObjectIdentity=ObjectIdentity
chkpntGaiaTrapConfiguration=_ChkpntGaiaTrapConfiguration_ObjectIdentity((1,3,6,1,4,1,2620,1,3000,10))
_ChkpntGaiaTrapSystemConfiguration_ObjectIdentity=ObjectIdentity
chkpntGaiaTrapSystemConfiguration=_ChkpntGaiaTrapSystemConfiguration_ObjectIdentity((1,3,6,1,4,1,2620,1,3000,10,1))
_ChkpntBios_ObjectIdentity=ObjectIdentity
chkpntBios=_ChkpntBios_ObjectIdentity((1,3,6,1,4,1,2620,1,3000,20))
_ChkpntGaiaTrapMIBConformance_ObjectIdentity=ObjectIdentity
chkpntGaiaTrapMIBConformance=_ChkpntGaiaTrapMIBConformance_ObjectIdentity((1,3,6,1,4,1,2620,2))
_ChkpntGaiaTrapMIBCompliances_ObjectIdentity=ObjectIdentity
chkpntGaiaTrapMIBCompliances=_ChkpntGaiaTrapMIBCompliances_ObjectIdentity((1,3,6,1,4,1,2620,2,1))
_ChkpntGaiaTrapMIBGroups_ObjectIdentity=ObjectIdentity
chkpntGaiaTrapMIBGroups=_ChkpntGaiaTrapMIBGroups_ObjectIdentity((1,3,6,1,4,1,2620,2,2))
_ChkpntGaiaNotificationGroups_ObjectIdentity=ObjectIdentity
chkpntGaiaNotificationGroups=_ChkpntGaiaNotificationGroups_ObjectIdentity((1,3,6,1,4,1,2620,2,3))
chkpntGaiaTrapGroup=ObjectGroup((1,3,6,1,4,1,2620,2,2,1))
chkpntGaiaTrapGroup.setObjects(*((_A,_F),(_A,_E),(_A,_R),(_A,_S),(_C,_M),(_C,_N),(_C,_G),(_C,_H),(_C,_O),(_C,_P),(_C,_I),(_C,_J),(_C,_L),(_C,_K)))
if mibBuilder.loadTexts:chkpntGaiaTrapGroup.setStatus(_B)
chkpntRAIDVolumeStateTrap=NotificationType((1,3,6,1,4,1,2620,1,3000,2,1,1))
chkpntRAIDVolumeStateTrap.setObjects(*((_A,_F),(_A,_E),(_C,_L),(_C,_K)))
if mibBuilder.loadTexts:chkpntRAIDVolumeStateTrap.setStatus(_B)
chkpntTempertureTrap=NotificationType((1,3,6,1,4,1,2620,1,3000,5,1,1))
chkpntTempertureTrap.setObjects(*((_A,_F),(_A,_E),(_C,_M),(_C,_N)))
if mibBuilder.loadTexts:chkpntTempertureTrap.setStatus(_B)
chkpntFanSpeedTrap=NotificationType((1,3,6,1,4,1,2620,1,3000,5,2,1))
chkpntFanSpeedTrap.setObjects(*((_A,_F),(_A,_E),(_C,_G),(_C,_H)))
if mibBuilder.loadTexts:chkpntFanSpeedTrap.setStatus(_B)
chkpntVoltageTrap=NotificationType((1,3,6,1,4,1,2620,1,3000,5,3,1))
chkpntVoltageTrap.setObjects(*((_A,_F),(_A,_E),(_C,_O),(_C,_P)))
if mibBuilder.loadTexts:chkpntVoltageTrap.setStatus(_B)
chkpntPowerSupplyTrap=NotificationType((1,3,6,1,4,1,2620,1,3000,5,4,1))
chkpntPowerSupplyTrap.setObjects(*((_A,_F),(_A,_E),(_C,_I),(_C,_J)))
if mibBuilder.loadTexts:chkpntPowerSupplyTrap.setStatus(_B)
chkpntSystemConfigurationChangeTrap=NotificationType((1,3,6,1,4,1,2620,1,3000,10,1,1))
chkpntSystemConfigurationChangeTrap.setObjects(*((_A,_F),(_A,_E)))
if mibBuilder.loadTexts:chkpntSystemConfigurationChangeTrap.setStatus(_B)
chkpntSystemConfigurationSaveTrap=NotificationType((1,3,6,1,4,1,2620,1,3000,10,1,2))
chkpntSystemConfigurationSaveTrap.setObjects(*((_A,_F),(_A,_E)))
if mibBuilder.loadTexts:chkpntSystemConfigurationSaveTrap.setStatus(_B)
chkpntBiosTrap=NotificationType((1,3,6,1,4,1,2620,1,3000,20,1))
chkpntBiosTrap.setObjects((_A,_E))
if mibBuilder.loadTexts:chkpntBiosTrap.setStatus(_B)
chkpntGaiaNotificationGroup=NotificationGroup((1,3,6,1,4,1,2620,2,3,1))
chkpntGaiaNotificationGroup.setObjects(*((_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:chkpntGaiaNotificationGroup.setStatus(_B)
chkpntGaiaTrapBasicCompliance=ModuleCompliance((1,3,6,1,4,1,2620,2,1,1))
chkpntGaiaTrapBasicCompliance.setObjects(*((_A,_b),(_A,_c)))
if mibBuilder.loadTexts:chkpntGaiaTrapBasicCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'checkpoint':checkpoint,'products':products,'svn':svn,'svnPerf':svnPerf,'raidInfo':raidInfo,'raidVolumeTable':raidVolumeTable,'raidVolumeEntry':raidVolumeEntry,_L:raidVolumeState,_K:raidVolumeFlags,'sensorInfo':sensorInfo,'tempertureSensorTable':tempertureSensorTable,'tempertureSensorEntry':tempertureSensorEntry,_M:tempertureSensorName,_N:tempertureSensorValue,'fanSpeedSensorTable':fanSpeedSensorTable,'fanSpeedSensorEntry':fanSpeedSensorEntry,_G:fanSpeedSensorName,_H:fanSpeedSensorValue,'voltageSensorTable':voltageSensorTable,'voltageSensorEntry':voltageSensorEntry,_O:voltageSensorName,_P:voltageSensorValue,'powerSupplyInfo':powerSupplyInfo,'powerSupplyTable':powerSupplyTable,'powerSupplyEntry':powerSupplyEntry,_I:powerSupplyIndex,_J:powerSupplyStatus,'chkpntGaiaTrap':chkpntGaiaTrap,'chkpntGaiaTrapInfo':chkpntGaiaTrapInfo,'chkpntGaiaTrapMibModule':chkpntGaiaTrapMibModule,_F:chkpntGaiaTrapOID,_E:chkpntGaiaTrapMsgText,_R:chkpntGaiaTrapChassisId,_S:chkpntGaiaTrapBladeId,'chkpntGaiaTrapDisk':chkpntGaiaTrapDisk,'chkpntGaiaTrapRAID':chkpntGaiaTrapRAID,_a:chkpntRAIDVolumeStateTrap,'chkpntGaiaTrapHWSensor':chkpntGaiaTrapHWSensor,'chkpntGaiaTrapTempertureSensor':chkpntGaiaTrapTempertureSensor,_T:chkpntTempertureTrap,'chkpntGaiaTrapFanSpeedSensor':chkpntGaiaTrapFanSpeedSensor,_U:chkpntFanSpeedTrap,'chkpntGaiaTrapVoltageSensor':chkpntGaiaTrapVoltageSensor,_V:chkpntVoltageTrap,'chkpntGaiaTrapPowerSupplySensor':chkpntGaiaTrapPowerSupplySensor,_W:chkpntPowerSupplyTrap,'chkpntGaiaTrapConfiguration':chkpntGaiaTrapConfiguration,'chkpntGaiaTrapSystemConfiguration':chkpntGaiaTrapSystemConfiguration,_X:chkpntSystemConfigurationChangeTrap,_Y:chkpntSystemConfigurationSaveTrap,'chkpntBios':chkpntBios,_Z:chkpntBiosTrap,'chkpntGaiaTrapMIBConformance':chkpntGaiaTrapMIBConformance,'chkpntGaiaTrapMIBCompliances':chkpntGaiaTrapMIBCompliances,'chkpntGaiaTrapBasicCompliance':chkpntGaiaTrapBasicCompliance,'chkpntGaiaTrapMIBGroups':chkpntGaiaTrapMIBGroups,_b:chkpntGaiaTrapGroup,'chkpntGaiaNotificationGroups':chkpntGaiaNotificationGroups,_c:chkpntGaiaNotificationGroup})