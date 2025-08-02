_Ar='tmnxOesHwNotificationGroupV14v0'
_Aq='tmnxOesHwNotifyObjsGroupV14v0'
_Ap='tmnxOesHwGroupV14v0'
_Ao='tmnxOesTempLowClear'
_An='tmnxOesTempLow'
_Am='tmnxOesCardFirmwareErr'
_Al='tmnxOesRedundancyReady'
_Ak='tmnxOesRedundancyFail'
_Aj='tmnxOesFanSpeedLowClear'
_Ai='tmnxOesFanSpeedLow'
_Ah='tmnxOesFanSpeedHighClear'
_Ag='tmnxOesFanSpeedHigh'
_Af='tmnxOesCardDegraded'
_Ae='tmnxOesOptTrnspndrMiscFail'
_Ad='tmnxOesFpgaTimeoutClear'
_Ac='tmnxOesFpgaTimeout'
_Ab='tmnxOesFpgaFailClear'
_Aa='tmnxOesFpgaFail'
_AZ='tmnxOesCtlCardActivityChange'
_AY='tmnxOesPortErrorClear'
_AX='tmnxOesPortError'
_AW='tmnxOesPowerSupplyFailureClear'
_AV='tmnxOesPowerSupplyFailure'
_AU='tmnxOesPowerSupplyInserted'
_AT='tmnxOesPowerSupplyRemoved'
_AS='tmnxOesFanFailureClear'
_AR='tmnxOesFanFailure'
_AQ='tmnxOesFan32HReqdClear'
_AP='tmnxOesFan32HReqd'
_AO='tmnxOesFanInserted'
_AN='tmnxOesFanRemoved'
_AM='tmnxOesUsrpnlPortUp'
_AL='tmnxOesUsrpnlPortDown'
_AK='tmnxOesCtlCardPortUp'
_AJ='tmnxOesCtlCardPortDown'
_AI='tmnxOesCmnEqpPortTypeName'
_AH='tmnxOesCmnEqpPortTypeDescr'
_AG='tmnxOesCmnEqpPortCardType'
_AF='tmnxOesControlCardHwIndex'
_AE='tmnxOesControlCardActState'
_AD='tmnxOesCardMemorySize'
_AC='tmnxOesCardRowLastChanged'
_AB='tmnxOesCardHwEntryIndex'
_AA='tmnxOesCardReboot'
_A9='tmnxOesCardSupportedTypes'
_A8='tmnxOesCardEquippedType'
_A7='tmnxOesCardAssignedType'
_A6='tmnxOesCardLastChange'
_A5='tmnxOesCardTypeNumPorts'
_A4='tmnxOesCardTypeWidth'
_A3='tmnxOesCardTypeHeight'
_A2='tmnxOesCardTypeStatus'
_A1='tmnxOesCardTypeDescription'
_A0='tmnxOesCardTypeName'
_z='tmnxOesFanHwIndex'
_y='tmnxOesFanSpeedControl'
_x='tmnxOesFanLastChg'
_w='tmnxOesPFHwIndex'
_v='tmnxOesPFClkDelta'
_u='tmnxOesPFClkB'
_t='tmnxOesPFClkA'
_s='tmnxOesPFInputPower'
_r='tmnxOesPFInputVoltage'
_q='tmnxOesPFInputCurrent'
_p='tmnxOesPFAmpRating'
_o='tmnxOesPFType'
_n='tmnxOesChassisHwEntryIndex'
_m='tmnxOesChassisActivitySwitch'
_l='tmnxOesChassisEquippedType'
_k='tmnxOesChassisAssignedType'
_j='tmnxOesChassisLastChange'
_i='tmnxOesChassisTypeStatus'
_h='tmnxOesChassisTypeDescription'
_g='tmnxOesChassisTypeName'
_f='tmnxOesChassisRowStatus'
_e='tmnxOesChassisRowLastChanged'
_d='accessible-for-notify'
_c='TmnxOesCardType'
_b='tmnxOesFanSlotNumber'
_a='TmnxOesChassisType'
_Z='tmnxOesChassisTypeIndex'
_Y='TmnxActionType'
_X='TmnxCardRebootType'
_W='tmnxOesPortNotifyError'
_V='tmnxOesCmnEqpPortNumber'
_U='tmnxOesCardTypeIndex'
_T='read-write'
_S='1/10 parts-per-million'
_R='read-create'
_Q='unknown'
_P='tmnxPortNotifyPortId'
_O='TIMETRA-PORT-MIB'
_N='SnmpAdminString'
_M='tmnxOesFanState'
_L='tmnxOesPFState'
_K='Integer32'
_J='tmnxOesSlotNumber'
_I='tmnxOesNotifyFailureReason'
_H='tmnxOesCmnEqpPortOperStatus'
_G='not-accessible'
_F='tmnxOesChassisNumber'
_E='tmnxHwClass'
_D='TIMETRA-CHASSIS-MIB'
_C='read-only'
_B='TIMETRA-OES-HARDWARE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_N)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_K,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp','TruthValue')
TmnxCardRebootType,TmnxDeviceState,TmnxHwIndex,TmnxLEDState,TmnxPhysChassisIndex,tmnxHwClass,tmnxHwIndex=mibBuilder.importSymbols(_D,_X,'TmnxDeviceState','TmnxHwIndex','TmnxLEDState','TmnxPhysChassisIndex',_E,'tmnxHwIndex')
timetraSRMIBModules,tmnxSRConfs,tmnxSRNotifyPrefix,tmnxSRObjs=mibBuilder.importSymbols('TIMETRA-GLOBAL-MIB','timetraSRMIBModules','tmnxSRConfs','tmnxSRNotifyPrefix','tmnxSRObjs')
TmnxPortOperStatus,tmnxPortNotifyPortId=mibBuilder.importSymbols(_O,'TmnxPortOperStatus',_P)
TItemDescription,TNamedItem,TNamedItemOrEmpty,TmnxActionType,TmnxAdminState,TmnxOperState=mibBuilder.importSymbols('TIMETRA-TC-MIB','TItemDescription','TNamedItem','TNamedItemOrEmpty',_Y,'TmnxAdminState','TmnxOperState')
timetraOesHardwareMIBModule=ModuleIdentity((1,3,6,1,4,1,6527,1,1,3,99))
if mibBuilder.loadTexts:timetraOesHardwareMIBModule.setRevisions(('2013-08-01 00:00',))
class TmnxOesCardHFD(SnmpAdminString):status=_A;subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2))
class TmnxOesHwMktPartNo(SnmpAdminString):status=_A;subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
class TmnxOesHwSWGenLoadName(SnmpAdminString):status=_A;subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
class TmnxOesHwLEDColorType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_Q,1),('off',2),('red',3),('green',4),('orange',5)))
class TmnxOesHwLEDStateType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_Q,1),('solid',2),('fastBlink',3),('slowBlink',4)))
class TmnxOesSlotNumber(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,40))
class TmnxOesChassisType(TextualConvention,Unsigned32):status=_A
class TmnxOesCardType(TextualConvention,Unsigned32):status=_A
class TmnxOesCardSuppType(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('invalid-card-type',0),('unassigned',1),('oes-supp-card-type-2',2),('oes-supp-card-type-3',3),('oes-supp-card-type-4',4),('oes-supp-card-type-5',5),('oes-supp-card-type-6',6),('oes-supp-card-type-7',7),('oes-supp-card-type-8',8)))
class TmnxOesCmnEqpPortNumber(TextualConvention,Unsigned32):status=_A
class TmnxOesPortErrorStatus(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('deviceFailure',0),('transmissionFailure',1)))
_TmnxOesHwConformance_ObjectIdentity=ObjectIdentity
tmnxOesHwConformance=_TmnxOesHwConformance_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,99))
_TmnxOesHwCompliances_ObjectIdentity=ObjectIdentity
tmnxOesHwCompliances=_TmnxOesHwCompliances_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,99,1))
_TmnxOesHwGroups_ObjectIdentity=ObjectIdentity
tmnxOesHwGroups=_TmnxOesHwGroups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,99,2))
_TmnxOesHwV14v0Groups_ObjectIdentity=ObjectIdentity
tmnxOesHwV14v0Groups=_TmnxOesHwV14v0Groups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,99,2,1))
_TmnxOesHwObjs_ObjectIdentity=ObjectIdentity
tmnxOesHwObjs=_TmnxOesHwObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,99))
_TmnxOesChassisObjs_ObjectIdentity=ObjectIdentity
tmnxOesChassisObjs=_TmnxOesChassisObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,99,1))
_TmnxOesChassisTypeTable_Object=MibTable
tmnxOesChassisTypeTable=_TmnxOesChassisTypeTable_Object((1,3,6,1,4,1,6527,3,1,2,99,1,1))
if mibBuilder.loadTexts:tmnxOesChassisTypeTable.setStatus(_A)
_TmnxOesChassisTypeEntry_Object=MibTableRow
tmnxOesChassisTypeEntry=_TmnxOesChassisTypeEntry_Object((1,3,6,1,4,1,6527,3,1,2,99,1,1,1))
tmnxOesChassisTypeEntry.setIndexNames((0,_B,_Z))
if mibBuilder.loadTexts:tmnxOesChassisTypeEntry.setStatus(_A)
_TmnxOesChassisTypeIndex_Type=TmnxOesChassisType
_TmnxOesChassisTypeIndex_Object=MibTableColumn
tmnxOesChassisTypeIndex=_TmnxOesChassisTypeIndex_Object((1,3,6,1,4,1,6527,3,1,2,99,1,1,1,1),_TmnxOesChassisTypeIndex_Type())
tmnxOesChassisTypeIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:tmnxOesChassisTypeIndex.setStatus(_A)
_TmnxOesChassisTypeName_Type=TNamedItemOrEmpty
_TmnxOesChassisTypeName_Object=MibTableColumn
tmnxOesChassisTypeName=_TmnxOesChassisTypeName_Object((1,3,6,1,4,1,6527,3,1,2,99,1,1,1,2),_TmnxOesChassisTypeName_Type())
tmnxOesChassisTypeName.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxOesChassisTypeName.setStatus(_A)
_TmnxOesChassisTypeDescription_Type=TItemDescription
_TmnxOesChassisTypeDescription_Object=MibTableColumn
tmnxOesChassisTypeDescription=_TmnxOesChassisTypeDescription_Object((1,3,6,1,4,1,6527,3,1,2,99,1,1,1,3),_TmnxOesChassisTypeDescription_Type())
tmnxOesChassisTypeDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxOesChassisTypeDescription.setStatus(_A)
_TmnxOesChassisTypeStatus_Type=TruthValue
_TmnxOesChassisTypeStatus_Object=MibTableColumn
tmnxOesChassisTypeStatus=_TmnxOesChassisTypeStatus_Object((1,3,6,1,4,1,6527,3,1,2,99,1,1,1,4),_TmnxOesChassisTypeStatus_Type())
tmnxOesChassisTypeStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxOesChassisTypeStatus.setStatus(_A)
_TmnxOesChassisLastChange_Type=TimeStamp
_TmnxOesChassisLastChange_Object=MibScalar
tmnxOesChassisLastChange=_TmnxOesChassisLastChange_Object((1,3,6,1,4,1,6527,3,1,2,99,1,2),_TmnxOesChassisLastChange_Type())
tmnxOesChassisLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxOesChassisLastChange.setStatus(_A)
_TmnxOesChassisTable_Object=MibTable
tmnxOesChassisTable=_TmnxOesChassisTable_Object((1,3,6,1,4,1,6527,3,1,2,99,1,3))
if mibBuilder.loadTexts:tmnxOesChassisTable.setStatus(_A)
_TmnxOesChassisEntry_Object=MibTableRow
tmnxOesChassisEntry=_TmnxOesChassisEntry_Object((1,3,6,1,4,1,6527,3,1,2,99,1,3,1))
tmnxOesChassisEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:tmnxOesChassisEntry.setStatus(_A)
_TmnxOesChassisNumber_Type=TmnxPhysChassisIndex
_TmnxOesChassisNumber_Object=MibTableColumn
tmnxOesChassisNumber=_TmnxOesChassisNumber_Object((1,3,6,1,4,1,6527,3,1,2,99,1,3,1,1),_TmnxOesChassisNumber_Type())
tmnxOesChassisNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:tmnxOesChassisNumber.setStatus(_A)
_TmnxOesChassisRowStatus_Type=RowStatus
_TmnxOesChassisRowStatus_Object=MibTableColumn
tmnxOesChassisRowStatus=_TmnxOesChassisRowStatus_Object((1,3,6,1,4,1,6527,3,1,2,99,1,3,1,2),_TmnxOesChassisRowStatus_Type())
tmnxOesChassisRowStatus.setMaxAccess(_R)
if mibBuilder.loadTexts:tmnxOesChassisRowStatus.setStatus(_A)
_TmnxOesChassisRowLastChanged_Type=TimeStamp
_TmnxOesChassisRowLastChanged_Object=MibTableColumn
tmnxOesChassisRowLastChanged=_TmnxOesChassisRowLastChanged_Object((1,3,6,1,4,1,6527,3,1,2,99,1,3,1,3),_TmnxOesChassisRowLastChanged_Type())
tmnxOesChassisRowLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxOesChassisRowLastChanged.setStatus(_A)
class _TmnxOesChassisAssignedType_Type(TmnxOesChassisType):defaultValue=1
_TmnxOesChassisAssignedType_Type.__name__=_a
_TmnxOesChassisAssignedType_Object=MibTableColumn
tmnxOesChassisAssignedType=_TmnxOesChassisAssignedType_Object((1,3,6,1,4,1,6527,3,1,2,99,1,3,1,4),_TmnxOesChassisAssignedType_Type())
tmnxOesChassisAssignedType.setMaxAccess(_R)
if mibBuilder.loadTexts:tmnxOesChassisAssignedType.setStatus(_A)
_TmnxOesChassisEquippedType_Type=TmnxOesChassisType
_TmnxOesChassisEquippedType_Object=MibTableColumn
tmnxOesChassisEquippedType=_TmnxOesChassisEquippedType_Object((1,3,6,1,4,1,6527,3,1,2,99,1,3,1,5),_TmnxOesChassisEquippedType_Type())
tmnxOesChassisEquippedType.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxOesChassisEquippedType.setStatus(_A)
class _TmnxOesChassisActivitySwitch_Type(TmnxActionType):defaultValue=2
_TmnxOesChassisActivitySwitch_Type.__name__=_Y
_TmnxOesChassisActivitySwitch_Object=MibTableColumn
tmnxOesChassisActivitySwitch=_TmnxOesChassisActivitySwitch_Object((1,3,6,1,4,1,6527,3,1,2,99,1,3,1,6),_TmnxOesChassisActivitySwitch_Type())
tmnxOesChassisActivitySwitch.setMaxAccess(_R)
if mibBuilder.loadTexts:tmnxOesChassisActivitySwitch.setStatus(_A)
_TmnxOesChassisHwEntryIndex_Type=TmnxHwIndex
_TmnxOesChassisHwEntryIndex_Object=MibTableColumn
tmnxOesChassisHwEntryIndex=_TmnxOesChassisHwEntryIndex_Object((1,3,6,1,4,1,6527,3,1,2,99,1,3,1,7),_TmnxOesChassisHwEntryIndex_Type())
tmnxOesChassisHwEntryIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxOesChassisHwEntryIndex.setStatus(_A)
_TmnxOesPFTable_Object=MibTable
tmnxOesPFTable=_TmnxOesPFTable_Object((1,3,6,1,4,1,6527,3,1,2,99,1,4))
if mibBuilder.loadTexts:tmnxOesPFTable.setStatus(_A)
_TmnxOesPFEntry_Object=MibTableRow
tmnxOesPFEntry=_TmnxOesPFEntry_Object((1,3,6,1,4,1,6527,3,1,2,99,1,4,1))
tmnxOesPFEntry.setIndexNames((0,_B,_F),(0,_B,_J))
if mibBuilder.loadTexts:tmnxOesPFEntry.setStatus(_A)
_TmnxOesSlotNumber_Type=TmnxOesSlotNumber
_TmnxOesSlotNumber_Object=MibTableColumn
tmnxOesSlotNumber=_TmnxOesSlotNumber_Object((1,3,6,1,4,1,6527,3,1,2,99,1,4,1,1),_TmnxOesSlotNumber_Type())
tmnxOesSlotNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:tmnxOesSlotNumber.setStatus(_A)
class _TmnxOesPFType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ac',1),('dc',2)))
_TmnxOesPFType_Type.__name__=_K
_TmnxOesPFType_Object=MibTableColumn
tmnxOesPFType=_TmnxOesPFType_Object((1,3,6,1,4,1,6527,3,1,2,99,1,4,1,2),_TmnxOesPFType_Type())
tmnxOesPFType.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxOesPFType.setStatus(_A)
_TmnxOesPFAmpRating_Type=Unsigned32
_TmnxOesPFAmpRating_Object=MibTableColumn
tmnxOesPFAmpRating=_TmnxOesPFAmpRating_Object((1,3,6,1,4,1,6527,3,1,2,99,1,4,1,3),_TmnxOesPFAmpRating_Type())
tmnxOesPFAmpRating.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxOesPFAmpRating.setStatus(_A)
if mibBuilder.loadTexts:tmnxOesPFAmpRating.setUnits('deci-amps')
_TmnxOesPFInputCurrent_Type=Unsigned32
_TmnxOesPFInputCurrent_Object=MibTableColumn
tmnxOesPFInputCurrent=_TmnxOesPFInputCurrent_Object((1,3,6,1,4,1,6527,3,1,2,99,1,4,1,4),_TmnxOesPFInputCurrent_Type())
tmnxOesPFInputCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxOesPFInputCurrent.setStatus(_A)
if mibBuilder.loadTexts:tmnxOesPFInputCurrent.setUnits('milli-amps')
_TmnxOesPFInputVoltage_Type=Unsigned32
_TmnxOesPFInputVoltage_Object=MibTableColumn
tmnxOesPFInputVoltage=_TmnxOesPFInputVoltage_Object((1,3,6,1,4,1,6527,3,1,2,99,1,4,1,5),_TmnxOesPFInputVoltage_Type())
tmnxOesPFInputVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxOesPFInputVoltage.setStatus(_A)
if mibBuilder.loadTexts:tmnxOesPFInputVoltage.setUnits('milli-volts')
_TmnxOesPFInputPower_Type=Unsigned32
_TmnxOesPFInputPower_Object=MibTableColumn
tmnxOesPFInputPower=_TmnxOesPFInputPower_Object((1,3,6,1,4,1,6527,3,1,2,99,1,4,1,6),_TmnxOesPFInputPower_Type())
tmnxOesPFInputPower.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxOesPFInputPower.setStatus(_A)
if mibBuilder.loadTexts:tmnxOesPFInputPower.setUnits('watts')
_TmnxOesPFClkA_Type=Unsigned32
_TmnxOesPFClkA_Object=MibTableColumn
tmnxOesPFClkA=_TmnxOesPFClkA_Object((1,3,6,1,4,1,6527,3,1,2,99,1,4,1,7),_TmnxOesPFClkA_Type())
tmnxOesPFClkA.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxOesPFClkA.setStatus(_A)
if mibBuilder.loadTexts:tmnxOesPFClkA.setUnits(_S)
_TmnxOesPFClkB_Type=Unsigned32
_TmnxOesPFClkB_Object=MibTableColumn
tmnxOesPFClkB=_TmnxOesPFClkB_Object((1,3,6,1,4,1,6527,3,1,2,99,1,4,1,8),_TmnxOesPFClkB_Type())
tmnxOesPFClkB.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxOesPFClkB.setStatus(_A)
if mibBuilder.loadTexts:tmnxOesPFClkB.setUnits(_S)
_TmnxOesPFClkDelta_Type=Integer32
_TmnxOesPFClkDelta_Object=MibTableColumn
tmnxOesPFClkDelta=_TmnxOesPFClkDelta_Object((1,3,6,1,4,1,6527,3,1,2,99,1,4,1,9),_TmnxOesPFClkDelta_Type())
tmnxOesPFClkDelta.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxOesPFClkDelta.setStatus(_A)
if mibBuilder.loadTexts:tmnxOesPFClkDelta.setUnits(_S)
_TmnxOesPFState_Type=TmnxDeviceState
_TmnxOesPFState_Object=MibTableColumn
tmnxOesPFState=_TmnxOesPFState_Object((1,3,6,1,4,1,6527,3,1,2,99,1,4,1,10),_TmnxOesPFState_Type())
tmnxOesPFState.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxOesPFState.setStatus(_A)
_TmnxOesPFHwIndex_Type=TmnxHwIndex
_TmnxOesPFHwIndex_Object=MibTableColumn
tmnxOesPFHwIndex=_TmnxOesPFHwIndex_Object((1,3,6,1,4,1,6527,3,1,2,99,1,4,1,11),_TmnxOesPFHwIndex_Type())
tmnxOesPFHwIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxOesPFHwIndex.setStatus(_A)
_TmnxOesFanLastChg_Type=TimeStamp
_TmnxOesFanLastChg_Object=MibScalar
tmnxOesFanLastChg=_TmnxOesFanLastChg_Object((1,3,6,1,4,1,6527,3,1,2,99,1,5),_TmnxOesFanLastChg_Type())
tmnxOesFanLastChg.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxOesFanLastChg.setStatus(_A)
_TmnxOesFanTable_Object=MibTable
tmnxOesFanTable=_TmnxOesFanTable_Object((1,3,6,1,4,1,6527,3,1,2,99,1,6))
if mibBuilder.loadTexts:tmnxOesFanTable.setStatus(_A)
_TmnxOesFanEntry_Object=MibTableRow
tmnxOesFanEntry=_TmnxOesFanEntry_Object((1,3,6,1,4,1,6527,3,1,2,99,1,6,1))
tmnxOesFanEntry.setIndexNames((0,_B,_F),(0,_B,_b))
if mibBuilder.loadTexts:tmnxOesFanEntry.setStatus(_A)
_TmnxOesFanSlotNumber_Type=TmnxOesSlotNumber
_TmnxOesFanSlotNumber_Object=MibTableColumn
tmnxOesFanSlotNumber=_TmnxOesFanSlotNumber_Object((1,3,6,1,4,1,6527,3,1,2,99,1,6,1,1),_TmnxOesFanSlotNumber_Type())
tmnxOesFanSlotNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:tmnxOesFanSlotNumber.setStatus(_A)
_TmnxOesFanState_Type=TmnxDeviceState
_TmnxOesFanState_Object=MibTableColumn
tmnxOesFanState=_TmnxOesFanState_Object((1,3,6,1,4,1,6527,3,1,2,99,1,6,1,2),_TmnxOesFanState_Type())
tmnxOesFanState.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxOesFanState.setStatus(_A)
class _TmnxOesFanSpeedControl_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('normal',1),('maximum',2)))
_TmnxOesFanSpeedControl_Type.__name__=_K
_TmnxOesFanSpeedControl_Object=MibTableColumn
tmnxOesFanSpeedControl=_TmnxOesFanSpeedControl_Object((1,3,6,1,4,1,6527,3,1,2,99,1,6,1,3),_TmnxOesFanSpeedControl_Type())
tmnxOesFanSpeedControl.setMaxAccess(_T)
if mibBuilder.loadTexts:tmnxOesFanSpeedControl.setStatus(_A)
_TmnxOesFanHwIndex_Type=TmnxHwIndex
_TmnxOesFanHwIndex_Object=MibTableColumn
tmnxOesFanHwIndex=_TmnxOesFanHwIndex_Object((1,3,6,1,4,1,6527,3,1,2,99,1,6,1,4),_TmnxOesFanHwIndex_Type())
tmnxOesFanHwIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxOesFanHwIndex.setStatus(_A)
_TmnxOesCardObjs_ObjectIdentity=ObjectIdentity
tmnxOesCardObjs=_TmnxOesCardObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,99,2))
_TmnxOesCardTypeTable_Object=MibTable
tmnxOesCardTypeTable=_TmnxOesCardTypeTable_Object((1,3,6,1,4,1,6527,3,1,2,99,2,1))
if mibBuilder.loadTexts:tmnxOesCardTypeTable.setStatus(_A)
_TmnxOesCardTypeEntry_Object=MibTableRow
tmnxOesCardTypeEntry=_TmnxOesCardTypeEntry_Object((1,3,6,1,4,1,6527,3,1,2,99,2,1,1))
tmnxOesCardTypeEntry.setIndexNames((0,_B,_U))
if mibBuilder.loadTexts:tmnxOesCardTypeEntry.setStatus(_A)
_TmnxOesCardTypeIndex_Type=TmnxOesCardType
_TmnxOesCardTypeIndex_Object=MibTableColumn
tmnxOesCardTypeIndex=_TmnxOesCardTypeIndex_Object((1,3,6,1,4,1,6527,3,1,2,99,2,1,1,1),_TmnxOesCardTypeIndex_Type())
tmnxOesCardTypeIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:tmnxOesCardTypeIndex.setStatus(_A)
class _TmnxOesCardTypeName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_TmnxOesCardTypeName_Type.__name__=_N
_TmnxOesCardTypeName_Object=MibTableColumn
tmnxOesCardTypeName=_TmnxOesCardTypeName_Object((1,3,6,1,4,1,6527,3,1,2,99,2,1,1,2),_TmnxOesCardTypeName_Type())
tmnxOesCardTypeName.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxOesCardTypeName.setStatus(_A)
class _TmnxOesCardTypeDescription_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TmnxOesCardTypeDescription_Type.__name__=_N
_TmnxOesCardTypeDescription_Object=MibTableColumn
tmnxOesCardTypeDescription=_TmnxOesCardTypeDescription_Object((1,3,6,1,4,1,6527,3,1,2,99,2,1,1,3),_TmnxOesCardTypeDescription_Type())
tmnxOesCardTypeDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxOesCardTypeDescription.setStatus(_A)
_TmnxOesCardTypeStatus_Type=TruthValue
_TmnxOesCardTypeStatus_Object=MibTableColumn
tmnxOesCardTypeStatus=_TmnxOesCardTypeStatus_Object((1,3,6,1,4,1,6527,3,1,2,99,2,1,1,4),_TmnxOesCardTypeStatus_Type())
tmnxOesCardTypeStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxOesCardTypeStatus.setStatus(_A)
_TmnxOesCardTypeHeight_Type=Unsigned32
_TmnxOesCardTypeHeight_Object=MibTableColumn
tmnxOesCardTypeHeight=_TmnxOesCardTypeHeight_Object((1,3,6,1,4,1,6527,3,1,2,99,2,1,1,5),_TmnxOesCardTypeHeight_Type())
tmnxOesCardTypeHeight.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxOesCardTypeHeight.setStatus(_A)
_TmnxOesCardTypeWidth_Type=Unsigned32
_TmnxOesCardTypeWidth_Object=MibTableColumn
tmnxOesCardTypeWidth=_TmnxOesCardTypeWidth_Object((1,3,6,1,4,1,6527,3,1,2,99,2,1,1,6),_TmnxOesCardTypeWidth_Type())
tmnxOesCardTypeWidth.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxOesCardTypeWidth.setStatus(_A)
_TmnxOesCardTypeNumPorts_Type=Unsigned32
_TmnxOesCardTypeNumPorts_Object=MibTableColumn
tmnxOesCardTypeNumPorts=_TmnxOesCardTypeNumPorts_Object((1,3,6,1,4,1,6527,3,1,2,99,2,1,1,7),_TmnxOesCardTypeNumPorts_Type())
tmnxOesCardTypeNumPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxOesCardTypeNumPorts.setStatus(_A)
_TmnxOesCardLastChange_Type=TimeStamp
_TmnxOesCardLastChange_Object=MibScalar
tmnxOesCardLastChange=_TmnxOesCardLastChange_Object((1,3,6,1,4,1,6527,3,1,2,99,2,2),_TmnxOesCardLastChange_Type())
tmnxOesCardLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxOesCardLastChange.setStatus(_A)
_TmnxOesCardTable_Object=MibTable
tmnxOesCardTable=_TmnxOesCardTable_Object((1,3,6,1,4,1,6527,3,1,2,99,2,3))
if mibBuilder.loadTexts:tmnxOesCardTable.setStatus(_A)
_TmnxOesCardEntry_Object=MibTableRow
tmnxOesCardEntry=_TmnxOesCardEntry_Object((1,3,6,1,4,1,6527,3,1,2,99,2,3,1))
tmnxOesCardEntry.setIndexNames((0,_B,_F),(0,_B,_J))
if mibBuilder.loadTexts:tmnxOesCardEntry.setStatus(_A)
class _TmnxOesCardAssignedType_Type(TmnxOesCardType):defaultValue=2
_TmnxOesCardAssignedType_Type.__name__=_c
_TmnxOesCardAssignedType_Object=MibTableColumn
tmnxOesCardAssignedType=_TmnxOesCardAssignedType_Object((1,3,6,1,4,1,6527,3,1,2,99,2,3,1,1),_TmnxOesCardAssignedType_Type())
tmnxOesCardAssignedType.setMaxAccess(_T)
if mibBuilder.loadTexts:tmnxOesCardAssignedType.setStatus(_A)
_TmnxOesCardEquippedType_Type=TmnxOesCardType
_TmnxOesCardEquippedType_Object=MibTableColumn
tmnxOesCardEquippedType=_TmnxOesCardEquippedType_Object((1,3,6,1,4,1,6527,3,1,2,99,2,3,1,2),_TmnxOesCardEquippedType_Type())
tmnxOesCardEquippedType.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxOesCardEquippedType.setStatus(_A)
_TmnxOesCardSupportedTypes_Type=TmnxOesCardSuppType
_TmnxOesCardSupportedTypes_Object=MibTableColumn
tmnxOesCardSupportedTypes=_TmnxOesCardSupportedTypes_Object((1,3,6,1,4,1,6527,3,1,2,99,2,3,1,3),_TmnxOesCardSupportedTypes_Type())
tmnxOesCardSupportedTypes.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxOesCardSupportedTypes.setStatus(_A)
class _TmnxOesCardReboot_Type(TmnxCardRebootType):defaultValue=2
_TmnxOesCardReboot_Type.__name__=_X
_TmnxOesCardReboot_Object=MibTableColumn
tmnxOesCardReboot=_TmnxOesCardReboot_Object((1,3,6,1,4,1,6527,3,1,2,99,2,3,1,4),_TmnxOesCardReboot_Type())
tmnxOesCardReboot.setMaxAccess(_T)
if mibBuilder.loadTexts:tmnxOesCardReboot.setStatus(_A)
_TmnxOesCardHwEntryIndex_Type=TmnxHwIndex
_TmnxOesCardHwEntryIndex_Object=MibTableColumn
tmnxOesCardHwEntryIndex=_TmnxOesCardHwEntryIndex_Object((1,3,6,1,4,1,6527,3,1,2,99,2,3,1,5),_TmnxOesCardHwEntryIndex_Type())
tmnxOesCardHwEntryIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxOesCardHwEntryIndex.setStatus(_A)
_TmnxOesCardRowLastChanged_Type=TimeStamp
_TmnxOesCardRowLastChanged_Object=MibTableColumn
tmnxOesCardRowLastChanged=_TmnxOesCardRowLastChanged_Object((1,3,6,1,4,1,6527,3,1,2,99,2,3,1,6),_TmnxOesCardRowLastChanged_Type())
tmnxOesCardRowLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxOesCardRowLastChanged.setStatus(_A)
_TmnxOesCardMemorySize_Type=Unsigned32
_TmnxOesCardMemorySize_Object=MibTableColumn
tmnxOesCardMemorySize=_TmnxOesCardMemorySize_Object((1,3,6,1,4,1,6527,3,1,2,99,2,3,1,7),_TmnxOesCardMemorySize_Type())
tmnxOesCardMemorySize.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxOesCardMemorySize.setStatus(_A)
if mibBuilder.loadTexts:tmnxOesCardMemorySize.setUnits('Giga-bytes')
_TmnxOesControlCardTable_Object=MibTable
tmnxOesControlCardTable=_TmnxOesControlCardTable_Object((1,3,6,1,4,1,6527,3,1,2,99,2,4))
if mibBuilder.loadTexts:tmnxOesControlCardTable.setStatus(_A)
_TmnxOesControlCardEntry_Object=MibTableRow
tmnxOesControlCardEntry=_TmnxOesControlCardEntry_Object((1,3,6,1,4,1,6527,3,1,2,99,2,4,1))
tmnxOesControlCardEntry.setIndexNames((0,_B,_F),(0,_B,_J))
if mibBuilder.loadTexts:tmnxOesControlCardEntry.setStatus(_A)
class _TmnxOesControlCardActState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_Q,1),('active',2),('standby',3),('unequipped',4)))
_TmnxOesControlCardActState_Type.__name__=_K
_TmnxOesControlCardActState_Object=MibTableColumn
tmnxOesControlCardActState=_TmnxOesControlCardActState_Object((1,3,6,1,4,1,6527,3,1,2,99,2,4,1,1),_TmnxOesControlCardActState_Type())
tmnxOesControlCardActState.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxOesControlCardActState.setStatus(_A)
_TmnxOesControlCardHwIndex_Type=TmnxHwIndex
_TmnxOesControlCardHwIndex_Object=MibTableColumn
tmnxOesControlCardHwIndex=_TmnxOesControlCardHwIndex_Object((1,3,6,1,4,1,6527,3,1,2,99,2,4,1,2),_TmnxOesControlCardHwIndex_Type())
tmnxOesControlCardHwIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxOesControlCardHwIndex.setStatus(_A)
_TmnxOesPortObjs_ObjectIdentity=ObjectIdentity
tmnxOesPortObjs=_TmnxOesPortObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,99,3))
_TmnxOesCmnEqpPortTable_Object=MibTable
tmnxOesCmnEqpPortTable=_TmnxOesCmnEqpPortTable_Object((1,3,6,1,4,1,6527,3,1,2,99,3,1))
if mibBuilder.loadTexts:tmnxOesCmnEqpPortTable.setStatus(_A)
_TmnxOesCmnEqpPortEntry_Object=MibTableRow
tmnxOesCmnEqpPortEntry=_TmnxOesCmnEqpPortEntry_Object((1,3,6,1,4,1,6527,3,1,2,99,3,1,1))
tmnxOesCmnEqpPortEntry.setIndexNames((0,_B,_F),(0,_B,_J),(0,_B,_V))
if mibBuilder.loadTexts:tmnxOesCmnEqpPortEntry.setStatus(_A)
_TmnxOesCmnEqpPortNumber_Type=TmnxOesCmnEqpPortNumber
_TmnxOesCmnEqpPortNumber_Object=MibTableColumn
tmnxOesCmnEqpPortNumber=_TmnxOesCmnEqpPortNumber_Object((1,3,6,1,4,1,6527,3,1,2,99,3,1,1,1),_TmnxOesCmnEqpPortNumber_Type())
tmnxOesCmnEqpPortNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:tmnxOesCmnEqpPortNumber.setStatus(_A)
_TmnxOesCmnEqpPortCardType_Type=TmnxOesCardType
_TmnxOesCmnEqpPortCardType_Object=MibTableColumn
tmnxOesCmnEqpPortCardType=_TmnxOesCmnEqpPortCardType_Object((1,3,6,1,4,1,6527,3,1,2,99,3,1,1,2),_TmnxOesCmnEqpPortCardType_Type())
tmnxOesCmnEqpPortCardType.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxOesCmnEqpPortCardType.setStatus(_A)
_TmnxOesCmnEqpPortOperStatus_Type=TmnxPortOperStatus
_TmnxOesCmnEqpPortOperStatus_Object=MibTableColumn
tmnxOesCmnEqpPortOperStatus=_TmnxOesCmnEqpPortOperStatus_Object((1,3,6,1,4,1,6527,3,1,2,99,3,1,1,3),_TmnxOesCmnEqpPortOperStatus_Type())
tmnxOesCmnEqpPortOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxOesCmnEqpPortOperStatus.setStatus(_A)
_TmnxOesCmnEqpPortTypeTable_Object=MibTable
tmnxOesCmnEqpPortTypeTable=_TmnxOesCmnEqpPortTypeTable_Object((1,3,6,1,4,1,6527,3,1,2,99,3,2))
if mibBuilder.loadTexts:tmnxOesCmnEqpPortTypeTable.setStatus(_A)
_TmnxOesCmnEqpPortTypeEntry_Object=MibTableRow
tmnxOesCmnEqpPortTypeEntry=_TmnxOesCmnEqpPortTypeEntry_Object((1,3,6,1,4,1,6527,3,1,2,99,3,2,1))
tmnxOesCmnEqpPortTypeEntry.setIndexNames((0,_B,_U),(0,_B,_V))
if mibBuilder.loadTexts:tmnxOesCmnEqpPortTypeEntry.setStatus(_A)
_TmnxOesCmnEqpPortTypeName_Type=TNamedItem
_TmnxOesCmnEqpPortTypeName_Object=MibTableColumn
tmnxOesCmnEqpPortTypeName=_TmnxOesCmnEqpPortTypeName_Object((1,3,6,1,4,1,6527,3,1,2,99,3,2,1,1),_TmnxOesCmnEqpPortTypeName_Type())
tmnxOesCmnEqpPortTypeName.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxOesCmnEqpPortTypeName.setStatus(_A)
_TmnxOesCmnEqpPortTypeDescr_Type=TItemDescription
_TmnxOesCmnEqpPortTypeDescr_Object=MibTableColumn
tmnxOesCmnEqpPortTypeDescr=_TmnxOesCmnEqpPortTypeDescr_Object((1,3,6,1,4,1,6527,3,1,2,99,3,2,1,2),_TmnxOesCmnEqpPortTypeDescr_Type())
tmnxOesCmnEqpPortTypeDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxOesCmnEqpPortTypeDescr.setStatus(_A)
_TmnxOesHwNotifyObjs_ObjectIdentity=ObjectIdentity
tmnxOesHwNotifyObjs=_TmnxOesHwNotifyObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,99,4))
_TmnxOesNotifyFailureReason_Type=DisplayString
_TmnxOesNotifyFailureReason_Object=MibScalar
tmnxOesNotifyFailureReason=_TmnxOesNotifyFailureReason_Object((1,3,6,1,4,1,6527,3,1,2,99,4,1),_TmnxOesNotifyFailureReason_Type())
tmnxOesNotifyFailureReason.setMaxAccess(_d)
if mibBuilder.loadTexts:tmnxOesNotifyFailureReason.setStatus(_A)
_TmnxOesPortNotifyError_Type=TmnxOesPortErrorStatus
_TmnxOesPortNotifyError_Object=MibScalar
tmnxOesPortNotifyError=_TmnxOesPortNotifyError_Object((1,3,6,1,4,1,6527,3,1,2,99,4,2),_TmnxOesPortNotifyError_Type())
tmnxOesPortNotifyError.setMaxAccess(_d)
if mibBuilder.loadTexts:tmnxOesPortNotifyError.setStatus(_A)
_TmnxOesHwMIBNotifyPrefix_ObjectIdentity=ObjectIdentity
tmnxOesHwMIBNotifyPrefix=_TmnxOesHwMIBNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,6527,3,1,3,99))
_TmnxOesHwNotifications_ObjectIdentity=ObjectIdentity
tmnxOesHwNotifications=_TmnxOesHwNotifications_ObjectIdentity((1,3,6,1,4,1,6527,3,1,3,99,1))
tmnxOesHwGroupV14v0=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,99,2,1,1))
tmnxOesHwGroupV14v0.setObjects(*((_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_L),(_B,_w),(_B,_x),(_B,_M),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_H),(_B,_AH),(_B,_AI)))
if mibBuilder.loadTexts:tmnxOesHwGroupV14v0.setStatus(_A)
tmnxOesHwNotifyObjsGroupV14v0=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,99,2,1,2))
tmnxOesHwNotifyObjsGroupV14v0.setObjects(*((_B,_I),(_B,_W)))
if mibBuilder.loadTexts:tmnxOesHwNotifyObjsGroupV14v0.setStatus(_A)
tmnxOesCtlCardPortDown=NotificationType((1,3,6,1,4,1,6527,3,1,3,99,1,1))
tmnxOesCtlCardPortDown.setObjects((_B,_H))
if mibBuilder.loadTexts:tmnxOesCtlCardPortDown.setStatus(_A)
tmnxOesCtlCardPortUp=NotificationType((1,3,6,1,4,1,6527,3,1,3,99,1,2))
tmnxOesCtlCardPortUp.setObjects((_B,_H))
if mibBuilder.loadTexts:tmnxOesCtlCardPortUp.setStatus(_A)
tmnxOesUsrpnlPortDown=NotificationType((1,3,6,1,4,1,6527,3,1,3,99,1,3))
tmnxOesUsrpnlPortDown.setObjects((_B,_H))
if mibBuilder.loadTexts:tmnxOesUsrpnlPortDown.setStatus(_A)
tmnxOesUsrpnlPortUp=NotificationType((1,3,6,1,4,1,6527,3,1,3,99,1,4))
tmnxOesUsrpnlPortUp.setObjects((_B,_H))
if mibBuilder.loadTexts:tmnxOesUsrpnlPortUp.setStatus(_A)
tmnxOesFanRemoved=NotificationType((1,3,6,1,4,1,6527,3,1,3,99,1,5))
tmnxOesFanRemoved.setObjects((_D,_E))
if mibBuilder.loadTexts:tmnxOesFanRemoved.setStatus(_A)
tmnxOesFanInserted=NotificationType((1,3,6,1,4,1,6527,3,1,3,99,1,6))
tmnxOesFanInserted.setObjects((_D,_E))
if mibBuilder.loadTexts:tmnxOesFanInserted.setStatus(_A)
tmnxOesFan32HReqd=NotificationType((1,3,6,1,4,1,6527,3,1,3,99,1,7))
tmnxOesFan32HReqd.setObjects((_D,_E))
if mibBuilder.loadTexts:tmnxOesFan32HReqd.setStatus(_A)
tmnxOesFan32HReqdClear=NotificationType((1,3,6,1,4,1,6527,3,1,3,99,1,8))
tmnxOesFan32HReqdClear.setObjects((_D,_E))
if mibBuilder.loadTexts:tmnxOesFan32HReqdClear.setStatus(_A)
tmnxOesFanFailure=NotificationType((1,3,6,1,4,1,6527,3,1,3,99,1,9))
tmnxOesFanFailure.setObjects(*((_D,_E),(_B,_M),(_B,_I)))
if mibBuilder.loadTexts:tmnxOesFanFailure.setStatus(_A)
tmnxOesFanFailureClear=NotificationType((1,3,6,1,4,1,6527,3,1,3,99,1,10))
tmnxOesFanFailureClear.setObjects(*((_D,_E),(_B,_M),(_B,_I)))
if mibBuilder.loadTexts:tmnxOesFanFailureClear.setStatus(_A)
tmnxOesPowerSupplyRemoved=NotificationType((1,3,6,1,4,1,6527,3,1,3,99,1,11))
tmnxOesPowerSupplyRemoved.setObjects((_D,_E))
if mibBuilder.loadTexts:tmnxOesPowerSupplyRemoved.setStatus(_A)
tmnxOesPowerSupplyInserted=NotificationType((1,3,6,1,4,1,6527,3,1,3,99,1,12))
tmnxOesPowerSupplyInserted.setObjects((_D,_E))
if mibBuilder.loadTexts:tmnxOesPowerSupplyInserted.setStatus(_A)
tmnxOesPowerSupplyFailure=NotificationType((1,3,6,1,4,1,6527,3,1,3,99,1,13))
tmnxOesPowerSupplyFailure.setObjects(*((_D,_E),(_B,_L),(_B,_I)))
if mibBuilder.loadTexts:tmnxOesPowerSupplyFailure.setStatus(_A)
tmnxOesPowerSupplyFailureClear=NotificationType((1,3,6,1,4,1,6527,3,1,3,99,1,14))
tmnxOesPowerSupplyFailureClear.setObjects(*((_D,_E),(_B,_L),(_B,_I)))
if mibBuilder.loadTexts:tmnxOesPowerSupplyFailureClear.setStatus(_A)
tmnxOesPortError=NotificationType((1,3,6,1,4,1,6527,3,1,3,99,1,15))
tmnxOesPortError.setObjects(*((_O,_P),(_B,_W)))
if mibBuilder.loadTexts:tmnxOesPortError.setStatus(_A)
tmnxOesPortErrorClear=NotificationType((1,3,6,1,4,1,6527,3,1,3,99,1,16))
tmnxOesPortErrorClear.setObjects((_O,_P))
if mibBuilder.loadTexts:tmnxOesPortErrorClear.setStatus(_A)
tmnxOesCtlCardActivityChange=NotificationType((1,3,6,1,4,1,6527,3,1,3,99,1,17))
tmnxOesCtlCardActivityChange.setObjects((_D,_E))
if mibBuilder.loadTexts:tmnxOesCtlCardActivityChange.setStatus(_A)
tmnxOesFpgaFail=NotificationType((1,3,6,1,4,1,6527,3,1,3,99,1,18))
tmnxOesFpgaFail.setObjects((_D,_E))
if mibBuilder.loadTexts:tmnxOesFpgaFail.setStatus(_A)
tmnxOesFpgaFailClear=NotificationType((1,3,6,1,4,1,6527,3,1,3,99,1,19))
tmnxOesFpgaFailClear.setObjects((_D,_E))
if mibBuilder.loadTexts:tmnxOesFpgaFailClear.setStatus(_A)
tmnxOesFpgaTimeout=NotificationType((1,3,6,1,4,1,6527,3,1,3,99,1,20))
tmnxOesFpgaTimeout.setObjects((_D,_E))
if mibBuilder.loadTexts:tmnxOesFpgaTimeout.setStatus(_A)
tmnxOesFpgaTimeoutClear=NotificationType((1,3,6,1,4,1,6527,3,1,3,99,1,21))
tmnxOesFpgaTimeoutClear.setObjects((_D,_E))
if mibBuilder.loadTexts:tmnxOesFpgaTimeoutClear.setStatus(_A)
tmnxOesOptTrnspndrMiscFail=NotificationType((1,3,6,1,4,1,6527,3,1,3,99,1,22))
tmnxOesOptTrnspndrMiscFail.setObjects((_D,_E))
if mibBuilder.loadTexts:tmnxOesOptTrnspndrMiscFail.setStatus(_A)
tmnxOesCardDegraded=NotificationType((1,3,6,1,4,1,6527,3,1,3,99,1,23))
tmnxOesCardDegraded.setObjects((_D,_E))
if mibBuilder.loadTexts:tmnxOesCardDegraded.setStatus(_A)
tmnxOesFanSpeedHigh=NotificationType((1,3,6,1,4,1,6527,3,1,3,99,1,24))
tmnxOesFanSpeedHigh.setObjects((_D,_E))
if mibBuilder.loadTexts:tmnxOesFanSpeedHigh.setStatus(_A)
tmnxOesFanSpeedHighClear=NotificationType((1,3,6,1,4,1,6527,3,1,3,99,1,25))
tmnxOesFanSpeedHighClear.setObjects((_D,_E))
if mibBuilder.loadTexts:tmnxOesFanSpeedHighClear.setStatus(_A)
tmnxOesFanSpeedLow=NotificationType((1,3,6,1,4,1,6527,3,1,3,99,1,26))
tmnxOesFanSpeedLow.setObjects((_D,_E))
if mibBuilder.loadTexts:tmnxOesFanSpeedLow.setStatus(_A)
tmnxOesFanSpeedLowClear=NotificationType((1,3,6,1,4,1,6527,3,1,3,99,1,27))
tmnxOesFanSpeedLowClear.setObjects((_D,_E))
if mibBuilder.loadTexts:tmnxOesFanSpeedLowClear.setStatus(_A)
tmnxOesTempLow=NotificationType((1,3,6,1,4,1,6527,3,1,3,99,1,28))
tmnxOesTempLow.setObjects((_D,_E))
if mibBuilder.loadTexts:tmnxOesTempLow.setStatus(_A)
tmnxOesTempLowClear=NotificationType((1,3,6,1,4,1,6527,3,1,3,99,1,29))
tmnxOesTempLowClear.setObjects((_D,_E))
if mibBuilder.loadTexts:tmnxOesTempLowClear.setStatus(_A)
tmnxOesRedundancyFail=NotificationType((1,3,6,1,4,1,6527,3,1,3,99,1,30))
tmnxOesRedundancyFail.setObjects((_D,_E))
if mibBuilder.loadTexts:tmnxOesRedundancyFail.setStatus(_A)
tmnxOesRedundancyReady=NotificationType((1,3,6,1,4,1,6527,3,1,3,99,1,31))
tmnxOesRedundancyReady.setObjects((_D,_E))
if mibBuilder.loadTexts:tmnxOesRedundancyReady.setStatus(_A)
tmnxOesCardFirmwareErr=NotificationType((1,3,6,1,4,1,6527,3,1,3,99,1,33))
tmnxOesCardFirmwareErr.setObjects((_D,_E))
if mibBuilder.loadTexts:tmnxOesCardFirmwareErr.setStatus(_A)
tmnxOesHwNotificationGroupV14v0=NotificationGroup((1,3,6,1,4,1,6527,3,1,1,99,2,1,3))
tmnxOesHwNotificationGroupV14v0.setObjects(*((_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_Ah),(_B,_Ai),(_B,_Aj),(_B,_Ak),(_B,_Al),(_B,_Am),(_B,_An),(_B,_Ao)))
if mibBuilder.loadTexts:tmnxOesHwNotificationGroupV14v0.setStatus(_A)
tmnxOesHwV14v0Compliance=ModuleCompliance((1,3,6,1,4,1,6527,3,1,1,99,1,1))
tmnxOesHwV14v0Compliance.setObjects(*((_B,_Ap),(_B,_Aq),(_B,_Ar)))
if mibBuilder.loadTexts:tmnxOesHwV14v0Compliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'TmnxOesCardHFD':TmnxOesCardHFD,'TmnxOesHwMktPartNo':TmnxOesHwMktPartNo,'TmnxOesHwSWGenLoadName':TmnxOesHwSWGenLoadName,'TmnxOesHwLEDColorType':TmnxOesHwLEDColorType,'TmnxOesHwLEDStateType':TmnxOesHwLEDStateType,'TmnxOesSlotNumber':TmnxOesSlotNumber,_a:TmnxOesChassisType,_c:TmnxOesCardType,'TmnxOesCardSuppType':TmnxOesCardSuppType,'TmnxOesCmnEqpPortNumber':TmnxOesCmnEqpPortNumber,'TmnxOesPortErrorStatus':TmnxOesPortErrorStatus,'timetraOesHardwareMIBModule':timetraOesHardwareMIBModule,'tmnxOesHwConformance':tmnxOesHwConformance,'tmnxOesHwCompliances':tmnxOesHwCompliances,'tmnxOesHwV14v0Compliance':tmnxOesHwV14v0Compliance,'tmnxOesHwGroups':tmnxOesHwGroups,'tmnxOesHwV14v0Groups':tmnxOesHwV14v0Groups,_Ap:tmnxOesHwGroupV14v0,_Aq:tmnxOesHwNotifyObjsGroupV14v0,_Ar:tmnxOesHwNotificationGroupV14v0,'tmnxOesHwObjs':tmnxOesHwObjs,'tmnxOesChassisObjs':tmnxOesChassisObjs,'tmnxOesChassisTypeTable':tmnxOesChassisTypeTable,'tmnxOesChassisTypeEntry':tmnxOesChassisTypeEntry,_Z:tmnxOesChassisTypeIndex,_g:tmnxOesChassisTypeName,_h:tmnxOesChassisTypeDescription,_i:tmnxOesChassisTypeStatus,_j:tmnxOesChassisLastChange,'tmnxOesChassisTable':tmnxOesChassisTable,'tmnxOesChassisEntry':tmnxOesChassisEntry,_F:tmnxOesChassisNumber,_f:tmnxOesChassisRowStatus,_e:tmnxOesChassisRowLastChanged,_k:tmnxOesChassisAssignedType,_l:tmnxOesChassisEquippedType,_m:tmnxOesChassisActivitySwitch,_n:tmnxOesChassisHwEntryIndex,'tmnxOesPFTable':tmnxOesPFTable,'tmnxOesPFEntry':tmnxOesPFEntry,_J:tmnxOesSlotNumber,_o:tmnxOesPFType,_p:tmnxOesPFAmpRating,_q:tmnxOesPFInputCurrent,_r:tmnxOesPFInputVoltage,_s:tmnxOesPFInputPower,_t:tmnxOesPFClkA,_u:tmnxOesPFClkB,_v:tmnxOesPFClkDelta,_L:tmnxOesPFState,_w:tmnxOesPFHwIndex,_x:tmnxOesFanLastChg,'tmnxOesFanTable':tmnxOesFanTable,'tmnxOesFanEntry':tmnxOesFanEntry,_b:tmnxOesFanSlotNumber,_M:tmnxOesFanState,_y:tmnxOesFanSpeedControl,_z:tmnxOesFanHwIndex,'tmnxOesCardObjs':tmnxOesCardObjs,'tmnxOesCardTypeTable':tmnxOesCardTypeTable,'tmnxOesCardTypeEntry':tmnxOesCardTypeEntry,_U:tmnxOesCardTypeIndex,_A0:tmnxOesCardTypeName,_A1:tmnxOesCardTypeDescription,_A2:tmnxOesCardTypeStatus,_A3:tmnxOesCardTypeHeight,_A4:tmnxOesCardTypeWidth,_A5:tmnxOesCardTypeNumPorts,_A6:tmnxOesCardLastChange,'tmnxOesCardTable':tmnxOesCardTable,'tmnxOesCardEntry':tmnxOesCardEntry,_A7:tmnxOesCardAssignedType,_A8:tmnxOesCardEquippedType,_A9:tmnxOesCardSupportedTypes,_AA:tmnxOesCardReboot,_AB:tmnxOesCardHwEntryIndex,_AC:tmnxOesCardRowLastChanged,_AD:tmnxOesCardMemorySize,'tmnxOesControlCardTable':tmnxOesControlCardTable,'tmnxOesControlCardEntry':tmnxOesControlCardEntry,_AE:tmnxOesControlCardActState,_AF:tmnxOesControlCardHwIndex,'tmnxOesPortObjs':tmnxOesPortObjs,'tmnxOesCmnEqpPortTable':tmnxOesCmnEqpPortTable,'tmnxOesCmnEqpPortEntry':tmnxOesCmnEqpPortEntry,_V:tmnxOesCmnEqpPortNumber,_AG:tmnxOesCmnEqpPortCardType,_H:tmnxOesCmnEqpPortOperStatus,'tmnxOesCmnEqpPortTypeTable':tmnxOesCmnEqpPortTypeTable,'tmnxOesCmnEqpPortTypeEntry':tmnxOesCmnEqpPortTypeEntry,_AI:tmnxOesCmnEqpPortTypeName,_AH:tmnxOesCmnEqpPortTypeDescr,'tmnxOesHwNotifyObjs':tmnxOesHwNotifyObjs,_I:tmnxOesNotifyFailureReason,_W:tmnxOesPortNotifyError,'tmnxOesHwMIBNotifyPrefix':tmnxOesHwMIBNotifyPrefix,'tmnxOesHwNotifications':tmnxOesHwNotifications,_AJ:tmnxOesCtlCardPortDown,_AK:tmnxOesCtlCardPortUp,_AL:tmnxOesUsrpnlPortDown,_AM:tmnxOesUsrpnlPortUp,_AN:tmnxOesFanRemoved,_AO:tmnxOesFanInserted,_AP:tmnxOesFan32HReqd,_AQ:tmnxOesFan32HReqdClear,_AR:tmnxOesFanFailure,_AS:tmnxOesFanFailureClear,_AT:tmnxOesPowerSupplyRemoved,_AU:tmnxOesPowerSupplyInserted,_AV:tmnxOesPowerSupplyFailure,_AW:tmnxOesPowerSupplyFailureClear,_AX:tmnxOesPortError,_AY:tmnxOesPortErrorClear,_AZ:tmnxOesCtlCardActivityChange,_Aa:tmnxOesFpgaFail,_Ab:tmnxOesFpgaFailClear,_Ac:tmnxOesFpgaTimeout,_Ad:tmnxOesFpgaTimeoutClear,_Ae:tmnxOesOptTrnspndrMiscFail,_Af:tmnxOesCardDegraded,_Ag:tmnxOesFanSpeedHigh,_Ah:tmnxOesFanSpeedHighClear,_Ai:tmnxOesFanSpeedLow,_Aj:tmnxOesFanSpeedLowClear,_An:tmnxOesTempLow,_Ao:tmnxOesTempLowClear,_Ak:tmnxOesRedundancyFail,_Al:tmnxOesRedundancyReady,_Am:tmnxOesCardFirmwareErr})