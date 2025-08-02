_X='adGenMiniDslam3gInfoCircuitIdChanges'
_W='adGenMiniDslam3gInfoDspWarmStartReason'
_V='adGenMiniDslam3gVlanVcVid'
_U='adGenMiniDslam3gVlanVcVci'
_T='adGenMiniDslam3gVlanVcVpi'
_S='adGenMiniDslam3gPerfDailyIntInterval'
_R='adGenMiniDslam3gPerf15MinIntInterval'
_Q='adGenMiniDslam3gMacIndex'
_P='adGenMiniDslam3gInfoUserTempThresh'
_O='adGenMiniDslam3gInfoCurrentTemp'
_N='adGenMiniDslam3gInfoFanNumber'
_M='not-accessible'
_L='adGenMiniDslam3gSpanPowerChannel'
_K='disable'
_J='enable'
_I='ifIndex'
_H='IF-MIB'
_G='ADTRAN-TAMINIDSLAM3G-MIB'
_F='adGenSlotInfoIndex'
_E='ADTRAN-GENSLOT-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adTAMiniDslam3gID,=mibBuilder.importSymbols('ADTRAN-GENMINIDSLAM-MIB','adTAMiniDslam3gID')
adGenSlotInfoIndex,=mibBuilder.importSymbols(_E,_F)
ifIndex,=mibBuilder.importSymbols(_H,_I)
InetAddress,InetAddressPrefixLength,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressPrefixLength','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
adGenMiniDslam3g=ModuleIdentity((1,3,6,1,4,1,664,6,10000,61,5,1))
if mibBuilder.loadTexts:adGenMiniDslam3g.setRevisions(('2014-09-04 00:00','2013-03-22 00:00','2012-06-27 00:00','2011-09-21 00:00','2011-09-09 00:00','2010-10-27 00:00'))
_AdGenMiniDslam3gMib_ObjectIdentity=ObjectIdentity
adGenMiniDslam3gMib=_AdGenMiniDslam3gMib_ObjectIdentity((1,3,6,1,4,1,664,6,10000,61,5,1,1))
_AdGenMiniDslam3gInfoTable_Object=MibTable
adGenMiniDslam3gInfoTable=_AdGenMiniDslam3gInfoTable_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,1))
if mibBuilder.loadTexts:adGenMiniDslam3gInfoTable.setStatus(_A)
_AdGenMiniDslam3gInfoEntry_Object=MibTableRow
adGenMiniDslam3gInfoEntry=_AdGenMiniDslam3gInfoEntry_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,1,1))
adGenMiniDslam3gInfoEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:adGenMiniDslam3gInfoEntry.setStatus(_A)
class _AdGenMiniDslam3gInfoUserTempThresh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-40,125))
_AdGenMiniDslam3gInfoUserTempThresh_Type.__name__=_C
_AdGenMiniDslam3gInfoUserTempThresh_Object=MibTableColumn
adGenMiniDslam3gInfoUserTempThresh=_AdGenMiniDslam3gInfoUserTempThresh_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,1,1,1),_AdGenMiniDslam3gInfoUserTempThresh_Type())
adGenMiniDslam3gInfoUserTempThresh.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenMiniDslam3gInfoUserTempThresh.setStatus(_A)
class _AdGenMiniDslam3gInfoUserTempTrapEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_AdGenMiniDslam3gInfoUserTempTrapEnable_Type.__name__=_C
_AdGenMiniDslam3gInfoUserTempTrapEnable_Object=MibTableColumn
adGenMiniDslam3gInfoUserTempTrapEnable=_AdGenMiniDslam3gInfoUserTempTrapEnable_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,1,1,2),_AdGenMiniDslam3gInfoUserTempTrapEnable_Type())
adGenMiniDslam3gInfoUserTempTrapEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenMiniDslam3gInfoUserTempTrapEnable.setStatus(_A)
class _AdGenMiniDslam3gInfoDspWarmStartEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_AdGenMiniDslam3gInfoDspWarmStartEnable_Type.__name__=_C
_AdGenMiniDslam3gInfoDspWarmStartEnable_Object=MibTableColumn
adGenMiniDslam3gInfoDspWarmStartEnable=_AdGenMiniDslam3gInfoDspWarmStartEnable_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,1,1,3),_AdGenMiniDslam3gInfoDspWarmStartEnable_Type())
adGenMiniDslam3gInfoDspWarmStartEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenMiniDslam3gInfoDspWarmStartEnable.setStatus(_A)
class _AdGenMiniDslam3gInfoCurrentTemp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-40,125))
_AdGenMiniDslam3gInfoCurrentTemp_Type.__name__=_C
_AdGenMiniDslam3gInfoCurrentTemp_Object=MibTableColumn
adGenMiniDslam3gInfoCurrentTemp=_AdGenMiniDslam3gInfoCurrentTemp_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,1,1,4),_AdGenMiniDslam3gInfoCurrentTemp_Type())
adGenMiniDslam3gInfoCurrentTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMiniDslam3gInfoCurrentTemp.setStatus(_A)
class _AdGenMiniDslam3gInfoFanNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,99))
_AdGenMiniDslam3gInfoFanNumber_Type.__name__=_C
_AdGenMiniDslam3gInfoFanNumber_Object=MibTableColumn
adGenMiniDslam3gInfoFanNumber=_AdGenMiniDslam3gInfoFanNumber_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,1,1,5),_AdGenMiniDslam3gInfoFanNumber_Type())
adGenMiniDslam3gInfoFanNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMiniDslam3gInfoFanNumber.setStatus(_A)
_AdGenMiniDslam3gInfoDspWarmStartReason_Type=DisplayString
_AdGenMiniDslam3gInfoDspWarmStartReason_Object=MibTableColumn
adGenMiniDslam3gInfoDspWarmStartReason=_AdGenMiniDslam3gInfoDspWarmStartReason_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,1,1,6),_AdGenMiniDslam3gInfoDspWarmStartReason_Type())
adGenMiniDslam3gInfoDspWarmStartReason.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMiniDslam3gInfoDspWarmStartReason.setStatus(_A)
class _AdGenMiniDslam3gInfoDownstreamRateLimitPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AdGenMiniDslam3gInfoDownstreamRateLimitPriority_Type.__name__=_C
_AdGenMiniDslam3gInfoDownstreamRateLimitPriority_Object=MibTableColumn
adGenMiniDslam3gInfoDownstreamRateLimitPriority=_AdGenMiniDslam3gInfoDownstreamRateLimitPriority_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,1,1,7),_AdGenMiniDslam3gInfoDownstreamRateLimitPriority_Type())
adGenMiniDslam3gInfoDownstreamRateLimitPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenMiniDslam3gInfoDownstreamRateLimitPriority.setStatus(_A)
_AdGenMiniDslam3gInfoCircuitIdChanges_Type=DisplayString
_AdGenMiniDslam3gInfoCircuitIdChanges_Object=MibTableColumn
adGenMiniDslam3gInfoCircuitIdChanges=_AdGenMiniDslam3gInfoCircuitIdChanges_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,1,1,8),_AdGenMiniDslam3gInfoCircuitIdChanges_Type())
adGenMiniDslam3gInfoCircuitIdChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMiniDslam3gInfoCircuitIdChanges.setStatus(_A)
_AdGenMiniDslam3gInfoMCastSessionControlStartIP_Type=IpAddress
_AdGenMiniDslam3gInfoMCastSessionControlStartIP_Object=MibTableColumn
adGenMiniDslam3gInfoMCastSessionControlStartIP=_AdGenMiniDslam3gInfoMCastSessionControlStartIP_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,1,1,9),_AdGenMiniDslam3gInfoMCastSessionControlStartIP_Type())
adGenMiniDslam3gInfoMCastSessionControlStartIP.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenMiniDslam3gInfoMCastSessionControlStartIP.setStatus(_A)
_AdGenMiniDslam3gInfoMCastSessionControlEndIP_Type=IpAddress
_AdGenMiniDslam3gInfoMCastSessionControlEndIP_Object=MibTableColumn
adGenMiniDslam3gInfoMCastSessionControlEndIP=_AdGenMiniDslam3gInfoMCastSessionControlEndIP_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,1,1,10),_AdGenMiniDslam3gInfoMCastSessionControlEndIP_Type())
adGenMiniDslam3gInfoMCastSessionControlEndIP.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenMiniDslam3gInfoMCastSessionControlEndIP.setStatus(_A)
_AdGenMiniDslam3gInfoMCastSessionControlBitrate_Type=Integer32
_AdGenMiniDslam3gInfoMCastSessionControlBitrate_Object=MibTableColumn
adGenMiniDslam3gInfoMCastSessionControlBitrate=_AdGenMiniDslam3gInfoMCastSessionControlBitrate_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,1,1,11),_AdGenMiniDslam3gInfoMCastSessionControlBitrate_Type())
adGenMiniDslam3gInfoMCastSessionControlBitrate.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenMiniDslam3gInfoMCastSessionControlBitrate.setStatus(_A)
_AdGenMiniDslam3gInfoMacAgingTime_Type=Unsigned32
_AdGenMiniDslam3gInfoMacAgingTime_Object=MibTableColumn
adGenMiniDslam3gInfoMacAgingTime=_AdGenMiniDslam3gInfoMacAgingTime_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,1,1,12),_AdGenMiniDslam3gInfoMacAgingTime_Type())
adGenMiniDslam3gInfoMacAgingTime.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenMiniDslam3gInfoMacAgingTime.setStatus(_A)
class _AdGenMiniDslam3gInfoLegacyDeployment_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_AdGenMiniDslam3gInfoLegacyDeployment_Type.__name__=_C
_AdGenMiniDslam3gInfoLegacyDeployment_Object=MibTableColumn
adGenMiniDslam3gInfoLegacyDeployment=_AdGenMiniDslam3gInfoLegacyDeployment_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,1,1,13),_AdGenMiniDslam3gInfoLegacyDeployment_Type())
adGenMiniDslam3gInfoLegacyDeployment.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenMiniDslam3gInfoLegacyDeployment.setStatus(_A)
class _AdGenMiniDslam3gInfoBondingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('atm',1),('efm',2)))
_AdGenMiniDslam3gInfoBondingMode_Type.__name__=_C
_AdGenMiniDslam3gInfoBondingMode_Object=MibTableColumn
adGenMiniDslam3gInfoBondingMode=_AdGenMiniDslam3gInfoBondingMode_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,1,1,14),_AdGenMiniDslam3gInfoBondingMode_Type())
adGenMiniDslam3gInfoBondingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMiniDslam3gInfoBondingMode.setStatus(_A)
_AdGenMiniDslam3gTraps_ObjectIdentity=ObjectIdentity
adGenMiniDslam3gTraps=_AdGenMiniDslam3gTraps_ObjectIdentity((1,3,6,1,4,1,664,6,10000,61,5,1,1,2))
_AdGenMiniDslam3gTrapsv1Patch_ObjectIdentity=ObjectIdentity
adGenMiniDslam3gTrapsv1Patch=_AdGenMiniDslam3gTrapsv1Patch_ObjectIdentity((1,3,6,1,4,1,664,6,10000,61,5,1,1,2,0))
_AdGenMiniDslam3gTestTable_Object=MibTable
adGenMiniDslam3gTestTable=_AdGenMiniDslam3gTestTable_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,3))
if mibBuilder.loadTexts:adGenMiniDslam3gTestTable.setStatus(_A)
_AdGenMiniDslam3gTestEntry_Object=MibTableRow
adGenMiniDslam3gTestEntry=_AdGenMiniDslam3gTestEntry_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,3,1))
adGenMiniDslam3gTestEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:adGenMiniDslam3gTestEntry.setStatus(_A)
class _AdGenMiniDslam3gTestPortNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,48))
_AdGenMiniDslam3gTestPortNumber_Type.__name__=_C
_AdGenMiniDslam3gTestPortNumber_Object=MibTableColumn
adGenMiniDslam3gTestPortNumber=_AdGenMiniDslam3gTestPortNumber_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,3,1,1),_AdGenMiniDslam3gTestPortNumber_Type())
adGenMiniDslam3gTestPortNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenMiniDslam3gTestPortNumber.setStatus(_A)
_AdGenMiniDslam3gTestFilename_Type=DisplayString
_AdGenMiniDslam3gTestFilename_Object=MibTableColumn
adGenMiniDslam3gTestFilename=_AdGenMiniDslam3gTestFilename_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,3,1,2),_AdGenMiniDslam3gTestFilename_Type())
adGenMiniDslam3gTestFilename.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenMiniDslam3gTestFilename.setStatus(_A)
class _AdGenMiniDslam3gSELTTestStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('start',1))
_AdGenMiniDslam3gSELTTestStart_Type.__name__=_C
_AdGenMiniDslam3gSELTTestStart_Object=MibTableColumn
adGenMiniDslam3gSELTTestStart=_AdGenMiniDslam3gSELTTestStart_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,3,1,3),_AdGenMiniDslam3gSELTTestStart_Type())
adGenMiniDslam3gSELTTestStart.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenMiniDslam3gSELTTestStart.setStatus(_A)
class _AdGenMiniDslam3gDELTTestStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('start',1))
_AdGenMiniDslam3gDELTTestStart_Type.__name__=_C
_AdGenMiniDslam3gDELTTestStart_Object=MibTableColumn
adGenMiniDslam3gDELTTestStart=_AdGenMiniDslam3gDELTTestStart_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,3,1,4),_AdGenMiniDslam3gDELTTestStart_Type())
adGenMiniDslam3gDELTTestStart.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenMiniDslam3gDELTTestStart.setStatus(_A)
class _AdGenMiniDslam3gTestStop_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('stop',1))
_AdGenMiniDslam3gTestStop_Type.__name__=_C
_AdGenMiniDslam3gTestStop_Object=MibTableColumn
adGenMiniDslam3gTestStop=_AdGenMiniDslam3gTestStop_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,3,1,5),_AdGenMiniDslam3gTestStop_Type())
adGenMiniDslam3gTestStop.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenMiniDslam3gTestStop.setStatus(_A)
_AdGenMiniDslam3gTestSELTDELTStatus_Type=DisplayString
_AdGenMiniDslam3gTestSELTDELTStatus_Object=MibTableColumn
adGenMiniDslam3gTestSELTDELTStatus=_AdGenMiniDslam3gTestSELTDELTStatus_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,3,1,6),_AdGenMiniDslam3gTestSELTDELTStatus_Type())
adGenMiniDslam3gTestSELTDELTStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMiniDslam3gTestSELTDELTStatus.setStatus(_A)
_AdGenMiniDslam3gAdslProvTable_Object=MibTable
adGenMiniDslam3gAdslProvTable=_AdGenMiniDslam3gAdslProvTable_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,4))
if mibBuilder.loadTexts:adGenMiniDslam3gAdslProvTable.setStatus(_A)
_AdGenMiniDslam3gAdslProvEntry_Object=MibTableRow
adGenMiniDslam3gAdslProvEntry=_AdGenMiniDslam3gAdslProvEntry_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,4,1))
adGenMiniDslam3gAdslProvEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:adGenMiniDslam3gAdslProvEntry.setStatus(_A)
class _AdGenMiniDslam3gAdslProvRetrainUasNe_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_AdGenMiniDslam3gAdslProvRetrainUasNe_Type.__name__=_C
_AdGenMiniDslam3gAdslProvRetrainUasNe_Object=MibTableColumn
adGenMiniDslam3gAdslProvRetrainUasNe=_AdGenMiniDslam3gAdslProvRetrainUasNe_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,4,1,1),_AdGenMiniDslam3gAdslProvRetrainUasNe_Type())
adGenMiniDslam3gAdslProvRetrainUasNe.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenMiniDslam3gAdslProvRetrainUasNe.setStatus(_A)
class _AdGenMiniDslam3gAdslProvRetrainMarginNe_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_AdGenMiniDslam3gAdslProvRetrainMarginNe_Type.__name__=_C
_AdGenMiniDslam3gAdslProvRetrainMarginNe_Object=MibTableColumn
adGenMiniDslam3gAdslProvRetrainMarginNe=_AdGenMiniDslam3gAdslProvRetrainMarginNe_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,4,1,2),_AdGenMiniDslam3gAdslProvRetrainMarginNe_Type())
adGenMiniDslam3gAdslProvRetrainMarginNe.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenMiniDslam3gAdslProvRetrainMarginNe.setStatus(_A)
class _AdGenMiniDslam3gAdslProvRetrainSesFe_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_AdGenMiniDslam3gAdslProvRetrainSesFe_Type.__name__=_C
_AdGenMiniDslam3gAdslProvRetrainSesFe_Object=MibTableColumn
adGenMiniDslam3gAdslProvRetrainSesFe=_AdGenMiniDslam3gAdslProvRetrainSesFe_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,4,1,3),_AdGenMiniDslam3gAdslProvRetrainSesFe_Type())
adGenMiniDslam3gAdslProvRetrainSesFe.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenMiniDslam3gAdslProvRetrainSesFe.setStatus(_A)
class _AdGenMiniDslam3gAdslProvRetrainUasFe_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_AdGenMiniDslam3gAdslProvRetrainUasFe_Type.__name__=_C
_AdGenMiniDslam3gAdslProvRetrainUasFe_Object=MibTableColumn
adGenMiniDslam3gAdslProvRetrainUasFe=_AdGenMiniDslam3gAdslProvRetrainUasFe_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,4,1,4),_AdGenMiniDslam3gAdslProvRetrainUasFe_Type())
adGenMiniDslam3gAdslProvRetrainUasFe.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenMiniDslam3gAdslProvRetrainUasFe.setStatus(_A)
class _AdGenMiniDslam3gAdslProvRetrainMarginFe_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_AdGenMiniDslam3gAdslProvRetrainMarginFe_Type.__name__=_C
_AdGenMiniDslam3gAdslProvRetrainMarginFe_Object=MibTableColumn
adGenMiniDslam3gAdslProvRetrainMarginFe=_AdGenMiniDslam3gAdslProvRetrainMarginFe_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,4,1,5),_AdGenMiniDslam3gAdslProvRetrainMarginFe_Type())
adGenMiniDslam3gAdslProvRetrainMarginFe.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenMiniDslam3gAdslProvRetrainMarginFe.setStatus(_A)
_AdGenMiniDslam3gAdslProvDownstreamRateLimit_Type=Integer32
_AdGenMiniDslam3gAdslProvDownstreamRateLimit_Object=MibTableColumn
adGenMiniDslam3gAdslProvDownstreamRateLimit=_AdGenMiniDslam3gAdslProvDownstreamRateLimit_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,4,1,6),_AdGenMiniDslam3gAdslProvDownstreamRateLimit_Type())
adGenMiniDslam3gAdslProvDownstreamRateLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenMiniDslam3gAdslProvDownstreamRateLimit.setStatus(_A)
_AdGenMiniDslam3gMacTable_Object=MibTable
adGenMiniDslam3gMacTable=_AdGenMiniDslam3gMacTable_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,5))
if mibBuilder.loadTexts:adGenMiniDslam3gMacTable.setStatus(_A)
_AdGenMiniDslam3gMacEntry_Object=MibTableRow
adGenMiniDslam3gMacEntry=_AdGenMiniDslam3gMacEntry_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,5,1))
adGenMiniDslam3gMacEntry.setIndexNames((0,_H,_I),(0,_G,_Q))
if mibBuilder.loadTexts:adGenMiniDslam3gMacEntry.setStatus(_A)
_AdGenMiniDslam3gMacIndex_Type=Unsigned32
_AdGenMiniDslam3gMacIndex_Object=MibTableColumn
adGenMiniDslam3gMacIndex=_AdGenMiniDslam3gMacIndex_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,5,1,1),_AdGenMiniDslam3gMacIndex_Type())
adGenMiniDslam3gMacIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:adGenMiniDslam3gMacIndex.setStatus(_A)
_AdGenMiniDslam3gMacAddress_Type=OctetString
_AdGenMiniDslam3gMacAddress_Object=MibTableColumn
adGenMiniDslam3gMacAddress=_AdGenMiniDslam3gMacAddress_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,5,1,2),_AdGenMiniDslam3gMacAddress_Type())
adGenMiniDslam3gMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMiniDslam3gMacAddress.setStatus(_A)
class _AdGenMiniDslam3gMacVID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_AdGenMiniDslam3gMacVID_Type.__name__=_C
_AdGenMiniDslam3gMacVID_Object=MibTableColumn
adGenMiniDslam3gMacVID=_AdGenMiniDslam3gMacVID_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,5,1,3),_AdGenMiniDslam3gMacVID_Type())
adGenMiniDslam3gMacVID.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMiniDslam3gMacVID.setStatus(_A)
class _AdGenMiniDslam3gMacType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('invalid',2),('dynamic',3),('static',4)))
_AdGenMiniDslam3gMacType_Type.__name__=_C
_AdGenMiniDslam3gMacType_Object=MibTableColumn
adGenMiniDslam3gMacType=_AdGenMiniDslam3gMacType_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,5,1,4),_AdGenMiniDslam3gMacType_Type())
adGenMiniDslam3gMacType.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMiniDslam3gMacType.setStatus(_A)
_AdGenMiniDslam3gMacIP_Type=IpAddress
_AdGenMiniDslam3gMacIP_Object=MibTableColumn
adGenMiniDslam3gMacIP=_AdGenMiniDslam3gMacIP_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,5,1,5),_AdGenMiniDslam3gMacIP_Type())
adGenMiniDslam3gMacIP.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMiniDslam3gMacIP.setStatus(_A)
_AdGenMiniDslam3gMacLeaseTime_Type=Unsigned32
_AdGenMiniDslam3gMacLeaseTime_Object=MibTableColumn
adGenMiniDslam3gMacLeaseTime=_AdGenMiniDslam3gMacLeaseTime_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,5,1,6),_AdGenMiniDslam3gMacLeaseTime_Type())
adGenMiniDslam3gMacLeaseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMiniDslam3gMacLeaseTime.setStatus(_A)
_AdGenMiniDslam3gMacGatewayMac_Type=OctetString
_AdGenMiniDslam3gMacGatewayMac_Object=MibTableColumn
adGenMiniDslam3gMacGatewayMac=_AdGenMiniDslam3gMacGatewayMac_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,5,1,7),_AdGenMiniDslam3gMacGatewayMac_Type())
adGenMiniDslam3gMacGatewayMac.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMiniDslam3gMacGatewayMac.setStatus(_A)
_AdGenMiniDslam3gMacGatewayIP_Type=IpAddress
_AdGenMiniDslam3gMacGatewayIP_Object=MibTableColumn
adGenMiniDslam3gMacGatewayIP=_AdGenMiniDslam3gMacGatewayIP_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,5,1,8),_AdGenMiniDslam3gMacGatewayIP_Type())
adGenMiniDslam3gMacGatewayIP.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMiniDslam3gMacGatewayIP.setStatus(_A)
_AdGenMiniDslam3gMacInterfaceState_Type=Unsigned32
_AdGenMiniDslam3gMacInterfaceState_Object=MibTableColumn
adGenMiniDslam3gMacInterfaceState=_AdGenMiniDslam3gMacInterfaceState_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,5,1,9),_AdGenMiniDslam3gMacInterfaceState_Type())
adGenMiniDslam3gMacInterfaceState.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMiniDslam3gMacInterfaceState.setStatus(_A)
_AdGenMiniDslam3gMacXid_Type=Unsigned32
_AdGenMiniDslam3gMacXid_Object=MibTableColumn
adGenMiniDslam3gMacXid=_AdGenMiniDslam3gMacXid_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,5,1,10),_AdGenMiniDslam3gMacXid_Type())
adGenMiniDslam3gMacXid.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMiniDslam3gMacXid.setStatus(_A)
_AdGenMiniDslam3gMacEncapsulationMode_Type=Unsigned32
_AdGenMiniDslam3gMacEncapsulationMode_Object=MibTableColumn
adGenMiniDslam3gMacEncapsulationMode=_AdGenMiniDslam3gMacEncapsulationMode_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,5,1,11),_AdGenMiniDslam3gMacEncapsulationMode_Type())
adGenMiniDslam3gMacEncapsulationMode.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMiniDslam3gMacEncapsulationMode.setStatus(_A)
_AdGenMiniDslam3gMacStartTime_Type=Unsigned32
_AdGenMiniDslam3gMacStartTime_Object=MibTableColumn
adGenMiniDslam3gMacStartTime=_AdGenMiniDslam3gMacStartTime_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,5,1,12),_AdGenMiniDslam3gMacStartTime_Type())
adGenMiniDslam3gMacStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMiniDslam3gMacStartTime.setStatus(_A)
_AdGenMiniDslam3gMacVpi_Type=Unsigned32
_AdGenMiniDslam3gMacVpi_Object=MibTableColumn
adGenMiniDslam3gMacVpi=_AdGenMiniDslam3gMacVpi_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,5,1,13),_AdGenMiniDslam3gMacVpi_Type())
adGenMiniDslam3gMacVpi.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMiniDslam3gMacVpi.setStatus(_A)
_AdGenMiniDslam3gMacVci_Type=Unsigned32
_AdGenMiniDslam3gMacVci_Object=MibTableColumn
adGenMiniDslam3gMacVci=_AdGenMiniDslam3gMacVci_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,5,1,14),_AdGenMiniDslam3gMacVci_Type())
adGenMiniDslam3gMacVci.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMiniDslam3gMacVci.setStatus(_A)
class _AdGenMiniDslam3gMacCTag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4098))
_AdGenMiniDslam3gMacCTag_Type.__name__=_C
_AdGenMiniDslam3gMacCTag_Object=MibTableColumn
adGenMiniDslam3gMacCTag=_AdGenMiniDslam3gMacCTag_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,5,1,15),_AdGenMiniDslam3gMacCTag_Type())
adGenMiniDslam3gMacCTag.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMiniDslam3gMacCTag.setStatus(_A)
class _AdGenMiniDslam3gMacCEVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4098))
_AdGenMiniDslam3gMacCEVlan_Type.__name__=_C
_AdGenMiniDslam3gMacCEVlan_Object=MibTableColumn
adGenMiniDslam3gMacCEVlan=_AdGenMiniDslam3gMacCEVlan_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,5,1,16),_AdGenMiniDslam3gMacCEVlan_Type())
adGenMiniDslam3gMacCEVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMiniDslam3gMacCEVlan.setStatus(_A)
_AdGenMiniDslam3gMacIpAddressType_Type=InetAddressType
_AdGenMiniDslam3gMacIpAddressType_Object=MibTableColumn
adGenMiniDslam3gMacIpAddressType=_AdGenMiniDslam3gMacIpAddressType_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,5,1,17),_AdGenMiniDslam3gMacIpAddressType_Type())
adGenMiniDslam3gMacIpAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMiniDslam3gMacIpAddressType.setStatus(_A)
_AdGenMiniDslam3gMacIpAddress_Type=InetAddress
_AdGenMiniDslam3gMacIpAddress_Object=MibTableColumn
adGenMiniDslam3gMacIpAddress=_AdGenMiniDslam3gMacIpAddress_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,5,1,18),_AdGenMiniDslam3gMacIpAddress_Type())
adGenMiniDslam3gMacIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMiniDslam3gMacIpAddress.setStatus(_A)
_AdGenMiniDslam3gMacIpAddressPrefix_Type=InetAddressPrefixLength
_AdGenMiniDslam3gMacIpAddressPrefix_Object=MibTableColumn
adGenMiniDslam3gMacIpAddressPrefix=_AdGenMiniDslam3gMacIpAddressPrefix_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,5,1,19),_AdGenMiniDslam3gMacIpAddressPrefix_Type())
adGenMiniDslam3gMacIpAddressPrefix.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMiniDslam3gMacIpAddressPrefix.setStatus(_A)
_AdGenMiniDslam3gPerf_ObjectIdentity=ObjectIdentity
adGenMiniDslam3gPerf=_AdGenMiniDslam3gPerf_ObjectIdentity((1,3,6,1,4,1,664,6,10000,61,5,1,1,6))
_AdGenMiniDslam3gPerf15MinCurrTable_Object=MibTable
adGenMiniDslam3gPerf15MinCurrTable=_AdGenMiniDslam3gPerf15MinCurrTable_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,6,1))
if mibBuilder.loadTexts:adGenMiniDslam3gPerf15MinCurrTable.setStatus(_A)
_AdGenMiniDslam3gPerf15MinCurrEntry_Object=MibTableRow
adGenMiniDslam3gPerf15MinCurrEntry=_AdGenMiniDslam3gPerf15MinCurrEntry_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,6,1,1))
adGenMiniDslam3gPerf15MinCurrEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:adGenMiniDslam3gPerf15MinCurrEntry.setStatus(_A)
_AdGenMiniDslam3gPerf15MinCurrIngressPackets_Type=Counter32
_AdGenMiniDslam3gPerf15MinCurrIngressPackets_Object=MibTableColumn
adGenMiniDslam3gPerf15MinCurrIngressPackets=_AdGenMiniDslam3gPerf15MinCurrIngressPackets_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,6,1,1,1),_AdGenMiniDslam3gPerf15MinCurrIngressPackets_Type())
adGenMiniDslam3gPerf15MinCurrIngressPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMiniDslam3gPerf15MinCurrIngressPackets.setStatus(_A)
_AdGenMiniDslam3gPerf15MinCurrIngressBytes_Type=Counter32
_AdGenMiniDslam3gPerf15MinCurrIngressBytes_Object=MibTableColumn
adGenMiniDslam3gPerf15MinCurrIngressBytes=_AdGenMiniDslam3gPerf15MinCurrIngressBytes_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,6,1,1,2),_AdGenMiniDslam3gPerf15MinCurrIngressBytes_Type())
adGenMiniDslam3gPerf15MinCurrIngressBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMiniDslam3gPerf15MinCurrIngressBytes.setStatus(_A)
_AdGenMiniDslam3gPerf15MinCurrEgressPackets_Type=Counter32
_AdGenMiniDslam3gPerf15MinCurrEgressPackets_Object=MibTableColumn
adGenMiniDslam3gPerf15MinCurrEgressPackets=_AdGenMiniDslam3gPerf15MinCurrEgressPackets_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,6,1,1,3),_AdGenMiniDslam3gPerf15MinCurrEgressPackets_Type())
adGenMiniDslam3gPerf15MinCurrEgressPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMiniDslam3gPerf15MinCurrEgressPackets.setStatus(_A)
_AdGenMiniDslam3gPerf15MinCurrEgressBytes_Type=Counter32
_AdGenMiniDslam3gPerf15MinCurrEgressBytes_Object=MibTableColumn
adGenMiniDslam3gPerf15MinCurrEgressBytes=_AdGenMiniDslam3gPerf15MinCurrEgressBytes_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,6,1,1,4),_AdGenMiniDslam3gPerf15MinCurrEgressBytes_Type())
adGenMiniDslam3gPerf15MinCurrEgressBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMiniDslam3gPerf15MinCurrEgressBytes.setStatus(_A)
_AdGenMiniDslam3gPerf15MinCurrEgressOverflowPackets_Type=Counter32
_AdGenMiniDslam3gPerf15MinCurrEgressOverflowPackets_Object=MibTableColumn
adGenMiniDslam3gPerf15MinCurrEgressOverflowPackets=_AdGenMiniDslam3gPerf15MinCurrEgressOverflowPackets_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,6,1,1,5),_AdGenMiniDslam3gPerf15MinCurrEgressOverflowPackets_Type())
adGenMiniDslam3gPerf15MinCurrEgressOverflowPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMiniDslam3gPerf15MinCurrEgressOverflowPackets.setStatus(_A)
_AdGenMiniDslam3gPerf15MinCurrEgressOverflowBytes_Type=Counter32
_AdGenMiniDslam3gPerf15MinCurrEgressOverflowBytes_Object=MibTableColumn
adGenMiniDslam3gPerf15MinCurrEgressOverflowBytes=_AdGenMiniDslam3gPerf15MinCurrEgressOverflowBytes_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,6,1,1,6),_AdGenMiniDslam3gPerf15MinCurrEgressOverflowBytes_Type())
adGenMiniDslam3gPerf15MinCurrEgressOverflowBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMiniDslam3gPerf15MinCurrEgressOverflowBytes.setStatus(_A)
_AdGenMiniDslam3gPerf15MinCurrValidIntervals_Type=Unsigned32
_AdGenMiniDslam3gPerf15MinCurrValidIntervals_Object=MibTableColumn
adGenMiniDslam3gPerf15MinCurrValidIntervals=_AdGenMiniDslam3gPerf15MinCurrValidIntervals_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,6,1,1,7),_AdGenMiniDslam3gPerf15MinCurrValidIntervals_Type())
adGenMiniDslam3gPerf15MinCurrValidIntervals.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMiniDslam3gPerf15MinCurrValidIntervals.setStatus(_A)
_AdGenMiniDslam3gPerf15MinIntTable_Object=MibTable
adGenMiniDslam3gPerf15MinIntTable=_AdGenMiniDslam3gPerf15MinIntTable_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,6,2))
if mibBuilder.loadTexts:adGenMiniDslam3gPerf15MinIntTable.setStatus(_A)
_AdGenMiniDslam3gPerf15MinIntEntry_Object=MibTableRow
adGenMiniDslam3gPerf15MinIntEntry=_AdGenMiniDslam3gPerf15MinIntEntry_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,6,2,1))
adGenMiniDslam3gPerf15MinIntEntry.setIndexNames((0,_H,_I),(0,_G,_R))
if mibBuilder.loadTexts:adGenMiniDslam3gPerf15MinIntEntry.setStatus(_A)
_AdGenMiniDslam3gPerf15MinIntInterval_Type=Integer32
_AdGenMiniDslam3gPerf15MinIntInterval_Object=MibTableColumn
adGenMiniDslam3gPerf15MinIntInterval=_AdGenMiniDslam3gPerf15MinIntInterval_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,6,2,1,1),_AdGenMiniDslam3gPerf15MinIntInterval_Type())
adGenMiniDslam3gPerf15MinIntInterval.setMaxAccess(_M)
if mibBuilder.loadTexts:adGenMiniDslam3gPerf15MinIntInterval.setStatus(_A)
_AdGenMiniDslam3gPerf15MinIntIngressPackets_Type=Counter32
_AdGenMiniDslam3gPerf15MinIntIngressPackets_Object=MibTableColumn
adGenMiniDslam3gPerf15MinIntIngressPackets=_AdGenMiniDslam3gPerf15MinIntIngressPackets_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,6,2,1,2),_AdGenMiniDslam3gPerf15MinIntIngressPackets_Type())
adGenMiniDslam3gPerf15MinIntIngressPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMiniDslam3gPerf15MinIntIngressPackets.setStatus(_A)
_AdGenMiniDslam3gPerf15MinIntIngressBytes_Type=Counter32
_AdGenMiniDslam3gPerf15MinIntIngressBytes_Object=MibTableColumn
adGenMiniDslam3gPerf15MinIntIngressBytes=_AdGenMiniDslam3gPerf15MinIntIngressBytes_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,6,2,1,3),_AdGenMiniDslam3gPerf15MinIntIngressBytes_Type())
adGenMiniDslam3gPerf15MinIntIngressBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMiniDslam3gPerf15MinIntIngressBytes.setStatus(_A)
_AdGenMiniDslam3gPerf15MinIntEgressPackets_Type=Counter32
_AdGenMiniDslam3gPerf15MinIntEgressPackets_Object=MibTableColumn
adGenMiniDslam3gPerf15MinIntEgressPackets=_AdGenMiniDslam3gPerf15MinIntEgressPackets_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,6,2,1,4),_AdGenMiniDslam3gPerf15MinIntEgressPackets_Type())
adGenMiniDslam3gPerf15MinIntEgressPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMiniDslam3gPerf15MinIntEgressPackets.setStatus(_A)
_AdGenMiniDslam3gPerf15MinIntEgressBytes_Type=Counter32
_AdGenMiniDslam3gPerf15MinIntEgressBytes_Object=MibTableColumn
adGenMiniDslam3gPerf15MinIntEgressBytes=_AdGenMiniDslam3gPerf15MinIntEgressBytes_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,6,2,1,5),_AdGenMiniDslam3gPerf15MinIntEgressBytes_Type())
adGenMiniDslam3gPerf15MinIntEgressBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMiniDslam3gPerf15MinIntEgressBytes.setStatus(_A)
_AdGenMiniDslam3gPerf15MinIntEgressOverflowPackets_Type=Counter32
_AdGenMiniDslam3gPerf15MinIntEgressOverflowPackets_Object=MibTableColumn
adGenMiniDslam3gPerf15MinIntEgressOverflowPackets=_AdGenMiniDslam3gPerf15MinIntEgressOverflowPackets_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,6,2,1,6),_AdGenMiniDslam3gPerf15MinIntEgressOverflowPackets_Type())
adGenMiniDslam3gPerf15MinIntEgressOverflowPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMiniDslam3gPerf15MinIntEgressOverflowPackets.setStatus(_A)
_AdGenMiniDslam3gPerf15MinIntEgressOverflowBytes_Type=Counter32
_AdGenMiniDslam3gPerf15MinIntEgressOverflowBytes_Object=MibTableColumn
adGenMiniDslam3gPerf15MinIntEgressOverflowBytes=_AdGenMiniDslam3gPerf15MinIntEgressOverflowBytes_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,6,2,1,7),_AdGenMiniDslam3gPerf15MinIntEgressOverflowBytes_Type())
adGenMiniDslam3gPerf15MinIntEgressOverflowBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMiniDslam3gPerf15MinIntEgressOverflowBytes.setStatus(_A)
_AdGenMiniDslam3gPerfDailyCurrTable_Object=MibTable
adGenMiniDslam3gPerfDailyCurrTable=_AdGenMiniDslam3gPerfDailyCurrTable_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,6,3))
if mibBuilder.loadTexts:adGenMiniDslam3gPerfDailyCurrTable.setStatus(_A)
_AdGenMiniDslam3gPerfDailyCurrEntry_Object=MibTableRow
adGenMiniDslam3gPerfDailyCurrEntry=_AdGenMiniDslam3gPerfDailyCurrEntry_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,6,3,1))
adGenMiniDslam3gPerfDailyCurrEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:adGenMiniDslam3gPerfDailyCurrEntry.setStatus(_A)
_AdGenMiniDslam3gPerfDailyCurrIngressPackets_Type=Counter32
_AdGenMiniDslam3gPerfDailyCurrIngressPackets_Object=MibTableColumn
adGenMiniDslam3gPerfDailyCurrIngressPackets=_AdGenMiniDslam3gPerfDailyCurrIngressPackets_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,6,3,1,1),_AdGenMiniDslam3gPerfDailyCurrIngressPackets_Type())
adGenMiniDslam3gPerfDailyCurrIngressPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMiniDslam3gPerfDailyCurrIngressPackets.setStatus(_A)
_AdGenMiniDslam3gPerfDailyCurrIngressBytes_Type=Counter32
_AdGenMiniDslam3gPerfDailyCurrIngressBytes_Object=MibTableColumn
adGenMiniDslam3gPerfDailyCurrIngressBytes=_AdGenMiniDslam3gPerfDailyCurrIngressBytes_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,6,3,1,2),_AdGenMiniDslam3gPerfDailyCurrIngressBytes_Type())
adGenMiniDslam3gPerfDailyCurrIngressBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMiniDslam3gPerfDailyCurrIngressBytes.setStatus(_A)
_AdGenMiniDslam3gPerfDailyCurrEgressPackets_Type=Counter32
_AdGenMiniDslam3gPerfDailyCurrEgressPackets_Object=MibTableColumn
adGenMiniDslam3gPerfDailyCurrEgressPackets=_AdGenMiniDslam3gPerfDailyCurrEgressPackets_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,6,3,1,3),_AdGenMiniDslam3gPerfDailyCurrEgressPackets_Type())
adGenMiniDslam3gPerfDailyCurrEgressPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMiniDslam3gPerfDailyCurrEgressPackets.setStatus(_A)
_AdGenMiniDslam3gPerfDailyCurrEgressBytes_Type=Counter32
_AdGenMiniDslam3gPerfDailyCurrEgressBytes_Object=MibTableColumn
adGenMiniDslam3gPerfDailyCurrEgressBytes=_AdGenMiniDslam3gPerfDailyCurrEgressBytes_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,6,3,1,4),_AdGenMiniDslam3gPerfDailyCurrEgressBytes_Type())
adGenMiniDslam3gPerfDailyCurrEgressBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMiniDslam3gPerfDailyCurrEgressBytes.setStatus(_A)
_AdGenMiniDslam3gPerfDailyCurrEgressOverflowPackets_Type=Counter32
_AdGenMiniDslam3gPerfDailyCurrEgressOverflowPackets_Object=MibTableColumn
adGenMiniDslam3gPerfDailyCurrEgressOverflowPackets=_AdGenMiniDslam3gPerfDailyCurrEgressOverflowPackets_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,6,3,1,5),_AdGenMiniDslam3gPerfDailyCurrEgressOverflowPackets_Type())
adGenMiniDslam3gPerfDailyCurrEgressOverflowPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMiniDslam3gPerfDailyCurrEgressOverflowPackets.setStatus(_A)
_AdGenMiniDslam3gPerfDailyCurrEgressOverflowBytes_Type=Counter32
_AdGenMiniDslam3gPerfDailyCurrEgressOverflowBytes_Object=MibTableColumn
adGenMiniDslam3gPerfDailyCurrEgressOverflowBytes=_AdGenMiniDslam3gPerfDailyCurrEgressOverflowBytes_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,6,3,1,6),_AdGenMiniDslam3gPerfDailyCurrEgressOverflowBytes_Type())
adGenMiniDslam3gPerfDailyCurrEgressOverflowBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMiniDslam3gPerfDailyCurrEgressOverflowBytes.setStatus(_A)
_AdGenMiniDslam3gPerfDailyCurrValidIntervals_Type=Unsigned32
_AdGenMiniDslam3gPerfDailyCurrValidIntervals_Object=MibTableColumn
adGenMiniDslam3gPerfDailyCurrValidIntervals=_AdGenMiniDslam3gPerfDailyCurrValidIntervals_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,6,3,1,7),_AdGenMiniDslam3gPerfDailyCurrValidIntervals_Type())
adGenMiniDslam3gPerfDailyCurrValidIntervals.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMiniDslam3gPerfDailyCurrValidIntervals.setStatus(_A)
_AdGenMiniDslam3gPerfDailyIntTable_Object=MibTable
adGenMiniDslam3gPerfDailyIntTable=_AdGenMiniDslam3gPerfDailyIntTable_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,6,4))
if mibBuilder.loadTexts:adGenMiniDslam3gPerfDailyIntTable.setStatus(_A)
_AdGenMiniDslam3gPerfDailyIntEntry_Object=MibTableRow
adGenMiniDslam3gPerfDailyIntEntry=_AdGenMiniDslam3gPerfDailyIntEntry_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,6,4,1))
adGenMiniDslam3gPerfDailyIntEntry.setIndexNames((0,_H,_I),(0,_G,_S))
if mibBuilder.loadTexts:adGenMiniDslam3gPerfDailyIntEntry.setStatus(_A)
_AdGenMiniDslam3gPerfDailyIntInterval_Type=Integer32
_AdGenMiniDslam3gPerfDailyIntInterval_Object=MibTableColumn
adGenMiniDslam3gPerfDailyIntInterval=_AdGenMiniDslam3gPerfDailyIntInterval_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,6,4,1,1),_AdGenMiniDslam3gPerfDailyIntInterval_Type())
adGenMiniDslam3gPerfDailyIntInterval.setMaxAccess(_M)
if mibBuilder.loadTexts:adGenMiniDslam3gPerfDailyIntInterval.setStatus(_A)
_AdGenMiniDslam3gPerfDailyIntIngressPackets_Type=Counter32
_AdGenMiniDslam3gPerfDailyIntIngressPackets_Object=MibTableColumn
adGenMiniDslam3gPerfDailyIntIngressPackets=_AdGenMiniDslam3gPerfDailyIntIngressPackets_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,6,4,1,2),_AdGenMiniDslam3gPerfDailyIntIngressPackets_Type())
adGenMiniDslam3gPerfDailyIntIngressPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMiniDslam3gPerfDailyIntIngressPackets.setStatus(_A)
_AdGenMiniDslam3gPerfDailyIntIngressBytes_Type=Counter32
_AdGenMiniDslam3gPerfDailyIntIngressBytes_Object=MibTableColumn
adGenMiniDslam3gPerfDailyIntIngressBytes=_AdGenMiniDslam3gPerfDailyIntIngressBytes_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,6,4,1,3),_AdGenMiniDslam3gPerfDailyIntIngressBytes_Type())
adGenMiniDslam3gPerfDailyIntIngressBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMiniDslam3gPerfDailyIntIngressBytes.setStatus(_A)
_AdGenMiniDslam3gPerfDailyIntEgressPackets_Type=Counter32
_AdGenMiniDslam3gPerfDailyIntEgressPackets_Object=MibTableColumn
adGenMiniDslam3gPerfDailyIntEgressPackets=_AdGenMiniDslam3gPerfDailyIntEgressPackets_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,6,4,1,4),_AdGenMiniDslam3gPerfDailyIntEgressPackets_Type())
adGenMiniDslam3gPerfDailyIntEgressPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMiniDslam3gPerfDailyIntEgressPackets.setStatus(_A)
_AdGenMiniDslam3gPerfDailyIntEgressBytes_Type=Counter32
_AdGenMiniDslam3gPerfDailyIntEgressBytes_Object=MibTableColumn
adGenMiniDslam3gPerfDailyIntEgressBytes=_AdGenMiniDslam3gPerfDailyIntEgressBytes_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,6,4,1,5),_AdGenMiniDslam3gPerfDailyIntEgressBytes_Type())
adGenMiniDslam3gPerfDailyIntEgressBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMiniDslam3gPerfDailyIntEgressBytes.setStatus(_A)
_AdGenMiniDslam3gPerfDailyIntEgressOverflowPackets_Type=Counter32
_AdGenMiniDslam3gPerfDailyIntEgressOverflowPackets_Object=MibTableColumn
adGenMiniDslam3gPerfDailyIntEgressOverflowPackets=_AdGenMiniDslam3gPerfDailyIntEgressOverflowPackets_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,6,4,1,6),_AdGenMiniDslam3gPerfDailyIntEgressOverflowPackets_Type())
adGenMiniDslam3gPerfDailyIntEgressOverflowPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMiniDslam3gPerfDailyIntEgressOverflowPackets.setStatus(_A)
_AdGenMiniDslam3gPerfDailyIntEgressOverflowBytes_Type=Counter32
_AdGenMiniDslam3gPerfDailyIntEgressOverflowBytes_Object=MibTableColumn
adGenMiniDslam3gPerfDailyIntEgressOverflowBytes=_AdGenMiniDslam3gPerfDailyIntEgressOverflowBytes_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,6,4,1,7),_AdGenMiniDslam3gPerfDailyIntEgressOverflowBytes_Type())
adGenMiniDslam3gPerfDailyIntEgressOverflowBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMiniDslam3gPerfDailyIntEgressOverflowBytes.setStatus(_A)
_AdGenMiniDslam3gVlanVcMapProfileTable_Object=MibTable
adGenMiniDslam3gVlanVcMapProfileTable=_AdGenMiniDslam3gVlanVcMapProfileTable_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,7))
if mibBuilder.loadTexts:adGenMiniDslam3gVlanVcMapProfileTable.setStatus(_A)
_AdGenMiniDslam3gVlanVcMapProfileEntry_Object=MibTableRow
adGenMiniDslam3gVlanVcMapProfileEntry=_AdGenMiniDslam3gVlanVcMapProfileEntry_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,7,1))
adGenMiniDslam3gVlanVcMapProfileEntry.setIndexNames((0,_H,_I),(0,_G,_T),(0,_G,_U),(0,_G,_V))
if mibBuilder.loadTexts:adGenMiniDslam3gVlanVcMapProfileEntry.setStatus(_A)
_AdGenMiniDslam3gVlanVcVpi_Type=Unsigned32
_AdGenMiniDslam3gVlanVcVpi_Object=MibTableColumn
adGenMiniDslam3gVlanVcVpi=_AdGenMiniDslam3gVlanVcVpi_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,7,1,1),_AdGenMiniDslam3gVlanVcVpi_Type())
adGenMiniDslam3gVlanVcVpi.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMiniDslam3gVlanVcVpi.setStatus(_A)
_AdGenMiniDslam3gVlanVcVci_Type=Unsigned32
_AdGenMiniDslam3gVlanVcVci_Object=MibTableColumn
adGenMiniDslam3gVlanVcVci=_AdGenMiniDslam3gVlanVcVci_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,7,1,2),_AdGenMiniDslam3gVlanVcVci_Type())
adGenMiniDslam3gVlanVcVci.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMiniDslam3gVlanVcVci.setStatus(_A)
_AdGenMiniDslam3gVlanVcVid_Type=Unsigned32
_AdGenMiniDslam3gVlanVcVid_Object=MibTableColumn
adGenMiniDslam3gVlanVcVid=_AdGenMiniDslam3gVlanVcVid_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,7,1,3),_AdGenMiniDslam3gVlanVcVid_Type())
adGenMiniDslam3gVlanVcVid.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMiniDslam3gVlanVcVid.setStatus(_A)
_AdGenMiniDslam3gSpanPowerTable_Object=MibTable
adGenMiniDslam3gSpanPowerTable=_AdGenMiniDslam3gSpanPowerTable_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,8))
if mibBuilder.loadTexts:adGenMiniDslam3gSpanPowerTable.setStatus(_A)
_AdGenMiniDslam3gSpanPowerEntry_Object=MibTableRow
adGenMiniDslam3gSpanPowerEntry=_AdGenMiniDslam3gSpanPowerEntry_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,8,1))
adGenMiniDslam3gSpanPowerEntry.setIndexNames((0,_E,_F),(0,_G,_L))
if mibBuilder.loadTexts:adGenMiniDslam3gSpanPowerEntry.setStatus(_A)
_AdGenMiniDslam3gSpanPowerChannel_Type=Unsigned32
_AdGenMiniDslam3gSpanPowerChannel_Object=MibTableColumn
adGenMiniDslam3gSpanPowerChannel=_AdGenMiniDslam3gSpanPowerChannel_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,8,1,1),_AdGenMiniDslam3gSpanPowerChannel_Type())
adGenMiniDslam3gSpanPowerChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMiniDslam3gSpanPowerChannel.setStatus(_A)
class _AdGenMiniDslam3gSpanPowerAlarmEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_AdGenMiniDslam3gSpanPowerAlarmEnable_Type.__name__=_C
_AdGenMiniDslam3gSpanPowerAlarmEnable_Object=MibTableColumn
adGenMiniDslam3gSpanPowerAlarmEnable=_AdGenMiniDslam3gSpanPowerAlarmEnable_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,8,1,2),_AdGenMiniDslam3gSpanPowerAlarmEnable_Type())
adGenMiniDslam3gSpanPowerAlarmEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenMiniDslam3gSpanPowerAlarmEnable.setStatus(_A)
class _AdGenMiniDslam3gSpanPowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('powered',1),('unPowered',2)))
_AdGenMiniDslam3gSpanPowerStatus_Type.__name__=_C
_AdGenMiniDslam3gSpanPowerStatus_Object=MibTableColumn
adGenMiniDslam3gSpanPowerStatus=_AdGenMiniDslam3gSpanPowerStatus_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,8,1,3),_AdGenMiniDslam3gSpanPowerStatus_Type())
adGenMiniDslam3gSpanPowerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMiniDslam3gSpanPowerStatus.setStatus(_A)
_AdGenMiniDslam3gGigeProvTable_Object=MibTable
adGenMiniDslam3gGigeProvTable=_AdGenMiniDslam3gGigeProvTable_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,9))
if mibBuilder.loadTexts:adGenMiniDslam3gGigeProvTable.setStatus(_A)
_AdGenMiniDslam3gGigeProvEntry_Object=MibTableRow
adGenMiniDslam3gGigeProvEntry=_AdGenMiniDslam3gGigeProvEntry_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,9,1))
adGenMiniDslam3gGigeProvEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:adGenMiniDslam3gGigeProvEntry.setStatus(_A)
class _AdGenMiniDslam3gGigeProvRemapPbit0_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AdGenMiniDslam3gGigeProvRemapPbit0_Type.__name__=_C
_AdGenMiniDslam3gGigeProvRemapPbit0_Object=MibTableColumn
adGenMiniDslam3gGigeProvRemapPbit0=_AdGenMiniDslam3gGigeProvRemapPbit0_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,9,1,1),_AdGenMiniDslam3gGigeProvRemapPbit0_Type())
adGenMiniDslam3gGigeProvRemapPbit0.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenMiniDslam3gGigeProvRemapPbit0.setStatus(_A)
class _AdGenMiniDslam3gGigeProvRemapPbit1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AdGenMiniDslam3gGigeProvRemapPbit1_Type.__name__=_C
_AdGenMiniDslam3gGigeProvRemapPbit1_Object=MibTableColumn
adGenMiniDslam3gGigeProvRemapPbit1=_AdGenMiniDslam3gGigeProvRemapPbit1_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,9,1,2),_AdGenMiniDslam3gGigeProvRemapPbit1_Type())
adGenMiniDslam3gGigeProvRemapPbit1.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenMiniDslam3gGigeProvRemapPbit1.setStatus(_A)
class _AdGenMiniDslam3gGigeProvRemapPbit2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AdGenMiniDslam3gGigeProvRemapPbit2_Type.__name__=_C
_AdGenMiniDslam3gGigeProvRemapPbit2_Object=MibTableColumn
adGenMiniDslam3gGigeProvRemapPbit2=_AdGenMiniDslam3gGigeProvRemapPbit2_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,9,1,3),_AdGenMiniDslam3gGigeProvRemapPbit2_Type())
adGenMiniDslam3gGigeProvRemapPbit2.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenMiniDslam3gGigeProvRemapPbit2.setStatus(_A)
class _AdGenMiniDslam3gGigeProvRemapPbit3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AdGenMiniDslam3gGigeProvRemapPbit3_Type.__name__=_C
_AdGenMiniDslam3gGigeProvRemapPbit3_Object=MibTableColumn
adGenMiniDslam3gGigeProvRemapPbit3=_AdGenMiniDslam3gGigeProvRemapPbit3_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,9,1,4),_AdGenMiniDslam3gGigeProvRemapPbit3_Type())
adGenMiniDslam3gGigeProvRemapPbit3.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenMiniDslam3gGigeProvRemapPbit3.setStatus(_A)
class _AdGenMiniDslam3gGigeProvRemapPbit4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AdGenMiniDslam3gGigeProvRemapPbit4_Type.__name__=_C
_AdGenMiniDslam3gGigeProvRemapPbit4_Object=MibTableColumn
adGenMiniDslam3gGigeProvRemapPbit4=_AdGenMiniDslam3gGigeProvRemapPbit4_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,9,1,5),_AdGenMiniDslam3gGigeProvRemapPbit4_Type())
adGenMiniDslam3gGigeProvRemapPbit4.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenMiniDslam3gGigeProvRemapPbit4.setStatus(_A)
class _AdGenMiniDslam3gGigeProvRemapPbit5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AdGenMiniDslam3gGigeProvRemapPbit5_Type.__name__=_C
_AdGenMiniDslam3gGigeProvRemapPbit5_Object=MibTableColumn
adGenMiniDslam3gGigeProvRemapPbit5=_AdGenMiniDslam3gGigeProvRemapPbit5_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,9,1,6),_AdGenMiniDslam3gGigeProvRemapPbit5_Type())
adGenMiniDslam3gGigeProvRemapPbit5.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenMiniDslam3gGigeProvRemapPbit5.setStatus(_A)
class _AdGenMiniDslam3gGigeProvRemapPbit6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AdGenMiniDslam3gGigeProvRemapPbit6_Type.__name__=_C
_AdGenMiniDslam3gGigeProvRemapPbit6_Object=MibTableColumn
adGenMiniDslam3gGigeProvRemapPbit6=_AdGenMiniDslam3gGigeProvRemapPbit6_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,9,1,7),_AdGenMiniDslam3gGigeProvRemapPbit6_Type())
adGenMiniDslam3gGigeProvRemapPbit6.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenMiniDslam3gGigeProvRemapPbit6.setStatus(_A)
class _AdGenMiniDslam3gGigeProvRemapPbit7_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AdGenMiniDslam3gGigeProvRemapPbit7_Type.__name__=_C
_AdGenMiniDslam3gGigeProvRemapPbit7_Object=MibTableColumn
adGenMiniDslam3gGigeProvRemapPbit7=_AdGenMiniDslam3gGigeProvRemapPbit7_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,9,1,8),_AdGenMiniDslam3gGigeProvRemapPbit7_Type())
adGenMiniDslam3gGigeProvRemapPbit7.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenMiniDslam3gGigeProvRemapPbit7.setStatus(_A)
class _AdGenMiniDslam3gGigeProvRemapPbitResetAll_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('reset',1))
_AdGenMiniDslam3gGigeProvRemapPbitResetAll_Type.__name__=_C
_AdGenMiniDslam3gGigeProvRemapPbitResetAll_Object=MibTableColumn
adGenMiniDslam3gGigeProvRemapPbitResetAll=_AdGenMiniDslam3gGigeProvRemapPbitResetAll_Object((1,3,6,1,4,1,664,6,10000,61,5,1,1,9,1,9),_AdGenMiniDslam3gGigeProvRemapPbitResetAll_Type())
adGenMiniDslam3gGigeProvRemapPbitResetAll.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenMiniDslam3gGigeProvRemapPbitResetAll.setStatus(_A)
adGenMiniDslam3gFanFailureActive=NotificationType((1,3,6,1,4,1,664,6,10000,61,5,1,1,2,0,1))
adGenMiniDslam3gFanFailureActive.setObjects(*((_E,_F),(_G,_N)))
if mibBuilder.loadTexts:adGenMiniDslam3gFanFailureActive.setStatus(_A)
adGenMiniDslam3gFanFailureInactive=NotificationType((1,3,6,1,4,1,664,6,10000,61,5,1,1,2,0,2))
adGenMiniDslam3gFanFailureInactive.setObjects(*((_E,_F),(_G,_N)))
if mibBuilder.loadTexts:adGenMiniDslam3gFanFailureInactive.setStatus(_A)
adGenMiniDslam3gFanTrayRemoved=NotificationType((1,3,6,1,4,1,664,6,10000,61,5,1,1,2,0,3))
adGenMiniDslam3gFanTrayRemoved.setObjects((_E,_F))
if mibBuilder.loadTexts:adGenMiniDslam3gFanTrayRemoved.setStatus(_A)
adGenMiniDslam3gFanTrayInserted=NotificationType((1,3,6,1,4,1,664,6,10000,61,5,1,1,2,0,4))
adGenMiniDslam3gFanTrayInserted.setObjects((_E,_F))
if mibBuilder.loadTexts:adGenMiniDslam3gFanTrayInserted.setStatus(_A)
adGenMiniDslam3gUserTempActive=NotificationType((1,3,6,1,4,1,664,6,10000,61,5,1,1,2,0,5))
adGenMiniDslam3gUserTempActive.setObjects(*((_E,_F),(_G,_O),(_G,_P)))
if mibBuilder.loadTexts:adGenMiniDslam3gUserTempActive.setStatus(_A)
adGenMiniDslam3gUserTempCleared=NotificationType((1,3,6,1,4,1,664,6,10000,61,5,1,1,2,0,6))
adGenMiniDslam3gUserTempCleared.setObjects(*((_E,_F),(_G,_O),(_G,_P)))
if mibBuilder.loadTexts:adGenMiniDslam3gUserTempCleared.setStatus(_A)
adGenMiniDslam3gCriticalHiTempActive=NotificationType((1,3,6,1,4,1,664,6,10000,61,5,1,1,2,0,7))
adGenMiniDslam3gCriticalHiTempActive.setObjects((_E,_F))
if mibBuilder.loadTexts:adGenMiniDslam3gCriticalHiTempActive.setStatus(_A)
adGenMiniDslam3gCriticalHiTempCleared=NotificationType((1,3,6,1,4,1,664,6,10000,61,5,1,1,2,0,8))
adGenMiniDslam3gCriticalHiTempCleared.setObjects((_E,_F))
if mibBuilder.loadTexts:adGenMiniDslam3gCriticalHiTempCleared.setStatus(_A)
adGenMiniDslamDspWarmStart=NotificationType((1,3,6,1,4,1,664,6,10000,61,5,1,1,2,0,9))
adGenMiniDslamDspWarmStart.setObjects(*((_E,_F),(_G,_W)))
if mibBuilder.loadTexts:adGenMiniDslamDspWarmStart.setStatus(_A)
adGenMiniDslamImaLinksOutOfOrderActive=NotificationType((1,3,6,1,4,1,664,6,10000,61,5,1,1,2,0,11))
adGenMiniDslamImaLinksOutOfOrderActive.setObjects((_E,_F))
if mibBuilder.loadTexts:adGenMiniDslamImaLinksOutOfOrderActive.setStatus(_A)
adGenMiniDslamImaLinksOutOfOrderCleared=NotificationType((1,3,6,1,4,1,664,6,10000,61,5,1,1,2,0,12))
adGenMiniDslamImaLinksOutOfOrderCleared.setObjects((_E,_F))
if mibBuilder.loadTexts:adGenMiniDslamImaLinksOutOfOrderCleared.setStatus(_A)
adGenMiniDslamConfigErrorActive=NotificationType((1,3,6,1,4,1,664,6,10000,61,5,1,1,2,0,13))
adGenMiniDslamConfigErrorActive.setObjects((_E,_F))
if mibBuilder.loadTexts:adGenMiniDslamConfigErrorActive.setStatus(_A)
adGenMiniDslamConfigErrorCleared=NotificationType((1,3,6,1,4,1,664,6,10000,61,5,1,1,2,0,14))
adGenMiniDslamConfigErrorCleared.setObjects((_E,_F))
if mibBuilder.loadTexts:adGenMiniDslamConfigErrorCleared.setStatus(_A)
adGenMiniDslamCircuitIdChange=NotificationType((1,3,6,1,4,1,664,6,10000,61,5,1,1,2,0,15))
adGenMiniDslamCircuitIdChange.setObjects(*((_E,_F),(_G,_X)))
if mibBuilder.loadTexts:adGenMiniDslamCircuitIdChange.setStatus(_A)
adGenMiniDslamSpanPowerFailureActive=NotificationType((1,3,6,1,4,1,664,6,10000,61,5,1,1,2,0,16))
adGenMiniDslamSpanPowerFailureActive.setObjects(*((_E,_F),(_G,_L)))
if mibBuilder.loadTexts:adGenMiniDslamSpanPowerFailureActive.setStatus(_A)
adGenMiniDslamSpanPowerFailureCleared=NotificationType((1,3,6,1,4,1,664,6,10000,61,5,1,1,2,0,17))
adGenMiniDslamSpanPowerFailureCleared.setObjects(*((_E,_F),(_G,_L)))
if mibBuilder.loadTexts:adGenMiniDslamSpanPowerFailureCleared.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'adGenMiniDslam3g':adGenMiniDslam3g,'adGenMiniDslam3gMib':adGenMiniDslam3gMib,'adGenMiniDslam3gInfoTable':adGenMiniDslam3gInfoTable,'adGenMiniDslam3gInfoEntry':adGenMiniDslam3gInfoEntry,_P:adGenMiniDslam3gInfoUserTempThresh,'adGenMiniDslam3gInfoUserTempTrapEnable':adGenMiniDslam3gInfoUserTempTrapEnable,'adGenMiniDslam3gInfoDspWarmStartEnable':adGenMiniDslam3gInfoDspWarmStartEnable,_O:adGenMiniDslam3gInfoCurrentTemp,_N:adGenMiniDslam3gInfoFanNumber,_W:adGenMiniDslam3gInfoDspWarmStartReason,'adGenMiniDslam3gInfoDownstreamRateLimitPriority':adGenMiniDslam3gInfoDownstreamRateLimitPriority,_X:adGenMiniDslam3gInfoCircuitIdChanges,'adGenMiniDslam3gInfoMCastSessionControlStartIP':adGenMiniDslam3gInfoMCastSessionControlStartIP,'adGenMiniDslam3gInfoMCastSessionControlEndIP':adGenMiniDslam3gInfoMCastSessionControlEndIP,'adGenMiniDslam3gInfoMCastSessionControlBitrate':adGenMiniDslam3gInfoMCastSessionControlBitrate,'adGenMiniDslam3gInfoMacAgingTime':adGenMiniDslam3gInfoMacAgingTime,'adGenMiniDslam3gInfoLegacyDeployment':adGenMiniDslam3gInfoLegacyDeployment,'adGenMiniDslam3gInfoBondingMode':adGenMiniDslam3gInfoBondingMode,'adGenMiniDslam3gTraps':adGenMiniDslam3gTraps,'adGenMiniDslam3gTrapsv1Patch':adGenMiniDslam3gTrapsv1Patch,'adGenMiniDslam3gFanFailureActive':adGenMiniDslam3gFanFailureActive,'adGenMiniDslam3gFanFailureInactive':adGenMiniDslam3gFanFailureInactive,'adGenMiniDslam3gFanTrayRemoved':adGenMiniDslam3gFanTrayRemoved,'adGenMiniDslam3gFanTrayInserted':adGenMiniDslam3gFanTrayInserted,'adGenMiniDslam3gUserTempActive':adGenMiniDslam3gUserTempActive,'adGenMiniDslam3gUserTempCleared':adGenMiniDslam3gUserTempCleared,'adGenMiniDslam3gCriticalHiTempActive':adGenMiniDslam3gCriticalHiTempActive,'adGenMiniDslam3gCriticalHiTempCleared':adGenMiniDslam3gCriticalHiTempCleared,'adGenMiniDslamDspWarmStart':adGenMiniDslamDspWarmStart,'adGenMiniDslamImaLinksOutOfOrderActive':adGenMiniDslamImaLinksOutOfOrderActive,'adGenMiniDslamImaLinksOutOfOrderCleared':adGenMiniDslamImaLinksOutOfOrderCleared,'adGenMiniDslamConfigErrorActive':adGenMiniDslamConfigErrorActive,'adGenMiniDslamConfigErrorCleared':adGenMiniDslamConfigErrorCleared,'adGenMiniDslamCircuitIdChange':adGenMiniDslamCircuitIdChange,'adGenMiniDslamSpanPowerFailureActive':adGenMiniDslamSpanPowerFailureActive,'adGenMiniDslamSpanPowerFailureCleared':adGenMiniDslamSpanPowerFailureCleared,'adGenMiniDslam3gTestTable':adGenMiniDslam3gTestTable,'adGenMiniDslam3gTestEntry':adGenMiniDslam3gTestEntry,'adGenMiniDslam3gTestPortNumber':adGenMiniDslam3gTestPortNumber,'adGenMiniDslam3gTestFilename':adGenMiniDslam3gTestFilename,'adGenMiniDslam3gSELTTestStart':adGenMiniDslam3gSELTTestStart,'adGenMiniDslam3gDELTTestStart':adGenMiniDslam3gDELTTestStart,'adGenMiniDslam3gTestStop':adGenMiniDslam3gTestStop,'adGenMiniDslam3gTestSELTDELTStatus':adGenMiniDslam3gTestSELTDELTStatus,'adGenMiniDslam3gAdslProvTable':adGenMiniDslam3gAdslProvTable,'adGenMiniDslam3gAdslProvEntry':adGenMiniDslam3gAdslProvEntry,'adGenMiniDslam3gAdslProvRetrainUasNe':adGenMiniDslam3gAdslProvRetrainUasNe,'adGenMiniDslam3gAdslProvRetrainMarginNe':adGenMiniDslam3gAdslProvRetrainMarginNe,'adGenMiniDslam3gAdslProvRetrainSesFe':adGenMiniDslam3gAdslProvRetrainSesFe,'adGenMiniDslam3gAdslProvRetrainUasFe':adGenMiniDslam3gAdslProvRetrainUasFe,'adGenMiniDslam3gAdslProvRetrainMarginFe':adGenMiniDslam3gAdslProvRetrainMarginFe,'adGenMiniDslam3gAdslProvDownstreamRateLimit':adGenMiniDslam3gAdslProvDownstreamRateLimit,'adGenMiniDslam3gMacTable':adGenMiniDslam3gMacTable,'adGenMiniDslam3gMacEntry':adGenMiniDslam3gMacEntry,_Q:adGenMiniDslam3gMacIndex,'adGenMiniDslam3gMacAddress':adGenMiniDslam3gMacAddress,'adGenMiniDslam3gMacVID':adGenMiniDslam3gMacVID,'adGenMiniDslam3gMacType':adGenMiniDslam3gMacType,'adGenMiniDslam3gMacIP':adGenMiniDslam3gMacIP,'adGenMiniDslam3gMacLeaseTime':adGenMiniDslam3gMacLeaseTime,'adGenMiniDslam3gMacGatewayMac':adGenMiniDslam3gMacGatewayMac,'adGenMiniDslam3gMacGatewayIP':adGenMiniDslam3gMacGatewayIP,'adGenMiniDslam3gMacInterfaceState':adGenMiniDslam3gMacInterfaceState,'adGenMiniDslam3gMacXid':adGenMiniDslam3gMacXid,'adGenMiniDslam3gMacEncapsulationMode':adGenMiniDslam3gMacEncapsulationMode,'adGenMiniDslam3gMacStartTime':adGenMiniDslam3gMacStartTime,'adGenMiniDslam3gMacVpi':adGenMiniDslam3gMacVpi,'adGenMiniDslam3gMacVci':adGenMiniDslam3gMacVci,'adGenMiniDslam3gMacCTag':adGenMiniDslam3gMacCTag,'adGenMiniDslam3gMacCEVlan':adGenMiniDslam3gMacCEVlan,'adGenMiniDslam3gMacIpAddressType':adGenMiniDslam3gMacIpAddressType,'adGenMiniDslam3gMacIpAddress':adGenMiniDslam3gMacIpAddress,'adGenMiniDslam3gMacIpAddressPrefix':adGenMiniDslam3gMacIpAddressPrefix,'adGenMiniDslam3gPerf':adGenMiniDslam3gPerf,'adGenMiniDslam3gPerf15MinCurrTable':adGenMiniDslam3gPerf15MinCurrTable,'adGenMiniDslam3gPerf15MinCurrEntry':adGenMiniDslam3gPerf15MinCurrEntry,'adGenMiniDslam3gPerf15MinCurrIngressPackets':adGenMiniDslam3gPerf15MinCurrIngressPackets,'adGenMiniDslam3gPerf15MinCurrIngressBytes':adGenMiniDslam3gPerf15MinCurrIngressBytes,'adGenMiniDslam3gPerf15MinCurrEgressPackets':adGenMiniDslam3gPerf15MinCurrEgressPackets,'adGenMiniDslam3gPerf15MinCurrEgressBytes':adGenMiniDslam3gPerf15MinCurrEgressBytes,'adGenMiniDslam3gPerf15MinCurrEgressOverflowPackets':adGenMiniDslam3gPerf15MinCurrEgressOverflowPackets,'adGenMiniDslam3gPerf15MinCurrEgressOverflowBytes':adGenMiniDslam3gPerf15MinCurrEgressOverflowBytes,'adGenMiniDslam3gPerf15MinCurrValidIntervals':adGenMiniDslam3gPerf15MinCurrValidIntervals,'adGenMiniDslam3gPerf15MinIntTable':adGenMiniDslam3gPerf15MinIntTable,'adGenMiniDslam3gPerf15MinIntEntry':adGenMiniDslam3gPerf15MinIntEntry,_R:adGenMiniDslam3gPerf15MinIntInterval,'adGenMiniDslam3gPerf15MinIntIngressPackets':adGenMiniDslam3gPerf15MinIntIngressPackets,'adGenMiniDslam3gPerf15MinIntIngressBytes':adGenMiniDslam3gPerf15MinIntIngressBytes,'adGenMiniDslam3gPerf15MinIntEgressPackets':adGenMiniDslam3gPerf15MinIntEgressPackets,'adGenMiniDslam3gPerf15MinIntEgressBytes':adGenMiniDslam3gPerf15MinIntEgressBytes,'adGenMiniDslam3gPerf15MinIntEgressOverflowPackets':adGenMiniDslam3gPerf15MinIntEgressOverflowPackets,'adGenMiniDslam3gPerf15MinIntEgressOverflowBytes':adGenMiniDslam3gPerf15MinIntEgressOverflowBytes,'adGenMiniDslam3gPerfDailyCurrTable':adGenMiniDslam3gPerfDailyCurrTable,'adGenMiniDslam3gPerfDailyCurrEntry':adGenMiniDslam3gPerfDailyCurrEntry,'adGenMiniDslam3gPerfDailyCurrIngressPackets':adGenMiniDslam3gPerfDailyCurrIngressPackets,'adGenMiniDslam3gPerfDailyCurrIngressBytes':adGenMiniDslam3gPerfDailyCurrIngressBytes,'adGenMiniDslam3gPerfDailyCurrEgressPackets':adGenMiniDslam3gPerfDailyCurrEgressPackets,'adGenMiniDslam3gPerfDailyCurrEgressBytes':adGenMiniDslam3gPerfDailyCurrEgressBytes,'adGenMiniDslam3gPerfDailyCurrEgressOverflowPackets':adGenMiniDslam3gPerfDailyCurrEgressOverflowPackets,'adGenMiniDslam3gPerfDailyCurrEgressOverflowBytes':adGenMiniDslam3gPerfDailyCurrEgressOverflowBytes,'adGenMiniDslam3gPerfDailyCurrValidIntervals':adGenMiniDslam3gPerfDailyCurrValidIntervals,'adGenMiniDslam3gPerfDailyIntTable':adGenMiniDslam3gPerfDailyIntTable,'adGenMiniDslam3gPerfDailyIntEntry':adGenMiniDslam3gPerfDailyIntEntry,_S:adGenMiniDslam3gPerfDailyIntInterval,'adGenMiniDslam3gPerfDailyIntIngressPackets':adGenMiniDslam3gPerfDailyIntIngressPackets,'adGenMiniDslam3gPerfDailyIntIngressBytes':adGenMiniDslam3gPerfDailyIntIngressBytes,'adGenMiniDslam3gPerfDailyIntEgressPackets':adGenMiniDslam3gPerfDailyIntEgressPackets,'adGenMiniDslam3gPerfDailyIntEgressBytes':adGenMiniDslam3gPerfDailyIntEgressBytes,'adGenMiniDslam3gPerfDailyIntEgressOverflowPackets':adGenMiniDslam3gPerfDailyIntEgressOverflowPackets,'adGenMiniDslam3gPerfDailyIntEgressOverflowBytes':adGenMiniDslam3gPerfDailyIntEgressOverflowBytes,'adGenMiniDslam3gVlanVcMapProfileTable':adGenMiniDslam3gVlanVcMapProfileTable,'adGenMiniDslam3gVlanVcMapProfileEntry':adGenMiniDslam3gVlanVcMapProfileEntry,_T:adGenMiniDslam3gVlanVcVpi,_U:adGenMiniDslam3gVlanVcVci,_V:adGenMiniDslam3gVlanVcVid,'adGenMiniDslam3gSpanPowerTable':adGenMiniDslam3gSpanPowerTable,'adGenMiniDslam3gSpanPowerEntry':adGenMiniDslam3gSpanPowerEntry,_L:adGenMiniDslam3gSpanPowerChannel,'adGenMiniDslam3gSpanPowerAlarmEnable':adGenMiniDslam3gSpanPowerAlarmEnable,'adGenMiniDslam3gSpanPowerStatus':adGenMiniDslam3gSpanPowerStatus,'adGenMiniDslam3gGigeProvTable':adGenMiniDslam3gGigeProvTable,'adGenMiniDslam3gGigeProvEntry':adGenMiniDslam3gGigeProvEntry,'adGenMiniDslam3gGigeProvRemapPbit0':adGenMiniDslam3gGigeProvRemapPbit0,'adGenMiniDslam3gGigeProvRemapPbit1':adGenMiniDslam3gGigeProvRemapPbit1,'adGenMiniDslam3gGigeProvRemapPbit2':adGenMiniDslam3gGigeProvRemapPbit2,'adGenMiniDslam3gGigeProvRemapPbit3':adGenMiniDslam3gGigeProvRemapPbit3,'adGenMiniDslam3gGigeProvRemapPbit4':adGenMiniDslam3gGigeProvRemapPbit4,'adGenMiniDslam3gGigeProvRemapPbit5':adGenMiniDslam3gGigeProvRemapPbit5,'adGenMiniDslam3gGigeProvRemapPbit6':adGenMiniDslam3gGigeProvRemapPbit6,'adGenMiniDslam3gGigeProvRemapPbit7':adGenMiniDslam3gGigeProvRemapPbit7,'adGenMiniDslam3gGigeProvRemapPbitResetAll':adGenMiniDslam3gGigeProvRemapPbitResetAll})