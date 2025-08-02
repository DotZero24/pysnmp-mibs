_AC='ncsCallAgentGroupVer1'
_AB='ncsStatsBasicGroupVer1'
_AA='ncsLinePkgGroupVer1'
_A9='ncsBasicGroupVer1'
_A8='ncsCADhcpSiteSpecificCode'
_A7='ncsCAStaticPort'
_A6='ncsCAStaticHost'
_A5='ncsCASelectConfigSource'
_A4='ncsCAPort'
_A3='ncsCAHost'
_A2='ncsCAConfigSource'
_A1='ncsStatsCumulatedAvgConnectionTime'
_A0='ncsStatsCumulatedTotalNumberOfConnections'
_z='ncsStatsCurrentAvgConnectionTime'
_y='ncsStatsCurrentTotalNumberOfConnections'
_x='ncsStatsCurrentNumberOfActiveConnections'
_w='ncsLinePackageTPartialDuration'
_v='ncsLinePackageTCriticalDuration'
_u='ncsLinePackageSlDuration'
_t='ncsLinePackageRtDuration'
_s='ncsLinePackageRoDuration'
_r='ncsLinePackageRgDuration'
_q='ncsLinePackageRbkDuration'
_p='ncsLinePackageOtDuration'
_o='ncsLinePackageMwiDuration'
_n='ncsLinePackageLDuration'
_m='ncsLinePackageDlDuration'
_l='ncsLinePackageBzDuration'
_k='ncsRetransmissionDisconnectMaxWaitingPeriod'
_j='ncsRetransmissionDisconnectMinWaitingPeriod'
_i='ncsRetransmissionDisconnectInitialWaitingPeriod'
_h='ncsRetransmissionMaxWaitingDelay'
_g='ncsRetransmissionHistoryTimeout'
_f='ncsRetransmissionDisconnectThresholdDnsQuery'
_e='ncsRetransmissionDisconnectThreshold'
_d='ncsRetransmissionSuspicionThresholdDnsQuery'
_c='ncsRetransmissionSuspicionThreshold'
_b='ncsRetransmissionDisconnectTimeout'
_a='ncsRetransmissionMaxPeriod'
_Z='ncsRetransmissionInitialPeriod'
_Y='ncsRetransmissionAlgorithm'
_X='ncsEndpointIdTerm2'
_W='ncsEndpointIdTerm1'
_V='ncsPiggyBackingEnable'
_U='ncsEndpointIdListIncludeNotStarted'
_T='ncsRestartLevel'
_S='ncsDefaultDigitMap'
_R='ncsPort'
_Q='performDnsQuery'
_P='noDnsQuery'
_O='192.168.0.10'
_N='MxIpSelectConfigSource'
_M='MxIpDhcpSiteSpecificCode'
_L='MxIpConfigSource'
_K='ifIndex'
_J='IF-MIB'
_I='MxIpHostName'
_H='MxIpPort'
_G='OctetString'
_F='Integer32'
_E='read-only'
_D='Unsigned32'
_C='read-write'
_B='MX-NCS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_J,_K)
ipAddressConfig,ipAddressStatus,mediatrixIpTelephonySignaling=mibBuilder.importSymbols('MX-SMI','ipAddressConfig','ipAddressStatus','mediatrixIpTelephonySignaling')
MxIpConfigSource,MxIpDhcpSiteSpecificCode,MxIpHostName,MxIpPort,MxIpSelectConfigSource=mibBuilder.importSymbols('MX-TC',_L,_M,_I,_H,_N)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ncsMIB=ModuleIdentity((1,3,6,1,4,1,4935,20,10,1))
if mibBuilder.loadTexts:ncsMIB.setRevisions(('1902-11-18 00:00',))
_IpAddressStatusNcsCallAgent_ObjectIdentity=ObjectIdentity
ipAddressStatusNcsCallAgent=_IpAddressStatusNcsCallAgent_ObjectIdentity((1,3,6,1,4,1,4935,10,1,60))
class _NcsCAConfigSource_Type(MxIpConfigSource):defaultValue=1
_NcsCAConfigSource_Type.__name__=_L
_NcsCAConfigSource_Object=MibScalar
ncsCAConfigSource=_NcsCAConfigSource_Object((1,3,6,1,4,1,4935,10,1,60,1),_NcsCAConfigSource_Type())
ncsCAConfigSource.setMaxAccess(_E)
if mibBuilder.loadTexts:ncsCAConfigSource.setStatus(_A)
class _NcsCAHost_Type(MxIpHostName):defaultValue=OctetString(_O)
_NcsCAHost_Type.__name__=_I
_NcsCAHost_Object=MibScalar
ncsCAHost=_NcsCAHost_Object((1,3,6,1,4,1,4935,10,1,60,2),_NcsCAHost_Type())
ncsCAHost.setMaxAccess(_E)
if mibBuilder.loadTexts:ncsCAHost.setStatus(_A)
class _NcsCAPort_Type(MxIpPort):defaultValue=2727
_NcsCAPort_Type.__name__=_H
_NcsCAPort_Object=MibScalar
ncsCAPort=_NcsCAPort_Object((1,3,6,1,4,1,4935,10,1,60,3),_NcsCAPort_Type())
ncsCAPort.setMaxAccess(_E)
if mibBuilder.loadTexts:ncsCAPort.setStatus(_A)
_IpAddressConfigNcsCallAgent_ObjectIdentity=ObjectIdentity
ipAddressConfigNcsCallAgent=_IpAddressConfigNcsCallAgent_ObjectIdentity((1,3,6,1,4,1,4935,15,1,60))
class _NcsCASelectConfigSource_Type(MxIpSelectConfigSource):defaultValue=1
_NcsCASelectConfigSource_Type.__name__=_N
_NcsCASelectConfigSource_Object=MibScalar
ncsCASelectConfigSource=_NcsCASelectConfigSource_Object((1,3,6,1,4,1,4935,15,1,60,1),_NcsCASelectConfigSource_Type())
ncsCASelectConfigSource.setMaxAccess(_C)
if mibBuilder.loadTexts:ncsCASelectConfigSource.setStatus(_A)
_IpAddressConfigNcsCAStatic_ObjectIdentity=ObjectIdentity
ipAddressConfigNcsCAStatic=_IpAddressConfigNcsCAStatic_ObjectIdentity((1,3,6,1,4,1,4935,15,1,60,6))
class _NcsCAStaticHost_Type(MxIpHostName):defaultValue=OctetString(_O)
_NcsCAStaticHost_Type.__name__=_I
_NcsCAStaticHost_Object=MibScalar
ncsCAStaticHost=_NcsCAStaticHost_Object((1,3,6,1,4,1,4935,15,1,60,6,1),_NcsCAStaticHost_Type())
ncsCAStaticHost.setMaxAccess(_C)
if mibBuilder.loadTexts:ncsCAStaticHost.setStatus(_A)
class _NcsCAStaticPort_Type(MxIpPort):defaultValue=2727
_NcsCAStaticPort_Type.__name__=_H
_NcsCAStaticPort_Object=MibScalar
ncsCAStaticPort=_NcsCAStaticPort_Object((1,3,6,1,4,1,4935,15,1,60,6,2),_NcsCAStaticPort_Type())
ncsCAStaticPort.setMaxAccess(_C)
if mibBuilder.loadTexts:ncsCAStaticPort.setStatus(_A)
_IpAddressConfigNcsCADhcp_ObjectIdentity=ObjectIdentity
ipAddressConfigNcsCADhcp=_IpAddressConfigNcsCADhcp_ObjectIdentity((1,3,6,1,4,1,4935,15,1,60,7))
class _NcsCADhcpSiteSpecificCode_Type(MxIpDhcpSiteSpecificCode):defaultValue=0
_NcsCADhcpSiteSpecificCode_Type.__name__=_M
_NcsCADhcpSiteSpecificCode_Object=MibScalar
ncsCADhcpSiteSpecificCode=_NcsCADhcpSiteSpecificCode_Object((1,3,6,1,4,1,4935,15,1,60,7,1),_NcsCADhcpSiteSpecificCode_Type())
ncsCADhcpSiteSpecificCode.setMaxAccess(_C)
if mibBuilder.loadTexts:ncsCADhcpSiteSpecificCode.setStatus(_A)
_Ncs_ObjectIdentity=ObjectIdentity
ncs=_Ncs_ObjectIdentity((1,3,6,1,4,1,4935,20,10))
if mibBuilder.loadTexts:ncs.setStatus(_A)
_NcsMIBObjects_ObjectIdentity=ObjectIdentity
ncsMIBObjects=_NcsMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,20,10,1,1))
class _NcsPort_Type(MxIpPort):defaultValue=2427
_NcsPort_Type.__name__=_H
_NcsPort_Object=MibScalar
ncsPort=_NcsPort_Object((1,3,6,1,4,1,4935,20,10,1,1,1),_NcsPort_Type())
ncsPort.setMaxAccess(_C)
if mibBuilder.loadTexts:ncsPort.setStatus(_A)
class _NcsDefaultDigitMap_Type(OctetString):defaultValue=OctetString('x.T');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_NcsDefaultDigitMap_Type.__name__=_G
_NcsDefaultDigitMap_Object=MibScalar
ncsDefaultDigitMap=_NcsDefaultDigitMap_Object((1,3,6,1,4,1,4935,20,10,1,1,2),_NcsDefaultDigitMap_Type())
ncsDefaultDigitMap.setMaxAccess(_C)
if mibBuilder.loadTexts:ncsDefaultDigitMap.setStatus(_A)
class _NcsRestartLevel_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('gateway',0),('group',1),('endpoint',2)))
_NcsRestartLevel_Type.__name__=_F
_NcsRestartLevel_Object=MibScalar
ncsRestartLevel=_NcsRestartLevel_Object((1,3,6,1,4,1,4935,20,10,1,1,4),_NcsRestartLevel_Type())
ncsRestartLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:ncsRestartLevel.setStatus(_A)
class _NcsEndpointIdListIncludeNotStarted_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('excludeNotStarted',0),('includeNotStarted',1)))
_NcsEndpointIdListIncludeNotStarted_Type.__name__=_F
_NcsEndpointIdListIncludeNotStarted_Object=MibScalar
ncsEndpointIdListIncludeNotStarted=_NcsEndpointIdListIncludeNotStarted_Object((1,3,6,1,4,1,4935,20,10,1,1,5),_NcsEndpointIdListIncludeNotStarted_Type())
ncsEndpointIdListIncludeNotStarted.setMaxAccess(_C)
if mibBuilder.loadTexts:ncsEndpointIdListIncludeNotStarted.setStatus(_A)
class _NcsPiggyBackingEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disable',0),('enable',1)))
_NcsPiggyBackingEnable_Type.__name__=_F
_NcsPiggyBackingEnable_Object=MibScalar
ncsPiggyBackingEnable=_NcsPiggyBackingEnable_Object((1,3,6,1,4,1,4935,20,10,1,1,6),_NcsPiggyBackingEnable_Type())
ncsPiggyBackingEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:ncsPiggyBackingEnable.setStatus(_A)
_NcsEndpointId_ObjectIdentity=ObjectIdentity
ncsEndpointId=_NcsEndpointId_ObjectIdentity((1,3,6,1,4,1,4935,20,10,1,1,20))
_NcsEndpointIfTable_Object=MibTable
ncsEndpointIfTable=_NcsEndpointIfTable_Object((1,3,6,1,4,1,4935,20,10,1,1,20,10))
if mibBuilder.loadTexts:ncsEndpointIfTable.setStatus(_A)
_NcsEndpointIfEntry_Object=MibTableRow
ncsEndpointIfEntry=_NcsEndpointIfEntry_Object((1,3,6,1,4,1,4935,20,10,1,1,20,10,1))
ncsEndpointIfEntry.setIndexNames((0,_J,_K))
if mibBuilder.loadTexts:ncsEndpointIfEntry.setStatus(_A)
class _NcsEndpointIdTerm1_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_NcsEndpointIdTerm1_Type.__name__=_G
_NcsEndpointIdTerm1_Object=MibTableColumn
ncsEndpointIdTerm1=_NcsEndpointIdTerm1_Object((1,3,6,1,4,1,4935,20,10,1,1,20,10,1,1),_NcsEndpointIdTerm1_Type())
ncsEndpointIdTerm1.setMaxAccess(_C)
if mibBuilder.loadTexts:ncsEndpointIdTerm1.setStatus(_A)
class _NcsEndpointIdTerm2_Type(OctetString):defaultValue=OctetString('aaln');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_NcsEndpointIdTerm2_Type.__name__=_G
_NcsEndpointIdTerm2_Object=MibTableColumn
ncsEndpointIdTerm2=_NcsEndpointIdTerm2_Object((1,3,6,1,4,1,4935,20,10,1,1,20,10,1,2),_NcsEndpointIdTerm2_Type())
ncsEndpointIdTerm2.setMaxAccess(_C)
if mibBuilder.loadTexts:ncsEndpointIdTerm2.setStatus(_A)
_NcsRetransmission_ObjectIdentity=ObjectIdentity
ncsRetransmission=_NcsRetransmission_ObjectIdentity((1,3,6,1,4,1,4935,20,10,1,1,23))
class _NcsRetransmissionAlgorithm_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('static',0),('exponential',1),('exponentialWithJitter',2)))
_NcsRetransmissionAlgorithm_Type.__name__=_F
_NcsRetransmissionAlgorithm_Object=MibScalar
ncsRetransmissionAlgorithm=_NcsRetransmissionAlgorithm_Object((1,3,6,1,4,1,4935,20,10,1,1,23,1),_NcsRetransmissionAlgorithm_Type())
ncsRetransmissionAlgorithm.setMaxAccess(_C)
if mibBuilder.loadTexts:ncsRetransmissionAlgorithm.setStatus(_A)
class _NcsRetransmissionInitialPeriod_Type(Unsigned32):defaultValue=200;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(200,4294967295))
_NcsRetransmissionInitialPeriod_Type.__name__=_D
_NcsRetransmissionInitialPeriod_Object=MibScalar
ncsRetransmissionInitialPeriod=_NcsRetransmissionInitialPeriod_Object((1,3,6,1,4,1,4935,20,10,1,1,23,2),_NcsRetransmissionInitialPeriod_Type())
ncsRetransmissionInitialPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:ncsRetransmissionInitialPeriod.setStatus(_A)
class _NcsRetransmissionMaxPeriod_Type(Unsigned32):defaultValue=30000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(200,4294967295))
_NcsRetransmissionMaxPeriod_Type.__name__=_D
_NcsRetransmissionMaxPeriod_Object=MibScalar
ncsRetransmissionMaxPeriod=_NcsRetransmissionMaxPeriod_Object((1,3,6,1,4,1,4935,20,10,1,1,23,3),_NcsRetransmissionMaxPeriod_Type())
ncsRetransmissionMaxPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:ncsRetransmissionMaxPeriod.setStatus(_A)
class _NcsRetransmissionDisconnectTimeout_Type(Unsigned32):defaultValue=20000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,4294967295))
_NcsRetransmissionDisconnectTimeout_Type.__name__=_D
_NcsRetransmissionDisconnectTimeout_Object=MibScalar
ncsRetransmissionDisconnectTimeout=_NcsRetransmissionDisconnectTimeout_Object((1,3,6,1,4,1,4935,20,10,1,1,23,4),_NcsRetransmissionDisconnectTimeout_Type())
ncsRetransmissionDisconnectTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:ncsRetransmissionDisconnectTimeout.setStatus(_A)
class _NcsRetransmissionSuspicionThreshold_Type(Unsigned32):defaultValue=7;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_NcsRetransmissionSuspicionThreshold_Type.__name__=_D
_NcsRetransmissionSuspicionThreshold_Object=MibScalar
ncsRetransmissionSuspicionThreshold=_NcsRetransmissionSuspicionThreshold_Object((1,3,6,1,4,1,4935,20,10,1,1,23,5),_NcsRetransmissionSuspicionThreshold_Type())
ncsRetransmissionSuspicionThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:ncsRetransmissionSuspicionThreshold.setStatus(_A)
class _NcsRetransmissionSuspicionThresholdDnsQuery_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_P,0),(_Q,1)))
_NcsRetransmissionSuspicionThresholdDnsQuery_Type.__name__=_F
_NcsRetransmissionSuspicionThresholdDnsQuery_Object=MibScalar
ncsRetransmissionSuspicionThresholdDnsQuery=_NcsRetransmissionSuspicionThresholdDnsQuery_Object((1,3,6,1,4,1,4935,20,10,1,1,23,6),_NcsRetransmissionSuspicionThresholdDnsQuery_Type())
ncsRetransmissionSuspicionThresholdDnsQuery.setMaxAccess(_C)
if mibBuilder.loadTexts:ncsRetransmissionSuspicionThresholdDnsQuery.setStatus(_A)
class _NcsRetransmissionDisconnectThreshold_Type(Unsigned32):defaultValue=7;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_NcsRetransmissionDisconnectThreshold_Type.__name__=_D
_NcsRetransmissionDisconnectThreshold_Object=MibScalar
ncsRetransmissionDisconnectThreshold=_NcsRetransmissionDisconnectThreshold_Object((1,3,6,1,4,1,4935,20,10,1,1,23,7),_NcsRetransmissionDisconnectThreshold_Type())
ncsRetransmissionDisconnectThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:ncsRetransmissionDisconnectThreshold.setStatus(_A)
class _NcsRetransmissionDisconnectThresholdDnsQuery_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_P,0),(_Q,1)))
_NcsRetransmissionDisconnectThresholdDnsQuery_Type.__name__=_F
_NcsRetransmissionDisconnectThresholdDnsQuery_Object=MibScalar
ncsRetransmissionDisconnectThresholdDnsQuery=_NcsRetransmissionDisconnectThresholdDnsQuery_Object((1,3,6,1,4,1,4935,20,10,1,1,23,8),_NcsRetransmissionDisconnectThresholdDnsQuery_Type())
ncsRetransmissionDisconnectThresholdDnsQuery.setMaxAccess(_C)
if mibBuilder.loadTexts:ncsRetransmissionDisconnectThresholdDnsQuery.setStatus(_A)
class _NcsRetransmissionHistoryTimeout_Type(Unsigned32):defaultValue=20000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,4294967295))
_NcsRetransmissionHistoryTimeout_Type.__name__=_D
_NcsRetransmissionHistoryTimeout_Object=MibScalar
ncsRetransmissionHistoryTimeout=_NcsRetransmissionHistoryTimeout_Object((1,3,6,1,4,1,4935,20,10,1,1,23,9),_NcsRetransmissionHistoryTimeout_Type())
ncsRetransmissionHistoryTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:ncsRetransmissionHistoryTimeout.setStatus(_A)
class _NcsRetransmissionMaxWaitingDelay_Type(Unsigned32):defaultValue=600000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,4294967295))
_NcsRetransmissionMaxWaitingDelay_Type.__name__=_D
_NcsRetransmissionMaxWaitingDelay_Object=MibScalar
ncsRetransmissionMaxWaitingDelay=_NcsRetransmissionMaxWaitingDelay_Object((1,3,6,1,4,1,4935,20,10,1,1,23,10),_NcsRetransmissionMaxWaitingDelay_Type())
ncsRetransmissionMaxWaitingDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:ncsRetransmissionMaxWaitingDelay.setStatus(_A)
class _NcsRetransmissionDisconnectInitialWaitingPeriod_Type(Unsigned32):defaultValue=15000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,4294967295))
_NcsRetransmissionDisconnectInitialWaitingPeriod_Type.__name__=_D
_NcsRetransmissionDisconnectInitialWaitingPeriod_Object=MibScalar
ncsRetransmissionDisconnectInitialWaitingPeriod=_NcsRetransmissionDisconnectInitialWaitingPeriod_Object((1,3,6,1,4,1,4935,20,10,1,1,23,11),_NcsRetransmissionDisconnectInitialWaitingPeriod_Type())
ncsRetransmissionDisconnectInitialWaitingPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:ncsRetransmissionDisconnectInitialWaitingPeriod.setStatus(_A)
class _NcsRetransmissionDisconnectMinWaitingPeriod_Type(Unsigned32):defaultValue=15000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,4294967295))
_NcsRetransmissionDisconnectMinWaitingPeriod_Type.__name__=_D
_NcsRetransmissionDisconnectMinWaitingPeriod_Object=MibScalar
ncsRetransmissionDisconnectMinWaitingPeriod=_NcsRetransmissionDisconnectMinWaitingPeriod_Object((1,3,6,1,4,1,4935,20,10,1,1,23,12),_NcsRetransmissionDisconnectMinWaitingPeriod_Type())
ncsRetransmissionDisconnectMinWaitingPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:ncsRetransmissionDisconnectMinWaitingPeriod.setStatus(_A)
class _NcsRetransmissionDisconnectMaxWaitingPeriod_Type(Unsigned32):defaultValue=600000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,4294967295))
_NcsRetransmissionDisconnectMaxWaitingPeriod_Type.__name__=_D
_NcsRetransmissionDisconnectMaxWaitingPeriod_Object=MibScalar
ncsRetransmissionDisconnectMaxWaitingPeriod=_NcsRetransmissionDisconnectMaxWaitingPeriod_Object((1,3,6,1,4,1,4935,20,10,1,1,23,13),_NcsRetransmissionDisconnectMaxWaitingPeriod_Type())
ncsRetransmissionDisconnectMaxWaitingPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:ncsRetransmissionDisconnectMaxWaitingPeriod.setStatus(_A)
_NcsLinePackage_ObjectIdentity=ObjectIdentity
ncsLinePackage=_NcsLinePackage_ObjectIdentity((1,3,6,1,4,1,4935,20,10,1,1,30))
class _NcsLinePackageBzDuration_Type(Unsigned32):defaultValue=30000
_NcsLinePackageBzDuration_Type.__name__=_D
_NcsLinePackageBzDuration_Object=MibScalar
ncsLinePackageBzDuration=_NcsLinePackageBzDuration_Object((1,3,6,1,4,1,4935,20,10,1,1,30,4),_NcsLinePackageBzDuration_Type())
ncsLinePackageBzDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:ncsLinePackageBzDuration.setStatus(_A)
class _NcsLinePackageDlDuration_Type(Unsigned32):defaultValue=16000
_NcsLinePackageDlDuration_Type.__name__=_D
_NcsLinePackageDlDuration_Object=MibScalar
ncsLinePackageDlDuration=_NcsLinePackageDlDuration_Object((1,3,6,1,4,1,4935,20,10,1,1,30,8),_NcsLinePackageDlDuration_Type())
ncsLinePackageDlDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:ncsLinePackageDlDuration.setStatus(_A)
class _NcsLinePackageLDuration_Type(Unsigned32):defaultValue=2000
_NcsLinePackageLDuration_Type.__name__=_D
_NcsLinePackageLDuration_Object=MibScalar
ncsLinePackageLDuration=_NcsLinePackageLDuration_Object((1,3,6,1,4,1,4935,20,10,1,1,30,12),_NcsLinePackageLDuration_Type())
ncsLinePackageLDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:ncsLinePackageLDuration.setStatus(_A)
class _NcsLinePackageMwiDuration_Type(Unsigned32):defaultValue=16000
_NcsLinePackageMwiDuration_Type.__name__=_D
_NcsLinePackageMwiDuration_Object=MibScalar
ncsLinePackageMwiDuration=_NcsLinePackageMwiDuration_Object((1,3,6,1,4,1,4935,20,10,1,1,30,16),_NcsLinePackageMwiDuration_Type())
ncsLinePackageMwiDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:ncsLinePackageMwiDuration.setStatus(_A)
class _NcsLinePackageOtDuration_Type(Unsigned32):defaultValue=65535000
_NcsLinePackageOtDuration_Type.__name__=_D
_NcsLinePackageOtDuration_Object=MibScalar
ncsLinePackageOtDuration=_NcsLinePackageOtDuration_Object((1,3,6,1,4,1,4935,20,10,1,1,30,20),_NcsLinePackageOtDuration_Type())
ncsLinePackageOtDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:ncsLinePackageOtDuration.setStatus(_A)
class _NcsLinePackageRbkDuration_Type(Unsigned32):defaultValue=180000
_NcsLinePackageRbkDuration_Type.__name__=_D
_NcsLinePackageRbkDuration_Object=MibScalar
ncsLinePackageRbkDuration=_NcsLinePackageRbkDuration_Object((1,3,6,1,4,1,4935,20,10,1,1,30,24),_NcsLinePackageRbkDuration_Type())
ncsLinePackageRbkDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:ncsLinePackageRbkDuration.setStatus(_A)
class _NcsLinePackageRgDuration_Type(Unsigned32):defaultValue=180000
_NcsLinePackageRgDuration_Type.__name__=_D
_NcsLinePackageRgDuration_Object=MibScalar
ncsLinePackageRgDuration=_NcsLinePackageRgDuration_Object((1,3,6,1,4,1,4935,20,10,1,1,30,28),_NcsLinePackageRgDuration_Type())
ncsLinePackageRgDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:ncsLinePackageRgDuration.setStatus(_A)
class _NcsLinePackageRoDuration_Type(Unsigned32):defaultValue=30000
_NcsLinePackageRoDuration_Type.__name__=_D
_NcsLinePackageRoDuration_Object=MibScalar
ncsLinePackageRoDuration=_NcsLinePackageRoDuration_Object((1,3,6,1,4,1,4935,20,10,1,1,30,32),_NcsLinePackageRoDuration_Type())
ncsLinePackageRoDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:ncsLinePackageRoDuration.setStatus(_A)
class _NcsLinePackageRtDuration_Type(Unsigned32):defaultValue=180000
_NcsLinePackageRtDuration_Type.__name__=_D
_NcsLinePackageRtDuration_Object=MibScalar
ncsLinePackageRtDuration=_NcsLinePackageRtDuration_Object((1,3,6,1,4,1,4935,20,10,1,1,30,36),_NcsLinePackageRtDuration_Type())
ncsLinePackageRtDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:ncsLinePackageRtDuration.setStatus(_A)
class _NcsLinePackageSlDuration_Type(Unsigned32):defaultValue=16000
_NcsLinePackageSlDuration_Type.__name__=_D
_NcsLinePackageSlDuration_Object=MibScalar
ncsLinePackageSlDuration=_NcsLinePackageSlDuration_Object((1,3,6,1,4,1,4935,20,10,1,1,30,40),_NcsLinePackageSlDuration_Type())
ncsLinePackageSlDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:ncsLinePackageSlDuration.setStatus(_A)
class _NcsLinePackageTCriticalDuration_Type(Unsigned32):defaultValue=4000
_NcsLinePackageTCriticalDuration_Type.__name__=_D
_NcsLinePackageTCriticalDuration_Object=MibScalar
ncsLinePackageTCriticalDuration=_NcsLinePackageTCriticalDuration_Object((1,3,6,1,4,1,4935,20,10,1,1,30,44),_NcsLinePackageTCriticalDuration_Type())
ncsLinePackageTCriticalDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:ncsLinePackageTCriticalDuration.setStatus(_A)
class _NcsLinePackageTPartialDuration_Type(Unsigned32):defaultValue=16000
_NcsLinePackageTPartialDuration_Type.__name__=_D
_NcsLinePackageTPartialDuration_Object=MibScalar
ncsLinePackageTPartialDuration=_NcsLinePackageTPartialDuration_Object((1,3,6,1,4,1,4935,20,10,1,1,30,48),_NcsLinePackageTPartialDuration_Type())
ncsLinePackageTPartialDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:ncsLinePackageTPartialDuration.setStatus(_A)
_NcsStats_ObjectIdentity=ObjectIdentity
ncsStats=_NcsStats_ObjectIdentity((1,3,6,1,4,1,4935,20,10,1,1,50))
_NcsStatsCurrentNumberOfActiveConnections_Type=Unsigned32
_NcsStatsCurrentNumberOfActiveConnections_Object=MibScalar
ncsStatsCurrentNumberOfActiveConnections=_NcsStatsCurrentNumberOfActiveConnections_Object((1,3,6,1,4,1,4935,20,10,1,1,50,1),_NcsStatsCurrentNumberOfActiveConnections_Type())
ncsStatsCurrentNumberOfActiveConnections.setMaxAccess(_E)
if mibBuilder.loadTexts:ncsStatsCurrentNumberOfActiveConnections.setStatus(_A)
_NcsStatsCurrentStatistics_ObjectIdentity=ObjectIdentity
ncsStatsCurrentStatistics=_NcsStatsCurrentStatistics_ObjectIdentity((1,3,6,1,4,1,4935,20,10,1,1,50,5))
_NcsStatsCurrentTotalNumberOfConnections_Type=Unsigned32
_NcsStatsCurrentTotalNumberOfConnections_Object=MibScalar
ncsStatsCurrentTotalNumberOfConnections=_NcsStatsCurrentTotalNumberOfConnections_Object((1,3,6,1,4,1,4935,20,10,1,1,50,5,1),_NcsStatsCurrentTotalNumberOfConnections_Type())
ncsStatsCurrentTotalNumberOfConnections.setMaxAccess(_E)
if mibBuilder.loadTexts:ncsStatsCurrentTotalNumberOfConnections.setStatus(_A)
_NcsStatsCurrentAvgConnectionTime_Type=Unsigned32
_NcsStatsCurrentAvgConnectionTime_Object=MibScalar
ncsStatsCurrentAvgConnectionTime=_NcsStatsCurrentAvgConnectionTime_Object((1,3,6,1,4,1,4935,20,10,1,1,50,5,2),_NcsStatsCurrentAvgConnectionTime_Type())
ncsStatsCurrentAvgConnectionTime.setMaxAccess(_E)
if mibBuilder.loadTexts:ncsStatsCurrentAvgConnectionTime.setStatus(_A)
_NcsStatsCumulatedStatistics_ObjectIdentity=ObjectIdentity
ncsStatsCumulatedStatistics=_NcsStatsCumulatedStatistics_ObjectIdentity((1,3,6,1,4,1,4935,20,10,1,1,50,6))
_NcsStatsCumulatedTotalNumberOfConnections_Type=Unsigned32
_NcsStatsCumulatedTotalNumberOfConnections_Object=MibScalar
ncsStatsCumulatedTotalNumberOfConnections=_NcsStatsCumulatedTotalNumberOfConnections_Object((1,3,6,1,4,1,4935,20,10,1,1,50,6,1),_NcsStatsCumulatedTotalNumberOfConnections_Type())
ncsStatsCumulatedTotalNumberOfConnections.setMaxAccess(_E)
if mibBuilder.loadTexts:ncsStatsCumulatedTotalNumberOfConnections.setStatus(_A)
_NcsStatsCumulatedAvgConnectionTime_Type=Unsigned32
_NcsStatsCumulatedAvgConnectionTime_Object=MibScalar
ncsStatsCumulatedAvgConnectionTime=_NcsStatsCumulatedAvgConnectionTime_Object((1,3,6,1,4,1,4935,20,10,1,1,50,6,2),_NcsStatsCumulatedAvgConnectionTime_Type())
ncsStatsCumulatedAvgConnectionTime.setMaxAccess(_E)
if mibBuilder.loadTexts:ncsStatsCumulatedAvgConnectionTime.setStatus(_A)
_NcsConformance_ObjectIdentity=ObjectIdentity
ncsConformance=_NcsConformance_ObjectIdentity((1,3,6,1,4,1,4935,20,10,1,2))
_NcsCompliances_ObjectIdentity=ObjectIdentity
ncsCompliances=_NcsCompliances_ObjectIdentity((1,3,6,1,4,1,4935,20,10,1,2,1))
_NcsGroups_ObjectIdentity=ObjectIdentity
ncsGroups=_NcsGroups_ObjectIdentity((1,3,6,1,4,1,4935,20,10,1,2,2))
ncsBasicGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,20,10,1,2,2,1))
ncsBasicGroupVer1.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k)))
if mibBuilder.loadTexts:ncsBasicGroupVer1.setStatus(_A)
ncsLinePkgGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,20,10,1,2,2,4))
ncsLinePkgGroupVer1.setObjects(*((_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w)))
if mibBuilder.loadTexts:ncsLinePkgGroupVer1.setStatus(_A)
ncsStatsBasicGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,20,10,1,2,2,5))
ncsStatsBasicGroupVer1.setObjects(*((_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1)))
if mibBuilder.loadTexts:ncsStatsBasicGroupVer1.setStatus(_A)
ncsCallAgentGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,20,10,1,2,2,6))
ncsCallAgentGroupVer1.setObjects(*((_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8)))
if mibBuilder.loadTexts:ncsCallAgentGroupVer1.setStatus(_A)
ncsResidentialGatewayBasicComplVer1=ModuleCompliance((1,3,6,1,4,1,4935,20,10,1,2,1,1))
ncsResidentialGatewayBasicComplVer1.setObjects(*((_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC)))
if mibBuilder.loadTexts:ncsResidentialGatewayBasicComplVer1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ipAddressStatusNcsCallAgent':ipAddressStatusNcsCallAgent,_A2:ncsCAConfigSource,_A3:ncsCAHost,_A4:ncsCAPort,'ipAddressConfigNcsCallAgent':ipAddressConfigNcsCallAgent,_A5:ncsCASelectConfigSource,'ipAddressConfigNcsCAStatic':ipAddressConfigNcsCAStatic,_A6:ncsCAStaticHost,_A7:ncsCAStaticPort,'ipAddressConfigNcsCADhcp':ipAddressConfigNcsCADhcp,_A8:ncsCADhcpSiteSpecificCode,'ncs':ncs,'ncsMIB':ncsMIB,'ncsMIBObjects':ncsMIBObjects,_R:ncsPort,_S:ncsDefaultDigitMap,_T:ncsRestartLevel,_U:ncsEndpointIdListIncludeNotStarted,_V:ncsPiggyBackingEnable,'ncsEndpointId':ncsEndpointId,'ncsEndpointIfTable':ncsEndpointIfTable,'ncsEndpointIfEntry':ncsEndpointIfEntry,_W:ncsEndpointIdTerm1,_X:ncsEndpointIdTerm2,'ncsRetransmission':ncsRetransmission,_Y:ncsRetransmissionAlgorithm,_Z:ncsRetransmissionInitialPeriod,_a:ncsRetransmissionMaxPeriod,_b:ncsRetransmissionDisconnectTimeout,_c:ncsRetransmissionSuspicionThreshold,_d:ncsRetransmissionSuspicionThresholdDnsQuery,_e:ncsRetransmissionDisconnectThreshold,_f:ncsRetransmissionDisconnectThresholdDnsQuery,_g:ncsRetransmissionHistoryTimeout,_h:ncsRetransmissionMaxWaitingDelay,_i:ncsRetransmissionDisconnectInitialWaitingPeriod,_j:ncsRetransmissionDisconnectMinWaitingPeriod,_k:ncsRetransmissionDisconnectMaxWaitingPeriod,'ncsLinePackage':ncsLinePackage,_l:ncsLinePackageBzDuration,_m:ncsLinePackageDlDuration,_n:ncsLinePackageLDuration,_o:ncsLinePackageMwiDuration,_p:ncsLinePackageOtDuration,_q:ncsLinePackageRbkDuration,_r:ncsLinePackageRgDuration,_s:ncsLinePackageRoDuration,_t:ncsLinePackageRtDuration,_u:ncsLinePackageSlDuration,_v:ncsLinePackageTCriticalDuration,_w:ncsLinePackageTPartialDuration,'ncsStats':ncsStats,_x:ncsStatsCurrentNumberOfActiveConnections,'ncsStatsCurrentStatistics':ncsStatsCurrentStatistics,_y:ncsStatsCurrentTotalNumberOfConnections,_z:ncsStatsCurrentAvgConnectionTime,'ncsStatsCumulatedStatistics':ncsStatsCumulatedStatistics,_A0:ncsStatsCumulatedTotalNumberOfConnections,_A1:ncsStatsCumulatedAvgConnectionTime,'ncsConformance':ncsConformance,'ncsCompliances':ncsCompliances,'ncsResidentialGatewayBasicComplVer1':ncsResidentialGatewayBasicComplVer1,'ncsGroups':ncsGroups,_A9:ncsBasicGroupVer1,_AA:ncsLinePkgGroupVer1,_AB:ncsStatsBasicGroupVer1,_AC:ncsCallAgentGroupVer1})