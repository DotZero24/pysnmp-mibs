_u='rbnEnvMonEntityObjectGroup'
_t='rbnPowerStatusChange'
_s='rbnFanStatusChange'
_r='rbnPowerFailChange'
_q='rbnFanFailChange'
_p='rbnEntityTempCurrent'
_o='rbnEntityTempDescr'
_n='rbnFanSpeedCurrent'
_m='rbnFanUnitDescr'
_l='rbnCpuTempCurrent'
_k='rbnCpuTempDescr'
_j='rbnVoltageCurrent'
_i='rbnVoltageDesired'
_h='rbnVoltageDescr'
_g='rbnEntityTempIndex'
_f='rbnFanUnitID'
_e='rbnCpuTempIndex'
_d='millivolts'
_c='rbnVoltageIndex'
_b='rbnPowerIndex'
_a='unknown'
_Z='absent'
_Y='failed'
_X='normal'
_W='rbnEnvMonFanSpeedObjectGroup'
_V='rbnEnvMonMIBNotificationGroup'
_U='rbnEnvMonMIBObjectGroup'
_T='rbnPowerStatus'
_S='rbnFanStatus'
_R='rbnPowerFail'
_Q='rbnPowerDescr'
_P='rbnFanFail'
_O='rbnFanDescr'
_N='rbnFanIndex'
_M='rbnEnvMonMIBNotificationGroupV2'
_L='rbnEnvMonMIBObjectGroupV2'
_K='rbnEnvMonTempObjectGroup'
_J='entPhysicalIndex'
_I='ENTITY-MIB'
_H='rbnEnvMonVoltageObjectGroup'
_G='not-accessible'
_F='DisplayString'
_E='Integer32'
_D='deprecated'
_C='read-only'
_B='current'
_A='RBN-ENVMON-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalIndex,=mibBuilder.importSymbols(_I,_J)
rbnMgmt,=mibBuilder.importSymbols('RBN-SMI','rbnMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention','TruthValue')
rbnEnvMonMIB=ModuleIdentity((1,3,6,1,4,1,2352,2,4))
if mibBuilder.loadTexts:rbnEnvMonMIB.setRevisions(('2012-10-03 00:00','2011-01-19 18:00','2010-11-11 00:00','2006-01-16 00:00','2002-06-05 00:00','2001-07-25 00:00','2000-04-24 00:00','1999-03-10 00:00'))
class RbnVoltage(TextualConvention,Unsigned32):status=_B;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,50000))
class RbnTemperature(TextualConvention,Unsigned32):status=_B;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
class RbnFanSpeed(TextualConvention,Unsigned32):status=_B
_RbnEnvMonMIBNotifications_ObjectIdentity=ObjectIdentity
rbnEnvMonMIBNotifications=_RbnEnvMonMIBNotifications_ObjectIdentity((1,3,6,1,4,1,2352,2,4,0))
_RbnEnvMonMIBObjects_ObjectIdentity=ObjectIdentity
rbnEnvMonMIBObjects=_RbnEnvMonMIBObjects_ObjectIdentity((1,3,6,1,4,1,2352,2,4,1))
_RbnFanStatusTable_Object=MibTable
rbnFanStatusTable=_RbnFanStatusTable_Object((1,3,6,1,4,1,2352,2,4,1,1))
if mibBuilder.loadTexts:rbnFanStatusTable.setStatus(_B)
_RbnFanStatusEntry_Object=MibTableRow
rbnFanStatusEntry=_RbnFanStatusEntry_Object((1,3,6,1,4,1,2352,2,4,1,1,1))
rbnFanStatusEntry.setIndexNames((0,_A,_N))
if mibBuilder.loadTexts:rbnFanStatusEntry.setStatus(_B)
class _RbnFanIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RbnFanIndex_Type.__name__=_E
_RbnFanIndex_Object=MibTableColumn
rbnFanIndex=_RbnFanIndex_Object((1,3,6,1,4,1,2352,2,4,1,1,1,1),_RbnFanIndex_Type())
rbnFanIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:rbnFanIndex.setStatus(_B)
class _RbnFanDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RbnFanDescr_Type.__name__=_F
_RbnFanDescr_Object=MibTableColumn
rbnFanDescr=_RbnFanDescr_Object((1,3,6,1,4,1,2352,2,4,1,1,1,2),_RbnFanDescr_Type())
rbnFanDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnFanDescr.setStatus(_B)
_RbnFanFail_Type=TruthValue
_RbnFanFail_Object=MibTableColumn
rbnFanFail=_RbnFanFail_Object((1,3,6,1,4,1,2352,2,4,1,1,1,3),_RbnFanFail_Type())
rbnFanFail.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnFanFail.setStatus(_D)
class _RbnFanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_X,1),(_Y,2),(_Z,3),(_a,4)))
_RbnFanStatus_Type.__name__=_E
_RbnFanStatus_Object=MibTableColumn
rbnFanStatus=_RbnFanStatus_Object((1,3,6,1,4,1,2352,2,4,1,1,1,4),_RbnFanStatus_Type())
rbnFanStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnFanStatus.setStatus(_B)
_RbnPowerStatusTable_Object=MibTable
rbnPowerStatusTable=_RbnPowerStatusTable_Object((1,3,6,1,4,1,2352,2,4,1,2))
if mibBuilder.loadTexts:rbnPowerStatusTable.setStatus(_B)
_RbnPowerStatusEntry_Object=MibTableRow
rbnPowerStatusEntry=_RbnPowerStatusEntry_Object((1,3,6,1,4,1,2352,2,4,1,2,1))
rbnPowerStatusEntry.setIndexNames((0,_A,_b))
if mibBuilder.loadTexts:rbnPowerStatusEntry.setStatus(_B)
class _RbnPowerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RbnPowerIndex_Type.__name__=_E
_RbnPowerIndex_Object=MibTableColumn
rbnPowerIndex=_RbnPowerIndex_Object((1,3,6,1,4,1,2352,2,4,1,2,1,1),_RbnPowerIndex_Type())
rbnPowerIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:rbnPowerIndex.setStatus(_B)
class _RbnPowerDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RbnPowerDescr_Type.__name__=_F
_RbnPowerDescr_Object=MibTableColumn
rbnPowerDescr=_RbnPowerDescr_Object((1,3,6,1,4,1,2352,2,4,1,2,1,2),_RbnPowerDescr_Type())
rbnPowerDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnPowerDescr.setStatus(_B)
_RbnPowerFail_Type=TruthValue
_RbnPowerFail_Object=MibTableColumn
rbnPowerFail=_RbnPowerFail_Object((1,3,6,1,4,1,2352,2,4,1,2,1,3),_RbnPowerFail_Type())
rbnPowerFail.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnPowerFail.setStatus(_D)
class _RbnPowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_X,1),(_Y,2),(_Z,3),(_a,4)))
_RbnPowerStatus_Type.__name__=_E
_RbnPowerStatus_Object=MibTableColumn
rbnPowerStatus=_RbnPowerStatus_Object((1,3,6,1,4,1,2352,2,4,1,2,1,4),_RbnPowerStatus_Type())
rbnPowerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnPowerStatus.setStatus(_B)
_RbnVoltageSensorTable_Object=MibTable
rbnVoltageSensorTable=_RbnVoltageSensorTable_Object((1,3,6,1,4,1,2352,2,4,1,3))
if mibBuilder.loadTexts:rbnVoltageSensorTable.setStatus(_B)
_RbnVoltageSensorEntry_Object=MibTableRow
rbnVoltageSensorEntry=_RbnVoltageSensorEntry_Object((1,3,6,1,4,1,2352,2,4,1,3,1))
rbnVoltageSensorEntry.setIndexNames((0,_I,_J),(0,_A,_c))
if mibBuilder.loadTexts:rbnVoltageSensorEntry.setStatus(_B)
class _RbnVoltageIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RbnVoltageIndex_Type.__name__=_E
_RbnVoltageIndex_Object=MibTableColumn
rbnVoltageIndex=_RbnVoltageIndex_Object((1,3,6,1,4,1,2352,2,4,1,3,1,1),_RbnVoltageIndex_Type())
rbnVoltageIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:rbnVoltageIndex.setStatus(_B)
class _RbnVoltageDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,48))
_RbnVoltageDescr_Type.__name__=_F
_RbnVoltageDescr_Object=MibTableColumn
rbnVoltageDescr=_RbnVoltageDescr_Object((1,3,6,1,4,1,2352,2,4,1,3,1,2),_RbnVoltageDescr_Type())
rbnVoltageDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnVoltageDescr.setStatus(_B)
_RbnVoltageDesired_Type=RbnVoltage
_RbnVoltageDesired_Object=MibTableColumn
rbnVoltageDesired=_RbnVoltageDesired_Object((1,3,6,1,4,1,2352,2,4,1,3,1,3),_RbnVoltageDesired_Type())
rbnVoltageDesired.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnVoltageDesired.setStatus(_B)
if mibBuilder.loadTexts:rbnVoltageDesired.setUnits(_d)
_RbnVoltageCurrent_Type=RbnVoltage
_RbnVoltageCurrent_Object=MibTableColumn
rbnVoltageCurrent=_RbnVoltageCurrent_Object((1,3,6,1,4,1,2352,2,4,1,3,1,4),_RbnVoltageCurrent_Type())
rbnVoltageCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnVoltageCurrent.setStatus(_B)
if mibBuilder.loadTexts:rbnVoltageCurrent.setUnits(_d)
_RbnCpuTempSensorTable_Object=MibTable
rbnCpuTempSensorTable=_RbnCpuTempSensorTable_Object((1,3,6,1,4,1,2352,2,4,1,4))
if mibBuilder.loadTexts:rbnCpuTempSensorTable.setStatus(_D)
_RbnCpuTempSensorEntry_Object=MibTableRow
rbnCpuTempSensorEntry=_RbnCpuTempSensorEntry_Object((1,3,6,1,4,1,2352,2,4,1,4,1))
rbnCpuTempSensorEntry.setIndexNames((0,_I,_J),(0,_A,_e))
if mibBuilder.loadTexts:rbnCpuTempSensorEntry.setStatus(_D)
class _RbnCpuTempIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RbnCpuTempIndex_Type.__name__=_E
_RbnCpuTempIndex_Object=MibTableColumn
rbnCpuTempIndex=_RbnCpuTempIndex_Object((1,3,6,1,4,1,2352,2,4,1,4,1,1),_RbnCpuTempIndex_Type())
rbnCpuTempIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:rbnCpuTempIndex.setStatus(_D)
class _RbnCpuTempDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,48))
_RbnCpuTempDescr_Type.__name__=_F
_RbnCpuTempDescr_Object=MibTableColumn
rbnCpuTempDescr=_RbnCpuTempDescr_Object((1,3,6,1,4,1,2352,2,4,1,4,1,2),_RbnCpuTempDescr_Type())
rbnCpuTempDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnCpuTempDescr.setStatus(_D)
_RbnCpuTempCurrent_Type=RbnTemperature
_RbnCpuTempCurrent_Object=MibTableColumn
rbnCpuTempCurrent=_RbnCpuTempCurrent_Object((1,3,6,1,4,1,2352,2,4,1,4,1,3),_RbnCpuTempCurrent_Type())
rbnCpuTempCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnCpuTempCurrent.setStatus(_D)
if mibBuilder.loadTexts:rbnCpuTempCurrent.setUnits('degrees')
_RbnFanSpeedTable_Object=MibTable
rbnFanSpeedTable=_RbnFanSpeedTable_Object((1,3,6,1,4,1,2352,2,4,1,5))
if mibBuilder.loadTexts:rbnFanSpeedTable.setStatus(_B)
_RbnFanSpeedEntry_Object=MibTableRow
rbnFanSpeedEntry=_RbnFanSpeedEntry_Object((1,3,6,1,4,1,2352,2,4,1,5,1))
rbnFanSpeedEntry.setIndexNames((0,_A,_N),(0,_A,_f))
if mibBuilder.loadTexts:rbnFanSpeedEntry.setStatus(_B)
class _RbnFanUnitID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RbnFanUnitID_Type.__name__=_E
_RbnFanUnitID_Object=MibTableColumn
rbnFanUnitID=_RbnFanUnitID_Object((1,3,6,1,4,1,2352,2,4,1,5,1,1),_RbnFanUnitID_Type())
rbnFanUnitID.setMaxAccess(_G)
if mibBuilder.loadTexts:rbnFanUnitID.setStatus(_B)
class _RbnFanUnitDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RbnFanUnitDescr_Type.__name__=_F
_RbnFanUnitDescr_Object=MibTableColumn
rbnFanUnitDescr=_RbnFanUnitDescr_Object((1,3,6,1,4,1,2352,2,4,1,5,1,2),_RbnFanUnitDescr_Type())
rbnFanUnitDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnFanUnitDescr.setStatus(_B)
_RbnFanSpeedCurrent_Type=RbnFanSpeed
_RbnFanSpeedCurrent_Object=MibTableColumn
rbnFanSpeedCurrent=_RbnFanSpeedCurrent_Object((1,3,6,1,4,1,2352,2,4,1,5,1,3),_RbnFanSpeedCurrent_Type())
rbnFanSpeedCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnFanSpeedCurrent.setStatus(_B)
_RbnEntityTempSensorTable_Object=MibTable
rbnEntityTempSensorTable=_RbnEntityTempSensorTable_Object((1,3,6,1,4,1,2352,2,4,1,6))
if mibBuilder.loadTexts:rbnEntityTempSensorTable.setStatus(_B)
_RbnEntityTempSensorEntry_Object=MibTableRow
rbnEntityTempSensorEntry=_RbnEntityTempSensorEntry_Object((1,3,6,1,4,1,2352,2,4,1,6,1))
rbnEntityTempSensorEntry.setIndexNames((0,_I,_J),(0,_A,_g))
if mibBuilder.loadTexts:rbnEntityTempSensorEntry.setStatus(_B)
class _RbnEntityTempIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RbnEntityTempIndex_Type.__name__=_E
_RbnEntityTempIndex_Object=MibTableColumn
rbnEntityTempIndex=_RbnEntityTempIndex_Object((1,3,6,1,4,1,2352,2,4,1,6,1,1),_RbnEntityTempIndex_Type())
rbnEntityTempIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:rbnEntityTempIndex.setStatus(_B)
class _RbnEntityTempDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,48))
_RbnEntityTempDescr_Type.__name__=_F
_RbnEntityTempDescr_Object=MibTableColumn
rbnEntityTempDescr=_RbnEntityTempDescr_Object((1,3,6,1,4,1,2352,2,4,1,6,1,2),_RbnEntityTempDescr_Type())
rbnEntityTempDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnEntityTempDescr.setStatus(_B)
_RbnEntityTempCurrent_Type=RbnTemperature
_RbnEntityTempCurrent_Object=MibTableColumn
rbnEntityTempCurrent=_RbnEntityTempCurrent_Object((1,3,6,1,4,1,2352,2,4,1,6,1,3),_RbnEntityTempCurrent_Type())
rbnEntityTempCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnEntityTempCurrent.setStatus(_B)
if mibBuilder.loadTexts:rbnEntityTempCurrent.setUnits('degrees Celsius')
_RbnEnvMonMIBConformance_ObjectIdentity=ObjectIdentity
rbnEnvMonMIBConformance=_RbnEnvMonMIBConformance_ObjectIdentity((1,3,6,1,4,1,2352,2,4,2))
_RbnEnvMonMIBGroups_ObjectIdentity=ObjectIdentity
rbnEnvMonMIBGroups=_RbnEnvMonMIBGroups_ObjectIdentity((1,3,6,1,4,1,2352,2,4,2,1))
_RbnEnvMonMIBCompliances_ObjectIdentity=ObjectIdentity
rbnEnvMonMIBCompliances=_RbnEnvMonMIBCompliances_ObjectIdentity((1,3,6,1,4,1,2352,2,4,2,2))
rbnEnvMonMIBObjectGroup=ObjectGroup((1,3,6,1,4,1,2352,2,4,2,1,1))
rbnEnvMonMIBObjectGroup.setObjects(*((_A,_O),(_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:rbnEnvMonMIBObjectGroup.setStatus(_D)
rbnEnvMonVoltageObjectGroup=ObjectGroup((1,3,6,1,4,1,2352,2,4,2,1,3))
rbnEnvMonVoltageObjectGroup.setObjects(*((_A,_h),(_A,_i),(_A,_j)))
if mibBuilder.loadTexts:rbnEnvMonVoltageObjectGroup.setStatus(_B)
rbnEnvMonTempObjectGroup=ObjectGroup((1,3,6,1,4,1,2352,2,4,2,1,4))
rbnEnvMonTempObjectGroup.setObjects(*((_A,_k),(_A,_l)))
if mibBuilder.loadTexts:rbnEnvMonTempObjectGroup.setStatus(_D)
rbnEnvMonMIBObjectGroupV2=ObjectGroup((1,3,6,1,4,1,2352,2,4,2,1,5))
rbnEnvMonMIBObjectGroupV2.setObjects(*((_A,_O),(_A,_S),(_A,_Q),(_A,_T)))
if mibBuilder.loadTexts:rbnEnvMonMIBObjectGroupV2.setStatus(_B)
rbnEnvMonFanSpeedObjectGroup=ObjectGroup((1,3,6,1,4,1,2352,2,4,2,1,7))
rbnEnvMonFanSpeedObjectGroup.setObjects(*((_A,_m),(_A,_n)))
if mibBuilder.loadTexts:rbnEnvMonFanSpeedObjectGroup.setStatus(_B)
rbnEnvMonEntityObjectGroup=ObjectGroup((1,3,6,1,4,1,2352,2,4,2,1,8))
rbnEnvMonEntityObjectGroup.setObjects(*((_A,_o),(_A,_p)))
if mibBuilder.loadTexts:rbnEnvMonEntityObjectGroup.setStatus(_B)
rbnFanFailChange=NotificationType((1,3,6,1,4,1,2352,2,4,0,1))
rbnFanFailChange.setObjects((_A,_P))
if mibBuilder.loadTexts:rbnFanFailChange.setStatus(_D)
rbnPowerFailChange=NotificationType((1,3,6,1,4,1,2352,2,4,0,2))
rbnPowerFailChange.setObjects((_A,_R))
if mibBuilder.loadTexts:rbnPowerFailChange.setStatus(_D)
rbnFanStatusChange=NotificationType((1,3,6,1,4,1,2352,2,4,0,3))
rbnFanStatusChange.setObjects((_A,_S))
if mibBuilder.loadTexts:rbnFanStatusChange.setStatus(_B)
rbnPowerStatusChange=NotificationType((1,3,6,1,4,1,2352,2,4,0,4))
rbnPowerStatusChange.setObjects((_A,_T))
if mibBuilder.loadTexts:rbnPowerStatusChange.setStatus(_B)
rbnEnvMonMIBNotificationGroup=NotificationGroup((1,3,6,1,4,1,2352,2,4,2,1,2))
rbnEnvMonMIBNotificationGroup.setObjects(*((_A,_q),(_A,_r)))
if mibBuilder.loadTexts:rbnEnvMonMIBNotificationGroup.setStatus(_D)
rbnEnvMonMIBNotificationGroupV2=NotificationGroup((1,3,6,1,4,1,2352,2,4,2,1,6))
rbnEnvMonMIBNotificationGroupV2.setObjects(*((_A,_s),(_A,_t)))
if mibBuilder.loadTexts:rbnEnvMonMIBNotificationGroupV2.setStatus(_B)
rbnEnvMonMIBCompliance=ModuleCompliance((1,3,6,1,4,1,2352,2,4,2,2,1))
rbnEnvMonMIBCompliance.setObjects(*((_A,_U),(_A,_V)))
if mibBuilder.loadTexts:rbnEnvMonMIBCompliance.setStatus('obsolete')
rbnEnvMonMIBComplianceV2=ModuleCompliance((1,3,6,1,4,1,2352,2,4,2,2,2))
rbnEnvMonMIBComplianceV2.setObjects(*((_A,_U),(_A,_V),(_A,_H),(_A,_K)))
if mibBuilder.loadTexts:rbnEnvMonMIBComplianceV2.setStatus(_D)
rbnEnvMonMIBComplianceV3=ModuleCompliance((1,3,6,1,4,1,2352,2,4,2,2,3))
rbnEnvMonMIBComplianceV3.setObjects(*((_A,_L),(_A,_M),(_A,_H),(_A,_K)))
if mibBuilder.loadTexts:rbnEnvMonMIBComplianceV3.setStatus(_D)
rbnEnvMonMIBComplianceV4=ModuleCompliance((1,3,6,1,4,1,2352,2,4,2,2,4))
rbnEnvMonMIBComplianceV4.setObjects(*((_A,_L),(_A,_M),(_A,_H),(_A,_K),(_A,_W)))
if mibBuilder.loadTexts:rbnEnvMonMIBComplianceV4.setStatus(_D)
rbnEnvMonMIBComplianceV5=ModuleCompliance((1,3,6,1,4,1,2352,2,4,2,2,5))
rbnEnvMonMIBComplianceV5.setObjects(*((_A,_L),(_A,_M),(_A,_H),(_A,_W),(_A,_u)))
if mibBuilder.loadTexts:rbnEnvMonMIBComplianceV5.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'RbnVoltage':RbnVoltage,'RbnTemperature':RbnTemperature,'RbnFanSpeed':RbnFanSpeed,'rbnEnvMonMIB':rbnEnvMonMIB,'rbnEnvMonMIBNotifications':rbnEnvMonMIBNotifications,_q:rbnFanFailChange,_r:rbnPowerFailChange,_s:rbnFanStatusChange,_t:rbnPowerStatusChange,'rbnEnvMonMIBObjects':rbnEnvMonMIBObjects,'rbnFanStatusTable':rbnFanStatusTable,'rbnFanStatusEntry':rbnFanStatusEntry,_N:rbnFanIndex,_O:rbnFanDescr,_P:rbnFanFail,_S:rbnFanStatus,'rbnPowerStatusTable':rbnPowerStatusTable,'rbnPowerStatusEntry':rbnPowerStatusEntry,_b:rbnPowerIndex,_Q:rbnPowerDescr,_R:rbnPowerFail,_T:rbnPowerStatus,'rbnVoltageSensorTable':rbnVoltageSensorTable,'rbnVoltageSensorEntry':rbnVoltageSensorEntry,_c:rbnVoltageIndex,_h:rbnVoltageDescr,_i:rbnVoltageDesired,_j:rbnVoltageCurrent,'rbnCpuTempSensorTable':rbnCpuTempSensorTable,'rbnCpuTempSensorEntry':rbnCpuTempSensorEntry,_e:rbnCpuTempIndex,_k:rbnCpuTempDescr,_l:rbnCpuTempCurrent,'rbnFanSpeedTable':rbnFanSpeedTable,'rbnFanSpeedEntry':rbnFanSpeedEntry,_f:rbnFanUnitID,_m:rbnFanUnitDescr,_n:rbnFanSpeedCurrent,'rbnEntityTempSensorTable':rbnEntityTempSensorTable,'rbnEntityTempSensorEntry':rbnEntityTempSensorEntry,_g:rbnEntityTempIndex,_o:rbnEntityTempDescr,_p:rbnEntityTempCurrent,'rbnEnvMonMIBConformance':rbnEnvMonMIBConformance,'rbnEnvMonMIBGroups':rbnEnvMonMIBGroups,_U:rbnEnvMonMIBObjectGroup,_V:rbnEnvMonMIBNotificationGroup,_H:rbnEnvMonVoltageObjectGroup,_K:rbnEnvMonTempObjectGroup,_L:rbnEnvMonMIBObjectGroupV2,_M:rbnEnvMonMIBNotificationGroupV2,_W:rbnEnvMonFanSpeedObjectGroup,_u:rbnEnvMonEntityObjectGroup,'rbnEnvMonMIBCompliances':rbnEnvMonMIBCompliances,'rbnEnvMonMIBCompliance':rbnEnvMonMIBCompliance,'rbnEnvMonMIBComplianceV2':rbnEnvMonMIBComplianceV2,'rbnEnvMonMIBComplianceV3':rbnEnvMonMIBComplianceV3,'rbnEnvMonMIBComplianceV4':rbnEnvMonMIBComplianceV4,'rbnEnvMonMIBComplianceV5':rbnEnvMonMIBComplianceV5})