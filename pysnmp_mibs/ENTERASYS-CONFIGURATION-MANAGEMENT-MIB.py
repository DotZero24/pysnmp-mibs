_i='etsysConfigMgmtNotificationsGroup'
_h='etsysConfigMgmtReadyNotification'
_g='etsysConfigMgmtChangeRowStatus'
_f='etsysConfigMgmtChangeErrorDescription'
_e='etsysConfigMgmtChangeValidationString'
_d='etsysConfigMgmtChangeBytesTransferred'
_c='etsysConfigMgmtChangeCompletionTime'
_b='etsysConfigMgmtChangeEnqueuedTime'
_a='etsysConfigMgmtChangeDelayTime'
_Z='etsysConfigMgmtChangeOperStatus'
_Y='etsysConfigMgmtChangeOperation'
_X='etsysConfigMgmtChangeURL'
_W='etsysConfigMgmtChangeNextAvailableIndex'
_V='etsysConfigMgmtChangeSupportedOperations'
_U='etsysConfigMgmtChangeSupportedURLs'
_T='etsysConfigMgmtChangeCompleted'
_S='etsysConfigMgmtChangeCurrent'
_R='etsysConfigMgmtChangeLimit'
_Q='etsysConfigMgmtPersistentStorageCkSum'
_P='etsysConfigMgmtPersistentStorageStatus'
_O='etsysConfigMgmtCurrentConfigURL'
_N='etsysConfigMgmtCurrentImageURL'
_M='0000000000000000'
_L='etsysConfigMgmtChangeIndex'
_K='SnmpAdminString'
_J='etsysConfigMgmtChangeGroup'
_I='etsysConfigMgmtStatusGroup'
_H='DateAndTime'
_G='Integer32'
_F='read-create'
_E='Unsigned32'
_D='DisplayString'
_C='read-only'
_B='ENTERASYS-CONFIGURATION-MANAGEMENT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_K)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_H,_D,'PhysAddress','RowStatus','TextualConvention')
etsysConfigurationManagementMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,16))
if mibBuilder.loadTexts:etsysConfigurationManagementMIB.setRevisions(('2013-02-04 16:00','2008-12-05 14:13','2002-10-03 20:21','2002-09-30 17:02','2001-12-03 19:49'))
class ConfigMgmtOperations(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('resetHardware',0),('resetSoftware',1),('imageDownload',2),('imageDownloadNonPersistent',3),('configurationReset',4),('configurationUpload',5),('configurationDownload',6),('imageSetSelected',7),('imageGetSelected',8),('configurationActivate',9),('configurationAppend',10),('configurationPersist',11),('configurationParse',12),('validationMD5sum',13),('bootPromDownload',14)))
_EtsysConfigMgmtNotifications_ObjectIdentity=ObjectIdentity
etsysConfigMgmtNotifications=_EtsysConfigMgmtNotifications_ObjectIdentity((1,3,6,1,4,1,5624,1,2,16,0))
_EtsysConfigMgmtStatus_ObjectIdentity=ObjectIdentity
etsysConfigMgmtStatus=_EtsysConfigMgmtStatus_ObjectIdentity((1,3,6,1,4,1,5624,1,2,16,1))
class _EtsysConfigMgmtCurrentImageURL_Type(DisplayString):defaultHexValue=''
_EtsysConfigMgmtCurrentImageURL_Type.__name__=_D
_EtsysConfigMgmtCurrentImageURL_Object=MibScalar
etsysConfigMgmtCurrentImageURL=_EtsysConfigMgmtCurrentImageURL_Object((1,3,6,1,4,1,5624,1,2,16,1,1),_EtsysConfigMgmtCurrentImageURL_Type())
etsysConfigMgmtCurrentImageURL.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysConfigMgmtCurrentImageURL.setStatus(_A)
class _EtsysConfigMgmtCurrentConfigURL_Type(DisplayString):defaultHexValue=''
_EtsysConfigMgmtCurrentConfigURL_Type.__name__=_D
_EtsysConfigMgmtCurrentConfigURL_Object=MibScalar
etsysConfigMgmtCurrentConfigURL=_EtsysConfigMgmtCurrentConfigURL_Object((1,3,6,1,4,1,5624,1,2,16,1,2),_EtsysConfigMgmtCurrentConfigURL_Type())
etsysConfigMgmtCurrentConfigURL.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysConfigMgmtCurrentConfigURL.setStatus(_A)
class _EtsysConfigMgmtPersistentStorageStatus_Type(DisplayString):defaultHexValue=''
_EtsysConfigMgmtPersistentStorageStatus_Type.__name__=_D
_EtsysConfigMgmtPersistentStorageStatus_Object=MibScalar
etsysConfigMgmtPersistentStorageStatus=_EtsysConfigMgmtPersistentStorageStatus_Object((1,3,6,1,4,1,5624,1,2,16,1,3),_EtsysConfigMgmtPersistentStorageStatus_Type())
etsysConfigMgmtPersistentStorageStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysConfigMgmtPersistentStorageStatus.setStatus(_A)
class _EtsysConfigMgmtPersistentStorageCkSum_Type(DisplayString):defaultHexValue=''
_EtsysConfigMgmtPersistentStorageCkSum_Type.__name__=_D
_EtsysConfigMgmtPersistentStorageCkSum_Object=MibScalar
etsysConfigMgmtPersistentStorageCkSum=_EtsysConfigMgmtPersistentStorageCkSum_Object((1,3,6,1,4,1,5624,1,2,16,1,4),_EtsysConfigMgmtPersistentStorageCkSum_Type())
etsysConfigMgmtPersistentStorageCkSum.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysConfigMgmtPersistentStorageCkSum.setStatus(_A)
_EtsysConfigMgmtChange_ObjectIdentity=ObjectIdentity
etsysConfigMgmtChange=_EtsysConfigMgmtChange_ObjectIdentity((1,3,6,1,4,1,5624,1,2,16,2))
class _EtsysConfigMgmtChangeLimit_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_EtsysConfigMgmtChangeLimit_Type.__name__=_E
_EtsysConfigMgmtChangeLimit_Object=MibScalar
etsysConfigMgmtChangeLimit=_EtsysConfigMgmtChangeLimit_Object((1,3,6,1,4,1,5624,1,2,16,2,1),_EtsysConfigMgmtChangeLimit_Type())
etsysConfigMgmtChangeLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysConfigMgmtChangeLimit.setStatus(_A)
_EtsysConfigMgmtChangeCurrent_Type=Gauge32
_EtsysConfigMgmtChangeCurrent_Object=MibScalar
etsysConfigMgmtChangeCurrent=_EtsysConfigMgmtChangeCurrent_Object((1,3,6,1,4,1,5624,1,2,16,2,2),_EtsysConfigMgmtChangeCurrent_Type())
etsysConfigMgmtChangeCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysConfigMgmtChangeCurrent.setStatus(_A)
_EtsysConfigMgmtChangeCompleted_Type=Counter32
_EtsysConfigMgmtChangeCompleted_Object=MibScalar
etsysConfigMgmtChangeCompleted=_EtsysConfigMgmtChangeCompleted_Object((1,3,6,1,4,1,5624,1,2,16,2,3),_EtsysConfigMgmtChangeCompleted_Type())
etsysConfigMgmtChangeCompleted.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysConfigMgmtChangeCompleted.setStatus(_A)
class _EtsysConfigMgmtChangeSupportedURLs_Type(Bits):namedValues=NamedValues(*(('etsysConfigMgmtFtp',0),('etsysConfigMgmtRcp',1),('etsysConfigMgmtHttp',2),('etsysConfigMgmtTftp',3),('etsysConfigMgmtFile',4),('etsysConfigMgmtBootP',5),('etsysConfigMgmtScp',6)))
_EtsysConfigMgmtChangeSupportedURLs_Type.__name__='Bits'
_EtsysConfigMgmtChangeSupportedURLs_Object=MibScalar
etsysConfigMgmtChangeSupportedURLs=_EtsysConfigMgmtChangeSupportedURLs_Object((1,3,6,1,4,1,5624,1,2,16,2,4),_EtsysConfigMgmtChangeSupportedURLs_Type())
etsysConfigMgmtChangeSupportedURLs.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysConfigMgmtChangeSupportedURLs.setStatus(_A)
_EtsysConfigMgmtChangeSupportedOperations_Type=ConfigMgmtOperations
_EtsysConfigMgmtChangeSupportedOperations_Object=MibScalar
etsysConfigMgmtChangeSupportedOperations=_EtsysConfigMgmtChangeSupportedOperations_Object((1,3,6,1,4,1,5624,1,2,16,2,5),_EtsysConfigMgmtChangeSupportedOperations_Type())
etsysConfigMgmtChangeSupportedOperations.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysConfigMgmtChangeSupportedOperations.setStatus(_A)
class _EtsysConfigMgmtChangeNextAvailableIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_EtsysConfigMgmtChangeNextAvailableIndex_Type.__name__=_E
_EtsysConfigMgmtChangeNextAvailableIndex_Object=MibScalar
etsysConfigMgmtChangeNextAvailableIndex=_EtsysConfigMgmtChangeNextAvailableIndex_Object((1,3,6,1,4,1,5624,1,2,16,2,6),_EtsysConfigMgmtChangeNextAvailableIndex_Type())
etsysConfigMgmtChangeNextAvailableIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysConfigMgmtChangeNextAvailableIndex.setStatus(_A)
_EtsysConfigMgmtChangeTable_Object=MibTable
etsysConfigMgmtChangeTable=_EtsysConfigMgmtChangeTable_Object((1,3,6,1,4,1,5624,1,2,16,2,7))
if mibBuilder.loadTexts:etsysConfigMgmtChangeTable.setStatus(_A)
_EtsysConfigMgmtChangeEntry_Object=MibTableRow
etsysConfigMgmtChangeEntry=_EtsysConfigMgmtChangeEntry_Object((1,3,6,1,4,1,5624,1,2,16,2,7,1))
etsysConfigMgmtChangeEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:etsysConfigMgmtChangeEntry.setStatus(_A)
class _EtsysConfigMgmtChangeIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_EtsysConfigMgmtChangeIndex_Type.__name__=_E
_EtsysConfigMgmtChangeIndex_Object=MibTableColumn
etsysConfigMgmtChangeIndex=_EtsysConfigMgmtChangeIndex_Object((1,3,6,1,4,1,5624,1,2,16,2,7,1,1),_EtsysConfigMgmtChangeIndex_Type())
etsysConfigMgmtChangeIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:etsysConfigMgmtChangeIndex.setStatus(_A)
class _EtsysConfigMgmtChangeURL_Type(DisplayString):defaultHexValue=''
_EtsysConfigMgmtChangeURL_Type.__name__=_D
_EtsysConfigMgmtChangeURL_Object=MibTableColumn
etsysConfigMgmtChangeURL=_EtsysConfigMgmtChangeURL_Object((1,3,6,1,4,1,5624,1,2,16,2,7,1,2),_EtsysConfigMgmtChangeURL_Type())
etsysConfigMgmtChangeURL.setMaxAccess(_F)
if mibBuilder.loadTexts:etsysConfigMgmtChangeURL.setStatus(_A)
_EtsysConfigMgmtChangeOperation_Type=ConfigMgmtOperations
_EtsysConfigMgmtChangeOperation_Object=MibTableColumn
etsysConfigMgmtChangeOperation=_EtsysConfigMgmtChangeOperation_Object((1,3,6,1,4,1,5624,1,2,16,2,7,1,3),_EtsysConfigMgmtChangeOperation_Type())
etsysConfigMgmtChangeOperation.setMaxAccess(_F)
if mibBuilder.loadTexts:etsysConfigMgmtChangeOperation.setStatus(_A)
class _EtsysConfigMgmtChangeOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('inactive',1),('pending',2),('running',3),('success',4),('failure',5)))
_EtsysConfigMgmtChangeOperStatus_Type.__name__=_G
_EtsysConfigMgmtChangeOperStatus_Object=MibTableColumn
etsysConfigMgmtChangeOperStatus=_EtsysConfigMgmtChangeOperStatus_Object((1,3,6,1,4,1,5624,1,2,16,2,7,1,4),_EtsysConfigMgmtChangeOperStatus_Type())
etsysConfigMgmtChangeOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysConfigMgmtChangeOperStatus.setStatus(_A)
class _EtsysConfigMgmtChangeDelayTime_Type(Unsigned32):defaultValue=0
_EtsysConfigMgmtChangeDelayTime_Type.__name__=_E
_EtsysConfigMgmtChangeDelayTime_Object=MibTableColumn
etsysConfigMgmtChangeDelayTime=_EtsysConfigMgmtChangeDelayTime_Object((1,3,6,1,4,1,5624,1,2,16,2,7,1,5),_EtsysConfigMgmtChangeDelayTime_Type())
etsysConfigMgmtChangeDelayTime.setMaxAccess(_F)
if mibBuilder.loadTexts:etsysConfigMgmtChangeDelayTime.setStatus(_A)
if mibBuilder.loadTexts:etsysConfigMgmtChangeDelayTime.setUnits('seconds')
class _EtsysConfigMgmtChangeEnqueuedTime_Type(DateAndTime):defaultHexValue=_M
_EtsysConfigMgmtChangeEnqueuedTime_Type.__name__=_H
_EtsysConfigMgmtChangeEnqueuedTime_Object=MibTableColumn
etsysConfigMgmtChangeEnqueuedTime=_EtsysConfigMgmtChangeEnqueuedTime_Object((1,3,6,1,4,1,5624,1,2,16,2,7,1,6),_EtsysConfigMgmtChangeEnqueuedTime_Type())
etsysConfigMgmtChangeEnqueuedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysConfigMgmtChangeEnqueuedTime.setStatus(_A)
class _EtsysConfigMgmtChangeCompletionTime_Type(DateAndTime):defaultHexValue=_M
_EtsysConfigMgmtChangeCompletionTime_Type.__name__=_H
_EtsysConfigMgmtChangeCompletionTime_Object=MibTableColumn
etsysConfigMgmtChangeCompletionTime=_EtsysConfigMgmtChangeCompletionTime_Object((1,3,6,1,4,1,5624,1,2,16,2,7,1,7),_EtsysConfigMgmtChangeCompletionTime_Type())
etsysConfigMgmtChangeCompletionTime.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysConfigMgmtChangeCompletionTime.setStatus(_A)
class _EtsysConfigMgmtChangeBytesTransferred_Type(Integer32):defaultValue=0
_EtsysConfigMgmtChangeBytesTransferred_Type.__name__=_G
_EtsysConfigMgmtChangeBytesTransferred_Object=MibTableColumn
etsysConfigMgmtChangeBytesTransferred=_EtsysConfigMgmtChangeBytesTransferred_Object((1,3,6,1,4,1,5624,1,2,16,2,7,1,8),_EtsysConfigMgmtChangeBytesTransferred_Type())
etsysConfigMgmtChangeBytesTransferred.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysConfigMgmtChangeBytesTransferred.setStatus(_A)
class _EtsysConfigMgmtChangeValidationString_Type(DisplayString):defaultHexValue=''
_EtsysConfigMgmtChangeValidationString_Type.__name__=_D
_EtsysConfigMgmtChangeValidationString_Object=MibTableColumn
etsysConfigMgmtChangeValidationString=_EtsysConfigMgmtChangeValidationString_Object((1,3,6,1,4,1,5624,1,2,16,2,7,1,9),_EtsysConfigMgmtChangeValidationString_Type())
etsysConfigMgmtChangeValidationString.setMaxAccess(_F)
if mibBuilder.loadTexts:etsysConfigMgmtChangeValidationString.setStatus(_A)
class _EtsysConfigMgmtChangeErrorDescription_Type(SnmpAdminString):defaultHexValue=''
_EtsysConfigMgmtChangeErrorDescription_Type.__name__=_K
_EtsysConfigMgmtChangeErrorDescription_Object=MibTableColumn
etsysConfigMgmtChangeErrorDescription=_EtsysConfigMgmtChangeErrorDescription_Object((1,3,6,1,4,1,5624,1,2,16,2,7,1,10),_EtsysConfigMgmtChangeErrorDescription_Type())
etsysConfigMgmtChangeErrorDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysConfigMgmtChangeErrorDescription.setStatus(_A)
_EtsysConfigMgmtChangeRowStatus_Type=RowStatus
_EtsysConfigMgmtChangeRowStatus_Object=MibTableColumn
etsysConfigMgmtChangeRowStatus=_EtsysConfigMgmtChangeRowStatus_Object((1,3,6,1,4,1,5624,1,2,16,2,7,1,11),_EtsysConfigMgmtChangeRowStatus_Type())
etsysConfigMgmtChangeRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:etsysConfigMgmtChangeRowStatus.setStatus(_A)
_EtsysConfigMgmtConformance_ObjectIdentity=ObjectIdentity
etsysConfigMgmtConformance=_EtsysConfigMgmtConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,16,3))
_EtsysConfigMgmtGroups_ObjectIdentity=ObjectIdentity
etsysConfigMgmtGroups=_EtsysConfigMgmtGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,16,3,1))
_EtsysConfigMgmtCompliances_ObjectIdentity=ObjectIdentity
etsysConfigMgmtCompliances=_EtsysConfigMgmtCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,16,3,2))
etsysConfigMgmtStatusGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,16,3,1,1))
etsysConfigMgmtStatusGroup.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:etsysConfigMgmtStatusGroup.setStatus(_A)
etsysConfigMgmtChangeGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,16,3,1,2))
etsysConfigMgmtChangeGroup.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:etsysConfigMgmtChangeGroup.setStatus(_A)
etsysConfigMgmtReadyNotification=NotificationType((1,3,6,1,4,1,5624,1,2,16,0,1))
if mibBuilder.loadTexts:etsysConfigMgmtReadyNotification.setStatus(_A)
etsysConfigMgmtNotificationsGroup=NotificationGroup((1,3,6,1,4,1,5624,1,2,16,3,1,3))
etsysConfigMgmtNotificationsGroup.setObjects((_B,_h))
if mibBuilder.loadTexts:etsysConfigMgmtNotificationsGroup.setStatus(_A)
etsysConfigMgmtCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,16,3,2,1))
etsysConfigMgmtCompliance.setObjects(*((_B,_I),(_B,_J)))
if mibBuilder.loadTexts:etsysConfigMgmtCompliance.setStatus('deprecated')
etsysConfigMgmtCompliance2=ModuleCompliance((1,3,6,1,4,1,5624,1,2,16,3,2,2))
etsysConfigMgmtCompliance2.setObjects(*((_B,_I),(_B,_J),(_B,_i)))
if mibBuilder.loadTexts:etsysConfigMgmtCompliance2.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ConfigMgmtOperations':ConfigMgmtOperations,'etsysConfigurationManagementMIB':etsysConfigurationManagementMIB,'etsysConfigMgmtNotifications':etsysConfigMgmtNotifications,_h:etsysConfigMgmtReadyNotification,'etsysConfigMgmtStatus':etsysConfigMgmtStatus,_N:etsysConfigMgmtCurrentImageURL,_O:etsysConfigMgmtCurrentConfigURL,_P:etsysConfigMgmtPersistentStorageStatus,_Q:etsysConfigMgmtPersistentStorageCkSum,'etsysConfigMgmtChange':etsysConfigMgmtChange,_R:etsysConfigMgmtChangeLimit,_S:etsysConfigMgmtChangeCurrent,_T:etsysConfigMgmtChangeCompleted,_U:etsysConfigMgmtChangeSupportedURLs,_V:etsysConfigMgmtChangeSupportedOperations,_W:etsysConfigMgmtChangeNextAvailableIndex,'etsysConfigMgmtChangeTable':etsysConfigMgmtChangeTable,'etsysConfigMgmtChangeEntry':etsysConfigMgmtChangeEntry,_L:etsysConfigMgmtChangeIndex,_X:etsysConfigMgmtChangeURL,_Y:etsysConfigMgmtChangeOperation,_Z:etsysConfigMgmtChangeOperStatus,_a:etsysConfigMgmtChangeDelayTime,_b:etsysConfigMgmtChangeEnqueuedTime,_c:etsysConfigMgmtChangeCompletionTime,_d:etsysConfigMgmtChangeBytesTransferred,_e:etsysConfigMgmtChangeValidationString,_f:etsysConfigMgmtChangeErrorDescription,_g:etsysConfigMgmtChangeRowStatus,'etsysConfigMgmtConformance':etsysConfigMgmtConformance,'etsysConfigMgmtGroups':etsysConfigMgmtGroups,_I:etsysConfigMgmtStatusGroup,_J:etsysConfigMgmtChangeGroup,_i:etsysConfigMgmtNotificationsGroup,'etsysConfigMgmtCompliances':etsysConfigMgmtCompliances,'etsysConfigMgmtCompliance':etsysConfigMgmtCompliance,'etsysConfigMgmtCompliance2':etsysConfigMgmtCompliance2})