_G='fsMIPingIndex'
_F='ARICENT-MIPING-MIB'
_E='OctetString'
_D='read-only'
_C='read-create'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
fsMIPingMIB=ModuleIdentity((1,3,6,1,4,1,29601,2,36))
if mibBuilder.loadTexts:fsMIPingMIB.setRevisions(('2012-09-05 00:00',))
_FsMIPingMIBObjects_ObjectIdentity=ObjectIdentity
fsMIPingMIBObjects=_FsMIPingMIBObjects_ObjectIdentity((1,3,6,1,4,1,29601,2,36,1))
_FsMIPingTable_Object=MibTable
fsMIPingTable=_FsMIPingTable_Object((1,3,6,1,4,1,29601,2,36,1,1))
if mibBuilder.loadTexts:fsMIPingTable.setStatus(_A)
_FsMIPingEntry_Object=MibTableRow
fsMIPingEntry=_FsMIPingEntry_Object((1,3,6,1,4,1,29601,2,36,1,1,1))
fsMIPingEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:fsMIPingEntry.setStatus(_A)
class _FsMIPingIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FsMIPingIndex_Type.__name__=_B
_FsMIPingIndex_Object=MibTableColumn
fsMIPingIndex=_FsMIPingIndex_Object((1,3,6,1,4,1,29601,2,36,1,1,1,1),_FsMIPingIndex_Type())
fsMIPingIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:fsMIPingIndex.setStatus(_A)
_FsMIPingDest_Type=IpAddress
_FsMIPingDest_Object=MibTableColumn
fsMIPingDest=_FsMIPingDest_Object((1,3,6,1,4,1,29601,2,36,1,1,1,2),_FsMIPingDest_Type())
fsMIPingDest.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIPingDest.setStatus(_A)
class _FsMIPingContextId_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsMIPingContextId_Type.__name__=_B
_FsMIPingContextId_Object=MibTableColumn
fsMIPingContextId=_FsMIPingContextId_Object((1,3,6,1,4,1,29601,2,36,1,1,1,3),_FsMIPingContextId_Type())
fsMIPingContextId.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIPingContextId.setStatus(_A)
class _FsMIPingTimeout_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_FsMIPingTimeout_Type.__name__=_B
_FsMIPingTimeout_Object=MibTableColumn
fsMIPingTimeout=_FsMIPingTimeout_Object((1,3,6,1,4,1,29601,2,36,1,1,1,4),_FsMIPingTimeout_Type())
fsMIPingTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIPingTimeout.setStatus(_A)
class _FsMIPingTries_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_FsMIPingTries_Type.__name__=_B
_FsMIPingTries_Object=MibTableColumn
fsMIPingTries=_FsMIPingTries_Object((1,3,6,1,4,1,29601,2,36,1,1,1,5),_FsMIPingTries_Type())
fsMIPingTries.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIPingTries.setStatus(_A)
class _FsMIPingDataSize_Type(Integer32):defaultValue=64;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2080))
_FsMIPingDataSize_Type.__name__=_B
_FsMIPingDataSize_Object=MibTableColumn
fsMIPingDataSize=_FsMIPingDataSize_Object((1,3,6,1,4,1,29601,2,36,1,1,1,6),_FsMIPingDataSize_Type())
fsMIPingDataSize.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIPingDataSize.setStatus(_A)
class _FsMIPingStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notinitiated',1),('progress',2),('completed',3)))
_FsMIPingStatus_Type.__name__=_B
_FsMIPingStatus_Object=MibTableColumn
fsMIPingStatus=_FsMIPingStatus_Object((1,3,6,1,4,1,29601,2,36,1,1,1,7),_FsMIPingStatus_Type())
fsMIPingStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIPingStatus.setStatus(_A)
class _FsMIPingSendCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FsMIPingSendCount_Type.__name__=_B
_FsMIPingSendCount_Object=MibTableColumn
fsMIPingSendCount=_FsMIPingSendCount_Object((1,3,6,1,4,1,29601,2,36,1,1,1,8),_FsMIPingSendCount_Type())
fsMIPingSendCount.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIPingSendCount.setStatus(_A)
class _FsMIPingAverageTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FsMIPingAverageTime_Type.__name__=_B
_FsMIPingAverageTime_Object=MibTableColumn
fsMIPingAverageTime=_FsMIPingAverageTime_Object((1,3,6,1,4,1,29601,2,36,1,1,1,9),_FsMIPingAverageTime_Type())
fsMIPingAverageTime.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIPingAverageTime.setStatus(_A)
class _FsMIPingMaxTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FsMIPingMaxTime_Type.__name__=_B
_FsMIPingMaxTime_Object=MibTableColumn
fsMIPingMaxTime=_FsMIPingMaxTime_Object((1,3,6,1,4,1,29601,2,36,1,1,1,10),_FsMIPingMaxTime_Type())
fsMIPingMaxTime.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIPingMaxTime.setStatus(_A)
class _FsMIPingMinTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FsMIPingMinTime_Type.__name__=_B
_FsMIPingMinTime_Object=MibTableColumn
fsMIPingMinTime=_FsMIPingMinTime_Object((1,3,6,1,4,1,29601,2,36,1,1,1,11),_FsMIPingMinTime_Type())
fsMIPingMinTime.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIPingMinTime.setStatus(_A)
_FsMIPingSuccesses_Type=Counter32
_FsMIPingSuccesses_Object=MibTableColumn
fsMIPingSuccesses=_FsMIPingSuccesses_Object((1,3,6,1,4,1,29601,2,36,1,1,1,12),_FsMIPingSuccesses_Type())
fsMIPingSuccesses.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIPingSuccesses.setStatus(_A)
_FsMIPingEntryStatus_Type=RowStatus
_FsMIPingEntryStatus_Object=MibTableColumn
fsMIPingEntryStatus=_FsMIPingEntryStatus_Object((1,3,6,1,4,1,29601,2,36,1,1,1,13),_FsMIPingEntryStatus_Type())
fsMIPingEntryStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIPingEntryStatus.setStatus(_A)
class _FsMIPingHostName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_FsMIPingHostName_Type.__name__=_E
_FsMIPingHostName_Object=MibTableColumn
fsMIPingHostName=_FsMIPingHostName_Object((1,3,6,1,4,1,29601,2,36,1,1,1,14),_FsMIPingHostName_Type())
fsMIPingHostName.setMaxAccess('read-write')
if mibBuilder.loadTexts:fsMIPingHostName.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'fsMIPingMIB':fsMIPingMIB,'fsMIPingMIBObjects':fsMIPingMIBObjects,'fsMIPingTable':fsMIPingTable,'fsMIPingEntry':fsMIPingEntry,_G:fsMIPingIndex,'fsMIPingDest':fsMIPingDest,'fsMIPingContextId':fsMIPingContextId,'fsMIPingTimeout':fsMIPingTimeout,'fsMIPingTries':fsMIPingTries,'fsMIPingDataSize':fsMIPingDataSize,'fsMIPingStatus':fsMIPingStatus,'fsMIPingSendCount':fsMIPingSendCount,'fsMIPingAverageTime':fsMIPingAverageTime,'fsMIPingMaxTime':fsMIPingMaxTime,'fsMIPingMinTime':fsMIPingMinTime,'fsMIPingSuccesses':fsMIPingSuccesses,'fsMIPingEntryStatus':fsMIPingEntryStatus,'fsMIPingHostName':fsMIPingHostName})