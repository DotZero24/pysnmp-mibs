_I='cadCamScaleCardId'
_H='CADANT-SW-MEAS-MIB'
_G='Integer32'
_F='CardId'
_E='OctetString'
_D='ifIndex'
_C='IF-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cadExperimental,=mibBuilder.importSymbols('CADANT-PRODUCTS-MIB','cadExperimental')
CardId,=mibBuilder.importSymbols('CADANT-TC',_F)
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_C,'InterfaceIndex',_D)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
cadSoftwareMeasMib=ModuleIdentity((1,3,6,1,4,1,4998,1,1,100,9))
if mibBuilder.loadTexts:cadSoftwareMeasMib.setRevisions(('2014-09-04 00:00','2012-07-07 00:00','2006-12-14 00:00','2006-04-14 00:00','2006-02-08 00:00','2006-01-30 00:00','2006-01-24 00:00','2006-01-10 00:00','2005-10-11 00:00','2005-08-18 00:00','2003-12-22 00:00','2001-10-23 00:00'))
_CadChassisScaleGroup_ObjectIdentity=ObjectIdentity
cadChassisScaleGroup=_CadChassisScaleGroup_ObjectIdentity((1,3,6,1,4,1,4998,1,1,100,9,1))
_CadantTotalDevices_Type=Unsigned32
_CadantTotalDevices_Object=MibScalar
cadantTotalDevices=_CadantTotalDevices_Object((1,3,6,1,4,1,4998,1,1,100,9,1,1),_CadantTotalDevices_Type())
cadantTotalDevices.setMaxAccess(_B)
if mibBuilder.loadTexts:cadantTotalDevices.setStatus(_A)
_CadantDsBondedDevices_Type=Unsigned32
_CadantDsBondedDevices_Object=MibScalar
cadantDsBondedDevices=_CadantDsBondedDevices_Object((1,3,6,1,4,1,4998,1,1,100,9,1,2),_CadantDsBondedDevices_Type())
cadantDsBondedDevices.setMaxAccess(_B)
if mibBuilder.loadTexts:cadantDsBondedDevices.setStatus(_A)
_CadantUsBondedDevices_Type=Unsigned32
_CadantUsBondedDevices_Object=MibScalar
cadantUsBondedDevices=_CadantUsBondedDevices_Object((1,3,6,1,4,1,4998,1,1,100,9,1,3),_CadantUsBondedDevices_Type())
cadantUsBondedDevices.setMaxAccess(_B)
if mibBuilder.loadTexts:cadantUsBondedDevices.setStatus(_A)
_CadantTotalServiceFlows_Type=Unsigned32
_CadantTotalServiceFlows_Object=MibScalar
cadantTotalServiceFlows=_CadantTotalServiceFlows_Object((1,3,6,1,4,1,4998,1,1,100,9,1,4),_CadantTotalServiceFlows_Type())
cadantTotalServiceFlows.setMaxAccess(_B)
if mibBuilder.loadTexts:cadantTotalServiceFlows.setStatus(_A)
_CadantTotalClassifiers_Type=Unsigned32
_CadantTotalClassifiers_Object=MibScalar
cadantTotalClassifiers=_CadantTotalClassifiers_Object((1,3,6,1,4,1,4998,1,1,100,9,1,5),_CadantTotalClassifiers_Type())
cadantTotalClassifiers.setMaxAccess(_B)
if mibBuilder.loadTexts:cadantTotalClassifiers.setStatus(_A)
_CadantTotalArpEntries_Type=Unsigned32
_CadantTotalArpEntries_Object=MibScalar
cadantTotalArpEntries=_CadantTotalArpEntries_Object((1,3,6,1,4,1,4998,1,1,100,9,1,6),_CadantTotalArpEntries_Type())
cadantTotalArpEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:cadantTotalArpEntries.setStatus(_A)
_CadantTotalIpv4Routes_Type=Unsigned32
_CadantTotalIpv4Routes_Object=MibScalar
cadantTotalIpv4Routes=_CadantTotalIpv4Routes_Object((1,3,6,1,4,1,4998,1,1,100,9,1,7),_CadantTotalIpv4Routes_Type())
cadantTotalIpv4Routes.setMaxAccess(_B)
if mibBuilder.loadTexts:cadantTotalIpv4Routes.setStatus(_A)
_CadantTotalNdEntries_Type=Unsigned32
_CadantTotalNdEntries_Object=MibScalar
cadantTotalNdEntries=_CadantTotalNdEntries_Object((1,3,6,1,4,1,4998,1,1,100,9,1,8),_CadantTotalNdEntries_Type())
cadantTotalNdEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:cadantTotalNdEntries.setStatus(_A)
_CadantTotalIpv6Routes_Type=Unsigned32
_CadantTotalIpv6Routes_Object=MibScalar
cadantTotalIpv6Routes=_CadantTotalIpv6Routes_Object((1,3,6,1,4,1,4998,1,1,100,9,1,9),_CadantTotalIpv6Routes_Type())
cadantTotalIpv6Routes.setMaxAccess(_B)
if mibBuilder.loadTexts:cadantTotalIpv6Routes.setStatus(_A)
_CadantDocsisMulticastStreams_Type=Unsigned32
_CadantDocsisMulticastStreams_Object=MibScalar
cadantDocsisMulticastStreams=_CadantDocsisMulticastStreams_Object((1,3,6,1,4,1,4998,1,1,100,9,1,10),_CadantDocsisMulticastStreams_Type())
cadantDocsisMulticastStreams.setMaxAccess(_B)
if mibBuilder.loadTexts:cadantDocsisMulticastStreams.setStatus(_A)
_CadantVideoMulticastStreams_Type=Unsigned32
_CadantVideoMulticastStreams_Object=MibScalar
cadantVideoMulticastStreams=_CadantVideoMulticastStreams_Object((1,3,6,1,4,1,4998,1,1,100,9,1,11),_CadantVideoMulticastStreams_Type())
cadantVideoMulticastStreams.setMaxAccess(_B)
if mibBuilder.loadTexts:cadantVideoMulticastStreams.setStatus(_A)
_CadantTotalCpe_Type=Unsigned32
_CadantTotalCpe_Object=MibScalar
cadantTotalCpe=_CadantTotalCpe_Object((1,3,6,1,4,1,4998,1,1,100,9,1,12),_CadantTotalCpe_Type())
cadantTotalCpe.setMaxAccess(_B)
if mibBuilder.loadTexts:cadantTotalCpe.setStatus(_A)
_CadSWUChannelMeasTable_Object=MibTable
cadSWUChannelMeasTable=_CadSWUChannelMeasTable_Object((1,3,6,1,4,1,4998,1,1,100,9,2))
if mibBuilder.loadTexts:cadSWUChannelMeasTable.setStatus(_A)
_CadSWUChannelMeasEntry_Object=MibTableRow
cadSWUChannelMeasEntry=_CadSWUChannelMeasEntry_Object((1,3,6,1,4,1,4998,1,1,100,9,2,1))
cadSWUChannelMeasEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:cadSWUChannelMeasEntry.setStatus(_A)
_CadUpChannelRequestSizeMslots_Type=Counter64
_CadUpChannelRequestSizeMslots_Object=MibTableColumn
cadUpChannelRequestSizeMslots=_CadUpChannelRequestSizeMslots_Object((1,3,6,1,4,1,4998,1,1,100,9,2,1,2),_CadUpChannelRequestSizeMslots_Type())
cadUpChannelRequestSizeMslots.setMaxAccess(_B)
if mibBuilder.loadTexts:cadUpChannelRequestSizeMslots.setStatus(_A)
_CadUpChannelInitialMaintSizeMslots_Type=Counter64
_CadUpChannelInitialMaintSizeMslots_Object=MibTableColumn
cadUpChannelInitialMaintSizeMslots=_CadUpChannelInitialMaintSizeMslots_Object((1,3,6,1,4,1,4998,1,1,100,9,2,1,3),_CadUpChannelInitialMaintSizeMslots_Type())
cadUpChannelInitialMaintSizeMslots.setMaxAccess(_B)
if mibBuilder.loadTexts:cadUpChannelInitialMaintSizeMslots.setStatus(_A)
class _CadUpChannelIngressCancellationBandwidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CadUpChannelIngressCancellationBandwidth_Type.__name__=_G
_CadUpChannelIngressCancellationBandwidth_Object=MibTableColumn
cadUpChannelIngressCancellationBandwidth=_CadUpChannelIngressCancellationBandwidth_Object((1,3,6,1,4,1,4998,1,1,100,9,2,1,4),_CadUpChannelIngressCancellationBandwidth_Type())
cadUpChannelIngressCancellationBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:cadUpChannelIngressCancellationBandwidth.setStatus(_A)
if mibBuilder.loadTexts:cadUpChannelIngressCancellationBandwidth.setUnits('percent')
_CadUpChannelAttenuation_Type=Integer32
_CadUpChannelAttenuation_Object=MibTableColumn
cadUpChannelAttenuation=_CadUpChannelAttenuation_Object((1,3,6,1,4,1,4998,1,1,100,9,2,1,5),_CadUpChannelAttenuation_Type())
cadUpChannelAttenuation.setMaxAccess(_B)
if mibBuilder.loadTexts:cadUpChannelAttenuation.setStatus(_A)
class _CadUpChannelRFCalibration_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_CadUpChannelRFCalibration_Type.__name__=_E
_CadUpChannelRFCalibration_Object=MibTableColumn
cadUpChannelRFCalibration=_CadUpChannelRFCalibration_Object((1,3,6,1,4,1,4998,1,1,100,9,2,1,6),_CadUpChannelRFCalibration_Type())
cadUpChannelRFCalibration.setMaxAccess(_B)
if mibBuilder.loadTexts:cadUpChannelRFCalibration.setStatus(_A)
_CadUpChannelTScale_Type=Integer32
_CadUpChannelTScale_Object=MibTableColumn
cadUpChannelTScale=_CadUpChannelTScale_Object((1,3,6,1,4,1,4998,1,1,100,9,2,1,7),_CadUpChannelTScale_Type())
cadUpChannelTScale.setMaxAccess(_B)
if mibBuilder.loadTexts:cadUpChannelTScale.setStatus(_A)
_CadUpChannelSScale_Type=Integer32
_CadUpChannelSScale_Object=MibTableColumn
cadUpChannelSScale=_CadUpChannelSScale_Object((1,3,6,1,4,1,4998,1,1,100,9,2,1,8),_CadUpChannelSScale_Type())
cadUpChannelSScale.setMaxAccess(_B)
if mibBuilder.loadTexts:cadUpChannelSScale.setStatus(_A)
_CadUpChannelStatsTable_Object=MibTable
cadUpChannelStatsTable=_CadUpChannelStatsTable_Object((1,3,6,1,4,1,4998,1,1,100,9,3))
if mibBuilder.loadTexts:cadUpChannelStatsTable.setStatus(_A)
_CadUpChannelStatsEntry_Object=MibTableRow
cadUpChannelStatsEntry=_CadUpChannelStatsEntry_Object((1,3,6,1,4,1,4998,1,1,100,9,3,1))
cadUpChannelStatsEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:cadUpChannelStatsEntry.setStatus(_A)
_CadUpChannelMaxUGSLastOneHour_Type=Unsigned32
_CadUpChannelMaxUGSLastOneHour_Object=MibTableColumn
cadUpChannelMaxUGSLastOneHour=_CadUpChannelMaxUGSLastOneHour_Object((1,3,6,1,4,1,4998,1,1,100,9,3,1,1),_CadUpChannelMaxUGSLastOneHour_Type())
cadUpChannelMaxUGSLastOneHour.setMaxAccess(_B)
if mibBuilder.loadTexts:cadUpChannelMaxUGSLastOneHour.setStatus(_A)
_CadUpChannelAvgUGSLastOneHour_Type=Unsigned32
_CadUpChannelAvgUGSLastOneHour_Object=MibTableColumn
cadUpChannelAvgUGSLastOneHour=_CadUpChannelAvgUGSLastOneHour_Object((1,3,6,1,4,1,4998,1,1,100,9,3,1,2),_CadUpChannelAvgUGSLastOneHour_Type())
cadUpChannelAvgUGSLastOneHour.setMaxAccess(_B)
if mibBuilder.loadTexts:cadUpChannelAvgUGSLastOneHour.setStatus(_A)
_CadUpChannelMinUGSLastOneHour_Type=Unsigned32
_CadUpChannelMinUGSLastOneHour_Object=MibTableColumn
cadUpChannelMinUGSLastOneHour=_CadUpChannelMinUGSLastOneHour_Object((1,3,6,1,4,1,4998,1,1,100,9,3,1,3),_CadUpChannelMinUGSLastOneHour_Type())
cadUpChannelMinUGSLastOneHour.setMaxAccess(_B)
if mibBuilder.loadTexts:cadUpChannelMinUGSLastOneHour.setStatus(_A)
_CadUpChannelMaxUGSLastFiveMins_Type=Unsigned32
_CadUpChannelMaxUGSLastFiveMins_Object=MibTableColumn
cadUpChannelMaxUGSLastFiveMins=_CadUpChannelMaxUGSLastFiveMins_Object((1,3,6,1,4,1,4998,1,1,100,9,3,1,4),_CadUpChannelMaxUGSLastFiveMins_Type())
cadUpChannelMaxUGSLastFiveMins.setMaxAccess(_B)
if mibBuilder.loadTexts:cadUpChannelMaxUGSLastFiveMins.setStatus(_A)
_CadUpChannelAvgUGSLastFiveMins_Type=Unsigned32
_CadUpChannelAvgUGSLastFiveMins_Object=MibTableColumn
cadUpChannelAvgUGSLastFiveMins=_CadUpChannelAvgUGSLastFiveMins_Object((1,3,6,1,4,1,4998,1,1,100,9,3,1,5),_CadUpChannelAvgUGSLastFiveMins_Type())
cadUpChannelAvgUGSLastFiveMins.setMaxAccess(_B)
if mibBuilder.loadTexts:cadUpChannelAvgUGSLastFiveMins.setStatus(_A)
_CadUpChannelMinUGSLastFiveMins_Type=Unsigned32
_CadUpChannelMinUGSLastFiveMins_Object=MibTableColumn
cadUpChannelMinUGSLastFiveMins=_CadUpChannelMinUGSLastFiveMins_Object((1,3,6,1,4,1,4998,1,1,100,9,3,1,6),_CadUpChannelMinUGSLastFiveMins_Type())
cadUpChannelMinUGSLastFiveMins.setMaxAccess(_B)
if mibBuilder.loadTexts:cadUpChannelMinUGSLastFiveMins.setStatus(_A)
_CadUpChannelNormalUGSDeniedLastOneHour_Type=Unsigned32
_CadUpChannelNormalUGSDeniedLastOneHour_Object=MibTableColumn
cadUpChannelNormalUGSDeniedLastOneHour=_CadUpChannelNormalUGSDeniedLastOneHour_Object((1,3,6,1,4,1,4998,1,1,100,9,3,1,7),_CadUpChannelNormalUGSDeniedLastOneHour_Type())
cadUpChannelNormalUGSDeniedLastOneHour.setMaxAccess(_B)
if mibBuilder.loadTexts:cadUpChannelNormalUGSDeniedLastOneHour.setStatus(_A)
_CadUpChannelNormalUGSDeniedLastFiveMins_Type=Unsigned32
_CadUpChannelNormalUGSDeniedLastFiveMins_Object=MibTableColumn
cadUpChannelNormalUGSDeniedLastFiveMins=_CadUpChannelNormalUGSDeniedLastFiveMins_Object((1,3,6,1,4,1,4998,1,1,100,9,3,1,8),_CadUpChannelNormalUGSDeniedLastFiveMins_Type())
cadUpChannelNormalUGSDeniedLastFiveMins.setMaxAccess(_B)
if mibBuilder.loadTexts:cadUpChannelNormalUGSDeniedLastFiveMins.setStatus(_A)
_CadUpChannelEmergencyUGSDeniedLastOneHour_Type=Unsigned32
_CadUpChannelEmergencyUGSDeniedLastOneHour_Object=MibTableColumn
cadUpChannelEmergencyUGSDeniedLastOneHour=_CadUpChannelEmergencyUGSDeniedLastOneHour_Object((1,3,6,1,4,1,4998,1,1,100,9,3,1,9),_CadUpChannelEmergencyUGSDeniedLastOneHour_Type())
cadUpChannelEmergencyUGSDeniedLastOneHour.setMaxAccess(_B)
if mibBuilder.loadTexts:cadUpChannelEmergencyUGSDeniedLastOneHour.setStatus(_A)
_CadUpChannelEmergencyUGSDeniedLastFiveMins_Type=Unsigned32
_CadUpChannelEmergencyUGSDeniedLastFiveMins_Object=MibTableColumn
cadUpChannelEmergencyUGSDeniedLastFiveMins=_CadUpChannelEmergencyUGSDeniedLastFiveMins_Object((1,3,6,1,4,1,4998,1,1,100,9,3,1,10),_CadUpChannelEmergencyUGSDeniedLastFiveMins_Type())
cadUpChannelEmergencyUGSDeniedLastFiveMins.setMaxAccess(_B)
if mibBuilder.loadTexts:cadUpChannelEmergencyUGSDeniedLastFiveMins.setStatus(_A)
_CadUpChannelTotalNormalUGSLastOneHour_Type=Unsigned32
_CadUpChannelTotalNormalUGSLastOneHour_Object=MibTableColumn
cadUpChannelTotalNormalUGSLastOneHour=_CadUpChannelTotalNormalUGSLastOneHour_Object((1,3,6,1,4,1,4998,1,1,100,9,3,1,11),_CadUpChannelTotalNormalUGSLastOneHour_Type())
cadUpChannelTotalNormalUGSLastOneHour.setMaxAccess(_B)
if mibBuilder.loadTexts:cadUpChannelTotalNormalUGSLastOneHour.setStatus(_A)
_CadUpChannelTotalNormalUGSLastFiveMins_Type=Unsigned32
_CadUpChannelTotalNormalUGSLastFiveMins_Object=MibTableColumn
cadUpChannelTotalNormalUGSLastFiveMins=_CadUpChannelTotalNormalUGSLastFiveMins_Object((1,3,6,1,4,1,4998,1,1,100,9,3,1,12),_CadUpChannelTotalNormalUGSLastFiveMins_Type())
cadUpChannelTotalNormalUGSLastFiveMins.setMaxAccess(_B)
if mibBuilder.loadTexts:cadUpChannelTotalNormalUGSLastFiveMins.setStatus(_A)
_CadUpChannelTotalEmergencyUGSLastOneHour_Type=Unsigned32
_CadUpChannelTotalEmergencyUGSLastOneHour_Object=MibTableColumn
cadUpChannelTotalEmergencyUGSLastOneHour=_CadUpChannelTotalEmergencyUGSLastOneHour_Object((1,3,6,1,4,1,4998,1,1,100,9,3,1,13),_CadUpChannelTotalEmergencyUGSLastOneHour_Type())
cadUpChannelTotalEmergencyUGSLastOneHour.setMaxAccess(_B)
if mibBuilder.loadTexts:cadUpChannelTotalEmergencyUGSLastOneHour.setStatus(_A)
_CadUpChannelTotalEmergencyUGSLastFiveMins_Type=Unsigned32
_CadUpChannelTotalEmergencyUGSLastFiveMins_Object=MibTableColumn
cadUpChannelTotalEmergencyUGSLastFiveMins=_CadUpChannelTotalEmergencyUGSLastFiveMins_Object((1,3,6,1,4,1,4998,1,1,100,9,3,1,14),_CadUpChannelTotalEmergencyUGSLastFiveMins_Type())
cadUpChannelTotalEmergencyUGSLastFiveMins.setMaxAccess(_B)
if mibBuilder.loadTexts:cadUpChannelTotalEmergencyUGSLastFiveMins.setStatus(_A)
_CadCamScaleTable_Object=MibTable
cadCamScaleTable=_CadCamScaleTable_Object((1,3,6,1,4,1,4998,1,1,100,9,4))
if mibBuilder.loadTexts:cadCamScaleTable.setStatus(_A)
_CadCamScaleEntry_Object=MibTableRow
cadCamScaleEntry=_CadCamScaleEntry_Object((1,3,6,1,4,1,4998,1,1,100,9,4,1))
cadCamScaleEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:cadCamScaleEntry.setStatus(_A)
class _CadCamScaleCardId_Type(CardId):subtypeSpec=CardId.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6),ValueRangeConstraint(9,14))
_CadCamScaleCardId_Type.__name__=_F
_CadCamScaleCardId_Object=MibTableColumn
cadCamScaleCardId=_CadCamScaleCardId_Object((1,3,6,1,4,1,4998,1,1,100,9,4,1,1),_CadCamScaleCardId_Type())
cadCamScaleCardId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cadCamScaleCardId.setStatus(_A)
_CadCamScaleDevices_Type=Unsigned32
_CadCamScaleDevices_Object=MibTableColumn
cadCamScaleDevices=_CadCamScaleDevices_Object((1,3,6,1,4,1,4998,1,1,100,9,4,1,2),_CadCamScaleDevices_Type())
cadCamScaleDevices.setMaxAccess(_B)
if mibBuilder.loadTexts:cadCamScaleDevices.setStatus(_A)
_CadCamScaleBondedDevices_Type=Unsigned32
_CadCamScaleBondedDevices_Object=MibTableColumn
cadCamScaleBondedDevices=_CadCamScaleBondedDevices_Object((1,3,6,1,4,1,4998,1,1,100,9,4,1,3),_CadCamScaleBondedDevices_Type())
cadCamScaleBondedDevices.setMaxAccess(_B)
if mibBuilder.loadTexts:cadCamScaleBondedDevices.setStatus(_A)
_CadCamScaleServiceFlows_Type=Unsigned32
_CadCamScaleServiceFlows_Object=MibTableColumn
cadCamScaleServiceFlows=_CadCamScaleServiceFlows_Object((1,3,6,1,4,1,4998,1,1,100,9,4,1,4),_CadCamScaleServiceFlows_Type())
cadCamScaleServiceFlows.setMaxAccess(_B)
if mibBuilder.loadTexts:cadCamScaleServiceFlows.setStatus(_A)
_CadCamScaleClassifiers_Type=Unsigned32
_CadCamScaleClassifiers_Object=MibTableColumn
cadCamScaleClassifiers=_CadCamScaleClassifiers_Object((1,3,6,1,4,1,4998,1,1,100,9,4,1,5),_CadCamScaleClassifiers_Type())
cadCamScaleClassifiers.setMaxAccess(_B)
if mibBuilder.loadTexts:cadCamScaleClassifiers.setStatus(_A)
_CadCamScaleIpv4Addresses_Type=Unsigned32
_CadCamScaleIpv4Addresses_Object=MibTableColumn
cadCamScaleIpv4Addresses=_CadCamScaleIpv4Addresses_Object((1,3,6,1,4,1,4998,1,1,100,9,4,1,6),_CadCamScaleIpv4Addresses_Type())
cadCamScaleIpv4Addresses.setMaxAccess(_B)
if mibBuilder.loadTexts:cadCamScaleIpv4Addresses.setStatus(_A)
_CadCamScaleIpv6Addresses_Type=Unsigned32
_CadCamScaleIpv6Addresses_Object=MibTableColumn
cadCamScaleIpv6Addresses=_CadCamScaleIpv6Addresses_Object((1,3,6,1,4,1,4998,1,1,100,9,4,1,7),_CadCamScaleIpv6Addresses_Type())
cadCamScaleIpv6Addresses.setMaxAccess(_B)
if mibBuilder.loadTexts:cadCamScaleIpv6Addresses.setStatus(_A)
_CadCamScaleUsRangeCount_Type=Unsigned32
_CadCamScaleUsRangeCount_Object=MibTableColumn
cadCamScaleUsRangeCount=_CadCamScaleUsRangeCount_Object((1,3,6,1,4,1,4998,1,1,100,9,4,1,8),_CadCamScaleUsRangeCount_Type())
cadCamScaleUsRangeCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cadCamScaleUsRangeCount.setStatus(_A)
_CadCamScaleTotalCpe_Type=Unsigned32
_CadCamScaleTotalCpe_Object=MibTableColumn
cadCamScaleTotalCpe=_CadCamScaleTotalCpe_Object((1,3,6,1,4,1,4998,1,1,100,9,4,1,9),_CadCamScaleTotalCpe_Type())
cadCamScaleTotalCpe.setMaxAccess(_B)
if mibBuilder.loadTexts:cadCamScaleTotalCpe.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'cadSoftwareMeasMib':cadSoftwareMeasMib,'cadChassisScaleGroup':cadChassisScaleGroup,'cadantTotalDevices':cadantTotalDevices,'cadantDsBondedDevices':cadantDsBondedDevices,'cadantUsBondedDevices':cadantUsBondedDevices,'cadantTotalServiceFlows':cadantTotalServiceFlows,'cadantTotalClassifiers':cadantTotalClassifiers,'cadantTotalArpEntries':cadantTotalArpEntries,'cadantTotalIpv4Routes':cadantTotalIpv4Routes,'cadantTotalNdEntries':cadantTotalNdEntries,'cadantTotalIpv6Routes':cadantTotalIpv6Routes,'cadantDocsisMulticastStreams':cadantDocsisMulticastStreams,'cadantVideoMulticastStreams':cadantVideoMulticastStreams,'cadantTotalCpe':cadantTotalCpe,'cadSWUChannelMeasTable':cadSWUChannelMeasTable,'cadSWUChannelMeasEntry':cadSWUChannelMeasEntry,'cadUpChannelRequestSizeMslots':cadUpChannelRequestSizeMslots,'cadUpChannelInitialMaintSizeMslots':cadUpChannelInitialMaintSizeMslots,'cadUpChannelIngressCancellationBandwidth':cadUpChannelIngressCancellationBandwidth,'cadUpChannelAttenuation':cadUpChannelAttenuation,'cadUpChannelRFCalibration':cadUpChannelRFCalibration,'cadUpChannelTScale':cadUpChannelTScale,'cadUpChannelSScale':cadUpChannelSScale,'cadUpChannelStatsTable':cadUpChannelStatsTable,'cadUpChannelStatsEntry':cadUpChannelStatsEntry,'cadUpChannelMaxUGSLastOneHour':cadUpChannelMaxUGSLastOneHour,'cadUpChannelAvgUGSLastOneHour':cadUpChannelAvgUGSLastOneHour,'cadUpChannelMinUGSLastOneHour':cadUpChannelMinUGSLastOneHour,'cadUpChannelMaxUGSLastFiveMins':cadUpChannelMaxUGSLastFiveMins,'cadUpChannelAvgUGSLastFiveMins':cadUpChannelAvgUGSLastFiveMins,'cadUpChannelMinUGSLastFiveMins':cadUpChannelMinUGSLastFiveMins,'cadUpChannelNormalUGSDeniedLastOneHour':cadUpChannelNormalUGSDeniedLastOneHour,'cadUpChannelNormalUGSDeniedLastFiveMins':cadUpChannelNormalUGSDeniedLastFiveMins,'cadUpChannelEmergencyUGSDeniedLastOneHour':cadUpChannelEmergencyUGSDeniedLastOneHour,'cadUpChannelEmergencyUGSDeniedLastFiveMins':cadUpChannelEmergencyUGSDeniedLastFiveMins,'cadUpChannelTotalNormalUGSLastOneHour':cadUpChannelTotalNormalUGSLastOneHour,'cadUpChannelTotalNormalUGSLastFiveMins':cadUpChannelTotalNormalUGSLastFiveMins,'cadUpChannelTotalEmergencyUGSLastOneHour':cadUpChannelTotalEmergencyUGSLastOneHour,'cadUpChannelTotalEmergencyUGSLastFiveMins':cadUpChannelTotalEmergencyUGSLastFiveMins,'cadCamScaleTable':cadCamScaleTable,'cadCamScaleEntry':cadCamScaleEntry,_I:cadCamScaleCardId,'cadCamScaleDevices':cadCamScaleDevices,'cadCamScaleBondedDevices':cadCamScaleBondedDevices,'cadCamScaleServiceFlows':cadCamScaleServiceFlows,'cadCamScaleClassifiers':cadCamScaleClassifiers,'cadCamScaleIpv4Addresses':cadCamScaleIpv4Addresses,'cadCamScaleIpv6Addresses':cadCamScaleIpv6Addresses,'cadCamScaleUsRangeCount':cadCamScaleUsRangeCount,'cadCamScaleTotalCpe':cadCamScaleTotalCpe})