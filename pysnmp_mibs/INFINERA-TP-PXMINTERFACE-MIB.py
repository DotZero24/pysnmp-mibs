_H='pxmInterfaceGroup'
_G='pxmInterfaceMacAddress'
_F='pxmInterfaceProtocolType'
_E='read-only'
_D='ifIndex'
_C='IF-MIB'
_B='INFINERA-TP-PXMINTERFACE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_C,_D)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
InfnPxmIntfProtocolType,=mibBuilder.importSymbols('INFINERA-TC-MIB','InfnPxmIntfProtocolType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
pxmInterfaceMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,73))
if mibBuilder.loadTexts:pxmInterfaceMIB.setRevisions(('2016-05-20 00:00',))
_PxmInterfaceTable_Object=MibTable
pxmInterfaceTable=_PxmInterfaceTable_Object((1,3,6,1,4,1,21296,2,2,2,2,73,1))
if mibBuilder.loadTexts:pxmInterfaceTable.setStatus(_A)
_PxmInterfaceEntry_Object=MibTableRow
pxmInterfaceEntry=_PxmInterfaceEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,73,1,1))
pxmInterfaceEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:pxmInterfaceEntry.setStatus(_A)
_PxmInterfaceProtocolType_Type=InfnPxmIntfProtocolType
_PxmInterfaceProtocolType_Object=MibTableColumn
pxmInterfaceProtocolType=_PxmInterfaceProtocolType_Object((1,3,6,1,4,1,21296,2,2,2,2,73,1,1,1),_PxmInterfaceProtocolType_Type())
pxmInterfaceProtocolType.setMaxAccess(_E)
if mibBuilder.loadTexts:pxmInterfaceProtocolType.setStatus(_A)
_PxmInterfaceMacAddress_Type=DisplayString
_PxmInterfaceMacAddress_Object=MibTableColumn
pxmInterfaceMacAddress=_PxmInterfaceMacAddress_Object((1,3,6,1,4,1,21296,2,2,2,2,73,1,1,2),_PxmInterfaceMacAddress_Type())
pxmInterfaceMacAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:pxmInterfaceMacAddress.setStatus(_A)
_PxmInterfaceConformance_ObjectIdentity=ObjectIdentity
pxmInterfaceConformance=_PxmInterfaceConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,73,3))
_PxmInterfaceCompliances_ObjectIdentity=ObjectIdentity
pxmInterfaceCompliances=_PxmInterfaceCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,73,3,1))
_PxmInterfaceGroups_ObjectIdentity=ObjectIdentity
pxmInterfaceGroups=_PxmInterfaceGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,73,3,2))
pxmInterfaceGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,73,3,2,1))
pxmInterfaceGroup.setObjects(*((_B,_F),(_B,_G)))
if mibBuilder.loadTexts:pxmInterfaceGroup.setStatus(_A)
pxmInterfaceCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,73,3,1,1))
pxmInterfaceCompliance.setObjects((_B,_H))
if mibBuilder.loadTexts:pxmInterfaceCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'pxmInterfaceMIB':pxmInterfaceMIB,'pxmInterfaceTable':pxmInterfaceTable,'pxmInterfaceEntry':pxmInterfaceEntry,_F:pxmInterfaceProtocolType,_G:pxmInterfaceMacAddress,'pxmInterfaceConformance':pxmInterfaceConformance,'pxmInterfaceCompliances':pxmInterfaceCompliances,'pxmInterfaceCompliance':pxmInterfaceCompliance,'pxmInterfaceGroups':pxmInterfaceGroups,_H:pxmInterfaceGroup})