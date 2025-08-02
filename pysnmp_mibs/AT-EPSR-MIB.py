_O='epsrSecondaryIfState'
_N='epsrSecondaryIfIndex'
_M='epsrPrimaryIfState'
_L='epsrPrimaryIfIndex'
_K='epsrControlVlanId'
_J='epsrToState'
_I='epsrFromState'
_H='epsrNodeTrapType'
_G='Integer32'
_F='DisplayStringUnsized'
_E='epsrDomainName'
_D='unknown'
_C='read-only'
_B='AT-EPSR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
DisplayStringUnsized,modules=mibBuilder.importSymbols('AT-SMI-MIB',_F,'modules')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
epsr=ModuleIdentity((1,3,6,1,4,1,207,8,4,4,4,136))
if mibBuilder.loadTexts:epsr.setRevisions(('2006-11-22 12:12','2006-02-16 16:19'))
class EpsrNodeState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('idle',0),('complete',1),('failed',2),('linksUp',3),('linksDown',4),('preForward',5),(_D,6)))
class EpsrInterfaceState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_D,0),('blocked',1),('forward',2)))
_EpsrEvents_ObjectIdentity=ObjectIdentity
epsrEvents=_EpsrEvents_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,136,1))
_EpsrEventVariablesTable_Object=MibTable
epsrEventVariablesTable=_EpsrEventVariablesTable_Object((1,3,6,1,4,1,207,8,4,4,4,136,2))
if mibBuilder.loadTexts:epsrEventVariablesTable.setStatus(_A)
_EpsrEventVariablesEntry_Object=MibTableRow
epsrEventVariablesEntry=_EpsrEventVariablesEntry_Object((1,3,6,1,4,1,207,8,4,4,4,136,2,1))
epsrEventVariablesEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:epsrEventVariablesEntry.setStatus(_A)
class _EpsrNodeTrapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_D,0),('masterNodeTrap',1),('transitNodeTrap',2)))
_EpsrNodeTrapType_Type.__name__=_G
_EpsrNodeTrapType_Object=MibTableColumn
epsrNodeTrapType=_EpsrNodeTrapType_Object((1,3,6,1,4,1,207,8,4,4,4,136,2,1,1),_EpsrNodeTrapType_Type())
epsrNodeTrapType.setMaxAccess(_C)
if mibBuilder.loadTexts:epsrNodeTrapType.setStatus(_A)
class _EpsrDomainName_Type(DisplayStringUnsized):subtypeSpec=DisplayStringUnsized.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_EpsrDomainName_Type.__name__=_F
_EpsrDomainName_Object=MibTableColumn
epsrDomainName=_EpsrDomainName_Object((1,3,6,1,4,1,207,8,4,4,4,136,2,1,2),_EpsrDomainName_Type())
epsrDomainName.setMaxAccess(_C)
if mibBuilder.loadTexts:epsrDomainName.setStatus(_A)
_EpsrFromState_Type=EpsrNodeState
_EpsrFromState_Object=MibTableColumn
epsrFromState=_EpsrFromState_Object((1,3,6,1,4,1,207,8,4,4,4,136,2,1,3),_EpsrFromState_Type())
epsrFromState.setMaxAccess(_C)
if mibBuilder.loadTexts:epsrFromState.setStatus(_A)
_EpsrToState_Type=EpsrNodeState
_EpsrToState_Object=MibTableColumn
epsrToState=_EpsrToState_Object((1,3,6,1,4,1,207,8,4,4,4,136,2,1,4),_EpsrToState_Type())
epsrToState.setMaxAccess(_C)
if mibBuilder.loadTexts:epsrToState.setStatus(_A)
_EpsrControlVlanId_Type=Integer32
_EpsrControlVlanId_Object=MibTableColumn
epsrControlVlanId=_EpsrControlVlanId_Object((1,3,6,1,4,1,207,8,4,4,4,136,2,1,5),_EpsrControlVlanId_Type())
epsrControlVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:epsrControlVlanId.setStatus(_A)
_EpsrPrimaryIfIndex_Type=InterfaceIndex
_EpsrPrimaryIfIndex_Object=MibTableColumn
epsrPrimaryIfIndex=_EpsrPrimaryIfIndex_Object((1,3,6,1,4,1,207,8,4,4,4,136,2,1,6),_EpsrPrimaryIfIndex_Type())
epsrPrimaryIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:epsrPrimaryIfIndex.setStatus(_A)
_EpsrPrimaryIfState_Type=EpsrInterfaceState
_EpsrPrimaryIfState_Object=MibTableColumn
epsrPrimaryIfState=_EpsrPrimaryIfState_Object((1,3,6,1,4,1,207,8,4,4,4,136,2,1,7),_EpsrPrimaryIfState_Type())
epsrPrimaryIfState.setMaxAccess(_C)
if mibBuilder.loadTexts:epsrPrimaryIfState.setStatus(_A)
_EpsrSecondaryIfIndex_Type=InterfaceIndex
_EpsrSecondaryIfIndex_Object=MibTableColumn
epsrSecondaryIfIndex=_EpsrSecondaryIfIndex_Object((1,3,6,1,4,1,207,8,4,4,4,136,2,1,8),_EpsrSecondaryIfIndex_Type())
epsrSecondaryIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:epsrSecondaryIfIndex.setStatus(_A)
_EpsrSecondaryIfState_Type=EpsrInterfaceState
_EpsrSecondaryIfState_Object=MibTableColumn
epsrSecondaryIfState=_EpsrSecondaryIfState_Object((1,3,6,1,4,1,207,8,4,4,4,136,2,1,9),_EpsrSecondaryIfState_Type())
epsrSecondaryIfState.setMaxAccess(_C)
if mibBuilder.loadTexts:epsrSecondaryIfState.setStatus(_A)
epsrNodeTrap=NotificationType((1,3,6,1,4,1,207,8,4,4,4,136,1,1))
epsrNodeTrap.setObjects(*((_B,_H),(_B,_E),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:epsrNodeTrap.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'EpsrNodeState':EpsrNodeState,'EpsrInterfaceState':EpsrInterfaceState,'epsr':epsr,'epsrEvents':epsrEvents,'epsrNodeTrap':epsrNodeTrap,'epsrEventVariablesTable':epsrEventVariablesTable,'epsrEventVariablesEntry':epsrEventVariablesEntry,_H:epsrNodeTrapType,_E:epsrDomainName,_I:epsrFromState,_J:epsrToState,_K:epsrControlVlanId,_L:epsrPrimaryIfIndex,_M:epsrPrimaryIfState,_N:epsrSecondaryIfIndex,_O:epsrSecondaryIfState})