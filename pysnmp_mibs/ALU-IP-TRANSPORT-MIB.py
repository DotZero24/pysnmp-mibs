_B0='aluIpTransportStatsGroup'
_A_='aluIpTransportNotifyObjsGroup'
_Az='aluIpTransportNotifyGroup'
_Ay='aluIpTransportV8v0Group'
_Ax='aluIpTransportStateChanged'
_Aw='aluIpTransportURemHostSessUpTime'
_Av='aluIpTransportURemHostSessState'
_Au='aluIpTransportURemHostCharsRcvd'
_At='aluIpTransportURemHostPktsRcvd'
_As='aluIpTransportURemHostCharsDrop'
_Ar='aluIpTransportURemHostPktsDrop'
_Aq='aluIpTransportURemHostCharsSent'
_Ap='aluIpTransportURemHostPktsSent'
_Ao='aluIpTransportRemHostInactTmouts'
_An='aluIpTransportRemHostConnsCloFar'
_Am='aluIpTransportRemHostConnFails'
_Al='aluIpTransportRemHostConnRetries'
_Ak='aluIpTransportRemHostConnsFrom'
_Aj='aluIpTransportRemHostConnsTo'
_Ai='aluIpTransportRemHostCharsRcvd'
_Ah='aluIpTransportRemHostPktsRcvd'
_Ag='aluIpTransportRemHostCharsDrop'
_Af='aluIpTransportRemHostPktsDrop'
_Ae='aluIpTransportRemHostCharsSent'
_Ad='aluIpTransportRemHostPktsSent'
_Ac='aluIpTransportPktsDropNoRemHost'
_Ab='aluIpTransportUnkRemCurrConns'
_Aa='aluIpTransportUnkRemLastPortNum'
_AZ='aluIpTransportUnkRemLastIpAddr'
_AY='aluIpTransportUnkRemLastIpAddrTy'
_AX='aluIpTransportUnkRemInactTimouts'
_AW='aluIpTransportUnkRemRejectsResrc'
_AV='aluIpTransportUnkRemRejectsFiltr'
_AU='aluIpTransportUnkRemSuccConnsFrm'
_AT='aluIpTransportUnkRemCharsRcvd'
_AS='aluIpTransportUnkRemPktsRcvd'
_AR='aluIpTransportUnkRemCharsSent'
_AQ='aluIpTransportUnkRemPktsSent'
_AP='aluIpTransportKnwRemCurrConns'
_AO='aluIpTransportKnwRemConnFails'
_AN='aluIpTransportKnwRemConnRetries'
_AM='aluIpTransportKnwRemConnsFrom'
_AL='aluIpTransportKnwRemConnsTo'
_AK='aluIpTransportKnwRemCharsRcvd'
_AJ='aluIpTransportKnwRemPktsRcvd'
_AI='aluIpTransportKnwRemCharsSent'
_AH='aluIpTransportKnwRemPktsSent'
_AG='aluIpTransportRemHostCheckTcpInf'
_AF='aluIpTransportRemHostCheckTcpRes'
_AE='aluIpTransportRemHostCheckTcp'
_AD='aluIpTransportRemHostLastConnect'
_AC='aluIpTransportRemHostSessUpTime'
_AB='aluIpTransportRemHostSessState'
_AA='aluIpTransportRemHostNameId'
_A9='aluIpTransportSvcBaseExtNumIpts'
_A8='aluIpTransportRemHostPortNum'
_A7='aluIpTransportRemHostIpAddr'
_A6='aluIpTransportRemHostIpAddrType'
_A5='aluIpTransportRemHostDescription'
_A4='aluIpTransportRemHostRowStatus'
_A3='aluIpTransportRemHostLastChanged'
_A2='aluIpTransportRemHostTblLastChgd'
_A1='aluIpTransportLastOperChange'
_A0='aluIpTransportNumRemHosts'
_z='aluIpTransportLocHostIpProtocol'
_y='aluIpTransportLocHostPortNum'
_x='aluIpTransportLocHostIpAddr'
_w='aluIpTransportLocHostIpAddrType'
_v='aluIpTransportProfile'
_u='aluIpTransportFcName'
_t='aluIpTransportDscpName'
_s='aluIpTransportFilterUnknownHost'
_r='aluIpTransportTcpConnInactTimout'
_q='aluIpTransportTcpConnRetryIntvl'
_p='aluIpTransportTcpConnMaxRetries'
_o='aluIpTransportDescription'
_n='aluIpTransportRowStatus'
_m='aluIpTransportLastMgmtChange'
_l='aluIpTransportTableLastChanged'
_k='aluIpTransportSvcBaseExtEntry'
_j='aluIpTransportURemHostPortNum'
_i='aluIpTransportURemHostIpAddr'
_h='aluIpTransportURemHostIpAddrType'
_g='unknown'
_f='TmnxEnabledDisabled'
_e='TmnxAdminState'
_d='TmnxActionType'
_c='TProfile'
_b='TLNamedItemOrEmpty'
_a='TFCName'
_Z='TDSCPName'
_Y='InetAddressType'
_X='aluIpTransportNotifyPortId'
_W='aluIpTransportNotifySvcId'
_V='aluIpTransportNotifyCustId'
_U='aluIpTransportOperFlags'
_T='aluIpTransportOperState'
_S='aluIpTransportAdminState'
_R='accessible-for-notify'
_Q='aluIpTransportRemHostName'
_P='aluIpTransportRemHostId'
_O='TItemDescription'
_N='DisplayString'
_M='Integer32'
_L='seconds'
_K='Unsigned32'
_J='not-accessible'
_I='TTcpUdpPort'
_H='InetAddress'
_G='aluIpTransportPortId'
_F='svcId'
_E='TIMETRA-SERV-MIB'
_D='read-create'
_C='read-only'
_B='ALU-IP-TRANSPORT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
aluSARConfs,aluSARMIBModules,aluSARNotifyPrefix,aluSARObjs=mibBuilder.importSymbols('ALU-SAR-GLOBAL-MIB','aluSARConfs','aluSARMIBModules','aluSARNotifyPrefix','aluSARObjs')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_H,_Y)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_M,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_K,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC',_N,'PhysAddress','RowStatus','TextualConvention','TimeStamp')
svcBaseInfoEntry,svcId=mibBuilder.importSymbols(_E,'svcBaseInfoEntry',_F)
TDSCPName,TFCName,TItemDescription,TLNamedItemOrEmpty,TProfile,TTcpUdpPort,TmnxActionType,TmnxAdminState,TmnxCustId,TmnxEnabledDisabled,TmnxOperState,TmnxPortID,TmnxServId=mibBuilder.importSymbols('TIMETRA-TC-MIB',_Z,_a,_O,_b,_c,_I,_d,_e,'TmnxCustId',_f,'TmnxOperState','TmnxPortID','TmnxServId')
aluIpTransportMIBModule=ModuleIdentity((1,3,6,1,4,1,6527,6,1,1,1,3,20))
if mibBuilder.loadTexts:aluIpTransportMIBModule.setRevisions(('2016-02-01 00:00',))
class AluIpTransportRemHostId(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
class AluIpTransportRemHostSessState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('invalid',0),('ready',1),('connecting',2),('connected',3)))
_AluIpTransportConformance_ObjectIdentity=ObjectIdentity
aluIpTransportConformance=_AluIpTransportConformance_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,1,22))
_AluIpTransportCompliances_ObjectIdentity=ObjectIdentity
aluIpTransportCompliances=_AluIpTransportCompliances_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,1,22,1))
_AluIpTransportGroups_ObjectIdentity=ObjectIdentity
aluIpTransportGroups=_AluIpTransportGroups_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,1,22,2))
_AluIpTransportV8v0Groups_ObjectIdentity=ObjectIdentity
aluIpTransportV8v0Groups=_AluIpTransportV8v0Groups_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,1,22,2,1))
_AluIpTransportObjs_ObjectIdentity=ObjectIdentity
aluIpTransportObjs=_AluIpTransportObjs_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,2,22))
_AluIpTransportConfigTimestamps_ObjectIdentity=ObjectIdentity
aluIpTransportConfigTimestamps=_AluIpTransportConfigTimestamps_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,2,22,1))
_AluIpTransportTableLastChanged_Type=TimeStamp
_AluIpTransportTableLastChanged_Object=MibScalar
aluIpTransportTableLastChanged=_AluIpTransportTableLastChanged_Object((1,3,6,1,4,1,6527,6,1,2,2,22,1,1),_AluIpTransportTableLastChanged_Type())
aluIpTransportTableLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:aluIpTransportTableLastChanged.setStatus(_A)
_AluIpTransportRemHostTblLastChgd_Type=TimeStamp
_AluIpTransportRemHostTblLastChgd_Object=MibScalar
aluIpTransportRemHostTblLastChgd=_AluIpTransportRemHostTblLastChgd_Object((1,3,6,1,4,1,6527,6,1,2,2,22,1,2),_AluIpTransportRemHostTblLastChgd_Type())
aluIpTransportRemHostTblLastChgd.setMaxAccess(_C)
if mibBuilder.loadTexts:aluIpTransportRemHostTblLastChgd.setStatus(_A)
_AluIpTransportConfigurations_ObjectIdentity=ObjectIdentity
aluIpTransportConfigurations=_AluIpTransportConfigurations_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,2,22,2))
_AluIpTransportTable_Object=MibTable
aluIpTransportTable=_AluIpTransportTable_Object((1,3,6,1,4,1,6527,6,1,2,2,22,2,1))
if mibBuilder.loadTexts:aluIpTransportTable.setStatus(_A)
_AluIpTransportEntry_Object=MibTableRow
aluIpTransportEntry=_AluIpTransportEntry_Object((1,3,6,1,4,1,6527,6,1,2,2,22,2,1,1))
aluIpTransportEntry.setIndexNames((0,_E,_F),(0,_B,_G))
if mibBuilder.loadTexts:aluIpTransportEntry.setStatus(_A)
_AluIpTransportPortId_Type=TmnxPortID
_AluIpTransportPortId_Object=MibTableColumn
aluIpTransportPortId=_AluIpTransportPortId_Object((1,3,6,1,4,1,6527,6,1,2,2,22,2,1,1,1),_AluIpTransportPortId_Type())
aluIpTransportPortId.setMaxAccess(_J)
if mibBuilder.loadTexts:aluIpTransportPortId.setStatus(_A)
_AluIpTransportLastMgmtChange_Type=TimeStamp
_AluIpTransportLastMgmtChange_Object=MibTableColumn
aluIpTransportLastMgmtChange=_AluIpTransportLastMgmtChange_Object((1,3,6,1,4,1,6527,6,1,2,2,22,2,1,1,2),_AluIpTransportLastMgmtChange_Type())
aluIpTransportLastMgmtChange.setMaxAccess(_C)
if mibBuilder.loadTexts:aluIpTransportLastMgmtChange.setStatus(_A)
_AluIpTransportRowStatus_Type=RowStatus
_AluIpTransportRowStatus_Object=MibTableColumn
aluIpTransportRowStatus=_AluIpTransportRowStatus_Object((1,3,6,1,4,1,6527,6,1,2,2,22,2,1,1,3),_AluIpTransportRowStatus_Type())
aluIpTransportRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:aluIpTransportRowStatus.setStatus(_A)
class _AluIpTransportAdminState_Type(TmnxAdminState):defaultValue=3
_AluIpTransportAdminState_Type.__name__=_e
_AluIpTransportAdminState_Object=MibTableColumn
aluIpTransportAdminState=_AluIpTransportAdminState_Object((1,3,6,1,4,1,6527,6,1,2,2,22,2,1,1,4),_AluIpTransportAdminState_Type())
aluIpTransportAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:aluIpTransportAdminState.setStatus(_A)
class _AluIpTransportDescription_Type(TItemDescription):defaultHexValue=''
_AluIpTransportDescription_Type.__name__=_O
_AluIpTransportDescription_Object=MibTableColumn
aluIpTransportDescription=_AluIpTransportDescription_Object((1,3,6,1,4,1,6527,6,1,2,2,22,2,1,1,5),_AluIpTransportDescription_Type())
aluIpTransportDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:aluIpTransportDescription.setStatus(_A)
class _AluIpTransportTcpConnMaxRetries_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_AluIpTransportTcpConnMaxRetries_Type.__name__=_K
_AluIpTransportTcpConnMaxRetries_Object=MibTableColumn
aluIpTransportTcpConnMaxRetries=_AluIpTransportTcpConnMaxRetries_Object((1,3,6,1,4,1,6527,6,1,2,2,22,2,1,1,6),_AluIpTransportTcpConnMaxRetries_Type())
aluIpTransportTcpConnMaxRetries.setMaxAccess(_D)
if mibBuilder.loadTexts:aluIpTransportTcpConnMaxRetries.setStatus(_A)
class _AluIpTransportTcpConnRetryIntvl_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_AluIpTransportTcpConnRetryIntvl_Type.__name__=_K
_AluIpTransportTcpConnRetryIntvl_Object=MibTableColumn
aluIpTransportTcpConnRetryIntvl=_AluIpTransportTcpConnRetryIntvl_Object((1,3,6,1,4,1,6527,6,1,2,2,22,2,1,1,7),_AluIpTransportTcpConnRetryIntvl_Type())
aluIpTransportTcpConnRetryIntvl.setMaxAccess(_D)
if mibBuilder.loadTexts:aluIpTransportTcpConnRetryIntvl.setStatus(_A)
if mibBuilder.loadTexts:aluIpTransportTcpConnRetryIntvl.setUnits(_L)
class _AluIpTransportTcpConnInactTimout_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AluIpTransportTcpConnInactTimout_Type.__name__=_K
_AluIpTransportTcpConnInactTimout_Object=MibTableColumn
aluIpTransportTcpConnInactTimout=_AluIpTransportTcpConnInactTimout_Object((1,3,6,1,4,1,6527,6,1,2,2,22,2,1,1,8),_AluIpTransportTcpConnInactTimout_Type())
aluIpTransportTcpConnInactTimout.setMaxAccess(_D)
if mibBuilder.loadTexts:aluIpTransportTcpConnInactTimout.setStatus(_A)
if mibBuilder.loadTexts:aluIpTransportTcpConnInactTimout.setUnits(_L)
class _AluIpTransportFilterUnknownHost_Type(TmnxEnabledDisabled):defaultValue=2
_AluIpTransportFilterUnknownHost_Type.__name__=_f
_AluIpTransportFilterUnknownHost_Object=MibTableColumn
aluIpTransportFilterUnknownHost=_AluIpTransportFilterUnknownHost_Object((1,3,6,1,4,1,6527,6,1,2,2,22,2,1,1,9),_AluIpTransportFilterUnknownHost_Type())
aluIpTransportFilterUnknownHost.setMaxAccess(_D)
if mibBuilder.loadTexts:aluIpTransportFilterUnknownHost.setStatus(_A)
class _AluIpTransportDscpName_Type(TDSCPName):defaultValue=OctetString('ef')
_AluIpTransportDscpName_Type.__name__=_Z
_AluIpTransportDscpName_Object=MibTableColumn
aluIpTransportDscpName=_AluIpTransportDscpName_Object((1,3,6,1,4,1,6527,6,1,2,2,22,2,1,1,10),_AluIpTransportDscpName_Type())
aluIpTransportDscpName.setMaxAccess(_D)
if mibBuilder.loadTexts:aluIpTransportDscpName.setStatus(_A)
class _AluIpTransportFcName_Type(TFCName):defaultValue=OctetString('ef')
_AluIpTransportFcName_Type.__name__=_a
_AluIpTransportFcName_Object=MibTableColumn
aluIpTransportFcName=_AluIpTransportFcName_Object((1,3,6,1,4,1,6527,6,1,2,2,22,2,1,1,11),_AluIpTransportFcName_Type())
aluIpTransportFcName.setMaxAccess(_D)
if mibBuilder.loadTexts:aluIpTransportFcName.setStatus(_A)
class _AluIpTransportProfile_Type(TProfile):defaultValue=1
_AluIpTransportProfile_Type.__name__=_c
_AluIpTransportProfile_Object=MibTableColumn
aluIpTransportProfile=_AluIpTransportProfile_Object((1,3,6,1,4,1,6527,6,1,2,2,22,2,1,1,12),_AluIpTransportProfile_Type())
aluIpTransportProfile.setMaxAccess(_D)
if mibBuilder.loadTexts:aluIpTransportProfile.setStatus(_A)
class _AluIpTransportLocHostIpAddrType_Type(InetAddressType):defaultValue=0;subtypeSpec=InetAddressType.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_g,0),('ipv4',1)))
_AluIpTransportLocHostIpAddrType_Type.__name__=_Y
_AluIpTransportLocHostIpAddrType_Object=MibTableColumn
aluIpTransportLocHostIpAddrType=_AluIpTransportLocHostIpAddrType_Object((1,3,6,1,4,1,6527,6,1,2,2,22,2,1,1,13),_AluIpTransportLocHostIpAddrType_Type())
aluIpTransportLocHostIpAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:aluIpTransportLocHostIpAddrType.setStatus(_A)
class _AluIpTransportLocHostIpAddr_Type(InetAddress):defaultHexValue='';subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_AluIpTransportLocHostIpAddr_Type.__name__=_H
_AluIpTransportLocHostIpAddr_Object=MibTableColumn
aluIpTransportLocHostIpAddr=_AluIpTransportLocHostIpAddr_Object((1,3,6,1,4,1,6527,6,1,2,2,22,2,1,1,14),_AluIpTransportLocHostIpAddr_Type())
aluIpTransportLocHostIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:aluIpTransportLocHostIpAddr.setStatus(_A)
class _AluIpTransportLocHostPortNum_Type(TTcpUdpPort):defaultValue=0;subtypeSpec=TTcpUdpPort.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1026,49150))
_AluIpTransportLocHostPortNum_Type.__name__=_I
_AluIpTransportLocHostPortNum_Object=MibTableColumn
aluIpTransportLocHostPortNum=_AluIpTransportLocHostPortNum_Object((1,3,6,1,4,1,6527,6,1,2,2,22,2,1,1,15),_AluIpTransportLocHostPortNum_Type())
aluIpTransportLocHostPortNum.setMaxAccess(_D)
if mibBuilder.loadTexts:aluIpTransportLocHostPortNum.setStatus(_A)
class _AluIpTransportLocHostIpProtocol_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,6,17)));namedValues=NamedValues(*(('unset',-1),('tcp',6),('udp',17)))
_AluIpTransportLocHostIpProtocol_Type.__name__=_M
_AluIpTransportLocHostIpProtocol_Object=MibTableColumn
aluIpTransportLocHostIpProtocol=_AluIpTransportLocHostIpProtocol_Object((1,3,6,1,4,1,6527,6,1,2,2,22,2,1,1,16),_AluIpTransportLocHostIpProtocol_Type())
aluIpTransportLocHostIpProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:aluIpTransportLocHostIpProtocol.setStatus(_A)
_AluIpTransportNumRemHosts_Type=Unsigned32
_AluIpTransportNumRemHosts_Object=MibTableColumn
aluIpTransportNumRemHosts=_AluIpTransportNumRemHosts_Object((1,3,6,1,4,1,6527,6,1,2,2,22,2,1,1,17),_AluIpTransportNumRemHosts_Type())
aluIpTransportNumRemHosts.setMaxAccess(_C)
if mibBuilder.loadTexts:aluIpTransportNumRemHosts.setStatus(_A)
_AluIpTransportOperState_Type=TmnxOperState
_AluIpTransportOperState_Object=MibTableColumn
aluIpTransportOperState=_AluIpTransportOperState_Object((1,3,6,1,4,1,6527,6,1,2,2,22,2,1,1,18),_AluIpTransportOperState_Type())
aluIpTransportOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:aluIpTransportOperState.setStatus(_A)
class _AluIpTransportOperFlags_Type(Bits):namedValues=NamedValues(*(('iptAdminDown',0),('svcAdminDown',1),('portOperDown',2),('noIfAddress',3),('ifOperDown',4),('portNumInUse',5),('portNumReserved',6)))
_AluIpTransportOperFlags_Type.__name__='Bits'
_AluIpTransportOperFlags_Object=MibTableColumn
aluIpTransportOperFlags=_AluIpTransportOperFlags_Object((1,3,6,1,4,1,6527,6,1,2,2,22,2,1,1,19),_AluIpTransportOperFlags_Type())
aluIpTransportOperFlags.setMaxAccess(_C)
if mibBuilder.loadTexts:aluIpTransportOperFlags.setStatus(_A)
_AluIpTransportLastOperChange_Type=TimeStamp
_AluIpTransportLastOperChange_Object=MibTableColumn
aluIpTransportLastOperChange=_AluIpTransportLastOperChange_Object((1,3,6,1,4,1,6527,6,1,2,2,22,2,1,1,20),_AluIpTransportLastOperChange_Type())
aluIpTransportLastOperChange.setMaxAccess(_C)
if mibBuilder.loadTexts:aluIpTransportLastOperChange.setStatus(_A)
_AluIpTransportRemHostTable_Object=MibTable
aluIpTransportRemHostTable=_AluIpTransportRemHostTable_Object((1,3,6,1,4,1,6527,6,1,2,2,22,2,2))
if mibBuilder.loadTexts:aluIpTransportRemHostTable.setStatus(_A)
_AluIpTransportRemHostEntry_Object=MibTableRow
aluIpTransportRemHostEntry=_AluIpTransportRemHostEntry_Object((1,3,6,1,4,1,6527,6,1,2,2,22,2,2,1))
aluIpTransportRemHostEntry.setIndexNames((0,_E,_F),(0,_B,_G),(0,_B,_P))
if mibBuilder.loadTexts:aluIpTransportRemHostEntry.setStatus(_A)
_AluIpTransportRemHostId_Type=AluIpTransportRemHostId
_AluIpTransportRemHostId_Object=MibTableColumn
aluIpTransportRemHostId=_AluIpTransportRemHostId_Object((1,3,6,1,4,1,6527,6,1,2,2,22,2,2,1,1),_AluIpTransportRemHostId_Type())
aluIpTransportRemHostId.setMaxAccess(_J)
if mibBuilder.loadTexts:aluIpTransportRemHostId.setStatus(_A)
_AluIpTransportRemHostLastChanged_Type=TimeStamp
_AluIpTransportRemHostLastChanged_Object=MibTableColumn
aluIpTransportRemHostLastChanged=_AluIpTransportRemHostLastChanged_Object((1,3,6,1,4,1,6527,6,1,2,2,22,2,2,1,2),_AluIpTransportRemHostLastChanged_Type())
aluIpTransportRemHostLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:aluIpTransportRemHostLastChanged.setStatus(_A)
_AluIpTransportRemHostRowStatus_Type=RowStatus
_AluIpTransportRemHostRowStatus_Object=MibTableColumn
aluIpTransportRemHostRowStatus=_AluIpTransportRemHostRowStatus_Object((1,3,6,1,4,1,6527,6,1,2,2,22,2,2,1,3),_AluIpTransportRemHostRowStatus_Type())
aluIpTransportRemHostRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:aluIpTransportRemHostRowStatus.setStatus(_A)
class _AluIpTransportRemHostName_Type(TLNamedItemOrEmpty):defaultHexValue=''
_AluIpTransportRemHostName_Type.__name__=_b
_AluIpTransportRemHostName_Object=MibTableColumn
aluIpTransportRemHostName=_AluIpTransportRemHostName_Object((1,3,6,1,4,1,6527,6,1,2,2,22,2,2,1,4),_AluIpTransportRemHostName_Type())
aluIpTransportRemHostName.setMaxAccess(_D)
if mibBuilder.loadTexts:aluIpTransportRemHostName.setStatus(_A)
class _AluIpTransportRemHostDescription_Type(TItemDescription):defaultHexValue=''
_AluIpTransportRemHostDescription_Type.__name__=_O
_AluIpTransportRemHostDescription_Object=MibTableColumn
aluIpTransportRemHostDescription=_AluIpTransportRemHostDescription_Object((1,3,6,1,4,1,6527,6,1,2,2,22,2,2,1,5),_AluIpTransportRemHostDescription_Type())
aluIpTransportRemHostDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:aluIpTransportRemHostDescription.setStatus(_A)
_AluIpTransportRemHostIpAddrType_Type=InetAddressType
_AluIpTransportRemHostIpAddrType_Object=MibTableColumn
aluIpTransportRemHostIpAddrType=_AluIpTransportRemHostIpAddrType_Object((1,3,6,1,4,1,6527,6,1,2,2,22,2,2,1,6),_AluIpTransportRemHostIpAddrType_Type())
aluIpTransportRemHostIpAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:aluIpTransportRemHostIpAddrType.setStatus(_A)
class _AluIpTransportRemHostIpAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_AluIpTransportRemHostIpAddr_Type.__name__=_H
_AluIpTransportRemHostIpAddr_Object=MibTableColumn
aluIpTransportRemHostIpAddr=_AluIpTransportRemHostIpAddr_Object((1,3,6,1,4,1,6527,6,1,2,2,22,2,2,1,7),_AluIpTransportRemHostIpAddr_Type())
aluIpTransportRemHostIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:aluIpTransportRemHostIpAddr.setStatus(_A)
class _AluIpTransportRemHostPortNum_Type(TTcpUdpPort):subtypeSpec=TTcpUdpPort.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AluIpTransportRemHostPortNum_Type.__name__=_I
_AluIpTransportRemHostPortNum_Object=MibTableColumn
aluIpTransportRemHostPortNum=_AluIpTransportRemHostPortNum_Object((1,3,6,1,4,1,6527,6,1,2,2,22,2,2,1,8),_AluIpTransportRemHostPortNum_Type())
aluIpTransportRemHostPortNum.setMaxAccess(_D)
if mibBuilder.loadTexts:aluIpTransportRemHostPortNum.setStatus(_A)
_AluIpTransportRemHostSessState_Type=AluIpTransportRemHostSessState
_AluIpTransportRemHostSessState_Object=MibTableColumn
aluIpTransportRemHostSessState=_AluIpTransportRemHostSessState_Object((1,3,6,1,4,1,6527,6,1,2,2,22,2,2,1,9),_AluIpTransportRemHostSessState_Type())
aluIpTransportRemHostSessState.setMaxAccess(_C)
if mibBuilder.loadTexts:aluIpTransportRemHostSessState.setStatus(_A)
_AluIpTransportRemHostSessUpTime_Type=Unsigned32
_AluIpTransportRemHostSessUpTime_Object=MibTableColumn
aluIpTransportRemHostSessUpTime=_AluIpTransportRemHostSessUpTime_Object((1,3,6,1,4,1,6527,6,1,2,2,22,2,2,1,10),_AluIpTransportRemHostSessUpTime_Type())
aluIpTransportRemHostSessUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:aluIpTransportRemHostSessUpTime.setStatus(_A)
if mibBuilder.loadTexts:aluIpTransportRemHostSessUpTime.setUnits(_L)
class _AluIpTransportRemHostLastConnect_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AluIpTransportRemHostLastConnect_Type.__name__=_N
_AluIpTransportRemHostLastConnect_Object=MibTableColumn
aluIpTransportRemHostLastConnect=_AluIpTransportRemHostLastConnect_Object((1,3,6,1,4,1,6527,6,1,2,2,22,2,2,1,11),_AluIpTransportRemHostLastConnect_Type())
aluIpTransportRemHostLastConnect.setMaxAccess(_C)
if mibBuilder.loadTexts:aluIpTransportRemHostLastConnect.setStatus(_A)
class _AluIpTransportRemHostCheckTcp_Type(TmnxActionType):defaultValue=2
_AluIpTransportRemHostCheckTcp_Type.__name__=_d
_AluIpTransportRemHostCheckTcp_Object=MibTableColumn
aluIpTransportRemHostCheckTcp=_AluIpTransportRemHostCheckTcp_Object((1,3,6,1,4,1,6527,6,1,2,2,22,2,2,1,12),_AluIpTransportRemHostCheckTcp_Type())
aluIpTransportRemHostCheckTcp.setMaxAccess(_D)
if mibBuilder.loadTexts:aluIpTransportRemHostCheckTcp.setStatus(_A)
class _AluIpTransportRemHostCheckTcpRes_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_g,1),('pass',2),('fail',3)))
_AluIpTransportRemHostCheckTcpRes_Type.__name__=_M
_AluIpTransportRemHostCheckTcpRes_Object=MibTableColumn
aluIpTransportRemHostCheckTcpRes=_AluIpTransportRemHostCheckTcpRes_Object((1,3,6,1,4,1,6527,6,1,2,2,22,2,2,1,13),_AluIpTransportRemHostCheckTcpRes_Type())
aluIpTransportRemHostCheckTcpRes.setMaxAccess(_C)
if mibBuilder.loadTexts:aluIpTransportRemHostCheckTcpRes.setStatus(_A)
class _AluIpTransportRemHostCheckTcpInf_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AluIpTransportRemHostCheckTcpInf_Type.__name__=_N
_AluIpTransportRemHostCheckTcpInf_Object=MibTableColumn
aluIpTransportRemHostCheckTcpInf=_AluIpTransportRemHostCheckTcpInf_Object((1,3,6,1,4,1,6527,6,1,2,2,22,2,2,1,14),_AluIpTransportRemHostCheckTcpInf_Type())
aluIpTransportRemHostCheckTcpInf.setMaxAccess(_C)
if mibBuilder.loadTexts:aluIpTransportRemHostCheckTcpInf.setStatus(_A)
_AluIpTransportSvcBaseExtTable_Object=MibTable
aluIpTransportSvcBaseExtTable=_AluIpTransportSvcBaseExtTable_Object((1,3,6,1,4,1,6527,6,1,2,2,22,2,3))
if mibBuilder.loadTexts:aluIpTransportSvcBaseExtTable.setStatus(_A)
_AluIpTransportSvcBaseExtEntry_Object=MibTableRow
aluIpTransportSvcBaseExtEntry=_AluIpTransportSvcBaseExtEntry_Object((1,3,6,1,4,1,6527,6,1,2,2,22,2,3,1))
if mibBuilder.loadTexts:aluIpTransportSvcBaseExtEntry.setStatus(_A)
_AluIpTransportSvcBaseExtNumIpts_Type=Unsigned32
_AluIpTransportSvcBaseExtNumIpts_Object=MibTableColumn
aluIpTransportSvcBaseExtNumIpts=_AluIpTransportSvcBaseExtNumIpts_Object((1,3,6,1,4,1,6527,6,1,2,2,22,2,3,1,1),_AluIpTransportSvcBaseExtNumIpts_Type())
aluIpTransportSvcBaseExtNumIpts.setMaxAccess(_C)
if mibBuilder.loadTexts:aluIpTransportSvcBaseExtNumIpts.setStatus(_A)
_AluIpTransportNameObjects_ObjectIdentity=ObjectIdentity
aluIpTransportNameObjects=_AluIpTransportNameObjects_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,2,22,3))
_AluIpTransportRemHostNameTable_Object=MibTable
aluIpTransportRemHostNameTable=_AluIpTransportRemHostNameTable_Object((1,3,6,1,4,1,6527,6,1,2,2,22,3,1))
if mibBuilder.loadTexts:aluIpTransportRemHostNameTable.setStatus(_A)
_AluIpTransportRemHostNameEntry_Object=MibTableRow
aluIpTransportRemHostNameEntry=_AluIpTransportRemHostNameEntry_Object((1,3,6,1,4,1,6527,6,1,2,2,22,3,1,1))
aluIpTransportRemHostNameEntry.setIndexNames((0,_E,_F),(0,_B,_G),(0,_B,_Q))
if mibBuilder.loadTexts:aluIpTransportRemHostNameEntry.setStatus(_A)
_AluIpTransportRemHostNameId_Type=AluIpTransportRemHostId
_AluIpTransportRemHostNameId_Object=MibTableColumn
aluIpTransportRemHostNameId=_AluIpTransportRemHostNameId_Object((1,3,6,1,4,1,6527,6,1,2,2,22,3,1,1,1),_AluIpTransportRemHostNameId_Type())
aluIpTransportRemHostNameId.setMaxAccess(_C)
if mibBuilder.loadTexts:aluIpTransportRemHostNameId.setStatus(_A)
_AluIpTransportStatus_ObjectIdentity=ObjectIdentity
aluIpTransportStatus=_AluIpTransportStatus_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,2,22,4))
_AluIpTransportStatsObjects_ObjectIdentity=ObjectIdentity
aluIpTransportStatsObjects=_AluIpTransportStatsObjects_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,2,22,5))
_AluIpTransportStatsTable_Object=MibTable
aluIpTransportStatsTable=_AluIpTransportStatsTable_Object((1,3,6,1,4,1,6527,6,1,2,2,22,5,1))
if mibBuilder.loadTexts:aluIpTransportStatsTable.setStatus(_A)
_AluIpTransportStatsEntry_Object=MibTableRow
aluIpTransportStatsEntry=_AluIpTransportStatsEntry_Object((1,3,6,1,4,1,6527,6,1,2,2,22,5,1,1))
aluIpTransportStatsEntry.setIndexNames((0,_E,_F),(0,_B,_G))
if mibBuilder.loadTexts:aluIpTransportStatsEntry.setStatus(_A)
_AluIpTransportKnwRemPktsSent_Type=Counter64
_AluIpTransportKnwRemPktsSent_Object=MibTableColumn
aluIpTransportKnwRemPktsSent=_AluIpTransportKnwRemPktsSent_Object((1,3,6,1,4,1,6527,6,1,2,2,22,5,1,1,1),_AluIpTransportKnwRemPktsSent_Type())
aluIpTransportKnwRemPktsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:aluIpTransportKnwRemPktsSent.setStatus(_A)
_AluIpTransportKnwRemCharsSent_Type=Counter64
_AluIpTransportKnwRemCharsSent_Object=MibTableColumn
aluIpTransportKnwRemCharsSent=_AluIpTransportKnwRemCharsSent_Object((1,3,6,1,4,1,6527,6,1,2,2,22,5,1,1,2),_AluIpTransportKnwRemCharsSent_Type())
aluIpTransportKnwRemCharsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:aluIpTransportKnwRemCharsSent.setStatus(_A)
_AluIpTransportKnwRemPktsRcvd_Type=Counter64
_AluIpTransportKnwRemPktsRcvd_Object=MibTableColumn
aluIpTransportKnwRemPktsRcvd=_AluIpTransportKnwRemPktsRcvd_Object((1,3,6,1,4,1,6527,6,1,2,2,22,5,1,1,3),_AluIpTransportKnwRemPktsRcvd_Type())
aluIpTransportKnwRemPktsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:aluIpTransportKnwRemPktsRcvd.setStatus(_A)
_AluIpTransportKnwRemCharsRcvd_Type=Counter64
_AluIpTransportKnwRemCharsRcvd_Object=MibTableColumn
aluIpTransportKnwRemCharsRcvd=_AluIpTransportKnwRemCharsRcvd_Object((1,3,6,1,4,1,6527,6,1,2,2,22,5,1,1,4),_AluIpTransportKnwRemCharsRcvd_Type())
aluIpTransportKnwRemCharsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:aluIpTransportKnwRemCharsRcvd.setStatus(_A)
_AluIpTransportKnwRemConnsTo_Type=Counter32
_AluIpTransportKnwRemConnsTo_Object=MibTableColumn
aluIpTransportKnwRemConnsTo=_AluIpTransportKnwRemConnsTo_Object((1,3,6,1,4,1,6527,6,1,2,2,22,5,1,1,5),_AluIpTransportKnwRemConnsTo_Type())
aluIpTransportKnwRemConnsTo.setMaxAccess(_C)
if mibBuilder.loadTexts:aluIpTransportKnwRemConnsTo.setStatus(_A)
_AluIpTransportKnwRemConnsFrom_Type=Counter32
_AluIpTransportKnwRemConnsFrom_Object=MibTableColumn
aluIpTransportKnwRemConnsFrom=_AluIpTransportKnwRemConnsFrom_Object((1,3,6,1,4,1,6527,6,1,2,2,22,5,1,1,6),_AluIpTransportKnwRemConnsFrom_Type())
aluIpTransportKnwRemConnsFrom.setMaxAccess(_C)
if mibBuilder.loadTexts:aluIpTransportKnwRemConnsFrom.setStatus(_A)
_AluIpTransportKnwRemConnRetries_Type=Counter32
_AluIpTransportKnwRemConnRetries_Object=MibTableColumn
aluIpTransportKnwRemConnRetries=_AluIpTransportKnwRemConnRetries_Object((1,3,6,1,4,1,6527,6,1,2,2,22,5,1,1,7),_AluIpTransportKnwRemConnRetries_Type())
aluIpTransportKnwRemConnRetries.setMaxAccess(_C)
if mibBuilder.loadTexts:aluIpTransportKnwRemConnRetries.setStatus(_A)
_AluIpTransportKnwRemConnFails_Type=Counter32
_AluIpTransportKnwRemConnFails_Object=MibTableColumn
aluIpTransportKnwRemConnFails=_AluIpTransportKnwRemConnFails_Object((1,3,6,1,4,1,6527,6,1,2,2,22,5,1,1,8),_AluIpTransportKnwRemConnFails_Type())
aluIpTransportKnwRemConnFails.setMaxAccess(_C)
if mibBuilder.loadTexts:aluIpTransportKnwRemConnFails.setStatus(_A)
_AluIpTransportKnwRemCurrConns_Type=Unsigned32
_AluIpTransportKnwRemCurrConns_Object=MibTableColumn
aluIpTransportKnwRemCurrConns=_AluIpTransportKnwRemCurrConns_Object((1,3,6,1,4,1,6527,6,1,2,2,22,5,1,1,9),_AluIpTransportKnwRemCurrConns_Type())
aluIpTransportKnwRemCurrConns.setMaxAccess(_C)
if mibBuilder.loadTexts:aluIpTransportKnwRemCurrConns.setStatus(_A)
_AluIpTransportUnkRemPktsSent_Type=Counter64
_AluIpTransportUnkRemPktsSent_Object=MibTableColumn
aluIpTransportUnkRemPktsSent=_AluIpTransportUnkRemPktsSent_Object((1,3,6,1,4,1,6527,6,1,2,2,22,5,1,1,10),_AluIpTransportUnkRemPktsSent_Type())
aluIpTransportUnkRemPktsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:aluIpTransportUnkRemPktsSent.setStatus(_A)
_AluIpTransportUnkRemCharsSent_Type=Counter64
_AluIpTransportUnkRemCharsSent_Object=MibTableColumn
aluIpTransportUnkRemCharsSent=_AluIpTransportUnkRemCharsSent_Object((1,3,6,1,4,1,6527,6,1,2,2,22,5,1,1,11),_AluIpTransportUnkRemCharsSent_Type())
aluIpTransportUnkRemCharsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:aluIpTransportUnkRemCharsSent.setStatus(_A)
_AluIpTransportUnkRemPktsRcvd_Type=Counter64
_AluIpTransportUnkRemPktsRcvd_Object=MibTableColumn
aluIpTransportUnkRemPktsRcvd=_AluIpTransportUnkRemPktsRcvd_Object((1,3,6,1,4,1,6527,6,1,2,2,22,5,1,1,12),_AluIpTransportUnkRemPktsRcvd_Type())
aluIpTransportUnkRemPktsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:aluIpTransportUnkRemPktsRcvd.setStatus(_A)
_AluIpTransportUnkRemCharsRcvd_Type=Counter64
_AluIpTransportUnkRemCharsRcvd_Object=MibTableColumn
aluIpTransportUnkRemCharsRcvd=_AluIpTransportUnkRemCharsRcvd_Object((1,3,6,1,4,1,6527,6,1,2,2,22,5,1,1,13),_AluIpTransportUnkRemCharsRcvd_Type())
aluIpTransportUnkRemCharsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:aluIpTransportUnkRemCharsRcvd.setStatus(_A)
_AluIpTransportUnkRemSuccConnsFrm_Type=Counter32
_AluIpTransportUnkRemSuccConnsFrm_Object=MibTableColumn
aluIpTransportUnkRemSuccConnsFrm=_AluIpTransportUnkRemSuccConnsFrm_Object((1,3,6,1,4,1,6527,6,1,2,2,22,5,1,1,14),_AluIpTransportUnkRemSuccConnsFrm_Type())
aluIpTransportUnkRemSuccConnsFrm.setMaxAccess(_C)
if mibBuilder.loadTexts:aluIpTransportUnkRemSuccConnsFrm.setStatus(_A)
_AluIpTransportUnkRemRejectsFiltr_Type=Counter32
_AluIpTransportUnkRemRejectsFiltr_Object=MibTableColumn
aluIpTransportUnkRemRejectsFiltr=_AluIpTransportUnkRemRejectsFiltr_Object((1,3,6,1,4,1,6527,6,1,2,2,22,5,1,1,15),_AluIpTransportUnkRemRejectsFiltr_Type())
aluIpTransportUnkRemRejectsFiltr.setMaxAccess(_C)
if mibBuilder.loadTexts:aluIpTransportUnkRemRejectsFiltr.setStatus(_A)
_AluIpTransportUnkRemRejectsResrc_Type=Counter32
_AluIpTransportUnkRemRejectsResrc_Object=MibTableColumn
aluIpTransportUnkRemRejectsResrc=_AluIpTransportUnkRemRejectsResrc_Object((1,3,6,1,4,1,6527,6,1,2,2,22,5,1,1,16),_AluIpTransportUnkRemRejectsResrc_Type())
aluIpTransportUnkRemRejectsResrc.setMaxAccess(_C)
if mibBuilder.loadTexts:aluIpTransportUnkRemRejectsResrc.setStatus(_A)
_AluIpTransportUnkRemInactTimouts_Type=Counter32
_AluIpTransportUnkRemInactTimouts_Object=MibTableColumn
aluIpTransportUnkRemInactTimouts=_AluIpTransportUnkRemInactTimouts_Object((1,3,6,1,4,1,6527,6,1,2,2,22,5,1,1,17),_AluIpTransportUnkRemInactTimouts_Type())
aluIpTransportUnkRemInactTimouts.setMaxAccess(_C)
if mibBuilder.loadTexts:aluIpTransportUnkRemInactTimouts.setStatus(_A)
_AluIpTransportUnkRemLastIpAddrTy_Type=InetAddressType
_AluIpTransportUnkRemLastIpAddrTy_Object=MibTableColumn
aluIpTransportUnkRemLastIpAddrTy=_AluIpTransportUnkRemLastIpAddrTy_Object((1,3,6,1,4,1,6527,6,1,2,2,22,5,1,1,18),_AluIpTransportUnkRemLastIpAddrTy_Type())
aluIpTransportUnkRemLastIpAddrTy.setMaxAccess(_C)
if mibBuilder.loadTexts:aluIpTransportUnkRemLastIpAddrTy.setStatus(_A)
class _AluIpTransportUnkRemLastIpAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_AluIpTransportUnkRemLastIpAddr_Type.__name__=_H
_AluIpTransportUnkRemLastIpAddr_Object=MibTableColumn
aluIpTransportUnkRemLastIpAddr=_AluIpTransportUnkRemLastIpAddr_Object((1,3,6,1,4,1,6527,6,1,2,2,22,5,1,1,19),_AluIpTransportUnkRemLastIpAddr_Type())
aluIpTransportUnkRemLastIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:aluIpTransportUnkRemLastIpAddr.setStatus(_A)
class _AluIpTransportUnkRemLastPortNum_Type(TTcpUdpPort):subtypeSpec=TTcpUdpPort.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,65535))
_AluIpTransportUnkRemLastPortNum_Type.__name__=_I
_AluIpTransportUnkRemLastPortNum_Object=MibTableColumn
aluIpTransportUnkRemLastPortNum=_AluIpTransportUnkRemLastPortNum_Object((1,3,6,1,4,1,6527,6,1,2,2,22,5,1,1,20),_AluIpTransportUnkRemLastPortNum_Type())
aluIpTransportUnkRemLastPortNum.setMaxAccess(_C)
if mibBuilder.loadTexts:aluIpTransportUnkRemLastPortNum.setStatus(_A)
_AluIpTransportUnkRemCurrConns_Type=Unsigned32
_AluIpTransportUnkRemCurrConns_Object=MibTableColumn
aluIpTransportUnkRemCurrConns=_AluIpTransportUnkRemCurrConns_Object((1,3,6,1,4,1,6527,6,1,2,2,22,5,1,1,21),_AluIpTransportUnkRemCurrConns_Type())
aluIpTransportUnkRemCurrConns.setMaxAccess(_C)
if mibBuilder.loadTexts:aluIpTransportUnkRemCurrConns.setStatus(_A)
_AluIpTransportPktsDropNoRemHost_Type=Counter64
_AluIpTransportPktsDropNoRemHost_Object=MibTableColumn
aluIpTransportPktsDropNoRemHost=_AluIpTransportPktsDropNoRemHost_Object((1,3,6,1,4,1,6527,6,1,2,2,22,5,1,1,22),_AluIpTransportPktsDropNoRemHost_Type())
aluIpTransportPktsDropNoRemHost.setMaxAccess(_C)
if mibBuilder.loadTexts:aluIpTransportPktsDropNoRemHost.setStatus(_A)
_AluIpTransportRemHostStatsTable_Object=MibTable
aluIpTransportRemHostStatsTable=_AluIpTransportRemHostStatsTable_Object((1,3,6,1,4,1,6527,6,1,2,2,22,5,2))
if mibBuilder.loadTexts:aluIpTransportRemHostStatsTable.setStatus(_A)
_AluIpTransportRemHostStatsEntry_Object=MibTableRow
aluIpTransportRemHostStatsEntry=_AluIpTransportRemHostStatsEntry_Object((1,3,6,1,4,1,6527,6,1,2,2,22,5,2,1))
aluIpTransportRemHostStatsEntry.setIndexNames((0,_E,_F),(0,_B,_G),(0,_B,_P))
if mibBuilder.loadTexts:aluIpTransportRemHostStatsEntry.setStatus(_A)
_AluIpTransportRemHostPktsSent_Type=Counter64
_AluIpTransportRemHostPktsSent_Object=MibTableColumn
aluIpTransportRemHostPktsSent=_AluIpTransportRemHostPktsSent_Object((1,3,6,1,4,1,6527,6,1,2,2,22,5,2,1,1),_AluIpTransportRemHostPktsSent_Type())
aluIpTransportRemHostPktsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:aluIpTransportRemHostPktsSent.setStatus(_A)
_AluIpTransportRemHostCharsSent_Type=Counter64
_AluIpTransportRemHostCharsSent_Object=MibTableColumn
aluIpTransportRemHostCharsSent=_AluIpTransportRemHostCharsSent_Object((1,3,6,1,4,1,6527,6,1,2,2,22,5,2,1,2),_AluIpTransportRemHostCharsSent_Type())
aluIpTransportRemHostCharsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:aluIpTransportRemHostCharsSent.setStatus(_A)
_AluIpTransportRemHostPktsDrop_Type=Counter64
_AluIpTransportRemHostPktsDrop_Object=MibTableColumn
aluIpTransportRemHostPktsDrop=_AluIpTransportRemHostPktsDrop_Object((1,3,6,1,4,1,6527,6,1,2,2,22,5,2,1,3),_AluIpTransportRemHostPktsDrop_Type())
aluIpTransportRemHostPktsDrop.setMaxAccess(_C)
if mibBuilder.loadTexts:aluIpTransportRemHostPktsDrop.setStatus(_A)
_AluIpTransportRemHostCharsDrop_Type=Counter64
_AluIpTransportRemHostCharsDrop_Object=MibTableColumn
aluIpTransportRemHostCharsDrop=_AluIpTransportRemHostCharsDrop_Object((1,3,6,1,4,1,6527,6,1,2,2,22,5,2,1,4),_AluIpTransportRemHostCharsDrop_Type())
aluIpTransportRemHostCharsDrop.setMaxAccess(_C)
if mibBuilder.loadTexts:aluIpTransportRemHostCharsDrop.setStatus(_A)
_AluIpTransportRemHostPktsRcvd_Type=Counter64
_AluIpTransportRemHostPktsRcvd_Object=MibTableColumn
aluIpTransportRemHostPktsRcvd=_AluIpTransportRemHostPktsRcvd_Object((1,3,6,1,4,1,6527,6,1,2,2,22,5,2,1,5),_AluIpTransportRemHostPktsRcvd_Type())
aluIpTransportRemHostPktsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:aluIpTransportRemHostPktsRcvd.setStatus(_A)
_AluIpTransportRemHostCharsRcvd_Type=Counter64
_AluIpTransportRemHostCharsRcvd_Object=MibTableColumn
aluIpTransportRemHostCharsRcvd=_AluIpTransportRemHostCharsRcvd_Object((1,3,6,1,4,1,6527,6,1,2,2,22,5,2,1,6),_AluIpTransportRemHostCharsRcvd_Type())
aluIpTransportRemHostCharsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:aluIpTransportRemHostCharsRcvd.setStatus(_A)
_AluIpTransportRemHostConnsTo_Type=Counter32
_AluIpTransportRemHostConnsTo_Object=MibTableColumn
aluIpTransportRemHostConnsTo=_AluIpTransportRemHostConnsTo_Object((1,3,6,1,4,1,6527,6,1,2,2,22,5,2,1,7),_AluIpTransportRemHostConnsTo_Type())
aluIpTransportRemHostConnsTo.setMaxAccess(_C)
if mibBuilder.loadTexts:aluIpTransportRemHostConnsTo.setStatus(_A)
_AluIpTransportRemHostConnsFrom_Type=Counter32
_AluIpTransportRemHostConnsFrom_Object=MibTableColumn
aluIpTransportRemHostConnsFrom=_AluIpTransportRemHostConnsFrom_Object((1,3,6,1,4,1,6527,6,1,2,2,22,5,2,1,8),_AluIpTransportRemHostConnsFrom_Type())
aluIpTransportRemHostConnsFrom.setMaxAccess(_C)
if mibBuilder.loadTexts:aluIpTransportRemHostConnsFrom.setStatus(_A)
_AluIpTransportRemHostConnRetries_Type=Counter32
_AluIpTransportRemHostConnRetries_Object=MibTableColumn
aluIpTransportRemHostConnRetries=_AluIpTransportRemHostConnRetries_Object((1,3,6,1,4,1,6527,6,1,2,2,22,5,2,1,9),_AluIpTransportRemHostConnRetries_Type())
aluIpTransportRemHostConnRetries.setMaxAccess(_C)
if mibBuilder.loadTexts:aluIpTransportRemHostConnRetries.setStatus(_A)
_AluIpTransportRemHostConnFails_Type=Counter32
_AluIpTransportRemHostConnFails_Object=MibTableColumn
aluIpTransportRemHostConnFails=_AluIpTransportRemHostConnFails_Object((1,3,6,1,4,1,6527,6,1,2,2,22,5,2,1,10),_AluIpTransportRemHostConnFails_Type())
aluIpTransportRemHostConnFails.setMaxAccess(_C)
if mibBuilder.loadTexts:aluIpTransportRemHostConnFails.setStatus(_A)
_AluIpTransportRemHostConnsCloFar_Type=Counter32
_AluIpTransportRemHostConnsCloFar_Object=MibTableColumn
aluIpTransportRemHostConnsCloFar=_AluIpTransportRemHostConnsCloFar_Object((1,3,6,1,4,1,6527,6,1,2,2,22,5,2,1,11),_AluIpTransportRemHostConnsCloFar_Type())
aluIpTransportRemHostConnsCloFar.setMaxAccess(_C)
if mibBuilder.loadTexts:aluIpTransportRemHostConnsCloFar.setStatus(_A)
_AluIpTransportRemHostInactTmouts_Type=Counter32
_AluIpTransportRemHostInactTmouts_Object=MibTableColumn
aluIpTransportRemHostInactTmouts=_AluIpTransportRemHostInactTmouts_Object((1,3,6,1,4,1,6527,6,1,2,2,22,5,2,1,12),_AluIpTransportRemHostInactTmouts_Type())
aluIpTransportRemHostInactTmouts.setMaxAccess(_C)
if mibBuilder.loadTexts:aluIpTransportRemHostInactTmouts.setStatus(_A)
_AluIpTransportURemHostStatsTable_Object=MibTable
aluIpTransportURemHostStatsTable=_AluIpTransportURemHostStatsTable_Object((1,3,6,1,4,1,6527,6,1,2,2,22,5,3))
if mibBuilder.loadTexts:aluIpTransportURemHostStatsTable.setStatus(_A)
_AluIpTransportURemHostStatsEntry_Object=MibTableRow
aluIpTransportURemHostStatsEntry=_AluIpTransportURemHostStatsEntry_Object((1,3,6,1,4,1,6527,6,1,2,2,22,5,3,1))
aluIpTransportURemHostStatsEntry.setIndexNames((0,_E,_F),(0,_B,_G),(0,_B,_h),(0,_B,_i),(0,_B,_j))
if mibBuilder.loadTexts:aluIpTransportURemHostStatsEntry.setStatus(_A)
_AluIpTransportURemHostIpAddrType_Type=InetAddressType
_AluIpTransportURemHostIpAddrType_Object=MibTableColumn
aluIpTransportURemHostIpAddrType=_AluIpTransportURemHostIpAddrType_Object((1,3,6,1,4,1,6527,6,1,2,2,22,5,3,1,1),_AluIpTransportURemHostIpAddrType_Type())
aluIpTransportURemHostIpAddrType.setMaxAccess(_J)
if mibBuilder.loadTexts:aluIpTransportURemHostIpAddrType.setStatus(_A)
class _AluIpTransportURemHostIpAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_AluIpTransportURemHostIpAddr_Type.__name__=_H
_AluIpTransportURemHostIpAddr_Object=MibTableColumn
aluIpTransportURemHostIpAddr=_AluIpTransportURemHostIpAddr_Object((1,3,6,1,4,1,6527,6,1,2,2,22,5,3,1,2),_AluIpTransportURemHostIpAddr_Type())
aluIpTransportURemHostIpAddr.setMaxAccess(_J)
if mibBuilder.loadTexts:aluIpTransportURemHostIpAddr.setStatus(_A)
class _AluIpTransportURemHostPortNum_Type(TTcpUdpPort):subtypeSpec=TTcpUdpPort.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AluIpTransportURemHostPortNum_Type.__name__=_I
_AluIpTransportURemHostPortNum_Object=MibTableColumn
aluIpTransportURemHostPortNum=_AluIpTransportURemHostPortNum_Object((1,3,6,1,4,1,6527,6,1,2,2,22,5,3,1,3),_AluIpTransportURemHostPortNum_Type())
aluIpTransportURemHostPortNum.setMaxAccess(_J)
if mibBuilder.loadTexts:aluIpTransportURemHostPortNum.setStatus(_A)
_AluIpTransportURemHostPktsSent_Type=Counter64
_AluIpTransportURemHostPktsSent_Object=MibTableColumn
aluIpTransportURemHostPktsSent=_AluIpTransportURemHostPktsSent_Object((1,3,6,1,4,1,6527,6,1,2,2,22,5,3,1,4),_AluIpTransportURemHostPktsSent_Type())
aluIpTransportURemHostPktsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:aluIpTransportURemHostPktsSent.setStatus(_A)
_AluIpTransportURemHostCharsSent_Type=Counter64
_AluIpTransportURemHostCharsSent_Object=MibTableColumn
aluIpTransportURemHostCharsSent=_AluIpTransportURemHostCharsSent_Object((1,3,6,1,4,1,6527,6,1,2,2,22,5,3,1,5),_AluIpTransportURemHostCharsSent_Type())
aluIpTransportURemHostCharsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:aluIpTransportURemHostCharsSent.setStatus(_A)
_AluIpTransportURemHostPktsDrop_Type=Counter64
_AluIpTransportURemHostPktsDrop_Object=MibTableColumn
aluIpTransportURemHostPktsDrop=_AluIpTransportURemHostPktsDrop_Object((1,3,6,1,4,1,6527,6,1,2,2,22,5,3,1,6),_AluIpTransportURemHostPktsDrop_Type())
aluIpTransportURemHostPktsDrop.setMaxAccess(_C)
if mibBuilder.loadTexts:aluIpTransportURemHostPktsDrop.setStatus(_A)
_AluIpTransportURemHostCharsDrop_Type=Counter64
_AluIpTransportURemHostCharsDrop_Object=MibTableColumn
aluIpTransportURemHostCharsDrop=_AluIpTransportURemHostCharsDrop_Object((1,3,6,1,4,1,6527,6,1,2,2,22,5,3,1,7),_AluIpTransportURemHostCharsDrop_Type())
aluIpTransportURemHostCharsDrop.setMaxAccess(_C)
if mibBuilder.loadTexts:aluIpTransportURemHostCharsDrop.setStatus(_A)
_AluIpTransportURemHostPktsRcvd_Type=Counter64
_AluIpTransportURemHostPktsRcvd_Object=MibTableColumn
aluIpTransportURemHostPktsRcvd=_AluIpTransportURemHostPktsRcvd_Object((1,3,6,1,4,1,6527,6,1,2,2,22,5,3,1,8),_AluIpTransportURemHostPktsRcvd_Type())
aluIpTransportURemHostPktsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:aluIpTransportURemHostPktsRcvd.setStatus(_A)
_AluIpTransportURemHostCharsRcvd_Type=Counter64
_AluIpTransportURemHostCharsRcvd_Object=MibTableColumn
aluIpTransportURemHostCharsRcvd=_AluIpTransportURemHostCharsRcvd_Object((1,3,6,1,4,1,6527,6,1,2,2,22,5,3,1,9),_AluIpTransportURemHostCharsRcvd_Type())
aluIpTransportURemHostCharsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:aluIpTransportURemHostCharsRcvd.setStatus(_A)
_AluIpTransportURemHostSessState_Type=AluIpTransportRemHostSessState
_AluIpTransportURemHostSessState_Object=MibTableColumn
aluIpTransportURemHostSessState=_AluIpTransportURemHostSessState_Object((1,3,6,1,4,1,6527,6,1,2,2,22,5,3,1,10),_AluIpTransportURemHostSessState_Type())
aluIpTransportURemHostSessState.setMaxAccess(_C)
if mibBuilder.loadTexts:aluIpTransportURemHostSessState.setStatus(_A)
_AluIpTransportURemHostSessUpTime_Type=Unsigned32
_AluIpTransportURemHostSessUpTime_Object=MibTableColumn
aluIpTransportURemHostSessUpTime=_AluIpTransportURemHostSessUpTime_Object((1,3,6,1,4,1,6527,6,1,2,2,22,5,3,1,11),_AluIpTransportURemHostSessUpTime_Type())
aluIpTransportURemHostSessUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:aluIpTransportURemHostSessUpTime.setStatus(_A)
if mibBuilder.loadTexts:aluIpTransportURemHostSessUpTime.setUnits(_L)
_AluIpTransportNotifyObjects_ObjectIdentity=ObjectIdentity
aluIpTransportNotifyObjects=_AluIpTransportNotifyObjects_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,2,22,6))
_AluIpTransportNotifyCustId_Type=TmnxCustId
_AluIpTransportNotifyCustId_Object=MibScalar
aluIpTransportNotifyCustId=_AluIpTransportNotifyCustId_Object((1,3,6,1,4,1,6527,6,1,2,2,22,6,1),_AluIpTransportNotifyCustId_Type())
aluIpTransportNotifyCustId.setMaxAccess(_R)
if mibBuilder.loadTexts:aluIpTransportNotifyCustId.setStatus(_A)
_AluIpTransportNotifySvcId_Type=TmnxServId
_AluIpTransportNotifySvcId_Object=MibScalar
aluIpTransportNotifySvcId=_AluIpTransportNotifySvcId_Object((1,3,6,1,4,1,6527,6,1,2,2,22,6,2),_AluIpTransportNotifySvcId_Type())
aluIpTransportNotifySvcId.setMaxAccess(_R)
if mibBuilder.loadTexts:aluIpTransportNotifySvcId.setStatus(_A)
_AluIpTransportNotifyPortId_Type=TmnxPortID
_AluIpTransportNotifyPortId_Object=MibScalar
aluIpTransportNotifyPortId=_AluIpTransportNotifyPortId_Object((1,3,6,1,4,1,6527,6,1,2,2,22,6,3),_AluIpTransportNotifyPortId_Type())
aluIpTransportNotifyPortId.setMaxAccess(_R)
if mibBuilder.loadTexts:aluIpTransportNotifyPortId.setStatus(_A)
_AluIpTransportNotifyPrefix_ObjectIdentity=ObjectIdentity
aluIpTransportNotifyPrefix=_AluIpTransportNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,3,18))
_AluIpTransportNotifications_ObjectIdentity=ObjectIdentity
aluIpTransportNotifications=_AluIpTransportNotifications_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,3,18,0))
svcBaseInfoEntry.registerAugmentions((_B,_k))
aluIpTransportSvcBaseExtEntry.setIndexNames(*svcBaseInfoEntry.getIndexNames())
aluIpTransportV8v0Group=ObjectGroup((1,3,6,1,4,1,6527,6,1,2,1,22,2,1,1))
aluIpTransportV8v0Group.setObjects(*((_B,_l),(_B,_m),(_B,_n),(_B,_S),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_T),(_B,_U),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_Q),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG)))
if mibBuilder.loadTexts:aluIpTransportV8v0Group.setStatus(_A)
aluIpTransportNotifyObjsGroup=ObjectGroup((1,3,6,1,4,1,6527,6,1,2,1,22,2,1,3))
aluIpTransportNotifyObjsGroup.setObjects(*((_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:aluIpTransportNotifyObjsGroup.setStatus(_A)
aluIpTransportStatsGroup=ObjectGroup((1,3,6,1,4,1,6527,6,1,2,1,22,2,1,4))
aluIpTransportStatsGroup.setObjects(*((_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_Ah),(_B,_Ai),(_B,_Aj),(_B,_Ak),(_B,_Al),(_B,_Am),(_B,_An),(_B,_Ao),(_B,_Ap),(_B,_Aq),(_B,_Ar),(_B,_As),(_B,_At),(_B,_Au),(_B,_Av),(_B,_Aw)))
if mibBuilder.loadTexts:aluIpTransportStatsGroup.setStatus(_A)
aluIpTransportStateChanged=NotificationType((1,3,6,1,4,1,6527,6,1,2,3,18,0,1))
aluIpTransportStateChanged.setObjects(*((_B,_V),(_B,_W),(_B,_X),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:aluIpTransportStateChanged.setStatus(_A)
aluIpTransportNotifyGroup=NotificationGroup((1,3,6,1,4,1,6527,6,1,2,1,22,2,1,2))
aluIpTransportNotifyGroup.setObjects((_B,_Ax))
if mibBuilder.loadTexts:aluIpTransportNotifyGroup.setStatus(_A)
aluIpTransport7705V8v0Compliance=ModuleCompliance((1,3,6,1,4,1,6527,6,1,2,1,22,1,1))
aluIpTransport7705V8v0Compliance.setObjects(*((_B,_Ay),(_B,_Az),(_B,_A_),(_B,_B0)))
if mibBuilder.loadTexts:aluIpTransport7705V8v0Compliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'AluIpTransportRemHostId':AluIpTransportRemHostId,'AluIpTransportRemHostSessState':AluIpTransportRemHostSessState,'aluIpTransportMIBModule':aluIpTransportMIBModule,'aluIpTransportConformance':aluIpTransportConformance,'aluIpTransportCompliances':aluIpTransportCompliances,'aluIpTransport7705V8v0Compliance':aluIpTransport7705V8v0Compliance,'aluIpTransportGroups':aluIpTransportGroups,'aluIpTransportV8v0Groups':aluIpTransportV8v0Groups,_Ay:aluIpTransportV8v0Group,_Az:aluIpTransportNotifyGroup,_A_:aluIpTransportNotifyObjsGroup,_B0:aluIpTransportStatsGroup,'aluIpTransportObjs':aluIpTransportObjs,'aluIpTransportConfigTimestamps':aluIpTransportConfigTimestamps,_l:aluIpTransportTableLastChanged,_A2:aluIpTransportRemHostTblLastChgd,'aluIpTransportConfigurations':aluIpTransportConfigurations,'aluIpTransportTable':aluIpTransportTable,'aluIpTransportEntry':aluIpTransportEntry,_G:aluIpTransportPortId,_m:aluIpTransportLastMgmtChange,_n:aluIpTransportRowStatus,_S:aluIpTransportAdminState,_o:aluIpTransportDescription,_p:aluIpTransportTcpConnMaxRetries,_q:aluIpTransportTcpConnRetryIntvl,_r:aluIpTransportTcpConnInactTimout,_s:aluIpTransportFilterUnknownHost,_t:aluIpTransportDscpName,_u:aluIpTransportFcName,_v:aluIpTransportProfile,_w:aluIpTransportLocHostIpAddrType,_x:aluIpTransportLocHostIpAddr,_y:aluIpTransportLocHostPortNum,_z:aluIpTransportLocHostIpProtocol,_A0:aluIpTransportNumRemHosts,_T:aluIpTransportOperState,_U:aluIpTransportOperFlags,_A1:aluIpTransportLastOperChange,'aluIpTransportRemHostTable':aluIpTransportRemHostTable,'aluIpTransportRemHostEntry':aluIpTransportRemHostEntry,_P:aluIpTransportRemHostId,_A3:aluIpTransportRemHostLastChanged,_A4:aluIpTransportRemHostRowStatus,_Q:aluIpTransportRemHostName,_A5:aluIpTransportRemHostDescription,_A6:aluIpTransportRemHostIpAddrType,_A7:aluIpTransportRemHostIpAddr,_A8:aluIpTransportRemHostPortNum,_AB:aluIpTransportRemHostSessState,_AC:aluIpTransportRemHostSessUpTime,_AD:aluIpTransportRemHostLastConnect,_AE:aluIpTransportRemHostCheckTcp,_AF:aluIpTransportRemHostCheckTcpRes,_AG:aluIpTransportRemHostCheckTcpInf,'aluIpTransportSvcBaseExtTable':aluIpTransportSvcBaseExtTable,_k:aluIpTransportSvcBaseExtEntry,_A9:aluIpTransportSvcBaseExtNumIpts,'aluIpTransportNameObjects':aluIpTransportNameObjects,'aluIpTransportRemHostNameTable':aluIpTransportRemHostNameTable,'aluIpTransportRemHostNameEntry':aluIpTransportRemHostNameEntry,_AA:aluIpTransportRemHostNameId,'aluIpTransportStatus':aluIpTransportStatus,'aluIpTransportStatsObjects':aluIpTransportStatsObjects,'aluIpTransportStatsTable':aluIpTransportStatsTable,'aluIpTransportStatsEntry':aluIpTransportStatsEntry,_AH:aluIpTransportKnwRemPktsSent,_AI:aluIpTransportKnwRemCharsSent,_AJ:aluIpTransportKnwRemPktsRcvd,_AK:aluIpTransportKnwRemCharsRcvd,_AL:aluIpTransportKnwRemConnsTo,_AM:aluIpTransportKnwRemConnsFrom,_AN:aluIpTransportKnwRemConnRetries,_AO:aluIpTransportKnwRemConnFails,_AP:aluIpTransportKnwRemCurrConns,_AQ:aluIpTransportUnkRemPktsSent,_AR:aluIpTransportUnkRemCharsSent,_AS:aluIpTransportUnkRemPktsRcvd,_AT:aluIpTransportUnkRemCharsRcvd,_AU:aluIpTransportUnkRemSuccConnsFrm,_AV:aluIpTransportUnkRemRejectsFiltr,_AW:aluIpTransportUnkRemRejectsResrc,_AX:aluIpTransportUnkRemInactTimouts,_AY:aluIpTransportUnkRemLastIpAddrTy,_AZ:aluIpTransportUnkRemLastIpAddr,_Aa:aluIpTransportUnkRemLastPortNum,_Ab:aluIpTransportUnkRemCurrConns,_Ac:aluIpTransportPktsDropNoRemHost,'aluIpTransportRemHostStatsTable':aluIpTransportRemHostStatsTable,'aluIpTransportRemHostStatsEntry':aluIpTransportRemHostStatsEntry,_Ad:aluIpTransportRemHostPktsSent,_Ae:aluIpTransportRemHostCharsSent,_Af:aluIpTransportRemHostPktsDrop,_Ag:aluIpTransportRemHostCharsDrop,_Ah:aluIpTransportRemHostPktsRcvd,_Ai:aluIpTransportRemHostCharsRcvd,_Aj:aluIpTransportRemHostConnsTo,_Ak:aluIpTransportRemHostConnsFrom,_Al:aluIpTransportRemHostConnRetries,_Am:aluIpTransportRemHostConnFails,_An:aluIpTransportRemHostConnsCloFar,_Ao:aluIpTransportRemHostInactTmouts,'aluIpTransportURemHostStatsTable':aluIpTransportURemHostStatsTable,'aluIpTransportURemHostStatsEntry':aluIpTransportURemHostStatsEntry,_h:aluIpTransportURemHostIpAddrType,_i:aluIpTransportURemHostIpAddr,_j:aluIpTransportURemHostPortNum,_Ap:aluIpTransportURemHostPktsSent,_Aq:aluIpTransportURemHostCharsSent,_Ar:aluIpTransportURemHostPktsDrop,_As:aluIpTransportURemHostCharsDrop,_At:aluIpTransportURemHostPktsRcvd,_Au:aluIpTransportURemHostCharsRcvd,_Av:aluIpTransportURemHostSessState,_Aw:aluIpTransportURemHostSessUpTime,'aluIpTransportNotifyObjects':aluIpTransportNotifyObjects,_V:aluIpTransportNotifyCustId,_W:aluIpTransportNotifySvcId,_X:aluIpTransportNotifyPortId,'aluIpTransportNotifyPrefix':aluIpTransportNotifyPrefix,'aluIpTransportNotifications':aluIpTransportNotifications,_Ax:aluIpTransportStateChanged})