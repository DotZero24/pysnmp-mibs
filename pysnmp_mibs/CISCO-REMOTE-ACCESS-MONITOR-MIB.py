_BS='ciscoRasActivityGroupRev1'
_BR='ciscoRasTooManySessions'
_BQ='ciscoRasTooManyFailedAuths'
_BP='ciscoRasTooHighThroughput'
_BO='crasWebvpnPeakConcurrentSessions'
_BN='crasWebvpnCumulateSessions'
_BM='crasWebvpnNumSessions'
_BL='crasSVCPeakConcurrentSessions'
_BK='crasSVCCumulateSessions'
_BJ='crasSVCNumSessions'
_BI='crasLBPeakConcurrentSessions'
_BH='crasLBCumulateSessions'
_BG='crasLBNumSessions'
_BF='crasL2LPeakConcurrentSessions'
_BE='crasL2LCumulateSessions'
_BD='crasL2LNumSessions'
_BC='crasIPSecPeakConcurrentSessions'
_BB='crasIPSecCumulateSessions'
_BA='crasIPSecNumSessions'
_B9='crasEmailPeakConcurrentSessions'
_B8='crasEmailCumulateSessions'
_B7='crasEmailNumSessions'
_B6='crasCntlTooHighThroughput'
_B5='crasCntlTooManyFailedAuths'
_B4='crasCntlTooManySessions'
_B3='crasNumDisabledAccounts'
_B2='crasGrpFailNumTerminatedOther'
_B1='crasGrpFailNumTerminatedMgmt'
_B0='crasGrpFailNumDeclined'
_A_='crasGrpFailNumResourceFailures'
_Az='crasGrpFailNumFailAuths'
_Ay='crasFailLastFailIndex'
_Ax='crasSessFailLocalAddrType'
_Aw='crasSessFailISPAddrType'
_Av='crasSessFailLocalAddr'
_Au='crasSessFailISPAddr'
_At='crasSessFailSessionIndex'
_As='crasSessFailTime'
_Ar='crasSessFailReason'
_Aq='crasSessFailType'
_Ap='crasSessFailGroupname'
_Ao='crasSessFailUsername'
_An='crasNumSetupFailInsufResources'
_Am='crasFailTableSize'
_Al='crasNumAbortedSessions'
_Ak='crasNumTotalFailures'
_Aj='crasActGrpOutOctets'
_Ai='crasActGrpInOctets'
_Ah='crasActGrpOutDropPkts'
_Ag='crasActGrpInDropPkts'
_Af='crasActGrpOutPkts'
_Ae='crasActGrpInPkts'
_Ad='crasActGrNumUsers'
_Ac='crasNumGroups'
_Ab='crasSessionState'
_Aa='crasSessionOutOctets'
_AZ='crasSessionInOctets'
_AY='crasSessionOutDropPkts'
_AX='crasSessionInDropPkts'
_AW='crasSessionOutPkts'
_AV='crasSessionInPkts'
_AU='crasDHCPServer'
_AT='crasDHCPServerAddrType'
_AS='crasSecDNSServer'
_AR='crasSecDNSServerAddrType'
_AQ='crasPrimDNSServer'
_AP='crasPrimDNSServerAddrType'
_AO='crasSecWINSServer'
_AN='crasSecWINSServerAddrType'
_AM='crasPrimWINSServer'
_AL='crasPrimWINSServerAddrType'
_AK='crasClientOSVersionString'
_AJ='crasClientOSVendorString'
_AI='crasClientVersionString'
_AH='crasClientVendorString'
_AG='crasHeartbeatInterval'
_AF='crasSessionCompressionAlgo'
_AE='crasSessionPktAuthenAlgo'
_AD='crasSessionEncryptionAlgo'
_AC='crasProtocolElement'
_AB='crasSessionProtocol'
_AA='crasISPAddress'
_A9='crasISPAddressType'
_A8='crasLocalAddress'
_A7='crasLocalAddressType'
_A6='crasSessionDuration'
_A5='crasAuthorMethod'
_A4='crasAuthenMethod'
_A3='crasGroup'
_A2='crasGlobalOutDropPkts'
_A1='crasGlobalInDropPkts'
_A0='crasGlobalOutUncompOctets'
_z='crasGlobalInDecompOctets'
_y='crasGlobalOutPkts'
_x='crasGlobalInPkts'
_w='crasNumPrevSessions'
_v='crasGlobalBwUsage'
_u='crasNumCryptoAccelerators'
_t='crasMaxGroupsSupportable'
_s='crasGrpFailGroupname'
_r='crasSessFailIndex'
_q='crasActGrpName'
_p='crasSessionIndex'
_o='crasUsername'
_n='Groups'
_m='kerberos'
_l='tacacsplus'
_k='radius'
_j='ObjectIdentifier'
_i='ciscoRasNotificationCntlGroup'
_h='ciscoRasNotificationsGroup'
_g='ciscoRasThresholdsGroup'
_f='ciscoRasSecurityGroup'
_e='ciscoRasOptionalFailureGroup'
_d='ciscoRasGrpActivityGroup'
_c='ciscoRasMandatoryFailureGroup'
_b='ciscoRasActivityGroup'
_a='ciscoRasResourceUsageGroup'
_Z='ciscoRasCapacityGroup'
_Y='crasThrMaxThroughput'
_X='crasThrMaxFailedAuths'
_W='crasThrMaxSessions'
_V='crasNumDeclinedSessions'
_U='crasGlobalOutOctets'
_T='crasGlobalInOctets'
_S='crasNumUsers'
_R='crasNumSessions'
_Q='crasMaxUsersSupportable'
_P='crasMaxSessionsSupportable'
_O='Users'
_N='TruthValue'
_M='SnmpAdminString'
_L='read-write'
_K='not-accessible'
_J='none'
_I='Unsigned32'
_H='other'
_G='Octets'
_F='Integer32'
_E='Packets'
_D='Sessions'
_C='read-only'
_B='current'
_A='CISCO-REMOTE-ACCESS-MONITOR-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString',_j)
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_M)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,zeroDotZero=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'iso','zeroDotZero')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp',_N)
ciscoRemoteAccessMonitorMIB=ModuleIdentity((1,3,6,1,4,1,9,9,392))
if mibBuilder.loadTexts:ciscoRemoteAccessMonitorMIB.setRevisions(('2020-10-04 00:00','2008-08-28 00:00'))
class RasProtocol(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_H,1),('ipsec',2),('l2tp',3),('l2tpoveripsec',4),('pptp',5),('l2f',6),('ssl',7)))
class UserAuthenMethod(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_J,1),(_H,2),(_k,3),(_l,4),(_m,5),('local',6),('ldap',7),('ntlm',8),('sdi',9)))
class UserAuthorMethod(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_J,1),(_H,2),(_k,3),(_l,4),(_m,5),('local',6),('ldap',7)))
class SessionEncrAlgo(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_J,1),('des',2),('des3',3),('rc4',4),('rc5',5),('idea',6),('cast',7),('blowfish',8),('aes',9)))
class SessionAuthAlgo(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),(_H,2),('hmacMd5',3),('hmacSha',4)))
class SessionCompressionAlgo(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_H,2),('lzs',3)))
class SessionStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('initializing',1),('established',2),('terminating',3)))
class SessionIndex(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
class FailureRecordIndex(TextualConvention,Unsigned32):status=_B;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CiscoRasMonitorMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoRasMonitorMIBNotifs=_CiscoRasMonitorMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,392,0))
_CiscoRasMonitorMIBObjects_ObjectIdentity=ObjectIdentity
ciscoRasMonitorMIBObjects=_CiscoRasMonitorMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,392,1))
_CrasCapacity_ObjectIdentity=ObjectIdentity
crasCapacity=_CrasCapacity_ObjectIdentity((1,3,6,1,4,1,9,9,392,1,1))
class _CrasMaxSessionsSupportable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CrasMaxSessionsSupportable_Type.__name__=_F
_CrasMaxSessionsSupportable_Object=MibScalar
crasMaxSessionsSupportable=_CrasMaxSessionsSupportable_Object((1,3,6,1,4,1,9,9,392,1,1,1),_CrasMaxSessionsSupportable_Type())
crasMaxSessionsSupportable.setMaxAccess(_C)
if mibBuilder.loadTexts:crasMaxSessionsSupportable.setStatus(_B)
if mibBuilder.loadTexts:crasMaxSessionsSupportable.setUnits(_D)
class _CrasMaxUsersSupportable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CrasMaxUsersSupportable_Type.__name__=_F
_CrasMaxUsersSupportable_Object=MibScalar
crasMaxUsersSupportable=_CrasMaxUsersSupportable_Object((1,3,6,1,4,1,9,9,392,1,1,2),_CrasMaxUsersSupportable_Type())
crasMaxUsersSupportable.setMaxAccess(_C)
if mibBuilder.loadTexts:crasMaxUsersSupportable.setStatus(_B)
if mibBuilder.loadTexts:crasMaxUsersSupportable.setUnits(_O)
class _CrasMaxGroupsSupportable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CrasMaxGroupsSupportable_Type.__name__=_F
_CrasMaxGroupsSupportable_Object=MibScalar
crasMaxGroupsSupportable=_CrasMaxGroupsSupportable_Object((1,3,6,1,4,1,9,9,392,1,1,3),_CrasMaxGroupsSupportable_Type())
crasMaxGroupsSupportable.setMaxAccess(_C)
if mibBuilder.loadTexts:crasMaxGroupsSupportable.setStatus(_B)
if mibBuilder.loadTexts:crasMaxGroupsSupportable.setUnits(_n)
class _CrasNumCryptoAccelerators_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CrasNumCryptoAccelerators_Type.__name__=_F
_CrasNumCryptoAccelerators_Object=MibScalar
crasNumCryptoAccelerators=_CrasNumCryptoAccelerators_Object((1,3,6,1,4,1,9,9,392,1,1,4),_CrasNumCryptoAccelerators_Type())
crasNumCryptoAccelerators.setMaxAccess(_C)
if mibBuilder.loadTexts:crasNumCryptoAccelerators.setStatus(_B)
if mibBuilder.loadTexts:crasNumCryptoAccelerators.setUnits(_O)
_CrasResourceUsage_ObjectIdentity=ObjectIdentity
crasResourceUsage=_CrasResourceUsage_ObjectIdentity((1,3,6,1,4,1,9,9,392,1,2))
_CrasGlobalBwUsage_Type=Gauge32
_CrasGlobalBwUsage_Object=MibScalar
crasGlobalBwUsage=_CrasGlobalBwUsage_Object((1,3,6,1,4,1,9,9,392,1,2,1),_CrasGlobalBwUsage_Type())
crasGlobalBwUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:crasGlobalBwUsage.setStatus(_B)
if mibBuilder.loadTexts:crasGlobalBwUsage.setUnits('MBytes/second')
_CrasActivity_ObjectIdentity=ObjectIdentity
crasActivity=_CrasActivity_ObjectIdentity((1,3,6,1,4,1,9,9,392,1,3))
_CrasNumSessions_Type=Gauge32
_CrasNumSessions_Object=MibScalar
crasNumSessions=_CrasNumSessions_Object((1,3,6,1,4,1,9,9,392,1,3,1),_CrasNumSessions_Type())
crasNumSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:crasNumSessions.setStatus(_B)
if mibBuilder.loadTexts:crasNumSessions.setUnits(_D)
_CrasNumPrevSessions_Type=Counter32
_CrasNumPrevSessions_Object=MibScalar
crasNumPrevSessions=_CrasNumPrevSessions_Object((1,3,6,1,4,1,9,9,392,1,3,2),_CrasNumPrevSessions_Type())
crasNumPrevSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:crasNumPrevSessions.setStatus(_B)
if mibBuilder.loadTexts:crasNumPrevSessions.setUnits(_D)
_CrasNumUsers_Type=Gauge32
_CrasNumUsers_Object=MibScalar
crasNumUsers=_CrasNumUsers_Object((1,3,6,1,4,1,9,9,392,1,3,3),_CrasNumUsers_Type())
crasNumUsers.setMaxAccess(_C)
if mibBuilder.loadTexts:crasNumUsers.setStatus(_B)
if mibBuilder.loadTexts:crasNumUsers.setUnits(_O)
_CrasNumGroups_Type=Gauge32
_CrasNumGroups_Object=MibScalar
crasNumGroups=_CrasNumGroups_Object((1,3,6,1,4,1,9,9,392,1,3,4),_CrasNumGroups_Type())
crasNumGroups.setMaxAccess(_C)
if mibBuilder.loadTexts:crasNumGroups.setStatus(_B)
if mibBuilder.loadTexts:crasNumGroups.setUnits(_n)
_CrasGlobalInPkts_Type=Counter64
_CrasGlobalInPkts_Object=MibScalar
crasGlobalInPkts=_CrasGlobalInPkts_Object((1,3,6,1,4,1,9,9,392,1,3,5),_CrasGlobalInPkts_Type())
crasGlobalInPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:crasGlobalInPkts.setStatus(_B)
if mibBuilder.loadTexts:crasGlobalInPkts.setUnits(_E)
_CrasGlobalOutPkts_Type=Counter64
_CrasGlobalOutPkts_Object=MibScalar
crasGlobalOutPkts=_CrasGlobalOutPkts_Object((1,3,6,1,4,1,9,9,392,1,3,6),_CrasGlobalOutPkts_Type())
crasGlobalOutPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:crasGlobalOutPkts.setStatus(_B)
if mibBuilder.loadTexts:crasGlobalOutPkts.setUnits(_E)
_CrasGlobalInOctets_Type=Counter64
_CrasGlobalInOctets_Object=MibScalar
crasGlobalInOctets=_CrasGlobalInOctets_Object((1,3,6,1,4,1,9,9,392,1,3,7),_CrasGlobalInOctets_Type())
crasGlobalInOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:crasGlobalInOctets.setStatus(_B)
if mibBuilder.loadTexts:crasGlobalInOctets.setUnits(_G)
_CrasGlobalInDecompOctets_Type=Counter64
_CrasGlobalInDecompOctets_Object=MibScalar
crasGlobalInDecompOctets=_CrasGlobalInDecompOctets_Object((1,3,6,1,4,1,9,9,392,1,3,8),_CrasGlobalInDecompOctets_Type())
crasGlobalInDecompOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:crasGlobalInDecompOctets.setStatus(_B)
if mibBuilder.loadTexts:crasGlobalInDecompOctets.setUnits(_G)
_CrasGlobalOutOctets_Type=Counter64
_CrasGlobalOutOctets_Object=MibScalar
crasGlobalOutOctets=_CrasGlobalOutOctets_Object((1,3,6,1,4,1,9,9,392,1,3,9),_CrasGlobalOutOctets_Type())
crasGlobalOutOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:crasGlobalOutOctets.setStatus(_B)
if mibBuilder.loadTexts:crasGlobalOutOctets.setUnits(_G)
_CrasGlobalOutUncompOctets_Type=Counter64
_CrasGlobalOutUncompOctets_Object=MibScalar
crasGlobalOutUncompOctets=_CrasGlobalOutUncompOctets_Object((1,3,6,1,4,1,9,9,392,1,3,10),_CrasGlobalOutUncompOctets_Type())
crasGlobalOutUncompOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:crasGlobalOutUncompOctets.setStatus(_B)
if mibBuilder.loadTexts:crasGlobalOutUncompOctets.setUnits(_G)
_CrasGlobalInDropPkts_Type=Counter64
_CrasGlobalInDropPkts_Object=MibScalar
crasGlobalInDropPkts=_CrasGlobalInDropPkts_Object((1,3,6,1,4,1,9,9,392,1,3,11),_CrasGlobalInDropPkts_Type())
crasGlobalInDropPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:crasGlobalInDropPkts.setStatus(_B)
if mibBuilder.loadTexts:crasGlobalInDropPkts.setUnits(_E)
_CrasGlobalOutDropPkts_Type=Counter64
_CrasGlobalOutDropPkts_Object=MibScalar
crasGlobalOutDropPkts=_CrasGlobalOutDropPkts_Object((1,3,6,1,4,1,9,9,392,1,3,12),_CrasGlobalOutDropPkts_Type())
crasGlobalOutDropPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:crasGlobalOutDropPkts.setStatus(_B)
if mibBuilder.loadTexts:crasGlobalOutDropPkts.setUnits(_E)
_CrasSessionTable_Object=MibTable
crasSessionTable=_CrasSessionTable_Object((1,3,6,1,4,1,9,9,392,1,3,21))
if mibBuilder.loadTexts:crasSessionTable.setStatus(_B)
_CrasSessionEntry_Object=MibTableRow
crasSessionEntry=_CrasSessionEntry_Object((1,3,6,1,4,1,9,9,392,1,3,21,1))
crasSessionEntry.setIndexNames((0,_A,_o),(0,_A,_p))
if mibBuilder.loadTexts:crasSessionEntry.setStatus(_B)
class _CrasUsername_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_CrasUsername_Type.__name__=_M
_CrasUsername_Object=MibTableColumn
crasUsername=_CrasUsername_Object((1,3,6,1,4,1,9,9,392,1,3,21,1,1),_CrasUsername_Type())
crasUsername.setMaxAccess(_K)
if mibBuilder.loadTexts:crasUsername.setStatus(_B)
_CrasGroup_Type=SnmpAdminString
_CrasGroup_Object=MibTableColumn
crasGroup=_CrasGroup_Object((1,3,6,1,4,1,9,9,392,1,3,21,1,2),_CrasGroup_Type())
crasGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:crasGroup.setStatus(_B)
_CrasSessionIndex_Type=SessionIndex
_CrasSessionIndex_Object=MibTableColumn
crasSessionIndex=_CrasSessionIndex_Object((1,3,6,1,4,1,9,9,392,1,3,21,1,3),_CrasSessionIndex_Type())
crasSessionIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:crasSessionIndex.setStatus(_B)
_CrasAuthenMethod_Type=UserAuthenMethod
_CrasAuthenMethod_Object=MibTableColumn
crasAuthenMethod=_CrasAuthenMethod_Object((1,3,6,1,4,1,9,9,392,1,3,21,1,4),_CrasAuthenMethod_Type())
crasAuthenMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:crasAuthenMethod.setStatus(_B)
_CrasAuthorMethod_Type=UserAuthorMethod
_CrasAuthorMethod_Object=MibTableColumn
crasAuthorMethod=_CrasAuthorMethod_Object((1,3,6,1,4,1,9,9,392,1,3,21,1,5),_CrasAuthorMethod_Type())
crasAuthorMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:crasAuthorMethod.setStatus(_B)
_CrasSessionDuration_Type=Counter32
_CrasSessionDuration_Object=MibTableColumn
crasSessionDuration=_CrasSessionDuration_Object((1,3,6,1,4,1,9,9,392,1,3,21,1,6),_CrasSessionDuration_Type())
crasSessionDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:crasSessionDuration.setStatus(_B)
_CrasLocalAddressType_Type=InetAddressType
_CrasLocalAddressType_Object=MibTableColumn
crasLocalAddressType=_CrasLocalAddressType_Object((1,3,6,1,4,1,9,9,392,1,3,21,1,7),_CrasLocalAddressType_Type())
crasLocalAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:crasLocalAddressType.setStatus(_B)
_CrasLocalAddress_Type=InetAddress
_CrasLocalAddress_Object=MibTableColumn
crasLocalAddress=_CrasLocalAddress_Object((1,3,6,1,4,1,9,9,392,1,3,21,1,8),_CrasLocalAddress_Type())
crasLocalAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:crasLocalAddress.setStatus(_B)
_CrasISPAddressType_Type=InetAddressType
_CrasISPAddressType_Object=MibTableColumn
crasISPAddressType=_CrasISPAddressType_Object((1,3,6,1,4,1,9,9,392,1,3,21,1,9),_CrasISPAddressType_Type())
crasISPAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:crasISPAddressType.setStatus(_B)
_CrasISPAddress_Type=InetAddress
_CrasISPAddress_Object=MibTableColumn
crasISPAddress=_CrasISPAddress_Object((1,3,6,1,4,1,9,9,392,1,3,21,1,10),_CrasISPAddress_Type())
crasISPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:crasISPAddress.setStatus(_B)
_CrasSessionProtocol_Type=RasProtocol
_CrasSessionProtocol_Object=MibTableColumn
crasSessionProtocol=_CrasSessionProtocol_Object((1,3,6,1,4,1,9,9,392,1,3,21,1,11),_CrasSessionProtocol_Type())
crasSessionProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:crasSessionProtocol.setStatus(_B)
class _CrasProtocolElement_Type(ObjectIdentifier):defaultValue=0,0
_CrasProtocolElement_Type.__name__=_j
_CrasProtocolElement_Object=MibTableColumn
crasProtocolElement=_CrasProtocolElement_Object((1,3,6,1,4,1,9,9,392,1,3,21,1,12),_CrasProtocolElement_Type())
crasProtocolElement.setMaxAccess(_C)
if mibBuilder.loadTexts:crasProtocolElement.setStatus(_B)
_CrasSessionEncryptionAlgo_Type=SessionEncrAlgo
_CrasSessionEncryptionAlgo_Object=MibTableColumn
crasSessionEncryptionAlgo=_CrasSessionEncryptionAlgo_Object((1,3,6,1,4,1,9,9,392,1,3,21,1,13),_CrasSessionEncryptionAlgo_Type())
crasSessionEncryptionAlgo.setMaxAccess(_C)
if mibBuilder.loadTexts:crasSessionEncryptionAlgo.setStatus(_B)
_CrasSessionPktAuthenAlgo_Type=SessionAuthAlgo
_CrasSessionPktAuthenAlgo_Object=MibTableColumn
crasSessionPktAuthenAlgo=_CrasSessionPktAuthenAlgo_Object((1,3,6,1,4,1,9,9,392,1,3,21,1,14),_CrasSessionPktAuthenAlgo_Type())
crasSessionPktAuthenAlgo.setMaxAccess(_C)
if mibBuilder.loadTexts:crasSessionPktAuthenAlgo.setStatus(_B)
_CrasSessionCompressionAlgo_Type=SessionCompressionAlgo
_CrasSessionCompressionAlgo_Object=MibTableColumn
crasSessionCompressionAlgo=_CrasSessionCompressionAlgo_Object((1,3,6,1,4,1,9,9,392,1,3,21,1,15),_CrasSessionCompressionAlgo_Type())
crasSessionCompressionAlgo.setMaxAccess(_C)
if mibBuilder.loadTexts:crasSessionCompressionAlgo.setStatus(_B)
class _CrasHeartbeatInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CrasHeartbeatInterval_Type.__name__=_I
_CrasHeartbeatInterval_Object=MibTableColumn
crasHeartbeatInterval=_CrasHeartbeatInterval_Object((1,3,6,1,4,1,9,9,392,1,3,21,1,16),_CrasHeartbeatInterval_Type())
crasHeartbeatInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:crasHeartbeatInterval.setStatus(_B)
if mibBuilder.loadTexts:crasHeartbeatInterval.setUnits('Seconds')
_CrasClientVendorString_Type=SnmpAdminString
_CrasClientVendorString_Object=MibTableColumn
crasClientVendorString=_CrasClientVendorString_Object((1,3,6,1,4,1,9,9,392,1,3,21,1,17),_CrasClientVendorString_Type())
crasClientVendorString.setMaxAccess(_C)
if mibBuilder.loadTexts:crasClientVendorString.setStatus(_B)
_CrasClientVersionString_Type=SnmpAdminString
_CrasClientVersionString_Object=MibTableColumn
crasClientVersionString=_CrasClientVersionString_Object((1,3,6,1,4,1,9,9,392,1,3,21,1,18),_CrasClientVersionString_Type())
crasClientVersionString.setMaxAccess(_C)
if mibBuilder.loadTexts:crasClientVersionString.setStatus(_B)
_CrasClientOSVendorString_Type=SnmpAdminString
_CrasClientOSVendorString_Object=MibTableColumn
crasClientOSVendorString=_CrasClientOSVendorString_Object((1,3,6,1,4,1,9,9,392,1,3,21,1,19),_CrasClientOSVendorString_Type())
crasClientOSVendorString.setMaxAccess(_C)
if mibBuilder.loadTexts:crasClientOSVendorString.setStatus(_B)
_CrasClientOSVersionString_Type=SnmpAdminString
_CrasClientOSVersionString_Object=MibTableColumn
crasClientOSVersionString=_CrasClientOSVersionString_Object((1,3,6,1,4,1,9,9,392,1,3,21,1,20),_CrasClientOSVersionString_Type())
crasClientOSVersionString.setMaxAccess(_C)
if mibBuilder.loadTexts:crasClientOSVersionString.setStatus(_B)
_CrasPrimWINSServerAddrType_Type=InetAddressType
_CrasPrimWINSServerAddrType_Object=MibTableColumn
crasPrimWINSServerAddrType=_CrasPrimWINSServerAddrType_Object((1,3,6,1,4,1,9,9,392,1,3,21,1,21),_CrasPrimWINSServerAddrType_Type())
crasPrimWINSServerAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:crasPrimWINSServerAddrType.setStatus(_B)
_CrasPrimWINSServer_Type=InetAddress
_CrasPrimWINSServer_Object=MibTableColumn
crasPrimWINSServer=_CrasPrimWINSServer_Object((1,3,6,1,4,1,9,9,392,1,3,21,1,22),_CrasPrimWINSServer_Type())
crasPrimWINSServer.setMaxAccess(_C)
if mibBuilder.loadTexts:crasPrimWINSServer.setStatus(_B)
_CrasSecWINSServerAddrType_Type=InetAddressType
_CrasSecWINSServerAddrType_Object=MibTableColumn
crasSecWINSServerAddrType=_CrasSecWINSServerAddrType_Object((1,3,6,1,4,1,9,9,392,1,3,21,1,23),_CrasSecWINSServerAddrType_Type())
crasSecWINSServerAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:crasSecWINSServerAddrType.setStatus(_B)
_CrasSecWINSServer_Type=InetAddress
_CrasSecWINSServer_Object=MibTableColumn
crasSecWINSServer=_CrasSecWINSServer_Object((1,3,6,1,4,1,9,9,392,1,3,21,1,24),_CrasSecWINSServer_Type())
crasSecWINSServer.setMaxAccess(_C)
if mibBuilder.loadTexts:crasSecWINSServer.setStatus(_B)
_CrasPrimDNSServerAddrType_Type=InetAddressType
_CrasPrimDNSServerAddrType_Object=MibTableColumn
crasPrimDNSServerAddrType=_CrasPrimDNSServerAddrType_Object((1,3,6,1,4,1,9,9,392,1,3,21,1,25),_CrasPrimDNSServerAddrType_Type())
crasPrimDNSServerAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:crasPrimDNSServerAddrType.setStatus(_B)
_CrasPrimDNSServer_Type=InetAddress
_CrasPrimDNSServer_Object=MibTableColumn
crasPrimDNSServer=_CrasPrimDNSServer_Object((1,3,6,1,4,1,9,9,392,1,3,21,1,26),_CrasPrimDNSServer_Type())
crasPrimDNSServer.setMaxAccess(_C)
if mibBuilder.loadTexts:crasPrimDNSServer.setStatus(_B)
_CrasSecDNSServerAddrType_Type=InetAddressType
_CrasSecDNSServerAddrType_Object=MibTableColumn
crasSecDNSServerAddrType=_CrasSecDNSServerAddrType_Object((1,3,6,1,4,1,9,9,392,1,3,21,1,27),_CrasSecDNSServerAddrType_Type())
crasSecDNSServerAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:crasSecDNSServerAddrType.setStatus(_B)
_CrasSecDNSServer_Type=InetAddress
_CrasSecDNSServer_Object=MibTableColumn
crasSecDNSServer=_CrasSecDNSServer_Object((1,3,6,1,4,1,9,9,392,1,3,21,1,28),_CrasSecDNSServer_Type())
crasSecDNSServer.setMaxAccess(_C)
if mibBuilder.loadTexts:crasSecDNSServer.setStatus(_B)
_CrasDHCPServerAddrType_Type=InetAddressType
_CrasDHCPServerAddrType_Object=MibTableColumn
crasDHCPServerAddrType=_CrasDHCPServerAddrType_Object((1,3,6,1,4,1,9,9,392,1,3,21,1,29),_CrasDHCPServerAddrType_Type())
crasDHCPServerAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:crasDHCPServerAddrType.setStatus(_B)
_CrasDHCPServer_Type=InetAddress
_CrasDHCPServer_Object=MibTableColumn
crasDHCPServer=_CrasDHCPServer_Object((1,3,6,1,4,1,9,9,392,1,3,21,1,30),_CrasDHCPServer_Type())
crasDHCPServer.setMaxAccess(_C)
if mibBuilder.loadTexts:crasDHCPServer.setStatus(_B)
_CrasSessionInPkts_Type=Counter64
_CrasSessionInPkts_Object=MibTableColumn
crasSessionInPkts=_CrasSessionInPkts_Object((1,3,6,1,4,1,9,9,392,1,3,21,1,31),_CrasSessionInPkts_Type())
crasSessionInPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:crasSessionInPkts.setStatus(_B)
if mibBuilder.loadTexts:crasSessionInPkts.setUnits(_E)
_CrasSessionOutPkts_Type=Counter64
_CrasSessionOutPkts_Object=MibTableColumn
crasSessionOutPkts=_CrasSessionOutPkts_Object((1,3,6,1,4,1,9,9,392,1,3,21,1,32),_CrasSessionOutPkts_Type())
crasSessionOutPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:crasSessionOutPkts.setStatus(_B)
if mibBuilder.loadTexts:crasSessionOutPkts.setUnits(_E)
_CrasSessionInDropPkts_Type=Counter64
_CrasSessionInDropPkts_Object=MibTableColumn
crasSessionInDropPkts=_CrasSessionInDropPkts_Object((1,3,6,1,4,1,9,9,392,1,3,21,1,33),_CrasSessionInDropPkts_Type())
crasSessionInDropPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:crasSessionInDropPkts.setStatus(_B)
if mibBuilder.loadTexts:crasSessionInDropPkts.setUnits(_E)
_CrasSessionOutDropPkts_Type=Counter64
_CrasSessionOutDropPkts_Object=MibTableColumn
crasSessionOutDropPkts=_CrasSessionOutDropPkts_Object((1,3,6,1,4,1,9,9,392,1,3,21,1,34),_CrasSessionOutDropPkts_Type())
crasSessionOutDropPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:crasSessionOutDropPkts.setStatus(_B)
if mibBuilder.loadTexts:crasSessionOutDropPkts.setUnits(_E)
_CrasSessionInOctets_Type=Counter64
_CrasSessionInOctets_Object=MibTableColumn
crasSessionInOctets=_CrasSessionInOctets_Object((1,3,6,1,4,1,9,9,392,1,3,21,1,35),_CrasSessionInOctets_Type())
crasSessionInOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:crasSessionInOctets.setStatus(_B)
if mibBuilder.loadTexts:crasSessionInOctets.setUnits(_G)
_CrasSessionOutOctets_Type=Counter64
_CrasSessionOutOctets_Object=MibTableColumn
crasSessionOutOctets=_CrasSessionOutOctets_Object((1,3,6,1,4,1,9,9,392,1,3,21,1,36),_CrasSessionOutOctets_Type())
crasSessionOutOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:crasSessionOutOctets.setStatus(_B)
if mibBuilder.loadTexts:crasSessionOutOctets.setUnits(_G)
_CrasSessionState_Type=SessionStatus
_CrasSessionState_Object=MibTableColumn
crasSessionState=_CrasSessionState_Object((1,3,6,1,4,1,9,9,392,1,3,21,1,37),_CrasSessionState_Type())
crasSessionState.setMaxAccess(_L)
if mibBuilder.loadTexts:crasSessionState.setStatus(_B)
_CrasActGroupTable_Object=MibTable
crasActGroupTable=_CrasActGroupTable_Object((1,3,6,1,4,1,9,9,392,1,3,22))
if mibBuilder.loadTexts:crasActGroupTable.setStatus(_B)
_CrasActGroupEntry_Object=MibTableRow
crasActGroupEntry=_CrasActGroupEntry_Object((1,3,6,1,4,1,9,9,392,1,3,22,1))
crasActGroupEntry.setIndexNames((0,_A,_q))
if mibBuilder.loadTexts:crasActGroupEntry.setStatus(_B)
class _CrasActGrpName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CrasActGrpName_Type.__name__=_M
_CrasActGrpName_Object=MibTableColumn
crasActGrpName=_CrasActGrpName_Object((1,3,6,1,4,1,9,9,392,1,3,22,1,1),_CrasActGrpName_Type())
crasActGrpName.setMaxAccess(_K)
if mibBuilder.loadTexts:crasActGrpName.setStatus(_B)
class _CrasActGrNumUsers_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CrasActGrNumUsers_Type.__name__=_F
_CrasActGrNumUsers_Object=MibTableColumn
crasActGrNumUsers=_CrasActGrNumUsers_Object((1,3,6,1,4,1,9,9,392,1,3,22,1,2),_CrasActGrNumUsers_Type())
crasActGrNumUsers.setMaxAccess(_C)
if mibBuilder.loadTexts:crasActGrNumUsers.setStatus(_B)
_CrasActGrpInPkts_Type=Counter64
_CrasActGrpInPkts_Object=MibTableColumn
crasActGrpInPkts=_CrasActGrpInPkts_Object((1,3,6,1,4,1,9,9,392,1,3,22,1,3),_CrasActGrpInPkts_Type())
crasActGrpInPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:crasActGrpInPkts.setStatus(_B)
if mibBuilder.loadTexts:crasActGrpInPkts.setUnits(_E)
_CrasActGrpOutPkts_Type=Counter64
_CrasActGrpOutPkts_Object=MibTableColumn
crasActGrpOutPkts=_CrasActGrpOutPkts_Object((1,3,6,1,4,1,9,9,392,1,3,22,1,4),_CrasActGrpOutPkts_Type())
crasActGrpOutPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:crasActGrpOutPkts.setStatus(_B)
if mibBuilder.loadTexts:crasActGrpOutPkts.setUnits(_E)
_CrasActGrpInDropPkts_Type=Counter64
_CrasActGrpInDropPkts_Object=MibTableColumn
crasActGrpInDropPkts=_CrasActGrpInDropPkts_Object((1,3,6,1,4,1,9,9,392,1,3,22,1,5),_CrasActGrpInDropPkts_Type())
crasActGrpInDropPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:crasActGrpInDropPkts.setStatus(_B)
if mibBuilder.loadTexts:crasActGrpInDropPkts.setUnits(_E)
_CrasActGrpOutDropPkts_Type=Counter64
_CrasActGrpOutDropPkts_Object=MibTableColumn
crasActGrpOutDropPkts=_CrasActGrpOutDropPkts_Object((1,3,6,1,4,1,9,9,392,1,3,22,1,6),_CrasActGrpOutDropPkts_Type())
crasActGrpOutDropPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:crasActGrpOutDropPkts.setStatus(_B)
if mibBuilder.loadTexts:crasActGrpOutDropPkts.setUnits(_E)
_CrasActGrpInOctets_Type=Counter64
_CrasActGrpInOctets_Object=MibTableColumn
crasActGrpInOctets=_CrasActGrpInOctets_Object((1,3,6,1,4,1,9,9,392,1,3,22,1,7),_CrasActGrpInOctets_Type())
crasActGrpInOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:crasActGrpInOctets.setStatus(_B)
if mibBuilder.loadTexts:crasActGrpInOctets.setUnits(_G)
_CrasActGrpOutOctets_Type=Counter64
_CrasActGrpOutOctets_Object=MibTableColumn
crasActGrpOutOctets=_CrasActGrpOutOctets_Object((1,3,6,1,4,1,9,9,392,1,3,22,1,8),_CrasActGrpOutOctets_Type())
crasActGrpOutOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:crasActGrpOutOctets.setStatus(_B)
if mibBuilder.loadTexts:crasActGrpOutOctets.setUnits(_G)
_CrasEmailNumSessions_Type=Gauge32
_CrasEmailNumSessions_Object=MibScalar
crasEmailNumSessions=_CrasEmailNumSessions_Object((1,3,6,1,4,1,9,9,392,1,3,23),_CrasEmailNumSessions_Type())
crasEmailNumSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:crasEmailNumSessions.setStatus(_B)
if mibBuilder.loadTexts:crasEmailNumSessions.setUnits(_D)
_CrasEmailCumulateSessions_Type=Counter32
_CrasEmailCumulateSessions_Object=MibScalar
crasEmailCumulateSessions=_CrasEmailCumulateSessions_Object((1,3,6,1,4,1,9,9,392,1,3,24),_CrasEmailCumulateSessions_Type())
crasEmailCumulateSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:crasEmailCumulateSessions.setStatus(_B)
if mibBuilder.loadTexts:crasEmailCumulateSessions.setUnits(_D)
_CrasEmailPeakConcurrentSessions_Type=Unsigned32
_CrasEmailPeakConcurrentSessions_Object=MibScalar
crasEmailPeakConcurrentSessions=_CrasEmailPeakConcurrentSessions_Object((1,3,6,1,4,1,9,9,392,1,3,25),_CrasEmailPeakConcurrentSessions_Type())
crasEmailPeakConcurrentSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:crasEmailPeakConcurrentSessions.setStatus(_B)
if mibBuilder.loadTexts:crasEmailPeakConcurrentSessions.setUnits(_D)
_CrasIPSecNumSessions_Type=Gauge32
_CrasIPSecNumSessions_Object=MibScalar
crasIPSecNumSessions=_CrasIPSecNumSessions_Object((1,3,6,1,4,1,9,9,392,1,3,26),_CrasIPSecNumSessions_Type())
crasIPSecNumSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:crasIPSecNumSessions.setStatus(_B)
if mibBuilder.loadTexts:crasIPSecNumSessions.setUnits(_D)
_CrasIPSecCumulateSessions_Type=Counter32
_CrasIPSecCumulateSessions_Object=MibScalar
crasIPSecCumulateSessions=_CrasIPSecCumulateSessions_Object((1,3,6,1,4,1,9,9,392,1,3,27),_CrasIPSecCumulateSessions_Type())
crasIPSecCumulateSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:crasIPSecCumulateSessions.setStatus(_B)
if mibBuilder.loadTexts:crasIPSecCumulateSessions.setUnits(_D)
_CrasIPSecPeakConcurrentSessions_Type=Unsigned32
_CrasIPSecPeakConcurrentSessions_Object=MibScalar
crasIPSecPeakConcurrentSessions=_CrasIPSecPeakConcurrentSessions_Object((1,3,6,1,4,1,9,9,392,1,3,28),_CrasIPSecPeakConcurrentSessions_Type())
crasIPSecPeakConcurrentSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:crasIPSecPeakConcurrentSessions.setStatus(_B)
if mibBuilder.loadTexts:crasIPSecPeakConcurrentSessions.setUnits(_D)
_CrasL2LNumSessions_Type=Gauge32
_CrasL2LNumSessions_Object=MibScalar
crasL2LNumSessions=_CrasL2LNumSessions_Object((1,3,6,1,4,1,9,9,392,1,3,29),_CrasL2LNumSessions_Type())
crasL2LNumSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:crasL2LNumSessions.setStatus(_B)
if mibBuilder.loadTexts:crasL2LNumSessions.setUnits(_D)
_CrasL2LCumulateSessions_Type=Counter32
_CrasL2LCumulateSessions_Object=MibScalar
crasL2LCumulateSessions=_CrasL2LCumulateSessions_Object((1,3,6,1,4,1,9,9,392,1,3,30),_CrasL2LCumulateSessions_Type())
crasL2LCumulateSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:crasL2LCumulateSessions.setStatus(_B)
if mibBuilder.loadTexts:crasL2LCumulateSessions.setUnits(_D)
_CrasL2LPeakConcurrentSessions_Type=Unsigned32
_CrasL2LPeakConcurrentSessions_Object=MibScalar
crasL2LPeakConcurrentSessions=_CrasL2LPeakConcurrentSessions_Object((1,3,6,1,4,1,9,9,392,1,3,31),_CrasL2LPeakConcurrentSessions_Type())
crasL2LPeakConcurrentSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:crasL2LPeakConcurrentSessions.setStatus(_B)
if mibBuilder.loadTexts:crasL2LPeakConcurrentSessions.setUnits(_D)
_CrasLBNumSessions_Type=Gauge32
_CrasLBNumSessions_Object=MibScalar
crasLBNumSessions=_CrasLBNumSessions_Object((1,3,6,1,4,1,9,9,392,1,3,32),_CrasLBNumSessions_Type())
crasLBNumSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:crasLBNumSessions.setStatus(_B)
if mibBuilder.loadTexts:crasLBNumSessions.setUnits(_D)
_CrasLBCumulateSessions_Type=Counter32
_CrasLBCumulateSessions_Object=MibScalar
crasLBCumulateSessions=_CrasLBCumulateSessions_Object((1,3,6,1,4,1,9,9,392,1,3,33),_CrasLBCumulateSessions_Type())
crasLBCumulateSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:crasLBCumulateSessions.setStatus(_B)
if mibBuilder.loadTexts:crasLBCumulateSessions.setUnits(_D)
_CrasLBPeakConcurrentSessions_Type=Unsigned32
_CrasLBPeakConcurrentSessions_Object=MibScalar
crasLBPeakConcurrentSessions=_CrasLBPeakConcurrentSessions_Object((1,3,6,1,4,1,9,9,392,1,3,34),_CrasLBPeakConcurrentSessions_Type())
crasLBPeakConcurrentSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:crasLBPeakConcurrentSessions.setStatus(_B)
if mibBuilder.loadTexts:crasLBPeakConcurrentSessions.setUnits(_D)
_CrasSVCNumSessions_Type=Gauge32
_CrasSVCNumSessions_Object=MibScalar
crasSVCNumSessions=_CrasSVCNumSessions_Object((1,3,6,1,4,1,9,9,392,1,3,35),_CrasSVCNumSessions_Type())
crasSVCNumSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:crasSVCNumSessions.setStatus(_B)
if mibBuilder.loadTexts:crasSVCNumSessions.setUnits(_D)
_CrasSVCCumulateSessions_Type=Counter32
_CrasSVCCumulateSessions_Object=MibScalar
crasSVCCumulateSessions=_CrasSVCCumulateSessions_Object((1,3,6,1,4,1,9,9,392,1,3,36),_CrasSVCCumulateSessions_Type())
crasSVCCumulateSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:crasSVCCumulateSessions.setStatus(_B)
if mibBuilder.loadTexts:crasSVCCumulateSessions.setUnits(_D)
_CrasSVCPeakConcurrentSessions_Type=Unsigned32
_CrasSVCPeakConcurrentSessions_Object=MibScalar
crasSVCPeakConcurrentSessions=_CrasSVCPeakConcurrentSessions_Object((1,3,6,1,4,1,9,9,392,1,3,37),_CrasSVCPeakConcurrentSessions_Type())
crasSVCPeakConcurrentSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:crasSVCPeakConcurrentSessions.setStatus(_B)
if mibBuilder.loadTexts:crasSVCPeakConcurrentSessions.setUnits(_D)
_CrasWebvpnNumSessions_Type=Gauge32
_CrasWebvpnNumSessions_Object=MibScalar
crasWebvpnNumSessions=_CrasWebvpnNumSessions_Object((1,3,6,1,4,1,9,9,392,1,3,38),_CrasWebvpnNumSessions_Type())
crasWebvpnNumSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:crasWebvpnNumSessions.setStatus(_B)
if mibBuilder.loadTexts:crasWebvpnNumSessions.setUnits(_D)
_CrasWebvpnCumulateSessions_Type=Counter32
_CrasWebvpnCumulateSessions_Object=MibScalar
crasWebvpnCumulateSessions=_CrasWebvpnCumulateSessions_Object((1,3,6,1,4,1,9,9,392,1,3,39),_CrasWebvpnCumulateSessions_Type())
crasWebvpnCumulateSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:crasWebvpnCumulateSessions.setStatus(_B)
if mibBuilder.loadTexts:crasWebvpnCumulateSessions.setUnits(_D)
_CrasWebvpnPeakConcurrentSessions_Type=Unsigned32
_CrasWebvpnPeakConcurrentSessions_Object=MibScalar
crasWebvpnPeakConcurrentSessions=_CrasWebvpnPeakConcurrentSessions_Object((1,3,6,1,4,1,9,9,392,1,3,40),_CrasWebvpnPeakConcurrentSessions_Type())
crasWebvpnPeakConcurrentSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:crasWebvpnPeakConcurrentSessions.setStatus(_B)
if mibBuilder.loadTexts:crasWebvpnPeakConcurrentSessions.setUnits(_D)
_CrasNumPeakSessions_Type=Unsigned32
_CrasNumPeakSessions_Object=MibScalar
crasNumPeakSessions=_CrasNumPeakSessions_Object((1,3,6,1,4,1,9,9,392,1,3,41),_CrasNumPeakSessions_Type())
crasNumPeakSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:crasNumPeakSessions.setStatus(_B)
if mibBuilder.loadTexts:crasNumPeakSessions.setUnits(_D)
_CrasFailures_ObjectIdentity=ObjectIdentity
crasFailures=_CrasFailures_ObjectIdentity((1,3,6,1,4,1,9,9,392,1,4))
_CrasFailuresGlobals_ObjectIdentity=ObjectIdentity
crasFailuresGlobals=_CrasFailuresGlobals_ObjectIdentity((1,3,6,1,4,1,9,9,392,1,4,1))
_CrasNumTotalFailures_Type=Counter64
_CrasNumTotalFailures_Object=MibScalar
crasNumTotalFailures=_CrasNumTotalFailures_Object((1,3,6,1,4,1,9,9,392,1,4,1,1),_CrasNumTotalFailures_Type())
crasNumTotalFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:crasNumTotalFailures.setStatus(_B)
class _CrasNumDeclinedSessions_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CrasNumDeclinedSessions_Type.__name__=_I
_CrasNumDeclinedSessions_Object=MibScalar
crasNumDeclinedSessions=_CrasNumDeclinedSessions_Object((1,3,6,1,4,1,9,9,392,1,4,1,2),_CrasNumDeclinedSessions_Type())
crasNumDeclinedSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:crasNumDeclinedSessions.setStatus(_B)
if mibBuilder.loadTexts:crasNumDeclinedSessions.setUnits(_D)
_CrasNumSetupFailInsufResources_Type=Counter64
_CrasNumSetupFailInsufResources_Object=MibScalar
crasNumSetupFailInsufResources=_CrasNumSetupFailInsufResources_Object((1,3,6,1,4,1,9,9,392,1,4,1,3),_CrasNumSetupFailInsufResources_Type())
crasNumSetupFailInsufResources.setMaxAccess(_C)
if mibBuilder.loadTexts:crasNumSetupFailInsufResources.setStatus(_B)
if mibBuilder.loadTexts:crasNumSetupFailInsufResources.setUnits(_D)
_CrasNumAbortedSessions_Type=Counter64
_CrasNumAbortedSessions_Object=MibScalar
crasNumAbortedSessions=_CrasNumAbortedSessions_Object((1,3,6,1,4,1,9,9,392,1,4,1,4),_CrasNumAbortedSessions_Type())
crasNumAbortedSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:crasNumAbortedSessions.setStatus(_B)
if mibBuilder.loadTexts:crasNumAbortedSessions.setUnits(_D)
_CrasFailGlobalCntl_ObjectIdentity=ObjectIdentity
crasFailGlobalCntl=_CrasFailGlobalCntl_ObjectIdentity((1,3,6,1,4,1,9,9,392,1,4,2))
class _CrasFailTableSize_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CrasFailTableSize_Type.__name__=_I
_CrasFailTableSize_Object=MibScalar
crasFailTableSize=_CrasFailTableSize_Object((1,3,6,1,4,1,9,9,392,1,4,2,1),_CrasFailTableSize_Type())
crasFailTableSize.setMaxAccess(_L)
if mibBuilder.loadTexts:crasFailTableSize.setStatus(_B)
_CrasSessFailures_ObjectIdentity=ObjectIdentity
crasSessFailures=_CrasSessFailures_ObjectIdentity((1,3,6,1,4,1,9,9,392,1,4,3))
_CrasSessFailTable_Object=MibTable
crasSessFailTable=_CrasSessFailTable_Object((1,3,6,1,4,1,9,9,392,1,4,3,1))
if mibBuilder.loadTexts:crasSessFailTable.setStatus(_B)
_CrasSessFailEntry_Object=MibTableRow
crasSessFailEntry=_CrasSessFailEntry_Object((1,3,6,1,4,1,9,9,392,1,4,3,1,1))
crasSessFailEntry.setIndexNames((0,_A,_r))
if mibBuilder.loadTexts:crasSessFailEntry.setStatus(_B)
_CrasSessFailIndex_Type=FailureRecordIndex
_CrasSessFailIndex_Object=MibTableColumn
crasSessFailIndex=_CrasSessFailIndex_Object((1,3,6,1,4,1,9,9,392,1,4,3,1,1,1),_CrasSessFailIndex_Type())
crasSessFailIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:crasSessFailIndex.setStatus(_B)
_CrasSessFailUsername_Type=SnmpAdminString
_CrasSessFailUsername_Object=MibTableColumn
crasSessFailUsername=_CrasSessFailUsername_Object((1,3,6,1,4,1,9,9,392,1,4,3,1,1,2),_CrasSessFailUsername_Type())
crasSessFailUsername.setMaxAccess(_C)
if mibBuilder.loadTexts:crasSessFailUsername.setStatus(_B)
_CrasSessFailGroupname_Type=SnmpAdminString
_CrasSessFailGroupname_Object=MibTableColumn
crasSessFailGroupname=_CrasSessFailGroupname_Object((1,3,6,1,4,1,9,9,392,1,4,3,1,1,3),_CrasSessFailGroupname_Type())
crasSessFailGroupname.setMaxAccess(_C)
if mibBuilder.loadTexts:crasSessFailGroupname.setStatus(_B)
class _CrasSessFailType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('setupFailure',1),('operationalFailure',2)))
_CrasSessFailType_Type.__name__=_F
_CrasSessFailType_Object=MibTableColumn
crasSessFailType=_CrasSessFailType_Object((1,3,6,1,4,1,9,9,392,1,4,3,1,1,4),_CrasSessFailType_Type())
crasSessFailType.setMaxAccess(_C)
if mibBuilder.loadTexts:crasSessFailType.setStatus(_B)
class _CrasSessFailReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_H,1),('internalError',2),('authenticationFailure',3),('authorizationFailure',4),('sysCapExceeded',5),('peerAbortRequest',6),('peerLost',7),('operRequest',8)))
_CrasSessFailReason_Type.__name__=_F
_CrasSessFailReason_Object=MibTableColumn
crasSessFailReason=_CrasSessFailReason_Object((1,3,6,1,4,1,9,9,392,1,4,3,1,1,5),_CrasSessFailReason_Type())
crasSessFailReason.setMaxAccess(_C)
if mibBuilder.loadTexts:crasSessFailReason.setStatus(_B)
_CrasSessFailTime_Type=TimeStamp
_CrasSessFailTime_Object=MibTableColumn
crasSessFailTime=_CrasSessFailTime_Object((1,3,6,1,4,1,9,9,392,1,4,3,1,1,6),_CrasSessFailTime_Type())
crasSessFailTime.setMaxAccess(_C)
if mibBuilder.loadTexts:crasSessFailTime.setStatus(_B)
_CrasSessFailSessionIndex_Type=SessionIndex
_CrasSessFailSessionIndex_Object=MibTableColumn
crasSessFailSessionIndex=_CrasSessFailSessionIndex_Object((1,3,6,1,4,1,9,9,392,1,4,3,1,1,7),_CrasSessFailSessionIndex_Type())
crasSessFailSessionIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:crasSessFailSessionIndex.setStatus(_B)
_CrasSessFailISPAddrType_Type=InetAddressType
_CrasSessFailISPAddrType_Object=MibTableColumn
crasSessFailISPAddrType=_CrasSessFailISPAddrType_Object((1,3,6,1,4,1,9,9,392,1,4,3,1,1,8),_CrasSessFailISPAddrType_Type())
crasSessFailISPAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:crasSessFailISPAddrType.setStatus(_B)
_CrasSessFailISPAddr_Type=InetAddress
_CrasSessFailISPAddr_Object=MibTableColumn
crasSessFailISPAddr=_CrasSessFailISPAddr_Object((1,3,6,1,4,1,9,9,392,1,4,3,1,1,9),_CrasSessFailISPAddr_Type())
crasSessFailISPAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:crasSessFailISPAddr.setStatus(_B)
_CrasSessFailLocalAddrType_Type=InetAddressType
_CrasSessFailLocalAddrType_Object=MibTableColumn
crasSessFailLocalAddrType=_CrasSessFailLocalAddrType_Object((1,3,6,1,4,1,9,9,392,1,4,3,1,1,10),_CrasSessFailLocalAddrType_Type())
crasSessFailLocalAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:crasSessFailLocalAddrType.setStatus(_B)
_CrasSessFailLocalAddr_Type=InetAddress
_CrasSessFailLocalAddr_Object=MibTableColumn
crasSessFailLocalAddr=_CrasSessFailLocalAddr_Object((1,3,6,1,4,1,9,9,392,1,4,3,1,1,11),_CrasSessFailLocalAddr_Type())
crasSessFailLocalAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:crasSessFailLocalAddr.setStatus(_B)
_CrasFailLastFailIndex_Type=FailureRecordIndex
_CrasFailLastFailIndex_Object=MibScalar
crasFailLastFailIndex=_CrasFailLastFailIndex_Object((1,3,6,1,4,1,9,9,392,1,4,3,2),_CrasFailLastFailIndex_Type())
crasFailLastFailIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:crasFailLastFailIndex.setStatus(_B)
_CrasGroupFailures_ObjectIdentity=ObjectIdentity
crasGroupFailures=_CrasGroupFailures_ObjectIdentity((1,3,6,1,4,1,9,9,392,1,4,4))
_CrasGrpFailTable_Object=MibTable
crasGrpFailTable=_CrasGrpFailTable_Object((1,3,6,1,4,1,9,9,392,1,4,4,1))
if mibBuilder.loadTexts:crasGrpFailTable.setStatus(_B)
_CrasGrpFailEntry_Object=MibTableRow
crasGrpFailEntry=_CrasGrpFailEntry_Object((1,3,6,1,4,1,9,9,392,1,4,4,1,1))
crasGrpFailEntry.setIndexNames((0,_A,_s))
if mibBuilder.loadTexts:crasGrpFailEntry.setStatus(_B)
class _CrasGrpFailGroupname_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CrasGrpFailGroupname_Type.__name__=_M
_CrasGrpFailGroupname_Object=MibTableColumn
crasGrpFailGroupname=_CrasGrpFailGroupname_Object((1,3,6,1,4,1,9,9,392,1,4,4,1,1,1),_CrasGrpFailGroupname_Type())
crasGrpFailGroupname.setMaxAccess(_K)
if mibBuilder.loadTexts:crasGrpFailGroupname.setStatus(_B)
_CrasGrpFailNumFailAuths_Type=Counter64
_CrasGrpFailNumFailAuths_Object=MibTableColumn
crasGrpFailNumFailAuths=_CrasGrpFailNumFailAuths_Object((1,3,6,1,4,1,9,9,392,1,4,4,1,1,2),_CrasGrpFailNumFailAuths_Type())
crasGrpFailNumFailAuths.setMaxAccess(_C)
if mibBuilder.loadTexts:crasGrpFailNumFailAuths.setStatus(_B)
_CrasGrpFailNumResourceFailures_Type=Counter64
_CrasGrpFailNumResourceFailures_Object=MibTableColumn
crasGrpFailNumResourceFailures=_CrasGrpFailNumResourceFailures_Object((1,3,6,1,4,1,9,9,392,1,4,4,1,1,3),_CrasGrpFailNumResourceFailures_Type())
crasGrpFailNumResourceFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:crasGrpFailNumResourceFailures.setStatus(_B)
_CrasGrpFailNumDeclined_Type=Counter64
_CrasGrpFailNumDeclined_Object=MibTableColumn
crasGrpFailNumDeclined=_CrasGrpFailNumDeclined_Object((1,3,6,1,4,1,9,9,392,1,4,4,1,1,4),_CrasGrpFailNumDeclined_Type())
crasGrpFailNumDeclined.setMaxAccess(_C)
if mibBuilder.loadTexts:crasGrpFailNumDeclined.setStatus(_B)
_CrasGrpFailNumTerminatedMgmt_Type=Counter64
_CrasGrpFailNumTerminatedMgmt_Object=MibTableColumn
crasGrpFailNumTerminatedMgmt=_CrasGrpFailNumTerminatedMgmt_Object((1,3,6,1,4,1,9,9,392,1,4,4,1,1,5),_CrasGrpFailNumTerminatedMgmt_Type())
crasGrpFailNumTerminatedMgmt.setMaxAccess(_C)
if mibBuilder.loadTexts:crasGrpFailNumTerminatedMgmt.setStatus(_B)
_CrasGrpFailNumTerminatedOther_Type=Counter64
_CrasGrpFailNumTerminatedOther_Object=MibTableColumn
crasGrpFailNumTerminatedOther=_CrasGrpFailNumTerminatedOther_Object((1,3,6,1,4,1,9,9,392,1,4,4,1,1,6),_CrasGrpFailNumTerminatedOther_Type())
crasGrpFailNumTerminatedOther.setMaxAccess(_C)
if mibBuilder.loadTexts:crasGrpFailNumTerminatedOther.setStatus(_B)
_CrasSecurity_ObjectIdentity=ObjectIdentity
crasSecurity=_CrasSecurity_ObjectIdentity((1,3,6,1,4,1,9,9,392,1,5))
_CrasSecurityGlobals_ObjectIdentity=ObjectIdentity
crasSecurityGlobals=_CrasSecurityGlobals_ObjectIdentity((1,3,6,1,4,1,9,9,392,1,5,1))
_CrasNumDisabledAccounts_Type=Counter64
_CrasNumDisabledAccounts_Object=MibScalar
crasNumDisabledAccounts=_CrasNumDisabledAccounts_Object((1,3,6,1,4,1,9,9,392,1,5,1,1),_CrasNumDisabledAccounts_Type())
crasNumDisabledAccounts.setMaxAccess(_C)
if mibBuilder.loadTexts:crasNumDisabledAccounts.setStatus(_B)
if mibBuilder.loadTexts:crasNumDisabledAccounts.setUnits(_O)
_CrasThresholds_ObjectIdentity=ObjectIdentity
crasThresholds=_CrasThresholds_ObjectIdentity((1,3,6,1,4,1,9,9,392,1,6))
class _CrasThrMaxSessions_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CrasThrMaxSessions_Type.__name__=_F
_CrasThrMaxSessions_Object=MibScalar
crasThrMaxSessions=_CrasThrMaxSessions_Object((1,3,6,1,4,1,9,9,392,1,6,1),_CrasThrMaxSessions_Type())
crasThrMaxSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:crasThrMaxSessions.setStatus(_B)
if mibBuilder.loadTexts:crasThrMaxSessions.setUnits(_D)
class _CrasThrMaxFailedAuths_Type(Unsigned32):defaultValue=4294967295;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CrasThrMaxFailedAuths_Type.__name__=_I
_CrasThrMaxFailedAuths_Object=MibScalar
crasThrMaxFailedAuths=_CrasThrMaxFailedAuths_Object((1,3,6,1,4,1,9,9,392,1,6,2),_CrasThrMaxFailedAuths_Type())
crasThrMaxFailedAuths.setMaxAccess(_C)
if mibBuilder.loadTexts:crasThrMaxFailedAuths.setStatus(_B)
class _CrasThrMaxThroughput_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CrasThrMaxThroughput_Type.__name__=_F
_CrasThrMaxThroughput_Object=MibScalar
crasThrMaxThroughput=_CrasThrMaxThroughput_Object((1,3,6,1,4,1,9,9,392,1,6,3),_CrasThrMaxThroughput_Type())
crasThrMaxThroughput.setMaxAccess(_C)
if mibBuilder.loadTexts:crasThrMaxThroughput.setStatus(_B)
if mibBuilder.loadTexts:crasThrMaxThroughput.setUnits('Octets Per Second')
_CrasNotifCntl_ObjectIdentity=ObjectIdentity
crasNotifCntl=_CrasNotifCntl_ObjectIdentity((1,3,6,1,4,1,9,9,392,1,7))
class _CrasCntlTooManySessions_Type(TruthValue):defaultValue=2
_CrasCntlTooManySessions_Type.__name__=_N
_CrasCntlTooManySessions_Object=MibScalar
crasCntlTooManySessions=_CrasCntlTooManySessions_Object((1,3,6,1,4,1,9,9,392,1,7,1),_CrasCntlTooManySessions_Type())
crasCntlTooManySessions.setMaxAccess(_L)
if mibBuilder.loadTexts:crasCntlTooManySessions.setStatus(_B)
class _CrasCntlTooManyFailedAuths_Type(TruthValue):defaultValue=2
_CrasCntlTooManyFailedAuths_Type.__name__=_N
_CrasCntlTooManyFailedAuths_Object=MibScalar
crasCntlTooManyFailedAuths=_CrasCntlTooManyFailedAuths_Object((1,3,6,1,4,1,9,9,392,1,7,2),_CrasCntlTooManyFailedAuths_Type())
crasCntlTooManyFailedAuths.setMaxAccess(_L)
if mibBuilder.loadTexts:crasCntlTooManyFailedAuths.setStatus(_B)
class _CrasCntlTooHighThroughput_Type(TruthValue):defaultValue=2
_CrasCntlTooHighThroughput_Type.__name__=_N
_CrasCntlTooHighThroughput_Object=MibScalar
crasCntlTooHighThroughput=_CrasCntlTooHighThroughput_Object((1,3,6,1,4,1,9,9,392,1,7,3),_CrasCntlTooHighThroughput_Type())
crasCntlTooHighThroughput.setMaxAccess(_L)
if mibBuilder.loadTexts:crasCntlTooHighThroughput.setStatus(_B)
_CiscoRasMonitorMIBConform_ObjectIdentity=ObjectIdentity
ciscoRasMonitorMIBConform=_CiscoRasMonitorMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,392,2))
_CiscoRasMonitorMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoRasMonitorMIBCompliances=_CiscoRasMonitorMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,392,2,1))
_CiscoRasMonitorMIBGroups_ObjectIdentity=ObjectIdentity
ciscoRasMonitorMIBGroups=_CiscoRasMonitorMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,392,2,2))
ciscoRasCapacityGroup=ObjectGroup((1,3,6,1,4,1,9,9,392,2,2,1))
ciscoRasCapacityGroup.setObjects(*((_A,_P),(_A,_Q),(_A,_t),(_A,_u)))
if mibBuilder.loadTexts:ciscoRasCapacityGroup.setStatus(_B)
ciscoRasResourceUsageGroup=ObjectGroup((1,3,6,1,4,1,9,9,392,2,2,2))
ciscoRasResourceUsageGroup.setObjects((_A,_v))
if mibBuilder.loadTexts:ciscoRasResourceUsageGroup.setStatus(_B)
ciscoRasActivityGroup=ObjectGroup((1,3,6,1,4,1,9,9,392,2,2,3))
ciscoRasActivityGroup.setObjects(*((_A,_R),(_A,_w),(_A,_S),(_A,_x),(_A,_y),(_A,_T),(_A,_U),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_Ab)))
if mibBuilder.loadTexts:ciscoRasActivityGroup.setStatus(_B)
ciscoRasGrpActivityGroup=ObjectGroup((1,3,6,1,4,1,9,9,392,2,2,4))
ciscoRasGrpActivityGroup.setObjects(*((_A,_Ac),(_A,_Ad),(_A,_Ae),(_A,_Af),(_A,_Ag),(_A,_Ah),(_A,_Ai),(_A,_Aj)))
if mibBuilder.loadTexts:ciscoRasGrpActivityGroup.setStatus(_B)
ciscoRasMandatoryFailureGroup=ObjectGroup((1,3,6,1,4,1,9,9,392,2,2,5))
ciscoRasMandatoryFailureGroup.setObjects(*((_A,_Ak),(_A,_V),(_A,_Al),(_A,_Am)))
if mibBuilder.loadTexts:ciscoRasMandatoryFailureGroup.setStatus(_B)
ciscoRasOptionalFailureGroup=ObjectGroup((1,3,6,1,4,1,9,9,392,2,2,6))
ciscoRasOptionalFailureGroup.setObjects(*((_A,_An),(_A,_Ao),(_A,_Ap),(_A,_Aq),(_A,_Ar),(_A,_As),(_A,_At),(_A,_Au),(_A,_Av),(_A,_Aw),(_A,_Ax),(_A,_Ay),(_A,_Az),(_A,_A_),(_A,_B0),(_A,_B1),(_A,_B2)))
if mibBuilder.loadTexts:ciscoRasOptionalFailureGroup.setStatus(_B)
ciscoRasSecurityGroup=ObjectGroup((1,3,6,1,4,1,9,9,392,2,2,7))
ciscoRasSecurityGroup.setObjects((_A,_B3))
if mibBuilder.loadTexts:ciscoRasSecurityGroup.setStatus(_B)
ciscoRasThresholdsGroup=ObjectGroup((1,3,6,1,4,1,9,9,392,2,2,8))
ciscoRasThresholdsGroup.setObjects(*((_A,_W),(_A,_X),(_A,_Y)))
if mibBuilder.loadTexts:ciscoRasThresholdsGroup.setStatus(_B)
ciscoRasNotificationCntlGroup=ObjectGroup((1,3,6,1,4,1,9,9,392,2,2,9))
ciscoRasNotificationCntlGroup.setObjects(*((_A,_B4),(_A,_B5),(_A,_B6)))
if mibBuilder.loadTexts:ciscoRasNotificationCntlGroup.setStatus(_B)
ciscoRasActivityGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,392,2,2,11))
ciscoRasActivityGroupRev1.setObjects(*((_A,_B7),(_A,_B8),(_A,_B9),(_A,_BA),(_A,_BB),(_A,_BC),(_A,_BD),(_A,_BE),(_A,_BF),(_A,_BG),(_A,_BH),(_A,_BI),(_A,_BJ),(_A,_BK),(_A,_BL),(_A,_BM),(_A,_BN),(_A,_BO)))
if mibBuilder.loadTexts:ciscoRasActivityGroupRev1.setStatus(_B)
ciscoRasTooManySessions=NotificationType((1,3,6,1,4,1,9,9,392,0,1))
ciscoRasTooManySessions.setObjects(*((_A,_R),(_A,_S),(_A,_P),(_A,_Q),(_A,_W)))
if mibBuilder.loadTexts:ciscoRasTooManySessions.setStatus(_B)
ciscoRasTooManyFailedAuths=NotificationType((1,3,6,1,4,1,9,9,392,0,2))
ciscoRasTooManyFailedAuths.setObjects(*((_A,_V),(_A,_X)))
if mibBuilder.loadTexts:ciscoRasTooManyFailedAuths.setStatus(_B)
ciscoRasTooHighThroughput=NotificationType((1,3,6,1,4,1,9,9,392,0,3))
ciscoRasTooHighThroughput.setObjects(*((_A,_T),(_A,_U),(_A,_Y)))
if mibBuilder.loadTexts:ciscoRasTooHighThroughput.setStatus(_B)
ciscoRasNotificationsGroup=NotificationGroup((1,3,6,1,4,1,9,9,392,2,2,10))
ciscoRasNotificationsGroup.setObjects(*((_A,_BP),(_A,_BQ),(_A,_BR)))
if mibBuilder.loadTexts:ciscoRasNotificationsGroup.setStatus(_B)
ciscoRasMonitorMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,392,2,1,1))
ciscoRasMonitorMIBCompliance.setObjects(*((_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i)))
if mibBuilder.loadTexts:ciscoRasMonitorMIBCompliance.setStatus('deprecated')
ciscoRasMonitorMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,392,2,1,2))
ciscoRasMonitorMIBComplianceRev1.setObjects(*((_A,_Z),(_A,_a),(_A,_b),(_A,_BS),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i)))
if mibBuilder.loadTexts:ciscoRasMonitorMIBComplianceRev1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'RasProtocol':RasProtocol,'UserAuthenMethod':UserAuthenMethod,'UserAuthorMethod':UserAuthorMethod,'SessionEncrAlgo':SessionEncrAlgo,'SessionAuthAlgo':SessionAuthAlgo,'SessionCompressionAlgo':SessionCompressionAlgo,'SessionStatus':SessionStatus,'SessionIndex':SessionIndex,'FailureRecordIndex':FailureRecordIndex,'ciscoRemoteAccessMonitorMIB':ciscoRemoteAccessMonitorMIB,'ciscoRasMonitorMIBNotifs':ciscoRasMonitorMIBNotifs,_BR:ciscoRasTooManySessions,_BQ:ciscoRasTooManyFailedAuths,_BP:ciscoRasTooHighThroughput,'ciscoRasMonitorMIBObjects':ciscoRasMonitorMIBObjects,'crasCapacity':crasCapacity,_P:crasMaxSessionsSupportable,_Q:crasMaxUsersSupportable,_t:crasMaxGroupsSupportable,_u:crasNumCryptoAccelerators,'crasResourceUsage':crasResourceUsage,_v:crasGlobalBwUsage,'crasActivity':crasActivity,_R:crasNumSessions,_w:crasNumPrevSessions,_S:crasNumUsers,_Ac:crasNumGroups,_x:crasGlobalInPkts,_y:crasGlobalOutPkts,_T:crasGlobalInOctets,_z:crasGlobalInDecompOctets,_U:crasGlobalOutOctets,_A0:crasGlobalOutUncompOctets,_A1:crasGlobalInDropPkts,_A2:crasGlobalOutDropPkts,'crasSessionTable':crasSessionTable,'crasSessionEntry':crasSessionEntry,_o:crasUsername,_A3:crasGroup,_p:crasSessionIndex,_A4:crasAuthenMethod,_A5:crasAuthorMethod,_A6:crasSessionDuration,_A7:crasLocalAddressType,_A8:crasLocalAddress,_A9:crasISPAddressType,_AA:crasISPAddress,_AB:crasSessionProtocol,_AC:crasProtocolElement,_AD:crasSessionEncryptionAlgo,_AE:crasSessionPktAuthenAlgo,_AF:crasSessionCompressionAlgo,_AG:crasHeartbeatInterval,_AH:crasClientVendorString,_AI:crasClientVersionString,_AJ:crasClientOSVendorString,_AK:crasClientOSVersionString,_AL:crasPrimWINSServerAddrType,_AM:crasPrimWINSServer,_AN:crasSecWINSServerAddrType,_AO:crasSecWINSServer,_AP:crasPrimDNSServerAddrType,_AQ:crasPrimDNSServer,_AR:crasSecDNSServerAddrType,_AS:crasSecDNSServer,_AT:crasDHCPServerAddrType,_AU:crasDHCPServer,_AV:crasSessionInPkts,_AW:crasSessionOutPkts,_AX:crasSessionInDropPkts,_AY:crasSessionOutDropPkts,_AZ:crasSessionInOctets,_Aa:crasSessionOutOctets,_Ab:crasSessionState,'crasActGroupTable':crasActGroupTable,'crasActGroupEntry':crasActGroupEntry,_q:crasActGrpName,_Ad:crasActGrNumUsers,_Ae:crasActGrpInPkts,_Af:crasActGrpOutPkts,_Ag:crasActGrpInDropPkts,_Ah:crasActGrpOutDropPkts,_Ai:crasActGrpInOctets,_Aj:crasActGrpOutOctets,_B7:crasEmailNumSessions,_B8:crasEmailCumulateSessions,_B9:crasEmailPeakConcurrentSessions,_BA:crasIPSecNumSessions,_BB:crasIPSecCumulateSessions,_BC:crasIPSecPeakConcurrentSessions,_BD:crasL2LNumSessions,_BE:crasL2LCumulateSessions,_BF:crasL2LPeakConcurrentSessions,_BG:crasLBNumSessions,_BH:crasLBCumulateSessions,_BI:crasLBPeakConcurrentSessions,_BJ:crasSVCNumSessions,_BK:crasSVCCumulateSessions,_BL:crasSVCPeakConcurrentSessions,_BM:crasWebvpnNumSessions,_BN:crasWebvpnCumulateSessions,_BO:crasWebvpnPeakConcurrentSessions,'crasNumPeakSessions':crasNumPeakSessions,'crasFailures':crasFailures,'crasFailuresGlobals':crasFailuresGlobals,_Ak:crasNumTotalFailures,_V:crasNumDeclinedSessions,_An:crasNumSetupFailInsufResources,_Al:crasNumAbortedSessions,'crasFailGlobalCntl':crasFailGlobalCntl,_Am:crasFailTableSize,'crasSessFailures':crasSessFailures,'crasSessFailTable':crasSessFailTable,'crasSessFailEntry':crasSessFailEntry,_r:crasSessFailIndex,_Ao:crasSessFailUsername,_Ap:crasSessFailGroupname,_Aq:crasSessFailType,_Ar:crasSessFailReason,_As:crasSessFailTime,_At:crasSessFailSessionIndex,_Aw:crasSessFailISPAddrType,_Au:crasSessFailISPAddr,_Ax:crasSessFailLocalAddrType,_Av:crasSessFailLocalAddr,_Ay:crasFailLastFailIndex,'crasGroupFailures':crasGroupFailures,'crasGrpFailTable':crasGrpFailTable,'crasGrpFailEntry':crasGrpFailEntry,_s:crasGrpFailGroupname,_Az:crasGrpFailNumFailAuths,_A_:crasGrpFailNumResourceFailures,_B0:crasGrpFailNumDeclined,_B1:crasGrpFailNumTerminatedMgmt,_B2:crasGrpFailNumTerminatedOther,'crasSecurity':crasSecurity,'crasSecurityGlobals':crasSecurityGlobals,_B3:crasNumDisabledAccounts,'crasThresholds':crasThresholds,_W:crasThrMaxSessions,_X:crasThrMaxFailedAuths,_Y:crasThrMaxThroughput,'crasNotifCntl':crasNotifCntl,_B4:crasCntlTooManySessions,_B5:crasCntlTooManyFailedAuths,_B6:crasCntlTooHighThroughput,'ciscoRasMonitorMIBConform':ciscoRasMonitorMIBConform,'ciscoRasMonitorMIBCompliances':ciscoRasMonitorMIBCompliances,'ciscoRasMonitorMIBCompliance':ciscoRasMonitorMIBCompliance,'ciscoRasMonitorMIBComplianceRev1':ciscoRasMonitorMIBComplianceRev1,'ciscoRasMonitorMIBGroups':ciscoRasMonitorMIBGroups,_Z:ciscoRasCapacityGroup,_a:ciscoRasResourceUsageGroup,_b:ciscoRasActivityGroup,_d:ciscoRasGrpActivityGroup,_c:ciscoRasMandatoryFailureGroup,_e:ciscoRasOptionalFailureGroup,_f:ciscoRasSecurityGroup,_g:ciscoRasThresholdsGroup,_i:ciscoRasNotificationCntlGroup,_h:ciscoRasNotificationsGroup,_BS:ciscoRasActivityGroupRev1})