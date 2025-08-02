_P='atEpsrv2SecondaryIfState'
_O='atEpsrv2SecondaryIfIndex'
_N='atEpsrv2PrimaryIfState'
_M='atEpsrv2PrimaryIfIndex'
_L='atEpsrv2ControlVlanId'
_K='atEpsrv2CurrentState'
_J='atEpsrv2FromState'
_I='atEpsrv2DomainName'
_H='atEpsrv2NodeType'
_G='unknown'
_F='Integer32'
_E='DisplayStringUnsized'
_D='atEpsrv2DomainID'
_C='read-only'
_B='AT-EPSRv2-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
DisplayStringUnsized,modules,sysinfo=mibBuilder.importSymbols('AT-SMI-MIB',_E,'modules','sysinfo')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
atEpsrv2=ModuleIdentity((1,3,6,1,4,1,207,8,4,4,4,536))
if mibBuilder.loadTexts:atEpsrv2.setRevisions(('2008-12-23 01:30',))
class AtEpsrv2NodeState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('idle',0),('complete',1),('failed',2),('linksUp',3),('linksDown',4),('preForward',5),(_G,6)))
class AtEpsrv2InterfaceState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),('down',2),('blocked',3),('forward',4)))
_AtEpsrv2Events_ObjectIdentity=ObjectIdentity
atEpsrv2Events=_AtEpsrv2Events_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,536,1))
_AtEpsrv2VariablesTable_Object=MibTable
atEpsrv2VariablesTable=_AtEpsrv2VariablesTable_Object((1,3,6,1,4,1,207,8,4,4,4,536,2))
if mibBuilder.loadTexts:atEpsrv2VariablesTable.setStatus(_A)
_AtEpsrv2VariablesEntry_Object=MibTableRow
atEpsrv2VariablesEntry=_AtEpsrv2VariablesEntry_Object((1,3,6,1,4,1,207,8,4,4,4,536,2,1))
atEpsrv2VariablesEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:atEpsrv2VariablesEntry.setStatus(_A)
class _AtEpsrv2NodeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('masterNode',1),('transitNode',2)))
_AtEpsrv2NodeType_Type.__name__=_F
_AtEpsrv2NodeType_Object=MibTableColumn
atEpsrv2NodeType=_AtEpsrv2NodeType_Object((1,3,6,1,4,1,207,8,4,4,4,536,2,1,1),_AtEpsrv2NodeType_Type())
atEpsrv2NodeType.setMaxAccess(_C)
if mibBuilder.loadTexts:atEpsrv2NodeType.setStatus(_A)
class _AtEpsrv2DomainName_Type(DisplayStringUnsized):subtypeSpec=DisplayStringUnsized.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_AtEpsrv2DomainName_Type.__name__=_E
_AtEpsrv2DomainName_Object=MibTableColumn
atEpsrv2DomainName=_AtEpsrv2DomainName_Object((1,3,6,1,4,1,207,8,4,4,4,536,2,1,2),_AtEpsrv2DomainName_Type())
atEpsrv2DomainName.setMaxAccess(_C)
if mibBuilder.loadTexts:atEpsrv2DomainName.setStatus(_A)
_AtEpsrv2DomainID_Type=Integer32
_AtEpsrv2DomainID_Object=MibTableColumn
atEpsrv2DomainID=_AtEpsrv2DomainID_Object((1,3,6,1,4,1,207,8,4,4,4,536,2,1,3),_AtEpsrv2DomainID_Type())
atEpsrv2DomainID.setMaxAccess(_C)
if mibBuilder.loadTexts:atEpsrv2DomainID.setStatus(_A)
_AtEpsrv2FromState_Type=AtEpsrv2NodeState
_AtEpsrv2FromState_Object=MibTableColumn
atEpsrv2FromState=_AtEpsrv2FromState_Object((1,3,6,1,4,1,207,8,4,4,4,536,2,1,4),_AtEpsrv2FromState_Type())
atEpsrv2FromState.setMaxAccess(_C)
if mibBuilder.loadTexts:atEpsrv2FromState.setStatus(_A)
_AtEpsrv2CurrentState_Type=AtEpsrv2NodeState
_AtEpsrv2CurrentState_Object=MibTableColumn
atEpsrv2CurrentState=_AtEpsrv2CurrentState_Object((1,3,6,1,4,1,207,8,4,4,4,536,2,1,5),_AtEpsrv2CurrentState_Type())
atEpsrv2CurrentState.setMaxAccess(_C)
if mibBuilder.loadTexts:atEpsrv2CurrentState.setStatus(_A)
_AtEpsrv2ControlVlanId_Type=Integer32
_AtEpsrv2ControlVlanId_Object=MibTableColumn
atEpsrv2ControlVlanId=_AtEpsrv2ControlVlanId_Object((1,3,6,1,4,1,207,8,4,4,4,536,2,1,6),_AtEpsrv2ControlVlanId_Type())
atEpsrv2ControlVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:atEpsrv2ControlVlanId.setStatus(_A)
_AtEpsrv2PrimaryIfIndex_Type=InterfaceIndex
_AtEpsrv2PrimaryIfIndex_Object=MibTableColumn
atEpsrv2PrimaryIfIndex=_AtEpsrv2PrimaryIfIndex_Object((1,3,6,1,4,1,207,8,4,4,4,536,2,1,7),_AtEpsrv2PrimaryIfIndex_Type())
atEpsrv2PrimaryIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:atEpsrv2PrimaryIfIndex.setStatus(_A)
_AtEpsrv2PrimaryIfState_Type=AtEpsrv2InterfaceState
_AtEpsrv2PrimaryIfState_Object=MibTableColumn
atEpsrv2PrimaryIfState=_AtEpsrv2PrimaryIfState_Object((1,3,6,1,4,1,207,8,4,4,4,536,2,1,8),_AtEpsrv2PrimaryIfState_Type())
atEpsrv2PrimaryIfState.setMaxAccess(_C)
if mibBuilder.loadTexts:atEpsrv2PrimaryIfState.setStatus(_A)
_AtEpsrv2SecondaryIfIndex_Type=InterfaceIndex
_AtEpsrv2SecondaryIfIndex_Object=MibTableColumn
atEpsrv2SecondaryIfIndex=_AtEpsrv2SecondaryIfIndex_Object((1,3,6,1,4,1,207,8,4,4,4,536,2,1,9),_AtEpsrv2SecondaryIfIndex_Type())
atEpsrv2SecondaryIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:atEpsrv2SecondaryIfIndex.setStatus(_A)
_AtEpsrv2SecondaryIfState_Type=AtEpsrv2InterfaceState
_AtEpsrv2SecondaryIfState_Object=MibTableColumn
atEpsrv2SecondaryIfState=_AtEpsrv2SecondaryIfState_Object((1,3,6,1,4,1,207,8,4,4,4,536,2,1,10),_AtEpsrv2SecondaryIfState_Type())
atEpsrv2SecondaryIfState.setMaxAccess(_C)
if mibBuilder.loadTexts:atEpsrv2SecondaryIfState.setStatus(_A)
atEpsrv2NodeTrap=NotificationType((1,3,6,1,4,1,207,8,4,4,4,536,1,1))
atEpsrv2NodeTrap.setObjects(*((_B,_H),(_B,_I),(_B,_D),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:atEpsrv2NodeTrap.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'AtEpsrv2NodeState':AtEpsrv2NodeState,'AtEpsrv2InterfaceState':AtEpsrv2InterfaceState,'atEpsrv2':atEpsrv2,'atEpsrv2Events':atEpsrv2Events,'atEpsrv2NodeTrap':atEpsrv2NodeTrap,'atEpsrv2VariablesTable':atEpsrv2VariablesTable,'atEpsrv2VariablesEntry':atEpsrv2VariablesEntry,_H:atEpsrv2NodeType,_I:atEpsrv2DomainName,_D:atEpsrv2DomainID,_J:atEpsrv2FromState,_K:atEpsrv2CurrentState,_L:atEpsrv2ControlVlanId,_M:atEpsrv2PrimaryIfIndex,_N:atEpsrv2PrimaryIfState,_O:atEpsrv2SecondaryIfIndex,_P:atEpsrv2SecondaryIfState})