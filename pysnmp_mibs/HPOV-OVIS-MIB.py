_H='accessible-for-notify'
_G='hpOVISDrillDownUrl'
_F='hpOVISAlarmText'
_E='hpOVISProbeType'
_D='hpOVISProbeSystem'
_C='hpOVISTargetHost'
_B='current'
_A='HPOV-OVIS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hpOVInternetServices=ModuleIdentity((1,3,6,1,4,1,11,2,17,16))
_Hp_ObjectIdentity=ObjectIdentity
hp=_Hp_ObjectIdentity((1,3,6,1,4,1,11))
_Nm_ObjectIdentity=ObjectIdentity
nm=_Nm_ObjectIdentity((1,3,6,1,4,1,11,2))
_OpenView_ObjectIdentity=ObjectIdentity
openView=_OpenView_ObjectIdentity((1,3,6,1,4,1,11,2,17))
_HpOVISTraps_ObjectIdentity=ObjectIdentity
hpOVISTraps=_HpOVISTraps_ObjectIdentity((1,3,6,1,4,1,11,2,17,16,0))
_HpOVISTrapVars_ObjectIdentity=ObjectIdentity
hpOVISTrapVars=_HpOVISTrapVars_ObjectIdentity((1,3,6,1,4,1,11,2,17,16,2))
_HpOVISTargetHost_Type=OctetString
_HpOVISTargetHost_Object=MibScalar
hpOVISTargetHost=_HpOVISTargetHost_Object((1,3,6,1,4,1,11,2,17,16,2,1),_HpOVISTargetHost_Type())
hpOVISTargetHost.setMaxAccess(_H)
if mibBuilder.loadTexts:hpOVISTargetHost.setStatus(_B)
_HpOVISProbeSystem_Type=OctetString
_HpOVISProbeSystem_Object=MibScalar
hpOVISProbeSystem=_HpOVISProbeSystem_Object((1,3,6,1,4,1,11,2,17,16,2,2),_HpOVISProbeSystem_Type())
hpOVISProbeSystem.setMaxAccess(_H)
if mibBuilder.loadTexts:hpOVISProbeSystem.setStatus(_B)
_HpOVISProbeType_Type=OctetString
_HpOVISProbeType_Object=MibScalar
hpOVISProbeType=_HpOVISProbeType_Object((1,3,6,1,4,1,11,2,17,16,2,3),_HpOVISProbeType_Type())
hpOVISProbeType.setMaxAccess(_H)
if mibBuilder.loadTexts:hpOVISProbeType.setStatus(_B)
_HpOVISAlarmText_Type=OctetString
_HpOVISAlarmText_Object=MibScalar
hpOVISAlarmText=_HpOVISAlarmText_Object((1,3,6,1,4,1,11,2,17,16,2,4),_HpOVISAlarmText_Type())
hpOVISAlarmText.setMaxAccess(_H)
if mibBuilder.loadTexts:hpOVISAlarmText.setStatus(_B)
_HpOVISDrillDownUrl_Type=OctetString
_HpOVISDrillDownUrl_Object=MibScalar
hpOVISDrillDownUrl=_HpOVISDrillDownUrl_Object((1,3,6,1,4,1,11,2,17,16,2,5),_HpOVISDrillDownUrl_Type())
hpOVISDrillDownUrl.setMaxAccess(_H)
if mibBuilder.loadTexts:hpOVISDrillDownUrl.setStatus(_B)
hpOVISNormalAlarm=NotificationType((1,3,6,1,4,1,11,2,17,16,0,1))
hpOVISNormalAlarm.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:hpOVISNormalAlarm.setStatus(_B)
hpOVISWarningAlarm=NotificationType((1,3,6,1,4,1,11,2,17,16,0,2))
hpOVISWarningAlarm.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:hpOVISWarningAlarm.setStatus(_B)
hpOVISMinorAlarm=NotificationType((1,3,6,1,4,1,11,2,17,16,0,3))
hpOVISMinorAlarm.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:hpOVISMinorAlarm.setStatus(_B)
hpOVISMajorAlarm=NotificationType((1,3,6,1,4,1,11,2,17,16,0,4))
hpOVISMajorAlarm.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:hpOVISMajorAlarm.setStatus(_B)
hpOVISCriticalAlarm=NotificationType((1,3,6,1,4,1,11,2,17,16,0,5))
hpOVISCriticalAlarm.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:hpOVISCriticalAlarm.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'hp':hp,'nm':nm,'openView':openView,'hpOVInternetServices':hpOVInternetServices,'hpOVISTraps':hpOVISTraps,'hpOVISNormalAlarm':hpOVISNormalAlarm,'hpOVISWarningAlarm':hpOVISWarningAlarm,'hpOVISMinorAlarm':hpOVISMinorAlarm,'hpOVISMajorAlarm':hpOVISMajorAlarm,'hpOVISCriticalAlarm':hpOVISCriticalAlarm,'hpOVISTrapVars':hpOVISTrapVars,_C:hpOVISTargetHost,_D:hpOVISProbeSystem,_E:hpOVISProbeType,_F:hpOVISAlarmText,_G:hpOVISDrillDownUrl})