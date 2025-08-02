_K='pxmTunnelGroup'
_J='pxmTunnelAssociatedLSPList'
_I='pxmTunnelSupportingEqptAid'
_H='pxmTunnelId'
_G='pxmTunnelNum'
_F='pxmTunnelMTUSize'
_E='ifIndex'
_D='IF-MIB'
_C='read-write'
_B='INFINERA-TP-PXMTUNNEL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_D,_E)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
pxmTunnelMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,69))
_PxmTunnelTable_Object=MibTable
pxmTunnelTable=_PxmTunnelTable_Object((1,3,6,1,4,1,21296,2,2,2,2,69,1))
if mibBuilder.loadTexts:pxmTunnelTable.setStatus(_A)
_PxmTunnelEntry_Object=MibTableRow
pxmTunnelEntry=_PxmTunnelEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,69,1,1))
pxmTunnelEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:pxmTunnelEntry.setStatus(_A)
_PxmTunnelMTUSize_Type=Integer32
_PxmTunnelMTUSize_Object=MibTableColumn
pxmTunnelMTUSize=_PxmTunnelMTUSize_Object((1,3,6,1,4,1,21296,2,2,2,2,69,1,1,1),_PxmTunnelMTUSize_Type())
pxmTunnelMTUSize.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmTunnelMTUSize.setStatus(_A)
_PxmTunnelNum_Type=Integer32
_PxmTunnelNum_Object=MibTableColumn
pxmTunnelNum=_PxmTunnelNum_Object((1,3,6,1,4,1,21296,2,2,2,2,69,1,1,2),_PxmTunnelNum_Type())
pxmTunnelNum.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmTunnelNum.setStatus(_A)
_PxmTunnelId_Type=DisplayString
_PxmTunnelId_Object=MibTableColumn
pxmTunnelId=_PxmTunnelId_Object((1,3,6,1,4,1,21296,2,2,2,2,69,1,1,3),_PxmTunnelId_Type())
pxmTunnelId.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmTunnelId.setStatus(_A)
_PxmTunnelSupportingEqptAid_Type=DisplayString
_PxmTunnelSupportingEqptAid_Object=MibTableColumn
pxmTunnelSupportingEqptAid=_PxmTunnelSupportingEqptAid_Object((1,3,6,1,4,1,21296,2,2,2,2,69,1,1,4),_PxmTunnelSupportingEqptAid_Type())
pxmTunnelSupportingEqptAid.setMaxAccess('read-create')
if mibBuilder.loadTexts:pxmTunnelSupportingEqptAid.setStatus(_A)
_PxmTunnelAssociatedLSPList_Type=DisplayString
_PxmTunnelAssociatedLSPList_Object=MibTableColumn
pxmTunnelAssociatedLSPList=_PxmTunnelAssociatedLSPList_Object((1,3,6,1,4,1,21296,2,2,2,2,69,1,1,5),_PxmTunnelAssociatedLSPList_Type())
pxmTunnelAssociatedLSPList.setMaxAccess('read-only')
if mibBuilder.loadTexts:pxmTunnelAssociatedLSPList.setStatus(_A)
_PxmTunnelConformance_ObjectIdentity=ObjectIdentity
pxmTunnelConformance=_PxmTunnelConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,69,3))
_PxmTunnelCompliances_ObjectIdentity=ObjectIdentity
pxmTunnelCompliances=_PxmTunnelCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,69,3,1))
_PxmTunnelGroups_ObjectIdentity=ObjectIdentity
pxmTunnelGroups=_PxmTunnelGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,69,3,2))
pxmTunnelGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,69,3,2,1))
pxmTunnelGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:pxmTunnelGroup.setStatus(_A)
pxmTunnelCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,69,3,1,1))
pxmTunnelCompliance.setObjects((_B,_K))
if mibBuilder.loadTexts:pxmTunnelCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'pxmTunnelMIB':pxmTunnelMIB,'pxmTunnelTable':pxmTunnelTable,'pxmTunnelEntry':pxmTunnelEntry,_F:pxmTunnelMTUSize,_G:pxmTunnelNum,_H:pxmTunnelId,_I:pxmTunnelSupportingEqptAid,_J:pxmTunnelAssociatedLSPList,'pxmTunnelConformance':pxmTunnelConformance,'pxmTunnelCompliances':pxmTunnelCompliances,'pxmTunnelCompliance':pxmTunnelCompliance,'pxmTunnelGroups':pxmTunnelGroups,_K:pxmTunnelGroup})