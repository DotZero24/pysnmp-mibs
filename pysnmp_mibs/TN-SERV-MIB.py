_AC='tnSvcTlsBackboneInfoEntry'
_AB='tnTlsMFibVcId'
_AA='tnTlsMFibSdpId'
_A9='tnTlsMFibEncapValue'
_A8='tnTlsMFibPortId'
_A7='tnTlsMFibLocale'
_A6='tnTlsMFibSrcInetAddr'
_A5='tnTlsMFibSrcInetAddrType'
_A4='tnTlsMFibGrpInetAddr'
_A3='tnTlsMFibGrpInetAddrType'
_A2='tnTlsMFibGrpMacAddr'
_A1='tnTlsMFibEntryType'
_A0='tnSvcEndPointName'
_z='tnTlsShgName'
_y='tnTlsFdbMacAddr'
_x='deci-seconds'
_w='tnCustId'
_v='undefined'
_u='default'
_t='radius'
_s='notApplicable'
_r='cesopsnCas'
_q='cesopsn'
_p='satopT3'
_o='satopE3'
_n='satopT1'
_m='satopE1'
_l='frDlci'
_k='atmVpc'
_j='atmVcc'
_i='atmCell'
_h='atmSdu'
_g='mirror'
_f='TmnxVRtrIDOrZero'
_e='TmnxServId'
_d='TmnxActionType'
_c='TNamedItem'
_b='SdpBindId'
_a='MacAddress'
_Z='InetAddressType'
_Y='OctetString'
_X='down'
_W='stp'
_V='ServiceAdminStatus'
_U='DisplayString'
_T='sap'
_S='disabled'
_R='InetAddress'
_Q='seconds'
_P='TNamedItemOrEmpty'
_O='none'
_N='tnSvcId'
_M='ServObjDesc'
_L='tnSysSwitchId'
_K='TROPIC-SYSTEM-MIB'
_J='TmnxEnabledDisabled'
_I='Unsigned32'
_H='not-accessible'
_G='TruthValue'
_F='TN-SERV-MIB'
_E='Integer32'
_D='read-write'
_C='read-create'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_Y,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_R,_Z)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_U,_a,'PhysAddress','RowStatus','TextualConvention','TimeStamp',_G)
SdpBindId,ServObjDesc,ServiceAdminStatus,ServiceOperStatus,TNamedItem,TNamedItemOrEmpty,TmnxActionType,TmnxCustId,TmnxEnabledDisabled,TmnxEncapVal,TmnxPortID,TmnxServId,TmnxVRtrIDOrZero=mibBuilder.importSymbols('TN-TC-MIB',_b,_M,_V,'ServiceOperStatus',_c,_P,_d,'TmnxCustId',_J,'TmnxEncapVal','TmnxPortID',_e,_f)
tnSRMIBModules,tnSRNotifyPrefix,tnSRObjs=mibBuilder.importSymbols('TROPIC-GLOBAL-REG','tnSRMIBModules','tnSRNotifyPrefix','tnSRObjs')
tnSysSwitchId,=mibBuilder.importSymbols(_K,_L)
tnServicesMIBModule=ModuleIdentity((1,3,6,1,4,1,7483,5,1,3,4))
if mibBuilder.loadTexts:tnServicesMIBModule.setRevisions(('2019-09-13 00:00','2018-09-21 00:00','2018-07-20 00:00','2017-07-07 00:00','2016-03-15 00:00','2015-11-02 00:00','2012-12-13 00:00','2012-12-05 00:00','2012-09-01 00:00','2009-02-28 00:00','2008-07-01 00:00','2008-01-01 00:00','2007-01-01 00:00','2006-02-28 00:00','2005-08-31 00:00','2005-01-24 00:00','2004-01-15 00:00','2003-08-15 00:00','2003-01-20 00:00','2000-08-14 00:00'))
class ServObjName(DisplayString):status=_A;subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
class ServObjLongDesc(DisplayString):status=_A;subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,160))
class ServType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,16)));namedValues=NamedValues(*(('unknown',0),('epipe',1),('p3pipe',2),('tls',3),('vprn',4),('ies',5),(_g,6),('apipe',7),('fpipe',8),('ipipe',9),('cpipe',10),('etree',16)))
class VpnId(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,2147483647))
class SdpId(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,17407))
class PWTemplateId(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,2147483647))
class TlsBpduTranslation(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('auto',1),(_S,2),('pvst',3),(_W,4),('pvst-rw',5),('auto-rw',6)))
class TlsLimitMacMoveLevel(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('primary',1),('secondary',2),('tertiary',3)))
class TlsLimitMacMove(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('blockable',1),('nonBlockable',2)))
class SdpBindVcType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17)));namedValues=NamedValues(*(('undef',1),('ether',2),('vlan',4),(_g,5),(_h,6),(_i,7),(_j,8),(_k,9),(_l,10),('ipipe',11),(_m,12),(_n,13),(_o,14),(_p,15),(_q,16),(_r,17)))
class StpExceptionCondition(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_O,1),('oneWayCommuniation',2),('downstreamLoopDetected',3)))
class LspIdList(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,68))
class BridgeId(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
class TSapIngQueueId(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
class TStpPortState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_S,1),('blocking',2),('listening',3),('learning',4),('forwarding',5),('broken',6),('discarding',7)))
class StpPortRole(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('master',0),('root',1),('designated',2),('alternate',3),('backup',4),(_S,5)))
class StpProtocol(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_s,0),(_W,1),('rstp',2),('mstp',3)))
class MfibLocation(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),('sdp',2)))
class MfibGrpSrcFwdOrBlk(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('forward',1),('block',2)))
class MvplsPruneState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_s,1),('notPruned',2),('pruned',3)))
class MstiInstanceId(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
class MstiInstanceIdOrZero(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
class DhcpLseStateInfoOrigin(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_O,0),('dhcp',1),(_t,2),('retailerRadius',3),('retailerDhcp',4),(_u,5)))
class IAIDType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_v,0),('temporary',1),('non-temporary',2),('prefix',3)))
class TdmOptionsSigPkts(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('noSigPkts',0),('dataPkts',1),('sigPkts',2),('dataAndSigPkts',3)))
class TdmOptionsCasTrunkFraming(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('noCas',0),('e1Trunk',1),('t1EsfTrunk',2),('t1SfTrunk',3)))
class SdpBindBandwidth(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000000))
class L2ptProtocols(TextualConvention,Bits):status=_A;namedValues=NamedValues(*((_W,0),('cdp',1),('vtp',2),('dtp',3),('pagp',4),('udld',5)))
class SvcISID(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,16777215))
class L2RouteOrigin(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('manual',1),('bgp-l2vpn',2),(_t,3)))
class ConfigStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('created',1),('modified',2),('deleted',3)))
class ServAccessLocation(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),('spoke',2)))
class ServShcvOperState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_S,1),(_v,2),(_X,3),('up',4)))
_TnServObjs_ObjectIdentity=ObjectIdentity
tnServObjs=_TnServObjs_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,4))
_TnCustObjs_ObjectIdentity=ObjectIdentity
tnCustObjs=_TnCustObjs_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,4,1))
_TnCustNumEntries_Type=Integer32
_TnCustNumEntries_Object=MibScalar
tnCustNumEntries=_TnCustNumEntries_Object((1,3,6,1,4,1,7483,6,1,2,4,1,1),_TnCustNumEntries_Type())
tnCustNumEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:tnCustNumEntries.setStatus(_A)
_TnCustNextFreeId_Type=TmnxCustId
_TnCustNextFreeId_Object=MibScalar
tnCustNextFreeId=_TnCustNextFreeId_Object((1,3,6,1,4,1,7483,6,1,2,4,1,2),_TnCustNextFreeId_Type())
tnCustNextFreeId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnCustNextFreeId.setStatus(_A)
_TnCustInfoTable_Object=MibTable
tnCustInfoTable=_TnCustInfoTable_Object((1,3,6,1,4,1,7483,6,1,2,4,1,3))
if mibBuilder.loadTexts:tnCustInfoTable.setStatus(_A)
_TnCustInfoEntry_Object=MibTableRow
tnCustInfoEntry=_TnCustInfoEntry_Object((1,3,6,1,4,1,7483,6,1,2,4,1,3,1))
tnCustInfoEntry.setIndexNames((0,_K,_L),(0,_F,_w))
if mibBuilder.loadTexts:tnCustInfoEntry.setStatus(_A)
_TnCustId_Type=TmnxCustId
_TnCustId_Object=MibTableColumn
tnCustId=_TnCustId_Object((1,3,6,1,4,1,7483,6,1,2,4,1,3,1,1),_TnCustId_Type())
tnCustId.setMaxAccess(_H)
if mibBuilder.loadTexts:tnCustId.setStatus(_A)
_TnCustRowStatus_Type=RowStatus
_TnCustRowStatus_Object=MibTableColumn
tnCustRowStatus=_TnCustRowStatus_Object((1,3,6,1,4,1,7483,6,1,2,4,1,3,1,2),_TnCustRowStatus_Type())
tnCustRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tnCustRowStatus.setStatus(_A)
class _TnCustDescription_Type(ServObjDesc):defaultValue=OctetString('')
_TnCustDescription_Type.__name__=_M
_TnCustDescription_Object=MibTableColumn
tnCustDescription=_TnCustDescription_Object((1,3,6,1,4,1,7483,6,1,2,4,1,3,1,3),_TnCustDescription_Type())
tnCustDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:tnCustDescription.setStatus(_A)
class _TnCustContact_Type(ServObjDesc):defaultValue=OctetString('')
_TnCustContact_Type.__name__=_M
_TnCustContact_Object=MibTableColumn
tnCustContact=_TnCustContact_Object((1,3,6,1,4,1,7483,6,1,2,4,1,3,1,4),_TnCustContact_Type())
tnCustContact.setMaxAccess(_C)
if mibBuilder.loadTexts:tnCustContact.setStatus(_A)
class _TnCustPhone_Type(ServObjDesc):defaultValue=OctetString('')
_TnCustPhone_Type.__name__=_M
_TnCustPhone_Object=MibTableColumn
tnCustPhone=_TnCustPhone_Object((1,3,6,1,4,1,7483,6,1,2,4,1,3,1,5),_TnCustPhone_Type())
tnCustPhone.setMaxAccess(_C)
if mibBuilder.loadTexts:tnCustPhone.setStatus(_A)
_TnCustLastMgmtChange_Type=TimeStamp
_TnCustLastMgmtChange_Object=MibTableColumn
tnCustLastMgmtChange=_TnCustLastMgmtChange_Object((1,3,6,1,4,1,7483,6,1,2,4,1,3,1,6),_TnCustLastMgmtChange_Type())
tnCustLastMgmtChange.setMaxAccess(_B)
if mibBuilder.loadTexts:tnCustLastMgmtChange.setStatus(_A)
_TnSvcObjs_ObjectIdentity=ObjectIdentity
tnSvcObjs=_TnSvcObjs_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,4,2))
_TnSvcNumEntries_Type=Integer32
_TnSvcNumEntries_Object=MibScalar
tnSvcNumEntries=_TnSvcNumEntries_Object((1,3,6,1,4,1,7483,6,1,2,4,2,1),_TnSvcNumEntries_Type())
tnSvcNumEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcNumEntries.setStatus(_A)
_TnSvcBaseInfoTable_Object=MibTable
tnSvcBaseInfoTable=_TnSvcBaseInfoTable_Object((1,3,6,1,4,1,7483,6,1,2,4,2,2))
if mibBuilder.loadTexts:tnSvcBaseInfoTable.setStatus(_A)
_TnSvcBaseInfoEntry_Object=MibTableRow
tnSvcBaseInfoEntry=_TnSvcBaseInfoEntry_Object((1,3,6,1,4,1,7483,6,1,2,4,2,2,1))
tnSvcBaseInfoEntry.setIndexNames((0,_K,_L),(0,_F,_N))
if mibBuilder.loadTexts:tnSvcBaseInfoEntry.setStatus(_A)
_TnSvcId_Type=TmnxServId
_TnSvcId_Object=MibTableColumn
tnSvcId=_TnSvcId_Object((1,3,6,1,4,1,7483,6,1,2,4,2,2,1,1),_TnSvcId_Type())
tnSvcId.setMaxAccess(_H)
if mibBuilder.loadTexts:tnSvcId.setStatus(_A)
_TnSvcRowStatus_Type=RowStatus
_TnSvcRowStatus_Object=MibTableColumn
tnSvcRowStatus=_TnSvcRowStatus_Object((1,3,6,1,4,1,7483,6,1,2,4,2,2,1,2),_TnSvcRowStatus_Type())
tnSvcRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSvcRowStatus.setStatus(_A)
_TnSvcType_Type=ServType
_TnSvcType_Object=MibTableColumn
tnSvcType=_TnSvcType_Object((1,3,6,1,4,1,7483,6,1,2,4,2,2,1,3),_TnSvcType_Type())
tnSvcType.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSvcType.setStatus(_A)
_TnSvcCustId_Type=TmnxCustId
_TnSvcCustId_Object=MibTableColumn
tnSvcCustId=_TnSvcCustId_Object((1,3,6,1,4,1,7483,6,1,2,4,2,2,1,4),_TnSvcCustId_Type())
tnSvcCustId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSvcCustId.setStatus(_A)
_TnSvcIpRouting_Type=TmnxEnabledDisabled
_TnSvcIpRouting_Object=MibTableColumn
tnSvcIpRouting=_TnSvcIpRouting_Object((1,3,6,1,4,1,7483,6,1,2,4,2,2,1,5),_TnSvcIpRouting_Type())
tnSvcIpRouting.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSvcIpRouting.setStatus(_A)
class _TnSvcDescription_Type(ServObjDesc):defaultValue=OctetString('')
_TnSvcDescription_Type.__name__=_M
_TnSvcDescription_Object=MibTableColumn
tnSvcDescription=_TnSvcDescription_Object((1,3,6,1,4,1,7483,6,1,2,4,2,2,1,6),_TnSvcDescription_Type())
tnSvcDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSvcDescription.setStatus(_A)
class _TnSvcMtu_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9194))
_TnSvcMtu_Type.__name__=_E
_TnSvcMtu_Object=MibTableColumn
tnSvcMtu=_TnSvcMtu_Object((1,3,6,1,4,1,7483,6,1,2,4,2,2,1,7),_TnSvcMtu_Type())
tnSvcMtu.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSvcMtu.setStatus(_A)
class _TnSvcAdminStatus_Type(ServiceAdminStatus):defaultValue=2
_TnSvcAdminStatus_Type.__name__=_V
_TnSvcAdminStatus_Object=MibTableColumn
tnSvcAdminStatus=_TnSvcAdminStatus_Object((1,3,6,1,4,1,7483,6,1,2,4,2,2,1,8),_TnSvcAdminStatus_Type())
tnSvcAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSvcAdminStatus.setStatus(_A)
_TnSvcOperStatus_Type=ServiceOperStatus
_TnSvcOperStatus_Object=MibTableColumn
tnSvcOperStatus=_TnSvcOperStatus_Object((1,3,6,1,4,1,7483,6,1,2,4,2,2,1,9),_TnSvcOperStatus_Type())
tnSvcOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcOperStatus.setStatus(_A)
_TnSvcNumSaps_Type=Integer32
_TnSvcNumSaps_Object=MibTableColumn
tnSvcNumSaps=_TnSvcNumSaps_Object((1,3,6,1,4,1,7483,6,1,2,4,2,2,1,10),_TnSvcNumSaps_Type())
tnSvcNumSaps.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcNumSaps.setStatus(_A)
_TnSvcNumSdps_Type=Integer32
_TnSvcNumSdps_Object=MibTableColumn
tnSvcNumSdps=_TnSvcNumSdps_Object((1,3,6,1,4,1,7483,6,1,2,4,2,2,1,11),_TnSvcNumSdps_Type())
tnSvcNumSdps.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcNumSdps.setStatus(_A)
_TnSvcLastMgmtChange_Type=TimeStamp
_TnSvcLastMgmtChange_Object=MibTableColumn
tnSvcLastMgmtChange=_TnSvcLastMgmtChange_Object((1,3,6,1,4,1,7483,6,1,2,4,2,2,1,12),_TnSvcLastMgmtChange_Type())
tnSvcLastMgmtChange.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcLastMgmtChange.setStatus(_A)
_TnSvcDefMeshVcId_Type=Unsigned32
_TnSvcDefMeshVcId_Object=MibTableColumn
tnSvcDefMeshVcId=_TnSvcDefMeshVcId_Object((1,3,6,1,4,1,7483,6,1,2,4,2,2,1,13),_TnSvcDefMeshVcId_Type())
tnSvcDefMeshVcId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSvcDefMeshVcId.setStatus(_A)
class _TnSvcVpnId_Type(VpnId):defaultValue=0
_TnSvcVpnId_Type.__name__='VpnId'
_TnSvcVpnId_Object=MibTableColumn
tnSvcVpnId=_TnSvcVpnId_Object((1,3,6,1,4,1,7483,6,1,2,4,2,2,1,14),_TnSvcVpnId_Type())
tnSvcVpnId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSvcVpnId.setStatus(_A)
class _TnSvcVRouterId_Type(TmnxVRtrIDOrZero):defaultValue=0
_TnSvcVRouterId_Type.__name__=_f
_TnSvcVRouterId_Object=MibTableColumn
tnSvcVRouterId=_TnSvcVRouterId_Object((1,3,6,1,4,1,7483,6,1,2,4,2,2,1,15),_TnSvcVRouterId_Type())
tnSvcVRouterId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSvcVRouterId.setStatus(_A)
class _TnSvcAutoBind_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_O,1),('gre',2),('ldp',3),('rsvp-te',4),('mpls',5)))
_TnSvcAutoBind_Type.__name__=_E
_TnSvcAutoBind_Object=MibTableColumn
tnSvcAutoBind=_TnSvcAutoBind_Object((1,3,6,1,4,1,7483,6,1,2,4,2,2,1,16),_TnSvcAutoBind_Type())
tnSvcAutoBind.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSvcAutoBind.setStatus(_A)
_TnSvcLastStatusChange_Type=TimeStamp
_TnSvcLastStatusChange_Object=MibTableColumn
tnSvcLastStatusChange=_TnSvcLastStatusChange_Object((1,3,6,1,4,1,7483,6,1,2,4,2,2,1,17),_TnSvcLastStatusChange_Type())
tnSvcLastStatusChange.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcLastStatusChange.setStatus(_A)
class _TnSvcVllType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,6,7,8,9,10,12,13,14,15,16,17)));namedValues=NamedValues(*(('undef',1),(_h,6),(_i,7),(_j,8),(_k,9),(_l,10),(_m,12),(_n,13),(_o,14),(_p,15),(_q,16),(_r,17)))
_TnSvcVllType_Type.__name__=_E
_TnSvcVllType_Object=MibTableColumn
tnSvcVllType=_TnSvcVllType_Object((1,3,6,1,4,1,7483,6,1,2,4,2,2,1,18),_TnSvcVllType_Type())
tnSvcVllType.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSvcVllType.setStatus(_A)
class _TnSvcMgmtVpls_Type(TruthValue):defaultValue=2
_TnSvcMgmtVpls_Type.__name__=_G
_TnSvcMgmtVpls_Object=MibTableColumn
tnSvcMgmtVpls=_TnSvcMgmtVpls_Object((1,3,6,1,4,1,7483,6,1,2,4,2,2,1,19),_TnSvcMgmtVpls_Type())
tnSvcMgmtVpls.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSvcMgmtVpls.setStatus(_A)
class _TnSvcRadiusDiscovery_Type(TruthValue):defaultValue=2
_TnSvcRadiusDiscovery_Type.__name__=_G
_TnSvcRadiusDiscovery_Object=MibTableColumn
tnSvcRadiusDiscovery=_TnSvcRadiusDiscovery_Object((1,3,6,1,4,1,7483,6,1,2,4,2,2,1,20),_TnSvcRadiusDiscovery_Type())
tnSvcRadiusDiscovery.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSvcRadiusDiscovery.setStatus(_A)
class _TnSvcRadiusUserNameType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_O,0),('vpn-id',1),('router-distinguisher',2)))
_TnSvcRadiusUserNameType_Type.__name__=_E
_TnSvcRadiusUserNameType_Object=MibTableColumn
tnSvcRadiusUserNameType=_TnSvcRadiusUserNameType_Object((1,3,6,1,4,1,7483,6,1,2,4,2,2,1,21),_TnSvcRadiusUserNameType_Type())
tnSvcRadiusUserNameType.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSvcRadiusUserNameType.setStatus(_A)
class _TnSvcRadiusUserName_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_TnSvcRadiusUserName_Type.__name__=_U
_TnSvcRadiusUserName_Object=MibTableColumn
tnSvcRadiusUserName=_TnSvcRadiusUserName_Object((1,3,6,1,4,1,7483,6,1,2,4,2,2,1,22),_TnSvcRadiusUserName_Type())
tnSvcRadiusUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSvcRadiusUserName.setStatus(_A)
class _TnSvcVcSwitching_Type(TruthValue):defaultValue=2
_TnSvcVcSwitching_Type.__name__=_G
_TnSvcVcSwitching_Object=MibTableColumn
tnSvcVcSwitching=_TnSvcVcSwitching_Object((1,3,6,1,4,1,7483,6,1,2,4,2,2,1,23),_TnSvcVcSwitching_Type())
tnSvcVcSwitching.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSvcVcSwitching.setStatus(_A)
class _TnSvcRadiusPEDiscPolicy_Type(TNamedItemOrEmpty):defaultValue=OctetString('')
_TnSvcRadiusPEDiscPolicy_Type.__name__=_P
_TnSvcRadiusPEDiscPolicy_Object=MibTableColumn
tnSvcRadiusPEDiscPolicy=_TnSvcRadiusPEDiscPolicy_Object((1,3,6,1,4,1,7483,6,1,2,4,2,2,1,24),_TnSvcRadiusPEDiscPolicy_Type())
tnSvcRadiusPEDiscPolicy.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSvcRadiusPEDiscPolicy.setStatus(_A)
class _TnSvcRadiusDiscoveryShutdown_Type(ServiceAdminStatus):defaultValue=2
_TnSvcRadiusDiscoveryShutdown_Type.__name__=_V
_TnSvcRadiusDiscoveryShutdown_Object=MibTableColumn
tnSvcRadiusDiscoveryShutdown=_TnSvcRadiusDiscoveryShutdown_Object((1,3,6,1,4,1,7483,6,1,2,4,2,2,1,25),_TnSvcRadiusDiscoveryShutdown_Type())
tnSvcRadiusDiscoveryShutdown.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSvcRadiusDiscoveryShutdown.setStatus(_A)
class _TnSvcVplsType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_O,1),('bVpls',2),('iVpls',3)))
_TnSvcVplsType_Type.__name__=_E
_TnSvcVplsType_Object=MibTableColumn
tnSvcVplsType=_TnSvcVplsType_Object((1,3,6,1,4,1,7483,6,1,2,4,2,2,1,26),_TnSvcVplsType_Type())
tnSvcVplsType.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSvcVplsType.setStatus(_A)
_TnSvcNumMcStandbySaps_Type=Integer32
_TnSvcNumMcStandbySaps_Object=MibTableColumn
tnSvcNumMcStandbySaps=_TnSvcNumMcStandbySaps_Object((1,3,6,1,4,1,7483,6,1,2,4,2,2,1,27),_TnSvcNumMcStandbySaps_Type())
tnSvcNumMcStandbySaps.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcNumMcStandbySaps.setStatus(_A)
class _TnSvcName_Type(TNamedItemOrEmpty):defaultHexValue=''
_TnSvcName_Type.__name__=_P
_TnSvcName_Object=MibTableColumn
tnSvcName=_TnSvcName_Object((1,3,6,1,4,1,7483,6,1,2,4,2,2,1,28),_TnSvcName_Type())
tnSvcName.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSvcName.setStatus(_A)
class _TnsvcEpipeAllowIpIfBinding_Type(TruthValue):defaultValue=2
_TnsvcEpipeAllowIpIfBinding_Type.__name__=_G
_TnsvcEpipeAllowIpIfBinding_Object=MibTableColumn
tnsvcEpipeAllowIpIfBinding=_TnsvcEpipeAllowIpIfBinding_Object((1,3,6,1,4,1,7483,6,1,2,4,2,2,1,29),_TnsvcEpipeAllowIpIfBinding_Type())
tnsvcEpipeAllowIpIfBinding.setMaxAccess(_D)
if mibBuilder.loadTexts:tnsvcEpipeAllowIpIfBinding.setStatus(_A)
class _TnSvcAlmProfName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,40))
_TnSvcAlmProfName_Type.__name__=_Y
_TnSvcAlmProfName_Object=MibTableColumn
tnSvcAlmProfName=_TnSvcAlmProfName_Object((1,3,6,1,4,1,7483,6,1,2,4,2,2,1,30),_TnSvcAlmProfName_Type())
tnSvcAlmProfName.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSvcAlmProfName.setStatus(_A)
_TnSvcTlsInfoTable_Object=MibTable
tnSvcTlsInfoTable=_TnSvcTlsInfoTable_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3))
if mibBuilder.loadTexts:tnSvcTlsInfoTable.setStatus(_A)
_TnSvcTlsInfoEntry_Object=MibTableRow
tnSvcTlsInfoEntry=_TnSvcTlsInfoEntry_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1))
tnSvcTlsInfoEntry.setIndexNames((0,_K,_L),(0,_F,_N))
if mibBuilder.loadTexts:tnSvcTlsInfoEntry.setStatus(_A)
class _TnSvcTlsMacLearning_Type(TmnxEnabledDisabled):defaultValue=1
_TnSvcTlsMacLearning_Type.__name__=_J
_TnSvcTlsMacLearning_Object=MibTableColumn
tnSvcTlsMacLearning=_TnSvcTlsMacLearning_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,1),_TnSvcTlsMacLearning_Type())
tnSvcTlsMacLearning.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSvcTlsMacLearning.setStatus(_A)
class _TnSvcTlsDiscardUnknownDest_Type(TmnxEnabledDisabled):defaultValue=2
_TnSvcTlsDiscardUnknownDest_Type.__name__=_J
_TnSvcTlsDiscardUnknownDest_Object=MibTableColumn
tnSvcTlsDiscardUnknownDest=_TnSvcTlsDiscardUnknownDest_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,2),_TnSvcTlsDiscardUnknownDest_Type())
tnSvcTlsDiscardUnknownDest.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSvcTlsDiscardUnknownDest.setStatus(_A)
class _TnSvcTlsFdbTableSize_Type(Integer32):defaultValue=250;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,511999))
_TnSvcTlsFdbTableSize_Type.__name__=_E
_TnSvcTlsFdbTableSize_Object=MibTableColumn
tnSvcTlsFdbTableSize=_TnSvcTlsFdbTableSize_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,3),_TnSvcTlsFdbTableSize_Type())
tnSvcTlsFdbTableSize.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSvcTlsFdbTableSize.setStatus(_A)
_TnSvcTlsFdbNumEntries_Type=Integer32
_TnSvcTlsFdbNumEntries_Object=MibTableColumn
tnSvcTlsFdbNumEntries=_TnSvcTlsFdbNumEntries_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,4),_TnSvcTlsFdbNumEntries_Type())
tnSvcTlsFdbNumEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcTlsFdbNumEntries.setStatus(_A)
_TnSvcTlsFdbNumStaticEntries_Type=Integer32
_TnSvcTlsFdbNumStaticEntries_Object=MibTableColumn
tnSvcTlsFdbNumStaticEntries=_TnSvcTlsFdbNumStaticEntries_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,5),_TnSvcTlsFdbNumStaticEntries_Type())
tnSvcTlsFdbNumStaticEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcTlsFdbNumStaticEntries.setStatus(_A)
class _TnSvcTlsFdbLocalAgeTime_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,86400))
_TnSvcTlsFdbLocalAgeTime_Type.__name__=_E
_TnSvcTlsFdbLocalAgeTime_Object=MibTableColumn
tnSvcTlsFdbLocalAgeTime=_TnSvcTlsFdbLocalAgeTime_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,6),_TnSvcTlsFdbLocalAgeTime_Type())
tnSvcTlsFdbLocalAgeTime.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSvcTlsFdbLocalAgeTime.setStatus(_A)
class _TnSvcTlsFdbRemoteAgeTime_Type(Integer32):defaultValue=900;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,86400))
_TnSvcTlsFdbRemoteAgeTime_Type.__name__=_E
_TnSvcTlsFdbRemoteAgeTime_Object=MibTableColumn
tnSvcTlsFdbRemoteAgeTime=_TnSvcTlsFdbRemoteAgeTime_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,7),_TnSvcTlsFdbRemoteAgeTime_Type())
tnSvcTlsFdbRemoteAgeTime.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSvcTlsFdbRemoteAgeTime.setStatus(_A)
class _TnSvcTlsStpAdminStatus_Type(TmnxEnabledDisabled):defaultValue=2
_TnSvcTlsStpAdminStatus_Type.__name__=_J
_TnSvcTlsStpAdminStatus_Object=MibTableColumn
tnSvcTlsStpAdminStatus=_TnSvcTlsStpAdminStatus_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,8),_TnSvcTlsStpAdminStatus_Type())
tnSvcTlsStpAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSvcTlsStpAdminStatus.setStatus(_A)
class _TnSvcTlsStpPriority_Type(Integer32):defaultValue=32768;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_TnSvcTlsStpPriority_Type.__name__=_E
_TnSvcTlsStpPriority_Object=MibTableColumn
tnSvcTlsStpPriority=_TnSvcTlsStpPriority_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,9),_TnSvcTlsStpPriority_Type())
tnSvcTlsStpPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSvcTlsStpPriority.setStatus(_A)
_TnSvcTlsStpBridgeAddress_Type=MacAddress
_TnSvcTlsStpBridgeAddress_Object=MibTableColumn
tnSvcTlsStpBridgeAddress=_TnSvcTlsStpBridgeAddress_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,10),_TnSvcTlsStpBridgeAddress_Type())
tnSvcTlsStpBridgeAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcTlsStpBridgeAddress.setStatus(_A)
_TnSvcTlsStpTimeSinceTopologyChange_Type=TimeTicks
_TnSvcTlsStpTimeSinceTopologyChange_Object=MibTableColumn
tnSvcTlsStpTimeSinceTopologyChange=_TnSvcTlsStpTimeSinceTopologyChange_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,11),_TnSvcTlsStpTimeSinceTopologyChange_Type())
tnSvcTlsStpTimeSinceTopologyChange.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcTlsStpTimeSinceTopologyChange.setStatus(_A)
_TnSvcTlsStpTopologyChanges_Type=Integer32
_TnSvcTlsStpTopologyChanges_Object=MibTableColumn
tnSvcTlsStpTopologyChanges=_TnSvcTlsStpTopologyChanges_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,12),_TnSvcTlsStpTopologyChanges_Type())
tnSvcTlsStpTopologyChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcTlsStpTopologyChanges.setStatus(_A)
_TnSvcTlsStpDesignatedRoot_Type=BridgeId
_TnSvcTlsStpDesignatedRoot_Object=MibTableColumn
tnSvcTlsStpDesignatedRoot=_TnSvcTlsStpDesignatedRoot_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,13),_TnSvcTlsStpDesignatedRoot_Type())
tnSvcTlsStpDesignatedRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcTlsStpDesignatedRoot.setStatus(_A)
_TnSvcTlsStpRootCost_Type=Integer32
_TnSvcTlsStpRootCost_Object=MibTableColumn
tnSvcTlsStpRootCost=_TnSvcTlsStpRootCost_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,14),_TnSvcTlsStpRootCost_Type())
tnSvcTlsStpRootCost.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcTlsStpRootCost.setStatus(_A)
_TnSvcTlsStpRootPort_Type=Integer32
_TnSvcTlsStpRootPort_Object=MibTableColumn
tnSvcTlsStpRootPort=_TnSvcTlsStpRootPort_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,15),_TnSvcTlsStpRootPort_Type())
tnSvcTlsStpRootPort.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcTlsStpRootPort.setStatus(_A)
_TnSvcTlsStpMaxAge_Type=Integer32
_TnSvcTlsStpMaxAge_Object=MibTableColumn
tnSvcTlsStpMaxAge=_TnSvcTlsStpMaxAge_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,16),_TnSvcTlsStpMaxAge_Type())
tnSvcTlsStpMaxAge.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcTlsStpMaxAge.setStatus(_A)
_TnSvcTlsStpHelloTime_Type=Integer32
_TnSvcTlsStpHelloTime_Object=MibTableColumn
tnSvcTlsStpHelloTime=_TnSvcTlsStpHelloTime_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,17),_TnSvcTlsStpHelloTime_Type())
tnSvcTlsStpHelloTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcTlsStpHelloTime.setStatus(_A)
_TnSvcTlsStpForwardDelay_Type=Integer32
_TnSvcTlsStpForwardDelay_Object=MibTableColumn
tnSvcTlsStpForwardDelay=_TnSvcTlsStpForwardDelay_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,19),_TnSvcTlsStpForwardDelay_Type())
tnSvcTlsStpForwardDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcTlsStpForwardDelay.setStatus(_A)
class _TnSvcTlsStpBridgeMaxAge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(6,40))
_TnSvcTlsStpBridgeMaxAge_Type.__name__=_E
_TnSvcTlsStpBridgeMaxAge_Object=MibTableColumn
tnSvcTlsStpBridgeMaxAge=_TnSvcTlsStpBridgeMaxAge_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,20),_TnSvcTlsStpBridgeMaxAge_Type())
tnSvcTlsStpBridgeMaxAge.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSvcTlsStpBridgeMaxAge.setStatus(_A)
class _TnSvcTlsStpBridgeHelloTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_TnSvcTlsStpBridgeHelloTime_Type.__name__=_E
_TnSvcTlsStpBridgeHelloTime_Object=MibTableColumn
tnSvcTlsStpBridgeHelloTime=_TnSvcTlsStpBridgeHelloTime_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,21),_TnSvcTlsStpBridgeHelloTime_Type())
tnSvcTlsStpBridgeHelloTime.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSvcTlsStpBridgeHelloTime.setStatus(_A)
class _TnSvcTlsStpBridgeForwardDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,30))
_TnSvcTlsStpBridgeForwardDelay_Type.__name__=_E
_TnSvcTlsStpBridgeForwardDelay_Object=MibTableColumn
tnSvcTlsStpBridgeForwardDelay=_TnSvcTlsStpBridgeForwardDelay_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,22),_TnSvcTlsStpBridgeForwardDelay_Type())
tnSvcTlsStpBridgeForwardDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSvcTlsStpBridgeForwardDelay.setStatus(_A)
class _TnSvcTlsStpOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),(_X,2)))
_TnSvcTlsStpOperStatus_Type.__name__=_E
_TnSvcTlsStpOperStatus_Object=MibTableColumn
tnSvcTlsStpOperStatus=_TnSvcTlsStpOperStatus_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,30),_TnSvcTlsStpOperStatus_Type())
tnSvcTlsStpOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcTlsStpOperStatus.setStatus(_A)
class _TnSvcTlsStpVirtualRootBridgeStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),(_X,2)))
_TnSvcTlsStpVirtualRootBridgeStatus_Type.__name__=_E
_TnSvcTlsStpVirtualRootBridgeStatus_Object=MibTableColumn
tnSvcTlsStpVirtualRootBridgeStatus=_TnSvcTlsStpVirtualRootBridgeStatus_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,31),_TnSvcTlsStpVirtualRootBridgeStatus_Type())
tnSvcTlsStpVirtualRootBridgeStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcTlsStpVirtualRootBridgeStatus.setStatus(_A)
class _TnSvcTlsMacAgeing_Type(TmnxEnabledDisabled):defaultValue=1
_TnSvcTlsMacAgeing_Type.__name__=_J
_TnSvcTlsMacAgeing_Object=MibTableColumn
tnSvcTlsMacAgeing=_TnSvcTlsMacAgeing_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,32),_TnSvcTlsMacAgeing_Type())
tnSvcTlsMacAgeing.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSvcTlsMacAgeing.setStatus(_A)
_TnSvcTlsStpTopologyChangeActive_Type=TruthValue
_TnSvcTlsStpTopologyChangeActive_Object=MibTableColumn
tnSvcTlsStpTopologyChangeActive=_TnSvcTlsStpTopologyChangeActive_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,33),_TnSvcTlsStpTopologyChangeActive_Type())
tnSvcTlsStpTopologyChangeActive.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcTlsStpTopologyChangeActive.setStatus(_A)
class _TnSvcTlsFdbTableFullHighWatermark_Type(Integer32):defaultValue=95;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_TnSvcTlsFdbTableFullHighWatermark_Type.__name__=_E
_TnSvcTlsFdbTableFullHighWatermark_Object=MibTableColumn
tnSvcTlsFdbTableFullHighWatermark=_TnSvcTlsFdbTableFullHighWatermark_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,34),_TnSvcTlsFdbTableFullHighWatermark_Type())
tnSvcTlsFdbTableFullHighWatermark.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSvcTlsFdbTableFullHighWatermark.setStatus(_A)
class _TnSvcTlsFdbTableFullLowWatermark_Type(Integer32):defaultValue=90;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_TnSvcTlsFdbTableFullLowWatermark_Type.__name__=_E
_TnSvcTlsFdbTableFullLowWatermark_Object=MibTableColumn
tnSvcTlsFdbTableFullLowWatermark=_TnSvcTlsFdbTableFullLowWatermark_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,35),_TnSvcTlsFdbTableFullLowWatermark_Type())
tnSvcTlsFdbTableFullLowWatermark.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSvcTlsFdbTableFullLowWatermark.setStatus(_A)
_TnSvcTlsVpnId_Type=VpnId
_TnSvcTlsVpnId_Object=MibTableColumn
tnSvcTlsVpnId=_TnSvcTlsVpnId_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,36),_TnSvcTlsVpnId_Type())
tnSvcTlsVpnId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcTlsVpnId.setStatus(_A)
_TnSvcTlsCustId_Type=TmnxCustId
_TnSvcTlsCustId_Object=MibTableColumn
tnSvcTlsCustId=_TnSvcTlsCustId_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,37),_TnSvcTlsCustId_Type())
tnSvcTlsCustId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcTlsCustId.setStatus(_A)
class _TnSvcTlsStpVersion_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5,6)));namedValues=NamedValues(*(('rstp',2),('compDot1w',3),('dot1w',4),('mstp',5),('pmstp',6)))
_TnSvcTlsStpVersion_Type.__name__=_E
_TnSvcTlsStpVersion_Object=MibTableColumn
tnSvcTlsStpVersion=_TnSvcTlsStpVersion_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,38),_TnSvcTlsStpVersion_Type())
tnSvcTlsStpVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSvcTlsStpVersion.setStatus(_A)
class _TnSvcTlsStpHoldCount_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_TnSvcTlsStpHoldCount_Type.__name__=_E
_TnSvcTlsStpHoldCount_Object=MibTableColumn
tnSvcTlsStpHoldCount=_TnSvcTlsStpHoldCount_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,39),_TnSvcTlsStpHoldCount_Type())
tnSvcTlsStpHoldCount.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSvcTlsStpHoldCount.setStatus(_A)
_TnSvcTlsStpPrimaryBridge_Type=BridgeId
_TnSvcTlsStpPrimaryBridge_Object=MibTableColumn
tnSvcTlsStpPrimaryBridge=_TnSvcTlsStpPrimaryBridge_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,40),_TnSvcTlsStpPrimaryBridge_Type())
tnSvcTlsStpPrimaryBridge.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcTlsStpPrimaryBridge.setStatus(_A)
class _TnSvcTlsStpBridgeInstanceId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_TnSvcTlsStpBridgeInstanceId_Type.__name__=_E
_TnSvcTlsStpBridgeInstanceId_Object=MibTableColumn
tnSvcTlsStpBridgeInstanceId=_TnSvcTlsStpBridgeInstanceId_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,41),_TnSvcTlsStpBridgeInstanceId_Type())
tnSvcTlsStpBridgeInstanceId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcTlsStpBridgeInstanceId.setStatus(_A)
_TnSvcTlsStpVcpOperProtocol_Type=StpProtocol
_TnSvcTlsStpVcpOperProtocol_Object=MibTableColumn
tnSvcTlsStpVcpOperProtocol=_TnSvcTlsStpVcpOperProtocol_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,42),_TnSvcTlsStpVcpOperProtocol_Type())
tnSvcTlsStpVcpOperProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcTlsStpVcpOperProtocol.setStatus(_A)
class _TnSvcTlsMacMoveMaxRate_Type(Unsigned32):defaultValue=2;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_TnSvcTlsMacMoveMaxRate_Type.__name__=_I
_TnSvcTlsMacMoveMaxRate_Object=MibTableColumn
tnSvcTlsMacMoveMaxRate=_TnSvcTlsMacMoveMaxRate_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,43),_TnSvcTlsMacMoveMaxRate_Type())
tnSvcTlsMacMoveMaxRate.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSvcTlsMacMoveMaxRate.setStatus(_A)
class _TnSvcTlsMacMoveRetryTimeout_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,600))
_TnSvcTlsMacMoveRetryTimeout_Type.__name__=_I
_TnSvcTlsMacMoveRetryTimeout_Object=MibTableColumn
tnSvcTlsMacMoveRetryTimeout=_TnSvcTlsMacMoveRetryTimeout_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,44),_TnSvcTlsMacMoveRetryTimeout_Type())
tnSvcTlsMacMoveRetryTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSvcTlsMacMoveRetryTimeout.setStatus(_A)
class _TnSvcTlsMacMoveAdminStatus_Type(TmnxEnabledDisabled):defaultValue=2
_TnSvcTlsMacMoveAdminStatus_Type.__name__=_J
_TnSvcTlsMacMoveAdminStatus_Object=MibTableColumn
tnSvcTlsMacMoveAdminStatus=_TnSvcTlsMacMoveAdminStatus_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,45),_TnSvcTlsMacMoveAdminStatus_Type())
tnSvcTlsMacMoveAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSvcTlsMacMoveAdminStatus.setStatus(_A)
_TnSvcTlsMacRelearnOnly_Type=TruthValue
_TnSvcTlsMacRelearnOnly_Object=MibTableColumn
tnSvcTlsMacRelearnOnly=_TnSvcTlsMacRelearnOnly_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,46),_TnSvcTlsMacRelearnOnly_Type())
tnSvcTlsMacRelearnOnly.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcTlsMacRelearnOnly.setStatus(_A)
class _TnSvcTlsMfibTableSize_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16383))
_TnSvcTlsMfibTableSize_Type.__name__=_E
_TnSvcTlsMfibTableSize_Object=MibTableColumn
tnSvcTlsMfibTableSize=_TnSvcTlsMfibTableSize_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,47),_TnSvcTlsMfibTableSize_Type())
tnSvcTlsMfibTableSize.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSvcTlsMfibTableSize.setStatus(_A)
class _TnSvcTlsMfibTableFullHighWatermark_Type(Integer32):defaultValue=95;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_TnSvcTlsMfibTableFullHighWatermark_Type.__name__=_E
_TnSvcTlsMfibTableFullHighWatermark_Object=MibTableColumn
tnSvcTlsMfibTableFullHighWatermark=_TnSvcTlsMfibTableFullHighWatermark_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,48),_TnSvcTlsMfibTableFullHighWatermark_Type())
tnSvcTlsMfibTableFullHighWatermark.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSvcTlsMfibTableFullHighWatermark.setStatus(_A)
class _TnSvcTlsMfibTableFullLowWatermark_Type(Integer32):defaultValue=90;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_TnSvcTlsMfibTableFullLowWatermark_Type.__name__=_E
_TnSvcTlsMfibTableFullLowWatermark_Object=MibTableColumn
tnSvcTlsMfibTableFullLowWatermark=_TnSvcTlsMfibTableFullLowWatermark_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,49),_TnSvcTlsMfibTableFullLowWatermark_Type())
tnSvcTlsMfibTableFullLowWatermark.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSvcTlsMfibTableFullLowWatermark.setStatus(_A)
class _TnSvcTlsMacFlushOnFail_Type(TmnxEnabledDisabled):defaultValue=2
_TnSvcTlsMacFlushOnFail_Type.__name__=_J
_TnSvcTlsMacFlushOnFail_Object=MibTableColumn
tnSvcTlsMacFlushOnFail=_TnSvcTlsMacFlushOnFail_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,50),_TnSvcTlsMacFlushOnFail_Type())
tnSvcTlsMacFlushOnFail.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSvcTlsMacFlushOnFail.setStatus(_A)
class _TnSvcTlsStpRegionName_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_TnSvcTlsStpRegionName_Type.__name__=_U
_TnSvcTlsStpRegionName_Object=MibTableColumn
tnSvcTlsStpRegionName=_TnSvcTlsStpRegionName_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,51),_TnSvcTlsStpRegionName_Type())
tnSvcTlsStpRegionName.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSvcTlsStpRegionName.setStatus(_A)
class _TnSvcTlsStpRegionRevision_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_TnSvcTlsStpRegionRevision_Type.__name__=_E
_TnSvcTlsStpRegionRevision_Object=MibTableColumn
tnSvcTlsStpRegionRevision=_TnSvcTlsStpRegionRevision_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,52),_TnSvcTlsStpRegionRevision_Type())
tnSvcTlsStpRegionRevision.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSvcTlsStpRegionRevision.setStatus(_A)
class _TnSvcTlsStpBridgeMaxHops_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,40))
_TnSvcTlsStpBridgeMaxHops_Type.__name__=_E
_TnSvcTlsStpBridgeMaxHops_Object=MibTableColumn
tnSvcTlsStpBridgeMaxHops=_TnSvcTlsStpBridgeMaxHops_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,53),_TnSvcTlsStpBridgeMaxHops_Type())
tnSvcTlsStpBridgeMaxHops.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSvcTlsStpBridgeMaxHops.setStatus(_A)
_TnSvcTlsStpCistRegionalRoot_Type=BridgeId
_TnSvcTlsStpCistRegionalRoot_Object=MibTableColumn
tnSvcTlsStpCistRegionalRoot=_TnSvcTlsStpCistRegionalRoot_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,54),_TnSvcTlsStpCistRegionalRoot_Type())
tnSvcTlsStpCistRegionalRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcTlsStpCistRegionalRoot.setStatus(_A)
_TnSvcTlsStpCistIntRootCost_Type=Integer32
_TnSvcTlsStpCistIntRootCost_Object=MibTableColumn
tnSvcTlsStpCistIntRootCost=_TnSvcTlsStpCistIntRootCost_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,55),_TnSvcTlsStpCistIntRootCost_Type())
tnSvcTlsStpCistIntRootCost.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcTlsStpCistIntRootCost.setStatus(_A)
_TnSvcTlsStpCistRemainingHopCount_Type=Integer32
_TnSvcTlsStpCistRemainingHopCount_Object=MibTableColumn
tnSvcTlsStpCistRemainingHopCount=_TnSvcTlsStpCistRemainingHopCount_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,56),_TnSvcTlsStpCistRemainingHopCount_Type())
tnSvcTlsStpCistRemainingHopCount.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcTlsStpCistRemainingHopCount.setStatus(_A)
_TnSvcTlsStpCistRegionalRootPort_Type=Integer32
_TnSvcTlsStpCistRegionalRootPort_Object=MibTableColumn
tnSvcTlsStpCistRegionalRootPort=_TnSvcTlsStpCistRegionalRootPort_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,57),_TnSvcTlsStpCistRegionalRootPort_Type())
tnSvcTlsStpCistRegionalRootPort.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcTlsStpCistRegionalRootPort.setStatus(_A)
_TnSvcTlsFdbNumLearnedEntries_Type=Integer32
_TnSvcTlsFdbNumLearnedEntries_Object=MibTableColumn
tnSvcTlsFdbNumLearnedEntries=_TnSvcTlsFdbNumLearnedEntries_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,58),_TnSvcTlsFdbNumLearnedEntries_Type())
tnSvcTlsFdbNumLearnedEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcTlsFdbNumLearnedEntries.setStatus(_A)
_TnSvcTlsFdbNumOamEntries_Type=Integer32
_TnSvcTlsFdbNumOamEntries_Object=MibTableColumn
tnSvcTlsFdbNumOamEntries=_TnSvcTlsFdbNumOamEntries_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,59),_TnSvcTlsFdbNumOamEntries_Type())
tnSvcTlsFdbNumOamEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcTlsFdbNumOamEntries.setStatus(_A)
_TnSvcTlsFdbNumDhcpEntries_Type=Integer32
_TnSvcTlsFdbNumDhcpEntries_Object=MibTableColumn
tnSvcTlsFdbNumDhcpEntries=_TnSvcTlsFdbNumDhcpEntries_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,60),_TnSvcTlsFdbNumDhcpEntries_Type())
tnSvcTlsFdbNumDhcpEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcTlsFdbNumDhcpEntries.setStatus(_A)
_TnSvcTlsFdbNumHostEntries_Type=Integer32
_TnSvcTlsFdbNumHostEntries_Object=MibTableColumn
tnSvcTlsFdbNumHostEntries=_TnSvcTlsFdbNumHostEntries_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,61),_TnSvcTlsFdbNumHostEntries_Type())
tnSvcTlsFdbNumHostEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcTlsFdbNumHostEntries.setStatus(_A)
class _TnSvcTlsShcvAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('alarm',1),('remove',2)))
_TnSvcTlsShcvAction_Type.__name__=_E
_TnSvcTlsShcvAction_Object=MibTableColumn
tnSvcTlsShcvAction=_TnSvcTlsShcvAction_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,62),_TnSvcTlsShcvAction_Type())
tnSvcTlsShcvAction.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSvcTlsShcvAction.setStatus(_A)
_TnSvcTlsShcvSrcIp_Type=IpAddress
_TnSvcTlsShcvSrcIp_Object=MibTableColumn
tnSvcTlsShcvSrcIp=_TnSvcTlsShcvSrcIp_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,63),_TnSvcTlsShcvSrcIp_Type())
tnSvcTlsShcvSrcIp.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSvcTlsShcvSrcIp.setStatus(_A)
_TnSvcTlsShcvSrcMac_Type=MacAddress
_TnSvcTlsShcvSrcMac_Object=MibTableColumn
tnSvcTlsShcvSrcMac=_TnSvcTlsShcvSrcMac_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,64),_TnSvcTlsShcvSrcMac_Type())
tnSvcTlsShcvSrcMac.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSvcTlsShcvSrcMac.setStatus(_A)
class _TnSvcTlsShcvInterval_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,6000))
_TnSvcTlsShcvInterval_Type.__name__=_I
_TnSvcTlsShcvInterval_Object=MibTableColumn
tnSvcTlsShcvInterval=_TnSvcTlsShcvInterval_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,65),_TnSvcTlsShcvInterval_Type())
tnSvcTlsShcvInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSvcTlsShcvInterval.setStatus(_A)
if mibBuilder.loadTexts:tnSvcTlsShcvInterval.setUnits('minutes')
class _TnSvcTlsPriPortsCumulativeFactor_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,10))
_TnSvcTlsPriPortsCumulativeFactor_Type.__name__=_I
_TnSvcTlsPriPortsCumulativeFactor_Object=MibTableColumn
tnSvcTlsPriPortsCumulativeFactor=_TnSvcTlsPriPortsCumulativeFactor_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,66),_TnSvcTlsPriPortsCumulativeFactor_Type())
tnSvcTlsPriPortsCumulativeFactor.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSvcTlsPriPortsCumulativeFactor.setStatus(_A)
class _TnSvcTlsSecPortsCumulativeFactor_Type(Unsigned32):defaultValue=2;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,9))
_TnSvcTlsSecPortsCumulativeFactor_Type.__name__=_I
_TnSvcTlsSecPortsCumulativeFactor_Object=MibTableColumn
tnSvcTlsSecPortsCumulativeFactor=_TnSvcTlsSecPortsCumulativeFactor_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,67),_TnSvcTlsSecPortsCumulativeFactor_Type())
tnSvcTlsSecPortsCumulativeFactor.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSvcTlsSecPortsCumulativeFactor.setStatus(_A)
_TnSvcTlsL2ptTermEnabled_Type=TruthValue
_TnSvcTlsL2ptTermEnabled_Object=MibTableColumn
tnSvcTlsL2ptTermEnabled=_TnSvcTlsL2ptTermEnabled_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,68),_TnSvcTlsL2ptTermEnabled_Type())
tnSvcTlsL2ptTermEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcTlsL2ptTermEnabled.setStatus(_A)
class _TnSvcTlsPropagateMacFlush_Type(TruthValue):defaultValue=2
_TnSvcTlsPropagateMacFlush_Type.__name__=_G
_TnSvcTlsPropagateMacFlush_Object=MibTableColumn
tnSvcTlsPropagateMacFlush=_TnSvcTlsPropagateMacFlush_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,69),_TnSvcTlsPropagateMacFlush_Type())
tnSvcTlsPropagateMacFlush.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSvcTlsPropagateMacFlush.setStatus(_A)
class _TnSvcTlsMrpAdminStatus_Type(TmnxEnabledDisabled):defaultValue=2
_TnSvcTlsMrpAdminStatus_Type.__name__=_J
_TnSvcTlsMrpAdminStatus_Object=MibTableColumn
tnSvcTlsMrpAdminStatus=_TnSvcTlsMrpAdminStatus_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,70),_TnSvcTlsMrpAdminStatus_Type())
tnSvcTlsMrpAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSvcTlsMrpAdminStatus.setStatus(_A)
class _TnSvcTlsMrpMaxAttributes_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2048))
_TnSvcTlsMrpMaxAttributes_Type.__name__=_I
_TnSvcTlsMrpMaxAttributes_Object=MibTableColumn
tnSvcTlsMrpMaxAttributes=_TnSvcTlsMrpMaxAttributes_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,71),_TnSvcTlsMrpMaxAttributes_Type())
tnSvcTlsMrpMaxAttributes.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSvcTlsMrpMaxAttributes.setStatus(_A)
_TnSvcTlsMrpAttributeCount_Type=Unsigned32
_TnSvcTlsMrpAttributeCount_Object=MibTableColumn
tnSvcTlsMrpAttributeCount=_TnSvcTlsMrpAttributeCount_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,72),_TnSvcTlsMrpAttributeCount_Type())
tnSvcTlsMrpAttributeCount.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcTlsMrpAttributeCount.setStatus(_A)
_TnSvcTlsMrpFailedRegisterCount_Type=Unsigned32
_TnSvcTlsMrpFailedRegisterCount_Object=MibTableColumn
tnSvcTlsMrpFailedRegisterCount=_TnSvcTlsMrpFailedRegisterCount_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,73),_TnSvcTlsMrpFailedRegisterCount_Type())
tnSvcTlsMrpFailedRegisterCount.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcTlsMrpFailedRegisterCount.setStatus(_A)
class _TnSvcTlsMcPathMgmtPlcyName_Type(TNamedItem):defaultValue=OctetString(_u)
_TnSvcTlsMcPathMgmtPlcyName_Type.__name__=_c
_TnSvcTlsMcPathMgmtPlcyName_Object=MibTableColumn
tnSvcTlsMcPathMgmtPlcyName=_TnSvcTlsMcPathMgmtPlcyName_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,74),_TnSvcTlsMcPathMgmtPlcyName_Type())
tnSvcTlsMcPathMgmtPlcyName.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSvcTlsMcPathMgmtPlcyName.setStatus(_A)
class _TnSvcTlsMrpFloodTime_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(3,600))
_TnSvcTlsMrpFloodTime_Type.__name__=_I
_TnSvcTlsMrpFloodTime_Object=MibTableColumn
tnSvcTlsMrpFloodTime=_TnSvcTlsMrpFloodTime_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,75),_TnSvcTlsMrpFloodTime_Type())
tnSvcTlsMrpFloodTime.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSvcTlsMrpFloodTime.setStatus(_A)
if mibBuilder.loadTexts:tnSvcTlsMrpFloodTime.setUnits(_Q)
class _TnSvcTlsMrpAttrTblHighWatermark_Type(Integer32):defaultValue=95;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_TnSvcTlsMrpAttrTblHighWatermark_Type.__name__=_E
_TnSvcTlsMrpAttrTblHighWatermark_Object=MibTableColumn
tnSvcTlsMrpAttrTblHighWatermark=_TnSvcTlsMrpAttrTblHighWatermark_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,76),_TnSvcTlsMrpAttrTblHighWatermark_Type())
tnSvcTlsMrpAttrTblHighWatermark.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSvcTlsMrpAttrTblHighWatermark.setStatus(_A)
class _TnSvcTlsMrpAttrTblLowWatermark_Type(Integer32):defaultValue=90;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_TnSvcTlsMrpAttrTblLowWatermark_Type.__name__=_E
_TnSvcTlsMrpAttrTblLowWatermark_Object=MibTableColumn
tnSvcTlsMrpAttrTblLowWatermark=_TnSvcTlsMrpAttrTblLowWatermark_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,77),_TnSvcTlsMrpAttrTblLowWatermark_Type())
tnSvcTlsMrpAttrTblLowWatermark.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSvcTlsMrpAttrTblLowWatermark.setStatus(_A)
class _TnSvcTlsMacMoveNumRetries_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_TnSvcTlsMacMoveNumRetries_Type.__name__=_I
_TnSvcTlsMacMoveNumRetries_Object=MibTableColumn
tnSvcTlsMacMoveNumRetries=_TnSvcTlsMacMoveNumRetries_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,78),_TnSvcTlsMacMoveNumRetries_Type())
tnSvcTlsMacMoveNumRetries.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSvcTlsMacMoveNumRetries.setStatus(_A)
class _TnSvcTlsMacSubNetLen_Type(Integer32):defaultValue=48;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(24,48))
_TnSvcTlsMacSubNetLen_Type.__name__=_E
_TnSvcTlsMacSubNetLen_Object=MibTableColumn
tnSvcTlsMacSubNetLen=_TnSvcTlsMacSubNetLen_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,79),_TnSvcTlsMacSubNetLen_Type())
tnSvcTlsMacSubNetLen.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSvcTlsMacSubNetLen.setStatus(_A)
class _TnSvcTlsSendFlushOnBVplsFail_Type(TruthValue):defaultValue=2
_TnSvcTlsSendFlushOnBVplsFail_Type.__name__=_G
_TnSvcTlsSendFlushOnBVplsFail_Object=MibTableColumn
tnSvcTlsSendFlushOnBVplsFail=_TnSvcTlsSendFlushOnBVplsFail_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,80),_TnSvcTlsSendFlushOnBVplsFail_Type())
tnSvcTlsSendFlushOnBVplsFail.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSvcTlsSendFlushOnBVplsFail.setStatus(_A)
class _TnSvcTlsPropMacFlushFromBVpls_Type(TruthValue):defaultValue=2
_TnSvcTlsPropMacFlushFromBVpls_Type.__name__=_G
_TnSvcTlsPropMacFlushFromBVpls_Object=MibTableColumn
tnSvcTlsPropMacFlushFromBVpls=_TnSvcTlsPropMacFlushFromBVpls_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,81),_TnSvcTlsPropMacFlushFromBVpls_Type())
tnSvcTlsPropMacFlushFromBVpls.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSvcTlsPropMacFlushFromBVpls.setStatus(_A)
class _TnSvcTlsMacNotifInterval_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_TnSvcTlsMacNotifInterval_Type.__name__=_I
_TnSvcTlsMacNotifInterval_Object=MibTableColumn
tnSvcTlsMacNotifInterval=_TnSvcTlsMacNotifInterval_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,82),_TnSvcTlsMacNotifInterval_Type())
tnSvcTlsMacNotifInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSvcTlsMacNotifInterval.setStatus(_A)
if mibBuilder.loadTexts:tnSvcTlsMacNotifInterval.setUnits(_x)
class _TnSvcTlsMacNotifCount_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_TnSvcTlsMacNotifCount_Type.__name__=_I
_TnSvcTlsMacNotifCount_Object=MibTableColumn
tnSvcTlsMacNotifCount=_TnSvcTlsMacNotifCount_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,83),_TnSvcTlsMacNotifCount_Type())
tnSvcTlsMacNotifCount.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSvcTlsMacNotifCount.setStatus(_A)
class _TnSvcTlsMacNotifAdminState_Type(TmnxEnabledDisabled):defaultValue=2
_TnSvcTlsMacNotifAdminState_Type.__name__=_J
_TnSvcTlsMacNotifAdminState_Object=MibTableColumn
tnSvcTlsMacNotifAdminState=_TnSvcTlsMacNotifAdminState_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,84),_TnSvcTlsMacNotifAdminState_Type())
tnSvcTlsMacNotifAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSvcTlsMacNotifAdminState.setStatus(_A)
class _TnSvcTlsShcvRetryTimeout_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,60))
_TnSvcTlsShcvRetryTimeout_Type.__name__=_I
_TnSvcTlsShcvRetryTimeout_Object=MibTableColumn
tnSvcTlsShcvRetryTimeout=_TnSvcTlsShcvRetryTimeout_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,87),_TnSvcTlsShcvRetryTimeout_Type())
tnSvcTlsShcvRetryTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSvcTlsShcvRetryTimeout.setStatus(_A)
if mibBuilder.loadTexts:tnSvcTlsShcvRetryTimeout.setUnits(_Q)
class _TnSvcTlsShcvRetryCount_Type(Unsigned32):defaultValue=2;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,29))
_TnSvcTlsShcvRetryCount_Type.__name__=_I
_TnSvcTlsShcvRetryCount_Object=MibTableColumn
tnSvcTlsShcvRetryCount=_TnSvcTlsShcvRetryCount_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,88),_TnSvcTlsShcvRetryCount_Type())
tnSvcTlsShcvRetryCount.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSvcTlsShcvRetryCount.setStatus(_A)
class _TnsvcTlsAllowIpIfBinding_Type(TruthValue):defaultValue=2
_TnsvcTlsAllowIpIfBinding_Type.__name__=_G
_TnsvcTlsAllowIpIfBinding_Object=MibTableColumn
tnsvcTlsAllowIpIfBinding=_TnsvcTlsAllowIpIfBinding_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,89),_TnsvcTlsAllowIpIfBinding_Type())
tnsvcTlsAllowIpIfBinding.setMaxAccess(_D)
if mibBuilder.loadTexts:tnsvcTlsAllowIpIfBinding.setStatus(_A)
_TnSvcTlsMfibTableNumEntries_Type=Integer32
_TnSvcTlsMfibTableNumEntries_Object=MibTableColumn
tnSvcTlsMfibTableNumEntries=_TnSvcTlsMfibTableNumEntries_Object((1,3,6,1,4,1,7483,6,1,2,4,2,3,1,90),_TnSvcTlsMfibTableNumEntries_Type())
tnSvcTlsMfibTableNumEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcTlsMfibTableNumEntries.setStatus(_A)
_TnTlsFdbInfoTable_Object=MibTable
tnTlsFdbInfoTable=_TnTlsFdbInfoTable_Object((1,3,6,1,4,1,7483,6,1,2,4,2,4))
if mibBuilder.loadTexts:tnTlsFdbInfoTable.setStatus(_A)
_TnTlsFdbInfoEntry_Object=MibTableRow
tnTlsFdbInfoEntry=_TnTlsFdbInfoEntry_Object((1,3,6,1,4,1,7483,6,1,2,4,2,4,1))
tnTlsFdbInfoEntry.setIndexNames((0,_K,_L),(0,_F,_N),(0,_F,_y))
if mibBuilder.loadTexts:tnTlsFdbInfoEntry.setStatus(_A)
_TnTlsFdbMacAddr_Type=MacAddress
_TnTlsFdbMacAddr_Object=MibTableColumn
tnTlsFdbMacAddr=_TnTlsFdbMacAddr_Object((1,3,6,1,4,1,7483,6,1,2,4,2,4,1,1),_TnTlsFdbMacAddr_Type())
tnTlsFdbMacAddr.setMaxAccess(_H)
if mibBuilder.loadTexts:tnTlsFdbMacAddr.setStatus(_A)
_TnTlsFdbRowStatus_Type=RowStatus
_TnTlsFdbRowStatus_Object=MibTableColumn
tnTlsFdbRowStatus=_TnTlsFdbRowStatus_Object((1,3,6,1,4,1,7483,6,1,2,4,2,4,1,2),_TnTlsFdbRowStatus_Type())
tnTlsFdbRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tnTlsFdbRowStatus.setStatus(_A)
class _TnTlsFdbType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('static',1),('learned',2),('oam',3),('dhcp',4),('host',5)))
_TnTlsFdbType_Type.__name__=_E
_TnTlsFdbType_Object=MibTableColumn
tnTlsFdbType=_TnTlsFdbType_Object((1,3,6,1,4,1,7483,6,1,2,4,2,4,1,3),_TnTlsFdbType_Type())
tnTlsFdbType.setMaxAccess(_C)
if mibBuilder.loadTexts:tnTlsFdbType.setStatus(_A)
class _TnTlsFdbLocale_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_T,1),('sdp',2),('cpm',3),('endpoint',4)))
_TnTlsFdbLocale_Type.__name__=_E
_TnTlsFdbLocale_Object=MibTableColumn
tnTlsFdbLocale=_TnTlsFdbLocale_Object((1,3,6,1,4,1,7483,6,1,2,4,2,4,1,4),_TnTlsFdbLocale_Type())
tnTlsFdbLocale.setMaxAccess(_C)
if mibBuilder.loadTexts:tnTlsFdbLocale.setStatus(_A)
_TnTlsFdbPortId_Type=TmnxPortID
_TnTlsFdbPortId_Object=MibTableColumn
tnTlsFdbPortId=_TnTlsFdbPortId_Object((1,3,6,1,4,1,7483,6,1,2,4,2,4,1,5),_TnTlsFdbPortId_Type())
tnTlsFdbPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnTlsFdbPortId.setStatus(_A)
_TnTlsFdbEncapValue_Type=TmnxEncapVal
_TnTlsFdbEncapValue_Object=MibTableColumn
tnTlsFdbEncapValue=_TnTlsFdbEncapValue_Object((1,3,6,1,4,1,7483,6,1,2,4,2,4,1,6),_TnTlsFdbEncapValue_Type())
tnTlsFdbEncapValue.setMaxAccess(_C)
if mibBuilder.loadTexts:tnTlsFdbEncapValue.setStatus(_A)
_TnTlsFdbSdpId_Type=SdpId
_TnTlsFdbSdpId_Object=MibTableColumn
tnTlsFdbSdpId=_TnTlsFdbSdpId_Object((1,3,6,1,4,1,7483,6,1,2,4,2,4,1,7),_TnTlsFdbSdpId_Type())
tnTlsFdbSdpId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnTlsFdbSdpId.setStatus(_A)
_TnTlsFdbVcId_Type=Unsigned32
_TnTlsFdbVcId_Object=MibTableColumn
tnTlsFdbVcId=_TnTlsFdbVcId_Object((1,3,6,1,4,1,7483,6,1,2,4,2,4,1,8),_TnTlsFdbVcId_Type())
tnTlsFdbVcId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnTlsFdbVcId.setStatus(_A)
_TnTlsFdbVpnId_Type=VpnId
_TnTlsFdbVpnId_Object=MibTableColumn
tnTlsFdbVpnId=_TnTlsFdbVpnId_Object((1,3,6,1,4,1,7483,6,1,2,4,2,4,1,9),_TnTlsFdbVpnId_Type())
tnTlsFdbVpnId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnTlsFdbVpnId.setStatus(_A)
_TnTlsFdbCustId_Type=TmnxCustId
_TnTlsFdbCustId_Object=MibTableColumn
tnTlsFdbCustId=_TnTlsFdbCustId_Object((1,3,6,1,4,1,7483,6,1,2,4,2,4,1,10),_TnTlsFdbCustId_Type())
tnTlsFdbCustId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnTlsFdbCustId.setStatus(_A)
_TnTlsFdbLastStateChange_Type=TimeStamp
_TnTlsFdbLastStateChange_Object=MibTableColumn
tnTlsFdbLastStateChange=_TnTlsFdbLastStateChange_Object((1,3,6,1,4,1,7483,6,1,2,4,2,4,1,11),_TnTlsFdbLastStateChange_Type())
tnTlsFdbLastStateChange.setMaxAccess(_B)
if mibBuilder.loadTexts:tnTlsFdbLastStateChange.setStatus(_A)
_TnTlsFdbProtected_Type=TruthValue
_TnTlsFdbProtected_Object=MibTableColumn
tnTlsFdbProtected=_TnTlsFdbProtected_Object((1,3,6,1,4,1,7483,6,1,2,4,2,4,1,12),_TnTlsFdbProtected_Type())
tnTlsFdbProtected.setMaxAccess(_B)
if mibBuilder.loadTexts:tnTlsFdbProtected.setStatus(_A)
_TnTlsFdbBackboneDstMac_Type=MacAddress
_TnTlsFdbBackboneDstMac_Object=MibTableColumn
tnTlsFdbBackboneDstMac=_TnTlsFdbBackboneDstMac_Object((1,3,6,1,4,1,7483,6,1,2,4,2,4,1,13),_TnTlsFdbBackboneDstMac_Type())
tnTlsFdbBackboneDstMac.setMaxAccess(_B)
if mibBuilder.loadTexts:tnTlsFdbBackboneDstMac.setStatus(_A)
_TnTlsFdbNumIVplsMac_Type=Unsigned32
_TnTlsFdbNumIVplsMac_Object=MibTableColumn
tnTlsFdbNumIVplsMac=_TnTlsFdbNumIVplsMac_Object((1,3,6,1,4,1,7483,6,1,2,4,2,4,1,14),_TnTlsFdbNumIVplsMac_Type())
tnTlsFdbNumIVplsMac.setMaxAccess(_B)
if mibBuilder.loadTexts:tnTlsFdbNumIVplsMac.setStatus(_A)
class _TnTlsFdbEndPointName_Type(TNamedItemOrEmpty):defaultValue=OctetString('')
_TnTlsFdbEndPointName_Type.__name__=_P
_TnTlsFdbEndPointName_Object=MibTableColumn
tnTlsFdbEndPointName=_TnTlsFdbEndPointName_Object((1,3,6,1,4,1,7483,6,1,2,4,2,4,1,15),_TnTlsFdbEndPointName_Type())
tnTlsFdbEndPointName.setMaxAccess(_C)
if mibBuilder.loadTexts:tnTlsFdbEndPointName.setStatus(_A)
_TnTlsFdbEPMacOperSdpId_Type=SdpId
_TnTlsFdbEPMacOperSdpId_Object=MibTableColumn
tnTlsFdbEPMacOperSdpId=_TnTlsFdbEPMacOperSdpId_Object((1,3,6,1,4,1,7483,6,1,2,4,2,4,1,16),_TnTlsFdbEPMacOperSdpId_Type())
tnTlsFdbEPMacOperSdpId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnTlsFdbEPMacOperSdpId.setStatus(_A)
_TnTlsFdbEPMacOperVcId_Type=Unsigned32
_TnTlsFdbEPMacOperVcId_Object=MibTableColumn
tnTlsFdbEPMacOperVcId=_TnTlsFdbEPMacOperVcId_Object((1,3,6,1,4,1,7483,6,1,2,4,2,4,1,17),_TnTlsFdbEPMacOperVcId_Type())
tnTlsFdbEPMacOperVcId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnTlsFdbEPMacOperVcId.setStatus(_A)
_TnTlsFdbPbbNumEpipes_Type=Unsigned32
_TnTlsFdbPbbNumEpipes_Object=MibTableColumn
tnTlsFdbPbbNumEpipes=_TnTlsFdbPbbNumEpipes_Object((1,3,6,1,4,1,7483,6,1,2,4,2,4,1,18),_TnTlsFdbPbbNumEpipes_Type())
tnTlsFdbPbbNumEpipes.setMaxAccess(_B)
if mibBuilder.loadTexts:tnTlsFdbPbbNumEpipes.setStatus(_A)
_TnTlsShgInfoTable_Object=MibTable
tnTlsShgInfoTable=_TnTlsShgInfoTable_Object((1,3,6,1,4,1,7483,6,1,2,4,2,6))
if mibBuilder.loadTexts:tnTlsShgInfoTable.setStatus(_A)
_TnTlsShgInfoEntry_Object=MibTableRow
tnTlsShgInfoEntry=_TnTlsShgInfoEntry_Object((1,3,6,1,4,1,7483,6,1,2,4,2,6,1))
tnTlsShgInfoEntry.setIndexNames((0,_K,_L),(0,_F,_N),(1,_F,_z))
if mibBuilder.loadTexts:tnTlsShgInfoEntry.setStatus(_A)
_TnTlsShgName_Type=TNamedItem
_TnTlsShgName_Object=MibTableColumn
tnTlsShgName=_TnTlsShgName_Object((1,3,6,1,4,1,7483,6,1,2,4,2,6,1,1),_TnTlsShgName_Type())
tnTlsShgName.setMaxAccess(_H)
if mibBuilder.loadTexts:tnTlsShgName.setStatus(_A)
_TnTlsShgRowStatus_Type=RowStatus
_TnTlsShgRowStatus_Object=MibTableColumn
tnTlsShgRowStatus=_TnTlsShgRowStatus_Object((1,3,6,1,4,1,7483,6,1,2,4,2,6,1,2),_TnTlsShgRowStatus_Type())
tnTlsShgRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tnTlsShgRowStatus.setStatus(_A)
_TnTlsShgCustId_Type=TmnxCustId
_TnTlsShgCustId_Object=MibTableColumn
tnTlsShgCustId=_TnTlsShgCustId_Object((1,3,6,1,4,1,7483,6,1,2,4,2,6,1,3),_TnTlsShgCustId_Type())
tnTlsShgCustId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnTlsShgCustId.setStatus(_A)
_TnTlsShgInstanceId_Type=Unsigned32
_TnTlsShgInstanceId_Object=MibTableColumn
tnTlsShgInstanceId=_TnTlsShgInstanceId_Object((1,3,6,1,4,1,7483,6,1,2,4,2,6,1,4),_TnTlsShgInstanceId_Type())
tnTlsShgInstanceId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnTlsShgInstanceId.setStatus(_A)
class _TnTlsShgDescription_Type(ServObjDesc):defaultValue=OctetString('')
_TnTlsShgDescription_Type.__name__=_M
_TnTlsShgDescription_Object=MibTableColumn
tnTlsShgDescription=_TnTlsShgDescription_Object((1,3,6,1,4,1,7483,6,1,2,4,2,6,1,5),_TnTlsShgDescription_Type())
tnTlsShgDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:tnTlsShgDescription.setStatus(_A)
_TnTlsShgLastMgmtChange_Type=TimeStamp
_TnTlsShgLastMgmtChange_Object=MibTableColumn
tnTlsShgLastMgmtChange=_TnTlsShgLastMgmtChange_Object((1,3,6,1,4,1,7483,6,1,2,4,2,6,1,6),_TnTlsShgLastMgmtChange_Type())
tnTlsShgLastMgmtChange.setMaxAccess(_B)
if mibBuilder.loadTexts:tnTlsShgLastMgmtChange.setStatus(_A)
class _TnTlsShgResidential_Type(TruthValue):defaultValue=2
_TnTlsShgResidential_Type.__name__=_G
_TnTlsShgResidential_Object=MibTableColumn
tnTlsShgResidential=_TnTlsShgResidential_Object((1,3,6,1,4,1,7483,6,1,2,4,2,6,1,7),_TnTlsShgResidential_Type())
tnTlsShgResidential.setMaxAccess(_C)
if mibBuilder.loadTexts:tnTlsShgResidential.setStatus(_A)
class _TnTlsShgRestProtSrcMac_Type(TruthValue):defaultValue=2
_TnTlsShgRestProtSrcMac_Type.__name__=_G
_TnTlsShgRestProtSrcMac_Object=MibTableColumn
tnTlsShgRestProtSrcMac=_TnTlsShgRestProtSrcMac_Object((1,3,6,1,4,1,7483,6,1,2,4,2,6,1,8),_TnTlsShgRestProtSrcMac_Type())
tnTlsShgRestProtSrcMac.setMaxAccess(_C)
if mibBuilder.loadTexts:tnTlsShgRestProtSrcMac.setStatus(_A)
class _TnTlsShgRestUnprotDstMac_Type(TruthValue):defaultValue=2
_TnTlsShgRestUnprotDstMac_Type.__name__=_G
_TnTlsShgRestUnprotDstMac_Object=MibTableColumn
tnTlsShgRestUnprotDstMac=_TnTlsShgRestUnprotDstMac_Object((1,3,6,1,4,1,7483,6,1,2,4,2,6,1,9),_TnTlsShgRestUnprotDstMac_Type())
tnTlsShgRestUnprotDstMac.setMaxAccess(_C)
if mibBuilder.loadTexts:tnTlsShgRestUnprotDstMac.setStatus(_A)
class _TnTlsShgRestProtSrcMacAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disable',1),('alarm-only',2)))
_TnTlsShgRestProtSrcMacAction_Type.__name__=_E
_TnTlsShgRestProtSrcMacAction_Object=MibTableColumn
tnTlsShgRestProtSrcMacAction=_TnTlsShgRestProtSrcMacAction_Object((1,3,6,1,4,1,7483,6,1,2,4,2,6,1,10),_TnTlsShgRestProtSrcMacAction_Type())
tnTlsShgRestProtSrcMacAction.setMaxAccess(_C)
if mibBuilder.loadTexts:tnTlsShgRestProtSrcMacAction.setStatus(_A)
_TnTlsShgCreationOrigin_Type=L2RouteOrigin
_TnTlsShgCreationOrigin_Object=MibTableColumn
tnTlsShgCreationOrigin=_TnTlsShgCreationOrigin_Object((1,3,6,1,4,1,7483,6,1,2,4,2,6,1,11),_TnTlsShgCreationOrigin_Type())
tnTlsShgCreationOrigin.setMaxAccess(_B)
if mibBuilder.loadTexts:tnTlsShgCreationOrigin.setStatus(_A)
_TnSvcEndPointTable_Object=MibTable
tnSvcEndPointTable=_TnSvcEndPointTable_Object((1,3,6,1,4,1,7483,6,1,2,4,2,19))
if mibBuilder.loadTexts:tnSvcEndPointTable.setStatus(_A)
_TnSvcEndPointEntry_Object=MibTableRow
tnSvcEndPointEntry=_TnSvcEndPointEntry_Object((1,3,6,1,4,1,7483,6,1,2,4,2,19,1))
tnSvcEndPointEntry.setIndexNames((0,_K,_L),(0,_F,_N),(0,_F,_A0))
if mibBuilder.loadTexts:tnSvcEndPointEntry.setStatus(_A)
_TnSvcEndPointName_Type=TNamedItem
_TnSvcEndPointName_Object=MibTableColumn
tnSvcEndPointName=_TnSvcEndPointName_Object((1,3,6,1,4,1,7483,6,1,2,4,2,19,1,1),_TnSvcEndPointName_Type())
tnSvcEndPointName.setMaxAccess(_H)
if mibBuilder.loadTexts:tnSvcEndPointName.setStatus(_A)
_TnSvcEndPointRowStatus_Type=RowStatus
_TnSvcEndPointRowStatus_Object=MibTableColumn
tnSvcEndPointRowStatus=_TnSvcEndPointRowStatus_Object((1,3,6,1,4,1,7483,6,1,2,4,2,19,1,2),_TnSvcEndPointRowStatus_Type())
tnSvcEndPointRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSvcEndPointRowStatus.setStatus(_A)
class _TnSvcEndPointDescription_Type(ServObjDesc):defaultValue=OctetString('')
_TnSvcEndPointDescription_Type.__name__=_M
_TnSvcEndPointDescription_Object=MibTableColumn
tnSvcEndPointDescription=_TnSvcEndPointDescription_Object((1,3,6,1,4,1,7483,6,1,2,4,2,19,1,3),_TnSvcEndPointDescription_Type())
tnSvcEndPointDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSvcEndPointDescription.setStatus(_A)
class _TnSvcEndPointRevertTime_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,600))
_TnSvcEndPointRevertTime_Type.__name__=_E
_TnSvcEndPointRevertTime_Object=MibTableColumn
tnSvcEndPointRevertTime=_TnSvcEndPointRevertTime_Object((1,3,6,1,4,1,7483,6,1,2,4,2,19,1,4),_TnSvcEndPointRevertTime_Type())
tnSvcEndPointRevertTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSvcEndPointRevertTime.setStatus(_A)
if mibBuilder.loadTexts:tnSvcEndPointRevertTime.setUnits(_Q)
class _TnSvcEndPointTxActiveType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_O,0),(_T,1),('sdpBind',2)))
_TnSvcEndPointTxActiveType_Type.__name__=_E
_TnSvcEndPointTxActiveType_Object=MibTableColumn
tnSvcEndPointTxActiveType=_TnSvcEndPointTxActiveType_Object((1,3,6,1,4,1,7483,6,1,2,4,2,19,1,5),_TnSvcEndPointTxActiveType_Type())
tnSvcEndPointTxActiveType.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcEndPointTxActiveType.setStatus(_A)
_TnSvcEndPointTxActivePortId_Type=InterfaceIndexOrZero
_TnSvcEndPointTxActivePortId_Object=MibTableColumn
tnSvcEndPointTxActivePortId=_TnSvcEndPointTxActivePortId_Object((1,3,6,1,4,1,7483,6,1,2,4,2,19,1,6),_TnSvcEndPointTxActivePortId_Type())
tnSvcEndPointTxActivePortId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcEndPointTxActivePortId.setStatus(_A)
_TnSvcEndPointTxActiveEncap_Type=TmnxEncapVal
_TnSvcEndPointTxActiveEncap_Object=MibTableColumn
tnSvcEndPointTxActiveEncap=_TnSvcEndPointTxActiveEncap_Object((1,3,6,1,4,1,7483,6,1,2,4,2,19,1,7),_TnSvcEndPointTxActiveEncap_Type())
tnSvcEndPointTxActiveEncap.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcEndPointTxActiveEncap.setStatus(_A)
_TnSvcEndPointTxActiveSdpId_Type=SdpBindId
_TnSvcEndPointTxActiveSdpId_Object=MibTableColumn
tnSvcEndPointTxActiveSdpId=_TnSvcEndPointTxActiveSdpId_Object((1,3,6,1,4,1,7483,6,1,2,4,2,19,1,8),_TnSvcEndPointTxActiveSdpId_Type())
tnSvcEndPointTxActiveSdpId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcEndPointTxActiveSdpId.setStatus(_A)
class _TnSvcEndPointForceSwitchOver_Type(TmnxActionType):defaultValue=2
_TnSvcEndPointForceSwitchOver_Type.__name__=_d
_TnSvcEndPointForceSwitchOver_Object=MibTableColumn
tnSvcEndPointForceSwitchOver=_TnSvcEndPointForceSwitchOver_Object((1,3,6,1,4,1,7483,6,1,2,4,2,19,1,9),_TnSvcEndPointForceSwitchOver_Type())
tnSvcEndPointForceSwitchOver.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSvcEndPointForceSwitchOver.setStatus(_A)
class _TnSvcEndPointForceSwitchOverSdpId_Type(SdpBindId):defaultHexValue='0000000000000000'
_TnSvcEndPointForceSwitchOverSdpId_Type.__name__=_b
_TnSvcEndPointForceSwitchOverSdpId_Object=MibTableColumn
tnSvcEndPointForceSwitchOverSdpId=_TnSvcEndPointForceSwitchOverSdpId_Object((1,3,6,1,4,1,7483,6,1,2,4,2,19,1,10),_TnSvcEndPointForceSwitchOverSdpId_Type())
tnSvcEndPointForceSwitchOverSdpId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSvcEndPointForceSwitchOverSdpId.setStatus(_A)
class _TnSvcEndPointActiveHoldDelay_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_TnSvcEndPointActiveHoldDelay_Type.__name__=_I
_TnSvcEndPointActiveHoldDelay_Object=MibTableColumn
tnSvcEndPointActiveHoldDelay=_TnSvcEndPointActiveHoldDelay_Object((1,3,6,1,4,1,7483,6,1,2,4,2,19,1,11),_TnSvcEndPointActiveHoldDelay_Type())
tnSvcEndPointActiveHoldDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSvcEndPointActiveHoldDelay.setStatus(_A)
if mibBuilder.loadTexts:tnSvcEndPointActiveHoldDelay.setUnits(_x)
class _TnSvcEndPointIgnoreStandbySig_Type(TruthValue):defaultValue=2
_TnSvcEndPointIgnoreStandbySig_Type.__name__=_G
_TnSvcEndPointIgnoreStandbySig_Object=MibTableColumn
tnSvcEndPointIgnoreStandbySig=_TnSvcEndPointIgnoreStandbySig_Object((1,3,6,1,4,1,7483,6,1,2,4,2,19,1,12),_TnSvcEndPointIgnoreStandbySig_Type())
tnSvcEndPointIgnoreStandbySig.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSvcEndPointIgnoreStandbySig.setStatus(_A)
class _TnSvcEndPointMacPinning_Type(TmnxEnabledDisabled):defaultValue=2
_TnSvcEndPointMacPinning_Type.__name__=_J
_TnSvcEndPointMacPinning_Object=MibTableColumn
tnSvcEndPointMacPinning=_TnSvcEndPointMacPinning_Object((1,3,6,1,4,1,7483,6,1,2,4,2,19,1,13),_TnSvcEndPointMacPinning_Type())
tnSvcEndPointMacPinning.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSvcEndPointMacPinning.setStatus(_A)
class _TnSvcEndPointMacLimit_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,511999))
_TnSvcEndPointMacLimit_Type.__name__=_E
_TnSvcEndPointMacLimit_Object=MibTableColumn
tnSvcEndPointMacLimit=_TnSvcEndPointMacLimit_Object((1,3,6,1,4,1,7483,6,1,2,4,2,19,1,14),_TnSvcEndPointMacLimit_Type())
tnSvcEndPointMacLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSvcEndPointMacLimit.setStatus(_A)
class _TnSvcEndPointSuppressStandbySig_Type(TruthValue):defaultValue=1
_TnSvcEndPointSuppressStandbySig_Type.__name__=_G
_TnSvcEndPointSuppressStandbySig_Object=MibTableColumn
tnSvcEndPointSuppressStandbySig=_TnSvcEndPointSuppressStandbySig_Object((1,3,6,1,4,1,7483,6,1,2,4,2,19,1,15),_TnSvcEndPointSuppressStandbySig_Type())
tnSvcEndPointSuppressStandbySig.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSvcEndPointSuppressStandbySig.setStatus(_A)
class _TnSvcEndPointRevertTimeCountDn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,600))
_TnSvcEndPointRevertTimeCountDn_Type.__name__=_E
_TnSvcEndPointRevertTimeCountDn_Object=MibTableColumn
tnSvcEndPointRevertTimeCountDn=_TnSvcEndPointRevertTimeCountDn_Object((1,3,6,1,4,1,7483,6,1,2,4,2,19,1,16),_TnSvcEndPointRevertTimeCountDn_Type())
tnSvcEndPointRevertTimeCountDn.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcEndPointRevertTimeCountDn.setStatus(_A)
if mibBuilder.loadTexts:tnSvcEndPointRevertTimeCountDn.setUnits(_Q)
_TnSvcEndPointTxActiveChangeCount_Type=Counter32
_TnSvcEndPointTxActiveChangeCount_Object=MibTableColumn
tnSvcEndPointTxActiveChangeCount=_TnSvcEndPointTxActiveChangeCount_Object((1,3,6,1,4,1,7483,6,1,2,4,2,19,1,17),_TnSvcEndPointTxActiveChangeCount_Type())
tnSvcEndPointTxActiveChangeCount.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcEndPointTxActiveChangeCount.setStatus(_A)
_TnSvcEndPointTxActiveLastChange_Type=TimeStamp
_TnSvcEndPointTxActiveLastChange_Object=MibTableColumn
tnSvcEndPointTxActiveLastChange=_TnSvcEndPointTxActiveLastChange_Object((1,3,6,1,4,1,7483,6,1,2,4,2,19,1,18),_TnSvcEndPointTxActiveLastChange_Type())
tnSvcEndPointTxActiveLastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcEndPointTxActiveLastChange.setStatus(_A)
_TnSvcEndPointTxActiveUpTime_Type=TimeTicks
_TnSvcEndPointTxActiveUpTime_Object=MibTableColumn
tnSvcEndPointTxActiveUpTime=_TnSvcEndPointTxActiveUpTime_Object((1,3,6,1,4,1,7483,6,1,2,4,2,19,1,19),_TnSvcEndPointTxActiveUpTime_Type())
tnSvcEndPointTxActiveUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcEndPointTxActiveUpTime.setStatus(_A)
class _TnSvcEndPointMCEPId_Type(Unsigned32):defaultValue=0
_TnSvcEndPointMCEPId_Type.__name__=_I
_TnSvcEndPointMCEPId_Object=MibTableColumn
tnSvcEndPointMCEPId=_TnSvcEndPointMCEPId_Object((1,3,6,1,4,1,7483,6,1,2,4,2,19,1,20),_TnSvcEndPointMCEPId_Type())
tnSvcEndPointMCEPId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSvcEndPointMCEPId.setStatus(_A)
class _TnSvcEndPointMCEPPeerAddrType_Type(InetAddressType):defaultValue=0
_TnSvcEndPointMCEPPeerAddrType_Type.__name__=_Z
_TnSvcEndPointMCEPPeerAddrType_Object=MibTableColumn
tnSvcEndPointMCEPPeerAddrType=_TnSvcEndPointMCEPPeerAddrType_Object((1,3,6,1,4,1,7483,6,1,2,4,2,19,1,21),_TnSvcEndPointMCEPPeerAddrType_Type())
tnSvcEndPointMCEPPeerAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSvcEndPointMCEPPeerAddrType.setStatus(_A)
class _TnSvcEndPointMCEPPeerAddr_Type(InetAddress):defaultHexValue=''
_TnSvcEndPointMCEPPeerAddr_Type.__name__=_R
_TnSvcEndPointMCEPPeerAddr_Object=MibTableColumn
tnSvcEndPointMCEPPeerAddr=_TnSvcEndPointMCEPPeerAddr_Object((1,3,6,1,4,1,7483,6,1,2,4,2,19,1,22),_TnSvcEndPointMCEPPeerAddr_Type())
tnSvcEndPointMCEPPeerAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSvcEndPointMCEPPeerAddr.setStatus(_A)
class _TnSvcEndPointMCEPPeerName_Type(TNamedItemOrEmpty):defaultHexValue=''
_TnSvcEndPointMCEPPeerName_Type.__name__=_P
_TnSvcEndPointMCEPPeerName_Object=MibTableColumn
tnSvcEndPointMCEPPeerName=_TnSvcEndPointMCEPPeerName_Object((1,3,6,1,4,1,7483,6,1,2,4,2,19,1,23),_TnSvcEndPointMCEPPeerName_Type())
tnSvcEndPointMCEPPeerName.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSvcEndPointMCEPPeerName.setStatus(_A)
class _TnSvcEndPointBlockOnMeshFail_Type(TruthValue):defaultValue=2
_TnSvcEndPointBlockOnMeshFail_Type.__name__=_G
_TnSvcEndPointBlockOnMeshFail_Object=MibTableColumn
tnSvcEndPointBlockOnMeshFail=_TnSvcEndPointBlockOnMeshFail_Object((1,3,6,1,4,1,7483,6,1,2,4,2,19,1,24),_TnSvcEndPointBlockOnMeshFail_Type())
tnSvcEndPointBlockOnMeshFail.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSvcEndPointBlockOnMeshFail.setStatus(_A)
_TnSvcEndPointMCEPPsvModeActive_Type=TruthValue
_TnSvcEndPointMCEPPsvModeActive_Object=MibTableColumn
tnSvcEndPointMCEPPsvModeActive=_TnSvcEndPointMCEPPsvModeActive_Object((1,3,6,1,4,1,7483,6,1,2,4,2,19,1,25),_TnSvcEndPointMCEPPsvModeActive_Type())
tnSvcEndPointMCEPPsvModeActive.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcEndPointMCEPPsvModeActive.setStatus(_A)
class _TnSvcEndPointStandbySigMaster_Type(TruthValue):defaultValue=2
_TnSvcEndPointStandbySigMaster_Type.__name__=_G
_TnSvcEndPointStandbySigMaster_Object=MibTableColumn
tnSvcEndPointStandbySigMaster=_TnSvcEndPointStandbySigMaster_Object((1,3,6,1,4,1,7483,6,1,2,4,2,19,1,26),_TnSvcEndPointStandbySigMaster_Type())
tnSvcEndPointStandbySigMaster.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSvcEndPointStandbySigMaster.setStatus(_A)
_TnSvcTlsBackboneInfoTable_Object=MibTable
tnSvcTlsBackboneInfoTable=_TnSvcTlsBackboneInfoTable_Object((1,3,6,1,4,1,7483,6,1,2,4,2,27))
if mibBuilder.loadTexts:tnSvcTlsBackboneInfoTable.setStatus(_A)
_TnSvcTlsBackboneInfoEntry_Object=MibTableRow
tnSvcTlsBackboneInfoEntry=_TnSvcTlsBackboneInfoEntry_Object((1,3,6,1,4,1,7483,6,1,2,4,2,27,1))
if mibBuilder.loadTexts:tnSvcTlsBackboneInfoEntry.setStatus(_A)
class _TnSvcTlsBackboneSrcMac_Type(MacAddress):defaultHexValue='000000000000'
_TnSvcTlsBackboneSrcMac_Type.__name__=_a
_TnSvcTlsBackboneSrcMac_Object=MibTableColumn
tnSvcTlsBackboneSrcMac=_TnSvcTlsBackboneSrcMac_Object((1,3,6,1,4,1,7483,6,1,2,4,2,27,1,1),_TnSvcTlsBackboneSrcMac_Type())
tnSvcTlsBackboneSrcMac.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSvcTlsBackboneSrcMac.setStatus(_A)
class _TnSvcTlsBackboneVplsSvcId_Type(TmnxServId):defaultValue=0
_TnSvcTlsBackboneVplsSvcId_Type.__name__=_e
_TnSvcTlsBackboneVplsSvcId_Object=MibTableColumn
tnSvcTlsBackboneVplsSvcId=_TnSvcTlsBackboneVplsSvcId_Object((1,3,6,1,4,1,7483,6,1,2,4,2,27,1,2),_TnSvcTlsBackboneVplsSvcId_Type())
tnSvcTlsBackboneVplsSvcId.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSvcTlsBackboneVplsSvcId.setStatus(_A)
class _TnSvcTlsBackboneVplsSvcISID_Type(SvcISID):defaultValue=-1
_TnSvcTlsBackboneVplsSvcISID_Type.__name__='SvcISID'
_TnSvcTlsBackboneVplsSvcISID_Object=MibTableColumn
tnSvcTlsBackboneVplsSvcISID=_TnSvcTlsBackboneVplsSvcISID_Object((1,3,6,1,4,1,7483,6,1,2,4,2,27,1,3),_TnSvcTlsBackboneVplsSvcISID_Type())
tnSvcTlsBackboneVplsSvcISID.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSvcTlsBackboneVplsSvcISID.setStatus(_A)
_TnSvcTlsBackboneOperSrcMac_Type=MacAddress
_TnSvcTlsBackboneOperSrcMac_Object=MibTableColumn
tnSvcTlsBackboneOperSrcMac=_TnSvcTlsBackboneOperSrcMac_Object((1,3,6,1,4,1,7483,6,1,2,4,2,27,1,4),_TnSvcTlsBackboneOperSrcMac_Type())
tnSvcTlsBackboneOperSrcMac.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcTlsBackboneOperSrcMac.setStatus(_A)
_TnSvcTlsBackboneOperVplsSvcISID_Type=SvcISID
_TnSvcTlsBackboneOperVplsSvcISID_Object=MibTableColumn
tnSvcTlsBackboneOperVplsSvcISID=_TnSvcTlsBackboneOperVplsSvcISID_Object((1,3,6,1,4,1,7483,6,1,2,4,2,27,1,5),_TnSvcTlsBackboneOperVplsSvcISID_Type())
tnSvcTlsBackboneOperVplsSvcISID.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcTlsBackboneOperVplsSvcISID.setStatus(_A)
class _TnSvcTlsBackboneLDPMacFlush_Type(TruthValue):defaultValue=2
_TnSvcTlsBackboneLDPMacFlush_Type.__name__=_G
_TnSvcTlsBackboneLDPMacFlush_Object=MibTableColumn
tnSvcTlsBackboneLDPMacFlush=_TnSvcTlsBackboneLDPMacFlush_Object((1,3,6,1,4,1,7483,6,1,2,4,2,27,1,6),_TnSvcTlsBackboneLDPMacFlush_Type())
tnSvcTlsBackboneLDPMacFlush.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSvcTlsBackboneLDPMacFlush.setStatus(_A)
class _TnSvcTlsBackboneVplsStp_Type(TmnxEnabledDisabled):defaultValue=2
_TnSvcTlsBackboneVplsStp_Type.__name__=_J
_TnSvcTlsBackboneVplsStp_Object=MibTableColumn
tnSvcTlsBackboneVplsStp=_TnSvcTlsBackboneVplsStp_Object((1,3,6,1,4,1,7483,6,1,2,4,2,27,1,7),_TnSvcTlsBackboneVplsStp_Type())
tnSvcTlsBackboneVplsStp.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSvcTlsBackboneVplsStp.setStatus(_A)
class _TnSvcTlsBackboneLDPMacFlushNotMine_Type(TruthValue):defaultValue=2
_TnSvcTlsBackboneLDPMacFlushNotMine_Type.__name__=_G
_TnSvcTlsBackboneLDPMacFlushNotMine_Object=MibTableColumn
tnSvcTlsBackboneLDPMacFlushNotMine=_TnSvcTlsBackboneLDPMacFlushNotMine_Object((1,3,6,1,4,1,7483,6,1,2,4,2,27,1,8),_TnSvcTlsBackboneLDPMacFlushNotMine_Type())
tnSvcTlsBackboneLDPMacFlushNotMine.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSvcTlsBackboneLDPMacFlushNotMine.setStatus(_A)
class _TnSvcTlsBackboneUseSapBMac_Type(TruthValue):defaultValue=2
_TnSvcTlsBackboneUseSapBMac_Type.__name__=_G
_TnSvcTlsBackboneUseSapBMac_Object=MibTableColumn
tnSvcTlsBackboneUseSapBMac=_TnSvcTlsBackboneUseSapBMac_Object((1,3,6,1,4,1,7483,6,1,2,4,2,27,1,9),_TnSvcTlsBackboneUseSapBMac_Type())
tnSvcTlsBackboneUseSapBMac.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSvcTlsBackboneUseSapBMac.setStatus(_A)
_TnTlsMFibTable_Object=MibTable
tnTlsMFibTable=_TnTlsMFibTable_Object((1,3,6,1,4,1,7483,6,1,2,4,2,28))
if mibBuilder.loadTexts:tnTlsMFibTable.setStatus(_A)
_TnTlsMFibEntry_Object=MibTableRow
tnTlsMFibEntry=_TnTlsMFibEntry_Object((1,3,6,1,4,1,7483,6,1,2,4,2,28,1))
tnTlsMFibEntry.setIndexNames((0,_K,_L),(0,_F,_N),(0,_F,_A1),(0,_F,_A2),(0,_F,_A3),(0,_F,_A4),(0,_F,_A5),(0,_F,_A6),(0,_F,_A7),(0,_F,_A8),(0,_F,_A9),(0,_F,_AA),(0,_F,_AB))
if mibBuilder.loadTexts:tnTlsMFibEntry.setStatus(_A)
class _TnTlsMFibEntryType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ipBased',1),('macBased',2)))
_TnTlsMFibEntryType_Type.__name__=_E
_TnTlsMFibEntryType_Object=MibTableColumn
tnTlsMFibEntryType=_TnTlsMFibEntryType_Object((1,3,6,1,4,1,7483,6,1,2,4,2,28,1,1),_TnTlsMFibEntryType_Type())
tnTlsMFibEntryType.setMaxAccess(_H)
if mibBuilder.loadTexts:tnTlsMFibEntryType.setStatus(_A)
_TnTlsMFibGrpMacAddr_Type=MacAddress
_TnTlsMFibGrpMacAddr_Object=MibTableColumn
tnTlsMFibGrpMacAddr=_TnTlsMFibGrpMacAddr_Object((1,3,6,1,4,1,7483,6,1,2,4,2,28,1,2),_TnTlsMFibGrpMacAddr_Type())
tnTlsMFibGrpMacAddr.setMaxAccess(_H)
if mibBuilder.loadTexts:tnTlsMFibGrpMacAddr.setStatus(_A)
_TnTlsMFibGrpInetAddrType_Type=InetAddressType
_TnTlsMFibGrpInetAddrType_Object=MibTableColumn
tnTlsMFibGrpInetAddrType=_TnTlsMFibGrpInetAddrType_Object((1,3,6,1,4,1,7483,6,1,2,4,2,28,1,3),_TnTlsMFibGrpInetAddrType_Type())
tnTlsMFibGrpInetAddrType.setMaxAccess(_H)
if mibBuilder.loadTexts:tnTlsMFibGrpInetAddrType.setStatus(_A)
class _TnTlsMFibGrpInetAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_TnTlsMFibGrpInetAddr_Type.__name__=_R
_TnTlsMFibGrpInetAddr_Object=MibTableColumn
tnTlsMFibGrpInetAddr=_TnTlsMFibGrpInetAddr_Object((1,3,6,1,4,1,7483,6,1,2,4,2,28,1,4),_TnTlsMFibGrpInetAddr_Type())
tnTlsMFibGrpInetAddr.setMaxAccess(_H)
if mibBuilder.loadTexts:tnTlsMFibGrpInetAddr.setStatus(_A)
_TnTlsMFibSrcInetAddrType_Type=InetAddressType
_TnTlsMFibSrcInetAddrType_Object=MibTableColumn
tnTlsMFibSrcInetAddrType=_TnTlsMFibSrcInetAddrType_Object((1,3,6,1,4,1,7483,6,1,2,4,2,28,1,5),_TnTlsMFibSrcInetAddrType_Type())
tnTlsMFibSrcInetAddrType.setMaxAccess(_H)
if mibBuilder.loadTexts:tnTlsMFibSrcInetAddrType.setStatus(_A)
class _TnTlsMFibSrcInetAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_TnTlsMFibSrcInetAddr_Type.__name__=_R
_TnTlsMFibSrcInetAddr_Object=MibTableColumn
tnTlsMFibSrcInetAddr=_TnTlsMFibSrcInetAddr_Object((1,3,6,1,4,1,7483,6,1,2,4,2,28,1,6),_TnTlsMFibSrcInetAddr_Type())
tnTlsMFibSrcInetAddr.setMaxAccess(_H)
if mibBuilder.loadTexts:tnTlsMFibSrcInetAddr.setStatus(_A)
_TnTlsMFibLocale_Type=MfibLocation
_TnTlsMFibLocale_Object=MibTableColumn
tnTlsMFibLocale=_TnTlsMFibLocale_Object((1,3,6,1,4,1,7483,6,1,2,4,2,28,1,7),_TnTlsMFibLocale_Type())
tnTlsMFibLocale.setMaxAccess(_H)
if mibBuilder.loadTexts:tnTlsMFibLocale.setStatus(_A)
_TnTlsMFibPortId_Type=TmnxPortID
_TnTlsMFibPortId_Object=MibTableColumn
tnTlsMFibPortId=_TnTlsMFibPortId_Object((1,3,6,1,4,1,7483,6,1,2,4,2,28,1,8),_TnTlsMFibPortId_Type())
tnTlsMFibPortId.setMaxAccess(_H)
if mibBuilder.loadTexts:tnTlsMFibPortId.setStatus(_A)
_TnTlsMFibEncapValue_Type=TmnxEncapVal
_TnTlsMFibEncapValue_Object=MibTableColumn
tnTlsMFibEncapValue=_TnTlsMFibEncapValue_Object((1,3,6,1,4,1,7483,6,1,2,4,2,28,1,9),_TnTlsMFibEncapValue_Type())
tnTlsMFibEncapValue.setMaxAccess(_H)
if mibBuilder.loadTexts:tnTlsMFibEncapValue.setStatus(_A)
_TnTlsMFibSdpId_Type=SdpId
_TnTlsMFibSdpId_Object=MibTableColumn
tnTlsMFibSdpId=_TnTlsMFibSdpId_Object((1,3,6,1,4,1,7483,6,1,2,4,2,28,1,10),_TnTlsMFibSdpId_Type())
tnTlsMFibSdpId.setMaxAccess(_H)
if mibBuilder.loadTexts:tnTlsMFibSdpId.setStatus(_A)
_TnTlsMFibVcId_Type=Unsigned32
_TnTlsMFibVcId_Object=MibTableColumn
tnTlsMFibVcId=_TnTlsMFibVcId_Object((1,3,6,1,4,1,7483,6,1,2,4,2,28,1,11),_TnTlsMFibVcId_Type())
tnTlsMFibVcId.setMaxAccess(_H)
if mibBuilder.loadTexts:tnTlsMFibVcId.setStatus(_A)
_TnTlsMFibFwdOrBlk_Type=MfibGrpSrcFwdOrBlk
_TnTlsMFibFwdOrBlk_Object=MibTableColumn
tnTlsMFibFwdOrBlk=_TnTlsMFibFwdOrBlk_Object((1,3,6,1,4,1,7483,6,1,2,4,2,28,1,12),_TnTlsMFibFwdOrBlk_Type())
tnTlsMFibFwdOrBlk.setMaxAccess(_B)
if mibBuilder.loadTexts:tnTlsMFibFwdOrBlk.setStatus(_A)
_TnTlsMFibSvcId_Type=TmnxServId
_TnTlsMFibSvcId_Object=MibTableColumn
tnTlsMFibSvcId=_TnTlsMFibSvcId_Object((1,3,6,1,4,1,7483,6,1,2,4,2,28,1,13),_TnTlsMFibSvcId_Type())
tnTlsMFibSvcId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnTlsMFibSvcId.setStatus(_A)
_TnSvcTlsBgpADTableLastChanged_Type=TimeStamp
_TnSvcTlsBgpADTableLastChanged_Object=MibScalar
tnSvcTlsBgpADTableLastChanged=_TnSvcTlsBgpADTableLastChanged_Object((1,3,6,1,4,1,7483,6,1,2,4,2,30),_TnSvcTlsBgpADTableLastChanged_Type())
tnSvcTlsBgpADTableLastChanged.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcTlsBgpADTableLastChanged.setStatus(_A)
_TnSvcEpipePbbTableLastChanged_Type=TimeStamp
_TnSvcEpipePbbTableLastChanged_Object=MibScalar
tnSvcEpipePbbTableLastChanged=_TnSvcEpipePbbTableLastChanged_Object((1,3,6,1,4,1,7483,6,1,2,4,2,36),_TnSvcEpipePbbTableLastChanged_Type())
tnSvcEpipePbbTableLastChanged.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcEpipePbbTableLastChanged.setStatus(_A)
_TnSvcTotalFdbMimDestIdxEntries_Type=Unsigned32
_TnSvcTotalFdbMimDestIdxEntries_Object=MibScalar
tnSvcTotalFdbMimDestIdxEntries=_TnSvcTotalFdbMimDestIdxEntries_Object((1,3,6,1,4,1,7483,6,1,2,4,2,42),_TnSvcTotalFdbMimDestIdxEntries_Type())
tnSvcTotalFdbMimDestIdxEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcTotalFdbMimDestIdxEntries.setStatus(_A)
_TnSvcArpHostTableLastChanged_Type=TimeStamp
_TnSvcArpHostTableLastChanged_Object=MibScalar
tnSvcArpHostTableLastChanged=_TnSvcArpHostTableLastChanged_Object((1,3,6,1,4,1,7483,6,1,2,4,2,44),_TnSvcArpHostTableLastChanged_Type())
tnSvcArpHostTableLastChanged.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcArpHostTableLastChanged.setStatus(_A)
_TnSvcArpHostIfTableLastMgmtChange_Type=TimeStamp
_TnSvcArpHostIfTableLastMgmtChange_Object=MibScalar
tnSvcArpHostIfTableLastMgmtChange=_TnSvcArpHostIfTableLastMgmtChange_Object((1,3,6,1,4,1,7483,6,1,2,4,2,46),_TnSvcArpHostIfTableLastMgmtChange_Type())
tnSvcArpHostIfTableLastMgmtChange.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcArpHostIfTableLastMgmtChange.setStatus(_A)
_TnSvcArpHostDefaultSessionTimeout_Type=Unsigned32
_TnSvcArpHostDefaultSessionTimeout_Object=MibScalar
tnSvcArpHostDefaultSessionTimeout=_TnSvcArpHostDefaultSessionTimeout_Object((1,3,6,1,4,1,7483,6,1,2,4,2,48),_TnSvcArpHostDefaultSessionTimeout_Type())
tnSvcArpHostDefaultSessionTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcArpHostDefaultSessionTimeout.setStatus(_A)
if mibBuilder.loadTexts:tnSvcArpHostDefaultSessionTimeout.setUnits(_Q)
_TnSvcIgmpTrkTableLastMgmtChange_Type=TimeStamp
_TnSvcIgmpTrkTableLastMgmtChange_Object=MibScalar
tnSvcIgmpTrkTableLastMgmtChange=_TnSvcIgmpTrkTableLastMgmtChange_Object((1,3,6,1,4,1,7483,6,1,2,4,2,49),_TnSvcIgmpTrkTableLastMgmtChange_Type())
tnSvcIgmpTrkTableLastMgmtChange.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcIgmpTrkTableLastMgmtChange.setStatus(_A)
_TnSvcIpipeInfoTableLastMgmtChange_Type=TimeStamp
_TnSvcIpipeInfoTableLastMgmtChange_Object=MibScalar
tnSvcIpipeInfoTableLastMgmtChange=_TnSvcIpipeInfoTableLastMgmtChange_Object((1,3,6,1,4,1,7483,6,1,2,4,2,51),_TnSvcIpipeInfoTableLastMgmtChange_Type())
tnSvcIpipeInfoTableLastMgmtChange.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcIpipeInfoTableLastMgmtChange.setStatus(_A)
_TnSvcMacNameTableLastChanged_Type=TimeStamp
_TnSvcMacNameTableLastChanged_Object=MibScalar
tnSvcMacNameTableLastChanged=_TnSvcMacNameTableLastChanged_Object((1,3,6,1,4,1,7483,6,1,2,4,2,58),_TnSvcMacNameTableLastChanged_Type())
tnSvcMacNameTableLastChanged.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcMacNameTableLastChanged.setStatus(_A)
_TnSvcScalar1_Type=Unsigned32
_TnSvcScalar1_Object=MibScalar
tnSvcScalar1=_TnSvcScalar1_Object((1,3,6,1,4,1,7483,6,1,2,4,2,101),_TnSvcScalar1_Type())
tnSvcScalar1.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcScalar1.setStatus(_A)
_TnSvcScalar2_Type=Unsigned32
_TnSvcScalar2_Object=MibScalar
tnSvcScalar2=_TnSvcScalar2_Object((1,3,6,1,4,1,7483,6,1,2,4,2,102),_TnSvcScalar2_Type())
tnSvcScalar2.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcScalar2.setStatus(_A)
_TnSvcScalar3_Type=Unsigned32
_TnSvcScalar3_Object=MibScalar
tnSvcScalar3=_TnSvcScalar3_Object((1,3,6,1,4,1,7483,6,1,2,4,2,103),_TnSvcScalar3_Type())
tnSvcScalar3.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcScalar3.setStatus(_A)
_TnSvcScalar4_Type=Unsigned32
_TnSvcScalar4_Object=MibScalar
tnSvcScalar4=_TnSvcScalar4_Object((1,3,6,1,4,1,7483,6,1,2,4,2,104),_TnSvcScalar4_Type())
tnSvcScalar4.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcScalar4.setStatus(_A)
_TnSvcScalar5_Type=Unsigned32
_TnSvcScalar5_Object=MibScalar
tnSvcScalar5=_TnSvcScalar5_Object((1,3,6,1,4,1,7483,6,1,2,4,2,105),_TnSvcScalar5_Type())
tnSvcScalar5.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSvcScalar5.setStatus(_A)
_TnServNotifications_ObjectIdentity=ObjectIdentity
tnServNotifications=_TnServNotifications_ObjectIdentity((1,3,6,1,4,1,7483,6,1,3,4))
_TnCustTrapsPrefix_ObjectIdentity=ObjectIdentity
tnCustTrapsPrefix=_TnCustTrapsPrefix_ObjectIdentity((1,3,6,1,4,1,7483,6,1,3,4,1))
_TnCustTraps_ObjectIdentity=ObjectIdentity
tnCustTraps=_TnCustTraps_ObjectIdentity((1,3,6,1,4,1,7483,6,1,3,4,1,0))
_TnSvcTrapsPrefix_ObjectIdentity=ObjectIdentity
tnSvcTrapsPrefix=_TnSvcTrapsPrefix_ObjectIdentity((1,3,6,1,4,1,7483,6,1,3,4,2))
_TnSvcTraps_ObjectIdentity=ObjectIdentity
tnSvcTraps=_TnSvcTraps_ObjectIdentity((1,3,6,1,4,1,7483,6,1,3,4,2,0))
_TnTstpTrapsPrefix_ObjectIdentity=ObjectIdentity
tnTstpTrapsPrefix=_TnTstpTrapsPrefix_ObjectIdentity((1,3,6,1,4,1,7483,6,1,3,4,5))
_TnTstpTraps_ObjectIdentity=ObjectIdentity
tnTstpTraps=_TnTstpTraps_ObjectIdentity((1,3,6,1,4,1,7483,6,1,3,4,5,0))
tnSvcTlsInfoEntry.registerAugmentions((_F,_AC))
tnSvcTlsBackboneInfoEntry.setIndexNames(*tnSvcTlsInfoEntry.getIndexNames())
mibBuilder.exportSymbols(_F,**{'ServObjName':ServObjName,'ServObjLongDesc':ServObjLongDesc,'ServType':ServType,'VpnId':VpnId,'SdpId':SdpId,'PWTemplateId':PWTemplateId,'TlsBpduTranslation':TlsBpduTranslation,'TlsLimitMacMoveLevel':TlsLimitMacMoveLevel,'TlsLimitMacMove':TlsLimitMacMove,'SdpBindVcType':SdpBindVcType,'StpExceptionCondition':StpExceptionCondition,'LspIdList':LspIdList,'BridgeId':BridgeId,'TSapIngQueueId':TSapIngQueueId,'TStpPortState':TStpPortState,'StpPortRole':StpPortRole,'StpProtocol':StpProtocol,'MfibLocation':MfibLocation,'MfibGrpSrcFwdOrBlk':MfibGrpSrcFwdOrBlk,'MvplsPruneState':MvplsPruneState,'MstiInstanceId':MstiInstanceId,'MstiInstanceIdOrZero':MstiInstanceIdOrZero,'DhcpLseStateInfoOrigin':DhcpLseStateInfoOrigin,'IAIDType':IAIDType,'TdmOptionsSigPkts':TdmOptionsSigPkts,'TdmOptionsCasTrunkFraming':TdmOptionsCasTrunkFraming,'SdpBindBandwidth':SdpBindBandwidth,'L2ptProtocols':L2ptProtocols,'SvcISID':SvcISID,'L2RouteOrigin':L2RouteOrigin,'ConfigStatus':ConfigStatus,'ServAccessLocation':ServAccessLocation,'ServShcvOperState':ServShcvOperState,'tnServicesMIBModule':tnServicesMIBModule,'tnServObjs':tnServObjs,'tnCustObjs':tnCustObjs,'tnCustNumEntries':tnCustNumEntries,'tnCustNextFreeId':tnCustNextFreeId,'tnCustInfoTable':tnCustInfoTable,'tnCustInfoEntry':tnCustInfoEntry,_w:tnCustId,'tnCustRowStatus':tnCustRowStatus,'tnCustDescription':tnCustDescription,'tnCustContact':tnCustContact,'tnCustPhone':tnCustPhone,'tnCustLastMgmtChange':tnCustLastMgmtChange,'tnSvcObjs':tnSvcObjs,'tnSvcNumEntries':tnSvcNumEntries,'tnSvcBaseInfoTable':tnSvcBaseInfoTable,'tnSvcBaseInfoEntry':tnSvcBaseInfoEntry,_N:tnSvcId,'tnSvcRowStatus':tnSvcRowStatus,'tnSvcType':tnSvcType,'tnSvcCustId':tnSvcCustId,'tnSvcIpRouting':tnSvcIpRouting,'tnSvcDescription':tnSvcDescription,'tnSvcMtu':tnSvcMtu,'tnSvcAdminStatus':tnSvcAdminStatus,'tnSvcOperStatus':tnSvcOperStatus,'tnSvcNumSaps':tnSvcNumSaps,'tnSvcNumSdps':tnSvcNumSdps,'tnSvcLastMgmtChange':tnSvcLastMgmtChange,'tnSvcDefMeshVcId':tnSvcDefMeshVcId,'tnSvcVpnId':tnSvcVpnId,'tnSvcVRouterId':tnSvcVRouterId,'tnSvcAutoBind':tnSvcAutoBind,'tnSvcLastStatusChange':tnSvcLastStatusChange,'tnSvcVllType':tnSvcVllType,'tnSvcMgmtVpls':tnSvcMgmtVpls,'tnSvcRadiusDiscovery':tnSvcRadiusDiscovery,'tnSvcRadiusUserNameType':tnSvcRadiusUserNameType,'tnSvcRadiusUserName':tnSvcRadiusUserName,'tnSvcVcSwitching':tnSvcVcSwitching,'tnSvcRadiusPEDiscPolicy':tnSvcRadiusPEDiscPolicy,'tnSvcRadiusDiscoveryShutdown':tnSvcRadiusDiscoveryShutdown,'tnSvcVplsType':tnSvcVplsType,'tnSvcNumMcStandbySaps':tnSvcNumMcStandbySaps,'tnSvcName':tnSvcName,'tnsvcEpipeAllowIpIfBinding':tnsvcEpipeAllowIpIfBinding,'tnSvcAlmProfName':tnSvcAlmProfName,'tnSvcTlsInfoTable':tnSvcTlsInfoTable,'tnSvcTlsInfoEntry':tnSvcTlsInfoEntry,'tnSvcTlsMacLearning':tnSvcTlsMacLearning,'tnSvcTlsDiscardUnknownDest':tnSvcTlsDiscardUnknownDest,'tnSvcTlsFdbTableSize':tnSvcTlsFdbTableSize,'tnSvcTlsFdbNumEntries':tnSvcTlsFdbNumEntries,'tnSvcTlsFdbNumStaticEntries':tnSvcTlsFdbNumStaticEntries,'tnSvcTlsFdbLocalAgeTime':tnSvcTlsFdbLocalAgeTime,'tnSvcTlsFdbRemoteAgeTime':tnSvcTlsFdbRemoteAgeTime,'tnSvcTlsStpAdminStatus':tnSvcTlsStpAdminStatus,'tnSvcTlsStpPriority':tnSvcTlsStpPriority,'tnSvcTlsStpBridgeAddress':tnSvcTlsStpBridgeAddress,'tnSvcTlsStpTimeSinceTopologyChange':tnSvcTlsStpTimeSinceTopologyChange,'tnSvcTlsStpTopologyChanges':tnSvcTlsStpTopologyChanges,'tnSvcTlsStpDesignatedRoot':tnSvcTlsStpDesignatedRoot,'tnSvcTlsStpRootCost':tnSvcTlsStpRootCost,'tnSvcTlsStpRootPort':tnSvcTlsStpRootPort,'tnSvcTlsStpMaxAge':tnSvcTlsStpMaxAge,'tnSvcTlsStpHelloTime':tnSvcTlsStpHelloTime,'tnSvcTlsStpForwardDelay':tnSvcTlsStpForwardDelay,'tnSvcTlsStpBridgeMaxAge':tnSvcTlsStpBridgeMaxAge,'tnSvcTlsStpBridgeHelloTime':tnSvcTlsStpBridgeHelloTime,'tnSvcTlsStpBridgeForwardDelay':tnSvcTlsStpBridgeForwardDelay,'tnSvcTlsStpOperStatus':tnSvcTlsStpOperStatus,'tnSvcTlsStpVirtualRootBridgeStatus':tnSvcTlsStpVirtualRootBridgeStatus,'tnSvcTlsMacAgeing':tnSvcTlsMacAgeing,'tnSvcTlsStpTopologyChangeActive':tnSvcTlsStpTopologyChangeActive,'tnSvcTlsFdbTableFullHighWatermark':tnSvcTlsFdbTableFullHighWatermark,'tnSvcTlsFdbTableFullLowWatermark':tnSvcTlsFdbTableFullLowWatermark,'tnSvcTlsVpnId':tnSvcTlsVpnId,'tnSvcTlsCustId':tnSvcTlsCustId,'tnSvcTlsStpVersion':tnSvcTlsStpVersion,'tnSvcTlsStpHoldCount':tnSvcTlsStpHoldCount,'tnSvcTlsStpPrimaryBridge':tnSvcTlsStpPrimaryBridge,'tnSvcTlsStpBridgeInstanceId':tnSvcTlsStpBridgeInstanceId,'tnSvcTlsStpVcpOperProtocol':tnSvcTlsStpVcpOperProtocol,'tnSvcTlsMacMoveMaxRate':tnSvcTlsMacMoveMaxRate,'tnSvcTlsMacMoveRetryTimeout':tnSvcTlsMacMoveRetryTimeout,'tnSvcTlsMacMoveAdminStatus':tnSvcTlsMacMoveAdminStatus,'tnSvcTlsMacRelearnOnly':tnSvcTlsMacRelearnOnly,'tnSvcTlsMfibTableSize':tnSvcTlsMfibTableSize,'tnSvcTlsMfibTableFullHighWatermark':tnSvcTlsMfibTableFullHighWatermark,'tnSvcTlsMfibTableFullLowWatermark':tnSvcTlsMfibTableFullLowWatermark,'tnSvcTlsMacFlushOnFail':tnSvcTlsMacFlushOnFail,'tnSvcTlsStpRegionName':tnSvcTlsStpRegionName,'tnSvcTlsStpRegionRevision':tnSvcTlsStpRegionRevision,'tnSvcTlsStpBridgeMaxHops':tnSvcTlsStpBridgeMaxHops,'tnSvcTlsStpCistRegionalRoot':tnSvcTlsStpCistRegionalRoot,'tnSvcTlsStpCistIntRootCost':tnSvcTlsStpCistIntRootCost,'tnSvcTlsStpCistRemainingHopCount':tnSvcTlsStpCistRemainingHopCount,'tnSvcTlsStpCistRegionalRootPort':tnSvcTlsStpCistRegionalRootPort,'tnSvcTlsFdbNumLearnedEntries':tnSvcTlsFdbNumLearnedEntries,'tnSvcTlsFdbNumOamEntries':tnSvcTlsFdbNumOamEntries,'tnSvcTlsFdbNumDhcpEntries':tnSvcTlsFdbNumDhcpEntries,'tnSvcTlsFdbNumHostEntries':tnSvcTlsFdbNumHostEntries,'tnSvcTlsShcvAction':tnSvcTlsShcvAction,'tnSvcTlsShcvSrcIp':tnSvcTlsShcvSrcIp,'tnSvcTlsShcvSrcMac':tnSvcTlsShcvSrcMac,'tnSvcTlsShcvInterval':tnSvcTlsShcvInterval,'tnSvcTlsPriPortsCumulativeFactor':tnSvcTlsPriPortsCumulativeFactor,'tnSvcTlsSecPortsCumulativeFactor':tnSvcTlsSecPortsCumulativeFactor,'tnSvcTlsL2ptTermEnabled':tnSvcTlsL2ptTermEnabled,'tnSvcTlsPropagateMacFlush':tnSvcTlsPropagateMacFlush,'tnSvcTlsMrpAdminStatus':tnSvcTlsMrpAdminStatus,'tnSvcTlsMrpMaxAttributes':tnSvcTlsMrpMaxAttributes,'tnSvcTlsMrpAttributeCount':tnSvcTlsMrpAttributeCount,'tnSvcTlsMrpFailedRegisterCount':tnSvcTlsMrpFailedRegisterCount,'tnSvcTlsMcPathMgmtPlcyName':tnSvcTlsMcPathMgmtPlcyName,'tnSvcTlsMrpFloodTime':tnSvcTlsMrpFloodTime,'tnSvcTlsMrpAttrTblHighWatermark':tnSvcTlsMrpAttrTblHighWatermark,'tnSvcTlsMrpAttrTblLowWatermark':tnSvcTlsMrpAttrTblLowWatermark,'tnSvcTlsMacMoveNumRetries':tnSvcTlsMacMoveNumRetries,'tnSvcTlsMacSubNetLen':tnSvcTlsMacSubNetLen,'tnSvcTlsSendFlushOnBVplsFail':tnSvcTlsSendFlushOnBVplsFail,'tnSvcTlsPropMacFlushFromBVpls':tnSvcTlsPropMacFlushFromBVpls,'tnSvcTlsMacNotifInterval':tnSvcTlsMacNotifInterval,'tnSvcTlsMacNotifCount':tnSvcTlsMacNotifCount,'tnSvcTlsMacNotifAdminState':tnSvcTlsMacNotifAdminState,'tnSvcTlsShcvRetryTimeout':tnSvcTlsShcvRetryTimeout,'tnSvcTlsShcvRetryCount':tnSvcTlsShcvRetryCount,'tnsvcTlsAllowIpIfBinding':tnsvcTlsAllowIpIfBinding,'tnSvcTlsMfibTableNumEntries':tnSvcTlsMfibTableNumEntries,'tnTlsFdbInfoTable':tnTlsFdbInfoTable,'tnTlsFdbInfoEntry':tnTlsFdbInfoEntry,_y:tnTlsFdbMacAddr,'tnTlsFdbRowStatus':tnTlsFdbRowStatus,'tnTlsFdbType':tnTlsFdbType,'tnTlsFdbLocale':tnTlsFdbLocale,'tnTlsFdbPortId':tnTlsFdbPortId,'tnTlsFdbEncapValue':tnTlsFdbEncapValue,'tnTlsFdbSdpId':tnTlsFdbSdpId,'tnTlsFdbVcId':tnTlsFdbVcId,'tnTlsFdbVpnId':tnTlsFdbVpnId,'tnTlsFdbCustId':tnTlsFdbCustId,'tnTlsFdbLastStateChange':tnTlsFdbLastStateChange,'tnTlsFdbProtected':tnTlsFdbProtected,'tnTlsFdbBackboneDstMac':tnTlsFdbBackboneDstMac,'tnTlsFdbNumIVplsMac':tnTlsFdbNumIVplsMac,'tnTlsFdbEndPointName':tnTlsFdbEndPointName,'tnTlsFdbEPMacOperSdpId':tnTlsFdbEPMacOperSdpId,'tnTlsFdbEPMacOperVcId':tnTlsFdbEPMacOperVcId,'tnTlsFdbPbbNumEpipes':tnTlsFdbPbbNumEpipes,'tnTlsShgInfoTable':tnTlsShgInfoTable,'tnTlsShgInfoEntry':tnTlsShgInfoEntry,_z:tnTlsShgName,'tnTlsShgRowStatus':tnTlsShgRowStatus,'tnTlsShgCustId':tnTlsShgCustId,'tnTlsShgInstanceId':tnTlsShgInstanceId,'tnTlsShgDescription':tnTlsShgDescription,'tnTlsShgLastMgmtChange':tnTlsShgLastMgmtChange,'tnTlsShgResidential':tnTlsShgResidential,'tnTlsShgRestProtSrcMac':tnTlsShgRestProtSrcMac,'tnTlsShgRestUnprotDstMac':tnTlsShgRestUnprotDstMac,'tnTlsShgRestProtSrcMacAction':tnTlsShgRestProtSrcMacAction,'tnTlsShgCreationOrigin':tnTlsShgCreationOrigin,'tnSvcEndPointTable':tnSvcEndPointTable,'tnSvcEndPointEntry':tnSvcEndPointEntry,_A0:tnSvcEndPointName,'tnSvcEndPointRowStatus':tnSvcEndPointRowStatus,'tnSvcEndPointDescription':tnSvcEndPointDescription,'tnSvcEndPointRevertTime':tnSvcEndPointRevertTime,'tnSvcEndPointTxActiveType':tnSvcEndPointTxActiveType,'tnSvcEndPointTxActivePortId':tnSvcEndPointTxActivePortId,'tnSvcEndPointTxActiveEncap':tnSvcEndPointTxActiveEncap,'tnSvcEndPointTxActiveSdpId':tnSvcEndPointTxActiveSdpId,'tnSvcEndPointForceSwitchOver':tnSvcEndPointForceSwitchOver,'tnSvcEndPointForceSwitchOverSdpId':tnSvcEndPointForceSwitchOverSdpId,'tnSvcEndPointActiveHoldDelay':tnSvcEndPointActiveHoldDelay,'tnSvcEndPointIgnoreStandbySig':tnSvcEndPointIgnoreStandbySig,'tnSvcEndPointMacPinning':tnSvcEndPointMacPinning,'tnSvcEndPointMacLimit':tnSvcEndPointMacLimit,'tnSvcEndPointSuppressStandbySig':tnSvcEndPointSuppressStandbySig,'tnSvcEndPointRevertTimeCountDn':tnSvcEndPointRevertTimeCountDn,'tnSvcEndPointTxActiveChangeCount':tnSvcEndPointTxActiveChangeCount,'tnSvcEndPointTxActiveLastChange':tnSvcEndPointTxActiveLastChange,'tnSvcEndPointTxActiveUpTime':tnSvcEndPointTxActiveUpTime,'tnSvcEndPointMCEPId':tnSvcEndPointMCEPId,'tnSvcEndPointMCEPPeerAddrType':tnSvcEndPointMCEPPeerAddrType,'tnSvcEndPointMCEPPeerAddr':tnSvcEndPointMCEPPeerAddr,'tnSvcEndPointMCEPPeerName':tnSvcEndPointMCEPPeerName,'tnSvcEndPointBlockOnMeshFail':tnSvcEndPointBlockOnMeshFail,'tnSvcEndPointMCEPPsvModeActive':tnSvcEndPointMCEPPsvModeActive,'tnSvcEndPointStandbySigMaster':tnSvcEndPointStandbySigMaster,'tnSvcTlsBackboneInfoTable':tnSvcTlsBackboneInfoTable,_AC:tnSvcTlsBackboneInfoEntry,'tnSvcTlsBackboneSrcMac':tnSvcTlsBackboneSrcMac,'tnSvcTlsBackboneVplsSvcId':tnSvcTlsBackboneVplsSvcId,'tnSvcTlsBackboneVplsSvcISID':tnSvcTlsBackboneVplsSvcISID,'tnSvcTlsBackboneOperSrcMac':tnSvcTlsBackboneOperSrcMac,'tnSvcTlsBackboneOperVplsSvcISID':tnSvcTlsBackboneOperVplsSvcISID,'tnSvcTlsBackboneLDPMacFlush':tnSvcTlsBackboneLDPMacFlush,'tnSvcTlsBackboneVplsStp':tnSvcTlsBackboneVplsStp,'tnSvcTlsBackboneLDPMacFlushNotMine':tnSvcTlsBackboneLDPMacFlushNotMine,'tnSvcTlsBackboneUseSapBMac':tnSvcTlsBackboneUseSapBMac,'tnTlsMFibTable':tnTlsMFibTable,'tnTlsMFibEntry':tnTlsMFibEntry,_A1:tnTlsMFibEntryType,_A2:tnTlsMFibGrpMacAddr,_A3:tnTlsMFibGrpInetAddrType,_A4:tnTlsMFibGrpInetAddr,_A5:tnTlsMFibSrcInetAddrType,_A6:tnTlsMFibSrcInetAddr,_A7:tnTlsMFibLocale,_A8:tnTlsMFibPortId,_A9:tnTlsMFibEncapValue,_AA:tnTlsMFibSdpId,_AB:tnTlsMFibVcId,'tnTlsMFibFwdOrBlk':tnTlsMFibFwdOrBlk,'tnTlsMFibSvcId':tnTlsMFibSvcId,'tnSvcTlsBgpADTableLastChanged':tnSvcTlsBgpADTableLastChanged,'tnSvcEpipePbbTableLastChanged':tnSvcEpipePbbTableLastChanged,'tnSvcTotalFdbMimDestIdxEntries':tnSvcTotalFdbMimDestIdxEntries,'tnSvcArpHostTableLastChanged':tnSvcArpHostTableLastChanged,'tnSvcArpHostIfTableLastMgmtChange':tnSvcArpHostIfTableLastMgmtChange,'tnSvcArpHostDefaultSessionTimeout':tnSvcArpHostDefaultSessionTimeout,'tnSvcIgmpTrkTableLastMgmtChange':tnSvcIgmpTrkTableLastMgmtChange,'tnSvcIpipeInfoTableLastMgmtChange':tnSvcIpipeInfoTableLastMgmtChange,'tnSvcMacNameTableLastChanged':tnSvcMacNameTableLastChanged,'tnSvcScalar1':tnSvcScalar1,'tnSvcScalar2':tnSvcScalar2,'tnSvcScalar3':tnSvcScalar3,'tnSvcScalar4':tnSvcScalar4,'tnSvcScalar5':tnSvcScalar5,'tnServNotifications':tnServNotifications,'tnCustTrapsPrefix':tnCustTrapsPrefix,'tnCustTraps':tnCustTraps,'tnSvcTrapsPrefix':tnSvcTrapsPrefix,'tnSvcTraps':tnSvcTraps,'tnTstpTrapsPrefix':tnTstpTrapsPrefix,'tnTstpTraps':tnTstpTraps})