_X='sleMplsTpVplsMacLearningInfoMacAddress'
_W='sleMplsTpVplsSpokeCfgInfoVcName'
_V='reverse'
_U='forward'
_T='l2tpControlProtocol'
_S='genFecSignaling'
_R='pwIdFecSignaling'
_Q='manual'
_P='replace'
_O='remove'
_N='noOperation'
_M='Unsigned32'
_L='sleMplsTpVplsMeshCfgInfoPeerNodeId'
_K='sleMplsTpVplsIfCfgInfoIfIndex'
_J='sleMplsTpVplsIfCfgInfoName'
_I='none'
_H='IANAPwTypeTC'
_G='not-accessible'
_F='sleMplsTpVplsCfgInfoId'
_E='SLE-MPLS-TP-VPLS-MIB'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
sleMgmt,=mibBuilder.importSymbols('DASAN-SMI','sleMgmt')
IANAPwTypeTC,=mibBuilder.importSymbols('IANA-PWE3-MIB',_H)
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
MplsCcId,MplsIccId=mibBuilder.importSymbols('MPLS-TC-EXT-STD-MIB','MplsCcId','MplsIccId')
MplsLabel,=mibBuilder.importSymbols('MPLS-TC-STD-MIB','MplsLabel')
VlanIdOrAnyOrNone,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanIdOrAnyOrNone')
SleControlRequestResultType,SleControlStatusType=mibBuilder.importSymbols('SLE-TC-MIB','SleControlRequestResultType','SleControlStatusType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,transmission=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_M,'iso','transmission')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
sleMplsTpVpls=ModuleIdentity((1,3,6,1,4,1,6296,101,16,16))
if mibBuilder.loadTexts:sleMplsTpVpls.setRevisions(('2015-11-03 00:00',))
_SleMpls_ObjectIdentity=ObjectIdentity
sleMpls=_SleMpls_ObjectIdentity((1,3,6,1,4,1,6296,101,16))
if mibBuilder.loadTexts:sleMpls.setStatus(_A)
_SleMplsTpVplsCfg_ObjectIdentity=ObjectIdentity
sleMplsTpVplsCfg=_SleMplsTpVplsCfg_ObjectIdentity((1,3,6,1,4,1,6296,101,16,16,1))
_SleMplsTpVplsCfgInfoTable_Object=MibTable
sleMplsTpVplsCfgInfoTable=_SleMplsTpVplsCfgInfoTable_Object((1,3,6,1,4,1,6296,101,16,16,1,1))
if mibBuilder.loadTexts:sleMplsTpVplsCfgInfoTable.setStatus(_A)
_SleMplsTpVplsCfgInfoEntry_Object=MibTableRow
sleMplsTpVplsCfgInfoEntry=_SleMplsTpVplsCfgInfoEntry_Object((1,3,6,1,4,1,6296,101,16,16,1,1,1))
sleMplsTpVplsCfgInfoEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:sleMplsTpVplsCfgInfoEntry.setStatus(_A)
class _SleMplsTpVplsCfgInfoId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SleMplsTpVplsCfgInfoId_Type.__name__=_M
_SleMplsTpVplsCfgInfoId_Object=MibTableColumn
sleMplsTpVplsCfgInfoId=_SleMplsTpVplsCfgInfoId_Object((1,3,6,1,4,1,6296,101,16,16,1,1,1,1),_SleMplsTpVplsCfgInfoId_Type())
sleMplsTpVplsCfgInfoId.setMaxAccess(_G)
if mibBuilder.loadTexts:sleMplsTpVplsCfgInfoId.setStatus(_A)
_SleMplsTpVplsCfgInfoName_Type=OctetString
_SleMplsTpVplsCfgInfoName_Object=MibTableColumn
sleMplsTpVplsCfgInfoName=_SleMplsTpVplsCfgInfoName_Object((1,3,6,1,4,1,6296,101,16,16,1,1,1,2),_SleMplsTpVplsCfgInfoName_Type())
sleMplsTpVplsCfgInfoName.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpVplsCfgInfoName.setStatus(_A)
class _SleMplsTpVplsCfgInfoMacLearning_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_SleMplsTpVplsCfgInfoMacLearning_Type.__name__=_D
_SleMplsTpVplsCfgInfoMacLearning_Object=MibTableColumn
sleMplsTpVplsCfgInfoMacLearning=_SleMplsTpVplsCfgInfoMacLearning_Object((1,3,6,1,4,1,6296,101,16,16,1,1,1,3),_SleMplsTpVplsCfgInfoMacLearning_Type())
sleMplsTpVplsCfgInfoMacLearning.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpVplsCfgInfoMacLearning.setStatus(_A)
_SleMplsTpVplsCfgInfoMacLearningLimit_Type=Integer32
_SleMplsTpVplsCfgInfoMacLearningLimit_Object=MibTableColumn
sleMplsTpVplsCfgInfoMacLearningLimit=_SleMplsTpVplsCfgInfoMacLearningLimit_Object((1,3,6,1,4,1,6296,101,16,16,1,1,1,4),_SleMplsTpVplsCfgInfoMacLearningLimit_Type())
sleMplsTpVplsCfgInfoMacLearningLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpVplsCfgInfoMacLearningLimit.setStatus(_A)
class _SleMplsTpVplsCfgInfoServiceType_Type(IANAPwTypeTC):defaultValue=5
_SleMplsTpVplsCfgInfoServiceType_Type.__name__=_H
_SleMplsTpVplsCfgInfoServiceType_Object=MibTableColumn
sleMplsTpVplsCfgInfoServiceType=_SleMplsTpVplsCfgInfoServiceType_Object((1,3,6,1,4,1,6296,101,16,16,1,1,1,5),_SleMplsTpVplsCfgInfoServiceType_Type())
sleMplsTpVplsCfgInfoServiceType.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpVplsCfgInfoServiceType.setStatus(_A)
class _SleMplsTpVplsCfgInfoSignallingProto_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_I,0),('static',1),('bgp',2),('ldp',3),('bgpAdLdp',4)))
_SleMplsTpVplsCfgInfoSignallingProto_Type.__name__=_D
_SleMplsTpVplsCfgInfoSignallingProto_Object=MibTableColumn
sleMplsTpVplsCfgInfoSignallingProto=_SleMplsTpVplsCfgInfoSignallingProto_Object((1,3,6,1,4,1,6296,101,16,16,1,1,1,6),_SleMplsTpVplsCfgInfoSignallingProto_Type())
sleMplsTpVplsCfgInfoSignallingProto.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpVplsCfgInfoSignallingProto.setStatus(_A)
_SleMplsTpVplsCfgInfoGroupId_Type=Unsigned32
_SleMplsTpVplsCfgInfoGroupId_Object=MibTableColumn
sleMplsTpVplsCfgInfoGroupId=_SleMplsTpVplsCfgInfoGroupId_Object((1,3,6,1,4,1,6296,101,16,16,1,1,1,7),_SleMplsTpVplsCfgInfoGroupId_Type())
sleMplsTpVplsCfgInfoGroupId.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpVplsCfgInfoGroupId.setStatus(_A)
_SleMplsTpVplsCfgInfoDescription_Type=SnmpAdminString
_SleMplsTpVplsCfgInfoDescription_Object=MibTableColumn
sleMplsTpVplsCfgInfoDescription=_SleMplsTpVplsCfgInfoDescription_Object((1,3,6,1,4,1,6296,101,16,16,1,1,1,8),_SleMplsTpVplsCfgInfoDescription_Type())
sleMplsTpVplsCfgInfoDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpVplsCfgInfoDescription.setStatus(_A)
class _SleMplsTpVplsCfgInfoMtu_Type(Integer32):defaultValue=1500
_SleMplsTpVplsCfgInfoMtu_Type.__name__=_D
_SleMplsTpVplsCfgInfoMtu_Object=MibTableColumn
sleMplsTpVplsCfgInfoMtu=_SleMplsTpVplsCfgInfoMtu_Object((1,3,6,1,4,1,6296,101,16,16,1,1,1,9),_SleMplsTpVplsCfgInfoMtu_Type())
sleMplsTpVplsCfgInfoMtu.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpVplsCfgInfoMtu.setStatus(_A)
_SleMplsTpVplsCfgControl_ObjectIdentity=ObjectIdentity
sleMplsTpVplsCfgControl=_SleMplsTpVplsCfgControl_ObjectIdentity((1,3,6,1,4,1,6296,101,16,16,1,2))
class _SleMplsTpVplsCfgControlRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*(('createVpls',1),('deleteVpls',2),('setVplsMACLearningDisable',3),('setVplsMACLearningLimit',4),('setVplsACGroup',5),('setVplsDescription',6),('setVplsMtu',7),('setVplsServiceType',8),('unsetVplsMACLearningDisable',9),('unsetVplsMACLearningLimit',10),('unsetVplsACGroup',11),('unsetVplsDesc',12),('unsetVplsMtu',13),('unsetVplsServiceType',14)))
_SleMplsTpVplsCfgControlRequest_Type.__name__=_D
_SleMplsTpVplsCfgControlRequest_Object=MibScalar
sleMplsTpVplsCfgControlRequest=_SleMplsTpVplsCfgControlRequest_Object((1,3,6,1,4,1,6296,101,16,16,1,2,1),_SleMplsTpVplsCfgControlRequest_Type())
sleMplsTpVplsCfgControlRequest.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpVplsCfgControlRequest.setStatus(_A)
_SleMplsTpVplsCfgControlStatus_Type=SleControlStatusType
_SleMplsTpVplsCfgControlStatus_Object=MibScalar
sleMplsTpVplsCfgControlStatus=_SleMplsTpVplsCfgControlStatus_Object((1,3,6,1,4,1,6296,101,16,16,1,2,2),_SleMplsTpVplsCfgControlStatus_Type())
sleMplsTpVplsCfgControlStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpVplsCfgControlStatus.setStatus(_A)
_SleMplsTpVplsCfgControlTimer_Type=Gauge32
_SleMplsTpVplsCfgControlTimer_Object=MibScalar
sleMplsTpVplsCfgControlTimer=_SleMplsTpVplsCfgControlTimer_Object((1,3,6,1,4,1,6296,101,16,16,1,2,3),_SleMplsTpVplsCfgControlTimer_Type())
sleMplsTpVplsCfgControlTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpVplsCfgControlTimer.setStatus(_A)
_SleMplsTpVplsCfgControlTimestamp_Type=TimeTicks
_SleMplsTpVplsCfgControlTimestamp_Object=MibScalar
sleMplsTpVplsCfgControlTimestamp=_SleMplsTpVplsCfgControlTimestamp_Object((1,3,6,1,4,1,6296,101,16,16,1,2,4),_SleMplsTpVplsCfgControlTimestamp_Type())
sleMplsTpVplsCfgControlTimestamp.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpVplsCfgControlTimestamp.setStatus(_A)
_SleMplsTpVplsCfgControlReqResult_Type=SleControlRequestResultType
_SleMplsTpVplsCfgControlReqResult_Object=MibScalar
sleMplsTpVplsCfgControlReqResult=_SleMplsTpVplsCfgControlReqResult_Object((1,3,6,1,4,1,6296,101,16,16,1,2,5),_SleMplsTpVplsCfgControlReqResult_Type())
sleMplsTpVplsCfgControlReqResult.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpVplsCfgControlReqResult.setStatus(_A)
_SleMplsTpVplsCfgControlId_Type=Unsigned32
_SleMplsTpVplsCfgControlId_Object=MibScalar
sleMplsTpVplsCfgControlId=_SleMplsTpVplsCfgControlId_Object((1,3,6,1,4,1,6296,101,16,16,1,2,6),_SleMplsTpVplsCfgControlId_Type())
sleMplsTpVplsCfgControlId.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpVplsCfgControlId.setStatus(_A)
_SleMplsTpVplsCfgControlName_Type=OctetString
_SleMplsTpVplsCfgControlName_Object=MibScalar
sleMplsTpVplsCfgControlName=_SleMplsTpVplsCfgControlName_Object((1,3,6,1,4,1,6296,101,16,16,1,2,7),_SleMplsTpVplsCfgControlName_Type())
sleMplsTpVplsCfgControlName.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpVplsCfgControlName.setStatus(_A)
_SleMplsTpVplsCfgControlMacLearningLimit_Type=Integer32
_SleMplsTpVplsCfgControlMacLearningLimit_Object=MibScalar
sleMplsTpVplsCfgControlMacLearningLimit=_SleMplsTpVplsCfgControlMacLearningLimit_Object((1,3,6,1,4,1,6296,101,16,16,1,2,8),_SleMplsTpVplsCfgControlMacLearningLimit_Type())
sleMplsTpVplsCfgControlMacLearningLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpVplsCfgControlMacLearningLimit.setStatus(_A)
class _SleMplsTpVplsCfgControlServiceType_Type(IANAPwTypeTC):defaultValue=5
_SleMplsTpVplsCfgControlServiceType_Type.__name__=_H
_SleMplsTpVplsCfgControlServiceType_Object=MibScalar
sleMplsTpVplsCfgControlServiceType=_SleMplsTpVplsCfgControlServiceType_Object((1,3,6,1,4,1,6296,101,16,16,1,2,9),_SleMplsTpVplsCfgControlServiceType_Type())
sleMplsTpVplsCfgControlServiceType.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpVplsCfgControlServiceType.setStatus(_A)
_SleMplsTpVplsCfgControlGroupId_Type=Unsigned32
_SleMplsTpVplsCfgControlGroupId_Object=MibScalar
sleMplsTpVplsCfgControlGroupId=_SleMplsTpVplsCfgControlGroupId_Object((1,3,6,1,4,1,6296,101,16,16,1,2,10),_SleMplsTpVplsCfgControlGroupId_Type())
sleMplsTpVplsCfgControlGroupId.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpVplsCfgControlGroupId.setStatus(_A)
_SleMplsTpVplsCfgControlDescription_Type=SnmpAdminString
_SleMplsTpVplsCfgControlDescription_Object=MibScalar
sleMplsTpVplsCfgControlDescription=_SleMplsTpVplsCfgControlDescription_Object((1,3,6,1,4,1,6296,101,16,16,1,2,11),_SleMplsTpVplsCfgControlDescription_Type())
sleMplsTpVplsCfgControlDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpVplsCfgControlDescription.setStatus(_A)
class _SleMplsTpVplsCfgControlMtu_Type(Integer32):defaultValue=1500
_SleMplsTpVplsCfgControlMtu_Type.__name__=_D
_SleMplsTpVplsCfgControlMtu_Object=MibScalar
sleMplsTpVplsCfgControlMtu=_SleMplsTpVplsCfgControlMtu_Object((1,3,6,1,4,1,6296,101,16,16,1,2,12),_SleMplsTpVplsCfgControlMtu_Type())
sleMplsTpVplsCfgControlMtu.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpVplsCfgControlMtu.setStatus(_A)
_SleMplsTpVplsIfCfg_ObjectIdentity=ObjectIdentity
sleMplsTpVplsIfCfg=_SleMplsTpVplsIfCfg_ObjectIdentity((1,3,6,1,4,1,6296,101,16,16,2))
_SleMplsTpVplsIfCfgInfoTable_Object=MibTable
sleMplsTpVplsIfCfgInfoTable=_SleMplsTpVplsIfCfgInfoTable_Object((1,3,6,1,4,1,6296,101,16,16,2,1))
if mibBuilder.loadTexts:sleMplsTpVplsIfCfgInfoTable.setStatus(_A)
_SleMplsTpVplsIfCfgInfoEntry_Object=MibTableRow
sleMplsTpVplsIfCfgInfoEntry=_SleMplsTpVplsIfCfgInfoEntry_Object((1,3,6,1,4,1,6296,101,16,16,2,1,1))
sleMplsTpVplsIfCfgInfoEntry.setIndexNames((0,_E,_J),(0,_E,_K))
if mibBuilder.loadTexts:sleMplsTpVplsIfCfgInfoEntry.setStatus(_A)
_SleMplsTpVplsIfCfgInfoIfIndex_Type=InterfaceIndexOrZero
_SleMplsTpVplsIfCfgInfoIfIndex_Object=MibTableColumn
sleMplsTpVplsIfCfgInfoIfIndex=_SleMplsTpVplsIfCfgInfoIfIndex_Object((1,3,6,1,4,1,6296,101,16,16,2,1,1,1),_SleMplsTpVplsIfCfgInfoIfIndex_Type())
sleMplsTpVplsIfCfgInfoIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:sleMplsTpVplsIfCfgInfoIfIndex.setStatus(_A)
_SleMplsTpVplsIfCfgInfoName_Type=OctetString
_SleMplsTpVplsIfCfgInfoName_Object=MibTableColumn
sleMplsTpVplsIfCfgInfoName=_SleMplsTpVplsIfCfgInfoName_Object((1,3,6,1,4,1,6296,101,16,16,2,1,1,2),_SleMplsTpVplsIfCfgInfoName_Type())
sleMplsTpVplsIfCfgInfoName.setMaxAccess(_G)
if mibBuilder.loadTexts:sleMplsTpVplsIfCfgInfoName.setStatus(_A)
_SleMplsTpVplsIfCfgInfoServiceType_Type=IANAPwTypeTC
_SleMplsTpVplsIfCfgInfoServiceType_Object=MibTableColumn
sleMplsTpVplsIfCfgInfoServiceType=_SleMplsTpVplsIfCfgInfoServiceType_Object((1,3,6,1,4,1,6296,101,16,16,2,1,1,3),_SleMplsTpVplsIfCfgInfoServiceType_Type())
sleMplsTpVplsIfCfgInfoServiceType.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpVplsIfCfgInfoServiceType.setStatus(_A)
_SleMplsTpVplsIfCfgInfoVlanId_Type=VlanIdOrAnyOrNone
_SleMplsTpVplsIfCfgInfoVlanId_Object=MibTableColumn
sleMplsTpVplsIfCfgInfoVlanId=_SleMplsTpVplsIfCfgInfoVlanId_Object((1,3,6,1,4,1,6296,101,16,16,2,1,1,4),_SleMplsTpVplsIfCfgInfoVlanId_Type())
sleMplsTpVplsIfCfgInfoVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpVplsIfCfgInfoVlanId.setStatus(_A)
_SleMplsTpVplsIfCfgInfoInnerVlanId_Type=VlanIdOrAnyOrNone
_SleMplsTpVplsIfCfgInfoInnerVlanId_Object=MibTableColumn
sleMplsTpVplsIfCfgInfoInnerVlanId=_SleMplsTpVplsIfCfgInfoInnerVlanId_Object((1,3,6,1,4,1,6296,101,16,16,2,1,1,5),_SleMplsTpVplsIfCfgInfoInnerVlanId_Type())
sleMplsTpVplsIfCfgInfoInnerVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpVplsIfCfgInfoInnerVlanId.setStatus(_A)
class _SleMplsTpVplsIfCfgInfoAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_I,0),(_N,1),('add',2),(_O,3),(_P,4)))
_SleMplsTpVplsIfCfgInfoAction_Type.__name__=_D
_SleMplsTpVplsIfCfgInfoAction_Object=MibTableColumn
sleMplsTpVplsIfCfgInfoAction=_SleMplsTpVplsIfCfgInfoAction_Object((1,3,6,1,4,1,6296,101,16,16,2,1,1,6),_SleMplsTpVplsIfCfgInfoAction_Type())
sleMplsTpVplsIfCfgInfoAction.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpVplsIfCfgInfoAction.setStatus(_A)
_SleMplsTpVplsIfCfgControl_ObjectIdentity=ObjectIdentity
sleMplsTpVplsIfCfgControl=_SleMplsTpVplsIfCfgControl_ObjectIdentity((1,3,6,1,4,1,6296,101,16,16,2,2))
class _SleMplsTpVplsIfCfgControlRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('setBindVplsUntaggedMode',1),('setBindVplsSvlan',2),('setBindVplsTaggedMode',3),('setBindVplsQinQ',4),('setBindVplsQinQWithAction',5),('unsetbindvplsUnTaggedMode',6),('unsetBindVplsTaggedMode',7)))
_SleMplsTpVplsIfCfgControlRequest_Type.__name__=_D
_SleMplsTpVplsIfCfgControlRequest_Object=MibScalar
sleMplsTpVplsIfCfgControlRequest=_SleMplsTpVplsIfCfgControlRequest_Object((1,3,6,1,4,1,6296,101,16,16,2,2,1),_SleMplsTpVplsIfCfgControlRequest_Type())
sleMplsTpVplsIfCfgControlRequest.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpVplsIfCfgControlRequest.setStatus(_A)
_SleMplsTpVplsIfCfgControlStatus_Type=SleControlStatusType
_SleMplsTpVplsIfCfgControlStatus_Object=MibScalar
sleMplsTpVplsIfCfgControlStatus=_SleMplsTpVplsIfCfgControlStatus_Object((1,3,6,1,4,1,6296,101,16,16,2,2,2),_SleMplsTpVplsIfCfgControlStatus_Type())
sleMplsTpVplsIfCfgControlStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpVplsIfCfgControlStatus.setStatus(_A)
_SleMplsTpVplsIfCfgControlTimer_Type=Gauge32
_SleMplsTpVplsIfCfgControlTimer_Object=MibScalar
sleMplsTpVplsIfCfgControlTimer=_SleMplsTpVplsIfCfgControlTimer_Object((1,3,6,1,4,1,6296,101,16,16,2,2,3),_SleMplsTpVplsIfCfgControlTimer_Type())
sleMplsTpVplsIfCfgControlTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpVplsIfCfgControlTimer.setStatus(_A)
_SleMplsTpVplsIfCfgControlTimestamp_Type=TimeTicks
_SleMplsTpVplsIfCfgControlTimestamp_Object=MibScalar
sleMplsTpVplsIfCfgControlTimestamp=_SleMplsTpVplsIfCfgControlTimestamp_Object((1,3,6,1,4,1,6296,101,16,16,2,2,4),_SleMplsTpVplsIfCfgControlTimestamp_Type())
sleMplsTpVplsIfCfgControlTimestamp.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpVplsIfCfgControlTimestamp.setStatus(_A)
_SleMplsTpVplsIfCfgControlReqResult_Type=SleControlRequestResultType
_SleMplsTpVplsIfCfgControlReqResult_Object=MibScalar
sleMplsTpVplsIfCfgControlReqResult=_SleMplsTpVplsIfCfgControlReqResult_Object((1,3,6,1,4,1,6296,101,16,16,2,2,5),_SleMplsTpVplsIfCfgControlReqResult_Type())
sleMplsTpVplsIfCfgControlReqResult.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpVplsIfCfgControlReqResult.setStatus(_A)
_SleMplsTpVplsIfCfgControlIfIndex_Type=InterfaceIndexOrZero
_SleMplsTpVplsIfCfgControlIfIndex_Object=MibScalar
sleMplsTpVplsIfCfgControlIfIndex=_SleMplsTpVplsIfCfgControlIfIndex_Object((1,3,6,1,4,1,6296,101,16,16,2,2,6),_SleMplsTpVplsIfCfgControlIfIndex_Type())
sleMplsTpVplsIfCfgControlIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpVplsIfCfgControlIfIndex.setStatus(_A)
_SleMplsTpVplsIfCfgControlName_Type=OctetString
_SleMplsTpVplsIfCfgControlName_Object=MibScalar
sleMplsTpVplsIfCfgControlName=_SleMplsTpVplsIfCfgControlName_Object((1,3,6,1,4,1,6296,101,16,16,2,2,7),_SleMplsTpVplsIfCfgControlName_Type())
sleMplsTpVplsIfCfgControlName.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpVplsIfCfgControlName.setStatus(_A)
_SleMplsTpVplsIfCfgControlServiceType_Type=IANAPwTypeTC
_SleMplsTpVplsIfCfgControlServiceType_Object=MibScalar
sleMplsTpVplsIfCfgControlServiceType=_SleMplsTpVplsIfCfgControlServiceType_Object((1,3,6,1,4,1,6296,101,16,16,2,2,8),_SleMplsTpVplsIfCfgControlServiceType_Type())
sleMplsTpVplsIfCfgControlServiceType.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpVplsIfCfgControlServiceType.setStatus(_A)
_SleMplsTpVplsIfCfgControlVlanId_Type=VlanIdOrAnyOrNone
_SleMplsTpVplsIfCfgControlVlanId_Object=MibScalar
sleMplsTpVplsIfCfgControlVlanId=_SleMplsTpVplsIfCfgControlVlanId_Object((1,3,6,1,4,1,6296,101,16,16,2,2,9),_SleMplsTpVplsIfCfgControlVlanId_Type())
sleMplsTpVplsIfCfgControlVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpVplsIfCfgControlVlanId.setStatus(_A)
_SleMplsTpVplsIfCfgControlInnerVlanId_Type=VlanIdOrAnyOrNone
_SleMplsTpVplsIfCfgControlInnerVlanId_Object=MibScalar
sleMplsTpVplsIfCfgControlInnerVlanId=_SleMplsTpVplsIfCfgControlInnerVlanId_Object((1,3,6,1,4,1,6296,101,16,16,2,2,10),_SleMplsTpVplsIfCfgControlInnerVlanId_Type())
sleMplsTpVplsIfCfgControlInnerVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpVplsIfCfgControlInnerVlanId.setStatus(_A)
class _SleMplsTpVplsIfCfgControlAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_N,1),('add',2),(_O,3),(_P,4)))
_SleMplsTpVplsIfCfgControlAction_Type.__name__=_D
_SleMplsTpVplsIfCfgControlAction_Object=MibScalar
sleMplsTpVplsIfCfgControlAction=_SleMplsTpVplsIfCfgControlAction_Object((1,3,6,1,4,1,6296,101,16,16,2,2,11),_SleMplsTpVplsIfCfgControlAction_Type())
sleMplsTpVplsIfCfgControlAction.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpVplsIfCfgControlAction.setStatus(_A)
_SleMplsTpVplsMeshCfg_ObjectIdentity=ObjectIdentity
sleMplsTpVplsMeshCfg=_SleMplsTpVplsMeshCfg_ObjectIdentity((1,3,6,1,4,1,6296,101,16,16,3))
_SleMplsTpVplsMeshCfgInfoTable_Object=MibTable
sleMplsTpVplsMeshCfgInfoTable=_SleMplsTpVplsMeshCfgInfoTable_Object((1,3,6,1,4,1,6296,101,16,16,3,1))
if mibBuilder.loadTexts:sleMplsTpVplsMeshCfgInfoTable.setStatus(_A)
_SleMplsTpVplsMeshCfgInfoEntry_Object=MibTableRow
sleMplsTpVplsMeshCfgInfoEntry=_SleMplsTpVplsMeshCfgInfoEntry_Object((1,3,6,1,4,1,6296,101,16,16,3,1,1))
sleMplsTpVplsMeshCfgInfoEntry.setIndexNames((0,_E,_F),(0,_E,_L))
if mibBuilder.loadTexts:sleMplsTpVplsMeshCfgInfoEntry.setStatus(_A)
_SleMplsTpVplsMeshCfgInfoPeerNodeId_Type=IpAddress
_SleMplsTpVplsMeshCfgInfoPeerNodeId_Object=MibTableColumn
sleMplsTpVplsMeshCfgInfoPeerNodeId=_SleMplsTpVplsMeshCfgInfoPeerNodeId_Object((1,3,6,1,4,1,6296,101,16,16,3,1,1,1),_SleMplsTpVplsMeshCfgInfoPeerNodeId_Type())
sleMplsTpVplsMeshCfgInfoPeerNodeId.setMaxAccess(_G)
if mibBuilder.loadTexts:sleMplsTpVplsMeshCfgInfoPeerNodeId.setStatus(_A)
class _SleMplsTpVplsMeshCfgInfoPeerNodeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ietf',1),('itut',2)))
_SleMplsTpVplsMeshCfgInfoPeerNodeType_Type.__name__=_D
_SleMplsTpVplsMeshCfgInfoPeerNodeType_Object=MibTableColumn
sleMplsTpVplsMeshCfgInfoPeerNodeType=_SleMplsTpVplsMeshCfgInfoPeerNodeType_Object((1,3,6,1,4,1,6296,101,16,16,3,1,1,2),_SleMplsTpVplsMeshCfgInfoPeerNodeType_Type())
sleMplsTpVplsMeshCfgInfoPeerNodeType.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpVplsMeshCfgInfoPeerNodeType.setStatus(_A)
_SleMplsTpVplsMeshCfgInfoPeerGlobalId_Type=Unsigned32
_SleMplsTpVplsMeshCfgInfoPeerGlobalId_Object=MibTableColumn
sleMplsTpVplsMeshCfgInfoPeerGlobalId=_SleMplsTpVplsMeshCfgInfoPeerGlobalId_Object((1,3,6,1,4,1,6296,101,16,16,3,1,1,3),_SleMplsTpVplsMeshCfgInfoPeerGlobalId_Type())
sleMplsTpVplsMeshCfgInfoPeerGlobalId.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpVplsMeshCfgInfoPeerGlobalId.setStatus(_A)
_SleMplsTpVplsMeshCfgInfoPeerCc_Type=MplsCcId
_SleMplsTpVplsMeshCfgInfoPeerCc_Object=MibTableColumn
sleMplsTpVplsMeshCfgInfoPeerCc=_SleMplsTpVplsMeshCfgInfoPeerCc_Object((1,3,6,1,4,1,6296,101,16,16,3,1,1,4),_SleMplsTpVplsMeshCfgInfoPeerCc_Type())
sleMplsTpVplsMeshCfgInfoPeerCc.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpVplsMeshCfgInfoPeerCc.setStatus(_A)
_SleMplsTpVplsMeshCfgInfoPeerIcc_Type=MplsIccId
_SleMplsTpVplsMeshCfgInfoPeerIcc_Object=MibTableColumn
sleMplsTpVplsMeshCfgInfoPeerIcc=_SleMplsTpVplsMeshCfgInfoPeerIcc_Object((1,3,6,1,4,1,6296,101,16,16,3,1,1,5),_SleMplsTpVplsMeshCfgInfoPeerIcc_Type())
sleMplsTpVplsMeshCfgInfoPeerIcc.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpVplsMeshCfgInfoPeerIcc.setStatus(_A)
_SleMplsTpVplsMeshCfgInfoTunnelId_Type=Integer32
_SleMplsTpVplsMeshCfgInfoTunnelId_Object=MibTableColumn
sleMplsTpVplsMeshCfgInfoTunnelId=_SleMplsTpVplsMeshCfgInfoTunnelId_Object((1,3,6,1,4,1,6296,101,16,16,3,1,1,6),_SleMplsTpVplsMeshCfgInfoTunnelId_Type())
sleMplsTpVplsMeshCfgInfoTunnelId.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpVplsMeshCfgInfoTunnelId.setStatus(_A)
_SleMplsTpVplsMeshCfgInfoTunnelName_Type=OctetString
_SleMplsTpVplsMeshCfgInfoTunnelName_Object=MibTableColumn
sleMplsTpVplsMeshCfgInfoTunnelName=_SleMplsTpVplsMeshCfgInfoTunnelName_Object((1,3,6,1,4,1,6296,101,16,16,3,1,1,7),_SleMplsTpVplsMeshCfgInfoTunnelName_Type())
sleMplsTpVplsMeshCfgInfoTunnelName.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpVplsMeshCfgInfoTunnelName.setStatus(_A)
class _SleMplsTpVplsMeshCfgInfoOwner_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_Q,1),(_R,2),(_S,3),(_T,4),('other',5)))
_SleMplsTpVplsMeshCfgInfoOwner_Type.__name__=_D
_SleMplsTpVplsMeshCfgInfoOwner_Object=MibTableColumn
sleMplsTpVplsMeshCfgInfoOwner=_SleMplsTpVplsMeshCfgInfoOwner_Object((1,3,6,1,4,1,6296,101,16,16,3,1,1,8),_SleMplsTpVplsMeshCfgInfoOwner_Type())
sleMplsTpVplsMeshCfgInfoOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpVplsMeshCfgInfoOwner.setStatus(_A)
class _SleMplsTpVplsMeshCfgInfoTunnelPath_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_U,0),(_V,1),(_I,2)))
_SleMplsTpVplsMeshCfgInfoTunnelPath_Type.__name__=_D
_SleMplsTpVplsMeshCfgInfoTunnelPath_Object=MibTableColumn
sleMplsTpVplsMeshCfgInfoTunnelPath=_SleMplsTpVplsMeshCfgInfoTunnelPath_Object((1,3,6,1,4,1,6296,101,16,16,3,1,1,9),_SleMplsTpVplsMeshCfgInfoTunnelPath_Type())
sleMplsTpVplsMeshCfgInfoTunnelPath.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpVplsMeshCfgInfoTunnelPath.setStatus(_A)
_SleMplsTpVplsMeshCfgInfoInLabel_Type=MplsLabel
_SleMplsTpVplsMeshCfgInfoInLabel_Object=MibTableColumn
sleMplsTpVplsMeshCfgInfoInLabel=_SleMplsTpVplsMeshCfgInfoInLabel_Object((1,3,6,1,4,1,6296,101,16,16,3,1,1,10),_SleMplsTpVplsMeshCfgInfoInLabel_Type())
sleMplsTpVplsMeshCfgInfoInLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpVplsMeshCfgInfoInLabel.setStatus(_A)
_SleMplsTpVplsMeshCfgInfoOutLabel_Type=MplsLabel
_SleMplsTpVplsMeshCfgInfoOutLabel_Object=MibTableColumn
sleMplsTpVplsMeshCfgInfoOutLabel=_SleMplsTpVplsMeshCfgInfoOutLabel_Object((1,3,6,1,4,1,6296,101,16,16,3,1,1,11),_SleMplsTpVplsMeshCfgInfoOutLabel_Type())
sleMplsTpVplsMeshCfgInfoOutLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpVplsMeshCfgInfoOutLabel.setStatus(_A)
_SleMplsTpVplsMeshCfgInfoOutInterface_Type=InterfaceIndexOrZero
_SleMplsTpVplsMeshCfgInfoOutInterface_Object=MibTableColumn
sleMplsTpVplsMeshCfgInfoOutInterface=_SleMplsTpVplsMeshCfgInfoOutInterface_Object((1,3,6,1,4,1,6296,101,16,16,3,1,1,12),_SleMplsTpVplsMeshCfgInfoOutInterface_Type())
sleMplsTpVplsMeshCfgInfoOutInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpVplsMeshCfgInfoOutInterface.setStatus(_A)
_SleMplsTpVplsMeshCfgInfoTunnelLabel_Type=MplsLabel
_SleMplsTpVplsMeshCfgInfoTunnelLabel_Object=MibTableColumn
sleMplsTpVplsMeshCfgInfoTunnelLabel=_SleMplsTpVplsMeshCfgInfoTunnelLabel_Object((1,3,6,1,4,1,6296,101,16,16,3,1,1,13),_SleMplsTpVplsMeshCfgInfoTunnelLabel_Type())
sleMplsTpVplsMeshCfgInfoTunnelLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpVplsMeshCfgInfoTunnelLabel.setStatus(_A)
class _SleMplsTpVplsMeshCfgInfoState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_SleMplsTpVplsMeshCfgInfoState_Type.__name__=_D
_SleMplsTpVplsMeshCfgInfoState_Object=MibTableColumn
sleMplsTpVplsMeshCfgInfoState=_SleMplsTpVplsMeshCfgInfoState_Object((1,3,6,1,4,1,6296,101,16,16,3,1,1,14),_SleMplsTpVplsMeshCfgInfoState_Type())
sleMplsTpVplsMeshCfgInfoState.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpVplsMeshCfgInfoState.setStatus(_A)
_SleMplsTpVplsMeshCfgInfoQosServicePolicy_Type=OctetString
_SleMplsTpVplsMeshCfgInfoQosServicePolicy_Object=MibTableColumn
sleMplsTpVplsMeshCfgInfoQosServicePolicy=_SleMplsTpVplsMeshCfgInfoQosServicePolicy_Object((1,3,6,1,4,1,6296,101,16,16,3,1,1,15),_SleMplsTpVplsMeshCfgInfoQosServicePolicy_Type())
sleMplsTpVplsMeshCfgInfoQosServicePolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpVplsMeshCfgInfoQosServicePolicy.setStatus(_A)
_SleMplsTpVplsMeshCfgControl_ObjectIdentity=ObjectIdentity
sleMplsTpVplsMeshCfgControl=_SleMplsTpVplsMeshCfgControl_ObjectIdentity((1,3,6,1,4,1,6296,101,16,16,3,2))
class _SleMplsTpVplsMeshCfgControlRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('createMplsTpVplsPeer',1),('createMplsTpVplsPeerWithTunnelPath',2),('deleteVplsPeer',3),('setVplsPeerFibEntry',4),('unsetVplsPeerFibEntry',5),('setVplsPeerQosServicePolicy',6),('unsetVplsPeerQosServicePolicy',7)))
_SleMplsTpVplsMeshCfgControlRequest_Type.__name__=_D
_SleMplsTpVplsMeshCfgControlRequest_Object=MibScalar
sleMplsTpVplsMeshCfgControlRequest=_SleMplsTpVplsMeshCfgControlRequest_Object((1,3,6,1,4,1,6296,101,16,16,3,2,1),_SleMplsTpVplsMeshCfgControlRequest_Type())
sleMplsTpVplsMeshCfgControlRequest.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpVplsMeshCfgControlRequest.setStatus(_A)
_SleMplsTpVplsMeshCfgControlStatus_Type=SleControlStatusType
_SleMplsTpVplsMeshCfgControlStatus_Object=MibScalar
sleMplsTpVplsMeshCfgControlStatus=_SleMplsTpVplsMeshCfgControlStatus_Object((1,3,6,1,4,1,6296,101,16,16,3,2,2),_SleMplsTpVplsMeshCfgControlStatus_Type())
sleMplsTpVplsMeshCfgControlStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpVplsMeshCfgControlStatus.setStatus(_A)
_SleMplsTpVplsMeshCfgControlTimer_Type=Gauge32
_SleMplsTpVplsMeshCfgControlTimer_Object=MibScalar
sleMplsTpVplsMeshCfgControlTimer=_SleMplsTpVplsMeshCfgControlTimer_Object((1,3,6,1,4,1,6296,101,16,16,3,2,3),_SleMplsTpVplsMeshCfgControlTimer_Type())
sleMplsTpVplsMeshCfgControlTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpVplsMeshCfgControlTimer.setStatus(_A)
_SleMplsTpVplsMeshCfgControlTimestamp_Type=TimeTicks
_SleMplsTpVplsMeshCfgControlTimestamp_Object=MibScalar
sleMplsTpVplsMeshCfgControlTimestamp=_SleMplsTpVplsMeshCfgControlTimestamp_Object((1,3,6,1,4,1,6296,101,16,16,3,2,4),_SleMplsTpVplsMeshCfgControlTimestamp_Type())
sleMplsTpVplsMeshCfgControlTimestamp.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpVplsMeshCfgControlTimestamp.setStatus(_A)
_SleMplsTpVplsMeshCfgControlReqResult_Type=SleControlRequestResultType
_SleMplsTpVplsMeshCfgControlReqResult_Object=MibScalar
sleMplsTpVplsMeshCfgControlReqResult=_SleMplsTpVplsMeshCfgControlReqResult_Object((1,3,6,1,4,1,6296,101,16,16,3,2,5),_SleMplsTpVplsMeshCfgControlReqResult_Type())
sleMplsTpVplsMeshCfgControlReqResult.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpVplsMeshCfgControlReqResult.setStatus(_A)
_SleMplsTpVplsMeshCfgControlVplsId_Type=Unsigned32
_SleMplsTpVplsMeshCfgControlVplsId_Object=MibScalar
sleMplsTpVplsMeshCfgControlVplsId=_SleMplsTpVplsMeshCfgControlVplsId_Object((1,3,6,1,4,1,6296,101,16,16,3,2,6),_SleMplsTpVplsMeshCfgControlVplsId_Type())
sleMplsTpVplsMeshCfgControlVplsId.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpVplsMeshCfgControlVplsId.setStatus(_A)
_SleMplsTpVplsMeshCfgControlPeerNodeId_Type=IpAddress
_SleMplsTpVplsMeshCfgControlPeerNodeId_Object=MibScalar
sleMplsTpVplsMeshCfgControlPeerNodeId=_SleMplsTpVplsMeshCfgControlPeerNodeId_Object((1,3,6,1,4,1,6296,101,16,16,3,2,7),_SleMplsTpVplsMeshCfgControlPeerNodeId_Type())
sleMplsTpVplsMeshCfgControlPeerNodeId.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpVplsMeshCfgControlPeerNodeId.setStatus(_A)
class _SleMplsTpVplsMeshCfgControlPeerNodeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ietf',1),('itut',2)))
_SleMplsTpVplsMeshCfgControlPeerNodeType_Type.__name__=_D
_SleMplsTpVplsMeshCfgControlPeerNodeType_Object=MibScalar
sleMplsTpVplsMeshCfgControlPeerNodeType=_SleMplsTpVplsMeshCfgControlPeerNodeType_Object((1,3,6,1,4,1,6296,101,16,16,3,2,8),_SleMplsTpVplsMeshCfgControlPeerNodeType_Type())
sleMplsTpVplsMeshCfgControlPeerNodeType.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpVplsMeshCfgControlPeerNodeType.setStatus(_A)
_SleMplsTpVplsMeshCfgControlPeerGlobalId_Type=Unsigned32
_SleMplsTpVplsMeshCfgControlPeerGlobalId_Object=MibScalar
sleMplsTpVplsMeshCfgControlPeerGlobalId=_SleMplsTpVplsMeshCfgControlPeerGlobalId_Object((1,3,6,1,4,1,6296,101,16,16,3,2,9),_SleMplsTpVplsMeshCfgControlPeerGlobalId_Type())
sleMplsTpVplsMeshCfgControlPeerGlobalId.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpVplsMeshCfgControlPeerGlobalId.setStatus(_A)
_SleMplsTpVplsMeshCfgControlPeerCc_Type=MplsCcId
_SleMplsTpVplsMeshCfgControlPeerCc_Object=MibScalar
sleMplsTpVplsMeshCfgControlPeerCc=_SleMplsTpVplsMeshCfgControlPeerCc_Object((1,3,6,1,4,1,6296,101,16,16,3,2,10),_SleMplsTpVplsMeshCfgControlPeerCc_Type())
sleMplsTpVplsMeshCfgControlPeerCc.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpVplsMeshCfgControlPeerCc.setStatus(_A)
_SleMplsTpVplsMeshCfgControlPeerIcc_Type=MplsIccId
_SleMplsTpVplsMeshCfgControlPeerIcc_Object=MibScalar
sleMplsTpVplsMeshCfgControlPeerIcc=_SleMplsTpVplsMeshCfgControlPeerIcc_Object((1,3,6,1,4,1,6296,101,16,16,3,2,11),_SleMplsTpVplsMeshCfgControlPeerIcc_Type())
sleMplsTpVplsMeshCfgControlPeerIcc.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpVplsMeshCfgControlPeerIcc.setStatus(_A)
_SleMplsTpVplsMeshCfgControlTunnelId_Type=Integer32
_SleMplsTpVplsMeshCfgControlTunnelId_Object=MibScalar
sleMplsTpVplsMeshCfgControlTunnelId=_SleMplsTpVplsMeshCfgControlTunnelId_Object((1,3,6,1,4,1,6296,101,16,16,3,2,12),_SleMplsTpVplsMeshCfgControlTunnelId_Type())
sleMplsTpVplsMeshCfgControlTunnelId.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpVplsMeshCfgControlTunnelId.setStatus(_A)
_SleMplsTpVplsMeshCfgControlTunnelName_Type=OctetString
_SleMplsTpVplsMeshCfgControlTunnelName_Object=MibScalar
sleMplsTpVplsMeshCfgControlTunnelName=_SleMplsTpVplsMeshCfgControlTunnelName_Object((1,3,6,1,4,1,6296,101,16,16,3,2,13),_SleMplsTpVplsMeshCfgControlTunnelName_Type())
sleMplsTpVplsMeshCfgControlTunnelName.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpVplsMeshCfgControlTunnelName.setStatus(_A)
class _SleMplsTpVplsMeshCfgControlOwner_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_Q,1),(_R,2),(_S,3),(_T,4),('other',5)))
_SleMplsTpVplsMeshCfgControlOwner_Type.__name__=_D
_SleMplsTpVplsMeshCfgControlOwner_Object=MibScalar
sleMplsTpVplsMeshCfgControlOwner=_SleMplsTpVplsMeshCfgControlOwner_Object((1,3,6,1,4,1,6296,101,16,16,3,2,14),_SleMplsTpVplsMeshCfgControlOwner_Type())
sleMplsTpVplsMeshCfgControlOwner.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpVplsMeshCfgControlOwner.setStatus(_A)
class _SleMplsTpVplsMeshCfgControlTunnelPath_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_U,0),(_V,1)))
_SleMplsTpVplsMeshCfgControlTunnelPath_Type.__name__=_D
_SleMplsTpVplsMeshCfgControlTunnelPath_Object=MibScalar
sleMplsTpVplsMeshCfgControlTunnelPath=_SleMplsTpVplsMeshCfgControlTunnelPath_Object((1,3,6,1,4,1,6296,101,16,16,3,2,15),_SleMplsTpVplsMeshCfgControlTunnelPath_Type())
sleMplsTpVplsMeshCfgControlTunnelPath.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpVplsMeshCfgControlTunnelPath.setStatus(_A)
_SleMplsTpVplsMeshCfgControlInLabel_Type=MplsLabel
_SleMplsTpVplsMeshCfgControlInLabel_Object=MibScalar
sleMplsTpVplsMeshCfgControlInLabel=_SleMplsTpVplsMeshCfgControlInLabel_Object((1,3,6,1,4,1,6296,101,16,16,3,2,16),_SleMplsTpVplsMeshCfgControlInLabel_Type())
sleMplsTpVplsMeshCfgControlInLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpVplsMeshCfgControlInLabel.setStatus(_A)
_SleMplsTpVplsMeshCfgControlOutLabel_Type=MplsLabel
_SleMplsTpVplsMeshCfgControlOutLabel_Object=MibScalar
sleMplsTpVplsMeshCfgControlOutLabel=_SleMplsTpVplsMeshCfgControlOutLabel_Object((1,3,6,1,4,1,6296,101,16,16,3,2,17),_SleMplsTpVplsMeshCfgControlOutLabel_Type())
sleMplsTpVplsMeshCfgControlOutLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpVplsMeshCfgControlOutLabel.setStatus(_A)
_SleMplsTpVplsMeshCfgControlQosServicePolicy_Type=OctetString
_SleMplsTpVplsMeshCfgControlQosServicePolicy_Object=MibScalar
sleMplsTpVplsMeshCfgControlQosServicePolicy=_SleMplsTpVplsMeshCfgControlQosServicePolicy_Object((1,3,6,1,4,1,6296,101,16,16,3,2,18),_SleMplsTpVplsMeshCfgControlQosServicePolicy_Type())
sleMplsTpVplsMeshCfgControlQosServicePolicy.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpVplsMeshCfgControlQosServicePolicy.setStatus(_A)
_SleMplsTpVplsSpokeCfg_ObjectIdentity=ObjectIdentity
sleMplsTpVplsSpokeCfg=_SleMplsTpVplsSpokeCfg_ObjectIdentity((1,3,6,1,4,1,6296,101,16,16,4))
_SleMplsTpVplsSpokeCfgInfoTable_Object=MibTable
sleMplsTpVplsSpokeCfgInfoTable=_SleMplsTpVplsSpokeCfgInfoTable_Object((1,3,6,1,4,1,6296,101,16,16,4,1))
if mibBuilder.loadTexts:sleMplsTpVplsSpokeCfgInfoTable.setStatus(_A)
_SleMplsTpVplsSpokeCfgInfoEntry_Object=MibTableRow
sleMplsTpVplsSpokeCfgInfoEntry=_SleMplsTpVplsSpokeCfgInfoEntry_Object((1,3,6,1,4,1,6296,101,16,16,4,1,1))
sleMplsTpVplsSpokeCfgInfoEntry.setIndexNames((0,_E,_F),(0,_E,_W))
if mibBuilder.loadTexts:sleMplsTpVplsSpokeCfgInfoEntry.setStatus(_A)
_SleMplsTpVplsSpokeCfgInfoVcName_Type=OctetString
_SleMplsTpVplsSpokeCfgInfoVcName_Object=MibTableColumn
sleMplsTpVplsSpokeCfgInfoVcName=_SleMplsTpVplsSpokeCfgInfoVcName_Object((1,3,6,1,4,1,6296,101,16,16,4,1,1,1),_SleMplsTpVplsSpokeCfgInfoVcName_Type())
sleMplsTpVplsSpokeCfgInfoVcName.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpVplsSpokeCfgInfoVcName.setStatus(_A)
_SleMplsTpVplsSpokeCfgInfoTunnelName_Type=OctetString
_SleMplsTpVplsSpokeCfgInfoTunnelName_Object=MibTableColumn
sleMplsTpVplsSpokeCfgInfoTunnelName=_SleMplsTpVplsSpokeCfgInfoTunnelName_Object((1,3,6,1,4,1,6296,101,16,16,4,1,1,2),_SleMplsTpVplsSpokeCfgInfoTunnelName_Type())
sleMplsTpVplsSpokeCfgInfoTunnelName.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpVplsSpokeCfgInfoTunnelName.setStatus(_A)
_SleMplsTpVplsSpokeCfgInfoServiceType_Type=IANAPwTypeTC
_SleMplsTpVplsSpokeCfgInfoServiceType_Object=MibTableColumn
sleMplsTpVplsSpokeCfgInfoServiceType=_SleMplsTpVplsSpokeCfgInfoServiceType_Object((1,3,6,1,4,1,6296,101,16,16,4,1,1,3),_SleMplsTpVplsSpokeCfgInfoServiceType_Type())
sleMplsTpVplsSpokeCfgInfoServiceType.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpVplsSpokeCfgInfoServiceType.setStatus(_A)
_SleMplsTpVplsSpokeCfgInfoInLabel_Type=MplsLabel
_SleMplsTpVplsSpokeCfgInfoInLabel_Object=MibTableColumn
sleMplsTpVplsSpokeCfgInfoInLabel=_SleMplsTpVplsSpokeCfgInfoInLabel_Object((1,3,6,1,4,1,6296,101,16,16,4,1,1,4),_SleMplsTpVplsSpokeCfgInfoInLabel_Type())
sleMplsTpVplsSpokeCfgInfoInLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpVplsSpokeCfgInfoInLabel.setStatus(_A)
_SleMplsTpVplsSpokeCfgInfoOutLabel_Type=MplsLabel
_SleMplsTpVplsSpokeCfgInfoOutLabel_Object=MibTableColumn
sleMplsTpVplsSpokeCfgInfoOutLabel=_SleMplsTpVplsSpokeCfgInfoOutLabel_Object((1,3,6,1,4,1,6296,101,16,16,4,1,1,5),_SleMplsTpVplsSpokeCfgInfoOutLabel_Type())
sleMplsTpVplsSpokeCfgInfoOutLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpVplsSpokeCfgInfoOutLabel.setStatus(_A)
_SleMplsTpVplsSpokeCfgInfoOutInterface_Type=InterfaceIndexOrZero
_SleMplsTpVplsSpokeCfgInfoOutInterface_Object=MibTableColumn
sleMplsTpVplsSpokeCfgInfoOutInterface=_SleMplsTpVplsSpokeCfgInfoOutInterface_Object((1,3,6,1,4,1,6296,101,16,16,4,1,1,6),_SleMplsTpVplsSpokeCfgInfoOutInterface_Type())
sleMplsTpVplsSpokeCfgInfoOutInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpVplsSpokeCfgInfoOutInterface.setStatus(_A)
class _SleMplsTpVplsSpokeCfgInfoState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_SleMplsTpVplsSpokeCfgInfoState_Type.__name__=_D
_SleMplsTpVplsSpokeCfgInfoState_Object=MibTableColumn
sleMplsTpVplsSpokeCfgInfoState=_SleMplsTpVplsSpokeCfgInfoState_Object((1,3,6,1,4,1,6296,101,16,16,4,1,1,7),_SleMplsTpVplsSpokeCfgInfoState_Type())
sleMplsTpVplsSpokeCfgInfoState.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpVplsSpokeCfgInfoState.setStatus(_A)
_SleMplsTpVplsSpokeCfgInfoQosServicePolicy_Type=OctetString
_SleMplsTpVplsSpokeCfgInfoQosServicePolicy_Object=MibTableColumn
sleMplsTpVplsSpokeCfgInfoQosServicePolicy=_SleMplsTpVplsSpokeCfgInfoQosServicePolicy_Object((1,3,6,1,4,1,6296,101,16,16,4,1,1,8),_SleMplsTpVplsSpokeCfgInfoQosServicePolicy_Type())
sleMplsTpVplsSpokeCfgInfoQosServicePolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpVplsSpokeCfgInfoQosServicePolicy.setStatus(_A)
_SleMplsTpVplsSpokeCfgControl_ObjectIdentity=ObjectIdentity
sleMplsTpVplsSpokeCfgControl=_SleMplsTpVplsSpokeCfgControl_ObjectIdentity((1,3,6,1,4,1,6296,101,16,16,4,2))
class _SleMplsTpVplsSpokeCfgControlRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('createMplsTpVplsSpoke',1),('deleteMplsTpVplsSpoke',2),('setVplsSpokeFibEntry',3),('unsetVplsSpokeFibEntry',4),('setVplsSpokeQosServicePolicy',5),('unsetVplsSpokeQosServicePolicy',6)))
_SleMplsTpVplsSpokeCfgControlRequest_Type.__name__=_D
_SleMplsTpVplsSpokeCfgControlRequest_Object=MibScalar
sleMplsTpVplsSpokeCfgControlRequest=_SleMplsTpVplsSpokeCfgControlRequest_Object((1,3,6,1,4,1,6296,101,16,16,4,2,1),_SleMplsTpVplsSpokeCfgControlRequest_Type())
sleMplsTpVplsSpokeCfgControlRequest.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpVplsSpokeCfgControlRequest.setStatus(_A)
_SleMplsTpVplsSpokeCfgControlStatus_Type=SleControlStatusType
_SleMplsTpVplsSpokeCfgControlStatus_Object=MibScalar
sleMplsTpVplsSpokeCfgControlStatus=_SleMplsTpVplsSpokeCfgControlStatus_Object((1,3,6,1,4,1,6296,101,16,16,4,2,2),_SleMplsTpVplsSpokeCfgControlStatus_Type())
sleMplsTpVplsSpokeCfgControlStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpVplsSpokeCfgControlStatus.setStatus(_A)
_SleMplsTpVplsSpokeCfgControlTimer_Type=Gauge32
_SleMplsTpVplsSpokeCfgControlTimer_Object=MibScalar
sleMplsTpVplsSpokeCfgControlTimer=_SleMplsTpVplsSpokeCfgControlTimer_Object((1,3,6,1,4,1,6296,101,16,16,4,2,3),_SleMplsTpVplsSpokeCfgControlTimer_Type())
sleMplsTpVplsSpokeCfgControlTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpVplsSpokeCfgControlTimer.setStatus(_A)
_SleMplsTpVplsSpokeCfgControlTimestamp_Type=TimeTicks
_SleMplsTpVplsSpokeCfgControlTimestamp_Object=MibScalar
sleMplsTpVplsSpokeCfgControlTimestamp=_SleMplsTpVplsSpokeCfgControlTimestamp_Object((1,3,6,1,4,1,6296,101,16,16,4,2,4),_SleMplsTpVplsSpokeCfgControlTimestamp_Type())
sleMplsTpVplsSpokeCfgControlTimestamp.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpVplsSpokeCfgControlTimestamp.setStatus(_A)
_SleMplsTpVplsSpokeCfgControlReqResult_Type=SleControlRequestResultType
_SleMplsTpVplsSpokeCfgControlReqResult_Object=MibScalar
sleMplsTpVplsSpokeCfgControlReqResult=_SleMplsTpVplsSpokeCfgControlReqResult_Object((1,3,6,1,4,1,6296,101,16,16,4,2,5),_SleMplsTpVplsSpokeCfgControlReqResult_Type())
sleMplsTpVplsSpokeCfgControlReqResult.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpVplsSpokeCfgControlReqResult.setStatus(_A)
_SleMplsTpVplsSpokeCfgControlVplsId_Type=Unsigned32
_SleMplsTpVplsSpokeCfgControlVplsId_Object=MibScalar
sleMplsTpVplsSpokeCfgControlVplsId=_SleMplsTpVplsSpokeCfgControlVplsId_Object((1,3,6,1,4,1,6296,101,16,16,4,2,6),_SleMplsTpVplsSpokeCfgControlVplsId_Type())
sleMplsTpVplsSpokeCfgControlVplsId.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpVplsSpokeCfgControlVplsId.setStatus(_A)
_SleMplsTpVplsSpokeCfgControlVcName_Type=OctetString
_SleMplsTpVplsSpokeCfgControlVcName_Object=MibScalar
sleMplsTpVplsSpokeCfgControlVcName=_SleMplsTpVplsSpokeCfgControlVcName_Object((1,3,6,1,4,1,6296,101,16,16,4,2,7),_SleMplsTpVplsSpokeCfgControlVcName_Type())
sleMplsTpVplsSpokeCfgControlVcName.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpVplsSpokeCfgControlVcName.setStatus(_A)
_SleMplsTpVplsSpokeCfgControlTunnelName_Type=OctetString
_SleMplsTpVplsSpokeCfgControlTunnelName_Object=MibScalar
sleMplsTpVplsSpokeCfgControlTunnelName=_SleMplsTpVplsSpokeCfgControlTunnelName_Object((1,3,6,1,4,1,6296,101,16,16,4,2,8),_SleMplsTpVplsSpokeCfgControlTunnelName_Type())
sleMplsTpVplsSpokeCfgControlTunnelName.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpVplsSpokeCfgControlTunnelName.setStatus(_A)
_SleMplsTpVplsSpokeCfgControlServiceType_Type=IANAPwTypeTC
_SleMplsTpVplsSpokeCfgControlServiceType_Object=MibScalar
sleMplsTpVplsSpokeCfgControlServiceType=_SleMplsTpVplsSpokeCfgControlServiceType_Object((1,3,6,1,4,1,6296,101,16,16,4,2,9),_SleMplsTpVplsSpokeCfgControlServiceType_Type())
sleMplsTpVplsSpokeCfgControlServiceType.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpVplsSpokeCfgControlServiceType.setStatus(_A)
_SleMplsTpVplsSpokeCfgControlInLabel_Type=MplsLabel
_SleMplsTpVplsSpokeCfgControlInLabel_Object=MibScalar
sleMplsTpVplsSpokeCfgControlInLabel=_SleMplsTpVplsSpokeCfgControlInLabel_Object((1,3,6,1,4,1,6296,101,16,16,4,2,10),_SleMplsTpVplsSpokeCfgControlInLabel_Type())
sleMplsTpVplsSpokeCfgControlInLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpVplsSpokeCfgControlInLabel.setStatus(_A)
_SleMplsTpVplsSpokeCfgControlOutLabel_Type=MplsLabel
_SleMplsTpVplsSpokeCfgControlOutLabel_Object=MibScalar
sleMplsTpVplsSpokeCfgControlOutLabel=_SleMplsTpVplsSpokeCfgControlOutLabel_Object((1,3,6,1,4,1,6296,101,16,16,4,2,11),_SleMplsTpVplsSpokeCfgControlOutLabel_Type())
sleMplsTpVplsSpokeCfgControlOutLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpVplsSpokeCfgControlOutLabel.setStatus(_A)
_SleMplsTpVplsSpokeCfgControlOutInterface_Type=InterfaceIndexOrZero
_SleMplsTpVplsSpokeCfgControlOutInterface_Object=MibScalar
sleMplsTpVplsSpokeCfgControlOutInterface=_SleMplsTpVplsSpokeCfgControlOutInterface_Object((1,3,6,1,4,1,6296,101,16,16,4,2,12),_SleMplsTpVplsSpokeCfgControlOutInterface_Type())
sleMplsTpVplsSpokeCfgControlOutInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpVplsSpokeCfgControlOutInterface.setStatus(_A)
_SleMplsTpVplsSpokeCfgControlQosServicePolicy_Type=OctetString
_SleMplsTpVplsSpokeCfgControlQosServicePolicy_Object=MibScalar
sleMplsTpVplsSpokeCfgControlQosServicePolicy=_SleMplsTpVplsSpokeCfgControlQosServicePolicy_Object((1,3,6,1,4,1,6296,101,16,16,4,2,13),_SleMplsTpVplsSpokeCfgControlQosServicePolicy_Type())
sleMplsTpVplsSpokeCfgControlQosServicePolicy.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpVplsSpokeCfgControlQosServicePolicy.setStatus(_A)
_SleMplsTpVplsMacLearning_ObjectIdentity=ObjectIdentity
sleMplsTpVplsMacLearning=_SleMplsTpVplsMacLearning_ObjectIdentity((1,3,6,1,4,1,6296,101,16,16,5))
_SleMplsTpVplsMacLearningInfoTable_Object=MibTable
sleMplsTpVplsMacLearningInfoTable=_SleMplsTpVplsMacLearningInfoTable_Object((1,3,6,1,4,1,6296,101,16,16,5,1))
if mibBuilder.loadTexts:sleMplsTpVplsMacLearningInfoTable.setStatus(_A)
_SleMplsTpVplsMacLearningInfoEntry_Object=MibTableRow
sleMplsTpVplsMacLearningInfoEntry=_SleMplsTpVplsMacLearningInfoEntry_Object((1,3,6,1,4,1,6296,101,16,16,5,1,1))
sleMplsTpVplsMacLearningInfoEntry.setIndexNames((0,_E,_F),(0,_E,_X))
if mibBuilder.loadTexts:sleMplsTpVplsMacLearningInfoEntry.setStatus(_A)
_SleMplsTpVplsMacLearningInfoMacAddress_Type=OctetString
_SleMplsTpVplsMacLearningInfoMacAddress_Object=MibTableColumn
sleMplsTpVplsMacLearningInfoMacAddress=_SleMplsTpVplsMacLearningInfoMacAddress_Object((1,3,6,1,4,1,6296,101,16,16,5,1,1,1),_SleMplsTpVplsMacLearningInfoMacAddress_Type())
sleMplsTpVplsMacLearningInfoMacAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:sleMplsTpVplsMacLearningInfoMacAddress.setStatus(_A)
_SleMplsTpVplsMacLearningInfoInterfacIndex_Type=InterfaceIndexOrZero
_SleMplsTpVplsMacLearningInfoInterfacIndex_Object=MibTableColumn
sleMplsTpVplsMacLearningInfoInterfacIndex=_SleMplsTpVplsMacLearningInfoInterfacIndex_Object((1,3,6,1,4,1,6296,101,16,16,5,1,1,2),_SleMplsTpVplsMacLearningInfoInterfacIndex_Type())
sleMplsTpVplsMacLearningInfoInterfacIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpVplsMacLearningInfoInterfacIndex.setStatus(_A)
_SleMplsTpVplsMacLearningInfoMeshAddress_Type=IpAddress
_SleMplsTpVplsMacLearningInfoMeshAddress_Object=MibTableColumn
sleMplsTpVplsMacLearningInfoMeshAddress=_SleMplsTpVplsMacLearningInfoMeshAddress_Object((1,3,6,1,4,1,6296,101,16,16,5,1,1,3),_SleMplsTpVplsMacLearningInfoMeshAddress_Type())
sleMplsTpVplsMacLearningInfoMeshAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpVplsMacLearningInfoMeshAddress.setStatus(_A)
_SleMplsTpVplsMacLearningControl_ObjectIdentity=ObjectIdentity
sleMplsTpVplsMacLearningControl=_SleMplsTpVplsMacLearningControl_ObjectIdentity((1,3,6,1,4,1,6296,101,16,16,5,2))
class _SleMplsTpVplsMacLearningControlRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('clearVplsMacAddress',1))
_SleMplsTpVplsMacLearningControlRequest_Type.__name__=_D
_SleMplsTpVplsMacLearningControlRequest_Object=MibScalar
sleMplsTpVplsMacLearningControlRequest=_SleMplsTpVplsMacLearningControlRequest_Object((1,3,6,1,4,1,6296,101,16,16,5,2,1),_SleMplsTpVplsMacLearningControlRequest_Type())
sleMplsTpVplsMacLearningControlRequest.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpVplsMacLearningControlRequest.setStatus(_A)
_SleMplsTpVplsMacLearningControlStatus_Type=SleControlStatusType
_SleMplsTpVplsMacLearningControlStatus_Object=MibScalar
sleMplsTpVplsMacLearningControlStatus=_SleMplsTpVplsMacLearningControlStatus_Object((1,3,6,1,4,1,6296,101,16,16,5,2,2),_SleMplsTpVplsMacLearningControlStatus_Type())
sleMplsTpVplsMacLearningControlStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpVplsMacLearningControlStatus.setStatus(_A)
_SleMplsTpVplsMacLearningControlTimer_Type=Gauge32
_SleMplsTpVplsMacLearningControlTimer_Object=MibScalar
sleMplsTpVplsMacLearningControlTimer=_SleMplsTpVplsMacLearningControlTimer_Object((1,3,6,1,4,1,6296,101,16,16,5,2,3),_SleMplsTpVplsMacLearningControlTimer_Type())
sleMplsTpVplsMacLearningControlTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpVplsMacLearningControlTimer.setStatus(_A)
_SleMplsTpVplsMacLearningControlTimestamp_Type=TimeTicks
_SleMplsTpVplsMacLearningControlTimestamp_Object=MibScalar
sleMplsTpVplsMacLearningControlTimestamp=_SleMplsTpVplsMacLearningControlTimestamp_Object((1,3,6,1,4,1,6296,101,16,16,5,2,4),_SleMplsTpVplsMacLearningControlTimestamp_Type())
sleMplsTpVplsMacLearningControlTimestamp.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpVplsMacLearningControlTimestamp.setStatus(_A)
_SleMplsTpVplsMacLearningControlReqResult_Type=SleControlRequestResultType
_SleMplsTpVplsMacLearningControlReqResult_Object=MibScalar
sleMplsTpVplsMacLearningControlReqResult=_SleMplsTpVplsMacLearningControlReqResult_Object((1,3,6,1,4,1,6296,101,16,16,5,2,5),_SleMplsTpVplsMacLearningControlReqResult_Type())
sleMplsTpVplsMacLearningControlReqResult.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpVplsMacLearningControlReqResult.setStatus(_A)
_SleMplsTpVplsMacLearningControlVplsId_Type=Unsigned32
_SleMplsTpVplsMacLearningControlVplsId_Object=MibScalar
sleMplsTpVplsMacLearningControlVplsId=_SleMplsTpVplsMacLearningControlVplsId_Object((1,3,6,1,4,1,6296,101,16,16,5,2,6),_SleMplsTpVplsMacLearningControlVplsId_Type())
sleMplsTpVplsMacLearningControlVplsId.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpVplsMacLearningControlVplsId.setStatus(_A)
_SleMplsTpVplsStatistics_ObjectIdentity=ObjectIdentity
sleMplsTpVplsStatistics=_SleMplsTpVplsStatistics_ObjectIdentity((1,3,6,1,4,1,6296,101,16,16,6))
_SleMplsTpVplsAcStatistics_ObjectIdentity=ObjectIdentity
sleMplsTpVplsAcStatistics=_SleMplsTpVplsAcStatistics_ObjectIdentity((1,3,6,1,4,1,6296,101,16,16,6,1))
_SleMplsTpVplsAcStatisticsInfoTable_Object=MibTable
sleMplsTpVplsAcStatisticsInfoTable=_SleMplsTpVplsAcStatisticsInfoTable_Object((1,3,6,1,4,1,6296,101,16,16,6,1,1))
if mibBuilder.loadTexts:sleMplsTpVplsAcStatisticsInfoTable.setStatus(_A)
_SleMplsTpVplsAcStatisticsInfoEntry_Object=MibTableRow
sleMplsTpVplsAcStatisticsInfoEntry=_SleMplsTpVplsAcStatisticsInfoEntry_Object((1,3,6,1,4,1,6296,101,16,16,6,1,1,1))
sleMplsTpVplsAcStatisticsInfoEntry.setIndexNames((0,_E,_J),(0,_E,_K))
if mibBuilder.loadTexts:sleMplsTpVplsAcStatisticsInfoEntry.setStatus(_A)
_SleMplsTpVplsAcStatisticsInfoTxPackets_Type=Counter64
_SleMplsTpVplsAcStatisticsInfoTxPackets_Object=MibTableColumn
sleMplsTpVplsAcStatisticsInfoTxPackets=_SleMplsTpVplsAcStatisticsInfoTxPackets_Object((1,3,6,1,4,1,6296,101,16,16,6,1,1,1,1),_SleMplsTpVplsAcStatisticsInfoTxPackets_Type())
sleMplsTpVplsAcStatisticsInfoTxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpVplsAcStatisticsInfoTxPackets.setStatus(_A)
_SleMplsTpVplsAcStatisticsInfoTxBytes_Type=Counter64
_SleMplsTpVplsAcStatisticsInfoTxBytes_Object=MibTableColumn
sleMplsTpVplsAcStatisticsInfoTxBytes=_SleMplsTpVplsAcStatisticsInfoTxBytes_Object((1,3,6,1,4,1,6296,101,16,16,6,1,1,1,2),_SleMplsTpVplsAcStatisticsInfoTxBytes_Type())
sleMplsTpVplsAcStatisticsInfoTxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpVplsAcStatisticsInfoTxBytes.setStatus(_A)
_SleMplsTpVplsAcStatisticsInfoRxPackets_Type=Counter64
_SleMplsTpVplsAcStatisticsInfoRxPackets_Object=MibTableColumn
sleMplsTpVplsAcStatisticsInfoRxPackets=_SleMplsTpVplsAcStatisticsInfoRxPackets_Object((1,3,6,1,4,1,6296,101,16,16,6,1,1,1,3),_SleMplsTpVplsAcStatisticsInfoRxPackets_Type())
sleMplsTpVplsAcStatisticsInfoRxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpVplsAcStatisticsInfoRxPackets.setStatus(_A)
_SleMplsTpVplsAcStatisticsInfoRxBytes_Type=Counter64
_SleMplsTpVplsAcStatisticsInfoRxBytes_Object=MibTableColumn
sleMplsTpVplsAcStatisticsInfoRxBytes=_SleMplsTpVplsAcStatisticsInfoRxBytes_Object((1,3,6,1,4,1,6296,101,16,16,6,1,1,1,4),_SleMplsTpVplsAcStatisticsInfoRxBytes_Type())
sleMplsTpVplsAcStatisticsInfoRxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpVplsAcStatisticsInfoRxBytes.setStatus(_A)
_SleMplsTpVplsPeerStatistics_ObjectIdentity=ObjectIdentity
sleMplsTpVplsPeerStatistics=_SleMplsTpVplsPeerStatistics_ObjectIdentity((1,3,6,1,4,1,6296,101,16,16,6,2))
_SleMplsTpVplsPeerStatisticsInfoTable_Object=MibTable
sleMplsTpVplsPeerStatisticsInfoTable=_SleMplsTpVplsPeerStatisticsInfoTable_Object((1,3,6,1,4,1,6296,101,16,16,6,2,1))
if mibBuilder.loadTexts:sleMplsTpVplsPeerStatisticsInfoTable.setStatus(_A)
_SleMplsTpVplsPeerStatisticsInfoEntry_Object=MibTableRow
sleMplsTpVplsPeerStatisticsInfoEntry=_SleMplsTpVplsPeerStatisticsInfoEntry_Object((1,3,6,1,4,1,6296,101,16,16,6,2,1,1))
sleMplsTpVplsPeerStatisticsInfoEntry.setIndexNames((0,_E,_F),(0,_E,_L))
if mibBuilder.loadTexts:sleMplsTpVplsPeerStatisticsInfoEntry.setStatus(_A)
_SleMplsTpVplsPeerStatisticsInfoTxPackets_Type=Counter64
_SleMplsTpVplsPeerStatisticsInfoTxPackets_Object=MibTableColumn
sleMplsTpVplsPeerStatisticsInfoTxPackets=_SleMplsTpVplsPeerStatisticsInfoTxPackets_Object((1,3,6,1,4,1,6296,101,16,16,6,2,1,1,1),_SleMplsTpVplsPeerStatisticsInfoTxPackets_Type())
sleMplsTpVplsPeerStatisticsInfoTxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpVplsPeerStatisticsInfoTxPackets.setStatus(_A)
_SleMplsTpVplsPeerStatisticsInfoTxBytes_Type=Counter64
_SleMplsTpVplsPeerStatisticsInfoTxBytes_Object=MibTableColumn
sleMplsTpVplsPeerStatisticsInfoTxBytes=_SleMplsTpVplsPeerStatisticsInfoTxBytes_Object((1,3,6,1,4,1,6296,101,16,16,6,2,1,1,2),_SleMplsTpVplsPeerStatisticsInfoTxBytes_Type())
sleMplsTpVplsPeerStatisticsInfoTxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpVplsPeerStatisticsInfoTxBytes.setStatus(_A)
_SleMplsTpVplsPeerStatisticsInfoRxPackets_Type=Counter64
_SleMplsTpVplsPeerStatisticsInfoRxPackets_Object=MibTableColumn
sleMplsTpVplsPeerStatisticsInfoRxPackets=_SleMplsTpVplsPeerStatisticsInfoRxPackets_Object((1,3,6,1,4,1,6296,101,16,16,6,2,1,1,3),_SleMplsTpVplsPeerStatisticsInfoRxPackets_Type())
sleMplsTpVplsPeerStatisticsInfoRxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpVplsPeerStatisticsInfoRxPackets.setStatus(_A)
_SleMplsTpVplsPeerStatisticsInfoRxBytes_Type=Counter64
_SleMplsTpVplsPeerStatisticsInfoRxBytes_Object=MibTableColumn
sleMplsTpVplsPeerStatisticsInfoRxBytes=_SleMplsTpVplsPeerStatisticsInfoRxBytes_Object((1,3,6,1,4,1,6296,101,16,16,6,2,1,1,4),_SleMplsTpVplsPeerStatisticsInfoRxBytes_Type())
sleMplsTpVplsPeerStatisticsInfoRxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpVplsPeerStatisticsInfoRxBytes.setStatus(_A)
_SleMplsTpVplsStatisticsCfgControl_ObjectIdentity=ObjectIdentity
sleMplsTpVplsStatisticsCfgControl=_SleMplsTpVplsStatisticsCfgControl_ObjectIdentity((1,3,6,1,4,1,6296,101,16,16,6,3))
class _SleMplsTpVplsStatisticsCfgControlRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('clearVplsStatistics',1))
_SleMplsTpVplsStatisticsCfgControlRequest_Type.__name__=_D
_SleMplsTpVplsStatisticsCfgControlRequest_Object=MibScalar
sleMplsTpVplsStatisticsCfgControlRequest=_SleMplsTpVplsStatisticsCfgControlRequest_Object((1,3,6,1,4,1,6296,101,16,16,6,3,1),_SleMplsTpVplsStatisticsCfgControlRequest_Type())
sleMplsTpVplsStatisticsCfgControlRequest.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpVplsStatisticsCfgControlRequest.setStatus(_A)
_SleMplsTpVplsStatisticsCfgControlStatus_Type=SleControlStatusType
_SleMplsTpVplsStatisticsCfgControlStatus_Object=MibScalar
sleMplsTpVplsStatisticsCfgControlStatus=_SleMplsTpVplsStatisticsCfgControlStatus_Object((1,3,6,1,4,1,6296,101,16,16,6,3,2),_SleMplsTpVplsStatisticsCfgControlStatus_Type())
sleMplsTpVplsStatisticsCfgControlStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpVplsStatisticsCfgControlStatus.setStatus(_A)
_SleMplsTpVplsStatisticsCfgControlTimer_Type=Gauge32
_SleMplsTpVplsStatisticsCfgControlTimer_Object=MibScalar
sleMplsTpVplsStatisticsCfgControlTimer=_SleMplsTpVplsStatisticsCfgControlTimer_Object((1,3,6,1,4,1,6296,101,16,16,6,3,3),_SleMplsTpVplsStatisticsCfgControlTimer_Type())
sleMplsTpVplsStatisticsCfgControlTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpVplsStatisticsCfgControlTimer.setStatus(_A)
_SleMplsTpVplsStatisticsCfgControlTimestamp_Type=TimeTicks
_SleMplsTpVplsStatisticsCfgControlTimestamp_Object=MibScalar
sleMplsTpVplsStatisticsCfgControlTimestamp=_SleMplsTpVplsStatisticsCfgControlTimestamp_Object((1,3,6,1,4,1,6296,101,16,16,6,3,4),_SleMplsTpVplsStatisticsCfgControlTimestamp_Type())
sleMplsTpVplsStatisticsCfgControlTimestamp.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpVplsStatisticsCfgControlTimestamp.setStatus(_A)
_SleMplsTpVplsStatisticsCfgControlReqResult_Type=SleControlRequestResultType
_SleMplsTpVplsStatisticsCfgControlReqResult_Object=MibScalar
sleMplsTpVplsStatisticsCfgControlReqResult=_SleMplsTpVplsStatisticsCfgControlReqResult_Object((1,3,6,1,4,1,6296,101,16,16,6,3,5),_SleMplsTpVplsStatisticsCfgControlReqResult_Type())
sleMplsTpVplsStatisticsCfgControlReqResult.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpVplsStatisticsCfgControlReqResult.setStatus(_A)
_SleMplsTpVplsStatisticsCfgControlVplsId_Type=Unsigned32
_SleMplsTpVplsStatisticsCfgControlVplsId_Object=MibScalar
sleMplsTpVplsStatisticsCfgControlVplsId=_SleMplsTpVplsStatisticsCfgControlVplsId_Object((1,3,6,1,4,1,6296,101,16,16,6,3,6),_SleMplsTpVplsStatisticsCfgControlVplsId_Type())
sleMplsTpVplsStatisticsCfgControlVplsId.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpVplsStatisticsCfgControlVplsId.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'sleMpls':sleMpls,'sleMplsTpVpls':sleMplsTpVpls,'sleMplsTpVplsCfg':sleMplsTpVplsCfg,'sleMplsTpVplsCfgInfoTable':sleMplsTpVplsCfgInfoTable,'sleMplsTpVplsCfgInfoEntry':sleMplsTpVplsCfgInfoEntry,_F:sleMplsTpVplsCfgInfoId,'sleMplsTpVplsCfgInfoName':sleMplsTpVplsCfgInfoName,'sleMplsTpVplsCfgInfoMacLearning':sleMplsTpVplsCfgInfoMacLearning,'sleMplsTpVplsCfgInfoMacLearningLimit':sleMplsTpVplsCfgInfoMacLearningLimit,'sleMplsTpVplsCfgInfoServiceType':sleMplsTpVplsCfgInfoServiceType,'sleMplsTpVplsCfgInfoSignallingProto':sleMplsTpVplsCfgInfoSignallingProto,'sleMplsTpVplsCfgInfoGroupId':sleMplsTpVplsCfgInfoGroupId,'sleMplsTpVplsCfgInfoDescription':sleMplsTpVplsCfgInfoDescription,'sleMplsTpVplsCfgInfoMtu':sleMplsTpVplsCfgInfoMtu,'sleMplsTpVplsCfgControl':sleMplsTpVplsCfgControl,'sleMplsTpVplsCfgControlRequest':sleMplsTpVplsCfgControlRequest,'sleMplsTpVplsCfgControlStatus':sleMplsTpVplsCfgControlStatus,'sleMplsTpVplsCfgControlTimer':sleMplsTpVplsCfgControlTimer,'sleMplsTpVplsCfgControlTimestamp':sleMplsTpVplsCfgControlTimestamp,'sleMplsTpVplsCfgControlReqResult':sleMplsTpVplsCfgControlReqResult,'sleMplsTpVplsCfgControlId':sleMplsTpVplsCfgControlId,'sleMplsTpVplsCfgControlName':sleMplsTpVplsCfgControlName,'sleMplsTpVplsCfgControlMacLearningLimit':sleMplsTpVplsCfgControlMacLearningLimit,'sleMplsTpVplsCfgControlServiceType':sleMplsTpVplsCfgControlServiceType,'sleMplsTpVplsCfgControlGroupId':sleMplsTpVplsCfgControlGroupId,'sleMplsTpVplsCfgControlDescription':sleMplsTpVplsCfgControlDescription,'sleMplsTpVplsCfgControlMtu':sleMplsTpVplsCfgControlMtu,'sleMplsTpVplsIfCfg':sleMplsTpVplsIfCfg,'sleMplsTpVplsIfCfgInfoTable':sleMplsTpVplsIfCfgInfoTable,'sleMplsTpVplsIfCfgInfoEntry':sleMplsTpVplsIfCfgInfoEntry,_K:sleMplsTpVplsIfCfgInfoIfIndex,_J:sleMplsTpVplsIfCfgInfoName,'sleMplsTpVplsIfCfgInfoServiceType':sleMplsTpVplsIfCfgInfoServiceType,'sleMplsTpVplsIfCfgInfoVlanId':sleMplsTpVplsIfCfgInfoVlanId,'sleMplsTpVplsIfCfgInfoInnerVlanId':sleMplsTpVplsIfCfgInfoInnerVlanId,'sleMplsTpVplsIfCfgInfoAction':sleMplsTpVplsIfCfgInfoAction,'sleMplsTpVplsIfCfgControl':sleMplsTpVplsIfCfgControl,'sleMplsTpVplsIfCfgControlRequest':sleMplsTpVplsIfCfgControlRequest,'sleMplsTpVplsIfCfgControlStatus':sleMplsTpVplsIfCfgControlStatus,'sleMplsTpVplsIfCfgControlTimer':sleMplsTpVplsIfCfgControlTimer,'sleMplsTpVplsIfCfgControlTimestamp':sleMplsTpVplsIfCfgControlTimestamp,'sleMplsTpVplsIfCfgControlReqResult':sleMplsTpVplsIfCfgControlReqResult,'sleMplsTpVplsIfCfgControlIfIndex':sleMplsTpVplsIfCfgControlIfIndex,'sleMplsTpVplsIfCfgControlName':sleMplsTpVplsIfCfgControlName,'sleMplsTpVplsIfCfgControlServiceType':sleMplsTpVplsIfCfgControlServiceType,'sleMplsTpVplsIfCfgControlVlanId':sleMplsTpVplsIfCfgControlVlanId,'sleMplsTpVplsIfCfgControlInnerVlanId':sleMplsTpVplsIfCfgControlInnerVlanId,'sleMplsTpVplsIfCfgControlAction':sleMplsTpVplsIfCfgControlAction,'sleMplsTpVplsMeshCfg':sleMplsTpVplsMeshCfg,'sleMplsTpVplsMeshCfgInfoTable':sleMplsTpVplsMeshCfgInfoTable,'sleMplsTpVplsMeshCfgInfoEntry':sleMplsTpVplsMeshCfgInfoEntry,_L:sleMplsTpVplsMeshCfgInfoPeerNodeId,'sleMplsTpVplsMeshCfgInfoPeerNodeType':sleMplsTpVplsMeshCfgInfoPeerNodeType,'sleMplsTpVplsMeshCfgInfoPeerGlobalId':sleMplsTpVplsMeshCfgInfoPeerGlobalId,'sleMplsTpVplsMeshCfgInfoPeerCc':sleMplsTpVplsMeshCfgInfoPeerCc,'sleMplsTpVplsMeshCfgInfoPeerIcc':sleMplsTpVplsMeshCfgInfoPeerIcc,'sleMplsTpVplsMeshCfgInfoTunnelId':sleMplsTpVplsMeshCfgInfoTunnelId,'sleMplsTpVplsMeshCfgInfoTunnelName':sleMplsTpVplsMeshCfgInfoTunnelName,'sleMplsTpVplsMeshCfgInfoOwner':sleMplsTpVplsMeshCfgInfoOwner,'sleMplsTpVplsMeshCfgInfoTunnelPath':sleMplsTpVplsMeshCfgInfoTunnelPath,'sleMplsTpVplsMeshCfgInfoInLabel':sleMplsTpVplsMeshCfgInfoInLabel,'sleMplsTpVplsMeshCfgInfoOutLabel':sleMplsTpVplsMeshCfgInfoOutLabel,'sleMplsTpVplsMeshCfgInfoOutInterface':sleMplsTpVplsMeshCfgInfoOutInterface,'sleMplsTpVplsMeshCfgInfoTunnelLabel':sleMplsTpVplsMeshCfgInfoTunnelLabel,'sleMplsTpVplsMeshCfgInfoState':sleMplsTpVplsMeshCfgInfoState,'sleMplsTpVplsMeshCfgInfoQosServicePolicy':sleMplsTpVplsMeshCfgInfoQosServicePolicy,'sleMplsTpVplsMeshCfgControl':sleMplsTpVplsMeshCfgControl,'sleMplsTpVplsMeshCfgControlRequest':sleMplsTpVplsMeshCfgControlRequest,'sleMplsTpVplsMeshCfgControlStatus':sleMplsTpVplsMeshCfgControlStatus,'sleMplsTpVplsMeshCfgControlTimer':sleMplsTpVplsMeshCfgControlTimer,'sleMplsTpVplsMeshCfgControlTimestamp':sleMplsTpVplsMeshCfgControlTimestamp,'sleMplsTpVplsMeshCfgControlReqResult':sleMplsTpVplsMeshCfgControlReqResult,'sleMplsTpVplsMeshCfgControlVplsId':sleMplsTpVplsMeshCfgControlVplsId,'sleMplsTpVplsMeshCfgControlPeerNodeId':sleMplsTpVplsMeshCfgControlPeerNodeId,'sleMplsTpVplsMeshCfgControlPeerNodeType':sleMplsTpVplsMeshCfgControlPeerNodeType,'sleMplsTpVplsMeshCfgControlPeerGlobalId':sleMplsTpVplsMeshCfgControlPeerGlobalId,'sleMplsTpVplsMeshCfgControlPeerCc':sleMplsTpVplsMeshCfgControlPeerCc,'sleMplsTpVplsMeshCfgControlPeerIcc':sleMplsTpVplsMeshCfgControlPeerIcc,'sleMplsTpVplsMeshCfgControlTunnelId':sleMplsTpVplsMeshCfgControlTunnelId,'sleMplsTpVplsMeshCfgControlTunnelName':sleMplsTpVplsMeshCfgControlTunnelName,'sleMplsTpVplsMeshCfgControlOwner':sleMplsTpVplsMeshCfgControlOwner,'sleMplsTpVplsMeshCfgControlTunnelPath':sleMplsTpVplsMeshCfgControlTunnelPath,'sleMplsTpVplsMeshCfgControlInLabel':sleMplsTpVplsMeshCfgControlInLabel,'sleMplsTpVplsMeshCfgControlOutLabel':sleMplsTpVplsMeshCfgControlOutLabel,'sleMplsTpVplsMeshCfgControlQosServicePolicy':sleMplsTpVplsMeshCfgControlQosServicePolicy,'sleMplsTpVplsSpokeCfg':sleMplsTpVplsSpokeCfg,'sleMplsTpVplsSpokeCfgInfoTable':sleMplsTpVplsSpokeCfgInfoTable,'sleMplsTpVplsSpokeCfgInfoEntry':sleMplsTpVplsSpokeCfgInfoEntry,_W:sleMplsTpVplsSpokeCfgInfoVcName,'sleMplsTpVplsSpokeCfgInfoTunnelName':sleMplsTpVplsSpokeCfgInfoTunnelName,'sleMplsTpVplsSpokeCfgInfoServiceType':sleMplsTpVplsSpokeCfgInfoServiceType,'sleMplsTpVplsSpokeCfgInfoInLabel':sleMplsTpVplsSpokeCfgInfoInLabel,'sleMplsTpVplsSpokeCfgInfoOutLabel':sleMplsTpVplsSpokeCfgInfoOutLabel,'sleMplsTpVplsSpokeCfgInfoOutInterface':sleMplsTpVplsSpokeCfgInfoOutInterface,'sleMplsTpVplsSpokeCfgInfoState':sleMplsTpVplsSpokeCfgInfoState,'sleMplsTpVplsSpokeCfgInfoQosServicePolicy':sleMplsTpVplsSpokeCfgInfoQosServicePolicy,'sleMplsTpVplsSpokeCfgControl':sleMplsTpVplsSpokeCfgControl,'sleMplsTpVplsSpokeCfgControlRequest':sleMplsTpVplsSpokeCfgControlRequest,'sleMplsTpVplsSpokeCfgControlStatus':sleMplsTpVplsSpokeCfgControlStatus,'sleMplsTpVplsSpokeCfgControlTimer':sleMplsTpVplsSpokeCfgControlTimer,'sleMplsTpVplsSpokeCfgControlTimestamp':sleMplsTpVplsSpokeCfgControlTimestamp,'sleMplsTpVplsSpokeCfgControlReqResult':sleMplsTpVplsSpokeCfgControlReqResult,'sleMplsTpVplsSpokeCfgControlVplsId':sleMplsTpVplsSpokeCfgControlVplsId,'sleMplsTpVplsSpokeCfgControlVcName':sleMplsTpVplsSpokeCfgControlVcName,'sleMplsTpVplsSpokeCfgControlTunnelName':sleMplsTpVplsSpokeCfgControlTunnelName,'sleMplsTpVplsSpokeCfgControlServiceType':sleMplsTpVplsSpokeCfgControlServiceType,'sleMplsTpVplsSpokeCfgControlInLabel':sleMplsTpVplsSpokeCfgControlInLabel,'sleMplsTpVplsSpokeCfgControlOutLabel':sleMplsTpVplsSpokeCfgControlOutLabel,'sleMplsTpVplsSpokeCfgControlOutInterface':sleMplsTpVplsSpokeCfgControlOutInterface,'sleMplsTpVplsSpokeCfgControlQosServicePolicy':sleMplsTpVplsSpokeCfgControlQosServicePolicy,'sleMplsTpVplsMacLearning':sleMplsTpVplsMacLearning,'sleMplsTpVplsMacLearningInfoTable':sleMplsTpVplsMacLearningInfoTable,'sleMplsTpVplsMacLearningInfoEntry':sleMplsTpVplsMacLearningInfoEntry,_X:sleMplsTpVplsMacLearningInfoMacAddress,'sleMplsTpVplsMacLearningInfoInterfacIndex':sleMplsTpVplsMacLearningInfoInterfacIndex,'sleMplsTpVplsMacLearningInfoMeshAddress':sleMplsTpVplsMacLearningInfoMeshAddress,'sleMplsTpVplsMacLearningControl':sleMplsTpVplsMacLearningControl,'sleMplsTpVplsMacLearningControlRequest':sleMplsTpVplsMacLearningControlRequest,'sleMplsTpVplsMacLearningControlStatus':sleMplsTpVplsMacLearningControlStatus,'sleMplsTpVplsMacLearningControlTimer':sleMplsTpVplsMacLearningControlTimer,'sleMplsTpVplsMacLearningControlTimestamp':sleMplsTpVplsMacLearningControlTimestamp,'sleMplsTpVplsMacLearningControlReqResult':sleMplsTpVplsMacLearningControlReqResult,'sleMplsTpVplsMacLearningControlVplsId':sleMplsTpVplsMacLearningControlVplsId,'sleMplsTpVplsStatistics':sleMplsTpVplsStatistics,'sleMplsTpVplsAcStatistics':sleMplsTpVplsAcStatistics,'sleMplsTpVplsAcStatisticsInfoTable':sleMplsTpVplsAcStatisticsInfoTable,'sleMplsTpVplsAcStatisticsInfoEntry':sleMplsTpVplsAcStatisticsInfoEntry,'sleMplsTpVplsAcStatisticsInfoTxPackets':sleMplsTpVplsAcStatisticsInfoTxPackets,'sleMplsTpVplsAcStatisticsInfoTxBytes':sleMplsTpVplsAcStatisticsInfoTxBytes,'sleMplsTpVplsAcStatisticsInfoRxPackets':sleMplsTpVplsAcStatisticsInfoRxPackets,'sleMplsTpVplsAcStatisticsInfoRxBytes':sleMplsTpVplsAcStatisticsInfoRxBytes,'sleMplsTpVplsPeerStatistics':sleMplsTpVplsPeerStatistics,'sleMplsTpVplsPeerStatisticsInfoTable':sleMplsTpVplsPeerStatisticsInfoTable,'sleMplsTpVplsPeerStatisticsInfoEntry':sleMplsTpVplsPeerStatisticsInfoEntry,'sleMplsTpVplsPeerStatisticsInfoTxPackets':sleMplsTpVplsPeerStatisticsInfoTxPackets,'sleMplsTpVplsPeerStatisticsInfoTxBytes':sleMplsTpVplsPeerStatisticsInfoTxBytes,'sleMplsTpVplsPeerStatisticsInfoRxPackets':sleMplsTpVplsPeerStatisticsInfoRxPackets,'sleMplsTpVplsPeerStatisticsInfoRxBytes':sleMplsTpVplsPeerStatisticsInfoRxBytes,'sleMplsTpVplsStatisticsCfgControl':sleMplsTpVplsStatisticsCfgControl,'sleMplsTpVplsStatisticsCfgControlRequest':sleMplsTpVplsStatisticsCfgControlRequest,'sleMplsTpVplsStatisticsCfgControlStatus':sleMplsTpVplsStatisticsCfgControlStatus,'sleMplsTpVplsStatisticsCfgControlTimer':sleMplsTpVplsStatisticsCfgControlTimer,'sleMplsTpVplsStatisticsCfgControlTimestamp':sleMplsTpVplsStatisticsCfgControlTimestamp,'sleMplsTpVplsStatisticsCfgControlReqResult':sleMplsTpVplsStatisticsCfgControlReqResult,'sleMplsTpVplsStatisticsCfgControlVplsId':sleMplsTpVplsStatisticsCfgControlVplsId})