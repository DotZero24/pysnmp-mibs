_F='MxEnableState'
_E='read-only'
_D='Integer32'
_C='read-write'
_B='OctetString'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_B,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mediatrixServices,=mibBuilder.importSymbols('MX-SMI2','mediatrixServices')
MxActivationState,MxAdvancedIpPort,MxDigitMap,MxEnableState,MxIpAddress,MxIpHostName,MxIpPort,MxIpSubnetMask=mibBuilder.importSymbols('MX-TC','MxActivationState','MxAdvancedIpPort','MxDigitMap',_F,'MxIpAddress','MxIpHostName','MxIpPort','MxIpSubnetMask')
MxFloat32,MxIpAddr,MxIpAddrMask,MxIpAddrPort,MxIpHostNamePort,MxUInt64,MxUri,MxUrl=mibBuilder.importSymbols('MX-TC2','MxFloat32','MxIpAddr','MxIpAddrMask','MxIpAddrPort','MxIpHostNamePort','MxUInt64','MxUri','MxUrl')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
emsMIB=ModuleIdentity((1,3,6,1,4,1,4935,1000,100,200,100,4700))
_EmsMIBObjects_ObjectIdentity=ObjectIdentity
emsMIBObjects=_EmsMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,4700,1))
_ProvisioningGroup_ObjectIdentity=ObjectIdentity
provisioningGroup=_ProvisioningGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,4700,1,100))
class _EmsProvisioningEnable_Type(MxEnableState):defaultValue=0
_EmsProvisioningEnable_Type.__name__=_F
_EmsProvisioningEnable_Object=MibScalar
emsProvisioningEnable=_EmsProvisioningEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,4700,1,100,100),_EmsProvisioningEnable_Type())
emsProvisioningEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:emsProvisioningEnable.setStatus(_A)
class _PeriodicProvisioningTimer_Type(OctetString):defaultValue=OctetString('daily');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,250))
_PeriodicProvisioningTimer_Type.__name__=_B
_PeriodicProvisioningTimer_Object=MibScalar
periodicProvisioningTimer=_PeriodicProvisioningTimer_Object((1,3,6,1,4,1,4935,1000,100,200,100,4700,1,100,200),_PeriodicProvisioningTimer_Type())
periodicProvisioningTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:periodicProvisioningTimer.setStatus(_A)
_TimersGroup_ObjectIdentity=ObjectIdentity
timersGroup=_TimersGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,4700,1,150))
class _HourlyTimeRange_Type(OctetString):defaultValue=OctetString('55 - 05');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_HourlyTimeRange_Type.__name__=_B
_HourlyTimeRange_Object=MibScalar
hourlyTimeRange=_HourlyTimeRange_Object((1,3,6,1,4,1,4935,1000,100,200,100,4700,1,150,100),_HourlyTimeRange_Type())
hourlyTimeRange.setMaxAccess(_C)
if mibBuilder.loadTexts:hourlyTimeRange.setStatus(_A)
class _DailyTimeRange_Type(OctetString):defaultValue=OctetString('01:00 - 03:00');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DailyTimeRange_Type.__name__=_B
_DailyTimeRange_Object=MibScalar
dailyTimeRange=_DailyTimeRange_Object((1,3,6,1,4,1,4935,1000,100,200,100,4700,1,150,200),_DailyTimeRange_Type())
dailyTimeRange.setMaxAccess(_C)
if mibBuilder.loadTexts:dailyTimeRange.setStatus(_A)
class _WeeklyTimeRange_Type(OctetString):defaultValue=OctetString('Monday 01:00 - Monday 03:00');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_WeeklyTimeRange_Type.__name__=_B
_WeeklyTimeRange_Object=MibScalar
weeklyTimeRange=_WeeklyTimeRange_Object((1,3,6,1,4,1,4935,1000,100,200,100,4700,1,150,300),_WeeklyTimeRange_Type())
weeklyTimeRange.setMaxAccess(_C)
if mibBuilder.loadTexts:weeklyTimeRange.setStatus(_A)
_StatusGroup_ObjectIdentity=ObjectIdentity
statusGroup=_StatusGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,4700,1,200))
class _LastConnectionDateTime_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LastConnectionDateTime_Type.__name__=_B
_LastConnectionDateTime_Object=MibScalar
lastConnectionDateTime=_LastConnectionDateTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,4700,1,200,100),_LastConnectionDateTime_Type())
lastConnectionDateTime.setMaxAccess(_E)
if mibBuilder.loadTexts:lastConnectionDateTime.setStatus(_A)
class _LastProvisioningResult_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500,600)));namedValues=NamedValues(*(('none',100),('success',200),('partiallyProvisioned',300),('connectionFailed',400),('provisioningError',500),('unmanagedUnit',600)))
_LastProvisioningResult_Type.__name__=_D
_LastProvisioningResult_Object=MibScalar
lastProvisioningResult=_LastProvisioningResult_Object((1,3,6,1,4,1,4935,1000,100,200,100,4700,1,200,200),_LastProvisioningResult_Type())
lastProvisioningResult.setMaxAccess(_E)
if mibBuilder.loadTexts:lastProvisioningResult.setStatus(_A)
_NotificationsGroup_ObjectIdentity=ObjectIdentity
notificationsGroup=_NotificationsGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,4700,1,60010))
class _MinSeverity_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100,200,300,400,500)));namedValues=NamedValues(*(('disable',0),('debug',100),('info',200),('warning',300),('error',400),('critical',500)))
_MinSeverity_Type.__name__=_D
_MinSeverity_Object=MibScalar
minSeverity=_MinSeverity_Object((1,3,6,1,4,1,4935,1000,100,200,100,4700,1,60010,100),_MinSeverity_Type())
minSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:minSeverity.setStatus(_A)
_ConfigurationGroup_ObjectIdentity=ObjectIdentity
configurationGroup=_ConfigurationGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,4700,1,60020))
class _NeedRestartInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100)));namedValues=NamedValues(*(('no',0),('yes',100)))
_NeedRestartInfo_Type.__name__=_D
_NeedRestartInfo_Object=MibScalar
needRestartInfo=_NeedRestartInfo_Object((1,3,6,1,4,1,4935,1000,100,200,100,4700,1,60020,100),_NeedRestartInfo_Type())
needRestartInfo.setMaxAccess(_E)
if mibBuilder.loadTexts:needRestartInfo.setStatus(_A)
mibBuilder.exportSymbols('MX-EMS-MIB',**{'emsMIB':emsMIB,'emsMIBObjects':emsMIBObjects,'provisioningGroup':provisioningGroup,'emsProvisioningEnable':emsProvisioningEnable,'periodicProvisioningTimer':periodicProvisioningTimer,'timersGroup':timersGroup,'hourlyTimeRange':hourlyTimeRange,'dailyTimeRange':dailyTimeRange,'weeklyTimeRange':weeklyTimeRange,'statusGroup':statusGroup,'lastConnectionDateTime':lastConnectionDateTime,'lastProvisioningResult':lastProvisioningResult,'notificationsGroup':notificationsGroup,'minSeverity':minSeverity,'configurationGroup':configurationGroup,'needRestartInfo':needRestartInfo})