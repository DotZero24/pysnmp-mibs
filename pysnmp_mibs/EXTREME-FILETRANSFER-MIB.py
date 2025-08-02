_I='extremeFileTransferIndex'
_H='EXTREME-FILETRANSFER-MIB'
_G='DisplayString'
_F='OwnerString'
_E='OctetString'
_D='read-only'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
extremeAgent,=mibBuilder.importSymbols('EXTREME-BASE-MIB','extremeAgent')
OwnerString,=mibBuilder.importSymbols('RMON-MIB',_F)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TestAndIncr=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','RowStatus','TextualConvention','TestAndIncr')
extremeFileTransfer=ModuleIdentity((1,3,6,1,4,1,1916,1,10))
_ExtremeFileTransferGroup_ObjectIdentity=ObjectIdentity
extremeFileTransferGroup=_ExtremeFileTransferGroup_ObjectIdentity((1,3,6,1,4,1,1916,1,10,1))
_ExtremeFileTransferNextAvailableIndex_Type=TestAndIncr
_ExtremeFileTransferNextAvailableIndex_Object=MibScalar
extremeFileTransferNextAvailableIndex=_ExtremeFileTransferNextAvailableIndex_Object((1,3,6,1,4,1,1916,1,10,1,1),_ExtremeFileTransferNextAvailableIndex_Type())
extremeFileTransferNextAvailableIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeFileTransferNextAvailableIndex.setStatus(_A)
_ExtremeFileTransferTable_Object=MibTable
extremeFileTransferTable=_ExtremeFileTransferTable_Object((1,3,6,1,4,1,1916,1,10,1,2))
if mibBuilder.loadTexts:extremeFileTransferTable.setStatus(_A)
_ExtremeFileTransferEntry_Object=MibTableRow
extremeFileTransferEntry=_ExtremeFileTransferEntry_Object((1,3,6,1,4,1,1916,1,10,1,2,1))
extremeFileTransferEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:extremeFileTransferEntry.setStatus(_A)
_ExtremeFileTransferIndex_Type=Integer32
_ExtremeFileTransferIndex_Object=MibTableColumn
extremeFileTransferIndex=_ExtremeFileTransferIndex_Object((1,3,6,1,4,1,1916,1,10,1,2,1,1),_ExtremeFileTransferIndex_Type())
extremeFileTransferIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:extremeFileTransferIndex.setStatus(_A)
_ExtremeFileTransferServerAddress_Type=IpAddress
_ExtremeFileTransferServerAddress_Object=MibTableColumn
extremeFileTransferServerAddress=_ExtremeFileTransferServerAddress_Object((1,3,6,1,4,1,1916,1,10,1,2,1,2),_ExtremeFileTransferServerAddress_Type())
extremeFileTransferServerAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeFileTransferServerAddress.setStatus(_A)
class _ExtremeFileTransferFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ExtremeFileTransferFileName_Type.__name__=_G
_ExtremeFileTransferFileName_Object=MibTableColumn
extremeFileTransferFileName=_ExtremeFileTransferFileName_Object((1,3,6,1,4,1,1916,1,10,1,2,1,3),_ExtremeFileTransferFileName_Type())
extremeFileTransferFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeFileTransferFileName.setStatus(_A)
class _ExtremeFileTransferOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('downloadImageToPrimaryImmediate',1),('downloadImageToSecondaryImmediate',2),('downloadConfigImmediate',3),('uploadConfigImmediate',4),('scheduleConfigUploadPeriodic',5),('scheduleConfigUploadOnce',6),('scheduleImageDownloadToPrimaryOnce',7),('scheduleImageDownloadToSecondaryOnce',8),('scheduleConfigDownloadOnce',9)))
_ExtremeFileTransferOperation_Type.__name__=_C
_ExtremeFileTransferOperation_Object=MibTableColumn
extremeFileTransferOperation=_ExtremeFileTransferOperation_Object((1,3,6,1,4,1,1916,1,10,1,2,1,4),_ExtremeFileTransferOperation_Type())
extremeFileTransferOperation.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeFileTransferOperation.setStatus(_A)
class _ExtremeFileTransferScheduledTime_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(8,8),ValueSizeConstraint(11,11))
_ExtremeFileTransferScheduledTime_Type.__name__=_E
_ExtremeFileTransferScheduledTime_Object=MibTableColumn
extremeFileTransferScheduledTime=_ExtremeFileTransferScheduledTime_Object((1,3,6,1,4,1,1916,1,10,1,2,1,5),_ExtremeFileTransferScheduledTime_Type())
extremeFileTransferScheduledTime.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeFileTransferScheduledTime.setStatus(_A)
class _ExtremeFileTransferStartAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('start',1),('cancel',2)))
_ExtremeFileTransferStartAdminStatus_Type.__name__=_C
_ExtremeFileTransferStartAdminStatus_Object=MibTableColumn
extremeFileTransferStartAdminStatus=_ExtremeFileTransferStartAdminStatus_Object((1,3,6,1,4,1,1916,1,10,1,2,1,6),_ExtremeFileTransferStartAdminStatus_Type())
extremeFileTransferStartAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeFileTransferStartAdminStatus.setStatus(_A)
class _ExtremeFileTransferStartOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('idle',1),('scheduled',2),('inProgress',3)))
_ExtremeFileTransferStartOperStatus_Type.__name__=_C
_ExtremeFileTransferStartOperStatus_Object=MibTableColumn
extremeFileTransferStartOperStatus=_ExtremeFileTransferStartOperStatus_Object((1,3,6,1,4,1,1916,1,10,1,2,1,7),_ExtremeFileTransferStartOperStatus_Type())
extremeFileTransferStartOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeFileTransferStartOperStatus.setStatus(_A)
class _ExtremeFileTransferLastExecutionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('success',1),('statusUnknown',2),('generalError',3),('noResponseFromServer',4),('checksumError',5),('incompatibleImage',6),('tftpFileNotFound',7),('tftpAccessViolation',8),('fileTooLarge',9),('downloadInProgress',10)))
_ExtremeFileTransferLastExecutionStatus_Type.__name__=_C
_ExtremeFileTransferLastExecutionStatus_Object=MibTableColumn
extremeFileTransferLastExecutionStatus=_ExtremeFileTransferLastExecutionStatus_Object((1,3,6,1,4,1,1916,1,10,1,2,1,8),_ExtremeFileTransferLastExecutionStatus_Type())
extremeFileTransferLastExecutionStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeFileTransferLastExecutionStatus.setStatus(_A)
class _ExtremeFileTransferOwner_Type(OwnerString):subtypeSpec=OwnerString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ExtremeFileTransferOwner_Type.__name__=_F
_ExtremeFileTransferOwner_Object=MibTableColumn
extremeFileTransferOwner=_ExtremeFileTransferOwner_Object((1,3,6,1,4,1,1916,1,10,1,2,1,9),_ExtremeFileTransferOwner_Type())
extremeFileTransferOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeFileTransferOwner.setStatus(_A)
_ExtremeFileTransferRowStatus_Type=RowStatus
_ExtremeFileTransferRowStatus_Object=MibTableColumn
extremeFileTransferRowStatus=_ExtremeFileTransferRowStatus_Object((1,3,6,1,4,1,1916,1,10,1,2,1,10),_ExtremeFileTransferRowStatus_Type())
extremeFileTransferRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeFileTransferRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'extremeFileTransfer':extremeFileTransfer,'extremeFileTransferGroup':extremeFileTransferGroup,'extremeFileTransferNextAvailableIndex':extremeFileTransferNextAvailableIndex,'extremeFileTransferTable':extremeFileTransferTable,'extremeFileTransferEntry':extremeFileTransferEntry,_I:extremeFileTransferIndex,'extremeFileTransferServerAddress':extremeFileTransferServerAddress,'extremeFileTransferFileName':extremeFileTransferFileName,'extremeFileTransferOperation':extremeFileTransferOperation,'extremeFileTransferScheduledTime':extremeFileTransferScheduledTime,'extremeFileTransferStartAdminStatus':extremeFileTransferStartAdminStatus,'extremeFileTransferStartOperStatus':extremeFileTransferStartOperStatus,'extremeFileTransferLastExecutionStatus':extremeFileTransferLastExecutionStatus,'extremeFileTransferOwner':extremeFileTransferOwner,'extremeFileTransferRowStatus':extremeFileTransferRowStatus})