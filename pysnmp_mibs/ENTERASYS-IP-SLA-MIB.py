_As='etsysIpSlaRttGroup'
_Ar='etsysIpSlaPathGroup'
_Aq='etsysIpSlaCollectionGroup'
_Ap='etsysIpSlaConfigGroup'
_Ao='etsysIpSlaDistMaxRange'
_An='etsysIpSlaDistMinRange'
_Am='etsysIpSlaPdvDataSumSquareOneWayDS'
_Al='etsysIpSlaPdvDataSumOneWayDS'
_Ak='etsysIpSlaPdvDataMaxOneWayDS'
_Aj='etsysIpSlaPdvDataMinOneWayDS'
_Ai='etsysIpSlaPdvDataNumOneWayDS'
_Ah='etsysIpSlaPdvDataSumSquareOneWaySD'
_Ag='etsysIpSlaPdvDataSumOneWaySD'
_Af='etsysIpSlaPdvDataMaxOneWaySD'
_Ae='etsysIpSlaPdvDataMinOneWaySD'
_Ad='etsysIpSlaPdvDataNumOneWaySD'
_Ac='etsysIpSlaPdvDataSumSquareNegativeDS'
_Ab='etsysIpSlaPdvDataSumNegativeDS'
_Aa='etsysIpSlaPdvDataNumNegativeDS'
_AZ='etsysIpSlaPdvDataMaxNegativeDS'
_AY='etsysIpSlaPdvDataMinNegativeDS'
_AX='etsysIpSlaPdvDataSumSquarePositiveDS'
_AW='etsysIpSlaPdvDataSumPositiveDS'
_AV='etsysIpSlaPdvDataNumPositiveDS'
_AU='etsysIpSlaPdvDataMaxPositiveDS'
_AT='etsysIpSlaPdvDataMinPositiveDS'
_AS='etsysIpSlaPdvDataSumSquareNegativeSD'
_AR='etsysIpSlaPdvDataSumNegativeSD'
_AQ='etsysIpSlaPdvDataNumNegativeSD'
_AP='etsysIpSlaPdvDataMaxNegativeSD'
_AO='etsysIpSlaPdvDataMinNegativeSD'
_AN='etsysIpSlaPdvDataSumSquarePositiveSD'
_AM='etsysIpSlaPdvDataSumPositiveSD'
_AL='etsysIpSlaPdvDataNumPositiveSD'
_AK='etsysIpSlaPdvDataMaxPositiveSD'
_AJ='etsysIpSlaPdvDataMinPositiveSD'
_AI='etsysIpSlaPdvDataSamples'
_AH='etsysIpSlaRttDataTxErrors'
_AG='etsysIpSlaRttDataPktVlanPcpMismatch'
_AF='etsysIpSlaRttDataPktIpTosMismatch'
_AE='etsysIpSlaRttDataPktMissing'
_AD='etsysIpSlaRttDataPktLateArrival'
_AC='etsysIpSlaRttDataPktOutOfOrder'
_AB='etsysIpSlaRttDataSumSquareHigh'
_AA='etsysIpSlaRttDataSumSquareLow'
_A9='etsysIpSlaRttDataSum'
_A8='etsysIpSlaRttDataMaxDelay'
_A7='etsysIpSlaRttDataAvgDelay'
_A6='etsysIpSlaRttDataMinDelay'
_A5='etsysIpSlaRttDataSamples'
_A4='etsysIpSlaBucketTime'
_A3='etsysIpSlaHopDestAddr'
_A2='etsysIpSlaHopDestType'
_A1='etsysIpslaCollectionNumHops'
_A0='etsysIpSlaCollectionNumPaths'
_z='etsysIpSlaCollectionStartTime'
_y='etsysIpSlaScheduleTestStatus'
_x='etsysIpSlaScheduleTestState'
_w='etsysIpSlaScheduleTestFrequency'
_v='etsysIpSlaScheduleTestDuration'
_u='etsysIpSlaScheduleTestRepetitions'
_t='etsysIpSlaScheduleRecurrence'
_s='etsysIpSlaScheduleStartTime'
_r='etsysIpSlaConfigStatus'
_q='etsysIpSlaConfigStatisticsCollections'
_p='etsysIpSlaConfigDistributionInterval'
_o='etsysIpSlaConfigDistributionCount'
_n='etsysIpSlaConfigHistoryWrap'
_m='etsysIpSlaConfigHistoryAgeout'
_l='etsysIpSlaConfigHistoryInterval'
_k='etsysIpSlaConfigHistorySamples'
_j='etsysIpSlaConfigHistoryBucketType'
_i='etsysIpSlaConfigHistoryBuckets'
_h='etsysIpSlaConfigHistoryCollections'
_g='etsysIpSlaConfigHopCount'
_f='etsysIpSlaConfigPathCount'
_e='etsysIpSlaConfigProbeName'
_d='etsysIpSlaConfigDestPort'
_c='etsysIpSlaConfigDestAddr'
_b='etsysIpSlaConfigDestType'
_a='etsysIpSlaConfigType'
_Z='etsysIpSlaDataEntriesInUse'
_Y='etsysIpSlaMaxDataEntries'
_X='etsysIpSlaEntriesInUse'
_W='etsysIpSlaMaxEntries'
_V='InetPortNumber'
_U='InetAddressType'
_T='InetAddress'
_S='milliseconds'
_R='SnmpAdminString'
_Q='etsysIpSlaBucketIndex'
_P='seconds'
_O='etsysIpSlaHopIndex'
_N='etsysIpSlaPathIndex'
_M='read-write'
_L='microseconds'
_K='packets'
_J='etsysIpSlaCollectionIndex'
_I='etsysIpSlaCollectionType'
_H='not-accessible'
_G='Integer32'
_F='etsysIpSlaConfigIndex'
_E='Unsigned32'
_D='read-create'
_C='read-only'
_B='current'
_A='ENTERASYS-IP-SLA-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB',_T,_U,_V)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_R)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
etsysIpSlaMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,94))
if mibBuilder.loadTexts:etsysIpSlaMIB.setRevisions(('2013-02-06 18:26',))
_EtsysIpSla_ObjectIdentity=ObjectIdentity
etsysIpSla=_EtsysIpSla_ObjectIdentity((1,3,6,1,4,1,5624,1,2,94,1))
_EtsysIpSlaGlobals_ObjectIdentity=ObjectIdentity
etsysIpSlaGlobals=_EtsysIpSlaGlobals_ObjectIdentity((1,3,6,1,4,1,5624,1,2,94,1,1))
_EtsysIpSlaMaxEntries_Type=Unsigned32
_EtsysIpSlaMaxEntries_Object=MibScalar
etsysIpSlaMaxEntries=_EtsysIpSlaMaxEntries_Object((1,3,6,1,4,1,5624,1,2,94,1,1,1),_EtsysIpSlaMaxEntries_Type())
etsysIpSlaMaxEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysIpSlaMaxEntries.setStatus(_B)
_EtsysIpSlaEntriesInUse_Type=Gauge32
_EtsysIpSlaEntriesInUse_Object=MibScalar
etsysIpSlaEntriesInUse=_EtsysIpSlaEntriesInUse_Object((1,3,6,1,4,1,5624,1,2,94,1,1,2),_EtsysIpSlaEntriesInUse_Type())
etsysIpSlaEntriesInUse.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysIpSlaEntriesInUse.setStatus(_B)
_EtsysIpSlaMaxDataEntries_Type=Unsigned32
_EtsysIpSlaMaxDataEntries_Object=MibScalar
etsysIpSlaMaxDataEntries=_EtsysIpSlaMaxDataEntries_Object((1,3,6,1,4,1,5624,1,2,94,1,1,3),_EtsysIpSlaMaxDataEntries_Type())
etsysIpSlaMaxDataEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysIpSlaMaxDataEntries.setStatus(_B)
_EtsysIpSlaDataEntriesInUse_Type=Gauge32
_EtsysIpSlaDataEntriesInUse_Object=MibScalar
etsysIpSlaDataEntriesInUse=_EtsysIpSlaDataEntriesInUse_Object((1,3,6,1,4,1,5624,1,2,94,1,1,4),_EtsysIpSlaDataEntriesInUse_Type())
etsysIpSlaDataEntriesInUse.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysIpSlaDataEntriesInUse.setStatus(_B)
_EtsysIpSlaTables_ObjectIdentity=ObjectIdentity
etsysIpSlaTables=_EtsysIpSlaTables_ObjectIdentity((1,3,6,1,4,1,5624,1,2,94,1,2))
_EtsysIpSlaConfigTable_Object=MibTable
etsysIpSlaConfigTable=_EtsysIpSlaConfigTable_Object((1,3,6,1,4,1,5624,1,2,94,1,2,1))
if mibBuilder.loadTexts:etsysIpSlaConfigTable.setStatus(_B)
_EtsysIpSlaConfigEntry_Object=MibTableRow
etsysIpSlaConfigEntry=_EtsysIpSlaConfigEntry_Object((1,3,6,1,4,1,5624,1,2,94,1,2,1,1))
etsysIpSlaConfigEntry.setIndexNames((0,_A,_F))
if mibBuilder.loadTexts:etsysIpSlaConfigEntry.setStatus(_B)
_EtsysIpSlaConfigIndex_Type=Unsigned32
_EtsysIpSlaConfigIndex_Object=MibTableColumn
etsysIpSlaConfigIndex=_EtsysIpSlaConfigIndex_Object((1,3,6,1,4,1,5624,1,2,94,1,2,1,1,1),_EtsysIpSlaConfigIndex_Type())
etsysIpSlaConfigIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:etsysIpSlaConfigIndex.setStatus(_B)
class _EtsysIpSlaConfigType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('echo',1),('jitter',2)))
_EtsysIpSlaConfigType_Type.__name__=_G
_EtsysIpSlaConfigType_Object=MibTableColumn
etsysIpSlaConfigType=_EtsysIpSlaConfigType_Object((1,3,6,1,4,1,5624,1,2,94,1,2,1,1,2),_EtsysIpSlaConfigType_Type())
etsysIpSlaConfigType.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysIpSlaConfigType.setStatus(_B)
class _EtsysIpSlaConfigDestType_Type(InetAddressType):defaultValue=0
_EtsysIpSlaConfigDestType_Type.__name__=_U
_EtsysIpSlaConfigDestType_Object=MibTableColumn
etsysIpSlaConfigDestType=_EtsysIpSlaConfigDestType_Object((1,3,6,1,4,1,5624,1,2,94,1,2,1,1,3),_EtsysIpSlaConfigDestType_Type())
etsysIpSlaConfigDestType.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysIpSlaConfigDestType.setStatus(_B)
class _EtsysIpSlaConfigDestAddr_Type(InetAddress):defaultValue=OctetString('')
_EtsysIpSlaConfigDestAddr_Type.__name__=_T
_EtsysIpSlaConfigDestAddr_Object=MibTableColumn
etsysIpSlaConfigDestAddr=_EtsysIpSlaConfigDestAddr_Object((1,3,6,1,4,1,5624,1,2,94,1,2,1,1,4),_EtsysIpSlaConfigDestAddr_Type())
etsysIpSlaConfigDestAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysIpSlaConfigDestAddr.setStatus(_B)
class _EtsysIpSlaConfigDestPort_Type(InetPortNumber):defaultValue=0
_EtsysIpSlaConfigDestPort_Type.__name__=_V
_EtsysIpSlaConfigDestPort_Object=MibTableColumn
etsysIpSlaConfigDestPort=_EtsysIpSlaConfigDestPort_Object((1,3,6,1,4,1,5624,1,2,94,1,2,1,1,5),_EtsysIpSlaConfigDestPort_Type())
etsysIpSlaConfigDestPort.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysIpSlaConfigDestPort.setStatus(_B)
class _EtsysIpSlaConfigProbeName_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_EtsysIpSlaConfigProbeName_Type.__name__=_R
_EtsysIpSlaConfigProbeName_Object=MibTableColumn
etsysIpSlaConfigProbeName=_EtsysIpSlaConfigProbeName_Object((1,3,6,1,4,1,5624,1,2,94,1,2,1,1,6),_EtsysIpSlaConfigProbeName_Type())
etsysIpSlaConfigProbeName.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysIpSlaConfigProbeName.setStatus(_B)
class _EtsysIpSlaConfigPathCount_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_EtsysIpSlaConfigPathCount_Type.__name__=_E
_EtsysIpSlaConfigPathCount_Object=MibTableColumn
etsysIpSlaConfigPathCount=_EtsysIpSlaConfigPathCount_Object((1,3,6,1,4,1,5624,1,2,94,1,2,1,1,7),_EtsysIpSlaConfigPathCount_Type())
etsysIpSlaConfigPathCount.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysIpSlaConfigPathCount.setStatus(_B)
if mibBuilder.loadTexts:etsysIpSlaConfigPathCount.setUnits('paths')
class _EtsysIpSlaConfigHopCount_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_EtsysIpSlaConfigHopCount_Type.__name__=_E
_EtsysIpSlaConfigHopCount_Object=MibTableColumn
etsysIpSlaConfigHopCount=_EtsysIpSlaConfigHopCount_Object((1,3,6,1,4,1,5624,1,2,94,1,2,1,1,8),_EtsysIpSlaConfigHopCount_Type())
etsysIpSlaConfigHopCount.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysIpSlaConfigHopCount.setStatus(_B)
if mibBuilder.loadTexts:etsysIpSlaConfigHopCount.setUnits('hops')
class _EtsysIpSlaConfigHistoryCollections_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_EtsysIpSlaConfigHistoryCollections_Type.__name__=_E
_EtsysIpSlaConfigHistoryCollections_Object=MibTableColumn
etsysIpSlaConfigHistoryCollections=_EtsysIpSlaConfigHistoryCollections_Object((1,3,6,1,4,1,5624,1,2,94,1,2,1,1,9),_EtsysIpSlaConfigHistoryCollections_Type())
etsysIpSlaConfigHistoryCollections.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysIpSlaConfigHistoryCollections.setStatus(_B)
class _EtsysIpSlaConfigHistoryBuckets_Type(Unsigned32):defaultValue=15;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_EtsysIpSlaConfigHistoryBuckets_Type.__name__=_E
_EtsysIpSlaConfigHistoryBuckets_Object=MibTableColumn
etsysIpSlaConfigHistoryBuckets=_EtsysIpSlaConfigHistoryBuckets_Object((1,3,6,1,4,1,5624,1,2,94,1,2,1,1,10),_EtsysIpSlaConfigHistoryBuckets_Type())
etsysIpSlaConfigHistoryBuckets.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysIpSlaConfigHistoryBuckets.setStatus(_B)
class _EtsysIpSlaConfigHistoryBucketType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('static',1),('timed',2)))
_EtsysIpSlaConfigHistoryBucketType_Type.__name__=_G
_EtsysIpSlaConfigHistoryBucketType_Object=MibTableColumn
etsysIpSlaConfigHistoryBucketType=_EtsysIpSlaConfigHistoryBucketType_Object((1,3,6,1,4,1,5624,1,2,94,1,2,1,1,11),_EtsysIpSlaConfigHistoryBucketType_Type())
etsysIpSlaConfigHistoryBucketType.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysIpSlaConfigHistoryBucketType.setStatus(_B)
class _EtsysIpSlaConfigHistorySamples_Type(Unsigned32):defaultValue=16;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,512))
_EtsysIpSlaConfigHistorySamples_Type.__name__=_E
_EtsysIpSlaConfigHistorySamples_Object=MibTableColumn
etsysIpSlaConfigHistorySamples=_EtsysIpSlaConfigHistorySamples_Object((1,3,6,1,4,1,5624,1,2,94,1,2,1,1,12),_EtsysIpSlaConfigHistorySamples_Type())
etsysIpSlaConfigHistorySamples.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysIpSlaConfigHistorySamples.setStatus(_B)
class _EtsysIpSlaConfigHistoryInterval_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,3600))
_EtsysIpSlaConfigHistoryInterval_Type.__name__=_E
_EtsysIpSlaConfigHistoryInterval_Object=MibTableColumn
etsysIpSlaConfigHistoryInterval=_EtsysIpSlaConfigHistoryInterval_Object((1,3,6,1,4,1,5624,1,2,94,1,2,1,1,13),_EtsysIpSlaConfigHistoryInterval_Type())
etsysIpSlaConfigHistoryInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysIpSlaConfigHistoryInterval.setStatus(_B)
if mibBuilder.loadTexts:etsysIpSlaConfigHistoryInterval.setUnits(_P)
class _EtsysIpSlaConfigHistoryAgeout_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(15,7200))
_EtsysIpSlaConfigHistoryAgeout_Type.__name__=_E
_EtsysIpSlaConfigHistoryAgeout_Object=MibTableColumn
etsysIpSlaConfigHistoryAgeout=_EtsysIpSlaConfigHistoryAgeout_Object((1,3,6,1,4,1,5624,1,2,94,1,2,1,1,14),_EtsysIpSlaConfigHistoryAgeout_Type())
etsysIpSlaConfigHistoryAgeout.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysIpSlaConfigHistoryAgeout.setStatus(_B)
if mibBuilder.loadTexts:etsysIpSlaConfigHistoryAgeout.setUnits('minutes')
class _EtsysIpSlaConfigHistoryWrap_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('wrap',1),('noWrap',2)))
_EtsysIpSlaConfigHistoryWrap_Type.__name__=_G
_EtsysIpSlaConfigHistoryWrap_Object=MibTableColumn
etsysIpSlaConfigHistoryWrap=_EtsysIpSlaConfigHistoryWrap_Object((1,3,6,1,4,1,5624,1,2,94,1,2,1,1,15),_EtsysIpSlaConfigHistoryWrap_Type())
etsysIpSlaConfigHistoryWrap.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysIpSlaConfigHistoryWrap.setStatus(_B)
class _EtsysIpSlaConfigDistributionCount_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(2,5))
_EtsysIpSlaConfigDistributionCount_Type.__name__=_E
_EtsysIpSlaConfigDistributionCount_Object=MibTableColumn
etsysIpSlaConfigDistributionCount=_EtsysIpSlaConfigDistributionCount_Object((1,3,6,1,4,1,5624,1,2,94,1,2,1,1,16),_EtsysIpSlaConfigDistributionCount_Type())
etsysIpSlaConfigDistributionCount.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysIpSlaConfigDistributionCount.setStatus(_B)
class _EtsysIpSlaConfigDistributionInterval_Type(Unsigned32):defaultValue=25;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,1000))
_EtsysIpSlaConfigDistributionInterval_Type.__name__=_E
_EtsysIpSlaConfigDistributionInterval_Object=MibTableColumn
etsysIpSlaConfigDistributionInterval=_EtsysIpSlaConfigDistributionInterval_Object((1,3,6,1,4,1,5624,1,2,94,1,2,1,1,17),_EtsysIpSlaConfigDistributionInterval_Type())
etsysIpSlaConfigDistributionInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysIpSlaConfigDistributionInterval.setStatus(_B)
if mibBuilder.loadTexts:etsysIpSlaConfigDistributionInterval.setUnits(_S)
class _EtsysIpSlaConfigStatisticsCollections_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_EtsysIpSlaConfigStatisticsCollections_Type.__name__=_E
_EtsysIpSlaConfigStatisticsCollections_Object=MibTableColumn
etsysIpSlaConfigStatisticsCollections=_EtsysIpSlaConfigStatisticsCollections_Object((1,3,6,1,4,1,5624,1,2,94,1,2,1,1,18),_EtsysIpSlaConfigStatisticsCollections_Type())
etsysIpSlaConfigStatisticsCollections.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysIpSlaConfigStatisticsCollections.setStatus(_B)
_EtsysIpSlaConfigStatus_Type=RowStatus
_EtsysIpSlaConfigStatus_Object=MibTableColumn
etsysIpSlaConfigStatus=_EtsysIpSlaConfigStatus_Object((1,3,6,1,4,1,5624,1,2,94,1,2,1,1,19),_EtsysIpSlaConfigStatus_Type())
etsysIpSlaConfigStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysIpSlaConfigStatus.setStatus(_B)
_EtsysIpSlaScheduleTable_Object=MibTable
etsysIpSlaScheduleTable=_EtsysIpSlaScheduleTable_Object((1,3,6,1,4,1,5624,1,2,94,1,2,2))
if mibBuilder.loadTexts:etsysIpSlaScheduleTable.setStatus(_B)
_EtsysIpSlaScheduleEntry_Object=MibTableRow
etsysIpSlaScheduleEntry=_EtsysIpSlaScheduleEntry_Object((1,3,6,1,4,1,5624,1,2,94,1,2,2,1))
etsysIpSlaScheduleEntry.setIndexNames((0,_A,_F))
if mibBuilder.loadTexts:etsysIpSlaScheduleEntry.setStatus(_B)
class _EtsysIpSlaScheduleStartTime_Type(Unsigned32):defaultValue=0
_EtsysIpSlaScheduleStartTime_Type.__name__=_E
_EtsysIpSlaScheduleStartTime_Object=MibTableColumn
etsysIpSlaScheduleStartTime=_EtsysIpSlaScheduleStartTime_Object((1,3,6,1,4,1,5624,1,2,94,1,2,2,1,1),_EtsysIpSlaScheduleStartTime_Type())
etsysIpSlaScheduleStartTime.setMaxAccess(_M)
if mibBuilder.loadTexts:etsysIpSlaScheduleStartTime.setStatus(_B)
class _EtsysIpSlaScheduleRecurrence_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(120,7776000))
_EtsysIpSlaScheduleRecurrence_Type.__name__=_E
_EtsysIpSlaScheduleRecurrence_Object=MibTableColumn
etsysIpSlaScheduleRecurrence=_EtsysIpSlaScheduleRecurrence_Object((1,3,6,1,4,1,5624,1,2,94,1,2,2,1,2),_EtsysIpSlaScheduleRecurrence_Type())
etsysIpSlaScheduleRecurrence.setMaxAccess(_M)
if mibBuilder.loadTexts:etsysIpSlaScheduleRecurrence.setStatus(_B)
if mibBuilder.loadTexts:etsysIpSlaScheduleRecurrence.setUnits(_P)
class _EtsysIpSlaScheduleTestRepetitions_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_EtsysIpSlaScheduleTestRepetitions_Type.__name__=_E
_EtsysIpSlaScheduleTestRepetitions_Object=MibTableColumn
etsysIpSlaScheduleTestRepetitions=_EtsysIpSlaScheduleTestRepetitions_Object((1,3,6,1,4,1,5624,1,2,94,1,2,2,1,3),_EtsysIpSlaScheduleTestRepetitions_Type())
etsysIpSlaScheduleTestRepetitions.setMaxAccess(_M)
if mibBuilder.loadTexts:etsysIpSlaScheduleTestRepetitions.setStatus(_B)
class _EtsysIpSlaScheduleTestDuration_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,3600))
_EtsysIpSlaScheduleTestDuration_Type.__name__=_E
_EtsysIpSlaScheduleTestDuration_Object=MibTableColumn
etsysIpSlaScheduleTestDuration=_EtsysIpSlaScheduleTestDuration_Object((1,3,6,1,4,1,5624,1,2,94,1,2,2,1,4),_EtsysIpSlaScheduleTestDuration_Type())
etsysIpSlaScheduleTestDuration.setMaxAccess(_M)
if mibBuilder.loadTexts:etsysIpSlaScheduleTestDuration.setStatus(_B)
if mibBuilder.loadTexts:etsysIpSlaScheduleTestDuration.setUnits(_P)
class _EtsysIpSlaScheduleTestFrequency_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,3600))
_EtsysIpSlaScheduleTestFrequency_Type.__name__=_E
_EtsysIpSlaScheduleTestFrequency_Object=MibTableColumn
etsysIpSlaScheduleTestFrequency=_EtsysIpSlaScheduleTestFrequency_Object((1,3,6,1,4,1,5624,1,2,94,1,2,2,1,5),_EtsysIpSlaScheduleTestFrequency_Type())
etsysIpSlaScheduleTestFrequency.setMaxAccess(_M)
if mibBuilder.loadTexts:etsysIpSlaScheduleTestFrequency.setStatus(_B)
if mibBuilder.loadTexts:etsysIpSlaScheduleTestFrequency.setUnits(_P)
class _EtsysIpSlaScheduleTestState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('inactive',1),('complete',2),('running',3),('queued',4)))
_EtsysIpSlaScheduleTestState_Type.__name__=_G
_EtsysIpSlaScheduleTestState_Object=MibTableColumn
etsysIpSlaScheduleTestState=_EtsysIpSlaScheduleTestState_Object((1,3,6,1,4,1,5624,1,2,94,1,2,2,1,6),_EtsysIpSlaScheduleTestState_Type())
etsysIpSlaScheduleTestState.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysIpSlaScheduleTestState.setStatus(_B)
class _EtsysIpSlaScheduleTestStatus_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_EtsysIpSlaScheduleTestStatus_Type.__name__=_R
_EtsysIpSlaScheduleTestStatus_Object=MibTableColumn
etsysIpSlaScheduleTestStatus=_EtsysIpSlaScheduleTestStatus_Object((1,3,6,1,4,1,5624,1,2,94,1,2,2,1,7),_EtsysIpSlaScheduleTestStatus_Type())
etsysIpSlaScheduleTestStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysIpSlaScheduleTestStatus.setStatus(_B)
_EtsysIpSlaCollectionTable_Object=MibTable
etsysIpSlaCollectionTable=_EtsysIpSlaCollectionTable_Object((1,3,6,1,4,1,5624,1,2,94,1,2,3))
if mibBuilder.loadTexts:etsysIpSlaCollectionTable.setStatus(_B)
_EtsysIpSlaCollectionEntry_Object=MibTableRow
etsysIpSlaCollectionEntry=_EtsysIpSlaCollectionEntry_Object((1,3,6,1,4,1,5624,1,2,94,1,2,3,1))
etsysIpSlaCollectionEntry.setIndexNames((0,_A,_F),(0,_A,_I),(0,_A,_J))
if mibBuilder.loadTexts:etsysIpSlaCollectionEntry.setStatus(_B)
class _EtsysIpSlaCollectionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('summary',1),('distribution',2),('history',3)))
_EtsysIpSlaCollectionType_Type.__name__=_G
_EtsysIpSlaCollectionType_Object=MibTableColumn
etsysIpSlaCollectionType=_EtsysIpSlaCollectionType_Object((1,3,6,1,4,1,5624,1,2,94,1,2,3,1,1),_EtsysIpSlaCollectionType_Type())
etsysIpSlaCollectionType.setMaxAccess(_H)
if mibBuilder.loadTexts:etsysIpSlaCollectionType.setStatus(_B)
_EtsysIpSlaCollectionIndex_Type=Unsigned32
_EtsysIpSlaCollectionIndex_Object=MibTableColumn
etsysIpSlaCollectionIndex=_EtsysIpSlaCollectionIndex_Object((1,3,6,1,4,1,5624,1,2,94,1,2,3,1,2),_EtsysIpSlaCollectionIndex_Type())
etsysIpSlaCollectionIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:etsysIpSlaCollectionIndex.setStatus(_B)
_EtsysIpSlaCollectionStartTime_Type=Unsigned32
_EtsysIpSlaCollectionStartTime_Object=MibTableColumn
etsysIpSlaCollectionStartTime=_EtsysIpSlaCollectionStartTime_Object((1,3,6,1,4,1,5624,1,2,94,1,2,3,1,3),_EtsysIpSlaCollectionStartTime_Type())
etsysIpSlaCollectionStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysIpSlaCollectionStartTime.setStatus(_B)
_EtsysIpSlaCollectionNumPaths_Type=Gauge32
_EtsysIpSlaCollectionNumPaths_Object=MibTableColumn
etsysIpSlaCollectionNumPaths=_EtsysIpSlaCollectionNumPaths_Object((1,3,6,1,4,1,5624,1,2,94,1,2,3,1,4),_EtsysIpSlaCollectionNumPaths_Type())
etsysIpSlaCollectionNumPaths.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysIpSlaCollectionNumPaths.setStatus(_B)
_EtsysIpslaCollectionNumHops_Type=Gauge32
_EtsysIpslaCollectionNumHops_Object=MibTableColumn
etsysIpslaCollectionNumHops=_EtsysIpslaCollectionNumHops_Object((1,3,6,1,4,1,5624,1,2,94,1,2,3,1,5),_EtsysIpslaCollectionNumHops_Type())
etsysIpslaCollectionNumHops.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysIpslaCollectionNumHops.setStatus(_B)
_EtsysIpSlaPathTable_Object=MibTable
etsysIpSlaPathTable=_EtsysIpSlaPathTable_Object((1,3,6,1,4,1,5624,1,2,94,1,2,4))
if mibBuilder.loadTexts:etsysIpSlaPathTable.setStatus(_B)
_EtsysIpSlaPathEntry_Object=MibTableRow
etsysIpSlaPathEntry=_EtsysIpSlaPathEntry_Object((1,3,6,1,4,1,5624,1,2,94,1,2,4,1))
etsysIpSlaPathEntry.setIndexNames((0,_A,_F),(0,_A,_I),(0,_A,_J),(0,_A,_N),(0,_A,_O))
if mibBuilder.loadTexts:etsysIpSlaPathEntry.setStatus(_B)
_EtsysIpSlaPathIndex_Type=Unsigned32
_EtsysIpSlaPathIndex_Object=MibTableColumn
etsysIpSlaPathIndex=_EtsysIpSlaPathIndex_Object((1,3,6,1,4,1,5624,1,2,94,1,2,4,1,1),_EtsysIpSlaPathIndex_Type())
etsysIpSlaPathIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:etsysIpSlaPathIndex.setStatus(_B)
_EtsysIpSlaHopIndex_Type=Unsigned32
_EtsysIpSlaHopIndex_Object=MibTableColumn
etsysIpSlaHopIndex=_EtsysIpSlaHopIndex_Object((1,3,6,1,4,1,5624,1,2,94,1,2,4,1,2),_EtsysIpSlaHopIndex_Type())
etsysIpSlaHopIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:etsysIpSlaHopIndex.setStatus(_B)
_EtsysIpSlaHopDestType_Type=InetAddressType
_EtsysIpSlaHopDestType_Object=MibTableColumn
etsysIpSlaHopDestType=_EtsysIpSlaHopDestType_Object((1,3,6,1,4,1,5624,1,2,94,1,2,4,1,3),_EtsysIpSlaHopDestType_Type())
etsysIpSlaHopDestType.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysIpSlaHopDestType.setStatus(_B)
_EtsysIpSlaHopDestAddr_Type=InetAddress
_EtsysIpSlaHopDestAddr_Object=MibTableColumn
etsysIpSlaHopDestAddr=_EtsysIpSlaHopDestAddr_Object((1,3,6,1,4,1,5624,1,2,94,1,2,4,1,4),_EtsysIpSlaHopDestAddr_Type())
etsysIpSlaHopDestAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysIpSlaHopDestAddr.setStatus(_B)
_EtsysIpSlaRttDataTable_Object=MibTable
etsysIpSlaRttDataTable=_EtsysIpSlaRttDataTable_Object((1,3,6,1,4,1,5624,1,2,94,1,2,5))
if mibBuilder.loadTexts:etsysIpSlaRttDataTable.setStatus(_B)
_EtsysIpSlaRttDataEntry_Object=MibTableRow
etsysIpSlaRttDataEntry=_EtsysIpSlaRttDataEntry_Object((1,3,6,1,4,1,5624,1,2,94,1,2,5,1))
etsysIpSlaRttDataEntry.setIndexNames((0,_A,_F),(0,_A,_I),(0,_A,_J),(0,_A,_N),(0,_A,_O),(0,_A,_Q))
if mibBuilder.loadTexts:etsysIpSlaRttDataEntry.setStatus(_B)
_EtsysIpSlaBucketIndex_Type=Unsigned32
_EtsysIpSlaBucketIndex_Object=MibTableColumn
etsysIpSlaBucketIndex=_EtsysIpSlaBucketIndex_Object((1,3,6,1,4,1,5624,1,2,94,1,2,5,1,1),_EtsysIpSlaBucketIndex_Type())
etsysIpSlaBucketIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:etsysIpSlaBucketIndex.setStatus(_B)
_EtsysIpSlaBucketTime_Type=Unsigned32
_EtsysIpSlaBucketTime_Object=MibTableColumn
etsysIpSlaBucketTime=_EtsysIpSlaBucketTime_Object((1,3,6,1,4,1,5624,1,2,94,1,2,5,1,2),_EtsysIpSlaBucketTime_Type())
etsysIpSlaBucketTime.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysIpSlaBucketTime.setStatus(_B)
_EtsysIpSlaRttDataSamples_Type=Gauge32
_EtsysIpSlaRttDataSamples_Object=MibTableColumn
etsysIpSlaRttDataSamples=_EtsysIpSlaRttDataSamples_Object((1,3,6,1,4,1,5624,1,2,94,1,2,5,1,3),_EtsysIpSlaRttDataSamples_Type())
etsysIpSlaRttDataSamples.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysIpSlaRttDataSamples.setStatus(_B)
if mibBuilder.loadTexts:etsysIpSlaRttDataSamples.setUnits(_K)
_EtsysIpSlaRttDataMinDelay_Type=Gauge32
_EtsysIpSlaRttDataMinDelay_Object=MibTableColumn
etsysIpSlaRttDataMinDelay=_EtsysIpSlaRttDataMinDelay_Object((1,3,6,1,4,1,5624,1,2,94,1,2,5,1,4),_EtsysIpSlaRttDataMinDelay_Type())
etsysIpSlaRttDataMinDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysIpSlaRttDataMinDelay.setStatus(_B)
if mibBuilder.loadTexts:etsysIpSlaRttDataMinDelay.setUnits(_L)
_EtsysIpSlaRttDataAvgDelay_Type=Gauge32
_EtsysIpSlaRttDataAvgDelay_Object=MibTableColumn
etsysIpSlaRttDataAvgDelay=_EtsysIpSlaRttDataAvgDelay_Object((1,3,6,1,4,1,5624,1,2,94,1,2,5,1,5),_EtsysIpSlaRttDataAvgDelay_Type())
etsysIpSlaRttDataAvgDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysIpSlaRttDataAvgDelay.setStatus(_B)
if mibBuilder.loadTexts:etsysIpSlaRttDataAvgDelay.setUnits(_L)
_EtsysIpSlaRttDataMaxDelay_Type=Gauge32
_EtsysIpSlaRttDataMaxDelay_Object=MibTableColumn
etsysIpSlaRttDataMaxDelay=_EtsysIpSlaRttDataMaxDelay_Object((1,3,6,1,4,1,5624,1,2,94,1,2,5,1,6),_EtsysIpSlaRttDataMaxDelay_Type())
etsysIpSlaRttDataMaxDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysIpSlaRttDataMaxDelay.setStatus(_B)
if mibBuilder.loadTexts:etsysIpSlaRttDataMaxDelay.setUnits(_L)
_EtsysIpSlaRttDataSum_Type=Gauge32
_EtsysIpSlaRttDataSum_Object=MibTableColumn
etsysIpSlaRttDataSum=_EtsysIpSlaRttDataSum_Object((1,3,6,1,4,1,5624,1,2,94,1,2,5,1,7),_EtsysIpSlaRttDataSum_Type())
etsysIpSlaRttDataSum.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysIpSlaRttDataSum.setStatus(_B)
if mibBuilder.loadTexts:etsysIpSlaRttDataSum.setUnits(_L)
_EtsysIpSlaRttDataSumSquareLow_Type=Gauge32
_EtsysIpSlaRttDataSumSquareLow_Object=MibTableColumn
etsysIpSlaRttDataSumSquareLow=_EtsysIpSlaRttDataSumSquareLow_Object((1,3,6,1,4,1,5624,1,2,94,1,2,5,1,8),_EtsysIpSlaRttDataSumSquareLow_Type())
etsysIpSlaRttDataSumSquareLow.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysIpSlaRttDataSumSquareLow.setStatus(_B)
if mibBuilder.loadTexts:etsysIpSlaRttDataSumSquareLow.setUnits(_L)
_EtsysIpSlaRttDataSumSquareHigh_Type=Gauge32
_EtsysIpSlaRttDataSumSquareHigh_Object=MibTableColumn
etsysIpSlaRttDataSumSquareHigh=_EtsysIpSlaRttDataSumSquareHigh_Object((1,3,6,1,4,1,5624,1,2,94,1,2,5,1,9),_EtsysIpSlaRttDataSumSquareHigh_Type())
etsysIpSlaRttDataSumSquareHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysIpSlaRttDataSumSquareHigh.setStatus(_B)
if mibBuilder.loadTexts:etsysIpSlaRttDataSumSquareHigh.setUnits(_L)
_EtsysIpSlaRttDataPktOutOfOrder_Type=Gauge32
_EtsysIpSlaRttDataPktOutOfOrder_Object=MibTableColumn
etsysIpSlaRttDataPktOutOfOrder=_EtsysIpSlaRttDataPktOutOfOrder_Object((1,3,6,1,4,1,5624,1,2,94,1,2,5,1,10),_EtsysIpSlaRttDataPktOutOfOrder_Type())
etsysIpSlaRttDataPktOutOfOrder.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysIpSlaRttDataPktOutOfOrder.setStatus(_B)
if mibBuilder.loadTexts:etsysIpSlaRttDataPktOutOfOrder.setUnits(_K)
_EtsysIpSlaRttDataPktLateArrival_Type=Gauge32
_EtsysIpSlaRttDataPktLateArrival_Object=MibTableColumn
etsysIpSlaRttDataPktLateArrival=_EtsysIpSlaRttDataPktLateArrival_Object((1,3,6,1,4,1,5624,1,2,94,1,2,5,1,11),_EtsysIpSlaRttDataPktLateArrival_Type())
etsysIpSlaRttDataPktLateArrival.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysIpSlaRttDataPktLateArrival.setStatus(_B)
if mibBuilder.loadTexts:etsysIpSlaRttDataPktLateArrival.setUnits(_K)
_EtsysIpSlaRttDataPktMissing_Type=Gauge32
_EtsysIpSlaRttDataPktMissing_Object=MibTableColumn
etsysIpSlaRttDataPktMissing=_EtsysIpSlaRttDataPktMissing_Object((1,3,6,1,4,1,5624,1,2,94,1,2,5,1,12),_EtsysIpSlaRttDataPktMissing_Type())
etsysIpSlaRttDataPktMissing.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysIpSlaRttDataPktMissing.setStatus(_B)
if mibBuilder.loadTexts:etsysIpSlaRttDataPktMissing.setUnits(_K)
_EtsysIpSlaRttDataPktIpTosMismatch_Type=Gauge32
_EtsysIpSlaRttDataPktIpTosMismatch_Object=MibTableColumn
etsysIpSlaRttDataPktIpTosMismatch=_EtsysIpSlaRttDataPktIpTosMismatch_Object((1,3,6,1,4,1,5624,1,2,94,1,2,5,1,13),_EtsysIpSlaRttDataPktIpTosMismatch_Type())
etsysIpSlaRttDataPktIpTosMismatch.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysIpSlaRttDataPktIpTosMismatch.setStatus(_B)
if mibBuilder.loadTexts:etsysIpSlaRttDataPktIpTosMismatch.setUnits(_K)
_EtsysIpSlaRttDataPktVlanPcpMismatch_Type=Gauge32
_EtsysIpSlaRttDataPktVlanPcpMismatch_Object=MibTableColumn
etsysIpSlaRttDataPktVlanPcpMismatch=_EtsysIpSlaRttDataPktVlanPcpMismatch_Object((1,3,6,1,4,1,5624,1,2,94,1,2,5,1,14),_EtsysIpSlaRttDataPktVlanPcpMismatch_Type())
etsysIpSlaRttDataPktVlanPcpMismatch.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysIpSlaRttDataPktVlanPcpMismatch.setStatus(_B)
if mibBuilder.loadTexts:etsysIpSlaRttDataPktVlanPcpMismatch.setUnits(_K)
_EtsysIpSlaRttDataTxErrors_Type=Gauge32
_EtsysIpSlaRttDataTxErrors_Object=MibTableColumn
etsysIpSlaRttDataTxErrors=_EtsysIpSlaRttDataTxErrors_Object((1,3,6,1,4,1,5624,1,2,94,1,2,5,1,15),_EtsysIpSlaRttDataTxErrors_Type())
etsysIpSlaRttDataTxErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysIpSlaRttDataTxErrors.setStatus(_B)
_EtsysIpSlaPdvDataTable_Object=MibTable
etsysIpSlaPdvDataTable=_EtsysIpSlaPdvDataTable_Object((1,3,6,1,4,1,5624,1,2,94,1,2,6))
if mibBuilder.loadTexts:etsysIpSlaPdvDataTable.setStatus(_B)
_EtsysIpSlaPdvDataEntry_Object=MibTableRow
etsysIpSlaPdvDataEntry=_EtsysIpSlaPdvDataEntry_Object((1,3,6,1,4,1,5624,1,2,94,1,2,6,1))
etsysIpSlaPdvDataEntry.setIndexNames((0,_A,_F),(0,_A,_I),(0,_A,_J),(0,_A,_N),(0,_A,_O),(0,_A,_Q))
if mibBuilder.loadTexts:etsysIpSlaPdvDataEntry.setStatus(_B)
_EtsysIpSlaPdvDataSamples_Type=Gauge32
_EtsysIpSlaPdvDataSamples_Object=MibTableColumn
etsysIpSlaPdvDataSamples=_EtsysIpSlaPdvDataSamples_Object((1,3,6,1,4,1,5624,1,2,94,1,2,6,1,1),_EtsysIpSlaPdvDataSamples_Type())
etsysIpSlaPdvDataSamples.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysIpSlaPdvDataSamples.setStatus(_B)
_EtsysIpSlaPdvDataMinPositiveSD_Type=Gauge32
_EtsysIpSlaPdvDataMinPositiveSD_Object=MibTableColumn
etsysIpSlaPdvDataMinPositiveSD=_EtsysIpSlaPdvDataMinPositiveSD_Object((1,3,6,1,4,1,5624,1,2,94,1,2,6,1,2),_EtsysIpSlaPdvDataMinPositiveSD_Type())
etsysIpSlaPdvDataMinPositiveSD.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysIpSlaPdvDataMinPositiveSD.setStatus(_B)
_EtsysIpSlaPdvDataMaxPositiveSD_Type=Gauge32
_EtsysIpSlaPdvDataMaxPositiveSD_Object=MibTableColumn
etsysIpSlaPdvDataMaxPositiveSD=_EtsysIpSlaPdvDataMaxPositiveSD_Object((1,3,6,1,4,1,5624,1,2,94,1,2,6,1,3),_EtsysIpSlaPdvDataMaxPositiveSD_Type())
etsysIpSlaPdvDataMaxPositiveSD.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysIpSlaPdvDataMaxPositiveSD.setStatus(_B)
_EtsysIpSlaPdvDataNumPositiveSD_Type=Gauge32
_EtsysIpSlaPdvDataNumPositiveSD_Object=MibTableColumn
etsysIpSlaPdvDataNumPositiveSD=_EtsysIpSlaPdvDataNumPositiveSD_Object((1,3,6,1,4,1,5624,1,2,94,1,2,6,1,4),_EtsysIpSlaPdvDataNumPositiveSD_Type())
etsysIpSlaPdvDataNumPositiveSD.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysIpSlaPdvDataNumPositiveSD.setStatus(_B)
_EtsysIpSlaPdvDataSumPositiveSD_Type=Gauge32
_EtsysIpSlaPdvDataSumPositiveSD_Object=MibTableColumn
etsysIpSlaPdvDataSumPositiveSD=_EtsysIpSlaPdvDataSumPositiveSD_Object((1,3,6,1,4,1,5624,1,2,94,1,2,6,1,5),_EtsysIpSlaPdvDataSumPositiveSD_Type())
etsysIpSlaPdvDataSumPositiveSD.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysIpSlaPdvDataSumPositiveSD.setStatus(_B)
_EtsysIpSlaPdvDataSumSquarePositiveSD_Type=Gauge32
_EtsysIpSlaPdvDataSumSquarePositiveSD_Object=MibTableColumn
etsysIpSlaPdvDataSumSquarePositiveSD=_EtsysIpSlaPdvDataSumSquarePositiveSD_Object((1,3,6,1,4,1,5624,1,2,94,1,2,6,1,6),_EtsysIpSlaPdvDataSumSquarePositiveSD_Type())
etsysIpSlaPdvDataSumSquarePositiveSD.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysIpSlaPdvDataSumSquarePositiveSD.setStatus(_B)
_EtsysIpSlaPdvDataMinNegativeSD_Type=Gauge32
_EtsysIpSlaPdvDataMinNegativeSD_Object=MibTableColumn
etsysIpSlaPdvDataMinNegativeSD=_EtsysIpSlaPdvDataMinNegativeSD_Object((1,3,6,1,4,1,5624,1,2,94,1,2,6,1,7),_EtsysIpSlaPdvDataMinNegativeSD_Type())
etsysIpSlaPdvDataMinNegativeSD.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysIpSlaPdvDataMinNegativeSD.setStatus(_B)
_EtsysIpSlaPdvDataMaxNegativeSD_Type=Gauge32
_EtsysIpSlaPdvDataMaxNegativeSD_Object=MibTableColumn
etsysIpSlaPdvDataMaxNegativeSD=_EtsysIpSlaPdvDataMaxNegativeSD_Object((1,3,6,1,4,1,5624,1,2,94,1,2,6,1,8),_EtsysIpSlaPdvDataMaxNegativeSD_Type())
etsysIpSlaPdvDataMaxNegativeSD.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysIpSlaPdvDataMaxNegativeSD.setStatus(_B)
_EtsysIpSlaPdvDataNumNegativeSD_Type=Gauge32
_EtsysIpSlaPdvDataNumNegativeSD_Object=MibTableColumn
etsysIpSlaPdvDataNumNegativeSD=_EtsysIpSlaPdvDataNumNegativeSD_Object((1,3,6,1,4,1,5624,1,2,94,1,2,6,1,9),_EtsysIpSlaPdvDataNumNegativeSD_Type())
etsysIpSlaPdvDataNumNegativeSD.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysIpSlaPdvDataNumNegativeSD.setStatus(_B)
_EtsysIpSlaPdvDataSumNegativeSD_Type=Gauge32
_EtsysIpSlaPdvDataSumNegativeSD_Object=MibTableColumn
etsysIpSlaPdvDataSumNegativeSD=_EtsysIpSlaPdvDataSumNegativeSD_Object((1,3,6,1,4,1,5624,1,2,94,1,2,6,1,10),_EtsysIpSlaPdvDataSumNegativeSD_Type())
etsysIpSlaPdvDataSumNegativeSD.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysIpSlaPdvDataSumNegativeSD.setStatus(_B)
_EtsysIpSlaPdvDataSumSquareNegativeSD_Type=Gauge32
_EtsysIpSlaPdvDataSumSquareNegativeSD_Object=MibTableColumn
etsysIpSlaPdvDataSumSquareNegativeSD=_EtsysIpSlaPdvDataSumSquareNegativeSD_Object((1,3,6,1,4,1,5624,1,2,94,1,2,6,1,11),_EtsysIpSlaPdvDataSumSquareNegativeSD_Type())
etsysIpSlaPdvDataSumSquareNegativeSD.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysIpSlaPdvDataSumSquareNegativeSD.setStatus(_B)
_EtsysIpSlaPdvDataMinPositiveDS_Type=Gauge32
_EtsysIpSlaPdvDataMinPositiveDS_Object=MibTableColumn
etsysIpSlaPdvDataMinPositiveDS=_EtsysIpSlaPdvDataMinPositiveDS_Object((1,3,6,1,4,1,5624,1,2,94,1,2,6,1,12),_EtsysIpSlaPdvDataMinPositiveDS_Type())
etsysIpSlaPdvDataMinPositiveDS.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysIpSlaPdvDataMinPositiveDS.setStatus(_B)
_EtsysIpSlaPdvDataMaxPositiveDS_Type=Gauge32
_EtsysIpSlaPdvDataMaxPositiveDS_Object=MibTableColumn
etsysIpSlaPdvDataMaxPositiveDS=_EtsysIpSlaPdvDataMaxPositiveDS_Object((1,3,6,1,4,1,5624,1,2,94,1,2,6,1,13),_EtsysIpSlaPdvDataMaxPositiveDS_Type())
etsysIpSlaPdvDataMaxPositiveDS.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysIpSlaPdvDataMaxPositiveDS.setStatus(_B)
_EtsysIpSlaPdvDataNumPositiveDS_Type=Gauge32
_EtsysIpSlaPdvDataNumPositiveDS_Object=MibTableColumn
etsysIpSlaPdvDataNumPositiveDS=_EtsysIpSlaPdvDataNumPositiveDS_Object((1,3,6,1,4,1,5624,1,2,94,1,2,6,1,14),_EtsysIpSlaPdvDataNumPositiveDS_Type())
etsysIpSlaPdvDataNumPositiveDS.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysIpSlaPdvDataNumPositiveDS.setStatus(_B)
_EtsysIpSlaPdvDataSumPositiveDS_Type=Gauge32
_EtsysIpSlaPdvDataSumPositiveDS_Object=MibTableColumn
etsysIpSlaPdvDataSumPositiveDS=_EtsysIpSlaPdvDataSumPositiveDS_Object((1,3,6,1,4,1,5624,1,2,94,1,2,6,1,15),_EtsysIpSlaPdvDataSumPositiveDS_Type())
etsysIpSlaPdvDataSumPositiveDS.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysIpSlaPdvDataSumPositiveDS.setStatus(_B)
_EtsysIpSlaPdvDataSumSquarePositiveDS_Type=Gauge32
_EtsysIpSlaPdvDataSumSquarePositiveDS_Object=MibTableColumn
etsysIpSlaPdvDataSumSquarePositiveDS=_EtsysIpSlaPdvDataSumSquarePositiveDS_Object((1,3,6,1,4,1,5624,1,2,94,1,2,6,1,16),_EtsysIpSlaPdvDataSumSquarePositiveDS_Type())
etsysIpSlaPdvDataSumSquarePositiveDS.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysIpSlaPdvDataSumSquarePositiveDS.setStatus(_B)
_EtsysIpSlaPdvDataMinNegativeDS_Type=Gauge32
_EtsysIpSlaPdvDataMinNegativeDS_Object=MibTableColumn
etsysIpSlaPdvDataMinNegativeDS=_EtsysIpSlaPdvDataMinNegativeDS_Object((1,3,6,1,4,1,5624,1,2,94,1,2,6,1,17),_EtsysIpSlaPdvDataMinNegativeDS_Type())
etsysIpSlaPdvDataMinNegativeDS.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysIpSlaPdvDataMinNegativeDS.setStatus(_B)
_EtsysIpSlaPdvDataMaxNegativeDS_Type=Gauge32
_EtsysIpSlaPdvDataMaxNegativeDS_Object=MibTableColumn
etsysIpSlaPdvDataMaxNegativeDS=_EtsysIpSlaPdvDataMaxNegativeDS_Object((1,3,6,1,4,1,5624,1,2,94,1,2,6,1,18),_EtsysIpSlaPdvDataMaxNegativeDS_Type())
etsysIpSlaPdvDataMaxNegativeDS.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysIpSlaPdvDataMaxNegativeDS.setStatus(_B)
_EtsysIpSlaPdvDataNumNegativeDS_Type=Gauge32
_EtsysIpSlaPdvDataNumNegativeDS_Object=MibTableColumn
etsysIpSlaPdvDataNumNegativeDS=_EtsysIpSlaPdvDataNumNegativeDS_Object((1,3,6,1,4,1,5624,1,2,94,1,2,6,1,19),_EtsysIpSlaPdvDataNumNegativeDS_Type())
etsysIpSlaPdvDataNumNegativeDS.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysIpSlaPdvDataNumNegativeDS.setStatus(_B)
_EtsysIpSlaPdvDataSumNegativeDS_Type=Gauge32
_EtsysIpSlaPdvDataSumNegativeDS_Object=MibTableColumn
etsysIpSlaPdvDataSumNegativeDS=_EtsysIpSlaPdvDataSumNegativeDS_Object((1,3,6,1,4,1,5624,1,2,94,1,2,6,1,20),_EtsysIpSlaPdvDataSumNegativeDS_Type())
etsysIpSlaPdvDataSumNegativeDS.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysIpSlaPdvDataSumNegativeDS.setStatus(_B)
_EtsysIpSlaPdvDataSumSquareNegativeDS_Type=Gauge32
_EtsysIpSlaPdvDataSumSquareNegativeDS_Object=MibTableColumn
etsysIpSlaPdvDataSumSquareNegativeDS=_EtsysIpSlaPdvDataSumSquareNegativeDS_Object((1,3,6,1,4,1,5624,1,2,94,1,2,6,1,21),_EtsysIpSlaPdvDataSumSquareNegativeDS_Type())
etsysIpSlaPdvDataSumSquareNegativeDS.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysIpSlaPdvDataSumSquareNegativeDS.setStatus(_B)
_EtsysIpSlaPdvDataNumOneWaySD_Type=Gauge32
_EtsysIpSlaPdvDataNumOneWaySD_Object=MibTableColumn
etsysIpSlaPdvDataNumOneWaySD=_EtsysIpSlaPdvDataNumOneWaySD_Object((1,3,6,1,4,1,5624,1,2,94,1,2,6,1,22),_EtsysIpSlaPdvDataNumOneWaySD_Type())
etsysIpSlaPdvDataNumOneWaySD.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysIpSlaPdvDataNumOneWaySD.setStatus(_B)
_EtsysIpSlaPdvDataMinOneWaySD_Type=Gauge32
_EtsysIpSlaPdvDataMinOneWaySD_Object=MibTableColumn
etsysIpSlaPdvDataMinOneWaySD=_EtsysIpSlaPdvDataMinOneWaySD_Object((1,3,6,1,4,1,5624,1,2,94,1,2,6,1,23),_EtsysIpSlaPdvDataMinOneWaySD_Type())
etsysIpSlaPdvDataMinOneWaySD.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysIpSlaPdvDataMinOneWaySD.setStatus(_B)
_EtsysIpSlaPdvDataMaxOneWaySD_Type=Gauge32
_EtsysIpSlaPdvDataMaxOneWaySD_Object=MibTableColumn
etsysIpSlaPdvDataMaxOneWaySD=_EtsysIpSlaPdvDataMaxOneWaySD_Object((1,3,6,1,4,1,5624,1,2,94,1,2,6,1,24),_EtsysIpSlaPdvDataMaxOneWaySD_Type())
etsysIpSlaPdvDataMaxOneWaySD.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysIpSlaPdvDataMaxOneWaySD.setStatus(_B)
_EtsysIpSlaPdvDataSumOneWaySD_Type=Gauge32
_EtsysIpSlaPdvDataSumOneWaySD_Object=MibTableColumn
etsysIpSlaPdvDataSumOneWaySD=_EtsysIpSlaPdvDataSumOneWaySD_Object((1,3,6,1,4,1,5624,1,2,94,1,2,6,1,25),_EtsysIpSlaPdvDataSumOneWaySD_Type())
etsysIpSlaPdvDataSumOneWaySD.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysIpSlaPdvDataSumOneWaySD.setStatus(_B)
_EtsysIpSlaPdvDataSumSquareOneWaySD_Type=Gauge32
_EtsysIpSlaPdvDataSumSquareOneWaySD_Object=MibTableColumn
etsysIpSlaPdvDataSumSquareOneWaySD=_EtsysIpSlaPdvDataSumSquareOneWaySD_Object((1,3,6,1,4,1,5624,1,2,94,1,2,6,1,26),_EtsysIpSlaPdvDataSumSquareOneWaySD_Type())
etsysIpSlaPdvDataSumSquareOneWaySD.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysIpSlaPdvDataSumSquareOneWaySD.setStatus(_B)
_EtsysIpSlaPdvDataNumOneWayDS_Type=Gauge32
_EtsysIpSlaPdvDataNumOneWayDS_Object=MibTableColumn
etsysIpSlaPdvDataNumOneWayDS=_EtsysIpSlaPdvDataNumOneWayDS_Object((1,3,6,1,4,1,5624,1,2,94,1,2,6,1,27),_EtsysIpSlaPdvDataNumOneWayDS_Type())
etsysIpSlaPdvDataNumOneWayDS.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysIpSlaPdvDataNumOneWayDS.setStatus(_B)
_EtsysIpSlaPdvDataMinOneWayDS_Type=Gauge32
_EtsysIpSlaPdvDataMinOneWayDS_Object=MibTableColumn
etsysIpSlaPdvDataMinOneWayDS=_EtsysIpSlaPdvDataMinOneWayDS_Object((1,3,6,1,4,1,5624,1,2,94,1,2,6,1,28),_EtsysIpSlaPdvDataMinOneWayDS_Type())
etsysIpSlaPdvDataMinOneWayDS.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysIpSlaPdvDataMinOneWayDS.setStatus(_B)
_EtsysIpSlaPdvDataMaxOneWayDS_Type=Gauge32
_EtsysIpSlaPdvDataMaxOneWayDS_Object=MibTableColumn
etsysIpSlaPdvDataMaxOneWayDS=_EtsysIpSlaPdvDataMaxOneWayDS_Object((1,3,6,1,4,1,5624,1,2,94,1,2,6,1,29),_EtsysIpSlaPdvDataMaxOneWayDS_Type())
etsysIpSlaPdvDataMaxOneWayDS.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysIpSlaPdvDataMaxOneWayDS.setStatus(_B)
_EtsysIpSlaPdvDataSumOneWayDS_Type=Gauge32
_EtsysIpSlaPdvDataSumOneWayDS_Object=MibTableColumn
etsysIpSlaPdvDataSumOneWayDS=_EtsysIpSlaPdvDataSumOneWayDS_Object((1,3,6,1,4,1,5624,1,2,94,1,2,6,1,30),_EtsysIpSlaPdvDataSumOneWayDS_Type())
etsysIpSlaPdvDataSumOneWayDS.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysIpSlaPdvDataSumOneWayDS.setStatus(_B)
_EtsysIpSlaPdvDataSumSquareOneWayDS_Type=Gauge32
_EtsysIpSlaPdvDataSumSquareOneWayDS_Object=MibTableColumn
etsysIpSlaPdvDataSumSquareOneWayDS=_EtsysIpSlaPdvDataSumSquareOneWayDS_Object((1,3,6,1,4,1,5624,1,2,94,1,2,6,1,31),_EtsysIpSlaPdvDataSumSquareOneWayDS_Type())
etsysIpSlaPdvDataSumSquareOneWayDS.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysIpSlaPdvDataSumSquareOneWayDS.setStatus(_B)
_EtsysIpSlaDistDataTable_Object=MibTable
etsysIpSlaDistDataTable=_EtsysIpSlaDistDataTable_Object((1,3,6,1,4,1,5624,1,2,94,1,2,7))
if mibBuilder.loadTexts:etsysIpSlaDistDataTable.setStatus(_B)
_EtsysIpSlaDistDataEntry_Object=MibTableRow
etsysIpSlaDistDataEntry=_EtsysIpSlaDistDataEntry_Object((1,3,6,1,4,1,5624,1,2,94,1,2,7,1))
etsysIpSlaDistDataEntry.setIndexNames((0,_A,_F),(0,_A,_I),(0,_A,_J),(0,_A,_N),(0,_A,_O),(0,_A,_Q))
if mibBuilder.loadTexts:etsysIpSlaDistDataEntry.setStatus(_B)
_EtsysIpSlaDistMinRange_Type=Unsigned32
_EtsysIpSlaDistMinRange_Object=MibTableColumn
etsysIpSlaDistMinRange=_EtsysIpSlaDistMinRange_Object((1,3,6,1,4,1,5624,1,2,94,1,2,7,1,1),_EtsysIpSlaDistMinRange_Type())
etsysIpSlaDistMinRange.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysIpSlaDistMinRange.setStatus(_B)
if mibBuilder.loadTexts:etsysIpSlaDistMinRange.setUnits(_S)
_EtsysIpSlaDistMaxRange_Type=Unsigned32
_EtsysIpSlaDistMaxRange_Object=MibTableColumn
etsysIpSlaDistMaxRange=_EtsysIpSlaDistMaxRange_Object((1,3,6,1,4,1,5624,1,2,94,1,2,7,1,2),_EtsysIpSlaDistMaxRange_Type())
etsysIpSlaDistMaxRange.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysIpSlaDistMaxRange.setStatus(_B)
if mibBuilder.loadTexts:etsysIpSlaDistMaxRange.setUnits(_S)
_EtsysIpSlaConformance_ObjectIdentity=ObjectIdentity
etsysIpSlaConformance=_EtsysIpSlaConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,94,2))
_EtsysIpSlaGroups_ObjectIdentity=ObjectIdentity
etsysIpSlaGroups=_EtsysIpSlaGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,94,2,1))
_EtsysIpSlaCompliances_ObjectIdentity=ObjectIdentity
etsysIpSlaCompliances=_EtsysIpSlaCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,94,2,2))
etsysIpSlaGlobalGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,94,2,1,1))
etsysIpSlaGlobalGroup.setObjects(*((_A,_W),(_A,_X),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:etsysIpSlaGlobalGroup.setStatus(_B)
etsysIpSlaConfigGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,94,2,1,2))
etsysIpSlaConfigGroup.setObjects(*((_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y)))
if mibBuilder.loadTexts:etsysIpSlaConfigGroup.setStatus(_B)
etsysIpSlaCollectionGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,94,2,1,3))
etsysIpSlaCollectionGroup.setObjects(*((_A,_z),(_A,_A0),(_A,_A1)))
if mibBuilder.loadTexts:etsysIpSlaCollectionGroup.setStatus(_B)
etsysIpSlaPathGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,94,2,1,4))
etsysIpSlaPathGroup.setObjects(*((_A,_A2),(_A,_A3)))
if mibBuilder.loadTexts:etsysIpSlaPathGroup.setStatus(_B)
etsysIpSlaRttGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,94,2,1,5))
etsysIpSlaRttGroup.setObjects(*((_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH)))
if mibBuilder.loadTexts:etsysIpSlaRttGroup.setStatus(_B)
etsysIpSlaPdvGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,94,2,1,6))
etsysIpSlaPdvGroup.setObjects(*((_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_Ae),(_A,_Af),(_A,_Ag),(_A,_Ah),(_A,_Ai),(_A,_Aj),(_A,_Ak),(_A,_Al),(_A,_Am)))
if mibBuilder.loadTexts:etsysIpSlaPdvGroup.setStatus(_B)
etsysIpSlaDistribGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,94,2,1,7))
etsysIpSlaDistribGroup.setObjects(*((_A,_An),(_A,_Ao)))
if mibBuilder.loadTexts:etsysIpSlaDistribGroup.setStatus(_B)
etsysIpSlaCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,94,2,2,1))
etsysIpSlaCompliance.setObjects(*((_A,_Ap),(_A,_Aq),(_A,_Ar),(_A,_As)))
if mibBuilder.loadTexts:etsysIpSlaCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'etsysIpSlaMIB':etsysIpSlaMIB,'etsysIpSla':etsysIpSla,'etsysIpSlaGlobals':etsysIpSlaGlobals,_W:etsysIpSlaMaxEntries,_X:etsysIpSlaEntriesInUse,_Y:etsysIpSlaMaxDataEntries,_Z:etsysIpSlaDataEntriesInUse,'etsysIpSlaTables':etsysIpSlaTables,'etsysIpSlaConfigTable':etsysIpSlaConfigTable,'etsysIpSlaConfigEntry':etsysIpSlaConfigEntry,_F:etsysIpSlaConfigIndex,_a:etsysIpSlaConfigType,_b:etsysIpSlaConfigDestType,_c:etsysIpSlaConfigDestAddr,_d:etsysIpSlaConfigDestPort,_e:etsysIpSlaConfigProbeName,_f:etsysIpSlaConfigPathCount,_g:etsysIpSlaConfigHopCount,_h:etsysIpSlaConfigHistoryCollections,_i:etsysIpSlaConfigHistoryBuckets,_j:etsysIpSlaConfigHistoryBucketType,_k:etsysIpSlaConfigHistorySamples,_l:etsysIpSlaConfigHistoryInterval,_m:etsysIpSlaConfigHistoryAgeout,_n:etsysIpSlaConfigHistoryWrap,_o:etsysIpSlaConfigDistributionCount,_p:etsysIpSlaConfigDistributionInterval,_q:etsysIpSlaConfigStatisticsCollections,_r:etsysIpSlaConfigStatus,'etsysIpSlaScheduleTable':etsysIpSlaScheduleTable,'etsysIpSlaScheduleEntry':etsysIpSlaScheduleEntry,_s:etsysIpSlaScheduleStartTime,_t:etsysIpSlaScheduleRecurrence,_u:etsysIpSlaScheduleTestRepetitions,_v:etsysIpSlaScheduleTestDuration,_w:etsysIpSlaScheduleTestFrequency,_x:etsysIpSlaScheduleTestState,_y:etsysIpSlaScheduleTestStatus,'etsysIpSlaCollectionTable':etsysIpSlaCollectionTable,'etsysIpSlaCollectionEntry':etsysIpSlaCollectionEntry,_I:etsysIpSlaCollectionType,_J:etsysIpSlaCollectionIndex,_z:etsysIpSlaCollectionStartTime,_A0:etsysIpSlaCollectionNumPaths,_A1:etsysIpslaCollectionNumHops,'etsysIpSlaPathTable':etsysIpSlaPathTable,'etsysIpSlaPathEntry':etsysIpSlaPathEntry,_N:etsysIpSlaPathIndex,_O:etsysIpSlaHopIndex,_A2:etsysIpSlaHopDestType,_A3:etsysIpSlaHopDestAddr,'etsysIpSlaRttDataTable':etsysIpSlaRttDataTable,'etsysIpSlaRttDataEntry':etsysIpSlaRttDataEntry,_Q:etsysIpSlaBucketIndex,_A4:etsysIpSlaBucketTime,_A5:etsysIpSlaRttDataSamples,_A6:etsysIpSlaRttDataMinDelay,_A7:etsysIpSlaRttDataAvgDelay,_A8:etsysIpSlaRttDataMaxDelay,_A9:etsysIpSlaRttDataSum,_AA:etsysIpSlaRttDataSumSquareLow,_AB:etsysIpSlaRttDataSumSquareHigh,_AC:etsysIpSlaRttDataPktOutOfOrder,_AD:etsysIpSlaRttDataPktLateArrival,_AE:etsysIpSlaRttDataPktMissing,_AF:etsysIpSlaRttDataPktIpTosMismatch,_AG:etsysIpSlaRttDataPktVlanPcpMismatch,_AH:etsysIpSlaRttDataTxErrors,'etsysIpSlaPdvDataTable':etsysIpSlaPdvDataTable,'etsysIpSlaPdvDataEntry':etsysIpSlaPdvDataEntry,_AI:etsysIpSlaPdvDataSamples,_AJ:etsysIpSlaPdvDataMinPositiveSD,_AK:etsysIpSlaPdvDataMaxPositiveSD,_AL:etsysIpSlaPdvDataNumPositiveSD,_AM:etsysIpSlaPdvDataSumPositiveSD,_AN:etsysIpSlaPdvDataSumSquarePositiveSD,_AO:etsysIpSlaPdvDataMinNegativeSD,_AP:etsysIpSlaPdvDataMaxNegativeSD,_AQ:etsysIpSlaPdvDataNumNegativeSD,_AR:etsysIpSlaPdvDataSumNegativeSD,_AS:etsysIpSlaPdvDataSumSquareNegativeSD,_AT:etsysIpSlaPdvDataMinPositiveDS,_AU:etsysIpSlaPdvDataMaxPositiveDS,_AV:etsysIpSlaPdvDataNumPositiveDS,_AW:etsysIpSlaPdvDataSumPositiveDS,_AX:etsysIpSlaPdvDataSumSquarePositiveDS,_AY:etsysIpSlaPdvDataMinNegativeDS,_AZ:etsysIpSlaPdvDataMaxNegativeDS,_Aa:etsysIpSlaPdvDataNumNegativeDS,_Ab:etsysIpSlaPdvDataSumNegativeDS,_Ac:etsysIpSlaPdvDataSumSquareNegativeDS,_Ad:etsysIpSlaPdvDataNumOneWaySD,_Ae:etsysIpSlaPdvDataMinOneWaySD,_Af:etsysIpSlaPdvDataMaxOneWaySD,_Ag:etsysIpSlaPdvDataSumOneWaySD,_Ah:etsysIpSlaPdvDataSumSquareOneWaySD,_Ai:etsysIpSlaPdvDataNumOneWayDS,_Aj:etsysIpSlaPdvDataMinOneWayDS,_Ak:etsysIpSlaPdvDataMaxOneWayDS,_Al:etsysIpSlaPdvDataSumOneWayDS,_Am:etsysIpSlaPdvDataSumSquareOneWayDS,'etsysIpSlaDistDataTable':etsysIpSlaDistDataTable,'etsysIpSlaDistDataEntry':etsysIpSlaDistDataEntry,_An:etsysIpSlaDistMinRange,_Ao:etsysIpSlaDistMaxRange,'etsysIpSlaConformance':etsysIpSlaConformance,'etsysIpSlaGroups':etsysIpSlaGroups,'etsysIpSlaGlobalGroup':etsysIpSlaGlobalGroup,_Ap:etsysIpSlaConfigGroup,_Aq:etsysIpSlaCollectionGroup,_Ar:etsysIpSlaPathGroup,_As:etsysIpSlaRttGroup,'etsysIpSlaPdvGroup':etsysIpSlaPdvGroup,'etsysIpSlaDistribGroup':etsysIpSlaDistribGroup,'etsysIpSlaCompliances':etsysIpSlaCompliances,'etsysIpSlaCompliance':etsysIpSlaCompliance})