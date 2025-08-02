_c='rlCopyUnitsList'
_b='RlCopySecSdAccessType'
_a='rlCopyOptionsIndex'
_Z='rlCopyHistoryInetHistoryIndex'
_Y='rlCopyInetIndex'
_X='rlCopyMessagesMessageIndex'
_W='rlCopyMessagesCopyIndex'
_V='rlCopyHistoryHistoryIndex'
_U='rlCopyIndex'
_T='serial'
_S='read-create'
_R='not-accessible'
_Q='DisplayString'
_P='copyFinished'
_O='copyTimedout'
_N='copyFailed'
_M='downloadInProgress'
_L='uploadInProgress'
_K='disable'
_J='enable'
_I='TruthValue'
_H='rndErrorSeverity'
_G='rndErrorDesc'
_F='NETGEAR-RADLAN-COPY-MIB'
_E='NETGEAR-RADLAN-DEVICEPARAMS-MIB'
_D='Integer32'
_C='read-only'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
rndErrorDesc,rndErrorSeverity=mibBuilder.importSymbols(_E,_G,_H)
rnd,rndNotifications=mibBuilder.importSymbols('NETGEAR-RADLAN-MIB','rnd','rndNotifications')
RlSecSdAccessType,=mibBuilder.importSymbols('NETGEAR-RADLAN-SECSD-MIB','RlSecSdAccessType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_Q,'PhysAddress','RowStatus','TextualConvention',_I)
rlCopy=ModuleIdentity((1,3,6,1,4,1,4526,17,87))
if mibBuilder.loadTexts:rlCopy.setRevisions(('2010-07-25 00:00','2010-05-11 00:00','2010-02-17 00:00','2009-08-10 00:00','2006-02-02 00:00','2003-09-22 00:00'))
class RlCopyApplicationType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('mcli',1),('cli',2),('ewb',3),('nms',4),('initerm',5),(_T,6)))
class RlCopyLocationType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('local',1),('anotherUnit',2),('tftp',3),('xmodem',4),('scp',5),(_T,6),('http',7),('https',8),('http-xml',9),('https-xml',10)))
class RlCopyFileType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*(('other',1),('runningConfig',2),('startupConfig',3),('backupConfig',4),('runningMibConfig',5),('startupMibConfig',6),('backupMibConfig',7),('image',8),('boot',9),('null',10),('logging',11),('mirrorConfig',12),('usb',13)))
class RlCopySecSdAccessType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('exclude',1),('include-encrypted',2),('include-decrypted',3),('default',4)))
_RlCopyMibVersion_Type=Integer32
_RlCopyMibVersion_Object=MibScalar
rlCopyMibVersion=_RlCopyMibVersion_Object((1,3,6,1,4,1,4526,17,87,1),_RlCopyMibVersion_Type())
rlCopyMibVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:rlCopyMibVersion.setStatus(_A)
_RlCopyTable_Object=MibTable
rlCopyTable=_RlCopyTable_Object((1,3,6,1,4,1,4526,17,87,2))
if mibBuilder.loadTexts:rlCopyTable.setStatus(_A)
_RlCopyEntry_Object=MibTableRow
rlCopyEntry=_RlCopyEntry_Object((1,3,6,1,4,1,4526,17,87,2,1))
rlCopyEntry.setIndexNames((0,_F,_U))
if mibBuilder.loadTexts:rlCopyEntry.setStatus(_A)
_RlCopyIndex_Type=Integer32
_RlCopyIndex_Object=MibTableColumn
rlCopyIndex=_RlCopyIndex_Object((1,3,6,1,4,1,4526,17,87,2,1,1),_RlCopyIndex_Type())
rlCopyIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rlCopyIndex.setStatus(_A)
_RlCopyApplicationId_Type=RlCopyApplicationType
_RlCopyApplicationId_Object=MibTableColumn
rlCopyApplicationId=_RlCopyApplicationId_Object((1,3,6,1,4,1,4526,17,87,2,1,2),_RlCopyApplicationId_Type())
rlCopyApplicationId.setMaxAccess(_C)
if mibBuilder.loadTexts:rlCopyApplicationId.setStatus(_A)
_RlCopySourceLocation_Type=RlCopyLocationType
_RlCopySourceLocation_Object=MibTableColumn
rlCopySourceLocation=_RlCopySourceLocation_Object((1,3,6,1,4,1,4526,17,87,2,1,3),_RlCopySourceLocation_Type())
rlCopySourceLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCopySourceLocation.setStatus(_A)
_RlCopySourceIpAddress_Type=IpAddress
_RlCopySourceIpAddress_Object=MibTableColumn
rlCopySourceIpAddress=_RlCopySourceIpAddress_Object((1,3,6,1,4,1,4526,17,87,2,1,4),_RlCopySourceIpAddress_Type())
rlCopySourceIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCopySourceIpAddress.setStatus(_A)
_RlCopySourceUnitNumber_Type=Integer32
_RlCopySourceUnitNumber_Object=MibTableColumn
rlCopySourceUnitNumber=_RlCopySourceUnitNumber_Object((1,3,6,1,4,1,4526,17,87,2,1,5),_RlCopySourceUnitNumber_Type())
rlCopySourceUnitNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCopySourceUnitNumber.setStatus(_A)
_RlCopySourceFileName_Type=DisplayString
_RlCopySourceFileName_Object=MibTableColumn
rlCopySourceFileName=_RlCopySourceFileName_Object((1,3,6,1,4,1,4526,17,87,2,1,6),_RlCopySourceFileName_Type())
rlCopySourceFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCopySourceFileName.setStatus(_A)
_RlCopySourceFileType_Type=RlCopyFileType
_RlCopySourceFileType_Object=MibTableColumn
rlCopySourceFileType=_RlCopySourceFileType_Object((1,3,6,1,4,1,4526,17,87,2,1,7),_RlCopySourceFileType_Type())
rlCopySourceFileType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCopySourceFileType.setStatus(_A)
_RlCopyDestinationLocation_Type=RlCopyLocationType
_RlCopyDestinationLocation_Object=MibTableColumn
rlCopyDestinationLocation=_RlCopyDestinationLocation_Object((1,3,6,1,4,1,4526,17,87,2,1,8),_RlCopyDestinationLocation_Type())
rlCopyDestinationLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCopyDestinationLocation.setStatus(_A)
_RlCopyDestinationIpAddress_Type=IpAddress
_RlCopyDestinationIpAddress_Object=MibTableColumn
rlCopyDestinationIpAddress=_RlCopyDestinationIpAddress_Object((1,3,6,1,4,1,4526,17,87,2,1,9),_RlCopyDestinationIpAddress_Type())
rlCopyDestinationIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCopyDestinationIpAddress.setStatus(_A)
_RlCopyDestinationUnitNumber_Type=Integer32
_RlCopyDestinationUnitNumber_Object=MibTableColumn
rlCopyDestinationUnitNumber=_RlCopyDestinationUnitNumber_Object((1,3,6,1,4,1,4526,17,87,2,1,10),_RlCopyDestinationUnitNumber_Type())
rlCopyDestinationUnitNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCopyDestinationUnitNumber.setStatus(_A)
_RlCopyDestinationFileName_Type=DisplayString
_RlCopyDestinationFileName_Object=MibTableColumn
rlCopyDestinationFileName=_RlCopyDestinationFileName_Object((1,3,6,1,4,1,4526,17,87,2,1,11),_RlCopyDestinationFileName_Type())
rlCopyDestinationFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCopyDestinationFileName.setStatus(_A)
_RlCopyDestinationFileType_Type=RlCopyFileType
_RlCopyDestinationFileType_Object=MibTableColumn
rlCopyDestinationFileType=_RlCopyDestinationFileType_Object((1,3,6,1,4,1,4526,17,87,2,1,12),_RlCopyDestinationFileType_Type())
rlCopyDestinationFileType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCopyDestinationFileType.setStatus(_A)
_RlCopyUpTime_Type=TimeTicks
_RlCopyUpTime_Object=MibTableColumn
rlCopyUpTime=_RlCopyUpTime_Object((1,3,6,1,4,1,4526,17,87,2,1,13),_RlCopyUpTime_Type())
rlCopyUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:rlCopyUpTime.setStatus(_A)
class _RlCopyOperationState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_L,1),(_M,2),(_N,3),(_O,4),(_P,5)))
_RlCopyOperationState_Type.__name__=_D
_RlCopyOperationState_Object=MibTableColumn
rlCopyOperationState=_RlCopyOperationState_Object((1,3,6,1,4,1,4526,17,87,2,1,14),_RlCopyOperationState_Type())
rlCopyOperationState.setMaxAccess(_C)
if mibBuilder.loadTexts:rlCopyOperationState.setStatus(_A)
_RlCopyBytesTransferred_Type=Integer32
_RlCopyBytesTransferred_Object=MibTableColumn
rlCopyBytesTransferred=_RlCopyBytesTransferred_Object((1,3,6,1,4,1,4526,17,87,2,1,15),_RlCopyBytesTransferred_Type())
rlCopyBytesTransferred.setMaxAccess(_C)
if mibBuilder.loadTexts:rlCopyBytesTransferred.setStatus(_A)
class _RlCopyInBackground_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_RlCopyInBackground_Type.__name__=_D
_RlCopyInBackground_Object=MibTableColumn
rlCopyInBackground=_RlCopyInBackground_Object((1,3,6,1,4,1,4526,17,87,2,1,16),_RlCopyInBackground_Type())
rlCopyInBackground.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCopyInBackground.setStatus(_A)
_RlCopyRowStatus_Type=RowStatus
_RlCopyRowStatus_Object=MibTableColumn
rlCopyRowStatus=_RlCopyRowStatus_Object((1,3,6,1,4,1,4526,17,87,2,1,17),_RlCopyRowStatus_Type())
rlCopyRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCopyRowStatus.setStatus(_A)
class _RlCopyHistoryIndex_Type(Integer32):defaultValue=0
_RlCopyHistoryIndex_Type.__name__=_D
_RlCopyHistoryIndex_Object=MibTableColumn
rlCopyHistoryIndex=_RlCopyHistoryIndex_Object((1,3,6,1,4,1,4526,17,87,2,1,18),_RlCopyHistoryIndex_Type())
rlCopyHistoryIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCopyHistoryIndex.setStatus(_A)
_RlCopyFreeHistoryIndex_Type=Integer32
_RlCopyFreeHistoryIndex_Object=MibScalar
rlCopyFreeHistoryIndex=_RlCopyFreeHistoryIndex_Object((1,3,6,1,4,1,4526,17,87,3),_RlCopyFreeHistoryIndex_Type())
rlCopyFreeHistoryIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rlCopyFreeHistoryIndex.setStatus(_A)
_RlCopyHistoryTable_Object=MibTable
rlCopyHistoryTable=_RlCopyHistoryTable_Object((1,3,6,1,4,1,4526,17,87,4))
if mibBuilder.loadTexts:rlCopyHistoryTable.setStatus(_A)
_RlCopyHistoryEntry_Object=MibTableRow
rlCopyHistoryEntry=_RlCopyHistoryEntry_Object((1,3,6,1,4,1,4526,17,87,4,1))
rlCopyHistoryEntry.setIndexNames((0,_F,_V))
if mibBuilder.loadTexts:rlCopyHistoryEntry.setStatus(_A)
_RlCopyHistoryHistoryIndex_Type=Integer32
_RlCopyHistoryHistoryIndex_Object=MibTableColumn
rlCopyHistoryHistoryIndex=_RlCopyHistoryHistoryIndex_Object((1,3,6,1,4,1,4526,17,87,4,1,1),_RlCopyHistoryHistoryIndex_Type())
rlCopyHistoryHistoryIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rlCopyHistoryHistoryIndex.setStatus(_A)
_RlCopyHistoryApplicationId_Type=RlCopyApplicationType
_RlCopyHistoryApplicationId_Object=MibTableColumn
rlCopyHistoryApplicationId=_RlCopyHistoryApplicationId_Object((1,3,6,1,4,1,4526,17,87,4,1,2),_RlCopyHistoryApplicationId_Type())
rlCopyHistoryApplicationId.setMaxAccess(_C)
if mibBuilder.loadTexts:rlCopyHistoryApplicationId.setStatus(_A)
_RlCopyHistorySourceLocation_Type=RlCopyLocationType
_RlCopyHistorySourceLocation_Object=MibTableColumn
rlCopyHistorySourceLocation=_RlCopyHistorySourceLocation_Object((1,3,6,1,4,1,4526,17,87,4,1,3),_RlCopyHistorySourceLocation_Type())
rlCopyHistorySourceLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCopyHistorySourceLocation.setStatus(_A)
_RlCopyHistorySourceIpAddress_Type=IpAddress
_RlCopyHistorySourceIpAddress_Object=MibTableColumn
rlCopyHistorySourceIpAddress=_RlCopyHistorySourceIpAddress_Object((1,3,6,1,4,1,4526,17,87,4,1,4),_RlCopyHistorySourceIpAddress_Type())
rlCopyHistorySourceIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCopyHistorySourceIpAddress.setStatus(_A)
_RlCopyHistorySourceUnitNumber_Type=Integer32
_RlCopyHistorySourceUnitNumber_Object=MibTableColumn
rlCopyHistorySourceUnitNumber=_RlCopyHistorySourceUnitNumber_Object((1,3,6,1,4,1,4526,17,87,4,1,5),_RlCopyHistorySourceUnitNumber_Type())
rlCopyHistorySourceUnitNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCopyHistorySourceUnitNumber.setStatus(_A)
_RlCopyHistorySourceFileName_Type=DisplayString
_RlCopyHistorySourceFileName_Object=MibTableColumn
rlCopyHistorySourceFileName=_RlCopyHistorySourceFileName_Object((1,3,6,1,4,1,4526,17,87,4,1,6),_RlCopyHistorySourceFileName_Type())
rlCopyHistorySourceFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCopyHistorySourceFileName.setStatus(_A)
_RlCopyHistorySourceFileType_Type=RlCopyFileType
_RlCopyHistorySourceFileType_Object=MibTableColumn
rlCopyHistorySourceFileType=_RlCopyHistorySourceFileType_Object((1,3,6,1,4,1,4526,17,87,4,1,7),_RlCopyHistorySourceFileType_Type())
rlCopyHistorySourceFileType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCopyHistorySourceFileType.setStatus(_A)
_RlCopyHistoryDestinationLocation_Type=RlCopyLocationType
_RlCopyHistoryDestinationLocation_Object=MibTableColumn
rlCopyHistoryDestinationLocation=_RlCopyHistoryDestinationLocation_Object((1,3,6,1,4,1,4526,17,87,4,1,8),_RlCopyHistoryDestinationLocation_Type())
rlCopyHistoryDestinationLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCopyHistoryDestinationLocation.setStatus(_A)
_RlCopyHistoryDestinationIpAddress_Type=IpAddress
_RlCopyHistoryDestinationIpAddress_Object=MibTableColumn
rlCopyHistoryDestinationIpAddress=_RlCopyHistoryDestinationIpAddress_Object((1,3,6,1,4,1,4526,17,87,4,1,9),_RlCopyHistoryDestinationIpAddress_Type())
rlCopyHistoryDestinationIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCopyHistoryDestinationIpAddress.setStatus(_A)
_RlCopyHistoryDestinationUnitNumber_Type=Integer32
_RlCopyHistoryDestinationUnitNumber_Object=MibTableColumn
rlCopyHistoryDestinationUnitNumber=_RlCopyHistoryDestinationUnitNumber_Object((1,3,6,1,4,1,4526,17,87,4,1,10),_RlCopyHistoryDestinationUnitNumber_Type())
rlCopyHistoryDestinationUnitNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCopyHistoryDestinationUnitNumber.setStatus(_A)
_RlCopyHistoryDestinationFileName_Type=DisplayString
_RlCopyHistoryDestinationFileName_Object=MibTableColumn
rlCopyHistoryDestinationFileName=_RlCopyHistoryDestinationFileName_Object((1,3,6,1,4,1,4526,17,87,4,1,11),_RlCopyHistoryDestinationFileName_Type())
rlCopyHistoryDestinationFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCopyHistoryDestinationFileName.setStatus(_A)
_RlCopyHistoryDestinationFileType_Type=RlCopyFileType
_RlCopyHistoryDestinationFileType_Object=MibTableColumn
rlCopyHistoryDestinationFileType=_RlCopyHistoryDestinationFileType_Object((1,3,6,1,4,1,4526,17,87,4,1,12),_RlCopyHistoryDestinationFileType_Type())
rlCopyHistoryDestinationFileType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCopyHistoryDestinationFileType.setStatus(_A)
_RlCopyHistoryUpTime_Type=TimeTicks
_RlCopyHistoryUpTime_Object=MibTableColumn
rlCopyHistoryUpTime=_RlCopyHistoryUpTime_Object((1,3,6,1,4,1,4526,17,87,4,1,13),_RlCopyHistoryUpTime_Type())
rlCopyHistoryUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:rlCopyHistoryUpTime.setStatus(_A)
class _RlCopyHistoryOperationState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_L,1),(_M,2),(_N,3),(_O,4),(_P,5)))
_RlCopyHistoryOperationState_Type.__name__=_D
_RlCopyHistoryOperationState_Object=MibTableColumn
rlCopyHistoryOperationState=_RlCopyHistoryOperationState_Object((1,3,6,1,4,1,4526,17,87,4,1,14),_RlCopyHistoryOperationState_Type())
rlCopyHistoryOperationState.setMaxAccess(_C)
if mibBuilder.loadTexts:rlCopyHistoryOperationState.setStatus(_A)
_RlCopyHistoryBytesTransferred_Type=Integer32
_RlCopyHistoryBytesTransferred_Object=MibTableColumn
rlCopyHistoryBytesTransferred=_RlCopyHistoryBytesTransferred_Object((1,3,6,1,4,1,4526,17,87,4,1,15),_RlCopyHistoryBytesTransferred_Type())
rlCopyHistoryBytesTransferred.setMaxAccess(_C)
if mibBuilder.loadTexts:rlCopyHistoryBytesTransferred.setStatus(_A)
class _RlCopyHistoryInBackground_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_RlCopyHistoryInBackground_Type.__name__=_D
_RlCopyHistoryInBackground_Object=MibTableColumn
rlCopyHistoryInBackground=_RlCopyHistoryInBackground_Object((1,3,6,1,4,1,4526,17,87,4,1,16),_RlCopyHistoryInBackground_Type())
rlCopyHistoryInBackground.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCopyHistoryInBackground.setStatus(_A)
_RlCopyHistoryRowStatus_Type=RowStatus
_RlCopyHistoryRowStatus_Object=MibTableColumn
rlCopyHistoryRowStatus=_RlCopyHistoryRowStatus_Object((1,3,6,1,4,1,4526,17,87,4,1,17),_RlCopyHistoryRowStatus_Type())
rlCopyHistoryRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCopyHistoryRowStatus.setStatus(_A)
_RlCopyHistoryErrorMessage_Type=DisplayString
_RlCopyHistoryErrorMessage_Object=MibTableColumn
rlCopyHistoryErrorMessage=_RlCopyHistoryErrorMessage_Object((1,3,6,1,4,1,4526,17,87,4,1,18),_RlCopyHistoryErrorMessage_Type())
rlCopyHistoryErrorMessage.setMaxAccess(_C)
if mibBuilder.loadTexts:rlCopyHistoryErrorMessage.setStatus(_A)
class _RlCopyAuditingEnable_Type(TruthValue):defaultValue=1
_RlCopyAuditingEnable_Type.__name__=_I
_RlCopyAuditingEnable_Object=MibScalar
rlCopyAuditingEnable=_RlCopyAuditingEnable_Object((1,3,6,1,4,1,4526,17,87,5),_RlCopyAuditingEnable_Type())
rlCopyAuditingEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCopyAuditingEnable.setStatus(_A)
_RlCopyMessagesTable_Object=MibTable
rlCopyMessagesTable=_RlCopyMessagesTable_Object((1,3,6,1,4,1,4526,17,87,6))
if mibBuilder.loadTexts:rlCopyMessagesTable.setStatus(_A)
_RlCopyMessagesEntry_Object=MibTableRow
rlCopyMessagesEntry=_RlCopyMessagesEntry_Object((1,3,6,1,4,1,4526,17,87,6,1))
rlCopyMessagesEntry.setIndexNames((0,_F,_W),(0,_F,_X))
if mibBuilder.loadTexts:rlCopyMessagesEntry.setStatus(_A)
class _RlCopyMessagesCopyIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RlCopyMessagesCopyIndex_Type.__name__=_D
_RlCopyMessagesCopyIndex_Object=MibTableColumn
rlCopyMessagesCopyIndex=_RlCopyMessagesCopyIndex_Object((1,3,6,1,4,1,4526,17,87,6,1,1),_RlCopyMessagesCopyIndex_Type())
rlCopyMessagesCopyIndex.setMaxAccess(_R)
if mibBuilder.loadTexts:rlCopyMessagesCopyIndex.setStatus(_A)
class _RlCopyMessagesMessageIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RlCopyMessagesMessageIndex_Type.__name__=_D
_RlCopyMessagesMessageIndex_Object=MibTableColumn
rlCopyMessagesMessageIndex=_RlCopyMessagesMessageIndex_Object((1,3,6,1,4,1,4526,17,87,6,1,2),_RlCopyMessagesMessageIndex_Type())
rlCopyMessagesMessageIndex.setMaxAccess(_R)
if mibBuilder.loadTexts:rlCopyMessagesMessageIndex.setStatus(_A)
class _RlCopyMessagesMessageText_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_RlCopyMessagesMessageText_Type.__name__=_Q
_RlCopyMessagesMessageText_Object=MibTableColumn
rlCopyMessagesMessageText=_RlCopyMessagesMessageText_Object((1,3,6,1,4,1,4526,17,87,6,1,3),_RlCopyMessagesMessageText_Type())
rlCopyMessagesMessageText.setMaxAccess(_C)
if mibBuilder.loadTexts:rlCopyMessagesMessageText.setStatus(_A)
_RlCopyMessagesStatus_Type=RowStatus
_RlCopyMessagesStatus_Object=MibTableColumn
rlCopyMessagesStatus=_RlCopyMessagesStatus_Object((1,3,6,1,4,1,4526,17,87,6,1,4),_RlCopyMessagesStatus_Type())
rlCopyMessagesStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCopyMessagesStatus.setStatus(_A)
_RlCopyMessagesTableRemoveEntries_Type=Integer32
_RlCopyMessagesTableRemoveEntries_Object=MibScalar
rlCopyMessagesTableRemoveEntries=_RlCopyMessagesTableRemoveEntries_Object((1,3,6,1,4,1,4526,17,87,7),_RlCopyMessagesTableRemoveEntries_Type())
rlCopyMessagesTableRemoveEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCopyMessagesTableRemoveEntries.setStatus(_A)
_RlCopyInetTable_Object=MibTable
rlCopyInetTable=_RlCopyInetTable_Object((1,3,6,1,4,1,4526,17,87,8))
if mibBuilder.loadTexts:rlCopyInetTable.setStatus(_A)
_RlCopyInetEntry_Object=MibTableRow
rlCopyInetEntry=_RlCopyInetEntry_Object((1,3,6,1,4,1,4526,17,87,8,1))
rlCopyInetEntry.setIndexNames((0,_F,_Y))
if mibBuilder.loadTexts:rlCopyInetEntry.setStatus(_A)
_RlCopyInetIndex_Type=Integer32
_RlCopyInetIndex_Object=MibTableColumn
rlCopyInetIndex=_RlCopyInetIndex_Object((1,3,6,1,4,1,4526,17,87,8,1,1),_RlCopyInetIndex_Type())
rlCopyInetIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rlCopyInetIndex.setStatus(_A)
_RlCopyInetApplicationId_Type=RlCopyApplicationType
_RlCopyInetApplicationId_Object=MibTableColumn
rlCopyInetApplicationId=_RlCopyInetApplicationId_Object((1,3,6,1,4,1,4526,17,87,8,1,2),_RlCopyInetApplicationId_Type())
rlCopyInetApplicationId.setMaxAccess(_C)
if mibBuilder.loadTexts:rlCopyInetApplicationId.setStatus(_A)
_RlCopyInetSourceLocation_Type=RlCopyLocationType
_RlCopyInetSourceLocation_Object=MibTableColumn
rlCopyInetSourceLocation=_RlCopyInetSourceLocation_Object((1,3,6,1,4,1,4526,17,87,8,1,3),_RlCopyInetSourceLocation_Type())
rlCopyInetSourceLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCopyInetSourceLocation.setStatus(_A)
_RlCopyInetSourceIpAddressType_Type=InetAddressType
_RlCopyInetSourceIpAddressType_Object=MibTableColumn
rlCopyInetSourceIpAddressType=_RlCopyInetSourceIpAddressType_Object((1,3,6,1,4,1,4526,17,87,8,1,4),_RlCopyInetSourceIpAddressType_Type())
rlCopyInetSourceIpAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCopyInetSourceIpAddressType.setStatus(_A)
_RlCopyInetSourceIpAddress_Type=InetAddress
_RlCopyInetSourceIpAddress_Object=MibTableColumn
rlCopyInetSourceIpAddress=_RlCopyInetSourceIpAddress_Object((1,3,6,1,4,1,4526,17,87,8,1,5),_RlCopyInetSourceIpAddress_Type())
rlCopyInetSourceIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCopyInetSourceIpAddress.setStatus(_A)
_RlCopyInetSourceUnitNumber_Type=Integer32
_RlCopyInetSourceUnitNumber_Object=MibTableColumn
rlCopyInetSourceUnitNumber=_RlCopyInetSourceUnitNumber_Object((1,3,6,1,4,1,4526,17,87,8,1,6),_RlCopyInetSourceUnitNumber_Type())
rlCopyInetSourceUnitNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCopyInetSourceUnitNumber.setStatus(_A)
_RlCopyInetSourceFileName_Type=DisplayString
_RlCopyInetSourceFileName_Object=MibTableColumn
rlCopyInetSourceFileName=_RlCopyInetSourceFileName_Object((1,3,6,1,4,1,4526,17,87,8,1,7),_RlCopyInetSourceFileName_Type())
rlCopyInetSourceFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCopyInetSourceFileName.setStatus(_A)
_RlCopyInetSourceFileType_Type=RlCopyFileType
_RlCopyInetSourceFileType_Object=MibTableColumn
rlCopyInetSourceFileType=_RlCopyInetSourceFileType_Object((1,3,6,1,4,1,4526,17,87,8,1,8),_RlCopyInetSourceFileType_Type())
rlCopyInetSourceFileType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCopyInetSourceFileType.setStatus(_A)
_RlCopyInetDestinationLocation_Type=RlCopyLocationType
_RlCopyInetDestinationLocation_Object=MibTableColumn
rlCopyInetDestinationLocation=_RlCopyInetDestinationLocation_Object((1,3,6,1,4,1,4526,17,87,8,1,9),_RlCopyInetDestinationLocation_Type())
rlCopyInetDestinationLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCopyInetDestinationLocation.setStatus(_A)
_RlCopyInetDestinationIpAddressType_Type=InetAddressType
_RlCopyInetDestinationIpAddressType_Object=MibTableColumn
rlCopyInetDestinationIpAddressType=_RlCopyInetDestinationIpAddressType_Object((1,3,6,1,4,1,4526,17,87,8,1,10),_RlCopyInetDestinationIpAddressType_Type())
rlCopyInetDestinationIpAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCopyInetDestinationIpAddressType.setStatus(_A)
_RlCopyInetDestinationIpAddress_Type=InetAddress
_RlCopyInetDestinationIpAddress_Object=MibTableColumn
rlCopyInetDestinationIpAddress=_RlCopyInetDestinationIpAddress_Object((1,3,6,1,4,1,4526,17,87,8,1,11),_RlCopyInetDestinationIpAddress_Type())
rlCopyInetDestinationIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCopyInetDestinationIpAddress.setStatus(_A)
_RlCopyInetDestinationUnitNumber_Type=Integer32
_RlCopyInetDestinationUnitNumber_Object=MibTableColumn
rlCopyInetDestinationUnitNumber=_RlCopyInetDestinationUnitNumber_Object((1,3,6,1,4,1,4526,17,87,8,1,12),_RlCopyInetDestinationUnitNumber_Type())
rlCopyInetDestinationUnitNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCopyInetDestinationUnitNumber.setStatus(_A)
_RlCopyInetDestinationFileName_Type=DisplayString
_RlCopyInetDestinationFileName_Object=MibTableColumn
rlCopyInetDestinationFileName=_RlCopyInetDestinationFileName_Object((1,3,6,1,4,1,4526,17,87,8,1,13),_RlCopyInetDestinationFileName_Type())
rlCopyInetDestinationFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCopyInetDestinationFileName.setStatus(_A)
_RlCopyInetDestinationFileType_Type=RlCopyFileType
_RlCopyInetDestinationFileType_Object=MibTableColumn
rlCopyInetDestinationFileType=_RlCopyInetDestinationFileType_Object((1,3,6,1,4,1,4526,17,87,8,1,14),_RlCopyInetDestinationFileType_Type())
rlCopyInetDestinationFileType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCopyInetDestinationFileType.setStatus(_A)
_RlCopyInetUpTime_Type=TimeTicks
_RlCopyInetUpTime_Object=MibTableColumn
rlCopyInetUpTime=_RlCopyInetUpTime_Object((1,3,6,1,4,1,4526,17,87,8,1,15),_RlCopyInetUpTime_Type())
rlCopyInetUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:rlCopyInetUpTime.setStatus(_A)
class _RlCopyInetOperationState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_L,1),(_M,2),(_N,3),(_O,4),(_P,5)))
_RlCopyInetOperationState_Type.__name__=_D
_RlCopyInetOperationState_Object=MibTableColumn
rlCopyInetOperationState=_RlCopyInetOperationState_Object((1,3,6,1,4,1,4526,17,87,8,1,16),_RlCopyInetOperationState_Type())
rlCopyInetOperationState.setMaxAccess(_C)
if mibBuilder.loadTexts:rlCopyInetOperationState.setStatus(_A)
_RlCopyInetBytesTransferred_Type=Integer32
_RlCopyInetBytesTransferred_Object=MibTableColumn
rlCopyInetBytesTransferred=_RlCopyInetBytesTransferred_Object((1,3,6,1,4,1,4526,17,87,8,1,17),_RlCopyInetBytesTransferred_Type())
rlCopyInetBytesTransferred.setMaxAccess(_C)
if mibBuilder.loadTexts:rlCopyInetBytesTransferred.setStatus(_A)
class _RlCopyInetInBackground_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_RlCopyInetInBackground_Type.__name__=_D
_RlCopyInetInBackground_Object=MibTableColumn
rlCopyInetInBackground=_RlCopyInetInBackground_Object((1,3,6,1,4,1,4526,17,87,8,1,18),_RlCopyInetInBackground_Type())
rlCopyInetInBackground.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCopyInetInBackground.setStatus(_A)
_RlCopyInetRowStatus_Type=RowStatus
_RlCopyInetRowStatus_Object=MibTableColumn
rlCopyInetRowStatus=_RlCopyInetRowStatus_Object((1,3,6,1,4,1,4526,17,87,8,1,19),_RlCopyInetRowStatus_Type())
rlCopyInetRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCopyInetRowStatus.setStatus(_A)
class _RlCopyInetHistoryIndex_Type(Integer32):defaultValue=0
_RlCopyInetHistoryIndex_Type.__name__=_D
_RlCopyInetHistoryIndex_Object=MibTableColumn
rlCopyInetHistoryIndex=_RlCopyInetHistoryIndex_Object((1,3,6,1,4,1,4526,17,87,8,1,20),_RlCopyInetHistoryIndex_Type())
rlCopyInetHistoryIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCopyInetHistoryIndex.setStatus(_A)
class _RlCopyInetDestinationUnitList_Type(Integer32):defaultValue=0
_RlCopyInetDestinationUnitList_Type.__name__=_D
_RlCopyInetDestinationUnitList_Object=MibTableColumn
rlCopyInetDestinationUnitList=_RlCopyInetDestinationUnitList_Object((1,3,6,1,4,1,4526,17,87,8,1,21),_RlCopyInetDestinationUnitList_Type())
rlCopyInetDestinationUnitList.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCopyInetDestinationUnitList.setStatus(_A)
_RlCopyInetUnitStatusList_Type=Integer32
_RlCopyInetUnitStatusList_Object=MibTableColumn
rlCopyInetUnitStatusList=_RlCopyInetUnitStatusList_Object((1,3,6,1,4,1,4526,17,87,8,1,22),_RlCopyInetUnitStatusList_Type())
rlCopyInetUnitStatusList.setMaxAccess(_C)
if mibBuilder.loadTexts:rlCopyInetUnitStatusList.setStatus(_A)
class _RlCopyInetSpecificCopyInfo_Type(DisplayString):defaultValue=OctetString('')
_RlCopyInetSpecificCopyInfo_Type.__name__=_Q
_RlCopyInetSpecificCopyInfo_Object=MibTableColumn
rlCopyInetSpecificCopyInfo=_RlCopyInetSpecificCopyInfo_Object((1,3,6,1,4,1,4526,17,87,8,1,23),_RlCopyInetSpecificCopyInfo_Type())
rlCopyInetSpecificCopyInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCopyInetSpecificCopyInfo.setStatus(_A)
_RlCopyHistoryInetTable_Object=MibTable
rlCopyHistoryInetTable=_RlCopyHistoryInetTable_Object((1,3,6,1,4,1,4526,17,87,9))
if mibBuilder.loadTexts:rlCopyHistoryInetTable.setStatus(_A)
_RlCopyHistoryInetEntry_Object=MibTableRow
rlCopyHistoryInetEntry=_RlCopyHistoryInetEntry_Object((1,3,6,1,4,1,4526,17,87,9,1))
rlCopyHistoryInetEntry.setIndexNames((0,_F,_Z))
if mibBuilder.loadTexts:rlCopyHistoryInetEntry.setStatus(_A)
_RlCopyHistoryInetHistoryIndex_Type=Integer32
_RlCopyHistoryInetHistoryIndex_Object=MibTableColumn
rlCopyHistoryInetHistoryIndex=_RlCopyHistoryInetHistoryIndex_Object((1,3,6,1,4,1,4526,17,87,9,1,1),_RlCopyHistoryInetHistoryIndex_Type())
rlCopyHistoryInetHistoryIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rlCopyHistoryInetHistoryIndex.setStatus(_A)
_RlCopyHistoryInetApplicationId_Type=RlCopyApplicationType
_RlCopyHistoryInetApplicationId_Object=MibTableColumn
rlCopyHistoryInetApplicationId=_RlCopyHistoryInetApplicationId_Object((1,3,6,1,4,1,4526,17,87,9,1,2),_RlCopyHistoryInetApplicationId_Type())
rlCopyHistoryInetApplicationId.setMaxAccess(_C)
if mibBuilder.loadTexts:rlCopyHistoryInetApplicationId.setStatus(_A)
_RlCopyHistoryInetSourceLocation_Type=RlCopyLocationType
_RlCopyHistoryInetSourceLocation_Object=MibTableColumn
rlCopyHistoryInetSourceLocation=_RlCopyHistoryInetSourceLocation_Object((1,3,6,1,4,1,4526,17,87,9,1,3),_RlCopyHistoryInetSourceLocation_Type())
rlCopyHistoryInetSourceLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCopyHistoryInetSourceLocation.setStatus(_A)
_RlCopyHistoryInetSourceIpAddressType_Type=InetAddressType
_RlCopyHistoryInetSourceIpAddressType_Object=MibTableColumn
rlCopyHistoryInetSourceIpAddressType=_RlCopyHistoryInetSourceIpAddressType_Object((1,3,6,1,4,1,4526,17,87,9,1,4),_RlCopyHistoryInetSourceIpAddressType_Type())
rlCopyHistoryInetSourceIpAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCopyHistoryInetSourceIpAddressType.setStatus(_A)
_RlCopyHistoryInetSourceIpAddress_Type=InetAddress
_RlCopyHistoryInetSourceIpAddress_Object=MibTableColumn
rlCopyHistoryInetSourceIpAddress=_RlCopyHistoryInetSourceIpAddress_Object((1,3,6,1,4,1,4526,17,87,9,1,5),_RlCopyHistoryInetSourceIpAddress_Type())
rlCopyHistoryInetSourceIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCopyHistoryInetSourceIpAddress.setStatus(_A)
_RlCopyHistoryInetSourceUnitNumber_Type=Integer32
_RlCopyHistoryInetSourceUnitNumber_Object=MibTableColumn
rlCopyHistoryInetSourceUnitNumber=_RlCopyHistoryInetSourceUnitNumber_Object((1,3,6,1,4,1,4526,17,87,9,1,6),_RlCopyHistoryInetSourceUnitNumber_Type())
rlCopyHistoryInetSourceUnitNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCopyHistoryInetSourceUnitNumber.setStatus(_A)
_RlCopyHistoryInetSourceFileName_Type=DisplayString
_RlCopyHistoryInetSourceFileName_Object=MibTableColumn
rlCopyHistoryInetSourceFileName=_RlCopyHistoryInetSourceFileName_Object((1,3,6,1,4,1,4526,17,87,9,1,7),_RlCopyHistoryInetSourceFileName_Type())
rlCopyHistoryInetSourceFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCopyHistoryInetSourceFileName.setStatus(_A)
_RlCopyHistoryInetSourceFileType_Type=RlCopyFileType
_RlCopyHistoryInetSourceFileType_Object=MibTableColumn
rlCopyHistoryInetSourceFileType=_RlCopyHistoryInetSourceFileType_Object((1,3,6,1,4,1,4526,17,87,9,1,8),_RlCopyHistoryInetSourceFileType_Type())
rlCopyHistoryInetSourceFileType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCopyHistoryInetSourceFileType.setStatus(_A)
_RlCopyHistoryInetDestinationLocation_Type=RlCopyLocationType
_RlCopyHistoryInetDestinationLocation_Object=MibTableColumn
rlCopyHistoryInetDestinationLocation=_RlCopyHistoryInetDestinationLocation_Object((1,3,6,1,4,1,4526,17,87,9,1,9),_RlCopyHistoryInetDestinationLocation_Type())
rlCopyHistoryInetDestinationLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCopyHistoryInetDestinationLocation.setStatus(_A)
_RlCopyHistoryInetDestinationIpAddressType_Type=InetAddressType
_RlCopyHistoryInetDestinationIpAddressType_Object=MibTableColumn
rlCopyHistoryInetDestinationIpAddressType=_RlCopyHistoryInetDestinationIpAddressType_Object((1,3,6,1,4,1,4526,17,87,9,1,10),_RlCopyHistoryInetDestinationIpAddressType_Type())
rlCopyHistoryInetDestinationIpAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCopyHistoryInetDestinationIpAddressType.setStatus(_A)
_RlCopyHistoryInetDestinationIpAddress_Type=InetAddress
_RlCopyHistoryInetDestinationIpAddress_Object=MibTableColumn
rlCopyHistoryInetDestinationIpAddress=_RlCopyHistoryInetDestinationIpAddress_Object((1,3,6,1,4,1,4526,17,87,9,1,11),_RlCopyHistoryInetDestinationIpAddress_Type())
rlCopyHistoryInetDestinationIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCopyHistoryInetDestinationIpAddress.setStatus(_A)
_RlCopyHistoryInetDestinationUnitNumber_Type=Integer32
_RlCopyHistoryInetDestinationUnitNumber_Object=MibTableColumn
rlCopyHistoryInetDestinationUnitNumber=_RlCopyHistoryInetDestinationUnitNumber_Object((1,3,6,1,4,1,4526,17,87,9,1,12),_RlCopyHistoryInetDestinationUnitNumber_Type())
rlCopyHistoryInetDestinationUnitNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCopyHistoryInetDestinationUnitNumber.setStatus(_A)
_RlCopyHistoryInetDestinationFileName_Type=DisplayString
_RlCopyHistoryInetDestinationFileName_Object=MibTableColumn
rlCopyHistoryInetDestinationFileName=_RlCopyHistoryInetDestinationFileName_Object((1,3,6,1,4,1,4526,17,87,9,1,13),_RlCopyHistoryInetDestinationFileName_Type())
rlCopyHistoryInetDestinationFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCopyHistoryInetDestinationFileName.setStatus(_A)
_RlCopyHistoryInetDestinationFileType_Type=RlCopyFileType
_RlCopyHistoryInetDestinationFileType_Object=MibTableColumn
rlCopyHistoryInetDestinationFileType=_RlCopyHistoryInetDestinationFileType_Object((1,3,6,1,4,1,4526,17,87,9,1,14),_RlCopyHistoryInetDestinationFileType_Type())
rlCopyHistoryInetDestinationFileType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCopyHistoryInetDestinationFileType.setStatus(_A)
_RlCopyHistoryInetUpTime_Type=TimeTicks
_RlCopyHistoryInetUpTime_Object=MibTableColumn
rlCopyHistoryInetUpTime=_RlCopyHistoryInetUpTime_Object((1,3,6,1,4,1,4526,17,87,9,1,15),_RlCopyHistoryInetUpTime_Type())
rlCopyHistoryInetUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:rlCopyHistoryInetUpTime.setStatus(_A)
class _RlCopyHistoryInetOperationState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_L,1),(_M,2),(_N,3),(_O,4),(_P,5)))
_RlCopyHistoryInetOperationState_Type.__name__=_D
_RlCopyHistoryInetOperationState_Object=MibTableColumn
rlCopyHistoryInetOperationState=_RlCopyHistoryInetOperationState_Object((1,3,6,1,4,1,4526,17,87,9,1,16),_RlCopyHistoryInetOperationState_Type())
rlCopyHistoryInetOperationState.setMaxAccess(_C)
if mibBuilder.loadTexts:rlCopyHistoryInetOperationState.setStatus(_A)
_RlCopyHistoryInetBytesTransferred_Type=Integer32
_RlCopyHistoryInetBytesTransferred_Object=MibTableColumn
rlCopyHistoryInetBytesTransferred=_RlCopyHistoryInetBytesTransferred_Object((1,3,6,1,4,1,4526,17,87,9,1,17),_RlCopyHistoryInetBytesTransferred_Type())
rlCopyHistoryInetBytesTransferred.setMaxAccess(_C)
if mibBuilder.loadTexts:rlCopyHistoryInetBytesTransferred.setStatus(_A)
class _RlCopyHistoryInetInBackground_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_RlCopyHistoryInetInBackground_Type.__name__=_D
_RlCopyHistoryInetInBackground_Object=MibTableColumn
rlCopyHistoryInetInBackground=_RlCopyHistoryInetInBackground_Object((1,3,6,1,4,1,4526,17,87,9,1,18),_RlCopyHistoryInetInBackground_Type())
rlCopyHistoryInetInBackground.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCopyHistoryInetInBackground.setStatus(_A)
_RlCopyHistoryInetRowStatus_Type=RowStatus
_RlCopyHistoryInetRowStatus_Object=MibTableColumn
rlCopyHistoryInetRowStatus=_RlCopyHistoryInetRowStatus_Object((1,3,6,1,4,1,4526,17,87,9,1,19),_RlCopyHistoryInetRowStatus_Type())
rlCopyHistoryInetRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCopyHistoryInetRowStatus.setStatus(_A)
_RlCopyHistoryInetErrorMessage_Type=DisplayString
_RlCopyHistoryInetErrorMessage_Object=MibTableColumn
rlCopyHistoryInetErrorMessage=_RlCopyHistoryInetErrorMessage_Object((1,3,6,1,4,1,4526,17,87,9,1,20),_RlCopyHistoryInetErrorMessage_Type())
rlCopyHistoryInetErrorMessage.setMaxAccess(_C)
if mibBuilder.loadTexts:rlCopyHistoryInetErrorMessage.setStatus(_A)
class _RlCopyHistoryInetDestinationUnitList_Type(Integer32):defaultValue=0
_RlCopyHistoryInetDestinationUnitList_Type.__name__=_D
_RlCopyHistoryInetDestinationUnitList_Object=MibTableColumn
rlCopyHistoryInetDestinationUnitList=_RlCopyHistoryInetDestinationUnitList_Object((1,3,6,1,4,1,4526,17,87,9,1,21),_RlCopyHistoryInetDestinationUnitList_Type())
rlCopyHistoryInetDestinationUnitList.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCopyHistoryInetDestinationUnitList.setStatus(_A)
_RlCopyHistoryInetUnitStatusList_Type=Integer32
_RlCopyHistoryInetUnitStatusList_Object=MibTableColumn
rlCopyHistoryInetUnitStatusList=_RlCopyHistoryInetUnitStatusList_Object((1,3,6,1,4,1,4526,17,87,9,1,22),_RlCopyHistoryInetUnitStatusList_Type())
rlCopyHistoryInetUnitStatusList.setMaxAccess(_C)
if mibBuilder.loadTexts:rlCopyHistoryInetUnitStatusList.setStatus(_A)
_RlCopyHistoryInetTotalFileSize_Type=Integer32
_RlCopyHistoryInetTotalFileSize_Object=MibTableColumn
rlCopyHistoryInetTotalFileSize=_RlCopyHistoryInetTotalFileSize_Object((1,3,6,1,4,1,4526,17,87,9,1,23),_RlCopyHistoryInetTotalFileSize_Type())
rlCopyHistoryInetTotalFileSize.setMaxAccess(_C)
if mibBuilder.loadTexts:rlCopyHistoryInetTotalFileSize.setStatus(_A)
_RlCopyUnitsList_Type=Integer32
_RlCopyUnitsList_Object=MibScalar
rlCopyUnitsList=_RlCopyUnitsList_Object((1,3,6,1,4,1,4526,17,87,10),_RlCopyUnitsList_Type())
rlCopyUnitsList.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:rlCopyUnitsList.setStatus(_A)
_RlCopyMirrorTimeout_Type=Integer32
_RlCopyMirrorTimeout_Object=MibScalar
rlCopyMirrorTimeout=_RlCopyMirrorTimeout_Object((1,3,6,1,4,1,4526,17,87,11),_RlCopyMirrorTimeout_Type())
rlCopyMirrorTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCopyMirrorTimeout.setStatus(_A)
_RlCopyOptionsTable_Object=MibTable
rlCopyOptionsTable=_RlCopyOptionsTable_Object((1,3,6,1,4,1,4526,17,87,12))
if mibBuilder.loadTexts:rlCopyOptionsTable.setStatus(_A)
_RlCopyOptionsEntry_Object=MibTableRow
rlCopyOptionsEntry=_RlCopyOptionsEntry_Object((1,3,6,1,4,1,4526,17,87,12,1))
rlCopyOptionsEntry.setIndexNames((0,_F,_a))
if mibBuilder.loadTexts:rlCopyOptionsEntry.setStatus(_A)
_RlCopyOptionsIndex_Type=Unsigned32
_RlCopyOptionsIndex_Object=MibTableColumn
rlCopyOptionsIndex=_RlCopyOptionsIndex_Object((1,3,6,1,4,1,4526,17,87,12,1,1),_RlCopyOptionsIndex_Type())
rlCopyOptionsIndex.setMaxAccess(_R)
if mibBuilder.loadTexts:rlCopyOptionsIndex.setStatus(_A)
class _RlCopyOptionsRequestedSsdAccess_Type(RlCopySecSdAccessType):defaultValue=4
_RlCopyOptionsRequestedSsdAccess_Type.__name__=_b
_RlCopyOptionsRequestedSsdAccess_Object=MibTableColumn
rlCopyOptionsRequestedSsdAccess=_RlCopyOptionsRequestedSsdAccess_Object((1,3,6,1,4,1,4526,17,87,12,1,2),_RlCopyOptionsRequestedSsdAccess_Type())
rlCopyOptionsRequestedSsdAccess.setMaxAccess(_S)
if mibBuilder.loadTexts:rlCopyOptionsRequestedSsdAccess.setStatus(_A)
class _RlCopyOptionsCheckFilePermission_Type(TruthValue):defaultValue=1
_RlCopyOptionsCheckFilePermission_Type.__name__=_I
_RlCopyOptionsCheckFilePermission_Object=MibTableColumn
rlCopyOptionsCheckFilePermission=_RlCopyOptionsCheckFilePermission_Object((1,3,6,1,4,1,4526,17,87,12,1,3),_RlCopyOptionsCheckFilePermission_Type())
rlCopyOptionsCheckFilePermission.setMaxAccess(_S)
if mibBuilder.loadTexts:rlCopyOptionsCheckFilePermission.setStatus(_A)
class _RlCopyOptionsCheckSystemReservedStorage_Type(TruthValue):defaultValue=1
_RlCopyOptionsCheckSystemReservedStorage_Type.__name__=_I
_RlCopyOptionsCheckSystemReservedStorage_Object=MibTableColumn
rlCopyOptionsCheckSystemReservedStorage=_RlCopyOptionsCheckSystemReservedStorage_Object((1,3,6,1,4,1,4526,17,87,12,1,4),_RlCopyOptionsCheckSystemReservedStorage_Type())
rlCopyOptionsCheckSystemReservedStorage.setMaxAccess(_S)
if mibBuilder.loadTexts:rlCopyOptionsCheckSystemReservedStorage.setStatus(_A)
_RlCopyMirror_ObjectIdentity=ObjectIdentity
rlCopyMirror=_RlCopyMirror_ObjectIdentity((1,3,6,1,4,1,4526,17,87,13))
class _RlCopyMirrorEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_RlCopyMirrorEnable_Type.__name__=_D
_RlCopyMirrorEnable_Object=MibScalar
rlCopyMirrorEnable=_RlCopyMirrorEnable_Object((1,3,6,1,4,1,4526,17,87,13,1),_RlCopyMirrorEnable_Type())
rlCopyMirrorEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCopyMirrorEnable.setStatus(_A)
class _RlCopyStaticDowngradeStatus_Type(TruthValue):defaultValue=2
_RlCopyStaticDowngradeStatus_Type.__name__=_I
_RlCopyStaticDowngradeStatus_Object=MibScalar
rlCopyStaticDowngradeStatus=_RlCopyStaticDowngradeStatus_Object((1,3,6,1,4,1,4526,17,87,14),_RlCopyStaticDowngradeStatus_Type())
rlCopyStaticDowngradeStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rlCopyStaticDowngradeStatus.setStatus(_A)
rlCopyFinished=NotificationType((1,3,6,1,4,1,4526,17,0,180))
rlCopyFinished.setObjects(*((_E,_G),(_E,_H)))
if mibBuilder.loadTexts:rlCopyFinished.setStatus(_A)
rlCopyFailed=NotificationType((1,3,6,1,4,1,4526,17,0,181))
rlCopyFailed.setObjects(*((_E,_G),(_E,_H)))
if mibBuilder.loadTexts:rlCopyFailed.setStatus(_A)
rlCopySWFinished=NotificationType((1,3,6,1,4,1,4526,17,0,211))
rlCopySWFinished.setObjects(*((_E,_G),(_E,_H)))
if mibBuilder.loadTexts:rlCopySWFinished.setStatus(_A)
rlCopySWToUnits=NotificationType((1,3,6,1,4,1,4526,17,0,212))
rlCopySWToUnits.setObjects(*((_E,_G),(_E,_H),(_F,_c)))
if mibBuilder.loadTexts:rlCopySWToUnits.setStatus(_A)
rlCopyMirrorFileIllegal=NotificationType((1,3,6,1,4,1,4526,17,0,220))
rlCopyMirrorFileIllegal.setObjects(*((_E,_G),(_E,_H)))
if mibBuilder.loadTexts:rlCopyMirrorFileIllegal.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'RlCopyApplicationType':RlCopyApplicationType,'RlCopyLocationType':RlCopyLocationType,'RlCopyFileType':RlCopyFileType,_b:RlCopySecSdAccessType,'rlCopyFinished':rlCopyFinished,'rlCopyFailed':rlCopyFailed,'rlCopySWFinished':rlCopySWFinished,'rlCopySWToUnits':rlCopySWToUnits,'rlCopyMirrorFileIllegal':rlCopyMirrorFileIllegal,'rlCopy':rlCopy,'rlCopyMibVersion':rlCopyMibVersion,'rlCopyTable':rlCopyTable,'rlCopyEntry':rlCopyEntry,_U:rlCopyIndex,'rlCopyApplicationId':rlCopyApplicationId,'rlCopySourceLocation':rlCopySourceLocation,'rlCopySourceIpAddress':rlCopySourceIpAddress,'rlCopySourceUnitNumber':rlCopySourceUnitNumber,'rlCopySourceFileName':rlCopySourceFileName,'rlCopySourceFileType':rlCopySourceFileType,'rlCopyDestinationLocation':rlCopyDestinationLocation,'rlCopyDestinationIpAddress':rlCopyDestinationIpAddress,'rlCopyDestinationUnitNumber':rlCopyDestinationUnitNumber,'rlCopyDestinationFileName':rlCopyDestinationFileName,'rlCopyDestinationFileType':rlCopyDestinationFileType,'rlCopyUpTime':rlCopyUpTime,'rlCopyOperationState':rlCopyOperationState,'rlCopyBytesTransferred':rlCopyBytesTransferred,'rlCopyInBackground':rlCopyInBackground,'rlCopyRowStatus':rlCopyRowStatus,'rlCopyHistoryIndex':rlCopyHistoryIndex,'rlCopyFreeHistoryIndex':rlCopyFreeHistoryIndex,'rlCopyHistoryTable':rlCopyHistoryTable,'rlCopyHistoryEntry':rlCopyHistoryEntry,_V:rlCopyHistoryHistoryIndex,'rlCopyHistoryApplicationId':rlCopyHistoryApplicationId,'rlCopyHistorySourceLocation':rlCopyHistorySourceLocation,'rlCopyHistorySourceIpAddress':rlCopyHistorySourceIpAddress,'rlCopyHistorySourceUnitNumber':rlCopyHistorySourceUnitNumber,'rlCopyHistorySourceFileName':rlCopyHistorySourceFileName,'rlCopyHistorySourceFileType':rlCopyHistorySourceFileType,'rlCopyHistoryDestinationLocation':rlCopyHistoryDestinationLocation,'rlCopyHistoryDestinationIpAddress':rlCopyHistoryDestinationIpAddress,'rlCopyHistoryDestinationUnitNumber':rlCopyHistoryDestinationUnitNumber,'rlCopyHistoryDestinationFileName':rlCopyHistoryDestinationFileName,'rlCopyHistoryDestinationFileType':rlCopyHistoryDestinationFileType,'rlCopyHistoryUpTime':rlCopyHistoryUpTime,'rlCopyHistoryOperationState':rlCopyHistoryOperationState,'rlCopyHistoryBytesTransferred':rlCopyHistoryBytesTransferred,'rlCopyHistoryInBackground':rlCopyHistoryInBackground,'rlCopyHistoryRowStatus':rlCopyHistoryRowStatus,'rlCopyHistoryErrorMessage':rlCopyHistoryErrorMessage,'rlCopyAuditingEnable':rlCopyAuditingEnable,'rlCopyMessagesTable':rlCopyMessagesTable,'rlCopyMessagesEntry':rlCopyMessagesEntry,_W:rlCopyMessagesCopyIndex,_X:rlCopyMessagesMessageIndex,'rlCopyMessagesMessageText':rlCopyMessagesMessageText,'rlCopyMessagesStatus':rlCopyMessagesStatus,'rlCopyMessagesTableRemoveEntries':rlCopyMessagesTableRemoveEntries,'rlCopyInetTable':rlCopyInetTable,'rlCopyInetEntry':rlCopyInetEntry,_Y:rlCopyInetIndex,'rlCopyInetApplicationId':rlCopyInetApplicationId,'rlCopyInetSourceLocation':rlCopyInetSourceLocation,'rlCopyInetSourceIpAddressType':rlCopyInetSourceIpAddressType,'rlCopyInetSourceIpAddress':rlCopyInetSourceIpAddress,'rlCopyInetSourceUnitNumber':rlCopyInetSourceUnitNumber,'rlCopyInetSourceFileName':rlCopyInetSourceFileName,'rlCopyInetSourceFileType':rlCopyInetSourceFileType,'rlCopyInetDestinationLocation':rlCopyInetDestinationLocation,'rlCopyInetDestinationIpAddressType':rlCopyInetDestinationIpAddressType,'rlCopyInetDestinationIpAddress':rlCopyInetDestinationIpAddress,'rlCopyInetDestinationUnitNumber':rlCopyInetDestinationUnitNumber,'rlCopyInetDestinationFileName':rlCopyInetDestinationFileName,'rlCopyInetDestinationFileType':rlCopyInetDestinationFileType,'rlCopyInetUpTime':rlCopyInetUpTime,'rlCopyInetOperationState':rlCopyInetOperationState,'rlCopyInetBytesTransferred':rlCopyInetBytesTransferred,'rlCopyInetInBackground':rlCopyInetInBackground,'rlCopyInetRowStatus':rlCopyInetRowStatus,'rlCopyInetHistoryIndex':rlCopyInetHistoryIndex,'rlCopyInetDestinationUnitList':rlCopyInetDestinationUnitList,'rlCopyInetUnitStatusList':rlCopyInetUnitStatusList,'rlCopyInetSpecificCopyInfo':rlCopyInetSpecificCopyInfo,'rlCopyHistoryInetTable':rlCopyHistoryInetTable,'rlCopyHistoryInetEntry':rlCopyHistoryInetEntry,_Z:rlCopyHistoryInetHistoryIndex,'rlCopyHistoryInetApplicationId':rlCopyHistoryInetApplicationId,'rlCopyHistoryInetSourceLocation':rlCopyHistoryInetSourceLocation,'rlCopyHistoryInetSourceIpAddressType':rlCopyHistoryInetSourceIpAddressType,'rlCopyHistoryInetSourceIpAddress':rlCopyHistoryInetSourceIpAddress,'rlCopyHistoryInetSourceUnitNumber':rlCopyHistoryInetSourceUnitNumber,'rlCopyHistoryInetSourceFileName':rlCopyHistoryInetSourceFileName,'rlCopyHistoryInetSourceFileType':rlCopyHistoryInetSourceFileType,'rlCopyHistoryInetDestinationLocation':rlCopyHistoryInetDestinationLocation,'rlCopyHistoryInetDestinationIpAddressType':rlCopyHistoryInetDestinationIpAddressType,'rlCopyHistoryInetDestinationIpAddress':rlCopyHistoryInetDestinationIpAddress,'rlCopyHistoryInetDestinationUnitNumber':rlCopyHistoryInetDestinationUnitNumber,'rlCopyHistoryInetDestinationFileName':rlCopyHistoryInetDestinationFileName,'rlCopyHistoryInetDestinationFileType':rlCopyHistoryInetDestinationFileType,'rlCopyHistoryInetUpTime':rlCopyHistoryInetUpTime,'rlCopyHistoryInetOperationState':rlCopyHistoryInetOperationState,'rlCopyHistoryInetBytesTransferred':rlCopyHistoryInetBytesTransferred,'rlCopyHistoryInetInBackground':rlCopyHistoryInetInBackground,'rlCopyHistoryInetRowStatus':rlCopyHistoryInetRowStatus,'rlCopyHistoryInetErrorMessage':rlCopyHistoryInetErrorMessage,'rlCopyHistoryInetDestinationUnitList':rlCopyHistoryInetDestinationUnitList,'rlCopyHistoryInetUnitStatusList':rlCopyHistoryInetUnitStatusList,'rlCopyHistoryInetTotalFileSize':rlCopyHistoryInetTotalFileSize,_c:rlCopyUnitsList,'rlCopyMirrorTimeout':rlCopyMirrorTimeout,'rlCopyOptionsTable':rlCopyOptionsTable,'rlCopyOptionsEntry':rlCopyOptionsEntry,_a:rlCopyOptionsIndex,'rlCopyOptionsRequestedSsdAccess':rlCopyOptionsRequestedSsdAccess,'rlCopyOptionsCheckFilePermission':rlCopyOptionsCheckFilePermission,'rlCopyOptionsCheckSystemReservedStorage':rlCopyOptionsCheckSystemReservedStorage,'rlCopyMirror':rlCopyMirror,'rlCopyMirrorEnable':rlCopyMirrorEnable,'rlCopyStaticDowngradeStatus':rlCopyStaticDowngradeStatus})