_I='NotificationType'
_H='DisplayString'
_G='disable'
_F='enable'
_E='second'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier',_I,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_I,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','TextualConvention')
_Delta_ObjectIdentity=ObjectIdentity
delta=_Delta_ObjectIdentity((1,3,6,1,4,1,2254))
_Ups_ObjectIdentity=ObjectIdentity
ups=_Ups_ObjectIdentity((1,3,6,1,4,1,2254,2))
_Shutdownagent_ObjectIdentity=ObjectIdentity
shutdownagent=_Shutdownagent_ObjectIdentity((1,3,6,1,4,1,2254,2,200))
_DagentMonitor_ObjectIdentity=ObjectIdentity
dagentMonitor=_DagentMonitor_ObjectIdentity((1,3,6,1,4,1,2254,2,200,1))
class _DagentOSVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_DagentOSVersion_Type.__name__=_H
_DagentOSVersion_Object=MibScalar
dagentOSVersion=_DagentOSVersion_Object((1,3,6,1,4,1,2254,2,200,1,1),_DagentOSVersion_Type())
dagentOSVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:dagentOSVersion.setStatus(_A)
class _DagentSoftwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_DagentSoftwareVersion_Type.__name__=_H
_DagentSoftwareVersion_Object=MibScalar
dagentSoftwareVersion=_DagentSoftwareVersion_Object((1,3,6,1,4,1,2254,2,200,1,2),_DagentSoftwareVersion_Type())
dagentSoftwareVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:dagentSoftwareVersion.setStatus(_A)
class _DagentIsOSCountdown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_DagentIsOSCountdown_Type.__name__=_C
_DagentIsOSCountdown_Object=MibScalar
dagentIsOSCountdown=_DagentIsOSCountdown_Object((1,3,6,1,4,1,2254,2,200,1,3),_DagentIsOSCountdown_Type())
dagentIsOSCountdown.setMaxAccess(_D)
if mibBuilder.loadTexts:dagentIsOSCountdown.setStatus(_A)
_DagentOSCountdown_Type=Integer32
_DagentOSCountdown_Object=MibScalar
dagentOSCountdown=_DagentOSCountdown_Object((1,3,6,1,4,1,2254,2,200,1,4),_DagentOSCountdown_Type())
dagentOSCountdown.setMaxAccess(_D)
if mibBuilder.loadTexts:dagentOSCountdown.setStatus(_A)
if mibBuilder.loadTexts:dagentOSCountdown.setUnits(_E)
class _DagentShutdownReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('none',1),('power_fail',2),('battery_low',3),('overload',4),('on_bypass',5),('smart_shutdown',6)))
_DagentShutdownReason_Type.__name__=_C
_DagentShutdownReason_Object=MibScalar
dagentShutdownReason=_DagentShutdownReason_Object((1,3,6,1,4,1,2254,2,200,1,5),_DagentShutdownReason_Type())
dagentShutdownReason.setMaxAccess(_D)
if mibBuilder.loadTexts:dagentShutdownReason.setStatus(_A)
class _DagentHostName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_DagentHostName_Type.__name__=_H
_DagentHostName_Object=MibScalar
dagentHostName=_DagentHostName_Object((1,3,6,1,4,1,2254,2,200,1,6),_DagentHostName_Type())
dagentHostName.setMaxAccess(_D)
if mibBuilder.loadTexts:dagentHostName.setStatus(_A)
_DagentConfigure_ObjectIdentity=ObjectIdentity
dagentConfigure=_DagentConfigure_ObjectIdentity((1,3,6,1,4,1,2254,2,200,2))
class _DagentSetShutdownType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('shutdown',1),('power_off',2),('hibernate',3)))
_DagentSetShutdownType_Type.__name__=_C
_DagentSetShutdownType_Object=MibScalar
dagentSetShutdownType=_DagentSetShutdownType_Object((1,3,6,1,4,1,2254,2,200,2,1),_DagentSetShutdownType_Type())
dagentSetShutdownType.setMaxAccess(_B)
if mibBuilder.loadTexts:dagentSetShutdownType.setStatus(_A)
class _DagentSetEnablePowerFail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_DagentSetEnablePowerFail_Type.__name__=_C
_DagentSetEnablePowerFail_Object=MibScalar
dagentSetEnablePowerFail=_DagentSetEnablePowerFail_Object((1,3,6,1,4,1,2254,2,200,2,2),_DagentSetEnablePowerFail_Type())
dagentSetEnablePowerFail.setMaxAccess(_B)
if mibBuilder.loadTexts:dagentSetEnablePowerFail.setStatus(_A)
_DagentSetOSDelayPowerFail_Type=Integer32
_DagentSetOSDelayPowerFail_Object=MibScalar
dagentSetOSDelayPowerFail=_DagentSetOSDelayPowerFail_Object((1,3,6,1,4,1,2254,2,200,2,3),_DagentSetOSDelayPowerFail_Type())
dagentSetOSDelayPowerFail.setMaxAccess(_B)
if mibBuilder.loadTexts:dagentSetOSDelayPowerFail.setStatus(_A)
if mibBuilder.loadTexts:dagentSetOSDelayPowerFail.setUnits(_E)
class _DagentSetEnableBatteryLow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_DagentSetEnableBatteryLow_Type.__name__=_C
_DagentSetEnableBatteryLow_Object=MibScalar
dagentSetEnableBatteryLow=_DagentSetEnableBatteryLow_Object((1,3,6,1,4,1,2254,2,200,2,4),_DagentSetEnableBatteryLow_Type())
dagentSetEnableBatteryLow.setMaxAccess(_B)
if mibBuilder.loadTexts:dagentSetEnableBatteryLow.setStatus(_A)
_DagentSetOSDelayBatteryLow_Type=Integer32
_DagentSetOSDelayBatteryLow_Object=MibScalar
dagentSetOSDelayBatteryLow=_DagentSetOSDelayBatteryLow_Object((1,3,6,1,4,1,2254,2,200,2,5),_DagentSetOSDelayBatteryLow_Type())
dagentSetOSDelayBatteryLow.setMaxAccess(_B)
if mibBuilder.loadTexts:dagentSetOSDelayBatteryLow.setStatus(_A)
if mibBuilder.loadTexts:dagentSetOSDelayBatteryLow.setUnits(_E)
class _DagentSetEnableOverload_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_DagentSetEnableOverload_Type.__name__=_C
_DagentSetEnableOverload_Object=MibScalar
dagentSetEnableOverload=_DagentSetEnableOverload_Object((1,3,6,1,4,1,2254,2,200,2,6),_DagentSetEnableOverload_Type())
dagentSetEnableOverload.setMaxAccess(_B)
if mibBuilder.loadTexts:dagentSetEnableOverload.setStatus(_A)
_DagentSetOSDelayOverload_Type=Integer32
_DagentSetOSDelayOverload_Object=MibScalar
dagentSetOSDelayOverload=_DagentSetOSDelayOverload_Object((1,3,6,1,4,1,2254,2,200,2,7),_DagentSetOSDelayOverload_Type())
dagentSetOSDelayOverload.setMaxAccess(_B)
if mibBuilder.loadTexts:dagentSetOSDelayOverload.setStatus(_A)
if mibBuilder.loadTexts:dagentSetOSDelayOverload.setUnits(_E)
class _DagentSetEnableBypass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_DagentSetEnableBypass_Type.__name__=_C
_DagentSetEnableBypass_Object=MibScalar
dagentSetEnableBypass=_DagentSetEnableBypass_Object((1,3,6,1,4,1,2254,2,200,2,8),_DagentSetEnableBypass_Type())
dagentSetEnableBypass.setMaxAccess(_B)
if mibBuilder.loadTexts:dagentSetEnableBypass.setStatus(_A)
_DagentSetOSDelayBypass_Type=Integer32
_DagentSetOSDelayBypass_Object=MibScalar
dagentSetOSDelayBypass=_DagentSetOSDelayBypass_Object((1,3,6,1,4,1,2254,2,200,2,9),_DagentSetOSDelayBypass_Type())
dagentSetOSDelayBypass.setMaxAccess(_B)
if mibBuilder.loadTexts:dagentSetOSDelayBypass.setStatus(_A)
if mibBuilder.loadTexts:dagentSetOSDelayBypass.setUnits(_E)
class _DagentSetEnableSmartShutdown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_DagentSetEnableSmartShutdown_Type.__name__=_C
_DagentSetEnableSmartShutdown_Object=MibScalar
dagentSetEnableSmartShutdown=_DagentSetEnableSmartShutdown_Object((1,3,6,1,4,1,2254,2,200,2,10),_DagentSetEnableSmartShutdown_Type())
dagentSetEnableSmartShutdown.setMaxAccess(_B)
if mibBuilder.loadTexts:dagentSetEnableSmartShutdown.setStatus(_A)
_DagentSetOSDelaySmartShutdown_Type=Integer32
_DagentSetOSDelaySmartShutdown_Object=MibScalar
dagentSetOSDelaySmartShutdown=_DagentSetOSDelaySmartShutdown_Object((1,3,6,1,4,1,2254,2,200,2,11),_DagentSetOSDelaySmartShutdown_Type())
dagentSetOSDelaySmartShutdown.setMaxAccess(_B)
if mibBuilder.loadTexts:dagentSetOSDelaySmartShutdown.setStatus(_A)
if mibBuilder.loadTexts:dagentSetOSDelaySmartShutdown.setUnits(_E)
_DagentControl_ObjectIdentity=ObjectIdentity
dagentControl=_DagentControl_ObjectIdentity((1,3,6,1,4,1,2254,2,200,3))
class _DagentCancelShutdown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('cancel',1),('resume',2)))
_DagentCancelShutdown_Type.__name__=_C
_DagentCancelShutdown_Object=MibScalar
dagentCancelShutdown=_DagentCancelShutdown_Object((1,3,6,1,4,1,2254,2,200,3,1),_DagentCancelShutdown_Type())
dagentCancelShutdown.setMaxAccess(_B)
if mibBuilder.loadTexts:dagentCancelShutdown.setStatus(_A)
mibBuilder.exportSymbols('ShutdownAgent-MIB',**{'delta':delta,'ups':ups,'shutdownagent':shutdownagent,'dagentMonitor':dagentMonitor,'dagentOSVersion':dagentOSVersion,'dagentSoftwareVersion':dagentSoftwareVersion,'dagentIsOSCountdown':dagentIsOSCountdown,'dagentOSCountdown':dagentOSCountdown,'dagentShutdownReason':dagentShutdownReason,'dagentHostName':dagentHostName,'dagentConfigure':dagentConfigure,'dagentSetShutdownType':dagentSetShutdownType,'dagentSetEnablePowerFail':dagentSetEnablePowerFail,'dagentSetOSDelayPowerFail':dagentSetOSDelayPowerFail,'dagentSetEnableBatteryLow':dagentSetEnableBatteryLow,'dagentSetOSDelayBatteryLow':dagentSetOSDelayBatteryLow,'dagentSetEnableOverload':dagentSetEnableOverload,'dagentSetOSDelayOverload':dagentSetOSDelayOverload,'dagentSetEnableBypass':dagentSetEnableBypass,'dagentSetOSDelayBypass':dagentSetOSDelayBypass,'dagentSetEnableSmartShutdown':dagentSetEnableSmartShutdown,'dagentSetOSDelaySmartShutdown':dagentSetOSDelaySmartShutdown,'dagentControl':dagentControl,'dagentCancelShutdown':dagentCancelShutdown})