_X='opsmPtpGroup'
_W='opsmPtpRxPowerLevelHighThldReporting'
_V='opsmPtpRxPowerLevelHighThreshold'
_U='opsmPtpRxPowerLevelLowThldReporting'
_T='opsmPtpRxPowerLevelLowThreshold'
_S='opsmPtpOlosClearHysteresis'
_R='opsmPtpOlosSoakTimer'
_Q='opsmPtpOlosThreshold'
_P='opsmPtpSpanDistance'
_O='opsmPtpRxAssociatedEqptType'
_N='opsmPtpTxAssociatedPtpType'
_M='opsmPtpTxAssociatedPtp'
_L='opsmPtpTxAssociatedEqptType'
_K='opsmPtpRxAssociatedPtpType'
_J='opsmPtpRxAssociatedPtp'
_I='opsmPtpPmHistStatsEnable'
_H='opsmPtpExpectedSpanLossRange'
_G='opsmPtpProvisionedNeighborTP'
_F='ifIndex'
_E='IF-MIB'
_D='read-only'
_C='read-write'
_B='INFINERA-TP-OPSMPTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_E,_F)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
FloatTenths,InfnAdTpType,InfnEnableDisable,InfnEqptType,InfnPmHistStatsControl,InfnReporting,InfnSpanLossRange=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatTenths','InfnAdTpType','InfnEnableDisable','InfnEqptType','InfnPmHistStatsControl','InfnReporting','InfnSpanLossRange')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
opsmPtpMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,61))
if mibBuilder.loadTexts:opsmPtpMIB.setRevisions(('2015-04-20 00:00',))
_OpsmPtpTable_Object=MibTable
opsmPtpTable=_OpsmPtpTable_Object((1,3,6,1,4,1,21296,2,2,2,2,61,1))
if mibBuilder.loadTexts:opsmPtpTable.setStatus(_A)
_OpsmPtpEntry_Object=MibTableRow
opsmPtpEntry=_OpsmPtpEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,61,1,1))
opsmPtpEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:opsmPtpEntry.setStatus(_A)
_OpsmPtpProvisionedNeighborTP_Type=DisplayString
_OpsmPtpProvisionedNeighborTP_Object=MibTableColumn
opsmPtpProvisionedNeighborTP=_OpsmPtpProvisionedNeighborTP_Object((1,3,6,1,4,1,21296,2,2,2,2,61,1,1,1),_OpsmPtpProvisionedNeighborTP_Type())
opsmPtpProvisionedNeighborTP.setMaxAccess(_C)
if mibBuilder.loadTexts:opsmPtpProvisionedNeighborTP.setStatus(_A)
_OpsmPtpExpectedSpanLossRange_Type=InfnSpanLossRange
_OpsmPtpExpectedSpanLossRange_Object=MibTableColumn
opsmPtpExpectedSpanLossRange=_OpsmPtpExpectedSpanLossRange_Object((1,3,6,1,4,1,21296,2,2,2,2,61,1,1,2),_OpsmPtpExpectedSpanLossRange_Type())
opsmPtpExpectedSpanLossRange.setMaxAccess(_C)
if mibBuilder.loadTexts:opsmPtpExpectedSpanLossRange.setStatus(_A)
_OpsmPtpPmHistStatsEnable_Type=InfnPmHistStatsControl
_OpsmPtpPmHistStatsEnable_Object=MibTableColumn
opsmPtpPmHistStatsEnable=_OpsmPtpPmHistStatsEnable_Object((1,3,6,1,4,1,21296,2,2,2,2,61,1,1,3),_OpsmPtpPmHistStatsEnable_Type())
opsmPtpPmHistStatsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:opsmPtpPmHistStatsEnable.setStatus(_A)
_OpsmPtpRxAssociatedPtp_Type=DisplayString
_OpsmPtpRxAssociatedPtp_Object=MibTableColumn
opsmPtpRxAssociatedPtp=_OpsmPtpRxAssociatedPtp_Object((1,3,6,1,4,1,21296,2,2,2,2,61,1,1,4),_OpsmPtpRxAssociatedPtp_Type())
opsmPtpRxAssociatedPtp.setMaxAccess(_C)
if mibBuilder.loadTexts:opsmPtpRxAssociatedPtp.setStatus(_A)
_OpsmPtpRxAssociatedPtpType_Type=InfnAdTpType
_OpsmPtpRxAssociatedPtpType_Object=MibTableColumn
opsmPtpRxAssociatedPtpType=_OpsmPtpRxAssociatedPtpType_Object((1,3,6,1,4,1,21296,2,2,2,2,61,1,1,5),_OpsmPtpRxAssociatedPtpType_Type())
opsmPtpRxAssociatedPtpType.setMaxAccess(_D)
if mibBuilder.loadTexts:opsmPtpRxAssociatedPtpType.setStatus(_A)
_OpsmPtpTxAssociatedEqptType_Type=InfnEqptType
_OpsmPtpTxAssociatedEqptType_Object=MibTableColumn
opsmPtpTxAssociatedEqptType=_OpsmPtpTxAssociatedEqptType_Object((1,3,6,1,4,1,21296,2,2,2,2,61,1,1,6),_OpsmPtpTxAssociatedEqptType_Type())
opsmPtpTxAssociatedEqptType.setMaxAccess(_D)
if mibBuilder.loadTexts:opsmPtpTxAssociatedEqptType.setStatus(_A)
_OpsmPtpTxAssociatedPtp_Type=DisplayString
_OpsmPtpTxAssociatedPtp_Object=MibTableColumn
opsmPtpTxAssociatedPtp=_OpsmPtpTxAssociatedPtp_Object((1,3,6,1,4,1,21296,2,2,2,2,61,1,1,7),_OpsmPtpTxAssociatedPtp_Type())
opsmPtpTxAssociatedPtp.setMaxAccess(_C)
if mibBuilder.loadTexts:opsmPtpTxAssociatedPtp.setStatus(_A)
_OpsmPtpTxAssociatedPtpType_Type=InfnAdTpType
_OpsmPtpTxAssociatedPtpType_Object=MibTableColumn
opsmPtpTxAssociatedPtpType=_OpsmPtpTxAssociatedPtpType_Object((1,3,6,1,4,1,21296,2,2,2,2,61,1,1,8),_OpsmPtpTxAssociatedPtpType_Type())
opsmPtpTxAssociatedPtpType.setMaxAccess(_C)
if mibBuilder.loadTexts:opsmPtpTxAssociatedPtpType.setStatus(_A)
_OpsmPtpRxAssociatedEqptType_Type=InfnEqptType
_OpsmPtpRxAssociatedEqptType_Object=MibTableColumn
opsmPtpRxAssociatedEqptType=_OpsmPtpRxAssociatedEqptType_Object((1,3,6,1,4,1,21296,2,2,2,2,61,1,1,9),_OpsmPtpRxAssociatedEqptType_Type())
opsmPtpRxAssociatedEqptType.setMaxAccess(_D)
if mibBuilder.loadTexts:opsmPtpRxAssociatedEqptType.setStatus(_A)
_OpsmPtpSpanDistance_Type=FloatTenths
_OpsmPtpSpanDistance_Object=MibTableColumn
opsmPtpSpanDistance=_OpsmPtpSpanDistance_Object((1,3,6,1,4,1,21296,2,2,2,2,61,1,1,10),_OpsmPtpSpanDistance_Type())
opsmPtpSpanDistance.setMaxAccess(_C)
if mibBuilder.loadTexts:opsmPtpSpanDistance.setStatus(_A)
_OpsmPtpOlosThreshold_Type=FloatTenths
_OpsmPtpOlosThreshold_Object=MibTableColumn
opsmPtpOlosThreshold=_OpsmPtpOlosThreshold_Object((1,3,6,1,4,1,21296,2,2,2,2,61,1,1,11),_OpsmPtpOlosThreshold_Type())
opsmPtpOlosThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:opsmPtpOlosThreshold.setStatus(_A)
_OpsmPtpOlosSoakTimer_Type=Integer32
_OpsmPtpOlosSoakTimer_Object=MibTableColumn
opsmPtpOlosSoakTimer=_OpsmPtpOlosSoakTimer_Object((1,3,6,1,4,1,21296,2,2,2,2,61,1,1,12),_OpsmPtpOlosSoakTimer_Type())
opsmPtpOlosSoakTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:opsmPtpOlosSoakTimer.setStatus(_A)
_OpsmPtpOlosClearHysteresis_Type=FloatTenths
_OpsmPtpOlosClearHysteresis_Object=MibTableColumn
opsmPtpOlosClearHysteresis=_OpsmPtpOlosClearHysteresis_Object((1,3,6,1,4,1,21296,2,2,2,2,61,1,1,13),_OpsmPtpOlosClearHysteresis_Type())
opsmPtpOlosClearHysteresis.setMaxAccess(_C)
if mibBuilder.loadTexts:opsmPtpOlosClearHysteresis.setStatus(_A)
_OpsmPtpRxPowerLevelLowThreshold_Type=FloatTenths
_OpsmPtpRxPowerLevelLowThreshold_Object=MibTableColumn
opsmPtpRxPowerLevelLowThreshold=_OpsmPtpRxPowerLevelLowThreshold_Object((1,3,6,1,4,1,21296,2,2,2,2,61,1,1,14),_OpsmPtpRxPowerLevelLowThreshold_Type())
opsmPtpRxPowerLevelLowThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:opsmPtpRxPowerLevelLowThreshold.setStatus(_A)
_OpsmPtpRxPowerLevelLowThldReporting_Type=InfnReporting
_OpsmPtpRxPowerLevelLowThldReporting_Object=MibTableColumn
opsmPtpRxPowerLevelLowThldReporting=_OpsmPtpRxPowerLevelLowThldReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,61,1,1,15),_OpsmPtpRxPowerLevelLowThldReporting_Type())
opsmPtpRxPowerLevelLowThldReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:opsmPtpRxPowerLevelLowThldReporting.setStatus(_A)
_OpsmPtpRxPowerLevelHighThreshold_Type=FloatTenths
_OpsmPtpRxPowerLevelHighThreshold_Object=MibTableColumn
opsmPtpRxPowerLevelHighThreshold=_OpsmPtpRxPowerLevelHighThreshold_Object((1,3,6,1,4,1,21296,2,2,2,2,61,1,1,16),_OpsmPtpRxPowerLevelHighThreshold_Type())
opsmPtpRxPowerLevelHighThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:opsmPtpRxPowerLevelHighThreshold.setStatus(_A)
_OpsmPtpRxPowerLevelHighThldReporting_Type=InfnReporting
_OpsmPtpRxPowerLevelHighThldReporting_Object=MibTableColumn
opsmPtpRxPowerLevelHighThldReporting=_OpsmPtpRxPowerLevelHighThldReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,61,1,1,17),_OpsmPtpRxPowerLevelHighThldReporting_Type())
opsmPtpRxPowerLevelHighThldReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:opsmPtpRxPowerLevelHighThldReporting.setStatus(_A)
_OpsmPtpConformance_ObjectIdentity=ObjectIdentity
opsmPtpConformance=_OpsmPtpConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,61,3))
_OpsmPtpCompliances_ObjectIdentity=ObjectIdentity
opsmPtpCompliances=_OpsmPtpCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,61,3,1))
_OpsmPtpGroups_ObjectIdentity=ObjectIdentity
opsmPtpGroups=_OpsmPtpGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,61,3,2))
opsmPtpGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,61,3,2,1))
opsmPtpGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:opsmPtpGroup.setStatus(_A)
opsmPtpCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,61,3,1,1))
opsmPtpCompliance.setObjects((_B,_X))
if mibBuilder.loadTexts:opsmPtpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'opsmPtpMIB':opsmPtpMIB,'opsmPtpTable':opsmPtpTable,'opsmPtpEntry':opsmPtpEntry,_G:opsmPtpProvisionedNeighborTP,_H:opsmPtpExpectedSpanLossRange,_I:opsmPtpPmHistStatsEnable,_J:opsmPtpRxAssociatedPtp,_K:opsmPtpRxAssociatedPtpType,_L:opsmPtpTxAssociatedEqptType,_M:opsmPtpTxAssociatedPtp,_N:opsmPtpTxAssociatedPtpType,_O:opsmPtpRxAssociatedEqptType,_P:opsmPtpSpanDistance,_Q:opsmPtpOlosThreshold,_R:opsmPtpOlosSoakTimer,_S:opsmPtpOlosClearHysteresis,_T:opsmPtpRxPowerLevelLowThreshold,_U:opsmPtpRxPowerLevelLowThldReporting,_V:opsmPtpRxPowerLevelHighThreshold,_W:opsmPtpRxPowerLevelHighThldReporting,'opsmPtpConformance':opsmPtpConformance,'opsmPtpCompliances':opsmPtpCompliances,'opsmPtpCompliance':opsmPtpCompliance,'opsmPtpGroups':opsmPtpGroups,_X:opsmPtpGroup})