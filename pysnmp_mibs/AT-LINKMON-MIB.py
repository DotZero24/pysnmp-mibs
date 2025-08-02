_I='atLinkMonSampleBucket'
_H='not-accessible'
_G='atLinkMonProbeHistoryID'
_F='atLinkMonProbeID'
_E='ms'
_D='AT-LINKMON-MIB'
_C='Unsigned32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
DisplayStringUnsized,modules=mibBuilder.importSymbols('AT-SMI-MIB','DisplayStringUnsized','modules')
InetVersion,=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetVersion')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
atLinkMon=ModuleIdentity((1,3,6,1,4,1,207,8,4,4,4,606))
if mibBuilder.loadTexts:atLinkMon.setRevisions(('2020-09-15 00:00',))
class AtLinkMonType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('icmp',1),('http',2)))
_AtLinkMonProbeTable_Object=MibTable
atLinkMonProbeTable=_AtLinkMonProbeTable_Object((1,3,6,1,4,1,207,8,4,4,4,606,1))
if mibBuilder.loadTexts:atLinkMonProbeTable.setStatus(_A)
_AtLinkMonProbeEntry_Object=MibTableRow
atLinkMonProbeEntry=_AtLinkMonProbeEntry_Object((1,3,6,1,4,1,207,8,4,4,4,606,1,1))
atLinkMonProbeEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:atLinkMonProbeEntry.setStatus(_A)
_AtLinkMonProbeID_Type=Unsigned32
_AtLinkMonProbeID_Object=MibTableColumn
atLinkMonProbeID=_AtLinkMonProbeID_Object((1,3,6,1,4,1,207,8,4,4,4,606,1,1,1),_AtLinkMonProbeID_Type())
atLinkMonProbeID.setMaxAccess(_H)
if mibBuilder.loadTexts:atLinkMonProbeID.setStatus(_A)
_AtLinkMonProbeName_Type=DisplayStringUnsized
_AtLinkMonProbeName_Object=MibTableColumn
atLinkMonProbeName=_AtLinkMonProbeName_Object((1,3,6,1,4,1,207,8,4,4,4,606,1,1,2),_AtLinkMonProbeName_Type())
atLinkMonProbeName.setMaxAccess(_B)
if mibBuilder.loadTexts:atLinkMonProbeName.setStatus(_A)
_AtLinkMonProbeType_Type=AtLinkMonType
_AtLinkMonProbeType_Object=MibTableColumn
atLinkMonProbeType=_AtLinkMonProbeType_Object((1,3,6,1,4,1,207,8,4,4,4,606,1,1,3),_AtLinkMonProbeType_Type())
atLinkMonProbeType.setMaxAccess(_B)
if mibBuilder.loadTexts:atLinkMonProbeType.setStatus(_A)
if mibBuilder.loadTexts:atLinkMonProbeType.setUnits('ICMP: 1, HTTP: 2')
_AtLinkMonProbeIPVersion_Type=InetVersion
_AtLinkMonProbeIPVersion_Object=MibTableColumn
atLinkMonProbeIPVersion=_AtLinkMonProbeIPVersion_Object((1,3,6,1,4,1,207,8,4,4,4,606,1,1,4),_AtLinkMonProbeIPVersion_Type())
atLinkMonProbeIPVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:atLinkMonProbeIPVersion.setStatus(_A)
if mibBuilder.loadTexts:atLinkMonProbeIPVersion.setUnits('IPv4: 1, IPv6: 2')
_AtLinkMonProbeDestination_Type=DisplayStringUnsized
_AtLinkMonProbeDestination_Object=MibTableColumn
atLinkMonProbeDestination=_AtLinkMonProbeDestination_Object((1,3,6,1,4,1,207,8,4,4,4,606,1,1,5),_AtLinkMonProbeDestination_Type())
atLinkMonProbeDestination.setMaxAccess(_B)
if mibBuilder.loadTexts:atLinkMonProbeDestination.setStatus(_A)
_AtLinkMonProbeEgressIf_Type=DisplayStringUnsized
_AtLinkMonProbeEgressIf_Object=MibTableColumn
atLinkMonProbeEgressIf=_AtLinkMonProbeEgressIf_Object((1,3,6,1,4,1,207,8,4,4,4,606,1,1,6),_AtLinkMonProbeEgressIf_Type())
atLinkMonProbeEgressIf.setMaxAccess(_B)
if mibBuilder.loadTexts:atLinkMonProbeEgressIf.setStatus(_A)
_AtLinkmonProbeEgreesIfValid_Type=TruthValue
_AtLinkmonProbeEgreesIfValid_Object=MibTableColumn
atLinkmonProbeEgreesIfValid=_AtLinkmonProbeEgreesIfValid_Object((1,3,6,1,4,1,207,8,4,4,4,606,1,1,7),_AtLinkmonProbeEgreesIfValid_Type())
atLinkmonProbeEgreesIfValid.setMaxAccess(_B)
if mibBuilder.loadTexts:atLinkmonProbeEgreesIfValid.setStatus(_A)
_AtLinkMonProbeSource_Type=DisplayStringUnsized
_AtLinkMonProbeSource_Object=MibTableColumn
atLinkMonProbeSource=_AtLinkMonProbeSource_Object((1,3,6,1,4,1,207,8,4,4,4,606,1,1,8),_AtLinkMonProbeSource_Type())
atLinkMonProbeSource.setMaxAccess(_B)
if mibBuilder.loadTexts:atLinkMonProbeSource.setStatus(_A)
_AtLinkMonProbeSourceValid_Type=TruthValue
_AtLinkMonProbeSourceValid_Object=MibTableColumn
atLinkMonProbeSourceValid=_AtLinkMonProbeSourceValid_Object((1,3,6,1,4,1,207,8,4,4,4,606,1,1,9),_AtLinkMonProbeSourceValid_Type())
atLinkMonProbeSourceValid.setMaxAccess(_B)
if mibBuilder.loadTexts:atLinkMonProbeSourceValid.setStatus(_A)
class _AtLinkMonProbeDSCP_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_AtLinkMonProbeDSCP_Type.__name__=_C
_AtLinkMonProbeDSCP_Object=MibTableColumn
atLinkMonProbeDSCP=_AtLinkMonProbeDSCP_Object((1,3,6,1,4,1,207,8,4,4,4,606,1,1,10),_AtLinkMonProbeDSCP_Type())
atLinkMonProbeDSCP.setMaxAccess(_B)
if mibBuilder.loadTexts:atLinkMonProbeDSCP.setStatus(_A)
class _AtLinkMonProbePacketSize_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,1500))
_AtLinkMonProbePacketSize_Type.__name__=_C
_AtLinkMonProbePacketSize_Object=MibTableColumn
atLinkMonProbePacketSize=_AtLinkMonProbePacketSize_Object((1,3,6,1,4,1,207,8,4,4,4,606,1,1,11),_AtLinkMonProbePacketSize_Type())
atLinkMonProbePacketSize.setMaxAccess(_B)
if mibBuilder.loadTexts:atLinkMonProbePacketSize.setStatus(_A)
if mibBuilder.loadTexts:atLinkMonProbePacketSize.setUnits('bytes')
class _AtLinkMonProbeInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,3600000))
_AtLinkMonProbeInterval_Type.__name__=_C
_AtLinkMonProbeInterval_Object=MibTableColumn
atLinkMonProbeInterval=_AtLinkMonProbeInterval_Object((1,3,6,1,4,1,207,8,4,4,4,606,1,1,12),_AtLinkMonProbeInterval_Type())
atLinkMonProbeInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:atLinkMonProbeInterval.setStatus(_A)
if mibBuilder.loadTexts:atLinkMonProbeInterval.setUnits(_E)
class _AtLinkMonProbeSampleSize_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_AtLinkMonProbeSampleSize_Type.__name__=_C
_AtLinkMonProbeSampleSize_Object=MibTableColumn
atLinkMonProbeSampleSize=_AtLinkMonProbeSampleSize_Object((1,3,6,1,4,1,207,8,4,4,4,606,1,1,13),_AtLinkMonProbeSampleSize_Type())
atLinkMonProbeSampleSize.setMaxAccess(_B)
if mibBuilder.loadTexts:atLinkMonProbeSampleSize.setStatus(_A)
_AtLinkMonProbeEnabled_Type=TruthValue
_AtLinkMonProbeEnabled_Object=MibTableColumn
atLinkMonProbeEnabled=_AtLinkMonProbeEnabled_Object((1,3,6,1,4,1,207,8,4,4,4,606,1,1,14),_AtLinkMonProbeEnabled_Type())
atLinkMonProbeEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:atLinkMonProbeEnabled.setStatus(_A)
_AtLinkMonProbeDetailTable_Object=MibTable
atLinkMonProbeDetailTable=_AtLinkMonProbeDetailTable_Object((1,3,6,1,4,1,207,8,4,4,4,606,2))
if mibBuilder.loadTexts:atLinkMonProbeDetailTable.setStatus(_A)
_AtLinkMonProbeDetailEntry_Object=MibTableRow
atLinkMonProbeDetailEntry=_AtLinkMonProbeDetailEntry_Object((1,3,6,1,4,1,207,8,4,4,4,606,2,1))
atLinkMonProbeDetailEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:atLinkMonProbeDetailEntry.setStatus(_A)
_AtLinkMonProbeDetailProbesSent_Type=Counter64
_AtLinkMonProbeDetailProbesSent_Object=MibTableColumn
atLinkMonProbeDetailProbesSent=_AtLinkMonProbeDetailProbesSent_Object((1,3,6,1,4,1,207,8,4,4,4,606,2,1,1),_AtLinkMonProbeDetailProbesSent_Type())
atLinkMonProbeDetailProbesSent.setMaxAccess(_B)
if mibBuilder.loadTexts:atLinkMonProbeDetailProbesSent.setStatus(_A)
_AtLinkMonProbeDetailLastTxTime_Type=DisplayStringUnsized
_AtLinkMonProbeDetailLastTxTime_Object=MibTableColumn
atLinkMonProbeDetailLastTxTime=_AtLinkMonProbeDetailLastTxTime_Object((1,3,6,1,4,1,207,8,4,4,4,606,2,1,2),_AtLinkMonProbeDetailLastTxTime_Type())
atLinkMonProbeDetailLastTxTime.setMaxAccess(_B)
if mibBuilder.loadTexts:atLinkMonProbeDetailLastTxTime.setStatus(_A)
_AtLinkMonProbeDetailLastRxTime_Type=DisplayStringUnsized
_AtLinkMonProbeDetailLastRxTime_Object=MibTableColumn
atLinkMonProbeDetailLastRxTime=_AtLinkMonProbeDetailLastRxTime_Object((1,3,6,1,4,1,207,8,4,4,4,606,2,1,3),_AtLinkMonProbeDetailLastRxTime_Type())
atLinkMonProbeDetailLastRxTime.setMaxAccess(_B)
if mibBuilder.loadTexts:atLinkMonProbeDetailLastRxTime.setStatus(_A)
_AtLinkMonProbeLatestMetricsTable_Object=MibTable
atLinkMonProbeLatestMetricsTable=_AtLinkMonProbeLatestMetricsTable_Object((1,3,6,1,4,1,207,8,4,4,4,606,3))
if mibBuilder.loadTexts:atLinkMonProbeLatestMetricsTable.setStatus(_A)
_AtLinkMonProbeLatestMetricsEntry_Object=MibTableRow
atLinkMonProbeLatestMetricsEntry=_AtLinkMonProbeLatestMetricsEntry_Object((1,3,6,1,4,1,207,8,4,4,4,606,3,1))
atLinkMonProbeLatestMetricsEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:atLinkMonProbeLatestMetricsEntry.setStatus(_A)
_AtLinkMonProbeLatestMetricsLatency_Type=Unsigned32
_AtLinkMonProbeLatestMetricsLatency_Object=MibTableColumn
atLinkMonProbeLatestMetricsLatency=_AtLinkMonProbeLatestMetricsLatency_Object((1,3,6,1,4,1,207,8,4,4,4,606,3,1,1),_AtLinkMonProbeLatestMetricsLatency_Type())
atLinkMonProbeLatestMetricsLatency.setMaxAccess(_B)
if mibBuilder.loadTexts:atLinkMonProbeLatestMetricsLatency.setStatus(_A)
if mibBuilder.loadTexts:atLinkMonProbeLatestMetricsLatency.setUnits(_E)
_AtLinkMonProbeLatestMetricsJitter_Type=Unsigned32
_AtLinkMonProbeLatestMetricsJitter_Object=MibTableColumn
atLinkMonProbeLatestMetricsJitter=_AtLinkMonProbeLatestMetricsJitter_Object((1,3,6,1,4,1,207,8,4,4,4,606,3,1,2),_AtLinkMonProbeLatestMetricsJitter_Type())
atLinkMonProbeLatestMetricsJitter.setMaxAccess(_B)
if mibBuilder.loadTexts:atLinkMonProbeLatestMetricsJitter.setStatus(_A)
if mibBuilder.loadTexts:atLinkMonProbeLatestMetricsJitter.setUnits(_E)
class _AtLinkMonProbeLatestMetricsPktLoss_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_AtLinkMonProbeLatestMetricsPktLoss_Type.__name__=_C
_AtLinkMonProbeLatestMetricsPktLoss_Object=MibTableColumn
atLinkMonProbeLatestMetricsPktLoss=_AtLinkMonProbeLatestMetricsPktLoss_Object((1,3,6,1,4,1,207,8,4,4,4,606,3,1,3),_AtLinkMonProbeLatestMetricsPktLoss_Type())
atLinkMonProbeLatestMetricsPktLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:atLinkMonProbeLatestMetricsPktLoss.setStatus(_A)
if mibBuilder.loadTexts:atLinkMonProbeLatestMetricsPktLoss.setUnits('1/10%')
_AtLinkMonProbeLatestMetricsCnscPktLoss_Type=Integer32
_AtLinkMonProbeLatestMetricsCnscPktLoss_Object=MibTableColumn
atLinkMonProbeLatestMetricsCnscPktLoss=_AtLinkMonProbeLatestMetricsCnscPktLoss_Object((1,3,6,1,4,1,207,8,4,4,4,606,3,1,4),_AtLinkMonProbeLatestMetricsCnscPktLoss_Type())
atLinkMonProbeLatestMetricsCnscPktLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:atLinkMonProbeLatestMetricsCnscPktLoss.setStatus(_A)
_AtLinkMonProbeHistoryTable_Object=MibTable
atLinkMonProbeHistoryTable=_AtLinkMonProbeHistoryTable_Object((1,3,6,1,4,1,207,8,4,4,4,606,4))
if mibBuilder.loadTexts:atLinkMonProbeHistoryTable.setStatus(_A)
_AtLinkMonProbeHistoryEntry_Object=MibTableRow
atLinkMonProbeHistoryEntry=_AtLinkMonProbeHistoryEntry_Object((1,3,6,1,4,1,207,8,4,4,4,606,4,1))
atLinkMonProbeHistoryEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:atLinkMonProbeHistoryEntry.setStatus(_A)
class _AtLinkMonProbeHistoryID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AtLinkMonProbeHistoryID_Type.__name__=_C
_AtLinkMonProbeHistoryID_Object=MibTableColumn
atLinkMonProbeHistoryID=_AtLinkMonProbeHistoryID_Object((1,3,6,1,4,1,207,8,4,4,4,606,4,1,1),_AtLinkMonProbeHistoryID_Type())
atLinkMonProbeHistoryID.setMaxAccess(_B)
if mibBuilder.loadTexts:atLinkMonProbeHistoryID.setStatus(_A)
_AtLinkMonProbeHistoryProbeName_Type=DisplayStringUnsized
_AtLinkMonProbeHistoryProbeName_Object=MibTableColumn
atLinkMonProbeHistoryProbeName=_AtLinkMonProbeHistoryProbeName_Object((1,3,6,1,4,1,207,8,4,4,4,606,4,1,2),_AtLinkMonProbeHistoryProbeName_Type())
atLinkMonProbeHistoryProbeName.setMaxAccess(_B)
if mibBuilder.loadTexts:atLinkMonProbeHistoryProbeName.setStatus(_A)
class _AtLinkMonProbeHistoryInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2678400))
_AtLinkMonProbeHistoryInterval_Type.__name__=_C
_AtLinkMonProbeHistoryInterval_Object=MibTableColumn
atLinkMonProbeHistoryInterval=_AtLinkMonProbeHistoryInterval_Object((1,3,6,1,4,1,207,8,4,4,4,606,4,1,3),_AtLinkMonProbeHistoryInterval_Type())
atLinkMonProbeHistoryInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:atLinkMonProbeHistoryInterval.setStatus(_A)
class _AtLinkMonProbeHistoryBuckets_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AtLinkMonProbeHistoryBuckets_Type.__name__=_C
_AtLinkMonProbeHistoryBuckets_Object=MibTableColumn
atLinkMonProbeHistoryBuckets=_AtLinkMonProbeHistoryBuckets_Object((1,3,6,1,4,1,207,8,4,4,4,606,4,1,4),_AtLinkMonProbeHistoryBuckets_Type())
atLinkMonProbeHistoryBuckets.setMaxAccess(_B)
if mibBuilder.loadTexts:atLinkMonProbeHistoryBuckets.setStatus(_A)
_AtLinkMonProbeHistoryLastSmplID_Type=Unsigned32
_AtLinkMonProbeHistoryLastSmplID_Object=MibTableColumn
atLinkMonProbeHistoryLastSmplID=_AtLinkMonProbeHistoryLastSmplID_Object((1,3,6,1,4,1,207,8,4,4,4,606,4,1,5),_AtLinkMonProbeHistoryLastSmplID_Type())
atLinkMonProbeHistoryLastSmplID.setMaxAccess(_B)
if mibBuilder.loadTexts:atLinkMonProbeHistoryLastSmplID.setStatus(_A)
_AtLinkMonProbeHistoryLastSmplTime_Type=DisplayStringUnsized
_AtLinkMonProbeHistoryLastSmplTime_Object=MibTableColumn
atLinkMonProbeHistoryLastSmplTime=_AtLinkMonProbeHistoryLastSmplTime_Object((1,3,6,1,4,1,207,8,4,4,4,606,4,1,6),_AtLinkMonProbeHistoryLastSmplTime_Type())
atLinkMonProbeHistoryLastSmplTime.setMaxAccess(_B)
if mibBuilder.loadTexts:atLinkMonProbeHistoryLastSmplTime.setStatus(_A)
_AtLinkMonSampleTable_Object=MibTable
atLinkMonSampleTable=_AtLinkMonSampleTable_Object((1,3,6,1,4,1,207,8,4,4,4,606,5))
if mibBuilder.loadTexts:atLinkMonSampleTable.setStatus(_A)
_AtLinkMonSampleEntry_Object=MibTableRow
atLinkMonSampleEntry=_AtLinkMonSampleEntry_Object((1,3,6,1,4,1,207,8,4,4,4,606,5,1))
atLinkMonSampleEntry.setIndexNames((0,_D,_G),(0,_D,_I))
if mibBuilder.loadTexts:atLinkMonSampleEntry.setStatus(_A)
_AtLinkMonSampleBucket_Type=Unsigned32
_AtLinkMonSampleBucket_Object=MibTableColumn
atLinkMonSampleBucket=_AtLinkMonSampleBucket_Object((1,3,6,1,4,1,207,8,4,4,4,606,5,1,1),_AtLinkMonSampleBucket_Type())
atLinkMonSampleBucket.setMaxAccess(_H)
if mibBuilder.loadTexts:atLinkMonSampleBucket.setStatus(_A)
_AtLinkMonSampleLatencySum_Type=Unsigned32
_AtLinkMonSampleLatencySum_Object=MibTableColumn
atLinkMonSampleLatencySum=_AtLinkMonSampleLatencySum_Object((1,3,6,1,4,1,207,8,4,4,4,606,5,1,2),_AtLinkMonSampleLatencySum_Type())
atLinkMonSampleLatencySum.setMaxAccess(_B)
if mibBuilder.loadTexts:atLinkMonSampleLatencySum.setStatus(_A)
if mibBuilder.loadTexts:atLinkMonSampleLatencySum.setUnits(_E)
_AtLinkMonSampleLatencyCount_Type=Unsigned32
_AtLinkMonSampleLatencyCount_Object=MibTableColumn
atLinkMonSampleLatencyCount=_AtLinkMonSampleLatencyCount_Object((1,3,6,1,4,1,207,8,4,4,4,606,5,1,3),_AtLinkMonSampleLatencyCount_Type())
atLinkMonSampleLatencyCount.setMaxAccess(_B)
if mibBuilder.loadTexts:atLinkMonSampleLatencyCount.setStatus(_A)
_AtLinkMonSampleJitterSum_Type=Unsigned32
_AtLinkMonSampleJitterSum_Object=MibTableColumn
atLinkMonSampleJitterSum=_AtLinkMonSampleJitterSum_Object((1,3,6,1,4,1,207,8,4,4,4,606,5,1,4),_AtLinkMonSampleJitterSum_Type())
atLinkMonSampleJitterSum.setMaxAccess(_B)
if mibBuilder.loadTexts:atLinkMonSampleJitterSum.setStatus(_A)
if mibBuilder.loadTexts:atLinkMonSampleJitterSum.setUnits(_E)
_AtLinkMonSampleJitterCount_Type=Unsigned32
_AtLinkMonSampleJitterCount_Object=MibTableColumn
atLinkMonSampleJitterCount=_AtLinkMonSampleJitterCount_Object((1,3,6,1,4,1,207,8,4,4,4,606,5,1,5),_AtLinkMonSampleJitterCount_Type())
atLinkMonSampleJitterCount.setMaxAccess(_B)
if mibBuilder.loadTexts:atLinkMonSampleJitterCount.setStatus(_A)
_AtLinkMonSamplePktLossSum_Type=Unsigned32
_AtLinkMonSamplePktLossSum_Object=MibTableColumn
atLinkMonSamplePktLossSum=_AtLinkMonSamplePktLossSum_Object((1,3,6,1,4,1,207,8,4,4,4,606,5,1,6),_AtLinkMonSamplePktLossSum_Type())
atLinkMonSamplePktLossSum.setMaxAccess(_B)
if mibBuilder.loadTexts:atLinkMonSamplePktLossSum.setStatus(_A)
if mibBuilder.loadTexts:atLinkMonSamplePktLossSum.setUnits('1/10%')
_AtLinkMonSamplePktsTx_Type=Unsigned32
_AtLinkMonSamplePktsTx_Object=MibTableColumn
atLinkMonSamplePktsTx=_AtLinkMonSamplePktsTx_Object((1,3,6,1,4,1,207,8,4,4,4,606,5,1,7),_AtLinkMonSamplePktsTx_Type())
atLinkMonSamplePktsTx.setMaxAccess(_B)
if mibBuilder.loadTexts:atLinkMonSamplePktsTx.setStatus(_A)
_AtLinkMonSamplePktsRx_Type=Unsigned32
_AtLinkMonSamplePktsRx_Object=MibTableColumn
atLinkMonSamplePktsRx=_AtLinkMonSamplePktsRx_Object((1,3,6,1,4,1,207,8,4,4,4,606,5,1,8),_AtLinkMonSamplePktsRx_Type())
atLinkMonSamplePktsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:atLinkMonSamplePktsRx.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'AtLinkMonType':AtLinkMonType,'atLinkMon':atLinkMon,'atLinkMonProbeTable':atLinkMonProbeTable,'atLinkMonProbeEntry':atLinkMonProbeEntry,_F:atLinkMonProbeID,'atLinkMonProbeName':atLinkMonProbeName,'atLinkMonProbeType':atLinkMonProbeType,'atLinkMonProbeIPVersion':atLinkMonProbeIPVersion,'atLinkMonProbeDestination':atLinkMonProbeDestination,'atLinkMonProbeEgressIf':atLinkMonProbeEgressIf,'atLinkmonProbeEgreesIfValid':atLinkmonProbeEgreesIfValid,'atLinkMonProbeSource':atLinkMonProbeSource,'atLinkMonProbeSourceValid':atLinkMonProbeSourceValid,'atLinkMonProbeDSCP':atLinkMonProbeDSCP,'atLinkMonProbePacketSize':atLinkMonProbePacketSize,'atLinkMonProbeInterval':atLinkMonProbeInterval,'atLinkMonProbeSampleSize':atLinkMonProbeSampleSize,'atLinkMonProbeEnabled':atLinkMonProbeEnabled,'atLinkMonProbeDetailTable':atLinkMonProbeDetailTable,'atLinkMonProbeDetailEntry':atLinkMonProbeDetailEntry,'atLinkMonProbeDetailProbesSent':atLinkMonProbeDetailProbesSent,'atLinkMonProbeDetailLastTxTime':atLinkMonProbeDetailLastTxTime,'atLinkMonProbeDetailLastRxTime':atLinkMonProbeDetailLastRxTime,'atLinkMonProbeLatestMetricsTable':atLinkMonProbeLatestMetricsTable,'atLinkMonProbeLatestMetricsEntry':atLinkMonProbeLatestMetricsEntry,'atLinkMonProbeLatestMetricsLatency':atLinkMonProbeLatestMetricsLatency,'atLinkMonProbeLatestMetricsJitter':atLinkMonProbeLatestMetricsJitter,'atLinkMonProbeLatestMetricsPktLoss':atLinkMonProbeLatestMetricsPktLoss,'atLinkMonProbeLatestMetricsCnscPktLoss':atLinkMonProbeLatestMetricsCnscPktLoss,'atLinkMonProbeHistoryTable':atLinkMonProbeHistoryTable,'atLinkMonProbeHistoryEntry':atLinkMonProbeHistoryEntry,_G:atLinkMonProbeHistoryID,'atLinkMonProbeHistoryProbeName':atLinkMonProbeHistoryProbeName,'atLinkMonProbeHistoryInterval':atLinkMonProbeHistoryInterval,'atLinkMonProbeHistoryBuckets':atLinkMonProbeHistoryBuckets,'atLinkMonProbeHistoryLastSmplID':atLinkMonProbeHistoryLastSmplID,'atLinkMonProbeHistoryLastSmplTime':atLinkMonProbeHistoryLastSmplTime,'atLinkMonSampleTable':atLinkMonSampleTable,'atLinkMonSampleEntry':atLinkMonSampleEntry,_I:atLinkMonSampleBucket,'atLinkMonSampleLatencySum':atLinkMonSampleLatencySum,'atLinkMonSampleLatencyCount':atLinkMonSampleLatencyCount,'atLinkMonSampleJitterSum':atLinkMonSampleJitterSum,'atLinkMonSampleJitterCount':atLinkMonSampleJitterCount,'atLinkMonSamplePktLossSum':atLinkMonSamplePktLossSum,'atLinkMonSamplePktsTx':atLinkMonSamplePktsTx,'atLinkMonSamplePktsRx':atLinkMonSamplePktsRx})