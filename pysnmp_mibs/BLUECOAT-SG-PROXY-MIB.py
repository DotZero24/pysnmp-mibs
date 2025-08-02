_L='sgProxyHttpMedianServiceTime'
_K='not-accessible'
_J='sgProxyCpuCoreIndex'
_I='BLUECOAT-SG-PROXY-MIB'
_H='Integer32'
_G='Bytes Per Second'
_F='Percentage'
_E='deprecated'
_D='Bytes'
_C='Milliseconds'
_B='current'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
blueCoatMgmt,=mibBuilder.importSymbols('BLUECOAT-MIB','blueCoatMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
bluecoatSGProxyMIB=ModuleIdentity((1,3,6,1,4,1,3417,2,11))
if mibBuilder.loadTexts:bluecoatSGProxyMIB.setRevisions(('2011-11-01 03:00','2007-11-05 03:00','2007-08-28 03:00'))
_SgProxyConfig_ObjectIdentity=ObjectIdentity
sgProxyConfig=_SgProxyConfig_ObjectIdentity((1,3,6,1,4,1,3417,2,11,1))
_SgProxyAdmin_Type=DisplayString
_SgProxyAdmin_Object=MibScalar
sgProxyAdmin=_SgProxyAdmin_Object((1,3,6,1,4,1,3417,2,11,1,1),_SgProxyAdmin_Type())
sgProxyAdmin.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyAdmin.setStatus(_B)
_SgProxySoftware_Type=DisplayString
_SgProxySoftware_Object=MibScalar
sgProxySoftware=_SgProxySoftware_Object((1,3,6,1,4,1,3417,2,11,1,2),_SgProxySoftware_Type())
sgProxySoftware.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxySoftware.setStatus(_B)
_SgProxyVersion_Type=DisplayString
_SgProxyVersion_Object=MibScalar
sgProxyVersion=_SgProxyVersion_Object((1,3,6,1,4,1,3417,2,11,1,3),_SgProxyVersion_Type())
sgProxyVersion.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyVersion.setStatus(_B)
_SgProxySerialNumber_Type=DisplayString
_SgProxySerialNumber_Object=MibScalar
sgProxySerialNumber=_SgProxySerialNumber_Object((1,3,6,1,4,1,3417,2,11,1,4),_SgProxySerialNumber_Type())
sgProxySerialNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxySerialNumber.setStatus(_B)
_SgProxySystem_ObjectIdentity=ObjectIdentity
sgProxySystem=_SgProxySystem_ObjectIdentity((1,3,6,1,4,1,3417,2,11,2))
_SgProxyCpu_ObjectIdentity=ObjectIdentity
sgProxyCpu=_SgProxyCpu_ObjectIdentity((1,3,6,1,4,1,3417,2,11,2,1))
_SgProxyCpuUpTime_Type=Counter64
_SgProxyCpuUpTime_Object=MibScalar
sgProxyCpuUpTime=_SgProxyCpuUpTime_Object((1,3,6,1,4,1,3417,2,11,2,1,1),_SgProxyCpuUpTime_Type())
sgProxyCpuUpTime.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyCpuUpTime.setStatus(_E)
if mibBuilder.loadTexts:sgProxyCpuUpTime.setUnits(_C)
_SgProxyCpuBusyTime_Type=Counter64
_SgProxyCpuBusyTime_Object=MibScalar
sgProxyCpuBusyTime=_SgProxyCpuBusyTime_Object((1,3,6,1,4,1,3417,2,11,2,1,2),_SgProxyCpuBusyTime_Type())
sgProxyCpuBusyTime.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyCpuBusyTime.setStatus(_E)
if mibBuilder.loadTexts:sgProxyCpuBusyTime.setUnits(_C)
_SgProxyCpuIdleTime_Type=Counter64
_SgProxyCpuIdleTime_Object=MibScalar
sgProxyCpuIdleTime=_SgProxyCpuIdleTime_Object((1,3,6,1,4,1,3417,2,11,2,1,3),_SgProxyCpuIdleTime_Type())
sgProxyCpuIdleTime.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyCpuIdleTime.setStatus(_E)
if mibBuilder.loadTexts:sgProxyCpuIdleTime.setUnits(_C)
_SgProxyCpuUpTimeSinceLastAccess_Type=Counter64
_SgProxyCpuUpTimeSinceLastAccess_Object=MibScalar
sgProxyCpuUpTimeSinceLastAccess=_SgProxyCpuUpTimeSinceLastAccess_Object((1,3,6,1,4,1,3417,2,11,2,1,4),_SgProxyCpuUpTimeSinceLastAccess_Type())
sgProxyCpuUpTimeSinceLastAccess.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyCpuUpTimeSinceLastAccess.setStatus(_E)
if mibBuilder.loadTexts:sgProxyCpuUpTimeSinceLastAccess.setUnits(_C)
_SgProxyCpuBusyTimeSinceLastAccess_Type=Counter64
_SgProxyCpuBusyTimeSinceLastAccess_Object=MibScalar
sgProxyCpuBusyTimeSinceLastAccess=_SgProxyCpuBusyTimeSinceLastAccess_Object((1,3,6,1,4,1,3417,2,11,2,1,5),_SgProxyCpuBusyTimeSinceLastAccess_Type())
sgProxyCpuBusyTimeSinceLastAccess.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyCpuBusyTimeSinceLastAccess.setStatus(_E)
if mibBuilder.loadTexts:sgProxyCpuBusyTimeSinceLastAccess.setUnits(_C)
_SgProxyCpuIdleTimeSinceLastAccess_Type=Counter64
_SgProxyCpuIdleTimeSinceLastAccess_Object=MibScalar
sgProxyCpuIdleTimeSinceLastAccess=_SgProxyCpuIdleTimeSinceLastAccess_Object((1,3,6,1,4,1,3417,2,11,2,1,6),_SgProxyCpuIdleTimeSinceLastAccess_Type())
sgProxyCpuIdleTimeSinceLastAccess.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyCpuIdleTimeSinceLastAccess.setStatus(_E)
if mibBuilder.loadTexts:sgProxyCpuIdleTimeSinceLastAccess.setUnits(_C)
_SgProxyCpuBusyPerCent_Type=Gauge32
_SgProxyCpuBusyPerCent_Object=MibScalar
sgProxyCpuBusyPerCent=_SgProxyCpuBusyPerCent_Object((1,3,6,1,4,1,3417,2,11,2,1,7),_SgProxyCpuBusyPerCent_Type())
sgProxyCpuBusyPerCent.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyCpuBusyPerCent.setStatus(_E)
if mibBuilder.loadTexts:sgProxyCpuBusyPerCent.setUnits(_F)
_SgProxyCpuIdlePerCent_Type=Gauge32
_SgProxyCpuIdlePerCent_Object=MibScalar
sgProxyCpuIdlePerCent=_SgProxyCpuIdlePerCent_Object((1,3,6,1,4,1,3417,2,11,2,1,8),_SgProxyCpuIdlePerCent_Type())
sgProxyCpuIdlePerCent.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyCpuIdlePerCent.setStatus(_E)
if mibBuilder.loadTexts:sgProxyCpuIdlePerCent.setUnits(_F)
_SgProxyCache_ObjectIdentity=ObjectIdentity
sgProxyCache=_SgProxyCache_ObjectIdentity((1,3,6,1,4,1,3417,2,11,2,2))
_SgProxyStorage_Type=Counter64
_SgProxyStorage_Object=MibScalar
sgProxyStorage=_SgProxyStorage_Object((1,3,6,1,4,1,3417,2,11,2,2,1),_SgProxyStorage_Type())
sgProxyStorage.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyStorage.setStatus(_B)
_SgProxyNumObjects_Type=Gauge32
_SgProxyNumObjects_Object=MibScalar
sgProxyNumObjects=_SgProxyNumObjects_Object((1,3,6,1,4,1,3417,2,11,2,2,2),_SgProxyNumObjects_Type())
sgProxyNumObjects.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyNumObjects.setStatus(_B)
_SgProxyMemory_ObjectIdentity=ObjectIdentity
sgProxyMemory=_SgProxyMemory_ObjectIdentity((1,3,6,1,4,1,3417,2,11,2,3))
_SgProxyMemAvailable_Type=Counter64
_SgProxyMemAvailable_Object=MibScalar
sgProxyMemAvailable=_SgProxyMemAvailable_Object((1,3,6,1,4,1,3417,2,11,2,3,1),_SgProxyMemAvailable_Type())
sgProxyMemAvailable.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyMemAvailable.setStatus(_B)
if mibBuilder.loadTexts:sgProxyMemAvailable.setUnits(_D)
_SgProxyMemCacheUsage_Type=Counter64
_SgProxyMemCacheUsage_Object=MibScalar
sgProxyMemCacheUsage=_SgProxyMemCacheUsage_Object((1,3,6,1,4,1,3417,2,11,2,3,2),_SgProxyMemCacheUsage_Type())
sgProxyMemCacheUsage.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyMemCacheUsage.setStatus(_B)
if mibBuilder.loadTexts:sgProxyMemCacheUsage.setUnits(_D)
_SgProxyMemSysUsage_Type=Counter64
_SgProxyMemSysUsage_Object=MibScalar
sgProxyMemSysUsage=_SgProxyMemSysUsage_Object((1,3,6,1,4,1,3417,2,11,2,3,3),_SgProxyMemSysUsage_Type())
sgProxyMemSysUsage.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyMemSysUsage.setStatus(_B)
if mibBuilder.loadTexts:sgProxyMemSysUsage.setUnits(_D)
_SgProxyMemoryPressure_Type=Gauge32
_SgProxyMemoryPressure_Object=MibScalar
sgProxyMemoryPressure=_SgProxyMemoryPressure_Object((1,3,6,1,4,1,3417,2,11,2,3,4),_SgProxyMemoryPressure_Type())
sgProxyMemoryPressure.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyMemoryPressure.setStatus(_B)
if mibBuilder.loadTexts:sgProxyMemoryPressure.setUnits(_F)
_SgProxyCpuCoreTable_Object=MibTable
sgProxyCpuCoreTable=_SgProxyCpuCoreTable_Object((1,3,6,1,4,1,3417,2,11,2,4))
if mibBuilder.loadTexts:sgProxyCpuCoreTable.setStatus(_B)
_SgProxyCpuCoreTableEntry_Object=MibTableRow
sgProxyCpuCoreTableEntry=_SgProxyCpuCoreTableEntry_Object((1,3,6,1,4,1,3417,2,11,2,4,1))
sgProxyCpuCoreTableEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:sgProxyCpuCoreTableEntry.setStatus(_B)
class _SgProxyCpuCoreIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_SgProxyCpuCoreIndex_Type.__name__=_H
_SgProxyCpuCoreIndex_Object=MibTableColumn
sgProxyCpuCoreIndex=_SgProxyCpuCoreIndex_Object((1,3,6,1,4,1,3417,2,11,2,4,1,1),_SgProxyCpuCoreIndex_Type())
sgProxyCpuCoreIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:sgProxyCpuCoreIndex.setStatus(_B)
_SgProxyCpuCoreUpTime_Type=Counter64
_SgProxyCpuCoreUpTime_Object=MibTableColumn
sgProxyCpuCoreUpTime=_SgProxyCpuCoreUpTime_Object((1,3,6,1,4,1,3417,2,11,2,4,1,2),_SgProxyCpuCoreUpTime_Type())
sgProxyCpuCoreUpTime.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyCpuCoreUpTime.setStatus(_B)
if mibBuilder.loadTexts:sgProxyCpuCoreUpTime.setUnits(_C)
_SgProxyCpuCoreBusyTime_Type=Counter64
_SgProxyCpuCoreBusyTime_Object=MibTableColumn
sgProxyCpuCoreBusyTime=_SgProxyCpuCoreBusyTime_Object((1,3,6,1,4,1,3417,2,11,2,4,1,3),_SgProxyCpuCoreBusyTime_Type())
sgProxyCpuCoreBusyTime.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyCpuCoreBusyTime.setStatus(_B)
if mibBuilder.loadTexts:sgProxyCpuCoreBusyTime.setUnits(_C)
_SgProxyCpuCoreIdleTime_Type=Counter64
_SgProxyCpuCoreIdleTime_Object=MibTableColumn
sgProxyCpuCoreIdleTime=_SgProxyCpuCoreIdleTime_Object((1,3,6,1,4,1,3417,2,11,2,4,1,4),_SgProxyCpuCoreIdleTime_Type())
sgProxyCpuCoreIdleTime.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyCpuCoreIdleTime.setStatus(_B)
if mibBuilder.loadTexts:sgProxyCpuCoreIdleTime.setUnits(_C)
_SgProxyCpuCoreUpTimeSinceLastAccess_Type=Counter64
_SgProxyCpuCoreUpTimeSinceLastAccess_Object=MibTableColumn
sgProxyCpuCoreUpTimeSinceLastAccess=_SgProxyCpuCoreUpTimeSinceLastAccess_Object((1,3,6,1,4,1,3417,2,11,2,4,1,5),_SgProxyCpuCoreUpTimeSinceLastAccess_Type())
sgProxyCpuCoreUpTimeSinceLastAccess.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyCpuCoreUpTimeSinceLastAccess.setStatus(_B)
if mibBuilder.loadTexts:sgProxyCpuCoreUpTimeSinceLastAccess.setUnits(_C)
_SgProxyCpuCoreBusyTimeSinceLastAccess_Type=Counter64
_SgProxyCpuCoreBusyTimeSinceLastAccess_Object=MibTableColumn
sgProxyCpuCoreBusyTimeSinceLastAccess=_SgProxyCpuCoreBusyTimeSinceLastAccess_Object((1,3,6,1,4,1,3417,2,11,2,4,1,6),_SgProxyCpuCoreBusyTimeSinceLastAccess_Type())
sgProxyCpuCoreBusyTimeSinceLastAccess.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyCpuCoreBusyTimeSinceLastAccess.setStatus(_B)
if mibBuilder.loadTexts:sgProxyCpuCoreBusyTimeSinceLastAccess.setUnits(_C)
_SgProxyCpuCoreIdleTimeSinceLastAccess_Type=Counter64
_SgProxyCpuCoreIdleTimeSinceLastAccess_Object=MibTableColumn
sgProxyCpuCoreIdleTimeSinceLastAccess=_SgProxyCpuCoreIdleTimeSinceLastAccess_Object((1,3,6,1,4,1,3417,2,11,2,4,1,7),_SgProxyCpuCoreIdleTimeSinceLastAccess_Type())
sgProxyCpuCoreIdleTimeSinceLastAccess.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyCpuCoreIdleTimeSinceLastAccess.setStatus(_B)
if mibBuilder.loadTexts:sgProxyCpuCoreIdleTimeSinceLastAccess.setUnits(_C)
_SgProxyCpuCoreBusyPerCent_Type=Gauge32
_SgProxyCpuCoreBusyPerCent_Object=MibTableColumn
sgProxyCpuCoreBusyPerCent=_SgProxyCpuCoreBusyPerCent_Object((1,3,6,1,4,1,3417,2,11,2,4,1,8),_SgProxyCpuCoreBusyPerCent_Type())
sgProxyCpuCoreBusyPerCent.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyCpuCoreBusyPerCent.setStatus(_B)
if mibBuilder.loadTexts:sgProxyCpuCoreBusyPerCent.setUnits(_F)
_SgProxyCpuCoreIdlePerCent_Type=Gauge32
_SgProxyCpuCoreIdlePerCent_Object=MibTableColumn
sgProxyCpuCoreIdlePerCent=_SgProxyCpuCoreIdlePerCent_Object((1,3,6,1,4,1,3417,2,11,2,4,1,9),_SgProxyCpuCoreIdlePerCent_Type())
sgProxyCpuCoreIdlePerCent.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyCpuCoreIdlePerCent.setStatus(_B)
if mibBuilder.loadTexts:sgProxyCpuCoreIdlePerCent.setUnits(_F)
_SgProxyHttp_ObjectIdentity=ObjectIdentity
sgProxyHttp=_SgProxyHttp_ObjectIdentity((1,3,6,1,4,1,3417,2,11,3))
_SgProxyHttpPerf_ObjectIdentity=ObjectIdentity
sgProxyHttpPerf=_SgProxyHttpPerf_ObjectIdentity((1,3,6,1,4,1,3417,2,11,3,1))
_SgProxyHttpClient_ObjectIdentity=ObjectIdentity
sgProxyHttpClient=_SgProxyHttpClient_ObjectIdentity((1,3,6,1,4,1,3417,2,11,3,1,1))
_SgProxyHttpClientRequests_Type=Counter64
_SgProxyHttpClientRequests_Object=MibScalar
sgProxyHttpClientRequests=_SgProxyHttpClientRequests_Object((1,3,6,1,4,1,3417,2,11,3,1,1,1),_SgProxyHttpClientRequests_Type())
sgProxyHttpClientRequests.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyHttpClientRequests.setStatus(_B)
_SgProxyHttpClientHits_Type=Counter64
_SgProxyHttpClientHits_Object=MibScalar
sgProxyHttpClientHits=_SgProxyHttpClientHits_Object((1,3,6,1,4,1,3417,2,11,3,1,1,2),_SgProxyHttpClientHits_Type())
sgProxyHttpClientHits.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyHttpClientHits.setStatus(_B)
_SgProxyHttpClientPartialHits_Type=Counter64
_SgProxyHttpClientPartialHits_Object=MibScalar
sgProxyHttpClientPartialHits=_SgProxyHttpClientPartialHits_Object((1,3,6,1,4,1,3417,2,11,3,1,1,3),_SgProxyHttpClientPartialHits_Type())
sgProxyHttpClientPartialHits.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyHttpClientPartialHits.setStatus(_B)
_SgProxyHttpClientMisses_Type=Counter64
_SgProxyHttpClientMisses_Object=MibScalar
sgProxyHttpClientMisses=_SgProxyHttpClientMisses_Object((1,3,6,1,4,1,3417,2,11,3,1,1,4),_SgProxyHttpClientMisses_Type())
sgProxyHttpClientMisses.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyHttpClientMisses.setStatus(_B)
_SgProxyHttpClientErrors_Type=Counter64
_SgProxyHttpClientErrors_Object=MibScalar
sgProxyHttpClientErrors=_SgProxyHttpClientErrors_Object((1,3,6,1,4,1,3417,2,11,3,1,1,5),_SgProxyHttpClientErrors_Type())
sgProxyHttpClientErrors.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyHttpClientErrors.setStatus(_B)
_SgProxyHttpClientRequestRate_Type=Gauge32
_SgProxyHttpClientRequestRate_Object=MibScalar
sgProxyHttpClientRequestRate=_SgProxyHttpClientRequestRate_Object((1,3,6,1,4,1,3417,2,11,3,1,1,6),_SgProxyHttpClientRequestRate_Type())
sgProxyHttpClientRequestRate.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyHttpClientRequestRate.setStatus(_B)
if mibBuilder.loadTexts:sgProxyHttpClientRequestRate.setUnits('Requests Per Second')
_SgProxyHttpClientHitRate_Type=Gauge32
_SgProxyHttpClientHitRate_Object=MibScalar
sgProxyHttpClientHitRate=_SgProxyHttpClientHitRate_Object((1,3,6,1,4,1,3417,2,11,3,1,1,7),_SgProxyHttpClientHitRate_Type())
sgProxyHttpClientHitRate.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyHttpClientHitRate.setStatus(_B)
if mibBuilder.loadTexts:sgProxyHttpClientHitRate.setUnits(_F)
_SgProxyHttpClientByteHitRate_Type=Gauge32
_SgProxyHttpClientByteHitRate_Object=MibScalar
sgProxyHttpClientByteHitRate=_SgProxyHttpClientByteHitRate_Object((1,3,6,1,4,1,3417,2,11,3,1,1,8),_SgProxyHttpClientByteHitRate_Type())
sgProxyHttpClientByteHitRate.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyHttpClientByteHitRate.setStatus(_B)
if mibBuilder.loadTexts:sgProxyHttpClientByteHitRate.setUnits(_F)
_SgProxyHttpClientInBytes_Type=Counter64
_SgProxyHttpClientInBytes_Object=MibScalar
sgProxyHttpClientInBytes=_SgProxyHttpClientInBytes_Object((1,3,6,1,4,1,3417,2,11,3,1,1,9),_SgProxyHttpClientInBytes_Type())
sgProxyHttpClientInBytes.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyHttpClientInBytes.setStatus(_B)
if mibBuilder.loadTexts:sgProxyHttpClientInBytes.setUnits(_D)
_SgProxyHttpClientOutBytes_Type=Counter64
_SgProxyHttpClientOutBytes_Object=MibScalar
sgProxyHttpClientOutBytes=_SgProxyHttpClientOutBytes_Object((1,3,6,1,4,1,3417,2,11,3,1,1,10),_SgProxyHttpClientOutBytes_Type())
sgProxyHttpClientOutBytes.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyHttpClientOutBytes.setStatus(_B)
if mibBuilder.loadTexts:sgProxyHttpClientOutBytes.setUnits(_D)
_SgProxyHttpServer_ObjectIdentity=ObjectIdentity
sgProxyHttpServer=_SgProxyHttpServer_ObjectIdentity((1,3,6,1,4,1,3417,2,11,3,1,2))
_SgProxyHttpServerRequests_Type=Counter64
_SgProxyHttpServerRequests_Object=MibScalar
sgProxyHttpServerRequests=_SgProxyHttpServerRequests_Object((1,3,6,1,4,1,3417,2,11,3,1,2,1),_SgProxyHttpServerRequests_Type())
sgProxyHttpServerRequests.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyHttpServerRequests.setStatus(_B)
_SgProxyHttpServerErrors_Type=Counter64
_SgProxyHttpServerErrors_Object=MibScalar
sgProxyHttpServerErrors=_SgProxyHttpServerErrors_Object((1,3,6,1,4,1,3417,2,11,3,1,2,2),_SgProxyHttpServerErrors_Type())
sgProxyHttpServerErrors.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyHttpServerErrors.setStatus(_B)
_SgProxyHttpServerInBytes_Type=Counter64
_SgProxyHttpServerInBytes_Object=MibScalar
sgProxyHttpServerInBytes=_SgProxyHttpServerInBytes_Object((1,3,6,1,4,1,3417,2,11,3,1,2,3),_SgProxyHttpServerInBytes_Type())
sgProxyHttpServerInBytes.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyHttpServerInBytes.setStatus(_B)
if mibBuilder.loadTexts:sgProxyHttpServerInBytes.setUnits(_D)
_SgProxyHttpServerOutBytes_Type=Counter64
_SgProxyHttpServerOutBytes_Object=MibScalar
sgProxyHttpServerOutBytes=_SgProxyHttpServerOutBytes_Object((1,3,6,1,4,1,3417,2,11,3,1,2,4),_SgProxyHttpServerOutBytes_Type())
sgProxyHttpServerOutBytes.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyHttpServerOutBytes.setStatus(_B)
if mibBuilder.loadTexts:sgProxyHttpServerOutBytes.setUnits(_D)
_SgProxyHttpConnections_ObjectIdentity=ObjectIdentity
sgProxyHttpConnections=_SgProxyHttpConnections_ObjectIdentity((1,3,6,1,4,1,3417,2,11,3,1,3))
_SgProxyHttpClientConnections_Type=Gauge32
_SgProxyHttpClientConnections_Object=MibScalar
sgProxyHttpClientConnections=_SgProxyHttpClientConnections_Object((1,3,6,1,4,1,3417,2,11,3,1,3,1),_SgProxyHttpClientConnections_Type())
sgProxyHttpClientConnections.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyHttpClientConnections.setStatus(_B)
_SgProxyHttpClientConnectionsActive_Type=Gauge32
_SgProxyHttpClientConnectionsActive_Object=MibScalar
sgProxyHttpClientConnectionsActive=_SgProxyHttpClientConnectionsActive_Object((1,3,6,1,4,1,3417,2,11,3,1,3,2),_SgProxyHttpClientConnectionsActive_Type())
sgProxyHttpClientConnectionsActive.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyHttpClientConnectionsActive.setStatus(_B)
_SgProxyHttpClientConnectionsIdle_Type=Gauge32
_SgProxyHttpClientConnectionsIdle_Object=MibScalar
sgProxyHttpClientConnectionsIdle=_SgProxyHttpClientConnectionsIdle_Object((1,3,6,1,4,1,3417,2,11,3,1,3,3),_SgProxyHttpClientConnectionsIdle_Type())
sgProxyHttpClientConnectionsIdle.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyHttpClientConnectionsIdle.setStatus(_B)
_SgProxyHttpServerConnections_Type=Gauge32
_SgProxyHttpServerConnections_Object=MibScalar
sgProxyHttpServerConnections=_SgProxyHttpServerConnections_Object((1,3,6,1,4,1,3417,2,11,3,1,3,4),_SgProxyHttpServerConnections_Type())
sgProxyHttpServerConnections.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyHttpServerConnections.setStatus(_B)
_SgProxyHttpServerConnectionsActive_Type=Gauge32
_SgProxyHttpServerConnectionsActive_Object=MibScalar
sgProxyHttpServerConnectionsActive=_SgProxyHttpServerConnectionsActive_Object((1,3,6,1,4,1,3417,2,11,3,1,3,5),_SgProxyHttpServerConnectionsActive_Type())
sgProxyHttpServerConnectionsActive.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyHttpServerConnectionsActive.setStatus(_B)
_SgProxyHttpServerConnectionsIdle_Type=Gauge32
_SgProxyHttpServerConnectionsIdle_Object=MibScalar
sgProxyHttpServerConnectionsIdle=_SgProxyHttpServerConnectionsIdle_Object((1,3,6,1,4,1,3417,2,11,3,1,3,6),_SgProxyHttpServerConnectionsIdle_Type())
sgProxyHttpServerConnectionsIdle.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyHttpServerConnectionsIdle.setStatus(_B)
_SgProxyHttpResponse_ObjectIdentity=ObjectIdentity
sgProxyHttpResponse=_SgProxyHttpResponse_ObjectIdentity((1,3,6,1,4,1,3417,2,11,3,2))
_SgProxyHttpResponseTime_ObjectIdentity=ObjectIdentity
sgProxyHttpResponseTime=_SgProxyHttpResponseTime_ObjectIdentity((1,3,6,1,4,1,3417,2,11,3,2,1))
_SgProxyHttpServiceTimeAll_Type=Gauge32
_SgProxyHttpServiceTimeAll_Object=MibScalar
sgProxyHttpServiceTimeAll=_SgProxyHttpServiceTimeAll_Object((1,3,6,1,4,1,3417,2,11,3,2,1,1),_SgProxyHttpServiceTimeAll_Type())
sgProxyHttpServiceTimeAll.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyHttpServiceTimeAll.setStatus(_B)
if mibBuilder.loadTexts:sgProxyHttpServiceTimeAll.setUnits(_C)
_SgProxyHttpServiceTimeHit_Type=Gauge32
_SgProxyHttpServiceTimeHit_Object=MibScalar
sgProxyHttpServiceTimeHit=_SgProxyHttpServiceTimeHit_Object((1,3,6,1,4,1,3417,2,11,3,2,1,2),_SgProxyHttpServiceTimeHit_Type())
sgProxyHttpServiceTimeHit.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyHttpServiceTimeHit.setStatus(_B)
if mibBuilder.loadTexts:sgProxyHttpServiceTimeHit.setUnits(_C)
_SgProxyHttpServiceTimePartialHit_Type=Gauge32
_SgProxyHttpServiceTimePartialHit_Object=MibScalar
sgProxyHttpServiceTimePartialHit=_SgProxyHttpServiceTimePartialHit_Object((1,3,6,1,4,1,3417,2,11,3,2,1,3),_SgProxyHttpServiceTimePartialHit_Type())
sgProxyHttpServiceTimePartialHit.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyHttpServiceTimePartialHit.setStatus(_B)
if mibBuilder.loadTexts:sgProxyHttpServiceTimePartialHit.setUnits(_C)
_SgProxyHttpServiceTimeMiss_Type=Gauge32
_SgProxyHttpServiceTimeMiss_Object=MibScalar
sgProxyHttpServiceTimeMiss=_SgProxyHttpServiceTimeMiss_Object((1,3,6,1,4,1,3417,2,11,3,2,1,4),_SgProxyHttpServiceTimeMiss_Type())
sgProxyHttpServiceTimeMiss.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyHttpServiceTimeMiss.setStatus(_B)
if mibBuilder.loadTexts:sgProxyHttpServiceTimeMiss.setUnits(_C)
_SgProxyHttpTotalFetchTimeAll_Type=Counter64
_SgProxyHttpTotalFetchTimeAll_Object=MibScalar
sgProxyHttpTotalFetchTimeAll=_SgProxyHttpTotalFetchTimeAll_Object((1,3,6,1,4,1,3417,2,11,3,2,1,5),_SgProxyHttpTotalFetchTimeAll_Type())
sgProxyHttpTotalFetchTimeAll.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyHttpTotalFetchTimeAll.setStatus(_B)
if mibBuilder.loadTexts:sgProxyHttpTotalFetchTimeAll.setUnits(_C)
_SgProxyHttpTotalFetchTimeHit_Type=Counter64
_SgProxyHttpTotalFetchTimeHit_Object=MibScalar
sgProxyHttpTotalFetchTimeHit=_SgProxyHttpTotalFetchTimeHit_Object((1,3,6,1,4,1,3417,2,11,3,2,1,6),_SgProxyHttpTotalFetchTimeHit_Type())
sgProxyHttpTotalFetchTimeHit.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyHttpTotalFetchTimeHit.setStatus(_B)
if mibBuilder.loadTexts:sgProxyHttpTotalFetchTimeHit.setUnits(_C)
_SgProxyHttpTotalFetchTimePartialHit_Type=Counter64
_SgProxyHttpTotalFetchTimePartialHit_Object=MibScalar
sgProxyHttpTotalFetchTimePartialHit=_SgProxyHttpTotalFetchTimePartialHit_Object((1,3,6,1,4,1,3417,2,11,3,2,1,7),_SgProxyHttpTotalFetchTimePartialHit_Type())
sgProxyHttpTotalFetchTimePartialHit.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyHttpTotalFetchTimePartialHit.setStatus(_B)
if mibBuilder.loadTexts:sgProxyHttpTotalFetchTimePartialHit.setUnits(_C)
_SgProxyHttpTotalFetchTimeMiss_Type=Counter64
_SgProxyHttpTotalFetchTimeMiss_Object=MibScalar
sgProxyHttpTotalFetchTimeMiss=_SgProxyHttpTotalFetchTimeMiss_Object((1,3,6,1,4,1,3417,2,11,3,2,1,8),_SgProxyHttpTotalFetchTimeMiss_Type())
sgProxyHttpTotalFetchTimeMiss.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyHttpTotalFetchTimeMiss.setStatus(_B)
if mibBuilder.loadTexts:sgProxyHttpTotalFetchTimeMiss.setUnits(_C)
_SgProxyHttpResponseFirstByte_ObjectIdentity=ObjectIdentity
sgProxyHttpResponseFirstByte=_SgProxyHttpResponseFirstByte_ObjectIdentity((1,3,6,1,4,1,3417,2,11,3,2,2))
_SgProxyHttpFirstByteAll_Type=Gauge32
_SgProxyHttpFirstByteAll_Object=MibScalar
sgProxyHttpFirstByteAll=_SgProxyHttpFirstByteAll_Object((1,3,6,1,4,1,3417,2,11,3,2,2,1),_SgProxyHttpFirstByteAll_Type())
sgProxyHttpFirstByteAll.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyHttpFirstByteAll.setStatus(_B)
if mibBuilder.loadTexts:sgProxyHttpFirstByteAll.setUnits(_C)
_SgProxyHttpFirstByteHit_Type=Gauge32
_SgProxyHttpFirstByteHit_Object=MibScalar
sgProxyHttpFirstByteHit=_SgProxyHttpFirstByteHit_Object((1,3,6,1,4,1,3417,2,11,3,2,2,2),_SgProxyHttpFirstByteHit_Type())
sgProxyHttpFirstByteHit.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyHttpFirstByteHit.setStatus(_B)
if mibBuilder.loadTexts:sgProxyHttpFirstByteHit.setUnits(_C)
_SgProxyHttpFirstBytePartialHit_Type=Gauge32
_SgProxyHttpFirstBytePartialHit_Object=MibScalar
sgProxyHttpFirstBytePartialHit=_SgProxyHttpFirstBytePartialHit_Object((1,3,6,1,4,1,3417,2,11,3,2,2,3),_SgProxyHttpFirstBytePartialHit_Type())
sgProxyHttpFirstBytePartialHit.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyHttpFirstBytePartialHit.setStatus(_B)
if mibBuilder.loadTexts:sgProxyHttpFirstBytePartialHit.setUnits(_C)
_SgProxyHttpFirstByteMiss_Type=Gauge32
_SgProxyHttpFirstByteMiss_Object=MibScalar
sgProxyHttpFirstByteMiss=_SgProxyHttpFirstByteMiss_Object((1,3,6,1,4,1,3417,2,11,3,2,2,4),_SgProxyHttpFirstByteMiss_Type())
sgProxyHttpFirstByteMiss.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyHttpFirstByteMiss.setStatus(_B)
if mibBuilder.loadTexts:sgProxyHttpFirstByteMiss.setUnits(_C)
_SgProxyHttpResponseByteRate_ObjectIdentity=ObjectIdentity
sgProxyHttpResponseByteRate=_SgProxyHttpResponseByteRate_ObjectIdentity((1,3,6,1,4,1,3417,2,11,3,2,3))
_SgProxyHttpByteRateAll_Type=Gauge32
_SgProxyHttpByteRateAll_Object=MibScalar
sgProxyHttpByteRateAll=_SgProxyHttpByteRateAll_Object((1,3,6,1,4,1,3417,2,11,3,2,3,1),_SgProxyHttpByteRateAll_Type())
sgProxyHttpByteRateAll.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyHttpByteRateAll.setStatus(_B)
if mibBuilder.loadTexts:sgProxyHttpByteRateAll.setUnits(_G)
_SgProxyHttpByteRateHit_Type=Gauge32
_SgProxyHttpByteRateHit_Object=MibScalar
sgProxyHttpByteRateHit=_SgProxyHttpByteRateHit_Object((1,3,6,1,4,1,3417,2,11,3,2,3,2),_SgProxyHttpByteRateHit_Type())
sgProxyHttpByteRateHit.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyHttpByteRateHit.setStatus(_B)
if mibBuilder.loadTexts:sgProxyHttpByteRateHit.setUnits(_G)
_SgProxyHttpByteRatePartialHit_Type=Gauge32
_SgProxyHttpByteRatePartialHit_Object=MibScalar
sgProxyHttpByteRatePartialHit=_SgProxyHttpByteRatePartialHit_Object((1,3,6,1,4,1,3417,2,11,3,2,3,3),_SgProxyHttpByteRatePartialHit_Type())
sgProxyHttpByteRatePartialHit.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyHttpByteRatePartialHit.setStatus(_B)
if mibBuilder.loadTexts:sgProxyHttpByteRatePartialHit.setUnits(_G)
_SgProxyHttpByteRateMiss_Type=Gauge32
_SgProxyHttpByteRateMiss_Object=MibScalar
sgProxyHttpByteRateMiss=_SgProxyHttpByteRateMiss_Object((1,3,6,1,4,1,3417,2,11,3,2,3,4),_SgProxyHttpByteRateMiss_Type())
sgProxyHttpByteRateMiss.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyHttpByteRateMiss.setStatus(_B)
if mibBuilder.loadTexts:sgProxyHttpByteRateMiss.setUnits(_G)
_SgProxyHttpResponseSize_ObjectIdentity=ObjectIdentity
sgProxyHttpResponseSize=_SgProxyHttpResponseSize_ObjectIdentity((1,3,6,1,4,1,3417,2,11,3,2,4))
_SgProxyHttpResponseSizeAll_Type=Gauge32
_SgProxyHttpResponseSizeAll_Object=MibScalar
sgProxyHttpResponseSizeAll=_SgProxyHttpResponseSizeAll_Object((1,3,6,1,4,1,3417,2,11,3,2,4,1),_SgProxyHttpResponseSizeAll_Type())
sgProxyHttpResponseSizeAll.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyHttpResponseSizeAll.setStatus(_B)
if mibBuilder.loadTexts:sgProxyHttpResponseSizeAll.setUnits(_D)
_SgProxyHttpResponseSizeHit_Type=Gauge32
_SgProxyHttpResponseSizeHit_Object=MibScalar
sgProxyHttpResponseSizeHit=_SgProxyHttpResponseSizeHit_Object((1,3,6,1,4,1,3417,2,11,3,2,4,2),_SgProxyHttpResponseSizeHit_Type())
sgProxyHttpResponseSizeHit.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyHttpResponseSizeHit.setStatus(_B)
if mibBuilder.loadTexts:sgProxyHttpResponseSizeHit.setUnits(_D)
_SgProxyHttpResponseSizePartialHit_Type=Gauge32
_SgProxyHttpResponseSizePartialHit_Object=MibScalar
sgProxyHttpResponseSizePartialHit=_SgProxyHttpResponseSizePartialHit_Object((1,3,6,1,4,1,3417,2,11,3,2,4,3),_SgProxyHttpResponseSizePartialHit_Type())
sgProxyHttpResponseSizePartialHit.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyHttpResponseSizePartialHit.setStatus(_B)
if mibBuilder.loadTexts:sgProxyHttpResponseSizePartialHit.setUnits(_D)
_SgProxyHttpResponseSizeMiss_Type=Gauge32
_SgProxyHttpResponseSizeMiss_Object=MibScalar
sgProxyHttpResponseSizeMiss=_SgProxyHttpResponseSizeMiss_Object((1,3,6,1,4,1,3417,2,11,3,2,4,4),_SgProxyHttpResponseSizeMiss_Type())
sgProxyHttpResponseSizeMiss.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyHttpResponseSizeMiss.setStatus(_B)
if mibBuilder.loadTexts:sgProxyHttpResponseSizeMiss.setUnits(_D)
_SgProxyHttpMedian_ObjectIdentity=ObjectIdentity
sgProxyHttpMedian=_SgProxyHttpMedian_ObjectIdentity((1,3,6,1,4,1,3417,2,11,3,3))
_SgProxyHttpMedianServiceTable_Object=MibTable
sgProxyHttpMedianServiceTable=_SgProxyHttpMedianServiceTable_Object((1,3,6,1,4,1,3417,2,11,3,3,1))
if mibBuilder.loadTexts:sgProxyHttpMedianServiceTable.setStatus(_B)
_SgProxyHttpMedianServiceEntry_Object=MibTableRow
sgProxyHttpMedianServiceEntry=_SgProxyHttpMedianServiceEntry_Object((1,3,6,1,4,1,3417,2,11,3,3,1,1))
sgProxyHttpMedianServiceEntry.setIndexNames((0,_I,_L))
if mibBuilder.loadTexts:sgProxyHttpMedianServiceEntry.setStatus(_B)
class _SgProxyHttpMedianServiceTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,5,60)));namedValues=NamedValues(*(('one',1),('five',5),('sixty',60)))
_SgProxyHttpMedianServiceTime_Type.__name__=_H
_SgProxyHttpMedianServiceTime_Object=MibTableColumn
sgProxyHttpMedianServiceTime=_SgProxyHttpMedianServiceTime_Object((1,3,6,1,4,1,3417,2,11,3,3,1,1,1),_SgProxyHttpMedianServiceTime_Type())
sgProxyHttpMedianServiceTime.setMaxAccess(_K)
if mibBuilder.loadTexts:sgProxyHttpMedianServiceTime.setStatus(_B)
if mibBuilder.loadTexts:sgProxyHttpMedianServiceTime.setUnits('Minutes')
_SgProxyHttpMedianServiceTimeAll_Type=Gauge32
_SgProxyHttpMedianServiceTimeAll_Object=MibTableColumn
sgProxyHttpMedianServiceTimeAll=_SgProxyHttpMedianServiceTimeAll_Object((1,3,6,1,4,1,3417,2,11,3,3,1,1,2),_SgProxyHttpMedianServiceTimeAll_Type())
sgProxyHttpMedianServiceTimeAll.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyHttpMedianServiceTimeAll.setStatus(_B)
if mibBuilder.loadTexts:sgProxyHttpMedianServiceTimeAll.setUnits(_C)
_SgProxyHttpMedianServiceTimeHit_Type=Gauge32
_SgProxyHttpMedianServiceTimeHit_Object=MibTableColumn
sgProxyHttpMedianServiceTimeHit=_SgProxyHttpMedianServiceTimeHit_Object((1,3,6,1,4,1,3417,2,11,3,3,1,1,3),_SgProxyHttpMedianServiceTimeHit_Type())
sgProxyHttpMedianServiceTimeHit.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyHttpMedianServiceTimeHit.setStatus(_B)
if mibBuilder.loadTexts:sgProxyHttpMedianServiceTimeHit.setUnits(_C)
_SgProxyHttpMedianServiceTimePartialHit_Type=Gauge32
_SgProxyHttpMedianServiceTimePartialHit_Object=MibTableColumn
sgProxyHttpMedianServiceTimePartialHit=_SgProxyHttpMedianServiceTimePartialHit_Object((1,3,6,1,4,1,3417,2,11,3,3,1,1,4),_SgProxyHttpMedianServiceTimePartialHit_Type())
sgProxyHttpMedianServiceTimePartialHit.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyHttpMedianServiceTimePartialHit.setStatus(_B)
if mibBuilder.loadTexts:sgProxyHttpMedianServiceTimePartialHit.setUnits(_C)
_SgProxyHttpMedianServiceTimeMiss_Type=Gauge32
_SgProxyHttpMedianServiceTimeMiss_Object=MibTableColumn
sgProxyHttpMedianServiceTimeMiss=_SgProxyHttpMedianServiceTimeMiss_Object((1,3,6,1,4,1,3417,2,11,3,3,1,1,5),_SgProxyHttpMedianServiceTimeMiss_Type())
sgProxyHttpMedianServiceTimeMiss.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyHttpMedianServiceTimeMiss.setStatus(_B)
if mibBuilder.loadTexts:sgProxyHttpMedianServiceTimeMiss.setUnits(_C)
_SgProxyDnsMedianServiceTime_Type=Gauge32
_SgProxyDnsMedianServiceTime_Object=MibTableColumn
sgProxyDnsMedianServiceTime=_SgProxyDnsMedianServiceTime_Object((1,3,6,1,4,1,3417,2,11,3,3,1,1,6),_SgProxyDnsMedianServiceTime_Type())
sgProxyDnsMedianServiceTime.setMaxAccess(_A)
if mibBuilder.loadTexts:sgProxyDnsMedianServiceTime.setStatus(_B)
if mibBuilder.loadTexts:sgProxyDnsMedianServiceTime.setUnits(_C)
mibBuilder.exportSymbols(_I,**{'bluecoatSGProxyMIB':bluecoatSGProxyMIB,'sgProxyConfig':sgProxyConfig,'sgProxyAdmin':sgProxyAdmin,'sgProxySoftware':sgProxySoftware,'sgProxyVersion':sgProxyVersion,'sgProxySerialNumber':sgProxySerialNumber,'sgProxySystem':sgProxySystem,'sgProxyCpu':sgProxyCpu,'sgProxyCpuUpTime':sgProxyCpuUpTime,'sgProxyCpuBusyTime':sgProxyCpuBusyTime,'sgProxyCpuIdleTime':sgProxyCpuIdleTime,'sgProxyCpuUpTimeSinceLastAccess':sgProxyCpuUpTimeSinceLastAccess,'sgProxyCpuBusyTimeSinceLastAccess':sgProxyCpuBusyTimeSinceLastAccess,'sgProxyCpuIdleTimeSinceLastAccess':sgProxyCpuIdleTimeSinceLastAccess,'sgProxyCpuBusyPerCent':sgProxyCpuBusyPerCent,'sgProxyCpuIdlePerCent':sgProxyCpuIdlePerCent,'sgProxyCache':sgProxyCache,'sgProxyStorage':sgProxyStorage,'sgProxyNumObjects':sgProxyNumObjects,'sgProxyMemory':sgProxyMemory,'sgProxyMemAvailable':sgProxyMemAvailable,'sgProxyMemCacheUsage':sgProxyMemCacheUsage,'sgProxyMemSysUsage':sgProxyMemSysUsage,'sgProxyMemoryPressure':sgProxyMemoryPressure,'sgProxyCpuCoreTable':sgProxyCpuCoreTable,'sgProxyCpuCoreTableEntry':sgProxyCpuCoreTableEntry,_J:sgProxyCpuCoreIndex,'sgProxyCpuCoreUpTime':sgProxyCpuCoreUpTime,'sgProxyCpuCoreBusyTime':sgProxyCpuCoreBusyTime,'sgProxyCpuCoreIdleTime':sgProxyCpuCoreIdleTime,'sgProxyCpuCoreUpTimeSinceLastAccess':sgProxyCpuCoreUpTimeSinceLastAccess,'sgProxyCpuCoreBusyTimeSinceLastAccess':sgProxyCpuCoreBusyTimeSinceLastAccess,'sgProxyCpuCoreIdleTimeSinceLastAccess':sgProxyCpuCoreIdleTimeSinceLastAccess,'sgProxyCpuCoreBusyPerCent':sgProxyCpuCoreBusyPerCent,'sgProxyCpuCoreIdlePerCent':sgProxyCpuCoreIdlePerCent,'sgProxyHttp':sgProxyHttp,'sgProxyHttpPerf':sgProxyHttpPerf,'sgProxyHttpClient':sgProxyHttpClient,'sgProxyHttpClientRequests':sgProxyHttpClientRequests,'sgProxyHttpClientHits':sgProxyHttpClientHits,'sgProxyHttpClientPartialHits':sgProxyHttpClientPartialHits,'sgProxyHttpClientMisses':sgProxyHttpClientMisses,'sgProxyHttpClientErrors':sgProxyHttpClientErrors,'sgProxyHttpClientRequestRate':sgProxyHttpClientRequestRate,'sgProxyHttpClientHitRate':sgProxyHttpClientHitRate,'sgProxyHttpClientByteHitRate':sgProxyHttpClientByteHitRate,'sgProxyHttpClientInBytes':sgProxyHttpClientInBytes,'sgProxyHttpClientOutBytes':sgProxyHttpClientOutBytes,'sgProxyHttpServer':sgProxyHttpServer,'sgProxyHttpServerRequests':sgProxyHttpServerRequests,'sgProxyHttpServerErrors':sgProxyHttpServerErrors,'sgProxyHttpServerInBytes':sgProxyHttpServerInBytes,'sgProxyHttpServerOutBytes':sgProxyHttpServerOutBytes,'sgProxyHttpConnections':sgProxyHttpConnections,'sgProxyHttpClientConnections':sgProxyHttpClientConnections,'sgProxyHttpClientConnectionsActive':sgProxyHttpClientConnectionsActive,'sgProxyHttpClientConnectionsIdle':sgProxyHttpClientConnectionsIdle,'sgProxyHttpServerConnections':sgProxyHttpServerConnections,'sgProxyHttpServerConnectionsActive':sgProxyHttpServerConnectionsActive,'sgProxyHttpServerConnectionsIdle':sgProxyHttpServerConnectionsIdle,'sgProxyHttpResponse':sgProxyHttpResponse,'sgProxyHttpResponseTime':sgProxyHttpResponseTime,'sgProxyHttpServiceTimeAll':sgProxyHttpServiceTimeAll,'sgProxyHttpServiceTimeHit':sgProxyHttpServiceTimeHit,'sgProxyHttpServiceTimePartialHit':sgProxyHttpServiceTimePartialHit,'sgProxyHttpServiceTimeMiss':sgProxyHttpServiceTimeMiss,'sgProxyHttpTotalFetchTimeAll':sgProxyHttpTotalFetchTimeAll,'sgProxyHttpTotalFetchTimeHit':sgProxyHttpTotalFetchTimeHit,'sgProxyHttpTotalFetchTimePartialHit':sgProxyHttpTotalFetchTimePartialHit,'sgProxyHttpTotalFetchTimeMiss':sgProxyHttpTotalFetchTimeMiss,'sgProxyHttpResponseFirstByte':sgProxyHttpResponseFirstByte,'sgProxyHttpFirstByteAll':sgProxyHttpFirstByteAll,'sgProxyHttpFirstByteHit':sgProxyHttpFirstByteHit,'sgProxyHttpFirstBytePartialHit':sgProxyHttpFirstBytePartialHit,'sgProxyHttpFirstByteMiss':sgProxyHttpFirstByteMiss,'sgProxyHttpResponseByteRate':sgProxyHttpResponseByteRate,'sgProxyHttpByteRateAll':sgProxyHttpByteRateAll,'sgProxyHttpByteRateHit':sgProxyHttpByteRateHit,'sgProxyHttpByteRatePartialHit':sgProxyHttpByteRatePartialHit,'sgProxyHttpByteRateMiss':sgProxyHttpByteRateMiss,'sgProxyHttpResponseSize':sgProxyHttpResponseSize,'sgProxyHttpResponseSizeAll':sgProxyHttpResponseSizeAll,'sgProxyHttpResponseSizeHit':sgProxyHttpResponseSizeHit,'sgProxyHttpResponseSizePartialHit':sgProxyHttpResponseSizePartialHit,'sgProxyHttpResponseSizeMiss':sgProxyHttpResponseSizeMiss,'sgProxyHttpMedian':sgProxyHttpMedian,'sgProxyHttpMedianServiceTable':sgProxyHttpMedianServiceTable,'sgProxyHttpMedianServiceEntry':sgProxyHttpMedianServiceEntry,_L:sgProxyHttpMedianServiceTime,'sgProxyHttpMedianServiceTimeAll':sgProxyHttpMedianServiceTimeAll,'sgProxyHttpMedianServiceTimeHit':sgProxyHttpMedianServiceTimeHit,'sgProxyHttpMedianServiceTimePartialHit':sgProxyHttpMedianServiceTimePartialHit,'sgProxyHttpMedianServiceTimeMiss':sgProxyHttpMedianServiceTimeMiss,'sgProxyDnsMedianServiceTime':sgProxyDnsMedianServiceTime})