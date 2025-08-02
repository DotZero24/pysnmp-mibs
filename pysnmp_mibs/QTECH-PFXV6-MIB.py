_U='qtechPFXv6MIBGroup'
_T='qtechSlaacRequestSuccessNumber'
_S='qtechSlaacRequestNumber'
_R='qtechPFXv6IfUserate'
_Q='qtechPFXv6IfFrees'
_P='qtechPFXv6IfAccepts'
_O='qtechPFXv6IfRejects'
_N='qtechPFXv6IfTotal'
_M='qtechPFXv6IfName'
_L='qtechPFXv6Userate'
_K='qtechPFXv6Frees'
_J='qtechPFXv6Accepts'
_I='qtechPFXv6Rejects'
_H='qtechPFXv6Total'
_G='qtechPFXv6IfIfIndex'
_F='qtechPFXv6Name'
_E='DisplayString'
_D='Integer32'
_C='read-only'
_B='QTECH-PFXV6-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
IfIndex,=mibBuilder.importSymbols('QTECH-TC','IfIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','RowStatus','TextualConvention')
qtechPFXv6MIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,134))
if mibBuilder.loadTexts:qtechPFXv6MIB.setRevisions(('2015-01-13 00:00',))
_QtechPFXv6MIBObjects_ObjectIdentity=ObjectIdentity
qtechPFXv6MIBObjects=_QtechPFXv6MIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,134,1))
_QtechPFXv6Table_Object=MibTable
qtechPFXv6Table=_QtechPFXv6Table_Object((1,3,6,1,4,1,27514,1,1,10,2,134,1,1))
if mibBuilder.loadTexts:qtechPFXv6Table.setStatus(_A)
_QtechPFXv6Entry_Object=MibTableRow
qtechPFXv6Entry=_QtechPFXv6Entry_Object((1,3,6,1,4,1,27514,1,1,10,2,134,1,1,1))
qtechPFXv6Entry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:qtechPFXv6Entry.setStatus(_A)
class _QtechPFXv6Name_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechPFXv6Name_Type.__name__=_E
_QtechPFXv6Name_Object=MibTableColumn
qtechPFXv6Name=_QtechPFXv6Name_Object((1,3,6,1,4,1,27514,1,1,10,2,134,1,1,1,1),_QtechPFXv6Name_Type())
qtechPFXv6Name.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPFXv6Name.setStatus(_A)
_QtechPFXv6Total_Type=Integer32
_QtechPFXv6Total_Object=MibTableColumn
qtechPFXv6Total=_QtechPFXv6Total_Object((1,3,6,1,4,1,27514,1,1,10,2,134,1,1,1,2),_QtechPFXv6Total_Type())
qtechPFXv6Total.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPFXv6Total.setStatus(_A)
_QtechPFXv6Rejects_Type=Integer32
_QtechPFXv6Rejects_Object=MibTableColumn
qtechPFXv6Rejects=_QtechPFXv6Rejects_Object((1,3,6,1,4,1,27514,1,1,10,2,134,1,1,1,3),_QtechPFXv6Rejects_Type())
qtechPFXv6Rejects.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPFXv6Rejects.setStatus(_A)
_QtechPFXv6Accepts_Type=Integer32
_QtechPFXv6Accepts_Object=MibTableColumn
qtechPFXv6Accepts=_QtechPFXv6Accepts_Object((1,3,6,1,4,1,27514,1,1,10,2,134,1,1,1,4),_QtechPFXv6Accepts_Type())
qtechPFXv6Accepts.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPFXv6Accepts.setStatus(_A)
_QtechPFXv6Frees_Type=Integer32
_QtechPFXv6Frees_Object=MibTableColumn
qtechPFXv6Frees=_QtechPFXv6Frees_Object((1,3,6,1,4,1,27514,1,1,10,2,134,1,1,1,5),_QtechPFXv6Frees_Type())
qtechPFXv6Frees.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPFXv6Frees.setStatus(_A)
class _QtechPFXv6Userate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_QtechPFXv6Userate_Type.__name__=_D
_QtechPFXv6Userate_Object=MibTableColumn
qtechPFXv6Userate=_QtechPFXv6Userate_Object((1,3,6,1,4,1,27514,1,1,10,2,134,1,1,1,6),_QtechPFXv6Userate_Type())
qtechPFXv6Userate.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPFXv6Userate.setStatus(_A)
_QtechPFXv6IfTable_Object=MibTable
qtechPFXv6IfTable=_QtechPFXv6IfTable_Object((1,3,6,1,4,1,27514,1,1,10,2,134,1,2))
if mibBuilder.loadTexts:qtechPFXv6IfTable.setStatus(_A)
_QtechPFXv6IfEntry_Object=MibTableRow
qtechPFXv6IfEntry=_QtechPFXv6IfEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,134,1,2,1))
qtechPFXv6IfEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:qtechPFXv6IfEntry.setStatus(_A)
_QtechPFXv6IfIfIndex_Type=IfIndex
_QtechPFXv6IfIfIndex_Object=MibTableColumn
qtechPFXv6IfIfIndex=_QtechPFXv6IfIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,134,1,2,1,1),_QtechPFXv6IfIfIndex_Type())
qtechPFXv6IfIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPFXv6IfIfIndex.setStatus(_A)
class _QtechPFXv6IfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechPFXv6IfName_Type.__name__=_E
_QtechPFXv6IfName_Object=MibTableColumn
qtechPFXv6IfName=_QtechPFXv6IfName_Object((1,3,6,1,4,1,27514,1,1,10,2,134,1,2,1,2),_QtechPFXv6IfName_Type())
qtechPFXv6IfName.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPFXv6IfName.setStatus(_A)
_QtechPFXv6IfTotal_Type=Integer32
_QtechPFXv6IfTotal_Object=MibTableColumn
qtechPFXv6IfTotal=_QtechPFXv6IfTotal_Object((1,3,6,1,4,1,27514,1,1,10,2,134,1,2,1,3),_QtechPFXv6IfTotal_Type())
qtechPFXv6IfTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPFXv6IfTotal.setStatus(_A)
_QtechPFXv6IfRejects_Type=Integer32
_QtechPFXv6IfRejects_Object=MibTableColumn
qtechPFXv6IfRejects=_QtechPFXv6IfRejects_Object((1,3,6,1,4,1,27514,1,1,10,2,134,1,2,1,4),_QtechPFXv6IfRejects_Type())
qtechPFXv6IfRejects.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPFXv6IfRejects.setStatus(_A)
_QtechPFXv6IfAccepts_Type=Integer32
_QtechPFXv6IfAccepts_Object=MibTableColumn
qtechPFXv6IfAccepts=_QtechPFXv6IfAccepts_Object((1,3,6,1,4,1,27514,1,1,10,2,134,1,2,1,5),_QtechPFXv6IfAccepts_Type())
qtechPFXv6IfAccepts.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPFXv6IfAccepts.setStatus(_A)
_QtechPFXv6IfFrees_Type=Integer32
_QtechPFXv6IfFrees_Object=MibTableColumn
qtechPFXv6IfFrees=_QtechPFXv6IfFrees_Object((1,3,6,1,4,1,27514,1,1,10,2,134,1,2,1,6),_QtechPFXv6IfFrees_Type())
qtechPFXv6IfFrees.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPFXv6IfFrees.setStatus(_A)
class _QtechPFXv6IfUserate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_QtechPFXv6IfUserate_Type.__name__=_D
_QtechPFXv6IfUserate_Object=MibTableColumn
qtechPFXv6IfUserate=_QtechPFXv6IfUserate_Object((1,3,6,1,4,1,27514,1,1,10,2,134,1,2,1,7),_QtechPFXv6IfUserate_Type())
qtechPFXv6IfUserate.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPFXv6IfUserate.setStatus(_A)
_QtechSlaacRequestNumber_Type=Counter32
_QtechSlaacRequestNumber_Object=MibScalar
qtechSlaacRequestNumber=_QtechSlaacRequestNumber_Object((1,3,6,1,4,1,27514,1,1,10,2,134,1,3),_QtechSlaacRequestNumber_Type())
qtechSlaacRequestNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechSlaacRequestNumber.setStatus(_A)
_QtechSlaacRequestSuccessNumber_Type=Counter32
_QtechSlaacRequestSuccessNumber_Object=MibScalar
qtechSlaacRequestSuccessNumber=_QtechSlaacRequestSuccessNumber_Object((1,3,6,1,4,1,27514,1,1,10,2,134,1,4),_QtechSlaacRequestSuccessNumber_Type())
qtechSlaacRequestSuccessNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechSlaacRequestSuccessNumber.setStatus(_A)
_QtechPFXv6MIBConformance_ObjectIdentity=ObjectIdentity
qtechPFXv6MIBConformance=_QtechPFXv6MIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,134,2))
_QtechPFXv6MIBCompliances_ObjectIdentity=ObjectIdentity
qtechPFXv6MIBCompliances=_QtechPFXv6MIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,134,2,1))
_QtechPFXv6MIBGroups_ObjectIdentity=ObjectIdentity
qtechPFXv6MIBGroups=_QtechPFXv6MIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,134,2,2))
qtechPFXv6MIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,134,2,2,1))
qtechPFXv6MIBGroup.setObjects(*((_B,_F),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_G),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:qtechPFXv6MIBGroup.setStatus(_A)
qtechPFXv6MIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,134,2,1,1))
qtechPFXv6MIBCompliance.setObjects((_B,_U))
if mibBuilder.loadTexts:qtechPFXv6MIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'qtechPFXv6MIB':qtechPFXv6MIB,'qtechPFXv6MIBObjects':qtechPFXv6MIBObjects,'qtechPFXv6Table':qtechPFXv6Table,'qtechPFXv6Entry':qtechPFXv6Entry,_F:qtechPFXv6Name,_H:qtechPFXv6Total,_I:qtechPFXv6Rejects,_J:qtechPFXv6Accepts,_K:qtechPFXv6Frees,_L:qtechPFXv6Userate,'qtechPFXv6IfTable':qtechPFXv6IfTable,'qtechPFXv6IfEntry':qtechPFXv6IfEntry,_G:qtechPFXv6IfIfIndex,_M:qtechPFXv6IfName,_N:qtechPFXv6IfTotal,_O:qtechPFXv6IfRejects,_P:qtechPFXv6IfAccepts,_Q:qtechPFXv6IfFrees,_R:qtechPFXv6IfUserate,_S:qtechSlaacRequestNumber,_T:qtechSlaacRequestSuccessNumber,'qtechPFXv6MIBConformance':qtechPFXv6MIBConformance,'qtechPFXv6MIBCompliances':qtechPFXv6MIBCompliances,'qtechPFXv6MIBCompliance':qtechPFXv6MIBCompliance,'qtechPFXv6MIBGroups':qtechPFXv6MIBGroups,_U:qtechPFXv6MIBGroup})