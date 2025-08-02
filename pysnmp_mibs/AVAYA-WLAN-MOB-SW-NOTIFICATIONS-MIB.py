_g='avWlanSwitchNotifAuxAuxLimitsReached'
_f='avWlanNotifAuxInetAddress'
_e='avWlanNotifAuxInetAddressType'
_d='avWlanNotifAuxControlFrameType'
_c='avWlanNotifAuxRemoveReason'
_b='avWlanNotifAuxVlanState'
_a='avWlanNotifAuxStateChangeReason'
_Z='avWlanNotifAuxNewState'
_Y='avWlanNotifAuxOldState'
_X='avWlanNotifAuxRoleChangeReason'
_W='avWlanNotifAuxNewVlanRole'
_V='avWlanNotifAuxOldVlanRole'
_U='avWlanNotifAuxMobilityVlanPeerGenerationNumber'
_T='avWlanNotifAuxMobilityVlanSelfGenerationNumber'
_S='avWlanNotifAuxConnectionFailureReason'
_R='avWlanNotifAuxMSTDownloadEntries'
_Q='avWlanNotifAuxNumberOfVlanEntries'
_P='administrator'
_O='SnmpAdminString'
_N='avWlanNotifAuxVlanServerAddress'
_M='avWlanNotifAuxVlanServerInetAddress'
_L='avWlanNotifAuxVlanServerInetAddressType'
_K='avWlanNotifAuxPeerDeviceAddress'
_J='avWlanNotifAuxPeerDeviceInetAddress'
_I='avWlanNotifAuxPeerDeviceInetAddressType'
_H='avWlanNotifAuxPeerDeviceType'
_G='avWlanNotifAuxMobilityControllerInetAddress'
_F='avWlanNotifAuxMobilityControllerInetAddressType'
_E='Integer32'
_D='avWlanNotifAuxMobilityVlanName'
_C='accessible-for-notify'
_B='current'
_A='AVAYA-WLAN-MOB-SW-NOTIFICATIONS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AvWlanMobVlanRole,AvWlanMobVlanState,AvWlanSwitchNotifAuxLimitsMap=mibBuilder.importSymbols('AVAYA-WLAN-TC-MIB','AvWlanMobVlanRole','AvWlanMobVlanState','AvWlanSwitchNotifAuxLimitsMap')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_O)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
avayaWlanMibs,=mibBuilder.importSymbols('SYNOPTICS-ROOT-MIB','avayaWlanMibs')
avayaWlanMobSwitchNotificationsMib=ModuleIdentity((1,3,6,1,4,1,45,7,19))
if mibBuilder.loadTexts:avayaWlanMobSwitchNotificationsMib.setRevisions(('2011-12-15 00:00',))
_AvWlanMobSwNotifications_ObjectIdentity=ObjectIdentity
avWlanMobSwNotifications=_AvWlanMobSwNotifications_ObjectIdentity((1,3,6,1,4,1,45,7,19,0))
_AvWlanSwitchNotifications_ObjectIdentity=ObjectIdentity
avWlanSwitchNotifications=_AvWlanSwitchNotifications_ObjectIdentity((1,3,6,1,4,1,45,7,19,0,1))
_AvWlanMobSwNotificationObjects_ObjectIdentity=ObjectIdentity
avWlanMobSwNotificationObjects=_AvWlanMobSwNotificationObjects_ObjectIdentity((1,3,6,1,4,1,45,7,19,1))
_AvWlanMobSwNotificationAuxObjects_ObjectIdentity=ObjectIdentity
avWlanMobSwNotificationAuxObjects=_AvWlanMobSwNotificationAuxObjects_ObjectIdentity((1,3,6,1,4,1,45,7,19,1,1))
_AvWlanNotifAuxMobilityControllerInetAddressType_Type=InetAddressType
_AvWlanNotifAuxMobilityControllerInetAddressType_Object=MibScalar
avWlanNotifAuxMobilityControllerInetAddressType=_AvWlanNotifAuxMobilityControllerInetAddressType_Object((1,3,6,1,4,1,45,7,19,1,1,1),_AvWlanNotifAuxMobilityControllerInetAddressType_Type())
avWlanNotifAuxMobilityControllerInetAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:avWlanNotifAuxMobilityControllerInetAddressType.setStatus(_B)
_AvWlanNotifAuxMobilityControllerInetAddress_Type=InetAddress
_AvWlanNotifAuxMobilityControllerInetAddress_Object=MibScalar
avWlanNotifAuxMobilityControllerInetAddress=_AvWlanNotifAuxMobilityControllerInetAddress_Object((1,3,6,1,4,1,45,7,19,1,1,2),_AvWlanNotifAuxMobilityControllerInetAddress_Type())
avWlanNotifAuxMobilityControllerInetAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:avWlanNotifAuxMobilityControllerInetAddress.setStatus(_B)
_AvWlanNotifAuxNumberOfVlanEntries_Type=Unsigned32
_AvWlanNotifAuxNumberOfVlanEntries_Object=MibScalar
avWlanNotifAuxNumberOfVlanEntries=_AvWlanNotifAuxNumberOfVlanEntries_Object((1,3,6,1,4,1,45,7,19,1,1,3),_AvWlanNotifAuxNumberOfVlanEntries_Type())
avWlanNotifAuxNumberOfVlanEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:avWlanNotifAuxNumberOfVlanEntries.setStatus(_B)
_AvWlanNotifAuxMSTDownloadEntries_Type=Unsigned32
_AvWlanNotifAuxMSTDownloadEntries_Object=MibScalar
avWlanNotifAuxMSTDownloadEntries=_AvWlanNotifAuxMSTDownloadEntries_Object((1,3,6,1,4,1,45,7,19,1,1,4),_AvWlanNotifAuxMSTDownloadEntries_Type())
avWlanNotifAuxMSTDownloadEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:avWlanNotifAuxMSTDownloadEntries.setStatus(_B)
_AvWlanNotifAuxPeerDeviceInetAddressType_Type=InetAddressType
_AvWlanNotifAuxPeerDeviceInetAddressType_Object=MibScalar
avWlanNotifAuxPeerDeviceInetAddressType=_AvWlanNotifAuxPeerDeviceInetAddressType_Object((1,3,6,1,4,1,45,7,19,1,1,5),_AvWlanNotifAuxPeerDeviceInetAddressType_Type())
avWlanNotifAuxPeerDeviceInetAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:avWlanNotifAuxPeerDeviceInetAddressType.setStatus(_B)
_AvWlanNotifAuxPeerDeviceInetAddress_Type=InetAddress
_AvWlanNotifAuxPeerDeviceInetAddress_Object=MibScalar
avWlanNotifAuxPeerDeviceInetAddress=_AvWlanNotifAuxPeerDeviceInetAddress_Object((1,3,6,1,4,1,45,7,19,1,1,6),_AvWlanNotifAuxPeerDeviceInetAddress_Type())
avWlanNotifAuxPeerDeviceInetAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:avWlanNotifAuxPeerDeviceInetAddress.setStatus(_B)
_AvWlanNotifAuxPeerDeviceAddress_Type=MacAddress
_AvWlanNotifAuxPeerDeviceAddress_Object=MibScalar
avWlanNotifAuxPeerDeviceAddress=_AvWlanNotifAuxPeerDeviceAddress_Object((1,3,6,1,4,1,45,7,19,1,1,7),_AvWlanNotifAuxPeerDeviceAddress_Type())
avWlanNotifAuxPeerDeviceAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:avWlanNotifAuxPeerDeviceAddress.setStatus(_B)
class _AvWlanNotifAuxPeerDeviceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('accessPoint',1),('mobilitySwitch',2)))
_AvWlanNotifAuxPeerDeviceType_Type.__name__=_E
_AvWlanNotifAuxPeerDeviceType_Object=MibScalar
avWlanNotifAuxPeerDeviceType=_AvWlanNotifAuxPeerDeviceType_Object((1,3,6,1,4,1,45,7,19,1,1,8),_AvWlanNotifAuxPeerDeviceType_Type())
avWlanNotifAuxPeerDeviceType.setMaxAccess(_C)
if mibBuilder.loadTexts:avWlanNotifAuxPeerDeviceType.setStatus(_B)
class _AvWlanNotifAuxConnectionFailureReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('kaLoss',1),('controlPlane',2),('peerReset',3)))
_AvWlanNotifAuxConnectionFailureReason_Type.__name__=_E
_AvWlanNotifAuxConnectionFailureReason_Object=MibScalar
avWlanNotifAuxConnectionFailureReason=_AvWlanNotifAuxConnectionFailureReason_Object((1,3,6,1,4,1,45,7,19,1,1,9),_AvWlanNotifAuxConnectionFailureReason_Type())
avWlanNotifAuxConnectionFailureReason.setMaxAccess(_C)
if mibBuilder.loadTexts:avWlanNotifAuxConnectionFailureReason.setStatus(_B)
class _AvWlanNotifAuxMobilityVlanName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AvWlanNotifAuxMobilityVlanName_Type.__name__=_O
_AvWlanNotifAuxMobilityVlanName_Object=MibScalar
avWlanNotifAuxMobilityVlanName=_AvWlanNotifAuxMobilityVlanName_Object((1,3,6,1,4,1,45,7,19,1,1,10),_AvWlanNotifAuxMobilityVlanName_Type())
avWlanNotifAuxMobilityVlanName.setMaxAccess(_C)
if mibBuilder.loadTexts:avWlanNotifAuxMobilityVlanName.setStatus(_B)
_AvWlanNotifAuxVlanServerInetAddressType_Type=InetAddressType
_AvWlanNotifAuxVlanServerInetAddressType_Object=MibScalar
avWlanNotifAuxVlanServerInetAddressType=_AvWlanNotifAuxVlanServerInetAddressType_Object((1,3,6,1,4,1,45,7,19,1,1,11),_AvWlanNotifAuxVlanServerInetAddressType_Type())
avWlanNotifAuxVlanServerInetAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:avWlanNotifAuxVlanServerInetAddressType.setStatus(_B)
_AvWlanNotifAuxVlanServerInetAddress_Type=InetAddress
_AvWlanNotifAuxVlanServerInetAddress_Object=MibScalar
avWlanNotifAuxVlanServerInetAddress=_AvWlanNotifAuxVlanServerInetAddress_Object((1,3,6,1,4,1,45,7,19,1,1,12),_AvWlanNotifAuxVlanServerInetAddress_Type())
avWlanNotifAuxVlanServerInetAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:avWlanNotifAuxVlanServerInetAddress.setStatus(_B)
_AvWlanNotifAuxVlanServerAddress_Type=MacAddress
_AvWlanNotifAuxVlanServerAddress_Object=MibScalar
avWlanNotifAuxVlanServerAddress=_AvWlanNotifAuxVlanServerAddress_Object((1,3,6,1,4,1,45,7,19,1,1,13),_AvWlanNotifAuxVlanServerAddress_Type())
avWlanNotifAuxVlanServerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:avWlanNotifAuxVlanServerAddress.setStatus(_B)
_AvWlanNotifAuxMobilityVlanSelfGenerationNumber_Type=Unsigned32
_AvWlanNotifAuxMobilityVlanSelfGenerationNumber_Object=MibScalar
avWlanNotifAuxMobilityVlanSelfGenerationNumber=_AvWlanNotifAuxMobilityVlanSelfGenerationNumber_Object((1,3,6,1,4,1,45,7,19,1,1,14),_AvWlanNotifAuxMobilityVlanSelfGenerationNumber_Type())
avWlanNotifAuxMobilityVlanSelfGenerationNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:avWlanNotifAuxMobilityVlanSelfGenerationNumber.setStatus(_B)
_AvWlanNotifAuxMobilityVlanPeerGenerationNumber_Type=Unsigned32
_AvWlanNotifAuxMobilityVlanPeerGenerationNumber_Object=MibScalar
avWlanNotifAuxMobilityVlanPeerGenerationNumber=_AvWlanNotifAuxMobilityVlanPeerGenerationNumber_Object((1,3,6,1,4,1,45,7,19,1,1,15),_AvWlanNotifAuxMobilityVlanPeerGenerationNumber_Type())
avWlanNotifAuxMobilityVlanPeerGenerationNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:avWlanNotifAuxMobilityVlanPeerGenerationNumber.setStatus(_B)
_AvWlanNotifAuxOldVlanRole_Type=AvWlanMobVlanRole
_AvWlanNotifAuxOldVlanRole_Object=MibScalar
avWlanNotifAuxOldVlanRole=_AvWlanNotifAuxOldVlanRole_Object((1,3,6,1,4,1,45,7,19,1,1,16),_AvWlanNotifAuxOldVlanRole_Type())
avWlanNotifAuxOldVlanRole.setMaxAccess(_C)
if mibBuilder.loadTexts:avWlanNotifAuxOldVlanRole.setStatus(_B)
_AvWlanNotifAuxNewVlanRole_Type=AvWlanMobVlanRole
_AvWlanNotifAuxNewVlanRole_Object=MibScalar
avWlanNotifAuxNewVlanRole=_AvWlanNotifAuxNewVlanRole_Object((1,3,6,1,4,1,45,7,19,1,1,17),_AvWlanNotifAuxNewVlanRole_Type())
avWlanNotifAuxNewVlanRole.setMaxAccess(_C)
if mibBuilder.loadTexts:avWlanNotifAuxNewVlanRole.setStatus(_B)
class _AvWlanNotifAuxRoleChangeReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),('clientRoam',2)))
_AvWlanNotifAuxRoleChangeReason_Type.__name__=_E
_AvWlanNotifAuxRoleChangeReason_Object=MibScalar
avWlanNotifAuxRoleChangeReason=_AvWlanNotifAuxRoleChangeReason_Object((1,3,6,1,4,1,45,7,19,1,1,18),_AvWlanNotifAuxRoleChangeReason_Type())
avWlanNotifAuxRoleChangeReason.setMaxAccess(_C)
if mibBuilder.loadTexts:avWlanNotifAuxRoleChangeReason.setStatus(_B)
_AvWlanNotifAuxOldState_Type=AvWlanMobVlanState
_AvWlanNotifAuxOldState_Object=MibScalar
avWlanNotifAuxOldState=_AvWlanNotifAuxOldState_Object((1,3,6,1,4,1,45,7,19,1,1,19),_AvWlanNotifAuxOldState_Type())
avWlanNotifAuxOldState.setMaxAccess(_C)
if mibBuilder.loadTexts:avWlanNotifAuxOldState.setStatus(_B)
_AvWlanNotifAuxNewState_Type=AvWlanMobVlanState
_AvWlanNotifAuxNewState_Object=MibScalar
avWlanNotifAuxNewState=_AvWlanNotifAuxNewState_Object((1,3,6,1,4,1,45,7,19,1,1,20),_AvWlanNotifAuxNewState_Type())
avWlanNotifAuxNewState.setMaxAccess(_C)
if mibBuilder.loadTexts:avWlanNotifAuxNewState.setStatus(_B)
class _AvWlanNotifAuxStateChangeReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('mobVlanDeleted',1),('mobVlanCreated',2),('localVlanDeleted',3)))
_AvWlanNotifAuxStateChangeReason_Type.__name__=_E
_AvWlanNotifAuxStateChangeReason_Object=MibScalar
avWlanNotifAuxStateChangeReason=_AvWlanNotifAuxStateChangeReason_Object((1,3,6,1,4,1,45,7,19,1,1,21),_AvWlanNotifAuxStateChangeReason_Type())
avWlanNotifAuxStateChangeReason.setMaxAccess(_C)
if mibBuilder.loadTexts:avWlanNotifAuxStateChangeReason.setStatus(_B)
_AvWlanNotifAuxVlanState_Type=AvWlanMobVlanState
_AvWlanNotifAuxVlanState_Object=MibScalar
avWlanNotifAuxVlanState=_AvWlanNotifAuxVlanState_Object((1,3,6,1,4,1,45,7,19,1,1,22),_AvWlanNotifAuxVlanState_Type())
avWlanNotifAuxVlanState.setMaxAccess(_C)
if mibBuilder.loadTexts:avWlanNotifAuxVlanState.setStatus(_B)
class _AvWlanNotifAuxRemoveReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),('lvidDeletion',2)))
_AvWlanNotifAuxRemoveReason_Type.__name__=_E
_AvWlanNotifAuxRemoveReason_Object=MibScalar
avWlanNotifAuxRemoveReason=_AvWlanNotifAuxRemoveReason_Object((1,3,6,1,4,1,45,7,19,1,1,23),_AvWlanNotifAuxRemoveReason_Type())
avWlanNotifAuxRemoveReason.setMaxAccess(_C)
if mibBuilder.loadTexts:avWlanNotifAuxRemoveReason.setStatus(_B)
class _AvWlanNotifAuxControlFrameType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('igmpReport',1),('igmpLeave',2)))
_AvWlanNotifAuxControlFrameType_Type.__name__=_E
_AvWlanNotifAuxControlFrameType_Object=MibScalar
avWlanNotifAuxControlFrameType=_AvWlanNotifAuxControlFrameType_Object((1,3,6,1,4,1,45,7,19,1,1,24),_AvWlanNotifAuxControlFrameType_Type())
avWlanNotifAuxControlFrameType.setMaxAccess(_C)
if mibBuilder.loadTexts:avWlanNotifAuxControlFrameType.setStatus(_B)
_AvWlanNotifAuxInetAddressType_Type=InetAddressType
_AvWlanNotifAuxInetAddressType_Object=MibScalar
avWlanNotifAuxInetAddressType=_AvWlanNotifAuxInetAddressType_Object((1,3,6,1,4,1,45,7,19,1,1,25),_AvWlanNotifAuxInetAddressType_Type())
avWlanNotifAuxInetAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:avWlanNotifAuxInetAddressType.setStatus(_B)
_AvWlanNotifAuxInetAddress_Type=InetAddress
_AvWlanNotifAuxInetAddress_Object=MibScalar
avWlanNotifAuxInetAddress=_AvWlanNotifAuxInetAddress_Object((1,3,6,1,4,1,45,7,19,1,1,26),_AvWlanNotifAuxInetAddress_Type())
avWlanNotifAuxInetAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:avWlanNotifAuxInetAddress.setStatus(_B)
_AvWlanSwitchNotifAuxAuxLimitsReached_Type=AvWlanSwitchNotifAuxLimitsMap
_AvWlanSwitchNotifAuxAuxLimitsReached_Object=MibScalar
avWlanSwitchNotifAuxAuxLimitsReached=_AvWlanSwitchNotifAuxAuxLimitsReached_Object((1,3,6,1,4,1,45,7,19,1,1,27),_AvWlanSwitchNotifAuxAuxLimitsReached_Type())
avWlanSwitchNotifAuxAuxLimitsReached.setMaxAccess(_C)
if mibBuilder.loadTexts:avWlanSwitchNotifAuxAuxLimitsReached.setStatus(_B)
avWlanSwitchMCPConnectionEstablished=NotificationType((1,3,6,1,4,1,45,7,19,0,1,1))
avWlanSwitchMCPConnectionEstablished.setObjects(*((_A,_F),(_A,_G)))
if mibBuilder.loadTexts:avWlanSwitchMCPConnectionEstablished.setStatus(_B)
avWlanSwitchMCPLostConnection=NotificationType((1,3,6,1,4,1,45,7,19,0,1,2))
avWlanSwitchMCPLostConnection.setObjects(*((_A,_F),(_A,_G)))
if mibBuilder.loadTexts:avWlanSwitchMCPLostConnection.setStatus(_B)
avWlanSwitchMVTDownload=NotificationType((1,3,6,1,4,1,45,7,19,0,1,3))
avWlanSwitchMVTDownload.setObjects(*((_A,_F),(_A,_G),(_A,_Q)))
if mibBuilder.loadTexts:avWlanSwitchMVTDownload.setStatus(_B)
avWlanSwitchMSTDownload=NotificationType((1,3,6,1,4,1,45,7,19,0,1,4))
avWlanSwitchMSTDownload.setObjects(*((_A,_F),(_A,_G),(_A,_R)))
if mibBuilder.loadTexts:avWlanSwitchMSTDownload.setStatus(_B)
avWlanSwitchPeerDeviceConnectionEstablished=NotificationType((1,3,6,1,4,1,45,7,19,0,1,5))
avWlanSwitchPeerDeviceConnectionEstablished.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_H)))
if mibBuilder.loadTexts:avWlanSwitchPeerDeviceConnectionEstablished.setStatus(_B)
avWlanSwitchPeerDeviceLostConnection=NotificationType((1,3,6,1,4,1,45,7,19,0,1,6))
avWlanSwitchPeerDeviceLostConnection.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_H),(_A,_S)))
if mibBuilder.loadTexts:avWlanSwitchPeerDeviceLostConnection.setStatus(_B)
avWlanSwitchVlanServerElected=NotificationType((1,3,6,1,4,1,45,7,19,0,1,7))
avWlanSwitchVlanServerElected.setObjects(*((_A,_D),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:avWlanSwitchVlanServerElected.setStatus(_B)
avWlanSwitchLostConnectionToVlanServer=NotificationType((1,3,6,1,4,1,45,7,19,0,1,8))
avWlanSwitchLostConnectionToVlanServer.setObjects(*((_A,_D),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:avWlanSwitchLostConnectionToVlanServer.setStatus(_B)
avWlanSwitchVlanGenNumberMismatch=NotificationType((1,3,6,1,4,1,45,7,19,0,1,9))
avWlanSwitchVlanGenNumberMismatch.setObjects(*((_A,_D),(_A,_T),(_A,_U)))
if mibBuilder.loadTexts:avWlanSwitchVlanGenNumberMismatch.setStatus(_B)
avWlanSwitchVlanRoleChanged=NotificationType((1,3,6,1,4,1,45,7,19,0,1,10))
avWlanSwitchVlanRoleChanged.setObjects(*((_A,_D),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:avWlanSwitchVlanRoleChanged.setStatus(_B)
avWlanSwitchVlanMapStateChanged=NotificationType((1,3,6,1,4,1,45,7,19,0,1,11))
avWlanSwitchVlanMapStateChanged.setObjects(*((_A,_D),(_A,_Y),(_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:avWlanSwitchVlanMapStateChanged.setStatus(_B)
avWlanSwitchVlanMapRemoved=NotificationType((1,3,6,1,4,1,45,7,19,0,1,12))
avWlanSwitchVlanMapRemoved.setObjects(*((_A,_D),(_A,_b),(_A,_c)))
if mibBuilder.loadTexts:avWlanSwitchVlanMapRemoved.setStatus(_B)
avWlanSwitchVlanTrackAffected=NotificationType((1,3,6,1,4,1,45,7,19,0,1,13))
avWlanSwitchVlanTrackAffected.setObjects((_A,_D))
if mibBuilder.loadTexts:avWlanSwitchVlanTrackAffected.setStatus(_B)
avWlanSwitchIgmpSnoopingEnabled=NotificationType((1,3,6,1,4,1,45,7,19,0,1,14))
avWlanSwitchIgmpSnoopingEnabled.setObjects((_A,_D))
if mibBuilder.loadTexts:avWlanSwitchIgmpSnoopingEnabled.setStatus(_B)
avWlanSwitchIgmpSnoopingDisabled=NotificationType((1,3,6,1,4,1,45,7,19,0,1,15))
avWlanSwitchIgmpSnoopingDisabled.setObjects((_A,_D))
if mibBuilder.loadTexts:avWlanSwitchIgmpSnoopingDisabled.setStatus(_B)
avWlanSwitchIgmpControlFrameReceived=NotificationType((1,3,6,1,4,1,45,7,19,0,1,16))
avWlanSwitchIgmpControlFrameReceived.setObjects(*((_A,_D),(_A,_d),(_A,_H),(_A,_e),(_A,_f)))
if mibBuilder.loadTexts:avWlanSwitchIgmpControlFrameReceived.setStatus(_B)
avWlanSwitchLimitsReached=NotificationType((1,3,6,1,4,1,45,7,19,0,1,17))
avWlanSwitchLimitsReached.setObjects((_A,_g))
if mibBuilder.loadTexts:avWlanSwitchLimitsReached.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'avayaWlanMobSwitchNotificationsMib':avayaWlanMobSwitchNotificationsMib,'avWlanMobSwNotifications':avWlanMobSwNotifications,'avWlanSwitchNotifications':avWlanSwitchNotifications,'avWlanSwitchMCPConnectionEstablished':avWlanSwitchMCPConnectionEstablished,'avWlanSwitchMCPLostConnection':avWlanSwitchMCPLostConnection,'avWlanSwitchMVTDownload':avWlanSwitchMVTDownload,'avWlanSwitchMSTDownload':avWlanSwitchMSTDownload,'avWlanSwitchPeerDeviceConnectionEstablished':avWlanSwitchPeerDeviceConnectionEstablished,'avWlanSwitchPeerDeviceLostConnection':avWlanSwitchPeerDeviceLostConnection,'avWlanSwitchVlanServerElected':avWlanSwitchVlanServerElected,'avWlanSwitchLostConnectionToVlanServer':avWlanSwitchLostConnectionToVlanServer,'avWlanSwitchVlanGenNumberMismatch':avWlanSwitchVlanGenNumberMismatch,'avWlanSwitchVlanRoleChanged':avWlanSwitchVlanRoleChanged,'avWlanSwitchVlanMapStateChanged':avWlanSwitchVlanMapStateChanged,'avWlanSwitchVlanMapRemoved':avWlanSwitchVlanMapRemoved,'avWlanSwitchVlanTrackAffected':avWlanSwitchVlanTrackAffected,'avWlanSwitchIgmpSnoopingEnabled':avWlanSwitchIgmpSnoopingEnabled,'avWlanSwitchIgmpSnoopingDisabled':avWlanSwitchIgmpSnoopingDisabled,'avWlanSwitchIgmpControlFrameReceived':avWlanSwitchIgmpControlFrameReceived,'avWlanSwitchLimitsReached':avWlanSwitchLimitsReached,'avWlanMobSwNotificationObjects':avWlanMobSwNotificationObjects,'avWlanMobSwNotificationAuxObjects':avWlanMobSwNotificationAuxObjects,_F:avWlanNotifAuxMobilityControllerInetAddressType,_G:avWlanNotifAuxMobilityControllerInetAddress,_Q:avWlanNotifAuxNumberOfVlanEntries,_R:avWlanNotifAuxMSTDownloadEntries,_I:avWlanNotifAuxPeerDeviceInetAddressType,_J:avWlanNotifAuxPeerDeviceInetAddress,_K:avWlanNotifAuxPeerDeviceAddress,_H:avWlanNotifAuxPeerDeviceType,_S:avWlanNotifAuxConnectionFailureReason,_D:avWlanNotifAuxMobilityVlanName,_L:avWlanNotifAuxVlanServerInetAddressType,_M:avWlanNotifAuxVlanServerInetAddress,_N:avWlanNotifAuxVlanServerAddress,_T:avWlanNotifAuxMobilityVlanSelfGenerationNumber,_U:avWlanNotifAuxMobilityVlanPeerGenerationNumber,_V:avWlanNotifAuxOldVlanRole,_W:avWlanNotifAuxNewVlanRole,_X:avWlanNotifAuxRoleChangeReason,_Y:avWlanNotifAuxOldState,_Z:avWlanNotifAuxNewState,_a:avWlanNotifAuxStateChangeReason,_b:avWlanNotifAuxVlanState,_c:avWlanNotifAuxRemoveReason,_d:avWlanNotifAuxControlFrameType,_e:avWlanNotifAuxInetAddressType,_f:avWlanNotifAuxInetAddress,_g:avWlanSwitchNotifAuxAuxLimitsReached})