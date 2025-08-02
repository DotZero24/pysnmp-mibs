_H='cacheClientAddress'
_G='cachePeerIndex'
_F='cacheMedianTime'
_E='Integer32'
_D='InetAddress'
_C='SQUID-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_D,'InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
squid=ModuleIdentity((1,3,6,1,4,1,3495,1))
if mibBuilder.loadTexts:squid.setRevisions(('2008-12-24 02:00','2007-12-14 00:00','1999-01-01 00:00','1998-09-22 00:00'))
class ValidPort(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
class CachePeerTableIndex(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Nlanr_ObjectIdentity=ObjectIdentity
nlanr=_Nlanr_ObjectIdentity((1,3,6,1,4,1,3495))
_CacheSystem_ObjectIdentity=ObjectIdentity
cacheSystem=_CacheSystem_ObjectIdentity((1,3,6,1,4,1,3495,1,1))
_CacheSysVMsize_Type=Integer32
_CacheSysVMsize_Object=MibScalar
cacheSysVMsize=_CacheSysVMsize_Object((1,3,6,1,4,1,3495,1,1,1),_CacheSysVMsize_Type())
cacheSysVMsize.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheSysVMsize.setStatus(_A)
_CacheSysStorage_Type=Integer32
_CacheSysStorage_Object=MibScalar
cacheSysStorage=_CacheSysStorage_Object((1,3,6,1,4,1,3495,1,1,2),_CacheSysStorage_Type())
cacheSysStorage.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheSysStorage.setStatus(_A)
_CacheUptime_Type=TimeTicks
_CacheUptime_Object=MibScalar
cacheUptime=_CacheUptime_Object((1,3,6,1,4,1,3495,1,1,3),_CacheUptime_Type())
cacheUptime.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheUptime.setStatus(_A)
_CacheConfig_ObjectIdentity=ObjectIdentity
cacheConfig=_CacheConfig_ObjectIdentity((1,3,6,1,4,1,3495,1,2))
_CacheAdmin_Type=DisplayString
_CacheAdmin_Object=MibScalar
cacheAdmin=_CacheAdmin_Object((1,3,6,1,4,1,3495,1,2,1),_CacheAdmin_Type())
cacheAdmin.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheAdmin.setStatus(_A)
_CacheSoftware_Type=DisplayString
_CacheSoftware_Object=MibScalar
cacheSoftware=_CacheSoftware_Object((1,3,6,1,4,1,3495,1,2,2),_CacheSoftware_Type())
cacheSoftware.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheSoftware.setStatus(_A)
_CacheVersionId_Type=OctetString
_CacheVersionId_Object=MibScalar
cacheVersionId=_CacheVersionId_Object((1,3,6,1,4,1,3495,1,2,3),_CacheVersionId_Type())
cacheVersionId.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheVersionId.setStatus(_A)
_CacheLoggingFacility_Type=DisplayString
_CacheLoggingFacility_Object=MibScalar
cacheLoggingFacility=_CacheLoggingFacility_Object((1,3,6,1,4,1,3495,1,2,4),_CacheLoggingFacility_Type())
cacheLoggingFacility.setMaxAccess('read-write')
if mibBuilder.loadTexts:cacheLoggingFacility.setStatus(_A)
_CacheStorageConfig_ObjectIdentity=ObjectIdentity
cacheStorageConfig=_CacheStorageConfig_ObjectIdentity((1,3,6,1,4,1,3495,1,2,5))
_CacheMemMaxSize_Type=Integer32
_CacheMemMaxSize_Object=MibScalar
cacheMemMaxSize=_CacheMemMaxSize_Object((1,3,6,1,4,1,3495,1,2,5,1),_CacheMemMaxSize_Type())
cacheMemMaxSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheMemMaxSize.setStatus(_A)
_CacheSwapMaxSize_Type=Integer32
_CacheSwapMaxSize_Object=MibScalar
cacheSwapMaxSize=_CacheSwapMaxSize_Object((1,3,6,1,4,1,3495,1,2,5,2),_CacheSwapMaxSize_Type())
cacheSwapMaxSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheSwapMaxSize.setStatus(_A)
_CacheSwapHighWM_Type=Integer32
_CacheSwapHighWM_Object=MibScalar
cacheSwapHighWM=_CacheSwapHighWM_Object((1,3,6,1,4,1,3495,1,2,5,3),_CacheSwapHighWM_Type())
cacheSwapHighWM.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheSwapHighWM.setStatus(_A)
_CacheSwapLowWM_Type=Integer32
_CacheSwapLowWM_Object=MibScalar
cacheSwapLowWM=_CacheSwapLowWM_Object((1,3,6,1,4,1,3495,1,2,5,4),_CacheSwapLowWM_Type())
cacheSwapLowWM.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheSwapLowWM.setStatus(_A)
_CacheUniqName_Type=DisplayString
_CacheUniqName_Object=MibScalar
cacheUniqName=_CacheUniqName_Object((1,3,6,1,4,1,3495,1,2,6),_CacheUniqName_Type())
cacheUniqName.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheUniqName.setStatus(_A)
_CachePerf_ObjectIdentity=ObjectIdentity
cachePerf=_CachePerf_ObjectIdentity((1,3,6,1,4,1,3495,1,3))
_CacheSysPerf_ObjectIdentity=ObjectIdentity
cacheSysPerf=_CacheSysPerf_ObjectIdentity((1,3,6,1,4,1,3495,1,3,1))
_CacheSysPageFaults_Type=Counter32
_CacheSysPageFaults_Object=MibScalar
cacheSysPageFaults=_CacheSysPageFaults_Object((1,3,6,1,4,1,3495,1,3,1,1),_CacheSysPageFaults_Type())
cacheSysPageFaults.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheSysPageFaults.setStatus(_A)
_CacheSysNumReads_Type=Counter32
_CacheSysNumReads_Object=MibScalar
cacheSysNumReads=_CacheSysNumReads_Object((1,3,6,1,4,1,3495,1,3,1,2),_CacheSysNumReads_Type())
cacheSysNumReads.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheSysNumReads.setStatus(_A)
_CacheMemUsage_Type=Integer32
_CacheMemUsage_Object=MibScalar
cacheMemUsage=_CacheMemUsage_Object((1,3,6,1,4,1,3495,1,3,1,3),_CacheMemUsage_Type())
cacheMemUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheMemUsage.setStatus(_A)
_CacheCpuTime_Type=Integer32
_CacheCpuTime_Object=MibScalar
cacheCpuTime=_CacheCpuTime_Object((1,3,6,1,4,1,3495,1,3,1,4),_CacheCpuTime_Type())
cacheCpuTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheCpuTime.setStatus(_A)
_CacheCpuUsage_Type=Integer32
_CacheCpuUsage_Object=MibScalar
cacheCpuUsage=_CacheCpuUsage_Object((1,3,6,1,4,1,3495,1,3,1,5),_CacheCpuUsage_Type())
cacheCpuUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheCpuUsage.setStatus(_A)
_CacheMaxResSize_Type=Integer32
_CacheMaxResSize_Object=MibScalar
cacheMaxResSize=_CacheMaxResSize_Object((1,3,6,1,4,1,3495,1,3,1,6),_CacheMaxResSize_Type())
cacheMaxResSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheMaxResSize.setStatus(_A)
_CacheNumObjCount_Type=Gauge32
_CacheNumObjCount_Object=MibScalar
cacheNumObjCount=_CacheNumObjCount_Object((1,3,6,1,4,1,3495,1,3,1,7),_CacheNumObjCount_Type())
cacheNumObjCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheNumObjCount.setStatus(_A)
_CacheCurrentLRUExpiration_Type=TimeTicks
_CacheCurrentLRUExpiration_Object=MibScalar
cacheCurrentLRUExpiration=_CacheCurrentLRUExpiration_Object((1,3,6,1,4,1,3495,1,3,1,8),_CacheCurrentLRUExpiration_Type())
cacheCurrentLRUExpiration.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheCurrentLRUExpiration.setStatus(_A)
_CacheCurrentUnlinkRequests_Type=Gauge32
_CacheCurrentUnlinkRequests_Object=MibScalar
cacheCurrentUnlinkRequests=_CacheCurrentUnlinkRequests_Object((1,3,6,1,4,1,3495,1,3,1,9),_CacheCurrentUnlinkRequests_Type())
cacheCurrentUnlinkRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheCurrentUnlinkRequests.setStatus(_A)
_CacheCurrentUnusedFDescrCnt_Type=Gauge32
_CacheCurrentUnusedFDescrCnt_Object=MibScalar
cacheCurrentUnusedFDescrCnt=_CacheCurrentUnusedFDescrCnt_Object((1,3,6,1,4,1,3495,1,3,1,10),_CacheCurrentUnusedFDescrCnt_Type())
cacheCurrentUnusedFDescrCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheCurrentUnusedFDescrCnt.setStatus(_A)
_CacheCurrentResFileDescrCnt_Type=Gauge32
_CacheCurrentResFileDescrCnt_Object=MibScalar
cacheCurrentResFileDescrCnt=_CacheCurrentResFileDescrCnt_Object((1,3,6,1,4,1,3495,1,3,1,11),_CacheCurrentResFileDescrCnt_Type())
cacheCurrentResFileDescrCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheCurrentResFileDescrCnt.setStatus(_A)
_CacheCurrentFileDescrCnt_Type=Gauge32
_CacheCurrentFileDescrCnt_Object=MibScalar
cacheCurrentFileDescrCnt=_CacheCurrentFileDescrCnt_Object((1,3,6,1,4,1,3495,1,3,1,12),_CacheCurrentFileDescrCnt_Type())
cacheCurrentFileDescrCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheCurrentFileDescrCnt.setStatus(_A)
_CacheCurrentFileDescrMax_Type=Gauge32
_CacheCurrentFileDescrMax_Object=MibScalar
cacheCurrentFileDescrMax=_CacheCurrentFileDescrMax_Object((1,3,6,1,4,1,3495,1,3,1,13),_CacheCurrentFileDescrMax_Type())
cacheCurrentFileDescrMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheCurrentFileDescrMax.setStatus(_A)
_CacheProtoStats_ObjectIdentity=ObjectIdentity
cacheProtoStats=_CacheProtoStats_ObjectIdentity((1,3,6,1,4,1,3495,1,3,2))
_CacheProtoAggregateStats_ObjectIdentity=ObjectIdentity
cacheProtoAggregateStats=_CacheProtoAggregateStats_ObjectIdentity((1,3,6,1,4,1,3495,1,3,2,1))
_CacheProtoClientHttpRequests_Type=Counter32
_CacheProtoClientHttpRequests_Object=MibScalar
cacheProtoClientHttpRequests=_CacheProtoClientHttpRequests_Object((1,3,6,1,4,1,3495,1,3,2,1,1),_CacheProtoClientHttpRequests_Type())
cacheProtoClientHttpRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheProtoClientHttpRequests.setStatus(_A)
_CacheHttpHits_Type=Counter32
_CacheHttpHits_Object=MibScalar
cacheHttpHits=_CacheHttpHits_Object((1,3,6,1,4,1,3495,1,3,2,1,2),_CacheHttpHits_Type())
cacheHttpHits.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheHttpHits.setStatus(_A)
_CacheHttpErrors_Type=Counter32
_CacheHttpErrors_Object=MibScalar
cacheHttpErrors=_CacheHttpErrors_Object((1,3,6,1,4,1,3495,1,3,2,1,3),_CacheHttpErrors_Type())
cacheHttpErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheHttpErrors.setStatus(_A)
_CacheHttpInKb_Type=Counter32
_CacheHttpInKb_Object=MibScalar
cacheHttpInKb=_CacheHttpInKb_Object((1,3,6,1,4,1,3495,1,3,2,1,4),_CacheHttpInKb_Type())
cacheHttpInKb.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheHttpInKb.setStatus(_A)
_CacheHttpOutKb_Type=Counter32
_CacheHttpOutKb_Object=MibScalar
cacheHttpOutKb=_CacheHttpOutKb_Object((1,3,6,1,4,1,3495,1,3,2,1,5),_CacheHttpOutKb_Type())
cacheHttpOutKb.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheHttpOutKb.setStatus(_A)
_CacheIcpPktsSent_Type=Counter32
_CacheIcpPktsSent_Object=MibScalar
cacheIcpPktsSent=_CacheIcpPktsSent_Object((1,3,6,1,4,1,3495,1,3,2,1,6),_CacheIcpPktsSent_Type())
cacheIcpPktsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheIcpPktsSent.setStatus(_A)
_CacheIcpPktsRecv_Type=Counter32
_CacheIcpPktsRecv_Object=MibScalar
cacheIcpPktsRecv=_CacheIcpPktsRecv_Object((1,3,6,1,4,1,3495,1,3,2,1,7),_CacheIcpPktsRecv_Type())
cacheIcpPktsRecv.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheIcpPktsRecv.setStatus(_A)
_CacheIcpKbSent_Type=Counter32
_CacheIcpKbSent_Object=MibScalar
cacheIcpKbSent=_CacheIcpKbSent_Object((1,3,6,1,4,1,3495,1,3,2,1,8),_CacheIcpKbSent_Type())
cacheIcpKbSent.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheIcpKbSent.setStatus(_A)
_CacheIcpKbRecv_Type=Counter32
_CacheIcpKbRecv_Object=MibScalar
cacheIcpKbRecv=_CacheIcpKbRecv_Object((1,3,6,1,4,1,3495,1,3,2,1,9),_CacheIcpKbRecv_Type())
cacheIcpKbRecv.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheIcpKbRecv.setStatus(_A)
_CacheServerRequests_Type=Integer32
_CacheServerRequests_Object=MibScalar
cacheServerRequests=_CacheServerRequests_Object((1,3,6,1,4,1,3495,1,3,2,1,10),_CacheServerRequests_Type())
cacheServerRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheServerRequests.setStatus(_A)
_CacheServerErrors_Type=Integer32
_CacheServerErrors_Object=MibScalar
cacheServerErrors=_CacheServerErrors_Object((1,3,6,1,4,1,3495,1,3,2,1,11),_CacheServerErrors_Type())
cacheServerErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheServerErrors.setStatus(_A)
_CacheServerInKb_Type=Counter32
_CacheServerInKb_Object=MibScalar
cacheServerInKb=_CacheServerInKb_Object((1,3,6,1,4,1,3495,1,3,2,1,12),_CacheServerInKb_Type())
cacheServerInKb.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheServerInKb.setStatus(_A)
_CacheServerOutKb_Type=Counter32
_CacheServerOutKb_Object=MibScalar
cacheServerOutKb=_CacheServerOutKb_Object((1,3,6,1,4,1,3495,1,3,2,1,13),_CacheServerOutKb_Type())
cacheServerOutKb.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheServerOutKb.setStatus(_A)
_CacheCurrentSwapSize_Type=Gauge32
_CacheCurrentSwapSize_Object=MibScalar
cacheCurrentSwapSize=_CacheCurrentSwapSize_Object((1,3,6,1,4,1,3495,1,3,2,1,14),_CacheCurrentSwapSize_Type())
cacheCurrentSwapSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheCurrentSwapSize.setStatus(_A)
_CacheClients_Type=Gauge32
_CacheClients_Object=MibScalar
cacheClients=_CacheClients_Object((1,3,6,1,4,1,3495,1,3,2,1,15),_CacheClients_Type())
cacheClients.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheClients.setStatus(_A)
_CacheMedianSvcTable_Object=MibTable
cacheMedianSvcTable=_CacheMedianSvcTable_Object((1,3,6,1,4,1,3495,1,3,2,2))
if mibBuilder.loadTexts:cacheMedianSvcTable.setStatus(_A)
_CacheMedianSvcEntry_Object=MibTableRow
cacheMedianSvcEntry=_CacheMedianSvcEntry_Object((1,3,6,1,4,1,3495,1,3,2,2,1))
cacheMedianSvcEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cacheMedianSvcEntry.setStatus(_A)
class _CacheMedianTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1),ValueRangeConstraint(5,5),ValueRangeConstraint(60,60))
_CacheMedianTime_Type.__name__=_E
_CacheMedianTime_Object=MibTableColumn
cacheMedianTime=_CacheMedianTime_Object((1,3,6,1,4,1,3495,1,3,2,2,1,1),_CacheMedianTime_Type())
cacheMedianTime.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cacheMedianTime.setStatus(_A)
_CacheHttpAllSvcTime_Type=Integer32
_CacheHttpAllSvcTime_Object=MibTableColumn
cacheHttpAllSvcTime=_CacheHttpAllSvcTime_Object((1,3,6,1,4,1,3495,1,3,2,2,1,2),_CacheHttpAllSvcTime_Type())
cacheHttpAllSvcTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheHttpAllSvcTime.setStatus(_A)
_CacheHttpMissSvcTime_Type=Integer32
_CacheHttpMissSvcTime_Object=MibTableColumn
cacheHttpMissSvcTime=_CacheHttpMissSvcTime_Object((1,3,6,1,4,1,3495,1,3,2,2,1,3),_CacheHttpMissSvcTime_Type())
cacheHttpMissSvcTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheHttpMissSvcTime.setStatus(_A)
_CacheHttpNmSvcTime_Type=Integer32
_CacheHttpNmSvcTime_Object=MibTableColumn
cacheHttpNmSvcTime=_CacheHttpNmSvcTime_Object((1,3,6,1,4,1,3495,1,3,2,2,1,4),_CacheHttpNmSvcTime_Type())
cacheHttpNmSvcTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheHttpNmSvcTime.setStatus(_A)
_CacheHttpHitSvcTime_Type=Integer32
_CacheHttpHitSvcTime_Object=MibTableColumn
cacheHttpHitSvcTime=_CacheHttpHitSvcTime_Object((1,3,6,1,4,1,3495,1,3,2,2,1,5),_CacheHttpHitSvcTime_Type())
cacheHttpHitSvcTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheHttpHitSvcTime.setStatus(_A)
_CacheIcpQuerySvcTime_Type=Integer32
_CacheIcpQuerySvcTime_Object=MibTableColumn
cacheIcpQuerySvcTime=_CacheIcpQuerySvcTime_Object((1,3,6,1,4,1,3495,1,3,2,2,1,6),_CacheIcpQuerySvcTime_Type())
cacheIcpQuerySvcTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheIcpQuerySvcTime.setStatus(_A)
_CacheIcpReplySvcTime_Type=Integer32
_CacheIcpReplySvcTime_Object=MibTableColumn
cacheIcpReplySvcTime=_CacheIcpReplySvcTime_Object((1,3,6,1,4,1,3495,1,3,2,2,1,7),_CacheIcpReplySvcTime_Type())
cacheIcpReplySvcTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheIcpReplySvcTime.setStatus(_A)
_CacheDnsSvcTime_Type=Integer32
_CacheDnsSvcTime_Object=MibTableColumn
cacheDnsSvcTime=_CacheDnsSvcTime_Object((1,3,6,1,4,1,3495,1,3,2,2,1,8),_CacheDnsSvcTime_Type())
cacheDnsSvcTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheDnsSvcTime.setStatus(_A)
_CacheRequestHitRatio_Type=Integer32
_CacheRequestHitRatio_Object=MibTableColumn
cacheRequestHitRatio=_CacheRequestHitRatio_Object((1,3,6,1,4,1,3495,1,3,2,2,1,9),_CacheRequestHitRatio_Type())
cacheRequestHitRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheRequestHitRatio.setStatus(_A)
_CacheRequestByteRatio_Type=Integer32
_CacheRequestByteRatio_Object=MibTableColumn
cacheRequestByteRatio=_CacheRequestByteRatio_Object((1,3,6,1,4,1,3495,1,3,2,2,1,10),_CacheRequestByteRatio_Type())
cacheRequestByteRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheRequestByteRatio.setStatus(_A)
_CacheHttpNhSvcTime_Type=Integer32
_CacheHttpNhSvcTime_Object=MibTableColumn
cacheHttpNhSvcTime=_CacheHttpNhSvcTime_Object((1,3,6,1,4,1,3495,1,3,2,2,1,11),_CacheHttpNhSvcTime_Type())
cacheHttpNhSvcTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheHttpNhSvcTime.setStatus(_A)
_CacheNetwork_ObjectIdentity=ObjectIdentity
cacheNetwork=_CacheNetwork_ObjectIdentity((1,3,6,1,4,1,3495,1,4))
_CacheIpCache_ObjectIdentity=ObjectIdentity
cacheIpCache=_CacheIpCache_ObjectIdentity((1,3,6,1,4,1,3495,1,4,1))
_CacheIpEntries_Type=Gauge32
_CacheIpEntries_Object=MibScalar
cacheIpEntries=_CacheIpEntries_Object((1,3,6,1,4,1,3495,1,4,1,1),_CacheIpEntries_Type())
cacheIpEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheIpEntries.setStatus(_A)
_CacheIpRequests_Type=Counter32
_CacheIpRequests_Object=MibScalar
cacheIpRequests=_CacheIpRequests_Object((1,3,6,1,4,1,3495,1,4,1,2),_CacheIpRequests_Type())
cacheIpRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheIpRequests.setStatus(_A)
_CacheIpHits_Type=Counter32
_CacheIpHits_Object=MibScalar
cacheIpHits=_CacheIpHits_Object((1,3,6,1,4,1,3495,1,4,1,3),_CacheIpHits_Type())
cacheIpHits.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheIpHits.setStatus(_A)
_CacheIpPendingHits_Type=Gauge32
_CacheIpPendingHits_Object=MibScalar
cacheIpPendingHits=_CacheIpPendingHits_Object((1,3,6,1,4,1,3495,1,4,1,4),_CacheIpPendingHits_Type())
cacheIpPendingHits.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheIpPendingHits.setStatus(_A)
_CacheIpNegativeHits_Type=Counter32
_CacheIpNegativeHits_Object=MibScalar
cacheIpNegativeHits=_CacheIpNegativeHits_Object((1,3,6,1,4,1,3495,1,4,1,5),_CacheIpNegativeHits_Type())
cacheIpNegativeHits.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheIpNegativeHits.setStatus(_A)
_CacheIpMisses_Type=Counter32
_CacheIpMisses_Object=MibScalar
cacheIpMisses=_CacheIpMisses_Object((1,3,6,1,4,1,3495,1,4,1,6),_CacheIpMisses_Type())
cacheIpMisses.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheIpMisses.setStatus(_A)
_CacheBlockingGetHostByName_Type=Counter32
_CacheBlockingGetHostByName_Object=MibScalar
cacheBlockingGetHostByName=_CacheBlockingGetHostByName_Object((1,3,6,1,4,1,3495,1,4,1,7),_CacheBlockingGetHostByName_Type())
cacheBlockingGetHostByName.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheBlockingGetHostByName.setStatus(_A)
_CacheAttemptReleaseLckEntries_Type=Counter32
_CacheAttemptReleaseLckEntries_Object=MibScalar
cacheAttemptReleaseLckEntries=_CacheAttemptReleaseLckEntries_Object((1,3,6,1,4,1,3495,1,4,1,8),_CacheAttemptReleaseLckEntries_Type())
cacheAttemptReleaseLckEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheAttemptReleaseLckEntries.setStatus(_A)
_CacheFqdnCache_ObjectIdentity=ObjectIdentity
cacheFqdnCache=_CacheFqdnCache_ObjectIdentity((1,3,6,1,4,1,3495,1,4,2))
_CacheFqdnEntries_Type=Gauge32
_CacheFqdnEntries_Object=MibScalar
cacheFqdnEntries=_CacheFqdnEntries_Object((1,3,6,1,4,1,3495,1,4,2,1),_CacheFqdnEntries_Type())
cacheFqdnEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheFqdnEntries.setStatus(_A)
_CacheFqdnRequests_Type=Counter32
_CacheFqdnRequests_Object=MibScalar
cacheFqdnRequests=_CacheFqdnRequests_Object((1,3,6,1,4,1,3495,1,4,2,2),_CacheFqdnRequests_Type())
cacheFqdnRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheFqdnRequests.setStatus(_A)
_CacheFqdnHits_Type=Counter32
_CacheFqdnHits_Object=MibScalar
cacheFqdnHits=_CacheFqdnHits_Object((1,3,6,1,4,1,3495,1,4,2,3),_CacheFqdnHits_Type())
cacheFqdnHits.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheFqdnHits.setStatus(_A)
_CacheFqdnPendingHits_Type=Gauge32
_CacheFqdnPendingHits_Object=MibScalar
cacheFqdnPendingHits=_CacheFqdnPendingHits_Object((1,3,6,1,4,1,3495,1,4,2,4),_CacheFqdnPendingHits_Type())
cacheFqdnPendingHits.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheFqdnPendingHits.setStatus(_A)
_CacheFqdnNegativeHits_Type=Counter32
_CacheFqdnNegativeHits_Object=MibScalar
cacheFqdnNegativeHits=_CacheFqdnNegativeHits_Object((1,3,6,1,4,1,3495,1,4,2,5),_CacheFqdnNegativeHits_Type())
cacheFqdnNegativeHits.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheFqdnNegativeHits.setStatus(_A)
_CacheFqdnMisses_Type=Counter32
_CacheFqdnMisses_Object=MibScalar
cacheFqdnMisses=_CacheFqdnMisses_Object((1,3,6,1,4,1,3495,1,4,2,6),_CacheFqdnMisses_Type())
cacheFqdnMisses.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheFqdnMisses.setStatus(_A)
_CacheBlockingGetHostByAddr_Type=Counter32
_CacheBlockingGetHostByAddr_Object=MibScalar
cacheBlockingGetHostByAddr=_CacheBlockingGetHostByAddr_Object((1,3,6,1,4,1,3495,1,4,2,7),_CacheBlockingGetHostByAddr_Type())
cacheBlockingGetHostByAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheBlockingGetHostByAddr.setStatus(_A)
_CacheDns_ObjectIdentity=ObjectIdentity
cacheDns=_CacheDns_ObjectIdentity((1,3,6,1,4,1,3495,1,4,3))
_CacheDnsRequests_Type=Counter32
_CacheDnsRequests_Object=MibScalar
cacheDnsRequests=_CacheDnsRequests_Object((1,3,6,1,4,1,3495,1,4,3,1),_CacheDnsRequests_Type())
cacheDnsRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheDnsRequests.setStatus(_A)
_CacheDnsReplies_Type=Counter32
_CacheDnsReplies_Object=MibScalar
cacheDnsReplies=_CacheDnsReplies_Object((1,3,6,1,4,1,3495,1,4,3,2),_CacheDnsReplies_Type())
cacheDnsReplies.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheDnsReplies.setStatus(_A)
_CacheDnsNumberServers_Type=Counter32
_CacheDnsNumberServers_Object=MibScalar
cacheDnsNumberServers=_CacheDnsNumberServers_Object((1,3,6,1,4,1,3495,1,4,3,3),_CacheDnsNumberServers_Type())
cacheDnsNumberServers.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheDnsNumberServers.setStatus(_A)
_CacheMesh_ObjectIdentity=ObjectIdentity
cacheMesh=_CacheMesh_ObjectIdentity((1,3,6,1,4,1,3495,1,5))
_CachePeerTable_Object=MibTable
cachePeerTable=_CachePeerTable_Object((1,3,6,1,4,1,3495,1,5,1))
if mibBuilder.loadTexts:cachePeerTable.setStatus(_A)
_CachePeerEntry_Object=MibTableRow
cachePeerEntry=_CachePeerEntry_Object((1,3,6,1,4,1,3495,1,5,1,3))
cachePeerEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:cachePeerEntry.setStatus(_A)
_CachePeerIndex_Type=CachePeerTableIndex
_CachePeerIndex_Object=MibTableColumn
cachePeerIndex=_CachePeerIndex_Object((1,3,6,1,4,1,3495,1,5,1,3,1),_CachePeerIndex_Type())
cachePeerIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cachePeerIndex.setStatus(_A)
_CachePeerName_Type=DisplayString
_CachePeerName_Object=MibTableColumn
cachePeerName=_CachePeerName_Object((1,3,6,1,4,1,3495,1,5,1,3,2),_CachePeerName_Type())
cachePeerName.setMaxAccess(_B)
if mibBuilder.loadTexts:cachePeerName.setStatus(_A)
_CachePeerAddressType_Type=InetAddressType
_CachePeerAddressType_Object=MibTableColumn
cachePeerAddressType=_CachePeerAddressType_Object((1,3,6,1,4,1,3495,1,5,1,3,3),_CachePeerAddressType_Type())
cachePeerAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:cachePeerAddressType.setStatus(_A)
class _CachePeerAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CachePeerAddress_Type.__name__=_D
_CachePeerAddress_Object=MibTableColumn
cachePeerAddress=_CachePeerAddress_Object((1,3,6,1,4,1,3495,1,5,1,3,4),_CachePeerAddress_Type())
cachePeerAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:cachePeerAddress.setStatus(_A)
_CachePeerPortHttp_Type=ValidPort
_CachePeerPortHttp_Object=MibTableColumn
cachePeerPortHttp=_CachePeerPortHttp_Object((1,3,6,1,4,1,3495,1,5,1,3,5),_CachePeerPortHttp_Type())
cachePeerPortHttp.setMaxAccess(_B)
if mibBuilder.loadTexts:cachePeerPortHttp.setStatus(_A)
_CachePeerPortIcp_Type=ValidPort
_CachePeerPortIcp_Object=MibTableColumn
cachePeerPortIcp=_CachePeerPortIcp_Object((1,3,6,1,4,1,3495,1,5,1,3,6),_CachePeerPortIcp_Type())
cachePeerPortIcp.setMaxAccess(_B)
if mibBuilder.loadTexts:cachePeerPortIcp.setStatus(_A)
_CachePeerType_Type=Integer32
_CachePeerType_Object=MibTableColumn
cachePeerType=_CachePeerType_Object((1,3,6,1,4,1,3495,1,5,1,3,7),_CachePeerType_Type())
cachePeerType.setMaxAccess(_B)
if mibBuilder.loadTexts:cachePeerType.setStatus(_A)
_CachePeerState_Type=Integer32
_CachePeerState_Object=MibTableColumn
cachePeerState=_CachePeerState_Object((1,3,6,1,4,1,3495,1,5,1,3,8),_CachePeerState_Type())
cachePeerState.setMaxAccess(_B)
if mibBuilder.loadTexts:cachePeerState.setStatus(_A)
_CachePeerPingsSent_Type=Counter32
_CachePeerPingsSent_Object=MibTableColumn
cachePeerPingsSent=_CachePeerPingsSent_Object((1,3,6,1,4,1,3495,1,5,1,3,9),_CachePeerPingsSent_Type())
cachePeerPingsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:cachePeerPingsSent.setStatus(_A)
_CachePeerPingsAcked_Type=Counter32
_CachePeerPingsAcked_Object=MibTableColumn
cachePeerPingsAcked=_CachePeerPingsAcked_Object((1,3,6,1,4,1,3495,1,5,1,3,10),_CachePeerPingsAcked_Type())
cachePeerPingsAcked.setMaxAccess(_B)
if mibBuilder.loadTexts:cachePeerPingsAcked.setStatus(_A)
_CachePeerFetches_Type=Counter32
_CachePeerFetches_Object=MibTableColumn
cachePeerFetches=_CachePeerFetches_Object((1,3,6,1,4,1,3495,1,5,1,3,11),_CachePeerFetches_Type())
cachePeerFetches.setMaxAccess(_B)
if mibBuilder.loadTexts:cachePeerFetches.setStatus(_A)
_CachePeerRtt_Type=Integer32
_CachePeerRtt_Object=MibTableColumn
cachePeerRtt=_CachePeerRtt_Object((1,3,6,1,4,1,3495,1,5,1,3,12),_CachePeerRtt_Type())
cachePeerRtt.setMaxAccess(_B)
if mibBuilder.loadTexts:cachePeerRtt.setStatus(_A)
_CachePeerIgnored_Type=Counter32
_CachePeerIgnored_Object=MibTableColumn
cachePeerIgnored=_CachePeerIgnored_Object((1,3,6,1,4,1,3495,1,5,1,3,13),_CachePeerIgnored_Type())
cachePeerIgnored.setMaxAccess(_B)
if mibBuilder.loadTexts:cachePeerIgnored.setStatus(_A)
_CachePeerKeepAlSent_Type=Counter32
_CachePeerKeepAlSent_Object=MibTableColumn
cachePeerKeepAlSent=_CachePeerKeepAlSent_Object((1,3,6,1,4,1,3495,1,5,1,3,14),_CachePeerKeepAlSent_Type())
cachePeerKeepAlSent.setMaxAccess(_B)
if mibBuilder.loadTexts:cachePeerKeepAlSent.setStatus(_A)
_CachePeerKeepAlRecv_Type=Counter32
_CachePeerKeepAlRecv_Object=MibTableColumn
cachePeerKeepAlRecv=_CachePeerKeepAlRecv_Object((1,3,6,1,4,1,3495,1,5,1,3,15),_CachePeerKeepAlRecv_Type())
cachePeerKeepAlRecv.setMaxAccess(_B)
if mibBuilder.loadTexts:cachePeerKeepAlRecv.setStatus(_A)
_CacheClientTable_Object=MibTable
cacheClientTable=_CacheClientTable_Object((1,3,6,1,4,1,3495,1,5,2))
if mibBuilder.loadTexts:cacheClientTable.setStatus(_A)
_CacheClientEntry_Object=MibTableRow
cacheClientEntry=_CacheClientEntry_Object((1,3,6,1,4,1,3495,1,5,2,2))
cacheClientEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:cacheClientEntry.setStatus(_A)
_CacheClientAddressType_Type=InetAddressType
_CacheClientAddressType_Object=MibTableColumn
cacheClientAddressType=_CacheClientAddressType_Object((1,3,6,1,4,1,3495,1,5,2,2,1),_CacheClientAddressType_Type())
cacheClientAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheClientAddressType.setStatus(_A)
class _CacheClientAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CacheClientAddress_Type.__name__=_D
_CacheClientAddress_Object=MibTableColumn
cacheClientAddress=_CacheClientAddress_Object((1,3,6,1,4,1,3495,1,5,2,2,2),_CacheClientAddress_Type())
cacheClientAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheClientAddress.setStatus(_A)
_CacheClientHttpRequests_Type=Counter32
_CacheClientHttpRequests_Object=MibTableColumn
cacheClientHttpRequests=_CacheClientHttpRequests_Object((1,3,6,1,4,1,3495,1,5,2,2,3),_CacheClientHttpRequests_Type())
cacheClientHttpRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheClientHttpRequests.setStatus(_A)
_CacheClientHttpKb_Type=Counter32
_CacheClientHttpKb_Object=MibTableColumn
cacheClientHttpKb=_CacheClientHttpKb_Object((1,3,6,1,4,1,3495,1,5,2,2,4),_CacheClientHttpKb_Type())
cacheClientHttpKb.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheClientHttpKb.setStatus(_A)
_CacheClientHttpHits_Type=Counter32
_CacheClientHttpHits_Object=MibTableColumn
cacheClientHttpHits=_CacheClientHttpHits_Object((1,3,6,1,4,1,3495,1,5,2,2,5),_CacheClientHttpHits_Type())
cacheClientHttpHits.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheClientHttpHits.setStatus(_A)
_CacheClientHTTPHitKb_Type=Counter32
_CacheClientHTTPHitKb_Object=MibTableColumn
cacheClientHTTPHitKb=_CacheClientHTTPHitKb_Object((1,3,6,1,4,1,3495,1,5,2,2,6),_CacheClientHTTPHitKb_Type())
cacheClientHTTPHitKb.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheClientHTTPHitKb.setStatus(_A)
_CacheClientIcpRequests_Type=Counter32
_CacheClientIcpRequests_Object=MibTableColumn
cacheClientIcpRequests=_CacheClientIcpRequests_Object((1,3,6,1,4,1,3495,1,5,2,2,7),_CacheClientIcpRequests_Type())
cacheClientIcpRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheClientIcpRequests.setStatus(_A)
_CacheClientIcpKb_Type=Counter32
_CacheClientIcpKb_Object=MibTableColumn
cacheClientIcpKb=_CacheClientIcpKb_Object((1,3,6,1,4,1,3495,1,5,2,2,8),_CacheClientIcpKb_Type())
cacheClientIcpKb.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheClientIcpKb.setStatus(_A)
_CacheClientIcpHits_Type=Counter32
_CacheClientIcpHits_Object=MibTableColumn
cacheClientIcpHits=_CacheClientIcpHits_Object((1,3,6,1,4,1,3495,1,5,2,2,9),_CacheClientIcpHits_Type())
cacheClientIcpHits.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheClientIcpHits.setStatus(_A)
_CacheClientIcpHitKb_Type=Counter32
_CacheClientIcpHitKb_Object=MibTableColumn
cacheClientIcpHitKb=_CacheClientIcpHitKb_Object((1,3,6,1,4,1,3495,1,5,2,2,10),_CacheClientIcpHitKb_Type())
cacheClientIcpHitKb.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheClientIcpHitKb.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'ValidPort':ValidPort,'CachePeerTableIndex':CachePeerTableIndex,'nlanr':nlanr,'squid':squid,'cacheSystem':cacheSystem,'cacheSysVMsize':cacheSysVMsize,'cacheSysStorage':cacheSysStorage,'cacheUptime':cacheUptime,'cacheConfig':cacheConfig,'cacheAdmin':cacheAdmin,'cacheSoftware':cacheSoftware,'cacheVersionId':cacheVersionId,'cacheLoggingFacility':cacheLoggingFacility,'cacheStorageConfig':cacheStorageConfig,'cacheMemMaxSize':cacheMemMaxSize,'cacheSwapMaxSize':cacheSwapMaxSize,'cacheSwapHighWM':cacheSwapHighWM,'cacheSwapLowWM':cacheSwapLowWM,'cacheUniqName':cacheUniqName,'cachePerf':cachePerf,'cacheSysPerf':cacheSysPerf,'cacheSysPageFaults':cacheSysPageFaults,'cacheSysNumReads':cacheSysNumReads,'cacheMemUsage':cacheMemUsage,'cacheCpuTime':cacheCpuTime,'cacheCpuUsage':cacheCpuUsage,'cacheMaxResSize':cacheMaxResSize,'cacheNumObjCount':cacheNumObjCount,'cacheCurrentLRUExpiration':cacheCurrentLRUExpiration,'cacheCurrentUnlinkRequests':cacheCurrentUnlinkRequests,'cacheCurrentUnusedFDescrCnt':cacheCurrentUnusedFDescrCnt,'cacheCurrentResFileDescrCnt':cacheCurrentResFileDescrCnt,'cacheCurrentFileDescrCnt':cacheCurrentFileDescrCnt,'cacheCurrentFileDescrMax':cacheCurrentFileDescrMax,'cacheProtoStats':cacheProtoStats,'cacheProtoAggregateStats':cacheProtoAggregateStats,'cacheProtoClientHttpRequests':cacheProtoClientHttpRequests,'cacheHttpHits':cacheHttpHits,'cacheHttpErrors':cacheHttpErrors,'cacheHttpInKb':cacheHttpInKb,'cacheHttpOutKb':cacheHttpOutKb,'cacheIcpPktsSent':cacheIcpPktsSent,'cacheIcpPktsRecv':cacheIcpPktsRecv,'cacheIcpKbSent':cacheIcpKbSent,'cacheIcpKbRecv':cacheIcpKbRecv,'cacheServerRequests':cacheServerRequests,'cacheServerErrors':cacheServerErrors,'cacheServerInKb':cacheServerInKb,'cacheServerOutKb':cacheServerOutKb,'cacheCurrentSwapSize':cacheCurrentSwapSize,'cacheClients':cacheClients,'cacheMedianSvcTable':cacheMedianSvcTable,'cacheMedianSvcEntry':cacheMedianSvcEntry,_F:cacheMedianTime,'cacheHttpAllSvcTime':cacheHttpAllSvcTime,'cacheHttpMissSvcTime':cacheHttpMissSvcTime,'cacheHttpNmSvcTime':cacheHttpNmSvcTime,'cacheHttpHitSvcTime':cacheHttpHitSvcTime,'cacheIcpQuerySvcTime':cacheIcpQuerySvcTime,'cacheIcpReplySvcTime':cacheIcpReplySvcTime,'cacheDnsSvcTime':cacheDnsSvcTime,'cacheRequestHitRatio':cacheRequestHitRatio,'cacheRequestByteRatio':cacheRequestByteRatio,'cacheHttpNhSvcTime':cacheHttpNhSvcTime,'cacheNetwork':cacheNetwork,'cacheIpCache':cacheIpCache,'cacheIpEntries':cacheIpEntries,'cacheIpRequests':cacheIpRequests,'cacheIpHits':cacheIpHits,'cacheIpPendingHits':cacheIpPendingHits,'cacheIpNegativeHits':cacheIpNegativeHits,'cacheIpMisses':cacheIpMisses,'cacheBlockingGetHostByName':cacheBlockingGetHostByName,'cacheAttemptReleaseLckEntries':cacheAttemptReleaseLckEntries,'cacheFqdnCache':cacheFqdnCache,'cacheFqdnEntries':cacheFqdnEntries,'cacheFqdnRequests':cacheFqdnRequests,'cacheFqdnHits':cacheFqdnHits,'cacheFqdnPendingHits':cacheFqdnPendingHits,'cacheFqdnNegativeHits':cacheFqdnNegativeHits,'cacheFqdnMisses':cacheFqdnMisses,'cacheBlockingGetHostByAddr':cacheBlockingGetHostByAddr,'cacheDns':cacheDns,'cacheDnsRequests':cacheDnsRequests,'cacheDnsReplies':cacheDnsReplies,'cacheDnsNumberServers':cacheDnsNumberServers,'cacheMesh':cacheMesh,'cachePeerTable':cachePeerTable,'cachePeerEntry':cachePeerEntry,_G:cachePeerIndex,'cachePeerName':cachePeerName,'cachePeerAddressType':cachePeerAddressType,'cachePeerAddress':cachePeerAddress,'cachePeerPortHttp':cachePeerPortHttp,'cachePeerPortIcp':cachePeerPortIcp,'cachePeerType':cachePeerType,'cachePeerState':cachePeerState,'cachePeerPingsSent':cachePeerPingsSent,'cachePeerPingsAcked':cachePeerPingsAcked,'cachePeerFetches':cachePeerFetches,'cachePeerRtt':cachePeerRtt,'cachePeerIgnored':cachePeerIgnored,'cachePeerKeepAlSent':cachePeerKeepAlSent,'cachePeerKeepAlRecv':cachePeerKeepAlRecv,'cacheClientTable':cacheClientTable,'cacheClientEntry':cacheClientEntry,'cacheClientAddressType':cacheClientAddressType,_H:cacheClientAddress,'cacheClientHttpRequests':cacheClientHttpRequests,'cacheClientHttpKb':cacheClientHttpKb,'cacheClientHttpHits':cacheClientHttpHits,'cacheClientHTTPHitKb':cacheClientHTTPHitKb,'cacheClientIcpRequests':cacheClientIcpRequests,'cacheClientIcpKb':cacheClientIcpKb,'cacheClientIcpHits':cacheClientIcpHits,'cacheClientIcpHitKb':cacheClientIcpHitKb})