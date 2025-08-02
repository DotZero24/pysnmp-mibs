_AF='ocmIfGroupV4'
_AE='ocmIfGroupV2'
_AD='ocmIfHighInputPower'
_AC='ocmIfSpacingMode'
_AB='ocmChannelSaveReference'
_AA='ocmChannelReferenceTime'
_A9='ocmGeneralOcmIfTableSize'
_A8='ocmGeneralStateLastChangeTime'
_A7='ocmGeneralLastChangeTime'
_A6='read-write'
_A5='DisplayString'
_A4='SubrackNumber'
_A3='SlotNumber'
_A2='BoardOrInterfaceOperStatus'
_A1='BoardOrInterfaceAdminStatus'
_A0='ocmChannelGroupV2'
_z='ocmIfGroupV3'
_y='ocmIfGroup'
_x='ocmIfPowerOffsetAdjustment'
_w='ocmChannelReferencePowerLevel'
_v='ocmChannelOcmRefIfIndex'
_u='ocmChannelUpdateLastChangeTime'
_t='ocmChannelPowerLevel'
_s='ocmChannelFrequency'
_r='ocmChannelName'
_q='PortNumber'
_p='ocmChannelGroup'
_o='ocmIfChangePowerOffset'
_n='ocmIfChangePowerThreshold'
_m='ocmChannelIndex'
_l='ocmIfDeltaPower'
_k='ocmIfMinPowerLevel'
_j='ocmIfMaxPowerLevel'
_i='ocmIfChangeConnectedBoardType'
_h='ocmIfConnectedBoardType'
_g='ocmIfPowerOffset'
_f='ocmIfSaveReference'
_e='ocmIfChangeConnectedPort'
_d='ocmIfConfigurationCommand'
_c='ocmIfModuleFailure'
_b='ocmIfCommissioningMode'
_a='ocmIfDataSourceNotDefined'
_Z='ocmIfSwitchFailure'
_Y='ocmIfReferenceTime'
_X='ocmIfControlMode'
_W='ocmIfActivePort'
_V='ocmIfConnectedPort'
_U='ocmIfConnectedSlot'
_T='ocmIfConnectedSubrack'
_S='ocmIfUpdateLastChangeTime'
_R='ocmIfPowerThreshold'
_Q='ocmIfOperStatus'
_P='ocmIfAdminStatus'
_O='ocmIfInvPhysIndexOrZero'
_N='ocmIfRxPort'
_M='ocmIfSlot'
_L='ocmIfSubrack'
_K='ocmIfDescr'
_J='ocmIfName'
_I='Unsigned32'
_H='ocmIfIndex'
_G='ocmGeneralGroup'
_F='deprecated'
_E='Integer32'
_D='read-create'
_C='read-only'
_B='current'
_A='LUM-OCM-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lumModules,lumOcmMIB=mibBuilder.importSymbols('LUM-REG','lumModules','lumOcmMIB')
BoardOrInterfaceAdminStatus,BoardOrInterfaceOperStatus,CommandString,FaultStatus,LambdaFrequency,MgmtNameString,PortNumber,SlotNumber,SubrackNumber=mibBuilder.importSymbols('LUM-TC',_A1,_A2,'CommandString','FaultStatus','LambdaFrequency','MgmtNameString',_q,_A3,_A4)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_A5,'PhysAddress','TextualConvention')
lumOcmMIBModule=ModuleIdentity((1,3,6,1,4,1,8708,1,1,33))
if mibBuilder.loadTexts:lumOcmMIBModule.setRevisions(('2018-06-15 00:00','2017-12-15 00:00','2017-06-15 00:00','2016-01-11 00:00','2014-05-16 00:00','2008-01-16 00:00'))
_LumOcmConfs_ObjectIdentity=ObjectIdentity
lumOcmConfs=_LumOcmConfs_ObjectIdentity((1,3,6,1,4,1,8708,2,33,1))
_LumOcmGroups_ObjectIdentity=ObjectIdentity
lumOcmGroups=_LumOcmGroups_ObjectIdentity((1,3,6,1,4,1,8708,2,33,1,1))
_LumOcmCompl_ObjectIdentity=ObjectIdentity
lumOcmCompl=_LumOcmCompl_ObjectIdentity((1,3,6,1,4,1,8708,2,33,1,2))
_LumOcmMinimalGroups_ObjectIdentity=ObjectIdentity
lumOcmMinimalGroups=_LumOcmMinimalGroups_ObjectIdentity((1,3,6,1,4,1,8708,2,33,1,3))
_LumOcmMinimalCompl_ObjectIdentity=ObjectIdentity
lumOcmMinimalCompl=_LumOcmMinimalCompl_ObjectIdentity((1,3,6,1,4,1,8708,2,33,1,4))
_LumOcmMIBObjects_ObjectIdentity=ObjectIdentity
lumOcmMIBObjects=_LumOcmMIBObjects_ObjectIdentity((1,3,6,1,4,1,8708,2,33,2))
_OcmGeneral_ObjectIdentity=ObjectIdentity
ocmGeneral=_OcmGeneral_ObjectIdentity((1,3,6,1,4,1,8708,2,33,2,1))
_OcmGeneralLastChangeTime_Type=DateAndTime
_OcmGeneralLastChangeTime_Object=MibScalar
ocmGeneralLastChangeTime=_OcmGeneralLastChangeTime_Object((1,3,6,1,4,1,8708,2,33,2,1,1),_OcmGeneralLastChangeTime_Type())
ocmGeneralLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ocmGeneralLastChangeTime.setStatus(_B)
_OcmGeneralStateLastChangeTime_Type=DateAndTime
_OcmGeneralStateLastChangeTime_Object=MibScalar
ocmGeneralStateLastChangeTime=_OcmGeneralStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,33,2,1,2),_OcmGeneralStateLastChangeTime_Type())
ocmGeneralStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ocmGeneralStateLastChangeTime.setStatus(_B)
_OcmGeneralOcmIfTableSize_Type=Unsigned32
_OcmGeneralOcmIfTableSize_Object=MibScalar
ocmGeneralOcmIfTableSize=_OcmGeneralOcmIfTableSize_Object((1,3,6,1,4,1,8708,2,33,2,1,3),_OcmGeneralOcmIfTableSize_Type())
ocmGeneralOcmIfTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:ocmGeneralOcmIfTableSize.setStatus(_B)
_OcmGeneralOcmChannelTableSize_Type=Unsigned32
_OcmGeneralOcmChannelTableSize_Object=MibScalar
ocmGeneralOcmChannelTableSize=_OcmGeneralOcmChannelTableSize_Object((1,3,6,1,4,1,8708,2,33,2,1,4),_OcmGeneralOcmChannelTableSize_Type())
ocmGeneralOcmChannelTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:ocmGeneralOcmChannelTableSize.setStatus(_B)
_OcmIfList_ObjectIdentity=ObjectIdentity
ocmIfList=_OcmIfList_ObjectIdentity((1,3,6,1,4,1,8708,2,33,2,2))
_OcmIfTable_Object=MibTable
ocmIfTable=_OcmIfTable_Object((1,3,6,1,4,1,8708,2,33,2,2,1))
if mibBuilder.loadTexts:ocmIfTable.setStatus(_B)
_OcmIfEntry_Object=MibTableRow
ocmIfEntry=_OcmIfEntry_Object((1,3,6,1,4,1,8708,2,33,2,2,1,1))
ocmIfEntry.setIndexNames((0,_A,_H))
if mibBuilder.loadTexts:ocmIfEntry.setStatus(_B)
class _OcmIfIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_OcmIfIndex_Type.__name__=_I
_OcmIfIndex_Object=MibTableColumn
ocmIfIndex=_OcmIfIndex_Object((1,3,6,1,4,1,8708,2,33,2,2,1,1,1),_OcmIfIndex_Type())
ocmIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ocmIfIndex.setStatus(_B)
_OcmIfName_Type=MgmtNameString
_OcmIfName_Object=MibTableColumn
ocmIfName=_OcmIfName_Object((1,3,6,1,4,1,8708,2,33,2,2,1,1,2),_OcmIfName_Type())
ocmIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:ocmIfName.setStatus(_B)
class _OcmIfDescr_Type(DisplayString):defaultValue=OctetString('')
_OcmIfDescr_Type.__name__=_A5
_OcmIfDescr_Object=MibTableColumn
ocmIfDescr=_OcmIfDescr_Object((1,3,6,1,4,1,8708,2,33,2,2,1,1,3),_OcmIfDescr_Type())
ocmIfDescr.setMaxAccess(_A6)
if mibBuilder.loadTexts:ocmIfDescr.setStatus(_B)
_OcmIfSubrack_Type=SubrackNumber
_OcmIfSubrack_Object=MibTableColumn
ocmIfSubrack=_OcmIfSubrack_Object((1,3,6,1,4,1,8708,2,33,2,2,1,1,4),_OcmIfSubrack_Type())
ocmIfSubrack.setMaxAccess(_D)
if mibBuilder.loadTexts:ocmIfSubrack.setStatus(_B)
_OcmIfSlot_Type=SlotNumber
_OcmIfSlot_Object=MibTableColumn
ocmIfSlot=_OcmIfSlot_Object((1,3,6,1,4,1,8708,2,33,2,2,1,1,5),_OcmIfSlot_Type())
ocmIfSlot.setMaxAccess(_D)
if mibBuilder.loadTexts:ocmIfSlot.setStatus(_B)
_OcmIfRxPort_Type=PortNumber
_OcmIfRxPort_Object=MibTableColumn
ocmIfRxPort=_OcmIfRxPort_Object((1,3,6,1,4,1,8708,2,33,2,2,1,1,6),_OcmIfRxPort_Type())
ocmIfRxPort.setMaxAccess(_D)
if mibBuilder.loadTexts:ocmIfRxPort.setStatus(_B)
class _OcmIfInvPhysIndexOrZero_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_OcmIfInvPhysIndexOrZero_Type.__name__=_I
_OcmIfInvPhysIndexOrZero_Object=MibTableColumn
ocmIfInvPhysIndexOrZero=_OcmIfInvPhysIndexOrZero_Object((1,3,6,1,4,1,8708,2,33,2,2,1,1,7),_OcmIfInvPhysIndexOrZero_Type())
ocmIfInvPhysIndexOrZero.setMaxAccess(_C)
if mibBuilder.loadTexts:ocmIfInvPhysIndexOrZero.setStatus(_B)
class _OcmIfAdminStatus_Type(BoardOrInterfaceAdminStatus):defaultValue=3
_OcmIfAdminStatus_Type.__name__=_A1
_OcmIfAdminStatus_Object=MibTableColumn
ocmIfAdminStatus=_OcmIfAdminStatus_Object((1,3,6,1,4,1,8708,2,33,2,2,1,1,8),_OcmIfAdminStatus_Type())
ocmIfAdminStatus.setMaxAccess(_A6)
if mibBuilder.loadTexts:ocmIfAdminStatus.setStatus(_B)
class _OcmIfOperStatus_Type(BoardOrInterfaceOperStatus):defaultValue=1
_OcmIfOperStatus_Type.__name__=_A2
_OcmIfOperStatus_Object=MibTableColumn
ocmIfOperStatus=_OcmIfOperStatus_Object((1,3,6,1,4,1,8708,2,33,2,2,1,1,9),_OcmIfOperStatus_Type())
ocmIfOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ocmIfOperStatus.setStatus(_B)
class _OcmIfPowerThreshold_Type(Integer32):defaultValue=-24;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-50,100))
_OcmIfPowerThreshold_Type.__name__=_E
_OcmIfPowerThreshold_Object=MibTableColumn
ocmIfPowerThreshold=_OcmIfPowerThreshold_Object((1,3,6,1,4,1,8708,2,33,2,2,1,1,12),_OcmIfPowerThreshold_Type())
ocmIfPowerThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:ocmIfPowerThreshold.setStatus(_B)
_OcmIfUpdateLastChangeTime_Type=DateAndTime
_OcmIfUpdateLastChangeTime_Object=MibTableColumn
ocmIfUpdateLastChangeTime=_OcmIfUpdateLastChangeTime_Object((1,3,6,1,4,1,8708,2,33,2,2,1,1,13),_OcmIfUpdateLastChangeTime_Type())
ocmIfUpdateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ocmIfUpdateLastChangeTime.setStatus(_B)
class _OcmIfConnectedSubrack_Type(SubrackNumber):defaultValue=0
_OcmIfConnectedSubrack_Type.__name__=_A4
_OcmIfConnectedSubrack_Object=MibTableColumn
ocmIfConnectedSubrack=_OcmIfConnectedSubrack_Object((1,3,6,1,4,1,8708,2,33,2,2,1,1,14),_OcmIfConnectedSubrack_Type())
ocmIfConnectedSubrack.setMaxAccess(_D)
if mibBuilder.loadTexts:ocmIfConnectedSubrack.setStatus(_B)
class _OcmIfConnectedSlot_Type(SlotNumber):defaultValue=0
_OcmIfConnectedSlot_Type.__name__=_A3
_OcmIfConnectedSlot_Object=MibTableColumn
ocmIfConnectedSlot=_OcmIfConnectedSlot_Object((1,3,6,1,4,1,8708,2,33,2,2,1,1,15),_OcmIfConnectedSlot_Type())
ocmIfConnectedSlot.setMaxAccess(_D)
if mibBuilder.loadTexts:ocmIfConnectedSlot.setStatus(_B)
class _OcmIfConnectedPort_Type(PortNumber):defaultValue=0
_OcmIfConnectedPort_Type.__name__=_q
_OcmIfConnectedPort_Object=MibTableColumn
ocmIfConnectedPort=_OcmIfConnectedPort_Object((1,3,6,1,4,1,8708,2,33,2,2,1,1,16),_OcmIfConnectedPort_Type())
ocmIfConnectedPort.setMaxAccess(_D)
if mibBuilder.loadTexts:ocmIfConnectedPort.setStatus(_B)
class _OcmIfActivePort_Type(PortNumber):defaultValue=1
_OcmIfActivePort_Type.__name__=_q
_OcmIfActivePort_Object=MibTableColumn
ocmIfActivePort=_OcmIfActivePort_Object((1,3,6,1,4,1,8708,2,33,2,2,1,1,17),_OcmIfActivePort_Type())
ocmIfActivePort.setMaxAccess(_C)
if mibBuilder.loadTexts:ocmIfActivePort.setStatus(_B)
class _OcmIfControlMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('normal',1),('commissioning',2)))
_OcmIfControlMode_Type.__name__=_E
_OcmIfControlMode_Object=MibTableColumn
ocmIfControlMode=_OcmIfControlMode_Object((1,3,6,1,4,1,8708,2,33,2,2,1,1,18),_OcmIfControlMode_Type())
ocmIfControlMode.setMaxAccess(_C)
if mibBuilder.loadTexts:ocmIfControlMode.setStatus(_B)
_OcmIfReferenceTime_Type=DisplayString
_OcmIfReferenceTime_Object=MibTableColumn
ocmIfReferenceTime=_OcmIfReferenceTime_Object((1,3,6,1,4,1,8708,2,33,2,2,1,1,21),_OcmIfReferenceTime_Type())
ocmIfReferenceTime.setMaxAccess(_D)
if mibBuilder.loadTexts:ocmIfReferenceTime.setStatus(_B)
_OcmIfSwitchFailure_Type=FaultStatus
_OcmIfSwitchFailure_Object=MibTableColumn
ocmIfSwitchFailure=_OcmIfSwitchFailure_Object((1,3,6,1,4,1,8708,2,33,2,2,1,1,22),_OcmIfSwitchFailure_Type())
ocmIfSwitchFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:ocmIfSwitchFailure.setStatus(_B)
_OcmIfDataSourceNotDefined_Type=FaultStatus
_OcmIfDataSourceNotDefined_Object=MibTableColumn
ocmIfDataSourceNotDefined=_OcmIfDataSourceNotDefined_Object((1,3,6,1,4,1,8708,2,33,2,2,1,1,23),_OcmIfDataSourceNotDefined_Type())
ocmIfDataSourceNotDefined.setMaxAccess(_C)
if mibBuilder.loadTexts:ocmIfDataSourceNotDefined.setStatus(_B)
_OcmIfCommissioningMode_Type=FaultStatus
_OcmIfCommissioningMode_Object=MibTableColumn
ocmIfCommissioningMode=_OcmIfCommissioningMode_Object((1,3,6,1,4,1,8708,2,33,2,2,1,1,24),_OcmIfCommissioningMode_Type())
ocmIfCommissioningMode.setMaxAccess(_C)
if mibBuilder.loadTexts:ocmIfCommissioningMode.setStatus(_B)
_OcmIfModuleFailure_Type=FaultStatus
_OcmIfModuleFailure_Object=MibTableColumn
ocmIfModuleFailure=_OcmIfModuleFailure_Object((1,3,6,1,4,1,8708,2,33,2,2,1,1,25),_OcmIfModuleFailure_Type())
ocmIfModuleFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:ocmIfModuleFailure.setStatus(_B)
_OcmIfConfigurationCommand_Type=CommandString
_OcmIfConfigurationCommand_Object=MibTableColumn
ocmIfConfigurationCommand=_OcmIfConfigurationCommand_Object((1,3,6,1,4,1,8708,2,33,2,2,1,1,26),_OcmIfConfigurationCommand_Type())
ocmIfConfigurationCommand.setMaxAccess(_C)
if mibBuilder.loadTexts:ocmIfConfigurationCommand.setStatus(_B)
_OcmIfChangeConnectedPort_Type=CommandString
_OcmIfChangeConnectedPort_Object=MibTableColumn
ocmIfChangeConnectedPort=_OcmIfChangeConnectedPort_Object((1,3,6,1,4,1,8708,2,33,2,2,1,1,27),_OcmIfChangeConnectedPort_Type())
ocmIfChangeConnectedPort.setMaxAccess(_C)
if mibBuilder.loadTexts:ocmIfChangeConnectedPort.setStatus(_B)
_OcmIfSaveReference_Type=CommandString
_OcmIfSaveReference_Object=MibTableColumn
ocmIfSaveReference=_OcmIfSaveReference_Object((1,3,6,1,4,1,8708,2,33,2,2,1,1,28),_OcmIfSaveReference_Type())
ocmIfSaveReference.setMaxAccess(_C)
if mibBuilder.loadTexts:ocmIfSaveReference.setStatus(_B)
class _OcmIfPowerOffset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,350))
_OcmIfPowerOffset_Type.__name__=_E
_OcmIfPowerOffset_Object=MibTableColumn
ocmIfPowerOffset=_OcmIfPowerOffset_Object((1,3,6,1,4,1,8708,2,33,2,2,1,1,29),_OcmIfPowerOffset_Type())
ocmIfPowerOffset.setMaxAccess(_D)
if mibBuilder.loadTexts:ocmIfPowerOffset.setStatus(_B)
class _OcmIfConnectedBoardType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('oa',1),('roadm',2),('oa26c',3),('mdu40',4),('other',5),('oaraed21hg',6),('oaraed20lg',7)))
_OcmIfConnectedBoardType_Type.__name__=_E
_OcmIfConnectedBoardType_Object=MibTableColumn
ocmIfConnectedBoardType=_OcmIfConnectedBoardType_Object((1,3,6,1,4,1,8708,2,33,2,2,1,1,30),_OcmIfConnectedBoardType_Type())
ocmIfConnectedBoardType.setMaxAccess(_D)
if mibBuilder.loadTexts:ocmIfConnectedBoardType.setStatus(_B)
_OcmIfChangeConnectedBoardType_Type=CommandString
_OcmIfChangeConnectedBoardType_Object=MibTableColumn
ocmIfChangeConnectedBoardType=_OcmIfChangeConnectedBoardType_Object((1,3,6,1,4,1,8708,2,33,2,2,1,1,31),_OcmIfChangeConnectedBoardType_Type())
ocmIfChangeConnectedBoardType.setMaxAccess(_C)
if mibBuilder.loadTexts:ocmIfChangeConnectedBoardType.setStatus(_B)
_OcmIfMaxPowerLevel_Type=Integer32
_OcmIfMaxPowerLevel_Object=MibTableColumn
ocmIfMaxPowerLevel=_OcmIfMaxPowerLevel_Object((1,3,6,1,4,1,8708,2,33,2,2,1,1,32),_OcmIfMaxPowerLevel_Type())
ocmIfMaxPowerLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:ocmIfMaxPowerLevel.setStatus(_B)
_OcmIfMinPowerLevel_Type=Integer32
_OcmIfMinPowerLevel_Object=MibTableColumn
ocmIfMinPowerLevel=_OcmIfMinPowerLevel_Object((1,3,6,1,4,1,8708,2,33,2,2,1,1,33),_OcmIfMinPowerLevel_Type())
ocmIfMinPowerLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:ocmIfMinPowerLevel.setStatus(_B)
_OcmIfDeltaPower_Type=Integer32
_OcmIfDeltaPower_Object=MibTableColumn
ocmIfDeltaPower=_OcmIfDeltaPower_Object((1,3,6,1,4,1,8708,2,33,2,2,1,1,34),_OcmIfDeltaPower_Type())
ocmIfDeltaPower.setMaxAccess(_C)
if mibBuilder.loadTexts:ocmIfDeltaPower.setStatus(_B)
_OcmIfChangePowerThreshold_Type=CommandString
_OcmIfChangePowerThreshold_Object=MibTableColumn
ocmIfChangePowerThreshold=_OcmIfChangePowerThreshold_Object((1,3,6,1,4,1,8708,2,33,2,2,1,1,35),_OcmIfChangePowerThreshold_Type())
ocmIfChangePowerThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:ocmIfChangePowerThreshold.setStatus(_B)
_OcmIfChangePowerOffset_Type=CommandString
_OcmIfChangePowerOffset_Object=MibTableColumn
ocmIfChangePowerOffset=_OcmIfChangePowerOffset_Object((1,3,6,1,4,1,8708,2,33,2,2,1,1,36),_OcmIfChangePowerOffset_Type())
ocmIfChangePowerOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:ocmIfChangePowerOffset.setStatus(_B)
class _OcmIfPowerOffsetAdjustment_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,350))
_OcmIfPowerOffsetAdjustment_Type.__name__=_E
_OcmIfPowerOffsetAdjustment_Object=MibTableColumn
ocmIfPowerOffsetAdjustment=_OcmIfPowerOffsetAdjustment_Object((1,3,6,1,4,1,8708,2,33,2,2,1,1,37),_OcmIfPowerOffsetAdjustment_Type())
ocmIfPowerOffsetAdjustment.setMaxAccess(_C)
if mibBuilder.loadTexts:ocmIfPowerOffsetAdjustment.setStatus(_B)
class _OcmIfSpacingMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('spacing50GHz',1))
_OcmIfSpacingMode_Type.__name__=_E
_OcmIfSpacingMode_Object=MibTableColumn
ocmIfSpacingMode=_OcmIfSpacingMode_Object((1,3,6,1,4,1,8708,2,33,2,2,1,1,38),_OcmIfSpacingMode_Type())
ocmIfSpacingMode.setMaxAccess(_D)
if mibBuilder.loadTexts:ocmIfSpacingMode.setStatus(_B)
_OcmIfHighInputPower_Type=FaultStatus
_OcmIfHighInputPower_Object=MibTableColumn
ocmIfHighInputPower=_OcmIfHighInputPower_Object((1,3,6,1,4,1,8708,2,33,2,2,1,1,39),_OcmIfHighInputPower_Type())
ocmIfHighInputPower.setMaxAccess(_C)
if mibBuilder.loadTexts:ocmIfHighInputPower.setStatus(_B)
_OcmChannelList_ObjectIdentity=ObjectIdentity
ocmChannelList=_OcmChannelList_ObjectIdentity((1,3,6,1,4,1,8708,2,33,2,3))
_OcmChannelTable_Object=MibTable
ocmChannelTable=_OcmChannelTable_Object((1,3,6,1,4,1,8708,2,33,2,3,1))
if mibBuilder.loadTexts:ocmChannelTable.setStatus(_B)
_OcmChannelEntry_Object=MibTableRow
ocmChannelEntry=_OcmChannelEntry_Object((1,3,6,1,4,1,8708,2,33,2,3,1,1))
ocmChannelEntry.setIndexNames((0,_A,_m))
if mibBuilder.loadTexts:ocmChannelEntry.setStatus(_B)
class _OcmChannelIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_OcmChannelIndex_Type.__name__=_I
_OcmChannelIndex_Object=MibTableColumn
ocmChannelIndex=_OcmChannelIndex_Object((1,3,6,1,4,1,8708,2,33,2,3,1,1,1),_OcmChannelIndex_Type())
ocmChannelIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ocmChannelIndex.setStatus(_B)
_OcmChannelName_Type=MgmtNameString
_OcmChannelName_Object=MibTableColumn
ocmChannelName=_OcmChannelName_Object((1,3,6,1,4,1,8708,2,33,2,3,1,1,2),_OcmChannelName_Type())
ocmChannelName.setMaxAccess(_C)
if mibBuilder.loadTexts:ocmChannelName.setStatus(_B)
_OcmChannelFrequency_Type=LambdaFrequency
_OcmChannelFrequency_Object=MibTableColumn
ocmChannelFrequency=_OcmChannelFrequency_Object((1,3,6,1,4,1,8708,2,33,2,3,1,1,3),_OcmChannelFrequency_Type())
ocmChannelFrequency.setMaxAccess(_D)
if mibBuilder.loadTexts:ocmChannelFrequency.setStatus(_B)
_OcmChannelPowerLevel_Type=Integer32
_OcmChannelPowerLevel_Object=MibTableColumn
ocmChannelPowerLevel=_OcmChannelPowerLevel_Object((1,3,6,1,4,1,8708,2,33,2,3,1,1,4),_OcmChannelPowerLevel_Type())
ocmChannelPowerLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:ocmChannelPowerLevel.setStatus(_B)
_OcmChannelUpdateLastChangeTime_Type=DateAndTime
_OcmChannelUpdateLastChangeTime_Object=MibTableColumn
ocmChannelUpdateLastChangeTime=_OcmChannelUpdateLastChangeTime_Object((1,3,6,1,4,1,8708,2,33,2,3,1,1,5),_OcmChannelUpdateLastChangeTime_Type())
ocmChannelUpdateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ocmChannelUpdateLastChangeTime.setStatus(_B)
class _OcmChannelOcmRefIfIndex_Type(Unsigned32):defaultValue=1
_OcmChannelOcmRefIfIndex_Type.__name__=_I
_OcmChannelOcmRefIfIndex_Object=MibTableColumn
ocmChannelOcmRefIfIndex=_OcmChannelOcmRefIfIndex_Object((1,3,6,1,4,1,8708,2,33,2,3,1,1,6),_OcmChannelOcmRefIfIndex_Type())
ocmChannelOcmRefIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ocmChannelOcmRefIfIndex.setStatus(_B)
class _OcmChannelReferencePowerLevel_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1000,1000))
_OcmChannelReferencePowerLevel_Type.__name__=_E
_OcmChannelReferencePowerLevel_Object=MibTableColumn
ocmChannelReferencePowerLevel=_OcmChannelReferencePowerLevel_Object((1,3,6,1,4,1,8708,2,33,2,3,1,1,7),_OcmChannelReferencePowerLevel_Type())
ocmChannelReferencePowerLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:ocmChannelReferencePowerLevel.setStatus(_B)
_OcmChannelReferenceTime_Type=DisplayString
_OcmChannelReferenceTime_Object=MibTableColumn
ocmChannelReferenceTime=_OcmChannelReferenceTime_Object((1,3,6,1,4,1,8708,2,33,2,3,1,1,8),_OcmChannelReferenceTime_Type())
ocmChannelReferenceTime.setMaxAccess(_D)
if mibBuilder.loadTexts:ocmChannelReferenceTime.setStatus(_B)
_OcmChannelSaveReference_Type=CommandString
_OcmChannelSaveReference_Object=MibTableColumn
ocmChannelSaveReference=_OcmChannelSaveReference_Object((1,3,6,1,4,1,8708,2,33,2,3,1,1,9),_OcmChannelSaveReference_Type())
ocmChannelSaveReference.setMaxAccess(_C)
if mibBuilder.loadTexts:ocmChannelSaveReference.setStatus(_B)
_LumentisOcmNotifications_ObjectIdentity=ObjectIdentity
lumentisOcmNotifications=_LumentisOcmNotifications_ObjectIdentity((1,3,6,1,4,1,8708,2,33,2,4))
ocmGeneralGroup=ObjectGroup((1,3,6,1,4,1,8708,2,33,1,1,1))
ocmGeneralGroup.setObjects(*((_A,_A7),(_A,_A8),(_A,_A9)))
if mibBuilder.loadTexts:ocmGeneralGroup.setStatus(_B)
ocmIfGroup=ObjectGroup((1,3,6,1,4,1,8708,2,33,1,1,2))
ocmIfGroup.setObjects(*((_A,_H),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l)))
if mibBuilder.loadTexts:ocmIfGroup.setStatus(_F)
ocmChannelGroup=ObjectGroup((1,3,6,1,4,1,8708,2,33,1,1,3))
ocmChannelGroup.setObjects(*((_A,_m),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w)))
if mibBuilder.loadTexts:ocmChannelGroup.setStatus(_F)
ocmIfGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,33,1,1,4))
ocmIfGroupV2.setObjects(*((_A,_H),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_n),(_A,_o)))
if mibBuilder.loadTexts:ocmIfGroupV2.setStatus(_F)
ocmIfGroupV3=ObjectGroup((1,3,6,1,4,1,8708,2,33,1,1,5))
ocmIfGroupV3.setObjects(*((_A,_H),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_n),(_A,_o),(_A,_x)))
if mibBuilder.loadTexts:ocmIfGroupV3.setStatus(_F)
ocmChannelGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,33,1,1,6))
ocmChannelGroupV2.setObjects(*((_A,_m),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_AA),(_A,_AB)))
if mibBuilder.loadTexts:ocmChannelGroupV2.setStatus(_B)
ocmIfGroupV4=ObjectGroup((1,3,6,1,4,1,8708,2,33,1,1,7))
ocmIfGroupV4.setObjects(*((_A,_H),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_n),(_A,_o),(_A,_x),(_A,_AC),(_A,_AD)))
if mibBuilder.loadTexts:ocmIfGroupV4.setStatus(_B)
lumOcmBasicComplV1=ModuleCompliance((1,3,6,1,4,1,8708,2,33,1,2,1))
lumOcmBasicComplV1.setObjects(*((_A,_G),(_A,_y),(_A,_p)))
if mibBuilder.loadTexts:lumOcmBasicComplV1.setStatus(_F)
lumOcmBasicComplV2=ModuleCompliance((1,3,6,1,4,1,8708,2,33,1,2,2))
lumOcmBasicComplV2.setObjects(*((_A,_G),(_A,_AE),(_A,_p)))
if mibBuilder.loadTexts:lumOcmBasicComplV2.setStatus(_F)
lumOcmBasicComplV3=ModuleCompliance((1,3,6,1,4,1,8708,2,33,1,2,3))
lumOcmBasicComplV3.setObjects(*((_A,_G),(_A,_z),(_A,_p)))
if mibBuilder.loadTexts:lumOcmBasicComplV3.setStatus(_F)
lumOcmBasicComplV4=ModuleCompliance((1,3,6,1,4,1,8708,2,33,1,2,4))
lumOcmBasicComplV4.setObjects(*((_A,_G),(_A,_z),(_A,_A0)))
if mibBuilder.loadTexts:lumOcmBasicComplV4.setStatus(_F)
lumOcmBasicComplV5=ModuleCompliance((1,3,6,1,4,1,8708,2,33,1,2,5))
lumOcmBasicComplV5.setObjects(*((_A,_G),(_A,_AF),(_A,_A0)))
if mibBuilder.loadTexts:lumOcmBasicComplV5.setStatus(_B)
lumOcmMinimalComplV1=ModuleCompliance((1,3,6,1,4,1,8708,2,33,1,4,1))
lumOcmMinimalComplV1.setObjects(*((_A,_G),(_A,_y)))
if mibBuilder.loadTexts:lumOcmMinimalComplV1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'lumOcmMIBModule':lumOcmMIBModule,'lumOcmConfs':lumOcmConfs,'lumOcmGroups':lumOcmGroups,_G:ocmGeneralGroup,_y:ocmIfGroup,_p:ocmChannelGroup,_AE:ocmIfGroupV2,_z:ocmIfGroupV3,_A0:ocmChannelGroupV2,_AF:ocmIfGroupV4,'lumOcmCompl':lumOcmCompl,'lumOcmBasicComplV1':lumOcmBasicComplV1,'lumOcmBasicComplV2':lumOcmBasicComplV2,'lumOcmBasicComplV3':lumOcmBasicComplV3,'lumOcmBasicComplV4':lumOcmBasicComplV4,'lumOcmBasicComplV5':lumOcmBasicComplV5,'lumOcmMinimalGroups':lumOcmMinimalGroups,'lumOcmMinimalCompl':lumOcmMinimalCompl,'lumOcmMinimalComplV1':lumOcmMinimalComplV1,'lumOcmMIBObjects':lumOcmMIBObjects,'ocmGeneral':ocmGeneral,_A7:ocmGeneralLastChangeTime,_A8:ocmGeneralStateLastChangeTime,_A9:ocmGeneralOcmIfTableSize,'ocmGeneralOcmChannelTableSize':ocmGeneralOcmChannelTableSize,'ocmIfList':ocmIfList,'ocmIfTable':ocmIfTable,'ocmIfEntry':ocmIfEntry,_H:ocmIfIndex,_J:ocmIfName,_K:ocmIfDescr,_L:ocmIfSubrack,_M:ocmIfSlot,_N:ocmIfRxPort,_O:ocmIfInvPhysIndexOrZero,_P:ocmIfAdminStatus,_Q:ocmIfOperStatus,_R:ocmIfPowerThreshold,_S:ocmIfUpdateLastChangeTime,_T:ocmIfConnectedSubrack,_U:ocmIfConnectedSlot,_V:ocmIfConnectedPort,_W:ocmIfActivePort,_X:ocmIfControlMode,_Y:ocmIfReferenceTime,_Z:ocmIfSwitchFailure,_a:ocmIfDataSourceNotDefined,_b:ocmIfCommissioningMode,_c:ocmIfModuleFailure,_d:ocmIfConfigurationCommand,_e:ocmIfChangeConnectedPort,_f:ocmIfSaveReference,_g:ocmIfPowerOffset,_h:ocmIfConnectedBoardType,_i:ocmIfChangeConnectedBoardType,_j:ocmIfMaxPowerLevel,_k:ocmIfMinPowerLevel,_l:ocmIfDeltaPower,_n:ocmIfChangePowerThreshold,_o:ocmIfChangePowerOffset,_x:ocmIfPowerOffsetAdjustment,_AC:ocmIfSpacingMode,_AD:ocmIfHighInputPower,'ocmChannelList':ocmChannelList,'ocmChannelTable':ocmChannelTable,'ocmChannelEntry':ocmChannelEntry,_m:ocmChannelIndex,_r:ocmChannelName,_s:ocmChannelFrequency,_t:ocmChannelPowerLevel,_u:ocmChannelUpdateLastChangeTime,_v:ocmChannelOcmRefIfIndex,_w:ocmChannelReferencePowerLevel,_AA:ocmChannelReferenceTime,_AB:ocmChannelSaveReference,'lumentisOcmNotifications':lumentisOcmNotifications})