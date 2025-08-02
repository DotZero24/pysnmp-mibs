_O='mplsXCExtReadOnlyObjectsGroup'
_N='mplsXCExtGroup'
_M='mplsXCOutSegmentIndex'
_L='mplsXCIndex'
_K='mplsXCInSegmentIndex'
_J='mplsXCGroup'
_I='mplsLsrNotificationGroup'
_H='mplsInterfaceGroup'
_G='mplsXCExtOppositeDirXCPtr'
_F='mplsXCExtTunnelPointer'
_E='mplsOutSegmentGroup'
_D='mplsInSegmentGroup'
_C='MPLS-LSR-EXT-STD-MIB'
_B='current'
_A='MPLS-LSR-STD-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mplsInSegmentGroup,mplsInterfaceGroup,mplsLsrNotificationGroup,mplsOutSegmentGroup,mplsXCGroup,mplsXCInSegmentIndex,mplsXCIndex,mplsXCOutSegmentIndex=mibBuilder.importSymbols(_A,_D,_H,_I,_E,_J,_K,_L,_M)
mplsStdMIB,=mibBuilder.importSymbols('MPLS-TC-STD-MIB','mplsStdMIB')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowPointer,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowPointer','TextualConvention')
mplsLsrExtStdMIB=ModuleIdentity((1,3,6,1,2,1,10,166,19))
if mibBuilder.loadTexts:mplsLsrExtStdMIB.setRevisions(('2015-02-02 00:00',))
_MplsLsrExtNotifications_ObjectIdentity=ObjectIdentity
mplsLsrExtNotifications=_MplsLsrExtNotifications_ObjectIdentity((1,3,6,1,2,1,10,166,19,0))
_MplsLsrExtObjects_ObjectIdentity=ObjectIdentity
mplsLsrExtObjects=_MplsLsrExtObjects_ObjectIdentity((1,3,6,1,2,1,10,166,19,1))
_MplsXCExtTable_Object=MibTable
mplsXCExtTable=_MplsXCExtTable_Object((1,3,6,1,2,1,10,166,19,1,1))
if mibBuilder.loadTexts:mplsXCExtTable.setStatus(_B)
_MplsXCExtEntry_Object=MibTableRow
mplsXCExtEntry=_MplsXCExtEntry_Object((1,3,6,1,2,1,10,166,19,1,1,1))
mplsXCExtEntry.setIndexNames((0,_A,_L),(0,_A,_K),(0,_A,_M))
if mibBuilder.loadTexts:mplsXCExtEntry.setStatus(_B)
_MplsXCExtTunnelPointer_Type=RowPointer
_MplsXCExtTunnelPointer_Object=MibTableColumn
mplsXCExtTunnelPointer=_MplsXCExtTunnelPointer_Object((1,3,6,1,2,1,10,166,19,1,1,1,1),_MplsXCExtTunnelPointer_Type())
mplsXCExtTunnelPointer.setMaxAccess('read-only')
if mibBuilder.loadTexts:mplsXCExtTunnelPointer.setStatus(_B)
_MplsXCExtOppositeDirXCPtr_Type=RowPointer
_MplsXCExtOppositeDirXCPtr_Object=MibTableColumn
mplsXCExtOppositeDirXCPtr=_MplsXCExtOppositeDirXCPtr_Object((1,3,6,1,2,1,10,166,19,1,1,1,2),_MplsXCExtOppositeDirXCPtr_Type())
mplsXCExtOppositeDirXCPtr.setMaxAccess('read-create')
if mibBuilder.loadTexts:mplsXCExtOppositeDirXCPtr.setStatus(_B)
_MplsLsrExtConformance_ObjectIdentity=ObjectIdentity
mplsLsrExtConformance=_MplsLsrExtConformance_ObjectIdentity((1,3,6,1,2,1,10,166,19,2))
_MplsLsrExtCompliances_ObjectIdentity=ObjectIdentity
mplsLsrExtCompliances=_MplsLsrExtCompliances_ObjectIdentity((1,3,6,1,2,1,10,166,19,2,1))
_MplsLsrExtGroups_ObjectIdentity=ObjectIdentity
mplsLsrExtGroups=_MplsLsrExtGroups_ObjectIdentity((1,3,6,1,2,1,10,166,19,2,2))
mplsXCExtGroup=ObjectGroup((1,3,6,1,2,1,10,166,19,2,2,1))
mplsXCExtGroup.setObjects(*((_C,_F),(_C,_G)))
if mibBuilder.loadTexts:mplsXCExtGroup.setStatus(_B)
mplsXCExtReadOnlyObjectsGroup=ObjectGroup((1,3,6,1,2,1,10,166,19,2,2,2))
mplsXCExtReadOnlyObjectsGroup.setObjects(*((_C,_F),(_C,_G)))
if mibBuilder.loadTexts:mplsXCExtReadOnlyObjectsGroup.setStatus(_B)
mplsLsrExtModuleFullCompliance=ModuleCompliance((1,3,6,1,2,1,10,166,19,2,1,1))
mplsLsrExtModuleFullCompliance.setObjects(*((_A,_D),(_A,_E),(_A,_J),(_A,_I),(_C,_N)))
if mibBuilder.loadTexts:mplsLsrExtModuleFullCompliance.setStatus(_B)
mplsLsrExtModuleReadOnlyCompliance=ModuleCompliance((1,3,6,1,2,1,10,166,19,2,1,2))
mplsLsrExtModuleReadOnlyCompliance.setObjects(*((_A,_H),(_A,_D),(_A,_E),(_C,_O)))
if mibBuilder.loadTexts:mplsLsrExtModuleReadOnlyCompliance.setStatus(_B)
mibBuilder.exportSymbols(_C,**{'mplsLsrExtStdMIB':mplsLsrExtStdMIB,'mplsLsrExtNotifications':mplsLsrExtNotifications,'mplsLsrExtObjects':mplsLsrExtObjects,'mplsXCExtTable':mplsXCExtTable,'mplsXCExtEntry':mplsXCExtEntry,_F:mplsXCExtTunnelPointer,_G:mplsXCExtOppositeDirXCPtr,'mplsLsrExtConformance':mplsLsrExtConformance,'mplsLsrExtCompliances':mplsLsrExtCompliances,'mplsLsrExtModuleFullCompliance':mplsLsrExtModuleFullCompliance,'mplsLsrExtModuleReadOnlyCompliance':mplsLsrExtModuleReadOnlyCompliance,'mplsLsrExtGroups':mplsLsrExtGroups,_N:mplsXCExtGroup,_O:mplsXCExtReadOnlyObjectsGroup})