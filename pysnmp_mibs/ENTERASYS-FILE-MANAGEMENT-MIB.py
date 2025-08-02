_v='etsysFileOperationGroup'
_u='etsysFileListingGroup'
_t='etsysFileTransferGroup'
_s='etsysFileOperationRowStatus'
_r='etsysFileOperationErrorDescription'
_q='etsysFileOperationFileNewName'
_p='etsysFileOperationFileName'
_o='etsysFileOperationType'
_n='etsysFileOperationNextAvailableIndex'
_m='etsysFileOperationsCompleted'
_l='etsysFileOperationsCurrent'
_k='etsysFileOperationLimit'
_j='etsysFileListingFileOrigin'
_i='etsysFileListingFileDate'
_h='etsysFileListingFileType'
_g='etsysFileListingFileSize'
_f='etsysFileListingFileName'
_e='etsysFileTransferRequestRowStatus'
_d='etsysFileTransferRequestStorageType'
_c='etsysFileTransferRequestErrorDescription'
_b='etsysFileTransferRequestBytesTransferred'
_a='etsysFileTransferRequestCompletionTime'
_Z='etsysFileTransferRequestEnqueuedTime'
_Y='etsysFileTransferRequestOperStatus'
_X='etsysFileTransferRequestDestination'
_W='etsysFileTransferRequestSource'
_V='etsysFileTransferRequestNextAvailableIndex'
_U='etsysFileTransferRequestSupportedURLs'
_T='etsysFileTransferRequestsCompleted'
_S='etsysFileTransferRequestsCurrent'
_R='etsysFileTransferRequestLimit'
_Q='etsysFileOperationIndex'
_P='etsysFileListingIndex'
_O='etsysFileTransferRequestIndex'
_N='StorageType'
_M='DisplayString'
_L='hrFSIndex'
_K='HOST-RESOURCES-MIB'
_J='0000000000000000'
_I='not-accessible'
_H='DateAndTime'
_G='Integer32'
_F='SnmpAdminString'
_E='read-create'
_D='Unsigned32'
_C='read-only'
_B='ENTERASYS-FILE-MANAGEMENT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
hrFSIndex,=mibBuilder.importSymbols(_K,_L)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_H,_M,'PhysAddress','RowStatus',_N,'TextualConvention')
etsysFileManagementMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,15))
if mibBuilder.loadTexts:etsysFileManagementMIB.setRevisions(('2001-12-03 19:54',))
_EtsysFileTransfer_ObjectIdentity=ObjectIdentity
etsysFileTransfer=_EtsysFileTransfer_ObjectIdentity((1,3,6,1,4,1,5624,1,2,15,1))
class _EtsysFileTransferRequestLimit_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_EtsysFileTransferRequestLimit_Type.__name__=_D
_EtsysFileTransferRequestLimit_Object=MibScalar
etsysFileTransferRequestLimit=_EtsysFileTransferRequestLimit_Object((1,3,6,1,4,1,5624,1,2,15,1,1),_EtsysFileTransferRequestLimit_Type())
etsysFileTransferRequestLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysFileTransferRequestLimit.setStatus(_A)
_EtsysFileTransferRequestsCurrent_Type=Gauge32
_EtsysFileTransferRequestsCurrent_Object=MibScalar
etsysFileTransferRequestsCurrent=_EtsysFileTransferRequestsCurrent_Object((1,3,6,1,4,1,5624,1,2,15,1,2),_EtsysFileTransferRequestsCurrent_Type())
etsysFileTransferRequestsCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysFileTransferRequestsCurrent.setStatus(_A)
_EtsysFileTransferRequestsCompleted_Type=Counter32
_EtsysFileTransferRequestsCompleted_Object=MibScalar
etsysFileTransferRequestsCompleted=_EtsysFileTransferRequestsCompleted_Object((1,3,6,1,4,1,5624,1,2,15,1,3),_EtsysFileTransferRequestsCompleted_Type())
etsysFileTransferRequestsCompleted.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysFileTransferRequestsCompleted.setStatus(_A)
class _EtsysFileTransferRequestSupportedURLs_Type(Bits):namedValues=NamedValues(*(('etsysFileTransferFtp',0),('etsysFileTransferRcp',1),('etsysFileTransferHttp',2),('etsysFileTransferTftp',3),('etsysFileTransferFile',4)))
_EtsysFileTransferRequestSupportedURLs_Type.__name__='Bits'
_EtsysFileTransferRequestSupportedURLs_Object=MibScalar
etsysFileTransferRequestSupportedURLs=_EtsysFileTransferRequestSupportedURLs_Object((1,3,6,1,4,1,5624,1,2,15,1,4),_EtsysFileTransferRequestSupportedURLs_Type())
etsysFileTransferRequestSupportedURLs.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysFileTransferRequestSupportedURLs.setStatus(_A)
class _EtsysFileTransferRequestNextAvailableIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_EtsysFileTransferRequestNextAvailableIndex_Type.__name__=_D
_EtsysFileTransferRequestNextAvailableIndex_Object=MibScalar
etsysFileTransferRequestNextAvailableIndex=_EtsysFileTransferRequestNextAvailableIndex_Object((1,3,6,1,4,1,5624,1,2,15,1,5),_EtsysFileTransferRequestNextAvailableIndex_Type())
etsysFileTransferRequestNextAvailableIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysFileTransferRequestNextAvailableIndex.setStatus(_A)
_EtsysFileTransferRequestTable_Object=MibTable
etsysFileTransferRequestTable=_EtsysFileTransferRequestTable_Object((1,3,6,1,4,1,5624,1,2,15,1,6))
if mibBuilder.loadTexts:etsysFileTransferRequestTable.setStatus(_A)
_EtsysFileTransferRequestEntry_Object=MibTableRow
etsysFileTransferRequestEntry=_EtsysFileTransferRequestEntry_Object((1,3,6,1,4,1,5624,1,2,15,1,6,1))
etsysFileTransferRequestEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:etsysFileTransferRequestEntry.setStatus(_A)
class _EtsysFileTransferRequestIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_EtsysFileTransferRequestIndex_Type.__name__=_D
_EtsysFileTransferRequestIndex_Object=MibTableColumn
etsysFileTransferRequestIndex=_EtsysFileTransferRequestIndex_Object((1,3,6,1,4,1,5624,1,2,15,1,6,1,1),_EtsysFileTransferRequestIndex_Type())
etsysFileTransferRequestIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:etsysFileTransferRequestIndex.setStatus(_A)
_EtsysFileTransferRequestSource_Type=DisplayString
_EtsysFileTransferRequestSource_Object=MibTableColumn
etsysFileTransferRequestSource=_EtsysFileTransferRequestSource_Object((1,3,6,1,4,1,5624,1,2,15,1,6,1,2),_EtsysFileTransferRequestSource_Type())
etsysFileTransferRequestSource.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysFileTransferRequestSource.setStatus(_A)
_EtsysFileTransferRequestDestination_Type=DisplayString
_EtsysFileTransferRequestDestination_Object=MibTableColumn
etsysFileTransferRequestDestination=_EtsysFileTransferRequestDestination_Object((1,3,6,1,4,1,5624,1,2,15,1,6,1,3),_EtsysFileTransferRequestDestination_Type())
etsysFileTransferRequestDestination.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysFileTransferRequestDestination.setStatus(_A)
class _EtsysFileTransferRequestOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('inactive',1),('pending',2),('running',3),('success',4),('failure',5)))
_EtsysFileTransferRequestOperStatus_Type.__name__=_G
_EtsysFileTransferRequestOperStatus_Object=MibTableColumn
etsysFileTransferRequestOperStatus=_EtsysFileTransferRequestOperStatus_Object((1,3,6,1,4,1,5624,1,2,15,1,6,1,4),_EtsysFileTransferRequestOperStatus_Type())
etsysFileTransferRequestOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysFileTransferRequestOperStatus.setStatus(_A)
class _EtsysFileTransferRequestEnqueuedTime_Type(DateAndTime):defaultHexValue=_J
_EtsysFileTransferRequestEnqueuedTime_Type.__name__=_H
_EtsysFileTransferRequestEnqueuedTime_Object=MibTableColumn
etsysFileTransferRequestEnqueuedTime=_EtsysFileTransferRequestEnqueuedTime_Object((1,3,6,1,4,1,5624,1,2,15,1,6,1,5),_EtsysFileTransferRequestEnqueuedTime_Type())
etsysFileTransferRequestEnqueuedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysFileTransferRequestEnqueuedTime.setStatus(_A)
class _EtsysFileTransferRequestCompletionTime_Type(DateAndTime):defaultHexValue=_J
_EtsysFileTransferRequestCompletionTime_Type.__name__=_H
_EtsysFileTransferRequestCompletionTime_Object=MibTableColumn
etsysFileTransferRequestCompletionTime=_EtsysFileTransferRequestCompletionTime_Object((1,3,6,1,4,1,5624,1,2,15,1,6,1,6),_EtsysFileTransferRequestCompletionTime_Type())
etsysFileTransferRequestCompletionTime.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysFileTransferRequestCompletionTime.setStatus(_A)
class _EtsysFileTransferRequestBytesTransferred_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_EtsysFileTransferRequestBytesTransferred_Type.__name__=_G
_EtsysFileTransferRequestBytesTransferred_Object=MibTableColumn
etsysFileTransferRequestBytesTransferred=_EtsysFileTransferRequestBytesTransferred_Object((1,3,6,1,4,1,5624,1,2,15,1,6,1,7),_EtsysFileTransferRequestBytesTransferred_Type())
etsysFileTransferRequestBytesTransferred.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysFileTransferRequestBytesTransferred.setStatus(_A)
class _EtsysFileTransferRequestErrorDescription_Type(SnmpAdminString):defaultHexValue=''
_EtsysFileTransferRequestErrorDescription_Type.__name__=_F
_EtsysFileTransferRequestErrorDescription_Object=MibTableColumn
etsysFileTransferRequestErrorDescription=_EtsysFileTransferRequestErrorDescription_Object((1,3,6,1,4,1,5624,1,2,15,1,6,1,8),_EtsysFileTransferRequestErrorDescription_Type())
etsysFileTransferRequestErrorDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysFileTransferRequestErrorDescription.setStatus(_A)
class _EtsysFileTransferRequestStorageType_Type(StorageType):defaultValue=2
_EtsysFileTransferRequestStorageType_Type.__name__=_N
_EtsysFileTransferRequestStorageType_Object=MibTableColumn
etsysFileTransferRequestStorageType=_EtsysFileTransferRequestStorageType_Object((1,3,6,1,4,1,5624,1,2,15,1,6,1,9),_EtsysFileTransferRequestStorageType_Type())
etsysFileTransferRequestStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysFileTransferRequestStorageType.setStatus(_A)
_EtsysFileTransferRequestRowStatus_Type=RowStatus
_EtsysFileTransferRequestRowStatus_Object=MibTableColumn
etsysFileTransferRequestRowStatus=_EtsysFileTransferRequestRowStatus_Object((1,3,6,1,4,1,5624,1,2,15,1,6,1,10),_EtsysFileTransferRequestRowStatus_Type())
etsysFileTransferRequestRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysFileTransferRequestRowStatus.setStatus(_A)
_EtsysFileListing_ObjectIdentity=ObjectIdentity
etsysFileListing=_EtsysFileListing_ObjectIdentity((1,3,6,1,4,1,5624,1,2,15,2))
_EtsysFileListingTable_Object=MibTable
etsysFileListingTable=_EtsysFileListingTable_Object((1,3,6,1,4,1,5624,1,2,15,2,1))
if mibBuilder.loadTexts:etsysFileListingTable.setStatus(_A)
_EtsysFileListingEntry_Object=MibTableRow
etsysFileListingEntry=_EtsysFileListingEntry_Object((1,3,6,1,4,1,5624,1,2,15,2,1,1))
etsysFileListingEntry.setIndexNames((0,_K,_L),(0,_B,_P))
if mibBuilder.loadTexts:etsysFileListingEntry.setStatus(_A)
_EtsysFileListingIndex_Type=Unsigned32
_EtsysFileListingIndex_Object=MibTableColumn
etsysFileListingIndex=_EtsysFileListingIndex_Object((1,3,6,1,4,1,5624,1,2,15,2,1,1,1),_EtsysFileListingIndex_Type())
etsysFileListingIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:etsysFileListingIndex.setStatus(_A)
_EtsysFileListingFileName_Type=DisplayString
_EtsysFileListingFileName_Object=MibTableColumn
etsysFileListingFileName=_EtsysFileListingFileName_Object((1,3,6,1,4,1,5624,1,2,15,2,1,1,2),_EtsysFileListingFileName_Type())
etsysFileListingFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysFileListingFileName.setStatus(_A)
class _EtsysFileListingFileSize_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_EtsysFileListingFileSize_Type.__name__=_D
_EtsysFileListingFileSize_Object=MibTableColumn
etsysFileListingFileSize=_EtsysFileListingFileSize_Object((1,3,6,1,4,1,5624,1,2,15,2,1,1,3),_EtsysFileListingFileSize_Type())
etsysFileListingFileSize.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysFileListingFileSize.setStatus(_A)
class _EtsysFileListingFileType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('unsupported',1),('directory',2),('ordinary-file',3),('symbolic-link',4)))
_EtsysFileListingFileType_Type.__name__=_G
_EtsysFileListingFileType_Object=MibTableColumn
etsysFileListingFileType=_EtsysFileListingFileType_Object((1,3,6,1,4,1,5624,1,2,15,2,1,1,4),_EtsysFileListingFileType_Type())
etsysFileListingFileType.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysFileListingFileType.setStatus(_A)
class _EtsysFileListingFileDate_Type(DateAndTime):defaultHexValue=_J
_EtsysFileListingFileDate_Type.__name__=_H
_EtsysFileListingFileDate_Object=MibTableColumn
etsysFileListingFileDate=_EtsysFileListingFileDate_Object((1,3,6,1,4,1,5624,1,2,15,2,1,1,5),_EtsysFileListingFileDate_Type())
etsysFileListingFileDate.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysFileListingFileDate.setStatus(_A)
class _EtsysFileListingFileOrigin_Type(DisplayString):defaultHexValue=''
_EtsysFileListingFileOrigin_Type.__name__=_M
_EtsysFileListingFileOrigin_Object=MibTableColumn
etsysFileListingFileOrigin=_EtsysFileListingFileOrigin_Object((1,3,6,1,4,1,5624,1,2,15,2,1,1,6),_EtsysFileListingFileOrigin_Type())
etsysFileListingFileOrigin.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysFileListingFileOrigin.setStatus(_A)
_EtsysFileOperation_ObjectIdentity=ObjectIdentity
etsysFileOperation=_EtsysFileOperation_ObjectIdentity((1,3,6,1,4,1,5624,1,2,15,3))
class _EtsysFileOperationLimit_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_EtsysFileOperationLimit_Type.__name__=_D
_EtsysFileOperationLimit_Object=MibScalar
etsysFileOperationLimit=_EtsysFileOperationLimit_Object((1,3,6,1,4,1,5624,1,2,15,3,1),_EtsysFileOperationLimit_Type())
etsysFileOperationLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysFileOperationLimit.setStatus(_A)
_EtsysFileOperationsCurrent_Type=Gauge32
_EtsysFileOperationsCurrent_Object=MibScalar
etsysFileOperationsCurrent=_EtsysFileOperationsCurrent_Object((1,3,6,1,4,1,5624,1,2,15,3,2),_EtsysFileOperationsCurrent_Type())
etsysFileOperationsCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysFileOperationsCurrent.setStatus(_A)
_EtsysFileOperationsCompleted_Type=Counter32
_EtsysFileOperationsCompleted_Object=MibScalar
etsysFileOperationsCompleted=_EtsysFileOperationsCompleted_Object((1,3,6,1,4,1,5624,1,2,15,3,3),_EtsysFileOperationsCompleted_Type())
etsysFileOperationsCompleted.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysFileOperationsCompleted.setStatus(_A)
class _EtsysFileOperationNextAvailableIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_EtsysFileOperationNextAvailableIndex_Type.__name__=_D
_EtsysFileOperationNextAvailableIndex_Object=MibScalar
etsysFileOperationNextAvailableIndex=_EtsysFileOperationNextAvailableIndex_Object((1,3,6,1,4,1,5624,1,2,15,3,4),_EtsysFileOperationNextAvailableIndex_Type())
etsysFileOperationNextAvailableIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysFileOperationNextAvailableIndex.setStatus(_A)
_EtsysFileOperationTable_Object=MibTable
etsysFileOperationTable=_EtsysFileOperationTable_Object((1,3,6,1,4,1,5624,1,2,15,3,5))
if mibBuilder.loadTexts:etsysFileOperationTable.setStatus(_A)
_EtsysFileOperationEntry_Object=MibTableRow
etsysFileOperationEntry=_EtsysFileOperationEntry_Object((1,3,6,1,4,1,5624,1,2,15,3,5,1))
etsysFileOperationEntry.setIndexNames((0,_B,_Q))
if mibBuilder.loadTexts:etsysFileOperationEntry.setStatus(_A)
class _EtsysFileOperationIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_EtsysFileOperationIndex_Type.__name__=_D
_EtsysFileOperationIndex_Object=MibTableColumn
etsysFileOperationIndex=_EtsysFileOperationIndex_Object((1,3,6,1,4,1,5624,1,2,15,3,5,1,1),_EtsysFileOperationIndex_Type())
etsysFileOperationIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:etsysFileOperationIndex.setStatus(_A)
class _EtsysFileOperationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('delete',1),('rename',2)))
_EtsysFileOperationType_Type.__name__=_G
_EtsysFileOperationType_Object=MibTableColumn
etsysFileOperationType=_EtsysFileOperationType_Object((1,3,6,1,4,1,5624,1,2,15,3,5,1,2),_EtsysFileOperationType_Type())
etsysFileOperationType.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysFileOperationType.setStatus(_A)
class _EtsysFileOperationFileName_Type(SnmpAdminString):defaultHexValue=''
_EtsysFileOperationFileName_Type.__name__=_F
_EtsysFileOperationFileName_Object=MibTableColumn
etsysFileOperationFileName=_EtsysFileOperationFileName_Object((1,3,6,1,4,1,5624,1,2,15,3,5,1,3),_EtsysFileOperationFileName_Type())
etsysFileOperationFileName.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysFileOperationFileName.setStatus(_A)
class _EtsysFileOperationFileNewName_Type(SnmpAdminString):defaultHexValue=''
_EtsysFileOperationFileNewName_Type.__name__=_F
_EtsysFileOperationFileNewName_Object=MibTableColumn
etsysFileOperationFileNewName=_EtsysFileOperationFileNewName_Object((1,3,6,1,4,1,5624,1,2,15,3,5,1,4),_EtsysFileOperationFileNewName_Type())
etsysFileOperationFileNewName.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysFileOperationFileNewName.setStatus(_A)
class _EtsysFileOperationErrorDescription_Type(SnmpAdminString):defaultHexValue=''
_EtsysFileOperationErrorDescription_Type.__name__=_F
_EtsysFileOperationErrorDescription_Object=MibTableColumn
etsysFileOperationErrorDescription=_EtsysFileOperationErrorDescription_Object((1,3,6,1,4,1,5624,1,2,15,3,5,1,5),_EtsysFileOperationErrorDescription_Type())
etsysFileOperationErrorDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysFileOperationErrorDescription.setStatus(_A)
_EtsysFileOperationRowStatus_Type=RowStatus
_EtsysFileOperationRowStatus_Object=MibTableColumn
etsysFileOperationRowStatus=_EtsysFileOperationRowStatus_Object((1,3,6,1,4,1,5624,1,2,15,3,5,1,6),_EtsysFileOperationRowStatus_Type())
etsysFileOperationRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysFileOperationRowStatus.setStatus(_A)
_EtsysFileConformance_ObjectIdentity=ObjectIdentity
etsysFileConformance=_EtsysFileConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,15,4))
_EtsysFileGroups_ObjectIdentity=ObjectIdentity
etsysFileGroups=_EtsysFileGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,15,4,1))
_EtsysFileCompliances_ObjectIdentity=ObjectIdentity
etsysFileCompliances=_EtsysFileCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,15,4,2))
etsysFileTransferGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,15,4,1,1))
etsysFileTransferGroup.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:etsysFileTransferGroup.setStatus(_A)
etsysFileListingGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,15,4,1,2))
etsysFileListingGroup.setObjects(*((_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j)))
if mibBuilder.loadTexts:etsysFileListingGroup.setStatus(_A)
etsysFileOperationGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,15,4,1,3))
etsysFileOperationGroup.setObjects(*((_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s)))
if mibBuilder.loadTexts:etsysFileOperationGroup.setStatus(_A)
etsysFileCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,15,4,2,1))
etsysFileCompliance.setObjects(*((_B,_t),(_B,_u),(_B,_v)))
if mibBuilder.loadTexts:etsysFileCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'etsysFileManagementMIB':etsysFileManagementMIB,'etsysFileTransfer':etsysFileTransfer,_R:etsysFileTransferRequestLimit,_S:etsysFileTransferRequestsCurrent,_T:etsysFileTransferRequestsCompleted,_U:etsysFileTransferRequestSupportedURLs,_V:etsysFileTransferRequestNextAvailableIndex,'etsysFileTransferRequestTable':etsysFileTransferRequestTable,'etsysFileTransferRequestEntry':etsysFileTransferRequestEntry,_O:etsysFileTransferRequestIndex,_W:etsysFileTransferRequestSource,_X:etsysFileTransferRequestDestination,_Y:etsysFileTransferRequestOperStatus,_Z:etsysFileTransferRequestEnqueuedTime,_a:etsysFileTransferRequestCompletionTime,_b:etsysFileTransferRequestBytesTransferred,_c:etsysFileTransferRequestErrorDescription,_d:etsysFileTransferRequestStorageType,_e:etsysFileTransferRequestRowStatus,'etsysFileListing':etsysFileListing,'etsysFileListingTable':etsysFileListingTable,'etsysFileListingEntry':etsysFileListingEntry,_P:etsysFileListingIndex,_f:etsysFileListingFileName,_g:etsysFileListingFileSize,_h:etsysFileListingFileType,_i:etsysFileListingFileDate,_j:etsysFileListingFileOrigin,'etsysFileOperation':etsysFileOperation,_k:etsysFileOperationLimit,_l:etsysFileOperationsCurrent,_m:etsysFileOperationsCompleted,_n:etsysFileOperationNextAvailableIndex,'etsysFileOperationTable':etsysFileOperationTable,'etsysFileOperationEntry':etsysFileOperationEntry,_Q:etsysFileOperationIndex,_o:etsysFileOperationType,_p:etsysFileOperationFileName,_q:etsysFileOperationFileNewName,_r:etsysFileOperationErrorDescription,_s:etsysFileOperationRowStatus,'etsysFileConformance':etsysFileConformance,'etsysFileGroups':etsysFileGroups,_t:etsysFileTransferGroup,_u:etsysFileListingGroup,_v:etsysFileOperationGroup,'etsysFileCompliances':etsysFileCompliances,'etsysFileCompliance':etsysFileCompliance})