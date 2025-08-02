_AB='cienaCesBenchmarkGenTestSessionThroughputResultsIterations'
_AA='cienaCesBenchmarkGenTestSessionPdvResultsAvg'
_A9='cienaCesBenchmarkGenTestSessionLatencyResultsMax'
_A8='cienaCesBenchmarkGenTestSessionFramelossResultsResult'
_A7='cienaCesBenchmarkGenTestSessionThroughputResultsMax'
_A6='cienaCesBenchmarkTestInstanceEntryDstMac'
_A5='cienaCesBenchmarkTestInstanceEntryCvid'
_A4='cienaCesBenchmarkTestInstanceEntrySvid'
_A3='cienaCesBenchmarkEntityEntryPortId'
_A2='cienaCesBenchmarkEmixCharacterSetEntryIndex'
_A1='cienaCesBenchmarkGenTestSessionPdvResultsFrameSizeIndex'
_A0='cienaCesBenchmarkGenTestSessionPdvResultsColorIndex'
_z='cienaCesBenchmarkGenTestSessionPdvResultsPcpIndex'
_y='cienaCesBenchmarkGenTestSessionLatencyResultsFrameSizeIndex'
_x='cienaCesBenchmarkGenTestSessionLatencyResultsColorIndex'
_w='cienaCesBenchmarkGenTestSessionLatencyResultsPcpIndex'
_v='cienaCesBenchmarkGenTestSessionFramelossResultsRateIndex'
_u='cienaCesBenchmarkGenTestSessionFramelossResultsFrameSizeIndex'
_t='cienaCesBenchmarkGenTestSessionFramelossResultsColorIndex'
_s='cienaCesBenchmarkGenTestSessionFramelossResultsPcpIndex'
_r='cienaCesBenchmarkGenTestSessionThroughputResultsFrameSizeIndex'
_q='cienaCesBenchmarkGenTestSessionThroughputResultsColorIndex'
_p='cienaCesBenchmarkGenTestSessionThroughputResultsPcpIndex'
_o='cienaCesBenchmarkGenTestSessionColorIndex'
_n='cienaCesBenchmarkGenTestSessionPcpIndex'
_m='t15min'
_l='cienaCesBenchmarkProfileEntryId'
_k='cienaCesBenchmarkBwRatioPcpIndex'
_j='microseconds'
_i='cienaCesBenchmarkKpiColorIndex'
_h='cienaCesBenchmarkKpiPcpIndex'
_g='cienaCesBenchmarkEmixFrameSizeIndex'
_f='CienaCesBenchmarkAdminState'
_e='processingResults'
_d='waitingForResidualPackets'
_c='OctetString'
_b='cienaCesBenchmarkBwAllocProfileId'
_a='none'
_Z='running'
_Y='cienaCesBenchmarkGenTestSessionCurrentPktSize'
_X='cienaCesBenchmarkKpiColor'
_W='cienaCesBenchmarkKpiPcp'
_V='done'
_U='stoppedByUser'
_T='stoppedByDurationTimer'
_S='stoppedByIntervalTimer'
_R='idle'
_Q='cienaCesBenchmarkKpiProfileId'
_P='cienaCesBenchmarkEmixSequenceId'
_O='cienaCesBenchmarkTestInstanceEntryName'
_N='cienaGlobalSeverity'
_M='cienaGlobalMacAddress'
_L='read-write'
_K='TruthValue'
_J='cienaCesBenchmarkEntityEntryId'
_I='DisplayString'
_H='cienaCesBenchmarkTestInstanceEntryId'
_G='CIENA-GLOBAL-MIB'
_F='not-accessible'
_E='Integer32'
_D='read-create'
_C='CIENA-CES-BENCHMARK-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_c,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cienaGlobalMacAddress,cienaGlobalSeverity=mibBuilder.importSymbols(_G,_M,_N)
cienaCesConfig,cienaCesNotifications,cienaCesStatistics=mibBuilder.importSymbols('CIENA-SMI','cienaCesConfig','cienaCesNotifications','cienaCesStatistics')
InetAddress,InetAddressPrefixLength,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressPrefixLength','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_I,'MacAddress','PhysAddress','RowStatus','TextualConvention',_K)
cienaCesBenchmarkMIB=ModuleIdentity((1,3,6,1,4,1,1271,2,1,39))
if mibBuilder.loadTexts:cienaCesBenchmarkMIB.setRevisions(('2017-06-07 00:00','2017-02-28 00:00','2017-02-16 00:00','2016-11-11 00:00','2016-10-14 00:00','2016-10-07 00:00','2016-10-04 00:00','2016-09-07 00:00','2016-06-01 00:00','2016-05-13 00:00','2016-04-26 00:00','2016-03-30 00:00','2016-03-14 00:00','2016-03-10 00:00','2016-03-03 00:00','2016-02-24 00:00','2016-02-09 00:00'))
class CienaCesBenchmarkLatencyPdvTestState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_R,1),('sendingTraffic',2),('waitingForTimestampData',3),(_d,4),(_e,5),(_S,6),(_T,7),(_U,8),(_V,9)))
class CienaCesBenchmarkThroughputTestState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_R,1),(_Z,2),(_d,3),(_e,4),(_S,5),(_T,6),(_U,7),(_V,8),('txMaxThroughputForYellowTest',9)))
class CienaCesBenchmarkFramelossTestState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*((_R,1),('runningFirstTest',2),('waitingForResidualFirstPackets',3),('processingFirstResults',4),('runningSecondTest',5),('waitingForResidualSecondPackets',6),('processingSecondResults',7),(_S,8),(_T,9),(_U,10),(_V,11)))
class CienaCesBenchmarkRfc2544TestState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_R,1),(_Z,2),(_S,3),(_T,4),(_U,5),(_V,6)))
class CienaCesBenchmarkY1564TestState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_R,1),(_Z,2),(_S,3),(_T,4),(_U,5),(_V,6)))
class CienaCesBenchmarkColorTest(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('green',1),('yellow',2),('greenYellow',3),('greenYellowRed',4)))
class CienaCesBenchmarkKpiResult(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notAvailable',1),('pass',2),('fail',3)))
class CienaCesBenchmarkAdminState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disabled',1),('enabled',2)))
class CienaCesBenchmarkThroughputKpiPercent(TextualConvention,Unsigned32):status=_A;displayHint='d-4'
class CienaCesBenchmarkFramelossKpiPercent(TextualConvention,Unsigned32):status=_A;displayHint='d-4'
class CienaCesBenchmarkThroughputResult(TextualConvention,Unsigned32):status=_A;displayHint='d-2'
class CienaCesBenchmarkFramelossResult(TextualConvention,Unsigned32):status=_A;displayHint='d-2'
class CienaCesBenchmarkPcpBitmap(TextualConvention,Bits):status=_A;displayHint='x';namedValues=NamedValues(*(('pcp0',0),('pcp1',1),('pcp2',2),('pcp3',3),('pcp4',4),('pcp5',5),('pcp6',6),('pcp7',7)))
_CienaCesBenchmarkMIBObjects_ObjectIdentity=ObjectIdentity
cienaCesBenchmarkMIBObjects=_CienaCesBenchmarkMIBObjects_ObjectIdentity((1,3,6,1,4,1,1271,2,1,39,1))
_CienaCesBenchmarkModule_ObjectIdentity=ObjectIdentity
cienaCesBenchmarkModule=_CienaCesBenchmarkModule_ObjectIdentity((1,3,6,1,4,1,1271,2,1,39,1,1))
_CienaCesBenchmarkGlobalObjects_ObjectIdentity=ObjectIdentity
cienaCesBenchmarkGlobalObjects=_CienaCesBenchmarkGlobalObjects_ObjectIdentity((1,3,6,1,4,1,1271,2,1,39,1,1,1))
_CienaCesBenchmarkGlobalAdminState_Type=CienaCesBenchmarkAdminState
_CienaCesBenchmarkGlobalAdminState_Object=MibScalar
cienaCesBenchmarkGlobalAdminState=_CienaCesBenchmarkGlobalAdminState_Object((1,3,6,1,4,1,1271,2,1,39,1,1,1,1),_CienaCesBenchmarkGlobalAdminState_Type())
cienaCesBenchmarkGlobalAdminState.setMaxAccess(_L)
if mibBuilder.loadTexts:cienaCesBenchmarkGlobalAdminState.setStatus(_A)
class _CienaCesBenchmarkGlobalGeneratorDefaultEmixSequenceId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_CienaCesBenchmarkGlobalGeneratorDefaultEmixSequenceId_Type.__name__=_E
_CienaCesBenchmarkGlobalGeneratorDefaultEmixSequenceId_Object=MibScalar
cienaCesBenchmarkGlobalGeneratorDefaultEmixSequenceId=_CienaCesBenchmarkGlobalGeneratorDefaultEmixSequenceId_Object((1,3,6,1,4,1,1271,2,1,39,1,1,1,2),_CienaCesBenchmarkGlobalGeneratorDefaultEmixSequenceId_Type())
cienaCesBenchmarkGlobalGeneratorDefaultEmixSequenceId.setMaxAccess(_L)
if mibBuilder.loadTexts:cienaCesBenchmarkGlobalGeneratorDefaultEmixSequenceId.setStatus(_A)
class _CienaCesBenchmarkGlobalGeneratorDefaultKpiProfileId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_CienaCesBenchmarkGlobalGeneratorDefaultKpiProfileId_Type.__name__=_E
_CienaCesBenchmarkGlobalGeneratorDefaultKpiProfileId_Object=MibScalar
cienaCesBenchmarkGlobalGeneratorDefaultKpiProfileId=_CienaCesBenchmarkGlobalGeneratorDefaultKpiProfileId_Object((1,3,6,1,4,1,1271,2,1,39,1,1,1,3),_CienaCesBenchmarkGlobalGeneratorDefaultKpiProfileId_Type())
cienaCesBenchmarkGlobalGeneratorDefaultKpiProfileId.setMaxAccess(_L)
if mibBuilder.loadTexts:cienaCesBenchmarkGlobalGeneratorDefaultKpiProfileId.setStatus(_A)
class _CienaCesBenchmarkGlobalGeneratorDefaultBwAllocProfileId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_CienaCesBenchmarkGlobalGeneratorDefaultBwAllocProfileId_Type.__name__=_E
_CienaCesBenchmarkGlobalGeneratorDefaultBwAllocProfileId_Object=MibScalar
cienaCesBenchmarkGlobalGeneratorDefaultBwAllocProfileId=_CienaCesBenchmarkGlobalGeneratorDefaultBwAllocProfileId_Object((1,3,6,1,4,1,1271,2,1,39,1,1,1,4),_CienaCesBenchmarkGlobalGeneratorDefaultBwAllocProfileId_Type())
cienaCesBenchmarkGlobalGeneratorDefaultBwAllocProfileId.setMaxAccess(_L)
if mibBuilder.loadTexts:cienaCesBenchmarkGlobalGeneratorDefaultBwAllocProfileId.setStatus(_A)
_CienaCesBenchmarkGlobalPlatformMaxConfigEntities_Type=Integer32
_CienaCesBenchmarkGlobalPlatformMaxConfigEntities_Object=MibScalar
cienaCesBenchmarkGlobalPlatformMaxConfigEntities=_CienaCesBenchmarkGlobalPlatformMaxConfigEntities_Object((1,3,6,1,4,1,1271,2,1,39,1,1,1,5),_CienaCesBenchmarkGlobalPlatformMaxConfigEntities_Type())
cienaCesBenchmarkGlobalPlatformMaxConfigEntities.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkGlobalPlatformMaxConfigEntities.setStatus(_A)
_CienaCesBenchmarkGlobalPlatformMaxConfigTestInstances_Type=Integer32
_CienaCesBenchmarkGlobalPlatformMaxConfigTestInstances_Object=MibScalar
cienaCesBenchmarkGlobalPlatformMaxConfigTestInstances=_CienaCesBenchmarkGlobalPlatformMaxConfigTestInstances_Object((1,3,6,1,4,1,1271,2,1,39,1,1,1,6),_CienaCesBenchmarkGlobalPlatformMaxConfigTestInstances_Type())
cienaCesBenchmarkGlobalPlatformMaxConfigTestInstances.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkGlobalPlatformMaxConfigTestInstances.setStatus(_A)
_CienaCesBenchmarkGlobalPlatformMaxConfigTestProfiles_Type=Integer32
_CienaCesBenchmarkGlobalPlatformMaxConfigTestProfiles_Object=MibScalar
cienaCesBenchmarkGlobalPlatformMaxConfigTestProfiles=_CienaCesBenchmarkGlobalPlatformMaxConfigTestProfiles_Object((1,3,6,1,4,1,1271,2,1,39,1,1,1,7),_CienaCesBenchmarkGlobalPlatformMaxConfigTestProfiles_Type())
cienaCesBenchmarkGlobalPlatformMaxConfigTestProfiles.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkGlobalPlatformMaxConfigTestProfiles.setStatus(_A)
_CienaCesBenchmarkGlobalPlatformMaxConfigKpiProfiles_Type=Integer32
_CienaCesBenchmarkGlobalPlatformMaxConfigKpiProfiles_Object=MibScalar
cienaCesBenchmarkGlobalPlatformMaxConfigKpiProfiles=_CienaCesBenchmarkGlobalPlatformMaxConfigKpiProfiles_Object((1,3,6,1,4,1,1271,2,1,39,1,1,1,8),_CienaCesBenchmarkGlobalPlatformMaxConfigKpiProfiles_Type())
cienaCesBenchmarkGlobalPlatformMaxConfigKpiProfiles.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkGlobalPlatformMaxConfigKpiProfiles.setStatus(_A)
_CienaCesBenchmarkGlobalPlatformMaxConfigBwAllocProfiles_Type=Integer32
_CienaCesBenchmarkGlobalPlatformMaxConfigBwAllocProfiles_Object=MibScalar
cienaCesBenchmarkGlobalPlatformMaxConfigBwAllocProfiles=_CienaCesBenchmarkGlobalPlatformMaxConfigBwAllocProfiles_Object((1,3,6,1,4,1,1271,2,1,39,1,1,1,9),_CienaCesBenchmarkGlobalPlatformMaxConfigBwAllocProfiles_Type())
cienaCesBenchmarkGlobalPlatformMaxConfigBwAllocProfiles.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkGlobalPlatformMaxConfigBwAllocProfiles.setStatus(_A)
_CienaCesBenchmarkGlobalPlatformMaxConfigEmixSequences_Type=Integer32
_CienaCesBenchmarkGlobalPlatformMaxConfigEmixSequences_Object=MibScalar
cienaCesBenchmarkGlobalPlatformMaxConfigEmixSequences=_CienaCesBenchmarkGlobalPlatformMaxConfigEmixSequences_Object((1,3,6,1,4,1,1271,2,1,39,1,1,1,10),_CienaCesBenchmarkGlobalPlatformMaxConfigEmixSequences_Type())
cienaCesBenchmarkGlobalPlatformMaxConfigEmixSequences.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkGlobalPlatformMaxConfigEmixSequences.setStatus(_A)
_CienaCesBenchmarkGlobalPlatformMaxSimultaneousRunningTests_Type=Integer32
_CienaCesBenchmarkGlobalPlatformMaxSimultaneousRunningTests_Object=MibScalar
cienaCesBenchmarkGlobalPlatformMaxSimultaneousRunningTests=_CienaCesBenchmarkGlobalPlatformMaxSimultaneousRunningTests_Object((1,3,6,1,4,1,1271,2,1,39,1,1,1,11),_CienaCesBenchmarkGlobalPlatformMaxSimultaneousRunningTests_Type())
cienaCesBenchmarkGlobalPlatformMaxSimultaneousRunningTests.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkGlobalPlatformMaxSimultaneousRunningTests.setStatus(_A)
_CienaCesBenchmarkGlobalConfiguredEntities_Type=Integer32
_CienaCesBenchmarkGlobalConfiguredEntities_Object=MibScalar
cienaCesBenchmarkGlobalConfiguredEntities=_CienaCesBenchmarkGlobalConfiguredEntities_Object((1,3,6,1,4,1,1271,2,1,39,1,1,1,12),_CienaCesBenchmarkGlobalConfiguredEntities_Type())
cienaCesBenchmarkGlobalConfiguredEntities.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkGlobalConfiguredEntities.setStatus(_A)
_CienaCesBenchmarkGlobalConfiguredTestInstances_Type=Integer32
_CienaCesBenchmarkGlobalConfiguredTestInstances_Object=MibScalar
cienaCesBenchmarkGlobalConfiguredTestInstances=_CienaCesBenchmarkGlobalConfiguredTestInstances_Object((1,3,6,1,4,1,1271,2,1,39,1,1,1,13),_CienaCesBenchmarkGlobalConfiguredTestInstances_Type())
cienaCesBenchmarkGlobalConfiguredTestInstances.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkGlobalConfiguredTestInstances.setStatus(_A)
_CienaCesBenchmarkGlobalConfiguredProfiles_Type=Integer32
_CienaCesBenchmarkGlobalConfiguredProfiles_Object=MibScalar
cienaCesBenchmarkGlobalConfiguredProfiles=_CienaCesBenchmarkGlobalConfiguredProfiles_Object((1,3,6,1,4,1,1271,2,1,39,1,1,1,14),_CienaCesBenchmarkGlobalConfiguredProfiles_Type())
cienaCesBenchmarkGlobalConfiguredProfiles.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkGlobalConfiguredProfiles.setStatus(_A)
_CienaCesBenchmarkGlobalConfiguredEmixSequences_Type=Integer32
_CienaCesBenchmarkGlobalConfiguredEmixSequences_Object=MibScalar
cienaCesBenchmarkGlobalConfiguredEmixSequences=_CienaCesBenchmarkGlobalConfiguredEmixSequences_Object((1,3,6,1,4,1,1271,2,1,39,1,1,1,15),_CienaCesBenchmarkGlobalConfiguredEmixSequences_Type())
cienaCesBenchmarkGlobalConfiguredEmixSequences.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkGlobalConfiguredEmixSequences.setStatus(_A)
_CienaCesBenchmarkGlobalConfiguredKpiProfiles_Type=Integer32
_CienaCesBenchmarkGlobalConfiguredKpiProfiles_Object=MibScalar
cienaCesBenchmarkGlobalConfiguredKpiProfiles=_CienaCesBenchmarkGlobalConfiguredKpiProfiles_Object((1,3,6,1,4,1,1271,2,1,39,1,1,1,16),_CienaCesBenchmarkGlobalConfiguredKpiProfiles_Type())
cienaCesBenchmarkGlobalConfiguredKpiProfiles.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkGlobalConfiguredKpiProfiles.setStatus(_A)
_CienaCesBenchmarkGlobalConfiguredBwAllocProfiles_Type=Integer32
_CienaCesBenchmarkGlobalConfiguredBwAllocProfiles_Object=MibScalar
cienaCesBenchmarkGlobalConfiguredBwAllocProfiles=_CienaCesBenchmarkGlobalConfiguredBwAllocProfiles_Object((1,3,6,1,4,1,1271,2,1,39,1,1,1,17),_CienaCesBenchmarkGlobalConfiguredBwAllocProfiles_Type())
cienaCesBenchmarkGlobalConfiguredBwAllocProfiles.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkGlobalConfiguredBwAllocProfiles.setStatus(_A)
_CienaCesBenchmarkGlobalEnabledTestInstances_Type=Integer32
_CienaCesBenchmarkGlobalEnabledTestInstances_Object=MibScalar
cienaCesBenchmarkGlobalEnabledTestInstances=_CienaCesBenchmarkGlobalEnabledTestInstances_Object((1,3,6,1,4,1,1271,2,1,39,1,1,1,18),_CienaCesBenchmarkGlobalEnabledTestInstances_Type())
cienaCesBenchmarkGlobalEnabledTestInstances.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkGlobalEnabledTestInstances.setStatus(_A)
_CienaCesBenchmarkGlobalGeneratorRunningTestInstances_Type=Integer32
_CienaCesBenchmarkGlobalGeneratorRunningTestInstances_Object=MibScalar
cienaCesBenchmarkGlobalGeneratorRunningTestInstances=_CienaCesBenchmarkGlobalGeneratorRunningTestInstances_Object((1,3,6,1,4,1,1271,2,1,39,1,1,1,19),_CienaCesBenchmarkGlobalGeneratorRunningTestInstances_Type())
cienaCesBenchmarkGlobalGeneratorRunningTestInstances.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkGlobalGeneratorRunningTestInstances.setStatus(_A)
_CienaCesBenchmarkEntityTable_Object=MibTable
cienaCesBenchmarkEntityTable=_CienaCesBenchmarkEntityTable_Object((1,3,6,1,4,1,1271,2,1,39,1,1,2))
if mibBuilder.loadTexts:cienaCesBenchmarkEntityTable.setStatus(_A)
_CienaCesBenchmarkEntityEntry_Object=MibTableRow
cienaCesBenchmarkEntityEntry=_CienaCesBenchmarkEntityEntry_Object((1,3,6,1,4,1,1271,2,1,39,1,1,2,1))
cienaCesBenchmarkEntityEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:cienaCesBenchmarkEntityEntry.setStatus(_A)
_CienaCesBenchmarkEntityEntryId_Type=Integer32
_CienaCesBenchmarkEntityEntryId_Object=MibTableColumn
cienaCesBenchmarkEntityEntryId=_CienaCesBenchmarkEntityEntryId_Object((1,3,6,1,4,1,1271,2,1,39,1,1,2,1,1),_CienaCesBenchmarkEntityEntryId_Type())
cienaCesBenchmarkEntityEntryId.setMaxAccess(_F)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityEntryId.setStatus(_A)
class _CienaCesBenchmarkEntityEntryName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,46))
_CienaCesBenchmarkEntityEntryName_Type.__name__=_I
_CienaCesBenchmarkEntityEntryName_Object=MibTableColumn
cienaCesBenchmarkEntityEntryName=_CienaCesBenchmarkEntityEntryName_Object((1,3,6,1,4,1,1271,2,1,39,1,1,2,1,2),_CienaCesBenchmarkEntityEntryName_Type())
cienaCesBenchmarkEntityEntryName.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityEntryName.setStatus(_A)
class _CienaCesBenchmarkEntityEntryRole_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_a,1),('reflector',2),('generator',3)))
_CienaCesBenchmarkEntityEntryRole_Type.__name__=_E
_CienaCesBenchmarkEntityEntryRole_Object=MibTableColumn
cienaCesBenchmarkEntityEntryRole=_CienaCesBenchmarkEntityEntryRole_Object((1,3,6,1,4,1,1271,2,1,39,1,1,2,1,3),_CienaCesBenchmarkEntityEntryRole_Type())
cienaCesBenchmarkEntityEntryRole.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityEntryRole.setStatus(_A)
class _CienaCesBenchmarkEntityEntryPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CienaCesBenchmarkEntityEntryPortId_Type.__name__=_E
_CienaCesBenchmarkEntityEntryPortId_Object=MibTableColumn
cienaCesBenchmarkEntityEntryPortId=_CienaCesBenchmarkEntityEntryPortId_Object((1,3,6,1,4,1,1271,2,1,39,1,1,2,1,4),_CienaCesBenchmarkEntityEntryPortId_Type())
cienaCesBenchmarkEntityEntryPortId.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityEntryPortId.setStatus(_A)
class _CienaCesBenchmarkEntityEntryMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_a,1),('inService',2),('outOfService',3),('vidOutOfService',4),('evcOutOfService',5)))
_CienaCesBenchmarkEntityEntryMode_Type.__name__=_E
_CienaCesBenchmarkEntityEntryMode_Object=MibTableColumn
cienaCesBenchmarkEntityEntryMode=_CienaCesBenchmarkEntityEntryMode_Object((1,3,6,1,4,1,1271,2,1,39,1,1,2,1,5),_CienaCesBenchmarkEntityEntryMode_Type())
cienaCesBenchmarkEntityEntryMode.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityEntryMode.setStatus(_A)
class _CienaCesBenchmarkEntityEntryAdminState_Type(CienaCesBenchmarkAdminState):defaultValue=1
_CienaCesBenchmarkEntityEntryAdminState_Type.__name__=_f
_CienaCesBenchmarkEntityEntryAdminState_Object=MibTableColumn
cienaCesBenchmarkEntityEntryAdminState=_CienaCesBenchmarkEntityEntryAdminState_Object((1,3,6,1,4,1,1271,2,1,39,1,1,2,1,6),_CienaCesBenchmarkEntityEntryAdminState_Type())
cienaCesBenchmarkEntityEntryAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityEntryAdminState.setStatus(_A)
_CienaCesBenchmarkEntityEntryLocalMac_Type=MacAddress
_CienaCesBenchmarkEntityEntryLocalMac_Object=MibTableColumn
cienaCesBenchmarkEntityEntryLocalMac=_CienaCesBenchmarkEntityEntryLocalMac_Object((1,3,6,1,4,1,1271,2,1,39,1,1,2,1,7),_CienaCesBenchmarkEntityEntryLocalMac_Type())
cienaCesBenchmarkEntityEntryLocalMac.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityEntryLocalMac.setStatus(_A)
_CienaCesBenchmarkEntityEntrySlotId_Type=Integer32
_CienaCesBenchmarkEntityEntrySlotId_Object=MibTableColumn
cienaCesBenchmarkEntityEntrySlotId=_CienaCesBenchmarkEntityEntrySlotId_Object((1,3,6,1,4,1,1271,2,1,39,1,1,2,1,8),_CienaCesBenchmarkEntityEntrySlotId_Type())
cienaCesBenchmarkEntityEntrySlotId.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityEntrySlotId.setStatus(_A)
class _CienaCesBenchmarkEntityEntryReflectorVendorType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('other',1),('ciena',2)))
_CienaCesBenchmarkEntityEntryReflectorVendorType_Type.__name__=_E
_CienaCesBenchmarkEntityEntryReflectorVendorType_Object=MibTableColumn
cienaCesBenchmarkEntityEntryReflectorVendorType=_CienaCesBenchmarkEntityEntryReflectorVendorType_Object((1,3,6,1,4,1,1271,2,1,39,1,1,2,1,9),_CienaCesBenchmarkEntityEntryReflectorVendorType_Type())
cienaCesBenchmarkEntityEntryReflectorVendorType.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityEntryReflectorVendorType.setStatus(_A)
class _CienaCesBenchmarkEntityEntryReflectionLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_a,1),('l2only',2),('l2ToL3IPv4only',3),('l2ToL3IPv6only',4),('l2ToL4IPv4only',5),('l2ToL4IPv6only',6),('l2ToL4',7)))
_CienaCesBenchmarkEntityEntryReflectionLevel_Type.__name__=_E
_CienaCesBenchmarkEntityEntryReflectionLevel_Object=MibTableColumn
cienaCesBenchmarkEntityEntryReflectionLevel=_CienaCesBenchmarkEntityEntryReflectionLevel_Object((1,3,6,1,4,1,1271,2,1,39,1,1,2,1,10),_CienaCesBenchmarkEntityEntryReflectionLevel_Type())
cienaCesBenchmarkEntityEntryReflectionLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityEntryReflectionLevel.setStatus(_A)
class _CienaCesBenchmarkEntityEntryGeneratorHFrameSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,9216))
_CienaCesBenchmarkEntityEntryGeneratorHFrameSize_Type.__name__=_E
_CienaCesBenchmarkEntityEntryGeneratorHFrameSize_Object=MibTableColumn
cienaCesBenchmarkEntityEntryGeneratorHFrameSize=_CienaCesBenchmarkEntityEntryGeneratorHFrameSize_Object((1,3,6,1,4,1,1271,2,1,39,1,1,2,1,11),_CienaCesBenchmarkEntityEntryGeneratorHFrameSize_Type())
cienaCesBenchmarkEntityEntryGeneratorHFrameSize.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityEntryGeneratorHFrameSize.setStatus(_A)
_CienaCesBenchmarkEntityEntryMaxConfigTestInstances_Type=Integer32
_CienaCesBenchmarkEntityEntryMaxConfigTestInstances_Object=MibTableColumn
cienaCesBenchmarkEntityEntryMaxConfigTestInstances=_CienaCesBenchmarkEntityEntryMaxConfigTestInstances_Object((1,3,6,1,4,1,1271,2,1,39,1,1,2,1,12),_CienaCesBenchmarkEntityEntryMaxConfigTestInstances_Type())
cienaCesBenchmarkEntityEntryMaxConfigTestInstances.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityEntryMaxConfigTestInstances.setStatus(_A)
_CienaCesBenchmarkEntityEntryMaxSimultaneousTestInstances_Type=Integer32
_CienaCesBenchmarkEntityEntryMaxSimultaneousTestInstances_Object=MibTableColumn
cienaCesBenchmarkEntityEntryMaxSimultaneousTestInstances=_CienaCesBenchmarkEntityEntryMaxSimultaneousTestInstances_Object((1,3,6,1,4,1,1271,2,1,39,1,1,2,1,13),_CienaCesBenchmarkEntityEntryMaxSimultaneousTestInstances_Type())
cienaCesBenchmarkEntityEntryMaxSimultaneousTestInstances.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityEntryMaxSimultaneousTestInstances.setStatus(_A)
_CienaCesBenchmarkEntityEntryOperEnabled_Type=TruthValue
_CienaCesBenchmarkEntityEntryOperEnabled_Object=MibTableColumn
cienaCesBenchmarkEntityEntryOperEnabled=_CienaCesBenchmarkEntityEntryOperEnabled_Object((1,3,6,1,4,1,1271,2,1,39,1,1,2,1,14),_CienaCesBenchmarkEntityEntryOperEnabled_Type())
cienaCesBenchmarkEntityEntryOperEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityEntryOperEnabled.setStatus(_A)
_CienaCesBenchmarkEntityEntryNumTestInstancesConfigured_Type=Integer32
_CienaCesBenchmarkEntityEntryNumTestInstancesConfigured_Object=MibTableColumn
cienaCesBenchmarkEntityEntryNumTestInstancesConfigured=_CienaCesBenchmarkEntityEntryNumTestInstancesConfigured_Object((1,3,6,1,4,1,1271,2,1,39,1,1,2,1,15),_CienaCesBenchmarkEntityEntryNumTestInstancesConfigured_Type())
cienaCesBenchmarkEntityEntryNumTestInstancesConfigured.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityEntryNumTestInstancesConfigured.setStatus(_A)
_CienaCesBenchmarkEntityEntryNumTestInstancesEnabled_Type=Integer32
_CienaCesBenchmarkEntityEntryNumTestInstancesEnabled_Object=MibTableColumn
cienaCesBenchmarkEntityEntryNumTestInstancesEnabled=_CienaCesBenchmarkEntityEntryNumTestInstancesEnabled_Object((1,3,6,1,4,1,1271,2,1,39,1,1,2,1,16),_CienaCesBenchmarkEntityEntryNumTestInstancesEnabled_Type())
cienaCesBenchmarkEntityEntryNumTestInstancesEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityEntryNumTestInstancesEnabled.setStatus(_A)
_CienaCesBenchmarkEntityEntryGenNumTestInstancesRunning_Type=Integer32
_CienaCesBenchmarkEntityEntryGenNumTestInstancesRunning_Object=MibTableColumn
cienaCesBenchmarkEntityEntryGenNumTestInstancesRunning=_CienaCesBenchmarkEntityEntryGenNumTestInstancesRunning_Object((1,3,6,1,4,1,1271,2,1,39,1,1,2,1,17),_CienaCesBenchmarkEntityEntryGenNumTestInstancesRunning_Type())
cienaCesBenchmarkEntityEntryGenNumTestInstancesRunning.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityEntryGenNumTestInstancesRunning.setStatus(_A)
_CienaCesBenchmarkEntityEntryBwAvailable_Type=Integer32
_CienaCesBenchmarkEntityEntryBwAvailable_Object=MibTableColumn
cienaCesBenchmarkEntityEntryBwAvailable=_CienaCesBenchmarkEntityEntryBwAvailable_Object((1,3,6,1,4,1,1271,2,1,39,1,1,2,1,18),_CienaCesBenchmarkEntityEntryBwAvailable_Type())
cienaCesBenchmarkEntityEntryBwAvailable.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityEntryBwAvailable.setStatus(_A)
_CienaCesBenchmarkEntityEntryGenBwUsedByRunningTests_Type=Integer32
_CienaCesBenchmarkEntityEntryGenBwUsedByRunningTests_Object=MibTableColumn
cienaCesBenchmarkEntityEntryGenBwUsedByRunningTests=_CienaCesBenchmarkEntityEntryGenBwUsedByRunningTests_Object((1,3,6,1,4,1,1271,2,1,39,1,1,2,1,19),_CienaCesBenchmarkEntityEntryGenBwUsedByRunningTests_Type())
cienaCesBenchmarkEntityEntryGenBwUsedByRunningTests.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityEntryGenBwUsedByRunningTests.setStatus(_A)
_CienaCesBenchmarkEntityEntryAvailableHwSessions_Type=Integer32
_CienaCesBenchmarkEntityEntryAvailableHwSessions_Object=MibTableColumn
cienaCesBenchmarkEntityEntryAvailableHwSessions=_CienaCesBenchmarkEntityEntryAvailableHwSessions_Object((1,3,6,1,4,1,1271,2,1,39,1,1,2,1,20),_CienaCesBenchmarkEntityEntryAvailableHwSessions_Type())
cienaCesBenchmarkEntityEntryAvailableHwSessions.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityEntryAvailableHwSessions.setStatus(_A)
_CienaCesBenchmarkEntityEntryAllocatedHwSessions_Type=Integer32
_CienaCesBenchmarkEntityEntryAllocatedHwSessions_Object=MibTableColumn
cienaCesBenchmarkEntityEntryAllocatedHwSessions=_CienaCesBenchmarkEntityEntryAllocatedHwSessions_Object((1,3,6,1,4,1,1271,2,1,39,1,1,2,1,21),_CienaCesBenchmarkEntityEntryAllocatedHwSessions_Type())
cienaCesBenchmarkEntityEntryAllocatedHwSessions.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityEntryAllocatedHwSessions.setStatus(_A)
_CienaCesBenchmarkEntityEntryRowStatus_Type=RowStatus
_CienaCesBenchmarkEntityEntryRowStatus_Object=MibTableColumn
cienaCesBenchmarkEntityEntryRowStatus=_CienaCesBenchmarkEntityEntryRowStatus_Object((1,3,6,1,4,1,1271,2,1,39,1,1,2,1,22),_CienaCesBenchmarkEntityEntryRowStatus_Type())
cienaCesBenchmarkEntityEntryRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityEntryRowStatus.setStatus(_A)
_CienaCesBenchmarkEntityEntryClearStats_Type=TruthValue
_CienaCesBenchmarkEntityEntryClearStats_Object=MibTableColumn
cienaCesBenchmarkEntityEntryClearStats=_CienaCesBenchmarkEntityEntryClearStats_Object((1,3,6,1,4,1,1271,2,1,39,1,1,2,1,23),_CienaCesBenchmarkEntityEntryClearStats_Type())
cienaCesBenchmarkEntityEntryClearStats.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityEntryClearStats.setStatus(_A)
_CienaCesBenchmarkEntityEntryReflectorMacValidation_Type=TruthValue
_CienaCesBenchmarkEntityEntryReflectorMacValidation_Object=MibTableColumn
cienaCesBenchmarkEntityEntryReflectorMacValidation=_CienaCesBenchmarkEntityEntryReflectorMacValidation_Object((1,3,6,1,4,1,1271,2,1,39,1,1,2,1,24),_CienaCesBenchmarkEntityEntryReflectorMacValidation_Type())
cienaCesBenchmarkEntityEntryReflectorMacValidation.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityEntryReflectorMacValidation.setStatus(_A)
_CienaCesBenchmarkEntityStatsTable_Object=MibTable
cienaCesBenchmarkEntityStatsTable=_CienaCesBenchmarkEntityStatsTable_Object((1,3,6,1,4,1,1271,2,1,39,1,1,3))
if mibBuilder.loadTexts:cienaCesBenchmarkEntityStatsTable.setStatus(_A)
_CienaCesBenchmarkEntityStatsEntry_Object=MibTableRow
cienaCesBenchmarkEntityStatsEntry=_CienaCesBenchmarkEntityStatsEntry_Object((1,3,6,1,4,1,1271,2,1,39,1,1,3,1))
cienaCesBenchmarkEntityStatsEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:cienaCesBenchmarkEntityStatsEntry.setStatus(_A)
_CienaCesBenchmarkEntityStatsEntryClear_Type=TruthValue
_CienaCesBenchmarkEntityStatsEntryClear_Object=MibTableColumn
cienaCesBenchmarkEntityStatsEntryClear=_CienaCesBenchmarkEntityStatsEntryClear_Object((1,3,6,1,4,1,1271,2,1,39,1,1,3,1,1),_CienaCesBenchmarkEntityStatsEntryClear_Type())
cienaCesBenchmarkEntityStatsEntryClear.setMaxAccess(_L)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityStatsEntryClear.setStatus('obsolete')
_CienaCesBenchmarkEntityStatsEntryPortTxBytes_Type=Counter64
_CienaCesBenchmarkEntityStatsEntryPortTxBytes_Object=MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortTxBytes=_CienaCesBenchmarkEntityStatsEntryPortTxBytes_Object((1,3,6,1,4,1,1271,2,1,39,1,1,3,1,2),_CienaCesBenchmarkEntityStatsEntryPortTxBytes_Type())
cienaCesBenchmarkEntityStatsEntryPortTxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityStatsEntryPortTxBytes.setStatus(_A)
_CienaCesBenchmarkEntityStatsEntryPortTxPkts_Type=Counter64
_CienaCesBenchmarkEntityStatsEntryPortTxPkts_Object=MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortTxPkts=_CienaCesBenchmarkEntityStatsEntryPortTxPkts_Object((1,3,6,1,4,1,1271,2,1,39,1,1,3,1,3),_CienaCesBenchmarkEntityStatsEntryPortTxPkts_Type())
cienaCesBenchmarkEntityStatsEntryPortTxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityStatsEntryPortTxPkts.setStatus(_A)
_CienaCesBenchmarkEntityStatsEntryPortTxCrcErrorPkts_Type=Counter64
_CienaCesBenchmarkEntityStatsEntryPortTxCrcErrorPkts_Object=MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortTxCrcErrorPkts=_CienaCesBenchmarkEntityStatsEntryPortTxCrcErrorPkts_Object((1,3,6,1,4,1,1271,2,1,39,1,1,3,1,4),_CienaCesBenchmarkEntityStatsEntryPortTxCrcErrorPkts_Type())
cienaCesBenchmarkEntityStatsEntryPortTxCrcErrorPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityStatsEntryPortTxCrcErrorPkts.setStatus(_A)
_CienaCesBenchmarkEntityStatsEntryPortTxUcastPkts_Type=Counter64
_CienaCesBenchmarkEntityStatsEntryPortTxUcastPkts_Object=MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortTxUcastPkts=_CienaCesBenchmarkEntityStatsEntryPortTxUcastPkts_Object((1,3,6,1,4,1,1271,2,1,39,1,1,3,1,5),_CienaCesBenchmarkEntityStatsEntryPortTxUcastPkts_Type())
cienaCesBenchmarkEntityStatsEntryPortTxUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityStatsEntryPortTxUcastPkts.setStatus(_A)
_CienaCesBenchmarkEntityStatsEntryPortTxMcastPkts_Type=Counter64
_CienaCesBenchmarkEntityStatsEntryPortTxMcastPkts_Object=MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortTxMcastPkts=_CienaCesBenchmarkEntityStatsEntryPortTxMcastPkts_Object((1,3,6,1,4,1,1271,2,1,39,1,1,3,1,6),_CienaCesBenchmarkEntityStatsEntryPortTxMcastPkts_Type())
cienaCesBenchmarkEntityStatsEntryPortTxMcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityStatsEntryPortTxMcastPkts.setStatus(_A)
_CienaCesBenchmarkEntityStatsEntryPortTxBcastPkts_Type=Counter64
_CienaCesBenchmarkEntityStatsEntryPortTxBcastPkts_Object=MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortTxBcastPkts=_CienaCesBenchmarkEntityStatsEntryPortTxBcastPkts_Object((1,3,6,1,4,1,1271,2,1,39,1,1,3,1,7),_CienaCesBenchmarkEntityStatsEntryPortTxBcastPkts_Type())
cienaCesBenchmarkEntityStatsEntryPortTxBcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityStatsEntryPortTxBcastPkts.setStatus(_A)
_CienaCesBenchmarkEntityStatsEntryPortRxUndersizePkts_Type=Counter64
_CienaCesBenchmarkEntityStatsEntryPortRxUndersizePkts_Object=MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortRxUndersizePkts=_CienaCesBenchmarkEntityStatsEntryPortRxUndersizePkts_Object((1,3,6,1,4,1,1271,2,1,39,1,1,3,1,8),_CienaCesBenchmarkEntityStatsEntryPortRxUndersizePkts_Type())
cienaCesBenchmarkEntityStatsEntryPortRxUndersizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityStatsEntryPortRxUndersizePkts.setStatus(_A)
_CienaCesBenchmarkEntityStatsEntryPortRxOversizePkts_Type=Counter64
_CienaCesBenchmarkEntityStatsEntryPortRxOversizePkts_Object=MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortRxOversizePkts=_CienaCesBenchmarkEntityStatsEntryPortRxOversizePkts_Object((1,3,6,1,4,1,1271,2,1,39,1,1,3,1,9),_CienaCesBenchmarkEntityStatsEntryPortRxOversizePkts_Type())
cienaCesBenchmarkEntityStatsEntryPortRxOversizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityStatsEntryPortRxOversizePkts.setStatus(_A)
_CienaCesBenchmarkEntityStatsEntryPortRxFragmentsPkts_Type=Counter64
_CienaCesBenchmarkEntityStatsEntryPortRxFragmentsPkts_Object=MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortRxFragmentsPkts=_CienaCesBenchmarkEntityStatsEntryPortRxFragmentsPkts_Object((1,3,6,1,4,1,1271,2,1,39,1,1,3,1,10),_CienaCesBenchmarkEntityStatsEntryPortRxFragmentsPkts_Type())
cienaCesBenchmarkEntityStatsEntryPortRxFragmentsPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityStatsEntryPortRxFragmentsPkts.setStatus(_A)
_CienaCesBenchmarkEntityStatsEntryPortRxJabbersPkts_Type=Counter64
_CienaCesBenchmarkEntityStatsEntryPortRxJabbersPkts_Object=MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortRxJabbersPkts=_CienaCesBenchmarkEntityStatsEntryPortRxJabbersPkts_Object((1,3,6,1,4,1,1271,2,1,39,1,1,3,1,11),_CienaCesBenchmarkEntityStatsEntryPortRxJabbersPkts_Type())
cienaCesBenchmarkEntityStatsEntryPortRxJabbersPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityStatsEntryPortRxJabbersPkts.setStatus(_A)
_CienaCesBenchmarkEntityStatsEntryPortTxPausePkts_Type=Counter64
_CienaCesBenchmarkEntityStatsEntryPortTxPausePkts_Object=MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortTxPausePkts=_CienaCesBenchmarkEntityStatsEntryPortTxPausePkts_Object((1,3,6,1,4,1,1271,2,1,39,1,1,3,1,12),_CienaCesBenchmarkEntityStatsEntryPortTxPausePkts_Type())
cienaCesBenchmarkEntityStatsEntryPortTxPausePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityStatsEntryPortTxPausePkts.setStatus(_A)
_CienaCesBenchmarkEntityStatsEntryPortTxDropPkts_Type=Counter64
_CienaCesBenchmarkEntityStatsEntryPortTxDropPkts_Object=MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortTxDropPkts=_CienaCesBenchmarkEntityStatsEntryPortTxDropPkts_Object((1,3,6,1,4,1,1271,2,1,39,1,1,3,1,13),_CienaCesBenchmarkEntityStatsEntryPortTxDropPkts_Type())
cienaCesBenchmarkEntityStatsEntryPortTxDropPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityStatsEntryPortTxDropPkts.setStatus(_A)
_CienaCesBenchmarkEntityStatsEntryPortTxDiscardPkts_Type=Counter64
_CienaCesBenchmarkEntityStatsEntryPortTxDiscardPkts_Object=MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortTxDiscardPkts=_CienaCesBenchmarkEntityStatsEntryPortTxDiscardPkts_Object((1,3,6,1,4,1,1271,2,1,39,1,1,3,1,14),_CienaCesBenchmarkEntityStatsEntryPortTxDiscardPkts_Type())
cienaCesBenchmarkEntityStatsEntryPortTxDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityStatsEntryPortTxDiscardPkts.setStatus(_A)
_CienaCesBenchmarkEntityStatsEntryPortTxLOutRangePkts_Type=Counter64
_CienaCesBenchmarkEntityStatsEntryPortTxLOutRangePkts_Object=MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortTxLOutRangePkts=_CienaCesBenchmarkEntityStatsEntryPortTxLOutRangePkts_Object((1,3,6,1,4,1,1271,2,1,39,1,1,3,1,15),_CienaCesBenchmarkEntityStatsEntryPortTxLOutRangePkts_Type())
cienaCesBenchmarkEntityStatsEntryPortTxLOutRangePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityStatsEntryPortTxLOutRangePkts.setStatus(_A)
_CienaCesBenchmarkEntityStatsEntryPortTx64OctsPkts_Type=Counter64
_CienaCesBenchmarkEntityStatsEntryPortTx64OctsPkts_Object=MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortTx64OctsPkts=_CienaCesBenchmarkEntityStatsEntryPortTx64OctsPkts_Object((1,3,6,1,4,1,1271,2,1,39,1,1,3,1,16),_CienaCesBenchmarkEntityStatsEntryPortTx64OctsPkts_Type())
cienaCesBenchmarkEntityStatsEntryPortTx64OctsPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityStatsEntryPortTx64OctsPkts.setStatus(_A)
_CienaCesBenchmarkEntityStatsEntryPortTx65To127Pkts_Type=Counter64
_CienaCesBenchmarkEntityStatsEntryPortTx65To127Pkts_Object=MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortTx65To127Pkts=_CienaCesBenchmarkEntityStatsEntryPortTx65To127Pkts_Object((1,3,6,1,4,1,1271,2,1,39,1,1,3,1,17),_CienaCesBenchmarkEntityStatsEntryPortTx65To127Pkts_Type())
cienaCesBenchmarkEntityStatsEntryPortTx65To127Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityStatsEntryPortTx65To127Pkts.setStatus(_A)
_CienaCesBenchmarkEntityStatsEntryPortTx128To255Pkts_Type=Counter64
_CienaCesBenchmarkEntityStatsEntryPortTx128To255Pkts_Object=MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortTx128To255Pkts=_CienaCesBenchmarkEntityStatsEntryPortTx128To255Pkts_Object((1,3,6,1,4,1,1271,2,1,39,1,1,3,1,18),_CienaCesBenchmarkEntityStatsEntryPortTx128To255Pkts_Type())
cienaCesBenchmarkEntityStatsEntryPortTx128To255Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityStatsEntryPortTx128To255Pkts.setStatus(_A)
_CienaCesBenchmarkEntityStatsEntryPortTx256To511Pkts_Type=Counter64
_CienaCesBenchmarkEntityStatsEntryPortTx256To511Pkts_Object=MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortTx256To511Pkts=_CienaCesBenchmarkEntityStatsEntryPortTx256To511Pkts_Object((1,3,6,1,4,1,1271,2,1,39,1,1,3,1,19),_CienaCesBenchmarkEntityStatsEntryPortTx256To511Pkts_Type())
cienaCesBenchmarkEntityStatsEntryPortTx256To511Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityStatsEntryPortTx256To511Pkts.setStatus(_A)
_CienaCesBenchmarkEntityStatsEntryPortTx512To1023Pkts_Type=Counter64
_CienaCesBenchmarkEntityStatsEntryPortTx512To1023Pkts_Object=MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortTx512To1023Pkts=_CienaCesBenchmarkEntityStatsEntryPortTx512To1023Pkts_Object((1,3,6,1,4,1,1271,2,1,39,1,1,3,1,20),_CienaCesBenchmarkEntityStatsEntryPortTx512To1023Pkts_Type())
cienaCesBenchmarkEntityStatsEntryPortTx512To1023Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityStatsEntryPortTx512To1023Pkts.setStatus(_A)
_CienaCesBenchmarkEntityStatsEntryPortTx1024To1518Pkts_Type=Counter64
_CienaCesBenchmarkEntityStatsEntryPortTx1024To1518Pkts_Object=MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortTx1024To1518Pkts=_CienaCesBenchmarkEntityStatsEntryPortTx1024To1518Pkts_Object((1,3,6,1,4,1,1271,2,1,39,1,1,3,1,21),_CienaCesBenchmarkEntityStatsEntryPortTx1024To1518Pkts_Type())
cienaCesBenchmarkEntityStatsEntryPortTx1024To1518Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityStatsEntryPortTx1024To1518Pkts.setStatus(_A)
_CienaCesBenchmarkEntityStatsEntryPortTx1519To2047Pkts_Type=Counter64
_CienaCesBenchmarkEntityStatsEntryPortTx1519To2047Pkts_Object=MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortTx1519To2047Pkts=_CienaCesBenchmarkEntityStatsEntryPortTx1519To2047Pkts_Object((1,3,6,1,4,1,1271,2,1,39,1,1,3,1,22),_CienaCesBenchmarkEntityStatsEntryPortTx1519To2047Pkts_Type())
cienaCesBenchmarkEntityStatsEntryPortTx1519To2047Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityStatsEntryPortTx1519To2047Pkts.setStatus(_A)
_CienaCesBenchmarkEntityStatsEntryPortTx2048To4095Pkts_Type=Counter64
_CienaCesBenchmarkEntityStatsEntryPortTx2048To4095Pkts_Object=MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortTx2048To4095Pkts=_CienaCesBenchmarkEntityStatsEntryPortTx2048To4095Pkts_Object((1,3,6,1,4,1,1271,2,1,39,1,1,3,1,23),_CienaCesBenchmarkEntityStatsEntryPortTx2048To4095Pkts_Type())
cienaCesBenchmarkEntityStatsEntryPortTx2048To4095Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityStatsEntryPortTx2048To4095Pkts.setStatus(_A)
_CienaCesBenchmarkEntityStatsEntryPortTx4096To9216Pkts_Type=Counter64
_CienaCesBenchmarkEntityStatsEntryPortTx4096To9216Pkts_Object=MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortTx4096To9216Pkts=_CienaCesBenchmarkEntityStatsEntryPortTx4096To9216Pkts_Object((1,3,6,1,4,1,1271,2,1,39,1,1,3,1,24),_CienaCesBenchmarkEntityStatsEntryPortTx4096To9216Pkts_Type())
cienaCesBenchmarkEntityStatsEntryPortTx4096To9216Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityStatsEntryPortTx4096To9216Pkts.setStatus(_A)
_CienaCesBenchmarkEntityStatsEntryPortRxBytes_Type=Counter64
_CienaCesBenchmarkEntityStatsEntryPortRxBytes_Object=MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortRxBytes=_CienaCesBenchmarkEntityStatsEntryPortRxBytes_Object((1,3,6,1,4,1,1271,2,1,39,1,1,3,1,25),_CienaCesBenchmarkEntityStatsEntryPortRxBytes_Type())
cienaCesBenchmarkEntityStatsEntryPortRxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityStatsEntryPortRxBytes.setStatus(_A)
_CienaCesBenchmarkEntityStatsEntryPortRxPkts_Type=Counter64
_CienaCesBenchmarkEntityStatsEntryPortRxPkts_Object=MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortRxPkts=_CienaCesBenchmarkEntityStatsEntryPortRxPkts_Object((1,3,6,1,4,1,1271,2,1,39,1,1,3,1,26),_CienaCesBenchmarkEntityStatsEntryPortRxPkts_Type())
cienaCesBenchmarkEntityStatsEntryPortRxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityStatsEntryPortRxPkts.setStatus(_A)
_CienaCesBenchmarkEntityStatsEntryPortRxExDeferPkts_Type=Counter64
_CienaCesBenchmarkEntityStatsEntryPortRxExDeferPkts_Object=MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortRxExDeferPkts=_CienaCesBenchmarkEntityStatsEntryPortRxExDeferPkts_Object((1,3,6,1,4,1,1271,2,1,39,1,1,3,1,27),_CienaCesBenchmarkEntityStatsEntryPortRxExDeferPkts_Type())
cienaCesBenchmarkEntityStatsEntryPortRxExDeferPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityStatsEntryPortRxExDeferPkts.setStatus(_A)
_CienaCesBenchmarkEntityStatsEntryPortRxDeferPkts_Type=Counter64
_CienaCesBenchmarkEntityStatsEntryPortRxDeferPkts_Object=MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortRxDeferPkts=_CienaCesBenchmarkEntityStatsEntryPortRxDeferPkts_Object((1,3,6,1,4,1,1271,2,1,39,1,1,3,1,28),_CienaCesBenchmarkEntityStatsEntryPortRxDeferPkts_Type())
cienaCesBenchmarkEntityStatsEntryPortRxDeferPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityStatsEntryPortRxDeferPkts.setStatus(_A)
_CienaCesBenchmarkEntityStatsEntryPortRxGiantPkts_Type=Counter64
_CienaCesBenchmarkEntityStatsEntryPortRxGiantPkts_Object=MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortRxGiantPkts=_CienaCesBenchmarkEntityStatsEntryPortRxGiantPkts_Object((1,3,6,1,4,1,1271,2,1,39,1,1,3,1,29),_CienaCesBenchmarkEntityStatsEntryPortRxGiantPkts_Type())
cienaCesBenchmarkEntityStatsEntryPortRxGiantPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityStatsEntryPortRxGiantPkts.setStatus(_A)
_CienaCesBenchmarkEntityStatsEntryPortRxUnderRunPkts_Type=Counter64
_CienaCesBenchmarkEntityStatsEntryPortRxUnderRunPkts_Object=MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortRxUnderRunPkts=_CienaCesBenchmarkEntityStatsEntryPortRxUnderRunPkts_Object((1,3,6,1,4,1,1271,2,1,39,1,1,3,1,30),_CienaCesBenchmarkEntityStatsEntryPortRxUnderRunPkts_Type())
cienaCesBenchmarkEntityStatsEntryPortRxUnderRunPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityStatsEntryPortRxUnderRunPkts.setStatus(_A)
_CienaCesBenchmarkEntityStatsEntryPortRxCrcErrorPkts_Type=Counter64
_CienaCesBenchmarkEntityStatsEntryPortRxCrcErrorPkts_Object=MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortRxCrcErrorPkts=_CienaCesBenchmarkEntityStatsEntryPortRxCrcErrorPkts_Object((1,3,6,1,4,1,1271,2,1,39,1,1,3,1,31),_CienaCesBenchmarkEntityStatsEntryPortRxCrcErrorPkts_Type())
cienaCesBenchmarkEntityStatsEntryPortRxCrcErrorPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityStatsEntryPortRxCrcErrorPkts.setStatus(_A)
_CienaCesBenchmarkEntityStatsEntryPortRxLCheckErrorPkts_Type=Counter64
_CienaCesBenchmarkEntityStatsEntryPortRxLCheckErrorPkts_Object=MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortRxLCheckErrorPkts=_CienaCesBenchmarkEntityStatsEntryPortRxLCheckErrorPkts_Object((1,3,6,1,4,1,1271,2,1,39,1,1,3,1,32),_CienaCesBenchmarkEntityStatsEntryPortRxLCheckErrorPkts_Type())
cienaCesBenchmarkEntityStatsEntryPortRxLCheckErrorPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityStatsEntryPortRxLCheckErrorPkts.setStatus(_A)
_CienaCesBenchmarkEntityStatsEntryPortRxLOutRangePkts_Type=Counter64
_CienaCesBenchmarkEntityStatsEntryPortRxLOutRangePkts_Object=MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortRxLOutRangePkts=_CienaCesBenchmarkEntityStatsEntryPortRxLOutRangePkts_Object((1,3,6,1,4,1,1271,2,1,39,1,1,3,1,33),_CienaCesBenchmarkEntityStatsEntryPortRxLOutRangePkts_Type())
cienaCesBenchmarkEntityStatsEntryPortRxLOutRangePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityStatsEntryPortRxLOutRangePkts.setStatus(_A)
_CienaCesBenchmarkEntityStatsEntryPortRxPausePkts_Type=Counter64
_CienaCesBenchmarkEntityStatsEntryPortRxPausePkts_Object=MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortRxPausePkts=_CienaCesBenchmarkEntityStatsEntryPortRxPausePkts_Object((1,3,6,1,4,1,1271,2,1,39,1,1,3,1,34),_CienaCesBenchmarkEntityStatsEntryPortRxPausePkts_Type())
cienaCesBenchmarkEntityStatsEntryPortRxPausePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityStatsEntryPortRxPausePkts.setStatus(_A)
_CienaCesBenchmarkEntityStatsEntryPortRxUcastPkts_Type=Counter64
_CienaCesBenchmarkEntityStatsEntryPortRxUcastPkts_Object=MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortRxUcastPkts=_CienaCesBenchmarkEntityStatsEntryPortRxUcastPkts_Object((1,3,6,1,4,1,1271,2,1,39,1,1,3,1,35),_CienaCesBenchmarkEntityStatsEntryPortRxUcastPkts_Type())
cienaCesBenchmarkEntityStatsEntryPortRxUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityStatsEntryPortRxUcastPkts.setStatus(_A)
_CienaCesBenchmarkEntityStatsEntryPortRxMcastPkts_Type=Counter64
_CienaCesBenchmarkEntityStatsEntryPortRxMcastPkts_Object=MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortRxMcastPkts=_CienaCesBenchmarkEntityStatsEntryPortRxMcastPkts_Object((1,3,6,1,4,1,1271,2,1,39,1,1,3,1,36),_CienaCesBenchmarkEntityStatsEntryPortRxMcastPkts_Type())
cienaCesBenchmarkEntityStatsEntryPortRxMcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityStatsEntryPortRxMcastPkts.setStatus(_A)
_CienaCesBenchmarkEntityStatsEntryPortRxBcastPkts_Type=Counter64
_CienaCesBenchmarkEntityStatsEntryPortRxBcastPkts_Object=MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortRxBcastPkts=_CienaCesBenchmarkEntityStatsEntryPortRxBcastPkts_Object((1,3,6,1,4,1,1271,2,1,39,1,1,3,1,37),_CienaCesBenchmarkEntityStatsEntryPortRxBcastPkts_Type())
cienaCesBenchmarkEntityStatsEntryPortRxBcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityStatsEntryPortRxBcastPkts.setStatus(_A)
_CienaCesBenchmarkEntityStatsEntryPortRx64OctsPkts_Type=Counter64
_CienaCesBenchmarkEntityStatsEntryPortRx64OctsPkts_Object=MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortRx64OctsPkts=_CienaCesBenchmarkEntityStatsEntryPortRx64OctsPkts_Object((1,3,6,1,4,1,1271,2,1,39,1,1,3,1,38),_CienaCesBenchmarkEntityStatsEntryPortRx64OctsPkts_Type())
cienaCesBenchmarkEntityStatsEntryPortRx64OctsPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityStatsEntryPortRx64OctsPkts.setStatus(_A)
_CienaCesBenchmarkEntityStatsEntryPortRx65To127Pkts_Type=Counter64
_CienaCesBenchmarkEntityStatsEntryPortRx65To127Pkts_Object=MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortRx65To127Pkts=_CienaCesBenchmarkEntityStatsEntryPortRx65To127Pkts_Object((1,3,6,1,4,1,1271,2,1,39,1,1,3,1,39),_CienaCesBenchmarkEntityStatsEntryPortRx65To127Pkts_Type())
cienaCesBenchmarkEntityStatsEntryPortRx65To127Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityStatsEntryPortRx65To127Pkts.setStatus(_A)
_CienaCesBenchmarkEntityStatsEntryPortRx128To255Pkts_Type=Counter64
_CienaCesBenchmarkEntityStatsEntryPortRx128To255Pkts_Object=MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortRx128To255Pkts=_CienaCesBenchmarkEntityStatsEntryPortRx128To255Pkts_Object((1,3,6,1,4,1,1271,2,1,39,1,1,3,1,40),_CienaCesBenchmarkEntityStatsEntryPortRx128To255Pkts_Type())
cienaCesBenchmarkEntityStatsEntryPortRx128To255Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityStatsEntryPortRx128To255Pkts.setStatus(_A)
_CienaCesBenchmarkEntityStatsEntryPortRx256To511Pkts_Type=Counter64
_CienaCesBenchmarkEntityStatsEntryPortRx256To511Pkts_Object=MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortRx256To511Pkts=_CienaCesBenchmarkEntityStatsEntryPortRx256To511Pkts_Object((1,3,6,1,4,1,1271,2,1,39,1,1,3,1,41),_CienaCesBenchmarkEntityStatsEntryPortRx256To511Pkts_Type())
cienaCesBenchmarkEntityStatsEntryPortRx256To511Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityStatsEntryPortRx256To511Pkts.setStatus(_A)
_CienaCesBenchmarkEntityStatsEntryPortRx512To1023Pkts_Type=Counter64
_CienaCesBenchmarkEntityStatsEntryPortRx512To1023Pkts_Object=MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortRx512To1023Pkts=_CienaCesBenchmarkEntityStatsEntryPortRx512To1023Pkts_Object((1,3,6,1,4,1,1271,2,1,39,1,1,3,1,42),_CienaCesBenchmarkEntityStatsEntryPortRx512To1023Pkts_Type())
cienaCesBenchmarkEntityStatsEntryPortRx512To1023Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityStatsEntryPortRx512To1023Pkts.setStatus(_A)
_CienaCesBenchmarkEntityStatsEntryPortRx1024To1518Pkts_Type=Counter64
_CienaCesBenchmarkEntityStatsEntryPortRx1024To1518Pkts_Object=MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortRx1024To1518Pkts=_CienaCesBenchmarkEntityStatsEntryPortRx1024To1518Pkts_Object((1,3,6,1,4,1,1271,2,1,39,1,1,3,1,43),_CienaCesBenchmarkEntityStatsEntryPortRx1024To1518Pkts_Type())
cienaCesBenchmarkEntityStatsEntryPortRx1024To1518Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityStatsEntryPortRx1024To1518Pkts.setStatus(_A)
_CienaCesBenchmarkEntityStatsEntryPortRx1519To2047Pkts_Type=Counter64
_CienaCesBenchmarkEntityStatsEntryPortRx1519To2047Pkts_Object=MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortRx1519To2047Pkts=_CienaCesBenchmarkEntityStatsEntryPortRx1519To2047Pkts_Object((1,3,6,1,4,1,1271,2,1,39,1,1,3,1,44),_CienaCesBenchmarkEntityStatsEntryPortRx1519To2047Pkts_Type())
cienaCesBenchmarkEntityStatsEntryPortRx1519To2047Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityStatsEntryPortRx1519To2047Pkts.setStatus(_A)
_CienaCesBenchmarkEntityStatsEntryPortRx2048To4095Pkts_Type=Counter64
_CienaCesBenchmarkEntityStatsEntryPortRx2048To4095Pkts_Object=MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortRx2048To4095Pkts=_CienaCesBenchmarkEntityStatsEntryPortRx2048To4095Pkts_Object((1,3,6,1,4,1,1271,2,1,39,1,1,3,1,45),_CienaCesBenchmarkEntityStatsEntryPortRx2048To4095Pkts_Type())
cienaCesBenchmarkEntityStatsEntryPortRx2048To4095Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityStatsEntryPortRx2048To4095Pkts.setStatus(_A)
_CienaCesBenchmarkEntityStatsEntryPortRx4096To9216Pkts_Type=Counter64
_CienaCesBenchmarkEntityStatsEntryPortRx4096To9216Pkts_Object=MibTableColumn
cienaCesBenchmarkEntityStatsEntryPortRx4096To9216Pkts=_CienaCesBenchmarkEntityStatsEntryPortRx4096To9216Pkts_Object((1,3,6,1,4,1,1271,2,1,39,1,1,3,1,46),_CienaCesBenchmarkEntityStatsEntryPortRx4096To9216Pkts_Type())
cienaCesBenchmarkEntityStatsEntryPortRx4096To9216Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityStatsEntryPortRx4096To9216Pkts.setStatus(_A)
_CienaCesBenchmarkEntityStatsEntryFpgaMissClassPkts_Type=Counter64
_CienaCesBenchmarkEntityStatsEntryFpgaMissClassPkts_Object=MibTableColumn
cienaCesBenchmarkEntityStatsEntryFpgaMissClassPkts=_CienaCesBenchmarkEntityStatsEntryFpgaMissClassPkts_Object((1,3,6,1,4,1,1271,2,1,39,1,1,3,1,47),_CienaCesBenchmarkEntityStatsEntryFpgaMissClassPkts_Type())
cienaCesBenchmarkEntityStatsEntryFpgaMissClassPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityStatsEntryFpgaMissClassPkts.setStatus(_A)
_CienaCesBenchmarkEntityStatsEntryFpgaCrcErrPkts_Type=Counter64
_CienaCesBenchmarkEntityStatsEntryFpgaCrcErrPkts_Object=MibTableColumn
cienaCesBenchmarkEntityStatsEntryFpgaCrcErrPkts=_CienaCesBenchmarkEntityStatsEntryFpgaCrcErrPkts_Object((1,3,6,1,4,1,1271,2,1,39,1,1,3,1,48),_CienaCesBenchmarkEntityStatsEntryFpgaCrcErrPkts_Type())
cienaCesBenchmarkEntityStatsEntryFpgaCrcErrPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityStatsEntryFpgaCrcErrPkts.setStatus(_A)
_CienaCesBenchmarkEntityStatsEntryFpgaUdpChkSumErrPkts_Type=Counter64
_CienaCesBenchmarkEntityStatsEntryFpgaUdpChkSumErrPkts_Object=MibTableColumn
cienaCesBenchmarkEntityStatsEntryFpgaUdpChkSumErrPkts=_CienaCesBenchmarkEntityStatsEntryFpgaUdpChkSumErrPkts_Object((1,3,6,1,4,1,1271,2,1,39,1,1,3,1,49),_CienaCesBenchmarkEntityStatsEntryFpgaUdpChkSumErrPkts_Type())
cienaCesBenchmarkEntityStatsEntryFpgaUdpChkSumErrPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEntityStatsEntryFpgaUdpChkSumErrPkts.setStatus(_A)
_CienaCesBenchmarkEmixSequenceTable_Object=MibTable
cienaCesBenchmarkEmixSequenceTable=_CienaCesBenchmarkEmixSequenceTable_Object((1,3,6,1,4,1,1271,2,1,39,1,1,4))
if mibBuilder.loadTexts:cienaCesBenchmarkEmixSequenceTable.setStatus(_A)
_CienaCesBenchmarkEmixSequenceEntry_Object=MibTableRow
cienaCesBenchmarkEmixSequenceEntry=_CienaCesBenchmarkEmixSequenceEntry_Object((1,3,6,1,4,1,1271,2,1,39,1,1,4,1))
cienaCesBenchmarkEmixSequenceEntry.setIndexNames((0,_C,_P))
if mibBuilder.loadTexts:cienaCesBenchmarkEmixSequenceEntry.setStatus(_A)
class _CienaCesBenchmarkEmixSequenceId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_CienaCesBenchmarkEmixSequenceId_Type.__name__=_E
_CienaCesBenchmarkEmixSequenceId_Object=MibTableColumn
cienaCesBenchmarkEmixSequenceId=_CienaCesBenchmarkEmixSequenceId_Object((1,3,6,1,4,1,1271,2,1,39,1,1,4,1,1),_CienaCesBenchmarkEmixSequenceId_Type())
cienaCesBenchmarkEmixSequenceId.setMaxAccess(_F)
if mibBuilder.loadTexts:cienaCesBenchmarkEmixSequenceId.setStatus(_A)
class _CienaCesBenchmarkEmixSequenceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,46))
_CienaCesBenchmarkEmixSequenceName_Type.__name__=_I
_CienaCesBenchmarkEmixSequenceName_Object=MibTableColumn
cienaCesBenchmarkEmixSequenceName=_CienaCesBenchmarkEmixSequenceName_Object((1,3,6,1,4,1,1271,2,1,39,1,1,4,1,2),_CienaCesBenchmarkEmixSequenceName_Type())
cienaCesBenchmarkEmixSequenceName.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkEmixSequenceName.setStatus(_A)
class _CienaCesBenchmarkEmixSequence_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_CienaCesBenchmarkEmixSequence_Type.__name__=_I
_CienaCesBenchmarkEmixSequence_Object=MibTableColumn
cienaCesBenchmarkEmixSequence=_CienaCesBenchmarkEmixSequence_Object((1,3,6,1,4,1,1271,2,1,39,1,1,4,1,3),_CienaCesBenchmarkEmixSequence_Type())
cienaCesBenchmarkEmixSequence.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkEmixSequence.setStatus(_A)
class _CienaCesBenchmarkEmixSequenceUFrameSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,9216))
_CienaCesBenchmarkEmixSequenceUFrameSize_Type.__name__=_E
_CienaCesBenchmarkEmixSequenceUFrameSize_Object=MibTableColumn
cienaCesBenchmarkEmixSequenceUFrameSize=_CienaCesBenchmarkEmixSequenceUFrameSize_Object((1,3,6,1,4,1,1271,2,1,39,1,1,4,1,4),_CienaCesBenchmarkEmixSequenceUFrameSize_Type())
cienaCesBenchmarkEmixSequenceUFrameSize.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkEmixSequenceUFrameSize.setStatus(_A)
_CienaCesBenchmarkEmixSequenceNumOfRef_Type=Integer32
_CienaCesBenchmarkEmixSequenceNumOfRef_Object=MibTableColumn
cienaCesBenchmarkEmixSequenceNumOfRef=_CienaCesBenchmarkEmixSequenceNumOfRef_Object((1,3,6,1,4,1,1271,2,1,39,1,1,4,1,5),_CienaCesBenchmarkEmixSequenceNumOfRef_Type())
cienaCesBenchmarkEmixSequenceNumOfRef.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEmixSequenceNumOfRef.setStatus(_A)
_CienaCesBenchmarkEmixSequenceUserCreated_Type=TruthValue
_CienaCesBenchmarkEmixSequenceUserCreated_Object=MibTableColumn
cienaCesBenchmarkEmixSequenceUserCreated=_CienaCesBenchmarkEmixSequenceUserCreated_Object((1,3,6,1,4,1,1271,2,1,39,1,1,4,1,6),_CienaCesBenchmarkEmixSequenceUserCreated_Type())
cienaCesBenchmarkEmixSequenceUserCreated.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEmixSequenceUserCreated.setStatus(_A)
_CienaCesBenchmarkEmixSequenceRowStatus_Type=RowStatus
_CienaCesBenchmarkEmixSequenceRowStatus_Object=MibTableColumn
cienaCesBenchmarkEmixSequenceRowStatus=_CienaCesBenchmarkEmixSequenceRowStatus_Object((1,3,6,1,4,1,1271,2,1,39,1,1,4,1,7),_CienaCesBenchmarkEmixSequenceRowStatus_Type())
cienaCesBenchmarkEmixSequenceRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkEmixSequenceRowStatus.setStatus(_A)
_CienaCesBenchmarkEmixFrameSizeTable_Object=MibTable
cienaCesBenchmarkEmixFrameSizeTable=_CienaCesBenchmarkEmixFrameSizeTable_Object((1,3,6,1,4,1,1271,2,1,39,1,1,5))
if mibBuilder.loadTexts:cienaCesBenchmarkEmixFrameSizeTable.setStatus(_A)
_CienaCesBenchmarkEmixFrameSizeEntry_Object=MibTableRow
cienaCesBenchmarkEmixFrameSizeEntry=_CienaCesBenchmarkEmixFrameSizeEntry_Object((1,3,6,1,4,1,1271,2,1,39,1,1,5,1))
cienaCesBenchmarkEmixFrameSizeEntry.setIndexNames((0,_C,_J),(0,_C,_P),(0,_C,_g))
if mibBuilder.loadTexts:cienaCesBenchmarkEmixFrameSizeEntry.setStatus(_A)
class _CienaCesBenchmarkEmixFrameSizeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_CienaCesBenchmarkEmixFrameSizeIndex_Type.__name__=_E
_CienaCesBenchmarkEmixFrameSizeIndex_Object=MibTableColumn
cienaCesBenchmarkEmixFrameSizeIndex=_CienaCesBenchmarkEmixFrameSizeIndex_Object((1,3,6,1,4,1,1271,2,1,39,1,1,5,1,1),_CienaCesBenchmarkEmixFrameSizeIndex_Type())
cienaCesBenchmarkEmixFrameSizeIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cienaCesBenchmarkEmixFrameSizeIndex.setStatus(_A)
class _CienaCesBenchmarkEmixFrameSizeEntryFrameSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,9216))
_CienaCesBenchmarkEmixFrameSizeEntryFrameSize_Type.__name__=_E
_CienaCesBenchmarkEmixFrameSizeEntryFrameSize_Object=MibTableColumn
cienaCesBenchmarkEmixFrameSizeEntryFrameSize=_CienaCesBenchmarkEmixFrameSizeEntryFrameSize_Object((1,3,6,1,4,1,1271,2,1,39,1,1,5,1,2),_CienaCesBenchmarkEmixFrameSizeEntryFrameSize_Type())
cienaCesBenchmarkEmixFrameSizeEntryFrameSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEmixFrameSizeEntryFrameSize.setStatus(_A)
_CienaCesBenchmarkEmixAvgFrameSizeTable_Object=MibTable
cienaCesBenchmarkEmixAvgFrameSizeTable=_CienaCesBenchmarkEmixAvgFrameSizeTable_Object((1,3,6,1,4,1,1271,2,1,39,1,1,6))
if mibBuilder.loadTexts:cienaCesBenchmarkEmixAvgFrameSizeTable.setStatus(_A)
_CienaCesBenchmarkEmixAvgFrameSizeEntry_Object=MibTableRow
cienaCesBenchmarkEmixAvgFrameSizeEntry=_CienaCesBenchmarkEmixAvgFrameSizeEntry_Object((1,3,6,1,4,1,1271,2,1,39,1,1,6,1))
cienaCesBenchmarkEmixAvgFrameSizeEntry.setIndexNames((0,_C,_J),(0,_C,_P))
if mibBuilder.loadTexts:cienaCesBenchmarkEmixAvgFrameSizeEntry.setStatus(_A)
class _CienaCesBenchmarkEmixAvgFrameSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,9216))
_CienaCesBenchmarkEmixAvgFrameSize_Type.__name__=_E
_CienaCesBenchmarkEmixAvgFrameSize_Object=MibTableColumn
cienaCesBenchmarkEmixAvgFrameSize=_CienaCesBenchmarkEmixAvgFrameSize_Object((1,3,6,1,4,1,1271,2,1,39,1,1,6,1,1),_CienaCesBenchmarkEmixAvgFrameSize_Type())
cienaCesBenchmarkEmixAvgFrameSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEmixAvgFrameSize.setStatus(_A)
_CienaCesBenchmarkKpiProfileTable_Object=MibTable
cienaCesBenchmarkKpiProfileTable=_CienaCesBenchmarkKpiProfileTable_Object((1,3,6,1,4,1,1271,2,1,39,1,1,7))
if mibBuilder.loadTexts:cienaCesBenchmarkKpiProfileTable.setStatus(_A)
_CienaCesBenchmarkKpiProfileEntry_Object=MibTableRow
cienaCesBenchmarkKpiProfileEntry=_CienaCesBenchmarkKpiProfileEntry_Object((1,3,6,1,4,1,1271,2,1,39,1,1,7,1))
cienaCesBenchmarkKpiProfileEntry.setIndexNames((0,_C,_Q))
if mibBuilder.loadTexts:cienaCesBenchmarkKpiProfileEntry.setStatus(_A)
class _CienaCesBenchmarkKpiProfileId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_CienaCesBenchmarkKpiProfileId_Type.__name__=_E
_CienaCesBenchmarkKpiProfileId_Object=MibTableColumn
cienaCesBenchmarkKpiProfileId=_CienaCesBenchmarkKpiProfileId_Object((1,3,6,1,4,1,1271,2,1,39,1,1,7,1,1),_CienaCesBenchmarkKpiProfileId_Type())
cienaCesBenchmarkKpiProfileId.setMaxAccess(_F)
if mibBuilder.loadTexts:cienaCesBenchmarkKpiProfileId.setStatus(_A)
class _CienaCesBenchmarkKpiProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,46))
_CienaCesBenchmarkKpiProfileName_Type.__name__=_I
_CienaCesBenchmarkKpiProfileName_Object=MibTableColumn
cienaCesBenchmarkKpiProfileName=_CienaCesBenchmarkKpiProfileName_Object((1,3,6,1,4,1,1271,2,1,39,1,1,7,1,2),_CienaCesBenchmarkKpiProfileName_Type())
cienaCesBenchmarkKpiProfileName.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkKpiProfileName.setStatus(_A)
_CienaCesBenchmarkKpiProfileNumOfRef_Type=Integer32
_CienaCesBenchmarkKpiProfileNumOfRef_Object=MibTableColumn
cienaCesBenchmarkKpiProfileNumOfRef=_CienaCesBenchmarkKpiProfileNumOfRef_Object((1,3,6,1,4,1,1271,2,1,39,1,1,7,1,3),_CienaCesBenchmarkKpiProfileNumOfRef_Type())
cienaCesBenchmarkKpiProfileNumOfRef.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkKpiProfileNumOfRef.setStatus(_A)
_CienaCesBenchmarkKpiProfileRowStatus_Type=RowStatus
_CienaCesBenchmarkKpiProfileRowStatus_Object=MibTableColumn
cienaCesBenchmarkKpiProfileRowStatus=_CienaCesBenchmarkKpiProfileRowStatus_Object((1,3,6,1,4,1,1271,2,1,39,1,1,7,1,4),_CienaCesBenchmarkKpiProfileRowStatus_Type())
cienaCesBenchmarkKpiProfileRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkKpiProfileRowStatus.setStatus(_A)
_CienaCesBenchmarkKpiPcpColorTable_Object=MibTable
cienaCesBenchmarkKpiPcpColorTable=_CienaCesBenchmarkKpiPcpColorTable_Object((1,3,6,1,4,1,1271,2,1,39,1,1,8))
if mibBuilder.loadTexts:cienaCesBenchmarkKpiPcpColorTable.setStatus(_A)
_CienaCesBenchmarkKpiPcpColorEntry_Object=MibTableRow
cienaCesBenchmarkKpiPcpColorEntry=_CienaCesBenchmarkKpiPcpColorEntry_Object((1,3,6,1,4,1,1271,2,1,39,1,1,8,1))
cienaCesBenchmarkKpiPcpColorEntry.setIndexNames((0,_C,_Q),(0,_C,_h),(0,_C,_i))
if mibBuilder.loadTexts:cienaCesBenchmarkKpiPcpColorEntry.setStatus(_A)
class _CienaCesBenchmarkKpiPcpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_CienaCesBenchmarkKpiPcpIndex_Type.__name__=_E
_CienaCesBenchmarkKpiPcpIndex_Object=MibTableColumn
cienaCesBenchmarkKpiPcpIndex=_CienaCesBenchmarkKpiPcpIndex_Object((1,3,6,1,4,1,1271,2,1,39,1,1,8,1,1),_CienaCesBenchmarkKpiPcpIndex_Type())
cienaCesBenchmarkKpiPcpIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cienaCesBenchmarkKpiPcpIndex.setStatus(_A)
class _CienaCesBenchmarkKpiColorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_CienaCesBenchmarkKpiColorIndex_Type.__name__=_E
_CienaCesBenchmarkKpiColorIndex_Object=MibTableColumn
cienaCesBenchmarkKpiColorIndex=_CienaCesBenchmarkKpiColorIndex_Object((1,3,6,1,4,1,1271,2,1,39,1,1,8,1,2),_CienaCesBenchmarkKpiColorIndex_Type())
cienaCesBenchmarkKpiColorIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cienaCesBenchmarkKpiColorIndex.setStatus(_A)
class _CienaCesBenchmarkKpiPcp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_CienaCesBenchmarkKpiPcp_Type.__name__=_E
_CienaCesBenchmarkKpiPcp_Object=MibTableColumn
cienaCesBenchmarkKpiPcp=_CienaCesBenchmarkKpiPcp_Object((1,3,6,1,4,1,1271,2,1,39,1,1,8,1,3),_CienaCesBenchmarkKpiPcp_Type())
cienaCesBenchmarkKpiPcp.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkKpiPcp.setStatus(_A)
_CienaCesBenchmarkKpiColor_Type=CienaCesBenchmarkColorTest
_CienaCesBenchmarkKpiColor_Object=MibTableColumn
cienaCesBenchmarkKpiColor=_CienaCesBenchmarkKpiColor_Object((1,3,6,1,4,1,1271,2,1,39,1,1,8,1,4),_CienaCesBenchmarkKpiColor_Type())
cienaCesBenchmarkKpiColor.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkKpiColor.setStatus(_A)
_CienaCesBenchmarkKpiThroughput_Type=CienaCesBenchmarkThroughputKpiPercent
_CienaCesBenchmarkKpiThroughput_Object=MibTableColumn
cienaCesBenchmarkKpiThroughput=_CienaCesBenchmarkKpiThroughput_Object((1,3,6,1,4,1,1271,2,1,39,1,1,8,1,5),_CienaCesBenchmarkKpiThroughput_Type())
cienaCesBenchmarkKpiThroughput.setMaxAccess(_L)
if mibBuilder.loadTexts:cienaCesBenchmarkKpiThroughput.setStatus(_A)
_CienaCesBenchmarkKpiFrameloss_Type=CienaCesBenchmarkFramelossKpiPercent
_CienaCesBenchmarkKpiFrameloss_Object=MibTableColumn
cienaCesBenchmarkKpiFrameloss=_CienaCesBenchmarkKpiFrameloss_Object((1,3,6,1,4,1,1271,2,1,39,1,1,8,1,6),_CienaCesBenchmarkKpiFrameloss_Type())
cienaCesBenchmarkKpiFrameloss.setMaxAccess(_L)
if mibBuilder.loadTexts:cienaCesBenchmarkKpiFrameloss.setStatus(_A)
_CienaCesBenchmarkKpiLatency_Type=Integer32
_CienaCesBenchmarkKpiLatency_Object=MibTableColumn
cienaCesBenchmarkKpiLatency=_CienaCesBenchmarkKpiLatency_Object((1,3,6,1,4,1,1271,2,1,39,1,1,8,1,7),_CienaCesBenchmarkKpiLatency_Type())
cienaCesBenchmarkKpiLatency.setMaxAccess(_L)
if mibBuilder.loadTexts:cienaCesBenchmarkKpiLatency.setStatus(_A)
if mibBuilder.loadTexts:cienaCesBenchmarkKpiLatency.setUnits(_j)
_CienaCesBenchmarkKpiPdv_Type=Integer32
_CienaCesBenchmarkKpiPdv_Object=MibTableColumn
cienaCesBenchmarkKpiPdv=_CienaCesBenchmarkKpiPdv_Object((1,3,6,1,4,1,1271,2,1,39,1,1,8,1,8),_CienaCesBenchmarkKpiPdv_Type())
cienaCesBenchmarkKpiPdv.setMaxAccess(_L)
if mibBuilder.loadTexts:cienaCesBenchmarkKpiPdv.setStatus(_A)
if mibBuilder.loadTexts:cienaCesBenchmarkKpiPdv.setUnits(_j)
_CienaCesBenchmarkBwAllocProfileTable_Object=MibTable
cienaCesBenchmarkBwAllocProfileTable=_CienaCesBenchmarkBwAllocProfileTable_Object((1,3,6,1,4,1,1271,2,1,39,1,1,9))
if mibBuilder.loadTexts:cienaCesBenchmarkBwAllocProfileTable.setStatus(_A)
_CienaCesBenchmarkBwAllocProfileEntry_Object=MibTableRow
cienaCesBenchmarkBwAllocProfileEntry=_CienaCesBenchmarkBwAllocProfileEntry_Object((1,3,6,1,4,1,1271,2,1,39,1,1,9,1))
cienaCesBenchmarkBwAllocProfileEntry.setIndexNames((0,_C,_b))
if mibBuilder.loadTexts:cienaCesBenchmarkBwAllocProfileEntry.setStatus(_A)
class _CienaCesBenchmarkBwAllocProfileId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_CienaCesBenchmarkBwAllocProfileId_Type.__name__=_E
_CienaCesBenchmarkBwAllocProfileId_Object=MibTableColumn
cienaCesBenchmarkBwAllocProfileId=_CienaCesBenchmarkBwAllocProfileId_Object((1,3,6,1,4,1,1271,2,1,39,1,1,9,1,1),_CienaCesBenchmarkBwAllocProfileId_Type())
cienaCesBenchmarkBwAllocProfileId.setMaxAccess(_F)
if mibBuilder.loadTexts:cienaCesBenchmarkBwAllocProfileId.setStatus(_A)
class _CienaCesBenchmarkBwAllocProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,46))
_CienaCesBenchmarkBwAllocProfileName_Type.__name__=_I
_CienaCesBenchmarkBwAllocProfileName_Object=MibTableColumn
cienaCesBenchmarkBwAllocProfileName=_CienaCesBenchmarkBwAllocProfileName_Object((1,3,6,1,4,1,1271,2,1,39,1,1,9,1,2),_CienaCesBenchmarkBwAllocProfileName_Type())
cienaCesBenchmarkBwAllocProfileName.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkBwAllocProfileName.setStatus(_A)
_CienaCesBenchmarkBwAllocProfileNumOfRef_Type=Integer32
_CienaCesBenchmarkBwAllocProfileNumOfRef_Object=MibTableColumn
cienaCesBenchmarkBwAllocProfileNumOfRef=_CienaCesBenchmarkBwAllocProfileNumOfRef_Object((1,3,6,1,4,1,1271,2,1,39,1,1,9,1,3),_CienaCesBenchmarkBwAllocProfileNumOfRef_Type())
cienaCesBenchmarkBwAllocProfileNumOfRef.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkBwAllocProfileNumOfRef.setStatus(_A)
_CienaCesBenchmarkBwAllocProfileRowStatus_Type=RowStatus
_CienaCesBenchmarkBwAllocProfileRowStatus_Object=MibTableColumn
cienaCesBenchmarkBwAllocProfileRowStatus=_CienaCesBenchmarkBwAllocProfileRowStatus_Object((1,3,6,1,4,1,1271,2,1,39,1,1,9,1,4),_CienaCesBenchmarkBwAllocProfileRowStatus_Type())
cienaCesBenchmarkBwAllocProfileRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkBwAllocProfileRowStatus.setStatus(_A)
_CienaCesBenchmarkBwRatioTable_Object=MibTable
cienaCesBenchmarkBwRatioTable=_CienaCesBenchmarkBwRatioTable_Object((1,3,6,1,4,1,1271,2,1,39,1,1,10))
if mibBuilder.loadTexts:cienaCesBenchmarkBwRatioTable.setStatus(_A)
_CienaCesBenchmarkBwRatioEntry_Object=MibTableRow
cienaCesBenchmarkBwRatioEntry=_CienaCesBenchmarkBwRatioEntry_Object((1,3,6,1,4,1,1271,2,1,39,1,1,10,1))
cienaCesBenchmarkBwRatioEntry.setIndexNames((0,_C,_b),(0,_C,_k))
if mibBuilder.loadTexts:cienaCesBenchmarkBwRatioEntry.setStatus(_A)
class _CienaCesBenchmarkBwRatioPcpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_CienaCesBenchmarkBwRatioPcpIndex_Type.__name__=_E
_CienaCesBenchmarkBwRatioPcpIndex_Object=MibTableColumn
cienaCesBenchmarkBwRatioPcpIndex=_CienaCesBenchmarkBwRatioPcpIndex_Object((1,3,6,1,4,1,1271,2,1,39,1,1,10,1,1),_CienaCesBenchmarkBwRatioPcpIndex_Type())
cienaCesBenchmarkBwRatioPcpIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cienaCesBenchmarkBwRatioPcpIndex.setStatus(_A)
class _CienaCesBenchmarkBwRatioPcp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_CienaCesBenchmarkBwRatioPcp_Type.__name__=_E
_CienaCesBenchmarkBwRatioPcp_Object=MibTableColumn
cienaCesBenchmarkBwRatioPcp=_CienaCesBenchmarkBwRatioPcp_Object((1,3,6,1,4,1,1271,2,1,39,1,1,10,1,2),_CienaCesBenchmarkBwRatioPcp_Type())
cienaCesBenchmarkBwRatioPcp.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkBwRatioPcp.setStatus(_A)
class _CienaCesBenchmarkBwRatio_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_CienaCesBenchmarkBwRatio_Type.__name__=_E
_CienaCesBenchmarkBwRatio_Object=MibTableColumn
cienaCesBenchmarkBwRatio=_CienaCesBenchmarkBwRatio_Object((1,3,6,1,4,1,1271,2,1,39,1,1,10,1,3),_CienaCesBenchmarkBwRatio_Type())
cienaCesBenchmarkBwRatio.setMaxAccess(_L)
if mibBuilder.loadTexts:cienaCesBenchmarkBwRatio.setStatus(_A)
_CienaCesBenchmarkProfileTable_Object=MibTable
cienaCesBenchmarkProfileTable=_CienaCesBenchmarkProfileTable_Object((1,3,6,1,4,1,1271,2,1,39,1,1,11))
if mibBuilder.loadTexts:cienaCesBenchmarkProfileTable.setStatus(_A)
_CienaCesBenchmarkProfileEntry_Object=MibTableRow
cienaCesBenchmarkProfileEntry=_CienaCesBenchmarkProfileEntry_Object((1,3,6,1,4,1,1271,2,1,39,1,1,11,1))
cienaCesBenchmarkProfileEntry.setIndexNames((0,_C,_l))
if mibBuilder.loadTexts:cienaCesBenchmarkProfileEntry.setStatus(_A)
_CienaCesBenchmarkProfileEntryId_Type=Integer32
_CienaCesBenchmarkProfileEntryId_Object=MibTableColumn
cienaCesBenchmarkProfileEntryId=_CienaCesBenchmarkProfileEntryId_Object((1,3,6,1,4,1,1271,2,1,39,1,1,11,1,1),_CienaCesBenchmarkProfileEntryId_Type())
cienaCesBenchmarkProfileEntryId.setMaxAccess(_F)
if mibBuilder.loadTexts:cienaCesBenchmarkProfileEntryId.setStatus(_A)
class _CienaCesBenchmarkProfileEntryName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,46))
_CienaCesBenchmarkProfileEntryName_Type.__name__=_I
_CienaCesBenchmarkProfileEntryName_Object=MibTableColumn
cienaCesBenchmarkProfileEntryName=_CienaCesBenchmarkProfileEntryName_Object((1,3,6,1,4,1,1271,2,1,39,1,1,11,1,2),_CienaCesBenchmarkProfileEntryName_Type())
cienaCesBenchmarkProfileEntryName.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkProfileEntryName.setStatus(_A)
class _CienaCesBenchmarkProfileEntryBandwidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10000))
_CienaCesBenchmarkProfileEntryBandwidth_Type.__name__=_E
_CienaCesBenchmarkProfileEntryBandwidth_Object=MibTableColumn
cienaCesBenchmarkProfileEntryBandwidth=_CienaCesBenchmarkProfileEntryBandwidth_Object((1,3,6,1,4,1,1271,2,1,39,1,1,11,1,3),_CienaCesBenchmarkProfileEntryBandwidth_Type())
cienaCesBenchmarkProfileEntryBandwidth.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkProfileEntryBandwidth.setStatus(_A)
class _CienaCesBenchmarkProfileEntryExcessBandwidth_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_CienaCesBenchmarkProfileEntryExcessBandwidth_Type.__name__=_E
_CienaCesBenchmarkProfileEntryExcessBandwidth_Object=MibTableColumn
cienaCesBenchmarkProfileEntryExcessBandwidth=_CienaCesBenchmarkProfileEntryExcessBandwidth_Object((1,3,6,1,4,1,1271,2,1,39,1,1,11,1,4),_CienaCesBenchmarkProfileEntryExcessBandwidth_Type())
cienaCesBenchmarkProfileEntryExcessBandwidth.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkProfileEntryExcessBandwidth.setStatus(_A)
class _CienaCesBenchmarkProfileEntryInterval_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_m,1),('t1hr',2),('t6hr',3),('tCompletion',4),('t2hr',5)))
_CienaCesBenchmarkProfileEntryInterval_Type.__name__=_E
_CienaCesBenchmarkProfileEntryInterval_Object=MibTableColumn
cienaCesBenchmarkProfileEntryInterval=_CienaCesBenchmarkProfileEntryInterval_Object((1,3,6,1,4,1,1271,2,1,39,1,1,11,1,5),_CienaCesBenchmarkProfileEntryInterval_Type())
cienaCesBenchmarkProfileEntryInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkProfileEntryInterval.setStatus(_A)
class _CienaCesBenchmarkProfileEntryDuration_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_m,1),('t1hr',2),('t6hr',3),('t24hr',4),('tIndefinite',5),('tOnce',6)))
_CienaCesBenchmarkProfileEntryDuration_Type.__name__=_E
_CienaCesBenchmarkProfileEntryDuration_Object=MibTableColumn
cienaCesBenchmarkProfileEntryDuration=_CienaCesBenchmarkProfileEntryDuration_Object((1,3,6,1,4,1,1271,2,1,39,1,1,11,1,6),_CienaCesBenchmarkProfileEntryDuration_Type())
cienaCesBenchmarkProfileEntryDuration.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkProfileEntryDuration.setStatus(_A)
class _CienaCesBenchmarkProfileEntrySetFrameSizeList_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CienaCesBenchmarkProfileEntrySetFrameSizeList_Type.__name__=_I
_CienaCesBenchmarkProfileEntrySetFrameSizeList_Object=MibTableColumn
cienaCesBenchmarkProfileEntrySetFrameSizeList=_CienaCesBenchmarkProfileEntrySetFrameSizeList_Object((1,3,6,1,4,1,1271,2,1,39,1,1,11,1,7),_CienaCesBenchmarkProfileEntrySetFrameSizeList_Type())
cienaCesBenchmarkProfileEntrySetFrameSizeList.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkProfileEntrySetFrameSizeList.setStatus(_A)
class _CienaCesBenchmarkProfileEntryMaxSearches_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_CienaCesBenchmarkProfileEntryMaxSearches_Type.__name__=_E
_CienaCesBenchmarkProfileEntryMaxSearches_Object=MibTableColumn
cienaCesBenchmarkProfileEntryMaxSearches=_CienaCesBenchmarkProfileEntryMaxSearches_Object((1,3,6,1,4,1,1271,2,1,39,1,1,11,1,8),_CienaCesBenchmarkProfileEntryMaxSearches_Type())
cienaCesBenchmarkProfileEntryMaxSearches.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkProfileEntryMaxSearches.setStatus(_A)
class _CienaCesBenchmarkProfileEntryMaxSamples_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,20))
_CienaCesBenchmarkProfileEntryMaxSamples_Type.__name__=_E
_CienaCesBenchmarkProfileEntryMaxSamples_Object=MibTableColumn
cienaCesBenchmarkProfileEntryMaxSamples=_CienaCesBenchmarkProfileEntryMaxSamples_Object((1,3,6,1,4,1,1271,2,1,39,1,1,11,1,9),_CienaCesBenchmarkProfileEntryMaxSamples_Type())
cienaCesBenchmarkProfileEntryMaxSamples.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkProfileEntryMaxSamples.setStatus(_A)
class _CienaCesBenchmarkProfileEntrySamplingInterval_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,600))
_CienaCesBenchmarkProfileEntrySamplingInterval_Type.__name__=_E
_CienaCesBenchmarkProfileEntrySamplingInterval_Object=MibTableColumn
cienaCesBenchmarkProfileEntrySamplingInterval=_CienaCesBenchmarkProfileEntrySamplingInterval_Object((1,3,6,1,4,1,1271,2,1,39,1,1,11,1,10),_CienaCesBenchmarkProfileEntrySamplingInterval_Type())
cienaCesBenchmarkProfileEntrySamplingInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkProfileEntrySamplingInterval.setStatus(_A)
class _CienaCesBenchmarkProfileEntryFrameLossStartBw_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('profileBandwidth',1),('maximumThroughput',2),('maximumLineRate',3)))
_CienaCesBenchmarkProfileEntryFrameLossStartBw_Type.__name__=_E
_CienaCesBenchmarkProfileEntryFrameLossStartBw_Object=MibTableColumn
cienaCesBenchmarkProfileEntryFrameLossStartBw=_CienaCesBenchmarkProfileEntryFrameLossStartBw_Object((1,3,6,1,4,1,1271,2,1,39,1,1,11,1,11),_CienaCesBenchmarkProfileEntryFrameLossStartBw_Type())
cienaCesBenchmarkProfileEntryFrameLossStartBw.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkProfileEntryFrameLossStartBw.setStatus(_A)
class _CienaCesBenchmarkProfileEntryVidValidation_Type(TruthValue):defaultValue=1
_CienaCesBenchmarkProfileEntryVidValidation_Type.__name__=_K
_CienaCesBenchmarkProfileEntryVidValidation_Object=MibTableColumn
cienaCesBenchmarkProfileEntryVidValidation=_CienaCesBenchmarkProfileEntryVidValidation_Object((1,3,6,1,4,1,1271,2,1,39,1,1,11,1,12),_CienaCesBenchmarkProfileEntryVidValidation_Type())
cienaCesBenchmarkProfileEntryVidValidation.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkProfileEntryVidValidation.setStatus(_A)
class _CienaCesBenchmarkProfileEntryPcpValidation_Type(TruthValue):defaultValue=1
_CienaCesBenchmarkProfileEntryPcpValidation_Type.__name__=_K
_CienaCesBenchmarkProfileEntryPcpValidation_Object=MibTableColumn
cienaCesBenchmarkProfileEntryPcpValidation=_CienaCesBenchmarkProfileEntryPcpValidation_Object((1,3,6,1,4,1,1271,2,1,39,1,1,11,1,13),_CienaCesBenchmarkProfileEntryPcpValidation_Type())
cienaCesBenchmarkProfileEntryPcpValidation.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkProfileEntryPcpValidation.setStatus(_A)
class _CienaCesBenchmarkProfileEntryColorValidation_Type(TruthValue):defaultValue=1
_CienaCesBenchmarkProfileEntryColorValidation_Type.__name__=_K
_CienaCesBenchmarkProfileEntryColorValidation_Object=MibTableColumn
cienaCesBenchmarkProfileEntryColorValidation=_CienaCesBenchmarkProfileEntryColorValidation_Object((1,3,6,1,4,1,1271,2,1,39,1,1,11,1,14),_CienaCesBenchmarkProfileEntryColorValidation_Type())
cienaCesBenchmarkProfileEntryColorValidation.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkProfileEntryColorValidation.setStatus(_A)
class _CienaCesBenchmarkProfileEntryKpiProfileId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_CienaCesBenchmarkProfileEntryKpiProfileId_Type.__name__=_E
_CienaCesBenchmarkProfileEntryKpiProfileId_Object=MibTableColumn
cienaCesBenchmarkProfileEntryKpiProfileId=_CienaCesBenchmarkProfileEntryKpiProfileId_Object((1,3,6,1,4,1,1271,2,1,39,1,1,11,1,15),_CienaCesBenchmarkProfileEntryKpiProfileId_Type())
cienaCesBenchmarkProfileEntryKpiProfileId.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkProfileEntryKpiProfileId.setStatus(_A)
class _CienaCesBenchmarkProfileEntryBwAllocProfileId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_CienaCesBenchmarkProfileEntryBwAllocProfileId_Type.__name__=_E
_CienaCesBenchmarkProfileEntryBwAllocProfileId_Object=MibTableColumn
cienaCesBenchmarkProfileEntryBwAllocProfileId=_CienaCesBenchmarkProfileEntryBwAllocProfileId_Object((1,3,6,1,4,1,1271,2,1,39,1,1,11,1,16),_CienaCesBenchmarkProfileEntryBwAllocProfileId_Type())
cienaCesBenchmarkProfileEntryBwAllocProfileId.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkProfileEntryBwAllocProfileId.setStatus(_A)
class _CienaCesBenchmarkProfileEntryEmixSequenceId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_CienaCesBenchmarkProfileEntryEmixSequenceId_Type.__name__=_E
_CienaCesBenchmarkProfileEntryEmixSequenceId_Object=MibTableColumn
cienaCesBenchmarkProfileEntryEmixSequenceId=_CienaCesBenchmarkProfileEntryEmixSequenceId_Object((1,3,6,1,4,1,1271,2,1,39,1,1,11,1,17),_CienaCesBenchmarkProfileEntryEmixSequenceId_Type())
cienaCesBenchmarkProfileEntryEmixSequenceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkProfileEntryEmixSequenceId.setStatus(_A)
class _CienaCesBenchmarkProfileEntryEncapType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('untagged',1),('dot1q',2),('qinq',3)))
_CienaCesBenchmarkProfileEntryEncapType_Type.__name__=_E
_CienaCesBenchmarkProfileEntryEncapType_Object=MibTableColumn
cienaCesBenchmarkProfileEntryEncapType=_CienaCesBenchmarkProfileEntryEncapType_Object((1,3,6,1,4,1,1271,2,1,39,1,1,11,1,18),_CienaCesBenchmarkProfileEntryEncapType_Type())
cienaCesBenchmarkProfileEntryEncapType.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkProfileEntryEncapType.setStatus(_A)
class _CienaCesBenchmarkProfileEntryPduType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ethernet',1),('ip',2),('udpecho',3)))
_CienaCesBenchmarkProfileEntryPduType_Type.__name__=_E
_CienaCesBenchmarkProfileEntryPduType_Object=MibTableColumn
cienaCesBenchmarkProfileEntryPduType=_CienaCesBenchmarkProfileEntryPduType_Object((1,3,6,1,4,1,1271,2,1,39,1,1,11,1,19),_CienaCesBenchmarkProfileEntryPduType_Type())
cienaCesBenchmarkProfileEntryPduType.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkProfileEntryPduType.setStatus(_A)
_CienaCesBenchmarkProfileEntryDstmac_Type=MacAddress
_CienaCesBenchmarkProfileEntryDstmac_Object=MibTableColumn
cienaCesBenchmarkProfileEntryDstmac=_CienaCesBenchmarkProfileEntryDstmac_Object((1,3,6,1,4,1,1271,2,1,39,1,1,11,1,20),_CienaCesBenchmarkProfileEntryDstmac_Type())
cienaCesBenchmarkProfileEntryDstmac.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkProfileEntryDstmac.setStatus(_A)
class _CienaCesBenchmarkProfileEntrySVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_CienaCesBenchmarkProfileEntrySVid_Type.__name__=_E
_CienaCesBenchmarkProfileEntrySVid_Object=MibTableColumn
cienaCesBenchmarkProfileEntrySVid=_CienaCesBenchmarkProfileEntrySVid_Object((1,3,6,1,4,1,1271,2,1,39,1,1,11,1,21),_CienaCesBenchmarkProfileEntrySVid_Type())
cienaCesBenchmarkProfileEntrySVid.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkProfileEntrySVid.setStatus(_A)
_CienaCesBenchmarkProfileEntrySPcp_Type=CienaCesBenchmarkPcpBitmap
_CienaCesBenchmarkProfileEntrySPcp_Object=MibTableColumn
cienaCesBenchmarkProfileEntrySPcp=_CienaCesBenchmarkProfileEntrySPcp_Object((1,3,6,1,4,1,1271,2,1,39,1,1,11,1,22),_CienaCesBenchmarkProfileEntrySPcp_Type())
cienaCesBenchmarkProfileEntrySPcp.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkProfileEntrySPcp.setStatus(_A)
_CienaCesBenchmarkProfileEntrySColor_Type=CienaCesBenchmarkColorTest
_CienaCesBenchmarkProfileEntrySColor_Object=MibTableColumn
cienaCesBenchmarkProfileEntrySColor=_CienaCesBenchmarkProfileEntrySColor_Object((1,3,6,1,4,1,1271,2,1,39,1,1,11,1,23),_CienaCesBenchmarkProfileEntrySColor_Type())
cienaCesBenchmarkProfileEntrySColor.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkProfileEntrySColor.setStatus(_A)
class _CienaCesBenchmarkProfileEntryCVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_CienaCesBenchmarkProfileEntryCVid_Type.__name__=_E
_CienaCesBenchmarkProfileEntryCVid_Object=MibTableColumn
cienaCesBenchmarkProfileEntryCVid=_CienaCesBenchmarkProfileEntryCVid_Object((1,3,6,1,4,1,1271,2,1,39,1,1,11,1,24),_CienaCesBenchmarkProfileEntryCVid_Type())
cienaCesBenchmarkProfileEntryCVid.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkProfileEntryCVid.setStatus(_A)
_CienaCesBenchmarkProfileEntryCPcp_Type=CienaCesBenchmarkPcpBitmap
_CienaCesBenchmarkProfileEntryCPcp_Object=MibTableColumn
cienaCesBenchmarkProfileEntryCPcp=_CienaCesBenchmarkProfileEntryCPcp_Object((1,3,6,1,4,1,1271,2,1,39,1,1,11,1,25),_CienaCesBenchmarkProfileEntryCPcp_Type())
cienaCesBenchmarkProfileEntryCPcp.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkProfileEntryCPcp.setStatus(_A)
_CienaCesBenchmarkProfileEntryCColor_Type=CienaCesBenchmarkColorTest
_CienaCesBenchmarkProfileEntryCColor_Object=MibTableColumn
cienaCesBenchmarkProfileEntryCColor=_CienaCesBenchmarkProfileEntryCColor_Object((1,3,6,1,4,1,1271,2,1,39,1,1,11,1,26),_CienaCesBenchmarkProfileEntryCColor_Type())
cienaCesBenchmarkProfileEntryCColor.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkProfileEntryCColor.setStatus(_A)
class _CienaCesBenchmarkProfileEntryTpid_Type(Integer32):defaultValue=33024;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CienaCesBenchmarkProfileEntryTpid_Type.__name__=_E
_CienaCesBenchmarkProfileEntryTpid_Object=MibTableColumn
cienaCesBenchmarkProfileEntryTpid=_CienaCesBenchmarkProfileEntryTpid_Object((1,3,6,1,4,1,1271,2,1,39,1,1,11,1,27),_CienaCesBenchmarkProfileEntryTpid_Type())
cienaCesBenchmarkProfileEntryTpid.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkProfileEntryTpid.setStatus(_A)
class _CienaCesBenchmarkProfileEntryDscp_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_CienaCesBenchmarkProfileEntryDscp_Type.__name__=_E
_CienaCesBenchmarkProfileEntryDscp_Object=MibTableColumn
cienaCesBenchmarkProfileEntryDscp=_CienaCesBenchmarkProfileEntryDscp_Object((1,3,6,1,4,1,1271,2,1,39,1,1,11,1,28),_CienaCesBenchmarkProfileEntryDscp_Type())
cienaCesBenchmarkProfileEntryDscp.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkProfileEntryDscp.setStatus(_A)
_CienaCesBenchmarkProfileEntrySrcInetAddrType_Type=InetAddressType
_CienaCesBenchmarkProfileEntrySrcInetAddrType_Object=MibTableColumn
cienaCesBenchmarkProfileEntrySrcInetAddrType=_CienaCesBenchmarkProfileEntrySrcInetAddrType_Object((1,3,6,1,4,1,1271,2,1,39,1,1,11,1,29),_CienaCesBenchmarkProfileEntrySrcInetAddrType_Type())
cienaCesBenchmarkProfileEntrySrcInetAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkProfileEntrySrcInetAddrType.setStatus(_A)
_CienaCesBenchmarkProfileEntrySrcInetAddr_Type=InetAddress
_CienaCesBenchmarkProfileEntrySrcInetAddr_Object=MibTableColumn
cienaCesBenchmarkProfileEntrySrcInetAddr=_CienaCesBenchmarkProfileEntrySrcInetAddr_Object((1,3,6,1,4,1,1271,2,1,39,1,1,11,1,30),_CienaCesBenchmarkProfileEntrySrcInetAddr_Type())
cienaCesBenchmarkProfileEntrySrcInetAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkProfileEntrySrcInetAddr.setStatus(_A)
_CienaCesBenchmarkProfileEntryDstInetAddrType_Type=InetAddressType
_CienaCesBenchmarkProfileEntryDstInetAddrType_Object=MibTableColumn
cienaCesBenchmarkProfileEntryDstInetAddrType=_CienaCesBenchmarkProfileEntryDstInetAddrType_Object((1,3,6,1,4,1,1271,2,1,39,1,1,11,1,31),_CienaCesBenchmarkProfileEntryDstInetAddrType_Type())
cienaCesBenchmarkProfileEntryDstInetAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkProfileEntryDstInetAddrType.setStatus(_A)
_CienaCesBenchmarkProfileEntryDstInetAddr_Type=InetAddress
_CienaCesBenchmarkProfileEntryDstInetAddr_Object=MibTableColumn
cienaCesBenchmarkProfileEntryDstInetAddr=_CienaCesBenchmarkProfileEntryDstInetAddr_Object((1,3,6,1,4,1,1271,2,1,39,1,1,11,1,32),_CienaCesBenchmarkProfileEntryDstInetAddr_Type())
cienaCesBenchmarkProfileEntryDstInetAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkProfileEntryDstInetAddr.setStatus(_A)
class _CienaCesBenchmarkProfileEntryCustomPayload_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_CienaCesBenchmarkProfileEntryCustomPayload_Type.__name__=_c
_CienaCesBenchmarkProfileEntryCustomPayload_Object=MibTableColumn
cienaCesBenchmarkProfileEntryCustomPayload=_CienaCesBenchmarkProfileEntryCustomPayload_Object((1,3,6,1,4,1,1271,2,1,39,1,1,11,1,33),_CienaCesBenchmarkProfileEntryCustomPayload_Type())
cienaCesBenchmarkProfileEntryCustomPayload.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkProfileEntryCustomPayload.setStatus(_A)
class _CienaCesBenchmarkProfileEntryThroughputTest_Type(TruthValue):defaultValue=2
_CienaCesBenchmarkProfileEntryThroughputTest_Type.__name__=_K
_CienaCesBenchmarkProfileEntryThroughputTest_Object=MibTableColumn
cienaCesBenchmarkProfileEntryThroughputTest=_CienaCesBenchmarkProfileEntryThroughputTest_Object((1,3,6,1,4,1,1271,2,1,39,1,1,11,1,34),_CienaCesBenchmarkProfileEntryThroughputTest_Type())
cienaCesBenchmarkProfileEntryThroughputTest.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkProfileEntryThroughputTest.setStatus(_A)
class _CienaCesBenchmarkProfileEntryFramelossTest_Type(TruthValue):defaultValue=2
_CienaCesBenchmarkProfileEntryFramelossTest_Type.__name__=_K
_CienaCesBenchmarkProfileEntryFramelossTest_Object=MibTableColumn
cienaCesBenchmarkProfileEntryFramelossTest=_CienaCesBenchmarkProfileEntryFramelossTest_Object((1,3,6,1,4,1,1271,2,1,39,1,1,11,1,35),_CienaCesBenchmarkProfileEntryFramelossTest_Type())
cienaCesBenchmarkProfileEntryFramelossTest.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkProfileEntryFramelossTest.setStatus(_A)
class _CienaCesBenchmarkProfileEntryLatencyTest_Type(TruthValue):defaultValue=2
_CienaCesBenchmarkProfileEntryLatencyTest_Type.__name__=_K
_CienaCesBenchmarkProfileEntryLatencyTest_Object=MibTableColumn
cienaCesBenchmarkProfileEntryLatencyTest=_CienaCesBenchmarkProfileEntryLatencyTest_Object((1,3,6,1,4,1,1271,2,1,39,1,1,11,1,36),_CienaCesBenchmarkProfileEntryLatencyTest_Type())
cienaCesBenchmarkProfileEntryLatencyTest.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkProfileEntryLatencyTest.setStatus(_A)
class _CienaCesBenchmarkProfileEntryPdvTest_Type(TruthValue):defaultValue=2
_CienaCesBenchmarkProfileEntryPdvTest_Type.__name__=_K
_CienaCesBenchmarkProfileEntryPdvTest_Object=MibTableColumn
cienaCesBenchmarkProfileEntryPdvTest=_CienaCesBenchmarkProfileEntryPdvTest_Object((1,3,6,1,4,1,1271,2,1,39,1,1,11,1,37),_CienaCesBenchmarkProfileEntryPdvTest_Type())
cienaCesBenchmarkProfileEntryPdvTest.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkProfileEntryPdvTest.setStatus(_A)
_CienaCesBenchmarkProfileEntryBurstTest_Type=TruthValue
_CienaCesBenchmarkProfileEntryBurstTest_Object=MibTableColumn
cienaCesBenchmarkProfileEntryBurstTest=_CienaCesBenchmarkProfileEntryBurstTest_Object((1,3,6,1,4,1,1271,2,1,39,1,1,11,1,38),_CienaCesBenchmarkProfileEntryBurstTest_Type())
cienaCesBenchmarkProfileEntryBurstTest.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkProfileEntryBurstTest.setStatus(_A)
class _CienaCesBenchmarkProfileEntryRfc2544Suite_Type(TruthValue):defaultValue=2
_CienaCesBenchmarkProfileEntryRfc2544Suite_Type.__name__=_K
_CienaCesBenchmarkProfileEntryRfc2544Suite_Object=MibTableColumn
cienaCesBenchmarkProfileEntryRfc2544Suite=_CienaCesBenchmarkProfileEntryRfc2544Suite_Object((1,3,6,1,4,1,1271,2,1,39,1,1,11,1,39),_CienaCesBenchmarkProfileEntryRfc2544Suite_Type())
cienaCesBenchmarkProfileEntryRfc2544Suite.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkProfileEntryRfc2544Suite.setStatus(_A)
class _CienaCesBenchmarkProfileEntryY1564Test_Type(TruthValue):defaultValue=2
_CienaCesBenchmarkProfileEntryY1564Test_Type.__name__=_K
_CienaCesBenchmarkProfileEntryY1564Test_Object=MibTableColumn
cienaCesBenchmarkProfileEntryY1564Test=_CienaCesBenchmarkProfileEntryY1564Test_Object((1,3,6,1,4,1,1271,2,1,39,1,1,11,1,40),_CienaCesBenchmarkProfileEntryY1564Test_Type())
cienaCesBenchmarkProfileEntryY1564Test.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkProfileEntryY1564Test.setStatus(_A)
_CienaCesBenchmarkProfileEntryHwSessionsRequired_Type=Integer32
_CienaCesBenchmarkProfileEntryHwSessionsRequired_Object=MibTableColumn
cienaCesBenchmarkProfileEntryHwSessionsRequired=_CienaCesBenchmarkProfileEntryHwSessionsRequired_Object((1,3,6,1,4,1,1271,2,1,39,1,1,11,1,41),_CienaCesBenchmarkProfileEntryHwSessionsRequired_Type())
cienaCesBenchmarkProfileEntryHwSessionsRequired.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkProfileEntryHwSessionsRequired.setStatus(_A)
_CienaCesBenchmarkProfileEntryNumOfRef_Type=Integer32
_CienaCesBenchmarkProfileEntryNumOfRef_Object=MibTableColumn
cienaCesBenchmarkProfileEntryNumOfRef=_CienaCesBenchmarkProfileEntryNumOfRef_Object((1,3,6,1,4,1,1271,2,1,39,1,1,11,1,42),_CienaCesBenchmarkProfileEntryNumOfRef_Type())
cienaCesBenchmarkProfileEntryNumOfRef.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkProfileEntryNumOfRef.setStatus(_A)
_CienaCesBenchmarkProfileEntryRowStatus_Type=RowStatus
_CienaCesBenchmarkProfileEntryRowStatus_Object=MibTableColumn
cienaCesBenchmarkProfileEntryRowStatus=_CienaCesBenchmarkProfileEntryRowStatus_Object((1,3,6,1,4,1,1271,2,1,39,1,1,11,1,43),_CienaCesBenchmarkProfileEntryRowStatus_Type())
cienaCesBenchmarkProfileEntryRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkProfileEntryRowStatus.setStatus(_A)
_CienaCesBenchmarkTestInstanceTable_Object=MibTable
cienaCesBenchmarkTestInstanceTable=_CienaCesBenchmarkTestInstanceTable_Object((1,3,6,1,4,1,1271,2,1,39,1,1,12))
if mibBuilder.loadTexts:cienaCesBenchmarkTestInstanceTable.setStatus(_A)
_CienaCesBenchmarkTestInstanceEntry_Object=MibTableRow
cienaCesBenchmarkTestInstanceEntry=_CienaCesBenchmarkTestInstanceEntry_Object((1,3,6,1,4,1,1271,2,1,39,1,1,12,1))
cienaCesBenchmarkTestInstanceEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:cienaCesBenchmarkTestInstanceEntry.setStatus(_A)
_CienaCesBenchmarkTestInstanceEntryId_Type=Integer32
_CienaCesBenchmarkTestInstanceEntryId_Object=MibTableColumn
cienaCesBenchmarkTestInstanceEntryId=_CienaCesBenchmarkTestInstanceEntryId_Object((1,3,6,1,4,1,1271,2,1,39,1,1,12,1,1),_CienaCesBenchmarkTestInstanceEntryId_Type())
cienaCesBenchmarkTestInstanceEntryId.setMaxAccess(_F)
if mibBuilder.loadTexts:cienaCesBenchmarkTestInstanceEntryId.setStatus(_A)
class _CienaCesBenchmarkTestInstanceEntryName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,46))
_CienaCesBenchmarkTestInstanceEntryName_Type.__name__=_I
_CienaCesBenchmarkTestInstanceEntryName_Object=MibTableColumn
cienaCesBenchmarkTestInstanceEntryName=_CienaCesBenchmarkTestInstanceEntryName_Object((1,3,6,1,4,1,1271,2,1,39,1,1,12,1,2),_CienaCesBenchmarkTestInstanceEntryName_Type())
cienaCesBenchmarkTestInstanceEntryName.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkTestInstanceEntryName.setStatus(_A)
_CienaCesBenchmarkTestInstanceEntrySubPortId_Type=Integer32
_CienaCesBenchmarkTestInstanceEntrySubPortId_Object=MibTableColumn
cienaCesBenchmarkTestInstanceEntrySubPortId=_CienaCesBenchmarkTestInstanceEntrySubPortId_Object((1,3,6,1,4,1,1271,2,1,39,1,1,12,1,3),_CienaCesBenchmarkTestInstanceEntrySubPortId_Type())
cienaCesBenchmarkTestInstanceEntrySubPortId.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkTestInstanceEntrySubPortId.setStatus(_A)
_CienaCesBenchmarkTestInstanceEntryProfileId_Type=Integer32
_CienaCesBenchmarkTestInstanceEntryProfileId_Object=MibTableColumn
cienaCesBenchmarkTestInstanceEntryProfileId=_CienaCesBenchmarkTestInstanceEntryProfileId_Object((1,3,6,1,4,1,1271,2,1,39,1,1,12,1,4),_CienaCesBenchmarkTestInstanceEntryProfileId_Type())
cienaCesBenchmarkTestInstanceEntryProfileId.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkTestInstanceEntryProfileId.setStatus(_A)
_CienaCesBenchmarkTestInstanceEntrySvid_Type=Integer32
_CienaCesBenchmarkTestInstanceEntrySvid_Object=MibTableColumn
cienaCesBenchmarkTestInstanceEntrySvid=_CienaCesBenchmarkTestInstanceEntrySvid_Object((1,3,6,1,4,1,1271,2,1,39,1,1,12,1,5),_CienaCesBenchmarkTestInstanceEntrySvid_Type())
cienaCesBenchmarkTestInstanceEntrySvid.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkTestInstanceEntrySvid.setStatus(_A)
_CienaCesBenchmarkTestInstanceEntryCvid_Type=Integer32
_CienaCesBenchmarkTestInstanceEntryCvid_Object=MibTableColumn
cienaCesBenchmarkTestInstanceEntryCvid=_CienaCesBenchmarkTestInstanceEntryCvid_Object((1,3,6,1,4,1,1271,2,1,39,1,1,12,1,6),_CienaCesBenchmarkTestInstanceEntryCvid_Type())
cienaCesBenchmarkTestInstanceEntryCvid.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkTestInstanceEntryCvid.setStatus(_A)
_CienaCesBenchmarkTestInstanceEntryUntagged_Type=TruthValue
_CienaCesBenchmarkTestInstanceEntryUntagged_Object=MibTableColumn
cienaCesBenchmarkTestInstanceEntryUntagged=_CienaCesBenchmarkTestInstanceEntryUntagged_Object((1,3,6,1,4,1,1271,2,1,39,1,1,12,1,7),_CienaCesBenchmarkTestInstanceEntryUntagged_Type())
cienaCesBenchmarkTestInstanceEntryUntagged.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkTestInstanceEntryUntagged.setStatus(_A)
_CienaCesBenchmarkTestInstanceEntryDstMac_Type=MacAddress
_CienaCesBenchmarkTestInstanceEntryDstMac_Object=MibTableColumn
cienaCesBenchmarkTestInstanceEntryDstMac=_CienaCesBenchmarkTestInstanceEntryDstMac_Object((1,3,6,1,4,1,1271,2,1,39,1,1,12,1,8),_CienaCesBenchmarkTestInstanceEntryDstMac_Type())
cienaCesBenchmarkTestInstanceEntryDstMac.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkTestInstanceEntryDstMac.setStatus(_A)
_CienaCesBenchmarkTestInstanceEntryAdminState_Type=CienaCesBenchmarkAdminState
_CienaCesBenchmarkTestInstanceEntryAdminState_Object=MibTableColumn
cienaCesBenchmarkTestInstanceEntryAdminState=_CienaCesBenchmarkTestInstanceEntryAdminState_Object((1,3,6,1,4,1,1271,2,1,39,1,1,12,1,9),_CienaCesBenchmarkTestInstanceEntryAdminState_Type())
cienaCesBenchmarkTestInstanceEntryAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkTestInstanceEntryAdminState.setStatus(_A)
_CienaCesBenchmarkTestInstanceEntryStarted_Type=TruthValue
_CienaCesBenchmarkTestInstanceEntryStarted_Object=MibTableColumn
cienaCesBenchmarkTestInstanceEntryStarted=_CienaCesBenchmarkTestInstanceEntryStarted_Object((1,3,6,1,4,1,1271,2,1,39,1,1,12,1,10),_CienaCesBenchmarkTestInstanceEntryStarted_Type())
cienaCesBenchmarkTestInstanceEntryStarted.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkTestInstanceEntryStarted.setStatus(_A)
_CienaCesBenchmarkTestInstanceEntryCurrentInterval_Type=Integer32
_CienaCesBenchmarkTestInstanceEntryCurrentInterval_Object=MibTableColumn
cienaCesBenchmarkTestInstanceEntryCurrentInterval=_CienaCesBenchmarkTestInstanceEntryCurrentInterval_Object((1,3,6,1,4,1,1271,2,1,39,1,1,12,1,11),_CienaCesBenchmarkTestInstanceEntryCurrentInterval_Type())
cienaCesBenchmarkTestInstanceEntryCurrentInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkTestInstanceEntryCurrentInterval.setStatus(_A)
_CienaCesBenchmarkTestInstanceEntryTotalIntervals_Type=Integer32
_CienaCesBenchmarkTestInstanceEntryTotalIntervals_Object=MibTableColumn
cienaCesBenchmarkTestInstanceEntryTotalIntervals=_CienaCesBenchmarkTestInstanceEntryTotalIntervals_Object((1,3,6,1,4,1,1271,2,1,39,1,1,12,1,12),_CienaCesBenchmarkTestInstanceEntryTotalIntervals_Type())
cienaCesBenchmarkTestInstanceEntryTotalIntervals.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkTestInstanceEntryTotalIntervals.setStatus(_A)
_CienaCesBenchmarkTestInstanceEntryLastIterStart_Type=DateAndTime
_CienaCesBenchmarkTestInstanceEntryLastIterStart_Object=MibTableColumn
cienaCesBenchmarkTestInstanceEntryLastIterStart=_CienaCesBenchmarkTestInstanceEntryLastIterStart_Object((1,3,6,1,4,1,1271,2,1,39,1,1,12,1,13),_CienaCesBenchmarkTestInstanceEntryLastIterStart_Type())
cienaCesBenchmarkTestInstanceEntryLastIterStart.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkTestInstanceEntryLastIterStart.setStatus(_A)
_CienaCesBenchmarkTestInstanceEntryClearStats_Type=TruthValue
_CienaCesBenchmarkTestInstanceEntryClearStats_Object=MibTableColumn
cienaCesBenchmarkTestInstanceEntryClearStats=_CienaCesBenchmarkTestInstanceEntryClearStats_Object((1,3,6,1,4,1,1271,2,1,39,1,1,12,1,14),_CienaCesBenchmarkTestInstanceEntryClearStats_Type())
cienaCesBenchmarkTestInstanceEntryClearStats.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkTestInstanceEntryClearStats.setStatus(_A)
_CienaCesBenchmarkTestInstanceEntryRowStatus_Type=RowStatus
_CienaCesBenchmarkTestInstanceEntryRowStatus_Object=MibTableColumn
cienaCesBenchmarkTestInstanceEntryRowStatus=_CienaCesBenchmarkTestInstanceEntryRowStatus_Object((1,3,6,1,4,1,1271,2,1,39,1,1,12,1,15),_CienaCesBenchmarkTestInstanceEntryRowStatus_Type())
cienaCesBenchmarkTestInstanceEntryRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkTestInstanceEntryRowStatus.setStatus(_A)
_CienaCesBenchmarkTestInstanceEntryAssocEntityId_Type=Integer32
_CienaCesBenchmarkTestInstanceEntryAssocEntityId_Object=MibTableColumn
cienaCesBenchmarkTestInstanceEntryAssocEntityId=_CienaCesBenchmarkTestInstanceEntryAssocEntityId_Object((1,3,6,1,4,1,1271,2,1,39,1,1,12,1,16),_CienaCesBenchmarkTestInstanceEntryAssocEntityId_Type())
cienaCesBenchmarkTestInstanceEntryAssocEntityId.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkTestInstanceEntryAssocEntityId.setStatus(_A)
_CienaCesBenchmarkTestInstanceEntryOperState_Type=TruthValue
_CienaCesBenchmarkTestInstanceEntryOperState_Object=MibTableColumn
cienaCesBenchmarkTestInstanceEntryOperState=_CienaCesBenchmarkTestInstanceEntryOperState_Object((1,3,6,1,4,1,1271,2,1,39,1,1,12,1,17),_CienaCesBenchmarkTestInstanceEntryOperState_Type())
cienaCesBenchmarkTestInstanceEntryOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkTestInstanceEntryOperState.setStatus(_A)
_CienaCesBenchmarkTestInstanceEntryConnectivityTest_Type=TruthValue
_CienaCesBenchmarkTestInstanceEntryConnectivityTest_Object=MibTableColumn
cienaCesBenchmarkTestInstanceEntryConnectivityTest=_CienaCesBenchmarkTestInstanceEntryConnectivityTest_Object((1,3,6,1,4,1,1271,2,1,39,1,1,12,1,18),_CienaCesBenchmarkTestInstanceEntryConnectivityTest_Type())
cienaCesBenchmarkTestInstanceEntryConnectivityTest.setMaxAccess(_D)
if mibBuilder.loadTexts:cienaCesBenchmarkTestInstanceEntryConnectivityTest.setStatus(_A)
_CienaCesBenchmarkGenTestSessionAllocationTable_Object=MibTable
cienaCesBenchmarkGenTestSessionAllocationTable=_CienaCesBenchmarkGenTestSessionAllocationTable_Object((1,3,6,1,4,1,1271,2,1,39,1,1,13))
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionAllocationTable.setStatus(_A)
_CienaCesBenchmarkGenTestSessionAllocationEntry_Object=MibTableRow
cienaCesBenchmarkGenTestSessionAllocationEntry=_CienaCesBenchmarkGenTestSessionAllocationEntry_Object((1,3,6,1,4,1,1271,2,1,39,1,1,13,1))
cienaCesBenchmarkGenTestSessionAllocationEntry.setIndexNames((0,_C,_J),(0,_C,_H),(0,_C,_n),(0,_C,_o))
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionAllocationEntry.setStatus(_A)
class _CienaCesBenchmarkGenTestSessionPcpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_CienaCesBenchmarkGenTestSessionPcpIndex_Type.__name__=_E
_CienaCesBenchmarkGenTestSessionPcpIndex_Object=MibTableColumn
cienaCesBenchmarkGenTestSessionPcpIndex=_CienaCesBenchmarkGenTestSessionPcpIndex_Object((1,3,6,1,4,1,1271,2,1,39,1,1,13,1,1),_CienaCesBenchmarkGenTestSessionPcpIndex_Type())
cienaCesBenchmarkGenTestSessionPcpIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionPcpIndex.setStatus(_A)
class _CienaCesBenchmarkGenTestSessionColorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_CienaCesBenchmarkGenTestSessionColorIndex_Type.__name__=_E
_CienaCesBenchmarkGenTestSessionColorIndex_Object=MibTableColumn
cienaCesBenchmarkGenTestSessionColorIndex=_CienaCesBenchmarkGenTestSessionColorIndex_Object((1,3,6,1,4,1,1271,2,1,39,1,1,13,1,2),_CienaCesBenchmarkGenTestSessionColorIndex_Type())
cienaCesBenchmarkGenTestSessionColorIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionColorIndex.setStatus(_A)
class _CienaCesBenchmarkGenTestSessionPcp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_CienaCesBenchmarkGenTestSessionPcp_Type.__name__=_E
_CienaCesBenchmarkGenTestSessionPcp_Object=MibTableColumn
cienaCesBenchmarkGenTestSessionPcp=_CienaCesBenchmarkGenTestSessionPcp_Object((1,3,6,1,4,1,1271,2,1,39,1,1,13,1,3),_CienaCesBenchmarkGenTestSessionPcp_Type())
cienaCesBenchmarkGenTestSessionPcp.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionPcp.setStatus(_A)
_CienaCesBenchmarkGenTestSessionColor_Type=CienaCesBenchmarkColorTest
_CienaCesBenchmarkGenTestSessionColor_Object=MibTableColumn
cienaCesBenchmarkGenTestSessionColor=_CienaCesBenchmarkGenTestSessionColor_Object((1,3,6,1,4,1,1271,2,1,39,1,1,13,1,4),_CienaCesBenchmarkGenTestSessionColor_Type())
cienaCesBenchmarkGenTestSessionColor.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionColor.setStatus(_A)
class _CienaCesBenchmarkGenTestSessionId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_CienaCesBenchmarkGenTestSessionId_Type.__name__=_E
_CienaCesBenchmarkGenTestSessionId_Object=MibTableColumn
cienaCesBenchmarkGenTestSessionId=_CienaCesBenchmarkGenTestSessionId_Object((1,3,6,1,4,1,1271,2,1,39,1,1,13,1,5),_CienaCesBenchmarkGenTestSessionId_Type())
cienaCesBenchmarkGenTestSessionId.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionId.setStatus(_A)
_CienaCesBenchmarkGenTestSessionEmixSequenceId_Type=Integer32
_CienaCesBenchmarkGenTestSessionEmixSequenceId_Object=MibTableColumn
cienaCesBenchmarkGenTestSessionEmixSequenceId=_CienaCesBenchmarkGenTestSessionEmixSequenceId_Object((1,3,6,1,4,1,1271,2,1,39,1,1,13,1,6),_CienaCesBenchmarkGenTestSessionEmixSequenceId_Type())
cienaCesBenchmarkGenTestSessionEmixSequenceId.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionEmixSequenceId.setStatus(_A)
_CienaCesBenchmarkGenTestSessionCurrentPktSize_Type=Integer32
_CienaCesBenchmarkGenTestSessionCurrentPktSize_Object=MibTableColumn
cienaCesBenchmarkGenTestSessionCurrentPktSize=_CienaCesBenchmarkGenTestSessionCurrentPktSize_Object((1,3,6,1,4,1,1271,2,1,39,1,1,13,1,7),_CienaCesBenchmarkGenTestSessionCurrentPktSize_Type())
cienaCesBenchmarkGenTestSessionCurrentPktSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionCurrentPktSize.setStatus(_A)
_CienaCesBenchmarkGenTestSessionThroughputTestState_Type=CienaCesBenchmarkThroughputTestState
_CienaCesBenchmarkGenTestSessionThroughputTestState_Object=MibTableColumn
cienaCesBenchmarkGenTestSessionThroughputTestState=_CienaCesBenchmarkGenTestSessionThroughputTestState_Object((1,3,6,1,4,1,1271,2,1,39,1,1,13,1,8),_CienaCesBenchmarkGenTestSessionThroughputTestState_Type())
cienaCesBenchmarkGenTestSessionThroughputTestState.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionThroughputTestState.setStatus(_A)
_CienaCesBenchmarkGenTestSessionFramelossTestState_Type=CienaCesBenchmarkFramelossTestState
_CienaCesBenchmarkGenTestSessionFramelossTestState_Object=MibTableColumn
cienaCesBenchmarkGenTestSessionFramelossTestState=_CienaCesBenchmarkGenTestSessionFramelossTestState_Object((1,3,6,1,4,1,1271,2,1,39,1,1,13,1,9),_CienaCesBenchmarkGenTestSessionFramelossTestState_Type())
cienaCesBenchmarkGenTestSessionFramelossTestState.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionFramelossTestState.setStatus(_A)
_CienaCesBenchmarkGenTestSessionLatencyTestState_Type=CienaCesBenchmarkLatencyPdvTestState
_CienaCesBenchmarkGenTestSessionLatencyTestState_Object=MibTableColumn
cienaCesBenchmarkGenTestSessionLatencyTestState=_CienaCesBenchmarkGenTestSessionLatencyTestState_Object((1,3,6,1,4,1,1271,2,1,39,1,1,13,1,10),_CienaCesBenchmarkGenTestSessionLatencyTestState_Type())
cienaCesBenchmarkGenTestSessionLatencyTestState.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionLatencyTestState.setStatus(_A)
_CienaCesBenchmarkGenTestSessionPdvTestState_Type=CienaCesBenchmarkLatencyPdvTestState
_CienaCesBenchmarkGenTestSessionPdvTestState_Object=MibTableColumn
cienaCesBenchmarkGenTestSessionPdvTestState=_CienaCesBenchmarkGenTestSessionPdvTestState_Object((1,3,6,1,4,1,1271,2,1,39,1,1,13,1,11),_CienaCesBenchmarkGenTestSessionPdvTestState_Type())
cienaCesBenchmarkGenTestSessionPdvTestState.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionPdvTestState.setStatus(_A)
_CienaCesBenchmarkGenTestSessionRfc2544TestState_Type=CienaCesBenchmarkRfc2544TestState
_CienaCesBenchmarkGenTestSessionRfc2544TestState_Object=MibTableColumn
cienaCesBenchmarkGenTestSessionRfc2544TestState=_CienaCesBenchmarkGenTestSessionRfc2544TestState_Object((1,3,6,1,4,1,1271,2,1,39,1,1,13,1,12),_CienaCesBenchmarkGenTestSessionRfc2544TestState_Type())
cienaCesBenchmarkGenTestSessionRfc2544TestState.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionRfc2544TestState.setStatus(_A)
_CienaCesBenchmarkGenTestSessionY1564TestState_Type=CienaCesBenchmarkY1564TestState
_CienaCesBenchmarkGenTestSessionY1564TestState_Object=MibTableColumn
cienaCesBenchmarkGenTestSessionY1564TestState=_CienaCesBenchmarkGenTestSessionY1564TestState_Object((1,3,6,1,4,1,1271,2,1,39,1,1,13,1,13),_CienaCesBenchmarkGenTestSessionY1564TestState_Type())
cienaCesBenchmarkGenTestSessionY1564TestState.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionY1564TestState.setStatus(_A)
_CienaCesBenchmarkGenTestSessionCurrentRate_Type=Integer32
_CienaCesBenchmarkGenTestSessionCurrentRate_Object=MibTableColumn
cienaCesBenchmarkGenTestSessionCurrentRate=_CienaCesBenchmarkGenTestSessionCurrentRate_Object((1,3,6,1,4,1,1271,2,1,39,1,1,13,1,14),_CienaCesBenchmarkGenTestSessionCurrentRate_Type())
cienaCesBenchmarkGenTestSessionCurrentRate.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionCurrentRate.setStatus(_A)
_CienaCesBenchmarkGenTestSessionSamplesCompleted_Type=Integer32
_CienaCesBenchmarkGenTestSessionSamplesCompleted_Object=MibTableColumn
cienaCesBenchmarkGenTestSessionSamplesCompleted=_CienaCesBenchmarkGenTestSessionSamplesCompleted_Object((1,3,6,1,4,1,1271,2,1,39,1,1,13,1,15),_CienaCesBenchmarkGenTestSessionSamplesCompleted_Type())
cienaCesBenchmarkGenTestSessionSamplesCompleted.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionSamplesCompleted.setStatus(_A)
_CienaCesBenchmarkTestInstanceStatsTable_Object=MibTable
cienaCesBenchmarkTestInstanceStatsTable=_CienaCesBenchmarkTestInstanceStatsTable_Object((1,3,6,1,4,1,1271,2,1,39,1,1,14))
if mibBuilder.loadTexts:cienaCesBenchmarkTestInstanceStatsTable.setStatus(_A)
_CienaCesBenchmarkTestInstanceStatsEntry_Object=MibTableRow
cienaCesBenchmarkTestInstanceStatsEntry=_CienaCesBenchmarkTestInstanceStatsEntry_Object((1,3,6,1,4,1,1271,2,1,39,1,1,14,1))
cienaCesBenchmarkTestInstanceStatsEntry.setIndexNames((0,_C,_J),(0,_C,_H))
if mibBuilder.loadTexts:cienaCesBenchmarkTestInstanceStatsEntry.setStatus(_A)
_CienaCesBenchmarkTestInstanceStatsRxPkts_Type=Counter64
_CienaCesBenchmarkTestInstanceStatsRxPkts_Object=MibTableColumn
cienaCesBenchmarkTestInstanceStatsRxPkts=_CienaCesBenchmarkTestInstanceStatsRxPkts_Object((1,3,6,1,4,1,1271,2,1,39,1,1,14,1,1),_CienaCesBenchmarkTestInstanceStatsRxPkts_Type())
cienaCesBenchmarkTestInstanceStatsRxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkTestInstanceStatsRxPkts.setStatus(_A)
_CienaCesBenchmarkTestInstanceStatsRxIpv4Pkts_Type=Counter64
_CienaCesBenchmarkTestInstanceStatsRxIpv4Pkts_Object=MibTableColumn
cienaCesBenchmarkTestInstanceStatsRxIpv4Pkts=_CienaCesBenchmarkTestInstanceStatsRxIpv4Pkts_Object((1,3,6,1,4,1,1271,2,1,39,1,1,14,1,2),_CienaCesBenchmarkTestInstanceStatsRxIpv4Pkts_Type())
cienaCesBenchmarkTestInstanceStatsRxIpv4Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkTestInstanceStatsRxIpv4Pkts.setStatus(_A)
_CienaCesBenchmarkTestInstanceStatsRxIpv4UdpPkts_Type=Counter64
_CienaCesBenchmarkTestInstanceStatsRxIpv4UdpPkts_Object=MibTableColumn
cienaCesBenchmarkTestInstanceStatsRxIpv4UdpPkts=_CienaCesBenchmarkTestInstanceStatsRxIpv4UdpPkts_Object((1,3,6,1,4,1,1271,2,1,39,1,1,14,1,3),_CienaCesBenchmarkTestInstanceStatsRxIpv4UdpPkts_Type())
cienaCesBenchmarkTestInstanceStatsRxIpv4UdpPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkTestInstanceStatsRxIpv4UdpPkts.setStatus(_A)
_CienaCesBenchmarkTestInstanceStatsRxIpv6Pkts_Type=Counter64
_CienaCesBenchmarkTestInstanceStatsRxIpv6Pkts_Object=MibTableColumn
cienaCesBenchmarkTestInstanceStatsRxIpv6Pkts=_CienaCesBenchmarkTestInstanceStatsRxIpv6Pkts_Object((1,3,6,1,4,1,1271,2,1,39,1,1,14,1,4),_CienaCesBenchmarkTestInstanceStatsRxIpv6Pkts_Type())
cienaCesBenchmarkTestInstanceStatsRxIpv6Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkTestInstanceStatsRxIpv6Pkts.setStatus(_A)
_CienaCesBenchmarkTestInstanceStatsRxIpv6UdpPkts_Type=Counter64
_CienaCesBenchmarkTestInstanceStatsRxIpv6UdpPkts_Object=MibTableColumn
cienaCesBenchmarkTestInstanceStatsRxIpv6UdpPkts=_CienaCesBenchmarkTestInstanceStatsRxIpv6UdpPkts_Object((1,3,6,1,4,1,1271,2,1,39,1,1,14,1,5),_CienaCesBenchmarkTestInstanceStatsRxIpv6UdpPkts_Type())
cienaCesBenchmarkTestInstanceStatsRxIpv6UdpPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkTestInstanceStatsRxIpv6UdpPkts.setStatus(_A)
_CienaCesBenchmarkTestInstanceStatsRxNonIpPkts_Type=Counter64
_CienaCesBenchmarkTestInstanceStatsRxNonIpPkts_Object=MibTableColumn
cienaCesBenchmarkTestInstanceStatsRxNonIpPkts=_CienaCesBenchmarkTestInstanceStatsRxNonIpPkts_Object((1,3,6,1,4,1,1271,2,1,39,1,1,14,1,6),_CienaCesBenchmarkTestInstanceStatsRxNonIpPkts_Type())
cienaCesBenchmarkTestInstanceStatsRxNonIpPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkTestInstanceStatsRxNonIpPkts.setStatus(_A)
_CienaCesBenchmarkTestInstanceStatsRxUnrecognizedPkts_Type=Counter64
_CienaCesBenchmarkTestInstanceStatsRxUnrecognizedPkts_Object=MibTableColumn
cienaCesBenchmarkTestInstanceStatsRxUnrecognizedPkts=_CienaCesBenchmarkTestInstanceStatsRxUnrecognizedPkts_Object((1,3,6,1,4,1,1271,2,1,39,1,1,14,1,7),_CienaCesBenchmarkTestInstanceStatsRxUnrecognizedPkts_Type())
cienaCesBenchmarkTestInstanceStatsRxUnrecognizedPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkTestInstanceStatsRxUnrecognizedPkts.setStatus(_A)
_CienaCesBenchmarkTestInstanceStatsRxDuplicatePkts_Type=Counter64
_CienaCesBenchmarkTestInstanceStatsRxDuplicatePkts_Object=MibTableColumn
cienaCesBenchmarkTestInstanceStatsRxDuplicatePkts=_CienaCesBenchmarkTestInstanceStatsRxDuplicatePkts_Object((1,3,6,1,4,1,1271,2,1,39,1,1,14,1,8),_CienaCesBenchmarkTestInstanceStatsRxDuplicatePkts_Type())
cienaCesBenchmarkTestInstanceStatsRxDuplicatePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkTestInstanceStatsRxDuplicatePkts.setStatus(_A)
_CienaCesBenchmarkTestInstanceStatsRxDuplicatePktsOverflow_Type=TruthValue
_CienaCesBenchmarkTestInstanceStatsRxDuplicatePktsOverflow_Object=MibTableColumn
cienaCesBenchmarkTestInstanceStatsRxDuplicatePktsOverflow=_CienaCesBenchmarkTestInstanceStatsRxDuplicatePktsOverflow_Object((1,3,6,1,4,1,1271,2,1,39,1,1,14,1,9),_CienaCesBenchmarkTestInstanceStatsRxDuplicatePktsOverflow_Type())
cienaCesBenchmarkTestInstanceStatsRxDuplicatePktsOverflow.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkTestInstanceStatsRxDuplicatePktsOverflow.setStatus(_A)
_CienaCesBenchmarkTestInstanceStatsRxOOOPkts_Type=Counter64
_CienaCesBenchmarkTestInstanceStatsRxOOOPkts_Object=MibTableColumn
cienaCesBenchmarkTestInstanceStatsRxOOOPkts=_CienaCesBenchmarkTestInstanceStatsRxOOOPkts_Object((1,3,6,1,4,1,1271,2,1,39,1,1,14,1,10),_CienaCesBenchmarkTestInstanceStatsRxOOOPkts_Type())
cienaCesBenchmarkTestInstanceStatsRxOOOPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkTestInstanceStatsRxOOOPkts.setStatus(_A)
_CienaCesBenchmarkTestInstanceStatsRxOOOPktsOverflow_Type=TruthValue
_CienaCesBenchmarkTestInstanceStatsRxOOOPktsOverflow_Object=MibTableColumn
cienaCesBenchmarkTestInstanceStatsRxOOOPktsOverflow=_CienaCesBenchmarkTestInstanceStatsRxOOOPktsOverflow_Object((1,3,6,1,4,1,1271,2,1,39,1,1,14,1,11),_CienaCesBenchmarkTestInstanceStatsRxOOOPktsOverflow_Type())
cienaCesBenchmarkTestInstanceStatsRxOOOPktsOverflow.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkTestInstanceStatsRxOOOPktsOverflow.setStatus(_A)
_CienaCesBenchmarkTestInstanceStatsRxDiscSeqNumPkts_Type=Counter64
_CienaCesBenchmarkTestInstanceStatsRxDiscSeqNumPkts_Object=MibTableColumn
cienaCesBenchmarkTestInstanceStatsRxDiscSeqNumPkts=_CienaCesBenchmarkTestInstanceStatsRxDiscSeqNumPkts_Object((1,3,6,1,4,1,1271,2,1,39,1,1,14,1,12),_CienaCesBenchmarkTestInstanceStatsRxDiscSeqNumPkts_Type())
cienaCesBenchmarkTestInstanceStatsRxDiscSeqNumPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkTestInstanceStatsRxDiscSeqNumPkts.setStatus(_A)
_CienaCesBenchmarkTestInstanceStatsRxDiscSeqNumPktsOverflow_Type=TruthValue
_CienaCesBenchmarkTestInstanceStatsRxDiscSeqNumPktsOverflow_Object=MibTableColumn
cienaCesBenchmarkTestInstanceStatsRxDiscSeqNumPktsOverflow=_CienaCesBenchmarkTestInstanceStatsRxDiscSeqNumPktsOverflow_Object((1,3,6,1,4,1,1271,2,1,39,1,1,14,1,13),_CienaCesBenchmarkTestInstanceStatsRxDiscSeqNumPktsOverflow_Type())
cienaCesBenchmarkTestInstanceStatsRxDiscSeqNumPktsOverflow.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkTestInstanceStatsRxDiscSeqNumPktsOverflow.setStatus(_A)
_CienaCesBenchmarkTestInstanceStatsRxUdpCheckSumPkts_Type=Counter64
_CienaCesBenchmarkTestInstanceStatsRxUdpCheckSumPkts_Object=MibTableColumn
cienaCesBenchmarkTestInstanceStatsRxUdpCheckSumPkts=_CienaCesBenchmarkTestInstanceStatsRxUdpCheckSumPkts_Object((1,3,6,1,4,1,1271,2,1,39,1,1,14,1,14),_CienaCesBenchmarkTestInstanceStatsRxUdpCheckSumPkts_Type())
cienaCesBenchmarkTestInstanceStatsRxUdpCheckSumPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkTestInstanceStatsRxUdpCheckSumPkts.setStatus(_A)
_CienaCesBenchmarkTestInstanceStatsTxPkts_Type=Counter64
_CienaCesBenchmarkTestInstanceStatsTxPkts_Object=MibTableColumn
cienaCesBenchmarkTestInstanceStatsTxPkts=_CienaCesBenchmarkTestInstanceStatsTxPkts_Object((1,3,6,1,4,1,1271,2,1,39,1,1,14,1,15),_CienaCesBenchmarkTestInstanceStatsTxPkts_Type())
cienaCesBenchmarkTestInstanceStatsTxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkTestInstanceStatsTxPkts.setStatus(_A)
_CienaCesBenchmarkGenTestSessionThroughputResultsTable_Object=MibTable
cienaCesBenchmarkGenTestSessionThroughputResultsTable=_CienaCesBenchmarkGenTestSessionThroughputResultsTable_Object((1,3,6,1,4,1,1271,2,1,39,1,1,15))
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionThroughputResultsTable.setStatus(_A)
_CienaCesBenchmarkGenTestSessionThroughputResultsEntry_Object=MibTableRow
cienaCesBenchmarkGenTestSessionThroughputResultsEntry=_CienaCesBenchmarkGenTestSessionThroughputResultsEntry_Object((1,3,6,1,4,1,1271,2,1,39,1,1,15,1))
cienaCesBenchmarkGenTestSessionThroughputResultsEntry.setIndexNames((0,_C,_J),(0,_C,_H),(0,_C,_p),(0,_C,_q),(0,_C,_r))
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionThroughputResultsEntry.setStatus(_A)
class _CienaCesBenchmarkGenTestSessionThroughputResultsPcpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_CienaCesBenchmarkGenTestSessionThroughputResultsPcpIndex_Type.__name__=_E
_CienaCesBenchmarkGenTestSessionThroughputResultsPcpIndex_Object=MibTableColumn
cienaCesBenchmarkGenTestSessionThroughputResultsPcpIndex=_CienaCesBenchmarkGenTestSessionThroughputResultsPcpIndex_Object((1,3,6,1,4,1,1271,2,1,39,1,1,15,1,1),_CienaCesBenchmarkGenTestSessionThroughputResultsPcpIndex_Type())
cienaCesBenchmarkGenTestSessionThroughputResultsPcpIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionThroughputResultsPcpIndex.setStatus(_A)
class _CienaCesBenchmarkGenTestSessionThroughputResultsColorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_CienaCesBenchmarkGenTestSessionThroughputResultsColorIndex_Type.__name__=_E
_CienaCesBenchmarkGenTestSessionThroughputResultsColorIndex_Object=MibTableColumn
cienaCesBenchmarkGenTestSessionThroughputResultsColorIndex=_CienaCesBenchmarkGenTestSessionThroughputResultsColorIndex_Object((1,3,6,1,4,1,1271,2,1,39,1,1,15,1,2),_CienaCesBenchmarkGenTestSessionThroughputResultsColorIndex_Type())
cienaCesBenchmarkGenTestSessionThroughputResultsColorIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionThroughputResultsColorIndex.setStatus(_A)
class _CienaCesBenchmarkGenTestSessionThroughputResultsFrameSizeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_CienaCesBenchmarkGenTestSessionThroughputResultsFrameSizeIndex_Type.__name__=_E
_CienaCesBenchmarkGenTestSessionThroughputResultsFrameSizeIndex_Object=MibTableColumn
cienaCesBenchmarkGenTestSessionThroughputResultsFrameSizeIndex=_CienaCesBenchmarkGenTestSessionThroughputResultsFrameSizeIndex_Object((1,3,6,1,4,1,1271,2,1,39,1,1,15,1,3),_CienaCesBenchmarkGenTestSessionThroughputResultsFrameSizeIndex_Type())
cienaCesBenchmarkGenTestSessionThroughputResultsFrameSizeIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionThroughputResultsFrameSizeIndex.setStatus(_A)
class _CienaCesBenchmarkGenTestSessionThroughputResultsPcp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_CienaCesBenchmarkGenTestSessionThroughputResultsPcp_Type.__name__=_E
_CienaCesBenchmarkGenTestSessionThroughputResultsPcp_Object=MibTableColumn
cienaCesBenchmarkGenTestSessionThroughputResultsPcp=_CienaCesBenchmarkGenTestSessionThroughputResultsPcp_Object((1,3,6,1,4,1,1271,2,1,39,1,1,15,1,4),_CienaCesBenchmarkGenTestSessionThroughputResultsPcp_Type())
cienaCesBenchmarkGenTestSessionThroughputResultsPcp.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionThroughputResultsPcp.setStatus(_A)
_CienaCesBenchmarkGenTestSessionThroughputResultsColor_Type=CienaCesBenchmarkColorTest
_CienaCesBenchmarkGenTestSessionThroughputResultsColor_Object=MibTableColumn
cienaCesBenchmarkGenTestSessionThroughputResultsColor=_CienaCesBenchmarkGenTestSessionThroughputResultsColor_Object((1,3,6,1,4,1,1271,2,1,39,1,1,15,1,5),_CienaCesBenchmarkGenTestSessionThroughputResultsColor_Type())
cienaCesBenchmarkGenTestSessionThroughputResultsColor.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionThroughputResultsColor.setStatus(_A)
_CienaCesBenchmarkGenTestSessionThroughputResultsFrameSize_Type=Integer32
_CienaCesBenchmarkGenTestSessionThroughputResultsFrameSize_Object=MibTableColumn
cienaCesBenchmarkGenTestSessionThroughputResultsFrameSize=_CienaCesBenchmarkGenTestSessionThroughputResultsFrameSize_Object((1,3,6,1,4,1,1271,2,1,39,1,1,15,1,6),_CienaCesBenchmarkGenTestSessionThroughputResultsFrameSize_Type())
cienaCesBenchmarkGenTestSessionThroughputResultsFrameSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionThroughputResultsFrameSize.setStatus(_A)
class _CienaCesBenchmarkGenTestSessionThroughputResultsEmixSequenceId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_CienaCesBenchmarkGenTestSessionThroughputResultsEmixSequenceId_Type.__name__=_E
_CienaCesBenchmarkGenTestSessionThroughputResultsEmixSequenceId_Object=MibTableColumn
cienaCesBenchmarkGenTestSessionThroughputResultsEmixSequenceId=_CienaCesBenchmarkGenTestSessionThroughputResultsEmixSequenceId_Object((1,3,6,1,4,1,1271,2,1,39,1,1,15,1,7),_CienaCesBenchmarkGenTestSessionThroughputResultsEmixSequenceId_Type())
cienaCesBenchmarkGenTestSessionThroughputResultsEmixSequenceId.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionThroughputResultsEmixSequenceId.setStatus(_A)
_CienaCesBenchmarkGenTestSessionThroughputResultsMin_Type=CienaCesBenchmarkThroughputResult
_CienaCesBenchmarkGenTestSessionThroughputResultsMin_Object=MibTableColumn
cienaCesBenchmarkGenTestSessionThroughputResultsMin=_CienaCesBenchmarkGenTestSessionThroughputResultsMin_Object((1,3,6,1,4,1,1271,2,1,39,1,1,15,1,8),_CienaCesBenchmarkGenTestSessionThroughputResultsMin_Type())
cienaCesBenchmarkGenTestSessionThroughputResultsMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionThroughputResultsMin.setStatus(_A)
_CienaCesBenchmarkGenTestSessionThroughputResultsMax_Type=CienaCesBenchmarkThroughputResult
_CienaCesBenchmarkGenTestSessionThroughputResultsMax_Object=MibTableColumn
cienaCesBenchmarkGenTestSessionThroughputResultsMax=_CienaCesBenchmarkGenTestSessionThroughputResultsMax_Object((1,3,6,1,4,1,1271,2,1,39,1,1,15,1,9),_CienaCesBenchmarkGenTestSessionThroughputResultsMax_Type())
cienaCesBenchmarkGenTestSessionThroughputResultsMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionThroughputResultsMax.setStatus(_A)
_CienaCesBenchmarkGenTestSessionThroughputResultsAvg_Type=CienaCesBenchmarkThroughputResult
_CienaCesBenchmarkGenTestSessionThroughputResultsAvg_Object=MibTableColumn
cienaCesBenchmarkGenTestSessionThroughputResultsAvg=_CienaCesBenchmarkGenTestSessionThroughputResultsAvg_Object((1,3,6,1,4,1,1271,2,1,39,1,1,15,1,10),_CienaCesBenchmarkGenTestSessionThroughputResultsAvg_Type())
cienaCesBenchmarkGenTestSessionThroughputResultsAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionThroughputResultsAvg.setStatus(_A)
_CienaCesBenchmarkGenTestSessionThroughputResultsIterations_Type=Integer32
_CienaCesBenchmarkGenTestSessionThroughputResultsIterations_Object=MibTableColumn
cienaCesBenchmarkGenTestSessionThroughputResultsIterations=_CienaCesBenchmarkGenTestSessionThroughputResultsIterations_Object((1,3,6,1,4,1,1271,2,1,39,1,1,15,1,11),_CienaCesBenchmarkGenTestSessionThroughputResultsIterations_Type())
cienaCesBenchmarkGenTestSessionThroughputResultsIterations.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionThroughputResultsIterations.setStatus(_A)
_CienaCesBenchmarkGenTestSessionThroughputResultsKpiResult_Type=CienaCesBenchmarkKpiResult
_CienaCesBenchmarkGenTestSessionThroughputResultsKpiResult_Object=MibTableColumn
cienaCesBenchmarkGenTestSessionThroughputResultsKpiResult=_CienaCesBenchmarkGenTestSessionThroughputResultsKpiResult_Object((1,3,6,1,4,1,1271,2,1,39,1,1,15,1,12),_CienaCesBenchmarkGenTestSessionThroughputResultsKpiResult_Type())
cienaCesBenchmarkGenTestSessionThroughputResultsKpiResult.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionThroughputResultsKpiResult.setStatus(_A)
_CienaCesBenchmarkGenTestSessionFramelossResultsTable_Object=MibTable
cienaCesBenchmarkGenTestSessionFramelossResultsTable=_CienaCesBenchmarkGenTestSessionFramelossResultsTable_Object((1,3,6,1,4,1,1271,2,1,39,1,1,16))
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionFramelossResultsTable.setStatus(_A)
_CienaCesBenchmarkGenTestSessionFramelossResultsEntry_Object=MibTableRow
cienaCesBenchmarkGenTestSessionFramelossResultsEntry=_CienaCesBenchmarkGenTestSessionFramelossResultsEntry_Object((1,3,6,1,4,1,1271,2,1,39,1,1,16,1))
cienaCesBenchmarkGenTestSessionFramelossResultsEntry.setIndexNames((0,_C,_J),(0,_C,_H),(0,_C,_s),(0,_C,_t),(0,_C,_u),(0,_C,_v))
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionFramelossResultsEntry.setStatus(_A)
class _CienaCesBenchmarkGenTestSessionFramelossResultsPcpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_CienaCesBenchmarkGenTestSessionFramelossResultsPcpIndex_Type.__name__=_E
_CienaCesBenchmarkGenTestSessionFramelossResultsPcpIndex_Object=MibTableColumn
cienaCesBenchmarkGenTestSessionFramelossResultsPcpIndex=_CienaCesBenchmarkGenTestSessionFramelossResultsPcpIndex_Object((1,3,6,1,4,1,1271,2,1,39,1,1,16,1,1),_CienaCesBenchmarkGenTestSessionFramelossResultsPcpIndex_Type())
cienaCesBenchmarkGenTestSessionFramelossResultsPcpIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionFramelossResultsPcpIndex.setStatus(_A)
class _CienaCesBenchmarkGenTestSessionFramelossResultsColorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_CienaCesBenchmarkGenTestSessionFramelossResultsColorIndex_Type.__name__=_E
_CienaCesBenchmarkGenTestSessionFramelossResultsColorIndex_Object=MibTableColumn
cienaCesBenchmarkGenTestSessionFramelossResultsColorIndex=_CienaCesBenchmarkGenTestSessionFramelossResultsColorIndex_Object((1,3,6,1,4,1,1271,2,1,39,1,1,16,1,2),_CienaCesBenchmarkGenTestSessionFramelossResultsColorIndex_Type())
cienaCesBenchmarkGenTestSessionFramelossResultsColorIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionFramelossResultsColorIndex.setStatus(_A)
class _CienaCesBenchmarkGenTestSessionFramelossResultsFrameSizeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_CienaCesBenchmarkGenTestSessionFramelossResultsFrameSizeIndex_Type.__name__=_E
_CienaCesBenchmarkGenTestSessionFramelossResultsFrameSizeIndex_Object=MibTableColumn
cienaCesBenchmarkGenTestSessionFramelossResultsFrameSizeIndex=_CienaCesBenchmarkGenTestSessionFramelossResultsFrameSizeIndex_Object((1,3,6,1,4,1,1271,2,1,39,1,1,16,1,3),_CienaCesBenchmarkGenTestSessionFramelossResultsFrameSizeIndex_Type())
cienaCesBenchmarkGenTestSessionFramelossResultsFrameSizeIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionFramelossResultsFrameSizeIndex.setStatus(_A)
class _CienaCesBenchmarkGenTestSessionFramelossResultsRateIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_CienaCesBenchmarkGenTestSessionFramelossResultsRateIndex_Type.__name__=_E
_CienaCesBenchmarkGenTestSessionFramelossResultsRateIndex_Object=MibTableColumn
cienaCesBenchmarkGenTestSessionFramelossResultsRateIndex=_CienaCesBenchmarkGenTestSessionFramelossResultsRateIndex_Object((1,3,6,1,4,1,1271,2,1,39,1,1,16,1,4),_CienaCesBenchmarkGenTestSessionFramelossResultsRateIndex_Type())
cienaCesBenchmarkGenTestSessionFramelossResultsRateIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionFramelossResultsRateIndex.setStatus(_A)
class _CienaCesBenchmarkGenTestSessionFramelossResultsPcp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_CienaCesBenchmarkGenTestSessionFramelossResultsPcp_Type.__name__=_E
_CienaCesBenchmarkGenTestSessionFramelossResultsPcp_Object=MibTableColumn
cienaCesBenchmarkGenTestSessionFramelossResultsPcp=_CienaCesBenchmarkGenTestSessionFramelossResultsPcp_Object((1,3,6,1,4,1,1271,2,1,39,1,1,16,1,5),_CienaCesBenchmarkGenTestSessionFramelossResultsPcp_Type())
cienaCesBenchmarkGenTestSessionFramelossResultsPcp.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionFramelossResultsPcp.setStatus(_A)
_CienaCesBenchmarkGenTestSessionFramelossResultsColor_Type=CienaCesBenchmarkColorTest
_CienaCesBenchmarkGenTestSessionFramelossResultsColor_Object=MibTableColumn
cienaCesBenchmarkGenTestSessionFramelossResultsColor=_CienaCesBenchmarkGenTestSessionFramelossResultsColor_Object((1,3,6,1,4,1,1271,2,1,39,1,1,16,1,6),_CienaCesBenchmarkGenTestSessionFramelossResultsColor_Type())
cienaCesBenchmarkGenTestSessionFramelossResultsColor.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionFramelossResultsColor.setStatus(_A)
_CienaCesBenchmarkGenTestSessionFramelossResultsFrameSize_Type=Integer32
_CienaCesBenchmarkGenTestSessionFramelossResultsFrameSize_Object=MibTableColumn
cienaCesBenchmarkGenTestSessionFramelossResultsFrameSize=_CienaCesBenchmarkGenTestSessionFramelossResultsFrameSize_Object((1,3,6,1,4,1,1271,2,1,39,1,1,16,1,7),_CienaCesBenchmarkGenTestSessionFramelossResultsFrameSize_Type())
cienaCesBenchmarkGenTestSessionFramelossResultsFrameSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionFramelossResultsFrameSize.setStatus(_A)
class _CienaCesBenchmarkGenTestSessionFramelossResultsEmixSequenceId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_CienaCesBenchmarkGenTestSessionFramelossResultsEmixSequenceId_Type.__name__=_E
_CienaCesBenchmarkGenTestSessionFramelossResultsEmixSequenceId_Object=MibTableColumn
cienaCesBenchmarkGenTestSessionFramelossResultsEmixSequenceId=_CienaCesBenchmarkGenTestSessionFramelossResultsEmixSequenceId_Object((1,3,6,1,4,1,1271,2,1,39,1,1,16,1,8),_CienaCesBenchmarkGenTestSessionFramelossResultsEmixSequenceId_Type())
cienaCesBenchmarkGenTestSessionFramelossResultsEmixSequenceId.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionFramelossResultsEmixSequenceId.setStatus(_A)
_CienaCesBenchmarkGenTestSessionFramelossResultsRate_Type=Integer32
_CienaCesBenchmarkGenTestSessionFramelossResultsRate_Object=MibTableColumn
cienaCesBenchmarkGenTestSessionFramelossResultsRate=_CienaCesBenchmarkGenTestSessionFramelossResultsRate_Object((1,3,6,1,4,1,1271,2,1,39,1,1,16,1,9),_CienaCesBenchmarkGenTestSessionFramelossResultsRate_Type())
cienaCesBenchmarkGenTestSessionFramelossResultsRate.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionFramelossResultsRate.setStatus(_A)
_CienaCesBenchmarkGenTestSessionFramelossResultsFirst_Type=CienaCesBenchmarkFramelossResult
_CienaCesBenchmarkGenTestSessionFramelossResultsFirst_Object=MibTableColumn
cienaCesBenchmarkGenTestSessionFramelossResultsFirst=_CienaCesBenchmarkGenTestSessionFramelossResultsFirst_Object((1,3,6,1,4,1,1271,2,1,39,1,1,16,1,10),_CienaCesBenchmarkGenTestSessionFramelossResultsFirst_Type())
cienaCesBenchmarkGenTestSessionFramelossResultsFirst.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionFramelossResultsFirst.setStatus(_A)
_CienaCesBenchmarkGenTestSessionFramelossResultsSecond_Type=CienaCesBenchmarkFramelossResult
_CienaCesBenchmarkGenTestSessionFramelossResultsSecond_Object=MibTableColumn
cienaCesBenchmarkGenTestSessionFramelossResultsSecond=_CienaCesBenchmarkGenTestSessionFramelossResultsSecond_Object((1,3,6,1,4,1,1271,2,1,39,1,1,16,1,11),_CienaCesBenchmarkGenTestSessionFramelossResultsSecond_Type())
cienaCesBenchmarkGenTestSessionFramelossResultsSecond.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionFramelossResultsSecond.setStatus(_A)
_CienaCesBenchmarkGenTestSessionFramelossResultsKpiResult_Type=CienaCesBenchmarkKpiResult
_CienaCesBenchmarkGenTestSessionFramelossResultsKpiResult_Object=MibTableColumn
cienaCesBenchmarkGenTestSessionFramelossResultsKpiResult=_CienaCesBenchmarkGenTestSessionFramelossResultsKpiResult_Object((1,3,6,1,4,1,1271,2,1,39,1,1,16,1,12),_CienaCesBenchmarkGenTestSessionFramelossResultsKpiResult_Type())
cienaCesBenchmarkGenTestSessionFramelossResultsKpiResult.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionFramelossResultsKpiResult.setStatus(_A)
_CienaCesBenchmarkGenTestSessionFramelossResultsResult_Type=CienaCesBenchmarkFramelossResult
_CienaCesBenchmarkGenTestSessionFramelossResultsResult_Object=MibTableColumn
cienaCesBenchmarkGenTestSessionFramelossResultsResult=_CienaCesBenchmarkGenTestSessionFramelossResultsResult_Object((1,3,6,1,4,1,1271,2,1,39,1,1,16,1,13),_CienaCesBenchmarkGenTestSessionFramelossResultsResult_Type())
cienaCesBenchmarkGenTestSessionFramelossResultsResult.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionFramelossResultsResult.setStatus(_A)
_CienaCesBenchmarkGenTestSessionLatencyResultsTable_Object=MibTable
cienaCesBenchmarkGenTestSessionLatencyResultsTable=_CienaCesBenchmarkGenTestSessionLatencyResultsTable_Object((1,3,6,1,4,1,1271,2,1,39,1,1,17))
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionLatencyResultsTable.setStatus(_A)
_CienaCesBenchmarkGenTestSessionLatencyResultsEntry_Object=MibTableRow
cienaCesBenchmarkGenTestSessionLatencyResultsEntry=_CienaCesBenchmarkGenTestSessionLatencyResultsEntry_Object((1,3,6,1,4,1,1271,2,1,39,1,1,17,1))
cienaCesBenchmarkGenTestSessionLatencyResultsEntry.setIndexNames((0,_C,_J),(0,_C,_H),(0,_C,_w),(0,_C,_x),(0,_C,_y))
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionLatencyResultsEntry.setStatus(_A)
class _CienaCesBenchmarkGenTestSessionLatencyResultsPcpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_CienaCesBenchmarkGenTestSessionLatencyResultsPcpIndex_Type.__name__=_E
_CienaCesBenchmarkGenTestSessionLatencyResultsPcpIndex_Object=MibTableColumn
cienaCesBenchmarkGenTestSessionLatencyResultsPcpIndex=_CienaCesBenchmarkGenTestSessionLatencyResultsPcpIndex_Object((1,3,6,1,4,1,1271,2,1,39,1,1,17,1,1),_CienaCesBenchmarkGenTestSessionLatencyResultsPcpIndex_Type())
cienaCesBenchmarkGenTestSessionLatencyResultsPcpIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionLatencyResultsPcpIndex.setStatus(_A)
class _CienaCesBenchmarkGenTestSessionLatencyResultsColorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_CienaCesBenchmarkGenTestSessionLatencyResultsColorIndex_Type.__name__=_E
_CienaCesBenchmarkGenTestSessionLatencyResultsColorIndex_Object=MibTableColumn
cienaCesBenchmarkGenTestSessionLatencyResultsColorIndex=_CienaCesBenchmarkGenTestSessionLatencyResultsColorIndex_Object((1,3,6,1,4,1,1271,2,1,39,1,1,17,1,2),_CienaCesBenchmarkGenTestSessionLatencyResultsColorIndex_Type())
cienaCesBenchmarkGenTestSessionLatencyResultsColorIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionLatencyResultsColorIndex.setStatus(_A)
class _CienaCesBenchmarkGenTestSessionLatencyResultsFrameSizeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_CienaCesBenchmarkGenTestSessionLatencyResultsFrameSizeIndex_Type.__name__=_E
_CienaCesBenchmarkGenTestSessionLatencyResultsFrameSizeIndex_Object=MibTableColumn
cienaCesBenchmarkGenTestSessionLatencyResultsFrameSizeIndex=_CienaCesBenchmarkGenTestSessionLatencyResultsFrameSizeIndex_Object((1,3,6,1,4,1,1271,2,1,39,1,1,17,1,3),_CienaCesBenchmarkGenTestSessionLatencyResultsFrameSizeIndex_Type())
cienaCesBenchmarkGenTestSessionLatencyResultsFrameSizeIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionLatencyResultsFrameSizeIndex.setStatus(_A)
class _CienaCesBenchmarkGenTestSessionLatencyResultsPcp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_CienaCesBenchmarkGenTestSessionLatencyResultsPcp_Type.__name__=_E
_CienaCesBenchmarkGenTestSessionLatencyResultsPcp_Object=MibTableColumn
cienaCesBenchmarkGenTestSessionLatencyResultsPcp=_CienaCesBenchmarkGenTestSessionLatencyResultsPcp_Object((1,3,6,1,4,1,1271,2,1,39,1,1,17,1,4),_CienaCesBenchmarkGenTestSessionLatencyResultsPcp_Type())
cienaCesBenchmarkGenTestSessionLatencyResultsPcp.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionLatencyResultsPcp.setStatus(_A)
_CienaCesBenchmarkGenTestSessionLatencyResultsColor_Type=CienaCesBenchmarkColorTest
_CienaCesBenchmarkGenTestSessionLatencyResultsColor_Object=MibTableColumn
cienaCesBenchmarkGenTestSessionLatencyResultsColor=_CienaCesBenchmarkGenTestSessionLatencyResultsColor_Object((1,3,6,1,4,1,1271,2,1,39,1,1,17,1,5),_CienaCesBenchmarkGenTestSessionLatencyResultsColor_Type())
cienaCesBenchmarkGenTestSessionLatencyResultsColor.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionLatencyResultsColor.setStatus(_A)
_CienaCesBenchmarkGenTestSessionLatencyResultsFrameSize_Type=Integer32
_CienaCesBenchmarkGenTestSessionLatencyResultsFrameSize_Object=MibTableColumn
cienaCesBenchmarkGenTestSessionLatencyResultsFrameSize=_CienaCesBenchmarkGenTestSessionLatencyResultsFrameSize_Object((1,3,6,1,4,1,1271,2,1,39,1,1,17,1,6),_CienaCesBenchmarkGenTestSessionLatencyResultsFrameSize_Type())
cienaCesBenchmarkGenTestSessionLatencyResultsFrameSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionLatencyResultsFrameSize.setStatus(_A)
class _CienaCesBenchmarkGenTestSessionLatencyResultsEmixSequenceId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_CienaCesBenchmarkGenTestSessionLatencyResultsEmixSequenceId_Type.__name__=_E
_CienaCesBenchmarkGenTestSessionLatencyResultsEmixSequenceId_Object=MibTableColumn
cienaCesBenchmarkGenTestSessionLatencyResultsEmixSequenceId=_CienaCesBenchmarkGenTestSessionLatencyResultsEmixSequenceId_Object((1,3,6,1,4,1,1271,2,1,39,1,1,17,1,7),_CienaCesBenchmarkGenTestSessionLatencyResultsEmixSequenceId_Type())
cienaCesBenchmarkGenTestSessionLatencyResultsEmixSequenceId.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionLatencyResultsEmixSequenceId.setStatus(_A)
_CienaCesBenchmarkGenTestSessionLatencyResultsMin_Type=Unsigned32
_CienaCesBenchmarkGenTestSessionLatencyResultsMin_Object=MibTableColumn
cienaCesBenchmarkGenTestSessionLatencyResultsMin=_CienaCesBenchmarkGenTestSessionLatencyResultsMin_Object((1,3,6,1,4,1,1271,2,1,39,1,1,17,1,8),_CienaCesBenchmarkGenTestSessionLatencyResultsMin_Type())
cienaCesBenchmarkGenTestSessionLatencyResultsMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionLatencyResultsMin.setStatus(_A)
_CienaCesBenchmarkGenTestSessionLatencyResultsMax_Type=Unsigned32
_CienaCesBenchmarkGenTestSessionLatencyResultsMax_Object=MibTableColumn
cienaCesBenchmarkGenTestSessionLatencyResultsMax=_CienaCesBenchmarkGenTestSessionLatencyResultsMax_Object((1,3,6,1,4,1,1271,2,1,39,1,1,17,1,9),_CienaCesBenchmarkGenTestSessionLatencyResultsMax_Type())
cienaCesBenchmarkGenTestSessionLatencyResultsMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionLatencyResultsMax.setStatus(_A)
_CienaCesBenchmarkGenTestSessionLatencyResultsAvg_Type=Unsigned32
_CienaCesBenchmarkGenTestSessionLatencyResultsAvg_Object=MibTableColumn
cienaCesBenchmarkGenTestSessionLatencyResultsAvg=_CienaCesBenchmarkGenTestSessionLatencyResultsAvg_Object((1,3,6,1,4,1,1271,2,1,39,1,1,17,1,10),_CienaCesBenchmarkGenTestSessionLatencyResultsAvg_Type())
cienaCesBenchmarkGenTestSessionLatencyResultsAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionLatencyResultsAvg.setStatus(_A)
_CienaCesBenchmarkGenTestSessionLatencyResultsSamples_Type=Integer32
_CienaCesBenchmarkGenTestSessionLatencyResultsSamples_Object=MibTableColumn
cienaCesBenchmarkGenTestSessionLatencyResultsSamples=_CienaCesBenchmarkGenTestSessionLatencyResultsSamples_Object((1,3,6,1,4,1,1271,2,1,39,1,1,17,1,11),_CienaCesBenchmarkGenTestSessionLatencyResultsSamples_Type())
cienaCesBenchmarkGenTestSessionLatencyResultsSamples.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionLatencyResultsSamples.setStatus(_A)
_CienaCesBenchmarkGenTestSessionLatencyResultsKpiResult_Type=CienaCesBenchmarkKpiResult
_CienaCesBenchmarkGenTestSessionLatencyResultsKpiResult_Object=MibTableColumn
cienaCesBenchmarkGenTestSessionLatencyResultsKpiResult=_CienaCesBenchmarkGenTestSessionLatencyResultsKpiResult_Object((1,3,6,1,4,1,1271,2,1,39,1,1,17,1,12),_CienaCesBenchmarkGenTestSessionLatencyResultsKpiResult_Type())
cienaCesBenchmarkGenTestSessionLatencyResultsKpiResult.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionLatencyResultsKpiResult.setStatus(_A)
_CienaCesBenchmarkGenTestSessionPdvResultsTable_Object=MibTable
cienaCesBenchmarkGenTestSessionPdvResultsTable=_CienaCesBenchmarkGenTestSessionPdvResultsTable_Object((1,3,6,1,4,1,1271,2,1,39,1,1,18))
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionPdvResultsTable.setStatus(_A)
_CienaCesBenchmarkGenTestSessionPdvResultsEntry_Object=MibTableRow
cienaCesBenchmarkGenTestSessionPdvResultsEntry=_CienaCesBenchmarkGenTestSessionPdvResultsEntry_Object((1,3,6,1,4,1,1271,2,1,39,1,1,18,1))
cienaCesBenchmarkGenTestSessionPdvResultsEntry.setIndexNames((0,_C,_J),(0,_C,_H),(0,_C,_z),(0,_C,_A0),(0,_C,_A1))
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionPdvResultsEntry.setStatus(_A)
class _CienaCesBenchmarkGenTestSessionPdvResultsPcpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_CienaCesBenchmarkGenTestSessionPdvResultsPcpIndex_Type.__name__=_E
_CienaCesBenchmarkGenTestSessionPdvResultsPcpIndex_Object=MibTableColumn
cienaCesBenchmarkGenTestSessionPdvResultsPcpIndex=_CienaCesBenchmarkGenTestSessionPdvResultsPcpIndex_Object((1,3,6,1,4,1,1271,2,1,39,1,1,18,1,1),_CienaCesBenchmarkGenTestSessionPdvResultsPcpIndex_Type())
cienaCesBenchmarkGenTestSessionPdvResultsPcpIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionPdvResultsPcpIndex.setStatus(_A)
class _CienaCesBenchmarkGenTestSessionPdvResultsColorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_CienaCesBenchmarkGenTestSessionPdvResultsColorIndex_Type.__name__=_E
_CienaCesBenchmarkGenTestSessionPdvResultsColorIndex_Object=MibTableColumn
cienaCesBenchmarkGenTestSessionPdvResultsColorIndex=_CienaCesBenchmarkGenTestSessionPdvResultsColorIndex_Object((1,3,6,1,4,1,1271,2,1,39,1,1,18,1,2),_CienaCesBenchmarkGenTestSessionPdvResultsColorIndex_Type())
cienaCesBenchmarkGenTestSessionPdvResultsColorIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionPdvResultsColorIndex.setStatus(_A)
class _CienaCesBenchmarkGenTestSessionPdvResultsFrameSizeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_CienaCesBenchmarkGenTestSessionPdvResultsFrameSizeIndex_Type.__name__=_E
_CienaCesBenchmarkGenTestSessionPdvResultsFrameSizeIndex_Object=MibTableColumn
cienaCesBenchmarkGenTestSessionPdvResultsFrameSizeIndex=_CienaCesBenchmarkGenTestSessionPdvResultsFrameSizeIndex_Object((1,3,6,1,4,1,1271,2,1,39,1,1,18,1,3),_CienaCesBenchmarkGenTestSessionPdvResultsFrameSizeIndex_Type())
cienaCesBenchmarkGenTestSessionPdvResultsFrameSizeIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionPdvResultsFrameSizeIndex.setStatus(_A)
class _CienaCesBenchmarkGenTestSessionPdvResultsPcp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_CienaCesBenchmarkGenTestSessionPdvResultsPcp_Type.__name__=_E
_CienaCesBenchmarkGenTestSessionPdvResultsPcp_Object=MibTableColumn
cienaCesBenchmarkGenTestSessionPdvResultsPcp=_CienaCesBenchmarkGenTestSessionPdvResultsPcp_Object((1,3,6,1,4,1,1271,2,1,39,1,1,18,1,4),_CienaCesBenchmarkGenTestSessionPdvResultsPcp_Type())
cienaCesBenchmarkGenTestSessionPdvResultsPcp.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionPdvResultsPcp.setStatus(_A)
_CienaCesBenchmarkGenTestSessionPdvResultsColor_Type=CienaCesBenchmarkColorTest
_CienaCesBenchmarkGenTestSessionPdvResultsColor_Object=MibTableColumn
cienaCesBenchmarkGenTestSessionPdvResultsColor=_CienaCesBenchmarkGenTestSessionPdvResultsColor_Object((1,3,6,1,4,1,1271,2,1,39,1,1,18,1,5),_CienaCesBenchmarkGenTestSessionPdvResultsColor_Type())
cienaCesBenchmarkGenTestSessionPdvResultsColor.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionPdvResultsColor.setStatus(_A)
_CienaCesBenchmarkGenTestSessionPdvResultsFrameSize_Type=Integer32
_CienaCesBenchmarkGenTestSessionPdvResultsFrameSize_Object=MibTableColumn
cienaCesBenchmarkGenTestSessionPdvResultsFrameSize=_CienaCesBenchmarkGenTestSessionPdvResultsFrameSize_Object((1,3,6,1,4,1,1271,2,1,39,1,1,18,1,6),_CienaCesBenchmarkGenTestSessionPdvResultsFrameSize_Type())
cienaCesBenchmarkGenTestSessionPdvResultsFrameSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionPdvResultsFrameSize.setStatus(_A)
class _CienaCesBenchmarkGenTestSessionPdvResultsEmixSequenceId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_CienaCesBenchmarkGenTestSessionPdvResultsEmixSequenceId_Type.__name__=_E
_CienaCesBenchmarkGenTestSessionPdvResultsEmixSequenceId_Object=MibTableColumn
cienaCesBenchmarkGenTestSessionPdvResultsEmixSequenceId=_CienaCesBenchmarkGenTestSessionPdvResultsEmixSequenceId_Object((1,3,6,1,4,1,1271,2,1,39,1,1,18,1,7),_CienaCesBenchmarkGenTestSessionPdvResultsEmixSequenceId_Type())
cienaCesBenchmarkGenTestSessionPdvResultsEmixSequenceId.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionPdvResultsEmixSequenceId.setStatus(_A)
_CienaCesBenchmarkGenTestSessionPdvResultsAvg_Type=Unsigned32
_CienaCesBenchmarkGenTestSessionPdvResultsAvg_Object=MibTableColumn
cienaCesBenchmarkGenTestSessionPdvResultsAvg=_CienaCesBenchmarkGenTestSessionPdvResultsAvg_Object((1,3,6,1,4,1,1271,2,1,39,1,1,18,1,8),_CienaCesBenchmarkGenTestSessionPdvResultsAvg_Type())
cienaCesBenchmarkGenTestSessionPdvResultsAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionPdvResultsAvg.setStatus(_A)
_CienaCesBenchmarkGenTestSessionPdvResultsSamples_Type=Integer32
_CienaCesBenchmarkGenTestSessionPdvResultsSamples_Object=MibTableColumn
cienaCesBenchmarkGenTestSessionPdvResultsSamples=_CienaCesBenchmarkGenTestSessionPdvResultsSamples_Object((1,3,6,1,4,1,1271,2,1,39,1,1,18,1,9),_CienaCesBenchmarkGenTestSessionPdvResultsSamples_Type())
cienaCesBenchmarkGenTestSessionPdvResultsSamples.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionPdvResultsSamples.setStatus(_A)
_CienaCesBenchmarkGenTestSessionPdvResultsKpiResult_Type=CienaCesBenchmarkKpiResult
_CienaCesBenchmarkGenTestSessionPdvResultsKpiResult_Object=MibTableColumn
cienaCesBenchmarkGenTestSessionPdvResultsKpiResult=_CienaCesBenchmarkGenTestSessionPdvResultsKpiResult_Object((1,3,6,1,4,1,1271,2,1,39,1,1,18,1,10),_CienaCesBenchmarkGenTestSessionPdvResultsKpiResult_Type())
cienaCesBenchmarkGenTestSessionPdvResultsKpiResult.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkGenTestSessionPdvResultsKpiResult.setStatus(_A)
_CienaCesBenchmarkEmixCharacterSetTable_Object=MibTable
cienaCesBenchmarkEmixCharacterSetTable=_CienaCesBenchmarkEmixCharacterSetTable_Object((1,3,6,1,4,1,1271,2,1,39,1,1,19))
if mibBuilder.loadTexts:cienaCesBenchmarkEmixCharacterSetTable.setStatus(_A)
_CienaCesBenchmarkEmixCharacterSetEntry_Object=MibTableRow
cienaCesBenchmarkEmixCharacterSetEntry=_CienaCesBenchmarkEmixCharacterSetEntry_Object((1,3,6,1,4,1,1271,2,1,39,1,1,19,1))
cienaCesBenchmarkEmixCharacterSetEntry.setIndexNames((0,_C,_A2))
if mibBuilder.loadTexts:cienaCesBenchmarkEmixCharacterSetEntry.setStatus(_A)
class _CienaCesBenchmarkEmixCharacterSetEntryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,26))
_CienaCesBenchmarkEmixCharacterSetEntryIndex_Type.__name__=_E
_CienaCesBenchmarkEmixCharacterSetEntryIndex_Object=MibTableColumn
cienaCesBenchmarkEmixCharacterSetEntryIndex=_CienaCesBenchmarkEmixCharacterSetEntryIndex_Object((1,3,6,1,4,1,1271,2,1,39,1,1,19,1,1),_CienaCesBenchmarkEmixCharacterSetEntryIndex_Type())
cienaCesBenchmarkEmixCharacterSetEntryIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cienaCesBenchmarkEmixCharacterSetEntryIndex.setStatus(_A)
class _CienaCesBenchmarkEmixCharacterSetEntryCharacter_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_CienaCesBenchmarkEmixCharacterSetEntryCharacter_Type.__name__=_I
_CienaCesBenchmarkEmixCharacterSetEntryCharacter_Object=MibTableColumn
cienaCesBenchmarkEmixCharacterSetEntryCharacter=_CienaCesBenchmarkEmixCharacterSetEntryCharacter_Object((1,3,6,1,4,1,1271,2,1,39,1,1,19,1,2),_CienaCesBenchmarkEmixCharacterSetEntryCharacter_Type())
cienaCesBenchmarkEmixCharacterSetEntryCharacter.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEmixCharacterSetEntryCharacter.setStatus(_A)
class _CienaCesBenchmarkEmixCharacterSetEntryFrameSize_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,6))
_CienaCesBenchmarkEmixCharacterSetEntryFrameSize_Type.__name__=_I
_CienaCesBenchmarkEmixCharacterSetEntryFrameSize_Object=MibTableColumn
cienaCesBenchmarkEmixCharacterSetEntryFrameSize=_CienaCesBenchmarkEmixCharacterSetEntryFrameSize_Object((1,3,6,1,4,1,1271,2,1,39,1,1,19,1,3),_CienaCesBenchmarkEmixCharacterSetEntryFrameSize_Type())
cienaCesBenchmarkEmixCharacterSetEntryFrameSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesBenchmarkEmixCharacterSetEntryFrameSize.setStatus(_A)
_CienaCesBenchmarkNotifications_ObjectIdentity=ObjectIdentity
cienaCesBenchmarkNotifications=_CienaCesBenchmarkNotifications_ObjectIdentity((1,3,6,1,4,1,1271,2,2,39))
cienaCesBenchmarkTestStarted=NotificationType((1,3,6,1,4,1,1271,2,2,39,1))
cienaCesBenchmarkTestStarted.setObjects(*((_G,_N),(_G,_M),(_C,_A3),(_C,_H),(_C,_O),(_C,_A4),(_C,_A5),(_C,_A6)))
if mibBuilder.loadTexts:cienaCesBenchmarkTestStarted.setStatus(_A)
cienaCesBenchmarkTestStopped=NotificationType((1,3,6,1,4,1,1271,2,2,39,2))
cienaCesBenchmarkTestStopped.setObjects(*((_G,_N),(_G,_M),(_C,_H),(_C,_O)))
if mibBuilder.loadTexts:cienaCesBenchmarkTestStopped.setStatus(_A)
cienaCesBenchmarkTestCompleted=NotificationType((1,3,6,1,4,1,1271,2,2,39,3))
cienaCesBenchmarkTestCompleted.setObjects(*((_G,_N),(_G,_M),(_C,_H),(_C,_O)))
if mibBuilder.loadTexts:cienaCesBenchmarkTestCompleted.setStatus(_A)
cienaCesBenchmarkTestFailedThroughputKpi=NotificationType((1,3,6,1,4,1,1271,2,2,39,4))
cienaCesBenchmarkTestFailedThroughputKpi.setObjects(*((_G,_N),(_G,_M),(_C,_H),(_C,_O),(_C,_Q),(_C,_W),(_C,_X),(_C,_Y),(_C,_P),(_C,_A7)))
if mibBuilder.loadTexts:cienaCesBenchmarkTestFailedThroughputKpi.setStatus(_A)
cienaCesBenchmarkTestFailedFramelossKpi=NotificationType((1,3,6,1,4,1,1271,2,2,39,5))
cienaCesBenchmarkTestFailedFramelossKpi.setObjects(*((_G,_N),(_G,_M),(_C,_H),(_C,_O),(_C,_Q),(_C,_W),(_C,_X),(_C,_Y),(_C,_P),(_C,_A8)))
if mibBuilder.loadTexts:cienaCesBenchmarkTestFailedFramelossKpi.setStatus(_A)
cienaCesBenchmarkTestFailedLatencyKpi=NotificationType((1,3,6,1,4,1,1271,2,2,39,6))
cienaCesBenchmarkTestFailedLatencyKpi.setObjects(*((_G,_N),(_G,_M),(_C,_H),(_C,_O),(_C,_Q),(_C,_W),(_C,_X),(_C,_Y),(_C,_P),(_C,_A9)))
if mibBuilder.loadTexts:cienaCesBenchmarkTestFailedLatencyKpi.setStatus(_A)
cienaCesBenchmarkTestFailedPdvKpi=NotificationType((1,3,6,1,4,1,1271,2,2,39,7))
cienaCesBenchmarkTestFailedPdvKpi.setObjects(*((_G,_N),(_G,_M),(_C,_H),(_C,_O),(_C,_Q),(_C,_W),(_C,_X),(_C,_Y),(_C,_P),(_C,_AA)))
if mibBuilder.loadTexts:cienaCesBenchmarkTestFailedPdvKpi.setStatus(_A)
cienaCesBenchmarkTestIterationCompleted=NotificationType((1,3,6,1,4,1,1271,2,2,39,8))
cienaCesBenchmarkTestIterationCompleted.setObjects(*((_G,_N),(_G,_M),(_C,_H),(_C,_O),(_C,_AB)))
if mibBuilder.loadTexts:cienaCesBenchmarkTestIterationCompleted.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'CienaCesBenchmarkLatencyPdvTestState':CienaCesBenchmarkLatencyPdvTestState,'CienaCesBenchmarkThroughputTestState':CienaCesBenchmarkThroughputTestState,'CienaCesBenchmarkFramelossTestState':CienaCesBenchmarkFramelossTestState,'CienaCesBenchmarkRfc2544TestState':CienaCesBenchmarkRfc2544TestState,'CienaCesBenchmarkY1564TestState':CienaCesBenchmarkY1564TestState,'CienaCesBenchmarkColorTest':CienaCesBenchmarkColorTest,'CienaCesBenchmarkKpiResult':CienaCesBenchmarkKpiResult,_f:CienaCesBenchmarkAdminState,'CienaCesBenchmarkThroughputKpiPercent':CienaCesBenchmarkThroughputKpiPercent,'CienaCesBenchmarkFramelossKpiPercent':CienaCesBenchmarkFramelossKpiPercent,'CienaCesBenchmarkThroughputResult':CienaCesBenchmarkThroughputResult,'CienaCesBenchmarkFramelossResult':CienaCesBenchmarkFramelossResult,'CienaCesBenchmarkPcpBitmap':CienaCesBenchmarkPcpBitmap,'cienaCesBenchmarkMIB':cienaCesBenchmarkMIB,'cienaCesBenchmarkMIBObjects':cienaCesBenchmarkMIBObjects,'cienaCesBenchmarkModule':cienaCesBenchmarkModule,'cienaCesBenchmarkGlobalObjects':cienaCesBenchmarkGlobalObjects,'cienaCesBenchmarkGlobalAdminState':cienaCesBenchmarkGlobalAdminState,'cienaCesBenchmarkGlobalGeneratorDefaultEmixSequenceId':cienaCesBenchmarkGlobalGeneratorDefaultEmixSequenceId,'cienaCesBenchmarkGlobalGeneratorDefaultKpiProfileId':cienaCesBenchmarkGlobalGeneratorDefaultKpiProfileId,'cienaCesBenchmarkGlobalGeneratorDefaultBwAllocProfileId':cienaCesBenchmarkGlobalGeneratorDefaultBwAllocProfileId,'cienaCesBenchmarkGlobalPlatformMaxConfigEntities':cienaCesBenchmarkGlobalPlatformMaxConfigEntities,'cienaCesBenchmarkGlobalPlatformMaxConfigTestInstances':cienaCesBenchmarkGlobalPlatformMaxConfigTestInstances,'cienaCesBenchmarkGlobalPlatformMaxConfigTestProfiles':cienaCesBenchmarkGlobalPlatformMaxConfigTestProfiles,'cienaCesBenchmarkGlobalPlatformMaxConfigKpiProfiles':cienaCesBenchmarkGlobalPlatformMaxConfigKpiProfiles,'cienaCesBenchmarkGlobalPlatformMaxConfigBwAllocProfiles':cienaCesBenchmarkGlobalPlatformMaxConfigBwAllocProfiles,'cienaCesBenchmarkGlobalPlatformMaxConfigEmixSequences':cienaCesBenchmarkGlobalPlatformMaxConfigEmixSequences,'cienaCesBenchmarkGlobalPlatformMaxSimultaneousRunningTests':cienaCesBenchmarkGlobalPlatformMaxSimultaneousRunningTests,'cienaCesBenchmarkGlobalConfiguredEntities':cienaCesBenchmarkGlobalConfiguredEntities,'cienaCesBenchmarkGlobalConfiguredTestInstances':cienaCesBenchmarkGlobalConfiguredTestInstances,'cienaCesBenchmarkGlobalConfiguredProfiles':cienaCesBenchmarkGlobalConfiguredProfiles,'cienaCesBenchmarkGlobalConfiguredEmixSequences':cienaCesBenchmarkGlobalConfiguredEmixSequences,'cienaCesBenchmarkGlobalConfiguredKpiProfiles':cienaCesBenchmarkGlobalConfiguredKpiProfiles,'cienaCesBenchmarkGlobalConfiguredBwAllocProfiles':cienaCesBenchmarkGlobalConfiguredBwAllocProfiles,'cienaCesBenchmarkGlobalEnabledTestInstances':cienaCesBenchmarkGlobalEnabledTestInstances,'cienaCesBenchmarkGlobalGeneratorRunningTestInstances':cienaCesBenchmarkGlobalGeneratorRunningTestInstances,'cienaCesBenchmarkEntityTable':cienaCesBenchmarkEntityTable,'cienaCesBenchmarkEntityEntry':cienaCesBenchmarkEntityEntry,_J:cienaCesBenchmarkEntityEntryId,'cienaCesBenchmarkEntityEntryName':cienaCesBenchmarkEntityEntryName,'cienaCesBenchmarkEntityEntryRole':cienaCesBenchmarkEntityEntryRole,_A3:cienaCesBenchmarkEntityEntryPortId,'cienaCesBenchmarkEntityEntryMode':cienaCesBenchmarkEntityEntryMode,'cienaCesBenchmarkEntityEntryAdminState':cienaCesBenchmarkEntityEntryAdminState,'cienaCesBenchmarkEntityEntryLocalMac':cienaCesBenchmarkEntityEntryLocalMac,'cienaCesBenchmarkEntityEntrySlotId':cienaCesBenchmarkEntityEntrySlotId,'cienaCesBenchmarkEntityEntryReflectorVendorType':cienaCesBenchmarkEntityEntryReflectorVendorType,'cienaCesBenchmarkEntityEntryReflectionLevel':cienaCesBenchmarkEntityEntryReflectionLevel,'cienaCesBenchmarkEntityEntryGeneratorHFrameSize':cienaCesBenchmarkEntityEntryGeneratorHFrameSize,'cienaCesBenchmarkEntityEntryMaxConfigTestInstances':cienaCesBenchmarkEntityEntryMaxConfigTestInstances,'cienaCesBenchmarkEntityEntryMaxSimultaneousTestInstances':cienaCesBenchmarkEntityEntryMaxSimultaneousTestInstances,'cienaCesBenchmarkEntityEntryOperEnabled':cienaCesBenchmarkEntityEntryOperEnabled,'cienaCesBenchmarkEntityEntryNumTestInstancesConfigured':cienaCesBenchmarkEntityEntryNumTestInstancesConfigured,'cienaCesBenchmarkEntityEntryNumTestInstancesEnabled':cienaCesBenchmarkEntityEntryNumTestInstancesEnabled,'cienaCesBenchmarkEntityEntryGenNumTestInstancesRunning':cienaCesBenchmarkEntityEntryGenNumTestInstancesRunning,'cienaCesBenchmarkEntityEntryBwAvailable':cienaCesBenchmarkEntityEntryBwAvailable,'cienaCesBenchmarkEntityEntryGenBwUsedByRunningTests':cienaCesBenchmarkEntityEntryGenBwUsedByRunningTests,'cienaCesBenchmarkEntityEntryAvailableHwSessions':cienaCesBenchmarkEntityEntryAvailableHwSessions,'cienaCesBenchmarkEntityEntryAllocatedHwSessions':cienaCesBenchmarkEntityEntryAllocatedHwSessions,'cienaCesBenchmarkEntityEntryRowStatus':cienaCesBenchmarkEntityEntryRowStatus,'cienaCesBenchmarkEntityEntryClearStats':cienaCesBenchmarkEntityEntryClearStats,'cienaCesBenchmarkEntityEntryReflectorMacValidation':cienaCesBenchmarkEntityEntryReflectorMacValidation,'cienaCesBenchmarkEntityStatsTable':cienaCesBenchmarkEntityStatsTable,'cienaCesBenchmarkEntityStatsEntry':cienaCesBenchmarkEntityStatsEntry,'cienaCesBenchmarkEntityStatsEntryClear':cienaCesBenchmarkEntityStatsEntryClear,'cienaCesBenchmarkEntityStatsEntryPortTxBytes':cienaCesBenchmarkEntityStatsEntryPortTxBytes,'cienaCesBenchmarkEntityStatsEntryPortTxPkts':cienaCesBenchmarkEntityStatsEntryPortTxPkts,'cienaCesBenchmarkEntityStatsEntryPortTxCrcErrorPkts':cienaCesBenchmarkEntityStatsEntryPortTxCrcErrorPkts,'cienaCesBenchmarkEntityStatsEntryPortTxUcastPkts':cienaCesBenchmarkEntityStatsEntryPortTxUcastPkts,'cienaCesBenchmarkEntityStatsEntryPortTxMcastPkts':cienaCesBenchmarkEntityStatsEntryPortTxMcastPkts,'cienaCesBenchmarkEntityStatsEntryPortTxBcastPkts':cienaCesBenchmarkEntityStatsEntryPortTxBcastPkts,'cienaCesBenchmarkEntityStatsEntryPortRxUndersizePkts':cienaCesBenchmarkEntityStatsEntryPortRxUndersizePkts,'cienaCesBenchmarkEntityStatsEntryPortRxOversizePkts':cienaCesBenchmarkEntityStatsEntryPortRxOversizePkts,'cienaCesBenchmarkEntityStatsEntryPortRxFragmentsPkts':cienaCesBenchmarkEntityStatsEntryPortRxFragmentsPkts,'cienaCesBenchmarkEntityStatsEntryPortRxJabbersPkts':cienaCesBenchmarkEntityStatsEntryPortRxJabbersPkts,'cienaCesBenchmarkEntityStatsEntryPortTxPausePkts':cienaCesBenchmarkEntityStatsEntryPortTxPausePkts,'cienaCesBenchmarkEntityStatsEntryPortTxDropPkts':cienaCesBenchmarkEntityStatsEntryPortTxDropPkts,'cienaCesBenchmarkEntityStatsEntryPortTxDiscardPkts':cienaCesBenchmarkEntityStatsEntryPortTxDiscardPkts,'cienaCesBenchmarkEntityStatsEntryPortTxLOutRangePkts':cienaCesBenchmarkEntityStatsEntryPortTxLOutRangePkts,'cienaCesBenchmarkEntityStatsEntryPortTx64OctsPkts':cienaCesBenchmarkEntityStatsEntryPortTx64OctsPkts,'cienaCesBenchmarkEntityStatsEntryPortTx65To127Pkts':cienaCesBenchmarkEntityStatsEntryPortTx65To127Pkts,'cienaCesBenchmarkEntityStatsEntryPortTx128To255Pkts':cienaCesBenchmarkEntityStatsEntryPortTx128To255Pkts,'cienaCesBenchmarkEntityStatsEntryPortTx256To511Pkts':cienaCesBenchmarkEntityStatsEntryPortTx256To511Pkts,'cienaCesBenchmarkEntityStatsEntryPortTx512To1023Pkts':cienaCesBenchmarkEntityStatsEntryPortTx512To1023Pkts,'cienaCesBenchmarkEntityStatsEntryPortTx1024To1518Pkts':cienaCesBenchmarkEntityStatsEntryPortTx1024To1518Pkts,'cienaCesBenchmarkEntityStatsEntryPortTx1519To2047Pkts':cienaCesBenchmarkEntityStatsEntryPortTx1519To2047Pkts,'cienaCesBenchmarkEntityStatsEntryPortTx2048To4095Pkts':cienaCesBenchmarkEntityStatsEntryPortTx2048To4095Pkts,'cienaCesBenchmarkEntityStatsEntryPortTx4096To9216Pkts':cienaCesBenchmarkEntityStatsEntryPortTx4096To9216Pkts,'cienaCesBenchmarkEntityStatsEntryPortRxBytes':cienaCesBenchmarkEntityStatsEntryPortRxBytes,'cienaCesBenchmarkEntityStatsEntryPortRxPkts':cienaCesBenchmarkEntityStatsEntryPortRxPkts,'cienaCesBenchmarkEntityStatsEntryPortRxExDeferPkts':cienaCesBenchmarkEntityStatsEntryPortRxExDeferPkts,'cienaCesBenchmarkEntityStatsEntryPortRxDeferPkts':cienaCesBenchmarkEntityStatsEntryPortRxDeferPkts,'cienaCesBenchmarkEntityStatsEntryPortRxGiantPkts':cienaCesBenchmarkEntityStatsEntryPortRxGiantPkts,'cienaCesBenchmarkEntityStatsEntryPortRxUnderRunPkts':cienaCesBenchmarkEntityStatsEntryPortRxUnderRunPkts,'cienaCesBenchmarkEntityStatsEntryPortRxCrcErrorPkts':cienaCesBenchmarkEntityStatsEntryPortRxCrcErrorPkts,'cienaCesBenchmarkEntityStatsEntryPortRxLCheckErrorPkts':cienaCesBenchmarkEntityStatsEntryPortRxLCheckErrorPkts,'cienaCesBenchmarkEntityStatsEntryPortRxLOutRangePkts':cienaCesBenchmarkEntityStatsEntryPortRxLOutRangePkts,'cienaCesBenchmarkEntityStatsEntryPortRxPausePkts':cienaCesBenchmarkEntityStatsEntryPortRxPausePkts,'cienaCesBenchmarkEntityStatsEntryPortRxUcastPkts':cienaCesBenchmarkEntityStatsEntryPortRxUcastPkts,'cienaCesBenchmarkEntityStatsEntryPortRxMcastPkts':cienaCesBenchmarkEntityStatsEntryPortRxMcastPkts,'cienaCesBenchmarkEntityStatsEntryPortRxBcastPkts':cienaCesBenchmarkEntityStatsEntryPortRxBcastPkts,'cienaCesBenchmarkEntityStatsEntryPortRx64OctsPkts':cienaCesBenchmarkEntityStatsEntryPortRx64OctsPkts,'cienaCesBenchmarkEntityStatsEntryPortRx65To127Pkts':cienaCesBenchmarkEntityStatsEntryPortRx65To127Pkts,'cienaCesBenchmarkEntityStatsEntryPortRx128To255Pkts':cienaCesBenchmarkEntityStatsEntryPortRx128To255Pkts,'cienaCesBenchmarkEntityStatsEntryPortRx256To511Pkts':cienaCesBenchmarkEntityStatsEntryPortRx256To511Pkts,'cienaCesBenchmarkEntityStatsEntryPortRx512To1023Pkts':cienaCesBenchmarkEntityStatsEntryPortRx512To1023Pkts,'cienaCesBenchmarkEntityStatsEntryPortRx1024To1518Pkts':cienaCesBenchmarkEntityStatsEntryPortRx1024To1518Pkts,'cienaCesBenchmarkEntityStatsEntryPortRx1519To2047Pkts':cienaCesBenchmarkEntityStatsEntryPortRx1519To2047Pkts,'cienaCesBenchmarkEntityStatsEntryPortRx2048To4095Pkts':cienaCesBenchmarkEntityStatsEntryPortRx2048To4095Pkts,'cienaCesBenchmarkEntityStatsEntryPortRx4096To9216Pkts':cienaCesBenchmarkEntityStatsEntryPortRx4096To9216Pkts,'cienaCesBenchmarkEntityStatsEntryFpgaMissClassPkts':cienaCesBenchmarkEntityStatsEntryFpgaMissClassPkts,'cienaCesBenchmarkEntityStatsEntryFpgaCrcErrPkts':cienaCesBenchmarkEntityStatsEntryFpgaCrcErrPkts,'cienaCesBenchmarkEntityStatsEntryFpgaUdpChkSumErrPkts':cienaCesBenchmarkEntityStatsEntryFpgaUdpChkSumErrPkts,'cienaCesBenchmarkEmixSequenceTable':cienaCesBenchmarkEmixSequenceTable,'cienaCesBenchmarkEmixSequenceEntry':cienaCesBenchmarkEmixSequenceEntry,_P:cienaCesBenchmarkEmixSequenceId,'cienaCesBenchmarkEmixSequenceName':cienaCesBenchmarkEmixSequenceName,'cienaCesBenchmarkEmixSequence':cienaCesBenchmarkEmixSequence,'cienaCesBenchmarkEmixSequenceUFrameSize':cienaCesBenchmarkEmixSequenceUFrameSize,'cienaCesBenchmarkEmixSequenceNumOfRef':cienaCesBenchmarkEmixSequenceNumOfRef,'cienaCesBenchmarkEmixSequenceUserCreated':cienaCesBenchmarkEmixSequenceUserCreated,'cienaCesBenchmarkEmixSequenceRowStatus':cienaCesBenchmarkEmixSequenceRowStatus,'cienaCesBenchmarkEmixFrameSizeTable':cienaCesBenchmarkEmixFrameSizeTable,'cienaCesBenchmarkEmixFrameSizeEntry':cienaCesBenchmarkEmixFrameSizeEntry,_g:cienaCesBenchmarkEmixFrameSizeIndex,'cienaCesBenchmarkEmixFrameSizeEntryFrameSize':cienaCesBenchmarkEmixFrameSizeEntryFrameSize,'cienaCesBenchmarkEmixAvgFrameSizeTable':cienaCesBenchmarkEmixAvgFrameSizeTable,'cienaCesBenchmarkEmixAvgFrameSizeEntry':cienaCesBenchmarkEmixAvgFrameSizeEntry,'cienaCesBenchmarkEmixAvgFrameSize':cienaCesBenchmarkEmixAvgFrameSize,'cienaCesBenchmarkKpiProfileTable':cienaCesBenchmarkKpiProfileTable,'cienaCesBenchmarkKpiProfileEntry':cienaCesBenchmarkKpiProfileEntry,_Q:cienaCesBenchmarkKpiProfileId,'cienaCesBenchmarkKpiProfileName':cienaCesBenchmarkKpiProfileName,'cienaCesBenchmarkKpiProfileNumOfRef':cienaCesBenchmarkKpiProfileNumOfRef,'cienaCesBenchmarkKpiProfileRowStatus':cienaCesBenchmarkKpiProfileRowStatus,'cienaCesBenchmarkKpiPcpColorTable':cienaCesBenchmarkKpiPcpColorTable,'cienaCesBenchmarkKpiPcpColorEntry':cienaCesBenchmarkKpiPcpColorEntry,_h:cienaCesBenchmarkKpiPcpIndex,_i:cienaCesBenchmarkKpiColorIndex,_W:cienaCesBenchmarkKpiPcp,_X:cienaCesBenchmarkKpiColor,'cienaCesBenchmarkKpiThroughput':cienaCesBenchmarkKpiThroughput,'cienaCesBenchmarkKpiFrameloss':cienaCesBenchmarkKpiFrameloss,'cienaCesBenchmarkKpiLatency':cienaCesBenchmarkKpiLatency,'cienaCesBenchmarkKpiPdv':cienaCesBenchmarkKpiPdv,'cienaCesBenchmarkBwAllocProfileTable':cienaCesBenchmarkBwAllocProfileTable,'cienaCesBenchmarkBwAllocProfileEntry':cienaCesBenchmarkBwAllocProfileEntry,_b:cienaCesBenchmarkBwAllocProfileId,'cienaCesBenchmarkBwAllocProfileName':cienaCesBenchmarkBwAllocProfileName,'cienaCesBenchmarkBwAllocProfileNumOfRef':cienaCesBenchmarkBwAllocProfileNumOfRef,'cienaCesBenchmarkBwAllocProfileRowStatus':cienaCesBenchmarkBwAllocProfileRowStatus,'cienaCesBenchmarkBwRatioTable':cienaCesBenchmarkBwRatioTable,'cienaCesBenchmarkBwRatioEntry':cienaCesBenchmarkBwRatioEntry,_k:cienaCesBenchmarkBwRatioPcpIndex,'cienaCesBenchmarkBwRatioPcp':cienaCesBenchmarkBwRatioPcp,'cienaCesBenchmarkBwRatio':cienaCesBenchmarkBwRatio,'cienaCesBenchmarkProfileTable':cienaCesBenchmarkProfileTable,'cienaCesBenchmarkProfileEntry':cienaCesBenchmarkProfileEntry,_l:cienaCesBenchmarkProfileEntryId,'cienaCesBenchmarkProfileEntryName':cienaCesBenchmarkProfileEntryName,'cienaCesBenchmarkProfileEntryBandwidth':cienaCesBenchmarkProfileEntryBandwidth,'cienaCesBenchmarkProfileEntryExcessBandwidth':cienaCesBenchmarkProfileEntryExcessBandwidth,'cienaCesBenchmarkProfileEntryInterval':cienaCesBenchmarkProfileEntryInterval,'cienaCesBenchmarkProfileEntryDuration':cienaCesBenchmarkProfileEntryDuration,'cienaCesBenchmarkProfileEntrySetFrameSizeList':cienaCesBenchmarkProfileEntrySetFrameSizeList,'cienaCesBenchmarkProfileEntryMaxSearches':cienaCesBenchmarkProfileEntryMaxSearches,'cienaCesBenchmarkProfileEntryMaxSamples':cienaCesBenchmarkProfileEntryMaxSamples,'cienaCesBenchmarkProfileEntrySamplingInterval':cienaCesBenchmarkProfileEntrySamplingInterval,'cienaCesBenchmarkProfileEntryFrameLossStartBw':cienaCesBenchmarkProfileEntryFrameLossStartBw,'cienaCesBenchmarkProfileEntryVidValidation':cienaCesBenchmarkProfileEntryVidValidation,'cienaCesBenchmarkProfileEntryPcpValidation':cienaCesBenchmarkProfileEntryPcpValidation,'cienaCesBenchmarkProfileEntryColorValidation':cienaCesBenchmarkProfileEntryColorValidation,'cienaCesBenchmarkProfileEntryKpiProfileId':cienaCesBenchmarkProfileEntryKpiProfileId,'cienaCesBenchmarkProfileEntryBwAllocProfileId':cienaCesBenchmarkProfileEntryBwAllocProfileId,'cienaCesBenchmarkProfileEntryEmixSequenceId':cienaCesBenchmarkProfileEntryEmixSequenceId,'cienaCesBenchmarkProfileEntryEncapType':cienaCesBenchmarkProfileEntryEncapType,'cienaCesBenchmarkProfileEntryPduType':cienaCesBenchmarkProfileEntryPduType,'cienaCesBenchmarkProfileEntryDstmac':cienaCesBenchmarkProfileEntryDstmac,'cienaCesBenchmarkProfileEntrySVid':cienaCesBenchmarkProfileEntrySVid,'cienaCesBenchmarkProfileEntrySPcp':cienaCesBenchmarkProfileEntrySPcp,'cienaCesBenchmarkProfileEntrySColor':cienaCesBenchmarkProfileEntrySColor,'cienaCesBenchmarkProfileEntryCVid':cienaCesBenchmarkProfileEntryCVid,'cienaCesBenchmarkProfileEntryCPcp':cienaCesBenchmarkProfileEntryCPcp,'cienaCesBenchmarkProfileEntryCColor':cienaCesBenchmarkProfileEntryCColor,'cienaCesBenchmarkProfileEntryTpid':cienaCesBenchmarkProfileEntryTpid,'cienaCesBenchmarkProfileEntryDscp':cienaCesBenchmarkProfileEntryDscp,'cienaCesBenchmarkProfileEntrySrcInetAddrType':cienaCesBenchmarkProfileEntrySrcInetAddrType,'cienaCesBenchmarkProfileEntrySrcInetAddr':cienaCesBenchmarkProfileEntrySrcInetAddr,'cienaCesBenchmarkProfileEntryDstInetAddrType':cienaCesBenchmarkProfileEntryDstInetAddrType,'cienaCesBenchmarkProfileEntryDstInetAddr':cienaCesBenchmarkProfileEntryDstInetAddr,'cienaCesBenchmarkProfileEntryCustomPayload':cienaCesBenchmarkProfileEntryCustomPayload,'cienaCesBenchmarkProfileEntryThroughputTest':cienaCesBenchmarkProfileEntryThroughputTest,'cienaCesBenchmarkProfileEntryFramelossTest':cienaCesBenchmarkProfileEntryFramelossTest,'cienaCesBenchmarkProfileEntryLatencyTest':cienaCesBenchmarkProfileEntryLatencyTest,'cienaCesBenchmarkProfileEntryPdvTest':cienaCesBenchmarkProfileEntryPdvTest,'cienaCesBenchmarkProfileEntryBurstTest':cienaCesBenchmarkProfileEntryBurstTest,'cienaCesBenchmarkProfileEntryRfc2544Suite':cienaCesBenchmarkProfileEntryRfc2544Suite,'cienaCesBenchmarkProfileEntryY1564Test':cienaCesBenchmarkProfileEntryY1564Test,'cienaCesBenchmarkProfileEntryHwSessionsRequired':cienaCesBenchmarkProfileEntryHwSessionsRequired,'cienaCesBenchmarkProfileEntryNumOfRef':cienaCesBenchmarkProfileEntryNumOfRef,'cienaCesBenchmarkProfileEntryRowStatus':cienaCesBenchmarkProfileEntryRowStatus,'cienaCesBenchmarkTestInstanceTable':cienaCesBenchmarkTestInstanceTable,'cienaCesBenchmarkTestInstanceEntry':cienaCesBenchmarkTestInstanceEntry,_H:cienaCesBenchmarkTestInstanceEntryId,_O:cienaCesBenchmarkTestInstanceEntryName,'cienaCesBenchmarkTestInstanceEntrySubPortId':cienaCesBenchmarkTestInstanceEntrySubPortId,'cienaCesBenchmarkTestInstanceEntryProfileId':cienaCesBenchmarkTestInstanceEntryProfileId,_A4:cienaCesBenchmarkTestInstanceEntrySvid,_A5:cienaCesBenchmarkTestInstanceEntryCvid,'cienaCesBenchmarkTestInstanceEntryUntagged':cienaCesBenchmarkTestInstanceEntryUntagged,_A6:cienaCesBenchmarkTestInstanceEntryDstMac,'cienaCesBenchmarkTestInstanceEntryAdminState':cienaCesBenchmarkTestInstanceEntryAdminState,'cienaCesBenchmarkTestInstanceEntryStarted':cienaCesBenchmarkTestInstanceEntryStarted,'cienaCesBenchmarkTestInstanceEntryCurrentInterval':cienaCesBenchmarkTestInstanceEntryCurrentInterval,'cienaCesBenchmarkTestInstanceEntryTotalIntervals':cienaCesBenchmarkTestInstanceEntryTotalIntervals,'cienaCesBenchmarkTestInstanceEntryLastIterStart':cienaCesBenchmarkTestInstanceEntryLastIterStart,'cienaCesBenchmarkTestInstanceEntryClearStats':cienaCesBenchmarkTestInstanceEntryClearStats,'cienaCesBenchmarkTestInstanceEntryRowStatus':cienaCesBenchmarkTestInstanceEntryRowStatus,'cienaCesBenchmarkTestInstanceEntryAssocEntityId':cienaCesBenchmarkTestInstanceEntryAssocEntityId,'cienaCesBenchmarkTestInstanceEntryOperState':cienaCesBenchmarkTestInstanceEntryOperState,'cienaCesBenchmarkTestInstanceEntryConnectivityTest':cienaCesBenchmarkTestInstanceEntryConnectivityTest,'cienaCesBenchmarkGenTestSessionAllocationTable':cienaCesBenchmarkGenTestSessionAllocationTable,'cienaCesBenchmarkGenTestSessionAllocationEntry':cienaCesBenchmarkGenTestSessionAllocationEntry,_n:cienaCesBenchmarkGenTestSessionPcpIndex,_o:cienaCesBenchmarkGenTestSessionColorIndex,'cienaCesBenchmarkGenTestSessionPcp':cienaCesBenchmarkGenTestSessionPcp,'cienaCesBenchmarkGenTestSessionColor':cienaCesBenchmarkGenTestSessionColor,'cienaCesBenchmarkGenTestSessionId':cienaCesBenchmarkGenTestSessionId,'cienaCesBenchmarkGenTestSessionEmixSequenceId':cienaCesBenchmarkGenTestSessionEmixSequenceId,_Y:cienaCesBenchmarkGenTestSessionCurrentPktSize,'cienaCesBenchmarkGenTestSessionThroughputTestState':cienaCesBenchmarkGenTestSessionThroughputTestState,'cienaCesBenchmarkGenTestSessionFramelossTestState':cienaCesBenchmarkGenTestSessionFramelossTestState,'cienaCesBenchmarkGenTestSessionLatencyTestState':cienaCesBenchmarkGenTestSessionLatencyTestState,'cienaCesBenchmarkGenTestSessionPdvTestState':cienaCesBenchmarkGenTestSessionPdvTestState,'cienaCesBenchmarkGenTestSessionRfc2544TestState':cienaCesBenchmarkGenTestSessionRfc2544TestState,'cienaCesBenchmarkGenTestSessionY1564TestState':cienaCesBenchmarkGenTestSessionY1564TestState,'cienaCesBenchmarkGenTestSessionCurrentRate':cienaCesBenchmarkGenTestSessionCurrentRate,'cienaCesBenchmarkGenTestSessionSamplesCompleted':cienaCesBenchmarkGenTestSessionSamplesCompleted,'cienaCesBenchmarkTestInstanceStatsTable':cienaCesBenchmarkTestInstanceStatsTable,'cienaCesBenchmarkTestInstanceStatsEntry':cienaCesBenchmarkTestInstanceStatsEntry,'cienaCesBenchmarkTestInstanceStatsRxPkts':cienaCesBenchmarkTestInstanceStatsRxPkts,'cienaCesBenchmarkTestInstanceStatsRxIpv4Pkts':cienaCesBenchmarkTestInstanceStatsRxIpv4Pkts,'cienaCesBenchmarkTestInstanceStatsRxIpv4UdpPkts':cienaCesBenchmarkTestInstanceStatsRxIpv4UdpPkts,'cienaCesBenchmarkTestInstanceStatsRxIpv6Pkts':cienaCesBenchmarkTestInstanceStatsRxIpv6Pkts,'cienaCesBenchmarkTestInstanceStatsRxIpv6UdpPkts':cienaCesBenchmarkTestInstanceStatsRxIpv6UdpPkts,'cienaCesBenchmarkTestInstanceStatsRxNonIpPkts':cienaCesBenchmarkTestInstanceStatsRxNonIpPkts,'cienaCesBenchmarkTestInstanceStatsRxUnrecognizedPkts':cienaCesBenchmarkTestInstanceStatsRxUnrecognizedPkts,'cienaCesBenchmarkTestInstanceStatsRxDuplicatePkts':cienaCesBenchmarkTestInstanceStatsRxDuplicatePkts,'cienaCesBenchmarkTestInstanceStatsRxDuplicatePktsOverflow':cienaCesBenchmarkTestInstanceStatsRxDuplicatePktsOverflow,'cienaCesBenchmarkTestInstanceStatsRxOOOPkts':cienaCesBenchmarkTestInstanceStatsRxOOOPkts,'cienaCesBenchmarkTestInstanceStatsRxOOOPktsOverflow':cienaCesBenchmarkTestInstanceStatsRxOOOPktsOverflow,'cienaCesBenchmarkTestInstanceStatsRxDiscSeqNumPkts':cienaCesBenchmarkTestInstanceStatsRxDiscSeqNumPkts,'cienaCesBenchmarkTestInstanceStatsRxDiscSeqNumPktsOverflow':cienaCesBenchmarkTestInstanceStatsRxDiscSeqNumPktsOverflow,'cienaCesBenchmarkTestInstanceStatsRxUdpCheckSumPkts':cienaCesBenchmarkTestInstanceStatsRxUdpCheckSumPkts,'cienaCesBenchmarkTestInstanceStatsTxPkts':cienaCesBenchmarkTestInstanceStatsTxPkts,'cienaCesBenchmarkGenTestSessionThroughputResultsTable':cienaCesBenchmarkGenTestSessionThroughputResultsTable,'cienaCesBenchmarkGenTestSessionThroughputResultsEntry':cienaCesBenchmarkGenTestSessionThroughputResultsEntry,_p:cienaCesBenchmarkGenTestSessionThroughputResultsPcpIndex,_q:cienaCesBenchmarkGenTestSessionThroughputResultsColorIndex,_r:cienaCesBenchmarkGenTestSessionThroughputResultsFrameSizeIndex,'cienaCesBenchmarkGenTestSessionThroughputResultsPcp':cienaCesBenchmarkGenTestSessionThroughputResultsPcp,'cienaCesBenchmarkGenTestSessionThroughputResultsColor':cienaCesBenchmarkGenTestSessionThroughputResultsColor,'cienaCesBenchmarkGenTestSessionThroughputResultsFrameSize':cienaCesBenchmarkGenTestSessionThroughputResultsFrameSize,'cienaCesBenchmarkGenTestSessionThroughputResultsEmixSequenceId':cienaCesBenchmarkGenTestSessionThroughputResultsEmixSequenceId,'cienaCesBenchmarkGenTestSessionThroughputResultsMin':cienaCesBenchmarkGenTestSessionThroughputResultsMin,_A7:cienaCesBenchmarkGenTestSessionThroughputResultsMax,'cienaCesBenchmarkGenTestSessionThroughputResultsAvg':cienaCesBenchmarkGenTestSessionThroughputResultsAvg,_AB:cienaCesBenchmarkGenTestSessionThroughputResultsIterations,'cienaCesBenchmarkGenTestSessionThroughputResultsKpiResult':cienaCesBenchmarkGenTestSessionThroughputResultsKpiResult,'cienaCesBenchmarkGenTestSessionFramelossResultsTable':cienaCesBenchmarkGenTestSessionFramelossResultsTable,'cienaCesBenchmarkGenTestSessionFramelossResultsEntry':cienaCesBenchmarkGenTestSessionFramelossResultsEntry,_s:cienaCesBenchmarkGenTestSessionFramelossResultsPcpIndex,_t:cienaCesBenchmarkGenTestSessionFramelossResultsColorIndex,_u:cienaCesBenchmarkGenTestSessionFramelossResultsFrameSizeIndex,_v:cienaCesBenchmarkGenTestSessionFramelossResultsRateIndex,'cienaCesBenchmarkGenTestSessionFramelossResultsPcp':cienaCesBenchmarkGenTestSessionFramelossResultsPcp,'cienaCesBenchmarkGenTestSessionFramelossResultsColor':cienaCesBenchmarkGenTestSessionFramelossResultsColor,'cienaCesBenchmarkGenTestSessionFramelossResultsFrameSize':cienaCesBenchmarkGenTestSessionFramelossResultsFrameSize,'cienaCesBenchmarkGenTestSessionFramelossResultsEmixSequenceId':cienaCesBenchmarkGenTestSessionFramelossResultsEmixSequenceId,'cienaCesBenchmarkGenTestSessionFramelossResultsRate':cienaCesBenchmarkGenTestSessionFramelossResultsRate,'cienaCesBenchmarkGenTestSessionFramelossResultsFirst':cienaCesBenchmarkGenTestSessionFramelossResultsFirst,'cienaCesBenchmarkGenTestSessionFramelossResultsSecond':cienaCesBenchmarkGenTestSessionFramelossResultsSecond,'cienaCesBenchmarkGenTestSessionFramelossResultsKpiResult':cienaCesBenchmarkGenTestSessionFramelossResultsKpiResult,_A8:cienaCesBenchmarkGenTestSessionFramelossResultsResult,'cienaCesBenchmarkGenTestSessionLatencyResultsTable':cienaCesBenchmarkGenTestSessionLatencyResultsTable,'cienaCesBenchmarkGenTestSessionLatencyResultsEntry':cienaCesBenchmarkGenTestSessionLatencyResultsEntry,_w:cienaCesBenchmarkGenTestSessionLatencyResultsPcpIndex,_x:cienaCesBenchmarkGenTestSessionLatencyResultsColorIndex,_y:cienaCesBenchmarkGenTestSessionLatencyResultsFrameSizeIndex,'cienaCesBenchmarkGenTestSessionLatencyResultsPcp':cienaCesBenchmarkGenTestSessionLatencyResultsPcp,'cienaCesBenchmarkGenTestSessionLatencyResultsColor':cienaCesBenchmarkGenTestSessionLatencyResultsColor,'cienaCesBenchmarkGenTestSessionLatencyResultsFrameSize':cienaCesBenchmarkGenTestSessionLatencyResultsFrameSize,'cienaCesBenchmarkGenTestSessionLatencyResultsEmixSequenceId':cienaCesBenchmarkGenTestSessionLatencyResultsEmixSequenceId,'cienaCesBenchmarkGenTestSessionLatencyResultsMin':cienaCesBenchmarkGenTestSessionLatencyResultsMin,_A9:cienaCesBenchmarkGenTestSessionLatencyResultsMax,'cienaCesBenchmarkGenTestSessionLatencyResultsAvg':cienaCesBenchmarkGenTestSessionLatencyResultsAvg,'cienaCesBenchmarkGenTestSessionLatencyResultsSamples':cienaCesBenchmarkGenTestSessionLatencyResultsSamples,'cienaCesBenchmarkGenTestSessionLatencyResultsKpiResult':cienaCesBenchmarkGenTestSessionLatencyResultsKpiResult,'cienaCesBenchmarkGenTestSessionPdvResultsTable':cienaCesBenchmarkGenTestSessionPdvResultsTable,'cienaCesBenchmarkGenTestSessionPdvResultsEntry':cienaCesBenchmarkGenTestSessionPdvResultsEntry,_z:cienaCesBenchmarkGenTestSessionPdvResultsPcpIndex,_A0:cienaCesBenchmarkGenTestSessionPdvResultsColorIndex,_A1:cienaCesBenchmarkGenTestSessionPdvResultsFrameSizeIndex,'cienaCesBenchmarkGenTestSessionPdvResultsPcp':cienaCesBenchmarkGenTestSessionPdvResultsPcp,'cienaCesBenchmarkGenTestSessionPdvResultsColor':cienaCesBenchmarkGenTestSessionPdvResultsColor,'cienaCesBenchmarkGenTestSessionPdvResultsFrameSize':cienaCesBenchmarkGenTestSessionPdvResultsFrameSize,'cienaCesBenchmarkGenTestSessionPdvResultsEmixSequenceId':cienaCesBenchmarkGenTestSessionPdvResultsEmixSequenceId,_AA:cienaCesBenchmarkGenTestSessionPdvResultsAvg,'cienaCesBenchmarkGenTestSessionPdvResultsSamples':cienaCesBenchmarkGenTestSessionPdvResultsSamples,'cienaCesBenchmarkGenTestSessionPdvResultsKpiResult':cienaCesBenchmarkGenTestSessionPdvResultsKpiResult,'cienaCesBenchmarkEmixCharacterSetTable':cienaCesBenchmarkEmixCharacterSetTable,'cienaCesBenchmarkEmixCharacterSetEntry':cienaCesBenchmarkEmixCharacterSetEntry,_A2:cienaCesBenchmarkEmixCharacterSetEntryIndex,'cienaCesBenchmarkEmixCharacterSetEntryCharacter':cienaCesBenchmarkEmixCharacterSetEntryCharacter,'cienaCesBenchmarkEmixCharacterSetEntryFrameSize':cienaCesBenchmarkEmixCharacterSetEntryFrameSize,'cienaCesBenchmarkNotifications':cienaCesBenchmarkNotifications,'cienaCesBenchmarkTestStarted':cienaCesBenchmarkTestStarted,'cienaCesBenchmarkTestStopped':cienaCesBenchmarkTestStopped,'cienaCesBenchmarkTestCompleted':cienaCesBenchmarkTestCompleted,'cienaCesBenchmarkTestFailedThroughputKpi':cienaCesBenchmarkTestFailedThroughputKpi,'cienaCesBenchmarkTestFailedFramelossKpi':cienaCesBenchmarkTestFailedFramelossKpi,'cienaCesBenchmarkTestFailedLatencyKpi':cienaCesBenchmarkTestFailedLatencyKpi,'cienaCesBenchmarkTestFailedPdvKpi':cienaCesBenchmarkTestFailedPdvKpi,'cienaCesBenchmarkTestIterationCompleted':cienaCesBenchmarkTestIterationCompleted})