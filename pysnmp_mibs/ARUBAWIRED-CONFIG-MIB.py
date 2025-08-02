_g='arubaWiredConfigurationNotificationsGroup'
_f='arubaWiredConfigurationGroup'
_e='arubaWiredConfigurationScalarGroup'
_d='arubaWiredConfigurationNotificationOnCompletion'
_c='arubaWiredConfigurationChangeNotification'
_b='arubaWiredConfigurationCopyEntryRowStatus'
_a='arubaWiredConfigurationCopyNotificationOnCompletion'
_Z='arubaWiredConfigurationCopyVRFName'
_Y='arubaWiredConfigurationCopyUserPassword'
_X='arubaWiredConfigurationCopyUserName'
_W='arubaWiredConfigurationCopyServerAddressType'
_V='arubaWiredConfigurationCopyFileFormat'
_U='arubaWiredConfigurationCheckpointName'
_T='arubaWiredConfigurationCopyDestFileType'
_S='arubaWiredConfigurationCopySourceFileType'
_R='arubaWiredConfigurationCopyProtocol'
_Q='arubaWiredConfigurationChangeNotificationEnable'
_P='arubaWiredConfigurationCopyIndex'
_O='checkpoint'
_N='arubaWiredConfigurationCopyFailureCause'
_M='arubaWiredConfigurationCopyTimeCompleted'
_L='arubaWiredConfigurationCopyTimeStarted'
_K='arubaWiredConfigurationCopyState'
_J='arubaWiredConfigurationCopyServerAddress'
_I='arubaWiredConfigurationCopyFileName'
_H='arubaWiredConfigurationChangeTimestamp'
_G='arubaWiredConfigurationChangeSource'
_F='TruthValue'
_E='DisplayString'
_D='read-only'
_C='read-create'
_B='ARUBAWIRED-CONFIG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
wndFeatures,=mibBuilder.importSymbols('ARUBAWIRED-NETWORKING-OID','wndFeatures')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','RowStatus','TextualConvention','TimeStamp',_F)
arubaWiredConfigurationMIB=ModuleIdentity((1,3,6,1,4,1,47196,4,1,1,3,20))
if mibBuilder.loadTexts:arubaWiredConfigurationMIB.setRevisions(('2021-08-10 00:00',))
class ConfigurationEventMedium(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_O,1),('cli',2),('internal',3),('rest',4),('snmp',5),('ztp',6)))
class ConfigurationCopyProtocol(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('scp',1),('sftp',2),('tftp',3)))
class ConfigurationCopyState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('waiting',1),('running',2),('successful',3),('failed',4)))
class ConfigurationCopyFailureCause(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('authenticationFailed',1),('badFilename',2),('busy',3),('invalidConfiguration',4),('invalidURL',5),('systemNotReady',6),('timeout',7),('unknown',8)))
class ConfigurationFileType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('externalFile',1),('startupConfiguration',2),('runningConfiguration',3),(_O,4)))
class ConfigurationFileFormat(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('cli',1),('json',2)))
_ArubaWiredConfigurationNotifications_ObjectIdentity=ObjectIdentity
arubaWiredConfigurationNotifications=_ArubaWiredConfigurationNotifications_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,20,0))
_ArubaWiredConfigurationObjects_ObjectIdentity=ObjectIdentity
arubaWiredConfigurationObjects=_ArubaWiredConfigurationObjects_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,20,1))
_ArubaWiredConfigurationCopy_ObjectIdentity=ObjectIdentity
arubaWiredConfigurationCopy=_ArubaWiredConfigurationCopy_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,20,1,0))
_ArubaWiredConfigurationCopyTable_Object=MibTable
arubaWiredConfigurationCopyTable=_ArubaWiredConfigurationCopyTable_Object((1,3,6,1,4,1,47196,4,1,1,3,20,1,0,1))
if mibBuilder.loadTexts:arubaWiredConfigurationCopyTable.setStatus(_A)
_ArubaWiredConfigurationCopyEntry_Object=MibTableRow
arubaWiredConfigurationCopyEntry=_ArubaWiredConfigurationCopyEntry_Object((1,3,6,1,4,1,47196,4,1,1,3,20,1,0,1,1))
arubaWiredConfigurationCopyEntry.setIndexNames((0,_B,_P))
if mibBuilder.loadTexts:arubaWiredConfigurationCopyEntry.setStatus(_A)
_ArubaWiredConfigurationCopyIndex_Type=Unsigned32
_ArubaWiredConfigurationCopyIndex_Object=MibTableColumn
arubaWiredConfigurationCopyIndex=_ArubaWiredConfigurationCopyIndex_Object((1,3,6,1,4,1,47196,4,1,1,3,20,1,0,1,1,1),_ArubaWiredConfigurationCopyIndex_Type())
arubaWiredConfigurationCopyIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:arubaWiredConfigurationCopyIndex.setStatus(_A)
_ArubaWiredConfigurationCopySourceFileType_Type=ConfigurationFileType
_ArubaWiredConfigurationCopySourceFileType_Object=MibTableColumn
arubaWiredConfigurationCopySourceFileType=_ArubaWiredConfigurationCopySourceFileType_Object((1,3,6,1,4,1,47196,4,1,1,3,20,1,0,1,1,2),_ArubaWiredConfigurationCopySourceFileType_Type())
arubaWiredConfigurationCopySourceFileType.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredConfigurationCopySourceFileType.setStatus(_A)
_ArubaWiredConfigurationCopyDestFileType_Type=ConfigurationFileType
_ArubaWiredConfigurationCopyDestFileType_Object=MibTableColumn
arubaWiredConfigurationCopyDestFileType=_ArubaWiredConfigurationCopyDestFileType_Object((1,3,6,1,4,1,47196,4,1,1,3,20,1,0,1,1,3),_ArubaWiredConfigurationCopyDestFileType_Type())
arubaWiredConfigurationCopyDestFileType.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredConfigurationCopyDestFileType.setStatus(_A)
_ArubaWiredConfigurationCopyProtocol_Type=ConfigurationCopyProtocol
_ArubaWiredConfigurationCopyProtocol_Object=MibTableColumn
arubaWiredConfigurationCopyProtocol=_ArubaWiredConfigurationCopyProtocol_Object((1,3,6,1,4,1,47196,4,1,1,3,20,1,0,1,1,4),_ArubaWiredConfigurationCopyProtocol_Type())
arubaWiredConfigurationCopyProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredConfigurationCopyProtocol.setStatus(_A)
_ArubaWiredConfigurationCheckpointName_Type=DisplayString
_ArubaWiredConfigurationCheckpointName_Object=MibTableColumn
arubaWiredConfigurationCheckpointName=_ArubaWiredConfigurationCheckpointName_Object((1,3,6,1,4,1,47196,4,1,1,3,20,1,0,1,1,5),_ArubaWiredConfigurationCheckpointName_Type())
arubaWiredConfigurationCheckpointName.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredConfigurationCheckpointName.setStatus(_A)
_ArubaWiredConfigurationCopyFileFormat_Type=ConfigurationFileFormat
_ArubaWiredConfigurationCopyFileFormat_Object=MibTableColumn
arubaWiredConfigurationCopyFileFormat=_ArubaWiredConfigurationCopyFileFormat_Object((1,3,6,1,4,1,47196,4,1,1,3,20,1,0,1,1,6),_ArubaWiredConfigurationCopyFileFormat_Type())
arubaWiredConfigurationCopyFileFormat.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredConfigurationCopyFileFormat.setStatus(_A)
_ArubaWiredConfigurationCopyFileName_Type=DisplayString
_ArubaWiredConfigurationCopyFileName_Object=MibTableColumn
arubaWiredConfigurationCopyFileName=_ArubaWiredConfigurationCopyFileName_Object((1,3,6,1,4,1,47196,4,1,1,3,20,1,0,1,1,7),_ArubaWiredConfigurationCopyFileName_Type())
arubaWiredConfigurationCopyFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredConfigurationCopyFileName.setStatus(_A)
_ArubaWiredConfigurationCopyServerAddressType_Type=InetAddressType
_ArubaWiredConfigurationCopyServerAddressType_Object=MibTableColumn
arubaWiredConfigurationCopyServerAddressType=_ArubaWiredConfigurationCopyServerAddressType_Object((1,3,6,1,4,1,47196,4,1,1,3,20,1,0,1,1,8),_ArubaWiredConfigurationCopyServerAddressType_Type())
arubaWiredConfigurationCopyServerAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredConfigurationCopyServerAddressType.setStatus(_A)
_ArubaWiredConfigurationCopyServerAddress_Type=InetAddress
_ArubaWiredConfigurationCopyServerAddress_Object=MibTableColumn
arubaWiredConfigurationCopyServerAddress=_ArubaWiredConfigurationCopyServerAddress_Object((1,3,6,1,4,1,47196,4,1,1,3,20,1,0,1,1,9),_ArubaWiredConfigurationCopyServerAddress_Type())
arubaWiredConfigurationCopyServerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredConfigurationCopyServerAddress.setStatus(_A)
class _ArubaWiredConfigurationCopyUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,40))
_ArubaWiredConfigurationCopyUserName_Type.__name__=_E
_ArubaWiredConfigurationCopyUserName_Object=MibTableColumn
arubaWiredConfigurationCopyUserName=_ArubaWiredConfigurationCopyUserName_Object((1,3,6,1,4,1,47196,4,1,1,3,20,1,0,1,1,10),_ArubaWiredConfigurationCopyUserName_Type())
arubaWiredConfigurationCopyUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredConfigurationCopyUserName.setStatus(_A)
class _ArubaWiredConfigurationCopyUserPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,40))
_ArubaWiredConfigurationCopyUserPassword_Type.__name__=_E
_ArubaWiredConfigurationCopyUserPassword_Object=MibTableColumn
arubaWiredConfigurationCopyUserPassword=_ArubaWiredConfigurationCopyUserPassword_Object((1,3,6,1,4,1,47196,4,1,1,3,20,1,0,1,1,11),_ArubaWiredConfigurationCopyUserPassword_Type())
arubaWiredConfigurationCopyUserPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredConfigurationCopyUserPassword.setStatus(_A)
_ArubaWiredConfigurationCopyVRFName_Type=DisplayString
_ArubaWiredConfigurationCopyVRFName_Object=MibTableColumn
arubaWiredConfigurationCopyVRFName=_ArubaWiredConfigurationCopyVRFName_Object((1,3,6,1,4,1,47196,4,1,1,3,20,1,0,1,1,12),_ArubaWiredConfigurationCopyVRFName_Type())
arubaWiredConfigurationCopyVRFName.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredConfigurationCopyVRFName.setStatus(_A)
class _ArubaWiredConfigurationCopyNotificationOnCompletion_Type(TruthValue):defaultValue=2
_ArubaWiredConfigurationCopyNotificationOnCompletion_Type.__name__=_F
_ArubaWiredConfigurationCopyNotificationOnCompletion_Object=MibTableColumn
arubaWiredConfigurationCopyNotificationOnCompletion=_ArubaWiredConfigurationCopyNotificationOnCompletion_Object((1,3,6,1,4,1,47196,4,1,1,3,20,1,0,1,1,13),_ArubaWiredConfigurationCopyNotificationOnCompletion_Type())
arubaWiredConfigurationCopyNotificationOnCompletion.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredConfigurationCopyNotificationOnCompletion.setStatus(_A)
_ArubaWiredConfigurationCopyState_Type=ConfigurationCopyState
_ArubaWiredConfigurationCopyState_Object=MibTableColumn
arubaWiredConfigurationCopyState=_ArubaWiredConfigurationCopyState_Object((1,3,6,1,4,1,47196,4,1,1,3,20,1,0,1,1,14),_ArubaWiredConfigurationCopyState_Type())
arubaWiredConfigurationCopyState.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredConfigurationCopyState.setStatus(_A)
_ArubaWiredConfigurationCopyTimeStarted_Type=TimeStamp
_ArubaWiredConfigurationCopyTimeStarted_Object=MibTableColumn
arubaWiredConfigurationCopyTimeStarted=_ArubaWiredConfigurationCopyTimeStarted_Object((1,3,6,1,4,1,47196,4,1,1,3,20,1,0,1,1,15),_ArubaWiredConfigurationCopyTimeStarted_Type())
arubaWiredConfigurationCopyTimeStarted.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredConfigurationCopyTimeStarted.setStatus(_A)
_ArubaWiredConfigurationCopyTimeCompleted_Type=TimeStamp
_ArubaWiredConfigurationCopyTimeCompleted_Object=MibTableColumn
arubaWiredConfigurationCopyTimeCompleted=_ArubaWiredConfigurationCopyTimeCompleted_Object((1,3,6,1,4,1,47196,4,1,1,3,20,1,0,1,1,16),_ArubaWiredConfigurationCopyTimeCompleted_Type())
arubaWiredConfigurationCopyTimeCompleted.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredConfigurationCopyTimeCompleted.setStatus(_A)
_ArubaWiredConfigurationCopyFailureCause_Type=ConfigurationCopyFailureCause
_ArubaWiredConfigurationCopyFailureCause_Object=MibTableColumn
arubaWiredConfigurationCopyFailureCause=_ArubaWiredConfigurationCopyFailureCause_Object((1,3,6,1,4,1,47196,4,1,1,3,20,1,0,1,1,17),_ArubaWiredConfigurationCopyFailureCause_Type())
arubaWiredConfigurationCopyFailureCause.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredConfigurationCopyFailureCause.setStatus(_A)
_ArubaWiredConfigurationCopyEntryRowStatus_Type=RowStatus
_ArubaWiredConfigurationCopyEntryRowStatus_Object=MibTableColumn
arubaWiredConfigurationCopyEntryRowStatus=_ArubaWiredConfigurationCopyEntryRowStatus_Object((1,3,6,1,4,1,47196,4,1,1,3,20,1,0,1,1,18),_ArubaWiredConfigurationCopyEntryRowStatus_Type())
arubaWiredConfigurationCopyEntryRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredConfigurationCopyEntryRowStatus.setStatus(_A)
_ArubaWiredConfigurationChange_ObjectIdentity=ObjectIdentity
arubaWiredConfigurationChange=_ArubaWiredConfigurationChange_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,20,1,1))
class _ArubaWiredConfigurationChangeNotificationEnable_Type(TruthValue):defaultValue=2
_ArubaWiredConfigurationChangeNotificationEnable_Type.__name__=_F
_ArubaWiredConfigurationChangeNotificationEnable_Object=MibScalar
arubaWiredConfigurationChangeNotificationEnable=_ArubaWiredConfigurationChangeNotificationEnable_Object((1,3,6,1,4,1,47196,4,1,1,3,20,1,1,1),_ArubaWiredConfigurationChangeNotificationEnable_Type())
arubaWiredConfigurationChangeNotificationEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:arubaWiredConfigurationChangeNotificationEnable.setStatus(_A)
_ArubaWiredConfigurationChangeSource_Type=ConfigurationEventMedium
_ArubaWiredConfigurationChangeSource_Object=MibScalar
arubaWiredConfigurationChangeSource=_ArubaWiredConfigurationChangeSource_Object((1,3,6,1,4,1,47196,4,1,1,3,20,1,1,2),_ArubaWiredConfigurationChangeSource_Type())
arubaWiredConfigurationChangeSource.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredConfigurationChangeSource.setStatus(_A)
_ArubaWiredConfigurationChangeTimestamp_Type=TimeTicks
_ArubaWiredConfigurationChangeTimestamp_Object=MibScalar
arubaWiredConfigurationChangeTimestamp=_ArubaWiredConfigurationChangeTimestamp_Object((1,3,6,1,4,1,47196,4,1,1,3,20,1,1,3),_ArubaWiredConfigurationChangeTimestamp_Type())
arubaWiredConfigurationChangeTimestamp.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredConfigurationChangeTimestamp.setStatus(_A)
_ArubaWiredConfigurationConformance_ObjectIdentity=ObjectIdentity
arubaWiredConfigurationConformance=_ArubaWiredConfigurationConformance_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,20,2))
_ArubaWiredConfigurationCompliances_ObjectIdentity=ObjectIdentity
arubaWiredConfigurationCompliances=_ArubaWiredConfigurationCompliances_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,20,2,1))
_ArubaWiredConfigurationGroups_ObjectIdentity=ObjectIdentity
arubaWiredConfigurationGroups=_ArubaWiredConfigurationGroups_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,20,2,2))
arubaWiredConfigurationScalarGroup=ObjectGroup((1,3,6,1,4,1,47196,4,1,1,3,20,2,2,1))
arubaWiredConfigurationScalarGroup.setObjects(*((_B,_Q),(_B,_G),(_B,_H)))
if mibBuilder.loadTexts:arubaWiredConfigurationScalarGroup.setStatus(_A)
arubaWiredConfigurationGroup=ObjectGroup((1,3,6,1,4,1,47196,4,1,1,3,20,2,2,2))
arubaWiredConfigurationGroup.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_I),(_B,_W),(_B,_J),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_b)))
if mibBuilder.loadTexts:arubaWiredConfigurationGroup.setStatus(_A)
arubaWiredConfigurationChangeNotification=NotificationType((1,3,6,1,4,1,47196,4,1,1,3,20,0,1))
arubaWiredConfigurationChangeNotification.setObjects(*((_B,_G),(_B,_H)))
if mibBuilder.loadTexts:arubaWiredConfigurationChangeNotification.setStatus(_A)
arubaWiredConfigurationNotificationOnCompletion=NotificationType((1,3,6,1,4,1,47196,4,1,1,3,20,0,2))
arubaWiredConfigurationNotificationOnCompletion.setObjects(*((_B,_J),(_B,_I),(_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:arubaWiredConfigurationNotificationOnCompletion.setStatus(_A)
arubaWiredConfigurationNotificationsGroup=NotificationGroup((1,3,6,1,4,1,47196,4,1,1,3,20,2,2,3))
arubaWiredConfigurationNotificationsGroup.setObjects(*((_B,_c),(_B,_d)))
if mibBuilder.loadTexts:arubaWiredConfigurationNotificationsGroup.setStatus(_A)
arubaWiredConfigurationCompliance=ModuleCompliance((1,3,6,1,4,1,47196,4,1,1,3,20,2,1,1))
arubaWiredConfigurationCompliance.setObjects(*((_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:arubaWiredConfigurationCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ConfigurationEventMedium':ConfigurationEventMedium,'ConfigurationCopyProtocol':ConfigurationCopyProtocol,'ConfigurationCopyState':ConfigurationCopyState,'ConfigurationCopyFailureCause':ConfigurationCopyFailureCause,'ConfigurationFileType':ConfigurationFileType,'ConfigurationFileFormat':ConfigurationFileFormat,'arubaWiredConfigurationMIB':arubaWiredConfigurationMIB,'arubaWiredConfigurationNotifications':arubaWiredConfigurationNotifications,_c:arubaWiredConfigurationChangeNotification,_d:arubaWiredConfigurationNotificationOnCompletion,'arubaWiredConfigurationObjects':arubaWiredConfigurationObjects,'arubaWiredConfigurationCopy':arubaWiredConfigurationCopy,'arubaWiredConfigurationCopyTable':arubaWiredConfigurationCopyTable,'arubaWiredConfigurationCopyEntry':arubaWiredConfigurationCopyEntry,_P:arubaWiredConfigurationCopyIndex,_S:arubaWiredConfigurationCopySourceFileType,_T:arubaWiredConfigurationCopyDestFileType,_R:arubaWiredConfigurationCopyProtocol,_U:arubaWiredConfigurationCheckpointName,_V:arubaWiredConfigurationCopyFileFormat,_I:arubaWiredConfigurationCopyFileName,_W:arubaWiredConfigurationCopyServerAddressType,_J:arubaWiredConfigurationCopyServerAddress,_X:arubaWiredConfigurationCopyUserName,_Y:arubaWiredConfigurationCopyUserPassword,_Z:arubaWiredConfigurationCopyVRFName,_a:arubaWiredConfigurationCopyNotificationOnCompletion,_K:arubaWiredConfigurationCopyState,_L:arubaWiredConfigurationCopyTimeStarted,_M:arubaWiredConfigurationCopyTimeCompleted,_N:arubaWiredConfigurationCopyFailureCause,_b:arubaWiredConfigurationCopyEntryRowStatus,'arubaWiredConfigurationChange':arubaWiredConfigurationChange,_Q:arubaWiredConfigurationChangeNotificationEnable,_G:arubaWiredConfigurationChangeSource,_H:arubaWiredConfigurationChangeTimestamp,'arubaWiredConfigurationConformance':arubaWiredConfigurationConformance,'arubaWiredConfigurationCompliances':arubaWiredConfigurationCompliances,'arubaWiredConfigurationCompliance':arubaWiredConfigurationCompliance,'arubaWiredConfigurationGroups':arubaWiredConfigurationGroups,_e:arubaWiredConfigurationScalarGroup,_f:arubaWiredConfigurationGroup,_g:arubaWiredConfigurationNotificationsGroup})