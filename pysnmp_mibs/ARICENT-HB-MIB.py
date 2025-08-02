_F='TruthValue'
_E='Integer32'
_D='Unsigned32'
_C='read-only'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ZeroBasedCounter32,=mibBuilder.importSymbols('RMON2-MIB','ZeroBasedCounter32')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'enterprises','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_F)
fsHb=ModuleIdentity((1,3,6,1,4,1,29601,2,93))
if mibBuilder.loadTexts:fsHb.setRevisions(('2014-12-10 00:00',))
_FsHbScalar_ObjectIdentity=ObjectIdentity
fsHbScalar=_FsHbScalar_ObjectIdentity((1,3,6,1,4,1,29601,2,93,0))
class _FsHbInterval_Type(Unsigned32):defaultValue=500;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,5000))
_FsHbInterval_Type.__name__=_D
_FsHbInterval_Object=MibScalar
fsHbInterval=_FsHbInterval_Object((1,3,6,1,4,1,29601,2,93,0,1),_FsHbInterval_Type())
fsHbInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:fsHbInterval.setStatus(_A)
class _FsHbPeerDeadIntMultiplier_Type(Unsigned32):defaultValue=4;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,10))
_FsHbPeerDeadIntMultiplier_Type.__name__=_D
_FsHbPeerDeadIntMultiplier_Object=MibScalar
fsHbPeerDeadIntMultiplier=_FsHbPeerDeadIntMultiplier_Object((1,3,6,1,4,1,29601,2,93,0,2),_FsHbPeerDeadIntMultiplier_Type())
fsHbPeerDeadIntMultiplier.setMaxAccess(_B)
if mibBuilder.loadTexts:fsHbPeerDeadIntMultiplier.setStatus(_A)
class _FsHbTrcLevel_Type(Unsigned32):defaultValue=0
_FsHbTrcLevel_Type.__name__=_D
_FsHbTrcLevel_Object=MibScalar
fsHbTrcLevel=_FsHbTrcLevel_Object((1,3,6,1,4,1,29601,2,93,0,3),_FsHbTrcLevel_Type())
fsHbTrcLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:fsHbTrcLevel.setStatus(_A)
class _FsHbStatsEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_FsHbStatsEnable_Type.__name__=_E
_FsHbStatsEnable_Object=MibScalar
fsHbStatsEnable=_FsHbStatsEnable_Object((1,3,6,1,4,1,29601,2,93,0,4),_FsHbStatsEnable_Type())
fsHbStatsEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:fsHbStatsEnable.setStatus(_A)
class _FsHbClearStats_Type(TruthValue):defaultValue=2
_FsHbClearStats_Type.__name__=_F
_FsHbClearStats_Object=MibScalar
fsHbClearStats=_FsHbClearStats_Object((1,3,6,1,4,1,29601,2,93,0,5),_FsHbClearStats_Type())
fsHbClearStats.setMaxAccess(_B)
if mibBuilder.loadTexts:fsHbClearStats.setStatus(_A)
_FsHbStatistics_ObjectIdentity=ObjectIdentity
fsHbStatistics=_FsHbStatistics_ObjectIdentity((1,3,6,1,4,1,29601,2,93,1))
_FsHbStatsMsgTxCount_Type=ZeroBasedCounter32
_FsHbStatsMsgTxCount_Object=MibScalar
fsHbStatsMsgTxCount=_FsHbStatsMsgTxCount_Object((1,3,6,1,4,1,29601,2,93,1,1),_FsHbStatsMsgTxCount_Type())
fsHbStatsMsgTxCount.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHbStatsMsgTxCount.setStatus(_A)
_FsHbStatsMsgTxFailedCount_Type=ZeroBasedCounter32
_FsHbStatsMsgTxFailedCount_Object=MibScalar
fsHbStatsMsgTxFailedCount=_FsHbStatsMsgTxFailedCount_Object((1,3,6,1,4,1,29601,2,93,1,2),_FsHbStatsMsgTxFailedCount_Type())
fsHbStatsMsgTxFailedCount.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHbStatsMsgTxFailedCount.setStatus(_A)
_FsHbStatsMsgRxCount_Type=ZeroBasedCounter32
_FsHbStatsMsgRxCount_Object=MibScalar
fsHbStatsMsgRxCount=_FsHbStatsMsgRxCount_Object((1,3,6,1,4,1,29601,2,93,1,3),_FsHbStatsMsgRxCount_Type())
fsHbStatsMsgRxCount.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHbStatsMsgRxCount.setStatus(_A)
_FsHbStatsMsgRxProcCount_Type=ZeroBasedCounter32
_FsHbStatsMsgRxProcCount_Object=MibScalar
fsHbStatsMsgRxProcCount=_FsHbStatsMsgRxProcCount_Object((1,3,6,1,4,1,29601,2,93,1,4),_FsHbStatsMsgRxProcCount_Type())
fsHbStatsMsgRxProcCount.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHbStatsMsgRxProcCount.setStatus(_A)
_FsHbStatsRxFailedCount_Type=ZeroBasedCounter32
_FsHbStatsRxFailedCount_Object=MibScalar
fsHbStatsRxFailedCount=_FsHbStatsRxFailedCount_Object((1,3,6,1,4,1,29601,2,93,1,5),_FsHbStatsRxFailedCount_Type())
fsHbStatsRxFailedCount.setMaxAccess(_C)
if mibBuilder.loadTexts:fsHbStatsRxFailedCount.setStatus(_A)
mibBuilder.exportSymbols('ARICENT-HB-MIB',**{'fsHb':fsHb,'fsHbScalar':fsHbScalar,'fsHbInterval':fsHbInterval,'fsHbPeerDeadIntMultiplier':fsHbPeerDeadIntMultiplier,'fsHbTrcLevel':fsHbTrcLevel,'fsHbStatsEnable':fsHbStatsEnable,'fsHbClearStats':fsHbClearStats,'fsHbStatistics':fsHbStatistics,'fsHbStatsMsgTxCount':fsHbStatsMsgTxCount,'fsHbStatsMsgTxFailedCount':fsHbStatsMsgTxFailedCount,'fsHbStatsMsgRxCount':fsHbStatsMsgRxCount,'fsHbStatsMsgRxProcCount':fsHbStatsMsgRxProcCount,'fsHbStatsRxFailedCount':fsHbStatsRxFailedCount})