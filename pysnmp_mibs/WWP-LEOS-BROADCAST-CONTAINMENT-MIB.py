_O='not-accessible'
_N='DisplayString'
_M='Unsigned32'
_L='wwpLeosBroadcastContainmentFilterName'
_K='disable'
_J='enable'
_I='wwpLeosBroadcastContainmentPortId'
_H='wwpLeosBroadcastContainmentVlanId'
_G='read-write'
_F='wwpLeosBroadcastContainmentIndex'
_E='read-only'
_D='read-create'
_C='WWP-LEOS-BROADCAST-CONTAINMENT-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_M,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_N,'PhysAddress','RowStatus','TextualConvention','TruthValue')
wwpModulesLeos,=mibBuilder.importSymbols('WWP-SMI','wwpModulesLeos')
wwpLeosBroadcastContainmentMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,60,8))
if mibBuilder.loadTexts:wwpLeosBroadcastContainmentMIB.setRevisions(('2012-03-08 00:00','2012-03-02 00:00','2009-02-05 00:00','2008-06-25 00:00','2008-06-18 21:00','2007-06-02 21:00'))
class WwpLeosBroadcastContainmentCapabilitiesMap(TextualConvention,Bits):status=_A;namedValues=NamedValues(*((_H,0),(_I,1)))
_WwpLeosBroadcastContainmentMIBObjects_ObjectIdentity=ObjectIdentity
wwpLeosBroadcastContainmentMIBObjects=_WwpLeosBroadcastContainmentMIBObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,60,8,1))
_WwpLeosBroadcastContainmentCapability_Type=WwpLeosBroadcastContainmentCapabilitiesMap
_WwpLeosBroadcastContainmentCapability_Object=MibScalar
wwpLeosBroadcastContainmentCapability=_WwpLeosBroadcastContainmentCapability_Object((1,3,6,1,4,1,6141,2,60,8,1,1),_WwpLeosBroadcastContainmentCapability_Type())
wwpLeosBroadcastContainmentCapability.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosBroadcastContainmentCapability.setStatus(_A)
_WwpLeosBroadcastContainmentPktDroppedStats_Type=Counter32
_WwpLeosBroadcastContainmentPktDroppedStats_Object=MibScalar
wwpLeosBroadcastContainmentPktDroppedStats=_WwpLeosBroadcastContainmentPktDroppedStats_Object((1,3,6,1,4,1,6141,2,60,8,1,2),_WwpLeosBroadcastContainmentPktDroppedStats_Type())
wwpLeosBroadcastContainmentPktDroppedStats.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosBroadcastContainmentPktDroppedStats.setStatus(_A)
_WwpLeosBroadcastContainmentFilterTable_Object=MibTable
wwpLeosBroadcastContainmentFilterTable=_WwpLeosBroadcastContainmentFilterTable_Object((1,3,6,1,4,1,6141,2,60,8,1,4))
if mibBuilder.loadTexts:wwpLeosBroadcastContainmentFilterTable.setStatus(_A)
_WwpLeosBroadcastContainmentFilterEntry_Object=MibTableRow
wwpLeosBroadcastContainmentFilterEntry=_WwpLeosBroadcastContainmentFilterEntry_Object((1,3,6,1,4,1,6141,2,60,8,1,4,1))
wwpLeosBroadcastContainmentFilterEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:wwpLeosBroadcastContainmentFilterEntry.setStatus(_A)
class _WwpLeosBroadcastContainmentIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_WwpLeosBroadcastContainmentIndex_Type.__name__=_B
_WwpLeosBroadcastContainmentIndex_Object=MibTableColumn
wwpLeosBroadcastContainmentIndex=_WwpLeosBroadcastContainmentIndex_Object((1,3,6,1,4,1,6141,2,60,8,1,4,1,1),_WwpLeosBroadcastContainmentIndex_Type())
wwpLeosBroadcastContainmentIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosBroadcastContainmentIndex.setStatus(_A)
class _WwpLeosBroadcastContainmentFilterName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_WwpLeosBroadcastContainmentFilterName_Type.__name__=_N
_WwpLeosBroadcastContainmentFilterName_Object=MibTableColumn
wwpLeosBroadcastContainmentFilterName=_WwpLeosBroadcastContainmentFilterName_Object((1,3,6,1,4,1,6141,2,60,8,1,4,1,2),_WwpLeosBroadcastContainmentFilterName_Type())
wwpLeosBroadcastContainmentFilterName.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosBroadcastContainmentFilterName.setStatus(_A)
class _WwpLeosBroadcastContainmentPktLimit_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,104856000))
_WwpLeosBroadcastContainmentPktLimit_Type.__name__=_B
_WwpLeosBroadcastContainmentPktLimit_Object=MibTableColumn
wwpLeosBroadcastContainmentPktLimit=_WwpLeosBroadcastContainmentPktLimit_Object((1,3,6,1,4,1,6141,2,60,8,1,4,1,3),_WwpLeosBroadcastContainmentPktLimit_Type())
wwpLeosBroadcastContainmentPktLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosBroadcastContainmentPktLimit.setStatus(_A)
_WwpLeosBroadcastContainmentPktDropState_Type=TruthValue
_WwpLeosBroadcastContainmentPktDropState_Object=MibTableColumn
wwpLeosBroadcastContainmentPktDropState=_WwpLeosBroadcastContainmentPktDropState_Object((1,3,6,1,4,1,6141,2,60,8,1,4,1,4),_WwpLeosBroadcastContainmentPktDropState_Type())
wwpLeosBroadcastContainmentPktDropState.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosBroadcastContainmentPktDropState.setStatus(_A)
_WwpLeosBroadcastContainmentStatus_Type=RowStatus
_WwpLeosBroadcastContainmentStatus_Object=MibTableColumn
wwpLeosBroadcastContainmentStatus=_WwpLeosBroadcastContainmentStatus_Object((1,3,6,1,4,1,6141,2,60,8,1,4,1,5),_WwpLeosBroadcastContainmentStatus_Type())
wwpLeosBroadcastContainmentStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosBroadcastContainmentStatus.setStatus(_A)
class _WwpLeosBroadcastContainmentKbps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
_WwpLeosBroadcastContainmentKbps_Type.__name__=_B
_WwpLeosBroadcastContainmentKbps_Object=MibTableColumn
wwpLeosBroadcastContainmentKbps=_WwpLeosBroadcastContainmentKbps_Object((1,3,6,1,4,1,6141,2,60,8,1,4,1,6),_WwpLeosBroadcastContainmentKbps_Type())
wwpLeosBroadcastContainmentKbps.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosBroadcastContainmentKbps.setStatus(_A)
class _WwpLeosBroadcastContainmentClassifier_Type(Unsigned32):defaultValue=3
_WwpLeosBroadcastContainmentClassifier_Type.__name__=_M
_WwpLeosBroadcastContainmentClassifier_Object=MibTableColumn
wwpLeosBroadcastContainmentClassifier=_WwpLeosBroadcastContainmentClassifier_Object((1,3,6,1,4,1,6141,2,60,8,1,4,1,7),_WwpLeosBroadcastContainmentClassifier_Type())
wwpLeosBroadcastContainmentClassifier.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosBroadcastContainmentClassifier.setStatus(_A)
_WwpLeosBroadcastContainmentFilterMemTable_Object=MibTable
wwpLeosBroadcastContainmentFilterMemTable=_WwpLeosBroadcastContainmentFilterMemTable_Object((1,3,6,1,4,1,6141,2,60,8,1,5))
if mibBuilder.loadTexts:wwpLeosBroadcastContainmentFilterMemTable.setStatus(_A)
_WwpLeosBroadcastContainmentFilterMemEntry_Object=MibTableRow
wwpLeosBroadcastContainmentFilterMemEntry=_WwpLeosBroadcastContainmentFilterMemEntry_Object((1,3,6,1,4,1,6141,2,60,8,1,5,1))
wwpLeosBroadcastContainmentFilterMemEntry.setIndexNames((0,_C,_F),(0,_C,_H),(0,_C,_I))
if mibBuilder.loadTexts:wwpLeosBroadcastContainmentFilterMemEntry.setStatus(_A)
class _WwpLeosBroadcastContainmentVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_WwpLeosBroadcastContainmentVlanId_Type.__name__=_B
_WwpLeosBroadcastContainmentVlanId_Object=MibTableColumn
wwpLeosBroadcastContainmentVlanId=_WwpLeosBroadcastContainmentVlanId_Object((1,3,6,1,4,1,6141,2,60,8,1,5,1,1),_WwpLeosBroadcastContainmentVlanId_Type())
wwpLeosBroadcastContainmentVlanId.setMaxAccess(_O)
if mibBuilder.loadTexts:wwpLeosBroadcastContainmentVlanId.setStatus(_A)
class _WwpLeosBroadcastContainmentPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_WwpLeosBroadcastContainmentPortId_Type.__name__=_B
_WwpLeosBroadcastContainmentPortId_Object=MibTableColumn
wwpLeosBroadcastContainmentPortId=_WwpLeosBroadcastContainmentPortId_Object((1,3,6,1,4,1,6141,2,60,8,1,5,1,2),_WwpLeosBroadcastContainmentPortId_Type())
wwpLeosBroadcastContainmentPortId.setMaxAccess(_O)
if mibBuilder.loadTexts:wwpLeosBroadcastContainmentPortId.setStatus(_A)
_WwpLeosBroadcastContainmentFilterMemStatus_Type=RowStatus
_WwpLeosBroadcastContainmentFilterMemStatus_Object=MibTableColumn
wwpLeosBroadcastContainmentFilterMemStatus=_WwpLeosBroadcastContainmentFilterMemStatus_Object((1,3,6,1,4,1,6141,2,60,8,1,5,1,3),_WwpLeosBroadcastContainmentFilterMemStatus_Type())
wwpLeosBroadcastContainmentFilterMemStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosBroadcastContainmentFilterMemStatus.setStatus(_A)
class _WwpLeosBroadcastContainmentGlobalStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_WwpLeosBroadcastContainmentGlobalStatus_Type.__name__=_B
_WwpLeosBroadcastContainmentGlobalStatus_Object=MibScalar
wwpLeosBroadcastContainmentGlobalStatus=_WwpLeosBroadcastContainmentGlobalStatus_Object((1,3,6,1,4,1,6141,2,60,8,1,6),_WwpLeosBroadcastContainmentGlobalStatus_Type())
wwpLeosBroadcastContainmentGlobalStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:wwpLeosBroadcastContainmentGlobalStatus.setStatus(_A)
class _WwpLeosBroadcastContainmentGlobalTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,2560))
_WwpLeosBroadcastContainmentGlobalTime_Type.__name__=_B
_WwpLeosBroadcastContainmentGlobalTime_Object=MibScalar
wwpLeosBroadcastContainmentGlobalTime=_WwpLeosBroadcastContainmentGlobalTime_Object((1,3,6,1,4,1,6141,2,60,8,1,7),_WwpLeosBroadcastContainmentGlobalTime_Type())
wwpLeosBroadcastContainmentGlobalTime.setMaxAccess(_G)
if mibBuilder.loadTexts:wwpLeosBroadcastContainmentGlobalTime.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosBroadcastContainmentGlobalTime.setUnits('milli-seconds')
class _WwpLeosBroadcastContainmentIgnoreRapsMessages_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_WwpLeosBroadcastContainmentIgnoreRapsMessages_Type.__name__=_B
_WwpLeosBroadcastContainmentIgnoreRapsMessages_Object=MibScalar
wwpLeosBroadcastContainmentIgnoreRapsMessages=_WwpLeosBroadcastContainmentIgnoreRapsMessages_Object((1,3,6,1,4,1,6141,2,60,8,1,8),_WwpLeosBroadcastContainmentIgnoreRapsMessages_Type())
wwpLeosBroadcastContainmentIgnoreRapsMessages.setMaxAccess(_G)
if mibBuilder.loadTexts:wwpLeosBroadcastContainmentIgnoreRapsMessages.setStatus(_A)
class _WwpLeosBroadcastContainmentResourceMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_WwpLeosBroadcastContainmentResourceMode_Type.__name__=_B
_WwpLeosBroadcastContainmentResourceMode_Object=MibScalar
wwpLeosBroadcastContainmentResourceMode=_WwpLeosBroadcastContainmentResourceMode_Object((1,3,6,1,4,1,6141,2,60,8,1,9),_WwpLeosBroadcastContainmentResourceMode_Type())
wwpLeosBroadcastContainmentResourceMode.setMaxAccess(_G)
if mibBuilder.loadTexts:wwpLeosBroadcastContainmentResourceMode.setStatus(_A)
_WwpLeosBroadcastContainmentBytesDroppedStats_Type=Counter64
_WwpLeosBroadcastContainmentBytesDroppedStats_Object=MibScalar
wwpLeosBroadcastContainmentBytesDroppedStats=_WwpLeosBroadcastContainmentBytesDroppedStats_Object((1,3,6,1,4,1,6141,2,60,8,1,10),_WwpLeosBroadcastContainmentBytesDroppedStats_Type())
wwpLeosBroadcastContainmentBytesDroppedStats.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosBroadcastContainmentBytesDroppedStats.setStatus(_A)
_WwpLeosBroadcastContainmentMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
wwpLeosBroadcastContainmentMIBNotificationPrefix=_WwpLeosBroadcastContainmentMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,6141,2,60,8,2))
_WwpLeosBroadcastContainmentMIBNotifications_ObjectIdentity=ObjectIdentity
wwpLeosBroadcastContainmentMIBNotifications=_WwpLeosBroadcastContainmentMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6141,2,60,8,2,1))
_WwpLeosBroadcastContainmentMIBConformance_ObjectIdentity=ObjectIdentity
wwpLeosBroadcastContainmentMIBConformance=_WwpLeosBroadcastContainmentMIBConformance_ObjectIdentity((1,3,6,1,4,1,6141,2,60,8,3))
_WwpLeosBroadcastContainmentMIBCompliances_ObjectIdentity=ObjectIdentity
wwpLeosBroadcastContainmentMIBCompliances=_WwpLeosBroadcastContainmentMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6141,2,60,8,3,1))
_WwpLeosBroadcastContainmentMIGroups_ObjectIdentity=ObjectIdentity
wwpLeosBroadcastContainmentMIGroups=_WwpLeosBroadcastContainmentMIGroups_ObjectIdentity((1,3,6,1,4,1,6141,2,60,8,3,2))
wwpLeosBcastThresholdExceed=NotificationType((1,3,6,1,4,1,6141,2,60,8,2,1,1))
wwpLeosBcastThresholdExceed.setObjects(*((_C,_F),(_C,_L)))
if mibBuilder.loadTexts:wwpLeosBcastThresholdExceed.setStatus(_A)
wwpLeosBcastThresholdNormal=NotificationType((1,3,6,1,4,1,6141,2,60,8,2,1,2))
wwpLeosBcastThresholdNormal.setObjects(*((_C,_F),(_C,_L)))
if mibBuilder.loadTexts:wwpLeosBcastThresholdNormal.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'WwpLeosBroadcastContainmentCapabilitiesMap':WwpLeosBroadcastContainmentCapabilitiesMap,'wwpLeosBroadcastContainmentMIB':wwpLeosBroadcastContainmentMIB,'wwpLeosBroadcastContainmentMIBObjects':wwpLeosBroadcastContainmentMIBObjects,'wwpLeosBroadcastContainmentCapability':wwpLeosBroadcastContainmentCapability,'wwpLeosBroadcastContainmentPktDroppedStats':wwpLeosBroadcastContainmentPktDroppedStats,'wwpLeosBroadcastContainmentFilterTable':wwpLeosBroadcastContainmentFilterTable,'wwpLeosBroadcastContainmentFilterEntry':wwpLeosBroadcastContainmentFilterEntry,_F:wwpLeosBroadcastContainmentIndex,_L:wwpLeosBroadcastContainmentFilterName,'wwpLeosBroadcastContainmentPktLimit':wwpLeosBroadcastContainmentPktLimit,'wwpLeosBroadcastContainmentPktDropState':wwpLeosBroadcastContainmentPktDropState,'wwpLeosBroadcastContainmentStatus':wwpLeosBroadcastContainmentStatus,'wwpLeosBroadcastContainmentKbps':wwpLeosBroadcastContainmentKbps,'wwpLeosBroadcastContainmentClassifier':wwpLeosBroadcastContainmentClassifier,'wwpLeosBroadcastContainmentFilterMemTable':wwpLeosBroadcastContainmentFilterMemTable,'wwpLeosBroadcastContainmentFilterMemEntry':wwpLeosBroadcastContainmentFilterMemEntry,_H:wwpLeosBroadcastContainmentVlanId,_I:wwpLeosBroadcastContainmentPortId,'wwpLeosBroadcastContainmentFilterMemStatus':wwpLeosBroadcastContainmentFilterMemStatus,'wwpLeosBroadcastContainmentGlobalStatus':wwpLeosBroadcastContainmentGlobalStatus,'wwpLeosBroadcastContainmentGlobalTime':wwpLeosBroadcastContainmentGlobalTime,'wwpLeosBroadcastContainmentIgnoreRapsMessages':wwpLeosBroadcastContainmentIgnoreRapsMessages,'wwpLeosBroadcastContainmentResourceMode':wwpLeosBroadcastContainmentResourceMode,'wwpLeosBroadcastContainmentBytesDroppedStats':wwpLeosBroadcastContainmentBytesDroppedStats,'wwpLeosBroadcastContainmentMIBNotificationPrefix':wwpLeosBroadcastContainmentMIBNotificationPrefix,'wwpLeosBroadcastContainmentMIBNotifications':wwpLeosBroadcastContainmentMIBNotifications,'wwpLeosBcastThresholdExceed':wwpLeosBcastThresholdExceed,'wwpLeosBcastThresholdNormal':wwpLeosBcastThresholdNormal,'wwpLeosBroadcastContainmentMIBConformance':wwpLeosBroadcastContainmentMIBConformance,'wwpLeosBroadcastContainmentMIBCompliances':wwpLeosBroadcastContainmentMIBCompliances,'wwpLeosBroadcastContainmentMIGroups':wwpLeosBroadcastContainmentMIGroups})