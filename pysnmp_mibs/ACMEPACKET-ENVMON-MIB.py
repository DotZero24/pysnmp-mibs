_AE='apEnvMonPortChangeNotification'
_AD='apEnvMonVoltageChangeNotification'
_AC='apEnvMonI2CFailNotification'
_AB='apEnvMonStatusChangeNotification'
_AA='apEnvMonTrapPortID'
_A9='apEnvMonTrapPresence'
_A8='apEnvMonTrapPortType'
_A7='apEnvMonTrapInstance'
_A6='apEnvMonCpuCoreRamUsage'
_A5='apEnvMonCpuCoreRamDescr'
_A4='apEnvMonCpuCoreState'
_A3='apEnvMonCpuCoreUsage'
_A2='apEnvMonCpuCoreDescr'
_A1='apEnvMonCardRedundancy'
_A0='apEnvMonCardState'
_z='apEnvMonCardHealthScore'
_y='apEnvMonCardDescr'
_x='apEnvMonCardType'
_w='apEnvMonFanSlotID'
_v='apEnvMonTemperatureSlotType'
_u='apEnvMonTemperatureSlotID'
_t='apEnvMonVoltageSlotType'
_s='apEnvMonVoltageSlotID'
_r='apEnvMonEnableStatChangeNotif'
_q='apEnvMonPhyCardState'
_p='apEnvMonPhyCardStatusDescr'
_o='apEnvMonPhyCardStatusType'
_n='apEnvMonPowerSupplyState'
_m='apEnvMonPowerSupplyStatusDescr'
_l='apEnvMonPowerSupplyStatusType'
_k='apEnvMonFanState'
_j='apEnvMonFanStatusValue'
_i='apEnvMonFanStatusDescr'
_h='apEnvMonFanStatusType'
_g='apEnvMonTemperatureState'
_f='apEnvMonTemperatureStatusValue'
_e='apEnvMonTemperatureStatusDescr'
_d='apEnvMonTemperatureStatusType'
_c='apEnvMonVoltageState'
_b='apEnvMonVoltageStatusValue'
_a='apEnvMonVoltageStatusDescr'
_Z='apEnvMonVoltageStatusType'
_Y='apEnvMonI2CState'
_X='apEnvMonPhyCardStatusIndex'
_W='apEnvMonPowerSupplyStatusIndex'
_V='apEnvMonFanStatusIndex'
_U='apEnvMonTemperatureStatusIndex'
_T='apEnvMonVoltageStatusIndex'
_S='apEnvMonTempChangeNotification'
_R='apEnvMonTrapSlotType'
_Q='apEnvMonCpuCoreIndex'
_P='slot'
_O='right'
_N='left'
_M='unknown'
_L='apEnvMonTrapSlotID'
_K='apEnvMonTrapCurrentState'
_J='apEnvMonTrapPreviousState'
_I='apEnvMonCardSlot'
_H='not-accessible'
_G='deprecated'
_F='DisplayString'
_E='accessible-for-notify'
_D='Integer32'
_C='read-only'
_B='ACMEPACKET-ENVMON-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
acmepacketMgmt,=mibBuilder.importSymbols('ACMEPACKET-SMI','acmepacketMgmt')
ApHardwareModuleFamily,ApPhyPortType,ApPresence,ApRedundancyState=mibBuilder.importSymbols('ACMEPACKET-TC','ApHardwareModuleFamily','ApPhyPortType','ApPresence','ApRedundancyState')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention','TruthValue')
apEnvMonModule=ModuleIdentity((1,3,6,1,4,1,9148,3,3))
if mibBuilder.loadTexts:apEnvMonModule.setRevisions(('2012-07-16 00:00',))
class ApEnvMonState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('initial',1),('normal',2),('minor',3),('major',4),('critical',5),('shutdown',6),('notPresent',7),('notFunctioning',8),(_M,9)))
_ApEnvMonObjects_ObjectIdentity=ObjectIdentity
apEnvMonObjects=_ApEnvMonObjects_ObjectIdentity((1,3,6,1,4,1,9148,3,3,1))
_ApEnvMonI2CState_Type=ApEnvMonState
_ApEnvMonI2CState_Object=MibScalar
apEnvMonI2CState=_ApEnvMonI2CState_Object((1,3,6,1,4,1,9148,3,3,1,1),_ApEnvMonI2CState_Type())
apEnvMonI2CState.setMaxAccess(_C)
if mibBuilder.loadTexts:apEnvMonI2CState.setStatus(_A)
_ApEnvMonVoltageObjects_ObjectIdentity=ObjectIdentity
apEnvMonVoltageObjects=_ApEnvMonVoltageObjects_ObjectIdentity((1,3,6,1,4,1,9148,3,3,1,2))
_ApEnvMonVoltageStatusTable_Object=MibTable
apEnvMonVoltageStatusTable=_ApEnvMonVoltageStatusTable_Object((1,3,6,1,4,1,9148,3,3,1,2,1))
if mibBuilder.loadTexts:apEnvMonVoltageStatusTable.setStatus(_A)
_ApEnvMonVoltageStatusEntry_Object=MibTableRow
apEnvMonVoltageStatusEntry=_ApEnvMonVoltageStatusEntry_Object((1,3,6,1,4,1,9148,3,3,1,2,1,1))
apEnvMonVoltageStatusEntry.setIndexNames((0,_B,_T))
if mibBuilder.loadTexts:apEnvMonVoltageStatusEntry.setStatus(_A)
class _ApEnvMonVoltageStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ApEnvMonVoltageStatusIndex_Type.__name__=_D
_ApEnvMonVoltageStatusIndex_Object=MibTableColumn
apEnvMonVoltageStatusIndex=_ApEnvMonVoltageStatusIndex_Object((1,3,6,1,4,1,9148,3,3,1,2,1,1,1),_ApEnvMonVoltageStatusIndex_Type())
apEnvMonVoltageStatusIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:apEnvMonVoltageStatusIndex.setStatus(_A)
class _ApEnvMonVoltageStatusType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*((_M,0),('v2p5',1),('v3p3',2),('v5',3),('cpu',4),('v1',5),('v1p1',6),('v1p15',7),('v1p2',8),('v1p212',9),('v1p25',10),('v1p3',11),('v1p5',12),('v1p8',13),('v2p6',14),('v3p3aux',15)))
_ApEnvMonVoltageStatusType_Type.__name__=_D
_ApEnvMonVoltageStatusType_Object=MibTableColumn
apEnvMonVoltageStatusType=_ApEnvMonVoltageStatusType_Object((1,3,6,1,4,1,9148,3,3,1,2,1,1,2),_ApEnvMonVoltageStatusType_Type())
apEnvMonVoltageStatusType.setMaxAccess(_C)
if mibBuilder.loadTexts:apEnvMonVoltageStatusType.setStatus(_A)
class _ApEnvMonVoltageStatusDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ApEnvMonVoltageStatusDescr_Type.__name__=_F
_ApEnvMonVoltageStatusDescr_Object=MibTableColumn
apEnvMonVoltageStatusDescr=_ApEnvMonVoltageStatusDescr_Object((1,3,6,1,4,1,9148,3,3,1,2,1,1,3),_ApEnvMonVoltageStatusDescr_Type())
apEnvMonVoltageStatusDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:apEnvMonVoltageStatusDescr.setStatus(_A)
_ApEnvMonVoltageStatusValue_Type=Integer32
_ApEnvMonVoltageStatusValue_Object=MibTableColumn
apEnvMonVoltageStatusValue=_ApEnvMonVoltageStatusValue_Object((1,3,6,1,4,1,9148,3,3,1,2,1,1,4),_ApEnvMonVoltageStatusValue_Type())
apEnvMonVoltageStatusValue.setMaxAccess(_C)
if mibBuilder.loadTexts:apEnvMonVoltageStatusValue.setStatus(_A)
if mibBuilder.loadTexts:apEnvMonVoltageStatusValue.setUnits('millivolts')
_ApEnvMonVoltageState_Type=ApEnvMonState
_ApEnvMonVoltageState_Object=MibTableColumn
apEnvMonVoltageState=_ApEnvMonVoltageState_Object((1,3,6,1,4,1,9148,3,3,1,2,1,1,5),_ApEnvMonVoltageState_Type())
apEnvMonVoltageState.setMaxAccess(_C)
if mibBuilder.loadTexts:apEnvMonVoltageState.setStatus(_A)
_ApEnvMonVoltageSlotID_Type=Integer32
_ApEnvMonVoltageSlotID_Object=MibTableColumn
apEnvMonVoltageSlotID=_ApEnvMonVoltageSlotID_Object((1,3,6,1,4,1,9148,3,3,1,2,1,1,6),_ApEnvMonVoltageSlotID_Type())
apEnvMonVoltageSlotID.setMaxAccess(_C)
if mibBuilder.loadTexts:apEnvMonVoltageSlotID.setStatus(_A)
_ApEnvMonVoltageSlotType_Type=ApHardwareModuleFamily
_ApEnvMonVoltageSlotType_Object=MibTableColumn
apEnvMonVoltageSlotType=_ApEnvMonVoltageSlotType_Object((1,3,6,1,4,1,9148,3,3,1,2,1,1,7),_ApEnvMonVoltageSlotType_Type())
apEnvMonVoltageSlotType.setMaxAccess(_C)
if mibBuilder.loadTexts:apEnvMonVoltageSlotType.setStatus(_A)
_ApEnvMonTemperatureObjects_ObjectIdentity=ObjectIdentity
apEnvMonTemperatureObjects=_ApEnvMonTemperatureObjects_ObjectIdentity((1,3,6,1,4,1,9148,3,3,1,3))
_ApEnvMonTemperatureStatusTable_Object=MibTable
apEnvMonTemperatureStatusTable=_ApEnvMonTemperatureStatusTable_Object((1,3,6,1,4,1,9148,3,3,1,3,1))
if mibBuilder.loadTexts:apEnvMonTemperatureStatusTable.setStatus(_A)
_ApEnvMonTemperatureStatusEntry_Object=MibTableRow
apEnvMonTemperatureStatusEntry=_ApEnvMonTemperatureStatusEntry_Object((1,3,6,1,4,1,9148,3,3,1,3,1,1))
apEnvMonTemperatureStatusEntry.setIndexNames((0,_B,_U))
if mibBuilder.loadTexts:apEnvMonTemperatureStatusEntry.setStatus(_A)
class _ApEnvMonTemperatureStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ApEnvMonTemperatureStatusIndex_Type.__name__=_D
_ApEnvMonTemperatureStatusIndex_Object=MibTableColumn
apEnvMonTemperatureStatusIndex=_ApEnvMonTemperatureStatusIndex_Object((1,3,6,1,4,1,9148,3,3,1,3,1,1,1),_ApEnvMonTemperatureStatusIndex_Type())
apEnvMonTemperatureStatusIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:apEnvMonTemperatureStatusIndex.setStatus(_A)
class _ApEnvMonTemperatureStatusType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('ds1624sMain',1),('ds1624sCPU',2),('lm84',3),('lm75',4),('lm75Main',5),('lm75Cpu',6),('lm75Phy',7)))
_ApEnvMonTemperatureStatusType_Type.__name__=_D
_ApEnvMonTemperatureStatusType_Object=MibTableColumn
apEnvMonTemperatureStatusType=_ApEnvMonTemperatureStatusType_Object((1,3,6,1,4,1,9148,3,3,1,3,1,1,2),_ApEnvMonTemperatureStatusType_Type())
apEnvMonTemperatureStatusType.setMaxAccess(_C)
if mibBuilder.loadTexts:apEnvMonTemperatureStatusType.setStatus(_A)
class _ApEnvMonTemperatureStatusDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ApEnvMonTemperatureStatusDescr_Type.__name__=_F
_ApEnvMonTemperatureStatusDescr_Object=MibTableColumn
apEnvMonTemperatureStatusDescr=_ApEnvMonTemperatureStatusDescr_Object((1,3,6,1,4,1,9148,3,3,1,3,1,1,3),_ApEnvMonTemperatureStatusDescr_Type())
apEnvMonTemperatureStatusDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:apEnvMonTemperatureStatusDescr.setStatus(_A)
_ApEnvMonTemperatureStatusValue_Type=Integer32
_ApEnvMonTemperatureStatusValue_Object=MibTableColumn
apEnvMonTemperatureStatusValue=_ApEnvMonTemperatureStatusValue_Object((1,3,6,1,4,1,9148,3,3,1,3,1,1,4),_ApEnvMonTemperatureStatusValue_Type())
apEnvMonTemperatureStatusValue.setMaxAccess(_C)
if mibBuilder.loadTexts:apEnvMonTemperatureStatusValue.setStatus(_A)
if mibBuilder.loadTexts:apEnvMonTemperatureStatusValue.setUnits('degrees Celsius')
_ApEnvMonTemperatureState_Type=ApEnvMonState
_ApEnvMonTemperatureState_Object=MibTableColumn
apEnvMonTemperatureState=_ApEnvMonTemperatureState_Object((1,3,6,1,4,1,9148,3,3,1,3,1,1,5),_ApEnvMonTemperatureState_Type())
apEnvMonTemperatureState.setMaxAccess(_C)
if mibBuilder.loadTexts:apEnvMonTemperatureState.setStatus(_A)
_ApEnvMonTemperatureSlotID_Type=Integer32
_ApEnvMonTemperatureSlotID_Object=MibTableColumn
apEnvMonTemperatureSlotID=_ApEnvMonTemperatureSlotID_Object((1,3,6,1,4,1,9148,3,3,1,3,1,1,6),_ApEnvMonTemperatureSlotID_Type())
apEnvMonTemperatureSlotID.setMaxAccess(_C)
if mibBuilder.loadTexts:apEnvMonTemperatureSlotID.setStatus(_A)
_ApEnvMonTemperatureSlotType_Type=ApHardwareModuleFamily
_ApEnvMonTemperatureSlotType_Object=MibTableColumn
apEnvMonTemperatureSlotType=_ApEnvMonTemperatureSlotType_Object((1,3,6,1,4,1,9148,3,3,1,3,1,1,7),_ApEnvMonTemperatureSlotType_Type())
apEnvMonTemperatureSlotType.setMaxAccess(_C)
if mibBuilder.loadTexts:apEnvMonTemperatureSlotType.setStatus(_A)
_ApEnvMonFanObjects_ObjectIdentity=ObjectIdentity
apEnvMonFanObjects=_ApEnvMonFanObjects_ObjectIdentity((1,3,6,1,4,1,9148,3,3,1,4))
_ApEnvMonFanStatusTable_Object=MibTable
apEnvMonFanStatusTable=_ApEnvMonFanStatusTable_Object((1,3,6,1,4,1,9148,3,3,1,4,1))
if mibBuilder.loadTexts:apEnvMonFanStatusTable.setStatus(_A)
_ApEnvMonFanStatusEntry_Object=MibTableRow
apEnvMonFanStatusEntry=_ApEnvMonFanStatusEntry_Object((1,3,6,1,4,1,9148,3,3,1,4,1,1))
apEnvMonFanStatusEntry.setIndexNames((0,_B,_V))
if mibBuilder.loadTexts:apEnvMonFanStatusEntry.setStatus(_A)
class _ApEnvMonFanStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ApEnvMonFanStatusIndex_Type.__name__=_D
_ApEnvMonFanStatusIndex_Object=MibTableColumn
apEnvMonFanStatusIndex=_ApEnvMonFanStatusIndex_Object((1,3,6,1,4,1,9148,3,3,1,4,1,1,1),_ApEnvMonFanStatusIndex_Type())
apEnvMonFanStatusIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:apEnvMonFanStatusIndex.setStatus(_A)
class _ApEnvMonFanStatusType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_N,0),('middle',1),(_O,2),(_P,3)))
_ApEnvMonFanStatusType_Type.__name__=_D
_ApEnvMonFanStatusType_Object=MibTableColumn
apEnvMonFanStatusType=_ApEnvMonFanStatusType_Object((1,3,6,1,4,1,9148,3,3,1,4,1,1,2),_ApEnvMonFanStatusType_Type())
apEnvMonFanStatusType.setMaxAccess(_C)
if mibBuilder.loadTexts:apEnvMonFanStatusType.setStatus(_A)
class _ApEnvMonFanStatusDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ApEnvMonFanStatusDescr_Type.__name__=_F
_ApEnvMonFanStatusDescr_Object=MibTableColumn
apEnvMonFanStatusDescr=_ApEnvMonFanStatusDescr_Object((1,3,6,1,4,1,9148,3,3,1,4,1,1,3),_ApEnvMonFanStatusDescr_Type())
apEnvMonFanStatusDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:apEnvMonFanStatusDescr.setStatus(_A)
_ApEnvMonFanStatusValue_Type=Gauge32
_ApEnvMonFanStatusValue_Object=MibTableColumn
apEnvMonFanStatusValue=_ApEnvMonFanStatusValue_Object((1,3,6,1,4,1,9148,3,3,1,4,1,1,4),_ApEnvMonFanStatusValue_Type())
apEnvMonFanStatusValue.setMaxAccess(_C)
if mibBuilder.loadTexts:apEnvMonFanStatusValue.setStatus(_A)
if mibBuilder.loadTexts:apEnvMonFanStatusValue.setUnits('%')
_ApEnvMonFanState_Type=ApEnvMonState
_ApEnvMonFanState_Object=MibTableColumn
apEnvMonFanState=_ApEnvMonFanState_Object((1,3,6,1,4,1,9148,3,3,1,4,1,1,5),_ApEnvMonFanState_Type())
apEnvMonFanState.setMaxAccess(_C)
if mibBuilder.loadTexts:apEnvMonFanState.setStatus(_A)
_ApEnvMonFanSlotID_Type=Integer32
_ApEnvMonFanSlotID_Object=MibTableColumn
apEnvMonFanSlotID=_ApEnvMonFanSlotID_Object((1,3,6,1,4,1,9148,3,3,1,4,1,1,6),_ApEnvMonFanSlotID_Type())
apEnvMonFanSlotID.setMaxAccess(_C)
if mibBuilder.loadTexts:apEnvMonFanSlotID.setStatus(_A)
_ApEnvMonPowerSupplyObjects_ObjectIdentity=ObjectIdentity
apEnvMonPowerSupplyObjects=_ApEnvMonPowerSupplyObjects_ObjectIdentity((1,3,6,1,4,1,9148,3,3,1,5))
_ApEnvMonPowerSupplyStatusTable_Object=MibTable
apEnvMonPowerSupplyStatusTable=_ApEnvMonPowerSupplyStatusTable_Object((1,3,6,1,4,1,9148,3,3,1,5,1))
if mibBuilder.loadTexts:apEnvMonPowerSupplyStatusTable.setStatus(_A)
_ApEnvMonPowerSupplyStatusEntry_Object=MibTableRow
apEnvMonPowerSupplyStatusEntry=_ApEnvMonPowerSupplyStatusEntry_Object((1,3,6,1,4,1,9148,3,3,1,5,1,1))
apEnvMonPowerSupplyStatusEntry.setIndexNames((0,_B,_W))
if mibBuilder.loadTexts:apEnvMonPowerSupplyStatusEntry.setStatus(_A)
class _ApEnvMonPowerSupplyStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ApEnvMonPowerSupplyStatusIndex_Type.__name__=_D
_ApEnvMonPowerSupplyStatusIndex_Object=MibTableColumn
apEnvMonPowerSupplyStatusIndex=_ApEnvMonPowerSupplyStatusIndex_Object((1,3,6,1,4,1,9148,3,3,1,5,1,1,1),_ApEnvMonPowerSupplyStatusIndex_Type())
apEnvMonPowerSupplyStatusIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:apEnvMonPowerSupplyStatusIndex.setStatus(_A)
class _ApEnvMonPowerSupplyStatusType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,3)));namedValues=NamedValues(*((_N,0),(_O,1),(_P,3)))
_ApEnvMonPowerSupplyStatusType_Type.__name__=_D
_ApEnvMonPowerSupplyStatusType_Object=MibTableColumn
apEnvMonPowerSupplyStatusType=_ApEnvMonPowerSupplyStatusType_Object((1,3,6,1,4,1,9148,3,3,1,5,1,1,2),_ApEnvMonPowerSupplyStatusType_Type())
apEnvMonPowerSupplyStatusType.setMaxAccess(_C)
if mibBuilder.loadTexts:apEnvMonPowerSupplyStatusType.setStatus(_A)
class _ApEnvMonPowerSupplyStatusDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ApEnvMonPowerSupplyStatusDescr_Type.__name__=_F
_ApEnvMonPowerSupplyStatusDescr_Object=MibTableColumn
apEnvMonPowerSupplyStatusDescr=_ApEnvMonPowerSupplyStatusDescr_Object((1,3,6,1,4,1,9148,3,3,1,5,1,1,3),_ApEnvMonPowerSupplyStatusDescr_Type())
apEnvMonPowerSupplyStatusDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:apEnvMonPowerSupplyStatusDescr.setStatus(_A)
_ApEnvMonPowerSupplyState_Type=ApEnvMonState
_ApEnvMonPowerSupplyState_Object=MibTableColumn
apEnvMonPowerSupplyState=_ApEnvMonPowerSupplyState_Object((1,3,6,1,4,1,9148,3,3,1,5,1,1,4),_ApEnvMonPowerSupplyState_Type())
apEnvMonPowerSupplyState.setMaxAccess(_C)
if mibBuilder.loadTexts:apEnvMonPowerSupplyState.setStatus(_A)
_ApEnvMonPhyCardObjects_ObjectIdentity=ObjectIdentity
apEnvMonPhyCardObjects=_ApEnvMonPhyCardObjects_ObjectIdentity((1,3,6,1,4,1,9148,3,3,1,6))
_ApEnvMonPhyCardStatusTable_Object=MibTable
apEnvMonPhyCardStatusTable=_ApEnvMonPhyCardStatusTable_Object((1,3,6,1,4,1,9148,3,3,1,6,1))
if mibBuilder.loadTexts:apEnvMonPhyCardStatusTable.setStatus(_G)
_ApEnvMonPhyCardStatusEntry_Object=MibTableRow
apEnvMonPhyCardStatusEntry=_ApEnvMonPhyCardStatusEntry_Object((1,3,6,1,4,1,9148,3,3,1,6,1,1))
apEnvMonPhyCardStatusEntry.setIndexNames((0,_B,_X))
if mibBuilder.loadTexts:apEnvMonPhyCardStatusEntry.setStatus(_G)
class _ApEnvMonPhyCardStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ApEnvMonPhyCardStatusIndex_Type.__name__=_D
_ApEnvMonPhyCardStatusIndex_Object=MibTableColumn
apEnvMonPhyCardStatusIndex=_ApEnvMonPhyCardStatusIndex_Object((1,3,6,1,4,1,9148,3,3,1,6,1,1,1),_ApEnvMonPhyCardStatusIndex_Type())
apEnvMonPhyCardStatusIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:apEnvMonPhyCardStatusIndex.setStatus(_G)
class _ApEnvMonPhyCardStatusType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,3)));namedValues=NamedValues(*((_N,0),(_O,1),(_P,3)))
_ApEnvMonPhyCardStatusType_Type.__name__=_D
_ApEnvMonPhyCardStatusType_Object=MibTableColumn
apEnvMonPhyCardStatusType=_ApEnvMonPhyCardStatusType_Object((1,3,6,1,4,1,9148,3,3,1,6,1,1,2),_ApEnvMonPhyCardStatusType_Type())
apEnvMonPhyCardStatusType.setMaxAccess(_C)
if mibBuilder.loadTexts:apEnvMonPhyCardStatusType.setStatus(_G)
class _ApEnvMonPhyCardStatusDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ApEnvMonPhyCardStatusDescr_Type.__name__=_F
_ApEnvMonPhyCardStatusDescr_Object=MibTableColumn
apEnvMonPhyCardStatusDescr=_ApEnvMonPhyCardStatusDescr_Object((1,3,6,1,4,1,9148,3,3,1,6,1,1,3),_ApEnvMonPhyCardStatusDescr_Type())
apEnvMonPhyCardStatusDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:apEnvMonPhyCardStatusDescr.setStatus(_G)
_ApEnvMonPhyCardState_Type=ApEnvMonState
_ApEnvMonPhyCardState_Object=MibTableColumn
apEnvMonPhyCardState=_ApEnvMonPhyCardState_Object((1,3,6,1,4,1,9148,3,3,1,6,1,1,4),_ApEnvMonPhyCardState_Type())
apEnvMonPhyCardState.setMaxAccess(_C)
if mibBuilder.loadTexts:apEnvMonPhyCardState.setStatus(_G)
_ApEnvMonCardObjects_ObjectIdentity=ObjectIdentity
apEnvMonCardObjects=_ApEnvMonCardObjects_ObjectIdentity((1,3,6,1,4,1,9148,3,3,1,7))
_ApEnvMonCardTable_Object=MibTable
apEnvMonCardTable=_ApEnvMonCardTable_Object((1,3,6,1,4,1,9148,3,3,1,7,1))
if mibBuilder.loadTexts:apEnvMonCardTable.setStatus(_A)
_ApEnvMonCardEntry_Object=MibTableRow
apEnvMonCardEntry=_ApEnvMonCardEntry_Object((1,3,6,1,4,1,9148,3,3,1,7,1,1))
apEnvMonCardEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:apEnvMonCardEntry.setStatus(_A)
_ApEnvMonCardSlot_Type=Integer32
_ApEnvMonCardSlot_Object=MibTableColumn
apEnvMonCardSlot=_ApEnvMonCardSlot_Object((1,3,6,1,4,1,9148,3,3,1,7,1,1,1),_ApEnvMonCardSlot_Type())
apEnvMonCardSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:apEnvMonCardSlot.setStatus(_A)
_ApEnvMonCardType_Type=ApHardwareModuleFamily
_ApEnvMonCardType_Object=MibTableColumn
apEnvMonCardType=_ApEnvMonCardType_Object((1,3,6,1,4,1,9148,3,3,1,7,1,1,2),_ApEnvMonCardType_Type())
apEnvMonCardType.setMaxAccess(_C)
if mibBuilder.loadTexts:apEnvMonCardType.setStatus(_A)
_ApEnvMonCardDescr_Type=DisplayString
_ApEnvMonCardDescr_Object=MibTableColumn
apEnvMonCardDescr=_ApEnvMonCardDescr_Object((1,3,6,1,4,1,9148,3,3,1,7,1,1,3),_ApEnvMonCardDescr_Type())
apEnvMonCardDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:apEnvMonCardDescr.setStatus(_A)
_ApEnvMonCardHealthScore_Type=Integer32
_ApEnvMonCardHealthScore_Object=MibTableColumn
apEnvMonCardHealthScore=_ApEnvMonCardHealthScore_Object((1,3,6,1,4,1,9148,3,3,1,7,1,1,4),_ApEnvMonCardHealthScore_Type())
apEnvMonCardHealthScore.setMaxAccess(_C)
if mibBuilder.loadTexts:apEnvMonCardHealthScore.setStatus(_A)
_ApEnvMonCardState_Type=ApEnvMonState
_ApEnvMonCardState_Object=MibTableColumn
apEnvMonCardState=_ApEnvMonCardState_Object((1,3,6,1,4,1,9148,3,3,1,7,1,1,5),_ApEnvMonCardState_Type())
apEnvMonCardState.setMaxAccess(_C)
if mibBuilder.loadTexts:apEnvMonCardState.setStatus(_A)
_ApEnvMonCardRedundancy_Type=ApRedundancyState
_ApEnvMonCardRedundancy_Object=MibTableColumn
apEnvMonCardRedundancy=_ApEnvMonCardRedundancy_Object((1,3,6,1,4,1,9148,3,3,1,7,1,1,6),_ApEnvMonCardRedundancy_Type())
apEnvMonCardRedundancy.setMaxAccess(_C)
if mibBuilder.loadTexts:apEnvMonCardRedundancy.setStatus(_A)
_ApEnvMonCpuCoreTable_Object=MibTable
apEnvMonCpuCoreTable=_ApEnvMonCpuCoreTable_Object((1,3,6,1,4,1,9148,3,3,1,7,2))
if mibBuilder.loadTexts:apEnvMonCpuCoreTable.setStatus(_A)
_ApEnvMonCpuCoreEntry_Object=MibTableRow
apEnvMonCpuCoreEntry=_ApEnvMonCpuCoreEntry_Object((1,3,6,1,4,1,9148,3,3,1,7,2,1))
apEnvMonCpuCoreEntry.setIndexNames((0,_B,_I),(0,_B,_Q))
if mibBuilder.loadTexts:apEnvMonCpuCoreEntry.setStatus(_A)
_ApEnvMonCpuCoreIndex_Type=Integer32
_ApEnvMonCpuCoreIndex_Object=MibTableColumn
apEnvMonCpuCoreIndex=_ApEnvMonCpuCoreIndex_Object((1,3,6,1,4,1,9148,3,3,1,7,2,1,1),_ApEnvMonCpuCoreIndex_Type())
apEnvMonCpuCoreIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:apEnvMonCpuCoreIndex.setStatus(_A)
_ApEnvMonCpuCoreDescr_Type=DisplayString
_ApEnvMonCpuCoreDescr_Object=MibTableColumn
apEnvMonCpuCoreDescr=_ApEnvMonCpuCoreDescr_Object((1,3,6,1,4,1,9148,3,3,1,7,2,1,2),_ApEnvMonCpuCoreDescr_Type())
apEnvMonCpuCoreDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:apEnvMonCpuCoreDescr.setStatus(_A)
_ApEnvMonCpuCoreUsage_Type=Gauge32
_ApEnvMonCpuCoreUsage_Object=MibTableColumn
apEnvMonCpuCoreUsage=_ApEnvMonCpuCoreUsage_Object((1,3,6,1,4,1,9148,3,3,1,7,2,1,3),_ApEnvMonCpuCoreUsage_Type())
apEnvMonCpuCoreUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:apEnvMonCpuCoreUsage.setStatus(_A)
if mibBuilder.loadTexts:apEnvMonCpuCoreUsage.setUnits('%')
class _ApEnvMonCpuCoreState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,101,102,201,202,203,204,205,206,207,208,209,401,402,403,404,405,406)));namedValues=NamedValues(*((_M,0),('present',1),('booting',2),('registered',3),('readywait',4),('ready',5),('bootTimeout',6),('registerTimeout',7),('manifestTimeout',8),('readyTimeout',9),('healthWait',101),('healthRcvd',102),('becomingActive',201),('becomingStandby',202),('becomingOOS',203),('active',204),('standby',205),('oos',206),('activeTimeout',207),('standbyTimeout',208),('oosTimeout',209),('resetting',401),('reset',402),('resetTimeout',403),('shuttingDown',404),('shutOff',405),('shutdownTimeout',406)))
_ApEnvMonCpuCoreState_Type.__name__=_D
_ApEnvMonCpuCoreState_Object=MibTableColumn
apEnvMonCpuCoreState=_ApEnvMonCpuCoreState_Object((1,3,6,1,4,1,9148,3,3,1,7,2,1,4),_ApEnvMonCpuCoreState_Type())
apEnvMonCpuCoreState.setMaxAccess(_C)
if mibBuilder.loadTexts:apEnvMonCpuCoreState.setStatus(_A)
_ApEnvMonCpuCoreRamDescr_Type=DisplayString
_ApEnvMonCpuCoreRamDescr_Object=MibTableColumn
apEnvMonCpuCoreRamDescr=_ApEnvMonCpuCoreRamDescr_Object((1,3,6,1,4,1,9148,3,3,1,7,2,1,5),_ApEnvMonCpuCoreRamDescr_Type())
apEnvMonCpuCoreRamDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:apEnvMonCpuCoreRamDescr.setStatus(_A)
_ApEnvMonCpuCoreRamUsage_Type=Gauge32
_ApEnvMonCpuCoreRamUsage_Object=MibTableColumn
apEnvMonCpuCoreRamUsage=_ApEnvMonCpuCoreRamUsage_Object((1,3,6,1,4,1,9148,3,3,1,7,2,1,6),_ApEnvMonCpuCoreRamUsage_Type())
apEnvMonCpuCoreRamUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:apEnvMonCpuCoreRamUsage.setStatus(_A)
if mibBuilder.loadTexts:apEnvMonCpuCoreRamUsage.setUnits('%')
_ApEnvMonMIBNotificationEnables_ObjectIdentity=ObjectIdentity
apEnvMonMIBNotificationEnables=_ApEnvMonMIBNotificationEnables_ObjectIdentity((1,3,6,1,4,1,9148,3,3,2))
_ApEnvMonEnableStatChangeNotif_Type=TruthValue
_ApEnvMonEnableStatChangeNotif_Object=MibScalar
apEnvMonEnableStatChangeNotif=_ApEnvMonEnableStatChangeNotif_Object((1,3,6,1,4,1,9148,3,3,2,1),_ApEnvMonEnableStatChangeNotif_Type())
apEnvMonEnableStatChangeNotif.setMaxAccess(_C)
if mibBuilder.loadTexts:apEnvMonEnableStatChangeNotif.setStatus(_A)
_ApEnvMonNotificationObjects_ObjectIdentity=ObjectIdentity
apEnvMonNotificationObjects=_ApEnvMonNotificationObjects_ObjectIdentity((1,3,6,1,4,1,9148,3,3,3))
_ApEnvMonTrapInstance_Type=ObjectIdentifier
_ApEnvMonTrapInstance_Object=MibScalar
apEnvMonTrapInstance=_ApEnvMonTrapInstance_Object((1,3,6,1,4,1,9148,3,3,3,1),_ApEnvMonTrapInstance_Type())
apEnvMonTrapInstance.setMaxAccess(_E)
if mibBuilder.loadTexts:apEnvMonTrapInstance.setStatus(_A)
_ApEnvMonTrapPreviousState_Type=ApEnvMonState
_ApEnvMonTrapPreviousState_Object=MibScalar
apEnvMonTrapPreviousState=_ApEnvMonTrapPreviousState_Object((1,3,6,1,4,1,9148,3,3,3,2),_ApEnvMonTrapPreviousState_Type())
apEnvMonTrapPreviousState.setMaxAccess(_E)
if mibBuilder.loadTexts:apEnvMonTrapPreviousState.setStatus(_A)
_ApEnvMonTrapCurrentState_Type=ApEnvMonState
_ApEnvMonTrapCurrentState_Object=MibScalar
apEnvMonTrapCurrentState=_ApEnvMonTrapCurrentState_Object((1,3,6,1,4,1,9148,3,3,3,3),_ApEnvMonTrapCurrentState_Type())
apEnvMonTrapCurrentState.setMaxAccess(_E)
if mibBuilder.loadTexts:apEnvMonTrapCurrentState.setStatus(_A)
_ApEnvMonTrapSlotID_Type=Integer32
_ApEnvMonTrapSlotID_Object=MibScalar
apEnvMonTrapSlotID=_ApEnvMonTrapSlotID_Object((1,3,6,1,4,1,9148,3,3,3,4),_ApEnvMonTrapSlotID_Type())
apEnvMonTrapSlotID.setMaxAccess(_E)
if mibBuilder.loadTexts:apEnvMonTrapSlotID.setStatus(_A)
_ApEnvMonTrapSlotType_Type=ApHardwareModuleFamily
_ApEnvMonTrapSlotType_Object=MibScalar
apEnvMonTrapSlotType=_ApEnvMonTrapSlotType_Object((1,3,6,1,4,1,9148,3,3,3,5),_ApEnvMonTrapSlotType_Type())
apEnvMonTrapSlotType.setMaxAccess(_E)
if mibBuilder.loadTexts:apEnvMonTrapSlotType.setStatus(_A)
_ApEnvMonTrapPortType_Type=ApPhyPortType
_ApEnvMonTrapPortType_Object=MibScalar
apEnvMonTrapPortType=_ApEnvMonTrapPortType_Object((1,3,6,1,4,1,9148,3,3,3,6),_ApEnvMonTrapPortType_Type())
apEnvMonTrapPortType.setMaxAccess(_E)
if mibBuilder.loadTexts:apEnvMonTrapPortType.setStatus(_A)
_ApEnvMonTrapPresence_Type=ApPresence
_ApEnvMonTrapPresence_Object=MibScalar
apEnvMonTrapPresence=_ApEnvMonTrapPresence_Object((1,3,6,1,4,1,9148,3,3,3,7),_ApEnvMonTrapPresence_Type())
apEnvMonTrapPresence.setMaxAccess(_E)
if mibBuilder.loadTexts:apEnvMonTrapPresence.setStatus(_A)
_ApEnvMonTrapPortID_Type=Integer32
_ApEnvMonTrapPortID_Object=MibScalar
apEnvMonTrapPortID=_ApEnvMonTrapPortID_Object((1,3,6,1,4,1,9148,3,3,3,8),_ApEnvMonTrapPortID_Type())
apEnvMonTrapPortID.setMaxAccess(_E)
if mibBuilder.loadTexts:apEnvMonTrapPortID.setStatus(_A)
_ApEnvMonMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
apEnvMonMIBNotificationPrefix=_ApEnvMonMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9148,3,3,4))
_ApEnvMonMIBNotifications_ObjectIdentity=ObjectIdentity
apEnvMonMIBNotifications=_ApEnvMonMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9148,3,3,4,0))
_ApEnvMonMIBConformance_ObjectIdentity=ObjectIdentity
apEnvMonMIBConformance=_ApEnvMonMIBConformance_ObjectIdentity((1,3,6,1,4,1,9148,3,3,5))
_ApEnvMonMIBCompliances_ObjectIdentity=ObjectIdentity
apEnvMonMIBCompliances=_ApEnvMonMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9148,3,3,5,1))
_ApEnvMonMIBGroups_ObjectIdentity=ObjectIdentity
apEnvMonMIBGroups=_ApEnvMonMIBGroups_ObjectIdentity((1,3,6,1,4,1,9148,3,3,5,2))
apEnvMonGroup=ObjectGroup((1,3,6,1,4,1,9148,3,3,5,2,1))
apEnvMonGroup.setObjects(*((_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r)))
if mibBuilder.loadTexts:apEnvMonGroup.setStatus(_A)
apEnvMonExtGroup=ObjectGroup((1,3,6,1,4,1,9148,3,3,5,2,4))
apEnvMonExtGroup.setObjects(*((_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w)))
if mibBuilder.loadTexts:apEnvMonExtGroup.setStatus(_A)
apEnvMonCardGroup=ObjectGroup((1,3,6,1,4,1,9148,3,3,5,2,5))
apEnvMonCardGroup.setObjects(*((_B,_I),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_Q),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6)))
if mibBuilder.loadTexts:apEnvMonCardGroup.setStatus(_A)
apEnvMonI2CFailNotification=NotificationType((1,3,6,1,4,1,9148,3,3,4,0,1))
if mibBuilder.loadTexts:apEnvMonI2CFailNotification.setStatus(_A)
apEnvMonStatusChangeNotification=NotificationType((1,3,6,1,4,1,9148,3,3,4,0,2))
apEnvMonStatusChangeNotification.setObjects(*((_B,_A7),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:apEnvMonStatusChangeNotification.setStatus(_A)
apEnvMonTempChangeNotification=NotificationType((1,3,6,1,4,1,9148,3,3,4,0,3))
apEnvMonTempChangeNotification.setObjects(*((_B,_L),(_B,_R),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:apEnvMonTempChangeNotification.setStatus(_A)
apEnvMonVoltageChangeNotification=NotificationType((1,3,6,1,4,1,9148,3,3,4,0,4))
apEnvMonVoltageChangeNotification.setObjects(*((_B,_L),(_B,_R),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:apEnvMonVoltageChangeNotification.setStatus(_A)
apEnvMonPortChangeNotification=NotificationType((1,3,6,1,4,1,9148,3,3,4,0,5))
apEnvMonPortChangeNotification.setObjects(*((_B,_A8),(_B,_A9),(_B,_L),(_B,_AA)))
if mibBuilder.loadTexts:apEnvMonPortChangeNotification.setStatus(_A)
apEnvMonNotifyGroup=NotificationGroup((1,3,6,1,4,1,9148,3,3,5,2,3))
apEnvMonNotifyGroup.setObjects(*((_B,_AB),(_B,_AC)))
if mibBuilder.loadTexts:apEnvMonNotifyGroup.setStatus(_A)
apEnvMonExtNotifyGroup=NotificationGroup((1,3,6,1,4,1,9148,3,3,5,2,6))
apEnvMonExtNotifyGroup.setObjects(*((_B,_S),(_B,_AD)))
if mibBuilder.loadTexts:apEnvMonExtNotifyGroup.setStatus(_A)
apEnvMonPortNotifyGroup=NotificationGroup((1,3,6,1,4,1,9148,3,3,5,2,7))
apEnvMonPortNotifyGroup.setObjects((_B,_AE))
if mibBuilder.loadTexts:apEnvMonPortNotifyGroup.setStatus(_A)
apEnvMonTempNotifyGroup=NotificationGroup((1,3,6,1,4,1,9148,3,3,5,2,8))
apEnvMonTempNotifyGroup.setObjects((_B,_S))
if mibBuilder.loadTexts:apEnvMonTempNotifyGroup.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ApEnvMonState':ApEnvMonState,'apEnvMonModule':apEnvMonModule,'apEnvMonObjects':apEnvMonObjects,_Y:apEnvMonI2CState,'apEnvMonVoltageObjects':apEnvMonVoltageObjects,'apEnvMonVoltageStatusTable':apEnvMonVoltageStatusTable,'apEnvMonVoltageStatusEntry':apEnvMonVoltageStatusEntry,_T:apEnvMonVoltageStatusIndex,_Z:apEnvMonVoltageStatusType,_a:apEnvMonVoltageStatusDescr,_b:apEnvMonVoltageStatusValue,_c:apEnvMonVoltageState,_s:apEnvMonVoltageSlotID,_t:apEnvMonVoltageSlotType,'apEnvMonTemperatureObjects':apEnvMonTemperatureObjects,'apEnvMonTemperatureStatusTable':apEnvMonTemperatureStatusTable,'apEnvMonTemperatureStatusEntry':apEnvMonTemperatureStatusEntry,_U:apEnvMonTemperatureStatusIndex,_d:apEnvMonTemperatureStatusType,_e:apEnvMonTemperatureStatusDescr,_f:apEnvMonTemperatureStatusValue,_g:apEnvMonTemperatureState,_u:apEnvMonTemperatureSlotID,_v:apEnvMonTemperatureSlotType,'apEnvMonFanObjects':apEnvMonFanObjects,'apEnvMonFanStatusTable':apEnvMonFanStatusTable,'apEnvMonFanStatusEntry':apEnvMonFanStatusEntry,_V:apEnvMonFanStatusIndex,_h:apEnvMonFanStatusType,_i:apEnvMonFanStatusDescr,_j:apEnvMonFanStatusValue,_k:apEnvMonFanState,_w:apEnvMonFanSlotID,'apEnvMonPowerSupplyObjects':apEnvMonPowerSupplyObjects,'apEnvMonPowerSupplyStatusTable':apEnvMonPowerSupplyStatusTable,'apEnvMonPowerSupplyStatusEntry':apEnvMonPowerSupplyStatusEntry,_W:apEnvMonPowerSupplyStatusIndex,_l:apEnvMonPowerSupplyStatusType,_m:apEnvMonPowerSupplyStatusDescr,_n:apEnvMonPowerSupplyState,'apEnvMonPhyCardObjects':apEnvMonPhyCardObjects,'apEnvMonPhyCardStatusTable':apEnvMonPhyCardStatusTable,'apEnvMonPhyCardStatusEntry':apEnvMonPhyCardStatusEntry,_X:apEnvMonPhyCardStatusIndex,_o:apEnvMonPhyCardStatusType,_p:apEnvMonPhyCardStatusDescr,_q:apEnvMonPhyCardState,'apEnvMonCardObjects':apEnvMonCardObjects,'apEnvMonCardTable':apEnvMonCardTable,'apEnvMonCardEntry':apEnvMonCardEntry,_I:apEnvMonCardSlot,_x:apEnvMonCardType,_y:apEnvMonCardDescr,_z:apEnvMonCardHealthScore,_A0:apEnvMonCardState,_A1:apEnvMonCardRedundancy,'apEnvMonCpuCoreTable':apEnvMonCpuCoreTable,'apEnvMonCpuCoreEntry':apEnvMonCpuCoreEntry,_Q:apEnvMonCpuCoreIndex,_A2:apEnvMonCpuCoreDescr,_A3:apEnvMonCpuCoreUsage,_A4:apEnvMonCpuCoreState,_A5:apEnvMonCpuCoreRamDescr,_A6:apEnvMonCpuCoreRamUsage,'apEnvMonMIBNotificationEnables':apEnvMonMIBNotificationEnables,_r:apEnvMonEnableStatChangeNotif,'apEnvMonNotificationObjects':apEnvMonNotificationObjects,_A7:apEnvMonTrapInstance,_J:apEnvMonTrapPreviousState,_K:apEnvMonTrapCurrentState,_L:apEnvMonTrapSlotID,_R:apEnvMonTrapSlotType,_A8:apEnvMonTrapPortType,_A9:apEnvMonTrapPresence,_AA:apEnvMonTrapPortID,'apEnvMonMIBNotificationPrefix':apEnvMonMIBNotificationPrefix,'apEnvMonMIBNotifications':apEnvMonMIBNotifications,_AC:apEnvMonI2CFailNotification,_AB:apEnvMonStatusChangeNotification,_S:apEnvMonTempChangeNotification,_AD:apEnvMonVoltageChangeNotification,_AE:apEnvMonPortChangeNotification,'apEnvMonMIBConformance':apEnvMonMIBConformance,'apEnvMonMIBCompliances':apEnvMonMIBCompliances,'apEnvMonMIBGroups':apEnvMonMIBGroups,'apEnvMonGroup':apEnvMonGroup,'apEnvMonNotifyGroup':apEnvMonNotifyGroup,'apEnvMonExtGroup':apEnvMonExtGroup,'apEnvMonCardGroup':apEnvMonCardGroup,'apEnvMonExtNotifyGroup':apEnvMonExtNotifyGroup,'apEnvMonPortNotifyGroup':apEnvMonPortNotifyGroup,'apEnvMonTempNotifyGroup':apEnvMonTempNotifyGroup})