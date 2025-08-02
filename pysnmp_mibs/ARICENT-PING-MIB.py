_G='fsPingIndex'
_F='ARICENT-PING-MIB'
_E='OctetString'
_D='read-create'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
fsPingMIB=ModuleIdentity((1,3,6,1,4,1,2076,106))
if mibBuilder.loadTexts:fsPingMIB.setRevisions(('2012-09-05 00:00',))
_FsPingMIBObjects_ObjectIdentity=ObjectIdentity
fsPingMIBObjects=_FsPingMIBObjects_ObjectIdentity((1,3,6,1,4,1,2076,106,1))
_FsPingTable_Object=MibTable
fsPingTable=_FsPingTable_Object((1,3,6,1,4,1,2076,106,1,1))
if mibBuilder.loadTexts:fsPingTable.setStatus(_A)
_FsPingEntry_Object=MibTableRow
fsPingEntry=_FsPingEntry_Object((1,3,6,1,4,1,2076,106,1,1,1))
fsPingEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:fsPingEntry.setStatus(_A)
class _FsPingIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FsPingIndex_Type.__name__=_B
_FsPingIndex_Object=MibTableColumn
fsPingIndex=_FsPingIndex_Object((1,3,6,1,4,1,2076,106,1,1,1,1),_FsPingIndex_Type())
fsPingIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:fsPingIndex.setStatus(_A)
_FsPingDest_Type=IpAddress
_FsPingDest_Object=MibTableColumn
fsPingDest=_FsPingDest_Object((1,3,6,1,4,1,2076,106,1,1,1,2),_FsPingDest_Type())
fsPingDest.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPingDest.setStatus(_A)
class _FsPingTimeout_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_FsPingTimeout_Type.__name__=_B
_FsPingTimeout_Object=MibTableColumn
fsPingTimeout=_FsPingTimeout_Object((1,3,6,1,4,1,2076,106,1,1,1,3),_FsPingTimeout_Type())
fsPingTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPingTimeout.setStatus(_A)
class _FsPingTries_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_FsPingTries_Type.__name__=_B
_FsPingTries_Object=MibTableColumn
fsPingTries=_FsPingTries_Object((1,3,6,1,4,1,2076,106,1,1,1,4),_FsPingTries_Type())
fsPingTries.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPingTries.setStatus(_A)
class _FsPingDataSize_Type(Integer32):defaultValue=64;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2080))
_FsPingDataSize_Type.__name__=_B
_FsPingDataSize_Object=MibTableColumn
fsPingDataSize=_FsPingDataSize_Object((1,3,6,1,4,1,2076,106,1,1,1,5),_FsPingDataSize_Type())
fsPingDataSize.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPingDataSize.setStatus(_A)
class _FsPingStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notinitiated',1),('progress',2),('completed',3)))
_FsPingStatus_Type.__name__=_B
_FsPingStatus_Object=MibTableColumn
fsPingStatus=_FsPingStatus_Object((1,3,6,1,4,1,2076,106,1,1,1,6),_FsPingStatus_Type())
fsPingStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPingStatus.setStatus(_A)
class _FsPingSendCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FsPingSendCount_Type.__name__=_B
_FsPingSendCount_Object=MibTableColumn
fsPingSendCount=_FsPingSendCount_Object((1,3,6,1,4,1,2076,106,1,1,1,7),_FsPingSendCount_Type())
fsPingSendCount.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPingSendCount.setStatus(_A)
class _FsPingAverageTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FsPingAverageTime_Type.__name__=_B
_FsPingAverageTime_Object=MibTableColumn
fsPingAverageTime=_FsPingAverageTime_Object((1,3,6,1,4,1,2076,106,1,1,1,8),_FsPingAverageTime_Type())
fsPingAverageTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPingAverageTime.setStatus(_A)
class _FsPingMaxTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FsPingMaxTime_Type.__name__=_B
_FsPingMaxTime_Object=MibTableColumn
fsPingMaxTime=_FsPingMaxTime_Object((1,3,6,1,4,1,2076,106,1,1,1,9),_FsPingMaxTime_Type())
fsPingMaxTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPingMaxTime.setStatus(_A)
class _FsPingMinTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FsPingMinTime_Type.__name__=_B
_FsPingMinTime_Object=MibTableColumn
fsPingMinTime=_FsPingMinTime_Object((1,3,6,1,4,1,2076,106,1,1,1,10),_FsPingMinTime_Type())
fsPingMinTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPingMinTime.setStatus(_A)
_FsPingSuccesses_Type=Counter32
_FsPingSuccesses_Object=MibTableColumn
fsPingSuccesses=_FsPingSuccesses_Object((1,3,6,1,4,1,2076,106,1,1,1,11),_FsPingSuccesses_Type())
fsPingSuccesses.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPingSuccesses.setStatus(_A)
_FsPingEntryStatus_Type=RowStatus
_FsPingEntryStatus_Object=MibTableColumn
fsPingEntryStatus=_FsPingEntryStatus_Object((1,3,6,1,4,1,2076,106,1,1,1,12),_FsPingEntryStatus_Type())
fsPingEntryStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPingEntryStatus.setStatus(_A)
class _FsPingHostName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_FsPingHostName_Type.__name__=_E
_FsPingHostName_Object=MibTableColumn
fsPingHostName=_FsPingHostName_Object((1,3,6,1,4,1,2076,106,1,1,1,13),_FsPingHostName_Type())
fsPingHostName.setMaxAccess('read-write')
if mibBuilder.loadTexts:fsPingHostName.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'fsPingMIB':fsPingMIB,'fsPingMIBObjects':fsPingMIBObjects,'fsPingTable':fsPingTable,'fsPingEntry':fsPingEntry,_G:fsPingIndex,'fsPingDest':fsPingDest,'fsPingTimeout':fsPingTimeout,'fsPingTries':fsPingTries,'fsPingDataSize':fsPingDataSize,'fsPingStatus':fsPingStatus,'fsPingSendCount':fsPingSendCount,'fsPingAverageTime':fsPingAverageTime,'fsPingMaxTime':fsPingMaxTime,'fsPingMinTime':fsPingMinTime,'fsPingSuccesses':fsPingSuccesses,'fsPingEntryStatus':fsPingEntryStatus,'fsPingHostName':fsPingHostName})