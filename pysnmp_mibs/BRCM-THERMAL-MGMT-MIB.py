_H='Seconds'
_G='read-only'
_F='TruthValue'
_E='degrees C'
_D='Integer32'
_C='Unsigned32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cableDataMgmtMIBObjects,=mibBuilder.importSymbols('BRCM-CABLEDATA-MGMT-MIB','cableDataMgmtMIBObjects')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention',_F)
thermalMgmt=ModuleIdentity((1,3,6,1,4,1,4413,2,2,2,1,11))
if mibBuilder.loadTexts:thermalMgmt.setRevisions(('2007-02-05 00:00','2006-10-04 00:00'))
_ThermalMgmtBase_ObjectIdentity=ObjectIdentity
thermalMgmtBase=_ThermalMgmtBase_ObjectIdentity((1,3,6,1,4,1,4413,2,2,2,1,11,1))
_ThermalCurrentTemperature_Type=Integer32
_ThermalCurrentTemperature_Object=MibScalar
thermalCurrentTemperature=_ThermalCurrentTemperature_Object((1,3,6,1,4,1,4413,2,2,2,1,11,1,1),_ThermalCurrentTemperature_Type())
thermalCurrentTemperature.setMaxAccess(_G)
if mibBuilder.loadTexts:thermalCurrentTemperature.setStatus(_A)
if mibBuilder.loadTexts:thermalCurrentTemperature.setUnits(_E)
class _ThermalPowerOffThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(40,120))
_ThermalPowerOffThreshold_Type.__name__=_D
_ThermalPowerOffThreshold_Object=MibScalar
thermalPowerOffThreshold=_ThermalPowerOffThreshold_Object((1,3,6,1,4,1,4413,2,2,2,1,11,1,2),_ThermalPowerOffThreshold_Type())
thermalPowerOffThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:thermalPowerOffThreshold.setStatus(_A)
if mibBuilder.loadTexts:thermalPowerOffThreshold.setUnits(_E)
class _ThermalPowerOnThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(40,120))
_ThermalPowerOnThreshold_Type.__name__=_D
_ThermalPowerOnThreshold_Object=MibScalar
thermalPowerOnThreshold=_ThermalPowerOnThreshold_Object((1,3,6,1,4,1,4413,2,2,2,1,11,1,3),_ThermalPowerOnThreshold_Type())
thermalPowerOnThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:thermalPowerOnThreshold.setStatus(_A)
if mibBuilder.loadTexts:thermalPowerOnThreshold.setUnits(_E)
class _ThermalPowerOnDelay_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,50))
_ThermalPowerOnDelay_Type.__name__=_C
_ThermalPowerOnDelay_Object=MibScalar
thermalPowerOnDelay=_ThermalPowerOnDelay_Object((1,3,6,1,4,1,4413,2,2,2,1,11,1,4),_ThermalPowerOnDelay_Type())
thermalPowerOnDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:thermalPowerOnDelay.setStatus(_A)
if mibBuilder.loadTexts:thermalPowerOnDelay.setUnits('250 Milliseconds')
class _ThermalPowerOffDelay_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,60))
_ThermalPowerOffDelay_Type.__name__=_C
_ThermalPowerOffDelay_Object=MibScalar
thermalPowerOffDelay=_ThermalPowerOffDelay_Object((1,3,6,1,4,1,4413,2,2,2,1,11,1,5),_ThermalPowerOffDelay_Type())
thermalPowerOffDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:thermalPowerOffDelay.setStatus(_A)
if mibBuilder.loadTexts:thermalPowerOffDelay.setUnits(_H)
class _ThermalNotificationDelay_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,60))
_ThermalNotificationDelay_Type.__name__=_C
_ThermalNotificationDelay_Object=MibScalar
thermalNotificationDelay=_ThermalNotificationDelay_Object((1,3,6,1,4,1,4413,2,2,2,1,11,1,6),_ThermalNotificationDelay_Type())
thermalNotificationDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:thermalNotificationDelay.setStatus(_A)
if mibBuilder.loadTexts:thermalNotificationDelay.setUnits(_H)
class _ThermalMonitorInitialized_Type(TruthValue):defaultValue=2
_ThermalMonitorInitialized_Type.__name__=_F
_ThermalMonitorInitialized_Object=MibScalar
thermalMonitorInitialized=_ThermalMonitorInitialized_Object((1,3,6,1,4,1,4413,2,2,2,1,11,1,7),_ThermalMonitorInitialized_Type())
thermalMonitorInitialized.setMaxAccess(_G)
if mibBuilder.loadTexts:thermalMonitorInitialized.setStatus(_A)
mibBuilder.exportSymbols('BRCM-THERMAL-MGMT-MIB',**{'thermalMgmt':thermalMgmt,'thermalMgmtBase':thermalMgmtBase,'thermalCurrentTemperature':thermalCurrentTemperature,'thermalPowerOffThreshold':thermalPowerOffThreshold,'thermalPowerOnThreshold':thermalPowerOnThreshold,'thermalPowerOnDelay':thermalPowerOnDelay,'thermalPowerOffDelay':thermalPowerOffDelay,'thermalNotificationDelay':thermalNotificationDelay,'thermalMonitorInitialized':thermalMonitorInitialized})