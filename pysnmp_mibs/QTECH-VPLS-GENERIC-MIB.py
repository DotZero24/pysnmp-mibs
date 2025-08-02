_l='qtechvplsFwdFullAlarmCleared'
_k='qtechvplsFwdFullAlarmRaised'
_j='qtechvplsPwBindType'
_i='qtechvplsPwBindConfigType'
_h='qtechvplsStatusPeerCount'
_g='qtechvplsStatusOperStatus'
_f='qtechvplsConfigServiceType'
_e='qtechvplsConfigMtu'
_d='qtechvplsConfigIndexNext'
_c='qtechvplsConfigRowStatus'
_b='qtechvplsConfigMacAging'
_a='qtechvplsConfigDiscardUnknownDest'
_Z='qtechvplsConfigMacLearning'
_Y='qtechvplsConfigAdminStatus'
_X='qtechvplsConfigDescr'
_W='qtechvplsConfigName'
_V='qtechvplsIfBindIndex'
_U='qtechvplsBgpRteTargetIndex'
_T='qtechvplsPwBindIndex'
_S='autodiscovery'
_R='manual'
_Q='percentage'
_P='qtechvplsNotificationGroup'
_O='qtechvplsPwBindGroup'
_N='qtechvplsGroup'
_M='not-accessible'
_L='SnmpAdminString'
_K='qtechvplsConfigFwdFullLowWatermark'
_J='qtechvplsConfigFwdFullHighWatermark'
_I='qtechvplsConfigVpnId'
_H='TruthValue'
_G='Unsigned32'
_F='qtechvplsConfigIndex'
_E='read-only'
_D='Integer32'
_C='read-create'
_B='QTECH-VPLS-GENERIC-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
PwIndexType,=mibBuilder.importSymbols('PW-TC-STD-MIB','PwIndexType')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_L)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,transmission=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso','transmission')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','StorageType','TextualConvention',_H)
VPNIdOrZero,=mibBuilder.importSymbols('VPN-TC-STD-MIB','VPNIdOrZero')
qtechvplsGenericDraft01MIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,77))
if mibBuilder.loadTexts:qtechvplsGenericDraft01MIB.setRevisions(('2010-04-28 12:00','2010-06-04 12:00'))
class QtechVplsBgpRouteDistinguisher(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
class QtechVplsBgpRouteTarget(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
class QtechVplsBgpRouteTargetType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('import',1),('export',2),('both',3)))
_QtechvplsNotifications_ObjectIdentity=ObjectIdentity
qtechvplsNotifications=_QtechvplsNotifications_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,77,0))
_QtechvplsObjects_ObjectIdentity=ObjectIdentity
qtechvplsObjects=_QtechvplsObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,77,1))
_QtechvplsConfigIndexNext_Type=Unsigned32
_QtechvplsConfigIndexNext_Object=MibScalar
qtechvplsConfigIndexNext=_QtechvplsConfigIndexNext_Object((1,3,6,1,4,1,27514,1,1,10,2,77,1,1),_QtechvplsConfigIndexNext_Type())
qtechvplsConfigIndexNext.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechvplsConfigIndexNext.setStatus(_A)
_QtechvplsConfigTable_Object=MibTable
qtechvplsConfigTable=_QtechvplsConfigTable_Object((1,3,6,1,4,1,27514,1,1,10,2,77,1,2))
if mibBuilder.loadTexts:qtechvplsConfigTable.setStatus(_A)
_QtechvplsConfigEntry_Object=MibTableRow
qtechvplsConfigEntry=_QtechvplsConfigEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,77,1,2,1))
qtechvplsConfigEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:qtechvplsConfigEntry.setStatus(_A)
class _QtechvplsConfigIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_QtechvplsConfigIndex_Type.__name__=_G
_QtechvplsConfigIndex_Object=MibTableColumn
qtechvplsConfigIndex=_QtechvplsConfigIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,77,1,2,1,1),_QtechvplsConfigIndex_Type())
qtechvplsConfigIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:qtechvplsConfigIndex.setStatus(_A)
class _QtechvplsConfigName_Type(SnmpAdminString):defaultValue=OctetString('')
_QtechvplsConfigName_Type.__name__=_L
_QtechvplsConfigName_Object=MibTableColumn
qtechvplsConfigName=_QtechvplsConfigName_Object((1,3,6,1,4,1,27514,1,1,10,2,77,1,2,1,2),_QtechvplsConfigName_Type())
qtechvplsConfigName.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechvplsConfigName.setStatus(_A)
class _QtechvplsConfigDescr_Type(SnmpAdminString):defaultValue=OctetString('')
_QtechvplsConfigDescr_Type.__name__=_L
_QtechvplsConfigDescr_Object=MibTableColumn
qtechvplsConfigDescr=_QtechvplsConfigDescr_Object((1,3,6,1,4,1,27514,1,1,10,2,77,1,2,1,3),_QtechvplsConfigDescr_Type())
qtechvplsConfigDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechvplsConfigDescr.setStatus(_A)
class _QtechvplsConfigAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),('testing',3)))
_QtechvplsConfigAdminStatus_Type.__name__=_D
_QtechvplsConfigAdminStatus_Object=MibTableColumn
qtechvplsConfigAdminStatus=_QtechvplsConfigAdminStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,77,1,2,1,4),_QtechvplsConfigAdminStatus_Type())
qtechvplsConfigAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechvplsConfigAdminStatus.setStatus(_A)
class _QtechvplsConfigMacLearning_Type(TruthValue):defaultValue=1
_QtechvplsConfigMacLearning_Type.__name__=_H
_QtechvplsConfigMacLearning_Object=MibTableColumn
qtechvplsConfigMacLearning=_QtechvplsConfigMacLearning_Object((1,3,6,1,4,1,27514,1,1,10,2,77,1,2,1,5),_QtechvplsConfigMacLearning_Type())
qtechvplsConfigMacLearning.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechvplsConfigMacLearning.setStatus(_A)
class _QtechvplsConfigDiscardUnknownDest_Type(TruthValue):defaultValue=2
_QtechvplsConfigDiscardUnknownDest_Type.__name__=_H
_QtechvplsConfigDiscardUnknownDest_Object=MibTableColumn
qtechvplsConfigDiscardUnknownDest=_QtechvplsConfigDiscardUnknownDest_Object((1,3,6,1,4,1,27514,1,1,10,2,77,1,2,1,6),_QtechvplsConfigDiscardUnknownDest_Type())
qtechvplsConfigDiscardUnknownDest.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechvplsConfigDiscardUnknownDest.setStatus(_A)
class _QtechvplsConfigMacAging_Type(TruthValue):defaultValue=1
_QtechvplsConfigMacAging_Type.__name__=_H
_QtechvplsConfigMacAging_Object=MibTableColumn
qtechvplsConfigMacAging=_QtechvplsConfigMacAging_Object((1,3,6,1,4,1,27514,1,1,10,2,77,1,2,1,7),_QtechvplsConfigMacAging_Type())
qtechvplsConfigMacAging.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechvplsConfigMacAging.setStatus(_A)
class _QtechvplsConfigFwdFullHighWatermark_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_QtechvplsConfigFwdFullHighWatermark_Type.__name__=_G
_QtechvplsConfigFwdFullHighWatermark_Object=MibTableColumn
qtechvplsConfigFwdFullHighWatermark=_QtechvplsConfigFwdFullHighWatermark_Object((1,3,6,1,4,1,27514,1,1,10,2,77,1,2,1,8),_QtechvplsConfigFwdFullHighWatermark_Type())
qtechvplsConfigFwdFullHighWatermark.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechvplsConfigFwdFullHighWatermark.setStatus(_A)
if mibBuilder.loadTexts:qtechvplsConfigFwdFullHighWatermark.setUnits(_Q)
class _QtechvplsConfigFwdFullLowWatermark_Type(Unsigned32):defaultValue=80;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_QtechvplsConfigFwdFullLowWatermark_Type.__name__=_G
_QtechvplsConfigFwdFullLowWatermark_Object=MibTableColumn
qtechvplsConfigFwdFullLowWatermark=_QtechvplsConfigFwdFullLowWatermark_Object((1,3,6,1,4,1,27514,1,1,10,2,77,1,2,1,9),_QtechvplsConfigFwdFullLowWatermark_Type())
qtechvplsConfigFwdFullLowWatermark.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechvplsConfigFwdFullLowWatermark.setStatus(_A)
if mibBuilder.loadTexts:qtechvplsConfigFwdFullLowWatermark.setUnits(_Q)
_QtechvplsConfigRowStatus_Type=RowStatus
_QtechvplsConfigRowStatus_Object=MibTableColumn
qtechvplsConfigRowStatus=_QtechvplsConfigRowStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,77,1,2,1,10),_QtechvplsConfigRowStatus_Type())
qtechvplsConfigRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechvplsConfigRowStatus.setStatus(_A)
class _QtechvplsConfigMtu_Type(Unsigned32):defaultValue=1500;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(46,1530))
_QtechvplsConfigMtu_Type.__name__=_G
_QtechvplsConfigMtu_Object=MibTableColumn
qtechvplsConfigMtu=_QtechvplsConfigMtu_Object((1,3,6,1,4,1,27514,1,1,10,2,77,1,2,1,11),_QtechvplsConfigMtu_Type())
qtechvplsConfigMtu.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechvplsConfigMtu.setStatus(_A)
_QtechvplsConfigVpnId_Type=VPNIdOrZero
_QtechvplsConfigVpnId_Object=MibTableColumn
qtechvplsConfigVpnId=_QtechvplsConfigVpnId_Object((1,3,6,1,4,1,27514,1,1,10,2,77,1,2,1,12),_QtechvplsConfigVpnId_Type())
qtechvplsConfigVpnId.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechvplsConfigVpnId.setStatus(_A)
class _QtechvplsConfigServiceType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('vlan',1),('ethernet',2)))
_QtechvplsConfigServiceType_Type.__name__=_D
_QtechvplsConfigServiceType_Object=MibTableColumn
qtechvplsConfigServiceType=_QtechvplsConfigServiceType_Object((1,3,6,1,4,1,27514,1,1,10,2,77,1,2,1,13),_QtechvplsConfigServiceType_Type())
qtechvplsConfigServiceType.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechvplsConfigServiceType.setStatus(_A)
class _QtechvplsConfigServiceSignal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_S,2)))
_QtechvplsConfigServiceSignal_Type.__name__=_D
_QtechvplsConfigServiceSignal_Object=MibTableColumn
qtechvplsConfigServiceSignal=_QtechvplsConfigServiceSignal_Object((1,3,6,1,4,1,27514,1,1,10,2,77,1,2,1,14),_QtechvplsConfigServiceSignal_Type())
qtechvplsConfigServiceSignal.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechvplsConfigServiceSignal.setStatus(_A)
_QtechvplsStatusTable_Object=MibTable
qtechvplsStatusTable=_QtechvplsStatusTable_Object((1,3,6,1,4,1,27514,1,1,10,2,77,1,3))
if mibBuilder.loadTexts:qtechvplsStatusTable.setStatus(_A)
_QtechvplsStatusEntry_Object=MibTableRow
qtechvplsStatusEntry=_QtechvplsStatusEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,77,1,3,1))
qtechvplsStatusEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:qtechvplsStatusEntry.setStatus(_A)
class _QtechvplsStatusOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_QtechvplsStatusOperStatus_Type.__name__=_D
_QtechvplsStatusOperStatus_Object=MibTableColumn
qtechvplsStatusOperStatus=_QtechvplsStatusOperStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,77,1,3,1,1),_QtechvplsStatusOperStatus_Type())
qtechvplsStatusOperStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechvplsStatusOperStatus.setStatus(_A)
_QtechvplsStatusPeerCount_Type=Counter32
_QtechvplsStatusPeerCount_Object=MibTableColumn
qtechvplsStatusPeerCount=_QtechvplsStatusPeerCount_Object((1,3,6,1,4,1,27514,1,1,10,2,77,1,3,1,2),_QtechvplsStatusPeerCount_Type())
qtechvplsStatusPeerCount.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechvplsStatusPeerCount.setStatus(_A)
_QtechvplsPwBindTable_Object=MibTable
qtechvplsPwBindTable=_QtechvplsPwBindTable_Object((1,3,6,1,4,1,27514,1,1,10,2,77,1,4))
if mibBuilder.loadTexts:qtechvplsPwBindTable.setStatus(_A)
_QtechvplsPwBindEntry_Object=MibTableRow
qtechvplsPwBindEntry=_QtechvplsPwBindEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,77,1,4,1))
qtechvplsPwBindEntry.setIndexNames((0,_B,_F),(0,_B,_T))
if mibBuilder.loadTexts:qtechvplsPwBindEntry.setStatus(_A)
_QtechvplsPwBindIndex_Type=Unsigned32
_QtechvplsPwBindIndex_Object=MibTableColumn
qtechvplsPwBindIndex=_QtechvplsPwBindIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,77,1,4,1,1),_QtechvplsPwBindIndex_Type())
qtechvplsPwBindIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:qtechvplsPwBindIndex.setStatus(_A)
class _QtechvplsPwBindConfigType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_S,2)))
_QtechvplsPwBindConfigType_Type.__name__=_D
_QtechvplsPwBindConfigType_Object=MibTableColumn
qtechvplsPwBindConfigType=_QtechvplsPwBindConfigType_Object((1,3,6,1,4,1,27514,1,1,10,2,77,1,4,1,2),_QtechvplsPwBindConfigType_Type())
qtechvplsPwBindConfigType.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechvplsPwBindConfigType.setStatus(_A)
class _QtechvplsPwBindType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('mesh',1),('spoke',2)))
_QtechvplsPwBindType_Type.__name__=_D
_QtechvplsPwBindType_Object=MibTableColumn
qtechvplsPwBindType=_QtechvplsPwBindType_Object((1,3,6,1,4,1,27514,1,1,10,2,77,1,4,1,3),_QtechvplsPwBindType_Type())
qtechvplsPwBindType.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechvplsPwBindType.setStatus(_A)
_QtechvplsBgpADConfigTable_Object=MibTable
qtechvplsBgpADConfigTable=_QtechvplsBgpADConfigTable_Object((1,3,6,1,4,1,27514,1,1,10,2,77,1,5))
if mibBuilder.loadTexts:qtechvplsBgpADConfigTable.setStatus(_A)
_QtechvplsBgpADConfigEntry_Object=MibTableRow
qtechvplsBgpADConfigEntry=_QtechvplsBgpADConfigEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,77,1,5,1))
qtechvplsBgpADConfigEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:qtechvplsBgpADConfigEntry.setStatus(_A)
_QtechvplsBgpADConfigRouteDistinguisher_Type=QtechVplsBgpRouteDistinguisher
_QtechvplsBgpADConfigRouteDistinguisher_Object=MibTableColumn
qtechvplsBgpADConfigRouteDistinguisher=_QtechvplsBgpADConfigRouteDistinguisher_Object((1,3,6,1,4,1,27514,1,1,10,2,77,1,5,1,1),_QtechvplsBgpADConfigRouteDistinguisher_Type())
qtechvplsBgpADConfigRouteDistinguisher.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechvplsBgpADConfigRouteDistinguisher.setStatus(_A)
_QtechvplsBgpADConfigRowStatus_Type=RowStatus
_QtechvplsBgpADConfigRowStatus_Object=MibTableColumn
qtechvplsBgpADConfigRowStatus=_QtechvplsBgpADConfigRowStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,77,1,5,1,2),_QtechvplsBgpADConfigRowStatus_Type())
qtechvplsBgpADConfigRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechvplsBgpADConfigRowStatus.setStatus(_A)
_QtechvplsBgpRteTargetTable_Object=MibTable
qtechvplsBgpRteTargetTable=_QtechvplsBgpRteTargetTable_Object((1,3,6,1,4,1,27514,1,1,10,2,77,1,6))
if mibBuilder.loadTexts:qtechvplsBgpRteTargetTable.setStatus(_A)
_QtechvplsBgpRteTargetEntry_Object=MibTableRow
qtechvplsBgpRteTargetEntry=_QtechvplsBgpRteTargetEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,77,1,6,1))
qtechvplsBgpRteTargetEntry.setIndexNames((0,_B,_F),(0,_B,_U))
if mibBuilder.loadTexts:qtechvplsBgpRteTargetEntry.setStatus(_A)
_QtechvplsBgpRteTargetIndex_Type=Unsigned32
_QtechvplsBgpRteTargetIndex_Object=MibTableColumn
qtechvplsBgpRteTargetIndex=_QtechvplsBgpRteTargetIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,77,1,6,1,1),_QtechvplsBgpRteTargetIndex_Type())
qtechvplsBgpRteTargetIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:qtechvplsBgpRteTargetIndex.setStatus(_A)
_QtechvplsBgpRteTargetRTType_Type=QtechVplsBgpRouteTargetType
_QtechvplsBgpRteTargetRTType_Object=MibTableColumn
qtechvplsBgpRteTargetRTType=_QtechvplsBgpRteTargetRTType_Object((1,3,6,1,4,1,27514,1,1,10,2,77,1,6,1,2),_QtechvplsBgpRteTargetRTType_Type())
qtechvplsBgpRteTargetRTType.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechvplsBgpRteTargetRTType.setStatus(_A)
_QtechvplsBgpRteTargetRT_Type=QtechVplsBgpRouteTarget
_QtechvplsBgpRteTargetRT_Object=MibTableColumn
qtechvplsBgpRteTargetRT=_QtechvplsBgpRteTargetRT_Object((1,3,6,1,4,1,27514,1,1,10,2,77,1,6,1,3),_QtechvplsBgpRteTargetRT_Type())
qtechvplsBgpRteTargetRT.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechvplsBgpRteTargetRT.setStatus(_A)
_QtechvplsBgpRteTargetRTRowStatus_Type=RowStatus
_QtechvplsBgpRteTargetRTRowStatus_Object=MibTableColumn
qtechvplsBgpRteTargetRTRowStatus=_QtechvplsBgpRteTargetRTRowStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,77,1,6,1,4),_QtechvplsBgpRteTargetRTRowStatus_Type())
qtechvplsBgpRteTargetRTRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechvplsBgpRteTargetRTRowStatus.setStatus(_A)
_QtechvplsIfBindTable_Object=MibTable
qtechvplsIfBindTable=_QtechvplsIfBindTable_Object((1,3,6,1,4,1,27514,1,1,10,2,77,1,7))
if mibBuilder.loadTexts:qtechvplsIfBindTable.setStatus(_A)
_QtechVplsIfBindEntry_Object=MibTableRow
qtechVplsIfBindEntry=_QtechVplsIfBindEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,77,1,7,1))
qtechVplsIfBindEntry.setIndexNames((0,_B,_F),(0,_B,_V))
if mibBuilder.loadTexts:qtechVplsIfBindEntry.setStatus(_A)
_QtechvplsIfBindIndex_Type=InterfaceIndexOrZero
_QtechvplsIfBindIndex_Object=MibTableColumn
qtechvplsIfBindIndex=_QtechvplsIfBindIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,77,1,7,1,1),_QtechvplsIfBindIndex_Type())
qtechvplsIfBindIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechvplsIfBindIndex.setStatus(_A)
_QtechvplsSiteId_Type=Unsigned32
_QtechvplsSiteId_Object=MibTableColumn
qtechvplsSiteId=_QtechvplsSiteId_Object((1,3,6,1,4,1,27514,1,1,10,2,77,1,7,1,2),_QtechvplsSiteId_Type())
qtechvplsSiteId.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechvplsSiteId.setStatus(_A)
_QtechvplsIfRowStatus_Type=RowStatus
_QtechvplsIfRowStatus_Object=MibTableColumn
qtechvplsIfRowStatus=_QtechvplsIfRowStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,77,1,7,1,3),_QtechvplsIfRowStatus_Type())
qtechvplsIfRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechvplsIfRowStatus.setStatus(_A)
_QtechvplsConformance_ObjectIdentity=ObjectIdentity
qtechvplsConformance=_QtechvplsConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,77,2))
_QtechvplsCompliances_ObjectIdentity=ObjectIdentity
qtechvplsCompliances=_QtechvplsCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,77,2,1))
_QtechvplsGroups_ObjectIdentity=ObjectIdentity
qtechvplsGroups=_QtechvplsGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,77,2,2))
qtechvplsGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,77,2,2,1))
qtechvplsGroup.setObjects(*((_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_I),(_B,_J),(_B,_K),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:qtechvplsGroup.setStatus(_A)
qtechvplsPwBindGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,77,2,2,2))
qtechvplsPwBindGroup.setObjects(*((_B,_i),(_B,_j)))
if mibBuilder.loadTexts:qtechvplsPwBindGroup.setStatus(_A)
qtechvplsFwdFullAlarmRaised=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,77,0,1))
qtechvplsFwdFullAlarmRaised.setObjects(*((_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:qtechvplsFwdFullAlarmRaised.setStatus(_A)
qtechvplsFwdFullAlarmCleared=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,77,0,2))
qtechvplsFwdFullAlarmCleared.setObjects(*((_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:qtechvplsFwdFullAlarmCleared.setStatus(_A)
qtechvplsNotificationGroup=NotificationGroup((1,3,6,1,4,1,27514,1,1,10,2,77,2,2,3))
qtechvplsNotificationGroup.setObjects(*((_B,_k),(_B,_l)))
if mibBuilder.loadTexts:qtechvplsNotificationGroup.setStatus(_A)
qtechvplsModuleFullCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,77,2,1,1))
qtechvplsModuleFullCompliance.setObjects(*((_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:qtechvplsModuleFullCompliance.setStatus(_A)
qtechvplsModuleReadOnlyCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,77,2,1,2))
qtechvplsModuleReadOnlyCompliance.setObjects(*((_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:qtechvplsModuleReadOnlyCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'QtechVplsBgpRouteDistinguisher':QtechVplsBgpRouteDistinguisher,'QtechVplsBgpRouteTarget':QtechVplsBgpRouteTarget,'QtechVplsBgpRouteTargetType':QtechVplsBgpRouteTargetType,'qtechvplsGenericDraft01MIB':qtechvplsGenericDraft01MIB,'qtechvplsNotifications':qtechvplsNotifications,_k:qtechvplsFwdFullAlarmRaised,_l:qtechvplsFwdFullAlarmCleared,'qtechvplsObjects':qtechvplsObjects,_d:qtechvplsConfigIndexNext,'qtechvplsConfigTable':qtechvplsConfigTable,'qtechvplsConfigEntry':qtechvplsConfigEntry,_F:qtechvplsConfigIndex,_W:qtechvplsConfigName,_X:qtechvplsConfigDescr,_Y:qtechvplsConfigAdminStatus,_Z:qtechvplsConfigMacLearning,_a:qtechvplsConfigDiscardUnknownDest,_b:qtechvplsConfigMacAging,_J:qtechvplsConfigFwdFullHighWatermark,_K:qtechvplsConfigFwdFullLowWatermark,_c:qtechvplsConfigRowStatus,_e:qtechvplsConfigMtu,_I:qtechvplsConfigVpnId,_f:qtechvplsConfigServiceType,'qtechvplsConfigServiceSignal':qtechvplsConfigServiceSignal,'qtechvplsStatusTable':qtechvplsStatusTable,'qtechvplsStatusEntry':qtechvplsStatusEntry,_g:qtechvplsStatusOperStatus,_h:qtechvplsStatusPeerCount,'qtechvplsPwBindTable':qtechvplsPwBindTable,'qtechvplsPwBindEntry':qtechvplsPwBindEntry,_T:qtechvplsPwBindIndex,_i:qtechvplsPwBindConfigType,_j:qtechvplsPwBindType,'qtechvplsBgpADConfigTable':qtechvplsBgpADConfigTable,'qtechvplsBgpADConfigEntry':qtechvplsBgpADConfigEntry,'qtechvplsBgpADConfigRouteDistinguisher':qtechvplsBgpADConfigRouteDistinguisher,'qtechvplsBgpADConfigRowStatus':qtechvplsBgpADConfigRowStatus,'qtechvplsBgpRteTargetTable':qtechvplsBgpRteTargetTable,'qtechvplsBgpRteTargetEntry':qtechvplsBgpRteTargetEntry,_U:qtechvplsBgpRteTargetIndex,'qtechvplsBgpRteTargetRTType':qtechvplsBgpRteTargetRTType,'qtechvplsBgpRteTargetRT':qtechvplsBgpRteTargetRT,'qtechvplsBgpRteTargetRTRowStatus':qtechvplsBgpRteTargetRTRowStatus,'qtechvplsIfBindTable':qtechvplsIfBindTable,'qtechVplsIfBindEntry':qtechVplsIfBindEntry,_V:qtechvplsIfBindIndex,'qtechvplsSiteId':qtechvplsSiteId,'qtechvplsIfRowStatus':qtechvplsIfRowStatus,'qtechvplsConformance':qtechvplsConformance,'qtechvplsCompliances':qtechvplsCompliances,'qtechvplsModuleFullCompliance':qtechvplsModuleFullCompliance,'qtechvplsModuleReadOnlyCompliance':qtechvplsModuleReadOnlyCompliance,'qtechvplsGroups':qtechvplsGroups,_N:qtechvplsGroup,_O:qtechvplsPwBindGroup,_P:qtechvplsNotificationGroup})