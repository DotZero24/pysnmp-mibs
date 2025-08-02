_e='ifPhysAddress'
_d='extremeVlanIfIndex'
_c='extremeVlanIfDescr'
_b='extremeSlotModuleState'
_a='extremeSlotModuleInsertedType'
_Z='extremeSlotModuleConfiguredType'
_Y='extremeCurrentTemperature'
_X='extremeEsrpTrackedIpRoutes'
_W='extremeEsrpTrackedActivePorts'
_V='extremeEsrpState'
_U='extremeEsrpNetAddress'
_T='extremeEsrpInternalActivePorts'
_S='extremeEsrpGroup'
_R='extremeEsrpActivePorts'
_Q='ifDescr'
_P='ifAlias'
_O='EXTREME-VLAN-MIB'
_N='extremeSlotNumber'
_M='extremePowerSupplyNumber'
_L='extremeFanNumber'
_K='extremeEdpPortIfIndex'
_J='extremeEdpNeighborId'
_I='extremeEdpEntryAge'
_H='IF-MIB'
_G='EXTREME-EDP-MIB'
_F='EXTREME-ESRP-MIB'
_E='EXTREME-SYSTEM-MIB'
_D='sysDescr'
_C='sysUpTime'
_B='current'
_A='SNMPv2-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
extremeEdpEntryAge,extremeEdpNeighborId,extremeEdpNeighborVlanIpAddress,extremeEdpNeighborVlanName,extremeEdpPortIfIndex=mibBuilder.importSymbols(_G,_I,_J,'extremeEdpNeighborVlanIpAddress','extremeEdpNeighborVlanName',_K)
extremeEsrpActivePorts,extremeEsrpGroup,extremeEsrpInternalActivePorts,extremeEsrpNetAddress,extremeEsrpState,extremeEsrpTrackedActivePorts,extremeEsrpTrackedIpRoutes=mibBuilder.importSymbols(_F,_R,_S,_T,_U,_V,_W,_X)
extremeCurrentTemperature,extremeFanNumber,extremePowerSupplyNumber,extremeSlotModuleConfiguredType,extremeSlotModuleInsertedType,extremeSlotModuleState,extremeSlotNumber=mibBuilder.importSymbols(_E,_Y,_L,_M,_Z,_a,_b,_N)
extremeVlanIfDescr,extremeVlanIfIndex=mibBuilder.importSymbols(_O,_c,_d)
ifAlias,ifDescr,ifPhysAddress=mibBuilder.importSymbols(_H,_P,_Q,_e)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysDescr,sysUpTime=mibBuilder.importSymbols(_A,_D,_C)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Extremenetworks_ObjectIdentity=ObjectIdentity
extremenetworks=_Extremenetworks_ObjectIdentity((1,3,6,1,4,1,1916))
_ExtremeV1Traps_ObjectIdentity=ObjectIdentity
extremeV1Traps=_ExtremeV1Traps_ObjectIdentity((1,3,6,1,4,1,1916,0))
extremeOverheat=NotificationType((1,3,6,1,4,1,1916,0,6))
extremeOverheat.setObjects(*((_A,_C),(_A,_D),(_E,_Y)))
if mibBuilder.loadTexts:extremeOverheat.setStatus(_B)
extremeFanfailed=NotificationType((1,3,6,1,4,1,1916,0,7))
extremeFanfailed.setObjects(*((_A,_C),(_A,_D),(_E,_L)))
if mibBuilder.loadTexts:extremeFanfailed.setStatus(_B)
extremeFanOK=NotificationType((1,3,6,1,4,1,1916,0,8))
extremeFanOK.setObjects(*((_A,_C),(_A,_D),(_E,_L)))
if mibBuilder.loadTexts:extremeFanOK.setStatus(_B)
extremeInvalidLoginAttempt=NotificationType((1,3,6,1,4,1,1916,0,9))
extremeInvalidLoginAttempt.setObjects(*((_A,_C),(_A,_D)))
if mibBuilder.loadTexts:extremeInvalidLoginAttempt.setStatus(_B)
extremePowerSupplyFail=NotificationType((1,3,6,1,4,1,1916,0,10))
extremePowerSupplyFail.setObjects(*((_A,_C),(_A,_D),(_E,_M)))
if mibBuilder.loadTexts:extremePowerSupplyFail.setStatus(_B)
extremePowerSupplyGood=NotificationType((1,3,6,1,4,1,1916,0,11))
extremePowerSupplyGood.setObjects(*((_A,_C),(_A,_D),(_E,_M)))
if mibBuilder.loadTexts:extremePowerSupplyGood.setStatus(_B)
extremeRpsAlarm=NotificationType((1,3,6,1,4,1,1916,0,12))
extremeRpsAlarm.setObjects(*((_A,_C),(_A,_D)))
if mibBuilder.loadTexts:extremeRpsAlarm.setStatus(_B)
extremeRpsNoAlarm=NotificationType((1,3,6,1,4,1,1916,0,13))
extremeRpsNoAlarm.setObjects(*((_A,_C),(_A,_D)))
if mibBuilder.loadTexts:extremeRpsNoAlarm.setStatus(_B)
extremeSmartTrap=NotificationType((1,3,6,1,4,1,1916,0,14))
extremeSmartTrap.setObjects(*((_A,_C),(_A,_D)))
if mibBuilder.loadTexts:extremeSmartTrap.setStatus(_B)
extremeModuleStateChanged=NotificationType((1,3,6,1,4,1,1916,0,15))
extremeModuleStateChanged.setObjects(*((_A,_C),(_E,_N),(_E,_Z),(_E,_a),(_E,_b)))
if mibBuilder.loadTexts:extremeModuleStateChanged.setStatus(_B)
extremeEsrpStateChange=NotificationType((1,3,6,1,4,1,1916,0,17))
extremeEsrpStateChange.setObjects(*((_A,_C),(_A,_D),(_O,_d),(_O,_c),(_F,_S),(_F,_V),(_F,_U),(_H,_e),(_F,_R),(_F,_T),(_F,_W),(_F,_X)))
if mibBuilder.loadTexts:extremeEsrpStateChange.setStatus(_B)
extremeSlbUnitAdded=NotificationType((1,3,6,1,4,1,1916,0,18))
if mibBuilder.loadTexts:extremeSlbUnitAdded.setStatus(_B)
extremeSlbUnitRemoved=NotificationType((1,3,6,1,4,1,1916,0,19))
if mibBuilder.loadTexts:extremeSlbUnitRemoved.setStatus(_B)
extremeEdpNeighborAdded=NotificationType((1,3,6,1,4,1,1916,0,20))
extremeEdpNeighborAdded.setObjects(*((_A,_C),(_G,_K),(_G,_J),(_G,_I),(_H,_P),(_H,_Q)))
if mibBuilder.loadTexts:extremeEdpNeighborAdded.setStatus(_B)
extremeEdpNeighborRemoved=NotificationType((1,3,6,1,4,1,1916,0,21))
extremeEdpNeighborRemoved.setObjects(*((_A,_C),(_G,_K),(_G,_J),(_G,_I),(_H,_P),(_H,_Q)))
if mibBuilder.loadTexts:extremeEdpNeighborRemoved.setStatus(_B)
extremeCpuHealthCheckFailed=NotificationType((1,3,6,1,4,1,1916,0,22))
extremeCpuHealthCheckFailed.setObjects(*((_A,_C),(_A,_D),(_E,_N)))
if mibBuilder.loadTexts:extremeCpuHealthCheckFailed.setStatus(_B)
mibBuilder.exportSymbols('EXTREME-TRAP-MIB',**{'extremenetworks':extremenetworks,'extremeV1Traps':extremeV1Traps,'extremeOverheat':extremeOverheat,'extremeFanfailed':extremeFanfailed,'extremeFanOK':extremeFanOK,'extremeInvalidLoginAttempt':extremeInvalidLoginAttempt,'extremePowerSupplyFail':extremePowerSupplyFail,'extremePowerSupplyGood':extremePowerSupplyGood,'extremeRpsAlarm':extremeRpsAlarm,'extremeRpsNoAlarm':extremeRpsNoAlarm,'extremeSmartTrap':extremeSmartTrap,'extremeModuleStateChanged':extremeModuleStateChanged,'extremeEsrpStateChange':extremeEsrpStateChange,'extremeSlbUnitAdded':extremeSlbUnitAdded,'extremeSlbUnitRemoved':extremeSlbUnitRemoved,'extremeEdpNeighborAdded':extremeEdpNeighborAdded,'extremeEdpNeighborRemoved':extremeEdpNeighborRemoved,'extremeCpuHealthCheckFailed':extremeCpuHealthCheckFailed})