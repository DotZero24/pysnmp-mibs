_t='sdhpdhE1t1GroupV2'
_s='sdhpdhE1t1Group'
_r='sdhpdhE1t1SignalLabel'
_q='sdhpdhE1t1EquipmentIndex'
_p='sdhpdhEquipmentChangeMultiplexStructureCommand'
_o='sdhpdhEquipmentMultiplexingStructure'
_n='sdhpdhEquipmentName'
_m='deprecated'
_l='sdhpdhGeneralEquipmentTableSize'
_k='sdhpdhGeneralE1t1TableSize'
_j='sdhpdhGeneralStateLastChangeTime'
_i='sdhpdhGeneralLastChangeTime'
_h='degraded'
_g='MgmtNameString'
_f='BoardOrInterfaceOperStatus'
_e='BoardOrInterfaceAdminStatus'
_d='sdhpdhEquipmentGroup'
_c='sdhpdhGeneralGroup'
_b='sdhpdhE1t1FrameFormat'
_a='sdhpdhE1t1TuLossOfPointerC2W'
_Z='sdhpdhE1t1TuAlarmIndicationSignalC2W'
_Y='sdhpdhE1t1ClockDomain'
_X='sdhpdhE1t1VcIndex'
_W='sdhpdhE1t1TxSignalStatus'
_V='sdhpdhE1t1RxSignalStatus'
_U='sdhpdhE1t1MultiplexingInformation'
_T='sdhpdhE1t1SubChannelId'
_S='sdhpdhE1t1ConnectionStatus'
_R='sdhpdhE1t1UnEquipped'
_Q='sdhpdhE1t1LossOfFrameW2C'
_P='sdhpdhE1t1LossOfFrameC2W'
_O='sdhpdhE1t1AlarmIndicationSignalC2W'
_N='sdhpdhE1t1AlarmIndicationSignalW2C'
_M='sdhpdhE1t1OperStatus'
_L='sdhpdhE1t1AdminStatus'
_K='sdhpdhE1t1Descr'
_J='sdhpdhE1t1Name'
_I='sdhpdhEquipmentIndex'
_H='read-write'
_G='Unsigned32'
_F='sdhpdhE1t1Index'
_E='DisplayString'
_D='Integer32'
_C='read-only'
_B='current'
_A='LUM-SDHPDH-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lumModules,lumSdhpdhMIB=mibBuilder.importSymbols('LUM-REG','lumModules','lumSdhpdhMIB')
BoardOrInterfaceAdminStatus,BoardOrInterfaceOperStatus,CommandString,FaultStatus,MgmtNameString=mibBuilder.importSymbols('LUM-TC',_e,_f,'CommandString','FaultStatus',_g)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_E,'PhysAddress','TextualConvention')
lumSdhpdhMIBModule=ModuleIdentity((1,3,6,1,4,1,8708,1,1,35))
if mibBuilder.loadTexts:lumSdhpdhMIBModule.setRevisions(('2017-06-15 00:00','2016-01-11 00:00','2011-06-15 00:00','2009-06-15 00:00'))
_LumSdhpdhConfs_ObjectIdentity=ObjectIdentity
lumSdhpdhConfs=_LumSdhpdhConfs_ObjectIdentity((1,3,6,1,4,1,8708,2,35,1))
_LumSdhpdhGroups_ObjectIdentity=ObjectIdentity
lumSdhpdhGroups=_LumSdhpdhGroups_ObjectIdentity((1,3,6,1,4,1,8708,2,35,1,1))
_LumSdhpdhCompl_ObjectIdentity=ObjectIdentity
lumSdhpdhCompl=_LumSdhpdhCompl_ObjectIdentity((1,3,6,1,4,1,8708,2,35,1,2))
_LumSdhpdhMIBObjects_ObjectIdentity=ObjectIdentity
lumSdhpdhMIBObjects=_LumSdhpdhMIBObjects_ObjectIdentity((1,3,6,1,4,1,8708,2,35,2))
_SdhpdhGeneral_ObjectIdentity=ObjectIdentity
sdhpdhGeneral=_SdhpdhGeneral_ObjectIdentity((1,3,6,1,4,1,8708,2,35,2,1))
_SdhpdhGeneralLastChangeTime_Type=DateAndTime
_SdhpdhGeneralLastChangeTime_Object=MibScalar
sdhpdhGeneralLastChangeTime=_SdhpdhGeneralLastChangeTime_Object((1,3,6,1,4,1,8708,2,35,2,1,1),_SdhpdhGeneralLastChangeTime_Type())
sdhpdhGeneralLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:sdhpdhGeneralLastChangeTime.setStatus(_B)
_SdhpdhGeneralStateLastChangeTime_Type=DateAndTime
_SdhpdhGeneralStateLastChangeTime_Object=MibScalar
sdhpdhGeneralStateLastChangeTime=_SdhpdhGeneralStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,35,2,1,2),_SdhpdhGeneralStateLastChangeTime_Type())
sdhpdhGeneralStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:sdhpdhGeneralStateLastChangeTime.setStatus(_B)
_SdhpdhGeneralE1t1TableSize_Type=Unsigned32
_SdhpdhGeneralE1t1TableSize_Object=MibScalar
sdhpdhGeneralE1t1TableSize=_SdhpdhGeneralE1t1TableSize_Object((1,3,6,1,4,1,8708,2,35,2,1,3),_SdhpdhGeneralE1t1TableSize_Type())
sdhpdhGeneralE1t1TableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:sdhpdhGeneralE1t1TableSize.setStatus(_B)
_SdhpdhGeneralEquipmentTableSize_Type=Unsigned32
_SdhpdhGeneralEquipmentTableSize_Object=MibScalar
sdhpdhGeneralEquipmentTableSize=_SdhpdhGeneralEquipmentTableSize_Object((1,3,6,1,4,1,8708,2,35,2,1,4),_SdhpdhGeneralEquipmentTableSize_Type())
sdhpdhGeneralEquipmentTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:sdhpdhGeneralEquipmentTableSize.setStatus(_B)
_SdhpdhE1t1List_ObjectIdentity=ObjectIdentity
sdhpdhE1t1List=_SdhpdhE1t1List_ObjectIdentity((1,3,6,1,4,1,8708,2,35,2,2))
_SdhpdhE1t1Table_Object=MibTable
sdhpdhE1t1Table=_SdhpdhE1t1Table_Object((1,3,6,1,4,1,8708,2,35,2,2,1))
if mibBuilder.loadTexts:sdhpdhE1t1Table.setStatus(_B)
_SdhpdhE1t1Entry_Object=MibTableRow
sdhpdhE1t1Entry=_SdhpdhE1t1Entry_Object((1,3,6,1,4,1,8708,2,35,2,2,1,1))
sdhpdhE1t1Entry.setIndexNames((0,_A,_F))
if mibBuilder.loadTexts:sdhpdhE1t1Entry.setStatus(_B)
class _SdhpdhE1t1Index_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SdhpdhE1t1Index_Type.__name__=_G
_SdhpdhE1t1Index_Object=MibTableColumn
sdhpdhE1t1Index=_SdhpdhE1t1Index_Object((1,3,6,1,4,1,8708,2,35,2,2,1,1,1),_SdhpdhE1t1Index_Type())
sdhpdhE1t1Index.setMaxAccess(_C)
if mibBuilder.loadTexts:sdhpdhE1t1Index.setStatus(_B)
class _SdhpdhE1t1Name_Type(MgmtNameString):defaultValue=OctetString('')
_SdhpdhE1t1Name_Type.__name__=_g
_SdhpdhE1t1Name_Object=MibTableColumn
sdhpdhE1t1Name=_SdhpdhE1t1Name_Object((1,3,6,1,4,1,8708,2,35,2,2,1,1,2),_SdhpdhE1t1Name_Type())
sdhpdhE1t1Name.setMaxAccess(_C)
if mibBuilder.loadTexts:sdhpdhE1t1Name.setStatus(_B)
class _SdhpdhE1t1Descr_Type(DisplayString):defaultValue=OctetString('')
_SdhpdhE1t1Descr_Type.__name__=_E
_SdhpdhE1t1Descr_Object=MibTableColumn
sdhpdhE1t1Descr=_SdhpdhE1t1Descr_Object((1,3,6,1,4,1,8708,2,35,2,2,1,1,6),_SdhpdhE1t1Descr_Type())
sdhpdhE1t1Descr.setMaxAccess(_H)
if mibBuilder.loadTexts:sdhpdhE1t1Descr.setStatus(_B)
class _SdhpdhE1t1AdminStatus_Type(BoardOrInterfaceAdminStatus):defaultValue=3
_SdhpdhE1t1AdminStatus_Type.__name__=_e
_SdhpdhE1t1AdminStatus_Object=MibTableColumn
sdhpdhE1t1AdminStatus=_SdhpdhE1t1AdminStatus_Object((1,3,6,1,4,1,8708,2,35,2,2,1,1,7),_SdhpdhE1t1AdminStatus_Type())
sdhpdhE1t1AdminStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:sdhpdhE1t1AdminStatus.setStatus(_B)
class _SdhpdhE1t1OperStatus_Type(BoardOrInterfaceOperStatus):defaultValue=1
_SdhpdhE1t1OperStatus_Type.__name__=_f
_SdhpdhE1t1OperStatus_Object=MibTableColumn
sdhpdhE1t1OperStatus=_SdhpdhE1t1OperStatus_Object((1,3,6,1,4,1,8708,2,35,2,2,1,1,8),_SdhpdhE1t1OperStatus_Type())
sdhpdhE1t1OperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sdhpdhE1t1OperStatus.setStatus(_B)
_SdhpdhE1t1AlarmIndicationSignalW2C_Type=FaultStatus
_SdhpdhE1t1AlarmIndicationSignalW2C_Object=MibTableColumn
sdhpdhE1t1AlarmIndicationSignalW2C=_SdhpdhE1t1AlarmIndicationSignalW2C_Object((1,3,6,1,4,1,8708,2,35,2,2,1,1,9),_SdhpdhE1t1AlarmIndicationSignalW2C_Type())
sdhpdhE1t1AlarmIndicationSignalW2C.setMaxAccess(_C)
if mibBuilder.loadTexts:sdhpdhE1t1AlarmIndicationSignalW2C.setStatus(_B)
_SdhpdhE1t1AlarmIndicationSignalC2W_Type=FaultStatus
_SdhpdhE1t1AlarmIndicationSignalC2W_Object=MibTableColumn
sdhpdhE1t1AlarmIndicationSignalC2W=_SdhpdhE1t1AlarmIndicationSignalC2W_Object((1,3,6,1,4,1,8708,2,35,2,2,1,1,10),_SdhpdhE1t1AlarmIndicationSignalC2W_Type())
sdhpdhE1t1AlarmIndicationSignalC2W.setMaxAccess(_C)
if mibBuilder.loadTexts:sdhpdhE1t1AlarmIndicationSignalC2W.setStatus(_B)
_SdhpdhE1t1LossOfFrameC2W_Type=FaultStatus
_SdhpdhE1t1LossOfFrameC2W_Object=MibTableColumn
sdhpdhE1t1LossOfFrameC2W=_SdhpdhE1t1LossOfFrameC2W_Object((1,3,6,1,4,1,8708,2,35,2,2,1,1,11),_SdhpdhE1t1LossOfFrameC2W_Type())
sdhpdhE1t1LossOfFrameC2W.setMaxAccess(_C)
if mibBuilder.loadTexts:sdhpdhE1t1LossOfFrameC2W.setStatus(_B)
_SdhpdhE1t1LossOfFrameW2C_Type=FaultStatus
_SdhpdhE1t1LossOfFrameW2C_Object=MibTableColumn
sdhpdhE1t1LossOfFrameW2C=_SdhpdhE1t1LossOfFrameW2C_Object((1,3,6,1,4,1,8708,2,35,2,2,1,1,12),_SdhpdhE1t1LossOfFrameW2C_Type())
sdhpdhE1t1LossOfFrameW2C.setMaxAccess(_C)
if mibBuilder.loadTexts:sdhpdhE1t1LossOfFrameW2C.setStatus(_B)
_SdhpdhE1t1UnEquipped_Type=FaultStatus
_SdhpdhE1t1UnEquipped_Object=MibTableColumn
sdhpdhE1t1UnEquipped=_SdhpdhE1t1UnEquipped_Object((1,3,6,1,4,1,8708,2,35,2,2,1,1,13),_SdhpdhE1t1UnEquipped_Type())
sdhpdhE1t1UnEquipped.setMaxAccess(_C)
if mibBuilder.loadTexts:sdhpdhE1t1UnEquipped.setStatus(_B)
class _SdhpdhE1t1ConnectionStatus_Type(DisplayString):defaultValue=OctetString('Not connected')
_SdhpdhE1t1ConnectionStatus_Type.__name__=_E
_SdhpdhE1t1ConnectionStatus_Object=MibTableColumn
sdhpdhE1t1ConnectionStatus=_SdhpdhE1t1ConnectionStatus_Object((1,3,6,1,4,1,8708,2,35,2,2,1,1,14),_SdhpdhE1t1ConnectionStatus_Type())
sdhpdhE1t1ConnectionStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sdhpdhE1t1ConnectionStatus.setStatus(_B)
_SdhpdhE1t1SubChannelId_Type=Unsigned32
_SdhpdhE1t1SubChannelId_Object=MibTableColumn
sdhpdhE1t1SubChannelId=_SdhpdhE1t1SubChannelId_Object((1,3,6,1,4,1,8708,2,35,2,2,1,1,15),_SdhpdhE1t1SubChannelId_Type())
sdhpdhE1t1SubChannelId.setMaxAccess(_C)
if mibBuilder.loadTexts:sdhpdhE1t1SubChannelId.setStatus(_B)
class _SdhpdhE1t1MultiplexingInformation_Type(DisplayString):defaultValue=OctetString('')
_SdhpdhE1t1MultiplexingInformation_Type.__name__=_E
_SdhpdhE1t1MultiplexingInformation_Object=MibTableColumn
sdhpdhE1t1MultiplexingInformation=_SdhpdhE1t1MultiplexingInformation_Object((1,3,6,1,4,1,8708,2,35,2,2,1,1,16),_SdhpdhE1t1MultiplexingInformation_Type())
sdhpdhE1t1MultiplexingInformation.setMaxAccess(_C)
if mibBuilder.loadTexts:sdhpdhE1t1MultiplexingInformation.setStatus(_B)
class _SdhpdhE1t1RxSignalStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('down',1),(_h,2),('up',3)))
_SdhpdhE1t1RxSignalStatus_Type.__name__=_D
_SdhpdhE1t1RxSignalStatus_Object=MibTableColumn
sdhpdhE1t1RxSignalStatus=_SdhpdhE1t1RxSignalStatus_Object((1,3,6,1,4,1,8708,2,35,2,2,1,1,17),_SdhpdhE1t1RxSignalStatus_Type())
sdhpdhE1t1RxSignalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sdhpdhE1t1RxSignalStatus.setStatus(_B)
class _SdhpdhE1t1TxSignalStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('down',1),(_h,2),('up',3)))
_SdhpdhE1t1TxSignalStatus_Type.__name__=_D
_SdhpdhE1t1TxSignalStatus_Object=MibTableColumn
sdhpdhE1t1TxSignalStatus=_SdhpdhE1t1TxSignalStatus_Object((1,3,6,1,4,1,8708,2,35,2,2,1,1,18),_SdhpdhE1t1TxSignalStatus_Type())
sdhpdhE1t1TxSignalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sdhpdhE1t1TxSignalStatus.setStatus(_B)
_SdhpdhE1t1VcIndex_Type=Unsigned32
_SdhpdhE1t1VcIndex_Object=MibTableColumn
sdhpdhE1t1VcIndex=_SdhpdhE1t1VcIndex_Object((1,3,6,1,4,1,8708,2,35,2,2,1,1,19),_SdhpdhE1t1VcIndex_Type())
sdhpdhE1t1VcIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:sdhpdhE1t1VcIndex.setStatus(_B)
_SdhpdhE1t1ClockDomain_Type=DisplayString
_SdhpdhE1t1ClockDomain_Object=MibTableColumn
sdhpdhE1t1ClockDomain=_SdhpdhE1t1ClockDomain_Object((1,3,6,1,4,1,8708,2,35,2,2,1,1,20),_SdhpdhE1t1ClockDomain_Type())
sdhpdhE1t1ClockDomain.setMaxAccess(_C)
if mibBuilder.loadTexts:sdhpdhE1t1ClockDomain.setStatus(_B)
_SdhpdhE1t1TuAlarmIndicationSignalC2W_Type=FaultStatus
_SdhpdhE1t1TuAlarmIndicationSignalC2W_Object=MibTableColumn
sdhpdhE1t1TuAlarmIndicationSignalC2W=_SdhpdhE1t1TuAlarmIndicationSignalC2W_Object((1,3,6,1,4,1,8708,2,35,2,2,1,1,21),_SdhpdhE1t1TuAlarmIndicationSignalC2W_Type())
sdhpdhE1t1TuAlarmIndicationSignalC2W.setMaxAccess(_C)
if mibBuilder.loadTexts:sdhpdhE1t1TuAlarmIndicationSignalC2W.setStatus(_B)
_SdhpdhE1t1TuLossOfPointerC2W_Type=FaultStatus
_SdhpdhE1t1TuLossOfPointerC2W_Object=MibTableColumn
sdhpdhE1t1TuLossOfPointerC2W=_SdhpdhE1t1TuLossOfPointerC2W_Object((1,3,6,1,4,1,8708,2,35,2,2,1,1,22),_SdhpdhE1t1TuLossOfPointerC2W_Type())
sdhpdhE1t1TuLossOfPointerC2W.setMaxAccess(_C)
if mibBuilder.loadTexts:sdhpdhE1t1TuLossOfPointerC2W.setStatus(_B)
class _SdhpdhE1t1FrameFormat_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('sf',1),('esf',2)))
_SdhpdhE1t1FrameFormat_Type.__name__=_D
_SdhpdhE1t1FrameFormat_Object=MibTableColumn
sdhpdhE1t1FrameFormat=_SdhpdhE1t1FrameFormat_Object((1,3,6,1,4,1,8708,2,35,2,2,1,1,23),_SdhpdhE1t1FrameFormat_Type())
sdhpdhE1t1FrameFormat.setMaxAccess(_H)
if mibBuilder.loadTexts:sdhpdhE1t1FrameFormat.setStatus(_B)
_SdhpdhE1t1EquipmentIndex_Type=Unsigned32
_SdhpdhE1t1EquipmentIndex_Object=MibTableColumn
sdhpdhE1t1EquipmentIndex=_SdhpdhE1t1EquipmentIndex_Object((1,3,6,1,4,1,8708,2,35,2,2,1,1,24),_SdhpdhE1t1EquipmentIndex_Type())
sdhpdhE1t1EquipmentIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:sdhpdhE1t1EquipmentIndex.setStatus(_B)
class _SdhpdhE1t1SignalLabel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('unequipped',0),('equippedNonspecific',1),('asynchronous',2),('bitSynchronous',3),('byteSynchronous',4),('reserved',5),('testSignal',6),('vcAis',7)))
_SdhpdhE1t1SignalLabel_Type.__name__=_D
_SdhpdhE1t1SignalLabel_Object=MibTableColumn
sdhpdhE1t1SignalLabel=_SdhpdhE1t1SignalLabel_Object((1,3,6,1,4,1,8708,2,35,2,2,1,1,25),_SdhpdhE1t1SignalLabel_Type())
sdhpdhE1t1SignalLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:sdhpdhE1t1SignalLabel.setStatus(_B)
_SdhpdhEquipmentList_ObjectIdentity=ObjectIdentity
sdhpdhEquipmentList=_SdhpdhEquipmentList_ObjectIdentity((1,3,6,1,4,1,8708,2,35,2,3))
_SdhpdhEquipmentTable_Object=MibTable
sdhpdhEquipmentTable=_SdhpdhEquipmentTable_Object((1,3,6,1,4,1,8708,2,35,2,3,1))
if mibBuilder.loadTexts:sdhpdhEquipmentTable.setStatus(_B)
_SdhpdhEquipmentEntry_Object=MibTableRow
sdhpdhEquipmentEntry=_SdhpdhEquipmentEntry_Object((1,3,6,1,4,1,8708,2,35,2,3,1,1))
sdhpdhEquipmentEntry.setIndexNames((0,_A,_I))
if mibBuilder.loadTexts:sdhpdhEquipmentEntry.setStatus(_B)
class _SdhpdhEquipmentIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SdhpdhEquipmentIndex_Type.__name__=_G
_SdhpdhEquipmentIndex_Object=MibTableColumn
sdhpdhEquipmentIndex=_SdhpdhEquipmentIndex_Object((1,3,6,1,4,1,8708,2,35,2,3,1,1,1),_SdhpdhEquipmentIndex_Type())
sdhpdhEquipmentIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:sdhpdhEquipmentIndex.setStatus(_B)
_SdhpdhEquipmentName_Type=MgmtNameString
_SdhpdhEquipmentName_Object=MibTableColumn
sdhpdhEquipmentName=_SdhpdhEquipmentName_Object((1,3,6,1,4,1,8708,2,35,2,3,1,1,2),_SdhpdhEquipmentName_Type())
sdhpdhEquipmentName.setMaxAccess(_C)
if mibBuilder.loadTexts:sdhpdhEquipmentName.setStatus(_B)
class _SdhpdhEquipmentMultiplexingStructure_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('vc3',1),('vc4',2)))
_SdhpdhEquipmentMultiplexingStructure_Type.__name__=_D
_SdhpdhEquipmentMultiplexingStructure_Object=MibTableColumn
sdhpdhEquipmentMultiplexingStructure=_SdhpdhEquipmentMultiplexingStructure_Object((1,3,6,1,4,1,8708,2,35,2,3,1,1,3),_SdhpdhEquipmentMultiplexingStructure_Type())
sdhpdhEquipmentMultiplexingStructure.setMaxAccess('read-create')
if mibBuilder.loadTexts:sdhpdhEquipmentMultiplexingStructure.setStatus(_B)
_SdhpdhEquipmentChangeMultiplexStructureCommand_Type=CommandString
_SdhpdhEquipmentChangeMultiplexStructureCommand_Object=MibTableColumn
sdhpdhEquipmentChangeMultiplexStructureCommand=_SdhpdhEquipmentChangeMultiplexStructureCommand_Object((1,3,6,1,4,1,8708,2,35,2,3,1,1,4),_SdhpdhEquipmentChangeMultiplexStructureCommand_Type())
sdhpdhEquipmentChangeMultiplexStructureCommand.setMaxAccess(_C)
if mibBuilder.loadTexts:sdhpdhEquipmentChangeMultiplexStructureCommand.setStatus(_B)
sdhpdhGeneralGroup=ObjectGroup((1,3,6,1,4,1,8708,2,35,1,1,1))
sdhpdhGeneralGroup.setObjects(*((_A,_i),(_A,_j),(_A,_k),(_A,_l)))
if mibBuilder.loadTexts:sdhpdhGeneralGroup.setStatus(_B)
sdhpdhE1t1Group=ObjectGroup((1,3,6,1,4,1,8708,2,35,1,1,2))
sdhpdhE1t1Group.setObjects(*((_A,_F),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b)))
if mibBuilder.loadTexts:sdhpdhE1t1Group.setStatus(_m)
sdhpdhEquipmentGroup=ObjectGroup((1,3,6,1,4,1,8708,2,35,1,1,3))
sdhpdhEquipmentGroup.setObjects(*((_A,_I),(_A,_n),(_A,_o),(_A,_p)))
if mibBuilder.loadTexts:sdhpdhEquipmentGroup.setStatus(_B)
sdhpdhE1t1GroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,35,1,1,4))
sdhpdhE1t1GroupV2.setObjects(*((_A,_F),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_q),(_A,_r)))
if mibBuilder.loadTexts:sdhpdhE1t1GroupV2.setStatus(_B)
lumSdhpdhBasicCompl1=ModuleCompliance((1,3,6,1,4,1,8708,2,35,1,2,1))
lumSdhpdhBasicCompl1.setObjects(*((_A,_c),(_A,_s),(_A,_d)))
if mibBuilder.loadTexts:lumSdhpdhBasicCompl1.setStatus(_m)
lumSdhpdhBasicCompl2=ModuleCompliance((1,3,6,1,4,1,8708,2,35,1,2,2))
lumSdhpdhBasicCompl2.setObjects(*((_A,_c),(_A,_t),(_A,_d)))
if mibBuilder.loadTexts:lumSdhpdhBasicCompl2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'lumSdhpdhMIBModule':lumSdhpdhMIBModule,'lumSdhpdhConfs':lumSdhpdhConfs,'lumSdhpdhGroups':lumSdhpdhGroups,_c:sdhpdhGeneralGroup,_s:sdhpdhE1t1Group,_d:sdhpdhEquipmentGroup,_t:sdhpdhE1t1GroupV2,'lumSdhpdhCompl':lumSdhpdhCompl,'lumSdhpdhBasicCompl1':lumSdhpdhBasicCompl1,'lumSdhpdhBasicCompl2':lumSdhpdhBasicCompl2,'lumSdhpdhMIBObjects':lumSdhpdhMIBObjects,'sdhpdhGeneral':sdhpdhGeneral,_i:sdhpdhGeneralLastChangeTime,_j:sdhpdhGeneralStateLastChangeTime,_k:sdhpdhGeneralE1t1TableSize,_l:sdhpdhGeneralEquipmentTableSize,'sdhpdhE1t1List':sdhpdhE1t1List,'sdhpdhE1t1Table':sdhpdhE1t1Table,'sdhpdhE1t1Entry':sdhpdhE1t1Entry,_F:sdhpdhE1t1Index,_J:sdhpdhE1t1Name,_K:sdhpdhE1t1Descr,_L:sdhpdhE1t1AdminStatus,_M:sdhpdhE1t1OperStatus,_N:sdhpdhE1t1AlarmIndicationSignalW2C,_O:sdhpdhE1t1AlarmIndicationSignalC2W,_P:sdhpdhE1t1LossOfFrameC2W,_Q:sdhpdhE1t1LossOfFrameW2C,_R:sdhpdhE1t1UnEquipped,_S:sdhpdhE1t1ConnectionStatus,_T:sdhpdhE1t1SubChannelId,_U:sdhpdhE1t1MultiplexingInformation,_V:sdhpdhE1t1RxSignalStatus,_W:sdhpdhE1t1TxSignalStatus,_X:sdhpdhE1t1VcIndex,_Y:sdhpdhE1t1ClockDomain,_Z:sdhpdhE1t1TuAlarmIndicationSignalC2W,_a:sdhpdhE1t1TuLossOfPointerC2W,_b:sdhpdhE1t1FrameFormat,_q:sdhpdhE1t1EquipmentIndex,_r:sdhpdhE1t1SignalLabel,'sdhpdhEquipmentList':sdhpdhEquipmentList,'sdhpdhEquipmentTable':sdhpdhEquipmentTable,'sdhpdhEquipmentEntry':sdhpdhEquipmentEntry,_I:sdhpdhEquipmentIndex,_n:sdhpdhEquipmentName,_o:sdhpdhEquipmentMultiplexingStructure,_p:sdhpdhEquipmentChangeMultiplexStructureCommand})