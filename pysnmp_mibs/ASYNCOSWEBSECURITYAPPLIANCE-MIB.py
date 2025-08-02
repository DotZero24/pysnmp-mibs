_K='diskStatEntryNumber'
_J='cacheMedianTime'
_I='cacheSizeHistBinNumber'
_H='cacheServerSizeHistBinNumber'
_G='cacheClientSizeHistBinNumber'
_F='connectionURL'
_E='ASYNCOS-MAIL-MIB'
_D='ASYNCOSWEBSECURITYAPPLIANCE-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
connectionURL,=mibBuilder.importSymbols(_E,_F)
asyncOSAppliances,=mibBuilder.importSymbols('IRONPORT-SMI','asyncOSAppliances')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
asyncOSWebSecurityAppliance=ModuleIdentity((1,3,6,1,4,1,15497,1,2))
if mibBuilder.loadTexts:asyncOSWebSecurityAppliance.setRevisions(('2013-08-09 00:00','2010-04-20 00:00','2010-04-15 00:00','2009-07-13 00:00','2007-03-27 00:00'))
_ProxySystem_ObjectIdentity=ObjectIdentity
proxySystem=_ProxySystem_ObjectIdentity((1,3,6,1,4,1,15497,1,2,1))
_CacheUptime_Type=TimeTicks
_CacheUptime_Object=MibScalar
cacheUptime=_CacheUptime_Object((1,3,6,1,4,1,15497,1,2,1,1),_CacheUptime_Type())
cacheUptime.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheUptime.setStatus(_A)
_CacheMemory_Type=Integer32
_CacheMemory_Object=MibScalar
cacheMemory=_CacheMemory_Object((1,3,6,1,4,1,15497,1,2,1,2),_CacheMemory_Type())
cacheMemory.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheMemory.setStatus(_A)
_CacheSysStorage_Type=Integer32
_CacheSysStorage_Object=MibScalar
cacheSysStorage=_CacheSysStorage_Object((1,3,6,1,4,1,15497,1,2,1,3),_CacheSysStorage_Type())
cacheSysStorage.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheSysStorage.setStatus(_A)
_ProxyConfig_ObjectIdentity=ObjectIdentity
proxyConfig=_ProxyConfig_ObjectIdentity((1,3,6,1,4,1,15497,1,2,2))
_CacheAdmin_Type=DisplayString
_CacheAdmin_Object=MibScalar
cacheAdmin=_CacheAdmin_Object((1,3,6,1,4,1,15497,1,2,2,1),_CacheAdmin_Type())
cacheAdmin.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheAdmin.setStatus(_A)
_CacheSoftware_Type=DisplayString
_CacheSoftware_Object=MibScalar
cacheSoftware=_CacheSoftware_Object((1,3,6,1,4,1,15497,1,2,2,2),_CacheSoftware_Type())
cacheSoftware.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheSoftware.setStatus(_A)
_CacheVersion_Type=DisplayString
_CacheVersion_Object=MibScalar
cacheVersion=_CacheVersion_Object((1,3,6,1,4,1,15497,1,2,2,3),_CacheVersion_Type())
cacheVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheVersion.setStatus(_A)
_LicenseExpiration_Type=Integer32
_LicenseExpiration_Object=MibScalar
licenseExpiration=_LicenseExpiration_Object((1,3,6,1,4,1,15497,1,2,2,4),_LicenseExpiration_Type())
licenseExpiration.setMaxAccess(_B)
if mibBuilder.loadTexts:licenseExpiration.setStatus(_A)
_ProxyPerf_ObjectIdentity=ObjectIdentity
proxyPerf=_ProxyPerf_ObjectIdentity((1,3,6,1,4,1,15497,1,2,3))
_ProxySysPerf_ObjectIdentity=ObjectIdentity
proxySysPerf=_ProxySysPerf_ObjectIdentity((1,3,6,1,4,1,15497,1,2,3,1))
_CacheCpuTime_Type=Integer32
_CacheCpuTime_Object=MibScalar
cacheCpuTime=_CacheCpuTime_Object((1,3,6,1,4,1,15497,1,2,3,1,1),_CacheCpuTime_Type())
cacheCpuTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheCpuTime.setStatus(_A)
_CacheCpuUsage_Type=Integer32
_CacheCpuUsage_Object=MibScalar
cacheCpuUsage=_CacheCpuUsage_Object((1,3,6,1,4,1,15497,1,2,3,1,2),_CacheCpuUsage_Type())
cacheCpuUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheCpuUsage.setStatus(_A)
_CacheMaxResSize_Type=Integer32
_CacheMaxResSize_Object=MibScalar
cacheMaxResSize=_CacheMaxResSize_Object((1,3,6,1,4,1,15497,1,2,3,1,3),_CacheMaxResSize_Type())
cacheMaxResSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheMaxResSize.setStatus(_A)
_CacheUsedStoragePct_Type=Integer32
_CacheUsedStoragePct_Object=MibScalar
cacheUsedStoragePct=_CacheUsedStoragePct_Object((1,3,6,1,4,1,15497,1,2,3,1,4),_CacheUsedStoragePct_Type())
cacheUsedStoragePct.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheUsedStoragePct.setStatus(_A)
_CacheBusyCPUPct_Type=Integer32
_CacheBusyCPUPct_Object=MibScalar
cacheBusyCPUPct=_CacheBusyCPUPct_Object((1,3,6,1,4,1,15497,1,2,3,1,5),_CacheBusyCPUPct_Type())
cacheBusyCPUPct.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheBusyCPUPct.setStatus(_A)
_CacheMemoryBufferUsagePct_Type=Integer32
_CacheMemoryBufferUsagePct_Object=MibScalar
cacheMemoryBufferUsagePct=_CacheMemoryBufferUsagePct_Object((1,3,6,1,4,1,15497,1,2,3,1,6),_CacheMemoryBufferUsagePct_Type())
cacheMemoryBufferUsagePct.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheMemoryBufferUsagePct.setStatus(_A)
_ProxyClientSidePerf_ObjectIdentity=ObjectIdentity
proxyClientSidePerf=_ProxyClientSidePerf_ObjectIdentity((1,3,6,1,4,1,15497,1,2,3,2))
_CacheClientSizeHistTable_Object=MibTable
cacheClientSizeHistTable=_CacheClientSizeHistTable_Object((1,3,6,1,4,1,15497,1,2,3,2,1))
if mibBuilder.loadTexts:cacheClientSizeHistTable.setStatus(_A)
_CacheClientSizeHistEntry_Object=MibTableRow
cacheClientSizeHistEntry=_CacheClientSizeHistEntry_Object((1,3,6,1,4,1,15497,1,2,3,2,1,1))
cacheClientSizeHistEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:cacheClientSizeHistEntry.setStatus(_A)
class _CacheClientSizeHistBinNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_CacheClientSizeHistBinNumber_Type.__name__=_C
_CacheClientSizeHistBinNumber_Object=MibTableColumn
cacheClientSizeHistBinNumber=_CacheClientSizeHistBinNumber_Object((1,3,6,1,4,1,15497,1,2,3,2,1,1,1),_CacheClientSizeHistBinNumber_Type())
cacheClientSizeHistBinNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheClientSizeHistBinNumber.setStatus(_A)
_CacheClientReqSize_Type=Integer32
_CacheClientReqSize_Object=MibTableColumn
cacheClientReqSize=_CacheClientReqSize_Object((1,3,6,1,4,1,15497,1,2,3,2,1,1,2),_CacheClientReqSize_Type())
cacheClientReqSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheClientReqSize.setStatus(_A)
_CacheClientRequests_Type=Counter32
_CacheClientRequests_Object=MibScalar
cacheClientRequests=_CacheClientRequests_Object((1,3,6,1,4,1,15497,1,2,3,2,2),_CacheClientRequests_Type())
cacheClientRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheClientRequests.setStatus(_A)
_CacheClientHits_Type=Counter32
_CacheClientHits_Object=MibScalar
cacheClientHits=_CacheClientHits_Object((1,3,6,1,4,1,15497,1,2,3,2,3),_CacheClientHits_Type())
cacheClientHits.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheClientHits.setStatus(_A)
_CacheClientErrors_Type=Counter32
_CacheClientErrors_Object=MibScalar
cacheClientErrors=_CacheClientErrors_Object((1,3,6,1,4,1,15497,1,2,3,2,4),_CacheClientErrors_Type())
cacheClientErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheClientErrors.setStatus(_A)
_CacheClientInKb_Type=Counter32
_CacheClientInKb_Object=MibScalar
cacheClientInKb=_CacheClientInKb_Object((1,3,6,1,4,1,15497,1,2,3,2,5),_CacheClientInKb_Type())
cacheClientInKb.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheClientInKb.setStatus(_A)
_CacheClientOutKb_Type=Counter32
_CacheClientOutKb_Object=MibScalar
cacheClientOutKb=_CacheClientOutKb_Object((1,3,6,1,4,1,15497,1,2,3,2,6),_CacheClientOutKb_Type())
cacheClientOutKb.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheClientOutKb.setStatus(_A)
_CacheClientIdleConns_Type=Counter32
_CacheClientIdleConns_Object=MibScalar
cacheClientIdleConns=_CacheClientIdleConns_Object((1,3,6,1,4,1,15497,1,2,3,2,7),_CacheClientIdleConns_Type())
cacheClientIdleConns.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheClientIdleConns.setStatus(_A)
_CacheClientTotalConns_Type=Integer32
_CacheClientTotalConns_Object=MibScalar
cacheClientTotalConns=_CacheClientTotalConns_Object((1,3,6,1,4,1,15497,1,2,3,2,8),_CacheClientTotalConns_Type())
cacheClientTotalConns.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheClientTotalConns.setStatus(_A)
_CacheClientMaxConns_Type=Counter32
_CacheClientMaxConns_Object=MibScalar
cacheClientMaxConns=_CacheClientMaxConns_Object((1,3,6,1,4,1,15497,1,2,3,2,9),_CacheClientMaxConns_Type())
cacheClientMaxConns.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheClientMaxConns.setStatus(_A)
_CacheClientAccepts_Type=Counter32
_CacheClientAccepts_Object=MibScalar
cacheClientAccepts=_CacheClientAccepts_Object((1,3,6,1,4,1,15497,1,2,3,2,10),_CacheClientAccepts_Type())
cacheClientAccepts.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheClientAccepts.setStatus(_A)
_CacheClientICPRequests_Type=Counter32
_CacheClientICPRequests_Object=MibScalar
cacheClientICPRequests=_CacheClientICPRequests_Object((1,3,6,1,4,1,15497,1,2,3,2,11),_CacheClientICPRequests_Type())
cacheClientICPRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheClientICPRequests.setStatus(_A)
_CacheClientICPHits_Type=Counter32
_CacheClientICPHits_Object=MibScalar
cacheClientICPHits=_CacheClientICPHits_Object((1,3,6,1,4,1,15497,1,2,3,2,12),_CacheClientICPHits_Type())
cacheClientICPHits.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheClientICPHits.setStatus(_A)
_CacheClientICPMisses_Type=Counter32
_CacheClientICPMisses_Object=MibScalar
cacheClientICPMisses=_CacheClientICPMisses_Object((1,3,6,1,4,1,15497,1,2,3,2,13),_CacheClientICPMisses_Type())
cacheClientICPMisses.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheClientICPMisses.setStatus(_A)
_CacheClientICPErrors_Type=Counter32
_CacheClientICPErrors_Object=MibScalar
cacheClientICPErrors=_CacheClientICPErrors_Object((1,3,6,1,4,1,15497,1,2,3,2,14),_CacheClientICPErrors_Type())
cacheClientICPErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheClientICPErrors.setStatus(_A)
_CacheClientICPDenials_Type=Counter32
_CacheClientICPDenials_Object=MibScalar
cacheClientICPDenials=_CacheClientICPDenials_Object((1,3,6,1,4,1,15497,1,2,3,2,15),_CacheClientICPDenials_Type())
cacheClientICPDenials.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheClientICPDenials.setStatus(_A)
_CacheClientReqMisses_Type=Counter32
_CacheClientReqMisses_Object=MibScalar
cacheClientReqMisses=_CacheClientReqMisses_Object((1,3,6,1,4,1,15497,1,2,3,2,16),_CacheClientReqMisses_Type())
cacheClientReqMisses.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheClientReqMisses.setStatus(_A)
_CacheClientReqDenials_Type=Counter32
_CacheClientReqDenials_Object=MibScalar
cacheClientReqDenials=_CacheClientReqDenials_Object((1,3,6,1,4,1,15497,1,2,3,2,17),_CacheClientReqDenials_Type())
cacheClientReqDenials.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheClientReqDenials.setStatus(_A)
_ProxyServerSidePerf_ObjectIdentity=ObjectIdentity
proxyServerSidePerf=_ProxyServerSidePerf_ObjectIdentity((1,3,6,1,4,1,15497,1,2,3,3))
_CacheServerSizeHistTable_Object=MibTable
cacheServerSizeHistTable=_CacheServerSizeHistTable_Object((1,3,6,1,4,1,15497,1,2,3,3,1))
if mibBuilder.loadTexts:cacheServerSizeHistTable.setStatus(_A)
_CacheServerSizeHistEntry_Object=MibTableRow
cacheServerSizeHistEntry=_CacheServerSizeHistEntry_Object((1,3,6,1,4,1,15497,1,2,3,3,1,1))
cacheServerSizeHistEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:cacheServerSizeHistEntry.setStatus(_A)
class _CacheServerSizeHistBinNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_CacheServerSizeHistBinNumber_Type.__name__=_C
_CacheServerSizeHistBinNumber_Object=MibTableColumn
cacheServerSizeHistBinNumber=_CacheServerSizeHistBinNumber_Object((1,3,6,1,4,1,15497,1,2,3,3,1,1,1),_CacheServerSizeHistBinNumber_Type())
cacheServerSizeHistBinNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheServerSizeHistBinNumber.setStatus(_A)
_CacheServerReplySize_Type=Integer32
_CacheServerReplySize_Object=MibTableColumn
cacheServerReplySize=_CacheServerReplySize_Object((1,3,6,1,4,1,15497,1,2,3,3,1,1,2),_CacheServerReplySize_Type())
cacheServerReplySize.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheServerReplySize.setStatus(_A)
_CacheServerRequests_Type=Counter32
_CacheServerRequests_Object=MibScalar
cacheServerRequests=_CacheServerRequests_Object((1,3,6,1,4,1,15497,1,2,3,3,2),_CacheServerRequests_Type())
cacheServerRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheServerRequests.setStatus(_A)
_CacheServerSockets_Type=Counter32
_CacheServerSockets_Object=MibScalar
cacheServerSockets=_CacheServerSockets_Object((1,3,6,1,4,1,15497,1,2,3,3,3),_CacheServerSockets_Type())
cacheServerSockets.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheServerSockets.setStatus(_A)
_CacheServerErrors_Type=Counter32
_CacheServerErrors_Object=MibScalar
cacheServerErrors=_CacheServerErrors_Object((1,3,6,1,4,1,15497,1,2,3,3,4),_CacheServerErrors_Type())
cacheServerErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheServerErrors.setStatus(_A)
_CacheServerInKb_Type=Counter32
_CacheServerInKb_Object=MibScalar
cacheServerInKb=_CacheServerInKb_Object((1,3,6,1,4,1,15497,1,2,3,3,5),_CacheServerInKb_Type())
cacheServerInKb.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheServerInKb.setStatus(_A)
_CacheServerOutKb_Type=Counter32
_CacheServerOutKb_Object=MibScalar
cacheServerOutKb=_CacheServerOutKb_Object((1,3,6,1,4,1,15497,1,2,3,3,6),_CacheServerOutKb_Type())
cacheServerOutKb.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheServerOutKb.setStatus(_A)
_CacheServerIdleConns_Type=Counter32
_CacheServerIdleConns_Object=MibScalar
cacheServerIdleConns=_CacheServerIdleConns_Object((1,3,6,1,4,1,15497,1,2,3,3,7),_CacheServerIdleConns_Type())
cacheServerIdleConns.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheServerIdleConns.setStatus(_A)
_CacheServerTotalConns_Type=Counter32
_CacheServerTotalConns_Object=MibScalar
cacheServerTotalConns=_CacheServerTotalConns_Object((1,3,6,1,4,1,15497,1,2,3,3,8),_CacheServerTotalConns_Type())
cacheServerTotalConns.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheServerTotalConns.setStatus(_A)
_CacheServerCloseIdleConns_Type=Counter32
_CacheServerCloseIdleConns_Object=MibScalar
cacheServerCloseIdleConns=_CacheServerCloseIdleConns_Object((1,3,6,1,4,1,15497,1,2,3,3,9),_CacheServerCloseIdleConns_Type())
cacheServerCloseIdleConns.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheServerCloseIdleConns.setStatus(_A)
_CacheServerLimitIdleConns_Type=Counter32
_CacheServerLimitIdleConns_Object=MibScalar
cacheServerLimitIdleConns=_CacheServerLimitIdleConns_Object((1,3,6,1,4,1,15497,1,2,3,3,10),_CacheServerLimitIdleConns_Type())
cacheServerLimitIdleConns.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheServerLimitIdleConns.setStatus(_A)
_CacheServerConnsThresh_Type=Counter32
_CacheServerConnsThresh_Object=MibScalar
cacheServerConnsThresh=_CacheServerConnsThresh_Object((1,3,6,1,4,1,15497,1,2,3,3,11),_CacheServerConnsThresh_Type())
cacheServerConnsThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheServerConnsThresh.setStatus(_A)
_CacheServerPersisConnsRetries_Type=Counter32
_CacheServerPersisConnsRetries_Object=MibScalar
cacheServerPersisConnsRetries=_CacheServerPersisConnsRetries_Object((1,3,6,1,4,1,15497,1,2,3,3,12),_CacheServerPersisConnsRetries_Type())
cacheServerPersisConnsRetries.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheServerPersisConnsRetries.setStatus(_A)
_CacheServerRegConnsRetries_Type=Counter32
_CacheServerRegConnsRetries_Object=MibScalar
cacheServerRegConnsRetries=_CacheServerRegConnsRetries_Object((1,3,6,1,4,1,15497,1,2,3,3,13),_CacheServerRegConnsRetries_Type())
cacheServerRegConnsRetries.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheServerRegConnsRetries.setStatus(_A)
_CacheServerRWErrorRetries_Type=Counter32
_CacheServerRWErrorRetries_Object=MibScalar
cacheServerRWErrorRetries=_CacheServerRWErrorRetries_Object((1,3,6,1,4,1,15497,1,2,3,3,14),_CacheServerRWErrorRetries_Type())
cacheServerRWErrorRetries.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheServerRWErrorRetries.setStatus(_A)
_CacheServerEarlyCloseRetries_Type=Counter32
_CacheServerEarlyCloseRetries_Object=MibScalar
cacheServerEarlyCloseRetries=_CacheServerEarlyCloseRetries_Object((1,3,6,1,4,1,15497,1,2,3,3,15),_CacheServerEarlyCloseRetries_Type())
cacheServerEarlyCloseRetries.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheServerEarlyCloseRetries.setStatus(_A)
_CacheServerICPRequests_Type=Counter32
_CacheServerICPRequests_Object=MibScalar
cacheServerICPRequests=_CacheServerICPRequests_Object((1,3,6,1,4,1,15497,1,2,3,3,16),_CacheServerICPRequests_Type())
cacheServerICPRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheServerICPRequests.setStatus(_A)
_CacheServerICPHits_Type=Counter32
_CacheServerICPHits_Object=MibScalar
cacheServerICPHits=_CacheServerICPHits_Object((1,3,6,1,4,1,15497,1,2,3,3,17),_CacheServerICPHits_Type())
cacheServerICPHits.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheServerICPHits.setStatus(_A)
_CacheServerICPMisses_Type=Counter32
_CacheServerICPMisses_Object=MibScalar
cacheServerICPMisses=_CacheServerICPMisses_Object((1,3,6,1,4,1,15497,1,2,3,3,18),_CacheServerICPMisses_Type())
cacheServerICPMisses.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheServerICPMisses.setStatus(_A)
_CacheServerICPErrors_Type=Counter32
_CacheServerICPErrors_Object=MibScalar
cacheServerICPErrors=_CacheServerICPErrors_Object((1,3,6,1,4,1,15497,1,2,3,3,19),_CacheServerICPErrors_Type())
cacheServerICPErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheServerICPErrors.setStatus(_A)
_CacheServerICPDenials_Type=Counter32
_CacheServerICPDenials_Object=MibScalar
cacheServerICPDenials=_CacheServerICPDenials_Object((1,3,6,1,4,1,15497,1,2,3,3,20),_CacheServerICPDenials_Type())
cacheServerICPDenials.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheServerICPDenials.setStatus(_A)
_ProxyCachePerf_ObjectIdentity=ObjectIdentity
proxyCachePerf=_ProxyCachePerf_ObjectIdentity((1,3,6,1,4,1,15497,1,2,3,4))
_CacheCacheSizeHistTable_Object=MibTable
cacheCacheSizeHistTable=_CacheCacheSizeHistTable_Object((1,3,6,1,4,1,15497,1,2,3,4,1))
if mibBuilder.loadTexts:cacheCacheSizeHistTable.setStatus(_A)
_CacheCacheSizeHistEntry_Object=MibTableRow
cacheCacheSizeHistEntry=_CacheCacheSizeHistEntry_Object((1,3,6,1,4,1,15497,1,2,3,4,1,1))
cacheCacheSizeHistEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:cacheCacheSizeHistEntry.setStatus(_A)
class _CacheSizeHistBinNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_CacheSizeHistBinNumber_Type.__name__=_C
_CacheSizeHistBinNumber_Object=MibTableColumn
cacheSizeHistBinNumber=_CacheSizeHistBinNumber_Object((1,3,6,1,4,1,15497,1,2,3,4,1,1,1),_CacheSizeHistBinNumber_Type())
cacheSizeHistBinNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheSizeHistBinNumber.setStatus(_A)
_CacheCacheActiveObjs_Type=Integer32
_CacheCacheActiveObjs_Object=MibTableColumn
cacheCacheActiveObjs=_CacheCacheActiveObjs_Object((1,3,6,1,4,1,15497,1,2,3,4,1,1,2),_CacheCacheActiveObjs_Type())
cacheCacheActiveObjs.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheCacheActiveObjs.setStatus(_A)
_CacheCacheAllObjs_Type=Integer32
_CacheCacheAllObjs_Object=MibTableColumn
cacheCacheAllObjs=_CacheCacheAllObjs_Object((1,3,6,1,4,1,15497,1,2,3,4,1,1,3),_CacheCacheAllObjs_Type())
cacheCacheAllObjs.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheCacheAllObjs.setStatus(_A)
_CacheCacheLiveCachedObjs_Type=Counter32
_CacheCacheLiveCachedObjs_Object=MibScalar
cacheCacheLiveCachedObjs=_CacheCacheLiveCachedObjs_Object((1,3,6,1,4,1,15497,1,2,3,4,2),_CacheCacheLiveCachedObjs_Type())
cacheCacheLiveCachedObjs.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheCacheLiveCachedObjs.setStatus(_A)
_CacheCacheLiveCachedObjSizes_Type=Counter32
_CacheCacheLiveCachedObjSizes_Object=MibScalar
cacheCacheLiveCachedObjSizes=_CacheCacheLiveCachedObjSizes_Object((1,3,6,1,4,1,15497,1,2,3,4,3),_CacheCacheLiveCachedObjSizes_Type())
cacheCacheLiveCachedObjSizes.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheCacheLiveCachedObjSizes.setStatus(_A)
_CacheCacheTotalCachedObjs_Type=Counter32
_CacheCacheTotalCachedObjs_Object=MibScalar
cacheCacheTotalCachedObjs=_CacheCacheTotalCachedObjs_Object((1,3,6,1,4,1,15497,1,2,3,4,4),_CacheCacheTotalCachedObjs_Type())
cacheCacheTotalCachedObjs.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheCacheTotalCachedObjs.setStatus(_A)
_CacheCacheTotalCachedObjSizes_Type=Counter32
_CacheCacheTotalCachedObjSizes_Object=MibScalar
cacheCacheTotalCachedObjSizes=_CacheCacheTotalCachedObjSizes_Object((1,3,6,1,4,1,15497,1,2,3,4,5),_CacheCacheTotalCachedObjSizes_Type())
cacheCacheTotalCachedObjSizes.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheCacheTotalCachedObjSizes.setStatus(_A)
_ProxyMedianSvcTime_ObjectIdentity=ObjectIdentity
proxyMedianSvcTime=_ProxyMedianSvcTime_ObjectIdentity((1,3,6,1,4,1,15497,1,2,3,5))
_CacheMedianSvcTable_Object=MibTable
cacheMedianSvcTable=_CacheMedianSvcTable_Object((1,3,6,1,4,1,15497,1,2,3,5,1))
if mibBuilder.loadTexts:cacheMedianSvcTable.setStatus(_A)
_CacheMedianSvcEntry_Object=MibTableRow
cacheMedianSvcEntry=_CacheMedianSvcEntry_Object((1,3,6,1,4,1,15497,1,2,3,5,1,1))
cacheMedianSvcEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:cacheMedianSvcEntry.setStatus(_A)
class _CacheMedianTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_CacheMedianTime_Type.__name__=_C
_CacheMedianTime_Object=MibTableColumn
cacheMedianTime=_CacheMedianTime_Object((1,3,6,1,4,1,15497,1,2,3,5,1,1,1),_CacheMedianTime_Type())
cacheMedianTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheMedianTime.setStatus(_A)
_CacheHTTPCltSvcTime_Type=Integer32
_CacheHTTPCltSvcTime_Object=MibTableColumn
cacheHTTPCltSvcTime=_CacheHTTPCltSvcTime_Object((1,3,6,1,4,1,15497,1,2,3,5,1,1,2),_CacheHTTPCltSvcTime_Type())
cacheHTTPCltSvcTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheHTTPCltSvcTime.setStatus(_A)
_CacheHTTPMissSvcTime_Type=Integer32
_CacheHTTPMissSvcTime_Object=MibTableColumn
cacheHTTPMissSvcTime=_CacheHTTPMissSvcTime_Object((1,3,6,1,4,1,15497,1,2,3,5,1,1,3),_CacheHTTPMissSvcTime_Type())
cacheHTTPMissSvcTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheHTTPMissSvcTime.setStatus(_A)
_CacheHTTPHitSvcTime_Type=Integer32
_CacheHTTPHitSvcTime_Object=MibTableColumn
cacheHTTPHitSvcTime=_CacheHTTPHitSvcTime_Object((1,3,6,1,4,1,15497,1,2,3,5,1,1,4),_CacheHTTPHitSvcTime_Type())
cacheHTTPHitSvcTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheHTTPHitSvcTime.setStatus(_A)
_CacheHTTPSrvSvcTime_Type=Integer32
_CacheHTTPSrvSvcTime_Object=MibTableColumn
cacheHTTPSrvSvcTime=_CacheHTTPSrvSvcTime_Object((1,3,6,1,4,1,15497,1,2,3,5,1,1,5),_CacheHTTPSrvSvcTime_Type())
cacheHTTPSrvSvcTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheHTTPSrvSvcTime.setStatus(_A)
_CacheDnsSvcTime_Type=Integer32
_CacheDnsSvcTime_Object=MibTableColumn
cacheDnsSvcTime=_CacheDnsSvcTime_Object((1,3,6,1,4,1,15497,1,2,3,5,1,1,6),_CacheDnsSvcTime_Type())
cacheDnsSvcTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheDnsSvcTime.setStatus(_A)
_CacheHTTPSvcWaitTime_Type=Integer32
_CacheHTTPSvcWaitTime_Object=MibScalar
cacheHTTPSvcWaitTime=_CacheHTTPSvcWaitTime_Object((1,3,6,1,4,1,15497,1,2,3,5,1,1,7),_CacheHTTPSvcWaitTime_Type())
cacheHTTPSvcWaitTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheHTTPSvcWaitTime.setStatus(_A)
_ProxyExecutiveSummary_ObjectIdentity=ObjectIdentity
proxyExecutiveSummary=_ProxyExecutiveSummary_ObjectIdentity((1,3,6,1,4,1,15497,1,2,3,6))
_CacheTotalHttpReqs_Type=Integer32
_CacheTotalHttpReqs_Object=MibScalar
cacheTotalHttpReqs=_CacheTotalHttpReqs_Object((1,3,6,1,4,1,15497,1,2,3,6,1),_CacheTotalHttpReqs_Type())
cacheTotalHttpReqs.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheTotalHttpReqs.setStatus(_A)
_CacheMeanRespTime_Type=Integer32
_CacheMeanRespTime_Object=MibScalar
cacheMeanRespTime=_CacheMeanRespTime_Object((1,3,6,1,4,1,15497,1,2,3,6,2),_CacheMeanRespTime_Type())
cacheMeanRespTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheMeanRespTime.setStatus(_A)
_CacheMeanMissRespTime_Type=Integer32
_CacheMeanMissRespTime_Object=MibScalar
cacheMeanMissRespTime=_CacheMeanMissRespTime_Object((1,3,6,1,4,1,15497,1,2,3,6,3),_CacheMeanMissRespTime_Type())
cacheMeanMissRespTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheMeanMissRespTime.setStatus(_A)
_CacheMeanHitRespTime_Type=Integer32
_CacheMeanHitRespTime_Object=MibScalar
cacheMeanHitRespTime=_CacheMeanHitRespTime_Object((1,3,6,1,4,1,15497,1,2,3,6,4),_CacheMeanHitRespTime_Type())
cacheMeanHitRespTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheMeanHitRespTime.setStatus(_A)
_CacheMeanHitRatio_Type=Integer32
_CacheMeanHitRatio_Object=MibScalar
cacheMeanHitRatio=_CacheMeanHitRatio_Object((1,3,6,1,4,1,15497,1,2,3,6,5),_CacheMeanHitRatio_Type())
cacheMeanHitRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheMeanHitRatio.setStatus(_A)
_CacheMeanByteHitRatio_Type=Integer32
_CacheMeanByteHitRatio_Object=MibScalar
cacheMeanByteHitRatio=_CacheMeanByteHitRatio_Object((1,3,6,1,4,1,15497,1,2,3,6,6),_CacheMeanByteHitRatio_Type())
cacheMeanByteHitRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheMeanByteHitRatio.setStatus(_A)
_CacheTotalBandwidthSaving_Type=Integer32
_CacheTotalBandwidthSaving_Object=MibScalar
cacheTotalBandwidthSaving=_CacheTotalBandwidthSaving_Object((1,3,6,1,4,1,15497,1,2,3,6,7),_CacheTotalBandwidthSaving_Type())
cacheTotalBandwidthSaving.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheTotalBandwidthSaving.setStatus(_A)
_CacheDuration_Type=Integer32
_CacheDuration_Object=MibScalar
cacheDuration=_CacheDuration_Object((1,3,6,1,4,1,15497,1,2,3,6,8),_CacheDuration_Type())
cacheDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheDuration.setStatus(_A)
_CacheCltReplyErrPct_Type=Integer32
_CacheCltReplyErrPct_Object=MibScalar
cacheCltReplyErrPct=_CacheCltReplyErrPct_Object((1,3,6,1,4,1,15497,1,2,3,6,9),_CacheCltReplyErrPct_Type())
cacheCltReplyErrPct.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheCltReplyErrPct.setStatus(_A)
_ProxyRecentPerf_ObjectIdentity=ObjectIdentity
proxyRecentPerf=_ProxyRecentPerf_ObjectIdentity((1,3,6,1,4,1,15497,1,2,3,7))
_ProxyRecentThruputPerf_ObjectIdentity=ObjectIdentity
proxyRecentThruputPerf=_ProxyRecentThruputPerf_ObjectIdentity((1,3,6,1,4,1,15497,1,2,3,7,1))
_CacheThruputNow_Type=Integer32
_CacheThruputNow_Object=MibScalar
cacheThruputNow=_CacheThruputNow_Object((1,3,6,1,4,1,15497,1,2,3,7,1,1),_CacheThruputNow_Type())
cacheThruputNow.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheThruputNow.setStatus(_A)
_CacheThruput1hrPeak_Type=Integer32
_CacheThruput1hrPeak_Object=MibScalar
cacheThruput1hrPeak=_CacheThruput1hrPeak_Object((1,3,6,1,4,1,15497,1,2,3,7,1,2),_CacheThruput1hrPeak_Type())
cacheThruput1hrPeak.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheThruput1hrPeak.setStatus(_A)
_CacheThruput1hrMean_Type=Integer32
_CacheThruput1hrMean_Object=MibScalar
cacheThruput1hrMean=_CacheThruput1hrMean_Object((1,3,6,1,4,1,15497,1,2,3,7,1,3),_CacheThruput1hrMean_Type())
cacheThruput1hrMean.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheThruput1hrMean.setStatus(_A)
_CacheThruput1dayPeak_Type=Integer32
_CacheThruput1dayPeak_Object=MibScalar
cacheThruput1dayPeak=_CacheThruput1dayPeak_Object((1,3,6,1,4,1,15497,1,2,3,7,1,4),_CacheThruput1dayPeak_Type())
cacheThruput1dayPeak.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheThruput1dayPeak.setStatus(_A)
_CacheThruput1dayMean_Type=Integer32
_CacheThruput1dayMean_Object=MibScalar
cacheThruput1dayMean=_CacheThruput1dayMean_Object((1,3,6,1,4,1,15497,1,2,3,7,1,5),_CacheThruput1dayMean_Type())
cacheThruput1dayMean.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheThruput1dayMean.setStatus(_A)
_CacheThruput1weekPeak_Type=Integer32
_CacheThruput1weekPeak_Object=MibScalar
cacheThruput1weekPeak=_CacheThruput1weekPeak_Object((1,3,6,1,4,1,15497,1,2,3,7,1,6),_CacheThruput1weekPeak_Type())
cacheThruput1weekPeak.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheThruput1weekPeak.setStatus(_A)
_CacheThruput1weekMean_Type=Integer32
_CacheThruput1weekMean_Object=MibScalar
cacheThruput1weekMean=_CacheThruput1weekMean_Object((1,3,6,1,4,1,15497,1,2,3,7,1,7),_CacheThruput1weekMean_Type())
cacheThruput1weekMean.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheThruput1weekMean.setStatus(_A)
_CacheThruputLifePeak_Type=Integer32
_CacheThruputLifePeak_Object=MibScalar
cacheThruputLifePeak=_CacheThruputLifePeak_Object((1,3,6,1,4,1,15497,1,2,3,7,1,8),_CacheThruputLifePeak_Type())
cacheThruputLifePeak.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheThruputLifePeak.setStatus(_A)
_CacheThruputLifeMean_Type=Integer32
_CacheThruputLifeMean_Object=MibScalar
cacheThruputLifeMean=_CacheThruputLifeMean_Object((1,3,6,1,4,1,15497,1,2,3,7,1,9),_CacheThruputLifeMean_Type())
cacheThruputLifeMean.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheThruputLifeMean.setStatus(_A)
_ProxyRecentBandWSavPerf_ObjectIdentity=ObjectIdentity
proxyRecentBandWSavPerf=_ProxyRecentBandWSavPerf_ObjectIdentity((1,3,6,1,4,1,15497,1,2,3,7,2))
_CacheBwidthSavingNow_Type=Integer32
_CacheBwidthSavingNow_Object=MibScalar
cacheBwidthSavingNow=_CacheBwidthSavingNow_Object((1,3,6,1,4,1,15497,1,2,3,7,2,1),_CacheBwidthSavingNow_Type())
cacheBwidthSavingNow.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheBwidthSavingNow.setStatus(_A)
_CacheBwidthSaving1hrPeak_Type=Integer32
_CacheBwidthSaving1hrPeak_Object=MibScalar
cacheBwidthSaving1hrPeak=_CacheBwidthSaving1hrPeak_Object((1,3,6,1,4,1,15497,1,2,3,7,2,2),_CacheBwidthSaving1hrPeak_Type())
cacheBwidthSaving1hrPeak.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheBwidthSaving1hrPeak.setStatus(_A)
_CacheBwidthSaving1hrMean_Type=Integer32
_CacheBwidthSaving1hrMean_Object=MibScalar
cacheBwidthSaving1hrMean=_CacheBwidthSaving1hrMean_Object((1,3,6,1,4,1,15497,1,2,3,7,2,3),_CacheBwidthSaving1hrMean_Type())
cacheBwidthSaving1hrMean.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheBwidthSaving1hrMean.setStatus(_A)
_CacheBwidthSaving1dayPeak_Type=Integer32
_CacheBwidthSaving1dayPeak_Object=MibScalar
cacheBwidthSaving1dayPeak=_CacheBwidthSaving1dayPeak_Object((1,3,6,1,4,1,15497,1,2,3,7,2,4),_CacheBwidthSaving1dayPeak_Type())
cacheBwidthSaving1dayPeak.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheBwidthSaving1dayPeak.setStatus(_A)
_CacheBwidthSaving1dayMean_Type=Integer32
_CacheBwidthSaving1dayMean_Object=MibScalar
cacheBwidthSaving1dayMean=_CacheBwidthSaving1dayMean_Object((1,3,6,1,4,1,15497,1,2,3,7,2,5),_CacheBwidthSaving1dayMean_Type())
cacheBwidthSaving1dayMean.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheBwidthSaving1dayMean.setStatus(_A)
_CacheBwidthSaving1weekPeak_Type=Integer32
_CacheBwidthSaving1weekPeak_Object=MibScalar
cacheBwidthSaving1weekPeak=_CacheBwidthSaving1weekPeak_Object((1,3,6,1,4,1,15497,1,2,3,7,2,6),_CacheBwidthSaving1weekPeak_Type())
cacheBwidthSaving1weekPeak.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheBwidthSaving1weekPeak.setStatus(_A)
_CacheBwidthSaving1weekMean_Type=Integer32
_CacheBwidthSaving1weekMean_Object=MibScalar
cacheBwidthSaving1weekMean=_CacheBwidthSaving1weekMean_Object((1,3,6,1,4,1,15497,1,2,3,7,2,7),_CacheBwidthSaving1weekMean_Type())
cacheBwidthSaving1weekMean.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheBwidthSaving1weekMean.setStatus(_A)
_CacheBwidthSavingLifePeak_Type=Integer32
_CacheBwidthSavingLifePeak_Object=MibScalar
cacheBwidthSavingLifePeak=_CacheBwidthSavingLifePeak_Object((1,3,6,1,4,1,15497,1,2,3,7,2,8),_CacheBwidthSavingLifePeak_Type())
cacheBwidthSavingLifePeak.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheBwidthSavingLifePeak.setStatus(_A)
_CacheBwidthSavingLifeMean_Type=Integer32
_CacheBwidthSavingLifeMean_Object=MibScalar
cacheBwidthSavingLifeMean=_CacheBwidthSavingLifeMean_Object((1,3,6,1,4,1,15497,1,2,3,7,2,9),_CacheBwidthSavingLifeMean_Type())
cacheBwidthSavingLifeMean.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheBwidthSavingLifeMean.setStatus(_A)
_ProxyRecentBandWSpntPerf_ObjectIdentity=ObjectIdentity
proxyRecentBandWSpntPerf=_ProxyRecentBandWSpntPerf_ObjectIdentity((1,3,6,1,4,1,15497,1,2,3,7,3))
_CacheBwidthSpentNow_Type=Integer32
_CacheBwidthSpentNow_Object=MibScalar
cacheBwidthSpentNow=_CacheBwidthSpentNow_Object((1,3,6,1,4,1,15497,1,2,3,7,3,1),_CacheBwidthSpentNow_Type())
cacheBwidthSpentNow.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheBwidthSpentNow.setStatus(_A)
_CacheBwidthSpent1hrPeak_Type=Integer32
_CacheBwidthSpent1hrPeak_Object=MibScalar
cacheBwidthSpent1hrPeak=_CacheBwidthSpent1hrPeak_Object((1,3,6,1,4,1,15497,1,2,3,7,3,2),_CacheBwidthSpent1hrPeak_Type())
cacheBwidthSpent1hrPeak.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheBwidthSpent1hrPeak.setStatus(_A)
_CacheBwidthSpent1hrMean_Type=Integer32
_CacheBwidthSpent1hrMean_Object=MibScalar
cacheBwidthSpent1hrMean=_CacheBwidthSpent1hrMean_Object((1,3,6,1,4,1,15497,1,2,3,7,3,3),_CacheBwidthSpent1hrMean_Type())
cacheBwidthSpent1hrMean.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheBwidthSpent1hrMean.setStatus(_A)
_CacheBwidthSpent1dayPeak_Type=Integer32
_CacheBwidthSpent1dayPeak_Object=MibScalar
cacheBwidthSpent1dayPeak=_CacheBwidthSpent1dayPeak_Object((1,3,6,1,4,1,15497,1,2,3,7,3,4),_CacheBwidthSpent1dayPeak_Type())
cacheBwidthSpent1dayPeak.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheBwidthSpent1dayPeak.setStatus(_A)
_CacheBwidthSpent1dayMean_Type=Integer32
_CacheBwidthSpent1dayMean_Object=MibScalar
cacheBwidthSpent1dayMean=_CacheBwidthSpent1dayMean_Object((1,3,6,1,4,1,15497,1,2,3,7,3,5),_CacheBwidthSpent1dayMean_Type())
cacheBwidthSpent1dayMean.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheBwidthSpent1dayMean.setStatus(_A)
_CacheBwidthSpent1weekPeak_Type=Integer32
_CacheBwidthSpent1weekPeak_Object=MibScalar
cacheBwidthSpent1weekPeak=_CacheBwidthSpent1weekPeak_Object((1,3,6,1,4,1,15497,1,2,3,7,3,6),_CacheBwidthSpent1weekPeak_Type())
cacheBwidthSpent1weekPeak.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheBwidthSpent1weekPeak.setStatus(_A)
_CacheBwidthSpent1weekMean_Type=Integer32
_CacheBwidthSpent1weekMean_Object=MibScalar
cacheBwidthSpent1weekMean=_CacheBwidthSpent1weekMean_Object((1,3,6,1,4,1,15497,1,2,3,7,3,7),_CacheBwidthSpent1weekMean_Type())
cacheBwidthSpent1weekMean.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheBwidthSpent1weekMean.setStatus(_A)
_CacheBwidthSpentLifePeak_Type=Integer32
_CacheBwidthSpentLifePeak_Object=MibScalar
cacheBwidthSpentLifePeak=_CacheBwidthSpentLifePeak_Object((1,3,6,1,4,1,15497,1,2,3,7,3,8),_CacheBwidthSpentLifePeak_Type())
cacheBwidthSpentLifePeak.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheBwidthSpentLifePeak.setStatus(_A)
_CacheBwidthSpentLifeMean_Type=Integer32
_CacheBwidthSpentLifeMean_Object=MibScalar
cacheBwidthSpentLifeMean=_CacheBwidthSpentLifeMean_Object((1,3,6,1,4,1,15497,1,2,3,7,3,9),_CacheBwidthSpentLifeMean_Type())
cacheBwidthSpentLifeMean.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheBwidthSpentLifeMean.setStatus(_A)
_ProxyRecentBandWTotPerf_ObjectIdentity=ObjectIdentity
proxyRecentBandWTotPerf=_ProxyRecentBandWTotPerf_ObjectIdentity((1,3,6,1,4,1,15497,1,2,3,7,4))
_CacheBwidthTotalNow_Type=Integer32
_CacheBwidthTotalNow_Object=MibScalar
cacheBwidthTotalNow=_CacheBwidthTotalNow_Object((1,3,6,1,4,1,15497,1,2,3,7,4,1),_CacheBwidthTotalNow_Type())
cacheBwidthTotalNow.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheBwidthTotalNow.setStatus(_A)
_CacheBwidthTotal1hrPeak_Type=Integer32
_CacheBwidthTotal1hrPeak_Object=MibScalar
cacheBwidthTotal1hrPeak=_CacheBwidthTotal1hrPeak_Object((1,3,6,1,4,1,15497,1,2,3,7,4,2),_CacheBwidthTotal1hrPeak_Type())
cacheBwidthTotal1hrPeak.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheBwidthTotal1hrPeak.setStatus(_A)
_CacheBwidthTotal1hrMean_Type=Integer32
_CacheBwidthTotal1hrMean_Object=MibScalar
cacheBwidthTotal1hrMean=_CacheBwidthTotal1hrMean_Object((1,3,6,1,4,1,15497,1,2,3,7,4,3),_CacheBwidthTotal1hrMean_Type())
cacheBwidthTotal1hrMean.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheBwidthTotal1hrMean.setStatus(_A)
_CacheBwidthTotal1dayPeak_Type=Integer32
_CacheBwidthTotal1dayPeak_Object=MibScalar
cacheBwidthTotal1dayPeak=_CacheBwidthTotal1dayPeak_Object((1,3,6,1,4,1,15497,1,2,3,7,4,4),_CacheBwidthTotal1dayPeak_Type())
cacheBwidthTotal1dayPeak.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheBwidthTotal1dayPeak.setStatus(_A)
_CacheBwidthTotal1dayMean_Type=Integer32
_CacheBwidthTotal1dayMean_Object=MibScalar
cacheBwidthTotal1dayMean=_CacheBwidthTotal1dayMean_Object((1,3,6,1,4,1,15497,1,2,3,7,4,5),_CacheBwidthTotal1dayMean_Type())
cacheBwidthTotal1dayMean.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheBwidthTotal1dayMean.setStatus(_A)
_CacheBwidthTotal1weekPeak_Type=Integer32
_CacheBwidthTotal1weekPeak_Object=MibScalar
cacheBwidthTotal1weekPeak=_CacheBwidthTotal1weekPeak_Object((1,3,6,1,4,1,15497,1,2,3,7,4,6),_CacheBwidthTotal1weekPeak_Type())
cacheBwidthTotal1weekPeak.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheBwidthTotal1weekPeak.setStatus(_A)
_CacheBwidthTotal1weekMean_Type=Integer32
_CacheBwidthTotal1weekMean_Object=MibScalar
cacheBwidthTotal1weekMean=_CacheBwidthTotal1weekMean_Object((1,3,6,1,4,1,15497,1,2,3,7,4,7),_CacheBwidthTotal1weekMean_Type())
cacheBwidthTotal1weekMean.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheBwidthTotal1weekMean.setStatus(_A)
_CacheBwidthTotalLifePeak_Type=Integer32
_CacheBwidthTotalLifePeak_Object=MibScalar
cacheBwidthTotalLifePeak=_CacheBwidthTotalLifePeak_Object((1,3,6,1,4,1,15497,1,2,3,7,4,8),_CacheBwidthTotalLifePeak_Type())
cacheBwidthTotalLifePeak.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheBwidthTotalLifePeak.setStatus(_A)
_CacheBwidthTotalLifeMean_Type=Integer32
_CacheBwidthTotalLifeMean_Object=MibScalar
cacheBwidthTotalLifeMean=_CacheBwidthTotalLifeMean_Object((1,3,6,1,4,1,15497,1,2,3,7,4,9),_CacheBwidthTotalLifeMean_Type())
cacheBwidthTotalLifeMean.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheBwidthTotalLifeMean.setStatus(_A)
_ProxyRecentHitsPerf_ObjectIdentity=ObjectIdentity
proxyRecentHitsPerf=_ProxyRecentHitsPerf_ObjectIdentity((1,3,6,1,4,1,15497,1,2,3,7,5))
_CacheHitsNow_Type=Integer32
_CacheHitsNow_Object=MibScalar
cacheHitsNow=_CacheHitsNow_Object((1,3,6,1,4,1,15497,1,2,3,7,5,1),_CacheHitsNow_Type())
cacheHitsNow.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheHitsNow.setStatus(_A)
_CacheHits1hrPeak_Type=Integer32
_CacheHits1hrPeak_Object=MibScalar
cacheHits1hrPeak=_CacheHits1hrPeak_Object((1,3,6,1,4,1,15497,1,2,3,7,5,2),_CacheHits1hrPeak_Type())
cacheHits1hrPeak.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheHits1hrPeak.setStatus(_A)
_CacheHits1hrMean_Type=Integer32
_CacheHits1hrMean_Object=MibScalar
cacheHits1hrMean=_CacheHits1hrMean_Object((1,3,6,1,4,1,15497,1,2,3,7,5,3),_CacheHits1hrMean_Type())
cacheHits1hrMean.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheHits1hrMean.setStatus(_A)
_CacheHits1dayPeak_Type=Integer32
_CacheHits1dayPeak_Object=MibScalar
cacheHits1dayPeak=_CacheHits1dayPeak_Object((1,3,6,1,4,1,15497,1,2,3,7,5,4),_CacheHits1dayPeak_Type())
cacheHits1dayPeak.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheHits1dayPeak.setStatus(_A)
_CacheHits1dayMean_Type=Integer32
_CacheHits1dayMean_Object=MibScalar
cacheHits1dayMean=_CacheHits1dayMean_Object((1,3,6,1,4,1,15497,1,2,3,7,5,5),_CacheHits1dayMean_Type())
cacheHits1dayMean.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheHits1dayMean.setStatus(_A)
_CacheHits1weekPeak_Type=Integer32
_CacheHits1weekPeak_Object=MibScalar
cacheHits1weekPeak=_CacheHits1weekPeak_Object((1,3,6,1,4,1,15497,1,2,3,7,5,6),_CacheHits1weekPeak_Type())
cacheHits1weekPeak.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheHits1weekPeak.setStatus(_A)
_CacheHits1weekMean_Type=Integer32
_CacheHits1weekMean_Object=MibScalar
cacheHits1weekMean=_CacheHits1weekMean_Object((1,3,6,1,4,1,15497,1,2,3,7,5,7),_CacheHits1weekMean_Type())
cacheHits1weekMean.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheHits1weekMean.setStatus(_A)
_CacheHitsLifePeak_Type=Integer32
_CacheHitsLifePeak_Object=MibScalar
cacheHitsLifePeak=_CacheHitsLifePeak_Object((1,3,6,1,4,1,15497,1,2,3,7,5,8),_CacheHitsLifePeak_Type())
cacheHitsLifePeak.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheHitsLifePeak.setStatus(_A)
_CacheHitsLifeMean_Type=Integer32
_CacheHitsLifeMean_Object=MibScalar
cacheHitsLifeMean=_CacheHitsLifeMean_Object((1,3,6,1,4,1,15497,1,2,3,7,5,9),_CacheHitsLifeMean_Type())
cacheHitsLifeMean.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheHitsLifeMean.setStatus(_A)
_ProxyRecentMissesPerf_ObjectIdentity=ObjectIdentity
proxyRecentMissesPerf=_ProxyRecentMissesPerf_ObjectIdentity((1,3,6,1,4,1,15497,1,2,3,7,6))
_CacheMissesNow_Type=Integer32
_CacheMissesNow_Object=MibScalar
cacheMissesNow=_CacheMissesNow_Object((1,3,6,1,4,1,15497,1,2,3,7,6,1),_CacheMissesNow_Type())
cacheMissesNow.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheMissesNow.setStatus(_A)
_CacheMisses1hrPeak_Type=Integer32
_CacheMisses1hrPeak_Object=MibScalar
cacheMisses1hrPeak=_CacheMisses1hrPeak_Object((1,3,6,1,4,1,15497,1,2,3,7,6,2),_CacheMisses1hrPeak_Type())
cacheMisses1hrPeak.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheMisses1hrPeak.setStatus(_A)
_CacheMisses1hrMean_Type=Integer32
_CacheMisses1hrMean_Object=MibScalar
cacheMisses1hrMean=_CacheMisses1hrMean_Object((1,3,6,1,4,1,15497,1,2,3,7,6,3),_CacheMisses1hrMean_Type())
cacheMisses1hrMean.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheMisses1hrMean.setStatus(_A)
_CacheMisses1dayPeak_Type=Integer32
_CacheMisses1dayPeak_Object=MibScalar
cacheMisses1dayPeak=_CacheMisses1dayPeak_Object((1,3,6,1,4,1,15497,1,2,3,7,6,4),_CacheMisses1dayPeak_Type())
cacheMisses1dayPeak.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheMisses1dayPeak.setStatus(_A)
_CacheMisses1dayMean_Type=Integer32
_CacheMisses1dayMean_Object=MibScalar
cacheMisses1dayMean=_CacheMisses1dayMean_Object((1,3,6,1,4,1,15497,1,2,3,7,6,5),_CacheMisses1dayMean_Type())
cacheMisses1dayMean.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheMisses1dayMean.setStatus(_A)
_CacheMisses1weekPeak_Type=Integer32
_CacheMisses1weekPeak_Object=MibScalar
cacheMisses1weekPeak=_CacheMisses1weekPeak_Object((1,3,6,1,4,1,15497,1,2,3,7,6,6),_CacheMisses1weekPeak_Type())
cacheMisses1weekPeak.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheMisses1weekPeak.setStatus(_A)
_CacheMisses1weekMean_Type=Integer32
_CacheMisses1weekMean_Object=MibScalar
cacheMisses1weekMean=_CacheMisses1weekMean_Object((1,3,6,1,4,1,15497,1,2,3,7,6,7),_CacheMisses1weekMean_Type())
cacheMisses1weekMean.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheMisses1weekMean.setStatus(_A)
_CacheMissesLifePeak_Type=Integer32
_CacheMissesLifePeak_Object=MibScalar
cacheMissesLifePeak=_CacheMissesLifePeak_Object((1,3,6,1,4,1,15497,1,2,3,7,6,8),_CacheMissesLifePeak_Type())
cacheMissesLifePeak.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheMissesLifePeak.setStatus(_A)
_CacheMissesLifeMean_Type=Integer32
_CacheMissesLifeMean_Object=MibScalar
cacheMissesLifeMean=_CacheMissesLifeMean_Object((1,3,6,1,4,1,15497,1,2,3,7,6,9),_CacheMissesLifeMean_Type())
cacheMissesLifeMean.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheMissesLifeMean.setStatus(_A)
_ProxyRecentHitRespTimePerf_ObjectIdentity=ObjectIdentity
proxyRecentHitRespTimePerf=_ProxyRecentHitRespTimePerf_ObjectIdentity((1,3,6,1,4,1,15497,1,2,3,7,7))
_CacheHitRespTimeNow_Type=Integer32
_CacheHitRespTimeNow_Object=MibScalar
cacheHitRespTimeNow=_CacheHitRespTimeNow_Object((1,3,6,1,4,1,15497,1,2,3,7,7,1),_CacheHitRespTimeNow_Type())
cacheHitRespTimeNow.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheHitRespTimeNow.setStatus(_A)
_CacheHitRespTime1hrPeak_Type=Integer32
_CacheHitRespTime1hrPeak_Object=MibScalar
cacheHitRespTime1hrPeak=_CacheHitRespTime1hrPeak_Object((1,3,6,1,4,1,15497,1,2,3,7,7,2),_CacheHitRespTime1hrPeak_Type())
cacheHitRespTime1hrPeak.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheHitRespTime1hrPeak.setStatus(_A)
_CacheHitRespTime1hrMean_Type=Integer32
_CacheHitRespTime1hrMean_Object=MibScalar
cacheHitRespTime1hrMean=_CacheHitRespTime1hrMean_Object((1,3,6,1,4,1,15497,1,2,3,7,7,3),_CacheHitRespTime1hrMean_Type())
cacheHitRespTime1hrMean.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheHitRespTime1hrMean.setStatus(_A)
_CacheHitRespTime1dayPeak_Type=Integer32
_CacheHitRespTime1dayPeak_Object=MibScalar
cacheHitRespTime1dayPeak=_CacheHitRespTime1dayPeak_Object((1,3,6,1,4,1,15497,1,2,3,7,7,4),_CacheHitRespTime1dayPeak_Type())
cacheHitRespTime1dayPeak.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheHitRespTime1dayPeak.setStatus(_A)
_CacheHitRespTime1dayMean_Type=Integer32
_CacheHitRespTime1dayMean_Object=MibScalar
cacheHitRespTime1dayMean=_CacheHitRespTime1dayMean_Object((1,3,6,1,4,1,15497,1,2,3,7,7,5),_CacheHitRespTime1dayMean_Type())
cacheHitRespTime1dayMean.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheHitRespTime1dayMean.setStatus(_A)
_CacheHitRespTime1weekPeak_Type=Integer32
_CacheHitRespTime1weekPeak_Object=MibScalar
cacheHitRespTime1weekPeak=_CacheHitRespTime1weekPeak_Object((1,3,6,1,4,1,15497,1,2,3,7,7,6),_CacheHitRespTime1weekPeak_Type())
cacheHitRespTime1weekPeak.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheHitRespTime1weekPeak.setStatus(_A)
_CacheHitRespTime1weekMean_Type=Integer32
_CacheHitRespTime1weekMean_Object=MibScalar
cacheHitRespTime1weekMean=_CacheHitRespTime1weekMean_Object((1,3,6,1,4,1,15497,1,2,3,7,7,7),_CacheHitRespTime1weekMean_Type())
cacheHitRespTime1weekMean.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheHitRespTime1weekMean.setStatus(_A)
_CacheHitRespTimeLifePeak_Type=Integer32
_CacheHitRespTimeLifePeak_Object=MibScalar
cacheHitRespTimeLifePeak=_CacheHitRespTimeLifePeak_Object((1,3,6,1,4,1,15497,1,2,3,7,7,8),_CacheHitRespTimeLifePeak_Type())
cacheHitRespTimeLifePeak.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheHitRespTimeLifePeak.setStatus(_A)
_CacheHitRespTimeLifeMean_Type=Integer32
_CacheHitRespTimeLifeMean_Object=MibScalar
cacheHitRespTimeLifeMean=_CacheHitRespTimeLifeMean_Object((1,3,6,1,4,1,15497,1,2,3,7,7,9),_CacheHitRespTimeLifeMean_Type())
cacheHitRespTimeLifeMean.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheHitRespTimeLifeMean.setStatus(_A)
_ProxyRecentMissRespTimePerf_ObjectIdentity=ObjectIdentity
proxyRecentMissRespTimePerf=_ProxyRecentMissRespTimePerf_ObjectIdentity((1,3,6,1,4,1,15497,1,2,3,7,8))
_CacheMissRespTimeNow_Type=Integer32
_CacheMissRespTimeNow_Object=MibScalar
cacheMissRespTimeNow=_CacheMissRespTimeNow_Object((1,3,6,1,4,1,15497,1,2,3,7,8,1),_CacheMissRespTimeNow_Type())
cacheMissRespTimeNow.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheMissRespTimeNow.setStatus(_A)
_CacheMissRespTime1hrPeak_Type=Integer32
_CacheMissRespTime1hrPeak_Object=MibScalar
cacheMissRespTime1hrPeak=_CacheMissRespTime1hrPeak_Object((1,3,6,1,4,1,15497,1,2,3,7,8,2),_CacheMissRespTime1hrPeak_Type())
cacheMissRespTime1hrPeak.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheMissRespTime1hrPeak.setStatus(_A)
_CacheMissRespTime1hrMean_Type=Integer32
_CacheMissRespTime1hrMean_Object=MibScalar
cacheMissRespTime1hrMean=_CacheMissRespTime1hrMean_Object((1,3,6,1,4,1,15497,1,2,3,7,8,3),_CacheMissRespTime1hrMean_Type())
cacheMissRespTime1hrMean.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheMissRespTime1hrMean.setStatus(_A)
_CacheMissRespTime1dayPeak_Type=Integer32
_CacheMissRespTime1dayPeak_Object=MibScalar
cacheMissRespTime1dayPeak=_CacheMissRespTime1dayPeak_Object((1,3,6,1,4,1,15497,1,2,3,7,8,4),_CacheMissRespTime1dayPeak_Type())
cacheMissRespTime1dayPeak.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheMissRespTime1dayPeak.setStatus(_A)
_CacheMissRespTime1dayMean_Type=Integer32
_CacheMissRespTime1dayMean_Object=MibScalar
cacheMissRespTime1dayMean=_CacheMissRespTime1dayMean_Object((1,3,6,1,4,1,15497,1,2,3,7,8,5),_CacheMissRespTime1dayMean_Type())
cacheMissRespTime1dayMean.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheMissRespTime1dayMean.setStatus(_A)
_CacheMissRespTime1weekPeak_Type=Integer32
_CacheMissRespTime1weekPeak_Object=MibScalar
cacheMissRespTime1weekPeak=_CacheMissRespTime1weekPeak_Object((1,3,6,1,4,1,15497,1,2,3,7,8,6),_CacheMissRespTime1weekPeak_Type())
cacheMissRespTime1weekPeak.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheMissRespTime1weekPeak.setStatus(_A)
_CacheMissRespTime1weekMean_Type=Integer32
_CacheMissRespTime1weekMean_Object=MibScalar
cacheMissRespTime1weekMean=_CacheMissRespTime1weekMean_Object((1,3,6,1,4,1,15497,1,2,3,7,8,7),_CacheMissRespTime1weekMean_Type())
cacheMissRespTime1weekMean.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheMissRespTime1weekMean.setStatus(_A)
_CacheMissRespTimeLifePeak_Type=Integer32
_CacheMissRespTimeLifePeak_Object=MibScalar
cacheMissRespTimeLifePeak=_CacheMissRespTimeLifePeak_Object((1,3,6,1,4,1,15497,1,2,3,7,8,8),_CacheMissRespTimeLifePeak_Type())
cacheMissRespTimeLifePeak.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheMissRespTimeLifePeak.setStatus(_A)
_CacheMissRespTimeLifeMean_Type=Integer32
_CacheMissRespTimeLifeMean_Object=MibScalar
cacheMissRespTimeLifeMean=_CacheMissRespTimeLifeMean_Object((1,3,6,1,4,1,15497,1,2,3,7,8,9),_CacheMissRespTimeLifeMean_Type())
cacheMissRespTimeLifeMean.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheMissRespTimeLifeMean.setStatus(_A)
_ProxyRecentTotalRespTimePerf_ObjectIdentity=ObjectIdentity
proxyRecentTotalRespTimePerf=_ProxyRecentTotalRespTimePerf_ObjectIdentity((1,3,6,1,4,1,15497,1,2,3,7,9))
_CacheTotalRespTimeNow_Type=Integer32
_CacheTotalRespTimeNow_Object=MibScalar
cacheTotalRespTimeNow=_CacheTotalRespTimeNow_Object((1,3,6,1,4,1,15497,1,2,3,7,9,1),_CacheTotalRespTimeNow_Type())
cacheTotalRespTimeNow.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheTotalRespTimeNow.setStatus(_A)
_CacheTotalRespTime1hrPeak_Type=Integer32
_CacheTotalRespTime1hrPeak_Object=MibScalar
cacheTotalRespTime1hrPeak=_CacheTotalRespTime1hrPeak_Object((1,3,6,1,4,1,15497,1,2,3,7,9,2),_CacheTotalRespTime1hrPeak_Type())
cacheTotalRespTime1hrPeak.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheTotalRespTime1hrPeak.setStatus(_A)
_CacheTotalRespTime1hrMean_Type=Integer32
_CacheTotalRespTime1hrMean_Object=MibScalar
cacheTotalRespTime1hrMean=_CacheTotalRespTime1hrMean_Object((1,3,6,1,4,1,15497,1,2,3,7,9,3),_CacheTotalRespTime1hrMean_Type())
cacheTotalRespTime1hrMean.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheTotalRespTime1hrMean.setStatus(_A)
_CacheTotalRespTime1dayPeak_Type=Integer32
_CacheTotalRespTime1dayPeak_Object=MibScalar
cacheTotalRespTime1dayPeak=_CacheTotalRespTime1dayPeak_Object((1,3,6,1,4,1,15497,1,2,3,7,9,4),_CacheTotalRespTime1dayPeak_Type())
cacheTotalRespTime1dayPeak.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheTotalRespTime1dayPeak.setStatus(_A)
_CacheTotalRespTime1dayMean_Type=Integer32
_CacheTotalRespTime1dayMean_Object=MibScalar
cacheTotalRespTime1dayMean=_CacheTotalRespTime1dayMean_Object((1,3,6,1,4,1,15497,1,2,3,7,9,5),_CacheTotalRespTime1dayMean_Type())
cacheTotalRespTime1dayMean.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheTotalRespTime1dayMean.setStatus(_A)
_CacheTotalRespTime1weekPeak_Type=Integer32
_CacheTotalRespTime1weekPeak_Object=MibScalar
cacheTotalRespTime1weekPeak=_CacheTotalRespTime1weekPeak_Object((1,3,6,1,4,1,15497,1,2,3,7,9,6),_CacheTotalRespTime1weekPeak_Type())
cacheTotalRespTime1weekPeak.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheTotalRespTime1weekPeak.setStatus(_A)
_CacheTotalRespTime1weekMean_Type=Integer32
_CacheTotalRespTime1weekMean_Object=MibScalar
cacheTotalRespTime1weekMean=_CacheTotalRespTime1weekMean_Object((1,3,6,1,4,1,15497,1,2,3,7,9,7),_CacheTotalRespTime1weekMean_Type())
cacheTotalRespTime1weekMean.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheTotalRespTime1weekMean.setStatus(_A)
_CacheTotalRespTimeLifePeak_Type=Integer32
_CacheTotalRespTimeLifePeak_Object=MibScalar
cacheTotalRespTimeLifePeak=_CacheTotalRespTimeLifePeak_Object((1,3,6,1,4,1,15497,1,2,3,7,9,8),_CacheTotalRespTimeLifePeak_Type())
cacheTotalRespTimeLifePeak.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheTotalRespTimeLifePeak.setStatus(_A)
_CacheTotalRespTimeLifeMean_Type=Integer32
_CacheTotalRespTimeLifeMean_Object=MibScalar
cacheTotalRespTimeLifeMean=_CacheTotalRespTimeLifeMean_Object((1,3,6,1,4,1,15497,1,2,3,7,9,9),_CacheTotalRespTimeLifeMean_Type())
cacheTotalRespTimeLifeMean.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheTotalRespTimeLifeMean.setStatus(_A)
_ProxyRecentErrsPerf_ObjectIdentity=ObjectIdentity
proxyRecentErrsPerf=_ProxyRecentErrsPerf_ObjectIdentity((1,3,6,1,4,1,15497,1,2,3,7,10))
_CacheErrsNow_Type=Integer32
_CacheErrsNow_Object=MibScalar
cacheErrsNow=_CacheErrsNow_Object((1,3,6,1,4,1,15497,1,2,3,7,10,1),_CacheErrsNow_Type())
cacheErrsNow.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheErrsNow.setStatus(_A)
_CacheErrs1hrPeak_Type=Integer32
_CacheErrs1hrPeak_Object=MibScalar
cacheErrs1hrPeak=_CacheErrs1hrPeak_Object((1,3,6,1,4,1,15497,1,2,3,7,10,2),_CacheErrs1hrPeak_Type())
cacheErrs1hrPeak.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheErrs1hrPeak.setStatus(_A)
_CacheErrs1hrMean_Type=Integer32
_CacheErrs1hrMean_Object=MibScalar
cacheErrs1hrMean=_CacheErrs1hrMean_Object((1,3,6,1,4,1,15497,1,2,3,7,10,3),_CacheErrs1hrMean_Type())
cacheErrs1hrMean.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheErrs1hrMean.setStatus(_A)
_CacheErrs1dayPeak_Type=Integer32
_CacheErrs1dayPeak_Object=MibScalar
cacheErrs1dayPeak=_CacheErrs1dayPeak_Object((1,3,6,1,4,1,15497,1,2,3,7,10,4),_CacheErrs1dayPeak_Type())
cacheErrs1dayPeak.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheErrs1dayPeak.setStatus(_A)
_CacheErrs1dayMean_Type=Integer32
_CacheErrs1dayMean_Object=MibScalar
cacheErrs1dayMean=_CacheErrs1dayMean_Object((1,3,6,1,4,1,15497,1,2,3,7,10,5),_CacheErrs1dayMean_Type())
cacheErrs1dayMean.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheErrs1dayMean.setStatus(_A)
_CacheErrs1weekPeak_Type=Integer32
_CacheErrs1weekPeak_Object=MibScalar
cacheErrs1weekPeak=_CacheErrs1weekPeak_Object((1,3,6,1,4,1,15497,1,2,3,7,10,6),_CacheErrs1weekPeak_Type())
cacheErrs1weekPeak.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheErrs1weekPeak.setStatus(_A)
_CacheErrs1weekMean_Type=Integer32
_CacheErrs1weekMean_Object=MibScalar
cacheErrs1weekMean=_CacheErrs1weekMean_Object((1,3,6,1,4,1,15497,1,2,3,7,10,7),_CacheErrs1weekMean_Type())
cacheErrs1weekMean.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheErrs1weekMean.setStatus(_A)
_CacheErrsLifePeak_Type=Integer32
_CacheErrsLifePeak_Object=MibScalar
cacheErrsLifePeak=_CacheErrsLifePeak_Object((1,3,6,1,4,1,15497,1,2,3,7,10,8),_CacheErrsLifePeak_Type())
cacheErrsLifePeak.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheErrsLifePeak.setStatus(_A)
_CacheErrsLifeMean_Type=Integer32
_CacheErrsLifeMean_Object=MibScalar
cacheErrsLifeMean=_CacheErrsLifeMean_Object((1,3,6,1,4,1,15497,1,2,3,7,10,9),_CacheErrsLifeMean_Type())
cacheErrsLifeMean.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheErrsLifeMean.setStatus(_A)
_ProxyRecentDeniedPerf_ObjectIdentity=ObjectIdentity
proxyRecentDeniedPerf=_ProxyRecentDeniedPerf_ObjectIdentity((1,3,6,1,4,1,15497,1,2,3,7,11))
_CacheDeniedNow_Type=Integer32
_CacheDeniedNow_Object=MibScalar
cacheDeniedNow=_CacheDeniedNow_Object((1,3,6,1,4,1,15497,1,2,3,7,11,1),_CacheDeniedNow_Type())
cacheDeniedNow.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheDeniedNow.setStatus(_A)
_CacheDenied1hrPeak_Type=Integer32
_CacheDenied1hrPeak_Object=MibScalar
cacheDenied1hrPeak=_CacheDenied1hrPeak_Object((1,3,6,1,4,1,15497,1,2,3,7,11,2),_CacheDenied1hrPeak_Type())
cacheDenied1hrPeak.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheDenied1hrPeak.setStatus(_A)
_CacheDenied1hrMean_Type=Integer32
_CacheDenied1hrMean_Object=MibScalar
cacheDenied1hrMean=_CacheDenied1hrMean_Object((1,3,6,1,4,1,15497,1,2,3,7,11,3),_CacheDenied1hrMean_Type())
cacheDenied1hrMean.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheDenied1hrMean.setStatus(_A)
_CacheDenied1dayPeak_Type=Integer32
_CacheDenied1dayPeak_Object=MibScalar
cacheDenied1dayPeak=_CacheDenied1dayPeak_Object((1,3,6,1,4,1,15497,1,2,3,7,11,4),_CacheDenied1dayPeak_Type())
cacheDenied1dayPeak.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheDenied1dayPeak.setStatus(_A)
_CacheDenied1dayMean_Type=Integer32
_CacheDenied1dayMean_Object=MibScalar
cacheDenied1dayMean=_CacheDenied1dayMean_Object((1,3,6,1,4,1,15497,1,2,3,7,11,5),_CacheDenied1dayMean_Type())
cacheDenied1dayMean.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheDenied1dayMean.setStatus(_A)
_CacheDenied1weekPeak_Type=Integer32
_CacheDenied1weekPeak_Object=MibScalar
cacheDenied1weekPeak=_CacheDenied1weekPeak_Object((1,3,6,1,4,1,15497,1,2,3,7,11,6),_CacheDenied1weekPeak_Type())
cacheDenied1weekPeak.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheDenied1weekPeak.setStatus(_A)
_CacheDenied1weekMean_Type=Integer32
_CacheDenied1weekMean_Object=MibScalar
cacheDenied1weekMean=_CacheDenied1weekMean_Object((1,3,6,1,4,1,15497,1,2,3,7,11,7),_CacheDenied1weekMean_Type())
cacheDenied1weekMean.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheDenied1weekMean.setStatus(_A)
_CacheDeniedLifePeak_Type=Integer32
_CacheDeniedLifePeak_Object=MibScalar
cacheDeniedLifePeak=_CacheDeniedLifePeak_Object((1,3,6,1,4,1,15497,1,2,3,7,11,8),_CacheDeniedLifePeak_Type())
cacheDeniedLifePeak.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheDeniedLifePeak.setStatus(_A)
_CacheDeniedLifeMean_Type=Integer32
_CacheDeniedLifeMean_Object=MibScalar
cacheDeniedLifeMean=_CacheDeniedLifeMean_Object((1,3,6,1,4,1,15497,1,2,3,7,11,9),_CacheDeniedLifeMean_Type())
cacheDeniedLifeMean.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheDeniedLifeMean.setStatus(_A)
_ProxyRecentErrRespTimePerf_ObjectIdentity=ObjectIdentity
proxyRecentErrRespTimePerf=_ProxyRecentErrRespTimePerf_ObjectIdentity((1,3,6,1,4,1,15497,1,2,3,7,12))
_CacheErrRespTimeNow_Type=Integer32
_CacheErrRespTimeNow_Object=MibScalar
cacheErrRespTimeNow=_CacheErrRespTimeNow_Object((1,3,6,1,4,1,15497,1,2,3,7,12,1),_CacheErrRespTimeNow_Type())
cacheErrRespTimeNow.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheErrRespTimeNow.setStatus(_A)
_CacheErrRespTime1hrPeak_Type=Integer32
_CacheErrRespTime1hrPeak_Object=MibScalar
cacheErrRespTime1hrPeak=_CacheErrRespTime1hrPeak_Object((1,3,6,1,4,1,15497,1,2,3,7,12,2),_CacheErrRespTime1hrPeak_Type())
cacheErrRespTime1hrPeak.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheErrRespTime1hrPeak.setStatus(_A)
_CacheErrRespTime1hrMean_Type=Integer32
_CacheErrRespTime1hrMean_Object=MibScalar
cacheErrRespTime1hrMean=_CacheErrRespTime1hrMean_Object((1,3,6,1,4,1,15497,1,2,3,7,12,3),_CacheErrRespTime1hrMean_Type())
cacheErrRespTime1hrMean.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheErrRespTime1hrMean.setStatus(_A)
_CacheErrRespTime1dayPeak_Type=Integer32
_CacheErrRespTime1dayPeak_Object=MibScalar
cacheErrRespTime1dayPeak=_CacheErrRespTime1dayPeak_Object((1,3,6,1,4,1,15497,1,2,3,7,12,4),_CacheErrRespTime1dayPeak_Type())
cacheErrRespTime1dayPeak.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheErrRespTime1dayPeak.setStatus(_A)
_CacheErrRespTime1dayMean_Type=Integer32
_CacheErrRespTime1dayMean_Object=MibScalar
cacheErrRespTime1dayMean=_CacheErrRespTime1dayMean_Object((1,3,6,1,4,1,15497,1,2,3,7,12,5),_CacheErrRespTime1dayMean_Type())
cacheErrRespTime1dayMean.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheErrRespTime1dayMean.setStatus(_A)
_CacheErrRespTime1weekPeak_Type=Integer32
_CacheErrRespTime1weekPeak_Object=MibScalar
cacheErrRespTime1weekPeak=_CacheErrRespTime1weekPeak_Object((1,3,6,1,4,1,15497,1,2,3,7,12,6),_CacheErrRespTime1weekPeak_Type())
cacheErrRespTime1weekPeak.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheErrRespTime1weekPeak.setStatus(_A)
_CacheErrRespTime1weekMean_Type=Integer32
_CacheErrRespTime1weekMean_Object=MibScalar
cacheErrRespTime1weekMean=_CacheErrRespTime1weekMean_Object((1,3,6,1,4,1,15497,1,2,3,7,12,7),_CacheErrRespTime1weekMean_Type())
cacheErrRespTime1weekMean.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheErrRespTime1weekMean.setStatus(_A)
_CacheErrRespTimeLifePeak_Type=Integer32
_CacheErrRespTimeLifePeak_Object=MibScalar
cacheErrRespTimeLifePeak=_CacheErrRespTimeLifePeak_Object((1,3,6,1,4,1,15497,1,2,3,7,12,8),_CacheErrRespTimeLifePeak_Type())
cacheErrRespTimeLifePeak.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheErrRespTimeLifePeak.setStatus(_A)
_CacheErrRespTimeLifeMean_Type=Integer32
_CacheErrRespTimeLifeMean_Object=MibScalar
cacheErrRespTimeLifeMean=_CacheErrRespTimeLifeMean_Object((1,3,6,1,4,1,15497,1,2,3,7,12,9),_CacheErrRespTimeLifeMean_Type())
cacheErrRespTimeLifeMean.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheErrRespTimeLifeMean.setStatus(_A)
_ProxyRecentDeniedRespTimePerf_ObjectIdentity=ObjectIdentity
proxyRecentDeniedRespTimePerf=_ProxyRecentDeniedRespTimePerf_ObjectIdentity((1,3,6,1,4,1,15497,1,2,3,7,13))
_CacheDeniedRespTimeNow_Type=Integer32
_CacheDeniedRespTimeNow_Object=MibScalar
cacheDeniedRespTimeNow=_CacheDeniedRespTimeNow_Object((1,3,6,1,4,1,15497,1,2,3,7,13,1),_CacheDeniedRespTimeNow_Type())
cacheDeniedRespTimeNow.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheDeniedRespTimeNow.setStatus(_A)
_CacheDeniedRespTime1hrPeak_Type=Integer32
_CacheDeniedRespTime1hrPeak_Object=MibScalar
cacheDeniedRespTime1hrPeak=_CacheDeniedRespTime1hrPeak_Object((1,3,6,1,4,1,15497,1,2,3,7,13,2),_CacheDeniedRespTime1hrPeak_Type())
cacheDeniedRespTime1hrPeak.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheDeniedRespTime1hrPeak.setStatus(_A)
_CacheDeniedRespTime1hrMean_Type=Integer32
_CacheDeniedRespTime1hrMean_Object=MibScalar
cacheDeniedRespTime1hrMean=_CacheDeniedRespTime1hrMean_Object((1,3,6,1,4,1,15497,1,2,3,7,13,3),_CacheDeniedRespTime1hrMean_Type())
cacheDeniedRespTime1hrMean.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheDeniedRespTime1hrMean.setStatus(_A)
_CacheDeniedRespTime1dayPeak_Type=Integer32
_CacheDeniedRespTime1dayPeak_Object=MibScalar
cacheDeniedRespTime1dayPeak=_CacheDeniedRespTime1dayPeak_Object((1,3,6,1,4,1,15497,1,2,3,7,13,4),_CacheDeniedRespTime1dayPeak_Type())
cacheDeniedRespTime1dayPeak.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheDeniedRespTime1dayPeak.setStatus(_A)
_CacheDeniedRespTime1dayMean_Type=Integer32
_CacheDeniedRespTime1dayMean_Object=MibScalar
cacheDeniedRespTime1dayMean=_CacheDeniedRespTime1dayMean_Object((1,3,6,1,4,1,15497,1,2,3,7,13,5),_CacheDeniedRespTime1dayMean_Type())
cacheDeniedRespTime1dayMean.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheDeniedRespTime1dayMean.setStatus(_A)
_CacheDeniedRespTime1weekPeak_Type=Integer32
_CacheDeniedRespTime1weekPeak_Object=MibScalar
cacheDeniedRespTime1weekPeak=_CacheDeniedRespTime1weekPeak_Object((1,3,6,1,4,1,15497,1,2,3,7,13,6),_CacheDeniedRespTime1weekPeak_Type())
cacheDeniedRespTime1weekPeak.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheDeniedRespTime1weekPeak.setStatus(_A)
_CacheDeniedRespTime1weekMean_Type=Integer32
_CacheDeniedRespTime1weekMean_Object=MibScalar
cacheDeniedRespTime1weekMean=_CacheDeniedRespTime1weekMean_Object((1,3,6,1,4,1,15497,1,2,3,7,13,7),_CacheDeniedRespTime1weekMean_Type())
cacheDeniedRespTime1weekMean.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheDeniedRespTime1weekMean.setStatus(_A)
_CacheDeniedRespTimeLifePeak_Type=Integer32
_CacheDeniedRespTimeLifePeak_Object=MibScalar
cacheDeniedRespTimeLifePeak=_CacheDeniedRespTimeLifePeak_Object((1,3,6,1,4,1,15497,1,2,3,7,13,8),_CacheDeniedRespTimeLifePeak_Type())
cacheDeniedRespTimeLifePeak.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheDeniedRespTimeLifePeak.setStatus(_A)
_CacheDeniedRespTimeLifeMean_Type=Integer32
_CacheDeniedRespTimeLifeMean_Object=MibScalar
cacheDeniedRespTimeLifeMean=_CacheDeniedRespTimeLifeMean_Object((1,3,6,1,4,1,15497,1,2,3,7,13,9),_CacheDeniedRespTimeLifeMean_Type())
cacheDeniedRespTimeLifeMean.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheDeniedRespTimeLifeMean.setStatus(_A)
_ProxyHardware_ObjectIdentity=ObjectIdentity
proxyHardware=_ProxyHardware_ObjectIdentity((1,3,6,1,4,1,15497,1,2,4))
_ProxyHardwareDisk_ObjectIdentity=ObjectIdentity
proxyHardwareDisk=_ProxyHardwareDisk_ObjectIdentity((1,3,6,1,4,1,15497,1,2,4,1))
_HardwareDiskStatTable_Object=MibTable
hardwareDiskStatTable=_HardwareDiskStatTable_Object((1,3,6,1,4,1,15497,1,2,4,1,1))
if mibBuilder.loadTexts:hardwareDiskStatTable.setStatus(_A)
_DiskStatEntry_Object=MibTableRow
diskStatEntry=_DiskStatEntry_Object((1,3,6,1,4,1,15497,1,2,4,1,1,1))
diskStatEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:diskStatEntry.setStatus(_A)
class _DiskStatEntryNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,18))
_DiskStatEntryNumber_Type.__name__=_C
_DiskStatEntryNumber_Object=MibTableColumn
diskStatEntryNumber=_DiskStatEntryNumber_Object((1,3,6,1,4,1,15497,1,2,4,1,1,1,1),_DiskStatEntryNumber_Type())
diskStatEntryNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:diskStatEntryNumber.setStatus(_A)
_DiskStatWrites_Type=Integer32
_DiskStatWrites_Object=MibTableColumn
diskStatWrites=_DiskStatWrites_Object((1,3,6,1,4,1,15497,1,2,4,1,1,1,2),_DiskStatWrites_Type())
diskStatWrites.setMaxAccess(_B)
if mibBuilder.loadTexts:diskStatWrites.setStatus(_A)
_DiskStatWriteErrs_Type=Integer32
_DiskStatWriteErrs_Object=MibTableColumn
diskStatWriteErrs=_DiskStatWriteErrs_Object((1,3,6,1,4,1,15497,1,2,4,1,1,1,3),_DiskStatWriteErrs_Type())
diskStatWriteErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:diskStatWriteErrs.setStatus(_A)
_DiskStatReads_Type=Integer32
_DiskStatReads_Object=MibTableColumn
diskStatReads=_DiskStatReads_Object((1,3,6,1,4,1,15497,1,2,4,1,1,1,4),_DiskStatReads_Type())
diskStatReads.setMaxAccess(_B)
if mibBuilder.loadTexts:diskStatReads.setStatus(_A)
_DiskStatReadErrs_Type=Integer32
_DiskStatReadErrs_Object=MibTableColumn
diskStatReadErrs=_DiskStatReadErrs_Object((1,3,6,1,4,1,15497,1,2,4,1,1,1,5),_DiskStatReadErrs_Type())
diskStatReadErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:diskStatReadErrs.setStatus(_A)
_ProxyTraps_ObjectIdentity=ObjectIdentity
proxyTraps=_ProxyTraps_ObjectIdentity((1,3,6,1,4,1,15497,1,2,5))
upstreamProxyFailure=NotificationType((1,3,6,1,4,1,15497,1,2,5,1))
upstreamProxyFailure.setObjects((_E,_F))
if mibBuilder.loadTexts:upstreamProxyFailure.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'asyncOSWebSecurityAppliance':asyncOSWebSecurityAppliance,'proxySystem':proxySystem,'cacheUptime':cacheUptime,'cacheMemory':cacheMemory,'cacheSysStorage':cacheSysStorage,'proxyConfig':proxyConfig,'cacheAdmin':cacheAdmin,'cacheSoftware':cacheSoftware,'cacheVersion':cacheVersion,'licenseExpiration':licenseExpiration,'proxyPerf':proxyPerf,'proxySysPerf':proxySysPerf,'cacheCpuTime':cacheCpuTime,'cacheCpuUsage':cacheCpuUsage,'cacheMaxResSize':cacheMaxResSize,'cacheUsedStoragePct':cacheUsedStoragePct,'cacheBusyCPUPct':cacheBusyCPUPct,'cacheMemoryBufferUsagePct':cacheMemoryBufferUsagePct,'proxyClientSidePerf':proxyClientSidePerf,'cacheClientSizeHistTable':cacheClientSizeHistTable,'cacheClientSizeHistEntry':cacheClientSizeHistEntry,_G:cacheClientSizeHistBinNumber,'cacheClientReqSize':cacheClientReqSize,'cacheClientRequests':cacheClientRequests,'cacheClientHits':cacheClientHits,'cacheClientErrors':cacheClientErrors,'cacheClientInKb':cacheClientInKb,'cacheClientOutKb':cacheClientOutKb,'cacheClientIdleConns':cacheClientIdleConns,'cacheClientTotalConns':cacheClientTotalConns,'cacheClientMaxConns':cacheClientMaxConns,'cacheClientAccepts':cacheClientAccepts,'cacheClientICPRequests':cacheClientICPRequests,'cacheClientICPHits':cacheClientICPHits,'cacheClientICPMisses':cacheClientICPMisses,'cacheClientICPErrors':cacheClientICPErrors,'cacheClientICPDenials':cacheClientICPDenials,'cacheClientReqMisses':cacheClientReqMisses,'cacheClientReqDenials':cacheClientReqDenials,'proxyServerSidePerf':proxyServerSidePerf,'cacheServerSizeHistTable':cacheServerSizeHistTable,'cacheServerSizeHistEntry':cacheServerSizeHistEntry,_H:cacheServerSizeHistBinNumber,'cacheServerReplySize':cacheServerReplySize,'cacheServerRequests':cacheServerRequests,'cacheServerSockets':cacheServerSockets,'cacheServerErrors':cacheServerErrors,'cacheServerInKb':cacheServerInKb,'cacheServerOutKb':cacheServerOutKb,'cacheServerIdleConns':cacheServerIdleConns,'cacheServerTotalConns':cacheServerTotalConns,'cacheServerCloseIdleConns':cacheServerCloseIdleConns,'cacheServerLimitIdleConns':cacheServerLimitIdleConns,'cacheServerConnsThresh':cacheServerConnsThresh,'cacheServerPersisConnsRetries':cacheServerPersisConnsRetries,'cacheServerRegConnsRetries':cacheServerRegConnsRetries,'cacheServerRWErrorRetries':cacheServerRWErrorRetries,'cacheServerEarlyCloseRetries':cacheServerEarlyCloseRetries,'cacheServerICPRequests':cacheServerICPRequests,'cacheServerICPHits':cacheServerICPHits,'cacheServerICPMisses':cacheServerICPMisses,'cacheServerICPErrors':cacheServerICPErrors,'cacheServerICPDenials':cacheServerICPDenials,'proxyCachePerf':proxyCachePerf,'cacheCacheSizeHistTable':cacheCacheSizeHistTable,'cacheCacheSizeHistEntry':cacheCacheSizeHistEntry,_I:cacheSizeHistBinNumber,'cacheCacheActiveObjs':cacheCacheActiveObjs,'cacheCacheAllObjs':cacheCacheAllObjs,'cacheCacheLiveCachedObjs':cacheCacheLiveCachedObjs,'cacheCacheLiveCachedObjSizes':cacheCacheLiveCachedObjSizes,'cacheCacheTotalCachedObjs':cacheCacheTotalCachedObjs,'cacheCacheTotalCachedObjSizes':cacheCacheTotalCachedObjSizes,'proxyMedianSvcTime':proxyMedianSvcTime,'cacheMedianSvcTable':cacheMedianSvcTable,'cacheMedianSvcEntry':cacheMedianSvcEntry,_J:cacheMedianTime,'cacheHTTPCltSvcTime':cacheHTTPCltSvcTime,'cacheHTTPMissSvcTime':cacheHTTPMissSvcTime,'cacheHTTPHitSvcTime':cacheHTTPHitSvcTime,'cacheHTTPSrvSvcTime':cacheHTTPSrvSvcTime,'cacheDnsSvcTime':cacheDnsSvcTime,'cacheHTTPSvcWaitTime':cacheHTTPSvcWaitTime,'proxyExecutiveSummary':proxyExecutiveSummary,'cacheTotalHttpReqs':cacheTotalHttpReqs,'cacheMeanRespTime':cacheMeanRespTime,'cacheMeanMissRespTime':cacheMeanMissRespTime,'cacheMeanHitRespTime':cacheMeanHitRespTime,'cacheMeanHitRatio':cacheMeanHitRatio,'cacheMeanByteHitRatio':cacheMeanByteHitRatio,'cacheTotalBandwidthSaving':cacheTotalBandwidthSaving,'cacheDuration':cacheDuration,'cacheCltReplyErrPct':cacheCltReplyErrPct,'proxyRecentPerf':proxyRecentPerf,'proxyRecentThruputPerf':proxyRecentThruputPerf,'cacheThruputNow':cacheThruputNow,'cacheThruput1hrPeak':cacheThruput1hrPeak,'cacheThruput1hrMean':cacheThruput1hrMean,'cacheThruput1dayPeak':cacheThruput1dayPeak,'cacheThruput1dayMean':cacheThruput1dayMean,'cacheThruput1weekPeak':cacheThruput1weekPeak,'cacheThruput1weekMean':cacheThruput1weekMean,'cacheThruputLifePeak':cacheThruputLifePeak,'cacheThruputLifeMean':cacheThruputLifeMean,'proxyRecentBandWSavPerf':proxyRecentBandWSavPerf,'cacheBwidthSavingNow':cacheBwidthSavingNow,'cacheBwidthSaving1hrPeak':cacheBwidthSaving1hrPeak,'cacheBwidthSaving1hrMean':cacheBwidthSaving1hrMean,'cacheBwidthSaving1dayPeak':cacheBwidthSaving1dayPeak,'cacheBwidthSaving1dayMean':cacheBwidthSaving1dayMean,'cacheBwidthSaving1weekPeak':cacheBwidthSaving1weekPeak,'cacheBwidthSaving1weekMean':cacheBwidthSaving1weekMean,'cacheBwidthSavingLifePeak':cacheBwidthSavingLifePeak,'cacheBwidthSavingLifeMean':cacheBwidthSavingLifeMean,'proxyRecentBandWSpntPerf':proxyRecentBandWSpntPerf,'cacheBwidthSpentNow':cacheBwidthSpentNow,'cacheBwidthSpent1hrPeak':cacheBwidthSpent1hrPeak,'cacheBwidthSpent1hrMean':cacheBwidthSpent1hrMean,'cacheBwidthSpent1dayPeak':cacheBwidthSpent1dayPeak,'cacheBwidthSpent1dayMean':cacheBwidthSpent1dayMean,'cacheBwidthSpent1weekPeak':cacheBwidthSpent1weekPeak,'cacheBwidthSpent1weekMean':cacheBwidthSpent1weekMean,'cacheBwidthSpentLifePeak':cacheBwidthSpentLifePeak,'cacheBwidthSpentLifeMean':cacheBwidthSpentLifeMean,'proxyRecentBandWTotPerf':proxyRecentBandWTotPerf,'cacheBwidthTotalNow':cacheBwidthTotalNow,'cacheBwidthTotal1hrPeak':cacheBwidthTotal1hrPeak,'cacheBwidthTotal1hrMean':cacheBwidthTotal1hrMean,'cacheBwidthTotal1dayPeak':cacheBwidthTotal1dayPeak,'cacheBwidthTotal1dayMean':cacheBwidthTotal1dayMean,'cacheBwidthTotal1weekPeak':cacheBwidthTotal1weekPeak,'cacheBwidthTotal1weekMean':cacheBwidthTotal1weekMean,'cacheBwidthTotalLifePeak':cacheBwidthTotalLifePeak,'cacheBwidthTotalLifeMean':cacheBwidthTotalLifeMean,'proxyRecentHitsPerf':proxyRecentHitsPerf,'cacheHitsNow':cacheHitsNow,'cacheHits1hrPeak':cacheHits1hrPeak,'cacheHits1hrMean':cacheHits1hrMean,'cacheHits1dayPeak':cacheHits1dayPeak,'cacheHits1dayMean':cacheHits1dayMean,'cacheHits1weekPeak':cacheHits1weekPeak,'cacheHits1weekMean':cacheHits1weekMean,'cacheHitsLifePeak':cacheHitsLifePeak,'cacheHitsLifeMean':cacheHitsLifeMean,'proxyRecentMissesPerf':proxyRecentMissesPerf,'cacheMissesNow':cacheMissesNow,'cacheMisses1hrPeak':cacheMisses1hrPeak,'cacheMisses1hrMean':cacheMisses1hrMean,'cacheMisses1dayPeak':cacheMisses1dayPeak,'cacheMisses1dayMean':cacheMisses1dayMean,'cacheMisses1weekPeak':cacheMisses1weekPeak,'cacheMisses1weekMean':cacheMisses1weekMean,'cacheMissesLifePeak':cacheMissesLifePeak,'cacheMissesLifeMean':cacheMissesLifeMean,'proxyRecentHitRespTimePerf':proxyRecentHitRespTimePerf,'cacheHitRespTimeNow':cacheHitRespTimeNow,'cacheHitRespTime1hrPeak':cacheHitRespTime1hrPeak,'cacheHitRespTime1hrMean':cacheHitRespTime1hrMean,'cacheHitRespTime1dayPeak':cacheHitRespTime1dayPeak,'cacheHitRespTime1dayMean':cacheHitRespTime1dayMean,'cacheHitRespTime1weekPeak':cacheHitRespTime1weekPeak,'cacheHitRespTime1weekMean':cacheHitRespTime1weekMean,'cacheHitRespTimeLifePeak':cacheHitRespTimeLifePeak,'cacheHitRespTimeLifeMean':cacheHitRespTimeLifeMean,'proxyRecentMissRespTimePerf':proxyRecentMissRespTimePerf,'cacheMissRespTimeNow':cacheMissRespTimeNow,'cacheMissRespTime1hrPeak':cacheMissRespTime1hrPeak,'cacheMissRespTime1hrMean':cacheMissRespTime1hrMean,'cacheMissRespTime1dayPeak':cacheMissRespTime1dayPeak,'cacheMissRespTime1dayMean':cacheMissRespTime1dayMean,'cacheMissRespTime1weekPeak':cacheMissRespTime1weekPeak,'cacheMissRespTime1weekMean':cacheMissRespTime1weekMean,'cacheMissRespTimeLifePeak':cacheMissRespTimeLifePeak,'cacheMissRespTimeLifeMean':cacheMissRespTimeLifeMean,'proxyRecentTotalRespTimePerf':proxyRecentTotalRespTimePerf,'cacheTotalRespTimeNow':cacheTotalRespTimeNow,'cacheTotalRespTime1hrPeak':cacheTotalRespTime1hrPeak,'cacheTotalRespTime1hrMean':cacheTotalRespTime1hrMean,'cacheTotalRespTime1dayPeak':cacheTotalRespTime1dayPeak,'cacheTotalRespTime1dayMean':cacheTotalRespTime1dayMean,'cacheTotalRespTime1weekPeak':cacheTotalRespTime1weekPeak,'cacheTotalRespTime1weekMean':cacheTotalRespTime1weekMean,'cacheTotalRespTimeLifePeak':cacheTotalRespTimeLifePeak,'cacheTotalRespTimeLifeMean':cacheTotalRespTimeLifeMean,'proxyRecentErrsPerf':proxyRecentErrsPerf,'cacheErrsNow':cacheErrsNow,'cacheErrs1hrPeak':cacheErrs1hrPeak,'cacheErrs1hrMean':cacheErrs1hrMean,'cacheErrs1dayPeak':cacheErrs1dayPeak,'cacheErrs1dayMean':cacheErrs1dayMean,'cacheErrs1weekPeak':cacheErrs1weekPeak,'cacheErrs1weekMean':cacheErrs1weekMean,'cacheErrsLifePeak':cacheErrsLifePeak,'cacheErrsLifeMean':cacheErrsLifeMean,'proxyRecentDeniedPerf':proxyRecentDeniedPerf,'cacheDeniedNow':cacheDeniedNow,'cacheDenied1hrPeak':cacheDenied1hrPeak,'cacheDenied1hrMean':cacheDenied1hrMean,'cacheDenied1dayPeak':cacheDenied1dayPeak,'cacheDenied1dayMean':cacheDenied1dayMean,'cacheDenied1weekPeak':cacheDenied1weekPeak,'cacheDenied1weekMean':cacheDenied1weekMean,'cacheDeniedLifePeak':cacheDeniedLifePeak,'cacheDeniedLifeMean':cacheDeniedLifeMean,'proxyRecentErrRespTimePerf':proxyRecentErrRespTimePerf,'cacheErrRespTimeNow':cacheErrRespTimeNow,'cacheErrRespTime1hrPeak':cacheErrRespTime1hrPeak,'cacheErrRespTime1hrMean':cacheErrRespTime1hrMean,'cacheErrRespTime1dayPeak':cacheErrRespTime1dayPeak,'cacheErrRespTime1dayMean':cacheErrRespTime1dayMean,'cacheErrRespTime1weekPeak':cacheErrRespTime1weekPeak,'cacheErrRespTime1weekMean':cacheErrRespTime1weekMean,'cacheErrRespTimeLifePeak':cacheErrRespTimeLifePeak,'cacheErrRespTimeLifeMean':cacheErrRespTimeLifeMean,'proxyRecentDeniedRespTimePerf':proxyRecentDeniedRespTimePerf,'cacheDeniedRespTimeNow':cacheDeniedRespTimeNow,'cacheDeniedRespTime1hrPeak':cacheDeniedRespTime1hrPeak,'cacheDeniedRespTime1hrMean':cacheDeniedRespTime1hrMean,'cacheDeniedRespTime1dayPeak':cacheDeniedRespTime1dayPeak,'cacheDeniedRespTime1dayMean':cacheDeniedRespTime1dayMean,'cacheDeniedRespTime1weekPeak':cacheDeniedRespTime1weekPeak,'cacheDeniedRespTime1weekMean':cacheDeniedRespTime1weekMean,'cacheDeniedRespTimeLifePeak':cacheDeniedRespTimeLifePeak,'cacheDeniedRespTimeLifeMean':cacheDeniedRespTimeLifeMean,'proxyHardware':proxyHardware,'proxyHardwareDisk':proxyHardwareDisk,'hardwareDiskStatTable':hardwareDiskStatTable,'diskStatEntry':diskStatEntry,_K:diskStatEntryNumber,'diskStatWrites':diskStatWrites,'diskStatWriteErrs':diskStatWriteErrs,'diskStatReads':diskStatReads,'diskStatReadErrs':diskStatReadErrs,'proxyTraps':proxyTraps,'upstreamProxyFailure':upstreamProxyFailure})