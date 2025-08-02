_U='altigaT1E1StatsGroup'
_T='alT1E1StatsLESs'
_S='alT1E1StatsPCVs'
_R='alT1E1StatsDMs'
_Q='alT1E1StatsCSSs'
_P='alT1E1StatsLCVs'
_O='alT1E1StatsUASs'
_N='alT1E1StatsSEFSs'
_M='alT1E1StatsBESs'
_L='alT1E1StatsSESs'
_K='alT1E1StatsESs'
_J='alT1E1StatsBPVs'
_I='alT1E1StatsElapsedSecs'
_H='alT1E1StatsLineStatus'
_G='alT1E1StatsRowStatus'
_F='Integer32'
_E='alT1E1StatsConn'
_D='alT1E1StatsSlot'
_C='read-only'
_B='ALTIGA-T1E1-STATS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
alT1E1MibModule,=mibBuilder.importSymbols('ALTIGA-GLOBAL-REG','alT1E1MibModule')
alStatsT1E1,alT1E1Group=mibBuilder.importSymbols('ALTIGA-MIB','alStatsT1E1','alT1E1Group')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
altigaT1E1StatsMibModule=ModuleIdentity((1,3,6,1,4,1,3076,1,1,38,2))
if mibBuilder.loadTexts:altigaT1E1StatsMibModule.setRevisions(('2002-09-05 13:00','2002-07-10 00:00'))
_AltigaT1E1StatsMibConformance_ObjectIdentity=ObjectIdentity
altigaT1E1StatsMibConformance=_AltigaT1E1StatsMibConformance_ObjectIdentity((1,3,6,1,4,1,3076,1,1,38,2,1))
_AltigaT1E1StatsMibCompliances_ObjectIdentity=ObjectIdentity
altigaT1E1StatsMibCompliances=_AltigaT1E1StatsMibCompliances_ObjectIdentity((1,3,6,1,4,1,3076,1,1,38,2,1,1))
_AlStatsT1E1Global_ObjectIdentity=ObjectIdentity
alStatsT1E1Global=_AlStatsT1E1Global_ObjectIdentity((1,3,6,1,4,1,3076,2,1,2,33,1))
_AlT1E1StatsTable_Object=MibTable
alT1E1StatsTable=_AlT1E1StatsTable_Object((1,3,6,1,4,1,3076,2,1,2,33,2))
if mibBuilder.loadTexts:alT1E1StatsTable.setStatus(_A)
_AlT1E1StatsEntry_Object=MibTableRow
alT1E1StatsEntry=_AlT1E1StatsEntry_Object((1,3,6,1,4,1,3076,2,1,2,33,2,1))
alT1E1StatsEntry.setIndexNames((0,_B,_D),(0,_B,_E))
if mibBuilder.loadTexts:alT1E1StatsEntry.setStatus(_A)
_AlT1E1StatsRowStatus_Type=RowStatus
_AlT1E1StatsRowStatus_Object=MibTableColumn
alT1E1StatsRowStatus=_AlT1E1StatsRowStatus_Object((1,3,6,1,4,1,3076,2,1,2,33,2,1,1),_AlT1E1StatsRowStatus_Type())
alT1E1StatsRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:alT1E1StatsRowStatus.setStatus(_A)
_AlT1E1StatsSlot_Type=Integer32
_AlT1E1StatsSlot_Object=MibTableColumn
alT1E1StatsSlot=_AlT1E1StatsSlot_Object((1,3,6,1,4,1,3076,2,1,2,33,2,1,2),_AlT1E1StatsSlot_Type())
alT1E1StatsSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:alT1E1StatsSlot.setStatus(_A)
_AlT1E1StatsConn_Type=Integer32
_AlT1E1StatsConn_Object=MibTableColumn
alT1E1StatsConn=_AlT1E1StatsConn_Object((1,3,6,1,4,1,3076,2,1,2,33,2,1,3),_AlT1E1StatsConn_Type())
alT1E1StatsConn.setMaxAccess(_C)
if mibBuilder.loadTexts:alT1E1StatsConn.setStatus(_A)
class _AlT1E1StatsLineStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('init',1),('up',2),('red',3),('blue',4),('yellow',5),('loopback',6)))
_AlT1E1StatsLineStatus_Type.__name__=_F
_AlT1E1StatsLineStatus_Object=MibTableColumn
alT1E1StatsLineStatus=_AlT1E1StatsLineStatus_Object((1,3,6,1,4,1,3076,2,1,2,33,2,1,4),_AlT1E1StatsLineStatus_Type())
alT1E1StatsLineStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:alT1E1StatsLineStatus.setStatus(_A)
_AlT1E1StatsElapsedSecs_Type=Counter32
_AlT1E1StatsElapsedSecs_Object=MibTableColumn
alT1E1StatsElapsedSecs=_AlT1E1StatsElapsedSecs_Object((1,3,6,1,4,1,3076,2,1,2,33,2,1,5),_AlT1E1StatsElapsedSecs_Type())
alT1E1StatsElapsedSecs.setMaxAccess(_C)
if mibBuilder.loadTexts:alT1E1StatsElapsedSecs.setStatus(_A)
_AlT1E1StatsBPVs_Type=Counter32
_AlT1E1StatsBPVs_Object=MibTableColumn
alT1E1StatsBPVs=_AlT1E1StatsBPVs_Object((1,3,6,1,4,1,3076,2,1,2,33,2,1,6),_AlT1E1StatsBPVs_Type())
alT1E1StatsBPVs.setMaxAccess(_C)
if mibBuilder.loadTexts:alT1E1StatsBPVs.setStatus(_A)
_AlT1E1StatsESs_Type=Counter32
_AlT1E1StatsESs_Object=MibTableColumn
alT1E1StatsESs=_AlT1E1StatsESs_Object((1,3,6,1,4,1,3076,2,1,2,33,2,1,7),_AlT1E1StatsESs_Type())
alT1E1StatsESs.setMaxAccess(_C)
if mibBuilder.loadTexts:alT1E1StatsESs.setStatus(_A)
_AlT1E1StatsSESs_Type=Counter32
_AlT1E1StatsSESs_Object=MibTableColumn
alT1E1StatsSESs=_AlT1E1StatsSESs_Object((1,3,6,1,4,1,3076,2,1,2,33,2,1,8),_AlT1E1StatsSESs_Type())
alT1E1StatsSESs.setMaxAccess(_C)
if mibBuilder.loadTexts:alT1E1StatsSESs.setStatus(_A)
_AlT1E1StatsBESs_Type=Counter32
_AlT1E1StatsBESs_Object=MibTableColumn
alT1E1StatsBESs=_AlT1E1StatsBESs_Object((1,3,6,1,4,1,3076,2,1,2,33,2,1,9),_AlT1E1StatsBESs_Type())
alT1E1StatsBESs.setMaxAccess(_C)
if mibBuilder.loadTexts:alT1E1StatsBESs.setStatus(_A)
_AlT1E1StatsSEFSs_Type=Counter32
_AlT1E1StatsSEFSs_Object=MibTableColumn
alT1E1StatsSEFSs=_AlT1E1StatsSEFSs_Object((1,3,6,1,4,1,3076,2,1,2,33,2,1,10),_AlT1E1StatsSEFSs_Type())
alT1E1StatsSEFSs.setMaxAccess(_C)
if mibBuilder.loadTexts:alT1E1StatsSEFSs.setStatus(_A)
_AlT1E1StatsUASs_Type=Counter32
_AlT1E1StatsUASs_Object=MibTableColumn
alT1E1StatsUASs=_AlT1E1StatsUASs_Object((1,3,6,1,4,1,3076,2,1,2,33,2,1,11),_AlT1E1StatsUASs_Type())
alT1E1StatsUASs.setMaxAccess(_C)
if mibBuilder.loadTexts:alT1E1StatsUASs.setStatus(_A)
_AlT1E1StatsLCVs_Type=Counter32
_AlT1E1StatsLCVs_Object=MibTableColumn
alT1E1StatsLCVs=_AlT1E1StatsLCVs_Object((1,3,6,1,4,1,3076,2,1,2,33,2,1,12),_AlT1E1StatsLCVs_Type())
alT1E1StatsLCVs.setMaxAccess(_C)
if mibBuilder.loadTexts:alT1E1StatsLCVs.setStatus(_A)
_AlT1E1StatsCSSs_Type=Counter32
_AlT1E1StatsCSSs_Object=MibTableColumn
alT1E1StatsCSSs=_AlT1E1StatsCSSs_Object((1,3,6,1,4,1,3076,2,1,2,33,2,1,13),_AlT1E1StatsCSSs_Type())
alT1E1StatsCSSs.setMaxAccess(_C)
if mibBuilder.loadTexts:alT1E1StatsCSSs.setStatus(_A)
_AlT1E1StatsDMs_Type=Counter32
_AlT1E1StatsDMs_Object=MibTableColumn
alT1E1StatsDMs=_AlT1E1StatsDMs_Object((1,3,6,1,4,1,3076,2,1,2,33,2,1,14),_AlT1E1StatsDMs_Type())
alT1E1StatsDMs.setMaxAccess(_C)
if mibBuilder.loadTexts:alT1E1StatsDMs.setStatus(_A)
_AlT1E1StatsPCVs_Type=Counter32
_AlT1E1StatsPCVs_Object=MibTableColumn
alT1E1StatsPCVs=_AlT1E1StatsPCVs_Object((1,3,6,1,4,1,3076,2,1,2,33,2,1,15),_AlT1E1StatsPCVs_Type())
alT1E1StatsPCVs.setMaxAccess(_C)
if mibBuilder.loadTexts:alT1E1StatsPCVs.setStatus(_A)
_AlT1E1StatsLESs_Type=Counter32
_AlT1E1StatsLESs_Object=MibTableColumn
alT1E1StatsLESs=_AlT1E1StatsLESs_Object((1,3,6,1,4,1,3076,2,1,2,33,2,1,16),_AlT1E1StatsLESs_Type())
alT1E1StatsLESs.setMaxAccess(_C)
if mibBuilder.loadTexts:alT1E1StatsLESs.setStatus(_A)
altigaT1E1StatsGroup=ObjectGroup((1,3,6,1,4,1,3076,2,1,1,1,33,2))
altigaT1E1StatsGroup.setObjects(*((_B,_G),(_B,_D),(_B,_E),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:altigaT1E1StatsGroup.setStatus(_A)
altigaT1E1StatsMibCompliance=ModuleCompliance((1,3,6,1,4,1,3076,1,1,38,2,1,1,1))
altigaT1E1StatsMibCompliance.setObjects((_B,_U))
if mibBuilder.loadTexts:altigaT1E1StatsMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'altigaT1E1StatsMibModule':altigaT1E1StatsMibModule,'altigaT1E1StatsMibConformance':altigaT1E1StatsMibConformance,'altigaT1E1StatsMibCompliances':altigaT1E1StatsMibCompliances,'altigaT1E1StatsMibCompliance':altigaT1E1StatsMibCompliance,_U:altigaT1E1StatsGroup,'alStatsT1E1Global':alStatsT1E1Global,'alT1E1StatsTable':alT1E1StatsTable,'alT1E1StatsEntry':alT1E1StatsEntry,_G:alT1E1StatsRowStatus,_D:alT1E1StatsSlot,_E:alT1E1StatsConn,_H:alT1E1StatsLineStatus,_I:alT1E1StatsElapsedSecs,_J:alT1E1StatsBPVs,_K:alT1E1StatsESs,_L:alT1E1StatsSESs,_M:alT1E1StatsBESs,_N:alT1E1StatsSEFSs,_O:alT1E1StatsUASs,_P:alT1E1StatsLCVs,_Q:alT1E1StatsCSSs,_R:alT1E1StatsDMs,_S:alT1E1StatsPCVs,_T:alT1E1StatsLESs})