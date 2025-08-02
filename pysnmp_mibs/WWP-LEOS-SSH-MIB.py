_N='wwpLeosSSHServerClientIPv6Group'
_M='wwpLeosSSHServerClientInetAddr'
_L='wwpLeosSSHServerClientInetAddrType'
_K='wwpLeosSSHServerClientIndex'
_J='enabled'
_I='disabled'
_H='Unsigned32'
_G='OctetString'
_F='read-create'
_E='read-only'
_D='WWP-LEOS-SSH-MIB'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
wwpModulesLeos,=mibBuilder.importSymbols('WWP-SMI','wwpModulesLeos')
wwpLeosSSHMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,60,34))
if mibBuilder.loadTexts:wwpLeosSSHMIB.setRevisions(('2012-04-10 00:00','2011-06-15 00:00','2006-04-18 17:00'))
_WwpLeosSSHMIBObjects_ObjectIdentity=ObjectIdentity
wwpLeosSSHMIBObjects=_WwpLeosSSHMIBObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,60,34,1))
_WwpLeosSSHServerGlobal_ObjectIdentity=ObjectIdentity
wwpLeosSSHServerGlobal=_WwpLeosSSHServerGlobal_ObjectIdentity((1,3,6,1,4,1,6141,2,60,34,1,1))
class _WwpLeosSSHServerAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_WwpLeosSSHServerAdminState_Type.__name__=_B
_WwpLeosSSHServerAdminState_Object=MibScalar
wwpLeosSSHServerAdminState=_WwpLeosSSHServerAdminState_Object((1,3,6,1,4,1,6141,2,60,34,1,1,1),_WwpLeosSSHServerAdminState_Type())
wwpLeosSSHServerAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosSSHServerAdminState.setStatus(_A)
class _WwpLeosSSHServerOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_WwpLeosSSHServerOperState_Type.__name__=_B
_WwpLeosSSHServerOperState_Object=MibScalar
wwpLeosSSHServerOperState=_WwpLeosSSHServerOperState_Object((1,3,6,1,4,1,6141,2,60,34,1,1,2),_WwpLeosSSHServerOperState_Type())
wwpLeosSSHServerOperState.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosSSHServerOperState.setStatus(_A)
class _WwpLeosSSHServerAuthenticationRetries_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_WwpLeosSSHServerAuthenticationRetries_Type.__name__=_B
_WwpLeosSSHServerAuthenticationRetries_Object=MibScalar
wwpLeosSSHServerAuthenticationRetries=_WwpLeosSSHServerAuthenticationRetries_Object((1,3,6,1,4,1,6141,2,60,34,1,1,3),_WwpLeosSSHServerAuthenticationRetries_Type())
wwpLeosSSHServerAuthenticationRetries.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosSSHServerAuthenticationRetries.setStatus(_A)
_WwpLeosSSHServerMaxClients_Type=Integer32
_WwpLeosSSHServerMaxClients_Object=MibScalar
wwpLeosSSHServerMaxClients=_WwpLeosSSHServerMaxClients_Object((1,3,6,1,4,1,6141,2,60,34,1,1,4),_WwpLeosSSHServerMaxClients_Type())
wwpLeosSSHServerMaxClients.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosSSHServerMaxClients.setStatus(_A)
_WwpLeosSSHServerKeyGenerateSet_Type=TruthValue
_WwpLeosSSHServerKeyGenerateSet_Object=MibScalar
wwpLeosSSHServerKeyGenerateSet=_WwpLeosSSHServerKeyGenerateSet_Object((1,3,6,1,4,1,6141,2,60,34,1,1,5),_WwpLeosSSHServerKeyGenerateSet_Type())
wwpLeosSSHServerKeyGenerateSet.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosSSHServerKeyGenerateSet.setStatus(_A)
class _WwpLeosSSHServerKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_WwpLeosSSHServerKey_Type.__name__=_G
_WwpLeosSSHServerKey_Object=MibScalar
wwpLeosSSHServerKey=_WwpLeosSSHServerKey_Object((1,3,6,1,4,1,6141,2,60,34,1,1,6),_WwpLeosSSHServerKey_Type())
wwpLeosSSHServerKey.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosSSHServerKey.setStatus(_A)
class _WwpLeosSSHServerKeyStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('keyReady',1),('keyGenerating',2),('keyDoesnotExist',3),('keyGenerationFailed',4)))
_WwpLeosSSHServerKeyStatus_Type.__name__=_B
_WwpLeosSSHServerKeyStatus_Object=MibScalar
wwpLeosSSHServerKeyStatus=_WwpLeosSSHServerKeyStatus_Object((1,3,6,1,4,1,6141,2,60,34,1,1,7),_WwpLeosSSHServerKeyStatus_Type())
wwpLeosSSHServerKeyStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosSSHServerKeyStatus.setStatus(_A)
_WwpLeosSSHServerTftpServer_Type=IpAddress
_WwpLeosSSHServerTftpServer_Object=MibScalar
wwpLeosSSHServerTftpServer=_WwpLeosSSHServerTftpServer_Object((1,3,6,1,4,1,6141,2,60,34,1,1,8),_WwpLeosSSHServerTftpServer_Type())
wwpLeosSSHServerTftpServer.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosSSHServerTftpServer.setStatus(_A)
class _WwpLeosSSHServerMaxLimitedUsers_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_WwpLeosSSHServerMaxLimitedUsers_Type.__name__=_B
_WwpLeosSSHServerMaxLimitedUsers_Object=MibScalar
wwpLeosSSHServerMaxLimitedUsers=_WwpLeosSSHServerMaxLimitedUsers_Object((1,3,6,1,4,1,6141,2,60,34,1,1,9),_WwpLeosSSHServerMaxLimitedUsers_Type())
wwpLeosSSHServerMaxLimitedUsers.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosSSHServerMaxLimitedUsers.setStatus(_A)
class _WwpLeosSSHServerMaxSuperUsers_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_WwpLeosSSHServerMaxSuperUsers_Type.__name__=_B
_WwpLeosSSHServerMaxSuperUsers_Object=MibScalar
wwpLeosSSHServerMaxSuperUsers=_WwpLeosSSHServerMaxSuperUsers_Object((1,3,6,1,4,1,6141,2,60,34,1,1,10),_WwpLeosSSHServerMaxSuperUsers_Type())
wwpLeosSSHServerMaxSuperUsers.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosSSHServerMaxSuperUsers.setStatus(_A)
class _WwpLeosSSHServerMaxAdminUsers_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_WwpLeosSSHServerMaxAdminUsers_Type.__name__=_B
_WwpLeosSSHServerMaxAdminUsers_Object=MibScalar
wwpLeosSSHServerMaxAdminUsers=_WwpLeosSSHServerMaxAdminUsers_Object((1,3,6,1,4,1,6141,2,60,34,1,1,11),_WwpLeosSSHServerMaxAdminUsers_Type())
wwpLeosSSHServerMaxAdminUsers.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosSSHServerMaxAdminUsers.setStatus(_A)
_WwpLeosSSHServerClient_ObjectIdentity=ObjectIdentity
wwpLeosSSHServerClient=_WwpLeosSSHServerClient_ObjectIdentity((1,3,6,1,4,1,6141,2,60,34,1,2))
_WwpLeosSSHServerClientTable_Object=MibTable
wwpLeosSSHServerClientTable=_WwpLeosSSHServerClientTable_Object((1,3,6,1,4,1,6141,2,60,34,1,2,1))
if mibBuilder.loadTexts:wwpLeosSSHServerClientTable.setStatus(_A)
_WwpLeosSSHServerClientEntry_Object=MibTableRow
wwpLeosSSHServerClientEntry=_WwpLeosSSHServerClientEntry_Object((1,3,6,1,4,1,6141,2,60,34,1,2,1,1))
wwpLeosSSHServerClientEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:wwpLeosSSHServerClientEntry.setStatus(_A)
class _WwpLeosSSHServerClientIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_WwpLeosSSHServerClientIndex_Type.__name__=_B
_WwpLeosSSHServerClientIndex_Object=MibTableColumn
wwpLeosSSHServerClientIndex=_WwpLeosSSHServerClientIndex_Object((1,3,6,1,4,1,6141,2,60,34,1,2,1,1,1),_WwpLeosSSHServerClientIndex_Type())
wwpLeosSSHServerClientIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:wwpLeosSSHServerClientIndex.setStatus(_A)
_WwpLeosSSHServerClientIpAddr_Type=IpAddress
_WwpLeosSSHServerClientIpAddr_Object=MibTableColumn
wwpLeosSSHServerClientIpAddr=_WwpLeosSSHServerClientIpAddr_Object((1,3,6,1,4,1,6141,2,60,34,1,2,1,1,2),_WwpLeosSSHServerClientIpAddr_Type())
wwpLeosSSHServerClientIpAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosSSHServerClientIpAddr.setStatus(_A)
_WwpLeosSSHServerClientStatus_Type=RowStatus
_WwpLeosSSHServerClientStatus_Object=MibTableColumn
wwpLeosSSHServerClientStatus=_WwpLeosSSHServerClientStatus_Object((1,3,6,1,4,1,6141,2,60,34,1,2,1,1,3),_WwpLeosSSHServerClientStatus_Type())
wwpLeosSSHServerClientStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosSSHServerClientStatus.setStatus(_A)
_WwpLeosSSHServerClientInetAddrType_Type=InetAddressType
_WwpLeosSSHServerClientInetAddrType_Object=MibTableColumn
wwpLeosSSHServerClientInetAddrType=_WwpLeosSSHServerClientInetAddrType_Object((1,3,6,1,4,1,6141,2,60,34,1,2,1,1,4),_WwpLeosSSHServerClientInetAddrType_Type())
wwpLeosSSHServerClientInetAddrType.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosSSHServerClientInetAddrType.setStatus(_A)
_WwpLeosSSHServerClientInetAddr_Type=InetAddress
_WwpLeosSSHServerClientInetAddr_Object=MibTableColumn
wwpLeosSSHServerClientInetAddr=_WwpLeosSSHServerClientInetAddr_Object((1,3,6,1,4,1,6141,2,60,34,1,2,1,1,5),_WwpLeosSSHServerClientInetAddr_Type())
wwpLeosSSHServerClientInetAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosSSHServerClientInetAddr.setStatus(_A)
_WwpLeosSSHServerListenerPort_ObjectIdentity=ObjectIdentity
wwpLeosSSHServerListenerPort=_WwpLeosSSHServerListenerPort_ObjectIdentity((1,3,6,1,4,1,6141,2,60,34,1,3))
class _WwpLeosSSHServerListenerPortId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(22,65535))
_WwpLeosSSHServerListenerPortId_Type.__name__=_H
_WwpLeosSSHServerListenerPortId_Object=MibScalar
wwpLeosSSHServerListenerPortId=_WwpLeosSSHServerListenerPortId_Object((1,3,6,1,4,1,6141,2,60,34,1,3,1),_WwpLeosSSHServerListenerPortId_Type())
wwpLeosSSHServerListenerPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosSSHServerListenerPortId.setStatus(_A)
_WwpLeosSSHMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
wwpLeosSSHMIBNotificationPrefix=_WwpLeosSSHMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,6141,2,60,34,2))
_WwpLeosSSHMIBNotifications_ObjectIdentity=ObjectIdentity
wwpLeosSSHMIBNotifications=_WwpLeosSSHMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6141,2,60,34,2,0))
_WwpLeosSSHMIBConformance_ObjectIdentity=ObjectIdentity
wwpLeosSSHMIBConformance=_WwpLeosSSHMIBConformance_ObjectIdentity((1,3,6,1,4,1,6141,2,60,34,3))
_WwpLeosSSHMIBCompliances_ObjectIdentity=ObjectIdentity
wwpLeosSSHMIBCompliances=_WwpLeosSSHMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6141,2,60,34,3,1))
_WwpLeosSSHMIBGroups_ObjectIdentity=ObjectIdentity
wwpLeosSSHMIBGroups=_WwpLeosSSHMIBGroups_ObjectIdentity((1,3,6,1,4,1,6141,2,60,34,3,2))
wwpLeosSSHServerClientIPv6Group=ObjectGroup((1,3,6,1,4,1,6141,2,60,34,3,2,1))
wwpLeosSSHServerClientIPv6Group.setObjects(*((_D,_L),(_D,_M)))
if mibBuilder.loadTexts:wwpLeosSSHServerClientIPv6Group.setStatus(_A)
wwpLeosSSHServerClientCompliance=ModuleCompliance((1,3,6,1,4,1,6141,2,60,34,3,1,1))
wwpLeosSSHServerClientCompliance.setObjects((_D,_N))
if mibBuilder.loadTexts:wwpLeosSSHServerClientCompliance.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'wwpLeosSSHMIB':wwpLeosSSHMIB,'wwpLeosSSHMIBObjects':wwpLeosSSHMIBObjects,'wwpLeosSSHServerGlobal':wwpLeosSSHServerGlobal,'wwpLeosSSHServerAdminState':wwpLeosSSHServerAdminState,'wwpLeosSSHServerOperState':wwpLeosSSHServerOperState,'wwpLeosSSHServerAuthenticationRetries':wwpLeosSSHServerAuthenticationRetries,'wwpLeosSSHServerMaxClients':wwpLeosSSHServerMaxClients,'wwpLeosSSHServerKeyGenerateSet':wwpLeosSSHServerKeyGenerateSet,'wwpLeosSSHServerKey':wwpLeosSSHServerKey,'wwpLeosSSHServerKeyStatus':wwpLeosSSHServerKeyStatus,'wwpLeosSSHServerTftpServer':wwpLeosSSHServerTftpServer,'wwpLeosSSHServerMaxLimitedUsers':wwpLeosSSHServerMaxLimitedUsers,'wwpLeosSSHServerMaxSuperUsers':wwpLeosSSHServerMaxSuperUsers,'wwpLeosSSHServerMaxAdminUsers':wwpLeosSSHServerMaxAdminUsers,'wwpLeosSSHServerClient':wwpLeosSSHServerClient,'wwpLeosSSHServerClientTable':wwpLeosSSHServerClientTable,'wwpLeosSSHServerClientEntry':wwpLeosSSHServerClientEntry,_K:wwpLeosSSHServerClientIndex,'wwpLeosSSHServerClientIpAddr':wwpLeosSSHServerClientIpAddr,'wwpLeosSSHServerClientStatus':wwpLeosSSHServerClientStatus,_L:wwpLeosSSHServerClientInetAddrType,_M:wwpLeosSSHServerClientInetAddr,'wwpLeosSSHServerListenerPort':wwpLeosSSHServerListenerPort,'wwpLeosSSHServerListenerPortId':wwpLeosSSHServerListenerPortId,'wwpLeosSSHMIBNotificationPrefix':wwpLeosSSHMIBNotificationPrefix,'wwpLeosSSHMIBNotifications':wwpLeosSSHMIBNotifications,'wwpLeosSSHMIBConformance':wwpLeosSSHMIBConformance,'wwpLeosSSHMIBCompliances':wwpLeosSSHMIBCompliances,'wwpLeosSSHServerClientCompliance':wwpLeosSSHServerClientCompliance,'wwpLeosSSHMIBGroups':wwpLeosSSHMIBGroups,_N:wwpLeosSSHServerClientIPv6Group})