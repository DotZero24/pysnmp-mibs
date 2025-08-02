_K='bwAlarmGroup'
_J='alTriggerAlarm'
_I='DisplayString'
_H='alDestPort'
_G='alRemoteIpAddr'
_F='alName'
_E='alLastChange'
_D='Integer32'
_C='read-only'
_B='current'
_A='BORDERWARE-FW-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
bwProducts,=mibBuilder.importSymbols('BORDERWARE-MIB','bwProducts')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_I,'PhysAddress','TextualConvention')
bwFirewall=ModuleIdentity((1,3,6,1,4,1,8673,1,1))
if mibBuilder.loadTexts:bwFirewall.setRevisions(('2004-04-11 00:00',))
_BwFirewallConformance_ObjectIdentity=ObjectIdentity
bwFirewallConformance=_BwFirewallConformance_ObjectIdentity((1,3,6,1,4,1,8673,1,1,3))
_BwFirewallCompliances_ObjectIdentity=ObjectIdentity
bwFirewallCompliances=_BwFirewallCompliances_ObjectIdentity((1,3,6,1,4,1,8673,1,1,3,1))
_BwFirewallGroups_ObjectIdentity=ObjectIdentity
bwFirewallGroups=_BwFirewallGroups_ObjectIdentity((1,3,6,1,4,1,8673,1,1,3,2))
_BwAlarm_ObjectIdentity=ObjectIdentity
bwAlarm=_BwAlarm_ObjectIdentity((1,3,6,1,4,1,8673,1,1,100))
if mibBuilder.loadTexts:bwAlarm.setStatus(_B)
class _AlTriggerAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AlTriggerAlarm_Type.__name__=_D
_AlTriggerAlarm_Object=MibScalar
alTriggerAlarm=_AlTriggerAlarm_Object((1,3,6,1,4,1,8673,1,1,100,1),_AlTriggerAlarm_Type())
alTriggerAlarm.setMaxAccess('read-write')
if mibBuilder.loadTexts:alTriggerAlarm.setStatus(_B)
_AlLastChange_Type=DateAndTime
_AlLastChange_Object=MibScalar
alLastChange=_AlLastChange_Object((1,3,6,1,4,1,8673,1,1,100,4),_AlLastChange_Type())
alLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:alLastChange.setStatus(_B)
class _AlName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AlName_Type.__name__=_I
_AlName_Object=MibScalar
alName=_AlName_Object((1,3,6,1,4,1,8673,1,1,100,9),_AlName_Type())
alName.setMaxAccess(_C)
if mibBuilder.loadTexts:alName.setStatus(_B)
_AlRemoteIpAddr_Type=IpAddress
_AlRemoteIpAddr_Object=MibScalar
alRemoteIpAddr=_AlRemoteIpAddr_Object((1,3,6,1,4,1,8673,1,1,100,10),_AlRemoteIpAddr_Type())
alRemoteIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:alRemoteIpAddr.setStatus(_B)
class _AlDestPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AlDestPort_Type.__name__=_D
_AlDestPort_Object=MibScalar
alDestPort=_AlDestPort_Object((1,3,6,1,4,1,8673,1,1,100,15),_AlDestPort_Type())
alDestPort.setMaxAccess(_C)
if mibBuilder.loadTexts:alDestPort.setStatus(_B)
bwAlarmGroup=ObjectGroup((1,3,6,1,4,1,8673,1,1,3,2,1))
bwAlarmGroup.setObjects(*((_A,_J),(_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:bwAlarmGroup.setStatus(_B)
alAlarm=NotificationType((1,3,6,1,4,1,8673,1,1,100,50))
alAlarm.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:alAlarm.setStatus(_B)
bwFirewallCompliance=ModuleCompliance((1,3,6,1,4,1,8673,1,1,3,1,1))
bwFirewallCompliance.setObjects((_A,_K))
if mibBuilder.loadTexts:bwFirewallCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'bwFirewall':bwFirewall,'bwFirewallConformance':bwFirewallConformance,'bwFirewallCompliances':bwFirewallCompliances,'bwFirewallCompliance':bwFirewallCompliance,'bwFirewallGroups':bwFirewallGroups,_K:bwAlarmGroup,'bwAlarm':bwAlarm,_J:alTriggerAlarm,_E:alLastChange,_F:alName,_G:alRemoteIpAddr,_H:alDestPort,'alAlarm':alAlarm})