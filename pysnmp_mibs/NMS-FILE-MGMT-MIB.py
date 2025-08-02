_J='fileName'
_I='filePath'
_H='noOperation'
_G='fileTransferIndex'
_F='not-accessible'
_E='read-only'
_D='NMS-FILE-MGMT-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
nmsMgmt,=mibBuilder.importSymbols('NMS-SMI','nmsMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
nmsFileMgmtMIB=ModuleIdentity((1,3,6,1,4,1,3320,9,185))
_FileTransferManagement_ObjectIdentity=ObjectIdentity
fileTransferManagement=_FileTransferManagement_ObjectIdentity((1,3,6,1,4,1,3320,9,185,1))
if mibBuilder.loadTexts:fileTransferManagement.setStatus(_A)
_FileTransferTable_Object=MibTable
fileTransferTable=_FileTransferTable_Object((1,3,6,1,4,1,3320,9,185,1,1))
if mibBuilder.loadTexts:fileTransferTable.setStatus(_A)
_FileTransferEntry_Object=MibTableRow
fileTransferEntry=_FileTransferEntry_Object((1,3,6,1,4,1,3320,9,185,1,1,1))
fileTransferEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:fileTransferEntry.setStatus(_A)
class _FileTransferIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_FileTransferIndex_Type.__name__=_C
_FileTransferIndex_Object=MibTableColumn
fileTransferIndex=_FileTransferIndex_Object((1,3,6,1,4,1,3320,9,185,1,1,1,1),_FileTransferIndex_Type())
fileTransferIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fileTransferIndex.setStatus(_A)
class _FileTransferProtocolType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ftp',1),('tftp',2)))
_FileTransferProtocolType_Type.__name__=_C
_FileTransferProtocolType_Object=MibTableColumn
fileTransferProtocolType=_FileTransferProtocolType_Object((1,3,6,1,4,1,3320,9,185,1,1,1,2),_FileTransferProtocolType_Type())
fileTransferProtocolType.setMaxAccess(_B)
if mibBuilder.loadTexts:fileTransferProtocolType.setStatus(_A)
_ServerIpAddress_Type=IpAddress
_ServerIpAddress_Object=MibTableColumn
serverIpAddress=_ServerIpAddress_Object((1,3,6,1,4,1,3320,9,185,1,1,1,3),_ServerIpAddress_Type())
serverIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:serverIpAddress.setStatus(_A)
_FtpUserName_Type=DisplayString
_FtpUserName_Object=MibTableColumn
ftpUserName=_FtpUserName_Object((1,3,6,1,4,1,3320,9,185,1,1,1,4),_FtpUserName_Type())
ftpUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:ftpUserName.setStatus(_A)
_FtpUserPassword_Type=DisplayString
_FtpUserPassword_Object=MibTableColumn
ftpUserPassword=_FtpUserPassword_Object((1,3,6,1,4,1,3320,9,185,1,1,1,5),_FtpUserPassword_Type())
ftpUserPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:ftpUserPassword.setStatus(_A)
_TransferFileSrcNamePath_Type=DisplayString
_TransferFileSrcNamePath_Object=MibTableColumn
transferFileSrcNamePath=_TransferFileSrcNamePath_Object((1,3,6,1,4,1,3320,9,185,1,1,1,6),_TransferFileSrcNamePath_Type())
transferFileSrcNamePath.setMaxAccess(_B)
if mibBuilder.loadTexts:transferFileSrcNamePath.setStatus(_A)
_TransferFileDstNamePath_Type=DisplayString
_TransferFileDstNamePath_Object=MibTableColumn
transferFileDstNamePath=_TransferFileDstNamePath_Object((1,3,6,1,4,1,3320,9,185,1,1,1,7),_TransferFileDstNamePath_Type())
transferFileDstNamePath.setMaxAccess(_B)
if mibBuilder.loadTexts:transferFileDstNamePath.setStatus(_A)
class _TransferAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),('put',2),('get',3),('halt',4)))
_TransferAction_Type.__name__=_C
_TransferAction_Object=MibTableColumn
transferAction=_TransferAction_Object((1,3,6,1,4,1,3320,9,185,1,1,1,8),_TransferAction_Type())
transferAction.setMaxAccess(_B)
if mibBuilder.loadTexts:transferAction.setStatus(_A)
class _TransferStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('idle',1),('inProgress',2),('success',3),('failure',4)))
_TransferStatus_Type.__name__=_C
_TransferStatus_Object=MibTableColumn
transferStatus=_TransferStatus_Object((1,3,6,1,4,1,3320,9,185,1,1,1,9),_TransferStatus_Type())
transferStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:transferStatus.setStatus(_A)
_FileInfoManagementTable_Object=MibTable
fileInfoManagementTable=_FileInfoManagementTable_Object((1,3,6,1,4,1,3320,9,185,1,2))
if mibBuilder.loadTexts:fileInfoManagementTable.setStatus(_A)
_FileInfoManagementEntry_Object=MibTableRow
fileInfoManagementEntry=_FileInfoManagementEntry_Object((1,3,6,1,4,1,3320,9,185,1,2,1))
fileInfoManagementEntry.setIndexNames((0,_D,_I),(0,_D,_J))
if mibBuilder.loadTexts:fileInfoManagementEntry.setStatus(_A)
_FilePath_Type=DisplayString
_FilePath_Object=MibTableColumn
filePath=_FilePath_Object((1,3,6,1,4,1,3320,9,185,1,2,1,1),_FilePath_Type())
filePath.setMaxAccess(_F)
if mibBuilder.loadTexts:filePath.setStatus(_A)
_FileName_Type=DisplayString
_FileName_Object=MibTableColumn
fileName=_FileName_Object((1,3,6,1,4,1,3320,9,185,1,2,1,2),_FileName_Type())
fileName.setMaxAccess(_F)
if mibBuilder.loadTexts:fileName.setStatus(_A)
_FileSize_Type=Counter32
_FileSize_Object=MibTableColumn
fileSize=_FileSize_Object((1,3,6,1,4,1,3320,9,185,1,2,1,3),_FileSize_Type())
fileSize.setMaxAccess(_E)
if mibBuilder.loadTexts:fileSize.setStatus(_A)
if mibBuilder.loadTexts:fileSize.setUnits('bytes')
_FileModifyTime_Type=DateAndTime
_FileModifyTime_Object=MibTableColumn
fileModifyTime=_FileModifyTime_Object((1,3,6,1,4,1,3320,9,185,1,2,1,4),_FileModifyTime_Type())
fileModifyTime.setMaxAccess(_E)
if mibBuilder.loadTexts:fileModifyTime.setStatus(_A)
class _FileManagementAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),('erase',2)))
_FileManagementAction_Type.__name__=_C
_FileManagementAction_Object=MibTableColumn
fileManagementAction=_FileManagementAction_Object((1,3,6,1,4,1,3320,9,185,1,2,1,5),_FileManagementAction_Type())
fileManagementAction.setMaxAccess(_B)
if mibBuilder.loadTexts:fileManagementAction.setStatus(_A)
class _FileAttribute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('file',1),('dir',2)))
_FileAttribute_Type.__name__=_C
_FileAttribute_Object=MibTableColumn
fileAttribute=_FileAttribute_Object((1,3,6,1,4,1,3320,9,185,1,2,1,6),_FileAttribute_Type())
fileAttribute.setMaxAccess(_E)
if mibBuilder.loadTexts:fileAttribute.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'nmsFileMgmtMIB':nmsFileMgmtMIB,'fileTransferManagement':fileTransferManagement,'fileTransferTable':fileTransferTable,'fileTransferEntry':fileTransferEntry,_G:fileTransferIndex,'fileTransferProtocolType':fileTransferProtocolType,'serverIpAddress':serverIpAddress,'ftpUserName':ftpUserName,'ftpUserPassword':ftpUserPassword,'transferFileSrcNamePath':transferFileSrcNamePath,'transferFileDstNamePath':transferFileDstNamePath,'transferAction':transferAction,'transferStatus':transferStatus,'fileInfoManagementTable':fileInfoManagementTable,'fileInfoManagementEntry':fileInfoManagementEntry,_I:filePath,_J:fileName,'fileSize':fileSize,'fileModifyTime':fileModifyTime,'fileManagementAction':fileManagementAction,'fileAttribute':fileAttribute})