_N='endpointEpId'
_M='MX-EPADM-MIB'
_L='idleUnusable'
_K='active'
_J='shuttingDown'
_I='Unsigned32'
_H='noOp'
_G='locked'
_F='unlocked'
_E='MxEnableState'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mediatrixServices,=mibBuilder.importSymbols('MX-SMI2','mediatrixServices')
MxActivationState,MxAdvancedIpPort,MxDigitMap,MxEnableState,MxIpAddress,MxIpHostName,MxIpPort,MxIpSubnetMask=mibBuilder.importSymbols('MX-TC','MxActivationState','MxAdvancedIpPort','MxDigitMap',_E,'MxIpAddress','MxIpHostName','MxIpPort','MxIpSubnetMask')
MxFloat32,MxIpAddr,MxIpAddrMask,MxIpAddrPort,MxIpHostNamePort,MxUInt64,MxUri,MxUrl=mibBuilder.importSymbols('MX-TC2','MxFloat32','MxIpAddr','MxIpAddrMask','MxIpAddrPort','MxIpHostNamePort','MxUInt64','MxUri','MxUrl')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
epAdmMIB=ModuleIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1500))
_EpAdmMIBObjects_ObjectIdentity=ObjectIdentity
epAdmMIBObjects=_EpAdmMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1500,1))
_UnitStateGroup_ObjectIdentity=ObjectIdentity
unitStateGroup=_UnitStateGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1500,1,100))
class _UnitAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*((_F,100),(_J,200),(_G,300)))
_UnitAdminState_Type.__name__=_B
_UnitAdminState_Object=MibScalar
unitAdminState=_UnitAdminState_Object((1,3,6,1,4,1,4935,1000,100,200,100,1500,1,100,100),_UnitAdminState_Type())
unitAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:unitAdminState.setStatus(_A)
_UnitOpState_Type=MxEnableState
_UnitOpState_Object=MibScalar
unitOpState=_UnitOpState_Object((1,3,6,1,4,1,4935,1000,100,200,100,1500,1,100,200),_UnitOpState_Type())
unitOpState.setMaxAccess(_D)
if mibBuilder.loadTexts:unitOpState.setStatus(_A)
class _UnitUsageState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400)));namedValues=NamedValues(*(('idle',100),(_K,200),('busy',300),(_L,400)))
_UnitUsageState_Type.__name__=_B
_UnitUsageState_Object=MibScalar
unitUsageState=_UnitUsageState_Object((1,3,6,1,4,1,4935,1000,100,200,100,1500,1,100,300),_UnitUsageState_Type())
unitUsageState.setMaxAccess(_D)
if mibBuilder.loadTexts:unitUsageState.setStatus(_A)
_EndpointTable_Object=MibTable
endpointTable=_EndpointTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1500,1,200))
if mibBuilder.loadTexts:endpointTable.setStatus(_A)
_EndpointEntry_Object=MibTableRow
endpointEntry=_EndpointEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1500,1,200,1))
endpointEntry.setIndexNames((0,_M,_N))
if mibBuilder.loadTexts:endpointEntry.setStatus(_A)
_EndpointEpId_Type=OctetString
_EndpointEpId_Object=MibTableColumn
endpointEpId=_EndpointEpId_Object((1,3,6,1,4,1,4935,1000,100,200,100,1500,1,200,1,100),_EndpointEpId_Type())
endpointEpId.setMaxAccess(_D)
if mibBuilder.loadTexts:endpointEpId.setStatus(_A)
class _EndpointInitialAdminStateConfig_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*((_F,100),(_G,200)))
_EndpointInitialAdminStateConfig_Type.__name__=_B
_EndpointInitialAdminStateConfig_Object=MibTableColumn
endpointInitialAdminStateConfig=_EndpointInitialAdminStateConfig_Object((1,3,6,1,4,1,4935,1000,100,200,100,1500,1,200,1,200),_EndpointInitialAdminStateConfig_Type())
endpointInitialAdminStateConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:endpointInitialAdminStateConfig.setStatus(_A)
class _EndpointAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*((_F,100),(_J,200),(_G,300)))
_EndpointAdminState_Type.__name__=_B
_EndpointAdminState_Object=MibTableColumn
endpointAdminState=_EndpointAdminState_Object((1,3,6,1,4,1,4935,1000,100,200,100,1500,1,200,1,300),_EndpointAdminState_Type())
endpointAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:endpointAdminState.setStatus(_A)
_EndpointOpState_Type=MxEnableState
_EndpointOpState_Object=MibTableColumn
endpointOpState=_EndpointOpState_Object((1,3,6,1,4,1,4935,1000,100,200,100,1500,1,200,1,400),_EndpointOpState_Type())
endpointOpState.setMaxAccess(_D)
if mibBuilder.loadTexts:endpointOpState.setStatus(_A)
class _EndpointUsageState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400)));namedValues=NamedValues(*(('idle',100),(_K,200),('busy',300),(_L,400)))
_EndpointUsageState_Type.__name__=_B
_EndpointUsageState_Object=MibTableColumn
endpointUsageState=_EndpointUsageState_Object((1,3,6,1,4,1,4935,1000,100,200,100,1500,1,200,1,500),_EndpointUsageState_Type())
endpointUsageState.setMaxAccess(_D)
if mibBuilder.loadTexts:endpointUsageState.setStatus(_A)
class _EndpointUnlock_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10)));namedValues=NamedValues(*((_H,0),('unlock',10)))
_EndpointUnlock_Type.__name__=_B
_EndpointUnlock_Object=MibTableColumn
endpointUnlock=_EndpointUnlock_Object((1,3,6,1,4,1,4935,1000,100,200,100,1500,1,200,1,600),_EndpointUnlock_Type())
endpointUnlock.setMaxAccess(_C)
if mibBuilder.loadTexts:endpointUnlock.setStatus(_A)
class _EndpointLock_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10)));namedValues=NamedValues(*((_H,0),('lock',10)))
_EndpointLock_Type.__name__=_B
_EndpointLock_Object=MibTableColumn
endpointLock=_EndpointLock_Object((1,3,6,1,4,1,4935,1000,100,200,100,1500,1,200,1,700),_EndpointLock_Type())
endpointLock.setMaxAccess(_C)
if mibBuilder.loadTexts:endpointLock.setStatus(_A)
class _EndpointForceLock_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10)));namedValues=NamedValues(*((_H,0),('forceLock',10)))
_EndpointForceLock_Type.__name__=_B
_EndpointForceLock_Object=MibTableColumn
endpointForceLock=_EndpointForceLock_Object((1,3,6,1,4,1,4935,1000,100,200,100,1500,1,200,1,800),_EndpointForceLock_Type())
endpointForceLock.setMaxAccess(_C)
if mibBuilder.loadTexts:endpointForceLock.setStatus(_A)
_UnitConfigGroup_ObjectIdentity=ObjectIdentity
unitConfigGroup=_UnitConfigGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1500,1,300))
class _UnitDisabledWhenNoGatewayReadyEnable_Type(MxEnableState):defaultValue=0
_UnitDisabledWhenNoGatewayReadyEnable_Type.__name__=_E
_UnitDisabledWhenNoGatewayReadyEnable_Object=MibScalar
unitDisabledWhenNoGatewayReadyEnable=_UnitDisabledWhenNoGatewayReadyEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1500,1,300,100),_UnitDisabledWhenNoGatewayReadyEnable_Type())
unitDisabledWhenNoGatewayReadyEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:unitDisabledWhenNoGatewayReadyEnable.setStatus(_A)
class _BehaviorWhileInUnitShuttingDownState_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('blockNewCalls',100),('allowNewCalls',200)))
_BehaviorWhileInUnitShuttingDownState_Type.__name__=_B
_BehaviorWhileInUnitShuttingDownState_Object=MibScalar
behaviorWhileInUnitShuttingDownState=_BehaviorWhileInUnitShuttingDownState_Object((1,3,6,1,4,1,4935,1000,100,200,100,1500,1,300,200),_BehaviorWhileInUnitShuttingDownState_Type())
behaviorWhileInUnitShuttingDownState.setMaxAccess(_C)
if mibBuilder.loadTexts:behaviorWhileInUnitShuttingDownState.setStatus(_A)
_SipGatewayConfigGroup_ObjectIdentity=ObjectIdentity
sipGatewayConfigGroup=_SipGatewayConfigGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1500,1,350))
class _DisableSipGatewaysWhenTrunkLinesDown_Type(MxEnableState):defaultValue=0
_DisableSipGatewaysWhenTrunkLinesDown_Type.__name__=_E
_DisableSipGatewaysWhenTrunkLinesDown_Object=MibScalar
disableSipGatewaysWhenTrunkLinesDown=_DisableSipGatewaysWhenTrunkLinesDown_Object((1,3,6,1,4,1,4935,1000,100,200,100,1500,1,350,100),_DisableSipGatewaysWhenTrunkLinesDown_Type())
disableSipGatewaysWhenTrunkLinesDown.setMaxAccess(_C)
if mibBuilder.loadTexts:disableSipGatewaysWhenTrunkLinesDown.setStatus(_A)
class _DisableSipGatewaysWhenTrunkLinesDownDelay_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_DisableSipGatewaysWhenTrunkLinesDownDelay_Type.__name__=_I
_DisableSipGatewaysWhenTrunkLinesDownDelay_Object=MibScalar
disableSipGatewaysWhenTrunkLinesDownDelay=_DisableSipGatewaysWhenTrunkLinesDownDelay_Object((1,3,6,1,4,1,4935,1000,100,200,100,1500,1,350,200),_DisableSipGatewaysWhenTrunkLinesDownDelay_Type())
disableSipGatewaysWhenTrunkLinesDownDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:disableSipGatewaysWhenTrunkLinesDownDelay.setStatus(_A)
_EndpointConfigGroup_ObjectIdentity=ObjectIdentity
endpointConfigGroup=_EndpointConfigGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1500,1,400))
class _EndpointAutomaticShutdownEnable_Type(MxEnableState):defaultValue=0
_EndpointAutomaticShutdownEnable_Type.__name__=_E
_EndpointAutomaticShutdownEnable_Object=MibScalar
endpointAutomaticShutdownEnable=_EndpointAutomaticShutdownEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1500,1,400,100),_EndpointAutomaticShutdownEnable_Type())
endpointAutomaticShutdownEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:endpointAutomaticShutdownEnable.setStatus(_A)
_NotificationsGroup_ObjectIdentity=ObjectIdentity
notificationsGroup=_NotificationsGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1500,1,60010))
class _MinSeverity_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100,200,300,400,500)));namedValues=NamedValues(*(('disable',0),('debug',100),('info',200),('warning',300),('error',400),('critical',500)))
_MinSeverity_Type.__name__=_B
_MinSeverity_Object=MibScalar
minSeverity=_MinSeverity_Object((1,3,6,1,4,1,4935,1000,100,200,100,1500,1,60010,100),_MinSeverity_Type())
minSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:minSeverity.setStatus(_A)
_ConfigurationGroup_ObjectIdentity=ObjectIdentity
configurationGroup=_ConfigurationGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1500,1,60020))
class _NeedRestartInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100)));namedValues=NamedValues(*(('no',0),('yes',100)))
_NeedRestartInfo_Type.__name__=_B
_NeedRestartInfo_Object=MibScalar
needRestartInfo=_NeedRestartInfo_Object((1,3,6,1,4,1,4935,1000,100,200,100,1500,1,60020,100),_NeedRestartInfo_Type())
needRestartInfo.setMaxAccess(_D)
if mibBuilder.loadTexts:needRestartInfo.setStatus(_A)
mibBuilder.exportSymbols(_M,**{'epAdmMIB':epAdmMIB,'epAdmMIBObjects':epAdmMIBObjects,'unitStateGroup':unitStateGroup,'unitAdminState':unitAdminState,'unitOpState':unitOpState,'unitUsageState':unitUsageState,'endpointTable':endpointTable,'endpointEntry':endpointEntry,_N:endpointEpId,'endpointInitialAdminStateConfig':endpointInitialAdminStateConfig,'endpointAdminState':endpointAdminState,'endpointOpState':endpointOpState,'endpointUsageState':endpointUsageState,'endpointUnlock':endpointUnlock,'endpointLock':endpointLock,'endpointForceLock':endpointForceLock,'unitConfigGroup':unitConfigGroup,'unitDisabledWhenNoGatewayReadyEnable':unitDisabledWhenNoGatewayReadyEnable,'behaviorWhileInUnitShuttingDownState':behaviorWhileInUnitShuttingDownState,'sipGatewayConfigGroup':sipGatewayConfigGroup,'disableSipGatewaysWhenTrunkLinesDown':disableSipGatewaysWhenTrunkLinesDown,'disableSipGatewaysWhenTrunkLinesDownDelay':disableSipGatewaysWhenTrunkLinesDownDelay,'endpointConfigGroup':endpointConfigGroup,'endpointAutomaticShutdownEnable':endpointAutomaticShutdownEnable,'notificationsGroup':notificationsGroup,'minSeverity':minSeverity,'configurationGroup':configurationGroup,'needRestartInfo':needRestartInfo})