_U='fsPFXv6MIBGroup'
_T='fsSlaacRequestSuccessNumber'
_S='fsSlaacRequestNumber'
_R='fsPFXv6IfUserate'
_Q='fsPFXv6IfFrees'
_P='fsPFXv6IfAccepts'
_O='fsPFXv6IfRejects'
_N='fsPFXv6IfTotal'
_M='fsPFXv6IfName'
_L='fsPFXv6Userate'
_K='fsPFXv6Frees'
_J='fsPFXv6Accepts'
_I='fsPFXv6Rejects'
_H='fsPFXv6Total'
_G='fsPFXv6IfIfIndex'
_F='fsPFXv6Name'
_E='DisplayString'
_D='Integer32'
_C='read-only'
_B='FS-PFXV6-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
IfIndex,=mibBuilder.importSymbols('FS-TC','IfIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','RowStatus','TextualConvention')
fsPFXv6MIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,134))
if mibBuilder.loadTexts:fsPFXv6MIB.setRevisions(('2015-01-13 00:00',))
_FsPFXv6MIBObjects_ObjectIdentity=ObjectIdentity
fsPFXv6MIBObjects=_FsPFXv6MIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,134,1))
_FsPFXv6Table_Object=MibTable
fsPFXv6Table=_FsPFXv6Table_Object((1,3,6,1,4,1,52642,1,1,10,2,134,1,1))
if mibBuilder.loadTexts:fsPFXv6Table.setStatus(_A)
_FsPFXv6Entry_Object=MibTableRow
fsPFXv6Entry=_FsPFXv6Entry_Object((1,3,6,1,4,1,52642,1,1,10,2,134,1,1,1))
fsPFXv6Entry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:fsPFXv6Entry.setStatus(_A)
class _FsPFXv6Name_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsPFXv6Name_Type.__name__=_E
_FsPFXv6Name_Object=MibTableColumn
fsPFXv6Name=_FsPFXv6Name_Object((1,3,6,1,4,1,52642,1,1,10,2,134,1,1,1,1),_FsPFXv6Name_Type())
fsPFXv6Name.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPFXv6Name.setStatus(_A)
_FsPFXv6Total_Type=Integer32
_FsPFXv6Total_Object=MibTableColumn
fsPFXv6Total=_FsPFXv6Total_Object((1,3,6,1,4,1,52642,1,1,10,2,134,1,1,1,2),_FsPFXv6Total_Type())
fsPFXv6Total.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPFXv6Total.setStatus(_A)
_FsPFXv6Rejects_Type=Integer32
_FsPFXv6Rejects_Object=MibTableColumn
fsPFXv6Rejects=_FsPFXv6Rejects_Object((1,3,6,1,4,1,52642,1,1,10,2,134,1,1,1,3),_FsPFXv6Rejects_Type())
fsPFXv6Rejects.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPFXv6Rejects.setStatus(_A)
_FsPFXv6Accepts_Type=Integer32
_FsPFXv6Accepts_Object=MibTableColumn
fsPFXv6Accepts=_FsPFXv6Accepts_Object((1,3,6,1,4,1,52642,1,1,10,2,134,1,1,1,4),_FsPFXv6Accepts_Type())
fsPFXv6Accepts.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPFXv6Accepts.setStatus(_A)
_FsPFXv6Frees_Type=Integer32
_FsPFXv6Frees_Object=MibTableColumn
fsPFXv6Frees=_FsPFXv6Frees_Object((1,3,6,1,4,1,52642,1,1,10,2,134,1,1,1,5),_FsPFXv6Frees_Type())
fsPFXv6Frees.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPFXv6Frees.setStatus(_A)
class _FsPFXv6Userate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_FsPFXv6Userate_Type.__name__=_D
_FsPFXv6Userate_Object=MibTableColumn
fsPFXv6Userate=_FsPFXv6Userate_Object((1,3,6,1,4,1,52642,1,1,10,2,134,1,1,1,6),_FsPFXv6Userate_Type())
fsPFXv6Userate.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPFXv6Userate.setStatus(_A)
_FsPFXv6IfTable_Object=MibTable
fsPFXv6IfTable=_FsPFXv6IfTable_Object((1,3,6,1,4,1,52642,1,1,10,2,134,1,2))
if mibBuilder.loadTexts:fsPFXv6IfTable.setStatus(_A)
_FsPFXv6IfEntry_Object=MibTableRow
fsPFXv6IfEntry=_FsPFXv6IfEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,134,1,2,1))
fsPFXv6IfEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:fsPFXv6IfEntry.setStatus(_A)
_FsPFXv6IfIfIndex_Type=IfIndex
_FsPFXv6IfIfIndex_Object=MibTableColumn
fsPFXv6IfIfIndex=_FsPFXv6IfIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,134,1,2,1,1),_FsPFXv6IfIfIndex_Type())
fsPFXv6IfIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPFXv6IfIfIndex.setStatus(_A)
class _FsPFXv6IfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsPFXv6IfName_Type.__name__=_E
_FsPFXv6IfName_Object=MibTableColumn
fsPFXv6IfName=_FsPFXv6IfName_Object((1,3,6,1,4,1,52642,1,1,10,2,134,1,2,1,2),_FsPFXv6IfName_Type())
fsPFXv6IfName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPFXv6IfName.setStatus(_A)
_FsPFXv6IfTotal_Type=Integer32
_FsPFXv6IfTotal_Object=MibTableColumn
fsPFXv6IfTotal=_FsPFXv6IfTotal_Object((1,3,6,1,4,1,52642,1,1,10,2,134,1,2,1,3),_FsPFXv6IfTotal_Type())
fsPFXv6IfTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPFXv6IfTotal.setStatus(_A)
_FsPFXv6IfRejects_Type=Integer32
_FsPFXv6IfRejects_Object=MibTableColumn
fsPFXv6IfRejects=_FsPFXv6IfRejects_Object((1,3,6,1,4,1,52642,1,1,10,2,134,1,2,1,4),_FsPFXv6IfRejects_Type())
fsPFXv6IfRejects.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPFXv6IfRejects.setStatus(_A)
_FsPFXv6IfAccepts_Type=Integer32
_FsPFXv6IfAccepts_Object=MibTableColumn
fsPFXv6IfAccepts=_FsPFXv6IfAccepts_Object((1,3,6,1,4,1,52642,1,1,10,2,134,1,2,1,5),_FsPFXv6IfAccepts_Type())
fsPFXv6IfAccepts.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPFXv6IfAccepts.setStatus(_A)
_FsPFXv6IfFrees_Type=Integer32
_FsPFXv6IfFrees_Object=MibTableColumn
fsPFXv6IfFrees=_FsPFXv6IfFrees_Object((1,3,6,1,4,1,52642,1,1,10,2,134,1,2,1,6),_FsPFXv6IfFrees_Type())
fsPFXv6IfFrees.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPFXv6IfFrees.setStatus(_A)
class _FsPFXv6IfUserate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_FsPFXv6IfUserate_Type.__name__=_D
_FsPFXv6IfUserate_Object=MibTableColumn
fsPFXv6IfUserate=_FsPFXv6IfUserate_Object((1,3,6,1,4,1,52642,1,1,10,2,134,1,2,1,7),_FsPFXv6IfUserate_Type())
fsPFXv6IfUserate.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPFXv6IfUserate.setStatus(_A)
_FsSlaacRequestNumber_Type=Counter32
_FsSlaacRequestNumber_Object=MibScalar
fsSlaacRequestNumber=_FsSlaacRequestNumber_Object((1,3,6,1,4,1,52642,1,1,10,2,134,1,3),_FsSlaacRequestNumber_Type())
fsSlaacRequestNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:fsSlaacRequestNumber.setStatus(_A)
_FsSlaacRequestSuccessNumber_Type=Counter32
_FsSlaacRequestSuccessNumber_Object=MibScalar
fsSlaacRequestSuccessNumber=_FsSlaacRequestSuccessNumber_Object((1,3,6,1,4,1,52642,1,1,10,2,134,1,4),_FsSlaacRequestSuccessNumber_Type())
fsSlaacRequestSuccessNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:fsSlaacRequestSuccessNumber.setStatus(_A)
_FsPFXv6MIBConformance_ObjectIdentity=ObjectIdentity
fsPFXv6MIBConformance=_FsPFXv6MIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,134,2))
_FsPFXv6MIBCompliances_ObjectIdentity=ObjectIdentity
fsPFXv6MIBCompliances=_FsPFXv6MIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,134,2,1))
_FsPFXv6MIBGroups_ObjectIdentity=ObjectIdentity
fsPFXv6MIBGroups=_FsPFXv6MIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,134,2,2))
fsPFXv6MIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,134,2,2,1))
fsPFXv6MIBGroup.setObjects(*((_B,_F),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_G),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:fsPFXv6MIBGroup.setStatus(_A)
fsPFXv6MIBCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,134,2,1,1))
fsPFXv6MIBCompliance.setObjects((_B,_U))
if mibBuilder.loadTexts:fsPFXv6MIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fsPFXv6MIB':fsPFXv6MIB,'fsPFXv6MIBObjects':fsPFXv6MIBObjects,'fsPFXv6Table':fsPFXv6Table,'fsPFXv6Entry':fsPFXv6Entry,_F:fsPFXv6Name,_H:fsPFXv6Total,_I:fsPFXv6Rejects,_J:fsPFXv6Accepts,_K:fsPFXv6Frees,_L:fsPFXv6Userate,'fsPFXv6IfTable':fsPFXv6IfTable,'fsPFXv6IfEntry':fsPFXv6IfEntry,_G:fsPFXv6IfIfIndex,_M:fsPFXv6IfName,_N:fsPFXv6IfTotal,_O:fsPFXv6IfRejects,_P:fsPFXv6IfAccepts,_Q:fsPFXv6IfFrees,_R:fsPFXv6IfUserate,_S:fsSlaacRequestNumber,_T:fsSlaacRequestSuccessNumber,'fsPFXv6MIBConformance':fsPFXv6MIBConformance,'fsPFXv6MIBCompliances':fsPFXv6MIBCompliances,'fsPFXv6MIBCompliance':fsPFXv6MIBCompliance,'fsPFXv6MIBGroups':fsPFXv6MIBGroups,_U:fsPFXv6MIBGroup})