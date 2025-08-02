_AS='cdcNotificationGroup'
_AR='cdcFileXferGroup'
_AQ='cdcDataSelectionGroup'
_AP='cdcVFileGroup'
_AO='cdcFileXferComplete'
_AN='cdcVFileCollectionError'
_AM='cdcFileXferConfFailureEnable'
_AL='cdcFileXferConfSuccessEnable'
_AK='cdcFileXferConfRetryCount'
_AJ='cdcFileXferConfRetryPeriod'
_AI='cdcFileXferConfSecUrl'
_AH='cdcFileXferConfPriUrl'
_AG='cdcDGInstanceRowStatus'
_AF='cdcDGInstanceOtherPtr'
_AE='cdcDGInstanceNumRepititions'
_AD='cdcDGInstanceOidEnd'
_AC='cdcDGInstanceOid'
_AB='cdcDGInstanceType'
_AA='cdcDGBaseObjectRowStatus'
_A9='cdcDGBaseObjectList'
_A8='cdcDGBaseObjectSubtree'
_A7='cdcDGRowStatus'
_A6='cdcDGPollPeriod'
_A5='cdcDGInstGrpIndex'
_A4='cdcDGObjectGrpIndex'
_A3='cdcDGObject'
_A2='cdcDGContextName'
_A1='cdcDGTargetTag'
_A0='cdcDGVFileIndex'
_z='cdcDGType'
_y='cdcDGComment'
_x='cdcVFileCollectionErrorEnable'
_w='cdcVFileMgmtXferURL'
_v='cdcVFileMgmtCommand'
_u='cdcVFileMgmtTimeToLive'
_t='cdcVFileMgmtTimestamp'
_s='cdcVFileMgmtName'
_r='cdcVFileRowStatus'
_q='cdcVFileOperStatus'
_p='cdcVFileAdminStatus'
_o='cdcVFileRetentionPeriod'
_n='cdcVFileCollectionPeriod'
_m='cdcVFileCollectMode'
_l='cdcVFileFormat'
_k='cdcVFileCurrentSize'
_j='cdcVFileMaxSize'
_i='cdcVFileCommand'
_h='cdcVFileDescription'
_g='cdcVFileMaxSizeHitsLimit'
_f='cdcVFilePersistentStorage'
_e='cdcDGInstanceIndex'
_d='cdcDGInstanceGrpIndex'
_c='cdcDGBaseObjectIndex'
_b='cdcDGBaseObjectGrpIndex'
_a='cdcDGIndex'
_Z='CdcUrl'
_Y='cdcVFileMgmtIndex'
_X='disabled'
_W='enabled'
_V='CdcFileFormat'
_U='VariablePointer'
_T='RowPointer'
_S='DisplayString'
_R='SnmpTagValue'
_Q='cdcVFileMgmtLastXferURL'
_P='cdcVFileMgmtLastXferStatus'
_O='cdcVFileErrorCode'
_N='cdcVFileName'
_M='CdcRowInstanceId'
_L='read-write'
_K='cdcVFileIndex'
_J='TruthValue'
_I='SnmpAdminString'
_H='seconds'
_G='not-accessible'
_F='read-only'
_E='Integer32'
_D='Unsigned32'
_C='read-create'
_B='CISCO-DATA-COLLECTION-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_I)
SnmpTagValue,=mibBuilder.importSymbols('SNMP-TARGET-MIB',_R)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,zeroDotZero=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso','zeroDotZero')
DateAndTime,DisplayString,PhysAddress,RowPointer,RowStatus,TextualConvention,TruthValue,VariablePointer=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_S,'PhysAddress',_T,'RowStatus','TextualConvention',_J,_U)
ciscoDataCollectionMIB=ModuleIdentity((1,3,6,1,4,1,9,9,312))
if mibBuilder.loadTexts:ciscoDataCollectionMIB.setRevisions(('2002-10-30 05:30',))
class CdcCollectionSubtree(TextualConvention,ObjectIdentifier):status=_A
class CdcCollectionList(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
class CdcRowInstanceId(TextualConvention,ObjectIdentifier):status=_A
class CdcUrl(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
class CdcFileFormat(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('cdcBulkASCII',1),('cdcBulkBinary',2),('cdcSchemaASCII',3)))
class CdcFileXferStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('notStarted',1),('success',2),('aborted',3),('fileOpenFailRemote',4),('badDomainName',5),('unreachableIpAddress',6),('networkFailed',7),('fileWriteFailed',8),('authFailed',9)))
_CiscoDataCollMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoDataCollMIBNotifs=_CiscoDataCollMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,312,0))
_CiscoDataCollMIBObjects_ObjectIdentity=ObjectIdentity
ciscoDataCollMIBObjects=_CiscoDataCollMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,312,1))
_CdcVFile_ObjectIdentity=ObjectIdentity
cdcVFile=_CdcVFile_ObjectIdentity((1,3,6,1,4,1,9,9,312,1,1))
_CdcVFilePersistentStorage_Type=TruthValue
_CdcVFilePersistentStorage_Object=MibScalar
cdcVFilePersistentStorage=_CdcVFilePersistentStorage_Object((1,3,6,1,4,1,9,9,312,1,1,1),_CdcVFilePersistentStorage_Type())
cdcVFilePersistentStorage.setMaxAccess(_F)
if mibBuilder.loadTexts:cdcVFilePersistentStorage.setStatus(_A)
class _CdcVFileMaxSizeHitsLimit_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CdcVFileMaxSizeHitsLimit_Type.__name__=_D
_CdcVFileMaxSizeHitsLimit_Object=MibScalar
cdcVFileMaxSizeHitsLimit=_CdcVFileMaxSizeHitsLimit_Object((1,3,6,1,4,1,9,9,312,1,1,2),_CdcVFileMaxSizeHitsLimit_Type())
cdcVFileMaxSizeHitsLimit.setMaxAccess(_L)
if mibBuilder.loadTexts:cdcVFileMaxSizeHitsLimit.setStatus(_A)
_CdcVFileTable_Object=MibTable
cdcVFileTable=_CdcVFileTable_Object((1,3,6,1,4,1,9,9,312,1,1,3))
if mibBuilder.loadTexts:cdcVFileTable.setStatus(_A)
_CdcVFileEntry_Object=MibTableRow
cdcVFileEntry=_CdcVFileEntry_Object((1,3,6,1,4,1,9,9,312,1,1,3,1))
cdcVFileEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:cdcVFileEntry.setStatus(_A)
class _CdcVFileIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CdcVFileIndex_Type.__name__=_D
_CdcVFileIndex_Object=MibTableColumn
cdcVFileIndex=_CdcVFileIndex_Object((1,3,6,1,4,1,9,9,312,1,1,3,1,1),_CdcVFileIndex_Type())
cdcVFileIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:cdcVFileIndex.setStatus(_A)
class _CdcVFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CdcVFileName_Type.__name__=_S
_CdcVFileName_Object=MibTableColumn
cdcVFileName=_CdcVFileName_Object((1,3,6,1,4,1,9,9,312,1,1,3,1,2),_CdcVFileName_Type())
cdcVFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:cdcVFileName.setStatus(_A)
class _CdcVFileDescription_Type(SnmpAdminString):defaultHexValue=''
_CdcVFileDescription_Type.__name__=_I
_CdcVFileDescription_Object=MibTableColumn
cdcVFileDescription=_CdcVFileDescription_Object((1,3,6,1,4,1,9,9,312,1,1,3,1,3),_CdcVFileDescription_Type())
cdcVFileDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:cdcVFileDescription.setStatus(_A)
class _CdcVFileCommand_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('idle',1),('swapToNewFile',2),('collectNow',3)))
_CdcVFileCommand_Type.__name__=_E
_CdcVFileCommand_Object=MibTableColumn
cdcVFileCommand=_CdcVFileCommand_Object((1,3,6,1,4,1,9,9,312,1,1,3,1,4),_CdcVFileCommand_Type())
cdcVFileCommand.setMaxAccess(_C)
if mibBuilder.loadTexts:cdcVFileCommand.setStatus(_A)
class _CdcVFileMaxSize_Type(Unsigned32):defaultValue=50000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(512,4294967295))
_CdcVFileMaxSize_Type.__name__=_D
_CdcVFileMaxSize_Object=MibTableColumn
cdcVFileMaxSize=_CdcVFileMaxSize_Object((1,3,6,1,4,1,9,9,312,1,1,3,1,5),_CdcVFileMaxSize_Type())
cdcVFileMaxSize.setMaxAccess(_C)
if mibBuilder.loadTexts:cdcVFileMaxSize.setStatus(_A)
if mibBuilder.loadTexts:cdcVFileMaxSize.setUnits('bytes')
class _CdcVFileCurrentSize_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CdcVFileCurrentSize_Type.__name__=_D
_CdcVFileCurrentSize_Object=MibTableColumn
cdcVFileCurrentSize=_CdcVFileCurrentSize_Object((1,3,6,1,4,1,9,9,312,1,1,3,1,6),_CdcVFileCurrentSize_Type())
cdcVFileCurrentSize.setMaxAccess(_F)
if mibBuilder.loadTexts:cdcVFileCurrentSize.setStatus(_A)
if mibBuilder.loadTexts:cdcVFileCurrentSize.setUnits('bytes')
class _CdcVFileFormat_Type(CdcFileFormat):defaultValue=3
_CdcVFileFormat_Type.__name__=_V
_CdcVFileFormat_Object=MibTableColumn
cdcVFileFormat=_CdcVFileFormat_Object((1,3,6,1,4,1,9,9,312,1,1,3,1,7),_CdcVFileFormat_Type())
cdcVFileFormat.setMaxAccess(_C)
if mibBuilder.loadTexts:cdcVFileFormat.setStatus(_A)
class _CdcVFileCollectMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('auto',1),('manual',2)))
_CdcVFileCollectMode_Type.__name__=_E
_CdcVFileCollectMode_Object=MibTableColumn
cdcVFileCollectMode=_CdcVFileCollectMode_Object((1,3,6,1,4,1,9,9,312,1,1,3,1,8),_CdcVFileCollectMode_Type())
cdcVFileCollectMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cdcVFileCollectMode.setStatus(_A)
class _CdcVFileCollectionPeriod_Type(Unsigned32):defaultValue=1800;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,604800))
_CdcVFileCollectionPeriod_Type.__name__=_D
_CdcVFileCollectionPeriod_Object=MibTableColumn
cdcVFileCollectionPeriod=_CdcVFileCollectionPeriod_Object((1,3,6,1,4,1,9,9,312,1,1,3,1,9),_CdcVFileCollectionPeriod_Type())
cdcVFileCollectionPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:cdcVFileCollectionPeriod.setStatus(_A)
if mibBuilder.loadTexts:cdcVFileCollectionPeriod.setUnits(_H)
class _CdcVFileRetentionPeriod_Type(Unsigned32):defaultValue=1800;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,86400))
_CdcVFileRetentionPeriod_Type.__name__=_D
_CdcVFileRetentionPeriod_Object=MibTableColumn
cdcVFileRetentionPeriod=_CdcVFileRetentionPeriod_Object((1,3,6,1,4,1,9,9,312,1,1,3,1,10),_CdcVFileRetentionPeriod_Type())
cdcVFileRetentionPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:cdcVFileRetentionPeriod.setStatus(_A)
if mibBuilder.loadTexts:cdcVFileRetentionPeriod.setUnits(_H)
class _CdcVFileAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),(_X,2)))
_CdcVFileAdminStatus_Type.__name__=_E
_CdcVFileAdminStatus_Object=MibTableColumn
cdcVFileAdminStatus=_CdcVFileAdminStatus_Object((1,3,6,1,4,1,9,9,312,1,1,3,1,11),_CdcVFileAdminStatus_Type())
cdcVFileAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cdcVFileAdminStatus.setStatus(_A)
class _CdcVFileOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_W,1),(_X,2),('error',3)))
_CdcVFileOperStatus_Type.__name__=_E
_CdcVFileOperStatus_Object=MibTableColumn
cdcVFileOperStatus=_CdcVFileOperStatus_Object((1,3,6,1,4,1,9,9,312,1,1,3,1,12),_CdcVFileOperStatus_Type())
cdcVFileOperStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:cdcVFileOperStatus.setStatus(_A)
class _CdcVFileErrorCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('noError',1),('otherError',2),('noSpace',3),('openError',4),('tooSmallMaxSize',5),('tooManyMaxSizeHits',6),('noResource',7)))
_CdcVFileErrorCode_Type.__name__=_E
_CdcVFileErrorCode_Object=MibTableColumn
cdcVFileErrorCode=_CdcVFileErrorCode_Object((1,3,6,1,4,1,9,9,312,1,1,3,1,13),_CdcVFileErrorCode_Type())
cdcVFileErrorCode.setMaxAccess(_F)
if mibBuilder.loadTexts:cdcVFileErrorCode.setStatus(_A)
class _CdcVFileCollectionErrorEnable_Type(TruthValue):defaultValue=2
_CdcVFileCollectionErrorEnable_Type.__name__=_J
_CdcVFileCollectionErrorEnable_Object=MibTableColumn
cdcVFileCollectionErrorEnable=_CdcVFileCollectionErrorEnable_Object((1,3,6,1,4,1,9,9,312,1,1,3,1,14),_CdcVFileCollectionErrorEnable_Type())
cdcVFileCollectionErrorEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:cdcVFileCollectionErrorEnable.setStatus(_A)
_CdcVFileRowStatus_Type=RowStatus
_CdcVFileRowStatus_Object=MibTableColumn
cdcVFileRowStatus=_CdcVFileRowStatus_Object((1,3,6,1,4,1,9,9,312,1,1,3,1,15),_CdcVFileRowStatus_Type())
cdcVFileRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cdcVFileRowStatus.setStatus(_A)
_CdcVFileMgmtTable_Object=MibTable
cdcVFileMgmtTable=_CdcVFileMgmtTable_Object((1,3,6,1,4,1,9,9,312,1,1,4))
if mibBuilder.loadTexts:cdcVFileMgmtTable.setStatus(_A)
_CdcVFileMgmtEntry_Object=MibTableRow
cdcVFileMgmtEntry=_CdcVFileMgmtEntry_Object((1,3,6,1,4,1,9,9,312,1,1,4,1))
cdcVFileMgmtEntry.setIndexNames((0,_B,_K),(0,_B,_Y))
if mibBuilder.loadTexts:cdcVFileMgmtEntry.setStatus(_A)
class _CdcVFileMgmtIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CdcVFileMgmtIndex_Type.__name__=_D
_CdcVFileMgmtIndex_Object=MibTableColumn
cdcVFileMgmtIndex=_CdcVFileMgmtIndex_Object((1,3,6,1,4,1,9,9,312,1,1,4,1,1),_CdcVFileMgmtIndex_Type())
cdcVFileMgmtIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:cdcVFileMgmtIndex.setStatus(_A)
_CdcVFileMgmtName_Type=DisplayString
_CdcVFileMgmtName_Object=MibTableColumn
cdcVFileMgmtName=_CdcVFileMgmtName_Object((1,3,6,1,4,1,9,9,312,1,1,4,1,2),_CdcVFileMgmtName_Type())
cdcVFileMgmtName.setMaxAccess(_F)
if mibBuilder.loadTexts:cdcVFileMgmtName.setStatus(_A)
_CdcVFileMgmtTimestamp_Type=DateAndTime
_CdcVFileMgmtTimestamp_Object=MibTableColumn
cdcVFileMgmtTimestamp=_CdcVFileMgmtTimestamp_Object((1,3,6,1,4,1,9,9,312,1,1,4,1,3),_CdcVFileMgmtTimestamp_Type())
cdcVFileMgmtTimestamp.setMaxAccess(_F)
if mibBuilder.loadTexts:cdcVFileMgmtTimestamp.setStatus(_A)
class _CdcVFileMgmtTimeToLive_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,86400))
_CdcVFileMgmtTimeToLive_Type.__name__=_D
_CdcVFileMgmtTimeToLive_Object=MibTableColumn
cdcVFileMgmtTimeToLive=_CdcVFileMgmtTimeToLive_Object((1,3,6,1,4,1,9,9,312,1,1,4,1,4),_CdcVFileMgmtTimeToLive_Type())
cdcVFileMgmtTimeToLive.setMaxAccess(_F)
if mibBuilder.loadTexts:cdcVFileMgmtTimeToLive.setStatus(_A)
if mibBuilder.loadTexts:cdcVFileMgmtTimeToLive.setUnits(_H)
class _CdcVFileMgmtCommand_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('idle',1),('delete',2),('transfer',3),('abortTransfer',4)))
_CdcVFileMgmtCommand_Type.__name__=_E
_CdcVFileMgmtCommand_Object=MibTableColumn
cdcVFileMgmtCommand=_CdcVFileMgmtCommand_Object((1,3,6,1,4,1,9,9,312,1,1,4,1,5),_CdcVFileMgmtCommand_Type())
cdcVFileMgmtCommand.setMaxAccess(_L)
if mibBuilder.loadTexts:cdcVFileMgmtCommand.setStatus(_A)
class _CdcVFileMgmtXferURL_Type(CdcUrl):defaultValue=OctetString('')
_CdcVFileMgmtXferURL_Type.__name__=_Z
_CdcVFileMgmtXferURL_Object=MibTableColumn
cdcVFileMgmtXferURL=_CdcVFileMgmtXferURL_Object((1,3,6,1,4,1,9,9,312,1,1,4,1,6),_CdcVFileMgmtXferURL_Type())
cdcVFileMgmtXferURL.setMaxAccess(_L)
if mibBuilder.loadTexts:cdcVFileMgmtXferURL.setStatus(_A)
_CdcVFileMgmtLastXferStatus_Type=CdcFileXferStatus
_CdcVFileMgmtLastXferStatus_Object=MibTableColumn
cdcVFileMgmtLastXferStatus=_CdcVFileMgmtLastXferStatus_Object((1,3,6,1,4,1,9,9,312,1,1,4,1,7),_CdcVFileMgmtLastXferStatus_Type())
cdcVFileMgmtLastXferStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:cdcVFileMgmtLastXferStatus.setStatus(_A)
_CdcVFileMgmtLastXferURL_Type=CdcUrl
_CdcVFileMgmtLastXferURL_Object=MibTableColumn
cdcVFileMgmtLastXferURL=_CdcVFileMgmtLastXferURL_Object((1,3,6,1,4,1,9,9,312,1,1,4,1,8),_CdcVFileMgmtLastXferURL_Type())
cdcVFileMgmtLastXferURL.setMaxAccess(_F)
if mibBuilder.loadTexts:cdcVFileMgmtLastXferURL.setStatus(_A)
_CdcDataGroup_ObjectIdentity=ObjectIdentity
cdcDataGroup=_CdcDataGroup_ObjectIdentity((1,3,6,1,4,1,9,9,312,1,2))
_CdcDGTable_Object=MibTable
cdcDGTable=_CdcDGTable_Object((1,3,6,1,4,1,9,9,312,1,2,1))
if mibBuilder.loadTexts:cdcDGTable.setStatus(_A)
_CdcDGEntry_Object=MibTableRow
cdcDGEntry=_CdcDGEntry_Object((1,3,6,1,4,1,9,9,312,1,2,1,1))
cdcDGEntry.setIndexNames((0,_B,_a))
if mibBuilder.loadTexts:cdcDGEntry.setStatus(_A)
class _CdcDGIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CdcDGIndex_Type.__name__=_D
_CdcDGIndex_Object=MibTableColumn
cdcDGIndex=_CdcDGIndex_Object((1,3,6,1,4,1,9,9,312,1,2,1,1,1),_CdcDGIndex_Type())
cdcDGIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:cdcDGIndex.setStatus(_A)
class _CdcDGComment_Type(SnmpAdminString):defaultHexValue=''
_CdcDGComment_Type.__name__=_I
_CdcDGComment_Object=MibTableColumn
cdcDGComment=_CdcDGComment_Object((1,3,6,1,4,1,9,9,312,1,2,1,1,2),_CdcDGComment_Type())
cdcDGComment.setMaxAccess(_C)
if mibBuilder.loadTexts:cdcDGComment.setStatus(_A)
class _CdcDGType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('object',1),('table',2)))
_CdcDGType_Type.__name__=_E
_CdcDGType_Object=MibTableColumn
cdcDGType=_CdcDGType_Object((1,3,6,1,4,1,9,9,312,1,2,1,1,3),_CdcDGType_Type())
cdcDGType.setMaxAccess(_C)
if mibBuilder.loadTexts:cdcDGType.setStatus(_A)
class _CdcDGVFileIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CdcDGVFileIndex_Type.__name__=_D
_CdcDGVFileIndex_Object=MibTableColumn
cdcDGVFileIndex=_CdcDGVFileIndex_Object((1,3,6,1,4,1,9,9,312,1,2,1,1,4),_CdcDGVFileIndex_Type())
cdcDGVFileIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cdcDGVFileIndex.setStatus(_A)
class _CdcDGTargetTag_Type(SnmpTagValue):defaultHexValue=''
_CdcDGTargetTag_Type.__name__=_R
_CdcDGTargetTag_Object=MibTableColumn
cdcDGTargetTag=_CdcDGTargetTag_Object((1,3,6,1,4,1,9,9,312,1,2,1,1,5),_CdcDGTargetTag_Type())
cdcDGTargetTag.setMaxAccess(_C)
if mibBuilder.loadTexts:cdcDGTargetTag.setStatus(_A)
class _CdcDGContextName_Type(SnmpAdminString):defaultHexValue=''
_CdcDGContextName_Type.__name__=_I
_CdcDGContextName_Object=MibTableColumn
cdcDGContextName=_CdcDGContextName_Object((1,3,6,1,4,1,9,9,312,1,2,1,1,6),_CdcDGContextName_Type())
cdcDGContextName.setMaxAccess(_C)
if mibBuilder.loadTexts:cdcDGContextName.setStatus(_A)
class _CdcDGObject_Type(VariablePointer):defaultValue=0,0
_CdcDGObject_Type.__name__=_U
_CdcDGObject_Object=MibTableColumn
cdcDGObject=_CdcDGObject_Object((1,3,6,1,4,1,9,9,312,1,2,1,1,7),_CdcDGObject_Type())
cdcDGObject.setMaxAccess(_C)
if mibBuilder.loadTexts:cdcDGObject.setStatus(_A)
class _CdcDGObjectGrpIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CdcDGObjectGrpIndex_Type.__name__=_D
_CdcDGObjectGrpIndex_Object=MibTableColumn
cdcDGObjectGrpIndex=_CdcDGObjectGrpIndex_Object((1,3,6,1,4,1,9,9,312,1,2,1,1,8),_CdcDGObjectGrpIndex_Type())
cdcDGObjectGrpIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cdcDGObjectGrpIndex.setStatus(_A)
class _CdcDGInstGrpIndex_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CdcDGInstGrpIndex_Type.__name__=_D
_CdcDGInstGrpIndex_Object=MibTableColumn
cdcDGInstGrpIndex=_CdcDGInstGrpIndex_Object((1,3,6,1,4,1,9,9,312,1,2,1,1,9),_CdcDGInstGrpIndex_Type())
cdcDGInstGrpIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cdcDGInstGrpIndex.setStatus(_A)
class _CdcDGPollPeriod_Type(Unsigned32):defaultValue=600;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,86400))
_CdcDGPollPeriod_Type.__name__=_D
_CdcDGPollPeriod_Object=MibTableColumn
cdcDGPollPeriod=_CdcDGPollPeriod_Object((1,3,6,1,4,1,9,9,312,1,2,1,1,10),_CdcDGPollPeriod_Type())
cdcDGPollPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:cdcDGPollPeriod.setStatus(_A)
if mibBuilder.loadTexts:cdcDGPollPeriod.setUnits(_H)
_CdcDGRowStatus_Type=RowStatus
_CdcDGRowStatus_Object=MibTableColumn
cdcDGRowStatus=_CdcDGRowStatus_Object((1,3,6,1,4,1,9,9,312,1,2,1,1,11),_CdcDGRowStatus_Type())
cdcDGRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cdcDGRowStatus.setStatus(_A)
_CdcDGBaseObjectTable_Object=MibTable
cdcDGBaseObjectTable=_CdcDGBaseObjectTable_Object((1,3,6,1,4,1,9,9,312,1,2,2))
if mibBuilder.loadTexts:cdcDGBaseObjectTable.setStatus(_A)
_CdcDGBaseObjectEntry_Object=MibTableRow
cdcDGBaseObjectEntry=_CdcDGBaseObjectEntry_Object((1,3,6,1,4,1,9,9,312,1,2,2,1))
cdcDGBaseObjectEntry.setIndexNames((0,_B,_b),(0,_B,_c))
if mibBuilder.loadTexts:cdcDGBaseObjectEntry.setStatus(_A)
class _CdcDGBaseObjectGrpIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CdcDGBaseObjectGrpIndex_Type.__name__=_D
_CdcDGBaseObjectGrpIndex_Object=MibTableColumn
cdcDGBaseObjectGrpIndex=_CdcDGBaseObjectGrpIndex_Object((1,3,6,1,4,1,9,9,312,1,2,2,1,1),_CdcDGBaseObjectGrpIndex_Type())
cdcDGBaseObjectGrpIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:cdcDGBaseObjectGrpIndex.setStatus(_A)
class _CdcDGBaseObjectIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CdcDGBaseObjectIndex_Type.__name__=_D
_CdcDGBaseObjectIndex_Object=MibTableColumn
cdcDGBaseObjectIndex=_CdcDGBaseObjectIndex_Object((1,3,6,1,4,1,9,9,312,1,2,2,1,2),_CdcDGBaseObjectIndex_Type())
cdcDGBaseObjectIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:cdcDGBaseObjectIndex.setStatus(_A)
_CdcDGBaseObjectSubtree_Type=CdcCollectionSubtree
_CdcDGBaseObjectSubtree_Object=MibTableColumn
cdcDGBaseObjectSubtree=_CdcDGBaseObjectSubtree_Object((1,3,6,1,4,1,9,9,312,1,2,2,1,3),_CdcDGBaseObjectSubtree_Type())
cdcDGBaseObjectSubtree.setMaxAccess(_C)
if mibBuilder.loadTexts:cdcDGBaseObjectSubtree.setStatus(_A)
_CdcDGBaseObjectList_Type=CdcCollectionList
_CdcDGBaseObjectList_Object=MibTableColumn
cdcDGBaseObjectList=_CdcDGBaseObjectList_Object((1,3,6,1,4,1,9,9,312,1,2,2,1,4),_CdcDGBaseObjectList_Type())
cdcDGBaseObjectList.setMaxAccess(_C)
if mibBuilder.loadTexts:cdcDGBaseObjectList.setStatus(_A)
_CdcDGBaseObjectRowStatus_Type=RowStatus
_CdcDGBaseObjectRowStatus_Object=MibTableColumn
cdcDGBaseObjectRowStatus=_CdcDGBaseObjectRowStatus_Object((1,3,6,1,4,1,9,9,312,1,2,2,1,5),_CdcDGBaseObjectRowStatus_Type())
cdcDGBaseObjectRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cdcDGBaseObjectRowStatus.setStatus(_A)
_CdcDGInstanceTable_Object=MibTable
cdcDGInstanceTable=_CdcDGInstanceTable_Object((1,3,6,1,4,1,9,9,312,1,2,3))
if mibBuilder.loadTexts:cdcDGInstanceTable.setStatus(_A)
_CdcDGInstanceEntry_Object=MibTableRow
cdcDGInstanceEntry=_CdcDGInstanceEntry_Object((1,3,6,1,4,1,9,9,312,1,2,3,1))
cdcDGInstanceEntry.setIndexNames((0,_B,_d),(0,_B,_e))
if mibBuilder.loadTexts:cdcDGInstanceEntry.setStatus(_A)
class _CdcDGInstanceGrpIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CdcDGInstanceGrpIndex_Type.__name__=_D
_CdcDGInstanceGrpIndex_Object=MibTableColumn
cdcDGInstanceGrpIndex=_CdcDGInstanceGrpIndex_Object((1,3,6,1,4,1,9,9,312,1,2,3,1,1),_CdcDGInstanceGrpIndex_Type())
cdcDGInstanceGrpIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:cdcDGInstanceGrpIndex.setStatus(_A)
class _CdcDGInstanceIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CdcDGInstanceIndex_Type.__name__=_D
_CdcDGInstanceIndex_Object=MibTableColumn
cdcDGInstanceIndex=_CdcDGInstanceIndex_Object((1,3,6,1,4,1,9,9,312,1,2,3,1,2),_CdcDGInstanceIndex_Type())
cdcDGInstanceIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:cdcDGInstanceIndex.setStatus(_A)
class _CdcDGInstanceType_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('individual',1),('range',2),('repititions',3),('subTree',4),('other',5)))
_CdcDGInstanceType_Type.__name__=_E
_CdcDGInstanceType_Object=MibTableColumn
cdcDGInstanceType=_CdcDGInstanceType_Object((1,3,6,1,4,1,9,9,312,1,2,3,1,3),_CdcDGInstanceType_Type())
cdcDGInstanceType.setMaxAccess(_C)
if mibBuilder.loadTexts:cdcDGInstanceType.setStatus(_A)
class _CdcDGInstanceOid_Type(CdcRowInstanceId):defaultValue=0,0
_CdcDGInstanceOid_Type.__name__=_M
_CdcDGInstanceOid_Object=MibTableColumn
cdcDGInstanceOid=_CdcDGInstanceOid_Object((1,3,6,1,4,1,9,9,312,1,2,3,1,4),_CdcDGInstanceOid_Type())
cdcDGInstanceOid.setMaxAccess(_C)
if mibBuilder.loadTexts:cdcDGInstanceOid.setStatus(_A)
class _CdcDGInstanceOidEnd_Type(CdcRowInstanceId):defaultValue=0,0
_CdcDGInstanceOidEnd_Type.__name__=_M
_CdcDGInstanceOidEnd_Object=MibTableColumn
cdcDGInstanceOidEnd=_CdcDGInstanceOidEnd_Object((1,3,6,1,4,1,9,9,312,1,2,3,1,5),_CdcDGInstanceOidEnd_Type())
cdcDGInstanceOidEnd.setMaxAccess(_C)
if mibBuilder.loadTexts:cdcDGInstanceOidEnd.setStatus(_A)
class _CdcDGInstanceNumRepititions_Type(Unsigned32):defaultValue=1
_CdcDGInstanceNumRepititions_Type.__name__=_D
_CdcDGInstanceNumRepititions_Object=MibTableColumn
cdcDGInstanceNumRepititions=_CdcDGInstanceNumRepititions_Object((1,3,6,1,4,1,9,9,312,1,2,3,1,6),_CdcDGInstanceNumRepititions_Type())
cdcDGInstanceNumRepititions.setMaxAccess(_C)
if mibBuilder.loadTexts:cdcDGInstanceNumRepititions.setStatus(_A)
class _CdcDGInstanceOtherPtr_Type(RowPointer):defaultValue=0,0
_CdcDGInstanceOtherPtr_Type.__name__=_T
_CdcDGInstanceOtherPtr_Object=MibTableColumn
cdcDGInstanceOtherPtr=_CdcDGInstanceOtherPtr_Object((1,3,6,1,4,1,9,9,312,1,2,3,1,7),_CdcDGInstanceOtherPtr_Type())
cdcDGInstanceOtherPtr.setMaxAccess(_C)
if mibBuilder.loadTexts:cdcDGInstanceOtherPtr.setStatus(_A)
_CdcDGInstanceRowStatus_Type=RowStatus
_CdcDGInstanceRowStatus_Object=MibTableColumn
cdcDGInstanceRowStatus=_CdcDGInstanceRowStatus_Object((1,3,6,1,4,1,9,9,312,1,2,3,1,8),_CdcDGInstanceRowStatus_Type())
cdcDGInstanceRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cdcDGInstanceRowStatus.setStatus(_A)
_CdcFileXfer_ObjectIdentity=ObjectIdentity
cdcFileXfer=_CdcFileXfer_ObjectIdentity((1,3,6,1,4,1,9,9,312,1,3))
_CdcFileXferConfTable_Object=MibTable
cdcFileXferConfTable=_CdcFileXferConfTable_Object((1,3,6,1,4,1,9,9,312,1,3,1))
if mibBuilder.loadTexts:cdcFileXferConfTable.setStatus(_A)
_CdcFileXferConfEntry_Object=MibTableRow
cdcFileXferConfEntry=_CdcFileXferConfEntry_Object((1,3,6,1,4,1,9,9,312,1,3,1,1))
cdcFileXferConfEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:cdcFileXferConfEntry.setStatus(_A)
_CdcFileXferConfPriUrl_Type=CdcUrl
_CdcFileXferConfPriUrl_Object=MibTableColumn
cdcFileXferConfPriUrl=_CdcFileXferConfPriUrl_Object((1,3,6,1,4,1,9,9,312,1,3,1,1,1),_CdcFileXferConfPriUrl_Type())
cdcFileXferConfPriUrl.setMaxAccess(_C)
if mibBuilder.loadTexts:cdcFileXferConfPriUrl.setStatus(_A)
_CdcFileXferConfSecUrl_Type=CdcUrl
_CdcFileXferConfSecUrl_Object=MibTableColumn
cdcFileXferConfSecUrl=_CdcFileXferConfSecUrl_Object((1,3,6,1,4,1,9,9,312,1,3,1,1,2),_CdcFileXferConfSecUrl_Type())
cdcFileXferConfSecUrl.setMaxAccess(_C)
if mibBuilder.loadTexts:cdcFileXferConfSecUrl.setStatus(_A)
class _CdcFileXferConfRetryPeriod_Type(Unsigned32):defaultValue=300;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,86400))
_CdcFileXferConfRetryPeriod_Type.__name__=_D
_CdcFileXferConfRetryPeriod_Object=MibTableColumn
cdcFileXferConfRetryPeriod=_CdcFileXferConfRetryPeriod_Object((1,3,6,1,4,1,9,9,312,1,3,1,1,3),_CdcFileXferConfRetryPeriod_Type())
cdcFileXferConfRetryPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:cdcFileXferConfRetryPeriod.setStatus(_A)
if mibBuilder.loadTexts:cdcFileXferConfRetryPeriod.setUnits(_H)
class _CdcFileXferConfRetryCount_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_CdcFileXferConfRetryCount_Type.__name__=_D
_CdcFileXferConfRetryCount_Object=MibTableColumn
cdcFileXferConfRetryCount=_CdcFileXferConfRetryCount_Object((1,3,6,1,4,1,9,9,312,1,3,1,1,4),_CdcFileXferConfRetryCount_Type())
cdcFileXferConfRetryCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cdcFileXferConfRetryCount.setStatus(_A)
if mibBuilder.loadTexts:cdcFileXferConfRetryCount.setUnits(_H)
class _CdcFileXferConfSuccessEnable_Type(TruthValue):defaultValue=2
_CdcFileXferConfSuccessEnable_Type.__name__=_J
_CdcFileXferConfSuccessEnable_Object=MibTableColumn
cdcFileXferConfSuccessEnable=_CdcFileXferConfSuccessEnable_Object((1,3,6,1,4,1,9,9,312,1,3,1,1,5),_CdcFileXferConfSuccessEnable_Type())
cdcFileXferConfSuccessEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:cdcFileXferConfSuccessEnable.setStatus(_A)
class _CdcFileXferConfFailureEnable_Type(TruthValue):defaultValue=1
_CdcFileXferConfFailureEnable_Type.__name__=_J
_CdcFileXferConfFailureEnable_Object=MibTableColumn
cdcFileXferConfFailureEnable=_CdcFileXferConfFailureEnable_Object((1,3,6,1,4,1,9,9,312,1,3,1,1,6),_CdcFileXferConfFailureEnable_Type())
cdcFileXferConfFailureEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:cdcFileXferConfFailureEnable.setStatus(_A)
_CiscoDataCollMIBConformance_ObjectIdentity=ObjectIdentity
ciscoDataCollMIBConformance=_CiscoDataCollMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,312,2))
_CiscoDataCollMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoDataCollMIBCompliances=_CiscoDataCollMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,312,2,1))
_CiscoDataCollMIBGroups_ObjectIdentity=ObjectIdentity
ciscoDataCollMIBGroups=_CiscoDataCollMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,312,2,2))
cdcVFileGroup=ObjectGroup((1,3,6,1,4,1,9,9,312,2,2,1))
cdcVFileGroup.setObjects(*((_B,_f),(_B,_g),(_B,_N),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_O),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_P),(_B,_Q),(_B,_x)))
if mibBuilder.loadTexts:cdcVFileGroup.setStatus(_A)
cdcDataSelectionGroup=ObjectGroup((1,3,6,1,4,1,9,9,312,2,2,2))
cdcDataSelectionGroup.setObjects(*((_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG)))
if mibBuilder.loadTexts:cdcDataSelectionGroup.setStatus(_A)
cdcFileXferGroup=ObjectGroup((1,3,6,1,4,1,9,9,312,2,2,3))
cdcFileXferGroup.setObjects(*((_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM)))
if mibBuilder.loadTexts:cdcFileXferGroup.setStatus(_A)
cdcVFileCollectionError=NotificationType((1,3,6,1,4,1,9,9,312,0,1))
cdcVFileCollectionError.setObjects(*((_B,_N),(_B,_O)))
if mibBuilder.loadTexts:cdcVFileCollectionError.setStatus(_A)
cdcFileXferComplete=NotificationType((1,3,6,1,4,1,9,9,312,0,2))
cdcFileXferComplete.setObjects(*((_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:cdcFileXferComplete.setStatus(_A)
cdcNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,312,2,2,4))
cdcNotificationGroup.setObjects(*((_B,_AN),(_B,_AO)))
if mibBuilder.loadTexts:cdcNotificationGroup.setStatus(_A)
ciscoDataCollMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,312,2,1,1))
ciscoDataCollMIBCompliance.setObjects(*((_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS)))
if mibBuilder.loadTexts:ciscoDataCollMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CdcCollectionSubtree':CdcCollectionSubtree,'CdcCollectionList':CdcCollectionList,_M:CdcRowInstanceId,_Z:CdcUrl,_V:CdcFileFormat,'CdcFileXferStatus':CdcFileXferStatus,'ciscoDataCollectionMIB':ciscoDataCollectionMIB,'ciscoDataCollMIBNotifs':ciscoDataCollMIBNotifs,_AN:cdcVFileCollectionError,_AO:cdcFileXferComplete,'ciscoDataCollMIBObjects':ciscoDataCollMIBObjects,'cdcVFile':cdcVFile,_f:cdcVFilePersistentStorage,_g:cdcVFileMaxSizeHitsLimit,'cdcVFileTable':cdcVFileTable,'cdcVFileEntry':cdcVFileEntry,_K:cdcVFileIndex,_N:cdcVFileName,_h:cdcVFileDescription,_i:cdcVFileCommand,_j:cdcVFileMaxSize,_k:cdcVFileCurrentSize,_l:cdcVFileFormat,_m:cdcVFileCollectMode,_n:cdcVFileCollectionPeriod,_o:cdcVFileRetentionPeriod,_p:cdcVFileAdminStatus,_q:cdcVFileOperStatus,_O:cdcVFileErrorCode,_x:cdcVFileCollectionErrorEnable,_r:cdcVFileRowStatus,'cdcVFileMgmtTable':cdcVFileMgmtTable,'cdcVFileMgmtEntry':cdcVFileMgmtEntry,_Y:cdcVFileMgmtIndex,_s:cdcVFileMgmtName,_t:cdcVFileMgmtTimestamp,_u:cdcVFileMgmtTimeToLive,_v:cdcVFileMgmtCommand,_w:cdcVFileMgmtXferURL,_P:cdcVFileMgmtLastXferStatus,_Q:cdcVFileMgmtLastXferURL,'cdcDataGroup':cdcDataGroup,'cdcDGTable':cdcDGTable,'cdcDGEntry':cdcDGEntry,_a:cdcDGIndex,_y:cdcDGComment,_z:cdcDGType,_A0:cdcDGVFileIndex,_A1:cdcDGTargetTag,_A2:cdcDGContextName,_A3:cdcDGObject,_A4:cdcDGObjectGrpIndex,_A5:cdcDGInstGrpIndex,_A6:cdcDGPollPeriod,_A7:cdcDGRowStatus,'cdcDGBaseObjectTable':cdcDGBaseObjectTable,'cdcDGBaseObjectEntry':cdcDGBaseObjectEntry,_b:cdcDGBaseObjectGrpIndex,_c:cdcDGBaseObjectIndex,_A8:cdcDGBaseObjectSubtree,_A9:cdcDGBaseObjectList,_AA:cdcDGBaseObjectRowStatus,'cdcDGInstanceTable':cdcDGInstanceTable,'cdcDGInstanceEntry':cdcDGInstanceEntry,_d:cdcDGInstanceGrpIndex,_e:cdcDGInstanceIndex,_AB:cdcDGInstanceType,_AC:cdcDGInstanceOid,_AD:cdcDGInstanceOidEnd,_AE:cdcDGInstanceNumRepititions,_AF:cdcDGInstanceOtherPtr,_AG:cdcDGInstanceRowStatus,'cdcFileXfer':cdcFileXfer,'cdcFileXferConfTable':cdcFileXferConfTable,'cdcFileXferConfEntry':cdcFileXferConfEntry,_AH:cdcFileXferConfPriUrl,_AI:cdcFileXferConfSecUrl,_AJ:cdcFileXferConfRetryPeriod,_AK:cdcFileXferConfRetryCount,_AL:cdcFileXferConfSuccessEnable,_AM:cdcFileXferConfFailureEnable,'ciscoDataCollMIBConformance':ciscoDataCollMIBConformance,'ciscoDataCollMIBCompliances':ciscoDataCollMIBCompliances,'ciscoDataCollMIBCompliance':ciscoDataCollMIBCompliance,'ciscoDataCollMIBGroups':ciscoDataCollMIBGroups,_AP:cdcVFileGroup,_AQ:cdcDataSelectionGroup,_AR:cdcFileXferGroup,_AS:cdcNotificationGroup})