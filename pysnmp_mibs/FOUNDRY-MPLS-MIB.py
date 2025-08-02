_O='mplsLspIndex'
_N='mplsLspSignalingProto'
_M='deprecated'
_L='brcdMplsInterfaceIndex'
_K='brcdMplsAdminGroupId'
_J='mplsLspPathName'
_I='mplsLspName'
_H='read-create'
_G='not-accessible'
_F='DisplayString'
_E='Unsigned32'
_D='FOUNDRY-MPLS-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ClassOfService,=mibBuilder.importSymbols('FDRY-MPLS-L2VPN-MIB','ClassOfService')
AreaID,=mibBuilder.importSymbols('FOUNDRY-SN-OSPF-GROUP-MIB','AreaID')
snMpls,snTraps=mibBuilder.importSymbols('FOUNDRY-SN-ROOT-MIB','snMpls','snTraps')
MplsTunnelAffinity,=mibBuilder.importSymbols('MPLS-TC-STD-MIB','MplsTunnelAffinity')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','RowStatus','TextualConvention','TimeStamp','TruthValue')
mpls=ModuleIdentity((1,3,6,1,4,1,1991,1,2,15,1))
if mibBuilder.loadTexts:mpls.setRevisions(('2013-05-29 00:00','2010-06-02 00:00','2008-02-06 00:00'))
_MplsLspNotifications_ObjectIdentity=ObjectIdentity
mplsLspNotifications=_MplsLspNotifications_ObjectIdentity((1,3,6,1,4,1,1991,1,2,15,1,0))
_MplsInfo_ObjectIdentity=ObjectIdentity
mplsInfo=_MplsInfo_ObjectIdentity((1,3,6,1,4,1,1991,1,2,15,1,1))
_MplsVersion_Type=Unsigned32
_MplsVersion_Object=MibScalar
mplsVersion=_MplsVersion_Object((1,3,6,1,4,1,1991,1,2,15,1,1,1),_MplsVersion_Type())
mplsVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsVersion.setStatus(_A)
_BrcdMplsAdminGroupTable_Object=MibTable
brcdMplsAdminGroupTable=_BrcdMplsAdminGroupTable_Object((1,3,6,1,4,1,1991,1,2,15,1,1,2))
if mibBuilder.loadTexts:brcdMplsAdminGroupTable.setStatus(_A)
_BrcdMplsAdminGroupEntry_Object=MibTableRow
brcdMplsAdminGroupEntry=_BrcdMplsAdminGroupEntry_Object((1,3,6,1,4,1,1991,1,2,15,1,1,2,1))
brcdMplsAdminGroupEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:brcdMplsAdminGroupEntry.setStatus(_A)
class _BrcdMplsAdminGroupId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_BrcdMplsAdminGroupId_Type.__name__=_E
_BrcdMplsAdminGroupId_Object=MibTableColumn
brcdMplsAdminGroupId=_BrcdMplsAdminGroupId_Object((1,3,6,1,4,1,1991,1,2,15,1,1,2,1,1),_BrcdMplsAdminGroupId_Type())
brcdMplsAdminGroupId.setMaxAccess(_G)
if mibBuilder.loadTexts:brcdMplsAdminGroupId.setStatus(_A)
class _BrcdMplsAdminGroupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_BrcdMplsAdminGroupName_Type.__name__=_F
_BrcdMplsAdminGroupName_Object=MibTableColumn
brcdMplsAdminGroupName=_BrcdMplsAdminGroupName_Object((1,3,6,1,4,1,1991,1,2,15,1,1,2,1,2),_BrcdMplsAdminGroupName_Type())
brcdMplsAdminGroupName.setMaxAccess(_H)
if mibBuilder.loadTexts:brcdMplsAdminGroupName.setStatus(_A)
_BrcdMplsAdminGroupRowStatus_Type=RowStatus
_BrcdMplsAdminGroupRowStatus_Object=MibTableColumn
brcdMplsAdminGroupRowStatus=_BrcdMplsAdminGroupRowStatus_Object((1,3,6,1,4,1,1991,1,2,15,1,1,2,1,3),_BrcdMplsAdminGroupRowStatus_Type())
brcdMplsAdminGroupRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:brcdMplsAdminGroupRowStatus.setStatus(_A)
_BrcdMplsInterfaceTable_Object=MibTable
brcdMplsInterfaceTable=_BrcdMplsInterfaceTable_Object((1,3,6,1,4,1,1991,1,2,15,1,1,3))
if mibBuilder.loadTexts:brcdMplsInterfaceTable.setStatus(_A)
_BrcdMplsInterfaceEntry_Object=MibTableRow
brcdMplsInterfaceEntry=_BrcdMplsInterfaceEntry_Object((1,3,6,1,4,1,1991,1,2,15,1,1,3,1))
brcdMplsInterfaceEntry.setIndexNames((0,_D,_L))
if mibBuilder.loadTexts:brcdMplsInterfaceEntry.setStatus(_A)
_BrcdMplsInterfaceIndex_Type=Unsigned32
_BrcdMplsInterfaceIndex_Object=MibTableColumn
brcdMplsInterfaceIndex=_BrcdMplsInterfaceIndex_Object((1,3,6,1,4,1,1991,1,2,15,1,1,3,1,1),_BrcdMplsInterfaceIndex_Type())
brcdMplsInterfaceIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:brcdMplsInterfaceIndex.setStatus(_A)
_BrcdMplsInterfaceAdminGroup_Type=MplsTunnelAffinity
_BrcdMplsInterfaceAdminGroup_Object=MibTableColumn
brcdMplsInterfaceAdminGroup=_BrcdMplsInterfaceAdminGroup_Object((1,3,6,1,4,1,1991,1,2,15,1,1,3,1,2),_BrcdMplsInterfaceAdminGroup_Type())
brcdMplsInterfaceAdminGroup.setMaxAccess(_H)
if mibBuilder.loadTexts:brcdMplsInterfaceAdminGroup.setStatus(_A)
_BrcdMplsInterfaceRowStatus_Type=RowStatus
_BrcdMplsInterfaceRowStatus_Object=MibTableColumn
brcdMplsInterfaceRowStatus=_BrcdMplsInterfaceRowStatus_Object((1,3,6,1,4,1,1991,1,2,15,1,1,3,1,3),_BrcdMplsInterfaceRowStatus_Type())
brcdMplsInterfaceRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:brcdMplsInterfaceRowStatus.setStatus(_A)
_MplsLspInfo_ObjectIdentity=ObjectIdentity
mplsLspInfo=_MplsLspInfo_ObjectIdentity((1,3,6,1,4,1,1991,1,2,15,1,2))
_MplsConfiguredLsps_Type=Unsigned32
_MplsConfiguredLsps_Object=MibScalar
mplsConfiguredLsps=_MplsConfiguredLsps_Object((1,3,6,1,4,1,1991,1,2,15,1,2,1),_MplsConfiguredLsps_Type())
mplsConfiguredLsps.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsConfiguredLsps.setStatus(_M)
_MplsActiveLsps_Type=Unsigned32
_MplsActiveLsps_Object=MibScalar
mplsActiveLsps=_MplsActiveLsps_Object((1,3,6,1,4,1,1991,1,2,15,1,2,2),_MplsActiveLsps_Type())
mplsActiveLsps.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsActiveLsps.setStatus(_M)
_MplsLspTable_Object=MibTable
mplsLspTable=_MplsLspTable_Object((1,3,6,1,4,1,1991,1,2,15,1,2,3))
if mibBuilder.loadTexts:mplsLspTable.setStatus(_A)
_MplsLspEntry_Object=MibTableRow
mplsLspEntry=_MplsLspEntry_Object((1,3,6,1,4,1,1991,1,2,15,1,2,3,1))
mplsLspEntry.setIndexNames((0,_D,_N),(0,_D,_O))
if mibBuilder.loadTexts:mplsLspEntry.setStatus(_A)
class _MplsLspSignalingProto_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ldp',1),('rsvp',2)))
_MplsLspSignalingProto_Type.__name__=_C
_MplsLspSignalingProto_Object=MibTableColumn
mplsLspSignalingProto=_MplsLspSignalingProto_Object((1,3,6,1,4,1,1991,1,2,15,1,2,3,1,1),_MplsLspSignalingProto_Type())
mplsLspSignalingProto.setMaxAccess(_G)
if mibBuilder.loadTexts:mplsLspSignalingProto.setStatus(_A)
_MplsLspIndex_Type=Unsigned32
_MplsLspIndex_Object=MibTableColumn
mplsLspIndex=_MplsLspIndex_Object((1,3,6,1,4,1,1991,1,2,15,1,2,3,1,2),_MplsLspIndex_Type())
mplsLspIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:mplsLspIndex.setStatus(_A)
class _MplsLspName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_MplsLspName_Type.__name__=_F
_MplsLspName_Object=MibTableColumn
mplsLspName=_MplsLspName_Object((1,3,6,1,4,1,1991,1,2,15,1,2,3,1,3),_MplsLspName_Type())
mplsLspName.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsLspName.setStatus(_A)
class _MplsLspState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unknown',1),('up',2),('down',3)))
_MplsLspState_Type.__name__=_C
_MplsLspState_Object=MibTableColumn
mplsLspState=_MplsLspState_Object((1,3,6,1,4,1,1991,1,2,15,1,2,3,1,4),_MplsLspState_Type())
mplsLspState.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsLspState.setStatus(_A)
_MplsLspPackets_Type=Counter64
_MplsLspPackets_Object=MibTableColumn
mplsLspPackets=_MplsLspPackets_Object((1,3,6,1,4,1,1991,1,2,15,1,2,3,1,5),_MplsLspPackets_Type())
mplsLspPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsLspPackets.setStatus(_A)
_MplsLspAge_Type=TimeStamp
_MplsLspAge_Object=MibTableColumn
mplsLspAge=_MplsLspAge_Object((1,3,6,1,4,1,1991,1,2,15,1,2,3,1,6),_MplsLspAge_Type())
mplsLspAge.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsLspAge.setStatus(_A)
_MplsLspTimeUp_Type=TimeStamp
_MplsLspTimeUp_Object=MibTableColumn
mplsLspTimeUp=_MplsLspTimeUp_Object((1,3,6,1,4,1,1991,1,2,15,1,2,3,1,7),_MplsLspTimeUp_Type())
mplsLspTimeUp.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsLspTimeUp.setStatus(_A)
_MplsLspPrimaryTimeUp_Type=TimeStamp
_MplsLspPrimaryTimeUp_Object=MibTableColumn
mplsLspPrimaryTimeUp=_MplsLspPrimaryTimeUp_Object((1,3,6,1,4,1,1991,1,2,15,1,2,3,1,8),_MplsLspPrimaryTimeUp_Type())
mplsLspPrimaryTimeUp.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsLspPrimaryTimeUp.setStatus(_A)
_MplsLspTransitions_Type=Counter32
_MplsLspTransitions_Object=MibTableColumn
mplsLspTransitions=_MplsLspTransitions_Object((1,3,6,1,4,1,1991,1,2,15,1,2,3,1,9),_MplsLspTransitions_Type())
mplsLspTransitions.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsLspTransitions.setStatus(_A)
_MplsLspLastTransition_Type=TimeStamp
_MplsLspLastTransition_Object=MibTableColumn
mplsLspLastTransition=_MplsLspLastTransition_Object((1,3,6,1,4,1,1991,1,2,15,1,2,3,1,10),_MplsLspLastTransition_Type())
mplsLspLastTransition.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsLspLastTransition.setStatus(_A)
_MplsLspFrom_Type=IpAddress
_MplsLspFrom_Object=MibTableColumn
mplsLspFrom=_MplsLspFrom_Object((1,3,6,1,4,1,1991,1,2,15,1,2,3,1,11),_MplsLspFrom_Type())
mplsLspFrom.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsLspFrom.setStatus(_A)
_MplsLspTo_Type=IpAddress
_MplsLspTo_Object=MibTableColumn
mplsLspTo=_MplsLspTo_Object((1,3,6,1,4,1,1991,1,2,15,1,2,3,1,12),_MplsLspTo_Type())
mplsLspTo.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsLspTo.setStatus(_A)
class _MplsLspPathName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_MplsLspPathName_Type.__name__=_F
_MplsLspPathName_Object=MibTableColumn
mplsLspPathName=_MplsLspPathName_Object((1,3,6,1,4,1,1991,1,2,15,1,2,3,1,13),_MplsLspPathName_Type())
mplsLspPathName.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsLspPathName.setStatus(_A)
class _MplsLspPathType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('primary',2),('standby',3),('secondary',4)))
_MplsLspPathType_Type.__name__=_C
_MplsLspPathType_Object=MibTableColumn
mplsLspPathType=_MplsLspPathType_Object((1,3,6,1,4,1,1991,1,2,15,1,2,3,1,14),_MplsLspPathType_Type())
mplsLspPathType.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsLspPathType.setStatus(_A)
_MplsLspAdaptive_Type=TruthValue
_MplsLspAdaptive_Object=MibTableColumn
mplsLspAdaptive=_MplsLspAdaptive_Object((1,3,6,1,4,1,1991,1,2,15,1,2,3,1,15),_MplsLspAdaptive_Type())
mplsLspAdaptive.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsLspAdaptive.setStatus(_A)
_MplsLspBfdSessionId_Type=Unsigned32
_MplsLspBfdSessionId_Object=MibTableColumn
mplsLspBfdSessionId=_MplsLspBfdSessionId_Object((1,3,6,1,4,1,1991,1,2,15,1,2,3,1,16),_MplsLspBfdSessionId_Type())
mplsLspBfdSessionId.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsLspBfdSessionId.setStatus(_A)
class _MplsLspReoptimizeTimer_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(300,65535))
_MplsLspReoptimizeTimer_Type.__name__=_E
_MplsLspReoptimizeTimer_Object=MibTableColumn
mplsLspReoptimizeTimer=_MplsLspReoptimizeTimer_Object((1,3,6,1,4,1,1991,1,2,15,1,2,3,1,17),_MplsLspReoptimizeTimer_Type())
mplsLspReoptimizeTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsLspReoptimizeTimer.setStatus(_A)
_MplsLspCoS_Type=ClassOfService
_MplsLspCoS_Object=MibTableColumn
mplsLspCoS=_MplsLspCoS_Object((1,3,6,1,4,1,1991,1,2,15,1,2,3,1,18),_MplsLspCoS_Type())
mplsLspCoS.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsLspCoS.setStatus(_A)
class _MplsLspHopLimit_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MplsLspHopLimit_Type.__name__=_E
_MplsLspHopLimit_Object=MibTableColumn
mplsLspHopLimit=_MplsLspHopLimit_Object((1,3,6,1,4,1,1991,1,2,15,1,2,3,1,19),_MplsLspHopLimit_Type())
mplsLspHopLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsLspHopLimit.setStatus(_A)
class _MplsLspCspf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_MplsLspCspf_Type.__name__=_C
_MplsLspCspf_Object=MibTableColumn
mplsLspCspf=_MplsLspCspf_Object((1,3,6,1,4,1,1991,1,2,15,1,2,3,1,20),_MplsLspCspf_Type())
mplsLspCspf.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsLspCspf.setStatus(_A)
class _MplsLspCspfTieBreaker_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('random',1),('leastFill',2),('mostFill',3)))
_MplsLspCspfTieBreaker_Type.__name__=_C
_MplsLspCspfTieBreaker_Object=MibTableColumn
mplsLspCspfTieBreaker=_MplsLspCspfTieBreaker_Object((1,3,6,1,4,1,1991,1,2,15,1,2,3,1,21),_MplsLspCspfTieBreaker_Type())
mplsLspCspfTieBreaker.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsLspCspfTieBreaker.setStatus(_A)
class _MplsLspFrrMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('detour',2),('facility',3)))
_MplsLspFrrMode_Type.__name__=_C
_MplsLspFrrMode_Object=MibTableColumn
mplsLspFrrMode=_MplsLspFrrMode_Object((1,3,6,1,4,1,1991,1,2,15,1,2,3,1,22),_MplsLspFrrMode_Type())
mplsLspFrrMode.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsLspFrrMode.setStatus(_A)
class _MplsLspFrrSetupPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_MplsLspFrrSetupPriority_Type.__name__=_E
_MplsLspFrrSetupPriority_Object=MibTableColumn
mplsLspFrrSetupPriority=_MplsLspFrrSetupPriority_Object((1,3,6,1,4,1,1991,1,2,15,1,2,3,1,23),_MplsLspFrrSetupPriority_Type())
mplsLspFrrSetupPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsLspFrrSetupPriority.setStatus(_A)
class _MplsLspFrrHoldingPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_MplsLspFrrHoldingPriority_Type.__name__=_E
_MplsLspFrrHoldingPriority_Object=MibTableColumn
mplsLspFrrHoldingPriority=_MplsLspFrrHoldingPriority_Object((1,3,6,1,4,1,1991,1,2,15,1,2,3,1,24),_MplsLspFrrHoldingPriority_Type())
mplsLspFrrHoldingPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsLspFrrHoldingPriority.setStatus(_A)
class _MplsLspFrrHopLimit_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MplsLspFrrHopLimit_Type.__name__=_E
_MplsLspFrrHopLimit_Object=MibTableColumn
mplsLspFrrHopLimit=_MplsLspFrrHopLimit_Object((1,3,6,1,4,1,1991,1,2,15,1,2,3,1,25),_MplsLspFrrHopLimit_Type())
mplsLspFrrHopLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsLspFrrHopLimit.setStatus(_A)
class _MplsLspFrrBandwidth_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_MplsLspFrrBandwidth_Type.__name__=_E
_MplsLspFrrBandwidth_Object=MibTableColumn
mplsLspFrrBandwidth=_MplsLspFrrBandwidth_Object((1,3,6,1,4,1,1991,1,2,15,1,2,3,1,26),_MplsLspFrrBandwidth_Type())
mplsLspFrrBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsLspFrrBandwidth.setStatus(_A)
_MplsLspFrrAdmGrpIncludeAny_Type=MplsTunnelAffinity
_MplsLspFrrAdmGrpIncludeAny_Object=MibTableColumn
mplsLspFrrAdmGrpIncludeAny=_MplsLspFrrAdmGrpIncludeAny_Object((1,3,6,1,4,1,1991,1,2,15,1,2,3,1,27),_MplsLspFrrAdmGrpIncludeAny_Type())
mplsLspFrrAdmGrpIncludeAny.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsLspFrrAdmGrpIncludeAny.setStatus(_A)
_MplsLspFrrAdmGrpIncludeAll_Type=MplsTunnelAffinity
_MplsLspFrrAdmGrpIncludeAll_Object=MibTableColumn
mplsLspFrrAdmGrpIncludeAll=_MplsLspFrrAdmGrpIncludeAll_Object((1,3,6,1,4,1,1991,1,2,15,1,2,3,1,28),_MplsLspFrrAdmGrpIncludeAll_Type())
mplsLspFrrAdmGrpIncludeAll.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsLspFrrAdmGrpIncludeAll.setStatus(_A)
_MplsLspFrrAdmGrpExcludeAny_Type=MplsTunnelAffinity
_MplsLspFrrAdmGrpExcludeAny_Object=MibTableColumn
mplsLspFrrAdmGrpExcludeAny=_MplsLspFrrAdmGrpExcludeAny_Object((1,3,6,1,4,1,1991,1,2,15,1,2,3,1,29),_MplsLspFrrAdmGrpExcludeAny_Type())
mplsLspFrrAdmGrpExcludeAny.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsLspFrrAdmGrpExcludeAny.setStatus(_A)
class _MplsLspPathSelectMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('auto',1),('manual',2),('unconditional',3)))
_MplsLspPathSelectMode_Type.__name__=_C
_MplsLspPathSelectMode_Object=MibTableColumn
mplsLspPathSelectMode=_MplsLspPathSelectMode_Object((1,3,6,1,4,1,1991,1,2,15,1,2,3,1,30),_MplsLspPathSelectMode_Type())
mplsLspPathSelectMode.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsLspPathSelectMode.setStatus(_A)
class _MplsLspPathSelectPathname_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_MplsLspPathSelectPathname_Type.__name__=_F
_MplsLspPathSelectPathname_Object=MibTableColumn
mplsLspPathSelectPathname=_MplsLspPathSelectPathname_Object((1,3,6,1,4,1,1991,1,2,15,1,2,3,1,31),_MplsLspPathSelectPathname_Type())
mplsLspPathSelectPathname.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsLspPathSelectPathname.setStatus(_A)
class _MplsLspPathSelectRevertTimer_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MplsLspPathSelectRevertTimer_Type.__name__=_E
_MplsLspPathSelectRevertTimer_Object=MibTableColumn
mplsLspPathSelectRevertTimer=_MplsLspPathSelectRevertTimer_Object((1,3,6,1,4,1,1991,1,2,15,1,2,3,1,32),_MplsLspPathSelectRevertTimer_Type())
mplsLspPathSelectRevertTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsLspPathSelectRevertTimer.setStatus(_A)
_MplsLspShortcutOspfAllowed_Type=TruthValue
_MplsLspShortcutOspfAllowed_Object=MibTableColumn
mplsLspShortcutOspfAllowed=_MplsLspShortcutOspfAllowed_Object((1,3,6,1,4,1,1991,1,2,15,1,2,3,1,33),_MplsLspShortcutOspfAllowed_Type())
mplsLspShortcutOspfAllowed.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsLspShortcutOspfAllowed.setStatus(_A)
_MplsLspShortcutIsisAllowed_Type=TruthValue
_MplsLspShortcutIsisAllowed_Object=MibTableColumn
mplsLspShortcutIsisAllowed=_MplsLspShortcutIsisAllowed_Object((1,3,6,1,4,1,1991,1,2,15,1,2,3,1,34),_MplsLspShortcutIsisAllowed_Type())
mplsLspShortcutIsisAllowed.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsLspShortcutIsisAllowed.setStatus(_A)
class _MplsLspShortcutIsisLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('level1',1),('level2',2),('level1and2',3)))
_MplsLspShortcutIsisLevel_Type.__name__=_C
_MplsLspShortcutIsisLevel_Object=MibTableColumn
mplsLspShortcutIsisLevel=_MplsLspShortcutIsisLevel_Object((1,3,6,1,4,1,1991,1,2,15,1,2,3,1,35),_MplsLspShortcutIsisLevel_Type())
mplsLspShortcutIsisLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsLspShortcutIsisLevel.setStatus(_A)
_MplsLspShortcutIsisAnnounce_Type=TruthValue
_MplsLspShortcutIsisAnnounce_Object=MibTableColumn
mplsLspShortcutIsisAnnounce=_MplsLspShortcutIsisAnnounce_Object((1,3,6,1,4,1,1991,1,2,15,1,2,3,1,36),_MplsLspShortcutIsisAnnounce_Type())
mplsLspShortcutIsisAnnounce.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsLspShortcutIsisAnnounce.setStatus(_A)
class _MplsLspShortcutIsisAnnounceMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16777215))
_MplsLspShortcutIsisAnnounceMetric_Type.__name__=_C
_MplsLspShortcutIsisAnnounceMetric_Object=MibTableColumn
mplsLspShortcutIsisAnnounceMetric=_MplsLspShortcutIsisAnnounceMetric_Object((1,3,6,1,4,1,1991,1,2,15,1,2,3,1,37),_MplsLspShortcutIsisAnnounceMetric_Type())
mplsLspShortcutIsisAnnounceMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsLspShortcutIsisAnnounceMetric.setStatus(_A)
class _MplsLspShortcutIsisRelativeMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-16777215,16777215))
_MplsLspShortcutIsisRelativeMetric_Type.__name__=_C
_MplsLspShortcutIsisRelativeMetric_Object=MibTableColumn
mplsLspShortcutIsisRelativeMetric=_MplsLspShortcutIsisRelativeMetric_Object((1,3,6,1,4,1,1991,1,2,15,1,2,3,1,38),_MplsLspShortcutIsisRelativeMetric_Type())
mplsLspShortcutIsisRelativeMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:mplsLspShortcutIsisRelativeMetric.setStatus(_A)
_MplsVllInfo_ObjectIdentity=ObjectIdentity
mplsVllInfo=_MplsVllInfo_ObjectIdentity((1,3,6,1,4,1,1991,1,2,15,1,3))
_MplsVplsInfo_ObjectIdentity=ObjectIdentity
mplsVplsInfo=_MplsVplsInfo_ObjectIdentity((1,3,6,1,4,1,1991,1,2,15,1,4))
snMplsLspUp=NotificationType((1,3,6,1,4,1,1991,0,1010))
snMplsLspUp.setObjects(*((_D,_I),(_D,_J)))
if mibBuilder.loadTexts:snMplsLspUp.setStatus(_A)
snMplsLspDown=NotificationType((1,3,6,1,4,1,1991,0,1011))
snMplsLspDown.setObjects(*((_D,_I),(_D,_J)))
if mibBuilder.loadTexts:snMplsLspDown.setStatus(_A)
snMplsLspChange=NotificationType((1,3,6,1,4,1,1991,0,1012))
snMplsLspChange.setObjects(*((_D,_I),(_D,_J)))
if mibBuilder.loadTexts:snMplsLspChange.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'snMplsLspUp':snMplsLspUp,'snMplsLspDown':snMplsLspDown,'snMplsLspChange':snMplsLspChange,'mpls':mpls,'mplsLspNotifications':mplsLspNotifications,'mplsInfo':mplsInfo,'mplsVersion':mplsVersion,'brcdMplsAdminGroupTable':brcdMplsAdminGroupTable,'brcdMplsAdminGroupEntry':brcdMplsAdminGroupEntry,_K:brcdMplsAdminGroupId,'brcdMplsAdminGroupName':brcdMplsAdminGroupName,'brcdMplsAdminGroupRowStatus':brcdMplsAdminGroupRowStatus,'brcdMplsInterfaceTable':brcdMplsInterfaceTable,'brcdMplsInterfaceEntry':brcdMplsInterfaceEntry,_L:brcdMplsInterfaceIndex,'brcdMplsInterfaceAdminGroup':brcdMplsInterfaceAdminGroup,'brcdMplsInterfaceRowStatus':brcdMplsInterfaceRowStatus,'mplsLspInfo':mplsLspInfo,'mplsConfiguredLsps':mplsConfiguredLsps,'mplsActiveLsps':mplsActiveLsps,'mplsLspTable':mplsLspTable,'mplsLspEntry':mplsLspEntry,_N:mplsLspSignalingProto,_O:mplsLspIndex,_I:mplsLspName,'mplsLspState':mplsLspState,'mplsLspPackets':mplsLspPackets,'mplsLspAge':mplsLspAge,'mplsLspTimeUp':mplsLspTimeUp,'mplsLspPrimaryTimeUp':mplsLspPrimaryTimeUp,'mplsLspTransitions':mplsLspTransitions,'mplsLspLastTransition':mplsLspLastTransition,'mplsLspFrom':mplsLspFrom,'mplsLspTo':mplsLspTo,_J:mplsLspPathName,'mplsLspPathType':mplsLspPathType,'mplsLspAdaptive':mplsLspAdaptive,'mplsLspBfdSessionId':mplsLspBfdSessionId,'mplsLspReoptimizeTimer':mplsLspReoptimizeTimer,'mplsLspCoS':mplsLspCoS,'mplsLspHopLimit':mplsLspHopLimit,'mplsLspCspf':mplsLspCspf,'mplsLspCspfTieBreaker':mplsLspCspfTieBreaker,'mplsLspFrrMode':mplsLspFrrMode,'mplsLspFrrSetupPriority':mplsLspFrrSetupPriority,'mplsLspFrrHoldingPriority':mplsLspFrrHoldingPriority,'mplsLspFrrHopLimit':mplsLspFrrHopLimit,'mplsLspFrrBandwidth':mplsLspFrrBandwidth,'mplsLspFrrAdmGrpIncludeAny':mplsLspFrrAdmGrpIncludeAny,'mplsLspFrrAdmGrpIncludeAll':mplsLspFrrAdmGrpIncludeAll,'mplsLspFrrAdmGrpExcludeAny':mplsLspFrrAdmGrpExcludeAny,'mplsLspPathSelectMode':mplsLspPathSelectMode,'mplsLspPathSelectPathname':mplsLspPathSelectPathname,'mplsLspPathSelectRevertTimer':mplsLspPathSelectRevertTimer,'mplsLspShortcutOspfAllowed':mplsLspShortcutOspfAllowed,'mplsLspShortcutIsisAllowed':mplsLspShortcutIsisAllowed,'mplsLspShortcutIsisLevel':mplsLspShortcutIsisLevel,'mplsLspShortcutIsisAnnounce':mplsLspShortcutIsisAnnounce,'mplsLspShortcutIsisAnnounceMetric':mplsLspShortcutIsisAnnounceMetric,'mplsLspShortcutIsisRelativeMetric':mplsLspShortcutIsisRelativeMetric,'mplsVllInfo':mplsVllInfo,'mplsVplsInfo':mplsVplsInfo})