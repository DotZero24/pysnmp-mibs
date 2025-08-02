_D='bKafkaClientLatencyStatsInterval'
_C='BENU-KAFKA-CLIENT-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
benuWAG,=mibBuilder.importSymbols('BENU-WAG-MIB','benuWAG')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
benuKafkaClientMIB=ModuleIdentity((1,3,6,1,4,1,39406,2,1,12))
if mibBuilder.loadTexts:benuKafkaClientMIB.setRevisions(('2015-10-21 00:00',))
_BKafkaClientObjects_ObjectIdentity=ObjectIdentity
bKafkaClientObjects=_BKafkaClientObjects_ObjectIdentity((1,3,6,1,4,1,39406,2,1,12,1))
if mibBuilder.loadTexts:bKafkaClientObjects.setStatus(_A)
_BKafkaClientLatencyTable_Object=MibTable
bKafkaClientLatencyTable=_BKafkaClientLatencyTable_Object((1,3,6,1,4,1,39406,2,1,12,1,1))
if mibBuilder.loadTexts:bKafkaClientLatencyTable.setStatus(_A)
_BKafkaClientLatencyEntry_Object=MibTableRow
bKafkaClientLatencyEntry=_BKafkaClientLatencyEntry_Object((1,3,6,1,4,1,39406,2,1,12,1,1,1))
bKafkaClientLatencyEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:bKafkaClientLatencyEntry.setStatus(_A)
_BKafkaClientLatencyStatsInterval_Type=Integer32
_BKafkaClientLatencyStatsInterval_Object=MibTableColumn
bKafkaClientLatencyStatsInterval=_BKafkaClientLatencyStatsInterval_Object((1,3,6,1,4,1,39406,2,1,12,1,1,1,1),_BKafkaClientLatencyStatsInterval_Type())
bKafkaClientLatencyStatsInterval.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:bKafkaClientLatencyStatsInterval.setStatus(_A)
_BKafkaClientLatencyStatsIntervalDuration_Type=Integer32
_BKafkaClientLatencyStatsIntervalDuration_Object=MibTableColumn
bKafkaClientLatencyStatsIntervalDuration=_BKafkaClientLatencyStatsIntervalDuration_Object((1,3,6,1,4,1,39406,2,1,12,1,1,1,2),_BKafkaClientLatencyStatsIntervalDuration_Type())
bKafkaClientLatencyStatsIntervalDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:bKafkaClientLatencyStatsIntervalDuration.setStatus(_A)
_BKafkaClientLatencyTotalPktCount_Type=Unsigned32
_BKafkaClientLatencyTotalPktCount_Object=MibTableColumn
bKafkaClientLatencyTotalPktCount=_BKafkaClientLatencyTotalPktCount_Object((1,3,6,1,4,1,39406,2,1,12,1,1,1,3),_BKafkaClientLatencyTotalPktCount_Type())
bKafkaClientLatencyTotalPktCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bKafkaClientLatencyTotalPktCount.setStatus(_A)
_BKafkaClientLatencyMaxProcessingTime_Type=Unsigned32
_BKafkaClientLatencyMaxProcessingTime_Object=MibTableColumn
bKafkaClientLatencyMaxProcessingTime=_BKafkaClientLatencyMaxProcessingTime_Object((1,3,6,1,4,1,39406,2,1,12,1,1,1,4),_BKafkaClientLatencyMaxProcessingTime_Type())
bKafkaClientLatencyMaxProcessingTime.setMaxAccess(_B)
if mibBuilder.loadTexts:bKafkaClientLatencyMaxProcessingTime.setStatus(_A)
_BKafkaClientLatencyMinProcessingTime_Type=Unsigned32
_BKafkaClientLatencyMinProcessingTime_Object=MibTableColumn
bKafkaClientLatencyMinProcessingTime=_BKafkaClientLatencyMinProcessingTime_Object((1,3,6,1,4,1,39406,2,1,12,1,1,1,5),_BKafkaClientLatencyMinProcessingTime_Type())
bKafkaClientLatencyMinProcessingTime.setMaxAccess(_B)
if mibBuilder.loadTexts:bKafkaClientLatencyMinProcessingTime.setStatus(_A)
_BKafkaClientLatencyAvgProcessingTime_Type=Unsigned32
_BKafkaClientLatencyAvgProcessingTime_Object=MibTableColumn
bKafkaClientLatencyAvgProcessingTime=_BKafkaClientLatencyAvgProcessingTime_Object((1,3,6,1,4,1,39406,2,1,12,1,1,1,6),_BKafkaClientLatencyAvgProcessingTime_Type())
bKafkaClientLatencyAvgProcessingTime.setMaxAccess(_B)
if mibBuilder.loadTexts:bKafkaClientLatencyAvgProcessingTime.setStatus(_A)
_BKafkaClientLatencyProcessTimeMorethan1MSPktCount_Type=Unsigned32
_BKafkaClientLatencyProcessTimeMorethan1MSPktCount_Object=MibTableColumn
bKafkaClientLatencyProcessTimeMorethan1MSPktCount=_BKafkaClientLatencyProcessTimeMorethan1MSPktCount_Object((1,3,6,1,4,1,39406,2,1,12,1,1,1,7),_BKafkaClientLatencyProcessTimeMorethan1MSPktCount_Type())
bKafkaClientLatencyProcessTimeMorethan1MSPktCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bKafkaClientLatencyProcessTimeMorethan1MSPktCount.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'benuKafkaClientMIB':benuKafkaClientMIB,'bKafkaClientObjects':bKafkaClientObjects,'bKafkaClientLatencyTable':bKafkaClientLatencyTable,'bKafkaClientLatencyEntry':bKafkaClientLatencyEntry,_D:bKafkaClientLatencyStatsInterval,'bKafkaClientLatencyStatsIntervalDuration':bKafkaClientLatencyStatsIntervalDuration,'bKafkaClientLatencyTotalPktCount':bKafkaClientLatencyTotalPktCount,'bKafkaClientLatencyMaxProcessingTime':bKafkaClientLatencyMaxProcessingTime,'bKafkaClientLatencyMinProcessingTime':bKafkaClientLatencyMinProcessingTime,'bKafkaClientLatencyAvgProcessingTime':bKafkaClientLatencyAvgProcessingTime,'bKafkaClientLatencyProcessTimeMorethan1MSPktCount':bKafkaClientLatencyProcessTimeMorethan1MSPktCount})