_l='fsvplsFwdFullAlarmCleared'
_k='fsvplsFwdFullAlarmRaised'
_j='fsvplsPwBindType'
_i='fsvplsPwBindConfigType'
_h='fsvplsStatusPeerCount'
_g='fsvplsStatusOperStatus'
_f='fsvplsConfigServiceType'
_e='fsvplsConfigMtu'
_d='fsvplsConfigIndexNext'
_c='fsvplsConfigRowStatus'
_b='fsvplsConfigMacAging'
_a='fsvplsConfigDiscardUnknownDest'
_Z='fsvplsConfigMacLearning'
_Y='fsvplsConfigAdminStatus'
_X='fsvplsConfigDescr'
_W='fsvplsConfigName'
_V='fsvplsIfBindIndex'
_U='fsvplsBgpRteTargetIndex'
_T='fsvplsPwBindIndex'
_S='autodiscovery'
_R='manual'
_Q='percentage'
_P='fsvplsNotificationGroup'
_O='fsvplsPwBindGroup'
_N='fsvplsGroup'
_M='not-accessible'
_L='SnmpAdminString'
_K='fsvplsConfigFwdFullLowWatermark'
_J='fsvplsConfigFwdFullHighWatermark'
_I='fsvplsConfigVpnId'
_H='TruthValue'
_G='Unsigned32'
_F='fsvplsConfigIndex'
_E='read-only'
_D='Integer32'
_C='read-create'
_B='FS-VPLS-GENERIC-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
PwIndexType,=mibBuilder.importSymbols('PW-TC-STD-MIB','PwIndexType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_L)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,transmission=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso','transmission')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','StorageType','TextualConvention',_H)
VPNIdOrZero,=mibBuilder.importSymbols('VPN-TC-STD-MIB','VPNIdOrZero')
fsvplsGenericDraft01MIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,77))
if mibBuilder.loadTexts:fsvplsGenericDraft01MIB.setRevisions(('2010-04-28 12:00','2010-06-04 12:00'))
class FSVplsBgpRouteDistinguisher(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
class FSVplsBgpRouteTarget(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
class FSVplsBgpRouteTargetType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('import',1),('export',2),('both',3)))
_FsvplsNotifications_ObjectIdentity=ObjectIdentity
fsvplsNotifications=_FsvplsNotifications_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,77,0))
_FsvplsObjects_ObjectIdentity=ObjectIdentity
fsvplsObjects=_FsvplsObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,77,1))
_FsvplsConfigIndexNext_Type=Unsigned32
_FsvplsConfigIndexNext_Object=MibScalar
fsvplsConfigIndexNext=_FsvplsConfigIndexNext_Object((1,3,6,1,4,1,52642,1,1,10,2,77,1,1),_FsvplsConfigIndexNext_Type())
fsvplsConfigIndexNext.setMaxAccess(_E)
if mibBuilder.loadTexts:fsvplsConfigIndexNext.setStatus(_A)
_FsvplsConfigTable_Object=MibTable
fsvplsConfigTable=_FsvplsConfigTable_Object((1,3,6,1,4,1,52642,1,1,10,2,77,1,2))
if mibBuilder.loadTexts:fsvplsConfigTable.setStatus(_A)
_FsvplsConfigEntry_Object=MibTableRow
fsvplsConfigEntry=_FsvplsConfigEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,77,1,2,1))
fsvplsConfigEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:fsvplsConfigEntry.setStatus(_A)
class _FsvplsConfigIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FsvplsConfigIndex_Type.__name__=_G
_FsvplsConfigIndex_Object=MibTableColumn
fsvplsConfigIndex=_FsvplsConfigIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,77,1,2,1,1),_FsvplsConfigIndex_Type())
fsvplsConfigIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:fsvplsConfigIndex.setStatus(_A)
class _FsvplsConfigName_Type(SnmpAdminString):defaultValue=OctetString('')
_FsvplsConfigName_Type.__name__=_L
_FsvplsConfigName_Object=MibTableColumn
fsvplsConfigName=_FsvplsConfigName_Object((1,3,6,1,4,1,52642,1,1,10,2,77,1,2,1,2),_FsvplsConfigName_Type())
fsvplsConfigName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsvplsConfigName.setStatus(_A)
class _FsvplsConfigDescr_Type(SnmpAdminString):defaultValue=OctetString('')
_FsvplsConfigDescr_Type.__name__=_L
_FsvplsConfigDescr_Object=MibTableColumn
fsvplsConfigDescr=_FsvplsConfigDescr_Object((1,3,6,1,4,1,52642,1,1,10,2,77,1,2,1,3),_FsvplsConfigDescr_Type())
fsvplsConfigDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:fsvplsConfigDescr.setStatus(_A)
class _FsvplsConfigAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),('testing',3)))
_FsvplsConfigAdminStatus_Type.__name__=_D
_FsvplsConfigAdminStatus_Object=MibTableColumn
fsvplsConfigAdminStatus=_FsvplsConfigAdminStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,77,1,2,1,4),_FsvplsConfigAdminStatus_Type())
fsvplsConfigAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:fsvplsConfigAdminStatus.setStatus(_A)
class _FsvplsConfigMacLearning_Type(TruthValue):defaultValue=1
_FsvplsConfigMacLearning_Type.__name__=_H
_FsvplsConfigMacLearning_Object=MibTableColumn
fsvplsConfigMacLearning=_FsvplsConfigMacLearning_Object((1,3,6,1,4,1,52642,1,1,10,2,77,1,2,1,5),_FsvplsConfigMacLearning_Type())
fsvplsConfigMacLearning.setMaxAccess(_C)
if mibBuilder.loadTexts:fsvplsConfigMacLearning.setStatus(_A)
class _FsvplsConfigDiscardUnknownDest_Type(TruthValue):defaultValue=2
_FsvplsConfigDiscardUnknownDest_Type.__name__=_H
_FsvplsConfigDiscardUnknownDest_Object=MibTableColumn
fsvplsConfigDiscardUnknownDest=_FsvplsConfigDiscardUnknownDest_Object((1,3,6,1,4,1,52642,1,1,10,2,77,1,2,1,6),_FsvplsConfigDiscardUnknownDest_Type())
fsvplsConfigDiscardUnknownDest.setMaxAccess(_C)
if mibBuilder.loadTexts:fsvplsConfigDiscardUnknownDest.setStatus(_A)
class _FsvplsConfigMacAging_Type(TruthValue):defaultValue=1
_FsvplsConfigMacAging_Type.__name__=_H
_FsvplsConfigMacAging_Object=MibTableColumn
fsvplsConfigMacAging=_FsvplsConfigMacAging_Object((1,3,6,1,4,1,52642,1,1,10,2,77,1,2,1,7),_FsvplsConfigMacAging_Type())
fsvplsConfigMacAging.setMaxAccess(_E)
if mibBuilder.loadTexts:fsvplsConfigMacAging.setStatus(_A)
class _FsvplsConfigFwdFullHighWatermark_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_FsvplsConfigFwdFullHighWatermark_Type.__name__=_G
_FsvplsConfigFwdFullHighWatermark_Object=MibTableColumn
fsvplsConfigFwdFullHighWatermark=_FsvplsConfigFwdFullHighWatermark_Object((1,3,6,1,4,1,52642,1,1,10,2,77,1,2,1,8),_FsvplsConfigFwdFullHighWatermark_Type())
fsvplsConfigFwdFullHighWatermark.setMaxAccess(_C)
if mibBuilder.loadTexts:fsvplsConfigFwdFullHighWatermark.setStatus(_A)
if mibBuilder.loadTexts:fsvplsConfigFwdFullHighWatermark.setUnits(_Q)
class _FsvplsConfigFwdFullLowWatermark_Type(Unsigned32):defaultValue=80;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_FsvplsConfigFwdFullLowWatermark_Type.__name__=_G
_FsvplsConfigFwdFullLowWatermark_Object=MibTableColumn
fsvplsConfigFwdFullLowWatermark=_FsvplsConfigFwdFullLowWatermark_Object((1,3,6,1,4,1,52642,1,1,10,2,77,1,2,1,9),_FsvplsConfigFwdFullLowWatermark_Type())
fsvplsConfigFwdFullLowWatermark.setMaxAccess(_C)
if mibBuilder.loadTexts:fsvplsConfigFwdFullLowWatermark.setStatus(_A)
if mibBuilder.loadTexts:fsvplsConfigFwdFullLowWatermark.setUnits(_Q)
_FsvplsConfigRowStatus_Type=RowStatus
_FsvplsConfigRowStatus_Object=MibTableColumn
fsvplsConfigRowStatus=_FsvplsConfigRowStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,77,1,2,1,10),_FsvplsConfigRowStatus_Type())
fsvplsConfigRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsvplsConfigRowStatus.setStatus(_A)
class _FsvplsConfigMtu_Type(Unsigned32):defaultValue=1500;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(46,1530))
_FsvplsConfigMtu_Type.__name__=_G
_FsvplsConfigMtu_Object=MibTableColumn
fsvplsConfigMtu=_FsvplsConfigMtu_Object((1,3,6,1,4,1,52642,1,1,10,2,77,1,2,1,11),_FsvplsConfigMtu_Type())
fsvplsConfigMtu.setMaxAccess(_C)
if mibBuilder.loadTexts:fsvplsConfigMtu.setStatus(_A)
_FsvplsConfigVpnId_Type=VPNIdOrZero
_FsvplsConfigVpnId_Object=MibTableColumn
fsvplsConfigVpnId=_FsvplsConfigVpnId_Object((1,3,6,1,4,1,52642,1,1,10,2,77,1,2,1,12),_FsvplsConfigVpnId_Type())
fsvplsConfigVpnId.setMaxAccess(_C)
if mibBuilder.loadTexts:fsvplsConfigVpnId.setStatus(_A)
class _FsvplsConfigServiceType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('vlan',1),('ethernet',2)))
_FsvplsConfigServiceType_Type.__name__=_D
_FsvplsConfigServiceType_Object=MibTableColumn
fsvplsConfigServiceType=_FsvplsConfigServiceType_Object((1,3,6,1,4,1,52642,1,1,10,2,77,1,2,1,13),_FsvplsConfigServiceType_Type())
fsvplsConfigServiceType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsvplsConfigServiceType.setStatus(_A)
class _FsvplsConfigServiceSignal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_S,2)))
_FsvplsConfigServiceSignal_Type.__name__=_D
_FsvplsConfigServiceSignal_Object=MibTableColumn
fsvplsConfigServiceSignal=_FsvplsConfigServiceSignal_Object((1,3,6,1,4,1,52642,1,1,10,2,77,1,2,1,14),_FsvplsConfigServiceSignal_Type())
fsvplsConfigServiceSignal.setMaxAccess(_C)
if mibBuilder.loadTexts:fsvplsConfigServiceSignal.setStatus(_A)
_FsvplsStatusTable_Object=MibTable
fsvplsStatusTable=_FsvplsStatusTable_Object((1,3,6,1,4,1,52642,1,1,10,2,77,1,3))
if mibBuilder.loadTexts:fsvplsStatusTable.setStatus(_A)
_FsvplsStatusEntry_Object=MibTableRow
fsvplsStatusEntry=_FsvplsStatusEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,77,1,3,1))
fsvplsStatusEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:fsvplsStatusEntry.setStatus(_A)
class _FsvplsStatusOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_FsvplsStatusOperStatus_Type.__name__=_D
_FsvplsStatusOperStatus_Object=MibTableColumn
fsvplsStatusOperStatus=_FsvplsStatusOperStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,77,1,3,1,1),_FsvplsStatusOperStatus_Type())
fsvplsStatusOperStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:fsvplsStatusOperStatus.setStatus(_A)
_FsvplsStatusPeerCount_Type=Counter32
_FsvplsStatusPeerCount_Object=MibTableColumn
fsvplsStatusPeerCount=_FsvplsStatusPeerCount_Object((1,3,6,1,4,1,52642,1,1,10,2,77,1,3,1,2),_FsvplsStatusPeerCount_Type())
fsvplsStatusPeerCount.setMaxAccess(_E)
if mibBuilder.loadTexts:fsvplsStatusPeerCount.setStatus(_A)
_FsvplsPwBindTable_Object=MibTable
fsvplsPwBindTable=_FsvplsPwBindTable_Object((1,3,6,1,4,1,52642,1,1,10,2,77,1,4))
if mibBuilder.loadTexts:fsvplsPwBindTable.setStatus(_A)
_FsvplsPwBindEntry_Object=MibTableRow
fsvplsPwBindEntry=_FsvplsPwBindEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,77,1,4,1))
fsvplsPwBindEntry.setIndexNames((0,_B,_F),(0,_B,_T))
if mibBuilder.loadTexts:fsvplsPwBindEntry.setStatus(_A)
_FsvplsPwBindIndex_Type=Unsigned32
_FsvplsPwBindIndex_Object=MibTableColumn
fsvplsPwBindIndex=_FsvplsPwBindIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,77,1,4,1,1),_FsvplsPwBindIndex_Type())
fsvplsPwBindIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:fsvplsPwBindIndex.setStatus(_A)
class _FsvplsPwBindConfigType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_S,2)))
_FsvplsPwBindConfigType_Type.__name__=_D
_FsvplsPwBindConfigType_Object=MibTableColumn
fsvplsPwBindConfigType=_FsvplsPwBindConfigType_Object((1,3,6,1,4,1,52642,1,1,10,2,77,1,4,1,2),_FsvplsPwBindConfigType_Type())
fsvplsPwBindConfigType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsvplsPwBindConfigType.setStatus(_A)
class _FsvplsPwBindType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('mesh',1),('spoke',2)))
_FsvplsPwBindType_Type.__name__=_D
_FsvplsPwBindType_Object=MibTableColumn
fsvplsPwBindType=_FsvplsPwBindType_Object((1,3,6,1,4,1,52642,1,1,10,2,77,1,4,1,3),_FsvplsPwBindType_Type())
fsvplsPwBindType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsvplsPwBindType.setStatus(_A)
_FsvplsBgpADConfigTable_Object=MibTable
fsvplsBgpADConfigTable=_FsvplsBgpADConfigTable_Object((1,3,6,1,4,1,52642,1,1,10,2,77,1,5))
if mibBuilder.loadTexts:fsvplsBgpADConfigTable.setStatus(_A)
_FsvplsBgpADConfigEntry_Object=MibTableRow
fsvplsBgpADConfigEntry=_FsvplsBgpADConfigEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,77,1,5,1))
fsvplsBgpADConfigEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:fsvplsBgpADConfigEntry.setStatus(_A)
_FsvplsBgpADConfigRouteDistinguisher_Type=FSVplsBgpRouteDistinguisher
_FsvplsBgpADConfigRouteDistinguisher_Object=MibTableColumn
fsvplsBgpADConfigRouteDistinguisher=_FsvplsBgpADConfigRouteDistinguisher_Object((1,3,6,1,4,1,52642,1,1,10,2,77,1,5,1,1),_FsvplsBgpADConfigRouteDistinguisher_Type())
fsvplsBgpADConfigRouteDistinguisher.setMaxAccess(_C)
if mibBuilder.loadTexts:fsvplsBgpADConfigRouteDistinguisher.setStatus(_A)
_FsvplsBgpADConfigRowStatus_Type=RowStatus
_FsvplsBgpADConfigRowStatus_Object=MibTableColumn
fsvplsBgpADConfigRowStatus=_FsvplsBgpADConfigRowStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,77,1,5,1,2),_FsvplsBgpADConfigRowStatus_Type())
fsvplsBgpADConfigRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsvplsBgpADConfigRowStatus.setStatus(_A)
_FsvplsBgpRteTargetTable_Object=MibTable
fsvplsBgpRteTargetTable=_FsvplsBgpRteTargetTable_Object((1,3,6,1,4,1,52642,1,1,10,2,77,1,6))
if mibBuilder.loadTexts:fsvplsBgpRteTargetTable.setStatus(_A)
_FsvplsBgpRteTargetEntry_Object=MibTableRow
fsvplsBgpRteTargetEntry=_FsvplsBgpRteTargetEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,77,1,6,1))
fsvplsBgpRteTargetEntry.setIndexNames((0,_B,_F),(0,_B,_U))
if mibBuilder.loadTexts:fsvplsBgpRteTargetEntry.setStatus(_A)
_FsvplsBgpRteTargetIndex_Type=Unsigned32
_FsvplsBgpRteTargetIndex_Object=MibTableColumn
fsvplsBgpRteTargetIndex=_FsvplsBgpRteTargetIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,77,1,6,1,1),_FsvplsBgpRteTargetIndex_Type())
fsvplsBgpRteTargetIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:fsvplsBgpRteTargetIndex.setStatus(_A)
_FsvplsBgpRteTargetRTType_Type=FSVplsBgpRouteTargetType
_FsvplsBgpRteTargetRTType_Object=MibTableColumn
fsvplsBgpRteTargetRTType=_FsvplsBgpRteTargetRTType_Object((1,3,6,1,4,1,52642,1,1,10,2,77,1,6,1,2),_FsvplsBgpRteTargetRTType_Type())
fsvplsBgpRteTargetRTType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsvplsBgpRteTargetRTType.setStatus(_A)
_FsvplsBgpRteTargetRT_Type=FSVplsBgpRouteTarget
_FsvplsBgpRteTargetRT_Object=MibTableColumn
fsvplsBgpRteTargetRT=_FsvplsBgpRteTargetRT_Object((1,3,6,1,4,1,52642,1,1,10,2,77,1,6,1,3),_FsvplsBgpRteTargetRT_Type())
fsvplsBgpRteTargetRT.setMaxAccess(_C)
if mibBuilder.loadTexts:fsvplsBgpRteTargetRT.setStatus(_A)
_FsvplsBgpRteTargetRTRowStatus_Type=RowStatus
_FsvplsBgpRteTargetRTRowStatus_Object=MibTableColumn
fsvplsBgpRteTargetRTRowStatus=_FsvplsBgpRteTargetRTRowStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,77,1,6,1,4),_FsvplsBgpRteTargetRTRowStatus_Type())
fsvplsBgpRteTargetRTRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsvplsBgpRteTargetRTRowStatus.setStatus(_A)
_FsvplsIfBindTable_Object=MibTable
fsvplsIfBindTable=_FsvplsIfBindTable_Object((1,3,6,1,4,1,52642,1,1,10,2,77,1,7))
if mibBuilder.loadTexts:fsvplsIfBindTable.setStatus(_A)
_FsVplsIfBindEntry_Object=MibTableRow
fsVplsIfBindEntry=_FsVplsIfBindEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,77,1,7,1))
fsVplsIfBindEntry.setIndexNames((0,_B,_F),(0,_B,_V))
if mibBuilder.loadTexts:fsVplsIfBindEntry.setStatus(_A)
_FsvplsIfBindIndex_Type=InterfaceIndexOrZero
_FsvplsIfBindIndex_Object=MibTableColumn
fsvplsIfBindIndex=_FsvplsIfBindIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,77,1,7,1,1),_FsvplsIfBindIndex_Type())
fsvplsIfBindIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsvplsIfBindIndex.setStatus(_A)
_FsvplsSiteId_Type=Unsigned32
_FsvplsSiteId_Object=MibTableColumn
fsvplsSiteId=_FsvplsSiteId_Object((1,3,6,1,4,1,52642,1,1,10,2,77,1,7,1,2),_FsvplsSiteId_Type())
fsvplsSiteId.setMaxAccess(_C)
if mibBuilder.loadTexts:fsvplsSiteId.setStatus(_A)
_FsvplsIfRowStatus_Type=RowStatus
_FsvplsIfRowStatus_Object=MibTableColumn
fsvplsIfRowStatus=_FsvplsIfRowStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,77,1,7,1,3),_FsvplsIfRowStatus_Type())
fsvplsIfRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsvplsIfRowStatus.setStatus(_A)
_FsvplsConformance_ObjectIdentity=ObjectIdentity
fsvplsConformance=_FsvplsConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,77,2))
_FsvplsCompliances_ObjectIdentity=ObjectIdentity
fsvplsCompliances=_FsvplsCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,77,2,1))
_FsvplsGroups_ObjectIdentity=ObjectIdentity
fsvplsGroups=_FsvplsGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,77,2,2))
fsvplsGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,77,2,2,1))
fsvplsGroup.setObjects(*((_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_I),(_B,_J),(_B,_K),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:fsvplsGroup.setStatus(_A)
fsvplsPwBindGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,77,2,2,2))
fsvplsPwBindGroup.setObjects(*((_B,_i),(_B,_j)))
if mibBuilder.loadTexts:fsvplsPwBindGroup.setStatus(_A)
fsvplsFwdFullAlarmRaised=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,77,0,1))
fsvplsFwdFullAlarmRaised.setObjects(*((_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:fsvplsFwdFullAlarmRaised.setStatus(_A)
fsvplsFwdFullAlarmCleared=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,77,0,2))
fsvplsFwdFullAlarmCleared.setObjects(*((_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:fsvplsFwdFullAlarmCleared.setStatus(_A)
fsvplsNotificationGroup=NotificationGroup((1,3,6,1,4,1,52642,1,1,10,2,77,2,2,3))
fsvplsNotificationGroup.setObjects(*((_B,_k),(_B,_l)))
if mibBuilder.loadTexts:fsvplsNotificationGroup.setStatus(_A)
fsvplsModuleFullCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,77,2,1,1))
fsvplsModuleFullCompliance.setObjects(*((_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:fsvplsModuleFullCompliance.setStatus(_A)
fsvplsModuleReadOnlyCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,77,2,1,2))
fsvplsModuleReadOnlyCompliance.setObjects(*((_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:fsvplsModuleReadOnlyCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'FSVplsBgpRouteDistinguisher':FSVplsBgpRouteDistinguisher,'FSVplsBgpRouteTarget':FSVplsBgpRouteTarget,'FSVplsBgpRouteTargetType':FSVplsBgpRouteTargetType,'fsvplsGenericDraft01MIB':fsvplsGenericDraft01MIB,'fsvplsNotifications':fsvplsNotifications,_k:fsvplsFwdFullAlarmRaised,_l:fsvplsFwdFullAlarmCleared,'fsvplsObjects':fsvplsObjects,_d:fsvplsConfigIndexNext,'fsvplsConfigTable':fsvplsConfigTable,'fsvplsConfigEntry':fsvplsConfigEntry,_F:fsvplsConfigIndex,_W:fsvplsConfigName,_X:fsvplsConfigDescr,_Y:fsvplsConfigAdminStatus,_Z:fsvplsConfigMacLearning,_a:fsvplsConfigDiscardUnknownDest,_b:fsvplsConfigMacAging,_J:fsvplsConfigFwdFullHighWatermark,_K:fsvplsConfigFwdFullLowWatermark,_c:fsvplsConfigRowStatus,_e:fsvplsConfigMtu,_I:fsvplsConfigVpnId,_f:fsvplsConfigServiceType,'fsvplsConfigServiceSignal':fsvplsConfigServiceSignal,'fsvplsStatusTable':fsvplsStatusTable,'fsvplsStatusEntry':fsvplsStatusEntry,_g:fsvplsStatusOperStatus,_h:fsvplsStatusPeerCount,'fsvplsPwBindTable':fsvplsPwBindTable,'fsvplsPwBindEntry':fsvplsPwBindEntry,_T:fsvplsPwBindIndex,_i:fsvplsPwBindConfigType,_j:fsvplsPwBindType,'fsvplsBgpADConfigTable':fsvplsBgpADConfigTable,'fsvplsBgpADConfigEntry':fsvplsBgpADConfigEntry,'fsvplsBgpADConfigRouteDistinguisher':fsvplsBgpADConfigRouteDistinguisher,'fsvplsBgpADConfigRowStatus':fsvplsBgpADConfigRowStatus,'fsvplsBgpRteTargetTable':fsvplsBgpRteTargetTable,'fsvplsBgpRteTargetEntry':fsvplsBgpRteTargetEntry,_U:fsvplsBgpRteTargetIndex,'fsvplsBgpRteTargetRTType':fsvplsBgpRteTargetRTType,'fsvplsBgpRteTargetRT':fsvplsBgpRteTargetRT,'fsvplsBgpRteTargetRTRowStatus':fsvplsBgpRteTargetRTRowStatus,'fsvplsIfBindTable':fsvplsIfBindTable,'fsVplsIfBindEntry':fsVplsIfBindEntry,_V:fsvplsIfBindIndex,'fsvplsSiteId':fsvplsSiteId,'fsvplsIfRowStatus':fsvplsIfRowStatus,'fsvplsConformance':fsvplsConformance,'fsvplsCompliances':fsvplsCompliances,'fsvplsModuleFullCompliance':fsvplsModuleFullCompliance,'fsvplsModuleReadOnlyCompliance':fsvplsModuleReadOnlyCompliance,'fsvplsGroups':fsvplsGroups,_N:fsvplsGroup,_O:fsvplsPwBindGroup,_P:fsvplsNotificationGroup})