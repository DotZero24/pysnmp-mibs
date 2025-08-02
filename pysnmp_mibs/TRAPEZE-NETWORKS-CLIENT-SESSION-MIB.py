_AF='trpzClSessClientAddressTableGroup'
_AE='trpzClientSessClientSessionTableGroupRev3'
_AD='trpzClientSessClientSessionTableGroupRev2'
_AC='trpzClientSessRoamingHistoryTableGroup'
_AB='trpzClientSessClientSessionTableGroup'
_AA='trpzClientSessionCommonGroup'
_A9='trpzClSessClientSessDeviceProfileName'
_A8='trpzClSessClientSessDeviceGroup'
_A7='trpzClSessClientSessDeviceType'
_A6='trpzClSessClientAddressValue'
_A5='trpzClSessClientAddressType'
_A4='trpzClSessRoamHistPhysPortNum'
_A3='trpzClSessRoamHistApNum'
_A2='trpzClSessRoamHistAccessMode'
_A1='trpzClSessTotalSessions'
_A0='trpzClSessClientSessState'
_z='trpzClSessClientSessAuthMethod'
_y='trpzClSessClientAddressIndex'
_x='trpzClSessClientSessStatsMacAddress'
_w='trpzClSessRoamHistIndex'
_v='trpzClSessRoamHistMacAddress'
_u='deprecated'
_t='trpzClientSessRoamingHistoryTableGroupRev2'
_s='trpzClSessClientSessPhysPortNum'
_r='trpzClSessClientSessApNum'
_q='trpzClSessClientSessAccessMode'
_p='trpzClSessClientSessStatsLastSNR'
_o='trpzClSessClientSessStatsLastRssi'
_n='trpzClSessClientSessStatsLastRate'
_m='trpzClSessClientSessStatsEncErrOctet'
_l='trpzClSessClientSessStatsEncErrPkt'
_k='trpzClSessClientSessStatsMultiOctetIn'
_j='trpzClSessClientSessStatsMultiPktIn'
_i='trpzClSessClientSessStatsUniOctetOut'
_h='trpzClSessClientSessStatsUniPktOut'
_g='trpzClSessClientSessStatsUniOctetIn'
_f='trpzClSessClientSessStatsUniPktIn'
_e='trpzClSessRoamHistApNumOrPort'
_d='trpzClSessRoamHistAccessType'
_c='trpzClSessClientSessPortOrNum'
_b='trpzClSessClientSessAccessType'
_a='trpzClSessClientSessMacAddress'
_Z='trpzClientSessClientSessionStatisticsTableGroup'
_Y='trpzClientSessScalarsGroup'
_X='trpzClSessClientSessSessionState'
_W='trpzClSessClientSessDot1xAuthMethod'
_V='trpzClSessClientSessLoginType'
_U='trpzClSessRoamHistTimeStamp'
_T='trpzClSessRoamHistIpAddress'
_S='trpzClSessRoamHistRadioNum'
_R='trpzClSessRoamHistApSerialNum'
_Q='trpzClSessClientSessSsid'
_P='trpzClSessClientSessTimeStamp'
_O='trpzClSessClientSessVlanTag'
_N='trpzClSessClientSessAuthServer'
_M='trpzClSessClientSessRadioNum'
_L='trpzClSessClientSessApSerialNum'
_K='trpzClSessClientSessVlan'
_J='trpzClSessClientSessEncryptionType'
_I='trpzClSessClientSessIpAddress'
_H='trpzClSessClientSessUsername'
_G='trpzClSessClientSessSessionId'
_F='not-accessible'
_E='DisplayString'
_D='obsolete'
_C='read-only'
_B='current'
_A='TRAPEZE-NETWORKS-CLIENT-SESSION-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC',_E,'MacAddress','PhysAddress','TextualConvention','TimeStamp')
TrpzAccessType,TrpzApNum,TrpzApSerialNum,TrpzRadioNum,TrpzRadioRate,TrpzRssi=mibBuilder.importSymbols('TRAPEZE-NETWORKS-AP-TC','TrpzAccessType','TrpzApNum','TrpzApSerialNum','TrpzRadioNum','TrpzRadioRate','TrpzRssi')
TrpzPhysPortNumberOrZero,=mibBuilder.importSymbols('TRAPEZE-NETWORKS-BASIC-TC','TrpzPhysPortNumberOrZero')
TrpzClientAccessMode,TrpzClientAuthenProtocolType,TrpzClientDeviceGroupName,TrpzClientDeviceProfileName,TrpzClientDeviceType,TrpzClientSessionState,TrpzUserAccessType=mibBuilder.importSymbols('TRAPEZE-NETWORKS-CLIENT-SESSION-TC','TrpzClientAccessMode','TrpzClientAuthenProtocolType','TrpzClientDeviceGroupName','TrpzClientDeviceProfileName','TrpzClientDeviceType','TrpzClientSessionState','TrpzUserAccessType')
trpzMibs,=mibBuilder.importSymbols('TRAPEZE-NETWORKS-ROOT-MIB','trpzMibs')
trpzClientSessionMib=ModuleIdentity((1,3,6,1,4,1,14525,4,4))
if mibBuilder.loadTexts:trpzClientSessionMib.setRevisions(('2012-04-20 01:12','2011-12-06 01:10','2011-05-18 01:00','2008-10-23 00:56','2008-05-23 00:55','2007-11-01 00:54','2007-10-09 00:51','2006-11-16 00:43','2006-10-17 00:42','2006-09-26 00:32','2006-07-29 00:21','2006-06-06 00:10','2006-03-30 00:08'))
class TrpzEncryptionType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('none',1),('aesCcm',2),('aesOcb',3),('tkip',4),('wep104',5),('wep40',6),('staticWep',7)))
class TrpzAuthMethod(TextualConvention,Integer32):status=_D;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,14,18,22,26,27,34,255)));namedValues=NamedValues(*(('none',1),('identity',2),('notification',3),('nak',4),('md5',5),('otp',6),('tokenCard',7),('tls',14),('leap',18),('ttls',22),('peap',26),('msChapv2',27),('eapExt',34),('passThru',255)))
class TrpzSessState(TextualConvention,Integer32):status=_u;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21)));namedValues=NamedValues(*(('invalid',1),('initializing',2),('assocReqAndAuth',3),('assocAndAuth',4),('wired',5),('webLoginPh1',6),('webLoginPh1B',7),('webLoginPh1F',8),('webLoginPh2',9),('webPortalLogin',10),('authorizing',11),('authorized',12),('active',13),('activePortal',14),('deassociated',15),('roamingAway',16),('updatedToRoam',17),('roamedAway',18),('killing',19),('free',20),('enforceSoda',21)))
_TrpzClientSessionObjects_ObjectIdentity=ObjectIdentity
trpzClientSessionObjects=_TrpzClientSessionObjects_ObjectIdentity((1,3,6,1,4,1,14525,4,4,1))
_TrpzClientSessionDataObjects_ObjectIdentity=ObjectIdentity
trpzClientSessionDataObjects=_TrpzClientSessionDataObjects_ObjectIdentity((1,3,6,1,4,1,14525,4,4,1,1))
_TrpzClSessClientSessionTable_Object=MibTable
trpzClSessClientSessionTable=_TrpzClSessClientSessionTable_Object((1,3,6,1,4,1,14525,4,4,1,1,1))
if mibBuilder.loadTexts:trpzClSessClientSessionTable.setStatus(_B)
_TrpzClSessClientSessionEntry_Object=MibTableRow
trpzClSessClientSessionEntry=_TrpzClSessClientSessionEntry_Object((1,3,6,1,4,1,14525,4,4,1,1,1,1))
trpzClSessClientSessionEntry.setIndexNames((0,_A,_a))
if mibBuilder.loadTexts:trpzClSessClientSessionEntry.setStatus(_B)
_TrpzClSessClientSessMacAddress_Type=MacAddress
_TrpzClSessClientSessMacAddress_Object=MibTableColumn
trpzClSessClientSessMacAddress=_TrpzClSessClientSessMacAddress_Object((1,3,6,1,4,1,14525,4,4,1,1,1,1,1),_TrpzClSessClientSessMacAddress_Type())
trpzClSessClientSessMacAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:trpzClSessClientSessMacAddress.setStatus(_B)
class _TrpzClSessClientSessSessionId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_TrpzClSessClientSessSessionId_Type.__name__=_E
_TrpzClSessClientSessSessionId_Object=MibTableColumn
trpzClSessClientSessSessionId=_TrpzClSessClientSessSessionId_Object((1,3,6,1,4,1,14525,4,4,1,1,1,1,2),_TrpzClSessClientSessSessionId_Type())
trpzClSessClientSessSessionId.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzClSessClientSessSessionId.setStatus(_B)
class _TrpzClSessClientSessUsername_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_TrpzClSessClientSessUsername_Type.__name__=_E
_TrpzClSessClientSessUsername_Object=MibTableColumn
trpzClSessClientSessUsername=_TrpzClSessClientSessUsername_Object((1,3,6,1,4,1,14525,4,4,1,1,1,1,3),_TrpzClSessClientSessUsername_Type())
trpzClSessClientSessUsername.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzClSessClientSessUsername.setStatus(_B)
_TrpzClSessClientSessIpAddress_Type=IpAddress
_TrpzClSessClientSessIpAddress_Object=MibTableColumn
trpzClSessClientSessIpAddress=_TrpzClSessClientSessIpAddress_Object((1,3,6,1,4,1,14525,4,4,1,1,1,1,4),_TrpzClSessClientSessIpAddress_Type())
trpzClSessClientSessIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzClSessClientSessIpAddress.setStatus(_B)
_TrpzClSessClientSessEncryptionType_Type=TrpzEncryptionType
_TrpzClSessClientSessEncryptionType_Object=MibTableColumn
trpzClSessClientSessEncryptionType=_TrpzClSessClientSessEncryptionType_Object((1,3,6,1,4,1,14525,4,4,1,1,1,1,5),_TrpzClSessClientSessEncryptionType_Type())
trpzClSessClientSessEncryptionType.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzClSessClientSessEncryptionType.setStatus(_B)
class _TrpzClSessClientSessVlan_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_TrpzClSessClientSessVlan_Type.__name__=_E
_TrpzClSessClientSessVlan_Object=MibTableColumn
trpzClSessClientSessVlan=_TrpzClSessClientSessVlan_Object((1,3,6,1,4,1,14525,4,4,1,1,1,1,6),_TrpzClSessClientSessVlan_Type())
trpzClSessClientSessVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzClSessClientSessVlan.setStatus(_B)
_TrpzClSessClientSessApSerialNum_Type=TrpzApSerialNum
_TrpzClSessClientSessApSerialNum_Object=MibTableColumn
trpzClSessClientSessApSerialNum=_TrpzClSessClientSessApSerialNum_Object((1,3,6,1,4,1,14525,4,4,1,1,1,1,7),_TrpzClSessClientSessApSerialNum_Type())
trpzClSessClientSessApSerialNum.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzClSessClientSessApSerialNum.setStatus(_B)
_TrpzClSessClientSessRadioNum_Type=TrpzRadioNum
_TrpzClSessClientSessRadioNum_Object=MibTableColumn
trpzClSessClientSessRadioNum=_TrpzClSessClientSessRadioNum_Object((1,3,6,1,4,1,14525,4,4,1,1,1,1,8),_TrpzClSessClientSessRadioNum_Type())
trpzClSessClientSessRadioNum.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzClSessClientSessRadioNum.setStatus(_B)
_TrpzClSessClientSessAccessType_Type=TrpzAccessType
_TrpzClSessClientSessAccessType_Object=MibTableColumn
trpzClSessClientSessAccessType=_TrpzClSessClientSessAccessType_Object((1,3,6,1,4,1,14525,4,4,1,1,1,1,9),_TrpzClSessClientSessAccessType_Type())
trpzClSessClientSessAccessType.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzClSessClientSessAccessType.setStatus(_D)
_TrpzClSessClientSessAuthMethod_Type=TrpzAuthMethod
_TrpzClSessClientSessAuthMethod_Object=MibTableColumn
trpzClSessClientSessAuthMethod=_TrpzClSessClientSessAuthMethod_Object((1,3,6,1,4,1,14525,4,4,1,1,1,1,10),_TrpzClSessClientSessAuthMethod_Type())
trpzClSessClientSessAuthMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzClSessClientSessAuthMethod.setStatus(_D)
_TrpzClSessClientSessAuthServer_Type=IpAddress
_TrpzClSessClientSessAuthServer_Object=MibTableColumn
trpzClSessClientSessAuthServer=_TrpzClSessClientSessAuthServer_Object((1,3,6,1,4,1,14525,4,4,1,1,1,1,11),_TrpzClSessClientSessAuthServer_Type())
trpzClSessClientSessAuthServer.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzClSessClientSessAuthServer.setStatus(_B)
_TrpzClSessClientSessPortOrNum_Type=Unsigned32
_TrpzClSessClientSessPortOrNum_Object=MibTableColumn
trpzClSessClientSessPortOrNum=_TrpzClSessClientSessPortOrNum_Object((1,3,6,1,4,1,14525,4,4,1,1,1,1,12),_TrpzClSessClientSessPortOrNum_Type())
trpzClSessClientSessPortOrNum.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzClSessClientSessPortOrNum.setStatus(_D)
_TrpzClSessClientSessVlanTag_Type=Unsigned32
_TrpzClSessClientSessVlanTag_Object=MibTableColumn
trpzClSessClientSessVlanTag=_TrpzClSessClientSessVlanTag_Object((1,3,6,1,4,1,14525,4,4,1,1,1,1,13),_TrpzClSessClientSessVlanTag_Type())
trpzClSessClientSessVlanTag.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzClSessClientSessVlanTag.setStatus(_B)
_TrpzClSessClientSessTimeStamp_Type=TimeStamp
_TrpzClSessClientSessTimeStamp_Object=MibTableColumn
trpzClSessClientSessTimeStamp=_TrpzClSessClientSessTimeStamp_Object((1,3,6,1,4,1,14525,4,4,1,1,1,1,14),_TrpzClSessClientSessTimeStamp_Type())
trpzClSessClientSessTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzClSessClientSessTimeStamp.setStatus(_B)
class _TrpzClSessClientSessSsid_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,33))
_TrpzClSessClientSessSsid_Type.__name__=_E
_TrpzClSessClientSessSsid_Object=MibTableColumn
trpzClSessClientSessSsid=_TrpzClSessClientSessSsid_Object((1,3,6,1,4,1,14525,4,4,1,1,1,1,15),_TrpzClSessClientSessSsid_Type())
trpzClSessClientSessSsid.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzClSessClientSessSsid.setStatus(_B)
_TrpzClSessClientSessState_Type=TrpzSessState
_TrpzClSessClientSessState_Object=MibTableColumn
trpzClSessClientSessState=_TrpzClSessClientSessState_Object((1,3,6,1,4,1,14525,4,4,1,1,1,1,16),_TrpzClSessClientSessState_Type())
trpzClSessClientSessState.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzClSessClientSessState.setStatus(_u)
_TrpzClSessClientSessLoginType_Type=TrpzUserAccessType
_TrpzClSessClientSessLoginType_Object=MibTableColumn
trpzClSessClientSessLoginType=_TrpzClSessClientSessLoginType_Object((1,3,6,1,4,1,14525,4,4,1,1,1,1,17),_TrpzClSessClientSessLoginType_Type())
trpzClSessClientSessLoginType.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzClSessClientSessLoginType.setStatus(_B)
_TrpzClSessClientSessDot1xAuthMethod_Type=TrpzClientAuthenProtocolType
_TrpzClSessClientSessDot1xAuthMethod_Object=MibTableColumn
trpzClSessClientSessDot1xAuthMethod=_TrpzClSessClientSessDot1xAuthMethod_Object((1,3,6,1,4,1,14525,4,4,1,1,1,1,18),_TrpzClSessClientSessDot1xAuthMethod_Type())
trpzClSessClientSessDot1xAuthMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzClSessClientSessDot1xAuthMethod.setStatus(_B)
_TrpzClSessClientSessSessionState_Type=TrpzClientSessionState
_TrpzClSessClientSessSessionState_Object=MibTableColumn
trpzClSessClientSessSessionState=_TrpzClSessClientSessSessionState_Object((1,3,6,1,4,1,14525,4,4,1,1,1,1,19),_TrpzClSessClientSessSessionState_Type())
trpzClSessClientSessSessionState.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzClSessClientSessSessionState.setStatus(_B)
_TrpzClSessClientSessAccessMode_Type=TrpzClientAccessMode
_TrpzClSessClientSessAccessMode_Object=MibTableColumn
trpzClSessClientSessAccessMode=_TrpzClSessClientSessAccessMode_Object((1,3,6,1,4,1,14525,4,4,1,1,1,1,20),_TrpzClSessClientSessAccessMode_Type())
trpzClSessClientSessAccessMode.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzClSessClientSessAccessMode.setStatus(_B)
_TrpzClSessClientSessApNum_Type=TrpzApNum
_TrpzClSessClientSessApNum_Object=MibTableColumn
trpzClSessClientSessApNum=_TrpzClSessClientSessApNum_Object((1,3,6,1,4,1,14525,4,4,1,1,1,1,21),_TrpzClSessClientSessApNum_Type())
trpzClSessClientSessApNum.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzClSessClientSessApNum.setStatus(_B)
_TrpzClSessClientSessPhysPortNum_Type=TrpzPhysPortNumberOrZero
_TrpzClSessClientSessPhysPortNum_Object=MibTableColumn
trpzClSessClientSessPhysPortNum=_TrpzClSessClientSessPhysPortNum_Object((1,3,6,1,4,1,14525,4,4,1,1,1,1,22),_TrpzClSessClientSessPhysPortNum_Type())
trpzClSessClientSessPhysPortNum.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzClSessClientSessPhysPortNum.setStatus(_B)
_TrpzClSessClientSessDeviceType_Type=TrpzClientDeviceType
_TrpzClSessClientSessDeviceType_Object=MibTableColumn
trpzClSessClientSessDeviceType=_TrpzClSessClientSessDeviceType_Object((1,3,6,1,4,1,14525,4,4,1,1,1,1,23),_TrpzClSessClientSessDeviceType_Type())
trpzClSessClientSessDeviceType.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzClSessClientSessDeviceType.setStatus(_B)
_TrpzClSessClientSessDeviceGroup_Type=TrpzClientDeviceGroupName
_TrpzClSessClientSessDeviceGroup_Object=MibTableColumn
trpzClSessClientSessDeviceGroup=_TrpzClSessClientSessDeviceGroup_Object((1,3,6,1,4,1,14525,4,4,1,1,1,1,24),_TrpzClSessClientSessDeviceGroup_Type())
trpzClSessClientSessDeviceGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzClSessClientSessDeviceGroup.setStatus(_B)
_TrpzClSessClientSessDeviceProfileName_Type=TrpzClientDeviceProfileName
_TrpzClSessClientSessDeviceProfileName_Object=MibTableColumn
trpzClSessClientSessDeviceProfileName=_TrpzClSessClientSessDeviceProfileName_Object((1,3,6,1,4,1,14525,4,4,1,1,1,1,25),_TrpzClSessClientSessDeviceProfileName_Type())
trpzClSessClientSessDeviceProfileName.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzClSessClientSessDeviceProfileName.setStatus(_B)
_TrpzClSessRoamingHistoryTable_Object=MibTable
trpzClSessRoamingHistoryTable=_TrpzClSessRoamingHistoryTable_Object((1,3,6,1,4,1,14525,4,4,1,1,2))
if mibBuilder.loadTexts:trpzClSessRoamingHistoryTable.setStatus(_B)
_TrpzClSessRoamingHistoryEntry_Object=MibTableRow
trpzClSessRoamingHistoryEntry=_TrpzClSessRoamingHistoryEntry_Object((1,3,6,1,4,1,14525,4,4,1,1,2,1))
trpzClSessRoamingHistoryEntry.setIndexNames((0,_A,_v),(0,_A,_w))
if mibBuilder.loadTexts:trpzClSessRoamingHistoryEntry.setStatus(_B)
_TrpzClSessRoamHistMacAddress_Type=MacAddress
_TrpzClSessRoamHistMacAddress_Object=MibTableColumn
trpzClSessRoamHistMacAddress=_TrpzClSessRoamHistMacAddress_Object((1,3,6,1,4,1,14525,4,4,1,1,2,1,1),_TrpzClSessRoamHistMacAddress_Type())
trpzClSessRoamHistMacAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:trpzClSessRoamHistMacAddress.setStatus(_B)
_TrpzClSessRoamHistIndex_Type=Unsigned32
_TrpzClSessRoamHistIndex_Object=MibTableColumn
trpzClSessRoamHistIndex=_TrpzClSessRoamHistIndex_Object((1,3,6,1,4,1,14525,4,4,1,1,2,1,2),_TrpzClSessRoamHistIndex_Type())
trpzClSessRoamHistIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:trpzClSessRoamHistIndex.setStatus(_B)
_TrpzClSessRoamHistApSerialNum_Type=TrpzApSerialNum
_TrpzClSessRoamHistApSerialNum_Object=MibTableColumn
trpzClSessRoamHistApSerialNum=_TrpzClSessRoamHistApSerialNum_Object((1,3,6,1,4,1,14525,4,4,1,1,2,1,3),_TrpzClSessRoamHistApSerialNum_Type())
trpzClSessRoamHistApSerialNum.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzClSessRoamHistApSerialNum.setStatus(_B)
_TrpzClSessRoamHistRadioNum_Type=TrpzRadioNum
_TrpzClSessRoamHistRadioNum_Object=MibTableColumn
trpzClSessRoamHistRadioNum=_TrpzClSessRoamHistRadioNum_Object((1,3,6,1,4,1,14525,4,4,1,1,2,1,4),_TrpzClSessRoamHistRadioNum_Type())
trpzClSessRoamHistRadioNum.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzClSessRoamHistRadioNum.setStatus(_B)
_TrpzClSessRoamHistAccessType_Type=TrpzAccessType
_TrpzClSessRoamHistAccessType_Object=MibTableColumn
trpzClSessRoamHistAccessType=_TrpzClSessRoamHistAccessType_Object((1,3,6,1,4,1,14525,4,4,1,1,2,1,5),_TrpzClSessRoamHistAccessType_Type())
trpzClSessRoamHistAccessType.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzClSessRoamHistAccessType.setStatus(_D)
_TrpzClSessRoamHistApNumOrPort_Type=Unsigned32
_TrpzClSessRoamHistApNumOrPort_Object=MibTableColumn
trpzClSessRoamHistApNumOrPort=_TrpzClSessRoamHistApNumOrPort_Object((1,3,6,1,4,1,14525,4,4,1,1,2,1,6),_TrpzClSessRoamHistApNumOrPort_Type())
trpzClSessRoamHistApNumOrPort.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzClSessRoamHistApNumOrPort.setStatus(_D)
_TrpzClSessRoamHistIpAddress_Type=IpAddress
_TrpzClSessRoamHistIpAddress_Object=MibTableColumn
trpzClSessRoamHistIpAddress=_TrpzClSessRoamHistIpAddress_Object((1,3,6,1,4,1,14525,4,4,1,1,2,1,7),_TrpzClSessRoamHistIpAddress_Type())
trpzClSessRoamHistIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzClSessRoamHistIpAddress.setStatus(_B)
_TrpzClSessRoamHistTimeStamp_Type=TimeStamp
_TrpzClSessRoamHistTimeStamp_Object=MibTableColumn
trpzClSessRoamHistTimeStamp=_TrpzClSessRoamHistTimeStamp_Object((1,3,6,1,4,1,14525,4,4,1,1,2,1,8),_TrpzClSessRoamHistTimeStamp_Type())
trpzClSessRoamHistTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzClSessRoamHistTimeStamp.setStatus(_B)
_TrpzClSessRoamHistAccessMode_Type=TrpzClientAccessMode
_TrpzClSessRoamHistAccessMode_Object=MibTableColumn
trpzClSessRoamHistAccessMode=_TrpzClSessRoamHistAccessMode_Object((1,3,6,1,4,1,14525,4,4,1,1,2,1,9),_TrpzClSessRoamHistAccessMode_Type())
trpzClSessRoamHistAccessMode.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzClSessRoamHistAccessMode.setStatus(_B)
_TrpzClSessRoamHistApNum_Type=TrpzApNum
_TrpzClSessRoamHistApNum_Object=MibTableColumn
trpzClSessRoamHistApNum=_TrpzClSessRoamHistApNum_Object((1,3,6,1,4,1,14525,4,4,1,1,2,1,10),_TrpzClSessRoamHistApNum_Type())
trpzClSessRoamHistApNum.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzClSessRoamHistApNum.setStatus(_B)
_TrpzClSessRoamHistPhysPortNum_Type=TrpzPhysPortNumberOrZero
_TrpzClSessRoamHistPhysPortNum_Object=MibTableColumn
trpzClSessRoamHistPhysPortNum=_TrpzClSessRoamHistPhysPortNum_Object((1,3,6,1,4,1,14525,4,4,1,1,2,1,11),_TrpzClSessRoamHistPhysPortNum_Type())
trpzClSessRoamHistPhysPortNum.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzClSessRoamHistPhysPortNum.setStatus(_B)
_TrpzClSessClientSessionStatisticsTable_Object=MibTable
trpzClSessClientSessionStatisticsTable=_TrpzClSessClientSessionStatisticsTable_Object((1,3,6,1,4,1,14525,4,4,1,1,3))
if mibBuilder.loadTexts:trpzClSessClientSessionStatisticsTable.setStatus(_B)
_TrpzClSessClientSessionStatisticsEntry_Object=MibTableRow
trpzClSessClientSessionStatisticsEntry=_TrpzClSessClientSessionStatisticsEntry_Object((1,3,6,1,4,1,14525,4,4,1,1,3,1))
trpzClSessClientSessionStatisticsEntry.setIndexNames((0,_A,_x))
if mibBuilder.loadTexts:trpzClSessClientSessionStatisticsEntry.setStatus(_B)
_TrpzClSessClientSessStatsMacAddress_Type=MacAddress
_TrpzClSessClientSessStatsMacAddress_Object=MibTableColumn
trpzClSessClientSessStatsMacAddress=_TrpzClSessClientSessStatsMacAddress_Object((1,3,6,1,4,1,14525,4,4,1,1,3,1,1),_TrpzClSessClientSessStatsMacAddress_Type())
trpzClSessClientSessStatsMacAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:trpzClSessClientSessStatsMacAddress.setStatus(_B)
_TrpzClSessClientSessStatsUniPktIn_Type=Counter64
_TrpzClSessClientSessStatsUniPktIn_Object=MibTableColumn
trpzClSessClientSessStatsUniPktIn=_TrpzClSessClientSessStatsUniPktIn_Object((1,3,6,1,4,1,14525,4,4,1,1,3,1,2),_TrpzClSessClientSessStatsUniPktIn_Type())
trpzClSessClientSessStatsUniPktIn.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzClSessClientSessStatsUniPktIn.setStatus(_B)
_TrpzClSessClientSessStatsUniOctetIn_Type=Counter64
_TrpzClSessClientSessStatsUniOctetIn_Object=MibTableColumn
trpzClSessClientSessStatsUniOctetIn=_TrpzClSessClientSessStatsUniOctetIn_Object((1,3,6,1,4,1,14525,4,4,1,1,3,1,3),_TrpzClSessClientSessStatsUniOctetIn_Type())
trpzClSessClientSessStatsUniOctetIn.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzClSessClientSessStatsUniOctetIn.setStatus(_B)
_TrpzClSessClientSessStatsUniPktOut_Type=Counter64
_TrpzClSessClientSessStatsUniPktOut_Object=MibTableColumn
trpzClSessClientSessStatsUniPktOut=_TrpzClSessClientSessStatsUniPktOut_Object((1,3,6,1,4,1,14525,4,4,1,1,3,1,4),_TrpzClSessClientSessStatsUniPktOut_Type())
trpzClSessClientSessStatsUniPktOut.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzClSessClientSessStatsUniPktOut.setStatus(_B)
_TrpzClSessClientSessStatsUniOctetOut_Type=Counter64
_TrpzClSessClientSessStatsUniOctetOut_Object=MibTableColumn
trpzClSessClientSessStatsUniOctetOut=_TrpzClSessClientSessStatsUniOctetOut_Object((1,3,6,1,4,1,14525,4,4,1,1,3,1,5),_TrpzClSessClientSessStatsUniOctetOut_Type())
trpzClSessClientSessStatsUniOctetOut.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzClSessClientSessStatsUniOctetOut.setStatus(_B)
_TrpzClSessClientSessStatsMultiPktIn_Type=Counter64
_TrpzClSessClientSessStatsMultiPktIn_Object=MibTableColumn
trpzClSessClientSessStatsMultiPktIn=_TrpzClSessClientSessStatsMultiPktIn_Object((1,3,6,1,4,1,14525,4,4,1,1,3,1,6),_TrpzClSessClientSessStatsMultiPktIn_Type())
trpzClSessClientSessStatsMultiPktIn.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzClSessClientSessStatsMultiPktIn.setStatus(_B)
_TrpzClSessClientSessStatsMultiOctetIn_Type=Counter64
_TrpzClSessClientSessStatsMultiOctetIn_Object=MibTableColumn
trpzClSessClientSessStatsMultiOctetIn=_TrpzClSessClientSessStatsMultiOctetIn_Object((1,3,6,1,4,1,14525,4,4,1,1,3,1,7),_TrpzClSessClientSessStatsMultiOctetIn_Type())
trpzClSessClientSessStatsMultiOctetIn.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzClSessClientSessStatsMultiOctetIn.setStatus(_B)
_TrpzClSessClientSessStatsEncErrPkt_Type=Counter64
_TrpzClSessClientSessStatsEncErrPkt_Object=MibTableColumn
trpzClSessClientSessStatsEncErrPkt=_TrpzClSessClientSessStatsEncErrPkt_Object((1,3,6,1,4,1,14525,4,4,1,1,3,1,8),_TrpzClSessClientSessStatsEncErrPkt_Type())
trpzClSessClientSessStatsEncErrPkt.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzClSessClientSessStatsEncErrPkt.setStatus(_B)
_TrpzClSessClientSessStatsEncErrOctet_Type=Counter64
_TrpzClSessClientSessStatsEncErrOctet_Object=MibTableColumn
trpzClSessClientSessStatsEncErrOctet=_TrpzClSessClientSessStatsEncErrOctet_Object((1,3,6,1,4,1,14525,4,4,1,1,3,1,9),_TrpzClSessClientSessStatsEncErrOctet_Type())
trpzClSessClientSessStatsEncErrOctet.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzClSessClientSessStatsEncErrOctet.setStatus(_B)
_TrpzClSessClientSessStatsLastRate_Type=TrpzRadioRate
_TrpzClSessClientSessStatsLastRate_Object=MibTableColumn
trpzClSessClientSessStatsLastRate=_TrpzClSessClientSessStatsLastRate_Object((1,3,6,1,4,1,14525,4,4,1,1,3,1,10),_TrpzClSessClientSessStatsLastRate_Type())
trpzClSessClientSessStatsLastRate.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzClSessClientSessStatsLastRate.setStatus(_B)
_TrpzClSessClientSessStatsLastRssi_Type=TrpzRssi
_TrpzClSessClientSessStatsLastRssi_Object=MibTableColumn
trpzClSessClientSessStatsLastRssi=_TrpzClSessClientSessStatsLastRssi_Object((1,3,6,1,4,1,14525,4,4,1,1,3,1,11),_TrpzClSessClientSessStatsLastRssi_Type())
trpzClSessClientSessStatsLastRssi.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzClSessClientSessStatsLastRssi.setStatus(_B)
_TrpzClSessClientSessStatsLastSNR_Type=Integer32
_TrpzClSessClientSessStatsLastSNR_Object=MibTableColumn
trpzClSessClientSessStatsLastSNR=_TrpzClSessClientSessStatsLastSNR_Object((1,3,6,1,4,1,14525,4,4,1,1,3,1,12),_TrpzClSessClientSessStatsLastSNR_Type())
trpzClSessClientSessStatsLastSNR.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzClSessClientSessStatsLastSNR.setStatus(_B)
_TrpzClSessTotalSessions_Type=Unsigned32
_TrpzClSessTotalSessions_Object=MibScalar
trpzClSessTotalSessions=_TrpzClSessTotalSessions_Object((1,3,6,1,4,1,14525,4,4,1,1,4),_TrpzClSessTotalSessions_Type())
trpzClSessTotalSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzClSessTotalSessions.setStatus(_B)
_TrpzClSessClientAddressTable_Object=MibTable
trpzClSessClientAddressTable=_TrpzClSessClientAddressTable_Object((1,3,6,1,4,1,14525,4,4,1,1,5))
if mibBuilder.loadTexts:trpzClSessClientAddressTable.setStatus(_B)
_TrpzClSessClientAddressEntry_Object=MibTableRow
trpzClSessClientAddressEntry=_TrpzClSessClientAddressEntry_Object((1,3,6,1,4,1,14525,4,4,1,1,5,1))
trpzClSessClientAddressEntry.setIndexNames((0,_A,_a),(0,_A,_y))
if mibBuilder.loadTexts:trpzClSessClientAddressEntry.setStatus(_B)
_TrpzClSessClientAddressIndex_Type=Unsigned32
_TrpzClSessClientAddressIndex_Object=MibTableColumn
trpzClSessClientAddressIndex=_TrpzClSessClientAddressIndex_Object((1,3,6,1,4,1,14525,4,4,1,1,5,1,1),_TrpzClSessClientAddressIndex_Type())
trpzClSessClientAddressIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:trpzClSessClientAddressIndex.setStatus(_B)
_TrpzClSessClientAddressType_Type=InetAddressType
_TrpzClSessClientAddressType_Object=MibTableColumn
trpzClSessClientAddressType=_TrpzClSessClientAddressType_Object((1,3,6,1,4,1,14525,4,4,1,1,5,1,2),_TrpzClSessClientAddressType_Type())
trpzClSessClientAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzClSessClientAddressType.setStatus(_B)
_TrpzClSessClientAddressValue_Type=InetAddress
_TrpzClSessClientAddressValue_Object=MibTableColumn
trpzClSessClientAddressValue=_TrpzClSessClientAddressValue_Object((1,3,6,1,4,1,14525,4,4,1,1,5,1,3),_TrpzClSessClientAddressValue_Type())
trpzClSessClientAddressValue.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzClSessClientAddressValue.setStatus(_B)
_TrpzClientSessionConformance_ObjectIdentity=ObjectIdentity
trpzClientSessionConformance=_TrpzClientSessionConformance_ObjectIdentity((1,3,6,1,4,1,14525,4,4,1,2))
_TrpzClientSessionCompliances_ObjectIdentity=ObjectIdentity
trpzClientSessionCompliances=_TrpzClientSessionCompliances_ObjectIdentity((1,3,6,1,4,1,14525,4,4,1,2,1))
_TrpzClientSessionGroups_ObjectIdentity=ObjectIdentity
trpzClientSessionGroups=_TrpzClientSessionGroups_ObjectIdentity((1,3,6,1,4,1,14525,4,4,1,2,2))
trpzClientSessionCommonGroup=ObjectGroup((1,3,6,1,4,1,14525,4,4,1,2,2,1))
trpzClientSessionCommonGroup.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_b),(_A,_z),(_A,_N),(_A,_c),(_A,_O),(_A,_P),(_A,_Q),(_A,_A0),(_A,_R),(_A,_S),(_A,_d),(_A,_e),(_A,_T),(_A,_U),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p)))
if mibBuilder.loadTexts:trpzClientSessionCommonGroup.setStatus(_D)
trpzClientSessScalarsGroup=ObjectGroup((1,3,6,1,4,1,14525,4,4,1,2,2,2))
trpzClientSessScalarsGroup.setObjects((_A,_A1))
if mibBuilder.loadTexts:trpzClientSessScalarsGroup.setStatus(_B)
trpzClientSessClientSessionTableGroup=ObjectGroup((1,3,6,1,4,1,14525,4,4,1,2,2,3))
trpzClientSessClientSessionTableGroup.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_b),(_A,_N),(_A,_c),(_A,_O),(_A,_P),(_A,_Q),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:trpzClientSessClientSessionTableGroup.setStatus(_D)
trpzClientSessRoamingHistoryTableGroup=ObjectGroup((1,3,6,1,4,1,14525,4,4,1,2,2,4))
trpzClientSessRoamingHistoryTableGroup.setObjects(*((_A,_R),(_A,_S),(_A,_d),(_A,_e),(_A,_T),(_A,_U)))
if mibBuilder.loadTexts:trpzClientSessRoamingHistoryTableGroup.setStatus(_D)
trpzClientSessClientSessionStatisticsTableGroup=ObjectGroup((1,3,6,1,4,1,14525,4,4,1,2,2,5))
trpzClientSessClientSessionStatisticsTableGroup.setObjects(*((_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p)))
if mibBuilder.loadTexts:trpzClientSessClientSessionStatisticsTableGroup.setStatus(_B)
trpzClientSessClientSessionTableGroupRev2=ObjectGroup((1,3,6,1,4,1,14525,4,4,1,2,2,6))
trpzClientSessClientSessionTableGroupRev2.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_V),(_A,_W),(_A,_X),(_A,_q),(_A,_r),(_A,_s)))
if mibBuilder.loadTexts:trpzClientSessClientSessionTableGroupRev2.setStatus(_D)
trpzClientSessRoamingHistoryTableGroupRev2=ObjectGroup((1,3,6,1,4,1,14525,4,4,1,2,2,7))
trpzClientSessRoamingHistoryTableGroupRev2.setObjects(*((_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_A2),(_A,_A3),(_A,_A4)))
if mibBuilder.loadTexts:trpzClientSessRoamingHistoryTableGroupRev2.setStatus(_B)
trpzClSessClientAddressTableGroup=ObjectGroup((1,3,6,1,4,1,14525,4,4,1,2,2,8))
trpzClSessClientAddressTableGroup.setObjects(*((_A,_A5),(_A,_A6)))
if mibBuilder.loadTexts:trpzClSessClientAddressTableGroup.setStatus(_B)
trpzClientSessClientSessionTableGroupRev3=ObjectGroup((1,3,6,1,4,1,14525,4,4,1,2,2,9))
trpzClientSessClientSessionTableGroupRev3.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_V),(_A,_W),(_A,_X),(_A,_q),(_A,_r),(_A,_s),(_A,_A7),(_A,_A8),(_A,_A9)))
if mibBuilder.loadTexts:trpzClientSessClientSessionTableGroupRev3.setStatus(_B)
trpzClientSessionCompliance=ModuleCompliance((1,3,6,1,4,1,14525,4,4,1,2,1,1))
trpzClientSessionCompliance.setObjects((_A,_AA))
if mibBuilder.loadTexts:trpzClientSessionCompliance.setStatus(_D)
trpzClientSessionComplianceRev2=ModuleCompliance((1,3,6,1,4,1,14525,4,4,1,2,1,2))
trpzClientSessionComplianceRev2.setObjects(*((_A,_Y),(_A,_AB),(_A,_AC),(_A,_Z)))
if mibBuilder.loadTexts:trpzClientSessionComplianceRev2.setStatus(_D)
trpzClientSessionComplianceRev3=ModuleCompliance((1,3,6,1,4,1,14525,4,4,1,2,1,3))
trpzClientSessionComplianceRev3.setObjects(*((_A,_Y),(_A,_AD),(_A,_t),(_A,_Z)))
if mibBuilder.loadTexts:trpzClientSessionComplianceRev3.setStatus(_D)
trpzClientSessionComplianceRev4=ModuleCompliance((1,3,6,1,4,1,14525,4,4,1,2,1,4))
trpzClientSessionComplianceRev4.setObjects(*((_A,_Y),(_A,_AE),(_A,_t),(_A,_AF),(_A,_Z)))
if mibBuilder.loadTexts:trpzClientSessionComplianceRev4.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'TrpzEncryptionType':TrpzEncryptionType,'TrpzAuthMethod':TrpzAuthMethod,'TrpzSessState':TrpzSessState,'trpzClientSessionMib':trpzClientSessionMib,'trpzClientSessionObjects':trpzClientSessionObjects,'trpzClientSessionDataObjects':trpzClientSessionDataObjects,'trpzClSessClientSessionTable':trpzClSessClientSessionTable,'trpzClSessClientSessionEntry':trpzClSessClientSessionEntry,_a:trpzClSessClientSessMacAddress,_G:trpzClSessClientSessSessionId,_H:trpzClSessClientSessUsername,_I:trpzClSessClientSessIpAddress,_J:trpzClSessClientSessEncryptionType,_K:trpzClSessClientSessVlan,_L:trpzClSessClientSessApSerialNum,_M:trpzClSessClientSessRadioNum,_b:trpzClSessClientSessAccessType,_z:trpzClSessClientSessAuthMethod,_N:trpzClSessClientSessAuthServer,_c:trpzClSessClientSessPortOrNum,_O:trpzClSessClientSessVlanTag,_P:trpzClSessClientSessTimeStamp,_Q:trpzClSessClientSessSsid,_A0:trpzClSessClientSessState,_V:trpzClSessClientSessLoginType,_W:trpzClSessClientSessDot1xAuthMethod,_X:trpzClSessClientSessSessionState,_q:trpzClSessClientSessAccessMode,_r:trpzClSessClientSessApNum,_s:trpzClSessClientSessPhysPortNum,_A7:trpzClSessClientSessDeviceType,_A8:trpzClSessClientSessDeviceGroup,_A9:trpzClSessClientSessDeviceProfileName,'trpzClSessRoamingHistoryTable':trpzClSessRoamingHistoryTable,'trpzClSessRoamingHistoryEntry':trpzClSessRoamingHistoryEntry,_v:trpzClSessRoamHistMacAddress,_w:trpzClSessRoamHistIndex,_R:trpzClSessRoamHistApSerialNum,_S:trpzClSessRoamHistRadioNum,_d:trpzClSessRoamHistAccessType,_e:trpzClSessRoamHistApNumOrPort,_T:trpzClSessRoamHistIpAddress,_U:trpzClSessRoamHistTimeStamp,_A2:trpzClSessRoamHistAccessMode,_A3:trpzClSessRoamHistApNum,_A4:trpzClSessRoamHistPhysPortNum,'trpzClSessClientSessionStatisticsTable':trpzClSessClientSessionStatisticsTable,'trpzClSessClientSessionStatisticsEntry':trpzClSessClientSessionStatisticsEntry,_x:trpzClSessClientSessStatsMacAddress,_f:trpzClSessClientSessStatsUniPktIn,_g:trpzClSessClientSessStatsUniOctetIn,_h:trpzClSessClientSessStatsUniPktOut,_i:trpzClSessClientSessStatsUniOctetOut,_j:trpzClSessClientSessStatsMultiPktIn,_k:trpzClSessClientSessStatsMultiOctetIn,_l:trpzClSessClientSessStatsEncErrPkt,_m:trpzClSessClientSessStatsEncErrOctet,_n:trpzClSessClientSessStatsLastRate,_o:trpzClSessClientSessStatsLastRssi,_p:trpzClSessClientSessStatsLastSNR,_A1:trpzClSessTotalSessions,'trpzClSessClientAddressTable':trpzClSessClientAddressTable,'trpzClSessClientAddressEntry':trpzClSessClientAddressEntry,_y:trpzClSessClientAddressIndex,_A5:trpzClSessClientAddressType,_A6:trpzClSessClientAddressValue,'trpzClientSessionConformance':trpzClientSessionConformance,'trpzClientSessionCompliances':trpzClientSessionCompliances,'trpzClientSessionCompliance':trpzClientSessionCompliance,'trpzClientSessionComplianceRev2':trpzClientSessionComplianceRev2,'trpzClientSessionComplianceRev3':trpzClientSessionComplianceRev3,'trpzClientSessionComplianceRev4':trpzClientSessionComplianceRev4,'trpzClientSessionGroups':trpzClientSessionGroups,_AA:trpzClientSessionCommonGroup,_Y:trpzClientSessScalarsGroup,_AB:trpzClientSessClientSessionTableGroup,_AC:trpzClientSessRoamingHistoryTableGroup,_Z:trpzClientSessClientSessionStatisticsTableGroup,_AD:trpzClientSessClientSessionTableGroupRev2,_t:trpzClientSessRoamingHistoryTableGroupRev2,_AF:trpzClSessClientAddressTableGroup,_AE:trpzClientSessClientSessionTableGroupRev3})