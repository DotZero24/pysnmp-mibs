_F='nbsVlanTagsPortIfIndex'
_E='NBS-VLAN-TAGS-MIB'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
nbs,=mibBuilder.importSymbols('NBS-MIB','nbs')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
nbsVlanTagsMib=ModuleIdentity((1,3,6,1,4,1,629,219))
_NbsVlanTagsPortGrp_ObjectIdentity=ObjectIdentity
nbsVlanTagsPortGrp=_NbsVlanTagsPortGrp_ObjectIdentity((1,3,6,1,4,1,629,219,1))
if mibBuilder.loadTexts:nbsVlanTagsPortGrp.setStatus(_A)
_NbsVlanTagsPortTableSize_Type=Unsigned32
_NbsVlanTagsPortTableSize_Object=MibScalar
nbsVlanTagsPortTableSize=_NbsVlanTagsPortTableSize_Object((1,3,6,1,4,1,629,219,1,1),_NbsVlanTagsPortTableSize_Type())
nbsVlanTagsPortTableSize.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsVlanTagsPortTableSize.setStatus(_A)
_NbsVlanTagsPortTable_Object=MibTable
nbsVlanTagsPortTable=_NbsVlanTagsPortTable_Object((1,3,6,1,4,1,629,219,1,2))
if mibBuilder.loadTexts:nbsVlanTagsPortTable.setStatus(_A)
_NbsVlanTagsPortEntry_Object=MibTableRow
nbsVlanTagsPortEntry=_NbsVlanTagsPortEntry_Object((1,3,6,1,4,1,629,219,1,2,1))
nbsVlanTagsPortEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:nbsVlanTagsPortEntry.setStatus(_A)
_NbsVlanTagsPortIfIndex_Type=InterfaceIndex
_NbsVlanTagsPortIfIndex_Object=MibTableColumn
nbsVlanTagsPortIfIndex=_NbsVlanTagsPortIfIndex_Object((1,3,6,1,4,1,629,219,1,2,1,1),_NbsVlanTagsPortIfIndex_Type())
nbsVlanTagsPortIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsVlanTagsPortIfIndex.setStatus(_A)
class _NbsVlanTagsPortAction_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('notSupported',1),('add',2),('strip',3),('ignore',4)))
_NbsVlanTagsPortAction_Type.__name__=_B
_NbsVlanTagsPortAction_Object=MibTableColumn
nbsVlanTagsPortAction=_NbsVlanTagsPortAction_Object((1,3,6,1,4,1,629,219,1,2,1,2),_NbsVlanTagsPortAction_Type())
nbsVlanTagsPortAction.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsVlanTagsPortAction.setStatus(_A)
class _NbsVlanTagsPortVid_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_NbsVlanTagsPortVid_Type.__name__=_B
_NbsVlanTagsPortVid_Object=MibTableColumn
nbsVlanTagsPortVid=_NbsVlanTagsPortVid_Object((1,3,6,1,4,1,629,219,1,2,1,3),_NbsVlanTagsPortVid_Type())
nbsVlanTagsPortVid.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsVlanTagsPortVid.setStatus(_A)
class _NbsVlanTagsPortPriority_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_NbsVlanTagsPortPriority_Type.__name__=_B
_NbsVlanTagsPortPriority_Object=MibTableColumn
nbsVlanTagsPortPriority=_NbsVlanTagsPortPriority_Object((1,3,6,1,4,1,629,219,1,2,1,4),_NbsVlanTagsPortPriority_Type())
nbsVlanTagsPortPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsVlanTagsPortPriority.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'nbsVlanTagsMib':nbsVlanTagsMib,'nbsVlanTagsPortGrp':nbsVlanTagsPortGrp,'nbsVlanTagsPortTableSize':nbsVlanTagsPortTableSize,'nbsVlanTagsPortTable':nbsVlanTagsPortTable,'nbsVlanTagsPortEntry':nbsVlanTagsPortEntry,_F:nbsVlanTagsPortIfIndex,'nbsVlanTagsPortAction':nbsVlanTagsPortAction,'nbsVlanTagsPortVid':nbsVlanTagsPortVid,'nbsVlanTagsPortPriority':nbsVlanTagsPortPriority})