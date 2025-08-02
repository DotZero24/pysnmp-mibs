_A7='ntwsClientSessRoamingHistoryTableGroupRev2'
_A6='ntwsClientSessClientSessionTableGroupRev2'
_A5='ntwsClientSessRoamingHistoryTableGroup'
_A4='ntwsClientSessClientSessionTableGroup'
_A3='ntwsClientSessionCommonGroup'
_A2='ntwsClSessRoamHistPhysPortNum'
_A1='ntwsClSessRoamHistApNum'
_A0='ntwsClSessRoamHistAccessMode'
_z='ntwsClSessClientSessPhysPortNum'
_y='ntwsClSessClientSessApNum'
_x='ntwsClSessClientSessAccessMode'
_w='ntwsClSessTotalSessions'
_v='ntwsClSessClientSessState'
_u='ntwsClSessClientSessAuthMethod'
_t='ntwsClSessClientSessStatsMacAddress'
_s='ntwsClSessRoamHistIndex'
_r='ntwsClSessRoamHistMacAddress'
_q='ntwsClSessClientSessMacAddress'
_p='ntwsClientSessClientSessionStatisticsTableGroup'
_o='ntwsClientSessScalarsGroup'
_n='ntwsClSessClientSessSessionState'
_m='ntwsClSessClientSessDot1xAuthMethod'
_l='ntwsClSessClientSessLoginType'
_k='ntwsClSessClientSessStatsLastSNR'
_j='ntwsClSessClientSessStatsLastRssi'
_i='ntwsClSessClientSessStatsLastRate'
_h='ntwsClSessClientSessStatsEncErrOctet'
_g='ntwsClSessClientSessStatsEncErrPkt'
_f='ntwsClSessClientSessStatsMultiOctetIn'
_e='ntwsClSessClientSessStatsMultiPktIn'
_d='ntwsClSessClientSessStatsUniOctetOut'
_c='ntwsClSessClientSessStatsUniPktOut'
_b='ntwsClSessClientSessStatsUniOctetIn'
_a='ntwsClSessClientSessStatsUniPktIn'
_Z='ntwsClSessRoamHistApNumOrPort'
_Y='ntwsClSessRoamHistAccessType'
_X='ntwsClSessClientSessPortOrNum'
_W='ntwsClSessClientSessAccessType'
_V='ntwsClSessRoamHistTimeStamp'
_U='ntwsClSessRoamHistIpAddress'
_T='ntwsClSessRoamHistRadioNum'
_S='ntwsClSessRoamHistApSerialNum'
_R='ntwsClSessClientSessSsid'
_Q='ntwsClSessClientSessTimeStamp'
_P='ntwsClSessClientSessVlanTag'
_O='ntwsClSessClientSessAuthServer'
_N='ntwsClSessClientSessRadioNum'
_M='ntwsClSessClientSessApSerialNum'
_L='ntwsClSessClientSessVlan'
_K='ntwsClSessClientSessEncryptionType'
_J='ntwsClSessClientSessIpAddress'
_I='ntwsClSessClientSessUsername'
_H='ntwsClSessClientSessSessionId'
_G='not-accessible'
_F='deprecated'
_E='DisplayString'
_D='obsolete'
_C='read-only'
_B='current'
_A='NTWS-CLIENT-SESSION-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
NtwsAccessType,NtwsApNum,NtwsApSerialNum,NtwsRadioNum,NtwsRadioRate,NtwsRssi=mibBuilder.importSymbols('NTWS-AP-TC','NtwsAccessType','NtwsApNum','NtwsApSerialNum','NtwsRadioNum','NtwsRadioRate','NtwsRssi')
NtwsPhysPortNumberOrZero,=mibBuilder.importSymbols('NTWS-BASIC-TC','NtwsPhysPortNumberOrZero')
NtwsClientAccessMode,NtwsClientAuthenProtocolType,NtwsClientSessionState,NtwsUserAccessType=mibBuilder.importSymbols('NTWS-CLIENT-SESSION-TC','NtwsClientAccessMode','NtwsClientAuthenProtocolType','NtwsClientSessionState','NtwsUserAccessType')
ntwsMibs,=mibBuilder.importSymbols('NTWS-ROOT-MIB','ntwsMibs')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC',_E,'MacAddress','PhysAddress','TextualConvention','TimeStamp')
ntwsClientSessionMib=ModuleIdentity((1,3,6,1,4,1,45,6,1,4,4))
if mibBuilder.loadTexts:ntwsClientSessionMib.setRevisions(('2008-10-23 00:56','2008-05-23 00:55','2007-11-01 00:54','2007-10-09 00:51','2007-08-16 00:44','2006-11-16 00:43','2006-10-17 00:42','2006-09-26 00:32','2006-07-29 00:21','2006-06-06 00:10','2006-03-30 00:08'))
class NtwsEncryptionType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('none',1),('aesCcm',2),('aesOcb',3),('tkip',4),('wep104',5),('wep40',6),('staticWep',7)))
class NtwsAuthMethod(TextualConvention,Integer32):status=_F;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,14,18,22,26,27,34,255)));namedValues=NamedValues(*(('none',1),('identity',2),('notification',3),('nak',4),('md5',5),('otp',6),('tokenCard',7),('tls',14),('leap',18),('ttls',22),('peap',26),('msChapv2',27),('eapExt',34),('passThru',255)))
class NtwsSessState(TextualConvention,Integer32):status=_F;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21)));namedValues=NamedValues(*(('invalid',1),('initializing',2),('assocReqAndAuth',3),('assocAndAuth',4),('wired',5),('webLoginPh1',6),('webLoginPh1B',7),('webLoginPh1F',8),('webLoginPh2',9),('webPortalLogin',10),('authorizing',11),('authorized',12),('active',13),('activePortal',14),('deassociated',15),('roamingAway',16),('updatedToRoam',17),('roamedAway',18),('killing',19),('free',20),('enforceSoda',21)))
_NtwsClientSessionObjects_ObjectIdentity=ObjectIdentity
ntwsClientSessionObjects=_NtwsClientSessionObjects_ObjectIdentity((1,3,6,1,4,1,45,6,1,4,4,1))
_NtwsClientSessionDataObjects_ObjectIdentity=ObjectIdentity
ntwsClientSessionDataObjects=_NtwsClientSessionDataObjects_ObjectIdentity((1,3,6,1,4,1,45,6,1,4,4,1,1))
_NtwsClSessClientSessionTable_Object=MibTable
ntwsClSessClientSessionTable=_NtwsClSessClientSessionTable_Object((1,3,6,1,4,1,45,6,1,4,4,1,1,1))
if mibBuilder.loadTexts:ntwsClSessClientSessionTable.setStatus(_B)
_NtwsClSessClientSessionEntry_Object=MibTableRow
ntwsClSessClientSessionEntry=_NtwsClSessClientSessionEntry_Object((1,3,6,1,4,1,45,6,1,4,4,1,1,1,1))
ntwsClSessClientSessionEntry.setIndexNames((0,_A,_q))
if mibBuilder.loadTexts:ntwsClSessClientSessionEntry.setStatus(_B)
_NtwsClSessClientSessMacAddress_Type=MacAddress
_NtwsClSessClientSessMacAddress_Object=MibTableColumn
ntwsClSessClientSessMacAddress=_NtwsClSessClientSessMacAddress_Object((1,3,6,1,4,1,45,6,1,4,4,1,1,1,1,1),_NtwsClSessClientSessMacAddress_Type())
ntwsClSessClientSessMacAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:ntwsClSessClientSessMacAddress.setStatus(_B)
class _NtwsClSessClientSessSessionId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_NtwsClSessClientSessSessionId_Type.__name__=_E
_NtwsClSessClientSessSessionId_Object=MibTableColumn
ntwsClSessClientSessSessionId=_NtwsClSessClientSessSessionId_Object((1,3,6,1,4,1,45,6,1,4,4,1,1,1,1,2),_NtwsClSessClientSessSessionId_Type())
ntwsClSessClientSessSessionId.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClSessClientSessSessionId.setStatus(_B)
class _NtwsClSessClientSessUsername_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_NtwsClSessClientSessUsername_Type.__name__=_E
_NtwsClSessClientSessUsername_Object=MibTableColumn
ntwsClSessClientSessUsername=_NtwsClSessClientSessUsername_Object((1,3,6,1,4,1,45,6,1,4,4,1,1,1,1,3),_NtwsClSessClientSessUsername_Type())
ntwsClSessClientSessUsername.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClSessClientSessUsername.setStatus(_B)
_NtwsClSessClientSessIpAddress_Type=IpAddress
_NtwsClSessClientSessIpAddress_Object=MibTableColumn
ntwsClSessClientSessIpAddress=_NtwsClSessClientSessIpAddress_Object((1,3,6,1,4,1,45,6,1,4,4,1,1,1,1,4),_NtwsClSessClientSessIpAddress_Type())
ntwsClSessClientSessIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClSessClientSessIpAddress.setStatus(_B)
_NtwsClSessClientSessEncryptionType_Type=NtwsEncryptionType
_NtwsClSessClientSessEncryptionType_Object=MibTableColumn
ntwsClSessClientSessEncryptionType=_NtwsClSessClientSessEncryptionType_Object((1,3,6,1,4,1,45,6,1,4,4,1,1,1,1,5),_NtwsClSessClientSessEncryptionType_Type())
ntwsClSessClientSessEncryptionType.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClSessClientSessEncryptionType.setStatus(_B)
class _NtwsClSessClientSessVlan_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_NtwsClSessClientSessVlan_Type.__name__=_E
_NtwsClSessClientSessVlan_Object=MibTableColumn
ntwsClSessClientSessVlan=_NtwsClSessClientSessVlan_Object((1,3,6,1,4,1,45,6,1,4,4,1,1,1,1,6),_NtwsClSessClientSessVlan_Type())
ntwsClSessClientSessVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClSessClientSessVlan.setStatus(_B)
_NtwsClSessClientSessApSerialNum_Type=NtwsApSerialNum
_NtwsClSessClientSessApSerialNum_Object=MibTableColumn
ntwsClSessClientSessApSerialNum=_NtwsClSessClientSessApSerialNum_Object((1,3,6,1,4,1,45,6,1,4,4,1,1,1,1,7),_NtwsClSessClientSessApSerialNum_Type())
ntwsClSessClientSessApSerialNum.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClSessClientSessApSerialNum.setStatus(_B)
_NtwsClSessClientSessRadioNum_Type=NtwsRadioNum
_NtwsClSessClientSessRadioNum_Object=MibTableColumn
ntwsClSessClientSessRadioNum=_NtwsClSessClientSessRadioNum_Object((1,3,6,1,4,1,45,6,1,4,4,1,1,1,1,8),_NtwsClSessClientSessRadioNum_Type())
ntwsClSessClientSessRadioNum.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClSessClientSessRadioNum.setStatus(_B)
_NtwsClSessClientSessAccessType_Type=NtwsAccessType
_NtwsClSessClientSessAccessType_Object=MibTableColumn
ntwsClSessClientSessAccessType=_NtwsClSessClientSessAccessType_Object((1,3,6,1,4,1,45,6,1,4,4,1,1,1,1,9),_NtwsClSessClientSessAccessType_Type())
ntwsClSessClientSessAccessType.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClSessClientSessAccessType.setStatus(_D)
_NtwsClSessClientSessAuthMethod_Type=NtwsAuthMethod
_NtwsClSessClientSessAuthMethod_Object=MibTableColumn
ntwsClSessClientSessAuthMethod=_NtwsClSessClientSessAuthMethod_Object((1,3,6,1,4,1,45,6,1,4,4,1,1,1,1,10),_NtwsClSessClientSessAuthMethod_Type())
ntwsClSessClientSessAuthMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClSessClientSessAuthMethod.setStatus(_F)
_NtwsClSessClientSessAuthServer_Type=IpAddress
_NtwsClSessClientSessAuthServer_Object=MibTableColumn
ntwsClSessClientSessAuthServer=_NtwsClSessClientSessAuthServer_Object((1,3,6,1,4,1,45,6,1,4,4,1,1,1,1,11),_NtwsClSessClientSessAuthServer_Type())
ntwsClSessClientSessAuthServer.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClSessClientSessAuthServer.setStatus(_B)
_NtwsClSessClientSessPortOrNum_Type=Unsigned32
_NtwsClSessClientSessPortOrNum_Object=MibTableColumn
ntwsClSessClientSessPortOrNum=_NtwsClSessClientSessPortOrNum_Object((1,3,6,1,4,1,45,6,1,4,4,1,1,1,1,12),_NtwsClSessClientSessPortOrNum_Type())
ntwsClSessClientSessPortOrNum.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClSessClientSessPortOrNum.setStatus(_D)
_NtwsClSessClientSessVlanTag_Type=Unsigned32
_NtwsClSessClientSessVlanTag_Object=MibTableColumn
ntwsClSessClientSessVlanTag=_NtwsClSessClientSessVlanTag_Object((1,3,6,1,4,1,45,6,1,4,4,1,1,1,1,13),_NtwsClSessClientSessVlanTag_Type())
ntwsClSessClientSessVlanTag.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClSessClientSessVlanTag.setStatus(_B)
_NtwsClSessClientSessTimeStamp_Type=TimeStamp
_NtwsClSessClientSessTimeStamp_Object=MibTableColumn
ntwsClSessClientSessTimeStamp=_NtwsClSessClientSessTimeStamp_Object((1,3,6,1,4,1,45,6,1,4,4,1,1,1,1,14),_NtwsClSessClientSessTimeStamp_Type())
ntwsClSessClientSessTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClSessClientSessTimeStamp.setStatus(_B)
class _NtwsClSessClientSessSsid_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,33))
_NtwsClSessClientSessSsid_Type.__name__=_E
_NtwsClSessClientSessSsid_Object=MibTableColumn
ntwsClSessClientSessSsid=_NtwsClSessClientSessSsid_Object((1,3,6,1,4,1,45,6,1,4,4,1,1,1,1,15),_NtwsClSessClientSessSsid_Type())
ntwsClSessClientSessSsid.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClSessClientSessSsid.setStatus(_B)
_NtwsClSessClientSessState_Type=NtwsSessState
_NtwsClSessClientSessState_Object=MibTableColumn
ntwsClSessClientSessState=_NtwsClSessClientSessState_Object((1,3,6,1,4,1,45,6,1,4,4,1,1,1,1,16),_NtwsClSessClientSessState_Type())
ntwsClSessClientSessState.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClSessClientSessState.setStatus(_F)
_NtwsClSessClientSessLoginType_Type=NtwsUserAccessType
_NtwsClSessClientSessLoginType_Object=MibTableColumn
ntwsClSessClientSessLoginType=_NtwsClSessClientSessLoginType_Object((1,3,6,1,4,1,45,6,1,4,4,1,1,1,1,17),_NtwsClSessClientSessLoginType_Type())
ntwsClSessClientSessLoginType.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClSessClientSessLoginType.setStatus(_B)
_NtwsClSessClientSessDot1xAuthMethod_Type=NtwsClientAuthenProtocolType
_NtwsClSessClientSessDot1xAuthMethod_Object=MibTableColumn
ntwsClSessClientSessDot1xAuthMethod=_NtwsClSessClientSessDot1xAuthMethod_Object((1,3,6,1,4,1,45,6,1,4,4,1,1,1,1,18),_NtwsClSessClientSessDot1xAuthMethod_Type())
ntwsClSessClientSessDot1xAuthMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClSessClientSessDot1xAuthMethod.setStatus(_B)
_NtwsClSessClientSessSessionState_Type=NtwsClientSessionState
_NtwsClSessClientSessSessionState_Object=MibTableColumn
ntwsClSessClientSessSessionState=_NtwsClSessClientSessSessionState_Object((1,3,6,1,4,1,45,6,1,4,4,1,1,1,1,19),_NtwsClSessClientSessSessionState_Type())
ntwsClSessClientSessSessionState.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClSessClientSessSessionState.setStatus(_B)
_NtwsClSessClientSessAccessMode_Type=NtwsClientAccessMode
_NtwsClSessClientSessAccessMode_Object=MibTableColumn
ntwsClSessClientSessAccessMode=_NtwsClSessClientSessAccessMode_Object((1,3,6,1,4,1,45,6,1,4,4,1,1,1,1,20),_NtwsClSessClientSessAccessMode_Type())
ntwsClSessClientSessAccessMode.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClSessClientSessAccessMode.setStatus(_B)
_NtwsClSessClientSessApNum_Type=NtwsApNum
_NtwsClSessClientSessApNum_Object=MibTableColumn
ntwsClSessClientSessApNum=_NtwsClSessClientSessApNum_Object((1,3,6,1,4,1,45,6,1,4,4,1,1,1,1,21),_NtwsClSessClientSessApNum_Type())
ntwsClSessClientSessApNum.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClSessClientSessApNum.setStatus(_B)
_NtwsClSessClientSessPhysPortNum_Type=NtwsPhysPortNumberOrZero
_NtwsClSessClientSessPhysPortNum_Object=MibTableColumn
ntwsClSessClientSessPhysPortNum=_NtwsClSessClientSessPhysPortNum_Object((1,3,6,1,4,1,45,6,1,4,4,1,1,1,1,22),_NtwsClSessClientSessPhysPortNum_Type())
ntwsClSessClientSessPhysPortNum.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClSessClientSessPhysPortNum.setStatus(_B)
_NtwsClSessRoamingHistoryTable_Object=MibTable
ntwsClSessRoamingHistoryTable=_NtwsClSessRoamingHistoryTable_Object((1,3,6,1,4,1,45,6,1,4,4,1,1,2))
if mibBuilder.loadTexts:ntwsClSessRoamingHistoryTable.setStatus(_B)
_NtwsClSessRoamingHistoryEntry_Object=MibTableRow
ntwsClSessRoamingHistoryEntry=_NtwsClSessRoamingHistoryEntry_Object((1,3,6,1,4,1,45,6,1,4,4,1,1,2,1))
ntwsClSessRoamingHistoryEntry.setIndexNames((0,_A,_r),(0,_A,_s))
if mibBuilder.loadTexts:ntwsClSessRoamingHistoryEntry.setStatus(_B)
_NtwsClSessRoamHistMacAddress_Type=MacAddress
_NtwsClSessRoamHistMacAddress_Object=MibTableColumn
ntwsClSessRoamHistMacAddress=_NtwsClSessRoamHistMacAddress_Object((1,3,6,1,4,1,45,6,1,4,4,1,1,2,1,1),_NtwsClSessRoamHistMacAddress_Type())
ntwsClSessRoamHistMacAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:ntwsClSessRoamHistMacAddress.setStatus(_B)
_NtwsClSessRoamHistIndex_Type=Unsigned32
_NtwsClSessRoamHistIndex_Object=MibTableColumn
ntwsClSessRoamHistIndex=_NtwsClSessRoamHistIndex_Object((1,3,6,1,4,1,45,6,1,4,4,1,1,2,1,2),_NtwsClSessRoamHistIndex_Type())
ntwsClSessRoamHistIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:ntwsClSessRoamHistIndex.setStatus(_B)
_NtwsClSessRoamHistApSerialNum_Type=NtwsApSerialNum
_NtwsClSessRoamHistApSerialNum_Object=MibTableColumn
ntwsClSessRoamHistApSerialNum=_NtwsClSessRoamHistApSerialNum_Object((1,3,6,1,4,1,45,6,1,4,4,1,1,2,1,3),_NtwsClSessRoamHistApSerialNum_Type())
ntwsClSessRoamHistApSerialNum.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClSessRoamHistApSerialNum.setStatus(_B)
_NtwsClSessRoamHistRadioNum_Type=NtwsRadioNum
_NtwsClSessRoamHistRadioNum_Object=MibTableColumn
ntwsClSessRoamHistRadioNum=_NtwsClSessRoamHistRadioNum_Object((1,3,6,1,4,1,45,6,1,4,4,1,1,2,1,4),_NtwsClSessRoamHistRadioNum_Type())
ntwsClSessRoamHistRadioNum.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClSessRoamHistRadioNum.setStatus(_B)
_NtwsClSessRoamHistAccessType_Type=NtwsAccessType
_NtwsClSessRoamHistAccessType_Object=MibTableColumn
ntwsClSessRoamHistAccessType=_NtwsClSessRoamHistAccessType_Object((1,3,6,1,4,1,45,6,1,4,4,1,1,2,1,5),_NtwsClSessRoamHistAccessType_Type())
ntwsClSessRoamHistAccessType.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClSessRoamHistAccessType.setStatus(_D)
_NtwsClSessRoamHistApNumOrPort_Type=Unsigned32
_NtwsClSessRoamHistApNumOrPort_Object=MibTableColumn
ntwsClSessRoamHistApNumOrPort=_NtwsClSessRoamHistApNumOrPort_Object((1,3,6,1,4,1,45,6,1,4,4,1,1,2,1,6),_NtwsClSessRoamHistApNumOrPort_Type())
ntwsClSessRoamHistApNumOrPort.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClSessRoamHistApNumOrPort.setStatus(_D)
_NtwsClSessRoamHistIpAddress_Type=IpAddress
_NtwsClSessRoamHistIpAddress_Object=MibTableColumn
ntwsClSessRoamHistIpAddress=_NtwsClSessRoamHistIpAddress_Object((1,3,6,1,4,1,45,6,1,4,4,1,1,2,1,7),_NtwsClSessRoamHistIpAddress_Type())
ntwsClSessRoamHistIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClSessRoamHistIpAddress.setStatus(_B)
_NtwsClSessRoamHistTimeStamp_Type=TimeStamp
_NtwsClSessRoamHistTimeStamp_Object=MibTableColumn
ntwsClSessRoamHistTimeStamp=_NtwsClSessRoamHistTimeStamp_Object((1,3,6,1,4,1,45,6,1,4,4,1,1,2,1,8),_NtwsClSessRoamHistTimeStamp_Type())
ntwsClSessRoamHistTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClSessRoamHistTimeStamp.setStatus(_B)
_NtwsClSessRoamHistAccessMode_Type=NtwsClientAccessMode
_NtwsClSessRoamHistAccessMode_Object=MibTableColumn
ntwsClSessRoamHistAccessMode=_NtwsClSessRoamHistAccessMode_Object((1,3,6,1,4,1,45,6,1,4,4,1,1,2,1,9),_NtwsClSessRoamHistAccessMode_Type())
ntwsClSessRoamHistAccessMode.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClSessRoamHistAccessMode.setStatus(_B)
_NtwsClSessRoamHistApNum_Type=NtwsApNum
_NtwsClSessRoamHistApNum_Object=MibTableColumn
ntwsClSessRoamHistApNum=_NtwsClSessRoamHistApNum_Object((1,3,6,1,4,1,45,6,1,4,4,1,1,2,1,10),_NtwsClSessRoamHistApNum_Type())
ntwsClSessRoamHistApNum.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClSessRoamHistApNum.setStatus(_B)
_NtwsClSessRoamHistPhysPortNum_Type=NtwsPhysPortNumberOrZero
_NtwsClSessRoamHistPhysPortNum_Object=MibTableColumn
ntwsClSessRoamHistPhysPortNum=_NtwsClSessRoamHistPhysPortNum_Object((1,3,6,1,4,1,45,6,1,4,4,1,1,2,1,11),_NtwsClSessRoamHistPhysPortNum_Type())
ntwsClSessRoamHistPhysPortNum.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClSessRoamHistPhysPortNum.setStatus(_B)
_NtwsClSessClientSessionStatisticsTable_Object=MibTable
ntwsClSessClientSessionStatisticsTable=_NtwsClSessClientSessionStatisticsTable_Object((1,3,6,1,4,1,45,6,1,4,4,1,1,3))
if mibBuilder.loadTexts:ntwsClSessClientSessionStatisticsTable.setStatus(_B)
_NtwsClSessClientSessionStatisticsEntry_Object=MibTableRow
ntwsClSessClientSessionStatisticsEntry=_NtwsClSessClientSessionStatisticsEntry_Object((1,3,6,1,4,1,45,6,1,4,4,1,1,3,1))
ntwsClSessClientSessionStatisticsEntry.setIndexNames((0,_A,_t))
if mibBuilder.loadTexts:ntwsClSessClientSessionStatisticsEntry.setStatus(_B)
_NtwsClSessClientSessStatsMacAddress_Type=MacAddress
_NtwsClSessClientSessStatsMacAddress_Object=MibTableColumn
ntwsClSessClientSessStatsMacAddress=_NtwsClSessClientSessStatsMacAddress_Object((1,3,6,1,4,1,45,6,1,4,4,1,1,3,1,1),_NtwsClSessClientSessStatsMacAddress_Type())
ntwsClSessClientSessStatsMacAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:ntwsClSessClientSessStatsMacAddress.setStatus(_B)
_NtwsClSessClientSessStatsUniPktIn_Type=Counter64
_NtwsClSessClientSessStatsUniPktIn_Object=MibTableColumn
ntwsClSessClientSessStatsUniPktIn=_NtwsClSessClientSessStatsUniPktIn_Object((1,3,6,1,4,1,45,6,1,4,4,1,1,3,1,2),_NtwsClSessClientSessStatsUniPktIn_Type())
ntwsClSessClientSessStatsUniPktIn.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClSessClientSessStatsUniPktIn.setStatus(_B)
_NtwsClSessClientSessStatsUniOctetIn_Type=Counter64
_NtwsClSessClientSessStatsUniOctetIn_Object=MibTableColumn
ntwsClSessClientSessStatsUniOctetIn=_NtwsClSessClientSessStatsUniOctetIn_Object((1,3,6,1,4,1,45,6,1,4,4,1,1,3,1,3),_NtwsClSessClientSessStatsUniOctetIn_Type())
ntwsClSessClientSessStatsUniOctetIn.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClSessClientSessStatsUniOctetIn.setStatus(_B)
_NtwsClSessClientSessStatsUniPktOut_Type=Counter64
_NtwsClSessClientSessStatsUniPktOut_Object=MibTableColumn
ntwsClSessClientSessStatsUniPktOut=_NtwsClSessClientSessStatsUniPktOut_Object((1,3,6,1,4,1,45,6,1,4,4,1,1,3,1,4),_NtwsClSessClientSessStatsUniPktOut_Type())
ntwsClSessClientSessStatsUniPktOut.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClSessClientSessStatsUniPktOut.setStatus(_B)
_NtwsClSessClientSessStatsUniOctetOut_Type=Counter64
_NtwsClSessClientSessStatsUniOctetOut_Object=MibTableColumn
ntwsClSessClientSessStatsUniOctetOut=_NtwsClSessClientSessStatsUniOctetOut_Object((1,3,6,1,4,1,45,6,1,4,4,1,1,3,1,5),_NtwsClSessClientSessStatsUniOctetOut_Type())
ntwsClSessClientSessStatsUniOctetOut.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClSessClientSessStatsUniOctetOut.setStatus(_B)
_NtwsClSessClientSessStatsMultiPktIn_Type=Counter64
_NtwsClSessClientSessStatsMultiPktIn_Object=MibTableColumn
ntwsClSessClientSessStatsMultiPktIn=_NtwsClSessClientSessStatsMultiPktIn_Object((1,3,6,1,4,1,45,6,1,4,4,1,1,3,1,6),_NtwsClSessClientSessStatsMultiPktIn_Type())
ntwsClSessClientSessStatsMultiPktIn.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClSessClientSessStatsMultiPktIn.setStatus(_B)
_NtwsClSessClientSessStatsMultiOctetIn_Type=Counter64
_NtwsClSessClientSessStatsMultiOctetIn_Object=MibTableColumn
ntwsClSessClientSessStatsMultiOctetIn=_NtwsClSessClientSessStatsMultiOctetIn_Object((1,3,6,1,4,1,45,6,1,4,4,1,1,3,1,7),_NtwsClSessClientSessStatsMultiOctetIn_Type())
ntwsClSessClientSessStatsMultiOctetIn.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClSessClientSessStatsMultiOctetIn.setStatus(_B)
_NtwsClSessClientSessStatsEncErrPkt_Type=Counter64
_NtwsClSessClientSessStatsEncErrPkt_Object=MibTableColumn
ntwsClSessClientSessStatsEncErrPkt=_NtwsClSessClientSessStatsEncErrPkt_Object((1,3,6,1,4,1,45,6,1,4,4,1,1,3,1,8),_NtwsClSessClientSessStatsEncErrPkt_Type())
ntwsClSessClientSessStatsEncErrPkt.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClSessClientSessStatsEncErrPkt.setStatus(_B)
_NtwsClSessClientSessStatsEncErrOctet_Type=Counter64
_NtwsClSessClientSessStatsEncErrOctet_Object=MibTableColumn
ntwsClSessClientSessStatsEncErrOctet=_NtwsClSessClientSessStatsEncErrOctet_Object((1,3,6,1,4,1,45,6,1,4,4,1,1,3,1,9),_NtwsClSessClientSessStatsEncErrOctet_Type())
ntwsClSessClientSessStatsEncErrOctet.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClSessClientSessStatsEncErrOctet.setStatus(_B)
_NtwsClSessClientSessStatsLastRate_Type=NtwsRadioRate
_NtwsClSessClientSessStatsLastRate_Object=MibTableColumn
ntwsClSessClientSessStatsLastRate=_NtwsClSessClientSessStatsLastRate_Object((1,3,6,1,4,1,45,6,1,4,4,1,1,3,1,10),_NtwsClSessClientSessStatsLastRate_Type())
ntwsClSessClientSessStatsLastRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClSessClientSessStatsLastRate.setStatus(_B)
_NtwsClSessClientSessStatsLastRssi_Type=NtwsRssi
_NtwsClSessClientSessStatsLastRssi_Object=MibTableColumn
ntwsClSessClientSessStatsLastRssi=_NtwsClSessClientSessStatsLastRssi_Object((1,3,6,1,4,1,45,6,1,4,4,1,1,3,1,11),_NtwsClSessClientSessStatsLastRssi_Type())
ntwsClSessClientSessStatsLastRssi.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClSessClientSessStatsLastRssi.setStatus(_B)
_NtwsClSessClientSessStatsLastSNR_Type=Integer32
_NtwsClSessClientSessStatsLastSNR_Object=MibTableColumn
ntwsClSessClientSessStatsLastSNR=_NtwsClSessClientSessStatsLastSNR_Object((1,3,6,1,4,1,45,6,1,4,4,1,1,3,1,12),_NtwsClSessClientSessStatsLastSNR_Type())
ntwsClSessClientSessStatsLastSNR.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClSessClientSessStatsLastSNR.setStatus(_B)
_NtwsClSessTotalSessions_Type=Unsigned32
_NtwsClSessTotalSessions_Object=MibScalar
ntwsClSessTotalSessions=_NtwsClSessTotalSessions_Object((1,3,6,1,4,1,45,6,1,4,4,1,1,4),_NtwsClSessTotalSessions_Type())
ntwsClSessTotalSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClSessTotalSessions.setStatus(_B)
_NtwsClientSessionConformance_ObjectIdentity=ObjectIdentity
ntwsClientSessionConformance=_NtwsClientSessionConformance_ObjectIdentity((1,3,6,1,4,1,45,6,1,4,4,1,2))
_NtwsClientSessionCompliances_ObjectIdentity=ObjectIdentity
ntwsClientSessionCompliances=_NtwsClientSessionCompliances_ObjectIdentity((1,3,6,1,4,1,45,6,1,4,4,1,2,1))
_NtwsClientSessionGroups_ObjectIdentity=ObjectIdentity
ntwsClientSessionGroups=_NtwsClientSessionGroups_ObjectIdentity((1,3,6,1,4,1,45,6,1,4,4,1,2,2))
ntwsClientSessionCommonGroup=ObjectGroup((1,3,6,1,4,1,45,6,1,4,4,1,2,2,1))
ntwsClientSessionCommonGroup.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_W),(_A,_u),(_A,_O),(_A,_X),(_A,_P),(_A,_Q),(_A,_R),(_A,_v),(_A,_S),(_A,_T),(_A,_Y),(_A,_Z),(_A,_U),(_A,_V),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k)))
if mibBuilder.loadTexts:ntwsClientSessionCommonGroup.setStatus(_D)
ntwsClientSessScalarsGroup=ObjectGroup((1,3,6,1,4,1,45,6,1,4,4,1,2,2,2))
ntwsClientSessScalarsGroup.setObjects((_A,_w))
if mibBuilder.loadTexts:ntwsClientSessScalarsGroup.setStatus(_B)
ntwsClientSessClientSessionTableGroup=ObjectGroup((1,3,6,1,4,1,45,6,1,4,4,1,2,2,3))
ntwsClientSessClientSessionTableGroup.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_W),(_A,_O),(_A,_X),(_A,_P),(_A,_Q),(_A,_R),(_A,_l),(_A,_m),(_A,_n)))
if mibBuilder.loadTexts:ntwsClientSessClientSessionTableGroup.setStatus(_D)
ntwsClientSessRoamingHistoryTableGroup=ObjectGroup((1,3,6,1,4,1,45,6,1,4,4,1,2,2,4))
ntwsClientSessRoamingHistoryTableGroup.setObjects(*((_A,_S),(_A,_T),(_A,_Y),(_A,_Z),(_A,_U),(_A,_V)))
if mibBuilder.loadTexts:ntwsClientSessRoamingHistoryTableGroup.setStatus(_D)
ntwsClientSessClientSessionStatisticsTableGroup=ObjectGroup((1,3,6,1,4,1,45,6,1,4,4,1,2,2,5))
ntwsClientSessClientSessionStatisticsTableGroup.setObjects(*((_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k)))
if mibBuilder.loadTexts:ntwsClientSessClientSessionStatisticsTableGroup.setStatus(_B)
ntwsClientSessClientSessionTableGroupRev2=ObjectGroup((1,3,6,1,4,1,45,6,1,4,4,1,2,2,6))
ntwsClientSessClientSessionTableGroupRev2.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_l),(_A,_m),(_A,_n),(_A,_x),(_A,_y),(_A,_z)))
if mibBuilder.loadTexts:ntwsClientSessClientSessionTableGroupRev2.setStatus(_B)
ntwsClientSessRoamingHistoryTableGroupRev2=ObjectGroup((1,3,6,1,4,1,45,6,1,4,4,1,2,2,7))
ntwsClientSessRoamingHistoryTableGroupRev2.setObjects(*((_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_A0),(_A,_A1),(_A,_A2)))
if mibBuilder.loadTexts:ntwsClientSessRoamingHistoryTableGroupRev2.setStatus(_B)
ntwsClientSessionCompliance=ModuleCompliance((1,3,6,1,4,1,45,6,1,4,4,1,2,1,1))
ntwsClientSessionCompliance.setObjects((_A,_A3))
if mibBuilder.loadTexts:ntwsClientSessionCompliance.setStatus(_D)
ntwsClientSessionComplianceRev2=ModuleCompliance((1,3,6,1,4,1,45,6,1,4,4,1,2,1,2))
ntwsClientSessionComplianceRev2.setObjects(*((_A,_o),(_A,_A4),(_A,_A5),(_A,_p)))
if mibBuilder.loadTexts:ntwsClientSessionComplianceRev2.setStatus(_D)
ntwsClientSessionComplianceRev3=ModuleCompliance((1,3,6,1,4,1,45,6,1,4,4,1,2,1,3))
ntwsClientSessionComplianceRev3.setObjects(*((_A,_o),(_A,_A6),(_A,_A7),(_A,_p)))
if mibBuilder.loadTexts:ntwsClientSessionComplianceRev3.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'NtwsEncryptionType':NtwsEncryptionType,'NtwsAuthMethod':NtwsAuthMethod,'NtwsSessState':NtwsSessState,'ntwsClientSessionMib':ntwsClientSessionMib,'ntwsClientSessionObjects':ntwsClientSessionObjects,'ntwsClientSessionDataObjects':ntwsClientSessionDataObjects,'ntwsClSessClientSessionTable':ntwsClSessClientSessionTable,'ntwsClSessClientSessionEntry':ntwsClSessClientSessionEntry,_q:ntwsClSessClientSessMacAddress,_H:ntwsClSessClientSessSessionId,_I:ntwsClSessClientSessUsername,_J:ntwsClSessClientSessIpAddress,_K:ntwsClSessClientSessEncryptionType,_L:ntwsClSessClientSessVlan,_M:ntwsClSessClientSessApSerialNum,_N:ntwsClSessClientSessRadioNum,_W:ntwsClSessClientSessAccessType,_u:ntwsClSessClientSessAuthMethod,_O:ntwsClSessClientSessAuthServer,_X:ntwsClSessClientSessPortOrNum,_P:ntwsClSessClientSessVlanTag,_Q:ntwsClSessClientSessTimeStamp,_R:ntwsClSessClientSessSsid,_v:ntwsClSessClientSessState,_l:ntwsClSessClientSessLoginType,_m:ntwsClSessClientSessDot1xAuthMethod,_n:ntwsClSessClientSessSessionState,_x:ntwsClSessClientSessAccessMode,_y:ntwsClSessClientSessApNum,_z:ntwsClSessClientSessPhysPortNum,'ntwsClSessRoamingHistoryTable':ntwsClSessRoamingHistoryTable,'ntwsClSessRoamingHistoryEntry':ntwsClSessRoamingHistoryEntry,_r:ntwsClSessRoamHistMacAddress,_s:ntwsClSessRoamHistIndex,_S:ntwsClSessRoamHistApSerialNum,_T:ntwsClSessRoamHistRadioNum,_Y:ntwsClSessRoamHistAccessType,_Z:ntwsClSessRoamHistApNumOrPort,_U:ntwsClSessRoamHistIpAddress,_V:ntwsClSessRoamHistTimeStamp,_A0:ntwsClSessRoamHistAccessMode,_A1:ntwsClSessRoamHistApNum,_A2:ntwsClSessRoamHistPhysPortNum,'ntwsClSessClientSessionStatisticsTable':ntwsClSessClientSessionStatisticsTable,'ntwsClSessClientSessionStatisticsEntry':ntwsClSessClientSessionStatisticsEntry,_t:ntwsClSessClientSessStatsMacAddress,_a:ntwsClSessClientSessStatsUniPktIn,_b:ntwsClSessClientSessStatsUniOctetIn,_c:ntwsClSessClientSessStatsUniPktOut,_d:ntwsClSessClientSessStatsUniOctetOut,_e:ntwsClSessClientSessStatsMultiPktIn,_f:ntwsClSessClientSessStatsMultiOctetIn,_g:ntwsClSessClientSessStatsEncErrPkt,_h:ntwsClSessClientSessStatsEncErrOctet,_i:ntwsClSessClientSessStatsLastRate,_j:ntwsClSessClientSessStatsLastRssi,_k:ntwsClSessClientSessStatsLastSNR,_w:ntwsClSessTotalSessions,'ntwsClientSessionConformance':ntwsClientSessionConformance,'ntwsClientSessionCompliances':ntwsClientSessionCompliances,'ntwsClientSessionCompliance':ntwsClientSessionCompliance,'ntwsClientSessionComplianceRev2':ntwsClientSessionComplianceRev2,'ntwsClientSessionComplianceRev3':ntwsClientSessionComplianceRev3,'ntwsClientSessionGroups':ntwsClientSessionGroups,_A3:ntwsClientSessionCommonGroup,_o:ntwsClientSessScalarsGroup,_A4:ntwsClientSessClientSessionTableGroup,_A5:ntwsClientSessRoamingHistoryTableGroup,_p:ntwsClientSessClientSessionStatisticsTableGroup,_A6:ntwsClientSessClientSessionTableGroupRev2,_A7:ntwsClientSessRoamingHistoryTableGroupRev2})