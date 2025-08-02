_AP='mgcpFirewallGroupVer1'
_AO='mgcpXPPackageGroupVer1'
_AN='mgcpCallAgentGroupVer1'
_AM='mgcpStatsBasicGroupVer1'
_AL='mgcpLinePkgGroupVer1'
_AK='mgcpDtmfPkgGroupVer1'
_AJ='mgcpGenericPkgGroupVer1'
_AI='mgcpBasicGroupVer1'
_AH='mgcpFwKeepAliveTimeout'
_AG='mgcpFwKeepAliveEnable'
_AF='mgcpXPPackageIrDuration'
_AE='mgcpCADhcpSiteSpecificCode'
_AD='mgcpCAStaticPort'
_AC='mgcpCAStaticHost'
_AB='mgcpCASelectConfigSource'
_AA='mgcpCAPort'
_A9='mgcpCAHost'
_A8='mgcpCAConfigSource'
_A7='mgcpStatsCumulatedAvgConnectionTime'
_A6='mgcpStatsCumulatedTotalNumberOfConnections'
_A5='mgcpStatsCurrentAvgConnectionTime'
_A4='mgcpStatsCurrentTotalNumberOfConnections'
_A3='mgcpStatsCurrentNumberOfActiveConnections'
_A2='mgcpLinePackageWtDuration'
_A1='mgcpLinePackageSlDuration'
_A0='mgcpLinePackageRgDuration'
_z='mgcpLinePackageRoDuration'
_y='mgcpLinePackageOtDuration'
_x='mgcpLinePackageMwiDuration'
_w='mgcpLinePackageDlDuration'
_v='mgcpLinePackageBzDuration'
_u='mgcpDtmfPackageTPartialDuration'
_t='mgcpDtmfPackageTCriticalDuration'
_s='mgcpDtmfPackageLDuration'
_r='mgcpGenericMediaPackageRtDuration'
_q='mgcpGenericMediaPackageRbkDuration'
_p='mgcpRetransmissionDisconnectMaxWaitingPeriod'
_o='mgcpRetransmissionDisconnectMinWaitingPeriod'
_n='mgcpRetransmissionDisconnectInitialWaitingPeriod'
_m='mgcpRetransmissionMaxWaitingDelay'
_l='mgcpRetransmissionHistoryTimeout'
_k='mgcpRetransmissionDisconnectThresholdDnsQuery'
_j='mgcpRetransmissionDisconnectThreshold'
_i='mgcpRetransmissionSuspicionThresholdDnsQuery'
_h='mgcpRetransmissionSuspicionThreshold'
_g='mgcpRetransmissionDisconnectTimeout'
_f='mgcpRetransmissionMaxPeriod'
_e='mgcpRetransmissionInitialPeriod'
_d='mgcpRetransmissionAlgorithm'
_c='mgcpEndpointIdTerm2'
_b='mgcpEndpointIdTerm1'
_a='mgcpAddPtimeIfPresentInLCO'
_Z='mgcpPiggyBackingEnable'
_Y='mgcpEndpointIdListIncludeNotStarted'
_X='mgcpRestartLevel'
_W='mgcpDefaultPackage'
_V='mgcpDefaultDigitMap'
_U='mgcpPort'
_T='performDnsQuery'
_S='noDnsQuery'
_R='192.168.0.10'
_Q='MxIpSelectConfigSource'
_P='MxIpDhcpSiteSpecificCode'
_O='MxIpConfigSource'
_N='MxEnableState'
_M='ifIndex'
_L='IF-MIB'
_K='MxIpHostName'
_J='enable'
_I='disable'
_H='MxIpPort'
_G='OctetString'
_F='read-only'
_E='Integer32'
_D='Unsigned32'
_C='read-write'
_B='MX-MGCP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_L,_M)
ipAddressConfig,ipAddressStatus,mediatrixIpTelephonySignaling=mibBuilder.importSymbols('MX-SMI','ipAddressConfig','ipAddressStatus','mediatrixIpTelephonySignaling')
MxEnableState,MxIpConfigSource,MxIpDhcpSiteSpecificCode,MxIpHostName,MxIpPort,MxIpSelectConfigSource=mibBuilder.importSymbols('MX-TC',_N,_O,_P,_K,_H,_Q)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
mgcpMIB=ModuleIdentity((1,3,6,1,4,1,4935,20,1,1))
if mibBuilder.loadTexts:mgcpMIB.setRevisions(('2008-07-29 00:00','2004-09-21 00:00','2004-07-20 00:00','2002-12-31 00:00','2002-11-18 00:00','2002-07-10 00:00','2002-07-05 00:00','2002-06-26 00:00','2002-05-01 00:00','2002-03-13 00:00','2001-11-23 00:00','2001-08-02 00:00'))
_IpAddressStatusMgcpCallAgent_ObjectIdentity=ObjectIdentity
ipAddressStatusMgcpCallAgent=_IpAddressStatusMgcpCallAgent_ObjectIdentity((1,3,6,1,4,1,4935,10,1,50))
class _MgcpCAConfigSource_Type(MxIpConfigSource):defaultValue=1
_MgcpCAConfigSource_Type.__name__=_O
_MgcpCAConfigSource_Object=MibScalar
mgcpCAConfigSource=_MgcpCAConfigSource_Object((1,3,6,1,4,1,4935,10,1,50,1),_MgcpCAConfigSource_Type())
mgcpCAConfigSource.setMaxAccess(_F)
if mibBuilder.loadTexts:mgcpCAConfigSource.setStatus(_A)
class _MgcpCAHost_Type(MxIpHostName):defaultValue=OctetString(_R)
_MgcpCAHost_Type.__name__=_K
_MgcpCAHost_Object=MibScalar
mgcpCAHost=_MgcpCAHost_Object((1,3,6,1,4,1,4935,10,1,50,2),_MgcpCAHost_Type())
mgcpCAHost.setMaxAccess(_F)
if mibBuilder.loadTexts:mgcpCAHost.setStatus(_A)
class _MgcpCAPort_Type(MxIpPort):defaultValue=2727
_MgcpCAPort_Type.__name__=_H
_MgcpCAPort_Object=MibScalar
mgcpCAPort=_MgcpCAPort_Object((1,3,6,1,4,1,4935,10,1,50,3),_MgcpCAPort_Type())
mgcpCAPort.setMaxAccess(_F)
if mibBuilder.loadTexts:mgcpCAPort.setStatus(_A)
_IpAddressConfigMgcpCallAgent_ObjectIdentity=ObjectIdentity
ipAddressConfigMgcpCallAgent=_IpAddressConfigMgcpCallAgent_ObjectIdentity((1,3,6,1,4,1,4935,15,1,50))
class _MgcpCASelectConfigSource_Type(MxIpSelectConfigSource):defaultValue=1
_MgcpCASelectConfigSource_Type.__name__=_Q
_MgcpCASelectConfigSource_Object=MibScalar
mgcpCASelectConfigSource=_MgcpCASelectConfigSource_Object((1,3,6,1,4,1,4935,15,1,50,1),_MgcpCASelectConfigSource_Type())
mgcpCASelectConfigSource.setMaxAccess(_C)
if mibBuilder.loadTexts:mgcpCASelectConfigSource.setStatus(_A)
_IpAddressConfigMgcpCAStatic_ObjectIdentity=ObjectIdentity
ipAddressConfigMgcpCAStatic=_IpAddressConfigMgcpCAStatic_ObjectIdentity((1,3,6,1,4,1,4935,15,1,50,6))
class _MgcpCAStaticHost_Type(MxIpHostName):defaultValue=OctetString(_R)
_MgcpCAStaticHost_Type.__name__=_K
_MgcpCAStaticHost_Object=MibScalar
mgcpCAStaticHost=_MgcpCAStaticHost_Object((1,3,6,1,4,1,4935,15,1,50,6,1),_MgcpCAStaticHost_Type())
mgcpCAStaticHost.setMaxAccess(_C)
if mibBuilder.loadTexts:mgcpCAStaticHost.setStatus(_A)
class _MgcpCAStaticPort_Type(MxIpPort):defaultValue=2727
_MgcpCAStaticPort_Type.__name__=_H
_MgcpCAStaticPort_Object=MibScalar
mgcpCAStaticPort=_MgcpCAStaticPort_Object((1,3,6,1,4,1,4935,15,1,50,6,2),_MgcpCAStaticPort_Type())
mgcpCAStaticPort.setMaxAccess(_C)
if mibBuilder.loadTexts:mgcpCAStaticPort.setStatus(_A)
_IpAddressConfigMgcpCADhcp_ObjectIdentity=ObjectIdentity
ipAddressConfigMgcpCADhcp=_IpAddressConfigMgcpCADhcp_ObjectIdentity((1,3,6,1,4,1,4935,15,1,50,7))
class _MgcpCADhcpSiteSpecificCode_Type(MxIpDhcpSiteSpecificCode):defaultValue=0
_MgcpCADhcpSiteSpecificCode_Type.__name__=_P
_MgcpCADhcpSiteSpecificCode_Object=MibScalar
mgcpCADhcpSiteSpecificCode=_MgcpCADhcpSiteSpecificCode_Object((1,3,6,1,4,1,4935,15,1,50,7,1),_MgcpCADhcpSiteSpecificCode_Type())
mgcpCADhcpSiteSpecificCode.setMaxAccess(_C)
if mibBuilder.loadTexts:mgcpCADhcpSiteSpecificCode.setStatus(_A)
_Mgcp_ObjectIdentity=ObjectIdentity
mgcp=_Mgcp_ObjectIdentity((1,3,6,1,4,1,4935,20,1))
if mibBuilder.loadTexts:mgcp.setStatus(_A)
_MgcpMIBObjects_ObjectIdentity=ObjectIdentity
mgcpMIBObjects=_MgcpMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,20,1,1,1))
class _MgcpPort_Type(MxIpPort):defaultValue=2427
_MgcpPort_Type.__name__=_H
_MgcpPort_Object=MibScalar
mgcpPort=_MgcpPort_Object((1,3,6,1,4,1,4935,20,1,1,1,1),_MgcpPort_Type())
mgcpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:mgcpPort.setStatus(_A)
class _MgcpDefaultDigitMap_Type(OctetString):defaultValue=OctetString('x.T');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_MgcpDefaultDigitMap_Type.__name__=_G
_MgcpDefaultDigitMap_Object=MibScalar
mgcpDefaultDigitMap=_MgcpDefaultDigitMap_Object((1,3,6,1,4,1,4935,20,1,1,1,2),_MgcpDefaultDigitMap_Type())
mgcpDefaultDigitMap.setMaxAccess(_C)
if mibBuilder.loadTexts:mgcpDefaultDigitMap.setStatus(_A)
class _MgcpDefaultPackage_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('linePackage',0),('dtmfPackage',1),('genericPackage',2)))
_MgcpDefaultPackage_Type.__name__=_E
_MgcpDefaultPackage_Object=MibScalar
mgcpDefaultPackage=_MgcpDefaultPackage_Object((1,3,6,1,4,1,4935,20,1,1,1,3),_MgcpDefaultPackage_Type())
mgcpDefaultPackage.setMaxAccess(_C)
if mibBuilder.loadTexts:mgcpDefaultPackage.setStatus(_A)
class _MgcpRestartLevel_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('gateway',0),('group',1),('endpoint',2)))
_MgcpRestartLevel_Type.__name__=_E
_MgcpRestartLevel_Object=MibScalar
mgcpRestartLevel=_MgcpRestartLevel_Object((1,3,6,1,4,1,4935,20,1,1,1,4),_MgcpRestartLevel_Type())
mgcpRestartLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:mgcpRestartLevel.setStatus(_A)
class _MgcpEndpointIdListIncludeNotStarted_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('excludeNotStarted',0),('includeNotStarted',1)))
_MgcpEndpointIdListIncludeNotStarted_Type.__name__=_E
_MgcpEndpointIdListIncludeNotStarted_Object=MibScalar
mgcpEndpointIdListIncludeNotStarted=_MgcpEndpointIdListIncludeNotStarted_Object((1,3,6,1,4,1,4935,20,1,1,1,5),_MgcpEndpointIdListIncludeNotStarted_Type())
mgcpEndpointIdListIncludeNotStarted.setMaxAccess(_C)
if mibBuilder.loadTexts:mgcpEndpointIdListIncludeNotStarted.setStatus(_A)
class _MgcpPiggyBackingEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_MgcpPiggyBackingEnable_Type.__name__=_E
_MgcpPiggyBackingEnable_Object=MibScalar
mgcpPiggyBackingEnable=_MgcpPiggyBackingEnable_Object((1,3,6,1,4,1,4935,20,1,1,1,6),_MgcpPiggyBackingEnable_Type())
mgcpPiggyBackingEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:mgcpPiggyBackingEnable.setStatus(_A)
class _MgcpAddPtimeIfPresentInLCO_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('excludePtime',0),('includePtime',1)))
_MgcpAddPtimeIfPresentInLCO_Type.__name__=_E
_MgcpAddPtimeIfPresentInLCO_Object=MibScalar
mgcpAddPtimeIfPresentInLCO=_MgcpAddPtimeIfPresentInLCO_Object((1,3,6,1,4,1,4935,20,1,1,1,10),_MgcpAddPtimeIfPresentInLCO_Type())
mgcpAddPtimeIfPresentInLCO.setMaxAccess(_C)
if mibBuilder.loadTexts:mgcpAddPtimeIfPresentInLCO.setStatus(_A)
_MgcpEndpointId_ObjectIdentity=ObjectIdentity
mgcpEndpointId=_MgcpEndpointId_ObjectIdentity((1,3,6,1,4,1,4935,20,1,1,1,17))
_MgcpEndpointIfTable_Object=MibTable
mgcpEndpointIfTable=_MgcpEndpointIfTable_Object((1,3,6,1,4,1,4935,20,1,1,1,17,10))
if mibBuilder.loadTexts:mgcpEndpointIfTable.setStatus(_A)
_MgcpEndpointIfEntry_Object=MibTableRow
mgcpEndpointIfEntry=_MgcpEndpointIfEntry_Object((1,3,6,1,4,1,4935,20,1,1,1,17,10,1))
mgcpEndpointIfEntry.setIndexNames((0,_L,_M))
if mibBuilder.loadTexts:mgcpEndpointIfEntry.setStatus(_A)
class _MgcpEndpointIdTerm1_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_MgcpEndpointIdTerm1_Type.__name__=_G
_MgcpEndpointIdTerm1_Object=MibTableColumn
mgcpEndpointIdTerm1=_MgcpEndpointIdTerm1_Object((1,3,6,1,4,1,4935,20,1,1,1,17,10,1,1),_MgcpEndpointIdTerm1_Type())
mgcpEndpointIdTerm1.setMaxAccess(_C)
if mibBuilder.loadTexts:mgcpEndpointIdTerm1.setStatus(_A)
class _MgcpEndpointIdTerm2_Type(OctetString):defaultValue=OctetString('aaln');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_MgcpEndpointIdTerm2_Type.__name__=_G
_MgcpEndpointIdTerm2_Object=MibTableColumn
mgcpEndpointIdTerm2=_MgcpEndpointIdTerm2_Object((1,3,6,1,4,1,4935,20,1,1,1,17,10,1,2),_MgcpEndpointIdTerm2_Type())
mgcpEndpointIdTerm2.setMaxAccess(_C)
if mibBuilder.loadTexts:mgcpEndpointIdTerm2.setStatus(_A)
_MgcpRetransmission_ObjectIdentity=ObjectIdentity
mgcpRetransmission=_MgcpRetransmission_ObjectIdentity((1,3,6,1,4,1,4935,20,1,1,1,18))
class _MgcpRetransmissionAlgorithm_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('static',0),('exponential',1),('exponentialWithJitter',2)))
_MgcpRetransmissionAlgorithm_Type.__name__=_E
_MgcpRetransmissionAlgorithm_Object=MibScalar
mgcpRetransmissionAlgorithm=_MgcpRetransmissionAlgorithm_Object((1,3,6,1,4,1,4935,20,1,1,1,18,1),_MgcpRetransmissionAlgorithm_Type())
mgcpRetransmissionAlgorithm.setMaxAccess(_C)
if mibBuilder.loadTexts:mgcpRetransmissionAlgorithm.setStatus(_A)
class _MgcpRetransmissionInitialPeriod_Type(Unsigned32):defaultValue=200;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(200,4294967295))
_MgcpRetransmissionInitialPeriod_Type.__name__=_D
_MgcpRetransmissionInitialPeriod_Object=MibScalar
mgcpRetransmissionInitialPeriod=_MgcpRetransmissionInitialPeriod_Object((1,3,6,1,4,1,4935,20,1,1,1,18,2),_MgcpRetransmissionInitialPeriod_Type())
mgcpRetransmissionInitialPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:mgcpRetransmissionInitialPeriod.setStatus(_A)
class _MgcpRetransmissionMaxPeriod_Type(Unsigned32):defaultValue=30000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(200,4294967295))
_MgcpRetransmissionMaxPeriod_Type.__name__=_D
_MgcpRetransmissionMaxPeriod_Object=MibScalar
mgcpRetransmissionMaxPeriod=_MgcpRetransmissionMaxPeriod_Object((1,3,6,1,4,1,4935,20,1,1,1,18,3),_MgcpRetransmissionMaxPeriod_Type())
mgcpRetransmissionMaxPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:mgcpRetransmissionMaxPeriod.setStatus(_A)
class _MgcpRetransmissionDisconnectTimeout_Type(Unsigned32):defaultValue=20000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,4294967295))
_MgcpRetransmissionDisconnectTimeout_Type.__name__=_D
_MgcpRetransmissionDisconnectTimeout_Object=MibScalar
mgcpRetransmissionDisconnectTimeout=_MgcpRetransmissionDisconnectTimeout_Object((1,3,6,1,4,1,4935,20,1,1,1,18,4),_MgcpRetransmissionDisconnectTimeout_Type())
mgcpRetransmissionDisconnectTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:mgcpRetransmissionDisconnectTimeout.setStatus(_A)
class _MgcpRetransmissionSuspicionThreshold_Type(Unsigned32):defaultValue=7;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_MgcpRetransmissionSuspicionThreshold_Type.__name__=_D
_MgcpRetransmissionSuspicionThreshold_Object=MibScalar
mgcpRetransmissionSuspicionThreshold=_MgcpRetransmissionSuspicionThreshold_Object((1,3,6,1,4,1,4935,20,1,1,1,18,5),_MgcpRetransmissionSuspicionThreshold_Type())
mgcpRetransmissionSuspicionThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:mgcpRetransmissionSuspicionThreshold.setStatus(_A)
class _MgcpRetransmissionSuspicionThresholdDnsQuery_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_S,0),(_T,1)))
_MgcpRetransmissionSuspicionThresholdDnsQuery_Type.__name__=_E
_MgcpRetransmissionSuspicionThresholdDnsQuery_Object=MibScalar
mgcpRetransmissionSuspicionThresholdDnsQuery=_MgcpRetransmissionSuspicionThresholdDnsQuery_Object((1,3,6,1,4,1,4935,20,1,1,1,18,6),_MgcpRetransmissionSuspicionThresholdDnsQuery_Type())
mgcpRetransmissionSuspicionThresholdDnsQuery.setMaxAccess(_C)
if mibBuilder.loadTexts:mgcpRetransmissionSuspicionThresholdDnsQuery.setStatus(_A)
class _MgcpRetransmissionDisconnectThreshold_Type(Unsigned32):defaultValue=7;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_MgcpRetransmissionDisconnectThreshold_Type.__name__=_D
_MgcpRetransmissionDisconnectThreshold_Object=MibScalar
mgcpRetransmissionDisconnectThreshold=_MgcpRetransmissionDisconnectThreshold_Object((1,3,6,1,4,1,4935,20,1,1,1,18,7),_MgcpRetransmissionDisconnectThreshold_Type())
mgcpRetransmissionDisconnectThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:mgcpRetransmissionDisconnectThreshold.setStatus(_A)
class _MgcpRetransmissionDisconnectThresholdDnsQuery_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_S,0),(_T,1)))
_MgcpRetransmissionDisconnectThresholdDnsQuery_Type.__name__=_E
_MgcpRetransmissionDisconnectThresholdDnsQuery_Object=MibScalar
mgcpRetransmissionDisconnectThresholdDnsQuery=_MgcpRetransmissionDisconnectThresholdDnsQuery_Object((1,3,6,1,4,1,4935,20,1,1,1,18,8),_MgcpRetransmissionDisconnectThresholdDnsQuery_Type())
mgcpRetransmissionDisconnectThresholdDnsQuery.setMaxAccess(_C)
if mibBuilder.loadTexts:mgcpRetransmissionDisconnectThresholdDnsQuery.setStatus(_A)
class _MgcpRetransmissionHistoryTimeout_Type(Unsigned32):defaultValue=20000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,4294967295))
_MgcpRetransmissionHistoryTimeout_Type.__name__=_D
_MgcpRetransmissionHistoryTimeout_Object=MibScalar
mgcpRetransmissionHistoryTimeout=_MgcpRetransmissionHistoryTimeout_Object((1,3,6,1,4,1,4935,20,1,1,1,18,9),_MgcpRetransmissionHistoryTimeout_Type())
mgcpRetransmissionHistoryTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:mgcpRetransmissionHistoryTimeout.setStatus(_A)
class _MgcpRetransmissionMaxWaitingDelay_Type(Unsigned32):defaultValue=600000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,4294967295))
_MgcpRetransmissionMaxWaitingDelay_Type.__name__=_D
_MgcpRetransmissionMaxWaitingDelay_Object=MibScalar
mgcpRetransmissionMaxWaitingDelay=_MgcpRetransmissionMaxWaitingDelay_Object((1,3,6,1,4,1,4935,20,1,1,1,18,10),_MgcpRetransmissionMaxWaitingDelay_Type())
mgcpRetransmissionMaxWaitingDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:mgcpRetransmissionMaxWaitingDelay.setStatus(_A)
class _MgcpRetransmissionDisconnectInitialWaitingPeriod_Type(Unsigned32):defaultValue=15000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,4294967295))
_MgcpRetransmissionDisconnectInitialWaitingPeriod_Type.__name__=_D
_MgcpRetransmissionDisconnectInitialWaitingPeriod_Object=MibScalar
mgcpRetransmissionDisconnectInitialWaitingPeriod=_MgcpRetransmissionDisconnectInitialWaitingPeriod_Object((1,3,6,1,4,1,4935,20,1,1,1,18,11),_MgcpRetransmissionDisconnectInitialWaitingPeriod_Type())
mgcpRetransmissionDisconnectInitialWaitingPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:mgcpRetransmissionDisconnectInitialWaitingPeriod.setStatus(_A)
class _MgcpRetransmissionDisconnectMinWaitingPeriod_Type(Unsigned32):defaultValue=15000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,4294967295))
_MgcpRetransmissionDisconnectMinWaitingPeriod_Type.__name__=_D
_MgcpRetransmissionDisconnectMinWaitingPeriod_Object=MibScalar
mgcpRetransmissionDisconnectMinWaitingPeriod=_MgcpRetransmissionDisconnectMinWaitingPeriod_Object((1,3,6,1,4,1,4935,20,1,1,1,18,12),_MgcpRetransmissionDisconnectMinWaitingPeriod_Type())
mgcpRetransmissionDisconnectMinWaitingPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:mgcpRetransmissionDisconnectMinWaitingPeriod.setStatus(_A)
class _MgcpRetransmissionDisconnectMaxWaitingPeriod_Type(Unsigned32):defaultValue=600000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,4294967295))
_MgcpRetransmissionDisconnectMaxWaitingPeriod_Type.__name__=_D
_MgcpRetransmissionDisconnectMaxWaitingPeriod_Object=MibScalar
mgcpRetransmissionDisconnectMaxWaitingPeriod=_MgcpRetransmissionDisconnectMaxWaitingPeriod_Object((1,3,6,1,4,1,4935,20,1,1,1,18,13),_MgcpRetransmissionDisconnectMaxWaitingPeriod_Type())
mgcpRetransmissionDisconnectMaxWaitingPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:mgcpRetransmissionDisconnectMaxWaitingPeriod.setStatus(_A)
_MgcpDtmfPackage_ObjectIdentity=ObjectIdentity
mgcpDtmfPackage=_MgcpDtmfPackage_ObjectIdentity((1,3,6,1,4,1,4935,20,1,1,1,30))
class _MgcpDtmfPackageLDuration_Type(Unsigned32):defaultValue=2000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_MgcpDtmfPackageLDuration_Type.__name__=_D
_MgcpDtmfPackageLDuration_Object=MibScalar
mgcpDtmfPackageLDuration=_MgcpDtmfPackageLDuration_Object((1,3,6,1,4,1,4935,20,1,1,1,30,4),_MgcpDtmfPackageLDuration_Type())
mgcpDtmfPackageLDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:mgcpDtmfPackageLDuration.setStatus(_A)
class _MgcpDtmfPackageTCriticalDuration_Type(Unsigned32):defaultValue=4000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_MgcpDtmfPackageTCriticalDuration_Type.__name__=_D
_MgcpDtmfPackageTCriticalDuration_Object=MibScalar
mgcpDtmfPackageTCriticalDuration=_MgcpDtmfPackageTCriticalDuration_Object((1,3,6,1,4,1,4935,20,1,1,1,30,8),_MgcpDtmfPackageTCriticalDuration_Type())
mgcpDtmfPackageTCriticalDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:mgcpDtmfPackageTCriticalDuration.setStatus(_A)
class _MgcpDtmfPackageTPartialDuration_Type(Unsigned32):defaultValue=16000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_MgcpDtmfPackageTPartialDuration_Type.__name__=_D
_MgcpDtmfPackageTPartialDuration_Object=MibScalar
mgcpDtmfPackageTPartialDuration=_MgcpDtmfPackageTPartialDuration_Object((1,3,6,1,4,1,4935,20,1,1,1,30,12),_MgcpDtmfPackageTPartialDuration_Type())
mgcpDtmfPackageTPartialDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:mgcpDtmfPackageTPartialDuration.setStatus(_A)
_MgcpGenericMediaPackage_ObjectIdentity=ObjectIdentity
mgcpGenericMediaPackage=_MgcpGenericMediaPackage_ObjectIdentity((1,3,6,1,4,1,4935,20,1,1,1,35))
class _MgcpGenericMediaPackageRbkDuration_Type(Unsigned32):defaultValue=180000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_MgcpGenericMediaPackageRbkDuration_Type.__name__=_D
_MgcpGenericMediaPackageRbkDuration_Object=MibScalar
mgcpGenericMediaPackageRbkDuration=_MgcpGenericMediaPackageRbkDuration_Object((1,3,6,1,4,1,4935,20,1,1,1,35,10),_MgcpGenericMediaPackageRbkDuration_Type())
mgcpGenericMediaPackageRbkDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:mgcpGenericMediaPackageRbkDuration.setStatus(_A)
class _MgcpGenericMediaPackageRtDuration_Type(Unsigned32):defaultValue=180000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_MgcpGenericMediaPackageRtDuration_Type.__name__=_D
_MgcpGenericMediaPackageRtDuration_Object=MibScalar
mgcpGenericMediaPackageRtDuration=_MgcpGenericMediaPackageRtDuration_Object((1,3,6,1,4,1,4935,20,1,1,1,35,14),_MgcpGenericMediaPackageRtDuration_Type())
mgcpGenericMediaPackageRtDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:mgcpGenericMediaPackageRtDuration.setStatus(_A)
_MgcpLinePackage_ObjectIdentity=ObjectIdentity
mgcpLinePackage=_MgcpLinePackage_ObjectIdentity((1,3,6,1,4,1,4935,20,1,1,1,40))
class _MgcpLinePackageBzDuration_Type(Unsigned32):defaultValue=30000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_MgcpLinePackageBzDuration_Type.__name__=_D
_MgcpLinePackageBzDuration_Object=MibScalar
mgcpLinePackageBzDuration=_MgcpLinePackageBzDuration_Object((1,3,6,1,4,1,4935,20,1,1,1,40,4),_MgcpLinePackageBzDuration_Type())
mgcpLinePackageBzDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:mgcpLinePackageBzDuration.setStatus(_A)
class _MgcpLinePackageDlDuration_Type(Unsigned32):defaultValue=16000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_MgcpLinePackageDlDuration_Type.__name__=_D
_MgcpLinePackageDlDuration_Object=MibScalar
mgcpLinePackageDlDuration=_MgcpLinePackageDlDuration_Object((1,3,6,1,4,1,4935,20,1,1,1,40,8),_MgcpLinePackageDlDuration_Type())
mgcpLinePackageDlDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:mgcpLinePackageDlDuration.setStatus(_A)
class _MgcpLinePackageMwiDuration_Type(Unsigned32):defaultValue=16000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_MgcpLinePackageMwiDuration_Type.__name__=_D
_MgcpLinePackageMwiDuration_Object=MibScalar
mgcpLinePackageMwiDuration=_MgcpLinePackageMwiDuration_Object((1,3,6,1,4,1,4935,20,1,1,1,40,12),_MgcpLinePackageMwiDuration_Type())
mgcpLinePackageMwiDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:mgcpLinePackageMwiDuration.setStatus(_A)
class _MgcpLinePackageOtDuration_Type(Unsigned32):defaultValue=65535000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_MgcpLinePackageOtDuration_Type.__name__=_D
_MgcpLinePackageOtDuration_Object=MibScalar
mgcpLinePackageOtDuration=_MgcpLinePackageOtDuration_Object((1,3,6,1,4,1,4935,20,1,1,1,40,16),_MgcpLinePackageOtDuration_Type())
mgcpLinePackageOtDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:mgcpLinePackageOtDuration.setStatus(_A)
class _MgcpLinePackageRgDuration_Type(Unsigned32):defaultValue=180000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_MgcpLinePackageRgDuration_Type.__name__=_D
_MgcpLinePackageRgDuration_Object=MibScalar
mgcpLinePackageRgDuration=_MgcpLinePackageRgDuration_Object((1,3,6,1,4,1,4935,20,1,1,1,40,20),_MgcpLinePackageRgDuration_Type())
mgcpLinePackageRgDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:mgcpLinePackageRgDuration.setStatus(_A)
class _MgcpLinePackageRoDuration_Type(Unsigned32):defaultValue=30000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_MgcpLinePackageRoDuration_Type.__name__=_D
_MgcpLinePackageRoDuration_Object=MibScalar
mgcpLinePackageRoDuration=_MgcpLinePackageRoDuration_Object((1,3,6,1,4,1,4935,20,1,1,1,40,24),_MgcpLinePackageRoDuration_Type())
mgcpLinePackageRoDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:mgcpLinePackageRoDuration.setStatus(_A)
class _MgcpLinePackageSlDuration_Type(Unsigned32):defaultValue=16000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_MgcpLinePackageSlDuration_Type.__name__=_D
_MgcpLinePackageSlDuration_Object=MibScalar
mgcpLinePackageSlDuration=_MgcpLinePackageSlDuration_Object((1,3,6,1,4,1,4935,20,1,1,1,40,28),_MgcpLinePackageSlDuration_Type())
mgcpLinePackageSlDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:mgcpLinePackageSlDuration.setStatus(_A)
class _MgcpLinePackageWtDuration_Type(Unsigned32):defaultValue=30000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_MgcpLinePackageWtDuration_Type.__name__=_D
_MgcpLinePackageWtDuration_Object=MibScalar
mgcpLinePackageWtDuration=_MgcpLinePackageWtDuration_Object((1,3,6,1,4,1,4935,20,1,1,1,40,32),_MgcpLinePackageWtDuration_Type())
mgcpLinePackageWtDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:mgcpLinePackageWtDuration.setStatus(_A)
class _MgcpLinePackageOsiDuration_Type(Unsigned32):defaultValue=900;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_MgcpLinePackageOsiDuration_Type.__name__=_D
_MgcpLinePackageOsiDuration_Object=MibScalar
mgcpLinePackageOsiDuration=_MgcpLinePackageOsiDuration_Object((1,3,6,1,4,1,4935,20,1,1,1,40,36),_MgcpLinePackageOsiDuration_Type())
mgcpLinePackageOsiDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:mgcpLinePackageOsiDuration.setStatus(_A)
class _MgcpLinePackageHdPersistent_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_MgcpLinePackageHdPersistent_Type.__name__=_E
_MgcpLinePackageHdPersistent_Object=MibScalar
mgcpLinePackageHdPersistent=_MgcpLinePackageHdPersistent_Object((1,3,6,1,4,1,4935,20,1,1,1,40,100),_MgcpLinePackageHdPersistent_Type())
mgcpLinePackageHdPersistent.setMaxAccess(_C)
if mibBuilder.loadTexts:mgcpLinePackageHdPersistent.setStatus(_A)
class _MgcpLinePackageHfPersistent_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_MgcpLinePackageHfPersistent_Type.__name__=_E
_MgcpLinePackageHfPersistent_Object=MibScalar
mgcpLinePackageHfPersistent=_MgcpLinePackageHfPersistent_Object((1,3,6,1,4,1,4935,20,1,1,1,40,101),_MgcpLinePackageHfPersistent_Type())
mgcpLinePackageHfPersistent.setMaxAccess(_C)
if mibBuilder.loadTexts:mgcpLinePackageHfPersistent.setStatus(_A)
class _MgcpLinePackageHuPersistent_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_MgcpLinePackageHuPersistent_Type.__name__=_E
_MgcpLinePackageHuPersistent_Object=MibScalar
mgcpLinePackageHuPersistent=_MgcpLinePackageHuPersistent_Object((1,3,6,1,4,1,4935,20,1,1,1,40,102),_MgcpLinePackageHuPersistent_Type())
mgcpLinePackageHuPersistent.setMaxAccess(_C)
if mibBuilder.loadTexts:mgcpLinePackageHuPersistent.setStatus(_A)
_MgcpXPPackage_ObjectIdentity=ObjectIdentity
mgcpXPPackage=_MgcpXPPackage_ObjectIdentity((1,3,6,1,4,1,4935,20,1,1,1,43))
class _MgcpXPPackageIrDuration_Type(Unsigned32):defaultValue=500;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_MgcpXPPackageIrDuration_Type.__name__=_D
_MgcpXPPackageIrDuration_Object=MibScalar
mgcpXPPackageIrDuration=_MgcpXPPackageIrDuration_Object((1,3,6,1,4,1,4935,20,1,1,1,43,4),_MgcpXPPackageIrDuration_Type())
mgcpXPPackageIrDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:mgcpXPPackageIrDuration.setStatus(_A)
_MgcpFirewall_ObjectIdentity=ObjectIdentity
mgcpFirewall=_MgcpFirewall_ObjectIdentity((1,3,6,1,4,1,4935,20,1,1,1,46))
class _MgcpFwKeepAliveEnable_Type(MxEnableState):defaultValue=0
_MgcpFwKeepAliveEnable_Type.__name__=_N
_MgcpFwKeepAliveEnable_Object=MibScalar
mgcpFwKeepAliveEnable=_MgcpFwKeepAliveEnable_Object((1,3,6,1,4,1,4935,20,1,1,1,46,5),_MgcpFwKeepAliveEnable_Type())
mgcpFwKeepAliveEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:mgcpFwKeepAliveEnable.setStatus(_A)
class _MgcpFwKeepAliveTimeout_Type(Unsigned32):defaultValue=300;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,86400))
_MgcpFwKeepAliveTimeout_Type.__name__=_D
_MgcpFwKeepAliveTimeout_Object=MibScalar
mgcpFwKeepAliveTimeout=_MgcpFwKeepAliveTimeout_Object((1,3,6,1,4,1,4935,20,1,1,1,46,10),_MgcpFwKeepAliveTimeout_Type())
mgcpFwKeepAliveTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:mgcpFwKeepAliveTimeout.setStatus(_A)
_MgcpStats_ObjectIdentity=ObjectIdentity
mgcpStats=_MgcpStats_ObjectIdentity((1,3,6,1,4,1,4935,20,1,1,1,50))
_MgcpStatsCurrentNumberOfActiveConnections_Type=Unsigned32
_MgcpStatsCurrentNumberOfActiveConnections_Object=MibScalar
mgcpStatsCurrentNumberOfActiveConnections=_MgcpStatsCurrentNumberOfActiveConnections_Object((1,3,6,1,4,1,4935,20,1,1,1,50,1),_MgcpStatsCurrentNumberOfActiveConnections_Type())
mgcpStatsCurrentNumberOfActiveConnections.setMaxAccess(_F)
if mibBuilder.loadTexts:mgcpStatsCurrentNumberOfActiveConnections.setStatus(_A)
_MgcpStatsCurrentStatistics_ObjectIdentity=ObjectIdentity
mgcpStatsCurrentStatistics=_MgcpStatsCurrentStatistics_ObjectIdentity((1,3,6,1,4,1,4935,20,1,1,1,50,5))
_MgcpStatsCurrentTotalNumberOfConnections_Type=Unsigned32
_MgcpStatsCurrentTotalNumberOfConnections_Object=MibScalar
mgcpStatsCurrentTotalNumberOfConnections=_MgcpStatsCurrentTotalNumberOfConnections_Object((1,3,6,1,4,1,4935,20,1,1,1,50,5,1),_MgcpStatsCurrentTotalNumberOfConnections_Type())
mgcpStatsCurrentTotalNumberOfConnections.setMaxAccess(_F)
if mibBuilder.loadTexts:mgcpStatsCurrentTotalNumberOfConnections.setStatus(_A)
_MgcpStatsCurrentAvgConnectionTime_Type=Unsigned32
_MgcpStatsCurrentAvgConnectionTime_Object=MibScalar
mgcpStatsCurrentAvgConnectionTime=_MgcpStatsCurrentAvgConnectionTime_Object((1,3,6,1,4,1,4935,20,1,1,1,50,5,2),_MgcpStatsCurrentAvgConnectionTime_Type())
mgcpStatsCurrentAvgConnectionTime.setMaxAccess(_F)
if mibBuilder.loadTexts:mgcpStatsCurrentAvgConnectionTime.setStatus(_A)
_MgcpStatsCumulatedStatistics_ObjectIdentity=ObjectIdentity
mgcpStatsCumulatedStatistics=_MgcpStatsCumulatedStatistics_ObjectIdentity((1,3,6,1,4,1,4935,20,1,1,1,50,6))
_MgcpStatsCumulatedTotalNumberOfConnections_Type=Unsigned32
_MgcpStatsCumulatedTotalNumberOfConnections_Object=MibScalar
mgcpStatsCumulatedTotalNumberOfConnections=_MgcpStatsCumulatedTotalNumberOfConnections_Object((1,3,6,1,4,1,4935,20,1,1,1,50,6,1),_MgcpStatsCumulatedTotalNumberOfConnections_Type())
mgcpStatsCumulatedTotalNumberOfConnections.setMaxAccess(_F)
if mibBuilder.loadTexts:mgcpStatsCumulatedTotalNumberOfConnections.setStatus(_A)
_MgcpStatsCumulatedAvgConnectionTime_Type=Unsigned32
_MgcpStatsCumulatedAvgConnectionTime_Object=MibScalar
mgcpStatsCumulatedAvgConnectionTime=_MgcpStatsCumulatedAvgConnectionTime_Object((1,3,6,1,4,1,4935,20,1,1,1,50,6,2),_MgcpStatsCumulatedAvgConnectionTime_Type())
mgcpStatsCumulatedAvgConnectionTime.setMaxAccess(_F)
if mibBuilder.loadTexts:mgcpStatsCumulatedAvgConnectionTime.setStatus(_A)
_MgcpConformance_ObjectIdentity=ObjectIdentity
mgcpConformance=_MgcpConformance_ObjectIdentity((1,3,6,1,4,1,4935,20,1,1,2))
_MgcpCompliances_ObjectIdentity=ObjectIdentity
mgcpCompliances=_MgcpCompliances_ObjectIdentity((1,3,6,1,4,1,4935,20,1,1,2,1))
_MgcpGroups_ObjectIdentity=ObjectIdentity
mgcpGroups=_MgcpGroups_ObjectIdentity((1,3,6,1,4,1,4935,20,1,1,2,2))
mgcpBasicGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,20,1,1,2,2,1))
mgcpBasicGroupVer1.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p)))
if mibBuilder.loadTexts:mgcpBasicGroupVer1.setStatus(_A)
mgcpGenericPkgGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,20,1,1,2,2,2))
mgcpGenericPkgGroupVer1.setObjects(*((_B,_q),(_B,_r)))
if mibBuilder.loadTexts:mgcpGenericPkgGroupVer1.setStatus(_A)
mgcpDtmfPkgGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,20,1,1,2,2,3))
mgcpDtmfPkgGroupVer1.setObjects(*((_B,_s),(_B,_t),(_B,_u)))
if mibBuilder.loadTexts:mgcpDtmfPkgGroupVer1.setStatus(_A)
mgcpLinePkgGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,20,1,1,2,2,4))
mgcpLinePkgGroupVer1.setObjects(*((_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2)))
if mibBuilder.loadTexts:mgcpLinePkgGroupVer1.setStatus(_A)
mgcpStatsBasicGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,20,1,1,2,2,5))
mgcpStatsBasicGroupVer1.setObjects(*((_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7)))
if mibBuilder.loadTexts:mgcpStatsBasicGroupVer1.setStatus(_A)
mgcpCallAgentGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,20,1,1,2,2,6))
mgcpCallAgentGroupVer1.setObjects(*((_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE)))
if mibBuilder.loadTexts:mgcpCallAgentGroupVer1.setStatus(_A)
mgcpXPPackageGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,20,1,1,2,2,15))
mgcpXPPackageGroupVer1.setObjects((_B,_AF))
if mibBuilder.loadTexts:mgcpXPPackageGroupVer1.setStatus(_A)
mgcpFirewallGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,20,1,1,2,2,20))
mgcpFirewallGroupVer1.setObjects(*((_B,_AG),(_B,_AH)))
if mibBuilder.loadTexts:mgcpFirewallGroupVer1.setStatus(_A)
mgcpResidentialGatewayBasicComplVer1=ModuleCompliance((1,3,6,1,4,1,4935,20,1,1,2,1,1))
mgcpResidentialGatewayBasicComplVer1.setObjects(*((_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP)))
if mibBuilder.loadTexts:mgcpResidentialGatewayBasicComplVer1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ipAddressStatusMgcpCallAgent':ipAddressStatusMgcpCallAgent,_A8:mgcpCAConfigSource,_A9:mgcpCAHost,_AA:mgcpCAPort,'ipAddressConfigMgcpCallAgent':ipAddressConfigMgcpCallAgent,_AB:mgcpCASelectConfigSource,'ipAddressConfigMgcpCAStatic':ipAddressConfigMgcpCAStatic,_AC:mgcpCAStaticHost,_AD:mgcpCAStaticPort,'ipAddressConfigMgcpCADhcp':ipAddressConfigMgcpCADhcp,_AE:mgcpCADhcpSiteSpecificCode,'mgcp':mgcp,'mgcpMIB':mgcpMIB,'mgcpMIBObjects':mgcpMIBObjects,_U:mgcpPort,_V:mgcpDefaultDigitMap,_W:mgcpDefaultPackage,_X:mgcpRestartLevel,_Y:mgcpEndpointIdListIncludeNotStarted,_Z:mgcpPiggyBackingEnable,_a:mgcpAddPtimeIfPresentInLCO,'mgcpEndpointId':mgcpEndpointId,'mgcpEndpointIfTable':mgcpEndpointIfTable,'mgcpEndpointIfEntry':mgcpEndpointIfEntry,_b:mgcpEndpointIdTerm1,_c:mgcpEndpointIdTerm2,'mgcpRetransmission':mgcpRetransmission,_d:mgcpRetransmissionAlgorithm,_e:mgcpRetransmissionInitialPeriod,_f:mgcpRetransmissionMaxPeriod,_g:mgcpRetransmissionDisconnectTimeout,_h:mgcpRetransmissionSuspicionThreshold,_i:mgcpRetransmissionSuspicionThresholdDnsQuery,_j:mgcpRetransmissionDisconnectThreshold,_k:mgcpRetransmissionDisconnectThresholdDnsQuery,_l:mgcpRetransmissionHistoryTimeout,_m:mgcpRetransmissionMaxWaitingDelay,_n:mgcpRetransmissionDisconnectInitialWaitingPeriod,_o:mgcpRetransmissionDisconnectMinWaitingPeriod,_p:mgcpRetransmissionDisconnectMaxWaitingPeriod,'mgcpDtmfPackage':mgcpDtmfPackage,_s:mgcpDtmfPackageLDuration,_t:mgcpDtmfPackageTCriticalDuration,_u:mgcpDtmfPackageTPartialDuration,'mgcpGenericMediaPackage':mgcpGenericMediaPackage,_q:mgcpGenericMediaPackageRbkDuration,_r:mgcpGenericMediaPackageRtDuration,'mgcpLinePackage':mgcpLinePackage,_v:mgcpLinePackageBzDuration,_w:mgcpLinePackageDlDuration,_x:mgcpLinePackageMwiDuration,_y:mgcpLinePackageOtDuration,_A0:mgcpLinePackageRgDuration,_z:mgcpLinePackageRoDuration,_A1:mgcpLinePackageSlDuration,_A2:mgcpLinePackageWtDuration,'mgcpLinePackageOsiDuration':mgcpLinePackageOsiDuration,'mgcpLinePackageHdPersistent':mgcpLinePackageHdPersistent,'mgcpLinePackageHfPersistent':mgcpLinePackageHfPersistent,'mgcpLinePackageHuPersistent':mgcpLinePackageHuPersistent,'mgcpXPPackage':mgcpXPPackage,_AF:mgcpXPPackageIrDuration,'mgcpFirewall':mgcpFirewall,_AG:mgcpFwKeepAliveEnable,_AH:mgcpFwKeepAliveTimeout,'mgcpStats':mgcpStats,_A3:mgcpStatsCurrentNumberOfActiveConnections,'mgcpStatsCurrentStatistics':mgcpStatsCurrentStatistics,_A4:mgcpStatsCurrentTotalNumberOfConnections,_A5:mgcpStatsCurrentAvgConnectionTime,'mgcpStatsCumulatedStatistics':mgcpStatsCumulatedStatistics,_A6:mgcpStatsCumulatedTotalNumberOfConnections,_A7:mgcpStatsCumulatedAvgConnectionTime,'mgcpConformance':mgcpConformance,'mgcpCompliances':mgcpCompliances,'mgcpResidentialGatewayBasicComplVer1':mgcpResidentialGatewayBasicComplVer1,'mgcpGroups':mgcpGroups,_AI:mgcpBasicGroupVer1,_AJ:mgcpGenericPkgGroupVer1,_AK:mgcpDtmfPkgGroupVer1,_AL:mgcpLinePkgGroupVer1,_AM:mgcpStatsBasicGroupVer1,_AN:mgcpCallAgentGroupVer1,_AO:mgcpXPPackageGroupVer1,_AP:mgcpFirewallGroupVer1})