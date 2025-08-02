_Q='useGreater'
_P='wwpQosQueueId'
_O='wwpQosQPortId'
_N='wwpQosConfQueueId'
_M='wwpQosConfPortId'
_L='wwpQosPortIndex'
_K='wwpQosRxPriority'
_J='wwpQosStatsPortId'
_I='wwpQosStatsVlanId'
_H='read-create'
_G='wwpQosPortId'
_F='wwpQosVlanId'
_E='read-write'
_D='WWP-QOS-MIB'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
wwpModules,=mibBuilder.importSymbols('WWP-SMI','wwpModules')
wwpQosMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,12))
if mibBuilder.loadTexts:wwpQosMIB.setRevisions(('2001-04-03 17:00',))
class VlanId(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_WwpQosMIBObjects_ObjectIdentity=ObjectIdentity
wwpQosMIBObjects=_WwpQosMIBObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,12,1))
_WwpQos_ObjectIdentity=ObjectIdentity
wwpQos=_WwpQos_ObjectIdentity((1,3,6,1,4,1,6141,2,12,1,1))
_WwpQosTable_Object=MibTable
wwpQosTable=_WwpQosTable_Object((1,3,6,1,4,1,6141,2,12,1,1,1))
if mibBuilder.loadTexts:wwpQosTable.setStatus(_A)
_WwpQosEntry_Object=MibTableRow
wwpQosEntry=_WwpQosEntry_Object((1,3,6,1,4,1,6141,2,12,1,1,1,1))
wwpQosEntry.setIndexNames((0,_D,_F),(0,_D,_G))
if mibBuilder.loadTexts:wwpQosEntry.setStatus(_A)
_WwpQosVlanId_Type=VlanId
_WwpQosVlanId_Object=MibTableColumn
wwpQosVlanId=_WwpQosVlanId_Object((1,3,6,1,4,1,6141,2,12,1,1,1,1,1),_WwpQosVlanId_Type())
wwpQosVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpQosVlanId.setStatus(_A)
class _WwpQosPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpQosPortId_Type.__name__=_B
_WwpQosPortId_Object=MibTableColumn
wwpQosPortId=_WwpQosPortId_Object((1,3,6,1,4,1,6141,2,12,1,1,1,1,2),_WwpQosPortId_Type())
wwpQosPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpQosPortId.setStatus(_A)
class _WwpQosRateLimit_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
_WwpQosRateLimit_Type.__name__=_B
_WwpQosRateLimit_Object=MibTableColumn
wwpQosRateLimit=_WwpQosRateLimit_Object((1,3,6,1,4,1,6141,2,12,1,1,1,1,3),_WwpQosRateLimit_Type())
wwpQosRateLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpQosRateLimit.setStatus(_A)
if mibBuilder.loadTexts:wwpQosRateLimit.setUnits('kbps')
class _WwpQosPriQueue_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_WwpQosPriQueue_Type.__name__=_B
_WwpQosPriQueue_Object=MibTableColumn
wwpQosPriQueue=_WwpQosPriQueue_Object((1,3,6,1,4,1,6141,2,12,1,1,1,1,4),_WwpQosPriQueue_Type())
wwpQosPriQueue.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpQosPriQueue.setStatus(_A)
_WwpQosRowStatus_Type=RowStatus
_WwpQosRowStatus_Object=MibTableColumn
wwpQosRowStatus=_WwpQosRowStatus_Object((1,3,6,1,4,1,6141,2,12,1,1,1,1,5),_WwpQosRowStatus_Type())
wwpQosRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:wwpQosRowStatus.setStatus(_A)
_WwpQosStatsTable_Object=MibTable
wwpQosStatsTable=_WwpQosStatsTable_Object((1,3,6,1,4,1,6141,2,12,1,1,2))
if mibBuilder.loadTexts:wwpQosStatsTable.setStatus(_A)
_WwpQosStatsEntry_Object=MibTableRow
wwpQosStatsEntry=_WwpQosStatsEntry_Object((1,3,6,1,4,1,6141,2,12,1,1,2,1))
wwpQosStatsEntry.setIndexNames((0,_D,_I),(0,_D,_J))
if mibBuilder.loadTexts:wwpQosStatsEntry.setStatus(_A)
_WwpQosStatsVlanId_Type=VlanId
_WwpQosStatsVlanId_Object=MibTableColumn
wwpQosStatsVlanId=_WwpQosStatsVlanId_Object((1,3,6,1,4,1,6141,2,12,1,1,2,1,1),_WwpQosStatsVlanId_Type())
wwpQosStatsVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpQosStatsVlanId.setStatus(_A)
class _WwpQosStatsPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpQosStatsPortId_Type.__name__=_B
_WwpQosStatsPortId_Object=MibTableColumn
wwpQosStatsPortId=_WwpQosStatsPortId_Object((1,3,6,1,4,1,6141,2,12,1,1,2,1,2),_WwpQosStatsPortId_Type())
wwpQosStatsPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpQosStatsPortId.setStatus(_A)
_WwpQosRxBytes_Type=Counter64
_WwpQosRxBytes_Object=MibTableColumn
wwpQosRxBytes=_WwpQosRxBytes_Object((1,3,6,1,4,1,6141,2,12,1,1,2,1,3),_WwpQosRxBytes_Type())
wwpQosRxBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpQosRxBytes.setStatus(_A)
_WwpQosRxPkts_Type=Counter64
_WwpQosRxPkts_Object=MibTableColumn
wwpQosRxPkts=_WwpQosRxPkts_Object((1,3,6,1,4,1,6141,2,12,1,1,2,1,4),_WwpQosRxPkts_Type())
wwpQosRxPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpQosRxPkts.setStatus(_A)
class _WwpQosResetCounters_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('none',0),('reset',1)))
_WwpQosResetCounters_Type.__name__=_B
_WwpQosResetCounters_Object=MibTableColumn
wwpQosResetCounters=_WwpQosResetCounters_Object((1,3,6,1,4,1,6141,2,12,1,1,2,1,5),_WwpQosResetCounters_Type())
wwpQosResetCounters.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpQosResetCounters.setStatus('deprecated')
_WwpQosPriToQMapTable_Object=MibTable
wwpQosPriToQMapTable=_WwpQosPriToQMapTable_Object((1,3,6,1,4,1,6141,2,12,1,1,3))
if mibBuilder.loadTexts:wwpQosPriToQMapTable.setStatus(_A)
_WwpQosPriToQMapEntry_Object=MibTableRow
wwpQosPriToQMapEntry=_WwpQosPriToQMapEntry_Object((1,3,6,1,4,1,6141,2,12,1,1,3,1))
wwpQosPriToQMapEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:wwpQosPriToQMapEntry.setStatus(_A)
class _WwpQosRxPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpQosRxPriority_Type.__name__=_B
_WwpQosRxPriority_Object=MibTableColumn
wwpQosRxPriority=_WwpQosRxPriority_Object((1,3,6,1,4,1,6141,2,12,1,1,3,1,1),_WwpQosRxPriority_Type())
wwpQosRxPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpQosRxPriority.setStatus(_A)
class _WwpQosTxPriQueue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_WwpQosTxPriQueue_Type.__name__=_B
_WwpQosTxPriQueue_Object=MibTableColumn
wwpQosTxPriQueue=_WwpQosTxPriQueue_Object((1,3,6,1,4,1,6141,2,12,1,1,3,1,2),_WwpQosTxPriQueue_Type())
wwpQosTxPriQueue.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpQosTxPriQueue.setStatus(_A)
_WwpQosPortTable_Object=MibTable
wwpQosPortTable=_WwpQosPortTable_Object((1,3,6,1,4,1,6141,2,12,1,1,4))
if mibBuilder.loadTexts:wwpQosPortTable.setStatus(_A)
_WwpQosPortEntry_Object=MibTableRow
wwpQosPortEntry=_WwpQosPortEntry_Object((1,3,6,1,4,1,6141,2,12,1,1,4,1))
wwpQosPortEntry.setIndexNames((0,_D,_L))
if mibBuilder.loadTexts:wwpQosPortEntry.setStatus(_A)
class _WwpQosPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpQosPortIndex_Type.__name__=_B
_WwpQosPortIndex_Object=MibTableColumn
wwpQosPortIndex=_WwpQosPortIndex_Object((1,3,6,1,4,1,6141,2,12,1,1,4,1,1),_WwpQosPortIndex_Type())
wwpQosPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpQosPortIndex.setStatus(_A)
class _WwpQosPortPriQueue_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,3))
_WwpQosPortPriQueue_Type.__name__=_B
_WwpQosPortPriQueue_Object=MibTableColumn
wwpQosPortPriQueue=_WwpQosPortPriQueue_Object((1,3,6,1,4,1,6141,2,12,1,1,4,1,2),_WwpQosPortPriQueue_Type())
wwpQosPortPriQueue.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpQosPortPriQueue.setStatus(_A)
class _WwpQosPortQAlgo_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('weighted',0),('strict',1)))
_WwpQosPortQAlgo_Type.__name__=_B
_WwpQosPortQAlgo_Object=MibTableColumn
wwpQosPortQAlgo=_WwpQosPortQAlgo_Object((1,3,6,1,4,1,6141,2,12,1,1,4,1,3),_WwpQosPortQAlgo_Type())
wwpQosPortQAlgo.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpQosPortQAlgo.setStatus(_A)
class _WwpQosPortQApplyMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('qosMgmtPerQueue',1),('qosMgmtForAllQueues',2)))
_WwpQosPortQApplyMode_Type.__name__=_B
_WwpQosPortQApplyMode_Object=MibTableColumn
wwpQosPortQApplyMode=_WwpQosPortQApplyMode_Object((1,3,6,1,4,1,6141,2,12,1,1,4,1,4),_WwpQosPortQApplyMode_Type())
wwpQosPortQApplyMode.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpQosPortQApplyMode.setStatus(_A)
_WwpQosPortQConfTable_Object=MibTable
wwpQosPortQConfTable=_WwpQosPortQConfTable_Object((1,3,6,1,4,1,6141,2,12,1,1,5))
if mibBuilder.loadTexts:wwpQosPortQConfTable.setStatus(_A)
_WwpQosPortQConfEntry_Object=MibTableRow
wwpQosPortQConfEntry=_WwpQosPortQConfEntry_Object((1,3,6,1,4,1,6141,2,12,1,1,5,1))
wwpQosPortQConfEntry.setIndexNames((0,_D,_M),(0,_D,_N))
if mibBuilder.loadTexts:wwpQosPortQConfEntry.setStatus(_A)
class _WwpQosConfPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpQosConfPortId_Type.__name__=_B
_WwpQosConfPortId_Object=MibTableColumn
wwpQosConfPortId=_WwpQosConfPortId_Object((1,3,6,1,4,1,6141,2,12,1,1,5,1,1),_WwpQosConfPortId_Type())
wwpQosConfPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpQosConfPortId.setStatus(_A)
class _WwpQosConfQueueId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_WwpQosConfQueueId_Type.__name__=_B
_WwpQosConfQueueId_Object=MibTableColumn
wwpQosConfQueueId=_WwpQosConfQueueId_Object((1,3,6,1,4,1,6141,2,12,1,1,5,1,2),_WwpQosConfQueueId_Type())
wwpQosConfQueueId.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpQosConfQueueId.setStatus(_A)
class _WwpQosPortQConfWeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_WwpQosPortQConfWeight_Type.__name__=_B
_WwpQosPortQConfWeight_Object=MibTableColumn
wwpQosPortQConfWeight=_WwpQosPortQConfWeight_Object((1,3,6,1,4,1,6141,2,12,1,1,5,1,3),_WwpQosPortQConfWeight_Type())
wwpQosPortQConfWeight.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpQosPortQConfWeight.setStatus(_A)
class _WwpQosPortQConfDepth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_WwpQosPortQConfDepth_Type.__name__=_B
_WwpQosPortQConfDepth_Object=MibTableColumn
wwpQosPortQConfDepth=_WwpQosPortQConfDepth_Object((1,3,6,1,4,1,6141,2,12,1,1,5,1,4),_WwpQosPortQConfDepth_Type())
wwpQosPortQConfDepth.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpQosPortQConfDepth.setStatus(_A)
_WwpQosPortQConfStatus_Type=RowStatus
_WwpQosPortQConfStatus_Object=MibTableColumn
wwpQosPortQConfStatus=_WwpQosPortQConfStatus_Object((1,3,6,1,4,1,6141,2,12,1,1,5,1,5),_WwpQosPortQConfStatus_Type())
wwpQosPortQConfStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:wwpQosPortQConfStatus.setStatus(_A)
_WwpQosPortQStatusTable_Object=MibTable
wwpQosPortQStatusTable=_WwpQosPortQStatusTable_Object((1,3,6,1,4,1,6141,2,12,1,1,6))
if mibBuilder.loadTexts:wwpQosPortQStatusTable.setStatus(_A)
_WwpQosPortQStatusEntry_Object=MibTableRow
wwpQosPortQStatusEntry=_WwpQosPortQStatusEntry_Object((1,3,6,1,4,1,6141,2,12,1,1,6,1))
wwpQosPortQStatusEntry.setIndexNames((0,_D,_O),(0,_D,_P))
if mibBuilder.loadTexts:wwpQosPortQStatusEntry.setStatus(_A)
class _WwpQosQPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpQosQPortId_Type.__name__=_B
_WwpQosQPortId_Object=MibTableColumn
wwpQosQPortId=_WwpQosQPortId_Object((1,3,6,1,4,1,6141,2,12,1,1,6,1,1),_WwpQosQPortId_Type())
wwpQosQPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpQosQPortId.setStatus(_A)
class _WwpQosQueueId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_WwpQosQueueId_Type.__name__=_B
_WwpQosQueueId_Object=MibTableColumn
wwpQosQueueId=_WwpQosQueueId_Object((1,3,6,1,4,1,6141,2,12,1,1,6,1,2),_WwpQosQueueId_Type())
wwpQosQueueId.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpQosQueueId.setStatus(_A)
class _WwpQosPortQWeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_WwpQosPortQWeight_Type.__name__=_B
_WwpQosPortQWeight_Object=MibTableColumn
wwpQosPortQWeight=_WwpQosPortQWeight_Object((1,3,6,1,4,1,6141,2,12,1,1,6,1,3),_WwpQosPortQWeight_Type())
wwpQosPortQWeight.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpQosPortQWeight.setStatus(_A)
class _WwpQosPortQDepth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_WwpQosPortQDepth_Type.__name__=_B
_WwpQosPortQDepth_Object=MibTableColumn
wwpQosPortQDepth=_WwpQosPortQDepth_Object((1,3,6,1,4,1,6141,2,12,1,1,6,1,4),_WwpQosPortQDepth_Type())
wwpQosPortQDepth.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpQosPortQDepth.setStatus(_A)
class _WwpQosTxAssignmentMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('useQos',0),(_Q,1)))
_WwpQosTxAssignmentMode_Type.__name__=_B
_WwpQosTxAssignmentMode_Object=MibScalar
wwpQosTxAssignmentMode=_WwpQosTxAssignmentMode_Object((1,3,6,1,4,1,6141,2,12,1,1,7),_WwpQosTxAssignmentMode_Type())
wwpQosTxAssignmentMode.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpQosTxAssignmentMode.setStatus(_A)
class _WwpQosPortTxAssignmentMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('usePort',0),(_Q,1)))
_WwpQosPortTxAssignmentMode_Type.__name__=_B
_WwpQosPortTxAssignmentMode_Object=MibScalar
wwpQosPortTxAssignmentMode=_WwpQosPortTxAssignmentMode_Object((1,3,6,1,4,1,6141,2,12,1,1,8),_WwpQosPortTxAssignmentMode_Type())
wwpQosPortTxAssignmentMode.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpQosPortTxAssignmentMode.setStatus(_A)
_WwpQosNotificationPrefix_ObjectIdentity=ObjectIdentity
wwpQosNotificationPrefix=_WwpQosNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,6141,2,12,2))
_WwpQosNotifications_ObjectIdentity=ObjectIdentity
wwpQosNotifications=_WwpQosNotifications_ObjectIdentity((1,3,6,1,4,1,6141,2,12,2,0))
_WwpQosMIBConformance_ObjectIdentity=ObjectIdentity
wwpQosMIBConformance=_WwpQosMIBConformance_ObjectIdentity((1,3,6,1,4,1,6141,2,12,3))
_WwpQosMIBCompliances_ObjectIdentity=ObjectIdentity
wwpQosMIBCompliances=_WwpQosMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6141,2,12,3,1))
_WwpQosMIBGroups_ObjectIdentity=ObjectIdentity
wwpQosMIBGroups=_WwpQosMIBGroups_ObjectIdentity((1,3,6,1,4,1,6141,2,12,3,2))
mibBuilder.exportSymbols(_D,**{'VlanId':VlanId,'wwpQosMIB':wwpQosMIB,'wwpQosMIBObjects':wwpQosMIBObjects,'wwpQos':wwpQos,'wwpQosTable':wwpQosTable,'wwpQosEntry':wwpQosEntry,_F:wwpQosVlanId,_G:wwpQosPortId,'wwpQosRateLimit':wwpQosRateLimit,'wwpQosPriQueue':wwpQosPriQueue,'wwpQosRowStatus':wwpQosRowStatus,'wwpQosStatsTable':wwpQosStatsTable,'wwpQosStatsEntry':wwpQosStatsEntry,_I:wwpQosStatsVlanId,_J:wwpQosStatsPortId,'wwpQosRxBytes':wwpQosRxBytes,'wwpQosRxPkts':wwpQosRxPkts,'wwpQosResetCounters':wwpQosResetCounters,'wwpQosPriToQMapTable':wwpQosPriToQMapTable,'wwpQosPriToQMapEntry':wwpQosPriToQMapEntry,_K:wwpQosRxPriority,'wwpQosTxPriQueue':wwpQosTxPriQueue,'wwpQosPortTable':wwpQosPortTable,'wwpQosPortEntry':wwpQosPortEntry,_L:wwpQosPortIndex,'wwpQosPortPriQueue':wwpQosPortPriQueue,'wwpQosPortQAlgo':wwpQosPortQAlgo,'wwpQosPortQApplyMode':wwpQosPortQApplyMode,'wwpQosPortQConfTable':wwpQosPortQConfTable,'wwpQosPortQConfEntry':wwpQosPortQConfEntry,_M:wwpQosConfPortId,_N:wwpQosConfQueueId,'wwpQosPortQConfWeight':wwpQosPortQConfWeight,'wwpQosPortQConfDepth':wwpQosPortQConfDepth,'wwpQosPortQConfStatus':wwpQosPortQConfStatus,'wwpQosPortQStatusTable':wwpQosPortQStatusTable,'wwpQosPortQStatusEntry':wwpQosPortQStatusEntry,_O:wwpQosQPortId,_P:wwpQosQueueId,'wwpQosPortQWeight':wwpQosPortQWeight,'wwpQosPortQDepth':wwpQosPortQDepth,'wwpQosTxAssignmentMode':wwpQosTxAssignmentMode,'wwpQosPortTxAssignmentMode':wwpQosPortTxAssignmentMode,'wwpQosNotificationPrefix':wwpQosNotificationPrefix,'wwpQosNotifications':wwpQosNotifications,'wwpQosMIBConformance':wwpQosMIBConformance,'wwpQosMIBCompliances':wwpQosMIBCompliances,'wwpQosMIBGroups':wwpQosMIBGroups})