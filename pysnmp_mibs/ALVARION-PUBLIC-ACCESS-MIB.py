_AX='alvarionPublicAccessNASPortsMIBGroup'
_AW='alvarionPublicAccessNotificationGroup'
_AV='alvarionPublicAccessUserConfigMIBGroup'
_AU='alvarionPublicAccessUserMIBGroup'
_AT='alvarionPublicAccessMIBGroup'
_AS='publicAccessUsersLoggedInTrap'
_AR='publicAccessUsersSessionFailTrap'
_AQ='publicAccessUsersSessionStopTrap'
_AP='publicAccessUsersSessionStartTrap'
_AO='publicAccessUsersThresholdTrap'
_AN='publicAccessStatusChangedTrap'
_AM='publicAccessNASPortUserName'
_AL='publicAccessUsersConfigVirtualApProfileIndex'
_AK='publicAccessUsersConfigInterfaceIndex'
_AJ='publicAccessUsersConfigAccountingProfileIndex'
_AI='publicAccessUsersConfigAccountingEnabled'
_AH='publicAccessUsersConfigAuthenTimeout'
_AG='publicAccessUsersConfigAuthenProfileIndex'
_AF='publicAccessUsersConfigAuthenMode'
_AE='publicAccessUsersConfigAuthenType'
_AD='publicAccessUserNASPort'
_AC='publicAccessUserBandwidthControlLevel'
_AB='publicAccessUserMaxReceiveRate'
_AA='publicAccessUserMaxTransmitRate'
_A9='publicAccessUserRateLimitationEnabled'
_A8='publicAccessUserPacketsReceivedDropped'
_A7='publicAccessUserPacketsSentDropped'
_A6='publicAccessUserBytesReceivedDropped'
_A5='publicAccessUserBytesSentDropped'
_A4='publicAccessUserConfigIndex'
_A3='publicAccessUserApRadioIndex'
_A2='publicAccessUserVLAN'
_A1='publicAccessUserPHYType'
_A0='publicAccessUserSecurity'
_z='publicAccessUserSSID'
_y='publicAccessUserGroupName'
_x='publicAccessUserForceDisconnection'
_w='publicAccessUserPacketsReceived'
_v='publicAccessUserPacketsSent'
_u='publicAccessUserIdleTime'
_t='publicAccessUserSessionStartTime'
_s='publicAccessUserState'
_r='publicAccessUserAuthenMode'
_q='publicAccessUserAuthenType'
_p='publicAccessNASPortCount'
_o='publicAccessUsersLoggedInTrapInterval'
_n='publicAccessUsersLoggedInTrapEnabled'
_m='publicAccessUsersSessionTrapEnabled'
_l='publicAccessUsersThreshold'
_k='publicAccessUsersMaxCount'
_j='publicAccessDeviceForceReconfiguration'
_i='publicAccessDeviceAccountingProfileIndex'
_h='publicAccessDeviceAccountingEnabled'
_g='publicAccessDeviceAuthenProfileIndex'
_f='publicAccessDeviceConfigMode'
_e='publicAccessDeviceSessionTimeoutOperStatus'
_d='publicAccessDeviceSessionTimeoutAdminStatus'
_c='publicAccessDeviceUserPassword'
_b='publicAccessDeviceUserName'
_a='publicAccessNASPortIndex'
_Z='publicAccessUserIndex'
_Y='publicAccessUsersConfigIndex'
_X='disable'
_W='enable'
_V='minutes'
_U='publicAccessUserConnectedInterface'
_T='publicAccessUserApMacAddress'
_S='publicAccessUserStationMacAddress'
_R='publicAccessUserBytesReceived'
_Q='publicAccessUserBytesSent'
_P='publicAccessUserSessionDuration'
_O='publicAccessUserStationIpAddress'
_N='publicAccessStatusChangedCause'
_M='publicAccessStatus'
_L='not-accessible'
_K='AlvarionNotificationEnable'
_J='publicAccessUsersCount'
_I='seconds'
_H='Unsigned32'
_G='publicAccessUserName'
_F='OctetString'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='current'
_A='ALVARION-PUBLIC-ACCESS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
alvarionMgmtV2,=mibBuilder.importSymbols('ALVARION-SMI','alvarionMgmtV2')
AlvarionNotificationEnable,AlvarionPriorityQueue,AlvarionProfileIndexOrZero,AlvarionSSIDOrNone,AlvarionSecurity,AlvarionUsersAuthenticationMode,AlvarionUsersAuthenticationType=mibBuilder.importSymbols('ALVARION-TC',_K,'AlvarionPriorityQueue','AlvarionProfileIndexOrZero','AlvarionSSIDOrNone','AlvarionSecurity','AlvarionUsersAuthenticationMode','AlvarionUsersAuthenticationType')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','TextualConvention','TruthValue')
alvarionPublicAccessMIB=ModuleIdentity((1,3,6,1,4,1,12394,1,10,5,1))
_AlvarionPublicAccessMIBObjects_ObjectIdentity=ObjectIdentity
alvarionPublicAccessMIBObjects=_AlvarionPublicAccessMIBObjects_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,1,1))
_PublicAccessGroup_ObjectIdentity=ObjectIdentity
publicAccessGroup=_PublicAccessGroup_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,1,1,1))
class _PublicAccessStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_PublicAccessStatus_Type.__name__=_D
_PublicAccessStatus_Object=MibScalar
publicAccessStatus=_PublicAccessStatus_Object((1,3,6,1,4,1,12394,1,10,5,1,1,1,1),_PublicAccessStatus_Type())
publicAccessStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:publicAccessStatus.setStatus(_B)
class _PublicAccessStatusChangedCause_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,253))
_PublicAccessStatusChangedCause_Type.__name__=_F
_PublicAccessStatusChangedCause_Object=MibScalar
publicAccessStatusChangedCause=_PublicAccessStatusChangedCause_Object((1,3,6,1,4,1,12394,1,10,5,1,1,1,2),_PublicAccessStatusChangedCause_Type())
publicAccessStatusChangedCause.setMaxAccess(_C)
if mibBuilder.loadTexts:publicAccessStatusChangedCause.setStatus(_B)
_PublicAccessDeviceGroup_ObjectIdentity=ObjectIdentity
publicAccessDeviceGroup=_PublicAccessDeviceGroup_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,1,1,2))
class _PublicAccessDeviceUserName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,253))
_PublicAccessDeviceUserName_Type.__name__=_F
_PublicAccessDeviceUserName_Object=MibScalar
publicAccessDeviceUserName=_PublicAccessDeviceUserName_Object((1,3,6,1,4,1,12394,1,10,5,1,1,2,1),_PublicAccessDeviceUserName_Type())
publicAccessDeviceUserName.setMaxAccess(_E)
if mibBuilder.loadTexts:publicAccessDeviceUserName.setStatus(_B)
class _PublicAccessDeviceUserPassword_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,230))
_PublicAccessDeviceUserPassword_Type.__name__=_F
_PublicAccessDeviceUserPassword_Object=MibScalar
publicAccessDeviceUserPassword=_PublicAccessDeviceUserPassword_Object((1,3,6,1,4,1,12394,1,10,5,1,1,2,2),_PublicAccessDeviceUserPassword_Type())
publicAccessDeviceUserPassword.setMaxAccess(_E)
if mibBuilder.loadTexts:publicAccessDeviceUserPassword.setStatus(_B)
class _PublicAccessDeviceSessionTimeoutAdminStatus_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,9999))
_PublicAccessDeviceSessionTimeoutAdminStatus_Type.__name__=_H
_PublicAccessDeviceSessionTimeoutAdminStatus_Object=MibScalar
publicAccessDeviceSessionTimeoutAdminStatus=_PublicAccessDeviceSessionTimeoutAdminStatus_Object((1,3,6,1,4,1,12394,1,10,5,1,1,2,3),_PublicAccessDeviceSessionTimeoutAdminStatus_Type())
publicAccessDeviceSessionTimeoutAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:publicAccessDeviceSessionTimeoutAdminStatus.setStatus(_B)
if mibBuilder.loadTexts:publicAccessDeviceSessionTimeoutAdminStatus.setUnits(_V)
_PublicAccessDeviceSessionTimeoutOperStatus_Type=Unsigned32
_PublicAccessDeviceSessionTimeoutOperStatus_Object=MibScalar
publicAccessDeviceSessionTimeoutOperStatus=_PublicAccessDeviceSessionTimeoutOperStatus_Object((1,3,6,1,4,1,12394,1,10,5,1,1,2,4),_PublicAccessDeviceSessionTimeoutOperStatus_Type())
publicAccessDeviceSessionTimeoutOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:publicAccessDeviceSessionTimeoutOperStatus.setStatus(_B)
if mibBuilder.loadTexts:publicAccessDeviceSessionTimeoutOperStatus.setUnits(_I)
_PublicAccessDeviceConfigMode_Type=AlvarionUsersAuthenticationMode
_PublicAccessDeviceConfigMode_Object=MibScalar
publicAccessDeviceConfigMode=_PublicAccessDeviceConfigMode_Object((1,3,6,1,4,1,12394,1,10,5,1,1,2,5),_PublicAccessDeviceConfigMode_Type())
publicAccessDeviceConfigMode.setMaxAccess(_C)
if mibBuilder.loadTexts:publicAccessDeviceConfigMode.setStatus(_B)
_PublicAccessDeviceAuthenProfileIndex_Type=AlvarionProfileIndexOrZero
_PublicAccessDeviceAuthenProfileIndex_Object=MibScalar
publicAccessDeviceAuthenProfileIndex=_PublicAccessDeviceAuthenProfileIndex_Object((1,3,6,1,4,1,12394,1,10,5,1,1,2,6),_PublicAccessDeviceAuthenProfileIndex_Type())
publicAccessDeviceAuthenProfileIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:publicAccessDeviceAuthenProfileIndex.setStatus(_B)
class _PublicAccessDeviceAccountingEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),(_X,2)))
_PublicAccessDeviceAccountingEnabled_Type.__name__=_D
_PublicAccessDeviceAccountingEnabled_Object=MibScalar
publicAccessDeviceAccountingEnabled=_PublicAccessDeviceAccountingEnabled_Object((1,3,6,1,4,1,12394,1,10,5,1,1,2,7),_PublicAccessDeviceAccountingEnabled_Type())
publicAccessDeviceAccountingEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:publicAccessDeviceAccountingEnabled.setStatus(_B)
_PublicAccessDeviceAccountingProfileIndex_Type=AlvarionProfileIndexOrZero
_PublicAccessDeviceAccountingProfileIndex_Object=MibScalar
publicAccessDeviceAccountingProfileIndex=_PublicAccessDeviceAccountingProfileIndex_Object((1,3,6,1,4,1,12394,1,10,5,1,1,2,8),_PublicAccessDeviceAccountingProfileIndex_Type())
publicAccessDeviceAccountingProfileIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:publicAccessDeviceAccountingProfileIndex.setStatus(_B)
class _PublicAccessDeviceForceReconfiguration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('idle',0),('forceReconfiguration',1)))
_PublicAccessDeviceForceReconfiguration_Type.__name__=_D
_PublicAccessDeviceForceReconfiguration_Object=MibScalar
publicAccessDeviceForceReconfiguration=_PublicAccessDeviceForceReconfiguration_Object((1,3,6,1,4,1,12394,1,10,5,1,1,2,9),_PublicAccessDeviceForceReconfiguration_Type())
publicAccessDeviceForceReconfiguration.setMaxAccess(_E)
if mibBuilder.loadTexts:publicAccessDeviceForceReconfiguration.setStatus(_B)
_PublicAccessUsersGroup_ObjectIdentity=ObjectIdentity
publicAccessUsersGroup=_PublicAccessUsersGroup_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,1,1,3))
_PublicAccessUsersMaxCount_Type=Unsigned32
_PublicAccessUsersMaxCount_Object=MibScalar
publicAccessUsersMaxCount=_PublicAccessUsersMaxCount_Object((1,3,6,1,4,1,12394,1,10,5,1,1,3,1),_PublicAccessUsersMaxCount_Type())
publicAccessUsersMaxCount.setMaxAccess(_C)
if mibBuilder.loadTexts:publicAccessUsersMaxCount.setStatus(_B)
_PublicAccessUsersCount_Type=Gauge32
_PublicAccessUsersCount_Object=MibScalar
publicAccessUsersCount=_PublicAccessUsersCount_Object((1,3,6,1,4,1,12394,1,10,5,1,1,3,2),_PublicAccessUsersCount_Type())
publicAccessUsersCount.setMaxAccess(_C)
if mibBuilder.loadTexts:publicAccessUsersCount.setStatus(_B)
_PublicAccessUsersThreshold_Type=Unsigned32
_PublicAccessUsersThreshold_Object=MibScalar
publicAccessUsersThreshold=_PublicAccessUsersThreshold_Object((1,3,6,1,4,1,12394,1,10,5,1,1,3,3),_PublicAccessUsersThreshold_Type())
publicAccessUsersThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:publicAccessUsersThreshold.setStatus(_B)
class _PublicAccessUsersSessionTrapEnabled_Type(AlvarionNotificationEnable):defaultValue=2
_PublicAccessUsersSessionTrapEnabled_Type.__name__=_K
_PublicAccessUsersSessionTrapEnabled_Object=MibScalar
publicAccessUsersSessionTrapEnabled=_PublicAccessUsersSessionTrapEnabled_Object((1,3,6,1,4,1,12394,1,10,5,1,1,3,4),_PublicAccessUsersSessionTrapEnabled_Type())
publicAccessUsersSessionTrapEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:publicAccessUsersSessionTrapEnabled.setStatus(_B)
_PublicAccessUsersConfigTable_Object=MibTable
publicAccessUsersConfigTable=_PublicAccessUsersConfigTable_Object((1,3,6,1,4,1,12394,1,10,5,1,1,3,5))
if mibBuilder.loadTexts:publicAccessUsersConfigTable.setStatus(_B)
_PublicAccessUsersConfigEntry_Object=MibTableRow
publicAccessUsersConfigEntry=_PublicAccessUsersConfigEntry_Object((1,3,6,1,4,1,12394,1,10,5,1,1,3,5,1))
publicAccessUsersConfigEntry.setIndexNames((0,_A,_Y))
if mibBuilder.loadTexts:publicAccessUsersConfigEntry.setStatus(_B)
class _PublicAccessUsersConfigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PublicAccessUsersConfigIndex_Type.__name__=_D
_PublicAccessUsersConfigIndex_Object=MibTableColumn
publicAccessUsersConfigIndex=_PublicAccessUsersConfigIndex_Object((1,3,6,1,4,1,12394,1,10,5,1,1,3,5,1,1),_PublicAccessUsersConfigIndex_Type())
publicAccessUsersConfigIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:publicAccessUsersConfigIndex.setStatus(_B)
_PublicAccessUsersConfigAuthenType_Type=AlvarionUsersAuthenticationType
_PublicAccessUsersConfigAuthenType_Object=MibTableColumn
publicAccessUsersConfigAuthenType=_PublicAccessUsersConfigAuthenType_Object((1,3,6,1,4,1,12394,1,10,5,1,1,3,5,1,2),_PublicAccessUsersConfigAuthenType_Type())
publicAccessUsersConfigAuthenType.setMaxAccess(_C)
if mibBuilder.loadTexts:publicAccessUsersConfigAuthenType.setStatus(_B)
_PublicAccessUsersConfigAuthenMode_Type=AlvarionUsersAuthenticationMode
_PublicAccessUsersConfigAuthenMode_Object=MibTableColumn
publicAccessUsersConfigAuthenMode=_PublicAccessUsersConfigAuthenMode_Object((1,3,6,1,4,1,12394,1,10,5,1,1,3,5,1,3),_PublicAccessUsersConfigAuthenMode_Type())
publicAccessUsersConfigAuthenMode.setMaxAccess(_C)
if mibBuilder.loadTexts:publicAccessUsersConfigAuthenMode.setStatus(_B)
_PublicAccessUsersConfigAuthenProfileIndex_Type=AlvarionProfileIndexOrZero
_PublicAccessUsersConfigAuthenProfileIndex_Object=MibTableColumn
publicAccessUsersConfigAuthenProfileIndex=_PublicAccessUsersConfigAuthenProfileIndex_Object((1,3,6,1,4,1,12394,1,10,5,1,1,3,5,1,4),_PublicAccessUsersConfigAuthenProfileIndex_Type())
publicAccessUsersConfigAuthenProfileIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:publicAccessUsersConfigAuthenProfileIndex.setStatus(_B)
class _PublicAccessUsersConfigAuthenTimeout_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PublicAccessUsersConfigAuthenTimeout_Type.__name__=_H
_PublicAccessUsersConfigAuthenTimeout_Object=MibTableColumn
publicAccessUsersConfigAuthenTimeout=_PublicAccessUsersConfigAuthenTimeout_Object((1,3,6,1,4,1,12394,1,10,5,1,1,3,5,1,5),_PublicAccessUsersConfigAuthenTimeout_Type())
publicAccessUsersConfigAuthenTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:publicAccessUsersConfigAuthenTimeout.setStatus(_B)
if mibBuilder.loadTexts:publicAccessUsersConfigAuthenTimeout.setUnits(_I)
class _PublicAccessUsersConfigAccountingEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),(_X,2)))
_PublicAccessUsersConfigAccountingEnabled_Type.__name__=_D
_PublicAccessUsersConfigAccountingEnabled_Object=MibTableColumn
publicAccessUsersConfigAccountingEnabled=_PublicAccessUsersConfigAccountingEnabled_Object((1,3,6,1,4,1,12394,1,10,5,1,1,3,5,1,6),_PublicAccessUsersConfigAccountingEnabled_Type())
publicAccessUsersConfigAccountingEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:publicAccessUsersConfigAccountingEnabled.setStatus(_B)
_PublicAccessUsersConfigAccountingProfileIndex_Type=AlvarionProfileIndexOrZero
_PublicAccessUsersConfigAccountingProfileIndex_Object=MibTableColumn
publicAccessUsersConfigAccountingProfileIndex=_PublicAccessUsersConfigAccountingProfileIndex_Object((1,3,6,1,4,1,12394,1,10,5,1,1,3,5,1,7),_PublicAccessUsersConfigAccountingProfileIndex_Type())
publicAccessUsersConfigAccountingProfileIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:publicAccessUsersConfigAccountingProfileIndex.setStatus(_B)
_PublicAccessUsersConfigInterfaceIndex_Type=InterfaceIndex
_PublicAccessUsersConfigInterfaceIndex_Object=MibTableColumn
publicAccessUsersConfigInterfaceIndex=_PublicAccessUsersConfigInterfaceIndex_Object((1,3,6,1,4,1,12394,1,10,5,1,1,3,5,1,8),_PublicAccessUsersConfigInterfaceIndex_Type())
publicAccessUsersConfigInterfaceIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:publicAccessUsersConfigInterfaceIndex.setStatus(_B)
class _PublicAccessUsersConfigVirtualApProfileIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PublicAccessUsersConfigVirtualApProfileIndex_Type.__name__=_D
_PublicAccessUsersConfigVirtualApProfileIndex_Object=MibTableColumn
publicAccessUsersConfigVirtualApProfileIndex=_PublicAccessUsersConfigVirtualApProfileIndex_Object((1,3,6,1,4,1,12394,1,10,5,1,1,3,5,1,9),_PublicAccessUsersConfigVirtualApProfileIndex_Type())
publicAccessUsersConfigVirtualApProfileIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:publicAccessUsersConfigVirtualApProfileIndex.setStatus(_B)
_PublicAccessUserTable_Object=MibTable
publicAccessUserTable=_PublicAccessUserTable_Object((1,3,6,1,4,1,12394,1,10,5,1,1,3,6))
if mibBuilder.loadTexts:publicAccessUserTable.setStatus(_B)
_PublicAccessUserEntry_Object=MibTableRow
publicAccessUserEntry=_PublicAccessUserEntry_Object((1,3,6,1,4,1,12394,1,10,5,1,1,3,6,1))
publicAccessUserEntry.setIndexNames((0,_A,_Z))
if mibBuilder.loadTexts:publicAccessUserEntry.setStatus(_B)
class _PublicAccessUserIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PublicAccessUserIndex_Type.__name__=_D
_PublicAccessUserIndex_Object=MibTableColumn
publicAccessUserIndex=_PublicAccessUserIndex_Object((1,3,6,1,4,1,12394,1,10,5,1,1,3,6,1,1),_PublicAccessUserIndex_Type())
publicAccessUserIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:publicAccessUserIndex.setStatus(_B)
_PublicAccessUserAuthenType_Type=AlvarionUsersAuthenticationType
_PublicAccessUserAuthenType_Object=MibTableColumn
publicAccessUserAuthenType=_PublicAccessUserAuthenType_Object((1,3,6,1,4,1,12394,1,10,5,1,1,3,6,1,2),_PublicAccessUserAuthenType_Type())
publicAccessUserAuthenType.setMaxAccess(_C)
if mibBuilder.loadTexts:publicAccessUserAuthenType.setStatus(_B)
_PublicAccessUserAuthenMode_Type=AlvarionUsersAuthenticationMode
_PublicAccessUserAuthenMode_Object=MibTableColumn
publicAccessUserAuthenMode=_PublicAccessUserAuthenMode_Object((1,3,6,1,4,1,12394,1,10,5,1,1,3,6,1,3),_PublicAccessUserAuthenMode_Type())
publicAccessUserAuthenMode.setMaxAccess(_C)
if mibBuilder.loadTexts:publicAccessUserAuthenMode.setStatus(_B)
class _PublicAccessUserState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('unassigned',0),('connecting',1),('connected',2),('reconnecting',3),('disconnecting',4),('disconnected',5),('disconnectingAdministrative',6),('disconnectedAdministrative',7)))
_PublicAccessUserState_Type.__name__=_D
_PublicAccessUserState_Object=MibTableColumn
publicAccessUserState=_PublicAccessUserState_Object((1,3,6,1,4,1,12394,1,10,5,1,1,3,6,1,4),_PublicAccessUserState_Type())
publicAccessUserState.setMaxAccess(_C)
if mibBuilder.loadTexts:publicAccessUserState.setStatus(_B)
_PublicAccessUserStationIpAddress_Type=IpAddress
_PublicAccessUserStationIpAddress_Object=MibTableColumn
publicAccessUserStationIpAddress=_PublicAccessUserStationIpAddress_Object((1,3,6,1,4,1,12394,1,10,5,1,1,3,6,1,5),_PublicAccessUserStationIpAddress_Type())
publicAccessUserStationIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:publicAccessUserStationIpAddress.setStatus(_B)
class _PublicAccessUserName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,253))
_PublicAccessUserName_Type.__name__=_F
_PublicAccessUserName_Object=MibTableColumn
publicAccessUserName=_PublicAccessUserName_Object((1,3,6,1,4,1,12394,1,10,5,1,1,3,6,1,6),_PublicAccessUserName_Type())
publicAccessUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:publicAccessUserName.setStatus(_B)
_PublicAccessUserSessionStartTime_Type=DateAndTime
_PublicAccessUserSessionStartTime_Object=MibTableColumn
publicAccessUserSessionStartTime=_PublicAccessUserSessionStartTime_Object((1,3,6,1,4,1,12394,1,10,5,1,1,3,6,1,7),_PublicAccessUserSessionStartTime_Type())
publicAccessUserSessionStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:publicAccessUserSessionStartTime.setStatus(_B)
_PublicAccessUserSessionDuration_Type=Counter32
_PublicAccessUserSessionDuration_Object=MibTableColumn
publicAccessUserSessionDuration=_PublicAccessUserSessionDuration_Object((1,3,6,1,4,1,12394,1,10,5,1,1,3,6,1,8),_PublicAccessUserSessionDuration_Type())
publicAccessUserSessionDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:publicAccessUserSessionDuration.setStatus(_B)
if mibBuilder.loadTexts:publicAccessUserSessionDuration.setUnits(_I)
_PublicAccessUserIdleTime_Type=Counter32
_PublicAccessUserIdleTime_Object=MibTableColumn
publicAccessUserIdleTime=_PublicAccessUserIdleTime_Object((1,3,6,1,4,1,12394,1,10,5,1,1,3,6,1,9),_PublicAccessUserIdleTime_Type())
publicAccessUserIdleTime.setMaxAccess(_C)
if mibBuilder.loadTexts:publicAccessUserIdleTime.setStatus(_B)
if mibBuilder.loadTexts:publicAccessUserIdleTime.setUnits(_I)
_PublicAccessUserBytesSent_Type=Counter64
_PublicAccessUserBytesSent_Object=MibTableColumn
publicAccessUserBytesSent=_PublicAccessUserBytesSent_Object((1,3,6,1,4,1,12394,1,10,5,1,1,3,6,1,10),_PublicAccessUserBytesSent_Type())
publicAccessUserBytesSent.setMaxAccess(_C)
if mibBuilder.loadTexts:publicAccessUserBytesSent.setStatus(_B)
_PublicAccessUserBytesReceived_Type=Counter64
_PublicAccessUserBytesReceived_Object=MibTableColumn
publicAccessUserBytesReceived=_PublicAccessUserBytesReceived_Object((1,3,6,1,4,1,12394,1,10,5,1,1,3,6,1,11),_PublicAccessUserBytesReceived_Type())
publicAccessUserBytesReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:publicAccessUserBytesReceived.setStatus(_B)
_PublicAccessUserPacketsSent_Type=Counter32
_PublicAccessUserPacketsSent_Object=MibTableColumn
publicAccessUserPacketsSent=_PublicAccessUserPacketsSent_Object((1,3,6,1,4,1,12394,1,10,5,1,1,3,6,1,12),_PublicAccessUserPacketsSent_Type())
publicAccessUserPacketsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:publicAccessUserPacketsSent.setStatus(_B)
_PublicAccessUserPacketsReceived_Type=Counter32
_PublicAccessUserPacketsReceived_Object=MibTableColumn
publicAccessUserPacketsReceived=_PublicAccessUserPacketsReceived_Object((1,3,6,1,4,1,12394,1,10,5,1,1,3,6,1,13),_PublicAccessUserPacketsReceived_Type())
publicAccessUserPacketsReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:publicAccessUserPacketsReceived.setStatus(_B)
class _PublicAccessUserForceDisconnection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('idle',0),('adminReset',1)))
_PublicAccessUserForceDisconnection_Type.__name__=_D
_PublicAccessUserForceDisconnection_Object=MibTableColumn
publicAccessUserForceDisconnection=_PublicAccessUserForceDisconnection_Object((1,3,6,1,4,1,12394,1,10,5,1,1,3,6,1,14),_PublicAccessUserForceDisconnection_Type())
publicAccessUserForceDisconnection.setMaxAccess(_E)
if mibBuilder.loadTexts:publicAccessUserForceDisconnection.setStatus(_B)
_PublicAccessUserStationMacAddress_Type=MacAddress
_PublicAccessUserStationMacAddress_Object=MibTableColumn
publicAccessUserStationMacAddress=_PublicAccessUserStationMacAddress_Object((1,3,6,1,4,1,12394,1,10,5,1,1,3,6,1,15),_PublicAccessUserStationMacAddress_Type())
publicAccessUserStationMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:publicAccessUserStationMacAddress.setStatus(_B)
_PublicAccessUserApMacAddress_Type=MacAddress
_PublicAccessUserApMacAddress_Object=MibTableColumn
publicAccessUserApMacAddress=_PublicAccessUserApMacAddress_Object((1,3,6,1,4,1,12394,1,10,5,1,1,3,6,1,16),_PublicAccessUserApMacAddress_Type())
publicAccessUserApMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:publicAccessUserApMacAddress.setStatus(_B)
class _PublicAccessUserGroupName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_PublicAccessUserGroupName_Type.__name__=_F
_PublicAccessUserGroupName_Object=MibTableColumn
publicAccessUserGroupName=_PublicAccessUserGroupName_Object((1,3,6,1,4,1,12394,1,10,5,1,1,3,6,1,17),_PublicAccessUserGroupName_Type())
publicAccessUserGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:publicAccessUserGroupName.setStatus(_B)
_PublicAccessUserSSID_Type=AlvarionSSIDOrNone
_PublicAccessUserSSID_Object=MibTableColumn
publicAccessUserSSID=_PublicAccessUserSSID_Object((1,3,6,1,4,1,12394,1,10,5,1,1,3,6,1,18),_PublicAccessUserSSID_Type())
publicAccessUserSSID.setMaxAccess(_C)
if mibBuilder.loadTexts:publicAccessUserSSID.setStatus(_B)
_PublicAccessUserSecurity_Type=AlvarionSecurity
_PublicAccessUserSecurity_Object=MibTableColumn
publicAccessUserSecurity=_PublicAccessUserSecurity_Object((1,3,6,1,4,1,12394,1,10,5,1,1,3,6,1,19),_PublicAccessUserSecurity_Type())
publicAccessUserSecurity.setMaxAccess(_C)
if mibBuilder.loadTexts:publicAccessUserSecurity.setStatus(_B)
class _PublicAccessUserPHYType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('unknown',0),('ieee802dot11a',1),('ieee802dot11b',2),('ieee802dot11g',3)))
_PublicAccessUserPHYType_Type.__name__=_D
_PublicAccessUserPHYType_Object=MibTableColumn
publicAccessUserPHYType=_PublicAccessUserPHYType_Object((1,3,6,1,4,1,12394,1,10,5,1,1,3,6,1,20),_PublicAccessUserPHYType_Type())
publicAccessUserPHYType.setMaxAccess(_C)
if mibBuilder.loadTexts:publicAccessUserPHYType.setStatus(_B)
class _PublicAccessUserVLAN_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_PublicAccessUserVLAN_Type.__name__=_D
_PublicAccessUserVLAN_Object=MibTableColumn
publicAccessUserVLAN=_PublicAccessUserVLAN_Object((1,3,6,1,4,1,12394,1,10,5,1,1,3,6,1,21),_PublicAccessUserVLAN_Type())
publicAccessUserVLAN.setMaxAccess(_C)
if mibBuilder.loadTexts:publicAccessUserVLAN.setStatus(_B)
class _PublicAccessUserApRadioIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PublicAccessUserApRadioIndex_Type.__name__=_D
_PublicAccessUserApRadioIndex_Object=MibTableColumn
publicAccessUserApRadioIndex=_PublicAccessUserApRadioIndex_Object((1,3,6,1,4,1,12394,1,10,5,1,1,3,6,1,22),_PublicAccessUserApRadioIndex_Type())
publicAccessUserApRadioIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:publicAccessUserApRadioIndex.setStatus(_B)
class _PublicAccessUserConfigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PublicAccessUserConfigIndex_Type.__name__=_D
_PublicAccessUserConfigIndex_Object=MibTableColumn
publicAccessUserConfigIndex=_PublicAccessUserConfigIndex_Object((1,3,6,1,4,1,12394,1,10,5,1,1,3,6,1,23),_PublicAccessUserConfigIndex_Type())
publicAccessUserConfigIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:publicAccessUserConfigIndex.setStatus(_B)
class _PublicAccessUserConnectedInterface_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_PublicAccessUserConnectedInterface_Type.__name__=_F
_PublicAccessUserConnectedInterface_Object=MibTableColumn
publicAccessUserConnectedInterface=_PublicAccessUserConnectedInterface_Object((1,3,6,1,4,1,12394,1,10,5,1,1,3,6,1,24),_PublicAccessUserConnectedInterface_Type())
publicAccessUserConnectedInterface.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:publicAccessUserConnectedInterface.setStatus(_B)
_PublicAccessUserBytesSentDropped_Type=Counter64
_PublicAccessUserBytesSentDropped_Object=MibTableColumn
publicAccessUserBytesSentDropped=_PublicAccessUserBytesSentDropped_Object((1,3,6,1,4,1,12394,1,10,5,1,1,3,6,1,25),_PublicAccessUserBytesSentDropped_Type())
publicAccessUserBytesSentDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:publicAccessUserBytesSentDropped.setStatus(_B)
_PublicAccessUserBytesReceivedDropped_Type=Counter64
_PublicAccessUserBytesReceivedDropped_Object=MibTableColumn
publicAccessUserBytesReceivedDropped=_PublicAccessUserBytesReceivedDropped_Object((1,3,6,1,4,1,12394,1,10,5,1,1,3,6,1,26),_PublicAccessUserBytesReceivedDropped_Type())
publicAccessUserBytesReceivedDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:publicAccessUserBytesReceivedDropped.setStatus(_B)
_PublicAccessUserPacketsSentDropped_Type=Counter32
_PublicAccessUserPacketsSentDropped_Object=MibTableColumn
publicAccessUserPacketsSentDropped=_PublicAccessUserPacketsSentDropped_Object((1,3,6,1,4,1,12394,1,10,5,1,1,3,6,1,27),_PublicAccessUserPacketsSentDropped_Type())
publicAccessUserPacketsSentDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:publicAccessUserPacketsSentDropped.setStatus(_B)
_PublicAccessUserPacketsReceivedDropped_Type=Counter32
_PublicAccessUserPacketsReceivedDropped_Object=MibTableColumn
publicAccessUserPacketsReceivedDropped=_PublicAccessUserPacketsReceivedDropped_Object((1,3,6,1,4,1,12394,1,10,5,1,1,3,6,1,28),_PublicAccessUserPacketsReceivedDropped_Type())
publicAccessUserPacketsReceivedDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:publicAccessUserPacketsReceivedDropped.setStatus(_B)
_PublicAccessUserRateLimitationEnabled_Type=TruthValue
_PublicAccessUserRateLimitationEnabled_Object=MibTableColumn
publicAccessUserRateLimitationEnabled=_PublicAccessUserRateLimitationEnabled_Object((1,3,6,1,4,1,12394,1,10,5,1,1,3,6,1,29),_PublicAccessUserRateLimitationEnabled_Type())
publicAccessUserRateLimitationEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:publicAccessUserRateLimitationEnabled.setStatus(_B)
class _PublicAccessUserMaxTransmitRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,1000000))
_PublicAccessUserMaxTransmitRate_Type.__name__=_D
_PublicAccessUserMaxTransmitRate_Object=MibTableColumn
publicAccessUserMaxTransmitRate=_PublicAccessUserMaxTransmitRate_Object((1,3,6,1,4,1,12394,1,10,5,1,1,3,6,1,30),_PublicAccessUserMaxTransmitRate_Type())
publicAccessUserMaxTransmitRate.setMaxAccess(_C)
if mibBuilder.loadTexts:publicAccessUserMaxTransmitRate.setStatus(_B)
class _PublicAccessUserMaxReceiveRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,1000000))
_PublicAccessUserMaxReceiveRate_Type.__name__=_D
_PublicAccessUserMaxReceiveRate_Object=MibTableColumn
publicAccessUserMaxReceiveRate=_PublicAccessUserMaxReceiveRate_Object((1,3,6,1,4,1,12394,1,10,5,1,1,3,6,1,31),_PublicAccessUserMaxReceiveRate_Type())
publicAccessUserMaxReceiveRate.setMaxAccess(_C)
if mibBuilder.loadTexts:publicAccessUserMaxReceiveRate.setStatus(_B)
_PublicAccessUserBandwidthControlLevel_Type=AlvarionPriorityQueue
_PublicAccessUserBandwidthControlLevel_Object=MibTableColumn
publicAccessUserBandwidthControlLevel=_PublicAccessUserBandwidthControlLevel_Object((1,3,6,1,4,1,12394,1,10,5,1,1,3,6,1,32),_PublicAccessUserBandwidthControlLevel_Type())
publicAccessUserBandwidthControlLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:publicAccessUserBandwidthControlLevel.setStatus(_B)
_PublicAccessUserNASPort_Type=Unsigned32
_PublicAccessUserNASPort_Object=MibTableColumn
publicAccessUserNASPort=_PublicAccessUserNASPort_Object((1,3,6,1,4,1,12394,1,10,5,1,1,3,6,1,33),_PublicAccessUserNASPort_Type())
publicAccessUserNASPort.setMaxAccess(_C)
if mibBuilder.loadTexts:publicAccessUserNASPort.setStatus(_B)
class _PublicAccessUsersLoggedInTrapEnabled_Type(AlvarionNotificationEnable):defaultValue=2
_PublicAccessUsersLoggedInTrapEnabled_Type.__name__=_K
_PublicAccessUsersLoggedInTrapEnabled_Object=MibScalar
publicAccessUsersLoggedInTrapEnabled=_PublicAccessUsersLoggedInTrapEnabled_Object((1,3,6,1,4,1,12394,1,10,5,1,1,3,7),_PublicAccessUsersLoggedInTrapEnabled_Type())
publicAccessUsersLoggedInTrapEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:publicAccessUsersLoggedInTrapEnabled.setStatus(_B)
class _PublicAccessUsersLoggedInTrapInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_PublicAccessUsersLoggedInTrapInterval_Type.__name__=_H
_PublicAccessUsersLoggedInTrapInterval_Object=MibScalar
publicAccessUsersLoggedInTrapInterval=_PublicAccessUsersLoggedInTrapInterval_Object((1,3,6,1,4,1,12394,1,10,5,1,1,3,8),_PublicAccessUsersLoggedInTrapInterval_Type())
publicAccessUsersLoggedInTrapInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:publicAccessUsersLoggedInTrapInterval.setStatus(_B)
if mibBuilder.loadTexts:publicAccessUsersLoggedInTrapInterval.setUnits(_V)
_PublicAccessNASPortsGroup_ObjectIdentity=ObjectIdentity
publicAccessNASPortsGroup=_PublicAccessNASPortsGroup_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,1,1,4))
_PublicAccessNASPortCount_Type=Gauge32
_PublicAccessNASPortCount_Object=MibScalar
publicAccessNASPortCount=_PublicAccessNASPortCount_Object((1,3,6,1,4,1,12394,1,10,5,1,1,4,1),_PublicAccessNASPortCount_Type())
publicAccessNASPortCount.setMaxAccess(_C)
if mibBuilder.loadTexts:publicAccessNASPortCount.setStatus(_B)
_PublicAccessNASPortTable_Object=MibTable
publicAccessNASPortTable=_PublicAccessNASPortTable_Object((1,3,6,1,4,1,12394,1,10,5,1,1,4,2))
if mibBuilder.loadTexts:publicAccessNASPortTable.setStatus(_B)
_PublicAccessNASPortEntry_Object=MibTableRow
publicAccessNASPortEntry=_PublicAccessNASPortEntry_Object((1,3,6,1,4,1,12394,1,10,5,1,1,4,2,1))
publicAccessNASPortEntry.setIndexNames((0,_A,_a))
if mibBuilder.loadTexts:publicAccessNASPortEntry.setStatus(_B)
class _PublicAccessNASPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PublicAccessNASPortIndex_Type.__name__=_D
_PublicAccessNASPortIndex_Object=MibTableColumn
publicAccessNASPortIndex=_PublicAccessNASPortIndex_Object((1,3,6,1,4,1,12394,1,10,5,1,1,4,2,1,1),_PublicAccessNASPortIndex_Type())
publicAccessNASPortIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:publicAccessNASPortIndex.setStatus(_B)
class _PublicAccessNASPortUserName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,253))
_PublicAccessNASPortUserName_Type.__name__=_F
_PublicAccessNASPortUserName_Object=MibTableColumn
publicAccessNASPortUserName=_PublicAccessNASPortUserName_Object((1,3,6,1,4,1,12394,1,10,5,1,1,4,2,1,2),_PublicAccessNASPortUserName_Type())
publicAccessNASPortUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:publicAccessNASPortUserName.setStatus(_B)
_PublicAccessMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
publicAccessMIBNotificationPrefix=_PublicAccessMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,1,2))
_PublicAccessMIBNotifications_ObjectIdentity=ObjectIdentity
publicAccessMIBNotifications=_PublicAccessMIBNotifications_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,1,2,0))
_AlvarionPublicAccessMIBConformance_ObjectIdentity=ObjectIdentity
alvarionPublicAccessMIBConformance=_AlvarionPublicAccessMIBConformance_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,1,3))
_AlvarionPublicAccessMIBCompliances_ObjectIdentity=ObjectIdentity
alvarionPublicAccessMIBCompliances=_AlvarionPublicAccessMIBCompliances_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,1,3,1))
_AlvarionPublicAccessMIBGroups_ObjectIdentity=ObjectIdentity
alvarionPublicAccessMIBGroups=_AlvarionPublicAccessMIBGroups_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,1,3,2))
alvarionPublicAccessMIBGroup=ObjectGroup((1,3,6,1,4,1,12394,1,10,5,1,3,2,1))
alvarionPublicAccessMIBGroup.setObjects(*((_A,_M),(_A,_N),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_J),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p)))
if mibBuilder.loadTexts:alvarionPublicAccessMIBGroup.setStatus(_B)
alvarionPublicAccessUserMIBGroup=ObjectGroup((1,3,6,1,4,1,12394,1,10,5,1,3,2,2))
alvarionPublicAccessUserMIBGroup.setObjects(*((_A,_q),(_A,_r),(_A,_s),(_A,_O),(_A,_G),(_A,_t),(_A,_P),(_A,_u),(_A,_Q),(_A,_R),(_A,_v),(_A,_w),(_A,_x),(_A,_S),(_A,_T),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_U),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD)))
if mibBuilder.loadTexts:alvarionPublicAccessUserMIBGroup.setStatus(_B)
alvarionPublicAccessUserConfigMIBGroup=ObjectGroup((1,3,6,1,4,1,12394,1,10,5,1,3,2,3))
alvarionPublicAccessUserConfigMIBGroup.setObjects(*((_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL)))
if mibBuilder.loadTexts:alvarionPublicAccessUserConfigMIBGroup.setStatus(_B)
alvarionPublicAccessNASPortsMIBGroup=ObjectGroup((1,3,6,1,4,1,12394,1,10,5,1,3,2,5))
alvarionPublicAccessNASPortsMIBGroup.setObjects((_A,_AM))
if mibBuilder.loadTexts:alvarionPublicAccessNASPortsMIBGroup.setStatus(_B)
publicAccessStatusChangedTrap=NotificationType((1,3,6,1,4,1,12394,1,10,5,1,2,0,1))
publicAccessStatusChangedTrap.setObjects(*((_A,_M),(_A,_N)))
if mibBuilder.loadTexts:publicAccessStatusChangedTrap.setStatus(_B)
publicAccessUsersThresholdTrap=NotificationType((1,3,6,1,4,1,12394,1,10,5,1,2,0,2))
publicAccessUsersThresholdTrap.setObjects((_A,_J))
if mibBuilder.loadTexts:publicAccessUsersThresholdTrap.setStatus(_B)
publicAccessUsersSessionStartTrap=NotificationType((1,3,6,1,4,1,12394,1,10,5,1,2,0,3))
publicAccessUsersSessionStartTrap.setObjects((_A,_G))
if mibBuilder.loadTexts:publicAccessUsersSessionStartTrap.setStatus(_B)
publicAccessUsersSessionStopTrap=NotificationType((1,3,6,1,4,1,12394,1,10,5,1,2,0,4))
publicAccessUsersSessionStopTrap.setObjects((_A,_G))
if mibBuilder.loadTexts:publicAccessUsersSessionStopTrap.setStatus(_B)
publicAccessUsersSessionFailTrap=NotificationType((1,3,6,1,4,1,12394,1,10,5,1,2,0,5))
publicAccessUsersSessionFailTrap.setObjects((_A,_G))
if mibBuilder.loadTexts:publicAccessUsersSessionFailTrap.setStatus(_B)
publicAccessUsersLoggedInTrap=NotificationType((1,3,6,1,4,1,12394,1,10,5,1,2,0,6))
publicAccessUsersLoggedInTrap.setObjects(*((_A,_J),(_A,_G),(_A,_O),(_A,_S),(_A,_T),(_A,_U),(_A,_P),(_A,_R),(_A,_Q)))
if mibBuilder.loadTexts:publicAccessUsersLoggedInTrap.setStatus(_B)
alvarionPublicAccessNotificationGroup=NotificationGroup((1,3,6,1,4,1,12394,1,10,5,1,3,2,4))
alvarionPublicAccessNotificationGroup.setObjects(*((_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS)))
if mibBuilder.loadTexts:alvarionPublicAccessNotificationGroup.setStatus(_B)
alvarionPublicAccessMIBCompliance=ModuleCompliance((1,3,6,1,4,1,12394,1,10,5,1,3,1,1))
alvarionPublicAccessMIBCompliance.setObjects(*((_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX)))
if mibBuilder.loadTexts:alvarionPublicAccessMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'alvarionPublicAccessMIB':alvarionPublicAccessMIB,'alvarionPublicAccessMIBObjects':alvarionPublicAccessMIBObjects,'publicAccessGroup':publicAccessGroup,_M:publicAccessStatus,_N:publicAccessStatusChangedCause,'publicAccessDeviceGroup':publicAccessDeviceGroup,_b:publicAccessDeviceUserName,_c:publicAccessDeviceUserPassword,_d:publicAccessDeviceSessionTimeoutAdminStatus,_e:publicAccessDeviceSessionTimeoutOperStatus,_f:publicAccessDeviceConfigMode,_g:publicAccessDeviceAuthenProfileIndex,_h:publicAccessDeviceAccountingEnabled,_i:publicAccessDeviceAccountingProfileIndex,_j:publicAccessDeviceForceReconfiguration,'publicAccessUsersGroup':publicAccessUsersGroup,_k:publicAccessUsersMaxCount,_J:publicAccessUsersCount,_l:publicAccessUsersThreshold,_m:publicAccessUsersSessionTrapEnabled,'publicAccessUsersConfigTable':publicAccessUsersConfigTable,'publicAccessUsersConfigEntry':publicAccessUsersConfigEntry,_Y:publicAccessUsersConfigIndex,_AE:publicAccessUsersConfigAuthenType,_AF:publicAccessUsersConfigAuthenMode,_AG:publicAccessUsersConfigAuthenProfileIndex,_AH:publicAccessUsersConfigAuthenTimeout,_AI:publicAccessUsersConfigAccountingEnabled,_AJ:publicAccessUsersConfigAccountingProfileIndex,_AK:publicAccessUsersConfigInterfaceIndex,_AL:publicAccessUsersConfigVirtualApProfileIndex,'publicAccessUserTable':publicAccessUserTable,'publicAccessUserEntry':publicAccessUserEntry,_Z:publicAccessUserIndex,_q:publicAccessUserAuthenType,_r:publicAccessUserAuthenMode,_s:publicAccessUserState,_O:publicAccessUserStationIpAddress,_G:publicAccessUserName,_t:publicAccessUserSessionStartTime,_P:publicAccessUserSessionDuration,_u:publicAccessUserIdleTime,_Q:publicAccessUserBytesSent,_R:publicAccessUserBytesReceived,_v:publicAccessUserPacketsSent,_w:publicAccessUserPacketsReceived,_x:publicAccessUserForceDisconnection,_S:publicAccessUserStationMacAddress,_T:publicAccessUserApMacAddress,_y:publicAccessUserGroupName,_z:publicAccessUserSSID,_A0:publicAccessUserSecurity,_A1:publicAccessUserPHYType,_A2:publicAccessUserVLAN,_A3:publicAccessUserApRadioIndex,_A4:publicAccessUserConfigIndex,_U:publicAccessUserConnectedInterface,_A5:publicAccessUserBytesSentDropped,_A6:publicAccessUserBytesReceivedDropped,_A7:publicAccessUserPacketsSentDropped,_A8:publicAccessUserPacketsReceivedDropped,_A9:publicAccessUserRateLimitationEnabled,_AA:publicAccessUserMaxTransmitRate,_AB:publicAccessUserMaxReceiveRate,_AC:publicAccessUserBandwidthControlLevel,_AD:publicAccessUserNASPort,_n:publicAccessUsersLoggedInTrapEnabled,_o:publicAccessUsersLoggedInTrapInterval,'publicAccessNASPortsGroup':publicAccessNASPortsGroup,_p:publicAccessNASPortCount,'publicAccessNASPortTable':publicAccessNASPortTable,'publicAccessNASPortEntry':publicAccessNASPortEntry,_a:publicAccessNASPortIndex,_AM:publicAccessNASPortUserName,'publicAccessMIBNotificationPrefix':publicAccessMIBNotificationPrefix,'publicAccessMIBNotifications':publicAccessMIBNotifications,_AN:publicAccessStatusChangedTrap,_AO:publicAccessUsersThresholdTrap,_AP:publicAccessUsersSessionStartTrap,_AQ:publicAccessUsersSessionStopTrap,_AR:publicAccessUsersSessionFailTrap,_AS:publicAccessUsersLoggedInTrap,'alvarionPublicAccessMIBConformance':alvarionPublicAccessMIBConformance,'alvarionPublicAccessMIBCompliances':alvarionPublicAccessMIBCompliances,'alvarionPublicAccessMIBCompliance':alvarionPublicAccessMIBCompliance,'alvarionPublicAccessMIBGroups':alvarionPublicAccessMIBGroups,_AT:alvarionPublicAccessMIBGroup,_AU:alvarionPublicAccessUserMIBGroup,_AV:alvarionPublicAccessUserConfigMIBGroup,_AW:alvarionPublicAccessNotificationGroup,_AX:alvarionPublicAccessNASPortsMIBGroup})