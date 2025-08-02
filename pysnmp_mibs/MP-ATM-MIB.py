_AY='mpAtmCCAtmMultiLeafVci'
_AX='mpAtmCCAtmMultiLeafVpi'
_AW='mpAtmCCAtmMultiLeafIfIndex'
_AV='mpAtmCCAtmMultiRootVci'
_AU='mpAtmCCAtmMultiRootVpi'
_AT='mpAtmCCAtmMultiRootIfIndex'
_AS='mpAtmCCAtmMultiVci'
_AR='mpAtmCCAtmMultiVpi'
_AQ='mpAtmCCAtmMultiIfIndex'
_AP='mpAtmCCPgcActGrpNum'
_AO='mpAtmCCPgcPvcVci'
_AN='mpAtmCCPgcPvcVpi'
_AM='mpAtmCCPgcPvcIfIndex'
_AL='mpAtmCCUpgcPgcIndex'
_AK='underEstablish'
_AJ='mpAtmCCPathTestVci'
_AI='mpAtmCCPathTestVpi'
_AH='mpAtmCCVpTunnelingVpi'
_AG='mpAtmCCPvcTraceEntryIndex'
_AF='mpAtmCCVccStatusOrgVci'
_AE='mpAtmCCVccStatusOrgVpi'
_AD='mpAtmCCVccStatusOrgPort'
_AC='mpAtmCCProtocolTrapInfoIndex'
_AB='mpAtmCCPortBwInfoVpi'
_AA='mpAtmCCVccStatRegVci'
_A9='mpAtmCCVccStatRegVpi'
_A8='mpAtmCCOuspStatIndex'
_A7='mpAtmCCVcStatVci'
_A6='mpAtmCCVcStatVpi'
_A5='mpAtmCCVpStatVpi'
_A4='mpAtmCCSoftPvcCalledVci'
_A3='mpAtmCCSoftPvcCalledVpi'
_A2='mpAtmCCSoftPvcCalledIfIndex'
_A1='mpAtmCCSoftPvcCalledLeafReference'
_A0='mpAtmCCSoftPvpCalledVpi'
_z='mpAtmCCSoftPvpCalledIfIndex'
_y='mpAtmCCSoftPvpCalledLeafReference'
_x='mpAtmCCSoftPvcVci'
_w='mpAtmCCSoftPvcVpi'
_v='mpAtmCCSoftPvcIfIndex'
_u='mpAtmCCSoftPvcLeafReference'
_t='mpAtmCCSoftPvpVpi'
_s='mpAtmCCSoftPvpIfIndex'
_r='mpAtmCCSoftPvpLeafReference'
_q='mpAtmCCStaticPvcHighVci'
_p='mpAtmCCStaticPvcHighVpi'
_o='mpAtmCCStaticPvcHighIfIndex'
_n='mpAtmCCStaticPvcLowVci'
_m='mpAtmCCStaticPvcLowVpi'
_l='mpAtmCCStaticPvcLowIfIndex'
_k='mpAtmCCStaticPvcIndex'
_j='mpAtmCCStaticPvpHighVpi'
_i='mpAtmCCStaticPvpHighIfIndex'
_h='mpAtmCCStaticPvpLowVpi'
_g='mpAtmCCStaticPvpLowIfIndex'
_f='mpAtmCCStaticPvpIndex'
_e='PhysAddress'
_d='NotificationType'
_c='mpAtmCCPgcIndex'
_b='stsInactive'
_a='inactive'
_Z='mpAtmCCUpgcIndex'
_Y='underDeactivate'
_X='mpAtmCCPvcTraceIndex'
_W='incoming'
_V='outgoing'
_U='DisplayString'
_T='called'
_S='calling'
_R='active'
_Q='ture'
_P='OctetString'
_O='false'
_N='cancel'
_M='enable'
_L='unknown'
_K='delete'
_J='ifIndex'
_I='IF-MIB'
_H='down'
_G='up'
_F='not-accessible'
_E='MP-ATM-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_P,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AtmTrafficDescrParamIndex,=mibBuilder.importSymbols('ATM-MIB','AtmTrafficDescrParamIndex')
ifIndex,=mibBuilder.importSymbols(_I,_J)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,iso,mgmt=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier',_d,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_d,'TimeTicks','Unsigned32','iso','mgmt')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_U,_e,'TextualConvention')
class RowStatus(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_R,1),('notInService',2),('notReady',3),('createAndGo',4),('createAndWait',5),('destroy',6)))
class NetPrefix(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(13,13));fixedLength=13
class DisplayString(OctetString):0
class DateAndTime(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8),ValueSizeConstraint(11,11))
class MacAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
class PhysAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
class AtmAddr(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(8,8),ValueSizeConstraint(20,20))
class MpAtmCCCladType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*(('com',1),('mux',2),('atm-uni',3),('atm-trunk',4),('atm-uni-vmc',5),('lvc',6),('ffr',7),('odt',8),('ces',9),('ins',10),('sel',11),('eth',12),('atm-trunk-cdm',13)))
_Org_ObjectIdentity=ObjectIdentity
org=_Org_ObjectIdentity((1,3))
_Dod_ObjectIdentity=ObjectIdentity
dod=_Dod_ObjectIdentity((1,3,6))
_Internet_ObjectIdentity=ObjectIdentity
internet=_Internet_ObjectIdentity((1,3,6,1))
_Private_ObjectIdentity=ObjectIdentity
private=_Private_ObjectIdentity((1,3,6,1,4))
_Enterprises_ObjectIdentity=ObjectIdentity
enterprises=_Enterprises_ObjectIdentity((1,3,6,1,4,1))
_Nec_ObjectIdentity=ObjectIdentity
nec=_Nec_ObjectIdentity((1,3,6,1,4,1,119))
_NecProduct_ObjectIdentity=ObjectIdentity
necProduct=_NecProduct_ObjectIdentity((1,3,6,1,4,1,119,1))
_Datax_ObjectIdentity=ObjectIdentity
datax=_Datax_ObjectIdentity((1,3,6,1,4,1,119,1,3))
_Mmpf_ObjectIdentity=ObjectIdentity
mmpf=_Mmpf_ObjectIdentity((1,3,6,1,4,1,119,1,3,13))
_Mmn9110_ObjectIdentity=ObjectIdentity
mmn9110=_Mmn9110_ObjectIdentity((1,3,6,1,4,1,119,1,3,13,1))
_Mmn9120_ObjectIdentity=ObjectIdentity
mmn9120=_Mmn9120_ObjectIdentity((1,3,6,1,4,1,119,1,3,13,2))
_Nec_mib_ObjectIdentity=ObjectIdentity
nec_mib=_Nec_mib_ObjectIdentity((1,3,6,1,4,1,119,2))
_NecProductDepend_ObjectIdentity=ObjectIdentity
necProductDepend=_NecProductDepend_ObjectIdentity((1,3,6,1,4,1,119,2,3))
_Datax_mib_ObjectIdentity=ObjectIdentity
datax_mib=_Datax_mib_ObjectIdentity((1,3,6,1,4,1,119,2,3,3))
_Mmpf_mib_ObjectIdentity=ObjectIdentity
mmpf_mib=_Mmpf_mib_ObjectIdentity((1,3,6,1,4,1,119,2,3,3,13))
_MpSystem_ObjectIdentity=ObjectIdentity
mpSystem=_MpSystem_ObjectIdentity((1,3,6,1,4,1,119,2,3,3,13,1))
_MpIfCard_ObjectIdentity=ObjectIdentity
mpIfCard=_MpIfCard_ObjectIdentity((1,3,6,1,4,1,119,2,3,3,13,2))
_MpEtherPort_ObjectIdentity=ObjectIdentity
mpEtherPort=_MpEtherPort_ObjectIdentity((1,3,6,1,4,1,119,2,3,3,13,3))
_MpVlan_ObjectIdentity=ObjectIdentity
mpVlan=_MpVlan_ObjectIdentity((1,3,6,1,4,1,119,2,3,3,13,4))
_MpBridge_ObjectIdentity=ObjectIdentity
mpBridge=_MpBridge_ObjectIdentity((1,3,6,1,4,1,119,2,3,3,13,5))
_MpDbAccess_ObjectIdentity=ObjectIdentity
mpDbAccess=_MpDbAccess_ObjectIdentity((1,3,6,1,4,1,119,2,3,3,13,6))
_MpEventLog_ObjectIdentity=ObjectIdentity
mpEventLog=_MpEventLog_ObjectIdentity((1,3,6,1,4,1,119,2,3,3,13,7))
_MpUiSession_ObjectIdentity=ObjectIdentity
mpUiSession=_MpUiSession_ObjectIdentity((1,3,6,1,4,1,119,2,3,3,13,8))
_MpFtp_ObjectIdentity=ObjectIdentity
mpFtp=_MpFtp_ObjectIdentity((1,3,6,1,4,1,119,2,3,3,13,9))
_MpDhcp_ObjectIdentity=ObjectIdentity
mpDhcp=_MpDhcp_ObjectIdentity((1,3,6,1,4,1,119,2,3,3,13,10))
_MpIp_ObjectIdentity=ObjectIdentity
mpIp=_MpIp_ObjectIdentity((1,3,6,1,4,1,119,2,3,3,13,11))
_MpRip_ObjectIdentity=ObjectIdentity
mpRip=_MpRip_ObjectIdentity((1,3,6,1,4,1,119,2,3,3,13,12))
_MpSnmp_ObjectIdentity=ObjectIdentity
mpSnmp=_MpSnmp_ObjectIdentity((1,3,6,1,4,1,119,2,3,3,13,13))
_MpStats_ObjectIdentity=ObjectIdentity
mpStats=_MpStats_ObjectIdentity((1,3,6,1,4,1,119,2,3,3,13,14))
_MpCli_ObjectIdentity=ObjectIdentity
mpCli=_MpCli_ObjectIdentity((1,3,6,1,4,1,119,2,3,3,13,15))
_MpAtm_ObjectIdentity=ObjectIdentity
mpAtm=_MpAtm_ObjectIdentity((1,3,6,1,4,1,119,2,3,3,13,16))
_MpLis_ObjectIdentity=ObjectIdentity
mpLis=_MpLis_ObjectIdentity((1,3,6,1,4,1,119,2,3,3,13,17))
_MpDns_ObjectIdentity=ObjectIdentity
mpDns=_MpDns_ObjectIdentity((1,3,6,1,4,1,119,2,3,3,13,18))
_MpLec_ObjectIdentity=ObjectIdentity
mpLec=_MpLec_ObjectIdentity((1,3,6,1,4,1,119,2,3,3,13,19))
_MpMpc_ObjectIdentity=ObjectIdentity
mpMpc=_MpMpc_ObjectIdentity((1,3,6,1,4,1,119,2,3,3,13,20))
_MpStp_ObjectIdentity=ObjectIdentity
mpStp=_MpStp_ObjectIdentity((1,3,6,1,4,1,119,2,3,3,13,21))
_MpLlc_ObjectIdentity=ObjectIdentity
mpLlc=_MpLlc_ObjectIdentity((1,3,6,1,4,1,119,2,3,3,13,22))
_MpOspf_ObjectIdentity=ObjectIdentity
mpOspf=_MpOspf_ObjectIdentity((1,3,6,1,4,1,119,2,3,3,13,23))
_MpObsCtl_ObjectIdentity=ObjectIdentity
mpObsCtl=_MpObsCtl_ObjectIdentity((1,3,6,1,4,1,119,2,3,3,13,101))
_MpCardInfo_ObjectIdentity=ObjectIdentity
mpCardInfo=_MpCardInfo_ObjectIdentity((1,3,6,1,4,1,119,2,3,3,13,102))
_MpInterface_ObjectIdentity=ObjectIdentity
mpInterface=_MpInterface_ObjectIdentity((1,3,6,1,4,1,119,2,3,3,13,103))
_MpPvoice_ObjectIdentity=ObjectIdentity
mpPvoice=_MpPvoice_ObjectIdentity((1,3,6,1,4,1,119,2,3,3,13,104))
_MpAtmCallCtl_ObjectIdentity=ObjectIdentity
mpAtmCallCtl=_MpAtmCallCtl_ObjectIdentity((1,3,6,1,4,1,119,2,3,3,13,110))
_MpAtmCCBaseGroup_ObjectIdentity=ObjectIdentity
mpAtmCCBaseGroup=_MpAtmCCBaseGroup_ObjectIdentity((1,3,6,1,4,1,119,2,3,3,13,110,1))
_MpAtmCCNextTrafficDescrIndex_Type=AtmTrafficDescrParamIndex
_MpAtmCCNextTrafficDescrIndex_Object=MibScalar
mpAtmCCNextTrafficDescrIndex=_MpAtmCCNextTrafficDescrIndex_Object((1,3,6,1,4,1,119,2,3,3,13,110,1,1),_MpAtmCCNextTrafficDescrIndex_Type())
mpAtmCCNextTrafficDescrIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCNextTrafficDescrIndex.setStatus(_A)
_MpAtmCCNextNodeVci_Type=Integer32
_MpAtmCCNextNodeVci_Object=MibScalar
mpAtmCCNextNodeVci=_MpAtmCCNextNodeVci_Object((1,3,6,1,4,1,119,2,3,3,13,110,1,2),_MpAtmCCNextNodeVci_Type())
mpAtmCCNextNodeVci.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCNextNodeVci.setStatus(_A)
_MpAtmCCStaticPVPC_ObjectIdentity=ObjectIdentity
mpAtmCCStaticPVPC=_MpAtmCCStaticPVPC_ObjectIdentity((1,3,6,1,4,1,119,2,3,3,13,110,2))
_MpAtmCCStaticPvpTable_Object=MibTable
mpAtmCCStaticPvpTable=_MpAtmCCStaticPvpTable_Object((1,3,6,1,4,1,119,2,3,3,13,110,2,1))
if mibBuilder.loadTexts:mpAtmCCStaticPvpTable.setStatus(_A)
_MpAtmCCStaticPvpEntry_Object=MibTableRow
mpAtmCCStaticPvpEntry=_MpAtmCCStaticPvpEntry_Object((1,3,6,1,4,1,119,2,3,3,13,110,2,1,1))
mpAtmCCStaticPvpEntry.setIndexNames((0,_E,_f),(0,_E,_g),(0,_E,_h),(0,_E,_i),(0,_E,_j))
if mibBuilder.loadTexts:mpAtmCCStaticPvpEntry.setStatus(_A)
class _MpAtmCCStaticPvpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MpAtmCCStaticPvpIndex_Type.__name__=_C
_MpAtmCCStaticPvpIndex_Object=MibTableColumn
mpAtmCCStaticPvpIndex=_MpAtmCCStaticPvpIndex_Object((1,3,6,1,4,1,119,2,3,3,13,110,2,1,1,1),_MpAtmCCStaticPvpIndex_Type())
mpAtmCCStaticPvpIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:mpAtmCCStaticPvpIndex.setStatus(_A)
_MpAtmCCStaticPvpLowIfIndex_Type=Integer32
_MpAtmCCStaticPvpLowIfIndex_Object=MibTableColumn
mpAtmCCStaticPvpLowIfIndex=_MpAtmCCStaticPvpLowIfIndex_Object((1,3,6,1,4,1,119,2,3,3,13,110,2,1,1,2),_MpAtmCCStaticPvpLowIfIndex_Type())
mpAtmCCStaticPvpLowIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:mpAtmCCStaticPvpLowIfIndex.setStatus(_A)
class _MpAtmCCStaticPvpLowVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_MpAtmCCStaticPvpLowVpi_Type.__name__=_C
_MpAtmCCStaticPvpLowVpi_Object=MibTableColumn
mpAtmCCStaticPvpLowVpi=_MpAtmCCStaticPvpLowVpi_Object((1,3,6,1,4,1,119,2,3,3,13,110,2,1,1,3),_MpAtmCCStaticPvpLowVpi_Type())
mpAtmCCStaticPvpLowVpi.setMaxAccess(_F)
if mibBuilder.loadTexts:mpAtmCCStaticPvpLowVpi.setStatus(_A)
_MpAtmCCStaticPvpHighIfIndex_Type=Integer32
_MpAtmCCStaticPvpHighIfIndex_Object=MibTableColumn
mpAtmCCStaticPvpHighIfIndex=_MpAtmCCStaticPvpHighIfIndex_Object((1,3,6,1,4,1,119,2,3,3,13,110,2,1,1,4),_MpAtmCCStaticPvpHighIfIndex_Type())
mpAtmCCStaticPvpHighIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:mpAtmCCStaticPvpHighIfIndex.setStatus(_A)
class _MpAtmCCStaticPvpHighVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_MpAtmCCStaticPvpHighVpi_Type.__name__=_C
_MpAtmCCStaticPvpHighVpi_Object=MibTableColumn
mpAtmCCStaticPvpHighVpi=_MpAtmCCStaticPvpHighVpi_Object((1,3,6,1,4,1,119,2,3,3,13,110,2,1,1,5),_MpAtmCCStaticPvpHighVpi_Type())
mpAtmCCStaticPvpHighVpi.setMaxAccess(_F)
if mibBuilder.loadTexts:mpAtmCCStaticPvpHighVpi.setStatus(_A)
_MpAtmCCStaticPvpLowReceiveTrafficDescrIndex_Type=AtmTrafficDescrParamIndex
_MpAtmCCStaticPvpLowReceiveTrafficDescrIndex_Object=MibTableColumn
mpAtmCCStaticPvpLowReceiveTrafficDescrIndex=_MpAtmCCStaticPvpLowReceiveTrafficDescrIndex_Object((1,3,6,1,4,1,119,2,3,3,13,110,2,1,1,6),_MpAtmCCStaticPvpLowReceiveTrafficDescrIndex_Type())
mpAtmCCStaticPvpLowReceiveTrafficDescrIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCStaticPvpLowReceiveTrafficDescrIndex.setStatus(_A)
_MpAtmCCStaticPvpLowTransmitTrafficDescrIndex_Type=AtmTrafficDescrParamIndex
_MpAtmCCStaticPvpLowTransmitTrafficDescrIndex_Object=MibTableColumn
mpAtmCCStaticPvpLowTransmitTrafficDescrIndex=_MpAtmCCStaticPvpLowTransmitTrafficDescrIndex_Object((1,3,6,1,4,1,119,2,3,3,13,110,2,1,1,7),_MpAtmCCStaticPvpLowTransmitTrafficDescrIndex_Type())
mpAtmCCStaticPvpLowTransmitTrafficDescrIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCStaticPvpLowTransmitTrafficDescrIndex.setStatus(_A)
_MpAtmCCStaticPvpHighReceiveTrafficDescrIndex_Type=AtmTrafficDescrParamIndex
_MpAtmCCStaticPvpHighReceiveTrafficDescrIndex_Object=MibTableColumn
mpAtmCCStaticPvpHighReceiveTrafficDescrIndex=_MpAtmCCStaticPvpHighReceiveTrafficDescrIndex_Object((1,3,6,1,4,1,119,2,3,3,13,110,2,1,1,8),_MpAtmCCStaticPvpHighReceiveTrafficDescrIndex_Type())
mpAtmCCStaticPvpHighReceiveTrafficDescrIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCStaticPvpHighReceiveTrafficDescrIndex.setStatus(_A)
_MpAtmCCStaticPvpHighTransmitTrafficDescrIndex_Type=AtmTrafficDescrParamIndex
_MpAtmCCStaticPvpHighTransmitTrafficDescrIndex_Object=MibTableColumn
mpAtmCCStaticPvpHighTransmitTrafficDescrIndex=_MpAtmCCStaticPvpHighTransmitTrafficDescrIndex_Object((1,3,6,1,4,1,119,2,3,3,13,110,2,1,1,9),_MpAtmCCStaticPvpHighTransmitTrafficDescrIndex_Type())
mpAtmCCStaticPvpHighTransmitTrafficDescrIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCStaticPvpHighTransmitTrafficDescrIndex.setStatus(_A)
class _MpAtmCCStaticPvpPriority_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_MpAtmCCStaticPvpPriority_Type.__name__=_C
_MpAtmCCStaticPvpPriority_Object=MibTableColumn
mpAtmCCStaticPvpPriority=_MpAtmCCStaticPvpPriority_Object((1,3,6,1,4,1,119,2,3,3,13,110,2,1,1,10),_MpAtmCCStaticPvpPriority_Type())
mpAtmCCStaticPvpPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCStaticPvpPriority.setStatus(_A)
_MpAtmCCStaticPvpLowCladType_Type=MpAtmCCCladType
_MpAtmCCStaticPvpLowCladType_Object=MibTableColumn
mpAtmCCStaticPvpLowCladType=_MpAtmCCStaticPvpLowCladType_Object((1,3,6,1,4,1,119,2,3,3,13,110,2,1,1,11),_MpAtmCCStaticPvpLowCladType_Type())
mpAtmCCStaticPvpLowCladType.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCStaticPvpLowCladType.setStatus(_A)
_MpAtmCCStaticPvpHighCladType_Type=MpAtmCCCladType
_MpAtmCCStaticPvpHighCladType_Object=MibTableColumn
mpAtmCCStaticPvpHighCladType=_MpAtmCCStaticPvpHighCladType_Object((1,3,6,1,4,1,119,2,3,3,13,110,2,1,1,12),_MpAtmCCStaticPvpHighCladType_Type())
mpAtmCCStaticPvpHighCladType.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCStaticPvpHighCladType.setStatus(_A)
class _MpAtmCCStaticPvpAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_MpAtmCCStaticPvpAdminStatus_Type.__name__=_C
_MpAtmCCStaticPvpAdminStatus_Object=MibTableColumn
mpAtmCCStaticPvpAdminStatus=_MpAtmCCStaticPvpAdminStatus_Object((1,3,6,1,4,1,119,2,3,3,13,110,2,1,1,13),_MpAtmCCStaticPvpAdminStatus_Type())
mpAtmCCStaticPvpAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCStaticPvpAdminStatus.setStatus(_A)
_MpAtmCCStaticPvpOperStatus_Type=Integer32
_MpAtmCCStaticPvpOperStatus_Object=MibTableColumn
mpAtmCCStaticPvpOperStatus=_MpAtmCCStaticPvpOperStatus_Object((1,3,6,1,4,1,119,2,3,3,13,110,2,1,1,14),_MpAtmCCStaticPvpOperStatus_Type())
mpAtmCCStaticPvpOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCStaticPvpOperStatus.setStatus(_A)
_MpAtmCCStaticPvpPvpId_Type=Integer32
_MpAtmCCStaticPvpPvpId_Object=MibTableColumn
mpAtmCCStaticPvpPvpId=_MpAtmCCStaticPvpPvpId_Object((1,3,6,1,4,1,119,2,3,3,13,110,2,1,1,15),_MpAtmCCStaticPvpPvpId_Type())
mpAtmCCStaticPvpPvpId.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCStaticPvpPvpId.setStatus(_A)
_MpAtmCCStaticPvpSeqNo_Type=Integer32
_MpAtmCCStaticPvpSeqNo_Object=MibTableColumn
mpAtmCCStaticPvpSeqNo=_MpAtmCCStaticPvpSeqNo_Object((1,3,6,1,4,1,119,2,3,3,13,110,2,1,1,16),_MpAtmCCStaticPvpSeqNo_Type())
mpAtmCCStaticPvpSeqNo.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCStaticPvpSeqNo.setStatus(_A)
_MpAtmCCStaticPvpPgcRequest_Type=Integer32
_MpAtmCCStaticPvpPgcRequest_Object=MibTableColumn
mpAtmCCStaticPvpPgcRequest=_MpAtmCCStaticPvpPgcRequest_Object((1,3,6,1,4,1,119,2,3,3,13,110,2,1,1,17),_MpAtmCCStaticPvpPgcRequest_Type())
mpAtmCCStaticPvpPgcRequest.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCStaticPvpPgcRequest.setStatus(_A)
class _MpAtmCCStaticPvpCfgStatus_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_M,1),(_N,2),(_K,3),(_L,4)))
_MpAtmCCStaticPvpCfgStatus_Type.__name__=_C
_MpAtmCCStaticPvpCfgStatus_Object=MibTableColumn
mpAtmCCStaticPvpCfgStatus=_MpAtmCCStaticPvpCfgStatus_Object((1,3,6,1,4,1,119,2,3,3,13,110,2,1,1,98),_MpAtmCCStaticPvpCfgStatus_Type())
mpAtmCCStaticPvpCfgStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCStaticPvpCfgStatus.setStatus(_A)
_MpAtmCCStaticPvpErrInfo_Type=Integer32
_MpAtmCCStaticPvpErrInfo_Object=MibTableColumn
mpAtmCCStaticPvpErrInfo=_MpAtmCCStaticPvpErrInfo_Object((1,3,6,1,4,1,119,2,3,3,13,110,2,1,1,99),_MpAtmCCStaticPvpErrInfo_Type())
mpAtmCCStaticPvpErrInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCStaticPvpErrInfo.setStatus(_A)
_MpAtmCCStaticPvcTable_Object=MibTable
mpAtmCCStaticPvcTable=_MpAtmCCStaticPvcTable_Object((1,3,6,1,4,1,119,2,3,3,13,110,2,2))
if mibBuilder.loadTexts:mpAtmCCStaticPvcTable.setStatus(_A)
_MpAtmCCStaticPvcEntry_Object=MibTableRow
mpAtmCCStaticPvcEntry=_MpAtmCCStaticPvcEntry_Object((1,3,6,1,4,1,119,2,3,3,13,110,2,2,1))
mpAtmCCStaticPvcEntry.setIndexNames((0,_E,_k),(0,_E,_l),(0,_E,_m),(0,_E,_n),(0,_E,_o),(0,_E,_p),(0,_E,_q))
if mibBuilder.loadTexts:mpAtmCCStaticPvcEntry.setStatus(_A)
class _MpAtmCCStaticPvcIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MpAtmCCStaticPvcIndex_Type.__name__=_C
_MpAtmCCStaticPvcIndex_Object=MibTableColumn
mpAtmCCStaticPvcIndex=_MpAtmCCStaticPvcIndex_Object((1,3,6,1,4,1,119,2,3,3,13,110,2,2,1,1),_MpAtmCCStaticPvcIndex_Type())
mpAtmCCStaticPvcIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:mpAtmCCStaticPvcIndex.setStatus(_A)
_MpAtmCCStaticPvcLowIfIndex_Type=Integer32
_MpAtmCCStaticPvcLowIfIndex_Object=MibTableColumn
mpAtmCCStaticPvcLowIfIndex=_MpAtmCCStaticPvcLowIfIndex_Object((1,3,6,1,4,1,119,2,3,3,13,110,2,2,1,2),_MpAtmCCStaticPvcLowIfIndex_Type())
mpAtmCCStaticPvcLowIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:mpAtmCCStaticPvcLowIfIndex.setStatus(_A)
class _MpAtmCCStaticPvcLowVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_MpAtmCCStaticPvcLowVpi_Type.__name__=_C
_MpAtmCCStaticPvcLowVpi_Object=MibTableColumn
mpAtmCCStaticPvcLowVpi=_MpAtmCCStaticPvcLowVpi_Object((1,3,6,1,4,1,119,2,3,3,13,110,2,2,1,3),_MpAtmCCStaticPvcLowVpi_Type())
mpAtmCCStaticPvcLowVpi.setMaxAccess(_F)
if mibBuilder.loadTexts:mpAtmCCStaticPvcLowVpi.setStatus(_A)
class _MpAtmCCStaticPvcLowVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MpAtmCCStaticPvcLowVci_Type.__name__=_C
_MpAtmCCStaticPvcLowVci_Object=MibTableColumn
mpAtmCCStaticPvcLowVci=_MpAtmCCStaticPvcLowVci_Object((1,3,6,1,4,1,119,2,3,3,13,110,2,2,1,4),_MpAtmCCStaticPvcLowVci_Type())
mpAtmCCStaticPvcLowVci.setMaxAccess(_F)
if mibBuilder.loadTexts:mpAtmCCStaticPvcLowVci.setStatus(_A)
_MpAtmCCStaticPvcHighIfIndex_Type=Integer32
_MpAtmCCStaticPvcHighIfIndex_Object=MibTableColumn
mpAtmCCStaticPvcHighIfIndex=_MpAtmCCStaticPvcHighIfIndex_Object((1,3,6,1,4,1,119,2,3,3,13,110,2,2,1,5),_MpAtmCCStaticPvcHighIfIndex_Type())
mpAtmCCStaticPvcHighIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:mpAtmCCStaticPvcHighIfIndex.setStatus(_A)
class _MpAtmCCStaticPvcHighVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_MpAtmCCStaticPvcHighVpi_Type.__name__=_C
_MpAtmCCStaticPvcHighVpi_Object=MibTableColumn
mpAtmCCStaticPvcHighVpi=_MpAtmCCStaticPvcHighVpi_Object((1,3,6,1,4,1,119,2,3,3,13,110,2,2,1,6),_MpAtmCCStaticPvcHighVpi_Type())
mpAtmCCStaticPvcHighVpi.setMaxAccess(_F)
if mibBuilder.loadTexts:mpAtmCCStaticPvcHighVpi.setStatus(_A)
class _MpAtmCCStaticPvcHighVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MpAtmCCStaticPvcHighVci_Type.__name__=_C
_MpAtmCCStaticPvcHighVci_Object=MibTableColumn
mpAtmCCStaticPvcHighVci=_MpAtmCCStaticPvcHighVci_Object((1,3,6,1,4,1,119,2,3,3,13,110,2,2,1,7),_MpAtmCCStaticPvcHighVci_Type())
mpAtmCCStaticPvcHighVci.setMaxAccess(_F)
if mibBuilder.loadTexts:mpAtmCCStaticPvcHighVci.setStatus(_A)
_MpAtmCCStaticPvcLowReceiveTrafficDescrIndex_Type=AtmTrafficDescrParamIndex
_MpAtmCCStaticPvcLowReceiveTrafficDescrIndex_Object=MibTableColumn
mpAtmCCStaticPvcLowReceiveTrafficDescrIndex=_MpAtmCCStaticPvcLowReceiveTrafficDescrIndex_Object((1,3,6,1,4,1,119,2,3,3,13,110,2,2,1,8),_MpAtmCCStaticPvcLowReceiveTrafficDescrIndex_Type())
mpAtmCCStaticPvcLowReceiveTrafficDescrIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCStaticPvcLowReceiveTrafficDescrIndex.setStatus(_A)
_MpAtmCCStaticPvcLowTransmitTrafficDescrIndex_Type=AtmTrafficDescrParamIndex
_MpAtmCCStaticPvcLowTransmitTrafficDescrIndex_Object=MibTableColumn
mpAtmCCStaticPvcLowTransmitTrafficDescrIndex=_MpAtmCCStaticPvcLowTransmitTrafficDescrIndex_Object((1,3,6,1,4,1,119,2,3,3,13,110,2,2,1,9),_MpAtmCCStaticPvcLowTransmitTrafficDescrIndex_Type())
mpAtmCCStaticPvcLowTransmitTrafficDescrIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCStaticPvcLowTransmitTrafficDescrIndex.setStatus(_A)
_MpAtmCCStaticPvcHighReceiveTrafficDescrIndex_Type=AtmTrafficDescrParamIndex
_MpAtmCCStaticPvcHighReceiveTrafficDescrIndex_Object=MibTableColumn
mpAtmCCStaticPvcHighReceiveTrafficDescrIndex=_MpAtmCCStaticPvcHighReceiveTrafficDescrIndex_Object((1,3,6,1,4,1,119,2,3,3,13,110,2,2,1,10),_MpAtmCCStaticPvcHighReceiveTrafficDescrIndex_Type())
mpAtmCCStaticPvcHighReceiveTrafficDescrIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCStaticPvcHighReceiveTrafficDescrIndex.setStatus(_A)
_MpAtmCCStaticPvcHighTransmitTrafficDescrIndex_Type=AtmTrafficDescrParamIndex
_MpAtmCCStaticPvcHighTransmitTrafficDescrIndex_Object=MibTableColumn
mpAtmCCStaticPvcHighTransmitTrafficDescrIndex=_MpAtmCCStaticPvcHighTransmitTrafficDescrIndex_Object((1,3,6,1,4,1,119,2,3,3,13,110,2,2,1,11),_MpAtmCCStaticPvcHighTransmitTrafficDescrIndex_Type())
mpAtmCCStaticPvcHighTransmitTrafficDescrIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCStaticPvcHighTransmitTrafficDescrIndex.setStatus(_A)
class _MpAtmCCStaticPvcPriority_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_MpAtmCCStaticPvcPriority_Type.__name__=_C
_MpAtmCCStaticPvcPriority_Object=MibTableColumn
mpAtmCCStaticPvcPriority=_MpAtmCCStaticPvcPriority_Object((1,3,6,1,4,1,119,2,3,3,13,110,2,2,1,12),_MpAtmCCStaticPvcPriority_Type())
mpAtmCCStaticPvcPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCStaticPvcPriority.setStatus(_A)
_MpAtmCCStaticPvcLowCladType_Type=MpAtmCCCladType
_MpAtmCCStaticPvcLowCladType_Object=MibTableColumn
mpAtmCCStaticPvcLowCladType=_MpAtmCCStaticPvcLowCladType_Object((1,3,6,1,4,1,119,2,3,3,13,110,2,2,1,13),_MpAtmCCStaticPvcLowCladType_Type())
mpAtmCCStaticPvcLowCladType.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCStaticPvcLowCladType.setStatus(_A)
_MpAtmCCStaticPvcHighCladType_Type=MpAtmCCCladType
_MpAtmCCStaticPvcHighCladType_Object=MibTableColumn
mpAtmCCStaticPvcHighCladType=_MpAtmCCStaticPvcHighCladType_Object((1,3,6,1,4,1,119,2,3,3,13,110,2,2,1,14),_MpAtmCCStaticPvcHighCladType_Type())
mpAtmCCStaticPvcHighCladType.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCStaticPvcHighCladType.setStatus(_A)
class _MpAtmCCStaticPvcAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_MpAtmCCStaticPvcAdminStatus_Type.__name__=_C
_MpAtmCCStaticPvcAdminStatus_Object=MibTableColumn
mpAtmCCStaticPvcAdminStatus=_MpAtmCCStaticPvcAdminStatus_Object((1,3,6,1,4,1,119,2,3,3,13,110,2,2,1,15),_MpAtmCCStaticPvcAdminStatus_Type())
mpAtmCCStaticPvcAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCStaticPvcAdminStatus.setStatus(_A)
_MpAtmCCStaticPvcOperStatus_Type=Integer32
_MpAtmCCStaticPvcOperStatus_Object=MibTableColumn
mpAtmCCStaticPvcOperStatus=_MpAtmCCStaticPvcOperStatus_Object((1,3,6,1,4,1,119,2,3,3,13,110,2,2,1,16),_MpAtmCCStaticPvcOperStatus_Type())
mpAtmCCStaticPvcOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCStaticPvcOperStatus.setStatus(_A)
_MpAtmCCStaticPvcPvcId_Type=Integer32
_MpAtmCCStaticPvcPvcId_Object=MibTableColumn
mpAtmCCStaticPvcPvcId=_MpAtmCCStaticPvcPvcId_Object((1,3,6,1,4,1,119,2,3,3,13,110,2,2,1,17),_MpAtmCCStaticPvcPvcId_Type())
mpAtmCCStaticPvcPvcId.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCStaticPvcPvcId.setStatus(_A)
_MpAtmCCStaticPvcSeqNo_Type=Integer32
_MpAtmCCStaticPvcSeqNo_Object=MibTableColumn
mpAtmCCStaticPvcSeqNo=_MpAtmCCStaticPvcSeqNo_Object((1,3,6,1,4,1,119,2,3,3,13,110,2,2,1,18),_MpAtmCCStaticPvcSeqNo_Type())
mpAtmCCStaticPvcSeqNo.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCStaticPvcSeqNo.setStatus(_A)
_MpAtmCCStaticPvcPgcRequest_Type=Integer32
_MpAtmCCStaticPvcPgcRequest_Object=MibTableColumn
mpAtmCCStaticPvcPgcRequest=_MpAtmCCStaticPvcPgcRequest_Object((1,3,6,1,4,1,119,2,3,3,13,110,2,2,1,19),_MpAtmCCStaticPvcPgcRequest_Type())
mpAtmCCStaticPvcPgcRequest.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCStaticPvcPgcRequest.setStatus(_A)
class _MpAtmCCStaticPvcCfgStatus_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_M,1),(_N,2),(_K,3),(_L,4)))
_MpAtmCCStaticPvcCfgStatus_Type.__name__=_C
_MpAtmCCStaticPvcCfgStatus_Object=MibTableColumn
mpAtmCCStaticPvcCfgStatus=_MpAtmCCStaticPvcCfgStatus_Object((1,3,6,1,4,1,119,2,3,3,13,110,2,2,1,98),_MpAtmCCStaticPvcCfgStatus_Type())
mpAtmCCStaticPvcCfgStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCStaticPvcCfgStatus.setStatus(_A)
_MpAtmCCStaticPvcErrInfo_Type=Integer32
_MpAtmCCStaticPvcErrInfo_Object=MibTableColumn
mpAtmCCStaticPvcErrInfo=_MpAtmCCStaticPvcErrInfo_Object((1,3,6,1,4,1,119,2,3,3,13,110,2,2,1,99),_MpAtmCCStaticPvcErrInfo_Type())
mpAtmCCStaticPvcErrInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCStaticPvcErrInfo.setStatus(_A)
_MpAtmCCSoftPVPC_ObjectIdentity=ObjectIdentity
mpAtmCCSoftPVPC=_MpAtmCCSoftPVPC_ObjectIdentity((1,3,6,1,4,1,119,2,3,3,13,110,3))
_MpAtmCCSoftPvpTable_Object=MibTable
mpAtmCCSoftPvpTable=_MpAtmCCSoftPvpTable_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,1))
if mibBuilder.loadTexts:mpAtmCCSoftPvpTable.setStatus(_A)
_MpAtmCCSoftPvpEntry_Object=MibTableRow
mpAtmCCSoftPvpEntry=_MpAtmCCSoftPvpEntry_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,1,1))
mpAtmCCSoftPvpEntry.setIndexNames((0,_E,_r),(0,_E,_s),(0,_E,_t))
if mibBuilder.loadTexts:mpAtmCCSoftPvpEntry.setStatus(_A)
class _MpAtmCCSoftPvpLeafReference_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_MpAtmCCSoftPvpLeafReference_Type.__name__=_C
_MpAtmCCSoftPvpLeafReference_Object=MibTableColumn
mpAtmCCSoftPvpLeafReference=_MpAtmCCSoftPvpLeafReference_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,1,1,1),_MpAtmCCSoftPvpLeafReference_Type())
mpAtmCCSoftPvpLeafReference.setMaxAccess(_F)
if mibBuilder.loadTexts:mpAtmCCSoftPvpLeafReference.setStatus(_A)
_MpAtmCCSoftPvpIfIndex_Type=Integer32
_MpAtmCCSoftPvpIfIndex_Object=MibTableColumn
mpAtmCCSoftPvpIfIndex=_MpAtmCCSoftPvpIfIndex_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,1,1,2),_MpAtmCCSoftPvpIfIndex_Type())
mpAtmCCSoftPvpIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:mpAtmCCSoftPvpIfIndex.setStatus(_A)
_MpAtmCCSoftPvpVpi_Type=Integer32
_MpAtmCCSoftPvpVpi_Object=MibTableColumn
mpAtmCCSoftPvpVpi=_MpAtmCCSoftPvpVpi_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,1,1,3),_MpAtmCCSoftPvpVpi_Type())
mpAtmCCSoftPvpVpi.setMaxAccess(_F)
if mibBuilder.loadTexts:mpAtmCCSoftPvpVpi.setStatus(_A)
_MpAtmCCSoftPvpReceiveTrafficDescrIndex_Type=AtmTrafficDescrParamIndex
_MpAtmCCSoftPvpReceiveTrafficDescrIndex_Object=MibTableColumn
mpAtmCCSoftPvpReceiveTrafficDescrIndex=_MpAtmCCSoftPvpReceiveTrafficDescrIndex_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,1,1,4),_MpAtmCCSoftPvpReceiveTrafficDescrIndex_Type())
mpAtmCCSoftPvpReceiveTrafficDescrIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCSoftPvpReceiveTrafficDescrIndex.setStatus(_A)
_MpAtmCCSoftPvpTransmitTrafficDescrIndex_Type=AtmTrafficDescrParamIndex
_MpAtmCCSoftPvpTransmitTrafficDescrIndex_Object=MibTableColumn
mpAtmCCSoftPvpTransmitTrafficDescrIndex=_MpAtmCCSoftPvpTransmitTrafficDescrIndex_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,1,1,5),_MpAtmCCSoftPvpTransmitTrafficDescrIndex_Type())
mpAtmCCSoftPvpTransmitTrafficDescrIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCSoftPvpTransmitTrafficDescrIndex.setStatus(_A)
_MpAtmCCSoftPvpTargetAddress_Type=AtmAddr
_MpAtmCCSoftPvpTargetAddress_Object=MibTableColumn
mpAtmCCSoftPvpTargetAddress=_MpAtmCCSoftPvpTargetAddress_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,1,1,6),_MpAtmCCSoftPvpTargetAddress_Type())
mpAtmCCSoftPvpTargetAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCSoftPvpTargetAddress.setStatus(_A)
class _MpAtmCCSoftPvpTargetVpi_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_MpAtmCCSoftPvpTargetVpi_Type.__name__=_C
_MpAtmCCSoftPvpTargetVpi_Object=MibTableColumn
mpAtmCCSoftPvpTargetVpi=_MpAtmCCSoftPvpTargetVpi_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,1,1,7),_MpAtmCCSoftPvpTargetVpi_Type())
mpAtmCCSoftPvpTargetVpi.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCSoftPvpTargetVpi.setStatus(_A)
class _MpAtmCCSoftPvpLastReleaseCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,127))
_MpAtmCCSoftPvpLastReleaseCause_Type.__name__=_C
_MpAtmCCSoftPvpLastReleaseCause_Object=MibTableColumn
mpAtmCCSoftPvpLastReleaseCause=_MpAtmCCSoftPvpLastReleaseCause_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,1,1,8),_MpAtmCCSoftPvpLastReleaseCause_Type())
mpAtmCCSoftPvpLastReleaseCause.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCSoftPvpLastReleaseCause.setStatus(_A)
class _MpAtmCCSoftPvpLastReleaseDiagnostic_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_MpAtmCCSoftPvpLastReleaseDiagnostic_Type.__name__=_P
_MpAtmCCSoftPvpLastReleaseDiagnostic_Object=MibTableColumn
mpAtmCCSoftPvpLastReleaseDiagnostic=_MpAtmCCSoftPvpLastReleaseDiagnostic_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,1,1,9),_MpAtmCCSoftPvpLastReleaseDiagnostic_Type())
mpAtmCCSoftPvpLastReleaseDiagnostic.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCSoftPvpLastReleaseDiagnostic.setStatus(_A)
class _MpAtmCCSoftPvpPriority_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_MpAtmCCSoftPvpPriority_Type.__name__=_C
_MpAtmCCSoftPvpPriority_Object=MibTableColumn
mpAtmCCSoftPvpPriority=_MpAtmCCSoftPvpPriority_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,1,1,10),_MpAtmCCSoftPvpPriority_Type())
mpAtmCCSoftPvpPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCSoftPvpPriority.setStatus(_A)
_MpAtmCCSoftPvpCladType_Type=MpAtmCCCladType
_MpAtmCCSoftPvpCladType_Object=MibTableColumn
mpAtmCCSoftPvpCladType=_MpAtmCCSoftPvpCladType_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,1,1,11),_MpAtmCCSoftPvpCladType_Type())
mpAtmCCSoftPvpCladType.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCSoftPvpCladType.setStatus(_A)
_MpAtmCCSoftPvpOriginalAddress_Type=AtmAddr
_MpAtmCCSoftPvpOriginalAddress_Object=MibTableColumn
mpAtmCCSoftPvpOriginalAddress=_MpAtmCCSoftPvpOriginalAddress_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,1,1,12),_MpAtmCCSoftPvpOriginalAddress_Type())
mpAtmCCSoftPvpOriginalAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCSoftPvpOriginalAddress.setStatus(_A)
class _MpAtmCCSoftPvpAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_MpAtmCCSoftPvpAdminStatus_Type.__name__=_C
_MpAtmCCSoftPvpAdminStatus_Object=MibTableColumn
mpAtmCCSoftPvpAdminStatus=_MpAtmCCSoftPvpAdminStatus_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,1,1,13),_MpAtmCCSoftPvpAdminStatus_Type())
mpAtmCCSoftPvpAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCSoftPvpAdminStatus.setStatus(_A)
_MpAtmCCSoftPvpOperStatus_Type=Integer32
_MpAtmCCSoftPvpOperStatus_Object=MibTableColumn
mpAtmCCSoftPvpOperStatus=_MpAtmCCSoftPvpOperStatus_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,1,1,14),_MpAtmCCSoftPvpOperStatus_Type())
mpAtmCCSoftPvpOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCSoftPvpOperStatus.setStatus(_A)
_MpAtmCCSoftPvpPgcRequest_Type=Integer32
_MpAtmCCSoftPvpPgcRequest_Object=MibTableColumn
mpAtmCCSoftPvpPgcRequest=_MpAtmCCSoftPvpPgcRequest_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,1,1,15),_MpAtmCCSoftPvpPgcRequest_Type())
mpAtmCCSoftPvpPgcRequest.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCSoftPvpPgcRequest.setStatus(_A)
class _MpAtmCCSoftPvpCfgStatus_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_M,1),(_N,2),(_K,3),(_L,4)))
_MpAtmCCSoftPvpCfgStatus_Type.__name__=_C
_MpAtmCCSoftPvpCfgStatus_Object=MibTableColumn
mpAtmCCSoftPvpCfgStatus=_MpAtmCCSoftPvpCfgStatus_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,1,1,98),_MpAtmCCSoftPvpCfgStatus_Type())
mpAtmCCSoftPvpCfgStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCSoftPvpCfgStatus.setStatus(_A)
_MpAtmCCSoftPvpErrInfo_Type=Integer32
_MpAtmCCSoftPvpErrInfo_Object=MibTableColumn
mpAtmCCSoftPvpErrInfo=_MpAtmCCSoftPvpErrInfo_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,1,1,99),_MpAtmCCSoftPvpErrInfo_Type())
mpAtmCCSoftPvpErrInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCSoftPvpErrInfo.setStatus(_A)
_MpAtmCCSoftPvcTable_Object=MibTable
mpAtmCCSoftPvcTable=_MpAtmCCSoftPvcTable_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,2))
if mibBuilder.loadTexts:mpAtmCCSoftPvcTable.setStatus(_A)
_MpAtmCCSoftPvcEntry_Object=MibTableRow
mpAtmCCSoftPvcEntry=_MpAtmCCSoftPvcEntry_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,2,1))
mpAtmCCSoftPvcEntry.setIndexNames((0,_E,_u),(0,_E,_v),(0,_E,_w),(0,_E,_x))
if mibBuilder.loadTexts:mpAtmCCSoftPvcEntry.setStatus(_A)
class _MpAtmCCSoftPvcLeafReference_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_MpAtmCCSoftPvcLeafReference_Type.__name__=_C
_MpAtmCCSoftPvcLeafReference_Object=MibTableColumn
mpAtmCCSoftPvcLeafReference=_MpAtmCCSoftPvcLeafReference_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,2,1,1),_MpAtmCCSoftPvcLeafReference_Type())
mpAtmCCSoftPvcLeafReference.setMaxAccess(_F)
if mibBuilder.loadTexts:mpAtmCCSoftPvcLeafReference.setStatus(_A)
_MpAtmCCSoftPvcIfIndex_Type=Integer32
_MpAtmCCSoftPvcIfIndex_Object=MibTableColumn
mpAtmCCSoftPvcIfIndex=_MpAtmCCSoftPvcIfIndex_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,2,1,2),_MpAtmCCSoftPvcIfIndex_Type())
mpAtmCCSoftPvcIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:mpAtmCCSoftPvcIfIndex.setStatus(_A)
_MpAtmCCSoftPvcVpi_Type=Integer32
_MpAtmCCSoftPvcVpi_Object=MibTableColumn
mpAtmCCSoftPvcVpi=_MpAtmCCSoftPvcVpi_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,2,1,3),_MpAtmCCSoftPvcVpi_Type())
mpAtmCCSoftPvcVpi.setMaxAccess(_F)
if mibBuilder.loadTexts:mpAtmCCSoftPvcVpi.setStatus(_A)
_MpAtmCCSoftPvcVci_Type=Integer32
_MpAtmCCSoftPvcVci_Object=MibTableColumn
mpAtmCCSoftPvcVci=_MpAtmCCSoftPvcVci_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,2,1,4),_MpAtmCCSoftPvcVci_Type())
mpAtmCCSoftPvcVci.setMaxAccess(_F)
if mibBuilder.loadTexts:mpAtmCCSoftPvcVci.setStatus(_A)
_MpAtmCCSoftPvcReceiveTrafficDescrIndex_Type=AtmTrafficDescrParamIndex
_MpAtmCCSoftPvcReceiveTrafficDescrIndex_Object=MibTableColumn
mpAtmCCSoftPvcReceiveTrafficDescrIndex=_MpAtmCCSoftPvcReceiveTrafficDescrIndex_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,2,1,5),_MpAtmCCSoftPvcReceiveTrafficDescrIndex_Type())
mpAtmCCSoftPvcReceiveTrafficDescrIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCSoftPvcReceiveTrafficDescrIndex.setStatus(_A)
_MpAtmCCSoftPvcTransmitTrafficDescrIndex_Type=AtmTrafficDescrParamIndex
_MpAtmCCSoftPvcTransmitTrafficDescrIndex_Object=MibTableColumn
mpAtmCCSoftPvcTransmitTrafficDescrIndex=_MpAtmCCSoftPvcTransmitTrafficDescrIndex_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,2,1,6),_MpAtmCCSoftPvcTransmitTrafficDescrIndex_Type())
mpAtmCCSoftPvcTransmitTrafficDescrIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCSoftPvcTransmitTrafficDescrIndex.setStatus(_A)
_MpAtmCCSoftPvcTargetAddress_Type=AtmAddr
_MpAtmCCSoftPvcTargetAddress_Object=MibTableColumn
mpAtmCCSoftPvcTargetAddress=_MpAtmCCSoftPvcTargetAddress_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,2,1,7),_MpAtmCCSoftPvcTargetAddress_Type())
mpAtmCCSoftPvcTargetAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCSoftPvcTargetAddress.setStatus(_A)
class _MpAtmCCSoftPvcTargetVpi_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_MpAtmCCSoftPvcTargetVpi_Type.__name__=_C
_MpAtmCCSoftPvcTargetVpi_Object=MibTableColumn
mpAtmCCSoftPvcTargetVpi=_MpAtmCCSoftPvcTargetVpi_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,2,1,8),_MpAtmCCSoftPvcTargetVpi_Type())
mpAtmCCSoftPvcTargetVpi.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCSoftPvcTargetVpi.setStatus(_A)
class _MpAtmCCSoftPvcTargetVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MpAtmCCSoftPvcTargetVci_Type.__name__=_C
_MpAtmCCSoftPvcTargetVci_Object=MibTableColumn
mpAtmCCSoftPvcTargetVci=_MpAtmCCSoftPvcTargetVci_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,2,1,9),_MpAtmCCSoftPvcTargetVci_Type())
mpAtmCCSoftPvcTargetVci.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCSoftPvcTargetVci.setStatus(_A)
class _MpAtmCCSoftPvcLastReleaseCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,127))
_MpAtmCCSoftPvcLastReleaseCause_Type.__name__=_C
_MpAtmCCSoftPvcLastReleaseCause_Object=MibTableColumn
mpAtmCCSoftPvcLastReleaseCause=_MpAtmCCSoftPvcLastReleaseCause_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,2,1,10),_MpAtmCCSoftPvcLastReleaseCause_Type())
mpAtmCCSoftPvcLastReleaseCause.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCSoftPvcLastReleaseCause.setStatus(_A)
class _MpAtmCCSoftPvcLastReleaseDiagnostic_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_MpAtmCCSoftPvcLastReleaseDiagnostic_Type.__name__=_P
_MpAtmCCSoftPvcLastReleaseDiagnostic_Object=MibTableColumn
mpAtmCCSoftPvcLastReleaseDiagnostic=_MpAtmCCSoftPvcLastReleaseDiagnostic_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,2,1,11),_MpAtmCCSoftPvcLastReleaseDiagnostic_Type())
mpAtmCCSoftPvcLastReleaseDiagnostic.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCSoftPvcLastReleaseDiagnostic.setStatus(_A)
class _MpAtmCCSoftPvcPriority_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_MpAtmCCSoftPvcPriority_Type.__name__=_C
_MpAtmCCSoftPvcPriority_Object=MibTableColumn
mpAtmCCSoftPvcPriority=_MpAtmCCSoftPvcPriority_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,2,1,12),_MpAtmCCSoftPvcPriority_Type())
mpAtmCCSoftPvcPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCSoftPvcPriority.setStatus(_A)
_MpAtmCCSoftPvcCladType_Type=MpAtmCCCladType
_MpAtmCCSoftPvcCladType_Object=MibTableColumn
mpAtmCCSoftPvcCladType=_MpAtmCCSoftPvcCladType_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,2,1,13),_MpAtmCCSoftPvcCladType_Type())
mpAtmCCSoftPvcCladType.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCSoftPvcCladType.setStatus(_A)
_MpAtmCCSoftPvcOriginalAddress_Type=AtmAddr
_MpAtmCCSoftPvcOriginalAddress_Object=MibTableColumn
mpAtmCCSoftPvcOriginalAddress=_MpAtmCCSoftPvcOriginalAddress_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,2,1,14),_MpAtmCCSoftPvcOriginalAddress_Type())
mpAtmCCSoftPvcOriginalAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCSoftPvcOriginalAddress.setStatus(_A)
class _MpAtmCCSoftPvcAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_MpAtmCCSoftPvcAdminStatus_Type.__name__=_C
_MpAtmCCSoftPvcAdminStatus_Object=MibTableColumn
mpAtmCCSoftPvcAdminStatus=_MpAtmCCSoftPvcAdminStatus_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,2,1,15),_MpAtmCCSoftPvcAdminStatus_Type())
mpAtmCCSoftPvcAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCSoftPvcAdminStatus.setStatus(_A)
_MpAtmCCSoftPvcOperStatus_Type=Integer32
_MpAtmCCSoftPvcOperStatus_Object=MibTableColumn
mpAtmCCSoftPvcOperStatus=_MpAtmCCSoftPvcOperStatus_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,2,1,16),_MpAtmCCSoftPvcOperStatus_Type())
mpAtmCCSoftPvcOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCSoftPvcOperStatus.setStatus(_A)
_MpAtmCCSoftPvcPgcRequest_Type=Integer32
_MpAtmCCSoftPvcPgcRequest_Object=MibTableColumn
mpAtmCCSoftPvcPgcRequest=_MpAtmCCSoftPvcPgcRequest_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,2,1,17),_MpAtmCCSoftPvcPgcRequest_Type())
mpAtmCCSoftPvcPgcRequest.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCSoftPvcPgcRequest.setStatus(_A)
class _MpAtmCCSoftPvcCfgStatus_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_M,1),(_N,2),(_K,3),(_L,4)))
_MpAtmCCSoftPvcCfgStatus_Type.__name__=_C
_MpAtmCCSoftPvcCfgStatus_Object=MibTableColumn
mpAtmCCSoftPvcCfgStatus=_MpAtmCCSoftPvcCfgStatus_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,2,1,98),_MpAtmCCSoftPvcCfgStatus_Type())
mpAtmCCSoftPvcCfgStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCSoftPvcCfgStatus.setStatus(_A)
_MpAtmCCSoftPvcErrInfo_Type=Integer32
_MpAtmCCSoftPvcErrInfo_Object=MibTableColumn
mpAtmCCSoftPvcErrInfo=_MpAtmCCSoftPvcErrInfo_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,2,1,99),_MpAtmCCSoftPvcErrInfo_Type())
mpAtmCCSoftPvcErrInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCSoftPvcErrInfo.setStatus(_A)
_MpAtmCCSoftPvpCalledTable_Object=MibTable
mpAtmCCSoftPvpCalledTable=_MpAtmCCSoftPvpCalledTable_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,3))
if mibBuilder.loadTexts:mpAtmCCSoftPvpCalledTable.setStatus(_A)
_MpAtmCCSoftPvpCalledEntry_Object=MibTableRow
mpAtmCCSoftPvpCalledEntry=_MpAtmCCSoftPvpCalledEntry_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,3,1))
mpAtmCCSoftPvpCalledEntry.setIndexNames((0,_E,_y),(0,_E,_z),(0,_E,_A0))
if mibBuilder.loadTexts:mpAtmCCSoftPvpCalledEntry.setStatus(_A)
class _MpAtmCCSoftPvpCalledLeafReference_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_MpAtmCCSoftPvpCalledLeafReference_Type.__name__=_C
_MpAtmCCSoftPvpCalledLeafReference_Object=MibTableColumn
mpAtmCCSoftPvpCalledLeafReference=_MpAtmCCSoftPvpCalledLeafReference_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,3,1,1),_MpAtmCCSoftPvpCalledLeafReference_Type())
mpAtmCCSoftPvpCalledLeafReference.setMaxAccess(_F)
if mibBuilder.loadTexts:mpAtmCCSoftPvpCalledLeafReference.setStatus(_A)
_MpAtmCCSoftPvpCalledIfIndex_Type=Integer32
_MpAtmCCSoftPvpCalledIfIndex_Object=MibTableColumn
mpAtmCCSoftPvpCalledIfIndex=_MpAtmCCSoftPvpCalledIfIndex_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,3,1,2),_MpAtmCCSoftPvpCalledIfIndex_Type())
mpAtmCCSoftPvpCalledIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:mpAtmCCSoftPvpCalledIfIndex.setStatus(_A)
_MpAtmCCSoftPvpCalledVpi_Type=Integer32
_MpAtmCCSoftPvpCalledVpi_Object=MibTableColumn
mpAtmCCSoftPvpCalledVpi=_MpAtmCCSoftPvpCalledVpi_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,3,1,3),_MpAtmCCSoftPvpCalledVpi_Type())
mpAtmCCSoftPvpCalledVpi.setMaxAccess(_F)
if mibBuilder.loadTexts:mpAtmCCSoftPvpCalledVpi.setStatus(_A)
_MpAtmCCSoftPvpCalledReceiveTrafficDescrIndex_Type=AtmTrafficDescrParamIndex
_MpAtmCCSoftPvpCalledReceiveTrafficDescrIndex_Object=MibTableColumn
mpAtmCCSoftPvpCalledReceiveTrafficDescrIndex=_MpAtmCCSoftPvpCalledReceiveTrafficDescrIndex_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,3,1,4),_MpAtmCCSoftPvpCalledReceiveTrafficDescrIndex_Type())
mpAtmCCSoftPvpCalledReceiveTrafficDescrIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCSoftPvpCalledReceiveTrafficDescrIndex.setStatus(_A)
_MpAtmCCSoftPvpCalledTransmitTrafficDescrIndex_Type=AtmTrafficDescrParamIndex
_MpAtmCCSoftPvpCalledTransmitTrafficDescrIndex_Object=MibTableColumn
mpAtmCCSoftPvpCalledTransmitTrafficDescrIndex=_MpAtmCCSoftPvpCalledTransmitTrafficDescrIndex_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,3,1,5),_MpAtmCCSoftPvpCalledTransmitTrafficDescrIndex_Type())
mpAtmCCSoftPvpCalledTransmitTrafficDescrIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCSoftPvpCalledTransmitTrafficDescrIndex.setStatus(_A)
_MpAtmCCSoftPvpCalledTargetAddress_Type=AtmAddr
_MpAtmCCSoftPvpCalledTargetAddress_Object=MibTableColumn
mpAtmCCSoftPvpCalledTargetAddress=_MpAtmCCSoftPvpCalledTargetAddress_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,3,1,6),_MpAtmCCSoftPvpCalledTargetAddress_Type())
mpAtmCCSoftPvpCalledTargetAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCSoftPvpCalledTargetAddress.setStatus(_A)
class _MpAtmCCSoftPvpCalledTargetVpi_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_MpAtmCCSoftPvpCalledTargetVpi_Type.__name__=_C
_MpAtmCCSoftPvpCalledTargetVpi_Object=MibTableColumn
mpAtmCCSoftPvpCalledTargetVpi=_MpAtmCCSoftPvpCalledTargetVpi_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,3,1,7),_MpAtmCCSoftPvpCalledTargetVpi_Type())
mpAtmCCSoftPvpCalledTargetVpi.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCSoftPvpCalledTargetVpi.setStatus(_A)
class _MpAtmCCSoftPvpCalledLastReleaseCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,127))
_MpAtmCCSoftPvpCalledLastReleaseCause_Type.__name__=_C
_MpAtmCCSoftPvpCalledLastReleaseCause_Object=MibTableColumn
mpAtmCCSoftPvpCalledLastReleaseCause=_MpAtmCCSoftPvpCalledLastReleaseCause_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,3,1,8),_MpAtmCCSoftPvpCalledLastReleaseCause_Type())
mpAtmCCSoftPvpCalledLastReleaseCause.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCSoftPvpCalledLastReleaseCause.setStatus(_A)
class _MpAtmCCSoftPvpCalledLastReleaseDiagnostic_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_MpAtmCCSoftPvpCalledLastReleaseDiagnostic_Type.__name__=_P
_MpAtmCCSoftPvpCalledLastReleaseDiagnostic_Object=MibTableColumn
mpAtmCCSoftPvpCalledLastReleaseDiagnostic=_MpAtmCCSoftPvpCalledLastReleaseDiagnostic_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,3,1,9),_MpAtmCCSoftPvpCalledLastReleaseDiagnostic_Type())
mpAtmCCSoftPvpCalledLastReleaseDiagnostic.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCSoftPvpCalledLastReleaseDiagnostic.setStatus(_A)
class _MpAtmCCSoftPvpCalledPriority_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_MpAtmCCSoftPvpCalledPriority_Type.__name__=_C
_MpAtmCCSoftPvpCalledPriority_Object=MibTableColumn
mpAtmCCSoftPvpCalledPriority=_MpAtmCCSoftPvpCalledPriority_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,3,1,10),_MpAtmCCSoftPvpCalledPriority_Type())
mpAtmCCSoftPvpCalledPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCSoftPvpCalledPriority.setStatus(_A)
_MpAtmCCSoftPvpCalledCladType_Type=MpAtmCCCladType
_MpAtmCCSoftPvpCalledCladType_Object=MibTableColumn
mpAtmCCSoftPvpCalledCladType=_MpAtmCCSoftPvpCalledCladType_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,3,1,11),_MpAtmCCSoftPvpCalledCladType_Type())
mpAtmCCSoftPvpCalledCladType.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCSoftPvpCalledCladType.setStatus(_A)
_MpAtmCCSoftPvpCalledOriginalAddress_Type=AtmAddr
_MpAtmCCSoftPvpCalledOriginalAddress_Object=MibTableColumn
mpAtmCCSoftPvpCalledOriginalAddress=_MpAtmCCSoftPvpCalledOriginalAddress_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,3,1,12),_MpAtmCCSoftPvpCalledOriginalAddress_Type())
mpAtmCCSoftPvpCalledOriginalAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCSoftPvpCalledOriginalAddress.setStatus(_A)
class _MpAtmCCSoftPvpCalledAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_MpAtmCCSoftPvpCalledAdminStatus_Type.__name__=_C
_MpAtmCCSoftPvpCalledAdminStatus_Object=MibTableColumn
mpAtmCCSoftPvpCalledAdminStatus=_MpAtmCCSoftPvpCalledAdminStatus_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,3,1,13),_MpAtmCCSoftPvpCalledAdminStatus_Type())
mpAtmCCSoftPvpCalledAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCSoftPvpCalledAdminStatus.setStatus(_A)
_MpAtmCCSoftPvpCalledOperStatus_Type=Integer32
_MpAtmCCSoftPvpCalledOperStatus_Object=MibTableColumn
mpAtmCCSoftPvpCalledOperStatus=_MpAtmCCSoftPvpCalledOperStatus_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,3,1,14),_MpAtmCCSoftPvpCalledOperStatus_Type())
mpAtmCCSoftPvpCalledOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCSoftPvpCalledOperStatus.setStatus(_A)
_MpAtmCCSoftPvpCalledPgcRequest_Type=Integer32
_MpAtmCCSoftPvpCalledPgcRequest_Object=MibTableColumn
mpAtmCCSoftPvpCalledPgcRequest=_MpAtmCCSoftPvpCalledPgcRequest_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,3,1,15),_MpAtmCCSoftPvpCalledPgcRequest_Type())
mpAtmCCSoftPvpCalledPgcRequest.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCSoftPvpCalledPgcRequest.setStatus(_A)
class _MpAtmCCSoftPvpCalledCfgStatus_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_M,1),(_N,2),(_K,3),(_L,4)))
_MpAtmCCSoftPvpCalledCfgStatus_Type.__name__=_C
_MpAtmCCSoftPvpCalledCfgStatus_Object=MibTableColumn
mpAtmCCSoftPvpCalledCfgStatus=_MpAtmCCSoftPvpCalledCfgStatus_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,3,1,98),_MpAtmCCSoftPvpCalledCfgStatus_Type())
mpAtmCCSoftPvpCalledCfgStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCSoftPvpCalledCfgStatus.setStatus(_A)
_MpAtmCCSoftPvpCalledErrInfo_Type=Integer32
_MpAtmCCSoftPvpCalledErrInfo_Object=MibTableColumn
mpAtmCCSoftPvpCalledErrInfo=_MpAtmCCSoftPvpCalledErrInfo_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,3,1,99),_MpAtmCCSoftPvpCalledErrInfo_Type())
mpAtmCCSoftPvpCalledErrInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCSoftPvpCalledErrInfo.setStatus(_A)
_MpAtmCCSoftPvcCalledTable_Object=MibTable
mpAtmCCSoftPvcCalledTable=_MpAtmCCSoftPvcCalledTable_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,4))
if mibBuilder.loadTexts:mpAtmCCSoftPvcCalledTable.setStatus(_A)
_MpAtmCCSoftPvcCalledEntry_Object=MibTableRow
mpAtmCCSoftPvcCalledEntry=_MpAtmCCSoftPvcCalledEntry_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,4,1))
mpAtmCCSoftPvcCalledEntry.setIndexNames((0,_E,_A1),(0,_E,_A2),(0,_E,_A3),(0,_E,_A4))
if mibBuilder.loadTexts:mpAtmCCSoftPvcCalledEntry.setStatus(_A)
class _MpAtmCCSoftPvcCalledLeafReference_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_MpAtmCCSoftPvcCalledLeafReference_Type.__name__=_C
_MpAtmCCSoftPvcCalledLeafReference_Object=MibTableColumn
mpAtmCCSoftPvcCalledLeafReference=_MpAtmCCSoftPvcCalledLeafReference_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,4,1,1),_MpAtmCCSoftPvcCalledLeafReference_Type())
mpAtmCCSoftPvcCalledLeafReference.setMaxAccess(_F)
if mibBuilder.loadTexts:mpAtmCCSoftPvcCalledLeafReference.setStatus(_A)
_MpAtmCCSoftPvcCalledIfIndex_Type=Integer32
_MpAtmCCSoftPvcCalledIfIndex_Object=MibTableColumn
mpAtmCCSoftPvcCalledIfIndex=_MpAtmCCSoftPvcCalledIfIndex_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,4,1,2),_MpAtmCCSoftPvcCalledIfIndex_Type())
mpAtmCCSoftPvcCalledIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:mpAtmCCSoftPvcCalledIfIndex.setStatus(_A)
_MpAtmCCSoftPvcCalledVpi_Type=Integer32
_MpAtmCCSoftPvcCalledVpi_Object=MibTableColumn
mpAtmCCSoftPvcCalledVpi=_MpAtmCCSoftPvcCalledVpi_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,4,1,3),_MpAtmCCSoftPvcCalledVpi_Type())
mpAtmCCSoftPvcCalledVpi.setMaxAccess(_F)
if mibBuilder.loadTexts:mpAtmCCSoftPvcCalledVpi.setStatus(_A)
_MpAtmCCSoftPvcCalledVci_Type=Integer32
_MpAtmCCSoftPvcCalledVci_Object=MibTableColumn
mpAtmCCSoftPvcCalledVci=_MpAtmCCSoftPvcCalledVci_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,4,1,4),_MpAtmCCSoftPvcCalledVci_Type())
mpAtmCCSoftPvcCalledVci.setMaxAccess(_F)
if mibBuilder.loadTexts:mpAtmCCSoftPvcCalledVci.setStatus(_A)
_MpAtmCCSoftPvcCalledReceiveTrafficDescrIndex_Type=AtmTrafficDescrParamIndex
_MpAtmCCSoftPvcCalledReceiveTrafficDescrIndex_Object=MibTableColumn
mpAtmCCSoftPvcCalledReceiveTrafficDescrIndex=_MpAtmCCSoftPvcCalledReceiveTrafficDescrIndex_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,4,1,5),_MpAtmCCSoftPvcCalledReceiveTrafficDescrIndex_Type())
mpAtmCCSoftPvcCalledReceiveTrafficDescrIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCSoftPvcCalledReceiveTrafficDescrIndex.setStatus(_A)
_MpAtmCCSoftPvcCalledTransmitTrafficDescrIndex_Type=AtmTrafficDescrParamIndex
_MpAtmCCSoftPvcCalledTransmitTrafficDescrIndex_Object=MibTableColumn
mpAtmCCSoftPvcCalledTransmitTrafficDescrIndex=_MpAtmCCSoftPvcCalledTransmitTrafficDescrIndex_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,4,1,6),_MpAtmCCSoftPvcCalledTransmitTrafficDescrIndex_Type())
mpAtmCCSoftPvcCalledTransmitTrafficDescrIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCSoftPvcCalledTransmitTrafficDescrIndex.setStatus(_A)
_MpAtmCCSoftPvcCalledTargetAddress_Type=AtmAddr
_MpAtmCCSoftPvcCalledTargetAddress_Object=MibTableColumn
mpAtmCCSoftPvcCalledTargetAddress=_MpAtmCCSoftPvcCalledTargetAddress_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,4,1,7),_MpAtmCCSoftPvcCalledTargetAddress_Type())
mpAtmCCSoftPvcCalledTargetAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCSoftPvcCalledTargetAddress.setStatus(_A)
class _MpAtmCCSoftPvcCalledTargetVpi_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_MpAtmCCSoftPvcCalledTargetVpi_Type.__name__=_C
_MpAtmCCSoftPvcCalledTargetVpi_Object=MibTableColumn
mpAtmCCSoftPvcCalledTargetVpi=_MpAtmCCSoftPvcCalledTargetVpi_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,4,1,8),_MpAtmCCSoftPvcCalledTargetVpi_Type())
mpAtmCCSoftPvcCalledTargetVpi.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCSoftPvcCalledTargetVpi.setStatus(_A)
class _MpAtmCCSoftPvcCalledTargetVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MpAtmCCSoftPvcCalledTargetVci_Type.__name__=_C
_MpAtmCCSoftPvcCalledTargetVci_Object=MibTableColumn
mpAtmCCSoftPvcCalledTargetVci=_MpAtmCCSoftPvcCalledTargetVci_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,4,1,9),_MpAtmCCSoftPvcCalledTargetVci_Type())
mpAtmCCSoftPvcCalledTargetVci.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCSoftPvcCalledTargetVci.setStatus(_A)
class _MpAtmCCSoftPvcCalledLastReleaseCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,127))
_MpAtmCCSoftPvcCalledLastReleaseCause_Type.__name__=_C
_MpAtmCCSoftPvcCalledLastReleaseCause_Object=MibTableColumn
mpAtmCCSoftPvcCalledLastReleaseCause=_MpAtmCCSoftPvcCalledLastReleaseCause_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,4,1,10),_MpAtmCCSoftPvcCalledLastReleaseCause_Type())
mpAtmCCSoftPvcCalledLastReleaseCause.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCSoftPvcCalledLastReleaseCause.setStatus(_A)
class _MpAtmCCSoftPvcCalledLastReleaseDiagnostic_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_MpAtmCCSoftPvcCalledLastReleaseDiagnostic_Type.__name__=_P
_MpAtmCCSoftPvcCalledLastReleaseDiagnostic_Object=MibTableColumn
mpAtmCCSoftPvcCalledLastReleaseDiagnostic=_MpAtmCCSoftPvcCalledLastReleaseDiagnostic_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,4,1,11),_MpAtmCCSoftPvcCalledLastReleaseDiagnostic_Type())
mpAtmCCSoftPvcCalledLastReleaseDiagnostic.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCSoftPvcCalledLastReleaseDiagnostic.setStatus(_A)
class _MpAtmCCSoftPvcCalledPriority_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_MpAtmCCSoftPvcCalledPriority_Type.__name__=_C
_MpAtmCCSoftPvcCalledPriority_Object=MibTableColumn
mpAtmCCSoftPvcCalledPriority=_MpAtmCCSoftPvcCalledPriority_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,4,1,12),_MpAtmCCSoftPvcCalledPriority_Type())
mpAtmCCSoftPvcCalledPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCSoftPvcCalledPriority.setStatus(_A)
_MpAtmCCSoftPvcCalledCladType_Type=MpAtmCCCladType
_MpAtmCCSoftPvcCalledCladType_Object=MibTableColumn
mpAtmCCSoftPvcCalledCladType=_MpAtmCCSoftPvcCalledCladType_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,4,1,13),_MpAtmCCSoftPvcCalledCladType_Type())
mpAtmCCSoftPvcCalledCladType.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCSoftPvcCalledCladType.setStatus(_A)
_MpAtmCCSoftPvcCalledOriginalAddress_Type=AtmAddr
_MpAtmCCSoftPvcCalledOriginalAddress_Object=MibTableColumn
mpAtmCCSoftPvcCalledOriginalAddress=_MpAtmCCSoftPvcCalledOriginalAddress_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,4,1,14),_MpAtmCCSoftPvcCalledOriginalAddress_Type())
mpAtmCCSoftPvcCalledOriginalAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCSoftPvcCalledOriginalAddress.setStatus(_A)
class _MpAtmCCSoftPvcCalledAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_MpAtmCCSoftPvcCalledAdminStatus_Type.__name__=_C
_MpAtmCCSoftPvcCalledAdminStatus_Object=MibTableColumn
mpAtmCCSoftPvcCalledAdminStatus=_MpAtmCCSoftPvcCalledAdminStatus_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,4,1,15),_MpAtmCCSoftPvcCalledAdminStatus_Type())
mpAtmCCSoftPvcCalledAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCSoftPvcCalledAdminStatus.setStatus(_A)
_MpAtmCCSoftPvcCalledOperStatus_Type=Integer32
_MpAtmCCSoftPvcCalledOperStatus_Object=MibTableColumn
mpAtmCCSoftPvcCalledOperStatus=_MpAtmCCSoftPvcCalledOperStatus_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,4,1,16),_MpAtmCCSoftPvcCalledOperStatus_Type())
mpAtmCCSoftPvcCalledOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCSoftPvcCalledOperStatus.setStatus(_A)
_MpAtmCCSoftPvcCalledPgcRequest_Type=Integer32
_MpAtmCCSoftPvcCalledPgcRequest_Object=MibTableColumn
mpAtmCCSoftPvcCalledPgcRequest=_MpAtmCCSoftPvcCalledPgcRequest_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,4,1,17),_MpAtmCCSoftPvcCalledPgcRequest_Type())
mpAtmCCSoftPvcCalledPgcRequest.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCSoftPvcCalledPgcRequest.setStatus(_A)
class _MpAtmCCSoftPvcCalledCfgStatus_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_M,1),(_N,2),(_K,3),(_L,4)))
_MpAtmCCSoftPvcCalledCfgStatus_Type.__name__=_C
_MpAtmCCSoftPvcCalledCfgStatus_Object=MibTableColumn
mpAtmCCSoftPvcCalledCfgStatus=_MpAtmCCSoftPvcCalledCfgStatus_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,4,1,98),_MpAtmCCSoftPvcCalledCfgStatus_Type())
mpAtmCCSoftPvcCalledCfgStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCSoftPvcCalledCfgStatus.setStatus(_A)
_MpAtmCCSoftPvcCalledErrInfo_Type=Integer32
_MpAtmCCSoftPvcCalledErrInfo_Object=MibTableColumn
mpAtmCCSoftPvcCalledErrInfo=_MpAtmCCSoftPvcCalledErrInfo_Object((1,3,6,1,4,1,119,2,3,3,13,110,3,4,1,99),_MpAtmCCSoftPvcCalledErrInfo_Type())
mpAtmCCSoftPvcCalledErrInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCSoftPvcCalledErrInfo.setStatus(_A)
_MpAtmCCStatistics_ObjectIdentity=ObjectIdentity
mpAtmCCStatistics=_MpAtmCCStatistics_ObjectIdentity((1,3,6,1,4,1,119,2,3,3,13,110,4))
_MpAtmCCVpStatisticsTable_Object=MibTable
mpAtmCCVpStatisticsTable=_MpAtmCCVpStatisticsTable_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,1))
if mibBuilder.loadTexts:mpAtmCCVpStatisticsTable.setStatus(_A)
_MpAtmCCVpStatisticsEntry_Object=MibTableRow
mpAtmCCVpStatisticsEntry=_MpAtmCCVpStatisticsEntry_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,1,1))
mpAtmCCVpStatisticsEntry.setIndexNames((0,_I,_J),(0,_E,_A5))
if mibBuilder.loadTexts:mpAtmCCVpStatisticsEntry.setStatus(_A)
_MpAtmCCVpStatVpi_Type=Integer32
_MpAtmCCVpStatVpi_Object=MibTableColumn
mpAtmCCVpStatVpi=_MpAtmCCVpStatVpi_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,1,1,1),_MpAtmCCVpStatVpi_Type())
mpAtmCCVpStatVpi.setMaxAccess(_F)
if mibBuilder.loadTexts:mpAtmCCVpStatVpi.setStatus(_A)
_MpAtmCCVpStatInCells_Type=OctetString
_MpAtmCCVpStatInCells_Object=MibTableColumn
mpAtmCCVpStatInCells=_MpAtmCCVpStatInCells_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,1,1,2),_MpAtmCCVpStatInCells_Type())
mpAtmCCVpStatInCells.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCVpStatInCells.setStatus(_A)
_MpAtmCCVpStatInCellsCounters_Type=Counter32
_MpAtmCCVpStatInCellsCounters_Object=MibTableColumn
mpAtmCCVpStatInCellsCounters=_MpAtmCCVpStatInCellsCounters_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,1,1,3),_MpAtmCCVpStatInCellsCounters_Type())
mpAtmCCVpStatInCellsCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCVpStatInCellsCounters.setStatus(_A)
_MpAtmCCVpStatOutCells_Type=OctetString
_MpAtmCCVpStatOutCells_Object=MibTableColumn
mpAtmCCVpStatOutCells=_MpAtmCCVpStatOutCells_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,1,1,4),_MpAtmCCVpStatOutCells_Type())
mpAtmCCVpStatOutCells.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCVpStatOutCells.setStatus(_A)
_MpAtmCCVpStatOutCellsCounters_Type=Counter32
_MpAtmCCVpStatOutCellsCounters_Object=MibTableColumn
mpAtmCCVpStatOutCellsCounters=_MpAtmCCVpStatOutCellsCounters_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,1,1,5),_MpAtmCCVpStatOutCellsCounters_Type())
mpAtmCCVpStatOutCellsCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCVpStatOutCellsCounters.setStatus(_A)
_MpAtmCCVpStatInDropCells_Type=OctetString
_MpAtmCCVpStatInDropCells_Object=MibTableColumn
mpAtmCCVpStatInDropCells=_MpAtmCCVpStatInDropCells_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,1,1,6),_MpAtmCCVpStatInDropCells_Type())
mpAtmCCVpStatInDropCells.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCVpStatInDropCells.setStatus(_A)
_MpAtmCCVpStatInDropCellsCounters_Type=Counter32
_MpAtmCCVpStatInDropCellsCounters_Object=MibTableColumn
mpAtmCCVpStatInDropCellsCounters=_MpAtmCCVpStatInDropCellsCounters_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,1,1,7),_MpAtmCCVpStatInDropCellsCounters_Type())
mpAtmCCVpStatInDropCellsCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCVpStatInDropCellsCounters.setStatus(_A)
_MpAtmCCVcStatisticsTable_Object=MibTable
mpAtmCCVcStatisticsTable=_MpAtmCCVcStatisticsTable_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,2))
if mibBuilder.loadTexts:mpAtmCCVcStatisticsTable.setStatus(_A)
_MpAtmCCVcStatisticsEntry_Object=MibTableRow
mpAtmCCVcStatisticsEntry=_MpAtmCCVcStatisticsEntry_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,2,1))
mpAtmCCVcStatisticsEntry.setIndexNames((0,_I,_J),(0,_E,_A6),(0,_E,_A7))
if mibBuilder.loadTexts:mpAtmCCVcStatisticsEntry.setStatus(_A)
_MpAtmCCVcStatVpi_Type=Integer32
_MpAtmCCVcStatVpi_Object=MibTableColumn
mpAtmCCVcStatVpi=_MpAtmCCVcStatVpi_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,2,1,1),_MpAtmCCVcStatVpi_Type())
mpAtmCCVcStatVpi.setMaxAccess(_F)
if mibBuilder.loadTexts:mpAtmCCVcStatVpi.setStatus(_A)
_MpAtmCCVcStatVci_Type=Integer32
_MpAtmCCVcStatVci_Object=MibTableColumn
mpAtmCCVcStatVci=_MpAtmCCVcStatVci_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,2,1,2),_MpAtmCCVcStatVci_Type())
mpAtmCCVcStatVci.setMaxAccess(_F)
if mibBuilder.loadTexts:mpAtmCCVcStatVci.setStatus(_A)
_MpAtmCCVcStatInCells_Type=OctetString
_MpAtmCCVcStatInCells_Object=MibTableColumn
mpAtmCCVcStatInCells=_MpAtmCCVcStatInCells_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,2,1,3),_MpAtmCCVcStatInCells_Type())
mpAtmCCVcStatInCells.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCVcStatInCells.setStatus(_A)
_MpAtmCCVcStatInCellsCounters_Type=Counter32
_MpAtmCCVcStatInCellsCounters_Object=MibTableColumn
mpAtmCCVcStatInCellsCounters=_MpAtmCCVcStatInCellsCounters_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,2,1,4),_MpAtmCCVcStatInCellsCounters_Type())
mpAtmCCVcStatInCellsCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCVcStatInCellsCounters.setStatus(_A)
_MpAtmCCVcStatOutCells_Type=OctetString
_MpAtmCCVcStatOutCells_Object=MibTableColumn
mpAtmCCVcStatOutCells=_MpAtmCCVcStatOutCells_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,2,1,5),_MpAtmCCVcStatOutCells_Type())
mpAtmCCVcStatOutCells.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCVcStatOutCells.setStatus(_A)
_MpAtmCCVcStatOutCellsCounters_Type=Counter32
_MpAtmCCVcStatOutCellsCounters_Object=MibTableColumn
mpAtmCCVcStatOutCellsCounters=_MpAtmCCVcStatOutCellsCounters_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,2,1,6),_MpAtmCCVcStatOutCellsCounters_Type())
mpAtmCCVcStatOutCellsCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCVcStatOutCellsCounters.setStatus(_A)
_MpAtmCCVcStatInDropCells_Type=OctetString
_MpAtmCCVcStatInDropCells_Object=MibTableColumn
mpAtmCCVcStatInDropCells=_MpAtmCCVcStatInDropCells_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,2,1,7),_MpAtmCCVcStatInDropCells_Type())
mpAtmCCVcStatInDropCells.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCVcStatInDropCells.setStatus(_A)
_MpAtmCCVcStatInDropCellsCounters_Type=Counter32
_MpAtmCCVcStatInDropCellsCounters_Object=MibTableColumn
mpAtmCCVcStatInDropCellsCounters=_MpAtmCCVcStatInDropCellsCounters_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,2,1,8),_MpAtmCCVcStatInDropCellsCounters_Type())
mpAtmCCVcStatInDropCellsCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCVcStatInDropCellsCounters.setStatus(_A)
_MpAtmCCOuspStatisticsTable_Object=MibTable
mpAtmCCOuspStatisticsTable=_MpAtmCCOuspStatisticsTable_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,3))
if mibBuilder.loadTexts:mpAtmCCOuspStatisticsTable.setStatus(_A)
_MpAtmCCOuspStatisticsEntry_Object=MibTableRow
mpAtmCCOuspStatisticsEntry=_MpAtmCCOuspStatisticsEntry_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,3,1))
mpAtmCCOuspStatisticsEntry.setIndexNames((0,_E,_A8))
if mibBuilder.loadTexts:mpAtmCCOuspStatisticsEntry.setStatus(_A)
_MpAtmCCOuspStatIndex_Type=Integer32
_MpAtmCCOuspStatIndex_Object=MibTableColumn
mpAtmCCOuspStatIndex=_MpAtmCCOuspStatIndex_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,3,1,1),_MpAtmCCOuspStatIndex_Type())
mpAtmCCOuspStatIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:mpAtmCCOuspStatIndex.setStatus(_A)
_MpAtmCCOuspStatRcvCrcErrCellsCounters_Type=Counter32
_MpAtmCCOuspStatRcvCrcErrCellsCounters_Object=MibTableColumn
mpAtmCCOuspStatRcvCrcErrCellsCounters=_MpAtmCCOuspStatRcvCrcErrCellsCounters_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,3,1,2),_MpAtmCCOuspStatRcvCrcErrCellsCounters_Type())
mpAtmCCOuspStatRcvCrcErrCellsCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCOuspStatRcvCrcErrCellsCounters.setStatus(_A)
_MpAtmCCOuspStatSendOfifoFullCounters_Type=Counter32
_MpAtmCCOuspStatSendOfifoFullCounters_Object=MibTableColumn
mpAtmCCOuspStatSendOfifoFullCounters=_MpAtmCCOuspStatSendOfifoFullCounters_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,3,1,3),_MpAtmCCOuspStatSendOfifoFullCounters_Type())
mpAtmCCOuspStatSendOfifoFullCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCOuspStatSendOfifoFullCounters.setStatus(_A)
_MpAtmCCOuspStatRcvBufOverCounters_Type=Counter32
_MpAtmCCOuspStatRcvBufOverCounters_Object=MibTableColumn
mpAtmCCOuspStatRcvBufOverCounters=_MpAtmCCOuspStatRcvBufOverCounters_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,3,1,4),_MpAtmCCOuspStatRcvBufOverCounters_Type())
mpAtmCCOuspStatRcvBufOverCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCOuspStatRcvBufOverCounters.setStatus(_A)
_MpAtmCCOuspStatRcvUnknownCellsCounters_Type=Counter32
_MpAtmCCOuspStatRcvUnknownCellsCounters_Object=MibTableColumn
mpAtmCCOuspStatRcvUnknownCellsCounters=_MpAtmCCOuspStatRcvUnknownCellsCounters_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,3,1,5),_MpAtmCCOuspStatRcvUnknownCellsCounters_Type())
mpAtmCCOuspStatRcvUnknownCellsCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCOuspStatRcvUnknownCellsCounters.setStatus(_A)
_MpAtmCCOuspStatRcvInvalidCellsCounters_Type=Counter32
_MpAtmCCOuspStatRcvInvalidCellsCounters_Object=MibTableColumn
mpAtmCCOuspStatRcvInvalidCellsCounters=_MpAtmCCOuspStatRcvInvalidCellsCounters_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,3,1,6),_MpAtmCCOuspStatRcvInvalidCellsCounters_Type())
mpAtmCCOuspStatRcvInvalidCellsCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCOuspStatRcvInvalidCellsCounters.setStatus(_A)
_MpAtmCCOuspStatSendScheduleErrorCounters_Type=Counter32
_MpAtmCCOuspStatSendScheduleErrorCounters_Object=MibTableColumn
mpAtmCCOuspStatSendScheduleErrorCounters=_MpAtmCCOuspStatSendScheduleErrorCounters_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,3,1,7),_MpAtmCCOuspStatSendScheduleErrorCounters_Type())
mpAtmCCOuspStatSendScheduleErrorCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCOuspStatSendScheduleErrorCounters.setStatus(_A)
_MpAtmCCOuspStatRcvScheduleErrorCounters_Type=Counter32
_MpAtmCCOuspStatRcvScheduleErrorCounters_Object=MibTableColumn
mpAtmCCOuspStatRcvScheduleErrorCounters=_MpAtmCCOuspStatRcvScheduleErrorCounters_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,3,1,8),_MpAtmCCOuspStatRcvScheduleErrorCounters_Type())
mpAtmCCOuspStatRcvScheduleErrorCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCOuspStatRcvScheduleErrorCounters.setStatus(_A)
_MpAtmCCOuspStatSendInvalidCdvCounters_Type=Counter32
_MpAtmCCOuspStatSendInvalidCdvCounters_Object=MibTableColumn
mpAtmCCOuspStatSendInvalidCdvCounters=_MpAtmCCOuspStatSendInvalidCdvCounters_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,3,1,9),_MpAtmCCOuspStatSendInvalidCdvCounters_Type())
mpAtmCCOuspStatSendInvalidCdvCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCOuspStatSendInvalidCdvCounters.setStatus(_A)
_MpAtmCCPhyStatisticsTable_Object=MibTable
mpAtmCCPhyStatisticsTable=_MpAtmCCPhyStatisticsTable_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,4))
if mibBuilder.loadTexts:mpAtmCCPhyStatisticsTable.setStatus(_A)
_MpAtmCCPhyStatisticsEntry_Object=MibTableRow
mpAtmCCPhyStatisticsEntry=_MpAtmCCPhyStatisticsEntry_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,4,1))
mpAtmCCPhyStatisticsEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:mpAtmCCPhyStatisticsEntry.setStatus(_A)
_MpAtmCCPhyStatTmtCellsCounters_Type=Counter32
_MpAtmCCPhyStatTmtCellsCounters_Object=MibTableColumn
mpAtmCCPhyStatTmtCellsCounters=_MpAtmCCPhyStatTmtCellsCounters_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,4,1,1),_MpAtmCCPhyStatTmtCellsCounters_Type())
mpAtmCCPhyStatTmtCellsCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPhyStatTmtCellsCounters.setStatus(_A)
_MpAtmCCPhyStatRcvCellsCounters_Type=Counter32
_MpAtmCCPhyStatRcvCellsCounters_Object=MibTableColumn
mpAtmCCPhyStatRcvCellsCounters=_MpAtmCCPhyStatRcvCellsCounters_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,4,1,2),_MpAtmCCPhyStatRcvCellsCounters_Type())
mpAtmCCPhyStatRcvCellsCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPhyStatRcvCellsCounters.setStatus(_A)
_MpAtmCCPhyStatCorrectHecErrCounters_Type=Counter32
_MpAtmCCPhyStatCorrectHecErrCounters_Object=MibTableColumn
mpAtmCCPhyStatCorrectHecErrCounters=_MpAtmCCPhyStatCorrectHecErrCounters_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,4,1,3),_MpAtmCCPhyStatCorrectHecErrCounters_Type())
mpAtmCCPhyStatCorrectHecErrCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPhyStatCorrectHecErrCounters.setStatus(_A)
_MpAtmCCPhyStatUncorrectHecErrCounters_Type=Counter32
_MpAtmCCPhyStatUncorrectHecErrCounters_Object=MibTableColumn
mpAtmCCPhyStatUncorrectHecErrCounters=_MpAtmCCPhyStatUncorrectHecErrCounters_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,4,1,4),_MpAtmCCPhyStatUncorrectHecErrCounters_Type())
mpAtmCCPhyStatUncorrectHecErrCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPhyStatUncorrectHecErrCounters.setStatus(_A)
_MpAtmCCPhyStatB1ErrCounters_Type=Counter32
_MpAtmCCPhyStatB1ErrCounters_Object=MibTableColumn
mpAtmCCPhyStatB1ErrCounters=_MpAtmCCPhyStatB1ErrCounters_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,4,1,5),_MpAtmCCPhyStatB1ErrCounters_Type())
mpAtmCCPhyStatB1ErrCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPhyStatB1ErrCounters.setStatus(_A)
_MpAtmCCPhyStatB2ErrCounters_Type=Counter32
_MpAtmCCPhyStatB2ErrCounters_Object=MibTableColumn
mpAtmCCPhyStatB2ErrCounters=_MpAtmCCPhyStatB2ErrCounters_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,4,1,6),_MpAtmCCPhyStatB2ErrCounters_Type())
mpAtmCCPhyStatB2ErrCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPhyStatB2ErrCounters.setStatus(_A)
_MpAtmCCPhyStatB3ErrCounters_Type=Counter32
_MpAtmCCPhyStatB3ErrCounters_Object=MibTableColumn
mpAtmCCPhyStatB3ErrCounters=_MpAtmCCPhyStatB3ErrCounters_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,4,1,7),_MpAtmCCPhyStatB3ErrCounters_Type())
mpAtmCCPhyStatB3ErrCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPhyStatB3ErrCounters.setStatus(_A)
_MpAtmCCPhyStatFebeCounters_Type=Counter32
_MpAtmCCPhyStatFebeCounters_Object=MibTableColumn
mpAtmCCPhyStatFebeCounters=_MpAtmCCPhyStatFebeCounters_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,4,1,8),_MpAtmCCPhyStatFebeCounters_Type())
mpAtmCCPhyStatFebeCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPhyStatFebeCounters.setStatus(_A)
_MpAtmCCPhyStatSymbolErrCounters_Type=Counter32
_MpAtmCCPhyStatSymbolErrCounters_Object=MibTableColumn
mpAtmCCPhyStatSymbolErrCounters=_MpAtmCCPhyStatSymbolErrCounters_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,4,1,9),_MpAtmCCPhyStatSymbolErrCounters_Type())
mpAtmCCPhyStatSymbolErrCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPhyStatSymbolErrCounters.setStatus(_A)
_MpAtmCCPhyStatParityErrCounters_Type=Counter32
_MpAtmCCPhyStatParityErrCounters_Object=MibTableColumn
mpAtmCCPhyStatParityErrCounters=_MpAtmCCPhyStatParityErrCounters_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,4,1,10),_MpAtmCCPhyStatParityErrCounters_Type())
mpAtmCCPhyStatParityErrCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPhyStatParityErrCounters.setStatus(_A)
_MpAtmCCPortAlarmStatisticsTable_Object=MibTable
mpAtmCCPortAlarmStatisticsTable=_MpAtmCCPortAlarmStatisticsTable_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,5))
if mibBuilder.loadTexts:mpAtmCCPortAlarmStatisticsTable.setStatus(_A)
_MpAtmCCPortAlarmStatisticsEntry_Object=MibTableRow
mpAtmCCPortAlarmStatisticsEntry=_MpAtmCCPortAlarmStatisticsEntry_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,5,1))
mpAtmCCPortAlarmStatisticsEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:mpAtmCCPortAlarmStatisticsEntry.setStatus(_A)
_MpAtmCCPortAlarmStatRedLosCounters_Type=Counter32
_MpAtmCCPortAlarmStatRedLosCounters_Object=MibTableColumn
mpAtmCCPortAlarmStatRedLosCounters=_MpAtmCCPortAlarmStatRedLosCounters_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,5,1,1),_MpAtmCCPortAlarmStatRedLosCounters_Type())
mpAtmCCPortAlarmStatRedLosCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPortAlarmStatRedLosCounters.setStatus(_A)
_MpAtmCCPortAlarmStatRedLofCounters_Type=Counter32
_MpAtmCCPortAlarmStatRedLofCounters_Object=MibTableColumn
mpAtmCCPortAlarmStatRedLofCounters=_MpAtmCCPortAlarmStatRedLofCounters_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,5,1,2),_MpAtmCCPortAlarmStatRedLofCounters_Type())
mpAtmCCPortAlarmStatRedLofCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPortAlarmStatRedLofCounters.setStatus(_A)
_MpAtmCCPortAlarmStatRedMsAisCounters_Type=Counter32
_MpAtmCCPortAlarmStatRedMsAisCounters_Object=MibTableColumn
mpAtmCCPortAlarmStatRedMsAisCounters=_MpAtmCCPortAlarmStatRedMsAisCounters_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,5,1,3),_MpAtmCCPortAlarmStatRedMsAisCounters_Type())
mpAtmCCPortAlarmStatRedMsAisCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPortAlarmStatRedMsAisCounters.setStatus(_A)
_MpAtmCCPortAlarmStatRedLopCounters_Type=Counter32
_MpAtmCCPortAlarmStatRedLopCounters_Object=MibTableColumn
mpAtmCCPortAlarmStatRedLopCounters=_MpAtmCCPortAlarmStatRedLopCounters_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,5,1,4),_MpAtmCCPortAlarmStatRedLopCounters_Type())
mpAtmCCPortAlarmStatRedLopCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPortAlarmStatRedLopCounters.setStatus(_A)
_MpAtmCCPortAlarmStatRedPAisCounters_Type=Counter32
_MpAtmCCPortAlarmStatRedPAisCounters_Object=MibTableColumn
mpAtmCCPortAlarmStatRedPAisCounters=_MpAtmCCPortAlarmStatRedPAisCounters_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,5,1,5),_MpAtmCCPortAlarmStatRedPAisCounters_Type())
mpAtmCCPortAlarmStatRedPAisCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPortAlarmStatRedPAisCounters.setStatus(_A)
_MpAtmCCPortAlarmStatRedLocCounters_Type=Counter32
_MpAtmCCPortAlarmStatRedLocCounters_Object=MibTableColumn
mpAtmCCPortAlarmStatRedLocCounters=_MpAtmCCPortAlarmStatRedLocCounters_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,5,1,6),_MpAtmCCPortAlarmStatRedLocCounters_Type())
mpAtmCCPortAlarmStatRedLocCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPortAlarmStatRedLocCounters.setStatus(_A)
_MpAtmCCPortAlarmStatRedResetCounters_Type=Counter32
_MpAtmCCPortAlarmStatRedResetCounters_Object=MibTableColumn
mpAtmCCPortAlarmStatRedResetCounters=_MpAtmCCPortAlarmStatRedResetCounters_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,5,1,7),_MpAtmCCPortAlarmStatRedResetCounters_Type())
mpAtmCCPortAlarmStatRedResetCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPortAlarmStatRedResetCounters.setStatus(_A)
_MpAtmCCPortAlarmStatRedCcRedCounters_Type=Counter32
_MpAtmCCPortAlarmStatRedCcRedCounters_Object=MibTableColumn
mpAtmCCPortAlarmStatRedCcRedCounters=_MpAtmCCPortAlarmStatRedCcRedCounters_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,5,1,8),_MpAtmCCPortAlarmStatRedCcRedCounters_Type())
mpAtmCCPortAlarmStatRedCcRedCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPortAlarmStatRedCcRedCounters.setStatus(_A)
_MpAtmCCPortAlarmStatRedOofCounters_Type=Counter32
_MpAtmCCPortAlarmStatRedOofCounters_Object=MibTableColumn
mpAtmCCPortAlarmStatRedOofCounters=_MpAtmCCPortAlarmStatRedOofCounters_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,5,1,9),_MpAtmCCPortAlarmStatRedOofCounters_Type())
mpAtmCCPortAlarmStatRedOofCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPortAlarmStatRedOofCounters.setStatus(_A)
_MpAtmCCPortAlarmStatRedAisCounters_Type=Counter32
_MpAtmCCPortAlarmStatRedAisCounters_Object=MibTableColumn
mpAtmCCPortAlarmStatRedAisCounters=_MpAtmCCPortAlarmStatRedAisCounters_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,5,1,10),_MpAtmCCPortAlarmStatRedAisCounters_Type())
mpAtmCCPortAlarmStatRedAisCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPortAlarmStatRedAisCounters.setStatus(_A)
_MpAtmCCPortAlarmStatRedPOofCounters_Type=Counter32
_MpAtmCCPortAlarmStatRedPOofCounters_Object=MibTableColumn
mpAtmCCPortAlarmStatRedPOofCounters=_MpAtmCCPortAlarmStatRedPOofCounters_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,5,1,11),_MpAtmCCPortAlarmStatRedPOofCounters_Type())
mpAtmCCPortAlarmStatRedPOofCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPortAlarmStatRedPOofCounters.setStatus(_A)
_MpAtmCCPortAlarmStatRedBadSigCounters_Type=Counter32
_MpAtmCCPortAlarmStatRedBadSigCounters_Object=MibTableColumn
mpAtmCCPortAlarmStatRedBadSigCounters=_MpAtmCCPortAlarmStatRedBadSigCounters_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,5,1,12),_MpAtmCCPortAlarmStatRedBadSigCounters_Type())
mpAtmCCPortAlarmStatRedBadSigCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPortAlarmStatRedBadSigCounters.setStatus(_A)
_MpAtmCCPortAlarmStatRedLcdCounters_Type=Counter32
_MpAtmCCPortAlarmStatRedLcdCounters_Object=MibTableColumn
mpAtmCCPortAlarmStatRedLcdCounters=_MpAtmCCPortAlarmStatRedLcdCounters_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,5,1,13),_MpAtmCCPortAlarmStatRedLcdCounters_Type())
mpAtmCCPortAlarmStatRedLcdCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPortAlarmStatRedLcdCounters.setStatus(_A)
_MpAtmCCPortAlarmStatRedLinkAisCounters_Type=Counter32
_MpAtmCCPortAlarmStatRedLinkAisCounters_Object=MibTableColumn
mpAtmCCPortAlarmStatRedLinkAisCounters=_MpAtmCCPortAlarmStatRedLinkAisCounters_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,5,1,14),_MpAtmCCPortAlarmStatRedLinkAisCounters_Type())
mpAtmCCPortAlarmStatRedLinkAisCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPortAlarmStatRedLinkAisCounters.setStatus(_A)
_MpAtmCCPortAlarmStatRedInfo0Counters_Type=Counter32
_MpAtmCCPortAlarmStatRedInfo0Counters_Object=MibTableColumn
mpAtmCCPortAlarmStatRedInfo0Counters=_MpAtmCCPortAlarmStatRedInfo0Counters_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,5,1,15),_MpAtmCCPortAlarmStatRedInfo0Counters_Type())
mpAtmCCPortAlarmStatRedInfo0Counters.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPortAlarmStatRedInfo0Counters.setStatus(_A)
_MpAtmCCPortAlarmStatYelMsRdiCounters_Type=Counter32
_MpAtmCCPortAlarmStatYelMsRdiCounters_Object=MibTableColumn
mpAtmCCPortAlarmStatYelMsRdiCounters=_MpAtmCCPortAlarmStatYelMsRdiCounters_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,5,1,16),_MpAtmCCPortAlarmStatYelMsRdiCounters_Type())
mpAtmCCPortAlarmStatYelMsRdiCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPortAlarmStatYelMsRdiCounters.setStatus(_A)
_MpAtmCCPortAlarmStatYelPRdiCounters_Type=Counter32
_MpAtmCCPortAlarmStatYelPRdiCounters_Object=MibTableColumn
mpAtmCCPortAlarmStatYelPRdiCounters=_MpAtmCCPortAlarmStatYelPRdiCounters_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,5,1,17),_MpAtmCCPortAlarmStatYelPRdiCounters_Type())
mpAtmCCPortAlarmStatYelPRdiCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPortAlarmStatYelPRdiCounters.setStatus(_A)
_MpAtmCCPortAlarmStatYelCcYelCounters_Type=Counter32
_MpAtmCCPortAlarmStatYelCcYelCounters_Object=MibTableColumn
mpAtmCCPortAlarmStatYelCcYelCounters=_MpAtmCCPortAlarmStatYelCcYelCounters_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,5,1,18),_MpAtmCCPortAlarmStatYelCcYelCounters_Type())
mpAtmCCPortAlarmStatYelCcYelCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPortAlarmStatYelCcYelCounters.setStatus(_A)
_MpAtmCCPortAlarmStatYelRaiCounters_Type=Counter32
_MpAtmCCPortAlarmStatYelRaiCounters_Object=MibTableColumn
mpAtmCCPortAlarmStatYelRaiCounters=_MpAtmCCPortAlarmStatYelRaiCounters_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,5,1,19),_MpAtmCCPortAlarmStatYelRaiCounters_Type())
mpAtmCCPortAlarmStatYelRaiCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPortAlarmStatYelRaiCounters.setStatus(_A)
_MpAtmCCPortAlarmStatYelPRaiCounters_Type=Counter32
_MpAtmCCPortAlarmStatYelPRaiCounters_Object=MibTableColumn
mpAtmCCPortAlarmStatYelPRaiCounters=_MpAtmCCPortAlarmStatYelPRaiCounters_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,5,1,20),_MpAtmCCPortAlarmStatYelPRaiCounters_Type())
mpAtmCCPortAlarmStatYelPRaiCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPortAlarmStatYelPRaiCounters.setStatus(_A)
_MpAtmCCPortAlarmStatYelInfo2Counters_Type=Counter32
_MpAtmCCPortAlarmStatYelInfo2Counters_Object=MibTableColumn
mpAtmCCPortAlarmStatYelInfo2Counters=_MpAtmCCPortAlarmStatYelInfo2Counters_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,5,1,21),_MpAtmCCPortAlarmStatYelInfo2Counters_Type())
mpAtmCCPortAlarmStatYelInfo2Counters.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPortAlarmStatYelInfo2Counters.setStatus(_A)
_MpAtmCCVpTunnellingStatisticsTable_Object=MibTable
mpAtmCCVpTunnellingStatisticsTable=_MpAtmCCVpTunnellingStatisticsTable_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,6))
if mibBuilder.loadTexts:mpAtmCCVpTunnellingStatisticsTable.setStatus(_A)
_MpAtmCCVpTunnellingStatisticsEntry_Object=MibTableRow
mpAtmCCVpTunnellingStatisticsEntry=_MpAtmCCVpTunnellingStatisticsEntry_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,6,1))
mpAtmCCVpTunnellingStatisticsEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:mpAtmCCVpTunnellingStatisticsEntry.setStatus(_A)
_MpAtmCCVpTunStatTmtCellsCounters_Type=Counter32
_MpAtmCCVpTunStatTmtCellsCounters_Object=MibTableColumn
mpAtmCCVpTunStatTmtCellsCounters=_MpAtmCCVpTunStatTmtCellsCounters_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,6,1,1),_MpAtmCCVpTunStatTmtCellsCounters_Type())
mpAtmCCVpTunStatTmtCellsCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCVpTunStatTmtCellsCounters.setStatus(_A)
_MpAtmCCVpTunStatRcvCellsCounters_Type=Counter32
_MpAtmCCVpTunStatRcvCellsCounters_Object=MibTableColumn
mpAtmCCVpTunStatRcvCellsCounters=_MpAtmCCVpTunStatRcvCellsCounters_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,6,1,2),_MpAtmCCVpTunStatRcvCellsCounters_Type())
mpAtmCCVpTunStatRcvCellsCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCVpTunStatRcvCellsCounters.setStatus(_A)
_MpAtmCCVccStatisticsRegTable_Object=MibTable
mpAtmCCVccStatisticsRegTable=_MpAtmCCVccStatisticsRegTable_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,7))
if mibBuilder.loadTexts:mpAtmCCVccStatisticsRegTable.setStatus(_A)
_MpAtmCCVccStatisticsRegEntry_Object=MibTableRow
mpAtmCCVccStatisticsRegEntry=_MpAtmCCVccStatisticsRegEntry_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,7,1))
mpAtmCCVccStatisticsRegEntry.setIndexNames((0,_I,_J),(0,_E,_A9),(0,_E,_AA))
if mibBuilder.loadTexts:mpAtmCCVccStatisticsRegEntry.setStatus(_A)
_MpAtmCCVccStatRegVpi_Type=Integer32
_MpAtmCCVccStatRegVpi_Object=MibTableColumn
mpAtmCCVccStatRegVpi=_MpAtmCCVccStatRegVpi_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,7,1,1),_MpAtmCCVccStatRegVpi_Type())
mpAtmCCVccStatRegVpi.setMaxAccess(_F)
if mibBuilder.loadTexts:mpAtmCCVccStatRegVpi.setStatus(_A)
_MpAtmCCVccStatRegVci_Type=Integer32
_MpAtmCCVccStatRegVci_Object=MibTableColumn
mpAtmCCVccStatRegVci=_MpAtmCCVccStatRegVci_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,7,1,2),_MpAtmCCVccStatRegVci_Type())
mpAtmCCVccStatRegVci.setMaxAccess(_F)
if mibBuilder.loadTexts:mpAtmCCVccStatRegVci.setStatus(_A)
_MpAtmCCVccStatRegInCellsCounters_Type=Counter32
_MpAtmCCVccStatRegInCellsCounters_Object=MibTableColumn
mpAtmCCVccStatRegInCellsCounters=_MpAtmCCVccStatRegInCellsCounters_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,7,1,3),_MpAtmCCVccStatRegInCellsCounters_Type())
mpAtmCCVccStatRegInCellsCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCVccStatRegInCellsCounters.setStatus(_A)
_MpAtmCCVccStatRegOutCellsCounters_Type=Counter32
_MpAtmCCVccStatRegOutCellsCounters_Object=MibTableColumn
mpAtmCCVccStatRegOutCellsCounters=_MpAtmCCVccStatRegOutCellsCounters_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,7,1,4),_MpAtmCCVccStatRegOutCellsCounters_Type())
mpAtmCCVccStatRegOutCellsCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCVccStatRegOutCellsCounters.setStatus(_A)
class _MpAtmCCVccStatRegStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('start',1),('stop',2)))
_MpAtmCCVccStatRegStatus_Type.__name__=_C
_MpAtmCCVccStatRegStatus_Object=MibTableColumn
mpAtmCCVccStatRegStatus=_MpAtmCCVccStatRegStatus_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,7,1,5),_MpAtmCCVccStatRegStatus_Type())
mpAtmCCVccStatRegStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCVccStatRegStatus.setStatus(_A)
_MpAtmCCVccStatRegErrInfo_Type=Integer32
_MpAtmCCVccStatRegErrInfo_Object=MibTableColumn
mpAtmCCVccStatRegErrInfo=_MpAtmCCVccStatRegErrInfo_Object((1,3,6,1,4,1,119,2,3,3,13,110,4,7,1,99),_MpAtmCCVccStatRegErrInfo_Type())
mpAtmCCVccStatRegErrInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCVccStatRegErrInfo.setStatus(_A)
_MpAtmCCResourceControl_ObjectIdentity=ObjectIdentity
mpAtmCCResourceControl=_MpAtmCCResourceControl_ObjectIdentity((1,3,6,1,4,1,119,2,3,3,13,110,5))
_MpAtmCCPortResourceInfomationTable_Object=MibTable
mpAtmCCPortResourceInfomationTable=_MpAtmCCPortResourceInfomationTable_Object((1,3,6,1,4,1,119,2,3,3,13,110,5,1))
if mibBuilder.loadTexts:mpAtmCCPortResourceInfomationTable.setStatus(_A)
_MpAtmCCPortResourceInfomationEntry_Object=MibTableRow
mpAtmCCPortResourceInfomationEntry=_MpAtmCCPortResourceInfomationEntry_Object((1,3,6,1,4,1,119,2,3,3,13,110,5,1,1))
mpAtmCCPortResourceInfomationEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:mpAtmCCPortResourceInfomationEntry.setStatus(_A)
_MpAtmCCPortResInfoPortSpeed_Type=Gauge32
_MpAtmCCPortResInfoPortSpeed_Object=MibTableColumn
mpAtmCCPortResInfoPortSpeed=_MpAtmCCPortResInfoPortSpeed_Object((1,3,6,1,4,1,119,2,3,3,13,110,5,1,1,1),_MpAtmCCPortResInfoPortSpeed_Type())
mpAtmCCPortResInfoPortSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPortResInfoPortSpeed.setStatus(_A)
_MpAtmCCPortResInfoMaxVpiBits_Type=Integer32
_MpAtmCCPortResInfoMaxVpiBits_Object=MibTableColumn
mpAtmCCPortResInfoMaxVpiBits=_MpAtmCCPortResInfoMaxVpiBits_Object((1,3,6,1,4,1,119,2,3,3,13,110,5,1,1,2),_MpAtmCCPortResInfoMaxVpiBits_Type())
mpAtmCCPortResInfoMaxVpiBits.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPortResInfoMaxVpiBits.setStatus(_A)
_MpAtmCCPortResInfoMaxVciBits_Type=Integer32
_MpAtmCCPortResInfoMaxVciBits_Object=MibTableColumn
mpAtmCCPortResInfoMaxVciBits=_MpAtmCCPortResInfoMaxVciBits_Object((1,3,6,1,4,1,119,2,3,3,13,110,5,1,1,3),_MpAtmCCPortResInfoMaxVciBits_Type())
mpAtmCCPortResInfoMaxVciBits.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPortResInfoMaxVciBits.setStatus(_A)
_MpAtmCCPortResInfoMaxVPC_Type=Integer32
_MpAtmCCPortResInfoMaxVPC_Object=MibTableColumn
mpAtmCCPortResInfoMaxVPC=_MpAtmCCPortResInfoMaxVPC_Object((1,3,6,1,4,1,119,2,3,3,13,110,5,1,1,4),_MpAtmCCPortResInfoMaxVPC_Type())
mpAtmCCPortResInfoMaxVPC.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPortResInfoMaxVPC.setStatus(_A)
_MpAtmCCPortResInfoMaxVCC_Type=Integer32
_MpAtmCCPortResInfoMaxVCC_Object=MibTableColumn
mpAtmCCPortResInfoMaxVCC=_MpAtmCCPortResInfoMaxVCC_Object((1,3,6,1,4,1,119,2,3,3,13,110,5,1,1,5),_MpAtmCCPortResInfoMaxVCC_Type())
mpAtmCCPortResInfoMaxVCC.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPortResInfoMaxVCC.setStatus(_A)
_MpAtmCCPortResInfoMaxSvpcVpi_Type=Integer32
_MpAtmCCPortResInfoMaxSvpcVpi_Object=MibTableColumn
mpAtmCCPortResInfoMaxSvpcVpi=_MpAtmCCPortResInfoMaxSvpcVpi_Object((1,3,6,1,4,1,119,2,3,3,13,110,5,1,1,6),_MpAtmCCPortResInfoMaxSvpcVpi_Type())
mpAtmCCPortResInfoMaxSvpcVpi.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPortResInfoMaxSvpcVpi.setStatus(_A)
_MpAtmCCPortResInfoMaxSvccVpi_Type=Integer32
_MpAtmCCPortResInfoMaxSvccVpi_Object=MibTableColumn
mpAtmCCPortResInfoMaxSvccVpi=_MpAtmCCPortResInfoMaxSvccVpi_Object((1,3,6,1,4,1,119,2,3,3,13,110,5,1,1,7),_MpAtmCCPortResInfoMaxSvccVpi_Type())
mpAtmCCPortResInfoMaxSvccVpi.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPortResInfoMaxSvccVpi.setStatus(_A)
_MpAtmCCPortResInfoMinSvccVci_Type=Integer32
_MpAtmCCPortResInfoMinSvccVci_Object=MibTableColumn
mpAtmCCPortResInfoMinSvccVci=_MpAtmCCPortResInfoMinSvccVci_Object((1,3,6,1,4,1,119,2,3,3,13,110,5,1,1,8),_MpAtmCCPortResInfoMinSvccVci_Type())
mpAtmCCPortResInfoMinSvccVci.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPortResInfoMinSvccVci.setStatus(_A)
class _MpAtmCCPortResInfoShaperKind_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('vp',2),('vc',3),('vpAndVc',4)))
_MpAtmCCPortResInfoShaperKind_Type.__name__=_C
_MpAtmCCPortResInfoShaperKind_Object=MibTableColumn
mpAtmCCPortResInfoShaperKind=_MpAtmCCPortResInfoShaperKind_Object((1,3,6,1,4,1,119,2,3,3,13,110,5,1,1,9),_MpAtmCCPortResInfoShaperKind_Type())
mpAtmCCPortResInfoShaperKind.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPortResInfoShaperKind.setStatus(_A)
class _MpAtmCCPortResInfoVpTunnellingConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('notConfigured',1),('configured',2)))
_MpAtmCCPortResInfoVpTunnellingConfig_Type.__name__=_C
_MpAtmCCPortResInfoVpTunnellingConfig_Object=MibTableColumn
mpAtmCCPortResInfoVpTunnellingConfig=_MpAtmCCPortResInfoVpTunnellingConfig_Object((1,3,6,1,4,1,119,2,3,3,13,110,5,1,1,10),_MpAtmCCPortResInfoVpTunnellingConfig_Type())
mpAtmCCPortResInfoVpTunnellingConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPortResInfoVpTunnellingConfig.setStatus(_A)
class _MpAtmCCPortResInfoSvccVciHuntWay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('low2high',1),('high2low',2)))
_MpAtmCCPortResInfoSvccVciHuntWay_Type.__name__=_C
_MpAtmCCPortResInfoSvccVciHuntWay_Object=MibTableColumn
mpAtmCCPortResInfoSvccVciHuntWay=_MpAtmCCPortResInfoSvccVciHuntWay_Object((1,3,6,1,4,1,119,2,3,3,13,110,5,1,1,11),_MpAtmCCPortResInfoSvccVciHuntWay_Type())
mpAtmCCPortResInfoSvccVciHuntWay.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPortResInfoSvccVciHuntWay.setStatus(_A)
_MpAtmCCPortResInfoVpiCounters_Type=Counter32
_MpAtmCCPortResInfoVpiCounters_Object=MibTableColumn
mpAtmCCPortResInfoVpiCounters=_MpAtmCCPortResInfoVpiCounters_Object((1,3,6,1,4,1,119,2,3,3,13,110,5,1,1,12),_MpAtmCCPortResInfoVpiCounters_Type())
mpAtmCCPortResInfoVpiCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPortResInfoVpiCounters.setStatus(_A)
_MpAtmCCPortResInfoVpcCounters_Type=Counter32
_MpAtmCCPortResInfoVpcCounters_Object=MibTableColumn
mpAtmCCPortResInfoVpcCounters=_MpAtmCCPortResInfoVpcCounters_Object((1,3,6,1,4,1,119,2,3,3,13,110,5,1,1,13),_MpAtmCCPortResInfoVpcCounters_Type())
mpAtmCCPortResInfoVpcCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPortResInfoVpcCounters.setStatus(_A)
_MpAtmCCPortResInfoVccCounters_Type=Counter32
_MpAtmCCPortResInfoVccCounters_Object=MibTableColumn
mpAtmCCPortResInfoVccCounters=_MpAtmCCPortResInfoVccCounters_Object((1,3,6,1,4,1,119,2,3,3,13,110,5,1,1,14),_MpAtmCCPortResInfoVccCounters_Type())
mpAtmCCPortResInfoVccCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPortResInfoVccCounters.setStatus(_A)
_MpAtmCCPortBandwidthInfomationTable_Object=MibTable
mpAtmCCPortBandwidthInfomationTable=_MpAtmCCPortBandwidthInfomationTable_Object((1,3,6,1,4,1,119,2,3,3,13,110,5,2))
if mibBuilder.loadTexts:mpAtmCCPortBandwidthInfomationTable.setStatus(_A)
_MpAtmCCPortBandwidthInfomationEntry_Object=MibTableRow
mpAtmCCPortBandwidthInfomationEntry=_MpAtmCCPortBandwidthInfomationEntry_Object((1,3,6,1,4,1,119,2,3,3,13,110,5,2,1))
mpAtmCCPortBandwidthInfomationEntry.setIndexNames((0,_I,_J),(0,_E,_AB))
if mibBuilder.loadTexts:mpAtmCCPortBandwidthInfomationEntry.setStatus(_A)
_MpAtmCCPortBwInfoVpi_Type=Integer32
_MpAtmCCPortBwInfoVpi_Object=MibTableColumn
mpAtmCCPortBwInfoVpi=_MpAtmCCPortBwInfoVpi_Object((1,3,6,1,4,1,119,2,3,3,13,110,5,2,1,1),_MpAtmCCPortBwInfoVpi_Type())
mpAtmCCPortBwInfoVpi.setMaxAccess(_F)
if mibBuilder.loadTexts:mpAtmCCPortBwInfoVpi.setStatus(_A)
_MpAtmCCPortBwInfoRawBandwidthBps_Type=Integer32
_MpAtmCCPortBwInfoRawBandwidthBps_Object=MibTableColumn
mpAtmCCPortBwInfoRawBandwidthBps=_MpAtmCCPortBwInfoRawBandwidthBps_Object((1,3,6,1,4,1,119,2,3,3,13,110,5,2,1,2),_MpAtmCCPortBwInfoRawBandwidthBps_Type())
mpAtmCCPortBwInfoRawBandwidthBps.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPortBwInfoRawBandwidthBps.setStatus(_A)
_MpAtmCCPortBwInfoRawBandwidthCps_Type=Integer32
_MpAtmCCPortBwInfoRawBandwidthCps_Object=MibTableColumn
mpAtmCCPortBwInfoRawBandwidthCps=_MpAtmCCPortBwInfoRawBandwidthCps_Object((1,3,6,1,4,1,119,2,3,3,13,110,5,2,1,3),_MpAtmCCPortBwInfoRawBandwidthCps_Type())
mpAtmCCPortBwInfoRawBandwidthCps.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPortBwInfoRawBandwidthCps.setStatus(_A)
_MpAtmCCPortBwInfoTmitUsedBwCps_Type=Integer32
_MpAtmCCPortBwInfoTmitUsedBwCps_Object=MibTableColumn
mpAtmCCPortBwInfoTmitUsedBwCps=_MpAtmCCPortBwInfoTmitUsedBwCps_Object((1,3,6,1,4,1,119,2,3,3,13,110,5,2,1,4),_MpAtmCCPortBwInfoTmitUsedBwCps_Type())
mpAtmCCPortBwInfoTmitUsedBwCps.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPortBwInfoTmitUsedBwCps.setStatus(_A)
_MpAtmCCPortBwInfoRcvUsedBwCps_Type=Integer32
_MpAtmCCPortBwInfoRcvUsedBwCps_Object=MibTableColumn
mpAtmCCPortBwInfoRcvUsedBwCps=_MpAtmCCPortBwInfoRcvUsedBwCps_Object((1,3,6,1,4,1,119,2,3,3,13,110,5,2,1,5),_MpAtmCCPortBwInfoRcvUsedBwCps_Type())
mpAtmCCPortBwInfoRcvUsedBwCps.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPortBwInfoRcvUsedBwCps.setStatus(_A)
_MpAtmCCPortBwInfoVciCounters_Type=Integer32
_MpAtmCCPortBwInfoVciCounters_Object=MibTableColumn
mpAtmCCPortBwInfoVciCounters=_MpAtmCCPortBwInfoVciCounters_Object((1,3,6,1,4,1,119,2,3,3,13,110,5,2,1,6),_MpAtmCCPortBwInfoVciCounters_Type())
mpAtmCCPortBwInfoVciCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPortBwInfoVciCounters.setStatus(_A)
_MpAtmCCBwInfoPortTable_Object=MibTable
mpAtmCCBwInfoPortTable=_MpAtmCCBwInfoPortTable_Object((1,3,6,1,4,1,119,2,3,3,13,110,5,3))
if mibBuilder.loadTexts:mpAtmCCBwInfoPortTable.setStatus(_A)
_MpAtmCCBwInfoPortEntry_Object=MibTableRow
mpAtmCCBwInfoPortEntry=_MpAtmCCBwInfoPortEntry_Object((1,3,6,1,4,1,119,2,3,3,13,110,5,3,1))
mpAtmCCBwInfoPortEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:mpAtmCCBwInfoPortEntry.setStatus(_A)
_MpAtmCCBwInfoPortRawBandwidthBps_Type=Integer32
_MpAtmCCBwInfoPortRawBandwidthBps_Object=MibTableColumn
mpAtmCCBwInfoPortRawBandwidthBps=_MpAtmCCBwInfoPortRawBandwidthBps_Object((1,3,6,1,4,1,119,2,3,3,13,110,5,3,1,1),_MpAtmCCBwInfoPortRawBandwidthBps_Type())
mpAtmCCBwInfoPortRawBandwidthBps.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCBwInfoPortRawBandwidthBps.setStatus(_A)
_MpAtmCCBwInfoPortRawBandwidthCps_Type=Integer32
_MpAtmCCBwInfoPortRawBandwidthCps_Object=MibTableColumn
mpAtmCCBwInfoPortRawBandwidthCps=_MpAtmCCBwInfoPortRawBandwidthCps_Object((1,3,6,1,4,1,119,2,3,3,13,110,5,3,1,2),_MpAtmCCBwInfoPortRawBandwidthCps_Type())
mpAtmCCBwInfoPortRawBandwidthCps.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCBwInfoPortRawBandwidthCps.setStatus(_A)
_MpAtmCCBwInfoPortTmitUsedBwCps_Type=Integer32
_MpAtmCCBwInfoPortTmitUsedBwCps_Object=MibTableColumn
mpAtmCCBwInfoPortTmitUsedBwCps=_MpAtmCCBwInfoPortTmitUsedBwCps_Object((1,3,6,1,4,1,119,2,3,3,13,110,5,3,1,3),_MpAtmCCBwInfoPortTmitUsedBwCps_Type())
mpAtmCCBwInfoPortTmitUsedBwCps.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCBwInfoPortTmitUsedBwCps.setStatus(_A)
_MpAtmCCBwInfoPortRcvUsedBwCps_Type=Integer32
_MpAtmCCBwInfoPortRcvUsedBwCps_Object=MibTableColumn
mpAtmCCBwInfoPortRcvUsedBwCps=_MpAtmCCBwInfoPortRcvUsedBwCps_Object((1,3,6,1,4,1,119,2,3,3,13,110,5,3,1,4),_MpAtmCCBwInfoPortRcvUsedBwCps_Type())
mpAtmCCBwInfoPortRcvUsedBwCps.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCBwInfoPortRcvUsedBwCps.setStatus(_A)
_MpAtmCCBwInfoPortTmitRemainBwCps_Type=Integer32
_MpAtmCCBwInfoPortTmitRemainBwCps_Object=MibTableColumn
mpAtmCCBwInfoPortTmitRemainBwCps=_MpAtmCCBwInfoPortTmitRemainBwCps_Object((1,3,6,1,4,1,119,2,3,3,13,110,5,3,1,5),_MpAtmCCBwInfoPortTmitRemainBwCps_Type())
mpAtmCCBwInfoPortTmitRemainBwCps.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCBwInfoPortTmitRemainBwCps.setStatus(_A)
_MpAtmCCBwInfoPortRcvRemainBwCps_Type=Integer32
_MpAtmCCBwInfoPortRcvRemainBwCps_Object=MibTableColumn
mpAtmCCBwInfoPortRcvRemainBwCps=_MpAtmCCBwInfoPortRcvRemainBwCps_Object((1,3,6,1,4,1,119,2,3,3,13,110,5,3,1,6),_MpAtmCCBwInfoPortRcvRemainBwCps_Type())
mpAtmCCBwInfoPortRcvRemainBwCps.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCBwInfoPortRcvRemainBwCps.setStatus(_A)
class _MpAtmCCBwInfoPortVpTunneling_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_MpAtmCCBwInfoPortVpTunneling_Type.__name__=_C
_MpAtmCCBwInfoPortVpTunneling_Object=MibTableColumn
mpAtmCCBwInfoPortVpTunneling=_MpAtmCCBwInfoPortVpTunneling_Object((1,3,6,1,4,1,119,2,3,3,13,110,5,3,1,7),_MpAtmCCBwInfoPortVpTunneling_Type())
mpAtmCCBwInfoPortVpTunneling.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCBwInfoPortVpTunneling.setStatus(_A)
_MpAtmCCProtocol_ObjectIdentity=ObjectIdentity
mpAtmCCProtocol=_MpAtmCCProtocol_ObjectIdentity((1,3,6,1,4,1,119,2,3,3,13,110,6))
_MpAtmCCSscopTable_Object=MibTable
mpAtmCCSscopTable=_MpAtmCCSscopTable_Object((1,3,6,1,4,1,119,2,3,3,13,110,6,1))
if mibBuilder.loadTexts:mpAtmCCSscopTable.setStatus(_A)
_MpAtmCCSscopEntry_Object=MibTableRow
mpAtmCCSscopEntry=_MpAtmCCSscopEntry_Object((1,3,6,1,4,1,119,2,3,3,13,110,6,1,1))
mpAtmCCSscopEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:mpAtmCCSscopEntry.setStatus(_A)
class _MpAtmCCSscopTimerPoll_Type(Integer32):defaultValue=750
_MpAtmCCSscopTimerPoll_Type.__name__=_C
_MpAtmCCSscopTimerPoll_Object=MibTableColumn
mpAtmCCSscopTimerPoll=_MpAtmCCSscopTimerPoll_Object((1,3,6,1,4,1,119,2,3,3,13,110,6,1,1,1),_MpAtmCCSscopTimerPoll_Type())
mpAtmCCSscopTimerPoll.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCSscopTimerPoll.setStatus(_A)
class _MpAtmCCSscopTimerNoResponce_Type(Integer32):defaultValue=7000
_MpAtmCCSscopTimerNoResponce_Type.__name__=_C
_MpAtmCCSscopTimerNoResponce_Object=MibTableColumn
mpAtmCCSscopTimerNoResponce=_MpAtmCCSscopTimerNoResponce_Object((1,3,6,1,4,1,119,2,3,3,13,110,6,1,1,2),_MpAtmCCSscopTimerNoResponce_Type())
mpAtmCCSscopTimerNoResponce.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCSscopTimerNoResponce.setStatus(_A)
class _MpAtmCCSscopTimerKeepAlive_Type(Integer32):defaultValue=2000
_MpAtmCCSscopTimerKeepAlive_Type.__name__=_C
_MpAtmCCSscopTimerKeepAlive_Object=MibTableColumn
mpAtmCCSscopTimerKeepAlive=_MpAtmCCSscopTimerKeepAlive_Object((1,3,6,1,4,1,119,2,3,3,13,110,6,1,1,3),_MpAtmCCSscopTimerKeepAlive_Type())
mpAtmCCSscopTimerKeepAlive.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCSscopTimerKeepAlive.setStatus(_A)
class _MpAtmCCSscopTimerIdle_Type(Integer32):defaultValue=15000
_MpAtmCCSscopTimerIdle_Type.__name__=_C
_MpAtmCCSscopTimerIdle_Object=MibTableColumn
mpAtmCCSscopTimerIdle=_MpAtmCCSscopTimerIdle_Object((1,3,6,1,4,1,119,2,3,3,13,110,6,1,1,4),_MpAtmCCSscopTimerIdle_Type())
mpAtmCCSscopTimerIdle.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCSscopTimerIdle.setStatus(_A)
class _MpAtmCCSscopTimerCc_Type(Integer32):defaultValue=1000
_MpAtmCCSscopTimerCc_Type.__name__=_C
_MpAtmCCSscopTimerCc_Object=MibTableColumn
mpAtmCCSscopTimerCc=_MpAtmCCSscopTimerCc_Object((1,3,6,1,4,1,119,2,3,3,13,110,6,1,1,5),_MpAtmCCSscopTimerCc_Type())
mpAtmCCSscopTimerCc.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCSscopTimerCc.setStatus(_A)
class _MpAtmCCSscopMaxCc_Type(Integer32):defaultValue=4
_MpAtmCCSscopMaxCc_Type.__name__=_C
_MpAtmCCSscopMaxCc_Object=MibTableColumn
mpAtmCCSscopMaxCc=_MpAtmCCSscopMaxCc_Object((1,3,6,1,4,1,119,2,3,3,13,110,6,1,1,6),_MpAtmCCSscopMaxCc_Type())
mpAtmCCSscopMaxCc.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCSscopMaxCc.setStatus(_A)
class _MpAtmCCSscopMaxPd_Type(Integer32):defaultValue=25
_MpAtmCCSscopMaxPd_Type.__name__=_C
_MpAtmCCSscopMaxPd_Object=MibTableColumn
mpAtmCCSscopMaxPd=_MpAtmCCSscopMaxPd_Object((1,3,6,1,4,1,119,2,3,3,13,110,6,1,1,7),_MpAtmCCSscopMaxPd_Type())
mpAtmCCSscopMaxPd.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCSscopMaxPd.setStatus(_A)
class _MpAtmCCSscopMaxStat_Type(Integer32):defaultValue=67
_MpAtmCCSscopMaxStat_Type.__name__=_C
_MpAtmCCSscopMaxStat_Object=MibTableColumn
mpAtmCCSscopMaxStat=_MpAtmCCSscopMaxStat_Object((1,3,6,1,4,1,119,2,3,3,13,110,6,1,1,8),_MpAtmCCSscopMaxStat_Type())
mpAtmCCSscopMaxStat.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCSscopMaxStat.setStatus(_A)
class _MpAtmCCSscopClearBuffs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_MpAtmCCSscopClearBuffs_Type.__name__=_C
_MpAtmCCSscopClearBuffs_Object=MibTableColumn
mpAtmCCSscopClearBuffs=_MpAtmCCSscopClearBuffs_Object((1,3,6,1,4,1,119,2,3,3,13,110,6,1,1,9),_MpAtmCCSscopClearBuffs_Type())
mpAtmCCSscopClearBuffs.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCSscopClearBuffs.setStatus(_A)
class _MpAtmCCSscopCredit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_MpAtmCCSscopCredit_Type.__name__=_C
_MpAtmCCSscopCredit_Object=MibTableColumn
mpAtmCCSscopCredit=_MpAtmCCSscopCredit_Object((1,3,6,1,4,1,119,2,3,3,13,110,6,1,1,10),_MpAtmCCSscopCredit_Type())
mpAtmCCSscopCredit.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCSscopCredit.setStatus(_A)
_MpAtmCCIlmiTable_Object=MibTable
mpAtmCCIlmiTable=_MpAtmCCIlmiTable_Object((1,3,6,1,4,1,119,2,3,3,13,110,6,2))
if mibBuilder.loadTexts:mpAtmCCIlmiTable.setStatus(_A)
_MpAtmCCIlmiEntry_Object=MibTableRow
mpAtmCCIlmiEntry=_MpAtmCCIlmiEntry_Object((1,3,6,1,4,1,119,2,3,3,13,110,6,2,1))
mpAtmCCIlmiEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:mpAtmCCIlmiEntry.setStatus(_A)
class _MpAtmCCIlmiConfigStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_MpAtmCCIlmiConfigStatus_Type.__name__=_C
_MpAtmCCIlmiConfigStatus_Object=MibTableColumn
mpAtmCCIlmiConfigStatus=_MpAtmCCIlmiConfigStatus_Object((1,3,6,1,4,1,119,2,3,3,13,110,6,2,1,1),_MpAtmCCIlmiConfigStatus_Type())
mpAtmCCIlmiConfigStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCIlmiConfigStatus.setStatus(_A)
class _MpAtmCClmiMaxTransmissions_Type(Integer32):defaultValue=4
_MpAtmCClmiMaxTransmissions_Type.__name__=_C
_MpAtmCClmiMaxTransmissions_Object=MibTableColumn
mpAtmCClmiMaxTransmissions=_MpAtmCClmiMaxTransmissions_Object((1,3,6,1,4,1,119,2,3,3,13,110,6,2,1,2),_MpAtmCClmiMaxTransmissions_Type())
mpAtmCClmiMaxTransmissions.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCClmiMaxTransmissions.setStatus(_A)
class _MpAtmCCIlmiRetransmitInterval_Type(Integer32):defaultValue=5
_MpAtmCCIlmiRetransmitInterval_Type.__name__=_C
_MpAtmCCIlmiRetransmitInterval_Object=MibTableColumn
mpAtmCCIlmiRetransmitInterval=_MpAtmCCIlmiRetransmitInterval_Object((1,3,6,1,4,1,119,2,3,3,13,110,6,2,1,3),_MpAtmCCIlmiRetransmitInterval_Type())
mpAtmCCIlmiRetransmitInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCIlmiRetransmitInterval.setStatus(_A)
_MpAtmCCSignallingTable_Object=MibTable
mpAtmCCSignallingTable=_MpAtmCCSignallingTable_Object((1,3,6,1,4,1,119,2,3,3,13,110,6,3))
if mibBuilder.loadTexts:mpAtmCCSignallingTable.setStatus(_A)
_MpAtmCCSignallingEntry_Object=MibTableRow
mpAtmCCSignallingEntry=_MpAtmCCSignallingEntry_Object((1,3,6,1,4,1,119,2,3,3,13,110,6,3,1))
mpAtmCCSignallingEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:mpAtmCCSignallingEntry.setStatus(_A)
class _MpAtmCCSignallingT301_Type(Integer32):defaultValue=180
_MpAtmCCSignallingT301_Type.__name__=_C
_MpAtmCCSignallingT301_Object=MibTableColumn
mpAtmCCSignallingT301=_MpAtmCCSignallingT301_Object((1,3,6,1,4,1,119,2,3,3,13,110,6,3,1,1),_MpAtmCCSignallingT301_Type())
mpAtmCCSignallingT301.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCSignallingT301.setStatus(_A)
class _MpAtmCCSignallingT303_Type(Integer32):defaultValue=4
_MpAtmCCSignallingT303_Type.__name__=_C
_MpAtmCCSignallingT303_Object=MibTableColumn
mpAtmCCSignallingT303=_MpAtmCCSignallingT303_Object((1,3,6,1,4,1,119,2,3,3,13,110,6,3,1,2),_MpAtmCCSignallingT303_Type())
mpAtmCCSignallingT303.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCSignallingT303.setStatus(_A)
class _MpAtmCCSignallingT308_Type(Integer32):defaultValue=30
_MpAtmCCSignallingT308_Type.__name__=_C
_MpAtmCCSignallingT308_Object=MibTableColumn
mpAtmCCSignallingT308=_MpAtmCCSignallingT308_Object((1,3,6,1,4,1,119,2,3,3,13,110,6,3,1,3),_MpAtmCCSignallingT308_Type())
mpAtmCCSignallingT308.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCSignallingT308.setStatus(_A)
class _MpAtmCCSignallingT309_Type(Integer32):defaultValue=10
_MpAtmCCSignallingT309_Type.__name__=_C
_MpAtmCCSignallingT309_Object=MibTableColumn
mpAtmCCSignallingT309=_MpAtmCCSignallingT309_Object((1,3,6,1,4,1,119,2,3,3,13,110,6,3,1,4),_MpAtmCCSignallingT309_Type())
mpAtmCCSignallingT309.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCSignallingT309.setStatus(_A)
class _MpAtmCCSignallingT310_Type(Integer32):defaultValue=30
_MpAtmCCSignallingT310_Type.__name__=_C
_MpAtmCCSignallingT310_Object=MibTableColumn
mpAtmCCSignallingT310=_MpAtmCCSignallingT310_Object((1,3,6,1,4,1,119,2,3,3,13,110,6,3,1,5),_MpAtmCCSignallingT310_Type())
mpAtmCCSignallingT310.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCSignallingT310.setStatus(_A)
class _MpAtmCCSignallingT313_Type(Integer32):defaultValue=4
_MpAtmCCSignallingT313_Type.__name__=_C
_MpAtmCCSignallingT313_Object=MibTableColumn
mpAtmCCSignallingT313=_MpAtmCCSignallingT313_Object((1,3,6,1,4,1,119,2,3,3,13,110,6,3,1,6),_MpAtmCCSignallingT313_Type())
mpAtmCCSignallingT313.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCSignallingT313.setStatus(_A)
class _MpAtmCCSignallingT316_Type(Integer32):defaultValue=120
_MpAtmCCSignallingT316_Type.__name__=_C
_MpAtmCCSignallingT316_Object=MibTableColumn
mpAtmCCSignallingT316=_MpAtmCCSignallingT316_Object((1,3,6,1,4,1,119,2,3,3,13,110,6,3,1,7),_MpAtmCCSignallingT316_Type())
mpAtmCCSignallingT316.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCSignallingT316.setStatus(_A)
class _MpAtmCCSignallingT317_Type(Integer32):defaultValue=180
_MpAtmCCSignallingT317_Type.__name__=_C
_MpAtmCCSignallingT317_Object=MibTableColumn
mpAtmCCSignallingT317=_MpAtmCCSignallingT317_Object((1,3,6,1,4,1,119,2,3,3,13,110,6,3,1,8),_MpAtmCCSignallingT317_Type())
mpAtmCCSignallingT317.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCSignallingT317.setStatus(_A)
class _MpAtmCCSignallingT322_Type(Integer32):defaultValue=4
_MpAtmCCSignallingT322_Type.__name__=_C
_MpAtmCCSignallingT322_Object=MibTableColumn
mpAtmCCSignallingT322=_MpAtmCCSignallingT322_Object((1,3,6,1,4,1,119,2,3,3,13,110,6,3,1,9),_MpAtmCCSignallingT322_Type())
mpAtmCCSignallingT322.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCSignallingT322.setStatus(_A)
class _MpAtmCCSignallingT331_Type(Integer32):defaultValue=60
_MpAtmCCSignallingT331_Type.__name__=_C
_MpAtmCCSignallingT331_Object=MibTableColumn
mpAtmCCSignallingT331=_MpAtmCCSignallingT331_Object((1,3,6,1,4,1,119,2,3,3,13,110,6,3,1,10),_MpAtmCCSignallingT331_Type())
mpAtmCCSignallingT331.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCSignallingT331.setStatus(_A)
class _MpAtmCCSignallingT397_Type(Integer32):defaultValue=180
_MpAtmCCSignallingT397_Type.__name__=_C
_MpAtmCCSignallingT397_Object=MibTableColumn
mpAtmCCSignallingT397=_MpAtmCCSignallingT397_Object((1,3,6,1,4,1,119,2,3,3,13,110,6,3,1,11),_MpAtmCCSignallingT397_Type())
mpAtmCCSignallingT397.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCSignallingT397.setStatus(_A)
class _MpAtmCCSignallingT398_Type(Integer32):defaultValue=4
_MpAtmCCSignallingT398_Type.__name__=_C
_MpAtmCCSignallingT398_Object=MibTableColumn
mpAtmCCSignallingT398=_MpAtmCCSignallingT398_Object((1,3,6,1,4,1,119,2,3,3,13,110,6,3,1,12),_MpAtmCCSignallingT398_Type())
mpAtmCCSignallingT398.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCSignallingT398.setStatus(_A)
class _MpAtmCCSignallingT399_Type(Integer32):defaultValue=34
_MpAtmCCSignallingT399_Type.__name__=_C
_MpAtmCCSignallingT399_Object=MibTableColumn
mpAtmCCSignallingT399=_MpAtmCCSignallingT399_Object((1,3,6,1,4,1,119,2,3,3,13,110,6,3,1,13),_MpAtmCCSignallingT399_Type())
mpAtmCCSignallingT399.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCSignallingT399.setStatus(_A)
_MpAtmCCProtocolTrapInfoTable_Object=MibTable
mpAtmCCProtocolTrapInfoTable=_MpAtmCCProtocolTrapInfoTable_Object((1,3,6,1,4,1,119,2,3,3,13,110,6,4))
if mibBuilder.loadTexts:mpAtmCCProtocolTrapInfoTable.setStatus(_A)
_MpAtmCCProtocolTrapInfoEntry_Object=MibTableRow
mpAtmCCProtocolTrapInfoEntry=_MpAtmCCProtocolTrapInfoEntry_Object((1,3,6,1,4,1,119,2,3,3,13,110,6,4,1))
mpAtmCCProtocolTrapInfoEntry.setIndexNames((0,_E,_AC))
if mibBuilder.loadTexts:mpAtmCCProtocolTrapInfoEntry.setStatus(_A)
_MpAtmCCProtocolTrapInfoIndex_Type=Integer32
_MpAtmCCProtocolTrapInfoIndex_Object=MibTableColumn
mpAtmCCProtocolTrapInfoIndex=_MpAtmCCProtocolTrapInfoIndex_Object((1,3,6,1,4,1,119,2,3,3,13,110,6,4,1,1),_MpAtmCCProtocolTrapInfoIndex_Type())
mpAtmCCProtocolTrapInfoIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCProtocolTrapInfoIndex.setStatus(_A)
_MpAtmCCProtocolTrapInfoCause_Type=Integer32
_MpAtmCCProtocolTrapInfoCause_Object=MibTableColumn
mpAtmCCProtocolTrapInfoCause=_MpAtmCCProtocolTrapInfoCause_Object((1,3,6,1,4,1,119,2,3,3,13,110,6,4,1,2),_MpAtmCCProtocolTrapInfoCause_Type())
mpAtmCCProtocolTrapInfoCause.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCProtocolTrapInfoCause.setStatus(_A)
_MpAtmCCPathTrace_ObjectIdentity=ObjectIdentity
mpAtmCCPathTrace=_MpAtmCCPathTrace_ObjectIdentity((1,3,6,1,4,1,119,2,3,3,13,110,7))
_MpAtmCCVccStatusTable_Object=MibTable
mpAtmCCVccStatusTable=_MpAtmCCVccStatusTable_Object((1,3,6,1,4,1,119,2,3,3,13,110,7,1))
if mibBuilder.loadTexts:mpAtmCCVccStatusTable.setStatus(_A)
_MpAtmCCVccStatusEntry_Object=MibTableRow
mpAtmCCVccStatusEntry=_MpAtmCCVccStatusEntry_Object((1,3,6,1,4,1,119,2,3,3,13,110,7,1,1))
mpAtmCCVccStatusEntry.setIndexNames((0,_E,_AD),(0,_E,_AE),(0,_E,_AF))
if mibBuilder.loadTexts:mpAtmCCVccStatusEntry.setStatus(_A)
_MpAtmCCVccStatusOrgPort_Type=Integer32
_MpAtmCCVccStatusOrgPort_Object=MibTableColumn
mpAtmCCVccStatusOrgPort=_MpAtmCCVccStatusOrgPort_Object((1,3,6,1,4,1,119,2,3,3,13,110,7,1,1,1),_MpAtmCCVccStatusOrgPort_Type())
mpAtmCCVccStatusOrgPort.setMaxAccess(_F)
if mibBuilder.loadTexts:mpAtmCCVccStatusOrgPort.setStatus(_A)
_MpAtmCCVccStatusOrgVpi_Type=Integer32
_MpAtmCCVccStatusOrgVpi_Object=MibTableColumn
mpAtmCCVccStatusOrgVpi=_MpAtmCCVccStatusOrgVpi_Object((1,3,6,1,4,1,119,2,3,3,13,110,7,1,1,2),_MpAtmCCVccStatusOrgVpi_Type())
mpAtmCCVccStatusOrgVpi.setMaxAccess(_F)
if mibBuilder.loadTexts:mpAtmCCVccStatusOrgVpi.setStatus(_A)
_MpAtmCCVccStatusOrgVci_Type=Integer32
_MpAtmCCVccStatusOrgVci_Object=MibTableColumn
mpAtmCCVccStatusOrgVci=_MpAtmCCVccStatusOrgVci_Object((1,3,6,1,4,1,119,2,3,3,13,110,7,1,1,3),_MpAtmCCVccStatusOrgVci_Type())
mpAtmCCVccStatusOrgVci.setMaxAccess(_F)
if mibBuilder.loadTexts:mpAtmCCVccStatusOrgVci.setStatus(_A)
_MpAtmCCVccStatusDestPort_Type=Integer32
_MpAtmCCVccStatusDestPort_Object=MibTableColumn
mpAtmCCVccStatusDestPort=_MpAtmCCVccStatusDestPort_Object((1,3,6,1,4,1,119,2,3,3,13,110,7,1,1,4),_MpAtmCCVccStatusDestPort_Type())
mpAtmCCVccStatusDestPort.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCVccStatusDestPort.setStatus(_A)
_MpAtmCCVccStatusDestVpi_Type=Integer32
_MpAtmCCVccStatusDestVpi_Object=MibTableColumn
mpAtmCCVccStatusDestVpi=_MpAtmCCVccStatusDestVpi_Object((1,3,6,1,4,1,119,2,3,3,13,110,7,1,1,5),_MpAtmCCVccStatusDestVpi_Type())
mpAtmCCVccStatusDestVpi.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCVccStatusDestVpi.setStatus(_A)
_MpAtmCCVccStatusDestVci_Type=Integer32
_MpAtmCCVccStatusDestVci_Object=MibTableColumn
mpAtmCCVccStatusDestVci=_MpAtmCCVccStatusDestVci_Object((1,3,6,1,4,1,119,2,3,3,13,110,7,1,1,6),_MpAtmCCVccStatusDestVci_Type())
mpAtmCCVccStatusDestVci.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCVccStatusDestVci.setStatus(_A)
class _MpAtmCCVccStatusPathKind_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('pvc',1),('softpvc',2),('insPvc',3),('pvp',4),('softpvp',5)))
_MpAtmCCVccStatusPathKind_Type.__name__=_C
_MpAtmCCVccStatusPathKind_Object=MibTableColumn
mpAtmCCVccStatusPathKind=_MpAtmCCVccStatusPathKind_Object((1,3,6,1,4,1,119,2,3,3,13,110,7,1,1,7),_MpAtmCCVccStatusPathKind_Type())
mpAtmCCVccStatusPathKind.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCVccStatusPathKind.setStatus(_A)
class _MpAtmCCVccStatusOrgCallKind_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_S,1),(_V,2),(_W,3),(_T,4)))
_MpAtmCCVccStatusOrgCallKind_Type.__name__=_C
_MpAtmCCVccStatusOrgCallKind_Object=MibTableColumn
mpAtmCCVccStatusOrgCallKind=_MpAtmCCVccStatusOrgCallKind_Object((1,3,6,1,4,1,119,2,3,3,13,110,7,1,1,8),_MpAtmCCVccStatusOrgCallKind_Type())
mpAtmCCVccStatusOrgCallKind.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCVccStatusOrgCallKind.setStatus(_A)
class _MpAtmCCVccStatusDestCallKind_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_S,1),(_V,2),(_W,3),(_T,4)))
_MpAtmCCVccStatusDestCallKind_Type.__name__=_C
_MpAtmCCVccStatusDestCallKind_Object=MibTableColumn
mpAtmCCVccStatusDestCallKind=_MpAtmCCVccStatusDestCallKind_Object((1,3,6,1,4,1,119,2,3,3,13,110,7,1,1,9),_MpAtmCCVccStatusDestCallKind_Type())
mpAtmCCVccStatusDestCallKind.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCVccStatusDestCallKind.setStatus(_A)
class _MpAtmCCVccStatusAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_MpAtmCCVccStatusAdminStatus_Type.__name__=_C
_MpAtmCCVccStatusAdminStatus_Object=MibTableColumn
mpAtmCCVccStatusAdminStatus=_MpAtmCCVccStatusAdminStatus_Object((1,3,6,1,4,1,119,2,3,3,13,110,7,1,1,10),_MpAtmCCVccStatusAdminStatus_Type())
mpAtmCCVccStatusAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCVccStatusAdminStatus.setStatus(_A)
class _MpAtmCCVccStatusOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_MpAtmCCVccStatusOperStatus_Type.__name__=_C
_MpAtmCCVccStatusOperStatus_Object=MibTableColumn
mpAtmCCVccStatusOperStatus=_MpAtmCCVccStatusOperStatus_Object((1,3,6,1,4,1,119,2,3,3,13,110,7,1,1,11),_MpAtmCCVccStatusOperStatus_Type())
mpAtmCCVccStatusOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCVccStatusOperStatus.setStatus(_A)
class _MpAtmCCVccStatusInsStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('trunkPort',1),('insPort',2)))
_MpAtmCCVccStatusInsStatus_Type.__name__=_C
_MpAtmCCVccStatusInsStatus_Object=MibTableColumn
mpAtmCCVccStatusInsStatus=_MpAtmCCVccStatusInsStatus_Object((1,3,6,1,4,1,119,2,3,3,13,110,7,1,1,12),_MpAtmCCVccStatusInsStatus_Type())
mpAtmCCVccStatusInsStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCVccStatusInsStatus.setStatus(_A)
class _MpAtmCCVccStatusOrgPortVpTunneling_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_MpAtmCCVccStatusOrgPortVpTunneling_Type.__name__=_C
_MpAtmCCVccStatusOrgPortVpTunneling_Object=MibTableColumn
mpAtmCCVccStatusOrgPortVpTunneling=_MpAtmCCVccStatusOrgPortVpTunneling_Object((1,3,6,1,4,1,119,2,3,3,13,110,7,1,1,13),_MpAtmCCVccStatusOrgPortVpTunneling_Type())
mpAtmCCVccStatusOrgPortVpTunneling.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCVccStatusOrgPortVpTunneling.setStatus(_A)
class _MpAtmCCVccStatusDestPortVpTunneling_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_MpAtmCCVccStatusDestPortVpTunneling_Type.__name__=_C
_MpAtmCCVccStatusDestPortVpTunneling_Object=MibTableColumn
mpAtmCCVccStatusDestPortVpTunneling=_MpAtmCCVccStatusDestPortVpTunneling_Object((1,3,6,1,4,1,119,2,3,3,13,110,7,1,1,14),_MpAtmCCVccStatusDestPortVpTunneling_Type())
mpAtmCCVccStatusDestPortVpTunneling.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCVccStatusDestPortVpTunneling.setStatus(_A)
class _MpAtmCCVccStatusConnCastType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('p2p',1),('p2mpRoot',2),('p2mpLeaf',3)))
_MpAtmCCVccStatusConnCastType_Type.__name__=_C
_MpAtmCCVccStatusConnCastType_Object=MibTableColumn
mpAtmCCVccStatusConnCastType=_MpAtmCCVccStatusConnCastType_Object((1,3,6,1,4,1,119,2,3,3,13,110,7,1,1,15),_MpAtmCCVccStatusConnCastType_Type())
mpAtmCCVccStatusConnCastType.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCVccStatusConnCastType.setStatus(_A)
_MpAtmCCPvcTraceControlTable_Object=MibTable
mpAtmCCPvcTraceControlTable=_MpAtmCCPvcTraceControlTable_Object((1,3,6,1,4,1,119,2,3,3,13,110,7,2))
if mibBuilder.loadTexts:mpAtmCCPvcTraceControlTable.setStatus(_A)
_MpAtmCCPvcTraceCtlEntry_Object=MibTableRow
mpAtmCCPvcTraceCtlEntry=_MpAtmCCPvcTraceCtlEntry_Object((1,3,6,1,4,1,119,2,3,3,13,110,7,2,1))
mpAtmCCPvcTraceCtlEntry.setIndexNames((0,_E,_X))
if mibBuilder.loadTexts:mpAtmCCPvcTraceCtlEntry.setStatus(_A)
class _MpAtmCCPvcTraceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_MpAtmCCPvcTraceIndex_Type.__name__=_C
_MpAtmCCPvcTraceIndex_Object=MibTableColumn
mpAtmCCPvcTraceIndex=_MpAtmCCPvcTraceIndex_Object((1,3,6,1,4,1,119,2,3,3,13,110,7,2,1,1),_MpAtmCCPvcTraceIndex_Type())
mpAtmCCPvcTraceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPvcTraceIndex.setStatus(_A)
class _MpAtmCCPvcTraceCtlPathKind_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('vcc',1),('vpc',2)))
_MpAtmCCPvcTraceCtlPathKind_Type.__name__=_C
_MpAtmCCPvcTraceCtlPathKind_Object=MibTableColumn
mpAtmCCPvcTraceCtlPathKind=_MpAtmCCPvcTraceCtlPathKind_Object((1,3,6,1,4,1,119,2,3,3,13,110,7,2,1,2),_MpAtmCCPvcTraceCtlPathKind_Type())
mpAtmCCPvcTraceCtlPathKind.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCPvcTraceCtlPathKind.setStatus(_A)
_MpAtmCCPvcTraceCtlIfIndex_Type=Integer32
_MpAtmCCPvcTraceCtlIfIndex_Object=MibTableColumn
mpAtmCCPvcTraceCtlIfIndex=_MpAtmCCPvcTraceCtlIfIndex_Object((1,3,6,1,4,1,119,2,3,3,13,110,7,2,1,3),_MpAtmCCPvcTraceCtlIfIndex_Type())
mpAtmCCPvcTraceCtlIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCPvcTraceCtlIfIndex.setStatus(_A)
_MpAtmCCPvcTraceCtlVpi_Type=Integer32
_MpAtmCCPvcTraceCtlVpi_Object=MibTableColumn
mpAtmCCPvcTraceCtlVpi=_MpAtmCCPvcTraceCtlVpi_Object((1,3,6,1,4,1,119,2,3,3,13,110,7,2,1,4),_MpAtmCCPvcTraceCtlVpi_Type())
mpAtmCCPvcTraceCtlVpi.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCPvcTraceCtlVpi.setStatus(_A)
_MpAtmCCPvcTraceCtlVci_Type=Integer32
_MpAtmCCPvcTraceCtlVci_Object=MibTableColumn
mpAtmCCPvcTraceCtlVci=_MpAtmCCPvcTraceCtlVci_Object((1,3,6,1,4,1,119,2,3,3,13,110,7,2,1,5),_MpAtmCCPvcTraceCtlVci_Type())
mpAtmCCPvcTraceCtlVci.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCPvcTraceCtlVci.setStatus(_A)
class _MpAtmCCPvcTraceCtlStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('idle',1),('start',2),('collecting',3),('done',4),(_N,5),(_L,6)))
_MpAtmCCPvcTraceCtlStatus_Type.__name__=_C
_MpAtmCCPvcTraceCtlStatus_Object=MibTableColumn
mpAtmCCPvcTraceCtlStatus=_MpAtmCCPvcTraceCtlStatus_Object((1,3,6,1,4,1,119,2,3,3,13,110,7,2,1,6),_MpAtmCCPvcTraceCtlStatus_Type())
mpAtmCCPvcTraceCtlStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCPvcTraceCtlStatus.setStatus(_A)
_MpAtmCCPvcTraceInfoTable_Object=MibTable
mpAtmCCPvcTraceInfoTable=_MpAtmCCPvcTraceInfoTable_Object((1,3,6,1,4,1,119,2,3,3,13,110,7,3))
if mibBuilder.loadTexts:mpAtmCCPvcTraceInfoTable.setStatus(_A)
_MpAtmCCPvcTraceInfoEntry_Object=MibTableRow
mpAtmCCPvcTraceInfoEntry=_MpAtmCCPvcTraceInfoEntry_Object((1,3,6,1,4,1,119,2,3,3,13,110,7,3,1))
mpAtmCCPvcTraceInfoEntry.setIndexNames((0,_E,_X),(0,_E,_AG))
if mibBuilder.loadTexts:mpAtmCCPvcTraceInfoEntry.setStatus(_A)
class _MpAtmCCPvcTraceEntryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_MpAtmCCPvcTraceEntryIndex_Type.__name__=_C
_MpAtmCCPvcTraceEntryIndex_Object=MibTableColumn
mpAtmCCPvcTraceEntryIndex=_MpAtmCCPvcTraceEntryIndex_Object((1,3,6,1,4,1,119,2,3,3,13,110,7,3,1,1),_MpAtmCCPvcTraceEntryIndex_Type())
mpAtmCCPvcTraceEntryIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:mpAtmCCPvcTraceEntryIndex.setStatus(_A)
class _MpAtmCCPvcTraceInfoSysName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MpAtmCCPvcTraceInfoSysName_Type.__name__=_U
_MpAtmCCPvcTraceInfoSysName_Object=MibTableColumn
mpAtmCCPvcTraceInfoSysName=_MpAtmCCPvcTraceInfoSysName_Object((1,3,6,1,4,1,119,2,3,3,13,110,7,3,1,2),_MpAtmCCPvcTraceInfoSysName_Type())
mpAtmCCPvcTraceInfoSysName.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPvcTraceInfoSysName.setStatus(_A)
_MpAtmCCPvcTraceInfoIfIndex_Type=Integer32
_MpAtmCCPvcTraceInfoIfIndex_Object=MibTableColumn
mpAtmCCPvcTraceInfoIfIndex=_MpAtmCCPvcTraceInfoIfIndex_Object((1,3,6,1,4,1,119,2,3,3,13,110,7,3,1,3),_MpAtmCCPvcTraceInfoIfIndex_Type())
mpAtmCCPvcTraceInfoIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPvcTraceInfoIfIndex.setStatus(_A)
_MpAtmCCPvcTraceInfoVpi_Type=Integer32
_MpAtmCCPvcTraceInfoVpi_Object=MibTableColumn
mpAtmCCPvcTraceInfoVpi=_MpAtmCCPvcTraceInfoVpi_Object((1,3,6,1,4,1,119,2,3,3,13,110,7,3,1,4),_MpAtmCCPvcTraceInfoVpi_Type())
mpAtmCCPvcTraceInfoVpi.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPvcTraceInfoVpi.setStatus(_A)
_MpAtmCCPvcTraceInfoVci_Type=Integer32
_MpAtmCCPvcTraceInfoVci_Object=MibTableColumn
mpAtmCCPvcTraceInfoVci=_MpAtmCCPvcTraceInfoVci_Object((1,3,6,1,4,1,119,2,3,3,13,110,7,3,1,5),_MpAtmCCPvcTraceInfoVci_Type())
mpAtmCCPvcTraceInfoVci.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPvcTraceInfoVci.setStatus(_A)
class _MpAtmCCPvcTraceInfoPathKind_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('pvc',1),('softpvc',2),('inspvc',3),('pvp',4),('softpvp',5)))
_MpAtmCCPvcTraceInfoPathKind_Type.__name__=_C
_MpAtmCCPvcTraceInfoPathKind_Object=MibTableColumn
mpAtmCCPvcTraceInfoPathKind=_MpAtmCCPvcTraceInfoPathKind_Object((1,3,6,1,4,1,119,2,3,3,13,110,7,3,1,6),_MpAtmCCPvcTraceInfoPathKind_Type())
mpAtmCCPvcTraceInfoPathKind.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPvcTraceInfoPathKind.setStatus(_A)
class _MpAtmCCPvcTraceInfoCallKind_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_S,1),(_V,2),(_W,3),(_T,4)))
_MpAtmCCPvcTraceInfoCallKind_Type.__name__=_C
_MpAtmCCPvcTraceInfoCallKind_Object=MibTableColumn
mpAtmCCPvcTraceInfoCallKind=_MpAtmCCPvcTraceInfoCallKind_Object((1,3,6,1,4,1,119,2,3,3,13,110,7,3,1,7),_MpAtmCCPvcTraceInfoCallKind_Type())
mpAtmCCPvcTraceInfoCallKind.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPvcTraceInfoCallKind.setStatus(_A)
class _MpAtmCCPvcTraceInfoLastSegment_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('notlast',1),('last',2)))
_MpAtmCCPvcTraceInfoLastSegment_Type.__name__=_C
_MpAtmCCPvcTraceInfoLastSegment_Object=MibTableColumn
mpAtmCCPvcTraceInfoLastSegment=_MpAtmCCPvcTraceInfoLastSegment_Object((1,3,6,1,4,1,119,2,3,3,13,110,7,3,1,8),_MpAtmCCPvcTraceInfoLastSegment_Type())
mpAtmCCPvcTraceInfoLastSegment.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPvcTraceInfoLastSegment.setStatus(_A)
_MpAtmCCMuxMib_ObjectIdentity=ObjectIdentity
mpAtmCCMuxMib=_MpAtmCCMuxMib_ObjectIdentity((1,3,6,1,4,1,119,2,3,3,13,110,8))
_MpAtmCCMuxStatistics_ObjectIdentity=ObjectIdentity
mpAtmCCMuxStatistics=_MpAtmCCMuxStatistics_ObjectIdentity((1,3,6,1,4,1,119,2,3,3,13,110,8,1))
_MpAtmCCMuxStatReceiveCellsCounters_Type=Counter32
_MpAtmCCMuxStatReceiveCellsCounters_Object=MibScalar
mpAtmCCMuxStatReceiveCellsCounters=_MpAtmCCMuxStatReceiveCellsCounters_Object((1,3,6,1,4,1,119,2,3,3,13,110,8,1,1),_MpAtmCCMuxStatReceiveCellsCounters_Type())
mpAtmCCMuxStatReceiveCellsCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCMuxStatReceiveCellsCounters.setStatus(_A)
_MpAtmCCMuxStatReceiveCellsCntOvfCounters_Type=Counter32
_MpAtmCCMuxStatReceiveCellsCntOvfCounters_Object=MibScalar
mpAtmCCMuxStatReceiveCellsCntOvfCounters=_MpAtmCCMuxStatReceiveCellsCntOvfCounters_Object((1,3,6,1,4,1,119,2,3,3,13,110,8,1,2),_MpAtmCCMuxStatReceiveCellsCntOvfCounters_Type())
mpAtmCCMuxStatReceiveCellsCntOvfCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCMuxStatReceiveCellsCntOvfCounters.setStatus(_A)
_MpAtmCCMuxStatDiscardCellsBufOvfCounters_Type=Counter32
_MpAtmCCMuxStatDiscardCellsBufOvfCounters_Object=MibScalar
mpAtmCCMuxStatDiscardCellsBufOvfCounters=_MpAtmCCMuxStatDiscardCellsBufOvfCounters_Object((1,3,6,1,4,1,119,2,3,3,13,110,8,1,3),_MpAtmCCMuxStatDiscardCellsBufOvfCounters_Type())
mpAtmCCMuxStatDiscardCellsBufOvfCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCMuxStatDiscardCellsBufOvfCounters.setStatus(_A)
_MpAtmCCMuxStatDiscardCellsBufOvfCntOvfCounters_Type=Counter32
_MpAtmCCMuxStatDiscardCellsBufOvfCntOvfCounters_Object=MibScalar
mpAtmCCMuxStatDiscardCellsBufOvfCntOvfCounters=_MpAtmCCMuxStatDiscardCellsBufOvfCntOvfCounters_Object((1,3,6,1,4,1,119,2,3,3,13,110,8,1,4),_MpAtmCCMuxStatDiscardCellsBufOvfCntOvfCounters_Type())
mpAtmCCMuxStatDiscardCellsBufOvfCntOvfCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCMuxStatDiscardCellsBufOvfCntOvfCounters.setStatus(_A)
_MpAtmCCMuxStatDiscardCellsHTErrCounters_Type=Counter32
_MpAtmCCMuxStatDiscardCellsHTErrCounters_Object=MibScalar
mpAtmCCMuxStatDiscardCellsHTErrCounters=_MpAtmCCMuxStatDiscardCellsHTErrCounters_Object((1,3,6,1,4,1,119,2,3,3,13,110,8,1,5),_MpAtmCCMuxStatDiscardCellsHTErrCounters_Type())
mpAtmCCMuxStatDiscardCellsHTErrCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCMuxStatDiscardCellsHTErrCounters.setStatus(_A)
_MpAtmCCMuxStatDiscardCellsHTErrCntOvfCounters_Type=Counter32
_MpAtmCCMuxStatDiscardCellsHTErrCntOvfCounters_Object=MibScalar
mpAtmCCMuxStatDiscardCellsHTErrCntOvfCounters=_MpAtmCCMuxStatDiscardCellsHTErrCntOvfCounters_Object((1,3,6,1,4,1,119,2,3,3,13,110,8,1,6),_MpAtmCCMuxStatDiscardCellsHTErrCntOvfCounters_Type())
mpAtmCCMuxStatDiscardCellsHTErrCntOvfCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCMuxStatDiscardCellsHTErrCntOvfCounters.setStatus(_A)
_MpAtmCCMuxStatDiscardCellsThresholdOvfCounters_Type=Counter32
_MpAtmCCMuxStatDiscardCellsThresholdOvfCounters_Object=MibScalar
mpAtmCCMuxStatDiscardCellsThresholdOvfCounters=_MpAtmCCMuxStatDiscardCellsThresholdOvfCounters_Object((1,3,6,1,4,1,119,2,3,3,13,110,8,1,7),_MpAtmCCMuxStatDiscardCellsThresholdOvfCounters_Type())
mpAtmCCMuxStatDiscardCellsThresholdOvfCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCMuxStatDiscardCellsThresholdOvfCounters.setStatus(_A)
_MpAtmCCMuxStatDiscardCellsThresholdOvfCntOvfCounters_Type=Counter32
_MpAtmCCMuxStatDiscardCellsThresholdOvfCntOvfCounters_Object=MibScalar
mpAtmCCMuxStatDiscardCellsThresholdOvfCntOvfCounters=_MpAtmCCMuxStatDiscardCellsThresholdOvfCntOvfCounters_Object((1,3,6,1,4,1,119,2,3,3,13,110,8,1,8),_MpAtmCCMuxStatDiscardCellsThresholdOvfCntOvfCounters_Type())
mpAtmCCMuxStatDiscardCellsThresholdOvfCntOvfCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCMuxStatDiscardCellsThresholdOvfCntOvfCounters.setStatus(_A)
_MpAtmCCVpTunneling_ObjectIdentity=ObjectIdentity
mpAtmCCVpTunneling=_MpAtmCCVpTunneling_ObjectIdentity((1,3,6,1,4,1,119,2,3,3,13,110,9))
_MpAtmCCVpTunnelingTable_Object=MibTable
mpAtmCCVpTunnelingTable=_MpAtmCCVpTunnelingTable_Object((1,3,6,1,4,1,119,2,3,3,13,110,9,1))
if mibBuilder.loadTexts:mpAtmCCVpTunnelingTable.setStatus(_A)
_MpAtmCCVpTunnelingEntry_Object=MibTableRow
mpAtmCCVpTunnelingEntry=_MpAtmCCVpTunnelingEntry_Object((1,3,6,1,4,1,119,2,3,3,13,110,9,1,1))
mpAtmCCVpTunnelingEntry.setIndexNames((0,_I,_J),(0,_E,_AH))
if mibBuilder.loadTexts:mpAtmCCVpTunnelingEntry.setStatus(_A)
_MpAtmCCVpTunnelingVpi_Type=Integer32
_MpAtmCCVpTunnelingVpi_Object=MibTableColumn
mpAtmCCVpTunnelingVpi=_MpAtmCCVpTunnelingVpi_Object((1,3,6,1,4,1,119,2,3,3,13,110,9,1,1,1),_MpAtmCCVpTunnelingVpi_Type())
mpAtmCCVpTunnelingVpi.setMaxAccess(_F)
if mibBuilder.loadTexts:mpAtmCCVpTunnelingVpi.setStatus(_A)
class _MpAtmCCVpTunnelingAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_MpAtmCCVpTunnelingAdminStatus_Type.__name__=_C
_MpAtmCCVpTunnelingAdminStatus_Object=MibTableColumn
mpAtmCCVpTunnelingAdminStatus=_MpAtmCCVpTunnelingAdminStatus_Object((1,3,6,1,4,1,119,2,3,3,13,110,9,1,1,2),_MpAtmCCVpTunnelingAdminStatus_Type())
mpAtmCCVpTunnelingAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCVpTunnelingAdminStatus.setStatus(_A)
class _MpAtmCCVpTunnelingOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_MpAtmCCVpTunnelingOperStatus_Type.__name__=_C
_MpAtmCCVpTunnelingOperStatus_Object=MibTableColumn
mpAtmCCVpTunnelingOperStatus=_MpAtmCCVpTunnelingOperStatus_Object((1,3,6,1,4,1,119,2,3,3,13,110,9,1,1,3),_MpAtmCCVpTunnelingOperStatus_Type())
mpAtmCCVpTunnelingOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCVpTunnelingOperStatus.setStatus(_A)
_MpAtmCCVpTunnelingSpeed_Type=Integer32
_MpAtmCCVpTunnelingSpeed_Object=MibTableColumn
mpAtmCCVpTunnelingSpeed=_MpAtmCCVpTunnelingSpeed_Object((1,3,6,1,4,1,119,2,3,3,13,110,9,1,1,4),_MpAtmCCVpTunnelingSpeed_Type())
mpAtmCCVpTunnelingSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCVpTunnelingSpeed.setStatus(_A)
_MpAtmCCVpTunnelingNeighborInfo_Type=Integer32
_MpAtmCCVpTunnelingNeighborInfo_Object=MibTableColumn
mpAtmCCVpTunnelingNeighborInfo=_MpAtmCCVpTunnelingNeighborInfo_Object((1,3,6,1,4,1,119,2,3,3,13,110,9,1,1,5),_MpAtmCCVpTunnelingNeighborInfo_Type())
mpAtmCCVpTunnelingNeighborInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCVpTunnelingNeighborInfo.setStatus(_A)
_MpAtmCCVpTunnelingPnniVer_Type=Integer32
_MpAtmCCVpTunnelingPnniVer_Object=MibTableColumn
mpAtmCCVpTunnelingPnniVer=_MpAtmCCVpTunnelingPnniVer_Object((1,3,6,1,4,1,119,2,3,3,13,110,9,1,1,6),_MpAtmCCVpTunnelingPnniVer_Type())
mpAtmCCVpTunnelingPnniVer.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCVpTunnelingPnniVer.setStatus(_A)
class _MpAtmCCVpTunnelingContinuityCheck_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('off',1),('on',2)))
_MpAtmCCVpTunnelingContinuityCheck_Type.__name__=_C
_MpAtmCCVpTunnelingContinuityCheck_Object=MibTableColumn
mpAtmCCVpTunnelingContinuityCheck=_MpAtmCCVpTunnelingContinuityCheck_Object((1,3,6,1,4,1,119,2,3,3,13,110,9,1,1,7),_MpAtmCCVpTunnelingContinuityCheck_Type())
mpAtmCCVpTunnelingContinuityCheck.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCVpTunnelingContinuityCheck.setStatus(_A)
class _MpAtmCCVpTunnelingTrapState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('off',1),('on',2)))
_MpAtmCCVpTunnelingTrapState_Type.__name__=_C
_MpAtmCCVpTunnelingTrapState_Object=MibTableColumn
mpAtmCCVpTunnelingTrapState=_MpAtmCCVpTunnelingTrapState_Object((1,3,6,1,4,1,119,2,3,3,13,110,9,1,1,8),_MpAtmCCVpTunnelingTrapState_Type())
mpAtmCCVpTunnelingTrapState.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCVpTunnelingTrapState.setStatus(_A)
class _MpAtmCCVpTunnelingSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('critical',1),('major',2),('minor',3),('warning',4),('informational',5)))
_MpAtmCCVpTunnelingSeverity_Type.__name__=_C
_MpAtmCCVpTunnelingSeverity_Object=MibTableColumn
mpAtmCCVpTunnelingSeverity=_MpAtmCCVpTunnelingSeverity_Object((1,3,6,1,4,1,119,2,3,3,13,110,9,1,1,9),_MpAtmCCVpTunnelingSeverity_Type())
mpAtmCCVpTunnelingSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCVpTunnelingSeverity.setStatus(_A)
class _MpAtmCCVpTunnelingCfgStatus_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_M,1),(_N,2),(_K,3),(_L,4)))
_MpAtmCCVpTunnelingCfgStatus_Type.__name__=_C
_MpAtmCCVpTunnelingCfgStatus_Object=MibTableColumn
mpAtmCCVpTunnelingCfgStatus=_MpAtmCCVpTunnelingCfgStatus_Object((1,3,6,1,4,1,119,2,3,3,13,110,9,1,1,98),_MpAtmCCVpTunnelingCfgStatus_Type())
mpAtmCCVpTunnelingCfgStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCVpTunnelingCfgStatus.setStatus(_A)
_MpAtmCCVpTunnelingErrInfo_Type=Integer32
_MpAtmCCVpTunnelingErrInfo_Object=MibTableColumn
mpAtmCCVpTunnelingErrInfo=_MpAtmCCVpTunnelingErrInfo_Object((1,3,6,1,4,1,119,2,3,3,13,110,9,1,1,99),_MpAtmCCVpTunnelingErrInfo_Type())
mpAtmCCVpTunnelingErrInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCVpTunnelingErrInfo.setStatus(_A)
_MpAtmCCPathTest_ObjectIdentity=ObjectIdentity
mpAtmCCPathTest=_MpAtmCCPathTest_ObjectIdentity((1,3,6,1,4,1,119,2,3,3,13,110,10))
_MpAtmCCPathTestTable_Object=MibTable
mpAtmCCPathTestTable=_MpAtmCCPathTestTable_Object((1,3,6,1,4,1,119,2,3,3,13,110,10,1))
if mibBuilder.loadTexts:mpAtmCCPathTestTable.setStatus(_A)
_MpAtmCCPathTestEntry_Object=MibTableRow
mpAtmCCPathTestEntry=_MpAtmCCPathTestEntry_Object((1,3,6,1,4,1,119,2,3,3,13,110,10,1,1))
mpAtmCCPathTestEntry.setIndexNames((0,_I,_J),(0,_E,_AI),(0,_E,_AJ))
if mibBuilder.loadTexts:mpAtmCCPathTestEntry.setStatus(_A)
_MpAtmCCPathTestVpi_Type=Integer32
_MpAtmCCPathTestVpi_Object=MibTableColumn
mpAtmCCPathTestVpi=_MpAtmCCPathTestVpi_Object((1,3,6,1,4,1,119,2,3,3,13,110,10,1,1,1),_MpAtmCCPathTestVpi_Type())
mpAtmCCPathTestVpi.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPathTestVpi.setStatus(_A)
_MpAtmCCPathTestVci_Type=Integer32
_MpAtmCCPathTestVci_Object=MibTableColumn
mpAtmCCPathTestVci=_MpAtmCCPathTestVci_Object((1,3,6,1,4,1,119,2,3,3,13,110,10,1,1,2),_MpAtmCCPathTestVci_Type())
mpAtmCCPathTestVci.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPathTestVci.setStatus(_A)
class _MpAtmCCPathTestStatus_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('testReq',1),('sendStart',2),('sendStop',3),('loopSet',4),('loopRelease',5),(_K,6),(_L,7)))
_MpAtmCCPathTestStatus_Type.__name__=_C
_MpAtmCCPathTestStatus_Object=MibTableColumn
mpAtmCCPathTestStatus=_MpAtmCCPathTestStatus_Object((1,3,6,1,4,1,119,2,3,3,13,110,10,1,1,3),_MpAtmCCPathTestStatus_Type())
mpAtmCCPathTestStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCPathTestStatus.setStatus(_A)
class _MpAtmCCPathTestSendDirection_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('port',1),('mux',2)))
_MpAtmCCPathTestSendDirection_Type.__name__=_C
_MpAtmCCPathTestSendDirection_Object=MibTableColumn
mpAtmCCPathTestSendDirection=_MpAtmCCPathTestSendDirection_Object((1,3,6,1,4,1,119,2,3,3,13,110,10,1,1,4),_MpAtmCCPathTestSendDirection_Type())
mpAtmCCPathTestSendDirection.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCPathTestSendDirection.setStatus(_A)
class _MpAtmCCPathTestSendTime_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,68400))
_MpAtmCCPathTestSendTime_Type.__name__=_C
_MpAtmCCPathTestSendTime_Object=MibTableColumn
mpAtmCCPathTestSendTime=_MpAtmCCPathTestSendTime_Object((1,3,6,1,4,1,119,2,3,3,13,110,10,1,1,5),_MpAtmCCPathTestSendTime_Type())
mpAtmCCPathTestSendTime.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCPathTestSendTime.setStatus(_A)
_MpAtmCCPathTestSendCellsCounters_Type=Counter32
_MpAtmCCPathTestSendCellsCounters_Object=MibTableColumn
mpAtmCCPathTestSendCellsCounters=_MpAtmCCPathTestSendCellsCounters_Object((1,3,6,1,4,1,119,2,3,3,13,110,10,1,1,6),_MpAtmCCPathTestSendCellsCounters_Type())
mpAtmCCPathTestSendCellsCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPathTestSendCellsCounters.setStatus(_A)
_MpAtmCCPathTestRcvCellsCounters_Type=Counter32
_MpAtmCCPathTestRcvCellsCounters_Object=MibTableColumn
mpAtmCCPathTestRcvCellsCounters=_MpAtmCCPathTestRcvCellsCounters_Object((1,3,6,1,4,1,119,2,3,3,13,110,10,1,1,7),_MpAtmCCPathTestRcvCellsCounters_Type())
mpAtmCCPathTestRcvCellsCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPathTestRcvCellsCounters.setStatus(_A)
_MpAtmCCPathTestErrInfo_Type=Integer32
_MpAtmCCPathTestErrInfo_Object=MibTableColumn
mpAtmCCPathTestErrInfo=_MpAtmCCPathTestErrInfo_Object((1,3,6,1,4,1,119,2,3,3,13,110,10,1,1,99),_MpAtmCCPathTestErrInfo_Type())
mpAtmCCPathTestErrInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPathTestErrInfo.setStatus(_A)
_MpAtmCCPvcGroupCutover_ObjectIdentity=ObjectIdentity
mpAtmCCPvcGroupCutover=_MpAtmCCPvcGroupCutover_ObjectIdentity((1,3,6,1,4,1,119,2,3,3,13,110,11))
_MpAtmCCPvcGroupCutoverBaseInfo_ObjectIdentity=ObjectIdentity
mpAtmCCPvcGroupCutoverBaseInfo=_MpAtmCCPvcGroupCutoverBaseInfo_ObjectIdentity((1,3,6,1,4,1,119,2,3,3,13,110,11,1))
class _MpAtmCCPvcGroupCutoverEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_O,2)))
_MpAtmCCPvcGroupCutoverEnable_Type.__name__=_C
_MpAtmCCPvcGroupCutoverEnable_Object=MibScalar
mpAtmCCPvcGroupCutoverEnable=_MpAtmCCPvcGroupCutoverEnable_Object((1,3,6,1,4,1,119,2,3,3,13,110,11,1,1),_MpAtmCCPvcGroupCutoverEnable_Type())
mpAtmCCPvcGroupCutoverEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPvcGroupCutoverEnable.setStatus(_A)
class _MpAtmCCPvcGroupCutoverStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('null',1),('underAvtivate',2),(_Y,3)))
_MpAtmCCPvcGroupCutoverStatus_Type.__name__=_C
_MpAtmCCPvcGroupCutoverStatus_Object=MibScalar
mpAtmCCPvcGroupCutoverStatus=_MpAtmCCPvcGroupCutoverStatus_Object((1,3,6,1,4,1,119,2,3,3,13,110,11,1,2),_MpAtmCCPvcGroupCutoverStatus_Type())
mpAtmCCPvcGroupCutoverStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPvcGroupCutoverStatus.setStatus(_A)
_MpAtmCCUnitePvcGroup_ObjectIdentity=ObjectIdentity
mpAtmCCUnitePvcGroup=_MpAtmCCUnitePvcGroup_ObjectIdentity((1,3,6,1,4,1,119,2,3,3,13,110,11,2))
_MpAtmCCUpgcBaseInfo_ObjectIdentity=ObjectIdentity
mpAtmCCUpgcBaseInfo=_MpAtmCCUpgcBaseInfo_ObjectIdentity((1,3,6,1,4,1,119,2,3,3,13,110,11,2,1))
_MpAtmCCUpgcTotalGroupNumber_Type=Integer32
_MpAtmCCUpgcTotalGroupNumber_Object=MibScalar
mpAtmCCUpgcTotalGroupNumber=_MpAtmCCUpgcTotalGroupNumber_Object((1,3,6,1,4,1,119,2,3,3,13,110,11,2,1,1),_MpAtmCCUpgcTotalGroupNumber_Type())
mpAtmCCUpgcTotalGroupNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCUpgcTotalGroupNumber.setStatus(_A)
_MpAtmCCUpgcBaseActiveGroupNumber_Type=Integer32
_MpAtmCCUpgcBaseActiveGroupNumber_Object=MibScalar
mpAtmCCUpgcBaseActiveGroupNumber=_MpAtmCCUpgcBaseActiveGroupNumber_Object((1,3,6,1,4,1,119,2,3,3,13,110,11,2,1,2),_MpAtmCCUpgcBaseActiveGroupNumber_Type())
mpAtmCCUpgcBaseActiveGroupNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCUpgcBaseActiveGroupNumber.setStatus(_A)
_MpAtmCCUnitePvcGroupControlTable_Object=MibTable
mpAtmCCUnitePvcGroupControlTable=_MpAtmCCUnitePvcGroupControlTable_Object((1,3,6,1,4,1,119,2,3,3,13,110,11,2,2))
if mibBuilder.loadTexts:mpAtmCCUnitePvcGroupControlTable.setStatus(_A)
_MpAtmCCUpgcCtlEntry_Object=MibTableRow
mpAtmCCUpgcCtlEntry=_MpAtmCCUpgcCtlEntry_Object((1,3,6,1,4,1,119,2,3,3,13,110,11,2,2,1))
mpAtmCCUpgcCtlEntry.setIndexNames((0,_E,_Z))
if mibBuilder.loadTexts:mpAtmCCUpgcCtlEntry.setStatus(_A)
class _MpAtmCCUpgcIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_MpAtmCCUpgcIndex_Type.__name__=_C
_MpAtmCCUpgcIndex_Object=MibTableColumn
mpAtmCCUpgcIndex=_MpAtmCCUpgcIndex_Object((1,3,6,1,4,1,119,2,3,3,13,110,11,2,2,1,1),_MpAtmCCUpgcIndex_Type())
mpAtmCCUpgcIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCUpgcIndex.setStatus(_A)
class _MpAtmCCUpgcCtlStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('register',1),(_R,2),(_a,3),(_K,4),(_b,5),(_AK,6),(_Y,7)))
_MpAtmCCUpgcCtlStatus_Type.__name__=_C
_MpAtmCCUpgcCtlStatus_Object=MibTableColumn
mpAtmCCUpgcCtlStatus=_MpAtmCCUpgcCtlStatus_Object((1,3,6,1,4,1,119,2,3,3,13,110,11,2,2,1,2),_MpAtmCCUpgcCtlStatus_Type())
mpAtmCCUpgcCtlStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCUpgcCtlStatus.setStatus(_A)
_MpAtmCCUpgcCtlCountPgc_Type=Integer32
_MpAtmCCUpgcCtlCountPgc_Object=MibTableColumn
mpAtmCCUpgcCtlCountPgc=_MpAtmCCUpgcCtlCountPgc_Object((1,3,6,1,4,1,119,2,3,3,13,110,11,2,2,1,3),_MpAtmCCUpgcCtlCountPgc_Type())
mpAtmCCUpgcCtlCountPgc.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCUpgcCtlCountPgc.setStatus(_A)
_MpAtmCCUpgcCtlResult_Type=Integer32
_MpAtmCCUpgcCtlResult_Object=MibTableColumn
mpAtmCCUpgcCtlResult=_MpAtmCCUpgcCtlResult_Object((1,3,6,1,4,1,119,2,3,3,13,110,11,2,2,1,4),_MpAtmCCUpgcCtlResult_Type())
mpAtmCCUpgcCtlResult.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCUpgcCtlResult.setStatus(_A)
_MpAtmCCUnitePvcGroupRegisterTable_Object=MibTable
mpAtmCCUnitePvcGroupRegisterTable=_MpAtmCCUnitePvcGroupRegisterTable_Object((1,3,6,1,4,1,119,2,3,3,13,110,11,2,3))
if mibBuilder.loadTexts:mpAtmCCUnitePvcGroupRegisterTable.setStatus(_A)
_MpAtmCCUpgcRegiEntry_Object=MibTableRow
mpAtmCCUpgcRegiEntry=_MpAtmCCUpgcRegiEntry_Object((1,3,6,1,4,1,119,2,3,3,13,110,11,2,3,1))
mpAtmCCUpgcRegiEntry.setIndexNames((0,_E,_Z),(0,_E,_AL))
if mibBuilder.loadTexts:mpAtmCCUpgcRegiEntry.setStatus(_A)
class _MpAtmCCUpgcPgcIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_MpAtmCCUpgcPgcIndex_Type.__name__=_C
_MpAtmCCUpgcPgcIndex_Object=MibTableColumn
mpAtmCCUpgcPgcIndex=_MpAtmCCUpgcPgcIndex_Object((1,3,6,1,4,1,119,2,3,3,13,110,11,2,3,1,1),_MpAtmCCUpgcPgcIndex_Type())
mpAtmCCUpgcPgcIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCUpgcPgcIndex.setStatus(_A)
class _MpAtmCCUpgcRegiStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('add',1),(_K,2),(_M,3)))
_MpAtmCCUpgcRegiStatus_Type.__name__=_C
_MpAtmCCUpgcRegiStatus_Object=MibTableColumn
mpAtmCCUpgcRegiStatus=_MpAtmCCUpgcRegiStatus_Object((1,3,6,1,4,1,119,2,3,3,13,110,11,2,3,1,2),_MpAtmCCUpgcRegiStatus_Type())
mpAtmCCUpgcRegiStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCUpgcRegiStatus.setStatus(_A)
_MpAtmCCPvcGroup_ObjectIdentity=ObjectIdentity
mpAtmCCPvcGroup=_MpAtmCCPvcGroup_ObjectIdentity((1,3,6,1,4,1,119,2,3,3,13,110,11,3))
_MpAtmCCPgcBaseInfo_ObjectIdentity=ObjectIdentity
mpAtmCCPgcBaseInfo=_MpAtmCCPgcBaseInfo_ObjectIdentity((1,3,6,1,4,1,119,2,3,3,13,110,11,3,1))
_MpAtmCCPgcTotalGroupNumber_Type=Integer32
_MpAtmCCPgcTotalGroupNumber_Object=MibScalar
mpAtmCCPgcTotalGroupNumber=_MpAtmCCPgcTotalGroupNumber_Object((1,3,6,1,4,1,119,2,3,3,13,110,11,3,1,1),_MpAtmCCPgcTotalGroupNumber_Type())
mpAtmCCPgcTotalGroupNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPgcTotalGroupNumber.setStatus(_A)
_MpAtmCCPvcGroupControlTable_Object=MibTable
mpAtmCCPvcGroupControlTable=_MpAtmCCPvcGroupControlTable_Object((1,3,6,1,4,1,119,2,3,3,13,110,11,3,2))
if mibBuilder.loadTexts:mpAtmCCPvcGroupControlTable.setStatus(_A)
_MpAtmCCPgcCtlEntry_Object=MibTableRow
mpAtmCCPgcCtlEntry=_MpAtmCCPgcCtlEntry_Object((1,3,6,1,4,1,119,2,3,3,13,110,11,3,2,1))
mpAtmCCPgcCtlEntry.setIndexNames((0,_E,_c))
if mibBuilder.loadTexts:mpAtmCCPgcCtlEntry.setStatus(_A)
class _MpAtmCCPgcIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
_MpAtmCCPgcIndex_Type.__name__=_C
_MpAtmCCPgcIndex_Object=MibTableColumn
mpAtmCCPgcIndex=_MpAtmCCPgcIndex_Object((1,3,6,1,4,1,119,2,3,3,13,110,11,3,2,1,1),_MpAtmCCPgcIndex_Type())
mpAtmCCPgcIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPgcIndex.setStatus(_A)
class _MpAtmCCPgcCtlStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('register',1),(_R,2),(_a,3),(_K,4),(_b,5),(_AK,6),(_Y,7)))
_MpAtmCCPgcCtlStatus_Type.__name__=_C
_MpAtmCCPgcCtlStatus_Object=MibTableColumn
mpAtmCCPgcCtlStatus=_MpAtmCCPgcCtlStatus_Object((1,3,6,1,4,1,119,2,3,3,13,110,11,3,2,1,2),_MpAtmCCPgcCtlStatus_Type())
mpAtmCCPgcCtlStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCPgcCtlStatus.setStatus(_A)
_MpAtmCCPgcCtlCountPvc_Type=Integer32
_MpAtmCCPgcCtlCountPvc_Object=MibTableColumn
mpAtmCCPgcCtlCountPvc=_MpAtmCCPgcCtlCountPvc_Object((1,3,6,1,4,1,119,2,3,3,13,110,11,3,2,1,3),_MpAtmCCPgcCtlCountPvc_Type())
mpAtmCCPgcCtlCountPvc.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPgcCtlCountPvc.setStatus(_A)
_MpAtmCCPgcCtlResult_Type=Integer32
_MpAtmCCPgcCtlResult_Object=MibTableColumn
mpAtmCCPgcCtlResult=_MpAtmCCPgcCtlResult_Object((1,3,6,1,4,1,119,2,3,3,13,110,11,3,2,1,4),_MpAtmCCPgcCtlResult_Type())
mpAtmCCPgcCtlResult.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPgcCtlResult.setStatus(_A)
_MpAtmCCPvcGroupRegisterTable_Object=MibTable
mpAtmCCPvcGroupRegisterTable=_MpAtmCCPvcGroupRegisterTable_Object((1,3,6,1,4,1,119,2,3,3,13,110,11,3,3))
if mibBuilder.loadTexts:mpAtmCCPvcGroupRegisterTable.setStatus(_A)
_MpAtmCCPgcRegiEntry_Object=MibTableRow
mpAtmCCPgcRegiEntry=_MpAtmCCPgcRegiEntry_Object((1,3,6,1,4,1,119,2,3,3,13,110,11,3,3,1))
mpAtmCCPgcRegiEntry.setIndexNames((0,_E,_c),(0,_E,_AM),(0,_E,_AN),(0,_E,_AO))
if mibBuilder.loadTexts:mpAtmCCPgcRegiEntry.setStatus(_A)
_MpAtmCCPgcPvcIfIndex_Type=Integer32
_MpAtmCCPgcPvcIfIndex_Object=MibTableColumn
mpAtmCCPgcPvcIfIndex=_MpAtmCCPgcPvcIfIndex_Object((1,3,6,1,4,1,119,2,3,3,13,110,11,3,3,1,1),_MpAtmCCPgcPvcIfIndex_Type())
mpAtmCCPgcPvcIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:mpAtmCCPgcPvcIfIndex.setStatus(_A)
_MpAtmCCPgcPvcVpi_Type=Integer32
_MpAtmCCPgcPvcVpi_Object=MibTableColumn
mpAtmCCPgcPvcVpi=_MpAtmCCPgcPvcVpi_Object((1,3,6,1,4,1,119,2,3,3,13,110,11,3,3,1,2),_MpAtmCCPgcPvcVpi_Type())
mpAtmCCPgcPvcVpi.setMaxAccess(_F)
if mibBuilder.loadTexts:mpAtmCCPgcPvcVpi.setStatus(_A)
_MpAtmCCPgcPvcVci_Type=Integer32
_MpAtmCCPgcPvcVci_Object=MibTableColumn
mpAtmCCPgcPvcVci=_MpAtmCCPgcPvcVci_Object((1,3,6,1,4,1,119,2,3,3,13,110,11,3,3,1,3),_MpAtmCCPgcPvcVci_Type())
mpAtmCCPgcPvcVci.setMaxAccess(_F)
if mibBuilder.loadTexts:mpAtmCCPgcPvcVci.setStatus(_A)
class _MpAtmCCPgcPvcKind_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('staticPvc',1),('softPvc',2)))
_MpAtmCCPgcPvcKind_Type.__name__=_C
_MpAtmCCPgcPvcKind_Object=MibTableColumn
mpAtmCCPgcPvcKind=_MpAtmCCPgcPvcKind_Object((1,3,6,1,4,1,119,2,3,3,13,110,11,3,3,1,4),_MpAtmCCPgcPvcKind_Type())
mpAtmCCPgcPvcKind.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCPgcPvcKind.setStatus(_A)
_MpAtmCCPgcStaticPvcDestIfIndex_Type=Integer32
_MpAtmCCPgcStaticPvcDestIfIndex_Object=MibTableColumn
mpAtmCCPgcStaticPvcDestIfIndex=_MpAtmCCPgcStaticPvcDestIfIndex_Object((1,3,6,1,4,1,119,2,3,3,13,110,11,3,3,1,5),_MpAtmCCPgcStaticPvcDestIfIndex_Type())
mpAtmCCPgcStaticPvcDestIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCPgcStaticPvcDestIfIndex.setStatus(_A)
_MpAtmCCPgcSoftPvcDestAtmAddress_Type=AtmAddr
_MpAtmCCPgcSoftPvcDestAtmAddress_Object=MibTableColumn
mpAtmCCPgcSoftPvcDestAtmAddress=_MpAtmCCPgcSoftPvcDestAtmAddress_Object((1,3,6,1,4,1,119,2,3,3,13,110,11,3,3,1,6),_MpAtmCCPgcSoftPvcDestAtmAddress_Type())
mpAtmCCPgcSoftPvcDestAtmAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCPgcSoftPvcDestAtmAddress.setStatus(_A)
_MpAtmCCPgcPvcDestVpi_Type=Integer32
_MpAtmCCPgcPvcDestVpi_Object=MibTableColumn
mpAtmCCPgcPvcDestVpi=_MpAtmCCPgcPvcDestVpi_Object((1,3,6,1,4,1,119,2,3,3,13,110,11,3,3,1,7),_MpAtmCCPgcPvcDestVpi_Type())
mpAtmCCPgcPvcDestVpi.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCPgcPvcDestVpi.setStatus(_A)
_MpAtmCCPgcPvcDestVci_Type=Integer32
_MpAtmCCPgcPvcDestVci_Object=MibTableColumn
mpAtmCCPgcPvcDestVci=_MpAtmCCPgcPvcDestVci_Object((1,3,6,1,4,1,119,2,3,3,13,110,11,3,3,1,8),_MpAtmCCPgcPvcDestVci_Type())
mpAtmCCPgcPvcDestVci.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCPgcPvcDestVci.setStatus(_A)
_MpAtmCCPgcPvcReceiveTrafficDescrIndex_Type=AtmTrafficDescrParamIndex
_MpAtmCCPgcPvcReceiveTrafficDescrIndex_Object=MibTableColumn
mpAtmCCPgcPvcReceiveTrafficDescrIndex=_MpAtmCCPgcPvcReceiveTrafficDescrIndex_Object((1,3,6,1,4,1,119,2,3,3,13,110,11,3,3,1,9),_MpAtmCCPgcPvcReceiveTrafficDescrIndex_Type())
mpAtmCCPgcPvcReceiveTrafficDescrIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCPgcPvcReceiveTrafficDescrIndex.setStatus(_A)
_MpAtmCCPgcPvcTransmitTrafficDescrIndex_Type=AtmTrafficDescrParamIndex
_MpAtmCCPgcPvcTransmitTrafficDescrIndex_Object=MibTableColumn
mpAtmCCPgcPvcTransmitTrafficDescrIndex=_MpAtmCCPgcPvcTransmitTrafficDescrIndex_Object((1,3,6,1,4,1,119,2,3,3,13,110,11,3,3,1,10),_MpAtmCCPgcPvcTransmitTrafficDescrIndex_Type())
mpAtmCCPgcPvcTransmitTrafficDescrIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCPgcPvcTransmitTrafficDescrIndex.setStatus(_A)
class _MpAtmCCPgcPvcPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_MpAtmCCPgcPvcPriority_Type.__name__=_C
_MpAtmCCPgcPvcPriority_Object=MibTableColumn
mpAtmCCPgcPvcPriority=_MpAtmCCPgcPvcPriority_Object((1,3,6,1,4,1,119,2,3,3,13,110,11,3,3,1,11),_MpAtmCCPgcPvcPriority_Type())
mpAtmCCPgcPvcPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCPgcPvcPriority.setStatus(_A)
_MpAtmCCPgcStaticPvcId_Type=Integer32
_MpAtmCCPgcStaticPvcId_Object=MibTableColumn
mpAtmCCPgcStaticPvcId=_MpAtmCCPgcStaticPvcId_Object((1,3,6,1,4,1,119,2,3,3,13,110,11,3,3,1,12),_MpAtmCCPgcStaticPvcId_Type())
mpAtmCCPgcStaticPvcId.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCPgcStaticPvcId.setStatus(_A)
_MpAtmCCPgcStaticPvcSeqNo_Type=Integer32
_MpAtmCCPgcStaticPvcSeqNo_Object=MibTableColumn
mpAtmCCPgcStaticPvcSeqNo=_MpAtmCCPgcStaticPvcSeqNo_Object((1,3,6,1,4,1,119,2,3,3,13,110,11,3,3,1,13),_MpAtmCCPgcStaticPvcSeqNo_Type())
mpAtmCCPgcStaticPvcSeqNo.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCPgcStaticPvcSeqNo.setStatus(_A)
class _MpAtmCCPgcSoftPvcCallKind_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_T,2)))
_MpAtmCCPgcSoftPvcCallKind_Type.__name__=_C
_MpAtmCCPgcSoftPvcCallKind_Object=MibTableColumn
mpAtmCCPgcSoftPvcCallKind=_MpAtmCCPgcSoftPvcCallKind_Object((1,3,6,1,4,1,119,2,3,3,13,110,11,3,3,1,14),_MpAtmCCPgcSoftPvcCallKind_Type())
mpAtmCCPgcSoftPvcCallKind.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCPgcSoftPvcCallKind.setStatus(_A)
class _MpAtmCCPgcRegiAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_a,1),(_R,2),(_b,3),('connectWait',4),('disconnectWait',5)))
_MpAtmCCPgcRegiAdminStatus_Type.__name__=_C
_MpAtmCCPgcRegiAdminStatus_Object=MibTableColumn
mpAtmCCPgcRegiAdminStatus=_MpAtmCCPgcRegiAdminStatus_Object((1,3,6,1,4,1,119,2,3,3,13,110,11,3,3,1,15),_MpAtmCCPgcRegiAdminStatus_Type())
mpAtmCCPgcRegiAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCPgcRegiAdminStatus.setStatus(_A)
class _MpAtmCCPgcRegiCfgStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_M,1),(_N,2),(_K,3),(_L,4)))
_MpAtmCCPgcRegiCfgStatus_Type.__name__=_C
_MpAtmCCPgcRegiCfgStatus_Object=MibTableColumn
mpAtmCCPgcRegiCfgStatus=_MpAtmCCPgcRegiCfgStatus_Object((1,3,6,1,4,1,119,2,3,3,13,110,11,3,3,1,16),_MpAtmCCPgcRegiCfgStatus_Type())
mpAtmCCPgcRegiCfgStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCPgcRegiCfgStatus.setStatus(_A)
_MpAtmCCPgcRegiErrInfo_Type=Integer32
_MpAtmCCPgcRegiErrInfo_Object=MibTableColumn
mpAtmCCPgcRegiErrInfo=_MpAtmCCPgcRegiErrInfo_Object((1,3,6,1,4,1,119,2,3,3,13,110,11,3,3,1,17),_MpAtmCCPgcRegiErrInfo_Type())
mpAtmCCPgcRegiErrInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPgcRegiErrInfo.setStatus(_A)
_MpAtmCCPvcGroupActiveInfoTable_Object=MibTable
mpAtmCCPvcGroupActiveInfoTable=_MpAtmCCPvcGroupActiveInfoTable_Object((1,3,6,1,4,1,119,2,3,3,13,110,11,3,4))
if mibBuilder.loadTexts:mpAtmCCPvcGroupActiveInfoTable.setStatus(_A)
_MpAtmCCPgcActInfoEntry_Object=MibTableRow
mpAtmCCPgcActInfoEntry=_MpAtmCCPgcActInfoEntry_Object((1,3,6,1,4,1,119,2,3,3,13,110,11,3,4,1))
mpAtmCCPgcActInfoEntry.setIndexNames((0,_E,_AP))
if mibBuilder.loadTexts:mpAtmCCPgcActInfoEntry.setStatus(_A)
_MpAtmCCPgcActGrpNum_Type=Integer32
_MpAtmCCPgcActGrpNum_Object=MibTableColumn
mpAtmCCPgcActGrpNum=_MpAtmCCPgcActGrpNum_Object((1,3,6,1,4,1,119,2,3,3,13,110,11,3,4,1,1),_MpAtmCCPgcActGrpNum_Type())
mpAtmCCPgcActGrpNum.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCPgcActGrpNum.setStatus(_A)
_MpAtmCCAtmMulticast_ObjectIdentity=ObjectIdentity
mpAtmCCAtmMulticast=_MpAtmCCAtmMulticast_ObjectIdentity((1,3,6,1,4,1,119,2,3,3,13,110,12))
_MpAtmCCAtmMulticastRegistration_ObjectIdentity=ObjectIdentity
mpAtmCCAtmMulticastRegistration=_MpAtmCCAtmMulticastRegistration_ObjectIdentity((1,3,6,1,4,1,119,2,3,3,13,110,12,1))
_MpAtmCCAtmMultiRootIfIndex_Type=Integer32
_MpAtmCCAtmMultiRootIfIndex_Object=MibScalar
mpAtmCCAtmMultiRootIfIndex=_MpAtmCCAtmMultiRootIfIndex_Object((1,3,6,1,4,1,119,2,3,3,13,110,12,1,1),_MpAtmCCAtmMultiRootIfIndex_Type())
mpAtmCCAtmMultiRootIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCAtmMultiRootIfIndex.setStatus(_A)
_MpAtmCCAtmMultiRootVpi_Type=Integer32
_MpAtmCCAtmMultiRootVpi_Object=MibScalar
mpAtmCCAtmMultiRootVpi=_MpAtmCCAtmMultiRootVpi_Object((1,3,6,1,4,1,119,2,3,3,13,110,12,1,2),_MpAtmCCAtmMultiRootVpi_Type())
mpAtmCCAtmMultiRootVpi.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCAtmMultiRootVpi.setStatus(_A)
_MpAtmCCAtmMultiRootVci_Type=Integer32
_MpAtmCCAtmMultiRootVci_Object=MibScalar
mpAtmCCAtmMultiRootVci=_MpAtmCCAtmMultiRootVci_Object((1,3,6,1,4,1,119,2,3,3,13,110,12,1,3),_MpAtmCCAtmMultiRootVci_Type())
mpAtmCCAtmMultiRootVci.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCAtmMultiRootVci.setStatus(_A)
_MpAtmCCAtmMultiLeafIfIndex_Type=Integer32
_MpAtmCCAtmMultiLeafIfIndex_Object=MibScalar
mpAtmCCAtmMultiLeafIfIndex=_MpAtmCCAtmMultiLeafIfIndex_Object((1,3,6,1,4,1,119,2,3,3,13,110,12,1,4),_MpAtmCCAtmMultiLeafIfIndex_Type())
mpAtmCCAtmMultiLeafIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCAtmMultiLeafIfIndex.setStatus(_A)
_MpAtmCCAtmMultiLeafVpi_Type=Integer32
_MpAtmCCAtmMultiLeafVpi_Object=MibScalar
mpAtmCCAtmMultiLeafVpi=_MpAtmCCAtmMultiLeafVpi_Object((1,3,6,1,4,1,119,2,3,3,13,110,12,1,5),_MpAtmCCAtmMultiLeafVpi_Type())
mpAtmCCAtmMultiLeafVpi.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCAtmMultiLeafVpi.setStatus(_A)
_MpAtmCCAtmMultiLeafVci_Type=Integer32
_MpAtmCCAtmMultiLeafVci_Object=MibScalar
mpAtmCCAtmMultiLeafVci=_MpAtmCCAtmMultiLeafVci_Object((1,3,6,1,4,1,119,2,3,3,13,110,12,1,6),_MpAtmCCAtmMultiLeafVci_Type())
mpAtmCCAtmMultiLeafVci.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCAtmMultiLeafVci.setStatus(_A)
_MpAtmCCAtmMultiTrafficDescrIndex_Type=AtmTrafficDescrParamIndex
_MpAtmCCAtmMultiTrafficDescrIndex_Object=MibScalar
mpAtmCCAtmMultiTrafficDescrIndex=_MpAtmCCAtmMultiTrafficDescrIndex_Object((1,3,6,1,4,1,119,2,3,3,13,110,12,1,7),_MpAtmCCAtmMultiTrafficDescrIndex_Type())
mpAtmCCAtmMultiTrafficDescrIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCAtmMultiTrafficDescrIndex.setStatus(_A)
_MpAtmCCAtmMultiSlotNumber_Type=Integer32
_MpAtmCCAtmMultiSlotNumber_Object=MibScalar
mpAtmCCAtmMultiSlotNumber=_MpAtmCCAtmMultiSlotNumber_Object((1,3,6,1,4,1,119,2,3,3,13,110,12,1,8),_MpAtmCCAtmMultiSlotNumber_Type())
mpAtmCCAtmMultiSlotNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCAtmMultiSlotNumber.setStatus(_A)
class _MpAtmCCAtmMultiVcRdiResponse_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_O,2)))
_MpAtmCCAtmMultiVcRdiResponse_Type.__name__=_C
_MpAtmCCAtmMultiVcRdiResponse_Object=MibScalar
mpAtmCCAtmMultiVcRdiResponse=_MpAtmCCAtmMultiVcRdiResponse_Object((1,3,6,1,4,1,119,2,3,3,13,110,12,1,9),_MpAtmCCAtmMultiVcRdiResponse_Type())
mpAtmCCAtmMultiVcRdiResponse.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCAtmMultiVcRdiResponse.setStatus(_A)
_MpAtmCCAtmMultiPvcId_Type=Integer32
_MpAtmCCAtmMultiPvcId_Object=MibScalar
mpAtmCCAtmMultiPvcId=_MpAtmCCAtmMultiPvcId_Object((1,3,6,1,4,1,119,2,3,3,13,110,12,1,10),_MpAtmCCAtmMultiPvcId_Type())
mpAtmCCAtmMultiPvcId.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCAtmMultiPvcId.setStatus(_A)
_MpAtmCCAtmMultiSeqNo_Type=Integer32
_MpAtmCCAtmMultiSeqNo_Object=MibScalar
mpAtmCCAtmMultiSeqNo=_MpAtmCCAtmMultiSeqNo_Object((1,3,6,1,4,1,119,2,3,3,13,110,12,1,11),_MpAtmCCAtmMultiSeqNo_Type())
mpAtmCCAtmMultiSeqNo.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCAtmMultiSeqNo.setStatus(_A)
class _MpAtmCCAtmMultiCfgStatus_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_M,1),(_N,2),(_K,3),(_L,4)))
_MpAtmCCAtmMultiCfgStatus_Type.__name__=_C
_MpAtmCCAtmMultiCfgStatus_Object=MibScalar
mpAtmCCAtmMultiCfgStatus=_MpAtmCCAtmMultiCfgStatus_Object((1,3,6,1,4,1,119,2,3,3,13,110,12,1,98),_MpAtmCCAtmMultiCfgStatus_Type())
mpAtmCCAtmMultiCfgStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCAtmMultiCfgStatus.setStatus(_A)
_MpAtmCCAtmMultiRegErrInfo_Type=Integer32
_MpAtmCCAtmMultiRegErrInfo_Object=MibScalar
mpAtmCCAtmMultiRegErrInfo=_MpAtmCCAtmMultiRegErrInfo_Object((1,3,6,1,4,1,119,2,3,3,13,110,12,1,99),_MpAtmCCAtmMultiRegErrInfo_Type())
mpAtmCCAtmMultiRegErrInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCAtmMultiRegErrInfo.setStatus(_A)
_MpAtmCCAtmMulticastCtlTable_Object=MibTable
mpAtmCCAtmMulticastCtlTable=_MpAtmCCAtmMulticastCtlTable_Object((1,3,6,1,4,1,119,2,3,3,13,110,12,2))
if mibBuilder.loadTexts:mpAtmCCAtmMulticastCtlTable.setStatus(_A)
_MpAtmCCAtmMultiCtlEntry_Object=MibTableRow
mpAtmCCAtmMultiCtlEntry=_MpAtmCCAtmMultiCtlEntry_Object((1,3,6,1,4,1,119,2,3,3,13,110,12,2,1))
mpAtmCCAtmMultiCtlEntry.setIndexNames((0,_E,_AQ),(0,_E,_AR),(0,_E,_AS))
if mibBuilder.loadTexts:mpAtmCCAtmMultiCtlEntry.setStatus(_A)
_MpAtmCCAtmMultiIfIndex_Type=Integer32
_MpAtmCCAtmMultiIfIndex_Object=MibTableColumn
mpAtmCCAtmMultiIfIndex=_MpAtmCCAtmMultiIfIndex_Object((1,3,6,1,4,1,119,2,3,3,13,110,12,2,1,1),_MpAtmCCAtmMultiIfIndex_Type())
mpAtmCCAtmMultiIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:mpAtmCCAtmMultiIfIndex.setStatus(_A)
_MpAtmCCAtmMultiVpi_Type=Integer32
_MpAtmCCAtmMultiVpi_Object=MibTableColumn
mpAtmCCAtmMultiVpi=_MpAtmCCAtmMultiVpi_Object((1,3,6,1,4,1,119,2,3,3,13,110,12,2,1,2),_MpAtmCCAtmMultiVpi_Type())
mpAtmCCAtmMultiVpi.setMaxAccess(_F)
if mibBuilder.loadTexts:mpAtmCCAtmMultiVpi.setStatus(_A)
_MpAtmCCAtmMultiVci_Type=Integer32
_MpAtmCCAtmMultiVci_Object=MibTableColumn
mpAtmCCAtmMultiVci=_MpAtmCCAtmMultiVci_Object((1,3,6,1,4,1,119,2,3,3,13,110,12,2,1,3),_MpAtmCCAtmMultiVci_Type())
mpAtmCCAtmMultiVci.setMaxAccess(_F)
if mibBuilder.loadTexts:mpAtmCCAtmMultiVci.setStatus(_A)
class _MpAtmCCAtmMultiAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_MpAtmCCAtmMultiAdminStatus_Type.__name__=_C
_MpAtmCCAtmMultiAdminStatus_Object=MibTableColumn
mpAtmCCAtmMultiAdminStatus=_MpAtmCCAtmMultiAdminStatus_Object((1,3,6,1,4,1,119,2,3,3,13,110,12,2,1,4),_MpAtmCCAtmMultiAdminStatus_Type())
mpAtmCCAtmMultiAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAtmCCAtmMultiAdminStatus.setStatus(_A)
class _MpAtmCCAtmMultiOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_MpAtmCCAtmMultiOperStatus_Type.__name__=_C
_MpAtmCCAtmMultiOperStatus_Object=MibTableColumn
mpAtmCCAtmMultiOperStatus=_MpAtmCCAtmMultiOperStatus_Object((1,3,6,1,4,1,119,2,3,3,13,110,12,2,1,5),_MpAtmCCAtmMultiOperStatus_Type())
mpAtmCCAtmMultiOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCAtmMultiOperStatus.setStatus(_A)
_MpAtmCCAtmMultiErrInfo_Type=Integer32
_MpAtmCCAtmMultiErrInfo_Object=MibTableColumn
mpAtmCCAtmMultiErrInfo=_MpAtmCCAtmMultiErrInfo_Object((1,3,6,1,4,1,119,2,3,3,13,110,12,2,1,99),_MpAtmCCAtmMultiErrInfo_Type())
mpAtmCCAtmMultiErrInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCAtmMultiErrInfo.setStatus(_A)
_MpAtmCCAtmMulticastConfTable_Object=MibTable
mpAtmCCAtmMulticastConfTable=_MpAtmCCAtmMulticastConfTable_Object((1,3,6,1,4,1,119,2,3,3,13,110,12,3))
if mibBuilder.loadTexts:mpAtmCCAtmMulticastConfTable.setStatus(_A)
_MpAtmCCAtmMultiConfEntry_Object=MibTableRow
mpAtmCCAtmMultiConfEntry=_MpAtmCCAtmMultiConfEntry_Object((1,3,6,1,4,1,119,2,3,3,13,110,12,3,1))
mpAtmCCAtmMultiConfEntry.setIndexNames((0,_E,_AT),(0,_E,_AU),(0,_E,_AV),(0,_E,_AW),(0,_E,_AX),(0,_E,_AY))
if mibBuilder.loadTexts:mpAtmCCAtmMultiConfEntry.setStatus(_A)
_MpAtmCCAtmMultiConfRootIfIndex_Type=Integer32
_MpAtmCCAtmMultiConfRootIfIndex_Object=MibTableColumn
mpAtmCCAtmMultiConfRootIfIndex=_MpAtmCCAtmMultiConfRootIfIndex_Object((1,3,6,1,4,1,119,2,3,3,13,110,12,3,1,1),_MpAtmCCAtmMultiConfRootIfIndex_Type())
mpAtmCCAtmMultiConfRootIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCAtmMultiConfRootIfIndex.setStatus(_A)
_MpAtmCCAtmMultiConfRootVpi_Type=Integer32
_MpAtmCCAtmMultiConfRootVpi_Object=MibTableColumn
mpAtmCCAtmMultiConfRootVpi=_MpAtmCCAtmMultiConfRootVpi_Object((1,3,6,1,4,1,119,2,3,3,13,110,12,3,1,2),_MpAtmCCAtmMultiConfRootVpi_Type())
mpAtmCCAtmMultiConfRootVpi.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCAtmMultiConfRootVpi.setStatus(_A)
_MpAtmCCAtmMultiConfRootVci_Type=Integer32
_MpAtmCCAtmMultiConfRootVci_Object=MibTableColumn
mpAtmCCAtmMultiConfRootVci=_MpAtmCCAtmMultiConfRootVci_Object((1,3,6,1,4,1,119,2,3,3,13,110,12,3,1,3),_MpAtmCCAtmMultiConfRootVci_Type())
mpAtmCCAtmMultiConfRootVci.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCAtmMultiConfRootVci.setStatus(_A)
_MpAtmCCAtmMultiConfLeafIfIndex_Type=Integer32
_MpAtmCCAtmMultiConfLeafIfIndex_Object=MibTableColumn
mpAtmCCAtmMultiConfLeafIfIndex=_MpAtmCCAtmMultiConfLeafIfIndex_Object((1,3,6,1,4,1,119,2,3,3,13,110,12,3,1,4),_MpAtmCCAtmMultiConfLeafIfIndex_Type())
mpAtmCCAtmMultiConfLeafIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCAtmMultiConfLeafIfIndex.setStatus(_A)
_MpAtmCCAtmMultiConfLeafVpi_Type=Integer32
_MpAtmCCAtmMultiConfLeafVpi_Object=MibTableColumn
mpAtmCCAtmMultiConfLeafVpi=_MpAtmCCAtmMultiConfLeafVpi_Object((1,3,6,1,4,1,119,2,3,3,13,110,12,3,1,5),_MpAtmCCAtmMultiConfLeafVpi_Type())
mpAtmCCAtmMultiConfLeafVpi.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCAtmMultiConfLeafVpi.setStatus(_A)
_MpAtmCCAtmMultiConfLeafVci_Type=Integer32
_MpAtmCCAtmMultiConfLeafVci_Object=MibTableColumn
mpAtmCCAtmMultiConfLeafVci=_MpAtmCCAtmMultiConfLeafVci_Object((1,3,6,1,4,1,119,2,3,3,13,110,12,3,1,6),_MpAtmCCAtmMultiConfLeafVci_Type())
mpAtmCCAtmMultiConfLeafVci.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCAtmMultiConfLeafVci.setStatus(_A)
class _MpAtmCCAtmMultiConfRootAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_MpAtmCCAtmMultiConfRootAdminStatus_Type.__name__=_C
_MpAtmCCAtmMultiConfRootAdminStatus_Object=MibTableColumn
mpAtmCCAtmMultiConfRootAdminStatus=_MpAtmCCAtmMultiConfRootAdminStatus_Object((1,3,6,1,4,1,119,2,3,3,13,110,12,3,1,7),_MpAtmCCAtmMultiConfRootAdminStatus_Type())
mpAtmCCAtmMultiConfRootAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCAtmMultiConfRootAdminStatus.setStatus(_A)
class _MpAtmCCAtmMultiConfRootOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_MpAtmCCAtmMultiConfRootOperStatus_Type.__name__=_C
_MpAtmCCAtmMultiConfRootOperStatus_Object=MibTableColumn
mpAtmCCAtmMultiConfRootOperStatus=_MpAtmCCAtmMultiConfRootOperStatus_Object((1,3,6,1,4,1,119,2,3,3,13,110,12,3,1,8),_MpAtmCCAtmMultiConfRootOperStatus_Type())
mpAtmCCAtmMultiConfRootOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCAtmMultiConfRootOperStatus.setStatus(_A)
class _MpAtmCCAtmMultiConfLeafAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_MpAtmCCAtmMultiConfLeafAdminStatus_Type.__name__=_C
_MpAtmCCAtmMultiConfLeafAdminStatus_Object=MibTableColumn
mpAtmCCAtmMultiConfLeafAdminStatus=_MpAtmCCAtmMultiConfLeafAdminStatus_Object((1,3,6,1,4,1,119,2,3,3,13,110,12,3,1,9),_MpAtmCCAtmMultiConfLeafAdminStatus_Type())
mpAtmCCAtmMultiConfLeafAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCAtmMultiConfLeafAdminStatus.setStatus(_A)
class _MpAtmCCAtmMultiConfLeafOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_MpAtmCCAtmMultiConfLeafOperStatus_Type.__name__=_C
_MpAtmCCAtmMultiConfLeafOperStatus_Object=MibTableColumn
mpAtmCCAtmMultiConfLeafOperStatus=_MpAtmCCAtmMultiConfLeafOperStatus_Object((1,3,6,1,4,1,119,2,3,3,13,110,12,3,1,10),_MpAtmCCAtmMultiConfLeafOperStatus_Type())
mpAtmCCAtmMultiConfLeafOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCAtmMultiConfLeafOperStatus.setStatus(_A)
_MpAtmCCAtmMultiConfTrafficDescrIndex_Type=AtmTrafficDescrParamIndex
_MpAtmCCAtmMultiConfTrafficDescrIndex_Object=MibTableColumn
mpAtmCCAtmMultiConfTrafficDescrIndex=_MpAtmCCAtmMultiConfTrafficDescrIndex_Object((1,3,6,1,4,1,119,2,3,3,13,110,12,3,1,11),_MpAtmCCAtmMultiConfTrafficDescrIndex_Type())
mpAtmCCAtmMultiConfTrafficDescrIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCAtmMultiConfTrafficDescrIndex.setStatus(_A)
_MpAtmCCAtmMultiConfSlotNumber_Type=Integer32
_MpAtmCCAtmMultiConfSlotNumber_Object=MibTableColumn
mpAtmCCAtmMultiConfSlotNumber=_MpAtmCCAtmMultiConfSlotNumber_Object((1,3,6,1,4,1,119,2,3,3,13,110,12,3,1,12),_MpAtmCCAtmMultiConfSlotNumber_Type())
mpAtmCCAtmMultiConfSlotNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCAtmMultiConfSlotNumber.setStatus(_A)
class _MpAtmCCAtmMultiConfVcRdiResponse_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),(_O,2)))
_MpAtmCCAtmMultiConfVcRdiResponse_Type.__name__=_C
_MpAtmCCAtmMultiConfVcRdiResponse_Object=MibTableColumn
mpAtmCCAtmMultiConfVcRdiResponse=_MpAtmCCAtmMultiConfVcRdiResponse_Object((1,3,6,1,4,1,119,2,3,3,13,110,12,3,1,13),_MpAtmCCAtmMultiConfVcRdiResponse_Type())
mpAtmCCAtmMultiConfVcRdiResponse.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCAtmMultiConfVcRdiResponse.setStatus(_A)
_MpAtmCCAtmMultiConfPvcId_Type=Integer32
_MpAtmCCAtmMultiConfPvcId_Object=MibTableColumn
mpAtmCCAtmMultiConfPvcId=_MpAtmCCAtmMultiConfPvcId_Object((1,3,6,1,4,1,119,2,3,3,13,110,12,3,1,14),_MpAtmCCAtmMultiConfPvcId_Type())
mpAtmCCAtmMultiConfPvcId.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCAtmMultiConfPvcId.setStatus(_A)
_MpAtmCCAtmMultiConfSeqNo_Type=Integer32
_MpAtmCCAtmMultiConfSeqNo_Object=MibTableColumn
mpAtmCCAtmMultiConfSeqNo=_MpAtmCCAtmMultiConfSeqNo_Object((1,3,6,1,4,1,119,2,3,3,13,110,12,3,1,15),_MpAtmCCAtmMultiConfSeqNo_Type())
mpAtmCCAtmMultiConfSeqNo.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCAtmMultiConfSeqNo.setStatus(_A)
_MpAtmCCAtmMultiConfShaperRate_Type=Integer32
_MpAtmCCAtmMultiConfShaperRate_Object=MibTableColumn
mpAtmCCAtmMultiConfShaperRate=_MpAtmCCAtmMultiConfShaperRate_Object((1,3,6,1,4,1,119,2,3,3,13,110,12,3,1,16),_MpAtmCCAtmMultiConfShaperRate_Type())
mpAtmCCAtmMultiConfShaperRate.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCAtmMultiConfShaperRate.setStatus(_A)
class _MpAtmCCAtmMultiConfRootVpTunneling_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_O,2)))
_MpAtmCCAtmMultiConfRootVpTunneling_Type.__name__=_C
_MpAtmCCAtmMultiConfRootVpTunneling_Object=MibTableColumn
mpAtmCCAtmMultiConfRootVpTunneling=_MpAtmCCAtmMultiConfRootVpTunneling_Object((1,3,6,1,4,1,119,2,3,3,13,110,12,3,1,17),_MpAtmCCAtmMultiConfRootVpTunneling_Type())
mpAtmCCAtmMultiConfRootVpTunneling.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCAtmMultiConfRootVpTunneling.setStatus(_A)
class _MpAtmCCAtmMultiConfLeafVpTunneling_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_O,2)))
_MpAtmCCAtmMultiConfLeafVpTunneling_Type.__name__=_C
_MpAtmCCAtmMultiConfLeafVpTunneling_Object=MibTableColumn
mpAtmCCAtmMultiConfLeafVpTunneling=_MpAtmCCAtmMultiConfLeafVpTunneling_Object((1,3,6,1,4,1,119,2,3,3,13,110,12,3,1,18),_MpAtmCCAtmMultiConfLeafVpTunneling_Type())
mpAtmCCAtmMultiConfLeafVpTunneling.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCAtmMultiConfLeafVpTunneling.setStatus(_A)
class _MpAtmCCAtmMultiConfNextLeaf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_O,2)))
_MpAtmCCAtmMultiConfNextLeaf_Type.__name__=_C
_MpAtmCCAtmMultiConfNextLeaf_Object=MibTableColumn
mpAtmCCAtmMultiConfNextLeaf=_MpAtmCCAtmMultiConfNextLeaf_Object((1,3,6,1,4,1,119,2,3,3,13,110,12,3,1,19),_MpAtmCCAtmMultiConfNextLeaf_Type())
mpAtmCCAtmMultiConfNextLeaf.setMaxAccess(_B)
if mibBuilder.loadTexts:mpAtmCCAtmMultiConfNextLeaf.setStatus(_A)
_MpCes_ObjectIdentity=ObjectIdentity
mpCes=_MpCes_ObjectIdentity((1,3,6,1,4,1,119,2,3,3,13,111))
_MpIpsw_ObjectIdentity=ObjectIdentity
mpIpsw=_MpIpsw_ObjectIdentity((1,3,6,1,4,1,119,2,3,3,13,112))
_MpInsCtl_ObjectIdentity=ObjectIdentity
mpInsCtl=_MpInsCtl_ObjectIdentity((1,3,6,1,4,1,119,2,3,3,13,113))
_MpFfr_ObjectIdentity=ObjectIdentity
mpFfr=_MpFfr_ObjectIdentity((1,3,6,1,4,1,119,2,3,3,13,114))
mibBuilder.exportSymbols(_E,**{'RowStatus':RowStatus,'NetPrefix':NetPrefix,_U:DisplayString,'DateAndTime':DateAndTime,'MacAddress':MacAddress,_e:PhysAddress,'AtmAddr':AtmAddr,'MpAtmCCCladType':MpAtmCCCladType,'org':org,'dod':dod,'internet':internet,'private':private,'enterprises':enterprises,'nec':nec,'necProduct':necProduct,'datax':datax,'mmpf':mmpf,'mmn9110':mmn9110,'mmn9120':mmn9120,'nec-mib':nec_mib,'necProductDepend':necProductDepend,'datax-mib':datax_mib,'mmpf-mib':mmpf_mib,'mpSystem':mpSystem,'mpIfCard':mpIfCard,'mpEtherPort':mpEtherPort,'mpVlan':mpVlan,'mpBridge':mpBridge,'mpDbAccess':mpDbAccess,'mpEventLog':mpEventLog,'mpUiSession':mpUiSession,'mpFtp':mpFtp,'mpDhcp':mpDhcp,'mpIp':mpIp,'mpRip':mpRip,'mpSnmp':mpSnmp,'mpStats':mpStats,'mpCli':mpCli,'mpAtm':mpAtm,'mpLis':mpLis,'mpDns':mpDns,'mpLec':mpLec,'mpMpc':mpMpc,'mpStp':mpStp,'mpLlc':mpLlc,'mpOspf':mpOspf,'mpObsCtl':mpObsCtl,'mpCardInfo':mpCardInfo,'mpInterface':mpInterface,'mpPvoice':mpPvoice,'mpAtmCallCtl':mpAtmCallCtl,'mpAtmCCBaseGroup':mpAtmCCBaseGroup,'mpAtmCCNextTrafficDescrIndex':mpAtmCCNextTrafficDescrIndex,'mpAtmCCNextNodeVci':mpAtmCCNextNodeVci,'mpAtmCCStaticPVPC':mpAtmCCStaticPVPC,'mpAtmCCStaticPvpTable':mpAtmCCStaticPvpTable,'mpAtmCCStaticPvpEntry':mpAtmCCStaticPvpEntry,_f:mpAtmCCStaticPvpIndex,_g:mpAtmCCStaticPvpLowIfIndex,_h:mpAtmCCStaticPvpLowVpi,_i:mpAtmCCStaticPvpHighIfIndex,_j:mpAtmCCStaticPvpHighVpi,'mpAtmCCStaticPvpLowReceiveTrafficDescrIndex':mpAtmCCStaticPvpLowReceiveTrafficDescrIndex,'mpAtmCCStaticPvpLowTransmitTrafficDescrIndex':mpAtmCCStaticPvpLowTransmitTrafficDescrIndex,'mpAtmCCStaticPvpHighReceiveTrafficDescrIndex':mpAtmCCStaticPvpHighReceiveTrafficDescrIndex,'mpAtmCCStaticPvpHighTransmitTrafficDescrIndex':mpAtmCCStaticPvpHighTransmitTrafficDescrIndex,'mpAtmCCStaticPvpPriority':mpAtmCCStaticPvpPriority,'mpAtmCCStaticPvpLowCladType':mpAtmCCStaticPvpLowCladType,'mpAtmCCStaticPvpHighCladType':mpAtmCCStaticPvpHighCladType,'mpAtmCCStaticPvpAdminStatus':mpAtmCCStaticPvpAdminStatus,'mpAtmCCStaticPvpOperStatus':mpAtmCCStaticPvpOperStatus,'mpAtmCCStaticPvpPvpId':mpAtmCCStaticPvpPvpId,'mpAtmCCStaticPvpSeqNo':mpAtmCCStaticPvpSeqNo,'mpAtmCCStaticPvpPgcRequest':mpAtmCCStaticPvpPgcRequest,'mpAtmCCStaticPvpCfgStatus':mpAtmCCStaticPvpCfgStatus,'mpAtmCCStaticPvpErrInfo':mpAtmCCStaticPvpErrInfo,'mpAtmCCStaticPvcTable':mpAtmCCStaticPvcTable,'mpAtmCCStaticPvcEntry':mpAtmCCStaticPvcEntry,_k:mpAtmCCStaticPvcIndex,_l:mpAtmCCStaticPvcLowIfIndex,_m:mpAtmCCStaticPvcLowVpi,_n:mpAtmCCStaticPvcLowVci,_o:mpAtmCCStaticPvcHighIfIndex,_p:mpAtmCCStaticPvcHighVpi,_q:mpAtmCCStaticPvcHighVci,'mpAtmCCStaticPvcLowReceiveTrafficDescrIndex':mpAtmCCStaticPvcLowReceiveTrafficDescrIndex,'mpAtmCCStaticPvcLowTransmitTrafficDescrIndex':mpAtmCCStaticPvcLowTransmitTrafficDescrIndex,'mpAtmCCStaticPvcHighReceiveTrafficDescrIndex':mpAtmCCStaticPvcHighReceiveTrafficDescrIndex,'mpAtmCCStaticPvcHighTransmitTrafficDescrIndex':mpAtmCCStaticPvcHighTransmitTrafficDescrIndex,'mpAtmCCStaticPvcPriority':mpAtmCCStaticPvcPriority,'mpAtmCCStaticPvcLowCladType':mpAtmCCStaticPvcLowCladType,'mpAtmCCStaticPvcHighCladType':mpAtmCCStaticPvcHighCladType,'mpAtmCCStaticPvcAdminStatus':mpAtmCCStaticPvcAdminStatus,'mpAtmCCStaticPvcOperStatus':mpAtmCCStaticPvcOperStatus,'mpAtmCCStaticPvcPvcId':mpAtmCCStaticPvcPvcId,'mpAtmCCStaticPvcSeqNo':mpAtmCCStaticPvcSeqNo,'mpAtmCCStaticPvcPgcRequest':mpAtmCCStaticPvcPgcRequest,'mpAtmCCStaticPvcCfgStatus':mpAtmCCStaticPvcCfgStatus,'mpAtmCCStaticPvcErrInfo':mpAtmCCStaticPvcErrInfo,'mpAtmCCSoftPVPC':mpAtmCCSoftPVPC,'mpAtmCCSoftPvpTable':mpAtmCCSoftPvpTable,'mpAtmCCSoftPvpEntry':mpAtmCCSoftPvpEntry,_r:mpAtmCCSoftPvpLeafReference,_s:mpAtmCCSoftPvpIfIndex,_t:mpAtmCCSoftPvpVpi,'mpAtmCCSoftPvpReceiveTrafficDescrIndex':mpAtmCCSoftPvpReceiveTrafficDescrIndex,'mpAtmCCSoftPvpTransmitTrafficDescrIndex':mpAtmCCSoftPvpTransmitTrafficDescrIndex,'mpAtmCCSoftPvpTargetAddress':mpAtmCCSoftPvpTargetAddress,'mpAtmCCSoftPvpTargetVpi':mpAtmCCSoftPvpTargetVpi,'mpAtmCCSoftPvpLastReleaseCause':mpAtmCCSoftPvpLastReleaseCause,'mpAtmCCSoftPvpLastReleaseDiagnostic':mpAtmCCSoftPvpLastReleaseDiagnostic,'mpAtmCCSoftPvpPriority':mpAtmCCSoftPvpPriority,'mpAtmCCSoftPvpCladType':mpAtmCCSoftPvpCladType,'mpAtmCCSoftPvpOriginalAddress':mpAtmCCSoftPvpOriginalAddress,'mpAtmCCSoftPvpAdminStatus':mpAtmCCSoftPvpAdminStatus,'mpAtmCCSoftPvpOperStatus':mpAtmCCSoftPvpOperStatus,'mpAtmCCSoftPvpPgcRequest':mpAtmCCSoftPvpPgcRequest,'mpAtmCCSoftPvpCfgStatus':mpAtmCCSoftPvpCfgStatus,'mpAtmCCSoftPvpErrInfo':mpAtmCCSoftPvpErrInfo,'mpAtmCCSoftPvcTable':mpAtmCCSoftPvcTable,'mpAtmCCSoftPvcEntry':mpAtmCCSoftPvcEntry,_u:mpAtmCCSoftPvcLeafReference,_v:mpAtmCCSoftPvcIfIndex,_w:mpAtmCCSoftPvcVpi,_x:mpAtmCCSoftPvcVci,'mpAtmCCSoftPvcReceiveTrafficDescrIndex':mpAtmCCSoftPvcReceiveTrafficDescrIndex,'mpAtmCCSoftPvcTransmitTrafficDescrIndex':mpAtmCCSoftPvcTransmitTrafficDescrIndex,'mpAtmCCSoftPvcTargetAddress':mpAtmCCSoftPvcTargetAddress,'mpAtmCCSoftPvcTargetVpi':mpAtmCCSoftPvcTargetVpi,'mpAtmCCSoftPvcTargetVci':mpAtmCCSoftPvcTargetVci,'mpAtmCCSoftPvcLastReleaseCause':mpAtmCCSoftPvcLastReleaseCause,'mpAtmCCSoftPvcLastReleaseDiagnostic':mpAtmCCSoftPvcLastReleaseDiagnostic,'mpAtmCCSoftPvcPriority':mpAtmCCSoftPvcPriority,'mpAtmCCSoftPvcCladType':mpAtmCCSoftPvcCladType,'mpAtmCCSoftPvcOriginalAddress':mpAtmCCSoftPvcOriginalAddress,'mpAtmCCSoftPvcAdminStatus':mpAtmCCSoftPvcAdminStatus,'mpAtmCCSoftPvcOperStatus':mpAtmCCSoftPvcOperStatus,'mpAtmCCSoftPvcPgcRequest':mpAtmCCSoftPvcPgcRequest,'mpAtmCCSoftPvcCfgStatus':mpAtmCCSoftPvcCfgStatus,'mpAtmCCSoftPvcErrInfo':mpAtmCCSoftPvcErrInfo,'mpAtmCCSoftPvpCalledTable':mpAtmCCSoftPvpCalledTable,'mpAtmCCSoftPvpCalledEntry':mpAtmCCSoftPvpCalledEntry,_y:mpAtmCCSoftPvpCalledLeafReference,_z:mpAtmCCSoftPvpCalledIfIndex,_A0:mpAtmCCSoftPvpCalledVpi,'mpAtmCCSoftPvpCalledReceiveTrafficDescrIndex':mpAtmCCSoftPvpCalledReceiveTrafficDescrIndex,'mpAtmCCSoftPvpCalledTransmitTrafficDescrIndex':mpAtmCCSoftPvpCalledTransmitTrafficDescrIndex,'mpAtmCCSoftPvpCalledTargetAddress':mpAtmCCSoftPvpCalledTargetAddress,'mpAtmCCSoftPvpCalledTargetVpi':mpAtmCCSoftPvpCalledTargetVpi,'mpAtmCCSoftPvpCalledLastReleaseCause':mpAtmCCSoftPvpCalledLastReleaseCause,'mpAtmCCSoftPvpCalledLastReleaseDiagnostic':mpAtmCCSoftPvpCalledLastReleaseDiagnostic,'mpAtmCCSoftPvpCalledPriority':mpAtmCCSoftPvpCalledPriority,'mpAtmCCSoftPvpCalledCladType':mpAtmCCSoftPvpCalledCladType,'mpAtmCCSoftPvpCalledOriginalAddress':mpAtmCCSoftPvpCalledOriginalAddress,'mpAtmCCSoftPvpCalledAdminStatus':mpAtmCCSoftPvpCalledAdminStatus,'mpAtmCCSoftPvpCalledOperStatus':mpAtmCCSoftPvpCalledOperStatus,'mpAtmCCSoftPvpCalledPgcRequest':mpAtmCCSoftPvpCalledPgcRequest,'mpAtmCCSoftPvpCalledCfgStatus':mpAtmCCSoftPvpCalledCfgStatus,'mpAtmCCSoftPvpCalledErrInfo':mpAtmCCSoftPvpCalledErrInfo,'mpAtmCCSoftPvcCalledTable':mpAtmCCSoftPvcCalledTable,'mpAtmCCSoftPvcCalledEntry':mpAtmCCSoftPvcCalledEntry,_A1:mpAtmCCSoftPvcCalledLeafReference,_A2:mpAtmCCSoftPvcCalledIfIndex,_A3:mpAtmCCSoftPvcCalledVpi,_A4:mpAtmCCSoftPvcCalledVci,'mpAtmCCSoftPvcCalledReceiveTrafficDescrIndex':mpAtmCCSoftPvcCalledReceiveTrafficDescrIndex,'mpAtmCCSoftPvcCalledTransmitTrafficDescrIndex':mpAtmCCSoftPvcCalledTransmitTrafficDescrIndex,'mpAtmCCSoftPvcCalledTargetAddress':mpAtmCCSoftPvcCalledTargetAddress,'mpAtmCCSoftPvcCalledTargetVpi':mpAtmCCSoftPvcCalledTargetVpi,'mpAtmCCSoftPvcCalledTargetVci':mpAtmCCSoftPvcCalledTargetVci,'mpAtmCCSoftPvcCalledLastReleaseCause':mpAtmCCSoftPvcCalledLastReleaseCause,'mpAtmCCSoftPvcCalledLastReleaseDiagnostic':mpAtmCCSoftPvcCalledLastReleaseDiagnostic,'mpAtmCCSoftPvcCalledPriority':mpAtmCCSoftPvcCalledPriority,'mpAtmCCSoftPvcCalledCladType':mpAtmCCSoftPvcCalledCladType,'mpAtmCCSoftPvcCalledOriginalAddress':mpAtmCCSoftPvcCalledOriginalAddress,'mpAtmCCSoftPvcCalledAdminStatus':mpAtmCCSoftPvcCalledAdminStatus,'mpAtmCCSoftPvcCalledOperStatus':mpAtmCCSoftPvcCalledOperStatus,'mpAtmCCSoftPvcCalledPgcRequest':mpAtmCCSoftPvcCalledPgcRequest,'mpAtmCCSoftPvcCalledCfgStatus':mpAtmCCSoftPvcCalledCfgStatus,'mpAtmCCSoftPvcCalledErrInfo':mpAtmCCSoftPvcCalledErrInfo,'mpAtmCCStatistics':mpAtmCCStatistics,'mpAtmCCVpStatisticsTable':mpAtmCCVpStatisticsTable,'mpAtmCCVpStatisticsEntry':mpAtmCCVpStatisticsEntry,_A5:mpAtmCCVpStatVpi,'mpAtmCCVpStatInCells':mpAtmCCVpStatInCells,'mpAtmCCVpStatInCellsCounters':mpAtmCCVpStatInCellsCounters,'mpAtmCCVpStatOutCells':mpAtmCCVpStatOutCells,'mpAtmCCVpStatOutCellsCounters':mpAtmCCVpStatOutCellsCounters,'mpAtmCCVpStatInDropCells':mpAtmCCVpStatInDropCells,'mpAtmCCVpStatInDropCellsCounters':mpAtmCCVpStatInDropCellsCounters,'mpAtmCCVcStatisticsTable':mpAtmCCVcStatisticsTable,'mpAtmCCVcStatisticsEntry':mpAtmCCVcStatisticsEntry,_A6:mpAtmCCVcStatVpi,_A7:mpAtmCCVcStatVci,'mpAtmCCVcStatInCells':mpAtmCCVcStatInCells,'mpAtmCCVcStatInCellsCounters':mpAtmCCVcStatInCellsCounters,'mpAtmCCVcStatOutCells':mpAtmCCVcStatOutCells,'mpAtmCCVcStatOutCellsCounters':mpAtmCCVcStatOutCellsCounters,'mpAtmCCVcStatInDropCells':mpAtmCCVcStatInDropCells,'mpAtmCCVcStatInDropCellsCounters':mpAtmCCVcStatInDropCellsCounters,'mpAtmCCOuspStatisticsTable':mpAtmCCOuspStatisticsTable,'mpAtmCCOuspStatisticsEntry':mpAtmCCOuspStatisticsEntry,_A8:mpAtmCCOuspStatIndex,'mpAtmCCOuspStatRcvCrcErrCellsCounters':mpAtmCCOuspStatRcvCrcErrCellsCounters,'mpAtmCCOuspStatSendOfifoFullCounters':mpAtmCCOuspStatSendOfifoFullCounters,'mpAtmCCOuspStatRcvBufOverCounters':mpAtmCCOuspStatRcvBufOverCounters,'mpAtmCCOuspStatRcvUnknownCellsCounters':mpAtmCCOuspStatRcvUnknownCellsCounters,'mpAtmCCOuspStatRcvInvalidCellsCounters':mpAtmCCOuspStatRcvInvalidCellsCounters,'mpAtmCCOuspStatSendScheduleErrorCounters':mpAtmCCOuspStatSendScheduleErrorCounters,'mpAtmCCOuspStatRcvScheduleErrorCounters':mpAtmCCOuspStatRcvScheduleErrorCounters,'mpAtmCCOuspStatSendInvalidCdvCounters':mpAtmCCOuspStatSendInvalidCdvCounters,'mpAtmCCPhyStatisticsTable':mpAtmCCPhyStatisticsTable,'mpAtmCCPhyStatisticsEntry':mpAtmCCPhyStatisticsEntry,'mpAtmCCPhyStatTmtCellsCounters':mpAtmCCPhyStatTmtCellsCounters,'mpAtmCCPhyStatRcvCellsCounters':mpAtmCCPhyStatRcvCellsCounters,'mpAtmCCPhyStatCorrectHecErrCounters':mpAtmCCPhyStatCorrectHecErrCounters,'mpAtmCCPhyStatUncorrectHecErrCounters':mpAtmCCPhyStatUncorrectHecErrCounters,'mpAtmCCPhyStatB1ErrCounters':mpAtmCCPhyStatB1ErrCounters,'mpAtmCCPhyStatB2ErrCounters':mpAtmCCPhyStatB2ErrCounters,'mpAtmCCPhyStatB3ErrCounters':mpAtmCCPhyStatB3ErrCounters,'mpAtmCCPhyStatFebeCounters':mpAtmCCPhyStatFebeCounters,'mpAtmCCPhyStatSymbolErrCounters':mpAtmCCPhyStatSymbolErrCounters,'mpAtmCCPhyStatParityErrCounters':mpAtmCCPhyStatParityErrCounters,'mpAtmCCPortAlarmStatisticsTable':mpAtmCCPortAlarmStatisticsTable,'mpAtmCCPortAlarmStatisticsEntry':mpAtmCCPortAlarmStatisticsEntry,'mpAtmCCPortAlarmStatRedLosCounters':mpAtmCCPortAlarmStatRedLosCounters,'mpAtmCCPortAlarmStatRedLofCounters':mpAtmCCPortAlarmStatRedLofCounters,'mpAtmCCPortAlarmStatRedMsAisCounters':mpAtmCCPortAlarmStatRedMsAisCounters,'mpAtmCCPortAlarmStatRedLopCounters':mpAtmCCPortAlarmStatRedLopCounters,'mpAtmCCPortAlarmStatRedPAisCounters':mpAtmCCPortAlarmStatRedPAisCounters,'mpAtmCCPortAlarmStatRedLocCounters':mpAtmCCPortAlarmStatRedLocCounters,'mpAtmCCPortAlarmStatRedResetCounters':mpAtmCCPortAlarmStatRedResetCounters,'mpAtmCCPortAlarmStatRedCcRedCounters':mpAtmCCPortAlarmStatRedCcRedCounters,'mpAtmCCPortAlarmStatRedOofCounters':mpAtmCCPortAlarmStatRedOofCounters,'mpAtmCCPortAlarmStatRedAisCounters':mpAtmCCPortAlarmStatRedAisCounters,'mpAtmCCPortAlarmStatRedPOofCounters':mpAtmCCPortAlarmStatRedPOofCounters,'mpAtmCCPortAlarmStatRedBadSigCounters':mpAtmCCPortAlarmStatRedBadSigCounters,'mpAtmCCPortAlarmStatRedLcdCounters':mpAtmCCPortAlarmStatRedLcdCounters,'mpAtmCCPortAlarmStatRedLinkAisCounters':mpAtmCCPortAlarmStatRedLinkAisCounters,'mpAtmCCPortAlarmStatRedInfo0Counters':mpAtmCCPortAlarmStatRedInfo0Counters,'mpAtmCCPortAlarmStatYelMsRdiCounters':mpAtmCCPortAlarmStatYelMsRdiCounters,'mpAtmCCPortAlarmStatYelPRdiCounters':mpAtmCCPortAlarmStatYelPRdiCounters,'mpAtmCCPortAlarmStatYelCcYelCounters':mpAtmCCPortAlarmStatYelCcYelCounters,'mpAtmCCPortAlarmStatYelRaiCounters':mpAtmCCPortAlarmStatYelRaiCounters,'mpAtmCCPortAlarmStatYelPRaiCounters':mpAtmCCPortAlarmStatYelPRaiCounters,'mpAtmCCPortAlarmStatYelInfo2Counters':mpAtmCCPortAlarmStatYelInfo2Counters,'mpAtmCCVpTunnellingStatisticsTable':mpAtmCCVpTunnellingStatisticsTable,'mpAtmCCVpTunnellingStatisticsEntry':mpAtmCCVpTunnellingStatisticsEntry,'mpAtmCCVpTunStatTmtCellsCounters':mpAtmCCVpTunStatTmtCellsCounters,'mpAtmCCVpTunStatRcvCellsCounters':mpAtmCCVpTunStatRcvCellsCounters,'mpAtmCCVccStatisticsRegTable':mpAtmCCVccStatisticsRegTable,'mpAtmCCVccStatisticsRegEntry':mpAtmCCVccStatisticsRegEntry,_A9:mpAtmCCVccStatRegVpi,_AA:mpAtmCCVccStatRegVci,'mpAtmCCVccStatRegInCellsCounters':mpAtmCCVccStatRegInCellsCounters,'mpAtmCCVccStatRegOutCellsCounters':mpAtmCCVccStatRegOutCellsCounters,'mpAtmCCVccStatRegStatus':mpAtmCCVccStatRegStatus,'mpAtmCCVccStatRegErrInfo':mpAtmCCVccStatRegErrInfo,'mpAtmCCResourceControl':mpAtmCCResourceControl,'mpAtmCCPortResourceInfomationTable':mpAtmCCPortResourceInfomationTable,'mpAtmCCPortResourceInfomationEntry':mpAtmCCPortResourceInfomationEntry,'mpAtmCCPortResInfoPortSpeed':mpAtmCCPortResInfoPortSpeed,'mpAtmCCPortResInfoMaxVpiBits':mpAtmCCPortResInfoMaxVpiBits,'mpAtmCCPortResInfoMaxVciBits':mpAtmCCPortResInfoMaxVciBits,'mpAtmCCPortResInfoMaxVPC':mpAtmCCPortResInfoMaxVPC,'mpAtmCCPortResInfoMaxVCC':mpAtmCCPortResInfoMaxVCC,'mpAtmCCPortResInfoMaxSvpcVpi':mpAtmCCPortResInfoMaxSvpcVpi,'mpAtmCCPortResInfoMaxSvccVpi':mpAtmCCPortResInfoMaxSvccVpi,'mpAtmCCPortResInfoMinSvccVci':mpAtmCCPortResInfoMinSvccVci,'mpAtmCCPortResInfoShaperKind':mpAtmCCPortResInfoShaperKind,'mpAtmCCPortResInfoVpTunnellingConfig':mpAtmCCPortResInfoVpTunnellingConfig,'mpAtmCCPortResInfoSvccVciHuntWay':mpAtmCCPortResInfoSvccVciHuntWay,'mpAtmCCPortResInfoVpiCounters':mpAtmCCPortResInfoVpiCounters,'mpAtmCCPortResInfoVpcCounters':mpAtmCCPortResInfoVpcCounters,'mpAtmCCPortResInfoVccCounters':mpAtmCCPortResInfoVccCounters,'mpAtmCCPortBandwidthInfomationTable':mpAtmCCPortBandwidthInfomationTable,'mpAtmCCPortBandwidthInfomationEntry':mpAtmCCPortBandwidthInfomationEntry,_AB:mpAtmCCPortBwInfoVpi,'mpAtmCCPortBwInfoRawBandwidthBps':mpAtmCCPortBwInfoRawBandwidthBps,'mpAtmCCPortBwInfoRawBandwidthCps':mpAtmCCPortBwInfoRawBandwidthCps,'mpAtmCCPortBwInfoTmitUsedBwCps':mpAtmCCPortBwInfoTmitUsedBwCps,'mpAtmCCPortBwInfoRcvUsedBwCps':mpAtmCCPortBwInfoRcvUsedBwCps,'mpAtmCCPortBwInfoVciCounters':mpAtmCCPortBwInfoVciCounters,'mpAtmCCBwInfoPortTable':mpAtmCCBwInfoPortTable,'mpAtmCCBwInfoPortEntry':mpAtmCCBwInfoPortEntry,'mpAtmCCBwInfoPortRawBandwidthBps':mpAtmCCBwInfoPortRawBandwidthBps,'mpAtmCCBwInfoPortRawBandwidthCps':mpAtmCCBwInfoPortRawBandwidthCps,'mpAtmCCBwInfoPortTmitUsedBwCps':mpAtmCCBwInfoPortTmitUsedBwCps,'mpAtmCCBwInfoPortRcvUsedBwCps':mpAtmCCBwInfoPortRcvUsedBwCps,'mpAtmCCBwInfoPortTmitRemainBwCps':mpAtmCCBwInfoPortTmitRemainBwCps,'mpAtmCCBwInfoPortRcvRemainBwCps':mpAtmCCBwInfoPortRcvRemainBwCps,'mpAtmCCBwInfoPortVpTunneling':mpAtmCCBwInfoPortVpTunneling,'mpAtmCCProtocol':mpAtmCCProtocol,'mpAtmCCSscopTable':mpAtmCCSscopTable,'mpAtmCCSscopEntry':mpAtmCCSscopEntry,'mpAtmCCSscopTimerPoll':mpAtmCCSscopTimerPoll,'mpAtmCCSscopTimerNoResponce':mpAtmCCSscopTimerNoResponce,'mpAtmCCSscopTimerKeepAlive':mpAtmCCSscopTimerKeepAlive,'mpAtmCCSscopTimerIdle':mpAtmCCSscopTimerIdle,'mpAtmCCSscopTimerCc':mpAtmCCSscopTimerCc,'mpAtmCCSscopMaxCc':mpAtmCCSscopMaxCc,'mpAtmCCSscopMaxPd':mpAtmCCSscopMaxPd,'mpAtmCCSscopMaxStat':mpAtmCCSscopMaxStat,'mpAtmCCSscopClearBuffs':mpAtmCCSscopClearBuffs,'mpAtmCCSscopCredit':mpAtmCCSscopCredit,'mpAtmCCIlmiTable':mpAtmCCIlmiTable,'mpAtmCCIlmiEntry':mpAtmCCIlmiEntry,'mpAtmCCIlmiConfigStatus':mpAtmCCIlmiConfigStatus,'mpAtmCClmiMaxTransmissions':mpAtmCClmiMaxTransmissions,'mpAtmCCIlmiRetransmitInterval':mpAtmCCIlmiRetransmitInterval,'mpAtmCCSignallingTable':mpAtmCCSignallingTable,'mpAtmCCSignallingEntry':mpAtmCCSignallingEntry,'mpAtmCCSignallingT301':mpAtmCCSignallingT301,'mpAtmCCSignallingT303':mpAtmCCSignallingT303,'mpAtmCCSignallingT308':mpAtmCCSignallingT308,'mpAtmCCSignallingT309':mpAtmCCSignallingT309,'mpAtmCCSignallingT310':mpAtmCCSignallingT310,'mpAtmCCSignallingT313':mpAtmCCSignallingT313,'mpAtmCCSignallingT316':mpAtmCCSignallingT316,'mpAtmCCSignallingT317':mpAtmCCSignallingT317,'mpAtmCCSignallingT322':mpAtmCCSignallingT322,'mpAtmCCSignallingT331':mpAtmCCSignallingT331,'mpAtmCCSignallingT397':mpAtmCCSignallingT397,'mpAtmCCSignallingT398':mpAtmCCSignallingT398,'mpAtmCCSignallingT399':mpAtmCCSignallingT399,'mpAtmCCProtocolTrapInfoTable':mpAtmCCProtocolTrapInfoTable,'mpAtmCCProtocolTrapInfoEntry':mpAtmCCProtocolTrapInfoEntry,_AC:mpAtmCCProtocolTrapInfoIndex,'mpAtmCCProtocolTrapInfoCause':mpAtmCCProtocolTrapInfoCause,'mpAtmCCPathTrace':mpAtmCCPathTrace,'mpAtmCCVccStatusTable':mpAtmCCVccStatusTable,'mpAtmCCVccStatusEntry':mpAtmCCVccStatusEntry,_AD:mpAtmCCVccStatusOrgPort,_AE:mpAtmCCVccStatusOrgVpi,_AF:mpAtmCCVccStatusOrgVci,'mpAtmCCVccStatusDestPort':mpAtmCCVccStatusDestPort,'mpAtmCCVccStatusDestVpi':mpAtmCCVccStatusDestVpi,'mpAtmCCVccStatusDestVci':mpAtmCCVccStatusDestVci,'mpAtmCCVccStatusPathKind':mpAtmCCVccStatusPathKind,'mpAtmCCVccStatusOrgCallKind':mpAtmCCVccStatusOrgCallKind,'mpAtmCCVccStatusDestCallKind':mpAtmCCVccStatusDestCallKind,'mpAtmCCVccStatusAdminStatus':mpAtmCCVccStatusAdminStatus,'mpAtmCCVccStatusOperStatus':mpAtmCCVccStatusOperStatus,'mpAtmCCVccStatusInsStatus':mpAtmCCVccStatusInsStatus,'mpAtmCCVccStatusOrgPortVpTunneling':mpAtmCCVccStatusOrgPortVpTunneling,'mpAtmCCVccStatusDestPortVpTunneling':mpAtmCCVccStatusDestPortVpTunneling,'mpAtmCCVccStatusConnCastType':mpAtmCCVccStatusConnCastType,'mpAtmCCPvcTraceControlTable':mpAtmCCPvcTraceControlTable,'mpAtmCCPvcTraceCtlEntry':mpAtmCCPvcTraceCtlEntry,_X:mpAtmCCPvcTraceIndex,'mpAtmCCPvcTraceCtlPathKind':mpAtmCCPvcTraceCtlPathKind,'mpAtmCCPvcTraceCtlIfIndex':mpAtmCCPvcTraceCtlIfIndex,'mpAtmCCPvcTraceCtlVpi':mpAtmCCPvcTraceCtlVpi,'mpAtmCCPvcTraceCtlVci':mpAtmCCPvcTraceCtlVci,'mpAtmCCPvcTraceCtlStatus':mpAtmCCPvcTraceCtlStatus,'mpAtmCCPvcTraceInfoTable':mpAtmCCPvcTraceInfoTable,'mpAtmCCPvcTraceInfoEntry':mpAtmCCPvcTraceInfoEntry,_AG:mpAtmCCPvcTraceEntryIndex,'mpAtmCCPvcTraceInfoSysName':mpAtmCCPvcTraceInfoSysName,'mpAtmCCPvcTraceInfoIfIndex':mpAtmCCPvcTraceInfoIfIndex,'mpAtmCCPvcTraceInfoVpi':mpAtmCCPvcTraceInfoVpi,'mpAtmCCPvcTraceInfoVci':mpAtmCCPvcTraceInfoVci,'mpAtmCCPvcTraceInfoPathKind':mpAtmCCPvcTraceInfoPathKind,'mpAtmCCPvcTraceInfoCallKind':mpAtmCCPvcTraceInfoCallKind,'mpAtmCCPvcTraceInfoLastSegment':mpAtmCCPvcTraceInfoLastSegment,'mpAtmCCMuxMib':mpAtmCCMuxMib,'mpAtmCCMuxStatistics':mpAtmCCMuxStatistics,'mpAtmCCMuxStatReceiveCellsCounters':mpAtmCCMuxStatReceiveCellsCounters,'mpAtmCCMuxStatReceiveCellsCntOvfCounters':mpAtmCCMuxStatReceiveCellsCntOvfCounters,'mpAtmCCMuxStatDiscardCellsBufOvfCounters':mpAtmCCMuxStatDiscardCellsBufOvfCounters,'mpAtmCCMuxStatDiscardCellsBufOvfCntOvfCounters':mpAtmCCMuxStatDiscardCellsBufOvfCntOvfCounters,'mpAtmCCMuxStatDiscardCellsHTErrCounters':mpAtmCCMuxStatDiscardCellsHTErrCounters,'mpAtmCCMuxStatDiscardCellsHTErrCntOvfCounters':mpAtmCCMuxStatDiscardCellsHTErrCntOvfCounters,'mpAtmCCMuxStatDiscardCellsThresholdOvfCounters':mpAtmCCMuxStatDiscardCellsThresholdOvfCounters,'mpAtmCCMuxStatDiscardCellsThresholdOvfCntOvfCounters':mpAtmCCMuxStatDiscardCellsThresholdOvfCntOvfCounters,'mpAtmCCVpTunneling':mpAtmCCVpTunneling,'mpAtmCCVpTunnelingTable':mpAtmCCVpTunnelingTable,'mpAtmCCVpTunnelingEntry':mpAtmCCVpTunnelingEntry,_AH:mpAtmCCVpTunnelingVpi,'mpAtmCCVpTunnelingAdminStatus':mpAtmCCVpTunnelingAdminStatus,'mpAtmCCVpTunnelingOperStatus':mpAtmCCVpTunnelingOperStatus,'mpAtmCCVpTunnelingSpeed':mpAtmCCVpTunnelingSpeed,'mpAtmCCVpTunnelingNeighborInfo':mpAtmCCVpTunnelingNeighborInfo,'mpAtmCCVpTunnelingPnniVer':mpAtmCCVpTunnelingPnniVer,'mpAtmCCVpTunnelingContinuityCheck':mpAtmCCVpTunnelingContinuityCheck,'mpAtmCCVpTunnelingTrapState':mpAtmCCVpTunnelingTrapState,'mpAtmCCVpTunnelingSeverity':mpAtmCCVpTunnelingSeverity,'mpAtmCCVpTunnelingCfgStatus':mpAtmCCVpTunnelingCfgStatus,'mpAtmCCVpTunnelingErrInfo':mpAtmCCVpTunnelingErrInfo,'mpAtmCCPathTest':mpAtmCCPathTest,'mpAtmCCPathTestTable':mpAtmCCPathTestTable,'mpAtmCCPathTestEntry':mpAtmCCPathTestEntry,_AI:mpAtmCCPathTestVpi,_AJ:mpAtmCCPathTestVci,'mpAtmCCPathTestStatus':mpAtmCCPathTestStatus,'mpAtmCCPathTestSendDirection':mpAtmCCPathTestSendDirection,'mpAtmCCPathTestSendTime':mpAtmCCPathTestSendTime,'mpAtmCCPathTestSendCellsCounters':mpAtmCCPathTestSendCellsCounters,'mpAtmCCPathTestRcvCellsCounters':mpAtmCCPathTestRcvCellsCounters,'mpAtmCCPathTestErrInfo':mpAtmCCPathTestErrInfo,'mpAtmCCPvcGroupCutover':mpAtmCCPvcGroupCutover,'mpAtmCCPvcGroupCutoverBaseInfo':mpAtmCCPvcGroupCutoverBaseInfo,'mpAtmCCPvcGroupCutoverEnable':mpAtmCCPvcGroupCutoverEnable,'mpAtmCCPvcGroupCutoverStatus':mpAtmCCPvcGroupCutoverStatus,'mpAtmCCUnitePvcGroup':mpAtmCCUnitePvcGroup,'mpAtmCCUpgcBaseInfo':mpAtmCCUpgcBaseInfo,'mpAtmCCUpgcTotalGroupNumber':mpAtmCCUpgcTotalGroupNumber,'mpAtmCCUpgcBaseActiveGroupNumber':mpAtmCCUpgcBaseActiveGroupNumber,'mpAtmCCUnitePvcGroupControlTable':mpAtmCCUnitePvcGroupControlTable,'mpAtmCCUpgcCtlEntry':mpAtmCCUpgcCtlEntry,_Z:mpAtmCCUpgcIndex,'mpAtmCCUpgcCtlStatus':mpAtmCCUpgcCtlStatus,'mpAtmCCUpgcCtlCountPgc':mpAtmCCUpgcCtlCountPgc,'mpAtmCCUpgcCtlResult':mpAtmCCUpgcCtlResult,'mpAtmCCUnitePvcGroupRegisterTable':mpAtmCCUnitePvcGroupRegisterTable,'mpAtmCCUpgcRegiEntry':mpAtmCCUpgcRegiEntry,_AL:mpAtmCCUpgcPgcIndex,'mpAtmCCUpgcRegiStatus':mpAtmCCUpgcRegiStatus,'mpAtmCCPvcGroup':mpAtmCCPvcGroup,'mpAtmCCPgcBaseInfo':mpAtmCCPgcBaseInfo,'mpAtmCCPgcTotalGroupNumber':mpAtmCCPgcTotalGroupNumber,'mpAtmCCPvcGroupControlTable':mpAtmCCPvcGroupControlTable,'mpAtmCCPgcCtlEntry':mpAtmCCPgcCtlEntry,_c:mpAtmCCPgcIndex,'mpAtmCCPgcCtlStatus':mpAtmCCPgcCtlStatus,'mpAtmCCPgcCtlCountPvc':mpAtmCCPgcCtlCountPvc,'mpAtmCCPgcCtlResult':mpAtmCCPgcCtlResult,'mpAtmCCPvcGroupRegisterTable':mpAtmCCPvcGroupRegisterTable,'mpAtmCCPgcRegiEntry':mpAtmCCPgcRegiEntry,_AM:mpAtmCCPgcPvcIfIndex,_AN:mpAtmCCPgcPvcVpi,_AO:mpAtmCCPgcPvcVci,'mpAtmCCPgcPvcKind':mpAtmCCPgcPvcKind,'mpAtmCCPgcStaticPvcDestIfIndex':mpAtmCCPgcStaticPvcDestIfIndex,'mpAtmCCPgcSoftPvcDestAtmAddress':mpAtmCCPgcSoftPvcDestAtmAddress,'mpAtmCCPgcPvcDestVpi':mpAtmCCPgcPvcDestVpi,'mpAtmCCPgcPvcDestVci':mpAtmCCPgcPvcDestVci,'mpAtmCCPgcPvcReceiveTrafficDescrIndex':mpAtmCCPgcPvcReceiveTrafficDescrIndex,'mpAtmCCPgcPvcTransmitTrafficDescrIndex':mpAtmCCPgcPvcTransmitTrafficDescrIndex,'mpAtmCCPgcPvcPriority':mpAtmCCPgcPvcPriority,'mpAtmCCPgcStaticPvcId':mpAtmCCPgcStaticPvcId,'mpAtmCCPgcStaticPvcSeqNo':mpAtmCCPgcStaticPvcSeqNo,'mpAtmCCPgcSoftPvcCallKind':mpAtmCCPgcSoftPvcCallKind,'mpAtmCCPgcRegiAdminStatus':mpAtmCCPgcRegiAdminStatus,'mpAtmCCPgcRegiCfgStatus':mpAtmCCPgcRegiCfgStatus,'mpAtmCCPgcRegiErrInfo':mpAtmCCPgcRegiErrInfo,'mpAtmCCPvcGroupActiveInfoTable':mpAtmCCPvcGroupActiveInfoTable,'mpAtmCCPgcActInfoEntry':mpAtmCCPgcActInfoEntry,_AP:mpAtmCCPgcActGrpNum,'mpAtmCCAtmMulticast':mpAtmCCAtmMulticast,'mpAtmCCAtmMulticastRegistration':mpAtmCCAtmMulticastRegistration,_AT:mpAtmCCAtmMultiRootIfIndex,_AU:mpAtmCCAtmMultiRootVpi,_AV:mpAtmCCAtmMultiRootVci,_AW:mpAtmCCAtmMultiLeafIfIndex,_AX:mpAtmCCAtmMultiLeafVpi,_AY:mpAtmCCAtmMultiLeafVci,'mpAtmCCAtmMultiTrafficDescrIndex':mpAtmCCAtmMultiTrafficDescrIndex,'mpAtmCCAtmMultiSlotNumber':mpAtmCCAtmMultiSlotNumber,'mpAtmCCAtmMultiVcRdiResponse':mpAtmCCAtmMultiVcRdiResponse,'mpAtmCCAtmMultiPvcId':mpAtmCCAtmMultiPvcId,'mpAtmCCAtmMultiSeqNo':mpAtmCCAtmMultiSeqNo,'mpAtmCCAtmMultiCfgStatus':mpAtmCCAtmMultiCfgStatus,'mpAtmCCAtmMultiRegErrInfo':mpAtmCCAtmMultiRegErrInfo,'mpAtmCCAtmMulticastCtlTable':mpAtmCCAtmMulticastCtlTable,'mpAtmCCAtmMultiCtlEntry':mpAtmCCAtmMultiCtlEntry,_AQ:mpAtmCCAtmMultiIfIndex,_AR:mpAtmCCAtmMultiVpi,_AS:mpAtmCCAtmMultiVci,'mpAtmCCAtmMultiAdminStatus':mpAtmCCAtmMultiAdminStatus,'mpAtmCCAtmMultiOperStatus':mpAtmCCAtmMultiOperStatus,'mpAtmCCAtmMultiErrInfo':mpAtmCCAtmMultiErrInfo,'mpAtmCCAtmMulticastConfTable':mpAtmCCAtmMulticastConfTable,'mpAtmCCAtmMultiConfEntry':mpAtmCCAtmMultiConfEntry,'mpAtmCCAtmMultiConfRootIfIndex':mpAtmCCAtmMultiConfRootIfIndex,'mpAtmCCAtmMultiConfRootVpi':mpAtmCCAtmMultiConfRootVpi,'mpAtmCCAtmMultiConfRootVci':mpAtmCCAtmMultiConfRootVci,'mpAtmCCAtmMultiConfLeafIfIndex':mpAtmCCAtmMultiConfLeafIfIndex,'mpAtmCCAtmMultiConfLeafVpi':mpAtmCCAtmMultiConfLeafVpi,'mpAtmCCAtmMultiConfLeafVci':mpAtmCCAtmMultiConfLeafVci,'mpAtmCCAtmMultiConfRootAdminStatus':mpAtmCCAtmMultiConfRootAdminStatus,'mpAtmCCAtmMultiConfRootOperStatus':mpAtmCCAtmMultiConfRootOperStatus,'mpAtmCCAtmMultiConfLeafAdminStatus':mpAtmCCAtmMultiConfLeafAdminStatus,'mpAtmCCAtmMultiConfLeafOperStatus':mpAtmCCAtmMultiConfLeafOperStatus,'mpAtmCCAtmMultiConfTrafficDescrIndex':mpAtmCCAtmMultiConfTrafficDescrIndex,'mpAtmCCAtmMultiConfSlotNumber':mpAtmCCAtmMultiConfSlotNumber,'mpAtmCCAtmMultiConfVcRdiResponse':mpAtmCCAtmMultiConfVcRdiResponse,'mpAtmCCAtmMultiConfPvcId':mpAtmCCAtmMultiConfPvcId,'mpAtmCCAtmMultiConfSeqNo':mpAtmCCAtmMultiConfSeqNo,'mpAtmCCAtmMultiConfShaperRate':mpAtmCCAtmMultiConfShaperRate,'mpAtmCCAtmMultiConfRootVpTunneling':mpAtmCCAtmMultiConfRootVpTunneling,'mpAtmCCAtmMultiConfLeafVpTunneling':mpAtmCCAtmMultiConfLeafVpTunneling,'mpAtmCCAtmMultiConfNextLeaf':mpAtmCCAtmMultiConfNextLeaf,'mpCes':mpCes,'mpIpsw':mpIpsw,'mpInsCtl':mpInsCtl,'mpFfr':mpFfr})