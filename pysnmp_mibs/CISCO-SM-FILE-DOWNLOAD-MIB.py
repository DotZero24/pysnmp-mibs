_V='csFileStatusGroup'
_U='csDefineFileGroup'
_T='csFileSlotState'
_S='csDefineFileEntryStatus'
_R='csDefineFileOperation'
_Q='csDefineFileStatus'
_P='csDefineSlotNumber'
_O='csDefineFileName'
_N='csFileStatusSlotNumber'
_M='read-only'
_L='aborted'
_K='fileOpenFailed'
_J='success'
_I='inProgress'
_H='not-accessible'
_G='DisplayString'
_F='csDefineFileIndex'
_E='read-create'
_D='Unsigned32'
_C='Integer32'
_B='CISCO-SM-FILE-DOWNLOAD-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','RowStatus','TextualConvention')
ciscoSmFileDownloadMIB=ModuleIdentity((1,3,6,1,4,1,9,9,199))
if mibBuilder.loadTexts:ciscoSmFileDownloadMIB.setRevisions(('2002-05-21 00:00','2001-02-02 00:00'))
_CsFileMIBObjects_ObjectIdentity=ObjectIdentity
csFileMIBObjects=_CsFileMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,199,1))
_CsDefineFile_ObjectIdentity=ObjectIdentity
csDefineFile=_CsDefineFile_ObjectIdentity((1,3,6,1,4,1,9,9,199,1,1))
_CsDefineFileTable_Object=MibTable
csDefineFileTable=_CsDefineFileTable_Object((1,3,6,1,4,1,9,9,199,1,1,1))
if mibBuilder.loadTexts:csDefineFileTable.setStatus(_A)
_CsDefineFileEntry_Object=MibTableRow
csDefineFileEntry=_CsDefineFileEntry_Object((1,3,6,1,4,1,9,9,199,1,1,1,1))
csDefineFileEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:csDefineFileEntry.setStatus(_A)
class _CsDefineFileIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CsDefineFileIndex_Type.__name__=_D
_CsDefineFileIndex_Object=MibTableColumn
csDefineFileIndex=_CsDefineFileIndex_Object((1,3,6,1,4,1,9,9,199,1,1,1,1,1),_CsDefineFileIndex_Type())
csDefineFileIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:csDefineFileIndex.setStatus(_A)
class _CsDefineFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CsDefineFileName_Type.__name__=_G
_CsDefineFileName_Object=MibTableColumn
csDefineFileName=_CsDefineFileName_Object((1,3,6,1,4,1,9,9,199,1,1,1,1,2),_CsDefineFileName_Type())
csDefineFileName.setMaxAccess(_E)
if mibBuilder.loadTexts:csDefineFileName.setStatus(_A)
class _CsDefineSlotNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32),ValueRangeConstraint(100,100))
_CsDefineSlotNumber_Type.__name__=_D
_CsDefineSlotNumber_Object=MibTableColumn
csDefineSlotNumber=_CsDefineSlotNumber_Object((1,3,6,1,4,1,9,9,199,1,1,1,1,3),_CsDefineSlotNumber_Type())
csDefineSlotNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:csDefineSlotNumber.setStatus(_A)
class _CsDefineFileStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_I,1),(_J,2),('noMemory',3),(_K,4),('fileReadFailed',5),('fileNotValid',6),('downloadFailed',7),(_L,8),('dbUpdateFailed',9),('miscError',10)))
_CsDefineFileStatus_Type.__name__=_C
_CsDefineFileStatus_Object=MibTableColumn
csDefineFileStatus=_CsDefineFileStatus_Object((1,3,6,1,4,1,9,9,199,1,1,1,1,4),_CsDefineFileStatus_Type())
csDefineFileStatus.setMaxAccess(_M)
if mibBuilder.loadTexts:csDefineFileStatus.setStatus(_A)
class _CsDefineFileOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('sendToSMsOnly',1),('updateAndSend',2)))
_CsDefineFileOperation_Type.__name__=_C
_CsDefineFileOperation_Object=MibTableColumn
csDefineFileOperation=_CsDefineFileOperation_Object((1,3,6,1,4,1,9,9,199,1,1,1,1,5),_CsDefineFileOperation_Type())
csDefineFileOperation.setMaxAccess(_E)
if mibBuilder.loadTexts:csDefineFileOperation.setStatus(_A)
_CsDefineFileEntryStatus_Type=RowStatus
_CsDefineFileEntryStatus_Object=MibTableColumn
csDefineFileEntryStatus=_CsDefineFileEntryStatus_Object((1,3,6,1,4,1,9,9,199,1,1,1,1,6),_CsDefineFileEntryStatus_Type())
csDefineFileEntryStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:csDefineFileEntryStatus.setStatus(_A)
_CsFileStatus_ObjectIdentity=ObjectIdentity
csFileStatus=_CsFileStatus_ObjectIdentity((1,3,6,1,4,1,9,9,199,1,2))
_CsFileStatusTable_Object=MibTable
csFileStatusTable=_CsFileStatusTable_Object((1,3,6,1,4,1,9,9,199,1,2,1))
if mibBuilder.loadTexts:csFileStatusTable.setStatus(_A)
_CsFileStatusEntry_Object=MibTableRow
csFileStatusEntry=_CsFileStatusEntry_Object((1,3,6,1,4,1,9,9,199,1,2,1,1))
csFileStatusEntry.setIndexNames((0,_B,_F),(0,_B,_N))
if mibBuilder.loadTexts:csFileStatusEntry.setStatus(_A)
class _CsFileStatusSlotNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_CsFileStatusSlotNumber_Type.__name__=_D
_CsFileStatusSlotNumber_Object=MibTableColumn
csFileStatusSlotNumber=_CsFileStatusSlotNumber_Object((1,3,6,1,4,1,9,9,199,1,2,1,1,1),_CsFileStatusSlotNumber_Type())
csFileStatusSlotNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:csFileStatusSlotNumber.setStatus(_A)
class _CsFileSlotState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_I,1),('notProcessed',2),(_J,3),(_K,4),('fileWriteFailed',5),(_L,6),('miscFailure',7)))
_CsFileSlotState_Type.__name__=_C
_CsFileSlotState_Object=MibTableColumn
csFileSlotState=_CsFileSlotState_Object((1,3,6,1,4,1,9,9,199,1,2,1,1,2),_CsFileSlotState_Type())
csFileSlotState.setMaxAccess(_M)
if mibBuilder.loadTexts:csFileSlotState.setStatus(_A)
_CsFileMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
csFileMIBNotificationPrefix=_CsFileMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,199,2))
_CsFileMIBNotifications_ObjectIdentity=ObjectIdentity
csFileMIBNotifications=_CsFileMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,199,2,0))
_CsFileMIBConformance_ObjectIdentity=ObjectIdentity
csFileMIBConformance=_CsFileMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,199,3))
_CsFileMIBCompliances_ObjectIdentity=ObjectIdentity
csFileMIBCompliances=_CsFileMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,199,3,1))
_CsFileMIBGroups_ObjectIdentity=ObjectIdentity
csFileMIBGroups=_CsFileMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,199,3,2))
csDefineFileGroup=ObjectGroup((1,3,6,1,4,1,9,9,199,3,2,1))
csDefineFileGroup.setObjects(*((_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:csDefineFileGroup.setStatus(_A)
csFileStatusGroup=ObjectGroup((1,3,6,1,4,1,9,9,199,3,2,2))
csFileStatusGroup.setObjects((_B,_T))
if mibBuilder.loadTexts:csFileStatusGroup.setStatus(_A)
csFileMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,199,3,1,1))
csFileMIBCompliance.setObjects(*((_B,_U),(_B,_V)))
if mibBuilder.loadTexts:csFileMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoSmFileDownloadMIB':ciscoSmFileDownloadMIB,'csFileMIBObjects':csFileMIBObjects,'csDefineFile':csDefineFile,'csDefineFileTable':csDefineFileTable,'csDefineFileEntry':csDefineFileEntry,_F:csDefineFileIndex,_O:csDefineFileName,_P:csDefineSlotNumber,_Q:csDefineFileStatus,_R:csDefineFileOperation,_S:csDefineFileEntryStatus,'csFileStatus':csFileStatus,'csFileStatusTable':csFileStatusTable,'csFileStatusEntry':csFileStatusEntry,_N:csFileStatusSlotNumber,_T:csFileSlotState,'csFileMIBNotificationPrefix':csFileMIBNotificationPrefix,'csFileMIBNotifications':csFileMIBNotifications,'csFileMIBConformance':csFileMIBConformance,'csFileMIBCompliances':csFileMIBCompliances,'csFileMIBCompliance':csFileMIBCompliance,'csFileMIBGroups':csFileMIBGroups,_U:csDefineFileGroup,_V:csFileStatusGroup})