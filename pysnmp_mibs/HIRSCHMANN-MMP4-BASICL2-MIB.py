_Aa='initialize'
_AZ='hmAgentDot1xClientMacAddress'
_AY='HmAgentDot1xSessionTerminationAction'
_AX='voiceVlan'
_AW='guestVlan'
_AV='unauthenticatedVlan'
_AU='HmAgentDot1xPortControlMode'
_AT='hmAgentLogHostTableIndex'
_AS='hmAgentRadiusServerIndex'
_AR='hmAgentRadiusAccountingServerIndex'
_AQ='hmAgentClassOfServicePortPriority'
_AP='designated'
_AO='alternate'
_AN='notParticipate'
_AM='manualFwd'
_AL='discarding'
_AK='hmAgentProtocolGroupPortIfIndex'
_AJ='full-1000sx'
_AI='full-100fx'
_AH='half-100fx'
_AG='auto-negotiate'
_AF='hmAgentPortDot1dBasePort'
_AE='hmAgentDot3adAggPort'
_AD='hmAgentPortMirrorSessionNum'
_AC='transferFailed'
_AB='transferSuccessful'
_AA='unknownDirection'
_A9='failedCRC'
_A8='checkingCRC'
_A7='failureWritingToFlash'
_A6='writingToFlash'
_A5='invalidConfigFile'
_A4='updatingConfig'
_A3='wrongFileType'
_A2='errorStarting'
_A1='transferStarting'
_A0='clibanner'
_z='hmAgentSwitchVoiceVlanDeviceMacAddress'
_y='hmAgentSwitchVoiceVlanInterfaceNum'
_x='hmAgentSwitchMFDBSummaryMacAddress'
_w='hmAgentSwitchMFDBSummaryVlanId'
_v='hmAgentSwitchMFDBProtocolType'
_u='hmAgentSwitchMFDBMacAddress'
_t='hmAgentSwitchMFDBVlanId'
_s='HmAgentPortMask'
_r='hmAgentSwitchStaticMacFilteringAddress'
_q='hmAgentSwitchStaticMacFilteringVlanId'
_p='active'
_o='hmAgentLagDetailedIfIndex'
_n='hmAgentLagDetailedLagIndex'
_m='dynamic'
_l='hmAgentLagSummaryLagIndex'
_k='enabled'
_j='hmAgentUserIndex'
_i='hmAgentLoginSessionIndex'
_h='hmAgentTrapLogIndex'
_g='IpAddress'
_f='dot1qFdbId'
_e='HmAgentLogSeverity'
_d='hmAgentProtocolGroupId'
_c='forwarding'
_b='learning'
_a='notInitiated'
_Z='static'
_Y='none'
_X='default'
_W='dot1xPaePortNumber'
_V='IEEE8021-PAE-MIB'
_U='ifIndex'
_T='IF-MIB'
_S='hmAgentStpMstId'
_R='not-accessible'
_Q='dot1qVlanIndex'
_P='disabled'
_O='Q-BRIDGE-MIB'
_N='true'
_M='false'
_L='OctetString'
_K='read-create'
_J='obsolete'
_I='DisplayString'
_H='Unsigned32'
_G='HIRSCHMANN-MMP4-BASICL2-MIB'
_F='enable'
_E='disable'
_D='Integer32'
_C='read-only'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_L,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
HmAgentLogSeverity,hirschmann=mibBuilder.importSymbols('HMPRIV-MGMT-SNMP-MIB',_e,'hirschmann')
IANAifType,=mibBuilder.importSymbols('IANAifType-MIB','IANAifType')
dot1xPaePortNumber,=mibBuilder.importSymbols(_V,_W)
ifIndex,=mibBuilder.importSymbols(_T,_U)
InetAddress,=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress')
VlanIndex,dot1qFdbId,dot1qVlanIndex=mibBuilder.importSymbols(_O,'VlanIndex',_f,_Q)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,_g,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_I,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
hmPlatform4BasicL2=ModuleIdentity((1,3,6,1,4,1,248,15,1))
if mibBuilder.loadTexts:hmPlatform4BasicL2.setRevisions(('2005-11-22 12:00','2005-08-18 12:00','2004-07-02 00:00'))
class HmAgentPortMask(TextualConvention,OctetString):status=_A
class BridgeId(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
class HmAgentDot1xPortControlMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('forceUnauthorized',1),('auto',2),('forceAuthorized',3),('macBased',4)))
class HmAgentDot1xSessionTerminationAction(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_X,1),('reauthenticate',2)))
_HmPlatform4_ObjectIdentity=ObjectIdentity
hmPlatform4=_HmPlatform4_ObjectIdentity((1,3,6,1,4,1,248,15))
_HmAgentInfoGroup_ObjectIdentity=ObjectIdentity
hmAgentInfoGroup=_HmAgentInfoGroup_ObjectIdentity((1,3,6,1,4,1,248,15,1,1))
_HmAgentTrapLogGroup_ObjectIdentity=ObjectIdentity
hmAgentTrapLogGroup=_HmAgentTrapLogGroup_ObjectIdentity((1,3,6,1,4,1,248,15,1,1,2))
_HmAgentTrapLogTotal_Type=Integer32
_HmAgentTrapLogTotal_Object=MibScalar
hmAgentTrapLogTotal=_HmAgentTrapLogTotal_Object((1,3,6,1,4,1,248,15,1,1,2,1),_HmAgentTrapLogTotal_Type())
hmAgentTrapLogTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentTrapLogTotal.setStatus(_A)
_HmAgentTrapLogTotalSinceLastViewed_Type=Integer32
_HmAgentTrapLogTotalSinceLastViewed_Object=MibScalar
hmAgentTrapLogTotalSinceLastViewed=_HmAgentTrapLogTotalSinceLastViewed_Object((1,3,6,1,4,1,248,15,1,1,2,3),_HmAgentTrapLogTotalSinceLastViewed_Type())
hmAgentTrapLogTotalSinceLastViewed.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentTrapLogTotalSinceLastViewed.setStatus('deprecated')
_HmAgentTrapLogTable_Object=MibTable
hmAgentTrapLogTable=_HmAgentTrapLogTable_Object((1,3,6,1,4,1,248,15,1,1,2,4))
if mibBuilder.loadTexts:hmAgentTrapLogTable.setStatus(_A)
_HmAgentTrapLogEntry_Object=MibTableRow
hmAgentTrapLogEntry=_HmAgentTrapLogEntry_Object((1,3,6,1,4,1,248,15,1,1,2,4,1))
hmAgentTrapLogEntry.setIndexNames((0,_G,_h))
if mibBuilder.loadTexts:hmAgentTrapLogEntry.setStatus(_A)
_HmAgentTrapLogIndex_Type=Integer32
_HmAgentTrapLogIndex_Object=MibTableColumn
hmAgentTrapLogIndex=_HmAgentTrapLogIndex_Object((1,3,6,1,4,1,248,15,1,1,2,4,1,1),_HmAgentTrapLogIndex_Type())
hmAgentTrapLogIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentTrapLogIndex.setStatus(_A)
_HmAgentTrapLogSystemTime_Type=DisplayString
_HmAgentTrapLogSystemTime_Object=MibTableColumn
hmAgentTrapLogSystemTime=_HmAgentTrapLogSystemTime_Object((1,3,6,1,4,1,248,15,1,1,2,4,1,2),_HmAgentTrapLogSystemTime_Type())
hmAgentTrapLogSystemTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentTrapLogSystemTime.setStatus(_A)
class _HmAgentTrapLogTrap_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_HmAgentTrapLogTrap_Type.__name__=_I
_HmAgentTrapLogTrap_Object=MibTableColumn
hmAgentTrapLogTrap=_HmAgentTrapLogTrap_Object((1,3,6,1,4,1,248,15,1,1,2,4,1,3),_HmAgentTrapLogTrap_Type())
hmAgentTrapLogTrap.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentTrapLogTrap.setStatus(_A)
_HmAgentConfigGroup_ObjectIdentity=ObjectIdentity
hmAgentConfigGroup=_HmAgentConfigGroup_ObjectIdentity((1,3,6,1,4,1,248,15,1,2))
_HmAgentCLIConfigGroup_ObjectIdentity=ObjectIdentity
hmAgentCLIConfigGroup=_HmAgentCLIConfigGroup_ObjectIdentity((1,3,6,1,4,1,248,15,1,2,1))
_HmAgentLoginSessionTable_Object=MibTable
hmAgentLoginSessionTable=_HmAgentLoginSessionTable_Object((1,3,6,1,4,1,248,15,1,2,1,1))
if mibBuilder.loadTexts:hmAgentLoginSessionTable.setStatus(_A)
_HmAgentLoginSessionEntry_Object=MibTableRow
hmAgentLoginSessionEntry=_HmAgentLoginSessionEntry_Object((1,3,6,1,4,1,248,15,1,2,1,1,1))
hmAgentLoginSessionEntry.setIndexNames((0,_G,_i))
if mibBuilder.loadTexts:hmAgentLoginSessionEntry.setStatus(_A)
_HmAgentLoginSessionIndex_Type=Integer32
_HmAgentLoginSessionIndex_Object=MibTableColumn
hmAgentLoginSessionIndex=_HmAgentLoginSessionIndex_Object((1,3,6,1,4,1,248,15,1,2,1,1,1,1),_HmAgentLoginSessionIndex_Type())
hmAgentLoginSessionIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentLoginSessionIndex.setStatus(_A)
_HmAgentLoginSessionUserName_Type=DisplayString
_HmAgentLoginSessionUserName_Object=MibTableColumn
hmAgentLoginSessionUserName=_HmAgentLoginSessionUserName_Object((1,3,6,1,4,1,248,15,1,2,1,1,1,2),_HmAgentLoginSessionUserName_Type())
hmAgentLoginSessionUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentLoginSessionUserName.setStatus(_A)
_HmAgentLoginSessionIPAddress_Type=IpAddress
_HmAgentLoginSessionIPAddress_Object=MibTableColumn
hmAgentLoginSessionIPAddress=_HmAgentLoginSessionIPAddress_Object((1,3,6,1,4,1,248,15,1,2,1,1,1,3),_HmAgentLoginSessionIPAddress_Type())
hmAgentLoginSessionIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentLoginSessionIPAddress.setStatus(_A)
class _HmAgentLoginSessionConnectionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('serial',1),('telnet',2)))
_HmAgentLoginSessionConnectionType_Type.__name__=_D
_HmAgentLoginSessionConnectionType_Object=MibTableColumn
hmAgentLoginSessionConnectionType=_HmAgentLoginSessionConnectionType_Object((1,3,6,1,4,1,248,15,1,2,1,1,1,4),_HmAgentLoginSessionConnectionType_Type())
hmAgentLoginSessionConnectionType.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentLoginSessionConnectionType.setStatus(_A)
_HmAgentLoginSessionIdleTime_Type=TimeTicks
_HmAgentLoginSessionIdleTime_Object=MibTableColumn
hmAgentLoginSessionIdleTime=_HmAgentLoginSessionIdleTime_Object((1,3,6,1,4,1,248,15,1,2,1,1,1,5),_HmAgentLoginSessionIdleTime_Type())
hmAgentLoginSessionIdleTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentLoginSessionIdleTime.setStatus(_A)
_HmAgentLoginSessionSessionTime_Type=TimeTicks
_HmAgentLoginSessionSessionTime_Object=MibTableColumn
hmAgentLoginSessionSessionTime=_HmAgentLoginSessionSessionTime_Object((1,3,6,1,4,1,248,15,1,2,1,1,1,6),_HmAgentLoginSessionSessionTime_Type())
hmAgentLoginSessionSessionTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentLoginSessionSessionTime.setStatus(_A)
_HmAgentLoginSessionStatus_Type=RowStatus
_HmAgentLoginSessionStatus_Object=MibTableColumn
hmAgentLoginSessionStatus=_HmAgentLoginSessionStatus_Object((1,3,6,1,4,1,248,15,1,2,1,1,1,7),_HmAgentLoginSessionStatus_Type())
hmAgentLoginSessionStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentLoginSessionStatus.setStatus(_A)
_HmAgentTelnetConfigGroup_ObjectIdentity=ObjectIdentity
hmAgentTelnetConfigGroup=_HmAgentTelnetConfigGroup_ObjectIdentity((1,3,6,1,4,1,248,15,1,2,1,2))
class _HmAgentTelnetLoginTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,160))
_HmAgentTelnetLoginTimeout_Type.__name__=_D
_HmAgentTelnetLoginTimeout_Object=MibScalar
hmAgentTelnetLoginTimeout=_HmAgentTelnetLoginTimeout_Object((1,3,6,1,4,1,248,15,1,2,1,2,1),_HmAgentTelnetLoginTimeout_Type())
hmAgentTelnetLoginTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentTelnetLoginTimeout.setStatus(_A)
class _HmAgentTelnetMaxSessions_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_HmAgentTelnetMaxSessions_Type.__name__=_D
_HmAgentTelnetMaxSessions_Object=MibScalar
hmAgentTelnetMaxSessions=_HmAgentTelnetMaxSessions_Object((1,3,6,1,4,1,248,15,1,2,1,2,2),_HmAgentTelnetMaxSessions_Type())
hmAgentTelnetMaxSessions.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentTelnetMaxSessions.setStatus(_A)
class _HmAgentTelnetAllowNewMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HmAgentTelnetAllowNewMode_Type.__name__=_D
_HmAgentTelnetAllowNewMode_Object=MibScalar
hmAgentTelnetAllowNewMode=_HmAgentTelnetAllowNewMode_Object((1,3,6,1,4,1,248,15,1,2,1,2,3),_HmAgentTelnetAllowNewMode_Type())
hmAgentTelnetAllowNewMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentTelnetAllowNewMode.setStatus(_A)
_HmAgentUserConfigGroup_ObjectIdentity=ObjectIdentity
hmAgentUserConfigGroup=_HmAgentUserConfigGroup_ObjectIdentity((1,3,6,1,4,1,248,15,1,2,1,3))
class _HmAgentUserConfigCreate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HmAgentUserConfigCreate_Type.__name__=_I
_HmAgentUserConfigCreate_Object=MibScalar
hmAgentUserConfigCreate=_HmAgentUserConfigCreate_Object((1,3,6,1,4,1,248,15,1,2,1,3,1),_HmAgentUserConfigCreate_Type())
hmAgentUserConfigCreate.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentUserConfigCreate.setStatus(_A)
_HmAgentUserConfigTable_Object=MibTable
hmAgentUserConfigTable=_HmAgentUserConfigTable_Object((1,3,6,1,4,1,248,15,1,2,1,3,2))
if mibBuilder.loadTexts:hmAgentUserConfigTable.setStatus(_A)
_HmAgentUserConfigEntry_Object=MibTableRow
hmAgentUserConfigEntry=_HmAgentUserConfigEntry_Object((1,3,6,1,4,1,248,15,1,2,1,3,2,1))
hmAgentUserConfigEntry.setIndexNames((0,_G,_j))
if mibBuilder.loadTexts:hmAgentUserConfigEntry.setStatus(_A)
_HmAgentUserIndex_Type=Integer32
_HmAgentUserIndex_Object=MibTableColumn
hmAgentUserIndex=_HmAgentUserIndex_Object((1,3,6,1,4,1,248,15,1,2,1,3,2,1,1),_HmAgentUserIndex_Type())
hmAgentUserIndex.setMaxAccess(_R)
if mibBuilder.loadTexts:hmAgentUserIndex.setStatus(_A)
class _HmAgentUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HmAgentUserName_Type.__name__=_I
_HmAgentUserName_Object=MibTableColumn
hmAgentUserName=_HmAgentUserName_Object((1,3,6,1,4,1,248,15,1,2,1,3,2,1,2),_HmAgentUserName_Type())
hmAgentUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentUserName.setStatus(_A)
class _HmAgentUserPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HmAgentUserPassword_Type.__name__=_I
_HmAgentUserPassword_Object=MibTableColumn
hmAgentUserPassword=_HmAgentUserPassword_Object((1,3,6,1,4,1,248,15,1,2,1,3,2,1,3),_HmAgentUserPassword_Type())
hmAgentUserPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentUserPassword.setStatus(_A)
class _HmAgentUserAccessMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('read',1),('write',2)))
_HmAgentUserAccessMode_Type.__name__=_D
_HmAgentUserAccessMode_Object=MibTableColumn
hmAgentUserAccessMode=_HmAgentUserAccessMode_Object((1,3,6,1,4,1,248,15,1,2,1,3,2,1,4),_HmAgentUserAccessMode_Type())
hmAgentUserAccessMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentUserAccessMode.setStatus(_A)
_HmAgentUserStatus_Type=RowStatus
_HmAgentUserStatus_Object=MibTableColumn
hmAgentUserStatus=_HmAgentUserStatus_Object((1,3,6,1,4,1,248,15,1,2,1,3,2,1,5),_HmAgentUserStatus_Type())
hmAgentUserStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentUserStatus.setStatus(_A)
class _HmAgentUserAuthenticationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Y,1),('hmacmd5',2),('hmacsha',3)))
_HmAgentUserAuthenticationType_Type.__name__=_D
_HmAgentUserAuthenticationType_Object=MibTableColumn
hmAgentUserAuthenticationType=_HmAgentUserAuthenticationType_Object((1,3,6,1,4,1,248,15,1,2,1,3,2,1,6),_HmAgentUserAuthenticationType_Type())
hmAgentUserAuthenticationType.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentUserAuthenticationType.setStatus(_A)
class _HmAgentUserEncryptionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Y,1),('des',2)))
_HmAgentUserEncryptionType_Type.__name__=_D
_HmAgentUserEncryptionType_Object=MibTableColumn
hmAgentUserEncryptionType=_HmAgentUserEncryptionType_Object((1,3,6,1,4,1,248,15,1,2,1,3,2,1,7),_HmAgentUserEncryptionType_Type())
hmAgentUserEncryptionType.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentUserEncryptionType.setStatus(_A)
class _HmAgentUserEncryptionPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,64))
_HmAgentUserEncryptionPassword_Type.__name__=_I
_HmAgentUserEncryptionPassword_Object=MibTableColumn
hmAgentUserEncryptionPassword=_HmAgentUserEncryptionPassword_Object((1,3,6,1,4,1,248,15,1,2,1,3,2,1,8),_HmAgentUserEncryptionPassword_Type())
hmAgentUserEncryptionPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentUserEncryptionPassword.setStatus(_A)
_HmAgentUserDefaultPwdActive_Type=TruthValue
_HmAgentUserDefaultPwdActive_Object=MibScalar
hmAgentUserDefaultPwdActive=_HmAgentUserDefaultPwdActive_Object((1,3,6,1,4,1,248,15,1,2,1,3,248),_HmAgentUserDefaultPwdActive_Type())
hmAgentUserDefaultPwdActive.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentUserDefaultPwdActive.setStatus(_A)
class _HmAgentConfigEncryptionSecret_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_HmAgentConfigEncryptionSecret_Type.__name__=_I
_HmAgentConfigEncryptionSecret_Object=MibScalar
hmAgentConfigEncryptionSecret=_HmAgentConfigEncryptionSecret_Object((1,3,6,1,4,1,248,15,1,2,1,250),_HmAgentConfigEncryptionSecret_Type())
hmAgentConfigEncryptionSecret.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentConfigEncryptionSecret.setStatus(_A)
class _HmAgentConfigEncryptionStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_k,1),(_P,2)))
_HmAgentConfigEncryptionStatus_Type.__name__=_D
_HmAgentConfigEncryptionStatus_Object=MibScalar
hmAgentConfigEncryptionStatus=_HmAgentConfigEncryptionStatus_Object((1,3,6,1,4,1,248,15,1,2,1,251),_HmAgentConfigEncryptionStatus_Type())
hmAgentConfigEncryptionStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentConfigEncryptionStatus.setStatus(_A)
_HmAgentLagConfigGroup_ObjectIdentity=ObjectIdentity
hmAgentLagConfigGroup=_HmAgentLagConfigGroup_ObjectIdentity((1,3,6,1,4,1,248,15,1,2,2))
class _HmAgentLagConfigCreate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(1,15))
_HmAgentLagConfigCreate_Type.__name__=_I
_HmAgentLagConfigCreate_Object=MibScalar
hmAgentLagConfigCreate=_HmAgentLagConfigCreate_Object((1,3,6,1,4,1,248,15,1,2,2,1),_HmAgentLagConfigCreate_Type())
hmAgentLagConfigCreate.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentLagConfigCreate.setStatus(_A)
_HmAgentLagSummaryConfigTable_Object=MibTable
hmAgentLagSummaryConfigTable=_HmAgentLagSummaryConfigTable_Object((1,3,6,1,4,1,248,15,1,2,2,2))
if mibBuilder.loadTexts:hmAgentLagSummaryConfigTable.setStatus(_A)
_HmAgentLagSummaryConfigEntry_Object=MibTableRow
hmAgentLagSummaryConfigEntry=_HmAgentLagSummaryConfigEntry_Object((1,3,6,1,4,1,248,15,1,2,2,2,1))
hmAgentLagSummaryConfigEntry.setIndexNames((0,_G,_l))
if mibBuilder.loadTexts:hmAgentLagSummaryConfigEntry.setStatus(_A)
_HmAgentLagSummaryLagIndex_Type=Integer32
_HmAgentLagSummaryLagIndex_Object=MibTableColumn
hmAgentLagSummaryLagIndex=_HmAgentLagSummaryLagIndex_Object((1,3,6,1,4,1,248,15,1,2,2,2,1,1),_HmAgentLagSummaryLagIndex_Type())
hmAgentLagSummaryLagIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentLagSummaryLagIndex.setStatus(_A)
class _HmAgentLagSummaryName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_HmAgentLagSummaryName_Type.__name__=_I
_HmAgentLagSummaryName_Object=MibTableColumn
hmAgentLagSummaryName=_HmAgentLagSummaryName_Object((1,3,6,1,4,1,248,15,1,2,2,2,1,2),_HmAgentLagSummaryName_Type())
hmAgentLagSummaryName.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentLagSummaryName.setStatus(_A)
_HmAgentLagSummaryFlushTimer_Type=Integer32
_HmAgentLagSummaryFlushTimer_Object=MibTableColumn
hmAgentLagSummaryFlushTimer=_HmAgentLagSummaryFlushTimer_Object((1,3,6,1,4,1,248,15,1,2,2,2,1,3),_HmAgentLagSummaryFlushTimer_Type())
hmAgentLagSummaryFlushTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentLagSummaryFlushTimer.setStatus(_J)
class _HmAgentLagSummaryLinkTrap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HmAgentLagSummaryLinkTrap_Type.__name__=_D
_HmAgentLagSummaryLinkTrap_Object=MibTableColumn
hmAgentLagSummaryLinkTrap=_HmAgentLagSummaryLinkTrap_Object((1,3,6,1,4,1,248,15,1,2,2,2,1,4),_HmAgentLagSummaryLinkTrap_Type())
hmAgentLagSummaryLinkTrap.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentLagSummaryLinkTrap.setStatus(_A)
class _HmAgentLagSummaryAdminMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HmAgentLagSummaryAdminMode_Type.__name__=_D
_HmAgentLagSummaryAdminMode_Object=MibTableColumn
hmAgentLagSummaryAdminMode=_HmAgentLagSummaryAdminMode_Object((1,3,6,1,4,1,248,15,1,2,2,2,1,5),_HmAgentLagSummaryAdminMode_Type())
hmAgentLagSummaryAdminMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentLagSummaryAdminMode.setStatus(_A)
class _HmAgentLagSummaryStpMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4)));namedValues=NamedValues(*(('off',3),('on',4)))
_HmAgentLagSummaryStpMode_Type.__name__=_D
_HmAgentLagSummaryStpMode_Object=MibTableColumn
hmAgentLagSummaryStpMode=_HmAgentLagSummaryStpMode_Object((1,3,6,1,4,1,248,15,1,2,2,2,1,6),_HmAgentLagSummaryStpMode_Type())
hmAgentLagSummaryStpMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentLagSummaryStpMode.setStatus(_A)
_HmAgentLagSummaryAddPort_Type=Integer32
_HmAgentLagSummaryAddPort_Object=MibTableColumn
hmAgentLagSummaryAddPort=_HmAgentLagSummaryAddPort_Object((1,3,6,1,4,1,248,15,1,2,2,2,1,7),_HmAgentLagSummaryAddPort_Type())
hmAgentLagSummaryAddPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentLagSummaryAddPort.setStatus(_A)
_HmAgentLagSummaryDeletePort_Type=Integer32
_HmAgentLagSummaryDeletePort_Object=MibTableColumn
hmAgentLagSummaryDeletePort=_HmAgentLagSummaryDeletePort_Object((1,3,6,1,4,1,248,15,1,2,2,2,1,8),_HmAgentLagSummaryDeletePort_Type())
hmAgentLagSummaryDeletePort.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentLagSummaryDeletePort.setStatus(_A)
_HmAgentLagSummaryStatus_Type=RowStatus
_HmAgentLagSummaryStatus_Object=MibTableColumn
hmAgentLagSummaryStatus=_HmAgentLagSummaryStatus_Object((1,3,6,1,4,1,248,15,1,2,2,2,1,9),_HmAgentLagSummaryStatus_Type())
hmAgentLagSummaryStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentLagSummaryStatus.setStatus(_A)
class _HmAgentLagSummaryType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Z,1),(_m,2)))
_HmAgentLagSummaryType_Type.__name__=_D
_HmAgentLagSummaryType_Object=MibTableColumn
hmAgentLagSummaryType=_HmAgentLagSummaryType_Object((1,3,6,1,4,1,248,15,1,2,2,2,1,10),_HmAgentLagSummaryType_Type())
hmAgentLagSummaryType.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentLagSummaryType.setStatus(_A)
_HmAgentLagDetailedConfigTable_Object=MibTable
hmAgentLagDetailedConfigTable=_HmAgentLagDetailedConfigTable_Object((1,3,6,1,4,1,248,15,1,2,2,3))
if mibBuilder.loadTexts:hmAgentLagDetailedConfigTable.setStatus(_A)
_HmAgentLagDetailedConfigEntry_Object=MibTableRow
hmAgentLagDetailedConfigEntry=_HmAgentLagDetailedConfigEntry_Object((1,3,6,1,4,1,248,15,1,2,2,3,1))
hmAgentLagDetailedConfigEntry.setIndexNames((0,_G,_n),(0,_G,_o))
if mibBuilder.loadTexts:hmAgentLagDetailedConfigEntry.setStatus(_A)
_HmAgentLagDetailedLagIndex_Type=Integer32
_HmAgentLagDetailedLagIndex_Object=MibTableColumn
hmAgentLagDetailedLagIndex=_HmAgentLagDetailedLagIndex_Object((1,3,6,1,4,1,248,15,1,2,2,3,1,1),_HmAgentLagDetailedLagIndex_Type())
hmAgentLagDetailedLagIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentLagDetailedLagIndex.setStatus(_A)
_HmAgentLagDetailedIfIndex_Type=Integer32
_HmAgentLagDetailedIfIndex_Object=MibTableColumn
hmAgentLagDetailedIfIndex=_HmAgentLagDetailedIfIndex_Object((1,3,6,1,4,1,248,15,1,2,2,3,1,2),_HmAgentLagDetailedIfIndex_Type())
hmAgentLagDetailedIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentLagDetailedIfIndex.setStatus(_A)
_HmAgentLagDetailedPortSpeed_Type=ObjectIdentifier
_HmAgentLagDetailedPortSpeed_Object=MibTableColumn
hmAgentLagDetailedPortSpeed=_HmAgentLagDetailedPortSpeed_Object((1,3,6,1,4,1,248,15,1,2,2,3,1,3),_HmAgentLagDetailedPortSpeed_Type())
hmAgentLagDetailedPortSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentLagDetailedPortSpeed.setStatus(_A)
class _HmAgentLagDetailedPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_p,1),('inactive',2)))
_HmAgentLagDetailedPortStatus_Type.__name__=_D
_HmAgentLagDetailedPortStatus_Object=MibTableColumn
hmAgentLagDetailedPortStatus=_HmAgentLagDetailedPortStatus_Object((1,3,6,1,4,1,248,15,1,2,2,3,1,4),_HmAgentLagDetailedPortStatus_Type())
hmAgentLagDetailedPortStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentLagDetailedPortStatus.setStatus(_A)
class _HmAgentLagConfigStaticCapability_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HmAgentLagConfigStaticCapability_Type.__name__=_D
_HmAgentLagConfigStaticCapability_Object=MibScalar
hmAgentLagConfigStaticCapability=_HmAgentLagConfigStaticCapability_Object((1,3,6,1,4,1,248,15,1,2,2,4),_HmAgentLagConfigStaticCapability_Type())
hmAgentLagConfigStaticCapability.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentLagConfigStaticCapability.setStatus(_A)
_HmAgentSpanningTreeConfigGroup_ObjectIdentity=ObjectIdentity
hmAgentSpanningTreeConfigGroup=_HmAgentSpanningTreeConfigGroup_ObjectIdentity((1,3,6,1,4,1,248,15,1,2,7))
class _HmAgentSpanningTreeMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HmAgentSpanningTreeMode_Type.__name__=_D
_HmAgentSpanningTreeMode_Object=MibScalar
hmAgentSpanningTreeMode=_HmAgentSpanningTreeMode_Object((1,3,6,1,4,1,248,15,1,2,7,1),_HmAgentSpanningTreeMode_Type())
hmAgentSpanningTreeMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentSpanningTreeMode.setStatus(_A)
_HmAgentSwitchConfigGroup_ObjectIdentity=ObjectIdentity
hmAgentSwitchConfigGroup=_HmAgentSwitchConfigGroup_ObjectIdentity((1,3,6,1,4,1,248,15,1,2,8))
class _HmAgentSwitchBroadcastControlMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HmAgentSwitchBroadcastControlMode_Type.__name__=_D
_HmAgentSwitchBroadcastControlMode_Object=MibScalar
hmAgentSwitchBroadcastControlMode=_HmAgentSwitchBroadcastControlMode_Object((1,3,6,1,4,1,248,15,1,2,8,2),_HmAgentSwitchBroadcastControlMode_Type())
hmAgentSwitchBroadcastControlMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentSwitchBroadcastControlMode.setStatus(_A)
class _HmAgentSwitchDot3FlowControlMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HmAgentSwitchDot3FlowControlMode_Type.__name__=_D
_HmAgentSwitchDot3FlowControlMode_Object=MibScalar
hmAgentSwitchDot3FlowControlMode=_HmAgentSwitchDot3FlowControlMode_Object((1,3,6,1,4,1,248,15,1,2,8,3),_HmAgentSwitchDot3FlowControlMode_Type())
hmAgentSwitchDot3FlowControlMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentSwitchDot3FlowControlMode.setStatus(_A)
_HmAgentSwitchAddressAgingTimeoutTable_Object=MibTable
hmAgentSwitchAddressAgingTimeoutTable=_HmAgentSwitchAddressAgingTimeoutTable_Object((1,3,6,1,4,1,248,15,1,2,8,4))
if mibBuilder.loadTexts:hmAgentSwitchAddressAgingTimeoutTable.setStatus(_A)
_HmAgentSwitchAddressAgingTimeoutEntry_Object=MibTableRow
hmAgentSwitchAddressAgingTimeoutEntry=_HmAgentSwitchAddressAgingTimeoutEntry_Object((1,3,6,1,4,1,248,15,1,2,8,4,1))
hmAgentSwitchAddressAgingTimeoutEntry.setIndexNames((0,_O,_f))
if mibBuilder.loadTexts:hmAgentSwitchAddressAgingTimeoutEntry.setStatus(_A)
class _HmAgentSwitchAddressAgingTimeout_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,1000000))
_HmAgentSwitchAddressAgingTimeout_Type.__name__=_D
_HmAgentSwitchAddressAgingTimeout_Object=MibTableColumn
hmAgentSwitchAddressAgingTimeout=_HmAgentSwitchAddressAgingTimeout_Object((1,3,6,1,4,1,248,15,1,2,8,4,1,1),_HmAgentSwitchAddressAgingTimeout_Type())
hmAgentSwitchAddressAgingTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentSwitchAddressAgingTimeout.setStatus(_A)
_HmAgentSwitchStaticMacFilteringTable_Object=MibTable
hmAgentSwitchStaticMacFilteringTable=_HmAgentSwitchStaticMacFilteringTable_Object((1,3,6,1,4,1,248,15,1,2,8,5))
if mibBuilder.loadTexts:hmAgentSwitchStaticMacFilteringTable.setStatus(_A)
_HmAgentSwitchStaticMacFilteringEntry_Object=MibTableRow
hmAgentSwitchStaticMacFilteringEntry=_HmAgentSwitchStaticMacFilteringEntry_Object((1,3,6,1,4,1,248,15,1,2,8,5,1))
hmAgentSwitchStaticMacFilteringEntry.setIndexNames((0,_G,_q),(0,_G,_r))
if mibBuilder.loadTexts:hmAgentSwitchStaticMacFilteringEntry.setStatus(_A)
_HmAgentSwitchStaticMacFilteringVlanId_Type=Integer32
_HmAgentSwitchStaticMacFilteringVlanId_Object=MibTableColumn
hmAgentSwitchStaticMacFilteringVlanId=_HmAgentSwitchStaticMacFilteringVlanId_Object((1,3,6,1,4,1,248,15,1,2,8,5,1,1),_HmAgentSwitchStaticMacFilteringVlanId_Type())
hmAgentSwitchStaticMacFilteringVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentSwitchStaticMacFilteringVlanId.setStatus(_A)
_HmAgentSwitchStaticMacFilteringAddress_Type=MacAddress
_HmAgentSwitchStaticMacFilteringAddress_Object=MibTableColumn
hmAgentSwitchStaticMacFilteringAddress=_HmAgentSwitchStaticMacFilteringAddress_Object((1,3,6,1,4,1,248,15,1,2,8,5,1,2),_HmAgentSwitchStaticMacFilteringAddress_Type())
hmAgentSwitchStaticMacFilteringAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentSwitchStaticMacFilteringAddress.setStatus(_A)
_HmAgentSwitchStaticMacFilteringSourcePortMask_Type=HmAgentPortMask
_HmAgentSwitchStaticMacFilteringSourcePortMask_Object=MibTableColumn
hmAgentSwitchStaticMacFilteringSourcePortMask=_HmAgentSwitchStaticMacFilteringSourcePortMask_Object((1,3,6,1,4,1,248,15,1,2,8,5,1,3),_HmAgentSwitchStaticMacFilteringSourcePortMask_Type())
hmAgentSwitchStaticMacFilteringSourcePortMask.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentSwitchStaticMacFilteringSourcePortMask.setStatus(_A)
_HmAgentSwitchStaticMacFilteringDestPortMask_Type=HmAgentPortMask
_HmAgentSwitchStaticMacFilteringDestPortMask_Object=MibTableColumn
hmAgentSwitchStaticMacFilteringDestPortMask=_HmAgentSwitchStaticMacFilteringDestPortMask_Object((1,3,6,1,4,1,248,15,1,2,8,5,1,4),_HmAgentSwitchStaticMacFilteringDestPortMask_Type())
hmAgentSwitchStaticMacFilteringDestPortMask.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentSwitchStaticMacFilteringDestPortMask.setStatus(_A)
_HmAgentSwitchStaticMacFilteringStatus_Type=RowStatus
_HmAgentSwitchStaticMacFilteringStatus_Object=MibTableColumn
hmAgentSwitchStaticMacFilteringStatus=_HmAgentSwitchStaticMacFilteringStatus_Object((1,3,6,1,4,1,248,15,1,2,8,5,1,5),_HmAgentSwitchStaticMacFilteringStatus_Type())
hmAgentSwitchStaticMacFilteringStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:hmAgentSwitchStaticMacFilteringStatus.setStatus(_A)
_HmAgentSwitchIGMPSnoopingGroup_ObjectIdentity=ObjectIdentity
hmAgentSwitchIGMPSnoopingGroup=_HmAgentSwitchIGMPSnoopingGroup_ObjectIdentity((1,3,6,1,4,1,248,15,1,2,8,6))
class _HmAgentSwitchIGMPSnoopingAdminMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HmAgentSwitchIGMPSnoopingAdminMode_Type.__name__=_D
_HmAgentSwitchIGMPSnoopingAdminMode_Object=MibScalar
hmAgentSwitchIGMPSnoopingAdminMode=_HmAgentSwitchIGMPSnoopingAdminMode_Object((1,3,6,1,4,1,248,15,1,2,8,6,1),_HmAgentSwitchIGMPSnoopingAdminMode_Type())
hmAgentSwitchIGMPSnoopingAdminMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentSwitchIGMPSnoopingAdminMode.setStatus(_A)
class _HmAgentSwitchIGMPSnoopingGroupMembershipInterval_Type(Integer32):defaultValue=260;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,3600))
_HmAgentSwitchIGMPSnoopingGroupMembershipInterval_Type.__name__=_D
_HmAgentSwitchIGMPSnoopingGroupMembershipInterval_Object=MibScalar
hmAgentSwitchIGMPSnoopingGroupMembershipInterval=_HmAgentSwitchIGMPSnoopingGroupMembershipInterval_Object((1,3,6,1,4,1,248,15,1,2,8,6,2),_HmAgentSwitchIGMPSnoopingGroupMembershipInterval_Type())
hmAgentSwitchIGMPSnoopingGroupMembershipInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentSwitchIGMPSnoopingGroupMembershipInterval.setStatus(_A)
class _HmAgentSwitchIGMPSnoopingMaxResponseTime_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3598))
_HmAgentSwitchIGMPSnoopingMaxResponseTime_Type.__name__=_D
_HmAgentSwitchIGMPSnoopingMaxResponseTime_Object=MibScalar
hmAgentSwitchIGMPSnoopingMaxResponseTime=_HmAgentSwitchIGMPSnoopingMaxResponseTime_Object((1,3,6,1,4,1,248,15,1,2,8,6,3),_HmAgentSwitchIGMPSnoopingMaxResponseTime_Type())
hmAgentSwitchIGMPSnoopingMaxResponseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentSwitchIGMPSnoopingMaxResponseTime.setStatus(_A)
class _HmAgentSwitchIGMPSnoopingMRPExpirationTime_Type(Integer32):defaultValue=260;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_HmAgentSwitchIGMPSnoopingMRPExpirationTime_Type.__name__=_D
_HmAgentSwitchIGMPSnoopingMRPExpirationTime_Object=MibScalar
hmAgentSwitchIGMPSnoopingMRPExpirationTime=_HmAgentSwitchIGMPSnoopingMRPExpirationTime_Object((1,3,6,1,4,1,248,15,1,2,8,6,4),_HmAgentSwitchIGMPSnoopingMRPExpirationTime_Type())
hmAgentSwitchIGMPSnoopingMRPExpirationTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentSwitchIGMPSnoopingMRPExpirationTime.setStatus(_A)
class _HmAgentSwitchIGMPSnoopingPortMask_Type(HmAgentPortMask):defaultHexValue='000000000000'
_HmAgentSwitchIGMPSnoopingPortMask_Type.__name__=_s
_HmAgentSwitchIGMPSnoopingPortMask_Object=MibScalar
hmAgentSwitchIGMPSnoopingPortMask=_HmAgentSwitchIGMPSnoopingPortMask_Object((1,3,6,1,4,1,248,15,1,2,8,6,5),_HmAgentSwitchIGMPSnoopingPortMask_Type())
hmAgentSwitchIGMPSnoopingPortMask.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentSwitchIGMPSnoopingPortMask.setStatus(_A)
_HmAgentSwitchIGMPSnoopingMulticastControlFramesProcessed_Type=Counter32
_HmAgentSwitchIGMPSnoopingMulticastControlFramesProcessed_Object=MibScalar
hmAgentSwitchIGMPSnoopingMulticastControlFramesProcessed=_HmAgentSwitchIGMPSnoopingMulticastControlFramesProcessed_Object((1,3,6,1,4,1,248,15,1,2,8,6,6),_HmAgentSwitchIGMPSnoopingMulticastControlFramesProcessed_Type())
hmAgentSwitchIGMPSnoopingMulticastControlFramesProcessed.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentSwitchIGMPSnoopingMulticastControlFramesProcessed.setStatus(_A)
_HmAgentSwitchMFDBGroup_ObjectIdentity=ObjectIdentity
hmAgentSwitchMFDBGroup=_HmAgentSwitchMFDBGroup_ObjectIdentity((1,3,6,1,4,1,248,15,1,2,8,7))
_HmAgentSwitchMFDBTable_Object=MibTable
hmAgentSwitchMFDBTable=_HmAgentSwitchMFDBTable_Object((1,3,6,1,4,1,248,15,1,2,8,7,1))
if mibBuilder.loadTexts:hmAgentSwitchMFDBTable.setStatus(_A)
_HmAgentSwitchMFDBEntry_Object=MibTableRow
hmAgentSwitchMFDBEntry=_HmAgentSwitchMFDBEntry_Object((1,3,6,1,4,1,248,15,1,2,8,7,1,1))
hmAgentSwitchMFDBEntry.setIndexNames((0,_G,_t),(0,_G,_u),(0,_G,_v))
if mibBuilder.loadTexts:hmAgentSwitchMFDBEntry.setStatus(_A)
_HmAgentSwitchMFDBVlanId_Type=VlanIndex
_HmAgentSwitchMFDBVlanId_Object=MibTableColumn
hmAgentSwitchMFDBVlanId=_HmAgentSwitchMFDBVlanId_Object((1,3,6,1,4,1,248,15,1,2,8,7,1,1,1),_HmAgentSwitchMFDBVlanId_Type())
hmAgentSwitchMFDBVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentSwitchMFDBVlanId.setStatus(_A)
_HmAgentSwitchMFDBMacAddress_Type=MacAddress
_HmAgentSwitchMFDBMacAddress_Object=MibTableColumn
hmAgentSwitchMFDBMacAddress=_HmAgentSwitchMFDBMacAddress_Object((1,3,6,1,4,1,248,15,1,2,8,7,1,1,2),_HmAgentSwitchMFDBMacAddress_Type())
hmAgentSwitchMFDBMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentSwitchMFDBMacAddress.setStatus(_A)
class _HmAgentSwitchMFDBProtocolType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_Z,1),('gmrp',2),('igmp',3),('msd',4)))
_HmAgentSwitchMFDBProtocolType_Type.__name__=_D
_HmAgentSwitchMFDBProtocolType_Object=MibTableColumn
hmAgentSwitchMFDBProtocolType=_HmAgentSwitchMFDBProtocolType_Object((1,3,6,1,4,1,248,15,1,2,8,7,1,1,3),_HmAgentSwitchMFDBProtocolType_Type())
hmAgentSwitchMFDBProtocolType.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentSwitchMFDBProtocolType.setStatus(_A)
class _HmAgentSwitchMFDBType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Z,1),(_m,2)))
_HmAgentSwitchMFDBType_Type.__name__=_D
_HmAgentSwitchMFDBType_Object=MibTableColumn
hmAgentSwitchMFDBType=_HmAgentSwitchMFDBType_Object((1,3,6,1,4,1,248,15,1,2,8,7,1,1,4),_HmAgentSwitchMFDBType_Type())
hmAgentSwitchMFDBType.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentSwitchMFDBType.setStatus(_A)
_HmAgentSwitchMFDBDescription_Type=DisplayString
_HmAgentSwitchMFDBDescription_Object=MibTableColumn
hmAgentSwitchMFDBDescription=_HmAgentSwitchMFDBDescription_Object((1,3,6,1,4,1,248,15,1,2,8,7,1,1,5),_HmAgentSwitchMFDBDescription_Type())
hmAgentSwitchMFDBDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentSwitchMFDBDescription.setStatus(_A)
_HmAgentSwitchMFDBForwardingPortMask_Type=HmAgentPortMask
_HmAgentSwitchMFDBForwardingPortMask_Object=MibTableColumn
hmAgentSwitchMFDBForwardingPortMask=_HmAgentSwitchMFDBForwardingPortMask_Object((1,3,6,1,4,1,248,15,1,2,8,7,1,1,6),_HmAgentSwitchMFDBForwardingPortMask_Type())
hmAgentSwitchMFDBForwardingPortMask.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentSwitchMFDBForwardingPortMask.setStatus(_A)
_HmAgentSwitchMFDBFilteringPortMask_Type=HmAgentPortMask
_HmAgentSwitchMFDBFilteringPortMask_Object=MibTableColumn
hmAgentSwitchMFDBFilteringPortMask=_HmAgentSwitchMFDBFilteringPortMask_Object((1,3,6,1,4,1,248,15,1,2,8,7,1,1,7),_HmAgentSwitchMFDBFilteringPortMask_Type())
hmAgentSwitchMFDBFilteringPortMask.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentSwitchMFDBFilteringPortMask.setStatus(_A)
_HmAgentSwitchMFDBSummaryTable_Object=MibTable
hmAgentSwitchMFDBSummaryTable=_HmAgentSwitchMFDBSummaryTable_Object((1,3,6,1,4,1,248,15,1,2,8,7,2))
if mibBuilder.loadTexts:hmAgentSwitchMFDBSummaryTable.setStatus(_A)
_HmAgentSwitchMFDBSummaryEntry_Object=MibTableRow
hmAgentSwitchMFDBSummaryEntry=_HmAgentSwitchMFDBSummaryEntry_Object((1,3,6,1,4,1,248,15,1,2,8,7,2,1))
hmAgentSwitchMFDBSummaryEntry.setIndexNames((0,_G,_w),(0,_G,_x))
if mibBuilder.loadTexts:hmAgentSwitchMFDBSummaryEntry.setStatus(_A)
_HmAgentSwitchMFDBSummaryVlanId_Type=VlanIndex
_HmAgentSwitchMFDBSummaryVlanId_Object=MibTableColumn
hmAgentSwitchMFDBSummaryVlanId=_HmAgentSwitchMFDBSummaryVlanId_Object((1,3,6,1,4,1,248,15,1,2,8,7,2,1,1),_HmAgentSwitchMFDBSummaryVlanId_Type())
hmAgentSwitchMFDBSummaryVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentSwitchMFDBSummaryVlanId.setStatus(_A)
_HmAgentSwitchMFDBSummaryMacAddress_Type=MacAddress
_HmAgentSwitchMFDBSummaryMacAddress_Object=MibTableColumn
hmAgentSwitchMFDBSummaryMacAddress=_HmAgentSwitchMFDBSummaryMacAddress_Object((1,3,6,1,4,1,248,15,1,2,8,7,2,1,2),_HmAgentSwitchMFDBSummaryMacAddress_Type())
hmAgentSwitchMFDBSummaryMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentSwitchMFDBSummaryMacAddress.setStatus(_A)
_HmAgentSwitchMFDBSummaryForwardingPortMask_Type=HmAgentPortMask
_HmAgentSwitchMFDBSummaryForwardingPortMask_Object=MibTableColumn
hmAgentSwitchMFDBSummaryForwardingPortMask=_HmAgentSwitchMFDBSummaryForwardingPortMask_Object((1,3,6,1,4,1,248,15,1,2,8,7,2,1,3),_HmAgentSwitchMFDBSummaryForwardingPortMask_Type())
hmAgentSwitchMFDBSummaryForwardingPortMask.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentSwitchMFDBSummaryForwardingPortMask.setStatus(_A)
_HmAgentSwitchMFDBMaxTableEntries_Type=Gauge32
_HmAgentSwitchMFDBMaxTableEntries_Object=MibScalar
hmAgentSwitchMFDBMaxTableEntries=_HmAgentSwitchMFDBMaxTableEntries_Object((1,3,6,1,4,1,248,15,1,2,8,7,3),_HmAgentSwitchMFDBMaxTableEntries_Type())
hmAgentSwitchMFDBMaxTableEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentSwitchMFDBMaxTableEntries.setStatus(_A)
_HmAgentSwitchMFDBMostEntriesUsed_Type=Gauge32
_HmAgentSwitchMFDBMostEntriesUsed_Object=MibScalar
hmAgentSwitchMFDBMostEntriesUsed=_HmAgentSwitchMFDBMostEntriesUsed_Object((1,3,6,1,4,1,248,15,1,2,8,7,4),_HmAgentSwitchMFDBMostEntriesUsed_Type())
hmAgentSwitchMFDBMostEntriesUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentSwitchMFDBMostEntriesUsed.setStatus(_A)
_HmAgentSwitchMFDBCurrentEntries_Type=Gauge32
_HmAgentSwitchMFDBCurrentEntries_Object=MibScalar
hmAgentSwitchMFDBCurrentEntries=_HmAgentSwitchMFDBCurrentEntries_Object((1,3,6,1,4,1,248,15,1,2,8,7,5),_HmAgentSwitchMFDBCurrentEntries_Type())
hmAgentSwitchMFDBCurrentEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentSwitchMFDBCurrentEntries.setStatus(_A)
_HmAgentSwitchDVlanTagGroup_ObjectIdentity=ObjectIdentity
hmAgentSwitchDVlanTagGroup=_HmAgentSwitchDVlanTagGroup_ObjectIdentity((1,3,6,1,4,1,248,15,1,2,8,8))
class _HmAgentSwitchDVlanTagEthertype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HmAgentSwitchDVlanTagEthertype_Type.__name__=_D
_HmAgentSwitchDVlanTagEthertype_Object=MibScalar
hmAgentSwitchDVlanTagEthertype=_HmAgentSwitchDVlanTagEthertype_Object((1,3,6,1,4,1,248,15,1,2,8,8,1),_HmAgentSwitchDVlanTagEthertype_Type())
hmAgentSwitchDVlanTagEthertype.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentSwitchDVlanTagEthertype.setStatus(_A)
_HmAgentSwitchVoiceVLANGroup_ObjectIdentity=ObjectIdentity
hmAgentSwitchVoiceVLANGroup=_HmAgentSwitchVoiceVLANGroup_ObjectIdentity((1,3,6,1,4,1,248,15,1,2,8,25))
class _HmAgentSwitchVoiceVLANAdminMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HmAgentSwitchVoiceVLANAdminMode_Type.__name__=_D
_HmAgentSwitchVoiceVLANAdminMode_Object=MibScalar
hmAgentSwitchVoiceVLANAdminMode=_HmAgentSwitchVoiceVLANAdminMode_Object((1,3,6,1,4,1,248,15,1,2,8,25,1),_HmAgentSwitchVoiceVLANAdminMode_Type())
hmAgentSwitchVoiceVLANAdminMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentSwitchVoiceVLANAdminMode.setStatus(_A)
_HmAgentSwitchVoiceVlanDeviceTable_Object=MibTable
hmAgentSwitchVoiceVlanDeviceTable=_HmAgentSwitchVoiceVlanDeviceTable_Object((1,3,6,1,4,1,248,15,1,2,8,25,2))
if mibBuilder.loadTexts:hmAgentSwitchVoiceVlanDeviceTable.setStatus(_A)
_HmAgentSwitchVoiceVlanDeviceEntry_Object=MibTableRow
hmAgentSwitchVoiceVlanDeviceEntry=_HmAgentSwitchVoiceVlanDeviceEntry_Object((1,3,6,1,4,1,248,15,1,2,8,25,2,1))
hmAgentSwitchVoiceVlanDeviceEntry.setIndexNames((0,_G,_y),(0,_G,_z))
if mibBuilder.loadTexts:hmAgentSwitchVoiceVlanDeviceEntry.setStatus(_A)
class _HmAgentSwitchVoiceVlanInterfaceNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HmAgentSwitchVoiceVlanInterfaceNum_Type.__name__=_D
_HmAgentSwitchVoiceVlanInterfaceNum_Object=MibTableColumn
hmAgentSwitchVoiceVlanInterfaceNum=_HmAgentSwitchVoiceVlanInterfaceNum_Object((1,3,6,1,4,1,248,15,1,2,8,25,2,1,1),_HmAgentSwitchVoiceVlanInterfaceNum_Type())
hmAgentSwitchVoiceVlanInterfaceNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentSwitchVoiceVlanInterfaceNum.setStatus(_A)
_HmAgentSwitchVoiceVlanDeviceMacAddress_Type=MacAddress
_HmAgentSwitchVoiceVlanDeviceMacAddress_Object=MibTableColumn
hmAgentSwitchVoiceVlanDeviceMacAddress=_HmAgentSwitchVoiceVlanDeviceMacAddress_Object((1,3,6,1,4,1,248,15,1,2,8,25,2,1,2),_HmAgentSwitchVoiceVlanDeviceMacAddress_Type())
hmAgentSwitchVoiceVlanDeviceMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentSwitchVoiceVlanDeviceMacAddress.setStatus(_A)
_HmAgentTransferConfigGroup_ObjectIdentity=ObjectIdentity
hmAgentTransferConfigGroup=_HmAgentTransferConfigGroup_ObjectIdentity((1,3,6,1,4,1,248,15,1,2,9))
_HmAgentTransferUploadGroup_ObjectIdentity=ObjectIdentity
hmAgentTransferUploadGroup=_HmAgentTransferUploadGroup_ObjectIdentity((1,3,6,1,4,1,248,15,1,2,9,1))
class _HmAgentTransferUploadMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('tftp',1),('xmodem',2),('ymodem',3),('zmodem',4)))
_HmAgentTransferUploadMode_Type.__name__=_D
_HmAgentTransferUploadMode_Object=MibScalar
hmAgentTransferUploadMode=_HmAgentTransferUploadMode_Object((1,3,6,1,4,1,248,15,1,2,9,1,1),_HmAgentTransferUploadMode_Type())
hmAgentTransferUploadMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentTransferUploadMode.setStatus(_A)
_HmAgentTransferUploadServerIP_Type=IpAddress
_HmAgentTransferUploadServerIP_Object=MibScalar
hmAgentTransferUploadServerIP=_HmAgentTransferUploadServerIP_Object((1,3,6,1,4,1,248,15,1,2,9,1,2),_HmAgentTransferUploadServerIP_Type())
hmAgentTransferUploadServerIP.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentTransferUploadServerIP.setStatus(_A)
class _HmAgentTransferUploadPath_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_HmAgentTransferUploadPath_Type.__name__=_I
_HmAgentTransferUploadPath_Object=MibScalar
hmAgentTransferUploadPath=_HmAgentTransferUploadPath_Object((1,3,6,1,4,1,248,15,1,2,9,1,3),_HmAgentTransferUploadPath_Type())
hmAgentTransferUploadPath.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentTransferUploadPath.setStatus(_A)
class _HmAgentTransferUploadFilename_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_HmAgentTransferUploadFilename_Type.__name__=_I
_HmAgentTransferUploadFilename_Object=MibScalar
hmAgentTransferUploadFilename=_HmAgentTransferUploadFilename_Object((1,3,6,1,4,1,248,15,1,2,9,1,4),_HmAgentTransferUploadFilename_Type())
hmAgentTransferUploadFilename.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentTransferUploadFilename.setStatus(_A)
class _HmAgentTransferUploadDataType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5,6)));namedValues=NamedValues(*(('config',2),('errorlog',3),('messagelog',4),('traplog',5),(_A0,6)))
_HmAgentTransferUploadDataType_Type.__name__=_D
_HmAgentTransferUploadDataType_Object=MibScalar
hmAgentTransferUploadDataType=_HmAgentTransferUploadDataType_Object((1,3,6,1,4,1,248,15,1,2,9,1,5),_HmAgentTransferUploadDataType_Type())
hmAgentTransferUploadDataType.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentTransferUploadDataType.setStatus(_A)
class _HmAgentTransferUploadStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HmAgentTransferUploadStart_Type.__name__=_D
_HmAgentTransferUploadStart_Object=MibScalar
hmAgentTransferUploadStart=_HmAgentTransferUploadStart_Object((1,3,6,1,4,1,248,15,1,2,9,1,6),_HmAgentTransferUploadStart_Type())
hmAgentTransferUploadStart.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentTransferUploadStart.setStatus(_A)
class _HmAgentTransferUploadStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*((_a,1),(_A1,2),(_A2,3),(_A3,4),(_A4,5),(_A5,6),(_A6,7),(_A7,8),(_A8,9),(_A9,10),(_AA,11),(_AB,12),(_AC,13)))
_HmAgentTransferUploadStatus_Type.__name__=_D
_HmAgentTransferUploadStatus_Object=MibScalar
hmAgentTransferUploadStatus=_HmAgentTransferUploadStatus_Object((1,3,6,1,4,1,248,15,1,2,9,1,7),_HmAgentTransferUploadStatus_Type())
hmAgentTransferUploadStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentTransferUploadStatus.setStatus(_A)
_HmAgentTransferDownloadGroup_ObjectIdentity=ObjectIdentity
hmAgentTransferDownloadGroup=_HmAgentTransferDownloadGroup_ObjectIdentity((1,3,6,1,4,1,248,15,1,2,9,2))
class _HmAgentTransferDownloadMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('tftp',1),('xmodem',2),('ymodem',3),('zmodem',4)))
_HmAgentTransferDownloadMode_Type.__name__=_D
_HmAgentTransferDownloadMode_Object=MibScalar
hmAgentTransferDownloadMode=_HmAgentTransferDownloadMode_Object((1,3,6,1,4,1,248,15,1,2,9,2,1),_HmAgentTransferDownloadMode_Type())
hmAgentTransferDownloadMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentTransferDownloadMode.setStatus(_A)
_HmAgentTransferDownloadServerIP_Type=IpAddress
_HmAgentTransferDownloadServerIP_Object=MibScalar
hmAgentTransferDownloadServerIP=_HmAgentTransferDownloadServerIP_Object((1,3,6,1,4,1,248,15,1,2,9,2,2),_HmAgentTransferDownloadServerIP_Type())
hmAgentTransferDownloadServerIP.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentTransferDownloadServerIP.setStatus(_A)
class _HmAgentTransferDownloadPath_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_HmAgentTransferDownloadPath_Type.__name__=_I
_HmAgentTransferDownloadPath_Object=MibScalar
hmAgentTransferDownloadPath=_HmAgentTransferDownloadPath_Object((1,3,6,1,4,1,248,15,1,2,9,2,3),_HmAgentTransferDownloadPath_Type())
hmAgentTransferDownloadPath.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentTransferDownloadPath.setStatus(_A)
class _HmAgentTransferDownloadFilename_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_HmAgentTransferDownloadFilename_Type.__name__=_I
_HmAgentTransferDownloadFilename_Object=MibScalar
hmAgentTransferDownloadFilename=_HmAgentTransferDownloadFilename_Object((1,3,6,1,4,1,248,15,1,2,9,2,4),_HmAgentTransferDownloadFilename_Type())
hmAgentTransferDownloadFilename.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentTransferDownloadFilename.setStatus(_A)
class _HmAgentTransferDownloadDataType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('code',2),('config',3),('sshkey-rsa1',4),('sshkey-rsa2',5),('sshkey-dsa',6),('sslpem-root',7),('sslpem-server',8),('sslpem-dhweak',9),('sslpem-dhstrong',10),(_A0,11)))
_HmAgentTransferDownloadDataType_Type.__name__=_D
_HmAgentTransferDownloadDataType_Object=MibScalar
hmAgentTransferDownloadDataType=_HmAgentTransferDownloadDataType_Object((1,3,6,1,4,1,248,15,1,2,9,2,5),_HmAgentTransferDownloadDataType_Type())
hmAgentTransferDownloadDataType.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentTransferDownloadDataType.setStatus(_A)
class _HmAgentTransferDownloadStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HmAgentTransferDownloadStart_Type.__name__=_D
_HmAgentTransferDownloadStart_Object=MibScalar
hmAgentTransferDownloadStart=_HmAgentTransferDownloadStart_Object((1,3,6,1,4,1,248,15,1,2,9,2,6),_HmAgentTransferDownloadStart_Type())
hmAgentTransferDownloadStart.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentTransferDownloadStart.setStatus(_A)
class _HmAgentTransferDownloadStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*((_a,1),(_A1,2),(_A2,3),(_A3,4),(_A4,5),(_A5,6),(_A6,7),(_A7,8),(_A8,9),(_A9,10),(_AA,11),(_AB,12),(_AC,13)))
_HmAgentTransferDownloadStatus_Type.__name__=_D
_HmAgentTransferDownloadStatus_Object=MibScalar
hmAgentTransferDownloadStatus=_HmAgentTransferDownloadStatus_Object((1,3,6,1,4,1,248,15,1,2,9,2,7),_HmAgentTransferDownloadStatus_Type())
hmAgentTransferDownloadStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentTransferDownloadStatus.setStatus(_A)
_HmAgentPortMirroringGroup_ObjectIdentity=ObjectIdentity
hmAgentPortMirroringGroup=_HmAgentPortMirroringGroup_ObjectIdentity((1,3,6,1,4,1,248,15,1,2,10))
class _HmAgentMirroredPortIfIndex_Type(Integer32):defaultValue=0
_HmAgentMirroredPortIfIndex_Type.__name__=_D
_HmAgentMirroredPortIfIndex_Object=MibScalar
hmAgentMirroredPortIfIndex=_HmAgentMirroredPortIfIndex_Object((1,3,6,1,4,1,248,15,1,2,10,1),_HmAgentMirroredPortIfIndex_Type())
hmAgentMirroredPortIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentMirroredPortIfIndex.setStatus(_J)
class _HmAgentProbePortIfIndex_Type(Integer32):defaultValue=0
_HmAgentProbePortIfIndex_Type.__name__=_D
_HmAgentProbePortIfIndex_Object=MibScalar
hmAgentProbePortIfIndex=_HmAgentProbePortIfIndex_Object((1,3,6,1,4,1,248,15,1,2,10,2),_HmAgentProbePortIfIndex_Type())
hmAgentProbePortIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentProbePortIfIndex.setStatus(_J)
class _HmAgentPortMirroringMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_E,2),('delete',3)))
_HmAgentPortMirroringMode_Type.__name__=_D
_HmAgentPortMirroringMode_Object=MibScalar
hmAgentPortMirroringMode=_HmAgentPortMirroringMode_Object((1,3,6,1,4,1,248,15,1,2,10,3),_HmAgentPortMirroringMode_Type())
hmAgentPortMirroringMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentPortMirroringMode.setStatus(_J)
_HmAgentPortMirrorTable_Object=MibTable
hmAgentPortMirrorTable=_HmAgentPortMirrorTable_Object((1,3,6,1,4,1,248,15,1,2,10,4))
if mibBuilder.loadTexts:hmAgentPortMirrorTable.setStatus(_A)
_HmAgentPortMirrorEntry_Object=MibTableRow
hmAgentPortMirrorEntry=_HmAgentPortMirrorEntry_Object((1,3,6,1,4,1,248,15,1,2,10,4,1))
hmAgentPortMirrorEntry.setIndexNames((0,_G,_AD))
if mibBuilder.loadTexts:hmAgentPortMirrorEntry.setStatus(_A)
_HmAgentPortMirrorSessionNum_Type=Unsigned32
_HmAgentPortMirrorSessionNum_Object=MibTableColumn
hmAgentPortMirrorSessionNum=_HmAgentPortMirrorSessionNum_Object((1,3,6,1,4,1,248,15,1,2,10,4,1,1),_HmAgentPortMirrorSessionNum_Type())
hmAgentPortMirrorSessionNum.setMaxAccess(_R)
if mibBuilder.loadTexts:hmAgentPortMirrorSessionNum.setStatus(_A)
class _HmAgentPortMirrorDestinationPort_Type(Unsigned32):defaultValue=0
_HmAgentPortMirrorDestinationPort_Type.__name__=_H
_HmAgentPortMirrorDestinationPort_Object=MibTableColumn
hmAgentPortMirrorDestinationPort=_HmAgentPortMirrorDestinationPort_Object((1,3,6,1,4,1,248,15,1,2,10,4,1,2),_HmAgentPortMirrorDestinationPort_Type())
hmAgentPortMirrorDestinationPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentPortMirrorDestinationPort.setStatus(_A)
_HmAgentPortMirrorSourcePortMask_Type=HmAgentPortMask
_HmAgentPortMirrorSourcePortMask_Object=MibTableColumn
hmAgentPortMirrorSourcePortMask=_HmAgentPortMirrorSourcePortMask_Object((1,3,6,1,4,1,248,15,1,2,10,4,1,3),_HmAgentPortMirrorSourcePortMask_Type())
hmAgentPortMirrorSourcePortMask.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentPortMirrorSourcePortMask.setStatus(_A)
class _HmAgentPortMirrorAdminMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_E,2),('delete',3)))
_HmAgentPortMirrorAdminMode_Type.__name__=_D
_HmAgentPortMirrorAdminMode_Object=MibTableColumn
hmAgentPortMirrorAdminMode=_HmAgentPortMirrorAdminMode_Object((1,3,6,1,4,1,248,15,1,2,10,4,1,4),_HmAgentPortMirrorAdminMode_Type())
hmAgentPortMirrorAdminMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentPortMirrorAdminMode.setStatus(_A)
_HmAgentPortMirrorIngressMask_Type=HmAgentPortMask
_HmAgentPortMirrorIngressMask_Object=MibTableColumn
hmAgentPortMirrorIngressMask=_HmAgentPortMirrorIngressMask_Object((1,3,6,1,4,1,248,15,1,2,10,4,1,248),_HmAgentPortMirrorIngressMask_Type())
hmAgentPortMirrorIngressMask.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentPortMirrorIngressMask.setStatus(_A)
_HmAgentPortMirrorEgressMask_Type=HmAgentPortMask
_HmAgentPortMirrorEgressMask_Object=MibTableColumn
hmAgentPortMirrorEgressMask=_HmAgentPortMirrorEgressMask_Object((1,3,6,1,4,1,248,15,1,2,10,4,1,249),_HmAgentPortMirrorEgressMask_Type())
hmAgentPortMirrorEgressMask.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentPortMirrorEgressMask.setStatus(_A)
_HmAgentDot3adAggPortTable_Object=MibTable
hmAgentDot3adAggPortTable=_HmAgentDot3adAggPortTable_Object((1,3,6,1,4,1,248,15,1,2,12))
if mibBuilder.loadTexts:hmAgentDot3adAggPortTable.setStatus(_A)
_HmAgentDot3adAggPortEntry_Object=MibTableRow
hmAgentDot3adAggPortEntry=_HmAgentDot3adAggPortEntry_Object((1,3,6,1,4,1,248,15,1,2,12,1))
hmAgentDot3adAggPortEntry.setIndexNames((0,_G,_AE))
if mibBuilder.loadTexts:hmAgentDot3adAggPortEntry.setStatus(_A)
_HmAgentDot3adAggPort_Type=Integer32
_HmAgentDot3adAggPort_Object=MibTableColumn
hmAgentDot3adAggPort=_HmAgentDot3adAggPort_Object((1,3,6,1,4,1,248,15,1,2,12,1,1),_HmAgentDot3adAggPort_Type())
hmAgentDot3adAggPort.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentDot3adAggPort.setStatus(_A)
class _HmAgentDot3adAggPortLACPMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HmAgentDot3adAggPortLACPMode_Type.__name__=_D
_HmAgentDot3adAggPortLACPMode_Object=MibTableColumn
hmAgentDot3adAggPortLACPMode=_HmAgentDot3adAggPortLACPMode_Object((1,3,6,1,4,1,248,15,1,2,12,1,2),_HmAgentDot3adAggPortLACPMode_Type())
hmAgentDot3adAggPortLACPMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentDot3adAggPortLACPMode.setStatus(_A)
_HmAgentPortConfigTable_Object=MibTable
hmAgentPortConfigTable=_HmAgentPortConfigTable_Object((1,3,6,1,4,1,248,15,1,2,13))
if mibBuilder.loadTexts:hmAgentPortConfigTable.setStatus(_A)
_HmAgentPortConfigEntry_Object=MibTableRow
hmAgentPortConfigEntry=_HmAgentPortConfigEntry_Object((1,3,6,1,4,1,248,15,1,2,13,1))
hmAgentPortConfigEntry.setIndexNames((0,_G,_AF))
if mibBuilder.loadTexts:hmAgentPortConfigEntry.setStatus(_A)
class _HmAgentPortDot1dBasePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HmAgentPortDot1dBasePort_Type.__name__=_D
_HmAgentPortDot1dBasePort_Object=MibTableColumn
hmAgentPortDot1dBasePort=_HmAgentPortDot1dBasePort_Object((1,3,6,1,4,1,248,15,1,2,13,1,1),_HmAgentPortDot1dBasePort_Type())
hmAgentPortDot1dBasePort.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentPortDot1dBasePort.setStatus(_A)
_HmAgentPortIfIndex_Type=Integer32
_HmAgentPortIfIndex_Object=MibTableColumn
hmAgentPortIfIndex=_HmAgentPortIfIndex_Object((1,3,6,1,4,1,248,15,1,2,13,1,2),_HmAgentPortIfIndex_Type())
hmAgentPortIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentPortIfIndex.setStatus(_A)
_HmAgentPortIanaType_Type=IANAifType
_HmAgentPortIanaType_Object=MibTableColumn
hmAgentPortIanaType=_HmAgentPortIanaType_Object((1,3,6,1,4,1,248,15,1,2,13,1,3),_HmAgentPortIanaType_Type())
hmAgentPortIanaType.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentPortIanaType.setStatus(_A)
class _HmAgentPortSTPMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('dot1d',1),('fast',2),('off',3)))
_HmAgentPortSTPMode_Type.__name__=_D
_HmAgentPortSTPMode_Object=MibTableColumn
hmAgentPortSTPMode=_HmAgentPortSTPMode_Object((1,3,6,1,4,1,248,15,1,2,13,1,4),_HmAgentPortSTPMode_Type())
hmAgentPortSTPMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentPortSTPMode.setStatus(_A)
class _HmAgentPortSTPState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('blocking',1),('listening',2),(_b,3),(_c,4),(_P,5)))
_HmAgentPortSTPState_Type.__name__=_D
_HmAgentPortSTPState_Object=MibTableColumn
hmAgentPortSTPState=_HmAgentPortSTPState_Object((1,3,6,1,4,1,248,15,1,2,13,1,5),_HmAgentPortSTPState_Type())
hmAgentPortSTPState.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentPortSTPState.setStatus(_A)
class _HmAgentPortAdminMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HmAgentPortAdminMode_Type.__name__=_D
_HmAgentPortAdminMode_Object=MibTableColumn
hmAgentPortAdminMode=_HmAgentPortAdminMode_Object((1,3,6,1,4,1,248,15,1,2,13,1,6),_HmAgentPortAdminMode_Type())
hmAgentPortAdminMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentPortAdminMode.setStatus(_A)
class _HmAgentPortPhysicalMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_AG,1),('half-10',2),('full-10',3),('half-100',4),('full-100',5),(_AH,6),(_AI,7),(_AJ,8)))
_HmAgentPortPhysicalMode_Type.__name__=_D
_HmAgentPortPhysicalMode_Object=MibTableColumn
hmAgentPortPhysicalMode=_HmAgentPortPhysicalMode_Object((1,3,6,1,4,1,248,15,1,2,13,1,7),_HmAgentPortPhysicalMode_Type())
hmAgentPortPhysicalMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentPortPhysicalMode.setStatus(_J)
class _HmAgentPortPhysicalStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_AG,1),('half-10',2),('full-10',3),('half-100',4),('full-100',5),(_AH,6),(_AI,7),(_AJ,8)))
_HmAgentPortPhysicalStatus_Type.__name__=_D
_HmAgentPortPhysicalStatus_Object=MibTableColumn
hmAgentPortPhysicalStatus=_HmAgentPortPhysicalStatus_Object((1,3,6,1,4,1,248,15,1,2,13,1,8),_HmAgentPortPhysicalStatus_Type())
hmAgentPortPhysicalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentPortPhysicalStatus.setStatus(_J)
class _HmAgentPortLinkTrapMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HmAgentPortLinkTrapMode_Type.__name__=_D
_HmAgentPortLinkTrapMode_Object=MibTableColumn
hmAgentPortLinkTrapMode=_HmAgentPortLinkTrapMode_Object((1,3,6,1,4,1,248,15,1,2,13,1,9),_HmAgentPortLinkTrapMode_Type())
hmAgentPortLinkTrapMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentPortLinkTrapMode.setStatus(_A)
class _HmAgentPortClearStats_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HmAgentPortClearStats_Type.__name__=_D
_HmAgentPortClearStats_Object=MibTableColumn
hmAgentPortClearStats=_HmAgentPortClearStats_Object((1,3,6,1,4,1,248,15,1,2,13,1,10),_HmAgentPortClearStats_Type())
hmAgentPortClearStats.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentPortClearStats.setStatus(_A)
_HmAgentPortDefaultType_Type=ObjectIdentifier
_HmAgentPortDefaultType_Object=MibTableColumn
hmAgentPortDefaultType=_HmAgentPortDefaultType_Object((1,3,6,1,4,1,248,15,1,2,13,1,11),_HmAgentPortDefaultType_Type())
hmAgentPortDefaultType.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentPortDefaultType.setStatus(_A)
_HmAgentPortType_Type=ObjectIdentifier
_HmAgentPortType_Object=MibTableColumn
hmAgentPortType=_HmAgentPortType_Object((1,3,6,1,4,1,248,15,1,2,13,1,12),_HmAgentPortType_Type())
hmAgentPortType.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentPortType.setStatus(_A)
class _HmAgentPortAutoNegAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HmAgentPortAutoNegAdminStatus_Type.__name__=_D
_HmAgentPortAutoNegAdminStatus_Object=MibTableColumn
hmAgentPortAutoNegAdminStatus=_HmAgentPortAutoNegAdminStatus_Object((1,3,6,1,4,1,248,15,1,2,13,1,13),_HmAgentPortAutoNegAdminStatus_Type())
hmAgentPortAutoNegAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentPortAutoNegAdminStatus.setStatus(_A)
class _HmAgentPortDot3FlowControlMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HmAgentPortDot3FlowControlMode_Type.__name__=_D
_HmAgentPortDot3FlowControlMode_Object=MibTableColumn
hmAgentPortDot3FlowControlMode=_HmAgentPortDot3FlowControlMode_Object((1,3,6,1,4,1,248,15,1,2,13,1,14),_HmAgentPortDot3FlowControlMode_Type())
hmAgentPortDot3FlowControlMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentPortDot3FlowControlMode.setStatus(_A)
class _HmAgentPortDVlanTagMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('core',1),('normal',2),('access',3)))
_HmAgentPortDVlanTagMode_Type.__name__=_D
_HmAgentPortDVlanTagMode_Object=MibTableColumn
hmAgentPortDVlanTagMode=_HmAgentPortDVlanTagMode_Object((1,3,6,1,4,1,248,15,1,2,13,1,15),_HmAgentPortDVlanTagMode_Type())
hmAgentPortDVlanTagMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentPortDVlanTagMode.setStatus(_A)
class _HmAgentPortDVlanTagEthertype_Type(Integer32):defaultValue=33024;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HmAgentPortDVlanTagEthertype_Type.__name__=_D
_HmAgentPortDVlanTagEthertype_Object=MibTableColumn
hmAgentPortDVlanTagEthertype=_HmAgentPortDVlanTagEthertype_Object((1,3,6,1,4,1,248,15,1,2,13,1,16),_HmAgentPortDVlanTagEthertype_Type())
hmAgentPortDVlanTagEthertype.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentPortDVlanTagEthertype.setStatus(_A)
_HmAgentPortDVlanTagCustomerId_Type=Integer32
_HmAgentPortDVlanTagCustomerId_Object=MibTableColumn
hmAgentPortDVlanTagCustomerId=_HmAgentPortDVlanTagCustomerId_Object((1,3,6,1,4,1,248,15,1,2,13,1,17),_HmAgentPortDVlanTagCustomerId_Type())
hmAgentPortDVlanTagCustomerId.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentPortDVlanTagCustomerId.setStatus(_A)
_HmAgentPortMaxFrameSizeLimit_Type=Integer32
_HmAgentPortMaxFrameSizeLimit_Object=MibTableColumn
hmAgentPortMaxFrameSizeLimit=_HmAgentPortMaxFrameSizeLimit_Object((1,3,6,1,4,1,248,15,1,2,13,1,18),_HmAgentPortMaxFrameSizeLimit_Type())
hmAgentPortMaxFrameSizeLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentPortMaxFrameSizeLimit.setStatus(_A)
_HmAgentPortMaxFrameSize_Type=Integer32
_HmAgentPortMaxFrameSize_Object=MibTableColumn
hmAgentPortMaxFrameSize=_HmAgentPortMaxFrameSize_Object((1,3,6,1,4,1,248,15,1,2,13,1,19),_HmAgentPortMaxFrameSize_Type())
hmAgentPortMaxFrameSize.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentPortMaxFrameSize.setStatus(_A)
class _HmAgentPortVoiceVlanMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_Y,1),('vlanid',2),('dot1p',3),('vlanidanddot1p',4),('untagged',5),(_E,6)))
_HmAgentPortVoiceVlanMode_Type.__name__=_D
_HmAgentPortVoiceVlanMode_Object=MibTableColumn
hmAgentPortVoiceVlanMode=_HmAgentPortVoiceVlanMode_Object((1,3,6,1,4,1,248,15,1,2,13,1,20),_HmAgentPortVoiceVlanMode_Type())
hmAgentPortVoiceVlanMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentPortVoiceVlanMode.setStatus(_A)
class _HmAgentPortVoiceVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4093))
_HmAgentPortVoiceVlanID_Type.__name__=_D
_HmAgentPortVoiceVlanID_Object=MibTableColumn
hmAgentPortVoiceVlanID=_HmAgentPortVoiceVlanID_Object((1,3,6,1,4,1,248,15,1,2,13,1,21),_HmAgentPortVoiceVlanID_Type())
hmAgentPortVoiceVlanID.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentPortVoiceVlanID.setStatus(_A)
class _HmAgentPortVoiceVlanPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_HmAgentPortVoiceVlanPriority_Type.__name__=_D
_HmAgentPortVoiceVlanPriority_Object=MibTableColumn
hmAgentPortVoiceVlanPriority=_HmAgentPortVoiceVlanPriority_Object((1,3,6,1,4,1,248,15,1,2,13,1,22),_HmAgentPortVoiceVlanPriority_Type())
hmAgentPortVoiceVlanPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentPortVoiceVlanPriority.setStatus(_A)
class _HmAgentPortVoiceVlanDataPriorityMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('trust',1),('untrust',2)))
_HmAgentPortVoiceVlanDataPriorityMode_Type.__name__=_D
_HmAgentPortVoiceVlanDataPriorityMode_Object=MibTableColumn
hmAgentPortVoiceVlanDataPriorityMode=_HmAgentPortVoiceVlanDataPriorityMode_Object((1,3,6,1,4,1,248,15,1,2,13,1,23),_HmAgentPortVoiceVlanDataPriorityMode_Type())
hmAgentPortVoiceVlanDataPriorityMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentPortVoiceVlanDataPriorityMode.setStatus(_A)
class _HmAgentPortVoiceVlanOperationalStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_k,1),(_P,2)))
_HmAgentPortVoiceVlanOperationalStatus_Type.__name__=_D
_HmAgentPortVoiceVlanOperationalStatus_Object=MibTableColumn
hmAgentPortVoiceVlanOperationalStatus=_HmAgentPortVoiceVlanOperationalStatus_Object((1,3,6,1,4,1,248,15,1,2,13,1,24),_HmAgentPortVoiceVlanOperationalStatus_Type())
hmAgentPortVoiceVlanOperationalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentPortVoiceVlanOperationalStatus.setStatus(_A)
_HmAgentPortVoiceVlanDSCP_Type=Integer32
_HmAgentPortVoiceVlanDSCP_Object=MibTableColumn
hmAgentPortVoiceVlanDSCP=_HmAgentPortVoiceVlanDSCP_Object((1,3,6,1,4,1,248,15,1,2,13,1,25),_HmAgentPortVoiceVlanDSCP_Type())
hmAgentPortVoiceVlanDSCP.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentPortVoiceVlanDSCP.setStatus(_A)
class _HmAgentPortVoiceVlanAuthMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HmAgentPortVoiceVlanAuthMode_Type.__name__=_D
_HmAgentPortVoiceVlanAuthMode_Object=MibTableColumn
hmAgentPortVoiceVlanAuthMode=_HmAgentPortVoiceVlanAuthMode_Object((1,3,6,1,4,1,248,15,1,2,13,1,26),_HmAgentPortVoiceVlanAuthMode_Type())
hmAgentPortVoiceVlanAuthMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentPortVoiceVlanAuthMode.setStatus(_A)
_HmAgentProtocolConfigGroup_ObjectIdentity=ObjectIdentity
hmAgentProtocolConfigGroup=_HmAgentProtocolConfigGroup_ObjectIdentity((1,3,6,1,4,1,248,15,1,2,14))
class _HmAgentProtocolGroupCreate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_HmAgentProtocolGroupCreate_Type.__name__=_I
_HmAgentProtocolGroupCreate_Object=MibScalar
hmAgentProtocolGroupCreate=_HmAgentProtocolGroupCreate_Object((1,3,6,1,4,1,248,15,1,2,14,1),_HmAgentProtocolGroupCreate_Type())
hmAgentProtocolGroupCreate.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentProtocolGroupCreate.setStatus(_A)
_HmAgentProtocolGroupTable_Object=MibTable
hmAgentProtocolGroupTable=_HmAgentProtocolGroupTable_Object((1,3,6,1,4,1,248,15,1,2,14,2))
if mibBuilder.loadTexts:hmAgentProtocolGroupTable.setStatus(_A)
_HmAgentProtocolGroupEntry_Object=MibTableRow
hmAgentProtocolGroupEntry=_HmAgentProtocolGroupEntry_Object((1,3,6,1,4,1,248,15,1,2,14,2,1))
hmAgentProtocolGroupEntry.setIndexNames((0,_G,_d))
if mibBuilder.loadTexts:hmAgentProtocolGroupEntry.setStatus(_A)
_HmAgentProtocolGroupId_Type=Integer32
_HmAgentProtocolGroupId_Object=MibTableColumn
hmAgentProtocolGroupId=_HmAgentProtocolGroupId_Object((1,3,6,1,4,1,248,15,1,2,14,2,1,1),_HmAgentProtocolGroupId_Type())
hmAgentProtocolGroupId.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentProtocolGroupId.setStatus(_A)
_HmAgentProtocolGroupName_Type=DisplayString
_HmAgentProtocolGroupName_Object=MibTableColumn
hmAgentProtocolGroupName=_HmAgentProtocolGroupName_Object((1,3,6,1,4,1,248,15,1,2,14,2,1,2),_HmAgentProtocolGroupName_Type())
hmAgentProtocolGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentProtocolGroupName.setStatus(_A)
_HmAgentProtocolGroupVlanId_Type=Integer32
_HmAgentProtocolGroupVlanId_Object=MibTableColumn
hmAgentProtocolGroupVlanId=_HmAgentProtocolGroupVlanId_Object((1,3,6,1,4,1,248,15,1,2,14,2,1,3),_HmAgentProtocolGroupVlanId_Type())
hmAgentProtocolGroupVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentProtocolGroupVlanId.setStatus(_A)
class _HmAgentProtocolGroupProtocolIP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HmAgentProtocolGroupProtocolIP_Type.__name__=_D
_HmAgentProtocolGroupProtocolIP_Object=MibTableColumn
hmAgentProtocolGroupProtocolIP=_HmAgentProtocolGroupProtocolIP_Object((1,3,6,1,4,1,248,15,1,2,14,2,1,4),_HmAgentProtocolGroupProtocolIP_Type())
hmAgentProtocolGroupProtocolIP.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentProtocolGroupProtocolIP.setStatus(_A)
class _HmAgentProtocolGroupProtocolARP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HmAgentProtocolGroupProtocolARP_Type.__name__=_D
_HmAgentProtocolGroupProtocolARP_Object=MibTableColumn
hmAgentProtocolGroupProtocolARP=_HmAgentProtocolGroupProtocolARP_Object((1,3,6,1,4,1,248,15,1,2,14,2,1,5),_HmAgentProtocolGroupProtocolARP_Type())
hmAgentProtocolGroupProtocolARP.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentProtocolGroupProtocolARP.setStatus(_A)
class _HmAgentProtocolGroupProtocolIPX_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HmAgentProtocolGroupProtocolIPX_Type.__name__=_D
_HmAgentProtocolGroupProtocolIPX_Object=MibTableColumn
hmAgentProtocolGroupProtocolIPX=_HmAgentProtocolGroupProtocolIPX_Object((1,3,6,1,4,1,248,15,1,2,14,2,1,6),_HmAgentProtocolGroupProtocolIPX_Type())
hmAgentProtocolGroupProtocolIPX.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentProtocolGroupProtocolIPX.setStatus(_A)
_HmAgentProtocolGroupStatus_Type=RowStatus
_HmAgentProtocolGroupStatus_Object=MibTableColumn
hmAgentProtocolGroupStatus=_HmAgentProtocolGroupStatus_Object((1,3,6,1,4,1,248,15,1,2,14,2,1,7),_HmAgentProtocolGroupStatus_Type())
hmAgentProtocolGroupStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentProtocolGroupStatus.setStatus(_A)
_HmAgentProtocolGroupPortTable_Object=MibTable
hmAgentProtocolGroupPortTable=_HmAgentProtocolGroupPortTable_Object((1,3,6,1,4,1,248,15,1,2,14,3))
if mibBuilder.loadTexts:hmAgentProtocolGroupPortTable.setStatus(_A)
_HmAgentProtocolGroupPortEntry_Object=MibTableRow
hmAgentProtocolGroupPortEntry=_HmAgentProtocolGroupPortEntry_Object((1,3,6,1,4,1,248,15,1,2,14,3,1))
hmAgentProtocolGroupPortEntry.setIndexNames((0,_G,_d),(0,_G,_AK))
if mibBuilder.loadTexts:hmAgentProtocolGroupPortEntry.setStatus(_A)
_HmAgentProtocolGroupPortIfIndex_Type=Integer32
_HmAgentProtocolGroupPortIfIndex_Object=MibTableColumn
hmAgentProtocolGroupPortIfIndex=_HmAgentProtocolGroupPortIfIndex_Object((1,3,6,1,4,1,248,15,1,2,14,3,1,1),_HmAgentProtocolGroupPortIfIndex_Type())
hmAgentProtocolGroupPortIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentProtocolGroupPortIfIndex.setStatus(_A)
_HmAgentProtocolGroupPortStatus_Type=RowStatus
_HmAgentProtocolGroupPortStatus_Object=MibTableColumn
hmAgentProtocolGroupPortStatus=_HmAgentProtocolGroupPortStatus_Object((1,3,6,1,4,1,248,15,1,2,14,3,1,2),_HmAgentProtocolGroupPortStatus_Type())
hmAgentProtocolGroupPortStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:hmAgentProtocolGroupPortStatus.setStatus(_A)
_HmAgentStpSwitchConfigGroup_ObjectIdentity=ObjectIdentity
hmAgentStpSwitchConfigGroup=_HmAgentStpSwitchConfigGroup_ObjectIdentity((1,3,6,1,4,1,248,15,1,2,15))
class _HmAgentStpConfigDigestKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_HmAgentStpConfigDigestKey_Type.__name__=_L
_HmAgentStpConfigDigestKey_Object=MibScalar
hmAgentStpConfigDigestKey=_HmAgentStpConfigDigestKey_Object((1,3,6,1,4,1,248,15,1,2,15,1),_HmAgentStpConfigDigestKey_Type())
hmAgentStpConfigDigestKey.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentStpConfigDigestKey.setStatus(_A)
class _HmAgentStpConfigFormatSelector_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HmAgentStpConfigFormatSelector_Type.__name__=_H
_HmAgentStpConfigFormatSelector_Object=MibScalar
hmAgentStpConfigFormatSelector=_HmAgentStpConfigFormatSelector_Object((1,3,6,1,4,1,248,15,1,2,15,2),_HmAgentStpConfigFormatSelector_Type())
hmAgentStpConfigFormatSelector.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentStpConfigFormatSelector.setStatus(_A)
class _HmAgentStpConfigName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HmAgentStpConfigName_Type.__name__=_I
_HmAgentStpConfigName_Object=MibScalar
hmAgentStpConfigName=_HmAgentStpConfigName_Object((1,3,6,1,4,1,248,15,1,2,15,3),_HmAgentStpConfigName_Type())
hmAgentStpConfigName.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentStpConfigName.setStatus(_A)
class _HmAgentStpConfigRevision_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HmAgentStpConfigRevision_Type.__name__=_H
_HmAgentStpConfigRevision_Object=MibScalar
hmAgentStpConfigRevision=_HmAgentStpConfigRevision_Object((1,3,6,1,4,1,248,15,1,2,15,4),_HmAgentStpConfigRevision_Type())
hmAgentStpConfigRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentStpConfigRevision.setStatus(_A)
class _HmAgentStpForceVersion_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('dot1d',1),('dot1w',2),('dot1s',3)))
_HmAgentStpForceVersion_Type.__name__=_D
_HmAgentStpForceVersion_Object=MibScalar
hmAgentStpForceVersion=_HmAgentStpForceVersion_Object((1,3,6,1,4,1,248,15,1,2,15,5),_HmAgentStpForceVersion_Type())
hmAgentStpForceVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentStpForceVersion.setStatus(_A)
class _HmAgentStpAdminMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HmAgentStpAdminMode_Type.__name__=_D
_HmAgentStpAdminMode_Object=MibScalar
hmAgentStpAdminMode=_HmAgentStpAdminMode_Object((1,3,6,1,4,1,248,15,1,2,15,6),_HmAgentStpAdminMode_Type())
hmAgentStpAdminMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentStpAdminMode.setStatus(_A)
_HmAgentStpPortTable_Object=MibTable
hmAgentStpPortTable=_HmAgentStpPortTable_Object((1,3,6,1,4,1,248,15,1,2,15,7))
if mibBuilder.loadTexts:hmAgentStpPortTable.setStatus(_A)
_HmAgentStpPortEntry_Object=MibTableRow
hmAgentStpPortEntry=_HmAgentStpPortEntry_Object((1,3,6,1,4,1,248,15,1,2,15,7,1))
hmAgentStpPortEntry.setIndexNames((0,_T,_U))
if mibBuilder.loadTexts:hmAgentStpPortEntry.setStatus(_A)
class _HmAgentStpPortState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HmAgentStpPortState_Type.__name__=_D
_HmAgentStpPortState_Object=MibTableColumn
hmAgentStpPortState=_HmAgentStpPortState_Object((1,3,6,1,4,1,248,15,1,2,15,7,1,1),_HmAgentStpPortState_Type())
hmAgentStpPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentStpPortState.setStatus(_A)
_HmAgentStpPortStatsMstpBpduRx_Type=Counter32
_HmAgentStpPortStatsMstpBpduRx_Object=MibTableColumn
hmAgentStpPortStatsMstpBpduRx=_HmAgentStpPortStatsMstpBpduRx_Object((1,3,6,1,4,1,248,15,1,2,15,7,1,2),_HmAgentStpPortStatsMstpBpduRx_Type())
hmAgentStpPortStatsMstpBpduRx.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentStpPortStatsMstpBpduRx.setStatus(_A)
_HmAgentStpPortStatsMstpBpduTx_Type=Counter32
_HmAgentStpPortStatsMstpBpduTx_Object=MibTableColumn
hmAgentStpPortStatsMstpBpduTx=_HmAgentStpPortStatsMstpBpduTx_Object((1,3,6,1,4,1,248,15,1,2,15,7,1,3),_HmAgentStpPortStatsMstpBpduTx_Type())
hmAgentStpPortStatsMstpBpduTx.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentStpPortStatsMstpBpduTx.setStatus(_A)
_HmAgentStpPortStatsRstpBpduRx_Type=Counter32
_HmAgentStpPortStatsRstpBpduRx_Object=MibTableColumn
hmAgentStpPortStatsRstpBpduRx=_HmAgentStpPortStatsRstpBpduRx_Object((1,3,6,1,4,1,248,15,1,2,15,7,1,4),_HmAgentStpPortStatsRstpBpduRx_Type())
hmAgentStpPortStatsRstpBpduRx.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentStpPortStatsRstpBpduRx.setStatus(_A)
_HmAgentStpPortStatsRstpBpduTx_Type=Counter32
_HmAgentStpPortStatsRstpBpduTx_Object=MibTableColumn
hmAgentStpPortStatsRstpBpduTx=_HmAgentStpPortStatsRstpBpduTx_Object((1,3,6,1,4,1,248,15,1,2,15,7,1,5),_HmAgentStpPortStatsRstpBpduTx_Type())
hmAgentStpPortStatsRstpBpduTx.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentStpPortStatsRstpBpduTx.setStatus(_A)
_HmAgentStpPortStatsStpBpduRx_Type=Counter32
_HmAgentStpPortStatsStpBpduRx_Object=MibTableColumn
hmAgentStpPortStatsStpBpduRx=_HmAgentStpPortStatsStpBpduRx_Object((1,3,6,1,4,1,248,15,1,2,15,7,1,6),_HmAgentStpPortStatsStpBpduRx_Type())
hmAgentStpPortStatsStpBpduRx.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentStpPortStatsStpBpduRx.setStatus(_A)
_HmAgentStpPortStatsStpBpduTx_Type=Counter32
_HmAgentStpPortStatsStpBpduTx_Object=MibTableColumn
hmAgentStpPortStatsStpBpduTx=_HmAgentStpPortStatsStpBpduTx_Object((1,3,6,1,4,1,248,15,1,2,15,7,1,7),_HmAgentStpPortStatsStpBpduTx_Type())
hmAgentStpPortStatsStpBpduTx.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentStpPortStatsStpBpduTx.setStatus(_A)
_HmAgentStpPortUpTime_Type=TimeTicks
_HmAgentStpPortUpTime_Object=MibTableColumn
hmAgentStpPortUpTime=_HmAgentStpPortUpTime_Object((1,3,6,1,4,1,248,15,1,2,15,7,1,8),_HmAgentStpPortUpTime_Type())
hmAgentStpPortUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentStpPortUpTime.setStatus(_A)
class _HmAgentStpPortMigrationCheck_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_M,0),(_N,1)))
_HmAgentStpPortMigrationCheck_Type.__name__=_D
_HmAgentStpPortMigrationCheck_Object=MibTableColumn
hmAgentStpPortMigrationCheck=_HmAgentStpPortMigrationCheck_Object((1,3,6,1,4,1,248,15,1,2,15,7,1,9),_HmAgentStpPortMigrationCheck_Type())
hmAgentStpPortMigrationCheck.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentStpPortMigrationCheck.setStatus(_A)
class _HmAgentStpPortHelloTime_Type(Unsigned32):defaultValue=2;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_HmAgentStpPortHelloTime_Type.__name__=_H
_HmAgentStpPortHelloTime_Object=MibTableColumn
hmAgentStpPortHelloTime=_HmAgentStpPortHelloTime_Object((1,3,6,1,4,1,248,15,1,2,15,7,1,10),_HmAgentStpPortHelloTime_Type())
hmAgentStpPortHelloTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentStpPortHelloTime.setStatus(_A)
_HmAgentStpCstConfigGroup_ObjectIdentity=ObjectIdentity
hmAgentStpCstConfigGroup=_HmAgentStpCstConfigGroup_ObjectIdentity((1,3,6,1,4,1,248,15,1,2,15,8))
_HmAgentStpCstHelloTime_Type=Unsigned32
_HmAgentStpCstHelloTime_Object=MibScalar
hmAgentStpCstHelloTime=_HmAgentStpCstHelloTime_Object((1,3,6,1,4,1,248,15,1,2,15,8,1),_HmAgentStpCstHelloTime_Type())
hmAgentStpCstHelloTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentStpCstHelloTime.setStatus(_A)
_HmAgentStpCstMaxAge_Type=Unsigned32
_HmAgentStpCstMaxAge_Object=MibScalar
hmAgentStpCstMaxAge=_HmAgentStpCstMaxAge_Object((1,3,6,1,4,1,248,15,1,2,15,8,2),_HmAgentStpCstMaxAge_Type())
hmAgentStpCstMaxAge.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentStpCstMaxAge.setStatus(_A)
class _HmAgentStpCstRegionalRootId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_HmAgentStpCstRegionalRootId_Type.__name__=_L
_HmAgentStpCstRegionalRootId_Object=MibScalar
hmAgentStpCstRegionalRootId=_HmAgentStpCstRegionalRootId_Object((1,3,6,1,4,1,248,15,1,2,15,8,3),_HmAgentStpCstRegionalRootId_Type())
hmAgentStpCstRegionalRootId.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentStpCstRegionalRootId.setStatus(_A)
_HmAgentStpCstRegionalRootPathCost_Type=Unsigned32
_HmAgentStpCstRegionalRootPathCost_Object=MibScalar
hmAgentStpCstRegionalRootPathCost=_HmAgentStpCstRegionalRootPathCost_Object((1,3,6,1,4,1,248,15,1,2,15,8,4),_HmAgentStpCstRegionalRootPathCost_Type())
hmAgentStpCstRegionalRootPathCost.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentStpCstRegionalRootPathCost.setStatus(_A)
_HmAgentStpCstRootFwdDelay_Type=Unsigned32
_HmAgentStpCstRootFwdDelay_Object=MibScalar
hmAgentStpCstRootFwdDelay=_HmAgentStpCstRootFwdDelay_Object((1,3,6,1,4,1,248,15,1,2,15,8,5),_HmAgentStpCstRootFwdDelay_Type())
hmAgentStpCstRootFwdDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentStpCstRootFwdDelay.setStatus(_A)
class _HmAgentStpCstBridgeFwdDelay_Type(Unsigned32):defaultValue=15;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,30))
_HmAgentStpCstBridgeFwdDelay_Type.__name__=_H
_HmAgentStpCstBridgeFwdDelay_Object=MibScalar
hmAgentStpCstBridgeFwdDelay=_HmAgentStpCstBridgeFwdDelay_Object((1,3,6,1,4,1,248,15,1,2,15,8,6),_HmAgentStpCstBridgeFwdDelay_Type())
hmAgentStpCstBridgeFwdDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentStpCstBridgeFwdDelay.setStatus(_A)
class _HmAgentStpCstBridgeHelloTime_Type(Unsigned32):defaultValue=2;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_HmAgentStpCstBridgeHelloTime_Type.__name__=_H
_HmAgentStpCstBridgeHelloTime_Object=MibScalar
hmAgentStpCstBridgeHelloTime=_HmAgentStpCstBridgeHelloTime_Object((1,3,6,1,4,1,248,15,1,2,15,8,7),_HmAgentStpCstBridgeHelloTime_Type())
hmAgentStpCstBridgeHelloTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentStpCstBridgeHelloTime.setStatus(_A)
_HmAgentStpCstBridgeHoldTime_Type=Unsigned32
_HmAgentStpCstBridgeHoldTime_Object=MibScalar
hmAgentStpCstBridgeHoldTime=_HmAgentStpCstBridgeHoldTime_Object((1,3,6,1,4,1,248,15,1,2,15,8,8),_HmAgentStpCstBridgeHoldTime_Type())
hmAgentStpCstBridgeHoldTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentStpCstBridgeHoldTime.setStatus(_A)
class _HmAgentStpCstBridgeMaxAge_Type(Unsigned32):defaultValue=20;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(6,40))
_HmAgentStpCstBridgeMaxAge_Type.__name__=_H
_HmAgentStpCstBridgeMaxAge_Object=MibScalar
hmAgentStpCstBridgeMaxAge=_HmAgentStpCstBridgeMaxAge_Object((1,3,6,1,4,1,248,15,1,2,15,8,9),_HmAgentStpCstBridgeMaxAge_Type())
hmAgentStpCstBridgeMaxAge.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentStpCstBridgeMaxAge.setStatus(_A)
_HmAgentStpCstBridgeDesignatedRoot_Type=BridgeId
_HmAgentStpCstBridgeDesignatedRoot_Object=MibScalar
hmAgentStpCstBridgeDesignatedRoot=_HmAgentStpCstBridgeDesignatedRoot_Object((1,3,6,1,4,1,248,15,1,2,15,8,10),_HmAgentStpCstBridgeDesignatedRoot_Type())
hmAgentStpCstBridgeDesignatedRoot.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentStpCstBridgeDesignatedRoot.setStatus(_A)
class _HmAgentStpCstBridgePriority_Type(Unsigned32):defaultValue=32768;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,61440))
_HmAgentStpCstBridgePriority_Type.__name__=_H
_HmAgentStpCstBridgePriority_Object=MibScalar
hmAgentStpCstBridgePriority=_HmAgentStpCstBridgePriority_Object((1,3,6,1,4,1,248,15,1,2,15,8,11),_HmAgentStpCstBridgePriority_Type())
hmAgentStpCstBridgePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentStpCstBridgePriority.setStatus(_A)
_HmAgentStpCstBridgeTimeSinceTopologyChange_Type=TimeTicks
_HmAgentStpCstBridgeTimeSinceTopologyChange_Object=MibScalar
hmAgentStpCstBridgeTimeSinceTopologyChange=_HmAgentStpCstBridgeTimeSinceTopologyChange_Object((1,3,6,1,4,1,248,15,1,2,15,8,12),_HmAgentStpCstBridgeTimeSinceTopologyChange_Type())
hmAgentStpCstBridgeTimeSinceTopologyChange.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentStpCstBridgeTimeSinceTopologyChange.setStatus(_A)
_HmAgentStpCstBridgeTopChanges_Type=Counter32
_HmAgentStpCstBridgeTopChanges_Object=MibScalar
hmAgentStpCstBridgeTopChanges=_HmAgentStpCstBridgeTopChanges_Object((1,3,6,1,4,1,248,15,1,2,15,8,13),_HmAgentStpCstBridgeTopChanges_Type())
hmAgentStpCstBridgeTopChanges.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentStpCstBridgeTopChanges.setStatus(_A)
_HmAgentStpCstBridgeRootCost_Type=Unsigned32
_HmAgentStpCstBridgeRootCost_Object=MibScalar
hmAgentStpCstBridgeRootCost=_HmAgentStpCstBridgeRootCost_Object((1,3,6,1,4,1,248,15,1,2,15,8,14),_HmAgentStpCstBridgeRootCost_Type())
hmAgentStpCstBridgeRootCost.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentStpCstBridgeRootCost.setStatus(_A)
_HmAgentStpCstBridgeRootPort_Type=Unsigned32
_HmAgentStpCstBridgeRootPort_Object=MibScalar
hmAgentStpCstBridgeRootPort=_HmAgentStpCstBridgeRootPort_Object((1,3,6,1,4,1,248,15,1,2,15,8,15),_HmAgentStpCstBridgeRootPort_Type())
hmAgentStpCstBridgeRootPort.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentStpCstBridgeRootPort.setStatus(_A)
class _HmAgentStpCstBridgeMaxHops_Type(Unsigned32):defaultValue=20;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(6,40))
_HmAgentStpCstBridgeMaxHops_Type.__name__=_H
_HmAgentStpCstBridgeMaxHops_Object=MibScalar
hmAgentStpCstBridgeMaxHops=_HmAgentStpCstBridgeMaxHops_Object((1,3,6,1,4,1,248,15,1,2,15,8,16),_HmAgentStpCstBridgeMaxHops_Type())
hmAgentStpCstBridgeMaxHops.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentStpCstBridgeMaxHops.setStatus(_A)
class _HmAgentStpCstBridgeHoldCount_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,40))
_HmAgentStpCstBridgeHoldCount_Type.__name__=_H
_HmAgentStpCstBridgeHoldCount_Object=MibScalar
hmAgentStpCstBridgeHoldCount=_HmAgentStpCstBridgeHoldCount_Object((1,3,6,1,4,1,248,15,1,2,15,8,17),_HmAgentStpCstBridgeHoldCount_Type())
hmAgentStpCstBridgeHoldCount.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentStpCstBridgeHoldCount.setStatus(_A)
_HmAgentStpCstPortTable_Object=MibTable
hmAgentStpCstPortTable=_HmAgentStpCstPortTable_Object((1,3,6,1,4,1,248,15,1,2,15,9))
if mibBuilder.loadTexts:hmAgentStpCstPortTable.setStatus(_A)
_HmAgentStpCstPortEntry_Object=MibTableRow
hmAgentStpCstPortEntry=_HmAgentStpCstPortEntry_Object((1,3,6,1,4,1,248,15,1,2,15,9,1))
hmAgentStpCstPortEntry.setIndexNames((0,_T,_U))
if mibBuilder.loadTexts:hmAgentStpCstPortEntry.setStatus(_A)
class _HmAgentStpCstPortOperEdge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_M,2)))
_HmAgentStpCstPortOperEdge_Type.__name__=_D
_HmAgentStpCstPortOperEdge_Object=MibTableColumn
hmAgentStpCstPortOperEdge=_HmAgentStpCstPortOperEdge_Object((1,3,6,1,4,1,248,15,1,2,15,9,1,1),_HmAgentStpCstPortOperEdge_Type())
hmAgentStpCstPortOperEdge.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentStpCstPortOperEdge.setStatus(_A)
class _HmAgentStpCstPortOperPointToPoint_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_M,2)))
_HmAgentStpCstPortOperPointToPoint_Type.__name__=_D
_HmAgentStpCstPortOperPointToPoint_Object=MibTableColumn
hmAgentStpCstPortOperPointToPoint=_HmAgentStpCstPortOperPointToPoint_Object((1,3,6,1,4,1,248,15,1,2,15,9,1,2),_HmAgentStpCstPortOperPointToPoint_Type())
hmAgentStpCstPortOperPointToPoint.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentStpCstPortOperPointToPoint.setStatus(_A)
class _HmAgentStpCstPortTopologyChangeAck_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_M,2)))
_HmAgentStpCstPortTopologyChangeAck_Type.__name__=_D
_HmAgentStpCstPortTopologyChangeAck_Object=MibTableColumn
hmAgentStpCstPortTopologyChangeAck=_HmAgentStpCstPortTopologyChangeAck_Object((1,3,6,1,4,1,248,15,1,2,15,9,1,3),_HmAgentStpCstPortTopologyChangeAck_Type())
hmAgentStpCstPortTopologyChangeAck.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentStpCstPortTopologyChangeAck.setStatus(_A)
class _HmAgentStpCstPortEdge_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_M,2)))
_HmAgentStpCstPortEdge_Type.__name__=_D
_HmAgentStpCstPortEdge_Object=MibTableColumn
hmAgentStpCstPortEdge=_HmAgentStpCstPortEdge_Object((1,3,6,1,4,1,248,15,1,2,15,9,1,4),_HmAgentStpCstPortEdge_Type())
hmAgentStpCstPortEdge.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentStpCstPortEdge.setStatus(_A)
class _HmAgentStpCstPortForwardingState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_AL,1),(_b,2),(_c,3),(_P,4),(_AM,5),(_AN,6)))
_HmAgentStpCstPortForwardingState_Type.__name__=_D
_HmAgentStpCstPortForwardingState_Object=MibTableColumn
hmAgentStpCstPortForwardingState=_HmAgentStpCstPortForwardingState_Object((1,3,6,1,4,1,248,15,1,2,15,9,1,5),_HmAgentStpCstPortForwardingState_Type())
hmAgentStpCstPortForwardingState.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentStpCstPortForwardingState.setStatus(_A)
_HmAgentStpCstPortId_Type=OctetString
_HmAgentStpCstPortId_Object=MibTableColumn
hmAgentStpCstPortId=_HmAgentStpCstPortId_Object((1,3,6,1,4,1,248,15,1,2,15,9,1,6),_HmAgentStpCstPortId_Type())
hmAgentStpCstPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentStpCstPortId.setStatus(_A)
class _HmAgentStpCstPortPathCost_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200000000))
_HmAgentStpCstPortPathCost_Type.__name__=_H
_HmAgentStpCstPortPathCost_Object=MibTableColumn
hmAgentStpCstPortPathCost=_HmAgentStpCstPortPathCost_Object((1,3,6,1,4,1,248,15,1,2,15,9,1,7),_HmAgentStpCstPortPathCost_Type())
hmAgentStpCstPortPathCost.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentStpCstPortPathCost.setStatus(_A)
class _HmAgentStpCstPortPriority_Type(Unsigned32):defaultValue=128;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,240))
_HmAgentStpCstPortPriority_Type.__name__=_H
_HmAgentStpCstPortPriority_Object=MibTableColumn
hmAgentStpCstPortPriority=_HmAgentStpCstPortPriority_Object((1,3,6,1,4,1,248,15,1,2,15,9,1,8),_HmAgentStpCstPortPriority_Type())
hmAgentStpCstPortPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentStpCstPortPriority.setStatus(_A)
class _HmAgentStpCstDesignatedBridgeId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_HmAgentStpCstDesignatedBridgeId_Type.__name__=_L
_HmAgentStpCstDesignatedBridgeId_Object=MibTableColumn
hmAgentStpCstDesignatedBridgeId=_HmAgentStpCstDesignatedBridgeId_Object((1,3,6,1,4,1,248,15,1,2,15,9,1,9),_HmAgentStpCstDesignatedBridgeId_Type())
hmAgentStpCstDesignatedBridgeId.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentStpCstDesignatedBridgeId.setStatus(_A)
_HmAgentStpCstDesignatedCost_Type=Unsigned32
_HmAgentStpCstDesignatedCost_Object=MibTableColumn
hmAgentStpCstDesignatedCost=_HmAgentStpCstDesignatedCost_Object((1,3,6,1,4,1,248,15,1,2,15,9,1,10),_HmAgentStpCstDesignatedCost_Type())
hmAgentStpCstDesignatedCost.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentStpCstDesignatedCost.setStatus(_A)
class _HmAgentStpCstDesignatedPortId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_HmAgentStpCstDesignatedPortId_Type.__name__=_L
_HmAgentStpCstDesignatedPortId_Object=MibTableColumn
hmAgentStpCstDesignatedPortId=_HmAgentStpCstDesignatedPortId_Object((1,3,6,1,4,1,248,15,1,2,15,9,1,11),_HmAgentStpCstDesignatedPortId_Type())
hmAgentStpCstDesignatedPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentStpCstDesignatedPortId.setStatus(_A)
class _HmAgentStpCstExtPortPathCost_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200000000))
_HmAgentStpCstExtPortPathCost_Type.__name__=_H
_HmAgentStpCstExtPortPathCost_Object=MibTableColumn
hmAgentStpCstExtPortPathCost=_HmAgentStpCstExtPortPathCost_Object((1,3,6,1,4,1,248,15,1,2,15,9,1,12),_HmAgentStpCstExtPortPathCost_Type())
hmAgentStpCstExtPortPathCost.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentStpCstExtPortPathCost.setStatus(_A)
class _HmAgentStpCstPortAutoEdge_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_M,2)))
_HmAgentStpCstPortAutoEdge_Type.__name__=_D
_HmAgentStpCstPortAutoEdge_Object=MibTableColumn
hmAgentStpCstPortAutoEdge=_HmAgentStpCstPortAutoEdge_Object((1,3,6,1,4,1,248,15,1,2,15,9,1,13),_HmAgentStpCstPortAutoEdge_Type())
hmAgentStpCstPortAutoEdge.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentStpCstPortAutoEdge.setStatus(_A)
class _HmAgentStpCstPortRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('root',1),(_AO,2),(_AP,3),('backup',4),('master',5),(_P,6)))
_HmAgentStpCstPortRole_Type.__name__=_D
_HmAgentStpCstPortRole_Object=MibTableColumn
hmAgentStpCstPortRole=_HmAgentStpCstPortRole_Object((1,3,6,1,4,1,248,15,1,2,15,9,1,14),_HmAgentStpCstPortRole_Type())
hmAgentStpCstPortRole.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentStpCstPortRole.setStatus(_A)
class _HmAgentStpCstPortDisputed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_M,2)))
_HmAgentStpCstPortDisputed_Type.__name__=_D
_HmAgentStpCstPortDisputed_Object=MibTableColumn
hmAgentStpCstPortDisputed=_HmAgentStpCstPortDisputed_Object((1,3,6,1,4,1,248,15,1,2,15,9,1,15),_HmAgentStpCstPortDisputed_Type())
hmAgentStpCstPortDisputed.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentStpCstPortDisputed.setStatus(_A)
class _HmAgentStpCstPortBpduGuardEffect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HmAgentStpCstPortBpduGuardEffect_Type.__name__=_D
_HmAgentStpCstPortBpduGuardEffect_Object=MibTableColumn
hmAgentStpCstPortBpduGuardEffect=_HmAgentStpCstPortBpduGuardEffect_Object((1,3,6,1,4,1,248,15,1,2,15,9,1,16),_HmAgentStpCstPortBpduGuardEffect_Type())
hmAgentStpCstPortBpduGuardEffect.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentStpCstPortBpduGuardEffect.setStatus(_A)
class _HmAgentStpCstPortBpduFilter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HmAgentStpCstPortBpduFilter_Type.__name__=_D
_HmAgentStpCstPortBpduFilter_Object=MibTableColumn
hmAgentStpCstPortBpduFilter=_HmAgentStpCstPortBpduFilter_Object((1,3,6,1,4,1,248,15,1,2,15,9,1,17),_HmAgentStpCstPortBpduFilter_Type())
hmAgentStpCstPortBpduFilter.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentStpCstPortBpduFilter.setStatus(_A)
class _HmAgentStpCstPortBpduFlood_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HmAgentStpCstPortBpduFlood_Type.__name__=_D
_HmAgentStpCstPortBpduFlood_Object=MibTableColumn
hmAgentStpCstPortBpduFlood=_HmAgentStpCstPortBpduFlood_Object((1,3,6,1,4,1,248,15,1,2,15,9,1,18),_HmAgentStpCstPortBpduFlood_Type())
hmAgentStpCstPortBpduFlood.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentStpCstPortBpduFlood.setStatus(_A)
class _HmAgentStpCstPortRootGuard_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HmAgentStpCstPortRootGuard_Type.__name__=_D
_HmAgentStpCstPortRootGuard_Object=MibTableColumn
hmAgentStpCstPortRootGuard=_HmAgentStpCstPortRootGuard_Object((1,3,6,1,4,1,248,15,1,2,15,9,1,19),_HmAgentStpCstPortRootGuard_Type())
hmAgentStpCstPortRootGuard.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentStpCstPortRootGuard.setStatus(_A)
class _HmAgentStpCstPortTCNGuard_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HmAgentStpCstPortTCNGuard_Type.__name__=_D
_HmAgentStpCstPortTCNGuard_Object=MibTableColumn
hmAgentStpCstPortTCNGuard=_HmAgentStpCstPortTCNGuard_Object((1,3,6,1,4,1,248,15,1,2,15,9,1,20),_HmAgentStpCstPortTCNGuard_Type())
hmAgentStpCstPortTCNGuard.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentStpCstPortTCNGuard.setStatus(_A)
class _HmAgentStpCstPortLoopGuard_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HmAgentStpCstPortLoopGuard_Type.__name__=_D
_HmAgentStpCstPortLoopGuard_Object=MibTableColumn
hmAgentStpCstPortLoopGuard=_HmAgentStpCstPortLoopGuard_Object((1,3,6,1,4,1,248,15,1,2,15,9,1,21),_HmAgentStpCstPortLoopGuard_Type())
hmAgentStpCstPortLoopGuard.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentStpCstPortLoopGuard.setStatus(_A)
_HmAgentStpMstTable_Object=MibTable
hmAgentStpMstTable=_HmAgentStpMstTable_Object((1,3,6,1,4,1,248,15,1,2,15,10))
if mibBuilder.loadTexts:hmAgentStpMstTable.setStatus(_A)
_HmAgentStpMstEntry_Object=MibTableRow
hmAgentStpMstEntry=_HmAgentStpMstEntry_Object((1,3,6,1,4,1,248,15,1,2,15,10,1))
hmAgentStpMstEntry.setIndexNames((0,_G,_S))
if mibBuilder.loadTexts:hmAgentStpMstEntry.setStatus(_A)
_HmAgentStpMstId_Type=Unsigned32
_HmAgentStpMstId_Object=MibTableColumn
hmAgentStpMstId=_HmAgentStpMstId_Object((1,3,6,1,4,1,248,15,1,2,15,10,1,1),_HmAgentStpMstId_Type())
hmAgentStpMstId.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentStpMstId.setStatus(_A)
class _HmAgentStpMstBridgePriority_Type(Unsigned32):defaultValue=32768;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,61440))
_HmAgentStpMstBridgePriority_Type.__name__=_H
_HmAgentStpMstBridgePriority_Object=MibTableColumn
hmAgentStpMstBridgePriority=_HmAgentStpMstBridgePriority_Object((1,3,6,1,4,1,248,15,1,2,15,10,1,2),_HmAgentStpMstBridgePriority_Type())
hmAgentStpMstBridgePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentStpMstBridgePriority.setStatus(_A)
class _HmAgentStpMstBridgeIdentifier_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_HmAgentStpMstBridgeIdentifier_Type.__name__=_L
_HmAgentStpMstBridgeIdentifier_Object=MibTableColumn
hmAgentStpMstBridgeIdentifier=_HmAgentStpMstBridgeIdentifier_Object((1,3,6,1,4,1,248,15,1,2,15,10,1,3),_HmAgentStpMstBridgeIdentifier_Type())
hmAgentStpMstBridgeIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentStpMstBridgeIdentifier.setStatus(_A)
class _HmAgentStpMstDesignatedRootId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_HmAgentStpMstDesignatedRootId_Type.__name__=_L
_HmAgentStpMstDesignatedRootId_Object=MibTableColumn
hmAgentStpMstDesignatedRootId=_HmAgentStpMstDesignatedRootId_Object((1,3,6,1,4,1,248,15,1,2,15,10,1,4),_HmAgentStpMstDesignatedRootId_Type())
hmAgentStpMstDesignatedRootId.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentStpMstDesignatedRootId.setStatus(_A)
_HmAgentStpMstRootPathCost_Type=Unsigned32
_HmAgentStpMstRootPathCost_Object=MibTableColumn
hmAgentStpMstRootPathCost=_HmAgentStpMstRootPathCost_Object((1,3,6,1,4,1,248,15,1,2,15,10,1,5),_HmAgentStpMstRootPathCost_Type())
hmAgentStpMstRootPathCost.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentStpMstRootPathCost.setStatus(_A)
_HmAgentStpMstRootPortId_Type=OctetString
_HmAgentStpMstRootPortId_Object=MibTableColumn
hmAgentStpMstRootPortId=_HmAgentStpMstRootPortId_Object((1,3,6,1,4,1,248,15,1,2,15,10,1,6),_HmAgentStpMstRootPortId_Type())
hmAgentStpMstRootPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentStpMstRootPortId.setStatus(_A)
_HmAgentStpMstTimeSinceTopologyChange_Type=TimeTicks
_HmAgentStpMstTimeSinceTopologyChange_Object=MibTableColumn
hmAgentStpMstTimeSinceTopologyChange=_HmAgentStpMstTimeSinceTopologyChange_Object((1,3,6,1,4,1,248,15,1,2,15,10,1,7),_HmAgentStpMstTimeSinceTopologyChange_Type())
hmAgentStpMstTimeSinceTopologyChange.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentStpMstTimeSinceTopologyChange.setStatus(_A)
_HmAgentStpMstTopologyChangeCount_Type=Counter32
_HmAgentStpMstTopologyChangeCount_Object=MibTableColumn
hmAgentStpMstTopologyChangeCount=_HmAgentStpMstTopologyChangeCount_Object((1,3,6,1,4,1,248,15,1,2,15,10,1,8),_HmAgentStpMstTopologyChangeCount_Type())
hmAgentStpMstTopologyChangeCount.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentStpMstTopologyChangeCount.setStatus(_A)
class _HmAgentStpMstTopologyChangeParm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_M,2)))
_HmAgentStpMstTopologyChangeParm_Type.__name__=_D
_HmAgentStpMstTopologyChangeParm_Object=MibTableColumn
hmAgentStpMstTopologyChangeParm=_HmAgentStpMstTopologyChangeParm_Object((1,3,6,1,4,1,248,15,1,2,15,10,1,9),_HmAgentStpMstTopologyChangeParm_Type())
hmAgentStpMstTopologyChangeParm.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentStpMstTopologyChangeParm.setStatus(_A)
_HmAgentStpMstRowStatus_Type=RowStatus
_HmAgentStpMstRowStatus_Object=MibTableColumn
hmAgentStpMstRowStatus=_HmAgentStpMstRowStatus_Object((1,3,6,1,4,1,248,15,1,2,15,10,1,10),_HmAgentStpMstRowStatus_Type())
hmAgentStpMstRowStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:hmAgentStpMstRowStatus.setStatus(_A)
_HmAgentStpMstPortTable_Object=MibTable
hmAgentStpMstPortTable=_HmAgentStpMstPortTable_Object((1,3,6,1,4,1,248,15,1,2,15,11))
if mibBuilder.loadTexts:hmAgentStpMstPortTable.setStatus(_A)
_HmAgentStpMstPortEntry_Object=MibTableRow
hmAgentStpMstPortEntry=_HmAgentStpMstPortEntry_Object((1,3,6,1,4,1,248,15,1,2,15,11,1))
hmAgentStpMstPortEntry.setIndexNames((0,_G,_S),(0,_T,_U))
if mibBuilder.loadTexts:hmAgentStpMstPortEntry.setStatus(_A)
class _HmAgentStpMstPortForwardingState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_AL,1),(_b,2),(_c,3),(_P,4),(_AM,5),(_AN,6)))
_HmAgentStpMstPortForwardingState_Type.__name__=_D
_HmAgentStpMstPortForwardingState_Object=MibTableColumn
hmAgentStpMstPortForwardingState=_HmAgentStpMstPortForwardingState_Object((1,3,6,1,4,1,248,15,1,2,15,11,1,1),_HmAgentStpMstPortForwardingState_Type())
hmAgentStpMstPortForwardingState.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentStpMstPortForwardingState.setStatus(_A)
_HmAgentStpMstPortId_Type=OctetString
_HmAgentStpMstPortId_Object=MibTableColumn
hmAgentStpMstPortId=_HmAgentStpMstPortId_Object((1,3,6,1,4,1,248,15,1,2,15,11,1,2),_HmAgentStpMstPortId_Type())
hmAgentStpMstPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentStpMstPortId.setStatus(_A)
class _HmAgentStpMstPortPathCost_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200000000))
_HmAgentStpMstPortPathCost_Type.__name__=_H
_HmAgentStpMstPortPathCost_Object=MibTableColumn
hmAgentStpMstPortPathCost=_HmAgentStpMstPortPathCost_Object((1,3,6,1,4,1,248,15,1,2,15,11,1,3),_HmAgentStpMstPortPathCost_Type())
hmAgentStpMstPortPathCost.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentStpMstPortPathCost.setStatus(_A)
class _HmAgentStpMstPortPriority_Type(Unsigned32):defaultValue=128;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,240))
_HmAgentStpMstPortPriority_Type.__name__=_H
_HmAgentStpMstPortPriority_Object=MibTableColumn
hmAgentStpMstPortPriority=_HmAgentStpMstPortPriority_Object((1,3,6,1,4,1,248,15,1,2,15,11,1,4),_HmAgentStpMstPortPriority_Type())
hmAgentStpMstPortPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentStpMstPortPriority.setStatus(_A)
class _HmAgentStpMstDesignatedBridgeId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_HmAgentStpMstDesignatedBridgeId_Type.__name__=_L
_HmAgentStpMstDesignatedBridgeId_Object=MibTableColumn
hmAgentStpMstDesignatedBridgeId=_HmAgentStpMstDesignatedBridgeId_Object((1,3,6,1,4,1,248,15,1,2,15,11,1,5),_HmAgentStpMstDesignatedBridgeId_Type())
hmAgentStpMstDesignatedBridgeId.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentStpMstDesignatedBridgeId.setStatus(_A)
_HmAgentStpMstDesignatedCost_Type=Unsigned32
_HmAgentStpMstDesignatedCost_Object=MibTableColumn
hmAgentStpMstDesignatedCost=_HmAgentStpMstDesignatedCost_Object((1,3,6,1,4,1,248,15,1,2,15,11,1,6),_HmAgentStpMstDesignatedCost_Type())
hmAgentStpMstDesignatedCost.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentStpMstDesignatedCost.setStatus(_A)
class _HmAgentStpMstDesignatedPortId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_HmAgentStpMstDesignatedPortId_Type.__name__=_L
_HmAgentStpMstDesignatedPortId_Object=MibTableColumn
hmAgentStpMstDesignatedPortId=_HmAgentStpMstDesignatedPortId_Object((1,3,6,1,4,1,248,15,1,2,15,11,1,7),_HmAgentStpMstDesignatedPortId_Type())
hmAgentStpMstDesignatedPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentStpMstDesignatedPortId.setStatus(_A)
class _HmAgentStpMstPortRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('root',1),(_AO,2),(_AP,3),('backup',4),('master',5),(_P,6)))
_HmAgentStpMstPortRole_Type.__name__=_D
_HmAgentStpMstPortRole_Object=MibTableColumn
hmAgentStpMstPortRole=_HmAgentStpMstPortRole_Object((1,3,6,1,4,1,248,15,1,2,15,11,1,8),_HmAgentStpMstPortRole_Type())
hmAgentStpMstPortRole.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentStpMstPortRole.setStatus(_A)
class _HmAgentStpMstPortDisputed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_M,2)))
_HmAgentStpMstPortDisputed_Type.__name__=_D
_HmAgentStpMstPortDisputed_Object=MibTableColumn
hmAgentStpMstPortDisputed=_HmAgentStpMstPortDisputed_Object((1,3,6,1,4,1,248,15,1,2,15,11,1,9),_HmAgentStpMstPortDisputed_Type())
hmAgentStpMstPortDisputed.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentStpMstPortDisputed.setStatus(_A)
class _HmAgentStpMstPortLoopInconsistentState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_M,0),(_N,1)))
_HmAgentStpMstPortLoopInconsistentState_Type.__name__=_D
_HmAgentStpMstPortLoopInconsistentState_Object=MibTableColumn
hmAgentStpMstPortLoopInconsistentState=_HmAgentStpMstPortLoopInconsistentState_Object((1,3,6,1,4,1,248,15,1,2,15,11,1,10),_HmAgentStpMstPortLoopInconsistentState_Type())
hmAgentStpMstPortLoopInconsistentState.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentStpMstPortLoopInconsistentState.setStatus(_A)
_HmAgentStpMstPortTransitionsIntoLoopInconsistentState_Type=Counter32
_HmAgentStpMstPortTransitionsIntoLoopInconsistentState_Object=MibTableColumn
hmAgentStpMstPortTransitionsIntoLoopInconsistentState=_HmAgentStpMstPortTransitionsIntoLoopInconsistentState_Object((1,3,6,1,4,1,248,15,1,2,15,11,1,11),_HmAgentStpMstPortTransitionsIntoLoopInconsistentState_Type())
hmAgentStpMstPortTransitionsIntoLoopInconsistentState.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentStpMstPortTransitionsIntoLoopInconsistentState.setStatus(_A)
_HmAgentStpMstPortTransitionsOutOfLoopInconsistentState_Type=Counter32
_HmAgentStpMstPortTransitionsOutOfLoopInconsistentState_Object=MibTableColumn
hmAgentStpMstPortTransitionsOutOfLoopInconsistentState=_HmAgentStpMstPortTransitionsOutOfLoopInconsistentState_Object((1,3,6,1,4,1,248,15,1,2,15,11,1,12),_HmAgentStpMstPortTransitionsOutOfLoopInconsistentState_Type())
hmAgentStpMstPortTransitionsOutOfLoopInconsistentState.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentStpMstPortTransitionsOutOfLoopInconsistentState.setStatus(_A)
class _HmAgentStpMstReceivedBridgeId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_HmAgentStpMstReceivedBridgeId_Type.__name__=_L
_HmAgentStpMstReceivedBridgeId_Object=MibTableColumn
hmAgentStpMstReceivedBridgeId=_HmAgentStpMstReceivedBridgeId_Object((1,3,6,1,4,1,248,15,1,2,15,11,1,13),_HmAgentStpMstReceivedBridgeId_Type())
hmAgentStpMstReceivedBridgeId.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentStpMstReceivedBridgeId.setStatus(_A)
_HmAgentStpMstReceivedRPC_Type=Unsigned32
_HmAgentStpMstReceivedRPC_Object=MibTableColumn
hmAgentStpMstReceivedRPC=_HmAgentStpMstReceivedRPC_Object((1,3,6,1,4,1,248,15,1,2,15,11,1,14),_HmAgentStpMstReceivedRPC_Type())
hmAgentStpMstReceivedRPC.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentStpMstReceivedRPC.setStatus(_A)
class _HmAgentStpMstReceivedPortId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_HmAgentStpMstReceivedPortId_Type.__name__=_L
_HmAgentStpMstReceivedPortId_Object=MibTableColumn
hmAgentStpMstReceivedPortId=_HmAgentStpMstReceivedPortId_Object((1,3,6,1,4,1,248,15,1,2,15,11,1,15),_HmAgentStpMstReceivedPortId_Type())
hmAgentStpMstReceivedPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentStpMstReceivedPortId.setStatus(_A)
_HmAgentStpMstVlanTable_Object=MibTable
hmAgentStpMstVlanTable=_HmAgentStpMstVlanTable_Object((1,3,6,1,4,1,248,15,1,2,15,12))
if mibBuilder.loadTexts:hmAgentStpMstVlanTable.setStatus(_A)
_HmAgentStpMstVlanEntry_Object=MibTableRow
hmAgentStpMstVlanEntry=_HmAgentStpMstVlanEntry_Object((1,3,6,1,4,1,248,15,1,2,15,12,1))
hmAgentStpMstVlanEntry.setIndexNames((0,_G,_S),(0,_O,_Q))
if mibBuilder.loadTexts:hmAgentStpMstVlanEntry.setStatus(_A)
_HmAgentStpMstVlanRowStatus_Type=RowStatus
_HmAgentStpMstVlanRowStatus_Object=MibTableColumn
hmAgentStpMstVlanRowStatus=_HmAgentStpMstVlanRowStatus_Object((1,3,6,1,4,1,248,15,1,2,15,12,1,1),_HmAgentStpMstVlanRowStatus_Type())
hmAgentStpMstVlanRowStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:hmAgentStpMstVlanRowStatus.setStatus(_A)
class _HmAgentStpBpduGuardMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HmAgentStpBpduGuardMode_Type.__name__=_D
_HmAgentStpBpduGuardMode_Object=MibScalar
hmAgentStpBpduGuardMode=_HmAgentStpBpduGuardMode_Object((1,3,6,1,4,1,248,15,1,2,15,13),_HmAgentStpBpduGuardMode_Type())
hmAgentStpBpduGuardMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentStpBpduGuardMode.setStatus(_A)
class _HmAgentStpBpduFilterDefault_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HmAgentStpBpduFilterDefault_Type.__name__=_D
_HmAgentStpBpduFilterDefault_Object=MibScalar
hmAgentStpBpduFilterDefault=_HmAgentStpBpduFilterDefault_Object((1,3,6,1,4,1,248,15,1,2,15,14),_HmAgentStpBpduFilterDefault_Type())
hmAgentStpBpduFilterDefault.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentStpBpduFilterDefault.setStatus(_A)
_HmAgentClassOfServiceGroup_ObjectIdentity=ObjectIdentity
hmAgentClassOfServiceGroup=_HmAgentClassOfServiceGroup_ObjectIdentity((1,3,6,1,4,1,248,15,1,2,17))
_HmAgentClassOfServicePortTable_Object=MibTable
hmAgentClassOfServicePortTable=_HmAgentClassOfServicePortTable_Object((1,3,6,1,4,1,248,15,1,2,17,1))
if mibBuilder.loadTexts:hmAgentClassOfServicePortTable.setStatus(_A)
_HmAgentClassOfServicePortEntry_Object=MibTableRow
hmAgentClassOfServicePortEntry=_HmAgentClassOfServicePortEntry_Object((1,3,6,1,4,1,248,15,1,2,17,1,1))
hmAgentClassOfServicePortEntry.setIndexNames((0,_T,_U),(0,_G,_AQ))
if mibBuilder.loadTexts:hmAgentClassOfServicePortEntry.setStatus(_A)
class _HmAgentClassOfServicePortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HmAgentClassOfServicePortPriority_Type.__name__=_D
_HmAgentClassOfServicePortPriority_Object=MibTableColumn
hmAgentClassOfServicePortPriority=_HmAgentClassOfServicePortPriority_Object((1,3,6,1,4,1,248,15,1,2,17,1,1,1),_HmAgentClassOfServicePortPriority_Type())
hmAgentClassOfServicePortPriority.setMaxAccess(_R)
if mibBuilder.loadTexts:hmAgentClassOfServicePortPriority.setStatus(_A)
class _HmAgentClassOfServicePortClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HmAgentClassOfServicePortClass_Type.__name__=_D
_HmAgentClassOfServicePortClass_Object=MibTableColumn
hmAgentClassOfServicePortClass=_HmAgentClassOfServicePortClass_Object((1,3,6,1,4,1,248,15,1,2,17,1,1,2),_HmAgentClassOfServicePortClass_Type())
hmAgentClassOfServicePortClass.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentClassOfServicePortClass.setStatus(_A)
_HmAgentSystemGroup_ObjectIdentity=ObjectIdentity
hmAgentSystemGroup=_HmAgentSystemGroup_ObjectIdentity((1,3,6,1,4,1,248,15,1,3))
class _HmAgentSaveConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HmAgentSaveConfig_Type.__name__=_D
_HmAgentSaveConfig_Object=MibScalar
hmAgentSaveConfig=_HmAgentSaveConfig_Object((1,3,6,1,4,1,248,15,1,3,1),_HmAgentSaveConfig_Type())
hmAgentSaveConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentSaveConfig.setStatus(_A)
class _HmAgentClearConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HmAgentClearConfig_Type.__name__=_D
_HmAgentClearConfig_Object=MibScalar
hmAgentClearConfig=_HmAgentClearConfig_Object((1,3,6,1,4,1,248,15,1,3,2),_HmAgentClearConfig_Type())
hmAgentClearConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentClearConfig.setStatus(_A)
class _HmAgentClearLags_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HmAgentClearLags_Type.__name__=_D
_HmAgentClearLags_Object=MibScalar
hmAgentClearLags=_HmAgentClearLags_Object((1,3,6,1,4,1,248,15,1,3,3),_HmAgentClearLags_Type())
hmAgentClearLags.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentClearLags.setStatus(_A)
class _HmAgentClearLoginSessions_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HmAgentClearLoginSessions_Type.__name__=_D
_HmAgentClearLoginSessions_Object=MibScalar
hmAgentClearLoginSessions=_HmAgentClearLoginSessions_Object((1,3,6,1,4,1,248,15,1,3,4),_HmAgentClearLoginSessions_Type())
hmAgentClearLoginSessions.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentClearLoginSessions.setStatus(_A)
class _HmAgentClearPasswords_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HmAgentClearPasswords_Type.__name__=_D
_HmAgentClearPasswords_Object=MibScalar
hmAgentClearPasswords=_HmAgentClearPasswords_Object((1,3,6,1,4,1,248,15,1,3,5),_HmAgentClearPasswords_Type())
hmAgentClearPasswords.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentClearPasswords.setStatus(_A)
class _HmAgentClearPortStats_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HmAgentClearPortStats_Type.__name__=_D
_HmAgentClearPortStats_Object=MibScalar
hmAgentClearPortStats=_HmAgentClearPortStats_Object((1,3,6,1,4,1,248,15,1,3,6),_HmAgentClearPortStats_Type())
hmAgentClearPortStats.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentClearPortStats.setStatus(_A)
class _HmAgentClearSwitchStats_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HmAgentClearSwitchStats_Type.__name__=_D
_HmAgentClearSwitchStats_Object=MibScalar
hmAgentClearSwitchStats=_HmAgentClearSwitchStats_Object((1,3,6,1,4,1,248,15,1,3,7),_HmAgentClearSwitchStats_Type())
hmAgentClearSwitchStats.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentClearSwitchStats.setStatus(_A)
class _HmAgentClearTrapLog_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HmAgentClearTrapLog_Type.__name__=_D
_HmAgentClearTrapLog_Object=MibScalar
hmAgentClearTrapLog=_HmAgentClearTrapLog_Object((1,3,6,1,4,1,248,15,1,3,8),_HmAgentClearTrapLog_Type())
hmAgentClearTrapLog.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentClearTrapLog.setStatus(_A)
class _HmAgentClearVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HmAgentClearVlan_Type.__name__=_D
_HmAgentClearVlan_Object=MibScalar
hmAgentClearVlan=_HmAgentClearVlan_Object((1,3,6,1,4,1,248,15,1,3,9),_HmAgentClearVlan_Type())
hmAgentClearVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentClearVlan.setStatus(_A)
class _HmAgentResetSystem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HmAgentResetSystem_Type.__name__=_D
_HmAgentResetSystem_Object=MibScalar
hmAgentResetSystem=_HmAgentResetSystem_Object((1,3,6,1,4,1,248,15,1,3,10),_HmAgentResetSystem_Type())
hmAgentResetSystem.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentResetSystem.setStatus(_A)
class _HmAgentSaveConfigStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_a,1),('savingInProcess',2),('savingComplete',3)))
_HmAgentSaveConfigStatus_Type.__name__=_D
_HmAgentSaveConfigStatus_Object=MibScalar
hmAgentSaveConfigStatus=_HmAgentSaveConfigStatus_Object((1,3,6,1,4,1,248,15,1,3,11),_HmAgentSaveConfigStatus_Type())
hmAgentSaveConfigStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentSaveConfigStatus.setStatus(_A)
_HmAgentCableTesterGroup_ObjectIdentity=ObjectIdentity
hmAgentCableTesterGroup=_HmAgentCableTesterGroup_ObjectIdentity((1,3,6,1,4,1,248,15,1,4))
class _HmAgentCableTesterStatus_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_p,1),('success',2),('failure',3),('uninitialized',4)))
_HmAgentCableTesterStatus_Type.__name__=_D
_HmAgentCableTesterStatus_Object=MibScalar
hmAgentCableTesterStatus=_HmAgentCableTesterStatus_Object((1,3,6,1,4,1,248,15,1,4,1),_HmAgentCableTesterStatus_Type())
hmAgentCableTesterStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentCableTesterStatus.setStatus(_A)
class _HmAgentCableTesterIfIndex_Type(Unsigned32):defaultValue=0
_HmAgentCableTesterIfIndex_Type.__name__=_H
_HmAgentCableTesterIfIndex_Object=MibScalar
hmAgentCableTesterIfIndex=_HmAgentCableTesterIfIndex_Object((1,3,6,1,4,1,248,15,1,4,2),_HmAgentCableTesterIfIndex_Type())
hmAgentCableTesterIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentCableTesterIfIndex.setStatus(_A)
class _HmAgentCableTesterCableStatus_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('normal',1),('open',2),('short',3),('unknown',4)))
_HmAgentCableTesterCableStatus_Type.__name__=_D
_HmAgentCableTesterCableStatus_Object=MibScalar
hmAgentCableTesterCableStatus=_HmAgentCableTesterCableStatus_Object((1,3,6,1,4,1,248,15,1,4,3),_HmAgentCableTesterCableStatus_Type())
hmAgentCableTesterCableStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentCableTesterCableStatus.setStatus(_A)
class _HmAgentCableTesterMinimumCableLength_Type(Unsigned32):defaultValue=0
_HmAgentCableTesterMinimumCableLength_Type.__name__=_H
_HmAgentCableTesterMinimumCableLength_Object=MibScalar
hmAgentCableTesterMinimumCableLength=_HmAgentCableTesterMinimumCableLength_Object((1,3,6,1,4,1,248,15,1,4,4),_HmAgentCableTesterMinimumCableLength_Type())
hmAgentCableTesterMinimumCableLength.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentCableTesterMinimumCableLength.setStatus(_A)
class _HmAgentCableTesterMaximumCableLength_Type(Unsigned32):defaultValue=0
_HmAgentCableTesterMaximumCableLength_Type.__name__=_H
_HmAgentCableTesterMaximumCableLength_Object=MibScalar
hmAgentCableTesterMaximumCableLength=_HmAgentCableTesterMaximumCableLength_Object((1,3,6,1,4,1,248,15,1,4,5),_HmAgentCableTesterMaximumCableLength_Type())
hmAgentCableTesterMaximumCableLength.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentCableTesterMaximumCableLength.setStatus(_A)
class _HmAgentCableTesterCableFailureLocation_Type(Unsigned32):defaultValue=0
_HmAgentCableTesterCableFailureLocation_Type.__name__=_H
_HmAgentCableTesterCableFailureLocation_Object=MibScalar
hmAgentCableTesterCableFailureLocation=_HmAgentCableTesterCableFailureLocation_Object((1,3,6,1,4,1,248,15,1,4,6),_HmAgentCableTesterCableFailureLocation_Type())
hmAgentCableTesterCableFailureLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentCableTesterCableFailureLocation.setStatus(_A)
_HmPlatform4SwitchingTraps_ObjectIdentity=ObjectIdentity
hmPlatform4SwitchingTraps=_HmPlatform4SwitchingTraps_ObjectIdentity((1,3,6,1,4,1,248,15,1,50))
_HmRadius_ObjectIdentity=ObjectIdentity
hmRadius=_HmRadius_ObjectIdentity((1,3,6,1,4,1,248,15,8))
_HmAgentRadiusConfigGroup_ObjectIdentity=ObjectIdentity
hmAgentRadiusConfigGroup=_HmAgentRadiusConfigGroup_ObjectIdentity((1,3,6,1,4,1,248,15,8,1))
class _HmAgentRadiusMaxTransmit_Type(Unsigned32):defaultValue=4;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_HmAgentRadiusMaxTransmit_Type.__name__=_H
_HmAgentRadiusMaxTransmit_Object=MibScalar
hmAgentRadiusMaxTransmit=_HmAgentRadiusMaxTransmit_Object((1,3,6,1,4,1,248,15,8,1,1),_HmAgentRadiusMaxTransmit_Type())
hmAgentRadiusMaxTransmit.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentRadiusMaxTransmit.setStatus(_A)
class _HmAgentRadiusTimeout_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_HmAgentRadiusTimeout_Type.__name__=_H
_HmAgentRadiusTimeout_Object=MibScalar
hmAgentRadiusTimeout=_HmAgentRadiusTimeout_Object((1,3,6,1,4,1,248,15,8,1,2),_HmAgentRadiusTimeout_Type())
hmAgentRadiusTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentRadiusTimeout.setStatus(_A)
class _HmAgentRadiusAccountingMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HmAgentRadiusAccountingMode_Type.__name__=_D
_HmAgentRadiusAccountingMode_Object=MibScalar
hmAgentRadiusAccountingMode=_HmAgentRadiusAccountingMode_Object((1,3,6,1,4,1,248,15,8,1,3),_HmAgentRadiusAccountingMode_Type())
hmAgentRadiusAccountingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentRadiusAccountingMode.setStatus(_A)
class _HmAgentRadiusStatsClear_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HmAgentRadiusStatsClear_Type.__name__=_D
_HmAgentRadiusStatsClear_Object=MibScalar
hmAgentRadiusStatsClear=_HmAgentRadiusStatsClear_Object((1,3,6,1,4,1,248,15,8,1,4),_HmAgentRadiusStatsClear_Type())
hmAgentRadiusStatsClear.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentRadiusStatsClear.setStatus(_A)
class _HmAgentRadiusAccountingIndexNextValid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,2147483647))
_HmAgentRadiusAccountingIndexNextValid_Type.__name__=_D
_HmAgentRadiusAccountingIndexNextValid_Object=MibScalar
hmAgentRadiusAccountingIndexNextValid=_HmAgentRadiusAccountingIndexNextValid_Object((1,3,6,1,4,1,248,15,8,1,5),_HmAgentRadiusAccountingIndexNextValid_Type())
hmAgentRadiusAccountingIndexNextValid.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentRadiusAccountingIndexNextValid.setStatus(_A)
_HmAgentRadiusAccountingConfigTable_Object=MibTable
hmAgentRadiusAccountingConfigTable=_HmAgentRadiusAccountingConfigTable_Object((1,3,6,1,4,1,248,15,8,1,6))
if mibBuilder.loadTexts:hmAgentRadiusAccountingConfigTable.setStatus(_A)
_HmAgentRadiusAccountingConfigEntry_Object=MibTableRow
hmAgentRadiusAccountingConfigEntry=_HmAgentRadiusAccountingConfigEntry_Object((1,3,6,1,4,1,248,15,8,1,6,1))
hmAgentRadiusAccountingConfigEntry.setIndexNames((0,_G,_AR))
if mibBuilder.loadTexts:hmAgentRadiusAccountingConfigEntry.setStatus(_A)
class _HmAgentRadiusAccountingServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HmAgentRadiusAccountingServerIndex_Type.__name__=_D
_HmAgentRadiusAccountingServerIndex_Object=MibTableColumn
hmAgentRadiusAccountingServerIndex=_HmAgentRadiusAccountingServerIndex_Object((1,3,6,1,4,1,248,15,8,1,6,1,1),_HmAgentRadiusAccountingServerIndex_Type())
hmAgentRadiusAccountingServerIndex.setMaxAccess(_R)
if mibBuilder.loadTexts:hmAgentRadiusAccountingServerIndex.setStatus(_A)
_HmAgentRadiusAccountingServerAddress_Type=IpAddress
_HmAgentRadiusAccountingServerAddress_Object=MibTableColumn
hmAgentRadiusAccountingServerAddress=_HmAgentRadiusAccountingServerAddress_Object((1,3,6,1,4,1,248,15,8,1,6,1,2),_HmAgentRadiusAccountingServerAddress_Type())
hmAgentRadiusAccountingServerAddress.setMaxAccess(_K)
if mibBuilder.loadTexts:hmAgentRadiusAccountingServerAddress.setStatus(_A)
class _HmAgentRadiusAccountingPort_Type(Unsigned32):defaultValue=1813;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HmAgentRadiusAccountingPort_Type.__name__=_H
_HmAgentRadiusAccountingPort_Object=MibTableColumn
hmAgentRadiusAccountingPort=_HmAgentRadiusAccountingPort_Object((1,3,6,1,4,1,248,15,8,1,6,1,3),_HmAgentRadiusAccountingPort_Type())
hmAgentRadiusAccountingPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentRadiusAccountingPort.setStatus(_A)
class _HmAgentRadiusAccountingSecret_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_HmAgentRadiusAccountingSecret_Type.__name__=_I
_HmAgentRadiusAccountingSecret_Object=MibTableColumn
hmAgentRadiusAccountingSecret=_HmAgentRadiusAccountingSecret_Object((1,3,6,1,4,1,248,15,8,1,6,1,4),_HmAgentRadiusAccountingSecret_Type())
hmAgentRadiusAccountingSecret.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentRadiusAccountingSecret.setStatus(_A)
_HmAgentRadiusAccountingStatus_Type=RowStatus
_HmAgentRadiusAccountingStatus_Object=MibTableColumn
hmAgentRadiusAccountingStatus=_HmAgentRadiusAccountingStatus_Object((1,3,6,1,4,1,248,15,8,1,6,1,5),_HmAgentRadiusAccountingStatus_Type())
hmAgentRadiusAccountingStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:hmAgentRadiusAccountingStatus.setStatus(_A)
class _HmAgentRadiusServerIndexNextValid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,2147483647))
_HmAgentRadiusServerIndexNextValid_Type.__name__=_D
_HmAgentRadiusServerIndexNextValid_Object=MibScalar
hmAgentRadiusServerIndexNextValid=_HmAgentRadiusServerIndexNextValid_Object((1,3,6,1,4,1,248,15,8,1,7),_HmAgentRadiusServerIndexNextValid_Type())
hmAgentRadiusServerIndexNextValid.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentRadiusServerIndexNextValid.setStatus(_A)
_HmAgentRadiusServerConfigTable_Object=MibTable
hmAgentRadiusServerConfigTable=_HmAgentRadiusServerConfigTable_Object((1,3,6,1,4,1,248,15,8,1,8))
if mibBuilder.loadTexts:hmAgentRadiusServerConfigTable.setStatus(_A)
_HmAgentRadiusServerConfigEntry_Object=MibTableRow
hmAgentRadiusServerConfigEntry=_HmAgentRadiusServerConfigEntry_Object((1,3,6,1,4,1,248,15,8,1,8,1))
hmAgentRadiusServerConfigEntry.setIndexNames((0,_G,_AS))
if mibBuilder.loadTexts:hmAgentRadiusServerConfigEntry.setStatus(_A)
class _HmAgentRadiusServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HmAgentRadiusServerIndex_Type.__name__=_D
_HmAgentRadiusServerIndex_Object=MibTableColumn
hmAgentRadiusServerIndex=_HmAgentRadiusServerIndex_Object((1,3,6,1,4,1,248,15,8,1,8,1,1),_HmAgentRadiusServerIndex_Type())
hmAgentRadiusServerIndex.setMaxAccess(_R)
if mibBuilder.loadTexts:hmAgentRadiusServerIndex.setStatus(_A)
_HmAgentRadiusServerAddress_Type=IpAddress
_HmAgentRadiusServerAddress_Object=MibTableColumn
hmAgentRadiusServerAddress=_HmAgentRadiusServerAddress_Object((1,3,6,1,4,1,248,15,8,1,8,1,2),_HmAgentRadiusServerAddress_Type())
hmAgentRadiusServerAddress.setMaxAccess(_K)
if mibBuilder.loadTexts:hmAgentRadiusServerAddress.setStatus(_A)
class _HmAgentRadiusServerPort_Type(Unsigned32):defaultValue=1812;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HmAgentRadiusServerPort_Type.__name__=_H
_HmAgentRadiusServerPort_Object=MibTableColumn
hmAgentRadiusServerPort=_HmAgentRadiusServerPort_Object((1,3,6,1,4,1,248,15,8,1,8,1,3),_HmAgentRadiusServerPort_Type())
hmAgentRadiusServerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentRadiusServerPort.setStatus(_A)
class _HmAgentRadiusServerSecret_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,25))
_HmAgentRadiusServerSecret_Type.__name__=_I
_HmAgentRadiusServerSecret_Object=MibTableColumn
hmAgentRadiusServerSecret=_HmAgentRadiusServerSecret_Object((1,3,6,1,4,1,248,15,8,1,8,1,4),_HmAgentRadiusServerSecret_Type())
hmAgentRadiusServerSecret.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentRadiusServerSecret.setStatus(_A)
class _HmAgentRadiusServerPrimaryMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HmAgentRadiusServerPrimaryMode_Type.__name__=_D
_HmAgentRadiusServerPrimaryMode_Object=MibTableColumn
hmAgentRadiusServerPrimaryMode=_HmAgentRadiusServerPrimaryMode_Object((1,3,6,1,4,1,248,15,8,1,8,1,5),_HmAgentRadiusServerPrimaryMode_Type())
hmAgentRadiusServerPrimaryMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentRadiusServerPrimaryMode.setStatus(_A)
class _HmAgentRadiusServerCurrentMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_HmAgentRadiusServerCurrentMode_Type.__name__=_D
_HmAgentRadiusServerCurrentMode_Object=MibTableColumn
hmAgentRadiusServerCurrentMode=_HmAgentRadiusServerCurrentMode_Object((1,3,6,1,4,1,248,15,8,1,8,1,6),_HmAgentRadiusServerCurrentMode_Type())
hmAgentRadiusServerCurrentMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentRadiusServerCurrentMode.setStatus(_A)
class _HmAgentRadiusServerMsgAuth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HmAgentRadiusServerMsgAuth_Type.__name__=_D
_HmAgentRadiusServerMsgAuth_Object=MibTableColumn
hmAgentRadiusServerMsgAuth=_HmAgentRadiusServerMsgAuth_Object((1,3,6,1,4,1,248,15,8,1,8,1,7),_HmAgentRadiusServerMsgAuth_Type())
hmAgentRadiusServerMsgAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentRadiusServerMsgAuth.setStatus(_A)
_HmAgentRadiusServerStatus_Type=RowStatus
_HmAgentRadiusServerStatus_Object=MibTableColumn
hmAgentRadiusServerStatus=_HmAgentRadiusServerStatus_Object((1,3,6,1,4,1,248,15,8,1,8,1,8),_HmAgentRadiusServerStatus_Type())
hmAgentRadiusServerStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:hmAgentRadiusServerStatus.setStatus(_A)
_HmAgentMgmtSecurity_ObjectIdentity=ObjectIdentity
hmAgentMgmtSecurity=_HmAgentMgmtSecurity_ObjectIdentity((1,3,6,1,4,1,248,15,11))
_HmAgentSSHConfigGroup_ObjectIdentity=ObjectIdentity
hmAgentSSHConfigGroup=_HmAgentSSHConfigGroup_ObjectIdentity((1,3,6,1,4,1,248,15,11,2))
class _HmAgentSSHAdminMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HmAgentSSHAdminMode_Type.__name__=_D
_HmAgentSSHAdminMode_Object=MibScalar
hmAgentSSHAdminMode=_HmAgentSSHAdminMode_Object((1,3,6,1,4,1,248,15,11,2,1),_HmAgentSSHAdminMode_Type())
hmAgentSSHAdminMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentSSHAdminMode.setStatus(_A)
class _HmAgentSSHProtocolLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ssh10',1),('ssh20',2),('both',3)))
_HmAgentSSHProtocolLevel_Type.__name__=_D
_HmAgentSSHProtocolLevel_Object=MibScalar
hmAgentSSHProtocolLevel=_HmAgentSSHProtocolLevel_Object((1,3,6,1,4,1,248,15,11,2,2),_HmAgentSSHProtocolLevel_Type())
hmAgentSSHProtocolLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentSSHProtocolLevel.setStatus(_A)
_HmAgentSSHSessionsCount_Type=Integer32
_HmAgentSSHSessionsCount_Object=MibScalar
hmAgentSSHSessionsCount=_HmAgentSSHSessionsCount_Object((1,3,6,1,4,1,248,15,11,2,3),_HmAgentSSHSessionsCount_Type())
hmAgentSSHSessionsCount.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentSSHSessionsCount.setStatus(_A)
class _HmAgentSSHMaxSessionsCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_HmAgentSSHMaxSessionsCount_Type.__name__=_D
_HmAgentSSHMaxSessionsCount_Object=MibScalar
hmAgentSSHMaxSessionsCount=_HmAgentSSHMaxSessionsCount_Object((1,3,6,1,4,1,248,15,11,2,4),_HmAgentSSHMaxSessionsCount_Type())
hmAgentSSHMaxSessionsCount.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentSSHMaxSessionsCount.setStatus(_A)
class _HmAgentSSHSessionTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,160))
_HmAgentSSHSessionTimeout_Type.__name__=_D
_HmAgentSSHSessionTimeout_Object=MibScalar
hmAgentSSHSessionTimeout=_HmAgentSSHSessionTimeout_Object((1,3,6,1,4,1,248,15,11,2,5),_HmAgentSSHSessionTimeout_Type())
hmAgentSSHSessionTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentSSHSessionTimeout.setStatus(_A)
_HmAgentLogging_ObjectIdentity=ObjectIdentity
hmAgentLogging=_HmAgentLogging_ObjectIdentity((1,3,6,1,4,1,248,15,14))
_HmAgentLogConfigGroup_ObjectIdentity=ObjectIdentity
hmAgentLogConfigGroup=_HmAgentLogConfigGroup_ObjectIdentity((1,3,6,1,4,1,248,15,14,1))
_HmAgentLogSysLogConfigGroup_ObjectIdentity=ObjectIdentity
hmAgentLogSysLogConfigGroup=_HmAgentLogSysLogConfigGroup_ObjectIdentity((1,3,6,1,4,1,248,15,14,1,4))
class _HmAgentLogSyslogAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HmAgentLogSyslogAdminStatus_Type.__name__=_D
_HmAgentLogSyslogAdminStatus_Object=MibScalar
hmAgentLogSyslogAdminStatus=_HmAgentLogSyslogAdminStatus_Object((1,3,6,1,4,1,248,15,14,1,4,1),_HmAgentLogSyslogAdminStatus_Type())
hmAgentLogSyslogAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentLogSyslogAdminStatus.setStatus(_A)
_HmAgentLogSyslogHostTable_Object=MibTable
hmAgentLogSyslogHostTable=_HmAgentLogSyslogHostTable_Object((1,3,6,1,4,1,248,15,14,1,4,5))
if mibBuilder.loadTexts:hmAgentLogSyslogHostTable.setStatus(_A)
_HmAgentLogSyslogHostEntry_Object=MibTableRow
hmAgentLogSyslogHostEntry=_HmAgentLogSyslogHostEntry_Object((1,3,6,1,4,1,248,15,14,1,4,5,1))
hmAgentLogSyslogHostEntry.setIndexNames((0,_G,_AT))
if mibBuilder.loadTexts:hmAgentLogSyslogHostEntry.setStatus(_A)
_HmAgentLogHostTableIndex_Type=Unsigned32
_HmAgentLogHostTableIndex_Object=MibTableColumn
hmAgentLogHostTableIndex=_HmAgentLogHostTableIndex_Object((1,3,6,1,4,1,248,15,14,1,4,5,1,1),_HmAgentLogHostTableIndex_Type())
hmAgentLogHostTableIndex.setMaxAccess(_R)
if mibBuilder.loadTexts:hmAgentLogHostTableIndex.setStatus(_A)
class _HmAgentLogHostTableIpAddress_Type(IpAddress):defaultHexValue='00000000'
_HmAgentLogHostTableIpAddress_Type.__name__=_g
_HmAgentLogHostTableIpAddress_Object=MibTableColumn
hmAgentLogHostTableIpAddress=_HmAgentLogHostTableIpAddress_Object((1,3,6,1,4,1,248,15,14,1,4,5,1,3),_HmAgentLogHostTableIpAddress_Type())
hmAgentLogHostTableIpAddress.setMaxAccess(_K)
if mibBuilder.loadTexts:hmAgentLogHostTableIpAddress.setStatus(_A)
class _HmAgentLogHostTablePort_Type(Unsigned32):defaultValue=514;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HmAgentLogHostTablePort_Type.__name__=_H
_HmAgentLogHostTablePort_Object=MibTableColumn
hmAgentLogHostTablePort=_HmAgentLogHostTablePort_Object((1,3,6,1,4,1,248,15,14,1,4,5,1,4),_HmAgentLogHostTablePort_Type())
hmAgentLogHostTablePort.setMaxAccess(_K)
if mibBuilder.loadTexts:hmAgentLogHostTablePort.setStatus(_A)
class _HmAgentLogHostTableSeverityFilter_Type(HmAgentLogSeverity):defaultValue=2
_HmAgentLogHostTableSeverityFilter_Type.__name__=_e
_HmAgentLogHostTableSeverityFilter_Object=MibTableColumn
hmAgentLogHostTableSeverityFilter=_HmAgentLogHostTableSeverityFilter_Object((1,3,6,1,4,1,248,15,14,1,4,5,1,5),_HmAgentLogHostTableSeverityFilter_Type())
hmAgentLogHostTableSeverityFilter.setMaxAccess(_K)
if mibBuilder.loadTexts:hmAgentLogHostTableSeverityFilter.setStatus(_A)
_HmAgentLogHostTableRowStatus_Type=RowStatus
_HmAgentLogHostTableRowStatus_Object=MibTableColumn
hmAgentLogHostTableRowStatus=_HmAgentLogHostTableRowStatus_Object((1,3,6,1,4,1,248,15,14,1,4,5,1,7),_HmAgentLogHostTableRowStatus_Type())
hmAgentLogHostTableRowStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:hmAgentLogHostTableRowStatus.setStatus(_A)
_HmPlatform4OutboundTelnetPrivate_ObjectIdentity=ObjectIdentity
hmPlatform4OutboundTelnetPrivate=_HmPlatform4OutboundTelnetPrivate_ObjectIdentity((1,3,6,1,4,1,248,15,19))
_HmAgentOutboundTelnetGroup_ObjectIdentity=ObjectIdentity
hmAgentOutboundTelnetGroup=_HmAgentOutboundTelnetGroup_ObjectIdentity((1,3,6,1,4,1,248,15,19,1))
class _HmAgentOutboundTelnetAdminMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HmAgentOutboundTelnetAdminMode_Type.__name__=_D
_HmAgentOutboundTelnetAdminMode_Object=MibScalar
hmAgentOutboundTelnetAdminMode=_HmAgentOutboundTelnetAdminMode_Object((1,3,6,1,4,1,248,15,19,1,1),_HmAgentOutboundTelnetAdminMode_Type())
hmAgentOutboundTelnetAdminMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentOutboundTelnetAdminMode.setStatus(_A)
class _HmAgentOutboundTelnetMaxNoOfSessions_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_HmAgentOutboundTelnetMaxNoOfSessions_Type.__name__=_D
_HmAgentOutboundTelnetMaxNoOfSessions_Object=MibScalar
hmAgentOutboundTelnetMaxNoOfSessions=_HmAgentOutboundTelnetMaxNoOfSessions_Object((1,3,6,1,4,1,248,15,19,1,2),_HmAgentOutboundTelnetMaxNoOfSessions_Type())
hmAgentOutboundTelnetMaxNoOfSessions.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentOutboundTelnetMaxNoOfSessions.setStatus(_A)
class _HmAgentOutboundTelnetTimeout_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,160))
_HmAgentOutboundTelnetTimeout_Type.__name__=_D
_HmAgentOutboundTelnetTimeout_Object=MibScalar
hmAgentOutboundTelnetTimeout=_HmAgentOutboundTelnetTimeout_Object((1,3,6,1,4,1,248,15,19,1,3),_HmAgentOutboundTelnetTimeout_Type())
hmAgentOutboundTelnetTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentOutboundTelnetTimeout.setStatus(_A)
_HmAgentDot1xAdvanced_ObjectIdentity=ObjectIdentity
hmAgentDot1xAdvanced=_HmAgentDot1xAdvanced_ObjectIdentity((1,3,6,1,4,1,248,15,36))
_HmAgentDot1xEnhancementConfigGroup_ObjectIdentity=ObjectIdentity
hmAgentDot1xEnhancementConfigGroup=_HmAgentDot1xEnhancementConfigGroup_ObjectIdentity((1,3,6,1,4,1,248,15,36,1))
class _HmAgentDot1xRadiusVlanAssignment_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HmAgentDot1xRadiusVlanAssignment_Type.__name__=_D
_HmAgentDot1xRadiusVlanAssignment_Object=MibScalar
hmAgentDot1xRadiusVlanAssignment=_HmAgentDot1xRadiusVlanAssignment_Object((1,3,6,1,4,1,248,15,36,1,1),_HmAgentDot1xRadiusVlanAssignment_Type())
hmAgentDot1xRadiusVlanAssignment.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentDot1xRadiusVlanAssignment.setStatus(_A)
class _HmAgentDot1xDynamicVlanCreationMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HmAgentDot1xDynamicVlanCreationMode_Type.__name__=_D
_HmAgentDot1xDynamicVlanCreationMode_Object=MibScalar
hmAgentDot1xDynamicVlanCreationMode=_HmAgentDot1xDynamicVlanCreationMode_Object((1,3,6,1,4,1,248,15,36,1,2),_HmAgentDot1xDynamicVlanCreationMode_Type())
hmAgentDot1xDynamicVlanCreationMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentDot1xDynamicVlanCreationMode.setStatus(_A)
class _HmAgentDot1xSafeVlanMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HmAgentDot1xSafeVlanMode_Type.__name__=_D
_HmAgentDot1xSafeVlanMode_Object=MibScalar
hmAgentDot1xSafeVlanMode=_HmAgentDot1xSafeVlanMode_Object((1,3,6,1,4,1,248,15,36,1,3),_HmAgentDot1xSafeVlanMode_Type())
hmAgentDot1xSafeVlanMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentDot1xSafeVlanMode.setStatus(_A)
_HmAgentDot1xPortConfigGroup_ObjectIdentity=ObjectIdentity
hmAgentDot1xPortConfigGroup=_HmAgentDot1xPortConfigGroup_ObjectIdentity((1,3,6,1,4,1,248,15,36,2))
_HmAgentDot1xPortConfigTable_Object=MibTable
hmAgentDot1xPortConfigTable=_HmAgentDot1xPortConfigTable_Object((1,3,6,1,4,1,248,15,36,2,1))
if mibBuilder.loadTexts:hmAgentDot1xPortConfigTable.setStatus(_A)
_HmAgentDot1xPortConfigEntry_Object=MibTableRow
hmAgentDot1xPortConfigEntry=_HmAgentDot1xPortConfigEntry_Object((1,3,6,1,4,1,248,15,36,2,1,1))
hmAgentDot1xPortConfigEntry.setIndexNames((0,_V,_W))
if mibBuilder.loadTexts:hmAgentDot1xPortConfigEntry.setStatus(_A)
class _HmAgentDot1xPortControlMode_Type(HmAgentDot1xPortControlMode):defaultValue=2
_HmAgentDot1xPortControlMode_Type.__name__=_AU
_HmAgentDot1xPortControlMode_Object=MibTableColumn
hmAgentDot1xPortControlMode=_HmAgentDot1xPortControlMode_Object((1,3,6,1,4,1,248,15,36,2,1,1,1),_HmAgentDot1xPortControlMode_Type())
hmAgentDot1xPortControlMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentDot1xPortControlMode.setStatus(_A)
class _HmAgentDot1xGuestVlanId_Type(Unsigned32):defaultValue=0
_HmAgentDot1xGuestVlanId_Type.__name__=_H
_HmAgentDot1xGuestVlanId_Object=MibTableColumn
hmAgentDot1xGuestVlanId=_HmAgentDot1xGuestVlanId_Object((1,3,6,1,4,1,248,15,36,2,1,1,2),_HmAgentDot1xGuestVlanId_Type())
hmAgentDot1xGuestVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentDot1xGuestVlanId.setStatus(_A)
class _HmAgentDot1xGuestVlanPeriod_Type(Unsigned32):defaultValue=90;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HmAgentDot1xGuestVlanPeriod_Type.__name__=_H
_HmAgentDot1xGuestVlanPeriod_Object=MibTableColumn
hmAgentDot1xGuestVlanPeriod=_HmAgentDot1xGuestVlanPeriod_Object((1,3,6,1,4,1,248,15,36,2,1,1,3),_HmAgentDot1xGuestVlanPeriod_Type())
hmAgentDot1xGuestVlanPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentDot1xGuestVlanPeriod.setStatus(_A)
class _HmAgentDot1xUnauthenticatedVlan_Type(Unsigned32):defaultValue=0
_HmAgentDot1xUnauthenticatedVlan_Type.__name__=_H
_HmAgentDot1xUnauthenticatedVlan_Object=MibTableColumn
hmAgentDot1xUnauthenticatedVlan=_HmAgentDot1xUnauthenticatedVlan_Object((1,3,6,1,4,1,248,15,36,2,1,1,4),_HmAgentDot1xUnauthenticatedVlan_Type())
hmAgentDot1xUnauthenticatedVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentDot1xUnauthenticatedVlan.setStatus(_A)
_HmAgentDot1xMaxUsers_Type=Unsigned32
_HmAgentDot1xMaxUsers_Object=MibTableColumn
hmAgentDot1xMaxUsers=_HmAgentDot1xMaxUsers_Object((1,3,6,1,4,1,248,15,36,2,1,1,5),_HmAgentDot1xMaxUsers_Type())
hmAgentDot1xMaxUsers.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentDot1xMaxUsers.setStatus(_A)
class _HmAgentDot1xPortVlanAssigned_Type(Unsigned32):defaultValue=0
_HmAgentDot1xPortVlanAssigned_Type.__name__=_H
_HmAgentDot1xPortVlanAssigned_Object=MibTableColumn
hmAgentDot1xPortVlanAssigned=_HmAgentDot1xPortVlanAssigned_Object((1,3,6,1,4,1,248,15,36,2,1,1,6),_HmAgentDot1xPortVlanAssigned_Type())
hmAgentDot1xPortVlanAssigned.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentDot1xPortVlanAssigned.setStatus(_A)
class _HmAgentDot1xPortVlanAssignedReason_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,7)));namedValues=NamedValues(*((_X,1),('radius',2),(_AV,3),(_AW,4),(_AX,5),('notAssigned',7)))
_HmAgentDot1xPortVlanAssignedReason_Type.__name__=_D
_HmAgentDot1xPortVlanAssignedReason_Object=MibTableColumn
hmAgentDot1xPortVlanAssignedReason=_HmAgentDot1xPortVlanAssignedReason_Object((1,3,6,1,4,1,248,15,36,2,1,1,7),_HmAgentDot1xPortVlanAssignedReason_Type())
hmAgentDot1xPortVlanAssignedReason.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentDot1xPortVlanAssignedReason.setStatus(_A)
_HmAgentDot1xPortSessionTimeout_Type=Unsigned32
_HmAgentDot1xPortSessionTimeout_Object=MibTableColumn
hmAgentDot1xPortSessionTimeout=_HmAgentDot1xPortSessionTimeout_Object((1,3,6,1,4,1,248,15,36,2,1,1,8),_HmAgentDot1xPortSessionTimeout_Type())
hmAgentDot1xPortSessionTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentDot1xPortSessionTimeout.setStatus(_A)
class _HmAgentDot1xPortTerminationAction_Type(HmAgentDot1xSessionTerminationAction):defaultValue=1
_HmAgentDot1xPortTerminationAction_Type.__name__=_AY
_HmAgentDot1xPortTerminationAction_Object=MibTableColumn
hmAgentDot1xPortTerminationAction=_HmAgentDot1xPortTerminationAction_Object((1,3,6,1,4,1,248,15,36,2,1,1,9),_HmAgentDot1xPortTerminationAction_Type())
hmAgentDot1xPortTerminationAction.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentDot1xPortTerminationAction.setStatus(_A)
class _HmAgentDot1xPortMABenabled_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HmAgentDot1xPortMABenabled_Type.__name__=_D
_HmAgentDot1xPortMABenabled_Object=MibTableColumn
hmAgentDot1xPortMABenabled=_HmAgentDot1xPortMABenabled_Object((1,3,6,1,4,1,248,15,36,2,1,1,10),_HmAgentDot1xPortMABenabled_Type())
hmAgentDot1xPortMABenabled.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentDot1xPortMABenabled.setStatus(_A)
class _HmAgentDot1xPortMABenabledOperational_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HmAgentDot1xPortMABenabledOperational_Type.__name__=_D
_HmAgentDot1xPortMABenabledOperational_Object=MibTableColumn
hmAgentDot1xPortMABenabledOperational=_HmAgentDot1xPortMABenabledOperational_Object((1,3,6,1,4,1,248,15,36,2,1,1,11),_HmAgentDot1xPortMABenabledOperational_Type())
hmAgentDot1xPortMABenabledOperational.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentDot1xPortMABenabledOperational.setStatus(_A)
_HmAgentDot1xClientConfigGroup_ObjectIdentity=ObjectIdentity
hmAgentDot1xClientConfigGroup=_HmAgentDot1xClientConfigGroup_ObjectIdentity((1,3,6,1,4,1,248,15,36,3))
_HmAgentDot1xClientConfigTable_Object=MibTable
hmAgentDot1xClientConfigTable=_HmAgentDot1xClientConfigTable_Object((1,3,6,1,4,1,248,15,36,3,1))
if mibBuilder.loadTexts:hmAgentDot1xClientConfigTable.setStatus(_A)
_HmAgentDot1xClientConfigEntry_Object=MibTableRow
hmAgentDot1xClientConfigEntry=_HmAgentDot1xClientConfigEntry_Object((1,3,6,1,4,1,248,15,36,3,1,1))
hmAgentDot1xClientConfigEntry.setIndexNames((0,_G,_AZ))
if mibBuilder.loadTexts:hmAgentDot1xClientConfigEntry.setStatus(_A)
_HmAgentDot1xClientMacAddress_Type=MacAddress
_HmAgentDot1xClientMacAddress_Object=MibTableColumn
hmAgentDot1xClientMacAddress=_HmAgentDot1xClientMacAddress_Object((1,3,6,1,4,1,248,15,36,3,1,1,1),_HmAgentDot1xClientMacAddress_Type())
hmAgentDot1xClientMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentDot1xClientMacAddress.setStatus(_A)
_HmAgentDot1xLogicalPort_Type=Unsigned32
_HmAgentDot1xLogicalPort_Object=MibTableColumn
hmAgentDot1xLogicalPort=_HmAgentDot1xLogicalPort_Object((1,3,6,1,4,1,248,15,36,3,1,1,2),_HmAgentDot1xLogicalPort_Type())
hmAgentDot1xLogicalPort.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentDot1xLogicalPort.setStatus(_A)
_HmAgentDot1xInterface_Type=Unsigned32
_HmAgentDot1xInterface_Object=MibTableColumn
hmAgentDot1xInterface=_HmAgentDot1xInterface_Object((1,3,6,1,4,1,248,15,36,3,1,1,3),_HmAgentDot1xInterface_Type())
hmAgentDot1xInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentDot1xInterface.setStatus(_A)
class _HmAgentDot1xClientAuthPAEstate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_Aa,1),('disconnected',2),('connecting',3),('authenticating',4),('authenticated',5),('aborting',6),('held',7),('forceAuth',8),('forceUnauth',9)))
_HmAgentDot1xClientAuthPAEstate_Type.__name__=_D
_HmAgentDot1xClientAuthPAEstate_Object=MibTableColumn
hmAgentDot1xClientAuthPAEstate=_HmAgentDot1xClientAuthPAEstate_Object((1,3,6,1,4,1,248,15,36,3,1,1,4),_HmAgentDot1xClientAuthPAEstate_Type())
hmAgentDot1xClientAuthPAEstate.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentDot1xClientAuthPAEstate.setStatus(_A)
class _HmAgentDot1xClientBackendState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('request',1),('response',2),('success',3),('fail',4),('timeout',5),('idle',6),(_Aa,7)))
_HmAgentDot1xClientBackendState_Type.__name__=_D
_HmAgentDot1xClientBackendState_Object=MibTableColumn
hmAgentDot1xClientBackendState=_HmAgentDot1xClientBackendState_Object((1,3,6,1,4,1,248,15,36,3,1,1,5),_HmAgentDot1xClientBackendState_Type())
hmAgentDot1xClientBackendState.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentDot1xClientBackendState.setStatus(_A)
_HmAgentDot1xClientUserName_Type=DisplayString
_HmAgentDot1xClientUserName_Object=MibTableColumn
hmAgentDot1xClientUserName=_HmAgentDot1xClientUserName_Object((1,3,6,1,4,1,248,15,36,3,1,1,6),_HmAgentDot1xClientUserName_Type())
hmAgentDot1xClientUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentDot1xClientUserName.setStatus(_A)
_HmAgentDot1xClientSessionTime_Type=Unsigned32
_HmAgentDot1xClientSessionTime_Object=MibTableColumn
hmAgentDot1xClientSessionTime=_HmAgentDot1xClientSessionTime_Object((1,3,6,1,4,1,248,15,36,3,1,1,7),_HmAgentDot1xClientSessionTime_Type())
hmAgentDot1xClientSessionTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentDot1xClientSessionTime.setStatus(_A)
_HmAgentDot1xClientFilterID_Type=DisplayString
_HmAgentDot1xClientFilterID_Object=MibTableColumn
hmAgentDot1xClientFilterID=_HmAgentDot1xClientFilterID_Object((1,3,6,1,4,1,248,15,36,3,1,1,8),_HmAgentDot1xClientFilterID_Type())
hmAgentDot1xClientFilterID.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentDot1xClientFilterID.setStatus(_A)
_HmAgentDot1xClientVlanAssigned_Type=Unsigned32
_HmAgentDot1xClientVlanAssigned_Object=MibTableColumn
hmAgentDot1xClientVlanAssigned=_HmAgentDot1xClientVlanAssigned_Object((1,3,6,1,4,1,248,15,36,3,1,1,9),_HmAgentDot1xClientVlanAssigned_Type())
hmAgentDot1xClientVlanAssigned.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentDot1xClientVlanAssigned.setStatus(_A)
class _HmAgentDot1xClientVlanAssignedReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,7)));namedValues=NamedValues(*((_X,1),('radius',2),(_AV,3),(_AW,4),(_AX,5),('invalid',7)))
_HmAgentDot1xClientVlanAssignedReason_Type.__name__=_D
_HmAgentDot1xClientVlanAssignedReason_Object=MibTableColumn
hmAgentDot1xClientVlanAssignedReason=_HmAgentDot1xClientVlanAssignedReason_Object((1,3,6,1,4,1,248,15,36,3,1,1,10),_HmAgentDot1xClientVlanAssignedReason_Type())
hmAgentDot1xClientVlanAssignedReason.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentDot1xClientVlanAssignedReason.setStatus(_A)
_HmAgentDot1xClientSessionTimeout_Type=Unsigned32
_HmAgentDot1xClientSessionTimeout_Object=MibTableColumn
hmAgentDot1xClientSessionTimeout=_HmAgentDot1xClientSessionTimeout_Object((1,3,6,1,4,1,248,15,36,3,1,1,11),_HmAgentDot1xClientSessionTimeout_Type())
hmAgentDot1xClientSessionTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentDot1xClientSessionTimeout.setStatus(_A)
_HmAgentDot1xClientTerminationAction_Type=HmAgentDot1xSessionTerminationAction
_HmAgentDot1xClientTerminationAction_Object=MibTableColumn
hmAgentDot1xClientTerminationAction=_HmAgentDot1xClientTerminationAction_Object((1,3,6,1,4,1,248,15,36,3,1,1,12),_HmAgentDot1xClientTerminationAction_Type())
hmAgentDot1xClientTerminationAction.setMaxAccess(_C)
if mibBuilder.loadTexts:hmAgentDot1xClientTerminationAction.setStatus(_A)
_Dot1xTraps_ObjectIdentity=ObjectIdentity
dot1xTraps=_Dot1xTraps_ObjectIdentity((1,3,6,1,4,1,248,15,36,4))
multipleUsersTrap=NotificationType((1,3,6,1,4,1,248,15,1,50,1))
if mibBuilder.loadTexts:multipleUsersTrap.setStatus(_A)
broadcastStormStartTrap=NotificationType((1,3,6,1,4,1,248,15,1,50,2))
if mibBuilder.loadTexts:broadcastStormStartTrap.setStatus(_J)
broadcastStormEndTrap=NotificationType((1,3,6,1,4,1,248,15,1,50,3))
if mibBuilder.loadTexts:broadcastStormEndTrap.setStatus(_J)
linkFailureTrap=NotificationType((1,3,6,1,4,1,248,15,1,50,4))
if mibBuilder.loadTexts:linkFailureTrap.setStatus(_J)
vlanRequestFailureTrap=NotificationType((1,3,6,1,4,1,248,15,1,50,5))
vlanRequestFailureTrap.setObjects((_O,_Q))
if mibBuilder.loadTexts:vlanRequestFailureTrap.setStatus(_J)
vlanDeleteLastTrap=NotificationType((1,3,6,1,4,1,248,15,1,50,6))
vlanDeleteLastTrap.setObjects((_O,_Q))
if mibBuilder.loadTexts:vlanDeleteLastTrap.setStatus(_A)
vlanDefaultCfgFailureTrap=NotificationType((1,3,6,1,4,1,248,15,1,50,7))
vlanDefaultCfgFailureTrap.setObjects((_O,_Q))
if mibBuilder.loadTexts:vlanDefaultCfgFailureTrap.setStatus(_A)
vlanRestoreFailureTrap=NotificationType((1,3,6,1,4,1,248,15,1,50,8))
vlanRestoreFailureTrap.setObjects((_O,_Q))
if mibBuilder.loadTexts:vlanRestoreFailureTrap.setStatus(_J)
fanFailureTrap=NotificationType((1,3,6,1,4,1,248,15,1,50,9))
if mibBuilder.loadTexts:fanFailureTrap.setStatus(_J)
stpInstanceNewRootTrap=NotificationType((1,3,6,1,4,1,248,15,1,50,10))
stpInstanceNewRootTrap.setObjects((_G,_S))
if mibBuilder.loadTexts:stpInstanceNewRootTrap.setStatus(_A)
stpInstanceTopologyChangeTrap=NotificationType((1,3,6,1,4,1,248,15,1,50,11))
stpInstanceTopologyChangeTrap.setObjects((_G,_S))
if mibBuilder.loadTexts:stpInstanceTopologyChangeTrap.setStatus(_A)
powerSupplyStatusChangeTrap=NotificationType((1,3,6,1,4,1,248,15,1,50,12))
if mibBuilder.loadTexts:powerSupplyStatusChangeTrap.setStatus(_J)
failedUserLoginTrap=NotificationType((1,3,6,1,4,1,248,15,1,50,13))
if mibBuilder.loadTexts:failedUserLoginTrap.setStatus(_A)
dot1xPortStatusAuthorized=NotificationType((1,3,6,1,4,1,248,15,36,4,1))
dot1xPortStatusAuthorized.setObjects((_V,_W))
if mibBuilder.loadTexts:dot1xPortStatusAuthorized.setStatus(_A)
dot1xPortStatusUnauthorized=NotificationType((1,3,6,1,4,1,248,15,36,4,2))
dot1xPortStatusUnauthorized.setObjects((_V,_W))
if mibBuilder.loadTexts:dot1xPortStatusUnauthorized.setStatus(_A)
mibBuilder.exportSymbols(_G,**{_s:HmAgentPortMask,'BridgeId':BridgeId,_AU:HmAgentDot1xPortControlMode,_AY:HmAgentDot1xSessionTerminationAction,'hmPlatform4':hmPlatform4,'hmPlatform4BasicL2':hmPlatform4BasicL2,'hmAgentInfoGroup':hmAgentInfoGroup,'hmAgentTrapLogGroup':hmAgentTrapLogGroup,'hmAgentTrapLogTotal':hmAgentTrapLogTotal,'hmAgentTrapLogTotalSinceLastViewed':hmAgentTrapLogTotalSinceLastViewed,'hmAgentTrapLogTable':hmAgentTrapLogTable,'hmAgentTrapLogEntry':hmAgentTrapLogEntry,_h:hmAgentTrapLogIndex,'hmAgentTrapLogSystemTime':hmAgentTrapLogSystemTime,'hmAgentTrapLogTrap':hmAgentTrapLogTrap,'hmAgentConfigGroup':hmAgentConfigGroup,'hmAgentCLIConfigGroup':hmAgentCLIConfigGroup,'hmAgentLoginSessionTable':hmAgentLoginSessionTable,'hmAgentLoginSessionEntry':hmAgentLoginSessionEntry,_i:hmAgentLoginSessionIndex,'hmAgentLoginSessionUserName':hmAgentLoginSessionUserName,'hmAgentLoginSessionIPAddress':hmAgentLoginSessionIPAddress,'hmAgentLoginSessionConnectionType':hmAgentLoginSessionConnectionType,'hmAgentLoginSessionIdleTime':hmAgentLoginSessionIdleTime,'hmAgentLoginSessionSessionTime':hmAgentLoginSessionSessionTime,'hmAgentLoginSessionStatus':hmAgentLoginSessionStatus,'hmAgentTelnetConfigGroup':hmAgentTelnetConfigGroup,'hmAgentTelnetLoginTimeout':hmAgentTelnetLoginTimeout,'hmAgentTelnetMaxSessions':hmAgentTelnetMaxSessions,'hmAgentTelnetAllowNewMode':hmAgentTelnetAllowNewMode,'hmAgentUserConfigGroup':hmAgentUserConfigGroup,'hmAgentUserConfigCreate':hmAgentUserConfigCreate,'hmAgentUserConfigTable':hmAgentUserConfigTable,'hmAgentUserConfigEntry':hmAgentUserConfigEntry,_j:hmAgentUserIndex,'hmAgentUserName':hmAgentUserName,'hmAgentUserPassword':hmAgentUserPassword,'hmAgentUserAccessMode':hmAgentUserAccessMode,'hmAgentUserStatus':hmAgentUserStatus,'hmAgentUserAuthenticationType':hmAgentUserAuthenticationType,'hmAgentUserEncryptionType':hmAgentUserEncryptionType,'hmAgentUserEncryptionPassword':hmAgentUserEncryptionPassword,'hmAgentUserDefaultPwdActive':hmAgentUserDefaultPwdActive,'hmAgentConfigEncryptionSecret':hmAgentConfigEncryptionSecret,'hmAgentConfigEncryptionStatus':hmAgentConfigEncryptionStatus,'hmAgentLagConfigGroup':hmAgentLagConfigGroup,'hmAgentLagConfigCreate':hmAgentLagConfigCreate,'hmAgentLagSummaryConfigTable':hmAgentLagSummaryConfigTable,'hmAgentLagSummaryConfigEntry':hmAgentLagSummaryConfigEntry,_l:hmAgentLagSummaryLagIndex,'hmAgentLagSummaryName':hmAgentLagSummaryName,'hmAgentLagSummaryFlushTimer':hmAgentLagSummaryFlushTimer,'hmAgentLagSummaryLinkTrap':hmAgentLagSummaryLinkTrap,'hmAgentLagSummaryAdminMode':hmAgentLagSummaryAdminMode,'hmAgentLagSummaryStpMode':hmAgentLagSummaryStpMode,'hmAgentLagSummaryAddPort':hmAgentLagSummaryAddPort,'hmAgentLagSummaryDeletePort':hmAgentLagSummaryDeletePort,'hmAgentLagSummaryStatus':hmAgentLagSummaryStatus,'hmAgentLagSummaryType':hmAgentLagSummaryType,'hmAgentLagDetailedConfigTable':hmAgentLagDetailedConfigTable,'hmAgentLagDetailedConfigEntry':hmAgentLagDetailedConfigEntry,_n:hmAgentLagDetailedLagIndex,_o:hmAgentLagDetailedIfIndex,'hmAgentLagDetailedPortSpeed':hmAgentLagDetailedPortSpeed,'hmAgentLagDetailedPortStatus':hmAgentLagDetailedPortStatus,'hmAgentLagConfigStaticCapability':hmAgentLagConfigStaticCapability,'hmAgentSpanningTreeConfigGroup':hmAgentSpanningTreeConfigGroup,'hmAgentSpanningTreeMode':hmAgentSpanningTreeMode,'hmAgentSwitchConfigGroup':hmAgentSwitchConfigGroup,'hmAgentSwitchBroadcastControlMode':hmAgentSwitchBroadcastControlMode,'hmAgentSwitchDot3FlowControlMode':hmAgentSwitchDot3FlowControlMode,'hmAgentSwitchAddressAgingTimeoutTable':hmAgentSwitchAddressAgingTimeoutTable,'hmAgentSwitchAddressAgingTimeoutEntry':hmAgentSwitchAddressAgingTimeoutEntry,'hmAgentSwitchAddressAgingTimeout':hmAgentSwitchAddressAgingTimeout,'hmAgentSwitchStaticMacFilteringTable':hmAgentSwitchStaticMacFilteringTable,'hmAgentSwitchStaticMacFilteringEntry':hmAgentSwitchStaticMacFilteringEntry,_q:hmAgentSwitchStaticMacFilteringVlanId,_r:hmAgentSwitchStaticMacFilteringAddress,'hmAgentSwitchStaticMacFilteringSourcePortMask':hmAgentSwitchStaticMacFilteringSourcePortMask,'hmAgentSwitchStaticMacFilteringDestPortMask':hmAgentSwitchStaticMacFilteringDestPortMask,'hmAgentSwitchStaticMacFilteringStatus':hmAgentSwitchStaticMacFilteringStatus,'hmAgentSwitchIGMPSnoopingGroup':hmAgentSwitchIGMPSnoopingGroup,'hmAgentSwitchIGMPSnoopingAdminMode':hmAgentSwitchIGMPSnoopingAdminMode,'hmAgentSwitchIGMPSnoopingGroupMembershipInterval':hmAgentSwitchIGMPSnoopingGroupMembershipInterval,'hmAgentSwitchIGMPSnoopingMaxResponseTime':hmAgentSwitchIGMPSnoopingMaxResponseTime,'hmAgentSwitchIGMPSnoopingMRPExpirationTime':hmAgentSwitchIGMPSnoopingMRPExpirationTime,'hmAgentSwitchIGMPSnoopingPortMask':hmAgentSwitchIGMPSnoopingPortMask,'hmAgentSwitchIGMPSnoopingMulticastControlFramesProcessed':hmAgentSwitchIGMPSnoopingMulticastControlFramesProcessed,'hmAgentSwitchMFDBGroup':hmAgentSwitchMFDBGroup,'hmAgentSwitchMFDBTable':hmAgentSwitchMFDBTable,'hmAgentSwitchMFDBEntry':hmAgentSwitchMFDBEntry,_t:hmAgentSwitchMFDBVlanId,_u:hmAgentSwitchMFDBMacAddress,_v:hmAgentSwitchMFDBProtocolType,'hmAgentSwitchMFDBType':hmAgentSwitchMFDBType,'hmAgentSwitchMFDBDescription':hmAgentSwitchMFDBDescription,'hmAgentSwitchMFDBForwardingPortMask':hmAgentSwitchMFDBForwardingPortMask,'hmAgentSwitchMFDBFilteringPortMask':hmAgentSwitchMFDBFilteringPortMask,'hmAgentSwitchMFDBSummaryTable':hmAgentSwitchMFDBSummaryTable,'hmAgentSwitchMFDBSummaryEntry':hmAgentSwitchMFDBSummaryEntry,_w:hmAgentSwitchMFDBSummaryVlanId,_x:hmAgentSwitchMFDBSummaryMacAddress,'hmAgentSwitchMFDBSummaryForwardingPortMask':hmAgentSwitchMFDBSummaryForwardingPortMask,'hmAgentSwitchMFDBMaxTableEntries':hmAgentSwitchMFDBMaxTableEntries,'hmAgentSwitchMFDBMostEntriesUsed':hmAgentSwitchMFDBMostEntriesUsed,'hmAgentSwitchMFDBCurrentEntries':hmAgentSwitchMFDBCurrentEntries,'hmAgentSwitchDVlanTagGroup':hmAgentSwitchDVlanTagGroup,'hmAgentSwitchDVlanTagEthertype':hmAgentSwitchDVlanTagEthertype,'hmAgentSwitchVoiceVLANGroup':hmAgentSwitchVoiceVLANGroup,'hmAgentSwitchVoiceVLANAdminMode':hmAgentSwitchVoiceVLANAdminMode,'hmAgentSwitchVoiceVlanDeviceTable':hmAgentSwitchVoiceVlanDeviceTable,'hmAgentSwitchVoiceVlanDeviceEntry':hmAgentSwitchVoiceVlanDeviceEntry,_y:hmAgentSwitchVoiceVlanInterfaceNum,_z:hmAgentSwitchVoiceVlanDeviceMacAddress,'hmAgentTransferConfigGroup':hmAgentTransferConfigGroup,'hmAgentTransferUploadGroup':hmAgentTransferUploadGroup,'hmAgentTransferUploadMode':hmAgentTransferUploadMode,'hmAgentTransferUploadServerIP':hmAgentTransferUploadServerIP,'hmAgentTransferUploadPath':hmAgentTransferUploadPath,'hmAgentTransferUploadFilename':hmAgentTransferUploadFilename,'hmAgentTransferUploadDataType':hmAgentTransferUploadDataType,'hmAgentTransferUploadStart':hmAgentTransferUploadStart,'hmAgentTransferUploadStatus':hmAgentTransferUploadStatus,'hmAgentTransferDownloadGroup':hmAgentTransferDownloadGroup,'hmAgentTransferDownloadMode':hmAgentTransferDownloadMode,'hmAgentTransferDownloadServerIP':hmAgentTransferDownloadServerIP,'hmAgentTransferDownloadPath':hmAgentTransferDownloadPath,'hmAgentTransferDownloadFilename':hmAgentTransferDownloadFilename,'hmAgentTransferDownloadDataType':hmAgentTransferDownloadDataType,'hmAgentTransferDownloadStart':hmAgentTransferDownloadStart,'hmAgentTransferDownloadStatus':hmAgentTransferDownloadStatus,'hmAgentPortMirroringGroup':hmAgentPortMirroringGroup,'hmAgentMirroredPortIfIndex':hmAgentMirroredPortIfIndex,'hmAgentProbePortIfIndex':hmAgentProbePortIfIndex,'hmAgentPortMirroringMode':hmAgentPortMirroringMode,'hmAgentPortMirrorTable':hmAgentPortMirrorTable,'hmAgentPortMirrorEntry':hmAgentPortMirrorEntry,_AD:hmAgentPortMirrorSessionNum,'hmAgentPortMirrorDestinationPort':hmAgentPortMirrorDestinationPort,'hmAgentPortMirrorSourcePortMask':hmAgentPortMirrorSourcePortMask,'hmAgentPortMirrorAdminMode':hmAgentPortMirrorAdminMode,'hmAgentPortMirrorIngressMask':hmAgentPortMirrorIngressMask,'hmAgentPortMirrorEgressMask':hmAgentPortMirrorEgressMask,'hmAgentDot3adAggPortTable':hmAgentDot3adAggPortTable,'hmAgentDot3adAggPortEntry':hmAgentDot3adAggPortEntry,_AE:hmAgentDot3adAggPort,'hmAgentDot3adAggPortLACPMode':hmAgentDot3adAggPortLACPMode,'hmAgentPortConfigTable':hmAgentPortConfigTable,'hmAgentPortConfigEntry':hmAgentPortConfigEntry,_AF:hmAgentPortDot1dBasePort,'hmAgentPortIfIndex':hmAgentPortIfIndex,'hmAgentPortIanaType':hmAgentPortIanaType,'hmAgentPortSTPMode':hmAgentPortSTPMode,'hmAgentPortSTPState':hmAgentPortSTPState,'hmAgentPortAdminMode':hmAgentPortAdminMode,'hmAgentPortPhysicalMode':hmAgentPortPhysicalMode,'hmAgentPortPhysicalStatus':hmAgentPortPhysicalStatus,'hmAgentPortLinkTrapMode':hmAgentPortLinkTrapMode,'hmAgentPortClearStats':hmAgentPortClearStats,'hmAgentPortDefaultType':hmAgentPortDefaultType,'hmAgentPortType':hmAgentPortType,'hmAgentPortAutoNegAdminStatus':hmAgentPortAutoNegAdminStatus,'hmAgentPortDot3FlowControlMode':hmAgentPortDot3FlowControlMode,'hmAgentPortDVlanTagMode':hmAgentPortDVlanTagMode,'hmAgentPortDVlanTagEthertype':hmAgentPortDVlanTagEthertype,'hmAgentPortDVlanTagCustomerId':hmAgentPortDVlanTagCustomerId,'hmAgentPortMaxFrameSizeLimit':hmAgentPortMaxFrameSizeLimit,'hmAgentPortMaxFrameSize':hmAgentPortMaxFrameSize,'hmAgentPortVoiceVlanMode':hmAgentPortVoiceVlanMode,'hmAgentPortVoiceVlanID':hmAgentPortVoiceVlanID,'hmAgentPortVoiceVlanPriority':hmAgentPortVoiceVlanPriority,'hmAgentPortVoiceVlanDataPriorityMode':hmAgentPortVoiceVlanDataPriorityMode,'hmAgentPortVoiceVlanOperationalStatus':hmAgentPortVoiceVlanOperationalStatus,'hmAgentPortVoiceVlanDSCP':hmAgentPortVoiceVlanDSCP,'hmAgentPortVoiceVlanAuthMode':hmAgentPortVoiceVlanAuthMode,'hmAgentProtocolConfigGroup':hmAgentProtocolConfigGroup,'hmAgentProtocolGroupCreate':hmAgentProtocolGroupCreate,'hmAgentProtocolGroupTable':hmAgentProtocolGroupTable,'hmAgentProtocolGroupEntry':hmAgentProtocolGroupEntry,_d:hmAgentProtocolGroupId,'hmAgentProtocolGroupName':hmAgentProtocolGroupName,'hmAgentProtocolGroupVlanId':hmAgentProtocolGroupVlanId,'hmAgentProtocolGroupProtocolIP':hmAgentProtocolGroupProtocolIP,'hmAgentProtocolGroupProtocolARP':hmAgentProtocolGroupProtocolARP,'hmAgentProtocolGroupProtocolIPX':hmAgentProtocolGroupProtocolIPX,'hmAgentProtocolGroupStatus':hmAgentProtocolGroupStatus,'hmAgentProtocolGroupPortTable':hmAgentProtocolGroupPortTable,'hmAgentProtocolGroupPortEntry':hmAgentProtocolGroupPortEntry,_AK:hmAgentProtocolGroupPortIfIndex,'hmAgentProtocolGroupPortStatus':hmAgentProtocolGroupPortStatus,'hmAgentStpSwitchConfigGroup':hmAgentStpSwitchConfigGroup,'hmAgentStpConfigDigestKey':hmAgentStpConfigDigestKey,'hmAgentStpConfigFormatSelector':hmAgentStpConfigFormatSelector,'hmAgentStpConfigName':hmAgentStpConfigName,'hmAgentStpConfigRevision':hmAgentStpConfigRevision,'hmAgentStpForceVersion':hmAgentStpForceVersion,'hmAgentStpAdminMode':hmAgentStpAdminMode,'hmAgentStpPortTable':hmAgentStpPortTable,'hmAgentStpPortEntry':hmAgentStpPortEntry,'hmAgentStpPortState':hmAgentStpPortState,'hmAgentStpPortStatsMstpBpduRx':hmAgentStpPortStatsMstpBpduRx,'hmAgentStpPortStatsMstpBpduTx':hmAgentStpPortStatsMstpBpduTx,'hmAgentStpPortStatsRstpBpduRx':hmAgentStpPortStatsRstpBpduRx,'hmAgentStpPortStatsRstpBpduTx':hmAgentStpPortStatsRstpBpduTx,'hmAgentStpPortStatsStpBpduRx':hmAgentStpPortStatsStpBpduRx,'hmAgentStpPortStatsStpBpduTx':hmAgentStpPortStatsStpBpduTx,'hmAgentStpPortUpTime':hmAgentStpPortUpTime,'hmAgentStpPortMigrationCheck':hmAgentStpPortMigrationCheck,'hmAgentStpPortHelloTime':hmAgentStpPortHelloTime,'hmAgentStpCstConfigGroup':hmAgentStpCstConfigGroup,'hmAgentStpCstHelloTime':hmAgentStpCstHelloTime,'hmAgentStpCstMaxAge':hmAgentStpCstMaxAge,'hmAgentStpCstRegionalRootId':hmAgentStpCstRegionalRootId,'hmAgentStpCstRegionalRootPathCost':hmAgentStpCstRegionalRootPathCost,'hmAgentStpCstRootFwdDelay':hmAgentStpCstRootFwdDelay,'hmAgentStpCstBridgeFwdDelay':hmAgentStpCstBridgeFwdDelay,'hmAgentStpCstBridgeHelloTime':hmAgentStpCstBridgeHelloTime,'hmAgentStpCstBridgeHoldTime':hmAgentStpCstBridgeHoldTime,'hmAgentStpCstBridgeMaxAge':hmAgentStpCstBridgeMaxAge,'hmAgentStpCstBridgeDesignatedRoot':hmAgentStpCstBridgeDesignatedRoot,'hmAgentStpCstBridgePriority':hmAgentStpCstBridgePriority,'hmAgentStpCstBridgeTimeSinceTopologyChange':hmAgentStpCstBridgeTimeSinceTopologyChange,'hmAgentStpCstBridgeTopChanges':hmAgentStpCstBridgeTopChanges,'hmAgentStpCstBridgeRootCost':hmAgentStpCstBridgeRootCost,'hmAgentStpCstBridgeRootPort':hmAgentStpCstBridgeRootPort,'hmAgentStpCstBridgeMaxHops':hmAgentStpCstBridgeMaxHops,'hmAgentStpCstBridgeHoldCount':hmAgentStpCstBridgeHoldCount,'hmAgentStpCstPortTable':hmAgentStpCstPortTable,'hmAgentStpCstPortEntry':hmAgentStpCstPortEntry,'hmAgentStpCstPortOperEdge':hmAgentStpCstPortOperEdge,'hmAgentStpCstPortOperPointToPoint':hmAgentStpCstPortOperPointToPoint,'hmAgentStpCstPortTopologyChangeAck':hmAgentStpCstPortTopologyChangeAck,'hmAgentStpCstPortEdge':hmAgentStpCstPortEdge,'hmAgentStpCstPortForwardingState':hmAgentStpCstPortForwardingState,'hmAgentStpCstPortId':hmAgentStpCstPortId,'hmAgentStpCstPortPathCost':hmAgentStpCstPortPathCost,'hmAgentStpCstPortPriority':hmAgentStpCstPortPriority,'hmAgentStpCstDesignatedBridgeId':hmAgentStpCstDesignatedBridgeId,'hmAgentStpCstDesignatedCost':hmAgentStpCstDesignatedCost,'hmAgentStpCstDesignatedPortId':hmAgentStpCstDesignatedPortId,'hmAgentStpCstExtPortPathCost':hmAgentStpCstExtPortPathCost,'hmAgentStpCstPortAutoEdge':hmAgentStpCstPortAutoEdge,'hmAgentStpCstPortRole':hmAgentStpCstPortRole,'hmAgentStpCstPortDisputed':hmAgentStpCstPortDisputed,'hmAgentStpCstPortBpduGuardEffect':hmAgentStpCstPortBpduGuardEffect,'hmAgentStpCstPortBpduFilter':hmAgentStpCstPortBpduFilter,'hmAgentStpCstPortBpduFlood':hmAgentStpCstPortBpduFlood,'hmAgentStpCstPortRootGuard':hmAgentStpCstPortRootGuard,'hmAgentStpCstPortTCNGuard':hmAgentStpCstPortTCNGuard,'hmAgentStpCstPortLoopGuard':hmAgentStpCstPortLoopGuard,'hmAgentStpMstTable':hmAgentStpMstTable,'hmAgentStpMstEntry':hmAgentStpMstEntry,_S:hmAgentStpMstId,'hmAgentStpMstBridgePriority':hmAgentStpMstBridgePriority,'hmAgentStpMstBridgeIdentifier':hmAgentStpMstBridgeIdentifier,'hmAgentStpMstDesignatedRootId':hmAgentStpMstDesignatedRootId,'hmAgentStpMstRootPathCost':hmAgentStpMstRootPathCost,'hmAgentStpMstRootPortId':hmAgentStpMstRootPortId,'hmAgentStpMstTimeSinceTopologyChange':hmAgentStpMstTimeSinceTopologyChange,'hmAgentStpMstTopologyChangeCount':hmAgentStpMstTopologyChangeCount,'hmAgentStpMstTopologyChangeParm':hmAgentStpMstTopologyChangeParm,'hmAgentStpMstRowStatus':hmAgentStpMstRowStatus,'hmAgentStpMstPortTable':hmAgentStpMstPortTable,'hmAgentStpMstPortEntry':hmAgentStpMstPortEntry,'hmAgentStpMstPortForwardingState':hmAgentStpMstPortForwardingState,'hmAgentStpMstPortId':hmAgentStpMstPortId,'hmAgentStpMstPortPathCost':hmAgentStpMstPortPathCost,'hmAgentStpMstPortPriority':hmAgentStpMstPortPriority,'hmAgentStpMstDesignatedBridgeId':hmAgentStpMstDesignatedBridgeId,'hmAgentStpMstDesignatedCost':hmAgentStpMstDesignatedCost,'hmAgentStpMstDesignatedPortId':hmAgentStpMstDesignatedPortId,'hmAgentStpMstPortRole':hmAgentStpMstPortRole,'hmAgentStpMstPortDisputed':hmAgentStpMstPortDisputed,'hmAgentStpMstPortLoopInconsistentState':hmAgentStpMstPortLoopInconsistentState,'hmAgentStpMstPortTransitionsIntoLoopInconsistentState':hmAgentStpMstPortTransitionsIntoLoopInconsistentState,'hmAgentStpMstPortTransitionsOutOfLoopInconsistentState':hmAgentStpMstPortTransitionsOutOfLoopInconsistentState,'hmAgentStpMstReceivedBridgeId':hmAgentStpMstReceivedBridgeId,'hmAgentStpMstReceivedRPC':hmAgentStpMstReceivedRPC,'hmAgentStpMstReceivedPortId':hmAgentStpMstReceivedPortId,'hmAgentStpMstVlanTable':hmAgentStpMstVlanTable,'hmAgentStpMstVlanEntry':hmAgentStpMstVlanEntry,'hmAgentStpMstVlanRowStatus':hmAgentStpMstVlanRowStatus,'hmAgentStpBpduGuardMode':hmAgentStpBpduGuardMode,'hmAgentStpBpduFilterDefault':hmAgentStpBpduFilterDefault,'hmAgentClassOfServiceGroup':hmAgentClassOfServiceGroup,'hmAgentClassOfServicePortTable':hmAgentClassOfServicePortTable,'hmAgentClassOfServicePortEntry':hmAgentClassOfServicePortEntry,_AQ:hmAgentClassOfServicePortPriority,'hmAgentClassOfServicePortClass':hmAgentClassOfServicePortClass,'hmAgentSystemGroup':hmAgentSystemGroup,'hmAgentSaveConfig':hmAgentSaveConfig,'hmAgentClearConfig':hmAgentClearConfig,'hmAgentClearLags':hmAgentClearLags,'hmAgentClearLoginSessions':hmAgentClearLoginSessions,'hmAgentClearPasswords':hmAgentClearPasswords,'hmAgentClearPortStats':hmAgentClearPortStats,'hmAgentClearSwitchStats':hmAgentClearSwitchStats,'hmAgentClearTrapLog':hmAgentClearTrapLog,'hmAgentClearVlan':hmAgentClearVlan,'hmAgentResetSystem':hmAgentResetSystem,'hmAgentSaveConfigStatus':hmAgentSaveConfigStatus,'hmAgentCableTesterGroup':hmAgentCableTesterGroup,'hmAgentCableTesterStatus':hmAgentCableTesterStatus,'hmAgentCableTesterIfIndex':hmAgentCableTesterIfIndex,'hmAgentCableTesterCableStatus':hmAgentCableTesterCableStatus,'hmAgentCableTesterMinimumCableLength':hmAgentCableTesterMinimumCableLength,'hmAgentCableTesterMaximumCableLength':hmAgentCableTesterMaximumCableLength,'hmAgentCableTesterCableFailureLocation':hmAgentCableTesterCableFailureLocation,'hmPlatform4SwitchingTraps':hmPlatform4SwitchingTraps,'multipleUsersTrap':multipleUsersTrap,'broadcastStormStartTrap':broadcastStormStartTrap,'broadcastStormEndTrap':broadcastStormEndTrap,'linkFailureTrap':linkFailureTrap,'vlanRequestFailureTrap':vlanRequestFailureTrap,'vlanDeleteLastTrap':vlanDeleteLastTrap,'vlanDefaultCfgFailureTrap':vlanDefaultCfgFailureTrap,'vlanRestoreFailureTrap':vlanRestoreFailureTrap,'fanFailureTrap':fanFailureTrap,'stpInstanceNewRootTrap':stpInstanceNewRootTrap,'stpInstanceTopologyChangeTrap':stpInstanceTopologyChangeTrap,'powerSupplyStatusChangeTrap':powerSupplyStatusChangeTrap,'failedUserLoginTrap':failedUserLoginTrap,'hmRadius':hmRadius,'hmAgentRadiusConfigGroup':hmAgentRadiusConfigGroup,'hmAgentRadiusMaxTransmit':hmAgentRadiusMaxTransmit,'hmAgentRadiusTimeout':hmAgentRadiusTimeout,'hmAgentRadiusAccountingMode':hmAgentRadiusAccountingMode,'hmAgentRadiusStatsClear':hmAgentRadiusStatsClear,'hmAgentRadiusAccountingIndexNextValid':hmAgentRadiusAccountingIndexNextValid,'hmAgentRadiusAccountingConfigTable':hmAgentRadiusAccountingConfigTable,'hmAgentRadiusAccountingConfigEntry':hmAgentRadiusAccountingConfigEntry,_AR:hmAgentRadiusAccountingServerIndex,'hmAgentRadiusAccountingServerAddress':hmAgentRadiusAccountingServerAddress,'hmAgentRadiusAccountingPort':hmAgentRadiusAccountingPort,'hmAgentRadiusAccountingSecret':hmAgentRadiusAccountingSecret,'hmAgentRadiusAccountingStatus':hmAgentRadiusAccountingStatus,'hmAgentRadiusServerIndexNextValid':hmAgentRadiusServerIndexNextValid,'hmAgentRadiusServerConfigTable':hmAgentRadiusServerConfigTable,'hmAgentRadiusServerConfigEntry':hmAgentRadiusServerConfigEntry,_AS:hmAgentRadiusServerIndex,'hmAgentRadiusServerAddress':hmAgentRadiusServerAddress,'hmAgentRadiusServerPort':hmAgentRadiusServerPort,'hmAgentRadiusServerSecret':hmAgentRadiusServerSecret,'hmAgentRadiusServerPrimaryMode':hmAgentRadiusServerPrimaryMode,'hmAgentRadiusServerCurrentMode':hmAgentRadiusServerCurrentMode,'hmAgentRadiusServerMsgAuth':hmAgentRadiusServerMsgAuth,'hmAgentRadiusServerStatus':hmAgentRadiusServerStatus,'hmAgentMgmtSecurity':hmAgentMgmtSecurity,'hmAgentSSHConfigGroup':hmAgentSSHConfigGroup,'hmAgentSSHAdminMode':hmAgentSSHAdminMode,'hmAgentSSHProtocolLevel':hmAgentSSHProtocolLevel,'hmAgentSSHSessionsCount':hmAgentSSHSessionsCount,'hmAgentSSHMaxSessionsCount':hmAgentSSHMaxSessionsCount,'hmAgentSSHSessionTimeout':hmAgentSSHSessionTimeout,'hmAgentLogging':hmAgentLogging,'hmAgentLogConfigGroup':hmAgentLogConfigGroup,'hmAgentLogSysLogConfigGroup':hmAgentLogSysLogConfigGroup,'hmAgentLogSyslogAdminStatus':hmAgentLogSyslogAdminStatus,'hmAgentLogSyslogHostTable':hmAgentLogSyslogHostTable,'hmAgentLogSyslogHostEntry':hmAgentLogSyslogHostEntry,_AT:hmAgentLogHostTableIndex,'hmAgentLogHostTableIpAddress':hmAgentLogHostTableIpAddress,'hmAgentLogHostTablePort':hmAgentLogHostTablePort,'hmAgentLogHostTableSeverityFilter':hmAgentLogHostTableSeverityFilter,'hmAgentLogHostTableRowStatus':hmAgentLogHostTableRowStatus,'hmPlatform4OutboundTelnetPrivate':hmPlatform4OutboundTelnetPrivate,'hmAgentOutboundTelnetGroup':hmAgentOutboundTelnetGroup,'hmAgentOutboundTelnetAdminMode':hmAgentOutboundTelnetAdminMode,'hmAgentOutboundTelnetMaxNoOfSessions':hmAgentOutboundTelnetMaxNoOfSessions,'hmAgentOutboundTelnetTimeout':hmAgentOutboundTelnetTimeout,'hmAgentDot1xAdvanced':hmAgentDot1xAdvanced,'hmAgentDot1xEnhancementConfigGroup':hmAgentDot1xEnhancementConfigGroup,'hmAgentDot1xRadiusVlanAssignment':hmAgentDot1xRadiusVlanAssignment,'hmAgentDot1xDynamicVlanCreationMode':hmAgentDot1xDynamicVlanCreationMode,'hmAgentDot1xSafeVlanMode':hmAgentDot1xSafeVlanMode,'hmAgentDot1xPortConfigGroup':hmAgentDot1xPortConfigGroup,'hmAgentDot1xPortConfigTable':hmAgentDot1xPortConfigTable,'hmAgentDot1xPortConfigEntry':hmAgentDot1xPortConfigEntry,'hmAgentDot1xPortControlMode':hmAgentDot1xPortControlMode,'hmAgentDot1xGuestVlanId':hmAgentDot1xGuestVlanId,'hmAgentDot1xGuestVlanPeriod':hmAgentDot1xGuestVlanPeriod,'hmAgentDot1xUnauthenticatedVlan':hmAgentDot1xUnauthenticatedVlan,'hmAgentDot1xMaxUsers':hmAgentDot1xMaxUsers,'hmAgentDot1xPortVlanAssigned':hmAgentDot1xPortVlanAssigned,'hmAgentDot1xPortVlanAssignedReason':hmAgentDot1xPortVlanAssignedReason,'hmAgentDot1xPortSessionTimeout':hmAgentDot1xPortSessionTimeout,'hmAgentDot1xPortTerminationAction':hmAgentDot1xPortTerminationAction,'hmAgentDot1xPortMABenabled':hmAgentDot1xPortMABenabled,'hmAgentDot1xPortMABenabledOperational':hmAgentDot1xPortMABenabledOperational,'hmAgentDot1xClientConfigGroup':hmAgentDot1xClientConfigGroup,'hmAgentDot1xClientConfigTable':hmAgentDot1xClientConfigTable,'hmAgentDot1xClientConfigEntry':hmAgentDot1xClientConfigEntry,_AZ:hmAgentDot1xClientMacAddress,'hmAgentDot1xLogicalPort':hmAgentDot1xLogicalPort,'hmAgentDot1xInterface':hmAgentDot1xInterface,'hmAgentDot1xClientAuthPAEstate':hmAgentDot1xClientAuthPAEstate,'hmAgentDot1xClientBackendState':hmAgentDot1xClientBackendState,'hmAgentDot1xClientUserName':hmAgentDot1xClientUserName,'hmAgentDot1xClientSessionTime':hmAgentDot1xClientSessionTime,'hmAgentDot1xClientFilterID':hmAgentDot1xClientFilterID,'hmAgentDot1xClientVlanAssigned':hmAgentDot1xClientVlanAssigned,'hmAgentDot1xClientVlanAssignedReason':hmAgentDot1xClientVlanAssignedReason,'hmAgentDot1xClientSessionTimeout':hmAgentDot1xClientSessionTimeout,'hmAgentDot1xClientTerminationAction':hmAgentDot1xClientTerminationAction,'dot1xTraps':dot1xTraps,'dot1xPortStatusAuthorized':dot1xPortStatusAuthorized,'dot1xPortStatusUnauthorized':dot1xPortStatusUnauthorized})