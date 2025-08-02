_R='myPtTrafficCtrlMIBGroup'
_Q='stormViolationAlarmType'
_P='myPtUnicastStormControlLevel'
_O='myPtMulticastStormControlLevel'
_N='myPtBroadcastStormControlLevel'
_M='myPtUnicastStormControlStatus'
_L='myPtMulticastStormControlStatus'
_K='myPtBroadcastStormControlStatus'
_J='myPtProtectedPortStatus'
_I='Integer32'
_H='EnabledStatus'
_G='ifIndex'
_F='IF-MIB'
_E='myPtTrafficCtrlIfIndex'
_D='Percent'
_C='read-write'
_B='DES7200-TRAFFIC-CTRL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
myMgmt,=mibBuilder.importSymbols('DES7200-SMI','myMgmt')
ConfigStatus,IfIndex,MemberMap=mibBuilder.importSymbols('DES7200-TC','ConfigStatus','IfIndex','MemberMap')
ifIndex,=mibBuilder.importSymbols(_F,_G)
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_H)
VlanId,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanId')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
myTrafficCtrlMIB=ModuleIdentity((1,3,6,1,4,1,171,10,97,2,14))
if mibBuilder.loadTexts:myTrafficCtrlMIB.setRevisions(('2002-03-20 00:00',))
class Percent(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_MyTrafficCtrlMIBObjects_ObjectIdentity=ObjectIdentity
myTrafficCtrlMIBObjects=_MyTrafficCtrlMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,14,1))
_MyPtTrafficCtrlTable_Object=MibTable
myPtTrafficCtrlTable=_MyPtTrafficCtrlTable_Object((1,3,6,1,4,1,171,10,97,2,14,1,1))
if mibBuilder.loadTexts:myPtTrafficCtrlTable.setStatus(_A)
_MyPtTrafficCtrlEntry_Object=MibTableRow
myPtTrafficCtrlEntry=_MyPtTrafficCtrlEntry_Object((1,3,6,1,4,1,171,10,97,2,14,1,1,1))
myPtTrafficCtrlEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:myPtTrafficCtrlEntry.setStatus(_A)
_MyPtTrafficCtrlIfIndex_Type=IfIndex
_MyPtTrafficCtrlIfIndex_Object=MibTableColumn
myPtTrafficCtrlIfIndex=_MyPtTrafficCtrlIfIndex_Object((1,3,6,1,4,1,171,10,97,2,14,1,1,1,1),_MyPtTrafficCtrlIfIndex_Type())
myPtTrafficCtrlIfIndex.setMaxAccess('read-only')
if mibBuilder.loadTexts:myPtTrafficCtrlIfIndex.setStatus(_A)
class _MyPtProtectedPortStatus_Type(EnabledStatus):defaultValue=2
_MyPtProtectedPortStatus_Type.__name__=_H
_MyPtProtectedPortStatus_Object=MibTableColumn
myPtProtectedPortStatus=_MyPtProtectedPortStatus_Object((1,3,6,1,4,1,171,10,97,2,14,1,1,1,2),_MyPtProtectedPortStatus_Type())
myPtProtectedPortStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:myPtProtectedPortStatus.setStatus(_A)
_MyPtBroadcastStormControlStatus_Type=EnabledStatus
_MyPtBroadcastStormControlStatus_Object=MibTableColumn
myPtBroadcastStormControlStatus=_MyPtBroadcastStormControlStatus_Object((1,3,6,1,4,1,171,10,97,2,14,1,1,1,3),_MyPtBroadcastStormControlStatus_Type())
myPtBroadcastStormControlStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:myPtBroadcastStormControlStatus.setStatus(_A)
_MyPtMulticastStormControlStatus_Type=EnabledStatus
_MyPtMulticastStormControlStatus_Object=MibTableColumn
myPtMulticastStormControlStatus=_MyPtMulticastStormControlStatus_Object((1,3,6,1,4,1,171,10,97,2,14,1,1,1,4),_MyPtMulticastStormControlStatus_Type())
myPtMulticastStormControlStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:myPtMulticastStormControlStatus.setStatus(_A)
_MyPtUnicastStormControlStatus_Type=EnabledStatus
_MyPtUnicastStormControlStatus_Object=MibTableColumn
myPtUnicastStormControlStatus=_MyPtUnicastStormControlStatus_Object((1,3,6,1,4,1,171,10,97,2,14,1,1,1,5),_MyPtUnicastStormControlStatus_Type())
myPtUnicastStormControlStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:myPtUnicastStormControlStatus.setStatus(_A)
class _MyPtBroadcastStormControlLevel_Type(Percent):defaultValue=10
_MyPtBroadcastStormControlLevel_Type.__name__=_D
_MyPtBroadcastStormControlLevel_Object=MibTableColumn
myPtBroadcastStormControlLevel=_MyPtBroadcastStormControlLevel_Object((1,3,6,1,4,1,171,10,97,2,14,1,1,1,6),_MyPtBroadcastStormControlLevel_Type())
myPtBroadcastStormControlLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:myPtBroadcastStormControlLevel.setStatus(_A)
class _MyPtMulticastStormControlLevel_Type(Percent):defaultValue=10
_MyPtMulticastStormControlLevel_Type.__name__=_D
_MyPtMulticastStormControlLevel_Object=MibTableColumn
myPtMulticastStormControlLevel=_MyPtMulticastStormControlLevel_Object((1,3,6,1,4,1,171,10,97,2,14,1,1,1,7),_MyPtMulticastStormControlLevel_Type())
myPtMulticastStormControlLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:myPtMulticastStormControlLevel.setStatus(_A)
class _MyPtUnicastStormControlLevel_Type(Percent):defaultValue=10
_MyPtUnicastStormControlLevel_Type.__name__=_D
_MyPtUnicastStormControlLevel_Object=MibTableColumn
myPtUnicastStormControlLevel=_MyPtUnicastStormControlLevel_Object((1,3,6,1,4,1,171,10,97,2,14,1,1,1,8),_MyPtUnicastStormControlLevel_Type())
myPtUnicastStormControlLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:myPtUnicastStormControlLevel.setStatus(_A)
_MyPtTrafficCtrlTraps_ObjectIdentity=ObjectIdentity
myPtTrafficCtrlTraps=_MyPtTrafficCtrlTraps_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,14,2))
class _StormViolationAlarmType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('unknown',1),('broadcast',2),('mutlicast',3),('unicast',4)))
_StormViolationAlarmType_Type.__name__=_I
_StormViolationAlarmType_Object=MibScalar
stormViolationAlarmType=_StormViolationAlarmType_Object((1,3,6,1,4,1,171,10,97,2,14,2,1),_StormViolationAlarmType_Type())
stormViolationAlarmType.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:stormViolationAlarmType.setStatus(_A)
_MyPtTrafficCtrlMIBConformance_ObjectIdentity=ObjectIdentity
myPtTrafficCtrlMIBConformance=_MyPtTrafficCtrlMIBConformance_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,14,3))
_MyPtTrafficCtrlMIBCompliances_ObjectIdentity=ObjectIdentity
myPtTrafficCtrlMIBCompliances=_MyPtTrafficCtrlMIBCompliances_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,14,3,1))
_MyPtTrafficCtrlMIBGroups_ObjectIdentity=ObjectIdentity
myPtTrafficCtrlMIBGroups=_MyPtTrafficCtrlMIBGroups_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,14,3,2))
myPtTrafficCtrlMIBGroup=ObjectGroup((1,3,6,1,4,1,171,10,97,2,14,3,2,1))
myPtTrafficCtrlMIBGroup.setObjects(*((_B,_E),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:myPtTrafficCtrlMIBGroup.setStatus(_A)
stormViolationAlarm=NotificationType((1,3,6,1,4,1,171,10,97,2,14,2,2))
stormViolationAlarm.setObjects(*((_F,_G),(_B,_Q)))
if mibBuilder.loadTexts:stormViolationAlarm.setStatus(_A)
myPtTrafficCtrlMIBCompliance=ModuleCompliance((1,3,6,1,4,1,171,10,97,2,14,3,1,1))
myPtTrafficCtrlMIBCompliance.setObjects((_B,_R))
if mibBuilder.loadTexts:myPtTrafficCtrlMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_D:Percent,'myTrafficCtrlMIB':myTrafficCtrlMIB,'myTrafficCtrlMIBObjects':myTrafficCtrlMIBObjects,'myPtTrafficCtrlTable':myPtTrafficCtrlTable,'myPtTrafficCtrlEntry':myPtTrafficCtrlEntry,_E:myPtTrafficCtrlIfIndex,_J:myPtProtectedPortStatus,_K:myPtBroadcastStormControlStatus,_L:myPtMulticastStormControlStatus,_M:myPtUnicastStormControlStatus,_N:myPtBroadcastStormControlLevel,_O:myPtMulticastStormControlLevel,_P:myPtUnicastStormControlLevel,'myPtTrafficCtrlTraps':myPtTrafficCtrlTraps,_Q:stormViolationAlarmType,'stormViolationAlarm':stormViolationAlarm,'myPtTrafficCtrlMIBConformance':myPtTrafficCtrlMIBConformance,'myPtTrafficCtrlMIBCompliances':myPtTrafficCtrlMIBCompliances,'myPtTrafficCtrlMIBCompliance':myPtTrafficCtrlMIBCompliance,'myPtTrafficCtrlMIBGroups':myPtTrafficCtrlMIBGroups,_R:myPtTrafficCtrlMIBGroup})