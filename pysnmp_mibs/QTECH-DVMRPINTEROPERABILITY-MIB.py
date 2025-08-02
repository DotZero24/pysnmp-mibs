_y='qtechDvmrpRouteTrapGroup'
_x='qtechDvmrpRouteMIBGroup'
_w='qtechDvmrpMetricMIBGroup'
_v='qtechDvmrpSummaryMIBGroup'
_u='qtechDvmrpMetricOffsetMIBGroup'
_t='qtechDvmrpInterfaceMIBGroup'
_s='qtechDvmrpBaseMIBGroup'
_r='qtechDvmrpRouteInformation'
_q='qtechDvmrpRouteStatus'
_p='qtechDvmrpRouteNextHopInterface'
_o='qtechDvmrpRouteNextHopAddress'
_n='qtechDvmrpRouteExpires'
_m='qtechDvmrpRouteUptime'
_l='qtechDvmrpRouteMetric'
_k='qtechDvmrpRouteDistance'
_j='qtechDvmrpMetricStatus'
_i='qtechDvmrpMetricListAclName'
_h='qtechDvmrpSummaryStatus'
_g='qtechDvmrpSummaryMetric'
_f='qtechDvmrpMetricOffsetIncrement'
_e='qtechDvmrpInterfaceDvmrpRtAdvertised'
_d='qtechDvmrpInterfaceUniRtAdvertised'
_c='qtechDvmrpInterfacePoisonReverseRtsRec'
_b='qtechDvmrpInterfaceRtsRec'
_a='qtechDvmrpInterfaceAutoSummaryStatus'
_Z='qtechDvmrpInterfaceRejectNonPrunersStatus'
_Y='qtechDvmrpInterfaceUnicastRoutingStatus'
_X='qtechDvmrpInterfaceDefaultInformation'
_W='qtechDvmrpRoutehogNotification'
_V='qtechDvmrpRouteLimit'
_U='qtechDvmrpRouteInterface'
_T='qtechDvmrpRouteIpAddress'
_S='qtechDvmrpMetricProtocolId'
_R='qtechDvmrpMetric'
_Q='qtechDvmrpMetricIfIndex'
_P='qtechDvmrpSummaryMask'
_O='qtechDvmrpSummaryAddress'
_N='qtechDvmrpIfIndex'
_M='qtechDvmrpMetricOffsetInOrOut'
_L='qtechDvmrpMetricOffsetIfIndex'
_K='default'
_J='qtechDvmrpInterfaceIfIndex'
_I='Unsigned32'
_H='read-create'
_G='EnabledStatus'
_F='Integer32'
_E='read-write'
_D='read-only'
_C='not-accessible'
_B='QTECH-DVMRPINTEROPERABILITY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_G)
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
qtechDvmrpMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,29))
if mibBuilder.loadTexts:qtechDvmrpMIB.setRevisions(('2003-01-20 00:00',))
_QtechDvmrpMIBObjects_ObjectIdentity=ObjectIdentity
qtechDvmrpMIBObjects=_QtechDvmrpMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,29,1))
_QtechDvmrpGroup_ObjectIdentity=ObjectIdentity
qtechDvmrpGroup=_QtechDvmrpGroup_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,29,1,1))
class _QtechDvmrpRouteLimit_Type(Unsigned32):defaultValue=7000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_QtechDvmrpRouteLimit_Type.__name__=_I
_QtechDvmrpRouteLimit_Object=MibScalar
qtechDvmrpRouteLimit=_QtechDvmrpRouteLimit_Object((1,3,6,1,4,1,27514,1,1,10,2,29,1,1,1),_QtechDvmrpRouteLimit_Type())
qtechDvmrpRouteLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechDvmrpRouteLimit.setStatus(_A)
class _QtechDvmrpRoutehogNotification_Type(Unsigned32):defaultValue=10000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_QtechDvmrpRoutehogNotification_Type.__name__=_I
_QtechDvmrpRoutehogNotification_Object=MibScalar
qtechDvmrpRoutehogNotification=_QtechDvmrpRoutehogNotification_Object((1,3,6,1,4,1,27514,1,1,10,2,29,1,1,2),_QtechDvmrpRoutehogNotification_Type())
qtechDvmrpRoutehogNotification.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechDvmrpRoutehogNotification.setStatus(_A)
_QtechDvmrpInterfaceTable_Object=MibTable
qtechDvmrpInterfaceTable=_QtechDvmrpInterfaceTable_Object((1,3,6,1,4,1,27514,1,1,10,2,29,1,2))
if mibBuilder.loadTexts:qtechDvmrpInterfaceTable.setStatus(_A)
_QtechDvmrpInterfaceEntry_Object=MibTableRow
qtechDvmrpInterfaceEntry=_QtechDvmrpInterfaceEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,29,1,2,1))
qtechDvmrpInterfaceEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:qtechDvmrpInterfaceEntry.setStatus(_A)
_QtechDvmrpInterfaceIfIndex_Type=InterfaceIndex
_QtechDvmrpInterfaceIfIndex_Object=MibTableColumn
qtechDvmrpInterfaceIfIndex=_QtechDvmrpInterfaceIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,29,1,2,1,1),_QtechDvmrpInterfaceIfIndex_Type())
qtechDvmrpInterfaceIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDvmrpInterfaceIfIndex.setStatus(_A)
class _QtechDvmrpInterfaceDefaultInformation_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_K,0),('originate',1),('only',2)))
_QtechDvmrpInterfaceDefaultInformation_Type.__name__=_F
_QtechDvmrpInterfaceDefaultInformation_Object=MibTableColumn
qtechDvmrpInterfaceDefaultInformation=_QtechDvmrpInterfaceDefaultInformation_Object((1,3,6,1,4,1,27514,1,1,10,2,29,1,2,1,2),_QtechDvmrpInterfaceDefaultInformation_Type())
qtechDvmrpInterfaceDefaultInformation.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechDvmrpInterfaceDefaultInformation.setStatus(_A)
class _QtechDvmrpInterfaceUnicastRoutingStatus_Type(EnabledStatus):defaultValue=2
_QtechDvmrpInterfaceUnicastRoutingStatus_Type.__name__=_G
_QtechDvmrpInterfaceUnicastRoutingStatus_Object=MibTableColumn
qtechDvmrpInterfaceUnicastRoutingStatus=_QtechDvmrpInterfaceUnicastRoutingStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,29,1,2,1,3),_QtechDvmrpInterfaceUnicastRoutingStatus_Type())
qtechDvmrpInterfaceUnicastRoutingStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechDvmrpInterfaceUnicastRoutingStatus.setStatus(_A)
class _QtechDvmrpInterfaceRejectNonPrunersStatus_Type(EnabledStatus):defaultValue=2
_QtechDvmrpInterfaceRejectNonPrunersStatus_Type.__name__=_G
_QtechDvmrpInterfaceRejectNonPrunersStatus_Object=MibTableColumn
qtechDvmrpInterfaceRejectNonPrunersStatus=_QtechDvmrpInterfaceRejectNonPrunersStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,29,1,2,1,4),_QtechDvmrpInterfaceRejectNonPrunersStatus_Type())
qtechDvmrpInterfaceRejectNonPrunersStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechDvmrpInterfaceRejectNonPrunersStatus.setStatus(_A)
class _QtechDvmrpInterfaceAutoSummaryStatus_Type(EnabledStatus):defaultValue=1
_QtechDvmrpInterfaceAutoSummaryStatus_Type.__name__=_G
_QtechDvmrpInterfaceAutoSummaryStatus_Object=MibTableColumn
qtechDvmrpInterfaceAutoSummaryStatus=_QtechDvmrpInterfaceAutoSummaryStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,29,1,2,1,5),_QtechDvmrpInterfaceAutoSummaryStatus_Type())
qtechDvmrpInterfaceAutoSummaryStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechDvmrpInterfaceAutoSummaryStatus.setStatus(_A)
_QtechDvmrpInterfaceRtsRec_Type=Integer32
_QtechDvmrpInterfaceRtsRec_Object=MibTableColumn
qtechDvmrpInterfaceRtsRec=_QtechDvmrpInterfaceRtsRec_Object((1,3,6,1,4,1,27514,1,1,10,2,29,1,2,1,6),_QtechDvmrpInterfaceRtsRec_Type())
qtechDvmrpInterfaceRtsRec.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechDvmrpInterfaceRtsRec.setStatus(_A)
_QtechDvmrpInterfacePoisonReverseRtsRec_Type=Integer32
_QtechDvmrpInterfacePoisonReverseRtsRec_Object=MibTableColumn
qtechDvmrpInterfacePoisonReverseRtsRec=_QtechDvmrpInterfacePoisonReverseRtsRec_Object((1,3,6,1,4,1,27514,1,1,10,2,29,1,2,1,7),_QtechDvmrpInterfacePoisonReverseRtsRec_Type())
qtechDvmrpInterfacePoisonReverseRtsRec.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechDvmrpInterfacePoisonReverseRtsRec.setStatus(_A)
_QtechDvmrpInterfaceUniRtAdvertised_Type=Integer32
_QtechDvmrpInterfaceUniRtAdvertised_Object=MibTableColumn
qtechDvmrpInterfaceUniRtAdvertised=_QtechDvmrpInterfaceUniRtAdvertised_Object((1,3,6,1,4,1,27514,1,1,10,2,29,1,2,1,8),_QtechDvmrpInterfaceUniRtAdvertised_Type())
qtechDvmrpInterfaceUniRtAdvertised.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechDvmrpInterfaceUniRtAdvertised.setStatus(_A)
_QtechDvmrpInterfaceDvmrpRtAdvertised_Type=Integer32
_QtechDvmrpInterfaceDvmrpRtAdvertised_Object=MibTableColumn
qtechDvmrpInterfaceDvmrpRtAdvertised=_QtechDvmrpInterfaceDvmrpRtAdvertised_Object((1,3,6,1,4,1,27514,1,1,10,2,29,1,2,1,9),_QtechDvmrpInterfaceDvmrpRtAdvertised_Type())
qtechDvmrpInterfaceDvmrpRtAdvertised.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechDvmrpInterfaceDvmrpRtAdvertised.setStatus(_A)
_QtechDvmrpMetricOffsetTable_Object=MibTable
qtechDvmrpMetricOffsetTable=_QtechDvmrpMetricOffsetTable_Object((1,3,6,1,4,1,27514,1,1,10,2,29,1,3))
if mibBuilder.loadTexts:qtechDvmrpMetricOffsetTable.setStatus(_A)
_QtechDvmrpMetricOffsetEntry_Object=MibTableRow
qtechDvmrpMetricOffsetEntry=_QtechDvmrpMetricOffsetEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,29,1,3,1))
qtechDvmrpMetricOffsetEntry.setIndexNames((0,_B,_L),(0,_B,_M))
if mibBuilder.loadTexts:qtechDvmrpMetricOffsetEntry.setStatus(_A)
_QtechDvmrpMetricOffsetIfIndex_Type=InterfaceIndex
_QtechDvmrpMetricOffsetIfIndex_Object=MibTableColumn
qtechDvmrpMetricOffsetIfIndex=_QtechDvmrpMetricOffsetIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,29,1,3,1,1),_QtechDvmrpMetricOffsetIfIndex_Type())
qtechDvmrpMetricOffsetIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDvmrpMetricOffsetIfIndex.setStatus(_A)
class _QtechDvmrpMetricOffsetInOrOut_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('in',1),('out',2)))
_QtechDvmrpMetricOffsetInOrOut_Type.__name__=_F
_QtechDvmrpMetricOffsetInOrOut_Object=MibTableColumn
qtechDvmrpMetricOffsetInOrOut=_QtechDvmrpMetricOffsetInOrOut_Object((1,3,6,1,4,1,27514,1,1,10,2,29,1,3,1,2),_QtechDvmrpMetricOffsetInOrOut_Type())
qtechDvmrpMetricOffsetInOrOut.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDvmrpMetricOffsetInOrOut.setStatus(_A)
class _QtechDvmrpMetricOffsetIncrement_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_QtechDvmrpMetricOffsetIncrement_Type.__name__=_F
_QtechDvmrpMetricOffsetIncrement_Object=MibTableColumn
qtechDvmrpMetricOffsetIncrement=_QtechDvmrpMetricOffsetIncrement_Object((1,3,6,1,4,1,27514,1,1,10,2,29,1,3,1,3),_QtechDvmrpMetricOffsetIncrement_Type())
qtechDvmrpMetricOffsetIncrement.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechDvmrpMetricOffsetIncrement.setStatus(_A)
_QtechDvmrpSummaryTable_Object=MibTable
qtechDvmrpSummaryTable=_QtechDvmrpSummaryTable_Object((1,3,6,1,4,1,27514,1,1,10,2,29,1,4))
if mibBuilder.loadTexts:qtechDvmrpSummaryTable.setStatus(_A)
_QtechDvmrpSummaryEntry_Object=MibTableRow
qtechDvmrpSummaryEntry=_QtechDvmrpSummaryEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,29,1,4,1))
qtechDvmrpSummaryEntry.setIndexNames((0,_B,_N),(0,_B,_O),(0,_B,_P))
if mibBuilder.loadTexts:qtechDvmrpSummaryEntry.setStatus(_A)
_QtechDvmrpIfIndex_Type=InterfaceIndex
_QtechDvmrpIfIndex_Object=MibTableColumn
qtechDvmrpIfIndex=_QtechDvmrpIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,29,1,4,1,1),_QtechDvmrpIfIndex_Type())
qtechDvmrpIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDvmrpIfIndex.setStatus(_A)
_QtechDvmrpSummaryAddress_Type=IpAddress
_QtechDvmrpSummaryAddress_Object=MibTableColumn
qtechDvmrpSummaryAddress=_QtechDvmrpSummaryAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,29,1,4,1,2),_QtechDvmrpSummaryAddress_Type())
qtechDvmrpSummaryAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDvmrpSummaryAddress.setStatus(_A)
_QtechDvmrpSummaryMask_Type=IpAddress
_QtechDvmrpSummaryMask_Object=MibTableColumn
qtechDvmrpSummaryMask=_QtechDvmrpSummaryMask_Object((1,3,6,1,4,1,27514,1,1,10,2,29,1,4,1,3),_QtechDvmrpSummaryMask_Type())
qtechDvmrpSummaryMask.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDvmrpSummaryMask.setStatus(_A)
class _QtechDvmrpSummaryMetric_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_QtechDvmrpSummaryMetric_Type.__name__=_F
_QtechDvmrpSummaryMetric_Object=MibTableColumn
qtechDvmrpSummaryMetric=_QtechDvmrpSummaryMetric_Object((1,3,6,1,4,1,27514,1,1,10,2,29,1,4,1,4),_QtechDvmrpSummaryMetric_Type())
qtechDvmrpSummaryMetric.setMaxAccess(_H)
if mibBuilder.loadTexts:qtechDvmrpSummaryMetric.setStatus(_A)
_QtechDvmrpSummaryStatus_Type=RowStatus
_QtechDvmrpSummaryStatus_Object=MibTableColumn
qtechDvmrpSummaryStatus=_QtechDvmrpSummaryStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,29,1,4,1,5),_QtechDvmrpSummaryStatus_Type())
qtechDvmrpSummaryStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:qtechDvmrpSummaryStatus.setStatus(_A)
_QtechDvmrpMetricTable_Object=MibTable
qtechDvmrpMetricTable=_QtechDvmrpMetricTable_Object((1,3,6,1,4,1,27514,1,1,10,2,29,1,5))
if mibBuilder.loadTexts:qtechDvmrpMetricTable.setStatus(_A)
_QtechDvmrpMetricEntry_Object=MibTableRow
qtechDvmrpMetricEntry=_QtechDvmrpMetricEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,29,1,5,1))
qtechDvmrpMetricEntry.setIndexNames((0,_B,_Q),(0,_B,_R),(0,_B,_S))
if mibBuilder.loadTexts:qtechDvmrpMetricEntry.setStatus(_A)
_QtechDvmrpMetricIfIndex_Type=InterfaceIndex
_QtechDvmrpMetricIfIndex_Object=MibTableColumn
qtechDvmrpMetricIfIndex=_QtechDvmrpMetricIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,29,1,5,1,1),_QtechDvmrpMetricIfIndex_Type())
qtechDvmrpMetricIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDvmrpMetricIfIndex.setStatus(_A)
class _QtechDvmrpMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_QtechDvmrpMetric_Type.__name__=_F
_QtechDvmrpMetric_Object=MibTableColumn
qtechDvmrpMetric=_QtechDvmrpMetric_Object((1,3,6,1,4,1,27514,1,1,10,2,29,1,5,1,2),_QtechDvmrpMetric_Type())
qtechDvmrpMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDvmrpMetric.setStatus(_A)
_QtechDvmrpMetricListAclName_Type=DisplayString
_QtechDvmrpMetricListAclName_Object=MibTableColumn
qtechDvmrpMetricListAclName=_QtechDvmrpMetricListAclName_Object((1,3,6,1,4,1,27514,1,1,10,2,29,1,5,1,3),_QtechDvmrpMetricListAclName_Type())
qtechDvmrpMetricListAclName.setMaxAccess(_H)
if mibBuilder.loadTexts:qtechDvmrpMetricListAclName.setStatus(_A)
class _QtechDvmrpMetricProtocolId_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_K,0),('ospf',1),('rip',2),('static',3),('dvmrp',4)))
_QtechDvmrpMetricProtocolId_Type.__name__=_F
_QtechDvmrpMetricProtocolId_Object=MibTableColumn
qtechDvmrpMetricProtocolId=_QtechDvmrpMetricProtocolId_Object((1,3,6,1,4,1,27514,1,1,10,2,29,1,5,1,4),_QtechDvmrpMetricProtocolId_Type())
qtechDvmrpMetricProtocolId.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDvmrpMetricProtocolId.setStatus(_A)
_QtechDvmrpMetricStatus_Type=RowStatus
_QtechDvmrpMetricStatus_Object=MibTableColumn
qtechDvmrpMetricStatus=_QtechDvmrpMetricStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,29,1,5,1,5),_QtechDvmrpMetricStatus_Type())
qtechDvmrpMetricStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:qtechDvmrpMetricStatus.setStatus(_A)
_QtechDvmrpRouteTable_Object=MibTable
qtechDvmrpRouteTable=_QtechDvmrpRouteTable_Object((1,3,6,1,4,1,27514,1,1,10,2,29,1,6))
if mibBuilder.loadTexts:qtechDvmrpRouteTable.setStatus(_A)
_QtechDvmrpRouteEntry_Object=MibTableRow
qtechDvmrpRouteEntry=_QtechDvmrpRouteEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,29,1,6,1))
qtechDvmrpRouteEntry.setIndexNames((0,_B,_T),(0,_B,_U))
if mibBuilder.loadTexts:qtechDvmrpRouteEntry.setStatus(_A)
_QtechDvmrpRouteIpAddress_Type=IpAddress
_QtechDvmrpRouteIpAddress_Object=MibTableColumn
qtechDvmrpRouteIpAddress=_QtechDvmrpRouteIpAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,29,1,6,1,1),_QtechDvmrpRouteIpAddress_Type())
qtechDvmrpRouteIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDvmrpRouteIpAddress.setStatus(_A)
_QtechDvmrpRouteInterface_Type=InterfaceIndex
_QtechDvmrpRouteInterface_Object=MibTableColumn
qtechDvmrpRouteInterface=_QtechDvmrpRouteInterface_Object((1,3,6,1,4,1,27514,1,1,10,2,29,1,6,1,2),_QtechDvmrpRouteInterface_Type())
qtechDvmrpRouteInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDvmrpRouteInterface.setStatus(_A)
_QtechDvmrpRouteDistance_Type=Integer32
_QtechDvmrpRouteDistance_Object=MibTableColumn
qtechDvmrpRouteDistance=_QtechDvmrpRouteDistance_Object((1,3,6,1,4,1,27514,1,1,10,2,29,1,6,1,3),_QtechDvmrpRouteDistance_Type())
qtechDvmrpRouteDistance.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechDvmrpRouteDistance.setStatus(_A)
_QtechDvmrpRouteMetric_Type=Integer32
_QtechDvmrpRouteMetric_Object=MibTableColumn
qtechDvmrpRouteMetric=_QtechDvmrpRouteMetric_Object((1,3,6,1,4,1,27514,1,1,10,2,29,1,6,1,4),_QtechDvmrpRouteMetric_Type())
qtechDvmrpRouteMetric.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechDvmrpRouteMetric.setStatus(_A)
_QtechDvmrpRouteUptime_Type=TimeTicks
_QtechDvmrpRouteUptime_Object=MibTableColumn
qtechDvmrpRouteUptime=_QtechDvmrpRouteUptime_Object((1,3,6,1,4,1,27514,1,1,10,2,29,1,6,1,5),_QtechDvmrpRouteUptime_Type())
qtechDvmrpRouteUptime.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechDvmrpRouteUptime.setStatus(_A)
_QtechDvmrpRouteExpires_Type=TimeTicks
_QtechDvmrpRouteExpires_Object=MibTableColumn
qtechDvmrpRouteExpires=_QtechDvmrpRouteExpires_Object((1,3,6,1,4,1,27514,1,1,10,2,29,1,6,1,6),_QtechDvmrpRouteExpires_Type())
qtechDvmrpRouteExpires.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechDvmrpRouteExpires.setStatus(_A)
_QtechDvmrpRouteNextHopAddress_Type=IpAddress
_QtechDvmrpRouteNextHopAddress_Object=MibTableColumn
qtechDvmrpRouteNextHopAddress=_QtechDvmrpRouteNextHopAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,29,1,6,1,7),_QtechDvmrpRouteNextHopAddress_Type())
qtechDvmrpRouteNextHopAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechDvmrpRouteNextHopAddress.setStatus(_A)
_QtechDvmrpRouteNextHopInterface_Type=InterfaceIndex
_QtechDvmrpRouteNextHopInterface_Object=MibTableColumn
qtechDvmrpRouteNextHopInterface=_QtechDvmrpRouteNextHopInterface_Object((1,3,6,1,4,1,27514,1,1,10,2,29,1,6,1,8),_QtechDvmrpRouteNextHopInterface_Type())
qtechDvmrpRouteNextHopInterface.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechDvmrpRouteNextHopInterface.setStatus(_A)
_QtechDvmrpRouteStatus_Type=EnabledStatus
_QtechDvmrpRouteStatus_Object=MibTableColumn
qtechDvmrpRouteStatus=_QtechDvmrpRouteStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,29,1,6,1,9),_QtechDvmrpRouteStatus_Type())
qtechDvmrpRouteStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechDvmrpRouteStatus.setStatus(_A)
_QtechDvmrpTraps_ObjectIdentity=ObjectIdentity
qtechDvmrpTraps=_QtechDvmrpTraps_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,29,1,7))
_QtechDvmrpMIBConformance_ObjectIdentity=ObjectIdentity
qtechDvmrpMIBConformance=_QtechDvmrpMIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,29,2))
_QtechDvmrpMIBCompliances_ObjectIdentity=ObjectIdentity
qtechDvmrpMIBCompliances=_QtechDvmrpMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,29,2,1))
_QtechDvmrpMIBGroups_ObjectIdentity=ObjectIdentity
qtechDvmrpMIBGroups=_QtechDvmrpMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,29,2,2))
qtechDvmrpBaseMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,29,2,2,1))
qtechDvmrpBaseMIBGroup.setObjects(*((_B,_V),(_B,_W)))
if mibBuilder.loadTexts:qtechDvmrpBaseMIBGroup.setStatus(_A)
qtechDvmrpInterfaceMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,29,2,2,2))
qtechDvmrpInterfaceMIBGroup.setObjects(*((_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:qtechDvmrpInterfaceMIBGroup.setStatus(_A)
qtechDvmrpMetricOffsetMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,29,2,2,3))
qtechDvmrpMetricOffsetMIBGroup.setObjects((_B,_f))
if mibBuilder.loadTexts:qtechDvmrpMetricOffsetMIBGroup.setStatus(_A)
qtechDvmrpSummaryMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,29,2,2,4))
qtechDvmrpSummaryMIBGroup.setObjects(*((_B,_g),(_B,_h)))
if mibBuilder.loadTexts:qtechDvmrpSummaryMIBGroup.setStatus(_A)
qtechDvmrpMetricMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,29,2,2,5))
qtechDvmrpMetricMIBGroup.setObjects(*((_B,_i),(_B,_j)))
if mibBuilder.loadTexts:qtechDvmrpMetricMIBGroup.setStatus(_A)
qtechDvmrpRouteMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,29,2,2,6))
qtechDvmrpRouteMIBGroup.setObjects(*((_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q)))
if mibBuilder.loadTexts:qtechDvmrpRouteMIBGroup.setStatus(_A)
qtechDvmrpRouteInformation=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,29,1,7,1))
if mibBuilder.loadTexts:qtechDvmrpRouteInformation.setStatus(_A)
qtechDvmrpRouteTrapGroup=NotificationGroup((1,3,6,1,4,1,27514,1,1,10,2,29,2,2,7))
qtechDvmrpRouteTrapGroup.setObjects((_B,_r))
if mibBuilder.loadTexts:qtechDvmrpRouteTrapGroup.setStatus(_A)
qtechDvmrpMIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,29,2,1,1))
qtechDvmrpMIBCompliance.setObjects(*((_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y)))
if mibBuilder.loadTexts:qtechDvmrpMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'qtechDvmrpMIB':qtechDvmrpMIB,'qtechDvmrpMIBObjects':qtechDvmrpMIBObjects,'qtechDvmrpGroup':qtechDvmrpGroup,_V:qtechDvmrpRouteLimit,_W:qtechDvmrpRoutehogNotification,'qtechDvmrpInterfaceTable':qtechDvmrpInterfaceTable,'qtechDvmrpInterfaceEntry':qtechDvmrpInterfaceEntry,_J:qtechDvmrpInterfaceIfIndex,_X:qtechDvmrpInterfaceDefaultInformation,_Y:qtechDvmrpInterfaceUnicastRoutingStatus,_Z:qtechDvmrpInterfaceRejectNonPrunersStatus,_a:qtechDvmrpInterfaceAutoSummaryStatus,_b:qtechDvmrpInterfaceRtsRec,_c:qtechDvmrpInterfacePoisonReverseRtsRec,_d:qtechDvmrpInterfaceUniRtAdvertised,_e:qtechDvmrpInterfaceDvmrpRtAdvertised,'qtechDvmrpMetricOffsetTable':qtechDvmrpMetricOffsetTable,'qtechDvmrpMetricOffsetEntry':qtechDvmrpMetricOffsetEntry,_L:qtechDvmrpMetricOffsetIfIndex,_M:qtechDvmrpMetricOffsetInOrOut,_f:qtechDvmrpMetricOffsetIncrement,'qtechDvmrpSummaryTable':qtechDvmrpSummaryTable,'qtechDvmrpSummaryEntry':qtechDvmrpSummaryEntry,_N:qtechDvmrpIfIndex,_O:qtechDvmrpSummaryAddress,_P:qtechDvmrpSummaryMask,_g:qtechDvmrpSummaryMetric,_h:qtechDvmrpSummaryStatus,'qtechDvmrpMetricTable':qtechDvmrpMetricTable,'qtechDvmrpMetricEntry':qtechDvmrpMetricEntry,_Q:qtechDvmrpMetricIfIndex,_R:qtechDvmrpMetric,_i:qtechDvmrpMetricListAclName,_S:qtechDvmrpMetricProtocolId,_j:qtechDvmrpMetricStatus,'qtechDvmrpRouteTable':qtechDvmrpRouteTable,'qtechDvmrpRouteEntry':qtechDvmrpRouteEntry,_T:qtechDvmrpRouteIpAddress,_U:qtechDvmrpRouteInterface,_k:qtechDvmrpRouteDistance,_l:qtechDvmrpRouteMetric,_m:qtechDvmrpRouteUptime,_n:qtechDvmrpRouteExpires,_o:qtechDvmrpRouteNextHopAddress,_p:qtechDvmrpRouteNextHopInterface,_q:qtechDvmrpRouteStatus,'qtechDvmrpTraps':qtechDvmrpTraps,_r:qtechDvmrpRouteInformation,'qtechDvmrpMIBConformance':qtechDvmrpMIBConformance,'qtechDvmrpMIBCompliances':qtechDvmrpMIBCompliances,'qtechDvmrpMIBCompliance':qtechDvmrpMIBCompliance,'qtechDvmrpMIBGroups':qtechDvmrpMIBGroups,_s:qtechDvmrpBaseMIBGroup,_t:qtechDvmrpInterfaceMIBGroup,_u:qtechDvmrpMetricOffsetMIBGroup,_v:qtechDvmrpSummaryMIBGroup,_w:qtechDvmrpMetricMIBGroup,_x:qtechDvmrpRouteMIBGroup,_y:qtechDvmrpRouteTrapGroup})