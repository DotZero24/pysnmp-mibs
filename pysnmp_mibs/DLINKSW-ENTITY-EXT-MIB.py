_A9='dEntityExtGenericNotifInfoGroup'
_A8='dEntityExtPowerNotifGroup'
_A7='dEntityExtPowerGroup'
_A6='dEntityExtFanNotifGroup'
_A5='dEntityExtFanGroup'
_A4='dEntityExtThermalNotifGroup'
_A3='dEntityExtTempGroup'
_A2='dEntityExtSystemInfoGroup'
_A1='dEntityExtFactoryResetButton'
_A0='dEntityExtAirFlowChg'
_z='dEntityExtPowerStatusChg'
_y='dEntityExtThermalStatusChg'
_x='dEntityExtFanStatusChg'
_w='dEntityExtEnvAirFlowStatus'
_v='dEntityExtEnvNotifyEnable'
_u='dEntityExtVersionRuntime'
_t='dEntityExtVersionBootloader'
_s='dEntityExtCpuUtilFiveMinutes'
_r='dEntityExtCpuUtilOneMinute'
_q='dEntityExtCpuUtilFiveSeconds'
_p='dEntityExtMemUtilFree'
_o='dEntityExtMemUtilUsed'
_n='dEntityExtMemUtilTotal'
_m='dEntityExtUnitUpTime'
_l='dEntityExtUnitStatus'
_k='dEntityExtEnvPowerMaxPower'
_j='dEntityExtEnvPowerUsedPower'
_i='dEntityExtEnvPowerDescr'
_h='dEntityExtEnvFanDescr'
_g='dEntityExtEnvTempThresholdHigh'
_f='dEntityExtEnvTempThresholdLow'
_e='dEntityExtEnvTempCurrent'
_d='dEntityExtEnvTempDescr'
_c='dEntityExtVersionUnitId'
_b='percentage'
_a='dEntityExtCpuUtilCpuID'
_Z='dEntityExtCpuUtilUnitId'
_Y='dEntityExtMemUtilType'
_X='dEntityExtMemUtilUnitId'
_W='failed'
_V='abnormal'
_U='dEntityExtEnvPowerStatus'
_T='dEntityExtEnvFanStatus'
_S='dEntityExtEnvTempStatus'
_R='dEntityExtUnitIndex'
_Q='dEntityExtEnvAirFlowUnitId'
_P='dEntityExtEnvPowerIndex'
_O='dEntityExtEnvPowerUnitId'
_N='dEntityExtEnvFanIndex'
_M='dEntityExtEnvFanUnitId'
_L='read-write'
_K='degrees Celsius'
_J='dEntityExtEnvTempIndex'
_I='dEntityExtEnvTempUnitId'
_H='ok'
_G='DisplayString'
_F='Unsigned32'
_E='Integer32'
_D='not-accessible'
_C='read-only'
_B='DLINKSW-ENTITY-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlinkIndustrialCommon,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlinkIndustrialCommon')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention')
dlinkSwEntityExtMIB=ModuleIdentity((1,3,6,1,4,1,171,14,5))
if mibBuilder.loadTexts:dlinkSwEntityExtMIB.setRevisions(('2013-09-06 00:00','2013-03-13 00:00'))
_DEntityExtNotifications_ObjectIdentity=ObjectIdentity
dEntityExtNotifications=_DEntityExtNotifications_ObjectIdentity((1,3,6,1,4,1,171,14,5,0))
_DEntityExtObjects_ObjectIdentity=ObjectIdentity
dEntityExtObjects=_DEntityExtObjects_ObjectIdentity((1,3,6,1,4,1,171,14,5,1))
_DEntityExtEnvObjects_ObjectIdentity=ObjectIdentity
dEntityExtEnvObjects=_DEntityExtEnvObjects_ObjectIdentity((1,3,6,1,4,1,171,14,5,1,1))
_DEntityExtEnvTempTable_Object=MibTable
dEntityExtEnvTempTable=_DEntityExtEnvTempTable_Object((1,3,6,1,4,1,171,14,5,1,1,1))
if mibBuilder.loadTexts:dEntityExtEnvTempTable.setStatus(_A)
_DEntityExtEnvTempEntry_Object=MibTableRow
dEntityExtEnvTempEntry=_DEntityExtEnvTempEntry_Object((1,3,6,1,4,1,171,14,5,1,1,1,1))
dEntityExtEnvTempEntry.setIndexNames((0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:dEntityExtEnvTempEntry.setStatus(_A)
class _DEntityExtEnvTempUnitId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_DEntityExtEnvTempUnitId_Type.__name__=_F
_DEntityExtEnvTempUnitId_Object=MibTableColumn
dEntityExtEnvTempUnitId=_DEntityExtEnvTempUnitId_Object((1,3,6,1,4,1,171,14,5,1,1,1,1,1),_DEntityExtEnvTempUnitId_Type())
dEntityExtEnvTempUnitId.setMaxAccess(_D)
if mibBuilder.loadTexts:dEntityExtEnvTempUnitId.setStatus(_A)
class _DEntityExtEnvTempIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_DEntityExtEnvTempIndex_Type.__name__=_E
_DEntityExtEnvTempIndex_Object=MibTableColumn
dEntityExtEnvTempIndex=_DEntityExtEnvTempIndex_Object((1,3,6,1,4,1,171,14,5,1,1,1,1,2),_DEntityExtEnvTempIndex_Type())
dEntityExtEnvTempIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:dEntityExtEnvTempIndex.setStatus(_A)
class _DEntityExtEnvTempDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_DEntityExtEnvTempDescr_Type.__name__=_G
_DEntityExtEnvTempDescr_Object=MibTableColumn
dEntityExtEnvTempDescr=_DEntityExtEnvTempDescr_Object((1,3,6,1,4,1,171,14,5,1,1,1,1,3),_DEntityExtEnvTempDescr_Type())
dEntityExtEnvTempDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:dEntityExtEnvTempDescr.setStatus(_A)
_DEntityExtEnvTempCurrent_Type=Integer32
_DEntityExtEnvTempCurrent_Object=MibTableColumn
dEntityExtEnvTempCurrent=_DEntityExtEnvTempCurrent_Object((1,3,6,1,4,1,171,14,5,1,1,1,1,4),_DEntityExtEnvTempCurrent_Type())
dEntityExtEnvTempCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:dEntityExtEnvTempCurrent.setStatus(_A)
if mibBuilder.loadTexts:dEntityExtEnvTempCurrent.setUnits(_K)
_DEntityExtEnvTempThresholdLow_Type=Integer32
_DEntityExtEnvTempThresholdLow_Object=MibTableColumn
dEntityExtEnvTempThresholdLow=_DEntityExtEnvTempThresholdLow_Object((1,3,6,1,4,1,171,14,5,1,1,1,1,5),_DEntityExtEnvTempThresholdLow_Type())
dEntityExtEnvTempThresholdLow.setMaxAccess(_L)
if mibBuilder.loadTexts:dEntityExtEnvTempThresholdLow.setStatus(_A)
if mibBuilder.loadTexts:dEntityExtEnvTempThresholdLow.setUnits(_K)
_DEntityExtEnvTempThresholdHigh_Type=Integer32
_DEntityExtEnvTempThresholdHigh_Object=MibTableColumn
dEntityExtEnvTempThresholdHigh=_DEntityExtEnvTempThresholdHigh_Object((1,3,6,1,4,1,171,14,5,1,1,1,1,6),_DEntityExtEnvTempThresholdHigh_Type())
dEntityExtEnvTempThresholdHigh.setMaxAccess(_L)
if mibBuilder.loadTexts:dEntityExtEnvTempThresholdHigh.setStatus(_A)
if mibBuilder.loadTexts:dEntityExtEnvTempThresholdHigh.setUnits(_K)
class _DEntityExtEnvTempStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_V,2)))
_DEntityExtEnvTempStatus_Type.__name__=_E
_DEntityExtEnvTempStatus_Object=MibTableColumn
dEntityExtEnvTempStatus=_DEntityExtEnvTempStatus_Object((1,3,6,1,4,1,171,14,5,1,1,1,1,7),_DEntityExtEnvTempStatus_Type())
dEntityExtEnvTempStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dEntityExtEnvTempStatus.setStatus(_A)
_DEntityExtEnvFanTable_Object=MibTable
dEntityExtEnvFanTable=_DEntityExtEnvFanTable_Object((1,3,6,1,4,1,171,14,5,1,1,2))
if mibBuilder.loadTexts:dEntityExtEnvFanTable.setStatus(_A)
_DEntityExtEnvFanEntry_Object=MibTableRow
dEntityExtEnvFanEntry=_DEntityExtEnvFanEntry_Object((1,3,6,1,4,1,171,14,5,1,1,2,1))
dEntityExtEnvFanEntry.setIndexNames((0,_B,_M),(0,_B,_N))
if mibBuilder.loadTexts:dEntityExtEnvFanEntry.setStatus(_A)
class _DEntityExtEnvFanUnitId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_DEntityExtEnvFanUnitId_Type.__name__=_F
_DEntityExtEnvFanUnitId_Object=MibTableColumn
dEntityExtEnvFanUnitId=_DEntityExtEnvFanUnitId_Object((1,3,6,1,4,1,171,14,5,1,1,2,1,1),_DEntityExtEnvFanUnitId_Type())
dEntityExtEnvFanUnitId.setMaxAccess(_D)
if mibBuilder.loadTexts:dEntityExtEnvFanUnitId.setStatus(_A)
class _DEntityExtEnvFanIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_DEntityExtEnvFanIndex_Type.__name__=_E
_DEntityExtEnvFanIndex_Object=MibTableColumn
dEntityExtEnvFanIndex=_DEntityExtEnvFanIndex_Object((1,3,6,1,4,1,171,14,5,1,1,2,1,2),_DEntityExtEnvFanIndex_Type())
dEntityExtEnvFanIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:dEntityExtEnvFanIndex.setStatus(_A)
class _DEntityExtEnvFanDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_DEntityExtEnvFanDescr_Type.__name__=_G
_DEntityExtEnvFanDescr_Object=MibTableColumn
dEntityExtEnvFanDescr=_DEntityExtEnvFanDescr_Object((1,3,6,1,4,1,171,14,5,1,1,2,1,3),_DEntityExtEnvFanDescr_Type())
dEntityExtEnvFanDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:dEntityExtEnvFanDescr.setStatus(_A)
class _DEntityExtEnvFanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),('fault',2)))
_DEntityExtEnvFanStatus_Type.__name__=_E
_DEntityExtEnvFanStatus_Object=MibTableColumn
dEntityExtEnvFanStatus=_DEntityExtEnvFanStatus_Object((1,3,6,1,4,1,171,14,5,1,1,2,1,4),_DEntityExtEnvFanStatus_Type())
dEntityExtEnvFanStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dEntityExtEnvFanStatus.setStatus(_A)
_DEntityExtEnvPowerTable_Object=MibTable
dEntityExtEnvPowerTable=_DEntityExtEnvPowerTable_Object((1,3,6,1,4,1,171,14,5,1,1,3))
if mibBuilder.loadTexts:dEntityExtEnvPowerTable.setStatus(_A)
_DEntityExtEnvPowerEntry_Object=MibTableRow
dEntityExtEnvPowerEntry=_DEntityExtEnvPowerEntry_Object((1,3,6,1,4,1,171,14,5,1,1,3,1))
dEntityExtEnvPowerEntry.setIndexNames((0,_B,_O),(0,_B,_P))
if mibBuilder.loadTexts:dEntityExtEnvPowerEntry.setStatus(_A)
class _DEntityExtEnvPowerUnitId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_DEntityExtEnvPowerUnitId_Type.__name__=_F
_DEntityExtEnvPowerUnitId_Object=MibTableColumn
dEntityExtEnvPowerUnitId=_DEntityExtEnvPowerUnitId_Object((1,3,6,1,4,1,171,14,5,1,1,3,1,1),_DEntityExtEnvPowerUnitId_Type())
dEntityExtEnvPowerUnitId.setMaxAccess(_D)
if mibBuilder.loadTexts:dEntityExtEnvPowerUnitId.setStatus(_A)
class _DEntityExtEnvPowerIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_DEntityExtEnvPowerIndex_Type.__name__=_F
_DEntityExtEnvPowerIndex_Object=MibTableColumn
dEntityExtEnvPowerIndex=_DEntityExtEnvPowerIndex_Object((1,3,6,1,4,1,171,14,5,1,1,3,1,2),_DEntityExtEnvPowerIndex_Type())
dEntityExtEnvPowerIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:dEntityExtEnvPowerIndex.setStatus(_A)
class _DEntityExtEnvPowerDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_DEntityExtEnvPowerDescr_Type.__name__=_G
_DEntityExtEnvPowerDescr_Object=MibTableColumn
dEntityExtEnvPowerDescr=_DEntityExtEnvPowerDescr_Object((1,3,6,1,4,1,171,14,5,1,1,3,1,3),_DEntityExtEnvPowerDescr_Type())
dEntityExtEnvPowerDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:dEntityExtEnvPowerDescr.setStatus(_A)
_DEntityExtEnvPowerUsedPower_Type=Unsigned32
_DEntityExtEnvPowerUsedPower_Object=MibTableColumn
dEntityExtEnvPowerUsedPower=_DEntityExtEnvPowerUsedPower_Object((1,3,6,1,4,1,171,14,5,1,1,3,1,4),_DEntityExtEnvPowerUsedPower_Type())
dEntityExtEnvPowerUsedPower.setMaxAccess(_C)
if mibBuilder.loadTexts:dEntityExtEnvPowerUsedPower.setStatus(_A)
if mibBuilder.loadTexts:dEntityExtEnvPowerUsedPower.setUnits('watts')
_DEntityExtEnvPowerMaxPower_Type=Unsigned32
_DEntityExtEnvPowerMaxPower_Object=MibTableColumn
dEntityExtEnvPowerMaxPower=_DEntityExtEnvPowerMaxPower_Object((1,3,6,1,4,1,171,14,5,1,1,3,1,5),_DEntityExtEnvPowerMaxPower_Type())
dEntityExtEnvPowerMaxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:dEntityExtEnvPowerMaxPower.setStatus(_A)
if mibBuilder.loadTexts:dEntityExtEnvPowerMaxPower.setUnits('watts')
class _DEntityExtEnvPowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('inOperation',1),(_W,2),('empty',3)))
_DEntityExtEnvPowerStatus_Type.__name__=_E
_DEntityExtEnvPowerStatus_Object=MibTableColumn
dEntityExtEnvPowerStatus=_DEntityExtEnvPowerStatus_Object((1,3,6,1,4,1,171,14,5,1,1,3,1,6),_DEntityExtEnvPowerStatus_Type())
dEntityExtEnvPowerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dEntityExtEnvPowerStatus.setStatus(_A)
_DEntityExtEnvAirFlowTable_Object=MibTable
dEntityExtEnvAirFlowTable=_DEntityExtEnvAirFlowTable_Object((1,3,6,1,4,1,171,14,5,1,1,4))
if mibBuilder.loadTexts:dEntityExtEnvAirFlowTable.setStatus(_A)
_DEntityExtEnvAirFlowEntry_Object=MibTableRow
dEntityExtEnvAirFlowEntry=_DEntityExtEnvAirFlowEntry_Object((1,3,6,1,4,1,171,14,5,1,1,4,1))
dEntityExtEnvAirFlowEntry.setIndexNames((0,_B,_Q))
if mibBuilder.loadTexts:dEntityExtEnvAirFlowEntry.setStatus(_A)
class _DEntityExtEnvAirFlowUnitId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_DEntityExtEnvAirFlowUnitId_Type.__name__=_F
_DEntityExtEnvAirFlowUnitId_Object=MibTableColumn
dEntityExtEnvAirFlowUnitId=_DEntityExtEnvAirFlowUnitId_Object((1,3,6,1,4,1,171,14,5,1,1,4,1,1),_DEntityExtEnvAirFlowUnitId_Type())
dEntityExtEnvAirFlowUnitId.setMaxAccess(_D)
if mibBuilder.loadTexts:dEntityExtEnvAirFlowUnitId.setStatus(_A)
class _DEntityExtEnvAirFlowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_V,2)))
_DEntityExtEnvAirFlowStatus_Type.__name__=_E
_DEntityExtEnvAirFlowStatus_Object=MibTableColumn
dEntityExtEnvAirFlowStatus=_DEntityExtEnvAirFlowStatus_Object((1,3,6,1,4,1,171,14,5,1,1,4,1,2),_DEntityExtEnvAirFlowStatus_Type())
dEntityExtEnvAirFlowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dEntityExtEnvAirFlowStatus.setStatus(_A)
_DEntityExtEnvTrap_ObjectIdentity=ObjectIdentity
dEntityExtEnvTrap=_DEntityExtEnvTrap_ObjectIdentity((1,3,6,1,4,1,171,14,5,1,2))
class _DEntityExtEnvNotifyEnable_Type(Bits):namedValues=NamedValues(*(('fan',0),('power',1),('temperature',2)))
_DEntityExtEnvNotifyEnable_Type.__name__='Bits'
_DEntityExtEnvNotifyEnable_Object=MibScalar
dEntityExtEnvNotifyEnable=_DEntityExtEnvNotifyEnable_Object((1,3,6,1,4,1,171,14,5,1,2,1),_DEntityExtEnvNotifyEnable_Type())
dEntityExtEnvNotifyEnable.setMaxAccess(_L)
if mibBuilder.loadTexts:dEntityExtEnvNotifyEnable.setStatus(_A)
_DEntityExtUnitTable_Object=MibTable
dEntityExtUnitTable=_DEntityExtUnitTable_Object((1,3,6,1,4,1,171,14,5,1,3))
if mibBuilder.loadTexts:dEntityExtUnitTable.setStatus(_A)
_DEntityExtUnitEntry_Object=MibTableRow
dEntityExtUnitEntry=_DEntityExtUnitEntry_Object((1,3,6,1,4,1,171,14,5,1,3,1))
dEntityExtUnitEntry.setIndexNames((0,_B,_R))
if mibBuilder.loadTexts:dEntityExtUnitEntry.setStatus(_A)
class _DEntityExtUnitIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_DEntityExtUnitIndex_Type.__name__=_F
_DEntityExtUnitIndex_Object=MibTableColumn
dEntityExtUnitIndex=_DEntityExtUnitIndex_Object((1,3,6,1,4,1,171,14,5,1,3,1,1),_DEntityExtUnitIndex_Type())
dEntityExtUnitIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:dEntityExtUnitIndex.setStatus(_A)
class _DEntityExtUnitStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_W,2),('empty',3)))
_DEntityExtUnitStatus_Type.__name__=_E
_DEntityExtUnitStatus_Object=MibTableColumn
dEntityExtUnitStatus=_DEntityExtUnitStatus_Object((1,3,6,1,4,1,171,14,5,1,3,1,2),_DEntityExtUnitStatus_Type())
dEntityExtUnitStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dEntityExtUnitStatus.setStatus(_A)
_DEntityExtUnitUpTime_Type=Unsigned32
_DEntityExtUnitUpTime_Object=MibTableColumn
dEntityExtUnitUpTime=_DEntityExtUnitUpTime_Object((1,3,6,1,4,1,171,14,5,1,3,1,3),_DEntityExtUnitUpTime_Type())
dEntityExtUnitUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:dEntityExtUnitUpTime.setStatus(_A)
if mibBuilder.loadTexts:dEntityExtUnitUpTime.setUnits('seconds')
_DEntityExtMemoryUtilTable_Object=MibTable
dEntityExtMemoryUtilTable=_DEntityExtMemoryUtilTable_Object((1,3,6,1,4,1,171,14,5,1,4))
if mibBuilder.loadTexts:dEntityExtMemoryUtilTable.setStatus(_A)
_DEntityExtMemoryUtilEntry_Object=MibTableRow
dEntityExtMemoryUtilEntry=_DEntityExtMemoryUtilEntry_Object((1,3,6,1,4,1,171,14,5,1,4,1))
dEntityExtMemoryUtilEntry.setIndexNames((0,_B,_X),(0,_B,_Y))
if mibBuilder.loadTexts:dEntityExtMemoryUtilEntry.setStatus(_A)
class _DEntityExtMemUtilUnitId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_DEntityExtMemUtilUnitId_Type.__name__=_E
_DEntityExtMemUtilUnitId_Object=MibTableColumn
dEntityExtMemUtilUnitId=_DEntityExtMemUtilUnitId_Object((1,3,6,1,4,1,171,14,5,1,4,1,1),_DEntityExtMemUtilUnitId_Type())
dEntityExtMemUtilUnitId.setMaxAccess(_D)
if mibBuilder.loadTexts:dEntityExtMemUtilUnitId.setStatus(_A)
class _DEntityExtMemUtilType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('dram',1),('flash',2),('nvram',3)))
_DEntityExtMemUtilType_Type.__name__=_E
_DEntityExtMemUtilType_Object=MibTableColumn
dEntityExtMemUtilType=_DEntityExtMemUtilType_Object((1,3,6,1,4,1,171,14,5,1,4,1,2),_DEntityExtMemUtilType_Type())
dEntityExtMemUtilType.setMaxAccess(_D)
if mibBuilder.loadTexts:dEntityExtMemUtilType.setStatus(_A)
_DEntityExtMemUtilTotal_Type=Unsigned32
_DEntityExtMemUtilTotal_Object=MibTableColumn
dEntityExtMemUtilTotal=_DEntityExtMemUtilTotal_Object((1,3,6,1,4,1,171,14,5,1,4,1,3),_DEntityExtMemUtilTotal_Type())
dEntityExtMemUtilTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:dEntityExtMemUtilTotal.setStatus(_A)
if mibBuilder.loadTexts:dEntityExtMemUtilTotal.setUnits('KB')
_DEntityExtMemUtilUsed_Type=Unsigned32
_DEntityExtMemUtilUsed_Object=MibTableColumn
dEntityExtMemUtilUsed=_DEntityExtMemUtilUsed_Object((1,3,6,1,4,1,171,14,5,1,4,1,4),_DEntityExtMemUtilUsed_Type())
dEntityExtMemUtilUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:dEntityExtMemUtilUsed.setStatus(_A)
if mibBuilder.loadTexts:dEntityExtMemUtilUsed.setUnits('KB')
_DEntityExtMemUtilFree_Type=Unsigned32
_DEntityExtMemUtilFree_Object=MibTableColumn
dEntityExtMemUtilFree=_DEntityExtMemUtilFree_Object((1,3,6,1,4,1,171,14,5,1,4,1,5),_DEntityExtMemUtilFree_Type())
dEntityExtMemUtilFree.setMaxAccess(_C)
if mibBuilder.loadTexts:dEntityExtMemUtilFree.setStatus(_A)
if mibBuilder.loadTexts:dEntityExtMemUtilFree.setUnits('KB')
_DEntityExtCpuUtilTable_Object=MibTable
dEntityExtCpuUtilTable=_DEntityExtCpuUtilTable_Object((1,3,6,1,4,1,171,14,5,1,7))
if mibBuilder.loadTexts:dEntityExtCpuUtilTable.setStatus(_A)
_DEntityExtCpuUtilEntry_Object=MibTableRow
dEntityExtCpuUtilEntry=_DEntityExtCpuUtilEntry_Object((1,3,6,1,4,1,171,14,5,1,7,1))
dEntityExtCpuUtilEntry.setIndexNames((0,_B,_Z),(0,_B,_a))
if mibBuilder.loadTexts:dEntityExtCpuUtilEntry.setStatus(_A)
class _DEntityExtCpuUtilUnitId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_DEntityExtCpuUtilUnitId_Type.__name__=_F
_DEntityExtCpuUtilUnitId_Object=MibTableColumn
dEntityExtCpuUtilUnitId=_DEntityExtCpuUtilUnitId_Object((1,3,6,1,4,1,171,14,5,1,7,1,1),_DEntityExtCpuUtilUnitId_Type())
dEntityExtCpuUtilUnitId.setMaxAccess(_D)
if mibBuilder.loadTexts:dEntityExtCpuUtilUnitId.setStatus(_A)
class _DEntityExtCpuUtilCpuID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_DEntityExtCpuUtilCpuID_Type.__name__=_F
_DEntityExtCpuUtilCpuID_Object=MibTableColumn
dEntityExtCpuUtilCpuID=_DEntityExtCpuUtilCpuID_Object((1,3,6,1,4,1,171,14,5,1,7,1,2),_DEntityExtCpuUtilCpuID_Type())
dEntityExtCpuUtilCpuID.setMaxAccess(_D)
if mibBuilder.loadTexts:dEntityExtCpuUtilCpuID.setStatus(_A)
_DEntityExtCpuUtilFiveSeconds_Type=Unsigned32
_DEntityExtCpuUtilFiveSeconds_Object=MibTableColumn
dEntityExtCpuUtilFiveSeconds=_DEntityExtCpuUtilFiveSeconds_Object((1,3,6,1,4,1,171,14,5,1,7,1,3),_DEntityExtCpuUtilFiveSeconds_Type())
dEntityExtCpuUtilFiveSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:dEntityExtCpuUtilFiveSeconds.setStatus(_A)
if mibBuilder.loadTexts:dEntityExtCpuUtilFiveSeconds.setUnits(_b)
_DEntityExtCpuUtilOneMinute_Type=Unsigned32
_DEntityExtCpuUtilOneMinute_Object=MibTableColumn
dEntityExtCpuUtilOneMinute=_DEntityExtCpuUtilOneMinute_Object((1,3,6,1,4,1,171,14,5,1,7,1,4),_DEntityExtCpuUtilOneMinute_Type())
dEntityExtCpuUtilOneMinute.setMaxAccess(_C)
if mibBuilder.loadTexts:dEntityExtCpuUtilOneMinute.setStatus(_A)
if mibBuilder.loadTexts:dEntityExtCpuUtilOneMinute.setUnits(_b)
_DEntityExtCpuUtilFiveMinutes_Type=Unsigned32
_DEntityExtCpuUtilFiveMinutes_Object=MibTableColumn
dEntityExtCpuUtilFiveMinutes=_DEntityExtCpuUtilFiveMinutes_Object((1,3,6,1,4,1,171,14,5,1,7,1,5),_DEntityExtCpuUtilFiveMinutes_Type())
dEntityExtCpuUtilFiveMinutes.setMaxAccess(_C)
if mibBuilder.loadTexts:dEntityExtCpuUtilFiveMinutes.setStatus(_A)
_DEntityExtVersionTable_Object=MibTable
dEntityExtVersionTable=_DEntityExtVersionTable_Object((1,3,6,1,4,1,171,14,5,1,8))
if mibBuilder.loadTexts:dEntityExtVersionTable.setStatus(_A)
_DEntityExtVersionEntry_Object=MibTableRow
dEntityExtVersionEntry=_DEntityExtVersionEntry_Object((1,3,6,1,4,1,171,14,5,1,8,1))
dEntityExtVersionEntry.setIndexNames((0,_B,_c))
if mibBuilder.loadTexts:dEntityExtVersionEntry.setStatus(_A)
class _DEntityExtVersionUnitId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_DEntityExtVersionUnitId_Type.__name__=_F
_DEntityExtVersionUnitId_Object=MibTableColumn
dEntityExtVersionUnitId=_DEntityExtVersionUnitId_Object((1,3,6,1,4,1,171,14,5,1,8,1,1),_DEntityExtVersionUnitId_Type())
dEntityExtVersionUnitId.setMaxAccess(_D)
if mibBuilder.loadTexts:dEntityExtVersionUnitId.setStatus(_A)
class _DEntityExtVersionBootloader_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_DEntityExtVersionBootloader_Type.__name__=_G
_DEntityExtVersionBootloader_Object=MibTableColumn
dEntityExtVersionBootloader=_DEntityExtVersionBootloader_Object((1,3,6,1,4,1,171,14,5,1,8,1,2),_DEntityExtVersionBootloader_Type())
dEntityExtVersionBootloader.setMaxAccess(_C)
if mibBuilder.loadTexts:dEntityExtVersionBootloader.setStatus(_A)
class _DEntityExtVersionRuntime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_DEntityExtVersionRuntime_Type.__name__=_G
_DEntityExtVersionRuntime_Object=MibTableColumn
dEntityExtVersionRuntime=_DEntityExtVersionRuntime_Object((1,3,6,1,4,1,171,14,5,1,8,1,3),_DEntityExtVersionRuntime_Type())
dEntityExtVersionRuntime.setMaxAccess(_C)
if mibBuilder.loadTexts:dEntityExtVersionRuntime.setStatus(_A)
_DEntityExtConformance_ObjectIdentity=ObjectIdentity
dEntityExtConformance=_DEntityExtConformance_ObjectIdentity((1,3,6,1,4,1,171,14,5,2))
_DEntityExtMIBCompliances_ObjectIdentity=ObjectIdentity
dEntityExtMIBCompliances=_DEntityExtMIBCompliances_ObjectIdentity((1,3,6,1,4,1,171,14,5,2,1))
_DEntityExtMIBGroups_ObjectIdentity=ObjectIdentity
dEntityExtMIBGroups=_DEntityExtMIBGroups_ObjectIdentity((1,3,6,1,4,1,171,14,5,2,2))
dEntityExtTempGroup=ObjectGroup((1,3,6,1,4,1,171,14,5,2,2,1))
dEntityExtTempGroup.setObjects(*((_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_S)))
if mibBuilder.loadTexts:dEntityExtTempGroup.setStatus(_A)
dEntityExtFanGroup=ObjectGroup((1,3,6,1,4,1,171,14,5,2,2,2))
dEntityExtFanGroup.setObjects(*((_B,_h),(_B,_T)))
if mibBuilder.loadTexts:dEntityExtFanGroup.setStatus(_A)
dEntityExtPowerGroup=ObjectGroup((1,3,6,1,4,1,171,14,5,2,2,3))
dEntityExtPowerGroup.setObjects(*((_B,_i),(_B,_j),(_B,_k),(_B,_U)))
if mibBuilder.loadTexts:dEntityExtPowerGroup.setStatus(_A)
dEntityExtSystemInfoGroup=ObjectGroup((1,3,6,1,4,1,171,14,5,2,2,4))
dEntityExtSystemInfoGroup.setObjects(*((_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u)))
if mibBuilder.loadTexts:dEntityExtSystemInfoGroup.setStatus(_A)
dEntityExtGenericNotifInfoGroup=ObjectGroup((1,3,6,1,4,1,171,14,5,2,2,5))
dEntityExtGenericNotifInfoGroup.setObjects((_B,_v))
if mibBuilder.loadTexts:dEntityExtGenericNotifInfoGroup.setStatus(_A)
dEntityExtFanStatusChg=NotificationType((1,3,6,1,4,1,171,14,5,0,1))
dEntityExtFanStatusChg.setObjects(*((_B,_M),(_B,_N),(_B,_T)))
if mibBuilder.loadTexts:dEntityExtFanStatusChg.setStatus(_A)
dEntityExtThermalStatusChg=NotificationType((1,3,6,1,4,1,171,14,5,0,2))
dEntityExtThermalStatusChg.setObjects(*((_B,_I),(_B,_J),(_B,_S)))
if mibBuilder.loadTexts:dEntityExtThermalStatusChg.setStatus(_A)
dEntityExtPowerStatusChg=NotificationType((1,3,6,1,4,1,171,14,5,0,3))
dEntityExtPowerStatusChg.setObjects(*((_B,_O),(_B,_P),(_B,_U)))
if mibBuilder.loadTexts:dEntityExtPowerStatusChg.setStatus(_A)
dEntityExtAirFlowChg=NotificationType((1,3,6,1,4,1,171,14,5,0,4))
dEntityExtAirFlowChg.setObjects(*((_B,_Q),(_B,_w)))
if mibBuilder.loadTexts:dEntityExtAirFlowChg.setStatus(_A)
dEntityExtFactoryResetButton=NotificationType((1,3,6,1,4,1,171,14,5,0,5))
dEntityExtFactoryResetButton.setObjects((_B,_R))
if mibBuilder.loadTexts:dEntityExtFactoryResetButton.setStatus(_A)
dEntityExtFanNotifGroup=NotificationGroup((1,3,6,1,4,1,171,14,5,2,2,6))
dEntityExtFanNotifGroup.setObjects((_B,_x))
if mibBuilder.loadTexts:dEntityExtFanNotifGroup.setStatus(_A)
dEntityExtThermalNotifGroup=NotificationGroup((1,3,6,1,4,1,171,14,5,2,2,7))
dEntityExtThermalNotifGroup.setObjects((_B,_y))
if mibBuilder.loadTexts:dEntityExtThermalNotifGroup.setStatus(_A)
dEntityExtPowerNotifGroup=NotificationGroup((1,3,6,1,4,1,171,14,5,2,2,8))
dEntityExtPowerNotifGroup.setObjects((_B,_z))
if mibBuilder.loadTexts:dEntityExtPowerNotifGroup.setStatus(_A)
dEntityExtAirFlowNotifGroup=NotificationGroup((1,3,6,1,4,1,171,14,5,2,2,9))
dEntityExtAirFlowNotifGroup.setObjects((_B,_A0))
if mibBuilder.loadTexts:dEntityExtAirFlowNotifGroup.setStatus(_A)
dEntityExtFactoryResetButtonNotifGroup=NotificationGroup((1,3,6,1,4,1,171,14,5,2,2,10))
dEntityExtFactoryResetButtonNotifGroup.setObjects((_B,_A1))
if mibBuilder.loadTexts:dEntityExtFactoryResetButtonNotifGroup.setStatus(_A)
dEntityExtCompliance=ModuleCompliance((1,3,6,1,4,1,171,14,5,2,1,1))
dEntityExtCompliance.setObjects(*((_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,'dEntityExtAirFlowGroup'),(_B,_A9)))
if mibBuilder.loadTexts:dEntityExtCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'dlinkSwEntityExtMIB':dlinkSwEntityExtMIB,'dEntityExtNotifications':dEntityExtNotifications,_x:dEntityExtFanStatusChg,_y:dEntityExtThermalStatusChg,_z:dEntityExtPowerStatusChg,_A0:dEntityExtAirFlowChg,_A1:dEntityExtFactoryResetButton,'dEntityExtObjects':dEntityExtObjects,'dEntityExtEnvObjects':dEntityExtEnvObjects,'dEntityExtEnvTempTable':dEntityExtEnvTempTable,'dEntityExtEnvTempEntry':dEntityExtEnvTempEntry,_I:dEntityExtEnvTempUnitId,_J:dEntityExtEnvTempIndex,_d:dEntityExtEnvTempDescr,_e:dEntityExtEnvTempCurrent,_f:dEntityExtEnvTempThresholdLow,_g:dEntityExtEnvTempThresholdHigh,_S:dEntityExtEnvTempStatus,'dEntityExtEnvFanTable':dEntityExtEnvFanTable,'dEntityExtEnvFanEntry':dEntityExtEnvFanEntry,_M:dEntityExtEnvFanUnitId,_N:dEntityExtEnvFanIndex,_h:dEntityExtEnvFanDescr,_T:dEntityExtEnvFanStatus,'dEntityExtEnvPowerTable':dEntityExtEnvPowerTable,'dEntityExtEnvPowerEntry':dEntityExtEnvPowerEntry,_O:dEntityExtEnvPowerUnitId,_P:dEntityExtEnvPowerIndex,_i:dEntityExtEnvPowerDescr,_j:dEntityExtEnvPowerUsedPower,_k:dEntityExtEnvPowerMaxPower,_U:dEntityExtEnvPowerStatus,'dEntityExtEnvAirFlowTable':dEntityExtEnvAirFlowTable,'dEntityExtEnvAirFlowEntry':dEntityExtEnvAirFlowEntry,_Q:dEntityExtEnvAirFlowUnitId,_w:dEntityExtEnvAirFlowStatus,'dEntityExtEnvTrap':dEntityExtEnvTrap,_v:dEntityExtEnvNotifyEnable,'dEntityExtUnitTable':dEntityExtUnitTable,'dEntityExtUnitEntry':dEntityExtUnitEntry,_R:dEntityExtUnitIndex,_l:dEntityExtUnitStatus,_m:dEntityExtUnitUpTime,'dEntityExtMemoryUtilTable':dEntityExtMemoryUtilTable,'dEntityExtMemoryUtilEntry':dEntityExtMemoryUtilEntry,_X:dEntityExtMemUtilUnitId,_Y:dEntityExtMemUtilType,_n:dEntityExtMemUtilTotal,_o:dEntityExtMemUtilUsed,_p:dEntityExtMemUtilFree,'dEntityExtCpuUtilTable':dEntityExtCpuUtilTable,'dEntityExtCpuUtilEntry':dEntityExtCpuUtilEntry,_Z:dEntityExtCpuUtilUnitId,_a:dEntityExtCpuUtilCpuID,_q:dEntityExtCpuUtilFiveSeconds,_r:dEntityExtCpuUtilOneMinute,_s:dEntityExtCpuUtilFiveMinutes,'dEntityExtVersionTable':dEntityExtVersionTable,'dEntityExtVersionEntry':dEntityExtVersionEntry,_c:dEntityExtVersionUnitId,_t:dEntityExtVersionBootloader,_u:dEntityExtVersionRuntime,'dEntityExtConformance':dEntityExtConformance,'dEntityExtMIBCompliances':dEntityExtMIBCompliances,'dEntityExtCompliance':dEntityExtCompliance,'dEntityExtMIBGroups':dEntityExtMIBGroups,_A3:dEntityExtTempGroup,_A5:dEntityExtFanGroup,_A7:dEntityExtPowerGroup,_A2:dEntityExtSystemInfoGroup,_A9:dEntityExtGenericNotifInfoGroup,_A6:dEntityExtFanNotifGroup,_A4:dEntityExtThermalNotifGroup,_A8:dEntityExtPowerNotifGroup,'dEntityExtAirFlowNotifGroup':dEntityExtAirFlowNotifGroup,'dEntityExtFactoryResetButtonNotifGroup':dEntityExtFactoryResetButtonNotifGroup})