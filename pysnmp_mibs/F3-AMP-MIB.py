_A0='f3AmpStatsGroup'
_z='f3AmpConfigGroup'
_y='f3AmpStatsTxTimeStamp'
_x='f3AmpStatsLastTxStatus'
_w='f3AmpStatsRxTimeStamp'
_v='f3AmpStatsLastRxStatus'
_u='f3AmpStatsTimeoutRx'
_t='f3AmpStatsSpuriousMessageRx'
_s='f3AmpStatsConfigFailRx'
_r='f3AmpStatsConfigFailTx'
_q='f3AmpStatsConfigSuccessRx'
_p='f3AmpStatsConfigSuccessTx'
_o='f3AmpStatsProvRequestRx'
_n='f3AmpStatsProvRequestTx'
_m='f3AmpStatsProvDataRx'
_l='f3AmpStatsProvDataTx'
_k='f3AmpConfigRowStatus'
_j='f3AmpConfigStorageType'
_i='f3AmpConfigAction'
_h='f3AmpConfigRemTunnelMtu'
_g='f3AmpConfigRemTunnelEncapType'
_f='f3AmpConfigRemTunnelBufferSize'
_e='f3AmpConfigRemTunnelEIR'
_d='f3AmpConfigRemTunnelCIR'
_c='f3AmpConfigRemTunnelCOS'
_b='f3AmpConfigRemTunnelRip2PktsEnabled'
_a='f3AmpConfigRemTunnelSVlanIdEnabled'
_Z='f3AmpConfigRemTunnelSVlanId'
_Y='f3AmpConfigRemTunnelVlanId'
_X='f3AmpConfigRemTunnelIpMask'
_W='f3AmpConfigRemTunnelIpAddr'
_V='f3AmpConfigRemTunnelType'
_U='f3AmpConfigRemTunnelName'
_T='f3AmpConfigRemTunnelIndex'
_S='f3AmpConfigRemSysSrcIpAddrIfName'
_R='f3AmpConfigRemSysSrcIpAddrType'
_Q='f3AmpConfigRemSysSNMPV1IfName'
_P='f3AmpConfigRemSysDefGateway'
_O='f3AmpConfigRemSysIpMask'
_N='f3AmpConfigRemSysIpAddr'
_M='f3AmpConfigRemSysName'
_L='f3AmpConfigStatus'
_K='f3AmpConfigPort'
_J='f3AmpConfigEnabled'
_I='f3AmpConfigProtocol'
_H='f3AmpConfigRole'
_G='noPeer'
_F='f3AmpConfigIndex'
_E='Integer32'
_D='read-only'
_C='read-create'
_B='F3-AMP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsp150cm,=mibBuilder.importSymbols('ADVA-MIB','fsp150cm')
VlanId,=mibBuilder.importSymbols('CM-COMMON-MIB','VlanId')
IpManagementTunnelEncapsulationType,IpManagementTunnelType,IpSourceAddrType=mibBuilder.importSymbols('CM-IP-MIB','IpManagementTunnelEncapsulationType','IpManagementTunnelType','IpSourceAddrType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TruthValue,VariablePointer=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','StorageType','TextualConvention','TruthValue','VariablePointer')
f3AMPMIB=ModuleIdentity((1,3,6,1,4,1,2544,1,12,24))
if mibBuilder.loadTexts:f3AMPMIB.setRevisions(('2012-09-30 00:00',))
class AMPRole(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('client',1),('server',2)))
class AMPStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('notAvailable',1),('disabled',2),('associatingActive',3),('associatingPassive',4),('associated',5),(_G,6)))
class AMPConfigStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('none',1),('provision',2),(_G,3),('request',4),('configSuccess',5),('configFail',6),('timeout',7)))
class AMPProtocol(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('efmOam',1))
class AMPConfigAction(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noAction',1),('clearStats',2)))
_F3AmpConfigObjects_ObjectIdentity=ObjectIdentity
f3AmpConfigObjects=_F3AmpConfigObjects_ObjectIdentity((1,3,6,1,4,1,2544,1,12,24,1))
_F3AmpConfigTable_Object=MibTable
f3AmpConfigTable=_F3AmpConfigTable_Object((1,3,6,1,4,1,2544,1,12,24,1,1))
if mibBuilder.loadTexts:f3AmpConfigTable.setStatus(_A)
_F3AmpConfigEntry_Object=MibTableRow
f3AmpConfigEntry=_F3AmpConfigEntry_Object((1,3,6,1,4,1,2544,1,12,24,1,1,1))
f3AmpConfigEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:f3AmpConfigEntry.setStatus(_A)
class _F3AmpConfigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_F3AmpConfigIndex_Type.__name__=_E
_F3AmpConfigIndex_Object=MibTableColumn
f3AmpConfigIndex=_F3AmpConfigIndex_Object((1,3,6,1,4,1,2544,1,12,24,1,1,1,1),_F3AmpConfigIndex_Type())
f3AmpConfigIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:f3AmpConfigIndex.setStatus(_A)
_F3AmpConfigRole_Type=AMPRole
_F3AmpConfigRole_Object=MibTableColumn
f3AmpConfigRole=_F3AmpConfigRole_Object((1,3,6,1,4,1,2544,1,12,24,1,1,1,2),_F3AmpConfigRole_Type())
f3AmpConfigRole.setMaxAccess(_C)
if mibBuilder.loadTexts:f3AmpConfigRole.setStatus(_A)
_F3AmpConfigProtocol_Type=AMPProtocol
_F3AmpConfigProtocol_Object=MibTableColumn
f3AmpConfigProtocol=_F3AmpConfigProtocol_Object((1,3,6,1,4,1,2544,1,12,24,1,1,1,3),_F3AmpConfigProtocol_Type())
f3AmpConfigProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:f3AmpConfigProtocol.setStatus(_A)
_F3AmpConfigEnabled_Type=TruthValue
_F3AmpConfigEnabled_Object=MibTableColumn
f3AmpConfigEnabled=_F3AmpConfigEnabled_Object((1,3,6,1,4,1,2544,1,12,24,1,1,1,4),_F3AmpConfigEnabled_Type())
f3AmpConfigEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:f3AmpConfigEnabled.setStatus(_A)
_F3AmpConfigPort_Type=VariablePointer
_F3AmpConfigPort_Object=MibTableColumn
f3AmpConfigPort=_F3AmpConfigPort_Object((1,3,6,1,4,1,2544,1,12,24,1,1,1,5),_F3AmpConfigPort_Type())
f3AmpConfigPort.setMaxAccess(_C)
if mibBuilder.loadTexts:f3AmpConfigPort.setStatus(_A)
_F3AmpConfigStatus_Type=AMPStatus
_F3AmpConfigStatus_Object=MibTableColumn
f3AmpConfigStatus=_F3AmpConfigStatus_Object((1,3,6,1,4,1,2544,1,12,24,1,1,1,6),_F3AmpConfigStatus_Type())
f3AmpConfigStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:f3AmpConfigStatus.setStatus(_A)
_F3AmpConfigRemSysName_Type=DisplayString
_F3AmpConfigRemSysName_Object=MibTableColumn
f3AmpConfigRemSysName=_F3AmpConfigRemSysName_Object((1,3,6,1,4,1,2544,1,12,24,1,1,1,7),_F3AmpConfigRemSysName_Type())
f3AmpConfigRemSysName.setMaxAccess(_C)
if mibBuilder.loadTexts:f3AmpConfigRemSysName.setStatus(_A)
_F3AmpConfigRemSysIpAddr_Type=IpAddress
_F3AmpConfigRemSysIpAddr_Object=MibTableColumn
f3AmpConfigRemSysIpAddr=_F3AmpConfigRemSysIpAddr_Object((1,3,6,1,4,1,2544,1,12,24,1,1,1,8),_F3AmpConfigRemSysIpAddr_Type())
f3AmpConfigRemSysIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:f3AmpConfigRemSysIpAddr.setStatus(_A)
_F3AmpConfigRemSysIpMask_Type=IpAddress
_F3AmpConfigRemSysIpMask_Object=MibTableColumn
f3AmpConfigRemSysIpMask=_F3AmpConfigRemSysIpMask_Object((1,3,6,1,4,1,2544,1,12,24,1,1,1,9),_F3AmpConfigRemSysIpMask_Type())
f3AmpConfigRemSysIpMask.setMaxAccess(_C)
if mibBuilder.loadTexts:f3AmpConfigRemSysIpMask.setStatus(_A)
_F3AmpConfigRemSysDefGateway_Type=IpAddress
_F3AmpConfigRemSysDefGateway_Object=MibTableColumn
f3AmpConfigRemSysDefGateway=_F3AmpConfigRemSysDefGateway_Object((1,3,6,1,4,1,2544,1,12,24,1,1,1,10),_F3AmpConfigRemSysDefGateway_Type())
f3AmpConfigRemSysDefGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:f3AmpConfigRemSysDefGateway.setStatus(_A)
_F3AmpConfigRemSysSNMPV1IfName_Type=DisplayString
_F3AmpConfigRemSysSNMPV1IfName_Object=MibTableColumn
f3AmpConfigRemSysSNMPV1IfName=_F3AmpConfigRemSysSNMPV1IfName_Object((1,3,6,1,4,1,2544,1,12,24,1,1,1,11),_F3AmpConfigRemSysSNMPV1IfName_Type())
f3AmpConfigRemSysSNMPV1IfName.setMaxAccess(_D)
if mibBuilder.loadTexts:f3AmpConfigRemSysSNMPV1IfName.setStatus(_A)
_F3AmpConfigRemSysSrcIpAddrType_Type=IpSourceAddrType
_F3AmpConfigRemSysSrcIpAddrType_Object=MibTableColumn
f3AmpConfigRemSysSrcIpAddrType=_F3AmpConfigRemSysSrcIpAddrType_Object((1,3,6,1,4,1,2544,1,12,24,1,1,1,12),_F3AmpConfigRemSysSrcIpAddrType_Type())
f3AmpConfigRemSysSrcIpAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:f3AmpConfigRemSysSrcIpAddrType.setStatus(_A)
_F3AmpConfigRemSysSrcIpAddrIfName_Type=DisplayString
_F3AmpConfigRemSysSrcIpAddrIfName_Object=MibTableColumn
f3AmpConfigRemSysSrcIpAddrIfName=_F3AmpConfigRemSysSrcIpAddrIfName_Object((1,3,6,1,4,1,2544,1,12,24,1,1,1,13),_F3AmpConfigRemSysSrcIpAddrIfName_Type())
f3AmpConfigRemSysSrcIpAddrIfName.setMaxAccess(_D)
if mibBuilder.loadTexts:f3AmpConfigRemSysSrcIpAddrIfName.setStatus(_A)
class _F3AmpConfigRemTunnelIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_F3AmpConfigRemTunnelIndex_Type.__name__=_E
_F3AmpConfigRemTunnelIndex_Object=MibTableColumn
f3AmpConfigRemTunnelIndex=_F3AmpConfigRemTunnelIndex_Object((1,3,6,1,4,1,2544,1,12,24,1,1,1,14),_F3AmpConfigRemTunnelIndex_Type())
f3AmpConfigRemTunnelIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:f3AmpConfigRemTunnelIndex.setStatus(_A)
_F3AmpConfigRemTunnelName_Type=DisplayString
_F3AmpConfigRemTunnelName_Object=MibTableColumn
f3AmpConfigRemTunnelName=_F3AmpConfigRemTunnelName_Object((1,3,6,1,4,1,2544,1,12,24,1,1,1,15),_F3AmpConfigRemTunnelName_Type())
f3AmpConfigRemTunnelName.setMaxAccess(_C)
if mibBuilder.loadTexts:f3AmpConfigRemTunnelName.setStatus(_A)
_F3AmpConfigRemTunnelType_Type=IpManagementTunnelType
_F3AmpConfigRemTunnelType_Object=MibTableColumn
f3AmpConfigRemTunnelType=_F3AmpConfigRemTunnelType_Object((1,3,6,1,4,1,2544,1,12,24,1,1,1,16),_F3AmpConfigRemTunnelType_Type())
f3AmpConfigRemTunnelType.setMaxAccess(_C)
if mibBuilder.loadTexts:f3AmpConfigRemTunnelType.setStatus(_A)
_F3AmpConfigRemTunnelIpAddr_Type=IpAddress
_F3AmpConfigRemTunnelIpAddr_Object=MibTableColumn
f3AmpConfigRemTunnelIpAddr=_F3AmpConfigRemTunnelIpAddr_Object((1,3,6,1,4,1,2544,1,12,24,1,1,1,17),_F3AmpConfigRemTunnelIpAddr_Type())
f3AmpConfigRemTunnelIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:f3AmpConfigRemTunnelIpAddr.setStatus(_A)
_F3AmpConfigRemTunnelIpMask_Type=IpAddress
_F3AmpConfigRemTunnelIpMask_Object=MibTableColumn
f3AmpConfigRemTunnelIpMask=_F3AmpConfigRemTunnelIpMask_Object((1,3,6,1,4,1,2544,1,12,24,1,1,1,18),_F3AmpConfigRemTunnelIpMask_Type())
f3AmpConfigRemTunnelIpMask.setMaxAccess(_C)
if mibBuilder.loadTexts:f3AmpConfigRemTunnelIpMask.setStatus(_A)
_F3AmpConfigRemTunnelVlanId_Type=VlanId
_F3AmpConfigRemTunnelVlanId_Object=MibTableColumn
f3AmpConfigRemTunnelVlanId=_F3AmpConfigRemTunnelVlanId_Object((1,3,6,1,4,1,2544,1,12,24,1,1,1,19),_F3AmpConfigRemTunnelVlanId_Type())
f3AmpConfigRemTunnelVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:f3AmpConfigRemTunnelVlanId.setStatus(_A)
_F3AmpConfigRemTunnelSVlanId_Type=VlanId
_F3AmpConfigRemTunnelSVlanId_Object=MibTableColumn
f3AmpConfigRemTunnelSVlanId=_F3AmpConfigRemTunnelSVlanId_Object((1,3,6,1,4,1,2544,1,12,24,1,1,1,20),_F3AmpConfigRemTunnelSVlanId_Type())
f3AmpConfigRemTunnelSVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:f3AmpConfigRemTunnelSVlanId.setStatus(_A)
_F3AmpConfigRemTunnelSVlanIdEnabled_Type=TruthValue
_F3AmpConfigRemTunnelSVlanIdEnabled_Object=MibTableColumn
f3AmpConfigRemTunnelSVlanIdEnabled=_F3AmpConfigRemTunnelSVlanIdEnabled_Object((1,3,6,1,4,1,2544,1,12,24,1,1,1,21),_F3AmpConfigRemTunnelSVlanIdEnabled_Type())
f3AmpConfigRemTunnelSVlanIdEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:f3AmpConfigRemTunnelSVlanIdEnabled.setStatus(_A)
_F3AmpConfigRemTunnelRip2PktsEnabled_Type=TruthValue
_F3AmpConfigRemTunnelRip2PktsEnabled_Object=MibTableColumn
f3AmpConfigRemTunnelRip2PktsEnabled=_F3AmpConfigRemTunnelRip2PktsEnabled_Object((1,3,6,1,4,1,2544,1,12,24,1,1,1,22),_F3AmpConfigRemTunnelRip2PktsEnabled_Type())
f3AmpConfigRemTunnelRip2PktsEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:f3AmpConfigRemTunnelRip2PktsEnabled.setStatus(_A)
class _F3AmpConfigRemTunnelCOS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_F3AmpConfigRemTunnelCOS_Type.__name__=_E
_F3AmpConfigRemTunnelCOS_Object=MibTableColumn
f3AmpConfigRemTunnelCOS=_F3AmpConfigRemTunnelCOS_Object((1,3,6,1,4,1,2544,1,12,24,1,1,1,23),_F3AmpConfigRemTunnelCOS_Type())
f3AmpConfigRemTunnelCOS.setMaxAccess(_C)
if mibBuilder.loadTexts:f3AmpConfigRemTunnelCOS.setStatus(_A)
_F3AmpConfigRemTunnelCIR_Type=Unsigned32
_F3AmpConfigRemTunnelCIR_Object=MibTableColumn
f3AmpConfigRemTunnelCIR=_F3AmpConfigRemTunnelCIR_Object((1,3,6,1,4,1,2544,1,12,24,1,1,1,24),_F3AmpConfigRemTunnelCIR_Type())
f3AmpConfigRemTunnelCIR.setMaxAccess(_C)
if mibBuilder.loadTexts:f3AmpConfigRemTunnelCIR.setStatus(_A)
_F3AmpConfigRemTunnelEIR_Type=Unsigned32
_F3AmpConfigRemTunnelEIR_Object=MibTableColumn
f3AmpConfigRemTunnelEIR=_F3AmpConfigRemTunnelEIR_Object((1,3,6,1,4,1,2544,1,12,24,1,1,1,25),_F3AmpConfigRemTunnelEIR_Type())
f3AmpConfigRemTunnelEIR.setMaxAccess(_C)
if mibBuilder.loadTexts:f3AmpConfigRemTunnelEIR.setStatus(_A)
_F3AmpConfigRemTunnelBufferSize_Type=Unsigned32
_F3AmpConfigRemTunnelBufferSize_Object=MibTableColumn
f3AmpConfigRemTunnelBufferSize=_F3AmpConfigRemTunnelBufferSize_Object((1,3,6,1,4,1,2544,1,12,24,1,1,1,26),_F3AmpConfigRemTunnelBufferSize_Type())
f3AmpConfigRemTunnelBufferSize.setMaxAccess(_C)
if mibBuilder.loadTexts:f3AmpConfigRemTunnelBufferSize.setStatus(_A)
_F3AmpConfigRemTunnelEncapType_Type=IpManagementTunnelEncapsulationType
_F3AmpConfigRemTunnelEncapType_Object=MibTableColumn
f3AmpConfigRemTunnelEncapType=_F3AmpConfigRemTunnelEncapType_Object((1,3,6,1,4,1,2544,1,12,24,1,1,1,27),_F3AmpConfigRemTunnelEncapType_Type())
f3AmpConfigRemTunnelEncapType.setMaxAccess(_C)
if mibBuilder.loadTexts:f3AmpConfigRemTunnelEncapType.setStatus(_A)
_F3AmpConfigRemTunnelMtu_Type=Integer32
_F3AmpConfigRemTunnelMtu_Object=MibTableColumn
f3AmpConfigRemTunnelMtu=_F3AmpConfigRemTunnelMtu_Object((1,3,6,1,4,1,2544,1,12,24,1,1,1,28),_F3AmpConfigRemTunnelMtu_Type())
f3AmpConfigRemTunnelMtu.setMaxAccess(_C)
if mibBuilder.loadTexts:f3AmpConfigRemTunnelMtu.setStatus(_A)
_F3AmpConfigAction_Type=AMPConfigAction
_F3AmpConfigAction_Object=MibTableColumn
f3AmpConfigAction=_F3AmpConfigAction_Object((1,3,6,1,4,1,2544,1,12,24,1,1,1,29),_F3AmpConfigAction_Type())
f3AmpConfigAction.setMaxAccess(_C)
if mibBuilder.loadTexts:f3AmpConfigAction.setStatus(_A)
_F3AmpConfigStorageType_Type=StorageType
_F3AmpConfigStorageType_Object=MibTableColumn
f3AmpConfigStorageType=_F3AmpConfigStorageType_Object((1,3,6,1,4,1,2544,1,12,24,1,1,1,30),_F3AmpConfigStorageType_Type())
f3AmpConfigStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:f3AmpConfigStorageType.setStatus(_A)
_F3AmpConfigRowStatus_Type=RowStatus
_F3AmpConfigRowStatus_Object=MibTableColumn
f3AmpConfigRowStatus=_F3AmpConfigRowStatus_Object((1,3,6,1,4,1,2544,1,12,24,1,1,1,31),_F3AmpConfigRowStatus_Type())
f3AmpConfigRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:f3AmpConfigRowStatus.setStatus(_A)
_F3AmpStatsObjects_ObjectIdentity=ObjectIdentity
f3AmpStatsObjects=_F3AmpStatsObjects_ObjectIdentity((1,3,6,1,4,1,2544,1,12,24,2))
_F3AmpStatsTable_Object=MibTable
f3AmpStatsTable=_F3AmpStatsTable_Object((1,3,6,1,4,1,2544,1,12,24,2,1))
if mibBuilder.loadTexts:f3AmpStatsTable.setStatus(_A)
_F3AmpStatsEntry_Object=MibTableRow
f3AmpStatsEntry=_F3AmpStatsEntry_Object((1,3,6,1,4,1,2544,1,12,24,2,1,1))
f3AmpStatsEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:f3AmpStatsEntry.setStatus(_A)
_F3AmpStatsProvDataTx_Type=Unsigned32
_F3AmpStatsProvDataTx_Object=MibTableColumn
f3AmpStatsProvDataTx=_F3AmpStatsProvDataTx_Object((1,3,6,1,4,1,2544,1,12,24,2,1,1,1),_F3AmpStatsProvDataTx_Type())
f3AmpStatsProvDataTx.setMaxAccess(_D)
if mibBuilder.loadTexts:f3AmpStatsProvDataTx.setStatus(_A)
_F3AmpStatsProvDataRx_Type=Unsigned32
_F3AmpStatsProvDataRx_Object=MibTableColumn
f3AmpStatsProvDataRx=_F3AmpStatsProvDataRx_Object((1,3,6,1,4,1,2544,1,12,24,2,1,1,2),_F3AmpStatsProvDataRx_Type())
f3AmpStatsProvDataRx.setMaxAccess(_D)
if mibBuilder.loadTexts:f3AmpStatsProvDataRx.setStatus(_A)
_F3AmpStatsProvRequestTx_Type=Unsigned32
_F3AmpStatsProvRequestTx_Object=MibTableColumn
f3AmpStatsProvRequestTx=_F3AmpStatsProvRequestTx_Object((1,3,6,1,4,1,2544,1,12,24,2,1,1,3),_F3AmpStatsProvRequestTx_Type())
f3AmpStatsProvRequestTx.setMaxAccess(_D)
if mibBuilder.loadTexts:f3AmpStatsProvRequestTx.setStatus(_A)
_F3AmpStatsProvRequestRx_Type=Unsigned32
_F3AmpStatsProvRequestRx_Object=MibTableColumn
f3AmpStatsProvRequestRx=_F3AmpStatsProvRequestRx_Object((1,3,6,1,4,1,2544,1,12,24,2,1,1,4),_F3AmpStatsProvRequestRx_Type())
f3AmpStatsProvRequestRx.setMaxAccess(_D)
if mibBuilder.loadTexts:f3AmpStatsProvRequestRx.setStatus(_A)
_F3AmpStatsConfigSuccessTx_Type=Unsigned32
_F3AmpStatsConfigSuccessTx_Object=MibTableColumn
f3AmpStatsConfigSuccessTx=_F3AmpStatsConfigSuccessTx_Object((1,3,6,1,4,1,2544,1,12,24,2,1,1,5),_F3AmpStatsConfigSuccessTx_Type())
f3AmpStatsConfigSuccessTx.setMaxAccess(_D)
if mibBuilder.loadTexts:f3AmpStatsConfigSuccessTx.setStatus(_A)
_F3AmpStatsConfigSuccessRx_Type=Unsigned32
_F3AmpStatsConfigSuccessRx_Object=MibTableColumn
f3AmpStatsConfigSuccessRx=_F3AmpStatsConfigSuccessRx_Object((1,3,6,1,4,1,2544,1,12,24,2,1,1,6),_F3AmpStatsConfigSuccessRx_Type())
f3AmpStatsConfigSuccessRx.setMaxAccess(_D)
if mibBuilder.loadTexts:f3AmpStatsConfigSuccessRx.setStatus(_A)
_F3AmpStatsConfigFailTx_Type=Unsigned32
_F3AmpStatsConfigFailTx_Object=MibTableColumn
f3AmpStatsConfigFailTx=_F3AmpStatsConfigFailTx_Object((1,3,6,1,4,1,2544,1,12,24,2,1,1,7),_F3AmpStatsConfigFailTx_Type())
f3AmpStatsConfigFailTx.setMaxAccess(_D)
if mibBuilder.loadTexts:f3AmpStatsConfigFailTx.setStatus(_A)
_F3AmpStatsConfigFailRx_Type=Unsigned32
_F3AmpStatsConfigFailRx_Object=MibTableColumn
f3AmpStatsConfigFailRx=_F3AmpStatsConfigFailRx_Object((1,3,6,1,4,1,2544,1,12,24,2,1,1,8),_F3AmpStatsConfigFailRx_Type())
f3AmpStatsConfigFailRx.setMaxAccess(_D)
if mibBuilder.loadTexts:f3AmpStatsConfigFailRx.setStatus(_A)
_F3AmpStatsSpuriousMessageRx_Type=Unsigned32
_F3AmpStatsSpuriousMessageRx_Object=MibTableColumn
f3AmpStatsSpuriousMessageRx=_F3AmpStatsSpuriousMessageRx_Object((1,3,6,1,4,1,2544,1,12,24,2,1,1,9),_F3AmpStatsSpuriousMessageRx_Type())
f3AmpStatsSpuriousMessageRx.setMaxAccess(_D)
if mibBuilder.loadTexts:f3AmpStatsSpuriousMessageRx.setStatus(_A)
_F3AmpStatsTimeoutRx_Type=Unsigned32
_F3AmpStatsTimeoutRx_Object=MibTableColumn
f3AmpStatsTimeoutRx=_F3AmpStatsTimeoutRx_Object((1,3,6,1,4,1,2544,1,12,24,2,1,1,10),_F3AmpStatsTimeoutRx_Type())
f3AmpStatsTimeoutRx.setMaxAccess(_D)
if mibBuilder.loadTexts:f3AmpStatsTimeoutRx.setStatus(_A)
_F3AmpStatsLastRxStatus_Type=AMPConfigStatus
_F3AmpStatsLastRxStatus_Object=MibTableColumn
f3AmpStatsLastRxStatus=_F3AmpStatsLastRxStatus_Object((1,3,6,1,4,1,2544,1,12,24,2,1,1,11),_F3AmpStatsLastRxStatus_Type())
f3AmpStatsLastRxStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:f3AmpStatsLastRxStatus.setStatus(_A)
_F3AmpStatsRxTimeStamp_Type=DateAndTime
_F3AmpStatsRxTimeStamp_Object=MibTableColumn
f3AmpStatsRxTimeStamp=_F3AmpStatsRxTimeStamp_Object((1,3,6,1,4,1,2544,1,12,24,2,1,1,12),_F3AmpStatsRxTimeStamp_Type())
f3AmpStatsRxTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:f3AmpStatsRxTimeStamp.setStatus(_A)
_F3AmpStatsLastTxStatus_Type=AMPConfigStatus
_F3AmpStatsLastTxStatus_Object=MibTableColumn
f3AmpStatsLastTxStatus=_F3AmpStatsLastTxStatus_Object((1,3,6,1,4,1,2544,1,12,24,2,1,1,13),_F3AmpStatsLastTxStatus_Type())
f3AmpStatsLastTxStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:f3AmpStatsLastTxStatus.setStatus(_A)
_F3AmpStatsTxTimeStamp_Type=DateAndTime
_F3AmpStatsTxTimeStamp_Object=MibTableColumn
f3AmpStatsTxTimeStamp=_F3AmpStatsTxTimeStamp_Object((1,3,6,1,4,1,2544,1,12,24,2,1,1,14),_F3AmpStatsTxTimeStamp_Type())
f3AmpStatsTxTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:f3AmpStatsTxTimeStamp.setStatus(_A)
_F3AmpConformance_ObjectIdentity=ObjectIdentity
f3AmpConformance=_F3AmpConformance_ObjectIdentity((1,3,6,1,4,1,2544,1,12,24,3))
_F3AmpCompliances_ObjectIdentity=ObjectIdentity
f3AmpCompliances=_F3AmpCompliances_ObjectIdentity((1,3,6,1,4,1,2544,1,12,24,3,1))
_F3AmpGroups_ObjectIdentity=ObjectIdentity
f3AmpGroups=_F3AmpGroups_ObjectIdentity((1,3,6,1,4,1,2544,1,12,24,3,2))
f3AmpConfigGroup=ObjectGroup((1,3,6,1,4,1,2544,1,12,24,3,2,1))
f3AmpConfigGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k)))
if mibBuilder.loadTexts:f3AmpConfigGroup.setStatus(_A)
f3AmpStatsGroup=ObjectGroup((1,3,6,1,4,1,2544,1,12,24,3,2,2))
f3AmpStatsGroup.setObjects(*((_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y)))
if mibBuilder.loadTexts:f3AmpStatsGroup.setStatus(_A)
f3AmpCompliance=ModuleCompliance((1,3,6,1,4,1,2544,1,12,24,3,1,1))
f3AmpCompliance.setObjects(*((_B,_z),(_B,_A0)))
if mibBuilder.loadTexts:f3AmpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'AMPRole':AMPRole,'AMPStatus':AMPStatus,'AMPConfigStatus':AMPConfigStatus,'AMPProtocol':AMPProtocol,'AMPConfigAction':AMPConfigAction,'f3AMPMIB':f3AMPMIB,'f3AmpConfigObjects':f3AmpConfigObjects,'f3AmpConfigTable':f3AmpConfigTable,'f3AmpConfigEntry':f3AmpConfigEntry,_F:f3AmpConfigIndex,_H:f3AmpConfigRole,_I:f3AmpConfigProtocol,_J:f3AmpConfigEnabled,_K:f3AmpConfigPort,_L:f3AmpConfigStatus,_M:f3AmpConfigRemSysName,_N:f3AmpConfigRemSysIpAddr,_O:f3AmpConfigRemSysIpMask,_P:f3AmpConfigRemSysDefGateway,_Q:f3AmpConfigRemSysSNMPV1IfName,_R:f3AmpConfigRemSysSrcIpAddrType,_S:f3AmpConfigRemSysSrcIpAddrIfName,_T:f3AmpConfigRemTunnelIndex,_U:f3AmpConfigRemTunnelName,_V:f3AmpConfigRemTunnelType,_W:f3AmpConfigRemTunnelIpAddr,_X:f3AmpConfigRemTunnelIpMask,_Y:f3AmpConfigRemTunnelVlanId,_Z:f3AmpConfigRemTunnelSVlanId,_a:f3AmpConfigRemTunnelSVlanIdEnabled,_b:f3AmpConfigRemTunnelRip2PktsEnabled,_c:f3AmpConfigRemTunnelCOS,_d:f3AmpConfigRemTunnelCIR,_e:f3AmpConfigRemTunnelEIR,_f:f3AmpConfigRemTunnelBufferSize,_g:f3AmpConfigRemTunnelEncapType,_h:f3AmpConfigRemTunnelMtu,_i:f3AmpConfigAction,_j:f3AmpConfigStorageType,_k:f3AmpConfigRowStatus,'f3AmpStatsObjects':f3AmpStatsObjects,'f3AmpStatsTable':f3AmpStatsTable,'f3AmpStatsEntry':f3AmpStatsEntry,_l:f3AmpStatsProvDataTx,_m:f3AmpStatsProvDataRx,_n:f3AmpStatsProvRequestTx,_o:f3AmpStatsProvRequestRx,_p:f3AmpStatsConfigSuccessTx,_q:f3AmpStatsConfigSuccessRx,_r:f3AmpStatsConfigFailTx,_s:f3AmpStatsConfigFailRx,_t:f3AmpStatsSpuriousMessageRx,_u:f3AmpStatsTimeoutRx,_v:f3AmpStatsLastRxStatus,_w:f3AmpStatsRxTimeStamp,_x:f3AmpStatsLastTxStatus,_y:f3AmpStatsTxTimeStamp,'f3AmpConformance':f3AmpConformance,'f3AmpCompliances':f3AmpCompliances,'f3AmpCompliance':f3AmpCompliance,'f3AmpGroups':f3AmpGroups,_z:f3AmpConfigGroup,_A0:f3AmpStatsGroup})