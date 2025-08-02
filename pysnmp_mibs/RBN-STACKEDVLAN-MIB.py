_M='rbnStackedVlanMIBGroup'
_L='rbnStackedVlanHCOutBroadcastPkts'
_K='rbnStackedVlanHCOutMulticastPkts'
_J='rbnStackedVlanHCOutUcastPkts'
_I='rbnStackedVlanHCOutOctets'
_H='rbnStackedVlanHCInBroadcastPkts'
_G='rbnStackedVlanHCInMulticastPkts'
_F='rbnStackedVlanHCInUcastPkts'
_E='rbnStackedVlanHCInOctets'
_D='rbnStackedVlanIndex'
_C='read-only'
_B='RBN-STACKEDVLAN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
rbnMgmt,=mibBuilder.importSymbols('RBN-SMI','rbnMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
rbnStackedVlanMIB=ModuleIdentity((1,3,6,1,4,1,2352,2,40))
if mibBuilder.loadTexts:rbnStackedVlanMIB.setRevisions(('2007-02-27 00:00',))
_RbnStackedVlanMIBObjects_ObjectIdentity=ObjectIdentity
rbnStackedVlanMIBObjects=_RbnStackedVlanMIBObjects_ObjectIdentity((1,3,6,1,4,1,2352,2,40,1))
_RbnStackedVlanAggrStatsTable_Object=MibTable
rbnStackedVlanAggrStatsTable=_RbnStackedVlanAggrStatsTable_Object((1,3,6,1,4,1,2352,2,40,1,1))
if mibBuilder.loadTexts:rbnStackedVlanAggrStatsTable.setStatus(_A)
_RbnStackedVlanAggrStatsEntry_Object=MibTableRow
rbnStackedVlanAggrStatsEntry=_RbnStackedVlanAggrStatsEntry_Object((1,3,6,1,4,1,2352,2,40,1,1,1))
rbnStackedVlanAggrStatsEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:rbnStackedVlanAggrStatsEntry.setStatus(_A)
_RbnStackedVlanIndex_Type=InterfaceIndex
_RbnStackedVlanIndex_Object=MibTableColumn
rbnStackedVlanIndex=_RbnStackedVlanIndex_Object((1,3,6,1,4,1,2352,2,40,1,1,1,1),_RbnStackedVlanIndex_Type())
rbnStackedVlanIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:rbnStackedVlanIndex.setStatus(_A)
_RbnStackedVlanHCInOctets_Type=Counter64
_RbnStackedVlanHCInOctets_Object=MibTableColumn
rbnStackedVlanHCInOctets=_RbnStackedVlanHCInOctets_Object((1,3,6,1,4,1,2352,2,40,1,1,1,2),_RbnStackedVlanHCInOctets_Type())
rbnStackedVlanHCInOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnStackedVlanHCInOctets.setStatus(_A)
_RbnStackedVlanHCInUcastPkts_Type=Counter64
_RbnStackedVlanHCInUcastPkts_Object=MibTableColumn
rbnStackedVlanHCInUcastPkts=_RbnStackedVlanHCInUcastPkts_Object((1,3,6,1,4,1,2352,2,40,1,1,1,3),_RbnStackedVlanHCInUcastPkts_Type())
rbnStackedVlanHCInUcastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnStackedVlanHCInUcastPkts.setStatus(_A)
_RbnStackedVlanHCInMulticastPkts_Type=Counter64
_RbnStackedVlanHCInMulticastPkts_Object=MibTableColumn
rbnStackedVlanHCInMulticastPkts=_RbnStackedVlanHCInMulticastPkts_Object((1,3,6,1,4,1,2352,2,40,1,1,1,4),_RbnStackedVlanHCInMulticastPkts_Type())
rbnStackedVlanHCInMulticastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnStackedVlanHCInMulticastPkts.setStatus(_A)
_RbnStackedVlanHCInBroadcastPkts_Type=Counter64
_RbnStackedVlanHCInBroadcastPkts_Object=MibTableColumn
rbnStackedVlanHCInBroadcastPkts=_RbnStackedVlanHCInBroadcastPkts_Object((1,3,6,1,4,1,2352,2,40,1,1,1,5),_RbnStackedVlanHCInBroadcastPkts_Type())
rbnStackedVlanHCInBroadcastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnStackedVlanHCInBroadcastPkts.setStatus(_A)
_RbnStackedVlanHCOutOctets_Type=Counter64
_RbnStackedVlanHCOutOctets_Object=MibTableColumn
rbnStackedVlanHCOutOctets=_RbnStackedVlanHCOutOctets_Object((1,3,6,1,4,1,2352,2,40,1,1,1,6),_RbnStackedVlanHCOutOctets_Type())
rbnStackedVlanHCOutOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnStackedVlanHCOutOctets.setStatus(_A)
_RbnStackedVlanHCOutUcastPkts_Type=Counter64
_RbnStackedVlanHCOutUcastPkts_Object=MibTableColumn
rbnStackedVlanHCOutUcastPkts=_RbnStackedVlanHCOutUcastPkts_Object((1,3,6,1,4,1,2352,2,40,1,1,1,7),_RbnStackedVlanHCOutUcastPkts_Type())
rbnStackedVlanHCOutUcastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnStackedVlanHCOutUcastPkts.setStatus(_A)
_RbnStackedVlanHCOutMulticastPkts_Type=Counter64
_RbnStackedVlanHCOutMulticastPkts_Object=MibTableColumn
rbnStackedVlanHCOutMulticastPkts=_RbnStackedVlanHCOutMulticastPkts_Object((1,3,6,1,4,1,2352,2,40,1,1,1,8),_RbnStackedVlanHCOutMulticastPkts_Type())
rbnStackedVlanHCOutMulticastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnStackedVlanHCOutMulticastPkts.setStatus(_A)
_RbnStackedVlanHCOutBroadcastPkts_Type=Counter64
_RbnStackedVlanHCOutBroadcastPkts_Object=MibTableColumn
rbnStackedVlanHCOutBroadcastPkts=_RbnStackedVlanHCOutBroadcastPkts_Object((1,3,6,1,4,1,2352,2,40,1,1,1,9),_RbnStackedVlanHCOutBroadcastPkts_Type())
rbnStackedVlanHCOutBroadcastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnStackedVlanHCOutBroadcastPkts.setStatus(_A)
_RbnStackedVlanMIBConformance_ObjectIdentity=ObjectIdentity
rbnStackedVlanMIBConformance=_RbnStackedVlanMIBConformance_ObjectIdentity((1,3,6,1,4,1,2352,2,40,2))
_RbnStackedVlanMIBGroups_ObjectIdentity=ObjectIdentity
rbnStackedVlanMIBGroups=_RbnStackedVlanMIBGroups_ObjectIdentity((1,3,6,1,4,1,2352,2,40,2,1))
_RbnStackedVlanMIBCompliances_ObjectIdentity=ObjectIdentity
rbnStackedVlanMIBCompliances=_RbnStackedVlanMIBCompliances_ObjectIdentity((1,3,6,1,4,1,2352,2,40,2,2))
rbnStackedVlanMIBGroup=ObjectGroup((1,3,6,1,4,1,2352,2,40,2,1,1))
rbnStackedVlanMIBGroup.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:rbnStackedVlanMIBGroup.setStatus(_A)
rbnStackedVlanMIBCompliance=ModuleCompliance((1,3,6,1,4,1,2352,2,40,2,2,1))
rbnStackedVlanMIBCompliance.setObjects((_B,_M))
if mibBuilder.loadTexts:rbnStackedVlanMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'rbnStackedVlanMIB':rbnStackedVlanMIB,'rbnStackedVlanMIBObjects':rbnStackedVlanMIBObjects,'rbnStackedVlanAggrStatsTable':rbnStackedVlanAggrStatsTable,'rbnStackedVlanAggrStatsEntry':rbnStackedVlanAggrStatsEntry,_D:rbnStackedVlanIndex,_E:rbnStackedVlanHCInOctets,_F:rbnStackedVlanHCInUcastPkts,_G:rbnStackedVlanHCInMulticastPkts,_H:rbnStackedVlanHCInBroadcastPkts,_I:rbnStackedVlanHCOutOctets,_J:rbnStackedVlanHCOutUcastPkts,_K:rbnStackedVlanHCOutMulticastPkts,_L:rbnStackedVlanHCOutBroadcastPkts,'rbnStackedVlanMIBConformance':rbnStackedVlanMIBConformance,'rbnStackedVlanMIBGroups':rbnStackedVlanMIBGroups,_M:rbnStackedVlanMIBGroup,'rbnStackedVlanMIBCompliances':rbnStackedVlanMIBCompliances,'rbnStackedVlanMIBCompliance':rbnStackedVlanMIBCompliance})