_p='juniMRoutePortConfGroup'
_o='juniMRoutePortLimit'
_n='juniMRoutePortSGCount'
_m='juniMRoutePortAdmittedBw'
_l='juniMRoutePortHysteresis'
_k='juniMRoutePortPriorityBw'
_j='juniMRoutePortMaxBw'
_i='juniMroutePortLocationType'
_h='juniMRouteInterfaceBlockedGroups'
_g='juniMRouteInterfaceActiveGroups'
_f='juniMcastRpfDisable'
_e='juniMRouteOifCnt'
_d='juniMRoutePktFwd'
_c='juniMRouteOwnerProtoType'
_b='juniMRouteRpfDisabled'
_a='juniMRouteIsEcmp'
_Z='juniMRouteQosBw'
_Y='juniMRouteQosBwAdaptive'
_X='juniMRouteAdmBw'
_W='juniMRouteAdmBwAdaptive'
_V='juniMcastRouteStaticRowStatus'
_U='juniMcastRouteStaticTag'
_T='juniMcastRouteStaticRpfHop'
_S='juniMcastRouteStaticRtPreference'
_R='juniMRouteInterfaceEntry'
_Q='juniMRouteEntry'
_P='juniMRoutePortLocationIndex'
_O='juniMcastRouteStaticMask'
_N='juniMcastRouteStaticDest'
_M='DisplayString'
_L='juniMcastGlobalConfGroup'
_K='obsolete'
_J='not-accessible'
_I='juniMRouteConfGroup'
_H='read-create'
_G='juniMcastRpfRouteConfGroup'
_F='juniMRouteIfLocIndex'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='Juniper-MROUTER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
IANAipMRouteProtocol,=mibBuilder.importSymbols('IANA-RTPROTO-MIB','IANAipMRouteProtocol')
ipMRouteEntry,ipMRouteInterfaceEntry=mibBuilder.importSymbols('IPMROUTE-STD-MIB','ipMRouteEntry','ipMRouteInterfaceEntry')
juniMibs,=mibBuilder.importSymbols('Juniper-MIBs','juniMibs')
JuniInterfaceLocationType,JuniInterfaceLocationValue=mibBuilder.importSymbols('Juniper-TC','JuniInterfaceLocationType','JuniInterfaceLocationValue')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_M,'PhysAddress','RowStatus','TextualConvention','TruthValue')
juniMRouterMIB=ModuleIdentity((1,3,6,1,4,1,4874,2,2,65))
if mibBuilder.loadTexts:juniMRouterMIB.setRevisions(('2006-09-18 08:09','2006-09-02 11:02','2006-06-15 10:13','2002-10-28 20:06'))
_JuniMRouterMIBObject_ObjectIdentity=ObjectIdentity
juniMRouterMIBObject=_JuniMRouterMIBObject_ObjectIdentity((1,3,6,1,4,1,4874,2,2,65,1))
_JuniMcastTraps_ObjectIdentity=ObjectIdentity
juniMcastTraps=_JuniMcastTraps_ObjectIdentity((1,3,6,1,4,1,4874,2,2,65,1,1))
_JuniMcastObjects_ObjectIdentity=ObjectIdentity
juniMcastObjects=_JuniMcastObjects_ObjectIdentity((1,3,6,1,4,1,4874,2,2,65,1,2))
_JuniMcastRpfRouteTable_Object=MibTable
juniMcastRpfRouteTable=_JuniMcastRpfRouteTable_Object((1,3,6,1,4,1,4874,2,2,65,1,2,1))
if mibBuilder.loadTexts:juniMcastRpfRouteTable.setStatus(_A)
_JuniMcastRpfRouteEntry_Object=MibTableRow
juniMcastRpfRouteEntry=_JuniMcastRpfRouteEntry_Object((1,3,6,1,4,1,4874,2,2,65,1,2,1,1))
juniMcastRpfRouteEntry.setIndexNames((0,_B,_N),(0,_B,_O))
if mibBuilder.loadTexts:juniMcastRpfRouteEntry.setStatus(_A)
_JuniMcastRouteStaticDest_Type=IpAddress
_JuniMcastRouteStaticDest_Object=MibTableColumn
juniMcastRouteStaticDest=_JuniMcastRouteStaticDest_Object((1,3,6,1,4,1,4874,2,2,65,1,2,1,1,1),_JuniMcastRouteStaticDest_Type())
juniMcastRouteStaticDest.setMaxAccess(_J)
if mibBuilder.loadTexts:juniMcastRouteStaticDest.setStatus(_A)
_JuniMcastRouteStaticMask_Type=IpAddress
_JuniMcastRouteStaticMask_Object=MibTableColumn
juniMcastRouteStaticMask=_JuniMcastRouteStaticMask_Object((1,3,6,1,4,1,4874,2,2,65,1,2,1,1,2),_JuniMcastRouteStaticMask_Type())
juniMcastRouteStaticMask.setMaxAccess(_J)
if mibBuilder.loadTexts:juniMcastRouteStaticMask.setStatus(_A)
class _JuniMcastRouteStaticRtPreference_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_JuniMcastRouteStaticRtPreference_Type.__name__=_D
_JuniMcastRouteStaticRtPreference_Object=MibTableColumn
juniMcastRouteStaticRtPreference=_JuniMcastRouteStaticRtPreference_Object((1,3,6,1,4,1,4874,2,2,65,1,2,1,1,3),_JuniMcastRouteStaticRtPreference_Type())
juniMcastRouteStaticRtPreference.setMaxAccess(_H)
if mibBuilder.loadTexts:juniMcastRouteStaticRtPreference.setStatus(_A)
_JuniMcastRouteStaticRpfHop_Type=IpAddress
_JuniMcastRouteStaticRpfHop_Object=MibTableColumn
juniMcastRouteStaticRpfHop=_JuniMcastRouteStaticRpfHop_Object((1,3,6,1,4,1,4874,2,2,65,1,2,1,1,4),_JuniMcastRouteStaticRpfHop_Type())
juniMcastRouteStaticRpfHop.setMaxAccess(_H)
if mibBuilder.loadTexts:juniMcastRouteStaticRpfHop.setStatus(_A)
_JuniMcastRouteStaticTag_Type=Unsigned32
_JuniMcastRouteStaticTag_Object=MibTableColumn
juniMcastRouteStaticTag=_JuniMcastRouteStaticTag_Object((1,3,6,1,4,1,4874,2,2,65,1,2,1,1,5),_JuniMcastRouteStaticTag_Type())
juniMcastRouteStaticTag.setMaxAccess(_H)
if mibBuilder.loadTexts:juniMcastRouteStaticTag.setStatus(_A)
_JuniMcastRouteStaticRowStatus_Type=RowStatus
_JuniMcastRouteStaticRowStatus_Object=MibTableColumn
juniMcastRouteStaticRowStatus=_JuniMcastRouteStaticRowStatus_Object((1,3,6,1,4,1,4874,2,2,65,1,2,1,1,6),_JuniMcastRouteStaticRowStatus_Type())
juniMcastRouteStaticRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:juniMcastRouteStaticRowStatus.setStatus(_A)
_JuniMRouteTable_Object=MibTable
juniMRouteTable=_JuniMRouteTable_Object((1,3,6,1,4,1,4874,2,2,65,1,2,2))
if mibBuilder.loadTexts:juniMRouteTable.setStatus(_A)
_JuniMRouteEntry_Object=MibTableRow
juniMRouteEntry=_JuniMRouteEntry_Object((1,3,6,1,4,1,4874,2,2,65,1,2,2,1))
if mibBuilder.loadTexts:juniMRouteEntry.setStatus(_A)
_JuniMRouteAdmBwAdaptive_Type=TruthValue
_JuniMRouteAdmBwAdaptive_Object=MibTableColumn
juniMRouteAdmBwAdaptive=_JuniMRouteAdmBwAdaptive_Object((1,3,6,1,4,1,4874,2,2,65,1,2,2,1,1),_JuniMRouteAdmBwAdaptive_Type())
juniMRouteAdmBwAdaptive.setMaxAccess(_C)
if mibBuilder.loadTexts:juniMRouteAdmBwAdaptive.setStatus(_A)
_JuniMRouteAdmBw_Type=Integer32
_JuniMRouteAdmBw_Object=MibTableColumn
juniMRouteAdmBw=_JuniMRouteAdmBw_Object((1,3,6,1,4,1,4874,2,2,65,1,2,2,1,2),_JuniMRouteAdmBw_Type())
juniMRouteAdmBw.setMaxAccess(_C)
if mibBuilder.loadTexts:juniMRouteAdmBw.setStatus(_A)
_JuniMRouteQosBwAdaptive_Type=TruthValue
_JuniMRouteQosBwAdaptive_Object=MibTableColumn
juniMRouteQosBwAdaptive=_JuniMRouteQosBwAdaptive_Object((1,3,6,1,4,1,4874,2,2,65,1,2,2,1,3),_JuniMRouteQosBwAdaptive_Type())
juniMRouteQosBwAdaptive.setMaxAccess(_C)
if mibBuilder.loadTexts:juniMRouteQosBwAdaptive.setStatus(_A)
_JuniMRouteQosBw_Type=Integer32
_JuniMRouteQosBw_Object=MibTableColumn
juniMRouteQosBw=_JuniMRouteQosBw_Object((1,3,6,1,4,1,4874,2,2,65,1,2,2,1,4),_JuniMRouteQosBw_Type())
juniMRouteQosBw.setMaxAccess(_C)
if mibBuilder.loadTexts:juniMRouteQosBw.setStatus(_A)
_JuniMRouteIsEcmp_Type=TruthValue
_JuniMRouteIsEcmp_Object=MibTableColumn
juniMRouteIsEcmp=_JuniMRouteIsEcmp_Object((1,3,6,1,4,1,4874,2,2,65,1,2,2,1,5),_JuniMRouteIsEcmp_Type())
juniMRouteIsEcmp.setMaxAccess(_C)
if mibBuilder.loadTexts:juniMRouteIsEcmp.setStatus(_A)
_JuniMRouteRpfDisabled_Type=TruthValue
_JuniMRouteRpfDisabled_Object=MibTableColumn
juniMRouteRpfDisabled=_JuniMRouteRpfDisabled_Object((1,3,6,1,4,1,4874,2,2,65,1,2,2,1,6),_JuniMRouteRpfDisabled_Type())
juniMRouteRpfDisabled.setMaxAccess(_C)
if mibBuilder.loadTexts:juniMRouteRpfDisabled.setStatus(_A)
_JuniMRouteOwnerProtoType_Type=IANAipMRouteProtocol
_JuniMRouteOwnerProtoType_Object=MibTableColumn
juniMRouteOwnerProtoType=_JuniMRouteOwnerProtoType_Object((1,3,6,1,4,1,4874,2,2,65,1,2,2,1,7),_JuniMRouteOwnerProtoType_Type())
juniMRouteOwnerProtoType.setMaxAccess(_C)
if mibBuilder.loadTexts:juniMRouteOwnerProtoType.setStatus(_A)
_JuniMRoutePktFwd_Type=Counter64
_JuniMRoutePktFwd_Object=MibTableColumn
juniMRoutePktFwd=_JuniMRoutePktFwd_Object((1,3,6,1,4,1,4874,2,2,65,1,2,2,1,8),_JuniMRoutePktFwd_Type())
juniMRoutePktFwd.setMaxAccess(_C)
if mibBuilder.loadTexts:juniMRoutePktFwd.setStatus(_A)
_JuniMRouteOifCnt_Type=Integer32
_JuniMRouteOifCnt_Object=MibTableColumn
juniMRouteOifCnt=_JuniMRouteOifCnt_Object((1,3,6,1,4,1,4874,2,2,65,1,2,2,1,9),_JuniMRouteOifCnt_Type())
juniMRouteOifCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:juniMRouteOifCnt.setStatus(_A)
class _JuniMcastRpfDisable_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_JuniMcastRpfDisable_Type.__name__=_M
_JuniMcastRpfDisable_Object=MibScalar
juniMcastRpfDisable=_JuniMcastRpfDisable_Object((1,3,6,1,4,1,4874,2,2,65,1,2,3),_JuniMcastRpfDisable_Type())
juniMcastRpfDisable.setMaxAccess(_E)
if mibBuilder.loadTexts:juniMcastRpfDisable.setStatus(_A)
_JuniMRouteInterfaceTable_Object=MibTable
juniMRouteInterfaceTable=_JuniMRouteInterfaceTable_Object((1,3,6,1,4,1,4874,2,2,65,1,2,4))
if mibBuilder.loadTexts:juniMRouteInterfaceTable.setStatus(_A)
_JuniMRouteInterfaceEntry_Object=MibTableRow
juniMRouteInterfaceEntry=_JuniMRouteInterfaceEntry_Object((1,3,6,1,4,1,4874,2,2,65,1,2,4,1))
if mibBuilder.loadTexts:juniMRouteInterfaceEntry.setStatus(_A)
class _JuniMRouteInterfaceActiveGroups_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_JuniMRouteInterfaceActiveGroups_Type.__name__=_D
_JuniMRouteInterfaceActiveGroups_Object=MibTableColumn
juniMRouteInterfaceActiveGroups=_JuniMRouteInterfaceActiveGroups_Object((1,3,6,1,4,1,4874,2,2,65,1,2,4,1,1),_JuniMRouteInterfaceActiveGroups_Type())
juniMRouteInterfaceActiveGroups.setMaxAccess(_C)
if mibBuilder.loadTexts:juniMRouteInterfaceActiveGroups.setStatus(_A)
class _JuniMRouteInterfaceBlockedGroups_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_JuniMRouteInterfaceBlockedGroups_Type.__name__=_D
_JuniMRouteInterfaceBlockedGroups_Object=MibTableColumn
juniMRouteInterfaceBlockedGroups=_JuniMRouteInterfaceBlockedGroups_Object((1,3,6,1,4,1,4874,2,2,65,1,2,4,1,2),_JuniMRouteInterfaceBlockedGroups_Type())
juniMRouteInterfaceBlockedGroups.setMaxAccess(_C)
if mibBuilder.loadTexts:juniMRouteInterfaceBlockedGroups.setStatus(_A)
_JuniMroutePortLocationType_Type=JuniInterfaceLocationType
_JuniMroutePortLocationType_Object=MibScalar
juniMroutePortLocationType=_JuniMroutePortLocationType_Object((1,3,6,1,4,1,4874,2,2,65,1,2,5),_JuniMroutePortLocationType_Type())
juniMroutePortLocationType.setMaxAccess(_C)
if mibBuilder.loadTexts:juniMroutePortLocationType.setStatus(_A)
_JuniMRoutePortTable_Object=MibTable
juniMRoutePortTable=_JuniMRoutePortTable_Object((1,3,6,1,4,1,4874,2,2,65,1,2,6))
if mibBuilder.loadTexts:juniMRoutePortTable.setStatus(_A)
_JuniMRoutePortEntry_Object=MibTableRow
juniMRoutePortEntry=_JuniMRoutePortEntry_Object((1,3,6,1,4,1,4874,2,2,65,1,2,6,1))
juniMRoutePortEntry.setIndexNames((0,_B,_P))
if mibBuilder.loadTexts:juniMRoutePortEntry.setStatus(_A)
_JuniMRoutePortLocationIndex_Type=JuniInterfaceLocationValue
_JuniMRoutePortLocationIndex_Object=MibTableColumn
juniMRoutePortLocationIndex=_JuniMRoutePortLocationIndex_Object((1,3,6,1,4,1,4874,2,2,65,1,2,6,1,1),_JuniMRoutePortLocationIndex_Type())
juniMRoutePortLocationIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:juniMRoutePortLocationIndex.setStatus(_A)
class _JuniMRoutePortMaxBw_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_JuniMRoutePortMaxBw_Type.__name__=_D
_JuniMRoutePortMaxBw_Object=MibTableColumn
juniMRoutePortMaxBw=_JuniMRoutePortMaxBw_Object((1,3,6,1,4,1,4874,2,2,65,1,2,6,1,2),_JuniMRoutePortMaxBw_Type())
juniMRoutePortMaxBw.setMaxAccess(_E)
if mibBuilder.loadTexts:juniMRoutePortMaxBw.setStatus(_A)
class _JuniMRoutePortPriorityBw_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_JuniMRoutePortPriorityBw_Type.__name__=_D
_JuniMRoutePortPriorityBw_Object=MibTableColumn
juniMRoutePortPriorityBw=_JuniMRoutePortPriorityBw_Object((1,3,6,1,4,1,4874,2,2,65,1,2,6,1,3),_JuniMRoutePortPriorityBw_Type())
juniMRoutePortPriorityBw.setMaxAccess(_E)
if mibBuilder.loadTexts:juniMRoutePortPriorityBw.setStatus(_A)
class _JuniMRoutePortHysteresis_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_JuniMRoutePortHysteresis_Type.__name__=_D
_JuniMRoutePortHysteresis_Object=MibTableColumn
juniMRoutePortHysteresis=_JuniMRoutePortHysteresis_Object((1,3,6,1,4,1,4874,2,2,65,1,2,6,1,4),_JuniMRoutePortHysteresis_Type())
juniMRoutePortHysteresis.setMaxAccess(_E)
if mibBuilder.loadTexts:juniMRoutePortHysteresis.setStatus(_A)
class _JuniMRoutePortAdmittedBw_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_JuniMRoutePortAdmittedBw_Type.__name__=_D
_JuniMRoutePortAdmittedBw_Object=MibTableColumn
juniMRoutePortAdmittedBw=_JuniMRoutePortAdmittedBw_Object((1,3,6,1,4,1,4874,2,2,65,1,2,6,1,5),_JuniMRoutePortAdmittedBw_Type())
juniMRoutePortAdmittedBw.setMaxAccess(_C)
if mibBuilder.loadTexts:juniMRoutePortAdmittedBw.setStatus(_A)
class _JuniMRoutePortSGCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_JuniMRoutePortSGCount_Type.__name__=_D
_JuniMRoutePortSGCount_Object=MibTableColumn
juniMRoutePortSGCount=_JuniMRoutePortSGCount_Object((1,3,6,1,4,1,4874,2,2,65,1,2,6,1,6),_JuniMRoutePortSGCount_Type())
juniMRoutePortSGCount.setMaxAccess(_C)
if mibBuilder.loadTexts:juniMRoutePortSGCount.setStatus(_A)
class _JuniMRoutePortLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_JuniMRoutePortLimit_Type.__name__=_D
_JuniMRoutePortLimit_Object=MibTableColumn
juniMRoutePortLimit=_JuniMRoutePortLimit_Object((1,3,6,1,4,1,4874,2,2,65,1,2,6,1,7),_JuniMRoutePortLimit_Type())
juniMRoutePortLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:juniMRoutePortLimit.setStatus(_A)
_JuniMcastNotifyObject_ObjectIdentity=ObjectIdentity
juniMcastNotifyObject=_JuniMcastNotifyObject_ObjectIdentity((1,3,6,1,4,1,4874,2,2,65,1,3))
_JuniMcastNotificationObjects_ObjectIdentity=ObjectIdentity
juniMcastNotificationObjects=_JuniMcastNotificationObjects_ObjectIdentity((1,3,6,1,4,1,4874,2,2,65,1,3,1))
_JuniMRouteIfLocIndex_Type=JuniInterfaceLocationValue
_JuniMRouteIfLocIndex_Object=MibScalar
juniMRouteIfLocIndex=_JuniMRouteIfLocIndex_Object((1,3,6,1,4,1,4874,2,2,65,1,3,1,1),_JuniMRouteIfLocIndex_Type())
juniMRouteIfLocIndex.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:juniMRouteIfLocIndex.setStatus(_A)
_JuniMcastConformance_ObjectIdentity=ObjectIdentity
juniMcastConformance=_JuniMcastConformance_ObjectIdentity((1,3,6,1,4,1,4874,2,2,65,2))
_JuniMcastCompliances_ObjectIdentity=ObjectIdentity
juniMcastCompliances=_JuniMcastCompliances_ObjectIdentity((1,3,6,1,4,1,4874,2,2,65,2,1))
_JuniMcastConfGroups_ObjectIdentity=ObjectIdentity
juniMcastConfGroups=_JuniMcastConfGroups_ObjectIdentity((1,3,6,1,4,1,4874,2,2,65,2,2))
ipMRouteEntry.registerAugmentions((_B,_Q))
juniMRouteEntry.setIndexNames(*ipMRouteEntry.getIndexNames())
ipMRouteInterfaceEntry.registerAugmentions((_B,_R))
juniMRouteInterfaceEntry.setIndexNames(*ipMRouteInterfaceEntry.getIndexNames())
juniMcastRpfRouteConfGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,65,2,2,1))
juniMcastRpfRouteConfGroup.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:juniMcastRpfRouteConfGroup.setStatus(_A)
juniMRouteConfGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,65,2,2,2))
juniMRouteConfGroup.setObjects(*((_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:juniMRouteConfGroup.setStatus(_A)
juniMcastGlobalConfGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,65,2,2,3))
juniMcastGlobalConfGroup.setObjects((_B,_f))
if mibBuilder.loadTexts:juniMcastGlobalConfGroup.setStatus(_A)
juniMRoutePortConfGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,65,2,2,4))
juniMRoutePortConfGroup.setObjects(*((_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o)))
if mibBuilder.loadTexts:juniMRoutePortConfGroup.setStatus(_A)
juniMRoutePortBwExceded=NotificationType((1,3,6,1,4,1,4874,2,2,65,1,1,1))
juniMRoutePortBwExceded.setObjects((_B,_F))
if mibBuilder.loadTexts:juniMRoutePortBwExceded.setStatus(_A)
juniMRoutePortBwReceded=NotificationType((1,3,6,1,4,1,4874,2,2,65,1,1,2))
juniMRoutePortBwReceded.setObjects((_B,_F))
if mibBuilder.loadTexts:juniMRoutePortBwReceded.setStatus(_A)
juniMRoutePortPriorityBwExceded=NotificationType((1,3,6,1,4,1,4874,2,2,65,1,1,3))
juniMRoutePortPriorityBwExceded.setObjects((_B,_F))
if mibBuilder.loadTexts:juniMRoutePortPriorityBwExceded.setStatus(_A)
juniMRoutePortPriorityBwReceded=NotificationType((1,3,6,1,4,1,4874,2,2,65,1,1,4))
juniMRoutePortPriorityBwReceded.setObjects((_B,_F))
if mibBuilder.loadTexts:juniMRoutePortPriorityBwReceded.setStatus(_A)
juniMcastCompliance=ModuleCompliance((1,3,6,1,4,1,4874,2,2,65,2,1,1))
juniMcastCompliance.setObjects((_B,_G))
if mibBuilder.loadTexts:juniMcastCompliance.setStatus(_K)
juniMcastCompliance2=ModuleCompliance((1,3,6,1,4,1,4874,2,2,65,2,1,2))
juniMcastCompliance2.setObjects(*((_B,_G),(_B,_I)))
if mibBuilder.loadTexts:juniMcastCompliance2.setStatus(_K)
juniMcastCompliance3=ModuleCompliance((1,3,6,1,4,1,4874,2,2,65,2,1,3))
juniMcastCompliance3.setObjects(*((_B,_G),(_B,_I),(_B,_L)))
if mibBuilder.loadTexts:juniMcastCompliance3.setStatus(_K)
juniMcastCompliance4=ModuleCompliance((1,3,6,1,4,1,4874,2,2,65,2,1,4))
juniMcastCompliance4.setObjects(*((_B,_G),(_B,_I),(_B,_L),(_B,_p)))
if mibBuilder.loadTexts:juniMcastCompliance4.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'juniMRouterMIB':juniMRouterMIB,'juniMRouterMIBObject':juniMRouterMIBObject,'juniMcastTraps':juniMcastTraps,'juniMRoutePortBwExceded':juniMRoutePortBwExceded,'juniMRoutePortBwReceded':juniMRoutePortBwReceded,'juniMRoutePortPriorityBwExceded':juniMRoutePortPriorityBwExceded,'juniMRoutePortPriorityBwReceded':juniMRoutePortPriorityBwReceded,'juniMcastObjects':juniMcastObjects,'juniMcastRpfRouteTable':juniMcastRpfRouteTable,'juniMcastRpfRouteEntry':juniMcastRpfRouteEntry,_N:juniMcastRouteStaticDest,_O:juniMcastRouteStaticMask,_S:juniMcastRouteStaticRtPreference,_T:juniMcastRouteStaticRpfHop,_U:juniMcastRouteStaticTag,_V:juniMcastRouteStaticRowStatus,'juniMRouteTable':juniMRouteTable,_Q:juniMRouteEntry,_W:juniMRouteAdmBwAdaptive,_X:juniMRouteAdmBw,_Y:juniMRouteQosBwAdaptive,_Z:juniMRouteQosBw,_a:juniMRouteIsEcmp,_b:juniMRouteRpfDisabled,_c:juniMRouteOwnerProtoType,_d:juniMRoutePktFwd,_e:juniMRouteOifCnt,_f:juniMcastRpfDisable,'juniMRouteInterfaceTable':juniMRouteInterfaceTable,_R:juniMRouteInterfaceEntry,_g:juniMRouteInterfaceActiveGroups,_h:juniMRouteInterfaceBlockedGroups,_i:juniMroutePortLocationType,'juniMRoutePortTable':juniMRoutePortTable,'juniMRoutePortEntry':juniMRoutePortEntry,_P:juniMRoutePortLocationIndex,_j:juniMRoutePortMaxBw,_k:juniMRoutePortPriorityBw,_l:juniMRoutePortHysteresis,_m:juniMRoutePortAdmittedBw,_n:juniMRoutePortSGCount,_o:juniMRoutePortLimit,'juniMcastNotifyObject':juniMcastNotifyObject,'juniMcastNotificationObjects':juniMcastNotificationObjects,_F:juniMRouteIfLocIndex,'juniMcastConformance':juniMcastConformance,'juniMcastCompliances':juniMcastCompliances,'juniMcastCompliance':juniMcastCompliance,'juniMcastCompliance2':juniMcastCompliance2,'juniMcastCompliance3':juniMcastCompliance3,'juniMcastCompliance4':juniMcastCompliance4,'juniMcastConfGroups':juniMcastConfGroups,_G:juniMcastRpfRouteConfGroup,_I:juniMRouteConfGroup,_L:juniMcastGlobalConfGroup,_p:juniMRoutePortConfGroup})