_BB='arrisRouterFlapListLANIndex'
_BA='arrisRouterFlapListWLANIndex'
_B9='arrisRouterICtrlPortMapIndex'
_B8='arrisRouterWebAccessIndex'
_B7='arrisRouterInboundTrafficLogIndex'
_B6='arrisRouterMSOChgLogIndex'
_B5='arrisRouterFWLogExtIndex'
_B4='arrisRouterDebugLogIndex'
_B3='arrisRouterChangeLogIndex'
_B2='arrisRouterPCLogIndex'
_B1='arrisRouterFWLogIndex'
_B0='applySettings'
_A_='arrisRouterSNTPServerIndex'
_Az='arrisRouterFWPortAllowIndex'
_Ay='arrisRouterFWMacBridgingIndex'
_Ax='arrisRouterExceptionListIndex'
_Aw='arrisRouterTrustedDeviceIndex'
_Av='arrisRouterWhiteListIndex'
_Au='arrisRouterBlackListIndex'
_At='arrisRouterKeywordBlkIndex'
_As='arrisRouterFWPortTrigIndex'
_Ar='arrisRouterFWMACFilterIndex'
_Aq='arrisRouterFWIPFilterIndex'
_Ap='arrisRouterFWVirtSrvIndex'
_Ao='arrisRouterBssStaSteeringClientIndex'
_An='arrisRouterWMM50EDCAAPIndex'
_Am='arrisRouterChannelStatsRSSITableIndex'
_Al='arrisRouterWiFiClientInfoIndex'
_Ak='arrisRouterWiFiScanIndex'
_Aj='cancelWPS'
_Ai='activatePINCfg'
_Ah='activatePushButton'
_Ag='wpsPushButtonFindAP'
_Af='wpsAssociating'
_Ae='wpsPushButtonOverlap'
_Ad='wpsMsgExchangeErr'
_Ac='wpsSuccessful'
_Ab='wpsMsgDone'
_Aa='wpsTimedOut'
_AZ='wpsM7Sent'
_AY='wpsM2Sent'
_AX='wpsAssociatedStarted'
_AW='wpsInitialState'
_AV='wpsUnknown'
_AU='wpsResultConfigApAbort'
_AT='wpsResultConfigApFail'
_AS='wpsResultConfigApSuccess'
_AR='wpsResultAddClientAbort'
_AQ='wpsResultAddClientFail'
_AP='wpsResultAddClientSuccess'
_AO='wpsResultNoneIssued'
_AN='wpsResultUnknown'
_AM='arrisRouterWMMEDCAAPIndex'
_AL='arrisRouterMACAccessIndex'
_AK='arrisRouterWEP128BitKeyIndex'
_AJ='arrisRouterWEP64BitKeyIndex'
_AI='wpaWpa2Enterprise'
_AH='wpa2Enterprise'
_AG='wpaEnterprise'
_AF='greenField'
_AE='width20and40Mhz'
_AD='width20MHz'
_AC='percent100'
_AB='percent75'
_AA='percent50'
_A9='percent25'
_A8='percent12'
_A7='readandWrite'
_A6='writeOnly'
_A5='arrisRouterLanUSBPortIdx'
_A4='arrisRouterLanSrvDHCPOptionsIdx'
_A3='arrisRouterLanEtherPortIdx'
_A2='arrisRouterLanClientDHCPOptionsIdx'
_A1='arrisRouterLanCustomIdx'
_A0='arrisRouterDeviceUpDownIndex'
_z='arrisRouterLanDNSIdx'
_y='arrisRouterWanStaticDNSIPIndex'
_x='arrisRouterWanCurrentDNSIPIndex'
_w='arrisRouterWanStaticIPIndex'
_v='2012-02-15 00:00'
_u='2012-10-15 00:00'
_t='2012-10-26 00:00'
_s='2013-01-31 00:00'
_r='2013-08-13 00:00'
_q='2014-11-26 00:00'
_p='2014-12-12 00:00'
_o='2015-04-10 00:00'
_n='DscpOrAny'
_m='both'
_l='arrisRouterLanLocalUserIdx'
_k='arrisRouterLanFilesharingIdx'
_j='arrisRouterLanClientIPAddr'
_i='arrisRouterLanClientIPAddrType'
_h='arrisRouterWanCurrentIPIndex'
_g='2014-11-27 00:00'
_f='2014-12-09 00:00'
_e='2015-01-04 00:00'
_d='Counter64'
_c='tcp'
_b='udp'
_a='packets'
_Z='microseconds'
_Y='apply'
_X='noApply'
_W='static'
_V='dynamic'
_U='OctetString'
_T='bytes'
_S='InetAddressType'
_R='auto'
_Q='enabled'
_P='milliseconds'
_O='disabled'
_N='unknown'
_M='seconds'
_L='ifIndex'
_K='IF-MIB'
_J='not-accessible'
_I='ARRIS-ROUTER-DEVICE-MIB'
_H='Unsigned32'
_G='DisplayString'
_F='TruthValue'
_E='read-create'
_D='Integer32'
_C='read-only'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_U,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
arrisProdIdRouter,=mibBuilder.importSymbols('ARRIS-MIB','arrisProdIdRouter')
DscpOrAny,=mibBuilder.importSymbols('DIFFSERV-DSCP-TC',_n)
ifIndex,=mibBuilder.importSymbols(_K,_L)
InetAddress,InetAddressIPv6,InetAddressPrefixLength,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressIPv6','InetAddressPrefixLength',_S)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32',_d,'Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_G,'MacAddress','PhysAddress','RowStatus','TextualConvention',_F)
arrisRouterMib=ModuleIdentity((1,3,6,1,4,1,4115,1,20,1))
if mibBuilder.loadTexts:arrisRouterMib.setRevisions(('2015-07-15 00:00','2015-07-08 00:00','2015-06-26 00:00','2015-06-04 00:00','2015-05-26 00:00','2015-05-25 00:00','2015-05-15 00:00','2015-05-13 00:00','2015-04-28 00:00','2015-04-27 00:00','2015-04-24 00:00',_o,_o,'2015-04-01 00:00','2015-03-31 00:00',_e,'2015-03-26 00:00','2015-02-27 00:00',_e,'2015-02-17 00:00','2015-02-12 00:00','2015-02-06 00:00','2015-01-30 00:00','2015-02-10 00:00','2015-01-15 00:00','2015-01-08 00:00',_e,_p,'2014-12-24 00:00','2014-12-23 00:00',_f,_p,'2014-12-11 00:00',_f,_f,_g,'2014-11-25 00:00',_g,_g,_q,_q,'2014-11-21 00:00','2014-11-20 00:00','2014-11-14 00:00','2014-11-13 00:00','2014-11-01 00:00','2014-10-27 00:00','2014-10-23 00:00','2014-10-01 00:00','2014-10-17 00:00','2014-10-14 00:00','2014-10-13 00:00','2014-10-11 00:00','2014-09-15 00:00','2014-07-11 00:00','2014-06-16 00:00','2014-06-04 00:00','2014-05-15 00:00','2014-04-28 00:00','2014-03-27 00:00','2014-03-25 00:00','2014-03-19 00:00','2014-03-06 00:00','2014-02-24 00:00','2014-01-28 00:00','2014-01-27 00:00','2014-01-16 00:00','2014-01-10 00:00','2013-11-28 00:00','2013-11-25 00:00','2013-11-20 00:00','2013-10-17 00:00','2013-10-15 00:00','2013-09-19 00:00','2013-09-04 00:00','2013-08-26 00:00','2013-08-20 00:00',_r,_r,'2013-08-07 00:00','2013-08-02 00:00','2013-07-30 00:00','2013-07-26 00:00','2013-07-24 00:00','2013-07-22 00:01','2013-07-17 00:01','2013-07-17 00:00','2013-07-16 00:00','2013-06-26 00:00','2013-06-20 00:00','2013-06-05 00:00','2013-06-03 00:00','2013-05-31 00:00','2013-05-29 00:00','2013-05-22 00:00',_s,'2013-05-09 00:00','2013-04-27 00:00','2013-04-24 00:00','2013-04-17 00:00','2013-04-15 00:00','2013-04-03 00:00','2013-04-08 00:00','2013-03-19 00:00','2013-03-29 00:00','2013-03-15 00:00','2013-03-13 00:00','2013-03-07 00:00','2013-03-06 00:00','2013-02-08 00:00',_s,'2013-01-10 00:00','2012-12-27 00:00','2012-12-19 00:00','2012-12-17 00:00','2012-12-11 00:00','2012-12-04 00:00','2012-11-02 00:00','2012-11-01 00:00','2012-10-31 00:00',_t,_t,_u,_u,'2012-08-29 00:00','2012-06-12 00:00','2012-05-30 00:00','2012-05-22 00:00','2012-05-21 00:00','2012-04-02 00:00','2012-03-21 00:00',_v,_v,'2011-12-09 00:00','2011-10-06 00:00','2011-09-06 00:00','2011-08-30 00:00','2011-08-18 00:00','2011-05-05 00:00','2011-04-28 00:00','2011-02-09 00:00','2011-02-04 00:00','2011-01-18 00:00','2011-01-10 00:00','2011-01-09 00:00','2010-12-22 00:00','2010-12-17 00:00','2010-12-15 00:00','2010-12-06 00:00','2010-11-29 00:00','2010-11-26 00:00','2010-11-23 00:00','2010-11-08 00:00','2010-10-26 00:00','2010-10-25 00:00','2010-10-21 00:00','2010-10-20 00:00','2010-10-15 00:00','2010-10-12 00:00','2010-09-30 00:00','2010-09-24 00:00','2010-09-21 00:00','2010-09-16 00:00','2010-09-01 00:00','2010-08-17 00:00','2010-07-23 00:00','2010-07-22 00:00','2010-07-14 00:00','2010-07-12 00:00','2010-06-30 00:00','2010-06-28 00:00','2010-06-20 00:00','2010-06-17 00:00','2010-05-27 00:00','2010-05-26 00:00','2010-05-11 00:00','2010-05-07 00:00','2010-05-03 00:00','2010-04-29 00:00','2010-04-27 00:00','2010-04-25 00:00','2010-04-22 00:00','2010-02-11 00:00'))
_ArrisRouterMibObjects_ObjectIdentity=ObjectIdentity
arrisRouterMibObjects=_ArrisRouterMibObjects_ObjectIdentity((1,3,6,1,4,1,4115,1,20,1,1))
_ArrisRouterWanConfig_ObjectIdentity=ObjectIdentity
arrisRouterWanConfig=_ArrisRouterWanConfig_ObjectIdentity((1,3,6,1,4,1,4115,1,20,1,1,1))
class _ArrisRouterWanConnType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,5,6)));namedValues=NamedValues(*((_N,0),(_V,1),(_W,2),('l2tpStatic',5),('l2tpDynamic',6)))
_ArrisRouterWanConnType_Type.__name__=_D
_ArrisRouterWanConnType_Object=MibScalar
arrisRouterWanConnType=_ArrisRouterWanConnType_Object((1,3,6,1,4,1,4115,1,20,1,1,1,1),_ArrisRouterWanConnType_Type())
arrisRouterWanConnType.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWanConnType.setStatus(_A)
class _ArrisRouterWanConnHostName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_ArrisRouterWanConnHostName_Type.__name__=_G
_ArrisRouterWanConnHostName_Object=MibScalar
arrisRouterWanConnHostName=_ArrisRouterWanConnHostName_Object((1,3,6,1,4,1,4115,1,20,1,1,1,2),_ArrisRouterWanConnHostName_Type())
arrisRouterWanConnHostName.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWanConnHostName.setStatus(_A)
class _ArrisRouterWanConnDomainName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_ArrisRouterWanConnDomainName_Type.__name__=_G
_ArrisRouterWanConnDomainName_Object=MibScalar
arrisRouterWanConnDomainName=_ArrisRouterWanConnDomainName_Object((1,3,6,1,4,1,4115,1,20,1,1,1,3),_ArrisRouterWanConnDomainName_Type())
arrisRouterWanConnDomainName.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWanConnDomainName.setStatus(_A)
class _ArrisRouterWanMTUSize_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(256,1500))
_ArrisRouterWanMTUSize_Type.__name__=_H
_ArrisRouterWanMTUSize_Object=MibScalar
arrisRouterWanMTUSize=_ArrisRouterWanMTUSize_Object((1,3,6,1,4,1,4115,1,20,1,1,1,4),_ArrisRouterWanMTUSize_Type())
arrisRouterWanMTUSize.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWanMTUSize.setStatus(_A)
_ArrisRouterWanCurrentTable_Object=MibTable
arrisRouterWanCurrentTable=_ArrisRouterWanCurrentTable_Object((1,3,6,1,4,1,4115,1,20,1,1,1,7))
if mibBuilder.loadTexts:arrisRouterWanCurrentTable.setStatus(_A)
_ArrisRouterWanCurrentEntry_Object=MibTableRow
arrisRouterWanCurrentEntry=_ArrisRouterWanCurrentEntry_Object((1,3,6,1,4,1,4115,1,20,1,1,1,7,1))
arrisRouterWanCurrentEntry.setIndexNames((0,_I,_h))
if mibBuilder.loadTexts:arrisRouterWanCurrentEntry.setStatus(_A)
_ArrisRouterWanCurrentIPIndex_Type=Unsigned32
_ArrisRouterWanCurrentIPIndex_Object=MibTableColumn
arrisRouterWanCurrentIPIndex=_ArrisRouterWanCurrentIPIndex_Object((1,3,6,1,4,1,4115,1,20,1,1,1,7,1,1),_ArrisRouterWanCurrentIPIndex_Type())
arrisRouterWanCurrentIPIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:arrisRouterWanCurrentIPIndex.setStatus(_A)
_ArrisRouterWanCurrentIPAddrType_Type=InetAddressType
_ArrisRouterWanCurrentIPAddrType_Object=MibTableColumn
arrisRouterWanCurrentIPAddrType=_ArrisRouterWanCurrentIPAddrType_Object((1,3,6,1,4,1,4115,1,20,1,1,1,7,1,2),_ArrisRouterWanCurrentIPAddrType_Type())
arrisRouterWanCurrentIPAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWanCurrentIPAddrType.setStatus(_A)
_ArrisRouterWanCurrentIPAddr_Type=InetAddress
_ArrisRouterWanCurrentIPAddr_Object=MibTableColumn
arrisRouterWanCurrentIPAddr=_ArrisRouterWanCurrentIPAddr_Object((1,3,6,1,4,1,4115,1,20,1,1,1,7,1,3),_ArrisRouterWanCurrentIPAddr_Type())
arrisRouterWanCurrentIPAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWanCurrentIPAddr.setStatus(_A)
_ArrisRouterWanCurrentPrefix_Type=InetAddressPrefixLength
_ArrisRouterWanCurrentPrefix_Object=MibTableColumn
arrisRouterWanCurrentPrefix=_ArrisRouterWanCurrentPrefix_Object((1,3,6,1,4,1,4115,1,20,1,1,1,7,1,4),_ArrisRouterWanCurrentPrefix_Type())
arrisRouterWanCurrentPrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWanCurrentPrefix.setStatus(_A)
_ArrisRouterWanCurrentGWType_Type=InetAddressType
_ArrisRouterWanCurrentGWType_Object=MibTableColumn
arrisRouterWanCurrentGWType=_ArrisRouterWanCurrentGWType_Object((1,3,6,1,4,1,4115,1,20,1,1,1,7,1,5),_ArrisRouterWanCurrentGWType_Type())
arrisRouterWanCurrentGWType.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWanCurrentGWType.setStatus(_A)
_ArrisRouterWanCurrentGW_Type=InetAddress
_ArrisRouterWanCurrentGW_Object=MibTableColumn
arrisRouterWanCurrentGW=_ArrisRouterWanCurrentGW_Object((1,3,6,1,4,1,4115,1,20,1,1,1,7,1,6),_ArrisRouterWanCurrentGW_Type())
arrisRouterWanCurrentGW.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWanCurrentGW.setStatus(_A)
class _ArrisRouterWanCurrentIPType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_N,0),(_V,1),(_W,2)))
_ArrisRouterWanCurrentIPType_Type.__name__=_D
_ArrisRouterWanCurrentIPType_Object=MibTableColumn
arrisRouterWanCurrentIPType=_ArrisRouterWanCurrentIPType_Object((1,3,6,1,4,1,4115,1,20,1,1,1,7,1,7),_ArrisRouterWanCurrentIPType_Type())
arrisRouterWanCurrentIPType.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWanCurrentIPType.setStatus(_A)
_ArrisRouterWanCurrentNetMask_Type=InetAddress
_ArrisRouterWanCurrentNetMask_Object=MibTableColumn
arrisRouterWanCurrentNetMask=_ArrisRouterWanCurrentNetMask_Object((1,3,6,1,4,1,4115,1,20,1,1,1,7,1,8),_ArrisRouterWanCurrentNetMask_Type())
arrisRouterWanCurrentNetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWanCurrentNetMask.setStatus(_A)
_ArrisRouterWanCurrentPrefixDelegationV6_Type=InetAddressIPv6
_ArrisRouterWanCurrentPrefixDelegationV6_Object=MibTableColumn
arrisRouterWanCurrentPrefixDelegationV6=_ArrisRouterWanCurrentPrefixDelegationV6_Object((1,3,6,1,4,1,4115,1,20,1,1,1,7,1,9),_ArrisRouterWanCurrentPrefixDelegationV6_Type())
arrisRouterWanCurrentPrefixDelegationV6.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWanCurrentPrefixDelegationV6.setStatus(_A)
_ArrisRouterWanCurrentPrefixDelegationV6Len_Type=InetAddressPrefixLength
_ArrisRouterWanCurrentPrefixDelegationV6Len_Object=MibTableColumn
arrisRouterWanCurrentPrefixDelegationV6Len=_ArrisRouterWanCurrentPrefixDelegationV6Len_Object((1,3,6,1,4,1,4115,1,20,1,1,1,7,1,10),_ArrisRouterWanCurrentPrefixDelegationV6Len_Type())
arrisRouterWanCurrentPrefixDelegationV6Len.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWanCurrentPrefixDelegationV6Len.setStatus(_A)
_ArrisRouterWanCurrentPreferredLifetimeV6_Type=Integer32
_ArrisRouterWanCurrentPreferredLifetimeV6_Object=MibTableColumn
arrisRouterWanCurrentPreferredLifetimeV6=_ArrisRouterWanCurrentPreferredLifetimeV6_Object((1,3,6,1,4,1,4115,1,20,1,1,1,7,1,11),_ArrisRouterWanCurrentPreferredLifetimeV6_Type())
arrisRouterWanCurrentPreferredLifetimeV6.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWanCurrentPreferredLifetimeV6.setStatus(_A)
_ArrisRouterWanCurrentValidLifetimeV6_Type=Integer32
_ArrisRouterWanCurrentValidLifetimeV6_Object=MibTableColumn
arrisRouterWanCurrentValidLifetimeV6=_ArrisRouterWanCurrentValidLifetimeV6_Object((1,3,6,1,4,1,4115,1,20,1,1,1,7,1,12),_ArrisRouterWanCurrentValidLifetimeV6_Type())
arrisRouterWanCurrentValidLifetimeV6.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWanCurrentValidLifetimeV6.setStatus(_A)
class _ArrisRouterWanStaticFreeIdx_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_ArrisRouterWanStaticFreeIdx_Type.__name__=_H
_ArrisRouterWanStaticFreeIdx_Object=MibScalar
arrisRouterWanStaticFreeIdx=_ArrisRouterWanStaticFreeIdx_Object((1,3,6,1,4,1,4115,1,20,1,1,1,8),_ArrisRouterWanStaticFreeIdx_Type())
arrisRouterWanStaticFreeIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWanStaticFreeIdx.setStatus(_A)
_ArrisRouterWanStaticTable_Object=MibTable
arrisRouterWanStaticTable=_ArrisRouterWanStaticTable_Object((1,3,6,1,4,1,4115,1,20,1,1,1,9))
if mibBuilder.loadTexts:arrisRouterWanStaticTable.setStatus(_A)
_ArrisRouterWanStaticEntry_Object=MibTableRow
arrisRouterWanStaticEntry=_ArrisRouterWanStaticEntry_Object((1,3,6,1,4,1,4115,1,20,1,1,1,9,1))
arrisRouterWanStaticEntry.setIndexNames((0,_I,_w))
if mibBuilder.loadTexts:arrisRouterWanStaticEntry.setStatus(_A)
_ArrisRouterWanStaticIPIndex_Type=Unsigned32
_ArrisRouterWanStaticIPIndex_Object=MibTableColumn
arrisRouterWanStaticIPIndex=_ArrisRouterWanStaticIPIndex_Object((1,3,6,1,4,1,4115,1,20,1,1,1,9,1,1),_ArrisRouterWanStaticIPIndex_Type())
arrisRouterWanStaticIPIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:arrisRouterWanStaticIPIndex.setStatus(_A)
_ArrisRouterWanStaticIPAddrType_Type=InetAddressType
_ArrisRouterWanStaticIPAddrType_Object=MibTableColumn
arrisRouterWanStaticIPAddrType=_ArrisRouterWanStaticIPAddrType_Object((1,3,6,1,4,1,4115,1,20,1,1,1,9,1,2),_ArrisRouterWanStaticIPAddrType_Type())
arrisRouterWanStaticIPAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterWanStaticIPAddrType.setStatus(_A)
_ArrisRouterWanStaticIPAddr_Type=InetAddress
_ArrisRouterWanStaticIPAddr_Object=MibTableColumn
arrisRouterWanStaticIPAddr=_ArrisRouterWanStaticIPAddr_Object((1,3,6,1,4,1,4115,1,20,1,1,1,9,1,3),_ArrisRouterWanStaticIPAddr_Type())
arrisRouterWanStaticIPAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterWanStaticIPAddr.setStatus(_A)
_ArrisRouterWanStaticPrefix_Type=InetAddressPrefixLength
_ArrisRouterWanStaticPrefix_Object=MibTableColumn
arrisRouterWanStaticPrefix=_ArrisRouterWanStaticPrefix_Object((1,3,6,1,4,1,4115,1,20,1,1,1,9,1,4),_ArrisRouterWanStaticPrefix_Type())
arrisRouterWanStaticPrefix.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterWanStaticPrefix.setStatus(_A)
_ArrisRouterWanStaticGatewayType_Type=InetAddressType
_ArrisRouterWanStaticGatewayType_Object=MibTableColumn
arrisRouterWanStaticGatewayType=_ArrisRouterWanStaticGatewayType_Object((1,3,6,1,4,1,4115,1,20,1,1,1,9,1,5),_ArrisRouterWanStaticGatewayType_Type())
arrisRouterWanStaticGatewayType.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterWanStaticGatewayType.setStatus(_A)
_ArrisRouterWanStaticGateway_Type=InetAddress
_ArrisRouterWanStaticGateway_Object=MibTableColumn
arrisRouterWanStaticGateway=_ArrisRouterWanStaticGateway_Object((1,3,6,1,4,1,4115,1,20,1,1,1,9,1,6),_ArrisRouterWanStaticGateway_Type())
arrisRouterWanStaticGateway.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterWanStaticGateway.setStatus(_A)
_ArrisRouterWanStaticRowStatus_Type=RowStatus
_ArrisRouterWanStaticRowStatus_Object=MibTableColumn
arrisRouterWanStaticRowStatus=_ArrisRouterWanStaticRowStatus_Object((1,3,6,1,4,1,4115,1,20,1,1,1,9,1,7),_ArrisRouterWanStaticRowStatus_Type())
arrisRouterWanStaticRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterWanStaticRowStatus.setStatus(_A)
_ArrisRouterWanDelegatedPrefixLength_Type=InetAddressPrefixLength
_ArrisRouterWanDelegatedPrefixLength_Object=MibTableColumn
arrisRouterWanDelegatedPrefixLength=_ArrisRouterWanDelegatedPrefixLength_Object((1,3,6,1,4,1,4115,1,20,1,1,1,9,1,8),_ArrisRouterWanDelegatedPrefixLength_Type())
arrisRouterWanDelegatedPrefixLength.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterWanDelegatedPrefixLength.setStatus(_A)
_ArrisRouterWanDelegatedPrefix_Type=InetAddressIPv6
_ArrisRouterWanDelegatedPrefix_Object=MibTableColumn
arrisRouterWanDelegatedPrefix=_ArrisRouterWanDelegatedPrefix_Object((1,3,6,1,4,1,4115,1,20,1,1,1,9,1,9),_ArrisRouterWanDelegatedPrefix_Type())
arrisRouterWanDelegatedPrefix.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterWanDelegatedPrefix.setStatus(_A)
_ArrisRouterWanTunnelObjects_ObjectIdentity=ObjectIdentity
arrisRouterWanTunnelObjects=_ArrisRouterWanTunnelObjects_ObjectIdentity((1,3,6,1,4,1,4115,1,20,1,1,1,10))
class _ArrisRouterWanUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ArrisRouterWanUserName_Type.__name__=_G
_ArrisRouterWanUserName_Object=MibScalar
arrisRouterWanUserName=_ArrisRouterWanUserName_Object((1,3,6,1,4,1,4115,1,20,1,1,1,10,1),_ArrisRouterWanUserName_Type())
arrisRouterWanUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWanUserName.setStatus(_A)
class _ArrisRouterWanPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ArrisRouterWanPassword_Type.__name__=_G
_ArrisRouterWanPassword_Object=MibScalar
arrisRouterWanPassword=_ArrisRouterWanPassword_Object((1,3,6,1,4,1,4115,1,20,1,1,1,10,2),_ArrisRouterWanPassword_Type())
arrisRouterWanPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWanPassword.setStatus(_A)
_ArrisRouterWanEnableIdleTimeout_Type=TruthValue
_ArrisRouterWanEnableIdleTimeout_Object=MibScalar
arrisRouterWanEnableIdleTimeout=_ArrisRouterWanEnableIdleTimeout_Object((1,3,6,1,4,1,4115,1,20,1,1,1,10,3),_ArrisRouterWanEnableIdleTimeout_Type())
arrisRouterWanEnableIdleTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWanEnableIdleTimeout.setStatus(_A)
class _ArrisRouterWanIdleTimeout_Type(Unsigned32):defaultValue=300
_ArrisRouterWanIdleTimeout_Type.__name__=_H
_ArrisRouterWanIdleTimeout_Object=MibScalar
arrisRouterWanIdleTimeout=_ArrisRouterWanIdleTimeout_Object((1,3,6,1,4,1,4115,1,20,1,1,1,10,4),_ArrisRouterWanIdleTimeout_Type())
arrisRouterWanIdleTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWanIdleTimeout.setStatus(_A)
if mibBuilder.loadTexts:arrisRouterWanIdleTimeout.setUnits(_M)
_ArrisRouterWanTunnelAddrType_Type=InetAddressType
_ArrisRouterWanTunnelAddrType_Object=MibScalar
arrisRouterWanTunnelAddrType=_ArrisRouterWanTunnelAddrType_Object((1,3,6,1,4,1,4115,1,20,1,1,1,10,5),_ArrisRouterWanTunnelAddrType_Type())
arrisRouterWanTunnelAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWanTunnelAddrType.setStatus(_A)
_ArrisRouterWanTunnelAddr_Type=InetAddress
_ArrisRouterWanTunnelAddr_Object=MibScalar
arrisRouterWanTunnelAddr=_ArrisRouterWanTunnelAddr_Object((1,3,6,1,4,1,4115,1,20,1,1,1,10,6),_ArrisRouterWanTunnelAddr_Type())
arrisRouterWanTunnelAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWanTunnelAddr.setStatus(_A)
class _ArrisRouterWanTunnelHostName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_ArrisRouterWanTunnelHostName_Type.__name__=_G
_ArrisRouterWanTunnelHostName_Object=MibScalar
arrisRouterWanTunnelHostName=_ArrisRouterWanTunnelHostName_Object((1,3,6,1,4,1,4115,1,20,1,1,1,10,7),_ArrisRouterWanTunnelHostName_Type())
arrisRouterWanTunnelHostName.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWanTunnelHostName.setStatus(_A)
_ArrisRouterWanEnableKeepAlive_Type=TruthValue
_ArrisRouterWanEnableKeepAlive_Object=MibScalar
arrisRouterWanEnableKeepAlive=_ArrisRouterWanEnableKeepAlive_Object((1,3,6,1,4,1,4115,1,20,1,1,1,10,8),_ArrisRouterWanEnableKeepAlive_Type())
arrisRouterWanEnableKeepAlive.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWanEnableKeepAlive.setStatus(_A)
class _ArrisRouterWanKeepAliveTimeout_Type(Unsigned32):defaultValue=30
_ArrisRouterWanKeepAliveTimeout_Type.__name__=_H
_ArrisRouterWanKeepAliveTimeout_Object=MibScalar
arrisRouterWanKeepAliveTimeout=_ArrisRouterWanKeepAliveTimeout_Object((1,3,6,1,4,1,4115,1,20,1,1,1,10,9),_ArrisRouterWanKeepAliveTimeout_Type())
arrisRouterWanKeepAliveTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWanKeepAliveTimeout.setStatus(_A)
if mibBuilder.loadTexts:arrisRouterWanKeepAliveTimeout.setUnits(_M)
_ArrisRouterWanDNSObjects_ObjectIdentity=ObjectIdentity
arrisRouterWanDNSObjects=_ArrisRouterWanDNSObjects_ObjectIdentity((1,3,6,1,4,1,4115,1,20,1,1,1,11))
_ArrisRouterWanUseAutoDNS_Type=TruthValue
_ArrisRouterWanUseAutoDNS_Object=MibScalar
arrisRouterWanUseAutoDNS=_ArrisRouterWanUseAutoDNS_Object((1,3,6,1,4,1,4115,1,20,1,1,1,11,1),_ArrisRouterWanUseAutoDNS_Type())
arrisRouterWanUseAutoDNS.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWanUseAutoDNS.setStatus(_A)
_ArrisRouterWanCurrentDNSTable_Object=MibTable
arrisRouterWanCurrentDNSTable=_ArrisRouterWanCurrentDNSTable_Object((1,3,6,1,4,1,4115,1,20,1,1,1,11,2))
if mibBuilder.loadTexts:arrisRouterWanCurrentDNSTable.setStatus(_A)
_ArrisRouterWanCurrentDNSEntry_Object=MibTableRow
arrisRouterWanCurrentDNSEntry=_ArrisRouterWanCurrentDNSEntry_Object((1,3,6,1,4,1,4115,1,20,1,1,1,11,2,1))
arrisRouterWanCurrentDNSEntry.setIndexNames((0,_I,_x))
if mibBuilder.loadTexts:arrisRouterWanCurrentDNSEntry.setStatus(_A)
class _ArrisRouterWanCurrentDNSIPIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_ArrisRouterWanCurrentDNSIPIndex_Type.__name__=_H
_ArrisRouterWanCurrentDNSIPIndex_Object=MibTableColumn
arrisRouterWanCurrentDNSIPIndex=_ArrisRouterWanCurrentDNSIPIndex_Object((1,3,6,1,4,1,4115,1,20,1,1,1,11,2,1,1),_ArrisRouterWanCurrentDNSIPIndex_Type())
arrisRouterWanCurrentDNSIPIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:arrisRouterWanCurrentDNSIPIndex.setStatus(_A)
_ArrisRouterWanCurrentDNSIPAddrType_Type=InetAddressType
_ArrisRouterWanCurrentDNSIPAddrType_Object=MibTableColumn
arrisRouterWanCurrentDNSIPAddrType=_ArrisRouterWanCurrentDNSIPAddrType_Object((1,3,6,1,4,1,4115,1,20,1,1,1,11,2,1,2),_ArrisRouterWanCurrentDNSIPAddrType_Type())
arrisRouterWanCurrentDNSIPAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWanCurrentDNSIPAddrType.setStatus(_A)
_ArrisRouterWanCurrentDNSIPAddr_Type=InetAddress
_ArrisRouterWanCurrentDNSIPAddr_Object=MibTableColumn
arrisRouterWanCurrentDNSIPAddr=_ArrisRouterWanCurrentDNSIPAddr_Object((1,3,6,1,4,1,4115,1,20,1,1,1,11,2,1,3),_ArrisRouterWanCurrentDNSIPAddr_Type())
arrisRouterWanCurrentDNSIPAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWanCurrentDNSIPAddr.setStatus(_A)
_ArrisRouterWanStaticDNSTable_Object=MibTable
arrisRouterWanStaticDNSTable=_ArrisRouterWanStaticDNSTable_Object((1,3,6,1,4,1,4115,1,20,1,1,1,11,4))
if mibBuilder.loadTexts:arrisRouterWanStaticDNSTable.setStatus(_A)
_ArrisRouterWanStaticDNSEntry_Object=MibTableRow
arrisRouterWanStaticDNSEntry=_ArrisRouterWanStaticDNSEntry_Object((1,3,6,1,4,1,4115,1,20,1,1,1,11,4,1))
arrisRouterWanStaticDNSEntry.setIndexNames((0,_I,_y))
if mibBuilder.loadTexts:arrisRouterWanStaticDNSEntry.setStatus(_A)
class _ArrisRouterWanStaticDNSIPIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_ArrisRouterWanStaticDNSIPIndex_Type.__name__=_H
_ArrisRouterWanStaticDNSIPIndex_Object=MibTableColumn
arrisRouterWanStaticDNSIPIndex=_ArrisRouterWanStaticDNSIPIndex_Object((1,3,6,1,4,1,4115,1,20,1,1,1,11,4,1,1),_ArrisRouterWanStaticDNSIPIndex_Type())
arrisRouterWanStaticDNSIPIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:arrisRouterWanStaticDNSIPIndex.setStatus(_A)
_ArrisRouterWanStaticDNSIPAddrType_Type=InetAddressType
_ArrisRouterWanStaticDNSIPAddrType_Object=MibTableColumn
arrisRouterWanStaticDNSIPAddrType=_ArrisRouterWanStaticDNSIPAddrType_Object((1,3,6,1,4,1,4115,1,20,1,1,1,11,4,1,2),_ArrisRouterWanStaticDNSIPAddrType_Type())
arrisRouterWanStaticDNSIPAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterWanStaticDNSIPAddrType.setStatus(_A)
_ArrisRouterWanStaticDNSIPAddr_Type=InetAddress
_ArrisRouterWanStaticDNSIPAddr_Object=MibTableColumn
arrisRouterWanStaticDNSIPAddr=_ArrisRouterWanStaticDNSIPAddr_Object((1,3,6,1,4,1,4115,1,20,1,1,1,11,4,1,3),_ArrisRouterWanStaticDNSIPAddr_Type())
arrisRouterWanStaticDNSIPAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterWanStaticDNSIPAddr.setStatus(_A)
_ArrisRouterWanStaticDNSRowStatus_Type=RowStatus
_ArrisRouterWanStaticDNSRowStatus_Object=MibTableColumn
arrisRouterWanStaticDNSRowStatus=_ArrisRouterWanStaticDNSRowStatus_Object((1,3,6,1,4,1,4115,1,20,1,1,1,11,4,1,4),_ArrisRouterWanStaticDNSRowStatus_Type())
arrisRouterWanStaticDNSRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterWanStaticDNSRowStatus.setStatus(_A)
_ArrisRouterWanDHCPObjects_ObjectIdentity=ObjectIdentity
arrisRouterWanDHCPObjects=_ArrisRouterWanDHCPObjects_ObjectIdentity((1,3,6,1,4,1,4115,1,20,1,1,1,12))
class _ArrisRouterWanRenewLease_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_X,0),(_Y,1)))
_ArrisRouterWanRenewLease_Type.__name__=_D
_ArrisRouterWanRenewLease_Object=MibScalar
arrisRouterWanRenewLease=_ArrisRouterWanRenewLease_Object((1,3,6,1,4,1,4115,1,20,1,1,1,12,1),_ArrisRouterWanRenewLease_Type())
arrisRouterWanRenewLease.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWanRenewLease.setStatus(_A)
class _ArrisRouterWanReleaseLease_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_X,0),(_Y,1)))
_ArrisRouterWanReleaseLease_Type.__name__=_D
_ArrisRouterWanReleaseLease_Object=MibScalar
arrisRouterWanReleaseLease=_ArrisRouterWanReleaseLease_Object((1,3,6,1,4,1,4115,1,20,1,1,1,12,2),_ArrisRouterWanReleaseLease_Type())
arrisRouterWanReleaseLease.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWanReleaseLease.setStatus(_A)
_ArrisRouterWanDHCPDuration_Type=Unsigned32
_ArrisRouterWanDHCPDuration_Object=MibScalar
arrisRouterWanDHCPDuration=_ArrisRouterWanDHCPDuration_Object((1,3,6,1,4,1,4115,1,20,1,1,1,12,3),_ArrisRouterWanDHCPDuration_Type())
arrisRouterWanDHCPDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWanDHCPDuration.setStatus(_A)
if mibBuilder.loadTexts:arrisRouterWanDHCPDuration.setUnits(_M)
_ArrisRouterWanDHCPExpire_Type=DateAndTime
_ArrisRouterWanDHCPExpire_Object=MibScalar
arrisRouterWanDHCPExpire=_ArrisRouterWanDHCPExpire_Object((1,3,6,1,4,1,4115,1,20,1,1,1,12,4),_ArrisRouterWanDHCPExpire_Type())
arrisRouterWanDHCPExpire.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWanDHCPExpire.setStatus(_A)
class _ArrisRouterWanRenewLeaseV6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_X,0),(_Y,1)))
_ArrisRouterWanRenewLeaseV6_Type.__name__=_D
_ArrisRouterWanRenewLeaseV6_Object=MibScalar
arrisRouterWanRenewLeaseV6=_ArrisRouterWanRenewLeaseV6_Object((1,3,6,1,4,1,4115,1,20,1,1,1,12,5),_ArrisRouterWanRenewLeaseV6_Type())
arrisRouterWanRenewLeaseV6.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWanRenewLeaseV6.setStatus(_A)
class _ArrisRouterWanReleaseLeaseV6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_X,0),(_Y,1)))
_ArrisRouterWanReleaseLeaseV6_Type.__name__=_D
_ArrisRouterWanReleaseLeaseV6_Object=MibScalar
arrisRouterWanReleaseLeaseV6=_ArrisRouterWanReleaseLeaseV6_Object((1,3,6,1,4,1,4115,1,20,1,1,1,12,6),_ArrisRouterWanReleaseLeaseV6_Type())
arrisRouterWanReleaseLeaseV6.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWanReleaseLeaseV6.setStatus(_A)
_ArrisRouterWanDHCPDurationV6_Type=Unsigned32
_ArrisRouterWanDHCPDurationV6_Object=MibScalar
arrisRouterWanDHCPDurationV6=_ArrisRouterWanDHCPDurationV6_Object((1,3,6,1,4,1,4115,1,20,1,1,1,12,7),_ArrisRouterWanDHCPDurationV6_Type())
arrisRouterWanDHCPDurationV6.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWanDHCPDurationV6.setStatus(_A)
if mibBuilder.loadTexts:arrisRouterWanDHCPDurationV6.setUnits(_M)
_ArrisRouterWanDHCPExpireV6_Type=DateAndTime
_ArrisRouterWanDHCPExpireV6_Object=MibScalar
arrisRouterWanDHCPExpireV6=_ArrisRouterWanDHCPExpireV6_Object((1,3,6,1,4,1,4115,1,20,1,1,1,12,8),_ArrisRouterWanDHCPExpireV6_Type())
arrisRouterWanDHCPExpireV6.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWanDHCPExpireV6.setStatus(_A)
_ArrisRouterWanDhcpSrvIPAddr_Type=InetAddress
_ArrisRouterWanDhcpSrvIPAddr_Object=MibScalar
arrisRouterWanDhcpSrvIPAddr=_ArrisRouterWanDhcpSrvIPAddr_Object((1,3,6,1,4,1,4115,1,20,1,1,1,12,9),_ArrisRouterWanDhcpSrvIPAddr_Type())
arrisRouterWanDhcpSrvIPAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWanDhcpSrvIPAddr.setStatus(_A)
class _ArrisRouterWanDhcpOpt43Sub02_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('erouter',0),('ecm',1)))
_ArrisRouterWanDhcpOpt43Sub02_Type.__name__=_D
_ArrisRouterWanDhcpOpt43Sub02_Object=MibScalar
arrisRouterWanDhcpOpt43Sub02=_ArrisRouterWanDhcpOpt43Sub02_Object((1,3,6,1,4,1,4115,1,20,1,1,1,12,10),_ArrisRouterWanDhcpOpt43Sub02_Type())
arrisRouterWanDhcpOpt43Sub02.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWanDhcpOpt43Sub02.setStatus(_A)
class _ArrisRouterWanDHCPDUIDV6_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,130))
_ArrisRouterWanDHCPDUIDV6_Type.__name__=_G
_ArrisRouterWanDHCPDUIDV6_Object=MibScalar
arrisRouterWanDHCPDUIDV6=_ArrisRouterWanDHCPDUIDV6_Object((1,3,6,1,4,1,4115,1,20,1,1,1,12,11),_ArrisRouterWanDHCPDUIDV6_Type())
arrisRouterWanDHCPDUIDV6.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWanDHCPDUIDV6.setStatus(_A)
_ArrisRouterWanDHCPSrvAddrV6_Type=InetAddressIPv6
_ArrisRouterWanDHCPSrvAddrV6_Object=MibScalar
arrisRouterWanDHCPSrvAddrV6=_ArrisRouterWanDHCPSrvAddrV6_Object((1,3,6,1,4,1,4115,1,20,1,1,1,12,12),_ArrisRouterWanDHCPSrvAddrV6_Type())
arrisRouterWanDHCPSrvAddrV6.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWanDHCPSrvAddrV6.setStatus(_A)
class _ArrisRouterWanDHCPSrvDUIDV6_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,130))
_ArrisRouterWanDHCPSrvDUIDV6_Type.__name__=_G
_ArrisRouterWanDHCPSrvDUIDV6_Object=MibScalar
arrisRouterWanDHCPSrvDUIDV6=_ArrisRouterWanDHCPSrvDUIDV6_Object((1,3,6,1,4,1,4115,1,20,1,1,1,12,13),_ArrisRouterWanDHCPSrvDUIDV6_Type())
arrisRouterWanDHCPSrvDUIDV6.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWanDHCPSrvDUIDV6.setStatus(_A)
_ArrisRouterWanIFMacAddr_Type=MacAddress
_ArrisRouterWanIFMacAddr_Object=MibScalar
arrisRouterWanIFMacAddr=_ArrisRouterWanIFMacAddr_Object((1,3,6,1,4,1,4115,1,20,1,1,1,13),_ArrisRouterWanIFMacAddr_Type())
arrisRouterWanIFMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWanIFMacAddr.setStatus(_A)
class _ArrisRouterWanConnTypeV6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_N,0),(_V,1),(_W,2)))
_ArrisRouterWanConnTypeV6_Type.__name__=_D
_ArrisRouterWanConnTypeV6_Object=MibScalar
arrisRouterWanConnTypeV6=_ArrisRouterWanConnTypeV6_Object((1,3,6,1,4,1,4115,1,20,1,1,1,16),_ArrisRouterWanConnTypeV6_Type())
arrisRouterWanConnTypeV6.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWanConnTypeV6.setStatus(_A)
class _ArrisRouterWanIPProvMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('disabledBridge',0),('ipv4',1),('ipv6',2),('dualStack',3)))
_ArrisRouterWanIPProvMode_Type.__name__=_D
_ArrisRouterWanIPProvMode_Object=MibScalar
arrisRouterWanIPProvMode=_ArrisRouterWanIPProvMode_Object((1,3,6,1,4,1,4115,1,20,1,1,1,17),_ArrisRouterWanIPProvMode_Type())
arrisRouterWanIPProvMode.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWanIPProvMode.setStatus(_A)
_ArrisRouterDSLiteWanObjects_ObjectIdentity=ObjectIdentity
arrisRouterDSLiteWanObjects=_ArrisRouterDSLiteWanObjects_ObjectIdentity((1,3,6,1,4,1,4115,1,20,1,1,1,18))
class _ArrisRouterDSLiteWanEnable_Type(TruthValue):defaultValue=1
_ArrisRouterDSLiteWanEnable_Type.__name__=_F
_ArrisRouterDSLiteWanEnable_Object=MibScalar
arrisRouterDSLiteWanEnable=_ArrisRouterDSLiteWanEnable_Object((1,3,6,1,4,1,4115,1,20,1,1,1,18,1),_ArrisRouterDSLiteWanEnable_Type())
arrisRouterDSLiteWanEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterDSLiteWanEnable.setStatus(_A)
_ArrisRouterDSLiteWanLSNATAddrType_Type=InetAddressType
_ArrisRouterDSLiteWanLSNATAddrType_Object=MibScalar
arrisRouterDSLiteWanLSNATAddrType=_ArrisRouterDSLiteWanLSNATAddrType_Object((1,3,6,1,4,1,4115,1,20,1,1,1,18,2),_ArrisRouterDSLiteWanLSNATAddrType_Type())
arrisRouterDSLiteWanLSNATAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterDSLiteWanLSNATAddrType.setStatus(_A)
_ArrisRouterDSLiteWanLSNATAddr_Type=InetAddressIPv6
_ArrisRouterDSLiteWanLSNATAddr_Object=MibScalar
arrisRouterDSLiteWanLSNATAddr=_ArrisRouterDSLiteWanLSNATAddr_Object((1,3,6,1,4,1,4115,1,20,1,1,1,18,3),_ArrisRouterDSLiteWanLSNATAddr_Type())
arrisRouterDSLiteWanLSNATAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterDSLiteWanLSNATAddr.setStatus(_A)
class _ArrisRouterDSLiteTcpMssClamping_Type(TruthValue):defaultValue=1
_ArrisRouterDSLiteTcpMssClamping_Type.__name__=_F
_ArrisRouterDSLiteTcpMssClamping_Object=MibScalar
arrisRouterDSLiteTcpMssClamping=_ArrisRouterDSLiteTcpMssClamping_Object((1,3,6,1,4,1,4115,1,20,1,1,1,18,4),_ArrisRouterDSLiteTcpMssClamping_Type())
arrisRouterDSLiteTcpMssClamping.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterDSLiteTcpMssClamping.setStatus(_A)
_ArrisRouterDSLiteTcpMssValue_Type=Unsigned32
_ArrisRouterDSLiteTcpMssValue_Object=MibScalar
arrisRouterDSLiteTcpMssValue=_ArrisRouterDSLiteTcpMssValue_Object((1,3,6,1,4,1,4115,1,20,1,1,1,18,5),_ArrisRouterDSLiteTcpMssValue_Type())
arrisRouterDSLiteTcpMssValue.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterDSLiteTcpMssValue.setStatus(_A)
_ArrisRouterDSLiteWanResolvedAddr_Type=InetAddressIPv6
_ArrisRouterDSLiteWanResolvedAddr_Object=MibScalar
arrisRouterDSLiteWanResolvedAddr=_ArrisRouterDSLiteWanResolvedAddr_Object((1,3,6,1,4,1,4115,1,20,1,1,1,18,6),_ArrisRouterDSLiteWanResolvedAddr_Type())
arrisRouterDSLiteWanResolvedAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterDSLiteWanResolvedAddr.setStatus(_A)
_ArrisRouterSoftGreWanObjects_ObjectIdentity=ObjectIdentity
arrisRouterSoftGreWanObjects=_ArrisRouterSoftGreWanObjects_ObjectIdentity((1,3,6,1,4,1,4115,1,20,1,1,1,19))
_ArrisRouterSoftGreWanTable_Object=MibTable
arrisRouterSoftGreWanTable=_ArrisRouterSoftGreWanTable_Object((1,3,6,1,4,1,4115,1,20,1,1,1,19,1))
if mibBuilder.loadTexts:arrisRouterSoftGreWanTable.setStatus(_A)
_ArrisRouterSoftGreWanEntry_Object=MibTableRow
arrisRouterSoftGreWanEntry=_ArrisRouterSoftGreWanEntry_Object((1,3,6,1,4,1,4115,1,20,1,1,1,19,1,1))
arrisRouterSoftGreWanEntry.setIndexNames((0,_K,_L))
if mibBuilder.loadTexts:arrisRouterSoftGreWanEntry.setStatus(_A)
class _ArrisRouterSoftGreWanEnable_Type(TruthValue):defaultValue=2
_ArrisRouterSoftGreWanEnable_Type.__name__=_F
_ArrisRouterSoftGreWanEnable_Object=MibTableColumn
arrisRouterSoftGreWanEnable=_ArrisRouterSoftGreWanEnable_Object((1,3,6,1,4,1,4115,1,20,1,1,1,19,1,1,1),_ArrisRouterSoftGreWanEnable_Type())
arrisRouterSoftGreWanEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterSoftGreWanEnable.setStatus(_A)
_ArrisRouterSoftGreMappedInterface_Type=Unsigned32
_ArrisRouterSoftGreMappedInterface_Object=MibTableColumn
arrisRouterSoftGreMappedInterface=_ArrisRouterSoftGreMappedInterface_Object((1,3,6,1,4,1,4115,1,20,1,1,1,19,1,1,2),_ArrisRouterSoftGreMappedInterface_Type())
arrisRouterSoftGreMappedInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterSoftGreMappedInterface.setStatus(_A)
class _ArrisRouterSoftGreMaxSessions_Type(Integer32):defaultValue=5
_ArrisRouterSoftGreMaxSessions_Type.__name__=_D
_ArrisRouterSoftGreMaxSessions_Object=MibTableColumn
arrisRouterSoftGreMaxSessions=_ArrisRouterSoftGreMaxSessions_Object((1,3,6,1,4,1,4115,1,20,1,1,1,19,1,1,3),_ArrisRouterSoftGreMaxSessions_Type())
arrisRouterSoftGreMaxSessions.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterSoftGreMaxSessions.setStatus(_A)
class _ArrisRouterSoftGreWanControllerFqdn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ArrisRouterSoftGreWanControllerFqdn_Type.__name__=_G
_ArrisRouterSoftGreWanControllerFqdn_Object=MibTableColumn
arrisRouterSoftGreWanControllerFqdn=_ArrisRouterSoftGreWanControllerFqdn_Object((1,3,6,1,4,1,4115,1,20,1,1,1,19,1,1,4),_ArrisRouterSoftGreWanControllerFqdn_Type())
arrisRouterSoftGreWanControllerFqdn.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterSoftGreWanControllerFqdn.setStatus(_A)
_ArrisRouterSoftGreWanControllerProvisionedSecondaryIpAddressType_Type=InetAddressType
_ArrisRouterSoftGreWanControllerProvisionedSecondaryIpAddressType_Object=MibTableColumn
arrisRouterSoftGreWanControllerProvisionedSecondaryIpAddressType=_ArrisRouterSoftGreWanControllerProvisionedSecondaryIpAddressType_Object((1,3,6,1,4,1,4115,1,20,1,1,1,19,1,1,5),_ArrisRouterSoftGreWanControllerProvisionedSecondaryIpAddressType_Type())
arrisRouterSoftGreWanControllerProvisionedSecondaryIpAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterSoftGreWanControllerProvisionedSecondaryIpAddressType.setStatus(_A)
_ArrisRouterSoftGreWanControllerProvisionedSecondaryIpAddress_Type=InetAddress
_ArrisRouterSoftGreWanControllerProvisionedSecondaryIpAddress_Object=MibTableColumn
arrisRouterSoftGreWanControllerProvisionedSecondaryIpAddress=_ArrisRouterSoftGreWanControllerProvisionedSecondaryIpAddress_Object((1,3,6,1,4,1,4115,1,20,1,1,1,19,1,1,6),_ArrisRouterSoftGreWanControllerProvisionedSecondaryIpAddress_Type())
arrisRouterSoftGreWanControllerProvisionedSecondaryIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterSoftGreWanControllerProvisionedSecondaryIpAddress.setStatus(_A)
class _ArrisRouterSoftGreWanFailoverPingCount_Type(Integer32):defaultValue=3
_ArrisRouterSoftGreWanFailoverPingCount_Type.__name__=_D
_ArrisRouterSoftGreWanFailoverPingCount_Object=MibTableColumn
arrisRouterSoftGreWanFailoverPingCount=_ArrisRouterSoftGreWanFailoverPingCount_Object((1,3,6,1,4,1,4115,1,20,1,1,1,19,1,1,7),_ArrisRouterSoftGreWanFailoverPingCount_Type())
arrisRouterSoftGreWanFailoverPingCount.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterSoftGreWanFailoverPingCount.setStatus(_A)
class _ArrisRouterSoftGreWanFailoverPingInterval_Type(Integer32):defaultValue=60
_ArrisRouterSoftGreWanFailoverPingInterval_Type.__name__=_D
_ArrisRouterSoftGreWanFailoverPingInterval_Object=MibTableColumn
arrisRouterSoftGreWanFailoverPingInterval=_ArrisRouterSoftGreWanFailoverPingInterval_Object((1,3,6,1,4,1,4115,1,20,1,1,1,19,1,1,8),_ArrisRouterSoftGreWanFailoverPingInterval_Type())
arrisRouterSoftGreWanFailoverPingInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterSoftGreWanFailoverPingInterval.setStatus(_A)
class _ArrisRouterSoftGreWanFailoverThreshold_Type(Integer32):defaultValue=3
_ArrisRouterSoftGreWanFailoverThreshold_Type.__name__=_D
_ArrisRouterSoftGreWanFailoverThreshold_Object=MibTableColumn
arrisRouterSoftGreWanFailoverThreshold=_ArrisRouterSoftGreWanFailoverThreshold_Object((1,3,6,1,4,1,4115,1,20,1,1,1,19,1,1,9),_ArrisRouterSoftGreWanFailoverThreshold_Type())
arrisRouterSoftGreWanFailoverThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterSoftGreWanFailoverThreshold.setStatus(_A)
class _ArrisRouterSoftGreCircuitIdEnabled_Type(TruthValue):defaultValue=1
_ArrisRouterSoftGreCircuitIdEnabled_Type.__name__=_F
_ArrisRouterSoftGreCircuitIdEnabled_Object=MibTableColumn
arrisRouterSoftGreCircuitIdEnabled=_ArrisRouterSoftGreCircuitIdEnabled_Object((1,3,6,1,4,1,4115,1,20,1,1,1,19,1,1,10),_ArrisRouterSoftGreCircuitIdEnabled_Type())
arrisRouterSoftGreCircuitIdEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterSoftGreCircuitIdEnabled.setStatus(_A)
class _ArrisRouterSoftGreRemoteIdEnabled_Type(TruthValue):defaultValue=1
_ArrisRouterSoftGreRemoteIdEnabled_Type.__name__=_F
_ArrisRouterSoftGreRemoteIdEnabled_Object=MibTableColumn
arrisRouterSoftGreRemoteIdEnabled=_ArrisRouterSoftGreRemoteIdEnabled_Object((1,3,6,1,4,1,4115,1,20,1,1,1,19,1,1,11),_ArrisRouterSoftGreRemoteIdEnabled_Type())
arrisRouterSoftGreRemoteIdEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterSoftGreRemoteIdEnabled.setStatus(_A)
class _ArrisRouterSoftGreRadiusEnabled_Type(TruthValue):defaultValue=2
_ArrisRouterSoftGreRadiusEnabled_Type.__name__=_F
_ArrisRouterSoftGreRadiusEnabled_Object=MibTableColumn
arrisRouterSoftGreRadiusEnabled=_ArrisRouterSoftGreRadiusEnabled_Object((1,3,6,1,4,1,4115,1,20,1,1,1,19,1,1,12),_ArrisRouterSoftGreRadiusEnabled_Type())
arrisRouterSoftGreRadiusEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterSoftGreRadiusEnabled.setStatus(_A)
_ArrisRouterSoftGreRadiusServerAddressType_Type=InetAddressType
_ArrisRouterSoftGreRadiusServerAddressType_Object=MibTableColumn
arrisRouterSoftGreRadiusServerAddressType=_ArrisRouterSoftGreRadiusServerAddressType_Object((1,3,6,1,4,1,4115,1,20,1,1,1,19,1,1,13),_ArrisRouterSoftGreRadiusServerAddressType_Type())
arrisRouterSoftGreRadiusServerAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterSoftGreRadiusServerAddressType.setStatus(_A)
_ArrisRouterSoftGreRadiusServerAddress_Type=InetAddress
_ArrisRouterSoftGreRadiusServerAddress_Object=MibTableColumn
arrisRouterSoftGreRadiusServerAddress=_ArrisRouterSoftGreRadiusServerAddress_Object((1,3,6,1,4,1,4115,1,20,1,1,1,19,1,1,14),_ArrisRouterSoftGreRadiusServerAddress_Type())
arrisRouterSoftGreRadiusServerAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterSoftGreRadiusServerAddress.setStatus(_A)
class _ArrisRouterSoftGreRadiusServerPort_Type(Unsigned32):defaultValue=1812
_ArrisRouterSoftGreRadiusServerPort_Type.__name__=_H
_ArrisRouterSoftGreRadiusServerPort_Object=MibTableColumn
arrisRouterSoftGreRadiusServerPort=_ArrisRouterSoftGreRadiusServerPort_Object((1,3,6,1,4,1,4115,1,20,1,1,1,19,1,1,15),_ArrisRouterSoftGreRadiusServerPort_Type())
arrisRouterSoftGreRadiusServerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterSoftGreRadiusServerPort.setStatus(_A)
class _ArrisRouterSoftGreRadiusKey_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_ArrisRouterSoftGreRadiusKey_Type.__name__=_G
_ArrisRouterSoftGreRadiusKey_Object=MibTableColumn
arrisRouterSoftGreRadiusKey=_ArrisRouterSoftGreRadiusKey_Object((1,3,6,1,4,1,4115,1,20,1,1,1,19,1,1,16),_ArrisRouterSoftGreRadiusKey_Type())
arrisRouterSoftGreRadiusKey.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterSoftGreRadiusKey.setStatus(_A)
_ArrisRouterSoftGreRadiusReAuthInterval_Type=Unsigned32
_ArrisRouterSoftGreRadiusReAuthInterval_Object=MibTableColumn
arrisRouterSoftGreRadiusReAuthInterval=_ArrisRouterSoftGreRadiusReAuthInterval_Object((1,3,6,1,4,1,4115,1,20,1,1,1,19,1,1,17),_ArrisRouterSoftGreRadiusReAuthInterval_Type())
arrisRouterSoftGreRadiusReAuthInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterSoftGreRadiusReAuthInterval.setStatus(_A)
if mibBuilder.loadTexts:arrisRouterSoftGreRadiusReAuthInterval.setUnits(_M)
class _ArrisRouterSoftGreVlanQEnable_Type(TruthValue):defaultValue=1
_ArrisRouterSoftGreVlanQEnable_Type.__name__=_F
_ArrisRouterSoftGreVlanQEnable_Object=MibTableColumn
arrisRouterSoftGreVlanQEnable=_ArrisRouterSoftGreVlanQEnable_Object((1,3,6,1,4,1,4115,1,20,1,1,1,19,1,1,18),_ArrisRouterSoftGreVlanQEnable_Type())
arrisRouterSoftGreVlanQEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterSoftGreVlanQEnable.setStatus(_A)
class _ArrisRouterSoftGreWanDscp_Type(DscpOrAny):defaultValue=0
_ArrisRouterSoftGreWanDscp_Type.__name__=_n
_ArrisRouterSoftGreWanDscp_Object=MibTableColumn
arrisRouterSoftGreWanDscp=_ArrisRouterSoftGreWanDscp_Object((1,3,6,1,4,1,4115,1,20,1,1,1,19,1,1,19),_ArrisRouterSoftGreWanDscp_Type())
arrisRouterSoftGreWanDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterSoftGreWanDscp.setStatus(_A)
class _ArrisRouterSoftGreWanDNSRetryTimer_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,1800))
_ArrisRouterSoftGreWanDNSRetryTimer_Type.__name__=_H
_ArrisRouterSoftGreWanDNSRetryTimer_Object=MibTableColumn
arrisRouterSoftGreWanDNSRetryTimer=_ArrisRouterSoftGreWanDNSRetryTimer_Object((1,3,6,1,4,1,4115,1,20,1,1,1,19,1,1,20),_ArrisRouterSoftGreWanDNSRetryTimer_Type())
arrisRouterSoftGreWanDNSRetryTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterSoftGreWanDNSRetryTimer.setStatus(_A)
_ArrisRouterSoftGreWanCurrentControllerIPAddressType_Type=InetAddressType
_ArrisRouterSoftGreWanCurrentControllerIPAddressType_Object=MibTableColumn
arrisRouterSoftGreWanCurrentControllerIPAddressType=_ArrisRouterSoftGreWanCurrentControllerIPAddressType_Object((1,3,6,1,4,1,4115,1,20,1,1,1,19,1,1,21),_ArrisRouterSoftGreWanCurrentControllerIPAddressType_Type())
arrisRouterSoftGreWanCurrentControllerIPAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterSoftGreWanCurrentControllerIPAddressType.setStatus(_A)
_ArrisRouterSoftGreWanCurrentControllerIPAddress_Type=InetAddress
_ArrisRouterSoftGreWanCurrentControllerIPAddress_Object=MibTableColumn
arrisRouterSoftGreWanCurrentControllerIPAddress=_ArrisRouterSoftGreWanCurrentControllerIPAddress_Object((1,3,6,1,4,1,4115,1,20,1,1,1,19,1,1,22),_ArrisRouterSoftGreWanCurrentControllerIPAddress_Type())
arrisRouterSoftGreWanCurrentControllerIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterSoftGreWanCurrentControllerIPAddress.setStatus(_A)
_ArrisRouterSoftGreWanPrimaryControllerIPAddressType_Type=InetAddressType
_ArrisRouterSoftGreWanPrimaryControllerIPAddressType_Object=MibTableColumn
arrisRouterSoftGreWanPrimaryControllerIPAddressType=_ArrisRouterSoftGreWanPrimaryControllerIPAddressType_Object((1,3,6,1,4,1,4115,1,20,1,1,1,19,1,1,23),_ArrisRouterSoftGreWanPrimaryControllerIPAddressType_Type())
arrisRouterSoftGreWanPrimaryControllerIPAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterSoftGreWanPrimaryControllerIPAddressType.setStatus(_A)
_ArrisRouterSoftGreWanPrimaryControllerIPAddress_Type=InetAddress
_ArrisRouterSoftGreWanPrimaryControllerIPAddress_Object=MibTableColumn
arrisRouterSoftGreWanPrimaryControllerIPAddress=_ArrisRouterSoftGreWanPrimaryControllerIPAddress_Object((1,3,6,1,4,1,4115,1,20,1,1,1,19,1,1,24),_ArrisRouterSoftGreWanPrimaryControllerIPAddress_Type())
arrisRouterSoftGreWanPrimaryControllerIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterSoftGreWanPrimaryControllerIPAddress.setStatus(_A)
_ArrisRouterSoftGreWanSecondaryControllerIPAddressType_Type=InetAddressType
_ArrisRouterSoftGreWanSecondaryControllerIPAddressType_Object=MibTableColumn
arrisRouterSoftGreWanSecondaryControllerIPAddressType=_ArrisRouterSoftGreWanSecondaryControllerIPAddressType_Object((1,3,6,1,4,1,4115,1,20,1,1,1,19,1,1,25),_ArrisRouterSoftGreWanSecondaryControllerIPAddressType_Type())
arrisRouterSoftGreWanSecondaryControllerIPAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterSoftGreWanSecondaryControllerIPAddressType.setStatus(_A)
_ArrisRouterSoftGreWanSecondaryControllerIPAddress_Type=InetAddress
_ArrisRouterSoftGreWanSecondaryControllerIPAddress_Object=MibTableColumn
arrisRouterSoftGreWanSecondaryControllerIPAddress=_ArrisRouterSoftGreWanSecondaryControllerIPAddress_Object((1,3,6,1,4,1,4115,1,20,1,1,1,19,1,1,26),_ArrisRouterSoftGreWanSecondaryControllerIPAddress_Type())
arrisRouterSoftGreWanSecondaryControllerIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterSoftGreWanSecondaryControllerIPAddress.setStatus(_A)
class _ArrisRouterSoftGreWanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('up',0),('down',1),('error',2)))
_ArrisRouterSoftGreWanStatus_Type.__name__=_D
_ArrisRouterSoftGreWanStatus_Object=MibTableColumn
arrisRouterSoftGreWanStatus=_ArrisRouterSoftGreWanStatus_Object((1,3,6,1,4,1,4115,1,20,1,1,1,19,1,1,27),_ArrisRouterSoftGreWanStatus_Type())
arrisRouterSoftGreWanStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterSoftGreWanStatus.setStatus(_A)
class _ArrisRouterSoftGreTransportInterface_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('gwip',0),('cmip',1)))
_ArrisRouterSoftGreTransportInterface_Type.__name__=_D
_ArrisRouterSoftGreTransportInterface_Object=MibTableColumn
arrisRouterSoftGreTransportInterface=_ArrisRouterSoftGreTransportInterface_Object((1,3,6,1,4,1,4115,1,20,1,1,1,19,1,1,29),_ArrisRouterSoftGreTransportInterface_Type())
arrisRouterSoftGreTransportInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterSoftGreTransportInterface.setStatus(_A)
class _ArrisRouterSoftGreRadiusTransportInterface_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('gwip',0),('cmip',1)))
_ArrisRouterSoftGreRadiusTransportInterface_Type.__name__=_D
_ArrisRouterSoftGreRadiusTransportInterface_Object=MibTableColumn
arrisRouterSoftGreRadiusTransportInterface=_ArrisRouterSoftGreRadiusTransportInterface_Object((1,3,6,1,4,1,4115,1,20,1,1,1,19,1,1,30),_ArrisRouterSoftGreRadiusTransportInterface_Type())
arrisRouterSoftGreRadiusTransportInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterSoftGreRadiusTransportInterface.setStatus(_A)
_ArrisRouterSoftGreAcctServerAddressType_Type=InetAddressType
_ArrisRouterSoftGreAcctServerAddressType_Object=MibTableColumn
arrisRouterSoftGreAcctServerAddressType=_ArrisRouterSoftGreAcctServerAddressType_Object((1,3,6,1,4,1,4115,1,20,1,1,1,19,1,1,31),_ArrisRouterSoftGreAcctServerAddressType_Type())
arrisRouterSoftGreAcctServerAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterSoftGreAcctServerAddressType.setStatus(_A)
_ArrisRouterSoftGreAcctServerAddress_Type=InetAddress
_ArrisRouterSoftGreAcctServerAddress_Object=MibTableColumn
arrisRouterSoftGreAcctServerAddress=_ArrisRouterSoftGreAcctServerAddress_Object((1,3,6,1,4,1,4115,1,20,1,1,1,19,1,1,32),_ArrisRouterSoftGreAcctServerAddress_Type())
arrisRouterSoftGreAcctServerAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterSoftGreAcctServerAddress.setStatus(_A)
class _ArrisRouterSoftGreAcctServerPort_Type(Unsigned32):defaultValue=1813
_ArrisRouterSoftGreAcctServerPort_Type.__name__=_H
_ArrisRouterSoftGreAcctServerPort_Object=MibTableColumn
arrisRouterSoftGreAcctServerPort=_ArrisRouterSoftGreAcctServerPort_Object((1,3,6,1,4,1,4115,1,20,1,1,1,19,1,1,33),_ArrisRouterSoftGreAcctServerPort_Type())
arrisRouterSoftGreAcctServerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterSoftGreAcctServerPort.setStatus(_A)
class _ArrisRouterSoftGreAcctKey_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_ArrisRouterSoftGreAcctKey_Type.__name__=_G
_ArrisRouterSoftGreAcctKey_Object=MibTableColumn
arrisRouterSoftGreAcctKey=_ArrisRouterSoftGreAcctKey_Object((1,3,6,1,4,1,4115,1,20,1,1,1,19,1,1,34),_ArrisRouterSoftGreAcctKey_Type())
arrisRouterSoftGreAcctKey.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterSoftGreAcctKey.setStatus(_A)
_ArrisRouterSoftGreAcctInterval_Type=Unsigned32
_ArrisRouterSoftGreAcctInterval_Object=MibTableColumn
arrisRouterSoftGreAcctInterval=_ArrisRouterSoftGreAcctInterval_Object((1,3,6,1,4,1,4115,1,20,1,1,1,19,1,1,35),_ArrisRouterSoftGreAcctInterval_Type())
arrisRouterSoftGreAcctInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterSoftGreAcctInterval.setStatus(_A)
if mibBuilder.loadTexts:arrisRouterSoftGreAcctInterval.setUnits(_M)
_ArrisRouterSoftGreRadiusSecondaryServerAddressType_Type=InetAddressType
_ArrisRouterSoftGreRadiusSecondaryServerAddressType_Object=MibTableColumn
arrisRouterSoftGreRadiusSecondaryServerAddressType=_ArrisRouterSoftGreRadiusSecondaryServerAddressType_Object((1,3,6,1,4,1,4115,1,20,1,1,1,19,1,1,36),_ArrisRouterSoftGreRadiusSecondaryServerAddressType_Type())
arrisRouterSoftGreRadiusSecondaryServerAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterSoftGreRadiusSecondaryServerAddressType.setStatus(_A)
_ArrisRouterSoftGreRadiusSecondaryServerAddress_Type=InetAddress
_ArrisRouterSoftGreRadiusSecondaryServerAddress_Object=MibTableColumn
arrisRouterSoftGreRadiusSecondaryServerAddress=_ArrisRouterSoftGreRadiusSecondaryServerAddress_Object((1,3,6,1,4,1,4115,1,20,1,1,1,19,1,1,37),_ArrisRouterSoftGreRadiusSecondaryServerAddress_Type())
arrisRouterSoftGreRadiusSecondaryServerAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterSoftGreRadiusSecondaryServerAddress.setStatus(_A)
class _ArrisRouterSoftGreRadiusSecondaryServerPort_Type(Unsigned32):defaultValue=1812
_ArrisRouterSoftGreRadiusSecondaryServerPort_Type.__name__=_H
_ArrisRouterSoftGreRadiusSecondaryServerPort_Object=MibTableColumn
arrisRouterSoftGreRadiusSecondaryServerPort=_ArrisRouterSoftGreRadiusSecondaryServerPort_Object((1,3,6,1,4,1,4115,1,20,1,1,1,19,1,1,38),_ArrisRouterSoftGreRadiusSecondaryServerPort_Type())
arrisRouterSoftGreRadiusSecondaryServerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterSoftGreRadiusSecondaryServerPort.setStatus(_A)
class _ArrisRouterSoftGreRadiusSecondaryKey_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_ArrisRouterSoftGreRadiusSecondaryKey_Type.__name__=_G
_ArrisRouterSoftGreRadiusSecondaryKey_Object=MibTableColumn
arrisRouterSoftGreRadiusSecondaryKey=_ArrisRouterSoftGreRadiusSecondaryKey_Object((1,3,6,1,4,1,4115,1,20,1,1,1,19,1,1,39),_ArrisRouterSoftGreRadiusSecondaryKey_Type())
arrisRouterSoftGreRadiusSecondaryKey.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterSoftGreRadiusSecondaryKey.setStatus(_A)
_ArrisRouterSoftGreRadiusSecondaryReAuthInterval_Type=Unsigned32
_ArrisRouterSoftGreRadiusSecondaryReAuthInterval_Object=MibTableColumn
arrisRouterSoftGreRadiusSecondaryReAuthInterval=_ArrisRouterSoftGreRadiusSecondaryReAuthInterval_Object((1,3,6,1,4,1,4115,1,20,1,1,1,19,1,1,40),_ArrisRouterSoftGreRadiusSecondaryReAuthInterval_Type())
arrisRouterSoftGreRadiusSecondaryReAuthInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterSoftGreRadiusSecondaryReAuthInterval.setStatus(_A)
if mibBuilder.loadTexts:arrisRouterSoftGreRadiusSecondaryReAuthInterval.setUnits(_M)
_ArrisRouterSoftGreSSIDTable_Object=MibTable
arrisRouterSoftGreSSIDTable=_ArrisRouterSoftGreSSIDTable_Object((1,3,6,1,4,1,4115,1,20,1,1,1,19,2))
if mibBuilder.loadTexts:arrisRouterSoftGreSSIDTable.setStatus(_A)
_ArrisRouterSoftGreSSIDEntry_Object=MibTableRow
arrisRouterSoftGreSSIDEntry=_ArrisRouterSoftGreSSIDEntry_Object((1,3,6,1,4,1,4115,1,20,1,1,1,19,2,1))
arrisRouterSoftGreSSIDEntry.setIndexNames((0,_K,_L))
if mibBuilder.loadTexts:arrisRouterSoftGreSSIDEntry.setStatus(_A)
class _ArrisRouterSoftGreVLanId_Type(Unsigned32):defaultValue=0
_ArrisRouterSoftGreVLanId_Type.__name__=_H
_ArrisRouterSoftGreVLanId_Object=MibTableColumn
arrisRouterSoftGreVLanId=_ArrisRouterSoftGreVLanId_Object((1,3,6,1,4,1,4115,1,20,1,1,1,19,2,1,1),_ArrisRouterSoftGreVLanId_Type())
arrisRouterSoftGreVLanId.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterSoftGreVLanId.setStatus(_A)
class _ArrisRouterSoftGreVLanPriority_Type(Unsigned32):defaultValue=0
_ArrisRouterSoftGreVLanPriority_Type.__name__=_H
_ArrisRouterSoftGreVLanPriority_Object=MibTableColumn
arrisRouterSoftGreVLanPriority=_ArrisRouterSoftGreVLanPriority_Object((1,3,6,1,4,1,4115,1,20,1,1,1,19,2,1,2),_ArrisRouterSoftGreVLanPriority_Type())
arrisRouterSoftGreVLanPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterSoftGreVLanPriority.setStatus(_A)
class _ArrisRouterSoftGreCustomerOptOut_Type(TruthValue):defaultValue=2
_ArrisRouterSoftGreCustomerOptOut_Type.__name__=_F
_ArrisRouterSoftGreCustomerOptOut_Object=MibScalar
arrisRouterSoftGreCustomerOptOut=_ArrisRouterSoftGreCustomerOptOut_Object((1,3,6,1,4,1,4115,1,20,1,1,1,19,3),_ArrisRouterSoftGreCustomerOptOut_Type())
arrisRouterSoftGreCustomerOptOut.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterSoftGreCustomerOptOut.setStatus(_A)
class _ArrisRouterSoftGreCapable_Type(TruthValue):defaultValue=1
_ArrisRouterSoftGreCapable_Type.__name__=_F
_ArrisRouterSoftGreCapable_Object=MibScalar
arrisRouterSoftGreCapable=_ArrisRouterSoftGreCapable_Object((1,3,6,1,4,1,4115,1,20,1,1,1,19,5),_ArrisRouterSoftGreCapable_Type())
arrisRouterSoftGreCapable.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterSoftGreCapable.setStatus(_A)
_ArrisRouterDHCPRelayAgentWanObjects_ObjectIdentity=ObjectIdentity
arrisRouterDHCPRelayAgentWanObjects=_ArrisRouterDHCPRelayAgentWanObjects_ObjectIdentity((1,3,6,1,4,1,4115,1,20,1,1,1,20))
_ArrisRouterDHCPRelayAgentSSIDTable_Object=MibTable
arrisRouterDHCPRelayAgentSSIDTable=_ArrisRouterDHCPRelayAgentSSIDTable_Object((1,3,6,1,4,1,4115,1,20,1,1,1,20,1))
if mibBuilder.loadTexts:arrisRouterDHCPRelayAgentSSIDTable.setStatus(_A)
_ArrisRouterDHCPRelayAgentSSIDEntry_Object=MibTableRow
arrisRouterDHCPRelayAgentSSIDEntry=_ArrisRouterDHCPRelayAgentSSIDEntry_Object((1,3,6,1,4,1,4115,1,20,1,1,1,20,1,1))
arrisRouterDHCPRelayAgentSSIDEntry.setIndexNames((0,_K,_L))
if mibBuilder.loadTexts:arrisRouterDHCPRelayAgentSSIDEntry.setStatus(_A)
class _ArrisRouterDHCPRelayAgentEnable_Type(TruthValue):defaultValue=1
_ArrisRouterDHCPRelayAgentEnable_Type.__name__=_F
_ArrisRouterDHCPRelayAgentEnable_Object=MibTableColumn
arrisRouterDHCPRelayAgentEnable=_ArrisRouterDHCPRelayAgentEnable_Object((1,3,6,1,4,1,4115,1,20,1,1,1,20,1,1,1),_ArrisRouterDHCPRelayAgentEnable_Type())
arrisRouterDHCPRelayAgentEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterDHCPRelayAgentEnable.setStatus(_A)
class _ArrisRouterDHCPRelayAgentCircuitIdEnabled_Type(TruthValue):defaultValue=1
_ArrisRouterDHCPRelayAgentCircuitIdEnabled_Type.__name__=_F
_ArrisRouterDHCPRelayAgentCircuitIdEnabled_Object=MibTableColumn
arrisRouterDHCPRelayAgentCircuitIdEnabled=_ArrisRouterDHCPRelayAgentCircuitIdEnabled_Object((1,3,6,1,4,1,4115,1,20,1,1,1,20,1,1,2),_ArrisRouterDHCPRelayAgentCircuitIdEnabled_Type())
arrisRouterDHCPRelayAgentCircuitIdEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterDHCPRelayAgentCircuitIdEnabled.setStatus(_A)
class _ArrisRouterDHCPRelayAgentRemoteIdEnabled_Type(TruthValue):defaultValue=1
_ArrisRouterDHCPRelayAgentRemoteIdEnabled_Type.__name__=_F
_ArrisRouterDHCPRelayAgentRemoteIdEnabled_Object=MibTableColumn
arrisRouterDHCPRelayAgentRemoteIdEnabled=_ArrisRouterDHCPRelayAgentRemoteIdEnabled_Object((1,3,6,1,4,1,4115,1,20,1,1,1,20,1,1,3),_ArrisRouterDHCPRelayAgentRemoteIdEnabled_Type())
arrisRouterDHCPRelayAgentRemoteIdEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterDHCPRelayAgentRemoteIdEnabled.setStatus(_A)
class _ArrisRouterDHCPRelayAgentOption60SSIDEnabled_Type(TruthValue):defaultValue=2
_ArrisRouterDHCPRelayAgentOption60SSIDEnabled_Type.__name__=_F
_ArrisRouterDHCPRelayAgentOption60SSIDEnabled_Object=MibTableColumn
arrisRouterDHCPRelayAgentOption60SSIDEnabled=_ArrisRouterDHCPRelayAgentOption60SSIDEnabled_Object((1,3,6,1,4,1,4115,1,20,1,1,1,20,1,1,4),_ArrisRouterDHCPRelayAgentOption60SSIDEnabled_Type())
arrisRouterDHCPRelayAgentOption60SSIDEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterDHCPRelayAgentOption60SSIDEnabled.setStatus(_A)
_ArrisRouterWanTR181GatewayInfoObjects_ObjectIdentity=ObjectIdentity
arrisRouterWanTR181GatewayInfoObjects=_ArrisRouterWanTR181GatewayInfoObjects_ObjectIdentity((1,3,6,1,4,1,4115,1,20,1,1,1,21))
class _ArrisRouterTR181GatewayManufacturerOUI_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,6))
_ArrisRouterTR181GatewayManufacturerOUI_Type.__name__=_G
_ArrisRouterTR181GatewayManufacturerOUI_Object=MibScalar
arrisRouterTR181GatewayManufacturerOUI=_ArrisRouterTR181GatewayManufacturerOUI_Object((1,3,6,1,4,1,4115,1,20,1,1,1,21,1),_ArrisRouterTR181GatewayManufacturerOUI_Type())
arrisRouterTR181GatewayManufacturerOUI.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterTR181GatewayManufacturerOUI.setStatus(_A)
class _ArrisRouterTR181GatewayProductClass_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ArrisRouterTR181GatewayProductClass_Type.__name__=_G
_ArrisRouterTR181GatewayProductClass_Object=MibScalar
arrisRouterTR181GatewayProductClass=_ArrisRouterTR181GatewayProductClass_Object((1,3,6,1,4,1,4115,1,20,1,1,1,21,2),_ArrisRouterTR181GatewayProductClass_Type())
arrisRouterTR181GatewayProductClass.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterTR181GatewayProductClass.setStatus(_A)
class _ArrisRouterTR181GatewaySerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ArrisRouterTR181GatewaySerialNumber_Type.__name__=_G
_ArrisRouterTR181GatewaySerialNumber_Object=MibScalar
arrisRouterTR181GatewaySerialNumber=_ArrisRouterTR181GatewaySerialNumber_Object((1,3,6,1,4,1,4115,1,20,1,1,1,21,3),_ArrisRouterTR181GatewaySerialNumber_Type())
arrisRouterTR181GatewaySerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterTR181GatewaySerialNumber.setStatus(_A)
class _ArrisRouterWanForceIGMPVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_R,0),('igmpv1',1),('igmpv2',2),('igmpv3',3)))
_ArrisRouterWanForceIGMPVersion_Type.__name__=_D
_ArrisRouterWanForceIGMPVersion_Object=MibScalar
arrisRouterWanForceIGMPVersion=_ArrisRouterWanForceIGMPVersion_Object((1,3,6,1,4,1,4115,1,20,1,1,1,22),_ArrisRouterWanForceIGMPVersion_Type())
arrisRouterWanForceIGMPVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWanForceIGMPVersion.setStatus(_A)
_ArrisRouterLanConfig_ObjectIdentity=ObjectIdentity
arrisRouterLanConfig=_ArrisRouterLanConfig_ObjectIdentity((1,3,6,1,4,1,4115,1,20,1,1,2))
_ArrisRouterLanSrvTable_Object=MibTable
arrisRouterLanSrvTable=_ArrisRouterLanSrvTable_Object((1,3,6,1,4,1,4115,1,20,1,1,2,2))
if mibBuilder.loadTexts:arrisRouterLanSrvTable.setStatus(_A)
_ArrisRouterLanSrvEntry_Object=MibTableRow
arrisRouterLanSrvEntry=_ArrisRouterLanSrvEntry_Object((1,3,6,1,4,1,4115,1,20,1,1,2,2,1))
arrisRouterLanSrvEntry.setIndexNames((0,_K,_L))
if mibBuilder.loadTexts:arrisRouterLanSrvEntry.setStatus(_A)
class _ArrisRouterLanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ArrisRouterLanName_Type.__name__=_G
_ArrisRouterLanName_Object=MibTableColumn
arrisRouterLanName=_ArrisRouterLanName_Object((1,3,6,1,4,1,4115,1,20,1,1,2,2,1,1),_ArrisRouterLanName_Type())
arrisRouterLanName.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterLanName.setStatus(_A)
class _ArrisRouterLanSubnetMaskType_Type(InetAddressType):defaultValue=1
_ArrisRouterLanSubnetMaskType_Type.__name__=_S
_ArrisRouterLanSubnetMaskType_Object=MibTableColumn
arrisRouterLanSubnetMaskType=_ArrisRouterLanSubnetMaskType_Object((1,3,6,1,4,1,4115,1,20,1,1,2,2,1,2),_ArrisRouterLanSubnetMaskType_Type())
arrisRouterLanSubnetMaskType.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterLanSubnetMaskType.setStatus(_A)
_ArrisRouterLanSubnetMask_Type=InetAddress
_ArrisRouterLanSubnetMask_Object=MibTableColumn
arrisRouterLanSubnetMask=_ArrisRouterLanSubnetMask_Object((1,3,6,1,4,1,4115,1,20,1,1,2,2,1,3),_ArrisRouterLanSubnetMask_Type())
arrisRouterLanSubnetMask.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterLanSubnetMask.setStatus(_A)
class _ArrisRouterLanGatewayIpType_Type(InetAddressType):defaultValue=1
_ArrisRouterLanGatewayIpType_Type.__name__=_S
_ArrisRouterLanGatewayIpType_Object=MibTableColumn
arrisRouterLanGatewayIpType=_ArrisRouterLanGatewayIpType_Object((1,3,6,1,4,1,4115,1,20,1,1,2,2,1,4),_ArrisRouterLanGatewayIpType_Type())
arrisRouterLanGatewayIpType.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterLanGatewayIpType.setStatus(_A)
_ArrisRouterLanGatewayIp_Type=InetAddress
_ArrisRouterLanGatewayIp_Object=MibTableColumn
arrisRouterLanGatewayIp=_ArrisRouterLanGatewayIp_Object((1,3,6,1,4,1,4115,1,20,1,1,2,2,1,5),_ArrisRouterLanGatewayIp_Type())
arrisRouterLanGatewayIp.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterLanGatewayIp.setStatus(_A)
class _ArrisRouterLanGatewayIp2Type_Type(InetAddressType):defaultValue=1
_ArrisRouterLanGatewayIp2Type_Type.__name__=_S
_ArrisRouterLanGatewayIp2Type_Object=MibTableColumn
arrisRouterLanGatewayIp2Type=_ArrisRouterLanGatewayIp2Type_Object((1,3,6,1,4,1,4115,1,20,1,1,2,2,1,6),_ArrisRouterLanGatewayIp2Type_Type())
arrisRouterLanGatewayIp2Type.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterLanGatewayIp2Type.setStatus(_A)
_ArrisRouterLanGatewayIp2_Type=InetAddress
_ArrisRouterLanGatewayIp2_Object=MibTableColumn
arrisRouterLanGatewayIp2=_ArrisRouterLanGatewayIp2_Object((1,3,6,1,4,1,4115,1,20,1,1,2,2,1,7),_ArrisRouterLanGatewayIp2_Type())
arrisRouterLanGatewayIp2.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterLanGatewayIp2.setStatus(_A)
class _ArrisRouterLanVLanID_Type(Unsigned32):defaultValue=0
_ArrisRouterLanVLanID_Type.__name__=_H
_ArrisRouterLanVLanID_Object=MibTableColumn
arrisRouterLanVLanID=_ArrisRouterLanVLanID_Object((1,3,6,1,4,1,4115,1,20,1,1,2,2,1,8),_ArrisRouterLanVLanID_Type())
arrisRouterLanVLanID.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterLanVLanID.setStatus(_A)
class _ArrisRouterLanUseDHCP_Type(TruthValue):defaultValue=1
_ArrisRouterLanUseDHCP_Type.__name__=_F
_ArrisRouterLanUseDHCP_Object=MibTableColumn
arrisRouterLanUseDHCP=_ArrisRouterLanUseDHCP_Object((1,3,6,1,4,1,4115,1,20,1,1,2,2,1,9),_ArrisRouterLanUseDHCP_Type())
arrisRouterLanUseDHCP.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterLanUseDHCP.setStatus(_A)
_ArrisRouterLanStartDHCPType_Type=InetAddressType
_ArrisRouterLanStartDHCPType_Object=MibTableColumn
arrisRouterLanStartDHCPType=_ArrisRouterLanStartDHCPType_Object((1,3,6,1,4,1,4115,1,20,1,1,2,2,1,10),_ArrisRouterLanStartDHCPType_Type())
arrisRouterLanStartDHCPType.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterLanStartDHCPType.setStatus(_A)
_ArrisRouterLanStartDHCP_Type=InetAddress
_ArrisRouterLanStartDHCP_Object=MibTableColumn
arrisRouterLanStartDHCP=_ArrisRouterLanStartDHCP_Object((1,3,6,1,4,1,4115,1,20,1,1,2,2,1,11),_ArrisRouterLanStartDHCP_Type())
arrisRouterLanStartDHCP.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterLanStartDHCP.setStatus(_A)
_ArrisRouterLanEndDHCPType_Type=InetAddressType
_ArrisRouterLanEndDHCPType_Object=MibTableColumn
arrisRouterLanEndDHCPType=_ArrisRouterLanEndDHCPType_Object((1,3,6,1,4,1,4115,1,20,1,1,2,2,1,12),_ArrisRouterLanEndDHCPType_Type())
arrisRouterLanEndDHCPType.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterLanEndDHCPType.setStatus(_A)
_ArrisRouterLanEndDHCP_Type=InetAddress
_ArrisRouterLanEndDHCP_Object=MibTableColumn
arrisRouterLanEndDHCP=_ArrisRouterLanEndDHCP_Object((1,3,6,1,4,1,4115,1,20,1,1,2,2,1,13),_ArrisRouterLanEndDHCP_Type())
arrisRouterLanEndDHCP.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterLanEndDHCP.setStatus(_A)
_ArrisRouterLanLeaseTime_Type=Unsigned32
_ArrisRouterLanLeaseTime_Object=MibTableColumn
arrisRouterLanLeaseTime=_ArrisRouterLanLeaseTime_Object((1,3,6,1,4,1,4115,1,20,1,1,2,2,1,14),_ArrisRouterLanLeaseTime_Type())
arrisRouterLanLeaseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterLanLeaseTime.setStatus(_A)
if mibBuilder.loadTexts:arrisRouterLanLeaseTime.setUnits(_M)
class _ArrisRouterLanDomainName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ArrisRouterLanDomainName_Type.__name__=_G
_ArrisRouterLanDomainName_Object=MibTableColumn
arrisRouterLanDomainName=_ArrisRouterLanDomainName_Object((1,3,6,1,4,1,4115,1,20,1,1,2,2,1,15),_ArrisRouterLanDomainName_Type())
arrisRouterLanDomainName.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterLanDomainName.setStatus(_A)
class _ArrisRouterLanRelayDNS_Type(TruthValue):defaultValue=2
_ArrisRouterLanRelayDNS_Type.__name__=_F
_ArrisRouterLanRelayDNS_Object=MibTableColumn
arrisRouterLanRelayDNS=_ArrisRouterLanRelayDNS_Object((1,3,6,1,4,1,4115,1,20,1,1,2,2,1,19),_ArrisRouterLanRelayDNS_Type())
arrisRouterLanRelayDNS.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterLanRelayDNS.setStatus(_A)
class _ArrisRouterLanPassThru_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,1,2,3)));namedValues=NamedValues(*((_N,-1),('passThru',1),('routedNAT',2),('routedNoNAT',3)))
_ArrisRouterLanPassThru_Type.__name__=_D
_ArrisRouterLanPassThru_Object=MibTableColumn
arrisRouterLanPassThru=_ArrisRouterLanPassThru_Object((1,3,6,1,4,1,4115,1,20,1,1,2,2,1,21),_ArrisRouterLanPassThru_Type())
arrisRouterLanPassThru.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterLanPassThru.setStatus(_A)
_ArrisRouterLanFirewallOn_Type=TruthValue
_ArrisRouterLanFirewallOn_Object=MibTableColumn
arrisRouterLanFirewallOn=_ArrisRouterLanFirewallOn_Object((1,3,6,1,4,1,4115,1,20,1,1,2,2,1,22),_ArrisRouterLanFirewallOn_Type())
arrisRouterLanFirewallOn.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterLanFirewallOn.setStatus(_A)
_ArrisRouterLanUPnPEnable_Type=TruthValue
_ArrisRouterLanUPnPEnable_Object=MibTableColumn
arrisRouterLanUPnPEnable=_ArrisRouterLanUPnPEnable_Object((1,3,6,1,4,1,4115,1,20,1,1,2,2,1,23),_ArrisRouterLanUPnPEnable_Type())
arrisRouterLanUPnPEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterLanUPnPEnable.setStatus(_A)
_ArrisRouterLanCPEAging_Type=Integer32
_ArrisRouterLanCPEAging_Object=MibTableColumn
arrisRouterLanCPEAging=_ArrisRouterLanCPEAging_Object((1,3,6,1,4,1,4115,1,20,1,1,2,2,1,24),_ArrisRouterLanCPEAging_Type())
arrisRouterLanCPEAging.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterLanCPEAging.setStatus(_A)
class _ArrisRouterLanOverrideDNS_Type(TruthValue):defaultValue=2
_ArrisRouterLanOverrideDNS_Type.__name__=_F
_ArrisRouterLanOverrideDNS_Object=MibTableColumn
arrisRouterLanOverrideDNS=_ArrisRouterLanOverrideDNS_Object((1,3,6,1,4,1,4115,1,20,1,1,2,2,1,25),_ArrisRouterLanOverrideDNS_Type())
arrisRouterLanOverrideDNS.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterLanOverrideDNS.setStatus(_A)
class _ArrisRouterLanNatAlgsEnabled_Type(Bits):namedValues=NamedValues(*(('rsvp',0),('ftp',1),('tftp',2),('kerb88',3),('netBiosDgm',4),('ike',5),('rtsp',6),('kerb1293',7),('h225',8),('pptp',9),('msn',10),('sip',11),('icq',12),('irc6667',13),('icqTalk',14),('net2Phone',15),('irc7000',16),('irc8000',17)))
_ArrisRouterLanNatAlgsEnabled_Type.__name__='Bits'
_ArrisRouterLanNatAlgsEnabled_Object=MibTableColumn
arrisRouterLanNatAlgsEnabled=_ArrisRouterLanNatAlgsEnabled_Object((1,3,6,1,4,1,4115,1,20,1,1,2,2,1,26),_ArrisRouterLanNatAlgsEnabled_Type())
arrisRouterLanNatAlgsEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterLanNatAlgsEnabled.setStatus(_A)
_ArrisRouterLanMappedInterface_Type=Unsigned32
_ArrisRouterLanMappedInterface_Object=MibTableColumn
arrisRouterLanMappedInterface=_ArrisRouterLanMappedInterface_Object((1,3,6,1,4,1,4115,1,20,1,1,2,2,1,27),_ArrisRouterLanMappedInterface_Type())
arrisRouterLanMappedInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterLanMappedInterface.setStatus(_A)
class _ArrisRouterLanEnvironmentControl_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('unlocked',0),('locked',1)))
_ArrisRouterLanEnvironmentControl_Type.__name__=_D
_ArrisRouterLanEnvironmentControl_Object=MibTableColumn
arrisRouterLanEnvironmentControl=_ArrisRouterLanEnvironmentControl_Object((1,3,6,1,4,1,4115,1,20,1,1,2,2,1,28),_ArrisRouterLanEnvironmentControl_Type())
arrisRouterLanEnvironmentControl.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterLanEnvironmentControl.setStatus(_A)
_ArrisRouterLanPrefixLengthV6_Type=InetAddressPrefixLength
_ArrisRouterLanPrefixLengthV6_Object=MibTableColumn
arrisRouterLanPrefixLengthV6=_ArrisRouterLanPrefixLengthV6_Object((1,3,6,1,4,1,4115,1,20,1,1,2,2,1,29),_ArrisRouterLanPrefixLengthV6_Type())
arrisRouterLanPrefixLengthV6.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterLanPrefixLengthV6.setStatus(_A)
class _ArrisRouterLanUseDHCPV6_Type(TruthValue):defaultValue=1
_ArrisRouterLanUseDHCPV6_Type.__name__=_F
_ArrisRouterLanUseDHCPV6_Object=MibTableColumn
arrisRouterLanUseDHCPV6=_ArrisRouterLanUseDHCPV6_Object((1,3,6,1,4,1,4115,1,20,1,1,2,2,1,30),_ArrisRouterLanUseDHCPV6_Type())
arrisRouterLanUseDHCPV6.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterLanUseDHCPV6.setStatus(_A)
_ArrisRouterLanStartDHCPV6_Type=InetAddressIPv6
_ArrisRouterLanStartDHCPV6_Object=MibTableColumn
arrisRouterLanStartDHCPV6=_ArrisRouterLanStartDHCPV6_Object((1,3,6,1,4,1,4115,1,20,1,1,2,2,1,31),_ArrisRouterLanStartDHCPV6_Type())
arrisRouterLanStartDHCPV6.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterLanStartDHCPV6.setStatus(_A)
_ArrisRouterLanEndDHCPV6_Type=InetAddressIPv6
_ArrisRouterLanEndDHCPV6_Object=MibTableColumn
arrisRouterLanEndDHCPV6=_ArrisRouterLanEndDHCPV6_Object((1,3,6,1,4,1,4115,1,20,1,1,2,2,1,32),_ArrisRouterLanEndDHCPV6_Type())
arrisRouterLanEndDHCPV6.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterLanEndDHCPV6.setStatus(_A)
_ArrisRouterLanLeaseTimeV6_Type=Unsigned32
_ArrisRouterLanLeaseTimeV6_Object=MibTableColumn
arrisRouterLanLeaseTimeV6=_ArrisRouterLanLeaseTimeV6_Object((1,3,6,1,4,1,4115,1,20,1,1,2,2,1,33),_ArrisRouterLanLeaseTimeV6_Type())
arrisRouterLanLeaseTimeV6.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterLanLeaseTimeV6.setStatus(_A)
if mibBuilder.loadTexts:arrisRouterLanLeaseTimeV6.setUnits(_M)
_ArrisRouterLanLinkLocalAddressV6_Type=InetAddressIPv6
_ArrisRouterLanLinkLocalAddressV6_Object=MibTableColumn
arrisRouterLanLinkLocalAddressV6=_ArrisRouterLanLinkLocalAddressV6_Object((1,3,6,1,4,1,4115,1,20,1,1,2,2,1,34),_ArrisRouterLanLinkLocalAddressV6_Type())
arrisRouterLanLinkLocalAddressV6.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterLanLinkLocalAddressV6.setStatus(_A)
class _ArrisRouterLanDNSRelayV6_Type(TruthValue):defaultValue=2
_ArrisRouterLanDNSRelayV6_Type.__name__=_F
_ArrisRouterLanDNSRelayV6_Object=MibTableColumn
arrisRouterLanDNSRelayV6=_ArrisRouterLanDNSRelayV6_Object((1,3,6,1,4,1,4115,1,20,1,1,2,2,1,35),_ArrisRouterLanDNSRelayV6_Type())
arrisRouterLanDNSRelayV6.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterLanDNSRelayV6.setStatus(_A)
class _ArrisRouterLanDNSOverrideV6_Type(TruthValue):defaultValue=2
_ArrisRouterLanDNSOverrideV6_Type.__name__=_F
_ArrisRouterLanDNSOverrideV6_Object=MibTableColumn
arrisRouterLanDNSOverrideV6=_ArrisRouterLanDNSOverrideV6_Object((1,3,6,1,4,1,4115,1,20,1,1,2,2,1,36),_ArrisRouterLanDNSOverrideV6_Type())
arrisRouterLanDNSOverrideV6.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterLanDNSOverrideV6.setStatus(_A)
_ArrisRouterLanPreProvLeaseTime_Type=Unsigned32
_ArrisRouterLanPreProvLeaseTime_Object=MibTableColumn
arrisRouterLanPreProvLeaseTime=_ArrisRouterLanPreProvLeaseTime_Object((1,3,6,1,4,1,4115,1,20,1,1,2,2,1,37),_ArrisRouterLanPreProvLeaseTime_Type())
arrisRouterLanPreProvLeaseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterLanPreProvLeaseTime.setStatus(_A)
if mibBuilder.loadTexts:arrisRouterLanPreProvLeaseTime.setUnits(_M)
class _ArrisRouterLanParentalControlsEnable_Type(TruthValue):defaultValue=2
_ArrisRouterLanParentalControlsEnable_Type.__name__=_F
_ArrisRouterLanParentalControlsEnable_Object=MibTableColumn
arrisRouterLanParentalControlsEnable=_ArrisRouterLanParentalControlsEnable_Object((1,3,6,1,4,1,4115,1,20,1,1,2,2,1,39),_ArrisRouterLanParentalControlsEnable_Type())
arrisRouterLanParentalControlsEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterLanParentalControlsEnable.setStatus(_A)
_ArrisRouterLanDNSTable_Object=MibTable
arrisRouterLanDNSTable=_ArrisRouterLanDNSTable_Object((1,3,6,1,4,1,4115,1,20,1,1,2,3))
if mibBuilder.loadTexts:arrisRouterLanDNSTable.setStatus(_A)
_ArrisRouterLanDNSEntry_Object=MibTableRow
arrisRouterLanDNSEntry=_ArrisRouterLanDNSEntry_Object((1,3,6,1,4,1,4115,1,20,1,1,2,3,1))
arrisRouterLanDNSEntry.setIndexNames((0,_K,_L),(0,_I,_z))
if mibBuilder.loadTexts:arrisRouterLanDNSEntry.setStatus(_A)
class _ArrisRouterLanDNSIdx_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_ArrisRouterLanDNSIdx_Type.__name__=_H
_ArrisRouterLanDNSIdx_Object=MibTableColumn
arrisRouterLanDNSIdx=_ArrisRouterLanDNSIdx_Object((1,3,6,1,4,1,4115,1,20,1,1,2,3,1,1),_ArrisRouterLanDNSIdx_Type())
arrisRouterLanDNSIdx.setMaxAccess(_J)
if mibBuilder.loadTexts:arrisRouterLanDNSIdx.setStatus(_A)
_ArrisRouterLanDNSIPAddrType_Type=InetAddressType
_ArrisRouterLanDNSIPAddrType_Object=MibTableColumn
arrisRouterLanDNSIPAddrType=_ArrisRouterLanDNSIPAddrType_Object((1,3,6,1,4,1,4115,1,20,1,1,2,3,1,2),_ArrisRouterLanDNSIPAddrType_Type())
arrisRouterLanDNSIPAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterLanDNSIPAddrType.setStatus(_A)
_ArrisRouterLanDNSIPAddr_Type=InetAddress
_ArrisRouterLanDNSIPAddr_Object=MibTableColumn
arrisRouterLanDNSIPAddr=_ArrisRouterLanDNSIPAddr_Object((1,3,6,1,4,1,4115,1,20,1,1,2,3,1,3),_ArrisRouterLanDNSIPAddr_Type())
arrisRouterLanDNSIPAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterLanDNSIPAddr.setStatus(_A)
_ArrisRouterLanDNSRowStatus_Type=RowStatus
_ArrisRouterLanDNSRowStatus_Object=MibTableColumn
arrisRouterLanDNSRowStatus=_ArrisRouterLanDNSRowStatus_Object((1,3,6,1,4,1,4115,1,20,1,1,2,3,1,4),_ArrisRouterLanDNSRowStatus_Type())
arrisRouterLanDNSRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterLanDNSRowStatus.setStatus(_A)
_ArrisRouterClientObjects_ObjectIdentity=ObjectIdentity
arrisRouterClientObjects=_ArrisRouterClientObjects_ObjectIdentity((1,3,6,1,4,1,4115,1,20,1,1,2,4))
_ArrisRouterLanClientCount_Type=Unsigned32
_ArrisRouterLanClientCount_Object=MibScalar
arrisRouterLanClientCount=_ArrisRouterLanClientCount_Object((1,3,6,1,4,1,4115,1,20,1,1,2,4,1),_ArrisRouterLanClientCount_Type())
arrisRouterLanClientCount.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterLanClientCount.setStatus(_A)
_ArrisRouterLanClientTable_Object=MibTable
arrisRouterLanClientTable=_ArrisRouterLanClientTable_Object((1,3,6,1,4,1,4115,1,20,1,1,2,4,2))
if mibBuilder.loadTexts:arrisRouterLanClientTable.setStatus(_A)
_ArrisRouterLanClientEntry_Object=MibTableRow
arrisRouterLanClientEntry=_ArrisRouterLanClientEntry_Object((1,3,6,1,4,1,4115,1,20,1,1,2,4,2,1))
arrisRouterLanClientEntry.setIndexNames((0,_K,_L),(0,_I,_i),(0,_I,_j))
if mibBuilder.loadTexts:arrisRouterLanClientEntry.setStatus(_A)
_ArrisRouterLanClientIPAddrType_Type=InetAddressType
_ArrisRouterLanClientIPAddrType_Object=MibTableColumn
arrisRouterLanClientIPAddrType=_ArrisRouterLanClientIPAddrType_Object((1,3,6,1,4,1,4115,1,20,1,1,2,4,2,1,1),_ArrisRouterLanClientIPAddrType_Type())
arrisRouterLanClientIPAddrType.setMaxAccess(_J)
if mibBuilder.loadTexts:arrisRouterLanClientIPAddrType.setStatus(_A)
_ArrisRouterLanClientIPAddr_Type=InetAddress
_ArrisRouterLanClientIPAddr_Object=MibTableColumn
arrisRouterLanClientIPAddr=_ArrisRouterLanClientIPAddr_Object((1,3,6,1,4,1,4115,1,20,1,1,2,4,2,1,2),_ArrisRouterLanClientIPAddr_Type())
arrisRouterLanClientIPAddr.setMaxAccess(_J)
if mibBuilder.loadTexts:arrisRouterLanClientIPAddr.setStatus(_A)
class _ArrisRouterLanClientHostName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ArrisRouterLanClientHostName_Type.__name__=_G
_ArrisRouterLanClientHostName_Object=MibTableColumn
arrisRouterLanClientHostName=_ArrisRouterLanClientHostName_Object((1,3,6,1,4,1,4115,1,20,1,1,2,4,2,1,3),_ArrisRouterLanClientHostName_Type())
arrisRouterLanClientHostName.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterLanClientHostName.setStatus(_A)
_ArrisRouterLanClientMAC_Type=MacAddress
_ArrisRouterLanClientMAC_Object=MibTableColumn
arrisRouterLanClientMAC=_ArrisRouterLanClientMAC_Object((1,3,6,1,4,1,4115,1,20,1,1,2,4,2,1,4),_ArrisRouterLanClientMAC_Type())
arrisRouterLanClientMAC.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterLanClientMAC.setStatus(_A)
class _ArrisRouterLanClientAdapterType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23)));namedValues=NamedValues(*((_N,0),('ethernet',1),('usb',2),('moca',3),('dsg',4),('wireless1',5),('wireless2',6),('wireless3',7),('wireless4',8),('wireless5',9),('wireless6',10),('wireless7',11),('wireless8',12),('wireless9',13),('wireless10',14),('wireless11',15),('wireless12',16),('wireless13',17),('wireless14',18),('wireless15',19),('wireless16',20),('ethernet2',21),('ethernet3',22),('ethernet4',23)))
_ArrisRouterLanClientAdapterType_Type.__name__=_D
_ArrisRouterLanClientAdapterType_Object=MibTableColumn
arrisRouterLanClientAdapterType=_ArrisRouterLanClientAdapterType_Object((1,3,6,1,4,1,4115,1,20,1,1,2,4,2,1,6),_ArrisRouterLanClientAdapterType_Type())
arrisRouterLanClientAdapterType.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterLanClientAdapterType.setStatus(_A)
class _ArrisRouterLanClientType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,5,6)));namedValues=NamedValues(*((_N,0),(_V,1),(_W,5),('dynamicReserved',6)))
_ArrisRouterLanClientType_Type.__name__=_D
_ArrisRouterLanClientType_Object=MibTableColumn
arrisRouterLanClientType=_ArrisRouterLanClientType_Object((1,3,6,1,4,1,4115,1,20,1,1,2,4,2,1,7),_ArrisRouterLanClientType_Type())
arrisRouterLanClientType.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterLanClientType.setStatus(_A)
_ArrisRouterLanClientLeaseEnd_Type=DateAndTime
_ArrisRouterLanClientLeaseEnd_Object=MibTableColumn
arrisRouterLanClientLeaseEnd=_ArrisRouterLanClientLeaseEnd_Object((1,3,6,1,4,1,4115,1,20,1,1,2,4,2,1,9),_ArrisRouterLanClientLeaseEnd_Type())
arrisRouterLanClientLeaseEnd.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterLanClientLeaseEnd.setStatus(_A)
_ArrisRouterLanClientRowStatus_Type=RowStatus
_ArrisRouterLanClientRowStatus_Object=MibTableColumn
arrisRouterLanClientRowStatus=_ArrisRouterLanClientRowStatus_Object((1,3,6,1,4,1,4115,1,20,1,1,2,4,2,1,13),_ArrisRouterLanClientRowStatus_Type())
arrisRouterLanClientRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterLanClientRowStatus.setStatus(_A)
class _ArrisRouterLanClientOnline_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('offline',0),('online',1)))
_ArrisRouterLanClientOnline_Type.__name__=_D
_ArrisRouterLanClientOnline_Object=MibTableColumn
arrisRouterLanClientOnline=_ArrisRouterLanClientOnline_Object((1,3,6,1,4,1,4115,1,20,1,1,2,4,2,1,14),_ArrisRouterLanClientOnline_Type())
arrisRouterLanClientOnline.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterLanClientOnline.setStatus(_A)
_ArrisRouterLanClientComment_Type=DisplayString
_ArrisRouterLanClientComment_Object=MibTableColumn
arrisRouterLanClientComment=_ArrisRouterLanClientComment_Object((1,3,6,1,4,1,4115,1,20,1,1,2,4,2,1,15),_ArrisRouterLanClientComment_Type())
arrisRouterLanClientComment.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterLanClientComment.setStatus('deprecated')
class _ArrisRouterLanClientManufacturerOUI_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,6))
_ArrisRouterLanClientManufacturerOUI_Type.__name__=_G
_ArrisRouterLanClientManufacturerOUI_Object=MibTableColumn
arrisRouterLanClientManufacturerOUI=_ArrisRouterLanClientManufacturerOUI_Object((1,3,6,1,4,1,4115,1,20,1,1,2,4,2,1,17),_ArrisRouterLanClientManufacturerOUI_Type())
arrisRouterLanClientManufacturerOUI.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterLanClientManufacturerOUI.setStatus(_A)
class _ArrisRouterLanClientSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ArrisRouterLanClientSerialNumber_Type.__name__=_G
_ArrisRouterLanClientSerialNumber_Object=MibTableColumn
arrisRouterLanClientSerialNumber=_ArrisRouterLanClientSerialNumber_Object((1,3,6,1,4,1,4115,1,20,1,1,2,4,2,1,18),_ArrisRouterLanClientSerialNumber_Type())
arrisRouterLanClientSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterLanClientSerialNumber.setStatus(_A)
class _ArrisRouterLanClientProductClass_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ArrisRouterLanClientProductClass_Type.__name__=_G
_ArrisRouterLanClientProductClass_Object=MibTableColumn
arrisRouterLanClientProductClass=_ArrisRouterLanClientProductClass_Object((1,3,6,1,4,1,4115,1,20,1,1,2,4,2,1,19),_ArrisRouterLanClientProductClass_Type())
arrisRouterLanClientProductClass.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterLanClientProductClass.setStatus(_A)
class _ArrisRouterLanClientDeviceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ArrisRouterLanClientDeviceName_Type.__name__=_G
_ArrisRouterLanClientDeviceName_Object=MibTableColumn
arrisRouterLanClientDeviceName=_ArrisRouterLanClientDeviceName_Object((1,3,6,1,4,1,4115,1,20,1,1,2,4,2,1,20),_ArrisRouterLanClientDeviceName_Type())
arrisRouterLanClientDeviceName.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterLanClientDeviceName.setStatus(_A)
_ArrisRouterLanClientLastChange_Type=Integer32
_ArrisRouterLanClientLastChange_Object=MibTableColumn
arrisRouterLanClientLastChange=_ArrisRouterLanClientLastChange_Object((1,3,6,1,4,1,4115,1,20,1,1,2,4,2,1,24),_ArrisRouterLanClientLastChange_Type())
arrisRouterLanClientLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterLanClientLastChange.setStatus(_A)
if mibBuilder.loadTexts:arrisRouterLanClientLastChange.setUnits(_M)
_ArrisRouterLanClientTimeConnected_Type=Integer32
_ArrisRouterLanClientTimeConnected_Object=MibTableColumn
arrisRouterLanClientTimeConnected=_ArrisRouterLanClientTimeConnected_Object((1,3,6,1,4,1,4115,1,20,1,1,2,4,2,1,25),_ArrisRouterLanClientTimeConnected_Type())
arrisRouterLanClientTimeConnected.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterLanClientTimeConnected.setStatus(_A)
if mibBuilder.loadTexts:arrisRouterLanClientTimeConnected.setUnits(_M)
_ArrisRouterDeviceUpDownTable_Object=MibTable
arrisRouterDeviceUpDownTable=_ArrisRouterDeviceUpDownTable_Object((1,3,6,1,4,1,4115,1,20,1,1,2,4,3))
if mibBuilder.loadTexts:arrisRouterDeviceUpDownTable.setStatus(_A)
_ArrisRouterDeviceUpDownEntry_Object=MibTableRow
arrisRouterDeviceUpDownEntry=_ArrisRouterDeviceUpDownEntry_Object((1,3,6,1,4,1,4115,1,20,1,1,2,4,3,1))
arrisRouterDeviceUpDownEntry.setIndexNames((0,_K,_L),(0,_I,_A0))
if mibBuilder.loadTexts:arrisRouterDeviceUpDownEntry.setStatus(_A)
class _ArrisRouterDeviceUpDownIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_ArrisRouterDeviceUpDownIndex_Type.__name__=_D
_ArrisRouterDeviceUpDownIndex_Object=MibTableColumn
arrisRouterDeviceUpDownIndex=_ArrisRouterDeviceUpDownIndex_Object((1,3,6,1,4,1,4115,1,20,1,1,2,4,3,1,1),_ArrisRouterDeviceUpDownIndex_Type())
arrisRouterDeviceUpDownIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:arrisRouterDeviceUpDownIndex.setStatus(_A)
_ArrisRouterDeviceUpDownMAC_Type=MacAddress
_ArrisRouterDeviceUpDownMAC_Object=MibTableColumn
arrisRouterDeviceUpDownMAC=_ArrisRouterDeviceUpDownMAC_Object((1,3,6,1,4,1,4115,1,20,1,1,2,4,3,1,2),_ArrisRouterDeviceUpDownMAC_Type())
arrisRouterDeviceUpDownMAC.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterDeviceUpDownMAC.setStatus(_A)
_ArrisRouterDeviceUpDownIPType_Type=InetAddressType
_ArrisRouterDeviceUpDownIPType_Object=MibTableColumn
arrisRouterDeviceUpDownIPType=_ArrisRouterDeviceUpDownIPType_Object((1,3,6,1,4,1,4115,1,20,1,1,2,4,3,1,3),_ArrisRouterDeviceUpDownIPType_Type())
arrisRouterDeviceUpDownIPType.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterDeviceUpDownIPType.setStatus(_A)
_ArrisRouterDeviceUpDownStatus_Type=RowStatus
_ArrisRouterDeviceUpDownStatus_Object=MibTableColumn
arrisRouterDeviceUpDownStatus=_ArrisRouterDeviceUpDownStatus_Object((1,3,6,1,4,1,4115,1,20,1,1,2,4,3,1,7),_ArrisRouterDeviceUpDownStatus_Type())
arrisRouterDeviceUpDownStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterDeviceUpDownStatus.setStatus(_A)
_ArrisRouterLanCustomCount_Type=Unsigned32
_ArrisRouterLanCustomCount_Object=MibScalar
arrisRouterLanCustomCount=_ArrisRouterLanCustomCount_Object((1,3,6,1,4,1,4115,1,20,1,1,2,4,4),_ArrisRouterLanCustomCount_Type())
arrisRouterLanCustomCount.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterLanCustomCount.setStatus(_A)
_ArrisRouterLanCustomTable_Object=MibTable
arrisRouterLanCustomTable=_ArrisRouterLanCustomTable_Object((1,3,6,1,4,1,4115,1,20,1,1,2,4,5))
if mibBuilder.loadTexts:arrisRouterLanCustomTable.setStatus(_A)
_ArrisRouterLanCustomEntry_Object=MibTableRow
arrisRouterLanCustomEntry=_ArrisRouterLanCustomEntry_Object((1,3,6,1,4,1,4115,1,20,1,1,2,4,5,1))
arrisRouterLanCustomEntry.setIndexNames((0,_I,_A1))
if mibBuilder.loadTexts:arrisRouterLanCustomEntry.setStatus(_A)
_ArrisRouterLanCustomIdx_Type=Unsigned32
_ArrisRouterLanCustomIdx_Object=MibTableColumn
arrisRouterLanCustomIdx=_ArrisRouterLanCustomIdx_Object((1,3,6,1,4,1,4115,1,20,1,1,2,4,5,1,1),_ArrisRouterLanCustomIdx_Type())
arrisRouterLanCustomIdx.setMaxAccess(_J)
if mibBuilder.loadTexts:arrisRouterLanCustomIdx.setStatus(_A)
_ArrisRouterLanCustomMAC_Type=MacAddress
_ArrisRouterLanCustomMAC_Object=MibTableColumn
arrisRouterLanCustomMAC=_ArrisRouterLanCustomMAC_Object((1,3,6,1,4,1,4115,1,20,1,1,2,4,5,1,2),_ArrisRouterLanCustomMAC_Type())
arrisRouterLanCustomMAC.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterLanCustomMAC.setStatus(_A)
_ArrisRouterLanCustomIPAddrType_Type=InetAddressType
_ArrisRouterLanCustomIPAddrType_Object=MibTableColumn
arrisRouterLanCustomIPAddrType=_ArrisRouterLanCustomIPAddrType_Object((1,3,6,1,4,1,4115,1,20,1,1,2,4,5,1,3),_ArrisRouterLanCustomIPAddrType_Type())
arrisRouterLanCustomIPAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterLanCustomIPAddrType.setStatus(_A)
_ArrisRouterLanCustomIPAddr_Type=InetAddress
_ArrisRouterLanCustomIPAddr_Object=MibTableColumn
arrisRouterLanCustomIPAddr=_ArrisRouterLanCustomIPAddr_Object((1,3,6,1,4,1,4115,1,20,1,1,2,4,5,1,4),_ArrisRouterLanCustomIPAddr_Type())
arrisRouterLanCustomIPAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterLanCustomIPAddr.setStatus(_A)
class _ArrisRouterLanCustomFriendName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ArrisRouterLanCustomFriendName_Type.__name__=_G
_ArrisRouterLanCustomFriendName_Object=MibTableColumn
arrisRouterLanCustomFriendName=_ArrisRouterLanCustomFriendName_Object((1,3,6,1,4,1,4115,1,20,1,1,2,4,5,1,5),_ArrisRouterLanCustomFriendName_Type())
arrisRouterLanCustomFriendName.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterLanCustomFriendName.setStatus(_A)
class _ArrisRouterLanCustomHostName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ArrisRouterLanCustomHostName_Type.__name__=_G
_ArrisRouterLanCustomHostName_Object=MibTableColumn
arrisRouterLanCustomHostName=_ArrisRouterLanCustomHostName_Object((1,3,6,1,4,1,4115,1,20,1,1,2,4,5,1,6),_ArrisRouterLanCustomHostName_Type())
arrisRouterLanCustomHostName.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterLanCustomHostName.setStatus(_A)
class _ArrisRouterLanCustomMACMfg_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ArrisRouterLanCustomMACMfg_Type.__name__=_G
_ArrisRouterLanCustomMACMfg_Object=MibTableColumn
arrisRouterLanCustomMACMfg=_ArrisRouterLanCustomMACMfg_Object((1,3,6,1,4,1,4115,1,20,1,1,2,4,5,1,7),_ArrisRouterLanCustomMACMfg_Type())
arrisRouterLanCustomMACMfg.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterLanCustomMACMfg.setStatus(_A)
_ArrisRouterLanCustomComments_Type=DisplayString
_ArrisRouterLanCustomComments_Object=MibTableColumn
arrisRouterLanCustomComments=_ArrisRouterLanCustomComments_Object((1,3,6,1,4,1,4115,1,20,1,1,2,4,5,1,8),_ArrisRouterLanCustomComments_Type())
arrisRouterLanCustomComments.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterLanCustomComments.setStatus(_A)
_ArrisRouterLanCustomRowStatus_Type=RowStatus
_ArrisRouterLanCustomRowStatus_Object=MibTableColumn
arrisRouterLanCustomRowStatus=_ArrisRouterLanCustomRowStatus_Object((1,3,6,1,4,1,4115,1,20,1,1,2,4,5,1,9),_ArrisRouterLanCustomRowStatus_Type())
arrisRouterLanCustomRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterLanCustomRowStatus.setStatus(_A)
_ArrisRouterLanClientDHCPOptionsTable_Object=MibTable
arrisRouterLanClientDHCPOptionsTable=_ArrisRouterLanClientDHCPOptionsTable_Object((1,3,6,1,4,1,4115,1,20,1,1,2,4,8))
if mibBuilder.loadTexts:arrisRouterLanClientDHCPOptionsTable.setStatus(_A)
_ArrisRouterLanClientDHCPOptionsEntry_Object=MibTableRow
arrisRouterLanClientDHCPOptionsEntry=_ArrisRouterLanClientDHCPOptionsEntry_Object((1,3,6,1,4,1,4115,1,20,1,1,2,4,8,1))
arrisRouterLanClientDHCPOptionsEntry.setIndexNames((0,_K,_L),(0,_I,_i),(0,_I,_j),(0,_I,_A2))
if mibBuilder.loadTexts:arrisRouterLanClientDHCPOptionsEntry.setStatus(_A)
class _ArrisRouterLanClientDHCPOptionsIdx_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_ArrisRouterLanClientDHCPOptionsIdx_Type.__name__=_H
_ArrisRouterLanClientDHCPOptionsIdx_Object=MibTableColumn
arrisRouterLanClientDHCPOptionsIdx=_ArrisRouterLanClientDHCPOptionsIdx_Object((1,3,6,1,4,1,4115,1,20,1,1,2,4,8,1,1),_ArrisRouterLanClientDHCPOptionsIdx_Type())
arrisRouterLanClientDHCPOptionsIdx.setMaxAccess(_J)
if mibBuilder.loadTexts:arrisRouterLanClientDHCPOptionsIdx.setStatus(_A)
class _ArrisRouterLanClientDHCPOptionsTag_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_ArrisRouterLanClientDHCPOptionsTag_Type.__name__=_H
_ArrisRouterLanClientDHCPOptionsTag_Object=MibTableColumn
arrisRouterLanClientDHCPOptionsTag=_ArrisRouterLanClientDHCPOptionsTag_Object((1,3,6,1,4,1,4115,1,20,1,1,2,4,8,1,2),_ArrisRouterLanClientDHCPOptionsTag_Type())
arrisRouterLanClientDHCPOptionsTag.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterLanClientDHCPOptionsTag.setStatus(_A)
class _ArrisRouterLanClientDHCPOptionsValue_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ArrisRouterLanClientDHCPOptionsValue_Type.__name__=_G
_ArrisRouterLanClientDHCPOptionsValue_Object=MibTableColumn
arrisRouterLanClientDHCPOptionsValue=_ArrisRouterLanClientDHCPOptionsValue_Object((1,3,6,1,4,1,4115,1,20,1,1,2,4,8,1,3),_ArrisRouterLanClientDHCPOptionsValue_Type())
arrisRouterLanClientDHCPOptionsValue.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterLanClientDHCPOptionsValue.setStatus(_A)
_ArrisRouterLanClientDHCPOptionsRowStatus_Type=RowStatus
_ArrisRouterLanClientDHCPOptionsRowStatus_Object=MibTableColumn
arrisRouterLanClientDHCPOptionsRowStatus=_ArrisRouterLanClientDHCPOptionsRowStatus_Object((1,3,6,1,4,1,4115,1,20,1,1,2,4,8,1,4),_ArrisRouterLanClientDHCPOptionsRowStatus_Type())
arrisRouterLanClientDHCPOptionsRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterLanClientDHCPOptionsRowStatus.setStatus(_A)
_ArrisRouterRIPObjects_ObjectIdentity=ObjectIdentity
arrisRouterRIPObjects=_ArrisRouterRIPObjects_ObjectIdentity((1,3,6,1,4,1,4115,1,20,1,1,2,5))
_ArrisRouterRIPEnable_Type=TruthValue
_ArrisRouterRIPEnable_Object=MibScalar
arrisRouterRIPEnable=_ArrisRouterRIPEnable_Object((1,3,6,1,4,1,4115,1,20,1,1,2,5,1),_ArrisRouterRIPEnable_Type())
arrisRouterRIPEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterRIPEnable.setStatus(_A)
class _ArrisRouterRIPAuthEnable_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,0,1,2)));namedValues=NamedValues(*((_N,-1),('disable',0),('textAuth',1),('md5Auth',2)))
_ArrisRouterRIPAuthEnable_Type.__name__=_D
_ArrisRouterRIPAuthEnable_Object=MibScalar
arrisRouterRIPAuthEnable=_ArrisRouterRIPAuthEnable_Object((1,3,6,1,4,1,4115,1,20,1,1,2,5,2),_ArrisRouterRIPAuthEnable_Type())
arrisRouterRIPAuthEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterRIPAuthEnable.setStatus(_A)
class _ArrisRouterRIPReportTime_Type(Unsigned32):defaultValue=30
_ArrisRouterRIPReportTime_Type.__name__=_H
_ArrisRouterRIPReportTime_Object=MibScalar
arrisRouterRIPReportTime=_ArrisRouterRIPReportTime_Object((1,3,6,1,4,1,4115,1,20,1,1,2,5,3),_ArrisRouterRIPReportTime_Type())
arrisRouterRIPReportTime.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterRIPReportTime.setStatus(_A)
if mibBuilder.loadTexts:arrisRouterRIPReportTime.setUnits(_M)
class _ArrisRouterRIPAuthKeyString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_ArrisRouterRIPAuthKeyString_Type.__name__=_G
_ArrisRouterRIPAuthKeyString_Object=MibScalar
arrisRouterRIPAuthKeyString=_ArrisRouterRIPAuthKeyString_Object((1,3,6,1,4,1,4115,1,20,1,1,2,5,4),_ArrisRouterRIPAuthKeyString_Type())
arrisRouterRIPAuthKeyString.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterRIPAuthKeyString.setStatus(_A)
class _ArrisRouterRIPAuthKeyID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ArrisRouterRIPAuthKeyID_Type.__name__=_D
_ArrisRouterRIPAuthKeyID_Object=MibScalar
arrisRouterRIPAuthKeyID=_ArrisRouterRIPAuthKeyID_Object((1,3,6,1,4,1,4115,1,20,1,1,2,5,5),_ArrisRouterRIPAuthKeyID_Type())
arrisRouterRIPAuthKeyID.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterRIPAuthKeyID.setStatus(_A)
_ArrisRouterRIPIPAddrType_Type=InetAddressType
_ArrisRouterRIPIPAddrType_Object=MibScalar
arrisRouterRIPIPAddrType=_ArrisRouterRIPIPAddrType_Object((1,3,6,1,4,1,4115,1,20,1,1,2,5,6),_ArrisRouterRIPIPAddrType_Type())
arrisRouterRIPIPAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterRIPIPAddrType.setStatus(_A)
_ArrisRouterRIPIPAddr_Type=InetAddress
_ArrisRouterRIPIPAddr_Object=MibScalar
arrisRouterRIPIPAddr=_ArrisRouterRIPIPAddr_Object((1,3,6,1,4,1,4115,1,20,1,1,2,5,7),_ArrisRouterRIPIPAddr_Type())
arrisRouterRIPIPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterRIPIPAddr.setStatus(_A)
_ArrisRouterRIPPrefixLen_Type=InetAddressPrefixLength
_ArrisRouterRIPPrefixLen_Object=MibScalar
arrisRouterRIPPrefixLen=_ArrisRouterRIPPrefixLen_Object((1,3,6,1,4,1,4115,1,20,1,1,2,5,8),_ArrisRouterRIPPrefixLen_Type())
arrisRouterRIPPrefixLen.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterRIPPrefixLen.setStatus(_A)
class _ArrisRouterRIPAuthKeyChain_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ArrisRouterRIPAuthKeyChain_Type.__name__=_G
_ArrisRouterRIPAuthKeyChain_Object=MibScalar
arrisRouterRIPAuthKeyChain=_ArrisRouterRIPAuthKeyChain_Object((1,3,6,1,4,1,4115,1,20,1,1,2,5,9),_ArrisRouterRIPAuthKeyChain_Type())
arrisRouterRIPAuthKeyChain.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterRIPAuthKeyChain.setStatus(_A)
_ArrisRouterRIPRoutedSubnetIPType_Type=InetAddressType
_ArrisRouterRIPRoutedSubnetIPType_Object=MibScalar
arrisRouterRIPRoutedSubnetIPType=_ArrisRouterRIPRoutedSubnetIPType_Object((1,3,6,1,4,1,4115,1,20,1,1,2,5,10),_ArrisRouterRIPRoutedSubnetIPType_Type())
arrisRouterRIPRoutedSubnetIPType.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterRIPRoutedSubnetIPType.setStatus(_A)
_ArrisRouterRIPRoutedSubnetIP_Type=InetAddress
_ArrisRouterRIPRoutedSubnetIP_Object=MibScalar
arrisRouterRIPRoutedSubnetIP=_ArrisRouterRIPRoutedSubnetIP_Object((1,3,6,1,4,1,4115,1,20,1,1,2,5,11),_ArrisRouterRIPRoutedSubnetIP_Type())
arrisRouterRIPRoutedSubnetIP.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterRIPRoutedSubnetIP.setStatus(_A)
class _ArrisRouterRIPRoutedSubnetGWNetIPType_Type(InetAddressType):defaultValue=1
_ArrisRouterRIPRoutedSubnetGWNetIPType_Type.__name__=_S
_ArrisRouterRIPRoutedSubnetGWNetIPType_Object=MibScalar
arrisRouterRIPRoutedSubnetGWNetIPType=_ArrisRouterRIPRoutedSubnetGWNetIPType_Object((1,3,6,1,4,1,4115,1,20,1,1,2,5,12),_ArrisRouterRIPRoutedSubnetGWNetIPType_Type())
arrisRouterRIPRoutedSubnetGWNetIPType.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterRIPRoutedSubnetGWNetIPType.setStatus(_A)
_ArrisRouterRIPRoutedSubnetGWNetIP_Type=InetAddress
_ArrisRouterRIPRoutedSubnetGWNetIP_Object=MibScalar
arrisRouterRIPRoutedSubnetGWNetIP=_ArrisRouterRIPRoutedSubnetGWNetIP_Object((1,3,6,1,4,1,4115,1,20,1,1,2,5,13),_ArrisRouterRIPRoutedSubnetGWNetIP_Type())
arrisRouterRIPRoutedSubnetGWNetIP.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterRIPRoutedSubnetGWNetIP.setStatus(_A)
_ArrisRouterRIPRoutedSubnetMask_Type=InetAddress
_ArrisRouterRIPRoutedSubnetMask_Object=MibScalar
arrisRouterRIPRoutedSubnetMask=_ArrisRouterRIPRoutedSubnetMask_Object((1,3,6,1,4,1,4115,1,20,1,1,2,5,14),_ArrisRouterRIPRoutedSubnetMask_Type())
arrisRouterRIPRoutedSubnetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterRIPRoutedSubnetMask.setStatus(_A)
_ArrisRouterRIPRoutedSubnetEnabled_Type=TruthValue
_ArrisRouterRIPRoutedSubnetEnabled_Object=MibScalar
arrisRouterRIPRoutedSubnetEnabled=_ArrisRouterRIPRoutedSubnetEnabled_Object((1,3,6,1,4,1,4115,1,20,1,1,2,5,15),_ArrisRouterRIPRoutedSubnetEnabled_Type())
arrisRouterRIPRoutedSubnetEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterRIPRoutedSubnetEnabled.setStatus(_A)
class _ArrisRouterRIPSendCMInterface_Type(TruthValue):defaultValue=2
_ArrisRouterRIPSendCMInterface_Type.__name__=_F
_ArrisRouterRIPSendCMInterface_Object=MibScalar
arrisRouterRIPSendCMInterface=_ArrisRouterRIPSendCMInterface_Object((1,3,6,1,4,1,4115,1,20,1,1,2,5,16),_ArrisRouterRIPSendCMInterface_Type())
arrisRouterRIPSendCMInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterRIPSendCMInterface.setStatus(_A)
class _ArrisRouterRIPRoutedSubnetDHCP_Type(TruthValue):defaultValue=2
_ArrisRouterRIPRoutedSubnetDHCP_Type.__name__=_F
_ArrisRouterRIPRoutedSubnetDHCP_Object=MibScalar
arrisRouterRIPRoutedSubnetDHCP=_ArrisRouterRIPRoutedSubnetDHCP_Object((1,3,6,1,4,1,4115,1,20,1,1,2,5,17),_ArrisRouterRIPRoutedSubnetDHCP_Type())
arrisRouterRIPRoutedSubnetDHCP.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterRIPRoutedSubnetDHCP.setStatus(_A)
class _ArrisRouterRIPRoutedSubnetNAT_Type(TruthValue):defaultValue=2
_ArrisRouterRIPRoutedSubnetNAT_Type.__name__=_F
_ArrisRouterRIPRoutedSubnetNAT_Object=MibScalar
arrisRouterRIPRoutedSubnetNAT=_ArrisRouterRIPRoutedSubnetNAT_Object((1,3,6,1,4,1,4115,1,20,1,1,2,5,18),_ArrisRouterRIPRoutedSubnetNAT_Type())
arrisRouterRIPRoutedSubnetNAT.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterRIPRoutedSubnetNAT.setStatus(_A)
class _ArrisRouterLanSettings_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,10,11,12)));namedValues=NamedValues(*(('doNothing',0),('applyPrimaryLan',1),('applyGuestLans',2),('applyAllLans',3),('revertSettings',10),('resetDefaults',11),('restartWLAN',12)))
_ArrisRouterLanSettings_Type.__name__=_D
_ArrisRouterLanSettings_Object=MibScalar
arrisRouterLanSettings=_ArrisRouterLanSettings_Object((1,3,6,1,4,1,4115,1,20,1,1,2,6),_ArrisRouterLanSettings_Type())
arrisRouterLanSettings.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterLanSettings.setStatus(_A)
_ArrisRouterLanEtherPortTable_Object=MibTable
arrisRouterLanEtherPortTable=_ArrisRouterLanEtherPortTable_Object((1,3,6,1,4,1,4115,1,20,1,1,2,8))
if mibBuilder.loadTexts:arrisRouterLanEtherPortTable.setStatus(_A)
_ArrisRouterLanEtherPortEntry_Object=MibTableRow
arrisRouterLanEtherPortEntry=_ArrisRouterLanEtherPortEntry_Object((1,3,6,1,4,1,4115,1,20,1,1,2,8,1))
arrisRouterLanEtherPortEntry.setIndexNames((0,_I,_A3))
if mibBuilder.loadTexts:arrisRouterLanEtherPortEntry.setStatus(_A)
_ArrisRouterLanEtherPortIdx_Type=Unsigned32
_ArrisRouterLanEtherPortIdx_Object=MibTableColumn
arrisRouterLanEtherPortIdx=_ArrisRouterLanEtherPortIdx_Object((1,3,6,1,4,1,4115,1,20,1,1,2,8,1,1),_ArrisRouterLanEtherPortIdx_Type())
arrisRouterLanEtherPortIdx.setMaxAccess(_J)
if mibBuilder.loadTexts:arrisRouterLanEtherPortIdx.setStatus(_A)
_ArrisRouterLanEtherPortIFIndex_Type=Integer32
_ArrisRouterLanEtherPortIFIndex_Object=MibTableColumn
arrisRouterLanEtherPortIFIndex=_ArrisRouterLanEtherPortIFIndex_Object((1,3,6,1,4,1,4115,1,20,1,1,2,8,1,2),_ArrisRouterLanEtherPortIFIndex_Type())
arrisRouterLanEtherPortIFIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterLanEtherPortIFIndex.setStatus(_A)
class _ArrisRouterLanEtherPortEnabled_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_O,0),(_Q,1)))
_ArrisRouterLanEtherPortEnabled_Type.__name__=_D
_ArrisRouterLanEtherPortEnabled_Object=MibTableColumn
arrisRouterLanEtherPortEnabled=_ArrisRouterLanEtherPortEnabled_Object((1,3,6,1,4,1,4115,1,20,1,1,2,8,1,3),_ArrisRouterLanEtherPortEnabled_Type())
arrisRouterLanEtherPortEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterLanEtherPortEnabled.setStatus(_A)
class _ArrisRouterLanEtherPortDuplex_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('halfDuplex',0),('fullDuplex',1)))
_ArrisRouterLanEtherPortDuplex_Type.__name__=_D
_ArrisRouterLanEtherPortDuplex_Object=MibTableColumn
arrisRouterLanEtherPortDuplex=_ArrisRouterLanEtherPortDuplex_Object((1,3,6,1,4,1,4115,1,20,1,1,2,8,1,4),_ArrisRouterLanEtherPortDuplex_Type())
arrisRouterLanEtherPortDuplex.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterLanEtherPortDuplex.setStatus(_A)
_ArrisRouterLanEtherPortSpeed_Type=Integer32
_ArrisRouterLanEtherPortSpeed_Object=MibTableColumn
arrisRouterLanEtherPortSpeed=_ArrisRouterLanEtherPortSpeed_Object((1,3,6,1,4,1,4115,1,20,1,1,2,8,1,5),_ArrisRouterLanEtherPortSpeed_Type())
arrisRouterLanEtherPortSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterLanEtherPortSpeed.setStatus(_A)
class _ArrisRouterLanEtherPortAuto_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('manualConfigure',0),('autoNegotiate',1)))
_ArrisRouterLanEtherPortAuto_Type.__name__=_D
_ArrisRouterLanEtherPortAuto_Object=MibTableColumn
arrisRouterLanEtherPortAuto=_ArrisRouterLanEtherPortAuto_Object((1,3,6,1,4,1,4115,1,20,1,1,2,8,1,6),_ArrisRouterLanEtherPortAuto_Type())
arrisRouterLanEtherPortAuto.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterLanEtherPortAuto.setStatus(_A)
_ArrisRouterLanEtherPortHasLink_Type=TruthValue
_ArrisRouterLanEtherPortHasLink_Object=MibTableColumn
arrisRouterLanEtherPortHasLink=_ArrisRouterLanEtherPortHasLink_Object((1,3,6,1,4,1,4115,1,20,1,1,2,8,1,7),_ArrisRouterLanEtherPortHasLink_Type())
arrisRouterLanEtherPortHasLink.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterLanEtherPortHasLink.setStatus(_A)
_ArrisRouterRIPngObjects_ObjectIdentity=ObjectIdentity
arrisRouterRIPngObjects=_ArrisRouterRIPngObjects_ObjectIdentity((1,3,6,1,4,1,4115,1,20,1,1,2,9))
_ArrisRouterRIPngEnable_Type=TruthValue
_ArrisRouterRIPngEnable_Object=MibScalar
arrisRouterRIPngEnable=_ArrisRouterRIPngEnable_Object((1,3,6,1,4,1,4115,1,20,1,1,2,9,1),_ArrisRouterRIPngEnable_Type())
arrisRouterRIPngEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterRIPngEnable.setStatus(_A)
_ArrisRouterRIPngAddr_Type=InetAddressIPv6
_ArrisRouterRIPngAddr_Object=MibScalar
arrisRouterRIPngAddr=_ArrisRouterRIPngAddr_Object((1,3,6,1,4,1,4115,1,20,1,1,2,9,2),_ArrisRouterRIPngAddr_Type())
arrisRouterRIPngAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterRIPngAddr.setStatus(_A)
_ArrisRouterRIPngSubnetEnable_Type=TruthValue
_ArrisRouterRIPngSubnetEnable_Object=MibScalar
arrisRouterRIPngSubnetEnable=_ArrisRouterRIPngSubnetEnable_Object((1,3,6,1,4,1,4115,1,20,1,1,2,9,3),_ArrisRouterRIPngSubnetEnable_Type())
arrisRouterRIPngSubnetEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterRIPngSubnetEnable.setStatus(_A)
_ArrisRouterRIPngRoutedSubnetAddr_Type=InetAddressIPv6
_ArrisRouterRIPngRoutedSubnetAddr_Object=MibScalar
arrisRouterRIPngRoutedSubnetAddr=_ArrisRouterRIPngRoutedSubnetAddr_Object((1,3,6,1,4,1,4115,1,20,1,1,2,9,4),_ArrisRouterRIPngRoutedSubnetAddr_Type())
arrisRouterRIPngRoutedSubnetAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterRIPngRoutedSubnetAddr.setStatus(_A)
class _ArrisRouterRIPngRoutedSubnetPrefixLength_Type(Integer32):defaultValue=64
_ArrisRouterRIPngRoutedSubnetPrefixLength_Type.__name__=_D
_ArrisRouterRIPngRoutedSubnetPrefixLength_Object=MibScalar
arrisRouterRIPngRoutedSubnetPrefixLength=_ArrisRouterRIPngRoutedSubnetPrefixLength_Object((1,3,6,1,4,1,4115,1,20,1,1,2,9,5),_ArrisRouterRIPngRoutedSubnetPrefixLength_Type())
arrisRouterRIPngRoutedSubnetPrefixLength.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterRIPngRoutedSubnetPrefixLength.setStatus(_A)
class _ArrisRouterRIPngSendCMInterface_Type(TruthValue):defaultValue=2
_ArrisRouterRIPngSendCMInterface_Type.__name__=_F
_ArrisRouterRIPngSendCMInterface_Object=MibScalar
arrisRouterRIPngSendCMInterface=_ArrisRouterRIPngSendCMInterface_Object((1,3,6,1,4,1,4115,1,20,1,1,2,9,6),_ArrisRouterRIPngSendCMInterface_Type())
arrisRouterRIPngSendCMInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterRIPngSendCMInterface.setStatus(_A)
_ArrisRouterLanSrvDHCPOptionsTable_Object=MibTable
arrisRouterLanSrvDHCPOptionsTable=_ArrisRouterLanSrvDHCPOptionsTable_Object((1,3,6,1,4,1,4115,1,20,1,1,2,11))
if mibBuilder.loadTexts:arrisRouterLanSrvDHCPOptionsTable.setStatus(_A)
_ArrisRouterLanSrvDHCPOptionsEntry_Object=MibTableRow
arrisRouterLanSrvDHCPOptionsEntry=_ArrisRouterLanSrvDHCPOptionsEntry_Object((1,3,6,1,4,1,4115,1,20,1,1,2,11,1))
arrisRouterLanSrvDHCPOptionsEntry.setIndexNames((0,_K,_L),(0,_I,_A4))
if mibBuilder.loadTexts:arrisRouterLanSrvDHCPOptionsEntry.setStatus(_A)
_ArrisRouterLanSrvDHCPOptionsIdx_Type=Unsigned32
_ArrisRouterLanSrvDHCPOptionsIdx_Object=MibTableColumn
arrisRouterLanSrvDHCPOptionsIdx=_ArrisRouterLanSrvDHCPOptionsIdx_Object((1,3,6,1,4,1,4115,1,20,1,1,2,11,1,1),_ArrisRouterLanSrvDHCPOptionsIdx_Type())
arrisRouterLanSrvDHCPOptionsIdx.setMaxAccess(_J)
if mibBuilder.loadTexts:arrisRouterLanSrvDHCPOptionsIdx.setStatus(_A)
class _ArrisRouterLanSrvDHCPOptionsEnable_Type(TruthValue):defaultValue=1
_ArrisRouterLanSrvDHCPOptionsEnable_Type.__name__=_F
_ArrisRouterLanSrvDHCPOptionsEnable_Object=MibTableColumn
arrisRouterLanSrvDHCPOptionsEnable=_ArrisRouterLanSrvDHCPOptionsEnable_Object((1,3,6,1,4,1,4115,1,20,1,1,2,11,1,2),_ArrisRouterLanSrvDHCPOptionsEnable_Type())
arrisRouterLanSrvDHCPOptionsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterLanSrvDHCPOptionsEnable.setStatus(_A)
_ArrisRouterLanSrvDHCPOptionsIPAddrType_Type=InetAddressType
_ArrisRouterLanSrvDHCPOptionsIPAddrType_Object=MibTableColumn
arrisRouterLanSrvDHCPOptionsIPAddrType=_ArrisRouterLanSrvDHCPOptionsIPAddrType_Object((1,3,6,1,4,1,4115,1,20,1,1,2,11,1,3),_ArrisRouterLanSrvDHCPOptionsIPAddrType_Type())
arrisRouterLanSrvDHCPOptionsIPAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterLanSrvDHCPOptionsIPAddrType.setStatus(_A)
class _ArrisRouterLanSrvDHCPOptionsTag_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_ArrisRouterLanSrvDHCPOptionsTag_Type.__name__=_H
_ArrisRouterLanSrvDHCPOptionsTag_Object=MibTableColumn
arrisRouterLanSrvDHCPOptionsTag=_ArrisRouterLanSrvDHCPOptionsTag_Object((1,3,6,1,4,1,4115,1,20,1,1,2,11,1,4),_ArrisRouterLanSrvDHCPOptionsTag_Type())
arrisRouterLanSrvDHCPOptionsTag.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterLanSrvDHCPOptionsTag.setStatus(_A)
class _ArrisRouterLanSrvDHCPOptionsValue_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ArrisRouterLanSrvDHCPOptionsValue_Type.__name__=_G
_ArrisRouterLanSrvDHCPOptionsValue_Object=MibTableColumn
arrisRouterLanSrvDHCPOptionsValue=_ArrisRouterLanSrvDHCPOptionsValue_Object((1,3,6,1,4,1,4115,1,20,1,1,2,11,1,5),_ArrisRouterLanSrvDHCPOptionsValue_Type())
arrisRouterLanSrvDHCPOptionsValue.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterLanSrvDHCPOptionsValue.setStatus(_A)
_ArrisRouterLanSrvDHCPOptionsRowStatus_Type=RowStatus
_ArrisRouterLanSrvDHCPOptionsRowStatus_Object=MibTableColumn
arrisRouterLanSrvDHCPOptionsRowStatus=_ArrisRouterLanSrvDHCPOptionsRowStatus_Object((1,3,6,1,4,1,4115,1,20,1,1,2,11,1,6),_ArrisRouterLanSrvDHCPOptionsRowStatus_Type())
arrisRouterLanSrvDHCPOptionsRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterLanSrvDHCPOptionsRowStatus.setStatus(_A)
class _ArrisRouterLanMaxIPv6RAInterval_Type(Unsigned32):defaultValue=3
_ArrisRouterLanMaxIPv6RAInterval_Type.__name__=_H
_ArrisRouterLanMaxIPv6RAInterval_Object=MibScalar
arrisRouterLanMaxIPv6RAInterval=_ArrisRouterLanMaxIPv6RAInterval_Object((1,3,6,1,4,1,4115,1,20,1,1,2,13),_ArrisRouterLanMaxIPv6RAInterval_Type())
arrisRouterLanMaxIPv6RAInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterLanMaxIPv6RAInterval.setStatus(_A)
if mibBuilder.loadTexts:arrisRouterLanMaxIPv6RAInterval.setUnits(_M)
class _ArrisRouterLanMinIPv6RAInterval_Type(Unsigned32):defaultValue=3
_ArrisRouterLanMinIPv6RAInterval_Type.__name__=_H
_ArrisRouterLanMinIPv6RAInterval_Object=MibScalar
arrisRouterLanMinIPv6RAInterval=_ArrisRouterLanMinIPv6RAInterval_Object((1,3,6,1,4,1,4115,1,20,1,1,2,14),_ArrisRouterLanMinIPv6RAInterval_Type())
arrisRouterLanMinIPv6RAInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterLanMinIPv6RAInterval.setStatus(_A)
if mibBuilder.loadTexts:arrisRouterLanMinIPv6RAInterval.setUnits(_M)
class _ArrisRouterLanBridgeType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('subnetBridge',0),('fullBridge',1)))
_ArrisRouterLanBridgeType_Type.__name__=_D
_ArrisRouterLanBridgeType_Object=MibScalar
arrisRouterLanBridgeType=_ArrisRouterLanBridgeType_Object((1,3,6,1,4,1,4115,1,20,1,1,2,15),_ArrisRouterLanBridgeType_Type())
arrisRouterLanBridgeType.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterLanBridgeType.setStatus(_A)
_ArrisRouterLanUSBPortTable_Object=MibTable
arrisRouterLanUSBPortTable=_ArrisRouterLanUSBPortTable_Object((1,3,6,1,4,1,4115,1,20,1,1,2,16))
if mibBuilder.loadTexts:arrisRouterLanUSBPortTable.setStatus(_A)
_ArrisRouterLanUSBPortEntry_Object=MibTableRow
arrisRouterLanUSBPortEntry=_ArrisRouterLanUSBPortEntry_Object((1,3,6,1,4,1,4115,1,20,1,1,2,16,1))
arrisRouterLanUSBPortEntry.setIndexNames((0,_I,_A5))
if mibBuilder.loadTexts:arrisRouterLanUSBPortEntry.setStatus(_A)
class _ArrisRouterLanUSBPortIdx_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_ArrisRouterLanUSBPortIdx_Type.__name__=_H
_ArrisRouterLanUSBPortIdx_Object=MibTableColumn
arrisRouterLanUSBPortIdx=_ArrisRouterLanUSBPortIdx_Object((1,3,6,1,4,1,4115,1,20,1,1,2,16,1,1),_ArrisRouterLanUSBPortIdx_Type())
arrisRouterLanUSBPortIdx.setMaxAccess(_J)
if mibBuilder.loadTexts:arrisRouterLanUSBPortIdx.setStatus(_A)
_ArrisRouterLanUSBPortHasLink_Type=TruthValue
_ArrisRouterLanUSBPortHasLink_Object=MibTableColumn
arrisRouterLanUSBPortHasLink=_ArrisRouterLanUSBPortHasLink_Object((1,3,6,1,4,1,4115,1,20,1,1,2,16,1,2),_ArrisRouterLanUSBPortHasLink_Type())
arrisRouterLanUSBPortHasLink.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterLanUSBPortHasLink.setStatus(_A)
class _ArrisRouterLanUSBPortDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ArrisRouterLanUSBPortDescr_Type.__name__=_G
_ArrisRouterLanUSBPortDescr_Object=MibTableColumn
arrisRouterLanUSBPortDescr=_ArrisRouterLanUSBPortDescr_Object((1,3,6,1,4,1,4115,1,20,1,1,2,16,1,3),_ArrisRouterLanUSBPortDescr_Type())
arrisRouterLanUSBPortDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterLanUSBPortDescr.setStatus(_A)
class _ArrisRouterLanUSBPortSerialNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ArrisRouterLanUSBPortSerialNum_Type.__name__=_G
_ArrisRouterLanUSBPortSerialNum_Object=MibTableColumn
arrisRouterLanUSBPortSerialNum=_ArrisRouterLanUSBPortSerialNum_Object((1,3,6,1,4,1,4115,1,20,1,1,2,16,1,4),_ArrisRouterLanUSBPortSerialNum_Type())
arrisRouterLanUSBPortSerialNum.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterLanUSBPortSerialNum.setStatus(_A)
_ArrisRouterLanUSBPortSpeed_Type=Integer32
_ArrisRouterLanUSBPortSpeed_Object=MibTableColumn
arrisRouterLanUSBPortSpeed=_ArrisRouterLanUSBPortSpeed_Object((1,3,6,1,4,1,4115,1,20,1,1,2,16,1,5),_ArrisRouterLanUSBPortSpeed_Type())
arrisRouterLanUSBPortSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterLanUSBPortSpeed.setStatus(_A)
if mibBuilder.loadTexts:arrisRouterLanUSBPortSpeed.setUnits('Mbps')
class _ArrisRouterLanUSBPortManuf_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ArrisRouterLanUSBPortManuf_Type.__name__=_G
_ArrisRouterLanUSBPortManuf_Object=MibTableColumn
arrisRouterLanUSBPortManuf=_ArrisRouterLanUSBPortManuf_Object((1,3,6,1,4,1,4115,1,20,1,1,2,16,1,6),_ArrisRouterLanUSBPortManuf_Type())
arrisRouterLanUSBPortManuf.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterLanUSBPortManuf.setStatus(_A)
class _ArrisRouterLanUSBPortStorageNam_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ArrisRouterLanUSBPortStorageNam_Type.__name__=_G
_ArrisRouterLanUSBPortStorageNam_Object=MibTableColumn
arrisRouterLanUSBPortStorageNam=_ArrisRouterLanUSBPortStorageNam_Object((1,3,6,1,4,1,4115,1,20,1,1,2,16,1,7),_ArrisRouterLanUSBPortStorageNam_Type())
arrisRouterLanUSBPortStorageNam.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterLanUSBPortStorageNam.setStatus(_A)
class _ArrisRouterLanUSBPortFileSys_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ArrisRouterLanUSBPortFileSys_Type.__name__=_G
_ArrisRouterLanUSBPortFileSys_Object=MibTableColumn
arrisRouterLanUSBPortFileSys=_ArrisRouterLanUSBPortFileSys_Object((1,3,6,1,4,1,4115,1,20,1,1,2,16,1,8),_ArrisRouterLanUSBPortFileSys_Type())
arrisRouterLanUSBPortFileSys.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterLanUSBPortFileSys.setStatus(_A)
class _ArrisRouterLanUSBPortSpaceAvail_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ArrisRouterLanUSBPortSpaceAvail_Type.__name__=_G
_ArrisRouterLanUSBPortSpaceAvail_Object=MibTableColumn
arrisRouterLanUSBPortSpaceAvail=_ArrisRouterLanUSBPortSpaceAvail_Object((1,3,6,1,4,1,4115,1,20,1,1,2,16,1,9),_ArrisRouterLanUSBPortSpaceAvail_Type())
arrisRouterLanUSBPortSpaceAvail.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterLanUSBPortSpaceAvail.setStatus(_A)
class _ArrisRouterLanUSBPortTotalSpace_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ArrisRouterLanUSBPortTotalSpace_Type.__name__=_G
_ArrisRouterLanUSBPortTotalSpace_Object=MibTableColumn
arrisRouterLanUSBPortTotalSpace=_ArrisRouterLanUSBPortTotalSpace_Object((1,3,6,1,4,1,4115,1,20,1,1,2,16,1,10),_ArrisRouterLanUSBPortTotalSpace_Type())
arrisRouterLanUSBPortTotalSpace.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterLanUSBPortTotalSpace.setStatus(_A)
class _ArrisRouterLanUsbPortFoldersFile_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_ArrisRouterLanUsbPortFoldersFile_Type.__name__=_G
_ArrisRouterLanUsbPortFoldersFile_Object=MibTableColumn
arrisRouterLanUsbPortFoldersFile=_ArrisRouterLanUsbPortFoldersFile_Object((1,3,6,1,4,1,4115,1,20,1,1,2,16,1,11),_ArrisRouterLanUsbPortFoldersFile_Type())
arrisRouterLanUsbPortFoldersFile.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterLanUsbPortFoldersFile.setStatus(_A)
_ArrisRouterLanUSBPortDelStorage_Type=TruthValue
_ArrisRouterLanUSBPortDelStorage_Object=MibTableColumn
arrisRouterLanUSBPortDelStorage=_ArrisRouterLanUSBPortDelStorage_Object((1,3,6,1,4,1,4115,1,20,1,1,2,16,1,12),_ArrisRouterLanUSBPortDelStorage_Type())
arrisRouterLanUSBPortDelStorage.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterLanUSBPortDelStorage.setStatus(_A)
_ArrisRouterLanFileSharingObjs_ObjectIdentity=ObjectIdentity
arrisRouterLanFileSharingObjs=_ArrisRouterLanFileSharingObjs_ObjectIdentity((1,3,6,1,4,1,4115,1,20,1,1,2,17))
class _ArrisRouterLanFilesharingEnable_Type(TruthValue):defaultValue=1
_ArrisRouterLanFilesharingEnable_Type.__name__=_F
_ArrisRouterLanFilesharingEnable_Object=MibScalar
arrisRouterLanFilesharingEnable=_ArrisRouterLanFilesharingEnable_Object((1,3,6,1,4,1,4115,1,20,1,1,2,17,1),_ArrisRouterLanFilesharingEnable_Type())
arrisRouterLanFilesharingEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterLanFilesharingEnable.setStatus(_A)
class _ArrisRouterLanFilesharingDevName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ArrisRouterLanFilesharingDevName_Type.__name__=_G
_ArrisRouterLanFilesharingDevName_Object=MibScalar
arrisRouterLanFilesharingDevName=_ArrisRouterLanFilesharingDevName_Object((1,3,6,1,4,1,4115,1,20,1,1,2,17,2),_ArrisRouterLanFilesharingDevName_Type())
arrisRouterLanFilesharingDevName.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterLanFilesharingDevName.setStatus(_A)
_ArrisRouterLanFileSharingTable_Object=MibTable
arrisRouterLanFileSharingTable=_ArrisRouterLanFileSharingTable_Object((1,3,6,1,4,1,4115,1,20,1,1,2,17,3))
if mibBuilder.loadTexts:arrisRouterLanFileSharingTable.setStatus(_A)
_ArrisRouterLanFileSharingEntry_Object=MibTableRow
arrisRouterLanFileSharingEntry=_ArrisRouterLanFileSharingEntry_Object((1,3,6,1,4,1,4115,1,20,1,1,2,17,3,1))
arrisRouterLanFileSharingEntry.setIndexNames((0,_I,_k))
if mibBuilder.loadTexts:arrisRouterLanFileSharingEntry.setStatus(_A)
class _ArrisRouterLanFilesharingIdx_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_ArrisRouterLanFilesharingIdx_Type.__name__=_H
_ArrisRouterLanFilesharingIdx_Object=MibTableColumn
arrisRouterLanFilesharingIdx=_ArrisRouterLanFilesharingIdx_Object((1,3,6,1,4,1,4115,1,20,1,1,2,17,3,1,1),_ArrisRouterLanFilesharingIdx_Type())
arrisRouterLanFilesharingIdx.setMaxAccess(_J)
if mibBuilder.loadTexts:arrisRouterLanFilesharingIdx.setStatus(_A)
_ArrisRouterLanFilesharingRowStatus_Type=RowStatus
_ArrisRouterLanFilesharingRowStatus_Object=MibTableColumn
arrisRouterLanFilesharingRowStatus=_ArrisRouterLanFilesharingRowStatus_Object((1,3,6,1,4,1,4115,1,20,1,1,2,17,3,1,2),_ArrisRouterLanFilesharingRowStatus_Type())
arrisRouterLanFilesharingRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterLanFilesharingRowStatus.setStatus(_A)
class _ArrisRouterLanFilesharingUsbPort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_ArrisRouterLanFilesharingUsbPort_Type.__name__=_H
_ArrisRouterLanFilesharingUsbPort_Object=MibTableColumn
arrisRouterLanFilesharingUsbPort=_ArrisRouterLanFilesharingUsbPort_Object((1,3,6,1,4,1,4115,1,20,1,1,2,17,3,1,3),_ArrisRouterLanFilesharingUsbPort_Type())
arrisRouterLanFilesharingUsbPort.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterLanFilesharingUsbPort.setStatus(_A)
class _ArrisRouterLanFilesharingDirectory_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_ArrisRouterLanFilesharingDirectory_Type.__name__=_G
_ArrisRouterLanFilesharingDirectory_Object=MibTableColumn
arrisRouterLanFilesharingDirectory=_ArrisRouterLanFilesharingDirectory_Object((1,3,6,1,4,1,4115,1,20,1,1,2,17,3,1,4),_ArrisRouterLanFilesharingDirectory_Type())
arrisRouterLanFilesharingDirectory.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterLanFilesharingDirectory.setStatus(_A)
class _ArrisRouterLanFilesharingName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ArrisRouterLanFilesharingName_Type.__name__=_G
_ArrisRouterLanFilesharingName_Object=MibTableColumn
arrisRouterLanFilesharingName=_ArrisRouterLanFilesharingName_Object((1,3,6,1,4,1,4115,1,20,1,1,2,17,3,1,5),_ArrisRouterLanFilesharingName_Type())
arrisRouterLanFilesharingName.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterLanFilesharingName.setStatus(_A)
class _ArrisRouterLanFilesharingEnableHttp_Type(TruthValue):defaultValue=2
_ArrisRouterLanFilesharingEnableHttp_Type.__name__=_F
_ArrisRouterLanFilesharingEnableHttp_Object=MibTableColumn
arrisRouterLanFilesharingEnableHttp=_ArrisRouterLanFilesharingEnableHttp_Object((1,3,6,1,4,1,4115,1,20,1,1,2,17,3,1,6),_ArrisRouterLanFilesharingEnableHttp_Type())
arrisRouterLanFilesharingEnableHttp.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterLanFilesharingEnableHttp.setStatus(_A)
class _ArrisRouterLanFilesharingEnableFtp_Type(TruthValue):defaultValue=2
_ArrisRouterLanFilesharingEnableFtp_Type.__name__=_F
_ArrisRouterLanFilesharingEnableFtp_Object=MibTableColumn
arrisRouterLanFilesharingEnableFtp=_ArrisRouterLanFilesharingEnableFtp_Object((1,3,6,1,4,1,4115,1,20,1,1,2,17,3,1,7),_ArrisRouterLanFilesharingEnableFtp_Type())
arrisRouterLanFilesharingEnableFtp.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterLanFilesharingEnableFtp.setStatus(_A)
class _ArrisRouterLanFilesharingVisibility_Type(TruthValue):defaultValue=1
_ArrisRouterLanFilesharingVisibility_Type.__name__=_F
_ArrisRouterLanFilesharingVisibility_Object=MibTableColumn
arrisRouterLanFilesharingVisibility=_ArrisRouterLanFilesharingVisibility_Object((1,3,6,1,4,1,4115,1,20,1,1,2,17,3,1,8),_ArrisRouterLanFilesharingVisibility_Type())
arrisRouterLanFilesharingVisibility.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterLanFilesharingVisibility.setStatus(_A)
class _ArrisRouterLanFilesharingEveryOnePerm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('noAccess',0),('readOnly',1),(_A6,2),(_A7,3)))
_ArrisRouterLanFilesharingEveryOnePerm_Type.__name__=_D
_ArrisRouterLanFilesharingEveryOnePerm_Object=MibTableColumn
arrisRouterLanFilesharingEveryOnePerm=_ArrisRouterLanFilesharingEveryOnePerm_Object((1,3,6,1,4,1,4115,1,20,1,1,2,17,3,1,9),_ArrisRouterLanFilesharingEveryOnePerm_Type())
arrisRouterLanFilesharingEveryOnePerm.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterLanFilesharingEveryOnePerm.setStatus(_A)
class _ArrisRouterLanFilesharingDesc_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_ArrisRouterLanFilesharingDesc_Type.__name__=_G
_ArrisRouterLanFilesharingDesc_Object=MibTableColumn
arrisRouterLanFilesharingDesc=_ArrisRouterLanFilesharingDesc_Object((1,3,6,1,4,1,4115,1,20,1,1,2,17,3,1,10),_ArrisRouterLanFilesharingDesc_Type())
arrisRouterLanFilesharingDesc.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterLanFilesharingDesc.setStatus(_A)
_ArrisRouterLanLocalUserTable_Object=MibTable
arrisRouterLanLocalUserTable=_ArrisRouterLanLocalUserTable_Object((1,3,6,1,4,1,4115,1,20,1,1,2,17,4))
if mibBuilder.loadTexts:arrisRouterLanLocalUserTable.setStatus(_A)
_ArrisRouterLanLocalUserEntry_Object=MibTableRow
arrisRouterLanLocalUserEntry=_ArrisRouterLanLocalUserEntry_Object((1,3,6,1,4,1,4115,1,20,1,1,2,17,4,1))
arrisRouterLanLocalUserEntry.setIndexNames((0,_I,_l))
if mibBuilder.loadTexts:arrisRouterLanLocalUserEntry.setStatus(_A)
class _ArrisRouterLanLocalUserIdx_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_ArrisRouterLanLocalUserIdx_Type.__name__=_H
_ArrisRouterLanLocalUserIdx_Object=MibTableColumn
arrisRouterLanLocalUserIdx=_ArrisRouterLanLocalUserIdx_Object((1,3,6,1,4,1,4115,1,20,1,1,2,17,4,1,1),_ArrisRouterLanLocalUserIdx_Type())
arrisRouterLanLocalUserIdx.setMaxAccess(_J)
if mibBuilder.loadTexts:arrisRouterLanLocalUserIdx.setStatus(_A)
_ArrisRouterLanLocalUserRowStatus_Type=RowStatus
_ArrisRouterLanLocalUserRowStatus_Object=MibTableColumn
arrisRouterLanLocalUserRowStatus=_ArrisRouterLanLocalUserRowStatus_Object((1,3,6,1,4,1,4115,1,20,1,1,2,17,4,1,2),_ArrisRouterLanLocalUserRowStatus_Type())
arrisRouterLanLocalUserRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterLanLocalUserRowStatus.setStatus(_A)
class _ArrisRouterLanLocalUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ArrisRouterLanLocalUserName_Type.__name__=_G
_ArrisRouterLanLocalUserName_Object=MibTableColumn
arrisRouterLanLocalUserName=_ArrisRouterLanLocalUserName_Object((1,3,6,1,4,1,4115,1,20,1,1,2,17,4,1,3),_ArrisRouterLanLocalUserName_Type())
arrisRouterLanLocalUserName.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterLanLocalUserName.setStatus(_A)
class _ArrisRouterLanLocalUserPasswd_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ArrisRouterLanLocalUserPasswd_Type.__name__=_G
_ArrisRouterLanLocalUserPasswd_Object=MibTableColumn
arrisRouterLanLocalUserPasswd=_ArrisRouterLanLocalUserPasswd_Object((1,3,6,1,4,1,4115,1,20,1,1,2,17,4,1,4),_ArrisRouterLanLocalUserPasswd_Type())
arrisRouterLanLocalUserPasswd.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterLanLocalUserPasswd.setStatus(_A)
_ArrisRouterLanFilesharingPermitTable_Object=MibTable
arrisRouterLanFilesharingPermitTable=_ArrisRouterLanFilesharingPermitTable_Object((1,3,6,1,4,1,4115,1,20,1,1,2,17,5))
if mibBuilder.loadTexts:arrisRouterLanFilesharingPermitTable.setStatus(_A)
_ArrisRouterLanFilesharingPermitEntry_Object=MibTableRow
arrisRouterLanFilesharingPermitEntry=_ArrisRouterLanFilesharingPermitEntry_Object((1,3,6,1,4,1,4115,1,20,1,1,2,17,5,1))
arrisRouterLanFilesharingPermitEntry.setIndexNames((0,_I,_k),(0,_I,_l))
if mibBuilder.loadTexts:arrisRouterLanFilesharingPermitEntry.setStatus(_A)
class _ArrisRouterLanFilesharingPermitvalue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('noAccess',0),('readOnly',1),(_A6,2),(_A7,3)))
_ArrisRouterLanFilesharingPermitvalue_Type.__name__=_D
_ArrisRouterLanFilesharingPermitvalue_Object=MibTableColumn
arrisRouterLanFilesharingPermitvalue=_ArrisRouterLanFilesharingPermitvalue_Object((1,3,6,1,4,1,4115,1,20,1,1,2,17,5,1,1),_ArrisRouterLanFilesharingPermitvalue_Type())
arrisRouterLanFilesharingPermitvalue.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterLanFilesharingPermitvalue.setStatus(_A)
class _ArrisRouterLanIPv6RALifetime_Type(Unsigned32):defaultValue=1800
_ArrisRouterLanIPv6RALifetime_Type.__name__=_H
_ArrisRouterLanIPv6RALifetime_Object=MibScalar
arrisRouterLanIPv6RALifetime=_ArrisRouterLanIPv6RALifetime_Object((1,3,6,1,4,1,4115,1,20,1,1,2,19),_ArrisRouterLanIPv6RALifetime_Type())
arrisRouterLanIPv6RALifetime.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterLanIPv6RALifetime.setStatus(_A)
if mibBuilder.loadTexts:arrisRouterLanIPv6RALifetime.setUnits(_M)
_ArrisRouterWirelessCfg_ObjectIdentity=ObjectIdentity
arrisRouterWirelessCfg=_ArrisRouterWirelessCfg_ObjectIdentity((1,3,6,1,4,1,4115,1,20,1,1,3))
class _ArrisRouterWiFiCountry_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_ArrisRouterWiFiCountry_Type.__name__=_G
_ArrisRouterWiFiCountry_Object=MibScalar
arrisRouterWiFiCountry=_ArrisRouterWiFiCountry_Object((1,3,6,1,4,1,4115,1,20,1,1,3,1),_ArrisRouterWiFiCountry_Type())
arrisRouterWiFiCountry.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFiCountry.setStatus(_A)
class _ArrisRouterWiFiChannel_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,216))
_ArrisRouterWiFiChannel_Type.__name__=_H
_ArrisRouterWiFiChannel_Object=MibScalar
arrisRouterWiFiChannel=_ArrisRouterWiFiChannel_Object((1,3,6,1,4,1,4115,1,20,1,1,3,2),_ArrisRouterWiFiChannel_Type())
arrisRouterWiFiChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFiChannel.setStatus(_A)
class _ArrisRouterWiFiMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,0,1,4,6,7,9)));namedValues=NamedValues(*((_N,-1),('mixBG',0),('bOnly',1),('gOnly',4),('nOnly',6),('mixGN',7),('mixBGN',9)))
_ArrisRouterWiFiMode_Type.__name__=_D
_ArrisRouterWiFiMode_Object=MibScalar
arrisRouterWiFiMode=_ArrisRouterWiFiMode_Object((1,3,6,1,4,1,4115,1,20,1,1,3,3),_ArrisRouterWiFiMode_Type())
arrisRouterWiFiMode.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFiMode.setStatus(_A)
class _ArrisRouterWiFiBGProtect_Type(TruthValue):defaultValue=2
_ArrisRouterWiFiBGProtect_Type.__name__=_F
_ArrisRouterWiFiBGProtect_Object=MibScalar
arrisRouterWiFiBGProtect=_ArrisRouterWiFiBGProtect_Object((1,3,6,1,4,1,4115,1,20,1,1,3,4),_ArrisRouterWiFiBGProtect_Type())
arrisRouterWiFiBGProtect.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFiBGProtect.setStatus(_A)
class _ArrisRouterWiFiBeaconInterval_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ArrisRouterWiFiBeaconInterval_Type.__name__=_H
_ArrisRouterWiFiBeaconInterval_Object=MibScalar
arrisRouterWiFiBeaconInterval=_ArrisRouterWiFiBeaconInterval_Object((1,3,6,1,4,1,4115,1,20,1,1,3,5),_ArrisRouterWiFiBeaconInterval_Type())
arrisRouterWiFiBeaconInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFiBeaconInterval.setStatus(_A)
if mibBuilder.loadTexts:arrisRouterWiFiBeaconInterval.setUnits(_P)
class _ArrisRouterWiFiDTIMInterval_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_ArrisRouterWiFiDTIMInterval_Type.__name__=_H
_ArrisRouterWiFiDTIMInterval_Object=MibScalar
arrisRouterWiFiDTIMInterval=_ArrisRouterWiFiDTIMInterval_Object((1,3,6,1,4,1,4115,1,20,1,1,3,6),_ArrisRouterWiFiDTIMInterval_Type())
arrisRouterWiFiDTIMInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFiDTIMInterval.setStatus(_A)
if mibBuilder.loadTexts:arrisRouterWiFiDTIMInterval.setUnits(_P)
class _ArrisRouterWiFiTxPreamble_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,0,1)));namedValues=NamedValues(*((_N,-1),('long',0),('short',1)))
_ArrisRouterWiFiTxPreamble_Type.__name__=_D
_ArrisRouterWiFiTxPreamble_Object=MibScalar
arrisRouterWiFiTxPreamble=_ArrisRouterWiFiTxPreamble_Object((1,3,6,1,4,1,4115,1,20,1,1,3,7),_ArrisRouterWiFiTxPreamble_Type())
arrisRouterWiFiTxPreamble.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFiTxPreamble.setStatus(_A)
class _ArrisRouterWiFiRTSThreshold_Type(Unsigned32):defaultValue=2347;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2347))
_ArrisRouterWiFiRTSThreshold_Type.__name__=_H
_ArrisRouterWiFiRTSThreshold_Object=MibScalar
arrisRouterWiFiRTSThreshold=_ArrisRouterWiFiRTSThreshold_Object((1,3,6,1,4,1,4115,1,20,1,1,3,8),_ArrisRouterWiFiRTSThreshold_Type())
arrisRouterWiFiRTSThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFiRTSThreshold.setStatus(_A)
if mibBuilder.loadTexts:arrisRouterWiFiRTSThreshold.setUnits(_T)
class _ArrisRouterWiFiFragmentThresh_Type(Unsigned32):defaultValue=2346;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(256,2346))
_ArrisRouterWiFiFragmentThresh_Type.__name__=_H
_ArrisRouterWiFiFragmentThresh_Object=MibScalar
arrisRouterWiFiFragmentThresh=_ArrisRouterWiFiFragmentThresh_Object((1,3,6,1,4,1,4115,1,20,1,1,3,9),_ArrisRouterWiFiFragmentThresh_Type())
arrisRouterWiFiFragmentThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFiFragmentThresh.setStatus(_A)
if mibBuilder.loadTexts:arrisRouterWiFiFragmentThresh.setUnits(_T)
class _ArrisRouterWiFiShortSlot_Type(TruthValue):defaultValue=1
_ArrisRouterWiFiShortSlot_Type.__name__=_F
_ArrisRouterWiFiShortSlot_Object=MibScalar
arrisRouterWiFiShortSlot=_ArrisRouterWiFiShortSlot_Object((1,3,6,1,4,1,4115,1,20,1,1,3,10),_ArrisRouterWiFiShortSlot_Type())
arrisRouterWiFiShortSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFiShortSlot.setStatus(_A)
class _ArrisRouterWiFiFrameBurst_Type(TruthValue):defaultValue=1
_ArrisRouterWiFiFrameBurst_Type.__name__=_F
_ArrisRouterWiFiFrameBurst_Object=MibScalar
arrisRouterWiFiFrameBurst=_ArrisRouterWiFiFrameBurst_Object((1,3,6,1,4,1,4115,1,20,1,1,3,11),_ArrisRouterWiFiFrameBurst_Type())
arrisRouterWiFiFrameBurst.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFiFrameBurst.setStatus(_A)
class _ArrisRouterWiFiEnableRadio_Type(TruthValue):defaultValue=1
_ArrisRouterWiFiEnableRadio_Type.__name__=_F
_ArrisRouterWiFiEnableRadio_Object=MibScalar
arrisRouterWiFiEnableRadio=_ArrisRouterWiFiEnableRadio_Object((1,3,6,1,4,1,4115,1,20,1,1,3,12),_ArrisRouterWiFiEnableRadio_Type())
arrisRouterWiFiEnableRadio.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFiEnableRadio.setStatus(_A)
class _ArrisRouterWiFiShortRetryLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_ArrisRouterWiFiShortRetryLimit_Type.__name__=_D
_ArrisRouterWiFiShortRetryLimit_Object=MibScalar
arrisRouterWiFiShortRetryLimit=_ArrisRouterWiFiShortRetryLimit_Object((1,3,6,1,4,1,4115,1,20,1,1,3,14),_ArrisRouterWiFiShortRetryLimit_Type())
arrisRouterWiFiShortRetryLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFiShortRetryLimit.setStatus(_A)
class _ArrisRouterWiFiLongRetryLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_ArrisRouterWiFiLongRetryLimit_Type.__name__=_D
_ArrisRouterWiFiLongRetryLimit_Object=MibScalar
arrisRouterWiFiLongRetryLimit=_ArrisRouterWiFiLongRetryLimit_Object((1,3,6,1,4,1,4115,1,20,1,1,3,15),_ArrisRouterWiFiLongRetryLimit_Type())
arrisRouterWiFiLongRetryLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFiLongRetryLimit.setStatus(_A)
class _ArrisRouterWiFiOutputPower_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(12,25,50,75,100)));namedValues=NamedValues(*((_A8,12),(_A9,25),(_AA,50),(_AB,75),(_AC,100)))
_ArrisRouterWiFiOutputPower_Type.__name__=_D
_ArrisRouterWiFiOutputPower_Object=MibScalar
arrisRouterWiFiOutputPower=_ArrisRouterWiFiOutputPower_Object((1,3,6,1,4,1,4115,1,20,1,1,3,16),_ArrisRouterWiFiOutputPower_Type())
arrisRouterWiFiOutputPower.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFiOutputPower.setStatus(_A)
_ArrisRouterWiFi80211NSettings_ObjectIdentity=ObjectIdentity
arrisRouterWiFi80211NSettings=_ArrisRouterWiFi80211NSettings_ObjectIdentity((1,3,6,1,4,1,4115,1,20,1,1,3,21))
class _ArrisRouterWiFi80211NBand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('band24G',1),('band5G',2)))
_ArrisRouterWiFi80211NBand_Type.__name__=_D
_ArrisRouterWiFi80211NBand_Object=MibScalar
arrisRouterWiFi80211NBand=_ArrisRouterWiFi80211NBand_Object((1,3,6,1,4,1,4115,1,20,1,1,3,21,1),_ArrisRouterWiFi80211NBand_Type())
arrisRouterWiFi80211NBand.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFi80211NBand.setStatus(_A)
class _ArrisRouterWiFiHTMCS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25)));namedValues=NamedValues(*((_R,0),('legacy',1),('mcs0',2),('mcs1',3),('mcs2',4),('mcs3',5),('mcs4',6),('mcs5',7),('mcs6',8),('mcs7',9),('mcs8',10),('mcs9',11),('mcs10',12),('mcs11',13),('mcs12',14),('mcs13',15),('mcs14',16),('mcs15',17),('mcs16',18),('mcs17',19),('mcs18',20),('mcs19',21),('mcs20',22),('mcs21',23),('mcs22',24),('mcs23',25)))
_ArrisRouterWiFiHTMCS_Type.__name__=_D
_ArrisRouterWiFiHTMCS_Object=MibScalar
arrisRouterWiFiHTMCS=_ArrisRouterWiFiHTMCS_Object((1,3,6,1,4,1,4115,1,20,1,1,3,21,2),_ArrisRouterWiFiHTMCS_Type())
arrisRouterWiFiHTMCS.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFiHTMCS.setStatus(_A)
class _ArrisRouterWiFiChannelBW_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,0,1,2)));namedValues=NamedValues(*((_N,-1),(_AD,0),('width40MHz',1),(_AE,2)))
_ArrisRouterWiFiChannelBW_Type.__name__=_D
_ArrisRouterWiFiChannelBW_Object=MibScalar
arrisRouterWiFiChannelBW=_ArrisRouterWiFiChannelBW_Object((1,3,6,1,4,1,4115,1,20,1,1,3,21,3),_ArrisRouterWiFiChannelBW_Type())
arrisRouterWiFiChannelBW.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFiChannelBW.setStatus(_A)
class _ArrisRouterWiFi80211NSideBand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,1,2)));namedValues=NamedValues(*((_N,-1),('upper',1),('lower',2)))
_ArrisRouterWiFi80211NSideBand_Type.__name__=_D
_ArrisRouterWiFi80211NSideBand_Object=MibScalar
arrisRouterWiFi80211NSideBand=_ArrisRouterWiFi80211NSideBand_Object((1,3,6,1,4,1,4115,1,20,1,1,3,21,4),_ArrisRouterWiFi80211NSideBand_Type())
arrisRouterWiFi80211NSideBand.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFi80211NSideBand.setStatus(_A)
class _ArrisRouterWiFiHTMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('mixed',0),(_AF,1)))
_ArrisRouterWiFiHTMode_Type.__name__=_D
_ArrisRouterWiFiHTMode_Object=MibScalar
arrisRouterWiFiHTMode=_ArrisRouterWiFiHTMode_Object((1,3,6,1,4,1,4115,1,20,1,1,3,21,5),_ArrisRouterWiFiHTMode_Type())
arrisRouterWiFiHTMode.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFiHTMode.setStatus(_A)
class _ArrisRouterWiFiGuardInterval_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('gi400',0),('gi800',1),(_R,2)))
_ArrisRouterWiFiGuardInterval_Type.__name__=_D
_ArrisRouterWiFiGuardInterval_Object=MibScalar
arrisRouterWiFiGuardInterval=_ArrisRouterWiFiGuardInterval_Object((1,3,6,1,4,1,4115,1,20,1,1,3,21,6),_ArrisRouterWiFiGuardInterval_Type())
arrisRouterWiFiGuardInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFiGuardInterval.setStatus(_A)
class _ArrisRouterWiFiDeclinePeerBA_Type(TruthValue):defaultValue=2
_ArrisRouterWiFiDeclinePeerBA_Type.__name__=_F
_ArrisRouterWiFiDeclinePeerBA_Object=MibScalar
arrisRouterWiFiDeclinePeerBA=_ArrisRouterWiFiDeclinePeerBA_Object((1,3,6,1,4,1,4115,1,20,1,1,3,21,8),_ArrisRouterWiFiDeclinePeerBA_Type())
arrisRouterWiFiDeclinePeerBA.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFiDeclinePeerBA.setStatus(_A)
class _ArrisRouterWiFiBlockAck_Type(TruthValue):defaultValue=2
_ArrisRouterWiFiBlockAck_Type.__name__=_F
_ArrisRouterWiFiBlockAck_Object=MibScalar
arrisRouterWiFiBlockAck=_ArrisRouterWiFiBlockAck_Object((1,3,6,1,4,1,4115,1,20,1,1,3,21,9),_ArrisRouterWiFiBlockAck_Type())
arrisRouterWiFiBlockAck.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFiBlockAck.setStatus(_A)
class _ArrisRouterWiFiNProtection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('off',0),(_R,1)))
_ArrisRouterWiFiNProtection_Type.__name__=_D
_ArrisRouterWiFiNProtection_Object=MibScalar
arrisRouterWiFiNProtection=_ArrisRouterWiFiNProtection_Object((1,3,6,1,4,1,4115,1,20,1,1,3,21,10),_ArrisRouterWiFiNProtection_Type())
arrisRouterWiFiNProtection.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFiNProtection.setStatus(_A)
class _ArrisRouterWiFiAllow40MHzOnlyOperation_Type(TruthValue):defaultValue=2
_ArrisRouterWiFiAllow40MHzOnlyOperation_Type.__name__=_F
_ArrisRouterWiFiAllow40MHzOnlyOperation_Object=MibScalar
arrisRouterWiFiAllow40MHzOnlyOperation=_ArrisRouterWiFiAllow40MHzOnlyOperation_Object((1,3,6,1,4,1,4115,1,20,1,1,3,21,11),_ArrisRouterWiFiAllow40MHzOnlyOperation_Type())
arrisRouterWiFiAllow40MHzOnlyOperation.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFiAllow40MHzOnlyOperation.setStatus(_A)
_ArrisRouterBSSTable_Object=MibTable
arrisRouterBSSTable=_ArrisRouterBSSTable_Object((1,3,6,1,4,1,4115,1,20,1,1,3,22))
if mibBuilder.loadTexts:arrisRouterBSSTable.setStatus(_A)
_ArrisRouterBSSEntry_Object=MibTableRow
arrisRouterBSSEntry=_ArrisRouterBSSEntry_Object((1,3,6,1,4,1,4115,1,20,1,1,3,22,1))
arrisRouterBSSEntry.setIndexNames((0,_K,_L))
if mibBuilder.loadTexts:arrisRouterBSSEntry.setStatus(_A)
_ArrisRouterBssID_Type=PhysAddress
_ArrisRouterBssID_Object=MibTableColumn
arrisRouterBssID=_ArrisRouterBssID_Object((1,3,6,1,4,1,4115,1,20,1,1,3,22,1,1),_ArrisRouterBssID_Type())
arrisRouterBssID.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterBssID.setStatus(_A)
class _ArrisRouterBssSSID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ArrisRouterBssSSID_Type.__name__=_G
_ArrisRouterBssSSID_Object=MibTableColumn
arrisRouterBssSSID=_ArrisRouterBssSSID_Object((1,3,6,1,4,1,4115,1,20,1,1,3,22,1,2),_ArrisRouterBssSSID_Type())
arrisRouterBssSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterBssSSID.setStatus(_A)
class _ArrisRouterBssActive_Type(TruthValue):defaultValue=2
_ArrisRouterBssActive_Type.__name__=_F
_ArrisRouterBssActive_Object=MibTableColumn
arrisRouterBssActive=_ArrisRouterBssActive_Object((1,3,6,1,4,1,4115,1,20,1,1,3,22,1,3),_ArrisRouterBssActive_Type())
arrisRouterBssActive.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterBssActive.setStatus(_A)
class _ArrisRouterBssSSIDBroadcast_Type(TruthValue):defaultValue=1
_ArrisRouterBssSSIDBroadcast_Type.__name__=_F
_ArrisRouterBssSSIDBroadcast_Object=MibTableColumn
arrisRouterBssSSIDBroadcast=_ArrisRouterBssSSIDBroadcast_Object((1,3,6,1,4,1,4115,1,20,1,1,3,22,1,4),_ArrisRouterBssSSIDBroadcast_Type())
arrisRouterBssSSIDBroadcast.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterBssSSIDBroadcast.setStatus(_A)
class _ArrisRouterBssSecurityMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_O,0),('wep',1),('wpaPsk',2),('wpa2Psk',3),(_AG,4),(_AH,5),('wepEnterprise',6),('wpaWpa2Psk',7),(_AI,8)))
_ArrisRouterBssSecurityMode_Type.__name__=_D
_ArrisRouterBssSecurityMode_Object=MibTableColumn
arrisRouterBssSecurityMode=_ArrisRouterBssSecurityMode_Object((1,3,6,1,4,1,4115,1,20,1,1,3,22,1,5),_ArrisRouterBssSecurityMode_Type())
arrisRouterBssSecurityMode.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterBssSecurityMode.setStatus(_A)
class _ArrisRouterBssAccessMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('allowAny',1),('allowList',2),('denyList',3)))
_ArrisRouterBssAccessMode_Type.__name__=_D
_ArrisRouterBssAccessMode_Object=MibTableColumn
arrisRouterBssAccessMode=_ArrisRouterBssAccessMode_Object((1,3,6,1,4,1,4115,1,20,1,1,3,22,1,6),_ArrisRouterBssAccessMode_Type())
arrisRouterBssAccessMode.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterBssAccessMode.setStatus(_A)
class _ArrisRouterBssNetworkIsolate_Type(TruthValue):defaultValue=2
_ArrisRouterBssNetworkIsolate_Type.__name__=_F
_ArrisRouterBssNetworkIsolate_Object=MibTableColumn
arrisRouterBssNetworkIsolate=_ArrisRouterBssNetworkIsolate_Object((1,3,6,1,4,1,4115,1,20,1,1,3,22,1,7),_ArrisRouterBssNetworkIsolate_Type())
arrisRouterBssNetworkIsolate.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterBssNetworkIsolate.setStatus(_A)
_ArrisRouterBssMACAccessCount_Type=Unsigned32
_ArrisRouterBssMACAccessCount_Object=MibTableColumn
arrisRouterBssMACAccessCount=_ArrisRouterBssMACAccessCount_Object((1,3,6,1,4,1,4115,1,20,1,1,3,22,1,8),_ArrisRouterBssMACAccessCount_Type())
arrisRouterBssMACAccessCount.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterBssMACAccessCount.setStatus(_A)
class _ArrisRouterBssMACAccessClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('clear',1))
_ArrisRouterBssMACAccessClear_Type.__name__=_D
_ArrisRouterBssMACAccessClear_Object=MibTableColumn
arrisRouterBssMACAccessClear=_ArrisRouterBssMACAccessClear_Object((1,3,6,1,4,1,4115,1,20,1,1,3,22,1,9),_ArrisRouterBssMACAccessClear_Type())
arrisRouterBssMACAccessClear.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterBssMACAccessClear.setStatus(_A)
_ArrisRouterBSSArpAuditInterval_Type=Unsigned32
_ArrisRouterBSSArpAuditInterval_Object=MibTableColumn
arrisRouterBSSArpAuditInterval=_ArrisRouterBSSArpAuditInterval_Object((1,3,6,1,4,1,4115,1,20,1,1,3,22,1,10),_ArrisRouterBSSArpAuditInterval_Type())
arrisRouterBSSArpAuditInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterBSSArpAuditInterval.setStatus(_A)
if mibBuilder.loadTexts:arrisRouterBSSArpAuditInterval.setUnits(_M)
class _ArrisRouterBssMaxWifiClients_Type(Integer32):defaultValue=0
_ArrisRouterBssMaxWifiClients_Type.__name__=_D
_ArrisRouterBssMaxWifiClients_Object=MibTableColumn
arrisRouterBssMaxWifiClients=_ArrisRouterBssMaxWifiClients_Object((1,3,6,1,4,1,4115,1,20,1,1,3,22,1,11),_ArrisRouterBssMaxWifiClients_Type())
arrisRouterBssMaxWifiClients.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterBssMaxWifiClients.setStatus(_A)
class _ArrisRouterBssWmmEnable_Type(TruthValue):defaultValue=1
_ArrisRouterBssWmmEnable_Type.__name__=_F
_ArrisRouterBssWmmEnable_Object=MibTableColumn
arrisRouterBssWmmEnable=_ArrisRouterBssWmmEnable_Object((1,3,6,1,4,1,4115,1,20,1,1,3,22,1,12),_ArrisRouterBssWmmEnable_Type())
arrisRouterBssWmmEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterBssWmmEnable.setStatus(_A)
class _ArrisRouterBssWmmAPSD_Type(TruthValue):defaultValue=1
_ArrisRouterBssWmmAPSD_Type.__name__=_F
_ArrisRouterBssWmmAPSD_Object=MibTableColumn
arrisRouterBssWmmAPSD=_ArrisRouterBssWmmAPSD_Object((1,3,6,1,4,1,4115,1,20,1,1,3,22,1,13),_ArrisRouterBssWmmAPSD_Type())
arrisRouterBssWmmAPSD.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterBssWmmAPSD.setStatus(_A)
class _ArrisRouterBssActiveTimeout_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_ArrisRouterBssActiveTimeout_Type.__name__=_U
_ArrisRouterBssActiveTimeout_Object=MibTableColumn
arrisRouterBssActiveTimeout=_ArrisRouterBssActiveTimeout_Object((1,3,6,1,4,1,4115,1,20,1,1,3,22,1,14),_ArrisRouterBssActiveTimeout_Type())
arrisRouterBssActiveTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterBssActiveTimeout.setStatus(_A)
class _ArrisRouterDefaultBssSSID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ArrisRouterDefaultBssSSID_Type.__name__=_G
_ArrisRouterDefaultBssSSID_Object=MibTableColumn
arrisRouterDefaultBssSSID=_ArrisRouterDefaultBssSSID_Object((1,3,6,1,4,1,4115,1,20,1,1,3,22,1,15),_ArrisRouterDefaultBssSSID_Type())
arrisRouterDefaultBssSSID.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterDefaultBssSSID.setStatus(_A)
class _ArrisRouterBssStaSteeringEnable_Type(TruthValue):defaultValue=2
_ArrisRouterBssStaSteeringEnable_Type.__name__=_F
_ArrisRouterBssStaSteeringEnable_Object=MibTableColumn
arrisRouterBssStaSteeringEnable=_ArrisRouterBssStaSteeringEnable_Object((1,3,6,1,4,1,4115,1,20,1,1,3,22,1,16),_ArrisRouterBssStaSteeringEnable_Type())
arrisRouterBssStaSteeringEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterBssStaSteeringEnable.setStatus(_A)
_ArrisRouterWEPTable_Object=MibTable
arrisRouterWEPTable=_ArrisRouterWEPTable_Object((1,3,6,1,4,1,4115,1,20,1,1,3,23))
if mibBuilder.loadTexts:arrisRouterWEPTable.setStatus(_A)
_ArrisRouterWEPEntry_Object=MibTableRow
arrisRouterWEPEntry=_ArrisRouterWEPEntry_Object((1,3,6,1,4,1,4115,1,20,1,1,3,23,1))
arrisRouterWEPEntry.setIndexNames((0,_K,_L))
if mibBuilder.loadTexts:arrisRouterWEPEntry.setStatus(_A)
_ArrisRouterWEPCurrentKey_Type=Unsigned32
_ArrisRouterWEPCurrentKey_Object=MibTableColumn
arrisRouterWEPCurrentKey=_ArrisRouterWEPCurrentKey_Object((1,3,6,1,4,1,4115,1,20,1,1,3,23,1,1),_ArrisRouterWEPCurrentKey_Type())
arrisRouterWEPCurrentKey.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWEPCurrentKey.setStatus(_A)
class _ArrisRouterWEPEncryptionMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('wep64',1),('wep128',2)))
_ArrisRouterWEPEncryptionMode_Type.__name__=_D
_ArrisRouterWEPEncryptionMode_Object=MibTableColumn
arrisRouterWEPEncryptionMode=_ArrisRouterWEPEncryptionMode_Object((1,3,6,1,4,1,4115,1,20,1,1,3,23,1,2),_ArrisRouterWEPEncryptionMode_Type())
arrisRouterWEPEncryptionMode.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWEPEncryptionMode.setStatus(_A)
_ArrisRouterWEP64BitKeyTable_Object=MibTable
arrisRouterWEP64BitKeyTable=_ArrisRouterWEP64BitKeyTable_Object((1,3,6,1,4,1,4115,1,20,1,1,3,24))
if mibBuilder.loadTexts:arrisRouterWEP64BitKeyTable.setStatus(_A)
_ArrisRouterWEP64BitKeyEntry_Object=MibTableRow
arrisRouterWEP64BitKeyEntry=_ArrisRouterWEP64BitKeyEntry_Object((1,3,6,1,4,1,4115,1,20,1,1,3,24,1))
arrisRouterWEP64BitKeyEntry.setIndexNames((0,_K,_L),(0,_I,_AJ))
if mibBuilder.loadTexts:arrisRouterWEP64BitKeyEntry.setStatus(_A)
class _ArrisRouterWEP64BitKeyIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_ArrisRouterWEP64BitKeyIndex_Type.__name__=_D
_ArrisRouterWEP64BitKeyIndex_Object=MibTableColumn
arrisRouterWEP64BitKeyIndex=_ArrisRouterWEP64BitKeyIndex_Object((1,3,6,1,4,1,4115,1,20,1,1,3,24,1,1),_ArrisRouterWEP64BitKeyIndex_Type())
arrisRouterWEP64BitKeyIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:arrisRouterWEP64BitKeyIndex.setStatus(_A)
_ArrisRouterWEP64BitKeyValue_Type=DisplayString
_ArrisRouterWEP64BitKeyValue_Object=MibTableColumn
arrisRouterWEP64BitKeyValue=_ArrisRouterWEP64BitKeyValue_Object((1,3,6,1,4,1,4115,1,20,1,1,3,24,1,2),_ArrisRouterWEP64BitKeyValue_Type())
arrisRouterWEP64BitKeyValue.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterWEP64BitKeyValue.setStatus(_A)
_ArrisRouterWEP64BitKeyStatus_Type=RowStatus
_ArrisRouterWEP64BitKeyStatus_Object=MibTableColumn
arrisRouterWEP64BitKeyStatus=_ArrisRouterWEP64BitKeyStatus_Object((1,3,6,1,4,1,4115,1,20,1,1,3,24,1,3),_ArrisRouterWEP64BitKeyStatus_Type())
arrisRouterWEP64BitKeyStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterWEP64BitKeyStatus.setStatus(_A)
_ArrisRouterWEP128BitKeyTable_Object=MibTable
arrisRouterWEP128BitKeyTable=_ArrisRouterWEP128BitKeyTable_Object((1,3,6,1,4,1,4115,1,20,1,1,3,25))
if mibBuilder.loadTexts:arrisRouterWEP128BitKeyTable.setStatus(_A)
_ArrisRouterWEP128BitKeyEntry_Object=MibTableRow
arrisRouterWEP128BitKeyEntry=_ArrisRouterWEP128BitKeyEntry_Object((1,3,6,1,4,1,4115,1,20,1,1,3,25,1))
arrisRouterWEP128BitKeyEntry.setIndexNames((0,_K,_L),(0,_I,_AK))
if mibBuilder.loadTexts:arrisRouterWEP128BitKeyEntry.setStatus(_A)
class _ArrisRouterWEP128BitKeyIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_ArrisRouterWEP128BitKeyIndex_Type.__name__=_D
_ArrisRouterWEP128BitKeyIndex_Object=MibTableColumn
arrisRouterWEP128BitKeyIndex=_ArrisRouterWEP128BitKeyIndex_Object((1,3,6,1,4,1,4115,1,20,1,1,3,25,1,1),_ArrisRouterWEP128BitKeyIndex_Type())
arrisRouterWEP128BitKeyIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:arrisRouterWEP128BitKeyIndex.setStatus(_A)
_ArrisRouterWEP128BitKeyValue_Type=DisplayString
_ArrisRouterWEP128BitKeyValue_Object=MibTableColumn
arrisRouterWEP128BitKeyValue=_ArrisRouterWEP128BitKeyValue_Object((1,3,6,1,4,1,4115,1,20,1,1,3,25,1,2),_ArrisRouterWEP128BitKeyValue_Type())
arrisRouterWEP128BitKeyValue.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterWEP128BitKeyValue.setStatus(_A)
_ArrisRouterWEP128BitKeyStatus_Type=RowStatus
_ArrisRouterWEP128BitKeyStatus_Object=MibTableColumn
arrisRouterWEP128BitKeyStatus=_ArrisRouterWEP128BitKeyStatus_Object((1,3,6,1,4,1,4115,1,20,1,1,3,25,1,3),_ArrisRouterWEP128BitKeyStatus_Type())
arrisRouterWEP128BitKeyStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterWEP128BitKeyStatus.setStatus(_A)
_ArrisRouterWPATable_Object=MibTable
arrisRouterWPATable=_ArrisRouterWPATable_Object((1,3,6,1,4,1,4115,1,20,1,1,3,26))
if mibBuilder.loadTexts:arrisRouterWPATable.setStatus(_A)
_ArrisRouterWPAEntry_Object=MibTableRow
arrisRouterWPAEntry=_ArrisRouterWPAEntry_Object((1,3,6,1,4,1,4115,1,20,1,1,3,26,1))
arrisRouterWPAEntry.setIndexNames((0,_K,_L))
if mibBuilder.loadTexts:arrisRouterWPAEntry.setStatus(_A)
class _ArrisRouterWPAAlgorithm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('tkip',1),('aes',2),('tkipPlusAes',3)))
_ArrisRouterWPAAlgorithm_Type.__name__=_D
_ArrisRouterWPAAlgorithm_Object=MibTableColumn
arrisRouterWPAAlgorithm=_ArrisRouterWPAAlgorithm_Object((1,3,6,1,4,1,4115,1,20,1,1,3,26,1,1),_ArrisRouterWPAAlgorithm_Type())
arrisRouterWPAAlgorithm.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWPAAlgorithm.setStatus(_A)
class _ArrisRouterWPAPreSharedKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,64))
_ArrisRouterWPAPreSharedKey_Type.__name__=_U
_ArrisRouterWPAPreSharedKey_Object=MibTableColumn
arrisRouterWPAPreSharedKey=_ArrisRouterWPAPreSharedKey_Object((1,3,6,1,4,1,4115,1,20,1,1,3,26,1,2),_ArrisRouterWPAPreSharedKey_Type())
arrisRouterWPAPreSharedKey.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWPAPreSharedKey.setStatus(_A)
_ArrisRouterWPAReAuthInterval_Type=Unsigned32
_ArrisRouterWPAReAuthInterval_Object=MibTableColumn
arrisRouterWPAReAuthInterval=_ArrisRouterWPAReAuthInterval_Object((1,3,6,1,4,1,4115,1,20,1,1,3,26,1,4),_ArrisRouterWPAReAuthInterval_Type())
arrisRouterWPAReAuthInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWPAReAuthInterval.setStatus(_A)
if mibBuilder.loadTexts:arrisRouterWPAReAuthInterval.setUnits(_M)
class _ArrisRouterWPAPreAuthEnable_Type(TruthValue):defaultValue=2
_ArrisRouterWPAPreAuthEnable_Type.__name__=_F
_ArrisRouterWPAPreAuthEnable_Object=MibTableColumn
arrisRouterWPAPreAuthEnable=_ArrisRouterWPAPreAuthEnable_Object((1,3,6,1,4,1,4115,1,20,1,1,3,26,1,5),_ArrisRouterWPAPreAuthEnable_Type())
arrisRouterWPAPreAuthEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWPAPreAuthEnable.setStatus(_A)
class _ArrisRouterDefaultWPAPreSharedKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,64))
_ArrisRouterDefaultWPAPreSharedKey_Type.__name__=_U
_ArrisRouterDefaultWPAPreSharedKey_Object=MibTableColumn
arrisRouterDefaultWPAPreSharedKey=_ArrisRouterDefaultWPAPreSharedKey_Object((1,3,6,1,4,1,4115,1,20,1,1,3,26,1,6),_ArrisRouterDefaultWPAPreSharedKey_Type())
arrisRouterDefaultWPAPreSharedKey.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterDefaultWPAPreSharedKey.setStatus(_A)
_ArrisRouterRadiusTable_Object=MibTable
arrisRouterRadiusTable=_ArrisRouterRadiusTable_Object((1,3,6,1,4,1,4115,1,20,1,1,3,27))
if mibBuilder.loadTexts:arrisRouterRadiusTable.setStatus(_A)
_ArrisRouterRadiusEntry_Object=MibTableRow
arrisRouterRadiusEntry=_ArrisRouterRadiusEntry_Object((1,3,6,1,4,1,4115,1,20,1,1,3,27,1))
arrisRouterRadiusEntry.setIndexNames((0,_K,_L))
if mibBuilder.loadTexts:arrisRouterRadiusEntry.setStatus(_A)
_ArrisRouterRadiusAddressType_Type=InetAddressType
_ArrisRouterRadiusAddressType_Object=MibTableColumn
arrisRouterRadiusAddressType=_ArrisRouterRadiusAddressType_Object((1,3,6,1,4,1,4115,1,20,1,1,3,27,1,1),_ArrisRouterRadiusAddressType_Type())
arrisRouterRadiusAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterRadiusAddressType.setStatus(_A)
_ArrisRouterRadiusAddress_Type=InetAddress
_ArrisRouterRadiusAddress_Object=MibTableColumn
arrisRouterRadiusAddress=_ArrisRouterRadiusAddress_Object((1,3,6,1,4,1,4115,1,20,1,1,3,27,1,2),_ArrisRouterRadiusAddress_Type())
arrisRouterRadiusAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterRadiusAddress.setStatus(_A)
_ArrisRouterRadiusPort_Type=Unsigned32
_ArrisRouterRadiusPort_Object=MibTableColumn
arrisRouterRadiusPort=_ArrisRouterRadiusPort_Object((1,3,6,1,4,1,4115,1,20,1,1,3,27,1,3),_ArrisRouterRadiusPort_Type())
arrisRouterRadiusPort.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterRadiusPort.setStatus(_A)
class _ArrisRouterRadiusKey_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_ArrisRouterRadiusKey_Type.__name__=_G
_ArrisRouterRadiusKey_Object=MibTableColumn
arrisRouterRadiusKey=_ArrisRouterRadiusKey_Object((1,3,6,1,4,1,4115,1,20,1,1,3,27,1,4),_ArrisRouterRadiusKey_Type())
arrisRouterRadiusKey.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterRadiusKey.setStatus(_A)
_ArrisRouterRadiusReAuthInterval_Type=Unsigned32
_ArrisRouterRadiusReAuthInterval_Object=MibTableColumn
arrisRouterRadiusReAuthInterval=_ArrisRouterRadiusReAuthInterval_Object((1,3,6,1,4,1,4115,1,20,1,1,3,27,1,5),_ArrisRouterRadiusReAuthInterval_Type())
arrisRouterRadiusReAuthInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterRadiusReAuthInterval.setStatus(_A)
if mibBuilder.loadTexts:arrisRouterRadiusReAuthInterval.setUnits(_M)
_ArrisRouterMACAccessTable_Object=MibTable
arrisRouterMACAccessTable=_ArrisRouterMACAccessTable_Object((1,3,6,1,4,1,4115,1,20,1,1,3,28))
if mibBuilder.loadTexts:arrisRouterMACAccessTable.setStatus(_A)
_ArrisRouterMACAccessEntry_Object=MibTableRow
arrisRouterMACAccessEntry=_ArrisRouterMACAccessEntry_Object((1,3,6,1,4,1,4115,1,20,1,1,3,28,1))
arrisRouterMACAccessEntry.setIndexNames((0,_K,_L),(0,_I,_AL))
if mibBuilder.loadTexts:arrisRouterMACAccessEntry.setStatus(_A)
class _ArrisRouterMACAccessIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_ArrisRouterMACAccessIndex_Type.__name__=_D
_ArrisRouterMACAccessIndex_Object=MibTableColumn
arrisRouterMACAccessIndex=_ArrisRouterMACAccessIndex_Object((1,3,6,1,4,1,4115,1,20,1,1,3,28,1,1),_ArrisRouterMACAccessIndex_Type())
arrisRouterMACAccessIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:arrisRouterMACAccessIndex.setStatus(_A)
_ArrisRouterMACAccessAddr_Type=MacAddress
_ArrisRouterMACAccessAddr_Object=MibTableColumn
arrisRouterMACAccessAddr=_ArrisRouterMACAccessAddr_Object((1,3,6,1,4,1,4115,1,20,1,1,3,28,1,2),_ArrisRouterMACAccessAddr_Type())
arrisRouterMACAccessAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterMACAccessAddr.setStatus(_A)
_ArrisRouterMACAccessStatus_Type=RowStatus
_ArrisRouterMACAccessStatus_Object=MibTableColumn
arrisRouterMACAccessStatus=_ArrisRouterMACAccessStatus_Object((1,3,6,1,4,1,4115,1,20,1,1,3,28,1,3),_ArrisRouterMACAccessStatus_Type())
arrisRouterMACAccessStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterMACAccessStatus.setStatus(_A)
_ArrisRouterMACAccessDeviceName_Type=DisplayString
_ArrisRouterMACAccessDeviceName_Object=MibTableColumn
arrisRouterMACAccessDeviceName=_ArrisRouterMACAccessDeviceName_Object((1,3,6,1,4,1,4115,1,20,1,1,3,28,1,4),_ArrisRouterMACAccessDeviceName_Type())
arrisRouterMACAccessDeviceName.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterMACAccessDeviceName.setStatus(_A)
_ArrisRouterWMMCfg_ObjectIdentity=ObjectIdentity
arrisRouterWMMCfg=_ArrisRouterWMMCfg_ObjectIdentity((1,3,6,1,4,1,4115,1,20,1,1,3,29))
class _ArrisRouterWMMEnable_Type(TruthValue):defaultValue=1
_ArrisRouterWMMEnable_Type.__name__=_F
_ArrisRouterWMMEnable_Object=MibScalar
arrisRouterWMMEnable=_ArrisRouterWMMEnable_Object((1,3,6,1,4,1,4115,1,20,1,1,3,29,1),_ArrisRouterWMMEnable_Type())
arrisRouterWMMEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWMMEnable.setStatus(_A)
class _ArrisRouterWMMNoAck_Type(TruthValue):defaultValue=2
_ArrisRouterWMMNoAck_Type.__name__=_F
_ArrisRouterWMMNoAck_Object=MibScalar
arrisRouterWMMNoAck=_ArrisRouterWMMNoAck_Object((1,3,6,1,4,1,4115,1,20,1,1,3,29,2),_ArrisRouterWMMNoAck_Type())
arrisRouterWMMNoAck.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWMMNoAck.setStatus(_A)
class _ArrisRouterWMMAPSD_Type(TruthValue):defaultValue=1
_ArrisRouterWMMAPSD_Type.__name__=_F
_ArrisRouterWMMAPSD_Object=MibScalar
arrisRouterWMMAPSD=_ArrisRouterWMMAPSD_Object((1,3,6,1,4,1,4115,1,20,1,1,3,29,3),_ArrisRouterWMMAPSD_Type())
arrisRouterWMMAPSD.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWMMAPSD.setStatus(_A)
_ArrisRouterWMMEDCAAPTable_Object=MibTable
arrisRouterWMMEDCAAPTable=_ArrisRouterWMMEDCAAPTable_Object((1,3,6,1,4,1,4115,1,20,1,1,3,29,4))
if mibBuilder.loadTexts:arrisRouterWMMEDCAAPTable.setStatus(_A)
_ArrisRouterWMMEDCAAPEntry_Object=MibTableRow
arrisRouterWMMEDCAAPEntry=_ArrisRouterWMMEDCAAPEntry_Object((1,3,6,1,4,1,4115,1,20,1,1,3,29,4,1))
arrisRouterWMMEDCAAPEntry.setIndexNames((0,_I,_AM))
if mibBuilder.loadTexts:arrisRouterWMMEDCAAPEntry.setStatus(_A)
class _ArrisRouterWMMEDCAAPIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_ArrisRouterWMMEDCAAPIndex_Type.__name__=_D
_ArrisRouterWMMEDCAAPIndex_Object=MibTableColumn
arrisRouterWMMEDCAAPIndex=_ArrisRouterWMMEDCAAPIndex_Object((1,3,6,1,4,1,4115,1,20,1,1,3,29,4,1,1),_ArrisRouterWMMEDCAAPIndex_Type())
arrisRouterWMMEDCAAPIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:arrisRouterWMMEDCAAPIndex.setStatus(_A)
_ArrisRouterWMMEDCAAPCWmin_Type=Unsigned32
_ArrisRouterWMMEDCAAPCWmin_Object=MibTableColumn
arrisRouterWMMEDCAAPCWmin=_ArrisRouterWMMEDCAAPCWmin_Object((1,3,6,1,4,1,4115,1,20,1,1,3,29,4,1,2),_ArrisRouterWMMEDCAAPCWmin_Type())
arrisRouterWMMEDCAAPCWmin.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWMMEDCAAPCWmin.setStatus(_A)
if mibBuilder.loadTexts:arrisRouterWMMEDCAAPCWmin.setUnits(_P)
_ArrisRouterWMMEDCAAPCWmax_Type=Unsigned32
_ArrisRouterWMMEDCAAPCWmax_Object=MibTableColumn
arrisRouterWMMEDCAAPCWmax=_ArrisRouterWMMEDCAAPCWmax_Object((1,3,6,1,4,1,4115,1,20,1,1,3,29,4,1,3),_ArrisRouterWMMEDCAAPCWmax_Type())
arrisRouterWMMEDCAAPCWmax.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWMMEDCAAPCWmax.setStatus(_A)
if mibBuilder.loadTexts:arrisRouterWMMEDCAAPCWmax.setUnits(_P)
_ArrisRouterWMMEDCAAPAIFSN_Type=Unsigned32
_ArrisRouterWMMEDCAAPAIFSN_Object=MibTableColumn
arrisRouterWMMEDCAAPAIFSN=_ArrisRouterWMMEDCAAPAIFSN_Object((1,3,6,1,4,1,4115,1,20,1,1,3,29,4,1,4),_ArrisRouterWMMEDCAAPAIFSN_Type())
arrisRouterWMMEDCAAPAIFSN.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWMMEDCAAPAIFSN.setStatus(_A)
if mibBuilder.loadTexts:arrisRouterWMMEDCAAPAIFSN.setUnits(_P)
class _ArrisRouterWMMEDCAAPTxOpBLimit_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ArrisRouterWMMEDCAAPTxOpBLimit_Type.__name__=_H
_ArrisRouterWMMEDCAAPTxOpBLimit_Object=MibTableColumn
arrisRouterWMMEDCAAPTxOpBLimit=_ArrisRouterWMMEDCAAPTxOpBLimit_Object((1,3,6,1,4,1,4115,1,20,1,1,3,29,4,1,5),_ArrisRouterWMMEDCAAPTxOpBLimit_Type())
arrisRouterWMMEDCAAPTxOpBLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWMMEDCAAPTxOpBLimit.setStatus(_A)
if mibBuilder.loadTexts:arrisRouterWMMEDCAAPTxOpBLimit.setUnits(_Z)
class _ArrisRouterWMMEDCAAPTxOpAGLimit_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ArrisRouterWMMEDCAAPTxOpAGLimit_Type.__name__=_H
_ArrisRouterWMMEDCAAPTxOpAGLimit_Object=MibTableColumn
arrisRouterWMMEDCAAPTxOpAGLimit=_ArrisRouterWMMEDCAAPTxOpAGLimit_Object((1,3,6,1,4,1,4115,1,20,1,1,3,29,4,1,6),_ArrisRouterWMMEDCAAPTxOpAGLimit_Type())
arrisRouterWMMEDCAAPTxOpAGLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWMMEDCAAPTxOpAGLimit.setStatus(_A)
if mibBuilder.loadTexts:arrisRouterWMMEDCAAPTxOpAGLimit.setUnits(_Z)
_ArrisRouterWMMEDCAAPAdmitCont_Type=TruthValue
_ArrisRouterWMMEDCAAPAdmitCont_Object=MibTableColumn
arrisRouterWMMEDCAAPAdmitCont=_ArrisRouterWMMEDCAAPAdmitCont_Object((1,3,6,1,4,1,4115,1,20,1,1,3,29,4,1,7),_ArrisRouterWMMEDCAAPAdmitCont_Type())
arrisRouterWMMEDCAAPAdmitCont.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWMMEDCAAPAdmitCont.setStatus(_A)
_ArrisRouterWMMEDCAAPDiscardOld_Type=TruthValue
_ArrisRouterWMMEDCAAPDiscardOld_Object=MibTableColumn
arrisRouterWMMEDCAAPDiscardOld=_ArrisRouterWMMEDCAAPDiscardOld_Object((1,3,6,1,4,1,4115,1,20,1,1,3,29,4,1,8),_ArrisRouterWMMEDCAAPDiscardOld_Type())
arrisRouterWMMEDCAAPDiscardOld.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWMMEDCAAPDiscardOld.setStatus(_A)
_ArrisRouterWPSCfg_ObjectIdentity=ObjectIdentity
arrisRouterWPSCfg=_ArrisRouterWPSCfg_ObjectIdentity((1,3,6,1,4,1,4115,1,20,1,1,3,30))
class _ArrisRouterWpsMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_O,0),(_Q,1)))
_ArrisRouterWpsMode_Type.__name__=_D
_ArrisRouterWpsMode_Object=MibScalar
arrisRouterWpsMode=_ArrisRouterWpsMode_Object((1,3,6,1,4,1,4115,1,20,1,1,3,30,1),_ArrisRouterWpsMode_Type())
arrisRouterWpsMode.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWpsMode.setStatus(_A)
class _ArrisRouterWpsConfigState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_O,0),(_Q,1)))
_ArrisRouterWpsConfigState_Type.__name__=_D
_ArrisRouterWpsConfigState_Object=MibScalar
arrisRouterWpsConfigState=_ArrisRouterWpsConfigState_Object((1,3,6,1,4,1,4115,1,20,1,1,3,30,2),_ArrisRouterWpsConfigState_Type())
arrisRouterWpsConfigState.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWpsConfigState.setStatus(_A)
class _ArrisRouterWpsDevicePIN_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ArrisRouterWpsDevicePIN_Type.__name__=_G
_ArrisRouterWpsDevicePIN_Object=MibScalar
arrisRouterWpsDevicePIN=_ArrisRouterWpsDevicePIN_Object((1,3,6,1,4,1,4115,1,20,1,1,3,30,3),_ArrisRouterWpsDevicePIN_Type())
arrisRouterWpsDevicePIN.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWpsDevicePIN.setStatus(_A)
class _ArrisRouterWpsDeviceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ArrisRouterWpsDeviceName_Type.__name__=_G
_ArrisRouterWpsDeviceName_Object=MibScalar
arrisRouterWpsDeviceName=_ArrisRouterWpsDeviceName_Object((1,3,6,1,4,1,4115,1,20,1,1,3,30,4),_ArrisRouterWpsDeviceName_Type())
arrisRouterWpsDeviceName.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWpsDeviceName.setStatus(_A)
class _ArrisRouterWpsModelName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ArrisRouterWpsModelName_Type.__name__=_G
_ArrisRouterWpsModelName_Object=MibScalar
arrisRouterWpsModelName=_ArrisRouterWpsModelName_Object((1,3,6,1,4,1,4115,1,20,1,1,3,30,5),_ArrisRouterWpsModelName_Type())
arrisRouterWpsModelName.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWpsModelName.setStatus(_A)
class _ArrisRouterWpsMfg_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ArrisRouterWpsMfg_Type.__name__=_G
_ArrisRouterWpsMfg_Object=MibScalar
arrisRouterWpsMfg=_ArrisRouterWpsMfg_Object((1,3,6,1,4,1,4115,1,20,1,1,3,30,6),_ArrisRouterWpsMfg_Type())
arrisRouterWpsMfg.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWpsMfg.setStatus(_A)
class _ArrisRouterWpsResultStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,0,1,2,3,4,5,6)));namedValues=NamedValues(*((_AN,-1),(_AO,0),(_AP,1),(_AQ,2),(_AR,3),(_AS,4),(_AT,5),(_AU,6)))
_ArrisRouterWpsResultStatus_Type.__name__=_D
_ArrisRouterWpsResultStatus_Object=MibScalar
arrisRouterWpsResultStatus=_ArrisRouterWpsResultStatus_Object((1,3,6,1,4,1,4115,1,20,1,1,3,30,7),_ArrisRouterWpsResultStatus_Type())
arrisRouterWpsResultStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWpsResultStatus.setStatus(_A)
class _ArrisRouterWpsStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,0,1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_AV,-1),(_AW,0),(_AX,1),(_AY,2),(_AZ,3),(_Aa,4),(_Ab,5),(_Ac,6),(_Ad,7),(_Ae,8),(_Af,9),(_Ag,10)))
_ArrisRouterWpsStatus_Type.__name__=_D
_ArrisRouterWpsStatus_Object=MibScalar
arrisRouterWpsStatus=_ArrisRouterWpsStatus_Object((1,3,6,1,4,1,4115,1,20,1,1,3,30,8),_ArrisRouterWpsStatus_Type())
arrisRouterWpsStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWpsStatus.setStatus(_A)
class _ArrisRouterWpsConfigTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_O,0),(_Q,1)))
_ArrisRouterWpsConfigTimeout_Type.__name__=_D
_ArrisRouterWpsConfigTimeout_Object=MibScalar
arrisRouterWpsConfigTimeout=_ArrisRouterWpsConfigTimeout_Object((1,3,6,1,4,1,4115,1,20,1,1,3,30,9),_ArrisRouterWpsConfigTimeout_Type())
arrisRouterWpsConfigTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWpsConfigTimeout.setStatus(_A)
class _ArrisRouterWpsSTAPin_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ArrisRouterWpsSTAPin_Type.__name__=_G
_ArrisRouterWpsSTAPin_Object=MibScalar
arrisRouterWpsSTAPin=_ArrisRouterWpsSTAPin_Object((1,3,6,1,4,1,4115,1,20,1,1,3,30,10),_ArrisRouterWpsSTAPin_Type())
arrisRouterWpsSTAPin.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWpsSTAPin.setStatus(_A)
class _ArrisRouterWpsPushButton_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_N,0),(_Ah,1),(_Ai,2),(_Aj,3)))
_ArrisRouterWpsPushButton_Type.__name__=_D
_ArrisRouterWpsPushButton_Object=MibScalar
arrisRouterWpsPushButton=_ArrisRouterWpsPushButton_Object((1,3,6,1,4,1,4115,1,20,1,1,3,30,11),_ArrisRouterWpsPushButton_Type())
arrisRouterWpsPushButton.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWpsPushButton.setStatus(_A)
class _ArrisRouterWpsUUID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_ArrisRouterWpsUUID_Type.__name__=_G
_ArrisRouterWpsUUID_Object=MibScalar
arrisRouterWpsUUID=_ArrisRouterWpsUUID_Object((1,3,6,1,4,1,4115,1,20,1,1,3,30,14),_ArrisRouterWpsUUID_Type())
arrisRouterWpsUUID.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWpsUUID.setStatus(_A)
_ArrisRouterWPSMethodCfg_ObjectIdentity=ObjectIdentity
arrisRouterWPSMethodCfg=_ArrisRouterWPSMethodCfg_ObjectIdentity((1,3,6,1,4,1,4115,1,20,1,1,3,30,15))
class _ArrisRouterWPSMethodLabel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_O,0),(_Q,1)))
_ArrisRouterWPSMethodLabel_Type.__name__=_D
_ArrisRouterWPSMethodLabel_Object=MibScalar
arrisRouterWPSMethodLabel=_ArrisRouterWPSMethodLabel_Object((1,3,6,1,4,1,4115,1,20,1,1,3,30,15,1),_ArrisRouterWPSMethodLabel_Type())
arrisRouterWPSMethodLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWPSMethodLabel.setStatus(_A)
class _ArrisRouterWPSMethodPIN_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_O,0),(_Q,1)))
_ArrisRouterWPSMethodPIN_Type.__name__=_D
_ArrisRouterWPSMethodPIN_Object=MibScalar
arrisRouterWPSMethodPIN=_ArrisRouterWPSMethodPIN_Object((1,3,6,1,4,1,4115,1,20,1,1,3,30,15,2),_ArrisRouterWPSMethodPIN_Type())
arrisRouterWPSMethodPIN.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWPSMethodPIN.setStatus(_A)
class _ArrisRouterWPSMethodPushButton_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_O,0),(_Q,1)))
_ArrisRouterWPSMethodPushButton_Type.__name__=_D
_ArrisRouterWPSMethodPushButton_Object=MibScalar
arrisRouterWPSMethodPushButton=_ArrisRouterWPSMethodPushButton_Object((1,3,6,1,4,1,4115,1,20,1,1,3,30,15,3),_ArrisRouterWPSMethodPushButton_Type())
arrisRouterWPSMethodPushButton.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWPSMethodPushButton.setStatus(_A)
class _ArrisRouterWPSMethodKeypad_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_O,0),(_Q,1)))
_ArrisRouterWPSMethodKeypad_Type.__name__=_D
_ArrisRouterWPSMethodKeypad_Object=MibScalar
arrisRouterWPSMethodKeypad=_ArrisRouterWPSMethodKeypad_Object((1,3,6,1,4,1,4115,1,20,1,1,3,30,15,4),_ArrisRouterWPSMethodKeypad_Type())
arrisRouterWPSMethodKeypad.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWPSMethodKeypad.setStatus(_A)
class _ArrisRouterWiFiResetDefaults_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('nothingToReset',0),('resetWifiDefaults',1)))
_ArrisRouterWiFiResetDefaults_Type.__name__=_D
_ArrisRouterWiFiResetDefaults_Object=MibScalar
arrisRouterWiFiResetDefaults=_ArrisRouterWiFiResetDefaults_Object((1,3,6,1,4,1,4115,1,20,1,1,3,32),_ArrisRouterWiFiResetDefaults_Type())
arrisRouterWiFiResetDefaults.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFiResetDefaults.setStatus(_A)
_ArrisRouterWiFiCustomSSIDStr_Type=DisplayString
_ArrisRouterWiFiCustomSSIDStr_Object=MibScalar
arrisRouterWiFiCustomSSIDStr=_ArrisRouterWiFiCustomSSIDStr_Object((1,3,6,1,4,1,4115,1,20,1,1,3,34),_ArrisRouterWiFiCustomSSIDStr_Type())
arrisRouterWiFiCustomSSIDStr.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFiCustomSSIDStr.setStatus(_A)
class _ArrisRouterWiFiRadioControlMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('userControlled',0),('msoControlled24bgnMode',1),('msoControlled24nMode',2),('msoControlled50nMode',3)))
_ArrisRouterWiFiRadioControlMode_Type.__name__=_D
_ArrisRouterWiFiRadioControlMode_Object=MibScalar
arrisRouterWiFiRadioControlMode=_ArrisRouterWiFiRadioControlMode_Object((1,3,6,1,4,1,4115,1,20,1,1,3,37),_ArrisRouterWiFiRadioControlMode_Type())
arrisRouterWiFiRadioControlMode.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFiRadioControlMode.setStatus(_A)
_ArrisRouterWiFiScan_ObjectIdentity=ObjectIdentity
arrisRouterWiFiScan=_ArrisRouterWiFiScan_ObjectIdentity((1,3,6,1,4,1,4115,1,20,1,1,3,39))
class _ArrisRouterWiFiStartScan_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('startRadio0',1),('startRadio1',2)))
_ArrisRouterWiFiStartScan_Type.__name__=_D
_ArrisRouterWiFiStartScan_Object=MibScalar
arrisRouterWiFiStartScan=_ArrisRouterWiFiStartScan_Object((1,3,6,1,4,1,4115,1,20,1,1,3,39,1),_ArrisRouterWiFiStartScan_Type())
arrisRouterWiFiStartScan.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFiStartScan.setStatus(_A)
class _ArrisRouterWiFiScanResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('uninit',0),('running',1),('completeError',2),('completeSuccess',3)))
_ArrisRouterWiFiScanResult_Type.__name__=_D
_ArrisRouterWiFiScanResult_Object=MibScalar
arrisRouterWiFiScanResult=_ArrisRouterWiFiScanResult_Object((1,3,6,1,4,1,4115,1,20,1,1,3,39,2),_ArrisRouterWiFiScanResult_Type())
arrisRouterWiFiScanResult.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWiFiScanResult.setStatus(_A)
_ArrisRouterWiFiScanResultTable_Object=MibTable
arrisRouterWiFiScanResultTable=_ArrisRouterWiFiScanResultTable_Object((1,3,6,1,4,1,4115,1,20,1,1,3,39,3))
if mibBuilder.loadTexts:arrisRouterWiFiScanResultTable.setStatus(_A)
_ArrisRouterWiFiScanResultEntry_Object=MibTableRow
arrisRouterWiFiScanResultEntry=_ArrisRouterWiFiScanResultEntry_Object((1,3,6,1,4,1,4115,1,20,1,1,3,39,3,1))
arrisRouterWiFiScanResultEntry.setIndexNames((0,_I,_Ak))
if mibBuilder.loadTexts:arrisRouterWiFiScanResultEntry.setStatus(_A)
_ArrisRouterWiFiScanIndex_Type=Unsigned32
_ArrisRouterWiFiScanIndex_Object=MibTableColumn
arrisRouterWiFiScanIndex=_ArrisRouterWiFiScanIndex_Object((1,3,6,1,4,1,4115,1,20,1,1,3,39,3,1,1),_ArrisRouterWiFiScanIndex_Type())
arrisRouterWiFiScanIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:arrisRouterWiFiScanIndex.setStatus(_A)
_ArrisRouterWiFiScanSSID_Type=DisplayString
_ArrisRouterWiFiScanSSID_Object=MibTableColumn
arrisRouterWiFiScanSSID=_ArrisRouterWiFiScanSSID_Object((1,3,6,1,4,1,4115,1,20,1,1,3,39,3,1,2),_ArrisRouterWiFiScanSSID_Type())
arrisRouterWiFiScanSSID.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWiFiScanSSID.setStatus(_A)
_ArrisRouterWiFiScanChannel_Type=Unsigned32
_ArrisRouterWiFiScanChannel_Object=MibTableColumn
arrisRouterWiFiScanChannel=_ArrisRouterWiFiScanChannel_Object((1,3,6,1,4,1,4115,1,20,1,1,3,39,3,1,3),_ArrisRouterWiFiScanChannel_Type())
arrisRouterWiFiScanChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWiFiScanChannel.setStatus(_A)
_ArrisRouterWiFiScanChannel2_Type=Unsigned32
_ArrisRouterWiFiScanChannel2_Object=MibTableColumn
arrisRouterWiFiScanChannel2=_ArrisRouterWiFiScanChannel2_Object((1,3,6,1,4,1,4115,1,20,1,1,3,39,3,1,4),_ArrisRouterWiFiScanChannel2_Type())
arrisRouterWiFiScanChannel2.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWiFiScanChannel2.setStatus(_A)
_ArrisRouterWiFiScanRSSI_Type=Integer32
_ArrisRouterWiFiScanRSSI_Object=MibTableColumn
arrisRouterWiFiScanRSSI=_ArrisRouterWiFiScanRSSI_Object((1,3,6,1,4,1,4115,1,20,1,1,3,39,3,1,5),_ArrisRouterWiFiScanRSSI_Type())
arrisRouterWiFiScanRSSI.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWiFiScanRSSI.setStatus(_A)
if mibBuilder.loadTexts:arrisRouterWiFiScanRSSI.setUnits('dBm')
_ArrisRouterWiFiScanNoise_Type=Integer32
_ArrisRouterWiFiScanNoise_Object=MibTableColumn
arrisRouterWiFiScanNoise=_ArrisRouterWiFiScanNoise_Object((1,3,6,1,4,1,4115,1,20,1,1,3,39,3,1,6),_ArrisRouterWiFiScanNoise_Type())
arrisRouterWiFiScanNoise.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWiFiScanNoise.setStatus(_A)
if mibBuilder.loadTexts:arrisRouterWiFiScanNoise.setUnits('dBm')
_ArrisRouterWiFiScanMAC_Type=DisplayString
_ArrisRouterWiFiScanMAC_Object=MibTableColumn
arrisRouterWiFiScanMAC=_ArrisRouterWiFiScanMAC_Object((1,3,6,1,4,1,4115,1,20,1,1,3,39,3,1,7),_ArrisRouterWiFiScanMAC_Type())
arrisRouterWiFiScanMAC.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWiFiScanMAC.setStatus(_A)
_ArrisRouterWiFiScanMfg_Type=DisplayString
_ArrisRouterWiFiScanMfg_Object=MibTableColumn
arrisRouterWiFiScanMfg=_ArrisRouterWiFiScanMfg_Object((1,3,6,1,4,1,4115,1,20,1,1,3,39,3,1,8),_ArrisRouterWiFiScanMfg_Type())
arrisRouterWiFiScanMfg.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWiFiScanMfg.setStatus(_A)
_ArrisRouterWiFiScanSupportedRates_Type=DisplayString
_ArrisRouterWiFiScanSupportedRates_Object=MibTableColumn
arrisRouterWiFiScanSupportedRates=_ArrisRouterWiFiScanSupportedRates_Object((1,3,6,1,4,1,4115,1,20,1,1,3,39,3,1,9),_ArrisRouterWiFiScanSupportedRates_Type())
arrisRouterWiFiScanSupportedRates.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWiFiScanSupportedRates.setStatus(_A)
_ArrisRouterWiFiScanOperatingStandards_Type=DisplayString
_ArrisRouterWiFiScanOperatingStandards_Object=MibTableColumn
arrisRouterWiFiScanOperatingStandards=_ArrisRouterWiFiScanOperatingStandards_Object((1,3,6,1,4,1,4115,1,20,1,1,3,39,3,1,10),_ArrisRouterWiFiScanOperatingStandards_Type())
arrisRouterWiFiScanOperatingStandards.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWiFiScanOperatingStandards.setStatus(_A)
class _ArrisRouterWiFiScanSecurityModeEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('unknow',0),(_O,1),('wep',2),('wpa',3),('wpa2',4),('wpaWpa2',5),(_AG,6),(_AH,7),(_AI,8)))
_ArrisRouterWiFiScanSecurityModeEnabled_Type.__name__=_D
_ArrisRouterWiFiScanSecurityModeEnabled_Object=MibTableColumn
arrisRouterWiFiScanSecurityModeEnabled=_ArrisRouterWiFiScanSecurityModeEnabled_Object((1,3,6,1,4,1,4115,1,20,1,1,3,39,3,1,11),_ArrisRouterWiFiScanSecurityModeEnabled_Type())
arrisRouterWiFiScanSecurityModeEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWiFiScanSecurityModeEnabled.setStatus(_A)
class _ArrisRouterWiFiScanOperatingChannelBandwidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_R,0),('n20Mhz',1),('n40Mhz',2),('ac80Mhz',3),('ac160Mhz',4)))
_ArrisRouterWiFiScanOperatingChannelBandwidth_Type.__name__=_D
_ArrisRouterWiFiScanOperatingChannelBandwidth_Object=MibTableColumn
arrisRouterWiFiScanOperatingChannelBandwidth=_ArrisRouterWiFiScanOperatingChannelBandwidth_Object((1,3,6,1,4,1,4115,1,20,1,1,3,39,3,1,12),_ArrisRouterWiFiScanOperatingChannelBandwidth_Type())
arrisRouterWiFiScanOperatingChannelBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWiFiScanOperatingChannelBandwidth.setStatus(_A)
_ArrisRouterWiFiClientInfoTable_Object=MibTable
arrisRouterWiFiClientInfoTable=_ArrisRouterWiFiClientInfoTable_Object((1,3,6,1,4,1,4115,1,20,1,1,3,42))
if mibBuilder.loadTexts:arrisRouterWiFiClientInfoTable.setStatus(_A)
_ArrisRouterWiFiClientInfoEntry_Object=MibTableRow
arrisRouterWiFiClientInfoEntry=_ArrisRouterWiFiClientInfoEntry_Object((1,3,6,1,4,1,4115,1,20,1,1,3,42,1))
arrisRouterWiFiClientInfoEntry.setIndexNames((0,_K,_L),(0,_I,_Al))
if mibBuilder.loadTexts:arrisRouterWiFiClientInfoEntry.setStatus(_A)
class _ArrisRouterWiFiClientInfoIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_ArrisRouterWiFiClientInfoIndex_Type.__name__=_D
_ArrisRouterWiFiClientInfoIndex_Object=MibTableColumn
arrisRouterWiFiClientInfoIndex=_ArrisRouterWiFiClientInfoIndex_Object((1,3,6,1,4,1,4115,1,20,1,1,3,42,1,1),_ArrisRouterWiFiClientInfoIndex_Type())
arrisRouterWiFiClientInfoIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:arrisRouterWiFiClientInfoIndex.setStatus(_A)
_ArrisRouterWiFiClientInfoIPAddrType_Type=InetAddressType
_ArrisRouterWiFiClientInfoIPAddrType_Object=MibTableColumn
arrisRouterWiFiClientInfoIPAddrType=_ArrisRouterWiFiClientInfoIPAddrType_Object((1,3,6,1,4,1,4115,1,20,1,1,3,42,1,2),_ArrisRouterWiFiClientInfoIPAddrType_Type())
arrisRouterWiFiClientInfoIPAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWiFiClientInfoIPAddrType.setStatus(_A)
_ArrisRouterWiFiClientInfoIPAddr_Type=InetAddress
_ArrisRouterWiFiClientInfoIPAddr_Object=MibTableColumn
arrisRouterWiFiClientInfoIPAddr=_ArrisRouterWiFiClientInfoIPAddr_Object((1,3,6,1,4,1,4115,1,20,1,1,3,42,1,3),_ArrisRouterWiFiClientInfoIPAddr_Type())
arrisRouterWiFiClientInfoIPAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWiFiClientInfoIPAddr.setStatus(_A)
_ArrisRouterWiFiClientInfoIPAddrTextual_Type=DisplayString
_ArrisRouterWiFiClientInfoIPAddrTextual_Object=MibTableColumn
arrisRouterWiFiClientInfoIPAddrTextual=_ArrisRouterWiFiClientInfoIPAddrTextual_Object((1,3,6,1,4,1,4115,1,20,1,1,3,42,1,4),_ArrisRouterWiFiClientInfoIPAddrTextual_Type())
arrisRouterWiFiClientInfoIPAddrTextual.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWiFiClientInfoIPAddrTextual.setStatus(_A)
class _ArrisRouterWiFiClientInfoHostName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ArrisRouterWiFiClientInfoHostName_Type.__name__=_G
_ArrisRouterWiFiClientInfoHostName_Object=MibTableColumn
arrisRouterWiFiClientInfoHostName=_ArrisRouterWiFiClientInfoHostName_Object((1,3,6,1,4,1,4115,1,20,1,1,3,42,1,5),_ArrisRouterWiFiClientInfoHostName_Type())
arrisRouterWiFiClientInfoHostName.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWiFiClientInfoHostName.setStatus(_A)
_ArrisRouterWiFiClientInfoMAC_Type=MacAddress
_ArrisRouterWiFiClientInfoMAC_Object=MibTableColumn
arrisRouterWiFiClientInfoMAC=_ArrisRouterWiFiClientInfoMAC_Object((1,3,6,1,4,1,4115,1,20,1,1,3,42,1,6),_ArrisRouterWiFiClientInfoMAC_Type())
arrisRouterWiFiClientInfoMAC.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWiFiClientInfoMAC.setStatus(_A)
class _ArrisRouterWiFiClientInfoMACMfg_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ArrisRouterWiFiClientInfoMACMfg_Type.__name__=_G
_ArrisRouterWiFiClientInfoMACMfg_Object=MibTableColumn
arrisRouterWiFiClientInfoMACMfg=_ArrisRouterWiFiClientInfoMACMfg_Object((1,3,6,1,4,1,4115,1,20,1,1,3,42,1,7),_ArrisRouterWiFiClientInfoMACMfg_Type())
arrisRouterWiFiClientInfoMACMfg.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWiFiClientInfoMACMfg.setStatus(_A)
class _ArrisRouterWiFiClientInfoStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('down',0),('up',1)))
_ArrisRouterWiFiClientInfoStatus_Type.__name__=_D
_ArrisRouterWiFiClientInfoStatus_Object=MibTableColumn
arrisRouterWiFiClientInfoStatus=_ArrisRouterWiFiClientInfoStatus_Object((1,3,6,1,4,1,4115,1,20,1,1,3,42,1,8),_ArrisRouterWiFiClientInfoStatus_Type())
arrisRouterWiFiClientInfoStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWiFiClientInfoStatus.setStatus(_A)
_ArrisRouterWiFiClientInfoFirstSeen_Type=DateAndTime
_ArrisRouterWiFiClientInfoFirstSeen_Object=MibTableColumn
arrisRouterWiFiClientInfoFirstSeen=_ArrisRouterWiFiClientInfoFirstSeen_Object((1,3,6,1,4,1,4115,1,20,1,1,3,42,1,9),_ArrisRouterWiFiClientInfoFirstSeen_Type())
arrisRouterWiFiClientInfoFirstSeen.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWiFiClientInfoFirstSeen.setStatus(_A)
_ArrisRouterWiFiClientInfoLastSeen_Type=DateAndTime
_ArrisRouterWiFiClientInfoLastSeen_Object=MibTableColumn
arrisRouterWiFiClientInfoLastSeen=_ArrisRouterWiFiClientInfoLastSeen_Object((1,3,6,1,4,1,4115,1,20,1,1,3,42,1,10),_ArrisRouterWiFiClientInfoLastSeen_Type())
arrisRouterWiFiClientInfoLastSeen.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWiFiClientInfoLastSeen.setStatus(_A)
_ArrisRouterWiFiClientInfoIdleTime_Type=Integer32
_ArrisRouterWiFiClientInfoIdleTime_Object=MibTableColumn
arrisRouterWiFiClientInfoIdleTime=_ArrisRouterWiFiClientInfoIdleTime_Object((1,3,6,1,4,1,4115,1,20,1,1,3,42,1,11),_ArrisRouterWiFiClientInfoIdleTime_Type())
arrisRouterWiFiClientInfoIdleTime.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWiFiClientInfoIdleTime.setStatus(_A)
if mibBuilder.loadTexts:arrisRouterWiFiClientInfoIdleTime.setUnits(_M)
_ArrisRouterWiFiClientInfoInNetworkTime_Type=Integer32
_ArrisRouterWiFiClientInfoInNetworkTime_Object=MibTableColumn
arrisRouterWiFiClientInfoInNetworkTime=_ArrisRouterWiFiClientInfoInNetworkTime_Object((1,3,6,1,4,1,4115,1,20,1,1,3,42,1,12),_ArrisRouterWiFiClientInfoInNetworkTime_Type())
arrisRouterWiFiClientInfoInNetworkTime.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWiFiClientInfoInNetworkTime.setStatus(_A)
if mibBuilder.loadTexts:arrisRouterWiFiClientInfoInNetworkTime.setUnits(_M)
_ArrisRouterWiFiClientInfoState_Type=DisplayString
_ArrisRouterWiFiClientInfoState_Object=MibTableColumn
arrisRouterWiFiClientInfoState=_ArrisRouterWiFiClientInfoState_Object((1,3,6,1,4,1,4115,1,20,1,1,3,42,1,13),_ArrisRouterWiFiClientInfoState_Type())
arrisRouterWiFiClientInfoState.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWiFiClientInfoState.setStatus(_A)
_ArrisRouterWiFiClientInfoFlags_Type=DisplayString
_ArrisRouterWiFiClientInfoFlags_Object=MibTableColumn
arrisRouterWiFiClientInfoFlags=_ArrisRouterWiFiClientInfoFlags_Object((1,3,6,1,4,1,4115,1,20,1,1,3,42,1,14),_ArrisRouterWiFiClientInfoFlags_Type())
arrisRouterWiFiClientInfoFlags.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWiFiClientInfoFlags.setStatus(_A)
_ArrisRouterWiFiClientInfoTxPkts_Type=Integer32
_ArrisRouterWiFiClientInfoTxPkts_Object=MibTableColumn
arrisRouterWiFiClientInfoTxPkts=_ArrisRouterWiFiClientInfoTxPkts_Object((1,3,6,1,4,1,4115,1,20,1,1,3,42,1,15),_ArrisRouterWiFiClientInfoTxPkts_Type())
arrisRouterWiFiClientInfoTxPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWiFiClientInfoTxPkts.setStatus(_A)
if mibBuilder.loadTexts:arrisRouterWiFiClientInfoTxPkts.setUnits(_a)
_ArrisRouterWiFiClientInfoTxFailures_Type=Integer32
_ArrisRouterWiFiClientInfoTxFailures_Object=MibTableColumn
arrisRouterWiFiClientInfoTxFailures=_ArrisRouterWiFiClientInfoTxFailures_Object((1,3,6,1,4,1,4115,1,20,1,1,3,42,1,16),_ArrisRouterWiFiClientInfoTxFailures_Type())
arrisRouterWiFiClientInfoTxFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWiFiClientInfoTxFailures.setStatus(_A)
if mibBuilder.loadTexts:arrisRouterWiFiClientInfoTxFailures.setUnits(_a)
_ArrisRouterWiFiClientInfoRxUnicastPkts_Type=Integer32
_ArrisRouterWiFiClientInfoRxUnicastPkts_Object=MibTableColumn
arrisRouterWiFiClientInfoRxUnicastPkts=_ArrisRouterWiFiClientInfoRxUnicastPkts_Object((1,3,6,1,4,1,4115,1,20,1,1,3,42,1,17),_ArrisRouterWiFiClientInfoRxUnicastPkts_Type())
arrisRouterWiFiClientInfoRxUnicastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWiFiClientInfoRxUnicastPkts.setStatus(_A)
if mibBuilder.loadTexts:arrisRouterWiFiClientInfoRxUnicastPkts.setUnits(_a)
_ArrisRouterWiFiClientInfoRxMulticastPkts_Type=Integer32
_ArrisRouterWiFiClientInfoRxMulticastPkts_Object=MibTableColumn
arrisRouterWiFiClientInfoRxMulticastPkts=_ArrisRouterWiFiClientInfoRxMulticastPkts_Object((1,3,6,1,4,1,4115,1,20,1,1,3,42,1,18),_ArrisRouterWiFiClientInfoRxMulticastPkts_Type())
arrisRouterWiFiClientInfoRxMulticastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWiFiClientInfoRxMulticastPkts.setStatus(_A)
if mibBuilder.loadTexts:arrisRouterWiFiClientInfoRxMulticastPkts.setUnits(_a)
_ArrisRouterWiFiClientInfoLastTxPktRate_Type=Integer32
_ArrisRouterWiFiClientInfoLastTxPktRate_Object=MibTableColumn
arrisRouterWiFiClientInfoLastTxPktRate=_ArrisRouterWiFiClientInfoLastTxPktRate_Object((1,3,6,1,4,1,4115,1,20,1,1,3,42,1,19),_ArrisRouterWiFiClientInfoLastTxPktRate_Type())
arrisRouterWiFiClientInfoLastTxPktRate.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWiFiClientInfoLastTxPktRate.setStatus(_A)
if mibBuilder.loadTexts:arrisRouterWiFiClientInfoLastTxPktRate.setUnits('kbps')
_ArrisRouterWiFiClientInfoLastRxPktRate_Type=Integer32
_ArrisRouterWiFiClientInfoLastRxPktRate_Object=MibTableColumn
arrisRouterWiFiClientInfoLastRxPktRate=_ArrisRouterWiFiClientInfoLastRxPktRate_Object((1,3,6,1,4,1,4115,1,20,1,1,3,42,1,20),_ArrisRouterWiFiClientInfoLastRxPktRate_Type())
arrisRouterWiFiClientInfoLastRxPktRate.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWiFiClientInfoLastRxPktRate.setStatus(_A)
if mibBuilder.loadTexts:arrisRouterWiFiClientInfoLastRxPktRate.setUnits('kbps')
_ArrisRouterWiFiClientInfoRateSet_Type=DisplayString
_ArrisRouterWiFiClientInfoRateSet_Object=MibTableColumn
arrisRouterWiFiClientInfoRateSet=_ArrisRouterWiFiClientInfoRateSet_Object((1,3,6,1,4,1,4115,1,20,1,1,3,42,1,21),_ArrisRouterWiFiClientInfoRateSet_Type())
arrisRouterWiFiClientInfoRateSet.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWiFiClientInfoRateSet.setStatus(_A)
_ArrisRouterWiFiClientInfoRSSI_Type=Integer32
_ArrisRouterWiFiClientInfoRSSI_Object=MibTableColumn
arrisRouterWiFiClientInfoRSSI=_ArrisRouterWiFiClientInfoRSSI_Object((1,3,6,1,4,1,4115,1,20,1,1,3,42,1,22),_ArrisRouterWiFiClientInfoRSSI_Type())
arrisRouterWiFiClientInfoRSSI.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWiFiClientInfoRSSI.setStatus(_A)
_ArrisRouterWiFiPhysicalChannel_Type=Integer32
_ArrisRouterWiFiPhysicalChannel_Object=MibScalar
arrisRouterWiFiPhysicalChannel=_ArrisRouterWiFiPhysicalChannel_Object((1,3,6,1,4,1,4115,1,20,1,1,3,43),_ArrisRouterWiFiPhysicalChannel_Type())
arrisRouterWiFiPhysicalChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWiFiPhysicalChannel.setStatus(_A)
_ArrisRouterWiFi50RadioSettings_ObjectIdentity=ObjectIdentity
arrisRouterWiFi50RadioSettings=_ArrisRouterWiFi50RadioSettings_ObjectIdentity((1,3,6,1,4,1,4115,1,20,1,1,3,50))
class _ArrisRouterWiFi50Channel_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,216))
_ArrisRouterWiFi50Channel_Type.__name__=_H
_ArrisRouterWiFi50Channel_Object=MibScalar
arrisRouterWiFi50Channel=_ArrisRouterWiFi50Channel_Object((1,3,6,1,4,1,4115,1,20,1,1,3,50,1),_ArrisRouterWiFi50Channel_Type())
arrisRouterWiFi50Channel.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFi50Channel.setStatus(_A)
class _ArrisRouterWiFi50Mode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,0,1,4,5,6,7)));namedValues=NamedValues(*((_N,-1),('anMix',0),('aOnly',1),('nOnly',4),('acOnly',5),('nacMix',6),('anacMix',7)))
_ArrisRouterWiFi50Mode_Type.__name__=_D
_ArrisRouterWiFi50Mode_Object=MibScalar
arrisRouterWiFi50Mode=_ArrisRouterWiFi50Mode_Object((1,3,6,1,4,1,4115,1,20,1,1,3,50,2),_ArrisRouterWiFi50Mode_Type())
arrisRouterWiFi50Mode.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFi50Mode.setStatus(_A)
class _ArrisRouterWiFi50BeaconInterval_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ArrisRouterWiFi50BeaconInterval_Type.__name__=_H
_ArrisRouterWiFi50BeaconInterval_Object=MibScalar
arrisRouterWiFi50BeaconInterval=_ArrisRouterWiFi50BeaconInterval_Object((1,3,6,1,4,1,4115,1,20,1,1,3,50,3),_ArrisRouterWiFi50BeaconInterval_Type())
arrisRouterWiFi50BeaconInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFi50BeaconInterval.setStatus(_A)
if mibBuilder.loadTexts:arrisRouterWiFi50BeaconInterval.setUnits(_P)
class _ArrisRouterWiFi50DTIMInterval_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_ArrisRouterWiFi50DTIMInterval_Type.__name__=_H
_ArrisRouterWiFi50DTIMInterval_Object=MibScalar
arrisRouterWiFi50DTIMInterval=_ArrisRouterWiFi50DTIMInterval_Object((1,3,6,1,4,1,4115,1,20,1,1,3,50,4),_ArrisRouterWiFi50DTIMInterval_Type())
arrisRouterWiFi50DTIMInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFi50DTIMInterval.setStatus(_A)
if mibBuilder.loadTexts:arrisRouterWiFi50DTIMInterval.setUnits(_P)
class _ArrisRouterWiFi50TxPreamble_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,0,1)));namedValues=NamedValues(*((_N,-1),('long',0),('short',1)))
_ArrisRouterWiFi50TxPreamble_Type.__name__=_D
_ArrisRouterWiFi50TxPreamble_Object=MibScalar
arrisRouterWiFi50TxPreamble=_ArrisRouterWiFi50TxPreamble_Object((1,3,6,1,4,1,4115,1,20,1,1,3,50,5),_ArrisRouterWiFi50TxPreamble_Type())
arrisRouterWiFi50TxPreamble.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFi50TxPreamble.setStatus(_A)
class _ArrisRouterWiFi50RTSThreshold_Type(Unsigned32):defaultValue=2347;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2347))
_ArrisRouterWiFi50RTSThreshold_Type.__name__=_H
_ArrisRouterWiFi50RTSThreshold_Object=MibScalar
arrisRouterWiFi50RTSThreshold=_ArrisRouterWiFi50RTSThreshold_Object((1,3,6,1,4,1,4115,1,20,1,1,3,50,6),_ArrisRouterWiFi50RTSThreshold_Type())
arrisRouterWiFi50RTSThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFi50RTSThreshold.setStatus(_A)
if mibBuilder.loadTexts:arrisRouterWiFi50RTSThreshold.setUnits(_T)
class _ArrisRouterWiFi50FragmentThresh_Type(Unsigned32):defaultValue=2346;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(256,2346))
_ArrisRouterWiFi50FragmentThresh_Type.__name__=_H
_ArrisRouterWiFi50FragmentThresh_Object=MibScalar
arrisRouterWiFi50FragmentThresh=_ArrisRouterWiFi50FragmentThresh_Object((1,3,6,1,4,1,4115,1,20,1,1,3,50,7),_ArrisRouterWiFi50FragmentThresh_Type())
arrisRouterWiFi50FragmentThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFi50FragmentThresh.setStatus(_A)
if mibBuilder.loadTexts:arrisRouterWiFi50FragmentThresh.setUnits(_T)
class _ArrisRouterWiFi50ShortSlot_Type(TruthValue):defaultValue=1
_ArrisRouterWiFi50ShortSlot_Type.__name__=_F
_ArrisRouterWiFi50ShortSlot_Object=MibScalar
arrisRouterWiFi50ShortSlot=_ArrisRouterWiFi50ShortSlot_Object((1,3,6,1,4,1,4115,1,20,1,1,3,50,8),_ArrisRouterWiFi50ShortSlot_Type())
arrisRouterWiFi50ShortSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFi50ShortSlot.setStatus(_A)
class _ArrisRouterWiFi50FrameBurst_Type(TruthValue):defaultValue=2
_ArrisRouterWiFi50FrameBurst_Type.__name__=_F
_ArrisRouterWiFi50FrameBurst_Object=MibScalar
arrisRouterWiFi50FrameBurst=_ArrisRouterWiFi50FrameBurst_Object((1,3,6,1,4,1,4115,1,20,1,1,3,50,9),_ArrisRouterWiFi50FrameBurst_Type())
arrisRouterWiFi50FrameBurst.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFi50FrameBurst.setStatus(_A)
class _ArrisRouterWiFi50EnableRadio_Type(TruthValue):defaultValue=1
_ArrisRouterWiFi50EnableRadio_Type.__name__=_F
_ArrisRouterWiFi50EnableRadio_Object=MibScalar
arrisRouterWiFi50EnableRadio=_ArrisRouterWiFi50EnableRadio_Object((1,3,6,1,4,1,4115,1,20,1,1,3,50,10),_ArrisRouterWiFi50EnableRadio_Type())
arrisRouterWiFi50EnableRadio.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFi50EnableRadio.setStatus(_A)
class _ArrisRouterWiFi50ShortRetryLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_ArrisRouterWiFi50ShortRetryLimit_Type.__name__=_D
_ArrisRouterWiFi50ShortRetryLimit_Object=MibScalar
arrisRouterWiFi50ShortRetryLimit=_ArrisRouterWiFi50ShortRetryLimit_Object((1,3,6,1,4,1,4115,1,20,1,1,3,50,12),_ArrisRouterWiFi50ShortRetryLimit_Type())
arrisRouterWiFi50ShortRetryLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFi50ShortRetryLimit.setStatus(_A)
class _ArrisRouterWiFi50LongRetryLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_ArrisRouterWiFi50LongRetryLimit_Type.__name__=_D
_ArrisRouterWiFi50LongRetryLimit_Object=MibScalar
arrisRouterWiFi50LongRetryLimit=_ArrisRouterWiFi50LongRetryLimit_Object((1,3,6,1,4,1,4115,1,20,1,1,3,50,13),_ArrisRouterWiFi50LongRetryLimit_Type())
arrisRouterWiFi50LongRetryLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFi50LongRetryLimit.setStatus(_A)
class _ArrisRouterWiFi50OutputPower_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(12,25,50,75,100)));namedValues=NamedValues(*((_A8,12),(_A9,25),(_AA,50),(_AB,75),(_AC,100)))
_ArrisRouterWiFi50OutputPower_Type.__name__=_D
_ArrisRouterWiFi50OutputPower_Object=MibScalar
arrisRouterWiFi50OutputPower=_ArrisRouterWiFi50OutputPower_Object((1,3,6,1,4,1,4115,1,20,1,1,3,50,14),_ArrisRouterWiFi50OutputPower_Type())
arrisRouterWiFi50OutputPower.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFi50OutputPower.setStatus(_A)
class _ArrisRouterWiFi50MulticastA_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,12,18,24,36,48,72,96,108)));namedValues=NamedValues(*((_R,0),('rate12mbps',12),('rate18mbps',18),('rate24mbps',24),('rate36mbps',36),('rate48mbps',48),('rate72mbps',72),('rate96mbps',96),('rate108mbps',108)))
_ArrisRouterWiFi50MulticastA_Type.__name__=_D
_ArrisRouterWiFi50MulticastA_Object=MibScalar
arrisRouterWiFi50MulticastA=_ArrisRouterWiFi50MulticastA_Object((1,3,6,1,4,1,4115,1,20,1,1,3,50,15),_ArrisRouterWiFi50MulticastA_Type())
arrisRouterWiFi50MulticastA.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFi50MulticastA.setStatus(_A)
_ArrisRouterWiFi50PhysicalChannel_Type=Integer32
_ArrisRouterWiFi50PhysicalChannel_Object=MibScalar
arrisRouterWiFi50PhysicalChannel=_ArrisRouterWiFi50PhysicalChannel_Object((1,3,6,1,4,1,4115,1,20,1,1,3,50,16),_ArrisRouterWiFi50PhysicalChannel_Type())
arrisRouterWiFi50PhysicalChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWiFi50PhysicalChannel.setStatus(_A)
_ArrisRouterWiFi50NSettings_ObjectIdentity=ObjectIdentity
arrisRouterWiFi50NSettings=_ArrisRouterWiFi50NSettings_ObjectIdentity((1,3,6,1,4,1,4115,1,20,1,1,3,50,20))
class _ArrisRouterWiFi50HTMCS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25)));namedValues=NamedValues(*((_R,0),('legacy',1),('mcs0',2),('mcs1',3),('mcs2',4),('mcs3',5),('mcs4',6),('mcs5',7),('mcs6',8),('mcs7',9),('mcs8',10),('mcs9',11),('mcs10',12),('mcs11',13),('mcs12',14),('mcs13',15),('mcs14',16),('mcs15',17),('mcs16',18),('mcs17',19),('mcs18',20),('mcs19',21),('mcs20',22),('mcs21',23),('mcs22',24),('mcs23',25)))
_ArrisRouterWiFi50HTMCS_Type.__name__=_D
_ArrisRouterWiFi50HTMCS_Object=MibScalar
arrisRouterWiFi50HTMCS=_ArrisRouterWiFi50HTMCS_Object((1,3,6,1,4,1,4115,1,20,1,1,3,50,20,1),_ArrisRouterWiFi50HTMCS_Type())
arrisRouterWiFi50HTMCS.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFi50HTMCS.setStatus(_A)
class _ArrisRouterWiFi50ChannelBW_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,0,2,3)));namedValues=NamedValues(*((_N,-1),(_AD,0),(_AE,2),('width20and40and80Mhz',3)))
_ArrisRouterWiFi50ChannelBW_Type.__name__=_D
_ArrisRouterWiFi50ChannelBW_Object=MibScalar
arrisRouterWiFi50ChannelBW=_ArrisRouterWiFi50ChannelBW_Object((1,3,6,1,4,1,4115,1,20,1,1,3,50,20,2),_ArrisRouterWiFi50ChannelBW_Type())
arrisRouterWiFi50ChannelBW.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFi50ChannelBW.setStatus(_A)
class _ArrisRouterWiFi50NSideBand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,1,2)));namedValues=NamedValues(*((_N,-1),('upper',1),('lower',2)))
_ArrisRouterWiFi50NSideBand_Type.__name__=_D
_ArrisRouterWiFi50NSideBand_Object=MibScalar
arrisRouterWiFi50NSideBand=_ArrisRouterWiFi50NSideBand_Object((1,3,6,1,4,1,4115,1,20,1,1,3,50,20,3),_ArrisRouterWiFi50NSideBand_Type())
arrisRouterWiFi50NSideBand.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFi50NSideBand.setStatus(_A)
class _ArrisRouterWiFi50HTMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('mixed',0),(_AF,1)))
_ArrisRouterWiFi50HTMode_Type.__name__=_D
_ArrisRouterWiFi50HTMode_Object=MibScalar
arrisRouterWiFi50HTMode=_ArrisRouterWiFi50HTMode_Object((1,3,6,1,4,1,4115,1,20,1,1,3,50,20,4),_ArrisRouterWiFi50HTMode_Type())
arrisRouterWiFi50HTMode.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFi50HTMode.setStatus(_A)
class _ArrisRouterWiFi50GuardInterval_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('gi400',0),('gi800',1),(_R,2)))
_ArrisRouterWiFi50GuardInterval_Type.__name__=_D
_ArrisRouterWiFi50GuardInterval_Object=MibScalar
arrisRouterWiFi50GuardInterval=_ArrisRouterWiFi50GuardInterval_Object((1,3,6,1,4,1,4115,1,20,1,1,3,50,20,5),_ArrisRouterWiFi50GuardInterval_Type())
arrisRouterWiFi50GuardInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFi50GuardInterval.setStatus(_A)
class _ArrisRouterWiFi50AMSDUEnable_Type(TruthValue):defaultValue=2
_ArrisRouterWiFi50AMSDUEnable_Type.__name__=_F
_ArrisRouterWiFi50AMSDUEnable_Object=MibScalar
arrisRouterWiFi50AMSDUEnable=_ArrisRouterWiFi50AMSDUEnable_Object((1,3,6,1,4,1,4115,1,20,1,1,3,50,20,6),_ArrisRouterWiFi50AMSDUEnable_Type())
arrisRouterWiFi50AMSDUEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFi50AMSDUEnable.setStatus(_A)
class _ArrisRouterWiFi50DeclinePeerBA_Type(TruthValue):defaultValue=2
_ArrisRouterWiFi50DeclinePeerBA_Type.__name__=_F
_ArrisRouterWiFi50DeclinePeerBA_Object=MibScalar
arrisRouterWiFi50DeclinePeerBA=_ArrisRouterWiFi50DeclinePeerBA_Object((1,3,6,1,4,1,4115,1,20,1,1,3,50,20,7),_ArrisRouterWiFi50DeclinePeerBA_Type())
arrisRouterWiFi50DeclinePeerBA.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFi50DeclinePeerBA.setStatus(_A)
class _ArrisRouterWiFi50BlockAck_Type(TruthValue):defaultValue=2
_ArrisRouterWiFi50BlockAck_Type.__name__=_F
_ArrisRouterWiFi50BlockAck_Object=MibScalar
arrisRouterWiFi50BlockAck=_ArrisRouterWiFi50BlockAck_Object((1,3,6,1,4,1,4115,1,20,1,1,3,50,20,8),_ArrisRouterWiFi50BlockAck_Type())
arrisRouterWiFi50BlockAck.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFi50BlockAck.setStatus(_A)
class _ArrisRouterWiFi50NProtection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('off',0),(_R,1)))
_ArrisRouterWiFi50NProtection_Type.__name__=_D
_ArrisRouterWiFi50NProtection_Object=MibScalar
arrisRouterWiFi50NProtection=_ArrisRouterWiFi50NProtection_Object((1,3,6,1,4,1,4115,1,20,1,1,3,50,20,9),_ArrisRouterWiFi50NProtection_Type())
arrisRouterWiFi50NProtection.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFi50NProtection.setStatus(_A)
class _ArrisRouterWiFi50HTTxStream_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_ArrisRouterWiFi50HTTxStream_Type.__name__=_H
_ArrisRouterWiFi50HTTxStream_Object=MibScalar
arrisRouterWiFi50HTTxStream=_ArrisRouterWiFi50HTTxStream_Object((1,3,6,1,4,1,4115,1,20,1,1,3,50,21),_ArrisRouterWiFi50HTTxStream_Type())
arrisRouterWiFi50HTTxStream.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFi50HTTxStream.setStatus(_A)
class _ArrisRouterWiFi50HTRxStream_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_ArrisRouterWiFi50HTRxStream_Type.__name__=_H
_ArrisRouterWiFi50HTRxStream_Object=MibScalar
arrisRouterWiFi50HTRxStream=_ArrisRouterWiFi50HTRxStream_Object((1,3,6,1,4,1,4115,1,20,1,1,3,50,22),_ArrisRouterWiFi50HTRxStream_Type())
arrisRouterWiFi50HTRxStream.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFi50HTRxStream.setStatus(_A)
class _ArrisRouterWiFi50EnableSTBC_Type(TruthValue):defaultValue=2
_ArrisRouterWiFi50EnableSTBC_Type.__name__=_F
_ArrisRouterWiFi50EnableSTBC_Object=MibScalar
arrisRouterWiFi50EnableSTBC=_ArrisRouterWiFi50EnableSTBC_Object((1,3,6,1,4,1,4115,1,20,1,1,3,50,23),_ArrisRouterWiFi50EnableSTBC_Type())
arrisRouterWiFi50EnableSTBC.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFi50EnableSTBC.setStatus(_A)
class _ArrisRouterWiFi50EnableRDG_Type(TruthValue):defaultValue=2
_ArrisRouterWiFi50EnableRDG_Type.__name__=_F
_ArrisRouterWiFi50EnableRDG_Object=MibScalar
arrisRouterWiFi50EnableRDG=_ArrisRouterWiFi50EnableRDG_Object((1,3,6,1,4,1,4115,1,20,1,1,3,50,24),_ArrisRouterWiFi50EnableRDG_Type())
arrisRouterWiFi50EnableRDG.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFi50EnableRDG.setStatus(_A)
class _ArrisRouterWiFi50IGMPSnooping_Type(TruthValue):defaultValue=2
_ArrisRouterWiFi50IGMPSnooping_Type.__name__=_F
_ArrisRouterWiFi50IGMPSnooping_Object=MibScalar
arrisRouterWiFi50IGMPSnooping=_ArrisRouterWiFi50IGMPSnooping_Object((1,3,6,1,4,1,4115,1,20,1,1,3,50,25),_ArrisRouterWiFi50IGMPSnooping_Type())
arrisRouterWiFi50IGMPSnooping.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFi50IGMPSnooping.setStatus(_A)
class _ArrisRouterWiFi50BlockDFSChan_Type(TruthValue):defaultValue=1
_ArrisRouterWiFi50BlockDFSChan_Type.__name__=_F
_ArrisRouterWiFi50BlockDFSChan_Object=MibScalar
arrisRouterWiFi50BlockDFSChan=_ArrisRouterWiFi50BlockDFSChan_Object((1,3,6,1,4,1,4115,1,20,1,1,3,50,26),_ArrisRouterWiFi50BlockDFSChan_Type())
arrisRouterWiFi50BlockDFSChan.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFi50BlockDFSChan.setStatus(_A)
class _ArrisRouterWiFi50RTSRetry_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ArrisRouterWiFi50RTSRetry_Type.__name__=_D
_ArrisRouterWiFi50RTSRetry_Object=MibScalar
arrisRouterWiFi50RTSRetry=_ArrisRouterWiFi50RTSRetry_Object((1,3,6,1,4,1,4115,1,20,1,1,3,50,27),_ArrisRouterWiFi50RTSRetry_Type())
arrisRouterWiFi50RTSRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFi50RTSRetry.setStatus(_A)
class _ArrisRouterWiFi50TxRetry_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ArrisRouterWiFi50TxRetry_Type.__name__=_D
_ArrisRouterWiFi50TxRetry_Object=MibScalar
arrisRouterWiFi50TxRetry=_ArrisRouterWiFi50TxRetry_Object((1,3,6,1,4,1,4115,1,20,1,1,3,50,28),_ArrisRouterWiFi50TxRetry_Type())
arrisRouterWiFi50TxRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFi50TxRetry.setStatus(_A)
_ArrisRouterWiFiNumSSIDSupported_Type=Unsigned32
_ArrisRouterWiFiNumSSIDSupported_Object=MibScalar
arrisRouterWiFiNumSSIDSupported=_ArrisRouterWiFiNumSSIDSupported_Object((1,3,6,1,4,1,4115,1,20,1,1,3,51),_ArrisRouterWiFiNumSSIDSupported_Type())
arrisRouterWiFiNumSSIDSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWiFiNumSSIDSupported.setStatus(_A)
class _ArrisRouterWiFiHTTxStream_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_ArrisRouterWiFiHTTxStream_Type.__name__=_H
_ArrisRouterWiFiHTTxStream_Object=MibScalar
arrisRouterWiFiHTTxStream=_ArrisRouterWiFiHTTxStream_Object((1,3,6,1,4,1,4115,1,20,1,1,3,55),_ArrisRouterWiFiHTTxStream_Type())
arrisRouterWiFiHTTxStream.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFiHTTxStream.setStatus(_A)
class _ArrisRouterWiFiHTRxStream_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_ArrisRouterWiFiHTRxStream_Type.__name__=_H
_ArrisRouterWiFiHTRxStream_Object=MibScalar
arrisRouterWiFiHTRxStream=_ArrisRouterWiFiHTRxStream_Object((1,3,6,1,4,1,4115,1,20,1,1,3,56),_ArrisRouterWiFiHTRxStream_Type())
arrisRouterWiFiHTRxStream.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFiHTRxStream.setStatus(_A)
class _ArrisRouterWiFiEnableSTBC_Type(TruthValue):defaultValue=2
_ArrisRouterWiFiEnableSTBC_Type.__name__=_F
_ArrisRouterWiFiEnableSTBC_Object=MibScalar
arrisRouterWiFiEnableSTBC=_ArrisRouterWiFiEnableSTBC_Object((1,3,6,1,4,1,4115,1,20,1,1,3,57),_ArrisRouterWiFiEnableSTBC_Type())
arrisRouterWiFiEnableSTBC.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFiEnableSTBC.setStatus(_A)
class _ArrisRouterWiFiEnableRDG_Type(TruthValue):defaultValue=2
_ArrisRouterWiFiEnableRDG_Type.__name__=_F
_ArrisRouterWiFiEnableRDG_Object=MibScalar
arrisRouterWiFiEnableRDG=_ArrisRouterWiFiEnableRDG_Object((1,3,6,1,4,1,4115,1,20,1,1,3,58),_ArrisRouterWiFiEnableRDG_Type())
arrisRouterWiFiEnableRDG.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFiEnableRDG.setStatus(_A)
class _ArrisRouterWiFiIGMPSnooping_Type(TruthValue):defaultValue=2
_ArrisRouterWiFiIGMPSnooping_Type.__name__=_F
_ArrisRouterWiFiIGMPSnooping_Object=MibScalar
arrisRouterWiFiIGMPSnooping=_ArrisRouterWiFiIGMPSnooping_Object((1,3,6,1,4,1,4115,1,20,1,1,3,59),_ArrisRouterWiFiIGMPSnooping_Type())
arrisRouterWiFiIGMPSnooping.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFiIGMPSnooping.setStatus(_A)
class _ArrisRouterWiFiRTSRetry_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ArrisRouterWiFiRTSRetry_Type.__name__=_D
_ArrisRouterWiFiRTSRetry_Object=MibScalar
arrisRouterWiFiRTSRetry=_ArrisRouterWiFiRTSRetry_Object((1,3,6,1,4,1,4115,1,20,1,1,3,60),_ArrisRouterWiFiRTSRetry_Type())
arrisRouterWiFiRTSRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFiRTSRetry.setStatus(_A)
class _ArrisRouterWiFiTxRetry_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ArrisRouterWiFiTxRetry_Type.__name__=_D
_ArrisRouterWiFiTxRetry_Object=MibScalar
arrisRouterWiFiTxRetry=_ArrisRouterWiFiTxRetry_Object((1,3,6,1,4,1,4115,1,20,1,1,3,61),_ArrisRouterWiFiTxRetry_Type())
arrisRouterWiFiTxRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFiTxRetry.setStatus(_A)
_ArrisRouterWiFiPhysicalChannelStats_ObjectIdentity=ObjectIdentity
arrisRouterWiFiPhysicalChannelStats=_ArrisRouterWiFiPhysicalChannelStats_ObjectIdentity((1,3,6,1,4,1,4115,1,20,1,1,3,62))
class _ArrisRouterWiFiPhysicalChannelStatsEnable_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_O,0),('enable-2-4',1),('enable-5',2),('enable-all',3)))
_ArrisRouterWiFiPhysicalChannelStatsEnable_Type.__name__=_D
_ArrisRouterWiFiPhysicalChannelStatsEnable_Object=MibScalar
arrisRouterWiFiPhysicalChannelStatsEnable=_ArrisRouterWiFiPhysicalChannelStatsEnable_Object((1,3,6,1,4,1,4115,1,20,1,1,3,62,1),_ArrisRouterWiFiPhysicalChannelStatsEnable_Type())
arrisRouterWiFiPhysicalChannelStatsEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFiPhysicalChannelStatsEnable.setStatus(_A)
class _ArrisRouterWiFiPhysicalChannelStatsMeasurementRate_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,300))
_ArrisRouterWiFiPhysicalChannelStatsMeasurementRate_Type.__name__=_D
_ArrisRouterWiFiPhysicalChannelStatsMeasurementRate_Object=MibScalar
arrisRouterWiFiPhysicalChannelStatsMeasurementRate=_ArrisRouterWiFiPhysicalChannelStatsMeasurementRate_Object((1,3,6,1,4,1,4115,1,20,1,1,3,62,2),_ArrisRouterWiFiPhysicalChannelStatsMeasurementRate_Type())
arrisRouterWiFiPhysicalChannelStatsMeasurementRate.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFiPhysicalChannelStatsMeasurementRate.setStatus(_A)
class _ArrisRouterWiFiPhysicalChannelStatsMeasurementInterval_Type(Integer32):defaultValue=1800;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(300,3600))
_ArrisRouterWiFiPhysicalChannelStatsMeasurementInterval_Type.__name__=_D
_ArrisRouterWiFiPhysicalChannelStatsMeasurementInterval_Object=MibScalar
arrisRouterWiFiPhysicalChannelStatsMeasurementInterval=_ArrisRouterWiFiPhysicalChannelStatsMeasurementInterval_Object((1,3,6,1,4,1,4115,1,20,1,1,3,62,3),_ArrisRouterWiFiPhysicalChannelStatsMeasurementInterval_Type())
arrisRouterWiFiPhysicalChannelStatsMeasurementInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFiPhysicalChannelStatsMeasurementInterval.setStatus(_A)
_ArrisRouterChannelStatsMeasurementTable_Object=MibTable
arrisRouterChannelStatsMeasurementTable=_ArrisRouterChannelStatsMeasurementTable_Object((1,3,6,1,4,1,4115,1,20,1,1,3,62,4))
if mibBuilder.loadTexts:arrisRouterChannelStatsMeasurementTable.setStatus(_A)
_ArrisRouterChannelStatsMeasurementEntry_Object=MibTableRow
arrisRouterChannelStatsMeasurementEntry=_ArrisRouterChannelStatsMeasurementEntry_Object((1,3,6,1,4,1,4115,1,20,1,1,3,62,4,1))
arrisRouterChannelStatsMeasurementEntry.setIndexNames((0,_K,_L))
if mibBuilder.loadTexts:arrisRouterChannelStatsMeasurementEntry.setStatus(_A)
class _ArrisRouterChannelStatsMinNoiseFloor_Type(Integer32):defaultValue=-1
_ArrisRouterChannelStatsMinNoiseFloor_Type.__name__=_D
_ArrisRouterChannelStatsMinNoiseFloor_Object=MibTableColumn
arrisRouterChannelStatsMinNoiseFloor=_ArrisRouterChannelStatsMinNoiseFloor_Object((1,3,6,1,4,1,4115,1,20,1,1,3,62,4,1,1),_ArrisRouterChannelStatsMinNoiseFloor_Type())
arrisRouterChannelStatsMinNoiseFloor.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterChannelStatsMinNoiseFloor.setStatus(_A)
class _ArrisRouterChannelStatsMaxNoiseFloor_Type(Integer32):defaultValue=-1
_ArrisRouterChannelStatsMaxNoiseFloor_Type.__name__=_D
_ArrisRouterChannelStatsMaxNoiseFloor_Object=MibTableColumn
arrisRouterChannelStatsMaxNoiseFloor=_ArrisRouterChannelStatsMaxNoiseFloor_Object((1,3,6,1,4,1,4115,1,20,1,1,3,62,4,1,2),_ArrisRouterChannelStatsMaxNoiseFloor_Type())
arrisRouterChannelStatsMaxNoiseFloor.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterChannelStatsMaxNoiseFloor.setStatus(_A)
class _ArrisRouterChannelStatsMedianNoiseFloor_Type(Integer32):defaultValue=-1
_ArrisRouterChannelStatsMedianNoiseFloor_Type.__name__=_D
_ArrisRouterChannelStatsMedianNoiseFloor_Object=MibTableColumn
arrisRouterChannelStatsMedianNoiseFloor=_ArrisRouterChannelStatsMedianNoiseFloor_Object((1,3,6,1,4,1,4115,1,20,1,1,3,62,4,1,3),_ArrisRouterChannelStatsMedianNoiseFloor_Type())
arrisRouterChannelStatsMedianNoiseFloor.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterChannelStatsMedianNoiseFloor.setStatus(_A)
class _ArrisRouterChannelStatsPacketsSent_Type(Counter64):defaultValue=0
_ArrisRouterChannelStatsPacketsSent_Type.__name__=_d
_ArrisRouterChannelStatsPacketsSent_Object=MibTableColumn
arrisRouterChannelStatsPacketsSent=_ArrisRouterChannelStatsPacketsSent_Object((1,3,6,1,4,1,4115,1,20,1,1,3,62,4,1,4),_ArrisRouterChannelStatsPacketsSent_Type())
arrisRouterChannelStatsPacketsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterChannelStatsPacketsSent.setStatus(_A)
class _ArrisRouterChannelStatsPacketsReceived_Type(Counter64):defaultValue=0
_ArrisRouterChannelStatsPacketsReceived_Type.__name__=_d
_ArrisRouterChannelStatsPacketsReceived_Object=MibTableColumn
arrisRouterChannelStatsPacketsReceived=_ArrisRouterChannelStatsPacketsReceived_Object((1,3,6,1,4,1,4115,1,20,1,1,3,62,4,1,5),_ArrisRouterChannelStatsPacketsReceived_Type())
arrisRouterChannelStatsPacketsReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterChannelStatsPacketsReceived.setStatus(_A)
class _ArrisRouterChannelStatsCSTExceedPercent_Type(Integer32):defaultValue=-1
_ArrisRouterChannelStatsCSTExceedPercent_Type.__name__=_D
_ArrisRouterChannelStatsCSTExceedPercent_Object=MibTableColumn
arrisRouterChannelStatsCSTExceedPercent=_ArrisRouterChannelStatsCSTExceedPercent_Object((1,3,6,1,4,1,4115,1,20,1,1,3,62,4,1,6),_ArrisRouterChannelStatsCSTExceedPercent_Type())
arrisRouterChannelStatsCSTExceedPercent.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterChannelStatsCSTExceedPercent.setStatus(_A)
class _ArrisRouterChannelStatsActivityFactor_Type(Integer32):defaultValue=-1
_ArrisRouterChannelStatsActivityFactor_Type.__name__=_D
_ArrisRouterChannelStatsActivityFactor_Object=MibTableColumn
arrisRouterChannelStatsActivityFactor=_ArrisRouterChannelStatsActivityFactor_Object((1,3,6,1,4,1,4115,1,20,1,1,3,62,4,1,7),_ArrisRouterChannelStatsActivityFactor_Type())
arrisRouterChannelStatsActivityFactor.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterChannelStatsActivityFactor.setStatus(_A)
class _ArrisRouterChannelStatsChannelUtilization_Type(Integer32):defaultValue=-1
_ArrisRouterChannelStatsChannelUtilization_Type.__name__=_D
_ArrisRouterChannelStatsChannelUtilization_Object=MibTableColumn
arrisRouterChannelStatsChannelUtilization=_ArrisRouterChannelStatsChannelUtilization_Object((1,3,6,1,4,1,4115,1,20,1,1,3,62,4,1,8),_ArrisRouterChannelStatsChannelUtilization_Type())
arrisRouterChannelStatsChannelUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterChannelStatsChannelUtilization.setStatus(_A)
class _ArrisRouterChannelStatsRetransmissionsMetric_Type(Integer32):defaultValue=-1
_ArrisRouterChannelStatsRetransmissionsMetric_Type.__name__=_D
_ArrisRouterChannelStatsRetransmissionsMetric_Object=MibTableColumn
arrisRouterChannelStatsRetransmissionsMetric=_ArrisRouterChannelStatsRetransmissionsMetric_Object((1,3,6,1,4,1,4115,1,20,1,1,3,62,4,1,9),_ArrisRouterChannelStatsRetransmissionsMetric_Type())
arrisRouterChannelStatsRetransmissionsMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterChannelStatsRetransmissionsMetric.setStatus(_A)
_ArrisRouterChannelStatsRSSITable_Object=MibTable
arrisRouterChannelStatsRSSITable=_ArrisRouterChannelStatsRSSITable_Object((1,3,6,1,4,1,4115,1,20,1,1,3,62,5))
if mibBuilder.loadTexts:arrisRouterChannelStatsRSSITable.setStatus(_A)
_ArrisRouterChannelStatsRSSITableEntry_Object=MibTableRow
arrisRouterChannelStatsRSSITableEntry=_ArrisRouterChannelStatsRSSITableEntry_Object((1,3,6,1,4,1,4115,1,20,1,1,3,62,5,1))
arrisRouterChannelStatsRSSITableEntry.setIndexNames((0,_K,_L),(0,_I,_Am))
if mibBuilder.loadTexts:arrisRouterChannelStatsRSSITableEntry.setStatus(_A)
class _ArrisRouterChannelStatsRSSITableIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,40))
_ArrisRouterChannelStatsRSSITableIndex_Type.__name__=_D
_ArrisRouterChannelStatsRSSITableIndex_Object=MibTableColumn
arrisRouterChannelStatsRSSITableIndex=_ArrisRouterChannelStatsRSSITableIndex_Object((1,3,6,1,4,1,4115,1,20,1,1,3,62,5,1,1),_ArrisRouterChannelStatsRSSITableIndex_Type())
arrisRouterChannelStatsRSSITableIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:arrisRouterChannelStatsRSSITableIndex.setStatus(_A)
class _ArrisRouterChannelStatsRSSICount_Type(Integer32):defaultValue=-1
_ArrisRouterChannelStatsRSSICount_Type.__name__=_D
_ArrisRouterChannelStatsRSSICount_Object=MibTableColumn
arrisRouterChannelStatsRSSICount=_ArrisRouterChannelStatsRSSICount_Object((1,3,6,1,4,1,4115,1,20,1,1,3,62,5,1,2),_ArrisRouterChannelStatsRSSICount_Type())
arrisRouterChannelStatsRSSICount.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterChannelStatsRSSICount.setStatus(_A)
_ArrisRouterWMM50Cfg_ObjectIdentity=ObjectIdentity
arrisRouterWMM50Cfg=_ArrisRouterWMM50Cfg_ObjectIdentity((1,3,6,1,4,1,4115,1,20,1,1,3,63))
class _ArrisRouterWMM50Enable_Type(TruthValue):defaultValue=1
_ArrisRouterWMM50Enable_Type.__name__=_F
_ArrisRouterWMM50Enable_Object=MibScalar
arrisRouterWMM50Enable=_ArrisRouterWMM50Enable_Object((1,3,6,1,4,1,4115,1,20,1,1,3,63,1),_ArrisRouterWMM50Enable_Type())
arrisRouterWMM50Enable.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWMM50Enable.setStatus(_A)
class _ArrisRouterWMM50NoAck_Type(TruthValue):defaultValue=2
_ArrisRouterWMM50NoAck_Type.__name__=_F
_ArrisRouterWMM50NoAck_Object=MibScalar
arrisRouterWMM50NoAck=_ArrisRouterWMM50NoAck_Object((1,3,6,1,4,1,4115,1,20,1,1,3,63,2),_ArrisRouterWMM50NoAck_Type())
arrisRouterWMM50NoAck.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWMM50NoAck.setStatus(_A)
class _ArrisRouterWMM50APSD_Type(TruthValue):defaultValue=1
_ArrisRouterWMM50APSD_Type.__name__=_F
_ArrisRouterWMM50APSD_Object=MibScalar
arrisRouterWMM50APSD=_ArrisRouterWMM50APSD_Object((1,3,6,1,4,1,4115,1,20,1,1,3,63,3),_ArrisRouterWMM50APSD_Type())
arrisRouterWMM50APSD.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWMM50APSD.setStatus(_A)
_ArrisRouterWMM50EDCAAPTable_Object=MibTable
arrisRouterWMM50EDCAAPTable=_ArrisRouterWMM50EDCAAPTable_Object((1,3,6,1,4,1,4115,1,20,1,1,3,63,4))
if mibBuilder.loadTexts:arrisRouterWMM50EDCAAPTable.setStatus(_A)
_ArrisRouterWMM50EDCAAPEntry_Object=MibTableRow
arrisRouterWMM50EDCAAPEntry=_ArrisRouterWMM50EDCAAPEntry_Object((1,3,6,1,4,1,4115,1,20,1,1,3,63,4,1))
arrisRouterWMM50EDCAAPEntry.setIndexNames((0,_I,_An))
if mibBuilder.loadTexts:arrisRouterWMM50EDCAAPEntry.setStatus(_A)
class _ArrisRouterWMM50EDCAAPIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_ArrisRouterWMM50EDCAAPIndex_Type.__name__=_D
_ArrisRouterWMM50EDCAAPIndex_Object=MibTableColumn
arrisRouterWMM50EDCAAPIndex=_ArrisRouterWMM50EDCAAPIndex_Object((1,3,6,1,4,1,4115,1,20,1,1,3,63,4,1,1),_ArrisRouterWMM50EDCAAPIndex_Type())
arrisRouterWMM50EDCAAPIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:arrisRouterWMM50EDCAAPIndex.setStatus(_A)
_ArrisRouterWMM50EDCAAPCWmin_Type=Unsigned32
_ArrisRouterWMM50EDCAAPCWmin_Object=MibTableColumn
arrisRouterWMM50EDCAAPCWmin=_ArrisRouterWMM50EDCAAPCWmin_Object((1,3,6,1,4,1,4115,1,20,1,1,3,63,4,1,2),_ArrisRouterWMM50EDCAAPCWmin_Type())
arrisRouterWMM50EDCAAPCWmin.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWMM50EDCAAPCWmin.setStatus(_A)
if mibBuilder.loadTexts:arrisRouterWMM50EDCAAPCWmin.setUnits(_P)
_ArrisRouterWMM50EDCAAPCWmax_Type=Unsigned32
_ArrisRouterWMM50EDCAAPCWmax_Object=MibTableColumn
arrisRouterWMM50EDCAAPCWmax=_ArrisRouterWMM50EDCAAPCWmax_Object((1,3,6,1,4,1,4115,1,20,1,1,3,63,4,1,3),_ArrisRouterWMM50EDCAAPCWmax_Type())
arrisRouterWMM50EDCAAPCWmax.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWMM50EDCAAPCWmax.setStatus(_A)
if mibBuilder.loadTexts:arrisRouterWMM50EDCAAPCWmax.setUnits(_P)
_ArrisRouterWMM50EDCAAPAIFSN_Type=Unsigned32
_ArrisRouterWMM50EDCAAPAIFSN_Object=MibTableColumn
arrisRouterWMM50EDCAAPAIFSN=_ArrisRouterWMM50EDCAAPAIFSN_Object((1,3,6,1,4,1,4115,1,20,1,1,3,63,4,1,4),_ArrisRouterWMM50EDCAAPAIFSN_Type())
arrisRouterWMM50EDCAAPAIFSN.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWMM50EDCAAPAIFSN.setStatus(_A)
if mibBuilder.loadTexts:arrisRouterWMM50EDCAAPAIFSN.setUnits(_P)
class _ArrisRouterWMM50EDCAAPTxOpBLimit_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ArrisRouterWMM50EDCAAPTxOpBLimit_Type.__name__=_H
_ArrisRouterWMM50EDCAAPTxOpBLimit_Object=MibTableColumn
arrisRouterWMM50EDCAAPTxOpBLimit=_ArrisRouterWMM50EDCAAPTxOpBLimit_Object((1,3,6,1,4,1,4115,1,20,1,1,3,63,4,1,5),_ArrisRouterWMM50EDCAAPTxOpBLimit_Type())
arrisRouterWMM50EDCAAPTxOpBLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWMM50EDCAAPTxOpBLimit.setStatus(_A)
if mibBuilder.loadTexts:arrisRouterWMM50EDCAAPTxOpBLimit.setUnits(_Z)
class _ArrisRouterWMM50EDCAAPTxOpAGLimit_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ArrisRouterWMM50EDCAAPTxOpAGLimit_Type.__name__=_H
_ArrisRouterWMM50EDCAAPTxOpAGLimit_Object=MibTableColumn
arrisRouterWMM50EDCAAPTxOpAGLimit=_ArrisRouterWMM50EDCAAPTxOpAGLimit_Object((1,3,6,1,4,1,4115,1,20,1,1,3,63,4,1,6),_ArrisRouterWMM50EDCAAPTxOpAGLimit_Type())
arrisRouterWMM50EDCAAPTxOpAGLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWMM50EDCAAPTxOpAGLimit.setStatus(_A)
if mibBuilder.loadTexts:arrisRouterWMM50EDCAAPTxOpAGLimit.setUnits(_Z)
_ArrisRouterWMM50EDCAAPAdmitCont_Type=TruthValue
_ArrisRouterWMM50EDCAAPAdmitCont_Object=MibTableColumn
arrisRouterWMM50EDCAAPAdmitCont=_ArrisRouterWMM50EDCAAPAdmitCont_Object((1,3,6,1,4,1,4115,1,20,1,1,3,63,4,1,7),_ArrisRouterWMM50EDCAAPAdmitCont_Type())
arrisRouterWMM50EDCAAPAdmitCont.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWMM50EDCAAPAdmitCont.setStatus(_A)
_ArrisRouterWMM50EDCAAPDiscardOld_Type=TruthValue
_ArrisRouterWMM50EDCAAPDiscardOld_Object=MibTableColumn
arrisRouterWMM50EDCAAPDiscardOld=_ArrisRouterWMM50EDCAAPDiscardOld_Object((1,3,6,1,4,1,4115,1,20,1,1,3,63,4,1,8),_ArrisRouterWMM50EDCAAPDiscardOld_Type())
arrisRouterWMM50EDCAAPDiscardOld.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWMM50EDCAAPDiscardOld.setStatus(_A)
class _ArrisRouterWiFiExtensionChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('belowControlChannel',0),('aboveControlChannel',1),(_R,2)))
_ArrisRouterWiFiExtensionChannel_Type.__name__=_D
_ArrisRouterWiFiExtensionChannel_Object=MibScalar
arrisRouterWiFiExtensionChannel=_ArrisRouterWiFiExtensionChannel_Object((1,3,6,1,4,1,4115,1,20,1,1,3,64),_ArrisRouterWiFiExtensionChannel_Type())
arrisRouterWiFiExtensionChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFiExtensionChannel.setStatus(_A)
_ArrisRouterWPS50Cfg_ObjectIdentity=ObjectIdentity
arrisRouterWPS50Cfg=_ArrisRouterWPS50Cfg_ObjectIdentity((1,3,6,1,4,1,4115,1,20,1,1,3,65))
class _ArrisRouterWps50Mode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_O,0),(_Q,1)))
_ArrisRouterWps50Mode_Type.__name__=_D
_ArrisRouterWps50Mode_Object=MibScalar
arrisRouterWps50Mode=_ArrisRouterWps50Mode_Object((1,3,6,1,4,1,4115,1,20,1,1,3,65,1),_ArrisRouterWps50Mode_Type())
arrisRouterWps50Mode.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWps50Mode.setStatus(_A)
class _ArrisRouterWps50ConfigState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_O,0),(_Q,1)))
_ArrisRouterWps50ConfigState_Type.__name__=_D
_ArrisRouterWps50ConfigState_Object=MibScalar
arrisRouterWps50ConfigState=_ArrisRouterWps50ConfigState_Object((1,3,6,1,4,1,4115,1,20,1,1,3,65,2),_ArrisRouterWps50ConfigState_Type())
arrisRouterWps50ConfigState.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWps50ConfigState.setStatus(_A)
class _ArrisRouterWps50DevicePIN_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ArrisRouterWps50DevicePIN_Type.__name__=_G
_ArrisRouterWps50DevicePIN_Object=MibScalar
arrisRouterWps50DevicePIN=_ArrisRouterWps50DevicePIN_Object((1,3,6,1,4,1,4115,1,20,1,1,3,65,3),_ArrisRouterWps50DevicePIN_Type())
arrisRouterWps50DevicePIN.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWps50DevicePIN.setStatus(_A)
class _ArrisRouterWps50DeviceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ArrisRouterWps50DeviceName_Type.__name__=_G
_ArrisRouterWps50DeviceName_Object=MibScalar
arrisRouterWps50DeviceName=_ArrisRouterWps50DeviceName_Object((1,3,6,1,4,1,4115,1,20,1,1,3,65,4),_ArrisRouterWps50DeviceName_Type())
arrisRouterWps50DeviceName.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWps50DeviceName.setStatus(_A)
class _ArrisRouterWps50ModelName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ArrisRouterWps50ModelName_Type.__name__=_G
_ArrisRouterWps50ModelName_Object=MibScalar
arrisRouterWps50ModelName=_ArrisRouterWps50ModelName_Object((1,3,6,1,4,1,4115,1,20,1,1,3,65,5),_ArrisRouterWps50ModelName_Type())
arrisRouterWps50ModelName.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWps50ModelName.setStatus(_A)
class _ArrisRouterWps50Mfg_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ArrisRouterWps50Mfg_Type.__name__=_G
_ArrisRouterWps50Mfg_Object=MibScalar
arrisRouterWps50Mfg=_ArrisRouterWps50Mfg_Object((1,3,6,1,4,1,4115,1,20,1,1,3,65,6),_ArrisRouterWps50Mfg_Type())
arrisRouterWps50Mfg.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWps50Mfg.setStatus(_A)
class _ArrisRouterWps50ResultStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,0,1,2,3,4,5,6)));namedValues=NamedValues(*((_AN,-1),(_AO,0),(_AP,1),(_AQ,2),(_AR,3),(_AS,4),(_AT,5),(_AU,6)))
_ArrisRouterWps50ResultStatus_Type.__name__=_D
_ArrisRouterWps50ResultStatus_Object=MibScalar
arrisRouterWps50ResultStatus=_ArrisRouterWps50ResultStatus_Object((1,3,6,1,4,1,4115,1,20,1,1,3,65,7),_ArrisRouterWps50ResultStatus_Type())
arrisRouterWps50ResultStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWps50ResultStatus.setStatus(_A)
class _ArrisRouterWps50Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,0,1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_AV,-1),(_AW,0),(_AX,1),(_AY,2),(_AZ,3),(_Aa,4),(_Ab,5),(_Ac,6),(_Ad,7),(_Ae,8),(_Af,9),(_Ag,10)))
_ArrisRouterWps50Status_Type.__name__=_D
_ArrisRouterWps50Status_Object=MibScalar
arrisRouterWps50Status=_ArrisRouterWps50Status_Object((1,3,6,1,4,1,4115,1,20,1,1,3,65,8),_ArrisRouterWps50Status_Type())
arrisRouterWps50Status.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWps50Status.setStatus(_A)
class _ArrisRouterWps50ConfigTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_O,0),(_Q,1)))
_ArrisRouterWps50ConfigTimeout_Type.__name__=_D
_ArrisRouterWps50ConfigTimeout_Object=MibScalar
arrisRouterWps50ConfigTimeout=_ArrisRouterWps50ConfigTimeout_Object((1,3,6,1,4,1,4115,1,20,1,1,3,65,9),_ArrisRouterWps50ConfigTimeout_Type())
arrisRouterWps50ConfigTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWps50ConfigTimeout.setStatus(_A)
class _ArrisRouterWps50STAPin_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ArrisRouterWps50STAPin_Type.__name__=_G
_ArrisRouterWps50STAPin_Object=MibScalar
arrisRouterWps50STAPin=_ArrisRouterWps50STAPin_Object((1,3,6,1,4,1,4115,1,20,1,1,3,65,10),_ArrisRouterWps50STAPin_Type())
arrisRouterWps50STAPin.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWps50STAPin.setStatus(_A)
class _ArrisRouterWps50PushButton_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_N,0),(_Ah,1),(_Ai,2),(_Aj,3)))
_ArrisRouterWps50PushButton_Type.__name__=_D
_ArrisRouterWps50PushButton_Object=MibScalar
arrisRouterWps50PushButton=_ArrisRouterWps50PushButton_Object((1,3,6,1,4,1,4115,1,20,1,1,3,65,11),_ArrisRouterWps50PushButton_Type())
arrisRouterWps50PushButton.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWps50PushButton.setStatus(_A)
class _ArrisRouterWps50UUID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_ArrisRouterWps50UUID_Type.__name__=_G
_ArrisRouterWps50UUID_Object=MibScalar
arrisRouterWps50UUID=_ArrisRouterWps50UUID_Object((1,3,6,1,4,1,4115,1,20,1,1,3,65,14),_ArrisRouterWps50UUID_Type())
arrisRouterWps50UUID.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWps50UUID.setStatus(_A)
class _ArrisRouterWifiLowInitRate_Type(TruthValue):defaultValue=2
_ArrisRouterWifiLowInitRate_Type.__name__=_F
_ArrisRouterWifiLowInitRate_Object=MibScalar
arrisRouterWifiLowInitRate=_ArrisRouterWifiLowInitRate_Object((1,3,6,1,4,1,4115,1,20,1,1,3,66),_ArrisRouterWifiLowInitRate_Type())
arrisRouterWifiLowInitRate.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWifiLowInitRate.setStatus(_A)
_ArrisRouterWiFiBssStaSteering_ObjectIdentity=ObjectIdentity
arrisRouterWiFiBssStaSteering=_ArrisRouterWiFiBssStaSteering_ObjectIdentity((1,3,6,1,4,1,4115,1,20,1,1,3,69))
class _ArrisRouterWiFiBssStaSteeringReset_Type(TruthValue):defaultValue=2
_ArrisRouterWiFiBssStaSteeringReset_Type.__name__=_F
_ArrisRouterWiFiBssStaSteeringReset_Object=MibScalar
arrisRouterWiFiBssStaSteeringReset=_ArrisRouterWiFiBssStaSteeringReset_Object((1,3,6,1,4,1,4115,1,20,1,1,3,69,1),_ArrisRouterWiFiBssStaSteeringReset_Type())
arrisRouterWiFiBssStaSteeringReset.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFiBssStaSteeringReset.setStatus(_A)
class _ArrisRouterWiFiBssStaSteeringDenyCount_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_ArrisRouterWiFiBssStaSteeringDenyCount_Type.__name__=_D
_ArrisRouterWiFiBssStaSteeringDenyCount_Object=MibScalar
arrisRouterWiFiBssStaSteeringDenyCount=_ArrisRouterWiFiBssStaSteeringDenyCount_Object((1,3,6,1,4,1,4115,1,20,1,1,3,69,2),_ArrisRouterWiFiBssStaSteeringDenyCount_Type())
arrisRouterWiFiBssStaSteeringDenyCount.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFiBssStaSteeringDenyCount.setStatus(_A)
class _ArrisRouterWiFiBssStaSteeringDenyWindow_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,120))
_ArrisRouterWiFiBssStaSteeringDenyWindow_Type.__name__=_D
_ArrisRouterWiFiBssStaSteeringDenyWindow_Object=MibScalar
arrisRouterWiFiBssStaSteeringDenyWindow=_ArrisRouterWiFiBssStaSteeringDenyWindow_Object((1,3,6,1,4,1,4115,1,20,1,1,3,69,3),_ArrisRouterWiFiBssStaSteeringDenyWindow_Type())
arrisRouterWiFiBssStaSteeringDenyWindow.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFiBssStaSteeringDenyWindow.setStatus(_A)
_ArrisRouterBssStaSteeringTable_Object=MibTable
arrisRouterBssStaSteeringTable=_ArrisRouterBssStaSteeringTable_Object((1,3,6,1,4,1,4115,1,20,1,1,3,69,4))
if mibBuilder.loadTexts:arrisRouterBssStaSteeringTable.setStatus(_A)
_ArrisRouterBssStaSteeringEntry_Object=MibTableRow
arrisRouterBssStaSteeringEntry=_ArrisRouterBssStaSteeringEntry_Object((1,3,6,1,4,1,4115,1,20,1,1,3,69,4,1))
arrisRouterBssStaSteeringEntry.setIndexNames((0,_K,_L))
if mibBuilder.loadTexts:arrisRouterBssStaSteeringEntry.setStatus(_A)
class _ArrisRouterBssStaSteeringIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_ArrisRouterBssStaSteeringIndex_Type.__name__=_D
_ArrisRouterBssStaSteeringIndex_Object=MibTableColumn
arrisRouterBssStaSteeringIndex=_ArrisRouterBssStaSteeringIndex_Object((1,3,6,1,4,1,4115,1,20,1,1,3,69,4,1,1),_ArrisRouterBssStaSteeringIndex_Type())
arrisRouterBssStaSteeringIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:arrisRouterBssStaSteeringIndex.setStatus(_A)
class _ArrisRouterBssStaSteeringTableClear_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_ArrisRouterBssStaSteeringTableClear_Type.__name__=_D
_ArrisRouterBssStaSteeringTableClear_Object=MibTableColumn
arrisRouterBssStaSteeringTableClear=_ArrisRouterBssStaSteeringTableClear_Object((1,3,6,1,4,1,4115,1,20,1,1,3,69,4,1,2),_ArrisRouterBssStaSteeringTableClear_Type())
arrisRouterBssStaSteeringTableClear.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterBssStaSteeringTableClear.setStatus(_A)
class _ArrisRouterBssStaSteeringTableDenyCount_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_ArrisRouterBssStaSteeringTableDenyCount_Type.__name__=_D
_ArrisRouterBssStaSteeringTableDenyCount_Object=MibTableColumn
arrisRouterBssStaSteeringTableDenyCount=_ArrisRouterBssStaSteeringTableDenyCount_Object((1,3,6,1,4,1,4115,1,20,1,1,3,69,4,1,3),_ArrisRouterBssStaSteeringTableDenyCount_Type())
arrisRouterBssStaSteeringTableDenyCount.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterBssStaSteeringTableDenyCount.setStatus(_A)
class _ArrisRouterBssStaSteeringTableDenyWindow_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,120))
_ArrisRouterBssStaSteeringTableDenyWindow_Type.__name__=_D
_ArrisRouterBssStaSteeringTableDenyWindow_Object=MibTableColumn
arrisRouterBssStaSteeringTableDenyWindow=_ArrisRouterBssStaSteeringTableDenyWindow_Object((1,3,6,1,4,1,4115,1,20,1,1,3,69,4,1,4),_ArrisRouterBssStaSteeringTableDenyWindow_Type())
arrisRouterBssStaSteeringTableDenyWindow.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterBssStaSteeringTableDenyWindow.setStatus(_A)
_ArrisRouterBssStaSteeringTableStatus_Type=RowStatus
_ArrisRouterBssStaSteeringTableStatus_Object=MibTableColumn
arrisRouterBssStaSteeringTableStatus=_ArrisRouterBssStaSteeringTableStatus_Object((1,3,6,1,4,1,4115,1,20,1,1,3,69,4,1,5),_ArrisRouterBssStaSteeringTableStatus_Type())
arrisRouterBssStaSteeringTableStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterBssStaSteeringTableStatus.setStatus(_A)
_ArrisRouterBssStaSteeringClientTable_Object=MibTable
arrisRouterBssStaSteeringClientTable=_ArrisRouterBssStaSteeringClientTable_Object((1,3,6,1,4,1,4115,1,20,1,1,3,69,5))
if mibBuilder.loadTexts:arrisRouterBssStaSteeringClientTable.setStatus(_A)
_ArrisRouterBssStaSteeringClientEntry_Object=MibTableRow
arrisRouterBssStaSteeringClientEntry=_ArrisRouterBssStaSteeringClientEntry_Object((1,3,6,1,4,1,4115,1,20,1,1,3,69,5,1))
arrisRouterBssStaSteeringClientEntry.setIndexNames((0,_K,_L),(0,_I,_Ao))
if mibBuilder.loadTexts:arrisRouterBssStaSteeringClientEntry.setStatus(_A)
class _ArrisRouterBssStaSteeringClientIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_ArrisRouterBssStaSteeringClientIndex_Type.__name__=_D
_ArrisRouterBssStaSteeringClientIndex_Object=MibTableColumn
arrisRouterBssStaSteeringClientIndex=_ArrisRouterBssStaSteeringClientIndex_Object((1,3,6,1,4,1,4115,1,20,1,1,3,69,5,1,1),_ArrisRouterBssStaSteeringClientIndex_Type())
arrisRouterBssStaSteeringClientIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:arrisRouterBssStaSteeringClientIndex.setStatus(_A)
_ArrisRouterBssStaSteeringClientMacAddress_Type=MacAddress
_ArrisRouterBssStaSteeringClientMacAddress_Object=MibTableColumn
arrisRouterBssStaSteeringClientMacAddress=_ArrisRouterBssStaSteeringClientMacAddress_Object((1,3,6,1,4,1,4115,1,20,1,1,3,69,5,1,2),_ArrisRouterBssStaSteeringClientMacAddress_Type())
arrisRouterBssStaSteeringClientMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterBssStaSteeringClientMacAddress.setStatus(_A)
_ArrisRouterBssStaSteeringClientLastAssocTime_Type=DateAndTime
_ArrisRouterBssStaSteeringClientLastAssocTime_Object=MibTableColumn
arrisRouterBssStaSteeringClientLastAssocTime=_ArrisRouterBssStaSteeringClientLastAssocTime_Object((1,3,6,1,4,1,4115,1,20,1,1,3,69,5,1,3),_ArrisRouterBssStaSteeringClientLastAssocTime_Type())
arrisRouterBssStaSteeringClientLastAssocTime.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterBssStaSteeringClientLastAssocTime.setStatus(_A)
_ArrisRouterBssStaSteeringClientOtherBssJoinedCount_Type=Integer32
_ArrisRouterBssStaSteeringClientOtherBssJoinedCount_Object=MibTableColumn
arrisRouterBssStaSteeringClientOtherBssJoinedCount=_ArrisRouterBssStaSteeringClientOtherBssJoinedCount_Object((1,3,6,1,4,1,4115,1,20,1,1,3,69,5,1,4),_ArrisRouterBssStaSteeringClientOtherBssJoinedCount_Type())
arrisRouterBssStaSteeringClientOtherBssJoinedCount.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterBssStaSteeringClientOtherBssJoinedCount.setStatus(_A)
class _ArrisRouterWiFiInterworkingIE_Type(TruthValue):defaultValue=1
_ArrisRouterWiFiInterworkingIE_Type.__name__=_F
_ArrisRouterWiFiInterworkingIE_Object=MibScalar
arrisRouterWiFiInterworkingIE=_ArrisRouterWiFiInterworkingIE_Object((1,3,6,1,4,1,4115,1,20,1,1,3,70),_ArrisRouterWiFiInterworkingIE_Type())
arrisRouterWiFiInterworkingIE.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWiFiInterworkingIE.setStatus(_A)
_ArrisRouterAirtimeCtrlCfg_ObjectIdentity=ObjectIdentity
arrisRouterAirtimeCtrlCfg=_ArrisRouterAirtimeCtrlCfg_ObjectIdentity((1,3,6,1,4,1,4115,1,20,1,1,3,99))
class _ArrisRouterAirtimeCtrlBSSIDEnable_Type(TruthValue):defaultValue=2
_ArrisRouterAirtimeCtrlBSSIDEnable_Type.__name__=_F
_ArrisRouterAirtimeCtrlBSSIDEnable_Object=MibScalar
arrisRouterAirtimeCtrlBSSIDEnable=_ArrisRouterAirtimeCtrlBSSIDEnable_Object((1,3,6,1,4,1,4115,1,20,1,1,3,99,1),_ArrisRouterAirtimeCtrlBSSIDEnable_Type())
arrisRouterAirtimeCtrlBSSIDEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterAirtimeCtrlBSSIDEnable.setStatus(_A)
_ArrisRouterAirtimeCtrlBSSIDWeightTable_Object=MibTable
arrisRouterAirtimeCtrlBSSIDWeightTable=_ArrisRouterAirtimeCtrlBSSIDWeightTable_Object((1,3,6,1,4,1,4115,1,20,1,1,3,99,2))
if mibBuilder.loadTexts:arrisRouterAirtimeCtrlBSSIDWeightTable.setStatus(_A)
_ArrisRouterAirtimeCtrlBSSIDWeightEntry_Object=MibTableRow
arrisRouterAirtimeCtrlBSSIDWeightEntry=_ArrisRouterAirtimeCtrlBSSIDWeightEntry_Object((1,3,6,1,4,1,4115,1,20,1,1,3,99,2,1))
arrisRouterAirtimeCtrlBSSIDWeightEntry.setIndexNames((0,_K,_L))
if mibBuilder.loadTexts:arrisRouterAirtimeCtrlBSSIDWeightEntry.setStatus(_A)
class _ArrisRouterAirtimeCtrlBSSIDWeightGuaranteedPercentage_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ArrisRouterAirtimeCtrlBSSIDWeightGuaranteedPercentage_Type.__name__=_H
_ArrisRouterAirtimeCtrlBSSIDWeightGuaranteedPercentage_Object=MibTableColumn
arrisRouterAirtimeCtrlBSSIDWeightGuaranteedPercentage=_ArrisRouterAirtimeCtrlBSSIDWeightGuaranteedPercentage_Object((1,3,6,1,4,1,4115,1,20,1,1,3,99,2,1,1),_ArrisRouterAirtimeCtrlBSSIDWeightGuaranteedPercentage_Type())
arrisRouterAirtimeCtrlBSSIDWeightGuaranteedPercentage.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterAirtimeCtrlBSSIDWeightGuaranteedPercentage.setStatus(_A)
class _ArrisRouterAirtimeCtrlBSSIDWeightMaximumPercentage_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ArrisRouterAirtimeCtrlBSSIDWeightMaximumPercentage_Type.__name__=_H
_ArrisRouterAirtimeCtrlBSSIDWeightMaximumPercentage_Object=MibTableColumn
arrisRouterAirtimeCtrlBSSIDWeightMaximumPercentage=_ArrisRouterAirtimeCtrlBSSIDWeightMaximumPercentage_Object((1,3,6,1,4,1,4115,1,20,1,1,3,99,2,1,2),_ArrisRouterAirtimeCtrlBSSIDWeightMaximumPercentage_Type())
arrisRouterAirtimeCtrlBSSIDWeightMaximumPercentage.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterAirtimeCtrlBSSIDWeightMaximumPercentage.setStatus(_A)
_ArrisRouterFWCfg_ObjectIdentity=ObjectIdentity
arrisRouterFWCfg=_ArrisRouterFWCfg_ObjectIdentity((1,3,6,1,4,1,4115,1,20,1,1,4))
class _ArrisRouterFWEnabled_Type(TruthValue):defaultValue=1
_ArrisRouterFWEnabled_Type.__name__=_F
_ArrisRouterFWEnabled_Object=MibScalar
arrisRouterFWEnabled=_ArrisRouterFWEnabled_Object((1,3,6,1,4,1,4115,1,20,1,1,4,1),_ArrisRouterFWEnabled_Type())
arrisRouterFWEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterFWEnabled.setStatus(_A)
_ArrisRouterFWEnableDMZ_Type=TruthValue
_ArrisRouterFWEnableDMZ_Object=MibScalar
arrisRouterFWEnableDMZ=_ArrisRouterFWEnableDMZ_Object((1,3,6,1,4,1,4115,1,20,1,1,4,6),_ArrisRouterFWEnableDMZ_Type())
arrisRouterFWEnableDMZ.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterFWEnableDMZ.setStatus(_A)
_ArrisRouterFWIPAddrTypeDMZ_Type=InetAddressType
_ArrisRouterFWIPAddrTypeDMZ_Object=MibScalar
arrisRouterFWIPAddrTypeDMZ=_ArrisRouterFWIPAddrTypeDMZ_Object((1,3,6,1,4,1,4115,1,20,1,1,4,7),_ArrisRouterFWIPAddrTypeDMZ_Type())
arrisRouterFWIPAddrTypeDMZ.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterFWIPAddrTypeDMZ.setStatus(_A)
_ArrisRouterFWIPAddrDMZ_Type=InetAddress
_ArrisRouterFWIPAddrDMZ_Object=MibScalar
arrisRouterFWIPAddrDMZ=_ArrisRouterFWIPAddrDMZ_Object((1,3,6,1,4,1,4115,1,20,1,1,4,8),_ArrisRouterFWIPAddrDMZ_Type())
arrisRouterFWIPAddrDMZ.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterFWIPAddrDMZ.setStatus(_A)
class _ArrisRouterFWSecurityLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('minimum',1),('medium',2),('maximum',3),('custom',4)))
_ArrisRouterFWSecurityLevel_Type.__name__=_D
_ArrisRouterFWSecurityLevel_Object=MibScalar
arrisRouterFWSecurityLevel=_ArrisRouterFWSecurityLevel_Object((1,3,6,1,4,1,4115,1,20,1,1,4,9),_ArrisRouterFWSecurityLevel_Type())
arrisRouterFWSecurityLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterFWSecurityLevel.setStatus(_A)
_ArrisRouterFWVirtSrvTable_Object=MibTable
arrisRouterFWVirtSrvTable=_ArrisRouterFWVirtSrvTable_Object((1,3,6,1,4,1,4115,1,20,1,1,4,12))
if mibBuilder.loadTexts:arrisRouterFWVirtSrvTable.setStatus(_A)
_ArrisRouterFWVirtSrvEntry_Object=MibTableRow
arrisRouterFWVirtSrvEntry=_ArrisRouterFWVirtSrvEntry_Object((1,3,6,1,4,1,4115,1,20,1,1,4,12,1))
arrisRouterFWVirtSrvEntry.setIndexNames((0,_I,_Ap))
if mibBuilder.loadTexts:arrisRouterFWVirtSrvEntry.setStatus(_A)
_ArrisRouterFWVirtSrvIndex_Type=Unsigned32
_ArrisRouterFWVirtSrvIndex_Object=MibTableColumn
arrisRouterFWVirtSrvIndex=_ArrisRouterFWVirtSrvIndex_Object((1,3,6,1,4,1,4115,1,20,1,1,4,12,1,1),_ArrisRouterFWVirtSrvIndex_Type())
arrisRouterFWVirtSrvIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:arrisRouterFWVirtSrvIndex.setStatus(_A)
class _ArrisRouterFWVirtSrvDesc_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_ArrisRouterFWVirtSrvDesc_Type.__name__=_G
_ArrisRouterFWVirtSrvDesc_Object=MibTableColumn
arrisRouterFWVirtSrvDesc=_ArrisRouterFWVirtSrvDesc_Object((1,3,6,1,4,1,4115,1,20,1,1,4,12,1,2),_ArrisRouterFWVirtSrvDesc_Type())
arrisRouterFWVirtSrvDesc.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterFWVirtSrvDesc.setStatus(_A)
class _ArrisRouterFWVirtSrvPortStart_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ArrisRouterFWVirtSrvPortStart_Type.__name__=_H
_ArrisRouterFWVirtSrvPortStart_Object=MibTableColumn
arrisRouterFWVirtSrvPortStart=_ArrisRouterFWVirtSrvPortStart_Object((1,3,6,1,4,1,4115,1,20,1,1,4,12,1,3),_ArrisRouterFWVirtSrvPortStart_Type())
arrisRouterFWVirtSrvPortStart.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterFWVirtSrvPortStart.setStatus(_A)
class _ArrisRouterFWVirtSrvPortEnd_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ArrisRouterFWVirtSrvPortEnd_Type.__name__=_H
_ArrisRouterFWVirtSrvPortEnd_Object=MibTableColumn
arrisRouterFWVirtSrvPortEnd=_ArrisRouterFWVirtSrvPortEnd_Object((1,3,6,1,4,1,4115,1,20,1,1,4,12,1,4),_ArrisRouterFWVirtSrvPortEnd_Type())
arrisRouterFWVirtSrvPortEnd.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterFWVirtSrvPortEnd.setStatus(_A)
class _ArrisRouterFWVirtSrvProtoType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_b,0),(_c,1),(_m,2)))
_ArrisRouterFWVirtSrvProtoType_Type.__name__=_D
_ArrisRouterFWVirtSrvProtoType_Object=MibTableColumn
arrisRouterFWVirtSrvProtoType=_ArrisRouterFWVirtSrvProtoType_Object((1,3,6,1,4,1,4115,1,20,1,1,4,12,1,5),_ArrisRouterFWVirtSrvProtoType_Type())
arrisRouterFWVirtSrvProtoType.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterFWVirtSrvProtoType.setStatus(_A)
_ArrisRouterFWVirtSrvIPAddrType_Type=InetAddressType
_ArrisRouterFWVirtSrvIPAddrType_Object=MibTableColumn
arrisRouterFWVirtSrvIPAddrType=_ArrisRouterFWVirtSrvIPAddrType_Object((1,3,6,1,4,1,4115,1,20,1,1,4,12,1,6),_ArrisRouterFWVirtSrvIPAddrType_Type())
arrisRouterFWVirtSrvIPAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterFWVirtSrvIPAddrType.setStatus(_A)
_ArrisRouterFWVirtSrvIPAddr_Type=InetAddress
_ArrisRouterFWVirtSrvIPAddr_Object=MibTableColumn
arrisRouterFWVirtSrvIPAddr=_ArrisRouterFWVirtSrvIPAddr_Object((1,3,6,1,4,1,4115,1,20,1,1,4,12,1,7),_ArrisRouterFWVirtSrvIPAddr_Type())
arrisRouterFWVirtSrvIPAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterFWVirtSrvIPAddr.setStatus(_A)
class _ArrisRouterFWVirtSrvLocalPortStart_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ArrisRouterFWVirtSrvLocalPortStart_Type.__name__=_H
_ArrisRouterFWVirtSrvLocalPortStart_Object=MibTableColumn
arrisRouterFWVirtSrvLocalPortStart=_ArrisRouterFWVirtSrvLocalPortStart_Object((1,3,6,1,4,1,4115,1,20,1,1,4,12,1,9),_ArrisRouterFWVirtSrvLocalPortStart_Type())
arrisRouterFWVirtSrvLocalPortStart.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterFWVirtSrvLocalPortStart.setStatus(_A)
class _ArrisRouterFWVirtSrvLocalPortEnd_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ArrisRouterFWVirtSrvLocalPortEnd_Type.__name__=_H
_ArrisRouterFWVirtSrvLocalPortEnd_Object=MibTableColumn
arrisRouterFWVirtSrvLocalPortEnd=_ArrisRouterFWVirtSrvLocalPortEnd_Object((1,3,6,1,4,1,4115,1,20,1,1,4,12,1,10),_ArrisRouterFWVirtSrvLocalPortEnd_Type())
arrisRouterFWVirtSrvLocalPortEnd.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterFWVirtSrvLocalPortEnd.setStatus(_A)
_ArrisRouterFWVirtSrvRowStatus_Type=RowStatus
_ArrisRouterFWVirtSrvRowStatus_Object=MibTableColumn
arrisRouterFWVirtSrvRowStatus=_ArrisRouterFWVirtSrvRowStatus_Object((1,3,6,1,4,1,4115,1,20,1,1,4,12,1,11),_ArrisRouterFWVirtSrvRowStatus_Type())
arrisRouterFWVirtSrvRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterFWVirtSrvRowStatus.setStatus(_A)
class _ArrisRouterFWSrvTr69InstanceID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ArrisRouterFWSrvTr69InstanceID_Type.__name__=_H
_ArrisRouterFWSrvTr69InstanceID_Object=MibTableColumn
arrisRouterFWSrvTr69InstanceID=_ArrisRouterFWSrvTr69InstanceID_Object((1,3,6,1,4,1,4115,1,20,1,1,4,12,1,14),_ArrisRouterFWSrvTr69InstanceID_Type())
arrisRouterFWSrvTr69InstanceID.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterFWSrvTr69InstanceID.setStatus(_A)
_ArrisRouterFWIPFilterTable_Object=MibTable
arrisRouterFWIPFilterTable=_ArrisRouterFWIPFilterTable_Object((1,3,6,1,4,1,4115,1,20,1,1,4,13))
if mibBuilder.loadTexts:arrisRouterFWIPFilterTable.setStatus(_A)
_ArrisRouterFWIPFilterEntry_Object=MibTableRow
arrisRouterFWIPFilterEntry=_ArrisRouterFWIPFilterEntry_Object((1,3,6,1,4,1,4115,1,20,1,1,4,13,1))
arrisRouterFWIPFilterEntry.setIndexNames((0,_I,_Aq))
if mibBuilder.loadTexts:arrisRouterFWIPFilterEntry.setStatus(_A)
_ArrisRouterFWIPFilterIndex_Type=Unsigned32
_ArrisRouterFWIPFilterIndex_Object=MibTableColumn
arrisRouterFWIPFilterIndex=_ArrisRouterFWIPFilterIndex_Object((1,3,6,1,4,1,4115,1,20,1,1,4,13,1,1),_ArrisRouterFWIPFilterIndex_Type())
arrisRouterFWIPFilterIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:arrisRouterFWIPFilterIndex.setStatus(_A)
class _ArrisRouterFWIPFilterDesc_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ArrisRouterFWIPFilterDesc_Type.__name__=_G
_ArrisRouterFWIPFilterDesc_Object=MibTableColumn
arrisRouterFWIPFilterDesc=_ArrisRouterFWIPFilterDesc_Object((1,3,6,1,4,1,4115,1,20,1,1,4,13,1,2),_ArrisRouterFWIPFilterDesc_Type())
arrisRouterFWIPFilterDesc.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterFWIPFilterDesc.setStatus(_A)
_ArrisRouterFWIPFilterStartType_Type=InetAddressType
_ArrisRouterFWIPFilterStartType_Object=MibTableColumn
arrisRouterFWIPFilterStartType=_ArrisRouterFWIPFilterStartType_Object((1,3,6,1,4,1,4115,1,20,1,1,4,13,1,3),_ArrisRouterFWIPFilterStartType_Type())
arrisRouterFWIPFilterStartType.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterFWIPFilterStartType.setStatus(_A)
_ArrisRouterFWIPFilterStartAddr_Type=InetAddress
_ArrisRouterFWIPFilterStartAddr_Object=MibTableColumn
arrisRouterFWIPFilterStartAddr=_ArrisRouterFWIPFilterStartAddr_Object((1,3,6,1,4,1,4115,1,20,1,1,4,13,1,4),_ArrisRouterFWIPFilterStartAddr_Type())
arrisRouterFWIPFilterStartAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterFWIPFilterStartAddr.setStatus(_A)
_ArrisRouterFWIPFilterEndType_Type=InetAddressType
_ArrisRouterFWIPFilterEndType_Object=MibTableColumn
arrisRouterFWIPFilterEndType=_ArrisRouterFWIPFilterEndType_Object((1,3,6,1,4,1,4115,1,20,1,1,4,13,1,5),_ArrisRouterFWIPFilterEndType_Type())
arrisRouterFWIPFilterEndType.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterFWIPFilterEndType.setStatus(_A)
_ArrisRouterFWIPFilterEndAddr_Type=InetAddress
_ArrisRouterFWIPFilterEndAddr_Object=MibTableColumn
arrisRouterFWIPFilterEndAddr=_ArrisRouterFWIPFilterEndAddr_Object((1,3,6,1,4,1,4115,1,20,1,1,4,13,1,6),_ArrisRouterFWIPFilterEndAddr_Type())
arrisRouterFWIPFilterEndAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterFWIPFilterEndAddr.setStatus(_A)
class _ArrisRouterFWIPFilterPortStart_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ArrisRouterFWIPFilterPortStart_Type.__name__=_H
_ArrisRouterFWIPFilterPortStart_Object=MibTableColumn
arrisRouterFWIPFilterPortStart=_ArrisRouterFWIPFilterPortStart_Object((1,3,6,1,4,1,4115,1,20,1,1,4,13,1,7),_ArrisRouterFWIPFilterPortStart_Type())
arrisRouterFWIPFilterPortStart.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterFWIPFilterPortStart.setStatus(_A)
class _ArrisRouterFWIPFilterPortEnd_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ArrisRouterFWIPFilterPortEnd_Type.__name__=_H
_ArrisRouterFWIPFilterPortEnd_Object=MibTableColumn
arrisRouterFWIPFilterPortEnd=_ArrisRouterFWIPFilterPortEnd_Object((1,3,6,1,4,1,4115,1,20,1,1,4,13,1,8),_ArrisRouterFWIPFilterPortEnd_Type())
arrisRouterFWIPFilterPortEnd.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterFWIPFilterPortEnd.setStatus(_A)
class _ArrisRouterFWIPFilterProtoType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_b,0),(_c,1),(_m,2)))
_ArrisRouterFWIPFilterProtoType_Type.__name__=_D
_ArrisRouterFWIPFilterProtoType_Object=MibTableColumn
arrisRouterFWIPFilterProtoType=_ArrisRouterFWIPFilterProtoType_Object((1,3,6,1,4,1,4115,1,20,1,1,4,13,1,9),_ArrisRouterFWIPFilterProtoType_Type())
arrisRouterFWIPFilterProtoType.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterFWIPFilterProtoType.setStatus(_A)
_ArrisRouterFWIPFilterTOD_Type=Integer32
_ArrisRouterFWIPFilterTOD_Object=MibTableColumn
arrisRouterFWIPFilterTOD=_ArrisRouterFWIPFilterTOD_Object((1,3,6,1,4,1,4115,1,20,1,1,4,13,1,10),_ArrisRouterFWIPFilterTOD_Type())
arrisRouterFWIPFilterTOD.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterFWIPFilterTOD.setStatus(_A)
_ArrisRouterFWIPFilterRowStatus_Type=RowStatus
_ArrisRouterFWIPFilterRowStatus_Object=MibTableColumn
arrisRouterFWIPFilterRowStatus=_ArrisRouterFWIPFilterRowStatus_Object((1,3,6,1,4,1,4115,1,20,1,1,4,13,1,11),_ArrisRouterFWIPFilterRowStatus_Type())
arrisRouterFWIPFilterRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterFWIPFilterRowStatus.setStatus(_A)
class _ArrisRouterFWIPFilterAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('allow',0),('deny',1)))
_ArrisRouterFWIPFilterAction_Type.__name__=_D
_ArrisRouterFWIPFilterAction_Object=MibTableColumn
arrisRouterFWIPFilterAction=_ArrisRouterFWIPFilterAction_Object((1,3,6,1,4,1,4115,1,20,1,1,4,13,1,12),_ArrisRouterFWIPFilterAction_Type())
arrisRouterFWIPFilterAction.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterFWIPFilterAction.setStatus(_A)
class _ArrisRouterFWIPFilterDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('incoming',0),('outgoing',1)))
_ArrisRouterFWIPFilterDirection_Type.__name__=_D
_ArrisRouterFWIPFilterDirection_Object=MibTableColumn
arrisRouterFWIPFilterDirection=_ArrisRouterFWIPFilterDirection_Object((1,3,6,1,4,1,4115,1,20,1,1,4,13,1,13),_ArrisRouterFWIPFilterDirection_Type())
arrisRouterFWIPFilterDirection.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterFWIPFilterDirection.setStatus(_A)
_ArrisRouterFWAllowAll_Type=TruthValue
_ArrisRouterFWAllowAll_Object=MibScalar
arrisRouterFWAllowAll=_ArrisRouterFWAllowAll_Object((1,3,6,1,4,1,4115,1,20,1,1,4,14),_ArrisRouterFWAllowAll_Type())
arrisRouterFWAllowAll.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterFWAllowAll.setStatus(_A)
_ArrisRouterFWMACFilterTable_Object=MibTable
arrisRouterFWMACFilterTable=_ArrisRouterFWMACFilterTable_Object((1,3,6,1,4,1,4115,1,20,1,1,4,15))
if mibBuilder.loadTexts:arrisRouterFWMACFilterTable.setStatus(_A)
_ArrisRouterFWMACFilterEntry_Object=MibTableRow
arrisRouterFWMACFilterEntry=_ArrisRouterFWMACFilterEntry_Object((1,3,6,1,4,1,4115,1,20,1,1,4,15,1))
arrisRouterFWMACFilterEntry.setIndexNames((0,_K,_L),(0,_I,_Ar))
if mibBuilder.loadTexts:arrisRouterFWMACFilterEntry.setStatus(_A)
_ArrisRouterFWMACFilterIndex_Type=Unsigned32
_ArrisRouterFWMACFilterIndex_Object=MibTableColumn
arrisRouterFWMACFilterIndex=_ArrisRouterFWMACFilterIndex_Object((1,3,6,1,4,1,4115,1,20,1,1,4,15,1,1),_ArrisRouterFWMACFilterIndex_Type())
arrisRouterFWMACFilterIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:arrisRouterFWMACFilterIndex.setStatus(_A)
_ArrisRouterFWMACFilterAddr_Type=MacAddress
_ArrisRouterFWMACFilterAddr_Object=MibTableColumn
arrisRouterFWMACFilterAddr=_ArrisRouterFWMACFilterAddr_Object((1,3,6,1,4,1,4115,1,20,1,1,4,15,1,2),_ArrisRouterFWMACFilterAddr_Type())
arrisRouterFWMACFilterAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterFWMACFilterAddr.setStatus(_A)
_ArrisRouterFWMACFilterTOD_Type=Integer32
_ArrisRouterFWMACFilterTOD_Object=MibTableColumn
arrisRouterFWMACFilterTOD=_ArrisRouterFWMACFilterTOD_Object((1,3,6,1,4,1,4115,1,20,1,1,4,15,1,3),_ArrisRouterFWMACFilterTOD_Type())
arrisRouterFWMACFilterTOD.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterFWMACFilterTOD.setStatus(_A)
_ArrisRouterFWMACFilterRowStatus_Type=RowStatus
_ArrisRouterFWMACFilterRowStatus_Object=MibTableColumn
arrisRouterFWMACFilterRowStatus=_ArrisRouterFWMACFilterRowStatus_Object((1,3,6,1,4,1,4115,1,20,1,1,4,15,1,4),_ArrisRouterFWMACFilterRowStatus_Type())
arrisRouterFWMACFilterRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterFWMACFilterRowStatus.setStatus(_A)
_ArrisRouterFWPortTrigTable_Object=MibTable
arrisRouterFWPortTrigTable=_ArrisRouterFWPortTrigTable_Object((1,3,6,1,4,1,4115,1,20,1,1,4,16))
if mibBuilder.loadTexts:arrisRouterFWPortTrigTable.setStatus(_A)
_ArrisRouterFWPortTrigEntry_Object=MibTableRow
arrisRouterFWPortTrigEntry=_ArrisRouterFWPortTrigEntry_Object((1,3,6,1,4,1,4115,1,20,1,1,4,16,1))
arrisRouterFWPortTrigEntry.setIndexNames((0,_I,_As))
if mibBuilder.loadTexts:arrisRouterFWPortTrigEntry.setStatus(_A)
_ArrisRouterFWPortTrigIndex_Type=Unsigned32
_ArrisRouterFWPortTrigIndex_Object=MibTableColumn
arrisRouterFWPortTrigIndex=_ArrisRouterFWPortTrigIndex_Object((1,3,6,1,4,1,4115,1,20,1,1,4,16,1,1),_ArrisRouterFWPortTrigIndex_Type())
arrisRouterFWPortTrigIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:arrisRouterFWPortTrigIndex.setStatus(_A)
class _ArrisRouterFWPortTrigDesc_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_ArrisRouterFWPortTrigDesc_Type.__name__=_G
_ArrisRouterFWPortTrigDesc_Object=MibTableColumn
arrisRouterFWPortTrigDesc=_ArrisRouterFWPortTrigDesc_Object((1,3,6,1,4,1,4115,1,20,1,1,4,16,1,2),_ArrisRouterFWPortTrigDesc_Type())
arrisRouterFWPortTrigDesc.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterFWPortTrigDesc.setStatus(_A)
class _ArrisRouterFWPortTrigPortStart_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ArrisRouterFWPortTrigPortStart_Type.__name__=_H
_ArrisRouterFWPortTrigPortStart_Object=MibTableColumn
arrisRouterFWPortTrigPortStart=_ArrisRouterFWPortTrigPortStart_Object((1,3,6,1,4,1,4115,1,20,1,1,4,16,1,3),_ArrisRouterFWPortTrigPortStart_Type())
arrisRouterFWPortTrigPortStart.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterFWPortTrigPortStart.setStatus(_A)
class _ArrisRouterFWPortTrigPortEnd_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ArrisRouterFWPortTrigPortEnd_Type.__name__=_H
_ArrisRouterFWPortTrigPortEnd_Object=MibTableColumn
arrisRouterFWPortTrigPortEnd=_ArrisRouterFWPortTrigPortEnd_Object((1,3,6,1,4,1,4115,1,20,1,1,4,16,1,4),_ArrisRouterFWPortTrigPortEnd_Type())
arrisRouterFWPortTrigPortEnd.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterFWPortTrigPortEnd.setStatus(_A)
class _ArrisRouterFWPortTargPortStart_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ArrisRouterFWPortTargPortStart_Type.__name__=_H
_ArrisRouterFWPortTargPortStart_Object=MibTableColumn
arrisRouterFWPortTargPortStart=_ArrisRouterFWPortTargPortStart_Object((1,3,6,1,4,1,4115,1,20,1,1,4,16,1,5),_ArrisRouterFWPortTargPortStart_Type())
arrisRouterFWPortTargPortStart.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterFWPortTargPortStart.setStatus(_A)
class _ArrisRouterFWPortTargPortEnd_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ArrisRouterFWPortTargPortEnd_Type.__name__=_H
_ArrisRouterFWPortTargPortEnd_Object=MibTableColumn
arrisRouterFWPortTargPortEnd=_ArrisRouterFWPortTargPortEnd_Object((1,3,6,1,4,1,4115,1,20,1,1,4,16,1,6),_ArrisRouterFWPortTargPortEnd_Type())
arrisRouterFWPortTargPortEnd.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterFWPortTargPortEnd.setStatus(_A)
class _ArrisRouterFWPortTrigProtoType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_b,0),(_c,1),(_m,2)))
_ArrisRouterFWPortTrigProtoType_Type.__name__=_D
_ArrisRouterFWPortTrigProtoType_Object=MibTableColumn
arrisRouterFWPortTrigProtoType=_ArrisRouterFWPortTrigProtoType_Object((1,3,6,1,4,1,4115,1,20,1,1,4,16,1,7),_ArrisRouterFWPortTrigProtoType_Type())
arrisRouterFWPortTrigProtoType.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterFWPortTrigProtoType.setStatus(_A)
_ArrisRouterFWPortTrigRowStatus_Type=RowStatus
_ArrisRouterFWPortTrigRowStatus_Object=MibTableColumn
arrisRouterFWPortTrigRowStatus=_ArrisRouterFWPortTrigRowStatus_Object((1,3,6,1,4,1,4115,1,20,1,1,4,16,1,9),_ArrisRouterFWPortTrigRowStatus_Type())
arrisRouterFWPortTrigRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterFWPortTrigRowStatus.setStatus(_A)
_ArrisRouterFWFilterRules_ObjectIdentity=ObjectIdentity
arrisRouterFWFilterRules=_ArrisRouterFWFilterRules_ObjectIdentity((1,3,6,1,4,1,4115,1,20,1,1,4,17))
class _ArrisRouterFWBlockFragIPPkts_Type(TruthValue):defaultValue=2
_ArrisRouterFWBlockFragIPPkts_Type.__name__=_F
_ArrisRouterFWBlockFragIPPkts_Object=MibScalar
arrisRouterFWBlockFragIPPkts=_ArrisRouterFWBlockFragIPPkts_Object((1,3,6,1,4,1,4115,1,20,1,1,4,17,6),_ArrisRouterFWBlockFragIPPkts_Type())
arrisRouterFWBlockFragIPPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterFWBlockFragIPPkts.setStatus(_A)
class _ArrisRouterFWPortScanProtect_Type(TruthValue):defaultValue=2
_ArrisRouterFWPortScanProtect_Type.__name__=_F
_ArrisRouterFWPortScanProtect_Object=MibScalar
arrisRouterFWPortScanProtect=_ArrisRouterFWPortScanProtect_Object((1,3,6,1,4,1,4115,1,20,1,1,4,17,7),_ArrisRouterFWPortScanProtect_Type())
arrisRouterFWPortScanProtect.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterFWPortScanProtect.setStatus(_A)
class _ArrisRouterFWIPFloodDetect_Type(TruthValue):defaultValue=1
_ArrisRouterFWIPFloodDetect_Type.__name__=_F
_ArrisRouterFWIPFloodDetect_Object=MibScalar
arrisRouterFWIPFloodDetect=_ArrisRouterFWIPFloodDetect_Object((1,3,6,1,4,1,4115,1,20,1,1,4,17,8),_ArrisRouterFWIPFloodDetect_Type())
arrisRouterFWIPFloodDetect.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterFWIPFloodDetect.setStatus(_A)
class _ArrisRouterFWBlockFragIPPktsV4_Type(TruthValue):defaultValue=2
_ArrisRouterFWBlockFragIPPktsV4_Type.__name__=_F
_ArrisRouterFWBlockFragIPPktsV4_Object=MibScalar
arrisRouterFWBlockFragIPPktsV4=_ArrisRouterFWBlockFragIPPktsV4_Object((1,3,6,1,4,1,4115,1,20,1,1,4,17,9),_ArrisRouterFWBlockFragIPPktsV4_Type())
arrisRouterFWBlockFragIPPktsV4.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterFWBlockFragIPPktsV4.setStatus(_A)
class _ArrisRouterFWPortScanProtectV4_Type(TruthValue):defaultValue=2
_ArrisRouterFWPortScanProtectV4_Type.__name__=_F
_ArrisRouterFWPortScanProtectV4_Object=MibScalar
arrisRouterFWPortScanProtectV4=_ArrisRouterFWPortScanProtectV4_Object((1,3,6,1,4,1,4115,1,20,1,1,4,17,10),_ArrisRouterFWPortScanProtectV4_Type())
arrisRouterFWPortScanProtectV4.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterFWPortScanProtectV4.setStatus(_A)
class _ArrisRouterFWIPFloodDetectV4_Type(TruthValue):defaultValue=1
_ArrisRouterFWIPFloodDetectV4_Type.__name__=_F
_ArrisRouterFWIPFloodDetectV4_Object=MibScalar
arrisRouterFWIPFloodDetectV4=_ArrisRouterFWIPFloodDetectV4_Object((1,3,6,1,4,1,4115,1,20,1,1,4,17,11),_ArrisRouterFWIPFloodDetectV4_Type())
arrisRouterFWIPFloodDetectV4.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterFWIPFloodDetectV4.setStatus(_A)
class _ArrisRouterFWBlockFragIPPktsV6_Type(TruthValue):defaultValue=2
_ArrisRouterFWBlockFragIPPktsV6_Type.__name__=_F
_ArrisRouterFWBlockFragIPPktsV6_Object=MibScalar
arrisRouterFWBlockFragIPPktsV6=_ArrisRouterFWBlockFragIPPktsV6_Object((1,3,6,1,4,1,4115,1,20,1,1,4,17,12),_ArrisRouterFWBlockFragIPPktsV6_Type())
arrisRouterFWBlockFragIPPktsV6.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterFWBlockFragIPPktsV6.setStatus(_A)
class _ArrisRouterFWPortScanProtectV6_Type(TruthValue):defaultValue=2
_ArrisRouterFWPortScanProtectV6_Type.__name__=_F
_ArrisRouterFWPortScanProtectV6_Object=MibScalar
arrisRouterFWPortScanProtectV6=_ArrisRouterFWPortScanProtectV6_Object((1,3,6,1,4,1,4115,1,20,1,1,4,17,13),_ArrisRouterFWPortScanProtectV6_Type())
arrisRouterFWPortScanProtectV6.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterFWPortScanProtectV6.setStatus(_A)
class _ArrisRouterFWIPFloodDetectV6_Type(TruthValue):defaultValue=1
_ArrisRouterFWIPFloodDetectV6_Type.__name__=_F
_ArrisRouterFWIPFloodDetectV6_Object=MibScalar
arrisRouterFWIPFloodDetectV6=_ArrisRouterFWIPFloodDetectV6_Object((1,3,6,1,4,1,4115,1,20,1,1,4,17,14),_ArrisRouterFWIPFloodDetectV6_Type())
arrisRouterFWIPFloodDetectV6.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterFWIPFloodDetectV6.setStatus(_A)
_ArrisRouterFWDDNSObjs_ObjectIdentity=ObjectIdentity
arrisRouterFWDDNSObjs=_ArrisRouterFWDDNSObjs_ObjectIdentity((1,3,6,1,4,1,4115,1,20,1,1,4,18))
class _ArrisRouterFWDDNSEnable_Type(TruthValue):defaultValue=2
_ArrisRouterFWDDNSEnable_Type.__name__=_F
_ArrisRouterFWDDNSEnable_Object=MibScalar
arrisRouterFWDDNSEnable=_ArrisRouterFWDDNSEnable_Object((1,3,6,1,4,1,4115,1,20,1,1,4,18,1),_ArrisRouterFWDDNSEnable_Type())
arrisRouterFWDDNSEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterFWDDNSEnable.setStatus(_A)
class _ArrisRouterFWDDNSType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_N,0),('dynDNS',1),('tzo',2),('freeDNS',3),('zoneEdit',4),('noIP',5),('easyDNS',6),('domainsGoogle',7)))
_ArrisRouterFWDDNSType_Type.__name__=_D
_ArrisRouterFWDDNSType_Object=MibScalar
arrisRouterFWDDNSType=_ArrisRouterFWDDNSType_Object((1,3,6,1,4,1,4115,1,20,1,1,4,18,2),_ArrisRouterFWDDNSType_Type())
arrisRouterFWDDNSType.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterFWDDNSType.setStatus(_A)
class _ArrisRouterFWDDNSUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ArrisRouterFWDDNSUserName_Type.__name__=_G
_ArrisRouterFWDDNSUserName_Object=MibScalar
arrisRouterFWDDNSUserName=_ArrisRouterFWDDNSUserName_Object((1,3,6,1,4,1,4115,1,20,1,1,4,18,3),_ArrisRouterFWDDNSUserName_Type())
arrisRouterFWDDNSUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterFWDDNSUserName.setStatus(_A)
class _ArrisRouterFWDDNSPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ArrisRouterFWDDNSPassword_Type.__name__=_G
_ArrisRouterFWDDNSPassword_Object=MibScalar
arrisRouterFWDDNSPassword=_ArrisRouterFWDDNSPassword_Object((1,3,6,1,4,1,4115,1,20,1,1,4,18,4),_ArrisRouterFWDDNSPassword_Type())
arrisRouterFWDDNSPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterFWDDNSPassword.setStatus(_A)
class _ArrisRouterFWDDNSDomainName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ArrisRouterFWDDNSDomainName_Type.__name__=_G
_ArrisRouterFWDDNSDomainName_Object=MibScalar
arrisRouterFWDDNSDomainName=_ArrisRouterFWDDNSDomainName_Object((1,3,6,1,4,1,4115,1,20,1,1,4,18,5),_ArrisRouterFWDDNSDomainName_Type())
arrisRouterFWDDNSDomainName.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterFWDDNSDomainName.setStatus(_A)
_ArrisRouterFWDDNSIPAddrType_Type=InetAddressType
_ArrisRouterFWDDNSIPAddrType_Object=MibScalar
arrisRouterFWDDNSIPAddrType=_ArrisRouterFWDDNSIPAddrType_Object((1,3,6,1,4,1,4115,1,20,1,1,4,18,6),_ArrisRouterFWDDNSIPAddrType_Type())
arrisRouterFWDDNSIPAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterFWDDNSIPAddrType.setStatus(_A)
_ArrisRouterFWDDNSIPAddr_Type=InetAddress
_ArrisRouterFWDDNSIPAddr_Object=MibScalar
arrisRouterFWDDNSIPAddr=_ArrisRouterFWDDNSIPAddr_Object((1,3,6,1,4,1,4115,1,20,1,1,4,18,7),_ArrisRouterFWDDNSIPAddr_Type())
arrisRouterFWDDNSIPAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterFWDDNSIPAddr.setStatus(_A)
class _ArrisRouterFWDDNSStatus_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ArrisRouterFWDDNSStatus_Type.__name__=_G
_ArrisRouterFWDDNSStatus_Object=MibScalar
arrisRouterFWDDNSStatus=_ArrisRouterFWDDNSStatus_Object((1,3,6,1,4,1,4115,1,20,1,1,4,18,8),_ArrisRouterFWDDNSStatus_Type())
arrisRouterFWDDNSStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterFWDDNSStatus.setStatus(_A)
_ArrisRouterFWFeatures_ObjectIdentity=ObjectIdentity
arrisRouterFWFeatures=_ArrisRouterFWFeatures_ObjectIdentity((1,3,6,1,4,1,4115,1,20,1,1,4,19))
class _ArrisRouterFWIPSecPassThru_Type(TruthValue):defaultValue=2
_ArrisRouterFWIPSecPassThru_Type.__name__=_F
_ArrisRouterFWIPSecPassThru_Object=MibScalar
arrisRouterFWIPSecPassThru=_ArrisRouterFWIPSecPassThru_Object((1,3,6,1,4,1,4115,1,20,1,1,4,19,2),_ArrisRouterFWIPSecPassThru_Type())
arrisRouterFWIPSecPassThru.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterFWIPSecPassThru.setStatus(_A)
class _ArrisRouterFWPPTPPassThru_Type(TruthValue):defaultValue=2
_ArrisRouterFWPPTPPassThru_Type.__name__=_F
_ArrisRouterFWPPTPPassThru_Object=MibScalar
arrisRouterFWPPTPPassThru=_ArrisRouterFWPPTPPassThru_Object((1,3,6,1,4,1,4115,1,20,1,1,4,19,3),_ArrisRouterFWPPTPPassThru_Type())
arrisRouterFWPPTPPassThru.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterFWPPTPPassThru.setStatus(_A)
class _ArrisRouterFWEnableMulticast_Type(TruthValue):defaultValue=1
_ArrisRouterFWEnableMulticast_Type.__name__=_F
_ArrisRouterFWEnableMulticast_Object=MibScalar
arrisRouterFWEnableMulticast=_ArrisRouterFWEnableMulticast_Object((1,3,6,1,4,1,4115,1,20,1,1,4,19,4),_ArrisRouterFWEnableMulticast_Type())
arrisRouterFWEnableMulticast.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterFWEnableMulticast.setStatus(_A)
class _ArrisRouterFWEnableRemoteMgmt_Type(TruthValue):defaultValue=2
_ArrisRouterFWEnableRemoteMgmt_Type.__name__=_F
_ArrisRouterFWEnableRemoteMgmt_Object=MibScalar
arrisRouterFWEnableRemoteMgmt=_ArrisRouterFWEnableRemoteMgmt_Object((1,3,6,1,4,1,4115,1,20,1,1,4,19,5),_ArrisRouterFWEnableRemoteMgmt_Type())
arrisRouterFWEnableRemoteMgmt.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterFWEnableRemoteMgmt.setStatus(_A)
class _ArrisRouterFWL2TPPassThru_Type(TruthValue):defaultValue=2
_ArrisRouterFWL2TPPassThru_Type.__name__=_F
_ArrisRouterFWL2TPPassThru_Object=MibScalar
arrisRouterFWL2TPPassThru=_ArrisRouterFWL2TPPassThru_Object((1,3,6,1,4,1,4115,1,20,1,1,4,19,7),_ArrisRouterFWL2TPPassThru_Type())
arrisRouterFWL2TPPassThru.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterFWL2TPPassThru.setStatus(_A)
_ArrisRouterFWRemoteMgmt_ObjectIdentity=ObjectIdentity
arrisRouterFWRemoteMgmt=_ArrisRouterFWRemoteMgmt_ObjectIdentity((1,3,6,1,4,1,4115,1,20,1,1,4,19,12))
class _ArrisRouterFWRemoteMgmtHttp_Type(TruthValue):defaultValue=2
_ArrisRouterFWRemoteMgmtHttp_Type.__name__=_F
_ArrisRouterFWRemoteMgmtHttp_Object=MibScalar
arrisRouterFWRemoteMgmtHttp=_ArrisRouterFWRemoteMgmtHttp_Object((1,3,6,1,4,1,4115,1,20,1,1,4,19,12,1),_ArrisRouterFWRemoteMgmtHttp_Type())
arrisRouterFWRemoteMgmtHttp.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterFWRemoteMgmtHttp.setStatus(_A)
class _ArrisRouterFWRemoteMgmtHttps_Type(TruthValue):defaultValue=2
_ArrisRouterFWRemoteMgmtHttps_Type.__name__=_F
_ArrisRouterFWRemoteMgmtHttps_Object=MibScalar
arrisRouterFWRemoteMgmtHttps=_ArrisRouterFWRemoteMgmtHttps_Object((1,3,6,1,4,1,4115,1,20,1,1,4,19,12,2),_ArrisRouterFWRemoteMgmtHttps_Type())
arrisRouterFWRemoteMgmtHttps.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterFWRemoteMgmtHttps.setStatus(_A)
class _ArrisRouterFWRemoteMgmtHttpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ArrisRouterFWRemoteMgmtHttpPort_Type.__name__=_D
_ArrisRouterFWRemoteMgmtHttpPort_Object=MibScalar
arrisRouterFWRemoteMgmtHttpPort=_ArrisRouterFWRemoteMgmtHttpPort_Object((1,3,6,1,4,1,4115,1,20,1,1,4,19,12,3),_ArrisRouterFWRemoteMgmtHttpPort_Type())
arrisRouterFWRemoteMgmtHttpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterFWRemoteMgmtHttpPort.setStatus(_A)
class _ArrisRouterFWRemoteMgmtHttpsPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ArrisRouterFWRemoteMgmtHttpsPort_Type.__name__=_D
_ArrisRouterFWRemoteMgmtHttpsPort_Object=MibScalar
arrisRouterFWRemoteMgmtHttpsPort=_ArrisRouterFWRemoteMgmtHttpsPort_Object((1,3,6,1,4,1,4115,1,20,1,1,4,19,12,4),_ArrisRouterFWRemoteMgmtHttpsPort_Type())
arrisRouterFWRemoteMgmtHttpsPort.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterFWRemoteMgmtHttpsPort.setStatus(_A)
class _ArrisRouterFWRemoteMgmtAllowedType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('singleComputer',1),('rangeOfIP',2),('anyComputer',3)))
_ArrisRouterFWRemoteMgmtAllowedType_Type.__name__=_D
_ArrisRouterFWRemoteMgmtAllowedType_Object=MibScalar
arrisRouterFWRemoteMgmtAllowedType=_ArrisRouterFWRemoteMgmtAllowedType_Object((1,3,6,1,4,1,4115,1,20,1,1,4,19,12,5),_ArrisRouterFWRemoteMgmtAllowedType_Type())
arrisRouterFWRemoteMgmtAllowedType.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterFWRemoteMgmtAllowedType.setStatus(_A)
_ArrisRouterFWRemoteMgmtAllowedIPv4_Type=InetAddress
_ArrisRouterFWRemoteMgmtAllowedIPv4_Object=MibScalar
arrisRouterFWRemoteMgmtAllowedIPv4=_ArrisRouterFWRemoteMgmtAllowedIPv4_Object((1,3,6,1,4,1,4115,1,20,1,1,4,19,12,6),_ArrisRouterFWRemoteMgmtAllowedIPv4_Type())
arrisRouterFWRemoteMgmtAllowedIPv4.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterFWRemoteMgmtAllowedIPv4.setStatus(_A)
_ArrisRouterFWRemoteMgmtAllowedIPv6_Type=InetAddress
_ArrisRouterFWRemoteMgmtAllowedIPv6_Object=MibScalar
arrisRouterFWRemoteMgmtAllowedIPv6=_ArrisRouterFWRemoteMgmtAllowedIPv6_Object((1,3,6,1,4,1,4115,1,20,1,1,4,19,12,7),_ArrisRouterFWRemoteMgmtAllowedIPv6_Type())
arrisRouterFWRemoteMgmtAllowedIPv6.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterFWRemoteMgmtAllowedIPv6.setStatus(_A)
_ArrisRouterFWRemoteMgmtAllowedStartIPv4_Type=InetAddress
_ArrisRouterFWRemoteMgmtAllowedStartIPv4_Object=MibScalar
arrisRouterFWRemoteMgmtAllowedStartIPv4=_ArrisRouterFWRemoteMgmtAllowedStartIPv4_Object((1,3,6,1,4,1,4115,1,20,1,1,4,19,12,8),_ArrisRouterFWRemoteMgmtAllowedStartIPv4_Type())
arrisRouterFWRemoteMgmtAllowedStartIPv4.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterFWRemoteMgmtAllowedStartIPv4.setStatus(_A)
_ArrisRouterFWRemoteMgmtAllowedEndIPv4_Type=InetAddress
_ArrisRouterFWRemoteMgmtAllowedEndIPv4_Object=MibScalar
arrisRouterFWRemoteMgmtAllowedEndIPv4=_ArrisRouterFWRemoteMgmtAllowedEndIPv4_Object((1,3,6,1,4,1,4115,1,20,1,1,4,19,12,9),_ArrisRouterFWRemoteMgmtAllowedEndIPv4_Type())
arrisRouterFWRemoteMgmtAllowedEndIPv4.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterFWRemoteMgmtAllowedEndIPv4.setStatus(_A)
_ArrisRouterFWRemoteMgmtAllowedStartIPv6_Type=InetAddress
_ArrisRouterFWRemoteMgmtAllowedStartIPv6_Object=MibScalar
arrisRouterFWRemoteMgmtAllowedStartIPv6=_ArrisRouterFWRemoteMgmtAllowedStartIPv6_Object((1,3,6,1,4,1,4115,1,20,1,1,4,19,12,10),_ArrisRouterFWRemoteMgmtAllowedStartIPv6_Type())
arrisRouterFWRemoteMgmtAllowedStartIPv6.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterFWRemoteMgmtAllowedStartIPv6.setStatus(_A)
_ArrisRouterFWRemoteMgmtAllowedEndIPv6_Type=InetAddress
_ArrisRouterFWRemoteMgmtAllowedEndIPv6_Object=MibScalar
arrisRouterFWRemoteMgmtAllowedEndIPv6=_ArrisRouterFWRemoteMgmtAllowedEndIPv6_Object((1,3,6,1,4,1,4115,1,20,1,1,4,19,12,11),_ArrisRouterFWRemoteMgmtAllowedEndIPv6_Type())
arrisRouterFWRemoteMgmtAllowedEndIPv6.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterFWRemoteMgmtAllowedEndIPv6.setStatus(_A)
class _ArrisRouterFWRemoteMgmtTelnet_Type(TruthValue):defaultValue=2
_ArrisRouterFWRemoteMgmtTelnet_Type.__name__=_F
_ArrisRouterFWRemoteMgmtTelnet_Object=MibScalar
arrisRouterFWRemoteMgmtTelnet=_ArrisRouterFWRemoteMgmtTelnet_Object((1,3,6,1,4,1,4115,1,20,1,1,4,19,12,12),_ArrisRouterFWRemoteMgmtTelnet_Type())
arrisRouterFWRemoteMgmtTelnet.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterFWRemoteMgmtTelnet.setStatus(_A)
_ArrisRouterFWSelectRemoteMgmt_Type=TruthValue
_ArrisRouterFWSelectRemoteMgmt_Object=MibScalar
arrisRouterFWSelectRemoteMgmt=_ArrisRouterFWSelectRemoteMgmt_Object((1,3,6,1,4,1,4115,1,20,1,1,4,19,13),_ArrisRouterFWSelectRemoteMgmt_Type())
arrisRouterFWSelectRemoteMgmt.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterFWSelectRemoteMgmt.setStatus(_A)
_ArrisRouterFWParentalControls_ObjectIdentity=ObjectIdentity
arrisRouterFWParentalControls=_ArrisRouterFWParentalControls_ObjectIdentity((1,3,6,1,4,1,4115,1,20,1,1,4,20))
_ArrisRouterKeywordCount_Type=Integer32
_ArrisRouterKeywordCount_Object=MibScalar
arrisRouterKeywordCount=_ArrisRouterKeywordCount_Object((1,3,6,1,4,1,4115,1,20,1,1,4,20,1),_ArrisRouterKeywordCount_Type())
arrisRouterKeywordCount.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterKeywordCount.setStatus(_A)
_ArrisRouterBlackListCount_Type=Integer32
_ArrisRouterBlackListCount_Object=MibScalar
arrisRouterBlackListCount=_ArrisRouterBlackListCount_Object((1,3,6,1,4,1,4115,1,20,1,1,4,20,3),_ArrisRouterBlackListCount_Type())
arrisRouterBlackListCount.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterBlackListCount.setStatus(_A)
_ArrisRouterWhiteListCount_Type=Integer32
_ArrisRouterWhiteListCount_Object=MibScalar
arrisRouterWhiteListCount=_ArrisRouterWhiteListCount_Object((1,3,6,1,4,1,4115,1,20,1,1,4,20,5),_ArrisRouterWhiteListCount_Type())
arrisRouterWhiteListCount.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWhiteListCount.setStatus(_A)
_ArrisRouterKeywordBlkTable_Object=MibTable
arrisRouterKeywordBlkTable=_ArrisRouterKeywordBlkTable_Object((1,3,6,1,4,1,4115,1,20,1,1,4,20,10))
if mibBuilder.loadTexts:arrisRouterKeywordBlkTable.setStatus(_A)
_ArrisRouterKeywordBlkEntry_Object=MibTableRow
arrisRouterKeywordBlkEntry=_ArrisRouterKeywordBlkEntry_Object((1,3,6,1,4,1,4115,1,20,1,1,4,20,10,1))
arrisRouterKeywordBlkEntry.setIndexNames((0,_I,_At))
if mibBuilder.loadTexts:arrisRouterKeywordBlkEntry.setStatus(_A)
class _ArrisRouterKeywordBlkIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_ArrisRouterKeywordBlkIndex_Type.__name__=_D
_ArrisRouterKeywordBlkIndex_Object=MibTableColumn
arrisRouterKeywordBlkIndex=_ArrisRouterKeywordBlkIndex_Object((1,3,6,1,4,1,4115,1,20,1,1,4,20,10,1,1),_ArrisRouterKeywordBlkIndex_Type())
arrisRouterKeywordBlkIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:arrisRouterKeywordBlkIndex.setStatus(_A)
class _ArrisRouterKeywordBlkWord_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ArrisRouterKeywordBlkWord_Type.__name__=_G
_ArrisRouterKeywordBlkWord_Object=MibTableColumn
arrisRouterKeywordBlkWord=_ArrisRouterKeywordBlkWord_Object((1,3,6,1,4,1,4115,1,20,1,1,4,20,10,1,2),_ArrisRouterKeywordBlkWord_Type())
arrisRouterKeywordBlkWord.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterKeywordBlkWord.setStatus(_A)
_ArrisRouterKeywordBlkTOD_Type=Integer32
_ArrisRouterKeywordBlkTOD_Object=MibTableColumn
arrisRouterKeywordBlkTOD=_ArrisRouterKeywordBlkTOD_Object((1,3,6,1,4,1,4115,1,20,1,1,4,20,10,1,3),_ArrisRouterKeywordBlkTOD_Type())
arrisRouterKeywordBlkTOD.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterKeywordBlkTOD.setStatus(_A)
_ArrisRouterKeywordBlkStatus_Type=RowStatus
_ArrisRouterKeywordBlkStatus_Object=MibTableColumn
arrisRouterKeywordBlkStatus=_ArrisRouterKeywordBlkStatus_Object((1,3,6,1,4,1,4115,1,20,1,1,4,20,10,1,4),_ArrisRouterKeywordBlkStatus_Type())
arrisRouterKeywordBlkStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterKeywordBlkStatus.setStatus(_A)
_ArrisRouterBlackListTable_Object=MibTable
arrisRouterBlackListTable=_ArrisRouterBlackListTable_Object((1,3,6,1,4,1,4115,1,20,1,1,4,20,12))
if mibBuilder.loadTexts:arrisRouterBlackListTable.setStatus(_A)
_ArrisRouterBlackListEntry_Object=MibTableRow
arrisRouterBlackListEntry=_ArrisRouterBlackListEntry_Object((1,3,6,1,4,1,4115,1,20,1,1,4,20,12,1))
arrisRouterBlackListEntry.setIndexNames((0,_I,_Au))
if mibBuilder.loadTexts:arrisRouterBlackListEntry.setStatus(_A)
class _ArrisRouterBlackListIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_ArrisRouterBlackListIndex_Type.__name__=_D
_ArrisRouterBlackListIndex_Object=MibTableColumn
arrisRouterBlackListIndex=_ArrisRouterBlackListIndex_Object((1,3,6,1,4,1,4115,1,20,1,1,4,20,12,1,1),_ArrisRouterBlackListIndex_Type())
arrisRouterBlackListIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:arrisRouterBlackListIndex.setStatus(_A)
class _ArrisRouterBlackListDomain_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ArrisRouterBlackListDomain_Type.__name__=_G
_ArrisRouterBlackListDomain_Object=MibTableColumn
arrisRouterBlackListDomain=_ArrisRouterBlackListDomain_Object((1,3,6,1,4,1,4115,1,20,1,1,4,20,12,1,2),_ArrisRouterBlackListDomain_Type())
arrisRouterBlackListDomain.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterBlackListDomain.setStatus(_A)
_ArrisRouterBlackListTOD_Type=Integer32
_ArrisRouterBlackListTOD_Object=MibTableColumn
arrisRouterBlackListTOD=_ArrisRouterBlackListTOD_Object((1,3,6,1,4,1,4115,1,20,1,1,4,20,12,1,3),_ArrisRouterBlackListTOD_Type())
arrisRouterBlackListTOD.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterBlackListTOD.setStatus(_A)
_ArrisRouterBlackListStatus_Type=RowStatus
_ArrisRouterBlackListStatus_Object=MibTableColumn
arrisRouterBlackListStatus=_ArrisRouterBlackListStatus_Object((1,3,6,1,4,1,4115,1,20,1,1,4,20,12,1,4),_ArrisRouterBlackListStatus_Type())
arrisRouterBlackListStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterBlackListStatus.setStatus(_A)
_ArrisRouterWhiteListTable_Object=MibTable
arrisRouterWhiteListTable=_ArrisRouterWhiteListTable_Object((1,3,6,1,4,1,4115,1,20,1,1,4,20,14))
if mibBuilder.loadTexts:arrisRouterWhiteListTable.setStatus(_A)
_ArrisRouterWhiteListEntry_Object=MibTableRow
arrisRouterWhiteListEntry=_ArrisRouterWhiteListEntry_Object((1,3,6,1,4,1,4115,1,20,1,1,4,20,14,1))
arrisRouterWhiteListEntry.setIndexNames((0,_I,_Av))
if mibBuilder.loadTexts:arrisRouterWhiteListEntry.setStatus(_A)
class _ArrisRouterWhiteListIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_ArrisRouterWhiteListIndex_Type.__name__=_D
_ArrisRouterWhiteListIndex_Object=MibTableColumn
arrisRouterWhiteListIndex=_ArrisRouterWhiteListIndex_Object((1,3,6,1,4,1,4115,1,20,1,1,4,20,14,1,1),_ArrisRouterWhiteListIndex_Type())
arrisRouterWhiteListIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:arrisRouterWhiteListIndex.setStatus(_A)
class _ArrisRouterWhiteListDomain_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ArrisRouterWhiteListDomain_Type.__name__=_G
_ArrisRouterWhiteListDomain_Object=MibTableColumn
arrisRouterWhiteListDomain=_ArrisRouterWhiteListDomain_Object((1,3,6,1,4,1,4115,1,20,1,1,4,20,14,1,2),_ArrisRouterWhiteListDomain_Type())
arrisRouterWhiteListDomain.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterWhiteListDomain.setStatus(_A)
_ArrisRouterWhiteListTOD_Type=Integer32
_ArrisRouterWhiteListTOD_Object=MibTableColumn
arrisRouterWhiteListTOD=_ArrisRouterWhiteListTOD_Object((1,3,6,1,4,1,4115,1,20,1,1,4,20,14,1,3),_ArrisRouterWhiteListTOD_Type())
arrisRouterWhiteListTOD.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWhiteListTOD.setStatus(_A)
_ArrisRouterWhiteListStatus_Type=RowStatus
_ArrisRouterWhiteListStatus_Object=MibTableColumn
arrisRouterWhiteListStatus=_ArrisRouterWhiteListStatus_Object((1,3,6,1,4,1,4115,1,20,1,1,4,20,14,1,4),_ArrisRouterWhiteListStatus_Type())
arrisRouterWhiteListStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterWhiteListStatus.setStatus(_A)
_ArrisRouterTrustedDeviceTable_Object=MibTable
arrisRouterTrustedDeviceTable=_ArrisRouterTrustedDeviceTable_Object((1,3,6,1,4,1,4115,1,20,1,1,4,20,16))
if mibBuilder.loadTexts:arrisRouterTrustedDeviceTable.setStatus(_A)
_ArrisRouterTrustedDeviceEntry_Object=MibTableRow
arrisRouterTrustedDeviceEntry=_ArrisRouterTrustedDeviceEntry_Object((1,3,6,1,4,1,4115,1,20,1,1,4,20,16,1))
arrisRouterTrustedDeviceEntry.setIndexNames((0,_I,_Aw))
if mibBuilder.loadTexts:arrisRouterTrustedDeviceEntry.setStatus(_A)
class _ArrisRouterTrustedDeviceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_ArrisRouterTrustedDeviceIndex_Type.__name__=_D
_ArrisRouterTrustedDeviceIndex_Object=MibTableColumn
arrisRouterTrustedDeviceIndex=_ArrisRouterTrustedDeviceIndex_Object((1,3,6,1,4,1,4115,1,20,1,1,4,20,16,1,1),_ArrisRouterTrustedDeviceIndex_Type())
arrisRouterTrustedDeviceIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:arrisRouterTrustedDeviceIndex.setStatus(_A)
_ArrisRouterTrustedDeviceMAC_Type=MacAddress
_ArrisRouterTrustedDeviceMAC_Object=MibTableColumn
arrisRouterTrustedDeviceMAC=_ArrisRouterTrustedDeviceMAC_Object((1,3,6,1,4,1,4115,1,20,1,1,4,20,16,1,2),_ArrisRouterTrustedDeviceMAC_Type())
arrisRouterTrustedDeviceMAC.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterTrustedDeviceMAC.setStatus(_A)
_ArrisRouterTrustedDeviceStatus_Type=RowStatus
_ArrisRouterTrustedDeviceStatus_Object=MibTableColumn
arrisRouterTrustedDeviceStatus=_ArrisRouterTrustedDeviceStatus_Object((1,3,6,1,4,1,4115,1,20,1,1,4,20,16,1,3),_ArrisRouterTrustedDeviceStatus_Type())
arrisRouterTrustedDeviceStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterTrustedDeviceStatus.setStatus(_A)
_ArrisRouterTrustedDeviceName_Type=DisplayString
_ArrisRouterTrustedDeviceName_Object=MibTableColumn
arrisRouterTrustedDeviceName=_ArrisRouterTrustedDeviceName_Object((1,3,6,1,4,1,4115,1,20,1,1,4,20,16,1,4),_ArrisRouterTrustedDeviceName_Type())
arrisRouterTrustedDeviceName.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterTrustedDeviceName.setStatus(_A)
_ArrisRouterTrustedDeviceAddrType_Type=InetAddressType
_ArrisRouterTrustedDeviceAddrType_Object=MibTableColumn
arrisRouterTrustedDeviceAddrType=_ArrisRouterTrustedDeviceAddrType_Object((1,3,6,1,4,1,4115,1,20,1,1,4,20,16,1,5),_ArrisRouterTrustedDeviceAddrType_Type())
arrisRouterTrustedDeviceAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterTrustedDeviceAddrType.setStatus(_A)
_ArrisRouterTrustedDeviceAddr_Type=InetAddress
_ArrisRouterTrustedDeviceAddr_Object=MibTableColumn
arrisRouterTrustedDeviceAddr=_ArrisRouterTrustedDeviceAddr_Object((1,3,6,1,4,1,4115,1,20,1,1,4,20,16,1,6),_ArrisRouterTrustedDeviceAddr_Type())
arrisRouterTrustedDeviceAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterTrustedDeviceAddr.setStatus(_A)
class _ArrisRouterEnableParentalCont_Type(TruthValue):defaultValue=2
_ArrisRouterEnableParentalCont_Type.__name__=_F
_ArrisRouterEnableParentalCont_Object=MibScalar
arrisRouterEnableParentalCont=_ArrisRouterEnableParentalCont_Object((1,3,6,1,4,1,4115,1,20,1,1,4,20,17),_ArrisRouterEnableParentalCont_Type())
arrisRouterEnableParentalCont.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterEnableParentalCont.setStatus(_A)
class _ArrisRouterListActiveType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('blackList',1),('whiteList',2)))
_ArrisRouterListActiveType_Type.__name__=_D
_ArrisRouterListActiveType_Object=MibScalar
arrisRouterListActiveType=_ArrisRouterListActiveType_Object((1,3,6,1,4,1,4115,1,20,1,1,4,20,22),_ArrisRouterListActiveType_Type())
arrisRouterListActiveType.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterListActiveType.setStatus(_A)
_ArrisRouterExceptionListCount_Type=Integer32
_ArrisRouterExceptionListCount_Object=MibScalar
arrisRouterExceptionListCount=_ArrisRouterExceptionListCount_Object((1,3,6,1,4,1,4115,1,20,1,1,4,20,24),_ArrisRouterExceptionListCount_Type())
arrisRouterExceptionListCount.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterExceptionListCount.setStatus(_A)
_ArrisRouterExceptionListTable_Object=MibTable
arrisRouterExceptionListTable=_ArrisRouterExceptionListTable_Object((1,3,6,1,4,1,4115,1,20,1,1,4,20,25))
if mibBuilder.loadTexts:arrisRouterExceptionListTable.setStatus(_A)
_ArrisRouterExceptionListEntry_Object=MibTableRow
arrisRouterExceptionListEntry=_ArrisRouterExceptionListEntry_Object((1,3,6,1,4,1,4115,1,20,1,1,4,20,25,1))
arrisRouterExceptionListEntry.setIndexNames((0,_I,_Ax))
if mibBuilder.loadTexts:arrisRouterExceptionListEntry.setStatus(_A)
class _ArrisRouterExceptionListIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_ArrisRouterExceptionListIndex_Type.__name__=_D
_ArrisRouterExceptionListIndex_Object=MibTableColumn
arrisRouterExceptionListIndex=_ArrisRouterExceptionListIndex_Object((1,3,6,1,4,1,4115,1,20,1,1,4,20,25,1,1),_ArrisRouterExceptionListIndex_Type())
arrisRouterExceptionListIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:arrisRouterExceptionListIndex.setStatus(_A)
class _ArrisRouterExceptionListDomain_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ArrisRouterExceptionListDomain_Type.__name__=_G
_ArrisRouterExceptionListDomain_Object=MibTableColumn
arrisRouterExceptionListDomain=_ArrisRouterExceptionListDomain_Object((1,3,6,1,4,1,4115,1,20,1,1,4,20,25,1,2),_ArrisRouterExceptionListDomain_Type())
arrisRouterExceptionListDomain.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterExceptionListDomain.setStatus(_A)
_ArrisRouterExceptionListStatus_Type=RowStatus
_ArrisRouterExceptionListStatus_Object=MibTableColumn
arrisRouterExceptionListStatus=_ArrisRouterExceptionListStatus_Object((1,3,6,1,4,1,4115,1,20,1,1,4,20,25,1,3),_ArrisRouterExceptionListStatus_Type())
arrisRouterExceptionListStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterExceptionListStatus.setStatus(_A)
class _ArrisRouterFWAllowICMP_Type(TruthValue):defaultValue=1
_ArrisRouterFWAllowICMP_Type.__name__=_F
_ArrisRouterFWAllowICMP_Object=MibScalar
arrisRouterFWAllowICMP=_ArrisRouterFWAllowICMP_Object((1,3,6,1,4,1,4115,1,20,1,1,4,21),_ArrisRouterFWAllowICMP_Type())
arrisRouterFWAllowICMP.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterFWAllowICMP.setStatus(_A)
class _ArrisRouterFWVirtSrvTableEnabled_Type(TruthValue):defaultValue=1
_ArrisRouterFWVirtSrvTableEnabled_Type.__name__=_F
_ArrisRouterFWVirtSrvTableEnabled_Object=MibScalar
arrisRouterFWVirtSrvTableEnabled=_ArrisRouterFWVirtSrvTableEnabled_Object((1,3,6,1,4,1,4115,1,20,1,1,4,32),_ArrisRouterFWVirtSrvTableEnabled_Type())
arrisRouterFWVirtSrvTableEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterFWVirtSrvTableEnabled.setStatus(_A)
class _ArrisRouterFWPortTrigTableEnabled_Type(TruthValue):defaultValue=1
_ArrisRouterFWPortTrigTableEnabled_Type.__name__=_F
_ArrisRouterFWPortTrigTableEnabled_Object=MibScalar
arrisRouterFWPortTrigTableEnabled=_ArrisRouterFWPortTrigTableEnabled_Object((1,3,6,1,4,1,4115,1,20,1,1,4,33),_ArrisRouterFWPortTrigTableEnabled_Type())
arrisRouterFWPortTrigTableEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterFWPortTrigTableEnabled.setStatus(_A)
_ArrisRouterFWIPv6Security_ObjectIdentity=ObjectIdentity
arrisRouterFWIPv6Security=_ArrisRouterFWIPv6Security_ObjectIdentity((1,3,6,1,4,1,4115,1,20,1,1,4,40))
class _ArrisRouterFWIPv6Enable_Type(TruthValue):defaultValue=1
_ArrisRouterFWIPv6Enable_Type.__name__=_F
_ArrisRouterFWIPv6Enable_Object=MibScalar
arrisRouterFWIPv6Enable=_ArrisRouterFWIPv6Enable_Object((1,3,6,1,4,1,4115,1,20,1,1,4,40,7),_ArrisRouterFWIPv6Enable_Type())
arrisRouterFWIPv6Enable.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterFWIPv6Enable.setStatus(_A)
class _ArrisRouterFWMacBridgingWebPageEnabled_Type(TruthValue):defaultValue=2
_ArrisRouterFWMacBridgingWebPageEnabled_Type.__name__=_F
_ArrisRouterFWMacBridgingWebPageEnabled_Object=MibScalar
arrisRouterFWMacBridgingWebPageEnabled=_ArrisRouterFWMacBridgingWebPageEnabled_Object((1,3,6,1,4,1,4115,1,20,1,1,4,41),_ArrisRouterFWMacBridgingWebPageEnabled_Type())
arrisRouterFWMacBridgingWebPageEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterFWMacBridgingWebPageEnabled.setStatus(_A)
class _ArrisRouterFWMacBridgingFunctionEnabled_Type(TruthValue):defaultValue=2
_ArrisRouterFWMacBridgingFunctionEnabled_Type.__name__=_F
_ArrisRouterFWMacBridgingFunctionEnabled_Object=MibScalar
arrisRouterFWMacBridgingFunctionEnabled=_ArrisRouterFWMacBridgingFunctionEnabled_Object((1,3,6,1,4,1,4115,1,20,1,1,4,42),_ArrisRouterFWMacBridgingFunctionEnabled_Type())
arrisRouterFWMacBridgingFunctionEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterFWMacBridgingFunctionEnabled.setStatus(_A)
_ArrisRouterFWMacBridgingTable_Object=MibTable
arrisRouterFWMacBridgingTable=_ArrisRouterFWMacBridgingTable_Object((1,3,6,1,4,1,4115,1,20,1,1,4,43))
if mibBuilder.loadTexts:arrisRouterFWMacBridgingTable.setStatus(_A)
_ArrisRouterFWMacBridgingEntry_Object=MibTableRow
arrisRouterFWMacBridgingEntry=_ArrisRouterFWMacBridgingEntry_Object((1,3,6,1,4,1,4115,1,20,1,1,4,43,1))
arrisRouterFWMacBridgingEntry.setIndexNames((0,_I,_Ay))
if mibBuilder.loadTexts:arrisRouterFWMacBridgingEntry.setStatus(_A)
class _ArrisRouterFWMacBridgingIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_ArrisRouterFWMacBridgingIndex_Type.__name__=_D
_ArrisRouterFWMacBridgingIndex_Object=MibTableColumn
arrisRouterFWMacBridgingIndex=_ArrisRouterFWMacBridgingIndex_Object((1,3,6,1,4,1,4115,1,20,1,1,4,43,1,1),_ArrisRouterFWMacBridgingIndex_Type())
arrisRouterFWMacBridgingIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:arrisRouterFWMacBridgingIndex.setStatus(_A)
class _ArrisRouterFWMacBridgingName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ArrisRouterFWMacBridgingName_Type.__name__=_G
_ArrisRouterFWMacBridgingName_Object=MibTableColumn
arrisRouterFWMacBridgingName=_ArrisRouterFWMacBridgingName_Object((1,3,6,1,4,1,4115,1,20,1,1,4,43,1,2),_ArrisRouterFWMacBridgingName_Type())
arrisRouterFWMacBridgingName.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterFWMacBridgingName.setStatus(_A)
_ArrisRouterFWMacBridgingMACAddr_Type=MacAddress
_ArrisRouterFWMacBridgingMACAddr_Object=MibTableColumn
arrisRouterFWMacBridgingMACAddr=_ArrisRouterFWMacBridgingMACAddr_Object((1,3,6,1,4,1,4115,1,20,1,1,4,43,1,3),_ArrisRouterFWMacBridgingMACAddr_Type())
arrisRouterFWMacBridgingMACAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterFWMacBridgingMACAddr.setStatus(_A)
_ArrisRouterFWMacBridgingRowStatus_Type=RowStatus
_ArrisRouterFWMacBridgingRowStatus_Object=MibTableColumn
arrisRouterFWMacBridgingRowStatus=_ArrisRouterFWMacBridgingRowStatus_Object((1,3,6,1,4,1,4115,1,20,1,1,4,43,1,4),_ArrisRouterFWMacBridgingRowStatus_Type())
arrisRouterFWMacBridgingRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterFWMacBridgingRowStatus.setStatus(_A)
_ArrisRouterFWPortAllowTable_Object=MibTable
arrisRouterFWPortAllowTable=_ArrisRouterFWPortAllowTable_Object((1,3,6,1,4,1,4115,1,20,1,1,4,44))
if mibBuilder.loadTexts:arrisRouterFWPortAllowTable.setStatus(_A)
_ArrisRouterFWPortAllowEntry_Object=MibTableRow
arrisRouterFWPortAllowEntry=_ArrisRouterFWPortAllowEntry_Object((1,3,6,1,4,1,4115,1,20,1,1,4,44,1))
arrisRouterFWPortAllowEntry.setIndexNames((0,_I,_Az))
if mibBuilder.loadTexts:arrisRouterFWPortAllowEntry.setStatus(_A)
_ArrisRouterFWPortAllowIndex_Type=Unsigned32
_ArrisRouterFWPortAllowIndex_Object=MibTableColumn
arrisRouterFWPortAllowIndex=_ArrisRouterFWPortAllowIndex_Object((1,3,6,1,4,1,4115,1,20,1,1,4,44,1,1),_ArrisRouterFWPortAllowIndex_Type())
arrisRouterFWPortAllowIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:arrisRouterFWPortAllowIndex.setStatus(_A)
class _ArrisRouterFWPortAllowInboundPort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ArrisRouterFWPortAllowInboundPort_Type.__name__=_H
_ArrisRouterFWPortAllowInboundPort_Object=MibTableColumn
arrisRouterFWPortAllowInboundPort=_ArrisRouterFWPortAllowInboundPort_Object((1,3,6,1,4,1,4115,1,20,1,1,4,44,1,2),_ArrisRouterFWPortAllowInboundPort_Type())
arrisRouterFWPortAllowInboundPort.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterFWPortAllowInboundPort.setStatus(_A)
_ArrisRouterFWPortAllowRowStatus_Type=RowStatus
_ArrisRouterFWPortAllowRowStatus_Object=MibTableColumn
arrisRouterFWPortAllowRowStatus=_ArrisRouterFWPortAllowRowStatus_Object((1,3,6,1,4,1,4115,1,20,1,1,4,44,1,3),_ArrisRouterFWPortAllowRowStatus_Type())
arrisRouterFWPortAllowRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterFWPortAllowRowStatus.setStatus(_A)
class _ArrisRouterFWSrvTr69LastInstance_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ArrisRouterFWSrvTr69LastInstance_Type.__name__=_H
_ArrisRouterFWSrvTr69LastInstance_Object=MibScalar
arrisRouterFWSrvTr69LastInstance=_ArrisRouterFWSrvTr69LastInstance_Object((1,3,6,1,4,1,4115,1,20,1,1,4,46),_ArrisRouterFWSrvTr69LastInstance_Type())
arrisRouterFWSrvTr69LastInstance.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterFWSrvTr69LastInstance.setStatus(_A)
_ArrisRouterSysCfg_ObjectIdentity=ObjectIdentity
arrisRouterSysCfg=_ArrisRouterSysCfg_ObjectIdentity((1,3,6,1,4,1,4115,1,20,1,1,5))
class _ArrisRouterAdminPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ArrisRouterAdminPassword_Type.__name__=_G
_ArrisRouterAdminPassword_Object=MibScalar
arrisRouterAdminPassword=_ArrisRouterAdminPassword_Object((1,3,6,1,4,1,4115,1,20,1,1,5,1),_ArrisRouterAdminPassword_Type())
arrisRouterAdminPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterAdminPassword.setStatus(_A)
class _ArrisRouterAdminTimeout_Type(Unsigned32):defaultValue=600
_ArrisRouterAdminTimeout_Type.__name__=_H
_ArrisRouterAdminTimeout_Object=MibScalar
arrisRouterAdminTimeout=_ArrisRouterAdminTimeout_Object((1,3,6,1,4,1,4115,1,20,1,1,5,2),_ArrisRouterAdminTimeout_Type())
arrisRouterAdminTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterAdminTimeout.setStatus(_A)
if mibBuilder.loadTexts:arrisRouterAdminTimeout.setUnits(_M)
_ArrisRouterTimeZoneUTCOffset_Type=Integer32
_ArrisRouterTimeZoneUTCOffset_Object=MibScalar
arrisRouterTimeZoneUTCOffset=_ArrisRouterTimeZoneUTCOffset_Object((1,3,6,1,4,1,4115,1,20,1,1,5,3),_ArrisRouterTimeZoneUTCOffset_Type())
arrisRouterTimeZoneUTCOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterTimeZoneUTCOffset.setStatus(_A)
class _ArrisRouterReboot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('restart',1))
_ArrisRouterReboot_Type.__name__=_D
_ArrisRouterReboot_Object=MibScalar
arrisRouterReboot=_ArrisRouterReboot_Object((1,3,6,1,4,1,4115,1,20,1,1,5,4),_ArrisRouterReboot_Type())
arrisRouterReboot.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterReboot.setStatus(_A)
class _ArrisRouterDefaults_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,6)));namedValues=NamedValues(*(('restoreAll',3),('restoreAllNoReboot',6)))
_ArrisRouterDefaults_Type.__name__=_D
_ArrisRouterDefaults_Object=MibScalar
arrisRouterDefaults=_ArrisRouterDefaults_Object((1,3,6,1,4,1,4115,1,20,1,1,5,5),_ArrisRouterDefaults_Type())
arrisRouterDefaults.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterDefaults.setStatus(_A)
class _ArrisRouterLanguage_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ArrisRouterLanguage_Type.__name__=_G
_ArrisRouterLanguage_Object=MibScalar
arrisRouterLanguage=_ArrisRouterLanguage_Object((1,3,6,1,4,1,4115,1,20,1,1,5,6),_ArrisRouterLanguage_Type())
arrisRouterLanguage.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterLanguage.setStatus(_A)
class _ArrisRouterName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ArrisRouterName_Type.__name__=_G
_ArrisRouterName_Object=MibScalar
arrisRouterName=_ArrisRouterName_Object((1,3,6,1,4,1,4115,1,20,1,1,5,7),_ArrisRouterName_Type())
arrisRouterName.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterName.setStatus(_A)
class _ArrisRouterSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ArrisRouterSerialNumber_Type.__name__=_G
_ArrisRouterSerialNumber_Object=MibScalar
arrisRouterSerialNumber=_ArrisRouterSerialNumber_Object((1,3,6,1,4,1,4115,1,20,1,1,5,8),_ArrisRouterSerialNumber_Type())
arrisRouterSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterSerialNumber.setStatus(_A)
class _ArrisRouterBootCodeVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ArrisRouterBootCodeVersion_Type.__name__=_G
_ArrisRouterBootCodeVersion_Object=MibScalar
arrisRouterBootCodeVersion=_ArrisRouterBootCodeVersion_Object((1,3,6,1,4,1,4115,1,20,1,1,5,9),_ArrisRouterBootCodeVersion_Type())
arrisRouterBootCodeVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterBootCodeVersion.setStatus(_A)
class _ArrisRouterHardwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ArrisRouterHardwareVersion_Type.__name__=_G
_ArrisRouterHardwareVersion_Object=MibScalar
arrisRouterHardwareVersion=_ArrisRouterHardwareVersion_Object((1,3,6,1,4,1,4115,1,20,1,1,5,10),_ArrisRouterHardwareVersion_Type())
arrisRouterHardwareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterHardwareVersion.setStatus(_A)
class _ArrisRouterFirmwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ArrisRouterFirmwareVersion_Type.__name__=_G
_ArrisRouterFirmwareVersion_Object=MibScalar
arrisRouterFirmwareVersion=_ArrisRouterFirmwareVersion_Object((1,3,6,1,4,1,4115,1,20,1,1,5,11),_ArrisRouterFirmwareVersion_Type())
arrisRouterFirmwareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterFirmwareVersion.setStatus(_A)
class _ArrisRouterLogLevel_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('noLogging',0),('logError',1),('logWarn',2),('logInfo',3)))
_ArrisRouterLogLevel_Type.__name__=_D
_ArrisRouterLogLevel_Object=MibScalar
arrisRouterLogLevel=_ArrisRouterLogLevel_Object((1,3,6,1,4,1,4115,1,20,1,1,5,12),_ArrisRouterLogLevel_Type())
arrisRouterLogLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterLogLevel.setStatus(_A)
_ArrisRouterCustomSettings_Type=DisplayString
_ArrisRouterCustomSettings_Object=MibScalar
arrisRouterCustomSettings=_ArrisRouterCustomSettings_Object((1,3,6,1,4,1,4115,1,20,1,1,5,13),_ArrisRouterCustomSettings_Type())
arrisRouterCustomSettings.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterCustomSettings.setStatus(_A)
_ArrisRouterCustomID_Type=Integer32
_ArrisRouterCustomID_Object=MibScalar
arrisRouterCustomID=_ArrisRouterCustomID_Object((1,3,6,1,4,1,4115,1,20,1,1,5,14),_ArrisRouterCustomID_Type())
arrisRouterCustomID.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterCustomID.setStatus(_A)
_ArrisRouterCurrentTime_Type=DateAndTime
_ArrisRouterCurrentTime_Object=MibScalar
arrisRouterCurrentTime=_ArrisRouterCurrentTime_Object((1,3,6,1,4,1,4115,1,20,1,1,5,15),_ArrisRouterCurrentTime_Type())
arrisRouterCurrentTime.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterCurrentTime.setStatus(_A)
_ArrisRouterAuthTable_Object=MibTable
arrisRouterAuthTable=_ArrisRouterAuthTable_Object((1,3,6,1,4,1,4115,1,20,1,1,5,16))
if mibBuilder.loadTexts:arrisRouterAuthTable.setStatus(_A)
_ArrisRouterAuthEntry_Object=MibTableRow
arrisRouterAuthEntry=_ArrisRouterAuthEntry_Object((1,3,6,1,4,1,4115,1,20,1,1,5,16,1))
arrisRouterAuthEntry.setIndexNames((0,_I,_h))
if mibBuilder.loadTexts:arrisRouterAuthEntry.setStatus(_A)
_ArrisRouterAuthIndex_Type=Unsigned32
_ArrisRouterAuthIndex_Object=MibTableColumn
arrisRouterAuthIndex=_ArrisRouterAuthIndex_Object((1,3,6,1,4,1,4115,1,20,1,1,5,16,1,1),_ArrisRouterAuthIndex_Type())
arrisRouterAuthIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:arrisRouterAuthIndex.setStatus(_A)
class _ArrisRouterAuthUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ArrisRouterAuthUserName_Type.__name__=_G
_ArrisRouterAuthUserName_Object=MibTableColumn
arrisRouterAuthUserName=_ArrisRouterAuthUserName_Object((1,3,6,1,4,1,4115,1,20,1,1,5,16,1,2),_ArrisRouterAuthUserName_Type())
arrisRouterAuthUserName.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterAuthUserName.setStatus(_A)
class _ArrisRouterAuthPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ArrisRouterAuthPassword_Type.__name__=_G
_ArrisRouterAuthPassword_Object=MibTableColumn
arrisRouterAuthPassword=_ArrisRouterAuthPassword_Object((1,3,6,1,4,1,4115,1,20,1,1,5,16,1,3),_ArrisRouterAuthPassword_Type())
arrisRouterAuthPassword.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterAuthPassword.setStatus(_A)
class _ArrisRouterAuthType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ArrisRouterAuthType_Type.__name__=_G
_ArrisRouterAuthType_Object=MibTableColumn
arrisRouterAuthType=_ArrisRouterAuthType_Object((1,3,6,1,4,1,4115,1,20,1,1,5,16,1,4),_ArrisRouterAuthType_Type())
arrisRouterAuthType.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterAuthType.setStatus(_A)
_ArrisRouterAuthAccountEnabled_Type=TruthValue
_ArrisRouterAuthAccountEnabled_Object=MibTableColumn
arrisRouterAuthAccountEnabled=_ArrisRouterAuthAccountEnabled_Object((1,3,6,1,4,1,4115,1,20,1,1,5,16,1,6),_ArrisRouterAuthAccountEnabled_Type())
arrisRouterAuthAccountEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterAuthAccountEnabled.setStatus(_A)
_ArrisRouterSNTPSettings_ObjectIdentity=ObjectIdentity
arrisRouterSNTPSettings=_ArrisRouterSNTPSettings_ObjectIdentity((1,3,6,1,4,1,4115,1,20,1,1,5,17))
class _ArrisRouterEnableSNTP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disable',0),('enable',1)))
_ArrisRouterEnableSNTP_Type.__name__=_D
_ArrisRouterEnableSNTP_Object=MibScalar
arrisRouterEnableSNTP=_ArrisRouterEnableSNTP_Object((1,3,6,1,4,1,4115,1,20,1,1,5,17,1),_ArrisRouterEnableSNTP_Type())
arrisRouterEnableSNTP.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterEnableSNTP.setStatus(_A)
_ArrisRouterSNTPServerTable_Object=MibTable
arrisRouterSNTPServerTable=_ArrisRouterSNTPServerTable_Object((1,3,6,1,4,1,4115,1,20,1,1,5,17,4))
if mibBuilder.loadTexts:arrisRouterSNTPServerTable.setStatus(_A)
_ArrisRouterSNTPServerEntry_Object=MibTableRow
arrisRouterSNTPServerEntry=_ArrisRouterSNTPServerEntry_Object((1,3,6,1,4,1,4115,1,20,1,1,5,17,4,1))
arrisRouterSNTPServerEntry.setIndexNames((0,_I,_A_))
if mibBuilder.loadTexts:arrisRouterSNTPServerEntry.setStatus(_A)
class _ArrisRouterSNTPServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_ArrisRouterSNTPServerIndex_Type.__name__=_D
_ArrisRouterSNTPServerIndex_Object=MibTableColumn
arrisRouterSNTPServerIndex=_ArrisRouterSNTPServerIndex_Object((1,3,6,1,4,1,4115,1,20,1,1,5,17,4,1,1),_ArrisRouterSNTPServerIndex_Type())
arrisRouterSNTPServerIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:arrisRouterSNTPServerIndex.setStatus(_A)
_ArrisRouterSNTPServerAddrType_Type=InetAddressType
_ArrisRouterSNTPServerAddrType_Object=MibTableColumn
arrisRouterSNTPServerAddrType=_ArrisRouterSNTPServerAddrType_Object((1,3,6,1,4,1,4115,1,20,1,1,5,17,4,1,2),_ArrisRouterSNTPServerAddrType_Type())
arrisRouterSNTPServerAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterSNTPServerAddrType.setStatus(_A)
_ArrisRouterSNTPServerAddr_Type=InetAddress
_ArrisRouterSNTPServerAddr_Object=MibTableColumn
arrisRouterSNTPServerAddr=_ArrisRouterSNTPServerAddr_Object((1,3,6,1,4,1,4115,1,20,1,1,5,17,4,1,3),_ArrisRouterSNTPServerAddr_Type())
arrisRouterSNTPServerAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterSNTPServerAddr.setStatus(_A)
class _ArrisRouterSNTPServerName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ArrisRouterSNTPServerName_Type.__name__=_G
_ArrisRouterSNTPServerName_Object=MibTableColumn
arrisRouterSNTPServerName=_ArrisRouterSNTPServerName_Object((1,3,6,1,4,1,4115,1,20,1,1,5,17,4,1,4),_ArrisRouterSNTPServerName_Type())
arrisRouterSNTPServerName.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterSNTPServerName.setStatus(_A)
_ArrisRouterSNTPServerStatus_Type=RowStatus
_ArrisRouterSNTPServerStatus_Object=MibTableColumn
arrisRouterSNTPServerStatus=_ArrisRouterSNTPServerStatus_Object((1,3,6,1,4,1,4115,1,20,1,1,5,17,4,1,5),_ArrisRouterSNTPServerStatus_Type())
arrisRouterSNTPServerStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterSNTPServerStatus.setStatus(_A)
_ArrisRouterEmailSettings_ObjectIdentity=ObjectIdentity
arrisRouterEmailSettings=_ArrisRouterEmailSettings_ObjectIdentity((1,3,6,1,4,1,4115,1,20,1,1,5,18))
_ArrisRouterEmailServerName_Type=DisplayString
_ArrisRouterEmailServerName_Object=MibScalar
arrisRouterEmailServerName=_ArrisRouterEmailServerName_Object((1,3,6,1,4,1,4115,1,20,1,1,5,18,1),_ArrisRouterEmailServerName_Type())
arrisRouterEmailServerName.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterEmailServerName.setStatus(_A)
_ArrisRouterEmailServerUser_Type=DisplayString
_ArrisRouterEmailServerUser_Object=MibScalar
arrisRouterEmailServerUser=_ArrisRouterEmailServerUser_Object((1,3,6,1,4,1,4115,1,20,1,1,5,18,2),_ArrisRouterEmailServerUser_Type())
arrisRouterEmailServerUser.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterEmailServerUser.setStatus(_A)
_ArrisRouterEmailServerPW_Type=DisplayString
_ArrisRouterEmailServerPW_Object=MibScalar
arrisRouterEmailServerPW=_ArrisRouterEmailServerPW_Object((1,3,6,1,4,1,4115,1,20,1,1,5,18,3),_ArrisRouterEmailServerPW_Type())
arrisRouterEmailServerPW.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterEmailServerPW.setStatus(_A)
_ArrisRouterEmailAddress_Type=DisplayString
_ArrisRouterEmailAddress_Object=MibScalar
arrisRouterEmailAddress=_ArrisRouterEmailAddress_Object((1,3,6,1,4,1,4115,1,20,1,1,5,18,4),_ArrisRouterEmailAddress_Type())
arrisRouterEmailAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterEmailAddress.setStatus(_A)
class _ArrisRouterEnableLogEmail_Type(TruthValue):defaultValue=2
_ArrisRouterEnableLogEmail_Type.__name__=_F
_ArrisRouterEnableLogEmail_Object=MibScalar
arrisRouterEnableLogEmail=_ArrisRouterEnableLogEmail_Object((1,3,6,1,4,1,4115,1,20,1,1,5,18,5),_ArrisRouterEnableLogEmail_Type())
arrisRouterEnableLogEmail.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterEnableLogEmail.setStatus(_A)
class _ArrisRouterEmailApplySettings_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_B0,1))
_ArrisRouterEmailApplySettings_Type.__name__=_D
_ArrisRouterEmailApplySettings_Object=MibScalar
arrisRouterEmailApplySettings=_ArrisRouterEmailApplySettings_Object((1,3,6,1,4,1,4115,1,20,1,1,5,18,6),_ArrisRouterEmailApplySettings_Type())
arrisRouterEmailApplySettings.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterEmailApplySettings.setStatus(_A)
_ArrisRouterEmailSenderAddress_Type=DisplayString
_ArrisRouterEmailSenderAddress_Object=MibScalar
arrisRouterEmailSenderAddress=_ArrisRouterEmailSenderAddress_Object((1,3,6,1,4,1,4115,1,20,1,1,5,18,8),_ArrisRouterEmailSenderAddress_Type())
arrisRouterEmailSenderAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterEmailSenderAddress.setStatus(_A)
class _ArrisRouterEmailSend_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('networkCredential',1),('modemCredential',2)))
_ArrisRouterEmailSend_Type.__name__=_D
_ArrisRouterEmailSend_Object=MibScalar
arrisRouterEmailSend=_ArrisRouterEmailSend_Object((1,3,6,1,4,1,4115,1,20,1,1,5,18,9),_ArrisRouterEmailSend_Type())
arrisRouterEmailSend.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterEmailSend.setStatus(_A)
_ArrisRouterLogSettings_ObjectIdentity=ObjectIdentity
arrisRouterLogSettings=_ArrisRouterLogSettings_ObjectIdentity((1,3,6,1,4,1,4115,1,20,1,1,5,19))
_ArrisRouterUserLogs_ObjectIdentity=ObjectIdentity
arrisRouterUserLogs=_ArrisRouterUserLogs_ObjectIdentity((1,3,6,1,4,1,4115,1,20,1,1,5,19,1))
_ArrisRouterFirewallLogTable_Object=MibTable
arrisRouterFirewallLogTable=_ArrisRouterFirewallLogTable_Object((1,3,6,1,4,1,4115,1,20,1,1,5,19,1,1))
if mibBuilder.loadTexts:arrisRouterFirewallLogTable.setStatus(_A)
_ArrisRouterFirewallLogEntry_Object=MibTableRow
arrisRouterFirewallLogEntry=_ArrisRouterFirewallLogEntry_Object((1,3,6,1,4,1,4115,1,20,1,1,5,19,1,1,1))
arrisRouterFirewallLogEntry.setIndexNames((0,_I,_B1))
if mibBuilder.loadTexts:arrisRouterFirewallLogEntry.setStatus(_A)
class _ArrisRouterFWLogIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_ArrisRouterFWLogIndex_Type.__name__=_D
_ArrisRouterFWLogIndex_Object=MibTableColumn
arrisRouterFWLogIndex=_ArrisRouterFWLogIndex_Object((1,3,6,1,4,1,4115,1,20,1,1,5,19,1,1,1,1),_ArrisRouterFWLogIndex_Type())
arrisRouterFWLogIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:arrisRouterFWLogIndex.setStatus(_A)
_ArrisRouterFWLogTime_Type=DateAndTime
_ArrisRouterFWLogTime_Object=MibTableColumn
arrisRouterFWLogTime=_ArrisRouterFWLogTime_Object((1,3,6,1,4,1,4115,1,20,1,1,5,19,1,1,1,2),_ArrisRouterFWLogTime_Type())
arrisRouterFWLogTime.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterFWLogTime.setStatus(_A)
_ArrisRouterFWLogInfo_Type=DisplayString
_ArrisRouterFWLogInfo_Object=MibTableColumn
arrisRouterFWLogInfo=_ArrisRouterFWLogInfo_Object((1,3,6,1,4,1,4115,1,20,1,1,5,19,1,1,1,3),_ArrisRouterFWLogInfo_Type())
arrisRouterFWLogInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterFWLogInfo.setStatus(_A)
_ArrisRouterParentalContLogTable_Object=MibTable
arrisRouterParentalContLogTable=_ArrisRouterParentalContLogTable_Object((1,3,6,1,4,1,4115,1,20,1,1,5,19,1,2))
if mibBuilder.loadTexts:arrisRouterParentalContLogTable.setStatus(_A)
_ArrisRouterParentalContLogEntry_Object=MibTableRow
arrisRouterParentalContLogEntry=_ArrisRouterParentalContLogEntry_Object((1,3,6,1,4,1,4115,1,20,1,1,5,19,1,2,1))
arrisRouterParentalContLogEntry.setIndexNames((0,_I,_B2))
if mibBuilder.loadTexts:arrisRouterParentalContLogEntry.setStatus(_A)
class _ArrisRouterPCLogIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_ArrisRouterPCLogIndex_Type.__name__=_D
_ArrisRouterPCLogIndex_Object=MibTableColumn
arrisRouterPCLogIndex=_ArrisRouterPCLogIndex_Object((1,3,6,1,4,1,4115,1,20,1,1,5,19,1,2,1,1),_ArrisRouterPCLogIndex_Type())
arrisRouterPCLogIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:arrisRouterPCLogIndex.setStatus(_A)
_ArrisRouterPCLogTime_Type=DateAndTime
_ArrisRouterPCLogTime_Object=MibTableColumn
arrisRouterPCLogTime=_ArrisRouterPCLogTime_Object((1,3,6,1,4,1,4115,1,20,1,1,5,19,1,2,1,2),_ArrisRouterPCLogTime_Type())
arrisRouterPCLogTime.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterPCLogTime.setStatus(_A)
_ArrisRouterPCLogInfo_Type=DisplayString
_ArrisRouterPCLogInfo_Object=MibTableColumn
arrisRouterPCLogInfo=_ArrisRouterPCLogInfo_Object((1,3,6,1,4,1,4115,1,20,1,1,5,19,1,2,1,3),_ArrisRouterPCLogInfo_Type())
arrisRouterPCLogInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterPCLogInfo.setStatus(_A)
class _ArrisRouterPCLogType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_ArrisRouterPCLogType_Type.__name__=_D
_ArrisRouterPCLogType_Object=MibTableColumn
arrisRouterPCLogType=_ArrisRouterPCLogType_Object((1,3,6,1,4,1,4115,1,20,1,1,5,19,1,2,1,4),_ArrisRouterPCLogType_Type())
arrisRouterPCLogType.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterPCLogType.setStatus(_A)
_ArrisRouterChangeLogTable_Object=MibTable
arrisRouterChangeLogTable=_ArrisRouterChangeLogTable_Object((1,3,6,1,4,1,4115,1,20,1,1,5,19,1,3))
if mibBuilder.loadTexts:arrisRouterChangeLogTable.setStatus(_A)
_ArrisRouterChangeLogEntry_Object=MibTableRow
arrisRouterChangeLogEntry=_ArrisRouterChangeLogEntry_Object((1,3,6,1,4,1,4115,1,20,1,1,5,19,1,3,1))
arrisRouterChangeLogEntry.setIndexNames((0,_I,_B3))
if mibBuilder.loadTexts:arrisRouterChangeLogEntry.setStatus(_A)
class _ArrisRouterChangeLogIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,40))
_ArrisRouterChangeLogIndex_Type.__name__=_D
_ArrisRouterChangeLogIndex_Object=MibTableColumn
arrisRouterChangeLogIndex=_ArrisRouterChangeLogIndex_Object((1,3,6,1,4,1,4115,1,20,1,1,5,19,1,3,1,1),_ArrisRouterChangeLogIndex_Type())
arrisRouterChangeLogIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:arrisRouterChangeLogIndex.setStatus(_A)
_ArrisRouterChangeLogTime_Type=DateAndTime
_ArrisRouterChangeLogTime_Object=MibTableColumn
arrisRouterChangeLogTime=_ArrisRouterChangeLogTime_Object((1,3,6,1,4,1,4115,1,20,1,1,5,19,1,3,1,2),_ArrisRouterChangeLogTime_Type())
arrisRouterChangeLogTime.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterChangeLogTime.setStatus(_A)
_ArrisRouterChangeLogInfo_Type=DisplayString
_ArrisRouterChangeLogInfo_Object=MibTableColumn
arrisRouterChangeLogInfo=_ArrisRouterChangeLogInfo_Object((1,3,6,1,4,1,4115,1,20,1,1,5,19,1,3,1,3),_ArrisRouterChangeLogInfo_Type())
arrisRouterChangeLogInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterChangeLogInfo.setStatus(_A)
_ArrisRouterDebugLogTable_Object=MibTable
arrisRouterDebugLogTable=_ArrisRouterDebugLogTable_Object((1,3,6,1,4,1,4115,1,20,1,1,5,19,1,4))
if mibBuilder.loadTexts:arrisRouterDebugLogTable.setStatus(_A)
_ArrisRouterDebugLogEntry_Object=MibTableRow
arrisRouterDebugLogEntry=_ArrisRouterDebugLogEntry_Object((1,3,6,1,4,1,4115,1,20,1,1,5,19,1,4,1))
arrisRouterDebugLogEntry.setIndexNames((0,_I,_B4))
if mibBuilder.loadTexts:arrisRouterDebugLogEntry.setStatus(_A)
class _ArrisRouterDebugLogIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_ArrisRouterDebugLogIndex_Type.__name__=_D
_ArrisRouterDebugLogIndex_Object=MibTableColumn
arrisRouterDebugLogIndex=_ArrisRouterDebugLogIndex_Object((1,3,6,1,4,1,4115,1,20,1,1,5,19,1,4,1,1),_ArrisRouterDebugLogIndex_Type())
arrisRouterDebugLogIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:arrisRouterDebugLogIndex.setStatus(_A)
_ArrisRouterDebugLogTime_Type=DateAndTime
_ArrisRouterDebugLogTime_Object=MibTableColumn
arrisRouterDebugLogTime=_ArrisRouterDebugLogTime_Object((1,3,6,1,4,1,4115,1,20,1,1,5,19,1,4,1,2),_ArrisRouterDebugLogTime_Type())
arrisRouterDebugLogTime.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterDebugLogTime.setStatus(_A)
_ArrisRouterDebugLogInfo_Type=DisplayString
_ArrisRouterDebugLogInfo_Object=MibTableColumn
arrisRouterDebugLogInfo=_ArrisRouterDebugLogInfo_Object((1,3,6,1,4,1,4115,1,20,1,1,5,19,1,4,1,3),_ArrisRouterDebugLogInfo_Type())
arrisRouterDebugLogInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterDebugLogInfo.setStatus(_A)
_ArrisRouterFirewallLogExtTable_Object=MibTable
arrisRouterFirewallLogExtTable=_ArrisRouterFirewallLogExtTable_Object((1,3,6,1,4,1,4115,1,20,1,1,5,19,1,7))
if mibBuilder.loadTexts:arrisRouterFirewallLogExtTable.setStatus(_A)
_ArrisRouterFirewallLogExtEntry_Object=MibTableRow
arrisRouterFirewallLogExtEntry=_ArrisRouterFirewallLogExtEntry_Object((1,3,6,1,4,1,4115,1,20,1,1,5,19,1,7,1))
arrisRouterFirewallLogExtEntry.setIndexNames((0,_I,_B5))
if mibBuilder.loadTexts:arrisRouterFirewallLogExtEntry.setStatus(_A)
class _ArrisRouterFWLogExtIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_ArrisRouterFWLogExtIndex_Type.__name__=_D
_ArrisRouterFWLogExtIndex_Object=MibTableColumn
arrisRouterFWLogExtIndex=_ArrisRouterFWLogExtIndex_Object((1,3,6,1,4,1,4115,1,20,1,1,5,19,1,7,1,1),_ArrisRouterFWLogExtIndex_Type())
arrisRouterFWLogExtIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:arrisRouterFWLogExtIndex.setStatus(_A)
_ArrisRouterFWLogLatestEventTime_Type=DateAndTime
_ArrisRouterFWLogLatestEventTime_Object=MibTableColumn
arrisRouterFWLogLatestEventTime=_ArrisRouterFWLogLatestEventTime_Object((1,3,6,1,4,1,4115,1,20,1,1,5,19,1,7,1,2),_ArrisRouterFWLogLatestEventTime_Type())
arrisRouterFWLogLatestEventTime.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterFWLogLatestEventTime.setStatus(_A)
_ArrisRouterFWLogLatestEventInfo_Type=DisplayString
_ArrisRouterFWLogLatestEventInfo_Object=MibTableColumn
arrisRouterFWLogLatestEventInfo=_ArrisRouterFWLogLatestEventInfo_Object((1,3,6,1,4,1,4115,1,20,1,1,5,19,1,7,1,3),_ArrisRouterFWLogLatestEventInfo_Type())
arrisRouterFWLogLatestEventInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterFWLogLatestEventInfo.setStatus(_A)
_ArrisRouterFWLogEventCount_Type=Integer32
_ArrisRouterFWLogEventCount_Object=MibTableColumn
arrisRouterFWLogEventCount=_ArrisRouterFWLogEventCount_Object((1,3,6,1,4,1,4115,1,20,1,1,5,19,1,7,1,4),_ArrisRouterFWLogEventCount_Type())
arrisRouterFWLogEventCount.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterFWLogEventCount.setStatus(_A)
_ArrisRouterMSOLogs_ObjectIdentity=ObjectIdentity
arrisRouterMSOLogs=_ArrisRouterMSOLogs_ObjectIdentity((1,3,6,1,4,1,4115,1,20,1,1,5,19,2))
_ArrisRouterMSOChgLogTable_Object=MibTable
arrisRouterMSOChgLogTable=_ArrisRouterMSOChgLogTable_Object((1,3,6,1,4,1,4115,1,20,1,1,5,19,2,1))
if mibBuilder.loadTexts:arrisRouterMSOChgLogTable.setStatus(_A)
_ArrisRouterMSOChgLogEntry_Object=MibTableRow
arrisRouterMSOChgLogEntry=_ArrisRouterMSOChgLogEntry_Object((1,3,6,1,4,1,4115,1,20,1,1,5,19,2,1,1))
arrisRouterMSOChgLogEntry.setIndexNames((0,_I,_B6))
if mibBuilder.loadTexts:arrisRouterMSOChgLogEntry.setStatus(_A)
class _ArrisRouterMSOChgLogIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,40))
_ArrisRouterMSOChgLogIndex_Type.__name__=_D
_ArrisRouterMSOChgLogIndex_Object=MibTableColumn
arrisRouterMSOChgLogIndex=_ArrisRouterMSOChgLogIndex_Object((1,3,6,1,4,1,4115,1,20,1,1,5,19,2,1,1,1),_ArrisRouterMSOChgLogIndex_Type())
arrisRouterMSOChgLogIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:arrisRouterMSOChgLogIndex.setStatus(_A)
_ArrisRouterMSOChgLogTime_Type=DateAndTime
_ArrisRouterMSOChgLogTime_Object=MibTableColumn
arrisRouterMSOChgLogTime=_ArrisRouterMSOChgLogTime_Object((1,3,6,1,4,1,4115,1,20,1,1,5,19,2,1,1,2),_ArrisRouterMSOChgLogTime_Type())
arrisRouterMSOChgLogTime.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterMSOChgLogTime.setStatus(_A)
_ArrisRouterMSOChgLogInfo_Type=DisplayString
_ArrisRouterMSOChgLogInfo_Object=MibTableColumn
arrisRouterMSOChgLogInfo=_ArrisRouterMSOChgLogInfo_Object((1,3,6,1,4,1,4115,1,20,1,1,5,19,2,1,1,3),_ArrisRouterMSOChgLogInfo_Type())
arrisRouterMSOChgLogInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterMSOChgLogInfo.setStatus(_A)
class _ArrisRouterClearMSOLogs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('noOp',0),('clearLogs',1)))
_ArrisRouterClearMSOLogs_Type.__name__=_D
_ArrisRouterClearMSOLogs_Object=MibScalar
arrisRouterClearMSOLogs=_ArrisRouterClearMSOLogs_Object((1,3,6,1,4,1,4115,1,20,1,1,5,19,2,2),_ArrisRouterClearMSOLogs_Type())
arrisRouterClearMSOLogs.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterClearMSOLogs.setStatus(_A)
class _ArrisRouterClearLogs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('noOp',0),('clearUserLogs',1),('clearMSOLogs',2),('clearAllLogs',3)))
_ArrisRouterClearLogs_Type.__name__=_D
_ArrisRouterClearLogs_Object=MibScalar
arrisRouterClearLogs=_ArrisRouterClearLogs_Object((1,3,6,1,4,1,4115,1,20,1,1,5,19,3),_ArrisRouterClearLogs_Type())
arrisRouterClearLogs.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterClearLogs.setStatus(_A)
class _ArrisRouterTACACSAddr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ArrisRouterTACACSAddr_Type.__name__=_G
_ArrisRouterTACACSAddr_Object=MibScalar
arrisRouterTACACSAddr=_ArrisRouterTACACSAddr_Object((1,3,6,1,4,1,4115,1,20,1,1,5,20),_ArrisRouterTACACSAddr_Type())
arrisRouterTACACSAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterTACACSAddr.setStatus(_A)
class _ArrisRouterTACACSPort_Type(Integer32):defaultValue=49
_ArrisRouterTACACSPort_Type.__name__=_D
_ArrisRouterTACACSPort_Object=MibScalar
arrisRouterTACACSPort=_ArrisRouterTACACSPort_Object((1,3,6,1,4,1,4115,1,20,1,1,5,21),_ArrisRouterTACACSPort_Type())
arrisRouterTACACSPort.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterTACACSPort.setStatus(_A)
class _ArrisRouterTACACSSecretKey_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ArrisRouterTACACSSecretKey_Type.__name__=_G
_ArrisRouterTACACSSecretKey_Object=MibScalar
arrisRouterTACACSSecretKey=_ArrisRouterTACACSSecretKey_Object((1,3,6,1,4,1,4115,1,20,1,1,5,22),_ArrisRouterTACACSSecretKey_Type())
arrisRouterTACACSSecretKey.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterTACACSSecretKey.setStatus(_A)
class _ArrisRouterXmlProvisioningFile_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ArrisRouterXmlProvisioningFile_Type.__name__=_G
_ArrisRouterXmlProvisioningFile_Object=MibScalar
arrisRouterXmlProvisioningFile=_ArrisRouterXmlProvisioningFile_Object((1,3,6,1,4,1,4115,1,20,1,1,5,23),_ArrisRouterXmlProvisioningFile_Type())
arrisRouterXmlProvisioningFile.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterXmlProvisioningFile.setStatus(_A)
class _ArrisRouterXmlProvisioningStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('notSpecified',1),('inProgress',2),('downloadSuccess',3),('serverError',4),('fileNotFound',5),('fileFormatError',6),('downloadFromMgt',7)))
_ArrisRouterXmlProvisioningStatus_Type.__name__=_D
_ArrisRouterXmlProvisioningStatus_Object=MibScalar
arrisRouterXmlProvisioningStatus=_ArrisRouterXmlProvisioningStatus_Object((1,3,6,1,4,1,4115,1,20,1,1,5,24),_ArrisRouterXmlProvisioningStatus_Type())
arrisRouterXmlProvisioningStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterXmlProvisioningStatus.setStatus(_A)
class _ArrisRouterInboundTrafficLogEnable_Type(TruthValue):defaultValue=2
_ArrisRouterInboundTrafficLogEnable_Type.__name__=_F
_ArrisRouterInboundTrafficLogEnable_Object=MibScalar
arrisRouterInboundTrafficLogEnable=_ArrisRouterInboundTrafficLogEnable_Object((1,3,6,1,4,1,4115,1,20,1,1,5,34),_ArrisRouterInboundTrafficLogEnable_Type())
arrisRouterInboundTrafficLogEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterInboundTrafficLogEnable.setStatus(_A)
_ArrisRouterInboundTrafficLogTable_Object=MibTable
arrisRouterInboundTrafficLogTable=_ArrisRouterInboundTrafficLogTable_Object((1,3,6,1,4,1,4115,1,20,1,1,5,42))
if mibBuilder.loadTexts:arrisRouterInboundTrafficLogTable.setStatus(_A)
_ArrisRouterInboundTrafficLogEntry_Object=MibTableRow
arrisRouterInboundTrafficLogEntry=_ArrisRouterInboundTrafficLogEntry_Object((1,3,6,1,4,1,4115,1,20,1,1,5,42,1))
arrisRouterInboundTrafficLogEntry.setIndexNames((0,_I,_B7))
if mibBuilder.loadTexts:arrisRouterInboundTrafficLogEntry.setStatus(_A)
_ArrisRouterInboundTrafficLogIndex_Type=Unsigned32
_ArrisRouterInboundTrafficLogIndex_Object=MibTableColumn
arrisRouterInboundTrafficLogIndex=_ArrisRouterInboundTrafficLogIndex_Object((1,3,6,1,4,1,4115,1,20,1,1,5,42,1,1),_ArrisRouterInboundTrafficLogIndex_Type())
arrisRouterInboundTrafficLogIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:arrisRouterInboundTrafficLogIndex.setStatus(_A)
_ArrisRouterInboundTrafficLogData_Type=OctetString
_ArrisRouterInboundTrafficLogData_Object=MibTableColumn
arrisRouterInboundTrafficLogData=_ArrisRouterInboundTrafficLogData_Object((1,3,6,1,4,1,4115,1,20,1,1,5,42,1,2),_ArrisRouterInboundTrafficLogData_Type())
arrisRouterInboundTrafficLogData.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterInboundTrafficLogData.setStatus(_A)
class _ArrisRouterWirelessBand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,0,1,2)));namedValues=NamedValues(*((_N,-1),('band24GHz',0),('band5GHz',1),('band24GHzand5GHz',2)))
_ArrisRouterWirelessBand_Type.__name__=_D
_ArrisRouterWirelessBand_Object=MibScalar
arrisRouterWirelessBand=_ArrisRouterWirelessBand_Object((1,3,6,1,4,1,4115,1,20,1,1,5,55),_ArrisRouterWirelessBand_Type())
arrisRouterWirelessBand.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterWirelessBand.setStatus(_A)
class _ArrisRouterSaveCurrentConfigFile_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('save',1))
_ArrisRouterSaveCurrentConfigFile_Type.__name__=_D
_ArrisRouterSaveCurrentConfigFile_Object=MibScalar
arrisRouterSaveCurrentConfigFile=_ArrisRouterSaveCurrentConfigFile_Object((1,3,6,1,4,1,4115,1,20,1,1,5,57),_ArrisRouterSaveCurrentConfigFile_Type())
arrisRouterSaveCurrentConfigFile.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterSaveCurrentConfigFile.setStatus(_A)
class _ArrisRouterRestoreCurrentConfigFile_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('restore',1))
_ArrisRouterRestoreCurrentConfigFile_Type.__name__=_D
_ArrisRouterRestoreCurrentConfigFile_Object=MibScalar
arrisRouterRestoreCurrentConfigFile=_ArrisRouterRestoreCurrentConfigFile_Object((1,3,6,1,4,1,4115,1,20,1,1,5,58),_ArrisRouterRestoreCurrentConfigFile_Type())
arrisRouterRestoreCurrentConfigFile.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterRestoreCurrentConfigFile.setStatus(_A)
class _ArrisRouterLocalPosixTimeZone_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ArrisRouterLocalPosixTimeZone_Type.__name__=_G
_ArrisRouterLocalPosixTimeZone_Object=MibScalar
arrisRouterLocalPosixTimeZone=_ArrisRouterLocalPosixTimeZone_Object((1,3,6,1,4,1,4115,1,20,1,1,5,59),_ArrisRouterLocalPosixTimeZone_Type())
arrisRouterLocalPosixTimeZone.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterLocalPosixTimeZone.setStatus(_A)
_ArrisRouterFirstInstallWizardCompletionStatus_Type=TruthValue
_ArrisRouterFirstInstallWizardCompletionStatus_Object=MibScalar
arrisRouterFirstInstallWizardCompletionStatus=_ArrisRouterFirstInstallWizardCompletionStatus_Object((1,3,6,1,4,1,4115,1,20,1,1,5,62),_ArrisRouterFirstInstallWizardCompletionStatus_Type())
arrisRouterFirstInstallWizardCompletionStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterFirstInstallWizardCompletionStatus.setStatus(_A)
_ArrisRouterTroubleshooterEnable_Type=TruthValue
_ArrisRouterTroubleshooterEnable_Object=MibScalar
arrisRouterTroubleshooterEnable=_ArrisRouterTroubleshooterEnable_Object((1,3,6,1,4,1,4115,1,20,1,1,5,63),_ArrisRouterTroubleshooterEnable_Type())
arrisRouterTroubleshooterEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterTroubleshooterEnable.setStatus(_A)
_ArrisRouterCSRActiveTimeout_Type=Unsigned32
_ArrisRouterCSRActiveTimeout_Object=MibScalar
arrisRouterCSRActiveTimeout=_ArrisRouterCSRActiveTimeout_Object((1,3,6,1,4,1,4115,1,20,1,1,5,65),_ArrisRouterCSRActiveTimeout_Type())
arrisRouterCSRActiveTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterCSRActiveTimeout.setStatus(_A)
if mibBuilder.loadTexts:arrisRouterCSRActiveTimeout.setUnits(_M)
_ArrisRouterHostAccess_ObjectIdentity=ObjectIdentity
arrisRouterHostAccess=_ArrisRouterHostAccess_ObjectIdentity((1,3,6,1,4,1,4115,1,20,1,1,6))
_ArrisRouterWebAccessTable_Object=MibTable
arrisRouterWebAccessTable=_ArrisRouterWebAccessTable_Object((1,3,6,1,4,1,4115,1,20,1,1,6,7))
if mibBuilder.loadTexts:arrisRouterWebAccessTable.setStatus(_A)
_ArrisRouterWebAccessEntry_Object=MibTableRow
arrisRouterWebAccessEntry=_ArrisRouterWebAccessEntry_Object((1,3,6,1,4,1,4115,1,20,1,1,6,7,1))
arrisRouterWebAccessEntry.setIndexNames((0,_I,_B8))
if mibBuilder.loadTexts:arrisRouterWebAccessEntry.setStatus(_A)
class _ArrisRouterWebAccessIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_ArrisRouterWebAccessIndex_Type.__name__=_D
_ArrisRouterWebAccessIndex_Object=MibTableColumn
arrisRouterWebAccessIndex=_ArrisRouterWebAccessIndex_Object((1,3,6,1,4,1,4115,1,20,1,1,6,7,1,1),_ArrisRouterWebAccessIndex_Type())
arrisRouterWebAccessIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:arrisRouterWebAccessIndex.setStatus(_A)
_ArrisRouterWebAccessPage_Type=DisplayString
_ArrisRouterWebAccessPage_Object=MibTableColumn
arrisRouterWebAccessPage=_ArrisRouterWebAccessPage_Object((1,3,6,1,4,1,4115,1,20,1,1,6,7,1,2),_ArrisRouterWebAccessPage_Type())
arrisRouterWebAccessPage.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterWebAccessPage.setStatus(_A)
class _ArrisRouterWebAccessLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('noAccessAll',0),('accessTech',1),('accessUser',2),('accessAll',3)))
_ArrisRouterWebAccessLevel_Type.__name__=_D
_ArrisRouterWebAccessLevel_Object=MibTableColumn
arrisRouterWebAccessLevel=_ArrisRouterWebAccessLevel_Object((1,3,6,1,4,1,4115,1,20,1,1,6,7,1,3),_ArrisRouterWebAccessLevel_Type())
arrisRouterWebAccessLevel.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterWebAccessLevel.setStatus(_A)
_ArrisRouterWebAccessRowStatus_Type=RowStatus
_ArrisRouterWebAccessRowStatus_Object=MibTableColumn
arrisRouterWebAccessRowStatus=_ArrisRouterWebAccessRowStatus_Object((1,3,6,1,4,1,4115,1,20,1,1,6,7,1,4),_ArrisRouterWebAccessRowStatus_Type())
arrisRouterWebAccessRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterWebAccessRowStatus.setStatus(_A)
_ArrisRouterWebAccessWANACL_Type=DisplayString
_ArrisRouterWebAccessWANACL_Object=MibScalar
arrisRouterWebAccessWANACL=_ArrisRouterWebAccessWANACL_Object((1,3,6,1,4,1,4115,1,20,1,1,6,8),_ArrisRouterWebAccessWANACL_Type())
arrisRouterWebAccessWANACL.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterWebAccessWANACL.setStatus(_A)
_ArrisRouterPingMgmt_ObjectIdentity=ObjectIdentity
arrisRouterPingMgmt=_ArrisRouterPingMgmt_ObjectIdentity((1,3,6,1,4,1,4115,1,20,1,1,7))
class _ArrisRouterPingTargetAddrType_Type(InetAddressType):defaultValue=1
_ArrisRouterPingTargetAddrType_Type.__name__=_S
_ArrisRouterPingTargetAddrType_Object=MibScalar
arrisRouterPingTargetAddrType=_ArrisRouterPingTargetAddrType_Object((1,3,6,1,4,1,4115,1,20,1,1,7,1),_ArrisRouterPingTargetAddrType_Type())
arrisRouterPingTargetAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterPingTargetAddrType.setStatus(_A)
_ArrisRouterPingTargetAddress_Type=InetAddress
_ArrisRouterPingTargetAddress_Object=MibScalar
arrisRouterPingTargetAddress=_ArrisRouterPingTargetAddress_Object((1,3,6,1,4,1,4115,1,20,1,1,7,2),_ArrisRouterPingTargetAddress_Type())
arrisRouterPingTargetAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterPingTargetAddress.setStatus(_A)
class _ArrisRouterPingNumPkts_Type(Unsigned32):defaultValue=3
_ArrisRouterPingNumPkts_Type.__name__=_H
_ArrisRouterPingNumPkts_Object=MibScalar
arrisRouterPingNumPkts=_ArrisRouterPingNumPkts_Object((1,3,6,1,4,1,4115,1,20,1,1,7,3),_ArrisRouterPingNumPkts_Type())
arrisRouterPingNumPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterPingNumPkts.setStatus(_A)
class _ArrisRouterPingPktSize_Type(Unsigned32):defaultValue=64;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,1518))
_ArrisRouterPingPktSize_Type.__name__=_H
_ArrisRouterPingPktSize_Object=MibScalar
arrisRouterPingPktSize=_ArrisRouterPingPktSize_Object((1,3,6,1,4,1,4115,1,20,1,1,7,4),_ArrisRouterPingPktSize_Type())
arrisRouterPingPktSize.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterPingPktSize.setStatus(_A)
if mibBuilder.loadTexts:arrisRouterPingPktSize.setUnits(_T)
class _ArrisRouterPingInterval_Type(Unsigned32):defaultValue=0
_ArrisRouterPingInterval_Type.__name__=_H
_ArrisRouterPingInterval_Object=MibScalar
arrisRouterPingInterval=_ArrisRouterPingInterval_Object((1,3,6,1,4,1,4115,1,20,1,1,7,5),_ArrisRouterPingInterval_Type())
arrisRouterPingInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterPingInterval.setStatus(_A)
if mibBuilder.loadTexts:arrisRouterPingInterval.setUnits(_P)
class _ArrisRouterPingTimeout_Type(Integer32):defaultValue=5000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,65535))
_ArrisRouterPingTimeout_Type.__name__=_D
_ArrisRouterPingTimeout_Object=MibScalar
arrisRouterPingTimeout=_ArrisRouterPingTimeout_Object((1,3,6,1,4,1,4115,1,20,1,1,7,6),_ArrisRouterPingTimeout_Type())
arrisRouterPingTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterPingTimeout.setStatus(_A)
if mibBuilder.loadTexts:arrisRouterPingTimeout.setUnits(_P)
class _ArrisRouterPingVerifyReply_Type(TruthValue):defaultValue=1
_ArrisRouterPingVerifyReply_Type.__name__=_F
_ArrisRouterPingVerifyReply_Object=MibScalar
arrisRouterPingVerifyReply=_ArrisRouterPingVerifyReply_Object((1,3,6,1,4,1,4115,1,20,1,1,7,7),_ArrisRouterPingVerifyReply_Type())
arrisRouterPingVerifyReply.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterPingVerifyReply.setStatus(_A)
class _ArrisRouterPingIpStackNumber_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_ArrisRouterPingIpStackNumber_Type.__name__=_D
_ArrisRouterPingIpStackNumber_Object=MibScalar
arrisRouterPingIpStackNumber=_ArrisRouterPingIpStackNumber_Object((1,3,6,1,4,1,4115,1,20,1,1,7,8),_ArrisRouterPingIpStackNumber_Type())
arrisRouterPingIpStackNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterPingIpStackNumber.setStatus(_A)
class _ArrisRouterPingStartStop_Type(TruthValue):defaultValue=1
_ArrisRouterPingStartStop_Type.__name__=_F
_ArrisRouterPingStartStop_Object=MibScalar
arrisRouterPingStartStop=_ArrisRouterPingStartStop_Object((1,3,6,1,4,1,4115,1,20,1,1,7,9),_ArrisRouterPingStartStop_Type())
arrisRouterPingStartStop.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterPingStartStop.setStatus(_A)
_ArrisRouterPingPktsSent_Type=Counter32
_ArrisRouterPingPktsSent_Object=MibScalar
arrisRouterPingPktsSent=_ArrisRouterPingPktsSent_Object((1,3,6,1,4,1,4115,1,20,1,1,7,10),_ArrisRouterPingPktsSent_Type())
arrisRouterPingPktsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterPingPktsSent.setStatus(_A)
_ArrisRouterPingRepliesReceived_Type=Counter32
_ArrisRouterPingRepliesReceived_Object=MibScalar
arrisRouterPingRepliesReceived=_ArrisRouterPingRepliesReceived_Object((1,3,6,1,4,1,4115,1,20,1,1,7,11),_ArrisRouterPingRepliesReceived_Type())
arrisRouterPingRepliesReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterPingRepliesReceived.setStatus(_A)
_ArrisRouterPingRepliesVerified_Type=Counter32
_ArrisRouterPingRepliesVerified_Object=MibScalar
arrisRouterPingRepliesVerified=_ArrisRouterPingRepliesVerified_Object((1,3,6,1,4,1,4115,1,20,1,1,7,12),_ArrisRouterPingRepliesVerified_Type())
arrisRouterPingRepliesVerified.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterPingRepliesVerified.setStatus(_A)
_ArrisRouterPingOctetsSent_Type=Counter32
_ArrisRouterPingOctetsSent_Object=MibScalar
arrisRouterPingOctetsSent=_ArrisRouterPingOctetsSent_Object((1,3,6,1,4,1,4115,1,20,1,1,7,13),_ArrisRouterPingOctetsSent_Type())
arrisRouterPingOctetsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterPingOctetsSent.setStatus(_A)
_ArrisRouterPingOctetsReceived_Type=Counter32
_ArrisRouterPingOctetsReceived_Object=MibScalar
arrisRouterPingOctetsReceived=_ArrisRouterPingOctetsReceived_Object((1,3,6,1,4,1,4115,1,20,1,1,7,14),_ArrisRouterPingOctetsReceived_Type())
arrisRouterPingOctetsReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterPingOctetsReceived.setStatus(_A)
_ArrisRouterPingIcmpErrors_Type=Counter32
_ArrisRouterPingIcmpErrors_Object=MibScalar
arrisRouterPingIcmpErrors=_ArrisRouterPingIcmpErrors_Object((1,3,6,1,4,1,4115,1,20,1,1,7,15),_ArrisRouterPingIcmpErrors_Type())
arrisRouterPingIcmpErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterPingIcmpErrors.setStatus(_A)
_ArrisRouterPingLastIcmpError_Type=Unsigned32
_ArrisRouterPingLastIcmpError_Object=MibScalar
arrisRouterPingLastIcmpError=_ArrisRouterPingLastIcmpError_Object((1,3,6,1,4,1,4115,1,20,1,1,7,16),_ArrisRouterPingLastIcmpError_Type())
arrisRouterPingLastIcmpError.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterPingLastIcmpError.setStatus(_A)
_ArrisRouterPingAverageRtt_Type=Unsigned32
_ArrisRouterPingAverageRtt_Object=MibScalar
arrisRouterPingAverageRtt=_ArrisRouterPingAverageRtt_Object((1,3,6,1,4,1,4115,1,20,1,1,7,17),_ArrisRouterPingAverageRtt_Type())
arrisRouterPingAverageRtt.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterPingAverageRtt.setStatus(_A)
if mibBuilder.loadTexts:arrisRouterPingAverageRtt.setUnits(_P)
_ArrisRouterPingMinRtt_Type=Unsigned32
_ArrisRouterPingMinRtt_Object=MibScalar
arrisRouterPingMinRtt=_ArrisRouterPingMinRtt_Object((1,3,6,1,4,1,4115,1,20,1,1,7,18),_ArrisRouterPingMinRtt_Type())
arrisRouterPingMinRtt.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterPingMinRtt.setStatus(_A)
if mibBuilder.loadTexts:arrisRouterPingMinRtt.setUnits(_P)
_ArrisRouterPingMaxRtt_Type=Unsigned32
_ArrisRouterPingMaxRtt_Object=MibScalar
arrisRouterPingMaxRtt=_ArrisRouterPingMaxRtt_Object((1,3,6,1,4,1,4115,1,20,1,1,7,19),_ArrisRouterPingMaxRtt_Type())
arrisRouterPingMaxRtt.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterPingMaxRtt.setStatus(_A)
if mibBuilder.loadTexts:arrisRouterPingMaxRtt.setUnits(_P)
class _ArrisRouterPingTargetDNSQueryIPAddrType_Type(InetAddressType):defaultValue=1
_ArrisRouterPingTargetDNSQueryIPAddrType_Type.__name__=_S
_ArrisRouterPingTargetDNSQueryIPAddrType_Object=MibScalar
arrisRouterPingTargetDNSQueryIPAddrType=_ArrisRouterPingTargetDNSQueryIPAddrType_Object((1,3,6,1,4,1,4115,1,20,1,1,7,20),_ArrisRouterPingTargetDNSQueryIPAddrType_Type())
arrisRouterPingTargetDNSQueryIPAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterPingTargetDNSQueryIPAddrType.setStatus(_A)
class _ArrisRouterPingLog_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_ArrisRouterPingLog_Type.__name__=_G
_ArrisRouterPingLog_Object=MibScalar
arrisRouterPingLog=_ArrisRouterPingLog_Object((1,3,6,1,4,1,4115,1,20,1,1,7,21),_ArrisRouterPingLog_Type())
arrisRouterPingLog.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterPingLog.setStatus(_A)
_ArrisRouterTraceRtMgmt_ObjectIdentity=ObjectIdentity
arrisRouterTraceRtMgmt=_ArrisRouterTraceRtMgmt_ObjectIdentity((1,3,6,1,4,1,4115,1,20,1,1,8))
class _ArrisRouterTraceRtTargAddrType_Type(InetAddressType):defaultValue=1
_ArrisRouterTraceRtTargAddrType_Type.__name__=_S
_ArrisRouterTraceRtTargAddrType_Object=MibScalar
arrisRouterTraceRtTargAddrType=_ArrisRouterTraceRtTargAddrType_Object((1,3,6,1,4,1,4115,1,20,1,1,8,1),_ArrisRouterTraceRtTargAddrType_Type())
arrisRouterTraceRtTargAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterTraceRtTargAddrType.setStatus(_A)
_ArrisRouterTraceRtTargetAddr_Type=InetAddress
_ArrisRouterTraceRtTargetAddr_Object=MibScalar
arrisRouterTraceRtTargetAddr=_ArrisRouterTraceRtTargetAddr_Object((1,3,6,1,4,1,4115,1,20,1,1,8,2),_ArrisRouterTraceRtTargetAddr_Type())
arrisRouterTraceRtTargetAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterTraceRtTargetAddr.setStatus(_A)
class _ArrisRouterTraceRtMaxHops_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ArrisRouterTraceRtMaxHops_Type.__name__=_D
_ArrisRouterTraceRtMaxHops_Object=MibScalar
arrisRouterTraceRtMaxHops=_ArrisRouterTraceRtMaxHops_Object((1,3,6,1,4,1,4115,1,20,1,1,8,3),_ArrisRouterTraceRtMaxHops_Type())
arrisRouterTraceRtMaxHops.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterTraceRtMaxHops.setStatus(_A)
class _ArrisRouterTraceRtDataSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ArrisRouterTraceRtDataSize_Type.__name__=_D
_ArrisRouterTraceRtDataSize_Object=MibScalar
arrisRouterTraceRtDataSize=_ArrisRouterTraceRtDataSize_Object((1,3,6,1,4,1,4115,1,20,1,1,8,4),_ArrisRouterTraceRtDataSize_Type())
arrisRouterTraceRtDataSize.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterTraceRtDataSize.setStatus(_A)
class _ArrisRouterTraceRtResolveHosts_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('noResolve',0),('resolve',1)))
_ArrisRouterTraceRtResolveHosts_Type.__name__=_D
_ArrisRouterTraceRtResolveHosts_Object=MibScalar
arrisRouterTraceRtResolveHosts=_ArrisRouterTraceRtResolveHosts_Object((1,3,6,1,4,1,4115,1,20,1,1,8,5),_ArrisRouterTraceRtResolveHosts_Type())
arrisRouterTraceRtResolveHosts.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterTraceRtResolveHosts.setStatus(_A)
class _ArrisRouterTraceRtBasePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ArrisRouterTraceRtBasePort_Type.__name__=_D
_ArrisRouterTraceRtBasePort_Object=MibScalar
arrisRouterTraceRtBasePort=_ArrisRouterTraceRtBasePort_Object((1,3,6,1,4,1,4115,1,20,1,1,8,6),_ArrisRouterTraceRtBasePort_Type())
arrisRouterTraceRtBasePort.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterTraceRtBasePort.setStatus(_A)
class _ArrisRouterTraceRtStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,10,11)));namedValues=NamedValues(*(('traceRouteNotRunning',0),('traceRouteRunning',1),('startTrace',10),('stopTrace',11)))
_ArrisRouterTraceRtStart_Type.__name__=_D
_ArrisRouterTraceRtStart_Object=MibScalar
arrisRouterTraceRtStart=_ArrisRouterTraceRtStart_Object((1,3,6,1,4,1,4115,1,20,1,1,8,7),_ArrisRouterTraceRtStart_Type())
arrisRouterTraceRtStart.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterTraceRtStart.setStatus(_A)
class _ArrisRouterTraceRtLog_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_ArrisRouterTraceRtLog_Type.__name__=_G
_ArrisRouterTraceRtLog_Object=MibScalar
arrisRouterTraceRtLog=_ArrisRouterTraceRtLog_Object((1,3,6,1,4,1,4115,1,20,1,1,8,8),_ArrisRouterTraceRtLog_Type())
arrisRouterTraceRtLog.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterTraceRtLog.setStatus(_A)
class _ArrisRouterTraceRtTimeout_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_ArrisRouterTraceRtTimeout_Type.__name__=_H
_ArrisRouterTraceRtTimeout_Object=MibScalar
arrisRouterTraceRtTimeout=_ArrisRouterTraceRtTimeout_Object((1,3,6,1,4,1,4115,1,20,1,1,8,9),_ArrisRouterTraceRtTimeout_Type())
arrisRouterTraceRtTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterTraceRtTimeout.setStatus(_A)
if mibBuilder.loadTexts:arrisRouterTraceRtTimeout.setUnits(_M)
class _ArrisRouterTraceRtDiffServ_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ArrisRouterTraceRtDiffServ_Type.__name__=_H
_ArrisRouterTraceRtDiffServ_Object=MibScalar
arrisRouterTraceRtDiffServ=_ArrisRouterTraceRtDiffServ_Object((1,3,6,1,4,1,4115,1,20,1,1,8,10),_ArrisRouterTraceRtDiffServ_Type())
arrisRouterTraceRtDiffServ.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterTraceRtDiffServ.setStatus(_A)
class _ArrisRouterApplyAllSettings_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_N,0),(_B0,1)))
_ArrisRouterApplyAllSettings_Type.__name__=_D
_ArrisRouterApplyAllSettings_Object=MibScalar
arrisRouterApplyAllSettings=_ArrisRouterApplyAllSettings_Object((1,3,6,1,4,1,4115,1,20,1,1,9),_ArrisRouterApplyAllSettings_Type())
arrisRouterApplyAllSettings.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterApplyAllSettings.setStatus(_A)
_ArrisRouterICtrl_ObjectIdentity=ObjectIdentity
arrisRouterICtrl=_ArrisRouterICtrl_ObjectIdentity((1,3,6,1,4,1,4115,1,20,1,1,10))
_ArrisRouterICtrlPortMapCount_Type=Integer32
_ArrisRouterICtrlPortMapCount_Object=MibScalar
arrisRouterICtrlPortMapCount=_ArrisRouterICtrlPortMapCount_Object((1,3,6,1,4,1,4115,1,20,1,1,10,1),_ArrisRouterICtrlPortMapCount_Type())
arrisRouterICtrlPortMapCount.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterICtrlPortMapCount.setStatus(_A)
_ArrisRouterICtrlPortMapTable_Object=MibTable
arrisRouterICtrlPortMapTable=_ArrisRouterICtrlPortMapTable_Object((1,3,6,1,4,1,4115,1,20,1,1,10,2))
if mibBuilder.loadTexts:arrisRouterICtrlPortMapTable.setStatus(_A)
_ArrisRouterICtrlPortMapEntry_Object=MibTableRow
arrisRouterICtrlPortMapEntry=_ArrisRouterICtrlPortMapEntry_Object((1,3,6,1,4,1,4115,1,20,1,1,10,2,1))
arrisRouterICtrlPortMapEntry.setIndexNames((0,_I,_B9))
if mibBuilder.loadTexts:arrisRouterICtrlPortMapEntry.setStatus(_A)
class _ArrisRouterICtrlPortMapIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_ArrisRouterICtrlPortMapIndex_Type.__name__=_D
_ArrisRouterICtrlPortMapIndex_Object=MibTableColumn
arrisRouterICtrlPortMapIndex=_ArrisRouterICtrlPortMapIndex_Object((1,3,6,1,4,1,4115,1,20,1,1,10,2,1,1),_ArrisRouterICtrlPortMapIndex_Type())
arrisRouterICtrlPortMapIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:arrisRouterICtrlPortMapIndex.setStatus(_A)
_ArrisRouterPortMapDescription_Type=DisplayString
_ArrisRouterPortMapDescription_Object=MibTableColumn
arrisRouterPortMapDescription=_ArrisRouterPortMapDescription_Object((1,3,6,1,4,1,4115,1,20,1,1,10,2,1,2),_ArrisRouterPortMapDescription_Type())
arrisRouterPortMapDescription.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterPortMapDescription.setStatus(_A)
_ArrisRouterPortMapInternalClientAddrType_Type=InetAddressType
_ArrisRouterPortMapInternalClientAddrType_Object=MibTableColumn
arrisRouterPortMapInternalClientAddrType=_ArrisRouterPortMapInternalClientAddrType_Object((1,3,6,1,4,1,4115,1,20,1,1,10,2,1,3),_ArrisRouterPortMapInternalClientAddrType_Type())
arrisRouterPortMapInternalClientAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterPortMapInternalClientAddrType.setStatus(_A)
_ArrisRouterPortMapInternalClientAddr_Type=InetAddress
_ArrisRouterPortMapInternalClientAddr_Object=MibTableColumn
arrisRouterPortMapInternalClientAddr=_ArrisRouterPortMapInternalClientAddr_Object((1,3,6,1,4,1,4115,1,20,1,1,10,2,1,4),_ArrisRouterPortMapInternalClientAddr_Type())
arrisRouterPortMapInternalClientAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterPortMapInternalClientAddr.setStatus(_A)
class _ArrisRouterPortMapProtocol_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_c,1),(_b,2)))
_ArrisRouterPortMapProtocol_Type.__name__=_D
_ArrisRouterPortMapProtocol_Object=MibTableColumn
arrisRouterPortMapProtocol=_ArrisRouterPortMapProtocol_Object((1,3,6,1,4,1,4115,1,20,1,1,10,2,1,5),_ArrisRouterPortMapProtocol_Type())
arrisRouterPortMapProtocol.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterPortMapProtocol.setStatus(_A)
_ArrisRouterPortMapExternalPort_Type=Unsigned32
_ArrisRouterPortMapExternalPort_Object=MibTableColumn
arrisRouterPortMapExternalPort=_ArrisRouterPortMapExternalPort_Object((1,3,6,1,4,1,4115,1,20,1,1,10,2,1,6),_ArrisRouterPortMapExternalPort_Type())
arrisRouterPortMapExternalPort.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterPortMapExternalPort.setStatus(_A)
_ArrisRouterPortMapInternalPort_Type=Unsigned32
_ArrisRouterPortMapInternalPort_Object=MibTableColumn
arrisRouterPortMapInternalPort=_ArrisRouterPortMapInternalPort_Object((1,3,6,1,4,1,4115,1,20,1,1,10,2,1,7),_ArrisRouterPortMapInternalPort_Type())
arrisRouterPortMapInternalPort.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterPortMapInternalPort.setStatus(_A)
_ArrisRouterPortMapRowStatus_Type=RowStatus
_ArrisRouterPortMapRowStatus_Object=MibTableColumn
arrisRouterPortMapRowStatus=_ArrisRouterPortMapRowStatus_Object((1,3,6,1,4,1,4115,1,20,1,1,10,2,1,8),_ArrisRouterPortMapRowStatus_Type())
arrisRouterPortMapRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterPortMapRowStatus.setStatus(_A)
_ArrisRouterPortMapInternalStartPort_Type=Unsigned32
_ArrisRouterPortMapInternalStartPort_Object=MibTableColumn
arrisRouterPortMapInternalStartPort=_ArrisRouterPortMapInternalStartPort_Object((1,3,6,1,4,1,4115,1,20,1,1,10,2,1,9),_ArrisRouterPortMapInternalStartPort_Type())
arrisRouterPortMapInternalStartPort.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterPortMapInternalStartPort.setStatus(_A)
_ArrisRouterPortMapInternalEndPort_Type=Unsigned32
_ArrisRouterPortMapInternalEndPort_Object=MibTableColumn
arrisRouterPortMapInternalEndPort=_ArrisRouterPortMapInternalEndPort_Object((1,3,6,1,4,1,4115,1,20,1,1,10,2,1,10),_ArrisRouterPortMapInternalEndPort_Type())
arrisRouterPortMapInternalEndPort.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterPortMapInternalEndPort.setStatus(_A)
_ArrisRouterPortMapExternalStartPort_Type=Unsigned32
_ArrisRouterPortMapExternalStartPort_Object=MibTableColumn
arrisRouterPortMapExternalStartPort=_ArrisRouterPortMapExternalStartPort_Object((1,3,6,1,4,1,4115,1,20,1,1,10,2,1,11),_ArrisRouterPortMapExternalStartPort_Type())
arrisRouterPortMapExternalStartPort.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterPortMapExternalStartPort.setStatus(_A)
_ArrisRouterPortMapExternalEndPort_Type=Unsigned32
_ArrisRouterPortMapExternalEndPort_Object=MibTableColumn
arrisRouterPortMapExternalEndPort=_ArrisRouterPortMapExternalEndPort_Object((1,3,6,1,4,1,4115,1,20,1,1,10,2,1,12),_ArrisRouterPortMapExternalEndPort_Type())
arrisRouterPortMapExternalEndPort.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisRouterPortMapExternalEndPort.setStatus(_A)
_ArrisRouterICtrlGetDeviceSettings_ObjectIdentity=ObjectIdentity
arrisRouterICtrlGetDeviceSettings=_ArrisRouterICtrlGetDeviceSettings_ObjectIdentity((1,3,6,1,4,1,4115,1,20,1,1,10,3))
_ArrisRouterICtrlDeviceSettingsFWversion_Type=DisplayString
_ArrisRouterICtrlDeviceSettingsFWversion_Object=MibScalar
arrisRouterICtrlDeviceSettingsFWversion=_ArrisRouterICtrlDeviceSettingsFWversion_Object((1,3,6,1,4,1,4115,1,20,1,1,10,3,1),_ArrisRouterICtrlDeviceSettingsFWversion_Type())
arrisRouterICtrlDeviceSettingsFWversion.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterICtrlDeviceSettingsFWversion.setStatus(_A)
_ArrisRouterICtrlIsDeviceReady_ObjectIdentity=ObjectIdentity
arrisRouterICtrlIsDeviceReady=_ArrisRouterICtrlIsDeviceReady_ObjectIdentity((1,3,6,1,4,1,4115,1,20,1,1,10,4))
class _ArrisRouterICtrlDeviceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('error',0),('ok',1)))
_ArrisRouterICtrlDeviceStatus_Type.__name__=_D
_ArrisRouterICtrlDeviceStatus_Object=MibScalar
arrisRouterICtrlDeviceStatus=_ArrisRouterICtrlDeviceStatus_Object((1,3,6,1,4,1,4115,1,20,1,1,10,4,1),_ArrisRouterICtrlDeviceStatus_Type())
arrisRouterICtrlDeviceStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterICtrlDeviceStatus.setStatus(_A)
_ArrisRouterICtrlReboot_ObjectIdentity=ObjectIdentity
arrisRouterICtrlReboot=_ArrisRouterICtrlReboot_ObjectIdentity((1,3,6,1,4,1,4115,1,20,1,1,10,5))
class _ArrisRouterICtrlInitiateReboot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('reboot',1))
_ArrisRouterICtrlInitiateReboot_Type.__name__=_D
_ArrisRouterICtrlInitiateReboot_Object=MibScalar
arrisRouterICtrlInitiateReboot=_ArrisRouterICtrlInitiateReboot_Object((1,3,6,1,4,1,4115,1,20,1,1,10,5,1),_ArrisRouterICtrlInitiateReboot_Type())
arrisRouterICtrlInitiateReboot.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterICtrlInitiateReboot.setStatus(_A)
_ArrisRouterICtrlSetDeviceSettings_ObjectIdentity=ObjectIdentity
arrisRouterICtrlSetDeviceSettings=_ArrisRouterICtrlSetDeviceSettings_ObjectIdentity((1,3,6,1,4,1,4115,1,20,1,1,10,6))
_ArrisRouterICtrlSetDeviceName_Type=DisplayString
_ArrisRouterICtrlSetDeviceName_Object=MibScalar
arrisRouterICtrlSetDeviceName=_ArrisRouterICtrlSetDeviceName_Object((1,3,6,1,4,1,4115,1,20,1,1,10,6,1),_ArrisRouterICtrlSetDeviceName_Type())
arrisRouterICtrlSetDeviceName.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterICtrlSetDeviceName.setStatus(_A)
_ArrisRouterICtrlSetAdminPassword_Type=DisplayString
_ArrisRouterICtrlSetAdminPassword_Object=MibScalar
arrisRouterICtrlSetAdminPassword=_ArrisRouterICtrlSetAdminPassword_Object((1,3,6,1,4,1,4115,1,20,1,1,10,6,2),_ArrisRouterICtrlSetAdminPassword_Type())
arrisRouterICtrlSetAdminPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterICtrlSetAdminPassword.setStatus(_A)
_ArrisRouterICtrlRouterSettings_ObjectIdentity=ObjectIdentity
arrisRouterICtrlRouterSettings=_ArrisRouterICtrlRouterSettings_ObjectIdentity((1,3,6,1,4,1,4115,1,20,1,1,10,7))
_ArrisRouterICtrlRouterManageRemote_Type=TruthValue
_ArrisRouterICtrlRouterManageRemote_Object=MibScalar
arrisRouterICtrlRouterManageRemote=_ArrisRouterICtrlRouterManageRemote_Object((1,3,6,1,4,1,4115,1,20,1,1,10,7,1),_ArrisRouterICtrlRouterManageRemote_Type())
arrisRouterICtrlRouterManageRemote.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterICtrlRouterManageRemote.setStatus(_A)
_ArrisRouterICtrlRouterRemotePort_Type=Unsigned32
_ArrisRouterICtrlRouterRemotePort_Object=MibScalar
arrisRouterICtrlRouterRemotePort=_ArrisRouterICtrlRouterRemotePort_Object((1,3,6,1,4,1,4115,1,20,1,1,10,7,2),_ArrisRouterICtrlRouterRemotePort_Type())
arrisRouterICtrlRouterRemotePort.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterICtrlRouterRemotePort.setStatus(_A)
_ArrisRouterICtrlRouterRemoteSSL_Type=TruthValue
_ArrisRouterICtrlRouterRemoteSSL_Object=MibScalar
arrisRouterICtrlRouterRemoteSSL=_ArrisRouterICtrlRouterRemoteSSL_Object((1,3,6,1,4,1,4115,1,20,1,1,10,7,3),_ArrisRouterICtrlRouterRemoteSSL_Type())
arrisRouterICtrlRouterRemoteSSL.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterICtrlRouterRemoteSSL.setStatus(_A)
_ArrisRouterICtrlWLanRadioSettings_ObjectIdentity=ObjectIdentity
arrisRouterICtrlWLanRadioSettings=_ArrisRouterICtrlWLanRadioSettings_ObjectIdentity((1,3,6,1,4,1,4115,1,20,1,1,10,8))
_ArrisRouterICtrlWLanRadioMacAddress_Type=MacAddress
_ArrisRouterICtrlWLanRadioMacAddress_Object=MibScalar
arrisRouterICtrlWLanRadioMacAddress=_ArrisRouterICtrlWLanRadioMacAddress_Object((1,3,6,1,4,1,4115,1,20,1,1,10,8,1),_ArrisRouterICtrlWLanRadioMacAddress_Type())
arrisRouterICtrlWLanRadioMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterICtrlWLanRadioMacAddress.setStatus(_A)
_ArrisRouterICtrlWLanRadioChannelWidth_Type=Unsigned32
_ArrisRouterICtrlWLanRadioChannelWidth_Object=MibScalar
arrisRouterICtrlWLanRadioChannelWidth=_ArrisRouterICtrlWLanRadioChannelWidth_Object((1,3,6,1,4,1,4115,1,20,1,1,10,8,2),_ArrisRouterICtrlWLanRadioChannelWidth_Type())
arrisRouterICtrlWLanRadioChannelWidth.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterICtrlWLanRadioChannelWidth.setStatus(_A)
_ArrisRouterICtrlSetBridgeConnect_ObjectIdentity=ObjectIdentity
arrisRouterICtrlSetBridgeConnect=_ArrisRouterICtrlSetBridgeConnect_ObjectIdentity((1,3,6,1,4,1,4115,1,20,1,1,10,9))
_ArrisRouterICtrlSetBridgeEthernetPort_Type=Unsigned32
_ArrisRouterICtrlSetBridgeEthernetPort_Object=MibScalar
arrisRouterICtrlSetBridgeEthernetPort=_ArrisRouterICtrlSetBridgeEthernetPort_Object((1,3,6,1,4,1,4115,1,20,1,1,10,9,1),_ArrisRouterICtrlSetBridgeEthernetPort_Type())
arrisRouterICtrlSetBridgeEthernetPort.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterICtrlSetBridgeEthernetPort.setStatus(_A)
_ArrisRouterICtrlSetBridgeMinutes_Type=Unsigned32
_ArrisRouterICtrlSetBridgeMinutes_Object=MibScalar
arrisRouterICtrlSetBridgeMinutes=_ArrisRouterICtrlSetBridgeMinutes_Object((1,3,6,1,4,1,4115,1,20,1,1,10,9,2),_ArrisRouterICtrlSetBridgeMinutes_Type())
arrisRouterICtrlSetBridgeMinutes.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterICtrlSetBridgeMinutes.setStatus(_A)
class _ArrisRouterICtrlSetBridgePermanentPort4Enable_Type(TruthValue):defaultValue=2
_ArrisRouterICtrlSetBridgePermanentPort4Enable_Type.__name__=_F
_ArrisRouterICtrlSetBridgePermanentPort4Enable_Object=MibScalar
arrisRouterICtrlSetBridgePermanentPort4Enable=_ArrisRouterICtrlSetBridgePermanentPort4Enable_Object((1,3,6,1,4,1,4115,1,20,1,1,10,9,3),_ArrisRouterICtrlSetBridgePermanentPort4Enable_Type())
arrisRouterICtrlSetBridgePermanentPort4Enable.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterICtrlSetBridgePermanentPort4Enable.setStatus(_A)
_ArrisRouterICtrlGetWanSettings_ObjectIdentity=ObjectIdentity
arrisRouterICtrlGetWanSettings=_ArrisRouterICtrlGetWanSettings_ObjectIdentity((1,3,6,1,4,1,4115,1,20,1,1,10,10))
class _ArrisRouterICtrlGetWanType_Type(DisplayString):defaultValue=OctetString('DHCP')
_ArrisRouterICtrlGetWanType_Type.__name__=_G
_ArrisRouterICtrlGetWanType_Object=MibScalar
arrisRouterICtrlGetWanType=_ArrisRouterICtrlGetWanType_Object((1,3,6,1,4,1,4115,1,20,1,1,10,10,2),_ArrisRouterICtrlGetWanType_Type())
arrisRouterICtrlGetWanType.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterICtrlGetWanType.setStatus(_A)
_ArrisRouterICtrlGetWanMTU_Type=Unsigned32
_ArrisRouterICtrlGetWanMTU_Object=MibScalar
arrisRouterICtrlGetWanMTU=_ArrisRouterICtrlGetWanMTU_Object((1,3,6,1,4,1,4115,1,20,1,1,10,10,3),_ArrisRouterICtrlGetWanMTU_Type())
arrisRouterICtrlGetWanMTU.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterICtrlGetWanMTU.setStatus(_A)
_ArrisRouterICtrlGetWanPrefixLen_Type=InetAddressPrefixLength
_ArrisRouterICtrlGetWanPrefixLen_Object=MibScalar
arrisRouterICtrlGetWanPrefixLen=_ArrisRouterICtrlGetWanPrefixLen_Object((1,3,6,1,4,1,4115,1,20,1,1,10,10,4),_ArrisRouterICtrlGetWanPrefixLen_Type())
arrisRouterICtrlGetWanPrefixLen.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterICtrlGetWanPrefixLen.setStatus(_A)
_ArrisRouterICtrlGetWanGatewayAddrType_Type=InetAddressType
_ArrisRouterICtrlGetWanGatewayAddrType_Object=MibScalar
arrisRouterICtrlGetWanGatewayAddrType=_ArrisRouterICtrlGetWanGatewayAddrType_Object((1,3,6,1,4,1,4115,1,20,1,1,10,10,5),_ArrisRouterICtrlGetWanGatewayAddrType_Type())
arrisRouterICtrlGetWanGatewayAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterICtrlGetWanGatewayAddrType.setStatus(_A)
_ArrisRouterICtrlGetWanGatewayAddr_Type=InetAddress
_ArrisRouterICtrlGetWanGatewayAddr_Object=MibScalar
arrisRouterICtrlGetWanGatewayAddr=_ArrisRouterICtrlGetWanGatewayAddr_Object((1,3,6,1,4,1,4115,1,20,1,1,10,10,6),_ArrisRouterICtrlGetWanGatewayAddr_Type())
arrisRouterICtrlGetWanGatewayAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterICtrlGetWanGatewayAddr.setStatus(_A)
_ArrisRouterICtrlGetWanDNSPrimaryAddrType_Type=InetAddressType
_ArrisRouterICtrlGetWanDNSPrimaryAddrType_Object=MibScalar
arrisRouterICtrlGetWanDNSPrimaryAddrType=_ArrisRouterICtrlGetWanDNSPrimaryAddrType_Object((1,3,6,1,4,1,4115,1,20,1,1,10,10,7),_ArrisRouterICtrlGetWanDNSPrimaryAddrType_Type())
arrisRouterICtrlGetWanDNSPrimaryAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterICtrlGetWanDNSPrimaryAddrType.setStatus(_A)
_ArrisRouterICtrlGetWanDNSPrimaryAddr_Type=InetAddress
_ArrisRouterICtrlGetWanDNSPrimaryAddr_Object=MibScalar
arrisRouterICtrlGetWanDNSPrimaryAddr=_ArrisRouterICtrlGetWanDNSPrimaryAddr_Object((1,3,6,1,4,1,4115,1,20,1,1,10,10,8),_ArrisRouterICtrlGetWanDNSPrimaryAddr_Type())
arrisRouterICtrlGetWanDNSPrimaryAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterICtrlGetWanDNSPrimaryAddr.setStatus(_A)
_ArrisRouterICtrlGetWanDNSSecondaryAddrType_Type=InetAddressType
_ArrisRouterICtrlGetWanDNSSecondaryAddrType_Object=MibScalar
arrisRouterICtrlGetWanDNSSecondaryAddrType=_ArrisRouterICtrlGetWanDNSSecondaryAddrType_Object((1,3,6,1,4,1,4115,1,20,1,1,10,10,9),_ArrisRouterICtrlGetWanDNSSecondaryAddrType_Type())
arrisRouterICtrlGetWanDNSSecondaryAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterICtrlGetWanDNSSecondaryAddrType.setStatus(_A)
_ArrisRouterICtrlGetWanDNSSecondaryAddr_Type=InetAddress
_ArrisRouterICtrlGetWanDNSSecondaryAddr_Object=MibScalar
arrisRouterICtrlGetWanDNSSecondaryAddr=_ArrisRouterICtrlGetWanDNSSecondaryAddr_Object((1,3,6,1,4,1,4115,1,20,1,1,10,10,10),_ArrisRouterICtrlGetWanDNSSecondaryAddr_Type())
arrisRouterICtrlGetWanDNSSecondaryAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterICtrlGetWanDNSSecondaryAddr.setStatus(_A)
_ArrisRouterICtrlGetWanMacAddress_Type=MacAddress
_ArrisRouterICtrlGetWanMacAddress_Object=MibScalar
arrisRouterICtrlGetWanMacAddress=_ArrisRouterICtrlGetWanMacAddress_Object((1,3,6,1,4,1,4115,1,20,1,1,10,10,11),_ArrisRouterICtrlGetWanMacAddress_Type())
arrisRouterICtrlGetWanMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterICtrlGetWanMacAddress.setStatus(_A)
class _ArrisRouterICtrlHNAPServerPort_Type(Unsigned32):defaultValue=8081
_ArrisRouterICtrlHNAPServerPort_Type.__name__=_H
_ArrisRouterICtrlHNAPServerPort_Object=MibScalar
arrisRouterICtrlHNAPServerPort=_ArrisRouterICtrlHNAPServerPort_Object((1,3,6,1,4,1,4115,1,20,1,1,10,11),_ArrisRouterICtrlHNAPServerPort_Type())
arrisRouterICtrlHNAPServerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterICtrlHNAPServerPort.setStatus(_A)
class _ArrisRouterICtrlEnable_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_O,0),(_Q,1)))
_ArrisRouterICtrlEnable_Type.__name__=_D
_ArrisRouterICtrlEnable_Object=MibScalar
arrisRouterICtrlEnable=_ArrisRouterICtrlEnable_Object((1,3,6,1,4,1,4115,1,20,1,1,10,12),_ArrisRouterICtrlEnable_Type())
arrisRouterICtrlEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterICtrlEnable.setStatus(_A)
class _ArrisRouterICtrlHashingKey_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,127))
_ArrisRouterICtrlHashingKey_Type.__name__=_G
_ArrisRouterICtrlHashingKey_Object=MibScalar
arrisRouterICtrlHashingKey=_ArrisRouterICtrlHashingKey_Object((1,3,6,1,4,1,4115,1,20,1,1,10,13),_ArrisRouterICtrlHashingKey_Type())
arrisRouterICtrlHashingKey.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterICtrlHashingKey.setStatus(_A)
class _ArrisRouterICtrlPortMapTableEnabled_Type(TruthValue):defaultValue=1
_ArrisRouterICtrlPortMapTableEnabled_Type.__name__=_F
_ArrisRouterICtrlPortMapTableEnabled_Object=MibScalar
arrisRouterICtrlPortMapTableEnabled=_ArrisRouterICtrlPortMapTableEnabled_Object((1,3,6,1,4,1,4115,1,20,1,1,10,14),_ArrisRouterICtrlPortMapTableEnabled_Type())
arrisRouterICtrlPortMapTableEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterICtrlPortMapTableEnabled.setStatus(_A)
_ArrisRouterFlapListCfg_ObjectIdentity=ObjectIdentity
arrisRouterFlapListCfg=_ArrisRouterFlapListCfg_ObjectIdentity((1,3,6,1,4,1,4115,1,20,1,1,11))
class _ArrisRouterFlapListEnable_Type(TruthValue):defaultValue=2
_ArrisRouterFlapListEnable_Type.__name__=_F
_ArrisRouterFlapListEnable_Object=MibScalar
arrisRouterFlapListEnable=_ArrisRouterFlapListEnable_Object((1,3,6,1,4,1,4115,1,20,1,1,11,1),_ArrisRouterFlapListEnable_Type())
arrisRouterFlapListEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterFlapListEnable.setStatus(_A)
class _ArrisRouterFlapListWLANInterval_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_ArrisRouterFlapListWLANInterval_Type.__name__=_D
_ArrisRouterFlapListWLANInterval_Object=MibScalar
arrisRouterFlapListWLANInterval=_ArrisRouterFlapListWLANInterval_Object((1,3,6,1,4,1,4115,1,20,1,1,11,2),_ArrisRouterFlapListWLANInterval_Type())
arrisRouterFlapListWLANInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterFlapListWLANInterval.setStatus(_A)
class _ArrisRouterFlapListDHCPInterval_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_ArrisRouterFlapListDHCPInterval_Type.__name__=_D
_ArrisRouterFlapListDHCPInterval_Object=MibScalar
arrisRouterFlapListDHCPInterval=_ArrisRouterFlapListDHCPInterval_Object((1,3,6,1,4,1,4115,1,20,1,1,11,3),_ArrisRouterFlapListDHCPInterval_Type())
arrisRouterFlapListDHCPInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterFlapListDHCPInterval.setStatus(_A)
class _ArrisRouterFlapListReportPeroid_Type(Integer32):defaultValue=86400;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400))
_ArrisRouterFlapListReportPeroid_Type.__name__=_D
_ArrisRouterFlapListReportPeroid_Object=MibScalar
arrisRouterFlapListReportPeroid=_ArrisRouterFlapListReportPeroid_Object((1,3,6,1,4,1,4115,1,20,1,1,11,4),_ArrisRouterFlapListReportPeroid_Type())
arrisRouterFlapListReportPeroid.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterFlapListReportPeroid.setStatus(_A)
_ArrisRouterFlapListWLANCount_Type=Integer32
_ArrisRouterFlapListWLANCount_Object=MibScalar
arrisRouterFlapListWLANCount=_ArrisRouterFlapListWLANCount_Object((1,3,6,1,4,1,4115,1,20,1,1,11,5),_ArrisRouterFlapListWLANCount_Type())
arrisRouterFlapListWLANCount.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterFlapListWLANCount.setStatus(_A)
_ArrisRouterFlapListLANCount_Type=Integer32
_ArrisRouterFlapListLANCount_Object=MibScalar
arrisRouterFlapListLANCount=_ArrisRouterFlapListLANCount_Object((1,3,6,1,4,1,4115,1,20,1,1,11,6),_ArrisRouterFlapListLANCount_Type())
arrisRouterFlapListLANCount.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterFlapListLANCount.setStatus(_A)
class _ArrisRouterFlapListReqFreqThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ArrisRouterFlapListReqFreqThreshold_Type.__name__=_D
_ArrisRouterFlapListReqFreqThreshold_Object=MibScalar
arrisRouterFlapListReqFreqThreshold=_ArrisRouterFlapListReqFreqThreshold_Object((1,3,6,1,4,1,4115,1,20,1,1,11,7),_ArrisRouterFlapListReqFreqThreshold_Type())
arrisRouterFlapListReqFreqThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisRouterFlapListReqFreqThreshold.setStatus(_A)
_ArrisRouterFlapListWLANTable_Object=MibTable
arrisRouterFlapListWLANTable=_ArrisRouterFlapListWLANTable_Object((1,3,6,1,4,1,4115,1,20,1,1,11,10))
if mibBuilder.loadTexts:arrisRouterFlapListWLANTable.setStatus(_A)
_ArrisRouterFlapListWLANEntry_Object=MibTableRow
arrisRouterFlapListWLANEntry=_ArrisRouterFlapListWLANEntry_Object((1,3,6,1,4,1,4115,1,20,1,1,11,10,1))
arrisRouterFlapListWLANEntry.setIndexNames((0,_I,_BA))
if mibBuilder.loadTexts:arrisRouterFlapListWLANEntry.setStatus(_A)
class _ArrisRouterFlapListWLANIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_ArrisRouterFlapListWLANIndex_Type.__name__=_H
_ArrisRouterFlapListWLANIndex_Object=MibTableColumn
arrisRouterFlapListWLANIndex=_ArrisRouterFlapListWLANIndex_Object((1,3,6,1,4,1,4115,1,20,1,1,11,10,1,1),_ArrisRouterFlapListWLANIndex_Type())
arrisRouterFlapListWLANIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:arrisRouterFlapListWLANIndex.setStatus(_A)
_ArrisRouterFlapListWLANMacAddress_Type=MacAddress
_ArrisRouterFlapListWLANMacAddress_Object=MibTableColumn
arrisRouterFlapListWLANMacAddress=_ArrisRouterFlapListWLANMacAddress_Object((1,3,6,1,4,1,4115,1,20,1,1,11,10,1,2),_ArrisRouterFlapListWLANMacAddress_Type())
arrisRouterFlapListWLANMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterFlapListWLANMacAddress.setStatus(_A)
_ArrisRouterFlapListWLANRemoveTime_Type=DateAndTime
_ArrisRouterFlapListWLANRemoveTime_Object=MibTableColumn
arrisRouterFlapListWLANRemoveTime=_ArrisRouterFlapListWLANRemoveTime_Object((1,3,6,1,4,1,4115,1,20,1,1,11,10,1,3),_ArrisRouterFlapListWLANRemoveTime_Type())
arrisRouterFlapListWLANRemoveTime.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterFlapListWLANRemoveTime.setStatus(_A)
_ArrisRouterFlapListWLANFlapTime_Type=DateAndTime
_ArrisRouterFlapListWLANFlapTime_Object=MibTableColumn
arrisRouterFlapListWLANFlapTime=_ArrisRouterFlapListWLANFlapTime_Object((1,3,6,1,4,1,4115,1,20,1,1,11,10,1,4),_ArrisRouterFlapListWLANFlapTime_Type())
arrisRouterFlapListWLANFlapTime.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterFlapListWLANFlapTime.setStatus(_A)
_ArrisRouterFlapListLANTable_Object=MibTable
arrisRouterFlapListLANTable=_ArrisRouterFlapListLANTable_Object((1,3,6,1,4,1,4115,1,20,1,1,11,11))
if mibBuilder.loadTexts:arrisRouterFlapListLANTable.setStatus(_A)
_ArrisRouterFlapListLANEntry_Object=MibTableRow
arrisRouterFlapListLANEntry=_ArrisRouterFlapListLANEntry_Object((1,3,6,1,4,1,4115,1,20,1,1,11,11,1))
arrisRouterFlapListLANEntry.setIndexNames((0,_I,_BB))
if mibBuilder.loadTexts:arrisRouterFlapListLANEntry.setStatus(_A)
class _ArrisRouterFlapListLANIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_ArrisRouterFlapListLANIndex_Type.__name__=_H
_ArrisRouterFlapListLANIndex_Object=MibTableColumn
arrisRouterFlapListLANIndex=_ArrisRouterFlapListLANIndex_Object((1,3,6,1,4,1,4115,1,20,1,1,11,11,1,1),_ArrisRouterFlapListLANIndex_Type())
arrisRouterFlapListLANIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:arrisRouterFlapListLANIndex.setStatus(_A)
_ArrisRouterFlapListLANMacAddress_Type=MacAddress
_ArrisRouterFlapListLANMacAddress_Object=MibTableColumn
arrisRouterFlapListLANMacAddress=_ArrisRouterFlapListLANMacAddress_Object((1,3,6,1,4,1,4115,1,20,1,1,11,11,1,2),_ArrisRouterFlapListLANMacAddress_Type())
arrisRouterFlapListLANMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterFlapListLANMacAddress.setStatus(_A)
_ArrisRouterFlapListLANRemoveTime_Type=DateAndTime
_ArrisRouterFlapListLANRemoveTime_Object=MibTableColumn
arrisRouterFlapListLANRemoveTime=_ArrisRouterFlapListLANRemoveTime_Object((1,3,6,1,4,1,4115,1,20,1,1,11,11,1,3),_ArrisRouterFlapListLANRemoveTime_Type())
arrisRouterFlapListLANRemoveTime.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterFlapListLANRemoveTime.setStatus(_A)
_ArrisRouterFlapListLANFlapTime_Type=DateAndTime
_ArrisRouterFlapListLANFlapTime_Object=MibTableColumn
arrisRouterFlapListLANFlapTime=_ArrisRouterFlapListLANFlapTime_Object((1,3,6,1,4,1,4115,1,20,1,1,11,11,1,4),_ArrisRouterFlapListLANFlapTime_Type())
arrisRouterFlapListLANFlapTime.setMaxAccess(_C)
if mibBuilder.loadTexts:arrisRouterFlapListLANFlapTime.setStatus(_A)
mibBuilder.exportSymbols(_I,**{'arrisRouterMib':arrisRouterMib,'arrisRouterMibObjects':arrisRouterMibObjects,'arrisRouterWanConfig':arrisRouterWanConfig,'arrisRouterWanConnType':arrisRouterWanConnType,'arrisRouterWanConnHostName':arrisRouterWanConnHostName,'arrisRouterWanConnDomainName':arrisRouterWanConnDomainName,'arrisRouterWanMTUSize':arrisRouterWanMTUSize,'arrisRouterWanCurrentTable':arrisRouterWanCurrentTable,'arrisRouterWanCurrentEntry':arrisRouterWanCurrentEntry,_h:arrisRouterWanCurrentIPIndex,'arrisRouterWanCurrentIPAddrType':arrisRouterWanCurrentIPAddrType,'arrisRouterWanCurrentIPAddr':arrisRouterWanCurrentIPAddr,'arrisRouterWanCurrentPrefix':arrisRouterWanCurrentPrefix,'arrisRouterWanCurrentGWType':arrisRouterWanCurrentGWType,'arrisRouterWanCurrentGW':arrisRouterWanCurrentGW,'arrisRouterWanCurrentIPType':arrisRouterWanCurrentIPType,'arrisRouterWanCurrentNetMask':arrisRouterWanCurrentNetMask,'arrisRouterWanCurrentPrefixDelegationV6':arrisRouterWanCurrentPrefixDelegationV6,'arrisRouterWanCurrentPrefixDelegationV6Len':arrisRouterWanCurrentPrefixDelegationV6Len,'arrisRouterWanCurrentPreferredLifetimeV6':arrisRouterWanCurrentPreferredLifetimeV6,'arrisRouterWanCurrentValidLifetimeV6':arrisRouterWanCurrentValidLifetimeV6,'arrisRouterWanStaticFreeIdx':arrisRouterWanStaticFreeIdx,'arrisRouterWanStaticTable':arrisRouterWanStaticTable,'arrisRouterWanStaticEntry':arrisRouterWanStaticEntry,_w:arrisRouterWanStaticIPIndex,'arrisRouterWanStaticIPAddrType':arrisRouterWanStaticIPAddrType,'arrisRouterWanStaticIPAddr':arrisRouterWanStaticIPAddr,'arrisRouterWanStaticPrefix':arrisRouterWanStaticPrefix,'arrisRouterWanStaticGatewayType':arrisRouterWanStaticGatewayType,'arrisRouterWanStaticGateway':arrisRouterWanStaticGateway,'arrisRouterWanStaticRowStatus':arrisRouterWanStaticRowStatus,'arrisRouterWanDelegatedPrefixLength':arrisRouterWanDelegatedPrefixLength,'arrisRouterWanDelegatedPrefix':arrisRouterWanDelegatedPrefix,'arrisRouterWanTunnelObjects':arrisRouterWanTunnelObjects,'arrisRouterWanUserName':arrisRouterWanUserName,'arrisRouterWanPassword':arrisRouterWanPassword,'arrisRouterWanEnableIdleTimeout':arrisRouterWanEnableIdleTimeout,'arrisRouterWanIdleTimeout':arrisRouterWanIdleTimeout,'arrisRouterWanTunnelAddrType':arrisRouterWanTunnelAddrType,'arrisRouterWanTunnelAddr':arrisRouterWanTunnelAddr,'arrisRouterWanTunnelHostName':arrisRouterWanTunnelHostName,'arrisRouterWanEnableKeepAlive':arrisRouterWanEnableKeepAlive,'arrisRouterWanKeepAliveTimeout':arrisRouterWanKeepAliveTimeout,'arrisRouterWanDNSObjects':arrisRouterWanDNSObjects,'arrisRouterWanUseAutoDNS':arrisRouterWanUseAutoDNS,'arrisRouterWanCurrentDNSTable':arrisRouterWanCurrentDNSTable,'arrisRouterWanCurrentDNSEntry':arrisRouterWanCurrentDNSEntry,_x:arrisRouterWanCurrentDNSIPIndex,'arrisRouterWanCurrentDNSIPAddrType':arrisRouterWanCurrentDNSIPAddrType,'arrisRouterWanCurrentDNSIPAddr':arrisRouterWanCurrentDNSIPAddr,'arrisRouterWanStaticDNSTable':arrisRouterWanStaticDNSTable,'arrisRouterWanStaticDNSEntry':arrisRouterWanStaticDNSEntry,_y:arrisRouterWanStaticDNSIPIndex,'arrisRouterWanStaticDNSIPAddrType':arrisRouterWanStaticDNSIPAddrType,'arrisRouterWanStaticDNSIPAddr':arrisRouterWanStaticDNSIPAddr,'arrisRouterWanStaticDNSRowStatus':arrisRouterWanStaticDNSRowStatus,'arrisRouterWanDHCPObjects':arrisRouterWanDHCPObjects,'arrisRouterWanRenewLease':arrisRouterWanRenewLease,'arrisRouterWanReleaseLease':arrisRouterWanReleaseLease,'arrisRouterWanDHCPDuration':arrisRouterWanDHCPDuration,'arrisRouterWanDHCPExpire':arrisRouterWanDHCPExpire,'arrisRouterWanRenewLeaseV6':arrisRouterWanRenewLeaseV6,'arrisRouterWanReleaseLeaseV6':arrisRouterWanReleaseLeaseV6,'arrisRouterWanDHCPDurationV6':arrisRouterWanDHCPDurationV6,'arrisRouterWanDHCPExpireV6':arrisRouterWanDHCPExpireV6,'arrisRouterWanDhcpSrvIPAddr':arrisRouterWanDhcpSrvIPAddr,'arrisRouterWanDhcpOpt43Sub02':arrisRouterWanDhcpOpt43Sub02,'arrisRouterWanDHCPDUIDV6':arrisRouterWanDHCPDUIDV6,'arrisRouterWanDHCPSrvAddrV6':arrisRouterWanDHCPSrvAddrV6,'arrisRouterWanDHCPSrvDUIDV6':arrisRouterWanDHCPSrvDUIDV6,'arrisRouterWanIFMacAddr':arrisRouterWanIFMacAddr,'arrisRouterWanConnTypeV6':arrisRouterWanConnTypeV6,'arrisRouterWanIPProvMode':arrisRouterWanIPProvMode,'arrisRouterDSLiteWanObjects':arrisRouterDSLiteWanObjects,'arrisRouterDSLiteWanEnable':arrisRouterDSLiteWanEnable,'arrisRouterDSLiteWanLSNATAddrType':arrisRouterDSLiteWanLSNATAddrType,'arrisRouterDSLiteWanLSNATAddr':arrisRouterDSLiteWanLSNATAddr,'arrisRouterDSLiteTcpMssClamping':arrisRouterDSLiteTcpMssClamping,'arrisRouterDSLiteTcpMssValue':arrisRouterDSLiteTcpMssValue,'arrisRouterDSLiteWanResolvedAddr':arrisRouterDSLiteWanResolvedAddr,'arrisRouterSoftGreWanObjects':arrisRouterSoftGreWanObjects,'arrisRouterSoftGreWanTable':arrisRouterSoftGreWanTable,'arrisRouterSoftGreWanEntry':arrisRouterSoftGreWanEntry,'arrisRouterSoftGreWanEnable':arrisRouterSoftGreWanEnable,'arrisRouterSoftGreMappedInterface':arrisRouterSoftGreMappedInterface,'arrisRouterSoftGreMaxSessions':arrisRouterSoftGreMaxSessions,'arrisRouterSoftGreWanControllerFqdn':arrisRouterSoftGreWanControllerFqdn,'arrisRouterSoftGreWanControllerProvisionedSecondaryIpAddressType':arrisRouterSoftGreWanControllerProvisionedSecondaryIpAddressType,'arrisRouterSoftGreWanControllerProvisionedSecondaryIpAddress':arrisRouterSoftGreWanControllerProvisionedSecondaryIpAddress,'arrisRouterSoftGreWanFailoverPingCount':arrisRouterSoftGreWanFailoverPingCount,'arrisRouterSoftGreWanFailoverPingInterval':arrisRouterSoftGreWanFailoverPingInterval,'arrisRouterSoftGreWanFailoverThreshold':arrisRouterSoftGreWanFailoverThreshold,'arrisRouterSoftGreCircuitIdEnabled':arrisRouterSoftGreCircuitIdEnabled,'arrisRouterSoftGreRemoteIdEnabled':arrisRouterSoftGreRemoteIdEnabled,'arrisRouterSoftGreRadiusEnabled':arrisRouterSoftGreRadiusEnabled,'arrisRouterSoftGreRadiusServerAddressType':arrisRouterSoftGreRadiusServerAddressType,'arrisRouterSoftGreRadiusServerAddress':arrisRouterSoftGreRadiusServerAddress,'arrisRouterSoftGreRadiusServerPort':arrisRouterSoftGreRadiusServerPort,'arrisRouterSoftGreRadiusKey':arrisRouterSoftGreRadiusKey,'arrisRouterSoftGreRadiusReAuthInterval':arrisRouterSoftGreRadiusReAuthInterval,'arrisRouterSoftGreVlanQEnable':arrisRouterSoftGreVlanQEnable,'arrisRouterSoftGreWanDscp':arrisRouterSoftGreWanDscp,'arrisRouterSoftGreWanDNSRetryTimer':arrisRouterSoftGreWanDNSRetryTimer,'arrisRouterSoftGreWanCurrentControllerIPAddressType':arrisRouterSoftGreWanCurrentControllerIPAddressType,'arrisRouterSoftGreWanCurrentControllerIPAddress':arrisRouterSoftGreWanCurrentControllerIPAddress,'arrisRouterSoftGreWanPrimaryControllerIPAddressType':arrisRouterSoftGreWanPrimaryControllerIPAddressType,'arrisRouterSoftGreWanPrimaryControllerIPAddress':arrisRouterSoftGreWanPrimaryControllerIPAddress,'arrisRouterSoftGreWanSecondaryControllerIPAddressType':arrisRouterSoftGreWanSecondaryControllerIPAddressType,'arrisRouterSoftGreWanSecondaryControllerIPAddress':arrisRouterSoftGreWanSecondaryControllerIPAddress,'arrisRouterSoftGreWanStatus':arrisRouterSoftGreWanStatus,'arrisRouterSoftGreTransportInterface':arrisRouterSoftGreTransportInterface,'arrisRouterSoftGreRadiusTransportInterface':arrisRouterSoftGreRadiusTransportInterface,'arrisRouterSoftGreAcctServerAddressType':arrisRouterSoftGreAcctServerAddressType,'arrisRouterSoftGreAcctServerAddress':arrisRouterSoftGreAcctServerAddress,'arrisRouterSoftGreAcctServerPort':arrisRouterSoftGreAcctServerPort,'arrisRouterSoftGreAcctKey':arrisRouterSoftGreAcctKey,'arrisRouterSoftGreAcctInterval':arrisRouterSoftGreAcctInterval,'arrisRouterSoftGreRadiusSecondaryServerAddressType':arrisRouterSoftGreRadiusSecondaryServerAddressType,'arrisRouterSoftGreRadiusSecondaryServerAddress':arrisRouterSoftGreRadiusSecondaryServerAddress,'arrisRouterSoftGreRadiusSecondaryServerPort':arrisRouterSoftGreRadiusSecondaryServerPort,'arrisRouterSoftGreRadiusSecondaryKey':arrisRouterSoftGreRadiusSecondaryKey,'arrisRouterSoftGreRadiusSecondaryReAuthInterval':arrisRouterSoftGreRadiusSecondaryReAuthInterval,'arrisRouterSoftGreSSIDTable':arrisRouterSoftGreSSIDTable,'arrisRouterSoftGreSSIDEntry':arrisRouterSoftGreSSIDEntry,'arrisRouterSoftGreVLanId':arrisRouterSoftGreVLanId,'arrisRouterSoftGreVLanPriority':arrisRouterSoftGreVLanPriority,'arrisRouterSoftGreCustomerOptOut':arrisRouterSoftGreCustomerOptOut,'arrisRouterSoftGreCapable':arrisRouterSoftGreCapable,'arrisRouterDHCPRelayAgentWanObjects':arrisRouterDHCPRelayAgentWanObjects,'arrisRouterDHCPRelayAgentSSIDTable':arrisRouterDHCPRelayAgentSSIDTable,'arrisRouterDHCPRelayAgentSSIDEntry':arrisRouterDHCPRelayAgentSSIDEntry,'arrisRouterDHCPRelayAgentEnable':arrisRouterDHCPRelayAgentEnable,'arrisRouterDHCPRelayAgentCircuitIdEnabled':arrisRouterDHCPRelayAgentCircuitIdEnabled,'arrisRouterDHCPRelayAgentRemoteIdEnabled':arrisRouterDHCPRelayAgentRemoteIdEnabled,'arrisRouterDHCPRelayAgentOption60SSIDEnabled':arrisRouterDHCPRelayAgentOption60SSIDEnabled,'arrisRouterWanTR181GatewayInfoObjects':arrisRouterWanTR181GatewayInfoObjects,'arrisRouterTR181GatewayManufacturerOUI':arrisRouterTR181GatewayManufacturerOUI,'arrisRouterTR181GatewayProductClass':arrisRouterTR181GatewayProductClass,'arrisRouterTR181GatewaySerialNumber':arrisRouterTR181GatewaySerialNumber,'arrisRouterWanForceIGMPVersion':arrisRouterWanForceIGMPVersion,'arrisRouterLanConfig':arrisRouterLanConfig,'arrisRouterLanSrvTable':arrisRouterLanSrvTable,'arrisRouterLanSrvEntry':arrisRouterLanSrvEntry,'arrisRouterLanName':arrisRouterLanName,'arrisRouterLanSubnetMaskType':arrisRouterLanSubnetMaskType,'arrisRouterLanSubnetMask':arrisRouterLanSubnetMask,'arrisRouterLanGatewayIpType':arrisRouterLanGatewayIpType,'arrisRouterLanGatewayIp':arrisRouterLanGatewayIp,'arrisRouterLanGatewayIp2Type':arrisRouterLanGatewayIp2Type,'arrisRouterLanGatewayIp2':arrisRouterLanGatewayIp2,'arrisRouterLanVLanID':arrisRouterLanVLanID,'arrisRouterLanUseDHCP':arrisRouterLanUseDHCP,'arrisRouterLanStartDHCPType':arrisRouterLanStartDHCPType,'arrisRouterLanStartDHCP':arrisRouterLanStartDHCP,'arrisRouterLanEndDHCPType':arrisRouterLanEndDHCPType,'arrisRouterLanEndDHCP':arrisRouterLanEndDHCP,'arrisRouterLanLeaseTime':arrisRouterLanLeaseTime,'arrisRouterLanDomainName':arrisRouterLanDomainName,'arrisRouterLanRelayDNS':arrisRouterLanRelayDNS,'arrisRouterLanPassThru':arrisRouterLanPassThru,'arrisRouterLanFirewallOn':arrisRouterLanFirewallOn,'arrisRouterLanUPnPEnable':arrisRouterLanUPnPEnable,'arrisRouterLanCPEAging':arrisRouterLanCPEAging,'arrisRouterLanOverrideDNS':arrisRouterLanOverrideDNS,'arrisRouterLanNatAlgsEnabled':arrisRouterLanNatAlgsEnabled,'arrisRouterLanMappedInterface':arrisRouterLanMappedInterface,'arrisRouterLanEnvironmentControl':arrisRouterLanEnvironmentControl,'arrisRouterLanPrefixLengthV6':arrisRouterLanPrefixLengthV6,'arrisRouterLanUseDHCPV6':arrisRouterLanUseDHCPV6,'arrisRouterLanStartDHCPV6':arrisRouterLanStartDHCPV6,'arrisRouterLanEndDHCPV6':arrisRouterLanEndDHCPV6,'arrisRouterLanLeaseTimeV6':arrisRouterLanLeaseTimeV6,'arrisRouterLanLinkLocalAddressV6':arrisRouterLanLinkLocalAddressV6,'arrisRouterLanDNSRelayV6':arrisRouterLanDNSRelayV6,'arrisRouterLanDNSOverrideV6':arrisRouterLanDNSOverrideV6,'arrisRouterLanPreProvLeaseTime':arrisRouterLanPreProvLeaseTime,'arrisRouterLanParentalControlsEnable':arrisRouterLanParentalControlsEnable,'arrisRouterLanDNSTable':arrisRouterLanDNSTable,'arrisRouterLanDNSEntry':arrisRouterLanDNSEntry,_z:arrisRouterLanDNSIdx,'arrisRouterLanDNSIPAddrType':arrisRouterLanDNSIPAddrType,'arrisRouterLanDNSIPAddr':arrisRouterLanDNSIPAddr,'arrisRouterLanDNSRowStatus':arrisRouterLanDNSRowStatus,'arrisRouterClientObjects':arrisRouterClientObjects,'arrisRouterLanClientCount':arrisRouterLanClientCount,'arrisRouterLanClientTable':arrisRouterLanClientTable,'arrisRouterLanClientEntry':arrisRouterLanClientEntry,_i:arrisRouterLanClientIPAddrType,_j:arrisRouterLanClientIPAddr,'arrisRouterLanClientHostName':arrisRouterLanClientHostName,'arrisRouterLanClientMAC':arrisRouterLanClientMAC,'arrisRouterLanClientAdapterType':arrisRouterLanClientAdapterType,'arrisRouterLanClientType':arrisRouterLanClientType,'arrisRouterLanClientLeaseEnd':arrisRouterLanClientLeaseEnd,'arrisRouterLanClientRowStatus':arrisRouterLanClientRowStatus,'arrisRouterLanClientOnline':arrisRouterLanClientOnline,'arrisRouterLanClientComment':arrisRouterLanClientComment,'arrisRouterLanClientManufacturerOUI':arrisRouterLanClientManufacturerOUI,'arrisRouterLanClientSerialNumber':arrisRouterLanClientSerialNumber,'arrisRouterLanClientProductClass':arrisRouterLanClientProductClass,'arrisRouterLanClientDeviceName':arrisRouterLanClientDeviceName,'arrisRouterLanClientLastChange':arrisRouterLanClientLastChange,'arrisRouterLanClientTimeConnected':arrisRouterLanClientTimeConnected,'arrisRouterDeviceUpDownTable':arrisRouterDeviceUpDownTable,'arrisRouterDeviceUpDownEntry':arrisRouterDeviceUpDownEntry,_A0:arrisRouterDeviceUpDownIndex,'arrisRouterDeviceUpDownMAC':arrisRouterDeviceUpDownMAC,'arrisRouterDeviceUpDownIPType':arrisRouterDeviceUpDownIPType,'arrisRouterDeviceUpDownStatus':arrisRouterDeviceUpDownStatus,'arrisRouterLanCustomCount':arrisRouterLanCustomCount,'arrisRouterLanCustomTable':arrisRouterLanCustomTable,'arrisRouterLanCustomEntry':arrisRouterLanCustomEntry,_A1:arrisRouterLanCustomIdx,'arrisRouterLanCustomMAC':arrisRouterLanCustomMAC,'arrisRouterLanCustomIPAddrType':arrisRouterLanCustomIPAddrType,'arrisRouterLanCustomIPAddr':arrisRouterLanCustomIPAddr,'arrisRouterLanCustomFriendName':arrisRouterLanCustomFriendName,'arrisRouterLanCustomHostName':arrisRouterLanCustomHostName,'arrisRouterLanCustomMACMfg':arrisRouterLanCustomMACMfg,'arrisRouterLanCustomComments':arrisRouterLanCustomComments,'arrisRouterLanCustomRowStatus':arrisRouterLanCustomRowStatus,'arrisRouterLanClientDHCPOptionsTable':arrisRouterLanClientDHCPOptionsTable,'arrisRouterLanClientDHCPOptionsEntry':arrisRouterLanClientDHCPOptionsEntry,_A2:arrisRouterLanClientDHCPOptionsIdx,'arrisRouterLanClientDHCPOptionsTag':arrisRouterLanClientDHCPOptionsTag,'arrisRouterLanClientDHCPOptionsValue':arrisRouterLanClientDHCPOptionsValue,'arrisRouterLanClientDHCPOptionsRowStatus':arrisRouterLanClientDHCPOptionsRowStatus,'arrisRouterRIPObjects':arrisRouterRIPObjects,'arrisRouterRIPEnable':arrisRouterRIPEnable,'arrisRouterRIPAuthEnable':arrisRouterRIPAuthEnable,'arrisRouterRIPReportTime':arrisRouterRIPReportTime,'arrisRouterRIPAuthKeyString':arrisRouterRIPAuthKeyString,'arrisRouterRIPAuthKeyID':arrisRouterRIPAuthKeyID,'arrisRouterRIPIPAddrType':arrisRouterRIPIPAddrType,'arrisRouterRIPIPAddr':arrisRouterRIPIPAddr,'arrisRouterRIPPrefixLen':arrisRouterRIPPrefixLen,'arrisRouterRIPAuthKeyChain':arrisRouterRIPAuthKeyChain,'arrisRouterRIPRoutedSubnetIPType':arrisRouterRIPRoutedSubnetIPType,'arrisRouterRIPRoutedSubnetIP':arrisRouterRIPRoutedSubnetIP,'arrisRouterRIPRoutedSubnetGWNetIPType':arrisRouterRIPRoutedSubnetGWNetIPType,'arrisRouterRIPRoutedSubnetGWNetIP':arrisRouterRIPRoutedSubnetGWNetIP,'arrisRouterRIPRoutedSubnetMask':arrisRouterRIPRoutedSubnetMask,'arrisRouterRIPRoutedSubnetEnabled':arrisRouterRIPRoutedSubnetEnabled,'arrisRouterRIPSendCMInterface':arrisRouterRIPSendCMInterface,'arrisRouterRIPRoutedSubnetDHCP':arrisRouterRIPRoutedSubnetDHCP,'arrisRouterRIPRoutedSubnetNAT':arrisRouterRIPRoutedSubnetNAT,'arrisRouterLanSettings':arrisRouterLanSettings,'arrisRouterLanEtherPortTable':arrisRouterLanEtherPortTable,'arrisRouterLanEtherPortEntry':arrisRouterLanEtherPortEntry,_A3:arrisRouterLanEtherPortIdx,'arrisRouterLanEtherPortIFIndex':arrisRouterLanEtherPortIFIndex,'arrisRouterLanEtherPortEnabled':arrisRouterLanEtherPortEnabled,'arrisRouterLanEtherPortDuplex':arrisRouterLanEtherPortDuplex,'arrisRouterLanEtherPortSpeed':arrisRouterLanEtherPortSpeed,'arrisRouterLanEtherPortAuto':arrisRouterLanEtherPortAuto,'arrisRouterLanEtherPortHasLink':arrisRouterLanEtherPortHasLink,'arrisRouterRIPngObjects':arrisRouterRIPngObjects,'arrisRouterRIPngEnable':arrisRouterRIPngEnable,'arrisRouterRIPngAddr':arrisRouterRIPngAddr,'arrisRouterRIPngSubnetEnable':arrisRouterRIPngSubnetEnable,'arrisRouterRIPngRoutedSubnetAddr':arrisRouterRIPngRoutedSubnetAddr,'arrisRouterRIPngRoutedSubnetPrefixLength':arrisRouterRIPngRoutedSubnetPrefixLength,'arrisRouterRIPngSendCMInterface':arrisRouterRIPngSendCMInterface,'arrisRouterLanSrvDHCPOptionsTable':arrisRouterLanSrvDHCPOptionsTable,'arrisRouterLanSrvDHCPOptionsEntry':arrisRouterLanSrvDHCPOptionsEntry,_A4:arrisRouterLanSrvDHCPOptionsIdx,'arrisRouterLanSrvDHCPOptionsEnable':arrisRouterLanSrvDHCPOptionsEnable,'arrisRouterLanSrvDHCPOptionsIPAddrType':arrisRouterLanSrvDHCPOptionsIPAddrType,'arrisRouterLanSrvDHCPOptionsTag':arrisRouterLanSrvDHCPOptionsTag,'arrisRouterLanSrvDHCPOptionsValue':arrisRouterLanSrvDHCPOptionsValue,'arrisRouterLanSrvDHCPOptionsRowStatus':arrisRouterLanSrvDHCPOptionsRowStatus,'arrisRouterLanMaxIPv6RAInterval':arrisRouterLanMaxIPv6RAInterval,'arrisRouterLanMinIPv6RAInterval':arrisRouterLanMinIPv6RAInterval,'arrisRouterLanBridgeType':arrisRouterLanBridgeType,'arrisRouterLanUSBPortTable':arrisRouterLanUSBPortTable,'arrisRouterLanUSBPortEntry':arrisRouterLanUSBPortEntry,_A5:arrisRouterLanUSBPortIdx,'arrisRouterLanUSBPortHasLink':arrisRouterLanUSBPortHasLink,'arrisRouterLanUSBPortDescr':arrisRouterLanUSBPortDescr,'arrisRouterLanUSBPortSerialNum':arrisRouterLanUSBPortSerialNum,'arrisRouterLanUSBPortSpeed':arrisRouterLanUSBPortSpeed,'arrisRouterLanUSBPortManuf':arrisRouterLanUSBPortManuf,'arrisRouterLanUSBPortStorageNam':arrisRouterLanUSBPortStorageNam,'arrisRouterLanUSBPortFileSys':arrisRouterLanUSBPortFileSys,'arrisRouterLanUSBPortSpaceAvail':arrisRouterLanUSBPortSpaceAvail,'arrisRouterLanUSBPortTotalSpace':arrisRouterLanUSBPortTotalSpace,'arrisRouterLanUsbPortFoldersFile':arrisRouterLanUsbPortFoldersFile,'arrisRouterLanUSBPortDelStorage':arrisRouterLanUSBPortDelStorage,'arrisRouterLanFileSharingObjs':arrisRouterLanFileSharingObjs,'arrisRouterLanFilesharingEnable':arrisRouterLanFilesharingEnable,'arrisRouterLanFilesharingDevName':arrisRouterLanFilesharingDevName,'arrisRouterLanFileSharingTable':arrisRouterLanFileSharingTable,'arrisRouterLanFileSharingEntry':arrisRouterLanFileSharingEntry,_k:arrisRouterLanFilesharingIdx,'arrisRouterLanFilesharingRowStatus':arrisRouterLanFilesharingRowStatus,'arrisRouterLanFilesharingUsbPort':arrisRouterLanFilesharingUsbPort,'arrisRouterLanFilesharingDirectory':arrisRouterLanFilesharingDirectory,'arrisRouterLanFilesharingName':arrisRouterLanFilesharingName,'arrisRouterLanFilesharingEnableHttp':arrisRouterLanFilesharingEnableHttp,'arrisRouterLanFilesharingEnableFtp':arrisRouterLanFilesharingEnableFtp,'arrisRouterLanFilesharingVisibility':arrisRouterLanFilesharingVisibility,'arrisRouterLanFilesharingEveryOnePerm':arrisRouterLanFilesharingEveryOnePerm,'arrisRouterLanFilesharingDesc':arrisRouterLanFilesharingDesc,'arrisRouterLanLocalUserTable':arrisRouterLanLocalUserTable,'arrisRouterLanLocalUserEntry':arrisRouterLanLocalUserEntry,_l:arrisRouterLanLocalUserIdx,'arrisRouterLanLocalUserRowStatus':arrisRouterLanLocalUserRowStatus,'arrisRouterLanLocalUserName':arrisRouterLanLocalUserName,'arrisRouterLanLocalUserPasswd':arrisRouterLanLocalUserPasswd,'arrisRouterLanFilesharingPermitTable':arrisRouterLanFilesharingPermitTable,'arrisRouterLanFilesharingPermitEntry':arrisRouterLanFilesharingPermitEntry,'arrisRouterLanFilesharingPermitvalue':arrisRouterLanFilesharingPermitvalue,'arrisRouterLanIPv6RALifetime':arrisRouterLanIPv6RALifetime,'arrisRouterWirelessCfg':arrisRouterWirelessCfg,'arrisRouterWiFiCountry':arrisRouterWiFiCountry,'arrisRouterWiFiChannel':arrisRouterWiFiChannel,'arrisRouterWiFiMode':arrisRouterWiFiMode,'arrisRouterWiFiBGProtect':arrisRouterWiFiBGProtect,'arrisRouterWiFiBeaconInterval':arrisRouterWiFiBeaconInterval,'arrisRouterWiFiDTIMInterval':arrisRouterWiFiDTIMInterval,'arrisRouterWiFiTxPreamble':arrisRouterWiFiTxPreamble,'arrisRouterWiFiRTSThreshold':arrisRouterWiFiRTSThreshold,'arrisRouterWiFiFragmentThresh':arrisRouterWiFiFragmentThresh,'arrisRouterWiFiShortSlot':arrisRouterWiFiShortSlot,'arrisRouterWiFiFrameBurst':arrisRouterWiFiFrameBurst,'arrisRouterWiFiEnableRadio':arrisRouterWiFiEnableRadio,'arrisRouterWiFiShortRetryLimit':arrisRouterWiFiShortRetryLimit,'arrisRouterWiFiLongRetryLimit':arrisRouterWiFiLongRetryLimit,'arrisRouterWiFiOutputPower':arrisRouterWiFiOutputPower,'arrisRouterWiFi80211NSettings':arrisRouterWiFi80211NSettings,'arrisRouterWiFi80211NBand':arrisRouterWiFi80211NBand,'arrisRouterWiFiHTMCS':arrisRouterWiFiHTMCS,'arrisRouterWiFiChannelBW':arrisRouterWiFiChannelBW,'arrisRouterWiFi80211NSideBand':arrisRouterWiFi80211NSideBand,'arrisRouterWiFiHTMode':arrisRouterWiFiHTMode,'arrisRouterWiFiGuardInterval':arrisRouterWiFiGuardInterval,'arrisRouterWiFiDeclinePeerBA':arrisRouterWiFiDeclinePeerBA,'arrisRouterWiFiBlockAck':arrisRouterWiFiBlockAck,'arrisRouterWiFiNProtection':arrisRouterWiFiNProtection,'arrisRouterWiFiAllow40MHzOnlyOperation':arrisRouterWiFiAllow40MHzOnlyOperation,'arrisRouterBSSTable':arrisRouterBSSTable,'arrisRouterBSSEntry':arrisRouterBSSEntry,'arrisRouterBssID':arrisRouterBssID,'arrisRouterBssSSID':arrisRouterBssSSID,'arrisRouterBssActive':arrisRouterBssActive,'arrisRouterBssSSIDBroadcast':arrisRouterBssSSIDBroadcast,'arrisRouterBssSecurityMode':arrisRouterBssSecurityMode,'arrisRouterBssAccessMode':arrisRouterBssAccessMode,'arrisRouterBssNetworkIsolate':arrisRouterBssNetworkIsolate,'arrisRouterBssMACAccessCount':arrisRouterBssMACAccessCount,'arrisRouterBssMACAccessClear':arrisRouterBssMACAccessClear,'arrisRouterBSSArpAuditInterval':arrisRouterBSSArpAuditInterval,'arrisRouterBssMaxWifiClients':arrisRouterBssMaxWifiClients,'arrisRouterBssWmmEnable':arrisRouterBssWmmEnable,'arrisRouterBssWmmAPSD':arrisRouterBssWmmAPSD,'arrisRouterBssActiveTimeout':arrisRouterBssActiveTimeout,'arrisRouterDefaultBssSSID':arrisRouterDefaultBssSSID,'arrisRouterBssStaSteeringEnable':arrisRouterBssStaSteeringEnable,'arrisRouterWEPTable':arrisRouterWEPTable,'arrisRouterWEPEntry':arrisRouterWEPEntry,'arrisRouterWEPCurrentKey':arrisRouterWEPCurrentKey,'arrisRouterWEPEncryptionMode':arrisRouterWEPEncryptionMode,'arrisRouterWEP64BitKeyTable':arrisRouterWEP64BitKeyTable,'arrisRouterWEP64BitKeyEntry':arrisRouterWEP64BitKeyEntry,_AJ:arrisRouterWEP64BitKeyIndex,'arrisRouterWEP64BitKeyValue':arrisRouterWEP64BitKeyValue,'arrisRouterWEP64BitKeyStatus':arrisRouterWEP64BitKeyStatus,'arrisRouterWEP128BitKeyTable':arrisRouterWEP128BitKeyTable,'arrisRouterWEP128BitKeyEntry':arrisRouterWEP128BitKeyEntry,_AK:arrisRouterWEP128BitKeyIndex,'arrisRouterWEP128BitKeyValue':arrisRouterWEP128BitKeyValue,'arrisRouterWEP128BitKeyStatus':arrisRouterWEP128BitKeyStatus,'arrisRouterWPATable':arrisRouterWPATable,'arrisRouterWPAEntry':arrisRouterWPAEntry,'arrisRouterWPAAlgorithm':arrisRouterWPAAlgorithm,'arrisRouterWPAPreSharedKey':arrisRouterWPAPreSharedKey,'arrisRouterWPAReAuthInterval':arrisRouterWPAReAuthInterval,'arrisRouterWPAPreAuthEnable':arrisRouterWPAPreAuthEnable,'arrisRouterDefaultWPAPreSharedKey':arrisRouterDefaultWPAPreSharedKey,'arrisRouterRadiusTable':arrisRouterRadiusTable,'arrisRouterRadiusEntry':arrisRouterRadiusEntry,'arrisRouterRadiusAddressType':arrisRouterRadiusAddressType,'arrisRouterRadiusAddress':arrisRouterRadiusAddress,'arrisRouterRadiusPort':arrisRouterRadiusPort,'arrisRouterRadiusKey':arrisRouterRadiusKey,'arrisRouterRadiusReAuthInterval':arrisRouterRadiusReAuthInterval,'arrisRouterMACAccessTable':arrisRouterMACAccessTable,'arrisRouterMACAccessEntry':arrisRouterMACAccessEntry,_AL:arrisRouterMACAccessIndex,'arrisRouterMACAccessAddr':arrisRouterMACAccessAddr,'arrisRouterMACAccessStatus':arrisRouterMACAccessStatus,'arrisRouterMACAccessDeviceName':arrisRouterMACAccessDeviceName,'arrisRouterWMMCfg':arrisRouterWMMCfg,'arrisRouterWMMEnable':arrisRouterWMMEnable,'arrisRouterWMMNoAck':arrisRouterWMMNoAck,'arrisRouterWMMAPSD':arrisRouterWMMAPSD,'arrisRouterWMMEDCAAPTable':arrisRouterWMMEDCAAPTable,'arrisRouterWMMEDCAAPEntry':arrisRouterWMMEDCAAPEntry,_AM:arrisRouterWMMEDCAAPIndex,'arrisRouterWMMEDCAAPCWmin':arrisRouterWMMEDCAAPCWmin,'arrisRouterWMMEDCAAPCWmax':arrisRouterWMMEDCAAPCWmax,'arrisRouterWMMEDCAAPAIFSN':arrisRouterWMMEDCAAPAIFSN,'arrisRouterWMMEDCAAPTxOpBLimit':arrisRouterWMMEDCAAPTxOpBLimit,'arrisRouterWMMEDCAAPTxOpAGLimit':arrisRouterWMMEDCAAPTxOpAGLimit,'arrisRouterWMMEDCAAPAdmitCont':arrisRouterWMMEDCAAPAdmitCont,'arrisRouterWMMEDCAAPDiscardOld':arrisRouterWMMEDCAAPDiscardOld,'arrisRouterWPSCfg':arrisRouterWPSCfg,'arrisRouterWpsMode':arrisRouterWpsMode,'arrisRouterWpsConfigState':arrisRouterWpsConfigState,'arrisRouterWpsDevicePIN':arrisRouterWpsDevicePIN,'arrisRouterWpsDeviceName':arrisRouterWpsDeviceName,'arrisRouterWpsModelName':arrisRouterWpsModelName,'arrisRouterWpsMfg':arrisRouterWpsMfg,'arrisRouterWpsResultStatus':arrisRouterWpsResultStatus,'arrisRouterWpsStatus':arrisRouterWpsStatus,'arrisRouterWpsConfigTimeout':arrisRouterWpsConfigTimeout,'arrisRouterWpsSTAPin':arrisRouterWpsSTAPin,'arrisRouterWpsPushButton':arrisRouterWpsPushButton,'arrisRouterWpsUUID':arrisRouterWpsUUID,'arrisRouterWPSMethodCfg':arrisRouterWPSMethodCfg,'arrisRouterWPSMethodLabel':arrisRouterWPSMethodLabel,'arrisRouterWPSMethodPIN':arrisRouterWPSMethodPIN,'arrisRouterWPSMethodPushButton':arrisRouterWPSMethodPushButton,'arrisRouterWPSMethodKeypad':arrisRouterWPSMethodKeypad,'arrisRouterWiFiResetDefaults':arrisRouterWiFiResetDefaults,'arrisRouterWiFiCustomSSIDStr':arrisRouterWiFiCustomSSIDStr,'arrisRouterWiFiRadioControlMode':arrisRouterWiFiRadioControlMode,'arrisRouterWiFiScan':arrisRouterWiFiScan,'arrisRouterWiFiStartScan':arrisRouterWiFiStartScan,'arrisRouterWiFiScanResult':arrisRouterWiFiScanResult,'arrisRouterWiFiScanResultTable':arrisRouterWiFiScanResultTable,'arrisRouterWiFiScanResultEntry':arrisRouterWiFiScanResultEntry,_Ak:arrisRouterWiFiScanIndex,'arrisRouterWiFiScanSSID':arrisRouterWiFiScanSSID,'arrisRouterWiFiScanChannel':arrisRouterWiFiScanChannel,'arrisRouterWiFiScanChannel2':arrisRouterWiFiScanChannel2,'arrisRouterWiFiScanRSSI':arrisRouterWiFiScanRSSI,'arrisRouterWiFiScanNoise':arrisRouterWiFiScanNoise,'arrisRouterWiFiScanMAC':arrisRouterWiFiScanMAC,'arrisRouterWiFiScanMfg':arrisRouterWiFiScanMfg,'arrisRouterWiFiScanSupportedRates':arrisRouterWiFiScanSupportedRates,'arrisRouterWiFiScanOperatingStandards':arrisRouterWiFiScanOperatingStandards,'arrisRouterWiFiScanSecurityModeEnabled':arrisRouterWiFiScanSecurityModeEnabled,'arrisRouterWiFiScanOperatingChannelBandwidth':arrisRouterWiFiScanOperatingChannelBandwidth,'arrisRouterWiFiClientInfoTable':arrisRouterWiFiClientInfoTable,'arrisRouterWiFiClientInfoEntry':arrisRouterWiFiClientInfoEntry,_Al:arrisRouterWiFiClientInfoIndex,'arrisRouterWiFiClientInfoIPAddrType':arrisRouterWiFiClientInfoIPAddrType,'arrisRouterWiFiClientInfoIPAddr':arrisRouterWiFiClientInfoIPAddr,'arrisRouterWiFiClientInfoIPAddrTextual':arrisRouterWiFiClientInfoIPAddrTextual,'arrisRouterWiFiClientInfoHostName':arrisRouterWiFiClientInfoHostName,'arrisRouterWiFiClientInfoMAC':arrisRouterWiFiClientInfoMAC,'arrisRouterWiFiClientInfoMACMfg':arrisRouterWiFiClientInfoMACMfg,'arrisRouterWiFiClientInfoStatus':arrisRouterWiFiClientInfoStatus,'arrisRouterWiFiClientInfoFirstSeen':arrisRouterWiFiClientInfoFirstSeen,'arrisRouterWiFiClientInfoLastSeen':arrisRouterWiFiClientInfoLastSeen,'arrisRouterWiFiClientInfoIdleTime':arrisRouterWiFiClientInfoIdleTime,'arrisRouterWiFiClientInfoInNetworkTime':arrisRouterWiFiClientInfoInNetworkTime,'arrisRouterWiFiClientInfoState':arrisRouterWiFiClientInfoState,'arrisRouterWiFiClientInfoFlags':arrisRouterWiFiClientInfoFlags,'arrisRouterWiFiClientInfoTxPkts':arrisRouterWiFiClientInfoTxPkts,'arrisRouterWiFiClientInfoTxFailures':arrisRouterWiFiClientInfoTxFailures,'arrisRouterWiFiClientInfoRxUnicastPkts':arrisRouterWiFiClientInfoRxUnicastPkts,'arrisRouterWiFiClientInfoRxMulticastPkts':arrisRouterWiFiClientInfoRxMulticastPkts,'arrisRouterWiFiClientInfoLastTxPktRate':arrisRouterWiFiClientInfoLastTxPktRate,'arrisRouterWiFiClientInfoLastRxPktRate':arrisRouterWiFiClientInfoLastRxPktRate,'arrisRouterWiFiClientInfoRateSet':arrisRouterWiFiClientInfoRateSet,'arrisRouterWiFiClientInfoRSSI':arrisRouterWiFiClientInfoRSSI,'arrisRouterWiFiPhysicalChannel':arrisRouterWiFiPhysicalChannel,'arrisRouterWiFi50RadioSettings':arrisRouterWiFi50RadioSettings,'arrisRouterWiFi50Channel':arrisRouterWiFi50Channel,'arrisRouterWiFi50Mode':arrisRouterWiFi50Mode,'arrisRouterWiFi50BeaconInterval':arrisRouterWiFi50BeaconInterval,'arrisRouterWiFi50DTIMInterval':arrisRouterWiFi50DTIMInterval,'arrisRouterWiFi50TxPreamble':arrisRouterWiFi50TxPreamble,'arrisRouterWiFi50RTSThreshold':arrisRouterWiFi50RTSThreshold,'arrisRouterWiFi50FragmentThresh':arrisRouterWiFi50FragmentThresh,'arrisRouterWiFi50ShortSlot':arrisRouterWiFi50ShortSlot,'arrisRouterWiFi50FrameBurst':arrisRouterWiFi50FrameBurst,'arrisRouterWiFi50EnableRadio':arrisRouterWiFi50EnableRadio,'arrisRouterWiFi50ShortRetryLimit':arrisRouterWiFi50ShortRetryLimit,'arrisRouterWiFi50LongRetryLimit':arrisRouterWiFi50LongRetryLimit,'arrisRouterWiFi50OutputPower':arrisRouterWiFi50OutputPower,'arrisRouterWiFi50MulticastA':arrisRouterWiFi50MulticastA,'arrisRouterWiFi50PhysicalChannel':arrisRouterWiFi50PhysicalChannel,'arrisRouterWiFi50NSettings':arrisRouterWiFi50NSettings,'arrisRouterWiFi50HTMCS':arrisRouterWiFi50HTMCS,'arrisRouterWiFi50ChannelBW':arrisRouterWiFi50ChannelBW,'arrisRouterWiFi50NSideBand':arrisRouterWiFi50NSideBand,'arrisRouterWiFi50HTMode':arrisRouterWiFi50HTMode,'arrisRouterWiFi50GuardInterval':arrisRouterWiFi50GuardInterval,'arrisRouterWiFi50AMSDUEnable':arrisRouterWiFi50AMSDUEnable,'arrisRouterWiFi50DeclinePeerBA':arrisRouterWiFi50DeclinePeerBA,'arrisRouterWiFi50BlockAck':arrisRouterWiFi50BlockAck,'arrisRouterWiFi50NProtection':arrisRouterWiFi50NProtection,'arrisRouterWiFi50HTTxStream':arrisRouterWiFi50HTTxStream,'arrisRouterWiFi50HTRxStream':arrisRouterWiFi50HTRxStream,'arrisRouterWiFi50EnableSTBC':arrisRouterWiFi50EnableSTBC,'arrisRouterWiFi50EnableRDG':arrisRouterWiFi50EnableRDG,'arrisRouterWiFi50IGMPSnooping':arrisRouterWiFi50IGMPSnooping,'arrisRouterWiFi50BlockDFSChan':arrisRouterWiFi50BlockDFSChan,'arrisRouterWiFi50RTSRetry':arrisRouterWiFi50RTSRetry,'arrisRouterWiFi50TxRetry':arrisRouterWiFi50TxRetry,'arrisRouterWiFiNumSSIDSupported':arrisRouterWiFiNumSSIDSupported,'arrisRouterWiFiHTTxStream':arrisRouterWiFiHTTxStream,'arrisRouterWiFiHTRxStream':arrisRouterWiFiHTRxStream,'arrisRouterWiFiEnableSTBC':arrisRouterWiFiEnableSTBC,'arrisRouterWiFiEnableRDG':arrisRouterWiFiEnableRDG,'arrisRouterWiFiIGMPSnooping':arrisRouterWiFiIGMPSnooping,'arrisRouterWiFiRTSRetry':arrisRouterWiFiRTSRetry,'arrisRouterWiFiTxRetry':arrisRouterWiFiTxRetry,'arrisRouterWiFiPhysicalChannelStats':arrisRouterWiFiPhysicalChannelStats,'arrisRouterWiFiPhysicalChannelStatsEnable':arrisRouterWiFiPhysicalChannelStatsEnable,'arrisRouterWiFiPhysicalChannelStatsMeasurementRate':arrisRouterWiFiPhysicalChannelStatsMeasurementRate,'arrisRouterWiFiPhysicalChannelStatsMeasurementInterval':arrisRouterWiFiPhysicalChannelStatsMeasurementInterval,'arrisRouterChannelStatsMeasurementTable':arrisRouterChannelStatsMeasurementTable,'arrisRouterChannelStatsMeasurementEntry':arrisRouterChannelStatsMeasurementEntry,'arrisRouterChannelStatsMinNoiseFloor':arrisRouterChannelStatsMinNoiseFloor,'arrisRouterChannelStatsMaxNoiseFloor':arrisRouterChannelStatsMaxNoiseFloor,'arrisRouterChannelStatsMedianNoiseFloor':arrisRouterChannelStatsMedianNoiseFloor,'arrisRouterChannelStatsPacketsSent':arrisRouterChannelStatsPacketsSent,'arrisRouterChannelStatsPacketsReceived':arrisRouterChannelStatsPacketsReceived,'arrisRouterChannelStatsCSTExceedPercent':arrisRouterChannelStatsCSTExceedPercent,'arrisRouterChannelStatsActivityFactor':arrisRouterChannelStatsActivityFactor,'arrisRouterChannelStatsChannelUtilization':arrisRouterChannelStatsChannelUtilization,'arrisRouterChannelStatsRetransmissionsMetric':arrisRouterChannelStatsRetransmissionsMetric,'arrisRouterChannelStatsRSSITable':arrisRouterChannelStatsRSSITable,'arrisRouterChannelStatsRSSITableEntry':arrisRouterChannelStatsRSSITableEntry,_Am:arrisRouterChannelStatsRSSITableIndex,'arrisRouterChannelStatsRSSICount':arrisRouterChannelStatsRSSICount,'arrisRouterWMM50Cfg':arrisRouterWMM50Cfg,'arrisRouterWMM50Enable':arrisRouterWMM50Enable,'arrisRouterWMM50NoAck':arrisRouterWMM50NoAck,'arrisRouterWMM50APSD':arrisRouterWMM50APSD,'arrisRouterWMM50EDCAAPTable':arrisRouterWMM50EDCAAPTable,'arrisRouterWMM50EDCAAPEntry':arrisRouterWMM50EDCAAPEntry,_An:arrisRouterWMM50EDCAAPIndex,'arrisRouterWMM50EDCAAPCWmin':arrisRouterWMM50EDCAAPCWmin,'arrisRouterWMM50EDCAAPCWmax':arrisRouterWMM50EDCAAPCWmax,'arrisRouterWMM50EDCAAPAIFSN':arrisRouterWMM50EDCAAPAIFSN,'arrisRouterWMM50EDCAAPTxOpBLimit':arrisRouterWMM50EDCAAPTxOpBLimit,'arrisRouterWMM50EDCAAPTxOpAGLimit':arrisRouterWMM50EDCAAPTxOpAGLimit,'arrisRouterWMM50EDCAAPAdmitCont':arrisRouterWMM50EDCAAPAdmitCont,'arrisRouterWMM50EDCAAPDiscardOld':arrisRouterWMM50EDCAAPDiscardOld,'arrisRouterWiFiExtensionChannel':arrisRouterWiFiExtensionChannel,'arrisRouterWPS50Cfg':arrisRouterWPS50Cfg,'arrisRouterWps50Mode':arrisRouterWps50Mode,'arrisRouterWps50ConfigState':arrisRouterWps50ConfigState,'arrisRouterWps50DevicePIN':arrisRouterWps50DevicePIN,'arrisRouterWps50DeviceName':arrisRouterWps50DeviceName,'arrisRouterWps50ModelName':arrisRouterWps50ModelName,'arrisRouterWps50Mfg':arrisRouterWps50Mfg,'arrisRouterWps50ResultStatus':arrisRouterWps50ResultStatus,'arrisRouterWps50Status':arrisRouterWps50Status,'arrisRouterWps50ConfigTimeout':arrisRouterWps50ConfigTimeout,'arrisRouterWps50STAPin':arrisRouterWps50STAPin,'arrisRouterWps50PushButton':arrisRouterWps50PushButton,'arrisRouterWps50UUID':arrisRouterWps50UUID,'arrisRouterWifiLowInitRate':arrisRouterWifiLowInitRate,'arrisRouterWiFiBssStaSteering':arrisRouterWiFiBssStaSteering,'arrisRouterWiFiBssStaSteeringReset':arrisRouterWiFiBssStaSteeringReset,'arrisRouterWiFiBssStaSteeringDenyCount':arrisRouterWiFiBssStaSteeringDenyCount,'arrisRouterWiFiBssStaSteeringDenyWindow':arrisRouterWiFiBssStaSteeringDenyWindow,'arrisRouterBssStaSteeringTable':arrisRouterBssStaSteeringTable,'arrisRouterBssStaSteeringEntry':arrisRouterBssStaSteeringEntry,'arrisRouterBssStaSteeringIndex':arrisRouterBssStaSteeringIndex,'arrisRouterBssStaSteeringTableClear':arrisRouterBssStaSteeringTableClear,'arrisRouterBssStaSteeringTableDenyCount':arrisRouterBssStaSteeringTableDenyCount,'arrisRouterBssStaSteeringTableDenyWindow':arrisRouterBssStaSteeringTableDenyWindow,'arrisRouterBssStaSteeringTableStatus':arrisRouterBssStaSteeringTableStatus,'arrisRouterBssStaSteeringClientTable':arrisRouterBssStaSteeringClientTable,'arrisRouterBssStaSteeringClientEntry':arrisRouterBssStaSteeringClientEntry,_Ao:arrisRouterBssStaSteeringClientIndex,'arrisRouterBssStaSteeringClientMacAddress':arrisRouterBssStaSteeringClientMacAddress,'arrisRouterBssStaSteeringClientLastAssocTime':arrisRouterBssStaSteeringClientLastAssocTime,'arrisRouterBssStaSteeringClientOtherBssJoinedCount':arrisRouterBssStaSteeringClientOtherBssJoinedCount,'arrisRouterWiFiInterworkingIE':arrisRouterWiFiInterworkingIE,'arrisRouterAirtimeCtrlCfg':arrisRouterAirtimeCtrlCfg,'arrisRouterAirtimeCtrlBSSIDEnable':arrisRouterAirtimeCtrlBSSIDEnable,'arrisRouterAirtimeCtrlBSSIDWeightTable':arrisRouterAirtimeCtrlBSSIDWeightTable,'arrisRouterAirtimeCtrlBSSIDWeightEntry':arrisRouterAirtimeCtrlBSSIDWeightEntry,'arrisRouterAirtimeCtrlBSSIDWeightGuaranteedPercentage':arrisRouterAirtimeCtrlBSSIDWeightGuaranteedPercentage,'arrisRouterAirtimeCtrlBSSIDWeightMaximumPercentage':arrisRouterAirtimeCtrlBSSIDWeightMaximumPercentage,'arrisRouterFWCfg':arrisRouterFWCfg,'arrisRouterFWEnabled':arrisRouterFWEnabled,'arrisRouterFWEnableDMZ':arrisRouterFWEnableDMZ,'arrisRouterFWIPAddrTypeDMZ':arrisRouterFWIPAddrTypeDMZ,'arrisRouterFWIPAddrDMZ':arrisRouterFWIPAddrDMZ,'arrisRouterFWSecurityLevel':arrisRouterFWSecurityLevel,'arrisRouterFWVirtSrvTable':arrisRouterFWVirtSrvTable,'arrisRouterFWVirtSrvEntry':arrisRouterFWVirtSrvEntry,_Ap:arrisRouterFWVirtSrvIndex,'arrisRouterFWVirtSrvDesc':arrisRouterFWVirtSrvDesc,'arrisRouterFWVirtSrvPortStart':arrisRouterFWVirtSrvPortStart,'arrisRouterFWVirtSrvPortEnd':arrisRouterFWVirtSrvPortEnd,'arrisRouterFWVirtSrvProtoType':arrisRouterFWVirtSrvProtoType,'arrisRouterFWVirtSrvIPAddrType':arrisRouterFWVirtSrvIPAddrType,'arrisRouterFWVirtSrvIPAddr':arrisRouterFWVirtSrvIPAddr,'arrisRouterFWVirtSrvLocalPortStart':arrisRouterFWVirtSrvLocalPortStart,'arrisRouterFWVirtSrvLocalPortEnd':arrisRouterFWVirtSrvLocalPortEnd,'arrisRouterFWVirtSrvRowStatus':arrisRouterFWVirtSrvRowStatus,'arrisRouterFWSrvTr69InstanceID':arrisRouterFWSrvTr69InstanceID,'arrisRouterFWIPFilterTable':arrisRouterFWIPFilterTable,'arrisRouterFWIPFilterEntry':arrisRouterFWIPFilterEntry,_Aq:arrisRouterFWIPFilterIndex,'arrisRouterFWIPFilterDesc':arrisRouterFWIPFilterDesc,'arrisRouterFWIPFilterStartType':arrisRouterFWIPFilterStartType,'arrisRouterFWIPFilterStartAddr':arrisRouterFWIPFilterStartAddr,'arrisRouterFWIPFilterEndType':arrisRouterFWIPFilterEndType,'arrisRouterFWIPFilterEndAddr':arrisRouterFWIPFilterEndAddr,'arrisRouterFWIPFilterPortStart':arrisRouterFWIPFilterPortStart,'arrisRouterFWIPFilterPortEnd':arrisRouterFWIPFilterPortEnd,'arrisRouterFWIPFilterProtoType':arrisRouterFWIPFilterProtoType,'arrisRouterFWIPFilterTOD':arrisRouterFWIPFilterTOD,'arrisRouterFWIPFilterRowStatus':arrisRouterFWIPFilterRowStatus,'arrisRouterFWIPFilterAction':arrisRouterFWIPFilterAction,'arrisRouterFWIPFilterDirection':arrisRouterFWIPFilterDirection,'arrisRouterFWAllowAll':arrisRouterFWAllowAll,'arrisRouterFWMACFilterTable':arrisRouterFWMACFilterTable,'arrisRouterFWMACFilterEntry':arrisRouterFWMACFilterEntry,_Ar:arrisRouterFWMACFilterIndex,'arrisRouterFWMACFilterAddr':arrisRouterFWMACFilterAddr,'arrisRouterFWMACFilterTOD':arrisRouterFWMACFilterTOD,'arrisRouterFWMACFilterRowStatus':arrisRouterFWMACFilterRowStatus,'arrisRouterFWPortTrigTable':arrisRouterFWPortTrigTable,'arrisRouterFWPortTrigEntry':arrisRouterFWPortTrigEntry,_As:arrisRouterFWPortTrigIndex,'arrisRouterFWPortTrigDesc':arrisRouterFWPortTrigDesc,'arrisRouterFWPortTrigPortStart':arrisRouterFWPortTrigPortStart,'arrisRouterFWPortTrigPortEnd':arrisRouterFWPortTrigPortEnd,'arrisRouterFWPortTargPortStart':arrisRouterFWPortTargPortStart,'arrisRouterFWPortTargPortEnd':arrisRouterFWPortTargPortEnd,'arrisRouterFWPortTrigProtoType':arrisRouterFWPortTrigProtoType,'arrisRouterFWPortTrigRowStatus':arrisRouterFWPortTrigRowStatus,'arrisRouterFWFilterRules':arrisRouterFWFilterRules,'arrisRouterFWBlockFragIPPkts':arrisRouterFWBlockFragIPPkts,'arrisRouterFWPortScanProtect':arrisRouterFWPortScanProtect,'arrisRouterFWIPFloodDetect':arrisRouterFWIPFloodDetect,'arrisRouterFWBlockFragIPPktsV4':arrisRouterFWBlockFragIPPktsV4,'arrisRouterFWPortScanProtectV4':arrisRouterFWPortScanProtectV4,'arrisRouterFWIPFloodDetectV4':arrisRouterFWIPFloodDetectV4,'arrisRouterFWBlockFragIPPktsV6':arrisRouterFWBlockFragIPPktsV6,'arrisRouterFWPortScanProtectV6':arrisRouterFWPortScanProtectV6,'arrisRouterFWIPFloodDetectV6':arrisRouterFWIPFloodDetectV6,'arrisRouterFWDDNSObjs':arrisRouterFWDDNSObjs,'arrisRouterFWDDNSEnable':arrisRouterFWDDNSEnable,'arrisRouterFWDDNSType':arrisRouterFWDDNSType,'arrisRouterFWDDNSUserName':arrisRouterFWDDNSUserName,'arrisRouterFWDDNSPassword':arrisRouterFWDDNSPassword,'arrisRouterFWDDNSDomainName':arrisRouterFWDDNSDomainName,'arrisRouterFWDDNSIPAddrType':arrisRouterFWDDNSIPAddrType,'arrisRouterFWDDNSIPAddr':arrisRouterFWDDNSIPAddr,'arrisRouterFWDDNSStatus':arrisRouterFWDDNSStatus,'arrisRouterFWFeatures':arrisRouterFWFeatures,'arrisRouterFWIPSecPassThru':arrisRouterFWIPSecPassThru,'arrisRouterFWPPTPPassThru':arrisRouterFWPPTPPassThru,'arrisRouterFWEnableMulticast':arrisRouterFWEnableMulticast,'arrisRouterFWEnableRemoteMgmt':arrisRouterFWEnableRemoteMgmt,'arrisRouterFWL2TPPassThru':arrisRouterFWL2TPPassThru,'arrisRouterFWRemoteMgmt':arrisRouterFWRemoteMgmt,'arrisRouterFWRemoteMgmtHttp':arrisRouterFWRemoteMgmtHttp,'arrisRouterFWRemoteMgmtHttps':arrisRouterFWRemoteMgmtHttps,'arrisRouterFWRemoteMgmtHttpPort':arrisRouterFWRemoteMgmtHttpPort,'arrisRouterFWRemoteMgmtHttpsPort':arrisRouterFWRemoteMgmtHttpsPort,'arrisRouterFWRemoteMgmtAllowedType':arrisRouterFWRemoteMgmtAllowedType,'arrisRouterFWRemoteMgmtAllowedIPv4':arrisRouterFWRemoteMgmtAllowedIPv4,'arrisRouterFWRemoteMgmtAllowedIPv6':arrisRouterFWRemoteMgmtAllowedIPv6,'arrisRouterFWRemoteMgmtAllowedStartIPv4':arrisRouterFWRemoteMgmtAllowedStartIPv4,'arrisRouterFWRemoteMgmtAllowedEndIPv4':arrisRouterFWRemoteMgmtAllowedEndIPv4,'arrisRouterFWRemoteMgmtAllowedStartIPv6':arrisRouterFWRemoteMgmtAllowedStartIPv6,'arrisRouterFWRemoteMgmtAllowedEndIPv6':arrisRouterFWRemoteMgmtAllowedEndIPv6,'arrisRouterFWRemoteMgmtTelnet':arrisRouterFWRemoteMgmtTelnet,'arrisRouterFWSelectRemoteMgmt':arrisRouterFWSelectRemoteMgmt,'arrisRouterFWParentalControls':arrisRouterFWParentalControls,'arrisRouterKeywordCount':arrisRouterKeywordCount,'arrisRouterBlackListCount':arrisRouterBlackListCount,'arrisRouterWhiteListCount':arrisRouterWhiteListCount,'arrisRouterKeywordBlkTable':arrisRouterKeywordBlkTable,'arrisRouterKeywordBlkEntry':arrisRouterKeywordBlkEntry,_At:arrisRouterKeywordBlkIndex,'arrisRouterKeywordBlkWord':arrisRouterKeywordBlkWord,'arrisRouterKeywordBlkTOD':arrisRouterKeywordBlkTOD,'arrisRouterKeywordBlkStatus':arrisRouterKeywordBlkStatus,'arrisRouterBlackListTable':arrisRouterBlackListTable,'arrisRouterBlackListEntry':arrisRouterBlackListEntry,_Au:arrisRouterBlackListIndex,'arrisRouterBlackListDomain':arrisRouterBlackListDomain,'arrisRouterBlackListTOD':arrisRouterBlackListTOD,'arrisRouterBlackListStatus':arrisRouterBlackListStatus,'arrisRouterWhiteListTable':arrisRouterWhiteListTable,'arrisRouterWhiteListEntry':arrisRouterWhiteListEntry,_Av:arrisRouterWhiteListIndex,'arrisRouterWhiteListDomain':arrisRouterWhiteListDomain,'arrisRouterWhiteListTOD':arrisRouterWhiteListTOD,'arrisRouterWhiteListStatus':arrisRouterWhiteListStatus,'arrisRouterTrustedDeviceTable':arrisRouterTrustedDeviceTable,'arrisRouterTrustedDeviceEntry':arrisRouterTrustedDeviceEntry,_Aw:arrisRouterTrustedDeviceIndex,'arrisRouterTrustedDeviceMAC':arrisRouterTrustedDeviceMAC,'arrisRouterTrustedDeviceStatus':arrisRouterTrustedDeviceStatus,'arrisRouterTrustedDeviceName':arrisRouterTrustedDeviceName,'arrisRouterTrustedDeviceAddrType':arrisRouterTrustedDeviceAddrType,'arrisRouterTrustedDeviceAddr':arrisRouterTrustedDeviceAddr,'arrisRouterEnableParentalCont':arrisRouterEnableParentalCont,'arrisRouterListActiveType':arrisRouterListActiveType,'arrisRouterExceptionListCount':arrisRouterExceptionListCount,'arrisRouterExceptionListTable':arrisRouterExceptionListTable,'arrisRouterExceptionListEntry':arrisRouterExceptionListEntry,_Ax:arrisRouterExceptionListIndex,'arrisRouterExceptionListDomain':arrisRouterExceptionListDomain,'arrisRouterExceptionListStatus':arrisRouterExceptionListStatus,'arrisRouterFWAllowICMP':arrisRouterFWAllowICMP,'arrisRouterFWVirtSrvTableEnabled':arrisRouterFWVirtSrvTableEnabled,'arrisRouterFWPortTrigTableEnabled':arrisRouterFWPortTrigTableEnabled,'arrisRouterFWIPv6Security':arrisRouterFWIPv6Security,'arrisRouterFWIPv6Enable':arrisRouterFWIPv6Enable,'arrisRouterFWMacBridgingWebPageEnabled':arrisRouterFWMacBridgingWebPageEnabled,'arrisRouterFWMacBridgingFunctionEnabled':arrisRouterFWMacBridgingFunctionEnabled,'arrisRouterFWMacBridgingTable':arrisRouterFWMacBridgingTable,'arrisRouterFWMacBridgingEntry':arrisRouterFWMacBridgingEntry,_Ay:arrisRouterFWMacBridgingIndex,'arrisRouterFWMacBridgingName':arrisRouterFWMacBridgingName,'arrisRouterFWMacBridgingMACAddr':arrisRouterFWMacBridgingMACAddr,'arrisRouterFWMacBridgingRowStatus':arrisRouterFWMacBridgingRowStatus,'arrisRouterFWPortAllowTable':arrisRouterFWPortAllowTable,'arrisRouterFWPortAllowEntry':arrisRouterFWPortAllowEntry,_Az:arrisRouterFWPortAllowIndex,'arrisRouterFWPortAllowInboundPort':arrisRouterFWPortAllowInboundPort,'arrisRouterFWPortAllowRowStatus':arrisRouterFWPortAllowRowStatus,'arrisRouterFWSrvTr69LastInstance':arrisRouterFWSrvTr69LastInstance,'arrisRouterSysCfg':arrisRouterSysCfg,'arrisRouterAdminPassword':arrisRouterAdminPassword,'arrisRouterAdminTimeout':arrisRouterAdminTimeout,'arrisRouterTimeZoneUTCOffset':arrisRouterTimeZoneUTCOffset,'arrisRouterReboot':arrisRouterReboot,'arrisRouterDefaults':arrisRouterDefaults,'arrisRouterLanguage':arrisRouterLanguage,'arrisRouterName':arrisRouterName,'arrisRouterSerialNumber':arrisRouterSerialNumber,'arrisRouterBootCodeVersion':arrisRouterBootCodeVersion,'arrisRouterHardwareVersion':arrisRouterHardwareVersion,'arrisRouterFirmwareVersion':arrisRouterFirmwareVersion,'arrisRouterLogLevel':arrisRouterLogLevel,'arrisRouterCustomSettings':arrisRouterCustomSettings,'arrisRouterCustomID':arrisRouterCustomID,'arrisRouterCurrentTime':arrisRouterCurrentTime,'arrisRouterAuthTable':arrisRouterAuthTable,'arrisRouterAuthEntry':arrisRouterAuthEntry,'arrisRouterAuthIndex':arrisRouterAuthIndex,'arrisRouterAuthUserName':arrisRouterAuthUserName,'arrisRouterAuthPassword':arrisRouterAuthPassword,'arrisRouterAuthType':arrisRouterAuthType,'arrisRouterAuthAccountEnabled':arrisRouterAuthAccountEnabled,'arrisRouterSNTPSettings':arrisRouterSNTPSettings,'arrisRouterEnableSNTP':arrisRouterEnableSNTP,'arrisRouterSNTPServerTable':arrisRouterSNTPServerTable,'arrisRouterSNTPServerEntry':arrisRouterSNTPServerEntry,_A_:arrisRouterSNTPServerIndex,'arrisRouterSNTPServerAddrType':arrisRouterSNTPServerAddrType,'arrisRouterSNTPServerAddr':arrisRouterSNTPServerAddr,'arrisRouterSNTPServerName':arrisRouterSNTPServerName,'arrisRouterSNTPServerStatus':arrisRouterSNTPServerStatus,'arrisRouterEmailSettings':arrisRouterEmailSettings,'arrisRouterEmailServerName':arrisRouterEmailServerName,'arrisRouterEmailServerUser':arrisRouterEmailServerUser,'arrisRouterEmailServerPW':arrisRouterEmailServerPW,'arrisRouterEmailAddress':arrisRouterEmailAddress,'arrisRouterEnableLogEmail':arrisRouterEnableLogEmail,'arrisRouterEmailApplySettings':arrisRouterEmailApplySettings,'arrisRouterEmailSenderAddress':arrisRouterEmailSenderAddress,'arrisRouterEmailSend':arrisRouterEmailSend,'arrisRouterLogSettings':arrisRouterLogSettings,'arrisRouterUserLogs':arrisRouterUserLogs,'arrisRouterFirewallLogTable':arrisRouterFirewallLogTable,'arrisRouterFirewallLogEntry':arrisRouterFirewallLogEntry,_B1:arrisRouterFWLogIndex,'arrisRouterFWLogTime':arrisRouterFWLogTime,'arrisRouterFWLogInfo':arrisRouterFWLogInfo,'arrisRouterParentalContLogTable':arrisRouterParentalContLogTable,'arrisRouterParentalContLogEntry':arrisRouterParentalContLogEntry,_B2:arrisRouterPCLogIndex,'arrisRouterPCLogTime':arrisRouterPCLogTime,'arrisRouterPCLogInfo':arrisRouterPCLogInfo,'arrisRouterPCLogType':arrisRouterPCLogType,'arrisRouterChangeLogTable':arrisRouterChangeLogTable,'arrisRouterChangeLogEntry':arrisRouterChangeLogEntry,_B3:arrisRouterChangeLogIndex,'arrisRouterChangeLogTime':arrisRouterChangeLogTime,'arrisRouterChangeLogInfo':arrisRouterChangeLogInfo,'arrisRouterDebugLogTable':arrisRouterDebugLogTable,'arrisRouterDebugLogEntry':arrisRouterDebugLogEntry,_B4:arrisRouterDebugLogIndex,'arrisRouterDebugLogTime':arrisRouterDebugLogTime,'arrisRouterDebugLogInfo':arrisRouterDebugLogInfo,'arrisRouterFirewallLogExtTable':arrisRouterFirewallLogExtTable,'arrisRouterFirewallLogExtEntry':arrisRouterFirewallLogExtEntry,_B5:arrisRouterFWLogExtIndex,'arrisRouterFWLogLatestEventTime':arrisRouterFWLogLatestEventTime,'arrisRouterFWLogLatestEventInfo':arrisRouterFWLogLatestEventInfo,'arrisRouterFWLogEventCount':arrisRouterFWLogEventCount,'arrisRouterMSOLogs':arrisRouterMSOLogs,'arrisRouterMSOChgLogTable':arrisRouterMSOChgLogTable,'arrisRouterMSOChgLogEntry':arrisRouterMSOChgLogEntry,_B6:arrisRouterMSOChgLogIndex,'arrisRouterMSOChgLogTime':arrisRouterMSOChgLogTime,'arrisRouterMSOChgLogInfo':arrisRouterMSOChgLogInfo,'arrisRouterClearMSOLogs':arrisRouterClearMSOLogs,'arrisRouterClearLogs':arrisRouterClearLogs,'arrisRouterTACACSAddr':arrisRouterTACACSAddr,'arrisRouterTACACSPort':arrisRouterTACACSPort,'arrisRouterTACACSSecretKey':arrisRouterTACACSSecretKey,'arrisRouterXmlProvisioningFile':arrisRouterXmlProvisioningFile,'arrisRouterXmlProvisioningStatus':arrisRouterXmlProvisioningStatus,'arrisRouterInboundTrafficLogEnable':arrisRouterInboundTrafficLogEnable,'arrisRouterInboundTrafficLogTable':arrisRouterInboundTrafficLogTable,'arrisRouterInboundTrafficLogEntry':arrisRouterInboundTrafficLogEntry,_B7:arrisRouterInboundTrafficLogIndex,'arrisRouterInboundTrafficLogData':arrisRouterInboundTrafficLogData,'arrisRouterWirelessBand':arrisRouterWirelessBand,'arrisRouterSaveCurrentConfigFile':arrisRouterSaveCurrentConfigFile,'arrisRouterRestoreCurrentConfigFile':arrisRouterRestoreCurrentConfigFile,'arrisRouterLocalPosixTimeZone':arrisRouterLocalPosixTimeZone,'arrisRouterFirstInstallWizardCompletionStatus':arrisRouterFirstInstallWizardCompletionStatus,'arrisRouterTroubleshooterEnable':arrisRouterTroubleshooterEnable,'arrisRouterCSRActiveTimeout':arrisRouterCSRActiveTimeout,'arrisRouterHostAccess':arrisRouterHostAccess,'arrisRouterWebAccessTable':arrisRouterWebAccessTable,'arrisRouterWebAccessEntry':arrisRouterWebAccessEntry,_B8:arrisRouterWebAccessIndex,'arrisRouterWebAccessPage':arrisRouterWebAccessPage,'arrisRouterWebAccessLevel':arrisRouterWebAccessLevel,'arrisRouterWebAccessRowStatus':arrisRouterWebAccessRowStatus,'arrisRouterWebAccessWANACL':arrisRouterWebAccessWANACL,'arrisRouterPingMgmt':arrisRouterPingMgmt,'arrisRouterPingTargetAddrType':arrisRouterPingTargetAddrType,'arrisRouterPingTargetAddress':arrisRouterPingTargetAddress,'arrisRouterPingNumPkts':arrisRouterPingNumPkts,'arrisRouterPingPktSize':arrisRouterPingPktSize,'arrisRouterPingInterval':arrisRouterPingInterval,'arrisRouterPingTimeout':arrisRouterPingTimeout,'arrisRouterPingVerifyReply':arrisRouterPingVerifyReply,'arrisRouterPingIpStackNumber':arrisRouterPingIpStackNumber,'arrisRouterPingStartStop':arrisRouterPingStartStop,'arrisRouterPingPktsSent':arrisRouterPingPktsSent,'arrisRouterPingRepliesReceived':arrisRouterPingRepliesReceived,'arrisRouterPingRepliesVerified':arrisRouterPingRepliesVerified,'arrisRouterPingOctetsSent':arrisRouterPingOctetsSent,'arrisRouterPingOctetsReceived':arrisRouterPingOctetsReceived,'arrisRouterPingIcmpErrors':arrisRouterPingIcmpErrors,'arrisRouterPingLastIcmpError':arrisRouterPingLastIcmpError,'arrisRouterPingAverageRtt':arrisRouterPingAverageRtt,'arrisRouterPingMinRtt':arrisRouterPingMinRtt,'arrisRouterPingMaxRtt':arrisRouterPingMaxRtt,'arrisRouterPingTargetDNSQueryIPAddrType':arrisRouterPingTargetDNSQueryIPAddrType,'arrisRouterPingLog':arrisRouterPingLog,'arrisRouterTraceRtMgmt':arrisRouterTraceRtMgmt,'arrisRouterTraceRtTargAddrType':arrisRouterTraceRtTargAddrType,'arrisRouterTraceRtTargetAddr':arrisRouterTraceRtTargetAddr,'arrisRouterTraceRtMaxHops':arrisRouterTraceRtMaxHops,'arrisRouterTraceRtDataSize':arrisRouterTraceRtDataSize,'arrisRouterTraceRtResolveHosts':arrisRouterTraceRtResolveHosts,'arrisRouterTraceRtBasePort':arrisRouterTraceRtBasePort,'arrisRouterTraceRtStart':arrisRouterTraceRtStart,'arrisRouterTraceRtLog':arrisRouterTraceRtLog,'arrisRouterTraceRtTimeout':arrisRouterTraceRtTimeout,'arrisRouterTraceRtDiffServ':arrisRouterTraceRtDiffServ,'arrisRouterApplyAllSettings':arrisRouterApplyAllSettings,'arrisRouterICtrl':arrisRouterICtrl,'arrisRouterICtrlPortMapCount':arrisRouterICtrlPortMapCount,'arrisRouterICtrlPortMapTable':arrisRouterICtrlPortMapTable,'arrisRouterICtrlPortMapEntry':arrisRouterICtrlPortMapEntry,_B9:arrisRouterICtrlPortMapIndex,'arrisRouterPortMapDescription':arrisRouterPortMapDescription,'arrisRouterPortMapInternalClientAddrType':arrisRouterPortMapInternalClientAddrType,'arrisRouterPortMapInternalClientAddr':arrisRouterPortMapInternalClientAddr,'arrisRouterPortMapProtocol':arrisRouterPortMapProtocol,'arrisRouterPortMapExternalPort':arrisRouterPortMapExternalPort,'arrisRouterPortMapInternalPort':arrisRouterPortMapInternalPort,'arrisRouterPortMapRowStatus':arrisRouterPortMapRowStatus,'arrisRouterPortMapInternalStartPort':arrisRouterPortMapInternalStartPort,'arrisRouterPortMapInternalEndPort':arrisRouterPortMapInternalEndPort,'arrisRouterPortMapExternalStartPort':arrisRouterPortMapExternalStartPort,'arrisRouterPortMapExternalEndPort':arrisRouterPortMapExternalEndPort,'arrisRouterICtrlGetDeviceSettings':arrisRouterICtrlGetDeviceSettings,'arrisRouterICtrlDeviceSettingsFWversion':arrisRouterICtrlDeviceSettingsFWversion,'arrisRouterICtrlIsDeviceReady':arrisRouterICtrlIsDeviceReady,'arrisRouterICtrlDeviceStatus':arrisRouterICtrlDeviceStatus,'arrisRouterICtrlReboot':arrisRouterICtrlReboot,'arrisRouterICtrlInitiateReboot':arrisRouterICtrlInitiateReboot,'arrisRouterICtrlSetDeviceSettings':arrisRouterICtrlSetDeviceSettings,'arrisRouterICtrlSetDeviceName':arrisRouterICtrlSetDeviceName,'arrisRouterICtrlSetAdminPassword':arrisRouterICtrlSetAdminPassword,'arrisRouterICtrlRouterSettings':arrisRouterICtrlRouterSettings,'arrisRouterICtrlRouterManageRemote':arrisRouterICtrlRouterManageRemote,'arrisRouterICtrlRouterRemotePort':arrisRouterICtrlRouterRemotePort,'arrisRouterICtrlRouterRemoteSSL':arrisRouterICtrlRouterRemoteSSL,'arrisRouterICtrlWLanRadioSettings':arrisRouterICtrlWLanRadioSettings,'arrisRouterICtrlWLanRadioMacAddress':arrisRouterICtrlWLanRadioMacAddress,'arrisRouterICtrlWLanRadioChannelWidth':arrisRouterICtrlWLanRadioChannelWidth,'arrisRouterICtrlSetBridgeConnect':arrisRouterICtrlSetBridgeConnect,'arrisRouterICtrlSetBridgeEthernetPort':arrisRouterICtrlSetBridgeEthernetPort,'arrisRouterICtrlSetBridgeMinutes':arrisRouterICtrlSetBridgeMinutes,'arrisRouterICtrlSetBridgePermanentPort4Enable':arrisRouterICtrlSetBridgePermanentPort4Enable,'arrisRouterICtrlGetWanSettings':arrisRouterICtrlGetWanSettings,'arrisRouterICtrlGetWanType':arrisRouterICtrlGetWanType,'arrisRouterICtrlGetWanMTU':arrisRouterICtrlGetWanMTU,'arrisRouterICtrlGetWanPrefixLen':arrisRouterICtrlGetWanPrefixLen,'arrisRouterICtrlGetWanGatewayAddrType':arrisRouterICtrlGetWanGatewayAddrType,'arrisRouterICtrlGetWanGatewayAddr':arrisRouterICtrlGetWanGatewayAddr,'arrisRouterICtrlGetWanDNSPrimaryAddrType':arrisRouterICtrlGetWanDNSPrimaryAddrType,'arrisRouterICtrlGetWanDNSPrimaryAddr':arrisRouterICtrlGetWanDNSPrimaryAddr,'arrisRouterICtrlGetWanDNSSecondaryAddrType':arrisRouterICtrlGetWanDNSSecondaryAddrType,'arrisRouterICtrlGetWanDNSSecondaryAddr':arrisRouterICtrlGetWanDNSSecondaryAddr,'arrisRouterICtrlGetWanMacAddress':arrisRouterICtrlGetWanMacAddress,'arrisRouterICtrlHNAPServerPort':arrisRouterICtrlHNAPServerPort,'arrisRouterICtrlEnable':arrisRouterICtrlEnable,'arrisRouterICtrlHashingKey':arrisRouterICtrlHashingKey,'arrisRouterICtrlPortMapTableEnabled':arrisRouterICtrlPortMapTableEnabled,'arrisRouterFlapListCfg':arrisRouterFlapListCfg,'arrisRouterFlapListEnable':arrisRouterFlapListEnable,'arrisRouterFlapListWLANInterval':arrisRouterFlapListWLANInterval,'arrisRouterFlapListDHCPInterval':arrisRouterFlapListDHCPInterval,'arrisRouterFlapListReportPeroid':arrisRouterFlapListReportPeroid,'arrisRouterFlapListWLANCount':arrisRouterFlapListWLANCount,'arrisRouterFlapListLANCount':arrisRouterFlapListLANCount,'arrisRouterFlapListReqFreqThreshold':arrisRouterFlapListReqFreqThreshold,'arrisRouterFlapListWLANTable':arrisRouterFlapListWLANTable,'arrisRouterFlapListWLANEntry':arrisRouterFlapListWLANEntry,_BA:arrisRouterFlapListWLANIndex,'arrisRouterFlapListWLANMacAddress':arrisRouterFlapListWLANMacAddress,'arrisRouterFlapListWLANRemoveTime':arrisRouterFlapListWLANRemoveTime,'arrisRouterFlapListWLANFlapTime':arrisRouterFlapListWLANFlapTime,'arrisRouterFlapListLANTable':arrisRouterFlapListLANTable,'arrisRouterFlapListLANEntry':arrisRouterFlapListLANEntry,_BB:arrisRouterFlapListLANIndex,'arrisRouterFlapListLANMacAddress':arrisRouterFlapListLANMacAddress,'arrisRouterFlapListLANRemoveTime':arrisRouterFlapListLANRemoveTime,'arrisRouterFlapListLANFlapTime':arrisRouterFlapListLANFlapTime})