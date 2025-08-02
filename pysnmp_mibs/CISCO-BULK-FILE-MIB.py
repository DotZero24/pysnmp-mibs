_v='ciscoBulkFileDefineGroupRev1'
_u='ciscoBulkFileDefineGroup'
_t='cbfDefineFileCompletion'
_s='cbfDefineObjectLastPolledInst'
_r='cbfDefineObjectNumEntries'
_q='cbfDefineObjectTableInstance'
_p='cbfStatusFileEntryStatus'
_o='cbfStatusFilesBumped'
_n='cbfStatusHighFiles'
_m='cbfStatusFiles'
_l='cbfStatusMaxFiles'
_k='deprecated'
_j='cbfStatusFileIndex'
_i='cbfDefineObjectIndex'
_h='running'
_g='TruthValue'
_f='DisplayString'
_e='ciscoBulkFileNotiGroup'
_d='ciscoBulkFileStatusGroup'
_c='cbfStatusFileCompletionTime'
_b='cbfStatusFileState'
_a='cbfDefineObjectEntryStatus'
_Z='cbfDefineObjectID'
_Y='cbfDefineObjectClass'
_X='cbfDefineFileNotifyOnCompletion'
_W='cbfDefineFileEntryStatus'
_V='cbfDefineFileNow'
_U='cbfDefineFileFormat'
_T='cbfDefineFileStorage'
_S='cbfDefineFileName'
_R='cbfDefineObjectsRefused'
_Q='cbfDefineHighObjects'
_P='cbfDefineObjects'
_O='cbfDefineMaxObjects'
_N='cbfDefineFilesRefused'
_M='cbfDefineHighFiles'
_L='cbfDefineFiles'
_K='cbfDefineMaxFiles'
_J='not-accessible'
_I='ObjectIdentifier'
_H='cbfDefineFileIndex'
_G='read-write'
_F='Integer32'
_E='Unsigned32'
_D='read-create'
_C='read-only'
_B='current'
_A='CISCO-BULK-FILE-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString',_I)
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,zeroDotZero=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso','zeroDotZero')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_f,'PhysAddress','RowStatus','TextualConvention','TimeStamp',_g)
ciscoBulkFileMIB=ModuleIdentity((1,3,6,1,4,1,9,9,81))
if mibBuilder.loadTexts:ciscoBulkFileMIB.setRevisions(('2002-06-10 00:00','2002-05-15 00:00','2001-08-22 00:00','2001-08-01 00:00','2001-06-26 17:00','1998-10-29 17:00'))
_CiscoBulkFileMIBObjects_ObjectIdentity=ObjectIdentity
ciscoBulkFileMIBObjects=_CiscoBulkFileMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,81,1))
_CbfDefine_ObjectIdentity=ObjectIdentity
cbfDefine=_CbfDefine_ObjectIdentity((1,3,6,1,4,1,9,9,81,1,1))
class _CbfDefineMaxFiles_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CbfDefineMaxFiles_Type.__name__=_E
_CbfDefineMaxFiles_Object=MibScalar
cbfDefineMaxFiles=_CbfDefineMaxFiles_Object((1,3,6,1,4,1,9,9,81,1,1,1),_CbfDefineMaxFiles_Type())
cbfDefineMaxFiles.setMaxAccess(_G)
if mibBuilder.loadTexts:cbfDefineMaxFiles.setStatus(_B)
_CbfDefineFiles_Type=Gauge32
_CbfDefineFiles_Object=MibScalar
cbfDefineFiles=_CbfDefineFiles_Object((1,3,6,1,4,1,9,9,81,1,1,2),_CbfDefineFiles_Type())
cbfDefineFiles.setMaxAccess(_C)
if mibBuilder.loadTexts:cbfDefineFiles.setStatus(_B)
_CbfDefineHighFiles_Type=Gauge32
_CbfDefineHighFiles_Object=MibScalar
cbfDefineHighFiles=_CbfDefineHighFiles_Object((1,3,6,1,4,1,9,9,81,1,1,3),_CbfDefineHighFiles_Type())
cbfDefineHighFiles.setMaxAccess(_C)
if mibBuilder.loadTexts:cbfDefineHighFiles.setStatus(_B)
_CbfDefineFilesRefused_Type=Counter32
_CbfDefineFilesRefused_Object=MibScalar
cbfDefineFilesRefused=_CbfDefineFilesRefused_Object((1,3,6,1,4,1,9,9,81,1,1,4),_CbfDefineFilesRefused_Type())
cbfDefineFilesRefused.setMaxAccess(_C)
if mibBuilder.loadTexts:cbfDefineFilesRefused.setStatus(_B)
class _CbfDefineMaxObjects_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CbfDefineMaxObjects_Type.__name__=_E
_CbfDefineMaxObjects_Object=MibScalar
cbfDefineMaxObjects=_CbfDefineMaxObjects_Object((1,3,6,1,4,1,9,9,81,1,1,5),_CbfDefineMaxObjects_Type())
cbfDefineMaxObjects.setMaxAccess(_G)
if mibBuilder.loadTexts:cbfDefineMaxObjects.setStatus(_B)
_CbfDefineObjects_Type=Gauge32
_CbfDefineObjects_Object=MibScalar
cbfDefineObjects=_CbfDefineObjects_Object((1,3,6,1,4,1,9,9,81,1,1,6),_CbfDefineObjects_Type())
cbfDefineObjects.setMaxAccess(_C)
if mibBuilder.loadTexts:cbfDefineObjects.setStatus(_B)
_CbfDefineHighObjects_Type=Gauge32
_CbfDefineHighObjects_Object=MibScalar
cbfDefineHighObjects=_CbfDefineHighObjects_Object((1,3,6,1,4,1,9,9,81,1,1,7),_CbfDefineHighObjects_Type())
cbfDefineHighObjects.setMaxAccess(_C)
if mibBuilder.loadTexts:cbfDefineHighObjects.setStatus(_B)
_CbfDefineObjectsRefused_Type=Counter32
_CbfDefineObjectsRefused_Object=MibScalar
cbfDefineObjectsRefused=_CbfDefineObjectsRefused_Object((1,3,6,1,4,1,9,9,81,1,1,8),_CbfDefineObjectsRefused_Type())
cbfDefineObjectsRefused.setMaxAccess(_C)
if mibBuilder.loadTexts:cbfDefineObjectsRefused.setStatus(_B)
_CbfDefineFileTable_Object=MibTable
cbfDefineFileTable=_CbfDefineFileTable_Object((1,3,6,1,4,1,9,9,81,1,1,9))
if mibBuilder.loadTexts:cbfDefineFileTable.setStatus(_B)
_CbfDefineFileEntry_Object=MibTableRow
cbfDefineFileEntry=_CbfDefineFileEntry_Object((1,3,6,1,4,1,9,9,81,1,1,9,1))
cbfDefineFileEntry.setIndexNames((0,_A,_H))
if mibBuilder.loadTexts:cbfDefineFileEntry.setStatus(_B)
class _CbfDefineFileIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CbfDefineFileIndex_Type.__name__=_E
_CbfDefineFileIndex_Object=MibTableColumn
cbfDefineFileIndex=_CbfDefineFileIndex_Object((1,3,6,1,4,1,9,9,81,1,1,9,1,1),_CbfDefineFileIndex_Type())
cbfDefineFileIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:cbfDefineFileIndex.setStatus(_B)
class _CbfDefineFileName_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CbfDefineFileName_Type.__name__=_f
_CbfDefineFileName_Object=MibTableColumn
cbfDefineFileName=_CbfDefineFileName_Object((1,3,6,1,4,1,9,9,81,1,1,9,1,2),_CbfDefineFileName_Type())
cbfDefineFileName.setMaxAccess(_D)
if mibBuilder.loadTexts:cbfDefineFileName.setStatus(_B)
class _CbfDefineFileStorage_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ephemeral',1),('volatile',2),('permanent',3)))
_CbfDefineFileStorage_Type.__name__=_F
_CbfDefineFileStorage_Object=MibTableColumn
cbfDefineFileStorage=_CbfDefineFileStorage_Object((1,3,6,1,4,1,9,9,81,1,1,9,1,3),_CbfDefineFileStorage_Type())
cbfDefineFileStorage.setMaxAccess(_D)
if mibBuilder.loadTexts:cbfDefineFileStorage.setStatus(_B)
class _CbfDefineFileFormat_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('standardBER',1),('bulkBinary',2),('bulkASCII',3),('variantBERWithCksum',4),('variantBinWithCksum',5)))
_CbfDefineFileFormat_Type.__name__=_F
_CbfDefineFileFormat_Object=MibTableColumn
cbfDefineFileFormat=_CbfDefineFileFormat_Object((1,3,6,1,4,1,9,9,81,1,1,9,1,4),_CbfDefineFileFormat_Type())
cbfDefineFileFormat.setMaxAccess(_D)
if mibBuilder.loadTexts:cbfDefineFileFormat.setStatus(_B)
class _CbfDefineFileNow_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('notActive',1),('ready',2),('create',3),(_h,4),('forcedCreate',5)))
_CbfDefineFileNow_Type.__name__=_F
_CbfDefineFileNow_Object=MibTableColumn
cbfDefineFileNow=_CbfDefineFileNow_Object((1,3,6,1,4,1,9,9,81,1,1,9,1,5),_CbfDefineFileNow_Type())
cbfDefineFileNow.setMaxAccess(_D)
if mibBuilder.loadTexts:cbfDefineFileNow.setStatus(_B)
_CbfDefineFileEntryStatus_Type=RowStatus
_CbfDefineFileEntryStatus_Object=MibTableColumn
cbfDefineFileEntryStatus=_CbfDefineFileEntryStatus_Object((1,3,6,1,4,1,9,9,81,1,1,9,1,6),_CbfDefineFileEntryStatus_Type())
cbfDefineFileEntryStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cbfDefineFileEntryStatus.setStatus(_B)
class _CbfDefineFileNotifyOnCompletion_Type(TruthValue):defaultValue=2
_CbfDefineFileNotifyOnCompletion_Type.__name__=_g
_CbfDefineFileNotifyOnCompletion_Object=MibTableColumn
cbfDefineFileNotifyOnCompletion=_CbfDefineFileNotifyOnCompletion_Object((1,3,6,1,4,1,9,9,81,1,1,9,1,7),_CbfDefineFileNotifyOnCompletion_Type())
cbfDefineFileNotifyOnCompletion.setMaxAccess(_D)
if mibBuilder.loadTexts:cbfDefineFileNotifyOnCompletion.setStatus(_B)
_CbfDefineObjectTable_Object=MibTable
cbfDefineObjectTable=_CbfDefineObjectTable_Object((1,3,6,1,4,1,9,9,81,1,1,10))
if mibBuilder.loadTexts:cbfDefineObjectTable.setStatus(_B)
_CbfDefineObjectEntry_Object=MibTableRow
cbfDefineObjectEntry=_CbfDefineObjectEntry_Object((1,3,6,1,4,1,9,9,81,1,1,10,1))
cbfDefineObjectEntry.setIndexNames((0,_A,_H),(0,_A,_i))
if mibBuilder.loadTexts:cbfDefineObjectEntry.setStatus(_B)
class _CbfDefineObjectIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CbfDefineObjectIndex_Type.__name__=_E
_CbfDefineObjectIndex_Object=MibTableColumn
cbfDefineObjectIndex=_CbfDefineObjectIndex_Object((1,3,6,1,4,1,9,9,81,1,1,10,1,1),_CbfDefineObjectIndex_Type())
cbfDefineObjectIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:cbfDefineObjectIndex.setStatus(_B)
class _CbfDefineObjectClass_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('object',1),('lexicalTable',2),('leastCpuTable',3)))
_CbfDefineObjectClass_Type.__name__=_F
_CbfDefineObjectClass_Object=MibTableColumn
cbfDefineObjectClass=_CbfDefineObjectClass_Object((1,3,6,1,4,1,9,9,81,1,1,10,1,2),_CbfDefineObjectClass_Type())
cbfDefineObjectClass.setMaxAccess(_D)
if mibBuilder.loadTexts:cbfDefineObjectClass.setStatus(_B)
class _CbfDefineObjectID_Type(ObjectIdentifier):defaultValue=0,0
_CbfDefineObjectID_Type.__name__=_I
_CbfDefineObjectID_Object=MibTableColumn
cbfDefineObjectID=_CbfDefineObjectID_Object((1,3,6,1,4,1,9,9,81,1,1,10,1,3),_CbfDefineObjectID_Type())
cbfDefineObjectID.setMaxAccess(_D)
if mibBuilder.loadTexts:cbfDefineObjectID.setStatus(_B)
_CbfDefineObjectEntryStatus_Type=RowStatus
_CbfDefineObjectEntryStatus_Object=MibTableColumn
cbfDefineObjectEntryStatus=_CbfDefineObjectEntryStatus_Object((1,3,6,1,4,1,9,9,81,1,1,10,1,4),_CbfDefineObjectEntryStatus_Type())
cbfDefineObjectEntryStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cbfDefineObjectEntryStatus.setStatus(_B)
class _CbfDefineObjectTableInstance_Type(ObjectIdentifier):defaultValue=0,0
_CbfDefineObjectTableInstance_Type.__name__=_I
_CbfDefineObjectTableInstance_Object=MibTableColumn
cbfDefineObjectTableInstance=_CbfDefineObjectTableInstance_Object((1,3,6,1,4,1,9,9,81,1,1,10,1,5),_CbfDefineObjectTableInstance_Type())
cbfDefineObjectTableInstance.setMaxAccess(_D)
if mibBuilder.loadTexts:cbfDefineObjectTableInstance.setStatus(_B)
class _CbfDefineObjectNumEntries_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CbfDefineObjectNumEntries_Type.__name__=_E
_CbfDefineObjectNumEntries_Object=MibTableColumn
cbfDefineObjectNumEntries=_CbfDefineObjectNumEntries_Object((1,3,6,1,4,1,9,9,81,1,1,10,1,6),_CbfDefineObjectNumEntries_Type())
cbfDefineObjectNumEntries.setMaxAccess(_D)
if mibBuilder.loadTexts:cbfDefineObjectNumEntries.setStatus(_B)
_CbfDefineObjectLastPolledInst_Type=ObjectIdentifier
_CbfDefineObjectLastPolledInst_Object=MibTableColumn
cbfDefineObjectLastPolledInst=_CbfDefineObjectLastPolledInst_Object((1,3,6,1,4,1,9,9,81,1,1,10,1,7),_CbfDefineObjectLastPolledInst_Type())
cbfDefineObjectLastPolledInst.setMaxAccess(_C)
if mibBuilder.loadTexts:cbfDefineObjectLastPolledInst.setStatus(_B)
_CbfStatus_ObjectIdentity=ObjectIdentity
cbfStatus=_CbfStatus_ObjectIdentity((1,3,6,1,4,1,9,9,81,1,2))
class _CbfStatusMaxFiles_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CbfStatusMaxFiles_Type.__name__=_E
_CbfStatusMaxFiles_Object=MibScalar
cbfStatusMaxFiles=_CbfStatusMaxFiles_Object((1,3,6,1,4,1,9,9,81,1,2,1),_CbfStatusMaxFiles_Type())
cbfStatusMaxFiles.setMaxAccess(_G)
if mibBuilder.loadTexts:cbfStatusMaxFiles.setStatus(_B)
_CbfStatusFiles_Type=Gauge32
_CbfStatusFiles_Object=MibScalar
cbfStatusFiles=_CbfStatusFiles_Object((1,3,6,1,4,1,9,9,81,1,2,2),_CbfStatusFiles_Type())
cbfStatusFiles.setMaxAccess(_C)
if mibBuilder.loadTexts:cbfStatusFiles.setStatus(_B)
_CbfStatusHighFiles_Type=Gauge32
_CbfStatusHighFiles_Object=MibScalar
cbfStatusHighFiles=_CbfStatusHighFiles_Object((1,3,6,1,4,1,9,9,81,1,2,3),_CbfStatusHighFiles_Type())
cbfStatusHighFiles.setMaxAccess(_C)
if mibBuilder.loadTexts:cbfStatusHighFiles.setStatus(_B)
_CbfStatusFilesBumped_Type=Counter32
_CbfStatusFilesBumped_Object=MibScalar
cbfStatusFilesBumped=_CbfStatusFilesBumped_Object((1,3,6,1,4,1,9,9,81,1,2,4),_CbfStatusFilesBumped_Type())
cbfStatusFilesBumped.setMaxAccess(_C)
if mibBuilder.loadTexts:cbfStatusFilesBumped.setStatus(_B)
_CbfStatusFileTable_Object=MibTable
cbfStatusFileTable=_CbfStatusFileTable_Object((1,3,6,1,4,1,9,9,81,1,2,5))
if mibBuilder.loadTexts:cbfStatusFileTable.setStatus(_B)
_CbfStatusFileEntry_Object=MibTableRow
cbfStatusFileEntry=_CbfStatusFileEntry_Object((1,3,6,1,4,1,9,9,81,1,2,5,1))
cbfStatusFileEntry.setIndexNames((0,_A,_H),(0,_A,_j))
if mibBuilder.loadTexts:cbfStatusFileEntry.setStatus(_B)
class _CbfStatusFileIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CbfStatusFileIndex_Type.__name__=_E
_CbfStatusFileIndex_Object=MibTableColumn
cbfStatusFileIndex=_CbfStatusFileIndex_Object((1,3,6,1,4,1,9,9,81,1,2,5,1,1),_CbfStatusFileIndex_Type())
cbfStatusFileIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:cbfStatusFileIndex.setStatus(_B)
class _CbfStatusFileState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_h,1),('ready',2),('emptied',3),('noSpace',4),('badName',5),('writeErr',6),('noMem',7),('buffErr',8),('aborted',9)))
_CbfStatusFileState_Type.__name__=_F
_CbfStatusFileState_Object=MibTableColumn
cbfStatusFileState=_CbfStatusFileState_Object((1,3,6,1,4,1,9,9,81,1,2,5,1,2),_CbfStatusFileState_Type())
cbfStatusFileState.setMaxAccess(_C)
if mibBuilder.loadTexts:cbfStatusFileState.setStatus(_B)
_CbfStatusFileCompletionTime_Type=TimeStamp
_CbfStatusFileCompletionTime_Object=MibTableColumn
cbfStatusFileCompletionTime=_CbfStatusFileCompletionTime_Object((1,3,6,1,4,1,9,9,81,1,2,5,1,3),_CbfStatusFileCompletionTime_Type())
cbfStatusFileCompletionTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cbfStatusFileCompletionTime.setStatus(_B)
_CbfStatusFileEntryStatus_Type=RowStatus
_CbfStatusFileEntryStatus_Object=MibTableColumn
cbfStatusFileEntryStatus=_CbfStatusFileEntryStatus_Object((1,3,6,1,4,1,9,9,81,1,2,5,1,4),_CbfStatusFileEntryStatus_Type())
cbfStatusFileEntryStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:cbfStatusFileEntryStatus.setStatus(_B)
_CiscoBulkFileMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
ciscoBulkFileMIBNotificationPrefix=_CiscoBulkFileMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,81,2))
_CiscoBulkFileMIBNotifications_ObjectIdentity=ObjectIdentity
ciscoBulkFileMIBNotifications=_CiscoBulkFileMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,81,2,0))
_CiscoBulkFileMIBConformance_ObjectIdentity=ObjectIdentity
ciscoBulkFileMIBConformance=_CiscoBulkFileMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,81,3))
_CiscoBulkFileMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoBulkFileMIBCompliances=_CiscoBulkFileMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,81,3,1))
_CiscoBulkFileMIBGroups_ObjectIdentity=ObjectIdentity
ciscoBulkFileMIBGroups=_CiscoBulkFileMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,81,3,2))
ciscoBulkFileDefineGroup=ObjectGroup((1,3,6,1,4,1,9,9,81,3,2,1))
ciscoBulkFileDefineGroup.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:ciscoBulkFileDefineGroup.setStatus(_k)
ciscoBulkFileStatusGroup=ObjectGroup((1,3,6,1,4,1,9,9,81,3,2,2))
ciscoBulkFileStatusGroup.setObjects(*((_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_b),(_A,_c),(_A,_p)))
if mibBuilder.loadTexts:ciscoBulkFileStatusGroup.setStatus(_B)
ciscoBulkFileDefineGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,81,3,2,4))
ciscoBulkFileDefineGroupRev1.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_q),(_A,_r),(_A,_s)))
if mibBuilder.loadTexts:ciscoBulkFileDefineGroupRev1.setStatus(_B)
cbfDefineFileCompletion=NotificationType((1,3,6,1,4,1,9,9,81,2,0,1))
cbfDefineFileCompletion.setObjects(*((_A,_b),(_A,_c)))
if mibBuilder.loadTexts:cbfDefineFileCompletion.setStatus(_B)
ciscoBulkFileNotiGroup=NotificationGroup((1,3,6,1,4,1,9,9,81,3,2,3))
ciscoBulkFileNotiGroup.setObjects((_A,_t))
if mibBuilder.loadTexts:ciscoBulkFileNotiGroup.setStatus(_B)
ciscoBulkFileMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,81,3,1,1))
ciscoBulkFileMIBCompliance.setObjects(*((_A,_u),(_A,_d),(_A,_e)))
if mibBuilder.loadTexts:ciscoBulkFileMIBCompliance.setStatus(_k)
ciscoBulkFileMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,81,3,1,2))
ciscoBulkFileMIBComplianceRev1.setObjects(*((_A,_v),(_A,_d),(_A,_e)))
if mibBuilder.loadTexts:ciscoBulkFileMIBComplianceRev1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoBulkFileMIB':ciscoBulkFileMIB,'ciscoBulkFileMIBObjects':ciscoBulkFileMIBObjects,'cbfDefine':cbfDefine,_K:cbfDefineMaxFiles,_L:cbfDefineFiles,_M:cbfDefineHighFiles,_N:cbfDefineFilesRefused,_O:cbfDefineMaxObjects,_P:cbfDefineObjects,_Q:cbfDefineHighObjects,_R:cbfDefineObjectsRefused,'cbfDefineFileTable':cbfDefineFileTable,'cbfDefineFileEntry':cbfDefineFileEntry,_H:cbfDefineFileIndex,_S:cbfDefineFileName,_T:cbfDefineFileStorage,_U:cbfDefineFileFormat,_V:cbfDefineFileNow,_W:cbfDefineFileEntryStatus,_X:cbfDefineFileNotifyOnCompletion,'cbfDefineObjectTable':cbfDefineObjectTable,'cbfDefineObjectEntry':cbfDefineObjectEntry,_i:cbfDefineObjectIndex,_Y:cbfDefineObjectClass,_Z:cbfDefineObjectID,_a:cbfDefineObjectEntryStatus,_q:cbfDefineObjectTableInstance,_r:cbfDefineObjectNumEntries,_s:cbfDefineObjectLastPolledInst,'cbfStatus':cbfStatus,_l:cbfStatusMaxFiles,_m:cbfStatusFiles,_n:cbfStatusHighFiles,_o:cbfStatusFilesBumped,'cbfStatusFileTable':cbfStatusFileTable,'cbfStatusFileEntry':cbfStatusFileEntry,_j:cbfStatusFileIndex,_b:cbfStatusFileState,_c:cbfStatusFileCompletionTime,_p:cbfStatusFileEntryStatus,'ciscoBulkFileMIBNotificationPrefix':ciscoBulkFileMIBNotificationPrefix,'ciscoBulkFileMIBNotifications':ciscoBulkFileMIBNotifications,_t:cbfDefineFileCompletion,'ciscoBulkFileMIBConformance':ciscoBulkFileMIBConformance,'ciscoBulkFileMIBCompliances':ciscoBulkFileMIBCompliances,'ciscoBulkFileMIBCompliance':ciscoBulkFileMIBCompliance,'ciscoBulkFileMIBComplianceRev1':ciscoBulkFileMIBComplianceRev1,'ciscoBulkFileMIBGroups':ciscoBulkFileMIBGroups,_u:ciscoBulkFileDefineGroup,_d:ciscoBulkFileStatusGroup,_e:ciscoBulkFileNotiGroup,_v:ciscoBulkFileDefineGroupRev1})