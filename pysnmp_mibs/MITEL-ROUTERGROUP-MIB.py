_H='mitelIpRouteTblGateAddress'
_G='mitelIpRouteTblDestAddress'
_F='MITEL-ROUTERGROUP-MIB'
_E='disable'
_D='enable'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
mitelRouterIpRouterGroup=ModuleIdentity((1,3,6,1,4,1,1027,4,8,1,5))
if mibBuilder.loadTexts:mitelRouterIpRouterGroup.setRevisions(('2003-03-24 10:45','1999-03-01 00:00'))
_Mitel_ObjectIdentity=ObjectIdentity
mitel=_Mitel_ObjectIdentity((1,3,6,1,4,1,1027))
_MitelProprietary_ObjectIdentity=ObjectIdentity
mitelProprietary=_MitelProprietary_ObjectIdentity((1,3,6,1,4,1,1027,4))
_MitelPropIpNetworking_ObjectIdentity=ObjectIdentity
mitelPropIpNetworking=_MitelPropIpNetworking_ObjectIdentity((1,3,6,1,4,1,1027,4,8))
_MitelIpNetRouter_ObjectIdentity=ObjectIdentity
mitelIpNetRouter=_MitelIpNetRouter_ObjectIdentity((1,3,6,1,4,1,1027,4,8,1))
_MitelIpRouteTable_Object=MibTable
mitelIpRouteTable=_MitelIpRouteTable_Object((1,3,6,1,4,1,1027,4,8,1,5,1))
if mibBuilder.loadTexts:mitelIpRouteTable.setStatus(_A)
_MitelIpRouteEntry_Object=MibTableRow
mitelIpRouteEntry=_MitelIpRouteEntry_Object((1,3,6,1,4,1,1027,4,8,1,5,1,1))
mitelIpRouteEntry.setIndexNames((0,_F,_G),(0,_F,_H))
if mibBuilder.loadTexts:mitelIpRouteEntry.setStatus(_A)
_MitelIpRouteTblDestAddress_Type=IpAddress
_MitelIpRouteTblDestAddress_Object=MibTableColumn
mitelIpRouteTblDestAddress=_MitelIpRouteTblDestAddress_Object((1,3,6,1,4,1,1027,4,8,1,5,1,1,1),_MitelIpRouteTblDestAddress_Type())
mitelIpRouteTblDestAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelIpRouteTblDestAddress.setStatus(_A)
_MitelIpRouteTblGateAddress_Type=IpAddress
_MitelIpRouteTblGateAddress_Object=MibTableColumn
mitelIpRouteTblGateAddress=_MitelIpRouteTblGateAddress_Object((1,3,6,1,4,1,1027,4,8,1,5,1,1,2),_MitelIpRouteTblGateAddress_Type())
mitelIpRouteTblGateAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelIpRouteTblGateAddress.setStatus(_A)
_MitelIpRouteTblNetmaskAddress_Type=IpAddress
_MitelIpRouteTblNetmaskAddress_Object=MibTableColumn
mitelIpRouteTblNetmaskAddress=_MitelIpRouteTblNetmaskAddress_Object((1,3,6,1,4,1,1027,4,8,1,5,1,1,3),_MitelIpRouteTblNetmaskAddress_Type())
mitelIpRouteTblNetmaskAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelIpRouteTblNetmaskAddress.setStatus(_A)
class _MitelIpRouteTblIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,13))
_MitelIpRouteTblIfIndex_Type.__name__=_C
_MitelIpRouteTblIfIndex_Object=MibTableColumn
mitelIpRouteTblIfIndex=_MitelIpRouteTblIfIndex_Object((1,3,6,1,4,1,1027,4,8,1,5,1,1,4),_MitelIpRouteTblIfIndex_Type())
mitelIpRouteTblIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelIpRouteTblIfIndex.setStatus(_A)
_MitelIpRouteTblMetric1_Type=Integer32
_MitelIpRouteTblMetric1_Object=MibTableColumn
mitelIpRouteTblMetric1=_MitelIpRouteTblMetric1_Object((1,3,6,1,4,1,1027,4,8,1,5,1,1,5),_MitelIpRouteTblMetric1_Type())
mitelIpRouteTblMetric1.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelIpRouteTblMetric1.setStatus(_A)
_MitelIpRouteTblMetric2_Type=Integer32
_MitelIpRouteTblMetric2_Object=MibTableColumn
mitelIpRouteTblMetric2=_MitelIpRouteTblMetric2_Object((1,3,6,1,4,1,1027,4,8,1,5,1,1,6),_MitelIpRouteTblMetric2_Type())
mitelIpRouteTblMetric2.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelIpRouteTblMetric2.setStatus(_A)
_MitelIpRouteTblMetric3_Type=Integer32
_MitelIpRouteTblMetric3_Object=MibTableColumn
mitelIpRouteTblMetric3=_MitelIpRouteTblMetric3_Object((1,3,6,1,4,1,1027,4,8,1,5,1,1,7),_MitelIpRouteTblMetric3_Type())
mitelIpRouteTblMetric3.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelIpRouteTblMetric3.setStatus(_A)
_MitelIpRouteTblMetric4_Type=Integer32
_MitelIpRouteTblMetric4_Object=MibTableColumn
mitelIpRouteTblMetric4=_MitelIpRouteTblMetric4_Object((1,3,6,1,4,1,1027,4,8,1,5,1,1,8),_MitelIpRouteTblMetric4_Type())
mitelIpRouteTblMetric4.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelIpRouteTblMetric4.setStatus(_A)
_MitelIpRouteTblMetric5_Type=Integer32
_MitelIpRouteTblMetric5_Object=MibTableColumn
mitelIpRouteTblMetric5=_MitelIpRouteTblMetric5_Object((1,3,6,1,4,1,1027,4,8,1,5,1,1,9),_MitelIpRouteTblMetric5_Type())
mitelIpRouteTblMetric5.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelIpRouteTblMetric5.setStatus(_A)
_MitelIpRouteTblRouteType_Type=Integer32
_MitelIpRouteTblRouteType_Object=MibTableColumn
mitelIpRouteTblRouteType=_MitelIpRouteTblRouteType_Object((1,3,6,1,4,1,1027,4,8,1,5,1,1,10),_MitelIpRouteTblRouteType_Type())
mitelIpRouteTblRouteType.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelIpRouteTblRouteType.setStatus(_A)
_MitelIpRouteTblRouteProto_Type=Integer32
_MitelIpRouteTblRouteProto_Object=MibTableColumn
mitelIpRouteTblRouteProto=_MitelIpRouteTblRouteProto_Object((1,3,6,1,4,1,1027,4,8,1,5,1,1,11),_MitelIpRouteTblRouteProto_Type())
mitelIpRouteTblRouteProto.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelIpRouteTblRouteProto.setStatus(_A)
class _MitelIpRouteTblRouteAge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MitelIpRouteTblRouteAge_Type.__name__=_C
_MitelIpRouteTblRouteAge_Object=MibTableColumn
mitelIpRouteTblRouteAge=_MitelIpRouteTblRouteAge_Object((1,3,6,1,4,1,1027,4,8,1,5,1,1,12),_MitelIpRouteTblRouteAge_Type())
mitelIpRouteTblRouteAge.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelIpRouteTblRouteAge.setStatus(_A)
class _MitelIpRouteTblBlockLearning_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_MitelIpRouteTblBlockLearning_Type.__name__=_C
_MitelIpRouteTblBlockLearning_Object=MibTableColumn
mitelIpRouteTblBlockLearning=_MitelIpRouteTblBlockLearning_Object((1,3,6,1,4,1,1027,4,8,1,5,1,1,13),_MitelIpRouteTblBlockLearning_Type())
mitelIpRouteTblBlockLearning.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelIpRouteTblBlockLearning.setStatus(_A)
class _MitelIpRouteTblInUse_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_MitelIpRouteTblInUse_Type.__name__=_C
_MitelIpRouteTblInUse_Object=MibTableColumn
mitelIpRouteTblInUse=_MitelIpRouteTblInUse_Object((1,3,6,1,4,1,1027,4,8,1,5,1,1,14),_MitelIpRouteTblInUse_Type())
mitelIpRouteTblInUse.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelIpRouteTblInUse.setStatus(_A)
class _MitelIpRouteTblDisableLearned_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_MitelIpRouteTblDisableLearned_Type.__name__=_C
_MitelIpRouteTblDisableLearned_Object=MibTableColumn
mitelIpRouteTblDisableLearned=_MitelIpRouteTblDisableLearned_Object((1,3,6,1,4,1,1027,4,8,1,5,1,1,15),_MitelIpRouteTblDisableLearned_Type())
mitelIpRouteTblDisableLearned.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelIpRouteTblDisableLearned.setStatus(_A)
class _MitelIpRouteTblConvertStatic_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_MitelIpRouteTblConvertStatic_Type.__name__=_C
_MitelIpRouteTblConvertStatic_Object=MibTableColumn
mitelIpRouteTblConvertStatic=_MitelIpRouteTblConvertStatic_Object((1,3,6,1,4,1,1027,4,8,1,5,1,1,16),_MitelIpRouteTblConvertStatic_Type())
mitelIpRouteTblConvertStatic.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelIpRouteTblConvertStatic.setStatus(_A)
_MitelIpRouteTblRowStatus_Type=RowStatus
_MitelIpRouteTblRowStatus_Object=MibTableColumn
mitelIpRouteTblRowStatus=_MitelIpRouteTblRowStatus_Object((1,3,6,1,4,1,1027,4,8,1,5,1,1,17),_MitelIpRouteTblRowStatus_Type())
mitelIpRouteTblRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:mitelIpRouteTblRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'mitel':mitel,'mitelProprietary':mitelProprietary,'mitelPropIpNetworking':mitelPropIpNetworking,'mitelIpNetRouter':mitelIpNetRouter,'mitelRouterIpRouterGroup':mitelRouterIpRouterGroup,'mitelIpRouteTable':mitelIpRouteTable,'mitelIpRouteEntry':mitelIpRouteEntry,_G:mitelIpRouteTblDestAddress,_H:mitelIpRouteTblGateAddress,'mitelIpRouteTblNetmaskAddress':mitelIpRouteTblNetmaskAddress,'mitelIpRouteTblIfIndex':mitelIpRouteTblIfIndex,'mitelIpRouteTblMetric1':mitelIpRouteTblMetric1,'mitelIpRouteTblMetric2':mitelIpRouteTblMetric2,'mitelIpRouteTblMetric3':mitelIpRouteTblMetric3,'mitelIpRouteTblMetric4':mitelIpRouteTblMetric4,'mitelIpRouteTblMetric5':mitelIpRouteTblMetric5,'mitelIpRouteTblRouteType':mitelIpRouteTblRouteType,'mitelIpRouteTblRouteProto':mitelIpRouteTblRouteProto,'mitelIpRouteTblRouteAge':mitelIpRouteTblRouteAge,'mitelIpRouteTblBlockLearning':mitelIpRouteTblBlockLearning,'mitelIpRouteTblInUse':mitelIpRouteTblInUse,'mitelIpRouteTblDisableLearned':mitelIpRouteTblDisableLearned,'mitelIpRouteTblConvertStatic':mitelIpRouteTblConvertStatic,'mitelIpRouteTblRowStatus':mitelIpRouteTblRowStatus})