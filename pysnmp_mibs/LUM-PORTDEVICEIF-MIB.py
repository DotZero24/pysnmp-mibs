_A9='portDevIfL2GroupV1'
_A8='portDevIfL1GroupV1'
_A7='portDevIfGeneralGroupV1'
_A6='portDevIfL2AutoNegotiationStatus'
_A5='portDevIfL2AutoNegotiation'
_A4='portDevIfL2InternalReference'
_A3='portDevIfL2NidPort'
_A2='portDevIfL2VlanId'
_A1='portDevIfL2LocalPort'
_A0='portDevIfL2Slot'
_z='portDevIfL2Subrack'
_y='portDevIfL2PortDevId'
_x='portDevIfL2Descr'
_w='portDevIfL2Name'
_v='portDevIfL1ReceivedPowerHigh'
_u='portDevIfL1ReceivedPowerLow'
_t='portDevIfL1TrxMissing'
_s='portDevIfL1LossOfSignal'
_r='portDevIfL1TrxClass'
_q='portDevIfL1RxHighPower'
_p='portDevIfL1TxPowerLevel'
_o='portDevIfL1PowerLevelLowRelativeThreshold'
_n='portDevIfL1PowerLevel'
_m='portDevIfL1ReceiverSensitivity'
_l='portDevIfL1TrxMedia'
_k='portDevIfL1SignalFormat'
_j='portDevIfL1ExpectedTxFrequency'
_i='portDevIfL1TxFrequency'
_h='portDevIfL1LaserTempActual'
_g='portDevIfL1LaserBias'
_f='portDevIfL1LaserStatus'
_e='portDevIfL1InternalReference'
_d='portDevIfL1NidPort'
_c='portDevIfL1VlanId'
_b='portDevIfL1LocalPort'
_a='portDevIfL1Slot'
_Z='portDevIfL1Subrack'
_Y='portDevIfL1PortDevId'
_X='portDevIfL1OperStatus'
_W='portDevIfL1AdminStatus'
_V='portDevIfL1Descr'
_U='portDevIfL1Name'
_T='portDevIfL2TableSize'
_S='portDevIfL1TableSize'
_R='portDevIfGeneralStateLastChangeTime'
_Q='portDevIfGeneralLastChangeTime'
_P='LumPortDeviceDuplexMode'
_O='LumPortDeviceInterfaceSpeed'
_N='TrxMedia'
_M='LambdaFrequency'
_L='BoardOrInterfaceOperStatus'
_K='AdminStatus'
_J='portDevIfL2Index'
_I='portDevIfIndex'
_H='Integer32'
_G='DisplayString'
_F='read-write'
_E='Unsigned32'
_D='read-create'
_C='read-only'
_B='LUM-PORTDEVICEIF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
lumModules,lumPortdeviceIfMIB=mibBuilder.importSymbols('LUM-REG','lumModules','lumPortdeviceIfMIB')
AdminStatus,BoardOrInterfaceOperStatus,FaultStatus,LambdaFrequency,MgmtNameString,OnOff,SlotNumber,SubrackNumber,TrxMedia=mibBuilder.importSymbols('LUM-TC',_K,_L,'FaultStatus',_M,'MgmtNameString','OnOff','SlotNumber','SubrackNumber',_N)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_G,'PhysAddress','TextualConvention')
lumPortdeviceIfMIBModule=ModuleIdentity((1,3,6,1,4,1,8708,1,1,58))
if mibBuilder.loadTexts:lumPortdeviceIfMIBModule.setRevisions(('2017-06-15 00:00','2013-05-31 00:00'))
class LumPortDeviceDuplexMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,254,255)));namedValues=NamedValues(*(('halfDuplex',0),('fullDuplex',1),('autoDuplex',2),('incomplete',3),('duplexNotAvailable',254),('duplexNotApplicable',255)))
class LumPortDeviceInterfaceSpeed(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('fastEthernet',0),('gbE',1)))
class LumPortDeviceMasterSlaveRole(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,254,255)));namedValues=NamedValues(*(('msMaster',0),('msSlave',1),('msAuto',2),('msNotAvailable',254),('msNotApplicable',255)))
class LumPortDeviceMdixMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,254,255)));namedValues=NamedValues(*(('mdi',0),('mdix',1),('mdiNotAvailable',254),('mdiNotApplicable',255)))
class LumPortDevicePauseMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,254,255)));namedValues=NamedValues(*(('pauseDisabled',0),('pauseEnabled',1),('pauseTxEnabledRxDisabled',2),('pauseTxDisabledRxEnabled',3),('pauseAuto',4),('pauseNotAvailable',254),('pauseNotApplicable',255)))
class LumPortDeviceInterface(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('interfaceNone',0),('ifNif',1),('ifCifA',2),('ifCifB',3)))
_LumPortdeviceIfConfs_ObjectIdentity=ObjectIdentity
lumPortdeviceIfConfs=_LumPortdeviceIfConfs_ObjectIdentity((1,3,6,1,4,1,8708,2,58,1))
_LumPortdeviceIfGroups_ObjectIdentity=ObjectIdentity
lumPortdeviceIfGroups=_LumPortdeviceIfGroups_ObjectIdentity((1,3,6,1,4,1,8708,2,58,1,1))
_LumPortdeviceIfCompl_ObjectIdentity=ObjectIdentity
lumPortdeviceIfCompl=_LumPortdeviceIfCompl_ObjectIdentity((1,3,6,1,4,1,8708,2,58,1,2))
_LumPortdeviceIfMIBObjects_ObjectIdentity=ObjectIdentity
lumPortdeviceIfMIBObjects=_LumPortdeviceIfMIBObjects_ObjectIdentity((1,3,6,1,4,1,8708,2,58,2))
_PortDevIfGeneral_ObjectIdentity=ObjectIdentity
portDevIfGeneral=_PortDevIfGeneral_ObjectIdentity((1,3,6,1,4,1,8708,2,58,2,1))
_PortDevIfGeneralLastChangeTime_Type=DateAndTime
_PortDevIfGeneralLastChangeTime_Object=MibScalar
portDevIfGeneralLastChangeTime=_PortDevIfGeneralLastChangeTime_Object((1,3,6,1,4,1,8708,2,58,2,1,1),_PortDevIfGeneralLastChangeTime_Type())
portDevIfGeneralLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevIfGeneralLastChangeTime.setStatus(_A)
_PortDevIfGeneralStateLastChangeTime_Type=DateAndTime
_PortDevIfGeneralStateLastChangeTime_Object=MibScalar
portDevIfGeneralStateLastChangeTime=_PortDevIfGeneralStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,58,2,1,2),_PortDevIfGeneralStateLastChangeTime_Type())
portDevIfGeneralStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevIfGeneralStateLastChangeTime.setStatus(_A)
_PortDevIfL1TableSize_Type=Unsigned32
_PortDevIfL1TableSize_Object=MibScalar
portDevIfL1TableSize=_PortDevIfL1TableSize_Object((1,3,6,1,4,1,8708,2,58,2,1,3),_PortDevIfL1TableSize_Type())
portDevIfL1TableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevIfL1TableSize.setStatus(_A)
_PortDevIfL2TableSize_Type=Unsigned32
_PortDevIfL2TableSize_Object=MibScalar
portDevIfL2TableSize=_PortDevIfL2TableSize_Object((1,3,6,1,4,1,8708,2,58,2,1,4),_PortDevIfL2TableSize_Type())
portDevIfL2TableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevIfL2TableSize.setStatus(_A)
_PortDevIfL1List_ObjectIdentity=ObjectIdentity
portDevIfL1List=_PortDevIfL1List_ObjectIdentity((1,3,6,1,4,1,8708,2,58,2,2))
_PortDevIfL1Table_Object=MibTable
portDevIfL1Table=_PortDevIfL1Table_Object((1,3,6,1,4,1,8708,2,58,2,2,1))
if mibBuilder.loadTexts:portDevIfL1Table.setStatus(_A)
_PortDevIfL1Entry_Object=MibTableRow
portDevIfL1Entry=_PortDevIfL1Entry_Object((1,3,6,1,4,1,8708,2,58,2,2,1,1))
portDevIfL1Entry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:portDevIfL1Entry.setStatus(_A)
_PortDevIfIndex_Type=InterfaceIndex
_PortDevIfIndex_Object=MibTableColumn
portDevIfIndex=_PortDevIfIndex_Object((1,3,6,1,4,1,8708,2,58,2,2,1,1,1),_PortDevIfIndex_Type())
portDevIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevIfIndex.setStatus(_A)
_PortDevIfL1Name_Type=MgmtNameString
_PortDevIfL1Name_Object=MibTableColumn
portDevIfL1Name=_PortDevIfL1Name_Object((1,3,6,1,4,1,8708,2,58,2,2,1,1,2),_PortDevIfL1Name_Type())
portDevIfL1Name.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevIfL1Name.setStatus(_A)
class _PortDevIfL1Descr_Type(DisplayString):defaultValue=OctetString('')
_PortDevIfL1Descr_Type.__name__=_G
_PortDevIfL1Descr_Object=MibTableColumn
portDevIfL1Descr=_PortDevIfL1Descr_Object((1,3,6,1,4,1,8708,2,58,2,2,1,1,3),_PortDevIfL1Descr_Type())
portDevIfL1Descr.setMaxAccess(_F)
if mibBuilder.loadTexts:portDevIfL1Descr.setStatus(_A)
class _PortDevIfL1AdminStatus_Type(AdminStatus):defaultValue=2
_PortDevIfL1AdminStatus_Type.__name__=_K
_PortDevIfL1AdminStatus_Object=MibTableColumn
portDevIfL1AdminStatus=_PortDevIfL1AdminStatus_Object((1,3,6,1,4,1,8708,2,58,2,2,1,1,4),_PortDevIfL1AdminStatus_Type())
portDevIfL1AdminStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:portDevIfL1AdminStatus.setStatus(_A)
class _PortDevIfL1OperStatus_Type(BoardOrInterfaceOperStatus):defaultValue=3
_PortDevIfL1OperStatus_Type.__name__=_L
_PortDevIfL1OperStatus_Object=MibTableColumn
portDevIfL1OperStatus=_PortDevIfL1OperStatus_Object((1,3,6,1,4,1,8708,2,58,2,2,1,1,5),_PortDevIfL1OperStatus_Type())
portDevIfL1OperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevIfL1OperStatus.setStatus(_A)
class _PortDevIfL1PortDevId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PortDevIfL1PortDevId_Type.__name__=_E
_PortDevIfL1PortDevId_Object=MibTableColumn
portDevIfL1PortDevId=_PortDevIfL1PortDevId_Object((1,3,6,1,4,1,8708,2,58,2,2,1,1,6),_PortDevIfL1PortDevId_Type())
portDevIfL1PortDevId.setMaxAccess(_D)
if mibBuilder.loadTexts:portDevIfL1PortDevId.setStatus(_A)
_PortDevIfL1Subrack_Type=SubrackNumber
_PortDevIfL1Subrack_Object=MibTableColumn
portDevIfL1Subrack=_PortDevIfL1Subrack_Object((1,3,6,1,4,1,8708,2,58,2,2,1,1,7),_PortDevIfL1Subrack_Type())
portDevIfL1Subrack.setMaxAccess(_D)
if mibBuilder.loadTexts:portDevIfL1Subrack.setStatus(_A)
_PortDevIfL1Slot_Type=SlotNumber
_PortDevIfL1Slot_Object=MibTableColumn
portDevIfL1Slot=_PortDevIfL1Slot_Object((1,3,6,1,4,1,8708,2,58,2,2,1,1,8),_PortDevIfL1Slot_Type())
portDevIfL1Slot.setMaxAccess(_D)
if mibBuilder.loadTexts:portDevIfL1Slot.setStatus(_A)
class _PortDevIfL1LocalPort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PortDevIfL1LocalPort_Type.__name__=_E
_PortDevIfL1LocalPort_Object=MibTableColumn
portDevIfL1LocalPort=_PortDevIfL1LocalPort_Object((1,3,6,1,4,1,8708,2,58,2,2,1,1,9),_PortDevIfL1LocalPort_Type())
portDevIfL1LocalPort.setMaxAccess(_D)
if mibBuilder.loadTexts:portDevIfL1LocalPort.setStatus(_A)
class _PortDevIfL1VlanId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_PortDevIfL1VlanId_Type.__name__=_E
_PortDevIfL1VlanId_Object=MibTableColumn
portDevIfL1VlanId=_PortDevIfL1VlanId_Object((1,3,6,1,4,1,8708,2,58,2,2,1,1,10),_PortDevIfL1VlanId_Type())
portDevIfL1VlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:portDevIfL1VlanId.setStatus(_A)
_PortDevIfL1NidPort_Type=LumPortDeviceInterface
_PortDevIfL1NidPort_Object=MibTableColumn
portDevIfL1NidPort=_PortDevIfL1NidPort_Object((1,3,6,1,4,1,8708,2,58,2,2,1,1,11),_PortDevIfL1NidPort_Type())
portDevIfL1NidPort.setMaxAccess(_D)
if mibBuilder.loadTexts:portDevIfL1NidPort.setStatus(_A)
class _PortDevIfL1InternalReference_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PortDevIfL1InternalReference_Type.__name__=_E
_PortDevIfL1InternalReference_Object=MibTableColumn
portDevIfL1InternalReference=_PortDevIfL1InternalReference_Object((1,3,6,1,4,1,8708,2,58,2,2,1,1,12),_PortDevIfL1InternalReference_Type())
portDevIfL1InternalReference.setMaxAccess(_D)
if mibBuilder.loadTexts:portDevIfL1InternalReference.setStatus(_A)
class _PortDevIfL1LaserStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('off',1),('on',2)))
_PortDevIfL1LaserStatus_Type.__name__=_H
_PortDevIfL1LaserStatus_Object=MibTableColumn
portDevIfL1LaserStatus=_PortDevIfL1LaserStatus_Object((1,3,6,1,4,1,8708,2,58,2,2,1,1,13),_PortDevIfL1LaserStatus_Type())
portDevIfL1LaserStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevIfL1LaserStatus.setStatus(_A)
_PortDevIfL1LaserBias_Type=Unsigned32
_PortDevIfL1LaserBias_Object=MibTableColumn
portDevIfL1LaserBias=_PortDevIfL1LaserBias_Object((1,3,6,1,4,1,8708,2,58,2,2,1,1,14),_PortDevIfL1LaserBias_Type())
portDevIfL1LaserBias.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevIfL1LaserBias.setStatus(_A)
_PortDevIfL1LaserTempActual_Type=Integer32
_PortDevIfL1LaserTempActual_Object=MibTableColumn
portDevIfL1LaserTempActual=_PortDevIfL1LaserTempActual_Object((1,3,6,1,4,1,8708,2,58,2,2,1,1,15),_PortDevIfL1LaserTempActual_Type())
portDevIfL1LaserTempActual.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevIfL1LaserTempActual.setStatus(_A)
_PortDevIfL1TxFrequency_Type=LambdaFrequency
_PortDevIfL1TxFrequency_Object=MibTableColumn
portDevIfL1TxFrequency=_PortDevIfL1TxFrequency_Object((1,3,6,1,4,1,8708,2,58,2,2,1,1,16),_PortDevIfL1TxFrequency_Type())
portDevIfL1TxFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevIfL1TxFrequency.setStatus(_A)
class _PortDevIfL1ExpectedTxFrequency_Type(LambdaFrequency):defaultValue=0
_PortDevIfL1ExpectedTxFrequency_Type.__name__=_M
_PortDevIfL1ExpectedTxFrequency_Object=MibTableColumn
portDevIfL1ExpectedTxFrequency=_PortDevIfL1ExpectedTxFrequency_Object((1,3,6,1,4,1,8708,2,58,2,2,1,1,17),_PortDevIfL1ExpectedTxFrequency_Type())
portDevIfL1ExpectedTxFrequency.setMaxAccess(_F)
if mibBuilder.loadTexts:portDevIfL1ExpectedTxFrequency.setStatus(_A)
class _PortDevIfL1SignalFormat_Type(LumPortDeviceInterfaceSpeed):defaultValue=1
_PortDevIfL1SignalFormat_Type.__name__=_O
_PortDevIfL1SignalFormat_Object=MibTableColumn
portDevIfL1SignalFormat=_PortDevIfL1SignalFormat_Object((1,3,6,1,4,1,8708,2,58,2,2,1,1,18),_PortDevIfL1SignalFormat_Type())
portDevIfL1SignalFormat.setMaxAccess(_F)
if mibBuilder.loadTexts:portDevIfL1SignalFormat.setStatus(_A)
class _PortDevIfL1TrxMedia_Type(TrxMedia):defaultValue=1
_PortDevIfL1TrxMedia_Type.__name__=_N
_PortDevIfL1TrxMedia_Object=MibTableColumn
portDevIfL1TrxMedia=_PortDevIfL1TrxMedia_Object((1,3,6,1,4,1,8708,2,58,2,2,1,1,19),_PortDevIfL1TrxMedia_Type())
portDevIfL1TrxMedia.setMaxAccess(_D)
if mibBuilder.loadTexts:portDevIfL1TrxMedia.setStatus(_A)
_PortDevIfL1ReceiverSensitivity_Type=Integer32
_PortDevIfL1ReceiverSensitivity_Object=MibTableColumn
portDevIfL1ReceiverSensitivity=_PortDevIfL1ReceiverSensitivity_Object((1,3,6,1,4,1,8708,2,58,2,2,1,1,20),_PortDevIfL1ReceiverSensitivity_Type())
portDevIfL1ReceiverSensitivity.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevIfL1ReceiverSensitivity.setStatus(_A)
_PortDevIfL1PowerLevel_Type=Integer32
_PortDevIfL1PowerLevel_Object=MibTableColumn
portDevIfL1PowerLevel=_PortDevIfL1PowerLevel_Object((1,3,6,1,4,1,8708,2,58,2,2,1,1,21),_PortDevIfL1PowerLevel_Type())
portDevIfL1PowerLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevIfL1PowerLevel.setStatus(_A)
class _PortDevIfL1PowerLevelLowRelativeThreshold_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-50,100))
_PortDevIfL1PowerLevelLowRelativeThreshold_Type.__name__=_H
_PortDevIfL1PowerLevelLowRelativeThreshold_Object=MibTableColumn
portDevIfL1PowerLevelLowRelativeThreshold=_PortDevIfL1PowerLevelLowRelativeThreshold_Object((1,3,6,1,4,1,8708,2,58,2,2,1,1,22),_PortDevIfL1PowerLevelLowRelativeThreshold_Type())
portDevIfL1PowerLevelLowRelativeThreshold.setMaxAccess(_F)
if mibBuilder.loadTexts:portDevIfL1PowerLevelLowRelativeThreshold.setStatus(_A)
_PortDevIfL1TxPowerLevel_Type=Integer32
_PortDevIfL1TxPowerLevel_Object=MibTableColumn
portDevIfL1TxPowerLevel=_PortDevIfL1TxPowerLevel_Object((1,3,6,1,4,1,8708,2,58,2,2,1,1,23),_PortDevIfL1TxPowerLevel_Type())
portDevIfL1TxPowerLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevIfL1TxPowerLevel.setStatus(_A)
_PortDevIfL1RxHighPower_Type=Integer32
_PortDevIfL1RxHighPower_Object=MibTableColumn
portDevIfL1RxHighPower=_PortDevIfL1RxHighPower_Object((1,3,6,1,4,1,8708,2,58,2,2,1,1,24),_PortDevIfL1RxHighPower_Type())
portDevIfL1RxHighPower.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevIfL1RxHighPower.setStatus(_A)
class _PortDevIfL1TrxClass_Type(DisplayString):defaultValue=OctetString('')
_PortDevIfL1TrxClass_Type.__name__=_G
_PortDevIfL1TrxClass_Object=MibTableColumn
portDevIfL1TrxClass=_PortDevIfL1TrxClass_Object((1,3,6,1,4,1,8708,2,58,2,2,1,1,25),_PortDevIfL1TrxClass_Type())
portDevIfL1TrxClass.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevIfL1TrxClass.setStatus(_A)
_PortDevIfL1LossOfSignal_Type=FaultStatus
_PortDevIfL1LossOfSignal_Object=MibTableColumn
portDevIfL1LossOfSignal=_PortDevIfL1LossOfSignal_Object((1,3,6,1,4,1,8708,2,58,2,2,1,1,26),_PortDevIfL1LossOfSignal_Type())
portDevIfL1LossOfSignal.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevIfL1LossOfSignal.setStatus(_A)
_PortDevIfL1TrxMissing_Type=FaultStatus
_PortDevIfL1TrxMissing_Object=MibTableColumn
portDevIfL1TrxMissing=_PortDevIfL1TrxMissing_Object((1,3,6,1,4,1,8708,2,58,2,2,1,1,27),_PortDevIfL1TrxMissing_Type())
portDevIfL1TrxMissing.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevIfL1TrxMissing.setStatus(_A)
_PortDevIfL1ReceivedPowerLow_Type=FaultStatus
_PortDevIfL1ReceivedPowerLow_Object=MibTableColumn
portDevIfL1ReceivedPowerLow=_PortDevIfL1ReceivedPowerLow_Object((1,3,6,1,4,1,8708,2,58,2,2,1,1,28),_PortDevIfL1ReceivedPowerLow_Type())
portDevIfL1ReceivedPowerLow.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevIfL1ReceivedPowerLow.setStatus(_A)
_PortDevIfL1ReceivedPowerHigh_Type=FaultStatus
_PortDevIfL1ReceivedPowerHigh_Object=MibTableColumn
portDevIfL1ReceivedPowerHigh=_PortDevIfL1ReceivedPowerHigh_Object((1,3,6,1,4,1,8708,2,58,2,2,1,1,29),_PortDevIfL1ReceivedPowerHigh_Type())
portDevIfL1ReceivedPowerHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevIfL1ReceivedPowerHigh.setStatus(_A)
_PortDevIfL2List_ObjectIdentity=ObjectIdentity
portDevIfL2List=_PortDevIfL2List_ObjectIdentity((1,3,6,1,4,1,8708,2,58,2,3))
_PortDevIfL2Table_Object=MibTable
portDevIfL2Table=_PortDevIfL2Table_Object((1,3,6,1,4,1,8708,2,58,2,3,1))
if mibBuilder.loadTexts:portDevIfL2Table.setStatus(_A)
_PortDevIfL2Entry_Object=MibTableRow
portDevIfL2Entry=_PortDevIfL2Entry_Object((1,3,6,1,4,1,8708,2,58,2,3,1,1))
portDevIfL2Entry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:portDevIfL2Entry.setStatus(_A)
_PortDevIfL2Index_Type=InterfaceIndex
_PortDevIfL2Index_Object=MibTableColumn
portDevIfL2Index=_PortDevIfL2Index_Object((1,3,6,1,4,1,8708,2,58,2,3,1,1,1),_PortDevIfL2Index_Type())
portDevIfL2Index.setMaxAccess(_D)
if mibBuilder.loadTexts:portDevIfL2Index.setStatus(_A)
_PortDevIfL2Name_Type=MgmtNameString
_PortDevIfL2Name_Object=MibTableColumn
portDevIfL2Name=_PortDevIfL2Name_Object((1,3,6,1,4,1,8708,2,58,2,3,1,1,2),_PortDevIfL2Name_Type())
portDevIfL2Name.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevIfL2Name.setStatus(_A)
class _PortDevIfL2Descr_Type(DisplayString):defaultValue=OctetString('')
_PortDevIfL2Descr_Type.__name__=_G
_PortDevIfL2Descr_Object=MibTableColumn
portDevIfL2Descr=_PortDevIfL2Descr_Object((1,3,6,1,4,1,8708,2,58,2,3,1,1,3),_PortDevIfL2Descr_Type())
portDevIfL2Descr.setMaxAccess(_F)
if mibBuilder.loadTexts:portDevIfL2Descr.setStatus(_A)
class _PortDevIfL2PortDevId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PortDevIfL2PortDevId_Type.__name__=_E
_PortDevIfL2PortDevId_Object=MibTableColumn
portDevIfL2PortDevId=_PortDevIfL2PortDevId_Object((1,3,6,1,4,1,8708,2,58,2,3,1,1,4),_PortDevIfL2PortDevId_Type())
portDevIfL2PortDevId.setMaxAccess(_D)
if mibBuilder.loadTexts:portDevIfL2PortDevId.setStatus(_A)
_PortDevIfL2Subrack_Type=SubrackNumber
_PortDevIfL2Subrack_Object=MibTableColumn
portDevIfL2Subrack=_PortDevIfL2Subrack_Object((1,3,6,1,4,1,8708,2,58,2,3,1,1,5),_PortDevIfL2Subrack_Type())
portDevIfL2Subrack.setMaxAccess(_D)
if mibBuilder.loadTexts:portDevIfL2Subrack.setStatus(_A)
_PortDevIfL2Slot_Type=SlotNumber
_PortDevIfL2Slot_Object=MibTableColumn
portDevIfL2Slot=_PortDevIfL2Slot_Object((1,3,6,1,4,1,8708,2,58,2,3,1,1,6),_PortDevIfL2Slot_Type())
portDevIfL2Slot.setMaxAccess(_D)
if mibBuilder.loadTexts:portDevIfL2Slot.setStatus(_A)
class _PortDevIfL2LocalPort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PortDevIfL2LocalPort_Type.__name__=_E
_PortDevIfL2LocalPort_Object=MibTableColumn
portDevIfL2LocalPort=_PortDevIfL2LocalPort_Object((1,3,6,1,4,1,8708,2,58,2,3,1,1,7),_PortDevIfL2LocalPort_Type())
portDevIfL2LocalPort.setMaxAccess(_D)
if mibBuilder.loadTexts:portDevIfL2LocalPort.setStatus(_A)
class _PortDevIfL2VlanId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_PortDevIfL2VlanId_Type.__name__=_E
_PortDevIfL2VlanId_Object=MibTableColumn
portDevIfL2VlanId=_PortDevIfL2VlanId_Object((1,3,6,1,4,1,8708,2,58,2,3,1,1,8),_PortDevIfL2VlanId_Type())
portDevIfL2VlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:portDevIfL2VlanId.setStatus(_A)
_PortDevIfL2NidPort_Type=LumPortDeviceInterface
_PortDevIfL2NidPort_Object=MibTableColumn
portDevIfL2NidPort=_PortDevIfL2NidPort_Object((1,3,6,1,4,1,8708,2,58,2,3,1,1,9),_PortDevIfL2NidPort_Type())
portDevIfL2NidPort.setMaxAccess(_D)
if mibBuilder.loadTexts:portDevIfL2NidPort.setStatus(_A)
class _PortDevIfL2InternalReference_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PortDevIfL2InternalReference_Type.__name__=_E
_PortDevIfL2InternalReference_Object=MibTableColumn
portDevIfL2InternalReference=_PortDevIfL2InternalReference_Object((1,3,6,1,4,1,8708,2,58,2,3,1,1,10),_PortDevIfL2InternalReference_Type())
portDevIfL2InternalReference.setMaxAccess(_D)
if mibBuilder.loadTexts:portDevIfL2InternalReference.setStatus(_A)
class _PortDevIfL2AutoNegotiation_Type(OnOff):defaultValue=2
_PortDevIfL2AutoNegotiation_Type.__name__='OnOff'
_PortDevIfL2AutoNegotiation_Object=MibTableColumn
portDevIfL2AutoNegotiation=_PortDevIfL2AutoNegotiation_Object((1,3,6,1,4,1,8708,2,58,2,3,1,1,11),_PortDevIfL2AutoNegotiation_Type())
portDevIfL2AutoNegotiation.setMaxAccess(_F)
if mibBuilder.loadTexts:portDevIfL2AutoNegotiation.setStatus(_A)
class _PortDevIfL2AutoNegotiationStatus_Type(LumPortDeviceDuplexMode):defaultValue=3
_PortDevIfL2AutoNegotiationStatus_Type.__name__=_P
_PortDevIfL2AutoNegotiationStatus_Object=MibTableColumn
portDevIfL2AutoNegotiationStatus=_PortDevIfL2AutoNegotiationStatus_Object((1,3,6,1,4,1,8708,2,58,2,3,1,1,12),_PortDevIfL2AutoNegotiationStatus_Type())
portDevIfL2AutoNegotiationStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevIfL2AutoNegotiationStatus.setStatus(_A)
portDevIfGeneralGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,58,1,1,1))
portDevIfGeneralGroupV1.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:portDevIfGeneralGroupV1.setStatus(_A)
portDevIfL1GroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,58,1,1,2))
portDevIfL1GroupV1.setObjects(*((_B,_I),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v)))
if mibBuilder.loadTexts:portDevIfL1GroupV1.setStatus(_A)
portDevIfL2GroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,58,1,1,3))
portDevIfL2GroupV1.setObjects(*((_B,_J),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6)))
if mibBuilder.loadTexts:portDevIfL2GroupV1.setStatus(_A)
lumPortDeviceBasicComplV1=ModuleCompliance((1,3,6,1,4,1,8708,2,58,1,2,1))
lumPortDeviceBasicComplV1.setObjects(*((_B,_A7),(_B,_A8),(_B,_A9)))
if mibBuilder.loadTexts:lumPortDeviceBasicComplV1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_P:LumPortDeviceDuplexMode,_O:LumPortDeviceInterfaceSpeed,'LumPortDeviceMasterSlaveRole':LumPortDeviceMasterSlaveRole,'LumPortDeviceMdixMode':LumPortDeviceMdixMode,'LumPortDevicePauseMode':LumPortDevicePauseMode,'LumPortDeviceInterface':LumPortDeviceInterface,'lumPortdeviceIfMIBModule':lumPortdeviceIfMIBModule,'lumPortdeviceIfConfs':lumPortdeviceIfConfs,'lumPortdeviceIfGroups':lumPortdeviceIfGroups,_A7:portDevIfGeneralGroupV1,_A8:portDevIfL1GroupV1,_A9:portDevIfL2GroupV1,'lumPortdeviceIfCompl':lumPortdeviceIfCompl,'lumPortDeviceBasicComplV1':lumPortDeviceBasicComplV1,'lumPortdeviceIfMIBObjects':lumPortdeviceIfMIBObjects,'portDevIfGeneral':portDevIfGeneral,_Q:portDevIfGeneralLastChangeTime,_R:portDevIfGeneralStateLastChangeTime,_S:portDevIfL1TableSize,_T:portDevIfL2TableSize,'portDevIfL1List':portDevIfL1List,'portDevIfL1Table':portDevIfL1Table,'portDevIfL1Entry':portDevIfL1Entry,_I:portDevIfIndex,_U:portDevIfL1Name,_V:portDevIfL1Descr,_W:portDevIfL1AdminStatus,_X:portDevIfL1OperStatus,_Y:portDevIfL1PortDevId,_Z:portDevIfL1Subrack,_a:portDevIfL1Slot,_b:portDevIfL1LocalPort,_c:portDevIfL1VlanId,_d:portDevIfL1NidPort,_e:portDevIfL1InternalReference,_f:portDevIfL1LaserStatus,_g:portDevIfL1LaserBias,_h:portDevIfL1LaserTempActual,_i:portDevIfL1TxFrequency,_j:portDevIfL1ExpectedTxFrequency,_k:portDevIfL1SignalFormat,_l:portDevIfL1TrxMedia,_m:portDevIfL1ReceiverSensitivity,_n:portDevIfL1PowerLevel,_o:portDevIfL1PowerLevelLowRelativeThreshold,_p:portDevIfL1TxPowerLevel,_q:portDevIfL1RxHighPower,_r:portDevIfL1TrxClass,_s:portDevIfL1LossOfSignal,_t:portDevIfL1TrxMissing,_u:portDevIfL1ReceivedPowerLow,_v:portDevIfL1ReceivedPowerHigh,'portDevIfL2List':portDevIfL2List,'portDevIfL2Table':portDevIfL2Table,'portDevIfL2Entry':portDevIfL2Entry,_J:portDevIfL2Index,_w:portDevIfL2Name,_x:portDevIfL2Descr,_y:portDevIfL2PortDevId,_z:portDevIfL2Subrack,_A0:portDevIfL2Slot,_A1:portDevIfL2LocalPort,_A2:portDevIfL2VlanId,_A3:portDevIfL2NidPort,_A4:portDevIfL2InternalReference,_A5:portDevIfL2AutoNegotiation,_A6:portDevIfL2AutoNegotiationStatus})