_L='dellLanFileActionIndex'
_K='dellLanFileName'
_J='dellLanMngInfListPriority'
_I='dellLanMngInfListName'
_H='Unsigned32'
_G='NotificationType'
_F='Dell-LAN-SYSMNG-MIB'
_E='DisplayString'
_D='Integer32'
_C='read-only'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dellLanCommon,=mibBuilder.importSymbols('Dell-Vendor-MIB','dellLanCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier',_G,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_G,'TimeTicks',_H,'iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_E,'PhysAddress','RowStatus','TextualConvention','TruthValue')
dellLanSystemMng=ModuleIdentity((1,3,6,1,4,1,674,10895,5000,1,2))
class DellLanMngInfServiceType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('allType',0),('telnet',1),('snmp',2),('http',3),('https',4),('ssh',5),('sntp',6)))
class DellLanMngInfActionType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('permit',0),('deny',1)))
_DellLanMngIfGroup_ObjectIdentity=ObjectIdentity
dellLanMngIfGroup=_DellLanMngIfGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,1,2,1))
_DellLanMngInfEnable_Type=TruthValue
_DellLanMngInfEnable_Object=MibScalar
dellLanMngInfEnable=_DellLanMngInfEnable_Object((1,3,6,1,4,1,674,10895,5000,1,2,1,1),_DellLanMngInfEnable_Type())
dellLanMngInfEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:dellLanMngInfEnable.setStatus(_A)
class _DellLanMngInfActiveListName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_DellLanMngInfActiveListName_Type.__name__=_E
_DellLanMngInfActiveListName_Object=MibScalar
dellLanMngInfActiveListName=_DellLanMngInfActiveListName_Object((1,3,6,1,4,1,674,10895,5000,1,2,1,2),_DellLanMngInfActiveListName_Type())
dellLanMngInfActiveListName.setMaxAccess(_B)
if mibBuilder.loadTexts:dellLanMngInfActiveListName.setStatus(_A)
_DellLanMngInfListTable_Object=MibTable
dellLanMngInfListTable=_DellLanMngInfListTable_Object((1,3,6,1,4,1,674,10895,5000,1,2,1,3))
if mibBuilder.loadTexts:dellLanMngInfListTable.setStatus(_A)
_DellLanMngInfListEntry_Object=MibTableRow
dellLanMngInfListEntry=_DellLanMngInfListEntry_Object((1,3,6,1,4,1,674,10895,5000,1,2,1,3,1))
dellLanMngInfListEntry.setIndexNames((0,_F,_I),(0,_F,_J))
if mibBuilder.loadTexts:dellLanMngInfListEntry.setStatus(_A)
class _DellLanMngInfListName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_DellLanMngInfListName_Type.__name__=_E
_DellLanMngInfListName_Object=MibTableColumn
dellLanMngInfListName=_DellLanMngInfListName_Object((1,3,6,1,4,1,674,10895,5000,1,2,1,3,1,1),_DellLanMngInfListName_Type())
dellLanMngInfListName.setMaxAccess(_C)
if mibBuilder.loadTexts:dellLanMngInfListName.setStatus(_A)
class _DellLanMngInfListPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_DellLanMngInfListPriority_Type.__name__=_H
_DellLanMngInfListPriority_Object=MibTableColumn
dellLanMngInfListPriority=_DellLanMngInfListPriority_Object((1,3,6,1,4,1,674,10895,5000,1,2,1,3,1,2),_DellLanMngInfListPriority_Type())
dellLanMngInfListPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:dellLanMngInfListPriority.setStatus(_A)
_DellLanMngInfListIfIndex_Type=Unsigned32
_DellLanMngInfListIfIndex_Object=MibTableColumn
dellLanMngInfListIfIndex=_DellLanMngInfListIfIndex_Object((1,3,6,1,4,1,674,10895,5000,1,2,1,3,1,3),_DellLanMngInfListIfIndex_Type())
dellLanMngInfListIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dellLanMngInfListIfIndex.setStatus(_A)
_DellLanMngInfListIpAddr_Type=IpAddress
_DellLanMngInfListIpAddr_Object=MibTableColumn
dellLanMngInfListIpAddr=_DellLanMngInfListIpAddr_Object((1,3,6,1,4,1,674,10895,5000,1,2,1,3,1,4),_DellLanMngInfListIpAddr_Type())
dellLanMngInfListIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:dellLanMngInfListIpAddr.setStatus(_A)
_DellLanMngInfListIpNetMask_Type=IpAddress
_DellLanMngInfListIpNetMask_Object=MibTableColumn
dellLanMngInfListIpNetMask=_DellLanMngInfListIpNetMask_Object((1,3,6,1,4,1,674,10895,5000,1,2,1,3,1,5),_DellLanMngInfListIpNetMask_Type())
dellLanMngInfListIpNetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:dellLanMngInfListIpNetMask.setStatus(_A)
_DellLanMngInfListService_Type=DellLanMngInfServiceType
_DellLanMngInfListService_Object=MibTableColumn
dellLanMngInfListService=_DellLanMngInfListService_Object((1,3,6,1,4,1,674,10895,5000,1,2,1,3,1,6),_DellLanMngInfListService_Type())
dellLanMngInfListService.setMaxAccess(_B)
if mibBuilder.loadTexts:dellLanMngInfListService.setStatus(_A)
_DellLanMngInfListAction_Type=DellLanMngInfActionType
_DellLanMngInfListAction_Object=MibTableColumn
dellLanMngInfListAction=_DellLanMngInfListAction_Object((1,3,6,1,4,1,674,10895,5000,1,2,1,3,1,7),_DellLanMngInfListAction_Type())
dellLanMngInfListAction.setMaxAccess(_B)
if mibBuilder.loadTexts:dellLanMngInfListAction.setStatus(_A)
_DellLanMngInfListRowStatus_Type=RowStatus
_DellLanMngInfListRowStatus_Object=MibTableColumn
dellLanMngInfListRowStatus=_DellLanMngInfListRowStatus_Object((1,3,6,1,4,1,674,10895,5000,1,2,1,3,1,8),_DellLanMngInfListRowStatus_Type())
dellLanMngInfListRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dellLanMngInfListRowStatus.setStatus(_A)
_DellLanMngInfListVlanId_Type=Unsigned32
_DellLanMngInfListVlanId_Object=MibTableColumn
dellLanMngInfListVlanId=_DellLanMngInfListVlanId_Object((1,3,6,1,4,1,674,10895,5000,1,2,1,3,1,9),_DellLanMngInfListVlanId_Type())
dellLanMngInfListVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:dellLanMngInfListVlanId.setStatus(_A)
_DellLanFileSysGroup_ObjectIdentity=ObjectIdentity
dellLanFileSysGroup=_DellLanFileSysGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,1,2,2))
_DellLanFSMaxSize_Type=Integer32
_DellLanFSMaxSize_Object=MibScalar
dellLanFSMaxSize=_DellLanFSMaxSize_Object((1,3,6,1,4,1,674,10895,5000,1,2,2,1),_DellLanFSMaxSize_Type())
dellLanFSMaxSize.setMaxAccess(_C)
if mibBuilder.loadTexts:dellLanFSMaxSize.setStatus(_A)
_DellLanFSAvailableSize_Type=Integer32
_DellLanFSAvailableSize_Object=MibScalar
dellLanFSAvailableSize=_DellLanFSAvailableSize_Object((1,3,6,1,4,1,674,10895,5000,1,2,2,2),_DellLanFSAvailableSize_Type())
dellLanFSAvailableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:dellLanFSAvailableSize.setStatus(_A)
_DellLanFileTable_Object=MibTable
dellLanFileTable=_DellLanFileTable_Object((1,3,6,1,4,1,674,10895,5000,1,2,2,3))
if mibBuilder.loadTexts:dellLanFileTable.setStatus(_A)
_DellLanFileEntry_Object=MibTableRow
dellLanFileEntry=_DellLanFileEntry_Object((1,3,6,1,4,1,674,10895,5000,1,2,2,3,1))
dellLanFileEntry.setIndexNames((0,_F,_K))
if mibBuilder.loadTexts:dellLanFileEntry.setStatus(_A)
class _DellLanFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_DellLanFileName_Type.__name__=_E
_DellLanFileName_Object=MibTableColumn
dellLanFileName=_DellLanFileName_Object((1,3,6,1,4,1,674,10895,5000,1,2,2,3,1,1),_DellLanFileName_Type())
dellLanFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:dellLanFileName.setStatus(_A)
class _DellLanFilePermission_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('readonly',1),('writeonly',2),('readWrite',3),('noReadNoWrite',4)))
_DellLanFilePermission_Type.__name__=_D
_DellLanFilePermission_Object=MibTableColumn
dellLanFilePermission=_DellLanFilePermission_Object((1,3,6,1,4,1,674,10895,5000,1,2,2,3,1,2),_DellLanFilePermission_Type())
dellLanFilePermission.setMaxAccess(_C)
if mibBuilder.loadTexts:dellLanFilePermission.setStatus(_A)
class _DellLanFilePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_DellLanFilePriority_Type.__name__=_D
_DellLanFilePriority_Object=MibTableColumn
dellLanFilePriority=_DellLanFilePriority_Object((1,3,6,1,4,1,674,10895,5000,1,2,2,3,1,3),_DellLanFilePriority_Type())
dellLanFilePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:dellLanFilePriority.setStatus(_A)
_DellLanFileSize_Type=Integer32
_DellLanFileSize_Object=MibTableColumn
dellLanFileSize=_DellLanFileSize_Object((1,3,6,1,4,1,674,10895,5000,1,2,2,3,1,4),_DellLanFileSize_Type())
dellLanFileSize.setMaxAccess(_C)
if mibBuilder.loadTexts:dellLanFileSize.setStatus(_A)
class _DellLanFileType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('image',1),('config',2),('log',3),('sys',4),('activeImg',5)))
_DellLanFileType_Type.__name__=_D
_DellLanFileType_Object=MibTableColumn
dellLanFileType=_DellLanFileType_Object((1,3,6,1,4,1,674,10895,5000,1,2,2,3,1,5),_DellLanFileType_Type())
dellLanFileType.setMaxAccess(_C)
if mibBuilder.loadTexts:dellLanFileType.setStatus(_A)
_DellLanFileModificationDate_Type=DisplayString
_DellLanFileModificationDate_Object=MibTableColumn
dellLanFileModificationDate=_DellLanFileModificationDate_Object((1,3,6,1,4,1,674,10895,5000,1,2,2,3,1,6),_DellLanFileModificationDate_Type())
dellLanFileModificationDate.setMaxAccess(_C)
if mibBuilder.loadTexts:dellLanFileModificationDate.setStatus(_A)
_DellLanFileModificationTime_Type=DisplayString
_DellLanFileModificationTime_Object=MibTableColumn
dellLanFileModificationTime=_DellLanFileModificationTime_Object((1,3,6,1,4,1,674,10895,5000,1,2,2,3,1,7),_DellLanFileModificationTime_Type())
dellLanFileModificationTime.setMaxAccess(_C)
if mibBuilder.loadTexts:dellLanFileModificationTime.setStatus(_A)
class _DellLanFileDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_DellLanFileDescription_Type.__name__=_E
_DellLanFileDescription_Object=MibTableColumn
dellLanFileDescription=_DellLanFileDescription_Object((1,3,6,1,4,1,674,10895,5000,1,2,2,3,1,8),_DellLanFileDescription_Type())
dellLanFileDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:dellLanFileDescription.setStatus(_A)
_DellLanFileActionTable_Object=MibTable
dellLanFileActionTable=_DellLanFileActionTable_Object((1,3,6,1,4,1,674,10895,5000,1,2,2,4))
if mibBuilder.loadTexts:dellLanFileActionTable.setStatus(_A)
_DellLanFileActionEntry_Object=MibTableRow
dellLanFileActionEntry=_DellLanFileActionEntry_Object((1,3,6,1,4,1,674,10895,5000,1,2,2,4,1))
dellLanFileActionEntry.setIndexNames((0,_F,_L))
if mibBuilder.loadTexts:dellLanFileActionEntry.setStatus(_A)
_DellLanFileActionIndex_Type=Integer32
_DellLanFileActionIndex_Object=MibTableColumn
dellLanFileActionIndex=_DellLanFileActionIndex_Object((1,3,6,1,4,1,674,10895,5000,1,2,2,4,1,1),_DellLanFileActionIndex_Type())
dellLanFileActionIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:dellLanFileActionIndex.setStatus(_A)
_DellLanFileActionSourceFile_Type=DisplayString
_DellLanFileActionSourceFile_Object=MibTableColumn
dellLanFileActionSourceFile=_DellLanFileActionSourceFile_Object((1,3,6,1,4,1,674,10895,5000,1,2,2,4,1,2),_DellLanFileActionSourceFile_Type())
dellLanFileActionSourceFile.setMaxAccess(_B)
if mibBuilder.loadTexts:dellLanFileActionSourceFile.setStatus(_A)
_DellLanFileActionDestFile_Type=DisplayString
_DellLanFileActionDestFile_Object=MibTableColumn
dellLanFileActionDestFile=_DellLanFileActionDestFile_Object((1,3,6,1,4,1,674,10895,5000,1,2,2,4,1,3),_DellLanFileActionDestFile_Type())
dellLanFileActionDestFile.setMaxAccess(_B)
if mibBuilder.loadTexts:dellLanFileActionDestFile.setStatus(_A)
_DellLanFileActionForceAction_Type=TruthValue
_DellLanFileActionForceAction_Object=MibTableColumn
dellLanFileActionForceAction=_DellLanFileActionForceAction_Object((1,3,6,1,4,1,674,10895,5000,1,2,2,4,1,4),_DellLanFileActionForceAction_Type())
dellLanFileActionForceAction.setMaxAccess(_B)
if mibBuilder.loadTexts:dellLanFileActionForceAction.setStatus(_A)
class _DellLanFileActionCommand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('copy',2),('delete',3)))
_DellLanFileActionCommand_Type.__name__=_D
_DellLanFileActionCommand_Object=MibTableColumn
dellLanFileActionCommand=_DellLanFileActionCommand_Object((1,3,6,1,4,1,674,10895,5000,1,2,2,4,1,5),_DellLanFileActionCommand_Type())
dellLanFileActionCommand.setMaxAccess(_B)
if mibBuilder.loadTexts:dellLanFileActionCommand.setStatus(_A)
class _DellLanFileActionResultCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('success',0),('statusPending',1),('fileNotFound',2),('invalidCmd',3),('unknownError',4),('tftpServerConnectFailed',5),('fileSystemFull',6),('overwriteNotRequested',7),('overwriteFailed',8),('permissionDenied',9),('incompatFileType',10),('invalidDest',11)))
_DellLanFileActionResultCode_Type.__name__=_D
_DellLanFileActionResultCode_Object=MibTableColumn
dellLanFileActionResultCode=_DellLanFileActionResultCode_Object((1,3,6,1,4,1,674,10895,5000,1,2,2,4,1,6),_DellLanFileActionResultCode_Type())
dellLanFileActionResultCode.setMaxAccess(_C)
if mibBuilder.loadTexts:dellLanFileActionResultCode.setStatus(_A)
_DellLanSysMngGroup_ObjectIdentity=ObjectIdentity
dellLanSysMngGroup=_DellLanSysMngGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,1,2,3))
_DellLanSysActionReload_Type=Integer32
_DellLanSysActionReload_Object=MibScalar
dellLanSysActionReload=_DellLanSysActionReload_Object((1,3,6,1,4,1,674,10895,5000,1,2,3,1),_DellLanSysActionReload_Type())
dellLanSysActionReload.setMaxAccess(_B)
if mibBuilder.loadTexts:dellLanSysActionReload.setStatus(_A)
_DellLanSysActionSetActiveImage_Type=DisplayString
_DellLanSysActionSetActiveImage_Object=MibScalar
dellLanSysActionSetActiveImage=_DellLanSysActionSetActiveImage_Object((1,3,6,1,4,1,674,10895,5000,1,2,3,2),_DellLanSysActionSetActiveImage_Type())
dellLanSysActionSetActiveImage.setMaxAccess(_B)
if mibBuilder.loadTexts:dellLanSysActionSetActiveImage.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'DellLanMngInfServiceType':DellLanMngInfServiceType,'DellLanMngInfActionType':DellLanMngInfActionType,'dellLanSystemMng':dellLanSystemMng,'dellLanMngIfGroup':dellLanMngIfGroup,'dellLanMngInfEnable':dellLanMngInfEnable,'dellLanMngInfActiveListName':dellLanMngInfActiveListName,'dellLanMngInfListTable':dellLanMngInfListTable,'dellLanMngInfListEntry':dellLanMngInfListEntry,_I:dellLanMngInfListName,_J:dellLanMngInfListPriority,'dellLanMngInfListIfIndex':dellLanMngInfListIfIndex,'dellLanMngInfListIpAddr':dellLanMngInfListIpAddr,'dellLanMngInfListIpNetMask':dellLanMngInfListIpNetMask,'dellLanMngInfListService':dellLanMngInfListService,'dellLanMngInfListAction':dellLanMngInfListAction,'dellLanMngInfListRowStatus':dellLanMngInfListRowStatus,'dellLanMngInfListVlanId':dellLanMngInfListVlanId,'dellLanFileSysGroup':dellLanFileSysGroup,'dellLanFSMaxSize':dellLanFSMaxSize,'dellLanFSAvailableSize':dellLanFSAvailableSize,'dellLanFileTable':dellLanFileTable,'dellLanFileEntry':dellLanFileEntry,_K:dellLanFileName,'dellLanFilePermission':dellLanFilePermission,'dellLanFilePriority':dellLanFilePriority,'dellLanFileSize':dellLanFileSize,'dellLanFileType':dellLanFileType,'dellLanFileModificationDate':dellLanFileModificationDate,'dellLanFileModificationTime':dellLanFileModificationTime,'dellLanFileDescription':dellLanFileDescription,'dellLanFileActionTable':dellLanFileActionTable,'dellLanFileActionEntry':dellLanFileActionEntry,_L:dellLanFileActionIndex,'dellLanFileActionSourceFile':dellLanFileActionSourceFile,'dellLanFileActionDestFile':dellLanFileActionDestFile,'dellLanFileActionForceAction':dellLanFileActionForceAction,'dellLanFileActionCommand':dellLanFileActionCommand,'dellLanFileActionResultCode':dellLanFileActionResultCode,'dellLanSysMngGroup':dellLanSysMngGroup,'dellLanSysActionReload':dellLanSysActionReload,'dellLanSysActionSetActiveImage':dellLanSysActionSetActiveImage})