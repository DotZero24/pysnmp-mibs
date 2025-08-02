_AC='vpwsBindRemoteSiteID'
_AB='vpwsBindLocalSiteID'
_AA='vpwsBindCfgRemoteSiteID'
_A9='vpwsConfigIgnoreEncapsMismatch'
_A8='vpwsConfigIgnoreMtuMismatch'
_A7='vpwsConfigIncludeCSV'
_A6='vpwsConfigLabelBlockSize'
_A5='vpwsConfigLocalPreference'
_A4='vpwsConfigLocalSiteID'
_A3='vpwsConfigVpnId'
_A2='vpwsConfigRouteDistinguisher'
_A1='vpwsBindCfgLclSwitchIfIndex'
_A0='vpwsBindRemoteAddr'
_z='vpwsBindRemoteAddrType'
_y='vpwsBindRemoteRD'
_x='vpwsBindLclSwitchIfIndex'
_w='vpwsBindPwIfIndex'
_v='vpwsBindPwSetIndex'
_u='vpwsBindPwBindType'
_t='vpwsBindOperStatus'
_s='vpwsBindCfgPwBindType'
_r='vpwsBindCfgVpwsIndex'
_q='vpwsBindCfgOperStatus'
_p='vpwsBindCfgAdminStatus'
_o='vpwsBindCfgRowStatus'
_n='vpwsStatusDesignatedForwarder'
_m='vpwsStatusVcCount'
_l='vpwsStatusOperStatus'
_k='vpwsConfigSeqDelivery'
_j='vpwsConfigControlWord'
_i='vpwsConfigMtu'
_h='vpwsConfigPwEncapType'
_g='vpwsConfigSigType'
_f='vpwsConfigADType'
_e='vpwsConfigDescr'
_d='vpwsConfigName'
_c='vpwsConfigOperStatus'
_b='vpwsConfigAdminStatus'
_a='vpwsConfigRowStatus'
_Z='0000000000000000'
_Y='InterfaceIndexOrZero'
_X='IANAPwTypeTC'
_W='NumericIndexOrZero'
_V='L2vpnSigType'
_U='L2vpnPwBindType'
_T='L2vpnADType'
_S='BgpRouteDistinguisher'
_R='BgpExtendedCommunity'
_Q='vpwsBgpADGroup'
_P='vpwsDoubleSidedGroup'
_O='vpwsBindCfgPwSetIndex'
_N='ifIndex'
_M='IF-MIB'
_L='AdminStatus'
_K='L2vpnVeIdOrZero'
_J='vpwsBaseGroup'
_I='vpwsIndex'
_H='Unsigned32'
_G='l2vmEntityIndex'
_F='DC-L2VPN-MIB'
_E='TruthValue'
_D='read-only'
_C='read-create'
_B='DC-VPWS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
BgpExtendedCommunity,BgpRouteDistinguisher,L2vpnADType,L2vpnPwBindType,L2vpnSigType,L2vpnVeIdOrZero,l2vmEntityIndex=mibBuilder.importSymbols(_F,_R,_S,_T,_U,_V,_K,_G)
AdminStatus,NpgOperStatus,NumericIndex,NumericIndexOrZero=mibBuilder.importSymbols('DC-MASTER-TC',_L,'NpgOperStatus','NumericIndex',_W)
IANAPwTypeTC,=mibBuilder.importSymbols('IANA-PWE3-MIB',_X)
InterfaceIndex,InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols(_M,'InterfaceIndex',_Y,_N)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_E)
vpwsMib=ModuleIdentity((1,3,6,1,4,1,629,10,19))
_Nbase_ObjectIdentity=ObjectIdentity
nbase=_Nbase_ObjectIdentity((1,3,6,1,4,1,629))
_Opx_ObjectIdentity=ObjectIdentity
opx=_Opx_ObjectIdentity((1,3,6,1,4,1,629,10))
_VpwsObjects_ObjectIdentity=ObjectIdentity
vpwsObjects=_VpwsObjects_ObjectIdentity((1,3,6,1,4,1,629,10,19,1))
_VpwsConfigTable_Object=MibTable
vpwsConfigTable=_VpwsConfigTable_Object((1,3,6,1,4,1,629,10,19,1,1))
if mibBuilder.loadTexts:vpwsConfigTable.setStatus(_A)
_VpwsConfigEntry_Object=MibTableRow
vpwsConfigEntry=_VpwsConfigEntry_Object((1,3,6,1,4,1,629,10,19,1,1,1))
vpwsConfigEntry.setIndexNames((0,_F,_G),(0,_B,_I))
if mibBuilder.loadTexts:vpwsConfigEntry.setStatus(_A)
_VpwsIndex_Type=NumericIndex
_VpwsIndex_Object=MibTableColumn
vpwsIndex=_VpwsIndex_Object((1,3,6,1,4,1,629,10,19,1,1,1,2),_VpwsIndex_Type())
vpwsIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:vpwsIndex.setStatus(_A)
_VpwsConfigRowStatus_Type=RowStatus
_VpwsConfigRowStatus_Object=MibTableColumn
vpwsConfigRowStatus=_VpwsConfigRowStatus_Object((1,3,6,1,4,1,629,10,19,1,1,1,3),_VpwsConfigRowStatus_Type())
vpwsConfigRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwsConfigRowStatus.setStatus(_A)
class _VpwsConfigAdminStatus_Type(AdminStatus):defaultValue=1
_VpwsConfigAdminStatus_Type.__name__=_L
_VpwsConfigAdminStatus_Object=MibTableColumn
vpwsConfigAdminStatus=_VpwsConfigAdminStatus_Object((1,3,6,1,4,1,629,10,19,1,1,1,4),_VpwsConfigAdminStatus_Type())
vpwsConfigAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwsConfigAdminStatus.setStatus(_A)
_VpwsConfigOperStatus_Type=NpgOperStatus
_VpwsConfigOperStatus_Object=MibTableColumn
vpwsConfigOperStatus=_VpwsConfigOperStatus_Object((1,3,6,1,4,1,629,10,19,1,1,1,5),_VpwsConfigOperStatus_Type())
vpwsConfigOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwsConfigOperStatus.setStatus(_A)
_VpwsConfigName_Type=SnmpAdminString
_VpwsConfigName_Object=MibTableColumn
vpwsConfigName=_VpwsConfigName_Object((1,3,6,1,4,1,629,10,19,1,1,1,6),_VpwsConfigName_Type())
vpwsConfigName.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwsConfigName.setStatus(_A)
_VpwsConfigDescr_Type=SnmpAdminString
_VpwsConfigDescr_Object=MibTableColumn
vpwsConfigDescr=_VpwsConfigDescr_Object((1,3,6,1,4,1,629,10,19,1,1,1,7),_VpwsConfigDescr_Type())
vpwsConfigDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwsConfigDescr.setStatus(_A)
class _VpwsConfigADType_Type(L2vpnADType):defaultValue=1
_VpwsConfigADType_Type.__name__=_T
_VpwsConfigADType_Object=MibTableColumn
vpwsConfigADType=_VpwsConfigADType_Object((1,3,6,1,4,1,629,10,19,1,1,1,8),_VpwsConfigADType_Type())
vpwsConfigADType.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwsConfigADType.setStatus(_A)
class _VpwsConfigSigType_Type(L2vpnSigType):defaultValue=1
_VpwsConfigSigType_Type.__name__=_V
_VpwsConfigSigType_Object=MibTableColumn
vpwsConfigSigType=_VpwsConfigSigType_Object((1,3,6,1,4,1,629,10,19,1,1,1,9),_VpwsConfigSigType_Type())
vpwsConfigSigType.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwsConfigSigType.setStatus(_A)
class _VpwsConfigPwEncapType_Type(IANAPwTypeTC):defaultValue=5
_VpwsConfigPwEncapType_Type.__name__=_X
_VpwsConfigPwEncapType_Object=MibTableColumn
vpwsConfigPwEncapType=_VpwsConfigPwEncapType_Object((1,3,6,1,4,1,629,10,19,1,1,1,10),_VpwsConfigPwEncapType_Type())
vpwsConfigPwEncapType.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwsConfigPwEncapType.setStatus(_A)
class _VpwsConfigMtu_Type(Unsigned32):defaultValue=1500;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,9192))
_VpwsConfigMtu_Type.__name__=_H
_VpwsConfigMtu_Object=MibTableColumn
vpwsConfigMtu=_VpwsConfigMtu_Object((1,3,6,1,4,1,629,10,19,1,1,1,11),_VpwsConfigMtu_Type())
vpwsConfigMtu.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwsConfigMtu.setStatus(_A)
class _VpwsConfigControlWord_Type(TruthValue):defaultValue=2
_VpwsConfigControlWord_Type.__name__=_E
_VpwsConfigControlWord_Object=MibTableColumn
vpwsConfigControlWord=_VpwsConfigControlWord_Object((1,3,6,1,4,1,629,10,19,1,1,1,12),_VpwsConfigControlWord_Type())
vpwsConfigControlWord.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwsConfigControlWord.setStatus(_A)
class _VpwsConfigSeqDelivery_Type(TruthValue):defaultValue=2
_VpwsConfigSeqDelivery_Type.__name__=_E
_VpwsConfigSeqDelivery_Object=MibTableColumn
vpwsConfigSeqDelivery=_VpwsConfigSeqDelivery_Object((1,3,6,1,4,1,629,10,19,1,1,1,13),_VpwsConfigSeqDelivery_Type())
vpwsConfigSeqDelivery.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwsConfigSeqDelivery.setStatus(_A)
class _VpwsConfigRouteDistinguisher_Type(BgpRouteDistinguisher):defaultHexValue=_Z
_VpwsConfigRouteDistinguisher_Type.__name__=_S
_VpwsConfigRouteDistinguisher_Object=MibTableColumn
vpwsConfigRouteDistinguisher=_VpwsConfigRouteDistinguisher_Object((1,3,6,1,4,1,629,10,19,1,1,1,14),_VpwsConfigRouteDistinguisher_Type())
vpwsConfigRouteDistinguisher.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwsConfigRouteDistinguisher.setStatus(_A)
class _VpwsConfigVpnId_Type(BgpExtendedCommunity):defaultHexValue=_Z
_VpwsConfigVpnId_Type.__name__=_R
_VpwsConfigVpnId_Object=MibTableColumn
vpwsConfigVpnId=_VpwsConfigVpnId_Object((1,3,6,1,4,1,629,10,19,1,1,1,15),_VpwsConfigVpnId_Type())
vpwsConfigVpnId.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwsConfigVpnId.setStatus(_A)
class _VpwsConfigLocalSiteID_Type(L2vpnVeIdOrZero):defaultValue=0
_VpwsConfigLocalSiteID_Type.__name__=_K
_VpwsConfigLocalSiteID_Object=MibTableColumn
vpwsConfigLocalSiteID=_VpwsConfigLocalSiteID_Object((1,3,6,1,4,1,629,10,19,1,1,1,16),_VpwsConfigLocalSiteID_Type())
vpwsConfigLocalSiteID.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwsConfigLocalSiteID.setStatus(_A)
class _VpwsConfigLocalPreference_Type(Unsigned32):defaultValue=100
_VpwsConfigLocalPreference_Type.__name__=_H
_VpwsConfigLocalPreference_Object=MibTableColumn
vpwsConfigLocalPreference=_VpwsConfigLocalPreference_Object((1,3,6,1,4,1,629,10,19,1,1,1,17),_VpwsConfigLocalPreference_Type())
vpwsConfigLocalPreference.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwsConfigLocalPreference.setStatus(_A)
class _VpwsConfigLabelBlockSize_Type(Unsigned32):defaultValue=8;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,2),ValueRangeConstraint(4,4),ValueRangeConstraint(8,8),ValueRangeConstraint(16,16))
_VpwsConfigLabelBlockSize_Type.__name__=_H
_VpwsConfigLabelBlockSize_Object=MibTableColumn
vpwsConfigLabelBlockSize=_VpwsConfigLabelBlockSize_Object((1,3,6,1,4,1,629,10,19,1,1,1,18),_VpwsConfigLabelBlockSize_Type())
vpwsConfigLabelBlockSize.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwsConfigLabelBlockSize.setStatus(_A)
class _VpwsConfigIncludeCSV_Type(TruthValue):defaultValue=2
_VpwsConfigIncludeCSV_Type.__name__=_E
_VpwsConfigIncludeCSV_Object=MibTableColumn
vpwsConfigIncludeCSV=_VpwsConfigIncludeCSV_Object((1,3,6,1,4,1,629,10,19,1,1,1,19),_VpwsConfigIncludeCSV_Type())
vpwsConfigIncludeCSV.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwsConfigIncludeCSV.setStatus(_A)
class _VpwsConfigIgnoreMtuMismatch_Type(TruthValue):defaultValue=2
_VpwsConfigIgnoreMtuMismatch_Type.__name__=_E
_VpwsConfigIgnoreMtuMismatch_Object=MibTableColumn
vpwsConfigIgnoreMtuMismatch=_VpwsConfigIgnoreMtuMismatch_Object((1,3,6,1,4,1,629,10,19,1,1,1,20),_VpwsConfigIgnoreMtuMismatch_Type())
vpwsConfigIgnoreMtuMismatch.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwsConfigIgnoreMtuMismatch.setStatus(_A)
class _VpwsConfigIgnoreEncapsMismatch_Type(TruthValue):defaultValue=2
_VpwsConfigIgnoreEncapsMismatch_Type.__name__=_E
_VpwsConfigIgnoreEncapsMismatch_Object=MibTableColumn
vpwsConfigIgnoreEncapsMismatch=_VpwsConfigIgnoreEncapsMismatch_Object((1,3,6,1,4,1,629,10,19,1,1,1,21),_VpwsConfigIgnoreEncapsMismatch_Type())
vpwsConfigIgnoreEncapsMismatch.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwsConfigIgnoreEncapsMismatch.setStatus(_A)
_VpwsStatusTable_Object=MibTable
vpwsStatusTable=_VpwsStatusTable_Object((1,3,6,1,4,1,629,10,19,1,2))
if mibBuilder.loadTexts:vpwsStatusTable.setStatus(_A)
_VpwsStatusEntry_Object=MibTableRow
vpwsStatusEntry=_VpwsStatusEntry_Object((1,3,6,1,4,1,629,10,19,1,2,1))
vpwsStatusEntry.setIndexNames((0,_F,_G),(0,_B,_I))
if mibBuilder.loadTexts:vpwsStatusEntry.setStatus(_A)
_VpwsStatusOperStatus_Type=NpgOperStatus
_VpwsStatusOperStatus_Object=MibTableColumn
vpwsStatusOperStatus=_VpwsStatusOperStatus_Object((1,3,6,1,4,1,629,10,19,1,2,1,3),_VpwsStatusOperStatus_Type())
vpwsStatusOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwsStatusOperStatus.setStatus(_A)
_VpwsStatusVcCount_Type=Gauge32
_VpwsStatusVcCount_Object=MibTableColumn
vpwsStatusVcCount=_VpwsStatusVcCount_Object((1,3,6,1,4,1,629,10,19,1,2,1,4),_VpwsStatusVcCount_Type())
vpwsStatusVcCount.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwsStatusVcCount.setStatus(_A)
_VpwsStatusDesignatedForwarder_Type=TruthValue
_VpwsStatusDesignatedForwarder_Object=MibTableColumn
vpwsStatusDesignatedForwarder=_VpwsStatusDesignatedForwarder_Object((1,3,6,1,4,1,629,10,19,1,2,1,5),_VpwsStatusDesignatedForwarder_Type())
vpwsStatusDesignatedForwarder.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwsStatusDesignatedForwarder.setStatus(_A)
_VpwsBindCfgTable_Object=MibTable
vpwsBindCfgTable=_VpwsBindCfgTable_Object((1,3,6,1,4,1,629,10,19,1,3))
if mibBuilder.loadTexts:vpwsBindCfgTable.setStatus(_A)
_VpwsBindCfgEntry_Object=MibTableRow
vpwsBindCfgEntry=_VpwsBindCfgEntry_Object((1,3,6,1,4,1,629,10,19,1,3,1))
vpwsBindCfgEntry.setIndexNames((0,_F,_G),(0,_M,_N))
if mibBuilder.loadTexts:vpwsBindCfgEntry.setStatus(_A)
_VpwsBindCfgRowStatus_Type=RowStatus
_VpwsBindCfgRowStatus_Object=MibTableColumn
vpwsBindCfgRowStatus=_VpwsBindCfgRowStatus_Object((1,3,6,1,4,1,629,10,19,1,3,1,3),_VpwsBindCfgRowStatus_Type())
vpwsBindCfgRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwsBindCfgRowStatus.setStatus(_A)
class _VpwsBindCfgAdminStatus_Type(AdminStatus):defaultValue=1
_VpwsBindCfgAdminStatus_Type.__name__=_L
_VpwsBindCfgAdminStatus_Object=MibTableColumn
vpwsBindCfgAdminStatus=_VpwsBindCfgAdminStatus_Object((1,3,6,1,4,1,629,10,19,1,3,1,4),_VpwsBindCfgAdminStatus_Type())
vpwsBindCfgAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwsBindCfgAdminStatus.setStatus(_A)
_VpwsBindCfgOperStatus_Type=NpgOperStatus
_VpwsBindCfgOperStatus_Object=MibTableColumn
vpwsBindCfgOperStatus=_VpwsBindCfgOperStatus_Object((1,3,6,1,4,1,629,10,19,1,3,1,5),_VpwsBindCfgOperStatus_Type())
vpwsBindCfgOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwsBindCfgOperStatus.setStatus(_A)
class _VpwsBindCfgVpwsIndex_Type(NumericIndexOrZero):defaultValue=0
_VpwsBindCfgVpwsIndex_Type.__name__=_W
_VpwsBindCfgVpwsIndex_Object=MibTableColumn
vpwsBindCfgVpwsIndex=_VpwsBindCfgVpwsIndex_Object((1,3,6,1,4,1,629,10,19,1,3,1,6),_VpwsBindCfgVpwsIndex_Type())
vpwsBindCfgVpwsIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwsBindCfgVpwsIndex.setStatus(_A)
class _VpwsBindCfgPwBindType_Type(L2vpnPwBindType):defaultValue=1
_VpwsBindCfgPwBindType_Type.__name__=_U
_VpwsBindCfgPwBindType_Object=MibTableColumn
vpwsBindCfgPwBindType=_VpwsBindCfgPwBindType_Object((1,3,6,1,4,1,629,10,19,1,3,1,7),_VpwsBindCfgPwBindType_Type())
vpwsBindCfgPwBindType.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwsBindCfgPwBindType.setStatus(_A)
class _VpwsBindCfgPwSetIndex_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1073741823))
_VpwsBindCfgPwSetIndex_Type.__name__=_H
_VpwsBindCfgPwSetIndex_Object=MibTableColumn
vpwsBindCfgPwSetIndex=_VpwsBindCfgPwSetIndex_Object((1,3,6,1,4,1,629,10,19,1,3,1,8),_VpwsBindCfgPwSetIndex_Type())
vpwsBindCfgPwSetIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwsBindCfgPwSetIndex.setStatus(_A)
class _VpwsBindCfgRemoteSiteID_Type(L2vpnVeIdOrZero):defaultValue=0
_VpwsBindCfgRemoteSiteID_Type.__name__=_K
_VpwsBindCfgRemoteSiteID_Object=MibTableColumn
vpwsBindCfgRemoteSiteID=_VpwsBindCfgRemoteSiteID_Object((1,3,6,1,4,1,629,10,19,1,3,1,9),_VpwsBindCfgRemoteSiteID_Type())
vpwsBindCfgRemoteSiteID.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwsBindCfgRemoteSiteID.setStatus(_A)
class _VpwsBindCfgLclSwitchIfIndex_Type(InterfaceIndexOrZero):defaultValue=0
_VpwsBindCfgLclSwitchIfIndex_Type.__name__=_Y
_VpwsBindCfgLclSwitchIfIndex_Object=MibTableColumn
vpwsBindCfgLclSwitchIfIndex=_VpwsBindCfgLclSwitchIfIndex_Object((1,3,6,1,4,1,629,10,19,1,3,1,10),_VpwsBindCfgLclSwitchIfIndex_Type())
vpwsBindCfgLclSwitchIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:vpwsBindCfgLclSwitchIfIndex.setStatus(_A)
_VpwsBindTable_Object=MibTable
vpwsBindTable=_VpwsBindTable_Object((1,3,6,1,4,1,629,10,19,1,4))
if mibBuilder.loadTexts:vpwsBindTable.setStatus(_A)
_VpwsBindEntry_Object=MibTableRow
vpwsBindEntry=_VpwsBindEntry_Object((1,3,6,1,4,1,629,10,19,1,4,1))
vpwsBindEntry.setIndexNames((0,_F,_G),(0,_B,_I),(0,_M,_N))
if mibBuilder.loadTexts:vpwsBindEntry.setStatus(_A)
_VpwsBindOperStatus_Type=NpgOperStatus
_VpwsBindOperStatus_Object=MibTableColumn
vpwsBindOperStatus=_VpwsBindOperStatus_Object((1,3,6,1,4,1,629,10,19,1,4,1,4),_VpwsBindOperStatus_Type())
vpwsBindOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwsBindOperStatus.setStatus(_A)
_VpwsBindPwBindType_Type=L2vpnPwBindType
_VpwsBindPwBindType_Object=MibTableColumn
vpwsBindPwBindType=_VpwsBindPwBindType_Object((1,3,6,1,4,1,629,10,19,1,4,1,5),_VpwsBindPwBindType_Type())
vpwsBindPwBindType.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwsBindPwBindType.setStatus(_A)
_VpwsBindPwSetIndex_Type=NumericIndex
_VpwsBindPwSetIndex_Object=MibTableColumn
vpwsBindPwSetIndex=_VpwsBindPwSetIndex_Object((1,3,6,1,4,1,629,10,19,1,4,1,6),_VpwsBindPwSetIndex_Type())
vpwsBindPwSetIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwsBindPwSetIndex.setStatus(_A)
_VpwsBindPwIfIndex_Type=InterfaceIndex
_VpwsBindPwIfIndex_Object=MibTableColumn
vpwsBindPwIfIndex=_VpwsBindPwIfIndex_Object((1,3,6,1,4,1,629,10,19,1,4,1,7),_VpwsBindPwIfIndex_Type())
vpwsBindPwIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwsBindPwIfIndex.setStatus(_A)
_VpwsBindLocalSiteID_Type=L2vpnVeIdOrZero
_VpwsBindLocalSiteID_Object=MibTableColumn
vpwsBindLocalSiteID=_VpwsBindLocalSiteID_Object((1,3,6,1,4,1,629,10,19,1,4,1,8),_VpwsBindLocalSiteID_Type())
vpwsBindLocalSiteID.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwsBindLocalSiteID.setStatus(_A)
_VpwsBindRemoteSiteID_Type=L2vpnVeIdOrZero
_VpwsBindRemoteSiteID_Object=MibTableColumn
vpwsBindRemoteSiteID=_VpwsBindRemoteSiteID_Object((1,3,6,1,4,1,629,10,19,1,4,1,9),_VpwsBindRemoteSiteID_Type())
vpwsBindRemoteSiteID.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwsBindRemoteSiteID.setStatus(_A)
_VpwsBindLclSwitchIfIndex_Type=InterfaceIndex
_VpwsBindLclSwitchIfIndex_Object=MibTableColumn
vpwsBindLclSwitchIfIndex=_VpwsBindLclSwitchIfIndex_Object((1,3,6,1,4,1,629,10,19,1,4,1,10),_VpwsBindLclSwitchIfIndex_Type())
vpwsBindLclSwitchIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwsBindLclSwitchIfIndex.setStatus(_A)
_VpwsBindRemoteRD_Type=BgpRouteDistinguisher
_VpwsBindRemoteRD_Object=MibTableColumn
vpwsBindRemoteRD=_VpwsBindRemoteRD_Object((1,3,6,1,4,1,629,10,19,1,4,1,11),_VpwsBindRemoteRD_Type())
vpwsBindRemoteRD.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwsBindRemoteRD.setStatus(_A)
_VpwsBindRemoteAddrType_Type=InetAddressType
_VpwsBindRemoteAddrType_Object=MibTableColumn
vpwsBindRemoteAddrType=_VpwsBindRemoteAddrType_Object((1,3,6,1,4,1,629,10,19,1,4,1,12),_VpwsBindRemoteAddrType_Type())
vpwsBindRemoteAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwsBindRemoteAddrType.setStatus(_A)
_VpwsBindRemoteAddr_Type=InetAddress
_VpwsBindRemoteAddr_Object=MibTableColumn
vpwsBindRemoteAddr=_VpwsBindRemoteAddr_Object((1,3,6,1,4,1,629,10,19,1,4,1,13),_VpwsBindRemoteAddr_Type())
vpwsBindRemoteAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:vpwsBindRemoteAddr.setStatus(_A)
_VpwsConformance_ObjectIdentity=ObjectIdentity
vpwsConformance=_VpwsConformance_ObjectIdentity((1,3,6,1,4,1,629,10,19,2))
_VpwsCompliances_ObjectIdentity=ObjectIdentity
vpwsCompliances=_VpwsCompliances_ObjectIdentity((1,3,6,1,4,1,629,10,19,2,1))
_VpwsGroups_ObjectIdentity=ObjectIdentity
vpwsGroups=_VpwsGroups_ObjectIdentity((1,3,6,1,4,1,629,10,19,2,2))
vpwsBaseGroup=ObjectGroup((1,3,6,1,4,1,629,10,19,2,2,1))
vpwsBaseGroup.setObjects(*((_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_O),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0)))
if mibBuilder.loadTexts:vpwsBaseGroup.setStatus(_A)
vpwsDoubleSidedGroup=ObjectGroup((1,3,6,1,4,1,629,10,19,2,2,2))
vpwsDoubleSidedGroup.setObjects(*((_B,_O),(_B,_A1)))
if mibBuilder.loadTexts:vpwsDoubleSidedGroup.setStatus(_A)
vpwsBgpADGroup=ObjectGroup((1,3,6,1,4,1,629,10,19,2,2,3))
vpwsBgpADGroup.setObjects(*((_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC)))
if mibBuilder.loadTexts:vpwsBgpADGroup.setStatus(_A)
vpwsFullCompliance=ModuleCompliance((1,3,6,1,4,1,629,10,19,2,1,1))
vpwsFullCompliance.setObjects(*((_B,_J),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:vpwsFullCompliance.setStatus(_A)
vpwsDoubleSidedCompliance=ModuleCompliance((1,3,6,1,4,1,629,10,19,2,1,2))
vpwsDoubleSidedCompliance.setObjects(*((_B,_J),(_B,_P)))
if mibBuilder.loadTexts:vpwsDoubleSidedCompliance.setStatus(_A)
vpwsBgpADCompliance=ModuleCompliance((1,3,6,1,4,1,629,10,19,2,1,3))
vpwsBgpADCompliance.setObjects(*((_B,_J),(_B,_Q)))
if mibBuilder.loadTexts:vpwsBgpADCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'nbase':nbase,'opx':opx,'vpwsMib':vpwsMib,'vpwsObjects':vpwsObjects,'vpwsConfigTable':vpwsConfigTable,'vpwsConfigEntry':vpwsConfigEntry,_I:vpwsIndex,_a:vpwsConfigRowStatus,_b:vpwsConfigAdminStatus,_c:vpwsConfigOperStatus,_d:vpwsConfigName,_e:vpwsConfigDescr,_f:vpwsConfigADType,_g:vpwsConfigSigType,_h:vpwsConfigPwEncapType,_i:vpwsConfigMtu,_j:vpwsConfigControlWord,_k:vpwsConfigSeqDelivery,_A2:vpwsConfigRouteDistinguisher,_A3:vpwsConfigVpnId,_A4:vpwsConfigLocalSiteID,_A5:vpwsConfigLocalPreference,_A6:vpwsConfigLabelBlockSize,_A7:vpwsConfigIncludeCSV,_A8:vpwsConfigIgnoreMtuMismatch,_A9:vpwsConfigIgnoreEncapsMismatch,'vpwsStatusTable':vpwsStatusTable,'vpwsStatusEntry':vpwsStatusEntry,_l:vpwsStatusOperStatus,_m:vpwsStatusVcCount,_n:vpwsStatusDesignatedForwarder,'vpwsBindCfgTable':vpwsBindCfgTable,'vpwsBindCfgEntry':vpwsBindCfgEntry,_o:vpwsBindCfgRowStatus,_p:vpwsBindCfgAdminStatus,_q:vpwsBindCfgOperStatus,_r:vpwsBindCfgVpwsIndex,_s:vpwsBindCfgPwBindType,_O:vpwsBindCfgPwSetIndex,_AA:vpwsBindCfgRemoteSiteID,_A1:vpwsBindCfgLclSwitchIfIndex,'vpwsBindTable':vpwsBindTable,'vpwsBindEntry':vpwsBindEntry,_t:vpwsBindOperStatus,_u:vpwsBindPwBindType,_v:vpwsBindPwSetIndex,_w:vpwsBindPwIfIndex,_AB:vpwsBindLocalSiteID,_AC:vpwsBindRemoteSiteID,_x:vpwsBindLclSwitchIfIndex,_y:vpwsBindRemoteRD,_z:vpwsBindRemoteAddrType,_A0:vpwsBindRemoteAddr,'vpwsConformance':vpwsConformance,'vpwsCompliances':vpwsCompliances,'vpwsFullCompliance':vpwsFullCompliance,'vpwsDoubleSidedCompliance':vpwsDoubleSidedCompliance,'vpwsBgpADCompliance':vpwsBgpADCompliance,'vpwsGroups':vpwsGroups,_J:vpwsBaseGroup,_P:vpwsDoubleSidedGroup,_Q:vpwsBgpADGroup})