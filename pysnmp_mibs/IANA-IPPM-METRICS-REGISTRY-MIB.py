_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ianaIppmMetricsRegistry=ModuleIdentity((1,3,6,1,2,1,128))
if mibBuilder.loadTexts:ianaIppmMetricsRegistry.setRevisions(('2015-08-14 00:00','2014-05-22 00:00','2010-09-07 00:00','2009-09-02 00:00','2009-04-20 00:00','2006-12-04 00:00','2005-04-12 00:00'))
_IanaIppmMetrics_ObjectIdentity=ObjectIdentity
ianaIppmMetrics=_IanaIppmMetrics_ObjectIdentity((1,3,6,1,2,1,128,1))
if mibBuilder.loadTexts:ianaIppmMetrics.setStatus(_A)
_IetfInstantUnidirConnectivity_ObjectIdentity=ObjectIdentity
ietfInstantUnidirConnectivity=_IetfInstantUnidirConnectivity_ObjectIdentity((1,3,6,1,2,1,128,1,1))
if mibBuilder.loadTexts:ietfInstantUnidirConnectivity.setStatus(_A)
_IetfInstantBidirConnectivity_ObjectIdentity=ObjectIdentity
ietfInstantBidirConnectivity=_IetfInstantBidirConnectivity_ObjectIdentity((1,3,6,1,2,1,128,1,2))
if mibBuilder.loadTexts:ietfInstantBidirConnectivity.setStatus(_A)
_IetfIntervalUnidirConnectivity_ObjectIdentity=ObjectIdentity
ietfIntervalUnidirConnectivity=_IetfIntervalUnidirConnectivity_ObjectIdentity((1,3,6,1,2,1,128,1,3))
if mibBuilder.loadTexts:ietfIntervalUnidirConnectivity.setStatus(_A)
_IetfIntervalBidirConnectivity_ObjectIdentity=ObjectIdentity
ietfIntervalBidirConnectivity=_IetfIntervalBidirConnectivity_ObjectIdentity((1,3,6,1,2,1,128,1,4))
if mibBuilder.loadTexts:ietfIntervalBidirConnectivity.setStatus(_A)
_IetfIntervalTemporalConnectivity_ObjectIdentity=ObjectIdentity
ietfIntervalTemporalConnectivity=_IetfIntervalTemporalConnectivity_ObjectIdentity((1,3,6,1,2,1,128,1,5))
if mibBuilder.loadTexts:ietfIntervalTemporalConnectivity.setStatus(_A)
_IetfOneWayDelay_ObjectIdentity=ObjectIdentity
ietfOneWayDelay=_IetfOneWayDelay_ObjectIdentity((1,3,6,1,2,1,128,1,6))
if mibBuilder.loadTexts:ietfOneWayDelay.setStatus(_A)
_IetfOneWayDelayPoissonStream_ObjectIdentity=ObjectIdentity
ietfOneWayDelayPoissonStream=_IetfOneWayDelayPoissonStream_ObjectIdentity((1,3,6,1,2,1,128,1,7))
if mibBuilder.loadTexts:ietfOneWayDelayPoissonStream.setStatus(_A)
_IetfOneWayDelayPercentile_ObjectIdentity=ObjectIdentity
ietfOneWayDelayPercentile=_IetfOneWayDelayPercentile_ObjectIdentity((1,3,6,1,2,1,128,1,8))
if mibBuilder.loadTexts:ietfOneWayDelayPercentile.setStatus(_A)
_IetfOneWayDelayMedian_ObjectIdentity=ObjectIdentity
ietfOneWayDelayMedian=_IetfOneWayDelayMedian_ObjectIdentity((1,3,6,1,2,1,128,1,9))
if mibBuilder.loadTexts:ietfOneWayDelayMedian.setStatus(_A)
_IetfOneWayDelayMinimum_ObjectIdentity=ObjectIdentity
ietfOneWayDelayMinimum=_IetfOneWayDelayMinimum_ObjectIdentity((1,3,6,1,2,1,128,1,10))
if mibBuilder.loadTexts:ietfOneWayDelayMinimum.setStatus(_A)
_IetfOneWayDelayInversePercentile_ObjectIdentity=ObjectIdentity
ietfOneWayDelayInversePercentile=_IetfOneWayDelayInversePercentile_ObjectIdentity((1,3,6,1,2,1,128,1,11))
if mibBuilder.loadTexts:ietfOneWayDelayInversePercentile.setStatus(_A)
_IetfOneWayPktLoss_ObjectIdentity=ObjectIdentity
ietfOneWayPktLoss=_IetfOneWayPktLoss_ObjectIdentity((1,3,6,1,2,1,128,1,12))
if mibBuilder.loadTexts:ietfOneWayPktLoss.setStatus(_A)
_IetfOneWayPktLossPoissonStream_ObjectIdentity=ObjectIdentity
ietfOneWayPktLossPoissonStream=_IetfOneWayPktLossPoissonStream_ObjectIdentity((1,3,6,1,2,1,128,1,13))
if mibBuilder.loadTexts:ietfOneWayPktLossPoissonStream.setStatus(_A)
_IetfOneWayPktLossAverage_ObjectIdentity=ObjectIdentity
ietfOneWayPktLossAverage=_IetfOneWayPktLossAverage_ObjectIdentity((1,3,6,1,2,1,128,1,14))
if mibBuilder.loadTexts:ietfOneWayPktLossAverage.setStatus(_A)
_IetfRoundTripDelay_ObjectIdentity=ObjectIdentity
ietfRoundTripDelay=_IetfRoundTripDelay_ObjectIdentity((1,3,6,1,2,1,128,1,15))
if mibBuilder.loadTexts:ietfRoundTripDelay.setStatus(_A)
_IetfRoundTripDelayPoissonStream_ObjectIdentity=ObjectIdentity
ietfRoundTripDelayPoissonStream=_IetfRoundTripDelayPoissonStream_ObjectIdentity((1,3,6,1,2,1,128,1,16))
if mibBuilder.loadTexts:ietfRoundTripDelayPoissonStream.setStatus(_A)
_IetfRoundTripDelayPercentile_ObjectIdentity=ObjectIdentity
ietfRoundTripDelayPercentile=_IetfRoundTripDelayPercentile_ObjectIdentity((1,3,6,1,2,1,128,1,17))
if mibBuilder.loadTexts:ietfRoundTripDelayPercentile.setStatus(_A)
_IetfRoundTripDelayMedian_ObjectIdentity=ObjectIdentity
ietfRoundTripDelayMedian=_IetfRoundTripDelayMedian_ObjectIdentity((1,3,6,1,2,1,128,1,18))
if mibBuilder.loadTexts:ietfRoundTripDelayMedian.setStatus(_A)
_IetfRoundTripDelayMinimum_ObjectIdentity=ObjectIdentity
ietfRoundTripDelayMinimum=_IetfRoundTripDelayMinimum_ObjectIdentity((1,3,6,1,2,1,128,1,19))
if mibBuilder.loadTexts:ietfRoundTripDelayMinimum.setStatus(_A)
_IetfRoundTripDelayInvPercentile_ObjectIdentity=ObjectIdentity
ietfRoundTripDelayInvPercentile=_IetfRoundTripDelayInvPercentile_ObjectIdentity((1,3,6,1,2,1,128,1,20))
if mibBuilder.loadTexts:ietfRoundTripDelayInvPercentile.setStatus(_A)
_IetfOneWayLossDistanceStream_ObjectIdentity=ObjectIdentity
ietfOneWayLossDistanceStream=_IetfOneWayLossDistanceStream_ObjectIdentity((1,3,6,1,2,1,128,1,21))
if mibBuilder.loadTexts:ietfOneWayLossDistanceStream.setStatus(_A)
_IetfOneWayLossPeriodStream_ObjectIdentity=ObjectIdentity
ietfOneWayLossPeriodStream=_IetfOneWayLossPeriodStream_ObjectIdentity((1,3,6,1,2,1,128,1,22))
if mibBuilder.loadTexts:ietfOneWayLossPeriodStream.setStatus(_A)
_IetfOneWayLossNoticeableRate_ObjectIdentity=ObjectIdentity
ietfOneWayLossNoticeableRate=_IetfOneWayLossNoticeableRate_ObjectIdentity((1,3,6,1,2,1,128,1,23))
if mibBuilder.loadTexts:ietfOneWayLossNoticeableRate.setStatus(_A)
_IetfOneWayLossPeriodTotal_ObjectIdentity=ObjectIdentity
ietfOneWayLossPeriodTotal=_IetfOneWayLossPeriodTotal_ObjectIdentity((1,3,6,1,2,1,128,1,24))
if mibBuilder.loadTexts:ietfOneWayLossPeriodTotal.setStatus(_A)
_IetfOneWayLossPeriodLengths_ObjectIdentity=ObjectIdentity
ietfOneWayLossPeriodLengths=_IetfOneWayLossPeriodLengths_ObjectIdentity((1,3,6,1,2,1,128,1,25))
if mibBuilder.loadTexts:ietfOneWayLossPeriodLengths.setStatus(_A)
_IetfOneWayInterLossPeriodLengths_ObjectIdentity=ObjectIdentity
ietfOneWayInterLossPeriodLengths=_IetfOneWayInterLossPeriodLengths_ObjectIdentity((1,3,6,1,2,1,128,1,26))
if mibBuilder.loadTexts:ietfOneWayInterLossPeriodLengths.setStatus(_A)
_IetfOneWayIpdv_ObjectIdentity=ObjectIdentity
ietfOneWayIpdv=_IetfOneWayIpdv_ObjectIdentity((1,3,6,1,2,1,128,1,27))
if mibBuilder.loadTexts:ietfOneWayIpdv.setStatus(_A)
_IetfOneWayIpdvPoissonStream_ObjectIdentity=ObjectIdentity
ietfOneWayIpdvPoissonStream=_IetfOneWayIpdvPoissonStream_ObjectIdentity((1,3,6,1,2,1,128,1,28))
if mibBuilder.loadTexts:ietfOneWayIpdvPoissonStream.setStatus(_A)
_IetfOneWayIpdvPercentile_ObjectIdentity=ObjectIdentity
ietfOneWayIpdvPercentile=_IetfOneWayIpdvPercentile_ObjectIdentity((1,3,6,1,2,1,128,1,29))
if mibBuilder.loadTexts:ietfOneWayIpdvPercentile.setStatus(_A)
_IetfOneWayIpdvInversePercentile_ObjectIdentity=ObjectIdentity
ietfOneWayIpdvInversePercentile=_IetfOneWayIpdvInversePercentile_ObjectIdentity((1,3,6,1,2,1,128,1,30))
if mibBuilder.loadTexts:ietfOneWayIpdvInversePercentile.setStatus(_A)
_IetfOneWayIpdvJitter_ObjectIdentity=ObjectIdentity
ietfOneWayIpdvJitter=_IetfOneWayIpdvJitter_ObjectIdentity((1,3,6,1,2,1,128,1,31))
if mibBuilder.loadTexts:ietfOneWayIpdvJitter.setStatus(_A)
_IetfOneWayPeakToPeakIpdv_ObjectIdentity=ObjectIdentity
ietfOneWayPeakToPeakIpdv=_IetfOneWayPeakToPeakIpdv_ObjectIdentity((1,3,6,1,2,1,128,1,32))
if mibBuilder.loadTexts:ietfOneWayPeakToPeakIpdv.setStatus(_A)
_IetfOneWayDelayPeriodicStream_ObjectIdentity=ObjectIdentity
ietfOneWayDelayPeriodicStream=_IetfOneWayDelayPeriodicStream_ObjectIdentity((1,3,6,1,2,1,128,1,33))
if mibBuilder.loadTexts:ietfOneWayDelayPeriodicStream.setStatus(_A)
_IetfReorderedSingleton_ObjectIdentity=ObjectIdentity
ietfReorderedSingleton=_IetfReorderedSingleton_ObjectIdentity((1,3,6,1,2,1,128,1,34))
if mibBuilder.loadTexts:ietfReorderedSingleton.setStatus(_A)
_IetfReorderedPacketRatio_ObjectIdentity=ObjectIdentity
ietfReorderedPacketRatio=_IetfReorderedPacketRatio_ObjectIdentity((1,3,6,1,2,1,128,1,35))
if mibBuilder.loadTexts:ietfReorderedPacketRatio.setStatus(_A)
_IetfReorderingExtent_ObjectIdentity=ObjectIdentity
ietfReorderingExtent=_IetfReorderingExtent_ObjectIdentity((1,3,6,1,2,1,128,1,36))
if mibBuilder.loadTexts:ietfReorderingExtent.setStatus(_A)
_IetfReorderingLateTimeOffset_ObjectIdentity=ObjectIdentity
ietfReorderingLateTimeOffset=_IetfReorderingLateTimeOffset_ObjectIdentity((1,3,6,1,2,1,128,1,37))
if mibBuilder.loadTexts:ietfReorderingLateTimeOffset.setStatus(_A)
_IetfReorderingByteOffset_ObjectIdentity=ObjectIdentity
ietfReorderingByteOffset=_IetfReorderingByteOffset_ObjectIdentity((1,3,6,1,2,1,128,1,38))
if mibBuilder.loadTexts:ietfReorderingByteOffset.setStatus(_A)
_IetfReorderingGap_ObjectIdentity=ObjectIdentity
ietfReorderingGap=_IetfReorderingGap_ObjectIdentity((1,3,6,1,2,1,128,1,39))
if mibBuilder.loadTexts:ietfReorderingGap.setStatus(_A)
_IetfReorderingGapTime_ObjectIdentity=ObjectIdentity
ietfReorderingGapTime=_IetfReorderingGapTime_ObjectIdentity((1,3,6,1,2,1,128,1,40))
if mibBuilder.loadTexts:ietfReorderingGapTime.setStatus(_A)
_IetfReorderingFreeRunx_ObjectIdentity=ObjectIdentity
ietfReorderingFreeRunx=_IetfReorderingFreeRunx_ObjectIdentity((1,3,6,1,2,1,128,1,41))
if mibBuilder.loadTexts:ietfReorderingFreeRunx.setStatus(_A)
_IetfReorderingFreeRunq_ObjectIdentity=ObjectIdentity
ietfReorderingFreeRunq=_IetfReorderingFreeRunq_ObjectIdentity((1,3,6,1,2,1,128,1,42))
if mibBuilder.loadTexts:ietfReorderingFreeRunq.setStatus(_A)
_IetfReorderingFreeRunp_ObjectIdentity=ObjectIdentity
ietfReorderingFreeRunp=_IetfReorderingFreeRunp_ObjectIdentity((1,3,6,1,2,1,128,1,43))
if mibBuilder.loadTexts:ietfReorderingFreeRunp.setStatus(_A)
_IetfReorderingFreeRuna_ObjectIdentity=ObjectIdentity
ietfReorderingFreeRuna=_IetfReorderingFreeRuna_ObjectIdentity((1,3,6,1,2,1,128,1,44))
if mibBuilder.loadTexts:ietfReorderingFreeRuna.setStatus(_A)
_IetfnReordering_ObjectIdentity=ObjectIdentity
ietfnReordering=_IetfnReordering_ObjectIdentity((1,3,6,1,2,1,128,1,45))
if mibBuilder.loadTexts:ietfnReordering.setStatus(_A)
_IetfOneWayPacketArrivalCount_ObjectIdentity=ObjectIdentity
ietfOneWayPacketArrivalCount=_IetfOneWayPacketArrivalCount_ObjectIdentity((1,3,6,1,2,1,128,1,46))
if mibBuilder.loadTexts:ietfOneWayPacketArrivalCount.setStatus(_A)
_IetfOneWayPacketDuplication_ObjectIdentity=ObjectIdentity
ietfOneWayPacketDuplication=_IetfOneWayPacketDuplication_ObjectIdentity((1,3,6,1,2,1,128,1,47))
if mibBuilder.loadTexts:ietfOneWayPacketDuplication.setStatus(_A)
_IetfOneWayPacketDuplicationPoissonStream_ObjectIdentity=ObjectIdentity
ietfOneWayPacketDuplicationPoissonStream=_IetfOneWayPacketDuplicationPoissonStream_ObjectIdentity((1,3,6,1,2,1,128,1,48))
if mibBuilder.loadTexts:ietfOneWayPacketDuplicationPoissonStream.setStatus(_A)
_IetfOneWayPacketDuplicationPeriodicStream_ObjectIdentity=ObjectIdentity
ietfOneWayPacketDuplicationPeriodicStream=_IetfOneWayPacketDuplicationPeriodicStream_ObjectIdentity((1,3,6,1,2,1,128,1,49))
if mibBuilder.loadTexts:ietfOneWayPacketDuplicationPeriodicStream.setStatus(_A)
_IetfOneWayPacketDuplicationFraction_ObjectIdentity=ObjectIdentity
ietfOneWayPacketDuplicationFraction=_IetfOneWayPacketDuplicationFraction_ObjectIdentity((1,3,6,1,2,1,128,1,50))
if mibBuilder.loadTexts:ietfOneWayPacketDuplicationFraction.setStatus(_A)
_IetfOneWayReplicatedPacketRate_ObjectIdentity=ObjectIdentity
ietfOneWayReplicatedPacketRate=_IetfOneWayReplicatedPacketRate_ObjectIdentity((1,3,6,1,2,1,128,1,51))
if mibBuilder.loadTexts:ietfOneWayReplicatedPacketRate.setStatus(_A)
_IetfSpatialOneWayDelayVector_ObjectIdentity=ObjectIdentity
ietfSpatialOneWayDelayVector=_IetfSpatialOneWayDelayVector_ObjectIdentity((1,3,6,1,2,1,128,1,52))
if mibBuilder.loadTexts:ietfSpatialOneWayDelayVector.setStatus(_A)
_IetfSpatialPacketLossVector_ObjectIdentity=ObjectIdentity
ietfSpatialPacketLossVector=_IetfSpatialPacketLossVector_ObjectIdentity((1,3,6,1,2,1,128,1,53))
if mibBuilder.loadTexts:ietfSpatialPacketLossVector.setStatus(_A)
_IetfSpatialOneWayIpdvVector_ObjectIdentity=ObjectIdentity
ietfSpatialOneWayIpdvVector=_IetfSpatialOneWayIpdvVector_ObjectIdentity((1,3,6,1,2,1,128,1,54))
if mibBuilder.loadTexts:ietfSpatialOneWayIpdvVector.setStatus(_A)
_IetfSegmentOneWayDelayStream_ObjectIdentity=ObjectIdentity
ietfSegmentOneWayDelayStream=_IetfSegmentOneWayDelayStream_ObjectIdentity((1,3,6,1,2,1,128,1,55))
if mibBuilder.loadTexts:ietfSegmentOneWayDelayStream.setStatus(_A)
_IetfSegmentPacketLossStream_ObjectIdentity=ObjectIdentity
ietfSegmentPacketLossStream=_IetfSegmentPacketLossStream_ObjectIdentity((1,3,6,1,2,1,128,1,56))
if mibBuilder.loadTexts:ietfSegmentPacketLossStream.setStatus(_A)
_IetfSegmentIpdvPrevStream_ObjectIdentity=ObjectIdentity
ietfSegmentIpdvPrevStream=_IetfSegmentIpdvPrevStream_ObjectIdentity((1,3,6,1,2,1,128,1,57))
if mibBuilder.loadTexts:ietfSegmentIpdvPrevStream.setStatus(_A)
_IetfSegmentIpdvMinStream_ObjectIdentity=ObjectIdentity
ietfSegmentIpdvMinStream=_IetfSegmentIpdvMinStream_ObjectIdentity((1,3,6,1,2,1,128,1,58))
if mibBuilder.loadTexts:ietfSegmentIpdvMinStream.setStatus(_A)
_IetfOneToGroupDelayVector_ObjectIdentity=ObjectIdentity
ietfOneToGroupDelayVector=_IetfOneToGroupDelayVector_ObjectIdentity((1,3,6,1,2,1,128,1,59))
if mibBuilder.loadTexts:ietfOneToGroupDelayVector.setStatus(_A)
_IetfOneToGroupPacketLossVector_ObjectIdentity=ObjectIdentity
ietfOneToGroupPacketLossVector=_IetfOneToGroupPacketLossVector_ObjectIdentity((1,3,6,1,2,1,128,1,60))
if mibBuilder.loadTexts:ietfOneToGroupPacketLossVector.setStatus(_A)
_IetfOneToGroupIpdvVector_ObjectIdentity=ObjectIdentity
ietfOneToGroupIpdvVector=_IetfOneToGroupIpdvVector_ObjectIdentity((1,3,6,1,2,1,128,1,61))
if mibBuilder.loadTexts:ietfOneToGroupIpdvVector.setStatus(_A)
_IetfOnetoGroupReceiverNMeanDelay_ObjectIdentity=ObjectIdentity
ietfOnetoGroupReceiverNMeanDelay=_IetfOnetoGroupReceiverNMeanDelay_ObjectIdentity((1,3,6,1,2,1,128,1,62))
if mibBuilder.loadTexts:ietfOnetoGroupReceiverNMeanDelay.setStatus(_A)
_IetfOneToGroupMeanDelay_ObjectIdentity=ObjectIdentity
ietfOneToGroupMeanDelay=_IetfOneToGroupMeanDelay_ObjectIdentity((1,3,6,1,2,1,128,1,63))
if mibBuilder.loadTexts:ietfOneToGroupMeanDelay.setStatus(_A)
_IetfOneToGroupRangeMeanDelay_ObjectIdentity=ObjectIdentity
ietfOneToGroupRangeMeanDelay=_IetfOneToGroupRangeMeanDelay_ObjectIdentity((1,3,6,1,2,1,128,1,64))
if mibBuilder.loadTexts:ietfOneToGroupRangeMeanDelay.setStatus(_A)
_IetfOneToGroupMaxMeanDelay_ObjectIdentity=ObjectIdentity
ietfOneToGroupMaxMeanDelay=_IetfOneToGroupMaxMeanDelay_ObjectIdentity((1,3,6,1,2,1,128,1,65))
if mibBuilder.loadTexts:ietfOneToGroupMaxMeanDelay.setStatus(_A)
_IetfOneToGroupReceiverNLossRatio_ObjectIdentity=ObjectIdentity
ietfOneToGroupReceiverNLossRatio=_IetfOneToGroupReceiverNLossRatio_ObjectIdentity((1,3,6,1,2,1,128,1,66))
if mibBuilder.loadTexts:ietfOneToGroupReceiverNLossRatio.setStatus(_A)
_IetfOneToGroupReceiverNCompLossRatio_ObjectIdentity=ObjectIdentity
ietfOneToGroupReceiverNCompLossRatio=_IetfOneToGroupReceiverNCompLossRatio_ObjectIdentity((1,3,6,1,2,1,128,1,67))
if mibBuilder.loadTexts:ietfOneToGroupReceiverNCompLossRatio.setStatus(_A)
_IetfOneToGroupLossRatio_ObjectIdentity=ObjectIdentity
ietfOneToGroupLossRatio=_IetfOneToGroupLossRatio_ObjectIdentity((1,3,6,1,2,1,128,1,68))
if mibBuilder.loadTexts:ietfOneToGroupLossRatio.setStatus(_A)
_IetfOneToGroupRangeLossRatio_ObjectIdentity=ObjectIdentity
ietfOneToGroupRangeLossRatio=_IetfOneToGroupRangeLossRatio_ObjectIdentity((1,3,6,1,2,1,128,1,69))
if mibBuilder.loadTexts:ietfOneToGroupRangeLossRatio.setStatus(_A)
_IetfOneToGroupRangeDelayVariation_ObjectIdentity=ObjectIdentity
ietfOneToGroupRangeDelayVariation=_IetfOneToGroupRangeDelayVariation_ObjectIdentity((1,3,6,1,2,1,128,1,70))
if mibBuilder.loadTexts:ietfOneToGroupRangeDelayVariation.setStatus(_A)
_IetfFiniteOneWayDelayStream_ObjectIdentity=ObjectIdentity
ietfFiniteOneWayDelayStream=_IetfFiniteOneWayDelayStream_ObjectIdentity((1,3,6,1,2,1,128,1,71))
if mibBuilder.loadTexts:ietfFiniteOneWayDelayStream.setStatus(_A)
_IetfFiniteOneWayDelayMean_ObjectIdentity=ObjectIdentity
ietfFiniteOneWayDelayMean=_IetfFiniteOneWayDelayMean_ObjectIdentity((1,3,6,1,2,1,128,1,72))
if mibBuilder.loadTexts:ietfFiniteOneWayDelayMean.setStatus(_A)
_IetfCompositeOneWayDelayMean_ObjectIdentity=ObjectIdentity
ietfCompositeOneWayDelayMean=_IetfCompositeOneWayDelayMean_ObjectIdentity((1,3,6,1,2,1,128,1,73))
if mibBuilder.loadTexts:ietfCompositeOneWayDelayMean.setStatus(_A)
_IetfFiniteOneWayDelayMinimum_ObjectIdentity=ObjectIdentity
ietfFiniteOneWayDelayMinimum=_IetfFiniteOneWayDelayMinimum_ObjectIdentity((1,3,6,1,2,1,128,1,74))
if mibBuilder.loadTexts:ietfFiniteOneWayDelayMinimum.setStatus(_A)
_IetfCompositeOneWayDelayMinimum_ObjectIdentity=ObjectIdentity
ietfCompositeOneWayDelayMinimum=_IetfCompositeOneWayDelayMinimum_ObjectIdentity((1,3,6,1,2,1,128,1,75))
if mibBuilder.loadTexts:ietfCompositeOneWayDelayMinimum.setStatus(_A)
_IetfOneWayPktLossEmpiricProb_ObjectIdentity=ObjectIdentity
ietfOneWayPktLossEmpiricProb=_IetfOneWayPktLossEmpiricProb_ObjectIdentity((1,3,6,1,2,1,128,1,76))
if mibBuilder.loadTexts:ietfOneWayPktLossEmpiricProb.setStatus(_A)
_IetfCompositeOneWayPktLossEmpiricProb_ObjectIdentity=ObjectIdentity
ietfCompositeOneWayPktLossEmpiricProb=_IetfCompositeOneWayPktLossEmpiricProb_ObjectIdentity((1,3,6,1,2,1,128,1,77))
if mibBuilder.loadTexts:ietfCompositeOneWayPktLossEmpiricProb.setStatus(_A)
_IetfOneWayPdvRefminStream_ObjectIdentity=ObjectIdentity
ietfOneWayPdvRefminStream=_IetfOneWayPdvRefminStream_ObjectIdentity((1,3,6,1,2,1,128,1,78))
if mibBuilder.loadTexts:ietfOneWayPdvRefminStream.setStatus(_A)
_IetfOneWayPdvRefminMean_ObjectIdentity=ObjectIdentity
ietfOneWayPdvRefminMean=_IetfOneWayPdvRefminMean_ObjectIdentity((1,3,6,1,2,1,128,1,79))
if mibBuilder.loadTexts:ietfOneWayPdvRefminMean.setStatus(_A)
_IetfOneWayPdvRefminVariance_ObjectIdentity=ObjectIdentity
ietfOneWayPdvRefminVariance=_IetfOneWayPdvRefminVariance_ObjectIdentity((1,3,6,1,2,1,128,1,80))
if mibBuilder.loadTexts:ietfOneWayPdvRefminVariance.setStatus(_A)
_IetfOneWayPdvRefminSkewness_ObjectIdentity=ObjectIdentity
ietfOneWayPdvRefminSkewness=_IetfOneWayPdvRefminSkewness_ObjectIdentity((1,3,6,1,2,1,128,1,81))
if mibBuilder.loadTexts:ietfOneWayPdvRefminSkewness.setStatus(_A)
_IetfCompositeOneWayPdvRefminQtil_ObjectIdentity=ObjectIdentity
ietfCompositeOneWayPdvRefminQtil=_IetfCompositeOneWayPdvRefminQtil_ObjectIdentity((1,3,6,1,2,1,128,1,82))
if mibBuilder.loadTexts:ietfCompositeOneWayPdvRefminQtil.setStatus(_A)
_IetfCompositeOneWayPdvRefminNPA_ObjectIdentity=ObjectIdentity
ietfCompositeOneWayPdvRefminNPA=_IetfCompositeOneWayPdvRefminNPA_ObjectIdentity((1,3,6,1,2,1,128,1,83))
if mibBuilder.loadTexts:ietfCompositeOneWayPdvRefminNPA.setStatus(_A)
mibBuilder.exportSymbols('IANA-IPPM-METRICS-REGISTRY-MIB',**{'ianaIppmMetricsRegistry':ianaIppmMetricsRegistry,'ianaIppmMetrics':ianaIppmMetrics,'ietfInstantUnidirConnectivity':ietfInstantUnidirConnectivity,'ietfInstantBidirConnectivity':ietfInstantBidirConnectivity,'ietfIntervalUnidirConnectivity':ietfIntervalUnidirConnectivity,'ietfIntervalBidirConnectivity':ietfIntervalBidirConnectivity,'ietfIntervalTemporalConnectivity':ietfIntervalTemporalConnectivity,'ietfOneWayDelay':ietfOneWayDelay,'ietfOneWayDelayPoissonStream':ietfOneWayDelayPoissonStream,'ietfOneWayDelayPercentile':ietfOneWayDelayPercentile,'ietfOneWayDelayMedian':ietfOneWayDelayMedian,'ietfOneWayDelayMinimum':ietfOneWayDelayMinimum,'ietfOneWayDelayInversePercentile':ietfOneWayDelayInversePercentile,'ietfOneWayPktLoss':ietfOneWayPktLoss,'ietfOneWayPktLossPoissonStream':ietfOneWayPktLossPoissonStream,'ietfOneWayPktLossAverage':ietfOneWayPktLossAverage,'ietfRoundTripDelay':ietfRoundTripDelay,'ietfRoundTripDelayPoissonStream':ietfRoundTripDelayPoissonStream,'ietfRoundTripDelayPercentile':ietfRoundTripDelayPercentile,'ietfRoundTripDelayMedian':ietfRoundTripDelayMedian,'ietfRoundTripDelayMinimum':ietfRoundTripDelayMinimum,'ietfRoundTripDelayInvPercentile':ietfRoundTripDelayInvPercentile,'ietfOneWayLossDistanceStream':ietfOneWayLossDistanceStream,'ietfOneWayLossPeriodStream':ietfOneWayLossPeriodStream,'ietfOneWayLossNoticeableRate':ietfOneWayLossNoticeableRate,'ietfOneWayLossPeriodTotal':ietfOneWayLossPeriodTotal,'ietfOneWayLossPeriodLengths':ietfOneWayLossPeriodLengths,'ietfOneWayInterLossPeriodLengths':ietfOneWayInterLossPeriodLengths,'ietfOneWayIpdv':ietfOneWayIpdv,'ietfOneWayIpdvPoissonStream':ietfOneWayIpdvPoissonStream,'ietfOneWayIpdvPercentile':ietfOneWayIpdvPercentile,'ietfOneWayIpdvInversePercentile':ietfOneWayIpdvInversePercentile,'ietfOneWayIpdvJitter':ietfOneWayIpdvJitter,'ietfOneWayPeakToPeakIpdv':ietfOneWayPeakToPeakIpdv,'ietfOneWayDelayPeriodicStream':ietfOneWayDelayPeriodicStream,'ietfReorderedSingleton':ietfReorderedSingleton,'ietfReorderedPacketRatio':ietfReorderedPacketRatio,'ietfReorderingExtent':ietfReorderingExtent,'ietfReorderingLateTimeOffset':ietfReorderingLateTimeOffset,'ietfReorderingByteOffset':ietfReorderingByteOffset,'ietfReorderingGap':ietfReorderingGap,'ietfReorderingGapTime':ietfReorderingGapTime,'ietfReorderingFreeRunx':ietfReorderingFreeRunx,'ietfReorderingFreeRunq':ietfReorderingFreeRunq,'ietfReorderingFreeRunp':ietfReorderingFreeRunp,'ietfReorderingFreeRuna':ietfReorderingFreeRuna,'ietfnReordering':ietfnReordering,'ietfOneWayPacketArrivalCount':ietfOneWayPacketArrivalCount,'ietfOneWayPacketDuplication':ietfOneWayPacketDuplication,'ietfOneWayPacketDuplicationPoissonStream':ietfOneWayPacketDuplicationPoissonStream,'ietfOneWayPacketDuplicationPeriodicStream':ietfOneWayPacketDuplicationPeriodicStream,'ietfOneWayPacketDuplicationFraction':ietfOneWayPacketDuplicationFraction,'ietfOneWayReplicatedPacketRate':ietfOneWayReplicatedPacketRate,'ietfSpatialOneWayDelayVector':ietfSpatialOneWayDelayVector,'ietfSpatialPacketLossVector':ietfSpatialPacketLossVector,'ietfSpatialOneWayIpdvVector':ietfSpatialOneWayIpdvVector,'ietfSegmentOneWayDelayStream':ietfSegmentOneWayDelayStream,'ietfSegmentPacketLossStream':ietfSegmentPacketLossStream,'ietfSegmentIpdvPrevStream':ietfSegmentIpdvPrevStream,'ietfSegmentIpdvMinStream':ietfSegmentIpdvMinStream,'ietfOneToGroupDelayVector':ietfOneToGroupDelayVector,'ietfOneToGroupPacketLossVector':ietfOneToGroupPacketLossVector,'ietfOneToGroupIpdvVector':ietfOneToGroupIpdvVector,'ietfOnetoGroupReceiverNMeanDelay':ietfOnetoGroupReceiverNMeanDelay,'ietfOneToGroupMeanDelay':ietfOneToGroupMeanDelay,'ietfOneToGroupRangeMeanDelay':ietfOneToGroupRangeMeanDelay,'ietfOneToGroupMaxMeanDelay':ietfOneToGroupMaxMeanDelay,'ietfOneToGroupReceiverNLossRatio':ietfOneToGroupReceiverNLossRatio,'ietfOneToGroupReceiverNCompLossRatio':ietfOneToGroupReceiverNCompLossRatio,'ietfOneToGroupLossRatio':ietfOneToGroupLossRatio,'ietfOneToGroupRangeLossRatio':ietfOneToGroupRangeLossRatio,'ietfOneToGroupRangeDelayVariation':ietfOneToGroupRangeDelayVariation,'ietfFiniteOneWayDelayStream':ietfFiniteOneWayDelayStream,'ietfFiniteOneWayDelayMean':ietfFiniteOneWayDelayMean,'ietfCompositeOneWayDelayMean':ietfCompositeOneWayDelayMean,'ietfFiniteOneWayDelayMinimum':ietfFiniteOneWayDelayMinimum,'ietfCompositeOneWayDelayMinimum':ietfCompositeOneWayDelayMinimum,'ietfOneWayPktLossEmpiricProb':ietfOneWayPktLossEmpiricProb,'ietfCompositeOneWayPktLossEmpiricProb':ietfCompositeOneWayPktLossEmpiricProb,'ietfOneWayPdvRefminStream':ietfOneWayPdvRefminStream,'ietfOneWayPdvRefminMean':ietfOneWayPdvRefminMean,'ietfOneWayPdvRefminVariance':ietfOneWayPdvRefminVariance,'ietfOneWayPdvRefminSkewness':ietfOneWayPdvRefminSkewness,'ietfCompositeOneWayPdvRefminQtil':ietfCompositeOneWayPdvRefminQtil,'ietfCompositeOneWayPdvRefminNPA':ietfCompositeOneWayPdvRefminNPA})