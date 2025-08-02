_AD='cmSecurityObjectGroup'
_AC='f3SecurityTrap'
_AB='f3PrivilegeChangeRemoteName'
_AA='f3PrivilegeChangeRemainingTime'
_A9='f3PrivilegeChangeAction'
_A8='f3UsmUserAccessType'
_A7='cmRemoteAuthServerIpv6Addr'
_A6='cmRemoteAuthServerIpVersion'
_A5='cmRemoteAuthServerAccountingPort'
_A4='cmRemoteAuthServerSecret'
_A3='cmRemoteAuthServerTimeout'
_A2='cmRemoteAuthServerNumRetries'
_A1='cmRemoteAuthServerPort'
_A0='cmRemoteAuthServerIpAddress'
_z='cmRemoteAuthServerOrder'
_y='cmRemoteAuthServerEnabled'
_x='cmSecurityCryptoPassword'
_w='cmSecurityUserAction'
_v='cmSecurityUserRowStatus'
_u='cmSecurityUserStorageType'
_t='cmSecurityUserPassword'
_s='cmSecurityUserCliPagingEnable'
_r='cmSecurityUserLastLockedoutTime'
_q='cmSecurityUserLockedout'
_p='cmSecurityUserLastLoginTime'
_o='cmSecurityUserNumFailedLoginAttempts'
_n='cmSecurityUserLoginTimeout'
_m='cmSecurityUserPrivLevel'
_l='cmSecurityUserComment'
_k='f3SecurityTrapInfo'
_j='f3SecurityTrapType'
_i='f3NasIpv6Addr'
_h='f3TacacsDefaultPrivLevel'
_g='f3TacacsPrivLevelControlEnabled'
_f='cmRemoteAuthServerAccountingEnabled'
_e='cmSecurityPolicyStrength'
_d='cmNASIpAddress'
_c='cmAuthType'
_b='cmAccessOrder'
_a='cmAuthProtocol'
_Z='f3UsmUserEntry'
_Y='minutes'
_X='f3PrivilegeChangeId'
_W='not-applicable'
_V='Integer32'
_U='f3PrivilegeChangeState'
_T='f3PrivilegeChangeDuration'
_S='f3PrivilegeChangeRequestedPrivilege'
_R='f3PrivilegeChangeCurrentPrivilege'
_Q='f3PrivilegeChangeInterface'
_P='f3PrivilegeChangeTerminalIpv6Address'
_O='f3PrivilegeChangeTerminalIpv4Address'
_N='f3PrivilegeChangeIpv6Address'
_M='f3PrivilegeChangeIpv4Address'
_L='f3PrivilegeChangeUserName'
_K='cmRemoteAuthServerIndex'
_J='cmSecurityUserRemoteUser'
_I='cmSecurityUserName'
_H='none'
_G='Unsigned32'
_F='DisplayString'
_E='read-create'
_D='read-only'
_C='read-write'
_B='CM-SECURITY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsp150cm,=mibBuilder.importSymbols('ADVA-MIB','fsp150cm')
IpVersion,UserInterfaceType=mibBuilder.importSymbols('CM-COMMON-MIB','IpVersion','UserInterfaceType')
Ipv6Address,=mibBuilder.importSymbols('IPV6-TC','Ipv6Address')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
usmUserEntry,=mibBuilder.importSymbols('SNMP-USER-BASED-SM-MIB','usmUserEntry')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_V,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_F,'PhysAddress','RowStatus','StorageType','TextualConvention','TruthValue')
cmSecurityMIB=ModuleIdentity((1,3,6,1,4,1,2544,1,12,10))
if mibBuilder.loadTexts:cmSecurityMIB.setRevisions(('2016-06-14 00:00',))
class CmRemoteAuthProtocol(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('radius',2),('tacacs',3)))
class CmSecurityAccessOrder(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('local',1),('remote',2)))
class CmSecurityAuthType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('pap',1),('chap',2)))
class CmSecurityPrivLevel(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_W,0),('retrieve',1),('maintenance',2),('provisioning',3),('superuser',4),('testuser',5),('cryptouser',6),('netconf',7)))
class CmRemoteAuthOrder(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('first',1),('second',2),('third',3)))
class CmSecurityPolicyStrength(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('low',1),('medium',2),('high',3)))
class UsmUserAccessType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_C,2),('trap-only',3)))
class SecurityUserAction(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_W,0),('remove-lockout',1)))
class SnmpSecurityTrapType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('all',1),('loginFailed',2),('disabled',3)))
class PrivilegeRequestAction(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('undefined',0),(_H,1),('approve',2),('deny',3),('cancel',4)))
class PrivilegeRequestState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_H,1),('requestSent',2),('requestCanceled',3),('requestApproved',4),('requestDenied',5),('requestTimeout',6),('accessExpired',7),('accessCanceled',8)))
_CmSecurityObjects_ObjectIdentity=ObjectIdentity
cmSecurityObjects=_CmSecurityObjects_ObjectIdentity((1,3,6,1,4,1,2544,1,12,10,1))
_CmAuthProtocol_Type=CmRemoteAuthProtocol
_CmAuthProtocol_Object=MibScalar
cmAuthProtocol=_CmAuthProtocol_Object((1,3,6,1,4,1,2544,1,12,10,1,1),_CmAuthProtocol_Type())
cmAuthProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:cmAuthProtocol.setStatus(_A)
_CmAccessOrder_Type=CmSecurityAccessOrder
_CmAccessOrder_Object=MibScalar
cmAccessOrder=_CmAccessOrder_Object((1,3,6,1,4,1,2544,1,12,10,1,2),_CmAccessOrder_Type())
cmAccessOrder.setMaxAccess(_C)
if mibBuilder.loadTexts:cmAccessOrder.setStatus(_A)
_CmAuthType_Type=CmSecurityAuthType
_CmAuthType_Object=MibScalar
cmAuthType=_CmAuthType_Object((1,3,6,1,4,1,2544,1,12,10,1,3),_CmAuthType_Type())
cmAuthType.setMaxAccess(_C)
if mibBuilder.loadTexts:cmAuthType.setStatus(_A)
_CmNASIpAddress_Type=IpAddress
_CmNASIpAddress_Object=MibScalar
cmNASIpAddress=_CmNASIpAddress_Object((1,3,6,1,4,1,2544,1,12,10,1,4),_CmNASIpAddress_Type())
cmNASIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cmNASIpAddress.setStatus(_A)
_CmSecurityUserTable_Object=MibTable
cmSecurityUserTable=_CmSecurityUserTable_Object((1,3,6,1,4,1,2544,1,12,10,1,5))
if mibBuilder.loadTexts:cmSecurityUserTable.setStatus(_A)
_CmSecurityUserEntry_Object=MibTableRow
cmSecurityUserEntry=_CmSecurityUserEntry_Object((1,3,6,1,4,1,2544,1,12,10,1,5,1))
cmSecurityUserEntry.setIndexNames((0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:cmSecurityUserEntry.setStatus(_A)
class _CmSecurityUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CmSecurityUserName_Type.__name__=_F
_CmSecurityUserName_Object=MibTableColumn
cmSecurityUserName=_CmSecurityUserName_Object((1,3,6,1,4,1,2544,1,12,10,1,5,1,1),_CmSecurityUserName_Type())
cmSecurityUserName.setMaxAccess(_E)
if mibBuilder.loadTexts:cmSecurityUserName.setStatus(_A)
class _CmSecurityUserComment_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_CmSecurityUserComment_Type.__name__=_F
_CmSecurityUserComment_Object=MibTableColumn
cmSecurityUserComment=_CmSecurityUserComment_Object((1,3,6,1,4,1,2544,1,12,10,1,5,1,2),_CmSecurityUserComment_Type())
cmSecurityUserComment.setMaxAccess(_E)
if mibBuilder.loadTexts:cmSecurityUserComment.setStatus(_A)
_CmSecurityUserPrivLevel_Type=CmSecurityPrivLevel
_CmSecurityUserPrivLevel_Object=MibTableColumn
cmSecurityUserPrivLevel=_CmSecurityUserPrivLevel_Object((1,3,6,1,4,1,2544,1,12,10,1,5,1,3),_CmSecurityUserPrivLevel_Type())
cmSecurityUserPrivLevel.setMaxAccess(_E)
if mibBuilder.loadTexts:cmSecurityUserPrivLevel.setStatus(_A)
_CmSecurityUserLoginTimeout_Type=Integer32
_CmSecurityUserLoginTimeout_Object=MibTableColumn
cmSecurityUserLoginTimeout=_CmSecurityUserLoginTimeout_Object((1,3,6,1,4,1,2544,1,12,10,1,5,1,4),_CmSecurityUserLoginTimeout_Type())
cmSecurityUserLoginTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:cmSecurityUserLoginTimeout.setStatus(_A)
_CmSecurityUserNumFailedLoginAttempts_Type=Integer32
_CmSecurityUserNumFailedLoginAttempts_Object=MibTableColumn
cmSecurityUserNumFailedLoginAttempts=_CmSecurityUserNumFailedLoginAttempts_Object((1,3,6,1,4,1,2544,1,12,10,1,5,1,5),_CmSecurityUserNumFailedLoginAttempts_Type())
cmSecurityUserNumFailedLoginAttempts.setMaxAccess(_D)
if mibBuilder.loadTexts:cmSecurityUserNumFailedLoginAttempts.setStatus(_A)
_CmSecurityUserLastLoginTime_Type=DateAndTime
_CmSecurityUserLastLoginTime_Object=MibTableColumn
cmSecurityUserLastLoginTime=_CmSecurityUserLastLoginTime_Object((1,3,6,1,4,1,2544,1,12,10,1,5,1,6),_CmSecurityUserLastLoginTime_Type())
cmSecurityUserLastLoginTime.setMaxAccess(_D)
if mibBuilder.loadTexts:cmSecurityUserLastLoginTime.setStatus(_A)
_CmSecurityUserLockedout_Type=TruthValue
_CmSecurityUserLockedout_Object=MibTableColumn
cmSecurityUserLockedout=_CmSecurityUserLockedout_Object((1,3,6,1,4,1,2544,1,12,10,1,5,1,7),_CmSecurityUserLockedout_Type())
cmSecurityUserLockedout.setMaxAccess(_D)
if mibBuilder.loadTexts:cmSecurityUserLockedout.setStatus(_A)
_CmSecurityUserLastLockedoutTime_Type=DateAndTime
_CmSecurityUserLastLockedoutTime_Object=MibTableColumn
cmSecurityUserLastLockedoutTime=_CmSecurityUserLastLockedoutTime_Object((1,3,6,1,4,1,2544,1,12,10,1,5,1,8),_CmSecurityUserLastLockedoutTime_Type())
cmSecurityUserLastLockedoutTime.setMaxAccess(_D)
if mibBuilder.loadTexts:cmSecurityUserLastLockedoutTime.setStatus(_A)
_CmSecurityUserCliPagingEnable_Type=TruthValue
_CmSecurityUserCliPagingEnable_Object=MibTableColumn
cmSecurityUserCliPagingEnable=_CmSecurityUserCliPagingEnable_Object((1,3,6,1,4,1,2544,1,12,10,1,5,1,9),_CmSecurityUserCliPagingEnable_Type())
cmSecurityUserCliPagingEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:cmSecurityUserCliPagingEnable.setStatus(_A)
_CmSecurityUserRemoteUser_Type=TruthValue
_CmSecurityUserRemoteUser_Object=MibTableColumn
cmSecurityUserRemoteUser=_CmSecurityUserRemoteUser_Object((1,3,6,1,4,1,2544,1,12,10,1,5,1,10),_CmSecurityUserRemoteUser_Type())
cmSecurityUserRemoteUser.setMaxAccess(_D)
if mibBuilder.loadTexts:cmSecurityUserRemoteUser.setStatus(_A)
class _CmSecurityUserPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CmSecurityUserPassword_Type.__name__=_F
_CmSecurityUserPassword_Object=MibTableColumn
cmSecurityUserPassword=_CmSecurityUserPassword_Object((1,3,6,1,4,1,2544,1,12,10,1,5,1,11),_CmSecurityUserPassword_Type())
cmSecurityUserPassword.setMaxAccess(_E)
if mibBuilder.loadTexts:cmSecurityUserPassword.setStatus(_A)
_CmSecurityUserStorageType_Type=StorageType
_CmSecurityUserStorageType_Object=MibTableColumn
cmSecurityUserStorageType=_CmSecurityUserStorageType_Object((1,3,6,1,4,1,2544,1,12,10,1,5,1,12),_CmSecurityUserStorageType_Type())
cmSecurityUserStorageType.setMaxAccess(_E)
if mibBuilder.loadTexts:cmSecurityUserStorageType.setStatus(_A)
_CmSecurityUserRowStatus_Type=RowStatus
_CmSecurityUserRowStatus_Object=MibTableColumn
cmSecurityUserRowStatus=_CmSecurityUserRowStatus_Object((1,3,6,1,4,1,2544,1,12,10,1,5,1,13),_CmSecurityUserRowStatus_Type())
cmSecurityUserRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cmSecurityUserRowStatus.setStatus(_A)
_CmSecurityUserAction_Type=SecurityUserAction
_CmSecurityUserAction_Object=MibTableColumn
cmSecurityUserAction=_CmSecurityUserAction_Object((1,3,6,1,4,1,2544,1,12,10,1,5,1,14),_CmSecurityUserAction_Type())
cmSecurityUserAction.setMaxAccess(_C)
if mibBuilder.loadTexts:cmSecurityUserAction.setStatus(_A)
class _CmSecurityCryptoPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CmSecurityCryptoPassword_Type.__name__=_F
_CmSecurityCryptoPassword_Object=MibTableColumn
cmSecurityCryptoPassword=_CmSecurityCryptoPassword_Object((1,3,6,1,4,1,2544,1,12,10,1,5,1,15),_CmSecurityCryptoPassword_Type())
cmSecurityCryptoPassword.setMaxAccess(_E)
if mibBuilder.loadTexts:cmSecurityCryptoPassword.setStatus(_A)
_CmSecurityUserRemoteCryptoUser_Type=TruthValue
_CmSecurityUserRemoteCryptoUser_Object=MibTableColumn
cmSecurityUserRemoteCryptoUser=_CmSecurityUserRemoteCryptoUser_Object((1,3,6,1,4,1,2544,1,12,10,1,5,1,16),_CmSecurityUserRemoteCryptoUser_Type())
cmSecurityUserRemoteCryptoUser.setMaxAccess(_E)
if mibBuilder.loadTexts:cmSecurityUserRemoteCryptoUser.setStatus(_A)
_CmRemoteAuthServerTable_Object=MibTable
cmRemoteAuthServerTable=_CmRemoteAuthServerTable_Object((1,3,6,1,4,1,2544,1,12,10,1,6))
if mibBuilder.loadTexts:cmRemoteAuthServerTable.setStatus(_A)
_CmRemoteAuthServerEntry_Object=MibTableRow
cmRemoteAuthServerEntry=_CmRemoteAuthServerEntry_Object((1,3,6,1,4,1,2544,1,12,10,1,6,1))
cmRemoteAuthServerEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:cmRemoteAuthServerEntry.setStatus(_A)
_CmRemoteAuthServerIndex_Type=Integer32
_CmRemoteAuthServerIndex_Object=MibTableColumn
cmRemoteAuthServerIndex=_CmRemoteAuthServerIndex_Object((1,3,6,1,4,1,2544,1,12,10,1,6,1,1),_CmRemoteAuthServerIndex_Type())
cmRemoteAuthServerIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:cmRemoteAuthServerIndex.setStatus(_A)
_CmRemoteAuthServerEnabled_Type=TruthValue
_CmRemoteAuthServerEnabled_Object=MibTableColumn
cmRemoteAuthServerEnabled=_CmRemoteAuthServerEnabled_Object((1,3,6,1,4,1,2544,1,12,10,1,6,1,2),_CmRemoteAuthServerEnabled_Type())
cmRemoteAuthServerEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:cmRemoteAuthServerEnabled.setStatus(_A)
_CmRemoteAuthServerOrder_Type=CmRemoteAuthOrder
_CmRemoteAuthServerOrder_Object=MibTableColumn
cmRemoteAuthServerOrder=_CmRemoteAuthServerOrder_Object((1,3,6,1,4,1,2544,1,12,10,1,6,1,3),_CmRemoteAuthServerOrder_Type())
cmRemoteAuthServerOrder.setMaxAccess(_C)
if mibBuilder.loadTexts:cmRemoteAuthServerOrder.setStatus(_A)
_CmRemoteAuthServerIpAddress_Type=IpAddress
_CmRemoteAuthServerIpAddress_Object=MibTableColumn
cmRemoteAuthServerIpAddress=_CmRemoteAuthServerIpAddress_Object((1,3,6,1,4,1,2544,1,12,10,1,6,1,4),_CmRemoteAuthServerIpAddress_Type())
cmRemoteAuthServerIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cmRemoteAuthServerIpAddress.setStatus(_A)
_CmRemoteAuthServerPort_Type=Integer32
_CmRemoteAuthServerPort_Object=MibTableColumn
cmRemoteAuthServerPort=_CmRemoteAuthServerPort_Object((1,3,6,1,4,1,2544,1,12,10,1,6,1,5),_CmRemoteAuthServerPort_Type())
cmRemoteAuthServerPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cmRemoteAuthServerPort.setStatus(_A)
_CmRemoteAuthServerNumRetries_Type=Integer32
_CmRemoteAuthServerNumRetries_Object=MibTableColumn
cmRemoteAuthServerNumRetries=_CmRemoteAuthServerNumRetries_Object((1,3,6,1,4,1,2544,1,12,10,1,6,1,6),_CmRemoteAuthServerNumRetries_Type())
cmRemoteAuthServerNumRetries.setMaxAccess(_C)
if mibBuilder.loadTexts:cmRemoteAuthServerNumRetries.setStatus(_A)
_CmRemoteAuthServerTimeout_Type=Integer32
_CmRemoteAuthServerTimeout_Object=MibTableColumn
cmRemoteAuthServerTimeout=_CmRemoteAuthServerTimeout_Object((1,3,6,1,4,1,2544,1,12,10,1,6,1,7),_CmRemoteAuthServerTimeout_Type())
cmRemoteAuthServerTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:cmRemoteAuthServerTimeout.setStatus(_A)
class _CmRemoteAuthServerSecret_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_CmRemoteAuthServerSecret_Type.__name__=_F
_CmRemoteAuthServerSecret_Object=MibTableColumn
cmRemoteAuthServerSecret=_CmRemoteAuthServerSecret_Object((1,3,6,1,4,1,2544,1,12,10,1,6,1,8),_CmRemoteAuthServerSecret_Type())
cmRemoteAuthServerSecret.setMaxAccess(_C)
if mibBuilder.loadTexts:cmRemoteAuthServerSecret.setStatus(_A)
_CmRemoteAuthServerAccountingPort_Type=Integer32
_CmRemoteAuthServerAccountingPort_Object=MibTableColumn
cmRemoteAuthServerAccountingPort=_CmRemoteAuthServerAccountingPort_Object((1,3,6,1,4,1,2544,1,12,10,1,6,1,9),_CmRemoteAuthServerAccountingPort_Type())
cmRemoteAuthServerAccountingPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cmRemoteAuthServerAccountingPort.setStatus(_A)
_CmRemoteAuthServerIpVersion_Type=IpVersion
_CmRemoteAuthServerIpVersion_Object=MibTableColumn
cmRemoteAuthServerIpVersion=_CmRemoteAuthServerIpVersion_Object((1,3,6,1,4,1,2544,1,12,10,1,6,1,10),_CmRemoteAuthServerIpVersion_Type())
cmRemoteAuthServerIpVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:cmRemoteAuthServerIpVersion.setStatus(_A)
_CmRemoteAuthServerIpv6Addr_Type=Ipv6Address
_CmRemoteAuthServerIpv6Addr_Object=MibTableColumn
cmRemoteAuthServerIpv6Addr=_CmRemoteAuthServerIpv6Addr_Object((1,3,6,1,4,1,2544,1,12,10,1,6,1,11),_CmRemoteAuthServerIpv6Addr_Type())
cmRemoteAuthServerIpv6Addr.setMaxAccess(_C)
if mibBuilder.loadTexts:cmRemoteAuthServerIpv6Addr.setStatus(_A)
_CmSecurityPolicyStrength_Type=CmSecurityPolicyStrength
_CmSecurityPolicyStrength_Object=MibScalar
cmSecurityPolicyStrength=_CmSecurityPolicyStrength_Object((1,3,6,1,4,1,2544,1,12,10,1,7),_CmSecurityPolicyStrength_Type())
cmSecurityPolicyStrength.setMaxAccess(_C)
if mibBuilder.loadTexts:cmSecurityPolicyStrength.setStatus(_A)
_CmRemoteAuthServerAccountingEnabled_Type=TruthValue
_CmRemoteAuthServerAccountingEnabled_Object=MibScalar
cmRemoteAuthServerAccountingEnabled=_CmRemoteAuthServerAccountingEnabled_Object((1,3,6,1,4,1,2544,1,12,10,1,8),_CmRemoteAuthServerAccountingEnabled_Type())
cmRemoteAuthServerAccountingEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:cmRemoteAuthServerAccountingEnabled.setStatus(_A)
_F3UsmUserTable_Object=MibTable
f3UsmUserTable=_F3UsmUserTable_Object((1,3,6,1,4,1,2544,1,12,10,1,9))
if mibBuilder.loadTexts:f3UsmUserTable.setStatus(_A)
_F3UsmUserEntry_Object=MibTableRow
f3UsmUserEntry=_F3UsmUserEntry_Object((1,3,6,1,4,1,2544,1,12,10,1,9,1))
if mibBuilder.loadTexts:f3UsmUserEntry.setStatus(_A)
_F3UsmUserAccessType_Type=UsmUserAccessType
_F3UsmUserAccessType_Object=MibTableColumn
f3UsmUserAccessType=_F3UsmUserAccessType_Object((1,3,6,1,4,1,2544,1,12,10,1,9,1,1),_F3UsmUserAccessType_Type())
f3UsmUserAccessType.setMaxAccess(_D)
if mibBuilder.loadTexts:f3UsmUserAccessType.setStatus(_A)
_F3TacacsPrivLevelControlEnabled_Type=TruthValue
_F3TacacsPrivLevelControlEnabled_Object=MibScalar
f3TacacsPrivLevelControlEnabled=_F3TacacsPrivLevelControlEnabled_Object((1,3,6,1,4,1,2544,1,12,10,1,10),_F3TacacsPrivLevelControlEnabled_Type())
f3TacacsPrivLevelControlEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:f3TacacsPrivLevelControlEnabled.setStatus(_A)
_F3TacacsDefaultPrivLevel_Type=CmSecurityPrivLevel
_F3TacacsDefaultPrivLevel_Object=MibScalar
f3TacacsDefaultPrivLevel=_F3TacacsDefaultPrivLevel_Object((1,3,6,1,4,1,2544,1,12,10,1,11),_F3TacacsDefaultPrivLevel_Type())
f3TacacsDefaultPrivLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:f3TacacsDefaultPrivLevel.setStatus(_A)
_F3NasIpv6Addr_Type=Ipv6Address
_F3NasIpv6Addr_Object=MibScalar
f3NasIpv6Addr=_F3NasIpv6Addr_Object((1,3,6,1,4,1,2544,1,12,10,1,12),_F3NasIpv6Addr_Type())
f3NasIpv6Addr.setMaxAccess(_C)
if mibBuilder.loadTexts:f3NasIpv6Addr.setStatus(_A)
_F3SecurityTrapType_Type=SnmpSecurityTrapType
_F3SecurityTrapType_Object=MibScalar
f3SecurityTrapType=_F3SecurityTrapType_Object((1,3,6,1,4,1,2544,1,12,10,1,13),_F3SecurityTrapType_Type())
f3SecurityTrapType.setMaxAccess(_C)
if mibBuilder.loadTexts:f3SecurityTrapType.setStatus(_A)
_F3SecurityTrapInfo_Type=DisplayString
_F3SecurityTrapInfo_Object=MibScalar
f3SecurityTrapInfo=_F3SecurityTrapInfo_Object((1,3,6,1,4,1,2544,1,12,10,1,14),_F3SecurityTrapInfo_Type())
f3SecurityTrapInfo.setMaxAccess(_D)
if mibBuilder.loadTexts:f3SecurityTrapInfo.setStatus(_A)
_F3PrivilegeChangeTable_Object=MibTable
f3PrivilegeChangeTable=_F3PrivilegeChangeTable_Object((1,3,6,1,4,1,2544,1,12,10,1,15))
if mibBuilder.loadTexts:f3PrivilegeChangeTable.setStatus(_A)
_F3PrivilegeChangeEntry_Object=MibTableRow
f3PrivilegeChangeEntry=_F3PrivilegeChangeEntry_Object((1,3,6,1,4,1,2544,1,12,10,1,15,1))
f3PrivilegeChangeEntry.setIndexNames((0,_B,_X))
if mibBuilder.loadTexts:f3PrivilegeChangeEntry.setStatus(_A)
class _F3PrivilegeChangeId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_F3PrivilegeChangeId_Type.__name__=_G
_F3PrivilegeChangeId_Object=MibTableColumn
f3PrivilegeChangeId=_F3PrivilegeChangeId_Object((1,3,6,1,4,1,2544,1,12,10,1,15,1,1),_F3PrivilegeChangeId_Type())
f3PrivilegeChangeId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:f3PrivilegeChangeId.setStatus(_A)
_F3PrivilegeChangeUserName_Type=SnmpAdminString
_F3PrivilegeChangeUserName_Object=MibTableColumn
f3PrivilegeChangeUserName=_F3PrivilegeChangeUserName_Object((1,3,6,1,4,1,2544,1,12,10,1,15,1,2),_F3PrivilegeChangeUserName_Type())
f3PrivilegeChangeUserName.setMaxAccess(_D)
if mibBuilder.loadTexts:f3PrivilegeChangeUserName.setStatus(_A)
_F3PrivilegeChangeIpv4Address_Type=IpAddress
_F3PrivilegeChangeIpv4Address_Object=MibTableColumn
f3PrivilegeChangeIpv4Address=_F3PrivilegeChangeIpv4Address_Object((1,3,6,1,4,1,2544,1,12,10,1,15,1,3),_F3PrivilegeChangeIpv4Address_Type())
f3PrivilegeChangeIpv4Address.setMaxAccess(_D)
if mibBuilder.loadTexts:f3PrivilegeChangeIpv4Address.setStatus(_A)
_F3PrivilegeChangeIpv6Address_Type=Ipv6Address
_F3PrivilegeChangeIpv6Address_Object=MibTableColumn
f3PrivilegeChangeIpv6Address=_F3PrivilegeChangeIpv6Address_Object((1,3,6,1,4,1,2544,1,12,10,1,15,1,4),_F3PrivilegeChangeIpv6Address_Type())
f3PrivilegeChangeIpv6Address.setMaxAccess(_D)
if mibBuilder.loadTexts:f3PrivilegeChangeIpv6Address.setStatus(_A)
_F3PrivilegeChangeTerminalIpv4Address_Type=IpAddress
_F3PrivilegeChangeTerminalIpv4Address_Object=MibTableColumn
f3PrivilegeChangeTerminalIpv4Address=_F3PrivilegeChangeTerminalIpv4Address_Object((1,3,6,1,4,1,2544,1,12,10,1,15,1,5),_F3PrivilegeChangeTerminalIpv4Address_Type())
f3PrivilegeChangeTerminalIpv4Address.setMaxAccess(_D)
if mibBuilder.loadTexts:f3PrivilegeChangeTerminalIpv4Address.setStatus(_A)
_F3PrivilegeChangeTerminalIpv6Address_Type=Ipv6Address
_F3PrivilegeChangeTerminalIpv6Address_Object=MibTableColumn
f3PrivilegeChangeTerminalIpv6Address=_F3PrivilegeChangeTerminalIpv6Address_Object((1,3,6,1,4,1,2544,1,12,10,1,15,1,6),_F3PrivilegeChangeTerminalIpv6Address_Type())
f3PrivilegeChangeTerminalIpv6Address.setMaxAccess(_D)
if mibBuilder.loadTexts:f3PrivilegeChangeTerminalIpv6Address.setStatus(_A)
_F3PrivilegeChangeInterface_Type=UserInterfaceType
_F3PrivilegeChangeInterface_Object=MibTableColumn
f3PrivilegeChangeInterface=_F3PrivilegeChangeInterface_Object((1,3,6,1,4,1,2544,1,12,10,1,15,1,7),_F3PrivilegeChangeInterface_Type())
f3PrivilegeChangeInterface.setMaxAccess(_D)
if mibBuilder.loadTexts:f3PrivilegeChangeInterface.setStatus(_A)
_F3PrivilegeChangeCurrentPrivilege_Type=CmSecurityPrivLevel
_F3PrivilegeChangeCurrentPrivilege_Object=MibTableColumn
f3PrivilegeChangeCurrentPrivilege=_F3PrivilegeChangeCurrentPrivilege_Object((1,3,6,1,4,1,2544,1,12,10,1,15,1,8),_F3PrivilegeChangeCurrentPrivilege_Type())
f3PrivilegeChangeCurrentPrivilege.setMaxAccess(_D)
if mibBuilder.loadTexts:f3PrivilegeChangeCurrentPrivilege.setStatus(_A)
_F3PrivilegeChangeRequestedPrivilege_Type=CmSecurityPrivLevel
_F3PrivilegeChangeRequestedPrivilege_Object=MibTableColumn
f3PrivilegeChangeRequestedPrivilege=_F3PrivilegeChangeRequestedPrivilege_Object((1,3,6,1,4,1,2544,1,12,10,1,15,1,9),_F3PrivilegeChangeRequestedPrivilege_Type())
f3PrivilegeChangeRequestedPrivilege.setMaxAccess(_D)
if mibBuilder.loadTexts:f3PrivilegeChangeRequestedPrivilege.setStatus(_A)
class _F3PrivilegeChangeDuration_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,480))
_F3PrivilegeChangeDuration_Type.__name__=_G
_F3PrivilegeChangeDuration_Object=MibTableColumn
f3PrivilegeChangeDuration=_F3PrivilegeChangeDuration_Object((1,3,6,1,4,1,2544,1,12,10,1,15,1,10),_F3PrivilegeChangeDuration_Type())
f3PrivilegeChangeDuration.setMaxAccess(_D)
if mibBuilder.loadTexts:f3PrivilegeChangeDuration.setStatus(_A)
if mibBuilder.loadTexts:f3PrivilegeChangeDuration.setUnits(_Y)
_F3PrivilegeChangeAction_Type=PrivilegeRequestAction
_F3PrivilegeChangeAction_Object=MibTableColumn
f3PrivilegeChangeAction=_F3PrivilegeChangeAction_Object((1,3,6,1,4,1,2544,1,12,10,1,15,1,11),_F3PrivilegeChangeAction_Type())
f3PrivilegeChangeAction.setMaxAccess(_C)
if mibBuilder.loadTexts:f3PrivilegeChangeAction.setStatus(_A)
_F3PrivilegeChangeState_Type=PrivilegeRequestState
_F3PrivilegeChangeState_Object=MibTableColumn
f3PrivilegeChangeState=_F3PrivilegeChangeState_Object((1,3,6,1,4,1,2544,1,12,10,1,15,1,12),_F3PrivilegeChangeState_Type())
f3PrivilegeChangeState.setMaxAccess(_D)
if mibBuilder.loadTexts:f3PrivilegeChangeState.setStatus(_A)
_F3PrivilegeChangeRemainingTime_Type=Unsigned32
_F3PrivilegeChangeRemainingTime_Object=MibTableColumn
f3PrivilegeChangeRemainingTime=_F3PrivilegeChangeRemainingTime_Object((1,3,6,1,4,1,2544,1,12,10,1,15,1,13),_F3PrivilegeChangeRemainingTime_Type())
f3PrivilegeChangeRemainingTime.setMaxAccess(_D)
if mibBuilder.loadTexts:f3PrivilegeChangeRemainingTime.setStatus(_A)
if mibBuilder.loadTexts:f3PrivilegeChangeRemainingTime.setUnits('seconds')
_F3PrivilegeChangeRemoteName_Type=SnmpAdminString
_F3PrivilegeChangeRemoteName_Object=MibTableColumn
f3PrivilegeChangeRemoteName=_F3PrivilegeChangeRemoteName_Object((1,3,6,1,4,1,2544,1,12,10,1,15,1,14),_F3PrivilegeChangeRemoteName_Type())
f3PrivilegeChangeRemoteName.setMaxAccess(_D)
if mibBuilder.loadTexts:f3PrivilegeChangeRemoteName.setStatus(_A)
_F3UserPrivMgmtControl_Type=TruthValue
_F3UserPrivMgmtControl_Object=MibScalar
f3UserPrivMgmtControl=_F3UserPrivMgmtControl_Object((1,3,6,1,4,1,2544,1,12,10,1,16),_F3UserPrivMgmtControl_Type())
f3UserPrivMgmtControl.setMaxAccess(_C)
if mibBuilder.loadTexts:f3UserPrivMgmtControl.setStatus(_A)
class _F3UserPrivRspTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_F3UserPrivRspTimeout_Type.__name__=_V
_F3UserPrivRspTimeout_Object=MibScalar
f3UserPrivRspTimeout=_F3UserPrivRspTimeout_Object((1,3,6,1,4,1,2544,1,12,10,1,17),_F3UserPrivRspTimeout_Type())
f3UserPrivRspTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:f3UserPrivRspTimeout.setStatus(_A)
if mibBuilder.loadTexts:f3UserPrivRspTimeout.setUnits(_Y)
_CmSecurityConformance_ObjectIdentity=ObjectIdentity
cmSecurityConformance=_CmSecurityConformance_ObjectIdentity((1,3,6,1,4,1,2544,1,12,10,2))
_CmSecurityCompliances_ObjectIdentity=ObjectIdentity
cmSecurityCompliances=_CmSecurityCompliances_ObjectIdentity((1,3,6,1,4,1,2544,1,12,10,2,1))
_CmSecurityGroups_ObjectIdentity=ObjectIdentity
cmSecurityGroups=_CmSecurityGroups_ObjectIdentity((1,3,6,1,4,1,2544,1,12,10,2,2))
_CmSecurityNotifications_ObjectIdentity=ObjectIdentity
cmSecurityNotifications=_CmSecurityNotifications_ObjectIdentity((1,3,6,1,4,1,2544,1,12,10,3))
usmUserEntry.registerAugmentions((_B,_Z))
f3UsmUserEntry.setIndexNames(*usmUserEntry.getIndexNames())
cmSecurityObjectGroup=ObjectGroup((1,3,6,1,4,1,2544,1,12,10,2,2,1))
cmSecurityObjectGroup.setObjects(*((_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_I),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_J),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_K),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_A9),(_B,_U),(_B,_AA),(_B,_AB)))
if mibBuilder.loadTexts:cmSecurityObjectGroup.setStatus(_A)
f3SecurityTrap=NotificationType((1,3,6,1,4,1,2544,1,12,10,3,1))
if mibBuilder.loadTexts:f3SecurityTrap.setStatus(_A)
f3PrivilegeChangeTrap=NotificationType((1,3,6,1,4,1,2544,1,12,10,3,2))
f3PrivilegeChangeTrap.setObjects(*((_B,_U),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:f3PrivilegeChangeTrap.setStatus(_A)
cmSecurityNotifGroup=NotificationGroup((1,3,6,1,4,1,2544,1,12,10,2,2,2))
cmSecurityNotifGroup.setObjects((_B,_AC))
if mibBuilder.loadTexts:cmSecurityNotifGroup.setStatus(_A)
cmSecurityCompliance=ModuleCompliance((1,3,6,1,4,1,2544,1,12,10,2,1,1))
cmSecurityCompliance.setObjects((_B,_AD))
if mibBuilder.loadTexts:cmSecurityCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CmRemoteAuthProtocol':CmRemoteAuthProtocol,'CmSecurityAccessOrder':CmSecurityAccessOrder,'CmSecurityAuthType':CmSecurityAuthType,'CmSecurityPrivLevel':CmSecurityPrivLevel,'CmRemoteAuthOrder':CmRemoteAuthOrder,'CmSecurityPolicyStrength':CmSecurityPolicyStrength,'UsmUserAccessType':UsmUserAccessType,'SecurityUserAction':SecurityUserAction,'SnmpSecurityTrapType':SnmpSecurityTrapType,'PrivilegeRequestAction':PrivilegeRequestAction,'PrivilegeRequestState':PrivilegeRequestState,'cmSecurityMIB':cmSecurityMIB,'cmSecurityObjects':cmSecurityObjects,_a:cmAuthProtocol,_b:cmAccessOrder,_c:cmAuthType,_d:cmNASIpAddress,'cmSecurityUserTable':cmSecurityUserTable,'cmSecurityUserEntry':cmSecurityUserEntry,_I:cmSecurityUserName,_l:cmSecurityUserComment,_m:cmSecurityUserPrivLevel,_n:cmSecurityUserLoginTimeout,_o:cmSecurityUserNumFailedLoginAttempts,_p:cmSecurityUserLastLoginTime,_q:cmSecurityUserLockedout,_r:cmSecurityUserLastLockedoutTime,_s:cmSecurityUserCliPagingEnable,_J:cmSecurityUserRemoteUser,_t:cmSecurityUserPassword,_u:cmSecurityUserStorageType,_v:cmSecurityUserRowStatus,_w:cmSecurityUserAction,_x:cmSecurityCryptoPassword,'cmSecurityUserRemoteCryptoUser':cmSecurityUserRemoteCryptoUser,'cmRemoteAuthServerTable':cmRemoteAuthServerTable,'cmRemoteAuthServerEntry':cmRemoteAuthServerEntry,_K:cmRemoteAuthServerIndex,_y:cmRemoteAuthServerEnabled,_z:cmRemoteAuthServerOrder,_A0:cmRemoteAuthServerIpAddress,_A1:cmRemoteAuthServerPort,_A2:cmRemoteAuthServerNumRetries,_A3:cmRemoteAuthServerTimeout,_A4:cmRemoteAuthServerSecret,_A5:cmRemoteAuthServerAccountingPort,_A6:cmRemoteAuthServerIpVersion,_A7:cmRemoteAuthServerIpv6Addr,_e:cmSecurityPolicyStrength,_f:cmRemoteAuthServerAccountingEnabled,'f3UsmUserTable':f3UsmUserTable,_Z:f3UsmUserEntry,_A8:f3UsmUserAccessType,_g:f3TacacsPrivLevelControlEnabled,_h:f3TacacsDefaultPrivLevel,_i:f3NasIpv6Addr,_j:f3SecurityTrapType,_k:f3SecurityTrapInfo,'f3PrivilegeChangeTable':f3PrivilegeChangeTable,'f3PrivilegeChangeEntry':f3PrivilegeChangeEntry,_X:f3PrivilegeChangeId,_L:f3PrivilegeChangeUserName,_M:f3PrivilegeChangeIpv4Address,_N:f3PrivilegeChangeIpv6Address,_O:f3PrivilegeChangeTerminalIpv4Address,_P:f3PrivilegeChangeTerminalIpv6Address,_Q:f3PrivilegeChangeInterface,_R:f3PrivilegeChangeCurrentPrivilege,_S:f3PrivilegeChangeRequestedPrivilege,_T:f3PrivilegeChangeDuration,_A9:f3PrivilegeChangeAction,_U:f3PrivilegeChangeState,_AA:f3PrivilegeChangeRemainingTime,_AB:f3PrivilegeChangeRemoteName,'f3UserPrivMgmtControl':f3UserPrivMgmtControl,'f3UserPrivRspTimeout':f3UserPrivRspTimeout,'cmSecurityConformance':cmSecurityConformance,'cmSecurityCompliances':cmSecurityCompliances,'cmSecurityCompliance':cmSecurityCompliance,'cmSecurityGroups':cmSecurityGroups,_AD:cmSecurityObjectGroup,'cmSecurityNotifGroup':cmSecurityNotifGroup,'cmSecurityNotifications':cmSecurityNotifications,_AC:f3SecurityTrap,'f3PrivilegeChangeTrap':f3PrivilegeChangeTrap})