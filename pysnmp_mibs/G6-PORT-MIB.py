_Z='statusPortIndex'
_Y='monitorIndex'
_X='ms1000Mbit'
_W='ms100Mbit'
_V='ms10Mbit'
_U='configPortIndex'
_T='not-accessible'
_S='dhcpFilterApplies'
_R='bpduGuardApplies'
_Q='macAuthApplies'
_P='loopPreventionApplies'
_O='couplingApplies'
_N='ringApplies'
_M='rstpApplies'
_L='ms8021xApplies'
_K='portIsEnabled'
_J='G6-PORT-MIB'
_I='Bits'
_H='true'
_G='false'
_F='enabled'
_E='disabled'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
g6,=mibBuilder.importSymbols('MICROSENS-G6-MIB','g6')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI',_I,'Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
device=ModuleIdentity((1,3,6,1,4,1,3181,10,6,1))
if mibBuilder.loadTexts:device.setRevisions(('2018-02-12 16:19',))
_Port_ObjectIdentity=ObjectIdentity
port=_Port_ObjectIdentity((1,3,6,1,4,1,3181,10,6,1,81))
_ConfigTable_Object=MibTable
configTable=_ConfigTable_Object((1,3,6,1,4,1,3181,10,6,1,81,1))
if mibBuilder.loadTexts:configTable.setStatus(_A)
_ConfigEntry_Object=MibTableRow
configEntry=_ConfigEntry_Object((1,3,6,1,4,1,3181,10,6,1,81,1,1))
configEntry.setIndexNames((0,_J,_U))
if mibBuilder.loadTexts:configEntry.setStatus(_A)
class _ConfigPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24))
_ConfigPortIndex_Type.__name__=_B
_ConfigPortIndex_Object=MibTableColumn
configPortIndex=_ConfigPortIndex_Object((1,3,6,1,4,1,3181,10,6,1,81,1,1,1),_ConfigPortIndex_Type())
configPortIndex.setMaxAccess(_T)
if mibBuilder.loadTexts:configPortIndex.setStatus(_A)
_ConfigAlias_Type=DisplayString
_ConfigAlias_Object=MibTableColumn
configAlias=_ConfigAlias_Object((1,3,6,1,4,1,3181,10,6,1,81,1,1,2),_ConfigAlias_Type())
configAlias.setMaxAccess(_D)
if mibBuilder.loadTexts:configAlias.setStatus(_A)
class _ConfigPortOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_ConfigPortOperation_Type.__name__=_B
_ConfigPortOperation_Object=MibTableColumn
configPortOperation=_ConfigPortOperation_Object((1,3,6,1,4,1,3181,10,6,1,81,1,1,3),_ConfigPortOperation_Type())
configPortOperation.setMaxAccess(_D)
if mibBuilder.loadTexts:configPortOperation.setStatus(_A)
class _ConfigRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('default',0),('local',1),('uplink',2),('downlink',3)))
_ConfigRole_Type.__name__=_B
_ConfigRole_Object=MibTableColumn
configRole=_ConfigRole_Object((1,3,6,1,4,1,3181,10,6,1,81,1,1,4),_ConfigRole_Type())
configRole.setMaxAccess(_D)
if mibBuilder.loadTexts:configRole.setStatus(_A)
class _ConfigSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_V,0),(_W,1),(_X,2),('sfpAuto',3)))
_ConfigSpeed_Type.__name__=_B
_ConfigSpeed_Object=MibTableColumn
configSpeed=_ConfigSpeed_Object((1,3,6,1,4,1,3181,10,6,1,81,1,1,5),_ConfigSpeed_Type())
configSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:configSpeed.setStatus(_A)
class _ConfigMtu_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('ms1522Byte',0),('ms2048Byte',1),('ms10240Byte',2)))
_ConfigMtu_Type.__name__=_B
_ConfigMtu_Object=MibTableColumn
configMtu=_ConfigMtu_Object((1,3,6,1,4,1,3181,10,6,1,81,1,1,6),_ConfigMtu_Type())
configMtu.setMaxAccess(_D)
if mibBuilder.loadTexts:configMtu.setStatus(_A)
class _ConfigLoopProtection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_ConfigLoopProtection_Type.__name__=_B
_ConfigLoopProtection_Object=MibTableColumn
configLoopProtection=_ConfigLoopProtection_Object((1,3,6,1,4,1,3181,10,6,1,81,1,1,7),_ConfigLoopProtection_Type())
configLoopProtection.setMaxAccess(_D)
if mibBuilder.loadTexts:configLoopProtection.setStatus(_A)
class _ConfigAutoNegotiation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_ConfigAutoNegotiation_Type.__name__=_B
_ConfigAutoNegotiation_Object=MibTableColumn
configAutoNegotiation=_ConfigAutoNegotiation_Object((1,3,6,1,4,1,3181,10,6,1,81,1,1,8),_ConfigAutoNegotiation_Type())
configAutoNegotiation.setMaxAccess(_D)
if mibBuilder.loadTexts:configAutoNegotiation.setStatus(_A)
class _ConfigFullDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_ConfigFullDuplex_Type.__name__=_B
_ConfigFullDuplex_Object=MibTableColumn
configFullDuplex=_ConfigFullDuplex_Object((1,3,6,1,4,1,3181,10,6,1,81,1,1,9),_ConfigFullDuplex_Type())
configFullDuplex.setMaxAccess(_D)
if mibBuilder.loadTexts:configFullDuplex.setStatus(_A)
class _ConfigFlowcontrol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_ConfigFlowcontrol_Type.__name__=_B
_ConfigFlowcontrol_Object=MibTableColumn
configFlowcontrol=_ConfigFlowcontrol_Object((1,3,6,1,4,1,3181,10,6,1,81,1,1,10),_ConfigFlowcontrol_Type())
configFlowcontrol.setMaxAccess(_D)
if mibBuilder.loadTexts:configFlowcontrol.setStatus(_A)
class _ConfigMdiMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('auto',0),('forceMdiStd',1),('forceMdix',2)))
_ConfigMdiMode_Type.__name__=_B
_ConfigMdiMode_Object=MibTableColumn
configMdiMode=_ConfigMdiMode_Object((1,3,6,1,4,1,3181,10,6,1,81,1,1,11),_ConfigMdiMode_Type())
configMdiMode.setMaxAccess(_D)
if mibBuilder.loadTexts:configMdiMode.setStatus(_A)
class _ConfigEnergyEfficiency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_ConfigEnergyEfficiency_Type.__name__=_B
_ConfigEnergyEfficiency_Object=MibTableColumn
configEnergyEfficiency=_ConfigEnergyEfficiency_Object((1,3,6,1,4,1,3181,10,6,1,81,1,1,12),_ConfigEnergyEfficiency_Type())
configEnergyEfficiency.setMaxAccess(_D)
if mibBuilder.loadTexts:configEnergyEfficiency.setStatus(_A)
class _ConfigDualMediaMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('fiberPriority',0),('copperPriority',1),('forceFiber',2),('forceCopper',3)))
_ConfigDualMediaMode_Type.__name__=_B
_ConfigDualMediaMode_Object=MibTableColumn
configDualMediaMode=_ConfigDualMediaMode_Object((1,3,6,1,4,1,3181,10,6,1,81,1,1,13),_ConfigDualMediaMode_Type())
configDualMediaMode.setMaxAccess(_D)
if mibBuilder.loadTexts:configDualMediaMode.setStatus(_A)
_ConfigAllowedOutgoingPorts_Type=Integer32
_ConfigAllowedOutgoingPorts_Object=MibTableColumn
configAllowedOutgoingPorts=_ConfigAllowedOutgoingPorts_Object((1,3,6,1,4,1,3181,10,6,1,81,1,1,14),_ConfigAllowedOutgoingPorts_Type())
configAllowedOutgoingPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:configAllowedOutgoingPorts.setStatus(_A)
_MonitorTable_Object=MibTable
monitorTable=_MonitorTable_Object((1,3,6,1,4,1,3181,10,6,1,81,2))
if mibBuilder.loadTexts:monitorTable.setStatus(_A)
_MonitorEntry_Object=MibTableRow
monitorEntry=_MonitorEntry_Object((1,3,6,1,4,1,3181,10,6,1,81,2,1))
monitorEntry.setIndexNames((0,_J,_Y))
if mibBuilder.loadTexts:monitorEntry.setStatus(_A)
class _MonitorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0))
_MonitorIndex_Type.__name__=_B
_MonitorIndex_Object=MibTableColumn
monitorIndex=_MonitorIndex_Object((1,3,6,1,4,1,3181,10,6,1,81,2,1,1),_MonitorIndex_Type())
monitorIndex.setMaxAccess(_T)
if mibBuilder.loadTexts:monitorIndex.setStatus(_A)
class _MonitorMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_E,0),('txOnly',1),('rxOnly',2),('rxAndTx',3)))
_MonitorMode_Type.__name__=_B
_MonitorMode_Object=MibTableColumn
monitorMode=_MonitorMode_Object((1,3,6,1,4,1,3181,10,6,1,81,2,1,2),_MonitorMode_Type())
monitorMode.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorMode.setStatus(_A)
_MonitorSource_Type=Integer32
_MonitorSource_Object=MibTableColumn
monitorSource=_MonitorSource_Object((1,3,6,1,4,1,3181,10,6,1,81,2,1,3),_MonitorSource_Type())
monitorSource.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorSource.setStatus(_A)
class _MonitorDestination_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MonitorDestination_Type.__name__=_B
_MonitorDestination_Object=MibTableColumn
monitorDestination=_MonitorDestination_Object((1,3,6,1,4,1,3181,10,6,1,81,2,1,4),_MonitorDestination_Type())
monitorDestination.setMaxAccess(_D)
if mibBuilder.loadTexts:monitorDestination.setStatus(_A)
_PortRestartPort_Type=DisplayString
_PortRestartPort_Object=MibScalar
portRestartPort=_PortRestartPort_Object((1,3,6,1,4,1,3181,10,6,1,81,3),_PortRestartPort_Type())
portRestartPort.setMaxAccess(_D)
if mibBuilder.loadTexts:portRestartPort.setStatus(_A)
_PortUplinkPorts_Type=Integer32
_PortUplinkPorts_Object=MibScalar
portUplinkPorts=_PortUplinkPorts_Object((1,3,6,1,4,1,3181,10,6,1,81,100),_PortUplinkPorts_Type())
portUplinkPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:portUplinkPorts.setStatus(_A)
_PortDownlinkPorts_Type=Integer32
_PortDownlinkPorts_Object=MibScalar
portDownlinkPorts=_PortDownlinkPorts_Object((1,3,6,1,4,1,3181,10,6,1,81,101),_PortDownlinkPorts_Type())
portDownlinkPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:portDownlinkPorts.setStatus(_A)
_StatusTable_Object=MibTable
statusTable=_StatusTable_Object((1,3,6,1,4,1,3181,10,6,1,81,102))
if mibBuilder.loadTexts:statusTable.setStatus(_A)
_StatusEntry_Object=MibTableRow
statusEntry=_StatusEntry_Object((1,3,6,1,4,1,3181,10,6,1,81,102,1))
statusEntry.setIndexNames((0,_J,_Z))
if mibBuilder.loadTexts:statusEntry.setStatus(_A)
class _StatusPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_StatusPortIndex_Type.__name__=_B
_StatusPortIndex_Object=MibTableColumn
statusPortIndex=_StatusPortIndex_Object((1,3,6,1,4,1,3181,10,6,1,81,102,1,1),_StatusPortIndex_Type())
statusPortIndex.setMaxAccess(_T)
if mibBuilder.loadTexts:statusPortIndex.setStatus(_A)
class _StatusLinkUp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_StatusLinkUp_Type.__name__=_B
_StatusLinkUp_Object=MibTableColumn
statusLinkUp=_StatusLinkUp_Object((1,3,6,1,4,1,3181,10,6,1,81,102,1,2),_StatusLinkUp_Type())
statusLinkUp.setMaxAccess(_C)
if mibBuilder.loadTexts:statusLinkUp.setStatus(_A)
_StatusLastLinkChange_Type=DisplayString
_StatusLastLinkChange_Object=MibTableColumn
statusLastLinkChange=_StatusLastLinkChange_Object((1,3,6,1,4,1,3181,10,6,1,81,102,1,3),_StatusLastLinkChange_Type())
statusLastLinkChange.setMaxAccess(_C)
if mibBuilder.loadTexts:statusLastLinkChange.setStatus(_A)
class _StatusLinkState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('linkDown',0),('blocking',1),('learning',2),('forwarding',3),('unauthVlan',4)))
_StatusLinkState_Type.__name__=_B
_StatusLinkState_Object=MibTableColumn
statusLinkState=_StatusLinkState_Object((1,3,6,1,4,1,3181,10,6,1,81,102,1,4),_StatusLinkState_Type())
statusLinkState.setMaxAccess(_C)
if mibBuilder.loadTexts:statusLinkState.setStatus(_A)
class _StatusRxActivity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_StatusRxActivity_Type.__name__=_B
_StatusRxActivity_Object=MibTableColumn
statusRxActivity=_StatusRxActivity_Object((1,3,6,1,4,1,3181,10,6,1,81,102,1,5),_StatusRxActivity_Type())
statusRxActivity.setMaxAccess(_C)
if mibBuilder.loadTexts:statusRxActivity.setStatus(_A)
class _StatusTxActivity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_StatusTxActivity_Type.__name__=_B
_StatusTxActivity_Object=MibTableColumn
statusTxActivity=_StatusTxActivity_Object((1,3,6,1,4,1,3181,10,6,1,81,102,1,6),_StatusTxActivity_Type())
statusTxActivity.setMaxAccess(_C)
if mibBuilder.loadTexts:statusTxActivity.setStatus(_A)
class _StatusMediaUsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('copper',1),('fiber',2)))
_StatusMediaUsed_Type.__name__=_B
_StatusMediaUsed_Object=MibTableColumn
statusMediaUsed=_StatusMediaUsed_Object((1,3,6,1,4,1,3181,10,6,1,81,102,1,7),_StatusMediaUsed_Type())
statusMediaUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:statusMediaUsed.setStatus(_A)
class _StatusSpeedUsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('down',0),(_V,1),(_W,2),(_X,3)))
_StatusSpeedUsed_Type.__name__=_B
_StatusSpeedUsed_Object=MibTableColumn
statusSpeedUsed=_StatusSpeedUsed_Object((1,3,6,1,4,1,3181,10,6,1,81,102,1,8),_StatusSpeedUsed_Type())
statusSpeedUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:statusSpeedUsed.setStatus(_A)
_StatusLoopedPort_Type=Integer32
_StatusLoopedPort_Object=MibTableColumn
statusLoopedPort=_StatusLoopedPort_Object((1,3,6,1,4,1,3181,10,6,1,81,102,1,9),_StatusLoopedPort_Type())
statusLoopedPort.setMaxAccess(_C)
if mibBuilder.loadTexts:statusLoopedPort.setStatus(_A)
class _StatusFullDuplexUsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('full',1),('half',2)))
_StatusFullDuplexUsed_Type.__name__=_B
_StatusFullDuplexUsed_Object=MibTableColumn
statusFullDuplexUsed=_StatusFullDuplexUsed_Object((1,3,6,1,4,1,3181,10,6,1,81,102,1,10),_StatusFullDuplexUsed_Type())
statusFullDuplexUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:statusFullDuplexUsed.setStatus(_A)
class _StatusFlowcontrolUsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_StatusFlowcontrolUsed_Type.__name__=_B
_StatusFlowcontrolUsed_Object=MibTableColumn
statusFlowcontrolUsed=_StatusFlowcontrolUsed_Object((1,3,6,1,4,1,3181,10,6,1,81,102,1,11),_StatusFlowcontrolUsed_Type())
statusFlowcontrolUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:statusFlowcontrolUsed.setStatus(_A)
class _StatusMdiUsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_StatusMdiUsed_Type.__name__=_B
_StatusMdiUsed_Object=MibTableColumn
statusMdiUsed=_StatusMdiUsed_Object((1,3,6,1,4,1,3181,10,6,1,81,102,1,12),_StatusMdiUsed_Type())
statusMdiUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:statusMdiUsed.setStatus(_A)
class _StatusEeeActive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_StatusEeeActive_Type.__name__=_B
_StatusEeeActive_Object=MibTableColumn
statusEeeActive=_StatusEeeActive_Object((1,3,6,1,4,1,3181,10,6,1,81,102,1,13),_StatusEeeActive_Type())
statusEeeActive.setMaxAccess(_C)
if mibBuilder.loadTexts:statusEeeActive.setStatus(_A)
class _StatusBlockingAlgorithm_Type(Bits):namedValues=NamedValues(*((_K,0),(_L,1),(_M,2),(_N,3),(_O,4),(_P,5),(_Q,6),(_R,7),(_S,8)))
_StatusBlockingAlgorithm_Type.__name__=_I
_StatusBlockingAlgorithm_Object=MibTableColumn
statusBlockingAlgorithm=_StatusBlockingAlgorithm_Object((1,3,6,1,4,1,3181,10,6,1,81,102,1,14),_StatusBlockingAlgorithm_Type())
statusBlockingAlgorithm.setMaxAccess(_C)
if mibBuilder.loadTexts:statusBlockingAlgorithm.setStatus(_A)
class _StatusLearningAlgorithm_Type(Bits):namedValues=NamedValues(*((_K,0),(_L,1),(_M,2),(_N,3),(_O,4),(_P,5),(_Q,6),(_R,7),(_S,8)))
_StatusLearningAlgorithm_Type.__name__=_I
_StatusLearningAlgorithm_Object=MibTableColumn
statusLearningAlgorithm=_StatusLearningAlgorithm_Object((1,3,6,1,4,1,3181,10,6,1,81,102,1,15),_StatusLearningAlgorithm_Type())
statusLearningAlgorithm.setMaxAccess(_C)
if mibBuilder.loadTexts:statusLearningAlgorithm.setStatus(_A)
class _StatusForwardingAlgorithm_Type(Bits):namedValues=NamedValues(*((_K,0),(_L,1),(_M,2),(_N,3),(_O,4),(_P,5),(_Q,6),(_R,7),(_S,8)))
_StatusForwardingAlgorithm_Type.__name__=_I
_StatusForwardingAlgorithm_Object=MibTableColumn
statusForwardingAlgorithm=_StatusForwardingAlgorithm_Object((1,3,6,1,4,1,3181,10,6,1,81,102,1,16),_StatusForwardingAlgorithm_Type())
statusForwardingAlgorithm.setMaxAccess(_C)
if mibBuilder.loadTexts:statusForwardingAlgorithm.setStatus(_A)
class _StatusUnauthorizedAlgorithm_Type(Bits):namedValues=NamedValues(*((_K,0),(_L,1),(_M,2),(_N,3),(_O,4),(_P,5),(_Q,6),(_R,7),(_S,8)))
_StatusUnauthorizedAlgorithm_Type.__name__=_I
_StatusUnauthorizedAlgorithm_Object=MibTableColumn
statusUnauthorizedAlgorithm=_StatusUnauthorizedAlgorithm_Object((1,3,6,1,4,1,3181,10,6,1,81,102,1,17),_StatusUnauthorizedAlgorithm_Type())
statusUnauthorizedAlgorithm.setMaxAccess(_C)
if mibBuilder.loadTexts:statusUnauthorizedAlgorithm.setStatus(_A)
mibBuilder.exportSymbols(_J,**{'device':device,'port':port,'configTable':configTable,'configEntry':configEntry,_U:configPortIndex,'configAlias':configAlias,'configPortOperation':configPortOperation,'configRole':configRole,'configSpeed':configSpeed,'configMtu':configMtu,'configLoopProtection':configLoopProtection,'configAutoNegotiation':configAutoNegotiation,'configFullDuplex':configFullDuplex,'configFlowcontrol':configFlowcontrol,'configMdiMode':configMdiMode,'configEnergyEfficiency':configEnergyEfficiency,'configDualMediaMode':configDualMediaMode,'configAllowedOutgoingPorts':configAllowedOutgoingPorts,'monitorTable':monitorTable,'monitorEntry':monitorEntry,_Y:monitorIndex,'monitorMode':monitorMode,'monitorSource':monitorSource,'monitorDestination':monitorDestination,'portRestartPort':portRestartPort,'portUplinkPorts':portUplinkPorts,'portDownlinkPorts':portDownlinkPorts,'statusTable':statusTable,'statusEntry':statusEntry,_Z:statusPortIndex,'statusLinkUp':statusLinkUp,'statusLastLinkChange':statusLastLinkChange,'statusLinkState':statusLinkState,'statusRxActivity':statusRxActivity,'statusTxActivity':statusTxActivity,'statusMediaUsed':statusMediaUsed,'statusSpeedUsed':statusSpeedUsed,'statusLoopedPort':statusLoopedPort,'statusFullDuplexUsed':statusFullDuplexUsed,'statusFlowcontrolUsed':statusFlowcontrolUsed,'statusMdiUsed':statusMdiUsed,'statusEeeActive':statusEeeActive,'statusBlockingAlgorithm':statusBlockingAlgorithm,'statusLearningAlgorithm':statusLearningAlgorithm,'statusForwardingAlgorithm':statusForwardingAlgorithm,'statusUnauthorizedAlgorithm':statusUnauthorizedAlgorithm})