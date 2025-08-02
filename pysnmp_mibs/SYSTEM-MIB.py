_l='nnsntpErrorNotification'
_k='nnsntpSuccessNotification'
_j='nnsntpDisableNotification'
_i='nnsntpEnableNotification'
_h='nnlogoutNotification'
_g='nnauthenticationLoginSuccessNotification'
_f='nnauthenticationFailureNotification'
_e='nnuserLoginFailNotification'
_d='nnuserLogOffNotification'
_c='nnuserLoginNotification'
_b='nnshutDownNotification'
_a='nnssmPreviousState'
_Z='nnssmCurrentState'
_Y='nnreasonForFailure'
_X='nnsysLoginFailMsg'
_W='nnsysLogoutMsg'
_V='nnsysLoginMsg'
_U='nnsysRestartMsg'
_T='SntpEnabled'
_S='nndnsServerAddr'
_R='disabled'
_Q='read-create'
_P='enabled'
_O='nntimeStamp'
_N='nnclientIpAddress'
_M='nnprotocolType'
_L='other'
_K='nnsntpTimeout'
_J='nnsntpServerAddr'
_I='OctetString'
_H='accessible-for-notify'
_G='read-only'
_F='Integer32'
_E='TruthValue'
_D='DisplayString'
_C='read-write'
_B='SYSTEM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ntEnterpriseDataTasmanMgmt,=mibBuilder.importSymbols('NT-ENTERPRISE-DATA-MIB','ntEnterpriseDataTasmanMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','RowStatus','TextualConvention',_E)
nnsystemMib=ModuleIdentity((1,3,6,1,4,1,562,73,1,1,1,1))
if mibBuilder.loadTexts:nnsystemMib.setRevisions(('1900-08-18 00:00',))
class SntpEnabled(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('not-enabled',1),(_P,2)))
_NnsystemObjects_ObjectIdentity=ObjectIdentity
nnsystemObjects=_NnsystemObjects_ObjectIdentity((1,3,6,1,4,1,562,73,1,1,1,1,1))
_NnsysIpAddr_Type=IpAddress
_NnsysIpAddr_Object=MibScalar
nnsysIpAddr=_NnsysIpAddr_Object((1,3,6,1,4,1,562,73,1,1,1,1,1,1),_NnsysIpAddr_Type())
nnsysIpAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:nnsysIpAddr.setStatus(_A)
_NnsysNetMask_Type=IpAddress
_NnsysNetMask_Object=MibScalar
nnsysNetMask=_NnsysNetMask_Object((1,3,6,1,4,1,562,73,1,1,1,1,1,2),_NnsysNetMask_Type())
nnsysNetMask.setMaxAccess(_G)
if mibBuilder.loadTexts:nnsysNetMask.setStatus(_A)
_NnsysBroadcast_Type=IpAddress
_NnsysBroadcast_Object=MibScalar
nnsysBroadcast=_NnsysBroadcast_Object((1,3,6,1,4,1,562,73,1,1,1,1,1,3),_NnsysBroadcast_Type())
nnsysBroadcast.setMaxAccess(_G)
if mibBuilder.loadTexts:nnsysBroadcast.setStatus(_A)
class _NnsysVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_NnsysVersion_Type.__name__=_D
_NnsysVersion_Object=MibScalar
nnsysVersion=_NnsysVersion_Object((1,3,6,1,4,1,562,73,1,1,1,1,1,4),_NnsysVersion_Type())
nnsysVersion.setMaxAccess(_G)
if mibBuilder.loadTexts:nnsysVersion.setStatus(_A)
class _NnsysHostName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_NnsysHostName_Type.__name__=_D
_NnsysHostName_Object=MibScalar
nnsysHostName=_NnsysHostName_Object((1,3,6,1,4,1,562,73,1,1,1,1,1,6),_NnsysHostName_Type())
nnsysHostName.setMaxAccess(_C)
if mibBuilder.loadTexts:nnsysHostName.setStatus(_A)
class _NnsysDomainName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_NnsysDomainName_Type.__name__=_D
_NnsysDomainName_Object=MibScalar
nnsysDomainName=_NnsysDomainName_Object((1,3,6,1,4,1,562,73,1,1,1,1,1,7),_NnsysDomainName_Type())
nnsysDomainName.setMaxAccess(_C)
if mibBuilder.loadTexts:nnsysDomainName.setStatus(_A)
class _NnsysAlarmStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('clear',1),('minor',2),('major',3)))
_NnsysAlarmStatus_Type.__name__=_F
_NnsysAlarmStatus_Object=MibScalar
nnsysAlarmStatus=_NnsysAlarmStatus_Object((1,3,6,1,4,1,562,73,1,1,1,1,1,8),_NnsysAlarmStatus_Type())
nnsysAlarmStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:nnsysAlarmStatus.setStatus(_A)
class _NnsysReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),('reset',2)))
_NnsysReset_Type.__name__=_F
_NnsysReset_Object=MibScalar
nnsysReset=_NnsysReset_Object((1,3,6,1,4,1,562,73,1,1,1,1,1,10),_NnsysReset_Type())
nnsysReset.setMaxAccess(_C)
if mibBuilder.loadTexts:nnsysReset.setStatus(_A)
class _NnsysDateTime_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_NnsysDateTime_Type.__name__=_I
_NnsysDateTime_Object=MibScalar
nnsysDateTime=_NnsysDateTime_Object((1,3,6,1,4,1,562,73,1,1,1,1,1,11),_NnsysDateTime_Type())
nnsysDateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:nnsysDateTime.setStatus(_A)
_NnarpClearAtTable_Type=Integer32
_NnarpClearAtTable_Object=MibScalar
nnarpClearAtTable=_NnarpClearAtTable_Object((1,3,6,1,4,1,562,73,1,1,1,1,1,12),_NnarpClearAtTable_Type())
nnarpClearAtTable.setMaxAccess(_C)
if mibBuilder.loadTexts:nnarpClearAtTable.setStatus(_A)
_NnipClearRouteTable_Type=Integer32
_NnipClearRouteTable_Object=MibScalar
nnipClearRouteTable=_NnipClearRouteTable_Object((1,3,6,1,4,1,562,73,1,1,1,1,1,13),_NnipClearRouteTable_Type())
nnipClearRouteTable.setMaxAccess(_C)
if mibBuilder.loadTexts:nnipClearRouteTable.setStatus(_A)
class _NnarpTimeOut_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,28800))
_NnarpTimeOut_Type.__name__=_F
_NnarpTimeOut_Object=MibScalar
nnarpTimeOut=_NnarpTimeOut_Object((1,3,6,1,4,1,562,73,1,1,1,1,1,14),_NnarpTimeOut_Type())
nnarpTimeOut.setMaxAccess(_C)
if mibBuilder.loadTexts:nnarpTimeOut.setStatus(_A)
_NndnsGroup_ObjectIdentity=ObjectIdentity
nndnsGroup=_NndnsGroup_ObjectIdentity((1,3,6,1,4,1,562,73,1,1,1,1,2))
class _NndnsEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_R,2)))
_NndnsEnable_Type.__name__=_F
_NndnsEnable_Object=MibScalar
nndnsEnable=_NndnsEnable_Object((1,3,6,1,4,1,562,73,1,1,1,1,2,1),_NndnsEnable_Type())
nndnsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:nndnsEnable.setStatus(_A)
_NndnsServerTable_Object=MibTable
nndnsServerTable=_NndnsServerTable_Object((1,3,6,1,4,1,562,73,1,1,1,1,2,2))
if mibBuilder.loadTexts:nndnsServerTable.setStatus(_A)
_NndnsServerEntry_Object=MibTableRow
nndnsServerEntry=_NndnsServerEntry_Object((1,3,6,1,4,1,562,73,1,1,1,1,2,2,1))
nndnsServerEntry.setIndexNames((0,_B,_S))
if mibBuilder.loadTexts:nndnsServerEntry.setStatus(_A)
class _NndnsServerEntryType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('invalid',1),('primary',2),(_L,3)))
_NndnsServerEntryType_Type.__name__=_F
_NndnsServerEntryType_Object=MibTableColumn
nndnsServerEntryType=_NndnsServerEntryType_Object((1,3,6,1,4,1,562,73,1,1,1,1,2,2,1,1),_NndnsServerEntryType_Type())
nndnsServerEntryType.setMaxAccess(_C)
if mibBuilder.loadTexts:nndnsServerEntryType.setStatus(_A)
_NndnsServerAddr_Type=IpAddress
_NndnsServerAddr_Object=MibTableColumn
nndnsServerAddr=_NndnsServerAddr_Object((1,3,6,1,4,1,562,73,1,1,1,1,2,2,1,2),_NndnsServerAddr_Type())
nndnsServerAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:nndnsServerAddr.setStatus(_A)
_NnsystemEnableNotification_ObjectIdentity=ObjectIdentity
nnsystemEnableNotification=_NnsystemEnableNotification_ObjectIdentity((1,3,6,1,4,1,562,73,1,1,1,1,3))
class _NnenableSysShutDownNotification_Type(TruthValue):defaultValue=1
_NnenableSysShutDownNotification_Type.__name__=_E
_NnenableSysShutDownNotification_Object=MibScalar
nnenableSysShutDownNotification=_NnenableSysShutDownNotification_Object((1,3,6,1,4,1,562,73,1,1,1,1,3,1),_NnenableSysShutDownNotification_Type())
nnenableSysShutDownNotification.setMaxAccess(_C)
if mibBuilder.loadTexts:nnenableSysShutDownNotification.setStatus(_A)
class _NnenableUserLoginNotification_Type(TruthValue):defaultValue=1
_NnenableUserLoginNotification_Type.__name__=_E
_NnenableUserLoginNotification_Object=MibScalar
nnenableUserLoginNotification=_NnenableUserLoginNotification_Object((1,3,6,1,4,1,562,73,1,1,1,1,3,2),_NnenableUserLoginNotification_Type())
nnenableUserLoginNotification.setMaxAccess(_C)
if mibBuilder.loadTexts:nnenableUserLoginNotification.setStatus(_A)
class _NnenableUserLogOffNotification_Type(TruthValue):defaultValue=1
_NnenableUserLogOffNotification_Type.__name__=_E
_NnenableUserLogOffNotification_Object=MibScalar
nnenableUserLogOffNotification=_NnenableUserLogOffNotification_Object((1,3,6,1,4,1,562,73,1,1,1,1,3,3),_NnenableUserLogOffNotification_Type())
nnenableUserLogOffNotification.setMaxAccess(_C)
if mibBuilder.loadTexts:nnenableUserLogOffNotification.setStatus(_A)
class _NnenableUserLoginFailNotification_Type(TruthValue):defaultValue=1
_NnenableUserLoginFailNotification_Type.__name__=_E
_NnenableUserLoginFailNotification_Object=MibScalar
nnenableUserLoginFailNotification=_NnenableUserLoginFailNotification_Object((1,3,6,1,4,1,562,73,1,1,1,1,3,4),_NnenableUserLoginFailNotification_Type())
nnenableUserLoginFailNotification.setMaxAccess(_C)
if mibBuilder.loadTexts:nnenableUserLoginFailNotification.setStatus(_A)
class _NnenableAuthenticationLoginFailNotification_Type(TruthValue):defaultValue=1
_NnenableAuthenticationLoginFailNotification_Type.__name__=_E
_NnenableAuthenticationLoginFailNotification_Object=MibScalar
nnenableAuthenticationLoginFailNotification=_NnenableAuthenticationLoginFailNotification_Object((1,3,6,1,4,1,562,73,1,1,1,1,3,5),_NnenableAuthenticationLoginFailNotification_Type())
nnenableAuthenticationLoginFailNotification.setMaxAccess(_C)
if mibBuilder.loadTexts:nnenableAuthenticationLoginFailNotification.setStatus(_A)
class _NnenableAuthenticationLoginSuccessNotification_Type(TruthValue):defaultValue=1
_NnenableAuthenticationLoginSuccessNotification_Type.__name__=_E
_NnenableAuthenticationLoginSuccessNotification_Object=MibScalar
nnenableAuthenticationLoginSuccessNotification=_NnenableAuthenticationLoginSuccessNotification_Object((1,3,6,1,4,1,562,73,1,1,1,1,3,6),_NnenableAuthenticationLoginSuccessNotification_Type())
nnenableAuthenticationLoginSuccessNotification.setMaxAccess(_C)
if mibBuilder.loadTexts:nnenableAuthenticationLoginSuccessNotification.setStatus(_A)
class _NnenableLogoutNotification_Type(TruthValue):defaultValue=1
_NnenableLogoutNotification_Type.__name__=_E
_NnenableLogoutNotification_Object=MibScalar
nnenableLogoutNotification=_NnenableLogoutNotification_Object((1,3,6,1,4,1,562,73,1,1,1,1,3,7),_NnenableLogoutNotification_Type())
nnenableLogoutNotification.setMaxAccess(_C)
if mibBuilder.loadTexts:nnenableLogoutNotification.setStatus(_A)
_NnsystemNotifications_ObjectIdentity=ObjectIdentity
nnsystemNotifications=_NnsystemNotifications_ObjectIdentity((1,3,6,1,4,1,562,73,1,1,1,1,4))
_NnsystemTraps_ObjectIdentity=ObjectIdentity
nnsystemTraps=_NnsystemTraps_ObjectIdentity((1,3,6,1,4,1,562,73,1,1,1,1,4,0))
_NnuserAdminGroup_ObjectIdentity=ObjectIdentity
nnuserAdminGroup=_NnuserAdminGroup_ObjectIdentity((1,3,6,1,4,1,562,73,1,1,1,1,5))
class _NnuserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_NnuserName_Type.__name__=_D
_NnuserName_Object=MibScalar
nnuserName=_NnuserName_Object((1,3,6,1,4,1,562,73,1,1,1,1,5,1),_NnuserName_Type())
nnuserName.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:nnuserName.setStatus(_A)
_NnsntpGroup_ObjectIdentity=ObjectIdentity
nnsntpGroup=_NnsntpGroup_ObjectIdentity((1,3,6,1,4,1,562,73,1,1,1,1,10))
class _NnsntpClieenabled_Type(SntpEnabled):defaultValue=1
_NnsntpClieenabled_Type.__name__=_T
_NnsntpClieenabled_Object=MibScalar
nnsntpClieenabled=_NnsntpClieenabled_Object((1,3,6,1,4,1,562,73,1,1,1,1,10,1),_NnsntpClieenabled_Type())
nnsntpClieenabled.setMaxAccess(_Q)
if mibBuilder.loadTexts:nnsntpClieenabled.setStatus(_A)
class _NnsntpServerAddr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_NnsntpServerAddr_Type.__name__=_D
_NnsntpServerAddr_Object=MibScalar
nnsntpServerAddr=_NnsntpServerAddr_Object((1,3,6,1,4,1,562,73,1,1,1,1,10,2),_NnsntpServerAddr_Type())
nnsntpServerAddr.setMaxAccess(_Q)
if mibBuilder.loadTexts:nnsntpServerAddr.setStatus(_A)
class _NnsntpTimeout_Type(Integer32):defaultValue=1024
_NnsntpTimeout_Type.__name__=_F
_NnsntpTimeout_Object=MibScalar
nnsntpTimeout=_NnsntpTimeout_Object((1,3,6,1,4,1,562,73,1,1,1,1,10,3),_NnsntpTimeout_Type())
nnsntpTimeout.setMaxAccess(_Q)
if mibBuilder.loadTexts:nnsntpTimeout.setStatus(_A)
_NnsntpNotificationEnables_ObjectIdentity=ObjectIdentity
nnsntpNotificationEnables=_NnsntpNotificationEnables_ObjectIdentity((1,3,6,1,4,1,562,73,1,1,1,1,11))
class _NnenableSntpNotification_Type(TruthValue):defaultValue=1
_NnenableSntpNotification_Type.__name__=_E
_NnenableSntpNotification_Object=MibScalar
nnenableSntpNotification=_NnenableSntpNotification_Object((1,3,6,1,4,1,562,73,1,1,1,1,11,1),_NnenableSntpNotification_Type())
nnenableSntpNotification.setMaxAccess(_C)
if mibBuilder.loadTexts:nnenableSntpNotification.setStatus(_A)
_NnsntpNotifications_ObjectIdentity=ObjectIdentity
nnsntpNotifications=_NnsntpNotifications_ObjectIdentity((1,3,6,1,4,1,562,73,1,1,1,1,12))
_NnsntpTraps_ObjectIdentity=ObjectIdentity
nnsntpTraps=_NnsntpTraps_ObjectIdentity((1,3,6,1,4,1,562,73,1,1,1,1,12,0))
_NnenableBgpNotifications_ObjectIdentity=ObjectIdentity
nnenableBgpNotifications=_NnenableBgpNotifications_ObjectIdentity((1,3,6,1,4,1,562,73,1,1,1,1,14))
class _NnenableBgpEstablishedNotification_Type(TruthValue):defaultValue=1
_NnenableBgpEstablishedNotification_Type.__name__=_E
_NnenableBgpEstablishedNotification_Object=MibScalar
nnenableBgpEstablishedNotification=_NnenableBgpEstablishedNotification_Object((1,3,6,1,4,1,562,73,1,1,1,1,14,1),_NnenableBgpEstablishedNotification_Type())
nnenableBgpEstablishedNotification.setMaxAccess(_G)
if mibBuilder.loadTexts:nnenableBgpEstablishedNotification.setStatus(_A)
class _NnenableBgpBackwardNotification_Type(TruthValue):defaultValue=1
_NnenableBgpBackwardNotification_Type.__name__=_E
_NnenableBgpBackwardNotification_Object=MibScalar
nnenableBgpBackwardNotification=_NnenableBgpBackwardNotification_Object((1,3,6,1,4,1,562,73,1,1,1,1,14,2),_NnenableBgpBackwardNotification_Type())
nnenableBgpBackwardNotification.setMaxAccess(_G)
if mibBuilder.loadTexts:nnenableBgpBackwardNotification.setStatus(_A)
_NnsystemNotificationsVars_ObjectIdentity=ObjectIdentity
nnsystemNotificationsVars=_NnsystemNotificationsVars_ObjectIdentity((1,3,6,1,4,1,562,73,1,1,1,1,15))
class _NnsysRestartMsg_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_NnsysRestartMsg_Type.__name__=_D
_NnsysRestartMsg_Object=MibScalar
nnsysRestartMsg=_NnsysRestartMsg_Object((1,3,6,1,4,1,562,73,1,1,1,1,15,1),_NnsysRestartMsg_Type())
nnsysRestartMsg.setMaxAccess(_H)
if mibBuilder.loadTexts:nnsysRestartMsg.setStatus(_A)
class _NnsysLoginMsg_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_NnsysLoginMsg_Type.__name__=_D
_NnsysLoginMsg_Object=MibScalar
nnsysLoginMsg=_NnsysLoginMsg_Object((1,3,6,1,4,1,562,73,1,1,1,1,15,2),_NnsysLoginMsg_Type())
nnsysLoginMsg.setMaxAccess(_H)
if mibBuilder.loadTexts:nnsysLoginMsg.setStatus(_A)
class _NnsysLogoutMsg_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_NnsysLogoutMsg_Type.__name__=_D
_NnsysLogoutMsg_Object=MibScalar
nnsysLogoutMsg=_NnsysLogoutMsg_Object((1,3,6,1,4,1,562,73,1,1,1,1,15,3),_NnsysLogoutMsg_Type())
nnsysLogoutMsg.setMaxAccess(_H)
if mibBuilder.loadTexts:nnsysLogoutMsg.setStatus(_A)
class _NnsysLoginFailMsg_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_NnsysLoginFailMsg_Type.__name__=_D
_NnsysLoginFailMsg_Object=MibScalar
nnsysLoginFailMsg=_NnsysLoginFailMsg_Object((1,3,6,1,4,1,562,73,1,1,1,1,15,4),_NnsysLoginFailMsg_Type())
nnsysLoginFailMsg.setMaxAccess(_H)
if mibBuilder.loadTexts:nnsysLoginFailMsg.setStatus(_A)
class _NnprotocolType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('gui',1),('ssh',2),(_L,3)))
_NnprotocolType_Type.__name__=_F
_NnprotocolType_Object=MibScalar
nnprotocolType=_NnprotocolType_Object((1,3,6,1,4,1,562,73,1,1,1,1,15,5),_NnprotocolType_Type())
nnprotocolType.setMaxAccess(_H)
if mibBuilder.loadTexts:nnprotocolType.setStatus(_A)
class _NnclientIpAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_NnclientIpAddress_Type.__name__=_D
_NnclientIpAddress_Object=MibScalar
nnclientIpAddress=_NnclientIpAddress_Object((1,3,6,1,4,1,562,73,1,1,1,1,15,6),_NnclientIpAddress_Type())
nnclientIpAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:nnclientIpAddress.setStatus(_A)
class _NntimeStamp_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_NntimeStamp_Type.__name__=_D
_NntimeStamp_Object=MibScalar
nntimeStamp=_NntimeStamp_Object((1,3,6,1,4,1,562,73,1,1,1,1,15,7),_NntimeStamp_Type())
nntimeStamp.setMaxAccess(_H)
if mibBuilder.loadTexts:nntimeStamp.setStatus(_A)
class _NnreasonForFailure_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('username',1),('password',2),(_L,3)))
_NnreasonForFailure_Type.__name__=_F
_NnreasonForFailure_Object=MibScalar
nnreasonForFailure=_NnreasonForFailure_Object((1,3,6,1,4,1,562,73,1,1,1,1,15,8),_NnreasonForFailure_Type())
nnreasonForFailure.setMaxAccess(_H)
if mibBuilder.loadTexts:nnreasonForFailure.setStatus(_A)
_NnsysDst_ObjectIdentity=ObjectIdentity
nnsysDst=_NnsysDst_ObjectIdentity((1,3,6,1,4,1,562,73,1,1,1,1,20))
class _NnsysDstLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_NnsysDstLocation_Type.__name__=_D
_NnsysDstLocation_Object=MibScalar
nnsysDstLocation=_NnsysDstLocation_Object((1,3,6,1,4,1,562,73,1,1,1,1,20,1),_NnsysDstLocation_Type())
nnsysDstLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:nnsysDstLocation.setStatus(_A)
class _NnsysDstCurTimeZone_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_NnsysDstCurTimeZone_Type.__name__=_I
_NnsysDstCurTimeZone_Object=MibScalar
nnsysDstCurTimeZone=_NnsysDstCurTimeZone_Object((1,3,6,1,4,1,562,73,1,1,1,1,20,2),_NnsysDstCurTimeZone_Type())
nnsysDstCurTimeZone.setMaxAccess(_G)
if mibBuilder.loadTexts:nnsysDstCurTimeZone.setStatus(_A)
class _NnsysDstCurTime_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_NnsysDstCurTime_Type.__name__=_I
_NnsysDstCurTime_Object=MibScalar
nnsysDstCurTime=_NnsysDstCurTime_Object((1,3,6,1,4,1,562,73,1,1,1,1,20,3),_NnsysDstCurTime_Type())
nnsysDstCurTime.setMaxAccess(_C)
if mibBuilder.loadTexts:nnsysDstCurTime.setStatus(_A)
class _NnsysDstAutomated_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_R,2)))
_NnsysDstAutomated_Type.__name__=_F
_NnsysDstAutomated_Object=MibScalar
nnsysDstAutomated=_NnsysDstAutomated_Object((1,3,6,1,4,1,562,73,1,1,1,1,20,4),_NnsysDstAutomated_Type())
nnsysDstAutomated.setMaxAccess(_G)
if mibBuilder.loadTexts:nnsysDstAutomated.setStatus(_A)
class _NnsysDstStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('notactive',2)))
_NnsysDstStatus_Type.__name__=_F
_NnsysDstStatus_Object=MibScalar
nnsysDstStatus=_NnsysDstStatus_Object((1,3,6,1,4,1,562,73,1,1,1,1,20,5),_NnsysDstStatus_Type())
nnsysDstStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:nnsysDstStatus.setStatus(_A)
class _NnsysDstStart_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(7,7));fixedLength=7
_NnsysDstStart_Type.__name__=_I
_NnsysDstStart_Object=MibScalar
nnsysDstStart=_NnsysDstStart_Object((1,3,6,1,4,1,562,73,1,1,1,1,20,6),_NnsysDstStart_Type())
nnsysDstStart.setMaxAccess(_C)
if mibBuilder.loadTexts:nnsysDstStart.setStatus(_A)
class _NnsysDstEnd_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(7,7));fixedLength=7
_NnsysDstEnd_Type.__name__=_I
_NnsysDstEnd_Object=MibScalar
nnsysDstEnd=_NnsysDstEnd_Object((1,3,6,1,4,1,562,73,1,1,1,1,20,7),_NnsysDstEnd_Type())
nnsysDstEnd.setMaxAccess(_C)
if mibBuilder.loadTexts:nnsysDstEnd.setStatus(_A)
class _NnsysDstDuration_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_NnsysDstDuration_Type.__name__=_I
_NnsysDstDuration_Object=MibScalar
nnsysDstDuration=_NnsysDstDuration_Object((1,3,6,1,4,1,562,73,1,1,1,1,20,8),_NnsysDstDuration_Type())
nnsysDstDuration.setMaxAccess(_G)
if mibBuilder.loadTexts:nnsysDstDuration.setStatus(_A)
_NnssmTraps_ObjectIdentity=ObjectIdentity
nnssmTraps=_NnssmTraps_ObjectIdentity((1,3,6,1,4,1,562,73,1,1,1,1,21))
_NnssmNotifications_ObjectIdentity=ObjectIdentity
nnssmNotifications=_NnssmNotifications_ObjectIdentity((1,3,6,1,4,1,562,73,1,1,1,1,21,0))
_NnssmTrapVariables_ObjectIdentity=ObjectIdentity
nnssmTrapVariables=_NnssmTrapVariables_ObjectIdentity((1,3,6,1,4,1,562,73,1,1,1,1,21,1))
class _NnssmCurrentState_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_NnssmCurrentState_Type.__name__=_D
_NnssmCurrentState_Object=MibScalar
nnssmCurrentState=_NnssmCurrentState_Object((1,3,6,1,4,1,562,73,1,1,1,1,21,1,1),_NnssmCurrentState_Type())
nnssmCurrentState.setMaxAccess(_H)
if mibBuilder.loadTexts:nnssmCurrentState.setStatus(_A)
class _NnssmPreviousState_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_NnssmPreviousState_Type.__name__=_D
_NnssmPreviousState_Object=MibScalar
nnssmPreviousState=_NnssmPreviousState_Object((1,3,6,1,4,1,562,73,1,1,1,1,21,1,2),_NnssmPreviousState_Type())
nnssmPreviousState.setMaxAccess(_H)
if mibBuilder.loadTexts:nnssmPreviousState.setStatus(_A)
class _NnenableSsmModeNotification_Type(TruthValue):defaultValue=1
_NnenableSsmModeNotification_Type.__name__=_E
_NnenableSsmModeNotification_Object=MibScalar
nnenableSsmModeNotification=_NnenableSsmModeNotification_Object((1,3,6,1,4,1,562,73,1,1,1,1,21,2),_NnenableSsmModeNotification_Type())
nnenableSsmModeNotification.setMaxAccess(_C)
if mibBuilder.loadTexts:nnenableSsmModeNotification.setStatus(_A)
nnshutDownNotification=NotificationType((1,3,6,1,4,1,562,73,1,1,1,1,4,0,1))
nnshutDownNotification.setObjects((_B,_U))
if mibBuilder.loadTexts:nnshutDownNotification.setStatus(_A)
nnuserLoginNotification=NotificationType((1,3,6,1,4,1,562,73,1,1,1,1,4,0,2))
nnuserLoginNotification.setObjects((_B,_V))
if mibBuilder.loadTexts:nnuserLoginNotification.setStatus(_A)
nnuserLogOffNotification=NotificationType((1,3,6,1,4,1,562,73,1,1,1,1,4,0,3))
nnuserLogOffNotification.setObjects((_B,_W))
if mibBuilder.loadTexts:nnuserLogOffNotification.setStatus(_A)
nnuserLoginFailNotification=NotificationType((1,3,6,1,4,1,562,73,1,1,1,1,4,0,4))
nnuserLoginFailNotification.setObjects((_B,_X))
if mibBuilder.loadTexts:nnuserLoginFailNotification.setStatus(_A)
nnauthenticationFailureNotification=NotificationType((1,3,6,1,4,1,562,73,1,1,1,1,4,0,5))
nnauthenticationFailureNotification.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_Y)))
if mibBuilder.loadTexts:nnauthenticationFailureNotification.setStatus(_A)
nnauthenticationLoginSuccessNotification=NotificationType((1,3,6,1,4,1,562,73,1,1,1,1,4,0,6))
nnauthenticationLoginSuccessNotification.setObjects(*((_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:nnauthenticationLoginSuccessNotification.setStatus(_A)
nnlogoutNotification=NotificationType((1,3,6,1,4,1,562,73,1,1,1,1,4,0,7))
nnlogoutNotification.setObjects(*((_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:nnlogoutNotification.setStatus(_A)
nnsntpEnableNotification=NotificationType((1,3,6,1,4,1,562,73,1,1,1,1,12,0,1))
nnsntpEnableNotification.setObjects(*((_B,_J),(_B,_K)))
if mibBuilder.loadTexts:nnsntpEnableNotification.setStatus(_A)
nnsntpDisableNotification=NotificationType((1,3,6,1,4,1,562,73,1,1,1,1,12,0,2))
nnsntpDisableNotification.setObjects(*((_B,_J),(_B,_K)))
if mibBuilder.loadTexts:nnsntpDisableNotification.setStatus(_A)
nnsntpSuccessNotification=NotificationType((1,3,6,1,4,1,562,73,1,1,1,1,12,0,3))
nnsntpSuccessNotification.setObjects(*((_B,_J),(_B,_K)))
if mibBuilder.loadTexts:nnsntpSuccessNotification.setStatus(_A)
nnsntpErrorNotification=NotificationType((1,3,6,1,4,1,562,73,1,1,1,1,12,0,4))
nnsntpErrorNotification.setObjects(*((_B,_J),(_B,_K)))
if mibBuilder.loadTexts:nnsntpErrorNotification.setStatus(_A)
nnssmFromNormalTrap=NotificationType((1,3,6,1,4,1,562,73,1,1,1,1,21,0,1))
nnssmFromNormalTrap.setObjects((_B,_Z))
if mibBuilder.loadTexts:nnssmFromNormalTrap.setStatus(_A)
nnssmToNormalTrap=NotificationType((1,3,6,1,4,1,562,73,1,1,1,1,21,0,2))
nnssmToNormalTrap.setObjects((_B,_a))
if mibBuilder.loadTexts:nnssmToNormalTrap.setStatus(_A)
nnsystemNotificationGroup=NotificationGroup((1,3,6,1,4,1,562,73,1,1,1,1,18))
nnsystemNotificationGroup.setObjects(*((_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:nnsystemNotificationGroup.setStatus(_A)
nnsntpNotificationGroup=NotificationGroup((1,3,6,1,4,1,562,73,1,1,1,1,19))
nnsntpNotificationGroup.setObjects(*((_B,_i),(_B,_j),(_B,_k),(_B,_l)))
if mibBuilder.loadTexts:nnsntpNotificationGroup.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_T:SntpEnabled,'nnsystemMib':nnsystemMib,'nnsystemObjects':nnsystemObjects,'nnsysIpAddr':nnsysIpAddr,'nnsysNetMask':nnsysNetMask,'nnsysBroadcast':nnsysBroadcast,'nnsysVersion':nnsysVersion,'nnsysHostName':nnsysHostName,'nnsysDomainName':nnsysDomainName,'nnsysAlarmStatus':nnsysAlarmStatus,'nnsysReset':nnsysReset,'nnsysDateTime':nnsysDateTime,'nnarpClearAtTable':nnarpClearAtTable,'nnipClearRouteTable':nnipClearRouteTable,'nnarpTimeOut':nnarpTimeOut,'nndnsGroup':nndnsGroup,'nndnsEnable':nndnsEnable,'nndnsServerTable':nndnsServerTable,'nndnsServerEntry':nndnsServerEntry,'nndnsServerEntryType':nndnsServerEntryType,_S:nndnsServerAddr,'nnsystemEnableNotification':nnsystemEnableNotification,'nnenableSysShutDownNotification':nnenableSysShutDownNotification,'nnenableUserLoginNotification':nnenableUserLoginNotification,'nnenableUserLogOffNotification':nnenableUserLogOffNotification,'nnenableUserLoginFailNotification':nnenableUserLoginFailNotification,'nnenableAuthenticationLoginFailNotification':nnenableAuthenticationLoginFailNotification,'nnenableAuthenticationLoginSuccessNotification':nnenableAuthenticationLoginSuccessNotification,'nnenableLogoutNotification':nnenableLogoutNotification,'nnsystemNotifications':nnsystemNotifications,'nnsystemTraps':nnsystemTraps,_b:nnshutDownNotification,_c:nnuserLoginNotification,_d:nnuserLogOffNotification,_e:nnuserLoginFailNotification,_f:nnauthenticationFailureNotification,_g:nnauthenticationLoginSuccessNotification,_h:nnlogoutNotification,'nnuserAdminGroup':nnuserAdminGroup,'nnuserName':nnuserName,'nnsntpGroup':nnsntpGroup,'nnsntpClieenabled':nnsntpClieenabled,_J:nnsntpServerAddr,_K:nnsntpTimeout,'nnsntpNotificationEnables':nnsntpNotificationEnables,'nnenableSntpNotification':nnenableSntpNotification,'nnsntpNotifications':nnsntpNotifications,'nnsntpTraps':nnsntpTraps,_i:nnsntpEnableNotification,_j:nnsntpDisableNotification,_k:nnsntpSuccessNotification,_l:nnsntpErrorNotification,'nnenableBgpNotifications':nnenableBgpNotifications,'nnenableBgpEstablishedNotification':nnenableBgpEstablishedNotification,'nnenableBgpBackwardNotification':nnenableBgpBackwardNotification,'nnsystemNotificationsVars':nnsystemNotificationsVars,_U:nnsysRestartMsg,_V:nnsysLoginMsg,_W:nnsysLogoutMsg,_X:nnsysLoginFailMsg,_M:nnprotocolType,_N:nnclientIpAddress,_O:nntimeStamp,_Y:nnreasonForFailure,'nnsystemNotificationGroup':nnsystemNotificationGroup,'nnsntpNotificationGroup':nnsntpNotificationGroup,'nnsysDst':nnsysDst,'nnsysDstLocation':nnsysDstLocation,'nnsysDstCurTimeZone':nnsysDstCurTimeZone,'nnsysDstCurTime':nnsysDstCurTime,'nnsysDstAutomated':nnsysDstAutomated,'nnsysDstStatus':nnsysDstStatus,'nnsysDstStart':nnsysDstStart,'nnsysDstEnd':nnsysDstEnd,'nnsysDstDuration':nnsysDstDuration,'nnssmTraps':nnssmTraps,'nnssmNotifications':nnssmNotifications,'nnssmFromNormalTrap':nnssmFromNormalTrap,'nnssmToNormalTrap':nnssmToNormalTrap,'nnssmTrapVariables':nnssmTrapVariables,_Z:nnssmCurrentState,_a:nnssmPreviousState,'nnenableSsmModeNotification':nnenableSsmModeNotification})