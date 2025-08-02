_q='bandCtpGroup'
_p='bandCtpTargetLineOutputPower'
_o='bandCtpTxVOA'
_n='bandCtpDemuxFreqSlotAttenProfile'
_m='bandCtpMuxFreqSlotAttenProfile'
_l='bandCtpTxEDFAInputPowerOffset'
_k='bandCtpRxEDFATilt'
_j='bandCtpRxEDFAGain'
_i='bandCtpRxEDFAGainModeValue'
_h='bandCtpRxEDFAGainMode'
_g='bandCtpTeInterfaceList'
_f='bandCtpSlotOperatingMode'
_e='bandCtpALSDisableMode'
_d='bandCtpCustomMargin'
_c='bandCtpSpanLoss2ThldReporting'
_b='bandCtpSpanLoss2HighThreshold'
_a='bandCtpSpanLoss2LowThreshold'
_Z='bandCtpCBandOlosSoakTime'
_Y='bandCtpOprHighThreshold'
_X='bandCtpOprLowThreshold'
_W='bandCtpPmHistStatsEnable'
_V='bandCtpALSDisableTime'
_U='bandCtpALSAction'
_T='bandCtpMaxEngineeredSpanLoss'
_S='bandCtpSpanLossReporting'
_R='bandCtpExpectedSpanLoss'
_Q='bandCtpSpanLoss1ThldReporting'
_P='bandCtpSpanLoss1HighThreshold'
_O='bandCtpSpanLoss1LowThreshold'
_N='bandCtpRxExpectedPowerNominal'
_M='bandCtpChannelPlan'
_L='bandCtpMaxOCGs'
_K='ifIndex'
_J='IF-MIB'
_I='0.1 db'
_H='enabled'
_G='disabled'
_F='read-only'
_E='FloatTenths'
_D='Integer32'
_C='read-write'
_B='INFINERA-TP-BANDCTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_J,_K)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
FloatArbitraryPrecision,FloatTenths,InfnALSDisableMode,InfnReporting,InfnRxEDFAGainMode,InfnSlotOperatingMode=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatArbitraryPrecision',_E,'InfnALSDisableMode','InfnReporting','InfnRxEDFAGainMode','InfnSlotOperatingMode')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
bandCtpMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,2))
if mibBuilder.loadTexts:bandCtpMIB.setRevisions(('2008-10-20 00:00',))
_BandCtpTable_Object=MibTable
bandCtpTable=_BandCtpTable_Object((1,3,6,1,4,1,21296,2,2,2,2,2,1))
if mibBuilder.loadTexts:bandCtpTable.setStatus(_A)
_BandCtpEntry_Object=MibTableRow
bandCtpEntry=_BandCtpEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,2,1,1))
bandCtpEntry.setIndexNames((0,_J,_K))
if mibBuilder.loadTexts:bandCtpEntry.setStatus(_A)
class _BandCtpMaxOCGs_Type(Integer32):defaultValue=0
_BandCtpMaxOCGs_Type.__name__=_D
_BandCtpMaxOCGs_Object=MibTableColumn
bandCtpMaxOCGs=_BandCtpMaxOCGs_Object((1,3,6,1,4,1,21296,2,2,2,2,2,1,1,1),_BandCtpMaxOCGs_Type())
bandCtpMaxOCGs.setMaxAccess(_F)
if mibBuilder.loadTexts:bandCtpMaxOCGs.setStatus(_A)
class _BandCtpChannelPlan_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('unknown',1),('odd',2),('even',3),('all',4)))
_BandCtpChannelPlan_Type.__name__=_D
_BandCtpChannelPlan_Object=MibTableColumn
bandCtpChannelPlan=_BandCtpChannelPlan_Object((1,3,6,1,4,1,21296,2,2,2,2,2,1,1,2),_BandCtpChannelPlan_Type())
bandCtpChannelPlan.setMaxAccess(_F)
if mibBuilder.loadTexts:bandCtpChannelPlan.setStatus(_A)
class _BandCtpRxExpectedPowerNominal_Type(FloatTenths):defaultValue=-400;subtypeSpec=FloatTenths.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-400,-10))
_BandCtpRxExpectedPowerNominal_Type.__name__=_E
_BandCtpRxExpectedPowerNominal_Object=MibTableColumn
bandCtpRxExpectedPowerNominal=_BandCtpRxExpectedPowerNominal_Object((1,3,6,1,4,1,21296,2,2,2,2,2,1,1,3),_BandCtpRxExpectedPowerNominal_Type())
bandCtpRxExpectedPowerNominal.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpRxExpectedPowerNominal.setStatus(_A)
if mibBuilder.loadTexts:bandCtpRxExpectedPowerNominal.setUnits('0.1 dBm')
class _BandCtpSpanLoss1LowThreshold_Type(FloatTenths):defaultValue=15
_BandCtpSpanLoss1LowThreshold_Type.__name__=_E
_BandCtpSpanLoss1LowThreshold_Object=MibTableColumn
bandCtpSpanLoss1LowThreshold=_BandCtpSpanLoss1LowThreshold_Object((1,3,6,1,4,1,21296,2,2,2,2,2,1,1,4),_BandCtpSpanLoss1LowThreshold_Type())
bandCtpSpanLoss1LowThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpSpanLoss1LowThreshold.setStatus(_A)
class _BandCtpSpanLoss1HighThreshold_Type(FloatTenths):defaultValue=15
_BandCtpSpanLoss1HighThreshold_Type.__name__=_E
_BandCtpSpanLoss1HighThreshold_Object=MibTableColumn
bandCtpSpanLoss1HighThreshold=_BandCtpSpanLoss1HighThreshold_Object((1,3,6,1,4,1,21296,2,2,2,2,2,1,1,5),_BandCtpSpanLoss1HighThreshold_Type())
bandCtpSpanLoss1HighThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpSpanLoss1HighThreshold.setStatus(_A)
class _BandCtpSpanLoss1ThldReporting_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_BandCtpSpanLoss1ThldReporting_Type.__name__=_D
_BandCtpSpanLoss1ThldReporting_Object=MibTableColumn
bandCtpSpanLoss1ThldReporting=_BandCtpSpanLoss1ThldReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,2,1,1,6),_BandCtpSpanLoss1ThldReporting_Type())
bandCtpSpanLoss1ThldReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpSpanLoss1ThldReporting.setStatus(_A)
class _BandCtpExpectedSpanLoss_Type(FloatTenths):defaultValue=25;subtypeSpec=FloatTenths.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,400))
_BandCtpExpectedSpanLoss_Type.__name__=_E
_BandCtpExpectedSpanLoss_Object=MibTableColumn
bandCtpExpectedSpanLoss=_BandCtpExpectedSpanLoss_Object((1,3,6,1,4,1,21296,2,2,2,2,2,1,1,7),_BandCtpExpectedSpanLoss_Type())
bandCtpExpectedSpanLoss.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpExpectedSpanLoss.setStatus(_A)
if mibBuilder.loadTexts:bandCtpExpectedSpanLoss.setUnits(_I)
class _BandCtpSpanLossReporting_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_BandCtpSpanLossReporting_Type.__name__=_D
_BandCtpSpanLossReporting_Object=MibTableColumn
bandCtpSpanLossReporting=_BandCtpSpanLossReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,2,1,1,8),_BandCtpSpanLossReporting_Type())
bandCtpSpanLossReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpSpanLossReporting.setStatus(_A)
class _BandCtpMaxEngineeredSpanLoss_Type(FloatTenths):defaultValue=50;subtypeSpec=FloatTenths.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,400))
_BandCtpMaxEngineeredSpanLoss_Type.__name__=_E
_BandCtpMaxEngineeredSpanLoss_Object=MibTableColumn
bandCtpMaxEngineeredSpanLoss=_BandCtpMaxEngineeredSpanLoss_Object((1,3,6,1,4,1,21296,2,2,2,2,2,1,1,9),_BandCtpMaxEngineeredSpanLoss_Type())
bandCtpMaxEngineeredSpanLoss.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpMaxEngineeredSpanLoss.setStatus(_A)
if mibBuilder.loadTexts:bandCtpMaxEngineeredSpanLoss.setUnits(_I)
class _BandCtpALSAction_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_BandCtpALSAction_Type.__name__=_D
_BandCtpALSAction_Object=MibTableColumn
bandCtpALSAction=_BandCtpALSAction_Object((1,3,6,1,4,1,21296,2,2,2,2,2,1,1,10),_BandCtpALSAction_Type())
bandCtpALSAction.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpALSAction.setStatus(_A)
class _BandCtpALSDisableTime_Type(Integer32):defaultValue=15
_BandCtpALSDisableTime_Type.__name__=_D
_BandCtpALSDisableTime_Object=MibTableColumn
bandCtpALSDisableTime=_BandCtpALSDisableTime_Object((1,3,6,1,4,1,21296,2,2,2,2,2,1,1,11),_BandCtpALSDisableTime_Type())
bandCtpALSDisableTime.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpALSDisableTime.setStatus(_A)
class _BandCtpPmHistStatsEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_BandCtpPmHistStatsEnable_Type.__name__=_D
_BandCtpPmHistStatsEnable_Object=MibTableColumn
bandCtpPmHistStatsEnable=_BandCtpPmHistStatsEnable_Object((1,3,6,1,4,1,21296,2,2,2,2,2,1,1,12),_BandCtpPmHistStatsEnable_Type())
bandCtpPmHistStatsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpPmHistStatsEnable.setStatus(_A)
class _BandCtpOprLowThreshold_Type(FloatTenths):defaultValue=0
_BandCtpOprLowThreshold_Type.__name__=_E
_BandCtpOprLowThreshold_Object=MibTableColumn
bandCtpOprLowThreshold=_BandCtpOprLowThreshold_Object((1,3,6,1,4,1,21296,2,2,2,2,2,1,1,13),_BandCtpOprLowThreshold_Type())
bandCtpOprLowThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpOprLowThreshold.setStatus(_A)
if mibBuilder.loadTexts:bandCtpOprLowThreshold.setUnits(_I)
class _BandCtpOprHighThreshold_Type(FloatTenths):defaultValue=0
_BandCtpOprHighThreshold_Type.__name__=_E
_BandCtpOprHighThreshold_Object=MibTableColumn
bandCtpOprHighThreshold=_BandCtpOprHighThreshold_Object((1,3,6,1,4,1,21296,2,2,2,2,2,1,1,14),_BandCtpOprHighThreshold_Type())
bandCtpOprHighThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpOprHighThreshold.setStatus(_A)
if mibBuilder.loadTexts:bandCtpOprHighThreshold.setUnits(_I)
class _BandCtpCBandOlosSoakTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('fast',1),('medium',2),('long',3)))
_BandCtpCBandOlosSoakTime_Type.__name__=_D
_BandCtpCBandOlosSoakTime_Object=MibTableColumn
bandCtpCBandOlosSoakTime=_BandCtpCBandOlosSoakTime_Object((1,3,6,1,4,1,21296,2,2,2,2,2,1,1,15),_BandCtpCBandOlosSoakTime_Type())
bandCtpCBandOlosSoakTime.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpCBandOlosSoakTime.setStatus(_A)
_BandCtpSpanLoss2LowThreshold_Type=FloatTenths
_BandCtpSpanLoss2LowThreshold_Object=MibTableColumn
bandCtpSpanLoss2LowThreshold=_BandCtpSpanLoss2LowThreshold_Object((1,3,6,1,4,1,21296,2,2,2,2,2,1,1,16),_BandCtpSpanLoss2LowThreshold_Type())
bandCtpSpanLoss2LowThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpSpanLoss2LowThreshold.setStatus(_A)
_BandCtpSpanLoss2HighThreshold_Type=FloatTenths
_BandCtpSpanLoss2HighThreshold_Object=MibTableColumn
bandCtpSpanLoss2HighThreshold=_BandCtpSpanLoss2HighThreshold_Object((1,3,6,1,4,1,21296,2,2,2,2,2,1,1,17),_BandCtpSpanLoss2HighThreshold_Type())
bandCtpSpanLoss2HighThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpSpanLoss2HighThreshold.setStatus(_A)
_BandCtpSpanLoss2ThldReporting_Type=InfnReporting
_BandCtpSpanLoss2ThldReporting_Object=MibTableColumn
bandCtpSpanLoss2ThldReporting=_BandCtpSpanLoss2ThldReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,2,1,1,18),_BandCtpSpanLoss2ThldReporting_Type())
bandCtpSpanLoss2ThldReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpSpanLoss2ThldReporting.setStatus(_A)
_BandCtpCustomMargin_Type=FloatTenths
_BandCtpCustomMargin_Object=MibTableColumn
bandCtpCustomMargin=_BandCtpCustomMargin_Object((1,3,6,1,4,1,21296,2,2,2,2,2,1,1,19),_BandCtpCustomMargin_Type())
bandCtpCustomMargin.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpCustomMargin.setStatus(_A)
_BandCtpALSDisableMode_Type=InfnALSDisableMode
_BandCtpALSDisableMode_Object=MibTableColumn
bandCtpALSDisableMode=_BandCtpALSDisableMode_Object((1,3,6,1,4,1,21296,2,2,2,2,2,1,1,20),_BandCtpALSDisableMode_Type())
bandCtpALSDisableMode.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpALSDisableMode.setStatus(_A)
_BandCtpSlotOperatingMode_Type=InfnSlotOperatingMode
_BandCtpSlotOperatingMode_Object=MibTableColumn
bandCtpSlotOperatingMode=_BandCtpSlotOperatingMode_Object((1,3,6,1,4,1,21296,2,2,2,2,2,1,1,21),_BandCtpSlotOperatingMode_Type())
bandCtpSlotOperatingMode.setMaxAccess(_F)
if mibBuilder.loadTexts:bandCtpSlotOperatingMode.setStatus(_A)
_BandCtpTeInterfaceList_Type=DisplayString
_BandCtpTeInterfaceList_Object=MibTableColumn
bandCtpTeInterfaceList=_BandCtpTeInterfaceList_Object((1,3,6,1,4,1,21296,2,2,2,2,2,1,1,22),_BandCtpTeInterfaceList_Type())
bandCtpTeInterfaceList.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpTeInterfaceList.setStatus(_A)
_BandCtpRxEDFAGainMode_Type=InfnRxEDFAGainMode
_BandCtpRxEDFAGainMode_Object=MibTableColumn
bandCtpRxEDFAGainMode=_BandCtpRxEDFAGainMode_Object((1,3,6,1,4,1,21296,2,2,2,2,2,1,1,23),_BandCtpRxEDFAGainMode_Type())
bandCtpRxEDFAGainMode.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpRxEDFAGainMode.setStatus(_A)
_BandCtpRxEDFAGainModeValue_Type=InfnRxEDFAGainMode
_BandCtpRxEDFAGainModeValue_Object=MibTableColumn
bandCtpRxEDFAGainModeValue=_BandCtpRxEDFAGainModeValue_Object((1,3,6,1,4,1,21296,2,2,2,2,2,1,1,24),_BandCtpRxEDFAGainModeValue_Type())
bandCtpRxEDFAGainModeValue.setMaxAccess(_F)
if mibBuilder.loadTexts:bandCtpRxEDFAGainModeValue.setStatus(_A)
_BandCtpRxEDFAGain_Type=FloatArbitraryPrecision
_BandCtpRxEDFAGain_Object=MibTableColumn
bandCtpRxEDFAGain=_BandCtpRxEDFAGain_Object((1,3,6,1,4,1,21296,2,2,2,2,2,1,1,25),_BandCtpRxEDFAGain_Type())
bandCtpRxEDFAGain.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpRxEDFAGain.setStatus(_A)
_BandCtpRxEDFATilt_Type=FloatTenths
_BandCtpRxEDFATilt_Object=MibTableColumn
bandCtpRxEDFATilt=_BandCtpRxEDFATilt_Object((1,3,6,1,4,1,21296,2,2,2,2,2,1,1,26),_BandCtpRxEDFATilt_Type())
bandCtpRxEDFATilt.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpRxEDFATilt.setStatus(_A)
_BandCtpTxEDFAInputPowerOffset_Type=FloatTenths
_BandCtpTxEDFAInputPowerOffset_Object=MibTableColumn
bandCtpTxEDFAInputPowerOffset=_BandCtpTxEDFAInputPowerOffset_Object((1,3,6,1,4,1,21296,2,2,2,2,2,1,1,27),_BandCtpTxEDFAInputPowerOffset_Type())
bandCtpTxEDFAInputPowerOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpTxEDFAInputPowerOffset.setStatus(_A)
_BandCtpMuxFreqSlotAttenProfile_Type=DisplayString
_BandCtpMuxFreqSlotAttenProfile_Object=MibTableColumn
bandCtpMuxFreqSlotAttenProfile=_BandCtpMuxFreqSlotAttenProfile_Object((1,3,6,1,4,1,21296,2,2,2,2,2,1,1,28),_BandCtpMuxFreqSlotAttenProfile_Type())
bandCtpMuxFreqSlotAttenProfile.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpMuxFreqSlotAttenProfile.setStatus(_A)
_BandCtpDemuxFreqSlotAttenProfile_Type=DisplayString
_BandCtpDemuxFreqSlotAttenProfile_Object=MibTableColumn
bandCtpDemuxFreqSlotAttenProfile=_BandCtpDemuxFreqSlotAttenProfile_Object((1,3,6,1,4,1,21296,2,2,2,2,2,1,1,29),_BandCtpDemuxFreqSlotAttenProfile_Type())
bandCtpDemuxFreqSlotAttenProfile.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpDemuxFreqSlotAttenProfile.setStatus(_A)
_BandCtpTxVOA_Type=FloatTenths
_BandCtpTxVOA_Object=MibTableColumn
bandCtpTxVOA=_BandCtpTxVOA_Object((1,3,6,1,4,1,21296,2,2,2,2,2,1,1,30),_BandCtpTxVOA_Type())
bandCtpTxVOA.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpTxVOA.setStatus(_A)
_BandCtpTargetLineOutputPower_Type=FloatTenths
_BandCtpTargetLineOutputPower_Object=MibTableColumn
bandCtpTargetLineOutputPower=_BandCtpTargetLineOutputPower_Object((1,3,6,1,4,1,21296,2,2,2,2,2,1,1,31),_BandCtpTargetLineOutputPower_Type())
bandCtpTargetLineOutputPower.setMaxAccess(_C)
if mibBuilder.loadTexts:bandCtpTargetLineOutputPower.setStatus(_A)
_BandCtpConformance_ObjectIdentity=ObjectIdentity
bandCtpConformance=_BandCtpConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,2,3))
_BandCtpCompliances_ObjectIdentity=ObjectIdentity
bandCtpCompliances=_BandCtpCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,2,3,1))
_BandCtpGroups_ObjectIdentity=ObjectIdentity
bandCtpGroups=_BandCtpGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,2,3,2))
bandCtpGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,2,3,2,1))
bandCtpGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p)))
if mibBuilder.loadTexts:bandCtpGroup.setStatus(_A)
bandCtpCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,2,3,1,1))
bandCtpCompliance.setObjects((_B,_q))
if mibBuilder.loadTexts:bandCtpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'bandCtpMIB':bandCtpMIB,'bandCtpTable':bandCtpTable,'bandCtpEntry':bandCtpEntry,_L:bandCtpMaxOCGs,_M:bandCtpChannelPlan,_N:bandCtpRxExpectedPowerNominal,_O:bandCtpSpanLoss1LowThreshold,_P:bandCtpSpanLoss1HighThreshold,_Q:bandCtpSpanLoss1ThldReporting,_R:bandCtpExpectedSpanLoss,_S:bandCtpSpanLossReporting,_T:bandCtpMaxEngineeredSpanLoss,_U:bandCtpALSAction,_V:bandCtpALSDisableTime,_W:bandCtpPmHistStatsEnable,_X:bandCtpOprLowThreshold,_Y:bandCtpOprHighThreshold,_Z:bandCtpCBandOlosSoakTime,_a:bandCtpSpanLoss2LowThreshold,_b:bandCtpSpanLoss2HighThreshold,_c:bandCtpSpanLoss2ThldReporting,_d:bandCtpCustomMargin,_e:bandCtpALSDisableMode,_f:bandCtpSlotOperatingMode,_g:bandCtpTeInterfaceList,_h:bandCtpRxEDFAGainMode,_i:bandCtpRxEDFAGainModeValue,_j:bandCtpRxEDFAGain,_k:bandCtpRxEDFATilt,_l:bandCtpTxEDFAInputPowerOffset,_m:bandCtpMuxFreqSlotAttenProfile,_n:bandCtpDemuxFreqSlotAttenProfile,_o:bandCtpTxVOA,_p:bandCtpTargetLineOutputPower,'bandCtpConformance':bandCtpConformance,'bandCtpCompliances':bandCtpCompliances,'bandCtpCompliance':bandCtpCompliance,'bandCtpGroups':bandCtpGroups,_q:bandCtpGroup})