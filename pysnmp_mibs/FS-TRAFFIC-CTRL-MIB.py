_R='fsPtTrafficCtrlMIBGroup'
_Q='stormViolationAlarmType'
_P='fsPtUnicastStormControlLevel'
_O='fsPtMulticastStormControlLevel'
_N='fsPtBroadcastStormControlLevel'
_M='fsPtUnicastStormControlStatus'
_L='fsPtMulticastStormControlStatus'
_K='fsPtBroadcastStormControlStatus'
_J='fsPtProtectedPortStatus'
_I='Integer32'
_H='EnabledStatus'
_G='ifIndex'
_F='IF-MIB'
_E='fsPtTrafficCtrlIfIndex'
_D='Percent'
_C='read-write'
_B='FS-TRAFFIC-CTRL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
IfIndex,=mibBuilder.importSymbols('FS-TC','IfIndex')
ifIndex,=mibBuilder.importSymbols(_F,_G)
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
fsTrafficCtrlMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,14))
if mibBuilder.loadTexts:fsTrafficCtrlMIB.setRevisions(('2002-03-20 00:00',))
class Percent(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_FsTrafficCtrlMIBObjects_ObjectIdentity=ObjectIdentity
fsTrafficCtrlMIBObjects=_FsTrafficCtrlMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,14,1))
_FsPtTrafficCtrlTable_Object=MibTable
fsPtTrafficCtrlTable=_FsPtTrafficCtrlTable_Object((1,3,6,1,4,1,52642,1,1,10,2,14,1,1))
if mibBuilder.loadTexts:fsPtTrafficCtrlTable.setStatus(_A)
_FsPtTrafficCtrlEntry_Object=MibTableRow
fsPtTrafficCtrlEntry=_FsPtTrafficCtrlEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,14,1,1,1))
fsPtTrafficCtrlEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:fsPtTrafficCtrlEntry.setStatus(_A)
_FsPtTrafficCtrlIfIndex_Type=IfIndex
_FsPtTrafficCtrlIfIndex_Object=MibTableColumn
fsPtTrafficCtrlIfIndex=_FsPtTrafficCtrlIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,14,1,1,1,1),_FsPtTrafficCtrlIfIndex_Type())
fsPtTrafficCtrlIfIndex.setMaxAccess('read-only')
if mibBuilder.loadTexts:fsPtTrafficCtrlIfIndex.setStatus(_A)
class _FsPtProtectedPortStatus_Type(EnabledStatus):defaultValue=2
_FsPtProtectedPortStatus_Type.__name__=_H
_FsPtProtectedPortStatus_Object=MibTableColumn
fsPtProtectedPortStatus=_FsPtProtectedPortStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,14,1,1,1,2),_FsPtProtectedPortStatus_Type())
fsPtProtectedPortStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPtProtectedPortStatus.setStatus(_A)
_FsPtBroadcastStormControlStatus_Type=EnabledStatus
_FsPtBroadcastStormControlStatus_Object=MibTableColumn
fsPtBroadcastStormControlStatus=_FsPtBroadcastStormControlStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,14,1,1,1,3),_FsPtBroadcastStormControlStatus_Type())
fsPtBroadcastStormControlStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPtBroadcastStormControlStatus.setStatus(_A)
_FsPtMulticastStormControlStatus_Type=EnabledStatus
_FsPtMulticastStormControlStatus_Object=MibTableColumn
fsPtMulticastStormControlStatus=_FsPtMulticastStormControlStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,14,1,1,1,4),_FsPtMulticastStormControlStatus_Type())
fsPtMulticastStormControlStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPtMulticastStormControlStatus.setStatus(_A)
_FsPtUnicastStormControlStatus_Type=EnabledStatus
_FsPtUnicastStormControlStatus_Object=MibTableColumn
fsPtUnicastStormControlStatus=_FsPtUnicastStormControlStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,14,1,1,1,5),_FsPtUnicastStormControlStatus_Type())
fsPtUnicastStormControlStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPtUnicastStormControlStatus.setStatus(_A)
class _FsPtBroadcastStormControlLevel_Type(Percent):defaultValue=10
_FsPtBroadcastStormControlLevel_Type.__name__=_D
_FsPtBroadcastStormControlLevel_Object=MibTableColumn
fsPtBroadcastStormControlLevel=_FsPtBroadcastStormControlLevel_Object((1,3,6,1,4,1,52642,1,1,10,2,14,1,1,1,6),_FsPtBroadcastStormControlLevel_Type())
fsPtBroadcastStormControlLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPtBroadcastStormControlLevel.setStatus(_A)
class _FsPtMulticastStormControlLevel_Type(Percent):defaultValue=10
_FsPtMulticastStormControlLevel_Type.__name__=_D
_FsPtMulticastStormControlLevel_Object=MibTableColumn
fsPtMulticastStormControlLevel=_FsPtMulticastStormControlLevel_Object((1,3,6,1,4,1,52642,1,1,10,2,14,1,1,1,7),_FsPtMulticastStormControlLevel_Type())
fsPtMulticastStormControlLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPtMulticastStormControlLevel.setStatus(_A)
class _FsPtUnicastStormControlLevel_Type(Percent):defaultValue=10
_FsPtUnicastStormControlLevel_Type.__name__=_D
_FsPtUnicastStormControlLevel_Object=MibTableColumn
fsPtUnicastStormControlLevel=_FsPtUnicastStormControlLevel_Object((1,3,6,1,4,1,52642,1,1,10,2,14,1,1,1,8),_FsPtUnicastStormControlLevel_Type())
fsPtUnicastStormControlLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPtUnicastStormControlLevel.setStatus(_A)
_FsPtTrafficCtrlTraps_ObjectIdentity=ObjectIdentity
fsPtTrafficCtrlTraps=_FsPtTrafficCtrlTraps_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,14,2))
class _StormViolationAlarmType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('unknown',1),('broadcast',2),('mutlicast',3),('unicast',4)))
_StormViolationAlarmType_Type.__name__=_I
_StormViolationAlarmType_Object=MibScalar
stormViolationAlarmType=_StormViolationAlarmType_Object((1,3,6,1,4,1,52642,1,1,10,2,14,2,1),_StormViolationAlarmType_Type())
stormViolationAlarmType.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:stormViolationAlarmType.setStatus(_A)
_FsPtTrafficCtrlMIBConformance_ObjectIdentity=ObjectIdentity
fsPtTrafficCtrlMIBConformance=_FsPtTrafficCtrlMIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,14,3))
_FsPtTrafficCtrlMIBCompliances_ObjectIdentity=ObjectIdentity
fsPtTrafficCtrlMIBCompliances=_FsPtTrafficCtrlMIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,14,3,1))
_FsPtTrafficCtrlMIBGroups_ObjectIdentity=ObjectIdentity
fsPtTrafficCtrlMIBGroups=_FsPtTrafficCtrlMIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,14,3,2))
fsPtTrafficCtrlMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,14,3,2,1))
fsPtTrafficCtrlMIBGroup.setObjects(*((_B,_E),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:fsPtTrafficCtrlMIBGroup.setStatus(_A)
stormViolationAlarm=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,14,2,2))
stormViolationAlarm.setObjects(*((_F,_G),(_B,_Q)))
if mibBuilder.loadTexts:stormViolationAlarm.setStatus(_A)
fsPtTrafficCtrlMIBCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,14,3,1,1))
fsPtTrafficCtrlMIBCompliance.setObjects((_B,_R))
if mibBuilder.loadTexts:fsPtTrafficCtrlMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_D:Percent,'fsTrafficCtrlMIB':fsTrafficCtrlMIB,'fsTrafficCtrlMIBObjects':fsTrafficCtrlMIBObjects,'fsPtTrafficCtrlTable':fsPtTrafficCtrlTable,'fsPtTrafficCtrlEntry':fsPtTrafficCtrlEntry,_E:fsPtTrafficCtrlIfIndex,_J:fsPtProtectedPortStatus,_K:fsPtBroadcastStormControlStatus,_L:fsPtMulticastStormControlStatus,_M:fsPtUnicastStormControlStatus,_N:fsPtBroadcastStormControlLevel,_O:fsPtMulticastStormControlLevel,_P:fsPtUnicastStormControlLevel,'fsPtTrafficCtrlTraps':fsPtTrafficCtrlTraps,_Q:stormViolationAlarmType,'stormViolationAlarm':stormViolationAlarm,'fsPtTrafficCtrlMIBConformance':fsPtTrafficCtrlMIBConformance,'fsPtTrafficCtrlMIBCompliances':fsPtTrafficCtrlMIBCompliances,'fsPtTrafficCtrlMIBCompliance':fsPtTrafficCtrlMIBCompliance,'fsPtTrafficCtrlMIBGroups':fsPtTrafficCtrlMIBGroups,_R:fsPtTrafficCtrlMIBGroup})