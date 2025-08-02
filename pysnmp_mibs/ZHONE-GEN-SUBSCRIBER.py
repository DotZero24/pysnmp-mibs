_At='subVoiceIsdnSigDirectoryNumber'
_As='subVoiceIsdnSigEntryIndex'
_Ar='subVoiceIsdnSigHuntGrpEndPointIndex1'
_Aq='subVoiceVoipHotlineDN'
_Ap='subVoiceHotlineInitialTimer'
_Ao='subVoiceVoipAuthUsername'
_An='subVoiceTr008GroupId'
_Am='subVoiceTr008ChanNum'
_Al='subVoiceFeatureSetOne'
_Ak='subVoiceVoipPlarDestIpAddrType'
_Aj='subVoiceVoipPlarUdpPort'
_Ai='subVoiceVoipPLAR'
_Ah='subVoiceVoipPlarDestIpAddr'
_Ag='subVoiceIsdnSigHuntGrpEndPointIndex2'
_Af='subVoiceIsdnSigHuntGrpEndPointIndex3'
_Ae='subVoiceVoipUserName'
_Ad='subVoiceVoipIpInterface'
_Ac='subVoiceVoipDirectoryNumber'
_Ab='subVoiceVoipPreferredCodec'
_Aa='subVoiceVoipG711Fallback'
_AZ='subVoiceVoipFramesPerPacket'
_AY='subVoiceVoipG726ByteOrder'
_AX='subVoiceVoipPassword'
_AW='subVoiceDs1HuntGrpEndPointIndex2'
_AV='subVoicePotsHuntGrpEndPointIndex1'
_AU='subVoicePotsHuntGrpEndPointIndex2'
_AT='subVoicePotsHuntGrpEndPointIndex3'
_AS='subVoiceDs1HuntGrpEndPointIndex1'
_AR='subVoiceDs1HuntGrpEndPointIndex3'
_AQ='subVoiceHuntGroup'
_AP='subVoiceEbsLineGroupId'
_AO='subVoiceElcpAal2IsdnChannelId'
_AN='subVoiceElcpAal2PortType'
_AM='subVoiceElcpAal2PortId'
_AL='subVoiceElcpAal2Vci'
_AK='subVoiceElcpAal2Vpi'
_AJ='subVoiceElcpAal2LineGroupId'
_AI='subVoiceDs1LineGroupId'
_AH='subVoiceDs1Ds0ChannelID'
_AG='subVoiceIsdnChannelId'
_AF='subVoiceIsdnType'
_AE='subVoiceIsdnLineGroupId'
_AD='subVoicePotsLineGroupId'
_AC='subVoiceV52IsdnChannelId'
_AB='subVoiceV52UserType'
_AA='subVoiceV52UserPortId'
_A9='subVoiceV52InterfaceName'
_A8='subVoiceGr303IgCrv'
_A7='subVoiceGr303IgName'
_A6='subVoiceAal2Cid'
_A5='subVoiceAal2Vci'
_A4='subVoiceAal2Vpi'
_A3='subVoiceAal2LineGroupId'
_A2='subVoiceRowStatus'
_A1='subVoiceAdminStatus'
_A0='subVoiceConnectionDescription'
_z='subVoiceEndPoint2AddressIndex'
_y='subVoiceEndPoint1AddressIndex'
_x='subVoiceConnectionType'
_w='subDataRowStatus'
_v='subDataStatsStatus'
_u='subDataCurrentIpAddr'
_t='subDataIpAddrInUse'
_s='subDataMaxAddrAllowed'
_r='subDataUserPassword'
_q='subDataUserLogOnId'
_p='subDataIpIfOperStatus'
_o='subRowStatus'
_n='subNextVoiceConnectionIndex'
_m='subMaxCapableLineRate'
_l='subMaxAllowedLineRate'
_k='subIadType'
_j='subProviderId'
_i='subName'
_h='nextEndPointIndex'
_g='nextSubId'
_f='subVoiceTr008EndPointIndex'
_e='subVoiceIsdnSigEndPointIndex'
_d='subVoiceEbsEndPointIndex'
_c='T38FaxType'
_b='ZhoneCodecType'
_a='subVoiceVoipEndPointIndex'
_Z='subVoiceDs1EndPointIndex'
_Y='subVoiceIsdnEndPointIndex'
_X='subVoicePotsEndPointIndex'
_W='subVoiceV52EndPointIndex'
_V='subVoiceGr303EndPointIndex'
_U='subVoiceConnectionIndex'
_T='disabled'
_S='enabled'
_R='subDataIfIndex'
_Q='Kbits per second'
_P='ZhoneAdminString'
_O='InetAddressType'
_N='isdnBChannel'
_M='isdnDChannel'
_L='subVoiceAal2EndPointIndex'
_K='TruthValue'
_J='Unsigned32'
_I='subLgId'
_H='subId'
_G='read-only'
_F='not-accessible'
_E='read-create'
_D='Integer32'
_C='read-write'
_B='ZHONE-GEN-SUBSCRIBER'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AtmVcIdentifier,AtmVpIdentifier=mibBuilder.importSymbols('ATM-TC-MIB','AtmVcIdentifier','AtmVpIdentifier')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress',_O)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_K)
zhoneSubscriber,=mibBuilder.importSymbols('Zhone','zhoneSubscriber')
ZhoneAdminString,ZhoneRowStatus=mibBuilder.importSymbols('Zhone-TC',_P,'ZhoneRowStatus')
zhoneSubscriberRecords=ModuleIdentity((1,3,6,1,4,1,5504,3,4,1))
if mibBuilder.loadTexts:zhoneSubscriberRecords.setRevisions(('2014-10-01 10:00','2012-12-19 23:04','2011-12-25 23:19','2011-09-12 04:05','2010-06-08 02:53','2010-05-04 04:08','2009-06-26 03:20','2009-05-26 03:02','2008-05-27 17:23','2008-02-21 02:24','2007-12-26 14:43','2007-02-28 15:11','2006-02-03 10:42','2005-08-23 14:00','2005-05-19 16:18','2005-05-03 13:26','2005-02-25 17:39','2004-12-02 11:46','2004-05-26 12:09','2004-05-12 11:10','2004-04-21 11:37','2004-04-16 14:58','2004-03-29 11:33','2004-01-21 17:05','2004-01-07 09:48','2003-11-06 10:17','2003-07-28 11:16','2003-06-27 11:19','2003-05-30 14:13','2003-02-17 14:10','2003-02-03 13:40','2003-01-22 15:01','2002-06-24 17:01','2001-12-07 17:49','2001-10-29 15:46','2001-06-29 18:28','2000-11-15 12:52','2000-09-12 13:54'))
class ZhoneCodecType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('g711mu',1),('g711a',2),('g726',3),('g729a',4),('g723',5)))
class T38FaxType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('t38Udptl',1),('t38Rtp',2),('t38None',3)))
class _NextSubId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_NextSubId_Type.__name__=_D
_NextSubId_Object=MibScalar
nextSubId=_NextSubId_Object((1,3,6,1,4,1,5504,3,4,1,1),_NextSubId_Type())
nextSubId.setMaxAccess(_G)
if mibBuilder.loadTexts:nextSubId.setStatus(_A)
class _NextEndPointIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_NextEndPointIndex_Type.__name__=_D
_NextEndPointIndex_Object=MibScalar
nextEndPointIndex=_NextEndPointIndex_Object((1,3,6,1,4,1,5504,3,4,1,2),_NextEndPointIndex_Type())
nextEndPointIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:nextEndPointIndex.setStatus(_A)
_SubInfoTable_Object=MibTable
subInfoTable=_SubInfoTable_Object((1,3,6,1,4,1,5504,3,4,1,3))
if mibBuilder.loadTexts:subInfoTable.setStatus(_A)
_SubInfoEntry_Object=MibTableRow
subInfoEntry=_SubInfoEntry_Object((1,3,6,1,4,1,5504,3,4,1,3,1))
subInfoEntry.setIndexNames((0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:subInfoEntry.setStatus(_A)
class _SubId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SubId_Type.__name__=_D
_SubId_Object=MibTableColumn
subId=_SubId_Object((1,3,6,1,4,1,5504,3,4,1,3,1,1),_SubId_Type())
subId.setMaxAccess(_F)
if mibBuilder.loadTexts:subId.setStatus(_A)
class _SubLgId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SubLgId_Type.__name__=_D
_SubLgId_Object=MibTableColumn
subLgId=_SubLgId_Object((1,3,6,1,4,1,5504,3,4,1,3,1,2),_SubLgId_Type())
subLgId.setMaxAccess(_F)
if mibBuilder.loadTexts:subLgId.setStatus(_A)
_SubName_Type=ZhoneAdminString
_SubName_Object=MibTableColumn
subName=_SubName_Object((1,3,6,1,4,1,5504,3,4,1,3,1,3),_SubName_Type())
subName.setMaxAccess(_E)
if mibBuilder.loadTexts:subName.setStatus(_A)
_SubProviderId_Type=Integer32
_SubProviderId_Object=MibTableColumn
subProviderId=_SubProviderId_Object((1,3,6,1,4,1,5504,3,4,1,3,1,4),_SubProviderId_Type())
subProviderId.setMaxAccess(_E)
if mibBuilder.loadTexts:subProviderId.setStatus(_A)
class _SubIadType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('other',1),('zedge64T',2),('zedge64S',3),('zedge65',4),('zedge100',5),('matP',6),('zedgeBH2A',7),('zedgeH2A',8),('zedgeH2AO',9)))
_SubIadType_Type.__name__=_D
_SubIadType_Object=MibTableColumn
subIadType=_SubIadType_Object((1,3,6,1,4,1,5504,3,4,1,3,1,5),_SubIadType_Type())
subIadType.setMaxAccess(_E)
if mibBuilder.loadTexts:subIadType.setStatus(_A)
class _SubMaxAllowedLineRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SubMaxAllowedLineRate_Type.__name__=_D
_SubMaxAllowedLineRate_Object=MibTableColumn
subMaxAllowedLineRate=_SubMaxAllowedLineRate_Object((1,3,6,1,4,1,5504,3,4,1,3,1,6),_SubMaxAllowedLineRate_Type())
subMaxAllowedLineRate.setMaxAccess(_E)
if mibBuilder.loadTexts:subMaxAllowedLineRate.setStatus(_A)
if mibBuilder.loadTexts:subMaxAllowedLineRate.setUnits(_Q)
class _SubMaxCapableLineRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SubMaxCapableLineRate_Type.__name__=_D
_SubMaxCapableLineRate_Object=MibTableColumn
subMaxCapableLineRate=_SubMaxCapableLineRate_Object((1,3,6,1,4,1,5504,3,4,1,3,1,7),_SubMaxCapableLineRate_Type())
subMaxCapableLineRate.setMaxAccess(_E)
if mibBuilder.loadTexts:subMaxCapableLineRate.setStatus(_A)
if mibBuilder.loadTexts:subMaxCapableLineRate.setUnits(_Q)
class _SubNextVoiceConnectionIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SubNextVoiceConnectionIndex_Type.__name__=_D
_SubNextVoiceConnectionIndex_Object=MibTableColumn
subNextVoiceConnectionIndex=_SubNextVoiceConnectionIndex_Object((1,3,6,1,4,1,5504,3,4,1,3,1,8),_SubNextVoiceConnectionIndex_Type())
subNextVoiceConnectionIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:subNextVoiceConnectionIndex.setStatus(_A)
_SubRowStatus_Type=ZhoneRowStatus
_SubRowStatus_Object=MibTableColumn
subRowStatus=_SubRowStatus_Object((1,3,6,1,4,1,5504,3,4,1,3,1,9),_SubRowStatus_Type())
subRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:subRowStatus.setStatus(_A)
_SubDataConnectionTable_Object=MibTable
subDataConnectionTable=_SubDataConnectionTable_Object((1,3,6,1,4,1,5504,3,4,1,4))
if mibBuilder.loadTexts:subDataConnectionTable.setStatus(_A)
_SubDataConnectionEntry_Object=MibTableRow
subDataConnectionEntry=_SubDataConnectionEntry_Object((1,3,6,1,4,1,5504,3,4,1,4,1))
subDataConnectionEntry.setIndexNames((0,_B,_H),(0,_B,_I),(0,_B,_R))
if mibBuilder.loadTexts:subDataConnectionEntry.setStatus(_A)
_SubDataIfIndex_Type=InterfaceIndex
_SubDataIfIndex_Object=MibTableColumn
subDataIfIndex=_SubDataIfIndex_Object((1,3,6,1,4,1,5504,3,4,1,4,1,1),_SubDataIfIndex_Type())
subDataIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:subDataIfIndex.setStatus(_A)
class _SubDataIpIfOperStatus_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('up',1),('down',2),('testing',3),('unknown',4),('dormant',5),('notPresent',6),('lowerLayerDown',7)))
_SubDataIpIfOperStatus_Type.__name__=_D
_SubDataIpIfOperStatus_Object=MibTableColumn
subDataIpIfOperStatus=_SubDataIpIfOperStatus_Object((1,3,6,1,4,1,5504,3,4,1,4,1,2),_SubDataIpIfOperStatus_Type())
subDataIpIfOperStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:subDataIpIfOperStatus.setStatus(_A)
_SubDataUserLogOnId_Type=ZhoneAdminString
_SubDataUserLogOnId_Object=MibTableColumn
subDataUserLogOnId=_SubDataUserLogOnId_Object((1,3,6,1,4,1,5504,3,4,1,4,1,3),_SubDataUserLogOnId_Type())
subDataUserLogOnId.setMaxAccess(_E)
if mibBuilder.loadTexts:subDataUserLogOnId.setStatus(_A)
_SubDataUserPassword_Type=ZhoneAdminString
_SubDataUserPassword_Object=MibTableColumn
subDataUserPassword=_SubDataUserPassword_Object((1,3,6,1,4,1,5504,3,4,1,4,1,4),_SubDataUserPassword_Type())
subDataUserPassword.setMaxAccess(_E)
if mibBuilder.loadTexts:subDataUserPassword.setStatus(_A)
class _SubDataMaxAddrAllowed_Type(Integer32):defaultValue=1
_SubDataMaxAddrAllowed_Type.__name__=_D
_SubDataMaxAddrAllowed_Object=MibTableColumn
subDataMaxAddrAllowed=_SubDataMaxAddrAllowed_Object((1,3,6,1,4,1,5504,3,4,1,4,1,5),_SubDataMaxAddrAllowed_Type())
subDataMaxAddrAllowed.setMaxAccess(_E)
if mibBuilder.loadTexts:subDataMaxAddrAllowed.setStatus(_A)
_SubDataIpAddrInUse_Type=Integer32
_SubDataIpAddrInUse_Object=MibTableColumn
subDataIpAddrInUse=_SubDataIpAddrInUse_Object((1,3,6,1,4,1,5504,3,4,1,4,1,6),_SubDataIpAddrInUse_Type())
subDataIpAddrInUse.setMaxAccess(_G)
if mibBuilder.loadTexts:subDataIpAddrInUse.setStatus(_A)
_SubDataCurrentIpAddr_Type=IpAddress
_SubDataCurrentIpAddr_Object=MibTableColumn
subDataCurrentIpAddr=_SubDataCurrentIpAddr_Object((1,3,6,1,4,1,5504,3,4,1,4,1,7),_SubDataCurrentIpAddr_Type())
subDataCurrentIpAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:subDataCurrentIpAddr.setStatus(_A)
class _SubDataStatsStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_T,2)))
_SubDataStatsStatus_Type.__name__=_D
_SubDataStatsStatus_Object=MibTableColumn
subDataStatsStatus=_SubDataStatsStatus_Object((1,3,6,1,4,1,5504,3,4,1,4,1,8),_SubDataStatsStatus_Type())
subDataStatsStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:subDataStatsStatus.setStatus(_A)
_SubDataRowStatus_Type=ZhoneRowStatus
_SubDataRowStatus_Object=MibTableColumn
subDataRowStatus=_SubDataRowStatus_Object((1,3,6,1,4,1,5504,3,4,1,4,1,9),_SubDataRowStatus_Type())
subDataRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:subDataRowStatus.setStatus(_A)
_SubVoiceConnectionTable_Object=MibTable
subVoiceConnectionTable=_SubVoiceConnectionTable_Object((1,3,6,1,4,1,5504,3,4,1,5))
if mibBuilder.loadTexts:subVoiceConnectionTable.setStatus(_A)
_SubVoiceConnectionEntry_Object=MibTableRow
subVoiceConnectionEntry=_SubVoiceConnectionEntry_Object((1,3,6,1,4,1,5504,3,4,1,5,1))
subVoiceConnectionEntry.setIndexNames((0,_B,_H),(0,_B,_I),(0,_B,_U))
if mibBuilder.loadTexts:subVoiceConnectionEntry.setStatus(_A)
class _SubVoiceConnectionIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SubVoiceConnectionIndex_Type.__name__=_D
_SubVoiceConnectionIndex_Object=MibTableColumn
subVoiceConnectionIndex=_SubVoiceConnectionIndex_Object((1,3,6,1,4,1,5504,3,4,1,5,1,1),_SubVoiceConnectionIndex_Type())
subVoiceConnectionIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:subVoiceConnectionIndex.setStatus(_A)
class _SubVoiceConnectionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,19,20)));namedValues=NamedValues(*(('aal2ToGr303',1),('aal2ToV52',2),('voipToGr303',3),('potsToAal2',4),('isdnToAal2',5),('potsToGr303',6),('potsToV52',7),('voipToDs1',8),('sipToGr303',9),('voipToV52',10),('elcpAal2ToV52',11),('isdnToV52',12),('ebsToGr303',13),('voipToPots',14),('isdnsigToVoip',15),('potsToDs1',16),('voipToTr008',18),('voipToEbs',19),('isdnToVoip',20)))
_SubVoiceConnectionType_Type.__name__=_D
_SubVoiceConnectionType_Object=MibTableColumn
subVoiceConnectionType=_SubVoiceConnectionType_Object((1,3,6,1,4,1,5504,3,4,1,5,1,2),_SubVoiceConnectionType_Type())
subVoiceConnectionType.setMaxAccess(_E)
if mibBuilder.loadTexts:subVoiceConnectionType.setStatus(_A)
class _SubVoiceEndPoint1AddressIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SubVoiceEndPoint1AddressIndex_Type.__name__=_D
_SubVoiceEndPoint1AddressIndex_Object=MibTableColumn
subVoiceEndPoint1AddressIndex=_SubVoiceEndPoint1AddressIndex_Object((1,3,6,1,4,1,5504,3,4,1,5,1,3),_SubVoiceEndPoint1AddressIndex_Type())
subVoiceEndPoint1AddressIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:subVoiceEndPoint1AddressIndex.setStatus(_A)
class _SubVoiceEndPoint2AddressIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SubVoiceEndPoint2AddressIndex_Type.__name__=_D
_SubVoiceEndPoint2AddressIndex_Object=MibTableColumn
subVoiceEndPoint2AddressIndex=_SubVoiceEndPoint2AddressIndex_Object((1,3,6,1,4,1,5504,3,4,1,5,1,4),_SubVoiceEndPoint2AddressIndex_Type())
subVoiceEndPoint2AddressIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:subVoiceEndPoint2AddressIndex.setStatus(_A)
_SubVoiceConnectionDescription_Type=ZhoneAdminString
_SubVoiceConnectionDescription_Object=MibTableColumn
subVoiceConnectionDescription=_SubVoiceConnectionDescription_Object((1,3,6,1,4,1,5504,3,4,1,5,1,5),_SubVoiceConnectionDescription_Type())
subVoiceConnectionDescription.setMaxAccess(_E)
if mibBuilder.loadTexts:subVoiceConnectionDescription.setStatus(_A)
class _SubVoiceAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_T,2)))
_SubVoiceAdminStatus_Type.__name__=_D
_SubVoiceAdminStatus_Object=MibTableColumn
subVoiceAdminStatus=_SubVoiceAdminStatus_Object((1,3,6,1,4,1,5504,3,4,1,5,1,6),_SubVoiceAdminStatus_Type())
subVoiceAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:subVoiceAdminStatus.setStatus(_A)
_SubVoiceRowStatus_Type=ZhoneRowStatus
_SubVoiceRowStatus_Object=MibTableColumn
subVoiceRowStatus=_SubVoiceRowStatus_Object((1,3,6,1,4,1,5504,3,4,1,5,1,7),_SubVoiceRowStatus_Type())
subVoiceRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:subVoiceRowStatus.setStatus(_A)
_SubVoiceHuntGroup_Type=TruthValue
_SubVoiceHuntGroup_Object=MibTableColumn
subVoiceHuntGroup=_SubVoiceHuntGroup_Object((1,3,6,1,4,1,5504,3,4,1,5,1,8),_SubVoiceHuntGroup_Type())
subVoiceHuntGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:subVoiceHuntGroup.setStatus(_A)
class _SubVoiceFeatureSetOne_Type(Bits):defaultBinValue='11001';namedValues=NamedValues(*(('hookflash',0),('onhooksignaling',1),('alwaysoffhook',2),('plar',3),('callwait',4),('calltransfer',5),('conference',6),('lss-rb',7),('voiceonly',8),('hotline',9),('warmline',10),('lss-tone',11),('dtmf-rfc2833',12),('dtmf-inband',13),('cod',14),('dataonly',15),('centrex',16)))
_SubVoiceFeatureSetOne_Type.__name__='Bits'
_SubVoiceFeatureSetOne_Object=MibTableColumn
subVoiceFeatureSetOne=_SubVoiceFeatureSetOne_Object((1,3,6,1,4,1,5504,3,4,1,5,1,9),_SubVoiceFeatureSetOne_Type())
subVoiceFeatureSetOne.setMaxAccess(_C)
if mibBuilder.loadTexts:subVoiceFeatureSetOne.setStatus(_A)
_SubVoiceAal2Table_Object=MibTable
subVoiceAal2Table=_SubVoiceAal2Table_Object((1,3,6,1,4,1,5504,3,4,1,6))
if mibBuilder.loadTexts:subVoiceAal2Table.setStatus(_A)
_SubVoiceAal2Entry_Object=MibTableRow
subVoiceAal2Entry=_SubVoiceAal2Entry_Object((1,3,6,1,4,1,5504,3,4,1,6,1))
subVoiceAal2Entry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:subVoiceAal2Entry.setStatus(_A)
class _SubVoiceAal2EndPointIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SubVoiceAal2EndPointIndex_Type.__name__=_D
_SubVoiceAal2EndPointIndex_Object=MibTableColumn
subVoiceAal2EndPointIndex=_SubVoiceAal2EndPointIndex_Object((1,3,6,1,4,1,5504,3,4,1,6,1,1),_SubVoiceAal2EndPointIndex_Type())
subVoiceAal2EndPointIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:subVoiceAal2EndPointIndex.setStatus(_A)
_SubVoiceAal2LineGroupId_Type=Integer32
_SubVoiceAal2LineGroupId_Object=MibTableColumn
subVoiceAal2LineGroupId=_SubVoiceAal2LineGroupId_Object((1,3,6,1,4,1,5504,3,4,1,6,1,2),_SubVoiceAal2LineGroupId_Type())
subVoiceAal2LineGroupId.setMaxAccess(_C)
if mibBuilder.loadTexts:subVoiceAal2LineGroupId.setStatus(_A)
_SubVoiceAal2Vpi_Type=AtmVpIdentifier
_SubVoiceAal2Vpi_Object=MibTableColumn
subVoiceAal2Vpi=_SubVoiceAal2Vpi_Object((1,3,6,1,4,1,5504,3,4,1,6,1,3),_SubVoiceAal2Vpi_Type())
subVoiceAal2Vpi.setMaxAccess(_C)
if mibBuilder.loadTexts:subVoiceAal2Vpi.setStatus(_A)
_SubVoiceAal2Vci_Type=AtmVcIdentifier
_SubVoiceAal2Vci_Object=MibTableColumn
subVoiceAal2Vci=_SubVoiceAal2Vci_Object((1,3,6,1,4,1,5504,3,4,1,6,1,4),_SubVoiceAal2Vci_Type())
subVoiceAal2Vci.setMaxAccess(_C)
if mibBuilder.loadTexts:subVoiceAal2Vci.setStatus(_A)
class _SubVoiceAal2Cid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SubVoiceAal2Cid_Type.__name__=_D
_SubVoiceAal2Cid_Object=MibTableColumn
subVoiceAal2Cid=_SubVoiceAal2Cid_Object((1,3,6,1,4,1,5504,3,4,1,6,1,5),_SubVoiceAal2Cid_Type())
subVoiceAal2Cid.setMaxAccess(_C)
if mibBuilder.loadTexts:subVoiceAal2Cid.setStatus(_A)
_SubVoiceGr303Table_Object=MibTable
subVoiceGr303Table=_SubVoiceGr303Table_Object((1,3,6,1,4,1,5504,3,4,1,7))
if mibBuilder.loadTexts:subVoiceGr303Table.setStatus(_A)
_SubVoiceGr303Entry_Object=MibTableRow
subVoiceGr303Entry=_SubVoiceGr303Entry_Object((1,3,6,1,4,1,5504,3,4,1,7,1))
subVoiceGr303Entry.setIndexNames((0,_B,_V))
if mibBuilder.loadTexts:subVoiceGr303Entry.setStatus(_A)
class _SubVoiceGr303EndPointIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SubVoiceGr303EndPointIndex_Type.__name__=_D
_SubVoiceGr303EndPointIndex_Object=MibTableColumn
subVoiceGr303EndPointIndex=_SubVoiceGr303EndPointIndex_Object((1,3,6,1,4,1,5504,3,4,1,7,1,1),_SubVoiceGr303EndPointIndex_Type())
subVoiceGr303EndPointIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:subVoiceGr303EndPointIndex.setStatus(_A)
_SubVoiceGr303IgName_Type=ZhoneAdminString
_SubVoiceGr303IgName_Object=MibTableColumn
subVoiceGr303IgName=_SubVoiceGr303IgName_Object((1,3,6,1,4,1,5504,3,4,1,7,1,2),_SubVoiceGr303IgName_Type())
subVoiceGr303IgName.setMaxAccess(_C)
if mibBuilder.loadTexts:subVoiceGr303IgName.setStatus(_A)
class _SubVoiceGr303IgCrv_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2048))
_SubVoiceGr303IgCrv_Type.__name__=_D
_SubVoiceGr303IgCrv_Object=MibTableColumn
subVoiceGr303IgCrv=_SubVoiceGr303IgCrv_Object((1,3,6,1,4,1,5504,3,4,1,7,1,3),_SubVoiceGr303IgCrv_Type())
subVoiceGr303IgCrv.setMaxAccess(_C)
if mibBuilder.loadTexts:subVoiceGr303IgCrv.setStatus(_A)
_SubVoiceV52Table_Object=MibTable
subVoiceV52Table=_SubVoiceV52Table_Object((1,3,6,1,4,1,5504,3,4,1,8))
if mibBuilder.loadTexts:subVoiceV52Table.setStatus(_A)
_SubVoiceV52Entry_Object=MibTableRow
subVoiceV52Entry=_SubVoiceV52Entry_Object((1,3,6,1,4,1,5504,3,4,1,8,1))
subVoiceV52Entry.setIndexNames((0,_B,_W))
if mibBuilder.loadTexts:subVoiceV52Entry.setStatus(_A)
class _SubVoiceV52EndPointIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SubVoiceV52EndPointIndex_Type.__name__=_D
_SubVoiceV52EndPointIndex_Object=MibTableColumn
subVoiceV52EndPointIndex=_SubVoiceV52EndPointIndex_Object((1,3,6,1,4,1,5504,3,4,1,8,1,1),_SubVoiceV52EndPointIndex_Type())
subVoiceV52EndPointIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:subVoiceV52EndPointIndex.setStatus(_A)
_SubVoiceV52InterfaceName_Type=ZhoneAdminString
_SubVoiceV52InterfaceName_Object=MibTableColumn
subVoiceV52InterfaceName=_SubVoiceV52InterfaceName_Object((1,3,6,1,4,1,5504,3,4,1,8,1,2),_SubVoiceV52InterfaceName_Type())
subVoiceV52InterfaceName.setMaxAccess(_C)
if mibBuilder.loadTexts:subVoiceV52InterfaceName.setStatus(_A)
class _SubVoiceV52UserPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SubVoiceV52UserPortId_Type.__name__=_D
_SubVoiceV52UserPortId_Object=MibTableColumn
subVoiceV52UserPortId=_SubVoiceV52UserPortId_Object((1,3,6,1,4,1,5504,3,4,1,8,1,3),_SubVoiceV52UserPortId_Type())
subVoiceV52UserPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:subVoiceV52UserPortId.setStatus(_A)
class _SubVoiceV52UserType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('pots',1),(_M,2),(_N,3)))
_SubVoiceV52UserType_Type.__name__=_D
_SubVoiceV52UserType_Object=MibTableColumn
subVoiceV52UserType=_SubVoiceV52UserType_Object((1,3,6,1,4,1,5504,3,4,1,8,1,4),_SubVoiceV52UserType_Type())
subVoiceV52UserType.setMaxAccess(_C)
if mibBuilder.loadTexts:subVoiceV52UserType.setStatus(_A)
class _SubVoiceV52IsdnChannelId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_SubVoiceV52IsdnChannelId_Type.__name__=_D
_SubVoiceV52IsdnChannelId_Object=MibTableColumn
subVoiceV52IsdnChannelId=_SubVoiceV52IsdnChannelId_Object((1,3,6,1,4,1,5504,3,4,1,8,1,5),_SubVoiceV52IsdnChannelId_Type())
subVoiceV52IsdnChannelId.setMaxAccess(_C)
if mibBuilder.loadTexts:subVoiceV52IsdnChannelId.setStatus(_A)
_SubVoicePotsTable_Object=MibTable
subVoicePotsTable=_SubVoicePotsTable_Object((1,3,6,1,4,1,5504,3,4,1,9))
if mibBuilder.loadTexts:subVoicePotsTable.setStatus(_A)
_SubVoicePotsEntry_Object=MibTableRow
subVoicePotsEntry=_SubVoicePotsEntry_Object((1,3,6,1,4,1,5504,3,4,1,9,1))
subVoicePotsEntry.setIndexNames((0,_B,_X))
if mibBuilder.loadTexts:subVoicePotsEntry.setStatus(_A)
class _SubVoicePotsEndPointIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SubVoicePotsEndPointIndex_Type.__name__=_D
_SubVoicePotsEndPointIndex_Object=MibTableColumn
subVoicePotsEndPointIndex=_SubVoicePotsEndPointIndex_Object((1,3,6,1,4,1,5504,3,4,1,9,1,1),_SubVoicePotsEndPointIndex_Type())
subVoicePotsEndPointIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:subVoicePotsEndPointIndex.setStatus(_A)
_SubVoicePotsLineGroupId_Type=Integer32
_SubVoicePotsLineGroupId_Object=MibTableColumn
subVoicePotsLineGroupId=_SubVoicePotsLineGroupId_Object((1,3,6,1,4,1,5504,3,4,1,9,1,2),_SubVoicePotsLineGroupId_Type())
subVoicePotsLineGroupId.setMaxAccess(_C)
if mibBuilder.loadTexts:subVoicePotsLineGroupId.setStatus(_A)
_SubVoicePotsHuntGrpEndPointIndex1_Type=Integer32
_SubVoicePotsHuntGrpEndPointIndex1_Object=MibTableColumn
subVoicePotsHuntGrpEndPointIndex1=_SubVoicePotsHuntGrpEndPointIndex1_Object((1,3,6,1,4,1,5504,3,4,1,9,1,3),_SubVoicePotsHuntGrpEndPointIndex1_Type())
subVoicePotsHuntGrpEndPointIndex1.setMaxAccess(_C)
if mibBuilder.loadTexts:subVoicePotsHuntGrpEndPointIndex1.setStatus(_A)
_SubVoicePotsHuntGrpEndPointIndex2_Type=Integer32
_SubVoicePotsHuntGrpEndPointIndex2_Object=MibTableColumn
subVoicePotsHuntGrpEndPointIndex2=_SubVoicePotsHuntGrpEndPointIndex2_Object((1,3,6,1,4,1,5504,3,4,1,9,1,4),_SubVoicePotsHuntGrpEndPointIndex2_Type())
subVoicePotsHuntGrpEndPointIndex2.setMaxAccess(_C)
if mibBuilder.loadTexts:subVoicePotsHuntGrpEndPointIndex2.setStatus(_A)
_SubVoicePotsHuntGrpEndPointIndex3_Type=Integer32
_SubVoicePotsHuntGrpEndPointIndex3_Object=MibTableColumn
subVoicePotsHuntGrpEndPointIndex3=_SubVoicePotsHuntGrpEndPointIndex3_Object((1,3,6,1,4,1,5504,3,4,1,9,1,5),_SubVoicePotsHuntGrpEndPointIndex3_Type())
subVoicePotsHuntGrpEndPointIndex3.setMaxAccess(_C)
if mibBuilder.loadTexts:subVoicePotsHuntGrpEndPointIndex3.setStatus(_A)
_SubVoiceIsdnTable_Object=MibTable
subVoiceIsdnTable=_SubVoiceIsdnTable_Object((1,3,6,1,4,1,5504,3,4,1,10))
if mibBuilder.loadTexts:subVoiceIsdnTable.setStatus(_A)
_SubVoiceIsdnEntry_Object=MibTableRow
subVoiceIsdnEntry=_SubVoiceIsdnEntry_Object((1,3,6,1,4,1,5504,3,4,1,10,1))
subVoiceIsdnEntry.setIndexNames((0,_B,_Y))
if mibBuilder.loadTexts:subVoiceIsdnEntry.setStatus(_A)
class _SubVoiceIsdnEndPointIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SubVoiceIsdnEndPointIndex_Type.__name__=_D
_SubVoiceIsdnEndPointIndex_Object=MibTableColumn
subVoiceIsdnEndPointIndex=_SubVoiceIsdnEndPointIndex_Object((1,3,6,1,4,1,5504,3,4,1,10,1,1),_SubVoiceIsdnEndPointIndex_Type())
subVoiceIsdnEndPointIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:subVoiceIsdnEndPointIndex.setStatus(_A)
_SubVoiceIsdnLineGroupId_Type=Integer32
_SubVoiceIsdnLineGroupId_Object=MibTableColumn
subVoiceIsdnLineGroupId=_SubVoiceIsdnLineGroupId_Object((1,3,6,1,4,1,5504,3,4,1,10,1,2),_SubVoiceIsdnLineGroupId_Type())
subVoiceIsdnLineGroupId.setMaxAccess(_C)
if mibBuilder.loadTexts:subVoiceIsdnLineGroupId.setStatus(_A)
class _SubVoiceIsdnType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_SubVoiceIsdnType_Type.__name__=_D
_SubVoiceIsdnType_Object=MibTableColumn
subVoiceIsdnType=_SubVoiceIsdnType_Object((1,3,6,1,4,1,5504,3,4,1,10,1,3),_SubVoiceIsdnType_Type())
subVoiceIsdnType.setMaxAccess(_C)
if mibBuilder.loadTexts:subVoiceIsdnType.setStatus(_A)
class _SubVoiceIsdnChannelId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_SubVoiceIsdnChannelId_Type.__name__=_D
_SubVoiceIsdnChannelId_Object=MibTableColumn
subVoiceIsdnChannelId=_SubVoiceIsdnChannelId_Object((1,3,6,1,4,1,5504,3,4,1,10,1,4),_SubVoiceIsdnChannelId_Type())
subVoiceIsdnChannelId.setMaxAccess(_C)
if mibBuilder.loadTexts:subVoiceIsdnChannelId.setStatus(_A)
_SubVoiceDs1Table_Object=MibTable
subVoiceDs1Table=_SubVoiceDs1Table_Object((1,3,6,1,4,1,5504,3,4,1,12))
if mibBuilder.loadTexts:subVoiceDs1Table.setStatus(_A)
_SubVoiceDs1Entry_Object=MibTableRow
subVoiceDs1Entry=_SubVoiceDs1Entry_Object((1,3,6,1,4,1,5504,3,4,1,12,1))
subVoiceDs1Entry.setIndexNames((0,_B,_Z))
if mibBuilder.loadTexts:subVoiceDs1Entry.setStatus(_A)
class _SubVoiceDs1EndPointIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SubVoiceDs1EndPointIndex_Type.__name__=_D
_SubVoiceDs1EndPointIndex_Object=MibTableColumn
subVoiceDs1EndPointIndex=_SubVoiceDs1EndPointIndex_Object((1,3,6,1,4,1,5504,3,4,1,12,1,1),_SubVoiceDs1EndPointIndex_Type())
subVoiceDs1EndPointIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:subVoiceDs1EndPointIndex.setStatus(_A)
class _SubVoiceDs1Ds0ChannelID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_SubVoiceDs1Ds0ChannelID_Type.__name__=_D
_SubVoiceDs1Ds0ChannelID_Object=MibTableColumn
subVoiceDs1Ds0ChannelID=_SubVoiceDs1Ds0ChannelID_Object((1,3,6,1,4,1,5504,3,4,1,12,1,2),_SubVoiceDs1Ds0ChannelID_Type())
subVoiceDs1Ds0ChannelID.setMaxAccess(_C)
if mibBuilder.loadTexts:subVoiceDs1Ds0ChannelID.setStatus(_A)
_SubVoiceDs1LineGroupId_Type=InterfaceIndex
_SubVoiceDs1LineGroupId_Object=MibTableColumn
subVoiceDs1LineGroupId=_SubVoiceDs1LineGroupId_Object((1,3,6,1,4,1,5504,3,4,1,12,1,3),_SubVoiceDs1LineGroupId_Type())
subVoiceDs1LineGroupId.setMaxAccess(_C)
if mibBuilder.loadTexts:subVoiceDs1LineGroupId.setStatus(_A)
_SubVoiceDs1HuntGrpEndPointIndex1_Type=Integer32
_SubVoiceDs1HuntGrpEndPointIndex1_Object=MibTableColumn
subVoiceDs1HuntGrpEndPointIndex1=_SubVoiceDs1HuntGrpEndPointIndex1_Object((1,3,6,1,4,1,5504,3,4,1,12,1,4),_SubVoiceDs1HuntGrpEndPointIndex1_Type())
subVoiceDs1HuntGrpEndPointIndex1.setMaxAccess(_C)
if mibBuilder.loadTexts:subVoiceDs1HuntGrpEndPointIndex1.setStatus(_A)
_SubVoiceDs1HuntGrpEndPointIndex2_Type=Integer32
_SubVoiceDs1HuntGrpEndPointIndex2_Object=MibTableColumn
subVoiceDs1HuntGrpEndPointIndex2=_SubVoiceDs1HuntGrpEndPointIndex2_Object((1,3,6,1,4,1,5504,3,4,1,12,1,5),_SubVoiceDs1HuntGrpEndPointIndex2_Type())
subVoiceDs1HuntGrpEndPointIndex2.setMaxAccess(_C)
if mibBuilder.loadTexts:subVoiceDs1HuntGrpEndPointIndex2.setStatus(_A)
_SubVoiceDs1HuntGrpEndPointIndex3_Type=Integer32
_SubVoiceDs1HuntGrpEndPointIndex3_Object=MibTableColumn
subVoiceDs1HuntGrpEndPointIndex3=_SubVoiceDs1HuntGrpEndPointIndex3_Object((1,3,6,1,4,1,5504,3,4,1,12,1,6),_SubVoiceDs1HuntGrpEndPointIndex3_Type())
subVoiceDs1HuntGrpEndPointIndex3.setMaxAccess(_C)
if mibBuilder.loadTexts:subVoiceDs1HuntGrpEndPointIndex3.setStatus(_A)
_SubVoiceVoipTable_Object=MibTable
subVoiceVoipTable=_SubVoiceVoipTable_Object((1,3,6,1,4,1,5504,3,4,1,13))
if mibBuilder.loadTexts:subVoiceVoipTable.setStatus(_A)
_SubVoiceVoipEntry_Object=MibTableRow
subVoiceVoipEntry=_SubVoiceVoipEntry_Object((1,3,6,1,4,1,5504,3,4,1,13,1))
subVoiceVoipEntry.setIndexNames((0,_B,_a))
if mibBuilder.loadTexts:subVoiceVoipEntry.setStatus(_A)
class _SubVoiceVoipEndPointIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SubVoiceVoipEndPointIndex_Type.__name__=_D
_SubVoiceVoipEndPointIndex_Object=MibTableColumn
subVoiceVoipEndPointIndex=_SubVoiceVoipEndPointIndex_Object((1,3,6,1,4,1,5504,3,4,1,13,1,1),_SubVoiceVoipEndPointIndex_Type())
subVoiceVoipEndPointIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:subVoiceVoipEndPointIndex.setStatus(_A)
_SubVoiceVoipUserName_Type=SnmpAdminString
_SubVoiceVoipUserName_Object=MibTableColumn
subVoiceVoipUserName=_SubVoiceVoipUserName_Object((1,3,6,1,4,1,5504,3,4,1,13,1,2),_SubVoiceVoipUserName_Type())
subVoiceVoipUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:subVoiceVoipUserName.setStatus(_A)
_SubVoiceVoipDirectoryNumber_Type=ZhoneAdminString
_SubVoiceVoipDirectoryNumber_Object=MibTableColumn
subVoiceVoipDirectoryNumber=_SubVoiceVoipDirectoryNumber_Object((1,3,6,1,4,1,5504,3,4,1,13,1,3),_SubVoiceVoipDirectoryNumber_Type())
subVoiceVoipDirectoryNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:subVoiceVoipDirectoryNumber.setStatus(_A)
_SubVoiceVoipIpInterface_Type=InterfaceIndexOrZero
_SubVoiceVoipIpInterface_Object=MibTableColumn
subVoiceVoipIpInterface=_SubVoiceVoipIpInterface_Object((1,3,6,1,4,1,5504,3,4,1,13,1,4),_SubVoiceVoipIpInterface_Type())
subVoiceVoipIpInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:subVoiceVoipIpInterface.setStatus(_A)
class _SubVoiceVoipPreferredCodec_Type(ZhoneCodecType):defaultValue=1
_SubVoiceVoipPreferredCodec_Type.__name__=_b
_SubVoiceVoipPreferredCodec_Object=MibTableColumn
subVoiceVoipPreferredCodec=_SubVoiceVoipPreferredCodec_Object((1,3,6,1,4,1,5504,3,4,1,13,1,5),_SubVoiceVoipPreferredCodec_Type())
subVoiceVoipPreferredCodec.setMaxAccess(_C)
if mibBuilder.loadTexts:subVoiceVoipPreferredCodec.setStatus(_A)
class _SubVoiceVoipG711Fallback_Type(TruthValue):defaultValue=1
_SubVoiceVoipG711Fallback_Type.__name__=_K
_SubVoiceVoipG711Fallback_Object=MibTableColumn
subVoiceVoipG711Fallback=_SubVoiceVoipG711Fallback_Object((1,3,6,1,4,1,5504,3,4,1,13,1,6),_SubVoiceVoipG711Fallback_Type())
subVoiceVoipG711Fallback.setMaxAccess(_C)
if mibBuilder.loadTexts:subVoiceVoipG711Fallback.setStatus(_A)
class _SubVoiceVoipFramesPerPacket_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_SubVoiceVoipFramesPerPacket_Type.__name__=_D
_SubVoiceVoipFramesPerPacket_Object=MibTableColumn
subVoiceVoipFramesPerPacket=_SubVoiceVoipFramesPerPacket_Object((1,3,6,1,4,1,5504,3,4,1,13,1,8),_SubVoiceVoipFramesPerPacket_Type())
subVoiceVoipFramesPerPacket.setMaxAccess(_C)
if mibBuilder.loadTexts:subVoiceVoipFramesPerPacket.setStatus(_A)
class _SubVoiceVoipG726ByteOrder_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('bigEndian',1),('littleEndian',2)))
_SubVoiceVoipG726ByteOrder_Type.__name__=_D
_SubVoiceVoipG726ByteOrder_Object=MibTableColumn
subVoiceVoipG726ByteOrder=_SubVoiceVoipG726ByteOrder_Object((1,3,6,1,4,1,5504,3,4,1,13,1,9),_SubVoiceVoipG726ByteOrder_Type())
subVoiceVoipG726ByteOrder.setMaxAccess(_C)
if mibBuilder.loadTexts:subVoiceVoipG726ByteOrder.setStatus(_A)
_SubVoiceVoipPassword_Type=ZhoneAdminString
_SubVoiceVoipPassword_Object=MibTableColumn
subVoiceVoipPassword=_SubVoiceVoipPassword_Object((1,3,6,1,4,1,5504,3,4,1,13,1,10),_SubVoiceVoipPassword_Type())
subVoiceVoipPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:subVoiceVoipPassword.setStatus(_A)
class _SubVoiceVoipPLAR_Type(TruthValue):defaultValue=2
_SubVoiceVoipPLAR_Type.__name__=_K
_SubVoiceVoipPLAR_Object=MibTableColumn
subVoiceVoipPLAR=_SubVoiceVoipPLAR_Object((1,3,6,1,4,1,5504,3,4,1,13,1,11),_SubVoiceVoipPLAR_Type())
subVoiceVoipPLAR.setMaxAccess(_G)
if mibBuilder.loadTexts:subVoiceVoipPLAR.setStatus(_A)
class _SubVoiceVoipPlarDestIpAddrType_Type(InetAddressType):defaultValue=1
_SubVoiceVoipPlarDestIpAddrType_Type.__name__=_O
_SubVoiceVoipPlarDestIpAddrType_Object=MibTableColumn
subVoiceVoipPlarDestIpAddrType=_SubVoiceVoipPlarDestIpAddrType_Object((1,3,6,1,4,1,5504,3,4,1,13,1,12),_SubVoiceVoipPlarDestIpAddrType_Type())
subVoiceVoipPlarDestIpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:subVoiceVoipPlarDestIpAddrType.setStatus(_A)
_SubVoiceVoipPlarDestIpAddr_Type=InetAddress
_SubVoiceVoipPlarDestIpAddr_Object=MibTableColumn
subVoiceVoipPlarDestIpAddr=_SubVoiceVoipPlarDestIpAddr_Object((1,3,6,1,4,1,5504,3,4,1,13,1,13),_SubVoiceVoipPlarDestIpAddr_Type())
subVoiceVoipPlarDestIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:subVoiceVoipPlarDestIpAddr.setStatus(_A)
class _SubVoiceVoipPlarUdpPort_Type(Integer32):defaultValue=5060;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SubVoiceVoipPlarUdpPort_Type.__name__=_D
_SubVoiceVoipPlarUdpPort_Object=MibTableColumn
subVoiceVoipPlarUdpPort=_SubVoiceVoipPlarUdpPort_Object((1,3,6,1,4,1,5504,3,4,1,13,1,14),_SubVoiceVoipPlarUdpPort_Type())
subVoiceVoipPlarUdpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:subVoiceVoipPlarUdpPort.setStatus(_A)
class _SubVoiceVoipRegistrationServer_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SubVoiceVoipRegistrationServer_Type.__name__=_J
_SubVoiceVoipRegistrationServer_Object=MibTableColumn
subVoiceVoipRegistrationServer=_SubVoiceVoipRegistrationServer_Object((1,3,6,1,4,1,5504,3,4,1,13,1,15),_SubVoiceVoipRegistrationServer_Type())
subVoiceVoipRegistrationServer.setMaxAccess(_C)
if mibBuilder.loadTexts:subVoiceVoipRegistrationServer.setStatus(_A)
class _SubVoiceVoipT38Fax_Type(T38FaxType):defaultValue=3
_SubVoiceVoipT38Fax_Type.__name__=_c
_SubVoiceVoipT38Fax_Object=MibTableColumn
subVoiceVoipT38Fax=_SubVoiceVoipT38Fax_Object((1,3,6,1,4,1,5504,3,4,1,13,1,16),_SubVoiceVoipT38Fax_Type())
subVoiceVoipT38Fax.setMaxAccess(_C)
if mibBuilder.loadTexts:subVoiceVoipT38Fax.setStatus(_A)
class _SubVoiceVoipAuthUsername_Type(ZhoneAdminString):defaultValue=OctetString('')
_SubVoiceVoipAuthUsername_Type.__name__=_P
_SubVoiceVoipAuthUsername_Object=MibTableColumn
subVoiceVoipAuthUsername=_SubVoiceVoipAuthUsername_Object((1,3,6,1,4,1,5504,3,4,1,13,1,17),_SubVoiceVoipAuthUsername_Type())
subVoiceVoipAuthUsername.setMaxAccess(_C)
if mibBuilder.loadTexts:subVoiceVoipAuthUsername.setStatus(_A)
if mibBuilder.loadTexts:subVoiceVoipAuthUsername.setUnits('characters')
_SubVoiceVoipHotlineDN_Type=ZhoneAdminString
_SubVoiceVoipHotlineDN_Object=MibTableColumn
subVoiceVoipHotlineDN=_SubVoiceVoipHotlineDN_Object((1,3,6,1,4,1,5504,3,4,1,13,1,18),_SubVoiceVoipHotlineDN_Type())
subVoiceVoipHotlineDN.setMaxAccess(_C)
if mibBuilder.loadTexts:subVoiceVoipHotlineDN.setStatus(_A)
class _SubVoiceHotlineInitialTimer_Type(Unsigned32):defaultValue=4
_SubVoiceHotlineInitialTimer_Type.__name__=_J
_SubVoiceHotlineInitialTimer_Object=MibTableColumn
subVoiceHotlineInitialTimer=_SubVoiceHotlineInitialTimer_Object((1,3,6,1,4,1,5504,3,4,1,13,1,19),_SubVoiceHotlineInitialTimer_Type())
subVoiceHotlineInitialTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:subVoiceHotlineInitialTimer.setStatus(_A)
if mibBuilder.loadTexts:subVoiceHotlineInitialTimer.setUnits('seconds')
_SubVoiceElcpAal2Table_Object=MibTable
subVoiceElcpAal2Table=_SubVoiceElcpAal2Table_Object((1,3,6,1,4,1,5504,3,4,1,14))
if mibBuilder.loadTexts:subVoiceElcpAal2Table.setStatus(_A)
_SubVoiceElcpAal2Entry_Object=MibTableRow
subVoiceElcpAal2Entry=_SubVoiceElcpAal2Entry_Object((1,3,6,1,4,1,5504,3,4,1,14,1))
subVoiceElcpAal2Entry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:subVoiceElcpAal2Entry.setStatus(_A)
class _SubVoiceElcpAal2EndPointIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SubVoiceElcpAal2EndPointIndex_Type.__name__=_D
_SubVoiceElcpAal2EndPointIndex_Object=MibTableColumn
subVoiceElcpAal2EndPointIndex=_SubVoiceElcpAal2EndPointIndex_Object((1,3,6,1,4,1,5504,3,4,1,14,1,1),_SubVoiceElcpAal2EndPointIndex_Type())
subVoiceElcpAal2EndPointIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:subVoiceElcpAal2EndPointIndex.setStatus(_A)
_SubVoiceElcpAal2LineGroupId_Type=Integer32
_SubVoiceElcpAal2LineGroupId_Object=MibTableColumn
subVoiceElcpAal2LineGroupId=_SubVoiceElcpAal2LineGroupId_Object((1,3,6,1,4,1,5504,3,4,1,14,1,2),_SubVoiceElcpAal2LineGroupId_Type())
subVoiceElcpAal2LineGroupId.setMaxAccess(_C)
if mibBuilder.loadTexts:subVoiceElcpAal2LineGroupId.setStatus(_A)
_SubVoiceElcpAal2Vpi_Type=AtmVpIdentifier
_SubVoiceElcpAal2Vpi_Object=MibTableColumn
subVoiceElcpAal2Vpi=_SubVoiceElcpAal2Vpi_Object((1,3,6,1,4,1,5504,3,4,1,14,1,3),_SubVoiceElcpAal2Vpi_Type())
subVoiceElcpAal2Vpi.setMaxAccess(_C)
if mibBuilder.loadTexts:subVoiceElcpAal2Vpi.setStatus(_A)
_SubVoiceElcpAal2Vci_Type=AtmVcIdentifier
_SubVoiceElcpAal2Vci_Object=MibTableColumn
subVoiceElcpAal2Vci=_SubVoiceElcpAal2Vci_Object((1,3,6,1,4,1,5504,3,4,1,14,1,4),_SubVoiceElcpAal2Vci_Type())
subVoiceElcpAal2Vci.setMaxAccess(_C)
if mibBuilder.loadTexts:subVoiceElcpAal2Vci.setStatus(_A)
class _SubVoiceElcpAal2PortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_SubVoiceElcpAal2PortId_Type.__name__=_D
_SubVoiceElcpAal2PortId_Object=MibTableColumn
subVoiceElcpAal2PortId=_SubVoiceElcpAal2PortId_Object((1,3,6,1,4,1,5504,3,4,1,14,1,5),_SubVoiceElcpAal2PortId_Type())
subVoiceElcpAal2PortId.setMaxAccess(_C)
if mibBuilder.loadTexts:subVoiceElcpAal2PortId.setStatus(_A)
class _SubVoiceElcpAal2PortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('pots',1),(_M,2),(_N,3)))
_SubVoiceElcpAal2PortType_Type.__name__=_D
_SubVoiceElcpAal2PortType_Object=MibTableColumn
subVoiceElcpAal2PortType=_SubVoiceElcpAal2PortType_Object((1,3,6,1,4,1,5504,3,4,1,14,1,6),_SubVoiceElcpAal2PortType_Type())
subVoiceElcpAal2PortType.setMaxAccess(_C)
if mibBuilder.loadTexts:subVoiceElcpAal2PortType.setStatus(_A)
class _SubVoiceElcpAal2IsdnChannelId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_SubVoiceElcpAal2IsdnChannelId_Type.__name__=_D
_SubVoiceElcpAal2IsdnChannelId_Object=MibTableColumn
subVoiceElcpAal2IsdnChannelId=_SubVoiceElcpAal2IsdnChannelId_Object((1,3,6,1,4,1,5504,3,4,1,14,1,7),_SubVoiceElcpAal2IsdnChannelId_Type())
subVoiceElcpAal2IsdnChannelId.setMaxAccess(_C)
if mibBuilder.loadTexts:subVoiceElcpAal2IsdnChannelId.setStatus(_A)
_SubVoiceEbsTable_Object=MibTable
subVoiceEbsTable=_SubVoiceEbsTable_Object((1,3,6,1,4,1,5504,3,4,1,15))
if mibBuilder.loadTexts:subVoiceEbsTable.setStatus(_A)
_SubVoiceEbsEntry_Object=MibTableRow
subVoiceEbsEntry=_SubVoiceEbsEntry_Object((1,3,6,1,4,1,5504,3,4,1,15,1))
subVoiceEbsEntry.setIndexNames((0,_B,_d))
if mibBuilder.loadTexts:subVoiceEbsEntry.setStatus(_A)
class _SubVoiceEbsEndPointIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SubVoiceEbsEndPointIndex_Type.__name__=_D
_SubVoiceEbsEndPointIndex_Object=MibTableColumn
subVoiceEbsEndPointIndex=_SubVoiceEbsEndPointIndex_Object((1,3,6,1,4,1,5504,3,4,1,15,1,1),_SubVoiceEbsEndPointIndex_Type())
subVoiceEbsEndPointIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:subVoiceEbsEndPointIndex.setStatus(_A)
_SubVoiceEbsLineGroupId_Type=Integer32
_SubVoiceEbsLineGroupId_Object=MibTableColumn
subVoiceEbsLineGroupId=_SubVoiceEbsLineGroupId_Object((1,3,6,1,4,1,5504,3,4,1,15,1,2),_SubVoiceEbsLineGroupId_Type())
subVoiceEbsLineGroupId.setMaxAccess(_C)
if mibBuilder.loadTexts:subVoiceEbsLineGroupId.setStatus(_A)
_SubVoiceIsdnSigTable_Object=MibTable
subVoiceIsdnSigTable=_SubVoiceIsdnSigTable_Object((1,3,6,1,4,1,5504,3,4,1,16))
if mibBuilder.loadTexts:subVoiceIsdnSigTable.setStatus(_A)
_SubVoiceIsdnSigEntry_Object=MibTableRow
subVoiceIsdnSigEntry=_SubVoiceIsdnSigEntry_Object((1,3,6,1,4,1,5504,3,4,1,16,1))
subVoiceIsdnSigEntry.setIndexNames((0,_B,_e))
if mibBuilder.loadTexts:subVoiceIsdnSigEntry.setStatus(_A)
class _SubVoiceIsdnSigEndPointIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SubVoiceIsdnSigEndPointIndex_Type.__name__=_D
_SubVoiceIsdnSigEndPointIndex_Object=MibTableColumn
subVoiceIsdnSigEndPointIndex=_SubVoiceIsdnSigEndPointIndex_Object((1,3,6,1,4,1,5504,3,4,1,16,1,1),_SubVoiceIsdnSigEndPointIndex_Type())
subVoiceIsdnSigEndPointIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:subVoiceIsdnSigEndPointIndex.setStatus(_A)
class _SubVoiceIsdnSigEntryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SubVoiceIsdnSigEntryIndex_Type.__name__=_D
_SubVoiceIsdnSigEntryIndex_Object=MibTableColumn
subVoiceIsdnSigEntryIndex=_SubVoiceIsdnSigEntryIndex_Object((1,3,6,1,4,1,5504,3,4,1,16,1,2),_SubVoiceIsdnSigEntryIndex_Type())
subVoiceIsdnSigEntryIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:subVoiceIsdnSigEntryIndex.setStatus(_A)
_SubVoiceIsdnSigDirectoryNumber_Type=ZhoneAdminString
_SubVoiceIsdnSigDirectoryNumber_Object=MibTableColumn
subVoiceIsdnSigDirectoryNumber=_SubVoiceIsdnSigDirectoryNumber_Object((1,3,6,1,4,1,5504,3,4,1,16,1,3),_SubVoiceIsdnSigDirectoryNumber_Type())
subVoiceIsdnSigDirectoryNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:subVoiceIsdnSigDirectoryNumber.setStatus(_A)
_SubVoiceIsdnSigHuntGrpEndPointIndex1_Type=Integer32
_SubVoiceIsdnSigHuntGrpEndPointIndex1_Object=MibTableColumn
subVoiceIsdnSigHuntGrpEndPointIndex1=_SubVoiceIsdnSigHuntGrpEndPointIndex1_Object((1,3,6,1,4,1,5504,3,4,1,16,1,4),_SubVoiceIsdnSigHuntGrpEndPointIndex1_Type())
subVoiceIsdnSigHuntGrpEndPointIndex1.setMaxAccess(_C)
if mibBuilder.loadTexts:subVoiceIsdnSigHuntGrpEndPointIndex1.setStatus(_A)
_SubVoiceIsdnSigHuntGrpEndPointIndex2_Type=Integer32
_SubVoiceIsdnSigHuntGrpEndPointIndex2_Object=MibTableColumn
subVoiceIsdnSigHuntGrpEndPointIndex2=_SubVoiceIsdnSigHuntGrpEndPointIndex2_Object((1,3,6,1,4,1,5504,3,4,1,16,1,5),_SubVoiceIsdnSigHuntGrpEndPointIndex2_Type())
subVoiceIsdnSigHuntGrpEndPointIndex2.setMaxAccess(_C)
if mibBuilder.loadTexts:subVoiceIsdnSigHuntGrpEndPointIndex2.setStatus(_A)
_SubVoiceIsdnSigHuntGrpEndPointIndex3_Type=Integer32
_SubVoiceIsdnSigHuntGrpEndPointIndex3_Object=MibTableColumn
subVoiceIsdnSigHuntGrpEndPointIndex3=_SubVoiceIsdnSigHuntGrpEndPointIndex3_Object((1,3,6,1,4,1,5504,3,4,1,16,1,6),_SubVoiceIsdnSigHuntGrpEndPointIndex3_Type())
subVoiceIsdnSigHuntGrpEndPointIndex3.setMaxAccess(_C)
if mibBuilder.loadTexts:subVoiceIsdnSigHuntGrpEndPointIndex3.setStatus(_A)
_SubVoiceTr008Table_Object=MibTable
subVoiceTr008Table=_SubVoiceTr008Table_Object((1,3,6,1,4,1,5504,3,4,1,17))
if mibBuilder.loadTexts:subVoiceTr008Table.setStatus(_A)
_SubVoiceTr008Entry_Object=MibTableRow
subVoiceTr008Entry=_SubVoiceTr008Entry_Object((1,3,6,1,4,1,5504,3,4,1,17,1))
subVoiceTr008Entry.setIndexNames((0,_B,_f))
if mibBuilder.loadTexts:subVoiceTr008Entry.setStatus(_A)
_SubVoiceTr008EndPointIndex_Type=Integer32
_SubVoiceTr008EndPointIndex_Object=MibTableColumn
subVoiceTr008EndPointIndex=_SubVoiceTr008EndPointIndex_Object((1,3,6,1,4,1,5504,3,4,1,17,1,1),_SubVoiceTr008EndPointIndex_Type())
subVoiceTr008EndPointIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:subVoiceTr008EndPointIndex.setStatus(_A)
_SubVoiceTr008GroupId_Type=InterfaceIndex
_SubVoiceTr008GroupId_Object=MibTableColumn
subVoiceTr008GroupId=_SubVoiceTr008GroupId_Object((1,3,6,1,4,1,5504,3,4,1,17,1,2),_SubVoiceTr008GroupId_Type())
subVoiceTr008GroupId.setMaxAccess(_C)
if mibBuilder.loadTexts:subVoiceTr008GroupId.setStatus(_A)
class _SubVoiceTr008ChanNum_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_SubVoiceTr008ChanNum_Type.__name__=_D
_SubVoiceTr008ChanNum_Object=MibTableColumn
subVoiceTr008ChanNum=_SubVoiceTr008ChanNum_Object((1,3,6,1,4,1,5504,3,4,1,17,1,3),_SubVoiceTr008ChanNum_Type())
subVoiceTr008ChanNum.setMaxAccess(_C)
if mibBuilder.loadTexts:subVoiceTr008ChanNum.setStatus(_A)
zhoneSubscriberObjectsGroup=ObjectGroup((1,3,6,1,4,1,5504,3,4,1,11))
zhoneSubscriberObjectsGroup.setObjects(*((_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_Ah),(_B,_Ai),(_B,_Aj),(_B,_Ak),(_B,_Al),(_B,_Am),(_B,_An),(_B,_Ao),(_B,_Ap),(_B,_Aq),(_B,_Ar),(_B,_As),(_B,_At)))
if mibBuilder.loadTexts:zhoneSubscriberObjectsGroup.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_b:ZhoneCodecType,_c:T38FaxType,'zhoneSubscriberRecords':zhoneSubscriberRecords,_g:nextSubId,_h:nextEndPointIndex,'subInfoTable':subInfoTable,'subInfoEntry':subInfoEntry,_H:subId,_I:subLgId,_i:subName,_j:subProviderId,_k:subIadType,_l:subMaxAllowedLineRate,_m:subMaxCapableLineRate,_n:subNextVoiceConnectionIndex,_o:subRowStatus,'subDataConnectionTable':subDataConnectionTable,'subDataConnectionEntry':subDataConnectionEntry,_R:subDataIfIndex,_p:subDataIpIfOperStatus,_q:subDataUserLogOnId,_r:subDataUserPassword,_s:subDataMaxAddrAllowed,_t:subDataIpAddrInUse,_u:subDataCurrentIpAddr,_v:subDataStatsStatus,_w:subDataRowStatus,'subVoiceConnectionTable':subVoiceConnectionTable,'subVoiceConnectionEntry':subVoiceConnectionEntry,_U:subVoiceConnectionIndex,_x:subVoiceConnectionType,_y:subVoiceEndPoint1AddressIndex,_z:subVoiceEndPoint2AddressIndex,_A0:subVoiceConnectionDescription,_A1:subVoiceAdminStatus,_A2:subVoiceRowStatus,_AQ:subVoiceHuntGroup,_Al:subVoiceFeatureSetOne,'subVoiceAal2Table':subVoiceAal2Table,'subVoiceAal2Entry':subVoiceAal2Entry,_L:subVoiceAal2EndPointIndex,_A3:subVoiceAal2LineGroupId,_A4:subVoiceAal2Vpi,_A5:subVoiceAal2Vci,_A6:subVoiceAal2Cid,'subVoiceGr303Table':subVoiceGr303Table,'subVoiceGr303Entry':subVoiceGr303Entry,_V:subVoiceGr303EndPointIndex,_A7:subVoiceGr303IgName,_A8:subVoiceGr303IgCrv,'subVoiceV52Table':subVoiceV52Table,'subVoiceV52Entry':subVoiceV52Entry,_W:subVoiceV52EndPointIndex,_A9:subVoiceV52InterfaceName,_AA:subVoiceV52UserPortId,_AB:subVoiceV52UserType,_AC:subVoiceV52IsdnChannelId,'subVoicePotsTable':subVoicePotsTable,'subVoicePotsEntry':subVoicePotsEntry,_X:subVoicePotsEndPointIndex,_AD:subVoicePotsLineGroupId,_AV:subVoicePotsHuntGrpEndPointIndex1,_AU:subVoicePotsHuntGrpEndPointIndex2,_AT:subVoicePotsHuntGrpEndPointIndex3,'subVoiceIsdnTable':subVoiceIsdnTable,'subVoiceIsdnEntry':subVoiceIsdnEntry,_Y:subVoiceIsdnEndPointIndex,_AE:subVoiceIsdnLineGroupId,_AF:subVoiceIsdnType,_AG:subVoiceIsdnChannelId,'zhoneSubscriberObjectsGroup':zhoneSubscriberObjectsGroup,'subVoiceDs1Table':subVoiceDs1Table,'subVoiceDs1Entry':subVoiceDs1Entry,_Z:subVoiceDs1EndPointIndex,_AH:subVoiceDs1Ds0ChannelID,_AI:subVoiceDs1LineGroupId,_AS:subVoiceDs1HuntGrpEndPointIndex1,_AW:subVoiceDs1HuntGrpEndPointIndex2,_AR:subVoiceDs1HuntGrpEndPointIndex3,'subVoiceVoipTable':subVoiceVoipTable,'subVoiceVoipEntry':subVoiceVoipEntry,_a:subVoiceVoipEndPointIndex,_Ae:subVoiceVoipUserName,_Ac:subVoiceVoipDirectoryNumber,_Ad:subVoiceVoipIpInterface,_Ab:subVoiceVoipPreferredCodec,_Aa:subVoiceVoipG711Fallback,_AZ:subVoiceVoipFramesPerPacket,_AY:subVoiceVoipG726ByteOrder,_AX:subVoiceVoipPassword,_Ai:subVoiceVoipPLAR,_Ak:subVoiceVoipPlarDestIpAddrType,_Ah:subVoiceVoipPlarDestIpAddr,_Aj:subVoiceVoipPlarUdpPort,'subVoiceVoipRegistrationServer':subVoiceVoipRegistrationServer,'subVoiceVoipT38Fax':subVoiceVoipT38Fax,_Ao:subVoiceVoipAuthUsername,_Aq:subVoiceVoipHotlineDN,_Ap:subVoiceHotlineInitialTimer,'subVoiceElcpAal2Table':subVoiceElcpAal2Table,'subVoiceElcpAal2Entry':subVoiceElcpAal2Entry,'subVoiceElcpAal2EndPointIndex':subVoiceElcpAal2EndPointIndex,_AJ:subVoiceElcpAal2LineGroupId,_AK:subVoiceElcpAal2Vpi,_AL:subVoiceElcpAal2Vci,_AM:subVoiceElcpAal2PortId,_AN:subVoiceElcpAal2PortType,_AO:subVoiceElcpAal2IsdnChannelId,'subVoiceEbsTable':subVoiceEbsTable,'subVoiceEbsEntry':subVoiceEbsEntry,_d:subVoiceEbsEndPointIndex,_AP:subVoiceEbsLineGroupId,'subVoiceIsdnSigTable':subVoiceIsdnSigTable,'subVoiceIsdnSigEntry':subVoiceIsdnSigEntry,_e:subVoiceIsdnSigEndPointIndex,_As:subVoiceIsdnSigEntryIndex,_At:subVoiceIsdnSigDirectoryNumber,_Ar:subVoiceIsdnSigHuntGrpEndPointIndex1,_Ag:subVoiceIsdnSigHuntGrpEndPointIndex2,_Af:subVoiceIsdnSigHuntGrpEndPointIndex3,'subVoiceTr008Table':subVoiceTr008Table,'subVoiceTr008Entry':subVoiceTr008Entry,_f:subVoiceTr008EndPointIndex,_An:subVoiceTr008GroupId,_Am:subVoiceTr008ChanNum})