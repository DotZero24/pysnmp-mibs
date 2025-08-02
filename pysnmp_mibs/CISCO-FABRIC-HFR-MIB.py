_AI='cfhFabricCapacityGroup'
_AH='cfhBundleDownedLinkNotification'
_AG='cfhBundleStateNotification'
_AF='cfhPlaneStateNotification'
_AE='cfhPlaneCapacityThreshold'
_AD='cfhCardPlaneRxConnectivity'
_AC='cfhCardPlaneTxConnectivity'
_AB='cfhCardFabInUseDiscTime'
_AA='cfhCardFabUsage'
_A9='cfhCardFabInUse'
_A8='cfhBundlePortStatsHighRxPECells'
_A7='cfhBundlePortStatsHighRxUCECells'
_A6='cfhBundlePortStatsHighRxCECells'
_A5='cfhBundlePortStatsRxPECells'
_A4='cfhBundlePortStatsRxUCECells'
_A3='cfhBundlePortStatsRxCECells'
_A2='cfhBundlePortStatsTxDataCells'
_A1='cfhBundlePortStatsRxDataCells'
_A0='cfhBundlePortGrpId'
_z='cfhBundlePortOperState'
_y='cfhBundlePortAdminState'
_x='cfhBundlePortTotalNumber'
_w='cfhBundlePortSecondId'
_v='cfhBundlePortSecondCardIndex'
_u='cfhBundlePortLCRId'
_t='cfhBundlePortLCRCardIndex'
_s='cfhBundleTotalLinks'
_r='cfhBundleDowned'
_q='cfhBundleTotal'
_p='cfhPlaneStatsCounterDiscTime'
_o='cfhPlaneStatsMulticastLostCells'
_n='cfhPlaneStatsUnicastLostCells'
_m='cfhPlaneStatsRxPECells'
_l='cfhPlaneStatsRxUCECells'
_k='cfhPlaneStatsRxCECells'
_j='cfhPlaneStatsTxDataCells'
_i='cfhPlaneStatsRxDataCells'
_h='cfhPlaneDownedBundles'
_g='cfhPlaneTotalBundles'
_f='cfhPlaneAdminStatus'
_e='cfhGenBundleDownedLinkTrapEnable'
_d='cfhGenBundleStateTrapEnable'
_c='cfhGenPlaneStateTrapEnable'
_b='cfhBundlePortStatsEntry'
_a='cfhPlaneStatsEntry'
_Z='cfhBundlePortId'
_Y='cfhBundleId'
_X='Unsigned32'
_W='cfhNotificationsGroup'
_V='cfhCardGroup'
_U='cfhBundlePortGroup'
_T='cfhBundleGroup'
_S='cfhPlaneGroup'
_R='cfhGenInfoGroup'
_Q='cfhBundleDownedLinks'
_P='cfhPlaneOperStatus'
_O='not-accessible'
_N='cfhPlaneId'
_M='cfhBundleOperStatus'
_L='cfhBundlePlane'
_K='cfhBundleName'
_J='down'
_I='up'
_H='TruthValue'
_G='Integer32'
_F='entPhysicalIndex'
_E='ENTITY-MIB'
_D='read-write'
_C='read-only'
_B='CISCO-FABRIC-HFR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
PhysicalIndex,entPhysicalIndex=mibBuilder.importSymbols(_E,'PhysicalIndex',_F)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_X,'iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp',_H)
ciscoFabricHfrMIB=ModuleIdentity((1,3,6,1,4,1,9,9,257))
if mibBuilder.loadTexts:ciscoFabricHfrMIB.setRevisions(('2009-04-14 00:00','2006-01-01 00:00','2003-06-09 00:00'))
class CfhPlane(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
class CfhBundle(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
class CfhAdminState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
class CfhScaledPercentage(TextualConvention,Gauge32):status=_A;subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_CfhMIBNotifications_ObjectIdentity=ObjectIdentity
cfhMIBNotifications=_CfhMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,257,0))
_CiscoFabricHfrMIBObjects_ObjectIdentity=ObjectIdentity
ciscoFabricHfrMIBObjects=_CiscoFabricHfrMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,257,1))
_CfhGeneral_ObjectIdentity=ObjectIdentity
cfhGeneral=_CfhGeneral_ObjectIdentity((1,3,6,1,4,1,9,9,257,1,1))
class _CfhGenPlaneStateTrapEnable_Type(TruthValue):defaultValue=2
_CfhGenPlaneStateTrapEnable_Type.__name__=_H
_CfhGenPlaneStateTrapEnable_Object=MibScalar
cfhGenPlaneStateTrapEnable=_CfhGenPlaneStateTrapEnable_Object((1,3,6,1,4,1,9,9,257,1,1,1),_CfhGenPlaneStateTrapEnable_Type())
cfhGenPlaneStateTrapEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:cfhGenPlaneStateTrapEnable.setStatus(_A)
class _CfhGenBundleStateTrapEnable_Type(TruthValue):defaultValue=2
_CfhGenBundleStateTrapEnable_Type.__name__=_H
_CfhGenBundleStateTrapEnable_Object=MibScalar
cfhGenBundleStateTrapEnable=_CfhGenBundleStateTrapEnable_Object((1,3,6,1,4,1,9,9,257,1,1,2),_CfhGenBundleStateTrapEnable_Type())
cfhGenBundleStateTrapEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:cfhGenBundleStateTrapEnable.setStatus(_A)
class _CfhGenBundleDownedLinkTrapEnable_Type(TruthValue):defaultValue=2
_CfhGenBundleDownedLinkTrapEnable_Type.__name__=_H
_CfhGenBundleDownedLinkTrapEnable_Object=MibScalar
cfhGenBundleDownedLinkTrapEnable=_CfhGenBundleDownedLinkTrapEnable_Object((1,3,6,1,4,1,9,9,257,1,1,3),_CfhGenBundleDownedLinkTrapEnable_Type())
cfhGenBundleDownedLinkTrapEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:cfhGenBundleDownedLinkTrapEnable.setStatus(_A)
_CfhPlane_ObjectIdentity=ObjectIdentity
cfhPlane=_CfhPlane_ObjectIdentity((1,3,6,1,4,1,9,9,257,1,2))
_CfhPlaneTable_Object=MibTable
cfhPlaneTable=_CfhPlaneTable_Object((1,3,6,1,4,1,9,9,257,1,2,1))
if mibBuilder.loadTexts:cfhPlaneTable.setStatus(_A)
_CfhPlaneEntry_Object=MibTableRow
cfhPlaneEntry=_CfhPlaneEntry_Object((1,3,6,1,4,1,9,9,257,1,2,1,1))
cfhPlaneEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:cfhPlaneEntry.setStatus(_A)
_CfhPlaneId_Type=CfhPlane
_CfhPlaneId_Object=MibTableColumn
cfhPlaneId=_CfhPlaneId_Object((1,3,6,1,4,1,9,9,257,1,2,1,1,1),_CfhPlaneId_Type())
cfhPlaneId.setMaxAccess(_O)
if mibBuilder.loadTexts:cfhPlaneId.setStatus(_A)
_CfhPlaneAdminStatus_Type=CfhAdminState
_CfhPlaneAdminStatus_Object=MibTableColumn
cfhPlaneAdminStatus=_CfhPlaneAdminStatus_Object((1,3,6,1,4,1,9,9,257,1,2,1,1,2),_CfhPlaneAdminStatus_Type())
cfhPlaneAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cfhPlaneAdminStatus.setStatus(_A)
class _CfhPlaneOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),(_J,2),('mcastDown',3),('oos',4)))
_CfhPlaneOperStatus_Type.__name__=_G
_CfhPlaneOperStatus_Object=MibTableColumn
cfhPlaneOperStatus=_CfhPlaneOperStatus_Object((1,3,6,1,4,1,9,9,257,1,2,1,1,3),_CfhPlaneOperStatus_Type())
cfhPlaneOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cfhPlaneOperStatus.setStatus(_A)
_CfhPlaneTotalBundles_Type=Unsigned32
_CfhPlaneTotalBundles_Object=MibTableColumn
cfhPlaneTotalBundles=_CfhPlaneTotalBundles_Object((1,3,6,1,4,1,9,9,257,1,2,1,1,4),_CfhPlaneTotalBundles_Type())
cfhPlaneTotalBundles.setMaxAccess(_C)
if mibBuilder.loadTexts:cfhPlaneTotalBundles.setStatus(_A)
_CfhPlaneDownedBundles_Type=Gauge32
_CfhPlaneDownedBundles_Object=MibTableColumn
cfhPlaneDownedBundles=_CfhPlaneDownedBundles_Object((1,3,6,1,4,1,9,9,257,1,2,1,1,5),_CfhPlaneDownedBundles_Type())
cfhPlaneDownedBundles.setMaxAccess(_C)
if mibBuilder.loadTexts:cfhPlaneDownedBundles.setStatus(_A)
_CfhPlaneStatsTable_Object=MibTable
cfhPlaneStatsTable=_CfhPlaneStatsTable_Object((1,3,6,1,4,1,9,9,257,1,2,2))
if mibBuilder.loadTexts:cfhPlaneStatsTable.setStatus(_A)
_CfhPlaneStatsEntry_Object=MibTableRow
cfhPlaneStatsEntry=_CfhPlaneStatsEntry_Object((1,3,6,1,4,1,9,9,257,1,2,2,1))
if mibBuilder.loadTexts:cfhPlaneStatsEntry.setStatus(_A)
_CfhPlaneStatsRxDataCells_Type=Counter64
_CfhPlaneStatsRxDataCells_Object=MibTableColumn
cfhPlaneStatsRxDataCells=_CfhPlaneStatsRxDataCells_Object((1,3,6,1,4,1,9,9,257,1,2,2,1,1),_CfhPlaneStatsRxDataCells_Type())
cfhPlaneStatsRxDataCells.setMaxAccess(_C)
if mibBuilder.loadTexts:cfhPlaneStatsRxDataCells.setStatus(_A)
_CfhPlaneStatsTxDataCells_Type=Counter64
_CfhPlaneStatsTxDataCells_Object=MibTableColumn
cfhPlaneStatsTxDataCells=_CfhPlaneStatsTxDataCells_Object((1,3,6,1,4,1,9,9,257,1,2,2,1,2),_CfhPlaneStatsTxDataCells_Type())
cfhPlaneStatsTxDataCells.setMaxAccess(_C)
if mibBuilder.loadTexts:cfhPlaneStatsTxDataCells.setStatus(_A)
_CfhPlaneStatsRxCECells_Type=Counter32
_CfhPlaneStatsRxCECells_Object=MibTableColumn
cfhPlaneStatsRxCECells=_CfhPlaneStatsRxCECells_Object((1,3,6,1,4,1,9,9,257,1,2,2,1,3),_CfhPlaneStatsRxCECells_Type())
cfhPlaneStatsRxCECells.setMaxAccess(_C)
if mibBuilder.loadTexts:cfhPlaneStatsRxCECells.setStatus(_A)
_CfhPlaneStatsRxUCECells_Type=Counter32
_CfhPlaneStatsRxUCECells_Object=MibTableColumn
cfhPlaneStatsRxUCECells=_CfhPlaneStatsRxUCECells_Object((1,3,6,1,4,1,9,9,257,1,2,2,1,4),_CfhPlaneStatsRxUCECells_Type())
cfhPlaneStatsRxUCECells.setMaxAccess(_C)
if mibBuilder.loadTexts:cfhPlaneStatsRxUCECells.setStatus(_A)
_CfhPlaneStatsRxPECells_Type=Counter32
_CfhPlaneStatsRxPECells_Object=MibTableColumn
cfhPlaneStatsRxPECells=_CfhPlaneStatsRxPECells_Object((1,3,6,1,4,1,9,9,257,1,2,2,1,5),_CfhPlaneStatsRxPECells_Type())
cfhPlaneStatsRxPECells.setMaxAccess(_C)
if mibBuilder.loadTexts:cfhPlaneStatsRxPECells.setStatus(_A)
_CfhPlaneStatsUnicastLostCells_Type=Counter32
_CfhPlaneStatsUnicastLostCells_Object=MibTableColumn
cfhPlaneStatsUnicastLostCells=_CfhPlaneStatsUnicastLostCells_Object((1,3,6,1,4,1,9,9,257,1,2,2,1,6),_CfhPlaneStatsUnicastLostCells_Type())
cfhPlaneStatsUnicastLostCells.setMaxAccess(_C)
if mibBuilder.loadTexts:cfhPlaneStatsUnicastLostCells.setStatus(_A)
_CfhPlaneStatsMulticastLostCells_Type=Counter32
_CfhPlaneStatsMulticastLostCells_Object=MibTableColumn
cfhPlaneStatsMulticastLostCells=_CfhPlaneStatsMulticastLostCells_Object((1,3,6,1,4,1,9,9,257,1,2,2,1,7),_CfhPlaneStatsMulticastLostCells_Type())
cfhPlaneStatsMulticastLostCells.setMaxAccess(_C)
if mibBuilder.loadTexts:cfhPlaneStatsMulticastLostCells.setStatus(_A)
_CfhPlaneStatsCounterDiscTime_Type=TimeStamp
_CfhPlaneStatsCounterDiscTime_Object=MibTableColumn
cfhPlaneStatsCounterDiscTime=_CfhPlaneStatsCounterDiscTime_Object((1,3,6,1,4,1,9,9,257,1,2,2,1,8),_CfhPlaneStatsCounterDiscTime_Type())
cfhPlaneStatsCounterDiscTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cfhPlaneStatsCounterDiscTime.setStatus(_A)
_CfhPlaneCapacityThreshold_Type=Unsigned32
_CfhPlaneCapacityThreshold_Object=MibScalar
cfhPlaneCapacityThreshold=_CfhPlaneCapacityThreshold_Object((1,3,6,1,4,1,9,9,257,1,2,3),_CfhPlaneCapacityThreshold_Type())
cfhPlaneCapacityThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cfhPlaneCapacityThreshold.setStatus(_A)
_CfhBundle_ObjectIdentity=ObjectIdentity
cfhBundle=_CfhBundle_ObjectIdentity((1,3,6,1,4,1,9,9,257,1,3))
_CfhBundleTotal_Type=Unsigned32
_CfhBundleTotal_Object=MibScalar
cfhBundleTotal=_CfhBundleTotal_Object((1,3,6,1,4,1,9,9,257,1,3,1),_CfhBundleTotal_Type())
cfhBundleTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:cfhBundleTotal.setStatus(_A)
_CfhBundleDowned_Type=Gauge32
_CfhBundleDowned_Object=MibScalar
cfhBundleDowned=_CfhBundleDowned_Object((1,3,6,1,4,1,9,9,257,1,3,2),_CfhBundleDowned_Type())
cfhBundleDowned.setMaxAccess(_C)
if mibBuilder.loadTexts:cfhBundleDowned.setStatus(_A)
_CfhBundleTable_Object=MibTable
cfhBundleTable=_CfhBundleTable_Object((1,3,6,1,4,1,9,9,257,1,3,3))
if mibBuilder.loadTexts:cfhBundleTable.setStatus(_A)
_CfhBundleEntry_Object=MibTableRow
cfhBundleEntry=_CfhBundleEntry_Object((1,3,6,1,4,1,9,9,257,1,3,3,1))
cfhBundleEntry.setIndexNames((0,_B,_Y))
if mibBuilder.loadTexts:cfhBundleEntry.setStatus(_A)
_CfhBundleId_Type=CfhBundle
_CfhBundleId_Object=MibTableColumn
cfhBundleId=_CfhBundleId_Object((1,3,6,1,4,1,9,9,257,1,3,3,1,1),_CfhBundleId_Type())
cfhBundleId.setMaxAccess(_O)
if mibBuilder.loadTexts:cfhBundleId.setStatus(_A)
_CfhBundleName_Type=SnmpAdminString
_CfhBundleName_Object=MibTableColumn
cfhBundleName=_CfhBundleName_Object((1,3,6,1,4,1,9,9,257,1,3,3,1,2),_CfhBundleName_Type())
cfhBundleName.setMaxAccess(_C)
if mibBuilder.loadTexts:cfhBundleName.setStatus(_A)
_CfhBundlePlane_Type=CfhPlane
_CfhBundlePlane_Object=MibTableColumn
cfhBundlePlane=_CfhBundlePlane_Object((1,3,6,1,4,1,9,9,257,1,3,3,1,3),_CfhBundlePlane_Type())
cfhBundlePlane.setMaxAccess(_C)
if mibBuilder.loadTexts:cfhBundlePlane.setStatus(_A)
class _CfhBundleOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_CfhBundleOperStatus_Type.__name__=_G
_CfhBundleOperStatus_Object=MibTableColumn
cfhBundleOperStatus=_CfhBundleOperStatus_Object((1,3,6,1,4,1,9,9,257,1,3,3,1,4),_CfhBundleOperStatus_Type())
cfhBundleOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cfhBundleOperStatus.setStatus(_A)
_CfhBundleTotalLinks_Type=Unsigned32
_CfhBundleTotalLinks_Object=MibTableColumn
cfhBundleTotalLinks=_CfhBundleTotalLinks_Object((1,3,6,1,4,1,9,9,257,1,3,3,1,5),_CfhBundleTotalLinks_Type())
cfhBundleTotalLinks.setMaxAccess(_C)
if mibBuilder.loadTexts:cfhBundleTotalLinks.setStatus(_A)
_CfhBundleDownedLinks_Type=Gauge32
_CfhBundleDownedLinks_Object=MibTableColumn
cfhBundleDownedLinks=_CfhBundleDownedLinks_Object((1,3,6,1,4,1,9,9,257,1,3,3,1,6),_CfhBundleDownedLinks_Type())
cfhBundleDownedLinks.setMaxAccess(_C)
if mibBuilder.loadTexts:cfhBundleDownedLinks.setStatus(_A)
_CfhBundlePortLCRCardIndex_Type=PhysicalIndex
_CfhBundlePortLCRCardIndex_Object=MibTableColumn
cfhBundlePortLCRCardIndex=_CfhBundlePortLCRCardIndex_Object((1,3,6,1,4,1,9,9,257,1,3,3,1,7),_CfhBundlePortLCRCardIndex_Type())
cfhBundlePortLCRCardIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cfhBundlePortLCRCardIndex.setStatus(_A)
_CfhBundlePortLCRId_Type=Unsigned32
_CfhBundlePortLCRId_Object=MibTableColumn
cfhBundlePortLCRId=_CfhBundlePortLCRId_Object((1,3,6,1,4,1,9,9,257,1,3,3,1,8),_CfhBundlePortLCRId_Type())
cfhBundlePortLCRId.setMaxAccess(_C)
if mibBuilder.loadTexts:cfhBundlePortLCRId.setStatus(_A)
_CfhBundlePortSecondCardIndex_Type=PhysicalIndex
_CfhBundlePortSecondCardIndex_Object=MibTableColumn
cfhBundlePortSecondCardIndex=_CfhBundlePortSecondCardIndex_Object((1,3,6,1,4,1,9,9,257,1,3,3,1,9),_CfhBundlePortSecondCardIndex_Type())
cfhBundlePortSecondCardIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cfhBundlePortSecondCardIndex.setStatus(_A)
_CfhBundlePortSecondId_Type=Unsigned32
_CfhBundlePortSecondId_Object=MibTableColumn
cfhBundlePortSecondId=_CfhBundlePortSecondId_Object((1,3,6,1,4,1,9,9,257,1,3,3,1,10),_CfhBundlePortSecondId_Type())
cfhBundlePortSecondId.setMaxAccess(_C)
if mibBuilder.loadTexts:cfhBundlePortSecondId.setStatus(_A)
_CfhBundlePort_ObjectIdentity=ObjectIdentity
cfhBundlePort=_CfhBundlePort_ObjectIdentity((1,3,6,1,4,1,9,9,257,1,4))
_CfhBundlePortTotalNumber_Type=Unsigned32
_CfhBundlePortTotalNumber_Object=MibScalar
cfhBundlePortTotalNumber=_CfhBundlePortTotalNumber_Object((1,3,6,1,4,1,9,9,257,1,4,1),_CfhBundlePortTotalNumber_Type())
cfhBundlePortTotalNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cfhBundlePortTotalNumber.setStatus(_A)
_CfhBundlePortTable_Object=MibTable
cfhBundlePortTable=_CfhBundlePortTable_Object((1,3,6,1,4,1,9,9,257,1,4,2))
if mibBuilder.loadTexts:cfhBundlePortTable.setStatus(_A)
_CfhBundlePortEntry_Object=MibTableRow
cfhBundlePortEntry=_CfhBundlePortEntry_Object((1,3,6,1,4,1,9,9,257,1,4,2,1))
cfhBundlePortEntry.setIndexNames((0,_E,_F),(0,_B,_Z))
if mibBuilder.loadTexts:cfhBundlePortEntry.setStatus(_A)
class _CfhBundlePortId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CfhBundlePortId_Type.__name__=_X
_CfhBundlePortId_Object=MibTableColumn
cfhBundlePortId=_CfhBundlePortId_Object((1,3,6,1,4,1,9,9,257,1,4,2,1,1),_CfhBundlePortId_Type())
cfhBundlePortId.setMaxAccess(_O)
if mibBuilder.loadTexts:cfhBundlePortId.setStatus(_A)
_CfhBundlePortAdminState_Type=CfhAdminState
_CfhBundlePortAdminState_Object=MibTableColumn
cfhBundlePortAdminState=_CfhBundlePortAdminState_Object((1,3,6,1,4,1,9,9,257,1,4,2,1,3),_CfhBundlePortAdminState_Type())
cfhBundlePortAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:cfhBundlePortAdminState.setStatus(_A)
class _CfhBundlePortOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unknown',1),(_I,2),(_J,3)))
_CfhBundlePortOperState_Type.__name__=_G
_CfhBundlePortOperState_Object=MibTableColumn
cfhBundlePortOperState=_CfhBundlePortOperState_Object((1,3,6,1,4,1,9,9,257,1,4,2,1,4),_CfhBundlePortOperState_Type())
cfhBundlePortOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:cfhBundlePortOperState.setStatus(_A)
_CfhBundlePortGrpId_Type=CfhBundle
_CfhBundlePortGrpId_Object=MibTableColumn
cfhBundlePortGrpId=_CfhBundlePortGrpId_Object((1,3,6,1,4,1,9,9,257,1,4,2,1,5),_CfhBundlePortGrpId_Type())
cfhBundlePortGrpId.setMaxAccess(_C)
if mibBuilder.loadTexts:cfhBundlePortGrpId.setStatus(_A)
_CfhBundlePortStatsTable_Object=MibTable
cfhBundlePortStatsTable=_CfhBundlePortStatsTable_Object((1,3,6,1,4,1,9,9,257,1,4,3))
if mibBuilder.loadTexts:cfhBundlePortStatsTable.setStatus(_A)
_CfhBundlePortStatsEntry_Object=MibTableRow
cfhBundlePortStatsEntry=_CfhBundlePortStatsEntry_Object((1,3,6,1,4,1,9,9,257,1,4,3,1))
if mibBuilder.loadTexts:cfhBundlePortStatsEntry.setStatus(_A)
_CfhBundlePortStatsRxDataCells_Type=Counter64
_CfhBundlePortStatsRxDataCells_Object=MibTableColumn
cfhBundlePortStatsRxDataCells=_CfhBundlePortStatsRxDataCells_Object((1,3,6,1,4,1,9,9,257,1,4,3,1,1),_CfhBundlePortStatsRxDataCells_Type())
cfhBundlePortStatsRxDataCells.setMaxAccess(_C)
if mibBuilder.loadTexts:cfhBundlePortStatsRxDataCells.setStatus(_A)
_CfhBundlePortStatsTxDataCells_Type=Counter64
_CfhBundlePortStatsTxDataCells_Object=MibTableColumn
cfhBundlePortStatsTxDataCells=_CfhBundlePortStatsTxDataCells_Object((1,3,6,1,4,1,9,9,257,1,4,3,1,2),_CfhBundlePortStatsTxDataCells_Type())
cfhBundlePortStatsTxDataCells.setMaxAccess(_C)
if mibBuilder.loadTexts:cfhBundlePortStatsTxDataCells.setStatus(_A)
_CfhBundlePortStatsRxCECells_Type=Counter32
_CfhBundlePortStatsRxCECells_Object=MibTableColumn
cfhBundlePortStatsRxCECells=_CfhBundlePortStatsRxCECells_Object((1,3,6,1,4,1,9,9,257,1,4,3,1,3),_CfhBundlePortStatsRxCECells_Type())
cfhBundlePortStatsRxCECells.setMaxAccess(_C)
if mibBuilder.loadTexts:cfhBundlePortStatsRxCECells.setStatus(_A)
_CfhBundlePortStatsRxUCECells_Type=Counter32
_CfhBundlePortStatsRxUCECells_Object=MibTableColumn
cfhBundlePortStatsRxUCECells=_CfhBundlePortStatsRxUCECells_Object((1,3,6,1,4,1,9,9,257,1,4,3,1,4),_CfhBundlePortStatsRxUCECells_Type())
cfhBundlePortStatsRxUCECells.setMaxAccess(_C)
if mibBuilder.loadTexts:cfhBundlePortStatsRxUCECells.setStatus(_A)
_CfhBundlePortStatsRxPECells_Type=Counter32
_CfhBundlePortStatsRxPECells_Object=MibTableColumn
cfhBundlePortStatsRxPECells=_CfhBundlePortStatsRxPECells_Object((1,3,6,1,4,1,9,9,257,1,4,3,1,5),_CfhBundlePortStatsRxPECells_Type())
cfhBundlePortStatsRxPECells.setMaxAccess(_C)
if mibBuilder.loadTexts:cfhBundlePortStatsRxPECells.setStatus(_A)
_CfhBundlePortStatsHighRxCECells_Type=Gauge32
_CfhBundlePortStatsHighRxCECells_Object=MibTableColumn
cfhBundlePortStatsHighRxCECells=_CfhBundlePortStatsHighRxCECells_Object((1,3,6,1,4,1,9,9,257,1,4,3,1,6),_CfhBundlePortStatsHighRxCECells_Type())
cfhBundlePortStatsHighRxCECells.setMaxAccess(_C)
if mibBuilder.loadTexts:cfhBundlePortStatsHighRxCECells.setStatus(_A)
_CfhBundlePortStatsHighRxUCECells_Type=Gauge32
_CfhBundlePortStatsHighRxUCECells_Object=MibTableColumn
cfhBundlePortStatsHighRxUCECells=_CfhBundlePortStatsHighRxUCECells_Object((1,3,6,1,4,1,9,9,257,1,4,3,1,7),_CfhBundlePortStatsHighRxUCECells_Type())
cfhBundlePortStatsHighRxUCECells.setMaxAccess(_C)
if mibBuilder.loadTexts:cfhBundlePortStatsHighRxUCECells.setStatus(_A)
_CfhBundlePortStatsHighRxPECells_Type=Gauge32
_CfhBundlePortStatsHighRxPECells_Object=MibTableColumn
cfhBundlePortStatsHighRxPECells=_CfhBundlePortStatsHighRxPECells_Object((1,3,6,1,4,1,9,9,257,1,4,3,1,8),_CfhBundlePortStatsHighRxPECells_Type())
cfhBundlePortStatsHighRxPECells.setMaxAccess(_C)
if mibBuilder.loadTexts:cfhBundlePortStatsHighRxPECells.setStatus(_A)
_CfhCard_ObjectIdentity=ObjectIdentity
cfhCard=_CfhCard_ObjectIdentity((1,3,6,1,4,1,9,9,257,1,5))
_CfhCardTable_Object=MibTable
cfhCardTable=_CfhCardTable_Object((1,3,6,1,4,1,9,9,257,1,5,1))
if mibBuilder.loadTexts:cfhCardTable.setStatus(_A)
_CfhCardEntry_Object=MibTableRow
cfhCardEntry=_CfhCardEntry_Object((1,3,6,1,4,1,9,9,257,1,5,1,1))
cfhCardEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:cfhCardEntry.setStatus(_A)
_CfhCardFabInUse_Type=TruthValue
_CfhCardFabInUse_Object=MibTableColumn
cfhCardFabInUse=_CfhCardFabInUse_Object((1,3,6,1,4,1,9,9,257,1,5,1,1,1),_CfhCardFabInUse_Type())
cfhCardFabInUse.setMaxAccess(_C)
if mibBuilder.loadTexts:cfhCardFabInUse.setStatus(_A)
_CfhCardFabUsage_Type=CfhScaledPercentage
_CfhCardFabUsage_Object=MibTableColumn
cfhCardFabUsage=_CfhCardFabUsage_Object((1,3,6,1,4,1,9,9,257,1,5,1,1,2),_CfhCardFabUsage_Type())
cfhCardFabUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:cfhCardFabUsage.setStatus(_A)
if mibBuilder.loadTexts:cfhCardFabUsage.setUnits('thousandths of a percent')
_CfhCardFabInUseDiscTime_Type=TimeStamp
_CfhCardFabInUseDiscTime_Object=MibTableColumn
cfhCardFabInUseDiscTime=_CfhCardFabInUseDiscTime_Object((1,3,6,1,4,1,9,9,257,1,5,1,1,3),_CfhCardFabInUseDiscTime_Type())
cfhCardFabInUseDiscTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cfhCardFabInUseDiscTime.setStatus(_A)
_CfhCardPlaneTable_Object=MibTable
cfhCardPlaneTable=_CfhCardPlaneTable_Object((1,3,6,1,4,1,9,9,257,1,5,2))
if mibBuilder.loadTexts:cfhCardPlaneTable.setStatus(_A)
_CfhCardPlaneEntry_Object=MibTableRow
cfhCardPlaneEntry=_CfhCardPlaneEntry_Object((1,3,6,1,4,1,9,9,257,1,5,2,1))
cfhCardPlaneEntry.setIndexNames((0,_E,_F),(0,_B,_N))
if mibBuilder.loadTexts:cfhCardPlaneEntry.setStatus(_A)
_CfhCardPlaneTxConnectivity_Type=TruthValue
_CfhCardPlaneTxConnectivity_Object=MibTableColumn
cfhCardPlaneTxConnectivity=_CfhCardPlaneTxConnectivity_Object((1,3,6,1,4,1,9,9,257,1,5,2,1,1),_CfhCardPlaneTxConnectivity_Type())
cfhCardPlaneTxConnectivity.setMaxAccess(_C)
if mibBuilder.loadTexts:cfhCardPlaneTxConnectivity.setStatus(_A)
_CfhCardPlaneRxConnectivity_Type=TruthValue
_CfhCardPlaneRxConnectivity_Object=MibTableColumn
cfhCardPlaneRxConnectivity=_CfhCardPlaneRxConnectivity_Object((1,3,6,1,4,1,9,9,257,1,5,2,1,2),_CfhCardPlaneRxConnectivity_Type())
cfhCardPlaneRxConnectivity.setMaxAccess(_C)
if mibBuilder.loadTexts:cfhCardPlaneRxConnectivity.setStatus(_A)
_CfhMIBConformance_ObjectIdentity=ObjectIdentity
cfhMIBConformance=_CfhMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,257,3))
_CfhMIBCompliances_ObjectIdentity=ObjectIdentity
cfhMIBCompliances=_CfhMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,257,3,1))
_CfhMIBGroups_ObjectIdentity=ObjectIdentity
cfhMIBGroups=_CfhMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,257,3,2))
cfhPlaneEntry.registerAugmentions((_B,_a))
cfhPlaneStatsEntry.setIndexNames(*cfhPlaneEntry.getIndexNames())
cfhBundlePortEntry.registerAugmentions((_B,_b))
cfhBundlePortStatsEntry.setIndexNames(*cfhBundlePortEntry.getIndexNames())
cfhGenInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,257,3,2,1))
cfhGenInfoGroup.setObjects(*((_B,_c),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:cfhGenInfoGroup.setStatus(_A)
cfhPlaneGroup=ObjectGroup((1,3,6,1,4,1,9,9,257,3,2,2))
cfhPlaneGroup.setObjects(*((_B,_f),(_B,_P),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p)))
if mibBuilder.loadTexts:cfhPlaneGroup.setStatus(_A)
cfhBundleGroup=ObjectGroup((1,3,6,1,4,1,9,9,257,3,2,3))
cfhBundleGroup.setObjects(*((_B,_q),(_B,_r),(_B,_K),(_B,_L),(_B,_M),(_B,_s),(_B,_Q),(_B,_t),(_B,_u),(_B,_v),(_B,_w)))
if mibBuilder.loadTexts:cfhBundleGroup.setStatus(_A)
cfhBundlePortGroup=ObjectGroup((1,3,6,1,4,1,9,9,257,3,2,4))
cfhBundlePortGroup.setObjects(*((_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8)))
if mibBuilder.loadTexts:cfhBundlePortGroup.setStatus(_A)
cfhCardGroup=ObjectGroup((1,3,6,1,4,1,9,9,257,3,2,5))
cfhCardGroup.setObjects(*((_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD)))
if mibBuilder.loadTexts:cfhCardGroup.setStatus(_A)
cfhFabricCapacityGroup=ObjectGroup((1,3,6,1,4,1,9,9,257,3,2,7))
cfhFabricCapacityGroup.setObjects((_B,_AE))
if mibBuilder.loadTexts:cfhFabricCapacityGroup.setStatus(_A)
cfhPlaneStateNotification=NotificationType((1,3,6,1,4,1,9,9,257,0,1))
cfhPlaneStateNotification.setObjects((_B,_P))
if mibBuilder.loadTexts:cfhPlaneStateNotification.setStatus(_A)
cfhBundleStateNotification=NotificationType((1,3,6,1,4,1,9,9,257,0,2))
cfhBundleStateNotification.setObjects(*((_B,_M),(_B,_L),(_B,_K)))
if mibBuilder.loadTexts:cfhBundleStateNotification.setStatus(_A)
cfhBundleDownedLinkNotification=NotificationType((1,3,6,1,4,1,9,9,257,0,3))
cfhBundleDownedLinkNotification.setObjects(*((_B,_M),(_B,_L),(_B,_Q),(_B,_K)))
if mibBuilder.loadTexts:cfhBundleDownedLinkNotification.setStatus(_A)
cfhNotificationsGroup=NotificationGroup((1,3,6,1,4,1,9,9,257,3,2,6))
cfhNotificationsGroup.setObjects(*((_B,_AF),(_B,_AG),(_B,_AH)))
if mibBuilder.loadTexts:cfhNotificationsGroup.setStatus(_A)
cfhMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,257,3,1,1))
cfhMIBCompliance.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:cfhMIBCompliance.setStatus('deprecated')
cfhMIBCompliance1=ModuleCompliance((1,3,6,1,4,1,9,9,257,3,1,2))
cfhMIBCompliance1.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_AI)))
if mibBuilder.loadTexts:cfhMIBCompliance1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CfhPlane':CfhPlane,'CfhBundle':CfhBundle,'CfhAdminState':CfhAdminState,'CfhScaledPercentage':CfhScaledPercentage,'ciscoFabricHfrMIB':ciscoFabricHfrMIB,'cfhMIBNotifications':cfhMIBNotifications,_AF:cfhPlaneStateNotification,_AG:cfhBundleStateNotification,_AH:cfhBundleDownedLinkNotification,'ciscoFabricHfrMIBObjects':ciscoFabricHfrMIBObjects,'cfhGeneral':cfhGeneral,_c:cfhGenPlaneStateTrapEnable,_d:cfhGenBundleStateTrapEnable,_e:cfhGenBundleDownedLinkTrapEnable,'cfhPlane':cfhPlane,'cfhPlaneTable':cfhPlaneTable,'cfhPlaneEntry':cfhPlaneEntry,_N:cfhPlaneId,_f:cfhPlaneAdminStatus,_P:cfhPlaneOperStatus,_g:cfhPlaneTotalBundles,_h:cfhPlaneDownedBundles,'cfhPlaneStatsTable':cfhPlaneStatsTable,_a:cfhPlaneStatsEntry,_i:cfhPlaneStatsRxDataCells,_j:cfhPlaneStatsTxDataCells,_k:cfhPlaneStatsRxCECells,_l:cfhPlaneStatsRxUCECells,_m:cfhPlaneStatsRxPECells,_n:cfhPlaneStatsUnicastLostCells,_o:cfhPlaneStatsMulticastLostCells,_p:cfhPlaneStatsCounterDiscTime,_AE:cfhPlaneCapacityThreshold,'cfhBundle':cfhBundle,_q:cfhBundleTotal,_r:cfhBundleDowned,'cfhBundleTable':cfhBundleTable,'cfhBundleEntry':cfhBundleEntry,_Y:cfhBundleId,_K:cfhBundleName,_L:cfhBundlePlane,_M:cfhBundleOperStatus,_s:cfhBundleTotalLinks,_Q:cfhBundleDownedLinks,_t:cfhBundlePortLCRCardIndex,_u:cfhBundlePortLCRId,_v:cfhBundlePortSecondCardIndex,_w:cfhBundlePortSecondId,'cfhBundlePort':cfhBundlePort,_x:cfhBundlePortTotalNumber,'cfhBundlePortTable':cfhBundlePortTable,'cfhBundlePortEntry':cfhBundlePortEntry,_Z:cfhBundlePortId,_y:cfhBundlePortAdminState,_z:cfhBundlePortOperState,_A0:cfhBundlePortGrpId,'cfhBundlePortStatsTable':cfhBundlePortStatsTable,_b:cfhBundlePortStatsEntry,_A1:cfhBundlePortStatsRxDataCells,_A2:cfhBundlePortStatsTxDataCells,_A3:cfhBundlePortStatsRxCECells,_A4:cfhBundlePortStatsRxUCECells,_A5:cfhBundlePortStatsRxPECells,_A6:cfhBundlePortStatsHighRxCECells,_A7:cfhBundlePortStatsHighRxUCECells,_A8:cfhBundlePortStatsHighRxPECells,'cfhCard':cfhCard,'cfhCardTable':cfhCardTable,'cfhCardEntry':cfhCardEntry,_A9:cfhCardFabInUse,_AA:cfhCardFabUsage,_AB:cfhCardFabInUseDiscTime,'cfhCardPlaneTable':cfhCardPlaneTable,'cfhCardPlaneEntry':cfhCardPlaneEntry,_AC:cfhCardPlaneTxConnectivity,_AD:cfhCardPlaneRxConnectivity,'cfhMIBConformance':cfhMIBConformance,'cfhMIBCompliances':cfhMIBCompliances,'cfhMIBCompliance':cfhMIBCompliance,'cfhMIBCompliance1':cfhMIBCompliance1,'cfhMIBGroups':cfhMIBGroups,_R:cfhGenInfoGroup,_S:cfhPlaneGroup,_T:cfhBundleGroup,_U:cfhBundlePortGroup,_V:cfhCardGroup,_W:cfhNotificationsGroup,_AI:cfhFabricCapacityGroup})