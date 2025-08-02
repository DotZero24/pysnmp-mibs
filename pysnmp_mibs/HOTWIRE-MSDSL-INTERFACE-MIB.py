_b='msdslPortConfigAllocMethodIfIndex'
_a='msdslFracPortTS'
_Z='msdslFracPortIndex'
_Y='msdslG703WorstIntervalIfIndex'
_X='msdsldsx1WorstIntervalIfIndex'
_W='msdslFarEndIntervalPerfNumber'
_V='msdslFarEndIntervalPerfIfIndex'
_U='msdslFarEndCurrentPerfIfIndex'
_T='msdslIntervalPerfNumber'
_S='msdslIntervalPerfIfIndex'
_R='msdslCurrentPerfIfIndex'
_Q='msdslFarEndWorstIntervalIfIndex'
_P='msdslFarEndIntervalNumber'
_O='msdslFarEndIntervalIfIndex'
_N='msdslFarEndCurrentIfIndex'
_M='msdslWorstIntervalIfIndex'
_L='msdslIntervalNumber'
_K='msdslIntervalIfIndex'
_J='msdslCurrentIfIndex'
_I='NotificationType'
_H='msdslTotalIfIndex'
_G='read-write'
_F='ifIndex'
_E='IF-MIB'
_D='HOTWIRE-MSDSL-INTERFACE-MIB'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_E,_F)
pdnmsdsl,=mibBuilder.importSymbols('PDN-HEADER-MIB','pdnmsdsl')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier',_I,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_I,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_MsdslDevice_ObjectIdentity=ObjectIdentity
msdslDevice=_MsdslDevice_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,15,1))
_MsdslCurrent_ObjectIdentity=ObjectIdentity
msdslCurrent=_MsdslCurrent_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,15,1,1))
_MsdslCurrentTable_Object=MibTable
msdslCurrentTable=_MsdslCurrentTable_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,1,1))
if mibBuilder.loadTexts:msdslCurrentTable.setStatus(_A)
_MsdslCurrentEntry_Object=MibTableRow
msdslCurrentEntry=_MsdslCurrentEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,1,1,1))
msdslCurrentEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:msdslCurrentEntry.setStatus(_A)
class _MsdslCurrentIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MsdslCurrentIfIndex_Type.__name__=_C
_MsdslCurrentIfIndex_Object=MibTableColumn
msdslCurrentIfIndex=_MsdslCurrentIfIndex_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,1,1,1,1),_MsdslCurrentIfIndex_Type())
msdslCurrentIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslCurrentIfIndex.setStatus(_A)
_MsdslCurrentESs_Type=Gauge32
_MsdslCurrentESs_Object=MibTableColumn
msdslCurrentESs=_MsdslCurrentESs_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,1,1,1,2),_MsdslCurrentESs_Type())
msdslCurrentESs.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslCurrentESs.setStatus(_A)
_MsdslCurrentSESs_Type=Gauge32
_MsdslCurrentSESs_Object=MibTableColumn
msdslCurrentSESs=_MsdslCurrentSESs_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,1,1,1,3),_MsdslCurrentSESs_Type())
msdslCurrentSESs.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslCurrentSESs.setStatus(_A)
_MsdslCurrentFEBEs_Type=Gauge32
_MsdslCurrentFEBEs_Object=MibTableColumn
msdslCurrentFEBEs=_MsdslCurrentFEBEs_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,1,1,1,4),_MsdslCurrentFEBEs_Type())
msdslCurrentFEBEs.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslCurrentFEBEs.setStatus(_A)
class _MsdslErrEventsCounter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MsdslErrEventsCounter_Type.__name__=_C
_MsdslErrEventsCounter_Object=MibTableColumn
msdslErrEventsCounter=_MsdslErrEventsCounter_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,1,1,1,5),_MsdslErrEventsCounter_Type())
msdslErrEventsCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslErrEventsCounter.setStatus(_A)
class _MsdslErrTimeElapsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,899))
_MsdslErrTimeElapsed_Type.__name__=_C
_MsdslErrTimeElapsed_Object=MibTableColumn
msdslErrTimeElapsed=_MsdslErrTimeElapsed_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,1,1,1,6),_MsdslErrTimeElapsed_Type())
msdslErrTimeElapsed.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslErrTimeElapsed.setStatus(_A)
class _MsdslErrValidIntervals_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,96))
_MsdslErrValidIntervals_Type.__name__=_C
_MsdslErrValidIntervals_Object=MibTableColumn
msdslErrValidIntervals=_MsdslErrValidIntervals_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,1,1,1,7),_MsdslErrValidIntervals_Type())
msdslErrValidIntervals.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslErrValidIntervals.setStatus(_A)
_MsdslInterval_ObjectIdentity=ObjectIdentity
msdslInterval=_MsdslInterval_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,15,1,2))
_MsdslIntervalTable_Object=MibTable
msdslIntervalTable=_MsdslIntervalTable_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,2,2))
if mibBuilder.loadTexts:msdslIntervalTable.setStatus(_A)
_MsdslIntervalEntry_Object=MibTableRow
msdslIntervalEntry=_MsdslIntervalEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,2,2,1))
msdslIntervalEntry.setIndexNames((0,_D,_K),(0,_D,_L))
if mibBuilder.loadTexts:msdslIntervalEntry.setStatus(_A)
class _MsdslIntervalIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MsdslIntervalIfIndex_Type.__name__=_C
_MsdslIntervalIfIndex_Object=MibTableColumn
msdslIntervalIfIndex=_MsdslIntervalIfIndex_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,2,2,1,1),_MsdslIntervalIfIndex_Type())
msdslIntervalIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslIntervalIfIndex.setStatus(_A)
class _MsdslIntervalNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_MsdslIntervalNumber_Type.__name__=_C
_MsdslIntervalNumber_Object=MibTableColumn
msdslIntervalNumber=_MsdslIntervalNumber_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,2,2,1,2),_MsdslIntervalNumber_Type())
msdslIntervalNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslIntervalNumber.setStatus(_A)
_MsdslIntervalESs_Type=Gauge32
_MsdslIntervalESs_Object=MibTableColumn
msdslIntervalESs=_MsdslIntervalESs_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,2,2,1,3),_MsdslIntervalESs_Type())
msdslIntervalESs.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslIntervalESs.setStatus(_A)
_MsdslIntervalSESs_Type=Gauge32
_MsdslIntervalSESs_Object=MibTableColumn
msdslIntervalSESs=_MsdslIntervalSESs_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,2,2,1,4),_MsdslIntervalSESs_Type())
msdslIntervalSESs.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslIntervalSESs.setStatus(_A)
_MsdslIntervalFEBEs_Type=Gauge32
_MsdslIntervalFEBEs_Object=MibTableColumn
msdslIntervalFEBEs=_MsdslIntervalFEBEs_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,2,2,1,5),_MsdslIntervalFEBEs_Type())
msdslIntervalFEBEs.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslIntervalFEBEs.setStatus(_A)
_MsdslWorstInterval_ObjectIdentity=ObjectIdentity
msdslWorstInterval=_MsdslWorstInterval_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,15,1,3))
_MsdslWorstIntervalTable_Object=MibTable
msdslWorstIntervalTable=_MsdslWorstIntervalTable_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,3,3))
if mibBuilder.loadTexts:msdslWorstIntervalTable.setStatus(_A)
_MsdslWorstIntervalEntry_Object=MibTableRow
msdslWorstIntervalEntry=_MsdslWorstIntervalEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,3,3,1))
msdslWorstIntervalEntry.setIndexNames((0,_D,_M))
if mibBuilder.loadTexts:msdslWorstIntervalEntry.setStatus(_A)
class _MsdslWorstIntervalIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MsdslWorstIntervalIfIndex_Type.__name__=_C
_MsdslWorstIntervalIfIndex_Object=MibTableColumn
msdslWorstIntervalIfIndex=_MsdslWorstIntervalIfIndex_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,3,3,1,1),_MsdslWorstIntervalIfIndex_Type())
msdslWorstIntervalIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslWorstIntervalIfIndex.setStatus(_A)
class _MsdslWorstIntervalESs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_MsdslWorstIntervalESs_Type.__name__=_C
_MsdslWorstIntervalESs_Object=MibTableColumn
msdslWorstIntervalESs=_MsdslWorstIntervalESs_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,3,3,1,2),_MsdslWorstIntervalESs_Type())
msdslWorstIntervalESs.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslWorstIntervalESs.setStatus(_A)
class _MsdslWorstIntervalSESs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_MsdslWorstIntervalSESs_Type.__name__=_C
_MsdslWorstIntervalSESs_Object=MibTableColumn
msdslWorstIntervalSESs=_MsdslWorstIntervalSESs_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,3,3,1,3),_MsdslWorstIntervalSESs_Type())
msdslWorstIntervalSESs.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslWorstIntervalSESs.setStatus(_A)
class _MsdslWorstIntervalFEBEs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_MsdslWorstIntervalFEBEs_Type.__name__=_C
_MsdslWorstIntervalFEBEs_Object=MibTableColumn
msdslWorstIntervalFEBEs=_MsdslWorstIntervalFEBEs_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,3,3,1,4),_MsdslWorstIntervalFEBEs_Type())
msdslWorstIntervalFEBEs.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslWorstIntervalFEBEs.setStatus(_A)
_MsdslTotal_ObjectIdentity=ObjectIdentity
msdslTotal=_MsdslTotal_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,15,1,4))
_MsdslTotalTable_Object=MibTable
msdslTotalTable=_MsdslTotalTable_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,4,4))
if mibBuilder.loadTexts:msdslTotalTable.setStatus(_A)
_MsdslTotalEntry_Object=MibTableRow
msdslTotalEntry=_MsdslTotalEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,4,4,1))
msdslTotalEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:msdslTotalEntry.setStatus(_A)
class _MsdslTotalIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MsdslTotalIfIndex_Type.__name__=_C
_MsdslTotalIfIndex_Object=MibTableColumn
msdslTotalIfIndex=_MsdslTotalIfIndex_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,4,4,1,1),_MsdslTotalIfIndex_Type())
msdslTotalIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslTotalIfIndex.setStatus(_A)
_MsdslTotalESs_Type=Gauge32
_MsdslTotalESs_Object=MibTableColumn
msdslTotalESs=_MsdslTotalESs_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,4,4,1,2),_MsdslTotalESs_Type())
msdslTotalESs.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslTotalESs.setStatus(_A)
_MsdslTotalSESs_Type=Gauge32
_MsdslTotalSESs_Object=MibTableColumn
msdslTotalSESs=_MsdslTotalSESs_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,4,4,1,3),_MsdslTotalSESs_Type())
msdslTotalSESs.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslTotalSESs.setStatus(_A)
_MsdslTotalFEBEs_Type=Gauge32
_MsdslTotalFEBEs_Object=MibTableColumn
msdslTotalFEBEs=_MsdslTotalFEBEs_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,4,4,1,4),_MsdslTotalFEBEs_Type())
msdslTotalFEBEs.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslTotalFEBEs.setStatus(_A)
_MsdslFarEndCurrent_ObjectIdentity=ObjectIdentity
msdslFarEndCurrent=_MsdslFarEndCurrent_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,15,1,5))
_MsdslFarEndCurrentTable_Object=MibTable
msdslFarEndCurrentTable=_MsdslFarEndCurrentTable_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,5,5))
if mibBuilder.loadTexts:msdslFarEndCurrentTable.setStatus(_A)
_MsdslFarEndCurrentEntry_Object=MibTableRow
msdslFarEndCurrentEntry=_MsdslFarEndCurrentEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,5,5,1))
msdslFarEndCurrentEntry.setIndexNames((0,_D,_N))
if mibBuilder.loadTexts:msdslFarEndCurrentEntry.setStatus(_A)
class _MsdslFarEndCurrentIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MsdslFarEndCurrentIfIndex_Type.__name__=_C
_MsdslFarEndCurrentIfIndex_Object=MibTableColumn
msdslFarEndCurrentIfIndex=_MsdslFarEndCurrentIfIndex_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,5,5,1,1),_MsdslFarEndCurrentIfIndex_Type())
msdslFarEndCurrentIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslFarEndCurrentIfIndex.setStatus(_A)
_MsdslFarEndCurrentESs_Type=Gauge32
_MsdslFarEndCurrentESs_Object=MibTableColumn
msdslFarEndCurrentESs=_MsdslFarEndCurrentESs_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,5,5,1,2),_MsdslFarEndCurrentESs_Type())
msdslFarEndCurrentESs.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslFarEndCurrentESs.setStatus(_A)
_MsdslFarEndCurrentSESs_Type=Gauge32
_MsdslFarEndCurrentSESs_Object=MibTableColumn
msdslFarEndCurrentSESs=_MsdslFarEndCurrentSESs_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,5,5,1,3),_MsdslFarEndCurrentSESs_Type())
msdslFarEndCurrentSESs.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslFarEndCurrentSESs.setStatus(_A)
_MsdslFarEndCurrentFEBEs_Type=Gauge32
_MsdslFarEndCurrentFEBEs_Object=MibTableColumn
msdslFarEndCurrentFEBEs=_MsdslFarEndCurrentFEBEs_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,5,5,1,4),_MsdslFarEndCurrentFEBEs_Type())
msdslFarEndCurrentFEBEs.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslFarEndCurrentFEBEs.setStatus(_A)
_MsdslFarEndInterval_ObjectIdentity=ObjectIdentity
msdslFarEndInterval=_MsdslFarEndInterval_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,15,1,6))
_MsdslFarEndIntervalTable_Object=MibTable
msdslFarEndIntervalTable=_MsdslFarEndIntervalTable_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,6,6))
if mibBuilder.loadTexts:msdslFarEndIntervalTable.setStatus(_A)
_MsdslFarEndIntervalEntry_Object=MibTableRow
msdslFarEndIntervalEntry=_MsdslFarEndIntervalEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,6,6,1))
msdslFarEndIntervalEntry.setIndexNames((0,_D,_O),(0,_D,_P))
if mibBuilder.loadTexts:msdslFarEndIntervalEntry.setStatus(_A)
class _MsdslFarEndIntervalIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MsdslFarEndIntervalIfIndex_Type.__name__=_C
_MsdslFarEndIntervalIfIndex_Object=MibTableColumn
msdslFarEndIntervalIfIndex=_MsdslFarEndIntervalIfIndex_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,6,6,1,1),_MsdslFarEndIntervalIfIndex_Type())
msdslFarEndIntervalIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslFarEndIntervalIfIndex.setStatus(_A)
class _MsdslFarEndIntervalNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_MsdslFarEndIntervalNumber_Type.__name__=_C
_MsdslFarEndIntervalNumber_Object=MibTableColumn
msdslFarEndIntervalNumber=_MsdslFarEndIntervalNumber_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,6,6,1,2),_MsdslFarEndIntervalNumber_Type())
msdslFarEndIntervalNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslFarEndIntervalNumber.setStatus(_A)
_MsdslFarEndIntervalESs_Type=Gauge32
_MsdslFarEndIntervalESs_Object=MibTableColumn
msdslFarEndIntervalESs=_MsdslFarEndIntervalESs_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,6,6,1,3),_MsdslFarEndIntervalESs_Type())
msdslFarEndIntervalESs.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslFarEndIntervalESs.setStatus(_A)
_MsdslFarEndIntervalSESs_Type=Gauge32
_MsdslFarEndIntervalSESs_Object=MibTableColumn
msdslFarEndIntervalSESs=_MsdslFarEndIntervalSESs_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,6,6,1,4),_MsdslFarEndIntervalSESs_Type())
msdslFarEndIntervalSESs.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslFarEndIntervalSESs.setStatus(_A)
_MsdslFarEndIntervalFEBEs_Type=Gauge32
_MsdslFarEndIntervalFEBEs_Object=MibTableColumn
msdslFarEndIntervalFEBEs=_MsdslFarEndIntervalFEBEs_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,6,6,1,5),_MsdslFarEndIntervalFEBEs_Type())
msdslFarEndIntervalFEBEs.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslFarEndIntervalFEBEs.setStatus(_A)
_MsdslFarEndWorstInterval_ObjectIdentity=ObjectIdentity
msdslFarEndWorstInterval=_MsdslFarEndWorstInterval_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,15,1,7))
_MsdslFarEndWorstIntervalTable_Object=MibTable
msdslFarEndWorstIntervalTable=_MsdslFarEndWorstIntervalTable_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,7,7))
if mibBuilder.loadTexts:msdslFarEndWorstIntervalTable.setStatus(_A)
_MsdslFarEndWorstIntervalEntry_Object=MibTableRow
msdslFarEndWorstIntervalEntry=_MsdslFarEndWorstIntervalEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,7,7,1))
msdslFarEndWorstIntervalEntry.setIndexNames((0,_D,_Q))
if mibBuilder.loadTexts:msdslFarEndWorstIntervalEntry.setStatus(_A)
class _MsdslFarEndWorstIntervalIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MsdslFarEndWorstIntervalIfIndex_Type.__name__=_C
_MsdslFarEndWorstIntervalIfIndex_Object=MibTableColumn
msdslFarEndWorstIntervalIfIndex=_MsdslFarEndWorstIntervalIfIndex_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,7,7,1,1),_MsdslFarEndWorstIntervalIfIndex_Type())
msdslFarEndWorstIntervalIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslFarEndWorstIntervalIfIndex.setStatus(_A)
class _MsdslFarEndWorstIntervalESs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_MsdslFarEndWorstIntervalESs_Type.__name__=_C
_MsdslFarEndWorstIntervalESs_Object=MibTableColumn
msdslFarEndWorstIntervalESs=_MsdslFarEndWorstIntervalESs_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,7,7,1,2),_MsdslFarEndWorstIntervalESs_Type())
msdslFarEndWorstIntervalESs.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslFarEndWorstIntervalESs.setStatus(_A)
class _MsdslFarEndWorstIntervalSESs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_MsdslFarEndWorstIntervalSESs_Type.__name__=_C
_MsdslFarEndWorstIntervalSESs_Object=MibTableColumn
msdslFarEndWorstIntervalSESs=_MsdslFarEndWorstIntervalSESs_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,7,7,1,3),_MsdslFarEndWorstIntervalSESs_Type())
msdslFarEndWorstIntervalSESs.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslFarEndWorstIntervalSESs.setStatus(_A)
class _MsdslFarEndWorstIntervalFEBEs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_MsdslFarEndWorstIntervalFEBEs_Type.__name__=_C
_MsdslFarEndWorstIntervalFEBEs_Object=MibTableColumn
msdslFarEndWorstIntervalFEBEs=_MsdslFarEndWorstIntervalFEBEs_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,7,7,1,4),_MsdslFarEndWorstIntervalFEBEs_Type())
msdslFarEndWorstIntervalFEBEs.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslFarEndWorstIntervalFEBEs.setStatus(_A)
_MsdslFarEndTotal_ObjectIdentity=ObjectIdentity
msdslFarEndTotal=_MsdslFarEndTotal_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,15,1,8))
_MsdslFarEndTotalTable_Object=MibTable
msdslFarEndTotalTable=_MsdslFarEndTotalTable_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,8,8))
if mibBuilder.loadTexts:msdslFarEndTotalTable.setStatus(_A)
_MsdslFarEndTotalEntry_Object=MibTableRow
msdslFarEndTotalEntry=_MsdslFarEndTotalEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,8,8,1))
msdslFarEndTotalEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:msdslFarEndTotalEntry.setStatus(_A)
class _MsdslFarEndTotalIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MsdslFarEndTotalIfIndex_Type.__name__=_C
_MsdslFarEndTotalIfIndex_Object=MibTableColumn
msdslFarEndTotalIfIndex=_MsdslFarEndTotalIfIndex_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,8,8,1,1),_MsdslFarEndTotalIfIndex_Type())
msdslFarEndTotalIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslFarEndTotalIfIndex.setStatus(_A)
_MsdslFarEndTotalESs_Type=Gauge32
_MsdslFarEndTotalESs_Object=MibTableColumn
msdslFarEndTotalESs=_MsdslFarEndTotalESs_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,8,8,1,2),_MsdslFarEndTotalESs_Type())
msdslFarEndTotalESs.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslFarEndTotalESs.setStatus(_A)
_MsdslFarEndTotalSESs_Type=Gauge32
_MsdslFarEndTotalSESs_Object=MibTableColumn
msdslFarEndTotalSESs=_MsdslFarEndTotalSESs_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,8,8,1,3),_MsdslFarEndTotalSESs_Type())
msdslFarEndTotalSESs.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslFarEndTotalSESs.setStatus(_A)
_MsdslFarEndTotalFEBEs_Type=Gauge32
_MsdslFarEndTotalFEBEs_Object=MibTableColumn
msdslFarEndTotalFEBEs=_MsdslFarEndTotalFEBEs_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,8,8,1,4),_MsdslFarEndTotalFEBEs_Type())
msdslFarEndTotalFEBEs.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslFarEndTotalFEBEs.setStatus(_A)
_MsdslCurrentPerf_ObjectIdentity=ObjectIdentity
msdslCurrentPerf=_MsdslCurrentPerf_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,15,1,9))
_MsdslCurrentPerfTable_Object=MibTable
msdslCurrentPerfTable=_MsdslCurrentPerfTable_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,9,9))
if mibBuilder.loadTexts:msdslCurrentPerfTable.setStatus(_A)
_MsdslCurrentPerfEntry_Object=MibTableRow
msdslCurrentPerfEntry=_MsdslCurrentPerfEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,9,9,1))
msdslCurrentPerfEntry.setIndexNames((0,_D,_R))
if mibBuilder.loadTexts:msdslCurrentPerfEntry.setStatus(_A)
class _MsdslCurrentPerfIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MsdslCurrentPerfIfIndex_Type.__name__=_C
_MsdslCurrentPerfIfIndex_Object=MibTableColumn
msdslCurrentPerfIfIndex=_MsdslCurrentPerfIfIndex_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,9,9,1,1),_MsdslCurrentPerfIfIndex_Type())
msdslCurrentPerfIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslCurrentPerfIfIndex.setStatus(_A)
_MsdslCurrentPerfMargin_Type=Gauge32
_MsdslCurrentPerfMargin_Object=MibTableColumn
msdslCurrentPerfMargin=_MsdslCurrentPerfMargin_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,9,9,1,2),_MsdslCurrentPerfMargin_Type())
msdslCurrentPerfMargin.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslCurrentPerfMargin.setStatus(_A)
_MsdslCurrentPerfTxPwr_Type=Gauge32
_MsdslCurrentPerfTxPwr_Object=MibTableColumn
msdslCurrentPerfTxPwr=_MsdslCurrentPerfTxPwr_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,9,9,1,3),_MsdslCurrentPerfTxPwr_Type())
msdslCurrentPerfTxPwr.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslCurrentPerfTxPwr.setStatus(_A)
_MsdslCurrentPerfRxGain_Type=Gauge32
_MsdslCurrentPerfRxGain_Object=MibTableColumn
msdslCurrentPerfRxGain=_MsdslCurrentPerfRxGain_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,9,9,1,4),_MsdslCurrentPerfRxGain_Type())
msdslCurrentPerfRxGain.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslCurrentPerfRxGain.setStatus(_A)
_MsdslPerfPayloadRate_Type=Gauge32
_MsdslPerfPayloadRate_Object=MibTableColumn
msdslPerfPayloadRate=_MsdslPerfPayloadRate_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,9,9,1,5),_MsdslPerfPayloadRate_Type())
msdslPerfPayloadRate.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslPerfPayloadRate.setStatus(_A)
class _MsdslTimeElapsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,899))
_MsdslTimeElapsed_Type.__name__=_C
_MsdslTimeElapsed_Object=MibTableColumn
msdslTimeElapsed=_MsdslTimeElapsed_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,9,9,1,6),_MsdslTimeElapsed_Type())
msdslTimeElapsed.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslTimeElapsed.setStatus(_A)
class _MsdslValidIntervals_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,96))
_MsdslValidIntervals_Type.__name__=_C
_MsdslValidIntervals_Object=MibTableColumn
msdslValidIntervals=_MsdslValidIntervals_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,9,9,1,7),_MsdslValidIntervals_Type())
msdslValidIntervals.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslValidIntervals.setStatus(_A)
_MsdslIntervalPerf_ObjectIdentity=ObjectIdentity
msdslIntervalPerf=_MsdslIntervalPerf_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,15,1,10))
_MsdslIntervalPerfTable_Object=MibTable
msdslIntervalPerfTable=_MsdslIntervalPerfTable_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,10,10))
if mibBuilder.loadTexts:msdslIntervalPerfTable.setStatus(_A)
_MsdslIntervalPerfEntry_Object=MibTableRow
msdslIntervalPerfEntry=_MsdslIntervalPerfEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,10,10,1))
msdslIntervalPerfEntry.setIndexNames((0,_D,_S),(0,_D,_T))
if mibBuilder.loadTexts:msdslIntervalPerfEntry.setStatus(_A)
class _MsdslIntervalPerfIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MsdslIntervalPerfIfIndex_Type.__name__=_C
_MsdslIntervalPerfIfIndex_Object=MibTableColumn
msdslIntervalPerfIfIndex=_MsdslIntervalPerfIfIndex_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,10,10,1,1),_MsdslIntervalPerfIfIndex_Type())
msdslIntervalPerfIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslIntervalPerfIfIndex.setStatus(_A)
class _MsdslIntervalPerfNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_MsdslIntervalPerfNumber_Type.__name__=_C
_MsdslIntervalPerfNumber_Object=MibTableColumn
msdslIntervalPerfNumber=_MsdslIntervalPerfNumber_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,10,10,1,2),_MsdslIntervalPerfNumber_Type())
msdslIntervalPerfNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslIntervalPerfNumber.setStatus(_A)
_MsdslIntervalPerfMargin_Type=Gauge32
_MsdslIntervalPerfMargin_Object=MibTableColumn
msdslIntervalPerfMargin=_MsdslIntervalPerfMargin_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,10,10,1,3),_MsdslIntervalPerfMargin_Type())
msdslIntervalPerfMargin.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslIntervalPerfMargin.setStatus(_A)
_MsdslIntervalPerfTxPwr_Type=Gauge32
_MsdslIntervalPerfTxPwr_Object=MibTableColumn
msdslIntervalPerfTxPwr=_MsdslIntervalPerfTxPwr_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,10,10,1,4),_MsdslIntervalPerfTxPwr_Type())
msdslIntervalPerfTxPwr.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslIntervalPerfTxPwr.setStatus(_A)
_MsdslIntervalPerfRxGain_Type=Gauge32
_MsdslIntervalPerfRxGain_Object=MibTableColumn
msdslIntervalPerfRxGain=_MsdslIntervalPerfRxGain_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,10,10,1,5),_MsdslIntervalPerfRxGain_Type())
msdslIntervalPerfRxGain.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslIntervalPerfRxGain.setStatus(_A)
_MsdslFarEndCurrentPerf_ObjectIdentity=ObjectIdentity
msdslFarEndCurrentPerf=_MsdslFarEndCurrentPerf_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,15,1,11))
_MsdslFarEndCurrentPerfTable_Object=MibTable
msdslFarEndCurrentPerfTable=_MsdslFarEndCurrentPerfTable_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,11,11))
if mibBuilder.loadTexts:msdslFarEndCurrentPerfTable.setStatus(_A)
_MsdslFarEndCurrentPerfEntry_Object=MibTableRow
msdslFarEndCurrentPerfEntry=_MsdslFarEndCurrentPerfEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,11,11,1))
msdslFarEndCurrentPerfEntry.setIndexNames((0,_D,_U))
if mibBuilder.loadTexts:msdslFarEndCurrentPerfEntry.setStatus(_A)
class _MsdslFarEndCurrentPerfIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MsdslFarEndCurrentPerfIfIndex_Type.__name__=_C
_MsdslFarEndCurrentPerfIfIndex_Object=MibTableColumn
msdslFarEndCurrentPerfIfIndex=_MsdslFarEndCurrentPerfIfIndex_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,11,11,1,1),_MsdslFarEndCurrentPerfIfIndex_Type())
msdslFarEndCurrentPerfIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslFarEndCurrentPerfIfIndex.setStatus(_A)
_MsdslFarEndCurrentPerfMargin_Type=Gauge32
_MsdslFarEndCurrentPerfMargin_Object=MibTableColumn
msdslFarEndCurrentPerfMargin=_MsdslFarEndCurrentPerfMargin_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,11,11,1,2),_MsdslFarEndCurrentPerfMargin_Type())
msdslFarEndCurrentPerfMargin.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslFarEndCurrentPerfMargin.setStatus(_A)
_MsdslFarEndCurrentPerfTxPwr_Type=Gauge32
_MsdslFarEndCurrentPerfTxPwr_Object=MibTableColumn
msdslFarEndCurrentPerfTxPwr=_MsdslFarEndCurrentPerfTxPwr_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,11,11,1,3),_MsdslFarEndCurrentPerfTxPwr_Type())
msdslFarEndCurrentPerfTxPwr.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslFarEndCurrentPerfTxPwr.setStatus(_A)
_MsdslFarEndCurrentPerfRxGain_Type=Gauge32
_MsdslFarEndCurrentPerfRxGain_Object=MibTableColumn
msdslFarEndCurrentPerfRxGain=_MsdslFarEndCurrentPerfRxGain_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,11,11,1,4),_MsdslFarEndCurrentPerfRxGain_Type())
msdslFarEndCurrentPerfRxGain.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslFarEndCurrentPerfRxGain.setStatus(_A)
_MsdslFarEndIntervalPerf_ObjectIdentity=ObjectIdentity
msdslFarEndIntervalPerf=_MsdslFarEndIntervalPerf_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,15,1,12))
_MsdslFarEndIntervalPerfTable_Object=MibTable
msdslFarEndIntervalPerfTable=_MsdslFarEndIntervalPerfTable_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,12,12))
if mibBuilder.loadTexts:msdslFarEndIntervalPerfTable.setStatus(_A)
_MsdslFarEndIntervalPerfEntry_Object=MibTableRow
msdslFarEndIntervalPerfEntry=_MsdslFarEndIntervalPerfEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,12,12,1))
msdslFarEndIntervalPerfEntry.setIndexNames((0,_D,_V),(0,_D,_W))
if mibBuilder.loadTexts:msdslFarEndIntervalPerfEntry.setStatus(_A)
class _MsdslFarEndIntervalPerfIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MsdslFarEndIntervalPerfIfIndex_Type.__name__=_C
_MsdslFarEndIntervalPerfIfIndex_Object=MibTableColumn
msdslFarEndIntervalPerfIfIndex=_MsdslFarEndIntervalPerfIfIndex_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,12,12,1,1),_MsdslFarEndIntervalPerfIfIndex_Type())
msdslFarEndIntervalPerfIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslFarEndIntervalPerfIfIndex.setStatus(_A)
class _MsdslFarEndIntervalPerfNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_MsdslFarEndIntervalPerfNumber_Type.__name__=_C
_MsdslFarEndIntervalPerfNumber_Object=MibTableColumn
msdslFarEndIntervalPerfNumber=_MsdslFarEndIntervalPerfNumber_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,12,12,1,2),_MsdslFarEndIntervalPerfNumber_Type())
msdslFarEndIntervalPerfNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslFarEndIntervalPerfNumber.setStatus(_A)
_MsdslFarEndIntervalPerfMargin_Type=Gauge32
_MsdslFarEndIntervalPerfMargin_Object=MibTableColumn
msdslFarEndIntervalPerfMargin=_MsdslFarEndIntervalPerfMargin_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,12,12,1,3),_MsdslFarEndIntervalPerfMargin_Type())
msdslFarEndIntervalPerfMargin.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslFarEndIntervalPerfMargin.setStatus(_A)
_MsdslFarEndIntervalPerfTxPwr_Type=Gauge32
_MsdslFarEndIntervalPerfTxPwr_Object=MibTableColumn
msdslFarEndIntervalPerfTxPwr=_MsdslFarEndIntervalPerfTxPwr_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,12,12,1,4),_MsdslFarEndIntervalPerfTxPwr_Type())
msdslFarEndIntervalPerfTxPwr.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslFarEndIntervalPerfTxPwr.setStatus(_A)
_MsdslFarEndIntervalPerfRxGain_Type=Gauge32
_MsdslFarEndIntervalPerfRxGain_Object=MibTableColumn
msdslFarEndIntervalPerfRxGain=_MsdslFarEndIntervalPerfRxGain_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,12,12,1,5),_MsdslFarEndIntervalPerfRxGain_Type())
msdslFarEndIntervalPerfRxGain.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslFarEndIntervalPerfRxGain.setStatus(_A)
_Msdsldsx1WorstInterval_ObjectIdentity=ObjectIdentity
msdsldsx1WorstInterval=_Msdsldsx1WorstInterval_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,15,1,13))
_Msdsldsx1WorstIntervalTable_Object=MibTable
msdsldsx1WorstIntervalTable=_Msdsldsx1WorstIntervalTable_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,13,13))
if mibBuilder.loadTexts:msdsldsx1WorstIntervalTable.setStatus(_A)
_Msdsldsx1WorstIntervalEntry_Object=MibTableRow
msdsldsx1WorstIntervalEntry=_Msdsldsx1WorstIntervalEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,13,13,1))
msdsldsx1WorstIntervalEntry.setIndexNames((0,_D,_X))
if mibBuilder.loadTexts:msdsldsx1WorstIntervalEntry.setStatus(_A)
class _Msdsldsx1WorstIntervalIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Msdsldsx1WorstIntervalIfIndex_Type.__name__=_C
_Msdsldsx1WorstIntervalIfIndex_Object=MibTableColumn
msdsldsx1WorstIntervalIfIndex=_Msdsldsx1WorstIntervalIfIndex_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,13,13,1,1),_Msdsldsx1WorstIntervalIfIndex_Type())
msdsldsx1WorstIntervalIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:msdsldsx1WorstIntervalIfIndex.setStatus(_A)
_Msdsldsx1WorstIntervalESs_Type=Integer32
_Msdsldsx1WorstIntervalESs_Object=MibTableColumn
msdsldsx1WorstIntervalESs=_Msdsldsx1WorstIntervalESs_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,13,13,1,2),_Msdsldsx1WorstIntervalESs_Type())
msdsldsx1WorstIntervalESs.setMaxAccess(_B)
if mibBuilder.loadTexts:msdsldsx1WorstIntervalESs.setStatus(_A)
_Msdsldsx1WorstIntervalUASs_Type=Integer32
_Msdsldsx1WorstIntervalUASs_Object=MibTableColumn
msdsldsx1WorstIntervalUASs=_Msdsldsx1WorstIntervalUASs_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,13,13,1,3),_Msdsldsx1WorstIntervalUASs_Type())
msdsldsx1WorstIntervalUASs.setMaxAccess(_B)
if mibBuilder.loadTexts:msdsldsx1WorstIntervalUASs.setStatus(_A)
_Msdsldsx1WorstIntervalSESs_Type=Integer32
_Msdsldsx1WorstIntervalSESs_Object=MibTableColumn
msdsldsx1WorstIntervalSESs=_Msdsldsx1WorstIntervalSESs_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,13,13,1,4),_Msdsldsx1WorstIntervalSESs_Type())
msdsldsx1WorstIntervalSESs.setMaxAccess(_B)
if mibBuilder.loadTexts:msdsldsx1WorstIntervalSESs.setStatus(_A)
_Msdsldsx1WorstIntervalBESs_Type=Integer32
_Msdsldsx1WorstIntervalBESs_Object=MibTableColumn
msdsldsx1WorstIntervalBESs=_Msdsldsx1WorstIntervalBESs_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,13,13,1,5),_Msdsldsx1WorstIntervalBESs_Type())
msdsldsx1WorstIntervalBESs.setMaxAccess(_B)
if mibBuilder.loadTexts:msdsldsx1WorstIntervalBESs.setStatus(_A)
_Msdsldsx1WorstIntervalCSSs_Type=Integer32
_Msdsldsx1WorstIntervalCSSs_Object=MibTableColumn
msdsldsx1WorstIntervalCSSs=_Msdsldsx1WorstIntervalCSSs_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,13,13,1,6),_Msdsldsx1WorstIntervalCSSs_Type())
msdsldsx1WorstIntervalCSSs.setMaxAccess(_B)
if mibBuilder.loadTexts:msdsldsx1WorstIntervalCSSs.setStatus(_A)
_Msdsldsx1WorstIntervalLOFC_Type=Integer32
_Msdsldsx1WorstIntervalLOFC_Object=MibTableColumn
msdsldsx1WorstIntervalLOFC=_Msdsldsx1WorstIntervalLOFC_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,13,13,1,7),_Msdsldsx1WorstIntervalLOFC_Type())
msdsldsx1WorstIntervalLOFC.setMaxAccess(_B)
if mibBuilder.loadTexts:msdsldsx1WorstIntervalLOFC.setStatus(_A)
_MsdslG703WorstInterval_ObjectIdentity=ObjectIdentity
msdslG703WorstInterval=_MsdslG703WorstInterval_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,15,1,14))
_MsdslG703WorstIntervalTable_Object=MibTable
msdslG703WorstIntervalTable=_MsdslG703WorstIntervalTable_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,14,14))
if mibBuilder.loadTexts:msdslG703WorstIntervalTable.setStatus(_A)
_MsdslG703WorstIntervalEntry_Object=MibTableRow
msdslG703WorstIntervalEntry=_MsdslG703WorstIntervalEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,14,14,1))
msdslG703WorstIntervalEntry.setIndexNames((0,_D,_Y))
if mibBuilder.loadTexts:msdslG703WorstIntervalEntry.setStatus(_A)
class _MsdslG703WorstIntervalIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MsdslG703WorstIntervalIfIndex_Type.__name__=_C
_MsdslG703WorstIntervalIfIndex_Object=MibTableColumn
msdslG703WorstIntervalIfIndex=_MsdslG703WorstIntervalIfIndex_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,14,14,1,1),_MsdslG703WorstIntervalIfIndex_Type())
msdslG703WorstIntervalIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslG703WorstIntervalIfIndex.setStatus(_A)
_MsdslG703WorstIntervalESs_Type=Integer32
_MsdslG703WorstIntervalESs_Object=MibTableColumn
msdslG703WorstIntervalESs=_MsdslG703WorstIntervalESs_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,14,14,1,2),_MsdslG703WorstIntervalESs_Type())
msdslG703WorstIntervalESs.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslG703WorstIntervalESs.setStatus(_A)
_MsdslG703WorstIntervalUASs_Type=Integer32
_MsdslG703WorstIntervalUASs_Object=MibTableColumn
msdslG703WorstIntervalUASs=_MsdslG703WorstIntervalUASs_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,14,14,1,3),_MsdslG703WorstIntervalUASs_Type())
msdslG703WorstIntervalUASs.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslG703WorstIntervalUASs.setStatus(_A)
_MsdslG703WorstIntervalSESs_Type=Integer32
_MsdslG703WorstIntervalSESs_Object=MibTableColumn
msdslG703WorstIntervalSESs=_MsdslG703WorstIntervalSESs_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,14,14,1,4),_MsdslG703WorstIntervalSESs_Type())
msdslG703WorstIntervalSESs.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslG703WorstIntervalSESs.setStatus(_A)
_MsdslG703WorstIntervalBESs_Type=Integer32
_MsdslG703WorstIntervalBESs_Object=MibTableColumn
msdslG703WorstIntervalBESs=_MsdslG703WorstIntervalBESs_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,14,14,1,5),_MsdslG703WorstIntervalBESs_Type())
msdslG703WorstIntervalBESs.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslG703WorstIntervalBESs.setStatus(_A)
_MsdslG703WorstIntervalCSSs_Type=Integer32
_MsdslG703WorstIntervalCSSs_Object=MibTableColumn
msdslG703WorstIntervalCSSs=_MsdslG703WorstIntervalCSSs_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,14,14,1,6),_MsdslG703WorstIntervalCSSs_Type())
msdslG703WorstIntervalCSSs.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslG703WorstIntervalCSSs.setStatus(_A)
_MsdslG703WorstIntervalLOFC_Type=Integer32
_MsdslG703WorstIntervalLOFC_Object=MibTableColumn
msdslG703WorstIntervalLOFC=_MsdslG703WorstIntervalLOFC_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,14,14,1,7),_MsdslG703WorstIntervalLOFC_Type())
msdslG703WorstIntervalLOFC.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslG703WorstIntervalLOFC.setStatus(_A)
_MsdslConfiguration_ObjectIdentity=ObjectIdentity
msdslConfiguration=_MsdslConfiguration_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,15,1,15))
_MsdslFracTable_Object=MibTable
msdslFracTable=_MsdslFracTable_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,15,28))
if mibBuilder.loadTexts:msdslFracTable.setStatus(_A)
_MsdslFracEntry_Object=MibTableRow
msdslFracEntry=_MsdslFracEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,15,28,1))
msdslFracEntry.setIndexNames((0,_D,_Z),(0,_D,_a))
if mibBuilder.loadTexts:msdslFracEntry.setStatus(_A)
_MsdslFracPortIndex_Type=Integer32
_MsdslFracPortIndex_Object=MibTableColumn
msdslFracPortIndex=_MsdslFracPortIndex_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,15,28,1,1),_MsdslFracPortIndex_Type())
msdslFracPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslFracPortIndex.setStatus(_A)
class _MsdslFracPortTS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,31))
_MsdslFracPortTS_Type.__name__=_C
_MsdslFracPortTS_Object=MibTableColumn
msdslFracPortTS=_MsdslFracPortTS_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,15,28,1,2),_MsdslFracPortTS_Type())
msdslFracPortTS.setMaxAccess(_G)
if mibBuilder.loadTexts:msdslFracPortTS.setStatus(_A)
_MsdslFracPortIfIndex_Type=Integer32
_MsdslFracPortIfIndex_Object=MibTableColumn
msdslFracPortIfIndex=_MsdslFracPortIfIndex_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,15,28,1,3),_MsdslFracPortIfIndex_Type())
msdslFracPortIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:msdslFracPortIfIndex.setStatus(_A)
class _MsdslFracPortIfTS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_MsdslFracPortIfTS_Type.__name__=_C
_MsdslFracPortIfTS_Object=MibTableColumn
msdslFracPortIfTS=_MsdslFracPortIfTS_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,15,28,1,4),_MsdslFracPortIfTS_Type())
msdslFracPortIfTS.setMaxAccess(_G)
if mibBuilder.loadTexts:msdslFracPortIfTS.setStatus(_A)
class _MsdslFracPortVoiceData_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('voice',1),('data',2)))
_MsdslFracPortVoiceData_Type.__name__=_C
_MsdslFracPortVoiceData_Object=MibTableColumn
msdslFracPortVoiceData=_MsdslFracPortVoiceData_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,15,28,1,5),_MsdslFracPortVoiceData_Type())
msdslFracPortVoiceData.setMaxAccess(_G)
if mibBuilder.loadTexts:msdslFracPortVoiceData.setStatus(_A)
_MsdslPortConfigAllocMethodTable_Object=MibTable
msdslPortConfigAllocMethodTable=_MsdslPortConfigAllocMethodTable_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,15,29))
if mibBuilder.loadTexts:msdslPortConfigAllocMethodTable.setStatus(_A)
_MsdslPortConfigAllocMethodEntry_Object=MibTableRow
msdslPortConfigAllocMethodEntry=_MsdslPortConfigAllocMethodEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,15,29,1))
msdslPortConfigAllocMethodEntry.setIndexNames((0,_D,_b))
if mibBuilder.loadTexts:msdslPortConfigAllocMethodEntry.setStatus(_A)
_MsdslPortConfigAllocMethodIfIndex_Type=Integer32
_MsdslPortConfigAllocMethodIfIndex_Object=MibTableColumn
msdslPortConfigAllocMethodIfIndex=_MsdslPortConfigAllocMethodIfIndex_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,15,29,1,1),_MsdslPortConfigAllocMethodIfIndex_Type())
msdslPortConfigAllocMethodIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:msdslPortConfigAllocMethodIfIndex.setStatus(_A)
class _MsdslPortConfigAllocMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('ds1ByPass',1),('ds1CrossConn',2),('ds0CrossConn',3),('notAssigned',4),('disabled',5)))
_MsdslPortConfigAllocMethod_Type.__name__=_C
_MsdslPortConfigAllocMethod_Object=MibTableColumn
msdslPortConfigAllocMethod=_MsdslPortConfigAllocMethod_Object((1,3,6,1,4,1,1795,2,24,2,6,15,1,15,29,1,2),_MsdslPortConfigAllocMethod_Type())
msdslPortConfigAllocMethod.setMaxAccess(_G)
if mibBuilder.loadTexts:msdslPortConfigAllocMethod.setStatus(_A)
msdslMarginLow=NotificationType((1,3,6,1,4,1,1795,2,24,2,6,15,1,0,3))
msdslMarginLow.setObjects((_E,_F))
if mibBuilder.loadTexts:msdslMarginLow.setStatus('')
msdslErrorRateHigh=NotificationType((1,3,6,1,4,1,1795,2,24,2,6,15,1,0,4))
msdslErrorRateHigh.setObjects((_E,_F))
if mibBuilder.loadTexts:msdslErrorRateHigh.setStatus('')
msdslNTUTypeMismatch=NotificationType((1,3,6,1,4,1,1795,2,24,2,6,15,1,0,7))
msdslNTUTypeMismatch.setObjects((_E,_F))
if mibBuilder.loadTexts:msdslNTUTypeMismatch.setStatus('')
msdslMarginNormal=NotificationType((1,3,6,1,4,1,1795,2,24,2,6,15,1,0,103))
msdslMarginNormal.setObjects((_E,_F))
if mibBuilder.loadTexts:msdslMarginNormal.setStatus('')
msdslErrorRateNormal=NotificationType((1,3,6,1,4,1,1795,2,24,2,6,15,1,0,104))
msdslErrorRateNormal.setObjects((_E,_F))
if mibBuilder.loadTexts:msdslErrorRateNormal.setStatus('')
msdslTestOver=NotificationType((1,3,6,1,4,1,1795,2,24,2,6,15,1,0,106))
msdslTestOver.setObjects((_E,_F))
if mibBuilder.loadTexts:msdslTestOver.setStatus('')
mibBuilder.exportSymbols(_D,**{'msdslDevice':msdslDevice,'msdslMarginLow':msdslMarginLow,'msdslErrorRateHigh':msdslErrorRateHigh,'msdslNTUTypeMismatch':msdslNTUTypeMismatch,'msdslMarginNormal':msdslMarginNormal,'msdslErrorRateNormal':msdslErrorRateNormal,'msdslTestOver':msdslTestOver,'msdslCurrent':msdslCurrent,'msdslCurrentTable':msdslCurrentTable,'msdslCurrentEntry':msdslCurrentEntry,_J:msdslCurrentIfIndex,'msdslCurrentESs':msdslCurrentESs,'msdslCurrentSESs':msdslCurrentSESs,'msdslCurrentFEBEs':msdslCurrentFEBEs,'msdslErrEventsCounter':msdslErrEventsCounter,'msdslErrTimeElapsed':msdslErrTimeElapsed,'msdslErrValidIntervals':msdslErrValidIntervals,'msdslInterval':msdslInterval,'msdslIntervalTable':msdslIntervalTable,'msdslIntervalEntry':msdslIntervalEntry,_K:msdslIntervalIfIndex,_L:msdslIntervalNumber,'msdslIntervalESs':msdslIntervalESs,'msdslIntervalSESs':msdslIntervalSESs,'msdslIntervalFEBEs':msdslIntervalFEBEs,'msdslWorstInterval':msdslWorstInterval,'msdslWorstIntervalTable':msdslWorstIntervalTable,'msdslWorstIntervalEntry':msdslWorstIntervalEntry,_M:msdslWorstIntervalIfIndex,'msdslWorstIntervalESs':msdslWorstIntervalESs,'msdslWorstIntervalSESs':msdslWorstIntervalSESs,'msdslWorstIntervalFEBEs':msdslWorstIntervalFEBEs,'msdslTotal':msdslTotal,'msdslTotalTable':msdslTotalTable,'msdslTotalEntry':msdslTotalEntry,_H:msdslTotalIfIndex,'msdslTotalESs':msdslTotalESs,'msdslTotalSESs':msdslTotalSESs,'msdslTotalFEBEs':msdslTotalFEBEs,'msdslFarEndCurrent':msdslFarEndCurrent,'msdslFarEndCurrentTable':msdslFarEndCurrentTable,'msdslFarEndCurrentEntry':msdslFarEndCurrentEntry,_N:msdslFarEndCurrentIfIndex,'msdslFarEndCurrentESs':msdslFarEndCurrentESs,'msdslFarEndCurrentSESs':msdslFarEndCurrentSESs,'msdslFarEndCurrentFEBEs':msdslFarEndCurrentFEBEs,'msdslFarEndInterval':msdslFarEndInterval,'msdslFarEndIntervalTable':msdslFarEndIntervalTable,'msdslFarEndIntervalEntry':msdslFarEndIntervalEntry,_O:msdslFarEndIntervalIfIndex,_P:msdslFarEndIntervalNumber,'msdslFarEndIntervalESs':msdslFarEndIntervalESs,'msdslFarEndIntervalSESs':msdslFarEndIntervalSESs,'msdslFarEndIntervalFEBEs':msdslFarEndIntervalFEBEs,'msdslFarEndWorstInterval':msdslFarEndWorstInterval,'msdslFarEndWorstIntervalTable':msdslFarEndWorstIntervalTable,'msdslFarEndWorstIntervalEntry':msdslFarEndWorstIntervalEntry,_Q:msdslFarEndWorstIntervalIfIndex,'msdslFarEndWorstIntervalESs':msdslFarEndWorstIntervalESs,'msdslFarEndWorstIntervalSESs':msdslFarEndWorstIntervalSESs,'msdslFarEndWorstIntervalFEBEs':msdslFarEndWorstIntervalFEBEs,'msdslFarEndTotal':msdslFarEndTotal,'msdslFarEndTotalTable':msdslFarEndTotalTable,'msdslFarEndTotalEntry':msdslFarEndTotalEntry,'msdslFarEndTotalIfIndex':msdslFarEndTotalIfIndex,'msdslFarEndTotalESs':msdslFarEndTotalESs,'msdslFarEndTotalSESs':msdslFarEndTotalSESs,'msdslFarEndTotalFEBEs':msdslFarEndTotalFEBEs,'msdslCurrentPerf':msdslCurrentPerf,'msdslCurrentPerfTable':msdslCurrentPerfTable,'msdslCurrentPerfEntry':msdslCurrentPerfEntry,_R:msdslCurrentPerfIfIndex,'msdslCurrentPerfMargin':msdslCurrentPerfMargin,'msdslCurrentPerfTxPwr':msdslCurrentPerfTxPwr,'msdslCurrentPerfRxGain':msdslCurrentPerfRxGain,'msdslPerfPayloadRate':msdslPerfPayloadRate,'msdslTimeElapsed':msdslTimeElapsed,'msdslValidIntervals':msdslValidIntervals,'msdslIntervalPerf':msdslIntervalPerf,'msdslIntervalPerfTable':msdslIntervalPerfTable,'msdslIntervalPerfEntry':msdslIntervalPerfEntry,_S:msdslIntervalPerfIfIndex,_T:msdslIntervalPerfNumber,'msdslIntervalPerfMargin':msdslIntervalPerfMargin,'msdslIntervalPerfTxPwr':msdslIntervalPerfTxPwr,'msdslIntervalPerfRxGain':msdslIntervalPerfRxGain,'msdslFarEndCurrentPerf':msdslFarEndCurrentPerf,'msdslFarEndCurrentPerfTable':msdslFarEndCurrentPerfTable,'msdslFarEndCurrentPerfEntry':msdslFarEndCurrentPerfEntry,_U:msdslFarEndCurrentPerfIfIndex,'msdslFarEndCurrentPerfMargin':msdslFarEndCurrentPerfMargin,'msdslFarEndCurrentPerfTxPwr':msdslFarEndCurrentPerfTxPwr,'msdslFarEndCurrentPerfRxGain':msdslFarEndCurrentPerfRxGain,'msdslFarEndIntervalPerf':msdslFarEndIntervalPerf,'msdslFarEndIntervalPerfTable':msdslFarEndIntervalPerfTable,'msdslFarEndIntervalPerfEntry':msdslFarEndIntervalPerfEntry,_V:msdslFarEndIntervalPerfIfIndex,_W:msdslFarEndIntervalPerfNumber,'msdslFarEndIntervalPerfMargin':msdslFarEndIntervalPerfMargin,'msdslFarEndIntervalPerfTxPwr':msdslFarEndIntervalPerfTxPwr,'msdslFarEndIntervalPerfRxGain':msdslFarEndIntervalPerfRxGain,'msdsldsx1WorstInterval':msdsldsx1WorstInterval,'msdsldsx1WorstIntervalTable':msdsldsx1WorstIntervalTable,'msdsldsx1WorstIntervalEntry':msdsldsx1WorstIntervalEntry,_X:msdsldsx1WorstIntervalIfIndex,'msdsldsx1WorstIntervalESs':msdsldsx1WorstIntervalESs,'msdsldsx1WorstIntervalUASs':msdsldsx1WorstIntervalUASs,'msdsldsx1WorstIntervalSESs':msdsldsx1WorstIntervalSESs,'msdsldsx1WorstIntervalBESs':msdsldsx1WorstIntervalBESs,'msdsldsx1WorstIntervalCSSs':msdsldsx1WorstIntervalCSSs,'msdsldsx1WorstIntervalLOFC':msdsldsx1WorstIntervalLOFC,'msdslG703WorstInterval':msdslG703WorstInterval,'msdslG703WorstIntervalTable':msdslG703WorstIntervalTable,'msdslG703WorstIntervalEntry':msdslG703WorstIntervalEntry,_Y:msdslG703WorstIntervalIfIndex,'msdslG703WorstIntervalESs':msdslG703WorstIntervalESs,'msdslG703WorstIntervalUASs':msdslG703WorstIntervalUASs,'msdslG703WorstIntervalSESs':msdslG703WorstIntervalSESs,'msdslG703WorstIntervalBESs':msdslG703WorstIntervalBESs,'msdslG703WorstIntervalCSSs':msdslG703WorstIntervalCSSs,'msdslG703WorstIntervalLOFC':msdslG703WorstIntervalLOFC,'msdslConfiguration':msdslConfiguration,'msdslFracTable':msdslFracTable,'msdslFracEntry':msdslFracEntry,_Z:msdslFracPortIndex,_a:msdslFracPortTS,'msdslFracPortIfIndex':msdslFracPortIfIndex,'msdslFracPortIfTS':msdslFracPortIfTS,'msdslFracPortVoiceData':msdslFracPortVoiceData,'msdslPortConfigAllocMethodTable':msdslPortConfigAllocMethodTable,'msdslPortConfigAllocMethodEntry':msdslPortConfigAllocMethodEntry,_b:msdslPortConfigAllocMethodIfIndex,'msdslPortConfigAllocMethod':msdslPortConfigAllocMethod})