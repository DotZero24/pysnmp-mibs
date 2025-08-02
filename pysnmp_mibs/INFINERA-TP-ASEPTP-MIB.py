_U='asePtpGroup'
_T='asePtpShutterState'
_S='asePtpOLOSThreshold'
_R='asePtpPowerControlLoop'
_Q='asePtpOprOorHighThreshold'
_P='asePtpOprOorLowThreshold'
_O='asePtpOptOorHighThreshold'
_N='asePtpOptOorLowThreshold'
_M='asePtpTargetPower'
_L='asePtpRxProvEqptType'
_K='asePtpTxProvEqptType'
_J='asePtpTxProvNbrTP'
_I='asePtpRxProvNbrTP'
_H='asePtpPmHistStatsEnable'
_G='asePtpMoId'
_F='ifIndex'
_E='IF-MIB'
_D='read-only'
_C='read-write'
_B='INFINERA-TP-ASEPTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_E,_F)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
FloatArbitraryPrecision,InfnEnableDisableType,InfnEqptType,InfnPmHistStatsControl,InfnShutterState=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatArbitraryPrecision','InfnEnableDisableType','InfnEqptType','InfnPmHistStatsControl','InfnShutterState')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
asePtpMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,83))
if mibBuilder.loadTexts:asePtpMIB.setRevisions(('2017-05-08 00:00',))
_AsePtpTable_Object=MibTable
asePtpTable=_AsePtpTable_Object((1,3,6,1,4,1,21296,2,2,2,2,83,1))
if mibBuilder.loadTexts:asePtpTable.setStatus(_A)
_AsePtpEntry_Object=MibTableRow
asePtpEntry=_AsePtpEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,83,1,1))
asePtpEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:asePtpEntry.setStatus(_A)
_AsePtpMoId_Type=DisplayString
_AsePtpMoId_Object=MibTableColumn
asePtpMoId=_AsePtpMoId_Object((1,3,6,1,4,1,21296,2,2,2,2,83,1,1,1),_AsePtpMoId_Type())
asePtpMoId.setMaxAccess(_C)
if mibBuilder.loadTexts:asePtpMoId.setStatus(_A)
_AsePtpPmHistStatsEnable_Type=InfnPmHistStatsControl
_AsePtpPmHistStatsEnable_Object=MibTableColumn
asePtpPmHistStatsEnable=_AsePtpPmHistStatsEnable_Object((1,3,6,1,4,1,21296,2,2,2,2,83,1,1,2),_AsePtpPmHistStatsEnable_Type())
asePtpPmHistStatsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:asePtpPmHistStatsEnable.setStatus(_A)
_AsePtpRxProvNbrTP_Type=DisplayString
_AsePtpRxProvNbrTP_Object=MibTableColumn
asePtpRxProvNbrTP=_AsePtpRxProvNbrTP_Object((1,3,6,1,4,1,21296,2,2,2,2,83,1,1,3),_AsePtpRxProvNbrTP_Type())
asePtpRxProvNbrTP.setMaxAccess(_C)
if mibBuilder.loadTexts:asePtpRxProvNbrTP.setStatus(_A)
_AsePtpTxProvNbrTP_Type=DisplayString
_AsePtpTxProvNbrTP_Object=MibTableColumn
asePtpTxProvNbrTP=_AsePtpTxProvNbrTP_Object((1,3,6,1,4,1,21296,2,2,2,2,83,1,1,4),_AsePtpTxProvNbrTP_Type())
asePtpTxProvNbrTP.setMaxAccess(_C)
if mibBuilder.loadTexts:asePtpTxProvNbrTP.setStatus(_A)
_AsePtpTxProvEqptType_Type=InfnEqptType
_AsePtpTxProvEqptType_Object=MibTableColumn
asePtpTxProvEqptType=_AsePtpTxProvEqptType_Object((1,3,6,1,4,1,21296,2,2,2,2,83,1,1,5),_AsePtpTxProvEqptType_Type())
asePtpTxProvEqptType.setMaxAccess(_D)
if mibBuilder.loadTexts:asePtpTxProvEqptType.setStatus(_A)
_AsePtpRxProvEqptType_Type=InfnEqptType
_AsePtpRxProvEqptType_Object=MibTableColumn
asePtpRxProvEqptType=_AsePtpRxProvEqptType_Object((1,3,6,1,4,1,21296,2,2,2,2,83,1,1,6),_AsePtpRxProvEqptType_Type())
asePtpRxProvEqptType.setMaxAccess(_D)
if mibBuilder.loadTexts:asePtpRxProvEqptType.setStatus(_A)
_AsePtpTargetPower_Type=FloatArbitraryPrecision
_AsePtpTargetPower_Object=MibTableColumn
asePtpTargetPower=_AsePtpTargetPower_Object((1,3,6,1,4,1,21296,2,2,2,2,83,1,1,7),_AsePtpTargetPower_Type())
asePtpTargetPower.setMaxAccess(_C)
if mibBuilder.loadTexts:asePtpTargetPower.setStatus(_A)
_AsePtpOptOorLowThreshold_Type=FloatArbitraryPrecision
_AsePtpOptOorLowThreshold_Object=MibTableColumn
asePtpOptOorLowThreshold=_AsePtpOptOorLowThreshold_Object((1,3,6,1,4,1,21296,2,2,2,2,83,1,1,8),_AsePtpOptOorLowThreshold_Type())
asePtpOptOorLowThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:asePtpOptOorLowThreshold.setStatus(_A)
_AsePtpOptOorHighThreshold_Type=FloatArbitraryPrecision
_AsePtpOptOorHighThreshold_Object=MibTableColumn
asePtpOptOorHighThreshold=_AsePtpOptOorHighThreshold_Object((1,3,6,1,4,1,21296,2,2,2,2,83,1,1,9),_AsePtpOptOorHighThreshold_Type())
asePtpOptOorHighThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:asePtpOptOorHighThreshold.setStatus(_A)
_AsePtpOprOorLowThreshold_Type=FloatArbitraryPrecision
_AsePtpOprOorLowThreshold_Object=MibTableColumn
asePtpOprOorLowThreshold=_AsePtpOprOorLowThreshold_Object((1,3,6,1,4,1,21296,2,2,2,2,83,1,1,10),_AsePtpOprOorLowThreshold_Type())
asePtpOprOorLowThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:asePtpOprOorLowThreshold.setStatus(_A)
_AsePtpOprOorHighThreshold_Type=FloatArbitraryPrecision
_AsePtpOprOorHighThreshold_Object=MibTableColumn
asePtpOprOorHighThreshold=_AsePtpOprOorHighThreshold_Object((1,3,6,1,4,1,21296,2,2,2,2,83,1,1,11),_AsePtpOprOorHighThreshold_Type())
asePtpOprOorHighThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:asePtpOprOorHighThreshold.setStatus(_A)
_AsePtpPowerControlLoop_Type=InfnEnableDisableType
_AsePtpPowerControlLoop_Object=MibTableColumn
asePtpPowerControlLoop=_AsePtpPowerControlLoop_Object((1,3,6,1,4,1,21296,2,2,2,2,83,1,1,12),_AsePtpPowerControlLoop_Type())
asePtpPowerControlLoop.setMaxAccess(_C)
if mibBuilder.loadTexts:asePtpPowerControlLoop.setStatus(_A)
_AsePtpOLOSThreshold_Type=FloatArbitraryPrecision
_AsePtpOLOSThreshold_Object=MibTableColumn
asePtpOLOSThreshold=_AsePtpOLOSThreshold_Object((1,3,6,1,4,1,21296,2,2,2,2,83,1,1,13),_AsePtpOLOSThreshold_Type())
asePtpOLOSThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:asePtpOLOSThreshold.setStatus(_A)
_AsePtpShutterState_Type=InfnShutterState
_AsePtpShutterState_Object=MibTableColumn
asePtpShutterState=_AsePtpShutterState_Object((1,3,6,1,4,1,21296,2,2,2,2,83,1,1,14),_AsePtpShutterState_Type())
asePtpShutterState.setMaxAccess(_D)
if mibBuilder.loadTexts:asePtpShutterState.setStatus(_A)
_AsePtpConformance_ObjectIdentity=ObjectIdentity
asePtpConformance=_AsePtpConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,83,3))
_AsePtpCompliances_ObjectIdentity=ObjectIdentity
asePtpCompliances=_AsePtpCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,83,3,1))
_AsePtpGroups_ObjectIdentity=ObjectIdentity
asePtpGroups=_AsePtpGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,83,3,2))
asePtpGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,83,3,2,1))
asePtpGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:asePtpGroup.setStatus(_A)
asePtpCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,83,3,1,1))
asePtpCompliance.setObjects((_B,_U))
if mibBuilder.loadTexts:asePtpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'asePtpMIB':asePtpMIB,'asePtpTable':asePtpTable,'asePtpEntry':asePtpEntry,_G:asePtpMoId,_H:asePtpPmHistStatsEnable,_I:asePtpRxProvNbrTP,_J:asePtpTxProvNbrTP,_K:asePtpTxProvEqptType,_L:asePtpRxProvEqptType,_M:asePtpTargetPower,_N:asePtpOptOorLowThreshold,_O:asePtpOptOorHighThreshold,_P:asePtpOprOorLowThreshold,_Q:asePtpOprOorHighThreshold,_R:asePtpPowerControlLoop,_S:asePtpOLOSThreshold,_T:asePtpShutterState,'asePtpConformance':asePtpConformance,'asePtpCompliances':asePtpCompliances,'asePtpCompliance':asePtpCompliance,'asePtpGroups':asePtpGroups,_U:asePtpGroup})