_O='cmplsXCOppositeDirXCPtr'
_N='cmplsXCExtTunnelPointer'
_M='read-create'
_L='mplsXCOutSegmentIndex'
_K='mplsXCIndex'
_J='mplsXCInSegmentIndex'
_I='mplsLsrNotificationGroup'
_H='cmplsXCExtGroup'
_G='mplsXCGroup'
_F='mplsPerfGroup'
_E='mplsOutSegmentGroup'
_D='mplsInSegmentGroup'
_C='CISCO-MPLS-LSR-EXT-STD-MIB'
_B='current'
_A='MPLS-LSR-STD-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
mplsInSegmentGroup,mplsLsrNotificationGroup,mplsOutSegmentGroup,mplsPerfGroup,mplsXCGroup,mplsXCInSegmentIndex,mplsXCIndex,mplsXCOutSegmentIndex=mibBuilder.importSymbols(_A,_D,_I,_E,_F,_G,_J,_K,_L)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowPointer,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowPointer','TextualConvention')
cmplsLsrExtStdMIB=ModuleIdentity((1,3,6,1,4,1,9,10,145))
if mibBuilder.loadTexts:cmplsLsrExtStdMIB.setRevisions(('2012-02-22 00:00',))
_CmplsLsrExtNotifications_ObjectIdentity=ObjectIdentity
cmplsLsrExtNotifications=_CmplsLsrExtNotifications_ObjectIdentity((1,3,6,1,4,1,9,10,145,0))
_CmplsLsrExtObjects_ObjectIdentity=ObjectIdentity
cmplsLsrExtObjects=_CmplsLsrExtObjects_ObjectIdentity((1,3,6,1,4,1,9,10,145,1))
_CmplsXCExtTable_Object=MibTable
cmplsXCExtTable=_CmplsXCExtTable_Object((1,3,6,1,4,1,9,10,145,1,1))
if mibBuilder.loadTexts:cmplsXCExtTable.setStatus(_B)
_CmplsXCExtEntry_Object=MibTableRow
cmplsXCExtEntry=_CmplsXCExtEntry_Object((1,3,6,1,4,1,9,10,145,1,1,1))
cmplsXCExtEntry.setIndexNames((0,_A,_K),(0,_A,_J),(0,_A,_L))
if mibBuilder.loadTexts:cmplsXCExtEntry.setStatus(_B)
_CmplsXCExtTunnelPointer_Type=RowPointer
_CmplsXCExtTunnelPointer_Object=MibTableColumn
cmplsXCExtTunnelPointer=_CmplsXCExtTunnelPointer_Object((1,3,6,1,4,1,9,10,145,1,1,1,1),_CmplsXCExtTunnelPointer_Type())
cmplsXCExtTunnelPointer.setMaxAccess(_M)
if mibBuilder.loadTexts:cmplsXCExtTunnelPointer.setStatus(_B)
_CmplsXCOppositeDirXCPtr_Type=RowPointer
_CmplsXCOppositeDirXCPtr_Object=MibTableColumn
cmplsXCOppositeDirXCPtr=_CmplsXCOppositeDirXCPtr_Object((1,3,6,1,4,1,9,10,145,1,1,1,2),_CmplsXCOppositeDirXCPtr_Type())
cmplsXCOppositeDirXCPtr.setMaxAccess(_M)
if mibBuilder.loadTexts:cmplsXCOppositeDirXCPtr.setStatus(_B)
_CmplsLsrExtConformance_ObjectIdentity=ObjectIdentity
cmplsLsrExtConformance=_CmplsLsrExtConformance_ObjectIdentity((1,3,6,1,4,1,9,10,145,2))
_CmplsLsrExtGroups_ObjectIdentity=ObjectIdentity
cmplsLsrExtGroups=_CmplsLsrExtGroups_ObjectIdentity((1,3,6,1,4,1,9,10,145,2,1))
_CmplsLsrExtCompliances_ObjectIdentity=ObjectIdentity
cmplsLsrExtCompliances=_CmplsLsrExtCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,145,2,2))
cmplsXCExtGroup=ObjectGroup((1,3,6,1,4,1,9,10,145,2,1,1))
cmplsXCExtGroup.setObjects(*((_C,_N),(_C,_O)))
if mibBuilder.loadTexts:cmplsXCExtGroup.setStatus(_B)
cmplsLsrExtModuleFullCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,145,2,2,1))
cmplsLsrExtModuleFullCompliance.setObjects(*((_A,_D),(_A,_E),(_A,_G),(_A,_F),(_A,_I),(_C,_H)))
if mibBuilder.loadTexts:cmplsLsrExtModuleFullCompliance.setStatus(_B)
cmplsLsrExtModuleReadOnlyCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,145,2,2,2))
cmplsLsrExtModuleReadOnlyCompliance.setObjects(*((_A,'mplsInterfaceGroup'),(_A,_D),(_A,_E),(_A,_G),(_A,_F),(_C,_H)))
if mibBuilder.loadTexts:cmplsLsrExtModuleReadOnlyCompliance.setStatus(_B)
mibBuilder.exportSymbols(_C,**{'cmplsLsrExtStdMIB':cmplsLsrExtStdMIB,'cmplsLsrExtNotifications':cmplsLsrExtNotifications,'cmplsLsrExtObjects':cmplsLsrExtObjects,'cmplsXCExtTable':cmplsXCExtTable,'cmplsXCExtEntry':cmplsXCExtEntry,_N:cmplsXCExtTunnelPointer,_O:cmplsXCOppositeDirXCPtr,'cmplsLsrExtConformance':cmplsLsrExtConformance,'cmplsLsrExtGroups':cmplsLsrExtGroups,_H:cmplsXCExtGroup,'cmplsLsrExtCompliances':cmplsLsrExtCompliances,'cmplsLsrExtModuleFullCompliance':cmplsLsrExtModuleFullCompliance,'cmplsLsrExtModuleReadOnlyCompliance':cmplsLsrExtModuleReadOnlyCompliance})