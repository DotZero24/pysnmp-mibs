_T='idlerPtpGroup'
_S='idlerPtpOLOSThreshold'
_R='idlerPtpAutoDiscovery'
_Q='idlerPtpShutterState'
_P='idlerPtpTargetPower'
_O='idlerPtpPowerControlLoop'
_N='idlerPtpOprOorHighThreshold'
_M='idlerPtpOprOorLowThreshold'
_L='idlerPtpOptOorHighThreshold'
_K='idlerPtpOptOorLowThreshold'
_J='idlerPtpRxAssociatedOtsEqptType'
_I='idlerPtpTxAssociatedOtsEqptType'
_H='idlerPtpPmHistStatsEnable'
_G='idlerPtpMoId'
_F='read-only'
_E='ifIndex'
_D='IF-MIB'
_C='read-write'
_B='INFINERA-TP-IDLERPTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_D,_E)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
FloatArbitraryPrecision,InfnEnableDisableType,InfnEqptType,InfnPmHistStatsControl,InfnShutterState=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatArbitraryPrecision','InfnEnableDisableType','InfnEqptType','InfnPmHistStatsControl','InfnShutterState')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
idlerPtpMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,84))
if mibBuilder.loadTexts:idlerPtpMIB.setRevisions(('2017-05-08 00:00',))
_IdlerPtpTable_Object=MibTable
idlerPtpTable=_IdlerPtpTable_Object((1,3,6,1,4,1,21296,2,2,2,2,84,1))
if mibBuilder.loadTexts:idlerPtpTable.setStatus(_A)
_IdlerPtpEntry_Object=MibTableRow
idlerPtpEntry=_IdlerPtpEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,84,1,1))
idlerPtpEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:idlerPtpEntry.setStatus(_A)
_IdlerPtpMoId_Type=DisplayString
_IdlerPtpMoId_Object=MibTableColumn
idlerPtpMoId=_IdlerPtpMoId_Object((1,3,6,1,4,1,21296,2,2,2,2,84,1,1,1),_IdlerPtpMoId_Type())
idlerPtpMoId.setMaxAccess(_C)
if mibBuilder.loadTexts:idlerPtpMoId.setStatus(_A)
_IdlerPtpPmHistStatsEnable_Type=InfnPmHistStatsControl
_IdlerPtpPmHistStatsEnable_Object=MibTableColumn
idlerPtpPmHistStatsEnable=_IdlerPtpPmHistStatsEnable_Object((1,3,6,1,4,1,21296,2,2,2,2,84,1,1,2),_IdlerPtpPmHistStatsEnable_Type())
idlerPtpPmHistStatsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:idlerPtpPmHistStatsEnable.setStatus(_A)
_IdlerPtpTxAssociatedOtsEqptType_Type=InfnEqptType
_IdlerPtpTxAssociatedOtsEqptType_Object=MibTableColumn
idlerPtpTxAssociatedOtsEqptType=_IdlerPtpTxAssociatedOtsEqptType_Object((1,3,6,1,4,1,21296,2,2,2,2,84,1,1,3),_IdlerPtpTxAssociatedOtsEqptType_Type())
idlerPtpTxAssociatedOtsEqptType.setMaxAccess(_F)
if mibBuilder.loadTexts:idlerPtpTxAssociatedOtsEqptType.setStatus(_A)
_IdlerPtpRxAssociatedOtsEqptType_Type=InfnEqptType
_IdlerPtpRxAssociatedOtsEqptType_Object=MibTableColumn
idlerPtpRxAssociatedOtsEqptType=_IdlerPtpRxAssociatedOtsEqptType_Object((1,3,6,1,4,1,21296,2,2,2,2,84,1,1,4),_IdlerPtpRxAssociatedOtsEqptType_Type())
idlerPtpRxAssociatedOtsEqptType.setMaxAccess(_F)
if mibBuilder.loadTexts:idlerPtpRxAssociatedOtsEqptType.setStatus(_A)
_IdlerPtpOptOorLowThreshold_Type=FloatArbitraryPrecision
_IdlerPtpOptOorLowThreshold_Object=MibTableColumn
idlerPtpOptOorLowThreshold=_IdlerPtpOptOorLowThreshold_Object((1,3,6,1,4,1,21296,2,2,2,2,84,1,1,5),_IdlerPtpOptOorLowThreshold_Type())
idlerPtpOptOorLowThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:idlerPtpOptOorLowThreshold.setStatus(_A)
_IdlerPtpOptOorHighThreshold_Type=FloatArbitraryPrecision
_IdlerPtpOptOorHighThreshold_Object=MibTableColumn
idlerPtpOptOorHighThreshold=_IdlerPtpOptOorHighThreshold_Object((1,3,6,1,4,1,21296,2,2,2,2,84,1,1,6),_IdlerPtpOptOorHighThreshold_Type())
idlerPtpOptOorHighThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:idlerPtpOptOorHighThreshold.setStatus(_A)
_IdlerPtpOprOorLowThreshold_Type=FloatArbitraryPrecision
_IdlerPtpOprOorLowThreshold_Object=MibTableColumn
idlerPtpOprOorLowThreshold=_IdlerPtpOprOorLowThreshold_Object((1,3,6,1,4,1,21296,2,2,2,2,84,1,1,7),_IdlerPtpOprOorLowThreshold_Type())
idlerPtpOprOorLowThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:idlerPtpOprOorLowThreshold.setStatus(_A)
_IdlerPtpOprOorHighThreshold_Type=FloatArbitraryPrecision
_IdlerPtpOprOorHighThreshold_Object=MibTableColumn
idlerPtpOprOorHighThreshold=_IdlerPtpOprOorHighThreshold_Object((1,3,6,1,4,1,21296,2,2,2,2,84,1,1,8),_IdlerPtpOprOorHighThreshold_Type())
idlerPtpOprOorHighThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:idlerPtpOprOorHighThreshold.setStatus(_A)
_IdlerPtpPowerControlLoop_Type=InfnEnableDisableType
_IdlerPtpPowerControlLoop_Object=MibTableColumn
idlerPtpPowerControlLoop=_IdlerPtpPowerControlLoop_Object((1,3,6,1,4,1,21296,2,2,2,2,84,1,1,9),_IdlerPtpPowerControlLoop_Type())
idlerPtpPowerControlLoop.setMaxAccess(_C)
if mibBuilder.loadTexts:idlerPtpPowerControlLoop.setStatus(_A)
_IdlerPtpTargetPower_Type=FloatArbitraryPrecision
_IdlerPtpTargetPower_Object=MibTableColumn
idlerPtpTargetPower=_IdlerPtpTargetPower_Object((1,3,6,1,4,1,21296,2,2,2,2,84,1,1,10),_IdlerPtpTargetPower_Type())
idlerPtpTargetPower.setMaxAccess(_C)
if mibBuilder.loadTexts:idlerPtpTargetPower.setStatus(_A)
_IdlerPtpShutterState_Type=InfnShutterState
_IdlerPtpShutterState_Object=MibTableColumn
idlerPtpShutterState=_IdlerPtpShutterState_Object((1,3,6,1,4,1,21296,2,2,2,2,84,1,1,11),_IdlerPtpShutterState_Type())
idlerPtpShutterState.setMaxAccess(_C)
if mibBuilder.loadTexts:idlerPtpShutterState.setStatus(_A)
_IdlerPtpAutoDiscovery_Type=InfnEnableDisableType
_IdlerPtpAutoDiscovery_Object=MibTableColumn
idlerPtpAutoDiscovery=_IdlerPtpAutoDiscovery_Object((1,3,6,1,4,1,21296,2,2,2,2,84,1,1,12),_IdlerPtpAutoDiscovery_Type())
idlerPtpAutoDiscovery.setMaxAccess(_C)
if mibBuilder.loadTexts:idlerPtpAutoDiscovery.setStatus(_A)
_IdlerPtpOLOSThreshold_Type=FloatArbitraryPrecision
_IdlerPtpOLOSThreshold_Object=MibTableColumn
idlerPtpOLOSThreshold=_IdlerPtpOLOSThreshold_Object((1,3,6,1,4,1,21296,2,2,2,2,84,1,1,13),_IdlerPtpOLOSThreshold_Type())
idlerPtpOLOSThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:idlerPtpOLOSThreshold.setStatus(_A)
_IdlerPtpConformance_ObjectIdentity=ObjectIdentity
idlerPtpConformance=_IdlerPtpConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,84,3))
_IdlerPtpCompliances_ObjectIdentity=ObjectIdentity
idlerPtpCompliances=_IdlerPtpCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,84,3,1))
_IdlerPtpGroups_ObjectIdentity=ObjectIdentity
idlerPtpGroups=_IdlerPtpGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,84,3,2))
idlerPtpGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,84,3,2,1))
idlerPtpGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:idlerPtpGroup.setStatus(_A)
idlerPtpCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,84,3,1,1))
idlerPtpCompliance.setObjects((_B,_T))
if mibBuilder.loadTexts:idlerPtpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'idlerPtpMIB':idlerPtpMIB,'idlerPtpTable':idlerPtpTable,'idlerPtpEntry':idlerPtpEntry,_G:idlerPtpMoId,_H:idlerPtpPmHistStatsEnable,_I:idlerPtpTxAssociatedOtsEqptType,_J:idlerPtpRxAssociatedOtsEqptType,_K:idlerPtpOptOorLowThreshold,_L:idlerPtpOptOorHighThreshold,_M:idlerPtpOprOorLowThreshold,_N:idlerPtpOprOorHighThreshold,_O:idlerPtpPowerControlLoop,_P:idlerPtpTargetPower,_Q:idlerPtpShutterState,_R:idlerPtpAutoDiscovery,_S:idlerPtpOLOSThreshold,'idlerPtpConformance':idlerPtpConformance,'idlerPtpCompliances':idlerPtpCompliances,'idlerPtpCompliance':idlerPtpCompliance,'idlerPtpGroups':idlerPtpGroups,_T:idlerPtpGroup})