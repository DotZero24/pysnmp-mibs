_A1='juniDvmrpInterfaceGroup2'
_A0='juniDvmrpBaseGroup2'
_z='juniDvmrpInterfaceGroup'
_y='juniDvmrpBaseGroup'
_x='juniDvmrpRouteHogNotificationTrap'
_w='juniDvmrpInterfaceAnnounceListName'
_v='juniDvmrpUnicastRouting'
_u='juniDvmrpSrcGrpOifOIFDnTTL'
_t='juniDvmrpSrcGrpOifOIFPruned'
_s='juniDvmrpPruneUpTime'
_r='juniDvmrpPruneIIFIfIndex'
_q='juniDvmrpAclDistNbrStatus'
_p='juniDvmrpAclDistNbrNbrListName'
_o='juniDvmrpAclDistNbrDistance'
_n='juniDvmrpInterfaceEntry'
_m='juniDvmrpSrcGrpOifOIFIfIndex'
_l='juniDvmrpSrcGrpOifSourceMask'
_k='juniDvmrpSrcGrpOifSource'
_j='juniDvmrpSrcGrpOifGroup'
_i='juniDvmrpPruneSourceMask'
_h='juniDvmrpPruneSource'
_g='juniDvmrpPruneGroup'
_f='juniDvmrpSummaryAddrMask'
_e='juniDvmrpSummaryAddrAddress'
_d='juniDvmrpSummaryAddrIfIndex'
_c='juniDvmrpLocalAddrAddrOrIfIndex'
_b='juniDvmrpLocalAddrIfIndex'
_a='juniDvmrpAclDistNbrAclListName'
_Z='juniDvmrpAclDistNbrIfIndex'
_Y='juniDvmrpSourceGroup'
_X='juniDvmrpAclDistNbrGroup'
_W='juniDvmrpInterfaceAdminState'
_V='juniDvmrpInterfaceMetricOffsetIn'
_U='juniDvmrpInterfaceMetricOffsetOut'
_T='juniDvmrpInterfaceAutoSummary'
_S='juniDvmrpSummaryAddrStatus'
_R='juniDvmrpSummaryAddrCost'
_Q='juniDvmrpLocalAddrMask'
_P='obsolete'
_O='juniDvmrpS32PrunesOnly'
_N='juniDvmrpRouteLimit'
_M='juniDvmrpRouteHogNotification'
_L='juniDvmrpMcastAdminState'
_K='juniDvmrpAdminState'
_J='DisplayString'
_I='read-write'
_H='enable'
_G='disable'
_F='read-only'
_E='read-create'
_D='Integer32'
_C='not-accessible'
_B='current'
_A='Juniper-DVMRP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
junidDvmrpInterfaceEntry,=mibBuilder.importSymbols('DVMRP-STD-MIB-JUNI','junidDvmrpInterfaceEntry')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
juniMibs,=mibBuilder.importSymbols('Juniper-MIBs','juniMibs')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_J,'PhysAddress','RowStatus','TextualConvention','TruthValue')
juniDvmrpMIB=ModuleIdentity((1,3,6,1,4,1,4874,2,2,44))
if mibBuilder.loadTexts:juniDvmrpMIB.setRevisions(('2003-01-16 20:55','2001-11-30 21:24'))
_JuniDvmrpMIBObjects_ObjectIdentity=ObjectIdentity
juniDvmrpMIBObjects=_JuniDvmrpMIBObjects_ObjectIdentity((1,3,6,1,4,1,4874,2,2,44,1))
_JuniDvmrp_ObjectIdentity=ObjectIdentity
juniDvmrp=_JuniDvmrp_ObjectIdentity((1,3,6,1,4,1,4874,2,2,44,1,1))
_JuniDvmrpTraps_ObjectIdentity=ObjectIdentity
juniDvmrpTraps=_JuniDvmrpTraps_ObjectIdentity((1,3,6,1,4,1,4874,2,2,44,1,1,0))
_JuniDvmrpScalar_ObjectIdentity=ObjectIdentity
juniDvmrpScalar=_JuniDvmrpScalar_ObjectIdentity((1,3,6,1,4,1,4874,2,2,44,1,1,1))
class _JuniDvmrpAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_JuniDvmrpAdminState_Type.__name__=_D
_JuniDvmrpAdminState_Object=MibScalar
juniDvmrpAdminState=_JuniDvmrpAdminState_Object((1,3,6,1,4,1,4874,2,2,44,1,1,1,1),_JuniDvmrpAdminState_Type())
juniDvmrpAdminState.setMaxAccess(_I)
if mibBuilder.loadTexts:juniDvmrpAdminState.setStatus(_B)
class _JuniDvmrpMcastAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_JuniDvmrpMcastAdminState_Type.__name__=_D
_JuniDvmrpMcastAdminState_Object=MibScalar
juniDvmrpMcastAdminState=_JuniDvmrpMcastAdminState_Object((1,3,6,1,4,1,4874,2,2,44,1,1,1,2),_JuniDvmrpMcastAdminState_Type())
juniDvmrpMcastAdminState.setMaxAccess(_F)
if mibBuilder.loadTexts:juniDvmrpMcastAdminState.setStatus(_B)
class _JuniDvmrpRouteHogNotification_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,134217727))
_JuniDvmrpRouteHogNotification_Type.__name__=_D
_JuniDvmrpRouteHogNotification_Object=MibScalar
juniDvmrpRouteHogNotification=_JuniDvmrpRouteHogNotification_Object((1,3,6,1,4,1,4874,2,2,44,1,1,1,3),_JuniDvmrpRouteHogNotification_Type())
juniDvmrpRouteHogNotification.setMaxAccess(_I)
if mibBuilder.loadTexts:juniDvmrpRouteHogNotification.setStatus(_B)
class _JuniDvmrpRouteLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,134217727))
_JuniDvmrpRouteLimit_Type.__name__=_D
_JuniDvmrpRouteLimit_Object=MibScalar
juniDvmrpRouteLimit=_JuniDvmrpRouteLimit_Object((1,3,6,1,4,1,4874,2,2,44,1,1,1,4),_JuniDvmrpRouteLimit_Type())
juniDvmrpRouteLimit.setMaxAccess(_I)
if mibBuilder.loadTexts:juniDvmrpRouteLimit.setStatus(_B)
class _JuniDvmrpS32PrunesOnly_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_JuniDvmrpS32PrunesOnly_Type.__name__=_D
_JuniDvmrpS32PrunesOnly_Object=MibScalar
juniDvmrpS32PrunesOnly=_JuniDvmrpS32PrunesOnly_Object((1,3,6,1,4,1,4874,2,2,44,1,1,1,5),_JuniDvmrpS32PrunesOnly_Type())
juniDvmrpS32PrunesOnly.setMaxAccess(_F)
if mibBuilder.loadTexts:juniDvmrpS32PrunesOnly.setStatus(_B)
_JuniDvmrpUnicastRouting_Type=TruthValue
_JuniDvmrpUnicastRouting_Object=MibScalar
juniDvmrpUnicastRouting=_JuniDvmrpUnicastRouting_Object((1,3,6,1,4,1,4874,2,2,44,1,1,1,6),_JuniDvmrpUnicastRouting_Type())
juniDvmrpUnicastRouting.setMaxAccess(_I)
if mibBuilder.loadTexts:juniDvmrpUnicastRouting.setStatus(_B)
_JuniDvmrpAclDistNbrTable_Object=MibTable
juniDvmrpAclDistNbrTable=_JuniDvmrpAclDistNbrTable_Object((1,3,6,1,4,1,4874,2,2,44,1,1,2))
if mibBuilder.loadTexts:juniDvmrpAclDistNbrTable.setStatus(_B)
_JuniDvmrpAclDistNbrEntry_Object=MibTableRow
juniDvmrpAclDistNbrEntry=_JuniDvmrpAclDistNbrEntry_Object((1,3,6,1,4,1,4874,2,2,44,1,1,2,1))
juniDvmrpAclDistNbrEntry.setIndexNames((0,_A,_Z),(0,_A,_a))
if mibBuilder.loadTexts:juniDvmrpAclDistNbrEntry.setStatus(_B)
_JuniDvmrpAclDistNbrIfIndex_Type=InterfaceIndex
_JuniDvmrpAclDistNbrIfIndex_Object=MibTableColumn
juniDvmrpAclDistNbrIfIndex=_JuniDvmrpAclDistNbrIfIndex_Object((1,3,6,1,4,1,4874,2,2,44,1,1,2,1,1),_JuniDvmrpAclDistNbrIfIndex_Type())
juniDvmrpAclDistNbrIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDvmrpAclDistNbrIfIndex.setStatus(_B)
class _JuniDvmrpAclDistNbrAclListName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_JuniDvmrpAclDistNbrAclListName_Type.__name__=_J
_JuniDvmrpAclDistNbrAclListName_Object=MibTableColumn
juniDvmrpAclDistNbrAclListName=_JuniDvmrpAclDistNbrAclListName_Object((1,3,6,1,4,1,4874,2,2,44,1,1,2,1,2),_JuniDvmrpAclDistNbrAclListName_Type())
juniDvmrpAclDistNbrAclListName.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDvmrpAclDistNbrAclListName.setStatus(_B)
class _JuniDvmrpAclDistNbrDistance_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_JuniDvmrpAclDistNbrDistance_Type.__name__=_D
_JuniDvmrpAclDistNbrDistance_Object=MibTableColumn
juniDvmrpAclDistNbrDistance=_JuniDvmrpAclDistNbrDistance_Object((1,3,6,1,4,1,4874,2,2,44,1,1,2,1,3),_JuniDvmrpAclDistNbrDistance_Type())
juniDvmrpAclDistNbrDistance.setMaxAccess(_E)
if mibBuilder.loadTexts:juniDvmrpAclDistNbrDistance.setStatus(_B)
class _JuniDvmrpAclDistNbrNbrListName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_JuniDvmrpAclDistNbrNbrListName_Type.__name__=_J
_JuniDvmrpAclDistNbrNbrListName_Object=MibTableColumn
juniDvmrpAclDistNbrNbrListName=_JuniDvmrpAclDistNbrNbrListName_Object((1,3,6,1,4,1,4874,2,2,44,1,1,2,1,4),_JuniDvmrpAclDistNbrNbrListName_Type())
juniDvmrpAclDistNbrNbrListName.setMaxAccess(_E)
if mibBuilder.loadTexts:juniDvmrpAclDistNbrNbrListName.setStatus(_B)
_JuniDvmrpAclDistNbrStatus_Type=RowStatus
_JuniDvmrpAclDistNbrStatus_Object=MibTableColumn
juniDvmrpAclDistNbrStatus=_JuniDvmrpAclDistNbrStatus_Object((1,3,6,1,4,1,4874,2,2,44,1,1,2,1,5),_JuniDvmrpAclDistNbrStatus_Type())
juniDvmrpAclDistNbrStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:juniDvmrpAclDistNbrStatus.setStatus(_B)
_JuniDvmrpLocalAddrTable_Object=MibTable
juniDvmrpLocalAddrTable=_JuniDvmrpLocalAddrTable_Object((1,3,6,1,4,1,4874,2,2,44,1,1,3))
if mibBuilder.loadTexts:juniDvmrpLocalAddrTable.setStatus(_B)
_JuniDvmrpLocalAddrTableEntry_Object=MibTableRow
juniDvmrpLocalAddrTableEntry=_JuniDvmrpLocalAddrTableEntry_Object((1,3,6,1,4,1,4874,2,2,44,1,1,3,1))
juniDvmrpLocalAddrTableEntry.setIndexNames((0,_A,_b),(0,_A,_c))
if mibBuilder.loadTexts:juniDvmrpLocalAddrTableEntry.setStatus(_B)
_JuniDvmrpLocalAddrIfIndex_Type=InterfaceIndex
_JuniDvmrpLocalAddrIfIndex_Object=MibTableColumn
juniDvmrpLocalAddrIfIndex=_JuniDvmrpLocalAddrIfIndex_Object((1,3,6,1,4,1,4874,2,2,44,1,1,3,1,1),_JuniDvmrpLocalAddrIfIndex_Type())
juniDvmrpLocalAddrIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDvmrpLocalAddrIfIndex.setStatus(_B)
_JuniDvmrpLocalAddrAddrOrIfIndex_Type=Unsigned32
_JuniDvmrpLocalAddrAddrOrIfIndex_Object=MibTableColumn
juniDvmrpLocalAddrAddrOrIfIndex=_JuniDvmrpLocalAddrAddrOrIfIndex_Object((1,3,6,1,4,1,4874,2,2,44,1,1,3,1,2),_JuniDvmrpLocalAddrAddrOrIfIndex_Type())
juniDvmrpLocalAddrAddrOrIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDvmrpLocalAddrAddrOrIfIndex.setStatus(_B)
_JuniDvmrpLocalAddrMask_Type=IpAddress
_JuniDvmrpLocalAddrMask_Object=MibTableColumn
juniDvmrpLocalAddrMask=_JuniDvmrpLocalAddrMask_Object((1,3,6,1,4,1,4874,2,2,44,1,1,3,1,3),_JuniDvmrpLocalAddrMask_Type())
juniDvmrpLocalAddrMask.setMaxAccess(_F)
if mibBuilder.loadTexts:juniDvmrpLocalAddrMask.setStatus(_B)
_JuniDvmrpSummaryAddrTable_Object=MibTable
juniDvmrpSummaryAddrTable=_JuniDvmrpSummaryAddrTable_Object((1,3,6,1,4,1,4874,2,2,44,1,1,4))
if mibBuilder.loadTexts:juniDvmrpSummaryAddrTable.setStatus(_B)
_JuniDvmrpSummaryAddrTableEntry_Object=MibTableRow
juniDvmrpSummaryAddrTableEntry=_JuniDvmrpSummaryAddrTableEntry_Object((1,3,6,1,4,1,4874,2,2,44,1,1,4,1))
juniDvmrpSummaryAddrTableEntry.setIndexNames((0,_A,_d),(0,_A,_e),(0,_A,_f))
if mibBuilder.loadTexts:juniDvmrpSummaryAddrTableEntry.setStatus(_B)
_JuniDvmrpSummaryAddrIfIndex_Type=InterfaceIndex
_JuniDvmrpSummaryAddrIfIndex_Object=MibTableColumn
juniDvmrpSummaryAddrIfIndex=_JuniDvmrpSummaryAddrIfIndex_Object((1,3,6,1,4,1,4874,2,2,44,1,1,4,1,1),_JuniDvmrpSummaryAddrIfIndex_Type())
juniDvmrpSummaryAddrIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDvmrpSummaryAddrIfIndex.setStatus(_B)
_JuniDvmrpSummaryAddrAddress_Type=IpAddress
_JuniDvmrpSummaryAddrAddress_Object=MibTableColumn
juniDvmrpSummaryAddrAddress=_JuniDvmrpSummaryAddrAddress_Object((1,3,6,1,4,1,4874,2,2,44,1,1,4,1,2),_JuniDvmrpSummaryAddrAddress_Type())
juniDvmrpSummaryAddrAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDvmrpSummaryAddrAddress.setStatus(_B)
_JuniDvmrpSummaryAddrMask_Type=IpAddress
_JuniDvmrpSummaryAddrMask_Object=MibTableColumn
juniDvmrpSummaryAddrMask=_JuniDvmrpSummaryAddrMask_Object((1,3,6,1,4,1,4874,2,2,44,1,1,4,1,3),_JuniDvmrpSummaryAddrMask_Type())
juniDvmrpSummaryAddrMask.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDvmrpSummaryAddrMask.setStatus(_B)
class _JuniDvmrpSummaryAddrCost_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_JuniDvmrpSummaryAddrCost_Type.__name__=_D
_JuniDvmrpSummaryAddrCost_Object=MibTableColumn
juniDvmrpSummaryAddrCost=_JuniDvmrpSummaryAddrCost_Object((1,3,6,1,4,1,4874,2,2,44,1,1,4,1,4),_JuniDvmrpSummaryAddrCost_Type())
juniDvmrpSummaryAddrCost.setMaxAccess(_E)
if mibBuilder.loadTexts:juniDvmrpSummaryAddrCost.setStatus(_B)
_JuniDvmrpSummaryAddrStatus_Type=RowStatus
_JuniDvmrpSummaryAddrStatus_Object=MibTableColumn
juniDvmrpSummaryAddrStatus=_JuniDvmrpSummaryAddrStatus_Object((1,3,6,1,4,1,4874,2,2,44,1,1,4,1,5),_JuniDvmrpSummaryAddrStatus_Type())
juniDvmrpSummaryAddrStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:juniDvmrpSummaryAddrStatus.setStatus(_B)
_JuniDvmrpInterfaceTable_Object=MibTable
juniDvmrpInterfaceTable=_JuniDvmrpInterfaceTable_Object((1,3,6,1,4,1,4874,2,2,44,1,1,5))
if mibBuilder.loadTexts:juniDvmrpInterfaceTable.setStatus(_B)
_JuniDvmrpInterfaceEntry_Object=MibTableRow
juniDvmrpInterfaceEntry=_JuniDvmrpInterfaceEntry_Object((1,3,6,1,4,1,4874,2,2,44,1,1,5,1))
if mibBuilder.loadTexts:juniDvmrpInterfaceEntry.setStatus(_B)
class _JuniDvmrpInterfaceAutoSummary_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_JuniDvmrpInterfaceAutoSummary_Type.__name__=_D
_JuniDvmrpInterfaceAutoSummary_Object=MibTableColumn
juniDvmrpInterfaceAutoSummary=_JuniDvmrpInterfaceAutoSummary_Object((1,3,6,1,4,1,4874,2,2,44,1,1,5,1,3),_JuniDvmrpInterfaceAutoSummary_Type())
juniDvmrpInterfaceAutoSummary.setMaxAccess(_E)
if mibBuilder.loadTexts:juniDvmrpInterfaceAutoSummary.setStatus(_B)
class _JuniDvmrpInterfaceMetricOffsetOut_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_JuniDvmrpInterfaceMetricOffsetOut_Type.__name__=_D
_JuniDvmrpInterfaceMetricOffsetOut_Object=MibTableColumn
juniDvmrpInterfaceMetricOffsetOut=_JuniDvmrpInterfaceMetricOffsetOut_Object((1,3,6,1,4,1,4874,2,2,44,1,1,5,1,4),_JuniDvmrpInterfaceMetricOffsetOut_Type())
juniDvmrpInterfaceMetricOffsetOut.setMaxAccess(_E)
if mibBuilder.loadTexts:juniDvmrpInterfaceMetricOffsetOut.setStatus(_B)
class _JuniDvmrpInterfaceMetricOffsetIn_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_JuniDvmrpInterfaceMetricOffsetIn_Type.__name__=_D
_JuniDvmrpInterfaceMetricOffsetIn_Object=MibTableColumn
juniDvmrpInterfaceMetricOffsetIn=_JuniDvmrpInterfaceMetricOffsetIn_Object((1,3,6,1,4,1,4874,2,2,44,1,1,5,1,5),_JuniDvmrpInterfaceMetricOffsetIn_Type())
juniDvmrpInterfaceMetricOffsetIn.setMaxAccess(_E)
if mibBuilder.loadTexts:juniDvmrpInterfaceMetricOffsetIn.setStatus(_B)
class _JuniDvmrpInterfaceAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_JuniDvmrpInterfaceAdminState_Type.__name__=_D
_JuniDvmrpInterfaceAdminState_Object=MibTableColumn
juniDvmrpInterfaceAdminState=_JuniDvmrpInterfaceAdminState_Object((1,3,6,1,4,1,4874,2,2,44,1,1,5,1,6),_JuniDvmrpInterfaceAdminState_Type())
juniDvmrpInterfaceAdminState.setMaxAccess(_E)
if mibBuilder.loadTexts:juniDvmrpInterfaceAdminState.setStatus(_B)
_JuniDvmrpInterfaceAnnounceListName_Type=DisplayString
_JuniDvmrpInterfaceAnnounceListName_Object=MibTableColumn
juniDvmrpInterfaceAnnounceListName=_JuniDvmrpInterfaceAnnounceListName_Object((1,3,6,1,4,1,4874,2,2,44,1,1,5,1,7),_JuniDvmrpInterfaceAnnounceListName_Type())
juniDvmrpInterfaceAnnounceListName.setMaxAccess(_E)
if mibBuilder.loadTexts:juniDvmrpInterfaceAnnounceListName.setStatus(_B)
_JuniDvmrpPruneTable_Object=MibTable
juniDvmrpPruneTable=_JuniDvmrpPruneTable_Object((1,3,6,1,4,1,4874,2,2,44,1,1,6))
if mibBuilder.loadTexts:juniDvmrpPruneTable.setStatus(_B)
_JuniDvmrpPruneEntry_Object=MibTableRow
juniDvmrpPruneEntry=_JuniDvmrpPruneEntry_Object((1,3,6,1,4,1,4874,2,2,44,1,1,6,1))
juniDvmrpPruneEntry.setIndexNames((0,_A,_g),(0,_A,_h),(0,_A,_i))
if mibBuilder.loadTexts:juniDvmrpPruneEntry.setStatus(_B)
_JuniDvmrpPruneGroup_Type=IpAddress
_JuniDvmrpPruneGroup_Object=MibTableColumn
juniDvmrpPruneGroup=_JuniDvmrpPruneGroup_Object((1,3,6,1,4,1,4874,2,2,44,1,1,6,1,1),_JuniDvmrpPruneGroup_Type())
juniDvmrpPruneGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDvmrpPruneGroup.setStatus(_B)
_JuniDvmrpPruneSource_Type=IpAddress
_JuniDvmrpPruneSource_Object=MibTableColumn
juniDvmrpPruneSource=_JuniDvmrpPruneSource_Object((1,3,6,1,4,1,4874,2,2,44,1,1,6,1,2),_JuniDvmrpPruneSource_Type())
juniDvmrpPruneSource.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDvmrpPruneSource.setStatus(_B)
_JuniDvmrpPruneSourceMask_Type=IpAddress
_JuniDvmrpPruneSourceMask_Object=MibTableColumn
juniDvmrpPruneSourceMask=_JuniDvmrpPruneSourceMask_Object((1,3,6,1,4,1,4874,2,2,44,1,1,6,1,3),_JuniDvmrpPruneSourceMask_Type())
juniDvmrpPruneSourceMask.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDvmrpPruneSourceMask.setStatus(_B)
_JuniDvmrpPruneIIFIfIndex_Type=InterfaceIndex
_JuniDvmrpPruneIIFIfIndex_Object=MibTableColumn
juniDvmrpPruneIIFIfIndex=_JuniDvmrpPruneIIFIfIndex_Object((1,3,6,1,4,1,4874,2,2,44,1,1,6,1,4),_JuniDvmrpPruneIIFIfIndex_Type())
juniDvmrpPruneIIFIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:juniDvmrpPruneIIFIfIndex.setStatus(_B)
_JuniDvmrpPruneUpTime_Type=TimeTicks
_JuniDvmrpPruneUpTime_Object=MibTableColumn
juniDvmrpPruneUpTime=_JuniDvmrpPruneUpTime_Object((1,3,6,1,4,1,4874,2,2,44,1,1,6,1,5),_JuniDvmrpPruneUpTime_Type())
juniDvmrpPruneUpTime.setMaxAccess(_F)
if mibBuilder.loadTexts:juniDvmrpPruneUpTime.setStatus(_B)
_JuniDvmrpSrcGrpOifTable_Object=MibTable
juniDvmrpSrcGrpOifTable=_JuniDvmrpSrcGrpOifTable_Object((1,3,6,1,4,1,4874,2,2,44,1,1,7))
if mibBuilder.loadTexts:juniDvmrpSrcGrpOifTable.setStatus(_B)
_JuniDvmrpSrcGrpOifEntry_Object=MibTableRow
juniDvmrpSrcGrpOifEntry=_JuniDvmrpSrcGrpOifEntry_Object((1,3,6,1,4,1,4874,2,2,44,1,1,7,1))
juniDvmrpSrcGrpOifEntry.setIndexNames((0,_A,_j),(0,_A,_k),(0,_A,_l),(0,_A,_m))
if mibBuilder.loadTexts:juniDvmrpSrcGrpOifEntry.setStatus(_B)
_JuniDvmrpSrcGrpOifGroup_Type=IpAddress
_JuniDvmrpSrcGrpOifGroup_Object=MibTableColumn
juniDvmrpSrcGrpOifGroup=_JuniDvmrpSrcGrpOifGroup_Object((1,3,6,1,4,1,4874,2,2,44,1,1,7,1,1),_JuniDvmrpSrcGrpOifGroup_Type())
juniDvmrpSrcGrpOifGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDvmrpSrcGrpOifGroup.setStatus(_B)
_JuniDvmrpSrcGrpOifSource_Type=IpAddress
_JuniDvmrpSrcGrpOifSource_Object=MibTableColumn
juniDvmrpSrcGrpOifSource=_JuniDvmrpSrcGrpOifSource_Object((1,3,6,1,4,1,4874,2,2,44,1,1,7,1,2),_JuniDvmrpSrcGrpOifSource_Type())
juniDvmrpSrcGrpOifSource.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDvmrpSrcGrpOifSource.setStatus(_B)
_JuniDvmrpSrcGrpOifSourceMask_Type=IpAddress
_JuniDvmrpSrcGrpOifSourceMask_Object=MibTableColumn
juniDvmrpSrcGrpOifSourceMask=_JuniDvmrpSrcGrpOifSourceMask_Object((1,3,6,1,4,1,4874,2,2,44,1,1,7,1,3),_JuniDvmrpSrcGrpOifSourceMask_Type())
juniDvmrpSrcGrpOifSourceMask.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDvmrpSrcGrpOifSourceMask.setStatus(_B)
_JuniDvmrpSrcGrpOifOIFIfIndex_Type=InterfaceIndex
_JuniDvmrpSrcGrpOifOIFIfIndex_Object=MibTableColumn
juniDvmrpSrcGrpOifOIFIfIndex=_JuniDvmrpSrcGrpOifOIFIfIndex_Object((1,3,6,1,4,1,4874,2,2,44,1,1,7,1,4),_JuniDvmrpSrcGrpOifOIFIfIndex_Type())
juniDvmrpSrcGrpOifOIFIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDvmrpSrcGrpOifOIFIfIndex.setStatus(_B)
class _JuniDvmrpSrcGrpOifOIFPruned_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('false',0),('true',1)))
_JuniDvmrpSrcGrpOifOIFPruned_Type.__name__=_D
_JuniDvmrpSrcGrpOifOIFPruned_Object=MibTableColumn
juniDvmrpSrcGrpOifOIFPruned=_JuniDvmrpSrcGrpOifOIFPruned_Object((1,3,6,1,4,1,4874,2,2,44,1,1,7,1,5),_JuniDvmrpSrcGrpOifOIFPruned_Type())
juniDvmrpSrcGrpOifOIFPruned.setMaxAccess(_F)
if mibBuilder.loadTexts:juniDvmrpSrcGrpOifOIFPruned.setStatus(_B)
_JuniDvmrpSrcGrpOifOIFDnTTL_Type=TimeTicks
_JuniDvmrpSrcGrpOifOIFDnTTL_Object=MibTableColumn
juniDvmrpSrcGrpOifOIFDnTTL=_JuniDvmrpSrcGrpOifOIFDnTTL_Object((1,3,6,1,4,1,4874,2,2,44,1,1,7,1,6),_JuniDvmrpSrcGrpOifOIFDnTTL_Type())
juniDvmrpSrcGrpOifOIFDnTTL.setMaxAccess(_F)
if mibBuilder.loadTexts:juniDvmrpSrcGrpOifOIFDnTTL.setStatus(_B)
_JuniDvmrpConformance_ObjectIdentity=ObjectIdentity
juniDvmrpConformance=_JuniDvmrpConformance_ObjectIdentity((1,3,6,1,4,1,4874,2,2,44,4))
_JuniDvmrpCompliances_ObjectIdentity=ObjectIdentity
juniDvmrpCompliances=_JuniDvmrpCompliances_ObjectIdentity((1,3,6,1,4,1,4874,2,2,44,4,1))
_JuniDvmrpGroups_ObjectIdentity=ObjectIdentity
juniDvmrpGroups=_JuniDvmrpGroups_ObjectIdentity((1,3,6,1,4,1,4874,2,2,44,4,2))
junidDvmrpInterfaceEntry.registerAugmentions((_A,_n))
juniDvmrpInterfaceEntry.setIndexNames(*junidDvmrpInterfaceEntry.getIndexNames())
juniDvmrpBaseGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,44,4,2,1))
juniDvmrpBaseGroup.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:juniDvmrpBaseGroup.setStatus(_P)
juniDvmrpAclDistNbrGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,44,4,2,2))
juniDvmrpAclDistNbrGroup.setObjects(*((_A,_o),(_A,_p),(_A,_q)))
if mibBuilder.loadTexts:juniDvmrpAclDistNbrGroup.setStatus(_B)
juniDvmrpInterfaceGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,44,4,2,3))
juniDvmrpInterfaceGroup.setObjects(*((_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W)))
if mibBuilder.loadTexts:juniDvmrpInterfaceGroup.setStatus(_P)
juniDvmrpSourceGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,44,4,2,4))
juniDvmrpSourceGroup.setObjects(*((_A,_r),(_A,_s),(_A,_t),(_A,_u)))
if mibBuilder.loadTexts:juniDvmrpSourceGroup.setStatus(_B)
juniDvmrpBaseGroup2=ObjectGroup((1,3,6,1,4,1,4874,2,2,44,4,2,6))
juniDvmrpBaseGroup2.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_v)))
if mibBuilder.loadTexts:juniDvmrpBaseGroup2.setStatus(_B)
juniDvmrpInterfaceGroup2=ObjectGroup((1,3,6,1,4,1,4874,2,2,44,4,2,7))
juniDvmrpInterfaceGroup2.setObjects(*((_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_w)))
if mibBuilder.loadTexts:juniDvmrpInterfaceGroup2.setStatus(_B)
juniDvmrpRouteHogNotificationTrap=NotificationType((1,3,6,1,4,1,4874,2,2,44,1,1,0,1))
if mibBuilder.loadTexts:juniDvmrpRouteHogNotificationTrap.setStatus(_B)
juniDvmrpNotificationGroup=NotificationGroup((1,3,6,1,4,1,4874,2,2,44,4,2,5))
juniDvmrpNotificationGroup.setObjects((_A,_x))
if mibBuilder.loadTexts:juniDvmrpNotificationGroup.setStatus(_B)
juniDvmrpCompliance=ModuleCompliance((1,3,6,1,4,1,4874,2,2,44,4,1,1))
juniDvmrpCompliance.setObjects(*((_A,_y),(_A,_X),(_A,_z),(_A,_Y)))
if mibBuilder.loadTexts:juniDvmrpCompliance.setStatus(_P)
juniDvmrpCompliance2=ModuleCompliance((1,3,6,1,4,1,4874,2,2,44,4,1,2))
juniDvmrpCompliance2.setObjects(*((_A,_A0),(_A,_X),(_A,_A1),(_A,_Y)))
if mibBuilder.loadTexts:juniDvmrpCompliance2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'juniDvmrpMIB':juniDvmrpMIB,'juniDvmrpMIBObjects':juniDvmrpMIBObjects,'juniDvmrp':juniDvmrp,'juniDvmrpTraps':juniDvmrpTraps,_x:juniDvmrpRouteHogNotificationTrap,'juniDvmrpScalar':juniDvmrpScalar,_K:juniDvmrpAdminState,_L:juniDvmrpMcastAdminState,_M:juniDvmrpRouteHogNotification,_N:juniDvmrpRouteLimit,_O:juniDvmrpS32PrunesOnly,_v:juniDvmrpUnicastRouting,'juniDvmrpAclDistNbrTable':juniDvmrpAclDistNbrTable,'juniDvmrpAclDistNbrEntry':juniDvmrpAclDistNbrEntry,_Z:juniDvmrpAclDistNbrIfIndex,_a:juniDvmrpAclDistNbrAclListName,_o:juniDvmrpAclDistNbrDistance,_p:juniDvmrpAclDistNbrNbrListName,_q:juniDvmrpAclDistNbrStatus,'juniDvmrpLocalAddrTable':juniDvmrpLocalAddrTable,'juniDvmrpLocalAddrTableEntry':juniDvmrpLocalAddrTableEntry,_b:juniDvmrpLocalAddrIfIndex,_c:juniDvmrpLocalAddrAddrOrIfIndex,_Q:juniDvmrpLocalAddrMask,'juniDvmrpSummaryAddrTable':juniDvmrpSummaryAddrTable,'juniDvmrpSummaryAddrTableEntry':juniDvmrpSummaryAddrTableEntry,_d:juniDvmrpSummaryAddrIfIndex,_e:juniDvmrpSummaryAddrAddress,_f:juniDvmrpSummaryAddrMask,_R:juniDvmrpSummaryAddrCost,_S:juniDvmrpSummaryAddrStatus,'juniDvmrpInterfaceTable':juniDvmrpInterfaceTable,_n:juniDvmrpInterfaceEntry,_T:juniDvmrpInterfaceAutoSummary,_U:juniDvmrpInterfaceMetricOffsetOut,_V:juniDvmrpInterfaceMetricOffsetIn,_W:juniDvmrpInterfaceAdminState,_w:juniDvmrpInterfaceAnnounceListName,'juniDvmrpPruneTable':juniDvmrpPruneTable,'juniDvmrpPruneEntry':juniDvmrpPruneEntry,_g:juniDvmrpPruneGroup,_h:juniDvmrpPruneSource,_i:juniDvmrpPruneSourceMask,_r:juniDvmrpPruneIIFIfIndex,_s:juniDvmrpPruneUpTime,'juniDvmrpSrcGrpOifTable':juniDvmrpSrcGrpOifTable,'juniDvmrpSrcGrpOifEntry':juniDvmrpSrcGrpOifEntry,_j:juniDvmrpSrcGrpOifGroup,_k:juniDvmrpSrcGrpOifSource,_l:juniDvmrpSrcGrpOifSourceMask,_m:juniDvmrpSrcGrpOifOIFIfIndex,_t:juniDvmrpSrcGrpOifOIFPruned,_u:juniDvmrpSrcGrpOifOIFDnTTL,'juniDvmrpConformance':juniDvmrpConformance,'juniDvmrpCompliances':juniDvmrpCompliances,'juniDvmrpCompliance':juniDvmrpCompliance,'juniDvmrpCompliance2':juniDvmrpCompliance2,'juniDvmrpGroups':juniDvmrpGroups,_y:juniDvmrpBaseGroup,_X:juniDvmrpAclDistNbrGroup,_z:juniDvmrpInterfaceGroup,_Y:juniDvmrpSourceGroup,'juniDvmrpNotificationGroup':juniDvmrpNotificationGroup,_A0:juniDvmrpBaseGroup2,_A1:juniDvmrpInterfaceGroup2})