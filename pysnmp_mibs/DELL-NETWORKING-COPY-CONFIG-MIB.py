_J='copyConfigIndex'
_I='accessible-for-notify'
_H='DisplayString'
_G='read-only'
_F='copyAlarmIndex'
_E='copyAlarmString'
_D='copyAlarmLevel'
_C='read-write'
_B='DELL-NETWORKING-COPY-CONFIG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dellNetMgmt,=mibBuilder.importSymbols('DELL-NETWORKING-SMI','dellNetMgmt')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','RowStatus','TextualConvention')
dellNetCopyConfigMib=ModuleIdentity((1,3,6,1,4,1,6027,3,5))
if mibBuilder.loadTexts:dellNetCopyConfigMib.setRevisions(('2009-05-14 13:00','2007-06-19 12:00','2003-03-01 12:00'))
class DellNetConfigFileLocation(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('flash',1),('slot0',2),('tftp',3),('ftp',4),('scp',5),('usbflash',6),('nfsmount',7)))
class DellNetConfigFileType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('dellNetFile',1),('runningConfig',2),('startupConfig',3)))
class DellNetConfigCopyState(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('running',1),('successful',2),('failed',3)))
class DellNetConfigCopyFailCause(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('badFileName',1),('copyInProgress',2),('diskFull',3),('fileExist',4),('fileNotFound',5),('timeout',6),('unknown',7)))
_DellNetCopyConfigObjects_ObjectIdentity=ObjectIdentity
dellNetCopyConfigObjects=_DellNetCopyConfigObjects_ObjectIdentity((1,3,6,1,4,1,6027,3,5,1))
_DellNetCopyConfig_ObjectIdentity=ObjectIdentity
dellNetCopyConfig=_DellNetCopyConfig_ObjectIdentity((1,3,6,1,4,1,6027,3,5,1,1))
_DellNetCopyTable_Object=MibTable
dellNetCopyTable=_DellNetCopyTable_Object((1,3,6,1,4,1,6027,3,5,1,1,1))
if mibBuilder.loadTexts:dellNetCopyTable.setStatus(_A)
_DellNetCopyEntry_Object=MibTableRow
dellNetCopyEntry=_DellNetCopyEntry_Object((1,3,6,1,4,1,6027,3,5,1,1,1,1))
dellNetCopyEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:dellNetCopyEntry.setStatus(_A)
_CopyConfigIndex_Type=Integer32
_CopyConfigIndex_Object=MibTableColumn
copyConfigIndex=_CopyConfigIndex_Object((1,3,6,1,4,1,6027,3,5,1,1,1,1,1),_CopyConfigIndex_Type())
copyConfigIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:copyConfigIndex.setStatus(_A)
_CopySrcFileType_Type=DellNetConfigFileType
_CopySrcFileType_Object=MibTableColumn
copySrcFileType=_CopySrcFileType_Object((1,3,6,1,4,1,6027,3,5,1,1,1,1,2),_CopySrcFileType_Type())
copySrcFileType.setMaxAccess(_C)
if mibBuilder.loadTexts:copySrcFileType.setStatus(_A)
_CopySrcFileLocation_Type=DellNetConfigFileLocation
_CopySrcFileLocation_Object=MibTableColumn
copySrcFileLocation=_CopySrcFileLocation_Object((1,3,6,1,4,1,6027,3,5,1,1,1,1,3),_CopySrcFileLocation_Type())
copySrcFileLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:copySrcFileLocation.setStatus(_A)
_CopySrcFileName_Type=DisplayString
_CopySrcFileName_Object=MibTableColumn
copySrcFileName=_CopySrcFileName_Object((1,3,6,1,4,1,6027,3,5,1,1,1,1,4),_CopySrcFileName_Type())
copySrcFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:copySrcFileName.setStatus(_A)
_CopyDestFileType_Type=DellNetConfigFileType
_CopyDestFileType_Object=MibTableColumn
copyDestFileType=_CopyDestFileType_Object((1,3,6,1,4,1,6027,3,5,1,1,1,1,5),_CopyDestFileType_Type())
copyDestFileType.setMaxAccess(_C)
if mibBuilder.loadTexts:copyDestFileType.setStatus(_A)
_CopyDestFileLocation_Type=DellNetConfigFileLocation
_CopyDestFileLocation_Object=MibTableColumn
copyDestFileLocation=_CopyDestFileLocation_Object((1,3,6,1,4,1,6027,3,5,1,1,1,1,6),_CopyDestFileLocation_Type())
copyDestFileLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:copyDestFileLocation.setStatus(_A)
_CopyDestFileName_Type=DisplayString
_CopyDestFileName_Object=MibTableColumn
copyDestFileName=_CopyDestFileName_Object((1,3,6,1,4,1,6027,3,5,1,1,1,1,7),_CopyDestFileName_Type())
copyDestFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:copyDestFileName.setStatus(_A)
_CopyServerAddress_Type=IpAddress
_CopyServerAddress_Object=MibTableColumn
copyServerAddress=_CopyServerAddress_Object((1,3,6,1,4,1,6027,3,5,1,1,1,1,8),_CopyServerAddress_Type())
copyServerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:copyServerAddress.setStatus('deprecated')
class _CopyUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_CopyUserName_Type.__name__=_H
_CopyUserName_Object=MibTableColumn
copyUserName=_CopyUserName_Object((1,3,6,1,4,1,6027,3,5,1,1,1,1,9),_CopyUserName_Type())
copyUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:copyUserName.setStatus(_A)
class _CopyUserPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_CopyUserPassword_Type.__name__=_H
_CopyUserPassword_Object=MibTableColumn
copyUserPassword=_CopyUserPassword_Object((1,3,6,1,4,1,6027,3,5,1,1,1,1,10),_CopyUserPassword_Type())
copyUserPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:copyUserPassword.setStatus(_A)
_CopyState_Type=DellNetConfigCopyState
_CopyState_Object=MibTableColumn
copyState=_CopyState_Object((1,3,6,1,4,1,6027,3,5,1,1,1,1,11),_CopyState_Type())
copyState.setMaxAccess(_G)
if mibBuilder.loadTexts:copyState.setStatus(_A)
_CopyTimeStarted_Type=TimeTicks
_CopyTimeStarted_Object=MibTableColumn
copyTimeStarted=_CopyTimeStarted_Object((1,3,6,1,4,1,6027,3,5,1,1,1,1,12),_CopyTimeStarted_Type())
copyTimeStarted.setMaxAccess(_G)
if mibBuilder.loadTexts:copyTimeStarted.setStatus(_A)
_CopyTimeCompleted_Type=TimeTicks
_CopyTimeCompleted_Object=MibTableColumn
copyTimeCompleted=_CopyTimeCompleted_Object((1,3,6,1,4,1,6027,3,5,1,1,1,1,13),_CopyTimeCompleted_Type())
copyTimeCompleted.setMaxAccess(_G)
if mibBuilder.loadTexts:copyTimeCompleted.setStatus(_A)
_CopyFailCause_Type=DellNetConfigCopyFailCause
_CopyFailCause_Object=MibTableColumn
copyFailCause=_CopyFailCause_Object((1,3,6,1,4,1,6027,3,5,1,1,1,1,14),_CopyFailCause_Type())
copyFailCause.setMaxAccess(_G)
if mibBuilder.loadTexts:copyFailCause.setStatus(_A)
_CopyEntryRowStatus_Type=RowStatus
_CopyEntryRowStatus_Object=MibTableColumn
copyEntryRowStatus=_CopyEntryRowStatus_Object((1,3,6,1,4,1,6027,3,5,1,1,1,1,15),_CopyEntryRowStatus_Type())
copyEntryRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:copyEntryRowStatus.setStatus(_A)
_CopyServerInetAddressType_Type=InetAddressType
_CopyServerInetAddressType_Object=MibTableColumn
copyServerInetAddressType=_CopyServerInetAddressType_Object((1,3,6,1,4,1,6027,3,5,1,1,1,1,16),_CopyServerInetAddressType_Type())
copyServerInetAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:copyServerInetAddressType.setStatus(_A)
_CopyServerInetAddress_Type=InetAddress
_CopyServerInetAddress_Object=MibTableColumn
copyServerInetAddress=_CopyServerInetAddress_Object((1,3,6,1,4,1,6027,3,5,1,1,1,1,17),_CopyServerInetAddress_Type())
copyServerInetAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:copyServerInetAddress.setStatus(_A)
_DellNetCopyConfigTraps_ObjectIdentity=ObjectIdentity
dellNetCopyConfigTraps=_DellNetCopyConfigTraps_ObjectIdentity((1,3,6,1,4,1,6027,3,5,1,2))
_CopyAlarmMibNotifications_ObjectIdentity=ObjectIdentity
copyAlarmMibNotifications=_CopyAlarmMibNotifications_ObjectIdentity((1,3,6,1,4,1,6027,3,5,1,2,0))
_CopyAlarmVariable_ObjectIdentity=ObjectIdentity
copyAlarmVariable=_CopyAlarmVariable_ObjectIdentity((1,3,6,1,4,1,6027,3,5,1,2,1))
_CopyAlarmLevel_Type=Integer32
_CopyAlarmLevel_Object=MibScalar
copyAlarmLevel=_CopyAlarmLevel_Object((1,3,6,1,4,1,6027,3,5,1,2,1,1),_CopyAlarmLevel_Type())
copyAlarmLevel.setMaxAccess(_I)
if mibBuilder.loadTexts:copyAlarmLevel.setStatus(_A)
_CopyAlarmString_Type=OctetString
_CopyAlarmString_Object=MibScalar
copyAlarmString=_CopyAlarmString_Object((1,3,6,1,4,1,6027,3,5,1,2,1,2),_CopyAlarmString_Type())
copyAlarmString.setMaxAccess(_I)
if mibBuilder.loadTexts:copyAlarmString.setStatus(_A)
_CopyAlarmIndex_Type=Integer32
_CopyAlarmIndex_Object=MibScalar
copyAlarmIndex=_CopyAlarmIndex_Object((1,3,6,1,4,1,6027,3,5,1,2,1,3),_CopyAlarmIndex_Type())
copyAlarmIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:copyAlarmIndex.setStatus(_A)
copyConfigCompleted=NotificationType((1,3,6,1,4,1,6027,3,5,1,2,0,1))
copyConfigCompleted.setObjects(*((_B,_D),(_B,_E),(_B,_F)))
if mibBuilder.loadTexts:copyConfigCompleted.setStatus(_A)
configConflict=NotificationType((1,3,6,1,4,1,6027,3,5,1,2,0,2))
configConflict.setObjects(*((_B,_D),(_B,_E),(_B,_F)))
if mibBuilder.loadTexts:configConflict.setStatus(_A)
configConflictClear=NotificationType((1,3,6,1,4,1,6027,3,5,1,2,0,3))
configConflictClear.setObjects(*((_B,_D),(_B,_E),(_B,_F)))
if mibBuilder.loadTexts:configConflictClear.setStatus(_A)
batchConfigCommitProgress=NotificationType((1,3,6,1,4,1,6027,3,5,1,2,0,4))
batchConfigCommitProgress.setObjects(*((_B,_D),(_B,_E),(_B,_F)))
if mibBuilder.loadTexts:batchConfigCommitProgress.setStatus(_A)
batchConfigCommitCompleted=NotificationType((1,3,6,1,4,1,6027,3,5,1,2,0,5))
batchConfigCommitCompleted.setObjects(*((_B,_D),(_B,_E),(_B,_F)))
if mibBuilder.loadTexts:batchConfigCommitCompleted.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'DellNetConfigFileLocation':DellNetConfigFileLocation,'DellNetConfigFileType':DellNetConfigFileType,'DellNetConfigCopyState':DellNetConfigCopyState,'DellNetConfigCopyFailCause':DellNetConfigCopyFailCause,'dellNetCopyConfigMib':dellNetCopyConfigMib,'dellNetCopyConfigObjects':dellNetCopyConfigObjects,'dellNetCopyConfig':dellNetCopyConfig,'dellNetCopyTable':dellNetCopyTable,'dellNetCopyEntry':dellNetCopyEntry,_J:copyConfigIndex,'copySrcFileType':copySrcFileType,'copySrcFileLocation':copySrcFileLocation,'copySrcFileName':copySrcFileName,'copyDestFileType':copyDestFileType,'copyDestFileLocation':copyDestFileLocation,'copyDestFileName':copyDestFileName,'copyServerAddress':copyServerAddress,'copyUserName':copyUserName,'copyUserPassword':copyUserPassword,'copyState':copyState,'copyTimeStarted':copyTimeStarted,'copyTimeCompleted':copyTimeCompleted,'copyFailCause':copyFailCause,'copyEntryRowStatus':copyEntryRowStatus,'copyServerInetAddressType':copyServerInetAddressType,'copyServerInetAddress':copyServerInetAddress,'dellNetCopyConfigTraps':dellNetCopyConfigTraps,'copyAlarmMibNotifications':copyAlarmMibNotifications,'copyConfigCompleted':copyConfigCompleted,'configConflict':configConflict,'configConflictClear':configConflictClear,'batchConfigCommitProgress':batchConfigCommitProgress,'batchConfigCommitCompleted':batchConfigCommitCompleted,'copyAlarmVariable':copyAlarmVariable,_D:copyAlarmLevel,_E:copyAlarmString,_F:copyAlarmIndex})