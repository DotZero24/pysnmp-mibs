_u='coCdlFromCdlNetFlowDIChange'
_t='coCdlRxAggDefectIndChange'
_s='coCdlFromCdlNetHCEthernetCRC'
_r='coCdlFromCdlNetEthernetCRCOvrflw'
_q='coCdlFromCdlNetEthernetCRC'
_p='coCdlDINotifyThrottleInterval'
_o='coCdlDefectIndClearSoakInterval'
_n='coCdlDefectIndSetSoakInterval'
_m='coCdlDefectIndNotifyEnable'
_l='coCdlTxAggDefectIndLastChange'
_k='coCdlTxAggDefectIndCurrStatus'
_j='coCdlForceEndOfHop'
_i='deprecated'
_h='coCdlHCRxInvalidFlowID'
_g='coCdlRxInvalidFlowIDOverflow'
_f='coCdlRxInvalidFlowID'
_e='coCdlReceiveMaxFlowIdentifier'
_d='coCdlTransmitMaxFlowIdentifier'
_c='coCdlHCRxNonCdlPackets'
_b='coCdlRxNonCdlPacketsOverflow'
_a='coCdlRxNonCdlPackets'
_Z='coCdlHCRxHeaderCRCError'
_Y='coCdlRxHeaderCRCErrorOverflow'
_X='coCdlRxHeaderCRCError'
_W='coCdlNodeBehavior'
_V='coCdlAdminStatus'
_U='TruthValue'
_T='Integer32'
_S='coCdlDIAggNotifGroup'
_R='coCdlDIAggMandatoryGroup'
_Q='coCdlMIBBaseGroup'
_P='coCdlRxAggDefectIndLastChange'
_O='coCdlRxAggDefectIndCurrStatus'
_N='coCdlToCdlNetFlowDILastChange'
_M='coCdlToCdlNetFlowDICurrStatus'
_L='coCdlToCdlNetFlowIdentifier'
_K='coCdlFromCdlNetFlowIdentifier'
_J='milliseconds'
_I='ifIndex'
_H='IF-MIB'
_G='coCdlFromCdlNetFlowDILastChange'
_F='coCdlFromCdlNetFlowDICurrStatus'
_E='Unsigned32'
_D='read-write'
_C='read-only'
_B='current'
_A='CISCO-CDL-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
ifIndex,=mibBuilder.importSymbols(_H,_I)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_T,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp',_U)
ciscoCdlMIB=ModuleIdentity((1,3,6,1,4,1,9,10,88))
if mibBuilder.loadTexts:ciscoCdlMIB.setRevisions(('2002-10-02 00:00','2002-05-30 00:00'))
class CoCdlAggDefectIndStatus(TextualConvention,Bits):status=_B;namedValues=NamedValues(*(('hopByHopForwardDefect',0),('hopByHopBackwardDefect',1),('endToEndAggPathForwardDefect',2)))
class CoCdlFlowDefectIndStatus(TextualConvention,Bits):status=_B;namedValues=NamedValues(*(('endToEndPathImplicitFwdDefect',0),('endToEndPathBackwardDefect',1)))
class CoCdlNodeBehavior(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('endOfAggPath',1),('endOfHop',2),('cdlRegenerator',3)))
class CoCdlFlowIdentifier(TextualConvention,Unsigned32):status=_B;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CoCdlMIBNotifications_ObjectIdentity=ObjectIdentity
coCdlMIBNotifications=_CoCdlMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,10,88,0))
_CoCdlMIBObjects_ObjectIdentity=ObjectIdentity
coCdlMIBObjects=_CoCdlMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,10,88,1))
_CoCdlBaseGroup_ObjectIdentity=ObjectIdentity
coCdlBaseGroup=_CoCdlBaseGroup_ObjectIdentity((1,3,6,1,4,1,9,10,88,1,1))
_CoCdlIntfTable_Object=MibTable
coCdlIntfTable=_CoCdlIntfTable_Object((1,3,6,1,4,1,9,10,88,1,1,1))
if mibBuilder.loadTexts:coCdlIntfTable.setStatus(_B)
_CoCdlIntfEntry_Object=MibTableRow
coCdlIntfEntry=_CoCdlIntfEntry_Object((1,3,6,1,4,1,9,10,88,1,1,1,1))
coCdlIntfEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:coCdlIntfEntry.setStatus(_B)
_CoCdlAdminStatus_Type=TruthValue
_CoCdlAdminStatus_Object=MibTableColumn
coCdlAdminStatus=_CoCdlAdminStatus_Object((1,3,6,1,4,1,9,10,88,1,1,1,1,1),_CoCdlAdminStatus_Type())
coCdlAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:coCdlAdminStatus.setStatus(_B)
class _CoCdlForceEndOfHop_Type(TruthValue):defaultValue=2
_CoCdlForceEndOfHop_Type.__name__=_U
_CoCdlForceEndOfHop_Object=MibTableColumn
coCdlForceEndOfHop=_CoCdlForceEndOfHop_Object((1,3,6,1,4,1,9,10,88,1,1,1,1,2),_CoCdlForceEndOfHop_Type())
coCdlForceEndOfHop.setMaxAccess(_D)
if mibBuilder.loadTexts:coCdlForceEndOfHop.setStatus(_B)
_CoCdlNodeBehavior_Type=CoCdlNodeBehavior
_CoCdlNodeBehavior_Object=MibTableColumn
coCdlNodeBehavior=_CoCdlNodeBehavior_Object((1,3,6,1,4,1,9,10,88,1,1,1,1,3),_CoCdlNodeBehavior_Type())
coCdlNodeBehavior.setMaxAccess(_C)
if mibBuilder.loadTexts:coCdlNodeBehavior.setStatus(_B)
_CoCdlRxAggDefectIndCurrStatus_Type=CoCdlAggDefectIndStatus
_CoCdlRxAggDefectIndCurrStatus_Object=MibTableColumn
coCdlRxAggDefectIndCurrStatus=_CoCdlRxAggDefectIndCurrStatus_Object((1,3,6,1,4,1,9,10,88,1,1,1,1,4),_CoCdlRxAggDefectIndCurrStatus_Type())
coCdlRxAggDefectIndCurrStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:coCdlRxAggDefectIndCurrStatus.setStatus(_B)
_CoCdlRxAggDefectIndLastChange_Type=TimeStamp
_CoCdlRxAggDefectIndLastChange_Object=MibTableColumn
coCdlRxAggDefectIndLastChange=_CoCdlRxAggDefectIndLastChange_Object((1,3,6,1,4,1,9,10,88,1,1,1,1,5),_CoCdlRxAggDefectIndLastChange_Type())
coCdlRxAggDefectIndLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:coCdlRxAggDefectIndLastChange.setStatus(_B)
_CoCdlTxAggDefectIndCurrStatus_Type=CoCdlAggDefectIndStatus
_CoCdlTxAggDefectIndCurrStatus_Object=MibTableColumn
coCdlTxAggDefectIndCurrStatus=_CoCdlTxAggDefectIndCurrStatus_Object((1,3,6,1,4,1,9,10,88,1,1,1,1,6),_CoCdlTxAggDefectIndCurrStatus_Type())
coCdlTxAggDefectIndCurrStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:coCdlTxAggDefectIndCurrStatus.setStatus(_B)
_CoCdlTxAggDefectIndLastChange_Type=TimeStamp
_CoCdlTxAggDefectIndLastChange_Object=MibTableColumn
coCdlTxAggDefectIndLastChange=_CoCdlTxAggDefectIndLastChange_Object((1,3,6,1,4,1,9,10,88,1,1,1,1,7),_CoCdlTxAggDefectIndLastChange_Type())
coCdlTxAggDefectIndLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:coCdlTxAggDefectIndLastChange.setStatus(_B)
_CoCdlTransmitMaxFlowIdentifier_Type=CoCdlFlowIdentifier
_CoCdlTransmitMaxFlowIdentifier_Object=MibTableColumn
coCdlTransmitMaxFlowIdentifier=_CoCdlTransmitMaxFlowIdentifier_Object((1,3,6,1,4,1,9,10,88,1,1,1,1,8),_CoCdlTransmitMaxFlowIdentifier_Type())
coCdlTransmitMaxFlowIdentifier.setMaxAccess(_D)
if mibBuilder.loadTexts:coCdlTransmitMaxFlowIdentifier.setStatus(_B)
_CoCdlReceiveMaxFlowIdentifier_Type=CoCdlFlowIdentifier
_CoCdlReceiveMaxFlowIdentifier_Object=MibTableColumn
coCdlReceiveMaxFlowIdentifier=_CoCdlReceiveMaxFlowIdentifier_Object((1,3,6,1,4,1,9,10,88,1,1,1,1,9),_CoCdlReceiveMaxFlowIdentifier_Type())
coCdlReceiveMaxFlowIdentifier.setMaxAccess(_D)
if mibBuilder.loadTexts:coCdlReceiveMaxFlowIdentifier.setStatus(_B)
_CoCdlRxHeaderCRCError_Type=Counter32
_CoCdlRxHeaderCRCError_Object=MibTableColumn
coCdlRxHeaderCRCError=_CoCdlRxHeaderCRCError_Object((1,3,6,1,4,1,9,10,88,1,1,1,1,10),_CoCdlRxHeaderCRCError_Type())
coCdlRxHeaderCRCError.setMaxAccess(_C)
if mibBuilder.loadTexts:coCdlRxHeaderCRCError.setStatus(_B)
_CoCdlRxHeaderCRCErrorOverflow_Type=Counter32
_CoCdlRxHeaderCRCErrorOverflow_Object=MibTableColumn
coCdlRxHeaderCRCErrorOverflow=_CoCdlRxHeaderCRCErrorOverflow_Object((1,3,6,1,4,1,9,10,88,1,1,1,1,11),_CoCdlRxHeaderCRCErrorOverflow_Type())
coCdlRxHeaderCRCErrorOverflow.setMaxAccess(_C)
if mibBuilder.loadTexts:coCdlRxHeaderCRCErrorOverflow.setStatus(_B)
_CoCdlHCRxHeaderCRCError_Type=Counter64
_CoCdlHCRxHeaderCRCError_Object=MibTableColumn
coCdlHCRxHeaderCRCError=_CoCdlHCRxHeaderCRCError_Object((1,3,6,1,4,1,9,10,88,1,1,1,1,12),_CoCdlHCRxHeaderCRCError_Type())
coCdlHCRxHeaderCRCError.setMaxAccess(_C)
if mibBuilder.loadTexts:coCdlHCRxHeaderCRCError.setStatus(_B)
_CoCdlRxInvalidFlowID_Type=Counter32
_CoCdlRxInvalidFlowID_Object=MibTableColumn
coCdlRxInvalidFlowID=_CoCdlRxInvalidFlowID_Object((1,3,6,1,4,1,9,10,88,1,1,1,1,13),_CoCdlRxInvalidFlowID_Type())
coCdlRxInvalidFlowID.setMaxAccess(_C)
if mibBuilder.loadTexts:coCdlRxInvalidFlowID.setStatus(_B)
_CoCdlRxInvalidFlowIDOverflow_Type=Counter32
_CoCdlRxInvalidFlowIDOverflow_Object=MibTableColumn
coCdlRxInvalidFlowIDOverflow=_CoCdlRxInvalidFlowIDOverflow_Object((1,3,6,1,4,1,9,10,88,1,1,1,1,14),_CoCdlRxInvalidFlowIDOverflow_Type())
coCdlRxInvalidFlowIDOverflow.setMaxAccess(_C)
if mibBuilder.loadTexts:coCdlRxInvalidFlowIDOverflow.setStatus(_B)
_CoCdlHCRxInvalidFlowID_Type=Counter64
_CoCdlHCRxInvalidFlowID_Object=MibTableColumn
coCdlHCRxInvalidFlowID=_CoCdlHCRxInvalidFlowID_Object((1,3,6,1,4,1,9,10,88,1,1,1,1,15),_CoCdlHCRxInvalidFlowID_Type())
coCdlHCRxInvalidFlowID.setMaxAccess(_C)
if mibBuilder.loadTexts:coCdlHCRxInvalidFlowID.setStatus(_B)
_CoCdlRxNonCdlPackets_Type=Counter32
_CoCdlRxNonCdlPackets_Object=MibTableColumn
coCdlRxNonCdlPackets=_CoCdlRxNonCdlPackets_Object((1,3,6,1,4,1,9,10,88,1,1,1,1,16),_CoCdlRxNonCdlPackets_Type())
coCdlRxNonCdlPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:coCdlRxNonCdlPackets.setStatus(_B)
_CoCdlRxNonCdlPacketsOverflow_Type=Counter32
_CoCdlRxNonCdlPacketsOverflow_Object=MibTableColumn
coCdlRxNonCdlPacketsOverflow=_CoCdlRxNonCdlPacketsOverflow_Object((1,3,6,1,4,1,9,10,88,1,1,1,1,17),_CoCdlRxNonCdlPacketsOverflow_Type())
coCdlRxNonCdlPacketsOverflow.setMaxAccess(_C)
if mibBuilder.loadTexts:coCdlRxNonCdlPacketsOverflow.setStatus(_B)
_CoCdlHCRxNonCdlPackets_Type=Counter64
_CoCdlHCRxNonCdlPackets_Object=MibTableColumn
coCdlHCRxNonCdlPackets=_CoCdlHCRxNonCdlPackets_Object((1,3,6,1,4,1,9,10,88,1,1,1,1,18),_CoCdlHCRxNonCdlPackets_Type())
coCdlHCRxNonCdlPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:coCdlHCRxNonCdlPackets.setStatus(_B)
class _CoCdlDefectIndNotifyEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('disabled',1),('enabledAtTerminatingInterfaces',2),('enabledAtAllInterfaces',3)))
_CoCdlDefectIndNotifyEnable_Type.__name__=_T
_CoCdlDefectIndNotifyEnable_Object=MibScalar
coCdlDefectIndNotifyEnable=_CoCdlDefectIndNotifyEnable_Object((1,3,6,1,4,1,9,10,88,1,1,2),_CoCdlDefectIndNotifyEnable_Type())
coCdlDefectIndNotifyEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:coCdlDefectIndNotifyEnable.setStatus(_B)
class _CoCdlDefectIndSetSoakInterval_Type(Unsigned32):defaultValue=2500;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,60000))
_CoCdlDefectIndSetSoakInterval_Type.__name__=_E
_CoCdlDefectIndSetSoakInterval_Object=MibScalar
coCdlDefectIndSetSoakInterval=_CoCdlDefectIndSetSoakInterval_Object((1,3,6,1,4,1,9,10,88,1,1,3),_CoCdlDefectIndSetSoakInterval_Type())
coCdlDefectIndSetSoakInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:coCdlDefectIndSetSoakInterval.setStatus(_B)
if mibBuilder.loadTexts:coCdlDefectIndSetSoakInterval.setUnits(_J)
class _CoCdlDefectIndClearSoakInterval_Type(Unsigned32):defaultValue=10000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,60000))
_CoCdlDefectIndClearSoakInterval_Type.__name__=_E
_CoCdlDefectIndClearSoakInterval_Object=MibScalar
coCdlDefectIndClearSoakInterval=_CoCdlDefectIndClearSoakInterval_Object((1,3,6,1,4,1,9,10,88,1,1,4),_CoCdlDefectIndClearSoakInterval_Type())
coCdlDefectIndClearSoakInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:coCdlDefectIndClearSoakInterval.setStatus(_B)
if mibBuilder.loadTexts:coCdlDefectIndClearSoakInterval.setUnits(_J)
class _CoCdlDINotifyThrottleInterval_Type(Unsigned32):defaultValue=1000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,60000))
_CoCdlDINotifyThrottleInterval_Type.__name__=_E
_CoCdlDINotifyThrottleInterval_Object=MibScalar
coCdlDINotifyThrottleInterval=_CoCdlDINotifyThrottleInterval_Object((1,3,6,1,4,1,9,10,88,1,1,5),_CoCdlDINotifyThrottleInterval_Type())
coCdlDINotifyThrottleInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:coCdlDINotifyThrottleInterval.setStatus(_B)
if mibBuilder.loadTexts:coCdlDINotifyThrottleInterval.setUnits(_J)
_CoCdlFlowTermGroup_ObjectIdentity=ObjectIdentity
coCdlFlowTermGroup=_CoCdlFlowTermGroup_ObjectIdentity((1,3,6,1,4,1,9,10,88,1,2))
_CoCdlFlowTermTable_Object=MibTable
coCdlFlowTermTable=_CoCdlFlowTermTable_Object((1,3,6,1,4,1,9,10,88,1,2,1))
if mibBuilder.loadTexts:coCdlFlowTermTable.setStatus(_B)
_CoCdlFlowTermEntry_Object=MibTableRow
coCdlFlowTermEntry=_CoCdlFlowTermEntry_Object((1,3,6,1,4,1,9,10,88,1,2,1,1))
coCdlFlowTermEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:coCdlFlowTermEntry.setStatus(_B)
_CoCdlFromCdlNetFlowIdentifier_Type=CoCdlFlowIdentifier
_CoCdlFromCdlNetFlowIdentifier_Object=MibTableColumn
coCdlFromCdlNetFlowIdentifier=_CoCdlFromCdlNetFlowIdentifier_Object((1,3,6,1,4,1,9,10,88,1,2,1,1,1),_CoCdlFromCdlNetFlowIdentifier_Type())
coCdlFromCdlNetFlowIdentifier.setMaxAccess(_D)
if mibBuilder.loadTexts:coCdlFromCdlNetFlowIdentifier.setStatus(_B)
_CoCdlToCdlNetFlowIdentifier_Type=CoCdlFlowIdentifier
_CoCdlToCdlNetFlowIdentifier_Object=MibTableColumn
coCdlToCdlNetFlowIdentifier=_CoCdlToCdlNetFlowIdentifier_Object((1,3,6,1,4,1,9,10,88,1,2,1,1,2),_CoCdlToCdlNetFlowIdentifier_Type())
coCdlToCdlNetFlowIdentifier.setMaxAccess(_D)
if mibBuilder.loadTexts:coCdlToCdlNetFlowIdentifier.setStatus(_B)
_CoCdlFromCdlNetFlowDICurrStatus_Type=CoCdlFlowDefectIndStatus
_CoCdlFromCdlNetFlowDICurrStatus_Object=MibTableColumn
coCdlFromCdlNetFlowDICurrStatus=_CoCdlFromCdlNetFlowDICurrStatus_Object((1,3,6,1,4,1,9,10,88,1,2,1,1,3),_CoCdlFromCdlNetFlowDICurrStatus_Type())
coCdlFromCdlNetFlowDICurrStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:coCdlFromCdlNetFlowDICurrStatus.setStatus(_B)
_CoCdlFromCdlNetFlowDILastChange_Type=TimeStamp
_CoCdlFromCdlNetFlowDILastChange_Object=MibTableColumn
coCdlFromCdlNetFlowDILastChange=_CoCdlFromCdlNetFlowDILastChange_Object((1,3,6,1,4,1,9,10,88,1,2,1,1,4),_CoCdlFromCdlNetFlowDILastChange_Type())
coCdlFromCdlNetFlowDILastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:coCdlFromCdlNetFlowDILastChange.setStatus(_B)
_CoCdlToCdlNetFlowDICurrStatus_Type=CoCdlFlowDefectIndStatus
_CoCdlToCdlNetFlowDICurrStatus_Object=MibTableColumn
coCdlToCdlNetFlowDICurrStatus=_CoCdlToCdlNetFlowDICurrStatus_Object((1,3,6,1,4,1,9,10,88,1,2,1,1,5),_CoCdlToCdlNetFlowDICurrStatus_Type())
coCdlToCdlNetFlowDICurrStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:coCdlToCdlNetFlowDICurrStatus.setStatus(_B)
_CoCdlToCdlNetFlowDILastChange_Type=TimeStamp
_CoCdlToCdlNetFlowDILastChange_Object=MibTableColumn
coCdlToCdlNetFlowDILastChange=_CoCdlToCdlNetFlowDILastChange_Object((1,3,6,1,4,1,9,10,88,1,2,1,1,6),_CoCdlToCdlNetFlowDILastChange_Type())
coCdlToCdlNetFlowDILastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:coCdlToCdlNetFlowDILastChange.setStatus(_B)
_CoCdlFromCdlNetEthernetCRC_Type=Counter32
_CoCdlFromCdlNetEthernetCRC_Object=MibTableColumn
coCdlFromCdlNetEthernetCRC=_CoCdlFromCdlNetEthernetCRC_Object((1,3,6,1,4,1,9,10,88,1,2,1,1,7),_CoCdlFromCdlNetEthernetCRC_Type())
coCdlFromCdlNetEthernetCRC.setMaxAccess(_C)
if mibBuilder.loadTexts:coCdlFromCdlNetEthernetCRC.setStatus(_B)
_CoCdlFromCdlNetEthernetCRCOvrflw_Type=Counter32
_CoCdlFromCdlNetEthernetCRCOvrflw_Object=MibTableColumn
coCdlFromCdlNetEthernetCRCOvrflw=_CoCdlFromCdlNetEthernetCRCOvrflw_Object((1,3,6,1,4,1,9,10,88,1,2,1,1,8),_CoCdlFromCdlNetEthernetCRCOvrflw_Type())
coCdlFromCdlNetEthernetCRCOvrflw.setMaxAccess(_C)
if mibBuilder.loadTexts:coCdlFromCdlNetEthernetCRCOvrflw.setStatus(_B)
_CoCdlFromCdlNetHCEthernetCRC_Type=Counter64
_CoCdlFromCdlNetHCEthernetCRC_Object=MibTableColumn
coCdlFromCdlNetHCEthernetCRC=_CoCdlFromCdlNetHCEthernetCRC_Object((1,3,6,1,4,1,9,10,88,1,2,1,1,9),_CoCdlFromCdlNetHCEthernetCRC_Type())
coCdlFromCdlNetHCEthernetCRC.setMaxAccess(_C)
if mibBuilder.loadTexts:coCdlFromCdlNetHCEthernetCRC.setStatus(_B)
_CoCdlMIBConformance_ObjectIdentity=ObjectIdentity
coCdlMIBConformance=_CoCdlMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,10,88,3))
_CoCdlMIBCompliances_ObjectIdentity=ObjectIdentity
coCdlMIBCompliances=_CoCdlMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,88,3,1))
_CoCdlMIBGroups_ObjectIdentity=ObjectIdentity
coCdlMIBGroups=_CoCdlMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,10,88,3,2))
coCdlMIBBaseGroup=ObjectGroup((1,3,6,1,4,1,9,10,88,3,2,1))
coCdlMIBBaseGroup.setObjects(*((_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c)))
if mibBuilder.loadTexts:coCdlMIBBaseGroup.setStatus(_B)
coCdlMIBFlowIdGroup=ObjectGroup((1,3,6,1,4,1,9,10,88,3,2,2))
coCdlMIBFlowIdGroup.setObjects(*((_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h)))
if mibBuilder.loadTexts:coCdlMIBFlowIdGroup.setStatus(_B)
coCdlMIBFlowTermGroup=ObjectGroup((1,3,6,1,4,1,9,10,88,3,2,3))
coCdlMIBFlowTermGroup.setObjects(*((_A,_K),(_A,_L),(_A,_F),(_A,_G),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:coCdlMIBFlowTermGroup.setStatus(_i)
coCdlDIConfigGroup=ObjectGroup((1,3,6,1,4,1,9,10,88,3,2,4))
coCdlDIConfigGroup.setObjects((_A,_j))
if mibBuilder.loadTexts:coCdlDIConfigGroup.setStatus(_B)
coCdlDIAggMandatoryGroup=ObjectGroup((1,3,6,1,4,1,9,10,88,3,2,5))
coCdlDIAggMandatoryGroup.setObjects(*((_A,_O),(_A,_P),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p)))
if mibBuilder.loadTexts:coCdlDIAggMandatoryGroup.setStatus(_B)
coCdlMIBFlowTerm2Group=ObjectGroup((1,3,6,1,4,1,9,10,88,3,2,8))
coCdlMIBFlowTerm2Group.setObjects(*((_A,_K),(_A,_L),(_A,_F),(_A,_G),(_A,_M),(_A,_N),(_A,_q),(_A,_r),(_A,_s)))
if mibBuilder.loadTexts:coCdlMIBFlowTerm2Group.setStatus(_B)
coCdlRxAggDefectIndChange=NotificationType((1,3,6,1,4,1,9,10,88,0,1))
coCdlRxAggDefectIndChange.setObjects(*((_A,_O),(_A,_P)))
if mibBuilder.loadTexts:coCdlRxAggDefectIndChange.setStatus(_B)
coCdlFromCdlNetFlowDIChange=NotificationType((1,3,6,1,4,1,9,10,88,0,2))
coCdlFromCdlNetFlowDIChange.setObjects(*((_A,_F),(_A,_G)))
if mibBuilder.loadTexts:coCdlFromCdlNetFlowDIChange.setStatus(_B)
coCdlDIAggNotifGroup=NotificationGroup((1,3,6,1,4,1,9,10,88,3,2,6))
coCdlDIAggNotifGroup.setObjects((_A,_t))
if mibBuilder.loadTexts:coCdlDIAggNotifGroup.setStatus(_B)
coCdlDIFlowNotifGroup=NotificationGroup((1,3,6,1,4,1,9,10,88,3,2,7))
coCdlDIFlowNotifGroup.setObjects((_A,_u))
if mibBuilder.loadTexts:coCdlDIFlowNotifGroup.setStatus(_B)
coCdlMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,88,3,1,1))
coCdlMIBCompliance.setObjects(*((_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:coCdlMIBCompliance.setStatus(_i)
coCdlMIBCompliance2=ModuleCompliance((1,3,6,1,4,1,9,10,88,3,1,2))
coCdlMIBCompliance2.setObjects(*((_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:coCdlMIBCompliance2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'CoCdlAggDefectIndStatus':CoCdlAggDefectIndStatus,'CoCdlFlowDefectIndStatus':CoCdlFlowDefectIndStatus,'CoCdlNodeBehavior':CoCdlNodeBehavior,'CoCdlFlowIdentifier':CoCdlFlowIdentifier,'ciscoCdlMIB':ciscoCdlMIB,'coCdlMIBNotifications':coCdlMIBNotifications,_t:coCdlRxAggDefectIndChange,_u:coCdlFromCdlNetFlowDIChange,'coCdlMIBObjects':coCdlMIBObjects,'coCdlBaseGroup':coCdlBaseGroup,'coCdlIntfTable':coCdlIntfTable,'coCdlIntfEntry':coCdlIntfEntry,_V:coCdlAdminStatus,_j:coCdlForceEndOfHop,_W:coCdlNodeBehavior,_O:coCdlRxAggDefectIndCurrStatus,_P:coCdlRxAggDefectIndLastChange,_k:coCdlTxAggDefectIndCurrStatus,_l:coCdlTxAggDefectIndLastChange,_d:coCdlTransmitMaxFlowIdentifier,_e:coCdlReceiveMaxFlowIdentifier,_X:coCdlRxHeaderCRCError,_Y:coCdlRxHeaderCRCErrorOverflow,_Z:coCdlHCRxHeaderCRCError,_f:coCdlRxInvalidFlowID,_g:coCdlRxInvalidFlowIDOverflow,_h:coCdlHCRxInvalidFlowID,_a:coCdlRxNonCdlPackets,_b:coCdlRxNonCdlPacketsOverflow,_c:coCdlHCRxNonCdlPackets,_m:coCdlDefectIndNotifyEnable,_n:coCdlDefectIndSetSoakInterval,_o:coCdlDefectIndClearSoakInterval,_p:coCdlDINotifyThrottleInterval,'coCdlFlowTermGroup':coCdlFlowTermGroup,'coCdlFlowTermTable':coCdlFlowTermTable,'coCdlFlowTermEntry':coCdlFlowTermEntry,_K:coCdlFromCdlNetFlowIdentifier,_L:coCdlToCdlNetFlowIdentifier,_F:coCdlFromCdlNetFlowDICurrStatus,_G:coCdlFromCdlNetFlowDILastChange,_M:coCdlToCdlNetFlowDICurrStatus,_N:coCdlToCdlNetFlowDILastChange,_q:coCdlFromCdlNetEthernetCRC,_r:coCdlFromCdlNetEthernetCRCOvrflw,_s:coCdlFromCdlNetHCEthernetCRC,'coCdlMIBConformance':coCdlMIBConformance,'coCdlMIBCompliances':coCdlMIBCompliances,'coCdlMIBCompliance':coCdlMIBCompliance,'coCdlMIBCompliance2':coCdlMIBCompliance2,'coCdlMIBGroups':coCdlMIBGroups,_Q:coCdlMIBBaseGroup,'coCdlMIBFlowIdGroup':coCdlMIBFlowIdGroup,'coCdlMIBFlowTermGroup':coCdlMIBFlowTermGroup,'coCdlDIConfigGroup':coCdlDIConfigGroup,_R:coCdlDIAggMandatoryGroup,_S:coCdlDIAggNotifGroup,'coCdlDIFlowNotifGroup':coCdlDIFlowNotifGroup,'coCdlMIBFlowTerm2Group':coCdlMIBFlowTerm2Group})