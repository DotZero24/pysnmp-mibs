_Ag='fsDot11WIDSMIBGroup'
_Af='fsDot11WIDSSuspiciousSTAIgnoredTag'
_Ae='fsDot11WIDSSuspiciousSTANeedsDealingTag'
_Ad='fsDot11WIDSSuspiciousSTAWorksInAdhocMode'
_Ac='fsDot11WIDSSuspiciousSTAUsingChannel'
_Ab='fsDot11WIDSSuspiciousSTAMaxSignalStrength'
_Aa='fsDot11WIDSBSSIDSuspiciousSTAAccessing'
_AZ='fsDot11WIDSMomentLastTimeDetectedSusSTA'
_AY='fsDot11WIDSMomentFirstTimeDetectedSusSTA'
_AX='fsDot11WIDSAPCountDetectingSuspiciousSTA'
_AW='fsDot11WIDSSuspiciousAPIgnoredTag'
_AV='fsDot11WIDSSuspiciousAPNeedsDealingTag'
_AU='fsDot11WIDSSuspiciousAPFrameEncrption'
_AT='fsDot11WIDSSuspiciousAPUsingChannel'
_AS='fsDot11WIDSSuspiciousAPMaxSignalStrength'
_AR='fsDot11WIDSSuspiciousAPSSID'
_AQ='fsDot11WIDSMomentLastTimeDetectedSusAP'
_AP='fsDot11WIDSMomentFirstTimeDetectedSusAP'
_AO='fsDot11WIDSSuspiciousAPCount'
_AN='fsDot11WIDSAssociationFailureTotalTimes'
_AM='fsDot11WIDSShowStaticsInfo'
_AL='fsDot11WIDSShowStaticsMac'
_AK='fsDot11WIDSShowStaticsOper'
_AJ='fsDot11WIDUserisolationAP'
_AI='fsDot11WIDUserisolationAC'
_AH='fsDot11WIDSShowDot11IdsAttacklistInfo'
_AG='fsDot11WIDSShowDot11IdsAttacklistMac'
_AF='fsDot11WIDSShowDot11IdsAttacklistOper'
_AE='fsDot11WIDResetUserisolationStatistics'
_AD='fsDot11WIDSResetDynamicBlacklistType'
_AC='fsDot11WIDSResethistory'
_AB='fsDot11WIDSResetRoguehistoryStatistics'
_AA='fsDot11WIDSResetStatistics'
_A9='fsDot11WIDSEnableVlanPermitmaclist'
_A8='fsDot11WIDSEnableVlanPermitmaclistOper'
_A7='fsDot11WIDSRogueInfoString'
_A6='fsDot11WIDSRogueInfoMAC'
_A5='fsDot11WIDSRogueInfoOper'
_A4='fsDot11WIDSAttackDetectionMode'
_A3='fsDot11WIDSDynamicblacklistLifetime'
_A2='fsDot11WIDSDynamicblacklistEnable'
_A1='fsDot11StaticblacklistMAC'
_A0='fsDot11StaticblacklistOper'
_z='fsDot11WhitelistMAC'
_y='fsDot11WhitelistOper'
_x='fsDot11WIDSDeviceMode'
_w='fsDot11WIDSCountermeasureSet'
_v='fsDot11WIDSCountermeasuresMode'
_u='fsDot11WIDSDeviceagingDuration'
_t='fsDot11PermitMACAddr'
_s='fsDot11PermitMACOper'
_r='fsDot11AttackInfo'
_q='fsDot11AttackMAC'
_p='fsDot11AttackOper'
_o='fsDot11PermitSSID'
_n='fsDot11PermitOper'
_m='fsDot11VendorName'
_l='fsDot11VendorOper'
_k='fsDot11WIDSShowDot11IdsAttacklistNum'
_j='fsDot11WIDSSuspiciousSTAMAC'
_i='fsDot11WIDSSuspiciousAPBSS'
_h='fsDot11WIDSShowStaticsNum'
_g='fsDot11WIDSResetDynamicBlacklistMac'
_f='fsDot11WIDSEnableVlanPermitmaclistNum'
_e='fsDot11WIDSRogueInfoTYPE'
_d='fsDot11WIDSRogueInfoNUM'
_c='fsDot11StaticblacklistNum'
_b='fsDot11WhitelistNum'
_a='fsDot11WIDSAPID'
_Z='fsDot11PermitMACNum'
_Y='fsDot11AttackNum'
_X='fsDot11PermitNum'
_W='fsDot11VendorOUI'
_V='fsDot11WIDSDeviceInfoString'
_U='fsDot11WIDSDeviceInfoMAC'
_T='fsDot11WIDSDeviceInfoOper'
_S='fsDot11WIDSDeviceInfoTYPE'
_R='fsDot11WIDSDeviceInfoNUM'
_Q='fsDot11WIDSAttackExtensionInfo'
_P='fsDot11WIDSAttackType'
_O='fsDot11WIDSAttackingDeviceMac'
_N='fsDot11WIDSSUnauthorizedSSIDExtensionInfo'
_M='fsDot11WIDSUnauthorizedSSID'
_L='fsDot11WIDSSuspiciousDeviceExtensionInfo'
_K='fsDot11WIDSSuspiciousDeviceMac'
_J='fsDot11WIDSextinfo'
_I='fsDot11WIDSInformation'
_H='fsDot11WIDSAPBSSID'
_G='fsDot11WIDSSTAMAC'
_F='DisplayString'
_E='not-accessible'
_D='read-only'
_C='read-write'
_B='FS-DOT11-WIDS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_F,'MacAddress','PhysAddress','TextualConvention','TruthValue')
fsDot11WIDSMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,62))
if mibBuilder.loadTexts:fsDot11WIDSMIB.setRevisions(('2009-04-15 09:00',))
_FsDot11WIDSTraps_ObjectIdentity=ObjectIdentity
fsDot11WIDSTraps=_FsDot11WIDSTraps_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,62,0))
_FsDot11WIDSConfigObjects_ObjectIdentity=ObjectIdentity
fsDot11WIDSConfigObjects=_FsDot11WIDSConfigObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,62,1))
_FsDot11WIDSPermitVendorTable_Object=MibTable
fsDot11WIDSPermitVendorTable=_FsDot11WIDSPermitVendorTable_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,1))
if mibBuilder.loadTexts:fsDot11WIDSPermitVendorTable.setStatus(_A)
_FsDot11WIDSPermitVendorEntry_Object=MibTableRow
fsDot11WIDSPermitVendorEntry=_FsDot11WIDSPermitVendorEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,1,1))
fsDot11WIDSPermitVendorEntry.setIndexNames((0,_B,_W))
if mibBuilder.loadTexts:fsDot11WIDSPermitVendorEntry.setStatus(_A)
_FsDot11VendorOUI_Type=Integer32
_FsDot11VendorOUI_Object=MibTableColumn
fsDot11VendorOUI=_FsDot11VendorOUI_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,1,1,1),_FsDot11VendorOUI_Type())
fsDot11VendorOUI.setMaxAccess(_E)
if mibBuilder.loadTexts:fsDot11VendorOUI.setStatus(_A)
_FsDot11VendorOper_Type=Integer32
_FsDot11VendorOper_Object=MibTableColumn
fsDot11VendorOper=_FsDot11VendorOper_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,1,1,2),_FsDot11VendorOper_Type())
fsDot11VendorOper.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot11VendorOper.setStatus(_A)
_FsDot11VendorName_Type=MacAddress
_FsDot11VendorName_Object=MibTableColumn
fsDot11VendorName=_FsDot11VendorName_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,1,1,3),_FsDot11VendorName_Type())
fsDot11VendorName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot11VendorName.setStatus(_A)
_FsDot11WIDSPermitSSIDTable_Object=MibTable
fsDot11WIDSPermitSSIDTable=_FsDot11WIDSPermitSSIDTable_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,2))
if mibBuilder.loadTexts:fsDot11WIDSPermitSSIDTable.setStatus(_A)
_FsDot11WIDSPermitSSIDEntry_Object=MibTableRow
fsDot11WIDSPermitSSIDEntry=_FsDot11WIDSPermitSSIDEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,2,1))
fsDot11WIDSPermitSSIDEntry.setIndexNames((0,_B,_X))
if mibBuilder.loadTexts:fsDot11WIDSPermitSSIDEntry.setStatus(_A)
_FsDot11PermitNum_Type=Integer32
_FsDot11PermitNum_Object=MibTableColumn
fsDot11PermitNum=_FsDot11PermitNum_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,2,1,1),_FsDot11PermitNum_Type())
fsDot11PermitNum.setMaxAccess(_E)
if mibBuilder.loadTexts:fsDot11PermitNum.setStatus(_A)
_FsDot11PermitOper_Type=Integer32
_FsDot11PermitOper_Object=MibTableColumn
fsDot11PermitOper=_FsDot11PermitOper_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,2,1,2),_FsDot11PermitOper_Type())
fsDot11PermitOper.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot11PermitOper.setStatus(_A)
class _FsDot11PermitSSID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_FsDot11PermitSSID_Type.__name__=_F
_FsDot11PermitSSID_Object=MibTableColumn
fsDot11PermitSSID=_FsDot11PermitSSID_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,2,1,3),_FsDot11PermitSSID_Type())
fsDot11PermitSSID.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot11PermitSSID.setStatus(_A)
_FsDot11WIDSDeviceAttackMacaddressListTable_Object=MibTable
fsDot11WIDSDeviceAttackMacaddressListTable=_FsDot11WIDSDeviceAttackMacaddressListTable_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,3))
if mibBuilder.loadTexts:fsDot11WIDSDeviceAttackMacaddressListTable.setStatus(_A)
_FsDot11WIDSDeviceAttackMacaddressListEntry_Object=MibTableRow
fsDot11WIDSDeviceAttackMacaddressListEntry=_FsDot11WIDSDeviceAttackMacaddressListEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,3,1))
fsDot11WIDSDeviceAttackMacaddressListEntry.setIndexNames((0,_B,_Y))
if mibBuilder.loadTexts:fsDot11WIDSDeviceAttackMacaddressListEntry.setStatus(_A)
_FsDot11AttackNum_Type=Integer32
_FsDot11AttackNum_Object=MibTableColumn
fsDot11AttackNum=_FsDot11AttackNum_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,3,1,1),_FsDot11AttackNum_Type())
fsDot11AttackNum.setMaxAccess(_E)
if mibBuilder.loadTexts:fsDot11AttackNum.setStatus(_A)
_FsDot11AttackOper_Type=Integer32
_FsDot11AttackOper_Object=MibTableColumn
fsDot11AttackOper=_FsDot11AttackOper_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,3,1,2),_FsDot11AttackOper_Type())
fsDot11AttackOper.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot11AttackOper.setStatus(_A)
_FsDot11AttackMAC_Type=MacAddress
_FsDot11AttackMAC_Object=MibTableColumn
fsDot11AttackMAC=_FsDot11AttackMAC_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,3,1,3),_FsDot11AttackMAC_Type())
fsDot11AttackMAC.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot11AttackMAC.setStatus(_A)
class _FsDot11AttackInfo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_FsDot11AttackInfo_Type.__name__=_F
_FsDot11AttackInfo_Object=MibTableColumn
fsDot11AttackInfo=_FsDot11AttackInfo_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,3,1,4),_FsDot11AttackInfo_Type())
fsDot11AttackInfo.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDot11AttackInfo.setStatus(_A)
_FsDot11WIDSDevicePermitMacaddressListTable_Object=MibTable
fsDot11WIDSDevicePermitMacaddressListTable=_FsDot11WIDSDevicePermitMacaddressListTable_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,4))
if mibBuilder.loadTexts:fsDot11WIDSDevicePermitMacaddressListTable.setStatus(_A)
_FsDot11WIDSDevicePermitMacaddressListEntry_Object=MibTableRow
fsDot11WIDSDevicePermitMacaddressListEntry=_FsDot11WIDSDevicePermitMacaddressListEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,4,1))
fsDot11WIDSDevicePermitMacaddressListEntry.setIndexNames((0,_B,_Z))
if mibBuilder.loadTexts:fsDot11WIDSDevicePermitMacaddressListEntry.setStatus(_A)
_FsDot11PermitMACNum_Type=Integer32
_FsDot11PermitMACNum_Object=MibTableColumn
fsDot11PermitMACNum=_FsDot11PermitMACNum_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,4,1,1),_FsDot11PermitMACNum_Type())
fsDot11PermitMACNum.setMaxAccess(_E)
if mibBuilder.loadTexts:fsDot11PermitMACNum.setStatus(_A)
_FsDot11PermitMACOper_Type=Integer32
_FsDot11PermitMACOper_Object=MibTableColumn
fsDot11PermitMACOper=_FsDot11PermitMACOper_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,4,1,2),_FsDot11PermitMACOper_Type())
fsDot11PermitMACOper.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot11PermitMACOper.setStatus(_A)
_FsDot11PermitMACAddr_Type=MacAddress
_FsDot11PermitMACAddr_Object=MibTableColumn
fsDot11PermitMACAddr=_FsDot11PermitMACAddr_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,4,1,3),_FsDot11PermitMACAddr_Type())
fsDot11PermitMACAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot11PermitMACAddr.setStatus(_A)
_FsDot11WIDSDeviceagingDuration_Type=Integer32
_FsDot11WIDSDeviceagingDuration_Object=MibScalar
fsDot11WIDSDeviceagingDuration=_FsDot11WIDSDeviceagingDuration_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,5),_FsDot11WIDSDeviceagingDuration_Type())
fsDot11WIDSDeviceagingDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot11WIDSDeviceagingDuration.setStatus(_A)
_FsDot11WIDSCountermeasuresMode_Type=Integer32
_FsDot11WIDSCountermeasuresMode_Object=MibScalar
fsDot11WIDSCountermeasuresMode=_FsDot11WIDSCountermeasuresMode_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,6),_FsDot11WIDSCountermeasuresMode_Type())
fsDot11WIDSCountermeasuresMode.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot11WIDSCountermeasuresMode.setStatus(_A)
_FsDot11WIDSCountermeasureSet_Type=Integer32
_FsDot11WIDSCountermeasureSet_Object=MibScalar
fsDot11WIDSCountermeasureSet=_FsDot11WIDSCountermeasureSet_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,7),_FsDot11WIDSCountermeasureSet_Type())
fsDot11WIDSCountermeasureSet.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot11WIDSCountermeasureSet.setStatus(_A)
_FsDot11WIDSModeTable_Object=MibTable
fsDot11WIDSModeTable=_FsDot11WIDSModeTable_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,8))
if mibBuilder.loadTexts:fsDot11WIDSModeTable.setStatus(_A)
_FsDot11WIDSModeEntry_Object=MibTableRow
fsDot11WIDSModeEntry=_FsDot11WIDSModeEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,8,1))
fsDot11WIDSModeEntry.setIndexNames((0,_B,_a))
if mibBuilder.loadTexts:fsDot11WIDSModeEntry.setStatus(_A)
_FsDot11WIDSAPID_Type=Integer32
_FsDot11WIDSAPID_Object=MibTableColumn
fsDot11WIDSAPID=_FsDot11WIDSAPID_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,8,1,1),_FsDot11WIDSAPID_Type())
fsDot11WIDSAPID.setMaxAccess(_E)
if mibBuilder.loadTexts:fsDot11WIDSAPID.setStatus(_A)
_FsDot11WIDSDeviceMode_Type=Integer32
_FsDot11WIDSDeviceMode_Object=MibTableColumn
fsDot11WIDSDeviceMode=_FsDot11WIDSDeviceMode_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,8,1,2),_FsDot11WIDSDeviceMode_Type())
fsDot11WIDSDeviceMode.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot11WIDSDeviceMode.setStatus(_A)
_FsDot11WIDSWhitelistMacaddressListTable_Object=MibTable
fsDot11WIDSWhitelistMacaddressListTable=_FsDot11WIDSWhitelistMacaddressListTable_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,9))
if mibBuilder.loadTexts:fsDot11WIDSWhitelistMacaddressListTable.setStatus(_A)
_FsDot11WIDSWhitelistMacaddressListEntry_Object=MibTableRow
fsDot11WIDSWhitelistMacaddressListEntry=_FsDot11WIDSWhitelistMacaddressListEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,9,1))
fsDot11WIDSWhitelistMacaddressListEntry.setIndexNames((0,_B,_b))
if mibBuilder.loadTexts:fsDot11WIDSWhitelistMacaddressListEntry.setStatus(_A)
_FsDot11WhitelistNum_Type=Integer32
_FsDot11WhitelistNum_Object=MibTableColumn
fsDot11WhitelistNum=_FsDot11WhitelistNum_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,9,1,1),_FsDot11WhitelistNum_Type())
fsDot11WhitelistNum.setMaxAccess(_E)
if mibBuilder.loadTexts:fsDot11WhitelistNum.setStatus(_A)
_FsDot11WhitelistOper_Type=Integer32
_FsDot11WhitelistOper_Object=MibTableColumn
fsDot11WhitelistOper=_FsDot11WhitelistOper_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,9,1,2),_FsDot11WhitelistOper_Type())
fsDot11WhitelistOper.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot11WhitelistOper.setStatus(_A)
_FsDot11WhitelistMAC_Type=MacAddress
_FsDot11WhitelistMAC_Object=MibTableColumn
fsDot11WhitelistMAC=_FsDot11WhitelistMAC_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,9,1,3),_FsDot11WhitelistMAC_Type())
fsDot11WhitelistMAC.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot11WhitelistMAC.setStatus(_A)
_FsDot11WIDSStaticblackListTable_Object=MibTable
fsDot11WIDSStaticblackListTable=_FsDot11WIDSStaticblackListTable_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,10))
if mibBuilder.loadTexts:fsDot11WIDSStaticblackListTable.setStatus(_A)
_FsDot11WIDSStaticblackListEntry_Object=MibTableRow
fsDot11WIDSStaticblackListEntry=_FsDot11WIDSStaticblackListEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,10,1))
fsDot11WIDSStaticblackListEntry.setIndexNames((0,_B,_c))
if mibBuilder.loadTexts:fsDot11WIDSStaticblackListEntry.setStatus(_A)
_FsDot11StaticblacklistNum_Type=Integer32
_FsDot11StaticblacklistNum_Object=MibTableColumn
fsDot11StaticblacklistNum=_FsDot11StaticblacklistNum_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,10,1,1),_FsDot11StaticblacklistNum_Type())
fsDot11StaticblacklistNum.setMaxAccess(_E)
if mibBuilder.loadTexts:fsDot11StaticblacklistNum.setStatus(_A)
_FsDot11StaticblacklistOper_Type=Integer32
_FsDot11StaticblacklistOper_Object=MibTableColumn
fsDot11StaticblacklistOper=_FsDot11StaticblacklistOper_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,10,1,2),_FsDot11StaticblacklistOper_Type())
fsDot11StaticblacklistOper.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot11StaticblacklistOper.setStatus(_A)
_FsDot11StaticblacklistMAC_Type=MacAddress
_FsDot11StaticblacklistMAC_Object=MibTableColumn
fsDot11StaticblacklistMAC=_FsDot11StaticblacklistMAC_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,10,1,3),_FsDot11StaticblacklistMAC_Type())
fsDot11StaticblacklistMAC.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot11StaticblacklistMAC.setStatus(_A)
_FsDot11WIDSDynamicblacklistEnable_Type=TruthValue
_FsDot11WIDSDynamicblacklistEnable_Object=MibScalar
fsDot11WIDSDynamicblacklistEnable=_FsDot11WIDSDynamicblacklistEnable_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,11),_FsDot11WIDSDynamicblacklistEnable_Type())
fsDot11WIDSDynamicblacklistEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot11WIDSDynamicblacklistEnable.setStatus(_A)
_FsDot11WIDSDynamicblacklistLifetime_Type=Integer32
_FsDot11WIDSDynamicblacklistLifetime_Object=MibScalar
fsDot11WIDSDynamicblacklistLifetime=_FsDot11WIDSDynamicblacklistLifetime_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,12),_FsDot11WIDSDynamicblacklistLifetime_Type())
fsDot11WIDSDynamicblacklistLifetime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot11WIDSDynamicblacklistLifetime.setStatus(_A)
_FsDot11WIDSAttackDetectionMode_Type=Integer32
_FsDot11WIDSAttackDetectionMode_Object=MibScalar
fsDot11WIDSAttackDetectionMode=_FsDot11WIDSAttackDetectionMode_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,13),_FsDot11WIDSAttackDetectionMode_Type())
fsDot11WIDSAttackDetectionMode.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot11WIDSAttackDetectionMode.setStatus(_A)
_FsDot11WIDSRogueInfoTable_Object=MibTable
fsDot11WIDSRogueInfoTable=_FsDot11WIDSRogueInfoTable_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,14))
if mibBuilder.loadTexts:fsDot11WIDSRogueInfoTable.setStatus(_A)
_FsDot11WIDSRogueInfoEntry_Object=MibTableRow
fsDot11WIDSRogueInfoEntry=_FsDot11WIDSRogueInfoEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,14,1))
fsDot11WIDSRogueInfoEntry.setIndexNames((0,_B,_d),(0,_B,_e))
if mibBuilder.loadTexts:fsDot11WIDSRogueInfoEntry.setStatus(_A)
_FsDot11WIDSRogueInfoNUM_Type=Integer32
_FsDot11WIDSRogueInfoNUM_Object=MibTableColumn
fsDot11WIDSRogueInfoNUM=_FsDot11WIDSRogueInfoNUM_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,14,1,1),_FsDot11WIDSRogueInfoNUM_Type())
fsDot11WIDSRogueInfoNUM.setMaxAccess(_E)
if mibBuilder.loadTexts:fsDot11WIDSRogueInfoNUM.setStatus(_A)
_FsDot11WIDSRogueInfoTYPE_Type=Integer32
_FsDot11WIDSRogueInfoTYPE_Object=MibTableColumn
fsDot11WIDSRogueInfoTYPE=_FsDot11WIDSRogueInfoTYPE_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,14,1,2),_FsDot11WIDSRogueInfoTYPE_Type())
fsDot11WIDSRogueInfoTYPE.setMaxAccess(_E)
if mibBuilder.loadTexts:fsDot11WIDSRogueInfoTYPE.setStatus(_A)
_FsDot11WIDSRogueInfoOper_Type=Integer32
_FsDot11WIDSRogueInfoOper_Object=MibTableColumn
fsDot11WIDSRogueInfoOper=_FsDot11WIDSRogueInfoOper_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,14,1,3),_FsDot11WIDSRogueInfoOper_Type())
fsDot11WIDSRogueInfoOper.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot11WIDSRogueInfoOper.setStatus(_A)
_FsDot11WIDSRogueInfoMAC_Type=MacAddress
_FsDot11WIDSRogueInfoMAC_Object=MibTableColumn
fsDot11WIDSRogueInfoMAC=_FsDot11WIDSRogueInfoMAC_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,14,1,4),_FsDot11WIDSRogueInfoMAC_Type())
fsDot11WIDSRogueInfoMAC.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot11WIDSRogueInfoMAC.setStatus(_A)
_FsDot11WIDSRogueInfoString_Type=DisplayString
_FsDot11WIDSRogueInfoString_Object=MibTableColumn
fsDot11WIDSRogueInfoString=_FsDot11WIDSRogueInfoString_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,14,1,5),_FsDot11WIDSRogueInfoString_Type())
fsDot11WIDSRogueInfoString.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot11WIDSRogueInfoString.setStatus(_A)
_FsDot11WIDSPermitmaclistEnableTable_Object=MibTable
fsDot11WIDSPermitmaclistEnableTable=_FsDot11WIDSPermitmaclistEnableTable_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,15))
if mibBuilder.loadTexts:fsDot11WIDSPermitmaclistEnableTable.setStatus(_A)
_FsDot11WIDSPermitmaclistEnableEntry_Object=MibTableRow
fsDot11WIDSPermitmaclistEnableEntry=_FsDot11WIDSPermitmaclistEnableEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,15,1))
fsDot11WIDSPermitmaclistEnableEntry.setIndexNames((0,_B,_f))
if mibBuilder.loadTexts:fsDot11WIDSPermitmaclistEnableEntry.setStatus(_A)
_FsDot11WIDSEnableVlanPermitmaclistNum_Type=Integer32
_FsDot11WIDSEnableVlanPermitmaclistNum_Object=MibTableColumn
fsDot11WIDSEnableVlanPermitmaclistNum=_FsDot11WIDSEnableVlanPermitmaclistNum_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,15,1,1),_FsDot11WIDSEnableVlanPermitmaclistNum_Type())
fsDot11WIDSEnableVlanPermitmaclistNum.setMaxAccess(_E)
if mibBuilder.loadTexts:fsDot11WIDSEnableVlanPermitmaclistNum.setStatus(_A)
_FsDot11WIDSEnableVlanPermitmaclistOper_Type=Integer32
_FsDot11WIDSEnableVlanPermitmaclistOper_Object=MibTableColumn
fsDot11WIDSEnableVlanPermitmaclistOper=_FsDot11WIDSEnableVlanPermitmaclistOper_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,15,1,2),_FsDot11WIDSEnableVlanPermitmaclistOper_Type())
fsDot11WIDSEnableVlanPermitmaclistOper.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot11WIDSEnableVlanPermitmaclistOper.setStatus(_A)
_FsDot11WIDSEnableVlanPermitmaclist_Type=MacAddress
_FsDot11WIDSEnableVlanPermitmaclist_Object=MibTableColumn
fsDot11WIDSEnableVlanPermitmaclist=_FsDot11WIDSEnableVlanPermitmaclist_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,15,1,3),_FsDot11WIDSEnableVlanPermitmaclist_Type())
fsDot11WIDSEnableVlanPermitmaclist.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot11WIDSEnableVlanPermitmaclist.setStatus(_A)
_FsDot11WIDSResetStatistics_Type=TruthValue
_FsDot11WIDSResetStatistics_Object=MibScalar
fsDot11WIDSResetStatistics=_FsDot11WIDSResetStatistics_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,18),_FsDot11WIDSResetStatistics_Type())
fsDot11WIDSResetStatistics.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot11WIDSResetStatistics.setStatus(_A)
_FsDot11WIDSResetRoguehistoryStatistics_Type=Integer32
_FsDot11WIDSResetRoguehistoryStatistics_Object=MibScalar
fsDot11WIDSResetRoguehistoryStatistics=_FsDot11WIDSResetRoguehistoryStatistics_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,19),_FsDot11WIDSResetRoguehistoryStatistics_Type())
fsDot11WIDSResetRoguehistoryStatistics.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot11WIDSResetRoguehistoryStatistics.setStatus(_A)
_FsDot11WIDSResethistory_Type=Integer32
_FsDot11WIDSResethistory_Object=MibScalar
fsDot11WIDSResethistory=_FsDot11WIDSResethistory_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,20),_FsDot11WIDSResethistory_Type())
fsDot11WIDSResethistory.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot11WIDSResethistory.setStatus(_A)
_FsDot11WIDSResetDynamicBlacklistTable_Object=MibTable
fsDot11WIDSResetDynamicBlacklistTable=_FsDot11WIDSResetDynamicBlacklistTable_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,21))
if mibBuilder.loadTexts:fsDot11WIDSResetDynamicBlacklistTable.setStatus(_A)
_FsDot11WIDSResetDynamicBlacklistEntry_Object=MibTableRow
fsDot11WIDSResetDynamicBlacklistEntry=_FsDot11WIDSResetDynamicBlacklistEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,21,1))
fsDot11WIDSResetDynamicBlacklistEntry.setIndexNames((0,_B,_g))
if mibBuilder.loadTexts:fsDot11WIDSResetDynamicBlacklistEntry.setStatus(_A)
_FsDot11WIDSResetDynamicBlacklistMac_Type=MacAddress
_FsDot11WIDSResetDynamicBlacklistMac_Object=MibTableColumn
fsDot11WIDSResetDynamicBlacklistMac=_FsDot11WIDSResetDynamicBlacklistMac_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,21,1,1),_FsDot11WIDSResetDynamicBlacklistMac_Type())
fsDot11WIDSResetDynamicBlacklistMac.setMaxAccess(_E)
if mibBuilder.loadTexts:fsDot11WIDSResetDynamicBlacklistMac.setStatus(_A)
_FsDot11WIDSResetDynamicBlacklistType_Type=Integer32
_FsDot11WIDSResetDynamicBlacklistType_Object=MibTableColumn
fsDot11WIDSResetDynamicBlacklistType=_FsDot11WIDSResetDynamicBlacklistType_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,21,1,2),_FsDot11WIDSResetDynamicBlacklistType_Type())
fsDot11WIDSResetDynamicBlacklistType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot11WIDSResetDynamicBlacklistType.setStatus(_A)
_FsDot11WIDResetUserisolationStatistics_Type=Integer32
_FsDot11WIDResetUserisolationStatistics_Object=MibScalar
fsDot11WIDResetUserisolationStatistics=_FsDot11WIDResetUserisolationStatistics_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,22),_FsDot11WIDResetUserisolationStatistics_Type())
fsDot11WIDResetUserisolationStatistics.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot11WIDResetUserisolationStatistics.setStatus(_A)
_FsDot11WIDUserisolationAC_Type=Integer32
_FsDot11WIDUserisolationAC_Object=MibScalar
fsDot11WIDUserisolationAC=_FsDot11WIDUserisolationAC_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,23),_FsDot11WIDUserisolationAC_Type())
fsDot11WIDUserisolationAC.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot11WIDUserisolationAC.setStatus(_A)
_FsDot11WIDUserisolationAP_Type=Integer32
_FsDot11WIDUserisolationAP_Object=MibScalar
fsDot11WIDUserisolationAP=_FsDot11WIDUserisolationAP_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,24),_FsDot11WIDUserisolationAP_Type())
fsDot11WIDUserisolationAP.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot11WIDUserisolationAP.setStatus(_A)
_FsDot11WIDSShowStaticsTable_Object=MibTable
fsDot11WIDSShowStaticsTable=_FsDot11WIDSShowStaticsTable_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,25))
if mibBuilder.loadTexts:fsDot11WIDSShowStaticsTable.setStatus(_A)
_FsDot11WIDSShowStaticsEntry_Object=MibTableRow
fsDot11WIDSShowStaticsEntry=_FsDot11WIDSShowStaticsEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,25,1))
fsDot11WIDSShowStaticsEntry.setIndexNames((0,_B,_h))
if mibBuilder.loadTexts:fsDot11WIDSShowStaticsEntry.setStatus(_A)
_FsDot11WIDSShowStaticsNum_Type=Integer32
_FsDot11WIDSShowStaticsNum_Object=MibTableColumn
fsDot11WIDSShowStaticsNum=_FsDot11WIDSShowStaticsNum_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,25,1,1),_FsDot11WIDSShowStaticsNum_Type())
fsDot11WIDSShowStaticsNum.setMaxAccess(_E)
if mibBuilder.loadTexts:fsDot11WIDSShowStaticsNum.setStatus(_A)
_FsDot11WIDSShowStaticsOper_Type=Integer32
_FsDot11WIDSShowStaticsOper_Object=MibTableColumn
fsDot11WIDSShowStaticsOper=_FsDot11WIDSShowStaticsOper_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,25,1,2),_FsDot11WIDSShowStaticsOper_Type())
fsDot11WIDSShowStaticsOper.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot11WIDSShowStaticsOper.setStatus(_A)
_FsDot11WIDSShowStaticsMac_Type=MacAddress
_FsDot11WIDSShowStaticsMac_Object=MibTableColumn
fsDot11WIDSShowStaticsMac=_FsDot11WIDSShowStaticsMac_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,25,1,3),_FsDot11WIDSShowStaticsMac_Type())
fsDot11WIDSShowStaticsMac.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot11WIDSShowStaticsMac.setStatus(_A)
class _FsDot11WIDSShowStaticsInfo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_FsDot11WIDSShowStaticsInfo_Type.__name__=_F
_FsDot11WIDSShowStaticsInfo_Object=MibTableColumn
fsDot11WIDSShowStaticsInfo=_FsDot11WIDSShowStaticsInfo_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,25,1,4),_FsDot11WIDSShowStaticsInfo_Type())
fsDot11WIDSShowStaticsInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot11WIDSShowStaticsInfo.setStatus(_A)
_FsDot11WIDSAssociationFailureTotalTimes_Type=Integer32
_FsDot11WIDSAssociationFailureTotalTimes_Object=MibScalar
fsDot11WIDSAssociationFailureTotalTimes=_FsDot11WIDSAssociationFailureTotalTimes_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,26),_FsDot11WIDSAssociationFailureTotalTimes_Type())
fsDot11WIDSAssociationFailureTotalTimes.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDot11WIDSAssociationFailureTotalTimes.setStatus(_A)
_FsDot11WIDSSuspiciousAPInfoTable_Object=MibTable
fsDot11WIDSSuspiciousAPInfoTable=_FsDot11WIDSSuspiciousAPInfoTable_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,27))
if mibBuilder.loadTexts:fsDot11WIDSSuspiciousAPInfoTable.setStatus(_A)
_FsDot11WIDSSuspiciousAPInfoEntry_Object=MibTableRow
fsDot11WIDSSuspiciousAPInfoEntry=_FsDot11WIDSSuspiciousAPInfoEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,27,1))
fsDot11WIDSSuspiciousAPInfoEntry.setIndexNames((0,_B,_i))
if mibBuilder.loadTexts:fsDot11WIDSSuspiciousAPInfoEntry.setStatus(_A)
_FsDot11WIDSSuspiciousAPBSS_Type=MacAddress
_FsDot11WIDSSuspiciousAPBSS_Object=MibTableColumn
fsDot11WIDSSuspiciousAPBSS=_FsDot11WIDSSuspiciousAPBSS_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,27,1,1),_FsDot11WIDSSuspiciousAPBSS_Type())
fsDot11WIDSSuspiciousAPBSS.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDot11WIDSSuspiciousAPBSS.setStatus(_A)
_FsDot11WIDSSuspiciousAPCount_Type=Integer32
_FsDot11WIDSSuspiciousAPCount_Object=MibTableColumn
fsDot11WIDSSuspiciousAPCount=_FsDot11WIDSSuspiciousAPCount_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,27,1,2),_FsDot11WIDSSuspiciousAPCount_Type())
fsDot11WIDSSuspiciousAPCount.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDot11WIDSSuspiciousAPCount.setStatus(_A)
_FsDot11WIDSMomentFirstTimeDetectedSusAP_Type=TimeTicks
_FsDot11WIDSMomentFirstTimeDetectedSusAP_Object=MibTableColumn
fsDot11WIDSMomentFirstTimeDetectedSusAP=_FsDot11WIDSMomentFirstTimeDetectedSusAP_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,27,1,3),_FsDot11WIDSMomentFirstTimeDetectedSusAP_Type())
fsDot11WIDSMomentFirstTimeDetectedSusAP.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDot11WIDSMomentFirstTimeDetectedSusAP.setStatus(_A)
_FsDot11WIDSMomentLastTimeDetectedSusAP_Type=TimeTicks
_FsDot11WIDSMomentLastTimeDetectedSusAP_Object=MibTableColumn
fsDot11WIDSMomentLastTimeDetectedSusAP=_FsDot11WIDSMomentLastTimeDetectedSusAP_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,27,1,4),_FsDot11WIDSMomentLastTimeDetectedSusAP_Type())
fsDot11WIDSMomentLastTimeDetectedSusAP.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDot11WIDSMomentLastTimeDetectedSusAP.setStatus(_A)
_FsDot11WIDSSuspiciousAPSSID_Type=DisplayString
_FsDot11WIDSSuspiciousAPSSID_Object=MibTableColumn
fsDot11WIDSSuspiciousAPSSID=_FsDot11WIDSSuspiciousAPSSID_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,27,1,5),_FsDot11WIDSSuspiciousAPSSID_Type())
fsDot11WIDSSuspiciousAPSSID.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDot11WIDSSuspiciousAPSSID.setStatus(_A)
_FsDot11WIDSSuspiciousAPMaxSignalStrength_Type=Integer32
_FsDot11WIDSSuspiciousAPMaxSignalStrength_Object=MibTableColumn
fsDot11WIDSSuspiciousAPMaxSignalStrength=_FsDot11WIDSSuspiciousAPMaxSignalStrength_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,27,1,6),_FsDot11WIDSSuspiciousAPMaxSignalStrength_Type())
fsDot11WIDSSuspiciousAPMaxSignalStrength.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDot11WIDSSuspiciousAPMaxSignalStrength.setStatus(_A)
_FsDot11WIDSSuspiciousAPUsingChannel_Type=Integer32
_FsDot11WIDSSuspiciousAPUsingChannel_Object=MibTableColumn
fsDot11WIDSSuspiciousAPUsingChannel=_FsDot11WIDSSuspiciousAPUsingChannel_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,27,1,7),_FsDot11WIDSSuspiciousAPUsingChannel_Type())
fsDot11WIDSSuspiciousAPUsingChannel.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDot11WIDSSuspiciousAPUsingChannel.setStatus(_A)
_FsDot11WIDSSuspiciousAPFrameEncrption_Type=Integer32
_FsDot11WIDSSuspiciousAPFrameEncrption_Object=MibTableColumn
fsDot11WIDSSuspiciousAPFrameEncrption=_FsDot11WIDSSuspiciousAPFrameEncrption_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,27,1,8),_FsDot11WIDSSuspiciousAPFrameEncrption_Type())
fsDot11WIDSSuspiciousAPFrameEncrption.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDot11WIDSSuspiciousAPFrameEncrption.setStatus(_A)
_FsDot11WIDSSuspiciousAPNeedsDealingTag_Type=TruthValue
_FsDot11WIDSSuspiciousAPNeedsDealingTag_Object=MibTableColumn
fsDot11WIDSSuspiciousAPNeedsDealingTag=_FsDot11WIDSSuspiciousAPNeedsDealingTag_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,27,1,9),_FsDot11WIDSSuspiciousAPNeedsDealingTag_Type())
fsDot11WIDSSuspiciousAPNeedsDealingTag.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDot11WIDSSuspiciousAPNeedsDealingTag.setStatus(_A)
_FsDot11WIDSSuspiciousAPIgnoredTag_Type=TruthValue
_FsDot11WIDSSuspiciousAPIgnoredTag_Object=MibTableColumn
fsDot11WIDSSuspiciousAPIgnoredTag=_FsDot11WIDSSuspiciousAPIgnoredTag_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,27,1,10),_FsDot11WIDSSuspiciousAPIgnoredTag_Type())
fsDot11WIDSSuspiciousAPIgnoredTag.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDot11WIDSSuspiciousAPIgnoredTag.setStatus(_A)
_FsDot11WIDSSuspiciousSTAInfoTable_Object=MibTable
fsDot11WIDSSuspiciousSTAInfoTable=_FsDot11WIDSSuspiciousSTAInfoTable_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,28))
if mibBuilder.loadTexts:fsDot11WIDSSuspiciousSTAInfoTable.setStatus(_A)
_FsDot11WIDSSuspiciousSTAInfoEntry_Object=MibTableRow
fsDot11WIDSSuspiciousSTAInfoEntry=_FsDot11WIDSSuspiciousSTAInfoEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,28,1))
fsDot11WIDSSuspiciousSTAInfoEntry.setIndexNames((0,_B,_j))
if mibBuilder.loadTexts:fsDot11WIDSSuspiciousSTAInfoEntry.setStatus(_A)
_FsDot11WIDSSuspiciousSTAMAC_Type=MacAddress
_FsDot11WIDSSuspiciousSTAMAC_Object=MibTableColumn
fsDot11WIDSSuspiciousSTAMAC=_FsDot11WIDSSuspiciousSTAMAC_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,28,1,1),_FsDot11WIDSSuspiciousSTAMAC_Type())
fsDot11WIDSSuspiciousSTAMAC.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDot11WIDSSuspiciousSTAMAC.setStatus(_A)
_FsDot11WIDSAPCountDetectingSuspiciousSTA_Type=Integer32
_FsDot11WIDSAPCountDetectingSuspiciousSTA_Object=MibTableColumn
fsDot11WIDSAPCountDetectingSuspiciousSTA=_FsDot11WIDSAPCountDetectingSuspiciousSTA_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,28,1,2),_FsDot11WIDSAPCountDetectingSuspiciousSTA_Type())
fsDot11WIDSAPCountDetectingSuspiciousSTA.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDot11WIDSAPCountDetectingSuspiciousSTA.setStatus(_A)
_FsDot11WIDSMomentFirstTimeDetectedSusSTA_Type=TimeTicks
_FsDot11WIDSMomentFirstTimeDetectedSusSTA_Object=MibTableColumn
fsDot11WIDSMomentFirstTimeDetectedSusSTA=_FsDot11WIDSMomentFirstTimeDetectedSusSTA_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,28,1,3),_FsDot11WIDSMomentFirstTimeDetectedSusSTA_Type())
fsDot11WIDSMomentFirstTimeDetectedSusSTA.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDot11WIDSMomentFirstTimeDetectedSusSTA.setStatus(_A)
_FsDot11WIDSMomentLastTimeDetectedSusSTA_Type=TimeTicks
_FsDot11WIDSMomentLastTimeDetectedSusSTA_Object=MibTableColumn
fsDot11WIDSMomentLastTimeDetectedSusSTA=_FsDot11WIDSMomentLastTimeDetectedSusSTA_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,28,1,4),_FsDot11WIDSMomentLastTimeDetectedSusSTA_Type())
fsDot11WIDSMomentLastTimeDetectedSusSTA.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDot11WIDSMomentLastTimeDetectedSusSTA.setStatus(_A)
_FsDot11WIDSBSSIDSuspiciousSTAAccessing_Type=MacAddress
_FsDot11WIDSBSSIDSuspiciousSTAAccessing_Object=MibTableColumn
fsDot11WIDSBSSIDSuspiciousSTAAccessing=_FsDot11WIDSBSSIDSuspiciousSTAAccessing_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,28,1,5),_FsDot11WIDSBSSIDSuspiciousSTAAccessing_Type())
fsDot11WIDSBSSIDSuspiciousSTAAccessing.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDot11WIDSBSSIDSuspiciousSTAAccessing.setStatus(_A)
_FsDot11WIDSSuspiciousSTAMaxSignalStrength_Type=Integer32
_FsDot11WIDSSuspiciousSTAMaxSignalStrength_Object=MibTableColumn
fsDot11WIDSSuspiciousSTAMaxSignalStrength=_FsDot11WIDSSuspiciousSTAMaxSignalStrength_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,28,1,6),_FsDot11WIDSSuspiciousSTAMaxSignalStrength_Type())
fsDot11WIDSSuspiciousSTAMaxSignalStrength.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDot11WIDSSuspiciousSTAMaxSignalStrength.setStatus(_A)
_FsDot11WIDSSuspiciousSTAUsingChannel_Type=Integer32
_FsDot11WIDSSuspiciousSTAUsingChannel_Object=MibTableColumn
fsDot11WIDSSuspiciousSTAUsingChannel=_FsDot11WIDSSuspiciousSTAUsingChannel_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,28,1,7),_FsDot11WIDSSuspiciousSTAUsingChannel_Type())
fsDot11WIDSSuspiciousSTAUsingChannel.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDot11WIDSSuspiciousSTAUsingChannel.setStatus(_A)
_FsDot11WIDSSuspiciousSTAWorksInAdhocMode_Type=TruthValue
_FsDot11WIDSSuspiciousSTAWorksInAdhocMode_Object=MibTableColumn
fsDot11WIDSSuspiciousSTAWorksInAdhocMode=_FsDot11WIDSSuspiciousSTAWorksInAdhocMode_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,28,1,8),_FsDot11WIDSSuspiciousSTAWorksInAdhocMode_Type())
fsDot11WIDSSuspiciousSTAWorksInAdhocMode.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDot11WIDSSuspiciousSTAWorksInAdhocMode.setStatus(_A)
_FsDot11WIDSSuspiciousSTANeedsDealingTag_Type=TruthValue
_FsDot11WIDSSuspiciousSTANeedsDealingTag_Object=MibTableColumn
fsDot11WIDSSuspiciousSTANeedsDealingTag=_FsDot11WIDSSuspiciousSTANeedsDealingTag_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,28,1,9),_FsDot11WIDSSuspiciousSTANeedsDealingTag_Type())
fsDot11WIDSSuspiciousSTANeedsDealingTag.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDot11WIDSSuspiciousSTANeedsDealingTag.setStatus(_A)
_FsDot11WIDSSuspiciousSTAIgnoredTag_Type=TruthValue
_FsDot11WIDSSuspiciousSTAIgnoredTag_Object=MibTableColumn
fsDot11WIDSSuspiciousSTAIgnoredTag=_FsDot11WIDSSuspiciousSTAIgnoredTag_Object((1,3,6,1,4,1,52642,1,1,10,2,62,1,28,1,10),_FsDot11WIDSSuspiciousSTAIgnoredTag_Type())
fsDot11WIDSSuspiciousSTAIgnoredTag.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot11WIDSSuspiciousSTAIgnoredTag.setStatus(_A)
_FsDot11WIDSDetectObjects_ObjectIdentity=ObjectIdentity
fsDot11WIDSDetectObjects=_FsDot11WIDSDetectObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,62,2))
_FsDot11WIDSShowDot11IdsAttacklistTable_Object=MibTable
fsDot11WIDSShowDot11IdsAttacklistTable=_FsDot11WIDSShowDot11IdsAttacklistTable_Object((1,3,6,1,4,1,52642,1,1,10,2,62,2,1))
if mibBuilder.loadTexts:fsDot11WIDSShowDot11IdsAttacklistTable.setStatus(_A)
_FsDot11WIDSShowDot11IdsAttacklistEntry_Object=MibTableRow
fsDot11WIDSShowDot11IdsAttacklistEntry=_FsDot11WIDSShowDot11IdsAttacklistEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,62,2,1,1))
fsDot11WIDSShowDot11IdsAttacklistEntry.setIndexNames((0,_B,_k))
if mibBuilder.loadTexts:fsDot11WIDSShowDot11IdsAttacklistEntry.setStatus(_A)
_FsDot11WIDSShowDot11IdsAttacklistNum_Type=Integer32
_FsDot11WIDSShowDot11IdsAttacklistNum_Object=MibTableColumn
fsDot11WIDSShowDot11IdsAttacklistNum=_FsDot11WIDSShowDot11IdsAttacklistNum_Object((1,3,6,1,4,1,52642,1,1,10,2,62,2,1,1,1),_FsDot11WIDSShowDot11IdsAttacklistNum_Type())
fsDot11WIDSShowDot11IdsAttacklistNum.setMaxAccess(_E)
if mibBuilder.loadTexts:fsDot11WIDSShowDot11IdsAttacklistNum.setStatus(_A)
_FsDot11WIDSShowDot11IdsAttacklistOper_Type=Integer32
_FsDot11WIDSShowDot11IdsAttacklistOper_Object=MibTableColumn
fsDot11WIDSShowDot11IdsAttacklistOper=_FsDot11WIDSShowDot11IdsAttacklistOper_Object((1,3,6,1,4,1,52642,1,1,10,2,62,2,1,1,2),_FsDot11WIDSShowDot11IdsAttacklistOper_Type())
fsDot11WIDSShowDot11IdsAttacklistOper.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot11WIDSShowDot11IdsAttacklistOper.setStatus(_A)
_FsDot11WIDSShowDot11IdsAttacklistMac_Type=MacAddress
_FsDot11WIDSShowDot11IdsAttacklistMac_Object=MibTableColumn
fsDot11WIDSShowDot11IdsAttacklistMac=_FsDot11WIDSShowDot11IdsAttacklistMac_Object((1,3,6,1,4,1,52642,1,1,10,2,62,2,1,1,3),_FsDot11WIDSShowDot11IdsAttacklistMac_Type())
fsDot11WIDSShowDot11IdsAttacklistMac.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot11WIDSShowDot11IdsAttacklistMac.setStatus(_A)
class _FsDot11WIDSShowDot11IdsAttacklistInfo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_FsDot11WIDSShowDot11IdsAttacklistInfo_Type.__name__=_F
_FsDot11WIDSShowDot11IdsAttacklistInfo_Object=MibTableColumn
fsDot11WIDSShowDot11IdsAttacklistInfo=_FsDot11WIDSShowDot11IdsAttacklistInfo_Object((1,3,6,1,4,1,52642,1,1,10,2,62,2,1,1,4),_FsDot11WIDSShowDot11IdsAttacklistInfo_Type())
fsDot11WIDSShowDot11IdsAttacklistInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot11WIDSShowDot11IdsAttacklistInfo.setStatus(_A)
_FsDot11WIDSTrapsObjects_ObjectIdentity=ObjectIdentity
fsDot11WIDSTrapsObjects=_FsDot11WIDSTrapsObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,62,3))
_FsDot11WIDSSTAMAC_Type=MacAddress
_FsDot11WIDSSTAMAC_Object=MibScalar
fsDot11WIDSSTAMAC=_FsDot11WIDSSTAMAC_Object((1,3,6,1,4,1,52642,1,1,10,2,62,3,1),_FsDot11WIDSSTAMAC_Type())
fsDot11WIDSSTAMAC.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot11WIDSSTAMAC.setStatus(_A)
class _FsDot11WIDSAPBSSID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_FsDot11WIDSAPBSSID_Type.__name__=_F
_FsDot11WIDSAPBSSID_Object=MibScalar
fsDot11WIDSAPBSSID=_FsDot11WIDSAPBSSID_Object((1,3,6,1,4,1,52642,1,1,10,2,62,3,2),_FsDot11WIDSAPBSSID_Type())
fsDot11WIDSAPBSSID.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot11WIDSAPBSSID.setStatus(_A)
class _FsDot11WIDSInformation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_FsDot11WIDSInformation_Type.__name__=_F
_FsDot11WIDSInformation_Object=MibScalar
fsDot11WIDSInformation=_FsDot11WIDSInformation_Object((1,3,6,1,4,1,52642,1,1,10,2,62,3,3),_FsDot11WIDSInformation_Type())
fsDot11WIDSInformation.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot11WIDSInformation.setStatus(_A)
class _FsDot11WIDSextinfo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_FsDot11WIDSextinfo_Type.__name__=_F
_FsDot11WIDSextinfo_Object=MibScalar
fsDot11WIDSextinfo=_FsDot11WIDSextinfo_Object((1,3,6,1,4,1,52642,1,1,10,2,62,3,4),_FsDot11WIDSextinfo_Type())
fsDot11WIDSextinfo.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot11WIDSextinfo.setStatus(_A)
_FsDot11WIDSDeviceInfoNUM_Type=Integer32
_FsDot11WIDSDeviceInfoNUM_Object=MibScalar
fsDot11WIDSDeviceInfoNUM=_FsDot11WIDSDeviceInfoNUM_Object((1,3,6,1,4,1,52642,1,1,10,2,62,3,5),_FsDot11WIDSDeviceInfoNUM_Type())
fsDot11WIDSDeviceInfoNUM.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot11WIDSDeviceInfoNUM.setStatus(_A)
_FsDot11WIDSDeviceInfoTYPE_Type=Integer32
_FsDot11WIDSDeviceInfoTYPE_Object=MibScalar
fsDot11WIDSDeviceInfoTYPE=_FsDot11WIDSDeviceInfoTYPE_Object((1,3,6,1,4,1,52642,1,1,10,2,62,3,6),_FsDot11WIDSDeviceInfoTYPE_Type())
fsDot11WIDSDeviceInfoTYPE.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot11WIDSDeviceInfoTYPE.setStatus(_A)
_FsDot11WIDSDeviceInfoOper_Type=Integer32
_FsDot11WIDSDeviceInfoOper_Object=MibScalar
fsDot11WIDSDeviceInfoOper=_FsDot11WIDSDeviceInfoOper_Object((1,3,6,1,4,1,52642,1,1,10,2,62,3,7),_FsDot11WIDSDeviceInfoOper_Type())
fsDot11WIDSDeviceInfoOper.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot11WIDSDeviceInfoOper.setStatus(_A)
_FsDot11WIDSDeviceInfoMAC_Type=MacAddress
_FsDot11WIDSDeviceInfoMAC_Object=MibScalar
fsDot11WIDSDeviceInfoMAC=_FsDot11WIDSDeviceInfoMAC_Object((1,3,6,1,4,1,52642,1,1,10,2,62,3,8),_FsDot11WIDSDeviceInfoMAC_Type())
fsDot11WIDSDeviceInfoMAC.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot11WIDSDeviceInfoMAC.setStatus(_A)
class _FsDot11WIDSDeviceInfoString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_FsDot11WIDSDeviceInfoString_Type.__name__=_F
_FsDot11WIDSDeviceInfoString_Object=MibScalar
fsDot11WIDSDeviceInfoString=_FsDot11WIDSDeviceInfoString_Object((1,3,6,1,4,1,52642,1,1,10,2,62,3,9),_FsDot11WIDSDeviceInfoString_Type())
fsDot11WIDSDeviceInfoString.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot11WIDSDeviceInfoString.setStatus(_A)
_FsDot11WIDSSuspiciousDeviceMac_Type=MacAddress
_FsDot11WIDSSuspiciousDeviceMac_Object=MibScalar
fsDot11WIDSSuspiciousDeviceMac=_FsDot11WIDSSuspiciousDeviceMac_Object((1,3,6,1,4,1,52642,1,1,10,2,62,3,10),_FsDot11WIDSSuspiciousDeviceMac_Type())
fsDot11WIDSSuspiciousDeviceMac.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot11WIDSSuspiciousDeviceMac.setStatus(_A)
_FsDot11WIDSSuspiciousDeviceExtensionInfo_Type=DisplayString
_FsDot11WIDSSuspiciousDeviceExtensionInfo_Object=MibScalar
fsDot11WIDSSuspiciousDeviceExtensionInfo=_FsDot11WIDSSuspiciousDeviceExtensionInfo_Object((1,3,6,1,4,1,52642,1,1,10,2,62,3,11),_FsDot11WIDSSuspiciousDeviceExtensionInfo_Type())
fsDot11WIDSSuspiciousDeviceExtensionInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot11WIDSSuspiciousDeviceExtensionInfo.setStatus(_A)
_FsDot11WIDSUnauthorizedSSID_Type=DisplayString
_FsDot11WIDSUnauthorizedSSID_Object=MibScalar
fsDot11WIDSUnauthorizedSSID=_FsDot11WIDSUnauthorizedSSID_Object((1,3,6,1,4,1,52642,1,1,10,2,62,3,12),_FsDot11WIDSUnauthorizedSSID_Type())
fsDot11WIDSUnauthorizedSSID.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot11WIDSUnauthorizedSSID.setStatus(_A)
_FsDot11WIDSSUnauthorizedSSIDExtensionInfo_Type=DisplayString
_FsDot11WIDSSUnauthorizedSSIDExtensionInfo_Object=MibScalar
fsDot11WIDSSUnauthorizedSSIDExtensionInfo=_FsDot11WIDSSUnauthorizedSSIDExtensionInfo_Object((1,3,6,1,4,1,52642,1,1,10,2,62,3,13),_FsDot11WIDSSUnauthorizedSSIDExtensionInfo_Type())
fsDot11WIDSSUnauthorizedSSIDExtensionInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot11WIDSSUnauthorizedSSIDExtensionInfo.setStatus(_A)
_FsDot11WIDSAttackingDeviceMac_Type=MacAddress
_FsDot11WIDSAttackingDeviceMac_Object=MibScalar
fsDot11WIDSAttackingDeviceMac=_FsDot11WIDSAttackingDeviceMac_Object((1,3,6,1,4,1,52642,1,1,10,2,62,3,14),_FsDot11WIDSAttackingDeviceMac_Type())
fsDot11WIDSAttackingDeviceMac.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot11WIDSAttackingDeviceMac.setStatus(_A)
_FsDot11WIDSAttackType_Type=Integer32
_FsDot11WIDSAttackType_Object=MibScalar
fsDot11WIDSAttackType=_FsDot11WIDSAttackType_Object((1,3,6,1,4,1,52642,1,1,10,2,62,3,15),_FsDot11WIDSAttackType_Type())
fsDot11WIDSAttackType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot11WIDSAttackType.setStatus(_A)
_FsDot11WIDSAttackExtensionInfo_Type=DisplayString
_FsDot11WIDSAttackExtensionInfo_Object=MibScalar
fsDot11WIDSAttackExtensionInfo=_FsDot11WIDSAttackExtensionInfo_Object((1,3,6,1,4,1,52642,1,1,10,2,62,3,16),_FsDot11WIDSAttackExtensionInfo_Type())
fsDot11WIDSAttackExtensionInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDot11WIDSAttackExtensionInfo.setStatus(_A)
_FsDot11WIDSMIBConform_ObjectIdentity=ObjectIdentity
fsDot11WIDSMIBConform=_FsDot11WIDSMIBConform_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,62,4))
_FsDot11WIDSMIBCompliances_ObjectIdentity=ObjectIdentity
fsDot11WIDSMIBCompliances=_FsDot11WIDSMIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,62,4,1))
_FsDot11WIDSMIBGroups_ObjectIdentity=ObjectIdentity
fsDot11WIDSMIBGroups=_FsDot11WIDSMIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,62,4,2))
fsDot11WIDSMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,62,4,2,1))
fsDot11WIDSMIBGroup.setObjects(*((_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:fsDot11WIDSMIBGroup.setStatus(_A)
fsDot11WIDSWirelessUserConnect=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,62,0,1))
fsDot11WIDSWirelessUserConnect.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:fsDot11WIDSWirelessUserConnect.setStatus(_A)
fsDot11WIDSWirelessUserDisconnect=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,62,0,2))
fsDot11WIDSWirelessUserDisconnect.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:fsDot11WIDSWirelessUserDisconnect.setStatus(_A)
fsDot11WIDSWirelessUserReauthentication=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,62,0,3))
fsDot11WIDSWirelessUserReauthentication.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:fsDot11WIDSWirelessUserReauthentication.setStatus(_A)
fsDot11WIDSWirelessUserAuthenticationFailure=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,62,0,4))
fsDot11WIDSWirelessUserAuthenticationFailure.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:fsDot11WIDSWirelessUserAuthenticationFailure.setStatus(_A)
fsDot11WIDSWirelessUserConnectFailure=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,62,0,5))
fsDot11WIDSWirelessUserConnectFailure.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:fsDot11WIDSWirelessUserConnectFailure.setStatus(_A)
fsDot11WIDSDevice=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,62,0,6))
fsDot11WIDSDevice.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:fsDot11WIDSDevice.setStatus(_A)
fsDot11WIDSSuspiciousDeviceTrap=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,62,0,7))
fsDot11WIDSSuspiciousDeviceTrap.setObjects(*((_B,_K),(_B,_L)))
if mibBuilder.loadTexts:fsDot11WIDSSuspiciousDeviceTrap.setStatus(_A)
fsDot11WIDSUnauthorizedSSIDTrap=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,62,0,8))
fsDot11WIDSUnauthorizedSSIDTrap.setObjects(*((_B,_M),(_B,_N)))
if mibBuilder.loadTexts:fsDot11WIDSUnauthorizedSSIDTrap.setStatus(_A)
fsDot11WIDSDetectingAttackTrap=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,62,0,9))
fsDot11WIDSDetectingAttackTrap.setObjects(*((_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:fsDot11WIDSDetectingAttackTrap.setStatus(_A)
fsDot11WIDSMIBCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,62,4,1,1))
fsDot11WIDSMIBCompliance.setObjects((_B,_Ag))
if mibBuilder.loadTexts:fsDot11WIDSMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fsDot11WIDSMIB':fsDot11WIDSMIB,'fsDot11WIDSTraps':fsDot11WIDSTraps,'fsDot11WIDSWirelessUserConnect':fsDot11WIDSWirelessUserConnect,'fsDot11WIDSWirelessUserDisconnect':fsDot11WIDSWirelessUserDisconnect,'fsDot11WIDSWirelessUserReauthentication':fsDot11WIDSWirelessUserReauthentication,'fsDot11WIDSWirelessUserAuthenticationFailure':fsDot11WIDSWirelessUserAuthenticationFailure,'fsDot11WIDSWirelessUserConnectFailure':fsDot11WIDSWirelessUserConnectFailure,'fsDot11WIDSDevice':fsDot11WIDSDevice,'fsDot11WIDSSuspiciousDeviceTrap':fsDot11WIDSSuspiciousDeviceTrap,'fsDot11WIDSUnauthorizedSSIDTrap':fsDot11WIDSUnauthorizedSSIDTrap,'fsDot11WIDSDetectingAttackTrap':fsDot11WIDSDetectingAttackTrap,'fsDot11WIDSConfigObjects':fsDot11WIDSConfigObjects,'fsDot11WIDSPermitVendorTable':fsDot11WIDSPermitVendorTable,'fsDot11WIDSPermitVendorEntry':fsDot11WIDSPermitVendorEntry,_W:fsDot11VendorOUI,_l:fsDot11VendorOper,_m:fsDot11VendorName,'fsDot11WIDSPermitSSIDTable':fsDot11WIDSPermitSSIDTable,'fsDot11WIDSPermitSSIDEntry':fsDot11WIDSPermitSSIDEntry,_X:fsDot11PermitNum,_n:fsDot11PermitOper,_o:fsDot11PermitSSID,'fsDot11WIDSDeviceAttackMacaddressListTable':fsDot11WIDSDeviceAttackMacaddressListTable,'fsDot11WIDSDeviceAttackMacaddressListEntry':fsDot11WIDSDeviceAttackMacaddressListEntry,_Y:fsDot11AttackNum,_p:fsDot11AttackOper,_q:fsDot11AttackMAC,_r:fsDot11AttackInfo,'fsDot11WIDSDevicePermitMacaddressListTable':fsDot11WIDSDevicePermitMacaddressListTable,'fsDot11WIDSDevicePermitMacaddressListEntry':fsDot11WIDSDevicePermitMacaddressListEntry,_Z:fsDot11PermitMACNum,_s:fsDot11PermitMACOper,_t:fsDot11PermitMACAddr,_u:fsDot11WIDSDeviceagingDuration,_v:fsDot11WIDSCountermeasuresMode,_w:fsDot11WIDSCountermeasureSet,'fsDot11WIDSModeTable':fsDot11WIDSModeTable,'fsDot11WIDSModeEntry':fsDot11WIDSModeEntry,_a:fsDot11WIDSAPID,_x:fsDot11WIDSDeviceMode,'fsDot11WIDSWhitelistMacaddressListTable':fsDot11WIDSWhitelistMacaddressListTable,'fsDot11WIDSWhitelistMacaddressListEntry':fsDot11WIDSWhitelistMacaddressListEntry,_b:fsDot11WhitelistNum,_y:fsDot11WhitelistOper,_z:fsDot11WhitelistMAC,'fsDot11WIDSStaticblackListTable':fsDot11WIDSStaticblackListTable,'fsDot11WIDSStaticblackListEntry':fsDot11WIDSStaticblackListEntry,_c:fsDot11StaticblacklistNum,_A0:fsDot11StaticblacklistOper,_A1:fsDot11StaticblacklistMAC,_A2:fsDot11WIDSDynamicblacklistEnable,_A3:fsDot11WIDSDynamicblacklistLifetime,_A4:fsDot11WIDSAttackDetectionMode,'fsDot11WIDSRogueInfoTable':fsDot11WIDSRogueInfoTable,'fsDot11WIDSRogueInfoEntry':fsDot11WIDSRogueInfoEntry,_d:fsDot11WIDSRogueInfoNUM,_e:fsDot11WIDSRogueInfoTYPE,_A5:fsDot11WIDSRogueInfoOper,_A6:fsDot11WIDSRogueInfoMAC,_A7:fsDot11WIDSRogueInfoString,'fsDot11WIDSPermitmaclistEnableTable':fsDot11WIDSPermitmaclistEnableTable,'fsDot11WIDSPermitmaclistEnableEntry':fsDot11WIDSPermitmaclistEnableEntry,_f:fsDot11WIDSEnableVlanPermitmaclistNum,_A8:fsDot11WIDSEnableVlanPermitmaclistOper,_A9:fsDot11WIDSEnableVlanPermitmaclist,_AA:fsDot11WIDSResetStatistics,_AB:fsDot11WIDSResetRoguehistoryStatistics,_AC:fsDot11WIDSResethistory,'fsDot11WIDSResetDynamicBlacklistTable':fsDot11WIDSResetDynamicBlacklistTable,'fsDot11WIDSResetDynamicBlacklistEntry':fsDot11WIDSResetDynamicBlacklistEntry,_g:fsDot11WIDSResetDynamicBlacklistMac,_AD:fsDot11WIDSResetDynamicBlacklistType,_AE:fsDot11WIDResetUserisolationStatistics,_AI:fsDot11WIDUserisolationAC,_AJ:fsDot11WIDUserisolationAP,'fsDot11WIDSShowStaticsTable':fsDot11WIDSShowStaticsTable,'fsDot11WIDSShowStaticsEntry':fsDot11WIDSShowStaticsEntry,_h:fsDot11WIDSShowStaticsNum,_AK:fsDot11WIDSShowStaticsOper,_AL:fsDot11WIDSShowStaticsMac,_AM:fsDot11WIDSShowStaticsInfo,_AN:fsDot11WIDSAssociationFailureTotalTimes,'fsDot11WIDSSuspiciousAPInfoTable':fsDot11WIDSSuspiciousAPInfoTable,'fsDot11WIDSSuspiciousAPInfoEntry':fsDot11WIDSSuspiciousAPInfoEntry,_i:fsDot11WIDSSuspiciousAPBSS,_AO:fsDot11WIDSSuspiciousAPCount,_AP:fsDot11WIDSMomentFirstTimeDetectedSusAP,_AQ:fsDot11WIDSMomentLastTimeDetectedSusAP,_AR:fsDot11WIDSSuspiciousAPSSID,_AS:fsDot11WIDSSuspiciousAPMaxSignalStrength,_AT:fsDot11WIDSSuspiciousAPUsingChannel,_AU:fsDot11WIDSSuspiciousAPFrameEncrption,_AV:fsDot11WIDSSuspiciousAPNeedsDealingTag,_AW:fsDot11WIDSSuspiciousAPIgnoredTag,'fsDot11WIDSSuspiciousSTAInfoTable':fsDot11WIDSSuspiciousSTAInfoTable,'fsDot11WIDSSuspiciousSTAInfoEntry':fsDot11WIDSSuspiciousSTAInfoEntry,_j:fsDot11WIDSSuspiciousSTAMAC,_AX:fsDot11WIDSAPCountDetectingSuspiciousSTA,_AY:fsDot11WIDSMomentFirstTimeDetectedSusSTA,_AZ:fsDot11WIDSMomentLastTimeDetectedSusSTA,_Aa:fsDot11WIDSBSSIDSuspiciousSTAAccessing,_Ab:fsDot11WIDSSuspiciousSTAMaxSignalStrength,_Ac:fsDot11WIDSSuspiciousSTAUsingChannel,_Ad:fsDot11WIDSSuspiciousSTAWorksInAdhocMode,_Ae:fsDot11WIDSSuspiciousSTANeedsDealingTag,_Af:fsDot11WIDSSuspiciousSTAIgnoredTag,'fsDot11WIDSDetectObjects':fsDot11WIDSDetectObjects,'fsDot11WIDSShowDot11IdsAttacklistTable':fsDot11WIDSShowDot11IdsAttacklistTable,'fsDot11WIDSShowDot11IdsAttacklistEntry':fsDot11WIDSShowDot11IdsAttacklistEntry,_k:fsDot11WIDSShowDot11IdsAttacklistNum,_AF:fsDot11WIDSShowDot11IdsAttacklistOper,_AG:fsDot11WIDSShowDot11IdsAttacklistMac,_AH:fsDot11WIDSShowDot11IdsAttacklistInfo,'fsDot11WIDSTrapsObjects':fsDot11WIDSTrapsObjects,_G:fsDot11WIDSSTAMAC,_H:fsDot11WIDSAPBSSID,_I:fsDot11WIDSInformation,_J:fsDot11WIDSextinfo,_R:fsDot11WIDSDeviceInfoNUM,_S:fsDot11WIDSDeviceInfoTYPE,_T:fsDot11WIDSDeviceInfoOper,_U:fsDot11WIDSDeviceInfoMAC,_V:fsDot11WIDSDeviceInfoString,_K:fsDot11WIDSSuspiciousDeviceMac,_L:fsDot11WIDSSuspiciousDeviceExtensionInfo,_M:fsDot11WIDSUnauthorizedSSID,_N:fsDot11WIDSSUnauthorizedSSIDExtensionInfo,_O:fsDot11WIDSAttackingDeviceMac,_P:fsDot11WIDSAttackType,_Q:fsDot11WIDSAttackExtensionInfo,'fsDot11WIDSMIBConform':fsDot11WIDSMIBConform,'fsDot11WIDSMIBCompliances':fsDot11WIDSMIBCompliances,'fsDot11WIDSMIBCompliance':fsDot11WIDSMIBCompliance,'fsDot11WIDSMIBGroups':fsDot11WIDSMIBGroups,_Ag:fsDot11WIDSMIBGroup})