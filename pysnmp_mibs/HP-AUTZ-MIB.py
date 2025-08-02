_AJ='hpSwitchAutzUserRoleGroup6'
_AI='hpSwitchAutzUserRoleGroup5'
_AH='hpSwitchAutzUserRoleGroup4'
_AG='hpSwitchAutzUserRoleGroup3'
_AF='hpSwitchAutzUserRoleGroup2'
_AE='hpSwitchAutzUserRoleGroup1'
_AD='hpSwitchAutzUserRoleGroup'
_AC='hpicfSwitchAuthorizationNotificationGroup'
_AB='hpicfSwitchAuthorizationObjectsGroup'
_AA='hpSwitchAuthorizationConfigGroup'
_A9='hpicfSwitchAuthServerFail'
_A8='hpSwitchAutzUserRolePortMode'
_A7='hpSwitchAutzUserRoleTaggedVlanList'
_A6='hpSwitchAutzUserRolePoeAllocBy'
_A5='hpSwitchAutzUserRoleCachedReauthPeriod'
_A4='hpSwitchAutzUserRolePoePriority'
_A3='hpSwitchAutzUserRoleAdminEdgePort'
_A2='hpSwitchAutzUserRoleSubTypeRowStatus'
_A1='hpSwitchLocalMgmtPrivGroupStatus'
_A0='hpSwitchLocalMgmtPrivCmdStatus'
_z='hpSwitchLocalMgmtPrivCmdSendLog'
_y='hpSwitchLocalMgmtPrivCmdPriv'
_x='hpSwitchLocalMgmtPrivCmdMatchStr'
_w='hpSwitchLocalMgmtPrivGroupName'
_v='hpicfSwitchAuthServerNotifyEnable'
_u='hpSwitchAutzServiceCommandsLevel'
_t='hpSwitchAutzServiceSecondaryMethod'
_s='hpSwitchAutzServicePrimaryMethod'
_r='hpSwitchAutzUserRoleSubType'
_q='disable'
_p='enable'
_o='hpSwitchLocalMgmtPrivCmdSequenceIndex'
_n='radius'
_m='tacacs'
_l='hpSwitchAutzServiceType'
_k='Unsigned32'
_j='hpSwitchAutzLocalMgmtPrivGroup1'
_i='hpSwitchAutzLocalMgmtPrivGroup'
_h='hpSwitchAutzUserRoleLogOffPeriod'
_g='hpicfSwitchAuthServerIP'
_f='hpicfSwitchAuthServerIPType'
_e='hpicfSwitchAuthServerType'
_d='seconds'
_c='hpSwitchAutzUserRoleName'
_b='hpSwitchLocalMgmtPrivGroupIndex'
_a='accessible-for-notify'
_Z='local'
_Y='SnmpAdminString'
_X='hpSwitchAutzUserRoleTunneledNodeServerDownloadableRole'
_W='hpSwitchAutzUserRoleDownloadedEnabled'
_V='hpSwitchAutzUserRoleTaggedVlanId'
_U='not-accessible'
_T='TruthValue'
_S='hpSwitchAutzUserRoleTaggedVlanName'
_R='OctetString'
_Q='hpSwitchAutzUserRoleTunneledNodeServerSecondaryRole'
_P='hpSwitchAutzUserRoleTunneledNodeServerRedirect'
_O='read-write'
_N='hpSwitchAutzUserRoleVlanName'
_M='hpSwitchAutzUserRoleVlanId'
_L='hpSwitchAutzUserRoleReauthPeriod'
_K='hpSwitchAutzUserRoleIngressUserPolicyName'
_J='hpSwitchAutzUserRoleCaptivePortalProfileName'
_I='hpSwitchAutzUserRoleType'
_H='hpSwitchAutzUserRoleRowStatus'
_G='hpSwitchAutzUserRoleInitialRoleName'
_F='hpSwitchAutzUserRoleEnabled'
_E='deprecated'
_D='Integer32'
_C='read-create'
_B='current'
_A='HP-AUTZ-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_R,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
VidList,=mibBuilder.importSymbols('HP-ICF-TC','VidList')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
VlanIndex,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanIndex')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_Y)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_k,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_T)
hpSwitchAuthorizationMIB=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,32))
if mibBuilder.loadTexts:hpSwitchAuthorizationMIB.setRevisions(('2018-08-20 00:00','2018-03-19 00:00','2017-07-16 00:00','2017-03-16 00:00','2016-10-20 00:00','2016-05-09 00:00','2016-01-07 00:00','2014-08-04 00:00','2011-02-07 00:00','2007-08-29 00:00','2005-10-05 00:00'))
class HpAutzUserRoleName(TextualConvention,OctetString):status=_B;displayHint='63a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,63))
_HpicfSwitchAuthorizationNotifications_ObjectIdentity=ObjectIdentity
hpicfSwitchAuthorizationNotifications=_HpicfSwitchAuthorizationNotifications_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,32,0))
_HpSwitchAuthorizationConfig_ObjectIdentity=ObjectIdentity
hpSwitchAuthorizationConfig=_HpSwitchAuthorizationConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,32,1))
_HpSwitchAutzServiceTable_Object=MibTable
hpSwitchAutzServiceTable=_HpSwitchAutzServiceTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,32,1,1))
if mibBuilder.loadTexts:hpSwitchAutzServiceTable.setStatus(_B)
_HpSwitchAutzServiceEntry_Object=MibTableRow
hpSwitchAutzServiceEntry=_HpSwitchAutzServiceEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,32,1,1,1))
hpSwitchAutzServiceEntry.setIndexNames((0,_A,_l))
if mibBuilder.loadTexts:hpSwitchAutzServiceEntry.setStatus(_B)
class _HpSwitchAutzServiceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('commands',1),('exec',2),('network',3),('restUri',4)))
_HpSwitchAutzServiceType_Type.__name__=_D
_HpSwitchAutzServiceType_Object=MibTableColumn
hpSwitchAutzServiceType=_HpSwitchAutzServiceType_Object((1,3,6,1,4,1,11,2,14,11,5,1,32,1,1,1,1),_HpSwitchAutzServiceType_Type())
hpSwitchAutzServiceType.setMaxAccess(_U)
if mibBuilder.loadTexts:hpSwitchAutzServiceType.setStatus(_B)
class _HpSwitchAutzServicePrimaryMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_Z,1),(_m,2),(_n,3),('none',4),('auto',5)))
_HpSwitchAutzServicePrimaryMethod_Type.__name__=_D
_HpSwitchAutzServicePrimaryMethod_Object=MibTableColumn
hpSwitchAutzServicePrimaryMethod=_HpSwitchAutzServicePrimaryMethod_Object((1,3,6,1,4,1,11,2,14,11,5,1,32,1,1,1,2),_HpSwitchAutzServicePrimaryMethod_Type())
hpSwitchAutzServicePrimaryMethod.setMaxAccess(_O)
if mibBuilder.loadTexts:hpSwitchAutzServicePrimaryMethod.setStatus(_B)
class _HpSwitchAutzServiceSecondaryMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Z,1),('none',2)))
_HpSwitchAutzServiceSecondaryMethod_Type.__name__=_D
_HpSwitchAutzServiceSecondaryMethod_Object=MibTableColumn
hpSwitchAutzServiceSecondaryMethod=_HpSwitchAutzServiceSecondaryMethod_Object((1,3,6,1,4,1,11,2,14,11,5,1,32,1,1,1,3),_HpSwitchAutzServiceSecondaryMethod_Type())
hpSwitchAutzServiceSecondaryMethod.setMaxAccess(_O)
if mibBuilder.loadTexts:hpSwitchAutzServiceSecondaryMethod.setStatus(_B)
class _HpSwitchAutzServiceCommandsLevel_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('all',1),('managerlevelonly',2)))
_HpSwitchAutzServiceCommandsLevel_Type.__name__=_D
_HpSwitchAutzServiceCommandsLevel_Object=MibTableColumn
hpSwitchAutzServiceCommandsLevel=_HpSwitchAutzServiceCommandsLevel_Object((1,3,6,1,4,1,11,2,14,11,5,1,32,1,1,1,4),_HpSwitchAutzServiceCommandsLevel_Type())
hpSwitchAutzServiceCommandsLevel.setMaxAccess(_O)
if mibBuilder.loadTexts:hpSwitchAutzServiceCommandsLevel.setStatus(_B)
_HpicfSwitchAuthObjects_ObjectIdentity=ObjectIdentity
hpicfSwitchAuthObjects=_HpicfSwitchAuthObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,32,1,2))
class _HpicfSwitchAuthServerType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,9)));namedValues=NamedValues(*((_n,1),(_m,2),('other',9)))
_HpicfSwitchAuthServerType_Type.__name__=_D
_HpicfSwitchAuthServerType_Object=MibScalar
hpicfSwitchAuthServerType=_HpicfSwitchAuthServerType_Object((1,3,6,1,4,1,11,2,14,11,5,1,32,1,2,1),_HpicfSwitchAuthServerType_Type())
hpicfSwitchAuthServerType.setMaxAccess(_a)
if mibBuilder.loadTexts:hpicfSwitchAuthServerType.setStatus(_B)
_HpicfSwitchAuthServerIPType_Type=InetAddressType
_HpicfSwitchAuthServerIPType_Object=MibScalar
hpicfSwitchAuthServerIPType=_HpicfSwitchAuthServerIPType_Object((1,3,6,1,4,1,11,2,14,11,5,1,32,1,2,2),_HpicfSwitchAuthServerIPType_Type())
hpicfSwitchAuthServerIPType.setMaxAccess(_a)
if mibBuilder.loadTexts:hpicfSwitchAuthServerIPType.setStatus(_B)
_HpicfSwitchAuthServerIP_Type=InetAddress
_HpicfSwitchAuthServerIP_Object=MibScalar
hpicfSwitchAuthServerIP=_HpicfSwitchAuthServerIP_Object((1,3,6,1,4,1,11,2,14,11,5,1,32,1,2,3),_HpicfSwitchAuthServerIP_Type())
hpicfSwitchAuthServerIP.setMaxAccess(_a)
if mibBuilder.loadTexts:hpicfSwitchAuthServerIP.setStatus(_B)
_HpSwitchAuthConfigObjects_ObjectIdentity=ObjectIdentity
hpSwitchAuthConfigObjects=_HpSwitchAuthConfigObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,32,1,3))
class _HpicfSwitchAuthServerNotifyEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_HpicfSwitchAuthServerNotifyEnable_Type.__name__=_D
_HpicfSwitchAuthServerNotifyEnable_Object=MibScalar
hpicfSwitchAuthServerNotifyEnable=_HpicfSwitchAuthServerNotifyEnable_Object((1,3,6,1,4,1,11,2,14,11,5,1,32,1,3,1),_HpicfSwitchAuthServerNotifyEnable_Type())
hpicfSwitchAuthServerNotifyEnable.setMaxAccess(_O)
if mibBuilder.loadTexts:hpicfSwitchAuthServerNotifyEnable.setStatus(_B)
_HpSwitchAuthLocalPrivConfigObjects_ObjectIdentity=ObjectIdentity
hpSwitchAuthLocalPrivConfigObjects=_HpSwitchAuthLocalPrivConfigObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,32,1,4))
_HpSwitchLocalMgmtPrivGroupsTable_Object=MibTable
hpSwitchLocalMgmtPrivGroupsTable=_HpSwitchLocalMgmtPrivGroupsTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,32,1,4,1))
if mibBuilder.loadTexts:hpSwitchLocalMgmtPrivGroupsTable.setStatus(_B)
_HpSwitchLocalMgmtPrivGroupsEntry_Object=MibTableRow
hpSwitchLocalMgmtPrivGroupsEntry=_HpSwitchLocalMgmtPrivGroupsEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,32,1,4,1,1))
hpSwitchLocalMgmtPrivGroupsEntry.setIndexNames((0,_A,_b))
if mibBuilder.loadTexts:hpSwitchLocalMgmtPrivGroupsEntry.setStatus(_B)
class _HpSwitchLocalMgmtPrivGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpSwitchLocalMgmtPrivGroupIndex_Type.__name__=_D
_HpSwitchLocalMgmtPrivGroupIndex_Object=MibTableColumn
hpSwitchLocalMgmtPrivGroupIndex=_HpSwitchLocalMgmtPrivGroupIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,32,1,4,1,1,1),_HpSwitchLocalMgmtPrivGroupIndex_Type())
hpSwitchLocalMgmtPrivGroupIndex.setMaxAccess(_U)
if mibBuilder.loadTexts:hpSwitchLocalMgmtPrivGroupIndex.setStatus(_B)
class _HpSwitchLocalMgmtPrivGroupName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_HpSwitchLocalMgmtPrivGroupName_Type.__name__=_R
_HpSwitchLocalMgmtPrivGroupName_Object=MibTableColumn
hpSwitchLocalMgmtPrivGroupName=_HpSwitchLocalMgmtPrivGroupName_Object((1,3,6,1,4,1,11,2,14,11,5,1,32,1,4,1,1,2),_HpSwitchLocalMgmtPrivGroupName_Type())
hpSwitchLocalMgmtPrivGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchLocalMgmtPrivGroupName.setStatus(_B)
_HpSwitchLocalMgmtPrivGroupStatus_Type=RowStatus
_HpSwitchLocalMgmtPrivGroupStatus_Object=MibTableColumn
hpSwitchLocalMgmtPrivGroupStatus=_HpSwitchLocalMgmtPrivGroupStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,32,1,4,1,1,3),_HpSwitchLocalMgmtPrivGroupStatus_Type())
hpSwitchLocalMgmtPrivGroupStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchLocalMgmtPrivGroupStatus.setStatus(_B)
_HpSwitchLocalMgmtPrivCommandsTable_Object=MibTable
hpSwitchLocalMgmtPrivCommandsTable=_HpSwitchLocalMgmtPrivCommandsTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,32,1,4,2))
if mibBuilder.loadTexts:hpSwitchLocalMgmtPrivCommandsTable.setStatus(_B)
_HpSwitchLocalMgmtPrivCommandsEntry_Object=MibTableRow
hpSwitchLocalMgmtPrivCommandsEntry=_HpSwitchLocalMgmtPrivCommandsEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,32,1,4,2,1))
hpSwitchLocalMgmtPrivCommandsEntry.setIndexNames((0,_A,_b),(0,_A,_o))
if mibBuilder.loadTexts:hpSwitchLocalMgmtPrivCommandsEntry.setStatus(_B)
class _HpSwitchLocalMgmtPrivCmdSequenceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpSwitchLocalMgmtPrivCmdSequenceIndex_Type.__name__=_D
_HpSwitchLocalMgmtPrivCmdSequenceIndex_Object=MibTableColumn
hpSwitchLocalMgmtPrivCmdSequenceIndex=_HpSwitchLocalMgmtPrivCmdSequenceIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,32,1,4,2,1,1),_HpSwitchLocalMgmtPrivCmdSequenceIndex_Type())
hpSwitchLocalMgmtPrivCmdSequenceIndex.setMaxAccess(_U)
if mibBuilder.loadTexts:hpSwitchLocalMgmtPrivCmdSequenceIndex.setStatus(_B)
class _HpSwitchLocalMgmtPrivCmdMatchStr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,65535))
_HpSwitchLocalMgmtPrivCmdMatchStr_Type.__name__=_R
_HpSwitchLocalMgmtPrivCmdMatchStr_Object=MibTableColumn
hpSwitchLocalMgmtPrivCmdMatchStr=_HpSwitchLocalMgmtPrivCmdMatchStr_Object((1,3,6,1,4,1,11,2,14,11,5,1,32,1,4,2,1,2),_HpSwitchLocalMgmtPrivCmdMatchStr_Type())
hpSwitchLocalMgmtPrivCmdMatchStr.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchLocalMgmtPrivCmdMatchStr.setStatus(_B)
class _HpSwitchLocalMgmtPrivCmdPriv_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('permit',1),('deny',2)))
_HpSwitchLocalMgmtPrivCmdPriv_Type.__name__=_D
_HpSwitchLocalMgmtPrivCmdPriv_Object=MibTableColumn
hpSwitchLocalMgmtPrivCmdPriv=_HpSwitchLocalMgmtPrivCmdPriv_Object((1,3,6,1,4,1,11,2,14,11,5,1,32,1,4,2,1,3),_HpSwitchLocalMgmtPrivCmdPriv_Type())
hpSwitchLocalMgmtPrivCmdPriv.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchLocalMgmtPrivCmdPriv.setStatus(_B)
class _HpSwitchLocalMgmtPrivCmdSendLog_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_p,1),(_q,2)))
_HpSwitchLocalMgmtPrivCmdSendLog_Type.__name__=_D
_HpSwitchLocalMgmtPrivCmdSendLog_Object=MibTableColumn
hpSwitchLocalMgmtPrivCmdSendLog=_HpSwitchLocalMgmtPrivCmdSendLog_Object((1,3,6,1,4,1,11,2,14,11,5,1,32,1,4,2,1,4),_HpSwitchLocalMgmtPrivCmdSendLog_Type())
hpSwitchLocalMgmtPrivCmdSendLog.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchLocalMgmtPrivCmdSendLog.setStatus(_B)
_HpSwitchLocalMgmtPrivCmdStatus_Type=RowStatus
_HpSwitchLocalMgmtPrivCmdStatus_Object=MibTableColumn
hpSwitchLocalMgmtPrivCmdStatus=_HpSwitchLocalMgmtPrivCmdStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,32,1,4,2,1,5),_HpSwitchLocalMgmtPrivCmdStatus_Type())
hpSwitchLocalMgmtPrivCmdStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchLocalMgmtPrivCmdStatus.setStatus(_B)
_HpSwitchAutzUserRole_ObjectIdentity=ObjectIdentity
hpSwitchAutzUserRole=_HpSwitchAutzUserRole_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,32,1,5))
class _HpSwitchAutzUserRoleEnabled_Type(TruthValue):defaultValue=2
_HpSwitchAutzUserRoleEnabled_Type.__name__=_T
_HpSwitchAutzUserRoleEnabled_Object=MibScalar
hpSwitchAutzUserRoleEnabled=_HpSwitchAutzUserRoleEnabled_Object((1,3,6,1,4,1,11,2,14,11,5,1,32,1,5,1),_HpSwitchAutzUserRoleEnabled_Type())
hpSwitchAutzUserRoleEnabled.setMaxAccess(_O)
if mibBuilder.loadTexts:hpSwitchAutzUserRoleEnabled.setStatus(_B)
_HpSwitchAutzUserRoleInitialRoleName_Type=HpAutzUserRoleName
_HpSwitchAutzUserRoleInitialRoleName_Object=MibScalar
hpSwitchAutzUserRoleInitialRoleName=_HpSwitchAutzUserRoleInitialRoleName_Object((1,3,6,1,4,1,11,2,14,11,5,1,32,1,5,2),_HpSwitchAutzUserRoleInitialRoleName_Type())
hpSwitchAutzUserRoleInitialRoleName.setMaxAccess(_O)
if mibBuilder.loadTexts:hpSwitchAutzUserRoleInitialRoleName.setStatus(_B)
_HpSwitchAutzUserRoleTable_Object=MibTable
hpSwitchAutzUserRoleTable=_HpSwitchAutzUserRoleTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,32,1,5,3))
if mibBuilder.loadTexts:hpSwitchAutzUserRoleTable.setStatus(_B)
_HpSwitchAutzUserRoleEntry_Object=MibTableRow
hpSwitchAutzUserRoleEntry=_HpSwitchAutzUserRoleEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,32,1,5,3,1))
hpSwitchAutzUserRoleEntry.setIndexNames((0,_A,_c))
if mibBuilder.loadTexts:hpSwitchAutzUserRoleEntry.setStatus(_B)
_HpSwitchAutzUserRoleName_Type=HpAutzUserRoleName
_HpSwitchAutzUserRoleName_Object=MibTableColumn
hpSwitchAutzUserRoleName=_HpSwitchAutzUserRoleName_Object((1,3,6,1,4,1,11,2,14,11,5,1,32,1,5,3,1,1),_HpSwitchAutzUserRoleName_Type())
hpSwitchAutzUserRoleName.setMaxAccess(_U)
if mibBuilder.loadTexts:hpSwitchAutzUserRoleName.setStatus(_B)
_HpSwitchAutzUserRoleRowStatus_Type=RowStatus
_HpSwitchAutzUserRoleRowStatus_Object=MibTableColumn
hpSwitchAutzUserRoleRowStatus=_HpSwitchAutzUserRoleRowStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,32,1,5,3,1,2),_HpSwitchAutzUserRoleRowStatus_Type())
hpSwitchAutzUserRoleRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchAutzUserRoleRowStatus.setStatus(_B)
class _HpSwitchAutzUserRoleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('predefined',1),(_Z,2),('downloaded',3)))
_HpSwitchAutzUserRoleType_Type.__name__=_D
_HpSwitchAutzUserRoleType_Object=MibTableColumn
hpSwitchAutzUserRoleType=_HpSwitchAutzUserRoleType_Object((1,3,6,1,4,1,11,2,14,11,5,1,32,1,5,3,1,3),_HpSwitchAutzUserRoleType_Type())
hpSwitchAutzUserRoleType.setMaxAccess('read-only')
if mibBuilder.loadTexts:hpSwitchAutzUserRoleType.setStatus(_B)
class _HpSwitchAutzUserRoleCaptivePortalProfileName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_HpSwitchAutzUserRoleCaptivePortalProfileName_Type.__name__=_R
_HpSwitchAutzUserRoleCaptivePortalProfileName_Object=MibTableColumn
hpSwitchAutzUserRoleCaptivePortalProfileName=_HpSwitchAutzUserRoleCaptivePortalProfileName_Object((1,3,6,1,4,1,11,2,14,11,5,1,32,1,5,3,1,4),_HpSwitchAutzUserRoleCaptivePortalProfileName_Type())
hpSwitchAutzUserRoleCaptivePortalProfileName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchAutzUserRoleCaptivePortalProfileName.setStatus(_B)
class _HpSwitchAutzUserRoleIngressUserPolicyName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HpSwitchAutzUserRoleIngressUserPolicyName_Type.__name__=_R
_HpSwitchAutzUserRoleIngressUserPolicyName_Object=MibTableColumn
hpSwitchAutzUserRoleIngressUserPolicyName=_HpSwitchAutzUserRoleIngressUserPolicyName_Object((1,3,6,1,4,1,11,2,14,11,5,1,32,1,5,3,1,5),_HpSwitchAutzUserRoleIngressUserPolicyName_Type())
hpSwitchAutzUserRoleIngressUserPolicyName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchAutzUserRoleIngressUserPolicyName.setStatus(_B)
class _HpSwitchAutzUserRoleReauthPeriod_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999999999))
_HpSwitchAutzUserRoleReauthPeriod_Type.__name__=_D
_HpSwitchAutzUserRoleReauthPeriod_Object=MibTableColumn
hpSwitchAutzUserRoleReauthPeriod=_HpSwitchAutzUserRoleReauthPeriod_Object((1,3,6,1,4,1,11,2,14,11,5,1,32,1,5,3,1,6),_HpSwitchAutzUserRoleReauthPeriod_Type())
hpSwitchAutzUserRoleReauthPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchAutzUserRoleReauthPeriod.setStatus(_B)
if mibBuilder.loadTexts:hpSwitchAutzUserRoleReauthPeriod.setUnits(_d)
_HpSwitchAutzUserRoleVlanId_Type=VlanIndex
_HpSwitchAutzUserRoleVlanId_Object=MibTableColumn
hpSwitchAutzUserRoleVlanId=_HpSwitchAutzUserRoleVlanId_Object((1,3,6,1,4,1,11,2,14,11,5,1,32,1,5,3,1,7),_HpSwitchAutzUserRoleVlanId_Type())
hpSwitchAutzUserRoleVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchAutzUserRoleVlanId.setStatus(_B)
class _HpSwitchAutzUserRoleVlanName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HpSwitchAutzUserRoleVlanName_Type.__name__=_Y
_HpSwitchAutzUserRoleVlanName_Object=MibTableColumn
hpSwitchAutzUserRoleVlanName=_HpSwitchAutzUserRoleVlanName_Object((1,3,6,1,4,1,11,2,14,11,5,1,32,1,5,3,1,8),_HpSwitchAutzUserRoleVlanName_Type())
hpSwitchAutzUserRoleVlanName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchAutzUserRoleVlanName.setStatus(_B)
class _HpSwitchAutzUserRoleTunneledNodeServerRedirect_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_p,1),(_q,2)))
_HpSwitchAutzUserRoleTunneledNodeServerRedirect_Type.__name__=_D
_HpSwitchAutzUserRoleTunneledNodeServerRedirect_Object=MibTableColumn
hpSwitchAutzUserRoleTunneledNodeServerRedirect=_HpSwitchAutzUserRoleTunneledNodeServerRedirect_Object((1,3,6,1,4,1,11,2,14,11,5,1,32,1,5,3,1,9),_HpSwitchAutzUserRoleTunneledNodeServerRedirect_Type())
hpSwitchAutzUserRoleTunneledNodeServerRedirect.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchAutzUserRoleTunneledNodeServerRedirect.setStatus(_B)
class _HpSwitchAutzUserRoleTunneledNodeServerSecondaryRole_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_HpSwitchAutzUserRoleTunneledNodeServerSecondaryRole_Type.__name__=_R
_HpSwitchAutzUserRoleTunneledNodeServerSecondaryRole_Object=MibTableColumn
hpSwitchAutzUserRoleTunneledNodeServerSecondaryRole=_HpSwitchAutzUserRoleTunneledNodeServerSecondaryRole_Object((1,3,6,1,4,1,11,2,14,11,5,1,32,1,5,3,1,10),_HpSwitchAutzUserRoleTunneledNodeServerSecondaryRole_Type())
hpSwitchAutzUserRoleTunneledNodeServerSecondaryRole.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchAutzUserRoleTunneledNodeServerSecondaryRole.setStatus(_B)
_HpSwitchAutzUserRoleTaggedVlanId_Type=VlanIndex
_HpSwitchAutzUserRoleTaggedVlanId_Object=MibTableColumn
hpSwitchAutzUserRoleTaggedVlanId=_HpSwitchAutzUserRoleTaggedVlanId_Object((1,3,6,1,4,1,11,2,14,11,5,1,32,1,5,3,1,11),_HpSwitchAutzUserRoleTaggedVlanId_Type())
hpSwitchAutzUserRoleTaggedVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchAutzUserRoleTaggedVlanId.setStatus(_E)
class _HpSwitchAutzUserRoleTaggedVlanName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HpSwitchAutzUserRoleTaggedVlanName_Type.__name__=_Y
_HpSwitchAutzUserRoleTaggedVlanName_Object=MibTableColumn
hpSwitchAutzUserRoleTaggedVlanName=_HpSwitchAutzUserRoleTaggedVlanName_Object((1,3,6,1,4,1,11,2,14,11,5,1,32,1,5,3,1,12),_HpSwitchAutzUserRoleTaggedVlanName_Type())
hpSwitchAutzUserRoleTaggedVlanName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchAutzUserRoleTaggedVlanName.setStatus(_B)
_HpSwitchAutzUserRoleTunneledNodeServerDownloadableRole_Type=TruthValue
_HpSwitchAutzUserRoleTunneledNodeServerDownloadableRole_Object=MibTableColumn
hpSwitchAutzUserRoleTunneledNodeServerDownloadableRole=_HpSwitchAutzUserRoleTunneledNodeServerDownloadableRole_Object((1,3,6,1,4,1,11,2,14,11,5,1,32,1,5,3,1,13),_HpSwitchAutzUserRoleTunneledNodeServerDownloadableRole_Type())
hpSwitchAutzUserRoleTunneledNodeServerDownloadableRole.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchAutzUserRoleTunneledNodeServerDownloadableRole.setStatus(_B)
class _HpSwitchAutzUserRoleLogOffPeriod_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(60,9999999))
_HpSwitchAutzUserRoleLogOffPeriod_Type.__name__=_D
_HpSwitchAutzUserRoleLogOffPeriod_Object=MibTableColumn
hpSwitchAutzUserRoleLogOffPeriod=_HpSwitchAutzUserRoleLogOffPeriod_Object((1,3,6,1,4,1,11,2,14,11,5,1,32,1,5,3,1,14),_HpSwitchAutzUserRoleLogOffPeriod_Type())
hpSwitchAutzUserRoleLogOffPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchAutzUserRoleLogOffPeriod.setStatus(_B)
if mibBuilder.loadTexts:hpSwitchAutzUserRoleLogOffPeriod.setUnits(_d)
class _HpSwitchAutzUserRoleCachedReauthPeriod_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(60,2147483647))
_HpSwitchAutzUserRoleCachedReauthPeriod_Type.__name__=_k
_HpSwitchAutzUserRoleCachedReauthPeriod_Object=MibTableColumn
hpSwitchAutzUserRoleCachedReauthPeriod=_HpSwitchAutzUserRoleCachedReauthPeriod_Object((1,3,6,1,4,1,11,2,14,11,5,1,32,1,5,3,1,15),_HpSwitchAutzUserRoleCachedReauthPeriod_Type())
hpSwitchAutzUserRoleCachedReauthPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchAutzUserRoleCachedReauthPeriod.setStatus(_B)
if mibBuilder.loadTexts:hpSwitchAutzUserRoleCachedReauthPeriod.setUnits(_d)
_HpSwitchAutzUserRoleTaggedVlanList_Type=VidList
_HpSwitchAutzUserRoleTaggedVlanList_Object=MibTableColumn
hpSwitchAutzUserRoleTaggedVlanList=_HpSwitchAutzUserRoleTaggedVlanList_Object((1,3,6,1,4,1,11,2,14,11,5,1,32,1,5,3,1,16),_HpSwitchAutzUserRoleTaggedVlanList_Type())
hpSwitchAutzUserRoleTaggedVlanList.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchAutzUserRoleTaggedVlanList.setStatus(_B)
class _HpSwitchAutzUserRoleDownloadedEnabled_Type(TruthValue):defaultValue=2
_HpSwitchAutzUserRoleDownloadedEnabled_Type.__name__=_T
_HpSwitchAutzUserRoleDownloadedEnabled_Object=MibScalar
hpSwitchAutzUserRoleDownloadedEnabled=_HpSwitchAutzUserRoleDownloadedEnabled_Object((1,3,6,1,4,1,11,2,14,11,5,1,32,1,5,4),_HpSwitchAutzUserRoleDownloadedEnabled_Type())
hpSwitchAutzUserRoleDownloadedEnabled.setMaxAccess(_O)
if mibBuilder.loadTexts:hpSwitchAutzUserRoleDownloadedEnabled.setStatus(_B)
_HpSwitchAutzUserRoleSubTable_Object=MibTable
hpSwitchAutzUserRoleSubTable=_HpSwitchAutzUserRoleSubTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,32,1,5,5))
if mibBuilder.loadTexts:hpSwitchAutzUserRoleSubTable.setStatus(_B)
_HpSwitchAutzUserRoleSubEntry_Object=MibTableRow
hpSwitchAutzUserRoleSubEntry=_HpSwitchAutzUserRoleSubEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,32,1,5,5,1))
hpSwitchAutzUserRoleSubEntry.setIndexNames((0,_A,_c),(0,_A,_r))
if mibBuilder.loadTexts:hpSwitchAutzUserRoleSubEntry.setStatus(_B)
class _HpSwitchAutzUserRoleSubType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('device',1))
_HpSwitchAutzUserRoleSubType_Type.__name__=_D
_HpSwitchAutzUserRoleSubType_Object=MibTableColumn
hpSwitchAutzUserRoleSubType=_HpSwitchAutzUserRoleSubType_Object((1,3,6,1,4,1,11,2,14,11,5,1,32,1,5,5,1,1),_HpSwitchAutzUserRoleSubType_Type())
hpSwitchAutzUserRoleSubType.setMaxAccess(_U)
if mibBuilder.loadTexts:hpSwitchAutzUserRoleSubType.setStatus(_B)
class _HpSwitchAutzUserRoleAdminEdgePort_Type(TruthValue):defaultValue=2
_HpSwitchAutzUserRoleAdminEdgePort_Type.__name__=_T
_HpSwitchAutzUserRoleAdminEdgePort_Object=MibTableColumn
hpSwitchAutzUserRoleAdminEdgePort=_HpSwitchAutzUserRoleAdminEdgePort_Object((1,3,6,1,4,1,11,2,14,11,5,1,32,1,5,5,1,2),_HpSwitchAutzUserRoleAdminEdgePort_Type())
hpSwitchAutzUserRoleAdminEdgePort.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchAutzUserRoleAdminEdgePort.setStatus(_B)
class _HpSwitchAutzUserRolePoePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('default',0),('critical',1),('high',2),('low',3)))
_HpSwitchAutzUserRolePoePriority_Type.__name__=_D
_HpSwitchAutzUserRolePoePriority_Object=MibTableColumn
hpSwitchAutzUserRolePoePriority=_HpSwitchAutzUserRolePoePriority_Object((1,3,6,1,4,1,11,2,14,11,5,1,32,1,5,5,1,3),_HpSwitchAutzUserRolePoePriority_Type())
hpSwitchAutzUserRolePoePriority.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchAutzUserRolePoePriority.setStatus(_B)
class _HpSwitchAutzUserRolePoeAllocBy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('usage',1),('class',2)))
_HpSwitchAutzUserRolePoeAllocBy_Type.__name__=_D
_HpSwitchAutzUserRolePoeAllocBy_Object=MibTableColumn
hpSwitchAutzUserRolePoeAllocBy=_HpSwitchAutzUserRolePoeAllocBy_Object((1,3,6,1,4,1,11,2,14,11,5,1,32,1,5,5,1,4),_HpSwitchAutzUserRolePoeAllocBy_Type())
hpSwitchAutzUserRolePoeAllocBy.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchAutzUserRolePoeAllocBy.setStatus(_B)
_HpSwitchAutzUserRoleSubTypeRowStatus_Type=RowStatus
_HpSwitchAutzUserRoleSubTypeRowStatus_Object=MibTableColumn
hpSwitchAutzUserRoleSubTypeRowStatus=_HpSwitchAutzUserRoleSubTypeRowStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,32,1,5,5,1,5),_HpSwitchAutzUserRoleSubTypeRowStatus_Type())
hpSwitchAutzUserRoleSubTypeRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchAutzUserRoleSubTypeRowStatus.setStatus(_B)
class _HpSwitchAutzUserRolePortMode_Type(TruthValue):defaultValue=2
_HpSwitchAutzUserRolePortMode_Type.__name__=_T
_HpSwitchAutzUserRolePortMode_Object=MibTableColumn
hpSwitchAutzUserRolePortMode=_HpSwitchAutzUserRolePortMode_Object((1,3,6,1,4,1,11,2,14,11,5,1,32,1,5,5,1,7),_HpSwitchAutzUserRolePortMode_Type())
hpSwitchAutzUserRolePortMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchAutzUserRolePortMode.setStatus(_B)
_HpSwitchAuthorizationConformance_ObjectIdentity=ObjectIdentity
hpSwitchAuthorizationConformance=_HpSwitchAuthorizationConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,32,2))
_HpSwitchAuthorizationMIBCompliances_ObjectIdentity=ObjectIdentity
hpSwitchAuthorizationMIBCompliances=_HpSwitchAuthorizationMIBCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,32,2,1))
_HpSwitchAuthorizationMIBGroups_ObjectIdentity=ObjectIdentity
hpSwitchAuthorizationMIBGroups=_HpSwitchAuthorizationMIBGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,32,2,2))
hpSwitchAuthorizationConfigGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,32,2,2,1))
hpSwitchAuthorizationConfigGroup.setObjects(*((_A,_s),(_A,_t),(_A,_u),(_A,_v)))
if mibBuilder.loadTexts:hpSwitchAuthorizationConfigGroup.setStatus(_B)
hpicfSwitchAuthorizationObjectsGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,32,2,2,3))
hpicfSwitchAuthorizationObjectsGroup.setObjects(*((_A,_e),(_A,_f),(_A,_g)))
if mibBuilder.loadTexts:hpicfSwitchAuthorizationObjectsGroup.setStatus(_B)
hpSwitchAutzLocalMgmtPrivGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,32,2,2,4))
hpSwitchAutzLocalMgmtPrivGroup.setObjects(*((_A,_w),(_A,_x),(_A,_y),(_A,_z)))
if mibBuilder.loadTexts:hpSwitchAutzLocalMgmtPrivGroup.setStatus(_B)
hpSwitchAutzLocalMgmtPrivGroup1=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,32,2,2,5))
hpSwitchAutzLocalMgmtPrivGroup1.setObjects(*((_A,_A0),(_A,_A1)))
if mibBuilder.loadTexts:hpSwitchAutzLocalMgmtPrivGroup1.setStatus(_B)
hpSwitchAutzUserRoleGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,32,2,2,6))
hpSwitchAutzUserRoleGroup.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:hpSwitchAutzUserRoleGroup.setStatus(_E)
hpSwitchAutzUserRoleGroup1=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,32,2,2,7))
hpSwitchAutzUserRoleGroup1.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_P),(_A,_Q)))
if mibBuilder.loadTexts:hpSwitchAutzUserRoleGroup1.setStatus(_E)
hpSwitchAutzUserRoleGroup2=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,32,2,2,8))
hpSwitchAutzUserRoleGroup2.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_P),(_A,_Q),(_A,_V),(_A,_S)))
if mibBuilder.loadTexts:hpSwitchAutzUserRoleGroup2.setStatus(_E)
hpSwitchAutzUserRoleGroup3=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,32,2,2,9))
hpSwitchAutzUserRoleGroup3.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_P),(_A,_Q),(_A,_V),(_A,_S),(_A,_W)))
if mibBuilder.loadTexts:hpSwitchAutzUserRoleGroup3.setStatus(_E)
hpSwitchAutzUserRoleGroup4=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,32,2,2,10))
hpSwitchAutzUserRoleGroup4.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_P),(_A,_Q),(_A,_V),(_A,_S),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:hpSwitchAutzUserRoleGroup4.setStatus(_E)
hpSwitchAutzUserRoleGroup5=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,32,2,2,13))
hpSwitchAutzUserRoleGroup5.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_P),(_A,_Q),(_A,_V),(_A,_S),(_A,_W),(_A,_X),(_A,_h)))
if mibBuilder.loadTexts:hpSwitchAutzUserRoleGroup5.setStatus(_E)
hpSwitchAutzUserRoleGroup6=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,32,2,2,14))
hpSwitchAutzUserRoleGroup6.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_P),(_A,_Q),(_A,_S),(_A,_W),(_A,_X),(_A,_h),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8)))
if mibBuilder.loadTexts:hpSwitchAutzUserRoleGroup6.setStatus(_B)
hpicfSwitchAuthServerFail=NotificationType((1,3,6,1,4,1,11,2,14,11,5,1,32,0,1))
hpicfSwitchAuthServerFail.setObjects(*((_A,_e),(_A,_f),(_A,_g)))
if mibBuilder.loadTexts:hpicfSwitchAuthServerFail.setStatus(_B)
hpicfSwitchAuthorizationNotificationGroup=NotificationGroup((1,3,6,1,4,1,11,2,14,11,5,1,32,2,2,2))
hpicfSwitchAuthorizationNotificationGroup.setObjects((_A,_A9))
if mibBuilder.loadTexts:hpicfSwitchAuthorizationNotificationGroup.setStatus(_B)
hpSwitchAuthorizationMIBCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,32,2,1,1))
hpSwitchAuthorizationMIBCompliance.setObjects((_A,_AA))
if mibBuilder.loadTexts:hpSwitchAuthorizationMIBCompliance.setStatus(_B)
hpSwitchLocalMgmtPrivGrpMIBCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,32,2,1,2))
hpSwitchLocalMgmtPrivGrpMIBCompliance.setObjects((_A,_i))
if mibBuilder.loadTexts:hpSwitchLocalMgmtPrivGrpMIBCompliance.setStatus(_E)
hpSwitchLocalMgmtPrivGrpMIBCompliance1=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,32,2,1,3))
hpSwitchLocalMgmtPrivGrpMIBCompliance1.setObjects((_A,_j))
if mibBuilder.loadTexts:hpSwitchLocalMgmtPrivGrpMIBCompliance1.setStatus(_E)
hpSwitchAuthorizationObjectsGrpMIBCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,32,2,1,4))
hpSwitchAuthorizationObjectsGrpMIBCompliance.setObjects((_A,_AB))
if mibBuilder.loadTexts:hpSwitchAuthorizationObjectsGrpMIBCompliance.setStatus(_B)
hpSwitchAuthorizationNotificationGrpMIBCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,32,2,1,5))
hpSwitchAuthorizationNotificationGrpMIBCompliance.setObjects((_A,_AC))
if mibBuilder.loadTexts:hpSwitchAuthorizationNotificationGrpMIBCompliance.setStatus(_B)
hpSwitchAutzRoleGrpCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,32,2,1,6))
hpSwitchAutzRoleGrpCompliance.setObjects((_A,_AD))
if mibBuilder.loadTexts:hpSwitchAutzRoleGrpCompliance.setStatus(_E)
hpSwitchAutzRoleGrpCompliance1=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,32,2,1,7))
hpSwitchAutzRoleGrpCompliance1.setObjects((_A,_AE))
if mibBuilder.loadTexts:hpSwitchAutzRoleGrpCompliance1.setStatus(_E)
hpSwitchAutzRoleGrpCompliance2=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,32,2,1,8))
hpSwitchAutzRoleGrpCompliance2.setObjects((_A,_AF))
if mibBuilder.loadTexts:hpSwitchAutzRoleGrpCompliance2.setStatus(_E)
hpSwitchAutzRoleGrpCompliance3=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,32,2,1,9))
hpSwitchAutzRoleGrpCompliance3.setObjects((_A,_AG))
if mibBuilder.loadTexts:hpSwitchAutzRoleGrpCompliance3.setStatus(_E)
hpSwitchAutzRoleGrpCompliance4=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,32,2,1,10))
hpSwitchAutzRoleGrpCompliance4.setObjects((_A,_AH))
if mibBuilder.loadTexts:hpSwitchAutzRoleGrpCompliance4.setStatus(_E)
hpSwitchLocalMgmtPrivGrpMIBCompliance2=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,32,2,1,11))
hpSwitchLocalMgmtPrivGrpMIBCompliance2.setObjects((_A,_i))
if mibBuilder.loadTexts:hpSwitchLocalMgmtPrivGrpMIBCompliance2.setStatus(_B)
hpSwitchLocalMgmtPrivGrpMIBCompliance3=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,32,2,1,12))
hpSwitchLocalMgmtPrivGrpMIBCompliance3.setObjects((_A,_j))
if mibBuilder.loadTexts:hpSwitchLocalMgmtPrivGrpMIBCompliance3.setStatus(_B)
hpSwitchAutzRoleGrpCompliance5=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,32,2,1,13))
hpSwitchAutzRoleGrpCompliance5.setObjects((_A,_AI))
if mibBuilder.loadTexts:hpSwitchAutzRoleGrpCompliance5.setStatus(_E)
hpSwitchAutzRoleGrpCompliance6=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,32,2,1,14))
hpSwitchAutzRoleGrpCompliance6.setObjects((_A,_AJ))
if mibBuilder.loadTexts:hpSwitchAutzRoleGrpCompliance6.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'HpAutzUserRoleName':HpAutzUserRoleName,'hpSwitchAuthorizationMIB':hpSwitchAuthorizationMIB,'hpicfSwitchAuthorizationNotifications':hpicfSwitchAuthorizationNotifications,_A9:hpicfSwitchAuthServerFail,'hpSwitchAuthorizationConfig':hpSwitchAuthorizationConfig,'hpSwitchAutzServiceTable':hpSwitchAutzServiceTable,'hpSwitchAutzServiceEntry':hpSwitchAutzServiceEntry,_l:hpSwitchAutzServiceType,_s:hpSwitchAutzServicePrimaryMethod,_t:hpSwitchAutzServiceSecondaryMethod,_u:hpSwitchAutzServiceCommandsLevel,'hpicfSwitchAuthObjects':hpicfSwitchAuthObjects,_e:hpicfSwitchAuthServerType,_f:hpicfSwitchAuthServerIPType,_g:hpicfSwitchAuthServerIP,'hpSwitchAuthConfigObjects':hpSwitchAuthConfigObjects,_v:hpicfSwitchAuthServerNotifyEnable,'hpSwitchAuthLocalPrivConfigObjects':hpSwitchAuthLocalPrivConfigObjects,'hpSwitchLocalMgmtPrivGroupsTable':hpSwitchLocalMgmtPrivGroupsTable,'hpSwitchLocalMgmtPrivGroupsEntry':hpSwitchLocalMgmtPrivGroupsEntry,_b:hpSwitchLocalMgmtPrivGroupIndex,_w:hpSwitchLocalMgmtPrivGroupName,_A1:hpSwitchLocalMgmtPrivGroupStatus,'hpSwitchLocalMgmtPrivCommandsTable':hpSwitchLocalMgmtPrivCommandsTable,'hpSwitchLocalMgmtPrivCommandsEntry':hpSwitchLocalMgmtPrivCommandsEntry,_o:hpSwitchLocalMgmtPrivCmdSequenceIndex,_x:hpSwitchLocalMgmtPrivCmdMatchStr,_y:hpSwitchLocalMgmtPrivCmdPriv,_z:hpSwitchLocalMgmtPrivCmdSendLog,_A0:hpSwitchLocalMgmtPrivCmdStatus,'hpSwitchAutzUserRole':hpSwitchAutzUserRole,_F:hpSwitchAutzUserRoleEnabled,_G:hpSwitchAutzUserRoleInitialRoleName,'hpSwitchAutzUserRoleTable':hpSwitchAutzUserRoleTable,'hpSwitchAutzUserRoleEntry':hpSwitchAutzUserRoleEntry,_c:hpSwitchAutzUserRoleName,_H:hpSwitchAutzUserRoleRowStatus,_I:hpSwitchAutzUserRoleType,_J:hpSwitchAutzUserRoleCaptivePortalProfileName,_K:hpSwitchAutzUserRoleIngressUserPolicyName,_L:hpSwitchAutzUserRoleReauthPeriod,_M:hpSwitchAutzUserRoleVlanId,_N:hpSwitchAutzUserRoleVlanName,_P:hpSwitchAutzUserRoleTunneledNodeServerRedirect,_Q:hpSwitchAutzUserRoleTunneledNodeServerSecondaryRole,_V:hpSwitchAutzUserRoleTaggedVlanId,_S:hpSwitchAutzUserRoleTaggedVlanName,_X:hpSwitchAutzUserRoleTunneledNodeServerDownloadableRole,_h:hpSwitchAutzUserRoleLogOffPeriod,_A5:hpSwitchAutzUserRoleCachedReauthPeriod,_A7:hpSwitchAutzUserRoleTaggedVlanList,_W:hpSwitchAutzUserRoleDownloadedEnabled,'hpSwitchAutzUserRoleSubTable':hpSwitchAutzUserRoleSubTable,'hpSwitchAutzUserRoleSubEntry':hpSwitchAutzUserRoleSubEntry,_r:hpSwitchAutzUserRoleSubType,_A3:hpSwitchAutzUserRoleAdminEdgePort,_A4:hpSwitchAutzUserRolePoePriority,_A6:hpSwitchAutzUserRolePoeAllocBy,_A2:hpSwitchAutzUserRoleSubTypeRowStatus,_A8:hpSwitchAutzUserRolePortMode,'hpSwitchAuthorizationConformance':hpSwitchAuthorizationConformance,'hpSwitchAuthorizationMIBCompliances':hpSwitchAuthorizationMIBCompliances,'hpSwitchAuthorizationMIBCompliance':hpSwitchAuthorizationMIBCompliance,'hpSwitchLocalMgmtPrivGrpMIBCompliance':hpSwitchLocalMgmtPrivGrpMIBCompliance,'hpSwitchLocalMgmtPrivGrpMIBCompliance1':hpSwitchLocalMgmtPrivGrpMIBCompliance1,'hpSwitchAuthorizationObjectsGrpMIBCompliance':hpSwitchAuthorizationObjectsGrpMIBCompliance,'hpSwitchAuthorizationNotificationGrpMIBCompliance':hpSwitchAuthorizationNotificationGrpMIBCompliance,'hpSwitchAutzRoleGrpCompliance':hpSwitchAutzRoleGrpCompliance,'hpSwitchAutzRoleGrpCompliance1':hpSwitchAutzRoleGrpCompliance1,'hpSwitchAutzRoleGrpCompliance2':hpSwitchAutzRoleGrpCompliance2,'hpSwitchAutzRoleGrpCompliance3':hpSwitchAutzRoleGrpCompliance3,'hpSwitchAutzRoleGrpCompliance4':hpSwitchAutzRoleGrpCompliance4,'hpSwitchLocalMgmtPrivGrpMIBCompliance2':hpSwitchLocalMgmtPrivGrpMIBCompliance2,'hpSwitchLocalMgmtPrivGrpMIBCompliance3':hpSwitchLocalMgmtPrivGrpMIBCompliance3,'hpSwitchAutzRoleGrpCompliance5':hpSwitchAutzRoleGrpCompliance5,'hpSwitchAutzRoleGrpCompliance6':hpSwitchAutzRoleGrpCompliance6,'hpSwitchAuthorizationMIBGroups':hpSwitchAuthorizationMIBGroups,_AA:hpSwitchAuthorizationConfigGroup,_AC:hpicfSwitchAuthorizationNotificationGroup,_AB:hpicfSwitchAuthorizationObjectsGroup,_i:hpSwitchAutzLocalMgmtPrivGroup,_j:hpSwitchAutzLocalMgmtPrivGroup1,_AD:hpSwitchAutzUserRoleGroup,_AE:hpSwitchAutzUserRoleGroup1,_AF:hpSwitchAutzUserRoleGroup2,_AG:hpSwitchAutzUserRoleGroup3,_AH:hpSwitchAutzUserRoleGroup4,_AI:hpSwitchAutzUserRoleGroup5,_AJ:hpSwitchAutzUserRoleGroup6})