_l='tmnxLdapNotifyGroup'
_k='tmnxLdapInitialGroup'
_j='tmnxLdapServerOperStateChange'
_i='tmnxLdapOperStateChange'
_h='tmnxLdapServerTlsProfile'
_g='tmnxLdapServerSearch'
_f='tmnxLdapServerBindAuthPassword'
_e='tmnxLdapServerBindAuthRootDn'
_d='tmnxLdapServerAdminState'
_c='tmnxLdapServerRowStatus'
_b='tmnxLdapServerLastChanged'
_a='tmnxLdapServerTableLastChanged'
_Z='tmnxLdapPublicKeyAuthentication'
_Y='tmnxLdapUseTemplate'
_X='tmnxLdapTimeout'
_W='tmnxLdapRetryAttempts'
_V='tmnxLdapAdminState'
_U='tmnxLdapServerIndex'
_T='TTcpUdpPort'
_S='DisplayString'
_R='InetAddressType'
_Q='InetAddress'
_P='tmnxLdapServerName'
_O='tmnxLdapServerPort'
_N='tmnxLdapServerInetAddress'
_M='tmnxLdapServerInetAddressType'
_L='tmnxLdapServerOperState'
_K='tmnxLdapOperState'
_J='TmnxLongDisplayString'
_I='TmnxAdminState'
_H='TNamedItemOrEmpty'
_G='TruthValue'
_F='read-only'
_E='Unsigned32'
_D='read-write'
_C='read-create'
_B='current'
_A='TIMETRA-LDAP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_Q,_R)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_S,'PhysAddress','RowStatus','TextualConvention','TimeStamp',_G)
timetraSRMIBModules,tmnxSRConfs,tmnxSRNotifyPrefix,tmnxSRObjs=mibBuilder.importSymbols('TIMETRA-GLOBAL-MIB','timetraSRMIBModules','tmnxSRConfs','tmnxSRNotifyPrefix','tmnxSRObjs')
TNamedItemOrEmpty,TTcpUdpPort,TmnxAdminState,TmnxLongDisplayString,TmnxOperState=mibBuilder.importSymbols('TIMETRA-TC-MIB',_H,_T,_I,_J,'TmnxOperState')
timetraLdapMIBModule=ModuleIdentity((1,3,6,1,4,1,6527,1,1,3,106))
if mibBuilder.loadTexts:timetraLdapMIBModule.setRevisions(('2016-02-01 00:00',))
_TmnxLdapConformance_ObjectIdentity=ObjectIdentity
tmnxLdapConformance=_TmnxLdapConformance_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,106))
_TmnxLdapCompliances_ObjectIdentity=ObjectIdentity
tmnxLdapCompliances=_TmnxLdapCompliances_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,106,1))
_TmnxLdapGroups_ObjectIdentity=ObjectIdentity
tmnxLdapGroups=_TmnxLdapGroups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,106,2))
_TmnxLdapInitialGroups_ObjectIdentity=ObjectIdentity
tmnxLdapInitialGroups=_TmnxLdapInitialGroups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,106,2,1))
_TmnxLdapObjs_ObjectIdentity=ObjectIdentity
tmnxLdapObjs=_TmnxLdapObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,106))
_TmnxLdapScalarObjs_ObjectIdentity=ObjectIdentity
tmnxLdapScalarObjs=_TmnxLdapScalarObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,106,1))
_TmnxLdapScalarStatsObjs_ObjectIdentity=ObjectIdentity
tmnxLdapScalarStatsObjs=_TmnxLdapScalarStatsObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,106,1,1))
_TmnxLdapServerTableLastChanged_Type=TimeStamp
_TmnxLdapServerTableLastChanged_Object=MibScalar
tmnxLdapServerTableLastChanged=_TmnxLdapServerTableLastChanged_Object((1,3,6,1,4,1,6527,3,1,2,106,1,1,1),_TmnxLdapServerTableLastChanged_Type())
tmnxLdapServerTableLastChanged.setMaxAccess(_F)
if mibBuilder.loadTexts:tmnxLdapServerTableLastChanged.setStatus(_B)
_TmnxLdapScalarConfigObjs_ObjectIdentity=ObjectIdentity
tmnxLdapScalarConfigObjs=_TmnxLdapScalarConfigObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,106,1,2))
class _TmnxLdapAdminState_Type(TmnxAdminState):defaultValue=2
_TmnxLdapAdminState_Type.__name__=_I
_TmnxLdapAdminState_Object=MibScalar
tmnxLdapAdminState=_TmnxLdapAdminState_Object((1,3,6,1,4,1,6527,3,1,2,106,1,2,1),_TmnxLdapAdminState_Type())
tmnxLdapAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxLdapAdminState.setStatus(_B)
_TmnxLdapOperState_Type=TmnxOperState
_TmnxLdapOperState_Object=MibScalar
tmnxLdapOperState=_TmnxLdapOperState_Object((1,3,6,1,4,1,6527,3,1,2,106,1,2,2),_TmnxLdapOperState_Type())
tmnxLdapOperState.setMaxAccess(_F)
if mibBuilder.loadTexts:tmnxLdapOperState.setStatus(_B)
class _TmnxLdapRetryAttempts_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_TmnxLdapRetryAttempts_Type.__name__=_E
_TmnxLdapRetryAttempts_Object=MibScalar
tmnxLdapRetryAttempts=_TmnxLdapRetryAttempts_Object((1,3,6,1,4,1,6527,3,1,2,106,1,2,3),_TmnxLdapRetryAttempts_Type())
tmnxLdapRetryAttempts.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxLdapRetryAttempts.setStatus(_B)
class _TmnxLdapTimeout_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,90))
_TmnxLdapTimeout_Type.__name__=_E
_TmnxLdapTimeout_Object=MibScalar
tmnxLdapTimeout=_TmnxLdapTimeout_Object((1,3,6,1,4,1,6527,3,1,2,106,1,2,4),_TmnxLdapTimeout_Type())
tmnxLdapTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxLdapTimeout.setStatus(_B)
if mibBuilder.loadTexts:tmnxLdapTimeout.setUnits('Seconds')
class _TmnxLdapUseTemplate_Type(TruthValue):defaultValue=1
_TmnxLdapUseTemplate_Type.__name__=_G
_TmnxLdapUseTemplate_Object=MibScalar
tmnxLdapUseTemplate=_TmnxLdapUseTemplate_Object((1,3,6,1,4,1,6527,3,1,2,106,1,2,5),_TmnxLdapUseTemplate_Type())
tmnxLdapUseTemplate.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxLdapUseTemplate.setStatus(_B)
class _TmnxLdapPublicKeyAuthentication_Type(TruthValue):defaultValue=2
_TmnxLdapPublicKeyAuthentication_Type.__name__=_G
_TmnxLdapPublicKeyAuthentication_Object=MibScalar
tmnxLdapPublicKeyAuthentication=_TmnxLdapPublicKeyAuthentication_Object((1,3,6,1,4,1,6527,3,1,2,106,1,2,6),_TmnxLdapPublicKeyAuthentication_Type())
tmnxLdapPublicKeyAuthentication.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxLdapPublicKeyAuthentication.setStatus(_B)
_TmnxLdapConfigObjs_ObjectIdentity=ObjectIdentity
tmnxLdapConfigObjs=_TmnxLdapConfigObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,106,2))
_TmnxLdapServerTable_Object=MibTable
tmnxLdapServerTable=_TmnxLdapServerTable_Object((1,3,6,1,4,1,6527,3,1,2,106,2,1))
if mibBuilder.loadTexts:tmnxLdapServerTable.setStatus(_B)
_TmnxLdapServerEntry_Object=MibTableRow
tmnxLdapServerEntry=_TmnxLdapServerEntry_Object((1,3,6,1,4,1,6527,3,1,2,106,2,1,1))
tmnxLdapServerEntry.setIndexNames((0,_A,_U))
if mibBuilder.loadTexts:tmnxLdapServerEntry.setStatus(_B)
class _TmnxLdapServerIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_TmnxLdapServerIndex_Type.__name__=_E
_TmnxLdapServerIndex_Object=MibTableColumn
tmnxLdapServerIndex=_TmnxLdapServerIndex_Object((1,3,6,1,4,1,6527,3,1,2,106,2,1,1,1),_TmnxLdapServerIndex_Type())
tmnxLdapServerIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:tmnxLdapServerIndex.setStatus(_B)
_TmnxLdapServerLastChanged_Type=TimeStamp
_TmnxLdapServerLastChanged_Object=MibTableColumn
tmnxLdapServerLastChanged=_TmnxLdapServerLastChanged_Object((1,3,6,1,4,1,6527,3,1,2,106,2,1,1,2),_TmnxLdapServerLastChanged_Type())
tmnxLdapServerLastChanged.setMaxAccess(_F)
if mibBuilder.loadTexts:tmnxLdapServerLastChanged.setStatus(_B)
_TmnxLdapServerRowStatus_Type=RowStatus
_TmnxLdapServerRowStatus_Object=MibTableColumn
tmnxLdapServerRowStatus=_TmnxLdapServerRowStatus_Object((1,3,6,1,4,1,6527,3,1,2,106,2,1,1,3),_TmnxLdapServerRowStatus_Type())
tmnxLdapServerRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxLdapServerRowStatus.setStatus(_B)
class _TmnxLdapServerAdminState_Type(TmnxAdminState):defaultValue=3
_TmnxLdapServerAdminState_Type.__name__=_I
_TmnxLdapServerAdminState_Object=MibTableColumn
tmnxLdapServerAdminState=_TmnxLdapServerAdminState_Object((1,3,6,1,4,1,6527,3,1,2,106,2,1,1,4),_TmnxLdapServerAdminState_Type())
tmnxLdapServerAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxLdapServerAdminState.setStatus(_B)
_TmnxLdapServerOperState_Type=TmnxOperState
_TmnxLdapServerOperState_Object=MibTableColumn
tmnxLdapServerOperState=_TmnxLdapServerOperState_Object((1,3,6,1,4,1,6527,3,1,2,106,2,1,1,5),_TmnxLdapServerOperState_Type())
tmnxLdapServerOperState.setMaxAccess(_F)
if mibBuilder.loadTexts:tmnxLdapServerOperState.setStatus(_B)
class _TmnxLdapServerInetAddressType_Type(InetAddressType):defaultValue=0
_TmnxLdapServerInetAddressType_Type.__name__=_R
_TmnxLdapServerInetAddressType_Object=MibTableColumn
tmnxLdapServerInetAddressType=_TmnxLdapServerInetAddressType_Object((1,3,6,1,4,1,6527,3,1,2,106,2,1,1,6),_TmnxLdapServerInetAddressType_Type())
tmnxLdapServerInetAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxLdapServerInetAddressType.setStatus(_B)
class _TmnxLdapServerInetAddress_Type(InetAddress):defaultHexValue='';subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_TmnxLdapServerInetAddress_Type.__name__=_Q
_TmnxLdapServerInetAddress_Object=MibTableColumn
tmnxLdapServerInetAddress=_TmnxLdapServerInetAddress_Object((1,3,6,1,4,1,6527,3,1,2,106,2,1,1,7),_TmnxLdapServerInetAddress_Type())
tmnxLdapServerInetAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxLdapServerInetAddress.setStatus(_B)
class _TmnxLdapServerPort_Type(TTcpUdpPort):defaultValue=389;subtypeSpec=TTcpUdpPort.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_TmnxLdapServerPort_Type.__name__=_T
_TmnxLdapServerPort_Object=MibTableColumn
tmnxLdapServerPort=_TmnxLdapServerPort_Object((1,3,6,1,4,1,6527,3,1,2,106,2,1,1,8),_TmnxLdapServerPort_Type())
tmnxLdapServerPort.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxLdapServerPort.setStatus(_B)
class _TmnxLdapServerBindAuthRootDn_Type(TmnxLongDisplayString):defaultHexValue='';subtypeSpec=TmnxLongDisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_TmnxLdapServerBindAuthRootDn_Type.__name__=_J
_TmnxLdapServerBindAuthRootDn_Object=MibTableColumn
tmnxLdapServerBindAuthRootDn=_TmnxLdapServerBindAuthRootDn_Object((1,3,6,1,4,1,6527,3,1,2,106,2,1,1,9),_TmnxLdapServerBindAuthRootDn_Type())
tmnxLdapServerBindAuthRootDn.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxLdapServerBindAuthRootDn.setStatus(_B)
class _TmnxLdapServerBindAuthPassword_Type(DisplayString):defaultHexValue='';subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_TmnxLdapServerBindAuthPassword_Type.__name__=_S
_TmnxLdapServerBindAuthPassword_Object=MibTableColumn
tmnxLdapServerBindAuthPassword=_TmnxLdapServerBindAuthPassword_Object((1,3,6,1,4,1,6527,3,1,2,106,2,1,1,10),_TmnxLdapServerBindAuthPassword_Type())
tmnxLdapServerBindAuthPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxLdapServerBindAuthPassword.setStatus(_B)
class _TmnxLdapServerName_Type(TNamedItemOrEmpty):defaultHexValue=''
_TmnxLdapServerName_Type.__name__=_H
_TmnxLdapServerName_Object=MibTableColumn
tmnxLdapServerName=_TmnxLdapServerName_Object((1,3,6,1,4,1,6527,3,1,2,106,2,1,1,11),_TmnxLdapServerName_Type())
tmnxLdapServerName.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxLdapServerName.setStatus(_B)
class _TmnxLdapServerSearch_Type(TmnxLongDisplayString):defaultHexValue='';subtypeSpec=TmnxLongDisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_TmnxLdapServerSearch_Type.__name__=_J
_TmnxLdapServerSearch_Object=MibTableColumn
tmnxLdapServerSearch=_TmnxLdapServerSearch_Object((1,3,6,1,4,1,6527,3,1,2,106,2,1,1,12),_TmnxLdapServerSearch_Type())
tmnxLdapServerSearch.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxLdapServerSearch.setStatus(_B)
class _TmnxLdapServerTlsProfile_Type(TNamedItemOrEmpty):defaultHexValue=''
_TmnxLdapServerTlsProfile_Type.__name__=_H
_TmnxLdapServerTlsProfile_Object=MibTableColumn
tmnxLdapServerTlsProfile=_TmnxLdapServerTlsProfile_Object((1,3,6,1,4,1,6527,3,1,2,106,2,1,1,13),_TmnxLdapServerTlsProfile_Type())
tmnxLdapServerTlsProfile.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxLdapServerTlsProfile.setStatus(_B)
_TmnxLdapStatsObjs_ObjectIdentity=ObjectIdentity
tmnxLdapStatsObjs=_TmnxLdapStatsObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,106,3))
_TmnxLdapNotificationObjs_ObjectIdentity=ObjectIdentity
tmnxLdapNotificationObjs=_TmnxLdapNotificationObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,106,10))
_TmnxLdapNotifyPrefix_ObjectIdentity=ObjectIdentity
tmnxLdapNotifyPrefix=_TmnxLdapNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,6527,3,1,3,106))
_TmnxLdapNotifications_ObjectIdentity=ObjectIdentity
tmnxLdapNotifications=_TmnxLdapNotifications_ObjectIdentity((1,3,6,1,4,1,6527,3,1,3,106,0))
tmnxLdapInitialGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,106,2,1,1))
tmnxLdapInitialGroup.setObjects(*((_A,_V),(_A,_K),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_e),(_A,_f),(_A,_P),(_A,_g),(_A,_h)))
if mibBuilder.loadTexts:tmnxLdapInitialGroup.setStatus(_B)
tmnxLdapOperStateChange=NotificationType((1,3,6,1,4,1,6527,3,1,3,106,0,1))
tmnxLdapOperStateChange.setObjects((_A,_K))
if mibBuilder.loadTexts:tmnxLdapOperStateChange.setStatus(_B)
tmnxLdapServerOperStateChange=NotificationType((1,3,6,1,4,1,6527,3,1,3,106,0,2))
tmnxLdapServerOperStateChange.setObjects(*((_A,_P),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:tmnxLdapServerOperStateChange.setStatus(_B)
tmnxLdapNotifyGroup=NotificationGroup((1,3,6,1,4,1,6527,3,1,1,106,2,1,2))
tmnxLdapNotifyGroup.setObjects(*((_A,_i),(_A,_j)))
if mibBuilder.loadTexts:tmnxLdapNotifyGroup.setStatus(_B)
tmnxLdapCompliance=ModuleCompliance((1,3,6,1,4,1,6527,3,1,1,106,1,1))
tmnxLdapCompliance.setObjects(*((_A,_k),(_A,_l)))
if mibBuilder.loadTexts:tmnxLdapCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'timetraLdapMIBModule':timetraLdapMIBModule,'tmnxLdapConformance':tmnxLdapConformance,'tmnxLdapCompliances':tmnxLdapCompliances,'tmnxLdapCompliance':tmnxLdapCompliance,'tmnxLdapGroups':tmnxLdapGroups,'tmnxLdapInitialGroups':tmnxLdapInitialGroups,_k:tmnxLdapInitialGroup,_l:tmnxLdapNotifyGroup,'tmnxLdapObjs':tmnxLdapObjs,'tmnxLdapScalarObjs':tmnxLdapScalarObjs,'tmnxLdapScalarStatsObjs':tmnxLdapScalarStatsObjs,_a:tmnxLdapServerTableLastChanged,'tmnxLdapScalarConfigObjs':tmnxLdapScalarConfigObjs,_V:tmnxLdapAdminState,_K:tmnxLdapOperState,_W:tmnxLdapRetryAttempts,_X:tmnxLdapTimeout,_Y:tmnxLdapUseTemplate,_Z:tmnxLdapPublicKeyAuthentication,'tmnxLdapConfigObjs':tmnxLdapConfigObjs,'tmnxLdapServerTable':tmnxLdapServerTable,'tmnxLdapServerEntry':tmnxLdapServerEntry,_U:tmnxLdapServerIndex,_b:tmnxLdapServerLastChanged,_c:tmnxLdapServerRowStatus,_d:tmnxLdapServerAdminState,_L:tmnxLdapServerOperState,_M:tmnxLdapServerInetAddressType,_N:tmnxLdapServerInetAddress,_O:tmnxLdapServerPort,_e:tmnxLdapServerBindAuthRootDn,_f:tmnxLdapServerBindAuthPassword,_P:tmnxLdapServerName,_g:tmnxLdapServerSearch,_h:tmnxLdapServerTlsProfile,'tmnxLdapStatsObjs':tmnxLdapStatsObjs,'tmnxLdapNotificationObjs':tmnxLdapNotificationObjs,'tmnxLdapNotifyPrefix':tmnxLdapNotifyPrefix,'tmnxLdapNotifications':tmnxLdapNotifications,_i:tmnxLdapOperStateChange,_j:tmnxLdapServerOperStateChange})