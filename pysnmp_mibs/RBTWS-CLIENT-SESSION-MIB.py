_A8='rbtwsClientSessRoamingHistoryTableGroupRev2'
_A7='rbtwsClientSessClientSessionTableGroupRev2'
_A6='rbtwsClientSessRoamingHistoryTableGroup'
_A5='rbtwsClientSessClientSessionTableGroup'
_A4='rbtwsClientSessionCommonGroup'
_A3='rbtwsClSessRoamHistPhysPortNum'
_A2='rbtwsClSessRoamHistApNum'
_A1='rbtwsClSessRoamHistAccessMode'
_A0='rbtwsClSessClientSessPhysPortNum'
_z='rbtwsClSessClientSessApNum'
_y='rbtwsClSessClientSessAccessMode'
_x='rbtwsClSessTotalSessions'
_w='rbtwsClSessClientSessState'
_v='rbtwsClSessClientSessAuthMethod'
_u='rbtwsClSessClientSessStatsMacAddress'
_t='rbtwsClSessRoamHistIndex'
_s='rbtwsClSessRoamHistMacAddress'
_r='rbtwsClSessClientSessMacAddress'
_q='rbtwsClientSessClientSessionStatisticsTableGroup'
_p='rbtwsClientSessScalarsGroup'
_o='rbtwsClSessClientSessSessionState'
_n='rbtwsClSessClientSessDot1xAuthMethod'
_m='rbtwsClSessClientSessLoginType'
_l='rbtwsClSessClientSessStatsLastSNR'
_k='rbtwsClSessClientSessStatsLastRssi'
_j='rbtwsClSessClientSessStatsLastRate'
_i='rbtwsClSessClientSessStatsEncErrOctet'
_h='rbtwsClSessClientSessStatsEncErrPkt'
_g='rbtwsClSessClientSessStatsMultiOctetIn'
_f='rbtwsClSessClientSessStatsMultiPktIn'
_e='rbtwsClSessClientSessStatsUniOctetOut'
_d='rbtwsClSessClientSessStatsUniPktOut'
_c='rbtwsClSessClientSessStatsUniOctetIn'
_b='rbtwsClSessClientSessStatsUniPktIn'
_a='rbtwsClSessRoamHistApNumOrPort'
_Z='rbtwsClSessRoamHistAccessType'
_Y='rbtwsClSessClientSessPortOrNum'
_X='rbtwsClSessClientSessAccessType'
_W='Unsigned32'
_V='rbtwsClSessRoamHistTimeStamp'
_U='rbtwsClSessRoamHistIpAddress'
_T='rbtwsClSessRoamHistRadioNum'
_S='rbtwsClSessRoamHistApSerialNum'
_R='rbtwsClSessClientSessSsid'
_Q='rbtwsClSessClientSessTimeStamp'
_P='rbtwsClSessClientSessVlanTag'
_O='rbtwsClSessClientSessAuthServer'
_N='rbtwsClSessClientSessRadioNum'
_M='rbtwsClSessClientSessApSerialNum'
_L='rbtwsClSessClientSessVlan'
_K='rbtwsClSessClientSessEncryptionType'
_J='rbtwsClSessClientSessIpAddress'
_I='rbtwsClSessClientSessUsername'
_H='rbtwsClSessClientSessSessionId'
_G='not-accessible'
_F='deprecated'
_E='DisplayString'
_D='obsolete'
_C='read-only'
_B='current'
_A='RBTWS-CLIENT-SESSION-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
RbtwsAccessType,RbtwsApNum,RbtwsApSerialNum,RbtwsRadioNum,RbtwsRadioRate,RbtwsRssi=mibBuilder.importSymbols('RBTWS-AP-TC','RbtwsAccessType','RbtwsApNum','RbtwsApSerialNum','RbtwsRadioNum','RbtwsRadioRate','RbtwsRssi')
RbtwsClientAccessMode,RbtwsClientAuthenProtocolType,RbtwsClientSessionState,RbtwsUserAccessType=mibBuilder.importSymbols('RBTWS-CLIENT-SESSION-TC','RbtwsClientAccessMode','RbtwsClientAuthenProtocolType','RbtwsClientSessionState','RbtwsUserAccessType')
rbtwsMibs,=mibBuilder.importSymbols('RBTWS-ROOT-MIB','rbtwsMibs')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_W,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC',_E,'MacAddress','PhysAddress','TextualConvention','TimeStamp')
rbtwsClientSessionMib=ModuleIdentity((1,3,6,1,4,1,52,4,15,1,4,4))
if mibBuilder.loadTexts:rbtwsClientSessionMib.setRevisions(('2008-05-23 00:55','2007-11-01 00:54','2007-10-09 00:51','2006-11-16 00:43','2006-10-17 00:42','2006-09-26 00:32','2006-07-29 00:21','2006-06-06 00:10','2006-03-30 00:08'))
class RbtwsEncryptionType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('none',1),('aesCcm',2),('aesOcb',3),('tkip',4),('wep104',5),('wep40',6),('staticWep',7)))
class RbtwsAuthMethod(TextualConvention,Integer32):status=_F;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,14,18,22,26,27,34,255)));namedValues=NamedValues(*(('none',1),('identity',2),('notification',3),('nak',4),('md5',5),('otp',6),('tokenCard',7),('tls',14),('leap',18),('ttls',22),('peap',26),('msChapv2',27),('eapExt',34),('passThru',255)))
class RbtwsSessState(TextualConvention,Integer32):status=_F;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21)));namedValues=NamedValues(*(('invalid',1),('initializing',2),('assocReqAndAuth',3),('assocAndAuth',4),('wired',5),('webLoginPh1',6),('webLoginPh1B',7),('webLoginPh1F',8),('webLoginPh2',9),('webPortalLogin',10),('authorizing',11),('authorized',12),('active',13),('activePortal',14),('deassociated',15),('roamingAway',16),('updatedToRoam',17),('roamedAway',18),('killing',19),('free',20),('enforceSoda',21)))
_RbtwsClientSessionObjects_ObjectIdentity=ObjectIdentity
rbtwsClientSessionObjects=_RbtwsClientSessionObjects_ObjectIdentity((1,3,6,1,4,1,52,4,15,1,4,4,1))
_RbtwsClientSessionDataObjects_ObjectIdentity=ObjectIdentity
rbtwsClientSessionDataObjects=_RbtwsClientSessionDataObjects_ObjectIdentity((1,3,6,1,4,1,52,4,15,1,4,4,1,1))
_RbtwsClSessClientSessionTable_Object=MibTable
rbtwsClSessClientSessionTable=_RbtwsClSessClientSessionTable_Object((1,3,6,1,4,1,52,4,15,1,4,4,1,1,1))
if mibBuilder.loadTexts:rbtwsClSessClientSessionTable.setStatus(_B)
_RbtwsClSessClientSessionEntry_Object=MibTableRow
rbtwsClSessClientSessionEntry=_RbtwsClSessClientSessionEntry_Object((1,3,6,1,4,1,52,4,15,1,4,4,1,1,1,1))
rbtwsClSessClientSessionEntry.setIndexNames((0,_A,_r))
if mibBuilder.loadTexts:rbtwsClSessClientSessionEntry.setStatus(_B)
_RbtwsClSessClientSessMacAddress_Type=MacAddress
_RbtwsClSessClientSessMacAddress_Object=MibTableColumn
rbtwsClSessClientSessMacAddress=_RbtwsClSessClientSessMacAddress_Object((1,3,6,1,4,1,52,4,15,1,4,4,1,1,1,1,1),_RbtwsClSessClientSessMacAddress_Type())
rbtwsClSessClientSessMacAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:rbtwsClSessClientSessMacAddress.setStatus(_B)
class _RbtwsClSessClientSessSessionId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_RbtwsClSessClientSessSessionId_Type.__name__=_E
_RbtwsClSessClientSessSessionId_Object=MibTableColumn
rbtwsClSessClientSessSessionId=_RbtwsClSessClientSessSessionId_Object((1,3,6,1,4,1,52,4,15,1,4,4,1,1,1,1,2),_RbtwsClSessClientSessSessionId_Type())
rbtwsClSessClientSessSessionId.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClSessClientSessSessionId.setStatus(_B)
class _RbtwsClSessClientSessUsername_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_RbtwsClSessClientSessUsername_Type.__name__=_E
_RbtwsClSessClientSessUsername_Object=MibTableColumn
rbtwsClSessClientSessUsername=_RbtwsClSessClientSessUsername_Object((1,3,6,1,4,1,52,4,15,1,4,4,1,1,1,1,3),_RbtwsClSessClientSessUsername_Type())
rbtwsClSessClientSessUsername.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClSessClientSessUsername.setStatus(_B)
_RbtwsClSessClientSessIpAddress_Type=IpAddress
_RbtwsClSessClientSessIpAddress_Object=MibTableColumn
rbtwsClSessClientSessIpAddress=_RbtwsClSessClientSessIpAddress_Object((1,3,6,1,4,1,52,4,15,1,4,4,1,1,1,1,4),_RbtwsClSessClientSessIpAddress_Type())
rbtwsClSessClientSessIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClSessClientSessIpAddress.setStatus(_B)
_RbtwsClSessClientSessEncryptionType_Type=RbtwsEncryptionType
_RbtwsClSessClientSessEncryptionType_Object=MibTableColumn
rbtwsClSessClientSessEncryptionType=_RbtwsClSessClientSessEncryptionType_Object((1,3,6,1,4,1,52,4,15,1,4,4,1,1,1,1,5),_RbtwsClSessClientSessEncryptionType_Type())
rbtwsClSessClientSessEncryptionType.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClSessClientSessEncryptionType.setStatus(_B)
class _RbtwsClSessClientSessVlan_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_RbtwsClSessClientSessVlan_Type.__name__=_E
_RbtwsClSessClientSessVlan_Object=MibTableColumn
rbtwsClSessClientSessVlan=_RbtwsClSessClientSessVlan_Object((1,3,6,1,4,1,52,4,15,1,4,4,1,1,1,1,6),_RbtwsClSessClientSessVlan_Type())
rbtwsClSessClientSessVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClSessClientSessVlan.setStatus(_B)
_RbtwsClSessClientSessApSerialNum_Type=RbtwsApSerialNum
_RbtwsClSessClientSessApSerialNum_Object=MibTableColumn
rbtwsClSessClientSessApSerialNum=_RbtwsClSessClientSessApSerialNum_Object((1,3,6,1,4,1,52,4,15,1,4,4,1,1,1,1,7),_RbtwsClSessClientSessApSerialNum_Type())
rbtwsClSessClientSessApSerialNum.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClSessClientSessApSerialNum.setStatus(_B)
_RbtwsClSessClientSessRadioNum_Type=RbtwsRadioNum
_RbtwsClSessClientSessRadioNum_Object=MibTableColumn
rbtwsClSessClientSessRadioNum=_RbtwsClSessClientSessRadioNum_Object((1,3,6,1,4,1,52,4,15,1,4,4,1,1,1,1,8),_RbtwsClSessClientSessRadioNum_Type())
rbtwsClSessClientSessRadioNum.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClSessClientSessRadioNum.setStatus(_B)
_RbtwsClSessClientSessAccessType_Type=RbtwsAccessType
_RbtwsClSessClientSessAccessType_Object=MibTableColumn
rbtwsClSessClientSessAccessType=_RbtwsClSessClientSessAccessType_Object((1,3,6,1,4,1,52,4,15,1,4,4,1,1,1,1,9),_RbtwsClSessClientSessAccessType_Type())
rbtwsClSessClientSessAccessType.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClSessClientSessAccessType.setStatus(_D)
_RbtwsClSessClientSessAuthMethod_Type=RbtwsAuthMethod
_RbtwsClSessClientSessAuthMethod_Object=MibTableColumn
rbtwsClSessClientSessAuthMethod=_RbtwsClSessClientSessAuthMethod_Object((1,3,6,1,4,1,52,4,15,1,4,4,1,1,1,1,10),_RbtwsClSessClientSessAuthMethod_Type())
rbtwsClSessClientSessAuthMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClSessClientSessAuthMethod.setStatus(_F)
_RbtwsClSessClientSessAuthServer_Type=IpAddress
_RbtwsClSessClientSessAuthServer_Object=MibTableColumn
rbtwsClSessClientSessAuthServer=_RbtwsClSessClientSessAuthServer_Object((1,3,6,1,4,1,52,4,15,1,4,4,1,1,1,1,11),_RbtwsClSessClientSessAuthServer_Type())
rbtwsClSessClientSessAuthServer.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClSessClientSessAuthServer.setStatus(_B)
_RbtwsClSessClientSessPortOrNum_Type=Unsigned32
_RbtwsClSessClientSessPortOrNum_Object=MibTableColumn
rbtwsClSessClientSessPortOrNum=_RbtwsClSessClientSessPortOrNum_Object((1,3,6,1,4,1,52,4,15,1,4,4,1,1,1,1,12),_RbtwsClSessClientSessPortOrNum_Type())
rbtwsClSessClientSessPortOrNum.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClSessClientSessPortOrNum.setStatus(_D)
_RbtwsClSessClientSessVlanTag_Type=Unsigned32
_RbtwsClSessClientSessVlanTag_Object=MibTableColumn
rbtwsClSessClientSessVlanTag=_RbtwsClSessClientSessVlanTag_Object((1,3,6,1,4,1,52,4,15,1,4,4,1,1,1,1,13),_RbtwsClSessClientSessVlanTag_Type())
rbtwsClSessClientSessVlanTag.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClSessClientSessVlanTag.setStatus(_B)
_RbtwsClSessClientSessTimeStamp_Type=TimeStamp
_RbtwsClSessClientSessTimeStamp_Object=MibTableColumn
rbtwsClSessClientSessTimeStamp=_RbtwsClSessClientSessTimeStamp_Object((1,3,6,1,4,1,52,4,15,1,4,4,1,1,1,1,14),_RbtwsClSessClientSessTimeStamp_Type())
rbtwsClSessClientSessTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClSessClientSessTimeStamp.setStatus(_B)
class _RbtwsClSessClientSessSsid_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,33))
_RbtwsClSessClientSessSsid_Type.__name__=_E
_RbtwsClSessClientSessSsid_Object=MibTableColumn
rbtwsClSessClientSessSsid=_RbtwsClSessClientSessSsid_Object((1,3,6,1,4,1,52,4,15,1,4,4,1,1,1,1,15),_RbtwsClSessClientSessSsid_Type())
rbtwsClSessClientSessSsid.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClSessClientSessSsid.setStatus(_B)
_RbtwsClSessClientSessState_Type=RbtwsSessState
_RbtwsClSessClientSessState_Object=MibTableColumn
rbtwsClSessClientSessState=_RbtwsClSessClientSessState_Object((1,3,6,1,4,1,52,4,15,1,4,4,1,1,1,1,16),_RbtwsClSessClientSessState_Type())
rbtwsClSessClientSessState.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClSessClientSessState.setStatus(_F)
_RbtwsClSessClientSessLoginType_Type=RbtwsUserAccessType
_RbtwsClSessClientSessLoginType_Object=MibTableColumn
rbtwsClSessClientSessLoginType=_RbtwsClSessClientSessLoginType_Object((1,3,6,1,4,1,52,4,15,1,4,4,1,1,1,1,17),_RbtwsClSessClientSessLoginType_Type())
rbtwsClSessClientSessLoginType.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClSessClientSessLoginType.setStatus(_B)
_RbtwsClSessClientSessDot1xAuthMethod_Type=RbtwsClientAuthenProtocolType
_RbtwsClSessClientSessDot1xAuthMethod_Object=MibTableColumn
rbtwsClSessClientSessDot1xAuthMethod=_RbtwsClSessClientSessDot1xAuthMethod_Object((1,3,6,1,4,1,52,4,15,1,4,4,1,1,1,1,18),_RbtwsClSessClientSessDot1xAuthMethod_Type())
rbtwsClSessClientSessDot1xAuthMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClSessClientSessDot1xAuthMethod.setStatus(_B)
_RbtwsClSessClientSessSessionState_Type=RbtwsClientSessionState
_RbtwsClSessClientSessSessionState_Object=MibTableColumn
rbtwsClSessClientSessSessionState=_RbtwsClSessClientSessSessionState_Object((1,3,6,1,4,1,52,4,15,1,4,4,1,1,1,1,19),_RbtwsClSessClientSessSessionState_Type())
rbtwsClSessClientSessSessionState.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClSessClientSessSessionState.setStatus(_B)
_RbtwsClSessClientSessAccessMode_Type=RbtwsClientAccessMode
_RbtwsClSessClientSessAccessMode_Object=MibTableColumn
rbtwsClSessClientSessAccessMode=_RbtwsClSessClientSessAccessMode_Object((1,3,6,1,4,1,52,4,15,1,4,4,1,1,1,1,20),_RbtwsClSessClientSessAccessMode_Type())
rbtwsClSessClientSessAccessMode.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClSessClientSessAccessMode.setStatus(_B)
_RbtwsClSessClientSessApNum_Type=RbtwsApNum
_RbtwsClSessClientSessApNum_Object=MibTableColumn
rbtwsClSessClientSessApNum=_RbtwsClSessClientSessApNum_Object((1,3,6,1,4,1,52,4,15,1,4,4,1,1,1,1,21),_RbtwsClSessClientSessApNum_Type())
rbtwsClSessClientSessApNum.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClSessClientSessApNum.setStatus(_B)
class _RbtwsClSessClientSessPhysPortNum_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_RbtwsClSessClientSessPhysPortNum_Type.__name__=_W
_RbtwsClSessClientSessPhysPortNum_Object=MibTableColumn
rbtwsClSessClientSessPhysPortNum=_RbtwsClSessClientSessPhysPortNum_Object((1,3,6,1,4,1,52,4,15,1,4,4,1,1,1,1,22),_RbtwsClSessClientSessPhysPortNum_Type())
rbtwsClSessClientSessPhysPortNum.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClSessClientSessPhysPortNum.setStatus(_B)
_RbtwsClSessRoamingHistoryTable_Object=MibTable
rbtwsClSessRoamingHistoryTable=_RbtwsClSessRoamingHistoryTable_Object((1,3,6,1,4,1,52,4,15,1,4,4,1,1,2))
if mibBuilder.loadTexts:rbtwsClSessRoamingHistoryTable.setStatus(_B)
_RbtwsClSessRoamingHistoryEntry_Object=MibTableRow
rbtwsClSessRoamingHistoryEntry=_RbtwsClSessRoamingHistoryEntry_Object((1,3,6,1,4,1,52,4,15,1,4,4,1,1,2,1))
rbtwsClSessRoamingHistoryEntry.setIndexNames((0,_A,_s),(0,_A,_t))
if mibBuilder.loadTexts:rbtwsClSessRoamingHistoryEntry.setStatus(_B)
_RbtwsClSessRoamHistMacAddress_Type=MacAddress
_RbtwsClSessRoamHistMacAddress_Object=MibTableColumn
rbtwsClSessRoamHistMacAddress=_RbtwsClSessRoamHistMacAddress_Object((1,3,6,1,4,1,52,4,15,1,4,4,1,1,2,1,1),_RbtwsClSessRoamHistMacAddress_Type())
rbtwsClSessRoamHistMacAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:rbtwsClSessRoamHistMacAddress.setStatus(_B)
_RbtwsClSessRoamHistIndex_Type=Unsigned32
_RbtwsClSessRoamHistIndex_Object=MibTableColumn
rbtwsClSessRoamHistIndex=_RbtwsClSessRoamHistIndex_Object((1,3,6,1,4,1,52,4,15,1,4,4,1,1,2,1,2),_RbtwsClSessRoamHistIndex_Type())
rbtwsClSessRoamHistIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:rbtwsClSessRoamHistIndex.setStatus(_B)
_RbtwsClSessRoamHistApSerialNum_Type=RbtwsApSerialNum
_RbtwsClSessRoamHistApSerialNum_Object=MibTableColumn
rbtwsClSessRoamHistApSerialNum=_RbtwsClSessRoamHistApSerialNum_Object((1,3,6,1,4,1,52,4,15,1,4,4,1,1,2,1,3),_RbtwsClSessRoamHistApSerialNum_Type())
rbtwsClSessRoamHistApSerialNum.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClSessRoamHistApSerialNum.setStatus(_B)
_RbtwsClSessRoamHistRadioNum_Type=RbtwsRadioNum
_RbtwsClSessRoamHistRadioNum_Object=MibTableColumn
rbtwsClSessRoamHistRadioNum=_RbtwsClSessRoamHistRadioNum_Object((1,3,6,1,4,1,52,4,15,1,4,4,1,1,2,1,4),_RbtwsClSessRoamHistRadioNum_Type())
rbtwsClSessRoamHistRadioNum.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClSessRoamHistRadioNum.setStatus(_B)
_RbtwsClSessRoamHistAccessType_Type=RbtwsAccessType
_RbtwsClSessRoamHistAccessType_Object=MibTableColumn
rbtwsClSessRoamHistAccessType=_RbtwsClSessRoamHistAccessType_Object((1,3,6,1,4,1,52,4,15,1,4,4,1,1,2,1,5),_RbtwsClSessRoamHistAccessType_Type())
rbtwsClSessRoamHistAccessType.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClSessRoamHistAccessType.setStatus(_D)
_RbtwsClSessRoamHistApNumOrPort_Type=Unsigned32
_RbtwsClSessRoamHistApNumOrPort_Object=MibTableColumn
rbtwsClSessRoamHistApNumOrPort=_RbtwsClSessRoamHistApNumOrPort_Object((1,3,6,1,4,1,52,4,15,1,4,4,1,1,2,1,6),_RbtwsClSessRoamHistApNumOrPort_Type())
rbtwsClSessRoamHistApNumOrPort.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClSessRoamHistApNumOrPort.setStatus(_D)
_RbtwsClSessRoamHistIpAddress_Type=IpAddress
_RbtwsClSessRoamHistIpAddress_Object=MibTableColumn
rbtwsClSessRoamHistIpAddress=_RbtwsClSessRoamHistIpAddress_Object((1,3,6,1,4,1,52,4,15,1,4,4,1,1,2,1,7),_RbtwsClSessRoamHistIpAddress_Type())
rbtwsClSessRoamHistIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClSessRoamHistIpAddress.setStatus(_B)
_RbtwsClSessRoamHistTimeStamp_Type=TimeStamp
_RbtwsClSessRoamHistTimeStamp_Object=MibTableColumn
rbtwsClSessRoamHistTimeStamp=_RbtwsClSessRoamHistTimeStamp_Object((1,3,6,1,4,1,52,4,15,1,4,4,1,1,2,1,8),_RbtwsClSessRoamHistTimeStamp_Type())
rbtwsClSessRoamHistTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClSessRoamHistTimeStamp.setStatus(_B)
_RbtwsClSessRoamHistAccessMode_Type=RbtwsClientAccessMode
_RbtwsClSessRoamHistAccessMode_Object=MibTableColumn
rbtwsClSessRoamHistAccessMode=_RbtwsClSessRoamHistAccessMode_Object((1,3,6,1,4,1,52,4,15,1,4,4,1,1,2,1,9),_RbtwsClSessRoamHistAccessMode_Type())
rbtwsClSessRoamHistAccessMode.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClSessRoamHistAccessMode.setStatus(_B)
_RbtwsClSessRoamHistApNum_Type=RbtwsApNum
_RbtwsClSessRoamHistApNum_Object=MibTableColumn
rbtwsClSessRoamHistApNum=_RbtwsClSessRoamHistApNum_Object((1,3,6,1,4,1,52,4,15,1,4,4,1,1,2,1,10),_RbtwsClSessRoamHistApNum_Type())
rbtwsClSessRoamHistApNum.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClSessRoamHistApNum.setStatus(_B)
class _RbtwsClSessRoamHistPhysPortNum_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_RbtwsClSessRoamHistPhysPortNum_Type.__name__=_W
_RbtwsClSessRoamHistPhysPortNum_Object=MibTableColumn
rbtwsClSessRoamHistPhysPortNum=_RbtwsClSessRoamHistPhysPortNum_Object((1,3,6,1,4,1,52,4,15,1,4,4,1,1,2,1,11),_RbtwsClSessRoamHistPhysPortNum_Type())
rbtwsClSessRoamHistPhysPortNum.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClSessRoamHistPhysPortNum.setStatus(_B)
_RbtwsClSessClientSessionStatisticsTable_Object=MibTable
rbtwsClSessClientSessionStatisticsTable=_RbtwsClSessClientSessionStatisticsTable_Object((1,3,6,1,4,1,52,4,15,1,4,4,1,1,3))
if mibBuilder.loadTexts:rbtwsClSessClientSessionStatisticsTable.setStatus(_B)
_RbtwsClSessClientSessionStatisticsEntry_Object=MibTableRow
rbtwsClSessClientSessionStatisticsEntry=_RbtwsClSessClientSessionStatisticsEntry_Object((1,3,6,1,4,1,52,4,15,1,4,4,1,1,3,1))
rbtwsClSessClientSessionStatisticsEntry.setIndexNames((0,_A,_u))
if mibBuilder.loadTexts:rbtwsClSessClientSessionStatisticsEntry.setStatus(_B)
_RbtwsClSessClientSessStatsMacAddress_Type=MacAddress
_RbtwsClSessClientSessStatsMacAddress_Object=MibTableColumn
rbtwsClSessClientSessStatsMacAddress=_RbtwsClSessClientSessStatsMacAddress_Object((1,3,6,1,4,1,52,4,15,1,4,4,1,1,3,1,1),_RbtwsClSessClientSessStatsMacAddress_Type())
rbtwsClSessClientSessStatsMacAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:rbtwsClSessClientSessStatsMacAddress.setStatus(_B)
_RbtwsClSessClientSessStatsUniPktIn_Type=Counter64
_RbtwsClSessClientSessStatsUniPktIn_Object=MibTableColumn
rbtwsClSessClientSessStatsUniPktIn=_RbtwsClSessClientSessStatsUniPktIn_Object((1,3,6,1,4,1,52,4,15,1,4,4,1,1,3,1,2),_RbtwsClSessClientSessStatsUniPktIn_Type())
rbtwsClSessClientSessStatsUniPktIn.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClSessClientSessStatsUniPktIn.setStatus(_B)
_RbtwsClSessClientSessStatsUniOctetIn_Type=Counter64
_RbtwsClSessClientSessStatsUniOctetIn_Object=MibTableColumn
rbtwsClSessClientSessStatsUniOctetIn=_RbtwsClSessClientSessStatsUniOctetIn_Object((1,3,6,1,4,1,52,4,15,1,4,4,1,1,3,1,3),_RbtwsClSessClientSessStatsUniOctetIn_Type())
rbtwsClSessClientSessStatsUniOctetIn.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClSessClientSessStatsUniOctetIn.setStatus(_B)
_RbtwsClSessClientSessStatsUniPktOut_Type=Counter64
_RbtwsClSessClientSessStatsUniPktOut_Object=MibTableColumn
rbtwsClSessClientSessStatsUniPktOut=_RbtwsClSessClientSessStatsUniPktOut_Object((1,3,6,1,4,1,52,4,15,1,4,4,1,1,3,1,4),_RbtwsClSessClientSessStatsUniPktOut_Type())
rbtwsClSessClientSessStatsUniPktOut.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClSessClientSessStatsUniPktOut.setStatus(_B)
_RbtwsClSessClientSessStatsUniOctetOut_Type=Counter64
_RbtwsClSessClientSessStatsUniOctetOut_Object=MibTableColumn
rbtwsClSessClientSessStatsUniOctetOut=_RbtwsClSessClientSessStatsUniOctetOut_Object((1,3,6,1,4,1,52,4,15,1,4,4,1,1,3,1,5),_RbtwsClSessClientSessStatsUniOctetOut_Type())
rbtwsClSessClientSessStatsUniOctetOut.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClSessClientSessStatsUniOctetOut.setStatus(_B)
_RbtwsClSessClientSessStatsMultiPktIn_Type=Counter64
_RbtwsClSessClientSessStatsMultiPktIn_Object=MibTableColumn
rbtwsClSessClientSessStatsMultiPktIn=_RbtwsClSessClientSessStatsMultiPktIn_Object((1,3,6,1,4,1,52,4,15,1,4,4,1,1,3,1,6),_RbtwsClSessClientSessStatsMultiPktIn_Type())
rbtwsClSessClientSessStatsMultiPktIn.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClSessClientSessStatsMultiPktIn.setStatus(_B)
_RbtwsClSessClientSessStatsMultiOctetIn_Type=Counter64
_RbtwsClSessClientSessStatsMultiOctetIn_Object=MibTableColumn
rbtwsClSessClientSessStatsMultiOctetIn=_RbtwsClSessClientSessStatsMultiOctetIn_Object((1,3,6,1,4,1,52,4,15,1,4,4,1,1,3,1,7),_RbtwsClSessClientSessStatsMultiOctetIn_Type())
rbtwsClSessClientSessStatsMultiOctetIn.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClSessClientSessStatsMultiOctetIn.setStatus(_B)
_RbtwsClSessClientSessStatsEncErrPkt_Type=Counter64
_RbtwsClSessClientSessStatsEncErrPkt_Object=MibTableColumn
rbtwsClSessClientSessStatsEncErrPkt=_RbtwsClSessClientSessStatsEncErrPkt_Object((1,3,6,1,4,1,52,4,15,1,4,4,1,1,3,1,8),_RbtwsClSessClientSessStatsEncErrPkt_Type())
rbtwsClSessClientSessStatsEncErrPkt.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClSessClientSessStatsEncErrPkt.setStatus(_B)
_RbtwsClSessClientSessStatsEncErrOctet_Type=Counter64
_RbtwsClSessClientSessStatsEncErrOctet_Object=MibTableColumn
rbtwsClSessClientSessStatsEncErrOctet=_RbtwsClSessClientSessStatsEncErrOctet_Object((1,3,6,1,4,1,52,4,15,1,4,4,1,1,3,1,9),_RbtwsClSessClientSessStatsEncErrOctet_Type())
rbtwsClSessClientSessStatsEncErrOctet.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClSessClientSessStatsEncErrOctet.setStatus(_B)
_RbtwsClSessClientSessStatsLastRate_Type=RbtwsRadioRate
_RbtwsClSessClientSessStatsLastRate_Object=MibTableColumn
rbtwsClSessClientSessStatsLastRate=_RbtwsClSessClientSessStatsLastRate_Object((1,3,6,1,4,1,52,4,15,1,4,4,1,1,3,1,10),_RbtwsClSessClientSessStatsLastRate_Type())
rbtwsClSessClientSessStatsLastRate.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClSessClientSessStatsLastRate.setStatus(_B)
_RbtwsClSessClientSessStatsLastRssi_Type=RbtwsRssi
_RbtwsClSessClientSessStatsLastRssi_Object=MibTableColumn
rbtwsClSessClientSessStatsLastRssi=_RbtwsClSessClientSessStatsLastRssi_Object((1,3,6,1,4,1,52,4,15,1,4,4,1,1,3,1,11),_RbtwsClSessClientSessStatsLastRssi_Type())
rbtwsClSessClientSessStatsLastRssi.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClSessClientSessStatsLastRssi.setStatus(_B)
_RbtwsClSessClientSessStatsLastSNR_Type=Integer32
_RbtwsClSessClientSessStatsLastSNR_Object=MibTableColumn
rbtwsClSessClientSessStatsLastSNR=_RbtwsClSessClientSessStatsLastSNR_Object((1,3,6,1,4,1,52,4,15,1,4,4,1,1,3,1,12),_RbtwsClSessClientSessStatsLastSNR_Type())
rbtwsClSessClientSessStatsLastSNR.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClSessClientSessStatsLastSNR.setStatus(_B)
_RbtwsClSessTotalSessions_Type=Unsigned32
_RbtwsClSessTotalSessions_Object=MibScalar
rbtwsClSessTotalSessions=_RbtwsClSessTotalSessions_Object((1,3,6,1,4,1,52,4,15,1,4,4,1,1,4),_RbtwsClSessTotalSessions_Type())
rbtwsClSessTotalSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClSessTotalSessions.setStatus(_B)
_RbtwsClientSessionConformance_ObjectIdentity=ObjectIdentity
rbtwsClientSessionConformance=_RbtwsClientSessionConformance_ObjectIdentity((1,3,6,1,4,1,52,4,15,1,4,4,1,2))
_RbtwsClientSessionCompliances_ObjectIdentity=ObjectIdentity
rbtwsClientSessionCompliances=_RbtwsClientSessionCompliances_ObjectIdentity((1,3,6,1,4,1,52,4,15,1,4,4,1,2,1))
_RbtwsClientSessionGroups_ObjectIdentity=ObjectIdentity
rbtwsClientSessionGroups=_RbtwsClientSessionGroups_ObjectIdentity((1,3,6,1,4,1,52,4,15,1,4,4,1,2,2))
rbtwsClientSessionCommonGroup=ObjectGroup((1,3,6,1,4,1,52,4,15,1,4,4,1,2,2,1))
rbtwsClientSessionCommonGroup.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_X),(_A,_v),(_A,_O),(_A,_Y),(_A,_P),(_A,_Q),(_A,_R),(_A,_w),(_A,_S),(_A,_T),(_A,_Z),(_A,_a),(_A,_U),(_A,_V),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l)))
if mibBuilder.loadTexts:rbtwsClientSessionCommonGroup.setStatus(_D)
rbtwsClientSessScalarsGroup=ObjectGroup((1,3,6,1,4,1,52,4,15,1,4,4,1,2,2,2))
rbtwsClientSessScalarsGroup.setObjects((_A,_x))
if mibBuilder.loadTexts:rbtwsClientSessScalarsGroup.setStatus(_B)
rbtwsClientSessClientSessionTableGroup=ObjectGroup((1,3,6,1,4,1,52,4,15,1,4,4,1,2,2,3))
rbtwsClientSessClientSessionTableGroup.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_X),(_A,_O),(_A,_Y),(_A,_P),(_A,_Q),(_A,_R),(_A,_m),(_A,_n),(_A,_o)))
if mibBuilder.loadTexts:rbtwsClientSessClientSessionTableGroup.setStatus(_D)
rbtwsClientSessRoamingHistoryTableGroup=ObjectGroup((1,3,6,1,4,1,52,4,15,1,4,4,1,2,2,4))
rbtwsClientSessRoamingHistoryTableGroup.setObjects(*((_A,_S),(_A,_T),(_A,_Z),(_A,_a),(_A,_U),(_A,_V)))
if mibBuilder.loadTexts:rbtwsClientSessRoamingHistoryTableGroup.setStatus(_D)
rbtwsClientSessClientSessionStatisticsTableGroup=ObjectGroup((1,3,6,1,4,1,52,4,15,1,4,4,1,2,2,5))
rbtwsClientSessClientSessionStatisticsTableGroup.setObjects(*((_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l)))
if mibBuilder.loadTexts:rbtwsClientSessClientSessionStatisticsTableGroup.setStatus(_B)
rbtwsClientSessClientSessionTableGroupRev2=ObjectGroup((1,3,6,1,4,1,52,4,15,1,4,4,1,2,2,6))
rbtwsClientSessClientSessionTableGroupRev2.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_m),(_A,_n),(_A,_o),(_A,_y),(_A,_z),(_A,_A0)))
if mibBuilder.loadTexts:rbtwsClientSessClientSessionTableGroupRev2.setStatus(_B)
rbtwsClientSessRoamingHistoryTableGroupRev2=ObjectGroup((1,3,6,1,4,1,52,4,15,1,4,4,1,2,2,7))
rbtwsClientSessRoamingHistoryTableGroupRev2.setObjects(*((_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_A1),(_A,_A2),(_A,_A3)))
if mibBuilder.loadTexts:rbtwsClientSessRoamingHistoryTableGroupRev2.setStatus(_B)
rbtwsClientSessionCompliance=ModuleCompliance((1,3,6,1,4,1,52,4,15,1,4,4,1,2,1,1))
rbtwsClientSessionCompliance.setObjects((_A,_A4))
if mibBuilder.loadTexts:rbtwsClientSessionCompliance.setStatus(_D)
rbtwsClientSessionComplianceRev2=ModuleCompliance((1,3,6,1,4,1,52,4,15,1,4,4,1,2,1,2))
rbtwsClientSessionComplianceRev2.setObjects(*((_A,_p),(_A,_A5),(_A,_A6),(_A,_q)))
if mibBuilder.loadTexts:rbtwsClientSessionComplianceRev2.setStatus(_D)
rbtwsClientSessionComplianceRev3=ModuleCompliance((1,3,6,1,4,1,52,4,15,1,4,4,1,2,1,3))
rbtwsClientSessionComplianceRev3.setObjects(*((_A,_p),(_A,_A7),(_A,_A8),(_A,_q)))
if mibBuilder.loadTexts:rbtwsClientSessionComplianceRev3.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'RbtwsEncryptionType':RbtwsEncryptionType,'RbtwsAuthMethod':RbtwsAuthMethod,'RbtwsSessState':RbtwsSessState,'rbtwsClientSessionMib':rbtwsClientSessionMib,'rbtwsClientSessionObjects':rbtwsClientSessionObjects,'rbtwsClientSessionDataObjects':rbtwsClientSessionDataObjects,'rbtwsClSessClientSessionTable':rbtwsClSessClientSessionTable,'rbtwsClSessClientSessionEntry':rbtwsClSessClientSessionEntry,_r:rbtwsClSessClientSessMacAddress,_H:rbtwsClSessClientSessSessionId,_I:rbtwsClSessClientSessUsername,_J:rbtwsClSessClientSessIpAddress,_K:rbtwsClSessClientSessEncryptionType,_L:rbtwsClSessClientSessVlan,_M:rbtwsClSessClientSessApSerialNum,_N:rbtwsClSessClientSessRadioNum,_X:rbtwsClSessClientSessAccessType,_v:rbtwsClSessClientSessAuthMethod,_O:rbtwsClSessClientSessAuthServer,_Y:rbtwsClSessClientSessPortOrNum,_P:rbtwsClSessClientSessVlanTag,_Q:rbtwsClSessClientSessTimeStamp,_R:rbtwsClSessClientSessSsid,_w:rbtwsClSessClientSessState,_m:rbtwsClSessClientSessLoginType,_n:rbtwsClSessClientSessDot1xAuthMethod,_o:rbtwsClSessClientSessSessionState,_y:rbtwsClSessClientSessAccessMode,_z:rbtwsClSessClientSessApNum,_A0:rbtwsClSessClientSessPhysPortNum,'rbtwsClSessRoamingHistoryTable':rbtwsClSessRoamingHistoryTable,'rbtwsClSessRoamingHistoryEntry':rbtwsClSessRoamingHistoryEntry,_s:rbtwsClSessRoamHistMacAddress,_t:rbtwsClSessRoamHistIndex,_S:rbtwsClSessRoamHistApSerialNum,_T:rbtwsClSessRoamHistRadioNum,_Z:rbtwsClSessRoamHistAccessType,_a:rbtwsClSessRoamHistApNumOrPort,_U:rbtwsClSessRoamHistIpAddress,_V:rbtwsClSessRoamHistTimeStamp,_A1:rbtwsClSessRoamHistAccessMode,_A2:rbtwsClSessRoamHistApNum,_A3:rbtwsClSessRoamHistPhysPortNum,'rbtwsClSessClientSessionStatisticsTable':rbtwsClSessClientSessionStatisticsTable,'rbtwsClSessClientSessionStatisticsEntry':rbtwsClSessClientSessionStatisticsEntry,_u:rbtwsClSessClientSessStatsMacAddress,_b:rbtwsClSessClientSessStatsUniPktIn,_c:rbtwsClSessClientSessStatsUniOctetIn,_d:rbtwsClSessClientSessStatsUniPktOut,_e:rbtwsClSessClientSessStatsUniOctetOut,_f:rbtwsClSessClientSessStatsMultiPktIn,_g:rbtwsClSessClientSessStatsMultiOctetIn,_h:rbtwsClSessClientSessStatsEncErrPkt,_i:rbtwsClSessClientSessStatsEncErrOctet,_j:rbtwsClSessClientSessStatsLastRate,_k:rbtwsClSessClientSessStatsLastRssi,_l:rbtwsClSessClientSessStatsLastSNR,_x:rbtwsClSessTotalSessions,'rbtwsClientSessionConformance':rbtwsClientSessionConformance,'rbtwsClientSessionCompliances':rbtwsClientSessionCompliances,'rbtwsClientSessionCompliance':rbtwsClientSessionCompliance,'rbtwsClientSessionComplianceRev2':rbtwsClientSessionComplianceRev2,'rbtwsClientSessionComplianceRev3':rbtwsClientSessionComplianceRev3,'rbtwsClientSessionGroups':rbtwsClientSessionGroups,_A4:rbtwsClientSessionCommonGroup,_p:rbtwsClientSessScalarsGroup,_A5:rbtwsClientSessClientSessionTableGroup,_A6:rbtwsClientSessRoamingHistoryTableGroup,_q:rbtwsClientSessClientSessionStatisticsTableGroup,_A7:rbtwsClientSessClientSessionTableGroupRev2,_A8:rbtwsClientSessRoamingHistoryTableGroupRev2})