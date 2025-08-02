_Z='sleMplsTpMsPwCfgInfoName'
_Y='replace'
_X='remove'
_W='addSvlan'
_V='sleMplsTpPwIfCfgInfoVcName'
_U='sleMplsTpPwIfCfgInfoIndex'
_T='sleMplsTpPwAcCfgInfoIndex'
_S='enable'
_R='pwTaggedMode'
_Q='pwRawMode'
_P='l2tpControlProtocol'
_O='genFecSignaling'
_N='pwIdFecSignaling'
_M='manual'
_L='sleMplsTpPwCfgInfoId'
_K='VlanIdOrAnyOrNone'
_J='PwIDType'
_I='not-accessible'
_H='secondary'
_G='primary'
_F='SLE-MPLS-TP-PW-MIB'
_E='OctetString'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
sleMgmt,=mibBuilder.importSymbols('DASAN-SMI','sleMgmt')
IANAPwTypeTC,=mibBuilder.importSymbols('IANA-PWE3-MIB','IANAPwTypeTC')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
MplsCcId,MplsIccId=mibBuilder.importSymbols('MPLS-TC-EXT-STD-MIB','MplsCcId','MplsIccId')
MplsLabel,=mibBuilder.importSymbols('MPLS-TC-STD-MIB','MplsLabel')
PwGroupID,PwIDType=mibBuilder.importSymbols('PW-TC-STD-MIB','PwGroupID',_J)
VlanIdOrAnyOrNone,=mibBuilder.importSymbols('Q-BRIDGE-MIB',_K)
SleControlRequestResultType,SleControlStatusType=mibBuilder.importSymbols('SLE-TC-MIB','SleControlRequestResultType','SleControlStatusType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,transmission=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','transmission')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
sleMplsTpPw=ModuleIdentity((1,3,6,1,4,1,6296,101,16,15))
if mibBuilder.loadTexts:sleMplsTpPw.setRevisions(('2015-11-03 00:00',))
_SleMpls_ObjectIdentity=ObjectIdentity
sleMpls=_SleMpls_ObjectIdentity((1,3,6,1,4,1,6296,101,16))
if mibBuilder.loadTexts:sleMpls.setStatus(_A)
_SleMplsTpPwCfg_ObjectIdentity=ObjectIdentity
sleMplsTpPwCfg=_SleMplsTpPwCfg_ObjectIdentity((1,3,6,1,4,1,6296,101,16,15,1))
_SleMplsTpPwCfgInfoTable_Object=MibTable
sleMplsTpPwCfgInfoTable=_SleMplsTpPwCfgInfoTable_Object((1,3,6,1,4,1,6296,101,16,15,1,1))
if mibBuilder.loadTexts:sleMplsTpPwCfgInfoTable.setStatus(_A)
_SleMplsTpPwCfgInfoEntry_Object=MibTableRow
sleMplsTpPwCfgInfoEntry=_SleMplsTpPwCfgInfoEntry_Object((1,3,6,1,4,1,6296,101,16,15,1,1,1))
sleMplsTpPwCfgInfoEntry.setIndexNames((0,_F,_L))
if mibBuilder.loadTexts:sleMplsTpPwCfgInfoEntry.setStatus(_A)
class _SleMplsTpPwCfgInfoId_Type(PwIDType):subtypeSpec=PwIDType.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SleMplsTpPwCfgInfoId_Type.__name__=_J
_SleMplsTpPwCfgInfoId_Object=MibTableColumn
sleMplsTpPwCfgInfoId=_SleMplsTpPwCfgInfoId_Object((1,3,6,1,4,1,6296,101,16,15,1,1,1,1),_SleMplsTpPwCfgInfoId_Type())
sleMplsTpPwCfgInfoId.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpPwCfgInfoId.setStatus(_A)
_SleMplsTpPwCfgInfoName_Type=OctetString
_SleMplsTpPwCfgInfoName_Object=MibTableColumn
sleMplsTpPwCfgInfoName=_SleMplsTpPwCfgInfoName_Object((1,3,6,1,4,1,6296,101,16,15,1,1,1,2),_SleMplsTpPwCfgInfoName_Type())
sleMplsTpPwCfgInfoName.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpPwCfgInfoName.setStatus(_A)
class _SleMplsTpPwCfgInfoOwner_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3),(_P,4),('other',5)))
_SleMplsTpPwCfgInfoOwner_Type.__name__=_D
_SleMplsTpPwCfgInfoOwner_Object=MibTableColumn
sleMplsTpPwCfgInfoOwner=_SleMplsTpPwCfgInfoOwner_Object((1,3,6,1,4,1,6296,101,16,15,1,1,1,3),_SleMplsTpPwCfgInfoOwner_Type())
sleMplsTpPwCfgInfoOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpPwCfgInfoOwner.setStatus(_A)
_SleMplsTpPwCfgInfoType_Type=IANAPwTypeTC
_SleMplsTpPwCfgInfoType_Object=MibTableColumn
sleMplsTpPwCfgInfoType=_SleMplsTpPwCfgInfoType_Object((1,3,6,1,4,1,6296,101,16,15,1,1,1,4),_SleMplsTpPwCfgInfoType_Type())
sleMplsTpPwCfgInfoType.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpPwCfgInfoType.setStatus(_A)
_SleMplsTpPwCfgInfoControlWord_Type=Integer32
_SleMplsTpPwCfgInfoControlWord_Object=MibTableColumn
sleMplsTpPwCfgInfoControlWord=_SleMplsTpPwCfgInfoControlWord_Object((1,3,6,1,4,1,6296,101,16,15,1,1,1,5),_SleMplsTpPwCfgInfoControlWord_Type())
sleMplsTpPwCfgInfoControlWord.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpPwCfgInfoControlWord.setStatus(_A)
class _SleMplsTpPwCfgInfoPeerIdType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ietf',1),('itut',2)))
_SleMplsTpPwCfgInfoPeerIdType_Type.__name__=_D
_SleMplsTpPwCfgInfoPeerIdType_Object=MibTableColumn
sleMplsTpPwCfgInfoPeerIdType=_SleMplsTpPwCfgInfoPeerIdType_Object((1,3,6,1,4,1,6296,101,16,15,1,1,1,6),_SleMplsTpPwCfgInfoPeerIdType_Type())
sleMplsTpPwCfgInfoPeerIdType.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpPwCfgInfoPeerIdType.setStatus(_A)
_SleMplsTpPwCfgInfoPeerGolbalId_Type=Unsigned32
_SleMplsTpPwCfgInfoPeerGolbalId_Object=MibTableColumn
sleMplsTpPwCfgInfoPeerGolbalId=_SleMplsTpPwCfgInfoPeerGolbalId_Object((1,3,6,1,4,1,6296,101,16,15,1,1,1,7),_SleMplsTpPwCfgInfoPeerGolbalId_Type())
sleMplsTpPwCfgInfoPeerGolbalId.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpPwCfgInfoPeerGolbalId.setStatus(_A)
_SleMplsTpPwCfgInfoPeerCc_Type=MplsCcId
_SleMplsTpPwCfgInfoPeerCc_Object=MibTableColumn
sleMplsTpPwCfgInfoPeerCc=_SleMplsTpPwCfgInfoPeerCc_Object((1,3,6,1,4,1,6296,101,16,15,1,1,1,8),_SleMplsTpPwCfgInfoPeerCc_Type())
sleMplsTpPwCfgInfoPeerCc.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpPwCfgInfoPeerCc.setStatus(_A)
_SleMplsTpPwCfgInfoPeerIcc_Type=MplsIccId
_SleMplsTpPwCfgInfoPeerIcc_Object=MibTableColumn
sleMplsTpPwCfgInfoPeerIcc=_SleMplsTpPwCfgInfoPeerIcc_Object((1,3,6,1,4,1,6296,101,16,15,1,1,1,9),_SleMplsTpPwCfgInfoPeerIcc_Type())
sleMplsTpPwCfgInfoPeerIcc.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpPwCfgInfoPeerIcc.setStatus(_A)
_SleMplsTpPwCfgInfoPeerNodeId_Type=IpAddress
_SleMplsTpPwCfgInfoPeerNodeId_Object=MibTableColumn
sleMplsTpPwCfgInfoPeerNodeId=_SleMplsTpPwCfgInfoPeerNodeId_Object((1,3,6,1,4,1,6296,101,16,15,1,1,1,10),_SleMplsTpPwCfgInfoPeerNodeId_Type())
sleMplsTpPwCfgInfoPeerNodeId.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpPwCfgInfoPeerNodeId.setStatus(_A)
_SleMplsTpPwCfgInfoPeerAcId_Type=Unsigned32
_SleMplsTpPwCfgInfoPeerAcId_Object=MibTableColumn
sleMplsTpPwCfgInfoPeerAcId=_SleMplsTpPwCfgInfoPeerAcId_Object((1,3,6,1,4,1,6296,101,16,15,1,1,1,11),_SleMplsTpPwCfgInfoPeerAcId_Type())
sleMplsTpPwCfgInfoPeerAcId.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpPwCfgInfoPeerAcId.setStatus(_A)
_SleMplsTpPwCfgInfoGroupName_Type=SnmpAdminString
_SleMplsTpPwCfgInfoGroupName_Object=MibTableColumn
sleMplsTpPwCfgInfoGroupName=_SleMplsTpPwCfgInfoGroupName_Object((1,3,6,1,4,1,6296,101,16,15,1,1,1,12),_SleMplsTpPwCfgInfoGroupName_Type())
sleMplsTpPwCfgInfoGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpPwCfgInfoGroupName.setStatus(_A)
_SleMplsTpPwCfgInfoGroupId_Type=PwGroupID
_SleMplsTpPwCfgInfoGroupId_Object=MibTableColumn
sleMplsTpPwCfgInfoGroupId=_SleMplsTpPwCfgInfoGroupId_Object((1,3,6,1,4,1,6296,101,16,15,1,1,1,13),_SleMplsTpPwCfgInfoGroupId_Type())
sleMplsTpPwCfgInfoGroupId.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpPwCfgInfoGroupId.setStatus(_A)
class _SleMplsTpPwCfgInfoOperMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),(_Q,1),(_R,2)))
_SleMplsTpPwCfgInfoOperMode_Type.__name__=_D
_SleMplsTpPwCfgInfoOperMode_Object=MibTableColumn
sleMplsTpPwCfgInfoOperMode=_SleMplsTpPwCfgInfoOperMode_Object((1,3,6,1,4,1,6296,101,16,15,1,1,1,14),_SleMplsTpPwCfgInfoOperMode_Type())
sleMplsTpPwCfgInfoOperMode.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpPwCfgInfoOperMode.setStatus(_A)
class _SleMplsTpPwCfgInfoSvlanId_Type(VlanIdOrAnyOrNone):defaultValue=0
_SleMplsTpPwCfgInfoSvlanId_Type.__name__=_K
_SleMplsTpPwCfgInfoSvlanId_Object=MibTableColumn
sleMplsTpPwCfgInfoSvlanId=_SleMplsTpPwCfgInfoSvlanId_Object((1,3,6,1,4,1,6296,101,16,15,1,1,1,15),_SleMplsTpPwCfgInfoSvlanId_Type())
sleMplsTpPwCfgInfoSvlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpPwCfgInfoSvlanId.setStatus(_A)
class _SleMplsTpPwCfgInfoPwStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_S,1))
_SleMplsTpPwCfgInfoPwStatus_Type.__name__=_D
_SleMplsTpPwCfgInfoPwStatus_Object=MibTableColumn
sleMplsTpPwCfgInfoPwStatus=_SleMplsTpPwCfgInfoPwStatus_Object((1,3,6,1,4,1,6296,101,16,15,1,1,1,17),_SleMplsTpPwCfgInfoPwStatus_Type())
sleMplsTpPwCfgInfoPwStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpPwCfgInfoPwStatus.setStatus(_A)
_SleMplsTpPwCfgInfoInlabel_Type=MplsLabel
_SleMplsTpPwCfgInfoInlabel_Object=MibTableColumn
sleMplsTpPwCfgInfoInlabel=_SleMplsTpPwCfgInfoInlabel_Object((1,3,6,1,4,1,6296,101,16,15,1,1,1,18),_SleMplsTpPwCfgInfoInlabel_Type())
sleMplsTpPwCfgInfoInlabel.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpPwCfgInfoInlabel.setStatus(_A)
_SleMplsTpPwCfgInfoOutLabel_Type=MplsLabel
_SleMplsTpPwCfgInfoOutLabel_Object=MibTableColumn
sleMplsTpPwCfgInfoOutLabel=_SleMplsTpPwCfgInfoOutLabel_Object((1,3,6,1,4,1,6296,101,16,15,1,1,1,19),_SleMplsTpPwCfgInfoOutLabel_Type())
sleMplsTpPwCfgInfoOutLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpPwCfgInfoOutLabel.setStatus(_A)
class _SleMplsTpPwCfgInfoTunnelName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(1,16))
_SleMplsTpPwCfgInfoTunnelName_Type.__name__=_E
_SleMplsTpPwCfgInfoTunnelName_Object=MibTableColumn
sleMplsTpPwCfgInfoTunnelName=_SleMplsTpPwCfgInfoTunnelName_Object((1,3,6,1,4,1,6296,101,16,15,1,1,1,20),_SleMplsTpPwCfgInfoTunnelName_Type())
sleMplsTpPwCfgInfoTunnelName.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpPwCfgInfoTunnelName.setStatus(_A)
_SleMplsTpPwCfgInfoAcInterfaceIndex_Type=InterfaceIndexOrZero
_SleMplsTpPwCfgInfoAcInterfaceIndex_Object=MibTableColumn
sleMplsTpPwCfgInfoAcInterfaceIndex=_SleMplsTpPwCfgInfoAcInterfaceIndex_Object((1,3,6,1,4,1,6296,101,16,15,1,1,1,21),_SleMplsTpPwCfgInfoAcInterfaceIndex_Type())
sleMplsTpPwCfgInfoAcInterfaceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpPwCfgInfoAcInterfaceIndex.setStatus(_A)
_SleMplsTpPwCfgInfoVcStitchName_Type=OctetString
_SleMplsTpPwCfgInfoVcStitchName_Object=MibTableColumn
sleMplsTpPwCfgInfoVcStitchName=_SleMplsTpPwCfgInfoVcStitchName_Object((1,3,6,1,4,1,6296,101,16,15,1,1,1,22),_SleMplsTpPwCfgInfoVcStitchName_Type())
sleMplsTpPwCfgInfoVcStitchName.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpPwCfgInfoVcStitchName.setStatus(_A)
class _SleMplsTpPwCfgInfoPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SleMplsTpPwCfgInfoPriority_Type.__name__=_D
_SleMplsTpPwCfgInfoPriority_Object=MibTableColumn
sleMplsTpPwCfgInfoPriority=_SleMplsTpPwCfgInfoPriority_Object((1,3,6,1,4,1,6296,101,16,15,1,1,1,23),_SleMplsTpPwCfgInfoPriority_Type())
sleMplsTpPwCfgInfoPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpPwCfgInfoPriority.setStatus(_A)
class _SleMplsTpPwCfgInfostate_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_SleMplsTpPwCfgInfostate_Type.__name__=_D
_SleMplsTpPwCfgInfostate_Object=MibTableColumn
sleMplsTpPwCfgInfostate=_SleMplsTpPwCfgInfostate_Object((1,3,6,1,4,1,6296,101,16,15,1,1,1,24),_SleMplsTpPwCfgInfostate_Type())
sleMplsTpPwCfgInfostate.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpPwCfgInfostate.setStatus(_A)
_SleMplsTpPwCfgInfoDescription_Type=OctetString
_SleMplsTpPwCfgInfoDescription_Object=MibTableColumn
sleMplsTpPwCfgInfoDescription=_SleMplsTpPwCfgInfoDescription_Object((1,3,6,1,4,1,6296,101,16,15,1,1,1,25),_SleMplsTpPwCfgInfoDescription_Type())
sleMplsTpPwCfgInfoDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpPwCfgInfoDescription.setStatus(_A)
class _SleMplsTpPwCfgInfoLocalRefreshTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SleMplsTpPwCfgInfoLocalRefreshTimer_Type.__name__=_D
_SleMplsTpPwCfgInfoLocalRefreshTimer_Object=MibTableColumn
sleMplsTpPwCfgInfoLocalRefreshTimer=_SleMplsTpPwCfgInfoLocalRefreshTimer_Object((1,3,6,1,4,1,6296,101,16,15,1,1,1,26),_SleMplsTpPwCfgInfoLocalRefreshTimer_Type())
sleMplsTpPwCfgInfoLocalRefreshTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpPwCfgInfoLocalRefreshTimer.setStatus(_A)
_SleMplsTpPwCfgInfoQosServicePolicy_Type=OctetString
_SleMplsTpPwCfgInfoQosServicePolicy_Object=MibTableColumn
sleMplsTpPwCfgInfoQosServicePolicy=_SleMplsTpPwCfgInfoQosServicePolicy_Object((1,3,6,1,4,1,6296,101,16,15,1,1,1,27),_SleMplsTpPwCfgInfoQosServicePolicy_Type())
sleMplsTpPwCfgInfoQosServicePolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpPwCfgInfoQosServicePolicy.setStatus(_A)
_SleMplsTpPwCfgControl_ObjectIdentity=ObjectIdentity
sleMplsTpPwCfgControl=_SleMplsTpPwCfgControl_ObjectIdentity((1,3,6,1,4,1,6296,101,16,15,1,2))
class _SleMplsTpPwCfgControlRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*(('createPw',1),('createVpwsWithGroupId',2),('createRawModeVpwsWithGroupId',3),('createQInQVpwsWithGroupId',4),('createRawModeVpws',5),('createQInQVpws',6),('deletePw',7),('setPwFibEntry',8),('setPwVcStitchFibEntry',9),('unsetPwFibEntry',10),('setPwDescription',11),('createVpwswithPwStatus',12),('setPwQosServicePolicy',13),('unsetPwQosServicePolicy',14)))
_SleMplsTpPwCfgControlRequest_Type.__name__=_D
_SleMplsTpPwCfgControlRequest_Object=MibScalar
sleMplsTpPwCfgControlRequest=_SleMplsTpPwCfgControlRequest_Object((1,3,6,1,4,1,6296,101,16,15,1,2,1),_SleMplsTpPwCfgControlRequest_Type())
sleMplsTpPwCfgControlRequest.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpPwCfgControlRequest.setStatus(_A)
_SleMplsTpPwCfgControlStatus_Type=SleControlStatusType
_SleMplsTpPwCfgControlStatus_Object=MibScalar
sleMplsTpPwCfgControlStatus=_SleMplsTpPwCfgControlStatus_Object((1,3,6,1,4,1,6296,101,16,15,1,2,2),_SleMplsTpPwCfgControlStatus_Type())
sleMplsTpPwCfgControlStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpPwCfgControlStatus.setStatus(_A)
_SleMplsTpPwCfgControlTimer_Type=Gauge32
_SleMplsTpPwCfgControlTimer_Object=MibScalar
sleMplsTpPwCfgControlTimer=_SleMplsTpPwCfgControlTimer_Object((1,3,6,1,4,1,6296,101,16,15,1,2,3),_SleMplsTpPwCfgControlTimer_Type())
sleMplsTpPwCfgControlTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpPwCfgControlTimer.setStatus(_A)
_SleMplsTpPwCfgControlTimestamp_Type=TimeTicks
_SleMplsTpPwCfgControlTimestamp_Object=MibScalar
sleMplsTpPwCfgControlTimestamp=_SleMplsTpPwCfgControlTimestamp_Object((1,3,6,1,4,1,6296,101,16,15,1,2,4),_SleMplsTpPwCfgControlTimestamp_Type())
sleMplsTpPwCfgControlTimestamp.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpPwCfgControlTimestamp.setStatus(_A)
_SleMplsTpPwCfgControlReqResult_Type=SleControlRequestResultType
_SleMplsTpPwCfgControlReqResult_Object=MibScalar
sleMplsTpPwCfgControlReqResult=_SleMplsTpPwCfgControlReqResult_Object((1,3,6,1,4,1,6296,101,16,15,1,2,5),_SleMplsTpPwCfgControlReqResult_Type())
sleMplsTpPwCfgControlReqResult.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpPwCfgControlReqResult.setStatus(_A)
_SleMplsTpPwCfgControlId_Type=PwIDType
_SleMplsTpPwCfgControlId_Object=MibScalar
sleMplsTpPwCfgControlId=_SleMplsTpPwCfgControlId_Object((1,3,6,1,4,1,6296,101,16,15,1,2,6),_SleMplsTpPwCfgControlId_Type())
sleMplsTpPwCfgControlId.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpPwCfgControlId.setStatus(_A)
_SleMplsTpPwCfgControlName_Type=OctetString
_SleMplsTpPwCfgControlName_Object=MibScalar
sleMplsTpPwCfgControlName=_SleMplsTpPwCfgControlName_Object((1,3,6,1,4,1,6296,101,16,15,1,2,7),_SleMplsTpPwCfgControlName_Type())
sleMplsTpPwCfgControlName.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpPwCfgControlName.setStatus(_A)
class _SleMplsTpPwCfgControlOwner_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3),(_P,4),('other',5)))
_SleMplsTpPwCfgControlOwner_Type.__name__=_D
_SleMplsTpPwCfgControlOwner_Object=MibScalar
sleMplsTpPwCfgControlOwner=_SleMplsTpPwCfgControlOwner_Object((1,3,6,1,4,1,6296,101,16,15,1,2,8),_SleMplsTpPwCfgControlOwner_Type())
sleMplsTpPwCfgControlOwner.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpPwCfgControlOwner.setStatus(_A)
class _SleMplsTpPwCfgControlPeerIdType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ietf',1),('itut',2)))
_SleMplsTpPwCfgControlPeerIdType_Type.__name__=_D
_SleMplsTpPwCfgControlPeerIdType_Object=MibScalar
sleMplsTpPwCfgControlPeerIdType=_SleMplsTpPwCfgControlPeerIdType_Object((1,3,6,1,4,1,6296,101,16,15,1,2,9),_SleMplsTpPwCfgControlPeerIdType_Type())
sleMplsTpPwCfgControlPeerIdType.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpPwCfgControlPeerIdType.setStatus(_A)
_SleMplsTpPwCfgControlPeerGolbalId_Type=Unsigned32
_SleMplsTpPwCfgControlPeerGolbalId_Object=MibScalar
sleMplsTpPwCfgControlPeerGolbalId=_SleMplsTpPwCfgControlPeerGolbalId_Object((1,3,6,1,4,1,6296,101,16,15,1,2,10),_SleMplsTpPwCfgControlPeerGolbalId_Type())
sleMplsTpPwCfgControlPeerGolbalId.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpPwCfgControlPeerGolbalId.setStatus(_A)
_SleMplsTpPwCfgControlPeerCc_Type=MplsCcId
_SleMplsTpPwCfgControlPeerCc_Object=MibScalar
sleMplsTpPwCfgControlPeerCc=_SleMplsTpPwCfgControlPeerCc_Object((1,3,6,1,4,1,6296,101,16,15,1,2,11),_SleMplsTpPwCfgControlPeerCc_Type())
sleMplsTpPwCfgControlPeerCc.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpPwCfgControlPeerCc.setStatus(_A)
_SleMplsTpPwCfgControlPeerIcc_Type=MplsIccId
_SleMplsTpPwCfgControlPeerIcc_Object=MibScalar
sleMplsTpPwCfgControlPeerIcc=_SleMplsTpPwCfgControlPeerIcc_Object((1,3,6,1,4,1,6296,101,16,15,1,2,12),_SleMplsTpPwCfgControlPeerIcc_Type())
sleMplsTpPwCfgControlPeerIcc.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpPwCfgControlPeerIcc.setStatus(_A)
_SleMplsTpPwCfgControlPeerNodeId_Type=IpAddress
_SleMplsTpPwCfgControlPeerNodeId_Object=MibScalar
sleMplsTpPwCfgControlPeerNodeId=_SleMplsTpPwCfgControlPeerNodeId_Object((1,3,6,1,4,1,6296,101,16,15,1,2,13),_SleMplsTpPwCfgControlPeerNodeId_Type())
sleMplsTpPwCfgControlPeerNodeId.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpPwCfgControlPeerNodeId.setStatus(_A)
_SleMplsTpPwCfgControlPeerAcId_Type=Unsigned32
_SleMplsTpPwCfgControlPeerAcId_Object=MibScalar
sleMplsTpPwCfgControlPeerAcId=_SleMplsTpPwCfgControlPeerAcId_Object((1,3,6,1,4,1,6296,101,16,15,1,2,14),_SleMplsTpPwCfgControlPeerAcId_Type())
sleMplsTpPwCfgControlPeerAcId.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpPwCfgControlPeerAcId.setStatus(_A)
_SleMplsTpPwCfgControlGroupName_Type=OctetString
_SleMplsTpPwCfgControlGroupName_Object=MibScalar
sleMplsTpPwCfgControlGroupName=_SleMplsTpPwCfgControlGroupName_Object((1,3,6,1,4,1,6296,101,16,15,1,2,15),_SleMplsTpPwCfgControlGroupName_Type())
sleMplsTpPwCfgControlGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpPwCfgControlGroupName.setStatus(_A)
_SleMplsTpPwCfgControlGroupId_Type=PwGroupID
_SleMplsTpPwCfgControlGroupId_Object=MibScalar
sleMplsTpPwCfgControlGroupId=_SleMplsTpPwCfgControlGroupId_Object((1,3,6,1,4,1,6296,101,16,15,1,2,16),_SleMplsTpPwCfgControlGroupId_Type())
sleMplsTpPwCfgControlGroupId.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpPwCfgControlGroupId.setStatus(_A)
class _SleMplsTpPwCfgControlOperMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_SleMplsTpPwCfgControlOperMode_Type.__name__=_D
_SleMplsTpPwCfgControlOperMode_Object=MibScalar
sleMplsTpPwCfgControlOperMode=_SleMplsTpPwCfgControlOperMode_Object((1,3,6,1,4,1,6296,101,16,15,1,2,17),_SleMplsTpPwCfgControlOperMode_Type())
sleMplsTpPwCfgControlOperMode.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpPwCfgControlOperMode.setStatus(_A)
_SleMplsTpPwCfgControlSvlanId_Type=VlanIdOrAnyOrNone
_SleMplsTpPwCfgControlSvlanId_Object=MibScalar
sleMplsTpPwCfgControlSvlanId=_SleMplsTpPwCfgControlSvlanId_Object((1,3,6,1,4,1,6296,101,16,15,1,2,18),_SleMplsTpPwCfgControlSvlanId_Type())
sleMplsTpPwCfgControlSvlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpPwCfgControlSvlanId.setStatus(_A)
_SleMplsTpPwCfgControlInlabel_Type=MplsLabel
_SleMplsTpPwCfgControlInlabel_Object=MibScalar
sleMplsTpPwCfgControlInlabel=_SleMplsTpPwCfgControlInlabel_Object((1,3,6,1,4,1,6296,101,16,15,1,2,20),_SleMplsTpPwCfgControlInlabel_Type())
sleMplsTpPwCfgControlInlabel.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpPwCfgControlInlabel.setStatus(_A)
_SleMplsTpPwCfgControlOutLabel_Type=MplsLabel
_SleMplsTpPwCfgControlOutLabel_Object=MibScalar
sleMplsTpPwCfgControlOutLabel=_SleMplsTpPwCfgControlOutLabel_Object((1,3,6,1,4,1,6296,101,16,15,1,2,21),_SleMplsTpPwCfgControlOutLabel_Type())
sleMplsTpPwCfgControlOutLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpPwCfgControlOutLabel.setStatus(_A)
class _SleMplsTpPwCfgControlTunnelName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(1,16))
_SleMplsTpPwCfgControlTunnelName_Type.__name__=_E
_SleMplsTpPwCfgControlTunnelName_Object=MibScalar
sleMplsTpPwCfgControlTunnelName=_SleMplsTpPwCfgControlTunnelName_Object((1,3,6,1,4,1,6296,101,16,15,1,2,22),_SleMplsTpPwCfgControlTunnelName_Type())
sleMplsTpPwCfgControlTunnelName.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpPwCfgControlTunnelName.setStatus(_A)
_SleMplsTpPwCfgControlAcInterfaceIndex_Type=InterfaceIndexOrZero
_SleMplsTpPwCfgControlAcInterfaceIndex_Object=MibScalar
sleMplsTpPwCfgControlAcInterfaceIndex=_SleMplsTpPwCfgControlAcInterfaceIndex_Object((1,3,6,1,4,1,6296,101,16,15,1,2,23),_SleMplsTpPwCfgControlAcInterfaceIndex_Type())
sleMplsTpPwCfgControlAcInterfaceIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpPwCfgControlAcInterfaceIndex.setStatus(_A)
_SleMplsTpPwCfgControlVcStitchName_Type=OctetString
_SleMplsTpPwCfgControlVcStitchName_Object=MibScalar
sleMplsTpPwCfgControlVcStitchName=_SleMplsTpPwCfgControlVcStitchName_Object((1,3,6,1,4,1,6296,101,16,15,1,2,24),_SleMplsTpPwCfgControlVcStitchName_Type())
sleMplsTpPwCfgControlVcStitchName.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpPwCfgControlVcStitchName.setStatus(_A)
_SleMplsTpPwCfgControlDescription_Type=OctetString
_SleMplsTpPwCfgControlDescription_Object=MibScalar
sleMplsTpPwCfgControlDescription=_SleMplsTpPwCfgControlDescription_Object((1,3,6,1,4,1,6296,101,16,15,1,2,26),_SleMplsTpPwCfgControlDescription_Type())
sleMplsTpPwCfgControlDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpPwCfgControlDescription.setStatus(_A)
class _SleMplsTpPwCfgControlPwStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_S,1))
_SleMplsTpPwCfgControlPwStatus_Type.__name__=_D
_SleMplsTpPwCfgControlPwStatus_Object=MibScalar
sleMplsTpPwCfgControlPwStatus=_SleMplsTpPwCfgControlPwStatus_Object((1,3,6,1,4,1,6296,101,16,15,1,2,27),_SleMplsTpPwCfgControlPwStatus_Type())
sleMplsTpPwCfgControlPwStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpPwCfgControlPwStatus.setStatus(_A)
class _SleMplsTpPwCfgControlLocalRefreshTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SleMplsTpPwCfgControlLocalRefreshTimer_Type.__name__=_D
_SleMplsTpPwCfgControlLocalRefreshTimer_Object=MibScalar
sleMplsTpPwCfgControlLocalRefreshTimer=_SleMplsTpPwCfgControlLocalRefreshTimer_Object((1,3,6,1,4,1,6296,101,16,15,1,2,28),_SleMplsTpPwCfgControlLocalRefreshTimer_Type())
sleMplsTpPwCfgControlLocalRefreshTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpPwCfgControlLocalRefreshTimer.setStatus(_A)
_SleMplsTpPwCfgControlQosServicePolicy_Type=OctetString
_SleMplsTpPwCfgControlQosServicePolicy_Object=MibScalar
sleMplsTpPwCfgControlQosServicePolicy=_SleMplsTpPwCfgControlQosServicePolicy_Object((1,3,6,1,4,1,6296,101,16,15,1,2,29),_SleMplsTpPwCfgControlQosServicePolicy_Type())
sleMplsTpPwCfgControlQosServicePolicy.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpPwCfgControlQosServicePolicy.setStatus(_A)
_SleMplsTpPwAcCfg_ObjectIdentity=ObjectIdentity
sleMplsTpPwAcCfg=_SleMplsTpPwAcCfg_ObjectIdentity((1,3,6,1,4,1,6296,101,16,15,2))
_SleMplsTpPwAcCfgInfoTable_Object=MibTable
sleMplsTpPwAcCfgInfoTable=_SleMplsTpPwAcCfgInfoTable_Object((1,3,6,1,4,1,6296,101,16,15,2,1))
if mibBuilder.loadTexts:sleMplsTpPwAcCfgInfoTable.setStatus(_A)
_SleMplsTpPwAcCfgInfoEntry_Object=MibTableRow
sleMplsTpPwAcCfgInfoEntry=_SleMplsTpPwAcCfgInfoEntry_Object((1,3,6,1,4,1,6296,101,16,15,2,1,1))
sleMplsTpPwAcCfgInfoEntry.setIndexNames((0,_F,_T))
if mibBuilder.loadTexts:sleMplsTpPwAcCfgInfoEntry.setStatus(_A)
_SleMplsTpPwAcCfgInfoIndex_Type=InterfaceIndexOrZero
_SleMplsTpPwAcCfgInfoIndex_Object=MibTableColumn
sleMplsTpPwAcCfgInfoIndex=_SleMplsTpPwAcCfgInfoIndex_Object((1,3,6,1,4,1,6296,101,16,15,2,1,1,1),_SleMplsTpPwAcCfgInfoIndex_Type())
sleMplsTpPwAcCfgInfoIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:sleMplsTpPwAcCfgInfoIndex.setStatus(_A)
_SleMplsTpPwAcCfgInfoLocalAcId_Type=Unsigned32
_SleMplsTpPwAcCfgInfoLocalAcId_Object=MibTableColumn
sleMplsTpPwAcCfgInfoLocalAcId=_SleMplsTpPwAcCfgInfoLocalAcId_Object((1,3,6,1,4,1,6296,101,16,15,2,1,1,2),_SleMplsTpPwAcCfgInfoLocalAcId_Type())
sleMplsTpPwAcCfgInfoLocalAcId.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpPwAcCfgInfoLocalAcId.setStatus(_A)
_SleMplsTpPwAcCfgControl_ObjectIdentity=ObjectIdentity
sleMplsTpPwAcCfgControl=_SleMplsTpPwAcCfgControl_ObjectIdentity((1,3,6,1,4,1,6296,101,16,15,2,2))
class _SleMplsTpPwAcCfgControlRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('setPwLocalACId',1),('unsetPwIfLocalACId',2)))
_SleMplsTpPwAcCfgControlRequest_Type.__name__=_D
_SleMplsTpPwAcCfgControlRequest_Object=MibScalar
sleMplsTpPwAcCfgControlRequest=_SleMplsTpPwAcCfgControlRequest_Object((1,3,6,1,4,1,6296,101,16,15,2,2,1),_SleMplsTpPwAcCfgControlRequest_Type())
sleMplsTpPwAcCfgControlRequest.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpPwAcCfgControlRequest.setStatus(_A)
_SleMplsTpPwAcCfgControlStatus_Type=SleControlStatusType
_SleMplsTpPwAcCfgControlStatus_Object=MibScalar
sleMplsTpPwAcCfgControlStatus=_SleMplsTpPwAcCfgControlStatus_Object((1,3,6,1,4,1,6296,101,16,15,2,2,2),_SleMplsTpPwAcCfgControlStatus_Type())
sleMplsTpPwAcCfgControlStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpPwAcCfgControlStatus.setStatus(_A)
_SleMplsTpPwAcCfgControlTimer_Type=Gauge32
_SleMplsTpPwAcCfgControlTimer_Object=MibScalar
sleMplsTpPwAcCfgControlTimer=_SleMplsTpPwAcCfgControlTimer_Object((1,3,6,1,4,1,6296,101,16,15,2,2,3),_SleMplsTpPwAcCfgControlTimer_Type())
sleMplsTpPwAcCfgControlTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpPwAcCfgControlTimer.setStatus(_A)
_SleMplsTpPwAcCfgControlTimestamp_Type=TimeTicks
_SleMplsTpPwAcCfgControlTimestamp_Object=MibScalar
sleMplsTpPwAcCfgControlTimestamp=_SleMplsTpPwAcCfgControlTimestamp_Object((1,3,6,1,4,1,6296,101,16,15,2,2,4),_SleMplsTpPwAcCfgControlTimestamp_Type())
sleMplsTpPwAcCfgControlTimestamp.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpPwAcCfgControlTimestamp.setStatus(_A)
_SleMplsTpPwAcCfgControlReqResult_Type=SleControlRequestResultType
_SleMplsTpPwAcCfgControlReqResult_Object=MibScalar
sleMplsTpPwAcCfgControlReqResult=_SleMplsTpPwAcCfgControlReqResult_Object((1,3,6,1,4,1,6296,101,16,15,2,2,5),_SleMplsTpPwAcCfgControlReqResult_Type())
sleMplsTpPwAcCfgControlReqResult.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpPwAcCfgControlReqResult.setStatus(_A)
_SleMplsTpPwAcCfgControlIfIndex_Type=InterfaceIndexOrZero
_SleMplsTpPwAcCfgControlIfIndex_Object=MibScalar
sleMplsTpPwAcCfgControlIfIndex=_SleMplsTpPwAcCfgControlIfIndex_Object((1,3,6,1,4,1,6296,101,16,15,2,2,6),_SleMplsTpPwAcCfgControlIfIndex_Type())
sleMplsTpPwAcCfgControlIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpPwAcCfgControlIfIndex.setStatus(_A)
_SleMplsTpPwAcCfgControlLocalAcId_Type=Unsigned32
_SleMplsTpPwAcCfgControlLocalAcId_Object=MibScalar
sleMplsTpPwAcCfgControlLocalAcId=_SleMplsTpPwAcCfgControlLocalAcId_Object((1,3,6,1,4,1,6296,101,16,15,2,2,7),_SleMplsTpPwAcCfgControlLocalAcId_Type())
sleMplsTpPwAcCfgControlLocalAcId.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpPwAcCfgControlLocalAcId.setStatus(_A)
_SleMplsTpPwIfCfg_ObjectIdentity=ObjectIdentity
sleMplsTpPwIfCfg=_SleMplsTpPwIfCfg_ObjectIdentity((1,3,6,1,4,1,6296,101,16,15,3))
_SleMplsTpPwIfCfgInfoTable_Object=MibTable
sleMplsTpPwIfCfgInfoTable=_SleMplsTpPwIfCfgInfoTable_Object((1,3,6,1,4,1,6296,101,16,15,3,1))
if mibBuilder.loadTexts:sleMplsTpPwIfCfgInfoTable.setStatus(_A)
_SleMplsTpPwIfCfgInfoEntry_Object=MibTableRow
sleMplsTpPwIfCfgInfoEntry=_SleMplsTpPwIfCfgInfoEntry_Object((1,3,6,1,4,1,6296,101,16,15,3,1,1))
sleMplsTpPwIfCfgInfoEntry.setIndexNames((0,_F,_U),(0,_F,_V))
if mibBuilder.loadTexts:sleMplsTpPwIfCfgInfoEntry.setStatus(_A)
_SleMplsTpPwIfCfgInfoIndex_Type=InterfaceIndexOrZero
_SleMplsTpPwIfCfgInfoIndex_Object=MibTableColumn
sleMplsTpPwIfCfgInfoIndex=_SleMplsTpPwIfCfgInfoIndex_Object((1,3,6,1,4,1,6296,101,16,15,3,1,1,1),_SleMplsTpPwIfCfgInfoIndex_Type())
sleMplsTpPwIfCfgInfoIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:sleMplsTpPwIfCfgInfoIndex.setStatus(_A)
_SleMplsTpPwIfCfgInfoVcName_Type=OctetString
_SleMplsTpPwIfCfgInfoVcName_Object=MibTableColumn
sleMplsTpPwIfCfgInfoVcName=_SleMplsTpPwIfCfgInfoVcName_Object((1,3,6,1,4,1,6296,101,16,15,3,1,1,2),_SleMplsTpPwIfCfgInfoVcName_Type())
sleMplsTpPwIfCfgInfoVcName.setMaxAccess(_I)
if mibBuilder.loadTexts:sleMplsTpPwIfCfgInfoVcName.setStatus(_A)
_SleMplsTpPwIfCfgInfoServiceType_Type=IANAPwTypeTC
_SleMplsTpPwIfCfgInfoServiceType_Object=MibTableColumn
sleMplsTpPwIfCfgInfoServiceType=_SleMplsTpPwIfCfgInfoServiceType_Object((1,3,6,1,4,1,6296,101,16,15,3,1,1,3),_SleMplsTpPwIfCfgInfoServiceType_Type())
sleMplsTpPwIfCfgInfoServiceType.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpPwIfCfgInfoServiceType.setStatus(_A)
_SleMplsTpPwIfCfgInfoVlanId_Type=VlanIdOrAnyOrNone
_SleMplsTpPwIfCfgInfoVlanId_Object=MibTableColumn
sleMplsTpPwIfCfgInfoVlanId=_SleMplsTpPwIfCfgInfoVlanId_Object((1,3,6,1,4,1,6296,101,16,15,3,1,1,4),_SleMplsTpPwIfCfgInfoVlanId_Type())
sleMplsTpPwIfCfgInfoVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpPwIfCfgInfoVlanId.setStatus(_A)
class _SleMplsTpPwIfCfgInfoPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SleMplsTpPwIfCfgInfoPriority_Type.__name__=_D
_SleMplsTpPwIfCfgInfoPriority_Object=MibTableColumn
sleMplsTpPwIfCfgInfoPriority=_SleMplsTpPwIfCfgInfoPriority_Object((1,3,6,1,4,1,6296,101,16,15,3,1,1,5),_SleMplsTpPwIfCfgInfoPriority_Type())
sleMplsTpPwIfCfgInfoPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpPwIfCfgInfoPriority.setStatus(_A)
_SleMplsTpPwIfCfgInfoSVlanId_Type=VlanIdOrAnyOrNone
_SleMplsTpPwIfCfgInfoSVlanId_Object=MibTableColumn
sleMplsTpPwIfCfgInfoSVlanId=_SleMplsTpPwIfCfgInfoSVlanId_Object((1,3,6,1,4,1,6296,101,16,15,3,1,1,6),_SleMplsTpPwIfCfgInfoSVlanId_Type())
sleMplsTpPwIfCfgInfoSVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpPwIfCfgInfoSVlanId.setStatus(_A)
_SleMplsTpPwIfCfgInfoInnerVlanId_Type=VlanIdOrAnyOrNone
_SleMplsTpPwIfCfgInfoInnerVlanId_Object=MibTableColumn
sleMplsTpPwIfCfgInfoInnerVlanId=_SleMplsTpPwIfCfgInfoInnerVlanId_Object((1,3,6,1,4,1,6296,101,16,15,3,1,1,7),_SleMplsTpPwIfCfgInfoInnerVlanId_Type())
sleMplsTpPwIfCfgInfoInnerVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpPwIfCfgInfoInnerVlanId.setStatus(_A)
class _SleMplsTpPwIfCfgInfoAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('noOp',1),(_W,2),(_X,3),(_Y,4)))
_SleMplsTpPwIfCfgInfoAction_Type.__name__=_D
_SleMplsTpPwIfCfgInfoAction_Object=MibTableColumn
sleMplsTpPwIfCfgInfoAction=_SleMplsTpPwIfCfgInfoAction_Object((1,3,6,1,4,1,6296,101,16,15,3,1,1,8),_SleMplsTpPwIfCfgInfoAction_Type())
sleMplsTpPwIfCfgInfoAction.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpPwIfCfgInfoAction.setStatus(_A)
_SleMplsTpPwIfCfgControl_ObjectIdentity=ObjectIdentity
sleMplsTpPwIfCfgControl=_SleMplsTpPwIfCfgControl_ObjectIdentity((1,3,6,1,4,1,6296,101,16,15,3,2))
class _SleMplsTpPwIfCfgControlRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('setPwBindwithRaw',1),('setPwBindwithTagged',2),('unsetPwBindwithRaw',3),('unsetPwBindwithTagged',4),('setPWBindWithRawSvlanIdAction',5),('setPWBindWithRawSvlanIdTPIDActionPriority',6),('setPWBindWithTaggedTpidAction',7),('setPwbindWithTaggedTpidActionPriority',8),('setPWBindWithQinQ',9),('setPWBindWithQinQPrority',10),('setPWBindWithQinQTpidAction',11),('setPWBindWithQinQTpidActionPriority',12)))
_SleMplsTpPwIfCfgControlRequest_Type.__name__=_D
_SleMplsTpPwIfCfgControlRequest_Object=MibScalar
sleMplsTpPwIfCfgControlRequest=_SleMplsTpPwIfCfgControlRequest_Object((1,3,6,1,4,1,6296,101,16,15,3,2,1),_SleMplsTpPwIfCfgControlRequest_Type())
sleMplsTpPwIfCfgControlRequest.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpPwIfCfgControlRequest.setStatus(_A)
_SleMplsTpPwIfCfgControlStatus_Type=SleControlStatusType
_SleMplsTpPwIfCfgControlStatus_Object=MibScalar
sleMplsTpPwIfCfgControlStatus=_SleMplsTpPwIfCfgControlStatus_Object((1,3,6,1,4,1,6296,101,16,15,3,2,2),_SleMplsTpPwIfCfgControlStatus_Type())
sleMplsTpPwIfCfgControlStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpPwIfCfgControlStatus.setStatus(_A)
_SleMplsTpPwIfCfgControlTimer_Type=Gauge32
_SleMplsTpPwIfCfgControlTimer_Object=MibScalar
sleMplsTpPwIfCfgControlTimer=_SleMplsTpPwIfCfgControlTimer_Object((1,3,6,1,4,1,6296,101,16,15,3,2,3),_SleMplsTpPwIfCfgControlTimer_Type())
sleMplsTpPwIfCfgControlTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpPwIfCfgControlTimer.setStatus(_A)
_SleMplsTpPwIfCfgControlTimestamp_Type=TimeTicks
_SleMplsTpPwIfCfgControlTimestamp_Object=MibScalar
sleMplsTpPwIfCfgControlTimestamp=_SleMplsTpPwIfCfgControlTimestamp_Object((1,3,6,1,4,1,6296,101,16,15,3,2,4),_SleMplsTpPwIfCfgControlTimestamp_Type())
sleMplsTpPwIfCfgControlTimestamp.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpPwIfCfgControlTimestamp.setStatus(_A)
_SleMplsTpPwIfCfgControlReqResult_Type=SleControlRequestResultType
_SleMplsTpPwIfCfgControlReqResult_Object=MibScalar
sleMplsTpPwIfCfgControlReqResult=_SleMplsTpPwIfCfgControlReqResult_Object((1,3,6,1,4,1,6296,101,16,15,3,2,5),_SleMplsTpPwIfCfgControlReqResult_Type())
sleMplsTpPwIfCfgControlReqResult.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpPwIfCfgControlReqResult.setStatus(_A)
_SleMplsTpPwIfCfgControlIndex_Type=InterfaceIndexOrZero
_SleMplsTpPwIfCfgControlIndex_Object=MibScalar
sleMplsTpPwIfCfgControlIndex=_SleMplsTpPwIfCfgControlIndex_Object((1,3,6,1,4,1,6296,101,16,15,3,2,6),_SleMplsTpPwIfCfgControlIndex_Type())
sleMplsTpPwIfCfgControlIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpPwIfCfgControlIndex.setStatus(_A)
_SleMplsTpPwIfCfgControlVcName_Type=OctetString
_SleMplsTpPwIfCfgControlVcName_Object=MibScalar
sleMplsTpPwIfCfgControlVcName=_SleMplsTpPwIfCfgControlVcName_Object((1,3,6,1,4,1,6296,101,16,15,3,2,7),_SleMplsTpPwIfCfgControlVcName_Type())
sleMplsTpPwIfCfgControlVcName.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpPwIfCfgControlVcName.setStatus(_A)
_SleMplsTpPwIfCfgControlServiceType_Type=IANAPwTypeTC
_SleMplsTpPwIfCfgControlServiceType_Object=MibScalar
sleMplsTpPwIfCfgControlServiceType=_SleMplsTpPwIfCfgControlServiceType_Object((1,3,6,1,4,1,6296,101,16,15,3,2,8),_SleMplsTpPwIfCfgControlServiceType_Type())
sleMplsTpPwIfCfgControlServiceType.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpPwIfCfgControlServiceType.setStatus(_A)
_SleMplsTpPwIfCfgControlVlanId_Type=VlanIdOrAnyOrNone
_SleMplsTpPwIfCfgControlVlanId_Object=MibScalar
sleMplsTpPwIfCfgControlVlanId=_SleMplsTpPwIfCfgControlVlanId_Object((1,3,6,1,4,1,6296,101,16,15,3,2,9),_SleMplsTpPwIfCfgControlVlanId_Type())
sleMplsTpPwIfCfgControlVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpPwIfCfgControlVlanId.setStatus(_A)
class _SleMplsTpPwIfCfgControlPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SleMplsTpPwIfCfgControlPriority_Type.__name__=_D
_SleMplsTpPwIfCfgControlPriority_Object=MibScalar
sleMplsTpPwIfCfgControlPriority=_SleMplsTpPwIfCfgControlPriority_Object((1,3,6,1,4,1,6296,101,16,15,3,2,10),_SleMplsTpPwIfCfgControlPriority_Type())
sleMplsTpPwIfCfgControlPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpPwIfCfgControlPriority.setStatus(_A)
_SleMplsTpPwIfCfgControlSVlanId_Type=VlanIdOrAnyOrNone
_SleMplsTpPwIfCfgControlSVlanId_Object=MibScalar
sleMplsTpPwIfCfgControlSVlanId=_SleMplsTpPwIfCfgControlSVlanId_Object((1,3,6,1,4,1,6296,101,16,15,3,2,11),_SleMplsTpPwIfCfgControlSVlanId_Type())
sleMplsTpPwIfCfgControlSVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpPwIfCfgControlSVlanId.setStatus(_A)
_SleMplsTpPwIfCfgControlInnerVlanId_Type=VlanIdOrAnyOrNone
_SleMplsTpPwIfCfgControlInnerVlanId_Object=MibScalar
sleMplsTpPwIfCfgControlInnerVlanId=_SleMplsTpPwIfCfgControlInnerVlanId_Object((1,3,6,1,4,1,6296,101,16,15,3,2,12),_SleMplsTpPwIfCfgControlInnerVlanId_Type())
sleMplsTpPwIfCfgControlInnerVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpPwIfCfgControlInnerVlanId.setStatus(_A)
class _SleMplsTpPwIfCfgControlAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('noOp',1),(_W,2),(_X,3),(_Y,4)))
_SleMplsTpPwIfCfgControlAction_Type.__name__=_D
_SleMplsTpPwIfCfgControlAction_Object=MibScalar
sleMplsTpPwIfCfgControlAction=_SleMplsTpPwIfCfgControlAction_Object((1,3,6,1,4,1,6296,101,16,15,3,2,13),_SleMplsTpPwIfCfgControlAction_Type())
sleMplsTpPwIfCfgControlAction.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpPwIfCfgControlAction.setStatus(_A)
_SleMplsTpMsPwCfg_ObjectIdentity=ObjectIdentity
sleMplsTpMsPwCfg=_SleMplsTpMsPwCfg_ObjectIdentity((1,3,6,1,4,1,6296,101,16,15,4))
_SleMplsTpMsPwCfgInfoTable_Object=MibTable
sleMplsTpMsPwCfgInfoTable=_SleMplsTpMsPwCfgInfoTable_Object((1,3,6,1,4,1,6296,101,16,15,4,1))
if mibBuilder.loadTexts:sleMplsTpMsPwCfgInfoTable.setStatus(_A)
_SleMplsTpMsPwCfgInfoEntry_Object=MibTableRow
sleMplsTpMsPwCfgInfoEntry=_SleMplsTpMsPwCfgInfoEntry_Object((1,3,6,1,4,1,6296,101,16,15,4,1,1))
sleMplsTpMsPwCfgInfoEntry.setIndexNames((0,_F,_Z))
if mibBuilder.loadTexts:sleMplsTpMsPwCfgInfoEntry.setStatus(_A)
class _SleMplsTpMsPwCfgInfoName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SleMplsTpMsPwCfgInfoName_Type.__name__=_E
_SleMplsTpMsPwCfgInfoName_Object=MibTableColumn
sleMplsTpMsPwCfgInfoName=_SleMplsTpMsPwCfgInfoName_Object((1,3,6,1,4,1,6296,101,16,15,4,1,1,1),_SleMplsTpMsPwCfgInfoName_Type())
sleMplsTpMsPwCfgInfoName.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpMsPwCfgInfoName.setStatus(_A)
_SleMplsTpMsPwCfgInfoSegment1Name_Type=OctetString
_SleMplsTpMsPwCfgInfoSegment1Name_Object=MibTableColumn
sleMplsTpMsPwCfgInfoSegment1Name=_SleMplsTpMsPwCfgInfoSegment1Name_Object((1,3,6,1,4,1,6296,101,16,15,4,1,1,2),_SleMplsTpMsPwCfgInfoSegment1Name_Type())
sleMplsTpMsPwCfgInfoSegment1Name.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpMsPwCfgInfoSegment1Name.setStatus(_A)
_SleMplsTpMsPwCfgInfoSegment2Name_Type=OctetString
_SleMplsTpMsPwCfgInfoSegment2Name_Object=MibTableColumn
sleMplsTpMsPwCfgInfoSegment2Name=_SleMplsTpMsPwCfgInfoSegment2Name_Object((1,3,6,1,4,1,6296,101,16,15,4,1,1,3),_SleMplsTpMsPwCfgInfoSegment2Name_Type())
sleMplsTpMsPwCfgInfoSegment2Name.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpMsPwCfgInfoSegment2Name.setStatus(_A)
class _SleMplsTpMsPwCfgInfoDescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_SleMplsTpMsPwCfgInfoDescription_Type.__name__=_E
_SleMplsTpMsPwCfgInfoDescription_Object=MibTableColumn
sleMplsTpMsPwCfgInfoDescription=_SleMplsTpMsPwCfgInfoDescription_Object((1,3,6,1,4,1,6296,101,16,15,4,1,1,4),_SleMplsTpMsPwCfgInfoDescription_Type())
sleMplsTpMsPwCfgInfoDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpMsPwCfgInfoDescription.setStatus(_A)
class _SleMplsTpMsPwCfgInfoMtu_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(68,9216))
_SleMplsTpMsPwCfgInfoMtu_Type.__name__=_D
_SleMplsTpMsPwCfgInfoMtu_Object=MibTableColumn
sleMplsTpMsPwCfgInfoMtu=_SleMplsTpMsPwCfgInfoMtu_Object((1,3,6,1,4,1,6296,101,16,15,4,1,1,5),_SleMplsTpMsPwCfgInfoMtu_Type())
sleMplsTpMsPwCfgInfoMtu.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpMsPwCfgInfoMtu.setStatus(_A)
_SleMplsTpMsPwCfgInfoServiceType_Type=IANAPwTypeTC
_SleMplsTpMsPwCfgInfoServiceType_Object=MibTableColumn
sleMplsTpMsPwCfgInfoServiceType=_SleMplsTpMsPwCfgInfoServiceType_Object((1,3,6,1,4,1,6296,101,16,15,4,1,1,6),_SleMplsTpMsPwCfgInfoServiceType_Type())
sleMplsTpMsPwCfgInfoServiceType.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpMsPwCfgInfoServiceType.setStatus(_A)
_SleMplsTpMsPwCfgInfoVlanId_Type=VlanIdOrAnyOrNone
_SleMplsTpMsPwCfgInfoVlanId_Object=MibTableColumn
sleMplsTpMsPwCfgInfoVlanId=_SleMplsTpMsPwCfgInfoVlanId_Object((1,3,6,1,4,1,6296,101,16,15,4,1,1,7),_SleMplsTpMsPwCfgInfoVlanId_Type())
sleMplsTpMsPwCfgInfoVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpMsPwCfgInfoVlanId.setStatus(_A)
_SleMplsTpMsPwCfgControl_ObjectIdentity=ObjectIdentity
sleMplsTpMsPwCfgControl=_SleMplsTpMsPwCfgControl_ObjectIdentity((1,3,6,1,4,1,6296,101,16,15,4,2))
class _SleMplsTpMsPwCfgControlRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('createMsPw',1),('createMsPwWithMtuAndServiceType',2),('deleteMsPw',3),('setMsPwDescription',4),('unsetMsPwDescription',5)))
_SleMplsTpMsPwCfgControlRequest_Type.__name__=_D
_SleMplsTpMsPwCfgControlRequest_Object=MibScalar
sleMplsTpMsPwCfgControlRequest=_SleMplsTpMsPwCfgControlRequest_Object((1,3,6,1,4,1,6296,101,16,15,4,2,1),_SleMplsTpMsPwCfgControlRequest_Type())
sleMplsTpMsPwCfgControlRequest.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpMsPwCfgControlRequest.setStatus(_A)
_SleMplsTpMsPwCfgControlStatus_Type=SleControlStatusType
_SleMplsTpMsPwCfgControlStatus_Object=MibScalar
sleMplsTpMsPwCfgControlStatus=_SleMplsTpMsPwCfgControlStatus_Object((1,3,6,1,4,1,6296,101,16,15,4,2,2),_SleMplsTpMsPwCfgControlStatus_Type())
sleMplsTpMsPwCfgControlStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpMsPwCfgControlStatus.setStatus(_A)
_SleMplsTpMsPwCfgControlTimer_Type=Gauge32
_SleMplsTpMsPwCfgControlTimer_Object=MibScalar
sleMplsTpMsPwCfgControlTimer=_SleMplsTpMsPwCfgControlTimer_Object((1,3,6,1,4,1,6296,101,16,15,4,2,3),_SleMplsTpMsPwCfgControlTimer_Type())
sleMplsTpMsPwCfgControlTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:sleMplsTpMsPwCfgControlTimer.setStatus(_A)
_SleMplsTpMsPwCfgControlTimestamp_Type=TimeTicks
_SleMplsTpMsPwCfgControlTimestamp_Object=MibScalar
sleMplsTpMsPwCfgControlTimestamp=_SleMplsTpMsPwCfgControlTimestamp_Object((1,3,6,1,4,1,6296,101,16,15,4,2,4),_SleMplsTpMsPwCfgControlTimestamp_Type())
sleMplsTpMsPwCfgControlTimestamp.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpMsPwCfgControlTimestamp.setStatus(_A)
_SleMplsTpMsPwCfgControlReqResult_Type=SleControlRequestResultType
_SleMplsTpMsPwCfgControlReqResult_Object=MibScalar
sleMplsTpMsPwCfgControlReqResult=_SleMplsTpMsPwCfgControlReqResult_Object((1,3,6,1,4,1,6296,101,16,15,4,2,5),_SleMplsTpMsPwCfgControlReqResult_Type())
sleMplsTpMsPwCfgControlReqResult.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpMsPwCfgControlReqResult.setStatus(_A)
class _SleMplsTpMsPwCfgControlName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SleMplsTpMsPwCfgControlName_Type.__name__=_E
_SleMplsTpMsPwCfgControlName_Object=MibScalar
sleMplsTpMsPwCfgControlName=_SleMplsTpMsPwCfgControlName_Object((1,3,6,1,4,1,6296,101,16,15,4,2,6),_SleMplsTpMsPwCfgControlName_Type())
sleMplsTpMsPwCfgControlName.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpMsPwCfgControlName.setStatus(_A)
_SleMplsTpMsPwCfgControlSegment1Name_Type=OctetString
_SleMplsTpMsPwCfgControlSegment1Name_Object=MibScalar
sleMplsTpMsPwCfgControlSegment1Name=_SleMplsTpMsPwCfgControlSegment1Name_Object((1,3,6,1,4,1,6296,101,16,15,4,2,7),_SleMplsTpMsPwCfgControlSegment1Name_Type())
sleMplsTpMsPwCfgControlSegment1Name.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpMsPwCfgControlSegment1Name.setStatus(_A)
_SleMplsTpMsPwCfgControlSegment2Name_Type=OctetString
_SleMplsTpMsPwCfgControlSegment2Name_Object=MibScalar
sleMplsTpMsPwCfgControlSegment2Name=_SleMplsTpMsPwCfgControlSegment2Name_Object((1,3,6,1,4,1,6296,101,16,15,4,2,8),_SleMplsTpMsPwCfgControlSegment2Name_Type())
sleMplsTpMsPwCfgControlSegment2Name.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpMsPwCfgControlSegment2Name.setStatus(_A)
class _SleMplsTpMsPwCfgControlDescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_SleMplsTpMsPwCfgControlDescription_Type.__name__=_E
_SleMplsTpMsPwCfgControlDescription_Object=MibScalar
sleMplsTpMsPwCfgControlDescription=_SleMplsTpMsPwCfgControlDescription_Object((1,3,6,1,4,1,6296,101,16,15,4,2,9),_SleMplsTpMsPwCfgControlDescription_Type())
sleMplsTpMsPwCfgControlDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpMsPwCfgControlDescription.setStatus(_A)
class _SleMplsTpMsPwCfgControlMtu_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(68,9216))
_SleMplsTpMsPwCfgControlMtu_Type.__name__=_D
_SleMplsTpMsPwCfgControlMtu_Object=MibScalar
sleMplsTpMsPwCfgControlMtu=_SleMplsTpMsPwCfgControlMtu_Object((1,3,6,1,4,1,6296,101,16,15,4,2,10),_SleMplsTpMsPwCfgControlMtu_Type())
sleMplsTpMsPwCfgControlMtu.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpMsPwCfgControlMtu.setStatus(_A)
_SleMplsTpMsPwCfgControlServiceType_Type=IANAPwTypeTC
_SleMplsTpMsPwCfgControlServiceType_Object=MibScalar
sleMplsTpMsPwCfgControlServiceType=_SleMplsTpMsPwCfgControlServiceType_Object((1,3,6,1,4,1,6296,101,16,15,4,2,11),_SleMplsTpMsPwCfgControlServiceType_Type())
sleMplsTpMsPwCfgControlServiceType.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpMsPwCfgControlServiceType.setStatus(_A)
_SleMplsTpMsPwCfgControlVlanId_Type=VlanIdOrAnyOrNone
_SleMplsTpMsPwCfgControlVlanId_Object=MibScalar
sleMplsTpMsPwCfgControlVlanId=_SleMplsTpMsPwCfgControlVlanId_Object((1,3,6,1,4,1,6296,101,16,15,4,2,12),_SleMplsTpMsPwCfgControlVlanId_Type())
sleMplsTpMsPwCfgControlVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpMsPwCfgControlVlanId.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'sleMpls':sleMpls,'sleMplsTpPw':sleMplsTpPw,'sleMplsTpPwCfg':sleMplsTpPwCfg,'sleMplsTpPwCfgInfoTable':sleMplsTpPwCfgInfoTable,'sleMplsTpPwCfgInfoEntry':sleMplsTpPwCfgInfoEntry,_L:sleMplsTpPwCfgInfoId,'sleMplsTpPwCfgInfoName':sleMplsTpPwCfgInfoName,'sleMplsTpPwCfgInfoOwner':sleMplsTpPwCfgInfoOwner,'sleMplsTpPwCfgInfoType':sleMplsTpPwCfgInfoType,'sleMplsTpPwCfgInfoControlWord':sleMplsTpPwCfgInfoControlWord,'sleMplsTpPwCfgInfoPeerIdType':sleMplsTpPwCfgInfoPeerIdType,'sleMplsTpPwCfgInfoPeerGolbalId':sleMplsTpPwCfgInfoPeerGolbalId,'sleMplsTpPwCfgInfoPeerCc':sleMplsTpPwCfgInfoPeerCc,'sleMplsTpPwCfgInfoPeerIcc':sleMplsTpPwCfgInfoPeerIcc,'sleMplsTpPwCfgInfoPeerNodeId':sleMplsTpPwCfgInfoPeerNodeId,'sleMplsTpPwCfgInfoPeerAcId':sleMplsTpPwCfgInfoPeerAcId,'sleMplsTpPwCfgInfoGroupName':sleMplsTpPwCfgInfoGroupName,'sleMplsTpPwCfgInfoGroupId':sleMplsTpPwCfgInfoGroupId,'sleMplsTpPwCfgInfoOperMode':sleMplsTpPwCfgInfoOperMode,'sleMplsTpPwCfgInfoSvlanId':sleMplsTpPwCfgInfoSvlanId,'sleMplsTpPwCfgInfoPwStatus':sleMplsTpPwCfgInfoPwStatus,'sleMplsTpPwCfgInfoInlabel':sleMplsTpPwCfgInfoInlabel,'sleMplsTpPwCfgInfoOutLabel':sleMplsTpPwCfgInfoOutLabel,'sleMplsTpPwCfgInfoTunnelName':sleMplsTpPwCfgInfoTunnelName,'sleMplsTpPwCfgInfoAcInterfaceIndex':sleMplsTpPwCfgInfoAcInterfaceIndex,'sleMplsTpPwCfgInfoVcStitchName':sleMplsTpPwCfgInfoVcStitchName,'sleMplsTpPwCfgInfoPriority':sleMplsTpPwCfgInfoPriority,'sleMplsTpPwCfgInfostate':sleMplsTpPwCfgInfostate,'sleMplsTpPwCfgInfoDescription':sleMplsTpPwCfgInfoDescription,'sleMplsTpPwCfgInfoLocalRefreshTimer':sleMplsTpPwCfgInfoLocalRefreshTimer,'sleMplsTpPwCfgInfoQosServicePolicy':sleMplsTpPwCfgInfoQosServicePolicy,'sleMplsTpPwCfgControl':sleMplsTpPwCfgControl,'sleMplsTpPwCfgControlRequest':sleMplsTpPwCfgControlRequest,'sleMplsTpPwCfgControlStatus':sleMplsTpPwCfgControlStatus,'sleMplsTpPwCfgControlTimer':sleMplsTpPwCfgControlTimer,'sleMplsTpPwCfgControlTimestamp':sleMplsTpPwCfgControlTimestamp,'sleMplsTpPwCfgControlReqResult':sleMplsTpPwCfgControlReqResult,'sleMplsTpPwCfgControlId':sleMplsTpPwCfgControlId,'sleMplsTpPwCfgControlName':sleMplsTpPwCfgControlName,'sleMplsTpPwCfgControlOwner':sleMplsTpPwCfgControlOwner,'sleMplsTpPwCfgControlPeerIdType':sleMplsTpPwCfgControlPeerIdType,'sleMplsTpPwCfgControlPeerGolbalId':sleMplsTpPwCfgControlPeerGolbalId,'sleMplsTpPwCfgControlPeerCc':sleMplsTpPwCfgControlPeerCc,'sleMplsTpPwCfgControlPeerIcc':sleMplsTpPwCfgControlPeerIcc,'sleMplsTpPwCfgControlPeerNodeId':sleMplsTpPwCfgControlPeerNodeId,'sleMplsTpPwCfgControlPeerAcId':sleMplsTpPwCfgControlPeerAcId,'sleMplsTpPwCfgControlGroupName':sleMplsTpPwCfgControlGroupName,'sleMplsTpPwCfgControlGroupId':sleMplsTpPwCfgControlGroupId,'sleMplsTpPwCfgControlOperMode':sleMplsTpPwCfgControlOperMode,'sleMplsTpPwCfgControlSvlanId':sleMplsTpPwCfgControlSvlanId,'sleMplsTpPwCfgControlInlabel':sleMplsTpPwCfgControlInlabel,'sleMplsTpPwCfgControlOutLabel':sleMplsTpPwCfgControlOutLabel,'sleMplsTpPwCfgControlTunnelName':sleMplsTpPwCfgControlTunnelName,'sleMplsTpPwCfgControlAcInterfaceIndex':sleMplsTpPwCfgControlAcInterfaceIndex,'sleMplsTpPwCfgControlVcStitchName':sleMplsTpPwCfgControlVcStitchName,'sleMplsTpPwCfgControlDescription':sleMplsTpPwCfgControlDescription,'sleMplsTpPwCfgControlPwStatus':sleMplsTpPwCfgControlPwStatus,'sleMplsTpPwCfgControlLocalRefreshTimer':sleMplsTpPwCfgControlLocalRefreshTimer,'sleMplsTpPwCfgControlQosServicePolicy':sleMplsTpPwCfgControlQosServicePolicy,'sleMplsTpPwAcCfg':sleMplsTpPwAcCfg,'sleMplsTpPwAcCfgInfoTable':sleMplsTpPwAcCfgInfoTable,'sleMplsTpPwAcCfgInfoEntry':sleMplsTpPwAcCfgInfoEntry,_T:sleMplsTpPwAcCfgInfoIndex,'sleMplsTpPwAcCfgInfoLocalAcId':sleMplsTpPwAcCfgInfoLocalAcId,'sleMplsTpPwAcCfgControl':sleMplsTpPwAcCfgControl,'sleMplsTpPwAcCfgControlRequest':sleMplsTpPwAcCfgControlRequest,'sleMplsTpPwAcCfgControlStatus':sleMplsTpPwAcCfgControlStatus,'sleMplsTpPwAcCfgControlTimer':sleMplsTpPwAcCfgControlTimer,'sleMplsTpPwAcCfgControlTimestamp':sleMplsTpPwAcCfgControlTimestamp,'sleMplsTpPwAcCfgControlReqResult':sleMplsTpPwAcCfgControlReqResult,'sleMplsTpPwAcCfgControlIfIndex':sleMplsTpPwAcCfgControlIfIndex,'sleMplsTpPwAcCfgControlLocalAcId':sleMplsTpPwAcCfgControlLocalAcId,'sleMplsTpPwIfCfg':sleMplsTpPwIfCfg,'sleMplsTpPwIfCfgInfoTable':sleMplsTpPwIfCfgInfoTable,'sleMplsTpPwIfCfgInfoEntry':sleMplsTpPwIfCfgInfoEntry,_U:sleMplsTpPwIfCfgInfoIndex,_V:sleMplsTpPwIfCfgInfoVcName,'sleMplsTpPwIfCfgInfoServiceType':sleMplsTpPwIfCfgInfoServiceType,'sleMplsTpPwIfCfgInfoVlanId':sleMplsTpPwIfCfgInfoVlanId,'sleMplsTpPwIfCfgInfoPriority':sleMplsTpPwIfCfgInfoPriority,'sleMplsTpPwIfCfgInfoSVlanId':sleMplsTpPwIfCfgInfoSVlanId,'sleMplsTpPwIfCfgInfoInnerVlanId':sleMplsTpPwIfCfgInfoInnerVlanId,'sleMplsTpPwIfCfgInfoAction':sleMplsTpPwIfCfgInfoAction,'sleMplsTpPwIfCfgControl':sleMplsTpPwIfCfgControl,'sleMplsTpPwIfCfgControlRequest':sleMplsTpPwIfCfgControlRequest,'sleMplsTpPwIfCfgControlStatus':sleMplsTpPwIfCfgControlStatus,'sleMplsTpPwIfCfgControlTimer':sleMplsTpPwIfCfgControlTimer,'sleMplsTpPwIfCfgControlTimestamp':sleMplsTpPwIfCfgControlTimestamp,'sleMplsTpPwIfCfgControlReqResult':sleMplsTpPwIfCfgControlReqResult,'sleMplsTpPwIfCfgControlIndex':sleMplsTpPwIfCfgControlIndex,'sleMplsTpPwIfCfgControlVcName':sleMplsTpPwIfCfgControlVcName,'sleMplsTpPwIfCfgControlServiceType':sleMplsTpPwIfCfgControlServiceType,'sleMplsTpPwIfCfgControlVlanId':sleMplsTpPwIfCfgControlVlanId,'sleMplsTpPwIfCfgControlPriority':sleMplsTpPwIfCfgControlPriority,'sleMplsTpPwIfCfgControlSVlanId':sleMplsTpPwIfCfgControlSVlanId,'sleMplsTpPwIfCfgControlInnerVlanId':sleMplsTpPwIfCfgControlInnerVlanId,'sleMplsTpPwIfCfgControlAction':sleMplsTpPwIfCfgControlAction,'sleMplsTpMsPwCfg':sleMplsTpMsPwCfg,'sleMplsTpMsPwCfgInfoTable':sleMplsTpMsPwCfgInfoTable,'sleMplsTpMsPwCfgInfoEntry':sleMplsTpMsPwCfgInfoEntry,_Z:sleMplsTpMsPwCfgInfoName,'sleMplsTpMsPwCfgInfoSegment1Name':sleMplsTpMsPwCfgInfoSegment1Name,'sleMplsTpMsPwCfgInfoSegment2Name':sleMplsTpMsPwCfgInfoSegment2Name,'sleMplsTpMsPwCfgInfoDescription':sleMplsTpMsPwCfgInfoDescription,'sleMplsTpMsPwCfgInfoMtu':sleMplsTpMsPwCfgInfoMtu,'sleMplsTpMsPwCfgInfoServiceType':sleMplsTpMsPwCfgInfoServiceType,'sleMplsTpMsPwCfgInfoVlanId':sleMplsTpMsPwCfgInfoVlanId,'sleMplsTpMsPwCfgControl':sleMplsTpMsPwCfgControl,'sleMplsTpMsPwCfgControlRequest':sleMplsTpMsPwCfgControlRequest,'sleMplsTpMsPwCfgControlStatus':sleMplsTpMsPwCfgControlStatus,'sleMplsTpMsPwCfgControlTimer':sleMplsTpMsPwCfgControlTimer,'sleMplsTpMsPwCfgControlTimestamp':sleMplsTpMsPwCfgControlTimestamp,'sleMplsTpMsPwCfgControlReqResult':sleMplsTpMsPwCfgControlReqResult,'sleMplsTpMsPwCfgControlName':sleMplsTpMsPwCfgControlName,'sleMplsTpMsPwCfgControlSegment1Name':sleMplsTpMsPwCfgControlSegment1Name,'sleMplsTpMsPwCfgControlSegment2Name':sleMplsTpMsPwCfgControlSegment2Name,'sleMplsTpMsPwCfgControlDescription':sleMplsTpMsPwCfgControlDescription,'sleMplsTpMsPwCfgControlMtu':sleMplsTpMsPwCfgControlMtu,'sleMplsTpMsPwCfgControlServiceType':sleMplsTpMsPwCfgControlServiceType,'sleMplsTpMsPwCfgControlVlanId':sleMplsTpMsPwCfgControlVlanId})