_U='globalFnElecEqualizerIndex'
_T='globalFnElecAttenuatorIndex'
_S='globalFnRFPortIndex'
_R='globalFnRFRouterIndex'
_Q='normal'
_P='globalFnWingSwitchIndex'
_O='globalFnOpticalReceiverIndex'
_N='available'
_M='globalFnReturnLaserIndex'
_L='DisplayString'
_K='local'
_J='remote'
_I='segmentation'
_H='redundantMode'
_G='off'
_F='unavailable'
_E='ELECTROLINE-DHT-GLOBAL-FIBERNODE-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dhtExtensionsMibObjects,=mibBuilder.importSymbols('ELECTROLINE-DHT-EXTENSIONS-MIB','dhtExtensionsMibObjects')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_L,'PhysAddress','TextualConvention','TruthValue')
dhtGlobalFnIdentMIB=ModuleIdentity((1,3,6,1,4,1,5802,1,3,1,2,5,1,14))
if mibBuilder.loadTexts:dhtGlobalFnIdentMIB.setRevisions(('2004-12-10 00:00',))
_GlobalFnIdentObjects_ObjectIdentity=ObjectIdentity
globalFnIdentObjects=_GlobalFnIdentObjects_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,2,5,1,14,1))
class _GlobalFnNumberReturnLaser_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_GlobalFnNumberReturnLaser_Type.__name__=_C
_GlobalFnNumberReturnLaser_Object=MibScalar
globalFnNumberReturnLaser=_GlobalFnNumberReturnLaser_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,14,1,1),_GlobalFnNumberReturnLaser_Type())
globalFnNumberReturnLaser.setMaxAccess(_B)
if mibBuilder.loadTexts:globalFnNumberReturnLaser.setStatus(_A)
_GlobalFnReturnLaserTable_Object=MibTable
globalFnReturnLaserTable=_GlobalFnReturnLaserTable_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,14,1,2))
if mibBuilder.loadTexts:globalFnReturnLaserTable.setStatus(_A)
_GlobalFnReturnLaserTableEntry_Object=MibTableRow
globalFnReturnLaserTableEntry=_GlobalFnReturnLaserTableEntry_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,14,1,2,1))
globalFnReturnLaserTableEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:globalFnReturnLaserTableEntry.setStatus(_A)
_GlobalFnReturnLaserIndex_Type=Integer32
_GlobalFnReturnLaserIndex_Object=MibTableColumn
globalFnReturnLaserIndex=_GlobalFnReturnLaserIndex_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,14,1,2,1,1),_GlobalFnReturnLaserIndex_Type())
globalFnReturnLaserIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:globalFnReturnLaserIndex.setStatus(_A)
class _GlobalFnReturnLaserState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_N,2)))
_GlobalFnReturnLaserState_Type.__name__=_C
_GlobalFnReturnLaserState_Object=MibTableColumn
globalFnReturnLaserState=_GlobalFnReturnLaserState_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,14,1,2,1,2),_GlobalFnReturnLaserState_Type())
globalFnReturnLaserState.setMaxAccess(_B)
if mibBuilder.loadTexts:globalFnReturnLaserState.setStatus(_A)
_GlobalFnReturnLaserRFLevel_Type=Integer32
_GlobalFnReturnLaserRFLevel_Object=MibTableColumn
globalFnReturnLaserRFLevel=_GlobalFnReturnLaserRFLevel_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,14,1,2,1,3),_GlobalFnReturnLaserRFLevel_Type())
globalFnReturnLaserRFLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:globalFnReturnLaserRFLevel.setStatus(_A)
class _GlobalFnReturnLaserRFControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),('on',2)))
_GlobalFnReturnLaserRFControl_Type.__name__=_C
_GlobalFnReturnLaserRFControl_Object=MibTableColumn
globalFnReturnLaserRFControl=_GlobalFnReturnLaserRFControl_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,14,1,2,1,4),_GlobalFnReturnLaserRFControl_Type())
globalFnReturnLaserRFControl.setMaxAccess(_D)
if mibBuilder.loadTexts:globalFnReturnLaserRFControl.setStatus(_A)
_GlobalFnReturnLaserElecAttenuator_Type=Integer32
_GlobalFnReturnLaserElecAttenuator_Object=MibTableColumn
globalFnReturnLaserElecAttenuator=_GlobalFnReturnLaserElecAttenuator_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,14,1,2,1,5),_GlobalFnReturnLaserElecAttenuator_Type())
globalFnReturnLaserElecAttenuator.setMaxAccess(_D)
if mibBuilder.loadTexts:globalFnReturnLaserElecAttenuator.setStatus(_A)
class _GlobalFnNumberOpticalReceiver_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_GlobalFnNumberOpticalReceiver_Type.__name__=_C
_GlobalFnNumberOpticalReceiver_Object=MibScalar
globalFnNumberOpticalReceiver=_GlobalFnNumberOpticalReceiver_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,14,1,3),_GlobalFnNumberOpticalReceiver_Type())
globalFnNumberOpticalReceiver.setMaxAccess(_B)
if mibBuilder.loadTexts:globalFnNumberOpticalReceiver.setStatus(_A)
class _GlobalFnOpticalReceiverAGCState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_GlobalFnOpticalReceiverAGCState_Type.__name__=_C
_GlobalFnOpticalReceiverAGCState_Object=MibScalar
globalFnOpticalReceiverAGCState=_GlobalFnOpticalReceiverAGCState_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,14,1,4),_GlobalFnOpticalReceiverAGCState_Type())
globalFnOpticalReceiverAGCState.setMaxAccess(_B)
if mibBuilder.loadTexts:globalFnOpticalReceiverAGCState.setStatus(_A)
class _GlobalFnOpticalReceiverAGCControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('frx1-agc-off',1),('frx1-agc-on',2),('frx2-agc-off',3),('frx2-agc-on',4)))
_GlobalFnOpticalReceiverAGCControl_Type.__name__=_C
_GlobalFnOpticalReceiverAGCControl_Object=MibScalar
globalFnOpticalReceiverAGCControl=_GlobalFnOpticalReceiverAGCControl_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,14,1,5),_GlobalFnOpticalReceiverAGCControl_Type())
globalFnOpticalReceiverAGCControl.setMaxAccess(_D)
if mibBuilder.loadTexts:globalFnOpticalReceiverAGCControl.setStatus(_A)
_GlobalFnOpticalReceiverTable_Object=MibTable
globalFnOpticalReceiverTable=_GlobalFnOpticalReceiverTable_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,14,1,6))
if mibBuilder.loadTexts:globalFnOpticalReceiverTable.setStatus(_A)
_GlobalFnOpticalReceiverTableEntry_Object=MibTableRow
globalFnOpticalReceiverTableEntry=_GlobalFnOpticalReceiverTableEntry_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,14,1,6,1))
globalFnOpticalReceiverTableEntry.setIndexNames((0,_E,_O))
if mibBuilder.loadTexts:globalFnOpticalReceiverTableEntry.setStatus(_A)
_GlobalFnOpticalReceiverIndex_Type=Integer32
_GlobalFnOpticalReceiverIndex_Object=MibTableColumn
globalFnOpticalReceiverIndex=_GlobalFnOpticalReceiverIndex_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,14,1,6,1,1),_GlobalFnOpticalReceiverIndex_Type())
globalFnOpticalReceiverIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:globalFnOpticalReceiverIndex.setStatus(_A)
class _GlobalFnOpticalReceiverState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_N,2)))
_GlobalFnOpticalReceiverState_Type.__name__=_C
_GlobalFnOpticalReceiverState_Object=MibTableColumn
globalFnOpticalReceiverState=_GlobalFnOpticalReceiverState_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,14,1,6,1,2),_GlobalFnOpticalReceiverState_Type())
globalFnOpticalReceiverState.setMaxAccess(_B)
if mibBuilder.loadTexts:globalFnOpticalReceiverState.setStatus(_A)
class _GlobalFnOpticalReceiverType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_GlobalFnOpticalReceiverType_Type.__name__=_L
_GlobalFnOpticalReceiverType_Object=MibTableColumn
globalFnOpticalReceiverType=_GlobalFnOpticalReceiverType_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,14,1,6,1,3),_GlobalFnOpticalReceiverType_Type())
globalFnOpticalReceiverType.setMaxAccess(_B)
if mibBuilder.loadTexts:globalFnOpticalReceiverType.setStatus('optional')
_GlobalFnOpticalReceiverRFLevel_Type=Integer32
_GlobalFnOpticalReceiverRFLevel_Object=MibTableColumn
globalFnOpticalReceiverRFLevel=_GlobalFnOpticalReceiverRFLevel_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,14,1,6,1,4),_GlobalFnOpticalReceiverRFLevel_Type())
globalFnOpticalReceiverRFLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:globalFnOpticalReceiverRFLevel.setStatus(_A)
class _GlobalFnOpticalReceiverRFControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),('on',2)))
_GlobalFnOpticalReceiverRFControl_Type.__name__=_C
_GlobalFnOpticalReceiverRFControl_Object=MibTableColumn
globalFnOpticalReceiverRFControl=_GlobalFnOpticalReceiverRFControl_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,14,1,6,1,5),_GlobalFnOpticalReceiverRFControl_Type())
globalFnOpticalReceiverRFControl.setMaxAccess(_D)
if mibBuilder.loadTexts:globalFnOpticalReceiverRFControl.setStatus(_A)
_GlobalFnOpticalReceiverElecAttenuator_Type=Integer32
_GlobalFnOpticalReceiverElecAttenuator_Object=MibTableColumn
globalFnOpticalReceiverElecAttenuator=_GlobalFnOpticalReceiverElecAttenuator_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,14,1,6,1,6),_GlobalFnOpticalReceiverElecAttenuator_Type())
globalFnOpticalReceiverElecAttenuator.setMaxAccess(_D)
if mibBuilder.loadTexts:globalFnOpticalReceiverElecAttenuator.setStatus(_A)
class _GlobalFnNumberWingSwitch_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_GlobalFnNumberWingSwitch_Type.__name__=_C
_GlobalFnNumberWingSwitch_Object=MibScalar
globalFnNumberWingSwitch=_GlobalFnNumberWingSwitch_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,14,1,7),_GlobalFnNumberWingSwitch_Type())
globalFnNumberWingSwitch.setMaxAccess(_B)
if mibBuilder.loadTexts:globalFnNumberWingSwitch.setStatus(_A)
_GlobalFnWingSwitchTable_Object=MibTable
globalFnWingSwitchTable=_GlobalFnWingSwitchTable_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,14,1,8))
if mibBuilder.loadTexts:globalFnWingSwitchTable.setStatus(_A)
_GlobalFnWingSwitchTableEntry_Object=MibTableRow
globalFnWingSwitchTableEntry=_GlobalFnWingSwitchTableEntry_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,14,1,8,1))
globalFnWingSwitchTableEntry.setIndexNames((0,_E,_P))
if mibBuilder.loadTexts:globalFnWingSwitchTableEntry.setStatus(_A)
_GlobalFnWingSwitchIndex_Type=Integer32
_GlobalFnWingSwitchIndex_Object=MibTableColumn
globalFnWingSwitchIndex=_GlobalFnWingSwitchIndex_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,14,1,8,1,1),_GlobalFnWingSwitchIndex_Type())
globalFnWingSwitchIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:globalFnWingSwitchIndex.setStatus(_A)
class _GlobalFnWingSwitchState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_F,0),(_G,1),('sixDb',2),(_Q,3)))
_GlobalFnWingSwitchState_Type.__name__=_C
_GlobalFnWingSwitchState_Object=MibTableColumn
globalFnWingSwitchState=_GlobalFnWingSwitchState_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,14,1,8,1,2),_GlobalFnWingSwitchState_Type())
globalFnWingSwitchState.setMaxAccess(_B)
if mibBuilder.loadTexts:globalFnWingSwitchState.setStatus(_A)
class _GlobalFnWingSwitchControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),('sixDb',2),(_Q,3)))
_GlobalFnWingSwitchControl_Type.__name__=_C
_GlobalFnWingSwitchControl_Object=MibTableColumn
globalFnWingSwitchControl=_GlobalFnWingSwitchControl_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,14,1,8,1,3),_GlobalFnWingSwitchControl_Type())
globalFnWingSwitchControl.setMaxAccess(_D)
if mibBuilder.loadTexts:globalFnWingSwitchControl.setStatus(_A)
class _GlobalFnNumberRFRouter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_GlobalFnNumberRFRouter_Type.__name__=_C
_GlobalFnNumberRFRouter_Object=MibScalar
globalFnNumberRFRouter=_GlobalFnNumberRFRouter_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,14,1,9),_GlobalFnNumberRFRouter_Type())
globalFnNumberRFRouter.setMaxAccess(_B)
if mibBuilder.loadTexts:globalFnNumberRFRouter.setStatus(_A)
_GlobalFnRFRouterTable_Object=MibTable
globalFnRFRouterTable=_GlobalFnRFRouterTable_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,14,1,10))
if mibBuilder.loadTexts:globalFnRFRouterTable.setStatus(_A)
_GlobalRFRouterTableEntry_Object=MibTableRow
globalRFRouterTableEntry=_GlobalRFRouterTableEntry_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,14,1,10,1))
globalRFRouterTableEntry.setIndexNames((0,_E,_R))
if mibBuilder.loadTexts:globalRFRouterTableEntry.setStatus(_A)
_GlobalFnRFRouterIndex_Type=Integer32
_GlobalFnRFRouterIndex_Object=MibTableColumn
globalFnRFRouterIndex=_GlobalFnRFRouterIndex_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,14,1,10,1,1),_GlobalFnRFRouterIndex_Type())
globalFnRFRouterIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:globalFnRFRouterIndex.setStatus(_A)
class _GlobalFnRFRouterType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_GlobalFnRFRouterType_Type.__name__=_L
_GlobalFnRFRouterType_Object=MibTableColumn
globalFnRFRouterType=_GlobalFnRFRouterType_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,14,1,10,1,2),_GlobalFnRFRouterType_Type())
globalFnRFRouterType.setMaxAccess(_B)
if mibBuilder.loadTexts:globalFnRFRouterType.setStatus(_A)
class _GlobalFnRFRouterDownstreamSwitchState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),(_H,1),(_I,2)))
_GlobalFnRFRouterDownstreamSwitchState_Type.__name__=_C
_GlobalFnRFRouterDownstreamSwitchState_Object=MibTableColumn
globalFnRFRouterDownstreamSwitchState=_GlobalFnRFRouterDownstreamSwitchState_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,14,1,10,1,3),_GlobalFnRFRouterDownstreamSwitchState_Type())
globalFnRFRouterDownstreamSwitchState.setMaxAccess(_B)
if mibBuilder.loadTexts:globalFnRFRouterDownstreamSwitchState.setStatus(_A)
class _GlobalFnRFRouterDownstreamSwitchControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_GlobalFnRFRouterDownstreamSwitchControl_Type.__name__=_C
_GlobalFnRFRouterDownstreamSwitchControl_Object=MibTableColumn
globalFnRFRouterDownstreamSwitchControl=_GlobalFnRFRouterDownstreamSwitchControl_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,14,1,10,1,4),_GlobalFnRFRouterDownstreamSwitchControl_Type())
globalFnRFRouterDownstreamSwitchControl.setMaxAccess(_D)
if mibBuilder.loadTexts:globalFnRFRouterDownstreamSwitchControl.setStatus(_A)
class _GlobalFnRFRouterDownstreamControlTypeState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_K,1)))
_GlobalFnRFRouterDownstreamControlTypeState_Type.__name__=_C
_GlobalFnRFRouterDownstreamControlTypeState_Object=MibTableColumn
globalFnRFRouterDownstreamControlTypeState=_GlobalFnRFRouterDownstreamControlTypeState_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,14,1,10,1,5),_GlobalFnRFRouterDownstreamControlTypeState_Type())
globalFnRFRouterDownstreamControlTypeState.setMaxAccess(_B)
if mibBuilder.loadTexts:globalFnRFRouterDownstreamControlTypeState.setStatus(_A)
class _GlobalFnRFRouterDownstreamControlTypeSetting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_K,1)))
_GlobalFnRFRouterDownstreamControlTypeSetting_Type.__name__=_C
_GlobalFnRFRouterDownstreamControlTypeSetting_Object=MibTableColumn
globalFnRFRouterDownstreamControlTypeSetting=_GlobalFnRFRouterDownstreamControlTypeSetting_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,14,1,10,1,6),_GlobalFnRFRouterDownstreamControlTypeSetting_Type())
globalFnRFRouterDownstreamControlTypeSetting.setMaxAccess(_D)
if mibBuilder.loadTexts:globalFnRFRouterDownstreamControlTypeSetting.setStatus(_A)
class _GlobalFnRFRouterUptreamSwitchState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),(_H,1),(_I,2)))
_GlobalFnRFRouterUptreamSwitchState_Type.__name__=_C
_GlobalFnRFRouterUptreamSwitchState_Object=MibTableColumn
globalFnRFRouterUptreamSwitchState=_GlobalFnRFRouterUptreamSwitchState_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,14,1,10,1,7),_GlobalFnRFRouterUptreamSwitchState_Type())
globalFnRFRouterUptreamSwitchState.setMaxAccess(_B)
if mibBuilder.loadTexts:globalFnRFRouterUptreamSwitchState.setStatus(_A)
class _GlobalFnRFRouterUptreamSwitchControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_GlobalFnRFRouterUptreamSwitchControl_Type.__name__=_C
_GlobalFnRFRouterUptreamSwitchControl_Object=MibTableColumn
globalFnRFRouterUptreamSwitchControl=_GlobalFnRFRouterUptreamSwitchControl_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,14,1,10,1,8),_GlobalFnRFRouterUptreamSwitchControl_Type())
globalFnRFRouterUptreamSwitchControl.setMaxAccess(_D)
if mibBuilder.loadTexts:globalFnRFRouterUptreamSwitchControl.setStatus(_A)
class _GlobalFnRFRouterUpstreamControlTypeState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_K,1)))
_GlobalFnRFRouterUpstreamControlTypeState_Type.__name__=_C
_GlobalFnRFRouterUpstreamControlTypeState_Object=MibTableColumn
globalFnRFRouterUpstreamControlTypeState=_GlobalFnRFRouterUpstreamControlTypeState_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,14,1,10,1,9),_GlobalFnRFRouterUpstreamControlTypeState_Type())
globalFnRFRouterUpstreamControlTypeState.setMaxAccess(_B)
if mibBuilder.loadTexts:globalFnRFRouterUpstreamControlTypeState.setStatus(_A)
class _GlobalFnRFRouterUpstreamControlTypeSetting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_K,1)))
_GlobalFnRFRouterUpstreamControlTypeSetting_Type.__name__=_C
_GlobalFnRFRouterUpstreamControlTypeSetting_Object=MibTableColumn
globalFnRFRouterUpstreamControlTypeSetting=_GlobalFnRFRouterUpstreamControlTypeSetting_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,14,1,10,1,10),_GlobalFnRFRouterUpstreamControlTypeSetting_Type())
globalFnRFRouterUpstreamControlTypeSetting.setMaxAccess(_D)
if mibBuilder.loadTexts:globalFnRFRouterUpstreamControlTypeSetting.setStatus(_A)
class _GlobalFnNumberRFPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_GlobalFnNumberRFPort_Type.__name__=_C
_GlobalFnNumberRFPort_Object=MibScalar
globalFnNumberRFPort=_GlobalFnNumberRFPort_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,14,1,11),_GlobalFnNumberRFPort_Type())
globalFnNumberRFPort.setMaxAccess(_B)
if mibBuilder.loadTexts:globalFnNumberRFPort.setStatus(_A)
class _GlobalRFLinkSwitchState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_GlobalRFLinkSwitchState_Type.__name__=_C
_GlobalRFLinkSwitchState_Object=MibScalar
globalRFLinkSwitchState=_GlobalRFLinkSwitchState_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,14,1,12),_GlobalRFLinkSwitchState_Type())
globalRFLinkSwitchState.setMaxAccess(_B)
if mibBuilder.loadTexts:globalRFLinkSwitchState.setStatus(_A)
class _GlobalReverseRFLinkSwitchState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_GlobalReverseRFLinkSwitchState_Type.__name__=_C
_GlobalReverseRFLinkSwitchState_Object=MibScalar
globalReverseRFLinkSwitchState=_GlobalReverseRFLinkSwitchState_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,14,1,13),_GlobalReverseRFLinkSwitchState_Type())
globalReverseRFLinkSwitchState.setMaxAccess(_B)
if mibBuilder.loadTexts:globalReverseRFLinkSwitchState.setStatus(_A)
class _GlobalReverseRFLinkSwitchControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('path1-off',1),('path1-on',2),('path2-off',3),('path2-on',4),('path3-off',5),('path3-on',6)))
_GlobalReverseRFLinkSwitchControl_Type.__name__=_C
_GlobalReverseRFLinkSwitchControl_Object=MibScalar
globalReverseRFLinkSwitchControl=_GlobalReverseRFLinkSwitchControl_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,14,1,14),_GlobalReverseRFLinkSwitchControl_Type())
globalReverseRFLinkSwitchControl.setMaxAccess(_D)
if mibBuilder.loadTexts:globalReverseRFLinkSwitchControl.setStatus(_A)
_GlobalFnRFPortTable_Object=MibTable
globalFnRFPortTable=_GlobalFnRFPortTable_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,14,1,15))
if mibBuilder.loadTexts:globalFnRFPortTable.setStatus(_A)
_GlobalFnRFPortTableEntry_Object=MibTableRow
globalFnRFPortTableEntry=_GlobalFnRFPortTableEntry_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,14,1,15,1))
globalFnRFPortTableEntry.setIndexNames((0,_E,_S))
if mibBuilder.loadTexts:globalFnRFPortTableEntry.setStatus(_A)
_GlobalFnRFPortIndex_Type=Integer32
_GlobalFnRFPortIndex_Object=MibTableColumn
globalFnRFPortIndex=_GlobalFnRFPortIndex_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,14,1,15,1,1),_GlobalFnRFPortIndex_Type())
globalFnRFPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:globalFnRFPortIndex.setStatus(_A)
_GlobalUpStreamRFLevel_Type=Integer32
_GlobalUpStreamRFLevel_Object=MibTableColumn
globalUpStreamRFLevel=_GlobalUpStreamRFLevel_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,14,1,15,1,2),_GlobalUpStreamRFLevel_Type())
globalUpStreamRFLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:globalUpStreamRFLevel.setStatus(_A)
_GlobalFnDownStreamRFLevel_Type=Integer32
_GlobalFnDownStreamRFLevel_Object=MibTableColumn
globalFnDownStreamRFLevel=_GlobalFnDownStreamRFLevel_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,14,1,15,1,3),_GlobalFnDownStreamRFLevel_Type())
globalFnDownStreamRFLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:globalFnDownStreamRFLevel.setStatus(_A)
class _GlobalFnNumberElecAttenuator_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_GlobalFnNumberElecAttenuator_Type.__name__=_C
_GlobalFnNumberElecAttenuator_Object=MibScalar
globalFnNumberElecAttenuator=_GlobalFnNumberElecAttenuator_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,14,1,16),_GlobalFnNumberElecAttenuator_Type())
globalFnNumberElecAttenuator.setMaxAccess(_B)
if mibBuilder.loadTexts:globalFnNumberElecAttenuator.setStatus(_A)
_GlobalFnElecAttenuatorTable_Object=MibTable
globalFnElecAttenuatorTable=_GlobalFnElecAttenuatorTable_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,14,1,17))
if mibBuilder.loadTexts:globalFnElecAttenuatorTable.setStatus(_A)
_GlobalFnElecAttenuatorTableEntry_Object=MibTableRow
globalFnElecAttenuatorTableEntry=_GlobalFnElecAttenuatorTableEntry_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,14,1,17,1))
globalFnElecAttenuatorTableEntry.setIndexNames((0,_E,_T))
if mibBuilder.loadTexts:globalFnElecAttenuatorTableEntry.setStatus(_A)
_GlobalFnElecAttenuatorIndex_Type=Integer32
_GlobalFnElecAttenuatorIndex_Object=MibTableColumn
globalFnElecAttenuatorIndex=_GlobalFnElecAttenuatorIndex_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,14,1,17,1,1),_GlobalFnElecAttenuatorIndex_Type())
globalFnElecAttenuatorIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:globalFnElecAttenuatorIndex.setStatus(_A)
_GlobalFnElecAttenuatorValue_Type=Integer32
_GlobalFnElecAttenuatorValue_Object=MibTableColumn
globalFnElecAttenuatorValue=_GlobalFnElecAttenuatorValue_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,14,1,17,1,2),_GlobalFnElecAttenuatorValue_Type())
globalFnElecAttenuatorValue.setMaxAccess(_D)
if mibBuilder.loadTexts:globalFnElecAttenuatorValue.setStatus(_A)
class _GlobalFnNumberElecEqualizer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_GlobalFnNumberElecEqualizer_Type.__name__=_C
_GlobalFnNumberElecEqualizer_Object=MibScalar
globalFnNumberElecEqualizer=_GlobalFnNumberElecEqualizer_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,14,1,18),_GlobalFnNumberElecEqualizer_Type())
globalFnNumberElecEqualizer.setMaxAccess(_B)
if mibBuilder.loadTexts:globalFnNumberElecEqualizer.setStatus(_A)
_GlobalFnElecEqualizerTable_Object=MibTable
globalFnElecEqualizerTable=_GlobalFnElecEqualizerTable_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,14,1,19))
if mibBuilder.loadTexts:globalFnElecEqualizerTable.setStatus(_A)
_GlobalFnElecEqualizerTableEntry_Object=MibTableRow
globalFnElecEqualizerTableEntry=_GlobalFnElecEqualizerTableEntry_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,14,1,19,1))
globalFnElecEqualizerTableEntry.setIndexNames((0,_E,_U))
if mibBuilder.loadTexts:globalFnElecEqualizerTableEntry.setStatus(_A)
_GlobalFnElecEqualizerIndex_Type=Integer32
_GlobalFnElecEqualizerIndex_Object=MibTableColumn
globalFnElecEqualizerIndex=_GlobalFnElecEqualizerIndex_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,14,1,19,1,1),_GlobalFnElecEqualizerIndex_Type())
globalFnElecEqualizerIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:globalFnElecEqualizerIndex.setStatus(_A)
_GlobalFnElecEqualizerValue_Type=Integer32
_GlobalFnElecEqualizerValue_Object=MibTableColumn
globalFnElecEqualizerValue=_GlobalFnElecEqualizerValue_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,14,1,19,1,2),_GlobalFnElecEqualizerValue_Type())
globalFnElecEqualizerValue.setMaxAccess(_D)
if mibBuilder.loadTexts:globalFnElecEqualizerValue.setStatus(_A)
_GlobalFnAGCOffsetValue_Type=Integer32
_GlobalFnAGCOffsetValue_Object=MibScalar
globalFnAGCOffsetValue=_GlobalFnAGCOffsetValue_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,14,1,20),_GlobalFnAGCOffsetValue_Type())
globalFnAGCOffsetValue.setMaxAccess(_D)
if mibBuilder.loadTexts:globalFnAGCOffsetValue.setStatus(_A)
_GlobalFnAGCRfLevel_Type=Integer32
_GlobalFnAGCRfLevel_Object=MibScalar
globalFnAGCRfLevel=_GlobalFnAGCRfLevel_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,14,1,21),_GlobalFnAGCRfLevel_Type())
globalFnAGCRfLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:globalFnAGCRfLevel.setStatus(_A)
_GlobalFnRfLevelOffsetValue_Type=Integer32
_GlobalFnRfLevelOffsetValue_Object=MibScalar
globalFnRfLevelOffsetValue=_GlobalFnRfLevelOffsetValue_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,14,1,22),_GlobalFnRfLevelOffsetValue_Type())
globalFnRfLevelOffsetValue.setMaxAccess(_D)
if mibBuilder.loadTexts:globalFnRfLevelOffsetValue.setStatus(_A)
_GlobalFnTemperature_Type=Integer32
_GlobalFnTemperature_Object=MibScalar
globalFnTemperature=_GlobalFnTemperature_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,14,1,23),_GlobalFnTemperature_Type())
globalFnTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:globalFnTemperature.setStatus(_A)
class _GlobalFnReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('reset',1))
_GlobalFnReset_Type.__name__=_C
_GlobalFnReset_Object=MibScalar
globalFnReset=_GlobalFnReset_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,14,1,24),_GlobalFnReset_Type())
globalFnReset.setMaxAccess(_D)
if mibBuilder.loadTexts:globalFnReset.setStatus(_A)
class _GlobalFnResetFrxRtx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('reset',1))
_GlobalFnResetFrxRtx_Type.__name__=_C
_GlobalFnResetFrxRtx_Object=MibScalar
globalFnResetFrxRtx=_GlobalFnResetFrxRtx_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,14,1,25),_GlobalFnResetFrxRtx_Type())
globalFnResetFrxRtx.setMaxAccess(_D)
if mibBuilder.loadTexts:globalFnResetFrxRtx.setStatus(_A)
class _GlobalFnTypeOfPowerSupply_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('not-defined',0),('linePower',1),('mainPower',2)))
_GlobalFnTypeOfPowerSupply_Type.__name__=_C
_GlobalFnTypeOfPowerSupply_Object=MibScalar
globalFnTypeOfPowerSupply=_GlobalFnTypeOfPowerSupply_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,14,1,26),_GlobalFnTypeOfPowerSupply_Type())
globalFnTypeOfPowerSupply.setMaxAccess(_B)
if mibBuilder.loadTexts:globalFnTypeOfPowerSupply.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'dhtGlobalFnIdentMIB':dhtGlobalFnIdentMIB,'globalFnIdentObjects':globalFnIdentObjects,'globalFnNumberReturnLaser':globalFnNumberReturnLaser,'globalFnReturnLaserTable':globalFnReturnLaserTable,'globalFnReturnLaserTableEntry':globalFnReturnLaserTableEntry,_M:globalFnReturnLaserIndex,'globalFnReturnLaserState':globalFnReturnLaserState,'globalFnReturnLaserRFLevel':globalFnReturnLaserRFLevel,'globalFnReturnLaserRFControl':globalFnReturnLaserRFControl,'globalFnReturnLaserElecAttenuator':globalFnReturnLaserElecAttenuator,'globalFnNumberOpticalReceiver':globalFnNumberOpticalReceiver,'globalFnOpticalReceiverAGCState':globalFnOpticalReceiverAGCState,'globalFnOpticalReceiverAGCControl':globalFnOpticalReceiverAGCControl,'globalFnOpticalReceiverTable':globalFnOpticalReceiverTable,'globalFnOpticalReceiverTableEntry':globalFnOpticalReceiverTableEntry,_O:globalFnOpticalReceiverIndex,'globalFnOpticalReceiverState':globalFnOpticalReceiverState,'globalFnOpticalReceiverType':globalFnOpticalReceiverType,'globalFnOpticalReceiverRFLevel':globalFnOpticalReceiverRFLevel,'globalFnOpticalReceiverRFControl':globalFnOpticalReceiverRFControl,'globalFnOpticalReceiverElecAttenuator':globalFnOpticalReceiverElecAttenuator,'globalFnNumberWingSwitch':globalFnNumberWingSwitch,'globalFnWingSwitchTable':globalFnWingSwitchTable,'globalFnWingSwitchTableEntry':globalFnWingSwitchTableEntry,_P:globalFnWingSwitchIndex,'globalFnWingSwitchState':globalFnWingSwitchState,'globalFnWingSwitchControl':globalFnWingSwitchControl,'globalFnNumberRFRouter':globalFnNumberRFRouter,'globalFnRFRouterTable':globalFnRFRouterTable,'globalRFRouterTableEntry':globalRFRouterTableEntry,_R:globalFnRFRouterIndex,'globalFnRFRouterType':globalFnRFRouterType,'globalFnRFRouterDownstreamSwitchState':globalFnRFRouterDownstreamSwitchState,'globalFnRFRouterDownstreamSwitchControl':globalFnRFRouterDownstreamSwitchControl,'globalFnRFRouterDownstreamControlTypeState':globalFnRFRouterDownstreamControlTypeState,'globalFnRFRouterDownstreamControlTypeSetting':globalFnRFRouterDownstreamControlTypeSetting,'globalFnRFRouterUptreamSwitchState':globalFnRFRouterUptreamSwitchState,'globalFnRFRouterUptreamSwitchControl':globalFnRFRouterUptreamSwitchControl,'globalFnRFRouterUpstreamControlTypeState':globalFnRFRouterUpstreamControlTypeState,'globalFnRFRouterUpstreamControlTypeSetting':globalFnRFRouterUpstreamControlTypeSetting,'globalFnNumberRFPort':globalFnNumberRFPort,'globalRFLinkSwitchState':globalRFLinkSwitchState,'globalReverseRFLinkSwitchState':globalReverseRFLinkSwitchState,'globalReverseRFLinkSwitchControl':globalReverseRFLinkSwitchControl,'globalFnRFPortTable':globalFnRFPortTable,'globalFnRFPortTableEntry':globalFnRFPortTableEntry,_S:globalFnRFPortIndex,'globalUpStreamRFLevel':globalUpStreamRFLevel,'globalFnDownStreamRFLevel':globalFnDownStreamRFLevel,'globalFnNumberElecAttenuator':globalFnNumberElecAttenuator,'globalFnElecAttenuatorTable':globalFnElecAttenuatorTable,'globalFnElecAttenuatorTableEntry':globalFnElecAttenuatorTableEntry,_T:globalFnElecAttenuatorIndex,'globalFnElecAttenuatorValue':globalFnElecAttenuatorValue,'globalFnNumberElecEqualizer':globalFnNumberElecEqualizer,'globalFnElecEqualizerTable':globalFnElecEqualizerTable,'globalFnElecEqualizerTableEntry':globalFnElecEqualizerTableEntry,_U:globalFnElecEqualizerIndex,'globalFnElecEqualizerValue':globalFnElecEqualizerValue,'globalFnAGCOffsetValue':globalFnAGCOffsetValue,'globalFnAGCRfLevel':globalFnAGCRfLevel,'globalFnRfLevelOffsetValue':globalFnRfLevelOffsetValue,'globalFnTemperature':globalFnTemperature,'globalFnReset':globalFnReset,'globalFnResetFrxRtx':globalFnResetFrxRtx,'globalFnTypeOfPowerSupply':globalFnTypeOfPowerSupply})