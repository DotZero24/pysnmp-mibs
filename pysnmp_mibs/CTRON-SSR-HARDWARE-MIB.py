_m='hwConfGroupV30'
_l='hwConfGroupV10'
_k='sysHwLastHotSwapEvent'
_j='sysHwControlModuleBackupState'
_i='sysHwTotalL3SwitchedFrames'
_h='sysHwTotalL2SwitchedFrames'
_g='sysHwTotalOutFrames'
_f='sysHwTotalInFrames'
_e='sysHwTotalOutOctets'
_d='sysHwTotalInOctets'
_c='hwConfGroupV11'
_b='sysHwModuleStatus'
_a='hssi'
_Z='sysHwControlModuleLED'
_Y='sysHwSwitchingFabric'
_X='sysHwModuleService'
_W='sysHwModuleMemory'
_V='OctetString'
_U='sysHwChassisId'
_T='sysHwTemperature'
_S='sysHwFan'
_R='sysHwPowerSupply'
_Q='sysHwPortIfIndex'
_P='sysHwPortConnectorType'
_O='sysHwPortType'
_N='sysHwModuleVersion'
_M='sysHwModuleNumPorts'
_L='sysHwModuleDesc'
_K='sysHwModuleType'
_J='sysHwNumSlots'
_I='sysHwPortNumber'
_H='sysHwPortSlotNumber'
_G='sysHwModuleSlotNumber'
_F='unknown'
_E='Integer32'
_D='deprecated'
_C='read-only'
_B='current'
_A='CTRON-SSR-HARDWARE-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_V,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ssrMibs,=mibBuilder.importSymbols('CTRON-SSR-SMI-MIB','ssrMibs')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hardwareMIB=ModuleIdentity((1,3,6,1,4,1,52,2501,1,200))
if mibBuilder.loadTexts:hardwareMIB.setRevisions(('2000-07-17 00:00','2000-07-15 00:00','2000-05-31 00:00','2000-03-20 00:00','1999-12-30 00:00','1999-01-20 00:00','1998-08-04 00:00'))
class SSRInterfaceIndex(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
class SSRModuleType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,17,20,21,22,24,25,26,27,28,29,30,503,504,505,506,507)));namedValues=NamedValues(*(('controlModule',1),('ether100TX',2),('ether100FX',3),('gigabitSX',4),('gigabitLX',5),('serial4port',6),(_a,7),(_F,8),('gigabitLLX',9),('none',10),('controlModule2',11),('gigabitLLX2P',12),('serial2port',13),('cmts1x4port',15),('fddi2port',16),('controlModule3',17),('serial4portCE',20),('ether100TX16port',21),('gigabitTX',22),('atm155',24),('sonet4PortOc3',25),('sonet2PortOc12',26),('gigabitFX4P',27),('gigabitFX4PGBIC',28),('gigabitFX2PGBIC',29),('gigabit6K2PBP',30),('rbGigabit8PGBIC',503),('rbGigabit4PGBIC',504),('rbEther100TX24P',505),('rbEther100TC32P',506),('rbControlModule',507)))
class SSRModuleStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('online',1),('offline',2)))
class SSRPortType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('etherFast',1),('gigEther',2),(_a,3),('serial',4),(_F,5),('sonet',6),('ds1',7),('ds3',8),('cmt',9),('e1',10),('e3',11),('fddi',12)))
class SSRPortConnectorType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24)));namedValues=NamedValues(*(('empty',0),('db9m',1),('db9f',2),('db15m',3),('db15f',4),('db25m',5),('db25f',6),('rj11',7),('rj45',8),('aui',9),('ftypef',10),('fiberScMM',11),('v35',12),('eia530',13),('rs44x',14),('x21',15),(_a,16),(_F,17),('fiberScSM',18),('fiberMTRjMM',19),('fiberMTRjSM',20),('bncf',21),('bncm',22),('rj21',23),('fiberScSMLH',24)))
class SSRserviceType(TextualConvention,OctetString):status=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,7))
class SSRmemorySize(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
class SSRSwitchingFabricInfo(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
class SSRCmLedState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
class SSRBackupCMState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),('inactive',2),('standby',3),('notInstalled',4),('active',5)))
class PowerSupplyBits(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SysHwGroup_ObjectIdentity=ObjectIdentity
sysHwGroup=_SysHwGroup_ObjectIdentity((1,3,6,1,4,1,52,2501,1,1))
class _SysHwNumSlots_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_SysHwNumSlots_Type.__name__=_E
_SysHwNumSlots_Object=MibScalar
sysHwNumSlots=_SysHwNumSlots_Object((1,3,6,1,4,1,52,2501,1,1,1),_SysHwNumSlots_Type())
sysHwNumSlots.setMaxAccess(_C)
if mibBuilder.loadTexts:sysHwNumSlots.setStatus(_B)
_SysHwModuleTable_Object=MibTable
sysHwModuleTable=_SysHwModuleTable_Object((1,3,6,1,4,1,52,2501,1,1,2))
if mibBuilder.loadTexts:sysHwModuleTable.setStatus(_B)
_SysHwModuleEntry_Object=MibTableRow
sysHwModuleEntry=_SysHwModuleEntry_Object((1,3,6,1,4,1,52,2501,1,1,2,1))
sysHwModuleEntry.setIndexNames((0,_A,_G))
if mibBuilder.loadTexts:sysHwModuleEntry.setStatus(_B)
class _SysHwModuleSlotNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65))
_SysHwModuleSlotNumber_Type.__name__=_E
_SysHwModuleSlotNumber_Object=MibTableColumn
sysHwModuleSlotNumber=_SysHwModuleSlotNumber_Object((1,3,6,1,4,1,52,2501,1,1,2,1,1),_SysHwModuleSlotNumber_Type())
sysHwModuleSlotNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:sysHwModuleSlotNumber.setStatus(_B)
_SysHwModuleType_Type=SSRModuleType
_SysHwModuleType_Object=MibTableColumn
sysHwModuleType=_SysHwModuleType_Object((1,3,6,1,4,1,52,2501,1,1,2,1,2),_SysHwModuleType_Type())
sysHwModuleType.setMaxAccess(_C)
if mibBuilder.loadTexts:sysHwModuleType.setStatus(_B)
class _SysHwModuleDesc_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SysHwModuleDesc_Type.__name__=_V
_SysHwModuleDesc_Object=MibTableColumn
sysHwModuleDesc=_SysHwModuleDesc_Object((1,3,6,1,4,1,52,2501,1,1,2,1,3),_SysHwModuleDesc_Type())
sysHwModuleDesc.setMaxAccess(_C)
if mibBuilder.loadTexts:sysHwModuleDesc.setStatus(_B)
class _SysHwModuleNumPorts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_SysHwModuleNumPorts_Type.__name__=_E
_SysHwModuleNumPorts_Object=MibTableColumn
sysHwModuleNumPorts=_SysHwModuleNumPorts_Object((1,3,6,1,4,1,52,2501,1,1,2,1,4),_SysHwModuleNumPorts_Type())
sysHwModuleNumPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:sysHwModuleNumPorts.setStatus(_B)
class _SysHwModuleVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_SysHwModuleVersion_Type.__name__=_V
_SysHwModuleVersion_Object=MibTableColumn
sysHwModuleVersion=_SysHwModuleVersion_Object((1,3,6,1,4,1,52,2501,1,1,2,1,5),_SysHwModuleVersion_Type())
sysHwModuleVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:sysHwModuleVersion.setStatus(_B)
_SysHwModuleMemory_Type=SSRmemorySize
_SysHwModuleMemory_Object=MibTableColumn
sysHwModuleMemory=_SysHwModuleMemory_Object((1,3,6,1,4,1,52,2501,1,1,2,1,6),_SysHwModuleMemory_Type())
sysHwModuleMemory.setMaxAccess(_C)
if mibBuilder.loadTexts:sysHwModuleMemory.setStatus(_B)
_SysHwModuleService_Type=SSRserviceType
_SysHwModuleService_Object=MibTableColumn
sysHwModuleService=_SysHwModuleService_Object((1,3,6,1,4,1,52,2501,1,1,2,1,8),_SysHwModuleService_Type())
sysHwModuleService.setMaxAccess(_C)
if mibBuilder.loadTexts:sysHwModuleService.setStatus(_B)
_SysHwModuleStatus_Type=SSRModuleStatus
_SysHwModuleStatus_Object=MibTableColumn
sysHwModuleStatus=_SysHwModuleStatus_Object((1,3,6,1,4,1,52,2501,1,1,2,1,9),_SysHwModuleStatus_Type())
sysHwModuleStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sysHwModuleStatus.setStatus(_B)
_SysHwPortTable_Object=MibTable
sysHwPortTable=_SysHwPortTable_Object((1,3,6,1,4,1,52,2501,1,1,3))
if mibBuilder.loadTexts:sysHwPortTable.setStatus(_B)
_SysHwPortEntry_Object=MibTableRow
sysHwPortEntry=_SysHwPortEntry_Object((1,3,6,1,4,1,52,2501,1,1,3,1))
sysHwPortEntry.setIndexNames((0,_A,_H),(0,_A,_I))
if mibBuilder.loadTexts:sysHwPortEntry.setStatus(_B)
class _SysHwPortSlotNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SysHwPortSlotNumber_Type.__name__=_E
_SysHwPortSlotNumber_Object=MibTableColumn
sysHwPortSlotNumber=_SysHwPortSlotNumber_Object((1,3,6,1,4,1,52,2501,1,1,3,1,1),_SysHwPortSlotNumber_Type())
sysHwPortSlotNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:sysHwPortSlotNumber.setStatus(_B)
class _SysHwPortNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SysHwPortNumber_Type.__name__=_E
_SysHwPortNumber_Object=MibTableColumn
sysHwPortNumber=_SysHwPortNumber_Object((1,3,6,1,4,1,52,2501,1,1,3,1,2),_SysHwPortNumber_Type())
sysHwPortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:sysHwPortNumber.setStatus(_B)
_SysHwPortType_Type=SSRPortType
_SysHwPortType_Object=MibTableColumn
sysHwPortType=_SysHwPortType_Object((1,3,6,1,4,1,52,2501,1,1,3,1,3),_SysHwPortType_Type())
sysHwPortType.setMaxAccess(_C)
if mibBuilder.loadTexts:sysHwPortType.setStatus(_B)
_SysHwPortConnectorType_Type=SSRPortConnectorType
_SysHwPortConnectorType_Object=MibTableColumn
sysHwPortConnectorType=_SysHwPortConnectorType_Object((1,3,6,1,4,1,52,2501,1,1,3,1,4),_SysHwPortConnectorType_Type())
sysHwPortConnectorType.setMaxAccess(_C)
if mibBuilder.loadTexts:sysHwPortConnectorType.setStatus(_B)
_SysHwPortIfIndex_Type=SSRInterfaceIndex
_SysHwPortIfIndex_Object=MibTableColumn
sysHwPortIfIndex=_SysHwPortIfIndex_Object((1,3,6,1,4,1,52,2501,1,1,3,1,5),_SysHwPortIfIndex_Type())
sysHwPortIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:sysHwPortIfIndex.setStatus(_B)
_SysHwPowerSupply_Type=PowerSupplyBits
_SysHwPowerSupply_Object=MibScalar
sysHwPowerSupply=_SysHwPowerSupply_Object((1,3,6,1,4,1,52,2501,1,1,4),_SysHwPowerSupply_Type())
sysHwPowerSupply.setMaxAccess(_C)
if mibBuilder.loadTexts:sysHwPowerSupply.setStatus(_B)
class _SysHwFan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('working',1),('notWorking',2),(_F,3)))
_SysHwFan_Type.__name__=_E
_SysHwFan_Object=MibScalar
sysHwFan=_SysHwFan_Object((1,3,6,1,4,1,52,2501,1,1,5),_SysHwFan_Type())
sysHwFan.setMaxAccess(_C)
if mibBuilder.loadTexts:sysHwFan.setStatus(_B)
class _SysHwTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('normal',1),('outOfRange',2),(_F,3)))
_SysHwTemperature_Type.__name__=_E
_SysHwTemperature_Object=MibScalar
sysHwTemperature=_SysHwTemperature_Object((1,3,6,1,4,1,52,2501,1,1,6),_SysHwTemperature_Type())
sysHwTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:sysHwTemperature.setStatus(_B)
class _SysHwChassisId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SysHwChassisId_Type.__name__=_V
_SysHwChassisId_Object=MibScalar
sysHwChassisId=_SysHwChassisId_Object((1,3,6,1,4,1,52,2501,1,1,7),_SysHwChassisId_Type())
sysHwChassisId.setMaxAccess(_C)
if mibBuilder.loadTexts:sysHwChassisId.setStatus(_B)
_SysHwTotalInOctets_Type=Counter64
_SysHwTotalInOctets_Object=MibScalar
sysHwTotalInOctets=_SysHwTotalInOctets_Object((1,3,6,1,4,1,52,2501,1,1,10),_SysHwTotalInOctets_Type())
sysHwTotalInOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:sysHwTotalInOctets.setStatus(_D)
_SysHwTotalOutOctets_Type=Counter64
_SysHwTotalOutOctets_Object=MibScalar
sysHwTotalOutOctets=_SysHwTotalOutOctets_Object((1,3,6,1,4,1,52,2501,1,1,11),_SysHwTotalOutOctets_Type())
sysHwTotalOutOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:sysHwTotalOutOctets.setStatus(_D)
_SysHwTotalInFrames_Type=Counter64
_SysHwTotalInFrames_Object=MibScalar
sysHwTotalInFrames=_SysHwTotalInFrames_Object((1,3,6,1,4,1,52,2501,1,1,12),_SysHwTotalInFrames_Type())
sysHwTotalInFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:sysHwTotalInFrames.setStatus(_D)
_SysHwTotalOutFrames_Type=Counter64
_SysHwTotalOutFrames_Object=MibScalar
sysHwTotalOutFrames=_SysHwTotalOutFrames_Object((1,3,6,1,4,1,52,2501,1,1,13),_SysHwTotalOutFrames_Type())
sysHwTotalOutFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:sysHwTotalOutFrames.setStatus(_D)
_SysHwTotalL2SwitchedFrames_Type=Counter64
_SysHwTotalL2SwitchedFrames_Object=MibScalar
sysHwTotalL2SwitchedFrames=_SysHwTotalL2SwitchedFrames_Object((1,3,6,1,4,1,52,2501,1,1,14),_SysHwTotalL2SwitchedFrames_Type())
sysHwTotalL2SwitchedFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:sysHwTotalL2SwitchedFrames.setStatus(_D)
_SysHwTotalL3SwitchedFrames_Type=Counter64
_SysHwTotalL3SwitchedFrames_Object=MibScalar
sysHwTotalL3SwitchedFrames=_SysHwTotalL3SwitchedFrames_Object((1,3,6,1,4,1,52,2501,1,1,15),_SysHwTotalL3SwitchedFrames_Type())
sysHwTotalL3SwitchedFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:sysHwTotalL3SwitchedFrames.setStatus(_D)
_SysHwSwitchingFabric_Type=SSRSwitchingFabricInfo
_SysHwSwitchingFabric_Object=MibScalar
sysHwSwitchingFabric=_SysHwSwitchingFabric_Object((1,3,6,1,4,1,52,2501,1,1,19),_SysHwSwitchingFabric_Type())
sysHwSwitchingFabric.setMaxAccess(_C)
if mibBuilder.loadTexts:sysHwSwitchingFabric.setStatus(_B)
_SysHwControlModuleLED_Type=SSRCmLedState
_SysHwControlModuleLED_Object=MibScalar
sysHwControlModuleLED=_SysHwControlModuleLED_Object((1,3,6,1,4,1,52,2501,1,1,20),_SysHwControlModuleLED_Type())
sysHwControlModuleLED.setMaxAccess(_C)
if mibBuilder.loadTexts:sysHwControlModuleLED.setStatus(_B)
_SysHwControlModuleBackupState_Type=SSRBackupCMState
_SysHwControlModuleBackupState_Object=MibScalar
sysHwControlModuleBackupState=_SysHwControlModuleBackupState_Object((1,3,6,1,4,1,52,2501,1,1,21),_SysHwControlModuleBackupState_Type())
sysHwControlModuleBackupState.setMaxAccess(_C)
if mibBuilder.loadTexts:sysHwControlModuleBackupState.setStatus(_B)
_SysHwLastHotSwapEvent_Type=TimeTicks
_SysHwLastHotSwapEvent_Object=MibScalar
sysHwLastHotSwapEvent=_SysHwLastHotSwapEvent_Object((1,3,6,1,4,1,52,2501,1,1,22),_SysHwLastHotSwapEvent_Type())
sysHwLastHotSwapEvent.setMaxAccess(_C)
if mibBuilder.loadTexts:sysHwLastHotSwapEvent.setStatus(_B)
_HwConformance_ObjectIdentity=ObjectIdentity
hwConformance=_HwConformance_ObjectIdentity((1,3,6,1,4,1,52,2501,1,200,2))
_HwCompliances_ObjectIdentity=ObjectIdentity
hwCompliances=_HwCompliances_ObjectIdentity((1,3,6,1,4,1,52,2501,1,200,2,1))
_HwGroups_ObjectIdentity=ObjectIdentity
hwGroups=_HwGroups_ObjectIdentity((1,3,6,1,4,1,52,2501,1,200,2,2))
hwConfGroupV10=ObjectGroup((1,3,6,1,4,1,52,2501,1,200,2,2,1))
hwConfGroupV10.setObjects(*((_A,_J),(_A,_G),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_H),(_A,_I),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i)))
if mibBuilder.loadTexts:hwConfGroupV10.setStatus(_D)
hwConfGroupV11=ObjectGroup((1,3,6,1,4,1,52,2501,1,200,2,2,2))
hwConfGroupV11.setObjects(*((_A,_J),(_A,_G),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_W),(_A,_X),(_A,_H),(_A,_I),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:hwConfGroupV11.setStatus(_D)
hwConfGroupV12=ObjectGroup((1,3,6,1,4,1,52,2501,1,200,2,2,3))
hwConfGroupV12.setObjects(*((_A,_J),(_A,_G),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_W),(_A,_X),(_A,_b),(_A,_H),(_A,_I),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:hwConfGroupV12.setStatus(_D)
hwConfGroupV30=ObjectGroup((1,3,6,1,4,1,52,2501,1,200,2,2,4))
hwConfGroupV30.setObjects(*((_A,_J),(_A,_G),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_W),(_A,_X),(_A,_b),(_A,_H),(_A,_I),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_Y),(_A,_Z),(_A,_j),(_A,_k)))
if mibBuilder.loadTexts:hwConfGroupV30.setStatus(_B)
hwComplianceV10=ModuleCompliance((1,3,6,1,4,1,52,2501,1,200,2,2,1,1))
hwComplianceV10.setObjects((_A,_l))
if mibBuilder.loadTexts:hwComplianceV10.setStatus(_D)
hwComplianceV11=ModuleCompliance((1,3,6,1,4,1,52,2501,1,200,2,2,2,2))
hwComplianceV11.setObjects((_A,_c))
if mibBuilder.loadTexts:hwComplianceV11.setStatus(_D)
hwComplianceV12=ModuleCompliance((1,3,6,1,4,1,52,2501,1,200,2,2,2,3))
hwComplianceV12.setObjects((_A,_c))
if mibBuilder.loadTexts:hwComplianceV12.setStatus(_D)
hwComplianceV30=ModuleCompliance((1,3,6,1,4,1,52,2501,1,200,2,2,2,4))
hwComplianceV30.setObjects((_A,_m))
if mibBuilder.loadTexts:hwComplianceV30.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'SSRInterfaceIndex':SSRInterfaceIndex,'SSRModuleType':SSRModuleType,'SSRModuleStatus':SSRModuleStatus,'SSRPortType':SSRPortType,'SSRPortConnectorType':SSRPortConnectorType,'SSRserviceType':SSRserviceType,'SSRmemorySize':SSRmemorySize,'SSRSwitchingFabricInfo':SSRSwitchingFabricInfo,'SSRCmLedState':SSRCmLedState,'SSRBackupCMState':SSRBackupCMState,'PowerSupplyBits':PowerSupplyBits,'sysHwGroup':sysHwGroup,_J:sysHwNumSlots,'sysHwModuleTable':sysHwModuleTable,'sysHwModuleEntry':sysHwModuleEntry,_G:sysHwModuleSlotNumber,_K:sysHwModuleType,_L:sysHwModuleDesc,_M:sysHwModuleNumPorts,_N:sysHwModuleVersion,_W:sysHwModuleMemory,_X:sysHwModuleService,_b:sysHwModuleStatus,'sysHwPortTable':sysHwPortTable,'sysHwPortEntry':sysHwPortEntry,_H:sysHwPortSlotNumber,_I:sysHwPortNumber,_O:sysHwPortType,_P:sysHwPortConnectorType,_Q:sysHwPortIfIndex,_R:sysHwPowerSupply,_S:sysHwFan,_T:sysHwTemperature,_U:sysHwChassisId,_d:sysHwTotalInOctets,_e:sysHwTotalOutOctets,_f:sysHwTotalInFrames,_g:sysHwTotalOutFrames,_h:sysHwTotalL2SwitchedFrames,_i:sysHwTotalL3SwitchedFrames,_Y:sysHwSwitchingFabric,_Z:sysHwControlModuleLED,_j:sysHwControlModuleBackupState,_k:sysHwLastHotSwapEvent,'hardwareMIB':hardwareMIB,'hwConformance':hwConformance,'hwCompliances':hwCompliances,'hwGroups':hwGroups,_l:hwConfGroupV10,'hwComplianceV10':hwComplianceV10,_c:hwConfGroupV11,'hwComplianceV11':hwComplianceV11,'hwComplianceV12':hwComplianceV12,'hwComplianceV30':hwComplianceV30,'hwConfGroupV12':hwConfGroupV12,_m:hwConfGroupV30})