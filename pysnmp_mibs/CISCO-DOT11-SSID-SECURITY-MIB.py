_AC='cdot11SecSsidBackupVlanManagementGroup'
_AB='cdot11SecSsidMaxBackupVlans'
_AA='cdot11SecSsidBackupVlanRowStatus'
_A9='cdot11MbssidIfBroadcast'
_A8='cdot11MbssidIfMacAddress'
_A7='cdot11MbssidMacAddrSupported'
_A6='cdot11SecAuxSsidMbssidDtimPeriod'
_A5='cdot11SecAuxSsidMbssidBroadcast'
_A4='cdot11SecVlanNameRowStatus'
_A3='cdot11SecVlanNameId'
_A2='cdot11SecLocalAuthServerEnabled'
_A1='cdot11SecAuxSsidAuthMacAlternate'
_A0='cdot11SecAuxSsidAuthMacMethod'
_z='cdot11SecAuxSsidAuthEapMethod'
_y='cdot11SecAuxSsidAuthPlusMac'
_x='cdot11SecAuxSsidAuthPlusEap'
_w='cdot11SecAuxSsidAuthEnabled'
_v='cdot11SecInterfSsidRowStatus'
_u='cdot11SecAuxSsidVlanName'
_t='cdot11SecSsidInformationElement'
_s='cdot11SecSsidRedirectFilter'
_r='cdot11SecSsidRedirectDestAddr'
_q='cdot11SecSsidRedirectAddrType'
_p='cdot11SecAuxSsidWirelessNetId'
_o='cdot11SecAuxSsidRowStatus'
_n='cdot11SecAuxSsidAuthKeyMgmtOpt'
_m='cdot11SecAuxSsidAuthKeyMgmt'
_l='cdot11SecAuxSsidLoginPassword'
_k='cdot11SecAuxSsidLoginUsername'
_j='cdot11SecAuxRadiusAccounting'
_i='cdot11SecAuxSsidWpaPsk'
_h='cdot11SecAuxSsidVlan'
_g='cdot11SecAuxSsidMaxStations'
_f='cdot11SecAuxSsidProxyMobileIp'
_e='cdot11SecAuxSsidInfraStruct'
_d='cdot11SecAuxSsidBroadcast'
_c='cdot11SecVlanName'
_b='cdot11SecSsidBackupVlan'
_a='CDot11VlanName'
_Z='CDot11InformationElementType'
_Y='CDot11WiFiPaPreSharedKey'
_X='InetAddressType'
_W='InetAddress'
_V='dot11AuthenticationAlgorithmsIndex'
_U='IEEE802dot11-MIB'
_T='cdot11MbssidSupportGroup'
_S='cdot11SecVlanManagementGroup'
_R='cdot11ModuleAuthenticationGroup'
_Q='cdot11SsidAuthenticationGroup'
_P='cdot11SecSsidManagementGroup'
_O='cdot11MbssidMacAddrIndex'
_N='not-accessible'
_M='Unsigned32'
_L='CDot11IfVlanIdOrZero'
_K='read-only'
_J='ifIndex'
_I='IF-MIB'
_H='TruthValue'
_G='Integer32'
_F='SnmpAdminString'
_E='cdot11SecAuxSsid'
_D='read-write'
_C='read-create'
_B='CISCO-DOT11-SSID-SECURITY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CDot11IfVlanIdOrZero,=mibBuilder.importSymbols('CISCO-DOT11-IF-MIB',_L)
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
dot11AuthenticationAlgorithmsIndex,=mibBuilder.importSymbols(_U,_V)
ifIndex,=mibBuilder.importSymbols(_I,_J)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_W,_X)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_M,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_H)
ciscoDot11SsidSecMIB=ModuleIdentity((1,3,6,1,4,1,9,9,413))
if mibBuilder.loadTexts:ciscoDot11SsidSecMIB.setRevisions(('2007-04-12 00:00','2006-05-16 00:00','2004-09-14 00:00','2004-05-15 00:00'))
class CDot11SecAuthKeyMgmtType(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('cckm',0),('wpa',1),('wpa1',2),('wpa2',3)))
class CDot11WiFiPaPreSharedKey(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
class CDot11SsidString(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
class CDot11VlanName(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
class CDot11InformationElementType(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('ssidl',0),('advertisement',1),('wps',2)))
_CiscoDot11SsidSecMIBObjects_ObjectIdentity=ObjectIdentity
ciscoDot11SsidSecMIBObjects=_CiscoDot11SsidSecMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,413,1))
_Cdot11SecSsidManagement_ObjectIdentity=ObjectIdentity
cdot11SecSsidManagement=_Cdot11SecSsidManagement_ObjectIdentity((1,3,6,1,4,1,9,9,413,1,1))
_Cdot11SecAuxSsidTable_Object=MibTable
cdot11SecAuxSsidTable=_Cdot11SecAuxSsidTable_Object((1,3,6,1,4,1,9,9,413,1,1,1))
if mibBuilder.loadTexts:cdot11SecAuxSsidTable.setStatus(_A)
_Cdot11SecAuxSsidEntry_Object=MibTableRow
cdot11SecAuxSsidEntry=_Cdot11SecAuxSsidEntry_Object((1,3,6,1,4,1,9,9,413,1,1,1,1))
cdot11SecAuxSsidEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:cdot11SecAuxSsidEntry.setStatus(_A)
_Cdot11SecAuxSsid_Type=CDot11SsidString
_Cdot11SecAuxSsid_Object=MibTableColumn
cdot11SecAuxSsid=_Cdot11SecAuxSsid_Object((1,3,6,1,4,1,9,9,413,1,1,1,1,1),_Cdot11SecAuxSsid_Type())
cdot11SecAuxSsid.setMaxAccess(_N)
if mibBuilder.loadTexts:cdot11SecAuxSsid.setStatus(_A)
class _Cdot11SecAuxSsidBroadcast_Type(TruthValue):defaultValue=2
_Cdot11SecAuxSsidBroadcast_Type.__name__=_H
_Cdot11SecAuxSsidBroadcast_Object=MibTableColumn
cdot11SecAuxSsidBroadcast=_Cdot11SecAuxSsidBroadcast_Object((1,3,6,1,4,1,9,9,413,1,1,1,1,2),_Cdot11SecAuxSsidBroadcast_Type())
cdot11SecAuxSsidBroadcast.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot11SecAuxSsidBroadcast.setStatus(_A)
class _Cdot11SecAuxSsidInfraStruct_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('infraStructure',1),('nonInfraStructure',2),('optional',3)))
_Cdot11SecAuxSsidInfraStruct_Type.__name__=_G
_Cdot11SecAuxSsidInfraStruct_Object=MibTableColumn
cdot11SecAuxSsidInfraStruct=_Cdot11SecAuxSsidInfraStruct_Object((1,3,6,1,4,1,9,9,413,1,1,1,1,3),_Cdot11SecAuxSsidInfraStruct_Type())
cdot11SecAuxSsidInfraStruct.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot11SecAuxSsidInfraStruct.setStatus(_A)
class _Cdot11SecAuxSsidProxyMobileIp_Type(TruthValue):defaultValue=2
_Cdot11SecAuxSsidProxyMobileIp_Type.__name__=_H
_Cdot11SecAuxSsidProxyMobileIp_Object=MibTableColumn
cdot11SecAuxSsidProxyMobileIp=_Cdot11SecAuxSsidProxyMobileIp_Object((1,3,6,1,4,1,9,9,413,1,1,1,1,4),_Cdot11SecAuxSsidProxyMobileIp_Type())
cdot11SecAuxSsidProxyMobileIp.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot11SecAuxSsidProxyMobileIp.setStatus(_A)
class _Cdot11SecAuxSsidMaxStations_Type(Unsigned32):defaultValue=255;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2007))
_Cdot11SecAuxSsidMaxStations_Type.__name__=_M
_Cdot11SecAuxSsidMaxStations_Object=MibTableColumn
cdot11SecAuxSsidMaxStations=_Cdot11SecAuxSsidMaxStations_Object((1,3,6,1,4,1,9,9,413,1,1,1,1,5),_Cdot11SecAuxSsidMaxStations_Type())
cdot11SecAuxSsidMaxStations.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot11SecAuxSsidMaxStations.setStatus(_A)
class _Cdot11SecAuxSsidVlan_Type(CDot11IfVlanIdOrZero):defaultValue=0
_Cdot11SecAuxSsidVlan_Type.__name__=_L
_Cdot11SecAuxSsidVlan_Object=MibTableColumn
cdot11SecAuxSsidVlan=_Cdot11SecAuxSsidVlan_Object((1,3,6,1,4,1,9,9,413,1,1,1,1,6),_Cdot11SecAuxSsidVlan_Type())
cdot11SecAuxSsidVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot11SecAuxSsidVlan.setStatus(_A)
class _Cdot11SecAuxSsidWpaPsk_Type(CDot11WiFiPaPreSharedKey):defaultHexValue=''
_Cdot11SecAuxSsidWpaPsk_Type.__name__=_Y
_Cdot11SecAuxSsidWpaPsk_Object=MibTableColumn
cdot11SecAuxSsidWpaPsk=_Cdot11SecAuxSsidWpaPsk_Object((1,3,6,1,4,1,9,9,413,1,1,1,1,7),_Cdot11SecAuxSsidWpaPsk_Type())
cdot11SecAuxSsidWpaPsk.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot11SecAuxSsidWpaPsk.setStatus(_A)
class _Cdot11SecAuxRadiusAccounting_Type(SnmpAdminString):defaultValue=OctetString('')
_Cdot11SecAuxRadiusAccounting_Type.__name__=_F
_Cdot11SecAuxRadiusAccounting_Object=MibTableColumn
cdot11SecAuxRadiusAccounting=_Cdot11SecAuxRadiusAccounting_Object((1,3,6,1,4,1,9,9,413,1,1,1,1,8),_Cdot11SecAuxRadiusAccounting_Type())
cdot11SecAuxRadiusAccounting.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot11SecAuxRadiusAccounting.setStatus(_A)
class _Cdot11SecAuxSsidLoginUsername_Type(SnmpAdminString):defaultValue=OctetString('')
_Cdot11SecAuxSsidLoginUsername_Type.__name__=_F
_Cdot11SecAuxSsidLoginUsername_Object=MibTableColumn
cdot11SecAuxSsidLoginUsername=_Cdot11SecAuxSsidLoginUsername_Object((1,3,6,1,4,1,9,9,413,1,1,1,1,9),_Cdot11SecAuxSsidLoginUsername_Type())
cdot11SecAuxSsidLoginUsername.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot11SecAuxSsidLoginUsername.setStatus(_A)
class _Cdot11SecAuxSsidLoginPassword_Type(SnmpAdminString):defaultValue=OctetString('')
_Cdot11SecAuxSsidLoginPassword_Type.__name__=_F
_Cdot11SecAuxSsidLoginPassword_Object=MibTableColumn
cdot11SecAuxSsidLoginPassword=_Cdot11SecAuxSsidLoginPassword_Object((1,3,6,1,4,1,9,9,413,1,1,1,1,10),_Cdot11SecAuxSsidLoginPassword_Type())
cdot11SecAuxSsidLoginPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot11SecAuxSsidLoginPassword.setStatus(_A)
_Cdot11SecAuxSsidAuthKeyMgmt_Type=CDot11SecAuthKeyMgmtType
_Cdot11SecAuxSsidAuthKeyMgmt_Object=MibTableColumn
cdot11SecAuxSsidAuthKeyMgmt=_Cdot11SecAuxSsidAuthKeyMgmt_Object((1,3,6,1,4,1,9,9,413,1,1,1,1,11),_Cdot11SecAuxSsidAuthKeyMgmt_Type())
cdot11SecAuxSsidAuthKeyMgmt.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot11SecAuxSsidAuthKeyMgmt.setStatus(_A)
class _Cdot11SecAuxSsidAuthKeyMgmtOpt_Type(TruthValue):defaultValue=2
_Cdot11SecAuxSsidAuthKeyMgmtOpt_Type.__name__=_H
_Cdot11SecAuxSsidAuthKeyMgmtOpt_Object=MibTableColumn
cdot11SecAuxSsidAuthKeyMgmtOpt=_Cdot11SecAuxSsidAuthKeyMgmtOpt_Object((1,3,6,1,4,1,9,9,413,1,1,1,1,12),_Cdot11SecAuxSsidAuthKeyMgmtOpt_Type())
cdot11SecAuxSsidAuthKeyMgmtOpt.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot11SecAuxSsidAuthKeyMgmtOpt.setStatus(_A)
_Cdot11SecAuxSsidRowStatus_Type=RowStatus
_Cdot11SecAuxSsidRowStatus_Object=MibTableColumn
cdot11SecAuxSsidRowStatus=_Cdot11SecAuxSsidRowStatus_Object((1,3,6,1,4,1,9,9,413,1,1,1,1,13),_Cdot11SecAuxSsidRowStatus_Type())
cdot11SecAuxSsidRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot11SecAuxSsidRowStatus.setStatus(_A)
class _Cdot11SecAuxSsidWirelessNetId_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4096))
_Cdot11SecAuxSsidWirelessNetId_Type.__name__=_G
_Cdot11SecAuxSsidWirelessNetId_Object=MibTableColumn
cdot11SecAuxSsidWirelessNetId=_Cdot11SecAuxSsidWirelessNetId_Object((1,3,6,1,4,1,9,9,413,1,1,1,1,14),_Cdot11SecAuxSsidWirelessNetId_Type())
cdot11SecAuxSsidWirelessNetId.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot11SecAuxSsidWirelessNetId.setStatus(_A)
class _Cdot11SecSsidRedirectAddrType_Type(InetAddressType):defaultValue=1
_Cdot11SecSsidRedirectAddrType_Type.__name__=_X
_Cdot11SecSsidRedirectAddrType_Object=MibTableColumn
cdot11SecSsidRedirectAddrType=_Cdot11SecSsidRedirectAddrType_Object((1,3,6,1,4,1,9,9,413,1,1,1,1,15),_Cdot11SecSsidRedirectAddrType_Type())
cdot11SecSsidRedirectAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot11SecSsidRedirectAddrType.setStatus(_A)
class _Cdot11SecSsidRedirectDestAddr_Type(InetAddress):defaultHexValue='00000000'
_Cdot11SecSsidRedirectDestAddr_Type.__name__=_W
_Cdot11SecSsidRedirectDestAddr_Object=MibTableColumn
cdot11SecSsidRedirectDestAddr=_Cdot11SecSsidRedirectDestAddr_Object((1,3,6,1,4,1,9,9,413,1,1,1,1,16),_Cdot11SecSsidRedirectDestAddr_Type())
cdot11SecSsidRedirectDestAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot11SecSsidRedirectDestAddr.setStatus(_A)
class _Cdot11SecSsidRedirectFilter_Type(SnmpAdminString):defaultValue=OctetString('')
_Cdot11SecSsidRedirectFilter_Type.__name__=_F
_Cdot11SecSsidRedirectFilter_Object=MibTableColumn
cdot11SecSsidRedirectFilter=_Cdot11SecSsidRedirectFilter_Object((1,3,6,1,4,1,9,9,413,1,1,1,1,17),_Cdot11SecSsidRedirectFilter_Type())
cdot11SecSsidRedirectFilter.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot11SecSsidRedirectFilter.setStatus(_A)
class _Cdot11SecSsidInformationElement_Type(CDot11InformationElementType):defaultBinValue='0'
_Cdot11SecSsidInformationElement_Type.__name__=_Z
_Cdot11SecSsidInformationElement_Object=MibTableColumn
cdot11SecSsidInformationElement=_Cdot11SecSsidInformationElement_Object((1,3,6,1,4,1,9,9,413,1,1,1,1,18),_Cdot11SecSsidInformationElement_Type())
cdot11SecSsidInformationElement.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot11SecSsidInformationElement.setStatus(_A)
class _Cdot11SecAuxSsidVlanName_Type(CDot11VlanName):defaultValue=OctetString(' ')
_Cdot11SecAuxSsidVlanName_Type.__name__=_a
_Cdot11SecAuxSsidVlanName_Object=MibTableColumn
cdot11SecAuxSsidVlanName=_Cdot11SecAuxSsidVlanName_Object((1,3,6,1,4,1,9,9,413,1,1,1,1,19),_Cdot11SecAuxSsidVlanName_Type())
cdot11SecAuxSsidVlanName.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot11SecAuxSsidVlanName.setStatus(_A)
class _Cdot11SecAuxSsidMbssidBroadcast_Type(TruthValue):defaultValue=2
_Cdot11SecAuxSsidMbssidBroadcast_Type.__name__=_H
_Cdot11SecAuxSsidMbssidBroadcast_Object=MibTableColumn
cdot11SecAuxSsidMbssidBroadcast=_Cdot11SecAuxSsidMbssidBroadcast_Object((1,3,6,1,4,1,9,9,413,1,1,1,1,20),_Cdot11SecAuxSsidMbssidBroadcast_Type())
cdot11SecAuxSsidMbssidBroadcast.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot11SecAuxSsidMbssidBroadcast.setStatus(_A)
class _Cdot11SecAuxSsidMbssidDtimPeriod_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Cdot11SecAuxSsidMbssidDtimPeriod_Type.__name__=_G
_Cdot11SecAuxSsidMbssidDtimPeriod_Object=MibTableColumn
cdot11SecAuxSsidMbssidDtimPeriod=_Cdot11SecAuxSsidMbssidDtimPeriod_Object((1,3,6,1,4,1,9,9,413,1,1,1,1,21),_Cdot11SecAuxSsidMbssidDtimPeriod_Type())
cdot11SecAuxSsidMbssidDtimPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot11SecAuxSsidMbssidDtimPeriod.setStatus(_A)
if mibBuilder.loadTexts:cdot11SecAuxSsidMbssidDtimPeriod.setUnits('beacons')
_Cdot11SecAuxSsidAuthTable_Object=MibTable
cdot11SecAuxSsidAuthTable=_Cdot11SecAuxSsidAuthTable_Object((1,3,6,1,4,1,9,9,413,1,1,2))
if mibBuilder.loadTexts:cdot11SecAuxSsidAuthTable.setStatus(_A)
_Cdot11SecAuxSsidAuthEntry_Object=MibTableRow
cdot11SecAuxSsidAuthEntry=_Cdot11SecAuxSsidAuthEntry_Object((1,3,6,1,4,1,9,9,413,1,1,2,1))
cdot11SecAuxSsidAuthEntry.setIndexNames((0,_B,_E),(0,_U,_V))
if mibBuilder.loadTexts:cdot11SecAuxSsidAuthEntry.setStatus(_A)
_Cdot11SecAuxSsidAuthEnabled_Type=TruthValue
_Cdot11SecAuxSsidAuthEnabled_Object=MibTableColumn
cdot11SecAuxSsidAuthEnabled=_Cdot11SecAuxSsidAuthEnabled_Object((1,3,6,1,4,1,9,9,413,1,1,2,1,1),_Cdot11SecAuxSsidAuthEnabled_Type())
cdot11SecAuxSsidAuthEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:cdot11SecAuxSsidAuthEnabled.setStatus(_A)
_Cdot11SecAuxSsidAuthPlusEap_Type=TruthValue
_Cdot11SecAuxSsidAuthPlusEap_Object=MibTableColumn
cdot11SecAuxSsidAuthPlusEap=_Cdot11SecAuxSsidAuthPlusEap_Object((1,3,6,1,4,1,9,9,413,1,1,2,1,2),_Cdot11SecAuxSsidAuthPlusEap_Type())
cdot11SecAuxSsidAuthPlusEap.setMaxAccess(_D)
if mibBuilder.loadTexts:cdot11SecAuxSsidAuthPlusEap.setStatus(_A)
_Cdot11SecAuxSsidAuthPlusMac_Type=TruthValue
_Cdot11SecAuxSsidAuthPlusMac_Object=MibTableColumn
cdot11SecAuxSsidAuthPlusMac=_Cdot11SecAuxSsidAuthPlusMac_Object((1,3,6,1,4,1,9,9,413,1,1,2,1,3),_Cdot11SecAuxSsidAuthPlusMac_Type())
cdot11SecAuxSsidAuthPlusMac.setMaxAccess(_D)
if mibBuilder.loadTexts:cdot11SecAuxSsidAuthPlusMac.setStatus(_A)
_Cdot11SecAuxSsidAuthEapMethod_Type=SnmpAdminString
_Cdot11SecAuxSsidAuthEapMethod_Object=MibTableColumn
cdot11SecAuxSsidAuthEapMethod=_Cdot11SecAuxSsidAuthEapMethod_Object((1,3,6,1,4,1,9,9,413,1,1,2,1,4),_Cdot11SecAuxSsidAuthEapMethod_Type())
cdot11SecAuxSsidAuthEapMethod.setMaxAccess(_D)
if mibBuilder.loadTexts:cdot11SecAuxSsidAuthEapMethod.setStatus(_A)
_Cdot11SecAuxSsidAuthMacMethod_Type=SnmpAdminString
_Cdot11SecAuxSsidAuthMacMethod_Object=MibTableColumn
cdot11SecAuxSsidAuthMacMethod=_Cdot11SecAuxSsidAuthMacMethod_Object((1,3,6,1,4,1,9,9,413,1,1,2,1,5),_Cdot11SecAuxSsidAuthMacMethod_Type())
cdot11SecAuxSsidAuthMacMethod.setMaxAccess(_D)
if mibBuilder.loadTexts:cdot11SecAuxSsidAuthMacMethod.setStatus(_A)
_Cdot11SecAuxSsidAuthMacAlternate_Type=TruthValue
_Cdot11SecAuxSsidAuthMacAlternate_Object=MibTableColumn
cdot11SecAuxSsidAuthMacAlternate=_Cdot11SecAuxSsidAuthMacAlternate_Object((1,3,6,1,4,1,9,9,413,1,1,2,1,6),_Cdot11SecAuxSsidAuthMacAlternate_Type())
cdot11SecAuxSsidAuthMacAlternate.setMaxAccess(_D)
if mibBuilder.loadTexts:cdot11SecAuxSsidAuthMacAlternate.setStatus(_A)
_Cdot11SecInterfSsidTable_Object=MibTable
cdot11SecInterfSsidTable=_Cdot11SecInterfSsidTable_Object((1,3,6,1,4,1,9,9,413,1,1,3))
if mibBuilder.loadTexts:cdot11SecInterfSsidTable.setStatus(_A)
_Cdot11SecInterfSsidEntry_Object=MibTableRow
cdot11SecInterfSsidEntry=_Cdot11SecInterfSsidEntry_Object((1,3,6,1,4,1,9,9,413,1,1,3,1))
cdot11SecInterfSsidEntry.setIndexNames((0,_I,_J),(0,_B,_E))
if mibBuilder.loadTexts:cdot11SecInterfSsidEntry.setStatus(_A)
_Cdot11SecInterfSsidRowStatus_Type=RowStatus
_Cdot11SecInterfSsidRowStatus_Object=MibTableColumn
cdot11SecInterfSsidRowStatus=_Cdot11SecInterfSsidRowStatus_Object((1,3,6,1,4,1,9,9,413,1,1,3,1,1),_Cdot11SecInterfSsidRowStatus_Type())
cdot11SecInterfSsidRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot11SecInterfSsidRowStatus.setStatus(_A)
_Cdot11MbssidMacAddrSupportTable_Object=MibTable
cdot11MbssidMacAddrSupportTable=_Cdot11MbssidMacAddrSupportTable_Object((1,3,6,1,4,1,9,9,413,1,1,4))
if mibBuilder.loadTexts:cdot11MbssidMacAddrSupportTable.setStatus(_A)
_Cdot11MbssidMacAddrSupportEntry_Object=MibTableRow
cdot11MbssidMacAddrSupportEntry=_Cdot11MbssidMacAddrSupportEntry_Object((1,3,6,1,4,1,9,9,413,1,1,4,1))
cdot11MbssidMacAddrSupportEntry.setIndexNames((0,_I,_J),(0,_B,_O))
if mibBuilder.loadTexts:cdot11MbssidMacAddrSupportEntry.setStatus(_A)
class _Cdot11MbssidMacAddrIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_Cdot11MbssidMacAddrIndex_Type.__name__=_G
_Cdot11MbssidMacAddrIndex_Object=MibTableColumn
cdot11MbssidMacAddrIndex=_Cdot11MbssidMacAddrIndex_Object((1,3,6,1,4,1,9,9,413,1,1,4,1,1),_Cdot11MbssidMacAddrIndex_Type())
cdot11MbssidMacAddrIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:cdot11MbssidMacAddrIndex.setStatus(_A)
_Cdot11MbssidMacAddrSupported_Type=MacAddress
_Cdot11MbssidMacAddrSupported_Object=MibTableColumn
cdot11MbssidMacAddrSupported=_Cdot11MbssidMacAddrSupported_Object((1,3,6,1,4,1,9,9,413,1,1,4,1,2),_Cdot11MbssidMacAddrSupported_Type())
cdot11MbssidMacAddrSupported.setMaxAccess(_K)
if mibBuilder.loadTexts:cdot11MbssidMacAddrSupported.setStatus(_A)
_Cdot11MbssidInterfaceTable_Object=MibTable
cdot11MbssidInterfaceTable=_Cdot11MbssidInterfaceTable_Object((1,3,6,1,4,1,9,9,413,1,1,5))
if mibBuilder.loadTexts:cdot11MbssidInterfaceTable.setStatus(_A)
_Cdot11MbssidInterfaceEntry_Object=MibTableRow
cdot11MbssidInterfaceEntry=_Cdot11MbssidInterfaceEntry_Object((1,3,6,1,4,1,9,9,413,1,1,5,1))
cdot11MbssidInterfaceEntry.setIndexNames((0,_I,_J),(1,_B,_E))
if mibBuilder.loadTexts:cdot11MbssidInterfaceEntry.setStatus(_A)
_Cdot11MbssidIfMacAddress_Type=MacAddress
_Cdot11MbssidIfMacAddress_Object=MibTableColumn
cdot11MbssidIfMacAddress=_Cdot11MbssidIfMacAddress_Object((1,3,6,1,4,1,9,9,413,1,1,5,1,1),_Cdot11MbssidIfMacAddress_Type())
cdot11MbssidIfMacAddress.setMaxAccess(_K)
if mibBuilder.loadTexts:cdot11MbssidIfMacAddress.setStatus(_A)
_Cdot11MbssidIfBroadcast_Type=TruthValue
_Cdot11MbssidIfBroadcast_Object=MibTableColumn
cdot11MbssidIfBroadcast=_Cdot11MbssidIfBroadcast_Object((1,3,6,1,4,1,9,9,413,1,1,5,1,2),_Cdot11MbssidIfBroadcast_Type())
cdot11MbssidIfBroadcast.setMaxAccess(_K)
if mibBuilder.loadTexts:cdot11MbssidIfBroadcast.setStatus(_A)
class _Cdot11SecSsidMaxBackupVlans_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_Cdot11SecSsidMaxBackupVlans_Type.__name__=_M
_Cdot11SecSsidMaxBackupVlans_Object=MibScalar
cdot11SecSsidMaxBackupVlans=_Cdot11SecSsidMaxBackupVlans_Object((1,3,6,1,4,1,9,9,413,1,1,6),_Cdot11SecSsidMaxBackupVlans_Type())
cdot11SecSsidMaxBackupVlans.setMaxAccess(_D)
if mibBuilder.loadTexts:cdot11SecSsidMaxBackupVlans.setStatus(_A)
_Cdot11SecSsidBackupVlanTable_Object=MibTable
cdot11SecSsidBackupVlanTable=_Cdot11SecSsidBackupVlanTable_Object((1,3,6,1,4,1,9,9,413,1,1,7))
if mibBuilder.loadTexts:cdot11SecSsidBackupVlanTable.setStatus(_A)
_Cdot11SecSsidBackupVlanEntry_Object=MibTableRow
cdot11SecSsidBackupVlanEntry=_Cdot11SecSsidBackupVlanEntry_Object((1,3,6,1,4,1,9,9,413,1,1,7,1))
cdot11SecSsidBackupVlanEntry.setIndexNames((0,_B,_E),(0,_B,_b))
if mibBuilder.loadTexts:cdot11SecSsidBackupVlanEntry.setStatus(_A)
class _Cdot11SecSsidBackupVlan_Type(CDot11IfVlanIdOrZero):subtypeSpec=CDot11IfVlanIdOrZero.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Cdot11SecSsidBackupVlan_Type.__name__=_L
_Cdot11SecSsidBackupVlan_Object=MibTableColumn
cdot11SecSsidBackupVlan=_Cdot11SecSsidBackupVlan_Object((1,3,6,1,4,1,9,9,413,1,1,7,1,1),_Cdot11SecSsidBackupVlan_Type())
cdot11SecSsidBackupVlan.setMaxAccess(_N)
if mibBuilder.loadTexts:cdot11SecSsidBackupVlan.setStatus(_A)
_Cdot11SecSsidBackupVlanRowStatus_Type=RowStatus
_Cdot11SecSsidBackupVlanRowStatus_Object=MibTableColumn
cdot11SecSsidBackupVlanRowStatus=_Cdot11SecSsidBackupVlanRowStatus_Object((1,3,6,1,4,1,9,9,413,1,1,7,1,2),_Cdot11SecSsidBackupVlanRowStatus_Type())
cdot11SecSsidBackupVlanRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot11SecSsidBackupVlanRowStatus.setStatus(_A)
_Cdot11SecAuthManagement_ObjectIdentity=ObjectIdentity
cdot11SecAuthManagement=_Cdot11SecAuthManagement_ObjectIdentity((1,3,6,1,4,1,9,9,413,1,2))
_Cdot11SecLocalAuthServerEnabled_Type=TruthValue
_Cdot11SecLocalAuthServerEnabled_Object=MibScalar
cdot11SecLocalAuthServerEnabled=_Cdot11SecLocalAuthServerEnabled_Object((1,3,6,1,4,1,9,9,413,1,2,1),_Cdot11SecLocalAuthServerEnabled_Type())
cdot11SecLocalAuthServerEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:cdot11SecLocalAuthServerEnabled.setStatus(_A)
_Cdot11SecStatistics_ObjectIdentity=ObjectIdentity
cdot11SecStatistics=_Cdot11SecStatistics_ObjectIdentity((1,3,6,1,4,1,9,9,413,1,3))
_Cdot11SecVlanManagement_ObjectIdentity=ObjectIdentity
cdot11SecVlanManagement=_Cdot11SecVlanManagement_ObjectIdentity((1,3,6,1,4,1,9,9,413,1,4))
_Cdot11SecVlanNameTable_Object=MibTable
cdot11SecVlanNameTable=_Cdot11SecVlanNameTable_Object((1,3,6,1,4,1,9,9,413,1,4,1))
if mibBuilder.loadTexts:cdot11SecVlanNameTable.setStatus(_A)
_Cdot11SecVlanNameEntry_Object=MibTableRow
cdot11SecVlanNameEntry=_Cdot11SecVlanNameEntry_Object((1,3,6,1,4,1,9,9,413,1,4,1,1))
cdot11SecVlanNameEntry.setIndexNames((0,_B,_c))
if mibBuilder.loadTexts:cdot11SecVlanNameEntry.setStatus(_A)
_Cdot11SecVlanName_Type=CDot11VlanName
_Cdot11SecVlanName_Object=MibTableColumn
cdot11SecVlanName=_Cdot11SecVlanName_Object((1,3,6,1,4,1,9,9,413,1,4,1,1,1),_Cdot11SecVlanName_Type())
cdot11SecVlanName.setMaxAccess(_N)
if mibBuilder.loadTexts:cdot11SecVlanName.setStatus(_A)
_Cdot11SecVlanNameId_Type=CDot11IfVlanIdOrZero
_Cdot11SecVlanNameId_Object=MibTableColumn
cdot11SecVlanNameId=_Cdot11SecVlanNameId_Object((1,3,6,1,4,1,9,9,413,1,4,1,1,2),_Cdot11SecVlanNameId_Type())
cdot11SecVlanNameId.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot11SecVlanNameId.setStatus(_A)
_Cdot11SecVlanNameRowStatus_Type=RowStatus
_Cdot11SecVlanNameRowStatus_Object=MibTableColumn
cdot11SecVlanNameRowStatus=_Cdot11SecVlanNameRowStatus_Object((1,3,6,1,4,1,9,9,413,1,4,1,1,3),_Cdot11SecVlanNameRowStatus_Type())
cdot11SecVlanNameRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cdot11SecVlanNameRowStatus.setStatus(_A)
_CiscoDot11SsidSecMIBConformance_ObjectIdentity=ObjectIdentity
ciscoDot11SsidSecMIBConformance=_CiscoDot11SsidSecMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,413,2))
_CiscoDot11SsidSecMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoDot11SsidSecMIBCompliances=_CiscoDot11SsidSecMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,413,2,1))
_CiscoDot11SsidSecMIBGroups_ObjectIdentity=ObjectIdentity
ciscoDot11SsidSecMIBGroups=_CiscoDot11SsidSecMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,413,2,2))
cdot11SecSsidManagementGroup=ObjectGroup((1,3,6,1,4,1,9,9,413,2,2,1))
cdot11SecSsidManagementGroup.setObjects(*((_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v)))
if mibBuilder.loadTexts:cdot11SecSsidManagementGroup.setStatus(_A)
cdot11SsidAuthenticationGroup=ObjectGroup((1,3,6,1,4,1,9,9,413,2,2,2))
cdot11SsidAuthenticationGroup.setObjects(*((_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1)))
if mibBuilder.loadTexts:cdot11SsidAuthenticationGroup.setStatus(_A)
cdot11ModuleAuthenticationGroup=ObjectGroup((1,3,6,1,4,1,9,9,413,2,2,3))
cdot11ModuleAuthenticationGroup.setObjects((_B,_A2))
if mibBuilder.loadTexts:cdot11ModuleAuthenticationGroup.setStatus(_A)
cdot11SecVlanManagementGroup=ObjectGroup((1,3,6,1,4,1,9,9,413,2,2,4))
cdot11SecVlanManagementGroup.setObjects(*((_B,_A3),(_B,_A4)))
if mibBuilder.loadTexts:cdot11SecVlanManagementGroup.setStatus(_A)
cdot11MbssidSupportGroup=ObjectGroup((1,3,6,1,4,1,9,9,413,2,2,5))
cdot11MbssidSupportGroup.setObjects(*((_B,_A5),(_B,_A6),(_B,_O),(_B,_A7),(_B,_A8),(_B,_A9)))
if mibBuilder.loadTexts:cdot11MbssidSupportGroup.setStatus(_A)
cdot11SecSsidBackupVlanManagementGroup=ObjectGroup((1,3,6,1,4,1,9,9,413,2,2,6))
cdot11SecSsidBackupVlanManagementGroup.setObjects(*((_B,_AA),(_B,_AB)))
if mibBuilder.loadTexts:cdot11SecSsidBackupVlanManagementGroup.setStatus(_A)
ciscoDot11SsidSecCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,413,2,1,1))
ciscoDot11SsidSecCompliance.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:ciscoDot11SsidSecCompliance.setStatus('deprecated')
ciscoDot11SsidSecComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,413,2,1,2))
ciscoDot11SsidSecComplianceRev1.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_AC),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:ciscoDot11SsidSecComplianceRev1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CDot11SecAuthKeyMgmtType':CDot11SecAuthKeyMgmtType,_Y:CDot11WiFiPaPreSharedKey,'CDot11SsidString':CDot11SsidString,_a:CDot11VlanName,_Z:CDot11InformationElementType,'ciscoDot11SsidSecMIB':ciscoDot11SsidSecMIB,'ciscoDot11SsidSecMIBObjects':ciscoDot11SsidSecMIBObjects,'cdot11SecSsidManagement':cdot11SecSsidManagement,'cdot11SecAuxSsidTable':cdot11SecAuxSsidTable,'cdot11SecAuxSsidEntry':cdot11SecAuxSsidEntry,_E:cdot11SecAuxSsid,_d:cdot11SecAuxSsidBroadcast,_e:cdot11SecAuxSsidInfraStruct,_f:cdot11SecAuxSsidProxyMobileIp,_g:cdot11SecAuxSsidMaxStations,_h:cdot11SecAuxSsidVlan,_i:cdot11SecAuxSsidWpaPsk,_j:cdot11SecAuxRadiusAccounting,_k:cdot11SecAuxSsidLoginUsername,_l:cdot11SecAuxSsidLoginPassword,_m:cdot11SecAuxSsidAuthKeyMgmt,_n:cdot11SecAuxSsidAuthKeyMgmtOpt,_o:cdot11SecAuxSsidRowStatus,_p:cdot11SecAuxSsidWirelessNetId,_q:cdot11SecSsidRedirectAddrType,_r:cdot11SecSsidRedirectDestAddr,_s:cdot11SecSsidRedirectFilter,_t:cdot11SecSsidInformationElement,_u:cdot11SecAuxSsidVlanName,_A5:cdot11SecAuxSsidMbssidBroadcast,_A6:cdot11SecAuxSsidMbssidDtimPeriod,'cdot11SecAuxSsidAuthTable':cdot11SecAuxSsidAuthTable,'cdot11SecAuxSsidAuthEntry':cdot11SecAuxSsidAuthEntry,_w:cdot11SecAuxSsidAuthEnabled,_x:cdot11SecAuxSsidAuthPlusEap,_y:cdot11SecAuxSsidAuthPlusMac,_z:cdot11SecAuxSsidAuthEapMethod,_A0:cdot11SecAuxSsidAuthMacMethod,_A1:cdot11SecAuxSsidAuthMacAlternate,'cdot11SecInterfSsidTable':cdot11SecInterfSsidTable,'cdot11SecInterfSsidEntry':cdot11SecInterfSsidEntry,_v:cdot11SecInterfSsidRowStatus,'cdot11MbssidMacAddrSupportTable':cdot11MbssidMacAddrSupportTable,'cdot11MbssidMacAddrSupportEntry':cdot11MbssidMacAddrSupportEntry,_O:cdot11MbssidMacAddrIndex,_A7:cdot11MbssidMacAddrSupported,'cdot11MbssidInterfaceTable':cdot11MbssidInterfaceTable,'cdot11MbssidInterfaceEntry':cdot11MbssidInterfaceEntry,_A8:cdot11MbssidIfMacAddress,_A9:cdot11MbssidIfBroadcast,_AB:cdot11SecSsidMaxBackupVlans,'cdot11SecSsidBackupVlanTable':cdot11SecSsidBackupVlanTable,'cdot11SecSsidBackupVlanEntry':cdot11SecSsidBackupVlanEntry,_b:cdot11SecSsidBackupVlan,_AA:cdot11SecSsidBackupVlanRowStatus,'cdot11SecAuthManagement':cdot11SecAuthManagement,_A2:cdot11SecLocalAuthServerEnabled,'cdot11SecStatistics':cdot11SecStatistics,'cdot11SecVlanManagement':cdot11SecVlanManagement,'cdot11SecVlanNameTable':cdot11SecVlanNameTable,'cdot11SecVlanNameEntry':cdot11SecVlanNameEntry,_c:cdot11SecVlanName,_A3:cdot11SecVlanNameId,_A4:cdot11SecVlanNameRowStatus,'ciscoDot11SsidSecMIBConformance':ciscoDot11SsidSecMIBConformance,'ciscoDot11SsidSecMIBCompliances':ciscoDot11SsidSecMIBCompliances,'ciscoDot11SsidSecCompliance':ciscoDot11SsidSecCompliance,'ciscoDot11SsidSecComplianceRev1':ciscoDot11SsidSecComplianceRev1,'ciscoDot11SsidSecMIBGroups':ciscoDot11SsidSecMIBGroups,_P:cdot11SecSsidManagementGroup,_Q:cdot11SsidAuthenticationGroup,_R:cdot11ModuleAuthenticationGroup,_S:cdot11SecVlanManagementGroup,_T:cdot11MbssidSupportGroup,_AC:cdot11SecSsidBackupVlanManagementGroup})