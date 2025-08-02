_Z='fast-reroute'
_Y='preemptive'
_X='preemptable'
_W='mergeable'
_V='adaptive'
_U='record-route'
_T='bypass'
_S='secondary'
_R='standby'
_Q='primary'
_P='backupActive'
_O='notInService'
_N='unknown'
_M='mplsAdminGroupNumber'
_L='other'
_K='mplsPathName'
_J='mplsPathInfoName'
_I='DisplayString'
_H='OctetString'
_G='mplsLspInfoName'
_F='mplsLspName'
_E='Integer32'
_D='MPLS-MIB'
_C='deprecated'
_B='current'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
jnxMibs,=mibBuilder.importSymbols('JUNIPER-SMI','jnxMibs')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','TextualConvention','TimeStamp')
mpls=ModuleIdentity((1,3,6,1,4,1,2636,3,2))
if mibBuilder.loadTexts:mpls.setRevisions(('2009-02-23 14:45',))
_MplsLspTraps_ObjectIdentity=ObjectIdentity
mplsLspTraps=_MplsLspTraps_ObjectIdentity((1,3,6,1,4,1,2636,3,2,0))
_MplsInfo_ObjectIdentity=ObjectIdentity
mplsInfo=_MplsInfo_ObjectIdentity((1,3,6,1,4,1,2636,3,2,1))
_MplsVersion_Type=Integer32
_MplsVersion_Object=MibScalar
mplsVersion=_MplsVersion_Object((1,3,6,1,4,1,2636,3,2,1,1),_MplsVersion_Type())
mplsVersion.setMaxAccess(_A)
if mibBuilder.loadTexts:mplsVersion.setStatus(_B)
class _MplsSignalingProto_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),(_L,2),('rsvp',3),('ldp',4)))
_MplsSignalingProto_Type.__name__=_E
_MplsSignalingProto_Object=MibScalar
mplsSignalingProto=_MplsSignalingProto_Object((1,3,6,1,4,1,2636,3,2,1,2),_MplsSignalingProto_Type())
mplsSignalingProto.setMaxAccess(_A)
if mibBuilder.loadTexts:mplsSignalingProto.setStatus(_B)
_MplsConfiguredLsps_Type=Integer32
_MplsConfiguredLsps_Object=MibScalar
mplsConfiguredLsps=_MplsConfiguredLsps_Object((1,3,6,1,4,1,2636,3,2,1,3),_MplsConfiguredLsps_Type())
mplsConfiguredLsps.setMaxAccess(_A)
if mibBuilder.loadTexts:mplsConfiguredLsps.setStatus(_B)
_MplsActiveLsps_Type=Integer32
_MplsActiveLsps_Object=MibScalar
mplsActiveLsps=_MplsActiveLsps_Object((1,3,6,1,4,1,2636,3,2,1,4),_MplsActiveLsps_Type())
mplsActiveLsps.setMaxAccess(_A)
if mibBuilder.loadTexts:mplsActiveLsps.setStatus(_B)
_MplsTEInfo_ObjectIdentity=ObjectIdentity
mplsTEInfo=_MplsTEInfo_ObjectIdentity((1,3,6,1,4,1,2636,3,2,2))
class _MplsTEDistProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('isis',2),('ospf',3),('isis-ospf',4)))
_MplsTEDistProtocol_Type.__name__=_E
_MplsTEDistProtocol_Object=MibScalar
mplsTEDistProtocol=_MplsTEDistProtocol_Object((1,3,6,1,4,1,2636,3,2,2,1),_MplsTEDistProtocol_Type())
mplsTEDistProtocol.setMaxAccess(_A)
if mibBuilder.loadTexts:mplsTEDistProtocol.setStatus(_B)
_MplsAdminGroupList_Object=MibTable
mplsAdminGroupList=_MplsAdminGroupList_Object((1,3,6,1,4,1,2636,3,2,2,2))
if mibBuilder.loadTexts:mplsAdminGroupList.setStatus(_B)
_MplsAdminGroup_Object=MibTableRow
mplsAdminGroup=_MplsAdminGroup_Object((1,3,6,1,4,1,2636,3,2,2,2,1))
mplsAdminGroup.setIndexNames((0,_D,_M))
if mibBuilder.loadTexts:mplsAdminGroup.setStatus(_B)
class _MplsAdminGroupNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_MplsAdminGroupNumber_Type.__name__=_E
_MplsAdminGroupNumber_Object=MibTableColumn
mplsAdminGroupNumber=_MplsAdminGroupNumber_Object((1,3,6,1,4,1,2636,3,2,2,2,1,1),_MplsAdminGroupNumber_Type())
mplsAdminGroupNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:mplsAdminGroupNumber.setStatus(_B)
class _MplsAdminGroupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_MplsAdminGroupName_Type.__name__=_I
_MplsAdminGroupName_Object=MibTableColumn
mplsAdminGroupName=_MplsAdminGroupName_Object((1,3,6,1,4,1,2636,3,2,2,2,1,2),_MplsAdminGroupName_Type())
mplsAdminGroupName.setMaxAccess(_A)
if mibBuilder.loadTexts:mplsAdminGroupName.setStatus(_B)
_MplsLspList_Object=MibTable
mplsLspList=_MplsLspList_Object((1,3,6,1,4,1,2636,3,2,3))
if mibBuilder.loadTexts:mplsLspList.setStatus(_C)
_MplsLspEntry_Object=MibTableRow
mplsLspEntry=_MplsLspEntry_Object((1,3,6,1,4,1,2636,3,2,3,1))
mplsLspEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:mplsLspEntry.setStatus(_C)
class _MplsLspName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_MplsLspName_Type.__name__=_I
_MplsLspName_Object=MibTableColumn
mplsLspName=_MplsLspName_Object((1,3,6,1,4,1,2636,3,2,3,1,1),_MplsLspName_Type())
mplsLspName.setMaxAccess(_A)
if mibBuilder.loadTexts:mplsLspName.setStatus(_C)
class _MplsLspState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_N,1),('up',2),('down',3),(_O,4),(_P,5)))
_MplsLspState_Type.__name__=_E
_MplsLspState_Object=MibTableColumn
mplsLspState=_MplsLspState_Object((1,3,6,1,4,1,2636,3,2,3,1,2),_MplsLspState_Type())
mplsLspState.setMaxAccess(_A)
if mibBuilder.loadTexts:mplsLspState.setStatus(_C)
_MplsLspOctets_Type=Counter64
_MplsLspOctets_Object=MibTableColumn
mplsLspOctets=_MplsLspOctets_Object((1,3,6,1,4,1,2636,3,2,3,1,3),_MplsLspOctets_Type())
mplsLspOctets.setMaxAccess(_A)
if mibBuilder.loadTexts:mplsLspOctets.setStatus(_C)
_MplsLspPackets_Type=Counter64
_MplsLspPackets_Object=MibTableColumn
mplsLspPackets=_MplsLspPackets_Object((1,3,6,1,4,1,2636,3,2,3,1,4),_MplsLspPackets_Type())
mplsLspPackets.setMaxAccess(_A)
if mibBuilder.loadTexts:mplsLspPackets.setStatus(_C)
_MplsLspAge_Type=TimeStamp
_MplsLspAge_Object=MibTableColumn
mplsLspAge=_MplsLspAge_Object((1,3,6,1,4,1,2636,3,2,3,1,5),_MplsLspAge_Type())
mplsLspAge.setMaxAccess(_A)
if mibBuilder.loadTexts:mplsLspAge.setStatus(_C)
_MplsLspTimeUp_Type=TimeStamp
_MplsLspTimeUp_Object=MibTableColumn
mplsLspTimeUp=_MplsLspTimeUp_Object((1,3,6,1,4,1,2636,3,2,3,1,6),_MplsLspTimeUp_Type())
mplsLspTimeUp.setMaxAccess(_A)
if mibBuilder.loadTexts:mplsLspTimeUp.setStatus(_C)
_MplsLspPrimaryTimeUp_Type=TimeStamp
_MplsLspPrimaryTimeUp_Object=MibTableColumn
mplsLspPrimaryTimeUp=_MplsLspPrimaryTimeUp_Object((1,3,6,1,4,1,2636,3,2,3,1,7),_MplsLspPrimaryTimeUp_Type())
mplsLspPrimaryTimeUp.setMaxAccess(_A)
if mibBuilder.loadTexts:mplsLspPrimaryTimeUp.setStatus(_C)
_MplsLspTransitions_Type=Counter32
_MplsLspTransitions_Object=MibTableColumn
mplsLspTransitions=_MplsLspTransitions_Object((1,3,6,1,4,1,2636,3,2,3,1,8),_MplsLspTransitions_Type())
mplsLspTransitions.setMaxAccess(_A)
if mibBuilder.loadTexts:mplsLspTransitions.setStatus(_C)
_MplsLspLastTransition_Type=TimeStamp
_MplsLspLastTransition_Object=MibTableColumn
mplsLspLastTransition=_MplsLspLastTransition_Object((1,3,6,1,4,1,2636,3,2,3,1,9),_MplsLspLastTransition_Type())
mplsLspLastTransition.setMaxAccess(_A)
if mibBuilder.loadTexts:mplsLspLastTransition.setStatus(_C)
_MplsLspPathChanges_Type=Counter32
_MplsLspPathChanges_Object=MibTableColumn
mplsLspPathChanges=_MplsLspPathChanges_Object((1,3,6,1,4,1,2636,3,2,3,1,10),_MplsLspPathChanges_Type())
mplsLspPathChanges.setMaxAccess(_A)
if mibBuilder.loadTexts:mplsLspPathChanges.setStatus(_C)
_MplsLspLastPathChange_Type=TimeStamp
_MplsLspLastPathChange_Object=MibTableColumn
mplsLspLastPathChange=_MplsLspLastPathChange_Object((1,3,6,1,4,1,2636,3,2,3,1,11),_MplsLspLastPathChange_Type())
mplsLspLastPathChange.setMaxAccess(_A)
if mibBuilder.loadTexts:mplsLspLastPathChange.setStatus(_C)
_MplsLspConfiguredPaths_Type=Integer32
_MplsLspConfiguredPaths_Object=MibTableColumn
mplsLspConfiguredPaths=_MplsLspConfiguredPaths_Object((1,3,6,1,4,1,2636,3,2,3,1,12),_MplsLspConfiguredPaths_Type())
mplsLspConfiguredPaths.setMaxAccess(_A)
if mibBuilder.loadTexts:mplsLspConfiguredPaths.setStatus(_C)
_MplsLspStandbyPaths_Type=Integer32
_MplsLspStandbyPaths_Object=MibTableColumn
mplsLspStandbyPaths=_MplsLspStandbyPaths_Object((1,3,6,1,4,1,2636,3,2,3,1,13),_MplsLspStandbyPaths_Type())
mplsLspStandbyPaths.setMaxAccess(_A)
if mibBuilder.loadTexts:mplsLspStandbyPaths.setStatus(_C)
_MplsLspOperationalPaths_Type=Integer32
_MplsLspOperationalPaths_Object=MibTableColumn
mplsLspOperationalPaths=_MplsLspOperationalPaths_Object((1,3,6,1,4,1,2636,3,2,3,1,14),_MplsLspOperationalPaths_Type())
mplsLspOperationalPaths.setMaxAccess(_A)
if mibBuilder.loadTexts:mplsLspOperationalPaths.setStatus(_C)
_MplsLspFrom_Type=IpAddress
_MplsLspFrom_Object=MibTableColumn
mplsLspFrom=_MplsLspFrom_Object((1,3,6,1,4,1,2636,3,2,3,1,15),_MplsLspFrom_Type())
mplsLspFrom.setMaxAccess(_A)
if mibBuilder.loadTexts:mplsLspFrom.setStatus(_C)
_MplsLspTo_Type=IpAddress
_MplsLspTo_Object=MibTableColumn
mplsLspTo=_MplsLspTo_Object((1,3,6,1,4,1,2636,3,2,3,1,16),_MplsLspTo_Type())
mplsLspTo.setMaxAccess(_A)
if mibBuilder.loadTexts:mplsLspTo.setStatus(_C)
class _MplsPathName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_MplsPathName_Type.__name__=_I
_MplsPathName_Object=MibTableColumn
mplsPathName=_MplsPathName_Object((1,3,6,1,4,1,2636,3,2,3,1,17),_MplsPathName_Type())
mplsPathName.setMaxAccess(_A)
if mibBuilder.loadTexts:mplsPathName.setStatus(_C)
class _MplsPathType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_L,1),(_Q,2),(_R,3),(_S,4),(_T,5)))
_MplsPathType_Type.__name__=_E
_MplsPathType_Object=MibTableColumn
mplsPathType=_MplsPathType_Object((1,3,6,1,4,1,2636,3,2,3,1,18),_MplsPathType_Type())
mplsPathType.setMaxAccess(_A)
if mibBuilder.loadTexts:mplsPathType.setStatus(_C)
class _MplsPathExplicitRoute_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_MplsPathExplicitRoute_Type.__name__=_H
_MplsPathExplicitRoute_Object=MibTableColumn
mplsPathExplicitRoute=_MplsPathExplicitRoute_Object((1,3,6,1,4,1,2636,3,2,3,1,19),_MplsPathExplicitRoute_Type())
mplsPathExplicitRoute.setMaxAccess(_A)
if mibBuilder.loadTexts:mplsPathExplicitRoute.setStatus(_C)
class _MplsPathRecordRoute_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_MplsPathRecordRoute_Type.__name__=_H
_MplsPathRecordRoute_Object=MibTableColumn
mplsPathRecordRoute=_MplsPathRecordRoute_Object((1,3,6,1,4,1,2636,3,2,3,1,20),_MplsPathRecordRoute_Type())
mplsPathRecordRoute.setMaxAccess(_A)
if mibBuilder.loadTexts:mplsPathRecordRoute.setStatus(_C)
_MplsPathBandwidth_Type=Integer32
_MplsPathBandwidth_Object=MibTableColumn
mplsPathBandwidth=_MplsPathBandwidth_Object((1,3,6,1,4,1,2636,3,2,3,1,21),_MplsPathBandwidth_Type())
mplsPathBandwidth.setMaxAccess(_A)
if mibBuilder.loadTexts:mplsPathBandwidth.setStatus(_C)
class _MplsPathCOS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_MplsPathCOS_Type.__name__=_E
_MplsPathCOS_Object=MibTableColumn
mplsPathCOS=_MplsPathCOS_Object((1,3,6,1,4,1,2636,3,2,3,1,22),_MplsPathCOS_Type())
mplsPathCOS.setMaxAccess(_A)
if mibBuilder.loadTexts:mplsPathCOS.setStatus(_C)
_MplsPathInclude_Type=Integer32
_MplsPathInclude_Object=MibTableColumn
mplsPathInclude=_MplsPathInclude_Object((1,3,6,1,4,1,2636,3,2,3,1,23),_MplsPathInclude_Type())
mplsPathInclude.setMaxAccess(_A)
if mibBuilder.loadTexts:mplsPathInclude.setStatus(_C)
_MplsPathExclude_Type=Integer32
_MplsPathExclude_Object=MibTableColumn
mplsPathExclude=_MplsPathExclude_Object((1,3,6,1,4,1,2636,3,2,3,1,24),_MplsPathExclude_Type())
mplsPathExclude.setMaxAccess(_A)
if mibBuilder.loadTexts:mplsPathExclude.setStatus(_C)
class _MplsPathSetupPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_MplsPathSetupPriority_Type.__name__=_E
_MplsPathSetupPriority_Object=MibTableColumn
mplsPathSetupPriority=_MplsPathSetupPriority_Object((1,3,6,1,4,1,2636,3,2,3,1,25),_MplsPathSetupPriority_Type())
mplsPathSetupPriority.setMaxAccess(_A)
if mibBuilder.loadTexts:mplsPathSetupPriority.setStatus(_C)
class _MplsPathHoldPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_MplsPathHoldPriority_Type.__name__=_E
_MplsPathHoldPriority_Object=MibTableColumn
mplsPathHoldPriority=_MplsPathHoldPriority_Object((1,3,6,1,4,1,2636,3,2,3,1,26),_MplsPathHoldPriority_Type())
mplsPathHoldPriority.setMaxAccess(_A)
if mibBuilder.loadTexts:mplsPathHoldPriority.setStatus(_C)
class _MplsPathProperties_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,8,16,32,64)));namedValues=NamedValues(*((_U,1),(_V,2),('cspf',4),(_W,8),(_X,16),(_Y,32),(_Z,64)))
_MplsPathProperties_Type.__name__=_E
_MplsPathProperties_Object=MibTableColumn
mplsPathProperties=_MplsPathProperties_Object((1,3,6,1,4,1,2636,3,2,3,1,27),_MplsPathProperties_Type())
mplsPathProperties.setMaxAccess(_A)
if mibBuilder.loadTexts:mplsPathProperties.setStatus(_C)
_MplsTraps_ObjectIdentity=ObjectIdentity
mplsTraps=_MplsTraps_ObjectIdentity((1,3,6,1,4,1,2636,3,2,4))
_MplsLspInfoList_Object=MibTable
mplsLspInfoList=_MplsLspInfoList_Object((1,3,6,1,4,1,2636,3,2,5))
if mibBuilder.loadTexts:mplsLspInfoList.setStatus(_B)
_MplsLspInfoEntry_Object=MibTableRow
mplsLspInfoEntry=_MplsLspInfoEntry_Object((1,3,6,1,4,1,2636,3,2,5,1))
mplsLspInfoEntry.setIndexNames((1,_D,_G))
if mibBuilder.loadTexts:mplsLspInfoEntry.setStatus(_B)
class _MplsLspInfoName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_MplsLspInfoName_Type.__name__=_I
_MplsLspInfoName_Object=MibTableColumn
mplsLspInfoName=_MplsLspInfoName_Object((1,3,6,1,4,1,2636,3,2,5,1,1),_MplsLspInfoName_Type())
mplsLspInfoName.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:mplsLspInfoName.setStatus(_B)
class _MplsLspInfoState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_N,1),('up',2),('down',3),(_O,4),(_P,5)))
_MplsLspInfoState_Type.__name__=_E
_MplsLspInfoState_Object=MibTableColumn
mplsLspInfoState=_MplsLspInfoState_Object((1,3,6,1,4,1,2636,3,2,5,1,2),_MplsLspInfoState_Type())
mplsLspInfoState.setMaxAccess(_A)
if mibBuilder.loadTexts:mplsLspInfoState.setStatus(_B)
_MplsLspInfoOctets_Type=Counter64
_MplsLspInfoOctets_Object=MibTableColumn
mplsLspInfoOctets=_MplsLspInfoOctets_Object((1,3,6,1,4,1,2636,3,2,5,1,3),_MplsLspInfoOctets_Type())
mplsLspInfoOctets.setMaxAccess(_A)
if mibBuilder.loadTexts:mplsLspInfoOctets.setStatus(_B)
_MplsLspInfoPackets_Type=Counter64
_MplsLspInfoPackets_Object=MibTableColumn
mplsLspInfoPackets=_MplsLspInfoPackets_Object((1,3,6,1,4,1,2636,3,2,5,1,4),_MplsLspInfoPackets_Type())
mplsLspInfoPackets.setMaxAccess(_A)
if mibBuilder.loadTexts:mplsLspInfoPackets.setStatus(_B)
_MplsLspInfoAge_Type=TimeStamp
_MplsLspInfoAge_Object=MibTableColumn
mplsLspInfoAge=_MplsLspInfoAge_Object((1,3,6,1,4,1,2636,3,2,5,1,5),_MplsLspInfoAge_Type())
mplsLspInfoAge.setMaxAccess(_A)
if mibBuilder.loadTexts:mplsLspInfoAge.setStatus(_B)
_MplsLspInfoTimeUp_Type=TimeStamp
_MplsLspInfoTimeUp_Object=MibTableColumn
mplsLspInfoTimeUp=_MplsLspInfoTimeUp_Object((1,3,6,1,4,1,2636,3,2,5,1,6),_MplsLspInfoTimeUp_Type())
mplsLspInfoTimeUp.setMaxAccess(_A)
if mibBuilder.loadTexts:mplsLspInfoTimeUp.setStatus(_B)
_MplsLspInfoPrimaryTimeUp_Type=TimeStamp
_MplsLspInfoPrimaryTimeUp_Object=MibTableColumn
mplsLspInfoPrimaryTimeUp=_MplsLspInfoPrimaryTimeUp_Object((1,3,6,1,4,1,2636,3,2,5,1,7),_MplsLspInfoPrimaryTimeUp_Type())
mplsLspInfoPrimaryTimeUp.setMaxAccess(_A)
if mibBuilder.loadTexts:mplsLspInfoPrimaryTimeUp.setStatus(_B)
_MplsLspInfoTransitions_Type=Counter32
_MplsLspInfoTransitions_Object=MibTableColumn
mplsLspInfoTransitions=_MplsLspInfoTransitions_Object((1,3,6,1,4,1,2636,3,2,5,1,8),_MplsLspInfoTransitions_Type())
mplsLspInfoTransitions.setMaxAccess(_A)
if mibBuilder.loadTexts:mplsLspInfoTransitions.setStatus(_B)
_MplsLspInfoLastTransition_Type=TimeStamp
_MplsLspInfoLastTransition_Object=MibTableColumn
mplsLspInfoLastTransition=_MplsLspInfoLastTransition_Object((1,3,6,1,4,1,2636,3,2,5,1,9),_MplsLspInfoLastTransition_Type())
mplsLspInfoLastTransition.setMaxAccess(_A)
if mibBuilder.loadTexts:mplsLspInfoLastTransition.setStatus(_B)
_MplsLspInfoPathChanges_Type=Counter32
_MplsLspInfoPathChanges_Object=MibTableColumn
mplsLspInfoPathChanges=_MplsLspInfoPathChanges_Object((1,3,6,1,4,1,2636,3,2,5,1,10),_MplsLspInfoPathChanges_Type())
mplsLspInfoPathChanges.setMaxAccess(_A)
if mibBuilder.loadTexts:mplsLspInfoPathChanges.setStatus(_B)
_MplsLspInfoLastPathChange_Type=TimeStamp
_MplsLspInfoLastPathChange_Object=MibTableColumn
mplsLspInfoLastPathChange=_MplsLspInfoLastPathChange_Object((1,3,6,1,4,1,2636,3,2,5,1,11),_MplsLspInfoLastPathChange_Type())
mplsLspInfoLastPathChange.setMaxAccess(_A)
if mibBuilder.loadTexts:mplsLspInfoLastPathChange.setStatus(_B)
_MplsLspInfoConfiguredPaths_Type=Integer32
_MplsLspInfoConfiguredPaths_Object=MibTableColumn
mplsLspInfoConfiguredPaths=_MplsLspInfoConfiguredPaths_Object((1,3,6,1,4,1,2636,3,2,5,1,12),_MplsLspInfoConfiguredPaths_Type())
mplsLspInfoConfiguredPaths.setMaxAccess(_A)
if mibBuilder.loadTexts:mplsLspInfoConfiguredPaths.setStatus(_B)
_MplsLspInfoStandbyPaths_Type=Integer32
_MplsLspInfoStandbyPaths_Object=MibTableColumn
mplsLspInfoStandbyPaths=_MplsLspInfoStandbyPaths_Object((1,3,6,1,4,1,2636,3,2,5,1,13),_MplsLspInfoStandbyPaths_Type())
mplsLspInfoStandbyPaths.setMaxAccess(_A)
if mibBuilder.loadTexts:mplsLspInfoStandbyPaths.setStatus(_B)
_MplsLspInfoOperationalPaths_Type=Integer32
_MplsLspInfoOperationalPaths_Object=MibTableColumn
mplsLspInfoOperationalPaths=_MplsLspInfoOperationalPaths_Object((1,3,6,1,4,1,2636,3,2,5,1,14),_MplsLspInfoOperationalPaths_Type())
mplsLspInfoOperationalPaths.setMaxAccess(_A)
if mibBuilder.loadTexts:mplsLspInfoOperationalPaths.setStatus(_B)
_MplsLspInfoFrom_Type=IpAddress
_MplsLspInfoFrom_Object=MibTableColumn
mplsLspInfoFrom=_MplsLspInfoFrom_Object((1,3,6,1,4,1,2636,3,2,5,1,15),_MplsLspInfoFrom_Type())
mplsLspInfoFrom.setMaxAccess(_A)
if mibBuilder.loadTexts:mplsLspInfoFrom.setStatus(_B)
_MplsLspInfoTo_Type=IpAddress
_MplsLspInfoTo_Object=MibTableColumn
mplsLspInfoTo=_MplsLspInfoTo_Object((1,3,6,1,4,1,2636,3,2,5,1,16),_MplsLspInfoTo_Type())
mplsLspInfoTo.setMaxAccess(_A)
if mibBuilder.loadTexts:mplsLspInfoTo.setStatus(_B)
class _MplsPathInfoName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_MplsPathInfoName_Type.__name__=_I
_MplsPathInfoName_Object=MibTableColumn
mplsPathInfoName=_MplsPathInfoName_Object((1,3,6,1,4,1,2636,3,2,5,1,17),_MplsPathInfoName_Type())
mplsPathInfoName.setMaxAccess(_A)
if mibBuilder.loadTexts:mplsPathInfoName.setStatus(_B)
class _MplsPathInfoType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_L,1),(_Q,2),(_R,3),(_S,4),(_T,5)))
_MplsPathInfoType_Type.__name__=_E
_MplsPathInfoType_Object=MibTableColumn
mplsPathInfoType=_MplsPathInfoType_Object((1,3,6,1,4,1,2636,3,2,5,1,18),_MplsPathInfoType_Type())
mplsPathInfoType.setMaxAccess(_A)
if mibBuilder.loadTexts:mplsPathInfoType.setStatus(_B)
class _MplsPathInfoExplicitRoute_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_MplsPathInfoExplicitRoute_Type.__name__=_H
_MplsPathInfoExplicitRoute_Object=MibTableColumn
mplsPathInfoExplicitRoute=_MplsPathInfoExplicitRoute_Object((1,3,6,1,4,1,2636,3,2,5,1,19),_MplsPathInfoExplicitRoute_Type())
mplsPathInfoExplicitRoute.setMaxAccess(_A)
if mibBuilder.loadTexts:mplsPathInfoExplicitRoute.setStatus(_B)
class _MplsPathInfoRecordRoute_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_MplsPathInfoRecordRoute_Type.__name__=_H
_MplsPathInfoRecordRoute_Object=MibTableColumn
mplsPathInfoRecordRoute=_MplsPathInfoRecordRoute_Object((1,3,6,1,4,1,2636,3,2,5,1,20),_MplsPathInfoRecordRoute_Type())
mplsPathInfoRecordRoute.setMaxAccess(_A)
if mibBuilder.loadTexts:mplsPathInfoRecordRoute.setStatus(_B)
_MplsPathInfoBandwidth_Type=Integer32
_MplsPathInfoBandwidth_Object=MibTableColumn
mplsPathInfoBandwidth=_MplsPathInfoBandwidth_Object((1,3,6,1,4,1,2636,3,2,5,1,21),_MplsPathInfoBandwidth_Type())
mplsPathInfoBandwidth.setMaxAccess(_A)
if mibBuilder.loadTexts:mplsPathInfoBandwidth.setStatus(_B)
class _MplsPathInfoCOS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_MplsPathInfoCOS_Type.__name__=_E
_MplsPathInfoCOS_Object=MibTableColumn
mplsPathInfoCOS=_MplsPathInfoCOS_Object((1,3,6,1,4,1,2636,3,2,5,1,22),_MplsPathInfoCOS_Type())
mplsPathInfoCOS.setMaxAccess(_A)
if mibBuilder.loadTexts:mplsPathInfoCOS.setStatus(_B)
_MplsPathInfoInclude_Type=Integer32
_MplsPathInfoInclude_Object=MibTableColumn
mplsPathInfoInclude=_MplsPathInfoInclude_Object((1,3,6,1,4,1,2636,3,2,5,1,23),_MplsPathInfoInclude_Type())
mplsPathInfoInclude.setMaxAccess(_A)
if mibBuilder.loadTexts:mplsPathInfoInclude.setStatus(_B)
_MplsPathInfoExclude_Type=Integer32
_MplsPathInfoExclude_Object=MibTableColumn
mplsPathInfoExclude=_MplsPathInfoExclude_Object((1,3,6,1,4,1,2636,3,2,5,1,24),_MplsPathInfoExclude_Type())
mplsPathInfoExclude.setMaxAccess(_A)
if mibBuilder.loadTexts:mplsPathInfoExclude.setStatus(_B)
class _MplsPathInfoSetupPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_MplsPathInfoSetupPriority_Type.__name__=_E
_MplsPathInfoSetupPriority_Object=MibTableColumn
mplsPathInfoSetupPriority=_MplsPathInfoSetupPriority_Object((1,3,6,1,4,1,2636,3,2,5,1,25),_MplsPathInfoSetupPriority_Type())
mplsPathInfoSetupPriority.setMaxAccess(_A)
if mibBuilder.loadTexts:mplsPathInfoSetupPriority.setStatus(_B)
class _MplsPathInfoHoldPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_MplsPathInfoHoldPriority_Type.__name__=_E
_MplsPathInfoHoldPriority_Object=MibTableColumn
mplsPathInfoHoldPriority=_MplsPathInfoHoldPriority_Object((1,3,6,1,4,1,2636,3,2,5,1,26),_MplsPathInfoHoldPriority_Type())
mplsPathInfoHoldPriority.setMaxAccess(_A)
if mibBuilder.loadTexts:mplsPathInfoHoldPriority.setStatus(_B)
class _MplsPathInfoProperties_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,8,16,32,64)));namedValues=NamedValues(*((_U,1),(_V,2),('cspf',4),(_W,8),(_X,16),(_Y,32),(_Z,64)))
_MplsPathInfoProperties_Type.__name__=_E
_MplsPathInfoProperties_Object=MibTableColumn
mplsPathInfoProperties=_MplsPathInfoProperties_Object((1,3,6,1,4,1,2636,3,2,5,1,27),_MplsPathInfoProperties_Type())
mplsPathInfoProperties.setMaxAccess(_A)
if mibBuilder.loadTexts:mplsPathInfoProperties.setStatus(_B)
_MplsLspInfoAggrOctets_Type=Counter64
_MplsLspInfoAggrOctets_Object=MibTableColumn
mplsLspInfoAggrOctets=_MplsLspInfoAggrOctets_Object((1,3,6,1,4,1,2636,3,2,5,1,28),_MplsLspInfoAggrOctets_Type())
mplsLspInfoAggrOctets.setMaxAccess(_A)
if mibBuilder.loadTexts:mplsLspInfoAggrOctets.setStatus(_B)
_MplsLspInfoAggrPackets_Type=Counter64
_MplsLspInfoAggrPackets_Object=MibTableColumn
mplsLspInfoAggrPackets=_MplsLspInfoAggrPackets_Object((1,3,6,1,4,1,2636,3,2,5,1,29),_MplsLspInfoAggrPackets_Type())
mplsLspInfoAggrPackets.setMaxAccess(_A)
if mibBuilder.loadTexts:mplsLspInfoAggrPackets.setStatus(_B)
class _MplsPathInfoRecordRouteWithLabels_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_MplsPathInfoRecordRouteWithLabels_Type.__name__=_H
_MplsPathInfoRecordRouteWithLabels_Object=MibTableColumn
mplsPathInfoRecordRouteWithLabels=_MplsPathInfoRecordRouteWithLabels_Object((1,3,6,1,4,1,2636,3,2,5,1,30),_MplsPathInfoRecordRouteWithLabels_Type())
mplsPathInfoRecordRouteWithLabels.setMaxAccess(_A)
if mibBuilder.loadTexts:mplsPathInfoRecordRouteWithLabels.setStatus(_B)
mplsLspInfoUp=NotificationType((1,3,6,1,4,1,2636,3,2,0,1))
mplsLspInfoUp.setObjects(*((_D,_G),(_D,_J)))
if mibBuilder.loadTexts:mplsLspInfoUp.setStatus(_B)
mplsLspInfoDown=NotificationType((1,3,6,1,4,1,2636,3,2,0,2))
mplsLspInfoDown.setObjects(*((_D,_G),(_D,_J)))
if mibBuilder.loadTexts:mplsLspInfoDown.setStatus(_B)
mplsLspInfoChange=NotificationType((1,3,6,1,4,1,2636,3,2,0,3))
mplsLspInfoChange.setObjects(*((_D,_G),(_D,_J)))
if mibBuilder.loadTexts:mplsLspInfoChange.setStatus(_B)
mplsLspInfoPathDown=NotificationType((1,3,6,1,4,1,2636,3,2,0,4))
mplsLspInfoPathDown.setObjects(*((_D,_G),(_D,_J)))
if mibBuilder.loadTexts:mplsLspInfoPathDown.setStatus(_B)
mplsLspInfoPathUp=NotificationType((1,3,6,1,4,1,2636,3,2,0,5))
mplsLspInfoPathUp.setObjects(*((_D,_G),(_D,_J)))
if mibBuilder.loadTexts:mplsLspInfoPathUp.setStatus(_B)
mplsLspUp=NotificationType((1,3,6,1,4,1,2636,3,2,4,1))
mplsLspUp.setObjects(*((_D,_F),(_D,_K)))
if mibBuilder.loadTexts:mplsLspUp.setStatus(_C)
mplsLspDown=NotificationType((1,3,6,1,4,1,2636,3,2,4,2))
mplsLspDown.setObjects(*((_D,_F),(_D,_K)))
if mibBuilder.loadTexts:mplsLspDown.setStatus(_C)
mplsLspChange=NotificationType((1,3,6,1,4,1,2636,3,2,4,3))
mplsLspChange.setObjects(*((_D,_F),(_D,_K)))
if mibBuilder.loadTexts:mplsLspChange.setStatus(_C)
mplsLspPathDown=NotificationType((1,3,6,1,4,1,2636,3,2,4,4))
mplsLspPathDown.setObjects(*((_D,_F),(_D,_K)))
if mibBuilder.loadTexts:mplsLspPathDown.setStatus(_C)
mplsLspPathUp=NotificationType((1,3,6,1,4,1,2636,3,2,4,5))
mplsLspPathUp.setObjects(*((_D,_F),(_D,_K)))
if mibBuilder.loadTexts:mplsLspPathUp.setStatus(_C)
mibBuilder.exportSymbols(_D,**{'mpls':mpls,'mplsLspTraps':mplsLspTraps,'mplsLspInfoUp':mplsLspInfoUp,'mplsLspInfoDown':mplsLspInfoDown,'mplsLspInfoChange':mplsLspInfoChange,'mplsLspInfoPathDown':mplsLspInfoPathDown,'mplsLspInfoPathUp':mplsLspInfoPathUp,'mplsInfo':mplsInfo,'mplsVersion':mplsVersion,'mplsSignalingProto':mplsSignalingProto,'mplsConfiguredLsps':mplsConfiguredLsps,'mplsActiveLsps':mplsActiveLsps,'mplsTEInfo':mplsTEInfo,'mplsTEDistProtocol':mplsTEDistProtocol,'mplsAdminGroupList':mplsAdminGroupList,'mplsAdminGroup':mplsAdminGroup,_M:mplsAdminGroupNumber,'mplsAdminGroupName':mplsAdminGroupName,'mplsLspList':mplsLspList,'mplsLspEntry':mplsLspEntry,_F:mplsLspName,'mplsLspState':mplsLspState,'mplsLspOctets':mplsLspOctets,'mplsLspPackets':mplsLspPackets,'mplsLspAge':mplsLspAge,'mplsLspTimeUp':mplsLspTimeUp,'mplsLspPrimaryTimeUp':mplsLspPrimaryTimeUp,'mplsLspTransitions':mplsLspTransitions,'mplsLspLastTransition':mplsLspLastTransition,'mplsLspPathChanges':mplsLspPathChanges,'mplsLspLastPathChange':mplsLspLastPathChange,'mplsLspConfiguredPaths':mplsLspConfiguredPaths,'mplsLspStandbyPaths':mplsLspStandbyPaths,'mplsLspOperationalPaths':mplsLspOperationalPaths,'mplsLspFrom':mplsLspFrom,'mplsLspTo':mplsLspTo,_K:mplsPathName,'mplsPathType':mplsPathType,'mplsPathExplicitRoute':mplsPathExplicitRoute,'mplsPathRecordRoute':mplsPathRecordRoute,'mplsPathBandwidth':mplsPathBandwidth,'mplsPathCOS':mplsPathCOS,'mplsPathInclude':mplsPathInclude,'mplsPathExclude':mplsPathExclude,'mplsPathSetupPriority':mplsPathSetupPriority,'mplsPathHoldPriority':mplsPathHoldPriority,'mplsPathProperties':mplsPathProperties,'mplsTraps':mplsTraps,'mplsLspUp':mplsLspUp,'mplsLspDown':mplsLspDown,'mplsLspChange':mplsLspChange,'mplsLspPathDown':mplsLspPathDown,'mplsLspPathUp':mplsLspPathUp,'mplsLspInfoList':mplsLspInfoList,'mplsLspInfoEntry':mplsLspInfoEntry,_G:mplsLspInfoName,'mplsLspInfoState':mplsLspInfoState,'mplsLspInfoOctets':mplsLspInfoOctets,'mplsLspInfoPackets':mplsLspInfoPackets,'mplsLspInfoAge':mplsLspInfoAge,'mplsLspInfoTimeUp':mplsLspInfoTimeUp,'mplsLspInfoPrimaryTimeUp':mplsLspInfoPrimaryTimeUp,'mplsLspInfoTransitions':mplsLspInfoTransitions,'mplsLspInfoLastTransition':mplsLspInfoLastTransition,'mplsLspInfoPathChanges':mplsLspInfoPathChanges,'mplsLspInfoLastPathChange':mplsLspInfoLastPathChange,'mplsLspInfoConfiguredPaths':mplsLspInfoConfiguredPaths,'mplsLspInfoStandbyPaths':mplsLspInfoStandbyPaths,'mplsLspInfoOperationalPaths':mplsLspInfoOperationalPaths,'mplsLspInfoFrom':mplsLspInfoFrom,'mplsLspInfoTo':mplsLspInfoTo,_J:mplsPathInfoName,'mplsPathInfoType':mplsPathInfoType,'mplsPathInfoExplicitRoute':mplsPathInfoExplicitRoute,'mplsPathInfoRecordRoute':mplsPathInfoRecordRoute,'mplsPathInfoBandwidth':mplsPathInfoBandwidth,'mplsPathInfoCOS':mplsPathInfoCOS,'mplsPathInfoInclude':mplsPathInfoInclude,'mplsPathInfoExclude':mplsPathInfoExclude,'mplsPathInfoSetupPriority':mplsPathInfoSetupPriority,'mplsPathInfoHoldPriority':mplsPathInfoHoldPriority,'mplsPathInfoProperties':mplsPathInfoProperties,'mplsLspInfoAggrOctets':mplsLspInfoAggrOctets,'mplsLspInfoAggrPackets':mplsLspInfoAggrPackets,'mplsPathInfoRecordRouteWithLabels':mplsPathInfoRecordRouteWithLabels})