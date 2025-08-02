_U='efpAgentCosTrafficInfoQueueWredQueue'
_T='efpAgentCosTrafficInfoQueueTxQueue'
_S='efpAgentCosTrafficInfoQueueTotalDrops'
_R='efpAgentCosTrafficInfoQueueTotalPass'
_Q='efpAgentCosTrafficInfoQueueName'
_P='efpAgentCosTrafficInfoWredQueue'
_O='efpAgentCosTrafficInfoYellowDrops'
_N='efpAgentCosTrafficInfoRedDrops'
_M='efpAgentCosTrafficInfoRxQueue'
_L='efpAgentCosTrafficInfoTxQueue'
_K='efpAgentCosTrafficInfoTotalDrops'
_J='efpAgentCosTrafficInfoTotalPass'
_I='efpAgentCosTrafficInfoQueueIndex'
_H='DisplayString'
_G='efpAgentQosCosTrafficInfoQueueGroup'
_F='efpAgentQosCosTrafficInfoGroup'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='ELTEX-FASTPATH-QOS-COS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltFastpathQosMIB,=mibBuilder.importSymbols('ELTEX-FASTPATH-QOS-MIB','eltFastpathQosMIB')
ifIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','TextualConvention')
eltFastpathQosCosMIB=ModuleIdentity((1,3,6,1,4,1,35265,1,103,2,1))
if mibBuilder.loadTexts:eltFastpathQosCosMIB.setRevisions(('2017-03-09 00:00',))
_EfpQosCosObjects_ObjectIdentity=ObjectIdentity
efpQosCosObjects=_EfpQosCosObjects_ObjectIdentity((1,3,6,1,4,1,35265,1,103,2,1,1))
_EfpQosCosStatistics_ObjectIdentity=ObjectIdentity
efpQosCosStatistics=_EfpQosCosStatistics_ObjectIdentity((1,3,6,1,4,1,35265,1,103,2,1,1,3))
_EfpAgentCosTrafficInfoTable_Object=MibTable
efpAgentCosTrafficInfoTable=_EfpAgentCosTrafficInfoTable_Object((1,3,6,1,4,1,35265,1,103,2,1,1,3,1))
if mibBuilder.loadTexts:efpAgentCosTrafficInfoTable.setStatus(_A)
_EfpAgentCosTrafficInfoEntry_Object=MibTableRow
efpAgentCosTrafficInfoEntry=_EfpAgentCosTrafficInfoEntry_Object((1,3,6,1,4,1,35265,1,103,2,1,1,3,1,1))
efpAgentCosTrafficInfoEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:efpAgentCosTrafficInfoEntry.setStatus(_A)
_EfpAgentCosTrafficInfoTotalPass_Type=Counter64
_EfpAgentCosTrafficInfoTotalPass_Object=MibTableColumn
efpAgentCosTrafficInfoTotalPass=_EfpAgentCosTrafficInfoTotalPass_Object((1,3,6,1,4,1,35265,1,103,2,1,1,3,1,1,1),_EfpAgentCosTrafficInfoTotalPass_Type())
efpAgentCosTrafficInfoTotalPass.setMaxAccess(_C)
if mibBuilder.loadTexts:efpAgentCosTrafficInfoTotalPass.setStatus(_A)
_EfpAgentCosTrafficInfoTotalDrops_Type=Counter64
_EfpAgentCosTrafficInfoTotalDrops_Object=MibTableColumn
efpAgentCosTrafficInfoTotalDrops=_EfpAgentCosTrafficInfoTotalDrops_Object((1,3,6,1,4,1,35265,1,103,2,1,1,3,1,1,2),_EfpAgentCosTrafficInfoTotalDrops_Type())
efpAgentCosTrafficInfoTotalDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:efpAgentCosTrafficInfoTotalDrops.setStatus(_A)
_EfpAgentCosTrafficInfoTxQueue_Type=Gauge32
_EfpAgentCosTrafficInfoTxQueue_Object=MibTableColumn
efpAgentCosTrafficInfoTxQueue=_EfpAgentCosTrafficInfoTxQueue_Object((1,3,6,1,4,1,35265,1,103,2,1,1,3,1,1,3),_EfpAgentCosTrafficInfoTxQueue_Type())
efpAgentCosTrafficInfoTxQueue.setMaxAccess(_C)
if mibBuilder.loadTexts:efpAgentCosTrafficInfoTxQueue.setStatus(_A)
_EfpAgentCosTrafficInfoRxQueue_Type=Gauge32
_EfpAgentCosTrafficInfoRxQueue_Object=MibTableColumn
efpAgentCosTrafficInfoRxQueue=_EfpAgentCosTrafficInfoRxQueue_Object((1,3,6,1,4,1,35265,1,103,2,1,1,3,1,1,4),_EfpAgentCosTrafficInfoRxQueue_Type())
efpAgentCosTrafficInfoRxQueue.setMaxAccess(_C)
if mibBuilder.loadTexts:efpAgentCosTrafficInfoRxQueue.setStatus(_A)
_EfpAgentCosTrafficInfoRedDrops_Type=Counter64
_EfpAgentCosTrafficInfoRedDrops_Object=MibTableColumn
efpAgentCosTrafficInfoRedDrops=_EfpAgentCosTrafficInfoRedDrops_Object((1,3,6,1,4,1,35265,1,103,2,1,1,3,1,1,5),_EfpAgentCosTrafficInfoRedDrops_Type())
efpAgentCosTrafficInfoRedDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:efpAgentCosTrafficInfoRedDrops.setStatus(_A)
_EfpAgentCosTrafficInfoYellowDrops_Type=Counter64
_EfpAgentCosTrafficInfoYellowDrops_Object=MibTableColumn
efpAgentCosTrafficInfoYellowDrops=_EfpAgentCosTrafficInfoYellowDrops_Object((1,3,6,1,4,1,35265,1,103,2,1,1,3,1,1,6),_EfpAgentCosTrafficInfoYellowDrops_Type())
efpAgentCosTrafficInfoYellowDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:efpAgentCosTrafficInfoYellowDrops.setStatus(_A)
_EfpAgentCosTrafficInfoWredQueue_Type=Gauge32
_EfpAgentCosTrafficInfoWredQueue_Object=MibTableColumn
efpAgentCosTrafficInfoWredQueue=_EfpAgentCosTrafficInfoWredQueue_Object((1,3,6,1,4,1,35265,1,103,2,1,1,3,1,1,7),_EfpAgentCosTrafficInfoWredQueue_Type())
efpAgentCosTrafficInfoWredQueue.setMaxAccess(_C)
if mibBuilder.loadTexts:efpAgentCosTrafficInfoWredQueue.setStatus(_A)
_EfpAgentCosTrafficInfoQueueTable_Object=MibTable
efpAgentCosTrafficInfoQueueTable=_EfpAgentCosTrafficInfoQueueTable_Object((1,3,6,1,4,1,35265,1,103,2,1,1,3,2))
if mibBuilder.loadTexts:efpAgentCosTrafficInfoQueueTable.setStatus(_A)
_EfpAgentCosTrafficInfoQueueEntry_Object=MibTableRow
efpAgentCosTrafficInfoQueueEntry=_EfpAgentCosTrafficInfoQueueEntry_Object((1,3,6,1,4,1,35265,1,103,2,1,1,3,2,1))
efpAgentCosTrafficInfoQueueEntry.setIndexNames((0,_D,_E),(0,_B,_I))
if mibBuilder.loadTexts:efpAgentCosTrafficInfoQueueEntry.setStatus(_A)
_EfpAgentCosTrafficInfoQueueIndex_Type=Unsigned32
_EfpAgentCosTrafficInfoQueueIndex_Object=MibTableColumn
efpAgentCosTrafficInfoQueueIndex=_EfpAgentCosTrafficInfoQueueIndex_Object((1,3,6,1,4,1,35265,1,103,2,1,1,3,2,1,1),_EfpAgentCosTrafficInfoQueueIndex_Type())
efpAgentCosTrafficInfoQueueIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:efpAgentCosTrafficInfoQueueIndex.setStatus(_A)
class _EfpAgentCosTrafficInfoQueueName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,3))
_EfpAgentCosTrafficInfoQueueName_Type.__name__=_H
_EfpAgentCosTrafficInfoQueueName_Object=MibTableColumn
efpAgentCosTrafficInfoQueueName=_EfpAgentCosTrafficInfoQueueName_Object((1,3,6,1,4,1,35265,1,103,2,1,1,3,2,1,2),_EfpAgentCosTrafficInfoQueueName_Type())
efpAgentCosTrafficInfoQueueName.setMaxAccess(_C)
if mibBuilder.loadTexts:efpAgentCosTrafficInfoQueueName.setStatus(_A)
_EfpAgentCosTrafficInfoQueueTotalPass_Type=Counter64
_EfpAgentCosTrafficInfoQueueTotalPass_Object=MibTableColumn
efpAgentCosTrafficInfoQueueTotalPass=_EfpAgentCosTrafficInfoQueueTotalPass_Object((1,3,6,1,4,1,35265,1,103,2,1,1,3,2,1,3),_EfpAgentCosTrafficInfoQueueTotalPass_Type())
efpAgentCosTrafficInfoQueueTotalPass.setMaxAccess(_C)
if mibBuilder.loadTexts:efpAgentCosTrafficInfoQueueTotalPass.setStatus(_A)
_EfpAgentCosTrafficInfoQueueTotalDrops_Type=Counter64
_EfpAgentCosTrafficInfoQueueTotalDrops_Object=MibTableColumn
efpAgentCosTrafficInfoQueueTotalDrops=_EfpAgentCosTrafficInfoQueueTotalDrops_Object((1,3,6,1,4,1,35265,1,103,2,1,1,3,2,1,4),_EfpAgentCosTrafficInfoQueueTotalDrops_Type())
efpAgentCosTrafficInfoQueueTotalDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:efpAgentCosTrafficInfoQueueTotalDrops.setStatus(_A)
_EfpAgentCosTrafficInfoQueueTxQueue_Type=Gauge32
_EfpAgentCosTrafficInfoQueueTxQueue_Object=MibTableColumn
efpAgentCosTrafficInfoQueueTxQueue=_EfpAgentCosTrafficInfoQueueTxQueue_Object((1,3,6,1,4,1,35265,1,103,2,1,1,3,2,1,5),_EfpAgentCosTrafficInfoQueueTxQueue_Type())
efpAgentCosTrafficInfoQueueTxQueue.setMaxAccess(_C)
if mibBuilder.loadTexts:efpAgentCosTrafficInfoQueueTxQueue.setStatus(_A)
_EfpAgentCosTrafficInfoQueueWredQueue_Type=Gauge32
_EfpAgentCosTrafficInfoQueueWredQueue_Object=MibTableColumn
efpAgentCosTrafficInfoQueueWredQueue=_EfpAgentCosTrafficInfoQueueWredQueue_Object((1,3,6,1,4,1,35265,1,103,2,1,1,3,2,1,6),_EfpAgentCosTrafficInfoQueueWredQueue_Type())
efpAgentCosTrafficInfoQueueWredQueue.setMaxAccess(_C)
if mibBuilder.loadTexts:efpAgentCosTrafficInfoQueueWredQueue.setStatus(_A)
_EfpQosCosNotifications_ObjectIdentity=ObjectIdentity
efpQosCosNotifications=_EfpQosCosNotifications_ObjectIdentity((1,3,6,1,4,1,35265,1,103,2,1,2))
_EfpQosCosNotificationsPrefix_ObjectIdentity=ObjectIdentity
efpQosCosNotificationsPrefix=_EfpQosCosNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,35265,1,103,2,1,2,0))
_EfpQosCosConformance_ObjectIdentity=ObjectIdentity
efpQosCosConformance=_EfpQosCosConformance_ObjectIdentity((1,3,6,1,4,1,35265,1,103,2,1,3))
_EfpQosCosCompliances_ObjectIdentity=ObjectIdentity
efpQosCosCompliances=_EfpQosCosCompliances_ObjectIdentity((1,3,6,1,4,1,35265,1,103,2,1,3,1))
_EfpQosCosGroups_ObjectIdentity=ObjectIdentity
efpQosCosGroups=_EfpQosCosGroups_ObjectIdentity((1,3,6,1,4,1,35265,1,103,2,1,3,2))
efpAgentQosCosTrafficInfoGroup=ObjectGroup((1,3,6,1,4,1,35265,1,103,2,1,3,2,1))
efpAgentQosCosTrafficInfoGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:efpAgentQosCosTrafficInfoGroup.setStatus(_A)
efpAgentQosCosTrafficInfoQueueGroup=ObjectGroup((1,3,6,1,4,1,35265,1,103,2,1,3,2,2))
efpAgentQosCosTrafficInfoQueueGroup.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:efpAgentQosCosTrafficInfoQueueGroup.setStatus(_A)
efpQosCosCompliance=ModuleCompliance((1,3,6,1,4,1,35265,1,103,2,1,3,1,1))
efpQosCosCompliance.setObjects(*((_B,_F),(_B,_G)))
if mibBuilder.loadTexts:efpQosCosCompliance.setStatus('obsolete')
efpQosCosCompliance2=ModuleCompliance((1,3,6,1,4,1,35265,1,103,2,1,3,1,2))
efpQosCosCompliance2.setObjects(*((_B,_F),(_B,_G)))
if mibBuilder.loadTexts:efpQosCosCompliance2.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'eltFastpathQosCosMIB':eltFastpathQosCosMIB,'efpQosCosObjects':efpQosCosObjects,'efpQosCosStatistics':efpQosCosStatistics,'efpAgentCosTrafficInfoTable':efpAgentCosTrafficInfoTable,'efpAgentCosTrafficInfoEntry':efpAgentCosTrafficInfoEntry,_J:efpAgentCosTrafficInfoTotalPass,_K:efpAgentCosTrafficInfoTotalDrops,_L:efpAgentCosTrafficInfoTxQueue,_M:efpAgentCosTrafficInfoRxQueue,_N:efpAgentCosTrafficInfoRedDrops,_O:efpAgentCosTrafficInfoYellowDrops,_P:efpAgentCosTrafficInfoWredQueue,'efpAgentCosTrafficInfoQueueTable':efpAgentCosTrafficInfoQueueTable,'efpAgentCosTrafficInfoQueueEntry':efpAgentCosTrafficInfoQueueEntry,_I:efpAgentCosTrafficInfoQueueIndex,_Q:efpAgentCosTrafficInfoQueueName,_R:efpAgentCosTrafficInfoQueueTotalPass,_S:efpAgentCosTrafficInfoQueueTotalDrops,_T:efpAgentCosTrafficInfoQueueTxQueue,_U:efpAgentCosTrafficInfoQueueWredQueue,'efpQosCosNotifications':efpQosCosNotifications,'efpQosCosNotificationsPrefix':efpQosCosNotificationsPrefix,'efpQosCosConformance':efpQosCosConformance,'efpQosCosCompliances':efpQosCosCompliances,'efpQosCosCompliance':efpQosCosCompliance,'efpQosCosCompliance2':efpQosCosCompliance2,'efpQosCosGroups':efpQosCosGroups,_F:efpAgentQosCosTrafficInfoGroup,_G:efpAgentQosCosTrafficInfoQueueGroup})