_c='fcTraceRouteNotifyGroup'
_b='fcTraceRouteResultsGroup'
_a='fcTraceRouteConfigGroup'
_Z='fcTraceRouteCompletionNotify'
_Y='fcTraceRouteHopsHopLatency'
_X='fcTraceRouteHopsHopLatencyValid'
_W='fcTraceRouteHopsHopAddr'
_V='fcTraceRouteRowStatus'
_U='fcTraceRouteTrapOnCompletion'
_T='fcTraceRouteAgeInterval'
_S='fcTraceRouteAdminStatus'
_R='fcTraceRouteTimeout'
_Q='fcTraceRouteTargetAddrType'
_P='fcTraceRouteVsanIndex'
_O='fcTraceRouteHopsHopIndex'
_N='not-accessible'
_M='TruthValue'
_L='Integer32'
_K='VsanIndex'
_J='FcAddressType'
_I='FcStartOper'
_H='fcTraceRouteOperStatus'
_G='fcTraceRouteTargetAddr'
_F='fcTraceRouteIndex'
_E='read-only'
_D='Unsigned32'
_C='read-create'
_B='CISCO-FCTRACEROUTE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
FcStartOper,=mibBuilder.importSymbols('CISCO-FCPING-MIB',_I)
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
FcAddress,FcAddressType,FcNameId,VsanIndex=mibBuilder.importSymbols('CISCO-ST-TC','FcAddress',_J,'FcNameId',_K)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_L,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_M)
ciscoFcTraceRouteMIB=ModuleIdentity((1,3,6,1,4,1,9,9,296))
if mibBuilder.loadTexts:ciscoFcTraceRouteMIB.setRevisions(('2002-10-07 00:00',))
_CiscoFcTraceRouteMIBObjects_ObjectIdentity=ObjectIdentity
ciscoFcTraceRouteMIBObjects=_CiscoFcTraceRouteMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,296,1))
_FcTraceRouteConfiguration_ObjectIdentity=ObjectIdentity
fcTraceRouteConfiguration=_FcTraceRouteConfiguration_ObjectIdentity((1,3,6,1,4,1,9,9,296,1,1))
_FcTraceRouteTable_Object=MibTable
fcTraceRouteTable=_FcTraceRouteTable_Object((1,3,6,1,4,1,9,9,296,1,1,1))
if mibBuilder.loadTexts:fcTraceRouteTable.setStatus(_A)
_FcTraceRouteEntry_Object=MibTableRow
fcTraceRouteEntry=_FcTraceRouteEntry_Object((1,3,6,1,4,1,9,9,296,1,1,1,1))
fcTraceRouteEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:fcTraceRouteEntry.setStatus(_A)
class _FcTraceRouteIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FcTraceRouteIndex_Type.__name__=_D
_FcTraceRouteIndex_Object=MibTableColumn
fcTraceRouteIndex=_FcTraceRouteIndex_Object((1,3,6,1,4,1,9,9,296,1,1,1,1,1),_FcTraceRouteIndex_Type())
fcTraceRouteIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:fcTraceRouteIndex.setStatus(_A)
class _FcTraceRouteVsanIndex_Type(VsanIndex):defaultValue=1
_FcTraceRouteVsanIndex_Type.__name__=_K
_FcTraceRouteVsanIndex_Object=MibTableColumn
fcTraceRouteVsanIndex=_FcTraceRouteVsanIndex_Object((1,3,6,1,4,1,9,9,296,1,1,1,1,2),_FcTraceRouteVsanIndex_Type())
fcTraceRouteVsanIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fcTraceRouteVsanIndex.setStatus(_A)
class _FcTraceRouteTargetAddrType_Type(FcAddressType):defaultValue=1
_FcTraceRouteTargetAddrType_Type.__name__=_J
_FcTraceRouteTargetAddrType_Object=MibTableColumn
fcTraceRouteTargetAddrType=_FcTraceRouteTargetAddrType_Object((1,3,6,1,4,1,9,9,296,1,1,1,1,3),_FcTraceRouteTargetAddrType_Type())
fcTraceRouteTargetAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:fcTraceRouteTargetAddrType.setStatus(_A)
_FcTraceRouteTargetAddr_Type=FcAddress
_FcTraceRouteTargetAddr_Object=MibTableColumn
fcTraceRouteTargetAddr=_FcTraceRouteTargetAddr_Object((1,3,6,1,4,1,9,9,296,1,1,1,1,4),_FcTraceRouteTargetAddr_Type())
fcTraceRouteTargetAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:fcTraceRouteTargetAddr.setStatus(_A)
class _FcTraceRouteTimeout_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,25))
_FcTraceRouteTimeout_Type.__name__=_D
_FcTraceRouteTimeout_Object=MibTableColumn
fcTraceRouteTimeout=_FcTraceRouteTimeout_Object((1,3,6,1,4,1,9,9,296,1,1,1,1,5),_FcTraceRouteTimeout_Type())
fcTraceRouteTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:fcTraceRouteTimeout.setStatus(_A)
if mibBuilder.loadTexts:fcTraceRouteTimeout.setUnits('seconds')
class _FcTraceRouteAdminStatus_Type(FcStartOper):defaultValue=2
_FcTraceRouteAdminStatus_Type.__name__=_I
_FcTraceRouteAdminStatus_Object=MibTableColumn
fcTraceRouteAdminStatus=_FcTraceRouteAdminStatus_Object((1,3,6,1,4,1,9,9,296,1,1,1,1,6),_FcTraceRouteAdminStatus_Type())
fcTraceRouteAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fcTraceRouteAdminStatus.setStatus(_A)
class _FcTraceRouteOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('inProgress',1),('success',2),('partialSuccess',3),('failure',4),('disabled',5)))
_FcTraceRouteOperStatus_Type.__name__=_L
_FcTraceRouteOperStatus_Object=MibTableColumn
fcTraceRouteOperStatus=_FcTraceRouteOperStatus_Object((1,3,6,1,4,1,9,9,296,1,1,1,1,7),_FcTraceRouteOperStatus_Type())
fcTraceRouteOperStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:fcTraceRouteOperStatus.setStatus(_A)
class _FcTraceRouteAgeInterval_Type(Unsigned32):defaultValue=500000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500000,900000))
_FcTraceRouteAgeInterval_Type.__name__=_D
_FcTraceRouteAgeInterval_Object=MibTableColumn
fcTraceRouteAgeInterval=_FcTraceRouteAgeInterval_Object((1,3,6,1,4,1,9,9,296,1,1,1,1,8),_FcTraceRouteAgeInterval_Type())
fcTraceRouteAgeInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:fcTraceRouteAgeInterval.setStatus(_A)
if mibBuilder.loadTexts:fcTraceRouteAgeInterval.setUnits('milliseconds')
class _FcTraceRouteTrapOnCompletion_Type(TruthValue):defaultValue=2
_FcTraceRouteTrapOnCompletion_Type.__name__=_M
_FcTraceRouteTrapOnCompletion_Object=MibTableColumn
fcTraceRouteTrapOnCompletion=_FcTraceRouteTrapOnCompletion_Object((1,3,6,1,4,1,9,9,296,1,1,1,1,9),_FcTraceRouteTrapOnCompletion_Type())
fcTraceRouteTrapOnCompletion.setMaxAccess(_C)
if mibBuilder.loadTexts:fcTraceRouteTrapOnCompletion.setStatus(_A)
_FcTraceRouteRowStatus_Type=RowStatus
_FcTraceRouteRowStatus_Object=MibTableColumn
fcTraceRouteRowStatus=_FcTraceRouteRowStatus_Object((1,3,6,1,4,1,9,9,296,1,1,1,1,10),_FcTraceRouteRowStatus_Type())
fcTraceRouteRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fcTraceRouteRowStatus.setStatus(_A)
_FcTraceRouteResults_ObjectIdentity=ObjectIdentity
fcTraceRouteResults=_FcTraceRouteResults_ObjectIdentity((1,3,6,1,4,1,9,9,296,1,2))
_FcTraceRouteHopsTable_Object=MibTable
fcTraceRouteHopsTable=_FcTraceRouteHopsTable_Object((1,3,6,1,4,1,9,9,296,1,2,1))
if mibBuilder.loadTexts:fcTraceRouteHopsTable.setStatus(_A)
_FcTraceRouteHopsEntry_Object=MibTableRow
fcTraceRouteHopsEntry=_FcTraceRouteHopsEntry_Object((1,3,6,1,4,1,9,9,296,1,2,1,1))
fcTraceRouteHopsEntry.setIndexNames((0,_B,_F),(0,_B,_O))
if mibBuilder.loadTexts:fcTraceRouteHopsEntry.setStatus(_A)
class _FcTraceRouteHopsHopIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FcTraceRouteHopsHopIndex_Type.__name__=_D
_FcTraceRouteHopsHopIndex_Object=MibTableColumn
fcTraceRouteHopsHopIndex=_FcTraceRouteHopsHopIndex_Object((1,3,6,1,4,1,9,9,296,1,2,1,1,1),_FcTraceRouteHopsHopIndex_Type())
fcTraceRouteHopsHopIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:fcTraceRouteHopsHopIndex.setStatus(_A)
_FcTraceRouteHopsHopAddr_Type=FcNameId
_FcTraceRouteHopsHopAddr_Object=MibTableColumn
fcTraceRouteHopsHopAddr=_FcTraceRouteHopsHopAddr_Object((1,3,6,1,4,1,9,9,296,1,2,1,1,2),_FcTraceRouteHopsHopAddr_Type())
fcTraceRouteHopsHopAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:fcTraceRouteHopsHopAddr.setStatus(_A)
_FcTraceRouteHopsHopLatencyValid_Type=TruthValue
_FcTraceRouteHopsHopLatencyValid_Object=MibTableColumn
fcTraceRouteHopsHopLatencyValid=_FcTraceRouteHopsHopLatencyValid_Object((1,3,6,1,4,1,9,9,296,1,2,1,1,3),_FcTraceRouteHopsHopLatencyValid_Type())
fcTraceRouteHopsHopLatencyValid.setMaxAccess(_E)
if mibBuilder.loadTexts:fcTraceRouteHopsHopLatencyValid.setStatus(_A)
class _FcTraceRouteHopsHopLatency_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,25000000))
_FcTraceRouteHopsHopLatency_Type.__name__=_D
_FcTraceRouteHopsHopLatency_Object=MibTableColumn
fcTraceRouteHopsHopLatency=_FcTraceRouteHopsHopLatency_Object((1,3,6,1,4,1,9,9,296,1,2,1,1,4),_FcTraceRouteHopsHopLatency_Type())
fcTraceRouteHopsHopLatency.setMaxAccess(_E)
if mibBuilder.loadTexts:fcTraceRouteHopsHopLatency.setStatus(_A)
_FcTraceRouteNotification_ObjectIdentity=ObjectIdentity
fcTraceRouteNotification=_FcTraceRouteNotification_ObjectIdentity((1,3,6,1,4,1,9,9,296,1,3))
_FcTraceRouteNotifications_ObjectIdentity=ObjectIdentity
fcTraceRouteNotifications=_FcTraceRouteNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,296,1,3,0))
_FcTraceRouteMIBConformance_ObjectIdentity=ObjectIdentity
fcTraceRouteMIBConformance=_FcTraceRouteMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,296,2))
_FcTraceRouteMIBCompliances_ObjectIdentity=ObjectIdentity
fcTraceRouteMIBCompliances=_FcTraceRouteMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,296,2,1))
_FcTraceRouteMIBGroups_ObjectIdentity=ObjectIdentity
fcTraceRouteMIBGroups=_FcTraceRouteMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,296,2,2))
fcTraceRouteConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,296,2,2,1))
fcTraceRouteConfigGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_G),(_B,_R),(_B,_S),(_B,_H),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:fcTraceRouteConfigGroup.setStatus(_A)
fcTraceRouteResultsGroup=ObjectGroup((1,3,6,1,4,1,9,9,296,2,2,2))
fcTraceRouteResultsGroup.setObjects(*((_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:fcTraceRouteResultsGroup.setStatus(_A)
fcTraceRouteCompletionNotify=NotificationType((1,3,6,1,4,1,9,9,296,1,3,0,1))
fcTraceRouteCompletionNotify.setObjects(*((_B,_G),(_B,_H)))
if mibBuilder.loadTexts:fcTraceRouteCompletionNotify.setStatus(_A)
fcTraceRouteNotifyGroup=NotificationGroup((1,3,6,1,4,1,9,9,296,2,2,3))
fcTraceRouteNotifyGroup.setObjects((_B,_Z))
if mibBuilder.loadTexts:fcTraceRouteNotifyGroup.setStatus(_A)
fcTraceRouteMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,296,2,1,1))
fcTraceRouteMIBCompliance.setObjects(*((_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:fcTraceRouteMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoFcTraceRouteMIB':ciscoFcTraceRouteMIB,'ciscoFcTraceRouteMIBObjects':ciscoFcTraceRouteMIBObjects,'fcTraceRouteConfiguration':fcTraceRouteConfiguration,'fcTraceRouteTable':fcTraceRouteTable,'fcTraceRouteEntry':fcTraceRouteEntry,_F:fcTraceRouteIndex,_P:fcTraceRouteVsanIndex,_Q:fcTraceRouteTargetAddrType,_G:fcTraceRouteTargetAddr,_R:fcTraceRouteTimeout,_S:fcTraceRouteAdminStatus,_H:fcTraceRouteOperStatus,_T:fcTraceRouteAgeInterval,_U:fcTraceRouteTrapOnCompletion,_V:fcTraceRouteRowStatus,'fcTraceRouteResults':fcTraceRouteResults,'fcTraceRouteHopsTable':fcTraceRouteHopsTable,'fcTraceRouteHopsEntry':fcTraceRouteHopsEntry,_O:fcTraceRouteHopsHopIndex,_W:fcTraceRouteHopsHopAddr,_X:fcTraceRouteHopsHopLatencyValid,_Y:fcTraceRouteHopsHopLatency,'fcTraceRouteNotification':fcTraceRouteNotification,'fcTraceRouteNotifications':fcTraceRouteNotifications,_Z:fcTraceRouteCompletionNotify,'fcTraceRouteMIBConformance':fcTraceRouteMIBConformance,'fcTraceRouteMIBCompliances':fcTraceRouteMIBCompliances,'fcTraceRouteMIBCompliance':fcTraceRouteMIBCompliance,'fcTraceRouteMIBGroups':fcTraceRouteMIBGroups,_a:fcTraceRouteConfigGroup,_b:fcTraceRouteResultsGroup,_c:fcTraceRouteNotifyGroup})