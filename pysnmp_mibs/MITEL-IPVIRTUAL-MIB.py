_H='mitelIpVGrpTableRipIpAddr'
_G='read-write'
_F='mitelIpVGrpPortTableIfIndex'
_E='mitelIpVGrpPortTableNetAddr'
_D='Integer32'
_C='MITEL-IPVIRTUAL-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
mitelIpGrpIpVirtualGroup=ModuleIdentity((1,3,6,1,4,1,1027,4,8,1,1,4))
if mibBuilder.loadTexts:mitelIpGrpIpVirtualGroup.setRevisions(('2003-03-24 09:31','1999-03-01 00:00'))
_Mitel_ObjectIdentity=ObjectIdentity
mitel=_Mitel_ObjectIdentity((1,3,6,1,4,1,1027))
_MitelProprietary_ObjectIdentity=ObjectIdentity
mitelProprietary=_MitelProprietary_ObjectIdentity((1,3,6,1,4,1,1027,4))
_MitelPropIpNetworking_ObjectIdentity=ObjectIdentity
mitelPropIpNetworking=_MitelPropIpNetworking_ObjectIdentity((1,3,6,1,4,1,1027,4,8))
_MitelIpNetRouter_ObjectIdentity=ObjectIdentity
mitelIpNetRouter=_MitelIpNetRouter_ObjectIdentity((1,3,6,1,4,1,1027,4,8,1))
_MitelRouterIpGroup_ObjectIdentity=ObjectIdentity
mitelRouterIpGroup=_MitelRouterIpGroup_ObjectIdentity((1,3,6,1,4,1,1027,4,8,1,1))
_MitelIpVGrpPortTable_Object=MibTable
mitelIpVGrpPortTable=_MitelIpVGrpPortTable_Object((1,3,6,1,4,1,1027,4,8,1,1,4,1))
if mibBuilder.loadTexts:mitelIpVGrpPortTable.setStatus(_A)
_MitelIpVGrpPortEntry_Object=MibTableRow
mitelIpVGrpPortEntry=_MitelIpVGrpPortEntry_Object((1,3,6,1,4,1,1027,4,8,1,1,4,1,1))
mitelIpVGrpPortEntry.setIndexNames((0,_C,_E),(0,_C,_F))
if mibBuilder.loadTexts:mitelIpVGrpPortEntry.setStatus(_A)
_MitelIpVGrpPortTableNetAddr_Type=IpAddress
_MitelIpVGrpPortTableNetAddr_Object=MibTableColumn
mitelIpVGrpPortTableNetAddr=_MitelIpVGrpPortTableNetAddr_Object((1,3,6,1,4,1,1027,4,8,1,1,4,1,1,1),_MitelIpVGrpPortTableNetAddr_Type())
mitelIpVGrpPortTableNetAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelIpVGrpPortTableNetAddr.setStatus(_A)
_MitelIpVGrpPortTableNetMask_Type=IpAddress
_MitelIpVGrpPortTableNetMask_Object=MibTableColumn
mitelIpVGrpPortTableNetMask=_MitelIpVGrpPortTableNetMask_Object((1,3,6,1,4,1,1027,4,8,1,1,4,1,1,2),_MitelIpVGrpPortTableNetMask_Type())
mitelIpVGrpPortTableNetMask.setMaxAccess(_G)
if mibBuilder.loadTexts:mitelIpVGrpPortTableNetMask.setStatus(_A)
_MitelIpVGrpPortTableIfIndex_Type=Integer32
_MitelIpVGrpPortTableIfIndex_Object=MibTableColumn
mitelIpVGrpPortTableIfIndex=_MitelIpVGrpPortTableIfIndex_Object((1,3,6,1,4,1,1027,4,8,1,1,4,1,1,11),_MitelIpVGrpPortTableIfIndex_Type())
mitelIpVGrpPortTableIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelIpVGrpPortTableIfIndex.setStatus(_A)
_MitelIpVGrpPortTableStatus_Type=RowStatus
_MitelIpVGrpPortTableStatus_Object=MibTableColumn
mitelIpVGrpPortTableStatus=_MitelIpVGrpPortTableStatus_Object((1,3,6,1,4,1,1027,4,8,1,1,4,1,1,12),_MitelIpVGrpPortTableStatus_Type())
mitelIpVGrpPortTableStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:mitelIpVGrpPortTableStatus.setStatus(_A)
class _MitelIpVGrpPortTableCfgMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('static',1),('addressless',2),('dhcp',3),('ipcp',4)))
_MitelIpVGrpPortTableCfgMethod_Type.__name__=_D
_MitelIpVGrpPortTableCfgMethod_Object=MibTableColumn
mitelIpVGrpPortTableCfgMethod=_MitelIpVGrpPortTableCfgMethod_Object((1,3,6,1,4,1,1027,4,8,1,1,4,1,1,15),_MitelIpVGrpPortTableCfgMethod_Type())
mitelIpVGrpPortTableCfgMethod.setMaxAccess(_G)
if mibBuilder.loadTexts:mitelIpVGrpPortTableCfgMethod.setStatus(_A)
_MitelIpVGrpRipTable_Object=MibTable
mitelIpVGrpRipTable=_MitelIpVGrpRipTable_Object((1,3,6,1,4,1,1027,4,8,1,1,4,2))
if mibBuilder.loadTexts:mitelIpVGrpRipTable.setStatus(_A)
_MitelIpVGrpRipEntry_Object=MibTableRow
mitelIpVGrpRipEntry=_MitelIpVGrpRipEntry_Object((1,3,6,1,4,1,1027,4,8,1,1,4,2,1))
mitelIpVGrpRipEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:mitelIpVGrpRipEntry.setStatus(_A)
_MitelIpVGrpTableRipIpAddr_Type=IpAddress
_MitelIpVGrpTableRipIpAddr_Object=MibTableColumn
mitelIpVGrpTableRipIpAddr=_MitelIpVGrpTableRipIpAddr_Object((1,3,6,1,4,1,1027,4,8,1,1,4,2,1,1),_MitelIpVGrpTableRipIpAddr_Type())
mitelIpVGrpTableRipIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelIpVGrpTableRipIpAddr.setStatus(_A)
_MitelIpVGrpTableRipRxPkts_Type=Counter32
_MitelIpVGrpTableRipRxPkts_Object=MibTableColumn
mitelIpVGrpTableRipRxPkts=_MitelIpVGrpTableRipRxPkts_Object((1,3,6,1,4,1,1027,4,8,1,1,4,2,1,2),_MitelIpVGrpTableRipRxPkts_Type())
mitelIpVGrpTableRipRxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelIpVGrpTableRipRxPkts.setStatus(_A)
_MitelIpVGrpTableRipRxBadPkts_Type=Counter32
_MitelIpVGrpTableRipRxBadPkts_Object=MibTableColumn
mitelIpVGrpTableRipRxBadPkts=_MitelIpVGrpTableRipRxBadPkts_Object((1,3,6,1,4,1,1027,4,8,1,1,4,2,1,3),_MitelIpVGrpTableRipRxBadPkts_Type())
mitelIpVGrpTableRipRxBadPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelIpVGrpTableRipRxBadPkts.setStatus(_A)
_MitelIpVGrpTableRipRxBadRtes_Type=Counter32
_MitelIpVGrpTableRipRxBadRtes_Object=MibTableColumn
mitelIpVGrpTableRipRxBadRtes=_MitelIpVGrpTableRipRxBadRtes_Object((1,3,6,1,4,1,1027,4,8,1,1,4,2,1,4),_MitelIpVGrpTableRipRxBadRtes_Type())
mitelIpVGrpTableRipRxBadRtes.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelIpVGrpTableRipRxBadRtes.setStatus(_A)
_MitelIpVGrpTableRipTxUpdates_Type=Counter32
_MitelIpVGrpTableRipTxUpdates_Object=MibTableColumn
mitelIpVGrpTableRipTxUpdates=_MitelIpVGrpTableRipTxUpdates_Object((1,3,6,1,4,1,1027,4,8,1,1,4,2,1,5),_MitelIpVGrpTableRipTxUpdates_Type())
mitelIpVGrpTableRipTxUpdates.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelIpVGrpTableRipTxUpdates.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'mitel':mitel,'mitelProprietary':mitelProprietary,'mitelPropIpNetworking':mitelPropIpNetworking,'mitelIpNetRouter':mitelIpNetRouter,'mitelRouterIpGroup':mitelRouterIpGroup,'mitelIpGrpIpVirtualGroup':mitelIpGrpIpVirtualGroup,'mitelIpVGrpPortTable':mitelIpVGrpPortTable,'mitelIpVGrpPortEntry':mitelIpVGrpPortEntry,_E:mitelIpVGrpPortTableNetAddr,'mitelIpVGrpPortTableNetMask':mitelIpVGrpPortTableNetMask,_F:mitelIpVGrpPortTableIfIndex,'mitelIpVGrpPortTableStatus':mitelIpVGrpPortTableStatus,'mitelIpVGrpPortTableCfgMethod':mitelIpVGrpPortTableCfgMethod,'mitelIpVGrpRipTable':mitelIpVGrpRipTable,'mitelIpVGrpRipEntry':mitelIpVGrpRipEntry,_H:mitelIpVGrpTableRipIpAddr,'mitelIpVGrpTableRipRxPkts':mitelIpVGrpTableRipRxPkts,'mitelIpVGrpTableRipRxBadPkts':mitelIpVGrpTableRipRxBadPkts,'mitelIpVGrpTableRipRxBadRtes':mitelIpVGrpTableRipRxBadRtes,'mitelIpVGrpTableRipTxUpdates':mitelIpVGrpTableRipTxUpdates})