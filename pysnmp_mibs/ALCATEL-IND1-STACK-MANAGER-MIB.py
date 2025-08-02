_AQ='alaStackSplitProtectionGroup'
_AP='alaSSPConfigInfo'
_AO='alaStackMgrMIBObjectsGroup'
_AN='alaStackMgrStaticRouteGroup'
_AM='alaStackMgrStatGroup'
_AL='alaStackMgrTrapGroup'
_AK='alaStackMgrStackModeGroup'
_AJ='alaStackMgrNotificationGroup'
_AI='alaStackMgrCfgMgrGroup'
_AH='alaStackSplitRecoveryTrap'
_AG='alaStackSplitProtectionTrap'
_AF='alaStackMgrIncompatibleLicenseTrap'
_AE='alaStackMgrBadMixTrap'
_AD='alaStackMgrOutOfPassThruSlotsTrap'
_AC='alaStackMgrOutOfTokensTrap'
_AB='alaStackMgrOutOfSlotsTrap'
_AA='alaStackMgrClearedSlotTrap'
_A9='alaStackMgrDuplicateRoleTrap'
_A8='alaStackMgrRoleChangeTrap'
_A7='alaStackMgrNeighborChangeTrap'
_A6='alaStackMgrDuplicateSlotTrap'
_A5='alaStackMgrPrimaryLicense'
_A4='alaSspHelperAggregateStatus'
_A3='alaSspHelperStatus'
_A2='alaStackMgrTokensUsed'
_A1='alaStackMgrTokensAvailable'
_A0='alaStackMgrStaticRouteRowStatus'
_z='alaStackMgrStaticRouteStatus'
_y='alaStackMgrStaticRoutePortState'
_x='alaStackMgrStaticRoutePort'
_w='alaStackMgrStatDelayFromLastMsg'
_v='alaStackMgrStatErrorsTx'
_u='alaStackMgrStatErrorsRx'
_t='alaStackMgrStatPktsTx'
_s='alaStackMgrStatPktsRx'
_r='alaStackMgrOperStackMode'
_q='alaStackMgrAdminStackMode'
_p='alaStackMgrAdminStackingMode'
_o='alaStackMgrOperStackingMode'
_n='alaStackMgrCommandStatus'
_m='alaStackMgrCommandAction'
_l='alaStackMgrSavedSlotNINumber'
_k='alaStackMgrChasState'
_j='alaStackMgrRemoteLinkB'
_i='alaStackMgrRemoteNISlotB'
_h='alaStackMgrLocalLinkStateB'
_g='alaStackMgrRemoteLinkA'
_f='alaStackMgrRemoteNISlotA'
_e='alaStackMgrLocalLinkStateA'
_d='alaStackMgrSlotCMMNumber'
_c='alaSSPTableSlotNINumber'
_b='alaStackMgrStackModeIndex'
_a='AlaStackMgrLinkNumber'
_Z='alaStackMgrStaticRouteDstEndIf'
_Y='alaStackMgrStaticRouteDstStartIf'
_X='alaStackMgrStaticRouteSrcEndIf'
_W='alaStackMgrStaticRouteSrcStartIf'
_V='reloadAny'
_U='standalone'
_T='2009-02-06 00:00'
_S='alaStackMgrTrapLinkNumber'
_R='alaStackMgrStackStatus'
_Q='alaStackMgrSecondary'
_P='alaStackMgrPrimary'
_O='alaStackMgrChasRole'
_N='alaSspHelperAggregateId'
_M='disable'
_L='enable'
_K='read-create'
_J='alaStackMgrStatLinkNumber'
_I='notSignificant'
_H='accessible-for-notify'
_G='not-accessible'
_F='read-write'
_E='alaStackMgrSlotNINumber'
_D='Integer32'
_C='read-only'
_B='ALCATEL-IND1-STACK-MANAGER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
softentIND1StackMgr,=mibBuilder.importSymbols('ALCATEL-IND1-BASE','softentIND1StackMgr')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
alcatelIND1StackMgrMIB=ModuleIdentity((1,3,6,1,4,1,6486,800,1,2,1,24,1))
if mibBuilder.loadTexts:alcatelIND1StackMgrMIB.setRevisions((_T,_T,'2007-04-03 00:00','2005-07-15 00:00','2004-07-01 00:00','2004-04-23 00:00','2004-04-08 00:00','2004-04-04 00:00','2004-03-22 00:00','2004-03-08 00:00','2001-08-27 00:00'))
class AlaStackMgrLinkNumber(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,11,12,25,26,27,28,29,30,31,32,51,52)));namedValues=NamedValues(*(('linkA',1),('linkB',2),('linkA11',11),('linkB12',12),('linkA25',25),('linkB26',26),('linkA27',27),('linkB28',28),('linkA29',29),('linkB30',30),('linkA31',31),('linkB32',32),('linkA51',51),('linkB52',52)))
class AlaStackMgrNINumber(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1008))
class AlaStackMgrLinkStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
class AlaStackMgrSlotRole(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('unassigned',0),('primary',1),('secondary',2),('idle',3),(_U,4),('passthrough',5)))
class AlaStackMgrStackStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('loop',1),('noloop',2)))
class AlaStackMgrSlotState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('running',1),('duplicateSlot',2),('clearedSlot',3),('outOfSlots',4),('outOfTokens',5),('badMix',6),('inc-Lic',7)))
class AlaStackMgrCommandAction(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_I,0),('clearSlot',1),('clearSlotImmediately',2),(_V,3),('reloadPassThru',4)))
class AlaStackMgrCommandStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_I,0),('clearSlotInProgress',1),('clearSlotFailed',2),('clearSlotSuccess',3),('setSlotInProgress',4),('setSlotFailed',5),('setSlotSuccess',6)))
class AlaStackMgrStackingMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('stackable',1),(_U,2)))
class AlaStackMgrStackMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('os6850',1),('os6850e',2)))
class AlaStackMgrLicenseType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),('metro',1)))
class AlaSSPTableSlotNINumber(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,8),ValueRangeConstraint(255,255),ValueRangeConstraint(1001,1008))
class AlaSSPTableSspOpStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('active',1),('protection',2),('notinstack',3)))
_AlcatelIND1StackMgrMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1StackMgrMIBObjects=_AlcatelIND1StackMgrMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,24,1,1))
_AlaStackMgrChassisTable_Object=MibTable
alaStackMgrChassisTable=_AlaStackMgrChassisTable_Object((1,3,6,1,4,1,6486,800,1,2,1,24,1,1,1))
if mibBuilder.loadTexts:alaStackMgrChassisTable.setStatus(_A)
_AlaStackMgrChassisEntry_Object=MibTableRow
alaStackMgrChassisEntry=_AlaStackMgrChassisEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,24,1,1,1,1))
alaStackMgrChassisEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:alaStackMgrChassisEntry.setStatus(_A)
_AlaStackMgrSlotNINumber_Type=AlaStackMgrNINumber
_AlaStackMgrSlotNINumber_Object=MibTableColumn
alaStackMgrSlotNINumber=_AlaStackMgrSlotNINumber_Object((1,3,6,1,4,1,6486,800,1,2,1,24,1,1,1,1,1),_AlaStackMgrSlotNINumber_Type())
alaStackMgrSlotNINumber.setMaxAccess(_C)
if mibBuilder.loadTexts:alaStackMgrSlotNINumber.setStatus(_A)
class _AlaStackMgrSlotCMMNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,72))
_AlaStackMgrSlotCMMNumber_Type.__name__=_D
_AlaStackMgrSlotCMMNumber_Object=MibTableColumn
alaStackMgrSlotCMMNumber=_AlaStackMgrSlotCMMNumber_Object((1,3,6,1,4,1,6486,800,1,2,1,24,1,1,1,1,2),_AlaStackMgrSlotCMMNumber_Type())
alaStackMgrSlotCMMNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:alaStackMgrSlotCMMNumber.setStatus(_A)
_AlaStackMgrChasRole_Type=AlaStackMgrSlotRole
_AlaStackMgrChasRole_Object=MibTableColumn
alaStackMgrChasRole=_AlaStackMgrChasRole_Object((1,3,6,1,4,1,6486,800,1,2,1,24,1,1,1,1,3),_AlaStackMgrChasRole_Type())
alaStackMgrChasRole.setMaxAccess(_C)
if mibBuilder.loadTexts:alaStackMgrChasRole.setStatus(_A)
_AlaStackMgrLocalLinkStateA_Type=AlaStackMgrLinkStatus
_AlaStackMgrLocalLinkStateA_Object=MibTableColumn
alaStackMgrLocalLinkStateA=_AlaStackMgrLocalLinkStateA_Object((1,3,6,1,4,1,6486,800,1,2,1,24,1,1,1,1,4),_AlaStackMgrLocalLinkStateA_Type())
alaStackMgrLocalLinkStateA.setMaxAccess(_C)
if mibBuilder.loadTexts:alaStackMgrLocalLinkStateA.setStatus(_A)
_AlaStackMgrRemoteNISlotA_Type=AlaStackMgrNINumber
_AlaStackMgrRemoteNISlotA_Object=MibTableColumn
alaStackMgrRemoteNISlotA=_AlaStackMgrRemoteNISlotA_Object((1,3,6,1,4,1,6486,800,1,2,1,24,1,1,1,1,5),_AlaStackMgrRemoteNISlotA_Type())
alaStackMgrRemoteNISlotA.setMaxAccess(_C)
if mibBuilder.loadTexts:alaStackMgrRemoteNISlotA.setStatus(_A)
_AlaStackMgrRemoteLinkA_Type=AlaStackMgrLinkNumber
_AlaStackMgrRemoteLinkA_Object=MibTableColumn
alaStackMgrRemoteLinkA=_AlaStackMgrRemoteLinkA_Object((1,3,6,1,4,1,6486,800,1,2,1,24,1,1,1,1,6),_AlaStackMgrRemoteLinkA_Type())
alaStackMgrRemoteLinkA.setMaxAccess(_C)
if mibBuilder.loadTexts:alaStackMgrRemoteLinkA.setStatus(_A)
_AlaStackMgrLocalLinkStateB_Type=AlaStackMgrLinkStatus
_AlaStackMgrLocalLinkStateB_Object=MibTableColumn
alaStackMgrLocalLinkStateB=_AlaStackMgrLocalLinkStateB_Object((1,3,6,1,4,1,6486,800,1,2,1,24,1,1,1,1,7),_AlaStackMgrLocalLinkStateB_Type())
alaStackMgrLocalLinkStateB.setMaxAccess(_C)
if mibBuilder.loadTexts:alaStackMgrLocalLinkStateB.setStatus(_A)
_AlaStackMgrRemoteNISlotB_Type=AlaStackMgrNINumber
_AlaStackMgrRemoteNISlotB_Object=MibTableColumn
alaStackMgrRemoteNISlotB=_AlaStackMgrRemoteNISlotB_Object((1,3,6,1,4,1,6486,800,1,2,1,24,1,1,1,1,8),_AlaStackMgrRemoteNISlotB_Type())
alaStackMgrRemoteNISlotB.setMaxAccess(_C)
if mibBuilder.loadTexts:alaStackMgrRemoteNISlotB.setStatus(_A)
_AlaStackMgrRemoteLinkB_Type=AlaStackMgrLinkNumber
_AlaStackMgrRemoteLinkB_Object=MibTableColumn
alaStackMgrRemoteLinkB=_AlaStackMgrRemoteLinkB_Object((1,3,6,1,4,1,6486,800,1,2,1,24,1,1,1,1,9),_AlaStackMgrRemoteLinkB_Type())
alaStackMgrRemoteLinkB.setMaxAccess(_C)
if mibBuilder.loadTexts:alaStackMgrRemoteLinkB.setStatus(_A)
_AlaStackMgrChasState_Type=AlaStackMgrSlotState
_AlaStackMgrChasState_Object=MibTableColumn
alaStackMgrChasState=_AlaStackMgrChasState_Object((1,3,6,1,4,1,6486,800,1,2,1,24,1,1,1,1,10),_AlaStackMgrChasState_Type())
alaStackMgrChasState.setMaxAccess(_C)
if mibBuilder.loadTexts:alaStackMgrChasState.setStatus(_A)
_AlaStackMgrSavedSlotNINumber_Type=AlaStackMgrNINumber
_AlaStackMgrSavedSlotNINumber_Object=MibTableColumn
alaStackMgrSavedSlotNINumber=_AlaStackMgrSavedSlotNINumber_Object((1,3,6,1,4,1,6486,800,1,2,1,24,1,1,1,1,11),_AlaStackMgrSavedSlotNINumber_Type())
alaStackMgrSavedSlotNINumber.setMaxAccess(_F)
if mibBuilder.loadTexts:alaStackMgrSavedSlotNINumber.setStatus(_A)
_AlaStackMgrCommandAction_Type=AlaStackMgrCommandAction
_AlaStackMgrCommandAction_Object=MibTableColumn
alaStackMgrCommandAction=_AlaStackMgrCommandAction_Object((1,3,6,1,4,1,6486,800,1,2,1,24,1,1,1,1,12),_AlaStackMgrCommandAction_Type())
alaStackMgrCommandAction.setMaxAccess(_F)
if mibBuilder.loadTexts:alaStackMgrCommandAction.setStatus(_A)
_AlaStackMgrCommandStatus_Type=AlaStackMgrCommandStatus
_AlaStackMgrCommandStatus_Object=MibTableColumn
alaStackMgrCommandStatus=_AlaStackMgrCommandStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,24,1,1,1,1,13),_AlaStackMgrCommandStatus_Type())
alaStackMgrCommandStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:alaStackMgrCommandStatus.setStatus(_A)
_AlaStackMgrOperStackingMode_Type=AlaStackMgrStackingMode
_AlaStackMgrOperStackingMode_Object=MibTableColumn
alaStackMgrOperStackingMode=_AlaStackMgrOperStackingMode_Object((1,3,6,1,4,1,6486,800,1,2,1,24,1,1,1,1,14),_AlaStackMgrOperStackingMode_Type())
alaStackMgrOperStackingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:alaStackMgrOperStackingMode.setStatus(_A)
_AlaStackMgrAdminStackingMode_Type=AlaStackMgrStackingMode
_AlaStackMgrAdminStackingMode_Object=MibTableColumn
alaStackMgrAdminStackingMode=_AlaStackMgrAdminStackingMode_Object((1,3,6,1,4,1,6486,800,1,2,1,24,1,1,1,1,15),_AlaStackMgrAdminStackingMode_Type())
alaStackMgrAdminStackingMode.setMaxAccess(_F)
if mibBuilder.loadTexts:alaStackMgrAdminStackingMode.setStatus(_A)
_AlaStackMgrStatsTable_Object=MibTable
alaStackMgrStatsTable=_AlaStackMgrStatsTable_Object((1,3,6,1,4,1,6486,800,1,2,1,24,1,1,2))
if mibBuilder.loadTexts:alaStackMgrStatsTable.setStatus(_A)
_AlaStackMgrStatsEntry_Object=MibTableRow
alaStackMgrStatsEntry=_AlaStackMgrStatsEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,24,1,1,2,1))
alaStackMgrStatsEntry.setIndexNames((0,_B,_E),(0,_B,_J))
if mibBuilder.loadTexts:alaStackMgrStatsEntry.setStatus(_A)
_AlaStackMgrStatLinkNumber_Type=AlaStackMgrLinkNumber
_AlaStackMgrStatLinkNumber_Object=MibTableColumn
alaStackMgrStatLinkNumber=_AlaStackMgrStatLinkNumber_Object((1,3,6,1,4,1,6486,800,1,2,1,24,1,1,2,1,1),_AlaStackMgrStatLinkNumber_Type())
alaStackMgrStatLinkNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:alaStackMgrStatLinkNumber.setStatus(_A)
_AlaStackMgrStatPktsRx_Type=Counter32
_AlaStackMgrStatPktsRx_Object=MibTableColumn
alaStackMgrStatPktsRx=_AlaStackMgrStatPktsRx_Object((1,3,6,1,4,1,6486,800,1,2,1,24,1,1,2,1,2),_AlaStackMgrStatPktsRx_Type())
alaStackMgrStatPktsRx.setMaxAccess(_C)
if mibBuilder.loadTexts:alaStackMgrStatPktsRx.setStatus(_A)
_AlaStackMgrStatPktsTx_Type=Counter32
_AlaStackMgrStatPktsTx_Object=MibTableColumn
alaStackMgrStatPktsTx=_AlaStackMgrStatPktsTx_Object((1,3,6,1,4,1,6486,800,1,2,1,24,1,1,2,1,3),_AlaStackMgrStatPktsTx_Type())
alaStackMgrStatPktsTx.setMaxAccess(_C)
if mibBuilder.loadTexts:alaStackMgrStatPktsTx.setStatus(_A)
_AlaStackMgrStatErrorsRx_Type=Counter32
_AlaStackMgrStatErrorsRx_Object=MibTableColumn
alaStackMgrStatErrorsRx=_AlaStackMgrStatErrorsRx_Object((1,3,6,1,4,1,6486,800,1,2,1,24,1,1,2,1,4),_AlaStackMgrStatErrorsRx_Type())
alaStackMgrStatErrorsRx.setMaxAccess(_C)
if mibBuilder.loadTexts:alaStackMgrStatErrorsRx.setStatus(_A)
_AlaStackMgrStatErrorsTx_Type=Counter32
_AlaStackMgrStatErrorsTx_Object=MibTableColumn
alaStackMgrStatErrorsTx=_AlaStackMgrStatErrorsTx_Object((1,3,6,1,4,1,6486,800,1,2,1,24,1,1,2,1,5),_AlaStackMgrStatErrorsTx_Type())
alaStackMgrStatErrorsTx.setMaxAccess(_C)
if mibBuilder.loadTexts:alaStackMgrStatErrorsTx.setStatus(_A)
class _AlaStackMgrStatDelayFromLastMsg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AlaStackMgrStatDelayFromLastMsg_Type.__name__=_D
_AlaStackMgrStatDelayFromLastMsg_Object=MibTableColumn
alaStackMgrStatDelayFromLastMsg=_AlaStackMgrStatDelayFromLastMsg_Object((1,3,6,1,4,1,6486,800,1,2,1,24,1,1,2,1,6),_AlaStackMgrStatDelayFromLastMsg_Type())
alaStackMgrStatDelayFromLastMsg.setMaxAccess(_C)
if mibBuilder.loadTexts:alaStackMgrStatDelayFromLastMsg.setStatus(_A)
_AlaStackMgrStackStatus_Type=AlaStackMgrStackStatus
_AlaStackMgrStackStatus_Object=MibScalar
alaStackMgrStackStatus=_AlaStackMgrStackStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,24,1,1,3),_AlaStackMgrStackStatus_Type())
alaStackMgrStackStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:alaStackMgrStackStatus.setStatus(_A)
class _AlaStackMgrTokensUsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AlaStackMgrTokensUsed_Type.__name__=_D
_AlaStackMgrTokensUsed_Object=MibScalar
alaStackMgrTokensUsed=_AlaStackMgrTokensUsed_Object((1,3,6,1,4,1,6486,800,1,2,1,24,1,1,4),_AlaStackMgrTokensUsed_Type())
alaStackMgrTokensUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:alaStackMgrTokensUsed.setStatus(_A)
class _AlaStackMgrTokensAvailable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AlaStackMgrTokensAvailable_Type.__name__=_D
_AlaStackMgrTokensAvailable_Object=MibScalar
alaStackMgrTokensAvailable=_AlaStackMgrTokensAvailable_Object((1,3,6,1,4,1,6486,800,1,2,1,24,1,1,5),_AlaStackMgrTokensAvailable_Type())
alaStackMgrTokensAvailable.setMaxAccess(_C)
if mibBuilder.loadTexts:alaStackMgrTokensAvailable.setStatus(_A)
_AlaStackMgrStaticRouteTable_Object=MibTable
alaStackMgrStaticRouteTable=_AlaStackMgrStaticRouteTable_Object((1,3,6,1,4,1,6486,800,1,2,1,24,1,1,6))
if mibBuilder.loadTexts:alaStackMgrStaticRouteTable.setStatus(_A)
_AlaStackMgrStaticRouteEntry_Object=MibTableRow
alaStackMgrStaticRouteEntry=_AlaStackMgrStaticRouteEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,24,1,1,6,1))
alaStackMgrStaticRouteEntry.setIndexNames((0,_B,_W),(0,_B,_X),(0,_B,_Y),(0,_B,_Z))
if mibBuilder.loadTexts:alaStackMgrStaticRouteEntry.setStatus(_A)
_AlaStackMgrStaticRouteSrcStartIf_Type=InterfaceIndex
_AlaStackMgrStaticRouteSrcStartIf_Object=MibTableColumn
alaStackMgrStaticRouteSrcStartIf=_AlaStackMgrStaticRouteSrcStartIf_Object((1,3,6,1,4,1,6486,800,1,2,1,24,1,1,6,1,1),_AlaStackMgrStaticRouteSrcStartIf_Type())
alaStackMgrStaticRouteSrcStartIf.setMaxAccess(_G)
if mibBuilder.loadTexts:alaStackMgrStaticRouteSrcStartIf.setStatus(_A)
_AlaStackMgrStaticRouteSrcEndIf_Type=InterfaceIndex
_AlaStackMgrStaticRouteSrcEndIf_Object=MibTableColumn
alaStackMgrStaticRouteSrcEndIf=_AlaStackMgrStaticRouteSrcEndIf_Object((1,3,6,1,4,1,6486,800,1,2,1,24,1,1,6,1,2),_AlaStackMgrStaticRouteSrcEndIf_Type())
alaStackMgrStaticRouteSrcEndIf.setMaxAccess(_G)
if mibBuilder.loadTexts:alaStackMgrStaticRouteSrcEndIf.setStatus(_A)
_AlaStackMgrStaticRouteDstStartIf_Type=InterfaceIndex
_AlaStackMgrStaticRouteDstStartIf_Object=MibTableColumn
alaStackMgrStaticRouteDstStartIf=_AlaStackMgrStaticRouteDstStartIf_Object((1,3,6,1,4,1,6486,800,1,2,1,24,1,1,6,1,3),_AlaStackMgrStaticRouteDstStartIf_Type())
alaStackMgrStaticRouteDstStartIf.setMaxAccess(_G)
if mibBuilder.loadTexts:alaStackMgrStaticRouteDstStartIf.setStatus(_A)
_AlaStackMgrStaticRouteDstEndIf_Type=InterfaceIndex
_AlaStackMgrStaticRouteDstEndIf_Object=MibTableColumn
alaStackMgrStaticRouteDstEndIf=_AlaStackMgrStaticRouteDstEndIf_Object((1,3,6,1,4,1,6486,800,1,2,1,24,1,1,6,1,4),_AlaStackMgrStaticRouteDstEndIf_Type())
alaStackMgrStaticRouteDstEndIf.setMaxAccess(_G)
if mibBuilder.loadTexts:alaStackMgrStaticRouteDstEndIf.setStatus(_A)
class _AlaStackMgrStaticRoutePort_Type(AlaStackMgrLinkNumber):defaultValue=1
_AlaStackMgrStaticRoutePort_Type.__name__=_a
_AlaStackMgrStaticRoutePort_Object=MibTableColumn
alaStackMgrStaticRoutePort=_AlaStackMgrStaticRoutePort_Object((1,3,6,1,4,1,6486,800,1,2,1,24,1,1,6,1,5),_AlaStackMgrStaticRoutePort_Type())
alaStackMgrStaticRoutePort.setMaxAccess(_K)
if mibBuilder.loadTexts:alaStackMgrStaticRoutePort.setStatus(_A)
_AlaStackMgrStaticRoutePortState_Type=AlaStackMgrLinkStatus
_AlaStackMgrStaticRoutePortState_Object=MibTableColumn
alaStackMgrStaticRoutePortState=_AlaStackMgrStaticRoutePortState_Object((1,3,6,1,4,1,6486,800,1,2,1,24,1,1,6,1,6),_AlaStackMgrStaticRoutePortState_Type())
alaStackMgrStaticRoutePortState.setMaxAccess(_C)
if mibBuilder.loadTexts:alaStackMgrStaticRoutePortState.setStatus(_A)
class _AlaStackMgrStaticRouteStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_AlaStackMgrStaticRouteStatus_Type.__name__=_D
_AlaStackMgrStaticRouteStatus_Object=MibTableColumn
alaStackMgrStaticRouteStatus=_AlaStackMgrStaticRouteStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,24,1,1,6,1,7),_AlaStackMgrStaticRouteStatus_Type())
alaStackMgrStaticRouteStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:alaStackMgrStaticRouteStatus.setStatus(_A)
_AlaStackMgrStaticRouteRowStatus_Type=RowStatus
_AlaStackMgrStaticRouteRowStatus_Object=MibTableColumn
alaStackMgrStaticRouteRowStatus=_AlaStackMgrStaticRouteRowStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,24,1,1,6,1,8),_AlaStackMgrStaticRouteRowStatus_Type())
alaStackMgrStaticRouteRowStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:alaStackMgrStaticRouteRowStatus.setStatus(_A)
_AlaStackMgrStackModeTable_Object=MibTable
alaStackMgrStackModeTable=_AlaStackMgrStackModeTable_Object((1,3,6,1,4,1,6486,800,1,2,1,24,1,1,7))
if mibBuilder.loadTexts:alaStackMgrStackModeTable.setStatus(_A)
_AlaStackMgrStackModeEntry_Object=MibTableRow
alaStackMgrStackModeEntry=_AlaStackMgrStackModeEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,24,1,1,7,1))
alaStackMgrStackModeEntry.setIndexNames((0,_B,_b))
if mibBuilder.loadTexts:alaStackMgrStackModeEntry.setStatus(_A)
_AlaStackMgrStackModeIndex_Type=AlaStackMgrNINumber
_AlaStackMgrStackModeIndex_Object=MibTableColumn
alaStackMgrStackModeIndex=_AlaStackMgrStackModeIndex_Object((1,3,6,1,4,1,6486,800,1,2,1,24,1,1,7,1,1),_AlaStackMgrStackModeIndex_Type())
alaStackMgrStackModeIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:alaStackMgrStackModeIndex.setStatus(_A)
_AlaStackMgrAdminStackMode_Type=AlaStackMgrStackMode
_AlaStackMgrAdminStackMode_Object=MibTableColumn
alaStackMgrAdminStackMode=_AlaStackMgrAdminStackMode_Object((1,3,6,1,4,1,6486,800,1,2,1,24,1,1,7,1,2),_AlaStackMgrAdminStackMode_Type())
alaStackMgrAdminStackMode.setMaxAccess(_F)
if mibBuilder.loadTexts:alaStackMgrAdminStackMode.setStatus(_A)
_AlaStackMgrOperStackMode_Type=AlaStackMgrStackMode
_AlaStackMgrOperStackMode_Object=MibTableColumn
alaStackMgrOperStackMode=_AlaStackMgrOperStackMode_Object((1,3,6,1,4,1,6486,800,1,2,1,24,1,1,7,1,3),_AlaStackMgrOperStackMode_Type())
alaStackMgrOperStackMode.setMaxAccess(_C)
if mibBuilder.loadTexts:alaStackMgrOperStackMode.setStatus(_A)
class _AlaStackMgrCmdAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(3));namedValues=NamedValues((_V,3))
_AlaStackMgrCmdAction_Type.__name__=_D
_AlaStackMgrCmdAction_Object=MibTableColumn
alaStackMgrCmdAction=_AlaStackMgrCmdAction_Object((1,3,6,1,4,1,6486,800,1,2,1,24,1,1,7,1,4),_AlaStackMgrCmdAction_Type())
alaStackMgrCmdAction.setMaxAccess(_F)
if mibBuilder.loadTexts:alaStackMgrCmdAction.setStatus(_A)
_AlaSSPStateTable_Object=MibTable
alaSSPStateTable=_AlaSSPStateTable_Object((1,3,6,1,4,1,6486,800,1,2,1,24,1,1,8))
if mibBuilder.loadTexts:alaSSPStateTable.setStatus(_A)
_AlaSSPStateEntry_Object=MibTableRow
alaSSPStateEntry=_AlaSSPStateEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,24,1,1,8,1))
alaSSPStateEntry.setIndexNames((0,_B,_c))
if mibBuilder.loadTexts:alaSSPStateEntry.setStatus(_A)
_AlaSSPTableSlotNINumber_Type=AlaSSPTableSlotNINumber
_AlaSSPTableSlotNINumber_Object=MibTableColumn
alaSSPTableSlotNINumber=_AlaSSPTableSlotNINumber_Object((1,3,6,1,4,1,6486,800,1,2,1,24,1,1,8,1,1),_AlaSSPTableSlotNINumber_Type())
alaSSPTableSlotNINumber.setMaxAccess(_C)
if mibBuilder.loadTexts:alaSSPTableSlotNINumber.setStatus(_A)
_AlaSSPTableSspOpStatus_Type=AlaSSPTableSspOpStatus
_AlaSSPTableSspOpStatus_Object=MibTableColumn
alaSSPTableSspOpStatus=_AlaSSPTableSspOpStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,24,1,1,8,1,2),_AlaSSPTableSspOpStatus_Type())
alaSSPTableSspOpStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:alaSSPTableSspOpStatus.setStatus(_A)
_AlaSSPHelperGlobalConfig_ObjectIdentity=ObjectIdentity
alaSSPHelperGlobalConfig=_AlaSSPHelperGlobalConfig_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,24,1,1,9))
class _AlaSspHelperStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_AlaSspHelperStatus_Type.__name__=_D
_AlaSspHelperStatus_Object=MibScalar
alaSspHelperStatus=_AlaSspHelperStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,24,1,1,9,1),_AlaSspHelperStatus_Type())
alaSspHelperStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:alaSspHelperStatus.setStatus(_A)
_AlaSspHelperqAggregateTable_Object=MibTable
alaSspHelperqAggregateTable=_AlaSspHelperqAggregateTable_Object((1,3,6,1,4,1,6486,800,1,2,1,24,1,1,10))
if mibBuilder.loadTexts:alaSspHelperqAggregateTable.setStatus(_A)
_AlaSspHelperqAggregateEntry_Object=MibTableRow
alaSspHelperqAggregateEntry=_AlaSspHelperqAggregateEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,24,1,1,10,1))
alaSspHelperqAggregateEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:alaSspHelperqAggregateEntry.setStatus(_A)
class _AlaSspHelperAggregateId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_AlaSspHelperAggregateId_Type.__name__=_D
_AlaSspHelperAggregateId_Object=MibTableColumn
alaSspHelperAggregateId=_AlaSspHelperAggregateId_Object((1,3,6,1,4,1,6486,800,1,2,1,24,1,1,10,1,1),_AlaSspHelperAggregateId_Type())
alaSspHelperAggregateId.setMaxAccess(_C)
if mibBuilder.loadTexts:alaSspHelperAggregateId.setStatus(_A)
class _AlaSspHelperAggregateStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_AlaSspHelperAggregateStatus_Type.__name__=_D
_AlaSspHelperAggregateStatus_Object=MibTableColumn
alaSspHelperAggregateStatus=_AlaSspHelperAggregateStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,24,1,1,10,1,2),_AlaSspHelperAggregateStatus_Type())
alaSspHelperAggregateStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:alaSspHelperAggregateStatus.setStatus(_A)
_AlcatelIND1StackMgrMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1StackMgrMIBConformance=_AlcatelIND1StackMgrMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,24,1,2))
_AlcatelIND1StackMgrMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1StackMgrMIBGroups=_AlcatelIND1StackMgrMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,24,1,2,1))
_AlaSSPConfigInfo_ObjectIdentity=ObjectIdentity
alaSSPConfigInfo=_AlaSSPConfigInfo_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,24,1,2,1,8))
class _AlaSspConfigStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_AlaSspConfigStatus_Type.__name__=_D
_AlaSspConfigStatus_Object=MibScalar
alaSspConfigStatus=_AlaSspConfigStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,24,1,2,1,8,1),_AlaSspConfigStatus_Type())
alaSspConfigStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:alaSspConfigStatus.setStatus(_A)
class _AlaSspLinkaggId_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,31))
_AlaSspLinkaggId_Type.__name__=_D
_AlaSspLinkaggId_Object=MibScalar
alaSspLinkaggId=_AlaSspLinkaggId_Object((1,3,6,1,4,1,6486,800,1,2,1,24,1,2,1,8,2),_AlaSspLinkaggId_Type())
alaSspLinkaggId.setMaxAccess(_F)
if mibBuilder.loadTexts:alaSspLinkaggId.setStatus(_A)
class _AlaSspGuardTimer_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,100))
_AlaSspGuardTimer_Type.__name__=_D
_AlaSspGuardTimer_Object=MibScalar
alaSspGuardTimer=_AlaSspGuardTimer_Object((1,3,6,1,4,1,6486,800,1,2,1,24,1,2,1,8,3),_AlaSspGuardTimer_Type())
alaSspGuardTimer.setMaxAccess(_F)
if mibBuilder.loadTexts:alaSspGuardTimer.setStatus(_A)
_AlaSspUpTime_Type=TimeTicks
_AlaSspUpTime_Object=MibScalar
alaSspUpTime=_AlaSspUpTime_Object((1,3,6,1,4,1,6486,800,1,2,1,24,1,2,1,8,4),_AlaSspUpTime_Type())
alaSspUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:alaSspUpTime.setStatus(_A)
_AlaSspStateUpTime_Type=TimeTicks
_AlaSspStateUpTime_Object=MibScalar
alaSspStateUpTime=_AlaSspStateUpTime_Object((1,3,6,1,4,1,6486,800,1,2,1,24,1,2,1,8,5),_AlaSspStateUpTime_Type())
alaSspStateUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:alaSspStateUpTime.setStatus(_A)
_AlcatelIND1StackMgrMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1StackMgrMIBCompliances=_AlcatelIND1StackMgrMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,24,1,2,2))
_AlcatelIND1StackMgrTrapObjects_ObjectIdentity=ObjectIdentity
alcatelIND1StackMgrTrapObjects=_AlcatelIND1StackMgrTrapObjects_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,24,1,3))
_AlaStackMgrTrapLinkNumber_Type=AlaStackMgrLinkNumber
_AlaStackMgrTrapLinkNumber_Object=MibScalar
alaStackMgrTrapLinkNumber=_AlaStackMgrTrapLinkNumber_Object((1,3,6,1,4,1,6486,800,1,2,1,24,1,3,1),_AlaStackMgrTrapLinkNumber_Type())
alaStackMgrTrapLinkNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:alaStackMgrTrapLinkNumber.setStatus(_A)
_AlaStackMgrPrimary_Type=AlaStackMgrNINumber
_AlaStackMgrPrimary_Object=MibScalar
alaStackMgrPrimary=_AlaStackMgrPrimary_Object((1,3,6,1,4,1,6486,800,1,2,1,24,1,3,2),_AlaStackMgrPrimary_Type())
alaStackMgrPrimary.setMaxAccess(_H)
if mibBuilder.loadTexts:alaStackMgrPrimary.setStatus(_A)
_AlaStackMgrSecondary_Type=AlaStackMgrNINumber
_AlaStackMgrSecondary_Object=MibScalar
alaStackMgrSecondary=_AlaStackMgrSecondary_Object((1,3,6,1,4,1,6486,800,1,2,1,24,1,3,3),_AlaStackMgrSecondary_Type())
alaStackMgrSecondary.setMaxAccess(_H)
if mibBuilder.loadTexts:alaStackMgrSecondary.setStatus(_A)
_AlaStackMgrPrimaryLicense_Type=AlaStackMgrLicenseType
_AlaStackMgrPrimaryLicense_Object=MibScalar
alaStackMgrPrimaryLicense=_AlaStackMgrPrimaryLicense_Object((1,3,6,1,4,1,6486,800,1,2,1,24,1,3,4),_AlaStackMgrPrimaryLicense_Type())
alaStackMgrPrimaryLicense.setMaxAccess(_H)
if mibBuilder.loadTexts:alaStackMgrPrimaryLicense.setStatus(_A)
_AlaStackMgrTraps_ObjectIdentity=ObjectIdentity
alaStackMgrTraps=_AlaStackMgrTraps_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,24,1,4))
alaStackMgrCfgMgrGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,24,1,2,1,1))
alaStackMgrCfgMgrGroup.setObjects(*((_B,_E),(_B,_d),(_B,_O),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p)))
if mibBuilder.loadTexts:alaStackMgrCfgMgrGroup.setStatus(_A)
alaStackMgrStackModeGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,24,1,2,1,3))
alaStackMgrStackModeGroup.setObjects(*((_B,_q),(_B,_r)))
if mibBuilder.loadTexts:alaStackMgrStackModeGroup.setStatus(_A)
alaStackMgrTrapGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,24,1,2,1,4))
alaStackMgrTrapGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:alaStackMgrTrapGroup.setStatus(_A)
alaStackMgrStatGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,24,1,2,1,5))
alaStackMgrStatGroup.setObjects(*((_B,_J),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w)))
if mibBuilder.loadTexts:alaStackMgrStatGroup.setStatus(_A)
alaStackMgrStaticRouteGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,24,1,2,1,6))
alaStackMgrStaticRouteGroup.setObjects(*((_B,_x),(_B,_y),(_B,_z),(_B,_A0)))
if mibBuilder.loadTexts:alaStackMgrStaticRouteGroup.setStatus(_A)
alaStackMgrMIBObjectsGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,24,1,2,1,7))
alaStackMgrMIBObjectsGroup.setObjects(*((_B,_A1),(_B,_A2)))
if mibBuilder.loadTexts:alaStackMgrMIBObjectsGroup.setStatus(_A)
alaStackSplitProtectionGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,24,1,2,1,9))
alaStackSplitProtectionGroup.setObjects(*((_B,_A3),(_B,_N),(_B,_A4)))
if mibBuilder.loadTexts:alaStackSplitProtectionGroup.setStatus(_A)
alaStackMgrDuplicateSlotTrap=NotificationType((1,3,6,1,4,1,6486,800,1,2,1,24,1,4,0,1))
alaStackMgrDuplicateSlotTrap.setObjects((_B,_E))
if mibBuilder.loadTexts:alaStackMgrDuplicateSlotTrap.setStatus(_A)
alaStackMgrNeighborChangeTrap=NotificationType((1,3,6,1,4,1,6486,800,1,2,1,24,1,4,0,2))
alaStackMgrNeighborChangeTrap.setObjects(*((_B,_R),(_B,_E),(_B,_S)))
if mibBuilder.loadTexts:alaStackMgrNeighborChangeTrap.setStatus(_A)
alaStackMgrRoleChangeTrap=NotificationType((1,3,6,1,4,1,6486,800,1,2,1,24,1,4,0,3))
alaStackMgrRoleChangeTrap.setObjects(*((_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:alaStackMgrRoleChangeTrap.setStatus(_A)
alaStackMgrDuplicateRoleTrap=NotificationType((1,3,6,1,4,1,6486,800,1,2,1,24,1,4,0,4))
alaStackMgrDuplicateRoleTrap.setObjects(*((_B,_E),(_B,_O)))
if mibBuilder.loadTexts:alaStackMgrDuplicateRoleTrap.setStatus(_A)
alaStackMgrClearedSlotTrap=NotificationType((1,3,6,1,4,1,6486,800,1,2,1,24,1,4,0,5))
alaStackMgrClearedSlotTrap.setObjects((_B,_E))
if mibBuilder.loadTexts:alaStackMgrClearedSlotTrap.setStatus(_A)
alaStackMgrOutOfSlotsTrap=NotificationType((1,3,6,1,4,1,6486,800,1,2,1,24,1,4,0,6))
if mibBuilder.loadTexts:alaStackMgrOutOfSlotsTrap.setStatus(_A)
alaStackMgrOutOfTokensTrap=NotificationType((1,3,6,1,4,1,6486,800,1,2,1,24,1,4,0,7))
alaStackMgrOutOfTokensTrap.setObjects((_B,_E))
if mibBuilder.loadTexts:alaStackMgrOutOfTokensTrap.setStatus(_A)
alaStackMgrOutOfPassThruSlotsTrap=NotificationType((1,3,6,1,4,1,6486,800,1,2,1,24,1,4,0,8))
if mibBuilder.loadTexts:alaStackMgrOutOfPassThruSlotsTrap.setStatus(_A)
alaStackMgrBadMixTrap=NotificationType((1,3,6,1,4,1,6486,800,1,2,1,24,1,4,0,9))
alaStackMgrBadMixTrap.setObjects((_B,_E))
if mibBuilder.loadTexts:alaStackMgrBadMixTrap.setStatus(_A)
alaStackMgrIncompatibleLicenseTrap=NotificationType((1,3,6,1,4,1,6486,800,1,2,1,24,1,4,0,10))
alaStackMgrIncompatibleLicenseTrap.setObjects(*((_B,_E),(_B,_A5)))
if mibBuilder.loadTexts:alaStackMgrIncompatibleLicenseTrap.setStatus(_A)
alaStackSplitProtectionTrap=NotificationType((1,3,6,1,4,1,6486,800,1,2,1,24,1,4,0,11))
alaStackSplitProtectionTrap.setObjects((_B,_E))
if mibBuilder.loadTexts:alaStackSplitProtectionTrap.setStatus(_A)
alaStackSplitRecoveryTrap=NotificationType((1,3,6,1,4,1,6486,800,1,2,1,24,1,4,0,12))
alaStackSplitRecoveryTrap.setObjects((_B,_E))
if mibBuilder.loadTexts:alaStackSplitRecoveryTrap.setStatus(_A)
alaStackMgrNotificationGroup=NotificationGroup((1,3,6,1,4,1,6486,800,1,2,1,24,1,2,1,2))
alaStackMgrNotificationGroup.setObjects(*((_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH)))
if mibBuilder.loadTexts:alaStackMgrNotificationGroup.setStatus(_A)
alcatelIND1StackMgrMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6486,800,1,2,1,24,1,2,2,1))
alcatelIND1StackMgrMIBCompliance.setObjects(*((_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ)))
if mibBuilder.loadTexts:alcatelIND1StackMgrMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_a:AlaStackMgrLinkNumber,'AlaStackMgrNINumber':AlaStackMgrNINumber,'AlaStackMgrLinkStatus':AlaStackMgrLinkStatus,'AlaStackMgrSlotRole':AlaStackMgrSlotRole,'AlaStackMgrStackStatus':AlaStackMgrStackStatus,'AlaStackMgrSlotState':AlaStackMgrSlotState,'AlaStackMgrCommandAction':AlaStackMgrCommandAction,'AlaStackMgrCommandStatus':AlaStackMgrCommandStatus,'AlaStackMgrStackingMode':AlaStackMgrStackingMode,'AlaStackMgrStackMode':AlaStackMgrStackMode,'AlaStackMgrLicenseType':AlaStackMgrLicenseType,'AlaSSPTableSlotNINumber':AlaSSPTableSlotNINumber,'AlaSSPTableSspOpStatus':AlaSSPTableSspOpStatus,'alcatelIND1StackMgrMIB':alcatelIND1StackMgrMIB,'alcatelIND1StackMgrMIBObjects':alcatelIND1StackMgrMIBObjects,'alaStackMgrChassisTable':alaStackMgrChassisTable,'alaStackMgrChassisEntry':alaStackMgrChassisEntry,_E:alaStackMgrSlotNINumber,_d:alaStackMgrSlotCMMNumber,_O:alaStackMgrChasRole,_e:alaStackMgrLocalLinkStateA,_f:alaStackMgrRemoteNISlotA,_g:alaStackMgrRemoteLinkA,_h:alaStackMgrLocalLinkStateB,_i:alaStackMgrRemoteNISlotB,_j:alaStackMgrRemoteLinkB,_k:alaStackMgrChasState,_l:alaStackMgrSavedSlotNINumber,_m:alaStackMgrCommandAction,_n:alaStackMgrCommandStatus,_o:alaStackMgrOperStackingMode,_p:alaStackMgrAdminStackingMode,'alaStackMgrStatsTable':alaStackMgrStatsTable,'alaStackMgrStatsEntry':alaStackMgrStatsEntry,_J:alaStackMgrStatLinkNumber,_s:alaStackMgrStatPktsRx,_t:alaStackMgrStatPktsTx,_u:alaStackMgrStatErrorsRx,_v:alaStackMgrStatErrorsTx,_w:alaStackMgrStatDelayFromLastMsg,_R:alaStackMgrStackStatus,_A2:alaStackMgrTokensUsed,_A1:alaStackMgrTokensAvailable,'alaStackMgrStaticRouteTable':alaStackMgrStaticRouteTable,'alaStackMgrStaticRouteEntry':alaStackMgrStaticRouteEntry,_W:alaStackMgrStaticRouteSrcStartIf,_X:alaStackMgrStaticRouteSrcEndIf,_Y:alaStackMgrStaticRouteDstStartIf,_Z:alaStackMgrStaticRouteDstEndIf,_x:alaStackMgrStaticRoutePort,_y:alaStackMgrStaticRoutePortState,_z:alaStackMgrStaticRouteStatus,_A0:alaStackMgrStaticRouteRowStatus,'alaStackMgrStackModeTable':alaStackMgrStackModeTable,'alaStackMgrStackModeEntry':alaStackMgrStackModeEntry,_b:alaStackMgrStackModeIndex,_q:alaStackMgrAdminStackMode,_r:alaStackMgrOperStackMode,'alaStackMgrCmdAction':alaStackMgrCmdAction,'alaSSPStateTable':alaSSPStateTable,'alaSSPStateEntry':alaSSPStateEntry,_c:alaSSPTableSlotNINumber,'alaSSPTableSspOpStatus':alaSSPTableSspOpStatus,'alaSSPHelperGlobalConfig':alaSSPHelperGlobalConfig,_A3:alaSspHelperStatus,'alaSspHelperqAggregateTable':alaSspHelperqAggregateTable,'alaSspHelperqAggregateEntry':alaSspHelperqAggregateEntry,_N:alaSspHelperAggregateId,_A4:alaSspHelperAggregateStatus,'alcatelIND1StackMgrMIBConformance':alcatelIND1StackMgrMIBConformance,'alcatelIND1StackMgrMIBGroups':alcatelIND1StackMgrMIBGroups,_AI:alaStackMgrCfgMgrGroup,_AJ:alaStackMgrNotificationGroup,_AK:alaStackMgrStackModeGroup,_AL:alaStackMgrTrapGroup,_AM:alaStackMgrStatGroup,_AN:alaStackMgrStaticRouteGroup,_AO:alaStackMgrMIBObjectsGroup,_AP:alaSSPConfigInfo,'alaSspConfigStatus':alaSspConfigStatus,'alaSspLinkaggId':alaSspLinkaggId,'alaSspGuardTimer':alaSspGuardTimer,'alaSspUpTime':alaSspUpTime,'alaSspStateUpTime':alaSspStateUpTime,_AQ:alaStackSplitProtectionGroup,'alcatelIND1StackMgrMIBCompliances':alcatelIND1StackMgrMIBCompliances,'alcatelIND1StackMgrMIBCompliance':alcatelIND1StackMgrMIBCompliance,'alcatelIND1StackMgrTrapObjects':alcatelIND1StackMgrTrapObjects,_S:alaStackMgrTrapLinkNumber,_P:alaStackMgrPrimary,_Q:alaStackMgrSecondary,_A5:alaStackMgrPrimaryLicense,'alaStackMgrTraps':alaStackMgrTraps,_A6:alaStackMgrDuplicateSlotTrap,_A7:alaStackMgrNeighborChangeTrap,_A8:alaStackMgrRoleChangeTrap,_A9:alaStackMgrDuplicateRoleTrap,_AA:alaStackMgrClearedSlotTrap,_AB:alaStackMgrOutOfSlotsTrap,_AC:alaStackMgrOutOfTokensTrap,_AD:alaStackMgrOutOfPassThruSlotsTrap,_AE:alaStackMgrBadMixTrap,_AF:alaStackMgrIncompatibleLicenseTrap,_AG:alaStackSplitProtectionTrap,_AH:alaStackSplitRecoveryTrap})