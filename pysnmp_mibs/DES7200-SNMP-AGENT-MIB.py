_V='mySnmpTrapMIBGroup'
_U='myCommunityMIBGroup'
_T='myTrapAction'
_S='myTrapDstEntryStatus'
_R='myTrapDstCommunity'
_Q='myTrapDstMaxNumber'
_P='myTrapDstSendTrapClass'
_O='myCommunityStatus'
_N='myCommunityEnableIpAddrAuthen'
_M='myCommunityUserIpAddr'
_L='myCommunityWritable'
_K='myCommunityMaxNum'
_J='Community'
_I='read-create'
_H='myTrapType'
_G='myTrapDstAddr'
_F='myCommunityName'
_E='Integer32'
_D='read-only'
_C='read-write'
_B='DES7200-SNMP-AGENT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
myMgmt,=mibBuilder.importSymbols('DES7200-SMI','myMgmt')
ConfigStatus,MyTrapType=mibBuilder.importSymbols('DES7200-TC','ConfigStatus','MyTrapType')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
mySnmpAgentMIB=ModuleIdentity((1,3,6,1,4,1,171,10,97,2,5))
if mibBuilder.loadTexts:mySnmpAgentMIB.setRevisions(('2002-03-20 00:00',))
class Community(DisplayString):status=_A;subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_MySnmpAgentMIBObjects_ObjectIdentity=ObjectIdentity
mySnmpAgentMIBObjects=_MySnmpAgentMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,5,1))
_MySnmpCommunityObjects_ObjectIdentity=ObjectIdentity
mySnmpCommunityObjects=_MySnmpCommunityObjects_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,5,1,1))
_MyCommunityMaxNum_Type=Integer32
_MyCommunityMaxNum_Object=MibScalar
myCommunityMaxNum=_MyCommunityMaxNum_Object((1,3,6,1,4,1,171,10,97,2,5,1,1,1),_MyCommunityMaxNum_Type())
myCommunityMaxNum.setMaxAccess(_D)
if mibBuilder.loadTexts:myCommunityMaxNum.setStatus(_A)
_MyCommunityTable_Object=MibTable
myCommunityTable=_MyCommunityTable_Object((1,3,6,1,4,1,171,10,97,2,5,1,1,2))
if mibBuilder.loadTexts:myCommunityTable.setStatus(_A)
_MyCommunityEntry_Object=MibTableRow
myCommunityEntry=_MyCommunityEntry_Object((1,3,6,1,4,1,171,10,97,2,5,1,1,2,1))
myCommunityEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:myCommunityEntry.setStatus(_A)
_MyCommunityName_Type=Community
_MyCommunityName_Object=MibTableColumn
myCommunityName=_MyCommunityName_Object((1,3,6,1,4,1,171,10,97,2,5,1,1,2,1,1),_MyCommunityName_Type())
myCommunityName.setMaxAccess(_D)
if mibBuilder.loadTexts:myCommunityName.setStatus(_A)
class _MyCommunityWritable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('readonly',1),('writable',2)))
_MyCommunityWritable_Type.__name__=_E
_MyCommunityWritable_Object=MibTableColumn
myCommunityWritable=_MyCommunityWritable_Object((1,3,6,1,4,1,171,10,97,2,5,1,1,2,1,2),_MyCommunityWritable_Type())
myCommunityWritable.setMaxAccess(_C)
if mibBuilder.loadTexts:myCommunityWritable.setStatus(_A)
_MyCommunityUserIpAddr_Type=IpAddress
_MyCommunityUserIpAddr_Object=MibTableColumn
myCommunityUserIpAddr=_MyCommunityUserIpAddr_Object((1,3,6,1,4,1,171,10,97,2,5,1,1,2,1,3),_MyCommunityUserIpAddr_Type())
myCommunityUserIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:myCommunityUserIpAddr.setStatus(_A)
_MyCommunityEnableIpAddrAuthen_Type=EnabledStatus
_MyCommunityEnableIpAddrAuthen_Object=MibTableColumn
myCommunityEnableIpAddrAuthen=_MyCommunityEnableIpAddrAuthen_Object((1,3,6,1,4,1,171,10,97,2,5,1,1,2,1,4),_MyCommunityEnableIpAddrAuthen_Type())
myCommunityEnableIpAddrAuthen.setMaxAccess(_C)
if mibBuilder.loadTexts:myCommunityEnableIpAddrAuthen.setStatus(_A)
_MyCommunityStatus_Type=RowStatus
_MyCommunityStatus_Object=MibTableColumn
myCommunityStatus=_MyCommunityStatus_Object((1,3,6,1,4,1,171,10,97,2,5,1,1,2,1,5),_MyCommunityStatus_Type())
myCommunityStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:myCommunityStatus.setStatus(_A)
_MySnmpTrapObjects_ObjectIdentity=ObjectIdentity
mySnmpTrapObjects=_MySnmpTrapObjects_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,5,1,2))
_MyTrapDstMaxNumber_Type=Integer32
_MyTrapDstMaxNumber_Object=MibScalar
myTrapDstMaxNumber=_MyTrapDstMaxNumber_Object((1,3,6,1,4,1,171,10,97,2,5,1,2,1),_MyTrapDstMaxNumber_Type())
myTrapDstMaxNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:myTrapDstMaxNumber.setStatus(_A)
_MyTrapDstTable_Object=MibTable
myTrapDstTable=_MyTrapDstTable_Object((1,3,6,1,4,1,171,10,97,2,5,1,2,2))
if mibBuilder.loadTexts:myTrapDstTable.setStatus(_A)
_MyTrapDstEntry_Object=MibTableRow
myTrapDstEntry=_MyTrapDstEntry_Object((1,3,6,1,4,1,171,10,97,2,5,1,2,2,1))
myTrapDstEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:myTrapDstEntry.setStatus(_A)
_MyTrapDstAddr_Type=IpAddress
_MyTrapDstAddr_Object=MibTableColumn
myTrapDstAddr=_MyTrapDstAddr_Object((1,3,6,1,4,1,171,10,97,2,5,1,2,2,1,1),_MyTrapDstAddr_Type())
myTrapDstAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:myTrapDstAddr.setStatus(_A)
class _MyTrapDstCommunity_Type(Community):defaultValue=OctetString('public')
_MyTrapDstCommunity_Type.__name__=_J
_MyTrapDstCommunity_Object=MibTableColumn
myTrapDstCommunity=_MyTrapDstCommunity_Object((1,3,6,1,4,1,171,10,97,2,5,1,2,2,1,2),_MyTrapDstCommunity_Type())
myTrapDstCommunity.setMaxAccess(_C)
if mibBuilder.loadTexts:myTrapDstCommunity.setStatus(_A)
class _MyTrapDstSendTrapClass_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('snmpv1-Trap',1),('snmpv2c-Trap',2)))
_MyTrapDstSendTrapClass_Type.__name__=_E
_MyTrapDstSendTrapClass_Object=MibTableColumn
myTrapDstSendTrapClass=_MyTrapDstSendTrapClass_Object((1,3,6,1,4,1,171,10,97,2,5,1,2,2,1,3),_MyTrapDstSendTrapClass_Type())
myTrapDstSendTrapClass.setMaxAccess(_C)
if mibBuilder.loadTexts:myTrapDstSendTrapClass.setStatus(_A)
_MyTrapDstEntryStatus_Type=RowStatus
_MyTrapDstEntryStatus_Object=MibTableColumn
myTrapDstEntryStatus=_MyTrapDstEntryStatus_Object((1,3,6,1,4,1,171,10,97,2,5,1,2,2,1,4),_MyTrapDstEntryStatus_Type())
myTrapDstEntryStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:myTrapDstEntryStatus.setStatus(_A)
_MyTrapActionTable_Object=MibTable
myTrapActionTable=_MyTrapActionTable_Object((1,3,6,1,4,1,171,10,97,2,5,1,2,3))
if mibBuilder.loadTexts:myTrapActionTable.setStatus(_A)
_MyTrapActionEntry_Object=MibTableRow
myTrapActionEntry=_MyTrapActionEntry_Object((1,3,6,1,4,1,171,10,97,2,5,1,2,3,1))
myTrapActionEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:myTrapActionEntry.setStatus(_A)
_MyTrapType_Type=MyTrapType
_MyTrapType_Object=MibTableColumn
myTrapType=_MyTrapType_Object((1,3,6,1,4,1,171,10,97,2,5,1,2,3,1,1),_MyTrapType_Type())
myTrapType.setMaxAccess(_D)
if mibBuilder.loadTexts:myTrapType.setStatus(_A)
class _MyTrapAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('none',1),('sendtrap',2)))
_MyTrapAction_Type.__name__=_E
_MyTrapAction_Object=MibTableColumn
myTrapAction=_MyTrapAction_Object((1,3,6,1,4,1,171,10,97,2,5,1,2,3,1,2),_MyTrapAction_Type())
myTrapAction.setMaxAccess(_C)
if mibBuilder.loadTexts:myTrapAction.setStatus(_A)
_MySnmpAgentMIBConformance_ObjectIdentity=ObjectIdentity
mySnmpAgentMIBConformance=_MySnmpAgentMIBConformance_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,5,2))
_MySnmpAgentMIBCompliances_ObjectIdentity=ObjectIdentity
mySnmpAgentMIBCompliances=_MySnmpAgentMIBCompliances_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,5,2,1))
_MySnmpAgentMIBGroups_ObjectIdentity=ObjectIdentity
mySnmpAgentMIBGroups=_MySnmpAgentMIBGroups_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,5,2,2))
myCommunityMIBGroup=ObjectGroup((1,3,6,1,4,1,171,10,97,2,5,2,2,1))
myCommunityMIBGroup.setObjects(*((_B,_K),(_B,_F),(_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:myCommunityMIBGroup.setStatus(_A)
mySnmpTrapMIBGroup=ObjectGroup((1,3,6,1,4,1,171,10,97,2,5,2,2,2))
mySnmpTrapMIBGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_G),(_B,_R),(_B,_S),(_B,_H),(_B,_T)))
if mibBuilder.loadTexts:mySnmpTrapMIBGroup.setStatus(_A)
mySnmpAgentMIBCompliance=ModuleCompliance((1,3,6,1,4,1,171,10,97,2,5,2,1,1))
mySnmpAgentMIBCompliance.setObjects(*((_B,_U),(_B,_V)))
if mibBuilder.loadTexts:mySnmpAgentMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_J:Community,'mySnmpAgentMIB':mySnmpAgentMIB,'mySnmpAgentMIBObjects':mySnmpAgentMIBObjects,'mySnmpCommunityObjects':mySnmpCommunityObjects,_K:myCommunityMaxNum,'myCommunityTable':myCommunityTable,'myCommunityEntry':myCommunityEntry,_F:myCommunityName,_L:myCommunityWritable,_M:myCommunityUserIpAddr,_N:myCommunityEnableIpAddrAuthen,_O:myCommunityStatus,'mySnmpTrapObjects':mySnmpTrapObjects,_Q:myTrapDstMaxNumber,'myTrapDstTable':myTrapDstTable,'myTrapDstEntry':myTrapDstEntry,_G:myTrapDstAddr,_R:myTrapDstCommunity,_P:myTrapDstSendTrapClass,_S:myTrapDstEntryStatus,'myTrapActionTable':myTrapActionTable,'myTrapActionEntry':myTrapActionEntry,_H:myTrapType,_T:myTrapAction,'mySnmpAgentMIBConformance':mySnmpAgentMIBConformance,'mySnmpAgentMIBCompliances':mySnmpAgentMIBCompliances,'mySnmpAgentMIBCompliance':mySnmpAgentMIBCompliance,'mySnmpAgentMIBGroups':mySnmpAgentMIBGroups,_U:myCommunityMIBGroup,_V:mySnmpTrapMIBGroup})