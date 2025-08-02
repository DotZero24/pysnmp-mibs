_Q='ciscoDot11RadarNotificationGroup'
_P='ciscoDot11RadarDetectInfoGroup'
_O='cdrDot11RadarNotifObjectGroup'
_N='ciscoDot11RadarChannelReturn'
_M='ciscoDot11RadarChannelSwitch'
_L='cdrChannelReturnNotifEnabled'
_K='cdrChannelSwitchNotifEnabled'
_J='read-write'
_I='cdrChannelReturnLastTime'
_H='cdrChannelSwitchLastTime'
_G='cdrDot11PreferFrequency'
_F='cdrDot11NewFrequency'
_E='TruthValue'
_D='Unsigned32'
_C='read-only'
_B='current'
_A='CISCO-DOT11-RADAR-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_E)
ciscoDot11RadarMIB=ModuleIdentity((1,3,6,1,4,1,9,9,627))
if mibBuilder.loadTexts:ciscoDot11RadarMIB.setRevisions(('2007-05-07 00:00',))
_CiscoDot11RadarMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoDot11RadarMIBNotifs=_CiscoDot11RadarMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,627,0))
_CiscoDot11RadarMIBObjects_ObjectIdentity=ObjectIdentity
ciscoDot11RadarMIBObjects=_CiscoDot11RadarMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,627,1))
_CdrDot11RadarNotifConfig_ObjectIdentity=ObjectIdentity
cdrDot11RadarNotifConfig=_CdrDot11RadarNotifConfig_ObjectIdentity((1,3,6,1,4,1,9,9,627,1,1))
class _CdrChannelSwitchNotifEnabled_Type(TruthValue):defaultValue=2
_CdrChannelSwitchNotifEnabled_Type.__name__=_E
_CdrChannelSwitchNotifEnabled_Object=MibScalar
cdrChannelSwitchNotifEnabled=_CdrChannelSwitchNotifEnabled_Object((1,3,6,1,4,1,9,9,627,1,1,1),_CdrChannelSwitchNotifEnabled_Type())
cdrChannelSwitchNotifEnabled.setMaxAccess(_J)
if mibBuilder.loadTexts:cdrChannelSwitchNotifEnabled.setStatus(_B)
class _CdrChannelReturnNotifEnabled_Type(TruthValue):defaultValue=2
_CdrChannelReturnNotifEnabled_Type.__name__=_E
_CdrChannelReturnNotifEnabled_Object=MibScalar
cdrChannelReturnNotifEnabled=_CdrChannelReturnNotifEnabled_Object((1,3,6,1,4,1,9,9,627,1,1,2),_CdrChannelReturnNotifEnabled_Type())
cdrChannelReturnNotifEnabled.setMaxAccess(_J)
if mibBuilder.loadTexts:cdrChannelReturnNotifEnabled.setStatus(_B)
_CdrDot11RadarDetectInfo_ObjectIdentity=ObjectIdentity
cdrDot11RadarDetectInfo=_CdrDot11RadarDetectInfo_ObjectIdentity((1,3,6,1,4,1,9,9,627,1,2))
class _CdrDot11NewFrequency_Type(Unsigned32):defaultValue=0
_CdrDot11NewFrequency_Type.__name__=_D
_CdrDot11NewFrequency_Object=MibScalar
cdrDot11NewFrequency=_CdrDot11NewFrequency_Object((1,3,6,1,4,1,9,9,627,1,2,1),_CdrDot11NewFrequency_Type())
cdrDot11NewFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:cdrDot11NewFrequency.setStatus(_B)
if mibBuilder.loadTexts:cdrDot11NewFrequency.setUnits('MHz')
class _CdrDot11PreferFrequency_Type(Unsigned32):defaultValue=0
_CdrDot11PreferFrequency_Type.__name__=_D
_CdrDot11PreferFrequency_Object=MibScalar
cdrDot11PreferFrequency=_CdrDot11PreferFrequency_Object((1,3,6,1,4,1,9,9,627,1,2,2),_CdrDot11PreferFrequency_Type())
cdrDot11PreferFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:cdrDot11PreferFrequency.setStatus(_B)
if mibBuilder.loadTexts:cdrDot11PreferFrequency.setUnits('MHz')
_CdrChannelSwitchLastTime_Type=TimeTicks
_CdrChannelSwitchLastTime_Object=MibScalar
cdrChannelSwitchLastTime=_CdrChannelSwitchLastTime_Object((1,3,6,1,4,1,9,9,627,1,2,3),_CdrChannelSwitchLastTime_Type())
cdrChannelSwitchLastTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cdrChannelSwitchLastTime.setStatus(_B)
_CdrChannelReturnLastTime_Type=TimeTicks
_CdrChannelReturnLastTime_Object=MibScalar
cdrChannelReturnLastTime=_CdrChannelReturnLastTime_Object((1,3,6,1,4,1,9,9,627,1,2,4),_CdrChannelReturnLastTime_Type())
cdrChannelReturnLastTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cdrChannelReturnLastTime.setStatus(_B)
_CiscoDot11RadarMIBConform_ObjectIdentity=ObjectIdentity
ciscoDot11RadarMIBConform=_CiscoDot11RadarMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,627,2))
_CiscoDot11RadarMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoDot11RadarMIBCompliances=_CiscoDot11RadarMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,627,2,1))
_CiscoDot11RadarMIBGroups_ObjectIdentity=ObjectIdentity
ciscoDot11RadarMIBGroups=_CiscoDot11RadarMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,627,2,2))
cdrDot11RadarNotifObjectGroup=ObjectGroup((1,3,6,1,4,1,9,9,627,2,2,1))
cdrDot11RadarNotifObjectGroup.setObjects(*((_A,_K),(_A,_L)))
if mibBuilder.loadTexts:cdrDot11RadarNotifObjectGroup.setStatus(_B)
ciscoDot11RadarDetectInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,627,2,2,2))
ciscoDot11RadarDetectInfoGroup.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:ciscoDot11RadarDetectInfoGroup.setStatus(_B)
ciscoDot11RadarChannelSwitch=NotificationType((1,3,6,1,4,1,9,9,627,0,1))
ciscoDot11RadarChannelSwitch.setObjects(*((_A,_F),(_A,_H)))
if mibBuilder.loadTexts:ciscoDot11RadarChannelSwitch.setStatus(_B)
ciscoDot11RadarChannelReturn=NotificationType((1,3,6,1,4,1,9,9,627,0,2))
ciscoDot11RadarChannelReturn.setObjects(*((_A,_G),(_A,_I)))
if mibBuilder.loadTexts:ciscoDot11RadarChannelReturn.setStatus(_B)
ciscoDot11RadarNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,627,2,2,3))
ciscoDot11RadarNotificationGroup.setObjects(*((_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ciscoDot11RadarNotificationGroup.setStatus(_B)
ciscoDot11RadarCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,627,2,1,1))
ciscoDot11RadarCompliance.setObjects(*((_A,_O),(_A,_P),(_A,_Q)))
if mibBuilder.loadTexts:ciscoDot11RadarCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoDot11RadarMIB':ciscoDot11RadarMIB,'ciscoDot11RadarMIBNotifs':ciscoDot11RadarMIBNotifs,_M:ciscoDot11RadarChannelSwitch,_N:ciscoDot11RadarChannelReturn,'ciscoDot11RadarMIBObjects':ciscoDot11RadarMIBObjects,'cdrDot11RadarNotifConfig':cdrDot11RadarNotifConfig,_K:cdrChannelSwitchNotifEnabled,_L:cdrChannelReturnNotifEnabled,'cdrDot11RadarDetectInfo':cdrDot11RadarDetectInfo,_F:cdrDot11NewFrequency,_G:cdrDot11PreferFrequency,_H:cdrChannelSwitchLastTime,_I:cdrChannelReturnLastTime,'ciscoDot11RadarMIBConform':ciscoDot11RadarMIBConform,'ciscoDot11RadarMIBCompliances':ciscoDot11RadarMIBCompliances,'ciscoDot11RadarCompliance':ciscoDot11RadarCompliance,'ciscoDot11RadarMIBGroups':ciscoDot11RadarMIBGroups,_O:cdrDot11RadarNotifObjectGroup,_P:ciscoDot11RadarDetectInfoGroup,_Q:ciscoDot11RadarNotificationGroup})