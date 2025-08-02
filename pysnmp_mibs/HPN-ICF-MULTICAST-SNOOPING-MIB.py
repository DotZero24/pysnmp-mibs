_i='hpnicfMcsPortConfigVlanID'
_h='hpnicfMcsPortConfigSnoopingType'
_g='hpnicfMcsPortConfigIfIndex'
_f='hpnicfMcsRouterPortConfigVlanID'
_e='hpnicfMcsRouterPortConfigSnoopingType'
_d='hpnicfMcsRouterPortConfigIfIndex'
_c='hpnicfMcsPortStaticGroupSourceAddress'
_b='hpnicfMcsPortStaticGroupGroupAddress'
_a='hpnicfMcsPortStaticGroupVlanID'
_Z='hpnicfMcsPortStaticGroupSnoopingType'
_Y='hpnicfMcsPortStaticGroupIfIndex'
_X='hpnicfMcsPortJoinGroupSourceAddress'
_W='hpnicfMcsPortJoinGroupGroupAddress'
_V='hpnicfMcsPortJoinGroupVlanID'
_U='hpnicfMcsPortJoinGroupSnoopingType'
_T='hpnicfMcsPortJoinGroupIfIndex'
_S='hpnicfMcsStatisticsSnoopingType'
_R='hpnicfMcsL2EntryIfIndex'
_Q='hpnicfMcsL2EntrySourceAddress'
_P='hpnicfMcsL2EntryGroupAddress'
_O='hpnicfMcsL2EntryAddressType'
_N='hpnicfMcsL2EntryVUID'
_M='hpnicfMcsL2EntryVUType'
_L='hpnicfMcsVUSnoopingType'
_K='hpnicfMcsVUID'
_J='hpnicfMcsVUType'
_I='hpnicfMcsGlbSnoopingType'
_H='Integer32'
_G='TruthValue'
_F='read-only'
_E='Unsigned32'
_D='not-accessible'
_C='HPN-ICF-MULTICAST-SNOOPING-MIB'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_G)
hpnicfMulticastSnoop=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,123))
if mibBuilder.loadTexts:hpnicfMulticastSnoop.setRevisions(('2014-05-14 17:00',))
class HpnicfVirtualUnitType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('vlan',1),('vsi',2)))
_HpnicfMulticastSnoopObject_ObjectIdentity=ObjectIdentity
hpnicfMulticastSnoopObject=_HpnicfMulticastSnoopObject_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,123,1))
_HpnicfMcsGlobalConfigTable_Object=MibTable
hpnicfMcsGlobalConfigTable=_HpnicfMcsGlobalConfigTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,1))
if mibBuilder.loadTexts:hpnicfMcsGlobalConfigTable.setStatus(_A)
_HpnicfMcsGlobalConfigEntry_Object=MibTableRow
hpnicfMcsGlobalConfigEntry=_HpnicfMcsGlobalConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,1,1))
hpnicfMcsGlobalConfigEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:hpnicfMcsGlobalConfigEntry.setStatus(_A)
_HpnicfMcsGlbSnoopingType_Type=InetAddressType
_HpnicfMcsGlbSnoopingType_Object=MibTableColumn
hpnicfMcsGlbSnoopingType=_HpnicfMcsGlbSnoopingType_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,1,1,1),_HpnicfMcsGlbSnoopingType_Type())
hpnicfMcsGlbSnoopingType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfMcsGlbSnoopingType.setStatus(_A)
_HpnicfMcsGlbRowStatus_Type=RowStatus
_HpnicfMcsGlbRowStatus_Object=MibTableColumn
hpnicfMcsGlbRowStatus=_HpnicfMcsGlbRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,1,1,2),_HpnicfMcsGlbRowStatus_Type())
hpnicfMcsGlbRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMcsGlbRowStatus.setStatus(_A)
_HpnicfMcsGlbEntryLimit_Type=Unsigned32
_HpnicfMcsGlbEntryLimit_Object=MibTableColumn
hpnicfMcsGlbEntryLimit=_HpnicfMcsGlbEntryLimit_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,1,1,3),_HpnicfMcsGlbEntryLimit_Type())
hpnicfMcsGlbEntryLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMcsGlbEntryLimit.setStatus(_A)
class _HpnicfMcsGlbHostAgingTime_Type(Unsigned32):defaultValue=260;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8097894))
_HpnicfMcsGlbHostAgingTime_Type.__name__=_E
_HpnicfMcsGlbHostAgingTime_Object=MibTableColumn
hpnicfMcsGlbHostAgingTime=_HpnicfMcsGlbHostAgingTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,1,1,4),_HpnicfMcsGlbHostAgingTime_Type())
hpnicfMcsGlbHostAgingTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMcsGlbHostAgingTime.setStatus(_A)
class _HpnicfMcsGlbMaxResponseTime_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3174))
_HpnicfMcsGlbMaxResponseTime_Type.__name__=_E
_HpnicfMcsGlbMaxResponseTime_Object=MibTableColumn
hpnicfMcsGlbMaxResponseTime=_HpnicfMcsGlbMaxResponseTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,1,1,5),_HpnicfMcsGlbMaxResponseTime_Type())
hpnicfMcsGlbMaxResponseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMcsGlbMaxResponseTime.setStatus(_A)
class _HpnicfMcsGlbRouterAgingTime_Type(Unsigned32):defaultValue=260;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8097894))
_HpnicfMcsGlbRouterAgingTime_Type.__name__=_E
_HpnicfMcsGlbRouterAgingTime_Object=MibTableColumn
hpnicfMcsGlbRouterAgingTime=_HpnicfMcsGlbRouterAgingTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,1,1,6),_HpnicfMcsGlbRouterAgingTime_Type())
hpnicfMcsGlbRouterAgingTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMcsGlbRouterAgingTime.setStatus(_A)
class _HpnicfMcsGlbLastMemQryInterval_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,25))
_HpnicfMcsGlbLastMemQryInterval_Type.__name__=_E
_HpnicfMcsGlbLastMemQryInterval_Object=MibTableColumn
hpnicfMcsGlbLastMemQryInterval=_HpnicfMcsGlbLastMemQryInterval_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,1,1,7),_HpnicfMcsGlbLastMemQryInterval_Type())
hpnicfMcsGlbLastMemQryInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMcsGlbLastMemQryInterval.setStatus(_A)
class _HpnicfMcsGlbDropUnknownEnabled_Type(TruthValue):defaultValue=2
_HpnicfMcsGlbDropUnknownEnabled_Type.__name__=_G
_HpnicfMcsGlbDropUnknownEnabled_Object=MibTableColumn
hpnicfMcsGlbDropUnknownEnabled=_HpnicfMcsGlbDropUnknownEnabled_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,1,1,8),_HpnicfMcsGlbDropUnknownEnabled_Type())
hpnicfMcsGlbDropUnknownEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMcsGlbDropUnknownEnabled.setStatus(_A)
_HpnicfMcsVirtualUnitConfigTable_Object=MibTable
hpnicfMcsVirtualUnitConfigTable=_HpnicfMcsVirtualUnitConfigTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,2))
if mibBuilder.loadTexts:hpnicfMcsVirtualUnitConfigTable.setStatus(_A)
_HpnicfMcsVirtualUnitConfigEntry_Object=MibTableRow
hpnicfMcsVirtualUnitConfigEntry=_HpnicfMcsVirtualUnitConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,2,1))
hpnicfMcsVirtualUnitConfigEntry.setIndexNames((0,_C,_J),(0,_C,_K),(0,_C,_L))
if mibBuilder.loadTexts:hpnicfMcsVirtualUnitConfigEntry.setStatus(_A)
_HpnicfMcsVUType_Type=HpnicfVirtualUnitType
_HpnicfMcsVUType_Object=MibTableColumn
hpnicfMcsVUType=_HpnicfMcsVUType_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,2,1,1),_HpnicfMcsVUType_Type())
hpnicfMcsVUType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfMcsVUType.setStatus(_A)
_HpnicfMcsVUID_Type=Unsigned32
_HpnicfMcsVUID_Object=MibTableColumn
hpnicfMcsVUID=_HpnicfMcsVUID_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,2,1,2),_HpnicfMcsVUID_Type())
hpnicfMcsVUID.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfMcsVUID.setStatus(_A)
_HpnicfMcsVUSnoopingType_Type=InetAddressType
_HpnicfMcsVUSnoopingType_Object=MibTableColumn
hpnicfMcsVUSnoopingType=_HpnicfMcsVUSnoopingType_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,2,1,3),_HpnicfMcsVUSnoopingType_Type())
hpnicfMcsVUSnoopingType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfMcsVUSnoopingType.setStatus(_A)
_HpnicfMcsVURowStatus_Type=RowStatus
_HpnicfMcsVURowStatus_Object=MibTableColumn
hpnicfMcsVURowStatus=_HpnicfMcsVURowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,2,1,4),_HpnicfMcsVURowStatus_Type())
hpnicfMcsVURowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMcsVURowStatus.setStatus(_A)
class _HpnicfMcsVUHostAgingTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8097894))
_HpnicfMcsVUHostAgingTime_Type.__name__=_E
_HpnicfMcsVUHostAgingTime_Object=MibTableColumn
hpnicfMcsVUHostAgingTime=_HpnicfMcsVUHostAgingTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,2,1,5),_HpnicfMcsVUHostAgingTime_Type())
hpnicfMcsVUHostAgingTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMcsVUHostAgingTime.setStatus(_A)
class _HpnicfMcsVUMaxResponseTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3174))
_HpnicfMcsVUMaxResponseTime_Type.__name__=_E
_HpnicfMcsVUMaxResponseTime_Object=MibTableColumn
hpnicfMcsVUMaxResponseTime=_HpnicfMcsVUMaxResponseTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,2,1,6),_HpnicfMcsVUMaxResponseTime_Type())
hpnicfMcsVUMaxResponseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMcsVUMaxResponseTime.setStatus(_A)
class _HpnicfMcsVURouterAgingTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8097894))
_HpnicfMcsVURouterAgingTime_Type.__name__=_E
_HpnicfMcsVURouterAgingTime_Object=MibTableColumn
hpnicfMcsVURouterAgingTime=_HpnicfMcsVURouterAgingTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,2,1,7),_HpnicfMcsVURouterAgingTime_Type())
hpnicfMcsVURouterAgingTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMcsVURouterAgingTime.setStatus(_A)
class _HpnicfMcsVULastMemQryInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,25))
_HpnicfMcsVULastMemQryInterval_Type.__name__=_E
_HpnicfMcsVULastMemQryInterval_Object=MibTableColumn
hpnicfMcsVULastMemQryInterval=_HpnicfMcsVULastMemQryInterval_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,2,1,8),_HpnicfMcsVULastMemQryInterval_Type())
hpnicfMcsVULastMemQryInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMcsVULastMemQryInterval.setStatus(_A)
class _HpnicfMcsVUDropUnknownEnabled_Type(TruthValue):defaultValue=2
_HpnicfMcsVUDropUnknownEnabled_Type.__name__=_G
_HpnicfMcsVUDropUnknownEnabled_Object=MibTableColumn
hpnicfMcsVUDropUnknownEnabled=_HpnicfMcsVUDropUnknownEnabled_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,2,1,9),_HpnicfMcsVUDropUnknownEnabled_Type())
hpnicfMcsVUDropUnknownEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMcsVUDropUnknownEnabled.setStatus(_A)
class _HpnicfMcsVUPimSnoopingEnabled_Type(TruthValue):defaultValue=2
_HpnicfMcsVUPimSnoopingEnabled_Type.__name__=_G
_HpnicfMcsVUPimSnoopingEnabled_Object=MibTableColumn
hpnicfMcsVUPimSnoopingEnabled=_HpnicfMcsVUPimSnoopingEnabled_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,2,1,10),_HpnicfMcsVUPimSnoopingEnabled_Type())
hpnicfMcsVUPimSnoopingEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMcsVUPimSnoopingEnabled.setStatus(_A)
class _HpnicfMcsVUVersion_Type(Unsigned32):defaultValue=2;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,2),ValueRangeConstraint(3,3))
_HpnicfMcsVUVersion_Type.__name__=_E
_HpnicfMcsVUVersion_Object=MibTableColumn
hpnicfMcsVUVersion=_HpnicfMcsVUVersion_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,2,1,11),_HpnicfMcsVUVersion_Type())
hpnicfMcsVUVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMcsVUVersion.setStatus(_A)
class _HpnicfMcsVUQuerierEnabled_Type(TruthValue):defaultValue=2
_HpnicfMcsVUQuerierEnabled_Type.__name__=_G
_HpnicfMcsVUQuerierEnabled_Object=MibTableColumn
hpnicfMcsVUQuerierEnabled=_HpnicfMcsVUQuerierEnabled_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,2,1,12),_HpnicfMcsVUQuerierEnabled_Type())
hpnicfMcsVUQuerierEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMcsVUQuerierEnabled.setStatus(_A)
class _HpnicfMcsVUQuerierInterval_Type(Unsigned32):defaultValue=125;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,31744))
_HpnicfMcsVUQuerierInterval_Type.__name__=_E
_HpnicfMcsVUQuerierInterval_Object=MibTableColumn
hpnicfMcsVUQuerierInterval=_HpnicfMcsVUQuerierInterval_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,2,1,13),_HpnicfMcsVUQuerierInterval_Type())
hpnicfMcsVUQuerierInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMcsVUQuerierInterval.setStatus(_A)
_HpnicfMcsVUGeneQuerierSourceAddress_Type=InetAddress
_HpnicfMcsVUGeneQuerierSourceAddress_Object=MibTableColumn
hpnicfMcsVUGeneQuerierSourceAddress=_HpnicfMcsVUGeneQuerierSourceAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,2,1,14),_HpnicfMcsVUGeneQuerierSourceAddress_Type())
hpnicfMcsVUGeneQuerierSourceAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMcsVUGeneQuerierSourceAddress.setStatus(_A)
_HpnicfMcsVUSpecQuerierSourceAddress_Type=InetAddress
_HpnicfMcsVUSpecQuerierSourceAddress_Object=MibTableColumn
hpnicfMcsVUSpecQuerierSourceAddress=_HpnicfMcsVUSpecQuerierSourceAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,2,1,15),_HpnicfMcsVUSpecQuerierSourceAddress_Type())
hpnicfMcsVUSpecQuerierSourceAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMcsVUSpecQuerierSourceAddress.setStatus(_A)
_HpnicfMcsVULeaveSourceAddress_Type=InetAddress
_HpnicfMcsVULeaveSourceAddress_Object=MibTableColumn
hpnicfMcsVULeaveSourceAddress=_HpnicfMcsVULeaveSourceAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,2,1,16),_HpnicfMcsVULeaveSourceAddress_Type())
hpnicfMcsVULeaveSourceAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMcsVULeaveSourceAddress.setStatus(_A)
_HpnicfMcsVUReportSourceAddress_Type=InetAddress
_HpnicfMcsVUReportSourceAddress_Object=MibTableColumn
hpnicfMcsVUReportSourceAddress=_HpnicfMcsVUReportSourceAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,2,1,17),_HpnicfMcsVUReportSourceAddress_Type())
hpnicfMcsVUReportSourceAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMcsVUReportSourceAddress.setStatus(_A)
_HpnicfMcsL2EntryTable_Object=MibTable
hpnicfMcsL2EntryTable=_HpnicfMcsL2EntryTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,3))
if mibBuilder.loadTexts:hpnicfMcsL2EntryTable.setStatus(_A)
_HpnicfMcsL2EntryEntry_Object=MibTableRow
hpnicfMcsL2EntryEntry=_HpnicfMcsL2EntryEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,3,1))
hpnicfMcsL2EntryEntry.setIndexNames((0,_C,_M),(0,_C,_N),(0,_C,_O),(0,_C,_P),(0,_C,_Q),(0,_C,_R))
if mibBuilder.loadTexts:hpnicfMcsL2EntryEntry.setStatus(_A)
_HpnicfMcsL2EntryVUType_Type=HpnicfVirtualUnitType
_HpnicfMcsL2EntryVUType_Object=MibTableColumn
hpnicfMcsL2EntryVUType=_HpnicfMcsL2EntryVUType_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,3,1,1),_HpnicfMcsL2EntryVUType_Type())
hpnicfMcsL2EntryVUType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfMcsL2EntryVUType.setStatus(_A)
_HpnicfMcsL2EntryVUID_Type=Unsigned32
_HpnicfMcsL2EntryVUID_Object=MibTableColumn
hpnicfMcsL2EntryVUID=_HpnicfMcsL2EntryVUID_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,3,1,2),_HpnicfMcsL2EntryVUID_Type())
hpnicfMcsL2EntryVUID.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfMcsL2EntryVUID.setStatus(_A)
_HpnicfMcsL2EntryAddressType_Type=InetAddressType
_HpnicfMcsL2EntryAddressType_Object=MibTableColumn
hpnicfMcsL2EntryAddressType=_HpnicfMcsL2EntryAddressType_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,3,1,3),_HpnicfMcsL2EntryAddressType_Type())
hpnicfMcsL2EntryAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfMcsL2EntryAddressType.setStatus(_A)
_HpnicfMcsL2EntryGroupAddress_Type=InetAddress
_HpnicfMcsL2EntryGroupAddress_Object=MibTableColumn
hpnicfMcsL2EntryGroupAddress=_HpnicfMcsL2EntryGroupAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,3,1,4),_HpnicfMcsL2EntryGroupAddress_Type())
hpnicfMcsL2EntryGroupAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfMcsL2EntryGroupAddress.setStatus(_A)
_HpnicfMcsL2EntrySourceAddress_Type=InetAddress
_HpnicfMcsL2EntrySourceAddress_Object=MibTableColumn
hpnicfMcsL2EntrySourceAddress=_HpnicfMcsL2EntrySourceAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,3,1,5),_HpnicfMcsL2EntrySourceAddress_Type())
hpnicfMcsL2EntrySourceAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfMcsL2EntrySourceAddress.setStatus(_A)
_HpnicfMcsL2EntryIfIndex_Type=InterfaceIndex
_HpnicfMcsL2EntryIfIndex_Object=MibTableColumn
hpnicfMcsL2EntryIfIndex=_HpnicfMcsL2EntryIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,3,1,6),_HpnicfMcsL2EntryIfIndex_Type())
hpnicfMcsL2EntryIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfMcsL2EntryIfIndex.setStatus(_A)
class _HpnicfMcsL2EntryPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('interface',1),('ac',2),('npw',3),('upw',4),('trill',5)))
_HpnicfMcsL2EntryPortType_Type.__name__=_H
_HpnicfMcsL2EntryPortType_Object=MibTableColumn
hpnicfMcsL2EntryPortType=_HpnicfMcsL2EntryPortType_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,3,1,7),_HpnicfMcsL2EntryPortType_Type())
hpnicfMcsL2EntryPortType.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfMcsL2EntryPortType.setStatus(_A)
class _HpnicfMcsL2EntryPortAttribute_Type(Bits):namedValues=NamedValues(*(('d',0),('s',1),('p',2),('k',3),('r',4),('w',5)))
_HpnicfMcsL2EntryPortAttribute_Type.__name__='Bits'
_HpnicfMcsL2EntryPortAttribute_Object=MibTableColumn
hpnicfMcsL2EntryPortAttribute=_HpnicfMcsL2EntryPortAttribute_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,3,1,8),_HpnicfMcsL2EntryPortAttribute_Type())
hpnicfMcsL2EntryPortAttribute.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfMcsL2EntryPortAttribute.setStatus(_A)
_HpnicfMcsPacketStatisticsTable_Object=MibTable
hpnicfMcsPacketStatisticsTable=_HpnicfMcsPacketStatisticsTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,4))
if mibBuilder.loadTexts:hpnicfMcsPacketStatisticsTable.setStatus(_A)
_HpnicfMcsPacketStatisticsEntry_Object=MibTableRow
hpnicfMcsPacketStatisticsEntry=_HpnicfMcsPacketStatisticsEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,4,1))
hpnicfMcsPacketStatisticsEntry.setIndexNames((0,_C,_S))
if mibBuilder.loadTexts:hpnicfMcsPacketStatisticsEntry.setStatus(_A)
_HpnicfMcsStatisticsSnoopingType_Type=InetAddressType
_HpnicfMcsStatisticsSnoopingType_Object=MibTableColumn
hpnicfMcsStatisticsSnoopingType=_HpnicfMcsStatisticsSnoopingType_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,4,1,1),_HpnicfMcsStatisticsSnoopingType_Type())
hpnicfMcsStatisticsSnoopingType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfMcsStatisticsSnoopingType.setStatus(_A)
_HpnicfMcsRxGeneryQueryNum_Type=Counter64
_HpnicfMcsRxGeneryQueryNum_Object=MibTableColumn
hpnicfMcsRxGeneryQueryNum=_HpnicfMcsRxGeneryQueryNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,4,1,2),_HpnicfMcsRxGeneryQueryNum_Type())
hpnicfMcsRxGeneryQueryNum.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfMcsRxGeneryQueryNum.setStatus(_A)
_HpnicfMcsRxV2SpecificQueryNum_Type=Counter64
_HpnicfMcsRxV2SpecificQueryNum_Object=MibTableColumn
hpnicfMcsRxV2SpecificQueryNum=_HpnicfMcsRxV2SpecificQueryNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,4,1,3),_HpnicfMcsRxV2SpecificQueryNum_Type())
hpnicfMcsRxV2SpecificQueryNum.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfMcsRxV2SpecificQueryNum.setStatus(_A)
_HpnicfMcsRxV3SpecificQueryNum_Type=Counter64
_HpnicfMcsRxV3SpecificQueryNum_Object=MibTableColumn
hpnicfMcsRxV3SpecificQueryNum=_HpnicfMcsRxV3SpecificQueryNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,4,1,4),_HpnicfMcsRxV3SpecificQueryNum_Type())
hpnicfMcsRxV3SpecificQueryNum.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfMcsRxV3SpecificQueryNum.setStatus(_A)
_HpnicfMcsRxV3SpecificSGQueryNum_Type=Counter64
_HpnicfMcsRxV3SpecificSGQueryNum_Object=MibTableColumn
hpnicfMcsRxV3SpecificSGQueryNum=_HpnicfMcsRxV3SpecificSGQueryNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,4,1,5),_HpnicfMcsRxV3SpecificSGQueryNum_Type())
hpnicfMcsRxV3SpecificSGQueryNum.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfMcsRxV3SpecificSGQueryNum.setStatus(_A)
_HpnicfMcsRxV1ReportNum_Type=Counter64
_HpnicfMcsRxV1ReportNum_Object=MibTableColumn
hpnicfMcsRxV1ReportNum=_HpnicfMcsRxV1ReportNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,4,1,6),_HpnicfMcsRxV1ReportNum_Type())
hpnicfMcsRxV1ReportNum.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfMcsRxV1ReportNum.setStatus(_A)
_HpnicfMcsRxV2ReportNum_Type=Counter64
_HpnicfMcsRxV2ReportNum_Object=MibTableColumn
hpnicfMcsRxV2ReportNum=_HpnicfMcsRxV2ReportNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,4,1,7),_HpnicfMcsRxV2ReportNum_Type())
hpnicfMcsRxV2ReportNum.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfMcsRxV2ReportNum.setStatus(_A)
_HpnicfMcsRxV3ReportNum_Type=Counter64
_HpnicfMcsRxV3ReportNum_Object=MibTableColumn
hpnicfMcsRxV3ReportNum=_HpnicfMcsRxV3ReportNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,4,1,8),_HpnicfMcsRxV3ReportNum_Type())
hpnicfMcsRxV3ReportNum.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfMcsRxV3ReportNum.setStatus(_A)
_HpnicfMcsRxV3ErrCorReportNum_Type=Counter64
_HpnicfMcsRxV3ErrCorReportNum_Object=MibTableColumn
hpnicfMcsRxV3ErrCorReportNum=_HpnicfMcsRxV3ErrCorReportNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,4,1,9),_HpnicfMcsRxV3ErrCorReportNum_Type())
hpnicfMcsRxV3ErrCorReportNum.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfMcsRxV3ErrCorReportNum.setStatus(_A)
_HpnicfMcsRxLeaveNum_Type=Counter64
_HpnicfMcsRxLeaveNum_Object=MibTableColumn
hpnicfMcsRxLeaveNum=_HpnicfMcsRxLeaveNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,4,1,10),_HpnicfMcsRxLeaveNum_Type())
hpnicfMcsRxLeaveNum.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfMcsRxLeaveNum.setStatus(_A)
_HpnicfMcsRxPimHelloNum_Type=Counter64
_HpnicfMcsRxPimHelloNum_Object=MibTableColumn
hpnicfMcsRxPimHelloNum=_HpnicfMcsRxPimHelloNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,4,1,11),_HpnicfMcsRxPimHelloNum_Type())
hpnicfMcsRxPimHelloNum.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfMcsRxPimHelloNum.setStatus(_A)
_HpnicfMcsRxErrorPacketNum_Type=Counter64
_HpnicfMcsRxErrorPacketNum_Object=MibTableColumn
hpnicfMcsRxErrorPacketNum=_HpnicfMcsRxErrorPacketNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,4,1,12),_HpnicfMcsRxErrorPacketNum_Type())
hpnicfMcsRxErrorPacketNum.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfMcsRxErrorPacketNum.setStatus(_A)
_HpnicfMcsTxV2SpecificQueryNum_Type=Counter64
_HpnicfMcsTxV2SpecificQueryNum_Object=MibTableColumn
hpnicfMcsTxV2SpecificQueryNum=_HpnicfMcsTxV2SpecificQueryNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,4,1,13),_HpnicfMcsTxV2SpecificQueryNum_Type())
hpnicfMcsTxV2SpecificQueryNum.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfMcsTxV2SpecificQueryNum.setStatus(_A)
_HpnicfMcsTxV3SpecificQueryNum_Type=Counter64
_HpnicfMcsTxV3SpecificQueryNum_Object=MibTableColumn
hpnicfMcsTxV3SpecificQueryNum=_HpnicfMcsTxV3SpecificQueryNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,4,1,14),_HpnicfMcsTxV3SpecificQueryNum_Type())
hpnicfMcsTxV3SpecificQueryNum.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfMcsTxV3SpecificQueryNum.setStatus(_A)
_HpnicfMcsTxV3SpecificSGQueryNum_Type=Counter64
_HpnicfMcsTxV3SpecificSGQueryNum_Object=MibTableColumn
hpnicfMcsTxV3SpecificSGQueryNum=_HpnicfMcsTxV3SpecificSGQueryNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,4,1,15),_HpnicfMcsTxV3SpecificSGQueryNum_Type())
hpnicfMcsTxV3SpecificSGQueryNum.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfMcsTxV3SpecificSGQueryNum.setStatus(_A)
_HpnicfMcsPortJoinGroupConfigTable_Object=MibTable
hpnicfMcsPortJoinGroupConfigTable=_HpnicfMcsPortJoinGroupConfigTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,5))
if mibBuilder.loadTexts:hpnicfMcsPortJoinGroupConfigTable.setStatus(_A)
_HpnicfMcsPortJoinGroupConfigEntry_Object=MibTableRow
hpnicfMcsPortJoinGroupConfigEntry=_HpnicfMcsPortJoinGroupConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,5,1))
hpnicfMcsPortJoinGroupConfigEntry.setIndexNames((0,_C,_T),(0,_C,_U),(0,_C,_V),(0,_C,_W),(0,_C,_X))
if mibBuilder.loadTexts:hpnicfMcsPortJoinGroupConfigEntry.setStatus(_A)
_HpnicfMcsPortJoinGroupIfIndex_Type=InterfaceIndex
_HpnicfMcsPortJoinGroupIfIndex_Object=MibTableColumn
hpnicfMcsPortJoinGroupIfIndex=_HpnicfMcsPortJoinGroupIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,5,1,1),_HpnicfMcsPortJoinGroupIfIndex_Type())
hpnicfMcsPortJoinGroupIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfMcsPortJoinGroupIfIndex.setStatus(_A)
_HpnicfMcsPortJoinGroupSnoopingType_Type=InetAddressType
_HpnicfMcsPortJoinGroupSnoopingType_Object=MibTableColumn
hpnicfMcsPortJoinGroupSnoopingType=_HpnicfMcsPortJoinGroupSnoopingType_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,5,1,2),_HpnicfMcsPortJoinGroupSnoopingType_Type())
hpnicfMcsPortJoinGroupSnoopingType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfMcsPortJoinGroupSnoopingType.setStatus(_A)
class _HpnicfMcsPortJoinGroupVlanID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_HpnicfMcsPortJoinGroupVlanID_Type.__name__=_E
_HpnicfMcsPortJoinGroupVlanID_Object=MibTableColumn
hpnicfMcsPortJoinGroupVlanID=_HpnicfMcsPortJoinGroupVlanID_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,5,1,3),_HpnicfMcsPortJoinGroupVlanID_Type())
hpnicfMcsPortJoinGroupVlanID.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfMcsPortJoinGroupVlanID.setStatus(_A)
_HpnicfMcsPortJoinGroupGroupAddress_Type=InetAddress
_HpnicfMcsPortJoinGroupGroupAddress_Object=MibTableColumn
hpnicfMcsPortJoinGroupGroupAddress=_HpnicfMcsPortJoinGroupGroupAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,5,1,4),_HpnicfMcsPortJoinGroupGroupAddress_Type())
hpnicfMcsPortJoinGroupGroupAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfMcsPortJoinGroupGroupAddress.setStatus(_A)
_HpnicfMcsPortJoinGroupSourceAddress_Type=InetAddress
_HpnicfMcsPortJoinGroupSourceAddress_Object=MibTableColumn
hpnicfMcsPortJoinGroupSourceAddress=_HpnicfMcsPortJoinGroupSourceAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,5,1,5),_HpnicfMcsPortJoinGroupSourceAddress_Type())
hpnicfMcsPortJoinGroupSourceAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfMcsPortJoinGroupSourceAddress.setStatus(_A)
_HpnicfMcsPortJoinGroupStatus_Type=RowStatus
_HpnicfMcsPortJoinGroupStatus_Object=MibTableColumn
hpnicfMcsPortJoinGroupStatus=_HpnicfMcsPortJoinGroupStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,5,1,6),_HpnicfMcsPortJoinGroupStatus_Type())
hpnicfMcsPortJoinGroupStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMcsPortJoinGroupStatus.setStatus(_A)
_HpnicfMcsPortStaticGroupConfigTable_Object=MibTable
hpnicfMcsPortStaticGroupConfigTable=_HpnicfMcsPortStaticGroupConfigTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,6))
if mibBuilder.loadTexts:hpnicfMcsPortStaticGroupConfigTable.setStatus(_A)
_HpnicfMcsPortStaticGroupConfigEntry_Object=MibTableRow
hpnicfMcsPortStaticGroupConfigEntry=_HpnicfMcsPortStaticGroupConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,6,1))
hpnicfMcsPortStaticGroupConfigEntry.setIndexNames((0,_C,_Y),(0,_C,_Z),(0,_C,_a),(0,_C,_b),(0,_C,_c))
if mibBuilder.loadTexts:hpnicfMcsPortStaticGroupConfigEntry.setStatus(_A)
_HpnicfMcsPortStaticGroupIfIndex_Type=InterfaceIndex
_HpnicfMcsPortStaticGroupIfIndex_Object=MibTableColumn
hpnicfMcsPortStaticGroupIfIndex=_HpnicfMcsPortStaticGroupIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,6,1,1),_HpnicfMcsPortStaticGroupIfIndex_Type())
hpnicfMcsPortStaticGroupIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfMcsPortStaticGroupIfIndex.setStatus(_A)
_HpnicfMcsPortStaticGroupSnoopingType_Type=InetAddressType
_HpnicfMcsPortStaticGroupSnoopingType_Object=MibTableColumn
hpnicfMcsPortStaticGroupSnoopingType=_HpnicfMcsPortStaticGroupSnoopingType_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,6,1,2),_HpnicfMcsPortStaticGroupSnoopingType_Type())
hpnicfMcsPortStaticGroupSnoopingType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfMcsPortStaticGroupSnoopingType.setStatus(_A)
class _HpnicfMcsPortStaticGroupVlanID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_HpnicfMcsPortStaticGroupVlanID_Type.__name__=_E
_HpnicfMcsPortStaticGroupVlanID_Object=MibTableColumn
hpnicfMcsPortStaticGroupVlanID=_HpnicfMcsPortStaticGroupVlanID_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,6,1,3),_HpnicfMcsPortStaticGroupVlanID_Type())
hpnicfMcsPortStaticGroupVlanID.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfMcsPortStaticGroupVlanID.setStatus(_A)
_HpnicfMcsPortStaticGroupGroupAddress_Type=InetAddress
_HpnicfMcsPortStaticGroupGroupAddress_Object=MibTableColumn
hpnicfMcsPortStaticGroupGroupAddress=_HpnicfMcsPortStaticGroupGroupAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,6,1,4),_HpnicfMcsPortStaticGroupGroupAddress_Type())
hpnicfMcsPortStaticGroupGroupAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfMcsPortStaticGroupGroupAddress.setStatus(_A)
_HpnicfMcsPortStaticGroupSourceAddress_Type=InetAddress
_HpnicfMcsPortStaticGroupSourceAddress_Object=MibTableColumn
hpnicfMcsPortStaticGroupSourceAddress=_HpnicfMcsPortStaticGroupSourceAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,6,1,5),_HpnicfMcsPortStaticGroupSourceAddress_Type())
hpnicfMcsPortStaticGroupSourceAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfMcsPortStaticGroupSourceAddress.setStatus(_A)
_HpnicfMcsPortStaticGroupStatus_Type=RowStatus
_HpnicfMcsPortStaticGroupStatus_Object=MibTableColumn
hpnicfMcsPortStaticGroupStatus=_HpnicfMcsPortStaticGroupStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,6,1,6),_HpnicfMcsPortStaticGroupStatus_Type())
hpnicfMcsPortStaticGroupStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMcsPortStaticGroupStatus.setStatus(_A)
_HpnicfMcsRouterPortConfigTable_Object=MibTable
hpnicfMcsRouterPortConfigTable=_HpnicfMcsRouterPortConfigTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,7))
if mibBuilder.loadTexts:hpnicfMcsRouterPortConfigTable.setStatus(_A)
_HpnicfMcsRouterPortConfigEntry_Object=MibTableRow
hpnicfMcsRouterPortConfigEntry=_HpnicfMcsRouterPortConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,7,1))
hpnicfMcsRouterPortConfigEntry.setIndexNames((0,_C,_d),(0,_C,_e),(0,_C,_f))
if mibBuilder.loadTexts:hpnicfMcsRouterPortConfigEntry.setStatus(_A)
_HpnicfMcsRouterPortConfigIfIndex_Type=InterfaceIndex
_HpnicfMcsRouterPortConfigIfIndex_Object=MibTableColumn
hpnicfMcsRouterPortConfigIfIndex=_HpnicfMcsRouterPortConfigIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,7,1,1),_HpnicfMcsRouterPortConfigIfIndex_Type())
hpnicfMcsRouterPortConfigIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfMcsRouterPortConfigIfIndex.setStatus(_A)
_HpnicfMcsRouterPortConfigSnoopingType_Type=InetAddressType
_HpnicfMcsRouterPortConfigSnoopingType_Object=MibTableColumn
hpnicfMcsRouterPortConfigSnoopingType=_HpnicfMcsRouterPortConfigSnoopingType_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,7,1,2),_HpnicfMcsRouterPortConfigSnoopingType_Type())
hpnicfMcsRouterPortConfigSnoopingType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfMcsRouterPortConfigSnoopingType.setStatus(_A)
class _HpnicfMcsRouterPortConfigVlanID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_HpnicfMcsRouterPortConfigVlanID_Type.__name__=_E
_HpnicfMcsRouterPortConfigVlanID_Object=MibTableColumn
hpnicfMcsRouterPortConfigVlanID=_HpnicfMcsRouterPortConfigVlanID_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,7,1,3),_HpnicfMcsRouterPortConfigVlanID_Type())
hpnicfMcsRouterPortConfigVlanID.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfMcsRouterPortConfigVlanID.setStatus(_A)
_HpnicfMcsRouterPortConfigRowStatus_Type=RowStatus
_HpnicfMcsRouterPortConfigRowStatus_Object=MibTableColumn
hpnicfMcsRouterPortConfigRowStatus=_HpnicfMcsRouterPortConfigRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,7,1,4),_HpnicfMcsRouterPortConfigRowStatus_Type())
hpnicfMcsRouterPortConfigRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMcsRouterPortConfigRowStatus.setStatus(_A)
_HpnicfMcsPortConfigTable_Object=MibTable
hpnicfMcsPortConfigTable=_HpnicfMcsPortConfigTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,8))
if mibBuilder.loadTexts:hpnicfMcsPortConfigTable.setStatus(_A)
_HpnicfMcsPortConfigEntry_Object=MibTableRow
hpnicfMcsPortConfigEntry=_HpnicfMcsPortConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,8,1))
hpnicfMcsPortConfigEntry.setIndexNames((0,_C,_g),(0,_C,_h),(0,_C,_i))
if mibBuilder.loadTexts:hpnicfMcsPortConfigEntry.setStatus(_A)
_HpnicfMcsPortConfigIfIndex_Type=InterfaceIndex
_HpnicfMcsPortConfigIfIndex_Object=MibTableColumn
hpnicfMcsPortConfigIfIndex=_HpnicfMcsPortConfigIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,8,1,1),_HpnicfMcsPortConfigIfIndex_Type())
hpnicfMcsPortConfigIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfMcsPortConfigIfIndex.setStatus(_A)
_HpnicfMcsPortConfigSnoopingType_Type=InetAddressType
_HpnicfMcsPortConfigSnoopingType_Object=MibTableColumn
hpnicfMcsPortConfigSnoopingType=_HpnicfMcsPortConfigSnoopingType_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,8,1,2),_HpnicfMcsPortConfigSnoopingType_Type())
hpnicfMcsPortConfigSnoopingType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfMcsPortConfigSnoopingType.setStatus(_A)
class _HpnicfMcsPortConfigVlanID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_HpnicfMcsPortConfigVlanID_Type.__name__=_E
_HpnicfMcsPortConfigVlanID_Object=MibTableColumn
hpnicfMcsPortConfigVlanID=_HpnicfMcsPortConfigVlanID_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,8,1,3),_HpnicfMcsPortConfigVlanID_Type())
hpnicfMcsPortConfigVlanID.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfMcsPortConfigVlanID.setStatus(_A)
_HpnicfMcsPortConfigGroupLimitNumber_Type=Unsigned32
_HpnicfMcsPortConfigGroupLimitNumber_Object=MibTableColumn
hpnicfMcsPortConfigGroupLimitNumber=_HpnicfMcsPortConfigGroupLimitNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,8,1,4),_HpnicfMcsPortConfigGroupLimitNumber_Type())
hpnicfMcsPortConfigGroupLimitNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMcsPortConfigGroupLimitNumber.setStatus(_A)
class _HpnicfMcsPortConfigFastLeaveStatus_Type(TruthValue):defaultValue=2
_HpnicfMcsPortConfigFastLeaveStatus_Type.__name__=_G
_HpnicfMcsPortConfigFastLeaveStatus_Object=MibTableColumn
hpnicfMcsPortConfigFastLeaveStatus=_HpnicfMcsPortConfigFastLeaveStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,8,1,5),_HpnicfMcsPortConfigFastLeaveStatus_Type())
hpnicfMcsPortConfigFastLeaveStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMcsPortConfigFastLeaveStatus.setStatus(_A)
class _HpnicfMcsPortConfigGroupPolicyParameter_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(2000,3999))
_HpnicfMcsPortConfigGroupPolicyParameter_Type.__name__=_E
_HpnicfMcsPortConfigGroupPolicyParameter_Object=MibTableColumn
hpnicfMcsPortConfigGroupPolicyParameter=_HpnicfMcsPortConfigGroupPolicyParameter_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,8,1,6),_HpnicfMcsPortConfigGroupPolicyParameter_Type())
hpnicfMcsPortConfigGroupPolicyParameter.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMcsPortConfigGroupPolicyParameter.setStatus(_A)
class _HpnicfMcsPortConfigOverflowReplace_Type(TruthValue):defaultValue=2
_HpnicfMcsPortConfigOverflowReplace_Type.__name__=_G
_HpnicfMcsPortConfigOverflowReplace_Object=MibTableColumn
hpnicfMcsPortConfigOverflowReplace=_HpnicfMcsPortConfigOverflowReplace_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,8,1,7),_HpnicfMcsPortConfigOverflowReplace_Type())
hpnicfMcsPortConfigOverflowReplace.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMcsPortConfigOverflowReplace.setStatus(_A)
_HpnicfMcsPortConfigRowStatus_Type=RowStatus
_HpnicfMcsPortConfigRowStatus_Object=MibTableColumn
hpnicfMcsPortConfigRowStatus=_HpnicfMcsPortConfigRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,123,1,8,1,8),_HpnicfMcsPortConfigRowStatus_Type())
hpnicfMcsPortConfigRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMcsPortConfigRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'HpnicfVirtualUnitType':HpnicfVirtualUnitType,'hpnicfMulticastSnoop':hpnicfMulticastSnoop,'hpnicfMulticastSnoopObject':hpnicfMulticastSnoopObject,'hpnicfMcsGlobalConfigTable':hpnicfMcsGlobalConfigTable,'hpnicfMcsGlobalConfigEntry':hpnicfMcsGlobalConfigEntry,_I:hpnicfMcsGlbSnoopingType,'hpnicfMcsGlbRowStatus':hpnicfMcsGlbRowStatus,'hpnicfMcsGlbEntryLimit':hpnicfMcsGlbEntryLimit,'hpnicfMcsGlbHostAgingTime':hpnicfMcsGlbHostAgingTime,'hpnicfMcsGlbMaxResponseTime':hpnicfMcsGlbMaxResponseTime,'hpnicfMcsGlbRouterAgingTime':hpnicfMcsGlbRouterAgingTime,'hpnicfMcsGlbLastMemQryInterval':hpnicfMcsGlbLastMemQryInterval,'hpnicfMcsGlbDropUnknownEnabled':hpnicfMcsGlbDropUnknownEnabled,'hpnicfMcsVirtualUnitConfigTable':hpnicfMcsVirtualUnitConfigTable,'hpnicfMcsVirtualUnitConfigEntry':hpnicfMcsVirtualUnitConfigEntry,_J:hpnicfMcsVUType,_K:hpnicfMcsVUID,_L:hpnicfMcsVUSnoopingType,'hpnicfMcsVURowStatus':hpnicfMcsVURowStatus,'hpnicfMcsVUHostAgingTime':hpnicfMcsVUHostAgingTime,'hpnicfMcsVUMaxResponseTime':hpnicfMcsVUMaxResponseTime,'hpnicfMcsVURouterAgingTime':hpnicfMcsVURouterAgingTime,'hpnicfMcsVULastMemQryInterval':hpnicfMcsVULastMemQryInterval,'hpnicfMcsVUDropUnknownEnabled':hpnicfMcsVUDropUnknownEnabled,'hpnicfMcsVUPimSnoopingEnabled':hpnicfMcsVUPimSnoopingEnabled,'hpnicfMcsVUVersion':hpnicfMcsVUVersion,'hpnicfMcsVUQuerierEnabled':hpnicfMcsVUQuerierEnabled,'hpnicfMcsVUQuerierInterval':hpnicfMcsVUQuerierInterval,'hpnicfMcsVUGeneQuerierSourceAddress':hpnicfMcsVUGeneQuerierSourceAddress,'hpnicfMcsVUSpecQuerierSourceAddress':hpnicfMcsVUSpecQuerierSourceAddress,'hpnicfMcsVULeaveSourceAddress':hpnicfMcsVULeaveSourceAddress,'hpnicfMcsVUReportSourceAddress':hpnicfMcsVUReportSourceAddress,'hpnicfMcsL2EntryTable':hpnicfMcsL2EntryTable,'hpnicfMcsL2EntryEntry':hpnicfMcsL2EntryEntry,_M:hpnicfMcsL2EntryVUType,_N:hpnicfMcsL2EntryVUID,_O:hpnicfMcsL2EntryAddressType,_P:hpnicfMcsL2EntryGroupAddress,_Q:hpnicfMcsL2EntrySourceAddress,_R:hpnicfMcsL2EntryIfIndex,'hpnicfMcsL2EntryPortType':hpnicfMcsL2EntryPortType,'hpnicfMcsL2EntryPortAttribute':hpnicfMcsL2EntryPortAttribute,'hpnicfMcsPacketStatisticsTable':hpnicfMcsPacketStatisticsTable,'hpnicfMcsPacketStatisticsEntry':hpnicfMcsPacketStatisticsEntry,_S:hpnicfMcsStatisticsSnoopingType,'hpnicfMcsRxGeneryQueryNum':hpnicfMcsRxGeneryQueryNum,'hpnicfMcsRxV2SpecificQueryNum':hpnicfMcsRxV2SpecificQueryNum,'hpnicfMcsRxV3SpecificQueryNum':hpnicfMcsRxV3SpecificQueryNum,'hpnicfMcsRxV3SpecificSGQueryNum':hpnicfMcsRxV3SpecificSGQueryNum,'hpnicfMcsRxV1ReportNum':hpnicfMcsRxV1ReportNum,'hpnicfMcsRxV2ReportNum':hpnicfMcsRxV2ReportNum,'hpnicfMcsRxV3ReportNum':hpnicfMcsRxV3ReportNum,'hpnicfMcsRxV3ErrCorReportNum':hpnicfMcsRxV3ErrCorReportNum,'hpnicfMcsRxLeaveNum':hpnicfMcsRxLeaveNum,'hpnicfMcsRxPimHelloNum':hpnicfMcsRxPimHelloNum,'hpnicfMcsRxErrorPacketNum':hpnicfMcsRxErrorPacketNum,'hpnicfMcsTxV2SpecificQueryNum':hpnicfMcsTxV2SpecificQueryNum,'hpnicfMcsTxV3SpecificQueryNum':hpnicfMcsTxV3SpecificQueryNum,'hpnicfMcsTxV3SpecificSGQueryNum':hpnicfMcsTxV3SpecificSGQueryNum,'hpnicfMcsPortJoinGroupConfigTable':hpnicfMcsPortJoinGroupConfigTable,'hpnicfMcsPortJoinGroupConfigEntry':hpnicfMcsPortJoinGroupConfigEntry,_T:hpnicfMcsPortJoinGroupIfIndex,_U:hpnicfMcsPortJoinGroupSnoopingType,_V:hpnicfMcsPortJoinGroupVlanID,_W:hpnicfMcsPortJoinGroupGroupAddress,_X:hpnicfMcsPortJoinGroupSourceAddress,'hpnicfMcsPortJoinGroupStatus':hpnicfMcsPortJoinGroupStatus,'hpnicfMcsPortStaticGroupConfigTable':hpnicfMcsPortStaticGroupConfigTable,'hpnicfMcsPortStaticGroupConfigEntry':hpnicfMcsPortStaticGroupConfigEntry,_Y:hpnicfMcsPortStaticGroupIfIndex,_Z:hpnicfMcsPortStaticGroupSnoopingType,_a:hpnicfMcsPortStaticGroupVlanID,_b:hpnicfMcsPortStaticGroupGroupAddress,_c:hpnicfMcsPortStaticGroupSourceAddress,'hpnicfMcsPortStaticGroupStatus':hpnicfMcsPortStaticGroupStatus,'hpnicfMcsRouterPortConfigTable':hpnicfMcsRouterPortConfigTable,'hpnicfMcsRouterPortConfigEntry':hpnicfMcsRouterPortConfigEntry,_d:hpnicfMcsRouterPortConfigIfIndex,_e:hpnicfMcsRouterPortConfigSnoopingType,_f:hpnicfMcsRouterPortConfigVlanID,'hpnicfMcsRouterPortConfigRowStatus':hpnicfMcsRouterPortConfigRowStatus,'hpnicfMcsPortConfigTable':hpnicfMcsPortConfigTable,'hpnicfMcsPortConfigEntry':hpnicfMcsPortConfigEntry,_g:hpnicfMcsPortConfigIfIndex,_h:hpnicfMcsPortConfigSnoopingType,_i:hpnicfMcsPortConfigVlanID,'hpnicfMcsPortConfigGroupLimitNumber':hpnicfMcsPortConfigGroupLimitNumber,'hpnicfMcsPortConfigFastLeaveStatus':hpnicfMcsPortConfigFastLeaveStatus,'hpnicfMcsPortConfigGroupPolicyParameter':hpnicfMcsPortConfigGroupPolicyParameter,'hpnicfMcsPortConfigOverflowReplace':hpnicfMcsPortConfigOverflowReplace,'hpnicfMcsPortConfigRowStatus':hpnicfMcsPortConfigRowStatus})