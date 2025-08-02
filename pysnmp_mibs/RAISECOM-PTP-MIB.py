_b='raisecomPtpPortIdentity'
_a='raisecomPtpPortState'
_Z='raisecomPtpUnicastPeerPoolIndex'
_Y='raisecomPtpUnicastSlavePoolIndex'
_X='raisecomPtpUnicastMasterPoolIndex'
_W='raisecomPtpForeignRecordIndex'
_V='peer-to-peer'
_U='end-to-end'
_T='passive'
_S='master'
_R='faulty'
_Q='novalid'
_P='enable'
_O='disable'
_N='pdelay'
_M='delay'
_L='sync'
_K='announce'
_J='not-accessible'
_I='invalid'
_H='RAISECOM-PTP-MIB'
_G='read-create'
_F='rcPortIndex'
_E='SWITCH-SYSTEM-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
raisecomAgent,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','raisecomAgent')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
rcPortIndex,=mibBuilder.importSymbols(_E,_F)
EnableVar,=mibBuilder.importSymbols('SWITCH-TC','EnableVar')
raisecomPtp=ModuleIdentity((1,3,6,1,4,1,8886,1,26))
if mibBuilder.loadTexts:raisecomPtp.setRevisions(('2010-10-29 00:00',))
class PTPTimeStamp(TextualConvention,OctetString):status=_A;displayHint='6d.4d';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
class PTPTimeInterval(TextualConvention,OctetString):status=_A;displayHint='8d.4d';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(12,12));fixedLength=12
class PTPClockIdentity(TextualConvention,OctetString):status=_A;displayHint='1h:1h:1h:1h:1h:1h:1h:1h';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
class PTPPortIdentity(TextualConvention,OctetString):status=_A;displayHint='1h:1h:1h:1h:1h:1h:1h:1h.2d';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_RaisecomPtpGlobal_ObjectIdentity=ObjectIdentity
raisecomPtpGlobal=_RaisecomPtpGlobal_ObjectIdentity((1,3,6,1,4,1,8886,1,26,1))
class _RaisecomPtpEnable_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_O,0),(_P,1)))
_RaisecomPtpEnable_Type.__name__=_C
_RaisecomPtpEnable_Object=MibScalar
raisecomPtpEnable=_RaisecomPtpEnable_Object((1,3,6,1,4,1,8886,1,26,1,1),_RaisecomPtpEnable_Type())
raisecomPtpEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomPtpEnable.setStatus(_A)
class _RaisecomPtpClockMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ordinary',1),('boundary',2),('e2e-transparent',3),('p2p-transparent',4)))
_RaisecomPtpClockMode_Type.__name__=_C
_RaisecomPtpClockMode_Object=MibScalar
raisecomPtpClockMode=_RaisecomPtpClockMode_Object((1,3,6,1,4,1,8886,1,26,1,2),_RaisecomPtpClockMode_Type())
raisecomPtpClockMode.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomPtpClockMode.setStatus(_A)
class _RaisecomPtpClockUnicastFlag_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('multicast',0),('unicast',1)))
_RaisecomPtpClockUnicastFlag_Type.__name__=_C
_RaisecomPtpClockUnicastFlag_Object=MibScalar
raisecomPtpClockUnicastFlag=_RaisecomPtpClockUnicastFlag_Object((1,3,6,1,4,1,8886,1,26,1,3),_RaisecomPtpClockUnicastFlag_Type())
raisecomPtpClockUnicastFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomPtpClockUnicastFlag.setStatus(_A)
class _RaisecomPtpClockStepFlag_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('onestep',1),('twostep',2)))
_RaisecomPtpClockStepFlag_Type.__name__=_C
_RaisecomPtpClockStepFlag_Object=MibScalar
raisecomPtpClockStepFlag=_RaisecomPtpClockStepFlag_Object((1,3,6,1,4,1,8886,1,26,1,4),_RaisecomPtpClockStepFlag_Type())
raisecomPtpClockStepFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomPtpClockStepFlag.setStatus(_A)
class _RaisecomPtpClockStatisticClear_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),('clear',1)))
_RaisecomPtpClockStatisticClear_Type.__name__=_C
_RaisecomPtpClockStatisticClear_Object=MibScalar
raisecomPtpClockStatisticClear=_RaisecomPtpClockStatisticClear_Object((1,3,6,1,4,1,8886,1,26,1,5),_RaisecomPtpClockStatisticClear_Type())
raisecomPtpClockStatisticClear.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomPtpClockStatisticClear.setStatus(_A)
_RaisecomPtpGlobalPortTable_Object=MibTable
raisecomPtpGlobalPortTable=_RaisecomPtpGlobalPortTable_Object((1,3,6,1,4,1,8886,1,26,1,6))
if mibBuilder.loadTexts:raisecomPtpGlobalPortTable.setStatus(_A)
_RaisecomPtpGlobalPortEntry_Object=MibTableRow
raisecomPtpGlobalPortEntry=_RaisecomPtpGlobalPortEntry_Object((1,3,6,1,4,1,8886,1,26,1,6,1))
raisecomPtpGlobalPortEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:raisecomPtpGlobalPortEntry.setStatus(_A)
class _RaisecomPtpPortEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_O,0),(_P,1)))
_RaisecomPtpPortEnable_Type.__name__=_C
_RaisecomPtpPortEnable_Object=MibTableColumn
raisecomPtpPortEnable=_RaisecomPtpPortEnable_Object((1,3,6,1,4,1,8886,1,26,1,6,1,1),_RaisecomPtpPortEnable_Type())
raisecomPtpPortEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomPtpPortEnable.setStatus(_A)
class _RaisecomPtpPortTransmitProtocol_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3)));namedValues=NamedValues(*(('udp',1),('ethernet',3)))
_RaisecomPtpPortTransmitProtocol_Type.__name__=_C
_RaisecomPtpPortTransmitProtocol_Object=MibTableColumn
raisecomPtpPortTransmitProtocol=_RaisecomPtpPortTransmitProtocol_Object((1,3,6,1,4,1,8886,1,26,1,6,1,2),_RaisecomPtpPortTransmitProtocol_Type())
raisecomPtpPortTransmitProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomPtpPortTransmitProtocol.setStatus(_A)
class _RaisecomPtpPortVlan_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_RaisecomPtpPortVlan_Type.__name__=_C
_RaisecomPtpPortVlan_Object=MibTableColumn
raisecomPtpPortVlan=_RaisecomPtpPortVlan_Object((1,3,6,1,4,1,8886,1,26,1,6,1,3),_RaisecomPtpPortVlan_Type())
raisecomPtpPortVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomPtpPortVlan.setStatus(_A)
_RaisecomPtpPortAsymmetryDelay_Type=Integer32
_RaisecomPtpPortAsymmetryDelay_Object=MibTableColumn
raisecomPtpPortAsymmetryDelay=_RaisecomPtpPortAsymmetryDelay_Object((1,3,6,1,4,1,8886,1,26,1,6,1,4),_RaisecomPtpPortAsymmetryDelay_Type())
raisecomPtpPortAsymmetryDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomPtpPortAsymmetryDelay.setStatus(_A)
if mibBuilder.loadTexts:raisecomPtpPortAsymmetryDelay.setUnits('nanseconds')
_RaisecomPtpClock_ObjectIdentity=ObjectIdentity
raisecomPtpClock=_RaisecomPtpClock_ObjectIdentity((1,3,6,1,4,1,8886,1,26,2))
_RaisecomPtpClockIdentity_Type=PTPClockIdentity
_RaisecomPtpClockIdentity_Object=MibScalar
raisecomPtpClockIdentity=_RaisecomPtpClockIdentity_Object((1,3,6,1,4,1,8886,1,26,2,1),_RaisecomPtpClockIdentity_Type())
raisecomPtpClockIdentity.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpClockIdentity.setStatus(_A)
class _RaisecomPtpClockDomain_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RaisecomPtpClockDomain_Type.__name__=_C
_RaisecomPtpClockDomain_Object=MibScalar
raisecomPtpClockDomain=_RaisecomPtpClockDomain_Object((1,3,6,1,4,1,8886,1,26,2,2),_RaisecomPtpClockDomain_Type())
raisecomPtpClockDomain.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomPtpClockDomain.setStatus(_A)
class _RaisecomPtpClockPriority1_Type(Integer32):defaultValue=128;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RaisecomPtpClockPriority1_Type.__name__=_C
_RaisecomPtpClockPriority1_Object=MibScalar
raisecomPtpClockPriority1=_RaisecomPtpClockPriority1_Object((1,3,6,1,4,1,8886,1,26,2,3),_RaisecomPtpClockPriority1_Type())
raisecomPtpClockPriority1.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomPtpClockPriority1.setStatus(_A)
class _RaisecomPtpClockPriority2_Type(Integer32):defaultValue=128;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RaisecomPtpClockPriority2_Type.__name__=_C
_RaisecomPtpClockPriority2_Object=MibScalar
raisecomPtpClockPriority2=_RaisecomPtpClockPriority2_Object((1,3,6,1,4,1,8886,1,26,2,4),_RaisecomPtpClockPriority2_Type())
raisecomPtpClockPriority2.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomPtpClockPriority2.setStatus(_A)
class _RaisecomPtpClockClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RaisecomPtpClockClass_Type.__name__=_C
_RaisecomPtpClockClass_Object=MibScalar
raisecomPtpClockClass=_RaisecomPtpClockClass_Object((1,3,6,1,4,1,8886,1,26,2,5),_RaisecomPtpClockClass_Type())
raisecomPtpClockClass.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpClockClass.setStatus(_A)
class _RaisecomPtpClockAccuracy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RaisecomPtpClockAccuracy_Type.__name__=_C
_RaisecomPtpClockAccuracy_Object=MibScalar
raisecomPtpClockAccuracy=_RaisecomPtpClockAccuracy_Object((1,3,6,1,4,1,8886,1,26,2,6),_RaisecomPtpClockAccuracy_Type())
raisecomPtpClockAccuracy.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpClockAccuracy.setStatus(_A)
class _RaisecomPtpClockOffsetScaledLogVariance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RaisecomPtpClockOffsetScaledLogVariance_Type.__name__=_C
_RaisecomPtpClockOffsetScaledLogVariance_Object=MibScalar
raisecomPtpClockOffsetScaledLogVariance=_RaisecomPtpClockOffsetScaledLogVariance_Object((1,3,6,1,4,1,8886,1,26,2,7),_RaisecomPtpClockOffsetScaledLogVariance_Type())
raisecomPtpClockOffsetScaledLogVariance.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpClockOffsetScaledLogVariance.setStatus(_A)
class _RaisecomPtpClockNumberPorts_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RaisecomPtpClockNumberPorts_Type.__name__=_C
_RaisecomPtpClockNumberPorts_Object=MibScalar
raisecomPtpClockNumberPorts=_RaisecomPtpClockNumberPorts_Object((1,3,6,1,4,1,8886,1,26,2,8),_RaisecomPtpClockNumberPorts_Type())
raisecomPtpClockNumberPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpClockNumberPorts.setStatus(_A)
class _RaisecomPtpClockSlaveOnly_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('non-slave-only',0),('slave-only',1)))
_RaisecomPtpClockSlaveOnly_Type.__name__=_C
_RaisecomPtpClockSlaveOnly_Object=MibScalar
raisecomPtpClockSlaveOnly=_RaisecomPtpClockSlaveOnly_Object((1,3,6,1,4,1,8886,1,26,2,9),_RaisecomPtpClockSlaveOnly_Type())
raisecomPtpClockSlaveOnly.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomPtpClockSlaveOnly.setStatus(_A)
_RaisecomPtpCurrent_ObjectIdentity=ObjectIdentity
raisecomPtpCurrent=_RaisecomPtpCurrent_ObjectIdentity((1,3,6,1,4,1,8886,1,26,3))
_RaisecomPtpCurrentEndMeanPathDelay_Type=PTPTimeInterval
_RaisecomPtpCurrentEndMeanPathDelay_Object=MibScalar
raisecomPtpCurrentEndMeanPathDelay=_RaisecomPtpCurrentEndMeanPathDelay_Object((1,3,6,1,4,1,8886,1,26,3,1),_RaisecomPtpCurrentEndMeanPathDelay_Type())
raisecomPtpCurrentEndMeanPathDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpCurrentEndMeanPathDelay.setStatus(_A)
_RaisecomPtpCurrentOffsetFromParent_Type=PTPTimeInterval
_RaisecomPtpCurrentOffsetFromParent_Object=MibScalar
raisecomPtpCurrentOffsetFromParent=_RaisecomPtpCurrentOffsetFromParent_Object((1,3,6,1,4,1,8886,1,26,3,2),_RaisecomPtpCurrentOffsetFromParent_Type())
raisecomPtpCurrentOffsetFromParent.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpCurrentOffsetFromParent.setStatus(_A)
class _RaisecomPtpCurrentStepsRemoved_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_RaisecomPtpCurrentStepsRemoved_Type.__name__=_C
_RaisecomPtpCurrentStepsRemoved_Object=MibScalar
raisecomPtpCurrentStepsRemoved=_RaisecomPtpCurrentStepsRemoved_Object((1,3,6,1,4,1,8886,1,26,3,3),_RaisecomPtpCurrentStepsRemoved_Type())
raisecomPtpCurrentStepsRemoved.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpCurrentStepsRemoved.setStatus(_A)
_RaisecomPtpParent_ObjectIdentity=ObjectIdentity
raisecomPtpParent=_RaisecomPtpParent_ObjectIdentity((1,3,6,1,4,1,8886,1,26,4))
_RaisecomPtpParentPortIdentity_Type=PTPPortIdentity
_RaisecomPtpParentPortIdentity_Object=MibScalar
raisecomPtpParentPortIdentity=_RaisecomPtpParentPortIdentity_Object((1,3,6,1,4,1,8886,1,26,4,1),_RaisecomPtpParentPortIdentity_Type())
raisecomPtpParentPortIdentity.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpParentPortIdentity.setStatus(_A)
class _RaisecomPtpParentSatisticsFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('nosatistics',0),('satistics',1)))
_RaisecomPtpParentSatisticsFlag_Type.__name__=_C
_RaisecomPtpParentSatisticsFlag_Object=MibScalar
raisecomPtpParentSatisticsFlag=_RaisecomPtpParentSatisticsFlag_Object((1,3,6,1,4,1,8886,1,26,4,2),_RaisecomPtpParentSatisticsFlag_Type())
raisecomPtpParentSatisticsFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpParentSatisticsFlag.setStatus(_A)
class _RaisecomPtpParentOffsetScaledLogVariance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RaisecomPtpParentOffsetScaledLogVariance_Type.__name__=_C
_RaisecomPtpParentOffsetScaledLogVariance_Object=MibScalar
raisecomPtpParentOffsetScaledLogVariance=_RaisecomPtpParentOffsetScaledLogVariance_Object((1,3,6,1,4,1,8886,1,26,4,3),_RaisecomPtpParentOffsetScaledLogVariance_Type())
raisecomPtpParentOffsetScaledLogVariance.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpParentOffsetScaledLogVariance.setStatus(_A)
_RaisecomPtpParentPhaseChangeRate_Type=Integer32
_RaisecomPtpParentPhaseChangeRate_Object=MibScalar
raisecomPtpParentPhaseChangeRate=_RaisecomPtpParentPhaseChangeRate_Object((1,3,6,1,4,1,8886,1,26,4,4),_RaisecomPtpParentPhaseChangeRate_Type())
raisecomPtpParentPhaseChangeRate.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpParentPhaseChangeRate.setStatus(_A)
_RaisecomPtpGrandmasterIdentity_Type=PTPClockIdentity
_RaisecomPtpGrandmasterIdentity_Object=MibScalar
raisecomPtpGrandmasterIdentity=_RaisecomPtpGrandmasterIdentity_Object((1,3,6,1,4,1,8886,1,26,4,5),_RaisecomPtpGrandmasterIdentity_Type())
raisecomPtpGrandmasterIdentity.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpGrandmasterIdentity.setStatus(_A)
class _RaisecomPtpGrandmasterPriority1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RaisecomPtpGrandmasterPriority1_Type.__name__=_C
_RaisecomPtpGrandmasterPriority1_Object=MibScalar
raisecomPtpGrandmasterPriority1=_RaisecomPtpGrandmasterPriority1_Object((1,3,6,1,4,1,8886,1,26,4,6),_RaisecomPtpGrandmasterPriority1_Type())
raisecomPtpGrandmasterPriority1.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpGrandmasterPriority1.setStatus(_A)
class _RaisecomPtpGrandmasterPriority2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RaisecomPtpGrandmasterPriority2_Type.__name__=_C
_RaisecomPtpGrandmasterPriority2_Object=MibScalar
raisecomPtpGrandmasterPriority2=_RaisecomPtpGrandmasterPriority2_Object((1,3,6,1,4,1,8886,1,26,4,7),_RaisecomPtpGrandmasterPriority2_Type())
raisecomPtpGrandmasterPriority2.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpGrandmasterPriority2.setStatus(_A)
class _RaisecomPtpGrandmasterClockClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RaisecomPtpGrandmasterClockClass_Type.__name__=_C
_RaisecomPtpGrandmasterClockClass_Object=MibScalar
raisecomPtpGrandmasterClockClass=_RaisecomPtpGrandmasterClockClass_Object((1,3,6,1,4,1,8886,1,26,4,8),_RaisecomPtpGrandmasterClockClass_Type())
raisecomPtpGrandmasterClockClass.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpGrandmasterClockClass.setStatus(_A)
class _RaisecomPtpGrandmasterClockAccuracy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RaisecomPtpGrandmasterClockAccuracy_Type.__name__=_C
_RaisecomPtpGrandmasterClockAccuracy_Object=MibScalar
raisecomPtpGrandmasterClockAccuracy=_RaisecomPtpGrandmasterClockAccuracy_Object((1,3,6,1,4,1,8886,1,26,4,9),_RaisecomPtpGrandmasterClockAccuracy_Type())
raisecomPtpGrandmasterClockAccuracy.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpGrandmasterClockAccuracy.setStatus(_A)
class _RaisecomPtpGrandmasterOffsetScaledLogVariance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RaisecomPtpGrandmasterOffsetScaledLogVariance_Type.__name__=_C
_RaisecomPtpGrandmasterOffsetScaledLogVariance_Object=MibScalar
raisecomPtpGrandmasterOffsetScaledLogVariance=_RaisecomPtpGrandmasterOffsetScaledLogVariance_Object((1,3,6,1,4,1,8886,1,26,4,10),_RaisecomPtpGrandmasterOffsetScaledLogVariance_Type())
raisecomPtpGrandmasterOffsetScaledLogVariance.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpGrandmasterOffsetScaledLogVariance.setStatus(_A)
_RaisecomPtpTimeProperty_ObjectIdentity=ObjectIdentity
raisecomPtpTimeProperty=_RaisecomPtpTimeProperty_ObjectIdentity((1,3,6,1,4,1,8886,1,26,5))
class _RaisecomPtpTimeProCurrentUtcOffset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RaisecomPtpTimeProCurrentUtcOffset_Type.__name__=_C
_RaisecomPtpTimeProCurrentUtcOffset_Object=MibScalar
raisecomPtpTimeProCurrentUtcOffset=_RaisecomPtpTimeProCurrentUtcOffset_Object((1,3,6,1,4,1,8886,1,26,5,1),_RaisecomPtpTimeProCurrentUtcOffset_Type())
raisecomPtpTimeProCurrentUtcOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpTimeProCurrentUtcOffset.setStatus(_A)
if mibBuilder.loadTexts:raisecomPtpTimeProCurrentUtcOffset.setUnits('seconds')
class _RaisecomPtpTimeProCurrentUtcOffsetValid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Q,0),('valid',1)))
_RaisecomPtpTimeProCurrentUtcOffsetValid_Type.__name__=_C
_RaisecomPtpTimeProCurrentUtcOffsetValid_Object=MibScalar
raisecomPtpTimeProCurrentUtcOffsetValid=_RaisecomPtpTimeProCurrentUtcOffsetValid_Object((1,3,6,1,4,1,8886,1,26,5,2),_RaisecomPtpTimeProCurrentUtcOffsetValid_Type())
raisecomPtpTimeProCurrentUtcOffsetValid.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpTimeProCurrentUtcOffsetValid.setStatus(_A)
class _RaisecomPtpTimeProLeap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('noleap',0),('leap61',1),('leap59',2)))
_RaisecomPtpTimeProLeap_Type.__name__=_C
_RaisecomPtpTimeProLeap_Object=MibScalar
raisecomPtpTimeProLeap=_RaisecomPtpTimeProLeap_Object((1,3,6,1,4,1,8886,1,26,5,3),_RaisecomPtpTimeProLeap_Type())
raisecomPtpTimeProLeap.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpTimeProLeap.setStatus(_A)
class _RaisecomPtpTimeProTimeFrequencyTraceable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('time',1),('frequency',2),('both',3)))
_RaisecomPtpTimeProTimeFrequencyTraceable_Type.__name__=_C
_RaisecomPtpTimeProTimeFrequencyTraceable_Object=MibScalar
raisecomPtpTimeProTimeFrequencyTraceable=_RaisecomPtpTimeProTimeFrequencyTraceable_Object((1,3,6,1,4,1,8886,1,26,5,4),_RaisecomPtpTimeProTimeFrequencyTraceable_Type())
raisecomPtpTimeProTimeFrequencyTraceable.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpTimeProTimeFrequencyTraceable.setStatus(_A)
class _RaisecomPtpTimeProMatchTimescale_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('noptptime',0),('ptptime',1)))
_RaisecomPtpTimeProMatchTimescale_Type.__name__=_C
_RaisecomPtpTimeProMatchTimescale_Object=MibScalar
raisecomPtpTimeProMatchTimescale=_RaisecomPtpTimeProMatchTimescale_Object((1,3,6,1,4,1,8886,1,26,5,5),_RaisecomPtpTimeProMatchTimescale_Type())
raisecomPtpTimeProMatchTimescale.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpTimeProMatchTimescale.setStatus(_A)
class _RaisecomPtpTimeProTimeSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RaisecomPtpTimeProTimeSource_Type.__name__=_C
_RaisecomPtpTimeProTimeSource_Object=MibScalar
raisecomPtpTimeProTimeSource=_RaisecomPtpTimeProTimeSource_Object((1,3,6,1,4,1,8886,1,26,5,6),_RaisecomPtpTimeProTimeSource_Type())
raisecomPtpTimeProTimeSource.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomPtpTimeProTimeSource.setStatus(_A)
class _RaisecomPtpTimeProTimeSourceOper_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RaisecomPtpTimeProTimeSourceOper_Type.__name__=_C
_RaisecomPtpTimeProTimeSourceOper_Object=MibScalar
raisecomPtpTimeProTimeSourceOper=_RaisecomPtpTimeProTimeSourceOper_Object((1,3,6,1,4,1,8886,1,26,5,7),_RaisecomPtpTimeProTimeSourceOper_Type())
raisecomPtpTimeProTimeSourceOper.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpTimeProTimeSourceOper.setStatus(_A)
_RaisecomPtpPorts_ObjectIdentity=ObjectIdentity
raisecomPtpPorts=_RaisecomPtpPorts_ObjectIdentity((1,3,6,1,4,1,8886,1,26,6))
_RaisecomPtpPortTable_Object=MibTable
raisecomPtpPortTable=_RaisecomPtpPortTable_Object((1,3,6,1,4,1,8886,1,26,6,1))
if mibBuilder.loadTexts:raisecomPtpPortTable.setStatus(_A)
_RaisecomPtpPortEntry_Object=MibTableRow
raisecomPtpPortEntry=_RaisecomPtpPortEntry_Object((1,3,6,1,4,1,8886,1,26,6,1,1))
raisecomPtpPortEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:raisecomPtpPortEntry.setStatus(_A)
_RaisecomPtpPortIdentity_Type=OctetString
_RaisecomPtpPortIdentity_Object=MibTableColumn
raisecomPtpPortIdentity=_RaisecomPtpPortIdentity_Object((1,3,6,1,4,1,8886,1,26,6,1,1,1),_RaisecomPtpPortIdentity_Type())
raisecomPtpPortIdentity.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpPortIdentity.setStatus(_A)
class _RaisecomPtpPortState_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_I,0),('initializing',1),(_R,2),('disabled',3),('listening',4),('premaster',5),(_S,6),(_T,7),('uncalibrated',8),('slave',9)))
_RaisecomPtpPortState_Type.__name__=_C
_RaisecomPtpPortState_Object=MibTableColumn
raisecomPtpPortState=_RaisecomPtpPortState_Object((1,3,6,1,4,1,8886,1,26,6,1,1,2),_RaisecomPtpPortState_Type())
raisecomPtpPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpPortState.setStatus(_A)
class _RaisecomPtpPortStateForce_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,6,7,9)));namedValues=NamedValues(*(('noforce',0),(_S,6),(_T,7),('slave',9)))
_RaisecomPtpPortStateForce_Type.__name__=_C
_RaisecomPtpPortStateForce_Object=MibTableColumn
raisecomPtpPortStateForce=_RaisecomPtpPortStateForce_Object((1,3,6,1,4,1,8886,1,26,6,1,1,3),_RaisecomPtpPortStateForce_Type())
raisecomPtpPortStateForce.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomPtpPortStateForce.setStatus(_A)
class _RaisecomPtpPortDelayMechanism_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_U,1),(_V,2)))
_RaisecomPtpPortDelayMechanism_Type.__name__=_C
_RaisecomPtpPortDelayMechanism_Object=MibTableColumn
raisecomPtpPortDelayMechanism=_RaisecomPtpPortDelayMechanism_Object((1,3,6,1,4,1,8886,1,26,6,1,1,4),_RaisecomPtpPortDelayMechanism_Type())
raisecomPtpPortDelayMechanism.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomPtpPortDelayMechanism.setStatus(_A)
_RaisecomPtpPortPeerMeanPathDelay_Type=PTPTimeInterval
_RaisecomPtpPortPeerMeanPathDelay_Object=MibTableColumn
raisecomPtpPortPeerMeanPathDelay=_RaisecomPtpPortPeerMeanPathDelay_Object((1,3,6,1,4,1,8886,1,26,6,1,1,5),_RaisecomPtpPortPeerMeanPathDelay_Type())
raisecomPtpPortPeerMeanPathDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpPortPeerMeanPathDelay.setStatus(_A)
class _RaisecomPtpPortLogSyncInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-6,-1))
_RaisecomPtpPortLogSyncInterval_Type.__name__=_C
_RaisecomPtpPortLogSyncInterval_Object=MibTableColumn
raisecomPtpPortLogSyncInterval=_RaisecomPtpPortLogSyncInterval_Object((1,3,6,1,4,1,8886,1,26,6,1,1,6),_RaisecomPtpPortLogSyncInterval_Type())
raisecomPtpPortLogSyncInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomPtpPortLogSyncInterval.setStatus(_A)
class _RaisecomPtpPortLogAnnounceInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,4))
_RaisecomPtpPortLogAnnounceInterval_Type.__name__=_C
_RaisecomPtpPortLogAnnounceInterval_Object=MibTableColumn
raisecomPtpPortLogAnnounceInterval=_RaisecomPtpPortLogAnnounceInterval_Object((1,3,6,1,4,1,8886,1,26,6,1,1,7),_RaisecomPtpPortLogAnnounceInterval_Type())
raisecomPtpPortLogAnnounceInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomPtpPortLogAnnounceInterval.setStatus(_A)
class _RaisecomPtpPortLogMinDelayRequestInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-6,-1))
_RaisecomPtpPortLogMinDelayRequestInterval_Type.__name__=_C
_RaisecomPtpPortLogMinDelayRequestInterval_Object=MibTableColumn
raisecomPtpPortLogMinDelayRequestInterval=_RaisecomPtpPortLogMinDelayRequestInterval_Object((1,3,6,1,4,1,8886,1,26,6,1,1,8),_RaisecomPtpPortLogMinDelayRequestInterval_Type())
raisecomPtpPortLogMinDelayRequestInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomPtpPortLogMinDelayRequestInterval.setStatus(_A)
class _RaisecomPtpPortAnnounceReceiptTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,16))
_RaisecomPtpPortAnnounceReceiptTimeout_Type.__name__=_C
_RaisecomPtpPortAnnounceReceiptTimeout_Object=MibTableColumn
raisecomPtpPortAnnounceReceiptTimeout=_RaisecomPtpPortAnnounceReceiptTimeout_Object((1,3,6,1,4,1,8886,1,26,6,1,1,9),_RaisecomPtpPortAnnounceReceiptTimeout_Type())
raisecomPtpPortAnnounceReceiptTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomPtpPortAnnounceReceiptTimeout.setStatus(_A)
class _RaisecomPtpPortLogMinPDelayRequestInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-6,-1))
_RaisecomPtpPortLogMinPDelayRequestInterval_Type.__name__=_C
_RaisecomPtpPortLogMinPDelayRequestInterval_Object=MibTableColumn
raisecomPtpPortLogMinPDelayRequestInterval=_RaisecomPtpPortLogMinPDelayRequestInterval_Object((1,3,6,1,4,1,8886,1,26,6,1,1,10),_RaisecomPtpPortLogMinPDelayRequestInterval_Type())
raisecomPtpPortLogMinPDelayRequestInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomPtpPortLogMinPDelayRequestInterval.setStatus(_A)
class _RaisecomPtpPortVersionNumber_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('v1',1),('v2',2)))
_RaisecomPtpPortVersionNumber_Type.__name__=_C
_RaisecomPtpPortVersionNumber_Object=MibTableColumn
raisecomPtpPortVersionNumber=_RaisecomPtpPortVersionNumber_Object((1,3,6,1,4,1,8886,1,26,6,1,1,11),_RaisecomPtpPortVersionNumber_Type())
raisecomPtpPortVersionNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpPortVersionNumber.setStatus(_A)
_RaisecomPtpPortUnicastMasterMaxIndex_Type=Integer32
_RaisecomPtpPortUnicastMasterMaxIndex_Object=MibTableColumn
raisecomPtpPortUnicastMasterMaxIndex=_RaisecomPtpPortUnicastMasterMaxIndex_Object((1,3,6,1,4,1,8886,1,26,6,1,1,12),_RaisecomPtpPortUnicastMasterMaxIndex_Type())
raisecomPtpPortUnicastMasterMaxIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpPortUnicastMasterMaxIndex.setStatus(_A)
_RaisecomPtpPortUnicastPeerMaxIndex_Type=Integer32
_RaisecomPtpPortUnicastPeerMaxIndex_Object=MibTableColumn
raisecomPtpPortUnicastPeerMaxIndex=_RaisecomPtpPortUnicastPeerMaxIndex_Object((1,3,6,1,4,1,8886,1,26,6,1,1,13),_RaisecomPtpPortUnicastPeerMaxIndex_Type())
raisecomPtpPortUnicastPeerMaxIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpPortUnicastPeerMaxIndex.setStatus(_A)
_RaisecomPtpForeignRecords_ObjectIdentity=ObjectIdentity
raisecomPtpForeignRecords=_RaisecomPtpForeignRecords_ObjectIdentity((1,3,6,1,4,1,8886,1,26,7))
_RaisecomPtpForeignRecordTable_Object=MibTable
raisecomPtpForeignRecordTable=_RaisecomPtpForeignRecordTable_Object((1,3,6,1,4,1,8886,1,26,7,1))
if mibBuilder.loadTexts:raisecomPtpForeignRecordTable.setStatus(_A)
_RaisecomPtpForeignRecordEntry_Object=MibTableRow
raisecomPtpForeignRecordEntry=_RaisecomPtpForeignRecordEntry_Object((1,3,6,1,4,1,8886,1,26,7,1,1))
raisecomPtpForeignRecordEntry.setIndexNames((0,_E,_F),(0,_H,_W))
if mibBuilder.loadTexts:raisecomPtpForeignRecordEntry.setStatus(_A)
class _RaisecomPtpForeignRecordIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_RaisecomPtpForeignRecordIndex_Type.__name__=_C
_RaisecomPtpForeignRecordIndex_Object=MibTableColumn
raisecomPtpForeignRecordIndex=_RaisecomPtpForeignRecordIndex_Object((1,3,6,1,4,1,8886,1,26,7,1,1,1),_RaisecomPtpForeignRecordIndex_Type())
raisecomPtpForeignRecordIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:raisecomPtpForeignRecordIndex.setStatus(_A)
class _RaisecomPtpForeignRecordValid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Q,0),('valid',1)))
_RaisecomPtpForeignRecordValid_Type.__name__=_C
_RaisecomPtpForeignRecordValid_Object=MibTableColumn
raisecomPtpForeignRecordValid=_RaisecomPtpForeignRecordValid_Object((1,3,6,1,4,1,8886,1,26,7,1,1,2),_RaisecomPtpForeignRecordValid_Type())
raisecomPtpForeignRecordValid.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpForeignRecordValid.setStatus(_A)
_RaisecomPtpForeignRecordPortIdentity_Type=PTPPortIdentity
_RaisecomPtpForeignRecordPortIdentity_Object=MibTableColumn
raisecomPtpForeignRecordPortIdentity=_RaisecomPtpForeignRecordPortIdentity_Object((1,3,6,1,4,1,8886,1,26,7,1,1,3),_RaisecomPtpForeignRecordPortIdentity_Type())
raisecomPtpForeignRecordPortIdentity.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpForeignRecordPortIdentity.setStatus(_A)
_RaisecomPtpForeignRecordAnnounceNum_Type=Integer32
_RaisecomPtpForeignRecordAnnounceNum_Object=MibTableColumn
raisecomPtpForeignRecordAnnounceNum=_RaisecomPtpForeignRecordAnnounceNum_Object((1,3,6,1,4,1,8886,1,26,7,1,1,4),_RaisecomPtpForeignRecordAnnounceNum_Type())
raisecomPtpForeignRecordAnnounceNum.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpForeignRecordAnnounceNum.setStatus(_A)
_RaisecomPtpMessageStat_ObjectIdentity=ObjectIdentity
raisecomPtpMessageStat=_RaisecomPtpMessageStat_ObjectIdentity((1,3,6,1,4,1,8886,1,26,8))
_RaisecomPtpMessageStatTable_Object=MibTable
raisecomPtpMessageStatTable=_RaisecomPtpMessageStatTable_Object((1,3,6,1,4,1,8886,1,26,8,1))
if mibBuilder.loadTexts:raisecomPtpMessageStatTable.setStatus(_A)
_RaisecomPtpMessageStatEntry_Object=MibTableRow
raisecomPtpMessageStatEntry=_RaisecomPtpMessageStatEntry_Object((1,3,6,1,4,1,8886,1,26,8,1,1))
raisecomPtpMessageStatEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:raisecomPtpMessageStatEntry.setStatus(_A)
_RaisecomPtpMsgStatSendSync_Type=Integer32
_RaisecomPtpMsgStatSendSync_Object=MibTableColumn
raisecomPtpMsgStatSendSync=_RaisecomPtpMsgStatSendSync_Object((1,3,6,1,4,1,8886,1,26,8,1,1,1),_RaisecomPtpMsgStatSendSync_Type())
raisecomPtpMsgStatSendSync.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpMsgStatSendSync.setStatus(_A)
_RaisecomPtpMsgStatReceiveSync_Type=Integer32
_RaisecomPtpMsgStatReceiveSync_Object=MibTableColumn
raisecomPtpMsgStatReceiveSync=_RaisecomPtpMsgStatReceiveSync_Object((1,3,6,1,4,1,8886,1,26,8,1,1,2),_RaisecomPtpMsgStatReceiveSync_Type())
raisecomPtpMsgStatReceiveSync.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpMsgStatReceiveSync.setStatus(_A)
_RaisecomPtpMsgStatSendAnnounce_Type=Integer32
_RaisecomPtpMsgStatSendAnnounce_Object=MibTableColumn
raisecomPtpMsgStatSendAnnounce=_RaisecomPtpMsgStatSendAnnounce_Object((1,3,6,1,4,1,8886,1,26,8,1,1,3),_RaisecomPtpMsgStatSendAnnounce_Type())
raisecomPtpMsgStatSendAnnounce.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpMsgStatSendAnnounce.setStatus(_A)
_RaisecomPtpMsgStatReceiveAnnounce_Type=Integer32
_RaisecomPtpMsgStatReceiveAnnounce_Object=MibTableColumn
raisecomPtpMsgStatReceiveAnnounce=_RaisecomPtpMsgStatReceiveAnnounce_Object((1,3,6,1,4,1,8886,1,26,8,1,1,4),_RaisecomPtpMsgStatReceiveAnnounce_Type())
raisecomPtpMsgStatReceiveAnnounce.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpMsgStatReceiveAnnounce.setStatus(_A)
_RaisecomPtpMsgStatSendFollowUp_Type=Integer32
_RaisecomPtpMsgStatSendFollowUp_Object=MibTableColumn
raisecomPtpMsgStatSendFollowUp=_RaisecomPtpMsgStatSendFollowUp_Object((1,3,6,1,4,1,8886,1,26,8,1,1,5),_RaisecomPtpMsgStatSendFollowUp_Type())
raisecomPtpMsgStatSendFollowUp.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpMsgStatSendFollowUp.setStatus(_A)
_RaisecomPtpMsgStatReceiveFollowUp_Type=Integer32
_RaisecomPtpMsgStatReceiveFollowUp_Object=MibTableColumn
raisecomPtpMsgStatReceiveFollowUp=_RaisecomPtpMsgStatReceiveFollowUp_Object((1,3,6,1,4,1,8886,1,26,8,1,1,6),_RaisecomPtpMsgStatReceiveFollowUp_Type())
raisecomPtpMsgStatReceiveFollowUp.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpMsgStatReceiveFollowUp.setStatus(_A)
_RaisecomPtpMsgStatSendDelayReq_Type=Integer32
_RaisecomPtpMsgStatSendDelayReq_Object=MibTableColumn
raisecomPtpMsgStatSendDelayReq=_RaisecomPtpMsgStatSendDelayReq_Object((1,3,6,1,4,1,8886,1,26,8,1,1,7),_RaisecomPtpMsgStatSendDelayReq_Type())
raisecomPtpMsgStatSendDelayReq.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpMsgStatSendDelayReq.setStatus(_A)
_RaisecomPtpMsgStatReceiveDelayReq_Type=Integer32
_RaisecomPtpMsgStatReceiveDelayReq_Object=MibTableColumn
raisecomPtpMsgStatReceiveDelayReq=_RaisecomPtpMsgStatReceiveDelayReq_Object((1,3,6,1,4,1,8886,1,26,8,1,1,8),_RaisecomPtpMsgStatReceiveDelayReq_Type())
raisecomPtpMsgStatReceiveDelayReq.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpMsgStatReceiveDelayReq.setStatus(_A)
_RaisecomPtpMsgStatSendDelayResp_Type=Integer32
_RaisecomPtpMsgStatSendDelayResp_Object=MibTableColumn
raisecomPtpMsgStatSendDelayResp=_RaisecomPtpMsgStatSendDelayResp_Object((1,3,6,1,4,1,8886,1,26,8,1,1,9),_RaisecomPtpMsgStatSendDelayResp_Type())
raisecomPtpMsgStatSendDelayResp.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpMsgStatSendDelayResp.setStatus(_A)
_RaisecomPtpMsgStatReceiveDelayResp_Type=Integer32
_RaisecomPtpMsgStatReceiveDelayResp_Object=MibTableColumn
raisecomPtpMsgStatReceiveDelayResp=_RaisecomPtpMsgStatReceiveDelayResp_Object((1,3,6,1,4,1,8886,1,26,8,1,1,10),_RaisecomPtpMsgStatReceiveDelayResp_Type())
raisecomPtpMsgStatReceiveDelayResp.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpMsgStatReceiveDelayResp.setStatus(_A)
_RaisecomPtpMsgStatSendPdelayReq_Type=Integer32
_RaisecomPtpMsgStatSendPdelayReq_Object=MibTableColumn
raisecomPtpMsgStatSendPdelayReq=_RaisecomPtpMsgStatSendPdelayReq_Object((1,3,6,1,4,1,8886,1,26,8,1,1,11),_RaisecomPtpMsgStatSendPdelayReq_Type())
raisecomPtpMsgStatSendPdelayReq.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpMsgStatSendPdelayReq.setStatus(_A)
_RaisecomPtpMsgStatReceivePdelayReq_Type=Integer32
_RaisecomPtpMsgStatReceivePdelayReq_Object=MibTableColumn
raisecomPtpMsgStatReceivePdelayReq=_RaisecomPtpMsgStatReceivePdelayReq_Object((1,3,6,1,4,1,8886,1,26,8,1,1,12),_RaisecomPtpMsgStatReceivePdelayReq_Type())
raisecomPtpMsgStatReceivePdelayReq.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpMsgStatReceivePdelayReq.setStatus(_A)
_RaisecomPtpMsgStatSendPdelayResp_Type=Integer32
_RaisecomPtpMsgStatSendPdelayResp_Object=MibTableColumn
raisecomPtpMsgStatSendPdelayResp=_RaisecomPtpMsgStatSendPdelayResp_Object((1,3,6,1,4,1,8886,1,26,8,1,1,13),_RaisecomPtpMsgStatSendPdelayResp_Type())
raisecomPtpMsgStatSendPdelayResp.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpMsgStatSendPdelayResp.setStatus(_A)
_RaisecomPtpMsgStatReceivePdelayResp_Type=Integer32
_RaisecomPtpMsgStatReceivePdelayResp_Object=MibTableColumn
raisecomPtpMsgStatReceivePdelayResp=_RaisecomPtpMsgStatReceivePdelayResp_Object((1,3,6,1,4,1,8886,1,26,8,1,1,14),_RaisecomPtpMsgStatReceivePdelayResp_Type())
raisecomPtpMsgStatReceivePdelayResp.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpMsgStatReceivePdelayResp.setStatus(_A)
_RaisecomPtpMsgStatSendPdelayRespFUp_Type=Integer32
_RaisecomPtpMsgStatSendPdelayRespFUp_Object=MibTableColumn
raisecomPtpMsgStatSendPdelayRespFUp=_RaisecomPtpMsgStatSendPdelayRespFUp_Object((1,3,6,1,4,1,8886,1,26,8,1,1,15),_RaisecomPtpMsgStatSendPdelayRespFUp_Type())
raisecomPtpMsgStatSendPdelayRespFUp.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpMsgStatSendPdelayRespFUp.setStatus(_A)
_RaisecomPtpMsgStatReceivePdelayRespFUp_Type=Integer32
_RaisecomPtpMsgStatReceivePdelayRespFUp_Object=MibTableColumn
raisecomPtpMsgStatReceivePdelayRespFUp=_RaisecomPtpMsgStatReceivePdelayRespFUp_Object((1,3,6,1,4,1,8886,1,26,8,1,1,16),_RaisecomPtpMsgStatReceivePdelayRespFUp_Type())
raisecomPtpMsgStatReceivePdelayRespFUp.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpMsgStatReceivePdelayRespFUp.setStatus(_A)
_RaisecomPtpMsgStatSendSignaling_Type=Integer32
_RaisecomPtpMsgStatSendSignaling_Object=MibTableColumn
raisecomPtpMsgStatSendSignaling=_RaisecomPtpMsgStatSendSignaling_Object((1,3,6,1,4,1,8886,1,26,8,1,1,17),_RaisecomPtpMsgStatSendSignaling_Type())
raisecomPtpMsgStatSendSignaling.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpMsgStatSendSignaling.setStatus(_A)
_RaisecomPtpMsgStatReceiveSignaling_Type=Integer32
_RaisecomPtpMsgStatReceiveSignaling_Object=MibTableColumn
raisecomPtpMsgStatReceiveSignaling=_RaisecomPtpMsgStatReceiveSignaling_Object((1,3,6,1,4,1,8886,1,26,8,1,1,18),_RaisecomPtpMsgStatReceiveSignaling_Type())
raisecomPtpMsgStatReceiveSignaling.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpMsgStatReceiveSignaling.setStatus(_A)
_RaisecomPtpMsgStatSendManagement_Type=Integer32
_RaisecomPtpMsgStatSendManagement_Object=MibTableColumn
raisecomPtpMsgStatSendManagement=_RaisecomPtpMsgStatSendManagement_Object((1,3,6,1,4,1,8886,1,26,8,1,1,19),_RaisecomPtpMsgStatSendManagement_Type())
raisecomPtpMsgStatSendManagement.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpMsgStatSendManagement.setStatus(_A)
_RaisecomPtpMsgStatReceiveManagement_Type=Integer32
_RaisecomPtpMsgStatReceiveManagement_Object=MibTableColumn
raisecomPtpMsgStatReceiveManagement=_RaisecomPtpMsgStatReceiveManagement_Object((1,3,6,1,4,1,8886,1,26,8,1,1,20),_RaisecomPtpMsgStatReceiveManagement_Type())
raisecomPtpMsgStatReceiveManagement.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpMsgStatReceiveManagement.setStatus(_A)
_RaisecomPtpMsgStatSendError_Type=Integer32
_RaisecomPtpMsgStatSendError_Object=MibTableColumn
raisecomPtpMsgStatSendError=_RaisecomPtpMsgStatSendError_Object((1,3,6,1,4,1,8886,1,26,8,1,1,21),_RaisecomPtpMsgStatSendError_Type())
raisecomPtpMsgStatSendError.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpMsgStatSendError.setStatus(_A)
_RaisecomPtpMsgStatReceiveUnknown_Type=Integer32
_RaisecomPtpMsgStatReceiveUnknown_Object=MibTableColumn
raisecomPtpMsgStatReceiveUnknown=_RaisecomPtpMsgStatReceiveUnknown_Object((1,3,6,1,4,1,8886,1,26,8,1,1,22),_RaisecomPtpMsgStatReceiveUnknown_Type())
raisecomPtpMsgStatReceiveUnknown.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpMsgStatReceiveUnknown.setStatus(_A)
_RaisecomPtpMsgStatSendTotalNum_Type=Integer32
_RaisecomPtpMsgStatSendTotalNum_Object=MibTableColumn
raisecomPtpMsgStatSendTotalNum=_RaisecomPtpMsgStatSendTotalNum_Object((1,3,6,1,4,1,8886,1,26,8,1,1,23),_RaisecomPtpMsgStatSendTotalNum_Type())
raisecomPtpMsgStatSendTotalNum.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpMsgStatSendTotalNum.setStatus(_A)
_RaisecomPtpMsgStatReceiveTotalNum_Type=Integer32
_RaisecomPtpMsgStatReceiveTotalNum_Object=MibTableColumn
raisecomPtpMsgStatReceiveTotalNum=_RaisecomPtpMsgStatReceiveTotalNum_Object((1,3,6,1,4,1,8886,1,26,8,1,1,24),_RaisecomPtpMsgStatReceiveTotalNum_Type())
raisecomPtpMsgStatReceiveTotalNum.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpMsgStatReceiveTotalNum.setStatus(_A)
_RaisecomPtpUnicastAddr_ObjectIdentity=ObjectIdentity
raisecomPtpUnicastAddr=_RaisecomPtpUnicastAddr_ObjectIdentity((1,3,6,1,4,1,8886,1,26,9))
_RaisecomPtpUnicastMasterPoolTable_Object=MibTable
raisecomPtpUnicastMasterPoolTable=_RaisecomPtpUnicastMasterPoolTable_Object((1,3,6,1,4,1,8886,1,26,9,1))
if mibBuilder.loadTexts:raisecomPtpUnicastMasterPoolTable.setStatus(_A)
_RaisecomPtpUnicastMasterPoolEntry_Object=MibTableRow
raisecomPtpUnicastMasterPoolEntry=_RaisecomPtpUnicastMasterPoolEntry_Object((1,3,6,1,4,1,8886,1,26,9,1,1))
raisecomPtpUnicastMasterPoolEntry.setIndexNames((0,_E,_F),(0,_H,_X))
if mibBuilder.loadTexts:raisecomPtpUnicastMasterPoolEntry.setStatus(_A)
_RaisecomPtpUnicastMasterPoolIndex_Type=Integer32
_RaisecomPtpUnicastMasterPoolIndex_Object=MibTableColumn
raisecomPtpUnicastMasterPoolIndex=_RaisecomPtpUnicastMasterPoolIndex_Object((1,3,6,1,4,1,8886,1,26,9,1,1,1),_RaisecomPtpUnicastMasterPoolIndex_Type())
raisecomPtpUnicastMasterPoolIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:raisecomPtpUnicastMasterPoolIndex.setStatus(_A)
_RaisecomPtpUnicastMasterPoolMac_Type=MacAddress
_RaisecomPtpUnicastMasterPoolMac_Object=MibTableColumn
raisecomPtpUnicastMasterPoolMac=_RaisecomPtpUnicastMasterPoolMac_Object((1,3,6,1,4,1,8886,1,26,9,1,1,2),_RaisecomPtpUnicastMasterPoolMac_Type())
raisecomPtpUnicastMasterPoolMac.setMaxAccess(_G)
if mibBuilder.loadTexts:raisecomPtpUnicastMasterPoolMac.setStatus(_A)
class _RaisecomPtpUnicastMasterPoolVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_RaisecomPtpUnicastMasterPoolVlan_Type.__name__=_C
_RaisecomPtpUnicastMasterPoolVlan_Object=MibTableColumn
raisecomPtpUnicastMasterPoolVlan=_RaisecomPtpUnicastMasterPoolVlan_Object((1,3,6,1,4,1,8886,1,26,9,1,1,3),_RaisecomPtpUnicastMasterPoolVlan_Type())
raisecomPtpUnicastMasterPoolVlan.setMaxAccess(_G)
if mibBuilder.loadTexts:raisecomPtpUnicastMasterPoolVlan.setStatus(_A)
_RaisecomPtpUnicastMasterPoolIp_Type=IpAddress
_RaisecomPtpUnicastMasterPoolIp_Object=MibTableColumn
raisecomPtpUnicastMasterPoolIp=_RaisecomPtpUnicastMasterPoolIp_Object((1,3,6,1,4,1,8886,1,26,9,1,1,4),_RaisecomPtpUnicastMasterPoolIp_Type())
raisecomPtpUnicastMasterPoolIp.setMaxAccess(_G)
if mibBuilder.loadTexts:raisecomPtpUnicastMasterPoolIp.setStatus(_A)
_RaisecomPtpUnicastMasterPoolRowStatus_Type=RowStatus
_RaisecomPtpUnicastMasterPoolRowStatus_Object=MibTableColumn
raisecomPtpUnicastMasterPoolRowStatus=_RaisecomPtpUnicastMasterPoolRowStatus_Object((1,3,6,1,4,1,8886,1,26,9,1,1,5),_RaisecomPtpUnicastMasterPoolRowStatus_Type())
raisecomPtpUnicastMasterPoolRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:raisecomPtpUnicastMasterPoolRowStatus.setStatus(_A)
class _RaisecomPtpUnicastMasterPoolFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_I,0),(_K,1),(_L,2),(_M,3),(_N,4)))
_RaisecomPtpUnicastMasterPoolFlag_Type.__name__=_C
_RaisecomPtpUnicastMasterPoolFlag_Object=MibTableColumn
raisecomPtpUnicastMasterPoolFlag=_RaisecomPtpUnicastMasterPoolFlag_Object((1,3,6,1,4,1,8886,1,26,9,1,1,6),_RaisecomPtpUnicastMasterPoolFlag_Type())
raisecomPtpUnicastMasterPoolFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpUnicastMasterPoolFlag.setStatus(_A)
_RaisecomPtpUnicastSlavePoolTable_Object=MibTable
raisecomPtpUnicastSlavePoolTable=_RaisecomPtpUnicastSlavePoolTable_Object((1,3,6,1,4,1,8886,1,26,9,2))
if mibBuilder.loadTexts:raisecomPtpUnicastSlavePoolTable.setStatus(_A)
_RaisecomPtpUnicastSlavePoolEntry_Object=MibTableRow
raisecomPtpUnicastSlavePoolEntry=_RaisecomPtpUnicastSlavePoolEntry_Object((1,3,6,1,4,1,8886,1,26,9,2,1))
raisecomPtpUnicastSlavePoolEntry.setIndexNames((0,_E,_F),(0,_H,_Y))
if mibBuilder.loadTexts:raisecomPtpUnicastSlavePoolEntry.setStatus(_A)
_RaisecomPtpUnicastSlavePoolIndex_Type=Integer32
_RaisecomPtpUnicastSlavePoolIndex_Object=MibTableColumn
raisecomPtpUnicastSlavePoolIndex=_RaisecomPtpUnicastSlavePoolIndex_Object((1,3,6,1,4,1,8886,1,26,9,2,1,1),_RaisecomPtpUnicastSlavePoolIndex_Type())
raisecomPtpUnicastSlavePoolIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:raisecomPtpUnicastSlavePoolIndex.setStatus(_A)
_RaisecomPtpUnicastSlavePoolMac_Type=MacAddress
_RaisecomPtpUnicastSlavePoolMac_Object=MibTableColumn
raisecomPtpUnicastSlavePoolMac=_RaisecomPtpUnicastSlavePoolMac_Object((1,3,6,1,4,1,8886,1,26,9,2,1,2),_RaisecomPtpUnicastSlavePoolMac_Type())
raisecomPtpUnicastSlavePoolMac.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpUnicastSlavePoolMac.setStatus(_A)
class _RaisecomPtpUnicastSlavePoolVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_RaisecomPtpUnicastSlavePoolVlan_Type.__name__=_C
_RaisecomPtpUnicastSlavePoolVlan_Object=MibTableColumn
raisecomPtpUnicastSlavePoolVlan=_RaisecomPtpUnicastSlavePoolVlan_Object((1,3,6,1,4,1,8886,1,26,9,2,1,3),_RaisecomPtpUnicastSlavePoolVlan_Type())
raisecomPtpUnicastSlavePoolVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpUnicastSlavePoolVlan.setStatus(_A)
_RaisecomPtpUnicastSlavePoolIp_Type=IpAddress
_RaisecomPtpUnicastSlavePoolIp_Object=MibTableColumn
raisecomPtpUnicastSlavePoolIp=_RaisecomPtpUnicastSlavePoolIp_Object((1,3,6,1,4,1,8886,1,26,9,2,1,4),_RaisecomPtpUnicastSlavePoolIp_Type())
raisecomPtpUnicastSlavePoolIp.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpUnicastSlavePoolIp.setStatus(_A)
class _RaisecomPtpUnicastSlavePoolFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_I,0),(_K,1),(_L,2),(_M,3),(_N,4)))
_RaisecomPtpUnicastSlavePoolFlag_Type.__name__=_C
_RaisecomPtpUnicastSlavePoolFlag_Object=MibTableColumn
raisecomPtpUnicastSlavePoolFlag=_RaisecomPtpUnicastSlavePoolFlag_Object((1,3,6,1,4,1,8886,1,26,9,2,1,5),_RaisecomPtpUnicastSlavePoolFlag_Type())
raisecomPtpUnicastSlavePoolFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpUnicastSlavePoolFlag.setStatus(_A)
_RaisecomPtpUnicastPeerPoolTable_Object=MibTable
raisecomPtpUnicastPeerPoolTable=_RaisecomPtpUnicastPeerPoolTable_Object((1,3,6,1,4,1,8886,1,26,9,3))
if mibBuilder.loadTexts:raisecomPtpUnicastPeerPoolTable.setStatus(_A)
_RaisecomPtpUnicastPeerPoolEntry_Object=MibTableRow
raisecomPtpUnicastPeerPoolEntry=_RaisecomPtpUnicastPeerPoolEntry_Object((1,3,6,1,4,1,8886,1,26,9,3,1))
raisecomPtpUnicastPeerPoolEntry.setIndexNames((0,_E,_F),(0,_H,_Z))
if mibBuilder.loadTexts:raisecomPtpUnicastPeerPoolEntry.setStatus(_A)
_RaisecomPtpUnicastPeerPoolIndex_Type=Integer32
_RaisecomPtpUnicastPeerPoolIndex_Object=MibTableColumn
raisecomPtpUnicastPeerPoolIndex=_RaisecomPtpUnicastPeerPoolIndex_Object((1,3,6,1,4,1,8886,1,26,9,3,1,1),_RaisecomPtpUnicastPeerPoolIndex_Type())
raisecomPtpUnicastPeerPoolIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:raisecomPtpUnicastPeerPoolIndex.setStatus(_A)
_RaisecomPtpUnicastPeerPoolMac_Type=MacAddress
_RaisecomPtpUnicastPeerPoolMac_Object=MibTableColumn
raisecomPtpUnicastPeerPoolMac=_RaisecomPtpUnicastPeerPoolMac_Object((1,3,6,1,4,1,8886,1,26,9,3,1,2),_RaisecomPtpUnicastPeerPoolMac_Type())
raisecomPtpUnicastPeerPoolMac.setMaxAccess(_G)
if mibBuilder.loadTexts:raisecomPtpUnicastPeerPoolMac.setStatus(_A)
class _RaisecomPtpUnicastPeerPoolVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_RaisecomPtpUnicastPeerPoolVlan_Type.__name__=_C
_RaisecomPtpUnicastPeerPoolVlan_Object=MibTableColumn
raisecomPtpUnicastPeerPoolVlan=_RaisecomPtpUnicastPeerPoolVlan_Object((1,3,6,1,4,1,8886,1,26,9,3,1,3),_RaisecomPtpUnicastPeerPoolVlan_Type())
raisecomPtpUnicastPeerPoolVlan.setMaxAccess(_G)
if mibBuilder.loadTexts:raisecomPtpUnicastPeerPoolVlan.setStatus(_A)
_RaisecomPtpUnicastPeerPoolIp_Type=IpAddress
_RaisecomPtpUnicastPeerPoolIp_Object=MibTableColumn
raisecomPtpUnicastPeerPoolIp=_RaisecomPtpUnicastPeerPoolIp_Object((1,3,6,1,4,1,8886,1,26,9,3,1,4),_RaisecomPtpUnicastPeerPoolIp_Type())
raisecomPtpUnicastPeerPoolIp.setMaxAccess(_G)
if mibBuilder.loadTexts:raisecomPtpUnicastPeerPoolIp.setStatus(_A)
_RaisecomPtpUnicastPeerPoolRowStatus_Type=RowStatus
_RaisecomPtpUnicastPeerPoolRowStatus_Object=MibTableColumn
raisecomPtpUnicastPeerPoolRowStatus=_RaisecomPtpUnicastPeerPoolRowStatus_Object((1,3,6,1,4,1,8886,1,26,9,3,1,5),_RaisecomPtpUnicastPeerPoolRowStatus_Type())
raisecomPtpUnicastPeerPoolRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:raisecomPtpUnicastPeerPoolRowStatus.setStatus(_A)
class _RaisecomPtpUnicastPeerPoolFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_I,0),(_K,1),(_L,2),(_M,3),(_N,4)))
_RaisecomPtpUnicastPeerPoolFlag_Type.__name__=_C
_RaisecomPtpUnicastPeerPoolFlag_Object=MibTableColumn
raisecomPtpUnicastPeerPoolFlag=_RaisecomPtpUnicastPeerPoolFlag_Object((1,3,6,1,4,1,8886,1,26,9,3,1,6),_RaisecomPtpUnicastPeerPoolFlag_Type())
raisecomPtpUnicastPeerPoolFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpUnicastPeerPoolFlag.setStatus(_A)
_RaisecomPtpTClock_ObjectIdentity=ObjectIdentity
raisecomPtpTClock=_RaisecomPtpTClock_ObjectIdentity((1,3,6,1,4,1,8886,1,26,10))
_RaisecomPtpTClockIdentity_Type=PTPClockIdentity
_RaisecomPtpTClockIdentity_Object=MibScalar
raisecomPtpTClockIdentity=_RaisecomPtpTClockIdentity_Object((1,3,6,1,4,1,8886,1,26,10,1),_RaisecomPtpTClockIdentity_Type())
raisecomPtpTClockIdentity.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpTClockIdentity.setStatus(_A)
class _RaisecomPtpTClockNumberPorts_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RaisecomPtpTClockNumberPorts_Type.__name__=_C
_RaisecomPtpTClockNumberPorts_Object=MibScalar
raisecomPtpTClockNumberPorts=_RaisecomPtpTClockNumberPorts_Object((1,3,6,1,4,1,8886,1,26,10,2),_RaisecomPtpTClockNumberPorts_Type())
raisecomPtpTClockNumberPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpTClockNumberPorts.setStatus(_A)
class _RaisecomPtpTClockDelayMechanism_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_U,1),(_V,2)))
_RaisecomPtpTClockDelayMechanism_Type.__name__=_C
_RaisecomPtpTClockDelayMechanism_Object=MibScalar
raisecomPtpTClockDelayMechanism=_RaisecomPtpTClockDelayMechanism_Object((1,3,6,1,4,1,8886,1,26,10,3),_RaisecomPtpTClockDelayMechanism_Type())
raisecomPtpTClockDelayMechanism.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpTClockDelayMechanism.setStatus(_A)
class _RaisecomPtpTClockPrimaryDomain_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('default',0),('alternate-domain1',1),('alternate-domain2',2),('alternate-domain3',3)))
_RaisecomPtpTClockPrimaryDomain_Type.__name__=_C
_RaisecomPtpTClockPrimaryDomain_Object=MibScalar
raisecomPtpTClockPrimaryDomain=_RaisecomPtpTClockPrimaryDomain_Object((1,3,6,1,4,1,8886,1,26,10,4),_RaisecomPtpTClockPrimaryDomain_Type())
raisecomPtpTClockPrimaryDomain.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomPtpTClockPrimaryDomain.setStatus(_A)
_RaisecomPtpTCPorts_ObjectIdentity=ObjectIdentity
raisecomPtpTCPorts=_RaisecomPtpTCPorts_ObjectIdentity((1,3,6,1,4,1,8886,1,26,11))
_RaisecomPtpTCPortTable_Object=MibTable
raisecomPtpTCPortTable=_RaisecomPtpTCPortTable_Object((1,3,6,1,4,1,8886,1,26,11,1))
if mibBuilder.loadTexts:raisecomPtpTCPortTable.setStatus(_A)
_RaisecomPtpTCPortEntry_Object=MibTableRow
raisecomPtpTCPortEntry=_RaisecomPtpTCPortEntry_Object((1,3,6,1,4,1,8886,1,26,11,1,1))
raisecomPtpTCPortEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:raisecomPtpTCPortEntry.setStatus(_A)
_RaisecomPtpTCPortIdentity_Type=OctetString
_RaisecomPtpTCPortIdentity_Object=MibTableColumn
raisecomPtpTCPortIdentity=_RaisecomPtpTCPortIdentity_Object((1,3,6,1,4,1,8886,1,26,11,1,1,1),_RaisecomPtpTCPortIdentity_Type())
raisecomPtpTCPortIdentity.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpTCPortIdentity.setStatus(_A)
class _RaisecomPtpTCPortLogMinPdelayReqInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-6,-1))
_RaisecomPtpTCPortLogMinPdelayReqInterval_Type.__name__=_C
_RaisecomPtpTCPortLogMinPdelayReqInterval_Object=MibTableColumn
raisecomPtpTCPortLogMinPdelayReqInterval=_RaisecomPtpTCPortLogMinPdelayReqInterval_Object((1,3,6,1,4,1,8886,1,26,11,1,1,2),_RaisecomPtpTCPortLogMinPdelayReqInterval_Type())
raisecomPtpTCPortLogMinPdelayReqInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomPtpTCPortLogMinPdelayReqInterval.setStatus(_A)
class _RaisecomPtpTCPortFaultyFlag_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('normal',0),(_R,1)))
_RaisecomPtpTCPortFaultyFlag_Type.__name__=_C
_RaisecomPtpTCPortFaultyFlag_Object=MibTableColumn
raisecomPtpTCPortFaultyFlag=_RaisecomPtpTCPortFaultyFlag_Object((1,3,6,1,4,1,8886,1,26,11,1,1,3),_RaisecomPtpTCPortFaultyFlag_Type())
raisecomPtpTCPortFaultyFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomPtpTCPortFaultyFlag.setStatus(_A)
_RaisecomPtpTCPortPeerMeanPathDelay_Type=PTPTimeInterval
_RaisecomPtpTCPortPeerMeanPathDelay_Object=MibTableColumn
raisecomPtpTCPortPeerMeanPathDelay=_RaisecomPtpTCPortPeerMeanPathDelay_Object((1,3,6,1,4,1,8886,1,26,11,1,1,4),_RaisecomPtpTCPortPeerMeanPathDelay_Type())
raisecomPtpTCPortPeerMeanPathDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomPtpTCPortPeerMeanPathDelay.setStatus(_A)
_RaisecomPtpTraps_ObjectIdentity=ObjectIdentity
raisecomPtpTraps=_RaisecomPtpTraps_ObjectIdentity((1,3,6,1,4,1,8886,1,26,12))
raisecomPtpSyncTrap=NotificationType((1,3,6,1,4,1,8886,1,26,12,15))
raisecomPtpSyncTrap.setObjects(*((_H,_a),(_H,_b)))
if mibBuilder.loadTexts:raisecomPtpSyncTrap.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'PTPTimeStamp':PTPTimeStamp,'PTPTimeInterval':PTPTimeInterval,'PTPClockIdentity':PTPClockIdentity,'PTPPortIdentity':PTPPortIdentity,'raisecomPtp':raisecomPtp,'raisecomPtpGlobal':raisecomPtpGlobal,'raisecomPtpEnable':raisecomPtpEnable,'raisecomPtpClockMode':raisecomPtpClockMode,'raisecomPtpClockUnicastFlag':raisecomPtpClockUnicastFlag,'raisecomPtpClockStepFlag':raisecomPtpClockStepFlag,'raisecomPtpClockStatisticClear':raisecomPtpClockStatisticClear,'raisecomPtpGlobalPortTable':raisecomPtpGlobalPortTable,'raisecomPtpGlobalPortEntry':raisecomPtpGlobalPortEntry,'raisecomPtpPortEnable':raisecomPtpPortEnable,'raisecomPtpPortTransmitProtocol':raisecomPtpPortTransmitProtocol,'raisecomPtpPortVlan':raisecomPtpPortVlan,'raisecomPtpPortAsymmetryDelay':raisecomPtpPortAsymmetryDelay,'raisecomPtpClock':raisecomPtpClock,'raisecomPtpClockIdentity':raisecomPtpClockIdentity,'raisecomPtpClockDomain':raisecomPtpClockDomain,'raisecomPtpClockPriority1':raisecomPtpClockPriority1,'raisecomPtpClockPriority2':raisecomPtpClockPriority2,'raisecomPtpClockClass':raisecomPtpClockClass,'raisecomPtpClockAccuracy':raisecomPtpClockAccuracy,'raisecomPtpClockOffsetScaledLogVariance':raisecomPtpClockOffsetScaledLogVariance,'raisecomPtpClockNumberPorts':raisecomPtpClockNumberPorts,'raisecomPtpClockSlaveOnly':raisecomPtpClockSlaveOnly,'raisecomPtpCurrent':raisecomPtpCurrent,'raisecomPtpCurrentEndMeanPathDelay':raisecomPtpCurrentEndMeanPathDelay,'raisecomPtpCurrentOffsetFromParent':raisecomPtpCurrentOffsetFromParent,'raisecomPtpCurrentStepsRemoved':raisecomPtpCurrentStepsRemoved,'raisecomPtpParent':raisecomPtpParent,'raisecomPtpParentPortIdentity':raisecomPtpParentPortIdentity,'raisecomPtpParentSatisticsFlag':raisecomPtpParentSatisticsFlag,'raisecomPtpParentOffsetScaledLogVariance':raisecomPtpParentOffsetScaledLogVariance,'raisecomPtpParentPhaseChangeRate':raisecomPtpParentPhaseChangeRate,'raisecomPtpGrandmasterIdentity':raisecomPtpGrandmasterIdentity,'raisecomPtpGrandmasterPriority1':raisecomPtpGrandmasterPriority1,'raisecomPtpGrandmasterPriority2':raisecomPtpGrandmasterPriority2,'raisecomPtpGrandmasterClockClass':raisecomPtpGrandmasterClockClass,'raisecomPtpGrandmasterClockAccuracy':raisecomPtpGrandmasterClockAccuracy,'raisecomPtpGrandmasterOffsetScaledLogVariance':raisecomPtpGrandmasterOffsetScaledLogVariance,'raisecomPtpTimeProperty':raisecomPtpTimeProperty,'raisecomPtpTimeProCurrentUtcOffset':raisecomPtpTimeProCurrentUtcOffset,'raisecomPtpTimeProCurrentUtcOffsetValid':raisecomPtpTimeProCurrentUtcOffsetValid,'raisecomPtpTimeProLeap':raisecomPtpTimeProLeap,'raisecomPtpTimeProTimeFrequencyTraceable':raisecomPtpTimeProTimeFrequencyTraceable,'raisecomPtpTimeProMatchTimescale':raisecomPtpTimeProMatchTimescale,'raisecomPtpTimeProTimeSource':raisecomPtpTimeProTimeSource,'raisecomPtpTimeProTimeSourceOper':raisecomPtpTimeProTimeSourceOper,'raisecomPtpPorts':raisecomPtpPorts,'raisecomPtpPortTable':raisecomPtpPortTable,'raisecomPtpPortEntry':raisecomPtpPortEntry,_b:raisecomPtpPortIdentity,_a:raisecomPtpPortState,'raisecomPtpPortStateForce':raisecomPtpPortStateForce,'raisecomPtpPortDelayMechanism':raisecomPtpPortDelayMechanism,'raisecomPtpPortPeerMeanPathDelay':raisecomPtpPortPeerMeanPathDelay,'raisecomPtpPortLogSyncInterval':raisecomPtpPortLogSyncInterval,'raisecomPtpPortLogAnnounceInterval':raisecomPtpPortLogAnnounceInterval,'raisecomPtpPortLogMinDelayRequestInterval':raisecomPtpPortLogMinDelayRequestInterval,'raisecomPtpPortAnnounceReceiptTimeout':raisecomPtpPortAnnounceReceiptTimeout,'raisecomPtpPortLogMinPDelayRequestInterval':raisecomPtpPortLogMinPDelayRequestInterval,'raisecomPtpPortVersionNumber':raisecomPtpPortVersionNumber,'raisecomPtpPortUnicastMasterMaxIndex':raisecomPtpPortUnicastMasterMaxIndex,'raisecomPtpPortUnicastPeerMaxIndex':raisecomPtpPortUnicastPeerMaxIndex,'raisecomPtpForeignRecords':raisecomPtpForeignRecords,'raisecomPtpForeignRecordTable':raisecomPtpForeignRecordTable,'raisecomPtpForeignRecordEntry':raisecomPtpForeignRecordEntry,_W:raisecomPtpForeignRecordIndex,'raisecomPtpForeignRecordValid':raisecomPtpForeignRecordValid,'raisecomPtpForeignRecordPortIdentity':raisecomPtpForeignRecordPortIdentity,'raisecomPtpForeignRecordAnnounceNum':raisecomPtpForeignRecordAnnounceNum,'raisecomPtpMessageStat':raisecomPtpMessageStat,'raisecomPtpMessageStatTable':raisecomPtpMessageStatTable,'raisecomPtpMessageStatEntry':raisecomPtpMessageStatEntry,'raisecomPtpMsgStatSendSync':raisecomPtpMsgStatSendSync,'raisecomPtpMsgStatReceiveSync':raisecomPtpMsgStatReceiveSync,'raisecomPtpMsgStatSendAnnounce':raisecomPtpMsgStatSendAnnounce,'raisecomPtpMsgStatReceiveAnnounce':raisecomPtpMsgStatReceiveAnnounce,'raisecomPtpMsgStatSendFollowUp':raisecomPtpMsgStatSendFollowUp,'raisecomPtpMsgStatReceiveFollowUp':raisecomPtpMsgStatReceiveFollowUp,'raisecomPtpMsgStatSendDelayReq':raisecomPtpMsgStatSendDelayReq,'raisecomPtpMsgStatReceiveDelayReq':raisecomPtpMsgStatReceiveDelayReq,'raisecomPtpMsgStatSendDelayResp':raisecomPtpMsgStatSendDelayResp,'raisecomPtpMsgStatReceiveDelayResp':raisecomPtpMsgStatReceiveDelayResp,'raisecomPtpMsgStatSendPdelayReq':raisecomPtpMsgStatSendPdelayReq,'raisecomPtpMsgStatReceivePdelayReq':raisecomPtpMsgStatReceivePdelayReq,'raisecomPtpMsgStatSendPdelayResp':raisecomPtpMsgStatSendPdelayResp,'raisecomPtpMsgStatReceivePdelayResp':raisecomPtpMsgStatReceivePdelayResp,'raisecomPtpMsgStatSendPdelayRespFUp':raisecomPtpMsgStatSendPdelayRespFUp,'raisecomPtpMsgStatReceivePdelayRespFUp':raisecomPtpMsgStatReceivePdelayRespFUp,'raisecomPtpMsgStatSendSignaling':raisecomPtpMsgStatSendSignaling,'raisecomPtpMsgStatReceiveSignaling':raisecomPtpMsgStatReceiveSignaling,'raisecomPtpMsgStatSendManagement':raisecomPtpMsgStatSendManagement,'raisecomPtpMsgStatReceiveManagement':raisecomPtpMsgStatReceiveManagement,'raisecomPtpMsgStatSendError':raisecomPtpMsgStatSendError,'raisecomPtpMsgStatReceiveUnknown':raisecomPtpMsgStatReceiveUnknown,'raisecomPtpMsgStatSendTotalNum':raisecomPtpMsgStatSendTotalNum,'raisecomPtpMsgStatReceiveTotalNum':raisecomPtpMsgStatReceiveTotalNum,'raisecomPtpUnicastAddr':raisecomPtpUnicastAddr,'raisecomPtpUnicastMasterPoolTable':raisecomPtpUnicastMasterPoolTable,'raisecomPtpUnicastMasterPoolEntry':raisecomPtpUnicastMasterPoolEntry,_X:raisecomPtpUnicastMasterPoolIndex,'raisecomPtpUnicastMasterPoolMac':raisecomPtpUnicastMasterPoolMac,'raisecomPtpUnicastMasterPoolVlan':raisecomPtpUnicastMasterPoolVlan,'raisecomPtpUnicastMasterPoolIp':raisecomPtpUnicastMasterPoolIp,'raisecomPtpUnicastMasterPoolRowStatus':raisecomPtpUnicastMasterPoolRowStatus,'raisecomPtpUnicastMasterPoolFlag':raisecomPtpUnicastMasterPoolFlag,'raisecomPtpUnicastSlavePoolTable':raisecomPtpUnicastSlavePoolTable,'raisecomPtpUnicastSlavePoolEntry':raisecomPtpUnicastSlavePoolEntry,_Y:raisecomPtpUnicastSlavePoolIndex,'raisecomPtpUnicastSlavePoolMac':raisecomPtpUnicastSlavePoolMac,'raisecomPtpUnicastSlavePoolVlan':raisecomPtpUnicastSlavePoolVlan,'raisecomPtpUnicastSlavePoolIp':raisecomPtpUnicastSlavePoolIp,'raisecomPtpUnicastSlavePoolFlag':raisecomPtpUnicastSlavePoolFlag,'raisecomPtpUnicastPeerPoolTable':raisecomPtpUnicastPeerPoolTable,'raisecomPtpUnicastPeerPoolEntry':raisecomPtpUnicastPeerPoolEntry,_Z:raisecomPtpUnicastPeerPoolIndex,'raisecomPtpUnicastPeerPoolMac':raisecomPtpUnicastPeerPoolMac,'raisecomPtpUnicastPeerPoolVlan':raisecomPtpUnicastPeerPoolVlan,'raisecomPtpUnicastPeerPoolIp':raisecomPtpUnicastPeerPoolIp,'raisecomPtpUnicastPeerPoolRowStatus':raisecomPtpUnicastPeerPoolRowStatus,'raisecomPtpUnicastPeerPoolFlag':raisecomPtpUnicastPeerPoolFlag,'raisecomPtpTClock':raisecomPtpTClock,'raisecomPtpTClockIdentity':raisecomPtpTClockIdentity,'raisecomPtpTClockNumberPorts':raisecomPtpTClockNumberPorts,'raisecomPtpTClockDelayMechanism':raisecomPtpTClockDelayMechanism,'raisecomPtpTClockPrimaryDomain':raisecomPtpTClockPrimaryDomain,'raisecomPtpTCPorts':raisecomPtpTCPorts,'raisecomPtpTCPortTable':raisecomPtpTCPortTable,'raisecomPtpTCPortEntry':raisecomPtpTCPortEntry,'raisecomPtpTCPortIdentity':raisecomPtpTCPortIdentity,'raisecomPtpTCPortLogMinPdelayReqInterval':raisecomPtpTCPortLogMinPdelayReqInterval,'raisecomPtpTCPortFaultyFlag':raisecomPtpTCPortFaultyFlag,'raisecomPtpTCPortPeerMeanPathDelay':raisecomPtpTCPortPeerMeanPathDelay,'raisecomPtpTraps':raisecomPtpTraps,'raisecomPtpSyncTrap':raisecomPtpSyncTrap})