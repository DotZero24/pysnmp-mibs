_R='qtechPtTrafficCtrlMIBGroup'
_Q='stormViolationAlarmType'
_P='qtechPtUnicastStormControlLevel'
_O='qtechPtMulticastStormControlLevel'
_N='qtechPtBroadcastStormControlLevel'
_M='qtechPtUnicastStormControlStatus'
_L='qtechPtMulticastStormControlStatus'
_K='qtechPtBroadcastStormControlStatus'
_J='qtechPtProtectedPortStatus'
_I='Integer32'
_H='EnabledStatus'
_G='ifIndex'
_F='IF-MIB'
_E='qtechPtTrafficCtrlIfIndex'
_D='Percent'
_C='read-write'
_B='QTECH-TRAFFIC-CTRL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_F,_G)
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_H)
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
IfIndex,=mibBuilder.importSymbols('QTECH-TC','IfIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
qtechTrafficCtrlMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,14))
if mibBuilder.loadTexts:qtechTrafficCtrlMIB.setRevisions(('2002-03-20 00:00',))
class Percent(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_QtechTrafficCtrlMIBObjects_ObjectIdentity=ObjectIdentity
qtechTrafficCtrlMIBObjects=_QtechTrafficCtrlMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,14,1))
_QtechPtTrafficCtrlTable_Object=MibTable
qtechPtTrafficCtrlTable=_QtechPtTrafficCtrlTable_Object((1,3,6,1,4,1,27514,1,1,10,2,14,1,1))
if mibBuilder.loadTexts:qtechPtTrafficCtrlTable.setStatus(_A)
_QtechPtTrafficCtrlEntry_Object=MibTableRow
qtechPtTrafficCtrlEntry=_QtechPtTrafficCtrlEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,14,1,1,1))
qtechPtTrafficCtrlEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:qtechPtTrafficCtrlEntry.setStatus(_A)
_QtechPtTrafficCtrlIfIndex_Type=IfIndex
_QtechPtTrafficCtrlIfIndex_Object=MibTableColumn
qtechPtTrafficCtrlIfIndex=_QtechPtTrafficCtrlIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,14,1,1,1,1),_QtechPtTrafficCtrlIfIndex_Type())
qtechPtTrafficCtrlIfIndex.setMaxAccess('read-only')
if mibBuilder.loadTexts:qtechPtTrafficCtrlIfIndex.setStatus(_A)
class _QtechPtProtectedPortStatus_Type(EnabledStatus):defaultValue=2
_QtechPtProtectedPortStatus_Type.__name__=_H
_QtechPtProtectedPortStatus_Object=MibTableColumn
qtechPtProtectedPortStatus=_QtechPtProtectedPortStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,14,1,1,1,2),_QtechPtProtectedPortStatus_Type())
qtechPtProtectedPortStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPtProtectedPortStatus.setStatus(_A)
_QtechPtBroadcastStormControlStatus_Type=EnabledStatus
_QtechPtBroadcastStormControlStatus_Object=MibTableColumn
qtechPtBroadcastStormControlStatus=_QtechPtBroadcastStormControlStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,14,1,1,1,3),_QtechPtBroadcastStormControlStatus_Type())
qtechPtBroadcastStormControlStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPtBroadcastStormControlStatus.setStatus(_A)
_QtechPtMulticastStormControlStatus_Type=EnabledStatus
_QtechPtMulticastStormControlStatus_Object=MibTableColumn
qtechPtMulticastStormControlStatus=_QtechPtMulticastStormControlStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,14,1,1,1,4),_QtechPtMulticastStormControlStatus_Type())
qtechPtMulticastStormControlStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPtMulticastStormControlStatus.setStatus(_A)
_QtechPtUnicastStormControlStatus_Type=EnabledStatus
_QtechPtUnicastStormControlStatus_Object=MibTableColumn
qtechPtUnicastStormControlStatus=_QtechPtUnicastStormControlStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,14,1,1,1,5),_QtechPtUnicastStormControlStatus_Type())
qtechPtUnicastStormControlStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPtUnicastStormControlStatus.setStatus(_A)
class _QtechPtBroadcastStormControlLevel_Type(Percent):defaultValue=10
_QtechPtBroadcastStormControlLevel_Type.__name__=_D
_QtechPtBroadcastStormControlLevel_Object=MibTableColumn
qtechPtBroadcastStormControlLevel=_QtechPtBroadcastStormControlLevel_Object((1,3,6,1,4,1,27514,1,1,10,2,14,1,1,1,6),_QtechPtBroadcastStormControlLevel_Type())
qtechPtBroadcastStormControlLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPtBroadcastStormControlLevel.setStatus(_A)
class _QtechPtMulticastStormControlLevel_Type(Percent):defaultValue=10
_QtechPtMulticastStormControlLevel_Type.__name__=_D
_QtechPtMulticastStormControlLevel_Object=MibTableColumn
qtechPtMulticastStormControlLevel=_QtechPtMulticastStormControlLevel_Object((1,3,6,1,4,1,27514,1,1,10,2,14,1,1,1,7),_QtechPtMulticastStormControlLevel_Type())
qtechPtMulticastStormControlLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPtMulticastStormControlLevel.setStatus(_A)
class _QtechPtUnicastStormControlLevel_Type(Percent):defaultValue=10
_QtechPtUnicastStormControlLevel_Type.__name__=_D
_QtechPtUnicastStormControlLevel_Object=MibTableColumn
qtechPtUnicastStormControlLevel=_QtechPtUnicastStormControlLevel_Object((1,3,6,1,4,1,27514,1,1,10,2,14,1,1,1,8),_QtechPtUnicastStormControlLevel_Type())
qtechPtUnicastStormControlLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechPtUnicastStormControlLevel.setStatus(_A)
_QtechPtTrafficCtrlTraps_ObjectIdentity=ObjectIdentity
qtechPtTrafficCtrlTraps=_QtechPtTrafficCtrlTraps_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,14,2))
class _StormViolationAlarmType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('unknown',1),('broadcast',2),('mutlicast',3),('unicast',4)))
_StormViolationAlarmType_Type.__name__=_I
_StormViolationAlarmType_Object=MibScalar
stormViolationAlarmType=_StormViolationAlarmType_Object((1,3,6,1,4,1,27514,1,1,10,2,14,2,1),_StormViolationAlarmType_Type())
stormViolationAlarmType.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:stormViolationAlarmType.setStatus(_A)
_QtechPtTrafficCtrlMIBConformance_ObjectIdentity=ObjectIdentity
qtechPtTrafficCtrlMIBConformance=_QtechPtTrafficCtrlMIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,14,3))
_QtechPtTrafficCtrlMIBCompliances_ObjectIdentity=ObjectIdentity
qtechPtTrafficCtrlMIBCompliances=_QtechPtTrafficCtrlMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,14,3,1))
_QtechPtTrafficCtrlMIBGroups_ObjectIdentity=ObjectIdentity
qtechPtTrafficCtrlMIBGroups=_QtechPtTrafficCtrlMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,14,3,2))
qtechPtTrafficCtrlMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,14,3,2,1))
qtechPtTrafficCtrlMIBGroup.setObjects(*((_B,_E),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:qtechPtTrafficCtrlMIBGroup.setStatus(_A)
stormViolationAlarm=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,14,2,2))
stormViolationAlarm.setObjects(*((_F,_G),(_B,_Q)))
if mibBuilder.loadTexts:stormViolationAlarm.setStatus(_A)
qtechPtTrafficCtrlMIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,14,3,1,1))
qtechPtTrafficCtrlMIBCompliance.setObjects((_B,_R))
if mibBuilder.loadTexts:qtechPtTrafficCtrlMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_D:Percent,'qtechTrafficCtrlMIB':qtechTrafficCtrlMIB,'qtechTrafficCtrlMIBObjects':qtechTrafficCtrlMIBObjects,'qtechPtTrafficCtrlTable':qtechPtTrafficCtrlTable,'qtechPtTrafficCtrlEntry':qtechPtTrafficCtrlEntry,_E:qtechPtTrafficCtrlIfIndex,_J:qtechPtProtectedPortStatus,_K:qtechPtBroadcastStormControlStatus,_L:qtechPtMulticastStormControlStatus,_M:qtechPtUnicastStormControlStatus,_N:qtechPtBroadcastStormControlLevel,_O:qtechPtMulticastStormControlLevel,_P:qtechPtUnicastStormControlLevel,'qtechPtTrafficCtrlTraps':qtechPtTrafficCtrlTraps,_Q:stormViolationAlarmType,'stormViolationAlarm':stormViolationAlarm,'qtechPtTrafficCtrlMIBConformance':qtechPtTrafficCtrlMIBConformance,'qtechPtTrafficCtrlMIBCompliances':qtechPtTrafficCtrlMIBCompliances,'qtechPtTrafficCtrlMIBCompliance':qtechPtTrafficCtrlMIBCompliance,'qtechPtTrafficCtrlMIBGroups':qtechPtTrafficCtrlMIBGroups,_R:qtechPtTrafficCtrlMIBGroup})