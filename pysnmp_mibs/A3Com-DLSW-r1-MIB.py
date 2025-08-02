_q='endStationDlcError'
_p='endStationDiscRcvd'
_o='dlswDirNBIndex'
_n='notReachable'
_m='reachable'
_l='dynamic'
_k='partnerCapExMsg'
_j='userConfiguredPrivate'
_i='userConfiguredPublic'
_h='MacAddress'
_g='dlswDirMacIndex'
_f='notApplicable'
_e='complete'
_d='partial'
_c='disconnected'
_b='connected'
_a='Truthvalue'
_Z='individual'
_Y='dlswTConnConfigIndex'
_X='disabled'
_W='enabled'
_V='active'
_U='NotificationType'
_T='protocolError'
_S='operatorCommand'
_R='none'
_Q='local'
_P='remote'
_O='DisplayString'
_N='dlswCircuitS2Sap'
_M='dlswCircuitS2Mac'
_L='dlswCircuitS1Sap'
_K='dlswCircuitS1Mac'
_J='unknown'
_I='dlswTConnOperRemoteTAddr'
_H='dlswTConnOperTDomain'
_G='other'
_F='OctetString'
_E='read-write'
_D='A3Com-DLSW-r1-MIB'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier',_U,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_U,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_O,'PhysAddress','TextualConvention')
class NBName(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
class MacAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
class TAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
class DlswTimeStamp(TimeTicks):0
class EndStationLocation(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),('internal',2),(_P,3),(_Q,4)))
class DlcType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),('na',2),('llc',3),('sdlc',4)))
class LFSize(Integer32):0
class Truthvalue(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('false',1),('true',2)))
class RowStatus(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_V,1),('notInService',2),('notReady',3),('createAndGo',4),('createAndWait',5),('destroy',6)))
class Instancepointer(Integer32):0
_A3Com_ObjectIdentity=ObjectIdentity
a3Com=_A3Com_ObjectIdentity((1,3,6,1,4,1,43))
_BrouterMIB_ObjectIdentity=ObjectIdentity
brouterMIB=_BrouterMIB_ObjectIdentity((1,3,6,1,4,1,43,2))
_DlswMIB_3Com_ObjectIdentity=ObjectIdentity
dlswMIB_3Com=_DlswMIB_3Com_ObjectIdentity((1,3,6,1,4,1,43,2,24))
_DlswNode_ObjectIdentity=ObjectIdentity
dlswNode=_DlswNode_ObjectIdentity((1,3,6,1,4,1,43,2,24,1))
class _DlswVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_DlswVersion_Type.__name__=_F
_DlswVersion_Object=MibScalar
dlswVersion=_DlswVersion_Object((1,3,6,1,4,1,43,2,24,1,1),_DlswVersion_Type())
dlswVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswVersion.setStatus(_A)
class _DlswVendorID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_DlswVendorID_Type.__name__=_F
_DlswVendorID_Object=MibScalar
dlswVendorID=_DlswVendorID_Object((1,3,6,1,4,1,43,2,24,1,2),_DlswVendorID_Type())
dlswVendorID.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswVendorID.setStatus(_A)
class _DlswVersionString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DlswVersionString_Type.__name__=_O
_DlswVersionString_Object=MibScalar
dlswVersionString=_DlswVersionString_Object((1,3,6,1,4,1,43,2,24,1,3),_DlswVersionString_Type())
dlswVersionString.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswVersionString.setStatus(_A)
class _DlswStdPacingSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_R,1),('adaptiveRcvWindow',2),('fixedRcvWindow',3)))
_DlswStdPacingSupport_Type.__name__=_C
_DlswStdPacingSupport_Object=MibScalar
dlswStdPacingSupport=_DlswStdPacingSupport_Object((1,3,6,1,4,1,43,2,24,1,4),_DlswStdPacingSupport_Type())
dlswStdPacingSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswStdPacingSupport.setStatus(_A)
class _DlswStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_V,1),('inactive',2)))
_DlswStatus_Type.__name__=_C
_DlswStatus_Object=MibScalar
dlswStatus=_DlswStatus_Object((1,3,6,1,4,1,43,2,24,1,5),_DlswStatus_Type())
dlswStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:dlswStatus.setStatus(_A)
_DlswUpTime_Type=TimeTicks
_DlswUpTime_Object=MibScalar
dlswUpTime=_DlswUpTime_Object((1,3,6,1,4,1,43,2,24,1,6),_DlswUpTime_Type())
dlswUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswUpTime.setStatus(_A)
_DlswVirtualSegmentLFSize_Type=Integer32
_DlswVirtualSegmentLFSize_Object=MibScalar
dlswVirtualSegmentLFSize=_DlswVirtualSegmentLFSize_Object((1,3,6,1,4,1,43,2,24,1,7),_DlswVirtualSegmentLFSize_Type())
dlswVirtualSegmentLFSize.setMaxAccess(_E)
if mibBuilder.loadTexts:dlswVirtualSegmentLFSize.setStatus(_A)
_DlswResourceNBExclusivity_Type=Truthvalue
_DlswResourceNBExclusivity_Object=MibScalar
dlswResourceNBExclusivity=_DlswResourceNBExclusivity_Object((1,3,6,1,4,1,43,2,24,1,8),_DlswResourceNBExclusivity_Type())
dlswResourceNBExclusivity.setMaxAccess(_E)
if mibBuilder.loadTexts:dlswResourceNBExclusivity.setStatus(_A)
_DlswResourceMacExclusivity_Type=Truthvalue
_DlswResourceMacExclusivity_Object=MibScalar
dlswResourceMacExclusivity=_DlswResourceMacExclusivity_Object((1,3,6,1,4,1,43,2,24,1,9),_DlswResourceMacExclusivity_Type())
dlswResourceMacExclusivity.setMaxAccess(_E)
if mibBuilder.loadTexts:dlswResourceMacExclusivity.setStatus(_A)
_DlswTrapControl_ObjectIdentity=ObjectIdentity
dlswTrapControl=_DlswTrapControl_ObjectIdentity((1,3,6,1,4,1,43,2,24,1,10))
class _DlswTrapCntlTConn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),(_X,2)))
_DlswTrapCntlTConn_Type.__name__=_C
_DlswTrapCntlTConn_Object=MibScalar
dlswTrapCntlTConn=_DlswTrapCntlTConn_Object((1,3,6,1,4,1,43,2,24,1,10,3),_DlswTrapCntlTConn_Type())
dlswTrapCntlTConn.setMaxAccess(_E)
if mibBuilder.loadTexts:dlswTrapCntlTConn.setStatus(_A)
class _DlswTrapCntlCircuit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),(_X,2)))
_DlswTrapCntlCircuit_Type.__name__=_C
_DlswTrapCntlCircuit_Object=MibScalar
dlswTrapCntlCircuit=_DlswTrapCntlCircuit_Object((1,3,6,1,4,1,43,2,24,1,10,4),_DlswTrapCntlCircuit_Type())
dlswTrapCntlCircuit.setMaxAccess(_E)
if mibBuilder.loadTexts:dlswTrapCntlCircuit.setStatus(_A)
_DlswTConn_ObjectIdentity=ObjectIdentity
dlswTConn=_DlswTConn_ObjectIdentity((1,3,6,1,4,1,43,2,24,2))
_DlswTConnStat_ObjectIdentity=ObjectIdentity
dlswTConnStat=_DlswTConnStat_ObjectIdentity((1,3,6,1,4,1,43,2,24,2,1))
_DlswTConnStatActiveConnections_Type=Gauge32
_DlswTConnStatActiveConnections_Object=MibScalar
dlswTConnStatActiveConnections=_DlswTConnStatActiveConnections_Object((1,3,6,1,4,1,43,2,24,2,1,1),_DlswTConnStatActiveConnections_Type())
dlswTConnStatActiveConnections.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswTConnStatActiveConnections.setStatus(_A)
_DlswTConnStatCloseIdles_Type=Counter32
_DlswTConnStatCloseIdles_Object=MibScalar
dlswTConnStatCloseIdles=_DlswTConnStatCloseIdles_Object((1,3,6,1,4,1,43,2,24,2,1,2),_DlswTConnStatCloseIdles_Type())
dlswTConnStatCloseIdles.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswTConnStatCloseIdles.setStatus(_A)
_DlswTConnStatCloseBusys_Type=Counter32
_DlswTConnStatCloseBusys_Object=MibScalar
dlswTConnStatCloseBusys=_DlswTConnStatCloseBusys_Object((1,3,6,1,4,1,43,2,24,2,1,3),_DlswTConnStatCloseBusys_Type())
dlswTConnStatCloseBusys.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswTConnStatCloseBusys.setStatus(_A)
_DlswTConnConfigTable_Object=MibTable
dlswTConnConfigTable=_DlswTConnConfigTable_Object((1,3,6,1,4,1,43,2,24,2,2))
if mibBuilder.loadTexts:dlswTConnConfigTable.setStatus(_A)
_DlswTConnConfigEntry_Object=MibTableRow
dlswTConnConfigEntry=_DlswTConnConfigEntry_Object((1,3,6,1,4,1,43,2,24,2,2,1))
dlswTConnConfigEntry.setIndexNames((0,_D,_Y))
if mibBuilder.loadTexts:dlswTConnConfigEntry.setStatus(_A)
_DlswTConnConfigIndex_Type=Integer32
_DlswTConnConfigIndex_Object=MibTableColumn
dlswTConnConfigIndex=_DlswTConnConfigIndex_Object((1,3,6,1,4,1,43,2,24,2,2,1,1),_DlswTConnConfigIndex_Type())
dlswTConnConfigIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswTConnConfigIndex.setStatus(_A)
_DlswTConnConfigTDomain_Type=ObjectIdentifier
_DlswTConnConfigTDomain_Object=MibTableColumn
dlswTConnConfigTDomain=_DlswTConnConfigTDomain_Object((1,3,6,1,4,1,43,2,24,2,2,1,2),_DlswTConnConfigTDomain_Type())
dlswTConnConfigTDomain.setMaxAccess(_E)
if mibBuilder.loadTexts:dlswTConnConfigTDomain.setStatus(_A)
_DlswTConnConfigLocalTAddr_Type=TAddress
_DlswTConnConfigLocalTAddr_Object=MibTableColumn
dlswTConnConfigLocalTAddr=_DlswTConnConfigLocalTAddr_Object((1,3,6,1,4,1,43,2,24,2,2,1,3),_DlswTConnConfigLocalTAddr_Type())
dlswTConnConfigLocalTAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:dlswTConnConfigLocalTAddr.setStatus(_A)
_DlswTConnConfigRemoteTAddr_Type=TAddress
_DlswTConnConfigRemoteTAddr_Object=MibTableColumn
dlswTConnConfigRemoteTAddr=_DlswTConnConfigRemoteTAddr_Object((1,3,6,1,4,1,43,2,24,2,2,1,4),_DlswTConnConfigRemoteTAddr_Type())
dlswTConnConfigRemoteTAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:dlswTConnConfigRemoteTAddr.setStatus(_A)
_DlswTConnConfigLastModifyTime_Type=DlswTimeStamp
_DlswTConnConfigLastModifyTime_Object=MibTableColumn
dlswTConnConfigLastModifyTime=_DlswTConnConfigLastModifyTime_Object((1,3,6,1,4,1,43,2,24,2,2,1,5),_DlswTConnConfigLastModifyTime_Type())
dlswTConnConfigLastModifyTime.setMaxAccess(_E)
if mibBuilder.loadTexts:dlswTConnConfigLastModifyTime.setStatus(_A)
class _DlswTConnConfigEntryType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Z,1),('global',2),('group',3)))
_DlswTConnConfigEntryType_Type.__name__=_C
_DlswTConnConfigEntryType_Object=MibTableColumn
dlswTConnConfigEntryType=_DlswTConnConfigEntryType_Object((1,3,6,1,4,1,43,2,24,2,2,1,6),_DlswTConnConfigEntryType_Type())
dlswTConnConfigEntryType.setMaxAccess(_E)
if mibBuilder.loadTexts:dlswTConnConfigEntryType.setStatus(_A)
_DlswTConnConfigGroupDefinition_Type=Instancepointer
_DlswTConnConfigGroupDefinition_Object=MibTableColumn
dlswTConnConfigGroupDefinition=_DlswTConnConfigGroupDefinition_Object((1,3,6,1,4,1,43,2,24,2,2,1,7),_DlswTConnConfigGroupDefinition_Type())
dlswTConnConfigGroupDefinition.setMaxAccess(_E)
if mibBuilder.loadTexts:dlswTConnConfigGroupDefinition.setStatus(_A)
class _DlswTConnConfigSetupType_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_G,1),('activePersistent',2),('activeOnDemand',3),('passive',4),('excluded',5)))
_DlswTConnConfigSetupType_Type.__name__=_C
_DlswTConnConfigSetupType_Object=MibTableColumn
dlswTConnConfigSetupType=_DlswTConnConfigSetupType_Object((1,3,6,1,4,1,43,2,24,2,2,1,8),_DlswTConnConfigSetupType_Type())
dlswTConnConfigSetupType.setMaxAccess(_E)
if mibBuilder.loadTexts:dlswTConnConfigSetupType.setStatus(_A)
class _DlswTConnConfigSapList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_DlswTConnConfigSapList_Type.__name__=_F
_DlswTConnConfigSapList_Object=MibTableColumn
dlswTConnConfigSapList=_DlswTConnConfigSapList_Object((1,3,6,1,4,1,43,2,24,2,2,1,9),_DlswTConnConfigSapList_Type())
dlswTConnConfigSapList.setMaxAccess(_E)
if mibBuilder.loadTexts:dlswTConnConfigSapList.setStatus(_A)
class _DlswTConnConfigAdvertiseMacNB_Type(Truthvalue):defaultValue=2
_DlswTConnConfigAdvertiseMacNB_Type.__name__=_a
_DlswTConnConfigAdvertiseMacNB_Object=MibTableColumn
dlswTConnConfigAdvertiseMacNB=_DlswTConnConfigAdvertiseMacNB_Object((1,3,6,1,4,1,43,2,24,2,2,1,10),_DlswTConnConfigAdvertiseMacNB_Type())
dlswTConnConfigAdvertiseMacNB.setMaxAccess(_E)
if mibBuilder.loadTexts:dlswTConnConfigAdvertiseMacNB.setStatus(_A)
class _DlswTConnConfigInitCirRecvWndw_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DlswTConnConfigInitCirRecvWndw_Type.__name__=_C
_DlswTConnConfigInitCirRecvWndw_Object=MibTableColumn
dlswTConnConfigInitCirRecvWndw=_DlswTConnConfigInitCirRecvWndw_Object((1,3,6,1,4,1,43,2,24,2,2,1,11),_DlswTConnConfigInitCirRecvWndw_Type())
dlswTConnConfigInitCirRecvWndw.setMaxAccess(_E)
if mibBuilder.loadTexts:dlswTConnConfigInitCirRecvWndw.setStatus(_A)
_DlswTConnConfigOpens_Type=Counter32
_DlswTConnConfigOpens_Object=MibTableColumn
dlswTConnConfigOpens=_DlswTConnConfigOpens_Object((1,3,6,1,4,1,43,2,24,2,2,1,12),_DlswTConnConfigOpens_Type())
dlswTConnConfigOpens.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswTConnConfigOpens.setStatus(_A)
_DlswTConnConfigRowStatus_Type=RowStatus
_DlswTConnConfigRowStatus_Object=MibTableColumn
dlswTConnConfigRowStatus=_DlswTConnConfigRowStatus_Object((1,3,6,1,4,1,43,2,24,2,2,1,13),_DlswTConnConfigRowStatus_Type())
dlswTConnConfigRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:dlswTConnConfigRowStatus.setStatus(_A)
_DlswTConnOperTable_Object=MibTable
dlswTConnOperTable=_DlswTConnOperTable_Object((1,3,6,1,4,1,43,2,24,2,3))
if mibBuilder.loadTexts:dlswTConnOperTable.setStatus(_A)
_DlswTConnOperEntry_Object=MibTableRow
dlswTConnOperEntry=_DlswTConnOperEntry_Object((1,3,6,1,4,1,43,2,24,2,3,1))
dlswTConnOperEntry.setIndexNames((0,_D,_H),(0,_D,_I))
if mibBuilder.loadTexts:dlswTConnOperEntry.setStatus(_A)
_DlswTConnOperTDomain_Type=ObjectIdentifier
_DlswTConnOperTDomain_Object=MibTableColumn
dlswTConnOperTDomain=_DlswTConnOperTDomain_Object((1,3,6,1,4,1,43,2,24,2,3,1,1),_DlswTConnOperTDomain_Type())
dlswTConnOperTDomain.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswTConnOperTDomain.setStatus(_A)
_DlswTConnOperLocalTAddr_Type=TAddress
_DlswTConnOperLocalTAddr_Object=MibTableColumn
dlswTConnOperLocalTAddr=_DlswTConnOperLocalTAddr_Object((1,3,6,1,4,1,43,2,24,2,3,1,2),_DlswTConnOperLocalTAddr_Type())
dlswTConnOperLocalTAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswTConnOperLocalTAddr.setStatus(_A)
_DlswTConnOperRemoteTAddr_Type=TAddress
_DlswTConnOperRemoteTAddr_Object=MibTableColumn
dlswTConnOperRemoteTAddr=_DlswTConnOperRemoteTAddr_Object((1,3,6,1,4,1,43,2,24,2,3,1,3),_DlswTConnOperRemoteTAddr_Type())
dlswTConnOperRemoteTAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswTConnOperRemoteTAddr.setStatus(_A)
_DlswTConnOperEntryTime_Type=DlswTimeStamp
_DlswTConnOperEntryTime_Object=MibTableColumn
dlswTConnOperEntryTime=_DlswTConnOperEntryTime_Object((1,3,6,1,4,1,43,2,24,2,3,1,4),_DlswTConnOperEntryTime_Type())
dlswTConnOperEntryTime.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswTConnOperEntryTime.setStatus(_A)
_DlswTConnOperConnectTime_Type=DlswTimeStamp
_DlswTConnOperConnectTime_Object=MibTableColumn
dlswTConnOperConnectTime=_DlswTConnOperConnectTime_Object((1,3,6,1,4,1,43,2,24,2,3,1,5),_DlswTConnOperConnectTime_Type())
dlswTConnOperConnectTime.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswTConnOperConnectTime.setStatus(_A)
class _DlswTConnOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('connecting',1),('initCapExchange',2),(_b,3),('quiescing',4),('disconnecting',5),(_c,6)))
_DlswTConnOperState_Type.__name__=_C
_DlswTConnOperState_Object=MibTableColumn
dlswTConnOperState=_DlswTConnOperState_Object((1,3,6,1,4,1,43,2,24,2,3,1,6),_DlswTConnOperState_Type())
dlswTConnOperState.setMaxAccess(_E)
if mibBuilder.loadTexts:dlswTConnOperState.setStatus(_A)
_DlswTConnOperConfigIndex_Type=Integer32
_DlswTConnOperConfigIndex_Object=MibTableColumn
dlswTConnOperConfigIndex=_DlswTConnOperConfigIndex_Object((1,3,6,1,4,1,43,2,24,2,3,1,7),_DlswTConnOperConfigIndex_Type())
dlswTConnOperConfigIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswTConnOperConfigIndex.setStatus(_A)
class _DlswTConnOperFlowCntlMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('undetermined',1),('pacing',2),(_G,3)))
_DlswTConnOperFlowCntlMode_Type.__name__=_C
_DlswTConnOperFlowCntlMode_Object=MibTableColumn
dlswTConnOperFlowCntlMode=_DlswTConnOperFlowCntlMode_Object((1,3,6,1,4,1,43,2,24,2,3,1,8),_DlswTConnOperFlowCntlMode_Type())
dlswTConnOperFlowCntlMode.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswTConnOperFlowCntlMode.setStatus(_A)
class _DlswTConnOperPartnerVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2))
_DlswTConnOperPartnerVersion_Type.__name__=_F
_DlswTConnOperPartnerVersion_Object=MibTableColumn
dlswTConnOperPartnerVersion=_DlswTConnOperPartnerVersion_Object((1,3,6,1,4,1,43,2,24,2,3,1,9),_DlswTConnOperPartnerVersion_Type())
dlswTConnOperPartnerVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswTConnOperPartnerVersion.setStatus(_A)
class _DlswTConnOperPartnerVendorID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,3))
_DlswTConnOperPartnerVendorID_Type.__name__=_F
_DlswTConnOperPartnerVendorID_Object=MibTableColumn
dlswTConnOperPartnerVendorID=_DlswTConnOperPartnerVendorID_Object((1,3,6,1,4,1,43,2,24,2,3,1,10),_DlswTConnOperPartnerVendorID_Type())
dlswTConnOperPartnerVendorID.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswTConnOperPartnerVendorID.setStatus(_A)
class _DlswTConnOperPartnerVersionStr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,253))
_DlswTConnOperPartnerVersionStr_Type.__name__=_O
_DlswTConnOperPartnerVersionStr_Object=MibTableColumn
dlswTConnOperPartnerVersionStr=_DlswTConnOperPartnerVersionStr_Object((1,3,6,1,4,1,43,2,24,2,3,1,11),_DlswTConnOperPartnerVersionStr_Type())
dlswTConnOperPartnerVersionStr.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswTConnOperPartnerVersionStr.setStatus(_A)
class _DlswTConnOperPartnerInitPacingWndw_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DlswTConnOperPartnerInitPacingWndw_Type.__name__=_C
_DlswTConnOperPartnerInitPacingWndw_Object=MibTableColumn
dlswTConnOperPartnerInitPacingWndw=_DlswTConnOperPartnerInitPacingWndw_Object((1,3,6,1,4,1,43,2,24,2,3,1,12),_DlswTConnOperPartnerInitPacingWndw_Type())
dlswTConnOperPartnerInitPacingWndw.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswTConnOperPartnerInitPacingWndw.setStatus(_A)
class _DlswTConnOperPartnerSapList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_DlswTConnOperPartnerSapList_Type.__name__=_F
_DlswTConnOperPartnerSapList_Object=MibTableColumn
dlswTConnOperPartnerSapList=_DlswTConnOperPartnerSapList_Object((1,3,6,1,4,1,43,2,24,2,3,1,13),_DlswTConnOperPartnerSapList_Type())
dlswTConnOperPartnerSapList.setMaxAccess(_E)
if mibBuilder.loadTexts:dlswTConnOperPartnerSapList.setStatus(_A)
_DlswTConnOperPartnerNBExcl_Type=Truthvalue
_DlswTConnOperPartnerNBExcl_Object=MibTableColumn
dlswTConnOperPartnerNBExcl=_DlswTConnOperPartnerNBExcl_Object((1,3,6,1,4,1,43,2,24,2,3,1,14),_DlswTConnOperPartnerNBExcl_Type())
dlswTConnOperPartnerNBExcl.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswTConnOperPartnerNBExcl.setStatus(_A)
_DlswTConnOperPartnerMacExcl_Type=Truthvalue
_DlswTConnOperPartnerMacExcl_Object=MibTableColumn
dlswTConnOperPartnerMacExcl=_DlswTConnOperPartnerMacExcl_Object((1,3,6,1,4,1,43,2,24,2,3,1,15),_DlswTConnOperPartnerMacExcl_Type())
dlswTConnOperPartnerMacExcl.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswTConnOperPartnerMacExcl.setStatus(_A)
class _DlswTConnOperPartnerNBInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_R,1),(_d,2),(_e,3),(_f,4)))
_DlswTConnOperPartnerNBInfo_Type.__name__=_C
_DlswTConnOperPartnerNBInfo_Object=MibTableColumn
dlswTConnOperPartnerNBInfo=_DlswTConnOperPartnerNBInfo_Object((1,3,6,1,4,1,43,2,24,2,3,1,16),_DlswTConnOperPartnerNBInfo_Type())
dlswTConnOperPartnerNBInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswTConnOperPartnerNBInfo.setStatus(_A)
class _DlswTConnOperPartnerMacInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_R,1),(_d,2),(_e,3),(_f,4)))
_DlswTConnOperPartnerMacInfo_Type.__name__=_C
_DlswTConnOperPartnerMacInfo_Object=MibTableColumn
dlswTConnOperPartnerMacInfo=_DlswTConnOperPartnerMacInfo_Object((1,3,6,1,4,1,43,2,24,2,3,1,17),_DlswTConnOperPartnerMacInfo_Type())
dlswTConnOperPartnerMacInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswTConnOperPartnerMacInfo.setStatus(_A)
_DlswTConnOperDiscTime_Type=DlswTimeStamp
_DlswTConnOperDiscTime_Object=MibTableColumn
dlswTConnOperDiscTime=_DlswTConnOperDiscTime_Object((1,3,6,1,4,1,43,2,24,2,3,1,18),_DlswTConnOperDiscTime_Type())
dlswTConnOperDiscTime.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswTConnOperDiscTime.setStatus(_A)
class _DlswTConnOperDiscReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_G,1),('capExFailed',2),('transportLayerDisc',3),(_S,4),('lastCircuitDiscd',5),(_T,6)))
_DlswTConnOperDiscReason_Type.__name__=_C
_DlswTConnOperDiscReason_Object=MibTableColumn
dlswTConnOperDiscReason=_DlswTConnOperDiscReason_Object((1,3,6,1,4,1,43,2,24,2,3,1,19),_DlswTConnOperDiscReason_Type())
dlswTConnOperDiscReason.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswTConnOperDiscReason.setStatus(_A)
_DlswTConnOperDiscActiveCir_Type=Integer32
_DlswTConnOperDiscActiveCir_Object=MibTableColumn
dlswTConnOperDiscActiveCir=_DlswTConnOperDiscActiveCir_Object((1,3,6,1,4,1,43,2,24,2,3,1,20),_DlswTConnOperDiscActiveCir_Type())
dlswTConnOperDiscActiveCir.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswTConnOperDiscActiveCir.setStatus(_A)
_DlswTConnOperInDataPkts_Type=Counter32
_DlswTConnOperInDataPkts_Object=MibTableColumn
dlswTConnOperInDataPkts=_DlswTConnOperInDataPkts_Object((1,3,6,1,4,1,43,2,24,2,3,1,21),_DlswTConnOperInDataPkts_Type())
dlswTConnOperInDataPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswTConnOperInDataPkts.setStatus(_A)
_DlswTConnOperOutDataPkts_Type=Counter32
_DlswTConnOperOutDataPkts_Object=MibTableColumn
dlswTConnOperOutDataPkts=_DlswTConnOperOutDataPkts_Object((1,3,6,1,4,1,43,2,24,2,3,1,22),_DlswTConnOperOutDataPkts_Type())
dlswTConnOperOutDataPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswTConnOperOutDataPkts.setStatus(_A)
_DlswTConnOperInDataOctets_Type=Counter32
_DlswTConnOperInDataOctets_Object=MibTableColumn
dlswTConnOperInDataOctets=_DlswTConnOperInDataOctets_Object((1,3,6,1,4,1,43,2,24,2,3,1,23),_DlswTConnOperInDataOctets_Type())
dlswTConnOperInDataOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswTConnOperInDataOctets.setStatus(_A)
_DlswTConnOperOutDataOctets_Type=Counter32
_DlswTConnOperOutDataOctets_Object=MibTableColumn
dlswTConnOperOutDataOctets=_DlswTConnOperOutDataOctets_Object((1,3,6,1,4,1,43,2,24,2,3,1,24),_DlswTConnOperOutDataOctets_Type())
dlswTConnOperOutDataOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswTConnOperOutDataOctets.setStatus(_A)
_DlswTConnOperInCntlPkts_Type=Counter32
_DlswTConnOperInCntlPkts_Object=MibTableColumn
dlswTConnOperInCntlPkts=_DlswTConnOperInCntlPkts_Object((1,3,6,1,4,1,43,2,24,2,3,1,25),_DlswTConnOperInCntlPkts_Type())
dlswTConnOperInCntlPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswTConnOperInCntlPkts.setStatus(_A)
_DlswTConnOperOutCntlPkts_Type=Counter32
_DlswTConnOperOutCntlPkts_Object=MibTableColumn
dlswTConnOperOutCntlPkts=_DlswTConnOperOutCntlPkts_Object((1,3,6,1,4,1,43,2,24,2,3,1,26),_DlswTConnOperOutCntlPkts_Type())
dlswTConnOperOutCntlPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswTConnOperOutCntlPkts.setStatus(_A)
_DlswTConnOperCURexSents_Type=Counter32
_DlswTConnOperCURexSents_Object=MibTableColumn
dlswTConnOperCURexSents=_DlswTConnOperCURexSents_Object((1,3,6,1,4,1,43,2,24,2,3,1,27),_DlswTConnOperCURexSents_Type())
dlswTConnOperCURexSents.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswTConnOperCURexSents.setStatus(_A)
_DlswTConnOperICRexRcvds_Type=Counter32
_DlswTConnOperICRexRcvds_Object=MibTableColumn
dlswTConnOperICRexRcvds=_DlswTConnOperICRexRcvds_Object((1,3,6,1,4,1,43,2,24,2,3,1,28),_DlswTConnOperICRexRcvds_Type())
dlswTConnOperICRexRcvds.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswTConnOperICRexRcvds.setStatus(_A)
_DlswTConnOperCURexRcvds_Type=Counter32
_DlswTConnOperCURexRcvds_Object=MibTableColumn
dlswTConnOperCURexRcvds=_DlswTConnOperCURexRcvds_Object((1,3,6,1,4,1,43,2,24,2,3,1,29),_DlswTConnOperCURexRcvds_Type())
dlswTConnOperCURexRcvds.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswTConnOperCURexRcvds.setStatus(_A)
_DlswTConnOperICRexSents_Type=Counter32
_DlswTConnOperICRexSents_Object=MibTableColumn
dlswTConnOperICRexSents=_DlswTConnOperICRexSents_Object((1,3,6,1,4,1,43,2,24,2,3,1,30),_DlswTConnOperICRexSents_Type())
dlswTConnOperICRexSents.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswTConnOperICRexSents.setStatus(_A)
_DlswTConnOperNQexSents_Type=Counter32
_DlswTConnOperNQexSents_Object=MibTableColumn
dlswTConnOperNQexSents=_DlswTConnOperNQexSents_Object((1,3,6,1,4,1,43,2,24,2,3,1,31),_DlswTConnOperNQexSents_Type())
dlswTConnOperNQexSents.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswTConnOperNQexSents.setStatus(_A)
_DlswTConnOperNRexRcvds_Type=Counter32
_DlswTConnOperNRexRcvds_Object=MibTableColumn
dlswTConnOperNRexRcvds=_DlswTConnOperNRexRcvds_Object((1,3,6,1,4,1,43,2,24,2,3,1,32),_DlswTConnOperNRexRcvds_Type())
dlswTConnOperNRexRcvds.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswTConnOperNRexRcvds.setStatus(_A)
_DlswTConnOperNQexRcvds_Type=Counter32
_DlswTConnOperNQexRcvds_Object=MibTableColumn
dlswTConnOperNQexRcvds=_DlswTConnOperNQexRcvds_Object((1,3,6,1,4,1,43,2,24,2,3,1,33),_DlswTConnOperNQexRcvds_Type())
dlswTConnOperNQexRcvds.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswTConnOperNQexRcvds.setStatus(_A)
_DlswTConnOperNRexSents_Type=Counter32
_DlswTConnOperNRexSents_Object=MibTableColumn
dlswTConnOperNRexSents=_DlswTConnOperNRexSents_Object((1,3,6,1,4,1,43,2,24,2,3,1,34),_DlswTConnOperNRexSents_Type())
dlswTConnOperNRexSents.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswTConnOperNRexSents.setStatus(_A)
_DlswTConnOperCirCreates_Type=Counter32
_DlswTConnOperCirCreates_Object=MibTableColumn
dlswTConnOperCirCreates=_DlswTConnOperCirCreates_Object((1,3,6,1,4,1,43,2,24,2,3,1,35),_DlswTConnOperCirCreates_Type())
dlswTConnOperCirCreates.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswTConnOperCirCreates.setStatus(_A)
_DlswTConnOperCircuits_Type=Gauge32
_DlswTConnOperCircuits_Object=MibTableColumn
dlswTConnOperCircuits=_DlswTConnOperCircuits_Object((1,3,6,1,4,1,43,2,24,2,3,1,36),_DlswTConnOperCircuits_Type())
dlswTConnOperCircuits.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswTConnOperCircuits.setStatus(_A)
_DlswInterface_ObjectIdentity=ObjectIdentity
dlswInterface=_DlswInterface_ObjectIdentity((1,3,6,1,4,1,43,2,24,3))
_DlswDirectory_ObjectIdentity=ObjectIdentity
dlswDirectory=_DlswDirectory_ObjectIdentity((1,3,6,1,4,1,43,2,24,4))
_DlswDirStat_ObjectIdentity=ObjectIdentity
dlswDirStat=_DlswDirStat_ObjectIdentity((1,3,6,1,4,1,43,2,24,4,1))
_DlswDirMacEntries_Type=Gauge32
_DlswDirMacEntries_Object=MibScalar
dlswDirMacEntries=_DlswDirMacEntries_Object((1,3,6,1,4,1,43,2,24,4,1,1),_DlswDirMacEntries_Type())
dlswDirMacEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswDirMacEntries.setStatus(_A)
_DlswDirNBEntries_Type=Gauge32
_DlswDirNBEntries_Object=MibScalar
dlswDirNBEntries=_DlswDirNBEntries_Object((1,3,6,1,4,1,43,2,24,4,1,4),_DlswDirNBEntries_Type())
dlswDirNBEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswDirNBEntries.setStatus(_A)
_DlswDirCache_ObjectIdentity=ObjectIdentity
dlswDirCache=_DlswDirCache_ObjectIdentity((1,3,6,1,4,1,43,2,24,4,2))
_DlswDirMacTable_Object=MibTable
dlswDirMacTable=_DlswDirMacTable_Object((1,3,6,1,4,1,43,2,24,4,2,1))
if mibBuilder.loadTexts:dlswDirMacTable.setStatus(_A)
_DlswDirMacEntry_Object=MibTableRow
dlswDirMacEntry=_DlswDirMacEntry_Object((1,3,6,1,4,1,43,2,24,4,2,1,1))
dlswDirMacEntry.setIndexNames((0,_D,_g))
if mibBuilder.loadTexts:dlswDirMacEntry.setStatus(_A)
_DlswDirMacIndex_Type=Integer32
_DlswDirMacIndex_Object=MibTableColumn
dlswDirMacIndex=_DlswDirMacIndex_Object((1,3,6,1,4,1,43,2,24,4,2,1,1,1),_DlswDirMacIndex_Type())
dlswDirMacIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswDirMacIndex.setStatus(_A)
_DlswDirMacMac_Type=MacAddress
_DlswDirMacMac_Object=MibTableColumn
dlswDirMacMac=_DlswDirMacMac_Object((1,3,6,1,4,1,43,2,24,4,2,1,1,2),_DlswDirMacMac_Type())
dlswDirMacMac.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswDirMacMac.setStatus(_A)
class _DlswDirMacMask_Type(MacAddress):defaultHexValue='FFFFFFFFFFFF'
_DlswDirMacMask_Type.__name__=_h
_DlswDirMacMask_Object=MibTableColumn
dlswDirMacMask=_DlswDirMacMask_Object((1,3,6,1,4,1,43,2,24,4,2,1,1,3),_DlswDirMacMask_Type())
dlswDirMacMask.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswDirMacMask.setStatus(_A)
class _DlswDirMacEntryType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_G,1),(_i,2),(_j,3),(_k,4),(_l,5)))
_DlswDirMacEntryType_Type.__name__=_C
_DlswDirMacEntryType_Object=MibTableColumn
dlswDirMacEntryType=_DlswDirMacEntryType_Object((1,3,6,1,4,1,43,2,24,4,2,1,1,4),_DlswDirMacEntryType_Type())
dlswDirMacEntryType.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswDirMacEntryType.setStatus(_A)
class _DlswDirMacLocationType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_Q,2),(_P,3)))
_DlswDirMacLocationType_Type.__name__=_C
_DlswDirMacLocationType_Object=MibTableColumn
dlswDirMacLocationType=_DlswDirMacLocationType_Object((1,3,6,1,4,1,43,2,24,4,2,1,1,5),_DlswDirMacLocationType_Type())
dlswDirMacLocationType.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswDirMacLocationType.setStatus(_A)
_DlswDirMacLocation_Type=Instancepointer
_DlswDirMacLocation_Object=MibTableColumn
dlswDirMacLocation=_DlswDirMacLocation_Object((1,3,6,1,4,1,43,2,24,4,2,1,1,6),_DlswDirMacLocation_Type())
dlswDirMacLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswDirMacLocation.setStatus(_A)
class _DlswDirMacStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_m,2),(_n,3)))
_DlswDirMacStatus_Type.__name__=_C
_DlswDirMacStatus_Object=MibTableColumn
dlswDirMacStatus=_DlswDirMacStatus_Object((1,3,6,1,4,1,43,2,24,4,2,1,1,7),_DlswDirMacStatus_Type())
dlswDirMacStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswDirMacStatus.setStatus(_A)
_DlswDirMacLFSize_Type=LFSize
_DlswDirMacLFSize_Object=MibTableColumn
dlswDirMacLFSize=_DlswDirMacLFSize_Object((1,3,6,1,4,1,43,2,24,4,2,1,1,8),_DlswDirMacLFSize_Type())
dlswDirMacLFSize.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswDirMacLFSize.setStatus(_A)
_DlswDirMacRowStatus_Type=RowStatus
_DlswDirMacRowStatus_Object=MibTableColumn
dlswDirMacRowStatus=_DlswDirMacRowStatus_Object((1,3,6,1,4,1,43,2,24,4,2,1,1,9),_DlswDirMacRowStatus_Type())
dlswDirMacRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswDirMacRowStatus.setStatus(_A)
_DlswDirNBTable_Object=MibTable
dlswDirNBTable=_DlswDirNBTable_Object((1,3,6,1,4,1,43,2,24,4,2,2))
if mibBuilder.loadTexts:dlswDirNBTable.setStatus(_A)
_DlswDirNBEntry_Object=MibTableRow
dlswDirNBEntry=_DlswDirNBEntry_Object((1,3,6,1,4,1,43,2,24,4,2,2,1))
dlswDirNBEntry.setIndexNames((0,_D,_o))
if mibBuilder.loadTexts:dlswDirNBEntry.setStatus(_A)
_DlswDirNBIndex_Type=Integer32
_DlswDirNBIndex_Object=MibTableColumn
dlswDirNBIndex=_DlswDirNBIndex_Object((1,3,6,1,4,1,43,2,24,4,2,2,1,1),_DlswDirNBIndex_Type())
dlswDirNBIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswDirNBIndex.setStatus(_A)
_DlswDirNBName_Type=NBName
_DlswDirNBName_Object=MibTableColumn
dlswDirNBName=_DlswDirNBName_Object((1,3,6,1,4,1,43,2,24,4,2,2,1,2),_DlswDirNBName_Type())
dlswDirNBName.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswDirNBName.setStatus(_A)
class _DlswDirNBNameType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_Z,2),('group',3)))
_DlswDirNBNameType_Type.__name__=_C
_DlswDirNBNameType_Object=MibTableColumn
dlswDirNBNameType=_DlswDirNBNameType_Object((1,3,6,1,4,1,43,2,24,4,2,2,1,3),_DlswDirNBNameType_Type())
dlswDirNBNameType.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswDirNBNameType.setStatus(_A)
class _DlswDirNBEntryType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_G,1),(_i,2),(_j,3),(_k,4),(_l,5)))
_DlswDirNBEntryType_Type.__name__=_C
_DlswDirNBEntryType_Object=MibTableColumn
dlswDirNBEntryType=_DlswDirNBEntryType_Object((1,3,6,1,4,1,43,2,24,4,2,2,1,4),_DlswDirNBEntryType_Type())
dlswDirNBEntryType.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswDirNBEntryType.setStatus(_A)
class _DlswDirNBLocationType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_Q,2),(_P,3)))
_DlswDirNBLocationType_Type.__name__=_C
_DlswDirNBLocationType_Object=MibTableColumn
dlswDirNBLocationType=_DlswDirNBLocationType_Object((1,3,6,1,4,1,43,2,24,4,2,2,1,5),_DlswDirNBLocationType_Type())
dlswDirNBLocationType.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswDirNBLocationType.setStatus(_A)
_DlswDirNBLocation_Type=Instancepointer
_DlswDirNBLocation_Object=MibTableColumn
dlswDirNBLocation=_DlswDirNBLocation_Object((1,3,6,1,4,1,43,2,24,4,2,2,1,6),_DlswDirNBLocation_Type())
dlswDirNBLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswDirNBLocation.setStatus(_A)
class _DlswDirNBStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_m,2),(_n,3)))
_DlswDirNBStatus_Type.__name__=_C
_DlswDirNBStatus_Object=MibTableColumn
dlswDirNBStatus=_DlswDirNBStatus_Object((1,3,6,1,4,1,43,2,24,4,2,2,1,7),_DlswDirNBStatus_Type())
dlswDirNBStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswDirNBStatus.setStatus(_A)
_DlswDirNBLFSize_Type=LFSize
_DlswDirNBLFSize_Object=MibTableColumn
dlswDirNBLFSize=_DlswDirNBLFSize_Object((1,3,6,1,4,1,43,2,24,4,2,2,1,8),_DlswDirNBLFSize_Type())
dlswDirNBLFSize.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswDirNBLFSize.setStatus(_A)
_DlswDirNBRowStatus_Type=RowStatus
_DlswDirNBRowStatus_Object=MibTableColumn
dlswDirNBRowStatus=_DlswDirNBRowStatus_Object((1,3,6,1,4,1,43,2,24,4,2,2,1,9),_DlswDirNBRowStatus_Type())
dlswDirNBRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswDirNBRowStatus.setStatus(_A)
_DlswCircuit_ObjectIdentity=ObjectIdentity
dlswCircuit=_DlswCircuit_ObjectIdentity((1,3,6,1,4,1,43,2,24,5))
_DlswCircuitStat_ObjectIdentity=ObjectIdentity
dlswCircuitStat=_DlswCircuitStat_ObjectIdentity((1,3,6,1,4,1,43,2,24,5,1))
_DlswActiveCircuits_Type=Gauge32
_DlswActiveCircuits_Object=MibScalar
dlswActiveCircuits=_DlswActiveCircuits_Object((1,3,6,1,4,1,43,2,24,5,1,1),_DlswActiveCircuits_Type())
dlswActiveCircuits.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswActiveCircuits.setStatus(_A)
_DlswCircuitCreates_Type=Counter32
_DlswCircuitCreates_Object=MibScalar
dlswCircuitCreates=_DlswCircuitCreates_Object((1,3,6,1,4,1,43,2,24,5,1,2),_DlswCircuitCreates_Type())
dlswCircuitCreates.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswCircuitCreates.setStatus(_A)
_DlswCircuitTable_Object=MibTable
dlswCircuitTable=_DlswCircuitTable_Object((1,3,6,1,4,1,43,2,24,5,2))
if mibBuilder.loadTexts:dlswCircuitTable.setStatus(_A)
_DlswCircuitEntry_Object=MibTableRow
dlswCircuitEntry=_DlswCircuitEntry_Object((1,3,6,1,4,1,43,2,24,5,2,1))
dlswCircuitEntry.setIndexNames((0,_D,_K),(0,_D,_L),(0,_D,_M),(0,_D,_N))
if mibBuilder.loadTexts:dlswCircuitEntry.setStatus(_A)
_DlswCircuitS1Mac_Type=MacAddress
_DlswCircuitS1Mac_Object=MibTableColumn
dlswCircuitS1Mac=_DlswCircuitS1Mac_Object((1,3,6,1,4,1,43,2,24,5,2,1,1),_DlswCircuitS1Mac_Type())
dlswCircuitS1Mac.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswCircuitS1Mac.setStatus(_A)
class _DlswCircuitS1Sap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_DlswCircuitS1Sap_Type.__name__=_F
_DlswCircuitS1Sap_Object=MibTableColumn
dlswCircuitS1Sap=_DlswCircuitS1Sap_Object((1,3,6,1,4,1,43,2,24,5,2,1,2),_DlswCircuitS1Sap_Type())
dlswCircuitS1Sap.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswCircuitS1Sap.setStatus(_A)
_DlswCircuitS1IfIndex_Type=Integer32
_DlswCircuitS1IfIndex_Object=MibTableColumn
dlswCircuitS1IfIndex=_DlswCircuitS1IfIndex_Object((1,3,6,1,4,1,43,2,24,5,2,1,3),_DlswCircuitS1IfIndex_Type())
dlswCircuitS1IfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswCircuitS1IfIndex.setStatus(_A)
_DlswCircuitS1DlcType_Type=DlcType
_DlswCircuitS1DlcType_Object=MibTableColumn
dlswCircuitS1DlcType=_DlswCircuitS1DlcType_Object((1,3,6,1,4,1,43,2,24,5,2,1,4),_DlswCircuitS1DlcType_Type())
dlswCircuitS1DlcType.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswCircuitS1DlcType.setStatus(_A)
class _DlswCircuitS1RouteInfo_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DlswCircuitS1RouteInfo_Type.__name__=_F
_DlswCircuitS1RouteInfo_Object=MibTableColumn
dlswCircuitS1RouteInfo=_DlswCircuitS1RouteInfo_Object((1,3,6,1,4,1,43,2,24,5,2,1,5),_DlswCircuitS1RouteInfo_Type())
dlswCircuitS1RouteInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswCircuitS1RouteInfo.setStatus(_A)
class _DlswCircuitS1CircuitId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_DlswCircuitS1CircuitId_Type.__name__=_F
_DlswCircuitS1CircuitId_Object=MibTableColumn
dlswCircuitS1CircuitId=_DlswCircuitS1CircuitId_Object((1,3,6,1,4,1,43,2,24,5,2,1,6),_DlswCircuitS1CircuitId_Type())
dlswCircuitS1CircuitId.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswCircuitS1CircuitId.setStatus(_A)
_DlswCircuitS1Dlc_Type=Instancepointer
_DlswCircuitS1Dlc_Object=MibTableColumn
dlswCircuitS1Dlc=_DlswCircuitS1Dlc_Object((1,3,6,1,4,1,43,2,24,5,2,1,7),_DlswCircuitS1Dlc_Type())
dlswCircuitS1Dlc.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswCircuitS1Dlc.setStatus(_A)
_DlswCircuitS2Mac_Type=MacAddress
_DlswCircuitS2Mac_Object=MibTableColumn
dlswCircuitS2Mac=_DlswCircuitS2Mac_Object((1,3,6,1,4,1,43,2,24,5,2,1,8),_DlswCircuitS2Mac_Type())
dlswCircuitS2Mac.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswCircuitS2Mac.setStatus(_A)
class _DlswCircuitS2Sap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_DlswCircuitS2Sap_Type.__name__=_F
_DlswCircuitS2Sap_Object=MibTableColumn
dlswCircuitS2Sap=_DlswCircuitS2Sap_Object((1,3,6,1,4,1,43,2,24,5,2,1,9),_DlswCircuitS2Sap_Type())
dlswCircuitS2Sap.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswCircuitS2Sap.setStatus(_A)
_DlswCircuitS2Location_Type=EndStationLocation
_DlswCircuitS2Location_Object=MibTableColumn
dlswCircuitS2Location=_DlswCircuitS2Location_Object((1,3,6,1,4,1,43,2,24,5,2,1,10),_DlswCircuitS2Location_Type())
dlswCircuitS2Location.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswCircuitS2Location.setStatus(_A)
_DlswCircuitS2TDomain_Type=ObjectIdentifier
_DlswCircuitS2TDomain_Object=MibTableColumn
dlswCircuitS2TDomain=_DlswCircuitS2TDomain_Object((1,3,6,1,4,1,43,2,24,5,2,1,11),_DlswCircuitS2TDomain_Type())
dlswCircuitS2TDomain.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswCircuitS2TDomain.setStatus(_A)
_DlswCircuitS2TAddress_Type=TAddress
_DlswCircuitS2TAddress_Object=MibTableColumn
dlswCircuitS2TAddress=_DlswCircuitS2TAddress_Object((1,3,6,1,4,1,43,2,24,5,2,1,12),_DlswCircuitS2TAddress_Type())
dlswCircuitS2TAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswCircuitS2TAddress.setStatus(_A)
class _DlswCircuitS2CircuitId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_DlswCircuitS2CircuitId_Type.__name__=_F
_DlswCircuitS2CircuitId_Object=MibTableColumn
dlswCircuitS2CircuitId=_DlswCircuitS2CircuitId_Object((1,3,6,1,4,1,43,2,24,5,2,1,13),_DlswCircuitS2CircuitId_Type())
dlswCircuitS2CircuitId.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswCircuitS2CircuitId.setStatus(_A)
class _DlswCircuitOrigin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('s1',1),('s2',2)))
_DlswCircuitOrigin_Type.__name__=_C
_DlswCircuitOrigin_Object=MibTableColumn
dlswCircuitOrigin=_DlswCircuitOrigin_Object((1,3,6,1,4,1,43,2,24,5,2,1,14),_DlswCircuitOrigin_Type())
dlswCircuitOrigin.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswCircuitOrigin.setStatus(_A)
_DlswCircuitEntryTime_Type=DlswTimeStamp
_DlswCircuitEntryTime_Object=MibTableColumn
dlswCircuitEntryTime=_DlswCircuitEntryTime_Object((1,3,6,1,4,1,43,2,24,5,2,1,15),_DlswCircuitEntryTime_Type())
dlswCircuitEntryTime.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswCircuitEntryTime.setStatus(_A)
_DlswCircuitStateTime_Type=DlswTimeStamp
_DlswCircuitStateTime_Object=MibTableColumn
dlswCircuitStateTime=_DlswCircuitStateTime_Object((1,3,6,1,4,1,43,2,24,5,2,1,16),_DlswCircuitStateTime_Type())
dlswCircuitStateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswCircuitStateTime.setStatus(_A)
class _DlswCircuitState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*((_c,1),('circuitStart',2),('resolvePending',3),('circuitPending',4),('circuitEstablished',5),('connectPending',6),('contactPending',7),(_b,8),('disconnectPending',9),('haltPending',10),('haltPendingNoack',11),('circuitRestart',12),('restartPending',13)))
_DlswCircuitState_Type.__name__=_C
_DlswCircuitState_Object=MibTableColumn
dlswCircuitState=_DlswCircuitState_Object((1,3,6,1,4,1,43,2,24,5,2,1,17),_DlswCircuitState_Type())
dlswCircuitState.setMaxAccess(_E)
if mibBuilder.loadTexts:dlswCircuitState.setStatus(_A)
class _DlswCircuitPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('unsupported',0),('low',1),('medium',2),('high',3),('highest',4)))
_DlswCircuitPriority_Type.__name__=_C
_DlswCircuitPriority_Object=MibTableColumn
dlswCircuitPriority=_DlswCircuitPriority_Object((1,3,6,1,4,1,43,2,24,5,2,1,18),_DlswCircuitPriority_Type())
dlswCircuitPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswCircuitPriority.setStatus(_A)
class _DlswCircuitFCSendGrantedUnits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DlswCircuitFCSendGrantedUnits_Type.__name__=_C
_DlswCircuitFCSendGrantedUnits_Object=MibTableColumn
dlswCircuitFCSendGrantedUnits=_DlswCircuitFCSendGrantedUnits_Object((1,3,6,1,4,1,43,2,24,5,2,1,19),_DlswCircuitFCSendGrantedUnits_Type())
dlswCircuitFCSendGrantedUnits.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswCircuitFCSendGrantedUnits.setStatus(_A)
class _DlswCircuitFCSendCurrentWndw_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DlswCircuitFCSendCurrentWndw_Type.__name__=_C
_DlswCircuitFCSendCurrentWndw_Object=MibTableColumn
dlswCircuitFCSendCurrentWndw=_DlswCircuitFCSendCurrentWndw_Object((1,3,6,1,4,1,43,2,24,5,2,1,20),_DlswCircuitFCSendCurrentWndw_Type())
dlswCircuitFCSendCurrentWndw.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswCircuitFCSendCurrentWndw.setStatus(_A)
class _DlswCircuitFCRecvGrantedUnits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DlswCircuitFCRecvGrantedUnits_Type.__name__=_C
_DlswCircuitFCRecvGrantedUnits_Object=MibTableColumn
dlswCircuitFCRecvGrantedUnits=_DlswCircuitFCRecvGrantedUnits_Object((1,3,6,1,4,1,43,2,24,5,2,1,21),_DlswCircuitFCRecvGrantedUnits_Type())
dlswCircuitFCRecvGrantedUnits.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswCircuitFCRecvGrantedUnits.setStatus(_A)
class _DlswCircuitFCRecvCurrentWndw_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DlswCircuitFCRecvCurrentWndw_Type.__name__=_C
_DlswCircuitFCRecvCurrentWndw_Object=MibTableColumn
dlswCircuitFCRecvCurrentWndw=_DlswCircuitFCRecvCurrentWndw_Object((1,3,6,1,4,1,43,2,24,5,2,1,22),_DlswCircuitFCRecvCurrentWndw_Type())
dlswCircuitFCRecvCurrentWndw.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswCircuitFCRecvCurrentWndw.setStatus(_A)
_DlswCircuitFCLargestRecvGranted_Type=Gauge32
_DlswCircuitFCLargestRecvGranted_Object=MibTableColumn
dlswCircuitFCLargestRecvGranted=_DlswCircuitFCLargestRecvGranted_Object((1,3,6,1,4,1,43,2,24,5,2,1,23),_DlswCircuitFCLargestRecvGranted_Type())
dlswCircuitFCLargestRecvGranted.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswCircuitFCLargestRecvGranted.setStatus(_A)
_DlswCircuitFCLargestSendGranted_Type=Gauge32
_DlswCircuitFCLargestSendGranted_Object=MibTableColumn
dlswCircuitFCLargestSendGranted=_DlswCircuitFCLargestSendGranted_Object((1,3,6,1,4,1,43,2,24,5,2,1,24),_DlswCircuitFCLargestSendGranted_Type())
dlswCircuitFCLargestSendGranted.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswCircuitFCLargestSendGranted.setStatus(_A)
_DlswCircuitFCHalveWndwSents_Type=Counter32
_DlswCircuitFCHalveWndwSents_Object=MibTableColumn
dlswCircuitFCHalveWndwSents=_DlswCircuitFCHalveWndwSents_Object((1,3,6,1,4,1,43,2,24,5,2,1,25),_DlswCircuitFCHalveWndwSents_Type())
dlswCircuitFCHalveWndwSents.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswCircuitFCHalveWndwSents.setStatus(_A)
_DlswCircuitFCResetOpSents_Type=Counter32
_DlswCircuitFCResetOpSents_Object=MibTableColumn
dlswCircuitFCResetOpSents=_DlswCircuitFCResetOpSents_Object((1,3,6,1,4,1,43,2,24,5,2,1,26),_DlswCircuitFCResetOpSents_Type())
dlswCircuitFCResetOpSents.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswCircuitFCResetOpSents.setStatus(_A)
_DlswCircuitFCHalveWndwRcvds_Type=Counter32
_DlswCircuitFCHalveWndwRcvds_Object=MibTableColumn
dlswCircuitFCHalveWndwRcvds=_DlswCircuitFCHalveWndwRcvds_Object((1,3,6,1,4,1,43,2,24,5,2,1,27),_DlswCircuitFCHalveWndwRcvds_Type())
dlswCircuitFCHalveWndwRcvds.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswCircuitFCHalveWndwRcvds.setStatus(_A)
_DlswCircuitFCResetOpRcvds_Type=Counter32
_DlswCircuitFCResetOpRcvds_Object=MibTableColumn
dlswCircuitFCResetOpRcvds=_DlswCircuitFCResetOpRcvds_Object((1,3,6,1,4,1,43,2,24,5,2,1,28),_DlswCircuitFCResetOpRcvds_Type())
dlswCircuitFCResetOpRcvds.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswCircuitFCResetOpRcvds.setStatus(_A)
class _DlswCircuitDiscReasonLocal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_p,1),(_q,2),(_T,3),(_S,4),('haltDlRcvd',5),('haltDlNoAckRcvd',6),('transportConnClosed',7)))
_DlswCircuitDiscReasonLocal_Type.__name__=_C
_DlswCircuitDiscReasonLocal_Object=MibTableColumn
dlswCircuitDiscReasonLocal=_DlswCircuitDiscReasonLocal_Object((1,3,6,1,4,1,43,2,24,5,2,1,29),_DlswCircuitDiscReasonLocal_Type())
dlswCircuitDiscReasonLocal.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswCircuitDiscReasonLocal.setStatus(_A)
class _DlswCircuitDiscReasonRemote_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_J,0),(_p,1),(_q,2),(_T,3),(_S,4)))
_DlswCircuitDiscReasonRemote_Type.__name__=_C
_DlswCircuitDiscReasonRemote_Object=MibTableColumn
dlswCircuitDiscReasonRemote=_DlswCircuitDiscReasonRemote_Object((1,3,6,1,4,1,43,2,24,5,2,1,30),_DlswCircuitDiscReasonRemote_Type())
dlswCircuitDiscReasonRemote.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswCircuitDiscReasonRemote.setStatus(_A)
class _DlswCircuitDiscReasonRemoteData_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_DlswCircuitDiscReasonRemoteData_Type.__name__=_F
_DlswCircuitDiscReasonRemoteData_Object=MibTableColumn
dlswCircuitDiscReasonRemoteData=_DlswCircuitDiscReasonRemoteData_Object((1,3,6,1,4,1,43,2,24,5,2,1,31),_DlswCircuitDiscReasonRemoteData_Type())
dlswCircuitDiscReasonRemoteData.setMaxAccess(_B)
if mibBuilder.loadTexts:dlswCircuitDiscReasonRemoteData.setStatus(_A)
_DlswSdlc_ObjectIdentity=ObjectIdentity
dlswSdlc=_DlswSdlc_ObjectIdentity((1,3,6,1,4,1,43,2,24,6))
_DlswTraps_ObjectIdentity=ObjectIdentity
dlswTraps=_DlswTraps_ObjectIdentity((1,3,6,1,4,1,43,2,24,7))
dlswTrapTConnUp=NotificationType((1,3,6,1,4,1,43,2,24,0,1))
dlswTrapTConnUp.setObjects(*((_D,_H),(_D,_I)))
if mibBuilder.loadTexts:dlswTrapTConnUp.setStatus('')
dlswTrapTConnDown=NotificationType((1,3,6,1,4,1,43,2,24,0,2))
dlswTrapTConnDown.setObjects(*((_D,_H),(_D,_I)))
if mibBuilder.loadTexts:dlswTrapTConnDown.setStatus('')
dlswTrapCircuitUp=NotificationType((1,3,6,1,4,1,43,2,24,0,3))
dlswTrapCircuitUp.setObjects(*((_D,_K),(_D,_L),(_D,_M),(_D,_N)))
if mibBuilder.loadTexts:dlswTrapCircuitUp.setStatus('')
dlswTrapCircuitDown=NotificationType((1,3,6,1,4,1,43,2,24,0,4))
dlswTrapCircuitDown.setObjects(*((_D,_K),(_D,_L),(_D,_M),(_D,_N)))
if mibBuilder.loadTexts:dlswTrapCircuitDown.setStatus('')
mibBuilder.exportSymbols(_D,**{'NBName':NBName,_h:MacAddress,'TAddress':TAddress,'DlswTimeStamp':DlswTimeStamp,'EndStationLocation':EndStationLocation,'DlcType':DlcType,'LFSize':LFSize,_a:Truthvalue,'RowStatus':RowStatus,'Instancepointer':Instancepointer,'a3Com':a3Com,'brouterMIB':brouterMIB,'dlswMIB-3Com':dlswMIB_3Com,'dlswTrapTConnUp':dlswTrapTConnUp,'dlswTrapTConnDown':dlswTrapTConnDown,'dlswTrapCircuitUp':dlswTrapCircuitUp,'dlswTrapCircuitDown':dlswTrapCircuitDown,'dlswNode':dlswNode,'dlswVersion':dlswVersion,'dlswVendorID':dlswVendorID,'dlswVersionString':dlswVersionString,'dlswStdPacingSupport':dlswStdPacingSupport,'dlswStatus':dlswStatus,'dlswUpTime':dlswUpTime,'dlswVirtualSegmentLFSize':dlswVirtualSegmentLFSize,'dlswResourceNBExclusivity':dlswResourceNBExclusivity,'dlswResourceMacExclusivity':dlswResourceMacExclusivity,'dlswTrapControl':dlswTrapControl,'dlswTrapCntlTConn':dlswTrapCntlTConn,'dlswTrapCntlCircuit':dlswTrapCntlCircuit,'dlswTConn':dlswTConn,'dlswTConnStat':dlswTConnStat,'dlswTConnStatActiveConnections':dlswTConnStatActiveConnections,'dlswTConnStatCloseIdles':dlswTConnStatCloseIdles,'dlswTConnStatCloseBusys':dlswTConnStatCloseBusys,'dlswTConnConfigTable':dlswTConnConfigTable,'dlswTConnConfigEntry':dlswTConnConfigEntry,_Y:dlswTConnConfigIndex,'dlswTConnConfigTDomain':dlswTConnConfigTDomain,'dlswTConnConfigLocalTAddr':dlswTConnConfigLocalTAddr,'dlswTConnConfigRemoteTAddr':dlswTConnConfigRemoteTAddr,'dlswTConnConfigLastModifyTime':dlswTConnConfigLastModifyTime,'dlswTConnConfigEntryType':dlswTConnConfigEntryType,'dlswTConnConfigGroupDefinition':dlswTConnConfigGroupDefinition,'dlswTConnConfigSetupType':dlswTConnConfigSetupType,'dlswTConnConfigSapList':dlswTConnConfigSapList,'dlswTConnConfigAdvertiseMacNB':dlswTConnConfigAdvertiseMacNB,'dlswTConnConfigInitCirRecvWndw':dlswTConnConfigInitCirRecvWndw,'dlswTConnConfigOpens':dlswTConnConfigOpens,'dlswTConnConfigRowStatus':dlswTConnConfigRowStatus,'dlswTConnOperTable':dlswTConnOperTable,'dlswTConnOperEntry':dlswTConnOperEntry,_H:dlswTConnOperTDomain,'dlswTConnOperLocalTAddr':dlswTConnOperLocalTAddr,_I:dlswTConnOperRemoteTAddr,'dlswTConnOperEntryTime':dlswTConnOperEntryTime,'dlswTConnOperConnectTime':dlswTConnOperConnectTime,'dlswTConnOperState':dlswTConnOperState,'dlswTConnOperConfigIndex':dlswTConnOperConfigIndex,'dlswTConnOperFlowCntlMode':dlswTConnOperFlowCntlMode,'dlswTConnOperPartnerVersion':dlswTConnOperPartnerVersion,'dlswTConnOperPartnerVendorID':dlswTConnOperPartnerVendorID,'dlswTConnOperPartnerVersionStr':dlswTConnOperPartnerVersionStr,'dlswTConnOperPartnerInitPacingWndw':dlswTConnOperPartnerInitPacingWndw,'dlswTConnOperPartnerSapList':dlswTConnOperPartnerSapList,'dlswTConnOperPartnerNBExcl':dlswTConnOperPartnerNBExcl,'dlswTConnOperPartnerMacExcl':dlswTConnOperPartnerMacExcl,'dlswTConnOperPartnerNBInfo':dlswTConnOperPartnerNBInfo,'dlswTConnOperPartnerMacInfo':dlswTConnOperPartnerMacInfo,'dlswTConnOperDiscTime':dlswTConnOperDiscTime,'dlswTConnOperDiscReason':dlswTConnOperDiscReason,'dlswTConnOperDiscActiveCir':dlswTConnOperDiscActiveCir,'dlswTConnOperInDataPkts':dlswTConnOperInDataPkts,'dlswTConnOperOutDataPkts':dlswTConnOperOutDataPkts,'dlswTConnOperInDataOctets':dlswTConnOperInDataOctets,'dlswTConnOperOutDataOctets':dlswTConnOperOutDataOctets,'dlswTConnOperInCntlPkts':dlswTConnOperInCntlPkts,'dlswTConnOperOutCntlPkts':dlswTConnOperOutCntlPkts,'dlswTConnOperCURexSents':dlswTConnOperCURexSents,'dlswTConnOperICRexRcvds':dlswTConnOperICRexRcvds,'dlswTConnOperCURexRcvds':dlswTConnOperCURexRcvds,'dlswTConnOperICRexSents':dlswTConnOperICRexSents,'dlswTConnOperNQexSents':dlswTConnOperNQexSents,'dlswTConnOperNRexRcvds':dlswTConnOperNRexRcvds,'dlswTConnOperNQexRcvds':dlswTConnOperNQexRcvds,'dlswTConnOperNRexSents':dlswTConnOperNRexSents,'dlswTConnOperCirCreates':dlswTConnOperCirCreates,'dlswTConnOperCircuits':dlswTConnOperCircuits,'dlswInterface':dlswInterface,'dlswDirectory':dlswDirectory,'dlswDirStat':dlswDirStat,'dlswDirMacEntries':dlswDirMacEntries,'dlswDirNBEntries':dlswDirNBEntries,'dlswDirCache':dlswDirCache,'dlswDirMacTable':dlswDirMacTable,'dlswDirMacEntry':dlswDirMacEntry,_g:dlswDirMacIndex,'dlswDirMacMac':dlswDirMacMac,'dlswDirMacMask':dlswDirMacMask,'dlswDirMacEntryType':dlswDirMacEntryType,'dlswDirMacLocationType':dlswDirMacLocationType,'dlswDirMacLocation':dlswDirMacLocation,'dlswDirMacStatus':dlswDirMacStatus,'dlswDirMacLFSize':dlswDirMacLFSize,'dlswDirMacRowStatus':dlswDirMacRowStatus,'dlswDirNBTable':dlswDirNBTable,'dlswDirNBEntry':dlswDirNBEntry,_o:dlswDirNBIndex,'dlswDirNBName':dlswDirNBName,'dlswDirNBNameType':dlswDirNBNameType,'dlswDirNBEntryType':dlswDirNBEntryType,'dlswDirNBLocationType':dlswDirNBLocationType,'dlswDirNBLocation':dlswDirNBLocation,'dlswDirNBStatus':dlswDirNBStatus,'dlswDirNBLFSize':dlswDirNBLFSize,'dlswDirNBRowStatus':dlswDirNBRowStatus,'dlswCircuit':dlswCircuit,'dlswCircuitStat':dlswCircuitStat,'dlswActiveCircuits':dlswActiveCircuits,'dlswCircuitCreates':dlswCircuitCreates,'dlswCircuitTable':dlswCircuitTable,'dlswCircuitEntry':dlswCircuitEntry,_K:dlswCircuitS1Mac,_L:dlswCircuitS1Sap,'dlswCircuitS1IfIndex':dlswCircuitS1IfIndex,'dlswCircuitS1DlcType':dlswCircuitS1DlcType,'dlswCircuitS1RouteInfo':dlswCircuitS1RouteInfo,'dlswCircuitS1CircuitId':dlswCircuitS1CircuitId,'dlswCircuitS1Dlc':dlswCircuitS1Dlc,_M:dlswCircuitS2Mac,_N:dlswCircuitS2Sap,'dlswCircuitS2Location':dlswCircuitS2Location,'dlswCircuitS2TDomain':dlswCircuitS2TDomain,'dlswCircuitS2TAddress':dlswCircuitS2TAddress,'dlswCircuitS2CircuitId':dlswCircuitS2CircuitId,'dlswCircuitOrigin':dlswCircuitOrigin,'dlswCircuitEntryTime':dlswCircuitEntryTime,'dlswCircuitStateTime':dlswCircuitStateTime,'dlswCircuitState':dlswCircuitState,'dlswCircuitPriority':dlswCircuitPriority,'dlswCircuitFCSendGrantedUnits':dlswCircuitFCSendGrantedUnits,'dlswCircuitFCSendCurrentWndw':dlswCircuitFCSendCurrentWndw,'dlswCircuitFCRecvGrantedUnits':dlswCircuitFCRecvGrantedUnits,'dlswCircuitFCRecvCurrentWndw':dlswCircuitFCRecvCurrentWndw,'dlswCircuitFCLargestRecvGranted':dlswCircuitFCLargestRecvGranted,'dlswCircuitFCLargestSendGranted':dlswCircuitFCLargestSendGranted,'dlswCircuitFCHalveWndwSents':dlswCircuitFCHalveWndwSents,'dlswCircuitFCResetOpSents':dlswCircuitFCResetOpSents,'dlswCircuitFCHalveWndwRcvds':dlswCircuitFCHalveWndwRcvds,'dlswCircuitFCResetOpRcvds':dlswCircuitFCResetOpRcvds,'dlswCircuitDiscReasonLocal':dlswCircuitDiscReasonLocal,'dlswCircuitDiscReasonRemote':dlswCircuitDiscReasonRemote,'dlswCircuitDiscReasonRemoteData':dlswCircuitDiscReasonRemoteData,'dlswSdlc':dlswSdlc,'dlswTraps':dlswTraps})