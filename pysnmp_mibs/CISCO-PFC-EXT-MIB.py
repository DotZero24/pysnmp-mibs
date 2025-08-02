_c='ciscoPfcExtIfPriorityWaitGroup'
_b='deprecated'
_a='cpfcIfPriorityWaitTx'
_Z='cpfcIfPriorityWaitRx'
_Y='cpfcWatchdogIfQueueTotalDropInPkts'
_X='cpfcWatchdogIfQueueDropInPkts'
_W='cpfcWatchdogIfQueueDropPkts'
_V='cpfcWatchdogIfQueueTotalDropPkts'
_U='cpfcWatchdogIfQueueRestores'
_T='cpfcWatchdogIfQueueShutdowns'
_S='cpfcWatchdogIfQueueState'
_R='cpfcIfPriorityIndications'
_Q='cpfcIfPriorityRequests'
_P='cpfcIfIndications'
_O='cpfcIfRequests'
_N='micro-seconds'
_M='cpfcIfPriorityWaitCoS'
_L='cpfcWatchdogIfQueueNumber'
_K='cpfcIfPriorityValue'
_J='ciscoPfcExtWatchdogIfQueueGroup'
_I='not-accessible'
_H='ciscoPfcExtIfPriorityGroup'
_G='ciscoPfcExtIfGroup'
_F='Integer32'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='CISCO-PFC-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
QosQueueNumber,=mibBuilder.importSymbols('CISCO-QOS-TC-MIB','QosQueueNumber')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
Unsigned64,=mibBuilder.importSymbols('CISCO-TC','Unsigned64')
CounterBasedGauge64,=mibBuilder.importSymbols('HCNUM-TC','CounterBasedGauge64')
ifIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoPfcExtMIB=ModuleIdentity((1,3,6,1,4,1,9,9,813))
if mibBuilder.loadTexts:ciscoPfcExtMIB.setRevisions(('2017-05-26 00:00','2016-11-30 00:00','2016-04-28 00:00','2013-09-26 00:00'))
_CiscoPfcExtMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoPfcExtMIBNotifs=_CiscoPfcExtMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,813,0))
_CiscoPfcExtMIBObjects_ObjectIdentity=ObjectIdentity
ciscoPfcExtMIBObjects=_CiscoPfcExtMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,813,1))
_CpfcIfTable_Object=MibTable
cpfcIfTable=_CpfcIfTable_Object((1,3,6,1,4,1,9,9,813,1,1))
if mibBuilder.loadTexts:cpfcIfTable.setStatus(_A)
_CpfcIfEntry_Object=MibTableRow
cpfcIfEntry=_CpfcIfEntry_Object((1,3,6,1,4,1,9,9,813,1,1,1))
cpfcIfEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cpfcIfEntry.setStatus(_A)
_CpfcIfRequests_Type=Counter64
_CpfcIfRequests_Object=MibTableColumn
cpfcIfRequests=_CpfcIfRequests_Object((1,3,6,1,4,1,9,9,813,1,1,1,1),_CpfcIfRequests_Type())
cpfcIfRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:cpfcIfRequests.setStatus(_A)
_CpfcIfIndications_Type=Counter64
_CpfcIfIndications_Object=MibTableColumn
cpfcIfIndications=_CpfcIfIndications_Object((1,3,6,1,4,1,9,9,813,1,1,1,2),_CpfcIfIndications_Type())
cpfcIfIndications.setMaxAccess(_C)
if mibBuilder.loadTexts:cpfcIfIndications.setStatus(_A)
_CpfcIfPriorityTable_Object=MibTable
cpfcIfPriorityTable=_CpfcIfPriorityTable_Object((1,3,6,1,4,1,9,9,813,1,2))
if mibBuilder.loadTexts:cpfcIfPriorityTable.setStatus(_A)
_CpfcIfPriorityEntry_Object=MibTableRow
cpfcIfPriorityEntry=_CpfcIfPriorityEntry_Object((1,3,6,1,4,1,9,9,813,1,2,1))
cpfcIfPriorityEntry.setIndexNames((0,_D,_E),(0,_B,_K))
if mibBuilder.loadTexts:cpfcIfPriorityEntry.setStatus(_A)
class _CpfcIfPriorityValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_CpfcIfPriorityValue_Type.__name__=_F
_CpfcIfPriorityValue_Object=MibTableColumn
cpfcIfPriorityValue=_CpfcIfPriorityValue_Object((1,3,6,1,4,1,9,9,813,1,2,1,1),_CpfcIfPriorityValue_Type())
cpfcIfPriorityValue.setMaxAccess(_I)
if mibBuilder.loadTexts:cpfcIfPriorityValue.setStatus(_A)
_CpfcIfPriorityRequests_Type=Counter64
_CpfcIfPriorityRequests_Object=MibTableColumn
cpfcIfPriorityRequests=_CpfcIfPriorityRequests_Object((1,3,6,1,4,1,9,9,813,1,2,1,2),_CpfcIfPriorityRequests_Type())
cpfcIfPriorityRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:cpfcIfPriorityRequests.setStatus(_A)
_CpfcIfPriorityIndications_Type=Counter64
_CpfcIfPriorityIndications_Object=MibTableColumn
cpfcIfPriorityIndications=_CpfcIfPriorityIndications_Object((1,3,6,1,4,1,9,9,813,1,2,1,3),_CpfcIfPriorityIndications_Type())
cpfcIfPriorityIndications.setMaxAccess(_C)
if mibBuilder.loadTexts:cpfcIfPriorityIndications.setStatus(_A)
_CpfcWatchdogIfQueueInfoTable_Object=MibTable
cpfcWatchdogIfQueueInfoTable=_CpfcWatchdogIfQueueInfoTable_Object((1,3,6,1,4,1,9,9,813,1,3))
if mibBuilder.loadTexts:cpfcWatchdogIfQueueInfoTable.setStatus(_A)
_CpfcWatchdogIfQueueInfoEntry_Object=MibTableRow
cpfcWatchdogIfQueueInfoEntry=_CpfcWatchdogIfQueueInfoEntry_Object((1,3,6,1,4,1,9,9,813,1,3,1))
cpfcWatchdogIfQueueInfoEntry.setIndexNames((0,_D,_E),(0,_B,_L))
if mibBuilder.loadTexts:cpfcWatchdogIfQueueInfoEntry.setStatus(_A)
_CpfcWatchdogIfQueueNumber_Type=QosQueueNumber
_CpfcWatchdogIfQueueNumber_Object=MibTableColumn
cpfcWatchdogIfQueueNumber=_CpfcWatchdogIfQueueNumber_Object((1,3,6,1,4,1,9,9,813,1,3,1,1),_CpfcWatchdogIfQueueNumber_Type())
cpfcWatchdogIfQueueNumber.setMaxAccess(_I)
if mibBuilder.loadTexts:cpfcWatchdogIfQueueNumber.setStatus(_A)
class _CpfcWatchdogIfQueueState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('active',1),('shutdown',2),('notApplicable',3)))
_CpfcWatchdogIfQueueState_Type.__name__=_F
_CpfcWatchdogIfQueueState_Object=MibTableColumn
cpfcWatchdogIfQueueState=_CpfcWatchdogIfQueueState_Object((1,3,6,1,4,1,9,9,813,1,3,1,2),_CpfcWatchdogIfQueueState_Type())
cpfcWatchdogIfQueueState.setMaxAccess(_C)
if mibBuilder.loadTexts:cpfcWatchdogIfQueueState.setStatus(_A)
_CpfcWatchdogIfQueueShutdowns_Type=Counter64
_CpfcWatchdogIfQueueShutdowns_Object=MibTableColumn
cpfcWatchdogIfQueueShutdowns=_CpfcWatchdogIfQueueShutdowns_Object((1,3,6,1,4,1,9,9,813,1,3,1,3),_CpfcWatchdogIfQueueShutdowns_Type())
cpfcWatchdogIfQueueShutdowns.setMaxAccess(_C)
if mibBuilder.loadTexts:cpfcWatchdogIfQueueShutdowns.setStatus(_A)
_CpfcWatchdogIfQueueRestores_Type=Counter64
_CpfcWatchdogIfQueueRestores_Object=MibTableColumn
cpfcWatchdogIfQueueRestores=_CpfcWatchdogIfQueueRestores_Object((1,3,6,1,4,1,9,9,813,1,3,1,4),_CpfcWatchdogIfQueueRestores_Type())
cpfcWatchdogIfQueueRestores.setMaxAccess(_C)
if mibBuilder.loadTexts:cpfcWatchdogIfQueueRestores.setStatus(_A)
_CpfcWatchdogIfQueueTotalDropPkts_Type=Counter64
_CpfcWatchdogIfQueueTotalDropPkts_Object=MibTableColumn
cpfcWatchdogIfQueueTotalDropPkts=_CpfcWatchdogIfQueueTotalDropPkts_Object((1,3,6,1,4,1,9,9,813,1,3,1,5),_CpfcWatchdogIfQueueTotalDropPkts_Type())
cpfcWatchdogIfQueueTotalDropPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cpfcWatchdogIfQueueTotalDropPkts.setStatus(_A)
_CpfcWatchdogIfQueueDropPkts_Type=CounterBasedGauge64
_CpfcWatchdogIfQueueDropPkts_Object=MibTableColumn
cpfcWatchdogIfQueueDropPkts=_CpfcWatchdogIfQueueDropPkts_Object((1,3,6,1,4,1,9,9,813,1,3,1,6),_CpfcWatchdogIfQueueDropPkts_Type())
cpfcWatchdogIfQueueDropPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cpfcWatchdogIfQueueDropPkts.setStatus(_A)
_CpfcWatchdogIfQueueDropInPkts_Type=CounterBasedGauge64
_CpfcWatchdogIfQueueDropInPkts_Object=MibTableColumn
cpfcWatchdogIfQueueDropInPkts=_CpfcWatchdogIfQueueDropInPkts_Object((1,3,6,1,4,1,9,9,813,1,3,1,7),_CpfcWatchdogIfQueueDropInPkts_Type())
cpfcWatchdogIfQueueDropInPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cpfcWatchdogIfQueueDropInPkts.setStatus(_A)
_CpfcWatchdogIfQueueTotalDropInPkts_Type=CounterBasedGauge64
_CpfcWatchdogIfQueueTotalDropInPkts_Object=MibTableColumn
cpfcWatchdogIfQueueTotalDropInPkts=_CpfcWatchdogIfQueueTotalDropInPkts_Object((1,3,6,1,4,1,9,9,813,1,3,1,8),_CpfcWatchdogIfQueueTotalDropInPkts_Type())
cpfcWatchdogIfQueueTotalDropInPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cpfcWatchdogIfQueueTotalDropInPkts.setStatus(_A)
_CpfcIfPriorityWaitTable_Object=MibTable
cpfcIfPriorityWaitTable=_CpfcIfPriorityWaitTable_Object((1,3,6,1,4,1,9,9,813,1,4))
if mibBuilder.loadTexts:cpfcIfPriorityWaitTable.setStatus(_A)
_CpfcIfPriorityWaitEntry_Object=MibTableRow
cpfcIfPriorityWaitEntry=_CpfcIfPriorityWaitEntry_Object((1,3,6,1,4,1,9,9,813,1,4,1))
cpfcIfPriorityWaitEntry.setIndexNames((0,_D,_E),(0,_B,_M))
if mibBuilder.loadTexts:cpfcIfPriorityWaitEntry.setStatus(_A)
class _CpfcIfPriorityWaitCoS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_CpfcIfPriorityWaitCoS_Type.__name__=_F
_CpfcIfPriorityWaitCoS_Object=MibTableColumn
cpfcIfPriorityWaitCoS=_CpfcIfPriorityWaitCoS_Object((1,3,6,1,4,1,9,9,813,1,4,1,1),_CpfcIfPriorityWaitCoS_Type())
cpfcIfPriorityWaitCoS.setMaxAccess(_I)
if mibBuilder.loadTexts:cpfcIfPriorityWaitCoS.setStatus(_A)
_CpfcIfPriorityWaitRx_Type=Unsigned64
_CpfcIfPriorityWaitRx_Object=MibTableColumn
cpfcIfPriorityWaitRx=_CpfcIfPriorityWaitRx_Object((1,3,6,1,4,1,9,9,813,1,4,1,2),_CpfcIfPriorityWaitRx_Type())
cpfcIfPriorityWaitRx.setMaxAccess(_C)
if mibBuilder.loadTexts:cpfcIfPriorityWaitRx.setStatus(_A)
if mibBuilder.loadTexts:cpfcIfPriorityWaitRx.setUnits(_N)
_CpfcIfPriorityWaitTx_Type=Unsigned64
_CpfcIfPriorityWaitTx_Object=MibTableColumn
cpfcIfPriorityWaitTx=_CpfcIfPriorityWaitTx_Object((1,3,6,1,4,1,9,9,813,1,4,1,3),_CpfcIfPriorityWaitTx_Type())
cpfcIfPriorityWaitTx.setMaxAccess(_C)
if mibBuilder.loadTexts:cpfcIfPriorityWaitTx.setStatus(_A)
if mibBuilder.loadTexts:cpfcIfPriorityWaitTx.setUnits(_N)
_CiscoPfcExtMIBConform_ObjectIdentity=ObjectIdentity
ciscoPfcExtMIBConform=_CiscoPfcExtMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,813,2))
_CiscoPfcExtMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoPfcExtMIBCompliances=_CiscoPfcExtMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,813,2,1))
_CiscoPfcExtMIBGroups_ObjectIdentity=ObjectIdentity
ciscoPfcExtMIBGroups=_CiscoPfcExtMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,813,2,2))
ciscoPfcExtIfGroup=ObjectGroup((1,3,6,1,4,1,9,9,813,2,2,1))
ciscoPfcExtIfGroup.setObjects(*((_B,_O),(_B,_P)))
if mibBuilder.loadTexts:ciscoPfcExtIfGroup.setStatus(_A)
ciscoPfcExtIfPriorityGroup=ObjectGroup((1,3,6,1,4,1,9,9,813,2,2,2))
ciscoPfcExtIfPriorityGroup.setObjects(*((_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:ciscoPfcExtIfPriorityGroup.setStatus(_A)
ciscoPfcExtWatchdogIfQueueGroup=ObjectGroup((1,3,6,1,4,1,9,9,813,2,2,3))
ciscoPfcExtWatchdogIfQueueGroup.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:ciscoPfcExtWatchdogIfQueueGroup.setStatus(_A)
ciscoPfcExtWatchdogIfQueueDropInPktGroup=ObjectGroup((1,3,6,1,4,1,9,9,813,2,2,4))
ciscoPfcExtWatchdogIfQueueDropInPktGroup.setObjects(*((_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:ciscoPfcExtWatchdogIfQueueDropInPktGroup.setStatus(_A)
ciscoPfcExtIfPriorityWaitGroup=ObjectGroup((1,3,6,1,4,1,9,9,813,2,2,5))
ciscoPfcExtIfPriorityWaitGroup.setObjects(*((_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:ciscoPfcExtIfPriorityWaitGroup.setStatus(_A)
ciscoPfcExtMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,813,2,1,1))
ciscoPfcExtMIBCompliance.setObjects(*((_B,_G),(_B,_H)))
if mibBuilder.loadTexts:ciscoPfcExtMIBCompliance.setStatus(_b)
ciscoPfcExtMIBCompliance2=ModuleCompliance((1,3,6,1,4,1,9,9,813,2,1,2))
ciscoPfcExtMIBCompliance2.setObjects(*((_B,_G),(_B,_H),(_B,_J)))
if mibBuilder.loadTexts:ciscoPfcExtMIBCompliance2.setStatus(_b)
ciscoPfcExtMIBCompliance3=ModuleCompliance((1,3,6,1,4,1,9,9,813,2,1,3))
ciscoPfcExtMIBCompliance3.setObjects(*((_B,_G),(_B,_H),(_B,_J),(_B,_c)))
if mibBuilder.loadTexts:ciscoPfcExtMIBCompliance3.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoPfcExtMIB':ciscoPfcExtMIB,'ciscoPfcExtMIBNotifs':ciscoPfcExtMIBNotifs,'ciscoPfcExtMIBObjects':ciscoPfcExtMIBObjects,'cpfcIfTable':cpfcIfTable,'cpfcIfEntry':cpfcIfEntry,_O:cpfcIfRequests,_P:cpfcIfIndications,'cpfcIfPriorityTable':cpfcIfPriorityTable,'cpfcIfPriorityEntry':cpfcIfPriorityEntry,_K:cpfcIfPriorityValue,_Q:cpfcIfPriorityRequests,_R:cpfcIfPriorityIndications,'cpfcWatchdogIfQueueInfoTable':cpfcWatchdogIfQueueInfoTable,'cpfcWatchdogIfQueueInfoEntry':cpfcWatchdogIfQueueInfoEntry,_L:cpfcWatchdogIfQueueNumber,_S:cpfcWatchdogIfQueueState,_T:cpfcWatchdogIfQueueShutdowns,_U:cpfcWatchdogIfQueueRestores,_V:cpfcWatchdogIfQueueTotalDropPkts,_W:cpfcWatchdogIfQueueDropPkts,_X:cpfcWatchdogIfQueueDropInPkts,_Y:cpfcWatchdogIfQueueTotalDropInPkts,'cpfcIfPriorityWaitTable':cpfcIfPriorityWaitTable,'cpfcIfPriorityWaitEntry':cpfcIfPriorityWaitEntry,_M:cpfcIfPriorityWaitCoS,_Z:cpfcIfPriorityWaitRx,_a:cpfcIfPriorityWaitTx,'ciscoPfcExtMIBConform':ciscoPfcExtMIBConform,'ciscoPfcExtMIBCompliances':ciscoPfcExtMIBCompliances,'ciscoPfcExtMIBCompliance':ciscoPfcExtMIBCompliance,'ciscoPfcExtMIBCompliance2':ciscoPfcExtMIBCompliance2,'ciscoPfcExtMIBCompliance3':ciscoPfcExtMIBCompliance3,'ciscoPfcExtMIBGroups':ciscoPfcExtMIBGroups,_G:ciscoPfcExtIfGroup,_H:ciscoPfcExtIfPriorityGroup,_J:ciscoPfcExtWatchdogIfQueueGroup,'ciscoPfcExtWatchdogIfQueueDropInPktGroup':ciscoPfcExtWatchdogIfQueueDropInPktGroup,_c:ciscoPfcExtIfPriorityWaitGroup})