_O='copyFailCause'
_N='copyTimeCompleted'
_M='copyTimeStarted'
_L='copyState'
_K='copySrcFileName'
_J='copyServerAddress'
_I='ConfigCopyProtocol'
_H='copyIndex'
_G='TruthValue'
_F='Unsigned32'
_E='read-only'
_D='DisplayString'
_C='CONFIG-COPY-MIB'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','RowStatus','TextualConvention','TimeStamp',_G)
mgmt,=mibBuilder.importSymbols('ZXR10-SMI','mgmt')
configCopyMIB=ModuleIdentity((1,3,6,1,4,1,3902,3,202,1))
if mibBuilder.loadTexts:configCopyMIB.setRevisions(('2007-02-01 00:00',))
class ConfigCopyProtocol(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('tftp',1),('ftp',2)))
class ConfigCopyState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('waiting',1),('running',2),('successful',3),('failed',4)))
class ConfigCopyFailCause(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('unknown',1),('badFileName',2),('timeout',3),('noMem',4),('noConfig',5),('unsupportedProtocol',6),('someConfigApplyFailed',7)))
class ConfigFileType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('networkFile',1),('localFile',2),('startupConfig',3),('runningConfig',4)))
_ConfigCopyMIBObjects_ObjectIdentity=ObjectIdentity
configCopyMIBObjects=_ConfigCopyMIBObjects_ObjectIdentity((1,3,6,1,4,1,3902,3,202,1,1))
_Copy_ObjectIdentity=ObjectIdentity
copy=_Copy_ObjectIdentity((1,3,6,1,4,1,3902,3,202,1,1,1))
_CopyTable_Object=MibTable
copyTable=_CopyTable_Object((1,3,6,1,4,1,3902,3,202,1,1,1,1))
if mibBuilder.loadTexts:copyTable.setStatus(_A)
_CopyEntry_Object=MibTableRow
copyEntry=_CopyEntry_Object((1,3,6,1,4,1,3902,3,202,1,1,1,1,1))
copyEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:copyEntry.setStatus(_A)
class _CopyIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CopyIndex_Type.__name__=_F
_CopyIndex_Object=MibTableColumn
copyIndex=_CopyIndex_Object((1,3,6,1,4,1,3902,3,202,1,1,1,1,1,1),_CopyIndex_Type())
copyIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:copyIndex.setStatus(_A)
class _CopyProtocol_Type(ConfigCopyProtocol):defaultValue=2
_CopyProtocol_Type.__name__=_I
_CopyProtocol_Object=MibTableColumn
copyProtocol=_CopyProtocol_Object((1,3,6,1,4,1,3902,3,202,1,1,1,1,1,2),_CopyProtocol_Type())
copyProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:copyProtocol.setStatus(_A)
_CopySourceFileType_Type=ConfigFileType
_CopySourceFileType_Object=MibTableColumn
copySourceFileType=_CopySourceFileType_Object((1,3,6,1,4,1,3902,3,202,1,1,1,1,1,3),_CopySourceFileType_Type())
copySourceFileType.setMaxAccess(_B)
if mibBuilder.loadTexts:copySourceFileType.setStatus(_A)
_CopyDestFileType_Type=ConfigFileType
_CopyDestFileType_Object=MibTableColumn
copyDestFileType=_CopyDestFileType_Object((1,3,6,1,4,1,3902,3,202,1,1,1,1,1,4),_CopyDestFileType_Type())
copyDestFileType.setMaxAccess(_B)
if mibBuilder.loadTexts:copyDestFileType.setStatus(_A)
_CopyServerAddress_Type=IpAddress
_CopyServerAddress_Object=MibTableColumn
copyServerAddress=_CopyServerAddress_Object((1,3,6,1,4,1,3902,3,202,1,1,1,1,1,5),_CopyServerAddress_Type())
copyServerAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:copyServerAddress.setStatus(_A)
class _CopySrcFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_CopySrcFileName_Type.__name__=_D
_CopySrcFileName_Object=MibTableColumn
copySrcFileName=_CopySrcFileName_Object((1,3,6,1,4,1,3902,3,202,1,1,1,1,1,6),_CopySrcFileName_Type())
copySrcFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:copySrcFileName.setStatus(_A)
class _CopyDstFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_CopyDstFileName_Type.__name__=_D
_CopyDstFileName_Object=MibTableColumn
copyDstFileName=_CopyDstFileName_Object((1,3,6,1,4,1,3902,3,202,1,1,1,1,1,7),_CopyDstFileName_Type())
copyDstFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:copyDstFileName.setStatus(_A)
class _CopyUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,40))
_CopyUserName_Type.__name__=_D
_CopyUserName_Object=MibTableColumn
copyUserName=_CopyUserName_Object((1,3,6,1,4,1,3902,3,202,1,1,1,1,1,8),_CopyUserName_Type())
copyUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:copyUserName.setStatus(_A)
class _CopyUserPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,40))
_CopyUserPassword_Type.__name__=_D
_CopyUserPassword_Object=MibTableColumn
copyUserPassword=_CopyUserPassword_Object((1,3,6,1,4,1,3902,3,202,1,1,1,1,1,9),_CopyUserPassword_Type())
copyUserPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:copyUserPassword.setStatus(_A)
class _CopyNotificationOnCompletion_Type(TruthValue):defaultValue=2
_CopyNotificationOnCompletion_Type.__name__=_G
_CopyNotificationOnCompletion_Object=MibTableColumn
copyNotificationOnCompletion=_CopyNotificationOnCompletion_Object((1,3,6,1,4,1,3902,3,202,1,1,1,1,1,10),_CopyNotificationOnCompletion_Type())
copyNotificationOnCompletion.setMaxAccess(_B)
if mibBuilder.loadTexts:copyNotificationOnCompletion.setStatus(_A)
_CopyState_Type=ConfigCopyState
_CopyState_Object=MibTableColumn
copyState=_CopyState_Object((1,3,6,1,4,1,3902,3,202,1,1,1,1,1,11),_CopyState_Type())
copyState.setMaxAccess(_E)
if mibBuilder.loadTexts:copyState.setStatus(_A)
_CopyTimeStarted_Type=TimeStamp
_CopyTimeStarted_Object=MibTableColumn
copyTimeStarted=_CopyTimeStarted_Object((1,3,6,1,4,1,3902,3,202,1,1,1,1,1,12),_CopyTimeStarted_Type())
copyTimeStarted.setMaxAccess(_E)
if mibBuilder.loadTexts:copyTimeStarted.setStatus(_A)
_CopyTimeCompleted_Type=TimeStamp
_CopyTimeCompleted_Object=MibTableColumn
copyTimeCompleted=_CopyTimeCompleted_Object((1,3,6,1,4,1,3902,3,202,1,1,1,1,1,13),_CopyTimeCompleted_Type())
copyTimeCompleted.setMaxAccess(_E)
if mibBuilder.loadTexts:copyTimeCompleted.setStatus(_A)
_CopyFailCause_Type=ConfigCopyFailCause
_CopyFailCause_Object=MibTableColumn
copyFailCause=_CopyFailCause_Object((1,3,6,1,4,1,3902,3,202,1,1,1,1,1,14),_CopyFailCause_Type())
copyFailCause.setMaxAccess(_E)
if mibBuilder.loadTexts:copyFailCause.setStatus(_A)
_CopyEntryRowStatus_Type=RowStatus
_CopyEntryRowStatus_Object=MibTableColumn
copyEntryRowStatus=_CopyEntryRowStatus_Object((1,3,6,1,4,1,3902,3,202,1,1,1,1,1,15),_CopyEntryRowStatus_Type())
copyEntryRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:copyEntryRowStatus.setStatus(_A)
_ConfigCopyMIBTrapPrefix_ObjectIdentity=ObjectIdentity
configCopyMIBTrapPrefix=_ConfigCopyMIBTrapPrefix_ObjectIdentity((1,3,6,1,4,1,3902,3,202,1,2))
_CopyMIBTraps_ObjectIdentity=ObjectIdentity
copyMIBTraps=_CopyMIBTraps_ObjectIdentity((1,3,6,1,4,1,3902,3,202,1,2,1))
copyCompletion=NotificationType((1,3,6,1,4,1,3902,3,202,1,2,1,1))
copyCompletion.setObjects(*((_C,_J),(_C,_K),(_C,_L),(_C,_M),(_C,_N),(_C,_O)))
if mibBuilder.loadTexts:copyCompletion.setStatus(_A)
mibBuilder.exportSymbols(_C,**{_I:ConfigCopyProtocol,'ConfigCopyState':ConfigCopyState,'ConfigCopyFailCause':ConfigCopyFailCause,'ConfigFileType':ConfigFileType,'configCopyMIB':configCopyMIB,'configCopyMIBObjects':configCopyMIBObjects,'copy':copy,'copyTable':copyTable,'copyEntry':copyEntry,_H:copyIndex,'copyProtocol':copyProtocol,'copySourceFileType':copySourceFileType,'copyDestFileType':copyDestFileType,_J:copyServerAddress,_K:copySrcFileName,'copyDstFileName':copyDstFileName,'copyUserName':copyUserName,'copyUserPassword':copyUserPassword,'copyNotificationOnCompletion':copyNotificationOnCompletion,_L:copyState,_M:copyTimeStarted,_N:copyTimeCompleted,_O:copyFailCause,'copyEntryRowStatus':copyEntryRowStatus,'configCopyMIBTrapPrefix':configCopyMIBTrapPrefix,'copyMIBTraps':copyMIBTraps,'copyCompletion':copyCompletion})