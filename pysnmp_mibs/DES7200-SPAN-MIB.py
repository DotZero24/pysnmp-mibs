_I='mySPANMIBGroup'
_H='mySPANEntryStatus'
_G='mySPANIfRole'
_F='Integer32'
_E='mySPANIfIndex'
_D='mySPANSession'
_C='read-only'
_B='DES7200-SPAN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
myMgmt,=mibBuilder.importSymbols('DES7200-SMI','myMgmt')
ConfigStatus,IfIndex,MemberMap=mibBuilder.importSymbols('DES7200-TC','ConfigStatus','IfIndex','MemberMap')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
VlanId,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanId')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
mySPANMIB=ModuleIdentity((1,3,6,1,4,1,171,10,97,2,23))
if mibBuilder.loadTexts:mySPANMIB.setRevisions(('2002-03-20 00:00',))
_MySPANMIBObjects_ObjectIdentity=ObjectIdentity
mySPANMIBObjects=_MySPANMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,23,1))
_MySPANSessionNum_Type=Integer32
_MySPANSessionNum_Object=MibScalar
mySPANSessionNum=_MySPANSessionNum_Object((1,3,6,1,4,1,171,10,97,2,23,1,1),_MySPANSessionNum_Type())
mySPANSessionNum.setMaxAccess(_C)
if mibBuilder.loadTexts:mySPANSessionNum.setStatus(_A)
_MySPANTable_Object=MibTable
mySPANTable=_MySPANTable_Object((1,3,6,1,4,1,171,10,97,2,23,1,2))
if mibBuilder.loadTexts:mySPANTable.setStatus(_A)
_MySPANEntry_Object=MibTableRow
mySPANEntry=_MySPANEntry_Object((1,3,6,1,4,1,171,10,97,2,23,1,2,1))
mySPANEntry.setIndexNames((0,_B,_D),(0,_B,_E))
if mibBuilder.loadTexts:mySPANEntry.setStatus(_A)
_MySPANSession_Type=Integer32
_MySPANSession_Object=MibTableColumn
mySPANSession=_MySPANSession_Object((1,3,6,1,4,1,171,10,97,2,23,1,2,1,1),_MySPANSession_Type())
mySPANSession.setMaxAccess(_C)
if mibBuilder.loadTexts:mySPANSession.setStatus(_A)
_MySPANIfIndex_Type=IfIndex
_MySPANIfIndex_Object=MibTableColumn
mySPANIfIndex=_MySPANIfIndex_Object((1,3,6,1,4,1,171,10,97,2,23,1,2,1,2),_MySPANIfIndex_Type())
mySPANIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:mySPANIfIndex.setStatus(_A)
class _MySPANIfRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('span-desc',1),('span-src-rx',2),('span-src-tx',3),('span-src-all',4)))
_MySPANIfRole_Type.__name__=_F
_MySPANIfRole_Object=MibTableColumn
mySPANIfRole=_MySPANIfRole_Object((1,3,6,1,4,1,171,10,97,2,23,1,2,1,3),_MySPANIfRole_Type())
mySPANIfRole.setMaxAccess('read-create')
if mibBuilder.loadTexts:mySPANIfRole.setStatus(_A)
_MySPANEntryStatus_Type=ConfigStatus
_MySPANEntryStatus_Object=MibTableColumn
mySPANEntryStatus=_MySPANEntryStatus_Object((1,3,6,1,4,1,171,10,97,2,23,1,2,1,4),_MySPANEntryStatus_Type())
mySPANEntryStatus.setMaxAccess('read-write')
if mibBuilder.loadTexts:mySPANEntryStatus.setStatus(_A)
_MySPANMIBConformance_ObjectIdentity=ObjectIdentity
mySPANMIBConformance=_MySPANMIBConformance_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,23,3))
_MySPANMIBCompliances_ObjectIdentity=ObjectIdentity
mySPANMIBCompliances=_MySPANMIBCompliances_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,23,3,1))
_MySPANMIBGroups_ObjectIdentity=ObjectIdentity
mySPANMIBGroups=_MySPANMIBGroups_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,23,3,2))
mySPANMIBGroup=ObjectGroup((1,3,6,1,4,1,171,10,97,2,23,3,2,1))
mySPANMIBGroup.setObjects(*((_B,_D),(_B,_E),(_B,_G),(_B,_H)))
if mibBuilder.loadTexts:mySPANMIBGroup.setStatus(_A)
mySPANMIBCompliance=ModuleCompliance((1,3,6,1,4,1,171,10,97,2,23,3,1,1))
mySPANMIBCompliance.setObjects((_B,_I))
if mibBuilder.loadTexts:mySPANMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'mySPANMIB':mySPANMIB,'mySPANMIBObjects':mySPANMIBObjects,'mySPANSessionNum':mySPANSessionNum,'mySPANTable':mySPANTable,'mySPANEntry':mySPANEntry,_D:mySPANSession,_E:mySPANIfIndex,_G:mySPANIfRole,_H:mySPANEntryStatus,'mySPANMIBConformance':mySPANMIBConformance,'mySPANMIBCompliances':mySPANMIBCompliances,'mySPANMIBCompliance':mySPANMIBCompliance,'mySPANMIBGroups':mySPANMIBGroups,_I:mySPANMIBGroup})