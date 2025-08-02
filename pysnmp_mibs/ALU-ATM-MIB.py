_S='aluExtAtmVclVplOamStatsGroup'
_R='aluExtAtmIntfOamStatsGroup'
_Q='aeAal5VccStatsPPPoERelayErrors'
_P='aeAal5VccStatsPPPoERelayOverflow'
_O='aeAal5VccStatsPPPoERelayMalformed'
_N='aeAal5VccStatsPPPoERelayRxd'
_M='aeAtmVplStatsOamCellsGeneratedTxd'
_L='aeAtmVclStatsOamCellsGeneratedTxd'
_K='aeAtmIntfStatsTotalOamCellsTxd'
_J='aeAtmIntfStatsTotalOamCellsRxd'
_I='aeAal5VccPppoERelayStatsEntry'
_H='aeTAtmOamVplStatisticsEntry'
_G='aeTAtmOamVclStatisticsEntry'
_F='aeTAtmIntfStatsEntry'
_E='aeAtmVplStatsOamCellsGenerated'
_D='aeAtmVclStatsOamCellsGenerated'
_C='read-only'
_B='ALU-ATM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
aluSARConfs,aluSARMIBModules,aluSARNotifyPrefix,aluSARObjs=mibBuilder.importSymbols('ALU-SAR-GLOBAL-MIB','aluSARConfs','aluSARMIBModules','aluSARNotifyPrefix','aluSARObjs')
aal5VccEntry,atmVclEntry,atmVplEntry=mibBuilder.importSymbols('ATM-MIB','aal5VccEntry','atmVclEntry','atmVplEntry')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp')
tAtmIntfStatsEntry,=mibBuilder.importSymbols('TIMETRA-ATM-MIB','tAtmIntfStatsEntry')
aluATMMIBModule=ModuleIdentity((1,3,6,1,4,1,6527,6,1,1,1,3,4))
if mibBuilder.loadTexts:aluATMMIBModule.setRevisions(('1908-01-18 00:00',))
_AluAtmMIBConformance_ObjectIdentity=ObjectIdentity
aluAtmMIBConformance=_AluAtmMIBConformance_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,1,3))
_AluAtmMIBCompliances_ObjectIdentity=ObjectIdentity
aluAtmMIBCompliances=_AluAtmMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,1,3,1))
_AluAtmMIBGroups_ObjectIdentity=ObjectIdentity
aluAtmMIBGroups=_AluAtmMIBGroups_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,1,3,2))
_AluAtmObjs_ObjectIdentity=ObjectIdentity
aluAtmObjs=_AluAtmObjs_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,2,3))
_AluAtmExtensionObjs_ObjectIdentity=ObjectIdentity
aluAtmExtensionObjs=_AluAtmExtensionObjs_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,2,3,1))
_AeTAtmIntfStatsTable_Object=MibTable
aeTAtmIntfStatsTable=_AeTAtmIntfStatsTable_Object((1,3,6,1,4,1,6527,6,1,2,2,3,1,1))
if mibBuilder.loadTexts:aeTAtmIntfStatsTable.setStatus(_A)
_AeTAtmIntfStatsEntry_Object=MibTableRow
aeTAtmIntfStatsEntry=_AeTAtmIntfStatsEntry_Object((1,3,6,1,4,1,6527,6,1,2,2,3,1,1,1))
if mibBuilder.loadTexts:aeTAtmIntfStatsEntry.setStatus(_A)
_AeAtmIntfStatsTotalOamCellsRxd_Type=Counter64
_AeAtmIntfStatsTotalOamCellsRxd_Object=MibTableColumn
aeAtmIntfStatsTotalOamCellsRxd=_AeAtmIntfStatsTotalOamCellsRxd_Object((1,3,6,1,4,1,6527,6,1,2,2,3,1,1,1,1),_AeAtmIntfStatsTotalOamCellsRxd_Type())
aeAtmIntfStatsTotalOamCellsRxd.setMaxAccess(_C)
if mibBuilder.loadTexts:aeAtmIntfStatsTotalOamCellsRxd.setStatus(_A)
_AeAtmIntfStatsTotalOamCellsTxd_Type=Counter64
_AeAtmIntfStatsTotalOamCellsTxd_Object=MibTableColumn
aeAtmIntfStatsTotalOamCellsTxd=_AeAtmIntfStatsTotalOamCellsTxd_Object((1,3,6,1,4,1,6527,6,1,2,2,3,1,1,1,2),_AeAtmIntfStatsTotalOamCellsTxd_Type())
aeAtmIntfStatsTotalOamCellsTxd.setMaxAccess(_C)
if mibBuilder.loadTexts:aeAtmIntfStatsTotalOamCellsTxd.setStatus(_A)
_AeTAtmOamVclStatisticsTable_Object=MibTable
aeTAtmOamVclStatisticsTable=_AeTAtmOamVclStatisticsTable_Object((1,3,6,1,4,1,6527,6,1,2,2,3,1,2))
if mibBuilder.loadTexts:aeTAtmOamVclStatisticsTable.setStatus(_A)
_AeTAtmOamVclStatisticsEntry_Object=MibTableRow
aeTAtmOamVclStatisticsEntry=_AeTAtmOamVclStatisticsEntry_Object((1,3,6,1,4,1,6527,6,1,2,2,3,1,2,1))
if mibBuilder.loadTexts:aeTAtmOamVclStatisticsEntry.setStatus(_A)
_AeAtmVclStatsOamCellsGenerated_Type=Counter32
_AeAtmVclStatsOamCellsGenerated_Object=MibTableColumn
aeAtmVclStatsOamCellsGenerated=_AeAtmVclStatsOamCellsGenerated_Object((1,3,6,1,4,1,6527,6,1,2,2,3,1,2,1,1),_AeAtmVclStatsOamCellsGenerated_Type())
aeAtmVclStatsOamCellsGenerated.setMaxAccess(_C)
if mibBuilder.loadTexts:aeAtmVclStatsOamCellsGenerated.setStatus(_A)
_AeAtmVclStatsOamCellsGeneratedTxd_Type=Counter32
_AeAtmVclStatsOamCellsGeneratedTxd_Object=MibTableColumn
aeAtmVclStatsOamCellsGeneratedTxd=_AeAtmVclStatsOamCellsGeneratedTxd_Object((1,3,6,1,4,1,6527,6,1,2,2,3,1,2,1,2),_AeAtmVclStatsOamCellsGeneratedTxd_Type())
aeAtmVclStatsOamCellsGeneratedTxd.setMaxAccess(_C)
if mibBuilder.loadTexts:aeAtmVclStatsOamCellsGeneratedTxd.setStatus(_A)
_AeTAtmOamVplStatisticsTable_Object=MibTable
aeTAtmOamVplStatisticsTable=_AeTAtmOamVplStatisticsTable_Object((1,3,6,1,4,1,6527,6,1,2,2,3,1,3))
if mibBuilder.loadTexts:aeTAtmOamVplStatisticsTable.setStatus(_A)
_AeTAtmOamVplStatisticsEntry_Object=MibTableRow
aeTAtmOamVplStatisticsEntry=_AeTAtmOamVplStatisticsEntry_Object((1,3,6,1,4,1,6527,6,1,2,2,3,1,3,1))
if mibBuilder.loadTexts:aeTAtmOamVplStatisticsEntry.setStatus(_A)
_AeAtmVplStatsOamCellsGenerated_Type=Counter32
_AeAtmVplStatsOamCellsGenerated_Object=MibTableColumn
aeAtmVplStatsOamCellsGenerated=_AeAtmVplStatsOamCellsGenerated_Object((1,3,6,1,4,1,6527,6,1,2,2,3,1,3,1,1),_AeAtmVplStatsOamCellsGenerated_Type())
aeAtmVplStatsOamCellsGenerated.setMaxAccess(_C)
if mibBuilder.loadTexts:aeAtmVplStatsOamCellsGenerated.setStatus(_A)
_AeAtmVplStatsOamCellsGeneratedTxd_Type=Counter32
_AeAtmVplStatsOamCellsGeneratedTxd_Object=MibTableColumn
aeAtmVplStatsOamCellsGeneratedTxd=_AeAtmVplStatsOamCellsGeneratedTxd_Object((1,3,6,1,4,1,6527,6,1,2,2,3,1,3,1,2),_AeAtmVplStatsOamCellsGeneratedTxd_Type())
aeAtmVplStatsOamCellsGeneratedTxd.setMaxAccess(_C)
if mibBuilder.loadTexts:aeAtmVplStatsOamCellsGeneratedTxd.setStatus(_A)
_AeAal5VccPppoERelayStatsTable_Object=MibTable
aeAal5VccPppoERelayStatsTable=_AeAal5VccPppoERelayStatsTable_Object((1,3,6,1,4,1,6527,6,1,2,2,3,1,4))
if mibBuilder.loadTexts:aeAal5VccPppoERelayStatsTable.setStatus(_A)
_AeAal5VccPppoERelayStatsEntry_Object=MibTableRow
aeAal5VccPppoERelayStatsEntry=_AeAal5VccPppoERelayStatsEntry_Object((1,3,6,1,4,1,6527,6,1,2,2,3,1,4,1))
if mibBuilder.loadTexts:aeAal5VccPppoERelayStatsEntry.setStatus(_A)
_AeAal5VccStatsPPPoERelayRxd_Type=Counter64
_AeAal5VccStatsPPPoERelayRxd_Object=MibTableColumn
aeAal5VccStatsPPPoERelayRxd=_AeAal5VccStatsPPPoERelayRxd_Object((1,3,6,1,4,1,6527,6,1,2,2,3,1,4,1,1),_AeAal5VccStatsPPPoERelayRxd_Type())
aeAal5VccStatsPPPoERelayRxd.setMaxAccess(_C)
if mibBuilder.loadTexts:aeAal5VccStatsPPPoERelayRxd.setStatus(_A)
_AeAal5VccStatsPPPoERelayMalformed_Type=Counter64
_AeAal5VccStatsPPPoERelayMalformed_Object=MibTableColumn
aeAal5VccStatsPPPoERelayMalformed=_AeAal5VccStatsPPPoERelayMalformed_Object((1,3,6,1,4,1,6527,6,1,2,2,3,1,4,1,2),_AeAal5VccStatsPPPoERelayMalformed_Type())
aeAal5VccStatsPPPoERelayMalformed.setMaxAccess(_C)
if mibBuilder.loadTexts:aeAal5VccStatsPPPoERelayMalformed.setStatus(_A)
_AeAal5VccStatsPPPoERelayOverflow_Type=Counter64
_AeAal5VccStatsPPPoERelayOverflow_Object=MibTableColumn
aeAal5VccStatsPPPoERelayOverflow=_AeAal5VccStatsPPPoERelayOverflow_Object((1,3,6,1,4,1,6527,6,1,2,2,3,1,4,1,3),_AeAal5VccStatsPPPoERelayOverflow_Type())
aeAal5VccStatsPPPoERelayOverflow.setMaxAccess(_C)
if mibBuilder.loadTexts:aeAal5VccStatsPPPoERelayOverflow.setStatus(_A)
_AeAal5VccStatsPPPoERelayErrors_Type=Counter64
_AeAal5VccStatsPPPoERelayErrors_Object=MibTableColumn
aeAal5VccStatsPPPoERelayErrors=_AeAal5VccStatsPPPoERelayErrors_Object((1,3,6,1,4,1,6527,6,1,2,2,3,1,4,1,4),_AeAal5VccStatsPPPoERelayErrors_Type())
aeAal5VccStatsPPPoERelayErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:aeAal5VccStatsPPPoERelayErrors.setStatus(_A)
_AluAtmNotifyPrefix_ObjectIdentity=ObjectIdentity
aluAtmNotifyPrefix=_AluAtmNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,3,3))
tAtmIntfStatsEntry.registerAugmentions((_B,_F))
aeTAtmIntfStatsEntry.setIndexNames(*tAtmIntfStatsEntry.getIndexNames())
atmVclEntry.registerAugmentions((_B,_G))
aeTAtmOamVclStatisticsEntry.setIndexNames(*atmVclEntry.getIndexNames())
atmVplEntry.registerAugmentions((_B,_H))
aeTAtmOamVplStatisticsEntry.setIndexNames(*atmVplEntry.getIndexNames())
aal5VccEntry.registerAugmentions((_B,_I))
aeAal5VccPppoERelayStatsEntry.setIndexNames(*aal5VccEntry.getIndexNames())
aluExtAtmIntfOamStatsGroup=ObjectGroup((1,3,6,1,4,1,6527,6,1,2,1,3,2,1))
aluExtAtmIntfOamStatsGroup.setObjects(*((_B,_J),(_B,_K)))
if mibBuilder.loadTexts:aluExtAtmIntfOamStatsGroup.setStatus(_A)
aluExtAtmVclVplOamStatsGroup=ObjectGroup((1,3,6,1,4,1,6527,6,1,2,1,3,2,2))
aluExtAtmVclVplOamStatsGroup.setObjects(*((_B,_D),(_B,_E)))
if mibBuilder.loadTexts:aluExtAtmVclVplOamStatsGroup.setStatus('obsolete')
aluExtAtmVclVplOamStatsGroupV3v0=ObjectGroup((1,3,6,1,4,1,6527,6,1,2,1,3,2,3))
aluExtAtmVclVplOamStatsGroupV3v0.setObjects(*((_B,_D),(_B,_L),(_B,_E),(_B,_M)))
if mibBuilder.loadTexts:aluExtAtmVclVplOamStatsGroupV3v0.setStatus(_A)
aeAal5VccPppoERelayStatsGroup=ObjectGroup((1,3,6,1,4,1,6527,6,1,2,1,3,2,4))
aeAal5VccPppoERelayStatsGroup.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:aeAal5VccPppoERelayStatsGroup.setStatus(_A)
aluAtmMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6527,6,1,2,1,3,1,1))
aluAtmMIBCompliance.setObjects(*((_B,_R),(_B,_S)))
if mibBuilder.loadTexts:aluAtmMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'aluATMMIBModule':aluATMMIBModule,'aluAtmMIBConformance':aluAtmMIBConformance,'aluAtmMIBCompliances':aluAtmMIBCompliances,'aluAtmMIBCompliance':aluAtmMIBCompliance,'aluAtmMIBGroups':aluAtmMIBGroups,_R:aluExtAtmIntfOamStatsGroup,_S:aluExtAtmVclVplOamStatsGroup,'aluExtAtmVclVplOamStatsGroupV3v0':aluExtAtmVclVplOamStatsGroupV3v0,'aeAal5VccPppoERelayStatsGroup':aeAal5VccPppoERelayStatsGroup,'aluAtmObjs':aluAtmObjs,'aluAtmExtensionObjs':aluAtmExtensionObjs,'aeTAtmIntfStatsTable':aeTAtmIntfStatsTable,_F:aeTAtmIntfStatsEntry,_J:aeAtmIntfStatsTotalOamCellsRxd,_K:aeAtmIntfStatsTotalOamCellsTxd,'aeTAtmOamVclStatisticsTable':aeTAtmOamVclStatisticsTable,_G:aeTAtmOamVclStatisticsEntry,_D:aeAtmVclStatsOamCellsGenerated,_L:aeAtmVclStatsOamCellsGeneratedTxd,'aeTAtmOamVplStatisticsTable':aeTAtmOamVplStatisticsTable,_H:aeTAtmOamVplStatisticsEntry,_E:aeAtmVplStatsOamCellsGenerated,_M:aeAtmVplStatsOamCellsGeneratedTxd,'aeAal5VccPppoERelayStatsTable':aeAal5VccPppoERelayStatsTable,_I:aeAal5VccPppoERelayStatsEntry,_N:aeAal5VccStatsPPPoERelayRxd,_O:aeAal5VccStatsPPPoERelayMalformed,_P:aeAal5VccStatsPPPoERelayOverflow,_Q:aeAal5VccStatsPPPoERelayErrors,'aluAtmNotifyPrefix':aluAtmNotifyPrefix})