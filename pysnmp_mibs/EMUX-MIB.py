_BX='dyingGaspTrapsGroup'
_BW='tdmRedundancyGroup'
_BV='hostsGroup'
_BU='ipstoredGroup'
_BT='ipcurrentGroup'
_BS='vlanGroup'
_BR='e1trapsGroup'
_BQ='tdmGroupStat'
_BP='e1GroupStat'
_BO='muxBaseGroup'
_BN='dyingGaspTrap'
_BM='tdmLinkUp'
_BL='tdmLinkDown'
_BK='e1LinkChange'
_BJ='tdmRedundancyVLANPri'
_BI='tdmRedundancyUseIP'
_BH='tdmRedundancyDSCP'
_BG='tdmRedundancyVLANID'
_BF='tdmRedundancyRemoteIP'
_BE='tdmRedundancyEnabled'
_BD='hostNetwork'
_BC='sSecondaryMAC'
_BB='sPhysicalAddr'
_BA='sNetTrustUnkVlan'
_B9='sNetTrustLocal'
_B8='sNetTrustAll'
_B7='sDefaultVlanPri'
_B6='sDefaultVlan'
_B5='sNetGateway'
_B4='cSecondaryMAC'
_B3='cPhysicalAddr'
_B2='cNetTrustUnkVlan'
_B1='cNetTrustLocal'
_B0='cNetTrustAll'
_A_='cDefaultVlanPri'
_Az='cDefaultVlan'
_Ay='cNetGateway'
_Ax='tdmBandwidth'
_Aw='tdmTxDiscards'
_Av='tdmRecommenedJB'
_Au='tdmAvgSpeed'
_At='tdmFinish'
_As='tdmRestored'
_Ar='tdmLostReq'
_Aq='tdmSlipRem'
_Ap='tdmSlipAdd'
_Ao='tdmResync'
_An='tdmInterp'
_Am='tdmIgnored'
_Al='tdmResend'
_Ak='e1txCRC4Rem'
_Aj='e1txCRC4Sec'
_Ai='e1txOkCnt'
_Ah='e1rxCRC4Rem'
_Ag='e1rxCRC4Sec'
_Af='e1rxFastErr'
_Ae='e1rxRareErr'
_Ad='e1rxCodeErr'
_Ac='e1rxOkCnt'
_Ab='tdmProtocol'
_Aa='tdmInterpMode'
_AZ='tdmConstSpeed'
_AY='tdmDoubleSend'
_AX='tdmDescription'
_AW='tdmKeyFrameInterval'
_AV='tdmCompression'
_AU='tdmUsedTimeSlots'
_AT='tdmMaxTimeout'
_AS='tdmUseConstSpeed'
_AR='tdmConfigured'
_AQ='tdmSpeedRegualator'
_AP='tdmRemoteLoop'
_AO='tdmOriginalChannel'
_AN='tdmOriginalMAC'
_AM='tdmOriginalIP'
_AL='tdmRedirectedChannel'
_AK='tdmRedirectedMAC'
_AJ='tdmRedirectedIP'
_AI='tdmLostRequest'
_AH='tdmVLANPri'
_AG='tdmVLANID'
_AF='tdmRemoteTSMask'
_AE='tdmLocalTSMask'
_AD='tdmCurrentJBSize'
_AC='tdmHasData'
_AB='tdmCurrentTimeout'
_AA='tdmJBSize'
_A9='tdmFrameSize'
_A8='tdmResetConfig'
_A7='tdmStatus'
_A6='e1PRBSCheck'
_A5='e1NoLogEvents'
_A4='e1SignalLevel'
_A3='e1LongLine'
_A2='e1RXSpeed'
_A1='e1TestFrameRTT'
_A0='e1TxSpeed'
_z='e1SyncSource'
_y='e1SendType'
_x='e1RecvUnframed'
_w='e1LocalLoopback'
_v='e1ChResetConfig'
_u='e1ChLinkEnable'
_t='e1ChLinkStatus'
_s='e1ChStatus'
_r='e1Number'
_q='oldSysID'
_p='sysVendor'
_o='sysUpdate'
_n='sysSaveConfig'
_m='sysLicenseValid'
_l='sysDateTime'
_k='sysReset'
_j='devLocation'
_i='sysDevname'
_h='manContact'
_g='hwDescr'
_f='sysOSVer'
_e='sysHWVer'
_d='adcIndex'
_c='tdmRedundancyIndex'
_b='tdmStChIndex'
_a='e1StChIndex'
_Z='dontuse'
_Y='tdmChIndex'
_X='e1ChIndex'
_W='hostIndex'
_V='e1SendStatus'
_U='e1RecvStatus'
_T='vlanID'
_S='ais'
_R='tdmAdminStatus'
_Q='tdmLinkStatus'
_P='times'
_O='down'
_N='ms'
_M='no'
_L='yes'
_K='ppb'
_J='not-accessible'
_I='disabled'
_H='enabled'
_G='frames'
_F='s'
_E='Integer32'
_D='read-write'
_C='read-only'
_B='EMUX-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dBridge,=mibBuilder.importSymbols('BRIDGE-MIB','dot1dBridge')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
rstpMIB,=mibBuilder.importSymbols('RSTP-MIB','rstpMIB')
usmStats,=mibBuilder.importSymbols('SNMP-USER-BASED-SM-MIB','usmStats')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','TextualConvention')
Float,=mibBuilder.importSymbols('UCD-SNMP-MIB','Float')
nsc=ModuleIdentity((1,3,6,1,4,1,42926))
if mibBuilder.loadTexts:nsc.setRevisions(('2018-07-31 00:00','2018-01-18 00:00','2017-06-01 00:00','2017-03-02 00:00','2016-03-25 00:00','2015-06-03 00:00','2015-01-15 00:00','2012-09-06 00:00'))
class TimeSlotMask(TextualConvention,OctetString):status=_A;displayHint='1x:'
class E1Status(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('nos',0),(_S,1),('azs',2),('los',3),('rai',4),('prbserr',5),('testerr',6),('loopdet',7),('txlock',8),('codeerr',9),('fastpulseerr',10),('rarepulseerr',11),('mfaserr',12),('rcrc4err',13),('crc4err',14),('ok',16)))
class CRC4Status(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('check',0),('send',1),('reicheck',2),('reisend',3)))
_Emux_ObjectIdentity=ObjectIdentity
emux=_Emux_ObjectIdentity((1,3,6,1,4,1,42926,2))
_General_ObjectIdentity=ObjectIdentity
general=_General_ObjectIdentity((1,3,6,1,4,1,42926,2,3))
_Basic_ObjectIdentity=ObjectIdentity
basic=_Basic_ObjectIdentity((1,3,6,1,4,1,42926,2,3,1))
_SysHWVer_Type=DisplayString
_SysHWVer_Object=MibScalar
sysHWVer=_SysHWVer_Object((1,3,6,1,4,1,42926,2,3,1,1),_SysHWVer_Type())
sysHWVer.setMaxAccess(_C)
if mibBuilder.loadTexts:sysHWVer.setStatus(_A)
_SysOSVer_Type=DisplayString
_SysOSVer_Object=MibScalar
sysOSVer=_SysOSVer_Object((1,3,6,1,4,1,42926,2,3,1,2),_SysOSVer_Type())
sysOSVer.setMaxAccess(_C)
if mibBuilder.loadTexts:sysOSVer.setStatus(_A)
_HwDescr_Type=DisplayString
_HwDescr_Object=MibScalar
hwDescr=_HwDescr_Object((1,3,6,1,4,1,42926,2,3,1,3),_HwDescr_Type())
hwDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:hwDescr.setStatus(_A)
_ManContact_Type=DisplayString
_ManContact_Object=MibScalar
manContact=_ManContact_Object((1,3,6,1,4,1,42926,2,3,1,4),_ManContact_Type())
manContact.setMaxAccess(_D)
if mibBuilder.loadTexts:manContact.setStatus(_A)
_SysDevname_Type=DisplayString
_SysDevname_Object=MibScalar
sysDevname=_SysDevname_Object((1,3,6,1,4,1,42926,2,3,1,5),_SysDevname_Type())
sysDevname.setMaxAccess(_C)
if mibBuilder.loadTexts:sysDevname.setStatus(_A)
_DevLocation_Type=DisplayString
_DevLocation_Object=MibScalar
devLocation=_DevLocation_Object((1,3,6,1,4,1,42926,2,3,1,6),_DevLocation_Type())
devLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:devLocation.setStatus(_A)
_SysReset_Type=DisplayString
_SysReset_Object=MibScalar
sysReset=_SysReset_Object((1,3,6,1,4,1,42926,2,3,1,7),_SysReset_Type())
sysReset.setMaxAccess(_D)
if mibBuilder.loadTexts:sysReset.setStatus(_A)
_SysID_Type=DisplayString
_SysID_Object=MibScalar
sysID=_SysID_Object((1,3,6,1,4,1,42926,2,3,1,8),_SysID_Type())
sysID.setMaxAccess(_C)
if mibBuilder.loadTexts:sysID.setStatus(_A)
_SysDateTime_Type=DisplayString
_SysDateTime_Object=MibScalar
sysDateTime=_SysDateTime_Object((1,3,6,1,4,1,42926,2,3,1,9),_SysDateTime_Type())
sysDateTime.setMaxAccess(_D)
if mibBuilder.loadTexts:sysDateTime.setStatus(_A)
class _SysLicenseValid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),('invalid',2)))
_SysLicenseValid_Type.__name__=_E
_SysLicenseValid_Object=MibScalar
sysLicenseValid=_SysLicenseValid_Object((1,3,6,1,4,1,42926,2,3,1,10),_SysLicenseValid_Type())
sysLicenseValid.setMaxAccess(_C)
if mibBuilder.loadTexts:sysLicenseValid.setStatus(_A)
_SysSaveConfig_Type=DisplayString
_SysSaveConfig_Object=MibScalar
sysSaveConfig=_SysSaveConfig_Object((1,3,6,1,4,1,42926,2,3,1,11),_SysSaveConfig_Type())
sysSaveConfig.setMaxAccess(_D)
if mibBuilder.loadTexts:sysSaveConfig.setStatus(_A)
_SysUpdate_Type=DisplayString
_SysUpdate_Object=MibScalar
sysUpdate=_SysUpdate_Object((1,3,6,1,4,1,42926,2,3,1,12),_SysUpdate_Type())
sysUpdate.setMaxAccess(_D)
if mibBuilder.loadTexts:sysUpdate.setStatus(_A)
_SysVendor_Type=DisplayString
_SysVendor_Object=MibScalar
sysVendor=_SysVendor_Object((1,3,6,1,4,1,42926,2,3,1,13),_SysVendor_Type())
sysVendor.setMaxAccess(_C)
if mibBuilder.loadTexts:sysVendor.setStatus(_A)
_OldSysID_Type=DisplayString
_OldSysID_Object=MibScalar
oldSysID=_OldSysID_Object((1,3,6,1,4,1,42926,2,3,1,14),_OldSysID_Type())
oldSysID.setMaxAccess(_C)
if mibBuilder.loadTexts:oldSysID.setStatus(_A)
_Muxip_ObjectIdentity=ObjectIdentity
muxip=_Muxip_ObjectIdentity((1,3,6,1,4,1,42926,2,3,2))
_Ipcurrent_ObjectIdentity=ObjectIdentity
ipcurrent=_Ipcurrent_ObjectIdentity((1,3,6,1,4,1,42926,2,3,2,1))
_CNetIP_Type=IpAddress
_CNetIP_Object=MibScalar
cNetIP=_CNetIP_Object((1,3,6,1,4,1,42926,2,3,2,1,1),_CNetIP_Type())
cNetIP.setMaxAccess(_D)
if mibBuilder.loadTexts:cNetIP.setStatus(_A)
_CNetMask_Type=IpAddress
_CNetMask_Object=MibScalar
cNetMask=_CNetMask_Object((1,3,6,1,4,1,42926,2,3,2,1,2),_CNetMask_Type())
cNetMask.setMaxAccess(_D)
if mibBuilder.loadTexts:cNetMask.setStatus(_A)
_CNetGateway_Type=IpAddress
_CNetGateway_Object=MibScalar
cNetGateway=_CNetGateway_Object((1,3,6,1,4,1,42926,2,3,2,1,3),_CNetGateway_Type())
cNetGateway.setMaxAccess(_D)
if mibBuilder.loadTexts:cNetGateway.setStatus(_A)
_CDefaultVlan_Type=Integer32
_CDefaultVlan_Object=MibScalar
cDefaultVlan=_CDefaultVlan_Object((1,3,6,1,4,1,42926,2,3,2,1,4),_CDefaultVlan_Type())
cDefaultVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:cDefaultVlan.setStatus(_A)
_CDefaultVlanPri_Type=Integer32
_CDefaultVlanPri_Object=MibScalar
cDefaultVlanPri=_CDefaultVlanPri_Object((1,3,6,1,4,1,42926,2,3,2,1,5),_CDefaultVlanPri_Type())
cDefaultVlanPri.setMaxAccess(_D)
if mibBuilder.loadTexts:cDefaultVlanPri.setStatus(_A)
class _CNetTrustAll_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_CNetTrustAll_Type.__name__=_E
_CNetTrustAll_Object=MibScalar
cNetTrustAll=_CNetTrustAll_Object((1,3,6,1,4,1,42926,2,3,2,1,6),_CNetTrustAll_Type())
cNetTrustAll.setMaxAccess(_D)
if mibBuilder.loadTexts:cNetTrustAll.setStatus(_A)
class _CNetTrustLocal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_CNetTrustLocal_Type.__name__=_E
_CNetTrustLocal_Object=MibScalar
cNetTrustLocal=_CNetTrustLocal_Object((1,3,6,1,4,1,42926,2,3,2,1,7),_CNetTrustLocal_Type())
cNetTrustLocal.setMaxAccess(_D)
if mibBuilder.loadTexts:cNetTrustLocal.setStatus(_A)
class _CNetTrustUnkVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_CNetTrustUnkVlan_Type.__name__=_E
_CNetTrustUnkVlan_Object=MibScalar
cNetTrustUnkVlan=_CNetTrustUnkVlan_Object((1,3,6,1,4,1,42926,2,3,2,1,8),_CNetTrustUnkVlan_Type())
cNetTrustUnkVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:cNetTrustUnkVlan.setStatus(_A)
_CDNS1_Type=IpAddress
_CDNS1_Object=MibScalar
cDNS1=_CDNS1_Object((1,3,6,1,4,1,42926,2,3,2,1,9),_CDNS1_Type())
cDNS1.setMaxAccess(_D)
if mibBuilder.loadTexts:cDNS1.setStatus(_A)
_CPhysicalAddr_Type=MacAddress
_CPhysicalAddr_Object=MibScalar
cPhysicalAddr=_CPhysicalAddr_Object((1,3,6,1,4,1,42926,2,3,2,1,10),_CPhysicalAddr_Type())
cPhysicalAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cPhysicalAddr.setStatus(_A)
_CSecondaryMAC_Type=MacAddress
_CSecondaryMAC_Object=MibScalar
cSecondaryMAC=_CSecondaryMAC_Object((1,3,6,1,4,1,42926,2,3,2,1,11),_CSecondaryMAC_Type())
cSecondaryMAC.setMaxAccess(_C)
if mibBuilder.loadTexts:cSecondaryMAC.setStatus(_A)
_Ipstored_ObjectIdentity=ObjectIdentity
ipstored=_Ipstored_ObjectIdentity((1,3,6,1,4,1,42926,2,3,2,2))
_SNetIP_Type=IpAddress
_SNetIP_Object=MibScalar
sNetIP=_SNetIP_Object((1,3,6,1,4,1,42926,2,3,2,2,1),_SNetIP_Type())
sNetIP.setMaxAccess(_D)
if mibBuilder.loadTexts:sNetIP.setStatus(_A)
_SNetMask_Type=IpAddress
_SNetMask_Object=MibScalar
sNetMask=_SNetMask_Object((1,3,6,1,4,1,42926,2,3,2,2,2),_SNetMask_Type())
sNetMask.setMaxAccess(_D)
if mibBuilder.loadTexts:sNetMask.setStatus(_A)
_SNetGateway_Type=IpAddress
_SNetGateway_Object=MibScalar
sNetGateway=_SNetGateway_Object((1,3,6,1,4,1,42926,2,3,2,2,3),_SNetGateway_Type())
sNetGateway.setMaxAccess(_D)
if mibBuilder.loadTexts:sNetGateway.setStatus(_A)
_SDefaultVlan_Type=Integer32
_SDefaultVlan_Object=MibScalar
sDefaultVlan=_SDefaultVlan_Object((1,3,6,1,4,1,42926,2,3,2,2,4),_SDefaultVlan_Type())
sDefaultVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:sDefaultVlan.setStatus(_A)
_SDefaultVlanPri_Type=Integer32
_SDefaultVlanPri_Object=MibScalar
sDefaultVlanPri=_SDefaultVlanPri_Object((1,3,6,1,4,1,42926,2,3,2,2,5),_SDefaultVlanPri_Type())
sDefaultVlanPri.setMaxAccess(_D)
if mibBuilder.loadTexts:sDefaultVlanPri.setStatus(_A)
class _SNetTrustAll_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_SNetTrustAll_Type.__name__=_E
_SNetTrustAll_Object=MibScalar
sNetTrustAll=_SNetTrustAll_Object((1,3,6,1,4,1,42926,2,3,2,2,6),_SNetTrustAll_Type())
sNetTrustAll.setMaxAccess(_D)
if mibBuilder.loadTexts:sNetTrustAll.setStatus(_A)
class _SNetTrustLocal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_SNetTrustLocal_Type.__name__=_E
_SNetTrustLocal_Object=MibScalar
sNetTrustLocal=_SNetTrustLocal_Object((1,3,6,1,4,1,42926,2,3,2,2,7),_SNetTrustLocal_Type())
sNetTrustLocal.setMaxAccess(_D)
if mibBuilder.loadTexts:sNetTrustLocal.setStatus(_A)
class _SNetTrustUnkVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_SNetTrustUnkVlan_Type.__name__=_E
_SNetTrustUnkVlan_Object=MibScalar
sNetTrustUnkVlan=_SNetTrustUnkVlan_Object((1,3,6,1,4,1,42926,2,3,2,2,8),_SNetTrustUnkVlan_Type())
sNetTrustUnkVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:sNetTrustUnkVlan.setStatus(_A)
_SDNS1_Type=IpAddress
_SDNS1_Object=MibScalar
sDNS1=_SDNS1_Object((1,3,6,1,4,1,42926,2,3,2,2,9),_SDNS1_Type())
sDNS1.setMaxAccess(_D)
if mibBuilder.loadTexts:sDNS1.setStatus(_A)
_SPhysicalAddr_Type=MacAddress
_SPhysicalAddr_Object=MibScalar
sPhysicalAddr=_SPhysicalAddr_Object((1,3,6,1,4,1,42926,2,3,2,2,10),_SPhysicalAddr_Type())
sPhysicalAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:sPhysicalAddr.setStatus(_A)
_SSecondaryMAC_Type=MacAddress
_SSecondaryMAC_Object=MibScalar
sSecondaryMAC=_SSecondaryMAC_Object((1,3,6,1,4,1,42926,2,3,2,2,11),_SSecondaryMAC_Type())
sSecondaryMAC.setMaxAccess(_C)
if mibBuilder.loadTexts:sSecondaryMAC.setStatus(_A)
_HostsTable_Object=MibTable
hostsTable=_HostsTable_Object((1,3,6,1,4,1,42926,2,3,2,3))
if mibBuilder.loadTexts:hostsTable.setStatus(_A)
_HostsTableEntry_Object=MibTableRow
hostsTableEntry=_HostsTableEntry_Object((1,3,6,1,4,1,42926,2,3,2,3,1))
hostsTableEntry.setIndexNames((0,_B,_W))
if mibBuilder.loadTexts:hostsTableEntry.setStatus(_A)
class _HostIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_HostIndex_Type.__name__=_E
_HostIndex_Object=MibTableColumn
hostIndex=_HostIndex_Object((1,3,6,1,4,1,42926,2,3,2,3,1,1),_HostIndex_Type())
hostIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:hostIndex.setStatus(_A)
_HostNetwork_Type=IpAddress
_HostNetwork_Object=MibTableColumn
hostNetwork=_HostNetwork_Object((1,3,6,1,4,1,42926,2,3,2,3,1,2),_HostNetwork_Type())
hostNetwork.setMaxAccess(_D)
if mibBuilder.loadTexts:hostNetwork.setStatus(_A)
_HostMask_Type=IpAddress
_HostMask_Object=MibTableColumn
hostMask=_HostMask_Object((1,3,6,1,4,1,42926,2,3,2,3,1,3),_HostMask_Type())
hostMask.setMaxAccess(_D)
if mibBuilder.loadTexts:hostMask.setStatus(_A)
_E1_ObjectIdentity=ObjectIdentity
e1=_E1_ObjectIdentity((1,3,6,1,4,1,42926,2,18))
_E1Number_Type=Integer32
_E1Number_Object=MibScalar
e1Number=_E1Number_Object((1,3,6,1,4,1,42926,2,18,1),_E1Number_Type())
e1Number.setMaxAccess(_C)
if mibBuilder.loadTexts:e1Number.setStatus(_A)
_E1ConfigTable_Object=MibTable
e1ConfigTable=_E1ConfigTable_Object((1,3,6,1,4,1,42926,2,18,6))
if mibBuilder.loadTexts:e1ConfigTable.setStatus(_A)
_E1ConfigTableEntry_Object=MibTableRow
e1ConfigTableEntry=_E1ConfigTableEntry_Object((1,3,6,1,4,1,42926,2,18,6,1))
e1ConfigTableEntry.setIndexNames((0,_B,_X))
if mibBuilder.loadTexts:e1ConfigTableEntry.setStatus(_A)
class _E1ChIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_E1ChIndex_Type.__name__=_E
_E1ChIndex_Object=MibTableColumn
e1ChIndex=_E1ChIndex_Object((1,3,6,1,4,1,42926,2,18,6,1,1),_E1ChIndex_Type())
e1ChIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:e1ChIndex.setStatus(_A)
_E1ChStatus_Type=DisplayString
_E1ChStatus_Object=MibTableColumn
e1ChStatus=_E1ChStatus_Object((1,3,6,1,4,1,42926,2,18,6,1,2),_E1ChStatus_Type())
e1ChStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:e1ChStatus.setStatus(_A)
class _E1ChLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),(_O,2)))
_E1ChLinkStatus_Type.__name__=_E
_E1ChLinkStatus_Object=MibTableColumn
e1ChLinkStatus=_E1ChLinkStatus_Object((1,3,6,1,4,1,42926,2,18,6,1,3),_E1ChLinkStatus_Type())
e1ChLinkStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:e1ChLinkStatus.setStatus(_A)
class _E1ChLinkEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_E1ChLinkEnable_Type.__name__=_E
_E1ChLinkEnable_Object=MibTableColumn
e1ChLinkEnable=_E1ChLinkEnable_Object((1,3,6,1,4,1,42926,2,18,6,1,4),_E1ChLinkEnable_Type())
e1ChLinkEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:e1ChLinkEnable.setStatus(_A)
_E1ChResetConfig_Type=DisplayString
_E1ChResetConfig_Object=MibTableColumn
e1ChResetConfig=_E1ChResetConfig_Object((1,3,6,1,4,1,42926,2,18,6,1,5),_E1ChResetConfig_Type())
e1ChResetConfig.setMaxAccess(_D)
if mibBuilder.loadTexts:e1ChResetConfig.setStatus(_A)
class _E1LocalLoopback_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_E1LocalLoopback_Type.__name__=_E
_E1LocalLoopback_Object=MibTableColumn
e1LocalLoopback=_E1LocalLoopback_Object((1,3,6,1,4,1,42926,2,18,6,1,7),_E1LocalLoopback_Type())
e1LocalLoopback.setMaxAccess(_D)
if mibBuilder.loadTexts:e1LocalLoopback.setStatus(_A)
class _E1RecvUnframed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_E1RecvUnframed_Type.__name__=_E
_E1RecvUnframed_Object=MibTableColumn
e1RecvUnframed=_E1RecvUnframed_Object((1,3,6,1,4,1,42926,2,18,6,1,8),_E1RecvUnframed_Type())
e1RecvUnframed.setMaxAccess(_D)
if mibBuilder.loadTexts:e1RecvUnframed.setStatus(_A)
class _E1SendType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_S,0),('azs',1),('prbs',2),('testFrames',3),('tdmop',4)))
_E1SendType_Type.__name__=_E
_E1SendType_Object=MibTableColumn
e1SendType=_E1SendType_Object((1,3,6,1,4,1,42926,2,18,6,1,10),_E1SendType_Type())
e1SendType.setMaxAccess(_D)
if mibBuilder.loadTexts:e1SendType.setStatus(_A)
class _E1SyncSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(-1));namedValues=NamedValues(('restore',-1))
_E1SyncSource_Type.__name__=_E
_E1SyncSource_Object=MibTableColumn
e1SyncSource=_E1SyncSource_Object((1,3,6,1,4,1,42926,2,18,6,1,11),_E1SyncSource_Type())
e1SyncSource.setMaxAccess(_D)
if mibBuilder.loadTexts:e1SyncSource.setStatus(_A)
_E1TxSpeed_Type=Integer32
_E1TxSpeed_Object=MibTableColumn
e1TxSpeed=_E1TxSpeed_Object((1,3,6,1,4,1,42926,2,18,6,1,15),_E1TxSpeed_Type())
e1TxSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:e1TxSpeed.setStatus(_A)
if mibBuilder.loadTexts:e1TxSpeed.setUnits(_K)
_E1TestFrameRTT_Type=Gauge32
_E1TestFrameRTT_Object=MibTableColumn
e1TestFrameRTT=_E1TestFrameRTT_Object((1,3,6,1,4,1,42926,2,18,6,1,16),_E1TestFrameRTT_Type())
e1TestFrameRTT.setMaxAccess(_C)
if mibBuilder.loadTexts:e1TestFrameRTT.setStatus(_A)
if mibBuilder.loadTexts:e1TestFrameRTT.setUnits('UI')
_E1RecvStatus_Type=E1Status
_E1RecvStatus_Object=MibTableColumn
e1RecvStatus=_E1RecvStatus_Object((1,3,6,1,4,1,42926,2,18,6,1,17),_E1RecvStatus_Type())
e1RecvStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:e1RecvStatus.setStatus(_A)
_E1SendStatus_Type=E1Status
_E1SendStatus_Object=MibTableColumn
e1SendStatus=_E1SendStatus_Object((1,3,6,1,4,1,42926,2,18,6,1,18),_E1SendStatus_Type())
e1SendStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:e1SendStatus.setStatus(_A)
_E1RXSpeed_Type=Integer32
_E1RXSpeed_Object=MibTableColumn
e1RXSpeed=_E1RXSpeed_Object((1,3,6,1,4,1,42926,2,18,6,1,21),_E1RXSpeed_Type())
e1RXSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:e1RXSpeed.setStatus(_A)
if mibBuilder.loadTexts:e1RXSpeed.setUnits(_K)
class _E1LongLine_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_E1LongLine_Type.__name__=_E
_E1LongLine_Object=MibTableColumn
e1LongLine=_E1LongLine_Object((1,3,6,1,4,1,42926,2,18,6,1,22),_E1LongLine_Type())
e1LongLine.setMaxAccess(_D)
if mibBuilder.loadTexts:e1LongLine.setStatus(_A)
_E1SignalLevel_Type=DisplayString
_E1SignalLevel_Object=MibTableColumn
e1SignalLevel=_E1SignalLevel_Object((1,3,6,1,4,1,42926,2,18,6,1,23),_E1SignalLevel_Type())
e1SignalLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:e1SignalLevel.setStatus(_A)
_E1NoLogEvents_Type=E1Status
_E1NoLogEvents_Object=MibTableColumn
e1NoLogEvents=_E1NoLogEvents_Object((1,3,6,1,4,1,42926,2,18,6,1,24),_E1NoLogEvents_Type())
e1NoLogEvents.setMaxAccess(_D)
if mibBuilder.loadTexts:e1NoLogEvents.setStatus(_A)
_E1CRC4_Type=CRC4Status
_E1CRC4_Object=MibTableColumn
e1CRC4=_E1CRC4_Object((1,3,6,1,4,1,42926,2,18,6,1,25),_E1CRC4_Type())
e1CRC4.setMaxAccess(_D)
if mibBuilder.loadTexts:e1CRC4.setStatus(_A)
class _E1PRBSCheck_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_E1PRBSCheck_Type.__name__=_E
_E1PRBSCheck_Object=MibTableColumn
e1PRBSCheck=_E1PRBSCheck_Object((1,3,6,1,4,1,42926,2,18,6,1,26),_E1PRBSCheck_Type())
e1PRBSCheck.setMaxAccess(_D)
if mibBuilder.loadTexts:e1PRBSCheck.setStatus(_A)
_TdmConfigTable_Object=MibTable
tdmConfigTable=_TdmConfigTable_Object((1,3,6,1,4,1,42926,2,18,7))
if mibBuilder.loadTexts:tdmConfigTable.setStatus(_A)
_TdmConfigTableEntry_Object=MibTableRow
tdmConfigTableEntry=_TdmConfigTableEntry_Object((1,3,6,1,4,1,42926,2,18,7,1))
tdmConfigTableEntry.setIndexNames((0,_B,_Y))
if mibBuilder.loadTexts:tdmConfigTableEntry.setStatus(_A)
class _TdmChIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_TdmChIndex_Type.__name__=_E
_TdmChIndex_Object=MibTableColumn
tdmChIndex=_TdmChIndex_Object((1,3,6,1,4,1,42926,2,18,7,1,1),_TdmChIndex_Type())
tdmChIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:tdmChIndex.setStatus(_A)
_TdmStatus_Type=DisplayString
_TdmStatus_Object=MibTableColumn
tdmStatus=_TdmStatus_Object((1,3,6,1,4,1,42926,2,18,7,1,2),_TdmStatus_Type())
tdmStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tdmStatus.setStatus(_A)
class _TdmLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),(_O,2)))
_TdmLinkStatus_Type.__name__=_E
_TdmLinkStatus_Object=MibTableColumn
tdmLinkStatus=_TdmLinkStatus_Object((1,3,6,1,4,1,42926,2,18,7,1,3),_TdmLinkStatus_Type())
tdmLinkStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tdmLinkStatus.setStatus(_A)
class _TdmAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('listen',0),('connect',1),('blocked',2),('alwaysSend',3)))
_TdmAdminStatus_Type.__name__=_E
_TdmAdminStatus_Object=MibTableColumn
tdmAdminStatus=_TdmAdminStatus_Object((1,3,6,1,4,1,42926,2,18,7,1,5),_TdmAdminStatus_Type())
tdmAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:tdmAdminStatus.setStatus(_A)
_TdmResetConfig_Type=DisplayString
_TdmResetConfig_Object=MibTableColumn
tdmResetConfig=_TdmResetConfig_Object((1,3,6,1,4,1,42926,2,18,7,1,7),_TdmResetConfig_Type())
tdmResetConfig.setMaxAccess(_D)
if mibBuilder.loadTexts:tdmResetConfig.setStatus(_A)
_TdmFrameSize_Type=Integer32
_TdmFrameSize_Object=MibTableColumn
tdmFrameSize=_TdmFrameSize_Object((1,3,6,1,4,1,42926,2,18,7,1,8),_TdmFrameSize_Type())
tdmFrameSize.setMaxAccess(_D)
if mibBuilder.loadTexts:tdmFrameSize.setStatus(_A)
if mibBuilder.loadTexts:tdmFrameSize.setUnits('1/2ms')
_TdmJBSize_Type=Integer32
_TdmJBSize_Object=MibTableColumn
tdmJBSize=_TdmJBSize_Object((1,3,6,1,4,1,42926,2,18,7,1,9),_TdmJBSize_Type())
tdmJBSize.setMaxAccess(_D)
if mibBuilder.loadTexts:tdmJBSize.setStatus(_A)
if mibBuilder.loadTexts:tdmJBSize.setUnits(_N)
_TdmCurrentTimeout_Type=Integer32
_TdmCurrentTimeout_Object=MibTableColumn
tdmCurrentTimeout=_TdmCurrentTimeout_Object((1,3,6,1,4,1,42926,2,18,7,1,10),_TdmCurrentTimeout_Type())
tdmCurrentTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:tdmCurrentTimeout.setStatus(_A)
if mibBuilder.loadTexts:tdmCurrentTimeout.setUnits(_N)
class _TdmMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_O,0),('waitingSync',1),('accumulating',2),('working',3)))
_TdmMode_Type.__name__=_E
_TdmMode_Object=MibTableColumn
tdmMode=_TdmMode_Object((1,3,6,1,4,1,42926,2,18,7,1,11),_TdmMode_Type())
tdmMode.setMaxAccess(_C)
if mibBuilder.loadTexts:tdmMode.setStatus(_A)
class _TdmHasData_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ok',1),('nodata',2)))
_TdmHasData_Type.__name__=_E
_TdmHasData_Object=MibTableColumn
tdmHasData=_TdmHasData_Object((1,3,6,1,4,1,42926,2,18,7,1,12),_TdmHasData_Type())
tdmHasData.setMaxAccess(_C)
if mibBuilder.loadTexts:tdmHasData.setStatus(_A)
_TdmCurrentJBSize_Type=Integer32
_TdmCurrentJBSize_Object=MibTableColumn
tdmCurrentJBSize=_TdmCurrentJBSize_Object((1,3,6,1,4,1,42926,2,18,7,1,13),_TdmCurrentJBSize_Type())
tdmCurrentJBSize.setMaxAccess(_C)
if mibBuilder.loadTexts:tdmCurrentJBSize.setStatus(_A)
if mibBuilder.loadTexts:tdmCurrentJBSize.setUnits('us')
_TdmLocalTSMask_Type=TimeSlotMask
_TdmLocalTSMask_Object=MibTableColumn
tdmLocalTSMask=_TdmLocalTSMask_Object((1,3,6,1,4,1,42926,2,18,7,1,14),_TdmLocalTSMask_Type())
tdmLocalTSMask.setMaxAccess(_C)
if mibBuilder.loadTexts:tdmLocalTSMask.setStatus(_A)
_TdmRemoteTSMask_Type=TimeSlotMask
_TdmRemoteTSMask_Object=MibTableColumn
tdmRemoteTSMask=_TdmRemoteTSMask_Object((1,3,6,1,4,1,42926,2,18,7,1,15),_TdmRemoteTSMask_Type())
tdmRemoteTSMask.setMaxAccess(_C)
if mibBuilder.loadTexts:tdmRemoteTSMask.setStatus(_A)
_TdmVLANID_Type=Integer32
_TdmVLANID_Object=MibTableColumn
tdmVLANID=_TdmVLANID_Object((1,3,6,1,4,1,42926,2,18,7,1,16),_TdmVLANID_Type())
tdmVLANID.setMaxAccess(_D)
if mibBuilder.loadTexts:tdmVLANID.setStatus(_A)
_TdmVLANPri_Type=Integer32
_TdmVLANPri_Object=MibTableColumn
tdmVLANPri=_TdmVLANPri_Object((1,3,6,1,4,1,42926,2,18,7,1,17),_TdmVLANPri_Type())
tdmVLANPri.setMaxAccess(_D)
if mibBuilder.loadTexts:tdmVLANPri.setStatus(_A)
class _TdmUseIP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('use',1),(_Z,2)))
_TdmUseIP_Type.__name__=_E
_TdmUseIP_Object=MibTableColumn
tdmUseIP=_TdmUseIP_Object((1,3,6,1,4,1,42926,2,18,7,1,18),_TdmUseIP_Type())
tdmUseIP.setMaxAccess(_D)
if mibBuilder.loadTexts:tdmUseIP.setStatus(_A)
class _TdmLostRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('request',1),('ignore',2)))
_TdmLostRequest_Type.__name__=_E
_TdmLostRequest_Object=MibTableColumn
tdmLostRequest=_TdmLostRequest_Object((1,3,6,1,4,1,42926,2,18,7,1,19),_TdmLostRequest_Type())
tdmLostRequest.setMaxAccess(_D)
if mibBuilder.loadTexts:tdmLostRequest.setStatus(_A)
_TdmRedirectedIP_Type=IpAddress
_TdmRedirectedIP_Object=MibTableColumn
tdmRedirectedIP=_TdmRedirectedIP_Object((1,3,6,1,4,1,42926,2,18,7,1,20),_TdmRedirectedIP_Type())
tdmRedirectedIP.setMaxAccess(_C)
if mibBuilder.loadTexts:tdmRedirectedIP.setStatus(_A)
_TdmRedirectedMAC_Type=MacAddress
_TdmRedirectedMAC_Object=MibTableColumn
tdmRedirectedMAC=_TdmRedirectedMAC_Object((1,3,6,1,4,1,42926,2,18,7,1,21),_TdmRedirectedMAC_Type())
tdmRedirectedMAC.setMaxAccess(_C)
if mibBuilder.loadTexts:tdmRedirectedMAC.setStatus(_A)
_TdmRedirectedChannel_Type=Integer32
_TdmRedirectedChannel_Object=MibTableColumn
tdmRedirectedChannel=_TdmRedirectedChannel_Object((1,3,6,1,4,1,42926,2,18,7,1,22),_TdmRedirectedChannel_Type())
tdmRedirectedChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:tdmRedirectedChannel.setStatus(_A)
_TdmOriginalIP_Type=IpAddress
_TdmOriginalIP_Object=MibTableColumn
tdmOriginalIP=_TdmOriginalIP_Object((1,3,6,1,4,1,42926,2,18,7,1,23),_TdmOriginalIP_Type())
tdmOriginalIP.setMaxAccess(_D)
if mibBuilder.loadTexts:tdmOriginalIP.setStatus(_A)
_TdmOriginalMAC_Type=MacAddress
_TdmOriginalMAC_Object=MibTableColumn
tdmOriginalMAC=_TdmOriginalMAC_Object((1,3,6,1,4,1,42926,2,18,7,1,24),_TdmOriginalMAC_Type())
tdmOriginalMAC.setMaxAccess(_D)
if mibBuilder.loadTexts:tdmOriginalMAC.setStatus(_A)
_TdmOriginalChannel_Type=Integer32
_TdmOriginalChannel_Object=MibTableColumn
tdmOriginalChannel=_TdmOriginalChannel_Object((1,3,6,1,4,1,42926,2,18,7,1,25),_TdmOriginalChannel_Type())
tdmOriginalChannel.setMaxAccess(_D)
if mibBuilder.loadTexts:tdmOriginalChannel.setStatus(_A)
class _TdmRemoteLoop_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_TdmRemoteLoop_Type.__name__=_E
_TdmRemoteLoop_Object=MibTableColumn
tdmRemoteLoop=_TdmRemoteLoop_Object((1,3,6,1,4,1,42926,2,18,7,1,28),_TdmRemoteLoop_Type())
tdmRemoteLoop.setMaxAccess(_D)
if mibBuilder.loadTexts:tdmRemoteLoop.setStatus(_A)
_TdmTos_Type=Integer32
_TdmTos_Object=MibTableColumn
tdmTos=_TdmTos_Object((1,3,6,1,4,1,42926,2,18,7,1,29),_TdmTos_Type())
tdmTos.setMaxAccess(_D)
if mibBuilder.loadTexts:tdmTos.setStatus(_A)
_TdmSpeedRegualator_Type=DisplayString
_TdmSpeedRegualator_Object=MibTableColumn
tdmSpeedRegualator=_TdmSpeedRegualator_Object((1,3,6,1,4,1,42926,2,18,7,1,30),_TdmSpeedRegualator_Type())
tdmSpeedRegualator.setMaxAccess(_D)
if mibBuilder.loadTexts:tdmSpeedRegualator.setStatus(_A)
_TdmSpeed_Type=Integer32
_TdmSpeed_Object=MibTableColumn
tdmSpeed=_TdmSpeed_Object((1,3,6,1,4,1,42926,2,18,7,1,31),_TdmSpeed_Type())
tdmSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:tdmSpeed.setStatus(_A)
if mibBuilder.loadTexts:tdmSpeed.setUnits(_K)
class _TdmConfigured_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('configured',1),('notConfigured',2)))
_TdmConfigured_Type.__name__=_E
_TdmConfigured_Object=MibTableColumn
tdmConfigured=_TdmConfigured_Object((1,3,6,1,4,1,42926,2,18,7,1,32),_TdmConfigured_Type())
tdmConfigured.setMaxAccess(_D)
if mibBuilder.loadTexts:tdmConfigured.setStatus(_A)
class _TdmUseConstSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('const',1),('restored',2)))
_TdmUseConstSpeed_Type.__name__=_E
_TdmUseConstSpeed_Object=MibTableColumn
tdmUseConstSpeed=_TdmUseConstSpeed_Object((1,3,6,1,4,1,42926,2,18,7,1,33),_TdmUseConstSpeed_Type())
tdmUseConstSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:tdmUseConstSpeed.setStatus(_A)
_TdmMaxTimeout_Type=Integer32
_TdmMaxTimeout_Object=MibTableColumn
tdmMaxTimeout=_TdmMaxTimeout_Object((1,3,6,1,4,1,42926,2,18,7,1,34),_TdmMaxTimeout_Type())
tdmMaxTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:tdmMaxTimeout.setStatus(_A)
if mibBuilder.loadTexts:tdmMaxTimeout.setUnits(_N)
_TdmUsedTimeSlots_Type=Integer32
_TdmUsedTimeSlots_Object=MibTableColumn
tdmUsedTimeSlots=_TdmUsedTimeSlots_Object((1,3,6,1,4,1,42926,2,18,7,1,35),_TdmUsedTimeSlots_Type())
tdmUsedTimeSlots.setMaxAccess(_C)
if mibBuilder.loadTexts:tdmUsedTimeSlots.setStatus(_A)
class _TdmCompression_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_TdmCompression_Type.__name__=_E
_TdmCompression_Object=MibTableColumn
tdmCompression=_TdmCompression_Object((1,3,6,1,4,1,42926,2,18,7,1,36),_TdmCompression_Type())
tdmCompression.setMaxAccess(_D)
if mibBuilder.loadTexts:tdmCompression.setStatus(_A)
_TdmKeyFrameInterval_Type=Integer32
_TdmKeyFrameInterval_Object=MibTableColumn
tdmKeyFrameInterval=_TdmKeyFrameInterval_Object((1,3,6,1,4,1,42926,2,18,7,1,37),_TdmKeyFrameInterval_Type())
tdmKeyFrameInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:tdmKeyFrameInterval.setStatus(_A)
_TdmDescription_Type=DisplayString
_TdmDescription_Object=MibTableColumn
tdmDescription=_TdmDescription_Object((1,3,6,1,4,1,42926,2,18,7,1,38),_TdmDescription_Type())
tdmDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:tdmDescription.setStatus(_A)
_TdmDoubleSend_Type=Integer32
_TdmDoubleSend_Object=MibTableColumn
tdmDoubleSend=_TdmDoubleSend_Object((1,3,6,1,4,1,42926,2,18,7,1,39),_TdmDoubleSend_Type())
tdmDoubleSend.setMaxAccess(_D)
if mibBuilder.loadTexts:tdmDoubleSend.setStatus(_A)
if mibBuilder.loadTexts:tdmDoubleSend.setUnits(_G)
_TdmConstSpeed_Type=Integer32
_TdmConstSpeed_Object=MibTableColumn
tdmConstSpeed=_TdmConstSpeed_Object((1,3,6,1,4,1,42926,2,18,7,1,40),_TdmConstSpeed_Type())
tdmConstSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:tdmConstSpeed.setStatus(_A)
if mibBuilder.loadTexts:tdmConstSpeed.setUnits(_K)
class _TdmInterpMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('prevdata',0),(_S,1)))
_TdmInterpMode_Type.__name__=_E
_TdmInterpMode_Object=MibTableColumn
tdmInterpMode=_TdmInterpMode_Object((1,3,6,1,4,1,42926,2,18,7,1,41),_TdmInterpMode_Type())
tdmInterpMode.setMaxAccess(_D)
if mibBuilder.loadTexts:tdmInterpMode.setStatus(_A)
class _TdmProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('tdmop',0),('satop',1),('cesopsn',2)))
_TdmProtocol_Type.__name__=_E
_TdmProtocol_Object=MibTableColumn
tdmProtocol=_TdmProtocol_Object((1,3,6,1,4,1,42926,2,18,7,1,42),_TdmProtocol_Type())
tdmProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:tdmProtocol.setStatus(_A)
_TdmDSCP_Type=DisplayString
_TdmDSCP_Object=MibTableColumn
tdmDSCP=_TdmDSCP_Object((1,3,6,1,4,1,42926,2,18,7,1,43),_TdmDSCP_Type())
tdmDSCP.setMaxAccess(_D)
if mibBuilder.loadTexts:tdmDSCP.setStatus(_A)
_E1StatisticsTable_Object=MibTable
e1StatisticsTable=_E1StatisticsTable_Object((1,3,6,1,4,1,42926,2,18,8))
if mibBuilder.loadTexts:e1StatisticsTable.setStatus(_A)
_E1StatisticsTableEntry_Object=MibTableRow
e1StatisticsTableEntry=_E1StatisticsTableEntry_Object((1,3,6,1,4,1,42926,2,18,8,1))
e1StatisticsTableEntry.setIndexNames((0,_B,_a))
if mibBuilder.loadTexts:e1StatisticsTableEntry.setStatus(_A)
class _E1StChIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_E1StChIndex_Type.__name__=_E
_E1StChIndex_Object=MibTableColumn
e1StChIndex=_E1StChIndex_Object((1,3,6,1,4,1,42926,2,18,8,1,1),_E1StChIndex_Type())
e1StChIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:e1StChIndex.setStatus(_A)
_E1rxOkCnt_Type=Counter32
_E1rxOkCnt_Object=MibTableColumn
e1rxOkCnt=_E1rxOkCnt_Object((1,3,6,1,4,1,42926,2,18,8,1,2),_E1rxOkCnt_Type())
e1rxOkCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:e1rxOkCnt.setStatus(_A)
if mibBuilder.loadTexts:e1rxOkCnt.setUnits(_F)
_E1rxNOS_Type=Counter32
_E1rxNOS_Object=MibTableColumn
e1rxNOS=_E1rxNOS_Object((1,3,6,1,4,1,42926,2,18,8,1,3),_E1rxNOS_Type())
e1rxNOS.setMaxAccess(_C)
if mibBuilder.loadTexts:e1rxNOS.setStatus(_A)
if mibBuilder.loadTexts:e1rxNOS.setUnits(_F)
_E1rxAIS_Type=Counter32
_E1rxAIS_Object=MibTableColumn
e1rxAIS=_E1rxAIS_Object((1,3,6,1,4,1,42926,2,18,8,1,4),_E1rxAIS_Type())
e1rxAIS.setMaxAccess(_C)
if mibBuilder.loadTexts:e1rxAIS.setStatus(_A)
if mibBuilder.loadTexts:e1rxAIS.setUnits(_F)
_E1rxAZS_Type=Counter32
_E1rxAZS_Object=MibTableColumn
e1rxAZS=_E1rxAZS_Object((1,3,6,1,4,1,42926,2,18,8,1,5),_E1rxAZS_Type())
e1rxAZS.setMaxAccess(_C)
if mibBuilder.loadTexts:e1rxAZS.setStatus(_A)
if mibBuilder.loadTexts:e1rxAZS.setUnits(_F)
_E1rxLOS_Type=Counter32
_E1rxLOS_Object=MibTableColumn
e1rxLOS=_E1rxLOS_Object((1,3,6,1,4,1,42926,2,18,8,1,6),_E1rxLOS_Type())
e1rxLOS.setMaxAccess(_C)
if mibBuilder.loadTexts:e1rxLOS.setStatus(_A)
if mibBuilder.loadTexts:e1rxLOS.setUnits(_F)
_E1rxRAI_Type=Counter32
_E1rxRAI_Object=MibTableColumn
e1rxRAI=_E1rxRAI_Object((1,3,6,1,4,1,42926,2,18,8,1,7),_E1rxRAI_Type())
e1rxRAI.setMaxAccess(_C)
if mibBuilder.loadTexts:e1rxRAI.setStatus(_A)
if mibBuilder.loadTexts:e1rxRAI.setUnits(_F)
_E1rxPRBS_Type=Counter32
_E1rxPRBS_Object=MibTableColumn
e1rxPRBS=_E1rxPRBS_Object((1,3,6,1,4,1,42926,2,18,8,1,8),_E1rxPRBS_Type())
e1rxPRBS.setMaxAccess(_C)
if mibBuilder.loadTexts:e1rxPRBS.setStatus(_A)
if mibBuilder.loadTexts:e1rxPRBS.setUnits(_F)
_E1rxTest_Type=Counter32
_E1rxTest_Object=MibTableColumn
e1rxTest=_E1rxTest_Object((1,3,6,1,4,1,42926,2,18,8,1,9),_E1rxTest_Type())
e1rxTest.setMaxAccess(_C)
if mibBuilder.loadTexts:e1rxTest.setStatus(_A)
if mibBuilder.loadTexts:e1rxTest.setUnits(_F)
_E1rxCodeErr_Type=Counter32
_E1rxCodeErr_Object=MibTableColumn
e1rxCodeErr=_E1rxCodeErr_Object((1,3,6,1,4,1,42926,2,18,8,1,11),_E1rxCodeErr_Type())
e1rxCodeErr.setMaxAccess(_C)
if mibBuilder.loadTexts:e1rxCodeErr.setStatus(_A)
if mibBuilder.loadTexts:e1rxCodeErr.setUnits(_F)
_E1rxRareErr_Type=Counter32
_E1rxRareErr_Object=MibTableColumn
e1rxRareErr=_E1rxRareErr_Object((1,3,6,1,4,1,42926,2,18,8,1,12),_E1rxRareErr_Type())
e1rxRareErr.setMaxAccess(_C)
if mibBuilder.loadTexts:e1rxRareErr.setStatus(_A)
if mibBuilder.loadTexts:e1rxRareErr.setUnits(_F)
_E1rxFastErr_Type=Counter32
_E1rxFastErr_Object=MibTableColumn
e1rxFastErr=_E1rxFastErr_Object((1,3,6,1,4,1,42926,2,18,8,1,13),_E1rxFastErr_Type())
e1rxFastErr.setMaxAccess(_C)
if mibBuilder.loadTexts:e1rxFastErr.setStatus(_A)
if mibBuilder.loadTexts:e1rxFastErr.setUnits(_F)
_E1rxFDev_Type=Integer32
_E1rxFDev_Object=MibTableColumn
e1rxFDev=_E1rxFDev_Object((1,3,6,1,4,1,42926,2,18,8,1,14),_E1rxFDev_Type())
e1rxFDev.setMaxAccess(_C)
if mibBuilder.loadTexts:e1rxFDev.setStatus(_A)
if mibBuilder.loadTexts:e1rxFDev.setUnits(_K)
_E1rxCRC4_Type=Counter64
_E1rxCRC4_Object=MibTableColumn
e1rxCRC4=_E1rxCRC4_Object((1,3,6,1,4,1,42926,2,18,8,1,15),_E1rxCRC4_Type())
e1rxCRC4.setMaxAccess(_C)
if mibBuilder.loadTexts:e1rxCRC4.setStatus(_A)
if mibBuilder.loadTexts:e1rxCRC4.setUnits(_F)
_E1rxCRC4Sec_Type=Counter32
_E1rxCRC4Sec_Object=MibTableColumn
e1rxCRC4Sec=_E1rxCRC4Sec_Object((1,3,6,1,4,1,42926,2,18,8,1,16),_E1rxCRC4Sec_Type())
e1rxCRC4Sec.setMaxAccess(_C)
if mibBuilder.loadTexts:e1rxCRC4Sec.setStatus(_A)
if mibBuilder.loadTexts:e1rxCRC4Sec.setUnits(_F)
_E1rxCRC4Rem_Type=Counter32
_E1rxCRC4Rem_Object=MibTableColumn
e1rxCRC4Rem=_E1rxCRC4Rem_Object((1,3,6,1,4,1,42926,2,18,8,1,17),_E1rxCRC4Rem_Type())
e1rxCRC4Rem.setMaxAccess(_C)
if mibBuilder.loadTexts:e1rxCRC4Rem.setStatus(_A)
if mibBuilder.loadTexts:e1rxCRC4Rem.setUnits(_F)
_E1rxMfAS_Type=Counter32
_E1rxMfAS_Object=MibTableColumn
e1rxMfAS=_E1rxMfAS_Object((1,3,6,1,4,1,42926,2,18,8,1,18),_E1rxMfAS_Type())
e1rxMfAS.setMaxAccess(_C)
if mibBuilder.loadTexts:e1rxMfAS.setStatus(_A)
if mibBuilder.loadTexts:e1rxMfAS.setUnits(_F)
_E1txOkCnt_Type=Counter32
_E1txOkCnt_Object=MibTableColumn
e1txOkCnt=_E1txOkCnt_Object((1,3,6,1,4,1,42926,2,18,8,1,102),_E1txOkCnt_Type())
e1txOkCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:e1txOkCnt.setStatus(_A)
if mibBuilder.loadTexts:e1txOkCnt.setUnits(_F)
_E1txNOS_Type=Counter32
_E1txNOS_Object=MibTableColumn
e1txNOS=_E1txNOS_Object((1,3,6,1,4,1,42926,2,18,8,1,103),_E1txNOS_Type())
e1txNOS.setMaxAccess(_C)
if mibBuilder.loadTexts:e1txNOS.setStatus(_A)
if mibBuilder.loadTexts:e1txNOS.setUnits(_F)
_E1txAIS_Type=Counter32
_E1txAIS_Object=MibTableColumn
e1txAIS=_E1txAIS_Object((1,3,6,1,4,1,42926,2,18,8,1,104),_E1txAIS_Type())
e1txAIS.setMaxAccess(_C)
if mibBuilder.loadTexts:e1txAIS.setStatus(_A)
if mibBuilder.loadTexts:e1txAIS.setUnits(_F)
_E1txAZS_Type=Counter32
_E1txAZS_Object=MibTableColumn
e1txAZS=_E1txAZS_Object((1,3,6,1,4,1,42926,2,18,8,1,105),_E1txAZS_Type())
e1txAZS.setMaxAccess(_C)
if mibBuilder.loadTexts:e1txAZS.setStatus(_A)
if mibBuilder.loadTexts:e1txAZS.setUnits(_F)
_E1txLOS_Type=Counter32
_E1txLOS_Object=MibTableColumn
e1txLOS=_E1txLOS_Object((1,3,6,1,4,1,42926,2,18,8,1,106),_E1txLOS_Type())
e1txLOS.setMaxAccess(_C)
if mibBuilder.loadTexts:e1txLOS.setStatus(_A)
if mibBuilder.loadTexts:e1txLOS.setUnits(_F)
_E1txRAI_Type=Counter32
_E1txRAI_Object=MibTableColumn
e1txRAI=_E1txRAI_Object((1,3,6,1,4,1,42926,2,18,8,1,107),_E1txRAI_Type())
e1txRAI.setMaxAccess(_C)
if mibBuilder.loadTexts:e1txRAI.setStatus(_A)
if mibBuilder.loadTexts:e1txRAI.setUnits(_F)
_E1txPRBS_Type=Counter32
_E1txPRBS_Object=MibTableColumn
e1txPRBS=_E1txPRBS_Object((1,3,6,1,4,1,42926,2,18,8,1,108),_E1txPRBS_Type())
e1txPRBS.setMaxAccess(_C)
if mibBuilder.loadTexts:e1txPRBS.setStatus(_A)
if mibBuilder.loadTexts:e1txPRBS.setUnits(_F)
_E1txLock_Type=Counter32
_E1txLock_Object=MibTableColumn
e1txLock=_E1txLock_Object((1,3,6,1,4,1,42926,2,18,8,1,112),_E1txLock_Type())
e1txLock.setMaxAccess(_C)
if mibBuilder.loadTexts:e1txLock.setStatus(_A)
if mibBuilder.loadTexts:e1txLock.setUnits(_F)
_E1Start_Type=DateAndTime
_E1Start_Object=MibTableColumn
e1Start=_E1Start_Object((1,3,6,1,4,1,42926,2,18,8,1,113),_E1Start_Type())
e1Start.setMaxAccess(_C)
if mibBuilder.loadTexts:e1Start.setStatus(_A)
_E1Finish_Type=DateAndTime
_E1Finish_Object=MibTableColumn
e1Finish=_E1Finish_Object((1,3,6,1,4,1,42926,2,18,8,1,114),_E1Finish_Type())
e1Finish.setMaxAccess(_C)
if mibBuilder.loadTexts:e1Finish.setStatus(_A)
_E1Total_Type=Counter32
_E1Total_Object=MibTableColumn
e1Total=_E1Total_Object((1,3,6,1,4,1,42926,2,18,8,1,115),_E1Total_Type())
e1Total.setMaxAccess(_C)
if mibBuilder.loadTexts:e1Total.setStatus(_A)
if mibBuilder.loadTexts:e1Total.setUnits(_F)
_E1txFDev_Type=Integer32
_E1txFDev_Object=MibTableColumn
e1txFDev=_E1txFDev_Object((1,3,6,1,4,1,42926,2,18,8,1,116),_E1txFDev_Type())
e1txFDev.setMaxAccess(_C)
if mibBuilder.loadTexts:e1txFDev.setStatus(_A)
if mibBuilder.loadTexts:e1txFDev.setUnits(_K)
_E1txCRC4Sec_Type=Counter32
_E1txCRC4Sec_Object=MibTableColumn
e1txCRC4Sec=_E1txCRC4Sec_Object((1,3,6,1,4,1,42926,2,18,8,1,117),_E1txCRC4Sec_Type())
e1txCRC4Sec.setMaxAccess(_C)
if mibBuilder.loadTexts:e1txCRC4Sec.setStatus(_A)
if mibBuilder.loadTexts:e1txCRC4Sec.setUnits(_F)
_E1txCRC4Rem_Type=Counter32
_E1txCRC4Rem_Object=MibTableColumn
e1txCRC4Rem=_E1txCRC4Rem_Object((1,3,6,1,4,1,42926,2,18,8,1,118),_E1txCRC4Rem_Type())
e1txCRC4Rem.setMaxAccess(_C)
if mibBuilder.loadTexts:e1txCRC4Rem.setStatus(_A)
if mibBuilder.loadTexts:e1txCRC4Rem.setUnits(_F)
_E1txMfAS_Type=Counter32
_E1txMfAS_Object=MibTableColumn
e1txMfAS=_E1txMfAS_Object((1,3,6,1,4,1,42926,2,18,8,1,119),_E1txMfAS_Type())
e1txMfAS.setMaxAccess(_C)
if mibBuilder.loadTexts:e1txMfAS.setStatus(_A)
if mibBuilder.loadTexts:e1txMfAS.setUnits(_F)
_TdmStatisticsTable_Object=MibTable
tdmStatisticsTable=_TdmStatisticsTable_Object((1,3,6,1,4,1,42926,2,18,9))
if mibBuilder.loadTexts:tdmStatisticsTable.setStatus(_A)
_TdmStatisticsTableEntry_Object=MibTableRow
tdmStatisticsTableEntry=_TdmStatisticsTableEntry_Object((1,3,6,1,4,1,42926,2,18,9,1))
tdmStatisticsTableEntry.setIndexNames((0,_B,_b))
if mibBuilder.loadTexts:tdmStatisticsTableEntry.setStatus(_A)
class _TdmStChIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_TdmStChIndex_Type.__name__=_E
_TdmStChIndex_Object=MibTableColumn
tdmStChIndex=_TdmStChIndex_Object((1,3,6,1,4,1,42926,2,18,9,1,1),_TdmStChIndex_Type())
tdmStChIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:tdmStChIndex.setStatus(_A)
_TdmResend_Type=Counter32
_TdmResend_Object=MibTableColumn
tdmResend=_TdmResend_Object((1,3,6,1,4,1,42926,2,18,9,1,2),_TdmResend_Type())
tdmResend.setMaxAccess(_C)
if mibBuilder.loadTexts:tdmResend.setStatus(_A)
if mibBuilder.loadTexts:tdmResend.setUnits(_G)
_TdmLost_Type=Counter32
_TdmLost_Object=MibTableColumn
tdmLost=_TdmLost_Object((1,3,6,1,4,1,42926,2,18,9,1,3),_TdmLost_Type())
tdmLost.setMaxAccess(_C)
if mibBuilder.loadTexts:tdmLost.setStatus(_A)
if mibBuilder.loadTexts:tdmLost.setUnits(_G)
_TdmOvf_Type=Counter32
_TdmOvf_Object=MibTableColumn
tdmOvf=_TdmOvf_Object((1,3,6,1,4,1,42926,2,18,9,1,4),_TdmOvf_Type())
tdmOvf.setMaxAccess(_C)
if mibBuilder.loadTexts:tdmOvf.setStatus(_A)
if mibBuilder.loadTexts:tdmOvf.setUnits(_P)
_TdmUndf_Type=Counter32
_TdmUndf_Object=MibTableColumn
tdmUndf=_TdmUndf_Object((1,3,6,1,4,1,42926,2,18,9,1,5),_TdmUndf_Type())
tdmUndf.setMaxAccess(_C)
if mibBuilder.loadTexts:tdmUndf.setStatus(_A)
if mibBuilder.loadTexts:tdmUndf.setUnits('Times')
_TdmIgnored_Type=Counter32
_TdmIgnored_Object=MibTableColumn
tdmIgnored=_TdmIgnored_Object((1,3,6,1,4,1,42926,2,18,9,1,6),_TdmIgnored_Type())
tdmIgnored.setMaxAccess(_C)
if mibBuilder.loadTexts:tdmIgnored.setStatus(_A)
if mibBuilder.loadTexts:tdmIgnored.setUnits(_G)
_TdmInterp_Type=Counter32
_TdmInterp_Object=MibTableColumn
tdmInterp=_TdmInterp_Object((1,3,6,1,4,1,42926,2,18,9,1,7),_TdmInterp_Type())
tdmInterp.setMaxAccess(_C)
if mibBuilder.loadTexts:tdmInterp.setStatus(_A)
if mibBuilder.loadTexts:tdmInterp.setUnits('125us')
_TdmResync_Type=Counter32
_TdmResync_Object=MibTableColumn
tdmResync=_TdmResync_Object((1,3,6,1,4,1,42926,2,18,9,1,8),_TdmResync_Type())
tdmResync.setMaxAccess(_C)
if mibBuilder.loadTexts:tdmResync.setStatus(_A)
if mibBuilder.loadTexts:tdmResync.setUnits(_P)
_TdmValid_Type=Counter32
_TdmValid_Object=MibTableColumn
tdmValid=_TdmValid_Object((1,3,6,1,4,1,42926,2,18,9,1,9),_TdmValid_Type())
tdmValid.setMaxAccess(_C)
if mibBuilder.loadTexts:tdmValid.setStatus(_A)
if mibBuilder.loadTexts:tdmValid.setUnits(_G)
_TdmSlipAdd_Type=Counter32
_TdmSlipAdd_Object=MibTableColumn
tdmSlipAdd=_TdmSlipAdd_Object((1,3,6,1,4,1,42926,2,18,9,1,10),_TdmSlipAdd_Type())
tdmSlipAdd.setMaxAccess(_C)
if mibBuilder.loadTexts:tdmSlipAdd.setStatus(_A)
if mibBuilder.loadTexts:tdmSlipAdd.setUnits(_P)
_TdmSlipRem_Type=Counter32
_TdmSlipRem_Object=MibTableColumn
tdmSlipRem=_TdmSlipRem_Object((1,3,6,1,4,1,42926,2,18,9,1,11),_TdmSlipRem_Type())
tdmSlipRem.setMaxAccess(_C)
if mibBuilder.loadTexts:tdmSlipRem.setStatus(_A)
if mibBuilder.loadTexts:tdmSlipRem.setUnits(_P)
_TdmLostReq_Type=Counter32
_TdmLostReq_Object=MibTableColumn
tdmLostReq=_TdmLostReq_Object((1,3,6,1,4,1,42926,2,18,9,1,12),_TdmLostReq_Type())
tdmLostReq.setMaxAccess(_C)
if mibBuilder.loadTexts:tdmLostReq.setStatus(_A)
if mibBuilder.loadTexts:tdmLostReq.setUnits(_G)
_TdmRestored_Type=Counter32
_TdmRestored_Object=MibTableColumn
tdmRestored=_TdmRestored_Object((1,3,6,1,4,1,42926,2,18,9,1,13),_TdmRestored_Type())
tdmRestored.setMaxAccess(_C)
if mibBuilder.loadTexts:tdmRestored.setStatus(_A)
if mibBuilder.loadTexts:tdmRestored.setUnits(_G)
_TdmStart_Type=DateAndTime
_TdmStart_Object=MibTableColumn
tdmStart=_TdmStart_Object((1,3,6,1,4,1,42926,2,18,9,1,14),_TdmStart_Type())
tdmStart.setMaxAccess(_C)
if mibBuilder.loadTexts:tdmStart.setStatus(_A)
_TdmFinish_Type=DateAndTime
_TdmFinish_Object=MibTableColumn
tdmFinish=_TdmFinish_Object((1,3,6,1,4,1,42926,2,18,9,1,15),_TdmFinish_Type())
tdmFinish.setMaxAccess(_C)
if mibBuilder.loadTexts:tdmFinish.setStatus(_A)
_TdmAvgSpeed_Type=Integer32
_TdmAvgSpeed_Object=MibTableColumn
tdmAvgSpeed=_TdmAvgSpeed_Object((1,3,6,1,4,1,42926,2,18,9,1,16),_TdmAvgSpeed_Type())
tdmAvgSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:tdmAvgSpeed.setStatus(_A)
if mibBuilder.loadTexts:tdmAvgSpeed.setUnits(_K)
_TdmAvgJB_Type=Integer32
_TdmAvgJB_Object=MibTableColumn
tdmAvgJB=_TdmAvgJB_Object((1,3,6,1,4,1,42926,2,18,9,1,17),_TdmAvgJB_Type())
tdmAvgJB.setMaxAccess(_C)
if mibBuilder.loadTexts:tdmAvgJB.setStatus(_A)
if mibBuilder.loadTexts:tdmAvgJB.setUnits('us')
_TdmMinJB_Type=Integer32
_TdmMinJB_Object=MibTableColumn
tdmMinJB=_TdmMinJB_Object((1,3,6,1,4,1,42926,2,18,9,1,18),_TdmMinJB_Type())
tdmMinJB.setMaxAccess(_C)
if mibBuilder.loadTexts:tdmMinJB.setStatus(_A)
if mibBuilder.loadTexts:tdmMinJB.setUnits(_N)
_TdmMaxJB_Type=Integer32
_TdmMaxJB_Object=MibTableColumn
tdmMaxJB=_TdmMaxJB_Object((1,3,6,1,4,1,42926,2,18,9,1,19),_TdmMaxJB_Type())
tdmMaxJB.setMaxAccess(_C)
if mibBuilder.loadTexts:tdmMaxJB.setStatus(_A)
if mibBuilder.loadTexts:tdmMaxJB.setUnits(_N)
_TdmRecommenedJB_Type=Integer32
_TdmRecommenedJB_Object=MibTableColumn
tdmRecommenedJB=_TdmRecommenedJB_Object((1,3,6,1,4,1,42926,2,18,9,1,20),_TdmRecommenedJB_Type())
tdmRecommenedJB.setMaxAccess(_C)
if mibBuilder.loadTexts:tdmRecommenedJB.setStatus(_A)
if mibBuilder.loadTexts:tdmRecommenedJB.setUnits(_N)
_TdmFatal_Type=Counter32
_TdmFatal_Object=MibTableColumn
tdmFatal=_TdmFatal_Object((1,3,6,1,4,1,42926,2,18,9,1,21),_TdmFatal_Type())
tdmFatal.setMaxAccess(_C)
if mibBuilder.loadTexts:tdmFatal.setStatus(_A)
if mibBuilder.loadTexts:tdmFatal.setUnits(_G)
_TdmTxDiscards_Type=Counter32
_TdmTxDiscards_Object=MibTableColumn
tdmTxDiscards=_TdmTxDiscards_Object((1,3,6,1,4,1,42926,2,18,9,1,22),_TdmTxDiscards_Type())
tdmTxDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:tdmTxDiscards.setStatus(_A)
if mibBuilder.loadTexts:tdmTxDiscards.setUnits(_G)
_TdmBandwidth_Type=Integer32
_TdmBandwidth_Object=MibTableColumn
tdmBandwidth=_TdmBandwidth_Object((1,3,6,1,4,1,42926,2,18,9,1,23),_TdmBandwidth_Type())
tdmBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:tdmBandwidth.setStatus(_A)
if mibBuilder.loadTexts:tdmBandwidth.setUnits('kbps')
_E1traps_ObjectIdentity=ObjectIdentity
e1traps=_E1traps_ObjectIdentity((1,3,6,1,4,1,42926,2,18,10))
_E1trapsPrefix_ObjectIdentity=ObjectIdentity
e1trapsPrefix=_E1trapsPrefix_ObjectIdentity((1,3,6,1,4,1,42926,2,18,10,0))
_TdmRedundancyTable_Object=MibTable
tdmRedundancyTable=_TdmRedundancyTable_Object((1,3,6,1,4,1,42926,2,18,11))
if mibBuilder.loadTexts:tdmRedundancyTable.setStatus(_A)
_TdmRedundancyTableEntry_Object=MibTableRow
tdmRedundancyTableEntry=_TdmRedundancyTableEntry_Object((1,3,6,1,4,1,42926,2,18,11,1))
tdmRedundancyTableEntry.setIndexNames((0,_B,_c))
if mibBuilder.loadTexts:tdmRedundancyTableEntry.setStatus(_A)
class _TdmRedundancyIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_TdmRedundancyIndex_Type.__name__=_E
_TdmRedundancyIndex_Object=MibTableColumn
tdmRedundancyIndex=_TdmRedundancyIndex_Object((1,3,6,1,4,1,42926,2,18,11,1,1),_TdmRedundancyIndex_Type())
tdmRedundancyIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:tdmRedundancyIndex.setStatus(_A)
class _TdmRedundancyEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_TdmRedundancyEnabled_Type.__name__=_E
_TdmRedundancyEnabled_Object=MibTableColumn
tdmRedundancyEnabled=_TdmRedundancyEnabled_Object((1,3,6,1,4,1,42926,2,18,11,1,2),_TdmRedundancyEnabled_Type())
tdmRedundancyEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:tdmRedundancyEnabled.setStatus(_A)
_TdmRedundancyRemoteIP_Type=IpAddress
_TdmRedundancyRemoteIP_Object=MibTableColumn
tdmRedundancyRemoteIP=_TdmRedundancyRemoteIP_Object((1,3,6,1,4,1,42926,2,18,11,1,3),_TdmRedundancyRemoteIP_Type())
tdmRedundancyRemoteIP.setMaxAccess(_D)
if mibBuilder.loadTexts:tdmRedundancyRemoteIP.setStatus(_A)
_TdmRedundancyVLANID_Type=Integer32
_TdmRedundancyVLANID_Object=MibTableColumn
tdmRedundancyVLANID=_TdmRedundancyVLANID_Object((1,3,6,1,4,1,42926,2,18,11,1,4),_TdmRedundancyVLANID_Type())
tdmRedundancyVLANID.setMaxAccess(_D)
if mibBuilder.loadTexts:tdmRedundancyVLANID.setStatus(_A)
_TdmRedundancyDSCP_Type=DisplayString
_TdmRedundancyDSCP_Object=MibTableColumn
tdmRedundancyDSCP=_TdmRedundancyDSCP_Object((1,3,6,1,4,1,42926,2,18,11,1,5),_TdmRedundancyDSCP_Type())
tdmRedundancyDSCP.setMaxAccess(_D)
if mibBuilder.loadTexts:tdmRedundancyDSCP.setStatus(_A)
class _TdmRedundancyUseIP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('use',1),(_Z,2)))
_TdmRedundancyUseIP_Type.__name__=_E
_TdmRedundancyUseIP_Object=MibTableColumn
tdmRedundancyUseIP=_TdmRedundancyUseIP_Object((1,3,6,1,4,1,42926,2,18,11,1,6),_TdmRedundancyUseIP_Type())
tdmRedundancyUseIP.setMaxAccess(_D)
if mibBuilder.loadTexts:tdmRedundancyUseIP.setStatus(_A)
_TdmRedundancyVLANPri_Type=Integer32
_TdmRedundancyVLANPri_Object=MibTableColumn
tdmRedundancyVLANPri=_TdmRedundancyVLANPri_Object((1,3,6,1,4,1,42926,2,18,11,1,7),_TdmRedundancyVLANPri_Type())
tdmRedundancyVLANPri.setMaxAccess(_D)
if mibBuilder.loadTexts:tdmRedundancyVLANPri.setStatus(_A)
_Eth_ObjectIdentity=ObjectIdentity
eth=_Eth_ObjectIdentity((1,3,6,1,4,1,42926,2,19))
_VlanTable_Object=MibTable
vlanTable=_VlanTable_Object((1,3,6,1,4,1,42926,2,19,3))
if mibBuilder.loadTexts:vlanTable.setStatus(_A)
_VlanTableEntry_Object=MibTableRow
vlanTableEntry=_VlanTableEntry_Object((1,3,6,1,4,1,42926,2,19,3,1))
vlanTableEntry.setIndexNames((0,_B,_T))
if mibBuilder.loadTexts:vlanTableEntry.setStatus(_A)
class _VlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_VlanID_Type.__name__=_E
_VlanID_Object=MibTableColumn
vlanID=_VlanID_Object((1,3,6,1,4,1,42926,2,19,3,1,1),_VlanID_Type())
vlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanID.setStatus(_A)
_Adc_ObjectIdentity=ObjectIdentity
adc=_Adc_ObjectIdentity((1,3,6,1,4,1,42926,2,21))
_AdcTable_Object=MibTable
adcTable=_AdcTable_Object((1,3,6,1,4,1,42926,2,21,1))
if mibBuilder.loadTexts:adcTable.setStatus(_A)
_AdcTableEntry_Object=MibTableRow
adcTableEntry=_AdcTableEntry_Object((1,3,6,1,4,1,42926,2,21,1,1))
adcTableEntry.setIndexNames((0,_B,_d))
if mibBuilder.loadTexts:adcTableEntry.setStatus(_A)
class _AdcIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_AdcIndex_Type.__name__=_E
_AdcIndex_Object=MibTableColumn
adcIndex=_AdcIndex_Object((1,3,6,1,4,1,42926,2,21,1,1,1),_AdcIndex_Type())
adcIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:adcIndex.setStatus(_A)
_AdcName_Type=DisplayString
_AdcName_Object=MibTableColumn
adcName=_AdcName_Object((1,3,6,1,4,1,42926,2,21,1,1,2),_AdcName_Type())
adcName.setMaxAccess(_C)
if mibBuilder.loadTexts:adcName.setStatus(_A)
_AdcValue_Type=Float
_AdcValue_Object=MibTableColumn
adcValue=_AdcValue_Object((1,3,6,1,4,1,42926,2,21,1,1,3),_AdcValue_Type())
adcValue.setMaxAccess(_C)
if mibBuilder.loadTexts:adcValue.setStatus(_A)
_AdcType_Type=DisplayString
_AdcType_Object=MibTableColumn
adcType=_AdcType_Object((1,3,6,1,4,1,42926,2,21,1,1,4),_AdcType_Type())
adcType.setMaxAccess(_C)
if mibBuilder.loadTexts:adcType.setStatus(_A)
class _AdcState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('normal',0),('errHigh',1),('errLow',2),('warnHigh',3),('warnLow',4),(_O,5)))
_AdcState_Type.__name__=_E
_AdcState_Object=MibTableColumn
adcState=_AdcState_Object((1,3,6,1,4,1,42926,2,21,1,1,5),_AdcState_Type())
adcState.setMaxAccess(_C)
if mibBuilder.loadTexts:adcState.setStatus(_A)
_DyingGaspNotifications_ObjectIdentity=ObjectIdentity
dyingGaspNotifications=_DyingGaspNotifications_ObjectIdentity((1,3,6,1,4,1,42926,2,22))
_DyingGaspTraps_ObjectIdentity=ObjectIdentity
dyingGaspTraps=_DyingGaspTraps_ObjectIdentity((1,3,6,1,4,1,42926,2,22,0))
_MuxConformance_ObjectIdentity=ObjectIdentity
muxConformance=_MuxConformance_ObjectIdentity((1,3,6,1,4,1,42926,2,30))
_MuxGroups_ObjectIdentity=ObjectIdentity
muxGroups=_MuxGroups_ObjectIdentity((1,3,6,1,4,1,42926,2,30,1))
_MuxCompliances_ObjectIdentity=ObjectIdentity
muxCompliances=_MuxCompliances_ObjectIdentity((1,3,6,1,4,1,42926,2,30,2))
muxBaseGroup=ObjectGroup((1,3,6,1,4,1,42926,2,30,1,1))
muxBaseGroup.setObjects(*((_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,'sysID'),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q)))
if mibBuilder.loadTexts:muxBaseGroup.setStatus(_A)
e1Group=ObjectGroup((1,3,6,1,4,1,42926,2,30,1,2))
e1Group.setObjects(*((_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_U),(_B,_V),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,'e1CRC4'),(_B,_A6)))
if mibBuilder.loadTexts:e1Group.setStatus(_A)
tdmGroup=ObjectGroup((1,3,6,1,4,1,42926,2,30,1,3))
tdmGroup.setObjects(*((_B,_A7),(_B,_Q),(_B,_R),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,'tdmMode'),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,'tdmUseIP'),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,'tdmTos'),(_B,_AQ),(_B,'tdmSpeed'),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,'tdmDSCP')))
if mibBuilder.loadTexts:tdmGroup.setStatus(_A)
e1GroupStat=ObjectGroup((1,3,6,1,4,1,42926,2,30,1,4))
e1GroupStat.setObjects(*((_B,_Ac),(_B,'e1rxNOS'),(_B,'e1rxAIS'),(_B,'e1rxAZS'),(_B,'e1rxLOS'),(_B,'e1rxRAI'),(_B,'e1rxPRBS'),(_B,'e1rxTest'),(_B,_Ad),(_B,_Ae),(_B,_Af),(_B,'e1rxFDev'),(_B,'e1rxCRC4'),(_B,_Ag),(_B,_Ah),(_B,'e1rxMfAS'),(_B,_Ai),(_B,'e1txNOS'),(_B,'e1txAIS'),(_B,'e1txAZS'),(_B,'e1txLOS'),(_B,'e1txRAI'),(_B,'e1txPRBS'),(_B,'e1txLock'),(_B,'e1Start'),(_B,'e1Finish'),(_B,'e1Total'),(_B,'e1txFDev'),(_B,_Aj),(_B,_Ak),(_B,'e1txMfAS')))
if mibBuilder.loadTexts:e1GroupStat.setStatus(_A)
tdmGroupStat=ObjectGroup((1,3,6,1,4,1,42926,2,30,1,5))
tdmGroupStat.setObjects(*((_B,_Al),(_B,'tdmLost'),(_B,'tdmOvf'),(_B,'tdmUndf'),(_B,_Am),(_B,_An),(_B,_Ao),(_B,'tdmValid'),(_B,_Ap),(_B,_Aq),(_B,_Ar),(_B,_As),(_B,'tdmStart'),(_B,_At),(_B,_Au),(_B,'tdmAvgJB'),(_B,'tdmMinJB'),(_B,'tdmMaxJB'),(_B,_Av),(_B,'tdmFatal'),(_B,_Aw),(_B,_Ax)))
if mibBuilder.loadTexts:tdmGroupStat.setStatus(_A)
vlanGroup=ObjectGroup((1,3,6,1,4,1,42926,2,30,1,6))
vlanGroup.setObjects((_B,_T))
if mibBuilder.loadTexts:vlanGroup.setStatus(_A)
ipcurrentGroup=ObjectGroup((1,3,6,1,4,1,42926,2,30,1,7))
ipcurrentGroup.setObjects(*((_B,'cNetIP'),(_B,'cNetMask'),(_B,_Ay),(_B,_Az),(_B,_A_),(_B,_B0),(_B,_B1),(_B,_B2),(_B,'cDNS1'),(_B,_B3),(_B,_B4)))
if mibBuilder.loadTexts:ipcurrentGroup.setStatus(_A)
ipstoredGroup=ObjectGroup((1,3,6,1,4,1,42926,2,30,1,8))
ipstoredGroup.setObjects(*((_B,'sNetIP'),(_B,'sNetMask'),(_B,_B5),(_B,_B6),(_B,_B7),(_B,_B8),(_B,_B9),(_B,_BA),(_B,'sDNS1'),(_B,_BB),(_B,_BC)))
if mibBuilder.loadTexts:ipstoredGroup.setStatus(_A)
hostsGroup=ObjectGroup((1,3,6,1,4,1,42926,2,30,1,9))
hostsGroup.setObjects(*((_B,_BD),(_B,'hostMask')))
if mibBuilder.loadTexts:hostsGroup.setStatus(_A)
adcGroup=ObjectGroup((1,3,6,1,4,1,42926,2,30,1,10))
adcGroup.setObjects(*((_B,'adcName'),(_B,'adcValue'),(_B,'adcType'),(_B,'adcState')))
if mibBuilder.loadTexts:adcGroup.setStatus(_A)
tdmRedundancyGroup=ObjectGroup((1,3,6,1,4,1,42926,2,30,1,13))
tdmRedundancyGroup.setObjects(*((_B,_BE),(_B,_BF),(_B,_BG),(_B,_BH),(_B,_BI),(_B,_BJ)))
if mibBuilder.loadTexts:tdmRedundancyGroup.setStatus(_A)
e1LinkChange=NotificationType((1,3,6,1,4,1,42926,2,18,10,0,1))
e1LinkChange.setObjects(*((_B,_U),(_B,_V)))
if mibBuilder.loadTexts:e1LinkChange.setStatus(_A)
tdmLinkDown=NotificationType((1,3,6,1,4,1,42926,2,18,10,0,2))
tdmLinkDown.setObjects(*((_B,_R),(_B,_Q)))
if mibBuilder.loadTexts:tdmLinkDown.setStatus(_A)
tdmLinkUp=NotificationType((1,3,6,1,4,1,42926,2,18,10,0,3))
tdmLinkUp.setObjects(*((_B,_R),(_B,_Q)))
if mibBuilder.loadTexts:tdmLinkUp.setStatus(_A)
dyingGaspTrap=NotificationType((1,3,6,1,4,1,42926,2,22,0,1))
if mibBuilder.loadTexts:dyingGaspTrap.setStatus(_A)
e1trapsGroup=NotificationGroup((1,3,6,1,4,1,42926,2,30,1,11))
e1trapsGroup.setObjects(*((_B,_BK),(_B,_BL),(_B,_BM)))
if mibBuilder.loadTexts:e1trapsGroup.setStatus(_A)
dyingGaspTrapsGroup=NotificationGroup((1,3,6,1,4,1,42926,2,30,1,12))
dyingGaspTrapsGroup.setObjects((_B,_BN))
if mibBuilder.loadTexts:dyingGaspTrapsGroup.setStatus(_A)
emuxCompliance=ModuleCompliance((1,3,6,1,4,1,42926,2,30,2,1))
emuxCompliance.setObjects(*((_B,_BO),(_B,'e1Group'),(_B,'tdmGroup'),(_B,_BP),(_B,_BQ),(_B,_BR),(_B,_BS),(_B,_BT),(_B,_BU),(_B,_BV),(_B,'adcGroup'),(_B,_BW),(_B,_BX)))
if mibBuilder.loadTexts:emuxCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'TimeSlotMask':TimeSlotMask,'E1Status':E1Status,'CRC4Status':CRC4Status,'nsc':nsc,'emux':emux,'general':general,'basic':basic,_e:sysHWVer,_f:sysOSVer,_g:hwDescr,_h:manContact,_i:sysDevname,_j:devLocation,_k:sysReset,'sysID':sysID,_l:sysDateTime,_m:sysLicenseValid,_n:sysSaveConfig,_o:sysUpdate,_p:sysVendor,_q:oldSysID,'muxip':muxip,'ipcurrent':ipcurrent,'cNetIP':cNetIP,'cNetMask':cNetMask,_Ay:cNetGateway,_Az:cDefaultVlan,_A_:cDefaultVlanPri,_B0:cNetTrustAll,_B1:cNetTrustLocal,_B2:cNetTrustUnkVlan,'cDNS1':cDNS1,_B3:cPhysicalAddr,_B4:cSecondaryMAC,'ipstored':ipstored,'sNetIP':sNetIP,'sNetMask':sNetMask,_B5:sNetGateway,_B6:sDefaultVlan,_B7:sDefaultVlanPri,_B8:sNetTrustAll,_B9:sNetTrustLocal,_BA:sNetTrustUnkVlan,'sDNS1':sDNS1,_BB:sPhysicalAddr,_BC:sSecondaryMAC,'hostsTable':hostsTable,'hostsTableEntry':hostsTableEntry,_W:hostIndex,_BD:hostNetwork,'hostMask':hostMask,'e1':e1,_r:e1Number,'e1ConfigTable':e1ConfigTable,'e1ConfigTableEntry':e1ConfigTableEntry,_X:e1ChIndex,_s:e1ChStatus,_t:e1ChLinkStatus,_u:e1ChLinkEnable,_v:e1ChResetConfig,_w:e1LocalLoopback,_x:e1RecvUnframed,_y:e1SendType,_z:e1SyncSource,_A0:e1TxSpeed,_A1:e1TestFrameRTT,_U:e1RecvStatus,_V:e1SendStatus,_A2:e1RXSpeed,_A3:e1LongLine,_A4:e1SignalLevel,_A5:e1NoLogEvents,'e1CRC4':e1CRC4,_A6:e1PRBSCheck,'tdmConfigTable':tdmConfigTable,'tdmConfigTableEntry':tdmConfigTableEntry,_Y:tdmChIndex,_A7:tdmStatus,_Q:tdmLinkStatus,_R:tdmAdminStatus,_A8:tdmResetConfig,_A9:tdmFrameSize,_AA:tdmJBSize,_AB:tdmCurrentTimeout,'tdmMode':tdmMode,_AC:tdmHasData,_AD:tdmCurrentJBSize,_AE:tdmLocalTSMask,_AF:tdmRemoteTSMask,_AG:tdmVLANID,_AH:tdmVLANPri,'tdmUseIP':tdmUseIP,_AI:tdmLostRequest,_AJ:tdmRedirectedIP,_AK:tdmRedirectedMAC,_AL:tdmRedirectedChannel,_AM:tdmOriginalIP,_AN:tdmOriginalMAC,_AO:tdmOriginalChannel,_AP:tdmRemoteLoop,'tdmTos':tdmTos,_AQ:tdmSpeedRegualator,'tdmSpeed':tdmSpeed,_AR:tdmConfigured,_AS:tdmUseConstSpeed,_AT:tdmMaxTimeout,_AU:tdmUsedTimeSlots,_AV:tdmCompression,_AW:tdmKeyFrameInterval,_AX:tdmDescription,_AY:tdmDoubleSend,_AZ:tdmConstSpeed,_Aa:tdmInterpMode,_Ab:tdmProtocol,'tdmDSCP':tdmDSCP,'e1StatisticsTable':e1StatisticsTable,'e1StatisticsTableEntry':e1StatisticsTableEntry,_a:e1StChIndex,_Ac:e1rxOkCnt,'e1rxNOS':e1rxNOS,'e1rxAIS':e1rxAIS,'e1rxAZS':e1rxAZS,'e1rxLOS':e1rxLOS,'e1rxRAI':e1rxRAI,'e1rxPRBS':e1rxPRBS,'e1rxTest':e1rxTest,_Ad:e1rxCodeErr,_Ae:e1rxRareErr,_Af:e1rxFastErr,'e1rxFDev':e1rxFDev,'e1rxCRC4':e1rxCRC4,_Ag:e1rxCRC4Sec,_Ah:e1rxCRC4Rem,'e1rxMfAS':e1rxMfAS,_Ai:e1txOkCnt,'e1txNOS':e1txNOS,'e1txAIS':e1txAIS,'e1txAZS':e1txAZS,'e1txLOS':e1txLOS,'e1txRAI':e1txRAI,'e1txPRBS':e1txPRBS,'e1txLock':e1txLock,'e1Start':e1Start,'e1Finish':e1Finish,'e1Total':e1Total,'e1txFDev':e1txFDev,_Aj:e1txCRC4Sec,_Ak:e1txCRC4Rem,'e1txMfAS':e1txMfAS,'tdmStatisticsTable':tdmStatisticsTable,'tdmStatisticsTableEntry':tdmStatisticsTableEntry,_b:tdmStChIndex,_Al:tdmResend,'tdmLost':tdmLost,'tdmOvf':tdmOvf,'tdmUndf':tdmUndf,_Am:tdmIgnored,_An:tdmInterp,_Ao:tdmResync,'tdmValid':tdmValid,_Ap:tdmSlipAdd,_Aq:tdmSlipRem,_Ar:tdmLostReq,_As:tdmRestored,'tdmStart':tdmStart,_At:tdmFinish,_Au:tdmAvgSpeed,'tdmAvgJB':tdmAvgJB,'tdmMinJB':tdmMinJB,'tdmMaxJB':tdmMaxJB,_Av:tdmRecommenedJB,'tdmFatal':tdmFatal,_Aw:tdmTxDiscards,_Ax:tdmBandwidth,'e1traps':e1traps,'e1trapsPrefix':e1trapsPrefix,_BK:e1LinkChange,_BL:tdmLinkDown,_BM:tdmLinkUp,'tdmRedundancyTable':tdmRedundancyTable,'tdmRedundancyTableEntry':tdmRedundancyTableEntry,_c:tdmRedundancyIndex,_BE:tdmRedundancyEnabled,_BF:tdmRedundancyRemoteIP,_BG:tdmRedundancyVLANID,_BH:tdmRedundancyDSCP,_BI:tdmRedundancyUseIP,_BJ:tdmRedundancyVLANPri,'eth':eth,'vlanTable':vlanTable,'vlanTableEntry':vlanTableEntry,_T:vlanID,'adc':adc,'adcTable':adcTable,'adcTableEntry':adcTableEntry,_d:adcIndex,'adcName':adcName,'adcValue':adcValue,'adcType':adcType,'adcState':adcState,'dyingGaspNotifications':dyingGaspNotifications,'dyingGaspTraps':dyingGaspTraps,_BN:dyingGaspTrap,'muxConformance':muxConformance,'muxGroups':muxGroups,_BO:muxBaseGroup,'e1Group':e1Group,'tdmGroup':tdmGroup,_BP:e1GroupStat,_BQ:tdmGroupStat,_BS:vlanGroup,_BT:ipcurrentGroup,_BU:ipstoredGroup,_BV:hostsGroup,'adcGroup':adcGroup,_BR:e1trapsGroup,_BX:dyingGaspTrapsGroup,_BW:tdmRedundancyGroup,'muxCompliances':muxCompliances,'emuxCompliance':emuxCompliance})