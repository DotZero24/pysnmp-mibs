_AK='hpnicfFlhChipGroup'
_AJ='hpnicfFlhNotificationGroup'
_AI='hpnicfFlhOperationGroup'
_AH='hpnicfFlhFileGroup'
_AG='hpnicfFlhPartitionGroup'
_AF='hpnicfFlhGroup'
_AE='hpnicfFlhOperNotification'
_AD='hpnicfFlhOperFailReason'
_AC='hpnicfFlhOperServerPort'
_AB='hpnicfFlhOperRowStatus'
_AA='hpnicfFlhOperProgress'
_A9='hpnicfFlhOperEndNotification'
_A8='hpnicfFlhOperDestinationFile'
_A7='hpnicfFlhOperSourceFile'
_A6='hpnicfFlhOperPassword'
_A5='hpnicfFlhOperServerUser'
_A4='hpnicfFlhOperServerAddress'
_A3='hpnicfFlhOperProtocol'
_A2='hpnicfFlhOperType'
_A1='hpnicfFlhFileChecksum'
_A0='hpnicfFlhFileStatus'
_z='hpnicfFlhFileSize'
_y='hpnicfFlhFileName'
_x='hpnicfFlhPartPathForGlobalOpt'
_w='hpnicfFlhPartBootable'
_v='hpnicfFlhPartFileNameLen'
_u='hpnicfFlhPartRequireErase'
_t='hpnicfFlhPartName'
_s='hpnicfFlhPartUpgradeMode'
_r='hpnicfFlhPartStatus'
_q='hpnicfFlhPartChecksumMethod'
_p='hpnicfFlhPartFileNum'
_o='hpnicfFlhPartSpaceFree'
_n='hpnicfFlhPartSpace'
_m='hpnicfFlhPartLastChip'
_l='hpnicfFlhPartFirstChip'
_k='hpnicfFlhChipEraseTimes'
_j='hpnicfFlhChipEraseTimesLimit'
_i='hpnicfFlhChipWriteTimes'
_h='hpnicfFlhChipWriteTimesLimit'
_g='hpnicfFlhChipDescr'
_f='hpnicfFlhChipID'
_e='hpnicfFlhKbyteSize'
_d='hpnicfFlhPartitionNum'
_c='hpnicfFlhMaxPartitions'
_b='hpnicfFlhMinPartitionSize'
_a='hpnicfFlhPartitionBool'
_Z='hpnicfFlhRemovable'
_Y='hpnicfFlhInitTime'
_X='hpnicfFlhDescr'
_W='hpnicfFlhChipNum'
_V='hpnicfFlhName'
_U='hpnicfFlhPos'
_T='hpnicfFlhSize'
_S='hpnicfFlhSupportNum'
_R='hpnicfFlhOperIndex'
_Q='hpnicfFlhFileIndex'
_P='hpnicfFlhChipSerialNo'
_O='read-write'
_N='TruthValue'
_M='IpAddress'
_L='hpnicfFlhOperStatus'
_K='hpnicfFlhPartIndex'
_J='not-accessible'
_I='deprecated'
_H='hpnicfFlhIndex'
_G='bytes'
_F='DisplayString'
_E='read-create'
_D='Integer32'
_C='read-only'
_B='HPN-ICF-FLASH-MAN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
PhysicalIndex,=mibBuilder.importSymbols('ENTITY-MIB','PhysicalIndex')
CounterBasedGauge64,=mibBuilder.importSymbols('HCNUM-TC','CounterBasedGauge64')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,_M,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','RowStatus','TextualConvention','TimeStamp',_N)
hpnicfFlash=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,5))
if mibBuilder.loadTexts:hpnicfFlash.setRevisions(('2013-05-23 00:00',))
class HpnicfFlashOperationStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31)));namedValues=NamedValues(*(('opInProgress',1),('opSuccess',2),('opInvalid',3),('opInvalidProtocol',4),('opInvalidSourceName',5),('opInvalidDestName',6),('opInvalidServerAddress',7),('opDeviceBusy',8),('opDeviceOpenError',9),('opDeviceError',10),('opDeviceNotProgrammable',11),('opDeviceFull',12),('opFileOpenError',13),('opFileTransferError',14),('opFileChecksumError',15),('opNoMemory',16),('opAuthFail',17),('opTimeout',18),('opUnknownFailure',19),('opDeleteFileOpenError',20),('opDeleteInvalidDevice',21),('opDeleteInvalidFunction',22),('opDeleteOperationError',23),('opDeleteInvalidFileName',24),('opDeleteDeviceBusy',25),('opDeleteParaError',26),('opDeleteInvalidPath',27),('opDeleteFileNotExistInSlave',28),('opDeleteFileFailedInSlave',29),('opSlaveFull',30),('opCopyToSlaveFailure',31)))
class HpnicfFlashPartitionUpgradeMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unknown',1),('rxbootFLH',2),('direct',3)))
class HpnicfFlashPartitionStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('readOnly',1),('runFromFlash',2),('readWrite',3)))
_HpnicfFlashManMIBObjects_ObjectIdentity=ObjectIdentity
hpnicfFlashManMIBObjects=_HpnicfFlashManMIBObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,5,1))
_HpnicfFlashDevice_ObjectIdentity=ObjectIdentity
hpnicfFlashDevice=_HpnicfFlashDevice_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,5,1,1))
_HpnicfFlhSupportNum_Type=Integer32
_HpnicfFlhSupportNum_Object=MibScalar
hpnicfFlhSupportNum=_HpnicfFlhSupportNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,1,1),_HpnicfFlhSupportNum_Type())
hpnicfFlhSupportNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlhSupportNum.setStatus(_A)
_HpnicfFlashTable_Object=MibTable
hpnicfFlashTable=_HpnicfFlashTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,1,2))
if mibBuilder.loadTexts:hpnicfFlashTable.setStatus(_A)
_HpnicfFlashEntry_Object=MibTableRow
hpnicfFlashEntry=_HpnicfFlashEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,1,2,1))
hpnicfFlashEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:hpnicfFlashEntry.setStatus(_A)
class _HpnicfFlhIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfFlhIndex_Type.__name__=_D
_HpnicfFlhIndex_Object=MibTableColumn
hpnicfFlhIndex=_HpnicfFlhIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,1,2,1,1),_HpnicfFlhIndex_Type())
hpnicfFlhIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlhIndex.setStatus(_A)
_HpnicfFlhSize_Type=Integer32
_HpnicfFlhSize_Object=MibTableColumn
hpnicfFlhSize=_HpnicfFlhSize_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,1,2,1,2),_HpnicfFlhSize_Type())
hpnicfFlhSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlhSize.setStatus(_I)
if mibBuilder.loadTexts:hpnicfFlhSize.setUnits(_G)
_HpnicfFlhPos_Type=PhysicalIndex
_HpnicfFlhPos_Object=MibTableColumn
hpnicfFlhPos=_HpnicfFlhPos_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,1,2,1,3),_HpnicfFlhPos_Type())
hpnicfFlhPos.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlhPos.setStatus(_A)
class _HpnicfFlhName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfFlhName_Type.__name__=_F
_HpnicfFlhName_Object=MibTableColumn
hpnicfFlhName=_HpnicfFlhName_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,1,2,1,4),_HpnicfFlhName_Type())
hpnicfFlhName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlhName.setStatus(_A)
class _HpnicfFlhChipNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_HpnicfFlhChipNum_Type.__name__=_D
_HpnicfFlhChipNum_Object=MibTableColumn
hpnicfFlhChipNum=_HpnicfFlhChipNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,1,2,1,5),_HpnicfFlhChipNum_Type())
hpnicfFlhChipNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlhChipNum.setStatus(_A)
class _HpnicfFlhDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HpnicfFlhDescr_Type.__name__=_F
_HpnicfFlhDescr_Object=MibTableColumn
hpnicfFlhDescr=_HpnicfFlhDescr_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,1,2,1,6),_HpnicfFlhDescr_Type())
hpnicfFlhDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlhDescr.setStatus(_A)
_HpnicfFlhInitTime_Type=TimeStamp
_HpnicfFlhInitTime_Object=MibTableColumn
hpnicfFlhInitTime=_HpnicfFlhInitTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,1,2,1,8),_HpnicfFlhInitTime_Type())
hpnicfFlhInitTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlhInitTime.setStatus(_A)
_HpnicfFlhRemovable_Type=TruthValue
_HpnicfFlhRemovable_Object=MibTableColumn
hpnicfFlhRemovable=_HpnicfFlhRemovable_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,1,2,1,9),_HpnicfFlhRemovable_Type())
hpnicfFlhRemovable.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlhRemovable.setStatus(_A)
_HpnicfFlhPartitionBool_Type=TruthValue
_HpnicfFlhPartitionBool_Object=MibTableColumn
hpnicfFlhPartitionBool=_HpnicfFlhPartitionBool_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,1,2,1,11),_HpnicfFlhPartitionBool_Type())
hpnicfFlhPartitionBool.setMaxAccess(_O)
if mibBuilder.loadTexts:hpnicfFlhPartitionBool.setStatus(_A)
_HpnicfFlhMinPartitionSize_Type=Integer32
_HpnicfFlhMinPartitionSize_Object=MibTableColumn
hpnicfFlhMinPartitionSize=_HpnicfFlhMinPartitionSize_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,1,2,1,12),_HpnicfFlhMinPartitionSize_Type())
hpnicfFlhMinPartitionSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlhMinPartitionSize.setStatus(_A)
if mibBuilder.loadTexts:hpnicfFlhMinPartitionSize.setUnits(_G)
class _HpnicfFlhMaxPartitions_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_HpnicfFlhMaxPartitions_Type.__name__=_D
_HpnicfFlhMaxPartitions_Object=MibTableColumn
hpnicfFlhMaxPartitions=_HpnicfFlhMaxPartitions_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,1,2,1,13),_HpnicfFlhMaxPartitions_Type())
hpnicfFlhMaxPartitions.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlhMaxPartitions.setStatus(_A)
_HpnicfFlhPartitionNum_Type=Integer32
_HpnicfFlhPartitionNum_Object=MibTableColumn
hpnicfFlhPartitionNum=_HpnicfFlhPartitionNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,1,2,1,14),_HpnicfFlhPartitionNum_Type())
hpnicfFlhPartitionNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlhPartitionNum.setStatus(_A)
_HpnicfFlhKbyteSize_Type=Integer32
_HpnicfFlhKbyteSize_Object=MibTableColumn
hpnicfFlhKbyteSize=_HpnicfFlhKbyteSize_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,1,2,1,15),_HpnicfFlhKbyteSize_Type())
hpnicfFlhKbyteSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlhKbyteSize.setStatus(_A)
if mibBuilder.loadTexts:hpnicfFlhKbyteSize.setUnits('kbytes')
_HpnicfFlhHCSize_Type=CounterBasedGauge64
_HpnicfFlhHCSize_Object=MibTableColumn
hpnicfFlhHCSize=_HpnicfFlhHCSize_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,1,2,1,16),_HpnicfFlhHCSize_Type())
hpnicfFlhHCSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlhHCSize.setStatus(_A)
if mibBuilder.loadTexts:hpnicfFlhHCSize.setUnits(_G)
_HpnicfFlashChips_ObjectIdentity=ObjectIdentity
hpnicfFlashChips=_HpnicfFlashChips_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,5,1,1,3))
_HpnicfFlhChipTable_Object=MibTable
hpnicfFlhChipTable=_HpnicfFlhChipTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,1,3,1))
if mibBuilder.loadTexts:hpnicfFlhChipTable.setStatus(_A)
_HpnicfFlhChipEntry_Object=MibTableRow
hpnicfFlhChipEntry=_HpnicfFlhChipEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,1,3,1,1))
hpnicfFlhChipEntry.setIndexNames((0,_B,_H),(0,_B,_P))
if mibBuilder.loadTexts:hpnicfFlhChipEntry.setStatus(_A)
class _HpnicfFlhChipSerialNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_HpnicfFlhChipSerialNo_Type.__name__=_D
_HpnicfFlhChipSerialNo_Object=MibTableColumn
hpnicfFlhChipSerialNo=_HpnicfFlhChipSerialNo_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,1,3,1,1,1),_HpnicfFlhChipSerialNo_Type())
hpnicfFlhChipSerialNo.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfFlhChipSerialNo.setStatus(_A)
class _HpnicfFlhChipID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,5))
_HpnicfFlhChipID_Type.__name__=_F
_HpnicfFlhChipID_Object=MibTableColumn
hpnicfFlhChipID=_HpnicfFlhChipID_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,1,3,1,1,2),_HpnicfFlhChipID_Type())
hpnicfFlhChipID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlhChipID.setStatus(_A)
class _HpnicfFlhChipDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HpnicfFlhChipDescr_Type.__name__=_F
_HpnicfFlhChipDescr_Object=MibTableColumn
hpnicfFlhChipDescr=_HpnicfFlhChipDescr_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,1,3,1,1,3),_HpnicfFlhChipDescr_Type())
hpnicfFlhChipDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlhChipDescr.setStatus(_A)
_HpnicfFlhChipWriteTimesLimit_Type=Integer32
_HpnicfFlhChipWriteTimesLimit_Object=MibTableColumn
hpnicfFlhChipWriteTimesLimit=_HpnicfFlhChipWriteTimesLimit_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,1,3,1,1,4),_HpnicfFlhChipWriteTimesLimit_Type())
hpnicfFlhChipWriteTimesLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlhChipWriteTimesLimit.setStatus(_A)
_HpnicfFlhChipWriteTimes_Type=Counter32
_HpnicfFlhChipWriteTimes_Object=MibTableColumn
hpnicfFlhChipWriteTimes=_HpnicfFlhChipWriteTimes_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,1,3,1,1,5),_HpnicfFlhChipWriteTimes_Type())
hpnicfFlhChipWriteTimes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlhChipWriteTimes.setStatus(_A)
_HpnicfFlhChipEraseTimesLimit_Type=Integer32
_HpnicfFlhChipEraseTimesLimit_Object=MibTableColumn
hpnicfFlhChipEraseTimesLimit=_HpnicfFlhChipEraseTimesLimit_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,1,3,1,1,6),_HpnicfFlhChipEraseTimesLimit_Type())
hpnicfFlhChipEraseTimesLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlhChipEraseTimesLimit.setStatus(_A)
_HpnicfFlhChipEraseTimes_Type=Counter32
_HpnicfFlhChipEraseTimes_Object=MibTableColumn
hpnicfFlhChipEraseTimes=_HpnicfFlhChipEraseTimes_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,1,3,1,1,7),_HpnicfFlhChipEraseTimes_Type())
hpnicfFlhChipEraseTimes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlhChipEraseTimes.setStatus(_A)
_HpnicfFlashPartitions_ObjectIdentity=ObjectIdentity
hpnicfFlashPartitions=_HpnicfFlashPartitions_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,5,1,1,4))
_HpnicfFlhPartitionTable_Object=MibTable
hpnicfFlhPartitionTable=_HpnicfFlhPartitionTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,1,4,1))
if mibBuilder.loadTexts:hpnicfFlhPartitionTable.setStatus(_A)
_HpnicfFlhPartitionEntry_Object=MibTableRow
hpnicfFlhPartitionEntry=_HpnicfFlhPartitionEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,1,4,1,1))
hpnicfFlhPartitionEntry.setIndexNames((0,_B,_H),(0,_B,_K))
if mibBuilder.loadTexts:hpnicfFlhPartitionEntry.setStatus(_A)
class _HpnicfFlhPartIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_HpnicfFlhPartIndex_Type.__name__=_D
_HpnicfFlhPartIndex_Object=MibTableColumn
hpnicfFlhPartIndex=_HpnicfFlhPartIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,1,4,1,1,1),_HpnicfFlhPartIndex_Type())
hpnicfFlhPartIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfFlhPartIndex.setStatus(_A)
class _HpnicfFlhPartFirstChip_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_HpnicfFlhPartFirstChip_Type.__name__=_D
_HpnicfFlhPartFirstChip_Object=MibTableColumn
hpnicfFlhPartFirstChip=_HpnicfFlhPartFirstChip_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,1,4,1,1,2),_HpnicfFlhPartFirstChip_Type())
hpnicfFlhPartFirstChip.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlhPartFirstChip.setStatus(_A)
class _HpnicfFlhPartLastChip_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_HpnicfFlhPartLastChip_Type.__name__=_D
_HpnicfFlhPartLastChip_Object=MibTableColumn
hpnicfFlhPartLastChip=_HpnicfFlhPartLastChip_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,1,4,1,1,3),_HpnicfFlhPartLastChip_Type())
hpnicfFlhPartLastChip.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlhPartLastChip.setStatus(_A)
_HpnicfFlhPartSpace_Type=Integer32
_HpnicfFlhPartSpace_Object=MibTableColumn
hpnicfFlhPartSpace=_HpnicfFlhPartSpace_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,1,4,1,1,4),_HpnicfFlhPartSpace_Type())
hpnicfFlhPartSpace.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlhPartSpace.setStatus(_I)
if mibBuilder.loadTexts:hpnicfFlhPartSpace.setUnits(_G)
_HpnicfFlhPartSpaceFree_Type=Gauge32
_HpnicfFlhPartSpaceFree_Object=MibTableColumn
hpnicfFlhPartSpaceFree=_HpnicfFlhPartSpaceFree_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,1,4,1,1,5),_HpnicfFlhPartSpaceFree_Type())
hpnicfFlhPartSpaceFree.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlhPartSpaceFree.setStatus(_I)
if mibBuilder.loadTexts:hpnicfFlhPartSpaceFree.setUnits(_G)
_HpnicfFlhPartFileNum_Type=Integer32
_HpnicfFlhPartFileNum_Object=MibTableColumn
hpnicfFlhPartFileNum=_HpnicfFlhPartFileNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,1,4,1,1,6),_HpnicfFlhPartFileNum_Type())
hpnicfFlhPartFileNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlhPartFileNum.setStatus(_A)
class _HpnicfFlhPartChecksumMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('simpleChecksum',1),('undefined',2),('simpleCRC',3)))
_HpnicfFlhPartChecksumMethod_Type.__name__=_D
_HpnicfFlhPartChecksumMethod_Object=MibTableColumn
hpnicfFlhPartChecksumMethod=_HpnicfFlhPartChecksumMethod_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,1,4,1,1,7),_HpnicfFlhPartChecksumMethod_Type())
hpnicfFlhPartChecksumMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlhPartChecksumMethod.setStatus(_A)
_HpnicfFlhPartStatus_Type=HpnicfFlashPartitionStatus
_HpnicfFlhPartStatus_Object=MibTableColumn
hpnicfFlhPartStatus=_HpnicfFlhPartStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,1,4,1,1,8),_HpnicfFlhPartStatus_Type())
hpnicfFlhPartStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlhPartStatus.setStatus(_A)
_HpnicfFlhPartUpgradeMode_Type=HpnicfFlashPartitionUpgradeMode
_HpnicfFlhPartUpgradeMode_Object=MibTableColumn
hpnicfFlhPartUpgradeMode=_HpnicfFlhPartUpgradeMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,1,4,1,1,9),_HpnicfFlhPartUpgradeMode_Type())
hpnicfFlhPartUpgradeMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlhPartUpgradeMode.setStatus(_A)
class _HpnicfFlhPartName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfFlhPartName_Type.__name__=_F
_HpnicfFlhPartName_Object=MibTableColumn
hpnicfFlhPartName=_HpnicfFlhPartName_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,1,4,1,1,10),_HpnicfFlhPartName_Type())
hpnicfFlhPartName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlhPartName.setStatus(_A)
_HpnicfFlhPartRequireErase_Type=TruthValue
_HpnicfFlhPartRequireErase_Object=MibTableColumn
hpnicfFlhPartRequireErase=_HpnicfFlhPartRequireErase_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,1,4,1,1,11),_HpnicfFlhPartRequireErase_Type())
hpnicfFlhPartRequireErase.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlhPartRequireErase.setStatus(_A)
class _HpnicfFlhPartFileNameLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_HpnicfFlhPartFileNameLen_Type.__name__=_D
_HpnicfFlhPartFileNameLen_Object=MibTableColumn
hpnicfFlhPartFileNameLen=_HpnicfFlhPartFileNameLen_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,1,4,1,1,12),_HpnicfFlhPartFileNameLen_Type())
hpnicfFlhPartFileNameLen.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlhPartFileNameLen.setStatus(_A)
_HpnicfFlhPartBootable_Type=TruthValue
_HpnicfFlhPartBootable_Object=MibTableColumn
hpnicfFlhPartBootable=_HpnicfFlhPartBootable_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,1,4,1,1,13),_HpnicfFlhPartBootable_Type())
hpnicfFlhPartBootable.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlhPartBootable.setStatus(_A)
_HpnicfFlhPartPathForGlobalOpt_Type=TruthValue
_HpnicfFlhPartPathForGlobalOpt_Object=MibTableColumn
hpnicfFlhPartPathForGlobalOpt=_HpnicfFlhPartPathForGlobalOpt_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,1,4,1,1,14),_HpnicfFlhPartPathForGlobalOpt_Type())
hpnicfFlhPartPathForGlobalOpt.setMaxAccess(_O)
if mibBuilder.loadTexts:hpnicfFlhPartPathForGlobalOpt.setStatus(_A)
_HpnicfFlhPartHCSpace_Type=CounterBasedGauge64
_HpnicfFlhPartHCSpace_Object=MibTableColumn
hpnicfFlhPartHCSpace=_HpnicfFlhPartHCSpace_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,1,4,1,1,15),_HpnicfFlhPartHCSpace_Type())
hpnicfFlhPartHCSpace.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlhPartHCSpace.setStatus(_A)
if mibBuilder.loadTexts:hpnicfFlhPartHCSpace.setUnits(_G)
_HpnicfFlhPartHCSpaceFree_Type=CounterBasedGauge64
_HpnicfFlhPartHCSpaceFree_Object=MibTableColumn
hpnicfFlhPartHCSpaceFree=_HpnicfFlhPartHCSpaceFree_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,1,4,1,1,16),_HpnicfFlhPartHCSpaceFree_Type())
hpnicfFlhPartHCSpaceFree.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlhPartHCSpaceFree.setStatus(_A)
if mibBuilder.loadTexts:hpnicfFlhPartHCSpaceFree.setUnits(_G)
_HpnicfFlhFiles_ObjectIdentity=ObjectIdentity
hpnicfFlhFiles=_HpnicfFlhFiles_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,5,1,1,4,2))
_HpnicfFlhFileTable_Object=MibTable
hpnicfFlhFileTable=_HpnicfFlhFileTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,1,4,2,1))
if mibBuilder.loadTexts:hpnicfFlhFileTable.setStatus(_A)
_HpnicfFlhFileEntry_Object=MibTableRow
hpnicfFlhFileEntry=_HpnicfFlhFileEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,1,4,2,1,1))
hpnicfFlhFileEntry.setIndexNames((0,_B,_H),(0,_B,_K),(0,_B,_Q))
if mibBuilder.loadTexts:hpnicfFlhFileEntry.setStatus(_A)
class _HpnicfFlhFileIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfFlhFileIndex_Type.__name__=_D
_HpnicfFlhFileIndex_Object=MibTableColumn
hpnicfFlhFileIndex=_HpnicfFlhFileIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,1,4,2,1,1,1),_HpnicfFlhFileIndex_Type())
hpnicfFlhFileIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfFlhFileIndex.setStatus(_A)
class _HpnicfFlhFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_HpnicfFlhFileName_Type.__name__=_F
_HpnicfFlhFileName_Object=MibTableColumn
hpnicfFlhFileName=_HpnicfFlhFileName_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,1,4,2,1,1,2),_HpnicfFlhFileName_Type())
hpnicfFlhFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlhFileName.setStatus(_A)
_HpnicfFlhFileSize_Type=Integer32
_HpnicfFlhFileSize_Object=MibTableColumn
hpnicfFlhFileSize=_HpnicfFlhFileSize_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,1,4,2,1,1,3),_HpnicfFlhFileSize_Type())
hpnicfFlhFileSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlhFileSize.setStatus(_I)
class _HpnicfFlhFileStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('deleted',1),('invalidChecksum',2),('valid',3)))
_HpnicfFlhFileStatus_Type.__name__=_D
_HpnicfFlhFileStatus_Object=MibTableColumn
hpnicfFlhFileStatus=_HpnicfFlhFileStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,1,4,2,1,1,4),_HpnicfFlhFileStatus_Type())
hpnicfFlhFileStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlhFileStatus.setStatus(_A)
_HpnicfFlhFileChecksum_Type=OctetString
_HpnicfFlhFileChecksum_Object=MibTableColumn
hpnicfFlhFileChecksum=_HpnicfFlhFileChecksum_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,1,4,2,1,1,5),_HpnicfFlhFileChecksum_Type())
hpnicfFlhFileChecksum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlhFileChecksum.setStatus(_A)
_HpnicfFlhFileHCSize_Type=CounterBasedGauge64
_HpnicfFlhFileHCSize_Object=MibTableColumn
hpnicfFlhFileHCSize=_HpnicfFlhFileHCSize_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,1,4,2,1,1,6),_HpnicfFlhFileHCSize_Type())
hpnicfFlhFileHCSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlhFileHCSize.setStatus(_A)
if mibBuilder.loadTexts:hpnicfFlhFileHCSize.setUnits(_G)
_HpnicfFlashOperate_ObjectIdentity=ObjectIdentity
hpnicfFlashOperate=_HpnicfFlashOperate_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,5,1,2))
_HpnicfFlhOpTable_Object=MibTable
hpnicfFlhOpTable=_HpnicfFlhOpTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,2,1))
if mibBuilder.loadTexts:hpnicfFlhOpTable.setStatus(_A)
_HpnicfFlhOpEntry_Object=MibTableRow
hpnicfFlhOpEntry=_HpnicfFlhOpEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,2,1,1))
hpnicfFlhOpEntry.setIndexNames((0,_B,_R))
if mibBuilder.loadTexts:hpnicfFlhOpEntry.setStatus(_A)
class _HpnicfFlhOperIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfFlhOperIndex_Type.__name__=_D
_HpnicfFlhOperIndex_Object=MibTableColumn
hpnicfFlhOperIndex=_HpnicfFlhOperIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,2,1,1,1),_HpnicfFlhOperIndex_Type())
hpnicfFlhOperIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfFlhOperIndex.setStatus(_A)
class _HpnicfFlhOperType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('net2FlashWithErase',1),('net2FlashWithoutErase',2),('flash2Net',3),('delete',4),('rename',5)))
_HpnicfFlhOperType_Type.__name__=_D
_HpnicfFlhOperType_Object=MibTableColumn
hpnicfFlhOperType=_HpnicfFlhOperType_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,2,1,1,2),_HpnicfFlhOperType_Type())
hpnicfFlhOperType.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfFlhOperType.setStatus(_A)
class _HpnicfFlhOperProtocol_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ftp',1),('tftp',2),('clusterftp',3),('clustertftp',4)))
_HpnicfFlhOperProtocol_Type.__name__=_D
_HpnicfFlhOperProtocol_Object=MibTableColumn
hpnicfFlhOperProtocol=_HpnicfFlhOperProtocol_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,2,1,1,3),_HpnicfFlhOperProtocol_Type())
hpnicfFlhOperProtocol.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfFlhOperProtocol.setStatus(_A)
class _HpnicfFlhOperServerAddress_Type(IpAddress):defaultHexValue='FFFFFFFF'
_HpnicfFlhOperServerAddress_Type.__name__=_M
_HpnicfFlhOperServerAddress_Object=MibTableColumn
hpnicfFlhOperServerAddress=_HpnicfFlhOperServerAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,2,1,1,4),_HpnicfFlhOperServerAddress_Type())
hpnicfFlhOperServerAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfFlhOperServerAddress.setStatus(_I)
_HpnicfFlhOperServerUser_Type=DisplayString
_HpnicfFlhOperServerUser_Object=MibTableColumn
hpnicfFlhOperServerUser=_HpnicfFlhOperServerUser_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,2,1,1,5),_HpnicfFlhOperServerUser_Type())
hpnicfFlhOperServerUser.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfFlhOperServerUser.setStatus(_A)
_HpnicfFlhOperPassword_Type=DisplayString
_HpnicfFlhOperPassword_Object=MibTableColumn
hpnicfFlhOperPassword=_HpnicfFlhOperPassword_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,2,1,1,6),_HpnicfFlhOperPassword_Type())
hpnicfFlhOperPassword.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfFlhOperPassword.setStatus(_A)
class _HpnicfFlhOperSourceFile_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_HpnicfFlhOperSourceFile_Type.__name__=_F
_HpnicfFlhOperSourceFile_Object=MibTableColumn
hpnicfFlhOperSourceFile=_HpnicfFlhOperSourceFile_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,2,1,1,7),_HpnicfFlhOperSourceFile_Type())
hpnicfFlhOperSourceFile.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfFlhOperSourceFile.setStatus(_A)
_HpnicfFlhOperDestinationFile_Type=DisplayString
_HpnicfFlhOperDestinationFile_Object=MibTableColumn
hpnicfFlhOperDestinationFile=_HpnicfFlhOperDestinationFile_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,2,1,1,8),_HpnicfFlhOperDestinationFile_Type())
hpnicfFlhOperDestinationFile.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfFlhOperDestinationFile.setStatus(_A)
_HpnicfFlhOperStatus_Type=HpnicfFlashOperationStatus
_HpnicfFlhOperStatus_Object=MibTableColumn
hpnicfFlhOperStatus=_HpnicfFlhOperStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,2,1,1,9),_HpnicfFlhOperStatus_Type())
hpnicfFlhOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlhOperStatus.setStatus(_A)
class _HpnicfFlhOperEndNotification_Type(TruthValue):defaultValue=2
_HpnicfFlhOperEndNotification_Type.__name__=_N
_HpnicfFlhOperEndNotification_Object=MibTableColumn
hpnicfFlhOperEndNotification=_HpnicfFlhOperEndNotification_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,2,1,1,10),_HpnicfFlhOperEndNotification_Type())
hpnicfFlhOperEndNotification.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfFlhOperEndNotification.setStatus(_A)
_HpnicfFlhOperProgress_Type=TimeTicks
_HpnicfFlhOperProgress_Object=MibTableColumn
hpnicfFlhOperProgress=_HpnicfFlhOperProgress_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,2,1,1,11),_HpnicfFlhOperProgress_Type())
hpnicfFlhOperProgress.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlhOperProgress.setStatus(_A)
_HpnicfFlhOperRowStatus_Type=RowStatus
_HpnicfFlhOperRowStatus_Object=MibTableColumn
hpnicfFlhOperRowStatus=_HpnicfFlhOperRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,2,1,1,12),_HpnicfFlhOperRowStatus_Type())
hpnicfFlhOperRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfFlhOperRowStatus.setStatus(_A)
class _HpnicfFlhOperServerPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfFlhOperServerPort_Type.__name__=_D
_HpnicfFlhOperServerPort_Object=MibTableColumn
hpnicfFlhOperServerPort=_HpnicfFlhOperServerPort_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,2,1,1,13),_HpnicfFlhOperServerPort_Type())
hpnicfFlhOperServerPort.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfFlhOperServerPort.setStatus(_A)
_HpnicfFlhOperFailReason_Type=DisplayString
_HpnicfFlhOperFailReason_Object=MibTableColumn
hpnicfFlhOperFailReason=_HpnicfFlhOperFailReason_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,2,1,1,14),_HpnicfFlhOperFailReason_Type())
hpnicfFlhOperFailReason.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlhOperFailReason.setStatus(_A)
_HpnicfFlhOperSrvAddrType_Type=InetAddressType
_HpnicfFlhOperSrvAddrType_Object=MibTableColumn
hpnicfFlhOperSrvAddrType=_HpnicfFlhOperSrvAddrType_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,2,1,1,15),_HpnicfFlhOperSrvAddrType_Type())
hpnicfFlhOperSrvAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfFlhOperSrvAddrType.setStatus(_A)
_HpnicfFlhOperSrvAddrRev_Type=InetAddress
_HpnicfFlhOperSrvAddrRev_Object=MibTableColumn
hpnicfFlhOperSrvAddrRev=_HpnicfFlhOperSrvAddrRev_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,2,1,1,16),_HpnicfFlhOperSrvAddrRev_Type())
hpnicfFlhOperSrvAddrRev.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfFlhOperSrvAddrRev.setStatus(_A)
_HpnicfFlhOperSrvVPNName_Type=DisplayString
_HpnicfFlhOperSrvVPNName_Object=MibTableColumn
hpnicfFlhOperSrvVPNName=_HpnicfFlhOperSrvVPNName_Object((1,3,6,1,4,1,11,2,14,11,15,2,5,1,2,1,1,17),_HpnicfFlhOperSrvVPNName_Type())
hpnicfFlhOperSrvVPNName.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfFlhOperSrvVPNName.setStatus(_A)
_HpnicfFlashNotification_ObjectIdentity=ObjectIdentity
hpnicfFlashNotification=_HpnicfFlashNotification_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,5,1,3))
_HpnicfFlashMIBConformance_ObjectIdentity=ObjectIdentity
hpnicfFlashMIBConformance=_HpnicfFlashMIBConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,5,2))
_HpnicfFlhMIBCompliances_ObjectIdentity=ObjectIdentity
hpnicfFlhMIBCompliances=_HpnicfFlhMIBCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,5,2,1))
_HpnicfFlashMIBGroups_ObjectIdentity=ObjectIdentity
hpnicfFlashMIBGroups=_HpnicfFlashMIBGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,5,2,2))
hpnicfFlhGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,5,2,2,1))
hpnicfFlhGroup.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_H),(_B,_e)))
if mibBuilder.loadTexts:hpnicfFlhGroup.setStatus(_A)
hpnicfFlhChipGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,5,2,2,3))
hpnicfFlhChipGroup.setObjects(*((_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k)))
if mibBuilder.loadTexts:hpnicfFlhChipGroup.setStatus(_A)
hpnicfFlhPartitionGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,5,2,2,4))
hpnicfFlhPartitionGroup.setObjects(*((_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x)))
if mibBuilder.loadTexts:hpnicfFlhPartitionGroup.setStatus(_A)
hpnicfFlhFileGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,5,2,2,5))
hpnicfFlhFileGroup.setObjects(*((_B,_y),(_B,_z),(_B,_A0),(_B,_A1)))
if mibBuilder.loadTexts:hpnicfFlhFileGroup.setStatus(_A)
hpnicfFlhOperationGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,5,2,2,6))
hpnicfFlhOperationGroup.setObjects(*((_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_L),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD)))
if mibBuilder.loadTexts:hpnicfFlhOperationGroup.setStatus(_A)
hpnicfFlhOperNotification=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,5,1,3,1))
hpnicfFlhOperNotification.setObjects((_B,_L))
if mibBuilder.loadTexts:hpnicfFlhOperNotification.setStatus(_A)
hpnicfFlhNotificationGroup=NotificationGroup((1,3,6,1,4,1,11,2,14,11,15,2,5,2,2,7))
hpnicfFlhNotificationGroup.setObjects((_B,_AE))
if mibBuilder.loadTexts:hpnicfFlhNotificationGroup.setStatus(_A)
hpnicfFlhMIBCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,15,2,5,2,1,1))
hpnicfFlhMIBCompliance.setObjects(*((_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK)))
if mibBuilder.loadTexts:hpnicfFlhMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'HpnicfFlashOperationStatus':HpnicfFlashOperationStatus,'HpnicfFlashPartitionUpgradeMode':HpnicfFlashPartitionUpgradeMode,'HpnicfFlashPartitionStatus':HpnicfFlashPartitionStatus,'hpnicfFlash':hpnicfFlash,'hpnicfFlashManMIBObjects':hpnicfFlashManMIBObjects,'hpnicfFlashDevice':hpnicfFlashDevice,_S:hpnicfFlhSupportNum,'hpnicfFlashTable':hpnicfFlashTable,'hpnicfFlashEntry':hpnicfFlashEntry,_H:hpnicfFlhIndex,_T:hpnicfFlhSize,_U:hpnicfFlhPos,_V:hpnicfFlhName,_W:hpnicfFlhChipNum,_X:hpnicfFlhDescr,_Y:hpnicfFlhInitTime,_Z:hpnicfFlhRemovable,_a:hpnicfFlhPartitionBool,_b:hpnicfFlhMinPartitionSize,_c:hpnicfFlhMaxPartitions,_d:hpnicfFlhPartitionNum,_e:hpnicfFlhKbyteSize,'hpnicfFlhHCSize':hpnicfFlhHCSize,'hpnicfFlashChips':hpnicfFlashChips,'hpnicfFlhChipTable':hpnicfFlhChipTable,'hpnicfFlhChipEntry':hpnicfFlhChipEntry,_P:hpnicfFlhChipSerialNo,_f:hpnicfFlhChipID,_g:hpnicfFlhChipDescr,_h:hpnicfFlhChipWriteTimesLimit,_i:hpnicfFlhChipWriteTimes,_j:hpnicfFlhChipEraseTimesLimit,_k:hpnicfFlhChipEraseTimes,'hpnicfFlashPartitions':hpnicfFlashPartitions,'hpnicfFlhPartitionTable':hpnicfFlhPartitionTable,'hpnicfFlhPartitionEntry':hpnicfFlhPartitionEntry,_K:hpnicfFlhPartIndex,_l:hpnicfFlhPartFirstChip,_m:hpnicfFlhPartLastChip,_n:hpnicfFlhPartSpace,_o:hpnicfFlhPartSpaceFree,_p:hpnicfFlhPartFileNum,_q:hpnicfFlhPartChecksumMethod,_r:hpnicfFlhPartStatus,_s:hpnicfFlhPartUpgradeMode,_t:hpnicfFlhPartName,_u:hpnicfFlhPartRequireErase,_v:hpnicfFlhPartFileNameLen,_w:hpnicfFlhPartBootable,_x:hpnicfFlhPartPathForGlobalOpt,'hpnicfFlhPartHCSpace':hpnicfFlhPartHCSpace,'hpnicfFlhPartHCSpaceFree':hpnicfFlhPartHCSpaceFree,'hpnicfFlhFiles':hpnicfFlhFiles,'hpnicfFlhFileTable':hpnicfFlhFileTable,'hpnicfFlhFileEntry':hpnicfFlhFileEntry,_Q:hpnicfFlhFileIndex,_y:hpnicfFlhFileName,_z:hpnicfFlhFileSize,_A0:hpnicfFlhFileStatus,_A1:hpnicfFlhFileChecksum,'hpnicfFlhFileHCSize':hpnicfFlhFileHCSize,'hpnicfFlashOperate':hpnicfFlashOperate,'hpnicfFlhOpTable':hpnicfFlhOpTable,'hpnicfFlhOpEntry':hpnicfFlhOpEntry,_R:hpnicfFlhOperIndex,_A2:hpnicfFlhOperType,_A3:hpnicfFlhOperProtocol,_A4:hpnicfFlhOperServerAddress,_A5:hpnicfFlhOperServerUser,_A6:hpnicfFlhOperPassword,_A7:hpnicfFlhOperSourceFile,_A8:hpnicfFlhOperDestinationFile,_L:hpnicfFlhOperStatus,_A9:hpnicfFlhOperEndNotification,_AA:hpnicfFlhOperProgress,_AB:hpnicfFlhOperRowStatus,_AC:hpnicfFlhOperServerPort,_AD:hpnicfFlhOperFailReason,'hpnicfFlhOperSrvAddrType':hpnicfFlhOperSrvAddrType,'hpnicfFlhOperSrvAddrRev':hpnicfFlhOperSrvAddrRev,'hpnicfFlhOperSrvVPNName':hpnicfFlhOperSrvVPNName,'hpnicfFlashNotification':hpnicfFlashNotification,_AE:hpnicfFlhOperNotification,'hpnicfFlashMIBConformance':hpnicfFlashMIBConformance,'hpnicfFlhMIBCompliances':hpnicfFlhMIBCompliances,'hpnicfFlhMIBCompliance':hpnicfFlhMIBCompliance,'hpnicfFlashMIBGroups':hpnicfFlashMIBGroups,_AF:hpnicfFlhGroup,_AK:hpnicfFlhChipGroup,_AG:hpnicfFlhPartitionGroup,_AH:hpnicfFlhFileGroup,_AI:hpnicfFlhOperationGroup,_AJ:hpnicfFlhNotificationGroup})