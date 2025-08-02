_X='myApMIBGroup'
_W='myApPortMemberAction'
_V='myApPortMemberApNumber'
_U='myApConfigAction'
_T='myApConfigPortMember'
_S='myApConfigCurrentPtNumber'
_R='myApConfigMaxPtNumber'
_Q='myApConfigIndex'
_P='myApFlowBanlance'
_O='myApMaxPtNumber'
_N='myApMemberAction'
_M='myApPortConfigApIndex'
_L='myApCurrentNumber'
_K='myApMaxNumber'
_J='myApPortConfigPortIndex'
_I='Integer32'
_H='myApPortMemberPortIndex'
_G='myApConfigNumber'
_F='myApIndex'
_E='read-write'
_D='obsolete'
_C='read-only'
_B='current'
_A='MY-AP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
myMgmt,=mibBuilder.importSymbols('MY-SMI','myMgmt')
ConfigStatus,IfIndex,MemberMap=mibBuilder.importSymbols('MY-TC','ConfigStatus','IfIndex','MemberMap')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
PortList,VlanId=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList','VlanId')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
myApMIB=ModuleIdentity((1,3,6,1,4,1,4881,1,1,10,2,7))
if mibBuilder.loadTexts:myApMIB.setRevisions(('2002-03-20 00:00',))
_MyApMIBObjects_ObjectIdentity=ObjectIdentity
myApMIBObjects=_MyApMIBObjects_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,7,1))
_MyApMaxNumber_Type=Integer32
_MyApMaxNumber_Object=MibScalar
myApMaxNumber=_MyApMaxNumber_Object((1,3,6,1,4,1,4881,1,1,10,2,7,1,1),_MyApMaxNumber_Type())
myApMaxNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:myApMaxNumber.setStatus(_B)
_MyApCurrentNumber_Type=Integer32
_MyApCurrentNumber_Object=MibScalar
myApCurrentNumber=_MyApCurrentNumber_Object((1,3,6,1,4,1,4881,1,1,10,2,7,1,2),_MyApCurrentNumber_Type())
myApCurrentNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:myApCurrentNumber.setStatus(_B)
_MyApPortConfigTable_Object=MibTable
myApPortConfigTable=_MyApPortConfigTable_Object((1,3,6,1,4,1,4881,1,1,10,2,7,1,3))
if mibBuilder.loadTexts:myApPortConfigTable.setStatus(_D)
_MyApPortConfigEntry_Object=MibTableRow
myApPortConfigEntry=_MyApPortConfigEntry_Object((1,3,6,1,4,1,4881,1,1,10,2,7,1,3,1))
myApPortConfigEntry.setIndexNames((0,_A,_J))
if mibBuilder.loadTexts:myApPortConfigEntry.setStatus(_D)
_MyApPortConfigPortIndex_Type=IfIndex
_MyApPortConfigPortIndex_Object=MibTableColumn
myApPortConfigPortIndex=_MyApPortConfigPortIndex_Object((1,3,6,1,4,1,4881,1,1,10,2,7,1,3,1,1),_MyApPortConfigPortIndex_Type())
myApPortConfigPortIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:myApPortConfigPortIndex.setStatus(_D)
_MyApPortConfigApIndex_Type=IfIndex
_MyApPortConfigApIndex_Object=MibTableColumn
myApPortConfigApIndex=_MyApPortConfigApIndex_Object((1,3,6,1,4,1,4881,1,1,10,2,7,1,3,1,2),_MyApPortConfigApIndex_Type())
myApPortConfigApIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:myApPortConfigApIndex.setStatus(_D)
_MyApTable_Object=MibTable
myApTable=_MyApTable_Object((1,3,6,1,4,1,4881,1,1,10,2,7,1,4))
if mibBuilder.loadTexts:myApTable.setStatus(_D)
_MyApEntry_Object=MibTableRow
myApEntry=_MyApEntry_Object((1,3,6,1,4,1,4881,1,1,10,2,7,1,4,1))
myApEntry.setIndexNames((0,_A,_F))
if mibBuilder.loadTexts:myApEntry.setStatus(_D)
_MyApIndex_Type=IfIndex
_MyApIndex_Object=MibTableColumn
myApIndex=_MyApIndex_Object((1,3,6,1,4,1,4881,1,1,10,2,7,1,4,1,1),_MyApIndex_Type())
myApIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:myApIndex.setStatus(_D)
_MyApMemberAction_Type=MemberMap
_MyApMemberAction_Object=MibTableColumn
myApMemberAction=_MyApMemberAction_Object((1,3,6,1,4,1,4881,1,1,10,2,7,1,4,1,2),_MyApMemberAction_Type())
myApMemberAction.setMaxAccess(_C)
if mibBuilder.loadTexts:myApMemberAction.setStatus(_D)
_MyApPossibleMember_Type=MemberMap
_MyApPossibleMember_Object=MibTableColumn
myApPossibleMember=_MyApPossibleMember_Object((1,3,6,1,4,1,4881,1,1,10,2,7,1,4,1,3),_MyApPossibleMember_Type())
myApPossibleMember.setMaxAccess(_C)
if mibBuilder.loadTexts:myApPossibleMember.setStatus(_D)
_MyApMaxPtNumber_Type=Integer32
_MyApMaxPtNumber_Object=MibTableColumn
myApMaxPtNumber=_MyApMaxPtNumber_Object((1,3,6,1,4,1,4881,1,1,10,2,7,1,4,1,4),_MyApMaxPtNumber_Type())
myApMaxPtNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:myApMaxPtNumber.setStatus(_D)
class _MyApFlowBanlance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('unknown',0),('source-mac',1),('destination-mac',2),('src-dest-mac',3),('source-ip',4),('destination-ip',5),('src-dest-ip',6),('src-dest-port',7)))
_MyApFlowBanlance_Type.__name__=_I
_MyApFlowBanlance_Object=MibScalar
myApFlowBanlance=_MyApFlowBanlance_Object((1,3,6,1,4,1,4881,1,1,10,2,7,1,5),_MyApFlowBanlance_Type())
myApFlowBanlance.setMaxAccess(_E)
if mibBuilder.loadTexts:myApFlowBanlance.setStatus(_B)
_MyApConfigTable_Object=MibTable
myApConfigTable=_MyApConfigTable_Object((1,3,6,1,4,1,4881,1,1,10,2,7,1,6))
if mibBuilder.loadTexts:myApConfigTable.setStatus(_B)
_MyApConfigEntry_Object=MibTableRow
myApConfigEntry=_MyApConfigEntry_Object((1,3,6,1,4,1,4881,1,1,10,2,7,1,6,1))
myApConfigEntry.setIndexNames((0,_A,_G))
if mibBuilder.loadTexts:myApConfigEntry.setStatus(_B)
_MyApConfigNumber_Type=Integer32
_MyApConfigNumber_Object=MibTableColumn
myApConfigNumber=_MyApConfigNumber_Object((1,3,6,1,4,1,4881,1,1,10,2,7,1,6,1,1),_MyApConfigNumber_Type())
myApConfigNumber.setMaxAccess('read-create')
if mibBuilder.loadTexts:myApConfigNumber.setStatus(_B)
_MyApConfigIndex_Type=IfIndex
_MyApConfigIndex_Object=MibTableColumn
myApConfigIndex=_MyApConfigIndex_Object((1,3,6,1,4,1,4881,1,1,10,2,7,1,6,1,2),_MyApConfigIndex_Type())
myApConfigIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:myApConfigIndex.setStatus(_B)
_MyApConfigMaxPtNumber_Type=Integer32
_MyApConfigMaxPtNumber_Object=MibTableColumn
myApConfigMaxPtNumber=_MyApConfigMaxPtNumber_Object((1,3,6,1,4,1,4881,1,1,10,2,7,1,6,1,3),_MyApConfigMaxPtNumber_Type())
myApConfigMaxPtNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:myApConfigMaxPtNumber.setStatus(_B)
_MyApConfigCurrentPtNumber_Type=Integer32
_MyApConfigCurrentPtNumber_Object=MibTableColumn
myApConfigCurrentPtNumber=_MyApConfigCurrentPtNumber_Object((1,3,6,1,4,1,4881,1,1,10,2,7,1,6,1,4),_MyApConfigCurrentPtNumber_Type())
myApConfigCurrentPtNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:myApConfigCurrentPtNumber.setStatus(_B)
_MyApConfigPortMember_Type=PortList
_MyApConfigPortMember_Object=MibTableColumn
myApConfigPortMember=_MyApConfigPortMember_Object((1,3,6,1,4,1,4881,1,1,10,2,7,1,6,1,5),_MyApConfigPortMember_Type())
myApConfigPortMember.setMaxAccess(_C)
if mibBuilder.loadTexts:myApConfigPortMember.setStatus(_B)
_MyApConfigAction_Type=Integer32
_MyApConfigAction_Object=MibTableColumn
myApConfigAction=_MyApConfigAction_Object((1,3,6,1,4,1,4881,1,1,10,2,7,1,6,1,6),_MyApConfigAction_Type())
myApConfigAction.setMaxAccess(_E)
if mibBuilder.loadTexts:myApConfigAction.setStatus(_B)
_MyApPortMemberTable_Object=MibTable
myApPortMemberTable=_MyApPortMemberTable_Object((1,3,6,1,4,1,4881,1,1,10,2,7,1,7))
if mibBuilder.loadTexts:myApPortMemberTable.setStatus(_B)
_MyApPortMemberEntry_Object=MibTableRow
myApPortMemberEntry=_MyApPortMemberEntry_Object((1,3,6,1,4,1,4881,1,1,10,2,7,1,7,1))
myApPortMemberEntry.setIndexNames((0,_A,_H))
if mibBuilder.loadTexts:myApPortMemberEntry.setStatus(_B)
_MyApPortMemberPortIndex_Type=IfIndex
_MyApPortMemberPortIndex_Object=MibTableColumn
myApPortMemberPortIndex=_MyApPortMemberPortIndex_Object((1,3,6,1,4,1,4881,1,1,10,2,7,1,7,1,1),_MyApPortMemberPortIndex_Type())
myApPortMemberPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:myApPortMemberPortIndex.setStatus(_B)
_MyApPortMemberApNumber_Type=Integer32
_MyApPortMemberApNumber_Object=MibTableColumn
myApPortMemberApNumber=_MyApPortMemberApNumber_Object((1,3,6,1,4,1,4881,1,1,10,2,7,1,7,1,2),_MyApPortMemberApNumber_Type())
myApPortMemberApNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:myApPortMemberApNumber.setStatus(_B)
_MyApPortMemberAction_Type=Integer32
_MyApPortMemberAction_Object=MibTableColumn
myApPortMemberAction=_MyApPortMemberAction_Object((1,3,6,1,4,1,4881,1,1,10,2,7,1,7,1,3),_MyApPortMemberAction_Type())
myApPortMemberAction.setMaxAccess(_E)
if mibBuilder.loadTexts:myApPortMemberAction.setStatus(_B)
_MyApMIBConformance_ObjectIdentity=ObjectIdentity
myApMIBConformance=_MyApMIBConformance_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,7,2))
_MyApMIBCompliances_ObjectIdentity=ObjectIdentity
myApMIBCompliances=_MyApMIBCompliances_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,7,2,1))
_MyApMIBGroups_ObjectIdentity=ObjectIdentity
myApMIBGroups=_MyApMIBGroups_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,7,2,2))
myApMIBGroup=ObjectGroup((1,3,6,1,4,1,4881,1,1,10,2,7,2,2,1))
myApMIBGroup.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_F),(_A,_N),(_A,_O),(_A,_P),(_A,_G),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_H),(_A,_V),(_A,_W)))
if mibBuilder.loadTexts:myApMIBGroup.setStatus(_B)
myApMIBCompliance=ModuleCompliance((1,3,6,1,4,1,4881,1,1,10,2,7,2,1,1))
myApMIBCompliance.setObjects((_A,_X))
if mibBuilder.loadTexts:myApMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'myApMIB':myApMIB,'myApMIBObjects':myApMIBObjects,_K:myApMaxNumber,_L:myApCurrentNumber,'myApPortConfigTable':myApPortConfigTable,'myApPortConfigEntry':myApPortConfigEntry,_J:myApPortConfigPortIndex,_M:myApPortConfigApIndex,'myApTable':myApTable,'myApEntry':myApEntry,_F:myApIndex,_N:myApMemberAction,'myApPossibleMember':myApPossibleMember,_O:myApMaxPtNumber,_P:myApFlowBanlance,'myApConfigTable':myApConfigTable,'myApConfigEntry':myApConfigEntry,_G:myApConfigNumber,_Q:myApConfigIndex,_R:myApConfigMaxPtNumber,_S:myApConfigCurrentPtNumber,_T:myApConfigPortMember,_U:myApConfigAction,'myApPortMemberTable':myApPortMemberTable,'myApPortMemberEntry':myApPortMemberEntry,_H:myApPortMemberPortIndex,_V:myApPortMemberApNumber,_W:myApPortMemberAction,'myApMIBConformance':myApMIBConformance,'myApMIBCompliances':myApMIBCompliances,'myApMIBCompliance':myApMIBCompliance,'myApMIBGroups':myApMIBGroups,_X:myApMIBGroup})