_r='bsIpv6FHSSourceGuardEntryIpv6Addr'
_q='bsIpv6FHSSourceGuardEntryIfIndex'
_p='bsIpv6FHSSourceGuardIfIndex'
_o='ipv6NDRedir'
_n='ipv6NDRA'
_m='ipv6NDRS'
_l='ipv6NDNA'
_k='ipv6NDNS'
_j='bsIpv6FHSSbtSrcIp'
_i='bsIpv6FHSSbtVlan'
_h='bsIpv6FHSSbtInterfaceIndex'
_g='FhsRaRouterPrefMax'
_f='bsIpv6FHSRagPolicyName'
_e='bsIpv6FHSDhcpv6gPolicyName'
_d='FhsDhcpv6GuardDeviceRole'
_c='bsIpv6FHSPolicyPortMapIfIndex'
_b='bsIpv6FHSMacAccessListMac'
_a='bsIpv6FHSMacAccessListName'
_Z='bsIpv6FHSIpv6AccessListPrefixMaskLen'
_Y='bsIpv6FHSIpv6AccessListPrefix'
_X='bsIpv6FHSIpv6AccessListName'
_W='bsIpv6FhsTrapPktDropReason'
_V='bsIpv6FHSNDVlanID'
_U='bsIpv6FHSNDIpv6Address'
_T='bsIpv6FHSNDInterfaceIndex'
_S='bsIpv6NDInspectionNotificationMsgType'
_R='bsIpv6NDInspectionNotificationClientMACAddr'
_Q='FhsRaGuardDeviceRole'
_P='FhsAccessType'
_O='none'
_N='bsIpv6FHSTrapVlanID'
_M='bsIpv6FHSTrapInterfaceIndex'
_L='bsIpv6FHSTrapMsgType'
_K='bsIpv6FHSTrapClientIpv6Address'
_J='bsIpv6FHSTrapClientMACAddr'
_I='obsolete'
_H='accessible-for-notify'
_G='TruthValue'
_F='not-accessible'
_E='read-only'
_D='Integer32'
_C='read-write'
_B='BAYSTACK-IPV6-FIRST-HOP-SEC-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
Ipv6Address,=mibBuilder.importSymbols('IPV6-TC','Ipv6Address')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_G)
bayStackMibs,=mibBuilder.importSymbols('SYNOPTICS-ROOT-MIB','bayStackMibs')
bayStackIpv6FirstHopSecMib=ModuleIdentity((1,3,6,1,4,1,45,5,45))
if mibBuilder.loadTexts:bayStackIpv6FirstHopSecMib.setRevisions(('2016-11-03 00:00','2015-07-02 00:00','2015-06-30 00:00','2015-06-09 00:00','2015-04-08 00:00','2014-03-20 00:00','2014-01-17 00:00','2013-11-18 00:00','2013-10-11 00:00','2013-08-20 00:00','2013-05-27 00:00'))
class FhsRaGuardDeviceRole(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('router',1),('host',2),(_O,3)))
class FhsRaManagedConfigFlag(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_O,1),('on',2),('off',3)))
class FhsRaRouterPrefMax(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_O,1),('high',2),('medium',3),('low',4)))
class FhsDhcpv6GuardDeviceRole(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('server',1),('client',2),(_O,3)))
class FhsListName(DisplayString):status=_A;subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
class FhsAccessType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('allow',1),('deny',2)))
class FhsSbtState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('incomplete',1),('reachable',2),('stale',3),('down',4)))
class FhsSbtType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('static',1),('nd',2),('dhcp',3)))
_BsIpv6FirstHopSecNotifications_ObjectIdentity=ObjectIdentity
bsIpv6FirstHopSecNotifications=_BsIpv6FirstHopSecNotifications_ObjectIdentity((1,3,6,1,4,1,45,5,45,0))
_BsIpv6FirstHopSecObjects_ObjectIdentity=ObjectIdentity
bsIpv6FirstHopSecObjects=_BsIpv6FirstHopSecObjects_ObjectIdentity((1,3,6,1,4,1,45,5,45,1))
_BsIpv6FHSScalVar_ObjectIdentity=ObjectIdentity
bsIpv6FHSScalVar=_BsIpv6FHSScalVar_ObjectIdentity((1,3,6,1,4,1,45,5,45,1,1))
class _BsIpv6FHSAdmin_Type(TruthValue):defaultValue=2
_BsIpv6FHSAdmin_Type.__name__=_G
_BsIpv6FHSAdmin_Object=MibScalar
bsIpv6FHSAdmin=_BsIpv6FHSAdmin_Object((1,3,6,1,4,1,45,5,45,1,1,1),_BsIpv6FHSAdmin_Type())
bsIpv6FHSAdmin.setMaxAccess(_C)
if mibBuilder.loadTexts:bsIpv6FHSAdmin.setStatus(_A)
class _BsIpv6FHSRagAdmin_Type(TruthValue):defaultValue=2
_BsIpv6FHSRagAdmin_Type.__name__=_G
_BsIpv6FHSRagAdmin_Object=MibScalar
bsIpv6FHSRagAdmin=_BsIpv6FHSRagAdmin_Object((1,3,6,1,4,1,45,5,45,1,1,2),_BsIpv6FHSRagAdmin_Type())
bsIpv6FHSRagAdmin.setMaxAccess(_C)
if mibBuilder.loadTexts:bsIpv6FHSRagAdmin.setStatus(_A)
class _BsIpv6FHSDhcpv6gAdmin_Type(TruthValue):defaultValue=2
_BsIpv6FHSDhcpv6gAdmin_Type.__name__=_G
_BsIpv6FHSDhcpv6gAdmin_Object=MibScalar
bsIpv6FHSDhcpv6gAdmin=_BsIpv6FHSDhcpv6gAdmin_Object((1,3,6,1,4,1,45,5,45,1,1,3),_BsIpv6FHSDhcpv6gAdmin_Type())
bsIpv6FHSDhcpv6gAdmin.setMaxAccess(_C)
if mibBuilder.loadTexts:bsIpv6FHSDhcpv6gAdmin.setStatus(_A)
class _BsIpv6FHSNdInspectAdmin_Type(TruthValue):defaultValue=2
_BsIpv6FHSNdInspectAdmin_Type.__name__=_G
_BsIpv6FHSNdInspectAdmin_Object=MibScalar
bsIpv6FHSNdInspectAdmin=_BsIpv6FHSNdInspectAdmin_Object((1,3,6,1,4,1,45,5,45,1,1,4),_BsIpv6FHSNdInspectAdmin_Type())
bsIpv6FHSNdInspectAdmin.setMaxAccess(_C)
if mibBuilder.loadTexts:bsIpv6FHSNdInspectAdmin.setStatus(_A)
class _BsIpv6FHSMaxDynSbtEntries_Type(Integer32):defaultValue=1024;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_BsIpv6FHSMaxDynSbtEntries_Type.__name__=_D
_BsIpv6FHSMaxDynSbtEntries_Object=MibScalar
bsIpv6FHSMaxDynSbtEntries=_BsIpv6FHSMaxDynSbtEntries_Object((1,3,6,1,4,1,45,5,45,1,1,5),_BsIpv6FHSMaxDynSbtEntries_Type())
bsIpv6FHSMaxDynSbtEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:bsIpv6FHSMaxDynSbtEntries.setStatus(_A)
class _BsIpv6FHSSbtReachLifeTime_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,864000))
_BsIpv6FHSSbtReachLifeTime_Type.__name__=_D
_BsIpv6FHSSbtReachLifeTime_Object=MibScalar
bsIpv6FHSSbtReachLifeTime=_BsIpv6FHSSbtReachLifeTime_Object((1,3,6,1,4,1,45,5,45,1,1,6),_BsIpv6FHSSbtReachLifeTime_Type())
bsIpv6FHSSbtReachLifeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:bsIpv6FHSSbtReachLifeTime.setStatus(_A)
class _BsIpv6FHSSbtStaleLifeTime_Type(Integer32):defaultValue=86400;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400))
_BsIpv6FHSSbtStaleLifeTime_Type.__name__=_D
_BsIpv6FHSSbtStaleLifeTime_Object=MibScalar
bsIpv6FHSSbtStaleLifeTime=_BsIpv6FHSSbtStaleLifeTime_Object((1,3,6,1,4,1,45,5,45,1,1,7),_BsIpv6FHSSbtStaleLifeTime_Type())
bsIpv6FHSSbtStaleLifeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:bsIpv6FHSSbtStaleLifeTime.setStatus(_A)
class _BsIpv6FHSSbtDownLifeTime_Type(Integer32):defaultValue=86400;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400))
_BsIpv6FHSSbtDownLifeTime_Type.__name__=_D
_BsIpv6FHSSbtDownLifeTime_Object=MibScalar
bsIpv6FHSSbtDownLifeTime=_BsIpv6FHSSbtDownLifeTime_Object((1,3,6,1,4,1,45,5,45,1,1,8),_BsIpv6FHSSbtDownLifeTime_Type())
bsIpv6FHSSbtDownLifeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:bsIpv6FHSSbtDownLifeTime.setStatus(_A)
_BsIpv6FHSSbtTblOverFlow_Type=Counter32
_BsIpv6FHSSbtTblOverFlow_Object=MibScalar
bsIpv6FHSSbtTblOverFlow=_BsIpv6FHSSbtTblOverFlow_Object((1,3,6,1,4,1,45,5,45,1,1,9),_BsIpv6FHSSbtTblOverFlow_Type())
bsIpv6FHSSbtTblOverFlow.setMaxAccess(_E)
if mibBuilder.loadTexts:bsIpv6FHSSbtTblOverFlow.setStatus(_A)
_BsIpv6FHSIpv6AccessListTable_Object=MibTable
bsIpv6FHSIpv6AccessListTable=_BsIpv6FHSIpv6AccessListTable_Object((1,3,6,1,4,1,45,5,45,1,2))
if mibBuilder.loadTexts:bsIpv6FHSIpv6AccessListTable.setStatus(_A)
_BsIpv6FHSIpv6AccessListEntry_Object=MibTableRow
bsIpv6FHSIpv6AccessListEntry=_BsIpv6FHSIpv6AccessListEntry_Object((1,3,6,1,4,1,45,5,45,1,2,1))
bsIpv6FHSIpv6AccessListEntry.setIndexNames((0,_B,_X),(0,_B,_Y),(0,_B,_Z))
if mibBuilder.loadTexts:bsIpv6FHSIpv6AccessListEntry.setStatus(_A)
_BsIpv6FHSIpv6AccessListName_Type=FhsListName
_BsIpv6FHSIpv6AccessListName_Object=MibTableColumn
bsIpv6FHSIpv6AccessListName=_BsIpv6FHSIpv6AccessListName_Object((1,3,6,1,4,1,45,5,45,1,2,1,1),_BsIpv6FHSIpv6AccessListName_Type())
bsIpv6FHSIpv6AccessListName.setMaxAccess(_F)
if mibBuilder.loadTexts:bsIpv6FHSIpv6AccessListName.setStatus(_A)
_BsIpv6FHSIpv6AccessListPrefix_Type=Ipv6Address
_BsIpv6FHSIpv6AccessListPrefix_Object=MibTableColumn
bsIpv6FHSIpv6AccessListPrefix=_BsIpv6FHSIpv6AccessListPrefix_Object((1,3,6,1,4,1,45,5,45,1,2,1,2),_BsIpv6FHSIpv6AccessListPrefix_Type())
bsIpv6FHSIpv6AccessListPrefix.setMaxAccess(_F)
if mibBuilder.loadTexts:bsIpv6FHSIpv6AccessListPrefix.setStatus(_A)
class _BsIpv6FHSIpv6AccessListPrefixMaskLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_BsIpv6FHSIpv6AccessListPrefixMaskLen_Type.__name__=_D
_BsIpv6FHSIpv6AccessListPrefixMaskLen_Object=MibTableColumn
bsIpv6FHSIpv6AccessListPrefixMaskLen=_BsIpv6FHSIpv6AccessListPrefixMaskLen_Object((1,3,6,1,4,1,45,5,45,1,2,1,3),_BsIpv6FHSIpv6AccessListPrefixMaskLen_Type())
bsIpv6FHSIpv6AccessListPrefixMaskLen.setMaxAccess(_F)
if mibBuilder.loadTexts:bsIpv6FHSIpv6AccessListPrefixMaskLen.setStatus(_A)
class _BsIpv6FHSIpv6AccessListMaskLenFrom_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_BsIpv6FHSIpv6AccessListMaskLenFrom_Type.__name__=_D
_BsIpv6FHSIpv6AccessListMaskLenFrom_Object=MibTableColumn
bsIpv6FHSIpv6AccessListMaskLenFrom=_BsIpv6FHSIpv6AccessListMaskLenFrom_Object((1,3,6,1,4,1,45,5,45,1,2,1,4),_BsIpv6FHSIpv6AccessListMaskLenFrom_Type())
bsIpv6FHSIpv6AccessListMaskLenFrom.setMaxAccess(_C)
if mibBuilder.loadTexts:bsIpv6FHSIpv6AccessListMaskLenFrom.setStatus(_A)
class _BsIpv6FHSIpv6AccessListMaskLenTo_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_BsIpv6FHSIpv6AccessListMaskLenTo_Type.__name__=_D
_BsIpv6FHSIpv6AccessListMaskLenTo_Object=MibTableColumn
bsIpv6FHSIpv6AccessListMaskLenTo=_BsIpv6FHSIpv6AccessListMaskLenTo_Object((1,3,6,1,4,1,45,5,45,1,2,1,5),_BsIpv6FHSIpv6AccessListMaskLenTo_Type())
bsIpv6FHSIpv6AccessListMaskLenTo.setMaxAccess(_C)
if mibBuilder.loadTexts:bsIpv6FHSIpv6AccessListMaskLenTo.setStatus(_A)
class _BsIpv6FHSIpv6AccessListAccessType_Type(FhsAccessType):defaultValue=1
_BsIpv6FHSIpv6AccessListAccessType_Type.__name__=_P
_BsIpv6FHSIpv6AccessListAccessType_Object=MibTableColumn
bsIpv6FHSIpv6AccessListAccessType=_BsIpv6FHSIpv6AccessListAccessType_Object((1,3,6,1,4,1,45,5,45,1,2,1,6),_BsIpv6FHSIpv6AccessListAccessType_Type())
bsIpv6FHSIpv6AccessListAccessType.setMaxAccess(_C)
if mibBuilder.loadTexts:bsIpv6FHSIpv6AccessListAccessType.setStatus(_A)
_BsIpv6FHSIpv6AccessListRowStatus_Type=RowStatus
_BsIpv6FHSIpv6AccessListRowStatus_Object=MibTableColumn
bsIpv6FHSIpv6AccessListRowStatus=_BsIpv6FHSIpv6AccessListRowStatus_Object((1,3,6,1,4,1,45,5,45,1,2,1,7),_BsIpv6FHSIpv6AccessListRowStatus_Type())
bsIpv6FHSIpv6AccessListRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:bsIpv6FHSIpv6AccessListRowStatus.setStatus(_A)
_BsIpv6FHSMacAccessListTable_Object=MibTable
bsIpv6FHSMacAccessListTable=_BsIpv6FHSMacAccessListTable_Object((1,3,6,1,4,1,45,5,45,1,3))
if mibBuilder.loadTexts:bsIpv6FHSMacAccessListTable.setStatus(_A)
_BsIpv6FHSMacAccessListEntry_Object=MibTableRow
bsIpv6FHSMacAccessListEntry=_BsIpv6FHSMacAccessListEntry_Object((1,3,6,1,4,1,45,5,45,1,3,3))
bsIpv6FHSMacAccessListEntry.setIndexNames((0,_B,_a),(0,_B,_b))
if mibBuilder.loadTexts:bsIpv6FHSMacAccessListEntry.setStatus(_A)
_BsIpv6FHSMacAccessListName_Type=FhsListName
_BsIpv6FHSMacAccessListName_Object=MibTableColumn
bsIpv6FHSMacAccessListName=_BsIpv6FHSMacAccessListName_Object((1,3,6,1,4,1,45,5,45,1,3,3,1),_BsIpv6FHSMacAccessListName_Type())
bsIpv6FHSMacAccessListName.setMaxAccess(_F)
if mibBuilder.loadTexts:bsIpv6FHSMacAccessListName.setStatus(_A)
_BsIpv6FHSMacAccessListMac_Type=MacAddress
_BsIpv6FHSMacAccessListMac_Object=MibTableColumn
bsIpv6FHSMacAccessListMac=_BsIpv6FHSMacAccessListMac_Object((1,3,6,1,4,1,45,5,45,1,3,3,2),_BsIpv6FHSMacAccessListMac_Type())
bsIpv6FHSMacAccessListMac.setMaxAccess(_F)
if mibBuilder.loadTexts:bsIpv6FHSMacAccessListMac.setStatus(_A)
class _BsIpv6FHSMacAccessListAccessType_Type(FhsAccessType):defaultValue=1
_BsIpv6FHSMacAccessListAccessType_Type.__name__=_P
_BsIpv6FHSMacAccessListAccessType_Object=MibTableColumn
bsIpv6FHSMacAccessListAccessType=_BsIpv6FHSMacAccessListAccessType_Object((1,3,6,1,4,1,45,5,45,1,3,3,3),_BsIpv6FHSMacAccessListAccessType_Type())
bsIpv6FHSMacAccessListAccessType.setMaxAccess(_C)
if mibBuilder.loadTexts:bsIpv6FHSMacAccessListAccessType.setStatus(_A)
_BsIpv6FHSMacAccessListRowStatus_Type=RowStatus
_BsIpv6FHSMacAccessListRowStatus_Object=MibTableColumn
bsIpv6FHSMacAccessListRowStatus=_BsIpv6FHSMacAccessListRowStatus_Object((1,3,6,1,4,1,45,5,45,1,3,3,4),_BsIpv6FHSMacAccessListRowStatus_Type())
bsIpv6FHSMacAccessListRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:bsIpv6FHSMacAccessListRowStatus.setStatus(_A)
_BsIpv6FHSPolicyPortMapTable_Object=MibTable
bsIpv6FHSPolicyPortMapTable=_BsIpv6FHSPolicyPortMapTable_Object((1,3,6,1,4,1,45,5,45,1,4))
if mibBuilder.loadTexts:bsIpv6FHSPolicyPortMapTable.setStatus(_A)
_BsIpv6FHSPolicyPortMapEntry_Object=MibTableRow
bsIpv6FHSPolicyPortMapEntry=_BsIpv6FHSPolicyPortMapEntry_Object((1,3,6,1,4,1,45,5,45,1,4,1))
bsIpv6FHSPolicyPortMapEntry.setIndexNames((0,_B,_c))
if mibBuilder.loadTexts:bsIpv6FHSPolicyPortMapEntry.setStatus(_A)
_BsIpv6FHSPolicyPortMapIfIndex_Type=InterfaceIndex
_BsIpv6FHSPolicyPortMapIfIndex_Object=MibTableColumn
bsIpv6FHSPolicyPortMapIfIndex=_BsIpv6FHSPolicyPortMapIfIndex_Object((1,3,6,1,4,1,45,5,45,1,4,1,1),_BsIpv6FHSPolicyPortMapIfIndex_Type())
bsIpv6FHSPolicyPortMapIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:bsIpv6FHSPolicyPortMapIfIndex.setStatus(_A)
_BsIpv6FHSPolicyPortMapDhcpv6gPolicyName_Type=FhsListName
_BsIpv6FHSPolicyPortMapDhcpv6gPolicyName_Object=MibTableColumn
bsIpv6FHSPolicyPortMapDhcpv6gPolicyName=_BsIpv6FHSPolicyPortMapDhcpv6gPolicyName_Object((1,3,6,1,4,1,45,5,45,1,4,1,2),_BsIpv6FHSPolicyPortMapDhcpv6gPolicyName_Type())
bsIpv6FHSPolicyPortMapDhcpv6gPolicyName.setMaxAccess(_C)
if mibBuilder.loadTexts:bsIpv6FHSPolicyPortMapDhcpv6gPolicyName.setStatus(_A)
_BsIpv6FHSPolicyPortMapRagPolicyName_Type=FhsListName
_BsIpv6FHSPolicyPortMapRagPolicyName_Object=MibTableColumn
bsIpv6FHSPolicyPortMapRagPolicyName=_BsIpv6FHSPolicyPortMapRagPolicyName_Object((1,3,6,1,4,1,45,5,45,1,4,1,3),_BsIpv6FHSPolicyPortMapRagPolicyName_Type())
bsIpv6FHSPolicyPortMapRagPolicyName.setMaxAccess(_C)
if mibBuilder.loadTexts:bsIpv6FHSPolicyPortMapRagPolicyName.setStatus(_A)
class _BsIpv6FHSPolicyPortMapNDAdmin_Type(TruthValue):defaultValue=2
_BsIpv6FHSPolicyPortMapNDAdmin_Type.__name__=_G
_BsIpv6FHSPolicyPortMapNDAdmin_Object=MibTableColumn
bsIpv6FHSPolicyPortMapNDAdmin=_BsIpv6FHSPolicyPortMapNDAdmin_Object((1,3,6,1,4,1,45,5,45,1,4,1,4),_BsIpv6FHSPolicyPortMapNDAdmin_Type())
bsIpv6FHSPolicyPortMapNDAdmin.setMaxAccess(_C)
if mibBuilder.loadTexts:bsIpv6FHSPolicyPortMapNDAdmin.setStatus(_A)
class _BsIpv6FHSPolicyPortMapSbtDynLearnAdmin_Type(TruthValue):defaultValue=1
_BsIpv6FHSPolicyPortMapSbtDynLearnAdmin_Type.__name__=_G
_BsIpv6FHSPolicyPortMapSbtDynLearnAdmin_Object=MibTableColumn
bsIpv6FHSPolicyPortMapSbtDynLearnAdmin=_BsIpv6FHSPolicyPortMapSbtDynLearnAdmin_Object((1,3,6,1,4,1,45,5,45,1,4,1,5),_BsIpv6FHSPolicyPortMapSbtDynLearnAdmin_Type())
bsIpv6FHSPolicyPortMapSbtDynLearnAdmin.setMaxAccess(_C)
if mibBuilder.loadTexts:bsIpv6FHSPolicyPortMapSbtDynLearnAdmin.setStatus(_A)
_BsIpv6FHSPolicyPortMapTotDhcpv6PktRcv_Type=Counter32
_BsIpv6FHSPolicyPortMapTotDhcpv6PktRcv_Object=MibTableColumn
bsIpv6FHSPolicyPortMapTotDhcpv6PktRcv=_BsIpv6FHSPolicyPortMapTotDhcpv6PktRcv_Object((1,3,6,1,4,1,45,5,45,1,4,1,6),_BsIpv6FHSPolicyPortMapTotDhcpv6PktRcv_Type())
bsIpv6FHSPolicyPortMapTotDhcpv6PktRcv.setMaxAccess(_E)
if mibBuilder.loadTexts:bsIpv6FHSPolicyPortMapTotDhcpv6PktRcv.setStatus(_A)
_BsIpv6FHSPolicyPortMapTotDhcpv6PktDropped_Type=Counter32
_BsIpv6FHSPolicyPortMapTotDhcpv6PktDropped_Object=MibTableColumn
bsIpv6FHSPolicyPortMapTotDhcpv6PktDropped=_BsIpv6FHSPolicyPortMapTotDhcpv6PktDropped_Object((1,3,6,1,4,1,45,5,45,1,4,1,7),_BsIpv6FHSPolicyPortMapTotDhcpv6PktDropped_Type())
bsIpv6FHSPolicyPortMapTotDhcpv6PktDropped.setMaxAccess(_E)
if mibBuilder.loadTexts:bsIpv6FHSPolicyPortMapTotDhcpv6PktDropped.setStatus(_A)
_BsIpv6FHSPolicyPortMapTotRaPktRcv_Type=Counter32
_BsIpv6FHSPolicyPortMapTotRaPktRcv_Object=MibTableColumn
bsIpv6FHSPolicyPortMapTotRaPktRcv=_BsIpv6FHSPolicyPortMapTotRaPktRcv_Object((1,3,6,1,4,1,45,5,45,1,4,1,8),_BsIpv6FHSPolicyPortMapTotRaPktRcv_Type())
bsIpv6FHSPolicyPortMapTotRaPktRcv.setMaxAccess(_E)
if mibBuilder.loadTexts:bsIpv6FHSPolicyPortMapTotRaPktRcv.setStatus(_A)
_BsIpv6FHSPolicyPortMapTotRaPktDropped_Type=Counter32
_BsIpv6FHSPolicyPortMapTotRaPktDropped_Object=MibTableColumn
bsIpv6FHSPolicyPortMapTotRaPktDropped=_BsIpv6FHSPolicyPortMapTotRaPktDropped_Object((1,3,6,1,4,1,45,5,45,1,4,1,9),_BsIpv6FHSPolicyPortMapTotRaPktDropped_Type())
bsIpv6FHSPolicyPortMapTotRaPktDropped.setMaxAccess(_E)
if mibBuilder.loadTexts:bsIpv6FHSPolicyPortMapTotRaPktDropped.setStatus(_A)
_BsIpv6FHSPolicyPortMapTotNdPktRcv_Type=Counter32
_BsIpv6FHSPolicyPortMapTotNdPktRcv_Object=MibTableColumn
bsIpv6FHSPolicyPortMapTotNdPktRcv=_BsIpv6FHSPolicyPortMapTotNdPktRcv_Object((1,3,6,1,4,1,45,5,45,1,4,1,10),_BsIpv6FHSPolicyPortMapTotNdPktRcv_Type())
bsIpv6FHSPolicyPortMapTotNdPktRcv.setMaxAccess(_E)
if mibBuilder.loadTexts:bsIpv6FHSPolicyPortMapTotNdPktRcv.setStatus(_A)
_BsIpv6FHSPolicyPortMapTotNdPktDropped_Type=Counter32
_BsIpv6FHSPolicyPortMapTotNdPktDropped_Object=MibTableColumn
bsIpv6FHSPolicyPortMapTotNdPktDropped=_BsIpv6FHSPolicyPortMapTotNdPktDropped_Object((1,3,6,1,4,1,45,5,45,1,4,1,11),_BsIpv6FHSPolicyPortMapTotNdPktDropped_Type())
bsIpv6FHSPolicyPortMapTotNdPktDropped.setMaxAccess(_E)
if mibBuilder.loadTexts:bsIpv6FHSPolicyPortMapTotNdPktDropped.setStatus(_A)
class _BsIpv6FHSPolicyPortMapClearDhcpGuardStats_Type(TruthValue):defaultValue=2
_BsIpv6FHSPolicyPortMapClearDhcpGuardStats_Type.__name__=_G
_BsIpv6FHSPolicyPortMapClearDhcpGuardStats_Object=MibTableColumn
bsIpv6FHSPolicyPortMapClearDhcpGuardStats=_BsIpv6FHSPolicyPortMapClearDhcpGuardStats_Object((1,3,6,1,4,1,45,5,45,1,4,1,12),_BsIpv6FHSPolicyPortMapClearDhcpGuardStats_Type())
bsIpv6FHSPolicyPortMapClearDhcpGuardStats.setMaxAccess(_C)
if mibBuilder.loadTexts:bsIpv6FHSPolicyPortMapClearDhcpGuardStats.setStatus(_A)
class _BsIpv6FHSPolicyPortMapClearRaGuardStats_Type(TruthValue):defaultValue=2
_BsIpv6FHSPolicyPortMapClearRaGuardStats_Type.__name__=_G
_BsIpv6FHSPolicyPortMapClearRaGuardStats_Object=MibTableColumn
bsIpv6FHSPolicyPortMapClearRaGuardStats=_BsIpv6FHSPolicyPortMapClearRaGuardStats_Object((1,3,6,1,4,1,45,5,45,1,4,1,13),_BsIpv6FHSPolicyPortMapClearRaGuardStats_Type())
bsIpv6FHSPolicyPortMapClearRaGuardStats.setMaxAccess(_C)
if mibBuilder.loadTexts:bsIpv6FHSPolicyPortMapClearRaGuardStats.setStatus(_A)
class _BsIpv6FHSPolicyPortMapClearNDInspectStats_Type(TruthValue):defaultValue=2
_BsIpv6FHSPolicyPortMapClearNDInspectStats_Type.__name__=_G
_BsIpv6FHSPolicyPortMapClearNDInspectStats_Object=MibTableColumn
bsIpv6FHSPolicyPortMapClearNDInspectStats=_BsIpv6FHSPolicyPortMapClearNDInspectStats_Object((1,3,6,1,4,1,45,5,45,1,4,1,14),_BsIpv6FHSPolicyPortMapClearNDInspectStats_Type())
bsIpv6FHSPolicyPortMapClearNDInspectStats.setMaxAccess(_C)
if mibBuilder.loadTexts:bsIpv6FHSPolicyPortMapClearNDInspectStats.setStatus(_A)
_BsIpv6FHSPolicyPortMapRowStatus_Type=RowStatus
_BsIpv6FHSPolicyPortMapRowStatus_Object=MibTableColumn
bsIpv6FHSPolicyPortMapRowStatus=_BsIpv6FHSPolicyPortMapRowStatus_Object((1,3,6,1,4,1,45,5,45,1,4,1,15),_BsIpv6FHSPolicyPortMapRowStatus_Type())
bsIpv6FHSPolicyPortMapRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:bsIpv6FHSPolicyPortMapRowStatus.setStatus(_A)
class _BsIpv6FHSPolicyPortMapDhcpv6gDeviceRole_Type(FhsDhcpv6GuardDeviceRole):defaultValue=1
_BsIpv6FHSPolicyPortMapDhcpv6gDeviceRole_Type.__name__=_d
_BsIpv6FHSPolicyPortMapDhcpv6gDeviceRole_Object=MibTableColumn
bsIpv6FHSPolicyPortMapDhcpv6gDeviceRole=_BsIpv6FHSPolicyPortMapDhcpv6gDeviceRole_Object((1,3,6,1,4,1,45,5,45,1,4,1,16),_BsIpv6FHSPolicyPortMapDhcpv6gDeviceRole_Type())
bsIpv6FHSPolicyPortMapDhcpv6gDeviceRole.setMaxAccess(_C)
if mibBuilder.loadTexts:bsIpv6FHSPolicyPortMapDhcpv6gDeviceRole.setStatus(_A)
class _BsIpv6FHSPolicyPortMapRagDeviceRole_Type(FhsRaGuardDeviceRole):defaultValue=1
_BsIpv6FHSPolicyPortMapRagDeviceRole_Type.__name__=_Q
_BsIpv6FHSPolicyPortMapRagDeviceRole_Object=MibTableColumn
bsIpv6FHSPolicyPortMapRagDeviceRole=_BsIpv6FHSPolicyPortMapRagDeviceRole_Object((1,3,6,1,4,1,45,5,45,1,4,1,17),_BsIpv6FHSPolicyPortMapRagDeviceRole_Type())
bsIpv6FHSPolicyPortMapRagDeviceRole.setMaxAccess(_C)
if mibBuilder.loadTexts:bsIpv6FHSPolicyPortMapRagDeviceRole.setStatus(_A)
_BsIpv6FHSDhcpv6gPolicyListTable_Object=MibTable
bsIpv6FHSDhcpv6gPolicyListTable=_BsIpv6FHSDhcpv6gPolicyListTable_Object((1,3,6,1,4,1,45,5,45,1,5))
if mibBuilder.loadTexts:bsIpv6FHSDhcpv6gPolicyListTable.setStatus(_A)
_BsIpv6FHSDhcpv6gPolicyListEntry_Object=MibTableRow
bsIpv6FHSDhcpv6gPolicyListEntry=_BsIpv6FHSDhcpv6gPolicyListEntry_Object((1,3,6,1,4,1,45,5,45,1,5,1))
bsIpv6FHSDhcpv6gPolicyListEntry.setIndexNames((0,_B,_e))
if mibBuilder.loadTexts:bsIpv6FHSDhcpv6gPolicyListEntry.setStatus(_A)
_BsIpv6FHSDhcpv6gPolicyName_Type=FhsListName
_BsIpv6FHSDhcpv6gPolicyName_Object=MibTableColumn
bsIpv6FHSDhcpv6gPolicyName=_BsIpv6FHSDhcpv6gPolicyName_Object((1,3,6,1,4,1,45,5,45,1,5,1,1),_BsIpv6FHSDhcpv6gPolicyName_Type())
bsIpv6FHSDhcpv6gPolicyName.setMaxAccess(_F)
if mibBuilder.loadTexts:bsIpv6FHSDhcpv6gPolicyName.setStatus(_A)
_BsIpv6FHSDhcpv6gDeviceRole_Type=FhsDhcpv6GuardDeviceRole
_BsIpv6FHSDhcpv6gDeviceRole_Object=MibTableColumn
bsIpv6FHSDhcpv6gDeviceRole=_BsIpv6FHSDhcpv6gDeviceRole_Object((1,3,6,1,4,1,45,5,45,1,5,1,2),_BsIpv6FHSDhcpv6gDeviceRole_Type())
bsIpv6FHSDhcpv6gDeviceRole.setMaxAccess(_C)
if mibBuilder.loadTexts:bsIpv6FHSDhcpv6gDeviceRole.setStatus(_A)
_BsIpv6FHSDhcpv6gServerAccessListName_Type=FhsListName
_BsIpv6FHSDhcpv6gServerAccessListName_Object=MibTableColumn
bsIpv6FHSDhcpv6gServerAccessListName=_BsIpv6FHSDhcpv6gServerAccessListName_Object((1,3,6,1,4,1,45,5,45,1,5,1,3),_BsIpv6FHSDhcpv6gServerAccessListName_Type())
bsIpv6FHSDhcpv6gServerAccessListName.setMaxAccess(_C)
if mibBuilder.loadTexts:bsIpv6FHSDhcpv6gServerAccessListName.setStatus(_A)
_BsIpv6FHSDhcpv6gReplyPrefixListName_Type=FhsListName
_BsIpv6FHSDhcpv6gReplyPrefixListName_Object=MibTableColumn
bsIpv6FHSDhcpv6gReplyPrefixListName=_BsIpv6FHSDhcpv6gReplyPrefixListName_Object((1,3,6,1,4,1,45,5,45,1,5,1,4),_BsIpv6FHSDhcpv6gReplyPrefixListName_Type())
bsIpv6FHSDhcpv6gReplyPrefixListName.setMaxAccess(_C)
if mibBuilder.loadTexts:bsIpv6FHSDhcpv6gReplyPrefixListName.setStatus(_A)
class _BsIpv6FHSDhcpv6gPrefLimitMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BsIpv6FHSDhcpv6gPrefLimitMin_Type.__name__=_D
_BsIpv6FHSDhcpv6gPrefLimitMin_Object=MibTableColumn
bsIpv6FHSDhcpv6gPrefLimitMin=_BsIpv6FHSDhcpv6gPrefLimitMin_Object((1,3,6,1,4,1,45,5,45,1,5,1,5),_BsIpv6FHSDhcpv6gPrefLimitMin_Type())
bsIpv6FHSDhcpv6gPrefLimitMin.setMaxAccess(_C)
if mibBuilder.loadTexts:bsIpv6FHSDhcpv6gPrefLimitMin.setStatus(_A)
class _BsIpv6FHSDhcpv6gPrefLimitMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BsIpv6FHSDhcpv6gPrefLimitMax_Type.__name__=_D
_BsIpv6FHSDhcpv6gPrefLimitMax_Object=MibTableColumn
bsIpv6FHSDhcpv6gPrefLimitMax=_BsIpv6FHSDhcpv6gPrefLimitMax_Object((1,3,6,1,4,1,45,5,45,1,5,1,6),_BsIpv6FHSDhcpv6gPrefLimitMax_Type())
bsIpv6FHSDhcpv6gPrefLimitMax.setMaxAccess(_C)
if mibBuilder.loadTexts:bsIpv6FHSDhcpv6gPrefLimitMax.setStatus(_A)
_BsIpv6FHSDhcpv6gPolicyListRowStatus_Type=RowStatus
_BsIpv6FHSDhcpv6gPolicyListRowStatus_Object=MibTableColumn
bsIpv6FHSDhcpv6gPolicyListRowStatus=_BsIpv6FHSDhcpv6gPolicyListRowStatus_Object((1,3,6,1,4,1,45,5,45,1,5,1,7),_BsIpv6FHSDhcpv6gPolicyListRowStatus_Type())
bsIpv6FHSDhcpv6gPolicyListRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:bsIpv6FHSDhcpv6gPolicyListRowStatus.setStatus(_A)
_BsIpv6FHSRagPolicyListTable_Object=MibTable
bsIpv6FHSRagPolicyListTable=_BsIpv6FHSRagPolicyListTable_Object((1,3,6,1,4,1,45,5,45,1,6))
if mibBuilder.loadTexts:bsIpv6FHSRagPolicyListTable.setStatus(_A)
_BsIpv6FHSRagPolicyListEntry_Object=MibTableRow
bsIpv6FHSRagPolicyListEntry=_BsIpv6FHSRagPolicyListEntry_Object((1,3,6,1,4,1,45,5,45,1,6,1))
bsIpv6FHSRagPolicyListEntry.setIndexNames((0,_B,_f))
if mibBuilder.loadTexts:bsIpv6FHSRagPolicyListEntry.setStatus(_A)
_BsIpv6FHSRagPolicyName_Type=FhsListName
_BsIpv6FHSRagPolicyName_Object=MibTableColumn
bsIpv6FHSRagPolicyName=_BsIpv6FHSRagPolicyName_Object((1,3,6,1,4,1,45,5,45,1,6,1,1),_BsIpv6FHSRagPolicyName_Type())
bsIpv6FHSRagPolicyName.setMaxAccess(_F)
if mibBuilder.loadTexts:bsIpv6FHSRagPolicyName.setStatus(_A)
class _BsIpv6FHSRagDeviceRole_Type(FhsRaGuardDeviceRole):defaultValue=1
_BsIpv6FHSRagDeviceRole_Type.__name__=_Q
_BsIpv6FHSRagDeviceRole_Object=MibTableColumn
bsIpv6FHSRagDeviceRole=_BsIpv6FHSRagDeviceRole_Object((1,3,6,1,4,1,45,5,45,1,6,1,2),_BsIpv6FHSRagDeviceRole_Type())
bsIpv6FHSRagDeviceRole.setMaxAccess(_C)
if mibBuilder.loadTexts:bsIpv6FHSRagDeviceRole.setStatus(_A)
_BsIpv6FHSRagIpv6AccessListName_Type=FhsListName
_BsIpv6FHSRagIpv6AccessListName_Object=MibTableColumn
bsIpv6FHSRagIpv6AccessListName=_BsIpv6FHSRagIpv6AccessListName_Object((1,3,6,1,4,1,45,5,45,1,6,1,3),_BsIpv6FHSRagIpv6AccessListName_Type())
bsIpv6FHSRagIpv6AccessListName.setMaxAccess(_C)
if mibBuilder.loadTexts:bsIpv6FHSRagIpv6AccessListName.setStatus(_A)
_BsIpv6FHSRagIpv6PrefixListName_Type=FhsListName
_BsIpv6FHSRagIpv6PrefixListName_Object=MibTableColumn
bsIpv6FHSRagIpv6PrefixListName=_BsIpv6FHSRagIpv6PrefixListName_Object((1,3,6,1,4,1,45,5,45,1,6,1,4),_BsIpv6FHSRagIpv6PrefixListName_Type())
bsIpv6FHSRagIpv6PrefixListName.setMaxAccess(_C)
if mibBuilder.loadTexts:bsIpv6FHSRagIpv6PrefixListName.setStatus(_A)
_BsIpv6FHSRagMacListName_Type=FhsListName
_BsIpv6FHSRagMacListName_Object=MibTableColumn
bsIpv6FHSRagMacListName=_BsIpv6FHSRagMacListName_Object((1,3,6,1,4,1,45,5,45,1,6,1,5),_BsIpv6FHSRagMacListName_Type())
bsIpv6FHSRagMacListName.setMaxAccess(_C)
if mibBuilder.loadTexts:bsIpv6FHSRagMacListName.setStatus(_A)
_BsIpv6FHSRagManagedConfigFlag_Type=FhsRaManagedConfigFlag
_BsIpv6FHSRagManagedConfigFlag_Object=MibTableColumn
bsIpv6FHSRagManagedConfigFlag=_BsIpv6FHSRagManagedConfigFlag_Object((1,3,6,1,4,1,45,5,45,1,6,1,6),_BsIpv6FHSRagManagedConfigFlag_Type())
bsIpv6FHSRagManagedConfigFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:bsIpv6FHSRagManagedConfigFlag.setStatus(_A)
class _BsIpv6FHSRagRouterPrefMax_Type(FhsRaRouterPrefMax):defaultValue=1
_BsIpv6FHSRagRouterPrefMax_Type.__name__=_g
_BsIpv6FHSRagRouterPrefMax_Object=MibTableColumn
bsIpv6FHSRagRouterPrefMax=_BsIpv6FHSRagRouterPrefMax_Object((1,3,6,1,4,1,45,5,45,1,6,1,7),_BsIpv6FHSRagRouterPrefMax_Type())
bsIpv6FHSRagRouterPrefMax.setMaxAccess(_C)
if mibBuilder.loadTexts:bsIpv6FHSRagRouterPrefMax.setStatus(_A)
class _BsIpv6FHSRagHopLimitMin_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BsIpv6FHSRagHopLimitMin_Type.__name__=_D
_BsIpv6FHSRagHopLimitMin_Object=MibTableColumn
bsIpv6FHSRagHopLimitMin=_BsIpv6FHSRagHopLimitMin_Object((1,3,6,1,4,1,45,5,45,1,6,1,8),_BsIpv6FHSRagHopLimitMin_Type())
bsIpv6FHSRagHopLimitMin.setMaxAccess(_C)
if mibBuilder.loadTexts:bsIpv6FHSRagHopLimitMin.setStatus(_A)
class _BsIpv6FHSRagHopLimitMax_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BsIpv6FHSRagHopLimitMax_Type.__name__=_D
_BsIpv6FHSRagHopLimitMax_Object=MibTableColumn
bsIpv6FHSRagHopLimitMax=_BsIpv6FHSRagHopLimitMax_Object((1,3,6,1,4,1,45,5,45,1,6,1,9),_BsIpv6FHSRagHopLimitMax_Type())
bsIpv6FHSRagHopLimitMax.setMaxAccess(_C)
if mibBuilder.loadTexts:bsIpv6FHSRagHopLimitMax.setStatus(_A)
_BsIpv6FHSRagPolicyListRowStatus_Type=RowStatus
_BsIpv6FHSRagPolicyListRowStatus_Object=MibTableColumn
bsIpv6FHSRagPolicyListRowStatus=_BsIpv6FHSRagPolicyListRowStatus_Object((1,3,6,1,4,1,45,5,45,1,6,1,10),_BsIpv6FHSRagPolicyListRowStatus_Type())
bsIpv6FHSRagPolicyListRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:bsIpv6FHSRagPolicyListRowStatus.setStatus(_A)
_BsIpv6FHSSbtTable_Object=MibTable
bsIpv6FHSSbtTable=_BsIpv6FHSSbtTable_Object((1,3,6,1,4,1,45,5,45,1,7))
if mibBuilder.loadTexts:bsIpv6FHSSbtTable.setStatus(_A)
_BsIpv6FHSSbtListEntry_Object=MibTableRow
bsIpv6FHSSbtListEntry=_BsIpv6FHSSbtListEntry_Object((1,3,6,1,4,1,45,5,45,1,7,1))
bsIpv6FHSSbtListEntry.setIndexNames((0,_B,_h),(0,_B,_i),(0,_B,_j))
if mibBuilder.loadTexts:bsIpv6FHSSbtListEntry.setStatus(_A)
_BsIpv6FHSSbtInterfaceIndex_Type=InterfaceIndex
_BsIpv6FHSSbtInterfaceIndex_Object=MibTableColumn
bsIpv6FHSSbtInterfaceIndex=_BsIpv6FHSSbtInterfaceIndex_Object((1,3,6,1,4,1,45,5,45,1,7,1,1),_BsIpv6FHSSbtInterfaceIndex_Type())
bsIpv6FHSSbtInterfaceIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:bsIpv6FHSSbtInterfaceIndex.setStatus(_A)
class _BsIpv6FHSSbtVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_BsIpv6FHSSbtVlan_Type.__name__=_D
_BsIpv6FHSSbtVlan_Object=MibTableColumn
bsIpv6FHSSbtVlan=_BsIpv6FHSSbtVlan_Object((1,3,6,1,4,1,45,5,45,1,7,1,2),_BsIpv6FHSSbtVlan_Type())
bsIpv6FHSSbtVlan.setMaxAccess(_F)
if mibBuilder.loadTexts:bsIpv6FHSSbtVlan.setStatus(_A)
_BsIpv6FHSSbtSrcIp_Type=Ipv6Address
_BsIpv6FHSSbtSrcIp_Object=MibTableColumn
bsIpv6FHSSbtSrcIp=_BsIpv6FHSSbtSrcIp_Object((1,3,6,1,4,1,45,5,45,1,7,1,3),_BsIpv6FHSSbtSrcIp_Type())
bsIpv6FHSSbtSrcIp.setMaxAccess(_F)
if mibBuilder.loadTexts:bsIpv6FHSSbtSrcIp.setStatus(_A)
_BsIpv6FHSSbtLinkLayerAddress_Type=MacAddress
_BsIpv6FHSSbtLinkLayerAddress_Object=MibTableColumn
bsIpv6FHSSbtLinkLayerAddress=_BsIpv6FHSSbtLinkLayerAddress_Object((1,3,6,1,4,1,45,5,45,1,7,1,4),_BsIpv6FHSSbtLinkLayerAddress_Type())
bsIpv6FHSSbtLinkLayerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:bsIpv6FHSSbtLinkLayerAddress.setStatus(_A)
_BsIpv6FHSSbtLearnType_Type=FhsSbtType
_BsIpv6FHSSbtLearnType_Object=MibTableColumn
bsIpv6FHSSbtLearnType=_BsIpv6FHSSbtLearnType_Object((1,3,6,1,4,1,45,5,45,1,7,1,5),_BsIpv6FHSSbtLearnType_Type())
bsIpv6FHSSbtLearnType.setMaxAccess(_E)
if mibBuilder.loadTexts:bsIpv6FHSSbtLearnType.setStatus(_A)
_BsIpv6FHSSbtLearnPriority_Type=Integer32
_BsIpv6FHSSbtLearnPriority_Object=MibTableColumn
bsIpv6FHSSbtLearnPriority=_BsIpv6FHSSbtLearnPriority_Object((1,3,6,1,4,1,45,5,45,1,7,1,6),_BsIpv6FHSSbtLearnPriority_Type())
bsIpv6FHSSbtLearnPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:bsIpv6FHSSbtLearnPriority.setStatus(_A)
_BsIpv6FHSSbtLearnState_Type=FhsSbtState
_BsIpv6FHSSbtLearnState_Object=MibTableColumn
bsIpv6FHSSbtLearnState=_BsIpv6FHSSbtLearnState_Object((1,3,6,1,4,1,45,5,45,1,7,1,7),_BsIpv6FHSSbtLearnState_Type())
bsIpv6FHSSbtLearnState.setMaxAccess(_E)
if mibBuilder.loadTexts:bsIpv6FHSSbtLearnState.setStatus(_A)
_BsIpv6FHSSbtLearnAge_Type=Integer32
_BsIpv6FHSSbtLearnAge_Object=MibTableColumn
bsIpv6FHSSbtLearnAge=_BsIpv6FHSSbtLearnAge_Object((1,3,6,1,4,1,45,5,45,1,7,1,8),_BsIpv6FHSSbtLearnAge_Type())
bsIpv6FHSSbtLearnAge.setMaxAccess(_E)
if mibBuilder.loadTexts:bsIpv6FHSSbtLearnAge.setStatus(_A)
_BsIpv6FHSSbtRowStatus_Type=RowStatus
_BsIpv6FHSSbtRowStatus_Object=MibTableColumn
bsIpv6FHSSbtRowStatus=_BsIpv6FHSSbtRowStatus_Object((1,3,6,1,4,1,45,5,45,1,7,1,9),_BsIpv6FHSSbtRowStatus_Type())
bsIpv6FHSSbtRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:bsIpv6FHSSbtRowStatus.setStatus(_A)
_BsIpv6NDTrapNotificationObjects_ObjectIdentity=ObjectIdentity
bsIpv6NDTrapNotificationObjects=_BsIpv6NDTrapNotificationObjects_ObjectIdentity((1,3,6,1,4,1,45,5,45,1,8))
_BsIpv6NDInspectionNotificationClientMACAddr_Type=MacAddress
_BsIpv6NDInspectionNotificationClientMACAddr_Object=MibScalar
bsIpv6NDInspectionNotificationClientMACAddr=_BsIpv6NDInspectionNotificationClientMACAddr_Object((1,3,6,1,4,1,45,5,45,1,8,1),_BsIpv6NDInspectionNotificationClientMACAddr_Type())
bsIpv6NDInspectionNotificationClientMACAddr.setMaxAccess(_H)
if mibBuilder.loadTexts:bsIpv6NDInspectionNotificationClientMACAddr.setStatus(_I)
class _BsIpv6NDInspectionNotificationMsgType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_k,1),(_l,2),(_m,3),(_n,4),(_o,5)))
_BsIpv6NDInspectionNotificationMsgType_Type.__name__=_D
_BsIpv6NDInspectionNotificationMsgType_Object=MibScalar
bsIpv6NDInspectionNotificationMsgType=_BsIpv6NDInspectionNotificationMsgType_Object((1,3,6,1,4,1,45,5,45,1,8,2),_BsIpv6NDInspectionNotificationMsgType_Type())
bsIpv6NDInspectionNotificationMsgType.setMaxAccess(_H)
if mibBuilder.loadTexts:bsIpv6NDInspectionNotificationMsgType.setStatus(_I)
_BsIpv6FHSNDInterfaceIndex_Type=InterfaceIndex
_BsIpv6FHSNDInterfaceIndex_Object=MibScalar
bsIpv6FHSNDInterfaceIndex=_BsIpv6FHSNDInterfaceIndex_Object((1,3,6,1,4,1,45,5,45,1,8,3),_BsIpv6FHSNDInterfaceIndex_Type())
bsIpv6FHSNDInterfaceIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:bsIpv6FHSNDInterfaceIndex.setStatus(_I)
_BsIpv6FHSNDIpv6Address_Type=Ipv6Address
_BsIpv6FHSNDIpv6Address_Object=MibScalar
bsIpv6FHSNDIpv6Address=_BsIpv6FHSNDIpv6Address_Object((1,3,6,1,4,1,45,5,45,1,8,4),_BsIpv6FHSNDIpv6Address_Type())
bsIpv6FHSNDIpv6Address.setMaxAccess(_H)
if mibBuilder.loadTexts:bsIpv6FHSNDIpv6Address.setStatus(_I)
class _BsIpv6FHSNDVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_BsIpv6FHSNDVlanID_Type.__name__=_D
_BsIpv6FHSNDVlanID_Object=MibScalar
bsIpv6FHSNDVlanID=_BsIpv6FHSNDVlanID_Object((1,3,6,1,4,1,45,5,45,1,8,5),_BsIpv6FHSNDVlanID_Type())
bsIpv6FHSNDVlanID.setMaxAccess(_H)
if mibBuilder.loadTexts:bsIpv6FHSNDVlanID.setStatus(_I)
_BsIpv6FHSSourceGuardInterfaceConfigTable_Object=MibTable
bsIpv6FHSSourceGuardInterfaceConfigTable=_BsIpv6FHSSourceGuardInterfaceConfigTable_Object((1,3,6,1,4,1,45,5,45,1,9))
if mibBuilder.loadTexts:bsIpv6FHSSourceGuardInterfaceConfigTable.setStatus(_A)
_BsIpv6FHSSourceGuardInterfaceConfigEntry_Object=MibTableRow
bsIpv6FHSSourceGuardInterfaceConfigEntry=_BsIpv6FHSSourceGuardInterfaceConfigEntry_Object((1,3,6,1,4,1,45,5,45,1,9,1))
bsIpv6FHSSourceGuardInterfaceConfigEntry.setIndexNames((0,_B,_p))
if mibBuilder.loadTexts:bsIpv6FHSSourceGuardInterfaceConfigEntry.setStatus(_A)
_BsIpv6FHSSourceGuardIfIndex_Type=InterfaceIndex
_BsIpv6FHSSourceGuardIfIndex_Object=MibTableColumn
bsIpv6FHSSourceGuardIfIndex=_BsIpv6FHSSourceGuardIfIndex_Object((1,3,6,1,4,1,45,5,45,1,9,1,1),_BsIpv6FHSSourceGuardIfIndex_Type())
bsIpv6FHSSourceGuardIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:bsIpv6FHSSourceGuardIfIndex.setStatus(_A)
class _BsIpv6FHSSourceGuardInterfaceState_Type(TruthValue):defaultValue=2
_BsIpv6FHSSourceGuardInterfaceState_Type.__name__=_G
_BsIpv6FHSSourceGuardInterfaceState_Object=MibTableColumn
bsIpv6FHSSourceGuardInterfaceState=_BsIpv6FHSSourceGuardInterfaceState_Object((1,3,6,1,4,1,45,5,45,1,9,1,2),_BsIpv6FHSSourceGuardInterfaceState_Type())
bsIpv6FHSSourceGuardInterfaceState.setMaxAccess(_C)
if mibBuilder.loadTexts:bsIpv6FHSSourceGuardInterfaceState.setStatus(_A)
class _BsIpv6FHSSourceGuardMaxAddr_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,10))
_BsIpv6FHSSourceGuardMaxAddr_Type.__name__=_D
_BsIpv6FHSSourceGuardMaxAddr_Object=MibTableColumn
bsIpv6FHSSourceGuardMaxAddr=_BsIpv6FHSSourceGuardMaxAddr_Object((1,3,6,1,4,1,45,5,45,1,9,1,3),_BsIpv6FHSSourceGuardMaxAddr_Type())
bsIpv6FHSSourceGuardMaxAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:bsIpv6FHSSourceGuardMaxAddr.setStatus(_A)
_BsIpv6FHSSourceGuardOverflowCount_Type=Counter32
_BsIpv6FHSSourceGuardOverflowCount_Object=MibTableColumn
bsIpv6FHSSourceGuardOverflowCount=_BsIpv6FHSSourceGuardOverflowCount_Object((1,3,6,1,4,1,45,5,45,1,9,1,4),_BsIpv6FHSSourceGuardOverflowCount_Type())
bsIpv6FHSSourceGuardOverflowCount.setMaxAccess(_E)
if mibBuilder.loadTexts:bsIpv6FHSSourceGuardOverflowCount.setStatus(_A)
_BsIpv6FHSSourceGuardClearOverflowCount_Type=TruthValue
_BsIpv6FHSSourceGuardClearOverflowCount_Object=MibTableColumn
bsIpv6FHSSourceGuardClearOverflowCount=_BsIpv6FHSSourceGuardClearOverflowCount_Object((1,3,6,1,4,1,45,5,45,1,9,1,5),_BsIpv6FHSSourceGuardClearOverflowCount_Type())
bsIpv6FHSSourceGuardClearOverflowCount.setMaxAccess(_C)
if mibBuilder.loadTexts:bsIpv6FHSSourceGuardClearOverflowCount.setStatus(_A)
_BsIpv6FHSSourceGuardDropCount_Type=Counter32
_BsIpv6FHSSourceGuardDropCount_Object=MibTableColumn
bsIpv6FHSSourceGuardDropCount=_BsIpv6FHSSourceGuardDropCount_Object((1,3,6,1,4,1,45,5,45,1,9,1,6),_BsIpv6FHSSourceGuardDropCount_Type())
bsIpv6FHSSourceGuardDropCount.setMaxAccess(_E)
if mibBuilder.loadTexts:bsIpv6FHSSourceGuardDropCount.setStatus(_A)
_BsIpv6FHSSourceGuardClearDropCount_Type=TruthValue
_BsIpv6FHSSourceGuardClearDropCount_Object=MibTableColumn
bsIpv6FHSSourceGuardClearDropCount=_BsIpv6FHSSourceGuardClearDropCount_Object((1,3,6,1,4,1,45,5,45,1,9,1,7),_BsIpv6FHSSourceGuardClearDropCount_Type())
bsIpv6FHSSourceGuardClearDropCount.setMaxAccess(_C)
if mibBuilder.loadTexts:bsIpv6FHSSourceGuardClearDropCount.setStatus(_A)
_BsIpv6FHSSourceGuardBindingTable_Object=MibTable
bsIpv6FHSSourceGuardBindingTable=_BsIpv6FHSSourceGuardBindingTable_Object((1,3,6,1,4,1,45,5,45,1,10))
if mibBuilder.loadTexts:bsIpv6FHSSourceGuardBindingTable.setStatus(_A)
_BsIpv6FHSSourceGuardBindingEntry_Object=MibTableRow
bsIpv6FHSSourceGuardBindingEntry=_BsIpv6FHSSourceGuardBindingEntry_Object((1,3,6,1,4,1,45,5,45,1,10,1))
bsIpv6FHSSourceGuardBindingEntry.setIndexNames((0,_B,_q),(0,_B,_r))
if mibBuilder.loadTexts:bsIpv6FHSSourceGuardBindingEntry.setStatus(_A)
_BsIpv6FHSSourceGuardEntryIfIndex_Type=InterfaceIndex
_BsIpv6FHSSourceGuardEntryIfIndex_Object=MibTableColumn
bsIpv6FHSSourceGuardEntryIfIndex=_BsIpv6FHSSourceGuardEntryIfIndex_Object((1,3,6,1,4,1,45,5,45,1,10,1,1),_BsIpv6FHSSourceGuardEntryIfIndex_Type())
bsIpv6FHSSourceGuardEntryIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:bsIpv6FHSSourceGuardEntryIfIndex.setStatus(_A)
_BsIpv6FHSSourceGuardEntryIpv6Addr_Type=Ipv6Address
_BsIpv6FHSSourceGuardEntryIpv6Addr_Object=MibTableColumn
bsIpv6FHSSourceGuardEntryIpv6Addr=_BsIpv6FHSSourceGuardEntryIpv6Addr_Object((1,3,6,1,4,1,45,5,45,1,10,1,2),_BsIpv6FHSSourceGuardEntryIpv6Addr_Type())
bsIpv6FHSSourceGuardEntryIpv6Addr.setMaxAccess(_E)
if mibBuilder.loadTexts:bsIpv6FHSSourceGuardEntryIpv6Addr.setStatus(_A)
_BsIpv6FHSTrapNotificationObjects_ObjectIdentity=ObjectIdentity
bsIpv6FHSTrapNotificationObjects=_BsIpv6FHSTrapNotificationObjects_ObjectIdentity((1,3,6,1,4,1,45,5,45,1,11))
_BsIpv6FHSTrapClientMACAddr_Type=MacAddress
_BsIpv6FHSTrapClientMACAddr_Object=MibScalar
bsIpv6FHSTrapClientMACAddr=_BsIpv6FHSTrapClientMACAddr_Object((1,3,6,1,4,1,45,5,45,1,11,1),_BsIpv6FHSTrapClientMACAddr_Type())
bsIpv6FHSTrapClientMACAddr.setMaxAccess(_H)
if mibBuilder.loadTexts:bsIpv6FHSTrapClientMACAddr.setStatus(_A)
_BsIpv6FHSTrapInterfaceIndex_Type=InterfaceIndex
_BsIpv6FHSTrapInterfaceIndex_Object=MibScalar
bsIpv6FHSTrapInterfaceIndex=_BsIpv6FHSTrapInterfaceIndex_Object((1,3,6,1,4,1,45,5,45,1,11,2),_BsIpv6FHSTrapInterfaceIndex_Type())
bsIpv6FHSTrapInterfaceIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:bsIpv6FHSTrapInterfaceIndex.setStatus(_A)
_BsIpv6FHSTrapClientIpv6Address_Type=Ipv6Address
_BsIpv6FHSTrapClientIpv6Address_Object=MibScalar
bsIpv6FHSTrapClientIpv6Address=_BsIpv6FHSTrapClientIpv6Address_Object((1,3,6,1,4,1,45,5,45,1,11,3),_BsIpv6FHSTrapClientIpv6Address_Type())
bsIpv6FHSTrapClientIpv6Address.setMaxAccess(_H)
if mibBuilder.loadTexts:bsIpv6FHSTrapClientIpv6Address.setStatus(_A)
class _BsIpv6FHSTrapVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_BsIpv6FHSTrapVlanID_Type.__name__=_D
_BsIpv6FHSTrapVlanID_Object=MibScalar
bsIpv6FHSTrapVlanID=_BsIpv6FHSTrapVlanID_Object((1,3,6,1,4,1,45,5,45,1,11,4),_BsIpv6FHSTrapVlanID_Type())
bsIpv6FHSTrapVlanID.setMaxAccess(_H)
if mibBuilder.loadTexts:bsIpv6FHSTrapVlanID.setStatus(_A)
class _BsIpv6FHSTrapMsgType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_k,1),(_l,2),(_m,3),(_n,4),(_o,5),('ipv6DHCPReq',6),('ipv6DHCPReply',7)))
_BsIpv6FHSTrapMsgType_Type.__name__=_D
_BsIpv6FHSTrapMsgType_Object=MibScalar
bsIpv6FHSTrapMsgType=_BsIpv6FHSTrapMsgType_Object((1,3,6,1,4,1,45,5,45,1,11,5),_BsIpv6FHSTrapMsgType_Type())
bsIpv6FHSTrapMsgType.setMaxAccess(_H)
if mibBuilder.loadTexts:bsIpv6FHSTrapMsgType.setStatus(_A)
class _BsIpv6FhsTrapPktDropReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('ipv6PortRoleMismatch',1),('ipv6MacMismatch',2),('ipv6PrefixMismatch',3),('ipv6IpMismatch',4),('ipv6ManagedFlagMismatch',5),('ipv6RouterPrefMismatch',6),('ipv6HopLimitMismatch',7),('ipv6LenMismatch',8)))
_BsIpv6FhsTrapPktDropReason_Type.__name__=_D
_BsIpv6FhsTrapPktDropReason_Object=MibScalar
bsIpv6FhsTrapPktDropReason=_BsIpv6FhsTrapPktDropReason_Object((1,3,6,1,4,1,45,5,45,1,11,6),_BsIpv6FhsTrapPktDropReason_Type())
bsIpv6FhsTrapPktDropReason.setMaxAccess(_H)
if mibBuilder.loadTexts:bsIpv6FhsTrapPktDropReason.setStatus(_A)
bsIpv6NDSBTTableFull=NotificationType((1,3,6,1,4,1,45,5,45,0,1))
bsIpv6NDSBTTableFull.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:bsIpv6NDSBTTableFull.setStatus(_I)
bsIpv6NDNotificationsUntrustedPort=NotificationType((1,3,6,1,4,1,45,5,45,0,2))
bsIpv6NDNotificationsUntrustedPort.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:bsIpv6NDNotificationsUntrustedPort.setStatus(_I)
bsIpv6NDNotificationSBTTableFull=NotificationType((1,3,6,1,4,1,45,5,45,0,3))
bsIpv6NDNotificationSBTTableFull.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:bsIpv6NDNotificationSBTTableFull.setStatus(_A)
bsIpv6NDNotificationUntrustedPort=NotificationType((1,3,6,1,4,1,45,5,45,0,4))
bsIpv6NDNotificationUntrustedPort.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:bsIpv6NDNotificationUntrustedPort.setStatus(_A)
bsIpv6RAGuardNotification=NotificationType((1,3,6,1,4,1,45,5,45,0,5))
bsIpv6RAGuardNotification.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_W)))
if mibBuilder.loadTexts:bsIpv6RAGuardNotification.setStatus(_A)
bsIpv6DHCPGuardNotification=NotificationType((1,3,6,1,4,1,45,5,45,0,6))
bsIpv6DHCPGuardNotification.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_W)))
if mibBuilder.loadTexts:bsIpv6DHCPGuardNotification.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_Q:FhsRaGuardDeviceRole,'FhsRaManagedConfigFlag':FhsRaManagedConfigFlag,_g:FhsRaRouterPrefMax,_d:FhsDhcpv6GuardDeviceRole,'FhsListName':FhsListName,_P:FhsAccessType,'FhsSbtState':FhsSbtState,'FhsSbtType':FhsSbtType,'bayStackIpv6FirstHopSecMib':bayStackIpv6FirstHopSecMib,'bsIpv6FirstHopSecNotifications':bsIpv6FirstHopSecNotifications,'bsIpv6NDSBTTableFull':bsIpv6NDSBTTableFull,'bsIpv6NDNotificationsUntrustedPort':bsIpv6NDNotificationsUntrustedPort,'bsIpv6NDNotificationSBTTableFull':bsIpv6NDNotificationSBTTableFull,'bsIpv6NDNotificationUntrustedPort':bsIpv6NDNotificationUntrustedPort,'bsIpv6RAGuardNotification':bsIpv6RAGuardNotification,'bsIpv6DHCPGuardNotification':bsIpv6DHCPGuardNotification,'bsIpv6FirstHopSecObjects':bsIpv6FirstHopSecObjects,'bsIpv6FHSScalVar':bsIpv6FHSScalVar,'bsIpv6FHSAdmin':bsIpv6FHSAdmin,'bsIpv6FHSRagAdmin':bsIpv6FHSRagAdmin,'bsIpv6FHSDhcpv6gAdmin':bsIpv6FHSDhcpv6gAdmin,'bsIpv6FHSNdInspectAdmin':bsIpv6FHSNdInspectAdmin,'bsIpv6FHSMaxDynSbtEntries':bsIpv6FHSMaxDynSbtEntries,'bsIpv6FHSSbtReachLifeTime':bsIpv6FHSSbtReachLifeTime,'bsIpv6FHSSbtStaleLifeTime':bsIpv6FHSSbtStaleLifeTime,'bsIpv6FHSSbtDownLifeTime':bsIpv6FHSSbtDownLifeTime,'bsIpv6FHSSbtTblOverFlow':bsIpv6FHSSbtTblOverFlow,'bsIpv6FHSIpv6AccessListTable':bsIpv6FHSIpv6AccessListTable,'bsIpv6FHSIpv6AccessListEntry':bsIpv6FHSIpv6AccessListEntry,_X:bsIpv6FHSIpv6AccessListName,_Y:bsIpv6FHSIpv6AccessListPrefix,_Z:bsIpv6FHSIpv6AccessListPrefixMaskLen,'bsIpv6FHSIpv6AccessListMaskLenFrom':bsIpv6FHSIpv6AccessListMaskLenFrom,'bsIpv6FHSIpv6AccessListMaskLenTo':bsIpv6FHSIpv6AccessListMaskLenTo,'bsIpv6FHSIpv6AccessListAccessType':bsIpv6FHSIpv6AccessListAccessType,'bsIpv6FHSIpv6AccessListRowStatus':bsIpv6FHSIpv6AccessListRowStatus,'bsIpv6FHSMacAccessListTable':bsIpv6FHSMacAccessListTable,'bsIpv6FHSMacAccessListEntry':bsIpv6FHSMacAccessListEntry,_a:bsIpv6FHSMacAccessListName,_b:bsIpv6FHSMacAccessListMac,'bsIpv6FHSMacAccessListAccessType':bsIpv6FHSMacAccessListAccessType,'bsIpv6FHSMacAccessListRowStatus':bsIpv6FHSMacAccessListRowStatus,'bsIpv6FHSPolicyPortMapTable':bsIpv6FHSPolicyPortMapTable,'bsIpv6FHSPolicyPortMapEntry':bsIpv6FHSPolicyPortMapEntry,_c:bsIpv6FHSPolicyPortMapIfIndex,'bsIpv6FHSPolicyPortMapDhcpv6gPolicyName':bsIpv6FHSPolicyPortMapDhcpv6gPolicyName,'bsIpv6FHSPolicyPortMapRagPolicyName':bsIpv6FHSPolicyPortMapRagPolicyName,'bsIpv6FHSPolicyPortMapNDAdmin':bsIpv6FHSPolicyPortMapNDAdmin,'bsIpv6FHSPolicyPortMapSbtDynLearnAdmin':bsIpv6FHSPolicyPortMapSbtDynLearnAdmin,'bsIpv6FHSPolicyPortMapTotDhcpv6PktRcv':bsIpv6FHSPolicyPortMapTotDhcpv6PktRcv,'bsIpv6FHSPolicyPortMapTotDhcpv6PktDropped':bsIpv6FHSPolicyPortMapTotDhcpv6PktDropped,'bsIpv6FHSPolicyPortMapTotRaPktRcv':bsIpv6FHSPolicyPortMapTotRaPktRcv,'bsIpv6FHSPolicyPortMapTotRaPktDropped':bsIpv6FHSPolicyPortMapTotRaPktDropped,'bsIpv6FHSPolicyPortMapTotNdPktRcv':bsIpv6FHSPolicyPortMapTotNdPktRcv,'bsIpv6FHSPolicyPortMapTotNdPktDropped':bsIpv6FHSPolicyPortMapTotNdPktDropped,'bsIpv6FHSPolicyPortMapClearDhcpGuardStats':bsIpv6FHSPolicyPortMapClearDhcpGuardStats,'bsIpv6FHSPolicyPortMapClearRaGuardStats':bsIpv6FHSPolicyPortMapClearRaGuardStats,'bsIpv6FHSPolicyPortMapClearNDInspectStats':bsIpv6FHSPolicyPortMapClearNDInspectStats,'bsIpv6FHSPolicyPortMapRowStatus':bsIpv6FHSPolicyPortMapRowStatus,'bsIpv6FHSPolicyPortMapDhcpv6gDeviceRole':bsIpv6FHSPolicyPortMapDhcpv6gDeviceRole,'bsIpv6FHSPolicyPortMapRagDeviceRole':bsIpv6FHSPolicyPortMapRagDeviceRole,'bsIpv6FHSDhcpv6gPolicyListTable':bsIpv6FHSDhcpv6gPolicyListTable,'bsIpv6FHSDhcpv6gPolicyListEntry':bsIpv6FHSDhcpv6gPolicyListEntry,_e:bsIpv6FHSDhcpv6gPolicyName,'bsIpv6FHSDhcpv6gDeviceRole':bsIpv6FHSDhcpv6gDeviceRole,'bsIpv6FHSDhcpv6gServerAccessListName':bsIpv6FHSDhcpv6gServerAccessListName,'bsIpv6FHSDhcpv6gReplyPrefixListName':bsIpv6FHSDhcpv6gReplyPrefixListName,'bsIpv6FHSDhcpv6gPrefLimitMin':bsIpv6FHSDhcpv6gPrefLimitMin,'bsIpv6FHSDhcpv6gPrefLimitMax':bsIpv6FHSDhcpv6gPrefLimitMax,'bsIpv6FHSDhcpv6gPolicyListRowStatus':bsIpv6FHSDhcpv6gPolicyListRowStatus,'bsIpv6FHSRagPolicyListTable':bsIpv6FHSRagPolicyListTable,'bsIpv6FHSRagPolicyListEntry':bsIpv6FHSRagPolicyListEntry,_f:bsIpv6FHSRagPolicyName,'bsIpv6FHSRagDeviceRole':bsIpv6FHSRagDeviceRole,'bsIpv6FHSRagIpv6AccessListName':bsIpv6FHSRagIpv6AccessListName,'bsIpv6FHSRagIpv6PrefixListName':bsIpv6FHSRagIpv6PrefixListName,'bsIpv6FHSRagMacListName':bsIpv6FHSRagMacListName,'bsIpv6FHSRagManagedConfigFlag':bsIpv6FHSRagManagedConfigFlag,'bsIpv6FHSRagRouterPrefMax':bsIpv6FHSRagRouterPrefMax,'bsIpv6FHSRagHopLimitMin':bsIpv6FHSRagHopLimitMin,'bsIpv6FHSRagHopLimitMax':bsIpv6FHSRagHopLimitMax,'bsIpv6FHSRagPolicyListRowStatus':bsIpv6FHSRagPolicyListRowStatus,'bsIpv6FHSSbtTable':bsIpv6FHSSbtTable,'bsIpv6FHSSbtListEntry':bsIpv6FHSSbtListEntry,_h:bsIpv6FHSSbtInterfaceIndex,_i:bsIpv6FHSSbtVlan,_j:bsIpv6FHSSbtSrcIp,'bsIpv6FHSSbtLinkLayerAddress':bsIpv6FHSSbtLinkLayerAddress,'bsIpv6FHSSbtLearnType':bsIpv6FHSSbtLearnType,'bsIpv6FHSSbtLearnPriority':bsIpv6FHSSbtLearnPriority,'bsIpv6FHSSbtLearnState':bsIpv6FHSSbtLearnState,'bsIpv6FHSSbtLearnAge':bsIpv6FHSSbtLearnAge,'bsIpv6FHSSbtRowStatus':bsIpv6FHSSbtRowStatus,'bsIpv6NDTrapNotificationObjects':bsIpv6NDTrapNotificationObjects,_R:bsIpv6NDInspectionNotificationClientMACAddr,_S:bsIpv6NDInspectionNotificationMsgType,_T:bsIpv6FHSNDInterfaceIndex,_U:bsIpv6FHSNDIpv6Address,_V:bsIpv6FHSNDVlanID,'bsIpv6FHSSourceGuardInterfaceConfigTable':bsIpv6FHSSourceGuardInterfaceConfigTable,'bsIpv6FHSSourceGuardInterfaceConfigEntry':bsIpv6FHSSourceGuardInterfaceConfigEntry,_p:bsIpv6FHSSourceGuardIfIndex,'bsIpv6FHSSourceGuardInterfaceState':bsIpv6FHSSourceGuardInterfaceState,'bsIpv6FHSSourceGuardMaxAddr':bsIpv6FHSSourceGuardMaxAddr,'bsIpv6FHSSourceGuardOverflowCount':bsIpv6FHSSourceGuardOverflowCount,'bsIpv6FHSSourceGuardClearOverflowCount':bsIpv6FHSSourceGuardClearOverflowCount,'bsIpv6FHSSourceGuardDropCount':bsIpv6FHSSourceGuardDropCount,'bsIpv6FHSSourceGuardClearDropCount':bsIpv6FHSSourceGuardClearDropCount,'bsIpv6FHSSourceGuardBindingTable':bsIpv6FHSSourceGuardBindingTable,'bsIpv6FHSSourceGuardBindingEntry':bsIpv6FHSSourceGuardBindingEntry,_q:bsIpv6FHSSourceGuardEntryIfIndex,_r:bsIpv6FHSSourceGuardEntryIpv6Addr,'bsIpv6FHSTrapNotificationObjects':bsIpv6FHSTrapNotificationObjects,_J:bsIpv6FHSTrapClientMACAddr,_M:bsIpv6FHSTrapInterfaceIndex,_K:bsIpv6FHSTrapClientIpv6Address,_N:bsIpv6FHSTrapVlanID,_L:bsIpv6FHSTrapMsgType,_W:bsIpv6FhsTrapPktDropReason})