_B8='clmgmtLicenseRTUUsageNotifGroup'
_B7='clmgmtLicenseRTUGroup'
_B6='clmgmtLicenseSubscriptionUsageNotifGroup'
_B5='clmgmtLicenseSubscriptionGroup'
_B4='clmgmtLicenseEvalRTUTransition'
_B3='clmgmtLicenseEvalRTUTransitionWarning'
_B2='clmgmtLicenseSubscriptionExpired'
_B1='clmgmtLicenseSubscriptionExtExpiryWarning'
_B0='clmgmtLicenseSubscriptionExpiryWarning'
_A_='clmgmtLicenseNotEnforced'
_Az='clmgmtLicenseEULAAccepted'
_Ay='clmgmtLicenseRevoked'
_Ax='clmgmtLicenseCleared'
_Aw='clmgmtLicenseInstalled'
_Av='clmgmtLicenseUsageCountAboutToExceed'
_Au='clmgmtLicenseUsageCountExceeded'
_At='clmgmtLicenseExpiryWarning'
_As='clmgmtLicenseExpired'
_Ar='clmgmtFeaturePeriodUsed'
_Aq='clmgmtLicensePeriodUsed'
_Ap='clmgmtFeatureStartDate'
_Ao='clmgmtLicenseEndDate'
_An='clmgmtLicenseStartDate'
_Am='clmgmtLicenseErrorNotifEnable'
_Al='clmgmtLicenseDeploymentNotifEnable'
_Ak='clmgmtLicenseUsageNotifEnable'
_Aj='clmgmtDevCredRowStatus'
_Ai='clmgmtDevCredStorageType'
_Ah='clmgmtDevCredCommandFailCause'
_Ag='clmgmtDevCredCommandState'
_Af='clmgmtDevCredCommand'
_Ae='clmgmtDevCredExportFile'
_Ad='clmgmtDevCredServerPassword'
_Ac='clmgmtDevCredServerUsername'
_Ab='clmgmtDevCredServerAddress'
_Aa='clmgmtDevCredServerAddressType'
_AZ='clmgmtDevCredTransferProtocol'
_AY='clmgmtDevCredEntPhysicalIndex'
_AX='clmgmtNextFreeDevCredExportActionIndex'
_AW='clmgmtLicenseStatus'
_AV='clmgmtLicenseEULAStatus'
_AU='clmgmtLicenseExpiredPeriod'
_AT='clmgmtLicenseValidityPeriodRemaining'
_AS='clmgmtLicenseValidityPeriod'
_AR='clmgmtLicenseCounted'
_AQ='clmgmtDefaultLicenseStore'
_AP='clmgmtLicenseStoreSizeRemaining'
_AO='clmgmtLicenseStoreTotalSize'
_AN='clmgmtLicenseStoreName'
_AM='clmgmtLicenseEULAFile'
_AL='clmgmtLicenseAcceptEULA'
_AK='clmgmtLicenseIndivActionFailCause'
_AJ='clmgmtLicenseIndivActionState'
_AI='clmgmtLicenseActionRowStatus'
_AH='clmgmtLicenseActionStorageType'
_AG='clmgmtLicenseActionFailCause'
_AF='clmgmtLicenseJobQPosition'
_AE='clmgmtLicenseActionState'
_AD='clmgmtLicenseAction'
_AC='clmgmtLicenseStopOnFailure'
_AB='clmgmtLicenseBackupFile'
_AA='clmgmtLicenseRehostTicketFile'
_A9='clmgmtLicensePermissionTicketFile'
_A8='clmgmtLicenseActionLicenseIndex'
_A7='clmgmtLicenseStore'
_A6='clmgmtLicenseFile'
_A5='clmgmtLicenseServerPassword'
_A4='clmgmtLicenseServerUsername'
_A3='clmgmtLicenseServerAddress'
_A2='clmgmtLicenseServerAddressType'
_A1='clmgmtLicenseActionTransferProtocol'
_A0='clmgmtLicenseActionEntPhysicalIndex'
_z='clmgmtNextFreeLicenseActionIndex'
_y='clmgmtDevCredExportActionIndex'
_x='clmgmtFeatureIndex'
_w='clmgmtLicenseIndex'
_v='clmgmtLicenseStoreUsed'
_u='clmgmtLicenseStoreIndex'
_t='clmgmtLicenseNumber'
_s='ClmgmtLicenseIndexOrZero'
_r='unrecognizedEntPhysicalIndex'
_q='fileServerNotReachable'
_p='transferProtocolNotSupported'
_o='clmgmtLicenseStoreInformationGroup'
_n='clmgmtLicenseErrorNotifGroup'
_m='clmgmtLicenseDeploymentNotifGroup'
_l='clmgmtLicenseUsageNotifGroup'
_k='clmgmtLicenseNotificationEnableGroup'
_j='clmgmtLicenseDevCredGroup'
_i='clmgmtLicensableFeatureInformationGroup'
_h='clmgmtLicenseInformationGroup'
_g='clmgmtLicenseDeviceInformationGroup'
_f='clmgmtLicenseDeploymentGroup'
_e='clmgmtLicenseUsageCountRemaining'
_d='ClmgmtLicenseTransferProtocol'
_c='clmgmtLicenseActionIndex'
_b='StorageType'
_a='InetAddressType'
_Z='InetAddress'
_Y='PhysicalIndexOrZero'
_X='clmgmtFeatureWhatIsCounted'
_W='clmgmtFeatureValidityPeriodRemaining'
_V='clmgmtLicenseMaxUsageCount'
_U='read-write'
_T='none'
_S='clmgmtFeatureEndDate'
_R='clmgmtLicenseType'
_Q='entPhysicalIndex'
_P='ENTITY-MIB'
_O='seconds'
_N='TruthValue'
_M='Integer32'
_L='clmgmtLicenseComments'
_K='clmgmtLicenseFeatureVersion'
_J='clmgmtLicenseFeatureName'
_I='not-accessible'
_H='Unsigned32'
_G='clmgmtFeatureVersion'
_F='clmgmtFeatureName'
_E='SnmpAdminString'
_D='read-create'
_C='read-only'
_B='current'
_A='CISCO-LICENSE-MGMT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
PhysicalIndexOrZero,entPhysicalIndex=mibBuilder.importSymbols(_P,_Y,_Q)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_Z,_a)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_M,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus',_b,'TextualConvention',_N)
ciscoLicenseMgmtMIB=ModuleIdentity((1,3,6,1,4,1,9,9,543))
if mibBuilder.loadTexts:ciscoLicenseMgmtMIB.setRevisions(('2012-04-19 00:00','2011-04-19 00:00','2008-11-21 00:00','2006-10-03 00:00'))
class ClmgmtLicenseIndex(TextualConvention,Unsigned32):status=_B;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
class ClmgmtLicenseIndexOrZero(TextualConvention,Unsigned32):status=_B
class ClmgmtLicenseTransferProtocol(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_T,1),('local',2),('tftp',3),('ftp',4),('rcp',5),('http',6),('scp',7),('sftp',8)))
class ClmgmtLicenseActionState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_T,1),('pending',2),('inProgress',3),('successful',4),('partiallySuccessful',5),('failed',6)))
class ClmgmtLicenseActionFailCause(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22)));namedValues=NamedValues(*((_T,1),('generalFailure',2),(_p,3),(_q,4),(_r,5),('invalidLicenseFilePath',6),('invalidLicenseFile',7),('invalidLicenseLine',8),('licenseAlreadyExists',9),('licenseNotValidForDevice',10),('invalidLicenseCount',11),('invalidLicensePeriod',12),('licenseInUse',13),('invalidLicenseStore',14),('licenseStorageFull',15),('invalidPermissionTicketFile',16),('invalidPermissionTicket',17),('invalidRehostTicketFile',18),('invalidRehostTicket',19),('invalidLicenseBackupFile',20),('licenseClearInProgress',21),('invalidLicenseEULAFile',22)))
_CiscoLicenseMgmtMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoLicenseMgmtMIBNotifs=_CiscoLicenseMgmtMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,543,0))
_CiscoLicenseMgmtMIBObjects_ObjectIdentity=ObjectIdentity
ciscoLicenseMgmtMIBObjects=_CiscoLicenseMgmtMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,543,1))
_ClmgmtLicenseConfiguration_ObjectIdentity=ObjectIdentity
clmgmtLicenseConfiguration=_ClmgmtLicenseConfiguration_ObjectIdentity((1,3,6,1,4,1,9,9,543,1,1))
class _ClmgmtNextFreeLicenseActionIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_ClmgmtNextFreeLicenseActionIndex_Type.__name__=_H
_ClmgmtNextFreeLicenseActionIndex_Object=MibScalar
clmgmtNextFreeLicenseActionIndex=_ClmgmtNextFreeLicenseActionIndex_Object((1,3,6,1,4,1,9,9,543,1,1,1),_ClmgmtNextFreeLicenseActionIndex_Type())
clmgmtNextFreeLicenseActionIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:clmgmtNextFreeLicenseActionIndex.setStatus(_B)
_ClmgmtLicenseActionTable_Object=MibTable
clmgmtLicenseActionTable=_ClmgmtLicenseActionTable_Object((1,3,6,1,4,1,9,9,543,1,1,2))
if mibBuilder.loadTexts:clmgmtLicenseActionTable.setStatus(_B)
_ClmgmtLicenseActionEntry_Object=MibTableRow
clmgmtLicenseActionEntry=_ClmgmtLicenseActionEntry_Object((1,3,6,1,4,1,9,9,543,1,1,2,1))
clmgmtLicenseActionEntry.setIndexNames((0,_A,_c))
if mibBuilder.loadTexts:clmgmtLicenseActionEntry.setStatus(_B)
class _ClmgmtLicenseActionIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_ClmgmtLicenseActionIndex_Type.__name__=_H
_ClmgmtLicenseActionIndex_Object=MibTableColumn
clmgmtLicenseActionIndex=_ClmgmtLicenseActionIndex_Object((1,3,6,1,4,1,9,9,543,1,1,2,1,1),_ClmgmtLicenseActionIndex_Type())
clmgmtLicenseActionIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:clmgmtLicenseActionIndex.setStatus(_B)
class _ClmgmtLicenseActionEntPhysicalIndex_Type(PhysicalIndexOrZero):defaultValue=0
_ClmgmtLicenseActionEntPhysicalIndex_Type.__name__=_Y
_ClmgmtLicenseActionEntPhysicalIndex_Object=MibTableColumn
clmgmtLicenseActionEntPhysicalIndex=_ClmgmtLicenseActionEntPhysicalIndex_Object((1,3,6,1,4,1,9,9,543,1,1,2,1,2),_ClmgmtLicenseActionEntPhysicalIndex_Type())
clmgmtLicenseActionEntPhysicalIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:clmgmtLicenseActionEntPhysicalIndex.setStatus(_B)
class _ClmgmtLicenseActionTransferProtocol_Type(ClmgmtLicenseTransferProtocol):defaultValue=1
_ClmgmtLicenseActionTransferProtocol_Type.__name__=_d
_ClmgmtLicenseActionTransferProtocol_Object=MibTableColumn
clmgmtLicenseActionTransferProtocol=_ClmgmtLicenseActionTransferProtocol_Object((1,3,6,1,4,1,9,9,543,1,1,2,1,3),_ClmgmtLicenseActionTransferProtocol_Type())
clmgmtLicenseActionTransferProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:clmgmtLicenseActionTransferProtocol.setStatus(_B)
class _ClmgmtLicenseServerAddressType_Type(InetAddressType):defaultValue=0
_ClmgmtLicenseServerAddressType_Type.__name__=_a
_ClmgmtLicenseServerAddressType_Object=MibTableColumn
clmgmtLicenseServerAddressType=_ClmgmtLicenseServerAddressType_Object((1,3,6,1,4,1,9,9,543,1,1,2,1,4),_ClmgmtLicenseServerAddressType_Type())
clmgmtLicenseServerAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:clmgmtLicenseServerAddressType.setStatus(_B)
class _ClmgmtLicenseServerAddress_Type(InetAddress):defaultValue=OctetString('')
_ClmgmtLicenseServerAddress_Type.__name__=_Z
_ClmgmtLicenseServerAddress_Object=MibTableColumn
clmgmtLicenseServerAddress=_ClmgmtLicenseServerAddress_Object((1,3,6,1,4,1,9,9,543,1,1,2,1,5),_ClmgmtLicenseServerAddress_Type())
clmgmtLicenseServerAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:clmgmtLicenseServerAddress.setStatus(_B)
class _ClmgmtLicenseServerUsername_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,96))
_ClmgmtLicenseServerUsername_Type.__name__=_E
_ClmgmtLicenseServerUsername_Object=MibTableColumn
clmgmtLicenseServerUsername=_ClmgmtLicenseServerUsername_Object((1,3,6,1,4,1,9,9,543,1,1,2,1,6),_ClmgmtLicenseServerUsername_Type())
clmgmtLicenseServerUsername.setMaxAccess(_D)
if mibBuilder.loadTexts:clmgmtLicenseServerUsername.setStatus(_B)
class _ClmgmtLicenseServerPassword_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,96))
_ClmgmtLicenseServerPassword_Type.__name__=_E
_ClmgmtLicenseServerPassword_Object=MibTableColumn
clmgmtLicenseServerPassword=_ClmgmtLicenseServerPassword_Object((1,3,6,1,4,1,9,9,543,1,1,2,1,7),_ClmgmtLicenseServerPassword_Type())
clmgmtLicenseServerPassword.setMaxAccess(_D)
if mibBuilder.loadTexts:clmgmtLicenseServerPassword.setStatus(_B)
class _ClmgmtLicenseFile_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ClmgmtLicenseFile_Type.__name__=_E
_ClmgmtLicenseFile_Object=MibTableColumn
clmgmtLicenseFile=_ClmgmtLicenseFile_Object((1,3,6,1,4,1,9,9,543,1,1,2,1,8),_ClmgmtLicenseFile_Type())
clmgmtLicenseFile.setMaxAccess(_D)
if mibBuilder.loadTexts:clmgmtLicenseFile.setStatus(_B)
class _ClmgmtLicenseStore_Type(Unsigned32):defaultValue=0
_ClmgmtLicenseStore_Type.__name__=_H
_ClmgmtLicenseStore_Object=MibTableColumn
clmgmtLicenseStore=_ClmgmtLicenseStore_Object((1,3,6,1,4,1,9,9,543,1,1,2,1,9),_ClmgmtLicenseStore_Type())
clmgmtLicenseStore.setMaxAccess(_D)
if mibBuilder.loadTexts:clmgmtLicenseStore.setStatus(_B)
class _ClmgmtLicenseActionLicenseIndex_Type(ClmgmtLicenseIndexOrZero):defaultValue=0
_ClmgmtLicenseActionLicenseIndex_Type.__name__=_s
_ClmgmtLicenseActionLicenseIndex_Object=MibTableColumn
clmgmtLicenseActionLicenseIndex=_ClmgmtLicenseActionLicenseIndex_Object((1,3,6,1,4,1,9,9,543,1,1,2,1,10),_ClmgmtLicenseActionLicenseIndex_Type())
clmgmtLicenseActionLicenseIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:clmgmtLicenseActionLicenseIndex.setStatus(_B)
class _ClmgmtLicensePermissionTicketFile_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ClmgmtLicensePermissionTicketFile_Type.__name__=_E
_ClmgmtLicensePermissionTicketFile_Object=MibTableColumn
clmgmtLicensePermissionTicketFile=_ClmgmtLicensePermissionTicketFile_Object((1,3,6,1,4,1,9,9,543,1,1,2,1,11),_ClmgmtLicensePermissionTicketFile_Type())
clmgmtLicensePermissionTicketFile.setMaxAccess(_D)
if mibBuilder.loadTexts:clmgmtLicensePermissionTicketFile.setStatus(_B)
class _ClmgmtLicenseRehostTicketFile_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ClmgmtLicenseRehostTicketFile_Type.__name__=_E
_ClmgmtLicenseRehostTicketFile_Object=MibTableColumn
clmgmtLicenseRehostTicketFile=_ClmgmtLicenseRehostTicketFile_Object((1,3,6,1,4,1,9,9,543,1,1,2,1,12),_ClmgmtLicenseRehostTicketFile_Type())
clmgmtLicenseRehostTicketFile.setMaxAccess(_D)
if mibBuilder.loadTexts:clmgmtLicenseRehostTicketFile.setStatus(_B)
class _ClmgmtLicenseBackupFile_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ClmgmtLicenseBackupFile_Type.__name__=_E
_ClmgmtLicenseBackupFile_Object=MibTableColumn
clmgmtLicenseBackupFile=_ClmgmtLicenseBackupFile_Object((1,3,6,1,4,1,9,9,543,1,1,2,1,13),_ClmgmtLicenseBackupFile_Type())
clmgmtLicenseBackupFile.setMaxAccess(_D)
if mibBuilder.loadTexts:clmgmtLicenseBackupFile.setStatus(_B)
class _ClmgmtLicenseStopOnFailure_Type(TruthValue):defaultValue=2
_ClmgmtLicenseStopOnFailure_Type.__name__=_N
_ClmgmtLicenseStopOnFailure_Object=MibTableColumn
clmgmtLicenseStopOnFailure=_ClmgmtLicenseStopOnFailure_Object((1,3,6,1,4,1,9,9,543,1,1,2,1,14),_ClmgmtLicenseStopOnFailure_Type())
clmgmtLicenseStopOnFailure.setMaxAccess(_D)
if mibBuilder.loadTexts:clmgmtLicenseStopOnFailure.setStatus(_B)
class _ClmgmtLicenseAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('noOp',1),('install',2),('clear',3),('processPermissionTicket',4),('regenerateLastRehostTicket',5),('backup',6),('generateEULA',7)))
_ClmgmtLicenseAction_Type.__name__=_M
_ClmgmtLicenseAction_Object=MibTableColumn
clmgmtLicenseAction=_ClmgmtLicenseAction_Object((1,3,6,1,4,1,9,9,543,1,1,2,1,15),_ClmgmtLicenseAction_Type())
clmgmtLicenseAction.setMaxAccess(_D)
if mibBuilder.loadTexts:clmgmtLicenseAction.setStatus(_B)
_ClmgmtLicenseActionState_Type=ClmgmtLicenseActionState
_ClmgmtLicenseActionState_Object=MibTableColumn
clmgmtLicenseActionState=_ClmgmtLicenseActionState_Object((1,3,6,1,4,1,9,9,543,1,1,2,1,16),_ClmgmtLicenseActionState_Type())
clmgmtLicenseActionState.setMaxAccess(_C)
if mibBuilder.loadTexts:clmgmtLicenseActionState.setStatus(_B)
_ClmgmtLicenseJobQPosition_Type=Unsigned32
_ClmgmtLicenseJobQPosition_Object=MibTableColumn
clmgmtLicenseJobQPosition=_ClmgmtLicenseJobQPosition_Object((1,3,6,1,4,1,9,9,543,1,1,2,1,17),_ClmgmtLicenseJobQPosition_Type())
clmgmtLicenseJobQPosition.setMaxAccess(_C)
if mibBuilder.loadTexts:clmgmtLicenseJobQPosition.setStatus(_B)
_ClmgmtLicenseActionFailCause_Type=ClmgmtLicenseActionFailCause
_ClmgmtLicenseActionFailCause_Object=MibTableColumn
clmgmtLicenseActionFailCause=_ClmgmtLicenseActionFailCause_Object((1,3,6,1,4,1,9,9,543,1,1,2,1,18),_ClmgmtLicenseActionFailCause_Type())
clmgmtLicenseActionFailCause.setMaxAccess(_C)
if mibBuilder.loadTexts:clmgmtLicenseActionFailCause.setStatus(_B)
class _ClmgmtLicenseActionStorageType_Type(StorageType):defaultValue=2
_ClmgmtLicenseActionStorageType_Type.__name__=_b
_ClmgmtLicenseActionStorageType_Object=MibTableColumn
clmgmtLicenseActionStorageType=_ClmgmtLicenseActionStorageType_Object((1,3,6,1,4,1,9,9,543,1,1,2,1,19),_ClmgmtLicenseActionStorageType_Type())
clmgmtLicenseActionStorageType.setMaxAccess(_D)
if mibBuilder.loadTexts:clmgmtLicenseActionStorageType.setStatus(_B)
_ClmgmtLicenseActionRowStatus_Type=RowStatus
_ClmgmtLicenseActionRowStatus_Object=MibTableColumn
clmgmtLicenseActionRowStatus=_ClmgmtLicenseActionRowStatus_Object((1,3,6,1,4,1,9,9,543,1,1,2,1,20),_ClmgmtLicenseActionRowStatus_Type())
clmgmtLicenseActionRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:clmgmtLicenseActionRowStatus.setStatus(_B)
class _ClmgmtLicenseAcceptEULA_Type(TruthValue):defaultValue=2
_ClmgmtLicenseAcceptEULA_Type.__name__=_N
_ClmgmtLicenseAcceptEULA_Object=MibTableColumn
clmgmtLicenseAcceptEULA=_ClmgmtLicenseAcceptEULA_Object((1,3,6,1,4,1,9,9,543,1,1,2,1,21),_ClmgmtLicenseAcceptEULA_Type())
clmgmtLicenseAcceptEULA.setMaxAccess(_D)
if mibBuilder.loadTexts:clmgmtLicenseAcceptEULA.setStatus(_B)
class _ClmgmtLicenseEULAFile_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ClmgmtLicenseEULAFile_Type.__name__=_E
_ClmgmtLicenseEULAFile_Object=MibTableColumn
clmgmtLicenseEULAFile=_ClmgmtLicenseEULAFile_Object((1,3,6,1,4,1,9,9,543,1,1,2,1,22),_ClmgmtLicenseEULAFile_Type())
clmgmtLicenseEULAFile.setMaxAccess(_D)
if mibBuilder.loadTexts:clmgmtLicenseEULAFile.setStatus(_B)
_ClmgmtLicenseActionResultTable_Object=MibTable
clmgmtLicenseActionResultTable=_ClmgmtLicenseActionResultTable_Object((1,3,6,1,4,1,9,9,543,1,1,3))
if mibBuilder.loadTexts:clmgmtLicenseActionResultTable.setStatus(_B)
_ClmgmtLicenseActionResultEntry_Object=MibTableRow
clmgmtLicenseActionResultEntry=_ClmgmtLicenseActionResultEntry_Object((1,3,6,1,4,1,9,9,543,1,1,3,1))
clmgmtLicenseActionResultEntry.setIndexNames((0,_A,_c),(0,_A,_t))
if mibBuilder.loadTexts:clmgmtLicenseActionResultEntry.setStatus(_B)
class _ClmgmtLicenseNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_ClmgmtLicenseNumber_Type.__name__=_H
_ClmgmtLicenseNumber_Object=MibTableColumn
clmgmtLicenseNumber=_ClmgmtLicenseNumber_Object((1,3,6,1,4,1,9,9,543,1,1,3,1,1),_ClmgmtLicenseNumber_Type())
clmgmtLicenseNumber.setMaxAccess(_I)
if mibBuilder.loadTexts:clmgmtLicenseNumber.setStatus(_B)
_ClmgmtLicenseIndivActionState_Type=ClmgmtLicenseActionState
_ClmgmtLicenseIndivActionState_Object=MibTableColumn
clmgmtLicenseIndivActionState=_ClmgmtLicenseIndivActionState_Object((1,3,6,1,4,1,9,9,543,1,1,3,1,2),_ClmgmtLicenseIndivActionState_Type())
clmgmtLicenseIndivActionState.setMaxAccess(_C)
if mibBuilder.loadTexts:clmgmtLicenseIndivActionState.setStatus(_B)
_ClmgmtLicenseIndivActionFailCause_Type=ClmgmtLicenseActionFailCause
_ClmgmtLicenseIndivActionFailCause_Object=MibTableColumn
clmgmtLicenseIndivActionFailCause=_ClmgmtLicenseIndivActionFailCause_Object((1,3,6,1,4,1,9,9,543,1,1,3,1,3),_ClmgmtLicenseIndivActionFailCause_Type())
clmgmtLicenseIndivActionFailCause.setMaxAccess(_C)
if mibBuilder.loadTexts:clmgmtLicenseIndivActionFailCause.setStatus(_B)
_ClmgmtLicenseInformation_ObjectIdentity=ObjectIdentity
clmgmtLicenseInformation=_ClmgmtLicenseInformation_ObjectIdentity((1,3,6,1,4,1,9,9,543,1,2))
_ClmgmtLicenseStoreInfoTable_Object=MibTable
clmgmtLicenseStoreInfoTable=_ClmgmtLicenseStoreInfoTable_Object((1,3,6,1,4,1,9,9,543,1,2,1))
if mibBuilder.loadTexts:clmgmtLicenseStoreInfoTable.setStatus(_B)
_ClmgmtLicenseStoreInfoEntry_Object=MibTableRow
clmgmtLicenseStoreInfoEntry=_ClmgmtLicenseStoreInfoEntry_Object((1,3,6,1,4,1,9,9,543,1,2,1,1))
clmgmtLicenseStoreInfoEntry.setIndexNames((0,_P,_Q),(0,_A,_u))
if mibBuilder.loadTexts:clmgmtLicenseStoreInfoEntry.setStatus(_B)
class _ClmgmtLicenseStoreIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_ClmgmtLicenseStoreIndex_Type.__name__=_H
_ClmgmtLicenseStoreIndex_Object=MibTableColumn
clmgmtLicenseStoreIndex=_ClmgmtLicenseStoreIndex_Object((1,3,6,1,4,1,9,9,543,1,2,1,1,1),_ClmgmtLicenseStoreIndex_Type())
clmgmtLicenseStoreIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:clmgmtLicenseStoreIndex.setStatus(_B)
class _ClmgmtLicenseStoreName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ClmgmtLicenseStoreName_Type.__name__=_E
_ClmgmtLicenseStoreName_Object=MibTableColumn
clmgmtLicenseStoreName=_ClmgmtLicenseStoreName_Object((1,3,6,1,4,1,9,9,543,1,2,1,1,2),_ClmgmtLicenseStoreName_Type())
clmgmtLicenseStoreName.setMaxAccess(_C)
if mibBuilder.loadTexts:clmgmtLicenseStoreName.setStatus(_B)
_ClmgmtLicenseStoreTotalSize_Type=Unsigned32
_ClmgmtLicenseStoreTotalSize_Object=MibTableColumn
clmgmtLicenseStoreTotalSize=_ClmgmtLicenseStoreTotalSize_Object((1,3,6,1,4,1,9,9,543,1,2,1,1,3),_ClmgmtLicenseStoreTotalSize_Type())
clmgmtLicenseStoreTotalSize.setMaxAccess(_C)
if mibBuilder.loadTexts:clmgmtLicenseStoreTotalSize.setStatus(_B)
if mibBuilder.loadTexts:clmgmtLicenseStoreTotalSize.setUnits('bytes')
_ClmgmtLicenseStoreSizeRemaining_Type=Unsigned32
_ClmgmtLicenseStoreSizeRemaining_Object=MibTableColumn
clmgmtLicenseStoreSizeRemaining=_ClmgmtLicenseStoreSizeRemaining_Object((1,3,6,1,4,1,9,9,543,1,2,1,1,4),_ClmgmtLicenseStoreSizeRemaining_Type())
clmgmtLicenseStoreSizeRemaining.setMaxAccess(_C)
if mibBuilder.loadTexts:clmgmtLicenseStoreSizeRemaining.setStatus(_B)
if mibBuilder.loadTexts:clmgmtLicenseStoreSizeRemaining.setUnits('bytes')
_ClmgmtLicenseDeviceInfoTable_Object=MibTable
clmgmtLicenseDeviceInfoTable=_ClmgmtLicenseDeviceInfoTable_Object((1,3,6,1,4,1,9,9,543,1,2,2))
if mibBuilder.loadTexts:clmgmtLicenseDeviceInfoTable.setStatus(_B)
_ClmgmtLicenseDeviceInfoEntry_Object=MibTableRow
clmgmtLicenseDeviceInfoEntry=_ClmgmtLicenseDeviceInfoEntry_Object((1,3,6,1,4,1,9,9,543,1,2,2,1))
clmgmtLicenseDeviceInfoEntry.setIndexNames((0,_P,_Q))
if mibBuilder.loadTexts:clmgmtLicenseDeviceInfoEntry.setStatus(_B)
class _ClmgmtDefaultLicenseStore_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_ClmgmtDefaultLicenseStore_Type.__name__=_H
_ClmgmtDefaultLicenseStore_Object=MibTableColumn
clmgmtDefaultLicenseStore=_ClmgmtDefaultLicenseStore_Object((1,3,6,1,4,1,9,9,543,1,2,2,1,1),_ClmgmtDefaultLicenseStore_Type())
clmgmtDefaultLicenseStore.setMaxAccess(_C)
if mibBuilder.loadTexts:clmgmtDefaultLicenseStore.setStatus(_B)
_ClmgmtLicenseInfoTable_Object=MibTable
clmgmtLicenseInfoTable=_ClmgmtLicenseInfoTable_Object((1,3,6,1,4,1,9,9,543,1,2,3))
if mibBuilder.loadTexts:clmgmtLicenseInfoTable.setStatus(_B)
_ClmgmtLicenseInfoEntry_Object=MibTableRow
clmgmtLicenseInfoEntry=_ClmgmtLicenseInfoEntry_Object((1,3,6,1,4,1,9,9,543,1,2,3,1))
clmgmtLicenseInfoEntry.setIndexNames((0,_P,_Q),(0,_A,_v),(0,_A,_w))
if mibBuilder.loadTexts:clmgmtLicenseInfoEntry.setStatus(_B)
class _ClmgmtLicenseStoreUsed_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_ClmgmtLicenseStoreUsed_Type.__name__=_H
_ClmgmtLicenseStoreUsed_Object=MibTableColumn
clmgmtLicenseStoreUsed=_ClmgmtLicenseStoreUsed_Object((1,3,6,1,4,1,9,9,543,1,2,3,1,1),_ClmgmtLicenseStoreUsed_Type())
clmgmtLicenseStoreUsed.setMaxAccess(_I)
if mibBuilder.loadTexts:clmgmtLicenseStoreUsed.setStatus(_B)
_ClmgmtLicenseIndex_Type=ClmgmtLicenseIndex
_ClmgmtLicenseIndex_Object=MibTableColumn
clmgmtLicenseIndex=_ClmgmtLicenseIndex_Object((1,3,6,1,4,1,9,9,543,1,2,3,1,2),_ClmgmtLicenseIndex_Type())
clmgmtLicenseIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:clmgmtLicenseIndex.setStatus(_B)
class _ClmgmtLicenseFeatureName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_ClmgmtLicenseFeatureName_Type.__name__=_E
_ClmgmtLicenseFeatureName_Object=MibTableColumn
clmgmtLicenseFeatureName=_ClmgmtLicenseFeatureName_Object((1,3,6,1,4,1,9,9,543,1,2,3,1,3),_ClmgmtLicenseFeatureName_Type())
clmgmtLicenseFeatureName.setMaxAccess(_C)
if mibBuilder.loadTexts:clmgmtLicenseFeatureName.setStatus(_B)
class _ClmgmtLicenseFeatureVersion_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_ClmgmtLicenseFeatureVersion_Type.__name__=_E
_ClmgmtLicenseFeatureVersion_Object=MibTableColumn
clmgmtLicenseFeatureVersion=_ClmgmtLicenseFeatureVersion_Object((1,3,6,1,4,1,9,9,543,1,2,3,1,4),_ClmgmtLicenseFeatureVersion_Type())
clmgmtLicenseFeatureVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:clmgmtLicenseFeatureVersion.setStatus(_B)
class _ClmgmtLicenseType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('demo',1),('extension',2),('gracePeriod',3),('permanent',4),('paidSubscription',5),('evaluationSubscription',6),('extensionSubscription',7),('evalRightToUse',8),('rightToUse',9),('permanentRightToUse',10)))
_ClmgmtLicenseType_Type.__name__=_M
_ClmgmtLicenseType_Object=MibTableColumn
clmgmtLicenseType=_ClmgmtLicenseType_Object((1,3,6,1,4,1,9,9,543,1,2,3,1,5),_ClmgmtLicenseType_Type())
clmgmtLicenseType.setMaxAccess(_C)
if mibBuilder.loadTexts:clmgmtLicenseType.setStatus(_B)
_ClmgmtLicenseCounted_Type=TruthValue
_ClmgmtLicenseCounted_Object=MibTableColumn
clmgmtLicenseCounted=_ClmgmtLicenseCounted_Object((1,3,6,1,4,1,9,9,543,1,2,3,1,6),_ClmgmtLicenseCounted_Type())
clmgmtLicenseCounted.setMaxAccess(_C)
if mibBuilder.loadTexts:clmgmtLicenseCounted.setStatus(_B)
_ClmgmtLicenseValidityPeriod_Type=Unsigned32
_ClmgmtLicenseValidityPeriod_Object=MibTableColumn
clmgmtLicenseValidityPeriod=_ClmgmtLicenseValidityPeriod_Object((1,3,6,1,4,1,9,9,543,1,2,3,1,7),_ClmgmtLicenseValidityPeriod_Type())
clmgmtLicenseValidityPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:clmgmtLicenseValidityPeriod.setStatus(_B)
if mibBuilder.loadTexts:clmgmtLicenseValidityPeriod.setUnits(_O)
_ClmgmtLicenseValidityPeriodRemaining_Type=Unsigned32
_ClmgmtLicenseValidityPeriodRemaining_Object=MibTableColumn
clmgmtLicenseValidityPeriodRemaining=_ClmgmtLicenseValidityPeriodRemaining_Object((1,3,6,1,4,1,9,9,543,1,2,3,1,8),_ClmgmtLicenseValidityPeriodRemaining_Type())
clmgmtLicenseValidityPeriodRemaining.setMaxAccess(_C)
if mibBuilder.loadTexts:clmgmtLicenseValidityPeriodRemaining.setStatus(_B)
if mibBuilder.loadTexts:clmgmtLicenseValidityPeriodRemaining.setUnits(_O)
_ClmgmtLicenseExpiredPeriod_Type=Unsigned32
_ClmgmtLicenseExpiredPeriod_Object=MibTableColumn
clmgmtLicenseExpiredPeriod=_ClmgmtLicenseExpiredPeriod_Object((1,3,6,1,4,1,9,9,543,1,2,3,1,9),_ClmgmtLicenseExpiredPeriod_Type())
clmgmtLicenseExpiredPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:clmgmtLicenseExpiredPeriod.setStatus(_B)
if mibBuilder.loadTexts:clmgmtLicenseExpiredPeriod.setUnits(_O)
_ClmgmtLicenseMaxUsageCount_Type=Unsigned32
_ClmgmtLicenseMaxUsageCount_Object=MibTableColumn
clmgmtLicenseMaxUsageCount=_ClmgmtLicenseMaxUsageCount_Object((1,3,6,1,4,1,9,9,543,1,2,3,1,10),_ClmgmtLicenseMaxUsageCount_Type())
clmgmtLicenseMaxUsageCount.setMaxAccess(_C)
if mibBuilder.loadTexts:clmgmtLicenseMaxUsageCount.setStatus(_B)
_ClmgmtLicenseUsageCountRemaining_Type=Unsigned32
_ClmgmtLicenseUsageCountRemaining_Object=MibTableColumn
clmgmtLicenseUsageCountRemaining=_ClmgmtLicenseUsageCountRemaining_Object((1,3,6,1,4,1,9,9,543,1,2,3,1,11),_ClmgmtLicenseUsageCountRemaining_Type())
clmgmtLicenseUsageCountRemaining.setMaxAccess(_C)
if mibBuilder.loadTexts:clmgmtLicenseUsageCountRemaining.setStatus(_B)
_ClmgmtLicenseEULAStatus_Type=TruthValue
_ClmgmtLicenseEULAStatus_Object=MibTableColumn
clmgmtLicenseEULAStatus=_ClmgmtLicenseEULAStatus_Object((1,3,6,1,4,1,9,9,543,1,2,3,1,12),_ClmgmtLicenseEULAStatus_Type())
clmgmtLicenseEULAStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:clmgmtLicenseEULAStatus.setStatus(_B)
class _ClmgmtLicenseComments_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ClmgmtLicenseComments_Type.__name__=_E
_ClmgmtLicenseComments_Object=MibTableColumn
clmgmtLicenseComments=_ClmgmtLicenseComments_Object((1,3,6,1,4,1,9,9,543,1,2,3,1,13),_ClmgmtLicenseComments_Type())
clmgmtLicenseComments.setMaxAccess(_U)
if mibBuilder.loadTexts:clmgmtLicenseComments.setStatus(_B)
class _ClmgmtLicenseStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('inactive',1),('notInUse',2),('inUse',3),('expiredInUse',4),('expiredNotInUse',5),('usageCountConsumed',6)))
_ClmgmtLicenseStatus_Type.__name__=_M
_ClmgmtLicenseStatus_Object=MibTableColumn
clmgmtLicenseStatus=_ClmgmtLicenseStatus_Object((1,3,6,1,4,1,9,9,543,1,2,3,1,14),_ClmgmtLicenseStatus_Type())
clmgmtLicenseStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:clmgmtLicenseStatus.setStatus(_B)
_ClmgmtLicenseStartDate_Type=DateAndTime
_ClmgmtLicenseStartDate_Object=MibTableColumn
clmgmtLicenseStartDate=_ClmgmtLicenseStartDate_Object((1,3,6,1,4,1,9,9,543,1,2,3,1,15),_ClmgmtLicenseStartDate_Type())
clmgmtLicenseStartDate.setMaxAccess(_C)
if mibBuilder.loadTexts:clmgmtLicenseStartDate.setStatus(_B)
_ClmgmtLicenseEndDate_Type=DateAndTime
_ClmgmtLicenseEndDate_Object=MibTableColumn
clmgmtLicenseEndDate=_ClmgmtLicenseEndDate_Object((1,3,6,1,4,1,9,9,543,1,2,3,1,16),_ClmgmtLicenseEndDate_Type())
clmgmtLicenseEndDate.setMaxAccess(_C)
if mibBuilder.loadTexts:clmgmtLicenseEndDate.setStatus(_B)
_ClmgmtLicensePeriodUsed_Type=Unsigned32
_ClmgmtLicensePeriodUsed_Object=MibTableColumn
clmgmtLicensePeriodUsed=_ClmgmtLicensePeriodUsed_Object((1,3,6,1,4,1,9,9,543,1,2,3,1,17),_ClmgmtLicensePeriodUsed_Type())
clmgmtLicensePeriodUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:clmgmtLicensePeriodUsed.setStatus(_B)
if mibBuilder.loadTexts:clmgmtLicensePeriodUsed.setUnits(_O)
_ClmgmtLicensableFeatureTable_Object=MibTable
clmgmtLicensableFeatureTable=_ClmgmtLicensableFeatureTable_Object((1,3,6,1,4,1,9,9,543,1,2,4))
if mibBuilder.loadTexts:clmgmtLicensableFeatureTable.setStatus(_B)
_ClmgmtLicensableFeatureEntry_Object=MibTableRow
clmgmtLicensableFeatureEntry=_ClmgmtLicensableFeatureEntry_Object((1,3,6,1,4,1,9,9,543,1,2,4,1))
clmgmtLicensableFeatureEntry.setIndexNames((0,_P,_Q),(0,_A,_x))
if mibBuilder.loadTexts:clmgmtLicensableFeatureEntry.setStatus(_B)
class _ClmgmtFeatureIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_ClmgmtFeatureIndex_Type.__name__=_H
_ClmgmtFeatureIndex_Object=MibTableColumn
clmgmtFeatureIndex=_ClmgmtFeatureIndex_Object((1,3,6,1,4,1,9,9,543,1,2,4,1,1),_ClmgmtFeatureIndex_Type())
clmgmtFeatureIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:clmgmtFeatureIndex.setStatus(_B)
class _ClmgmtFeatureName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_ClmgmtFeatureName_Type.__name__=_E
_ClmgmtFeatureName_Object=MibTableColumn
clmgmtFeatureName=_ClmgmtFeatureName_Object((1,3,6,1,4,1,9,9,543,1,2,4,1,2),_ClmgmtFeatureName_Type())
clmgmtFeatureName.setMaxAccess(_C)
if mibBuilder.loadTexts:clmgmtFeatureName.setStatus(_B)
class _ClmgmtFeatureVersion_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ClmgmtFeatureVersion_Type.__name__=_E
_ClmgmtFeatureVersion_Object=MibTableColumn
clmgmtFeatureVersion=_ClmgmtFeatureVersion_Object((1,3,6,1,4,1,9,9,543,1,2,4,1,3),_ClmgmtFeatureVersion_Type())
clmgmtFeatureVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:clmgmtFeatureVersion.setStatus(_B)
_ClmgmtFeatureValidityPeriodRemaining_Type=Unsigned32
_ClmgmtFeatureValidityPeriodRemaining_Object=MibTableColumn
clmgmtFeatureValidityPeriodRemaining=_ClmgmtFeatureValidityPeriodRemaining_Object((1,3,6,1,4,1,9,9,543,1,2,4,1,4),_ClmgmtFeatureValidityPeriodRemaining_Type())
clmgmtFeatureValidityPeriodRemaining.setMaxAccess(_C)
if mibBuilder.loadTexts:clmgmtFeatureValidityPeriodRemaining.setStatus(_B)
if mibBuilder.loadTexts:clmgmtFeatureValidityPeriodRemaining.setUnits(_O)
class _ClmgmtFeatureWhatIsCounted_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_ClmgmtFeatureWhatIsCounted_Type.__name__=_E
_ClmgmtFeatureWhatIsCounted_Object=MibTableColumn
clmgmtFeatureWhatIsCounted=_ClmgmtFeatureWhatIsCounted_Object((1,3,6,1,4,1,9,9,543,1,2,4,1,5),_ClmgmtFeatureWhatIsCounted_Type())
clmgmtFeatureWhatIsCounted.setMaxAccess(_C)
if mibBuilder.loadTexts:clmgmtFeatureWhatIsCounted.setStatus(_B)
_ClmgmtFeatureStartDate_Type=DateAndTime
_ClmgmtFeatureStartDate_Object=MibTableColumn
clmgmtFeatureStartDate=_ClmgmtFeatureStartDate_Object((1,3,6,1,4,1,9,9,543,1,2,4,1,6),_ClmgmtFeatureStartDate_Type())
clmgmtFeatureStartDate.setMaxAccess(_C)
if mibBuilder.loadTexts:clmgmtFeatureStartDate.setStatus(_B)
_ClmgmtFeatureEndDate_Type=DateAndTime
_ClmgmtFeatureEndDate_Object=MibTableColumn
clmgmtFeatureEndDate=_ClmgmtFeatureEndDate_Object((1,3,6,1,4,1,9,9,543,1,2,4,1,7),_ClmgmtFeatureEndDate_Type())
clmgmtFeatureEndDate.setMaxAccess(_C)
if mibBuilder.loadTexts:clmgmtFeatureEndDate.setStatus(_B)
_ClmgmtFeaturePeriodUsed_Type=Unsigned32
_ClmgmtFeaturePeriodUsed_Object=MibTableColumn
clmgmtFeaturePeriodUsed=_ClmgmtFeaturePeriodUsed_Object((1,3,6,1,4,1,9,9,543,1,2,4,1,8),_ClmgmtFeaturePeriodUsed_Type())
clmgmtFeaturePeriodUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:clmgmtFeaturePeriodUsed.setStatus(_B)
if mibBuilder.loadTexts:clmgmtFeaturePeriodUsed.setUnits(_O)
_ClmgmtLicenseDeviceInformation_ObjectIdentity=ObjectIdentity
clmgmtLicenseDeviceInformation=_ClmgmtLicenseDeviceInformation_ObjectIdentity((1,3,6,1,4,1,9,9,543,1,3))
_ClmgmtNextFreeDevCredExportActionIndex_Type=Unsigned32
_ClmgmtNextFreeDevCredExportActionIndex_Object=MibScalar
clmgmtNextFreeDevCredExportActionIndex=_ClmgmtNextFreeDevCredExportActionIndex_Object((1,3,6,1,4,1,9,9,543,1,3,1),_ClmgmtNextFreeDevCredExportActionIndex_Type())
clmgmtNextFreeDevCredExportActionIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:clmgmtNextFreeDevCredExportActionIndex.setStatus(_B)
_ClmgmtDevCredExportActionTable_Object=MibTable
clmgmtDevCredExportActionTable=_ClmgmtDevCredExportActionTable_Object((1,3,6,1,4,1,9,9,543,1,3,2))
if mibBuilder.loadTexts:clmgmtDevCredExportActionTable.setStatus(_B)
_ClmgmtDevCredExportActionEntry_Object=MibTableRow
clmgmtDevCredExportActionEntry=_ClmgmtDevCredExportActionEntry_Object((1,3,6,1,4,1,9,9,543,1,3,2,1))
clmgmtDevCredExportActionEntry.setIndexNames((0,_A,_y))
if mibBuilder.loadTexts:clmgmtDevCredExportActionEntry.setStatus(_B)
class _ClmgmtDevCredExportActionIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_ClmgmtDevCredExportActionIndex_Type.__name__=_H
_ClmgmtDevCredExportActionIndex_Object=MibTableColumn
clmgmtDevCredExportActionIndex=_ClmgmtDevCredExportActionIndex_Object((1,3,6,1,4,1,9,9,543,1,3,2,1,1),_ClmgmtDevCredExportActionIndex_Type())
clmgmtDevCredExportActionIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:clmgmtDevCredExportActionIndex.setStatus(_B)
class _ClmgmtDevCredEntPhysicalIndex_Type(PhysicalIndexOrZero):defaultValue=0
_ClmgmtDevCredEntPhysicalIndex_Type.__name__=_Y
_ClmgmtDevCredEntPhysicalIndex_Object=MibTableColumn
clmgmtDevCredEntPhysicalIndex=_ClmgmtDevCredEntPhysicalIndex_Object((1,3,6,1,4,1,9,9,543,1,3,2,1,2),_ClmgmtDevCredEntPhysicalIndex_Type())
clmgmtDevCredEntPhysicalIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:clmgmtDevCredEntPhysicalIndex.setStatus(_B)
class _ClmgmtDevCredTransferProtocol_Type(ClmgmtLicenseTransferProtocol):defaultValue=1
_ClmgmtDevCredTransferProtocol_Type.__name__=_d
_ClmgmtDevCredTransferProtocol_Object=MibTableColumn
clmgmtDevCredTransferProtocol=_ClmgmtDevCredTransferProtocol_Object((1,3,6,1,4,1,9,9,543,1,3,2,1,3),_ClmgmtDevCredTransferProtocol_Type())
clmgmtDevCredTransferProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:clmgmtDevCredTransferProtocol.setStatus(_B)
class _ClmgmtDevCredServerAddressType_Type(InetAddressType):defaultValue=0
_ClmgmtDevCredServerAddressType_Type.__name__=_a
_ClmgmtDevCredServerAddressType_Object=MibTableColumn
clmgmtDevCredServerAddressType=_ClmgmtDevCredServerAddressType_Object((1,3,6,1,4,1,9,9,543,1,3,2,1,4),_ClmgmtDevCredServerAddressType_Type())
clmgmtDevCredServerAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:clmgmtDevCredServerAddressType.setStatus(_B)
class _ClmgmtDevCredServerAddress_Type(InetAddress):defaultValue=OctetString('')
_ClmgmtDevCredServerAddress_Type.__name__=_Z
_ClmgmtDevCredServerAddress_Object=MibTableColumn
clmgmtDevCredServerAddress=_ClmgmtDevCredServerAddress_Object((1,3,6,1,4,1,9,9,543,1,3,2,1,5),_ClmgmtDevCredServerAddress_Type())
clmgmtDevCredServerAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:clmgmtDevCredServerAddress.setStatus(_B)
class _ClmgmtDevCredServerUsername_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,96))
_ClmgmtDevCredServerUsername_Type.__name__=_E
_ClmgmtDevCredServerUsername_Object=MibTableColumn
clmgmtDevCredServerUsername=_ClmgmtDevCredServerUsername_Object((1,3,6,1,4,1,9,9,543,1,3,2,1,6),_ClmgmtDevCredServerUsername_Type())
clmgmtDevCredServerUsername.setMaxAccess(_D)
if mibBuilder.loadTexts:clmgmtDevCredServerUsername.setStatus(_B)
class _ClmgmtDevCredServerPassword_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,96))
_ClmgmtDevCredServerPassword_Type.__name__=_E
_ClmgmtDevCredServerPassword_Object=MibTableColumn
clmgmtDevCredServerPassword=_ClmgmtDevCredServerPassword_Object((1,3,6,1,4,1,9,9,543,1,3,2,1,7),_ClmgmtDevCredServerPassword_Type())
clmgmtDevCredServerPassword.setMaxAccess(_D)
if mibBuilder.loadTexts:clmgmtDevCredServerPassword.setStatus(_B)
class _ClmgmtDevCredExportFile_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ClmgmtDevCredExportFile_Type.__name__=_E
_ClmgmtDevCredExportFile_Object=MibTableColumn
clmgmtDevCredExportFile=_ClmgmtDevCredExportFile_Object((1,3,6,1,4,1,9,9,543,1,3,2,1,8),_ClmgmtDevCredExportFile_Type())
clmgmtDevCredExportFile.setMaxAccess(_D)
if mibBuilder.loadTexts:clmgmtDevCredExportFile.setStatus(_B)
class _ClmgmtDevCredCommand_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noOp',1),('getDeviceCredentials',2)))
_ClmgmtDevCredCommand_Type.__name__=_M
_ClmgmtDevCredCommand_Object=MibTableColumn
clmgmtDevCredCommand=_ClmgmtDevCredCommand_Object((1,3,6,1,4,1,9,9,543,1,3,2,1,9),_ClmgmtDevCredCommand_Type())
clmgmtDevCredCommand.setMaxAccess(_D)
if mibBuilder.loadTexts:clmgmtDevCredCommand.setStatus(_B)
_ClmgmtDevCredCommandState_Type=ClmgmtLicenseActionState
_ClmgmtDevCredCommandState_Object=MibTableColumn
clmgmtDevCredCommandState=_ClmgmtDevCredCommandState_Object((1,3,6,1,4,1,9,9,543,1,3,2,1,10),_ClmgmtDevCredCommandState_Type())
clmgmtDevCredCommandState.setMaxAccess(_C)
if mibBuilder.loadTexts:clmgmtDevCredCommandState.setStatus(_B)
class _ClmgmtDevCredCommandFailCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_T,1),('unknownError',2),(_p,3),(_q,4),(_r,5),('invalidFile',6)))
_ClmgmtDevCredCommandFailCause_Type.__name__=_M
_ClmgmtDevCredCommandFailCause_Object=MibTableColumn
clmgmtDevCredCommandFailCause=_ClmgmtDevCredCommandFailCause_Object((1,3,6,1,4,1,9,9,543,1,3,2,1,11),_ClmgmtDevCredCommandFailCause_Type())
clmgmtDevCredCommandFailCause.setMaxAccess(_C)
if mibBuilder.loadTexts:clmgmtDevCredCommandFailCause.setStatus(_B)
class _ClmgmtDevCredStorageType_Type(StorageType):defaultValue=2
_ClmgmtDevCredStorageType_Type.__name__=_b
_ClmgmtDevCredStorageType_Object=MibTableColumn
clmgmtDevCredStorageType=_ClmgmtDevCredStorageType_Object((1,3,6,1,4,1,9,9,543,1,3,2,1,12),_ClmgmtDevCredStorageType_Type())
clmgmtDevCredStorageType.setMaxAccess(_D)
if mibBuilder.loadTexts:clmgmtDevCredStorageType.setStatus(_B)
_ClmgmtDevCredRowStatus_Type=RowStatus
_ClmgmtDevCredRowStatus_Object=MibTableColumn
clmgmtDevCredRowStatus=_ClmgmtDevCredRowStatus_Object((1,3,6,1,4,1,9,9,543,1,3,2,1,13),_ClmgmtDevCredRowStatus_Type())
clmgmtDevCredRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:clmgmtDevCredRowStatus.setStatus(_B)
_ClmgmtLicenseNotifObjects_ObjectIdentity=ObjectIdentity
clmgmtLicenseNotifObjects=_ClmgmtLicenseNotifObjects_ObjectIdentity((1,3,6,1,4,1,9,9,543,1,4))
class _ClmgmtLicenseUsageNotifEnable_Type(TruthValue):defaultValue=1
_ClmgmtLicenseUsageNotifEnable_Type.__name__=_N
_ClmgmtLicenseUsageNotifEnable_Object=MibScalar
clmgmtLicenseUsageNotifEnable=_ClmgmtLicenseUsageNotifEnable_Object((1,3,6,1,4,1,9,9,543,1,4,1),_ClmgmtLicenseUsageNotifEnable_Type())
clmgmtLicenseUsageNotifEnable.setMaxAccess(_U)
if mibBuilder.loadTexts:clmgmtLicenseUsageNotifEnable.setStatus(_B)
class _ClmgmtLicenseDeploymentNotifEnable_Type(TruthValue):defaultValue=1
_ClmgmtLicenseDeploymentNotifEnable_Type.__name__=_N
_ClmgmtLicenseDeploymentNotifEnable_Object=MibScalar
clmgmtLicenseDeploymentNotifEnable=_ClmgmtLicenseDeploymentNotifEnable_Object((1,3,6,1,4,1,9,9,543,1,4,2),_ClmgmtLicenseDeploymentNotifEnable_Type())
clmgmtLicenseDeploymentNotifEnable.setMaxAccess(_U)
if mibBuilder.loadTexts:clmgmtLicenseDeploymentNotifEnable.setStatus(_B)
class _ClmgmtLicenseErrorNotifEnable_Type(TruthValue):defaultValue=1
_ClmgmtLicenseErrorNotifEnable_Type.__name__=_N
_ClmgmtLicenseErrorNotifEnable_Object=MibScalar
clmgmtLicenseErrorNotifEnable=_ClmgmtLicenseErrorNotifEnable_Object((1,3,6,1,4,1,9,9,543,1,4,3),_ClmgmtLicenseErrorNotifEnable_Type())
clmgmtLicenseErrorNotifEnable.setMaxAccess(_U)
if mibBuilder.loadTexts:clmgmtLicenseErrorNotifEnable.setStatus(_B)
_CiscoLicenseMgmtMIBConform_ObjectIdentity=ObjectIdentity
ciscoLicenseMgmtMIBConform=_CiscoLicenseMgmtMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,543,2))
_CiscoLicenseMgmtCompliances_ObjectIdentity=ObjectIdentity
ciscoLicenseMgmtCompliances=_CiscoLicenseMgmtCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,543,2,1))
_CiscoLicenseMgmtGroups_ObjectIdentity=ObjectIdentity
ciscoLicenseMgmtGroups=_CiscoLicenseMgmtGroups_ObjectIdentity((1,3,6,1,4,1,9,9,543,2,2))
clmgmtLicenseDeploymentGroup=ObjectGroup((1,3,6,1,4,1,9,9,543,2,2,1))
clmgmtLicenseDeploymentGroup.setObjects(*((_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM)))
if mibBuilder.loadTexts:clmgmtLicenseDeploymentGroup.setStatus(_B)
clmgmtLicenseStoreInformationGroup=ObjectGroup((1,3,6,1,4,1,9,9,543,2,2,2))
clmgmtLicenseStoreInformationGroup.setObjects(*((_A,_AN),(_A,_AO),(_A,_AP)))
if mibBuilder.loadTexts:clmgmtLicenseStoreInformationGroup.setStatus(_B)
clmgmtLicenseDeviceInformationGroup=ObjectGroup((1,3,6,1,4,1,9,9,543,2,2,3))
clmgmtLicenseDeviceInformationGroup.setObjects((_A,_AQ))
if mibBuilder.loadTexts:clmgmtLicenseDeviceInformationGroup.setStatus(_B)
clmgmtLicenseInformationGroup=ObjectGroup((1,3,6,1,4,1,9,9,543,2,2,4))
clmgmtLicenseInformationGroup.setObjects(*((_A,_J),(_A,_K),(_A,_R),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_V),(_A,_e),(_A,_AV),(_A,_L),(_A,_AW)))
if mibBuilder.loadTexts:clmgmtLicenseInformationGroup.setStatus(_B)
clmgmtLicensableFeatureInformationGroup=ObjectGroup((1,3,6,1,4,1,9,9,543,2,2,5))
clmgmtLicensableFeatureInformationGroup.setObjects(*((_A,_F),(_A,_G),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:clmgmtLicensableFeatureInformationGroup.setStatus(_B)
clmgmtLicenseDevCredGroup=ObjectGroup((1,3,6,1,4,1,9,9,543,2,2,6))
clmgmtLicenseDevCredGroup.setObjects(*((_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_Ae),(_A,_Af),(_A,_Ag),(_A,_Ah),(_A,_Ai),(_A,_Aj)))
if mibBuilder.loadTexts:clmgmtLicenseDevCredGroup.setStatus(_B)
clmgmtLicenseNotificationEnableGroup=ObjectGroup((1,3,6,1,4,1,9,9,543,2,2,7))
clmgmtLicenseNotificationEnableGroup.setObjects(*((_A,_Ak),(_A,_Al),(_A,_Am)))
if mibBuilder.loadTexts:clmgmtLicenseNotificationEnableGroup.setStatus(_B)
clmgmtLicenseSubscriptionGroup=ObjectGroup((1,3,6,1,4,1,9,9,543,2,2,11))
clmgmtLicenseSubscriptionGroup.setObjects(*((_A,_An),(_A,_Ao),(_A,_Ap),(_A,_S)))
if mibBuilder.loadTexts:clmgmtLicenseSubscriptionGroup.setStatus(_B)
clmgmtLicenseRTUGroup=ObjectGroup((1,3,6,1,4,1,9,9,543,2,2,13))
clmgmtLicenseRTUGroup.setObjects(*((_A,_Aq),(_A,_Ar)))
if mibBuilder.loadTexts:clmgmtLicenseRTUGroup.setStatus(_B)
clmgmtLicenseExpired=NotificationType((1,3,6,1,4,1,9,9,543,0,1))
clmgmtLicenseExpired.setObjects(*((_A,_F),(_A,_G)))
if mibBuilder.loadTexts:clmgmtLicenseExpired.setStatus(_B)
clmgmtLicenseExpiryWarning=NotificationType((1,3,6,1,4,1,9,9,543,0,2))
clmgmtLicenseExpiryWarning.setObjects(*((_A,_F),(_A,_G),(_A,_W)))
if mibBuilder.loadTexts:clmgmtLicenseExpiryWarning.setStatus(_B)
clmgmtLicenseUsageCountExceeded=NotificationType((1,3,6,1,4,1,9,9,543,0,3))
clmgmtLicenseUsageCountExceeded.setObjects(*((_A,_J),(_A,_K),(_A,_V),(_A,_X),(_A,_L)))
if mibBuilder.loadTexts:clmgmtLicenseUsageCountExceeded.setStatus(_B)
clmgmtLicenseUsageCountAboutToExceed=NotificationType((1,3,6,1,4,1,9,9,543,0,4))
clmgmtLicenseUsageCountAboutToExceed.setObjects(*((_A,_J),(_A,_K),(_A,_V),(_A,_e),(_A,_X),(_A,_L)))
if mibBuilder.loadTexts:clmgmtLicenseUsageCountAboutToExceed.setStatus(_B)
clmgmtLicenseInstalled=NotificationType((1,3,6,1,4,1,9,9,543,0,5))
clmgmtLicenseInstalled.setObjects(*((_A,_J),(_A,_K),(_A,_R),(_A,_L)))
if mibBuilder.loadTexts:clmgmtLicenseInstalled.setStatus(_B)
clmgmtLicenseCleared=NotificationType((1,3,6,1,4,1,9,9,543,0,6))
clmgmtLicenseCleared.setObjects(*((_A,_J),(_A,_K),(_A,_R),(_A,_L)))
if mibBuilder.loadTexts:clmgmtLicenseCleared.setStatus(_B)
clmgmtLicenseRevoked=NotificationType((1,3,6,1,4,1,9,9,543,0,7))
clmgmtLicenseRevoked.setObjects(*((_A,_J),(_A,_K),(_A,_R),(_A,_L)))
if mibBuilder.loadTexts:clmgmtLicenseRevoked.setStatus(_B)
clmgmtLicenseEULAAccepted=NotificationType((1,3,6,1,4,1,9,9,543,0,8))
clmgmtLicenseEULAAccepted.setObjects(*((_A,_F),(_A,_G)))
if mibBuilder.loadTexts:clmgmtLicenseEULAAccepted.setStatus(_B)
clmgmtLicenseNotEnforced=NotificationType((1,3,6,1,4,1,9,9,543,0,9))
clmgmtLicenseNotEnforced.setObjects(*((_A,_F),(_A,_G)))
if mibBuilder.loadTexts:clmgmtLicenseNotEnforced.setStatus(_B)
clmgmtLicenseSubscriptionExpiryWarning=NotificationType((1,3,6,1,4,1,9,9,543,0,10))
clmgmtLicenseSubscriptionExpiryWarning.setObjects(*((_A,_F),(_A,_G),(_A,_S)))
if mibBuilder.loadTexts:clmgmtLicenseSubscriptionExpiryWarning.setStatus(_B)
clmgmtLicenseSubscriptionExtExpiryWarning=NotificationType((1,3,6,1,4,1,9,9,543,0,11))
clmgmtLicenseSubscriptionExtExpiryWarning.setObjects(*((_A,_F),(_A,_G),(_A,_S)))
if mibBuilder.loadTexts:clmgmtLicenseSubscriptionExtExpiryWarning.setStatus(_B)
clmgmtLicenseSubscriptionExpired=NotificationType((1,3,6,1,4,1,9,9,543,0,12))
clmgmtLicenseSubscriptionExpired.setObjects(*((_A,_F),(_A,_G),(_A,_S)))
if mibBuilder.loadTexts:clmgmtLicenseSubscriptionExpired.setStatus(_B)
clmgmtLicenseEvalRTUTransitionWarning=NotificationType((1,3,6,1,4,1,9,9,543,0,13))
clmgmtLicenseEvalRTUTransitionWarning.setObjects(*((_A,_F),(_A,_G),(_A,_W)))
if mibBuilder.loadTexts:clmgmtLicenseEvalRTUTransitionWarning.setStatus(_B)
clmgmtLicenseEvalRTUTransition=NotificationType((1,3,6,1,4,1,9,9,543,0,14))
clmgmtLicenseEvalRTUTransition.setObjects(*((_A,_F),(_A,_G)))
if mibBuilder.loadTexts:clmgmtLicenseEvalRTUTransition.setStatus(_B)
clmgmtLicenseUsageNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,543,2,2,8))
clmgmtLicenseUsageNotifGroup.setObjects(*((_A,_As),(_A,_At),(_A,_Au),(_A,_Av)))
if mibBuilder.loadTexts:clmgmtLicenseUsageNotifGroup.setStatus(_B)
clmgmtLicenseDeploymentNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,543,2,2,9))
clmgmtLicenseDeploymentNotifGroup.setObjects(*((_A,_Aw),(_A,_Ax),(_A,_Ay),(_A,_Az)))
if mibBuilder.loadTexts:clmgmtLicenseDeploymentNotifGroup.setStatus(_B)
clmgmtLicenseErrorNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,543,2,2,10))
clmgmtLicenseErrorNotifGroup.setObjects((_A,_A_))
if mibBuilder.loadTexts:clmgmtLicenseErrorNotifGroup.setStatus(_B)
clmgmtLicenseSubscriptionUsageNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,543,2,2,12))
clmgmtLicenseSubscriptionUsageNotifGroup.setObjects(*((_A,_B0),(_A,_B1),(_A,_B2)))
if mibBuilder.loadTexts:clmgmtLicenseSubscriptionUsageNotifGroup.setStatus(_B)
clmgmtLicenseRTUUsageNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,543,2,2,14))
clmgmtLicenseRTUUsageNotifGroup.setObjects(*((_A,_B3),(_A,_B4)))
if mibBuilder.loadTexts:clmgmtLicenseRTUUsageNotifGroup.setStatus(_B)
ciscoLicenseMgmtCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,543,2,1,1))
ciscoLicenseMgmtCompliance.setObjects(*((_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o)))
if mibBuilder.loadTexts:ciscoLicenseMgmtCompliance.setStatus('deprecated')
ciscoLicenseMgmtComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,543,2,1,2))
ciscoLicenseMgmtComplianceRev1.setObjects(*((_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_B5),(_A,_B6),(_A,_B7),(_A,_B8)))
if mibBuilder.loadTexts:ciscoLicenseMgmtComplianceRev1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ClmgmtLicenseIndex':ClmgmtLicenseIndex,_s:ClmgmtLicenseIndexOrZero,_d:ClmgmtLicenseTransferProtocol,'ClmgmtLicenseActionState':ClmgmtLicenseActionState,'ClmgmtLicenseActionFailCause':ClmgmtLicenseActionFailCause,'ciscoLicenseMgmtMIB':ciscoLicenseMgmtMIB,'ciscoLicenseMgmtMIBNotifs':ciscoLicenseMgmtMIBNotifs,_As:clmgmtLicenseExpired,_At:clmgmtLicenseExpiryWarning,_Au:clmgmtLicenseUsageCountExceeded,_Av:clmgmtLicenseUsageCountAboutToExceed,_Aw:clmgmtLicenseInstalled,_Ax:clmgmtLicenseCleared,_Ay:clmgmtLicenseRevoked,_Az:clmgmtLicenseEULAAccepted,_A_:clmgmtLicenseNotEnforced,_B0:clmgmtLicenseSubscriptionExpiryWarning,_B1:clmgmtLicenseSubscriptionExtExpiryWarning,_B2:clmgmtLicenseSubscriptionExpired,_B3:clmgmtLicenseEvalRTUTransitionWarning,_B4:clmgmtLicenseEvalRTUTransition,'ciscoLicenseMgmtMIBObjects':ciscoLicenseMgmtMIBObjects,'clmgmtLicenseConfiguration':clmgmtLicenseConfiguration,_z:clmgmtNextFreeLicenseActionIndex,'clmgmtLicenseActionTable':clmgmtLicenseActionTable,'clmgmtLicenseActionEntry':clmgmtLicenseActionEntry,_c:clmgmtLicenseActionIndex,_A0:clmgmtLicenseActionEntPhysicalIndex,_A1:clmgmtLicenseActionTransferProtocol,_A2:clmgmtLicenseServerAddressType,_A3:clmgmtLicenseServerAddress,_A4:clmgmtLicenseServerUsername,_A5:clmgmtLicenseServerPassword,_A6:clmgmtLicenseFile,_A7:clmgmtLicenseStore,_A8:clmgmtLicenseActionLicenseIndex,_A9:clmgmtLicensePermissionTicketFile,_AA:clmgmtLicenseRehostTicketFile,_AB:clmgmtLicenseBackupFile,_AC:clmgmtLicenseStopOnFailure,_AD:clmgmtLicenseAction,_AE:clmgmtLicenseActionState,_AF:clmgmtLicenseJobQPosition,_AG:clmgmtLicenseActionFailCause,_AH:clmgmtLicenseActionStorageType,_AI:clmgmtLicenseActionRowStatus,_AL:clmgmtLicenseAcceptEULA,_AM:clmgmtLicenseEULAFile,'clmgmtLicenseActionResultTable':clmgmtLicenseActionResultTable,'clmgmtLicenseActionResultEntry':clmgmtLicenseActionResultEntry,_t:clmgmtLicenseNumber,_AJ:clmgmtLicenseIndivActionState,_AK:clmgmtLicenseIndivActionFailCause,'clmgmtLicenseInformation':clmgmtLicenseInformation,'clmgmtLicenseStoreInfoTable':clmgmtLicenseStoreInfoTable,'clmgmtLicenseStoreInfoEntry':clmgmtLicenseStoreInfoEntry,_u:clmgmtLicenseStoreIndex,_AN:clmgmtLicenseStoreName,_AO:clmgmtLicenseStoreTotalSize,_AP:clmgmtLicenseStoreSizeRemaining,'clmgmtLicenseDeviceInfoTable':clmgmtLicenseDeviceInfoTable,'clmgmtLicenseDeviceInfoEntry':clmgmtLicenseDeviceInfoEntry,_AQ:clmgmtDefaultLicenseStore,'clmgmtLicenseInfoTable':clmgmtLicenseInfoTable,'clmgmtLicenseInfoEntry':clmgmtLicenseInfoEntry,_v:clmgmtLicenseStoreUsed,_w:clmgmtLicenseIndex,_J:clmgmtLicenseFeatureName,_K:clmgmtLicenseFeatureVersion,_R:clmgmtLicenseType,_AR:clmgmtLicenseCounted,_AS:clmgmtLicenseValidityPeriod,_AT:clmgmtLicenseValidityPeriodRemaining,_AU:clmgmtLicenseExpiredPeriod,_V:clmgmtLicenseMaxUsageCount,_e:clmgmtLicenseUsageCountRemaining,_AV:clmgmtLicenseEULAStatus,_L:clmgmtLicenseComments,_AW:clmgmtLicenseStatus,_An:clmgmtLicenseStartDate,_Ao:clmgmtLicenseEndDate,_Aq:clmgmtLicensePeriodUsed,'clmgmtLicensableFeatureTable':clmgmtLicensableFeatureTable,'clmgmtLicensableFeatureEntry':clmgmtLicensableFeatureEntry,_x:clmgmtFeatureIndex,_F:clmgmtFeatureName,_G:clmgmtFeatureVersion,_W:clmgmtFeatureValidityPeriodRemaining,_X:clmgmtFeatureWhatIsCounted,_Ap:clmgmtFeatureStartDate,_S:clmgmtFeatureEndDate,_Ar:clmgmtFeaturePeriodUsed,'clmgmtLicenseDeviceInformation':clmgmtLicenseDeviceInformation,_AX:clmgmtNextFreeDevCredExportActionIndex,'clmgmtDevCredExportActionTable':clmgmtDevCredExportActionTable,'clmgmtDevCredExportActionEntry':clmgmtDevCredExportActionEntry,_y:clmgmtDevCredExportActionIndex,_AY:clmgmtDevCredEntPhysicalIndex,_AZ:clmgmtDevCredTransferProtocol,_Aa:clmgmtDevCredServerAddressType,_Ab:clmgmtDevCredServerAddress,_Ac:clmgmtDevCredServerUsername,_Ad:clmgmtDevCredServerPassword,_Ae:clmgmtDevCredExportFile,_Af:clmgmtDevCredCommand,_Ag:clmgmtDevCredCommandState,_Ah:clmgmtDevCredCommandFailCause,_Ai:clmgmtDevCredStorageType,_Aj:clmgmtDevCredRowStatus,'clmgmtLicenseNotifObjects':clmgmtLicenseNotifObjects,_Ak:clmgmtLicenseUsageNotifEnable,_Al:clmgmtLicenseDeploymentNotifEnable,_Am:clmgmtLicenseErrorNotifEnable,'ciscoLicenseMgmtMIBConform':ciscoLicenseMgmtMIBConform,'ciscoLicenseMgmtCompliances':ciscoLicenseMgmtCompliances,'ciscoLicenseMgmtCompliance':ciscoLicenseMgmtCompliance,'ciscoLicenseMgmtComplianceRev1':ciscoLicenseMgmtComplianceRev1,'ciscoLicenseMgmtGroups':ciscoLicenseMgmtGroups,_f:clmgmtLicenseDeploymentGroup,_o:clmgmtLicenseStoreInformationGroup,_g:clmgmtLicenseDeviceInformationGroup,_h:clmgmtLicenseInformationGroup,_i:clmgmtLicensableFeatureInformationGroup,_j:clmgmtLicenseDevCredGroup,_k:clmgmtLicenseNotificationEnableGroup,_l:clmgmtLicenseUsageNotifGroup,_m:clmgmtLicenseDeploymentNotifGroup,_n:clmgmtLicenseErrorNotifGroup,_B5:clmgmtLicenseSubscriptionGroup,_B6:clmgmtLicenseSubscriptionUsageNotifGroup,_B7:clmgmtLicenseRTUGroup,_B8:clmgmtLicenseRTUUsageNotifGroup})