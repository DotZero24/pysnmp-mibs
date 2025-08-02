_G='rmonStatsEntry'
_F='SUPERMICRO-RMON-MIB'
_E='supported'
_D='notsupported'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
etherStatsEntry,=mibBuilder.importSymbols('RMON-MIB','etherStatsEntry')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
futrmon=ModuleIdentity((1,3,6,1,4,1,10876,101,1,44))
if mibBuilder.loadTexts:futrmon.setRevisions(('2012-09-05 00:00',))
_RmonDebugType_Type=Unsigned32
_RmonDebugType_Object=MibScalar
rmonDebugType=_RmonDebugType_Object((1,3,6,1,4,1,10876,101,1,44,1),_RmonDebugType_Type())
rmonDebugType.setMaxAccess(_C)
if mibBuilder.loadTexts:rmonDebugType.setStatus(_A)
class _RmonEnableStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('rmonenabled',1),('rmondisabled',2)))
_RmonEnableStatus_Type.__name__=_B
_RmonEnableStatus_Object=MibScalar
rmonEnableStatus=_RmonEnableStatus_Object((1,3,6,1,4,1,10876,101,1,44,2),_RmonEnableStatus_Type())
rmonEnableStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rmonEnableStatus.setStatus(_A)
class _RmonHwStatsSupp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RmonHwStatsSupp_Type.__name__=_B
_RmonHwStatsSupp_Object=MibScalar
rmonHwStatsSupp=_RmonHwStatsSupp_Object((1,3,6,1,4,1,10876,101,1,44,3),_RmonHwStatsSupp_Type())
rmonHwStatsSupp.setMaxAccess(_C)
if mibBuilder.loadTexts:rmonHwStatsSupp.setStatus(_A)
class _RmonHwHistorySupp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RmonHwHistorySupp_Type.__name__=_B
_RmonHwHistorySupp_Object=MibScalar
rmonHwHistorySupp=_RmonHwHistorySupp_Object((1,3,6,1,4,1,10876,101,1,44,4),_RmonHwHistorySupp_Type())
rmonHwHistorySupp.setMaxAccess(_C)
if mibBuilder.loadTexts:rmonHwHistorySupp.setStatus(_A)
class _RmonHwAlarmSupp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RmonHwAlarmSupp_Type.__name__=_B
_RmonHwAlarmSupp_Object=MibScalar
rmonHwAlarmSupp=_RmonHwAlarmSupp_Object((1,3,6,1,4,1,10876,101,1,44,5),_RmonHwAlarmSupp_Type())
rmonHwAlarmSupp.setMaxAccess(_C)
if mibBuilder.loadTexts:rmonHwAlarmSupp.setStatus(_A)
class _RmonHwHostSupp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RmonHwHostSupp_Type.__name__=_B
_RmonHwHostSupp_Object=MibScalar
rmonHwHostSupp=_RmonHwHostSupp_Object((1,3,6,1,4,1,10876,101,1,44,6),_RmonHwHostSupp_Type())
rmonHwHostSupp.setMaxAccess(_C)
if mibBuilder.loadTexts:rmonHwHostSupp.setStatus(_A)
class _RmonHwHostTopNSupp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RmonHwHostTopNSupp_Type.__name__=_B
_RmonHwHostTopNSupp_Object=MibScalar
rmonHwHostTopNSupp=_RmonHwHostTopNSupp_Object((1,3,6,1,4,1,10876,101,1,44,7),_RmonHwHostTopNSupp_Type())
rmonHwHostTopNSupp.setMaxAccess(_C)
if mibBuilder.loadTexts:rmonHwHostTopNSupp.setStatus(_A)
class _RmonHwMatrixSupp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RmonHwMatrixSupp_Type.__name__=_B
_RmonHwMatrixSupp_Object=MibScalar
rmonHwMatrixSupp=_RmonHwMatrixSupp_Object((1,3,6,1,4,1,10876,101,1,44,8),_RmonHwMatrixSupp_Type())
rmonHwMatrixSupp.setMaxAccess(_C)
if mibBuilder.loadTexts:rmonHwMatrixSupp.setStatus(_A)
class _RmonHwEventSupp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RmonHwEventSupp_Type.__name__=_B
_RmonHwEventSupp_Object=MibScalar
rmonHwEventSupp=_RmonHwEventSupp_Object((1,3,6,1,4,1,10876,101,1,44,9),_RmonHwEventSupp_Type())
rmonHwEventSupp.setMaxAccess(_C)
if mibBuilder.loadTexts:rmonHwEventSupp.setStatus(_A)
_RmonStatsTable_Object=MibTable
rmonStatsTable=_RmonStatsTable_Object((1,3,6,1,4,1,10876,101,1,44,10))
if mibBuilder.loadTexts:rmonStatsTable.setStatus(_A)
_RmonStatsEntry_Object=MibTableRow
rmonStatsEntry=_RmonStatsEntry_Object((1,3,6,1,4,1,10876,101,1,44,10,1))
if mibBuilder.loadTexts:rmonStatsEntry.setStatus(_A)
_RmonStatsOutFCSErrors_Type=Counter32
_RmonStatsOutFCSErrors_Object=MibTableColumn
rmonStatsOutFCSErrors=_RmonStatsOutFCSErrors_Object((1,3,6,1,4,1,10876,101,1,44,10,1,1),_RmonStatsOutFCSErrors_Type())
rmonStatsOutFCSErrors.setMaxAccess('read-only')
if mibBuilder.loadTexts:rmonStatsOutFCSErrors.setStatus(_A)
etherStatsEntry.registerAugmentions((_F,_G))
rmonStatsEntry.setIndexNames(*etherStatsEntry.getIndexNames())
mibBuilder.exportSymbols(_F,**{'futrmon':futrmon,'rmonDebugType':rmonDebugType,'rmonEnableStatus':rmonEnableStatus,'rmonHwStatsSupp':rmonHwStatsSupp,'rmonHwHistorySupp':rmonHwHistorySupp,'rmonHwAlarmSupp':rmonHwAlarmSupp,'rmonHwHostSupp':rmonHwHostSupp,'rmonHwHostTopNSupp':rmonHwHostTopNSupp,'rmonHwMatrixSupp':rmonHwMatrixSupp,'rmonHwEventSupp':rmonHwEventSupp,'rmonStatsTable':rmonStatsTable,_G:rmonStatsEntry,'rmonStatsOutFCSErrors':rmonStatsOutFCSErrors})