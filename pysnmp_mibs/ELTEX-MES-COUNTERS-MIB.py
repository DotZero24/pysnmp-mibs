_P='eltCountersQosDP'
_O='eltCountersQosQueueIndex'
_N='eltCountersQosIfIndex'
_M='rlQosAceTidxIndex'
_L='rlQosAceTidxAclIndex'
_K='PortList'
_J='not-accessible'
_I='RADLAN-QOS-CLI-MIB'
_H='ELTEX-MES-COUNTERS-MIB'
_G='Integer32'
_F='00'
_E='OctetString'
_D='read-only'
_C='TruthValue'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltMesCountersMIB,=mibBuilder.importSymbols('ELTEX-MES-MNG-MIB','eltMesCountersMIB')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB',_K)
rlQosAceTidxAclIndex,rlQosAceTidxIndex=mibBuilder.importSymbols(_I,_L,_M)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_C)
_EltMesCountersMIBObjects_ObjectIdentity=ObjectIdentity
eltMesCountersMIBObjects=_EltMesCountersMIBObjects_ObjectIdentity((1,3,6,1,4,1,35265,1,23,1,8,1))
_EltMesCountersGlobal_ObjectIdentity=ObjectIdentity
eltMesCountersGlobal=_EltMesCountersGlobal_ObjectIdentity((1,3,6,1,4,1,35265,1,23,1,8,1,1))
_EltMesCountersVlan_ObjectIdentity=ObjectIdentity
eltMesCountersVlan=_EltMesCountersVlan_ObjectIdentity((1,3,6,1,4,1,35265,1,23,1,8,1,1,1))
class _EltCountersVlanLowIn_Type(TruthValue):defaultValue=2
_EltCountersVlanLowIn_Type.__name__=_C
_EltCountersVlanLowIn_Object=MibScalar
eltCountersVlanLowIn=_EltCountersVlanLowIn_Object((1,3,6,1,4,1,35265,1,23,1,8,1,1,1,1),_EltCountersVlanLowIn_Type())
eltCountersVlanLowIn.setMaxAccess(_B)
if mibBuilder.loadTexts:eltCountersVlanLowIn.setStatus(_A)
class _EltCountersVlanHighIn_Type(TruthValue):defaultValue=2
_EltCountersVlanHighIn_Type.__name__=_C
_EltCountersVlanHighIn_Object=MibScalar
eltCountersVlanHighIn=_EltCountersVlanHighIn_Object((1,3,6,1,4,1,35265,1,23,1,8,1,1,1,2),_EltCountersVlanHighIn_Type())
eltCountersVlanHighIn.setMaxAccess(_B)
if mibBuilder.loadTexts:eltCountersVlanHighIn.setStatus(_A)
class _EltCountersVlanLowOut_Type(TruthValue):defaultValue=2
_EltCountersVlanLowOut_Type.__name__=_C
_EltCountersVlanLowOut_Object=MibScalar
eltCountersVlanLowOut=_EltCountersVlanLowOut_Object((1,3,6,1,4,1,35265,1,23,1,8,1,1,1,3),_EltCountersVlanLowOut_Type())
eltCountersVlanLowOut.setMaxAccess(_B)
if mibBuilder.loadTexts:eltCountersVlanLowOut.setStatus(_A)
class _EltCountersVlanHighOut_Type(TruthValue):defaultValue=2
_EltCountersVlanHighOut_Type.__name__=_C
_EltCountersVlanHighOut_Object=MibScalar
eltCountersVlanHighOut=_EltCountersVlanHighOut_Object((1,3,6,1,4,1,35265,1,23,1,8,1,1,1,4),_EltCountersVlanHighOut_Type())
eltCountersVlanHighOut.setMaxAccess(_B)
if mibBuilder.loadTexts:eltCountersVlanHighOut.setStatus(_A)
class _EltCountersVlanClear1to1023_Type(OctetString):defaultHexValue=_F;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_EltCountersVlanClear1to1023_Type.__name__=_E
_EltCountersVlanClear1to1023_Object=MibScalar
eltCountersVlanClear1to1023=_EltCountersVlanClear1to1023_Object((1,3,6,1,4,1,35265,1,23,1,8,1,1,1,5),_EltCountersVlanClear1to1023_Type())
eltCountersVlanClear1to1023.setMaxAccess(_B)
if mibBuilder.loadTexts:eltCountersVlanClear1to1023.setStatus(_A)
class _EltCountersVlanClear1024to2047_Type(OctetString):defaultHexValue=_F;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_EltCountersVlanClear1024to2047_Type.__name__=_E
_EltCountersVlanClear1024to2047_Object=MibScalar
eltCountersVlanClear1024to2047=_EltCountersVlanClear1024to2047_Object((1,3,6,1,4,1,35265,1,23,1,8,1,1,1,6),_EltCountersVlanClear1024to2047_Type())
eltCountersVlanClear1024to2047.setMaxAccess(_B)
if mibBuilder.loadTexts:eltCountersVlanClear1024to2047.setStatus(_A)
class _EltCountersVlanClear2048to3071_Type(OctetString):defaultHexValue=_F;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_EltCountersVlanClear2048to3071_Type.__name__=_E
_EltCountersVlanClear2048to3071_Object=MibScalar
eltCountersVlanClear2048to3071=_EltCountersVlanClear2048to3071_Object((1,3,6,1,4,1,35265,1,23,1,8,1,1,1,7),_EltCountersVlanClear2048to3071_Type())
eltCountersVlanClear2048to3071.setMaxAccess(_B)
if mibBuilder.loadTexts:eltCountersVlanClear2048to3071.setStatus(_A)
class _EltCountersVlanClear3072to4094_Type(OctetString):defaultHexValue=_F;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_EltCountersVlanClear3072to4094_Type.__name__=_E
_EltCountersVlanClear3072to4094_Object=MibScalar
eltCountersVlanClear3072to4094=_EltCountersVlanClear3072to4094_Object((1,3,6,1,4,1,35265,1,23,1,8,1,1,1,8),_EltCountersVlanClear3072to4094_Type())
eltCountersVlanClear3072to4094.setMaxAccess(_B)
if mibBuilder.loadTexts:eltCountersVlanClear3072to4094.setStatus(_A)
_EltMesCountersQos_ObjectIdentity=ObjectIdentity
eltMesCountersQos=_EltMesCountersQos_ObjectIdentity((1,3,6,1,4,1,35265,1,23,1,8,1,1,2))
class _EltCountersQosStatisticsEnable_Type(TruthValue):defaultValue=2
_EltCountersQosStatisticsEnable_Type.__name__=_C
_EltCountersQosStatisticsEnable_Object=MibScalar
eltCountersQosStatisticsEnable=_EltCountersQosStatisticsEnable_Object((1,3,6,1,4,1,35265,1,23,1,8,1,1,2,1),_EltCountersQosStatisticsEnable_Type())
eltCountersQosStatisticsEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:eltCountersQosStatisticsEnable.setStatus(_A)
class _EltCountersQosStatisticsClear_Type(PortList):defaultHexValue=_F
_EltCountersQosStatisticsClear_Type.__name__=_K
_EltCountersQosStatisticsClear_Object=MibScalar
eltCountersQosStatisticsClear=_EltCountersQosStatisticsClear_Object((1,3,6,1,4,1,35265,1,23,1,8,1,1,2,2),_EltCountersQosStatisticsClear_Type())
eltCountersQosStatisticsClear.setMaxAccess(_B)
if mibBuilder.loadTexts:eltCountersQosStatisticsClear.setStatus(_A)
_EltMesCountersAce_ObjectIdentity=ObjectIdentity
eltMesCountersAce=_EltMesCountersAce_ObjectIdentity((1,3,6,1,4,1,35265,1,23,1,8,1,1,3))
class _EltCountersPortAceStatisticsEnable_Type(TruthValue):defaultValue=2
_EltCountersPortAceStatisticsEnable_Type.__name__=_C
_EltCountersPortAceStatisticsEnable_Object=MibScalar
eltCountersPortAceStatisticsEnable=_EltCountersPortAceStatisticsEnable_Object((1,3,6,1,4,1,35265,1,23,1,8,1,1,3,1),_EltCountersPortAceStatisticsEnable_Type())
eltCountersPortAceStatisticsEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:eltCountersPortAceStatisticsEnable.setStatus(_A)
class _EltCountersVlanAceStatisticsEnable_Type(TruthValue):defaultValue=2
_EltCountersVlanAceStatisticsEnable_Type.__name__=_C
_EltCountersVlanAceStatisticsEnable_Object=MibScalar
eltCountersVlanAceStatisticsEnable=_EltCountersVlanAceStatisticsEnable_Object((1,3,6,1,4,1,35265,1,23,1,8,1,1,3,2),_EltCountersVlanAceStatisticsEnable_Type())
eltCountersVlanAceStatisticsEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:eltCountersVlanAceStatisticsEnable.setStatus(_A)
_EltCountersAceStatisticsClear_Type=TruthValue
_EltCountersAceStatisticsClear_Object=MibScalar
eltCountersAceStatisticsClear=_EltCountersAceStatisticsClear_Object((1,3,6,1,4,1,35265,1,23,1,8,1,1,3,3),_EltCountersAceStatisticsClear_Type())
eltCountersAceStatisticsClear.setMaxAccess(_B)
if mibBuilder.loadTexts:eltCountersAceStatisticsClear.setStatus(_A)
_EltMesCountersStatistics_ObjectIdentity=ObjectIdentity
eltMesCountersStatistics=_EltMesCountersStatistics_ObjectIdentity((1,3,6,1,4,1,35265,1,23,1,8,1,2))
_EltMesCountersQosStatistics_ObjectIdentity=ObjectIdentity
eltMesCountersQosStatistics=_EltMesCountersQosStatistics_ObjectIdentity((1,3,6,1,4,1,35265,1,23,1,8,1,2,1))
_EltCountersQosIfQueueTable_Object=MibTable
eltCountersQosIfQueueTable=_EltCountersQosIfQueueTable_Object((1,3,6,1,4,1,35265,1,23,1,8,1,2,1,1))
if mibBuilder.loadTexts:eltCountersQosIfQueueTable.setStatus(_A)
_EltCountersQosIfQueueEntry_Object=MibTableRow
eltCountersQosIfQueueEntry=_EltCountersQosIfQueueEntry_Object((1,3,6,1,4,1,35265,1,23,1,8,1,2,1,1,1))
eltCountersQosIfQueueEntry.setIndexNames((0,_H,_N),(0,_H,_O),(0,_H,_P))
if mibBuilder.loadTexts:eltCountersQosIfQueueEntry.setStatus(_A)
_EltCountersQosIfIndex_Type=InterfaceIndex
_EltCountersQosIfIndex_Object=MibTableColumn
eltCountersQosIfIndex=_EltCountersQosIfIndex_Object((1,3,6,1,4,1,35265,1,23,1,8,1,2,1,1,1,1),_EltCountersQosIfIndex_Type())
eltCountersQosIfIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:eltCountersQosIfIndex.setStatus(_A)
class _EltCountersQosQueueIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_EltCountersQosQueueIndex_Type.__name__=_G
_EltCountersQosQueueIndex_Object=MibTableColumn
eltCountersQosQueueIndex=_EltCountersQosQueueIndex_Object((1,3,6,1,4,1,35265,1,23,1,8,1,2,1,1,1,2),_EltCountersQosQueueIndex_Type())
eltCountersQosQueueIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:eltCountersQosQueueIndex.setStatus(_A)
class _EltCountersQosDP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_EltCountersQosDP_Type.__name__=_G
_EltCountersQosDP_Object=MibTableColumn
eltCountersQosDP=_EltCountersQosDP_Object((1,3,6,1,4,1,35265,1,23,1,8,1,2,1,1,1,3),_EltCountersQosDP_Type())
eltCountersQosDP.setMaxAccess(_J)
if mibBuilder.loadTexts:eltCountersQosDP.setStatus(_A)
_EltCountersQosOctetsDroppedCounter_Type=Counter64
_EltCountersQosOctetsDroppedCounter_Object=MibTableColumn
eltCountersQosOctetsDroppedCounter=_EltCountersQosOctetsDroppedCounter_Object((1,3,6,1,4,1,35265,1,23,1,8,1,2,1,1,1,4),_EltCountersQosOctetsDroppedCounter_Type())
eltCountersQosOctetsDroppedCounter.setMaxAccess(_D)
if mibBuilder.loadTexts:eltCountersQosOctetsDroppedCounter.setStatus(_A)
_EltCountersQosPktsDroppedCounter_Type=Counter64
_EltCountersQosPktsDroppedCounter_Object=MibTableColumn
eltCountersQosPktsDroppedCounter=_EltCountersQosPktsDroppedCounter_Object((1,3,6,1,4,1,35265,1,23,1,8,1,2,1,1,1,5),_EltCountersQosPktsDroppedCounter_Type())
eltCountersQosPktsDroppedCounter.setMaxAccess(_D)
if mibBuilder.loadTexts:eltCountersQosPktsDroppedCounter.setStatus(_A)
_EltCountersQosOctetsPassedCounter_Type=Counter64
_EltCountersQosOctetsPassedCounter_Object=MibTableColumn
eltCountersQosOctetsPassedCounter=_EltCountersQosOctetsPassedCounter_Object((1,3,6,1,4,1,35265,1,23,1,8,1,2,1,1,1,6),_EltCountersQosOctetsPassedCounter_Type())
eltCountersQosOctetsPassedCounter.setMaxAccess(_D)
if mibBuilder.loadTexts:eltCountersQosOctetsPassedCounter.setStatus(_A)
_EltCountersQosPktsPassedCounter_Type=Counter64
_EltCountersQosPktsPassedCounter_Object=MibTableColumn
eltCountersQosPktsPassedCounter=_EltCountersQosPktsPassedCounter_Object((1,3,6,1,4,1,35265,1,23,1,8,1,2,1,1,1,7),_EltCountersQosPktsPassedCounter_Type())
eltCountersQosPktsPassedCounter.setMaxAccess(_D)
if mibBuilder.loadTexts:eltCountersQosPktsPassedCounter.setStatus(_A)
_EltMesCountersAceStatistics_ObjectIdentity=ObjectIdentity
eltMesCountersAceStatistics=_EltMesCountersAceStatistics_ObjectIdentity((1,3,6,1,4,1,35265,1,23,1,8,1,2,2))
_EltCountersAceTable_Object=MibTable
eltCountersAceTable=_EltCountersAceTable_Object((1,3,6,1,4,1,35265,1,23,1,8,1,2,2,1))
if mibBuilder.loadTexts:eltCountersAceTable.setStatus(_A)
_EltCountersAceEntry_Object=MibTableRow
eltCountersAceEntry=_EltCountersAceEntry_Object((1,3,6,1,4,1,35265,1,23,1,8,1,2,2,1,1))
eltCountersAceEntry.setIndexNames((0,_I,_L),(0,_I,_M))
if mibBuilder.loadTexts:eltCountersAceEntry.setStatus(_A)
class _EltCountersAceHitCounterStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_EltCountersAceHitCounterStatus_Type.__name__=_G
_EltCountersAceHitCounterStatus_Object=MibTableColumn
eltCountersAceHitCounterStatus=_EltCountersAceHitCounterStatus_Object((1,3,6,1,4,1,35265,1,23,1,8,1,2,2,1,1,1),_EltCountersAceHitCounterStatus_Type())
eltCountersAceHitCounterStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:eltCountersAceHitCounterStatus.setStatus(_A)
_EltCountersAceHitCounterValue_Type=Counter64
_EltCountersAceHitCounterValue_Object=MibTableColumn
eltCountersAceHitCounterValue=_EltCountersAceHitCounterValue_Object((1,3,6,1,4,1,35265,1,23,1,8,1,2,2,1,1,2),_EltCountersAceHitCounterValue_Type())
eltCountersAceHitCounterValue.setMaxAccess(_D)
if mibBuilder.loadTexts:eltCountersAceHitCounterValue.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'eltMesCountersMIBObjects':eltMesCountersMIBObjects,'eltMesCountersGlobal':eltMesCountersGlobal,'eltMesCountersVlan':eltMesCountersVlan,'eltCountersVlanLowIn':eltCountersVlanLowIn,'eltCountersVlanHighIn':eltCountersVlanHighIn,'eltCountersVlanLowOut':eltCountersVlanLowOut,'eltCountersVlanHighOut':eltCountersVlanHighOut,'eltCountersVlanClear1to1023':eltCountersVlanClear1to1023,'eltCountersVlanClear1024to2047':eltCountersVlanClear1024to2047,'eltCountersVlanClear2048to3071':eltCountersVlanClear2048to3071,'eltCountersVlanClear3072to4094':eltCountersVlanClear3072to4094,'eltMesCountersQos':eltMesCountersQos,'eltCountersQosStatisticsEnable':eltCountersQosStatisticsEnable,'eltCountersQosStatisticsClear':eltCountersQosStatisticsClear,'eltMesCountersAce':eltMesCountersAce,'eltCountersPortAceStatisticsEnable':eltCountersPortAceStatisticsEnable,'eltCountersVlanAceStatisticsEnable':eltCountersVlanAceStatisticsEnable,'eltCountersAceStatisticsClear':eltCountersAceStatisticsClear,'eltMesCountersStatistics':eltMesCountersStatistics,'eltMesCountersQosStatistics':eltMesCountersQosStatistics,'eltCountersQosIfQueueTable':eltCountersQosIfQueueTable,'eltCountersQosIfQueueEntry':eltCountersQosIfQueueEntry,_N:eltCountersQosIfIndex,_O:eltCountersQosQueueIndex,_P:eltCountersQosDP,'eltCountersQosOctetsDroppedCounter':eltCountersQosOctetsDroppedCounter,'eltCountersQosPktsDroppedCounter':eltCountersQosPktsDroppedCounter,'eltCountersQosOctetsPassedCounter':eltCountersQosOctetsPassedCounter,'eltCountersQosPktsPassedCounter':eltCountersQosPktsPassedCounter,'eltMesCountersAceStatistics':eltMesCountersAceStatistics,'eltCountersAceTable':eltCountersAceTable,'eltCountersAceEntry':eltCountersAceEntry,'eltCountersAceHitCounterStatus':eltCountersAceHitCounterStatus,'eltCountersAceHitCounterValue':eltCountersAceHitCounterValue})