_R='customCfgActualConfigName'
_Q='customCfgExecPointId'
_P='customCfgExecElementNumber'
_O='customCfgToolId'
_N='interrupted'
_M='completed'
_L='ExecutionStatus'
_K='customCfgListId'
_J='CfgFtpTranferStatus'
_I='notActive'
_H='read-write'
_G='not-accessible'
_F='SIAE-CUSTOM-CONFIGURATION-MIB'
_E='Integer32'
_D='DisplayString'
_C='read-create'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
siaeMib,=mibBuilder.importSymbols('SIAE-TREE-MIB','siaeMib')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','RowStatus','TextualConvention')
customCfgMib=ModuleIdentity((1,3,6,1,4,1,3373,1103,97))
if mibBuilder.loadTexts:customCfgMib.setRevisions(('2015-07-21 00:00',))
class CfgFtpTranferStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('inProgress',1),(_M,2),(_N,3)))
class CfgToolFtpTransferFailureReason(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('connectFailure',0),('fileTransferFailure',1),('fileSavingFailure',2),('aborted',3)))
class ExecutionStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('notStarted',1),('running',2),(_M,3),(_N,4)))
class ScriptType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('constructor',1),('destructor',2)))
class _CustomCfgMibVersion_Type(Integer32):defaultValue=1
_CustomCfgMibVersion_Type.__name__=_E
_CustomCfgMibVersion_Object=MibScalar
customCfgMibVersion=_CustomCfgMibVersion_Object((1,3,6,1,4,1,3373,1103,97,1),_CustomCfgMibVersion_Type())
customCfgMibVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:customCfgMibVersion.setStatus(_A)
_CustomCfgToolTable_Object=MibTable
customCfgToolTable=_CustomCfgToolTable_Object((1,3,6,1,4,1,3373,1103,97,2))
if mibBuilder.loadTexts:customCfgToolTable.setStatus(_A)
_CustomCfgToolEntry_Object=MibTableRow
customCfgToolEntry=_CustomCfgToolEntry_Object((1,3,6,1,4,1,3373,1103,97,2,1))
customCfgToolEntry.setIndexNames((0,_F,_O))
if mibBuilder.loadTexts:customCfgToolEntry.setStatus(_A)
_CustomCfgToolId_Type=Integer32
_CustomCfgToolId_Object=MibTableColumn
customCfgToolId=_CustomCfgToolId_Object((1,3,6,1,4,1,3373,1103,97,2,1,1),_CustomCfgToolId_Type())
customCfgToolId.setMaxAccess(_G)
if mibBuilder.loadTexts:customCfgToolId.setStatus(_A)
_CustomCfgToolRowStatus_Type=RowStatus
_CustomCfgToolRowStatus_Object=MibTableColumn
customCfgToolRowStatus=_CustomCfgToolRowStatus_Object((1,3,6,1,4,1,3373,1103,97,2,1,2),_CustomCfgToolRowStatus_Type())
customCfgToolRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:customCfgToolRowStatus.setStatus(_A)
class _CustomCfgToolDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CustomCfgToolDescription_Type.__name__=_D
_CustomCfgToolDescription_Object=MibTableColumn
customCfgToolDescription=_CustomCfgToolDescription_Object((1,3,6,1,4,1,3373,1103,97,2,1,3),_CustomCfgToolDescription_Type())
customCfgToolDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:customCfgToolDescription.setStatus(_A)
class _CustomCfgToolConstructorName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CustomCfgToolConstructorName_Type.__name__=_D
_CustomCfgToolConstructorName_Object=MibTableColumn
customCfgToolConstructorName=_CustomCfgToolConstructorName_Object((1,3,6,1,4,1,3373,1103,97,2,1,4),_CustomCfgToolConstructorName_Type())
customCfgToolConstructorName.setMaxAccess(_B)
if mibBuilder.loadTexts:customCfgToolConstructorName.setStatus(_A)
class _CustomCfgToolDestructorName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CustomCfgToolDestructorName_Type.__name__=_D
_CustomCfgToolDestructorName_Object=MibTableColumn
customCfgToolDestructorName=_CustomCfgToolDestructorName_Object((1,3,6,1,4,1,3373,1103,97,2,1,5),_CustomCfgToolDestructorName_Type())
customCfgToolDestructorName.setMaxAccess(_B)
if mibBuilder.loadTexts:customCfgToolDestructorName.setStatus(_A)
_CustomCfgToolFtpServerIpAddress_Type=IpAddress
_CustomCfgToolFtpServerIpAddress_Object=MibTableColumn
customCfgToolFtpServerIpAddress=_CustomCfgToolFtpServerIpAddress_Object((1,3,6,1,4,1,3373,1103,97,2,1,6),_CustomCfgToolFtpServerIpAddress_Type())
customCfgToolFtpServerIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:customCfgToolFtpServerIpAddress.setStatus(_A)
class _CustomCfgToolFtpConstructorName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CustomCfgToolFtpConstructorName_Type.__name__=_D
_CustomCfgToolFtpConstructorName_Object=MibTableColumn
customCfgToolFtpConstructorName=_CustomCfgToolFtpConstructorName_Object((1,3,6,1,4,1,3373,1103,97,2,1,7),_CustomCfgToolFtpConstructorName_Type())
customCfgToolFtpConstructorName.setMaxAccess(_C)
if mibBuilder.loadTexts:customCfgToolFtpConstructorName.setStatus(_A)
class _CustomCfgToolFtpDestructorName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CustomCfgToolFtpDestructorName_Type.__name__=_D
_CustomCfgToolFtpDestructorName_Object=MibTableColumn
customCfgToolFtpDestructorName=_CustomCfgToolFtpDestructorName_Object((1,3,6,1,4,1,3373,1103,97,2,1,8),_CustomCfgToolFtpDestructorName_Type())
customCfgToolFtpDestructorName.setMaxAccess(_C)
if mibBuilder.loadTexts:customCfgToolFtpDestructorName.setStatus(_A)
class _CustomCfgToolUploadActionRequest_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_I,0),('loadCfg',1),('loadCfgContructor',2),('loadCfgDestructor',3),('removeCfg',4)))
_CustomCfgToolUploadActionRequest_Type.__name__=_E
_CustomCfgToolUploadActionRequest_Object=MibTableColumn
customCfgToolUploadActionRequest=_CustomCfgToolUploadActionRequest_Object((1,3,6,1,4,1,3373,1103,97,2,1,9),_CustomCfgToolUploadActionRequest_Type())
customCfgToolUploadActionRequest.setMaxAccess(_C)
if mibBuilder.loadTexts:customCfgToolUploadActionRequest.setStatus(_A)
class _CustomCfgToolUploadStatus_Type(CfgFtpTranferStatus):defaultValue=0
_CustomCfgToolUploadStatus_Type.__name__=_J
_CustomCfgToolUploadStatus_Object=MibTableColumn
customCfgToolUploadStatus=_CustomCfgToolUploadStatus_Object((1,3,6,1,4,1,3373,1103,97,2,1,10),_CustomCfgToolUploadStatus_Type())
customCfgToolUploadStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:customCfgToolUploadStatus.setStatus(_A)
_CustomCfgToolUploadFailure_Type=CfgToolFtpTransferFailureReason
_CustomCfgToolUploadFailure_Object=MibTableColumn
customCfgToolUploadFailure=_CustomCfgToolUploadFailure_Object((1,3,6,1,4,1,3373,1103,97,2,1,11),_CustomCfgToolUploadFailure_Type())
customCfgToolUploadFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:customCfgToolUploadFailure.setStatus(_A)
class _CustomCfgFlushActionRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),('startRemove',1)))
_CustomCfgFlushActionRequest_Type.__name__=_E
_CustomCfgFlushActionRequest_Object=MibScalar
customCfgFlushActionRequest=_CustomCfgFlushActionRequest_Object((1,3,6,1,4,1,3373,1103,97,3),_CustomCfgFlushActionRequest_Type())
customCfgFlushActionRequest.setMaxAccess(_H)
if mibBuilder.loadTexts:customCfgFlushActionRequest.setStatus(_A)
_CustomCfgListTable_Object=MibTable
customCfgListTable=_CustomCfgListTable_Object((1,3,6,1,4,1,3373,1103,97,4))
if mibBuilder.loadTexts:customCfgListTable.setStatus(_A)
_CustomCfgListEntry_Object=MibTableRow
customCfgListEntry=_CustomCfgListEntry_Object((1,3,6,1,4,1,3373,1103,97,4,1))
customCfgListEntry.setIndexNames((0,_F,_K))
if mibBuilder.loadTexts:customCfgListEntry.setStatus(_A)
_CustomCfgListId_Type=Integer32
_CustomCfgListId_Object=MibTableColumn
customCfgListId=_CustomCfgListId_Object((1,3,6,1,4,1,3373,1103,97,4,1,1),_CustomCfgListId_Type())
customCfgListId.setMaxAccess(_G)
if mibBuilder.loadTexts:customCfgListId.setStatus(_A)
_CustomCfgListRowStatus_Type=RowStatus
_CustomCfgListRowStatus_Object=MibTableColumn
customCfgListRowStatus=_CustomCfgListRowStatus_Object((1,3,6,1,4,1,3373,1103,97,4,1,2),_CustomCfgListRowStatus_Type())
customCfgListRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:customCfgListRowStatus.setStatus(_A)
class _CustomCfgListName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CustomCfgListName_Type.__name__=_D
_CustomCfgListName_Object=MibTableColumn
customCfgListName=_CustomCfgListName_Object((1,3,6,1,4,1,3373,1103,97,4,1,3),_CustomCfgListName_Type())
customCfgListName.setMaxAccess(_C)
if mibBuilder.loadTexts:customCfgListName.setStatus(_A)
class _CustomCfgListStatus_Type(ExecutionStatus):defaultValue=1
_CustomCfgListStatus_Type.__name__=_L
_CustomCfgListStatus_Object=MibTableColumn
customCfgListStatus=_CustomCfgListStatus_Object((1,3,6,1,4,1,3373,1103,97,4,1,4),_CustomCfgListStatus_Type())
customCfgListStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:customCfgListStatus.setStatus(_A)
class _CustomCfgListActionRequest_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),('run',1)))
_CustomCfgListActionRequest_Type.__name__=_E
_CustomCfgListActionRequest_Object=MibTableColumn
customCfgListActionRequest=_CustomCfgListActionRequest_Object((1,3,6,1,4,1,3373,1103,97,4,1,5),_CustomCfgListActionRequest_Type())
customCfgListActionRequest.setMaxAccess(_C)
if mibBuilder.loadTexts:customCfgListActionRequest.setStatus(_A)
_CustomCfgExecListTable_Object=MibTable
customCfgExecListTable=_CustomCfgExecListTable_Object((1,3,6,1,4,1,3373,1103,97,5))
if mibBuilder.loadTexts:customCfgExecListTable.setStatus(_A)
_CustomCfgExecListEntry_Object=MibTableRow
customCfgExecListEntry=_CustomCfgExecListEntry_Object((1,3,6,1,4,1,3373,1103,97,5,1))
customCfgExecListEntry.setIndexNames((0,_F,_K),(0,_F,_P))
if mibBuilder.loadTexts:customCfgExecListEntry.setStatus(_A)
_CustomCfgExecElementNumber_Type=Integer32
_CustomCfgExecElementNumber_Object=MibTableColumn
customCfgExecElementNumber=_CustomCfgExecElementNumber_Object((1,3,6,1,4,1,3373,1103,97,5,1,1),_CustomCfgExecElementNumber_Type())
customCfgExecElementNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:customCfgExecElementNumber.setStatus(_A)
_CustomCfgExecRowStatus_Type=RowStatus
_CustomCfgExecRowStatus_Object=MibTableColumn
customCfgExecRowStatus=_CustomCfgExecRowStatus_Object((1,3,6,1,4,1,3373,1103,97,5,1,2),_CustomCfgExecRowStatus_Type())
customCfgExecRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:customCfgExecRowStatus.setStatus(_A)
_CustomCfgExecToolId_Type=Integer32
_CustomCfgExecToolId_Object=MibTableColumn
customCfgExecToolId=_CustomCfgExecToolId_Object((1,3,6,1,4,1,3373,1103,97,5,1,3),_CustomCfgExecToolId_Type())
customCfgExecToolId.setMaxAccess(_C)
if mibBuilder.loadTexts:customCfgExecToolId.setStatus(_A)
_CustomCfgExecScriptType_Type=ScriptType
_CustomCfgExecScriptType_Object=MibTableColumn
customCfgExecScriptType=_CustomCfgExecScriptType_Object((1,3,6,1,4,1,3373,1103,97,5,1,4),_CustomCfgExecScriptType_Type())
customCfgExecScriptType.setMaxAccess(_C)
if mibBuilder.loadTexts:customCfgExecScriptType.setStatus(_A)
class _CustomCfgExecScriptStatus_Type(ExecutionStatus):defaultValue=1
_CustomCfgExecScriptStatus_Type.__name__=_L
_CustomCfgExecScriptStatus_Object=MibTableColumn
customCfgExecScriptStatus=_CustomCfgExecScriptStatus_Object((1,3,6,1,4,1,3373,1103,97,5,1,5),_CustomCfgExecScriptStatus_Type())
customCfgExecScriptStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:customCfgExecScriptStatus.setStatus(_A)
_CustomCfgCurrentExecPointTable_Object=MibTable
customCfgCurrentExecPointTable=_CustomCfgCurrentExecPointTable_Object((1,3,6,1,4,1,3373,1103,97,6))
if mibBuilder.loadTexts:customCfgCurrentExecPointTable.setStatus(_A)
_CustomCfgExecPointListEntry_Object=MibTableRow
customCfgExecPointListEntry=_CustomCfgExecPointListEntry_Object((1,3,6,1,4,1,3373,1103,97,6,1))
customCfgExecPointListEntry.setIndexNames((0,_F,_Q))
if mibBuilder.loadTexts:customCfgExecPointListEntry.setStatus(_A)
class _CustomCfgExecPointId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_CustomCfgExecPointId_Type.__name__=_E
_CustomCfgExecPointId_Object=MibTableColumn
customCfgExecPointId=_CustomCfgExecPointId_Object((1,3,6,1,4,1,3373,1103,97,6,1,1),_CustomCfgExecPointId_Type())
customCfgExecPointId.setMaxAccess(_G)
if mibBuilder.loadTexts:customCfgExecPointId.setStatus(_A)
_CustomCfgExecPointListId_Type=Integer32
_CustomCfgExecPointListId_Object=MibTableColumn
customCfgExecPointListId=_CustomCfgExecPointListId_Object((1,3,6,1,4,1,3373,1103,97,6,1,2),_CustomCfgExecPointListId_Type())
customCfgExecPointListId.setMaxAccess(_B)
if mibBuilder.loadTexts:customCfgExecPointListId.setStatus(_A)
_CustomCfgExecPointListElementId_Type=Integer32
_CustomCfgExecPointListElementId_Object=MibTableColumn
customCfgExecPointListElementId=_CustomCfgExecPointListElementId_Object((1,3,6,1,4,1,3373,1103,97,6,1,3),_CustomCfgExecPointListElementId_Type())
customCfgExecPointListElementId.setMaxAccess(_B)
if mibBuilder.loadTexts:customCfgExecPointListElementId.setStatus(_A)
class _CustomCfgExecPointScriptName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CustomCfgExecPointScriptName_Type.__name__=_D
_CustomCfgExecPointScriptName_Object=MibTableColumn
customCfgExecPointScriptName=_CustomCfgExecPointScriptName_Object((1,3,6,1,4,1,3373,1103,97,6,1,4),_CustomCfgExecPointScriptName_Type())
customCfgExecPointScriptName.setMaxAccess(_B)
if mibBuilder.loadTexts:customCfgExecPointScriptName.setStatus(_A)
_CustomCfgExecPointScriptLine_Type=Integer32
_CustomCfgExecPointScriptLine_Object=MibTableColumn
customCfgExecPointScriptLine=_CustomCfgExecPointScriptLine_Object((1,3,6,1,4,1,3373,1103,97,6,1,5),_CustomCfgExecPointScriptLine_Type())
customCfgExecPointScriptLine.setMaxAccess(_B)
if mibBuilder.loadTexts:customCfgExecPointScriptLine.setStatus(_A)
_CustomCfgExecPointScriptRows_Type=Integer32
_CustomCfgExecPointScriptRows_Object=MibTableColumn
customCfgExecPointScriptRows=_CustomCfgExecPointScriptRows_Object((1,3,6,1,4,1,3373,1103,97,6,1,6),_CustomCfgExecPointScriptRows_Type())
customCfgExecPointScriptRows.setMaxAccess(_B)
if mibBuilder.loadTexts:customCfgExecPointScriptRows.setStatus(_A)
_CustomCfgActualConfigTable_Object=MibTable
customCfgActualConfigTable=_CustomCfgActualConfigTable_Object((1,3,6,1,4,1,3373,1103,97,7))
if mibBuilder.loadTexts:customCfgActualConfigTable.setStatus(_A)
_CustomCfgActualConfigEntry_Object=MibTableRow
customCfgActualConfigEntry=_CustomCfgActualConfigEntry_Object((1,3,6,1,4,1,3373,1103,97,7,1))
customCfgActualConfigEntry.setIndexNames((0,_F,_R))
if mibBuilder.loadTexts:customCfgActualConfigEntry.setStatus(_A)
class _CustomCfgActualConfigName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CustomCfgActualConfigName_Type.__name__=_D
_CustomCfgActualConfigName_Object=MibTableColumn
customCfgActualConfigName=_CustomCfgActualConfigName_Object((1,3,6,1,4,1,3373,1103,97,7,1,1),_CustomCfgActualConfigName_Type())
customCfgActualConfigName.setMaxAccess(_B)
if mibBuilder.loadTexts:customCfgActualConfigName.setStatus(_A)
_CustomCfgActualConfigRowStatus_Type=RowStatus
_CustomCfgActualConfigRowStatus_Object=MibTableColumn
customCfgActualConfigRowStatus=_CustomCfgActualConfigRowStatus_Object((1,3,6,1,4,1,3373,1103,97,7,1,2),_CustomCfgActualConfigRowStatus_Type())
customCfgActualConfigRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:customCfgActualConfigRowStatus.setStatus(_A)
class _CustomCfgActualConfigDescription_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CustomCfgActualConfigDescription_Type.__name__=_D
_CustomCfgActualConfigDescription_Object=MibTableColumn
customCfgActualConfigDescription=_CustomCfgActualConfigDescription_Object((1,3,6,1,4,1,3373,1103,97,7,1,3),_CustomCfgActualConfigDescription_Type())
customCfgActualConfigDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:customCfgActualConfigDescription.setStatus(_A)
class _CustomCfgActualConfigVersion_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(5,5))
_CustomCfgActualConfigVersion_Type.__name__=_D
_CustomCfgActualConfigVersion_Object=MibTableColumn
customCfgActualConfigVersion=_CustomCfgActualConfigVersion_Object((1,3,6,1,4,1,3373,1103,97,7,1,4),_CustomCfgActualConfigVersion_Type())
customCfgActualConfigVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:customCfgActualConfigVersion.setStatus(_A)
_CustomCfgFtpLogTransfer_ObjectIdentity=ObjectIdentity
customCfgFtpLogTransfer=_CustomCfgFtpLogTransfer_ObjectIdentity((1,3,6,1,4,1,3373,1103,97,8))
class _CustomCfgLogActionRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('none',0),('deleteScriptExecLog',1),('readScriptExecLog',2),('deleteFaileCmdLog',3),('readFailedCmdLog',4)))
_CustomCfgLogActionRequest_Type.__name__=_E
_CustomCfgLogActionRequest_Object=MibScalar
customCfgLogActionRequest=_CustomCfgLogActionRequest_Object((1,3,6,1,4,1,3373,1103,97,8,1),_CustomCfgLogActionRequest_Type())
customCfgLogActionRequest.setMaxAccess(_H)
if mibBuilder.loadTexts:customCfgLogActionRequest.setStatus(_A)
class _CustomCfgLogFtpFilename_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CustomCfgLogFtpFilename_Type.__name__=_D
_CustomCfgLogFtpFilename_Object=MibScalar
customCfgLogFtpFilename=_CustomCfgLogFtpFilename_Object((1,3,6,1,4,1,3373,1103,97,8,2),_CustomCfgLogFtpFilename_Type())
customCfgLogFtpFilename.setMaxAccess(_H)
if mibBuilder.loadTexts:customCfgLogFtpFilename.setStatus(_A)
_CustomCfgLogServerIpAddress_Type=IpAddress
_CustomCfgLogServerIpAddress_Object=MibScalar
customCfgLogServerIpAddress=_CustomCfgLogServerIpAddress_Object((1,3,6,1,4,1,3373,1103,97,8,3),_CustomCfgLogServerIpAddress_Type())
customCfgLogServerIpAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:customCfgLogServerIpAddress.setStatus(_A)
class _CustomCfgLogDownloadStatus_Type(CfgFtpTranferStatus):defaultValue=0
_CustomCfgLogDownloadStatus_Type.__name__=_J
_CustomCfgLogDownloadStatus_Object=MibScalar
customCfgLogDownloadStatus=_CustomCfgLogDownloadStatus_Object((1,3,6,1,4,1,3373,1103,97,8,4),_CustomCfgLogDownloadStatus_Type())
customCfgLogDownloadStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:customCfgLogDownloadStatus.setStatus(_A)
_CustomCfgLogDownloadFailure_Type=CfgToolFtpTransferFailureReason
_CustomCfgLogDownloadFailure_Object=MibScalar
customCfgLogDownloadFailure=_CustomCfgLogDownloadFailure_Object((1,3,6,1,4,1,3373,1103,97,8,5),_CustomCfgLogDownloadFailure_Type())
customCfgLogDownloadFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:customCfgLogDownloadFailure.setStatus(_A)
mibBuilder.exportSymbols(_F,**{_J:CfgFtpTranferStatus,'CfgToolFtpTransferFailureReason':CfgToolFtpTransferFailureReason,_L:ExecutionStatus,'ScriptType':ScriptType,'customCfgMib':customCfgMib,'customCfgMibVersion':customCfgMibVersion,'customCfgToolTable':customCfgToolTable,'customCfgToolEntry':customCfgToolEntry,_O:customCfgToolId,'customCfgToolRowStatus':customCfgToolRowStatus,'customCfgToolDescription':customCfgToolDescription,'customCfgToolConstructorName':customCfgToolConstructorName,'customCfgToolDestructorName':customCfgToolDestructorName,'customCfgToolFtpServerIpAddress':customCfgToolFtpServerIpAddress,'customCfgToolFtpConstructorName':customCfgToolFtpConstructorName,'customCfgToolFtpDestructorName':customCfgToolFtpDestructorName,'customCfgToolUploadActionRequest':customCfgToolUploadActionRequest,'customCfgToolUploadStatus':customCfgToolUploadStatus,'customCfgToolUploadFailure':customCfgToolUploadFailure,'customCfgFlushActionRequest':customCfgFlushActionRequest,'customCfgListTable':customCfgListTable,'customCfgListEntry':customCfgListEntry,_K:customCfgListId,'customCfgListRowStatus':customCfgListRowStatus,'customCfgListName':customCfgListName,'customCfgListStatus':customCfgListStatus,'customCfgListActionRequest':customCfgListActionRequest,'customCfgExecListTable':customCfgExecListTable,'customCfgExecListEntry':customCfgExecListEntry,_P:customCfgExecElementNumber,'customCfgExecRowStatus':customCfgExecRowStatus,'customCfgExecToolId':customCfgExecToolId,'customCfgExecScriptType':customCfgExecScriptType,'customCfgExecScriptStatus':customCfgExecScriptStatus,'customCfgCurrentExecPointTable':customCfgCurrentExecPointTable,'customCfgExecPointListEntry':customCfgExecPointListEntry,_Q:customCfgExecPointId,'customCfgExecPointListId':customCfgExecPointListId,'customCfgExecPointListElementId':customCfgExecPointListElementId,'customCfgExecPointScriptName':customCfgExecPointScriptName,'customCfgExecPointScriptLine':customCfgExecPointScriptLine,'customCfgExecPointScriptRows':customCfgExecPointScriptRows,'customCfgActualConfigTable':customCfgActualConfigTable,'customCfgActualConfigEntry':customCfgActualConfigEntry,_R:customCfgActualConfigName,'customCfgActualConfigRowStatus':customCfgActualConfigRowStatus,'customCfgActualConfigDescription':customCfgActualConfigDescription,'customCfgActualConfigVersion':customCfgActualConfigVersion,'customCfgFtpLogTransfer':customCfgFtpLogTransfer,'customCfgLogActionRequest':customCfgLogActionRequest,'customCfgLogFtpFilename':customCfgLogFtpFilename,'customCfgLogServerIpAddress':customCfgLogServerIpAddress,'customCfgLogDownloadStatus':customCfgLogDownloadStatus,'customCfgLogDownloadFailure':customCfgLogDownloadFailure})