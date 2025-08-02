_AG='h3cFlhChipGroup'
_AF='h3cFlhNotificationGroup'
_AE='h3cFlhOperationGroup'
_AD='h3cFlhFileGroup'
_AC='h3cFlhPartitionGroup'
_AB='h3cFlhGroup'
_AA='h3cFlhOperNotification'
_A9='h3cFlhOperFailReason'
_A8='h3cFlhOperServerPort'
_A7='h3cFlhOperRowStatus'
_A6='h3cFlhOperProgress'
_A5='h3cFlhOperEndNotification'
_A4='h3cFlhOperDestinationFile'
_A3='h3cFlhOperSourceFile'
_A2='h3cFlhOperPassword'
_A1='h3cFlhOperServerUser'
_A0='h3cFlhOperServerAddress'
_z='h3cFlhOperProtocol'
_y='h3cFlhOperType'
_x='h3cFlhFileChecksum'
_w='h3cFlhFileStatus'
_v='h3cFlhFileSize'
_u='h3cFlhFileName'
_t='h3cFlhPartFileNameLen'
_s='h3cFlhPartRequireErase'
_r='h3cFlhPartName'
_q='h3cFlhPartUpgradeMode'
_p='h3cFlhPartStatus'
_o='h3cFlhPartChecksumMethod'
_n='h3cFlhPartFileNum'
_m='h3cFlhPartSpaceFree'
_l='h3cFlhPartSpace'
_k='h3cFlhPartLastChip'
_j='h3cFlhPartFirstChip'
_i='h3cFlhChipEraseTimes'
_h='h3cFlhChipEraseTimesLimit'
_g='h3cFlhChipWriteTimes'
_f='h3cFlhChipWriteTimesLimit'
_e='h3cFlhChipDescr'
_d='h3cFlhChipID'
_c='h3cFlhKbyteSize'
_b='h3cFlhPartitionNum'
_a='h3cFlhMaxPartitions'
_Z='h3cFlhMinPartitionSize'
_Y='h3cFlhPartitionBool'
_X='h3cFlhRemovable'
_W='h3cFlhInitTime'
_V='h3cFlhDescr'
_U='h3cFlhChipNum'
_T='h3cFlhName'
_S='h3cFlhPos'
_R='h3cFlhSize'
_Q='h3cFlhSupportNum'
_P='h3cFlhOperIndex'
_O='h3cFlhFileIndex'
_N='h3cFlhChipSerialNo'
_M='TruthValue'
_L='IpAddress'
_K='h3cFlhOperStatus'
_J='h3cFlhPartIndex'
_I='not-accessible'
_H='bytes'
_G='h3cFlhIndex'
_F='DisplayString'
_E='read-create'
_D='Integer32'
_C='read-only'
_B='A3COM-HUAWEI-FLASH-MAN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
huaweiUtility,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','huaweiUtility')
PhysicalIndex,=mibBuilder.importSymbols('ENTITY-MIB','PhysicalIndex')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,_L,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','RowStatus','TextualConvention','TimeStamp',_M)
h3cFlash=ModuleIdentity((1,3,6,1,4,1,43,45,1,6,9))
class H3cFlashOperationStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31)));namedValues=NamedValues(*(('opInProgress',1),('opSuccess',2),('opInvalid',3),('opInvalidProtocol',4),('opInvalidSourceName',5),('opInvalidDestName',6),('opInvalidServerAddress',7),('opDeviceBusy',8),('opDeviceOpenError',9),('opDeviceError',10),('opDeviceNotProgrammable',11),('opDeviceFull',12),('opFileOpenError',13),('opFileTransferError',14),('opFileChecksumError',15),('opNoMemory',16),('opAuthFail',17),('opTimeout',18),('opUnknownFailure',19),('opDeleteFileOpenError',20),('opDeleteInvalidDevice',21),('opDeleteInvalidFunction',22),('opDeleteOperationError',23),('opDeleteInvalidFileName',24),('opDeleteDeviceBusy',25),('opDeleteParaError',26),('opDeleteInvalidPath',27),('opDeleteFileNotExistInSlave',28),('opDeleteFileFailedInSlave',29),('opSlaveFull',30),('opCopyToSlaveFailure',31)))
class H3cFlashPartitionUpgradeMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unknown',1),('rxbootFLH',2),('direct',3)))
class H3cFlashPartitionStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('readOnly',1),('runFromFlash',2),('readWrite',3)))
_H3cFlashManMIBObjects_ObjectIdentity=ObjectIdentity
h3cFlashManMIBObjects=_H3cFlashManMIBObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,6,9,1))
_H3cFlashDevice_ObjectIdentity=ObjectIdentity
h3cFlashDevice=_H3cFlashDevice_ObjectIdentity((1,3,6,1,4,1,43,45,1,6,9,1,1))
_H3cFlhSupportNum_Type=Integer32
_H3cFlhSupportNum_Object=MibScalar
h3cFlhSupportNum=_H3cFlhSupportNum_Object((1,3,6,1,4,1,43,45,1,6,9,1,1,1),_H3cFlhSupportNum_Type())
h3cFlhSupportNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cFlhSupportNum.setStatus(_A)
_H3cFlashTable_Object=MibTable
h3cFlashTable=_H3cFlashTable_Object((1,3,6,1,4,1,43,45,1,6,9,1,1,2))
if mibBuilder.loadTexts:h3cFlashTable.setStatus(_A)
_H3cFlashEntry_Object=MibTableRow
h3cFlashEntry=_H3cFlashEntry_Object((1,3,6,1,4,1,43,45,1,6,9,1,1,2,1))
h3cFlashEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:h3cFlashEntry.setStatus(_A)
class _H3cFlhIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cFlhIndex_Type.__name__=_D
_H3cFlhIndex_Object=MibTableColumn
h3cFlhIndex=_H3cFlhIndex_Object((1,3,6,1,4,1,43,45,1,6,9,1,1,2,1,1),_H3cFlhIndex_Type())
h3cFlhIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cFlhIndex.setStatus(_A)
_H3cFlhSize_Type=Integer32
_H3cFlhSize_Object=MibTableColumn
h3cFlhSize=_H3cFlhSize_Object((1,3,6,1,4,1,43,45,1,6,9,1,1,2,1,2),_H3cFlhSize_Type())
h3cFlhSize.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cFlhSize.setStatus(_A)
if mibBuilder.loadTexts:h3cFlhSize.setUnits(_H)
_H3cFlhPos_Type=PhysicalIndex
_H3cFlhPos_Object=MibTableColumn
h3cFlhPos=_H3cFlhPos_Object((1,3,6,1,4,1,43,45,1,6,9,1,1,2,1,3),_H3cFlhPos_Type())
h3cFlhPos.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cFlhPos.setStatus(_A)
class _H3cFlhName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cFlhName_Type.__name__=_F
_H3cFlhName_Object=MibTableColumn
h3cFlhName=_H3cFlhName_Object((1,3,6,1,4,1,43,45,1,6,9,1,1,2,1,4),_H3cFlhName_Type())
h3cFlhName.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cFlhName.setStatus(_A)
class _H3cFlhChipNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_H3cFlhChipNum_Type.__name__=_D
_H3cFlhChipNum_Object=MibTableColumn
h3cFlhChipNum=_H3cFlhChipNum_Object((1,3,6,1,4,1,43,45,1,6,9,1,1,2,1,5),_H3cFlhChipNum_Type())
h3cFlhChipNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cFlhChipNum.setStatus(_A)
class _H3cFlhDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_H3cFlhDescr_Type.__name__=_F
_H3cFlhDescr_Object=MibTableColumn
h3cFlhDescr=_H3cFlhDescr_Object((1,3,6,1,4,1,43,45,1,6,9,1,1,2,1,6),_H3cFlhDescr_Type())
h3cFlhDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cFlhDescr.setStatus(_A)
_H3cFlhInitTime_Type=TimeStamp
_H3cFlhInitTime_Object=MibTableColumn
h3cFlhInitTime=_H3cFlhInitTime_Object((1,3,6,1,4,1,43,45,1,6,9,1,1,2,1,8),_H3cFlhInitTime_Type())
h3cFlhInitTime.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cFlhInitTime.setStatus(_A)
_H3cFlhRemovable_Type=TruthValue
_H3cFlhRemovable_Object=MibTableColumn
h3cFlhRemovable=_H3cFlhRemovable_Object((1,3,6,1,4,1,43,45,1,6,9,1,1,2,1,9),_H3cFlhRemovable_Type())
h3cFlhRemovable.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cFlhRemovable.setStatus(_A)
_H3cFlhPartitionBool_Type=TruthValue
_H3cFlhPartitionBool_Object=MibTableColumn
h3cFlhPartitionBool=_H3cFlhPartitionBool_Object((1,3,6,1,4,1,43,45,1,6,9,1,1,2,1,11),_H3cFlhPartitionBool_Type())
h3cFlhPartitionBool.setMaxAccess('read-write')
if mibBuilder.loadTexts:h3cFlhPartitionBool.setStatus(_A)
_H3cFlhMinPartitionSize_Type=Integer32
_H3cFlhMinPartitionSize_Object=MibTableColumn
h3cFlhMinPartitionSize=_H3cFlhMinPartitionSize_Object((1,3,6,1,4,1,43,45,1,6,9,1,1,2,1,12),_H3cFlhMinPartitionSize_Type())
h3cFlhMinPartitionSize.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cFlhMinPartitionSize.setStatus(_A)
if mibBuilder.loadTexts:h3cFlhMinPartitionSize.setUnits(_H)
class _H3cFlhMaxPartitions_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_H3cFlhMaxPartitions_Type.__name__=_D
_H3cFlhMaxPartitions_Object=MibTableColumn
h3cFlhMaxPartitions=_H3cFlhMaxPartitions_Object((1,3,6,1,4,1,43,45,1,6,9,1,1,2,1,13),_H3cFlhMaxPartitions_Type())
h3cFlhMaxPartitions.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cFlhMaxPartitions.setStatus(_A)
_H3cFlhPartitionNum_Type=Integer32
_H3cFlhPartitionNum_Object=MibTableColumn
h3cFlhPartitionNum=_H3cFlhPartitionNum_Object((1,3,6,1,4,1,43,45,1,6,9,1,1,2,1,14),_H3cFlhPartitionNum_Type())
h3cFlhPartitionNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cFlhPartitionNum.setStatus(_A)
_H3cFlhKbyteSize_Type=Integer32
_H3cFlhKbyteSize_Object=MibTableColumn
h3cFlhKbyteSize=_H3cFlhKbyteSize_Object((1,3,6,1,4,1,43,45,1,6,9,1,1,2,1,15),_H3cFlhKbyteSize_Type())
h3cFlhKbyteSize.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cFlhKbyteSize.setStatus(_A)
if mibBuilder.loadTexts:h3cFlhKbyteSize.setUnits('kbytes')
_H3cFlashChips_ObjectIdentity=ObjectIdentity
h3cFlashChips=_H3cFlashChips_ObjectIdentity((1,3,6,1,4,1,43,45,1,6,9,1,1,3))
_H3cFlhChipTable_Object=MibTable
h3cFlhChipTable=_H3cFlhChipTable_Object((1,3,6,1,4,1,43,45,1,6,9,1,1,3,1))
if mibBuilder.loadTexts:h3cFlhChipTable.setStatus(_A)
_H3cFlhChipEntry_Object=MibTableRow
h3cFlhChipEntry=_H3cFlhChipEntry_Object((1,3,6,1,4,1,43,45,1,6,9,1,1,3,1,1))
h3cFlhChipEntry.setIndexNames((0,_B,_G),(0,_B,_N))
if mibBuilder.loadTexts:h3cFlhChipEntry.setStatus(_A)
class _H3cFlhChipSerialNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_H3cFlhChipSerialNo_Type.__name__=_D
_H3cFlhChipSerialNo_Object=MibTableColumn
h3cFlhChipSerialNo=_H3cFlhChipSerialNo_Object((1,3,6,1,4,1,43,45,1,6,9,1,1,3,1,1,1),_H3cFlhChipSerialNo_Type())
h3cFlhChipSerialNo.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cFlhChipSerialNo.setStatus(_A)
class _H3cFlhChipID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,5))
_H3cFlhChipID_Type.__name__=_F
_H3cFlhChipID_Object=MibTableColumn
h3cFlhChipID=_H3cFlhChipID_Object((1,3,6,1,4,1,43,45,1,6,9,1,1,3,1,1,2),_H3cFlhChipID_Type())
h3cFlhChipID.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cFlhChipID.setStatus(_A)
class _H3cFlhChipDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_H3cFlhChipDescr_Type.__name__=_F
_H3cFlhChipDescr_Object=MibTableColumn
h3cFlhChipDescr=_H3cFlhChipDescr_Object((1,3,6,1,4,1,43,45,1,6,9,1,1,3,1,1,3),_H3cFlhChipDescr_Type())
h3cFlhChipDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cFlhChipDescr.setStatus(_A)
_H3cFlhChipWriteTimesLimit_Type=Integer32
_H3cFlhChipWriteTimesLimit_Object=MibTableColumn
h3cFlhChipWriteTimesLimit=_H3cFlhChipWriteTimesLimit_Object((1,3,6,1,4,1,43,45,1,6,9,1,1,3,1,1,4),_H3cFlhChipWriteTimesLimit_Type())
h3cFlhChipWriteTimesLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cFlhChipWriteTimesLimit.setStatus(_A)
_H3cFlhChipWriteTimes_Type=Counter32
_H3cFlhChipWriteTimes_Object=MibTableColumn
h3cFlhChipWriteTimes=_H3cFlhChipWriteTimes_Object((1,3,6,1,4,1,43,45,1,6,9,1,1,3,1,1,5),_H3cFlhChipWriteTimes_Type())
h3cFlhChipWriteTimes.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cFlhChipWriteTimes.setStatus(_A)
_H3cFlhChipEraseTimesLimit_Type=Integer32
_H3cFlhChipEraseTimesLimit_Object=MibTableColumn
h3cFlhChipEraseTimesLimit=_H3cFlhChipEraseTimesLimit_Object((1,3,6,1,4,1,43,45,1,6,9,1,1,3,1,1,6),_H3cFlhChipEraseTimesLimit_Type())
h3cFlhChipEraseTimesLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cFlhChipEraseTimesLimit.setStatus(_A)
_H3cFlhChipEraseTimes_Type=Counter32
_H3cFlhChipEraseTimes_Object=MibTableColumn
h3cFlhChipEraseTimes=_H3cFlhChipEraseTimes_Object((1,3,6,1,4,1,43,45,1,6,9,1,1,3,1,1,7),_H3cFlhChipEraseTimes_Type())
h3cFlhChipEraseTimes.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cFlhChipEraseTimes.setStatus(_A)
_H3cFlashPartitions_ObjectIdentity=ObjectIdentity
h3cFlashPartitions=_H3cFlashPartitions_ObjectIdentity((1,3,6,1,4,1,43,45,1,6,9,1,1,4))
_H3cFlhPartitionTable_Object=MibTable
h3cFlhPartitionTable=_H3cFlhPartitionTable_Object((1,3,6,1,4,1,43,45,1,6,9,1,1,4,1))
if mibBuilder.loadTexts:h3cFlhPartitionTable.setStatus(_A)
_H3cFlhPartitionEntry_Object=MibTableRow
h3cFlhPartitionEntry=_H3cFlhPartitionEntry_Object((1,3,6,1,4,1,43,45,1,6,9,1,1,4,1,1))
h3cFlhPartitionEntry.setIndexNames((0,_B,_G),(0,_B,_J))
if mibBuilder.loadTexts:h3cFlhPartitionEntry.setStatus(_A)
class _H3cFlhPartIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_H3cFlhPartIndex_Type.__name__=_D
_H3cFlhPartIndex_Object=MibTableColumn
h3cFlhPartIndex=_H3cFlhPartIndex_Object((1,3,6,1,4,1,43,45,1,6,9,1,1,4,1,1,1),_H3cFlhPartIndex_Type())
h3cFlhPartIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cFlhPartIndex.setStatus(_A)
class _H3cFlhPartFirstChip_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_H3cFlhPartFirstChip_Type.__name__=_D
_H3cFlhPartFirstChip_Object=MibTableColumn
h3cFlhPartFirstChip=_H3cFlhPartFirstChip_Object((1,3,6,1,4,1,43,45,1,6,9,1,1,4,1,1,2),_H3cFlhPartFirstChip_Type())
h3cFlhPartFirstChip.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cFlhPartFirstChip.setStatus(_A)
class _H3cFlhPartLastChip_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_H3cFlhPartLastChip_Type.__name__=_D
_H3cFlhPartLastChip_Object=MibTableColumn
h3cFlhPartLastChip=_H3cFlhPartLastChip_Object((1,3,6,1,4,1,43,45,1,6,9,1,1,4,1,1,3),_H3cFlhPartLastChip_Type())
h3cFlhPartLastChip.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cFlhPartLastChip.setStatus(_A)
_H3cFlhPartSpace_Type=Integer32
_H3cFlhPartSpace_Object=MibTableColumn
h3cFlhPartSpace=_H3cFlhPartSpace_Object((1,3,6,1,4,1,43,45,1,6,9,1,1,4,1,1,4),_H3cFlhPartSpace_Type())
h3cFlhPartSpace.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cFlhPartSpace.setStatus(_A)
if mibBuilder.loadTexts:h3cFlhPartSpace.setUnits(_H)
_H3cFlhPartSpaceFree_Type=Gauge32
_H3cFlhPartSpaceFree_Object=MibTableColumn
h3cFlhPartSpaceFree=_H3cFlhPartSpaceFree_Object((1,3,6,1,4,1,43,45,1,6,9,1,1,4,1,1,5),_H3cFlhPartSpaceFree_Type())
h3cFlhPartSpaceFree.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cFlhPartSpaceFree.setStatus(_A)
if mibBuilder.loadTexts:h3cFlhPartSpaceFree.setUnits(_H)
_H3cFlhPartFileNum_Type=Integer32
_H3cFlhPartFileNum_Object=MibTableColumn
h3cFlhPartFileNum=_H3cFlhPartFileNum_Object((1,3,6,1,4,1,43,45,1,6,9,1,1,4,1,1,6),_H3cFlhPartFileNum_Type())
h3cFlhPartFileNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cFlhPartFileNum.setStatus(_A)
class _H3cFlhPartChecksumMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('simpleChecksum',1),('undefined',2),('simpleCRC',3)))
_H3cFlhPartChecksumMethod_Type.__name__=_D
_H3cFlhPartChecksumMethod_Object=MibTableColumn
h3cFlhPartChecksumMethod=_H3cFlhPartChecksumMethod_Object((1,3,6,1,4,1,43,45,1,6,9,1,1,4,1,1,7),_H3cFlhPartChecksumMethod_Type())
h3cFlhPartChecksumMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cFlhPartChecksumMethod.setStatus(_A)
_H3cFlhPartStatus_Type=H3cFlashPartitionStatus
_H3cFlhPartStatus_Object=MibTableColumn
h3cFlhPartStatus=_H3cFlhPartStatus_Object((1,3,6,1,4,1,43,45,1,6,9,1,1,4,1,1,8),_H3cFlhPartStatus_Type())
h3cFlhPartStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cFlhPartStatus.setStatus(_A)
_H3cFlhPartUpgradeMode_Type=H3cFlashPartitionUpgradeMode
_H3cFlhPartUpgradeMode_Object=MibTableColumn
h3cFlhPartUpgradeMode=_H3cFlhPartUpgradeMode_Object((1,3,6,1,4,1,43,45,1,6,9,1,1,4,1,1,9),_H3cFlhPartUpgradeMode_Type())
h3cFlhPartUpgradeMode.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cFlhPartUpgradeMode.setStatus(_A)
class _H3cFlhPartName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cFlhPartName_Type.__name__=_F
_H3cFlhPartName_Object=MibTableColumn
h3cFlhPartName=_H3cFlhPartName_Object((1,3,6,1,4,1,43,45,1,6,9,1,1,4,1,1,10),_H3cFlhPartName_Type())
h3cFlhPartName.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cFlhPartName.setStatus(_A)
_H3cFlhPartRequireErase_Type=TruthValue
_H3cFlhPartRequireErase_Object=MibTableColumn
h3cFlhPartRequireErase=_H3cFlhPartRequireErase_Object((1,3,6,1,4,1,43,45,1,6,9,1,1,4,1,1,11),_H3cFlhPartRequireErase_Type())
h3cFlhPartRequireErase.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cFlhPartRequireErase.setStatus(_A)
class _H3cFlhPartFileNameLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_H3cFlhPartFileNameLen_Type.__name__=_D
_H3cFlhPartFileNameLen_Object=MibTableColumn
h3cFlhPartFileNameLen=_H3cFlhPartFileNameLen_Object((1,3,6,1,4,1,43,45,1,6,9,1,1,4,1,1,12),_H3cFlhPartFileNameLen_Type())
h3cFlhPartFileNameLen.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cFlhPartFileNameLen.setStatus(_A)
_H3cFlhFiles_ObjectIdentity=ObjectIdentity
h3cFlhFiles=_H3cFlhFiles_ObjectIdentity((1,3,6,1,4,1,43,45,1,6,9,1,1,4,2))
_H3cFlhFileTable_Object=MibTable
h3cFlhFileTable=_H3cFlhFileTable_Object((1,3,6,1,4,1,43,45,1,6,9,1,1,4,2,1))
if mibBuilder.loadTexts:h3cFlhFileTable.setStatus(_A)
_H3cFlhFileEntry_Object=MibTableRow
h3cFlhFileEntry=_H3cFlhFileEntry_Object((1,3,6,1,4,1,43,45,1,6,9,1,1,4,2,1,1))
h3cFlhFileEntry.setIndexNames((0,_B,_G),(0,_B,_J),(0,_B,_O))
if mibBuilder.loadTexts:h3cFlhFileEntry.setStatus(_A)
class _H3cFlhFileIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cFlhFileIndex_Type.__name__=_D
_H3cFlhFileIndex_Object=MibTableColumn
h3cFlhFileIndex=_H3cFlhFileIndex_Object((1,3,6,1,4,1,43,45,1,6,9,1,1,4,2,1,1,1),_H3cFlhFileIndex_Type())
h3cFlhFileIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cFlhFileIndex.setStatus(_A)
class _H3cFlhFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_H3cFlhFileName_Type.__name__=_F
_H3cFlhFileName_Object=MibTableColumn
h3cFlhFileName=_H3cFlhFileName_Object((1,3,6,1,4,1,43,45,1,6,9,1,1,4,2,1,1,2),_H3cFlhFileName_Type())
h3cFlhFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cFlhFileName.setStatus(_A)
_H3cFlhFileSize_Type=Integer32
_H3cFlhFileSize_Object=MibTableColumn
h3cFlhFileSize=_H3cFlhFileSize_Object((1,3,6,1,4,1,43,45,1,6,9,1,1,4,2,1,1,3),_H3cFlhFileSize_Type())
h3cFlhFileSize.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cFlhFileSize.setStatus(_A)
class _H3cFlhFileStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('deleted',1),('invalidChecksum',2),('valid',3)))
_H3cFlhFileStatus_Type.__name__=_D
_H3cFlhFileStatus_Object=MibTableColumn
h3cFlhFileStatus=_H3cFlhFileStatus_Object((1,3,6,1,4,1,43,45,1,6,9,1,1,4,2,1,1,4),_H3cFlhFileStatus_Type())
h3cFlhFileStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cFlhFileStatus.setStatus(_A)
_H3cFlhFileChecksum_Type=OctetString
_H3cFlhFileChecksum_Object=MibTableColumn
h3cFlhFileChecksum=_H3cFlhFileChecksum_Object((1,3,6,1,4,1,43,45,1,6,9,1,1,4,2,1,1,5),_H3cFlhFileChecksum_Type())
h3cFlhFileChecksum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cFlhFileChecksum.setStatus(_A)
_H3cFlashOperate_ObjectIdentity=ObjectIdentity
h3cFlashOperate=_H3cFlashOperate_ObjectIdentity((1,3,6,1,4,1,43,45,1,6,9,1,2))
_H3cFlhOpTable_Object=MibTable
h3cFlhOpTable=_H3cFlhOpTable_Object((1,3,6,1,4,1,43,45,1,6,9,1,2,1))
if mibBuilder.loadTexts:h3cFlhOpTable.setStatus(_A)
_H3cFlhOpEntry_Object=MibTableRow
h3cFlhOpEntry=_H3cFlhOpEntry_Object((1,3,6,1,4,1,43,45,1,6,9,1,2,1,1))
h3cFlhOpEntry.setIndexNames((0,_B,_P))
if mibBuilder.loadTexts:h3cFlhOpEntry.setStatus(_A)
class _H3cFlhOperIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cFlhOperIndex_Type.__name__=_D
_H3cFlhOperIndex_Object=MibTableColumn
h3cFlhOperIndex=_H3cFlhOperIndex_Object((1,3,6,1,4,1,43,45,1,6,9,1,2,1,1,1),_H3cFlhOperIndex_Type())
h3cFlhOperIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cFlhOperIndex.setStatus(_A)
class _H3cFlhOperType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('net2FlashWithErase',1),('net2FlashWithoutErase',2),('flash2Net',3),('delete',4),('rename',5)))
_H3cFlhOperType_Type.__name__=_D
_H3cFlhOperType_Object=MibTableColumn
h3cFlhOperType=_H3cFlhOperType_Object((1,3,6,1,4,1,43,45,1,6,9,1,2,1,1,2),_H3cFlhOperType_Type())
h3cFlhOperType.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cFlhOperType.setStatus(_A)
class _H3cFlhOperProtocol_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ftp',1),('tftp',2),('clusterftp',3),('clustertftp',4)))
_H3cFlhOperProtocol_Type.__name__=_D
_H3cFlhOperProtocol_Object=MibTableColumn
h3cFlhOperProtocol=_H3cFlhOperProtocol_Object((1,3,6,1,4,1,43,45,1,6,9,1,2,1,1,3),_H3cFlhOperProtocol_Type())
h3cFlhOperProtocol.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cFlhOperProtocol.setStatus(_A)
class _H3cFlhOperServerAddress_Type(IpAddress):defaultHexValue='FFFFFFFF'
_H3cFlhOperServerAddress_Type.__name__=_L
_H3cFlhOperServerAddress_Object=MibTableColumn
h3cFlhOperServerAddress=_H3cFlhOperServerAddress_Object((1,3,6,1,4,1,43,45,1,6,9,1,2,1,1,4),_H3cFlhOperServerAddress_Type())
h3cFlhOperServerAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cFlhOperServerAddress.setStatus('deprecated')
_H3cFlhOperServerUser_Type=DisplayString
_H3cFlhOperServerUser_Object=MibTableColumn
h3cFlhOperServerUser=_H3cFlhOperServerUser_Object((1,3,6,1,4,1,43,45,1,6,9,1,2,1,1,5),_H3cFlhOperServerUser_Type())
h3cFlhOperServerUser.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cFlhOperServerUser.setStatus(_A)
_H3cFlhOperPassword_Type=DisplayString
_H3cFlhOperPassword_Object=MibTableColumn
h3cFlhOperPassword=_H3cFlhOperPassword_Object((1,3,6,1,4,1,43,45,1,6,9,1,2,1,1,6),_H3cFlhOperPassword_Type())
h3cFlhOperPassword.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cFlhOperPassword.setStatus(_A)
class _H3cFlhOperSourceFile_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_H3cFlhOperSourceFile_Type.__name__=_F
_H3cFlhOperSourceFile_Object=MibTableColumn
h3cFlhOperSourceFile=_H3cFlhOperSourceFile_Object((1,3,6,1,4,1,43,45,1,6,9,1,2,1,1,7),_H3cFlhOperSourceFile_Type())
h3cFlhOperSourceFile.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cFlhOperSourceFile.setStatus(_A)
_H3cFlhOperDestinationFile_Type=DisplayString
_H3cFlhOperDestinationFile_Object=MibTableColumn
h3cFlhOperDestinationFile=_H3cFlhOperDestinationFile_Object((1,3,6,1,4,1,43,45,1,6,9,1,2,1,1,8),_H3cFlhOperDestinationFile_Type())
h3cFlhOperDestinationFile.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cFlhOperDestinationFile.setStatus(_A)
_H3cFlhOperStatus_Type=H3cFlashOperationStatus
_H3cFlhOperStatus_Object=MibTableColumn
h3cFlhOperStatus=_H3cFlhOperStatus_Object((1,3,6,1,4,1,43,45,1,6,9,1,2,1,1,9),_H3cFlhOperStatus_Type())
h3cFlhOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cFlhOperStatus.setStatus(_A)
class _H3cFlhOperEndNotification_Type(TruthValue):defaultValue=2
_H3cFlhOperEndNotification_Type.__name__=_M
_H3cFlhOperEndNotification_Object=MibTableColumn
h3cFlhOperEndNotification=_H3cFlhOperEndNotification_Object((1,3,6,1,4,1,43,45,1,6,9,1,2,1,1,10),_H3cFlhOperEndNotification_Type())
h3cFlhOperEndNotification.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cFlhOperEndNotification.setStatus(_A)
_H3cFlhOperProgress_Type=TimeTicks
_H3cFlhOperProgress_Object=MibTableColumn
h3cFlhOperProgress=_H3cFlhOperProgress_Object((1,3,6,1,4,1,43,45,1,6,9,1,2,1,1,11),_H3cFlhOperProgress_Type())
h3cFlhOperProgress.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cFlhOperProgress.setStatus(_A)
_H3cFlhOperRowStatus_Type=RowStatus
_H3cFlhOperRowStatus_Object=MibTableColumn
h3cFlhOperRowStatus=_H3cFlhOperRowStatus_Object((1,3,6,1,4,1,43,45,1,6,9,1,2,1,1,12),_H3cFlhOperRowStatus_Type())
h3cFlhOperRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cFlhOperRowStatus.setStatus(_A)
class _H3cFlhOperServerPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_H3cFlhOperServerPort_Type.__name__=_D
_H3cFlhOperServerPort_Object=MibTableColumn
h3cFlhOperServerPort=_H3cFlhOperServerPort_Object((1,3,6,1,4,1,43,45,1,6,9,1,2,1,1,13),_H3cFlhOperServerPort_Type())
h3cFlhOperServerPort.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cFlhOperServerPort.setStatus(_A)
_H3cFlhOperFailReason_Type=DisplayString
_H3cFlhOperFailReason_Object=MibTableColumn
h3cFlhOperFailReason=_H3cFlhOperFailReason_Object((1,3,6,1,4,1,43,45,1,6,9,1,2,1,1,14),_H3cFlhOperFailReason_Type())
h3cFlhOperFailReason.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cFlhOperFailReason.setStatus(_A)
_H3cFlhOperSrvAddrType_Type=InetAddressType
_H3cFlhOperSrvAddrType_Object=MibTableColumn
h3cFlhOperSrvAddrType=_H3cFlhOperSrvAddrType_Object((1,3,6,1,4,1,43,45,1,6,9,1,2,1,1,15),_H3cFlhOperSrvAddrType_Type())
h3cFlhOperSrvAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cFlhOperSrvAddrType.setStatus(_A)
_H3cFlhOperSrvAddrRev_Type=InetAddress
_H3cFlhOperSrvAddrRev_Object=MibTableColumn
h3cFlhOperSrvAddrRev=_H3cFlhOperSrvAddrRev_Object((1,3,6,1,4,1,43,45,1,6,9,1,2,1,1,16),_H3cFlhOperSrvAddrRev_Type())
h3cFlhOperSrvAddrRev.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cFlhOperSrvAddrRev.setStatus(_A)
_H3cFlhOperSrvVPNName_Type=DisplayString
_H3cFlhOperSrvVPNName_Object=MibTableColumn
h3cFlhOperSrvVPNName=_H3cFlhOperSrvVPNName_Object((1,3,6,1,4,1,43,45,1,6,9,1,2,1,1,17),_H3cFlhOperSrvVPNName_Type())
h3cFlhOperSrvVPNName.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cFlhOperSrvVPNName.setStatus(_A)
_H3cFlashNotification_ObjectIdentity=ObjectIdentity
h3cFlashNotification=_H3cFlashNotification_ObjectIdentity((1,3,6,1,4,1,43,45,1,6,9,1,3))
_H3cFlashMIBConformance_ObjectIdentity=ObjectIdentity
h3cFlashMIBConformance=_H3cFlashMIBConformance_ObjectIdentity((1,3,6,1,4,1,43,45,1,6,9,2))
_H3cFlhMIBCompliances_ObjectIdentity=ObjectIdentity
h3cFlhMIBCompliances=_H3cFlhMIBCompliances_ObjectIdentity((1,3,6,1,4,1,43,45,1,6,9,2,1))
_H3cFlashMIBGroups_ObjectIdentity=ObjectIdentity
h3cFlashMIBGroups=_H3cFlashMIBGroups_ObjectIdentity((1,3,6,1,4,1,43,45,1,6,9,2,2))
h3cFlhGroup=ObjectGroup((1,3,6,1,4,1,43,45,1,6,9,2,2,1))
h3cFlhGroup.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_G),(_B,_c)))
if mibBuilder.loadTexts:h3cFlhGroup.setStatus(_A)
h3cFlhChipGroup=ObjectGroup((1,3,6,1,4,1,43,45,1,6,9,2,2,3))
h3cFlhChipGroup.setObjects(*((_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i)))
if mibBuilder.loadTexts:h3cFlhChipGroup.setStatus(_A)
h3cFlhPartitionGroup=ObjectGroup((1,3,6,1,4,1,43,45,1,6,9,2,2,4))
h3cFlhPartitionGroup.setObjects(*((_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t)))
if mibBuilder.loadTexts:h3cFlhPartitionGroup.setStatus(_A)
h3cFlhFileGroup=ObjectGroup((1,3,6,1,4,1,43,45,1,6,9,2,2,5))
h3cFlhFileGroup.setObjects(*((_B,_u),(_B,_v),(_B,_w),(_B,_x)))
if mibBuilder.loadTexts:h3cFlhFileGroup.setStatus(_A)
h3cFlhOperationGroup=ObjectGroup((1,3,6,1,4,1,43,45,1,6,9,2,2,6))
h3cFlhOperationGroup.setObjects(*((_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_K),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9)))
if mibBuilder.loadTexts:h3cFlhOperationGroup.setStatus(_A)
h3cFlhOperNotification=NotificationType((1,3,6,1,4,1,43,45,1,6,9,1,3,1))
h3cFlhOperNotification.setObjects((_B,_K))
if mibBuilder.loadTexts:h3cFlhOperNotification.setStatus(_A)
h3cFlhNotificationGroup=NotificationGroup((1,3,6,1,4,1,43,45,1,6,9,2,2,7))
h3cFlhNotificationGroup.setObjects((_B,_AA))
if mibBuilder.loadTexts:h3cFlhNotificationGroup.setStatus(_A)
h3cFlhMIBCompliance=ModuleCompliance((1,3,6,1,4,1,43,45,1,6,9,2,1,1))
h3cFlhMIBCompliance.setObjects(*((_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG)))
if mibBuilder.loadTexts:h3cFlhMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'H3cFlashOperationStatus':H3cFlashOperationStatus,'H3cFlashPartitionUpgradeMode':H3cFlashPartitionUpgradeMode,'H3cFlashPartitionStatus':H3cFlashPartitionStatus,'h3cFlash':h3cFlash,'h3cFlashManMIBObjects':h3cFlashManMIBObjects,'h3cFlashDevice':h3cFlashDevice,_Q:h3cFlhSupportNum,'h3cFlashTable':h3cFlashTable,'h3cFlashEntry':h3cFlashEntry,_G:h3cFlhIndex,_R:h3cFlhSize,_S:h3cFlhPos,_T:h3cFlhName,_U:h3cFlhChipNum,_V:h3cFlhDescr,_W:h3cFlhInitTime,_X:h3cFlhRemovable,_Y:h3cFlhPartitionBool,_Z:h3cFlhMinPartitionSize,_a:h3cFlhMaxPartitions,_b:h3cFlhPartitionNum,_c:h3cFlhKbyteSize,'h3cFlashChips':h3cFlashChips,'h3cFlhChipTable':h3cFlhChipTable,'h3cFlhChipEntry':h3cFlhChipEntry,_N:h3cFlhChipSerialNo,_d:h3cFlhChipID,_e:h3cFlhChipDescr,_f:h3cFlhChipWriteTimesLimit,_g:h3cFlhChipWriteTimes,_h:h3cFlhChipEraseTimesLimit,_i:h3cFlhChipEraseTimes,'h3cFlashPartitions':h3cFlashPartitions,'h3cFlhPartitionTable':h3cFlhPartitionTable,'h3cFlhPartitionEntry':h3cFlhPartitionEntry,_J:h3cFlhPartIndex,_j:h3cFlhPartFirstChip,_k:h3cFlhPartLastChip,_l:h3cFlhPartSpace,_m:h3cFlhPartSpaceFree,_n:h3cFlhPartFileNum,_o:h3cFlhPartChecksumMethod,_p:h3cFlhPartStatus,_q:h3cFlhPartUpgradeMode,_r:h3cFlhPartName,_s:h3cFlhPartRequireErase,_t:h3cFlhPartFileNameLen,'h3cFlhFiles':h3cFlhFiles,'h3cFlhFileTable':h3cFlhFileTable,'h3cFlhFileEntry':h3cFlhFileEntry,_O:h3cFlhFileIndex,_u:h3cFlhFileName,_v:h3cFlhFileSize,_w:h3cFlhFileStatus,_x:h3cFlhFileChecksum,'h3cFlashOperate':h3cFlashOperate,'h3cFlhOpTable':h3cFlhOpTable,'h3cFlhOpEntry':h3cFlhOpEntry,_P:h3cFlhOperIndex,_y:h3cFlhOperType,_z:h3cFlhOperProtocol,_A0:h3cFlhOperServerAddress,_A1:h3cFlhOperServerUser,_A2:h3cFlhOperPassword,_A3:h3cFlhOperSourceFile,_A4:h3cFlhOperDestinationFile,_K:h3cFlhOperStatus,_A5:h3cFlhOperEndNotification,_A6:h3cFlhOperProgress,_A7:h3cFlhOperRowStatus,_A8:h3cFlhOperServerPort,_A9:h3cFlhOperFailReason,'h3cFlhOperSrvAddrType':h3cFlhOperSrvAddrType,'h3cFlhOperSrvAddrRev':h3cFlhOperSrvAddrRev,'h3cFlhOperSrvVPNName':h3cFlhOperSrvVPNName,'h3cFlashNotification':h3cFlashNotification,_AA:h3cFlhOperNotification,'h3cFlashMIBConformance':h3cFlashMIBConformance,'h3cFlhMIBCompliances':h3cFlhMIBCompliances,'h3cFlhMIBCompliance':h3cFlhMIBCompliance,'h3cFlashMIBGroups':h3cFlashMIBGroups,_AB:h3cFlhGroup,_AG:h3cFlhChipGroup,_AC:h3cFlhPartitionGroup,_AD:h3cFlhFileGroup,_AE:h3cFlhOperationGroup,_AF:h3cFlhNotificationGroup})