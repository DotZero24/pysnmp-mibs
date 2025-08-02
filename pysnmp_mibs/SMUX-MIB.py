_J='smuxTpriority'
_I='smuxTsubtree'
_H='read-write'
_G='invalid'
_F='smuxPindex'
_E='DisplayString'
_D='SMUX-MIB'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
_Unix_ObjectIdentity=ObjectIdentity
unix=_Unix_ObjectIdentity((1,3,6,1,4,1,4))
_Smux_ObjectIdentity=ObjectIdentity
smux=_Smux_ObjectIdentity((1,3,6,1,4,1,4,4))
_SmuxPeerTable_Object=MibTable
smuxPeerTable=_SmuxPeerTable_Object((1,3,6,1,4,1,4,4,1))
if mibBuilder.loadTexts:smuxPeerTable.setStatus(_A)
_SmuxPeerEntry_Object=MibTableRow
smuxPeerEntry=_SmuxPeerEntry_Object((1,3,6,1,4,1,4,4,1,1))
smuxPeerEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:smuxPeerEntry.setStatus(_A)
_SmuxPindex_Type=Integer32
_SmuxPindex_Object=MibTableColumn
smuxPindex=_SmuxPindex_Object((1,3,6,1,4,1,4,4,1,1,1),_SmuxPindex_Type())
smuxPindex.setMaxAccess(_B)
if mibBuilder.loadTexts:smuxPindex.setStatus(_A)
_SmuxPidentity_Type=ObjectIdentifier
_SmuxPidentity_Object=MibTableColumn
smuxPidentity=_SmuxPidentity_Object((1,3,6,1,4,1,4,4,1,1,2),_SmuxPidentity_Type())
smuxPidentity.setMaxAccess(_B)
if mibBuilder.loadTexts:smuxPidentity.setStatus(_A)
class _SmuxPdescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SmuxPdescription_Type.__name__=_E
_SmuxPdescription_Object=MibTableColumn
smuxPdescription=_SmuxPdescription_Object((1,3,6,1,4,1,4,4,1,1,3),_SmuxPdescription_Type())
smuxPdescription.setMaxAccess(_B)
if mibBuilder.loadTexts:smuxPdescription.setStatus(_A)
class _SmuxPstatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('valid',1),(_G,2),('connecting',3)))
_SmuxPstatus_Type.__name__=_C
_SmuxPstatus_Object=MibTableColumn
smuxPstatus=_SmuxPstatus_Object((1,3,6,1,4,1,4,4,1,1,4),_SmuxPstatus_Type())
smuxPstatus.setMaxAccess(_H)
if mibBuilder.loadTexts:smuxPstatus.setStatus(_A)
_SmuxTreeTable_Object=MibTable
smuxTreeTable=_SmuxTreeTable_Object((1,3,6,1,4,1,4,4,2))
if mibBuilder.loadTexts:smuxTreeTable.setStatus(_A)
_SmuxTreeEntry_Object=MibTableRow
smuxTreeEntry=_SmuxTreeEntry_Object((1,3,6,1,4,1,4,4,2,1))
smuxTreeEntry.setIndexNames((0,_D,_I),(0,_D,_J))
if mibBuilder.loadTexts:smuxTreeEntry.setStatus(_A)
_SmuxTsubtree_Type=ObjectIdentifier
_SmuxTsubtree_Object=MibTableColumn
smuxTsubtree=_SmuxTsubtree_Object((1,3,6,1,4,1,4,4,2,1,1),_SmuxTsubtree_Type())
smuxTsubtree.setMaxAccess(_B)
if mibBuilder.loadTexts:smuxTsubtree.setStatus(_A)
class _SmuxTpriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SmuxTpriority_Type.__name__=_C
_SmuxTpriority_Object=MibTableColumn
smuxTpriority=_SmuxTpriority_Object((1,3,6,1,4,1,4,4,2,1,2),_SmuxTpriority_Type())
smuxTpriority.setMaxAccess(_B)
if mibBuilder.loadTexts:smuxTpriority.setStatus(_A)
_SmuxTindex_Type=Integer32
_SmuxTindex_Object=MibTableColumn
smuxTindex=_SmuxTindex_Object((1,3,6,1,4,1,4,4,2,1,3),_SmuxTindex_Type())
smuxTindex.setMaxAccess(_B)
if mibBuilder.loadTexts:smuxTindex.setStatus(_A)
class _SmuxTstatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),(_G,2)))
_SmuxTstatus_Type.__name__=_C
_SmuxTstatus_Object=MibTableColumn
smuxTstatus=_SmuxTstatus_Object((1,3,6,1,4,1,4,4,2,1,4),_SmuxTstatus_Type())
smuxTstatus.setMaxAccess(_H)
if mibBuilder.loadTexts:smuxTstatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'unix':unix,'smux':smux,'smuxPeerTable':smuxPeerTable,'smuxPeerEntry':smuxPeerEntry,_F:smuxPindex,'smuxPidentity':smuxPidentity,'smuxPdescription':smuxPdescription,'smuxPstatus':smuxPstatus,'smuxTreeTable':smuxTreeTable,'smuxTreeEntry':smuxTreeEntry,_I:smuxTsubtree,_J:smuxTpriority,'smuxTindex':smuxTindex,'smuxTstatus':smuxTstatus})