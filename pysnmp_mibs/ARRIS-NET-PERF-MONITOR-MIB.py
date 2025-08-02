_R='arrisNpmResultDnsTestResultIndex'
_Q='0.0.0.0'
_P='read-create'
_O='arrisNpmSetupNetLatencyConfigIndex'
_N='read-only'
_M='not-accessible'
_L='arrisNpmSetupWebPageDlTestConfigIndex'
_K='enable'
_J='disable'
_I='InetAddressType'
_H='InetAddress'
_G='ARRIS-NET-PERF-MONITOR-MIB'
_F='Seconds'
_E='Integer32'
_D='OctetString'
_C='Unsigned32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
arrisProdIdCM,=mibBuilder.importSymbols('ARRIS-MIB','arrisProdIdCM')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_H,_I)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeInterval','TimeStamp','TruthValue')
arrisNetPerfMonitorMib=ModuleIdentity((1,3,6,1,4,1,4115,1,3,13))
if mibBuilder.loadTexts:arrisNetPerfMonitorMib.setRevisions(('1912-10-15 00:00',))
_ArrisNpmSetup_ObjectIdentity=ObjectIdentity
arrisNpmSetup=_ArrisNpmSetup_ObjectIdentity((1,3,6,1,4,1,4115,1,3,13,1))
class _ArrisNpmSetupBgTrafficRateEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_K,1)))
_ArrisNpmSetupBgTrafficRateEnable_Type.__name__=_E
_ArrisNpmSetupBgTrafficRateEnable_Object=MibScalar
arrisNpmSetupBgTrafficRateEnable=_ArrisNpmSetupBgTrafficRateEnable_Object((1,3,6,1,4,1,4115,1,3,13,1,1),_ArrisNpmSetupBgTrafficRateEnable_Type())
arrisNpmSetupBgTrafficRateEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisNpmSetupBgTrafficRateEnable.setStatus(_A)
class _ArrisNpmSetupBgTrafficMaxDownstreamRate_Type(Unsigned32):defaultValue=64;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_ArrisNpmSetupBgTrafficMaxDownstreamRate_Type.__name__=_C
_ArrisNpmSetupBgTrafficMaxDownstreamRate_Object=MibScalar
arrisNpmSetupBgTrafficMaxDownstreamRate=_ArrisNpmSetupBgTrafficMaxDownstreamRate_Object((1,3,6,1,4,1,4115,1,3,13,1,2),_ArrisNpmSetupBgTrafficMaxDownstreamRate_Type())
arrisNpmSetupBgTrafficMaxDownstreamRate.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisNpmSetupBgTrafficMaxDownstreamRate.setStatus(_A)
if mibBuilder.loadTexts:arrisNpmSetupBgTrafficMaxDownstreamRate.setUnits('Kbps')
class _ArrisNpmSetupBgTrafficMaxUpstreamRate_Type(Unsigned32):defaultValue=32;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_ArrisNpmSetupBgTrafficMaxUpstreamRate_Type.__name__=_C
_ArrisNpmSetupBgTrafficMaxUpstreamRate_Object=MibScalar
arrisNpmSetupBgTrafficMaxUpstreamRate=_ArrisNpmSetupBgTrafficMaxUpstreamRate_Object((1,3,6,1,4,1,4115,1,3,13,1,3),_ArrisNpmSetupBgTrafficMaxUpstreamRate_Type())
arrisNpmSetupBgTrafficMaxUpstreamRate.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisNpmSetupBgTrafficMaxUpstreamRate.setStatus(_A)
if mibBuilder.loadTexts:arrisNpmSetupBgTrafficMaxUpstreamRate.setUnits('Kbps')
class _ArrisNpmSetupGroupReference_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_ArrisNpmSetupGroupReference_Type.__name__=_D
_ArrisNpmSetupGroupReference_Object=MibScalar
arrisNpmSetupGroupReference=_ArrisNpmSetupGroupReference_Object((1,3,6,1,4,1,4115,1,3,13,1,4),_ArrisNpmSetupGroupReference_Type())
arrisNpmSetupGroupReference.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisNpmSetupGroupReference.setStatus(_A)
_ArrisNpmWebDlTest_ObjectIdentity=ObjectIdentity
arrisNpmWebDlTest=_ArrisNpmWebDlTest_ObjectIdentity((1,3,6,1,4,1,4115,1,3,13,2))
class _ArrisNpmSetupWebPageDlTestRunTime_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_ArrisNpmSetupWebPageDlTestRunTime_Type.__name__=_C
_ArrisNpmSetupWebPageDlTestRunTime_Object=MibScalar
arrisNpmSetupWebPageDlTestRunTime=_ArrisNpmSetupWebPageDlTestRunTime_Object((1,3,6,1,4,1,4115,1,3,13,2,1),_ArrisNpmSetupWebPageDlTestRunTime_Type())
arrisNpmSetupWebPageDlTestRunTime.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisNpmSetupWebPageDlTestRunTime.setStatus(_A)
if mibBuilder.loadTexts:arrisNpmSetupWebPageDlTestRunTime.setUnits(_F)
class _ArrisNpmSetupWebPageDlTestTimeout_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_ArrisNpmSetupWebPageDlTestTimeout_Type.__name__=_C
_ArrisNpmSetupWebPageDlTestTimeout_Object=MibScalar
arrisNpmSetupWebPageDlTestTimeout=_ArrisNpmSetupWebPageDlTestTimeout_Object((1,3,6,1,4,1,4115,1,3,13,2,2),_ArrisNpmSetupWebPageDlTestTimeout_Type())
arrisNpmSetupWebPageDlTestTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisNpmSetupWebPageDlTestTimeout.setStatus(_A)
if mibBuilder.loadTexts:arrisNpmSetupWebPageDlTestTimeout.setUnits(_F)
_ArrisNpmSetupWebPageDlTestTable_Object=MibTable
arrisNpmSetupWebPageDlTestTable=_ArrisNpmSetupWebPageDlTestTable_Object((1,3,6,1,4,1,4115,1,3,13,2,3))
if mibBuilder.loadTexts:arrisNpmSetupWebPageDlTestTable.setStatus(_A)
_ArrisNpmSetupWebPageDlTestEntry_Object=MibTableRow
arrisNpmSetupWebPageDlTestEntry=_ArrisNpmSetupWebPageDlTestEntry_Object((1,3,6,1,4,1,4115,1,3,13,2,3,1))
arrisNpmSetupWebPageDlTestEntry.setIndexNames((0,_G,_L))
if mibBuilder.loadTexts:arrisNpmSetupWebPageDlTestEntry.setStatus(_A)
class _ArrisNpmSetupWebPageDlTestConfigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_ArrisNpmSetupWebPageDlTestConfigIndex_Type.__name__=_E
_ArrisNpmSetupWebPageDlTestConfigIndex_Object=MibTableColumn
arrisNpmSetupWebPageDlTestConfigIndex=_ArrisNpmSetupWebPageDlTestConfigIndex_Object((1,3,6,1,4,1,4115,1,3,13,2,3,1,1),_ArrisNpmSetupWebPageDlTestConfigIndex_Type())
arrisNpmSetupWebPageDlTestConfigIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:arrisNpmSetupWebPageDlTestConfigIndex.setStatus(_A)
class _ArrisNpmSetupWebPageDlTestConfigUrl_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ArrisNpmSetupWebPageDlTestConfigUrl_Type.__name__=_D
_ArrisNpmSetupWebPageDlTestConfigUrl_Object=MibTableColumn
arrisNpmSetupWebPageDlTestConfigUrl=_ArrisNpmSetupWebPageDlTestConfigUrl_Object((1,3,6,1,4,1,4115,1,3,13,2,3,1,2),_ArrisNpmSetupWebPageDlTestConfigUrl_Type())
arrisNpmSetupWebPageDlTestConfigUrl.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisNpmSetupWebPageDlTestConfigUrl.setStatus(_A)
_ArrisNpmSetupWebPageDlTestConfigRowStatus_Type=RowStatus
_ArrisNpmSetupWebPageDlTestConfigRowStatus_Object=MibTableColumn
arrisNpmSetupWebPageDlTestConfigRowStatus=_ArrisNpmSetupWebPageDlTestConfigRowStatus_Object((1,3,6,1,4,1,4115,1,3,13,2,3,1,3),_ArrisNpmSetupWebPageDlTestConfigRowStatus_Type())
arrisNpmSetupWebPageDlTestConfigRowStatus.setMaxAccess(_P)
if mibBuilder.loadTexts:arrisNpmSetupWebPageDlTestConfigRowStatus.setStatus(_A)
_ArrisNpmResultWebPageDlTestTable_Object=MibTable
arrisNpmResultWebPageDlTestTable=_ArrisNpmResultWebPageDlTestTable_Object((1,3,6,1,4,1,4115,1,3,13,2,4))
if mibBuilder.loadTexts:arrisNpmResultWebPageDlTestTable.setStatus(_A)
_ArrisNpmResultWebPageDlTestEntry_Object=MibTableRow
arrisNpmResultWebPageDlTestEntry=_ArrisNpmResultWebPageDlTestEntry_Object((1,3,6,1,4,1,4115,1,3,13,2,4,1))
arrisNpmResultWebPageDlTestEntry.setIndexNames((0,_G,_L))
if mibBuilder.loadTexts:arrisNpmResultWebPageDlTestEntry.setStatus(_A)
class _ArrisNpmResultWebPageDlTestResult_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,400))
_ArrisNpmResultWebPageDlTestResult_Type.__name__=_D
_ArrisNpmResultWebPageDlTestResult_Object=MibTableColumn
arrisNpmResultWebPageDlTestResult=_ArrisNpmResultWebPageDlTestResult_Object((1,3,6,1,4,1,4115,1,3,13,2,4,1,1),_ArrisNpmResultWebPageDlTestResult_Type())
arrisNpmResultWebPageDlTestResult.setMaxAccess(_N)
if mibBuilder.loadTexts:arrisNpmResultWebPageDlTestResult.setStatus(_A)
_ArrisNpmDnsTest_ObjectIdentity=ObjectIdentity
arrisNpmDnsTest=_ArrisNpmDnsTest_ObjectIdentity((1,3,6,1,4,1,4115,1,3,13,3))
class _ArrisNpmSetupDnsTestEnable_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_K,1)))
_ArrisNpmSetupDnsTestEnable_Type.__name__=_E
_ArrisNpmSetupDnsTestEnable_Object=MibScalar
arrisNpmSetupDnsTestEnable=_ArrisNpmSetupDnsTestEnable_Object((1,3,6,1,4,1,4115,1,3,13,3,1),_ArrisNpmSetupDnsTestEnable_Type())
arrisNpmSetupDnsTestEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisNpmSetupDnsTestEnable.setStatus(_A)
class _ArrisNpmSetupDnsTestRunTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_ArrisNpmSetupDnsTestRunTime_Type.__name__=_C
_ArrisNpmSetupDnsTestRunTime_Object=MibScalar
arrisNpmSetupDnsTestRunTime=_ArrisNpmSetupDnsTestRunTime_Object((1,3,6,1,4,1,4115,1,3,13,3,2),_ArrisNpmSetupDnsTestRunTime_Type())
arrisNpmSetupDnsTestRunTime.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisNpmSetupDnsTestRunTime.setStatus(_A)
if mibBuilder.loadTexts:arrisNpmSetupDnsTestRunTime.setUnits(_F)
class _ArrisNpmSetupDnsTestRunTimeTimeout_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_ArrisNpmSetupDnsTestRunTimeTimeout_Type.__name__=_C
_ArrisNpmSetupDnsTestRunTimeTimeout_Object=MibScalar
arrisNpmSetupDnsTestRunTimeTimeout=_ArrisNpmSetupDnsTestRunTimeTimeout_Object((1,3,6,1,4,1,4115,1,3,13,3,3),_ArrisNpmSetupDnsTestRunTimeTimeout_Type())
arrisNpmSetupDnsTestRunTimeTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisNpmSetupDnsTestRunTimeTimeout.setStatus(_A)
if mibBuilder.loadTexts:arrisNpmSetupDnsTestRunTimeTimeout.setUnits(_F)
class _ArrisNpmSetupDnsPrimaryServerIpType_Type(InetAddressType):defaultValue=1
_ArrisNpmSetupDnsPrimaryServerIpType_Type.__name__=_I
_ArrisNpmSetupDnsPrimaryServerIpType_Object=MibScalar
arrisNpmSetupDnsPrimaryServerIpType=_ArrisNpmSetupDnsPrimaryServerIpType_Object((1,3,6,1,4,1,4115,1,3,13,3,4),_ArrisNpmSetupDnsPrimaryServerIpType_Type())
arrisNpmSetupDnsPrimaryServerIpType.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisNpmSetupDnsPrimaryServerIpType.setStatus(_A)
class _ArrisNpmSetupDnsPrimaryServerIpAddress_Type(InetAddress):defaultValue=OctetString(_Q)
_ArrisNpmSetupDnsPrimaryServerIpAddress_Type.__name__=_H
_ArrisNpmSetupDnsPrimaryServerIpAddress_Object=MibScalar
arrisNpmSetupDnsPrimaryServerIpAddress=_ArrisNpmSetupDnsPrimaryServerIpAddress_Object((1,3,6,1,4,1,4115,1,3,13,3,5),_ArrisNpmSetupDnsPrimaryServerIpAddress_Type())
arrisNpmSetupDnsPrimaryServerIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisNpmSetupDnsPrimaryServerIpAddress.setStatus(_A)
class _ArrisNpmSetupDnsSecondaryServerIpType_Type(InetAddressType):defaultValue=1
_ArrisNpmSetupDnsSecondaryServerIpType_Type.__name__=_I
_ArrisNpmSetupDnsSecondaryServerIpType_Object=MibScalar
arrisNpmSetupDnsSecondaryServerIpType=_ArrisNpmSetupDnsSecondaryServerIpType_Object((1,3,6,1,4,1,4115,1,3,13,3,6),_ArrisNpmSetupDnsSecondaryServerIpType_Type())
arrisNpmSetupDnsSecondaryServerIpType.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisNpmSetupDnsSecondaryServerIpType.setStatus(_A)
class _ArrisNpmSetupDnsSecondaryServerIpAddress_Type(InetAddress):defaultValue=OctetString(_Q)
_ArrisNpmSetupDnsSecondaryServerIpAddress_Type.__name__=_H
_ArrisNpmSetupDnsSecondaryServerIpAddress_Object=MibScalar
arrisNpmSetupDnsSecondaryServerIpAddress=_ArrisNpmSetupDnsSecondaryServerIpAddress_Object((1,3,6,1,4,1,4115,1,3,13,3,7),_ArrisNpmSetupDnsSecondaryServerIpAddress_Type())
arrisNpmSetupDnsSecondaryServerIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisNpmSetupDnsSecondaryServerIpAddress.setStatus(_A)
_ArrisNpmResultDnsTestTable_Object=MibTable
arrisNpmResultDnsTestTable=_ArrisNpmResultDnsTestTable_Object((1,3,6,1,4,1,4115,1,3,13,3,8))
if mibBuilder.loadTexts:arrisNpmResultDnsTestTable.setStatus(_A)
_ArrisNpmResultDnsTestEntry_Object=MibTableRow
arrisNpmResultDnsTestEntry=_ArrisNpmResultDnsTestEntry_Object((1,3,6,1,4,1,4115,1,3,13,3,8,1))
arrisNpmResultDnsTestEntry.setIndexNames((0,_G,_R))
if mibBuilder.loadTexts:arrisNpmResultDnsTestEntry.setStatus(_A)
class _ArrisNpmResultDnsTestResultIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_ArrisNpmResultDnsTestResultIndex_Type.__name__=_E
_ArrisNpmResultDnsTestResultIndex_Object=MibTableColumn
arrisNpmResultDnsTestResultIndex=_ArrisNpmResultDnsTestResultIndex_Object((1,3,6,1,4,1,4115,1,3,13,3,8,1,1),_ArrisNpmResultDnsTestResultIndex_Type())
arrisNpmResultDnsTestResultIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:arrisNpmResultDnsTestResultIndex.setStatus(_A)
class _ArrisNpmResultDnsTestResult_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,400))
_ArrisNpmResultDnsTestResult_Type.__name__=_D
_ArrisNpmResultDnsTestResult_Object=MibTableColumn
arrisNpmResultDnsTestResult=_ArrisNpmResultDnsTestResult_Object((1,3,6,1,4,1,4115,1,3,13,3,8,1,2),_ArrisNpmResultDnsTestResult_Type())
arrisNpmResultDnsTestResult.setMaxAccess(_N)
if mibBuilder.loadTexts:arrisNpmResultDnsTestResult.setStatus(_A)
_ArrisNpmNetLatencyTest_ObjectIdentity=ObjectIdentity
arrisNpmNetLatencyTest=_ArrisNpmNetLatencyTest_ObjectIdentity((1,3,6,1,4,1,4115,1,3,13,4))
class _ArrisNpmSetupNetLatencyTestRunUnderLoadEnable_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_K,1)))
_ArrisNpmSetupNetLatencyTestRunUnderLoadEnable_Type.__name__=_E
_ArrisNpmSetupNetLatencyTestRunUnderLoadEnable_Object=MibScalar
arrisNpmSetupNetLatencyTestRunUnderLoadEnable=_ArrisNpmSetupNetLatencyTestRunUnderLoadEnable_Object((1,3,6,1,4,1,4115,1,3,13,4,1),_ArrisNpmSetupNetLatencyTestRunUnderLoadEnable_Type())
arrisNpmSetupNetLatencyTestRunUnderLoadEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisNpmSetupNetLatencyTestRunUnderLoadEnable.setStatus(_A)
class _ArrisNpmSetupNetLatencyTestRunTime_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_ArrisNpmSetupNetLatencyTestRunTime_Type.__name__=_C
_ArrisNpmSetupNetLatencyTestRunTime_Object=MibScalar
arrisNpmSetupNetLatencyTestRunTime=_ArrisNpmSetupNetLatencyTestRunTime_Object((1,3,6,1,4,1,4115,1,3,13,4,2),_ArrisNpmSetupNetLatencyTestRunTime_Type())
arrisNpmSetupNetLatencyTestRunTime.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisNpmSetupNetLatencyTestRunTime.setStatus(_A)
if mibBuilder.loadTexts:arrisNpmSetupNetLatencyTestRunTime.setUnits(_F)
class _ArrisNpmSetupNetLatencyTestPingCount_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_ArrisNpmSetupNetLatencyTestPingCount_Type.__name__=_C
_ArrisNpmSetupNetLatencyTestPingCount_Object=MibScalar
arrisNpmSetupNetLatencyTestPingCount=_ArrisNpmSetupNetLatencyTestPingCount_Object((1,3,6,1,4,1,4115,1,3,13,4,3),_ArrisNpmSetupNetLatencyTestPingCount_Type())
arrisNpmSetupNetLatencyTestPingCount.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisNpmSetupNetLatencyTestPingCount.setStatus(_A)
class _ArrisNpmSetupNetLatencyTestPingInterval_Type(Unsigned32):defaultValue=50;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,36000000))
_ArrisNpmSetupNetLatencyTestPingInterval_Type.__name__=_C
_ArrisNpmSetupNetLatencyTestPingInterval_Object=MibScalar
arrisNpmSetupNetLatencyTestPingInterval=_ArrisNpmSetupNetLatencyTestPingInterval_Object((1,3,6,1,4,1,4115,1,3,13,4,4),_ArrisNpmSetupNetLatencyTestPingInterval_Type())
arrisNpmSetupNetLatencyTestPingInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisNpmSetupNetLatencyTestPingInterval.setStatus(_A)
if mibBuilder.loadTexts:arrisNpmSetupNetLatencyTestPingInterval.setUnits('Milliseconds')
class _ArrisNpmSetupNetLatencyTestPingTimeout_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_ArrisNpmSetupNetLatencyTestPingTimeout_Type.__name__=_C
_ArrisNpmSetupNetLatencyTestPingTimeout_Object=MibScalar
arrisNpmSetupNetLatencyTestPingTimeout=_ArrisNpmSetupNetLatencyTestPingTimeout_Object((1,3,6,1,4,1,4115,1,3,13,4,5),_ArrisNpmSetupNetLatencyTestPingTimeout_Type())
arrisNpmSetupNetLatencyTestPingTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisNpmSetupNetLatencyTestPingTimeout.setStatus(_A)
if mibBuilder.loadTexts:arrisNpmSetupNetLatencyTestPingTimeout.setUnits(_F)
_ArrisNpmSetupNetLatencyServerTable_Object=MibTable
arrisNpmSetupNetLatencyServerTable=_ArrisNpmSetupNetLatencyServerTable_Object((1,3,6,1,4,1,4115,1,3,13,4,6))
if mibBuilder.loadTexts:arrisNpmSetupNetLatencyServerTable.setStatus(_A)
_ArrisNpmSetupNetLatencyServerEntry_Object=MibTableRow
arrisNpmSetupNetLatencyServerEntry=_ArrisNpmSetupNetLatencyServerEntry_Object((1,3,6,1,4,1,4115,1,3,13,4,6,1))
arrisNpmSetupNetLatencyServerEntry.setIndexNames((0,_G,_O))
if mibBuilder.loadTexts:arrisNpmSetupNetLatencyServerEntry.setStatus(_A)
class _ArrisNpmSetupNetLatencyConfigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_ArrisNpmSetupNetLatencyConfigIndex_Type.__name__=_E
_ArrisNpmSetupNetLatencyConfigIndex_Object=MibTableColumn
arrisNpmSetupNetLatencyConfigIndex=_ArrisNpmSetupNetLatencyConfigIndex_Object((1,3,6,1,4,1,4115,1,3,13,4,6,1,1),_ArrisNpmSetupNetLatencyConfigIndex_Type())
arrisNpmSetupNetLatencyConfigIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:arrisNpmSetupNetLatencyConfigIndex.setStatus(_A)
class _ArrisNpmSetupNetLatencyConfigServer_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_ArrisNpmSetupNetLatencyConfigServer_Type.__name__=_D
_ArrisNpmSetupNetLatencyConfigServer_Object=MibTableColumn
arrisNpmSetupNetLatencyConfigServer=_ArrisNpmSetupNetLatencyConfigServer_Object((1,3,6,1,4,1,4115,1,3,13,4,6,1,2),_ArrisNpmSetupNetLatencyConfigServer_Type())
arrisNpmSetupNetLatencyConfigServer.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisNpmSetupNetLatencyConfigServer.setStatus(_A)
class _ArrisNpmSetupNetLatencyConfigServerPort_Type(Unsigned32):defaultValue=50000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(49152,65535))
_ArrisNpmSetupNetLatencyConfigServerPort_Type.__name__=_C
_ArrisNpmSetupNetLatencyConfigServerPort_Object=MibTableColumn
arrisNpmSetupNetLatencyConfigServerPort=_ArrisNpmSetupNetLatencyConfigServerPort_Object((1,3,6,1,4,1,4115,1,3,13,4,6,1,3),_ArrisNpmSetupNetLatencyConfigServerPort_Type())
arrisNpmSetupNetLatencyConfigServerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisNpmSetupNetLatencyConfigServerPort.setStatus(_A)
_ArrisNpmSetupNetLatencyConfigServerRowStatus_Type=RowStatus
_ArrisNpmSetupNetLatencyConfigServerRowStatus_Object=MibTableColumn
arrisNpmSetupNetLatencyConfigServerRowStatus=_ArrisNpmSetupNetLatencyConfigServerRowStatus_Object((1,3,6,1,4,1,4115,1,3,13,4,6,1,4),_ArrisNpmSetupNetLatencyConfigServerRowStatus_Type())
arrisNpmSetupNetLatencyConfigServerRowStatus.setMaxAccess(_P)
if mibBuilder.loadTexts:arrisNpmSetupNetLatencyConfigServerRowStatus.setStatus(_A)
_ArrisNpmResultNetLatencyTestTable_Object=MibTable
arrisNpmResultNetLatencyTestTable=_ArrisNpmResultNetLatencyTestTable_Object((1,3,6,1,4,1,4115,1,3,13,4,7))
if mibBuilder.loadTexts:arrisNpmResultNetLatencyTestTable.setStatus(_A)
_ArrisNpmResultNetLatencyTestEntry_Object=MibTableRow
arrisNpmResultNetLatencyTestEntry=_ArrisNpmResultNetLatencyTestEntry_Object((1,3,6,1,4,1,4115,1,3,13,4,7,1))
arrisNpmResultNetLatencyTestEntry.setIndexNames((0,_G,_O))
if mibBuilder.loadTexts:arrisNpmResultNetLatencyTestEntry.setStatus(_A)
class _ArrisNpmResultNetLatencyTestResult_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,400))
_ArrisNpmResultNetLatencyTestResult_Type.__name__=_D
_ArrisNpmResultNetLatencyTestResult_Object=MibTableColumn
arrisNpmResultNetLatencyTestResult=_ArrisNpmResultNetLatencyTestResult_Object((1,3,6,1,4,1,4115,1,3,13,4,7,1,1),_ArrisNpmResultNetLatencyTestResult_Type())
arrisNpmResultNetLatencyTestResult.setMaxAccess(_N)
if mibBuilder.loadTexts:arrisNpmResultNetLatencyTestResult.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'arrisNetPerfMonitorMib':arrisNetPerfMonitorMib,'arrisNpmSetup':arrisNpmSetup,'arrisNpmSetupBgTrafficRateEnable':arrisNpmSetupBgTrafficRateEnable,'arrisNpmSetupBgTrafficMaxDownstreamRate':arrisNpmSetupBgTrafficMaxDownstreamRate,'arrisNpmSetupBgTrafficMaxUpstreamRate':arrisNpmSetupBgTrafficMaxUpstreamRate,'arrisNpmSetupGroupReference':arrisNpmSetupGroupReference,'arrisNpmWebDlTest':arrisNpmWebDlTest,'arrisNpmSetupWebPageDlTestRunTime':arrisNpmSetupWebPageDlTestRunTime,'arrisNpmSetupWebPageDlTestTimeout':arrisNpmSetupWebPageDlTestTimeout,'arrisNpmSetupWebPageDlTestTable':arrisNpmSetupWebPageDlTestTable,'arrisNpmSetupWebPageDlTestEntry':arrisNpmSetupWebPageDlTestEntry,_L:arrisNpmSetupWebPageDlTestConfigIndex,'arrisNpmSetupWebPageDlTestConfigUrl':arrisNpmSetupWebPageDlTestConfigUrl,'arrisNpmSetupWebPageDlTestConfigRowStatus':arrisNpmSetupWebPageDlTestConfigRowStatus,'arrisNpmResultWebPageDlTestTable':arrisNpmResultWebPageDlTestTable,'arrisNpmResultWebPageDlTestEntry':arrisNpmResultWebPageDlTestEntry,'arrisNpmResultWebPageDlTestResult':arrisNpmResultWebPageDlTestResult,'arrisNpmDnsTest':arrisNpmDnsTest,'arrisNpmSetupDnsTestEnable':arrisNpmSetupDnsTestEnable,'arrisNpmSetupDnsTestRunTime':arrisNpmSetupDnsTestRunTime,'arrisNpmSetupDnsTestRunTimeTimeout':arrisNpmSetupDnsTestRunTimeTimeout,'arrisNpmSetupDnsPrimaryServerIpType':arrisNpmSetupDnsPrimaryServerIpType,'arrisNpmSetupDnsPrimaryServerIpAddress':arrisNpmSetupDnsPrimaryServerIpAddress,'arrisNpmSetupDnsSecondaryServerIpType':arrisNpmSetupDnsSecondaryServerIpType,'arrisNpmSetupDnsSecondaryServerIpAddress':arrisNpmSetupDnsSecondaryServerIpAddress,'arrisNpmResultDnsTestTable':arrisNpmResultDnsTestTable,'arrisNpmResultDnsTestEntry':arrisNpmResultDnsTestEntry,_R:arrisNpmResultDnsTestResultIndex,'arrisNpmResultDnsTestResult':arrisNpmResultDnsTestResult,'arrisNpmNetLatencyTest':arrisNpmNetLatencyTest,'arrisNpmSetupNetLatencyTestRunUnderLoadEnable':arrisNpmSetupNetLatencyTestRunUnderLoadEnable,'arrisNpmSetupNetLatencyTestRunTime':arrisNpmSetupNetLatencyTestRunTime,'arrisNpmSetupNetLatencyTestPingCount':arrisNpmSetupNetLatencyTestPingCount,'arrisNpmSetupNetLatencyTestPingInterval':arrisNpmSetupNetLatencyTestPingInterval,'arrisNpmSetupNetLatencyTestPingTimeout':arrisNpmSetupNetLatencyTestPingTimeout,'arrisNpmSetupNetLatencyServerTable':arrisNpmSetupNetLatencyServerTable,'arrisNpmSetupNetLatencyServerEntry':arrisNpmSetupNetLatencyServerEntry,_O:arrisNpmSetupNetLatencyConfigIndex,'arrisNpmSetupNetLatencyConfigServer':arrisNpmSetupNetLatencyConfigServer,'arrisNpmSetupNetLatencyConfigServerPort':arrisNpmSetupNetLatencyConfigServerPort,'arrisNpmSetupNetLatencyConfigServerRowStatus':arrisNpmSetupNetLatencyConfigServerRowStatus,'arrisNpmResultNetLatencyTestTable':arrisNpmResultNetLatencyTestTable,'arrisNpmResultNetLatencyTestEntry':arrisNpmResultNetLatencyTestEntry,'arrisNpmResultNetLatencyTestResult':arrisNpmResultNetLatencyTestResult})