_O='bcsiMplsLspIndex'
_N='bcsiMplsLspSignalingProto'
_M='deprecated'
_L='bcsiMplsInterfaceIndex'
_K='bcsiMplsAdminGroupId'
_J='bcsiMplsLspPathName'
_I='bcsiMplsLspName'
_H='read-create'
_G='not-accessible'
_F='DisplayString'
_E='Unsigned32'
_D='BROCADE-MPLS-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
bcsiModules,=mibBuilder.importSymbols('Brocade-REG-MIB','bcsiModules')
MplsTunnelAffinity,=mibBuilder.importSymbols('MPLS-TC-STD-MIB','MplsTunnelAffinity')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','RowStatus','TextualConvention','TimeStamp','TruthValue')
brocadeMplsMIB=ModuleIdentity((1,3,6,1,4,1,1588,3,1,10))
if mibBuilder.loadTexts:brocadeMplsMIB.setRevisions(('2018-05-29 12:00','2016-09-28 00:00','2013-05-29 00:00','2010-06-02 00:00','2008-02-06 00:00'))
class ClassOfService(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_BcsiMplsNotifications_ObjectIdentity=ObjectIdentity
bcsiMplsNotifications=_BcsiMplsNotifications_ObjectIdentity((1,3,6,1,4,1,1588,3,1,10,0))
_BcsiMplsObjects_ObjectIdentity=ObjectIdentity
bcsiMplsObjects=_BcsiMplsObjects_ObjectIdentity((1,3,6,1,4,1,1588,3,1,10,1))
_BcsiMplsInfo_ObjectIdentity=ObjectIdentity
bcsiMplsInfo=_BcsiMplsInfo_ObjectIdentity((1,3,6,1,4,1,1588,3,1,10,1,1))
_BcsiMplsVersion_Type=Unsigned32
_BcsiMplsVersion_Object=MibScalar
bcsiMplsVersion=_BcsiMplsVersion_Object((1,3,6,1,4,1,1588,3,1,10,1,1,1),_BcsiMplsVersion_Type())
bcsiMplsVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiMplsVersion.setStatus(_A)
_BcsiMplsAdminGroupTable_Object=MibTable
bcsiMplsAdminGroupTable=_BcsiMplsAdminGroupTable_Object((1,3,6,1,4,1,1588,3,1,10,1,1,2))
if mibBuilder.loadTexts:bcsiMplsAdminGroupTable.setStatus(_A)
_BcsiMplsAdminGroupEntry_Object=MibTableRow
bcsiMplsAdminGroupEntry=_BcsiMplsAdminGroupEntry_Object((1,3,6,1,4,1,1588,3,1,10,1,1,2,1))
bcsiMplsAdminGroupEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:bcsiMplsAdminGroupEntry.setStatus(_A)
class _BcsiMplsAdminGroupId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_BcsiMplsAdminGroupId_Type.__name__=_E
_BcsiMplsAdminGroupId_Object=MibTableColumn
bcsiMplsAdminGroupId=_BcsiMplsAdminGroupId_Object((1,3,6,1,4,1,1588,3,1,10,1,1,2,1,1),_BcsiMplsAdminGroupId_Type())
bcsiMplsAdminGroupId.setMaxAccess(_G)
if mibBuilder.loadTexts:bcsiMplsAdminGroupId.setStatus(_A)
class _BcsiMplsAdminGroupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_BcsiMplsAdminGroupName_Type.__name__=_F
_BcsiMplsAdminGroupName_Object=MibTableColumn
bcsiMplsAdminGroupName=_BcsiMplsAdminGroupName_Object((1,3,6,1,4,1,1588,3,1,10,1,1,2,1,2),_BcsiMplsAdminGroupName_Type())
bcsiMplsAdminGroupName.setMaxAccess(_H)
if mibBuilder.loadTexts:bcsiMplsAdminGroupName.setStatus(_A)
_BcsiMplsAdminGroupRowStatus_Type=RowStatus
_BcsiMplsAdminGroupRowStatus_Object=MibTableColumn
bcsiMplsAdminGroupRowStatus=_BcsiMplsAdminGroupRowStatus_Object((1,3,6,1,4,1,1588,3,1,10,1,1,2,1,3),_BcsiMplsAdminGroupRowStatus_Type())
bcsiMplsAdminGroupRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:bcsiMplsAdminGroupRowStatus.setStatus(_A)
_BcsiMplsInterfaceTable_Object=MibTable
bcsiMplsInterfaceTable=_BcsiMplsInterfaceTable_Object((1,3,6,1,4,1,1588,3,1,10,1,1,3))
if mibBuilder.loadTexts:bcsiMplsInterfaceTable.setStatus(_A)
_BcsiMplsInterfaceEntry_Object=MibTableRow
bcsiMplsInterfaceEntry=_BcsiMplsInterfaceEntry_Object((1,3,6,1,4,1,1588,3,1,10,1,1,3,1))
bcsiMplsInterfaceEntry.setIndexNames((0,_D,_L))
if mibBuilder.loadTexts:bcsiMplsInterfaceEntry.setStatus(_A)
_BcsiMplsInterfaceIndex_Type=Unsigned32
_BcsiMplsInterfaceIndex_Object=MibTableColumn
bcsiMplsInterfaceIndex=_BcsiMplsInterfaceIndex_Object((1,3,6,1,4,1,1588,3,1,10,1,1,3,1,1),_BcsiMplsInterfaceIndex_Type())
bcsiMplsInterfaceIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:bcsiMplsInterfaceIndex.setStatus(_A)
_BcsiMplsInterfaceAdminGroup_Type=MplsTunnelAffinity
_BcsiMplsInterfaceAdminGroup_Object=MibTableColumn
bcsiMplsInterfaceAdminGroup=_BcsiMplsInterfaceAdminGroup_Object((1,3,6,1,4,1,1588,3,1,10,1,1,3,1,2),_BcsiMplsInterfaceAdminGroup_Type())
bcsiMplsInterfaceAdminGroup.setMaxAccess(_H)
if mibBuilder.loadTexts:bcsiMplsInterfaceAdminGroup.setStatus(_A)
_BcsiMplsInterfaceRowStatus_Type=RowStatus
_BcsiMplsInterfaceRowStatus_Object=MibTableColumn
bcsiMplsInterfaceRowStatus=_BcsiMplsInterfaceRowStatus_Object((1,3,6,1,4,1,1588,3,1,10,1,1,3,1,3),_BcsiMplsInterfaceRowStatus_Type())
bcsiMplsInterfaceRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:bcsiMplsInterfaceRowStatus.setStatus(_A)
_BcsiMplsLspInfo_ObjectIdentity=ObjectIdentity
bcsiMplsLspInfo=_BcsiMplsLspInfo_ObjectIdentity((1,3,6,1,4,1,1588,3,1,10,1,2))
_BcsiMplsConfiguredLsps_Type=Unsigned32
_BcsiMplsConfiguredLsps_Object=MibScalar
bcsiMplsConfiguredLsps=_BcsiMplsConfiguredLsps_Object((1,3,6,1,4,1,1588,3,1,10,1,2,1),_BcsiMplsConfiguredLsps_Type())
bcsiMplsConfiguredLsps.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiMplsConfiguredLsps.setStatus(_M)
_BcsiMplsActiveLsps_Type=Unsigned32
_BcsiMplsActiveLsps_Object=MibScalar
bcsiMplsActiveLsps=_BcsiMplsActiveLsps_Object((1,3,6,1,4,1,1588,3,1,10,1,2,2),_BcsiMplsActiveLsps_Type())
bcsiMplsActiveLsps.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiMplsActiveLsps.setStatus(_M)
_BcsiMplsLspTable_Object=MibTable
bcsiMplsLspTable=_BcsiMplsLspTable_Object((1,3,6,1,4,1,1588,3,1,10,1,2,3))
if mibBuilder.loadTexts:bcsiMplsLspTable.setStatus(_A)
_BcsiMplsLspEntry_Object=MibTableRow
bcsiMplsLspEntry=_BcsiMplsLspEntry_Object((1,3,6,1,4,1,1588,3,1,10,1,2,3,1))
bcsiMplsLspEntry.setIndexNames((0,_D,_N),(0,_D,_O))
if mibBuilder.loadTexts:bcsiMplsLspEntry.setStatus(_A)
class _BcsiMplsLspSignalingProto_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ldp',1),('rsvp',2)))
_BcsiMplsLspSignalingProto_Type.__name__=_C
_BcsiMplsLspSignalingProto_Object=MibTableColumn
bcsiMplsLspSignalingProto=_BcsiMplsLspSignalingProto_Object((1,3,6,1,4,1,1588,3,1,10,1,2,3,1,1),_BcsiMplsLspSignalingProto_Type())
bcsiMplsLspSignalingProto.setMaxAccess(_G)
if mibBuilder.loadTexts:bcsiMplsLspSignalingProto.setStatus(_A)
_BcsiMplsLspIndex_Type=Unsigned32
_BcsiMplsLspIndex_Object=MibTableColumn
bcsiMplsLspIndex=_BcsiMplsLspIndex_Object((1,3,6,1,4,1,1588,3,1,10,1,2,3,1,2),_BcsiMplsLspIndex_Type())
bcsiMplsLspIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:bcsiMplsLspIndex.setStatus(_A)
class _BcsiMplsLspName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_BcsiMplsLspName_Type.__name__=_F
_BcsiMplsLspName_Object=MibTableColumn
bcsiMplsLspName=_BcsiMplsLspName_Object((1,3,6,1,4,1,1588,3,1,10,1,2,3,1,3),_BcsiMplsLspName_Type())
bcsiMplsLspName.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiMplsLspName.setStatus(_A)
class _BcsiMplsLspState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unknown',1),('up',2),('down',3)))
_BcsiMplsLspState_Type.__name__=_C
_BcsiMplsLspState_Object=MibTableColumn
bcsiMplsLspState=_BcsiMplsLspState_Object((1,3,6,1,4,1,1588,3,1,10,1,2,3,1,4),_BcsiMplsLspState_Type())
bcsiMplsLspState.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiMplsLspState.setStatus(_A)
_BcsiMplsLspPackets_Type=Counter64
_BcsiMplsLspPackets_Object=MibTableColumn
bcsiMplsLspPackets=_BcsiMplsLspPackets_Object((1,3,6,1,4,1,1588,3,1,10,1,2,3,1,5),_BcsiMplsLspPackets_Type())
bcsiMplsLspPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiMplsLspPackets.setStatus(_A)
_BcsiMplsLspAge_Type=TimeStamp
_BcsiMplsLspAge_Object=MibTableColumn
bcsiMplsLspAge=_BcsiMplsLspAge_Object((1,3,6,1,4,1,1588,3,1,10,1,2,3,1,6),_BcsiMplsLspAge_Type())
bcsiMplsLspAge.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiMplsLspAge.setStatus(_A)
_BcsiMplsLspTimeUp_Type=TimeStamp
_BcsiMplsLspTimeUp_Object=MibTableColumn
bcsiMplsLspTimeUp=_BcsiMplsLspTimeUp_Object((1,3,6,1,4,1,1588,3,1,10,1,2,3,1,7),_BcsiMplsLspTimeUp_Type())
bcsiMplsLspTimeUp.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiMplsLspTimeUp.setStatus(_A)
_BcsiMplsLspPrimaryTimeUp_Type=TimeStamp
_BcsiMplsLspPrimaryTimeUp_Object=MibTableColumn
bcsiMplsLspPrimaryTimeUp=_BcsiMplsLspPrimaryTimeUp_Object((1,3,6,1,4,1,1588,3,1,10,1,2,3,1,8),_BcsiMplsLspPrimaryTimeUp_Type())
bcsiMplsLspPrimaryTimeUp.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiMplsLspPrimaryTimeUp.setStatus(_A)
_BcsiMplsLspTransitions_Type=Counter32
_BcsiMplsLspTransitions_Object=MibTableColumn
bcsiMplsLspTransitions=_BcsiMplsLspTransitions_Object((1,3,6,1,4,1,1588,3,1,10,1,2,3,1,9),_BcsiMplsLspTransitions_Type())
bcsiMplsLspTransitions.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiMplsLspTransitions.setStatus(_A)
_BcsiMplsLspLastTransition_Type=TimeStamp
_BcsiMplsLspLastTransition_Object=MibTableColumn
bcsiMplsLspLastTransition=_BcsiMplsLspLastTransition_Object((1,3,6,1,4,1,1588,3,1,10,1,2,3,1,10),_BcsiMplsLspLastTransition_Type())
bcsiMplsLspLastTransition.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiMplsLspLastTransition.setStatus(_A)
_BcsiMplsLspFrom_Type=IpAddress
_BcsiMplsLspFrom_Object=MibTableColumn
bcsiMplsLspFrom=_BcsiMplsLspFrom_Object((1,3,6,1,4,1,1588,3,1,10,1,2,3,1,11),_BcsiMplsLspFrom_Type())
bcsiMplsLspFrom.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiMplsLspFrom.setStatus(_A)
_BcsiMplsLspTo_Type=IpAddress
_BcsiMplsLspTo_Object=MibTableColumn
bcsiMplsLspTo=_BcsiMplsLspTo_Object((1,3,6,1,4,1,1588,3,1,10,1,2,3,1,12),_BcsiMplsLspTo_Type())
bcsiMplsLspTo.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiMplsLspTo.setStatus(_A)
class _BcsiMplsLspPathName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_BcsiMplsLspPathName_Type.__name__=_F
_BcsiMplsLspPathName_Object=MibTableColumn
bcsiMplsLspPathName=_BcsiMplsLspPathName_Object((1,3,6,1,4,1,1588,3,1,10,1,2,3,1,13),_BcsiMplsLspPathName_Type())
bcsiMplsLspPathName.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiMplsLspPathName.setStatus(_A)
class _BcsiMplsLspPathType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('primary',2),('standby',3),('secondary',4)))
_BcsiMplsLspPathType_Type.__name__=_C
_BcsiMplsLspPathType_Object=MibTableColumn
bcsiMplsLspPathType=_BcsiMplsLspPathType_Object((1,3,6,1,4,1,1588,3,1,10,1,2,3,1,14),_BcsiMplsLspPathType_Type())
bcsiMplsLspPathType.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiMplsLspPathType.setStatus(_A)
_BcsiMplsLspAdaptive_Type=TruthValue
_BcsiMplsLspAdaptive_Object=MibTableColumn
bcsiMplsLspAdaptive=_BcsiMplsLspAdaptive_Object((1,3,6,1,4,1,1588,3,1,10,1,2,3,1,15),_BcsiMplsLspAdaptive_Type())
bcsiMplsLspAdaptive.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiMplsLspAdaptive.setStatus(_A)
_BcsiMplsLspBfdSessionId_Type=Unsigned32
_BcsiMplsLspBfdSessionId_Object=MibTableColumn
bcsiMplsLspBfdSessionId=_BcsiMplsLspBfdSessionId_Object((1,3,6,1,4,1,1588,3,1,10,1,2,3,1,16),_BcsiMplsLspBfdSessionId_Type())
bcsiMplsLspBfdSessionId.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiMplsLspBfdSessionId.setStatus(_A)
class _BcsiMplsLspReoptimizeTimer_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(300,65535))
_BcsiMplsLspReoptimizeTimer_Type.__name__=_E
_BcsiMplsLspReoptimizeTimer_Object=MibTableColumn
bcsiMplsLspReoptimizeTimer=_BcsiMplsLspReoptimizeTimer_Object((1,3,6,1,4,1,1588,3,1,10,1,2,3,1,17),_BcsiMplsLspReoptimizeTimer_Type())
bcsiMplsLspReoptimizeTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiMplsLspReoptimizeTimer.setStatus(_A)
_BcsiMplsLspCoS_Type=ClassOfService
_BcsiMplsLspCoS_Object=MibTableColumn
bcsiMplsLspCoS=_BcsiMplsLspCoS_Object((1,3,6,1,4,1,1588,3,1,10,1,2,3,1,18),_BcsiMplsLspCoS_Type())
bcsiMplsLspCoS.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiMplsLspCoS.setStatus(_A)
class _BcsiMplsLspHopLimit_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BcsiMplsLspHopLimit_Type.__name__=_E
_BcsiMplsLspHopLimit_Object=MibTableColumn
bcsiMplsLspHopLimit=_BcsiMplsLspHopLimit_Object((1,3,6,1,4,1,1588,3,1,10,1,2,3,1,19),_BcsiMplsLspHopLimit_Type())
bcsiMplsLspHopLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiMplsLspHopLimit.setStatus(_A)
class _BcsiMplsLspCspf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_BcsiMplsLspCspf_Type.__name__=_C
_BcsiMplsLspCspf_Object=MibTableColumn
bcsiMplsLspCspf=_BcsiMplsLspCspf_Object((1,3,6,1,4,1,1588,3,1,10,1,2,3,1,20),_BcsiMplsLspCspf_Type())
bcsiMplsLspCspf.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiMplsLspCspf.setStatus(_A)
class _BcsiMplsLspCspfTieBreaker_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('random',1),('leastFill',2),('mostFill',3)))
_BcsiMplsLspCspfTieBreaker_Type.__name__=_C
_BcsiMplsLspCspfTieBreaker_Object=MibTableColumn
bcsiMplsLspCspfTieBreaker=_BcsiMplsLspCspfTieBreaker_Object((1,3,6,1,4,1,1588,3,1,10,1,2,3,1,21),_BcsiMplsLspCspfTieBreaker_Type())
bcsiMplsLspCspfTieBreaker.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiMplsLspCspfTieBreaker.setStatus(_A)
class _BcsiMplsLspFrrMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('detour',2),('facility',3)))
_BcsiMplsLspFrrMode_Type.__name__=_C
_BcsiMplsLspFrrMode_Object=MibTableColumn
bcsiMplsLspFrrMode=_BcsiMplsLspFrrMode_Object((1,3,6,1,4,1,1588,3,1,10,1,2,3,1,22),_BcsiMplsLspFrrMode_Type())
bcsiMplsLspFrrMode.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiMplsLspFrrMode.setStatus(_A)
class _BcsiMplsLspFrrSetupPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_BcsiMplsLspFrrSetupPriority_Type.__name__=_E
_BcsiMplsLspFrrSetupPriority_Object=MibTableColumn
bcsiMplsLspFrrSetupPriority=_BcsiMplsLspFrrSetupPriority_Object((1,3,6,1,4,1,1588,3,1,10,1,2,3,1,23),_BcsiMplsLspFrrSetupPriority_Type())
bcsiMplsLspFrrSetupPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiMplsLspFrrSetupPriority.setStatus(_A)
class _BcsiMplsLspFrrHoldingPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_BcsiMplsLspFrrHoldingPriority_Type.__name__=_E
_BcsiMplsLspFrrHoldingPriority_Object=MibTableColumn
bcsiMplsLspFrrHoldingPriority=_BcsiMplsLspFrrHoldingPriority_Object((1,3,6,1,4,1,1588,3,1,10,1,2,3,1,24),_BcsiMplsLspFrrHoldingPriority_Type())
bcsiMplsLspFrrHoldingPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiMplsLspFrrHoldingPriority.setStatus(_A)
class _BcsiMplsLspFrrHopLimit_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BcsiMplsLspFrrHopLimit_Type.__name__=_E
_BcsiMplsLspFrrHopLimit_Object=MibTableColumn
bcsiMplsLspFrrHopLimit=_BcsiMplsLspFrrHopLimit_Object((1,3,6,1,4,1,1588,3,1,10,1,2,3,1,25),_BcsiMplsLspFrrHopLimit_Type())
bcsiMplsLspFrrHopLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiMplsLspFrrHopLimit.setStatus(_A)
class _BcsiMplsLspFrrBandwidth_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_BcsiMplsLspFrrBandwidth_Type.__name__=_E
_BcsiMplsLspFrrBandwidth_Object=MibTableColumn
bcsiMplsLspFrrBandwidth=_BcsiMplsLspFrrBandwidth_Object((1,3,6,1,4,1,1588,3,1,10,1,2,3,1,26),_BcsiMplsLspFrrBandwidth_Type())
bcsiMplsLspFrrBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiMplsLspFrrBandwidth.setStatus(_A)
_BcsiMplsLspFrrAdmGrpIncludeAny_Type=MplsTunnelAffinity
_BcsiMplsLspFrrAdmGrpIncludeAny_Object=MibTableColumn
bcsiMplsLspFrrAdmGrpIncludeAny=_BcsiMplsLspFrrAdmGrpIncludeAny_Object((1,3,6,1,4,1,1588,3,1,10,1,2,3,1,27),_BcsiMplsLspFrrAdmGrpIncludeAny_Type())
bcsiMplsLspFrrAdmGrpIncludeAny.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiMplsLspFrrAdmGrpIncludeAny.setStatus(_A)
_BcsiMplsLspFrrAdmGrpIncludeAll_Type=MplsTunnelAffinity
_BcsiMplsLspFrrAdmGrpIncludeAll_Object=MibTableColumn
bcsiMplsLspFrrAdmGrpIncludeAll=_BcsiMplsLspFrrAdmGrpIncludeAll_Object((1,3,6,1,4,1,1588,3,1,10,1,2,3,1,28),_BcsiMplsLspFrrAdmGrpIncludeAll_Type())
bcsiMplsLspFrrAdmGrpIncludeAll.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiMplsLspFrrAdmGrpIncludeAll.setStatus(_A)
_BcsiMplsLspFrrAdmGrpExcludeAny_Type=MplsTunnelAffinity
_BcsiMplsLspFrrAdmGrpExcludeAny_Object=MibTableColumn
bcsiMplsLspFrrAdmGrpExcludeAny=_BcsiMplsLspFrrAdmGrpExcludeAny_Object((1,3,6,1,4,1,1588,3,1,10,1,2,3,1,29),_BcsiMplsLspFrrAdmGrpExcludeAny_Type())
bcsiMplsLspFrrAdmGrpExcludeAny.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiMplsLspFrrAdmGrpExcludeAny.setStatus(_A)
class _BcsiMplsLspPathSelectMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('auto',1),('manual',2),('unconditional',3)))
_BcsiMplsLspPathSelectMode_Type.__name__=_C
_BcsiMplsLspPathSelectMode_Object=MibTableColumn
bcsiMplsLspPathSelectMode=_BcsiMplsLspPathSelectMode_Object((1,3,6,1,4,1,1588,3,1,10,1,2,3,1,30),_BcsiMplsLspPathSelectMode_Type())
bcsiMplsLspPathSelectMode.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiMplsLspPathSelectMode.setStatus(_A)
class _BcsiMplsLspPathSelectPathname_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_BcsiMplsLspPathSelectPathname_Type.__name__=_F
_BcsiMplsLspPathSelectPathname_Object=MibTableColumn
bcsiMplsLspPathSelectPathname=_BcsiMplsLspPathSelectPathname_Object((1,3,6,1,4,1,1588,3,1,10,1,2,3,1,31),_BcsiMplsLspPathSelectPathname_Type())
bcsiMplsLspPathSelectPathname.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiMplsLspPathSelectPathname.setStatus(_A)
class _BcsiMplsLspPathSelectRevertTimer_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BcsiMplsLspPathSelectRevertTimer_Type.__name__=_E
_BcsiMplsLspPathSelectRevertTimer_Object=MibTableColumn
bcsiMplsLspPathSelectRevertTimer=_BcsiMplsLspPathSelectRevertTimer_Object((1,3,6,1,4,1,1588,3,1,10,1,2,3,1,32),_BcsiMplsLspPathSelectRevertTimer_Type())
bcsiMplsLspPathSelectRevertTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiMplsLspPathSelectRevertTimer.setStatus(_A)
_BcsiMplsLspShortcutOspfAllowed_Type=TruthValue
_BcsiMplsLspShortcutOspfAllowed_Object=MibTableColumn
bcsiMplsLspShortcutOspfAllowed=_BcsiMplsLspShortcutOspfAllowed_Object((1,3,6,1,4,1,1588,3,1,10,1,2,3,1,33),_BcsiMplsLspShortcutOspfAllowed_Type())
bcsiMplsLspShortcutOspfAllowed.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiMplsLspShortcutOspfAllowed.setStatus(_A)
_BcsiMplsLspShortcutIsisAllowed_Type=TruthValue
_BcsiMplsLspShortcutIsisAllowed_Object=MibTableColumn
bcsiMplsLspShortcutIsisAllowed=_BcsiMplsLspShortcutIsisAllowed_Object((1,3,6,1,4,1,1588,3,1,10,1,2,3,1,34),_BcsiMplsLspShortcutIsisAllowed_Type())
bcsiMplsLspShortcutIsisAllowed.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiMplsLspShortcutIsisAllowed.setStatus(_A)
class _BcsiMplsLspShortcutIsisLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('level1',1),('level2',2),('level1and2',3)))
_BcsiMplsLspShortcutIsisLevel_Type.__name__=_C
_BcsiMplsLspShortcutIsisLevel_Object=MibTableColumn
bcsiMplsLspShortcutIsisLevel=_BcsiMplsLspShortcutIsisLevel_Object((1,3,6,1,4,1,1588,3,1,10,1,2,3,1,35),_BcsiMplsLspShortcutIsisLevel_Type())
bcsiMplsLspShortcutIsisLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiMplsLspShortcutIsisLevel.setStatus(_A)
_BcsiMplsLspShortcutIsisAnnounce_Type=TruthValue
_BcsiMplsLspShortcutIsisAnnounce_Object=MibTableColumn
bcsiMplsLspShortcutIsisAnnounce=_BcsiMplsLspShortcutIsisAnnounce_Object((1,3,6,1,4,1,1588,3,1,10,1,2,3,1,36),_BcsiMplsLspShortcutIsisAnnounce_Type())
bcsiMplsLspShortcutIsisAnnounce.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiMplsLspShortcutIsisAnnounce.setStatus(_A)
class _BcsiMplsLspShortcutIsisAnnounceMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16777215))
_BcsiMplsLspShortcutIsisAnnounceMetric_Type.__name__=_C
_BcsiMplsLspShortcutIsisAnnounceMetric_Object=MibTableColumn
bcsiMplsLspShortcutIsisAnnounceMetric=_BcsiMplsLspShortcutIsisAnnounceMetric_Object((1,3,6,1,4,1,1588,3,1,10,1,2,3,1,37),_BcsiMplsLspShortcutIsisAnnounceMetric_Type())
bcsiMplsLspShortcutIsisAnnounceMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiMplsLspShortcutIsisAnnounceMetric.setStatus(_A)
class _BcsiMplsLspShortcutIsisRelativeMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-16777215,16777215))
_BcsiMplsLspShortcutIsisRelativeMetric_Type.__name__=_C
_BcsiMplsLspShortcutIsisRelativeMetric_Object=MibTableColumn
bcsiMplsLspShortcutIsisRelativeMetric=_BcsiMplsLspShortcutIsisRelativeMetric_Object((1,3,6,1,4,1,1588,3,1,10,1,2,3,1,38),_BcsiMplsLspShortcutIsisRelativeMetric_Type())
bcsiMplsLspShortcutIsisRelativeMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiMplsLspShortcutIsisRelativeMetric.setStatus(_A)
_BcsiMplsVllInfo_ObjectIdentity=ObjectIdentity
bcsiMplsVllInfo=_BcsiMplsVllInfo_ObjectIdentity((1,3,6,1,4,1,1588,3,1,10,1,3))
_BcsiMplsVplsInfo_ObjectIdentity=ObjectIdentity
bcsiMplsVplsInfo=_BcsiMplsVplsInfo_ObjectIdentity((1,3,6,1,4,1,1588,3,1,10,1,4))
_BcsiMplsConformance_ObjectIdentity=ObjectIdentity
bcsiMplsConformance=_BcsiMplsConformance_ObjectIdentity((1,3,6,1,4,1,1588,3,1,10,2))
bcsiMplsLspUpNotification=NotificationType((1,3,6,1,4,1,1588,3,1,10,0,1))
bcsiMplsLspUpNotification.setObjects(*((_D,_I),(_D,_J)))
if mibBuilder.loadTexts:bcsiMplsLspUpNotification.setStatus(_A)
bcsiMplsLspDownNotification=NotificationType((1,3,6,1,4,1,1588,3,1,10,0,2))
bcsiMplsLspDownNotification.setObjects(*((_D,_I),(_D,_J)))
if mibBuilder.loadTexts:bcsiMplsLspDownNotification.setStatus(_A)
bcsiMplsLspChangeNotification=NotificationType((1,3,6,1,4,1,1588,3,1,10,0,3))
bcsiMplsLspChangeNotification.setObjects(*((_D,_I),(_D,_J)))
if mibBuilder.loadTexts:bcsiMplsLspChangeNotification.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'ClassOfService':ClassOfService,'brocadeMplsMIB':brocadeMplsMIB,'bcsiMplsNotifications':bcsiMplsNotifications,'bcsiMplsLspUpNotification':bcsiMplsLspUpNotification,'bcsiMplsLspDownNotification':bcsiMplsLspDownNotification,'bcsiMplsLspChangeNotification':bcsiMplsLspChangeNotification,'bcsiMplsObjects':bcsiMplsObjects,'bcsiMplsInfo':bcsiMplsInfo,'bcsiMplsVersion':bcsiMplsVersion,'bcsiMplsAdminGroupTable':bcsiMplsAdminGroupTable,'bcsiMplsAdminGroupEntry':bcsiMplsAdminGroupEntry,_K:bcsiMplsAdminGroupId,'bcsiMplsAdminGroupName':bcsiMplsAdminGroupName,'bcsiMplsAdminGroupRowStatus':bcsiMplsAdminGroupRowStatus,'bcsiMplsInterfaceTable':bcsiMplsInterfaceTable,'bcsiMplsInterfaceEntry':bcsiMplsInterfaceEntry,_L:bcsiMplsInterfaceIndex,'bcsiMplsInterfaceAdminGroup':bcsiMplsInterfaceAdminGroup,'bcsiMplsInterfaceRowStatus':bcsiMplsInterfaceRowStatus,'bcsiMplsLspInfo':bcsiMplsLspInfo,'bcsiMplsConfiguredLsps':bcsiMplsConfiguredLsps,'bcsiMplsActiveLsps':bcsiMplsActiveLsps,'bcsiMplsLspTable':bcsiMplsLspTable,'bcsiMplsLspEntry':bcsiMplsLspEntry,_N:bcsiMplsLspSignalingProto,_O:bcsiMplsLspIndex,_I:bcsiMplsLspName,'bcsiMplsLspState':bcsiMplsLspState,'bcsiMplsLspPackets':bcsiMplsLspPackets,'bcsiMplsLspAge':bcsiMplsLspAge,'bcsiMplsLspTimeUp':bcsiMplsLspTimeUp,'bcsiMplsLspPrimaryTimeUp':bcsiMplsLspPrimaryTimeUp,'bcsiMplsLspTransitions':bcsiMplsLspTransitions,'bcsiMplsLspLastTransition':bcsiMplsLspLastTransition,'bcsiMplsLspFrom':bcsiMplsLspFrom,'bcsiMplsLspTo':bcsiMplsLspTo,_J:bcsiMplsLspPathName,'bcsiMplsLspPathType':bcsiMplsLspPathType,'bcsiMplsLspAdaptive':bcsiMplsLspAdaptive,'bcsiMplsLspBfdSessionId':bcsiMplsLspBfdSessionId,'bcsiMplsLspReoptimizeTimer':bcsiMplsLspReoptimizeTimer,'bcsiMplsLspCoS':bcsiMplsLspCoS,'bcsiMplsLspHopLimit':bcsiMplsLspHopLimit,'bcsiMplsLspCspf':bcsiMplsLspCspf,'bcsiMplsLspCspfTieBreaker':bcsiMplsLspCspfTieBreaker,'bcsiMplsLspFrrMode':bcsiMplsLspFrrMode,'bcsiMplsLspFrrSetupPriority':bcsiMplsLspFrrSetupPriority,'bcsiMplsLspFrrHoldingPriority':bcsiMplsLspFrrHoldingPriority,'bcsiMplsLspFrrHopLimit':bcsiMplsLspFrrHopLimit,'bcsiMplsLspFrrBandwidth':bcsiMplsLspFrrBandwidth,'bcsiMplsLspFrrAdmGrpIncludeAny':bcsiMplsLspFrrAdmGrpIncludeAny,'bcsiMplsLspFrrAdmGrpIncludeAll':bcsiMplsLspFrrAdmGrpIncludeAll,'bcsiMplsLspFrrAdmGrpExcludeAny':bcsiMplsLspFrrAdmGrpExcludeAny,'bcsiMplsLspPathSelectMode':bcsiMplsLspPathSelectMode,'bcsiMplsLspPathSelectPathname':bcsiMplsLspPathSelectPathname,'bcsiMplsLspPathSelectRevertTimer':bcsiMplsLspPathSelectRevertTimer,'bcsiMplsLspShortcutOspfAllowed':bcsiMplsLspShortcutOspfAllowed,'bcsiMplsLspShortcutIsisAllowed':bcsiMplsLspShortcutIsisAllowed,'bcsiMplsLspShortcutIsisLevel':bcsiMplsLspShortcutIsisLevel,'bcsiMplsLspShortcutIsisAnnounce':bcsiMplsLspShortcutIsisAnnounce,'bcsiMplsLspShortcutIsisAnnounceMetric':bcsiMplsLspShortcutIsisAnnounceMetric,'bcsiMplsLspShortcutIsisRelativeMetric':bcsiMplsLspShortcutIsisRelativeMetric,'bcsiMplsVllInfo':bcsiMplsVllInfo,'bcsiMplsVplsInfo':bcsiMplsVplsInfo,'bcsiMplsConformance':bcsiMplsConformance})