_j='ciscoDot11QosNotificationGroup'
_i='ciscoDot11QosNotifControlGroup'
_h='ciscoDot11QosStatsGroup'
_g='ciscoDot11QosConfigGroup'
_f='cdot11QosChangeNotif'
_e='cdot11QosNotifEnabled'
_d='cdot11QosTransmittedFrames'
_c='cdot11QosMutipleRetries'
_b='cdot11QosRetries'
_a='cdot11QosFails'
_Z='cdot11QosDiscardedFrames'
_Y='cdot11QosIfDiscardedFragments'
_X='cdot11QosIfVlanTrafficClass'
_W='cdot11QosQueuePeakSize'
_V='cdot11QosQueueSize'
_U='cdot11QosQueueQuota'
_T='cdot11QosQueuesAvailable'
_S='cdot11QosOptionEnabled'
_R='cdot11QosOptionImplemented'
_Q='cdot11QosMaxRetry'
_P='cdot11QosBackoffOffset'
_O='cdot11QosCWmax'
_N='cdot11QosCWmin'
_M='cdot11QosIfVlanId'
_L='not-accessible'
_K='TruthValue'
_J='CDot11IfVlanIdOrZero'
_I='cdot11TrafficClass'
_H='cdot11TrafficQueue'
_G='read-write'
_F='Unsigned32'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='CISCO-DOT11-QOS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CDot11IfVlanIdOrZero,=mibBuilder.importSymbols('CISCO-DOT11-IF-MIB',_J)
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_K)
ciscoDot11QosMIB=ModuleIdentity((1,3,6,1,4,1,9,9,416))
if mibBuilder.loadTexts:ciscoDot11QosMIB.setRevisions(('2006-05-09 00:00','2003-11-24 00:00'))
class Cdot11QosTrafficClass(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('background',0),('bestEffort',1),('video',2),('voice',3)))
_CiscoDot11QosMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoDot11QosMIBNotifs=_CiscoDot11QosMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,416,0))
_CiscoDot11QosMIBObjects_ObjectIdentity=ObjectIdentity
ciscoDot11QosMIBObjects=_CiscoDot11QosMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,416,1))
_CiscoDot11QosConfig_ObjectIdentity=ObjectIdentity
ciscoDot11QosConfig=_CiscoDot11QosConfig_ObjectIdentity((1,3,6,1,4,1,9,9,416,1,1))
_Cdot11QosConfigTable_Object=MibTable
cdot11QosConfigTable=_Cdot11QosConfigTable_Object((1,3,6,1,4,1,9,9,416,1,1,1))
if mibBuilder.loadTexts:cdot11QosConfigTable.setStatus(_A)
_Cdot11QosConfigEntry_Object=MibTableRow
cdot11QosConfigEntry=_Cdot11QosConfigEntry_Object((1,3,6,1,4,1,9,9,416,1,1,1,1))
cdot11QosConfigEntry.setIndexNames((0,_D,_E),(0,_B,_H))
if mibBuilder.loadTexts:cdot11QosConfigEntry.setStatus(_A)
_Cdot11TrafficQueue_Type=Unsigned32
_Cdot11TrafficQueue_Object=MibTableColumn
cdot11TrafficQueue=_Cdot11TrafficQueue_Object((1,3,6,1,4,1,9,9,416,1,1,1,1,1),_Cdot11TrafficQueue_Type())
cdot11TrafficQueue.setMaxAccess(_L)
if mibBuilder.loadTexts:cdot11TrafficQueue.setStatus(_A)
_Cdot11TrafficClass_Type=Cdot11QosTrafficClass
_Cdot11TrafficClass_Object=MibTableColumn
cdot11TrafficClass=_Cdot11TrafficClass_Object((1,3,6,1,4,1,9,9,416,1,1,1,1,2),_Cdot11TrafficClass_Type())
cdot11TrafficClass.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot11TrafficClass.setStatus(_A)
class _Cdot11QosCWmin_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_Cdot11QosCWmin_Type.__name__=_F
_Cdot11QosCWmin_Object=MibTableColumn
cdot11QosCWmin=_Cdot11QosCWmin_Object((1,3,6,1,4,1,9,9,416,1,1,1,1,3),_Cdot11QosCWmin_Type())
cdot11QosCWmin.setMaxAccess(_G)
if mibBuilder.loadTexts:cdot11QosCWmin.setStatus(_A)
class _Cdot11QosCWmax_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_Cdot11QosCWmax_Type.__name__=_F
_Cdot11QosCWmax_Object=MibTableColumn
cdot11QosCWmax=_Cdot11QosCWmax_Object((1,3,6,1,4,1,9,9,416,1,1,1,1,4),_Cdot11QosCWmax_Type())
cdot11QosCWmax.setMaxAccess(_G)
if mibBuilder.loadTexts:cdot11QosCWmax.setStatus(_A)
class _Cdot11QosBackoffOffset_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20))
_Cdot11QosBackoffOffset_Type.__name__=_F
_Cdot11QosBackoffOffset_Object=MibTableColumn
cdot11QosBackoffOffset=_Cdot11QosBackoffOffset_Object((1,3,6,1,4,1,9,9,416,1,1,1,1,5),_Cdot11QosBackoffOffset_Type())
cdot11QosBackoffOffset.setMaxAccess(_G)
if mibBuilder.loadTexts:cdot11QosBackoffOffset.setStatus(_A)
class _Cdot11QosMaxRetry_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Cdot11QosMaxRetry_Type.__name__=_F
_Cdot11QosMaxRetry_Object=MibTableColumn
cdot11QosMaxRetry=_Cdot11QosMaxRetry_Object((1,3,6,1,4,1,9,9,416,1,1,1,1,6),_Cdot11QosMaxRetry_Type())
cdot11QosMaxRetry.setMaxAccess(_G)
if mibBuilder.loadTexts:cdot11QosMaxRetry.setStatus(_A)
_Cdot11QosSupportTable_Object=MibTable
cdot11QosSupportTable=_Cdot11QosSupportTable_Object((1,3,6,1,4,1,9,9,416,1,1,2))
if mibBuilder.loadTexts:cdot11QosSupportTable.setStatus(_A)
_Cdot11QosSupportEntry_Object=MibTableRow
cdot11QosSupportEntry=_Cdot11QosSupportEntry_Object((1,3,6,1,4,1,9,9,416,1,1,2,1))
cdot11QosSupportEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cdot11QosSupportEntry.setStatus(_A)
_Cdot11QosOptionImplemented_Type=TruthValue
_Cdot11QosOptionImplemented_Object=MibTableColumn
cdot11QosOptionImplemented=_Cdot11QosOptionImplemented_Object((1,3,6,1,4,1,9,9,416,1,1,2,1,1),_Cdot11QosOptionImplemented_Type())
cdot11QosOptionImplemented.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot11QosOptionImplemented.setStatus(_A)
_Cdot11QosOptionEnabled_Type=TruthValue
_Cdot11QosOptionEnabled_Object=MibTableColumn
cdot11QosOptionEnabled=_Cdot11QosOptionEnabled_Object((1,3,6,1,4,1,9,9,416,1,1,2,1,2),_Cdot11QosOptionEnabled_Type())
cdot11QosOptionEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot11QosOptionEnabled.setStatus(_A)
class _Cdot11QosQueuesAvailable_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,64))
_Cdot11QosQueuesAvailable_Type.__name__=_F
_Cdot11QosQueuesAvailable_Object=MibTableColumn
cdot11QosQueuesAvailable=_Cdot11QosQueuesAvailable_Object((1,3,6,1,4,1,9,9,416,1,1,2,1,3),_Cdot11QosQueuesAvailable_Type())
cdot11QosQueuesAvailable.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot11QosQueuesAvailable.setStatus(_A)
_Cdot11QosIfVlanTable_Object=MibTable
cdot11QosIfVlanTable=_Cdot11QosIfVlanTable_Object((1,3,6,1,4,1,9,9,416,1,1,3))
if mibBuilder.loadTexts:cdot11QosIfVlanTable.setStatus(_A)
_Cdot11QosIfVlanEntry_Object=MibTableRow
cdot11QosIfVlanEntry=_Cdot11QosIfVlanEntry_Object((1,3,6,1,4,1,9,9,416,1,1,3,1))
cdot11QosIfVlanEntry.setIndexNames((0,_D,_E),(0,_B,_M))
if mibBuilder.loadTexts:cdot11QosIfVlanEntry.setStatus(_A)
class _Cdot11QosIfVlanId_Type(CDot11IfVlanIdOrZero):subtypeSpec=CDot11IfVlanIdOrZero.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Cdot11QosIfVlanId_Type.__name__=_J
_Cdot11QosIfVlanId_Object=MibTableColumn
cdot11QosIfVlanId=_Cdot11QosIfVlanId_Object((1,3,6,1,4,1,9,9,416,1,1,3,1,1),_Cdot11QosIfVlanId_Type())
cdot11QosIfVlanId.setMaxAccess(_L)
if mibBuilder.loadTexts:cdot11QosIfVlanId.setStatus(_A)
_Cdot11QosIfVlanTrafficClass_Type=Cdot11QosTrafficClass
_Cdot11QosIfVlanTrafficClass_Object=MibTableColumn
cdot11QosIfVlanTrafficClass=_Cdot11QosIfVlanTrafficClass_Object((1,3,6,1,4,1,9,9,416,1,1,3,1,2),_Cdot11QosIfVlanTrafficClass_Type())
cdot11QosIfVlanTrafficClass.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot11QosIfVlanTrafficClass.setStatus(_A)
_CiscoDot11QosQueue_ObjectIdentity=ObjectIdentity
ciscoDot11QosQueue=_CiscoDot11QosQueue_ObjectIdentity((1,3,6,1,4,1,9,9,416,1,2))
_Cdot11QosQueueTable_Object=MibTable
cdot11QosQueueTable=_Cdot11QosQueueTable_Object((1,3,6,1,4,1,9,9,416,1,2,1))
if mibBuilder.loadTexts:cdot11QosQueueTable.setStatus(_A)
_Cdot11QosQueueEntry_Object=MibTableRow
cdot11QosQueueEntry=_Cdot11QosQueueEntry_Object((1,3,6,1,4,1,9,9,416,1,2,1,1))
cdot11QosQueueEntry.setIndexNames((0,_D,_E),(0,_B,_H))
if mibBuilder.loadTexts:cdot11QosQueueEntry.setStatus(_A)
class _Cdot11QosQueueQuota_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Cdot11QosQueueQuota_Type.__name__=_F
_Cdot11QosQueueQuota_Object=MibTableColumn
cdot11QosQueueQuota=_Cdot11QosQueueQuota_Object((1,3,6,1,4,1,9,9,416,1,2,1,1,1),_Cdot11QosQueueQuota_Type())
cdot11QosQueueQuota.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot11QosQueueQuota.setStatus(_A)
_Cdot11QosQueueSize_Type=Gauge32
_Cdot11QosQueueSize_Object=MibTableColumn
cdot11QosQueueSize=_Cdot11QosQueueSize_Object((1,3,6,1,4,1,9,9,416,1,2,1,1,2),_Cdot11QosQueueSize_Type())
cdot11QosQueueSize.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot11QosQueueSize.setStatus(_A)
_Cdot11QosQueuePeakSize_Type=Counter32
_Cdot11QosQueuePeakSize_Object=MibTableColumn
cdot11QosQueuePeakSize=_Cdot11QosQueuePeakSize_Object((1,3,6,1,4,1,9,9,416,1,2,1,1,3),_Cdot11QosQueuePeakSize_Type())
cdot11QosQueuePeakSize.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot11QosQueuePeakSize.setStatus(_A)
_CiscoDot11QosStatistics_ObjectIdentity=ObjectIdentity
ciscoDot11QosStatistics=_CiscoDot11QosStatistics_ObjectIdentity((1,3,6,1,4,1,9,9,416,1,3))
_Cdot11QosStatisticsTable_Object=MibTable
cdot11QosStatisticsTable=_Cdot11QosStatisticsTable_Object((1,3,6,1,4,1,9,9,416,1,3,1))
if mibBuilder.loadTexts:cdot11QosStatisticsTable.setStatus(_A)
_Cdot11QosStatisticsEntry_Object=MibTableRow
cdot11QosStatisticsEntry=_Cdot11QosStatisticsEntry_Object((1,3,6,1,4,1,9,9,416,1,3,1,1))
cdot11QosStatisticsEntry.setIndexNames((0,_D,_E),(0,_B,_H))
if mibBuilder.loadTexts:cdot11QosStatisticsEntry.setStatus(_A)
_Cdot11QosDiscardedFrames_Type=Counter32
_Cdot11QosDiscardedFrames_Object=MibTableColumn
cdot11QosDiscardedFrames=_Cdot11QosDiscardedFrames_Object((1,3,6,1,4,1,9,9,416,1,3,1,1,1),_Cdot11QosDiscardedFrames_Type())
cdot11QosDiscardedFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot11QosDiscardedFrames.setStatus(_A)
_Cdot11QosFails_Type=Counter32
_Cdot11QosFails_Object=MibTableColumn
cdot11QosFails=_Cdot11QosFails_Object((1,3,6,1,4,1,9,9,416,1,3,1,1,2),_Cdot11QosFails_Type())
cdot11QosFails.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot11QosFails.setStatus(_A)
_Cdot11QosRetries_Type=Counter32
_Cdot11QosRetries_Object=MibTableColumn
cdot11QosRetries=_Cdot11QosRetries_Object((1,3,6,1,4,1,9,9,416,1,3,1,1,3),_Cdot11QosRetries_Type())
cdot11QosRetries.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot11QosRetries.setStatus(_A)
_Cdot11QosMutipleRetries_Type=Counter32
_Cdot11QosMutipleRetries_Object=MibTableColumn
cdot11QosMutipleRetries=_Cdot11QosMutipleRetries_Object((1,3,6,1,4,1,9,9,416,1,3,1,1,4),_Cdot11QosMutipleRetries_Type())
cdot11QosMutipleRetries.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot11QosMutipleRetries.setStatus(_A)
_Cdot11QosTransmittedFrames_Type=Counter32
_Cdot11QosTransmittedFrames_Object=MibTableColumn
cdot11QosTransmittedFrames=_Cdot11QosTransmittedFrames_Object((1,3,6,1,4,1,9,9,416,1,3,1,1,5),_Cdot11QosTransmittedFrames_Type())
cdot11QosTransmittedFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot11QosTransmittedFrames.setStatus(_A)
_Cdot11QosIfStatisticsTable_Object=MibTable
cdot11QosIfStatisticsTable=_Cdot11QosIfStatisticsTable_Object((1,3,6,1,4,1,9,9,416,1,3,2))
if mibBuilder.loadTexts:cdot11QosIfStatisticsTable.setStatus(_A)
_Cdot11QosIfStatisticsEntry_Object=MibTableRow
cdot11QosIfStatisticsEntry=_Cdot11QosIfStatisticsEntry_Object((1,3,6,1,4,1,9,9,416,1,3,2,1))
cdot11QosIfStatisticsEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cdot11QosIfStatisticsEntry.setStatus(_A)
_Cdot11QosIfDiscardedFragments_Type=Counter32
_Cdot11QosIfDiscardedFragments_Object=MibTableColumn
cdot11QosIfDiscardedFragments=_Cdot11QosIfDiscardedFragments_Object((1,3,6,1,4,1,9,9,416,1,3,2,1,1),_Cdot11QosIfDiscardedFragments_Type())
cdot11QosIfDiscardedFragments.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot11QosIfDiscardedFragments.setStatus(_A)
_CiscoDot11QosNotifControl_ObjectIdentity=ObjectIdentity
ciscoDot11QosNotifControl=_CiscoDot11QosNotifControl_ObjectIdentity((1,3,6,1,4,1,9,9,416,1,4))
class _Cdot11QosNotifEnabled_Type(TruthValue):defaultValue=2
_Cdot11QosNotifEnabled_Type.__name__=_K
_Cdot11QosNotifEnabled_Object=MibScalar
cdot11QosNotifEnabled=_Cdot11QosNotifEnabled_Object((1,3,6,1,4,1,9,9,416,1,4,1),_Cdot11QosNotifEnabled_Type())
cdot11QosNotifEnabled.setMaxAccess(_G)
if mibBuilder.loadTexts:cdot11QosNotifEnabled.setStatus(_A)
_CiscoDot11QosMIBConformance_ObjectIdentity=ObjectIdentity
ciscoDot11QosMIBConformance=_CiscoDot11QosMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,416,2))
_CiscoDot11QosMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoDot11QosMIBCompliances=_CiscoDot11QosMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,416,2,1))
_CiscoDot11QosMIBGroups_ObjectIdentity=ObjectIdentity
ciscoDot11QosMIBGroups=_CiscoDot11QosMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,416,2,2))
ciscoDot11QosConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,416,2,2,1))
ciscoDot11QosConfigGroup.setObjects(*((_B,_I),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:ciscoDot11QosConfigGroup.setStatus(_A)
ciscoDot11QosStatsGroup=ObjectGroup((1,3,6,1,4,1,9,9,416,2,2,2))
ciscoDot11QosStatsGroup.setObjects(*((_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d)))
if mibBuilder.loadTexts:ciscoDot11QosStatsGroup.setStatus(_A)
ciscoDot11QosNotifControlGroup=ObjectGroup((1,3,6,1,4,1,9,9,416,2,2,3))
ciscoDot11QosNotifControlGroup.setObjects((_B,_e))
if mibBuilder.loadTexts:ciscoDot11QosNotifControlGroup.setStatus(_A)
cdot11QosChangeNotif=NotificationType((1,3,6,1,4,1,9,9,416,0,1))
cdot11QosChangeNotif.setObjects((_B,_I))
if mibBuilder.loadTexts:cdot11QosChangeNotif.setStatus(_A)
ciscoDot11QosNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,416,2,2,4))
ciscoDot11QosNotificationGroup.setObjects((_B,_f))
if mibBuilder.loadTexts:ciscoDot11QosNotificationGroup.setStatus(_A)
ciscoDot11QosMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,416,2,1,1))
ciscoDot11QosMIBCompliance.setObjects(*((_B,_g),(_B,_h),(_B,_i),(_B,_j)))
if mibBuilder.loadTexts:ciscoDot11QosMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'Cdot11QosTrafficClass':Cdot11QosTrafficClass,'ciscoDot11QosMIB':ciscoDot11QosMIB,'ciscoDot11QosMIBNotifs':ciscoDot11QosMIBNotifs,_f:cdot11QosChangeNotif,'ciscoDot11QosMIBObjects':ciscoDot11QosMIBObjects,'ciscoDot11QosConfig':ciscoDot11QosConfig,'cdot11QosConfigTable':cdot11QosConfigTable,'cdot11QosConfigEntry':cdot11QosConfigEntry,_H:cdot11TrafficQueue,_I:cdot11TrafficClass,_N:cdot11QosCWmin,_O:cdot11QosCWmax,_P:cdot11QosBackoffOffset,_Q:cdot11QosMaxRetry,'cdot11QosSupportTable':cdot11QosSupportTable,'cdot11QosSupportEntry':cdot11QosSupportEntry,_R:cdot11QosOptionImplemented,_S:cdot11QosOptionEnabled,_T:cdot11QosQueuesAvailable,'cdot11QosIfVlanTable':cdot11QosIfVlanTable,'cdot11QosIfVlanEntry':cdot11QosIfVlanEntry,_M:cdot11QosIfVlanId,_X:cdot11QosIfVlanTrafficClass,'ciscoDot11QosQueue':ciscoDot11QosQueue,'cdot11QosQueueTable':cdot11QosQueueTable,'cdot11QosQueueEntry':cdot11QosQueueEntry,_U:cdot11QosQueueQuota,_V:cdot11QosQueueSize,_W:cdot11QosQueuePeakSize,'ciscoDot11QosStatistics':ciscoDot11QosStatistics,'cdot11QosStatisticsTable':cdot11QosStatisticsTable,'cdot11QosStatisticsEntry':cdot11QosStatisticsEntry,_Z:cdot11QosDiscardedFrames,_a:cdot11QosFails,_b:cdot11QosRetries,_c:cdot11QosMutipleRetries,_d:cdot11QosTransmittedFrames,'cdot11QosIfStatisticsTable':cdot11QosIfStatisticsTable,'cdot11QosIfStatisticsEntry':cdot11QosIfStatisticsEntry,_Y:cdot11QosIfDiscardedFragments,'ciscoDot11QosNotifControl':ciscoDot11QosNotifControl,_e:cdot11QosNotifEnabled,'ciscoDot11QosMIBConformance':ciscoDot11QosMIBConformance,'ciscoDot11QosMIBCompliances':ciscoDot11QosMIBCompliances,'ciscoDot11QosMIBCompliance':ciscoDot11QosMIBCompliance,'ciscoDot11QosMIBGroups':ciscoDot11QosMIBGroups,_g:ciscoDot11QosConfigGroup,_h:ciscoDot11QosStatsGroup,_i:ciscoDot11QosNotifControlGroup,_j:ciscoDot11QosNotificationGroup})