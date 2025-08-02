_Ag='qtechDot11WIDSMIBGroup'
_Af='qtechDot11WIDSSuspiciousSTAIgnoredTag'
_Ae='qtechDot11WIDSSuspiciousSTANeedsDealingTag'
_Ad='qtechDot11WIDSSuspiciousSTAWorksInAdhocMode'
_Ac='qtechDot11WIDSSuspiciousSTAUsingChannel'
_Ab='qtechDot11WIDSSuspiciousSTAMaxSignalStrength'
_Aa='qtechDot11WIDSBSSIDSuspiciousSTAAccessing'
_AZ='qtechDot11WIDSMomentLastTimeDetectedSusSTA'
_AY='qtechDot11WIDSMomentFirstTimeDetectedSusSTA'
_AX='qtechDot11WIDSAPCountDetectingSuspiciousSTA'
_AW='qtechDot11WIDSSuspiciousAPIgnoredTag'
_AV='qtechDot11WIDSSuspiciousAPNeedsDealingTag'
_AU='qtechDot11WIDSSuspiciousAPFrameEncrption'
_AT='qtechDot11WIDSSuspiciousAPUsingChannel'
_AS='qtechDot11WIDSSuspiciousAPMaxSignalStrength'
_AR='qtechDot11WIDSSuspiciousAPSSID'
_AQ='qtechDot11WIDSMomentLastTimeDetectedSusAP'
_AP='qtechDot11WIDSMomentFirstTimeDetectedSusAP'
_AO='qtechDot11WIDSSuspiciousAPCount'
_AN='qtechDot11WIDSAssociationFailureTotalTimes'
_AM='qtechDot11WIDSShowStaticsInfo'
_AL='qtechDot11WIDSShowStaticsMac'
_AK='qtechDot11WIDSShowStaticsOper'
_AJ='qtechDot11WIDUserisolationAP'
_AI='qtechDot11WIDUserisolationAC'
_AH='qtechDot11WIDSShowDot11IdsAttacklistInfo'
_AG='qtechDot11WIDSShowDot11IdsAttacklistMac'
_AF='qtechDot11WIDSShowDot11IdsAttacklistOper'
_AE='qtechDot11WIDResetUserisolationStatistics'
_AD='qtechDot11WIDSResetDynamicBlacklistType'
_AC='qtechDot11WIDSResethistory'
_AB='qtechDot11WIDSResetRoguehistoryStatistics'
_AA='qtechDot11WIDSResetStatistics'
_A9='qtechDot11WIDSEnableVlanPermitmaclist'
_A8='qtechDot11WIDSEnableVlanPermitmaclistOper'
_A7='qtechDot11WIDSRogueInfoString'
_A6='qtechDot11WIDSRogueInfoMAC'
_A5='qtechDot11WIDSRogueInfoOper'
_A4='qtechDot11WIDSAttackDetectionMode'
_A3='qtechDot11WIDSDynamicblacklistLifetime'
_A2='qtechDot11WIDSDynamicblacklistEnable'
_A1='qtechDot11StaticblacklistMAC'
_A0='qtechDot11StaticblacklistOper'
_z='qtechDot11WhitelistMAC'
_y='qtechDot11WhitelistOper'
_x='qtechDot11WIDSDeviceMode'
_w='qtechDot11WIDSCountermeasureSet'
_v='qtechDot11WIDSCountermeasuresMode'
_u='qtechDot11WIDSDeviceagingDuration'
_t='qtechDot11PermitMACAddr'
_s='qtechDot11PermitMACOper'
_r='qtechDot11AttackInfo'
_q='qtechDot11AttackMAC'
_p='qtechDot11AttackOper'
_o='qtechDot11PermitSSID'
_n='qtechDot11PermitOper'
_m='qtechDot11VendorName'
_l='qtechDot11VendorOper'
_k='qtechDot11WIDSShowDot11IdsAttacklistNum'
_j='qtechDot11WIDSSuspiciousSTAMAC'
_i='qtechDot11WIDSSuspiciousAPBSS'
_h='qtechDot11WIDSShowStaticsNum'
_g='qtechDot11WIDSResetDynamicBlacklistMac'
_f='qtechDot11WIDSEnableVlanPermitmaclistNum'
_e='qtechDot11WIDSRogueInfoTYPE'
_d='qtechDot11WIDSRogueInfoNUM'
_c='qtechDot11StaticblacklistNum'
_b='qtechDot11WhitelistNum'
_a='qtechDot11WIDSAPID'
_Z='qtechDot11PermitMACNum'
_Y='qtechDot11AttackNum'
_X='qtechDot11PermitNum'
_W='qtechDot11VendorOUI'
_V='qtechDot11WIDSDeviceInfoString'
_U='qtechDot11WIDSDeviceInfoMAC'
_T='qtechDot11WIDSDeviceInfoOper'
_S='qtechDot11WIDSDeviceInfoTYPE'
_R='qtechDot11WIDSDeviceInfoNUM'
_Q='qtechDot11WIDSAttackExtensionInfo'
_P='qtechDot11WIDSAttackType'
_O='qtechDot11WIDSAttackingDeviceMac'
_N='qtechDot11WIDSSUnauthorizedSSIDExtensionInfo'
_M='qtechDot11WIDSUnauthorizedSSID'
_L='qtechDot11WIDSSuspiciousDeviceExtensionInfo'
_K='qtechDot11WIDSSuspiciousDeviceMac'
_J='qtechDot11WIDSextinfo'
_I='qtechDot11WIDSInformation'
_H='qtechDot11WIDSAPBSSID'
_G='qtechDot11WIDSSTAMAC'
_F='DisplayString'
_E='not-accessible'
_D='read-only'
_C='read-write'
_B='QTECH-DOT11-WIDS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_F,'MacAddress','PhysAddress','TextualConvention','TruthValue')
qtechDot11WIDSMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,62))
if mibBuilder.loadTexts:qtechDot11WIDSMIB.setRevisions(('2009-04-15 09:00',))
_QtechDot11WIDSTraps_ObjectIdentity=ObjectIdentity
qtechDot11WIDSTraps=_QtechDot11WIDSTraps_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,62,0))
_QtechDot11WIDSConfigObjects_ObjectIdentity=ObjectIdentity
qtechDot11WIDSConfigObjects=_QtechDot11WIDSConfigObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,62,1))
_QtechDot11WIDSPermitVendorTable_Object=MibTable
qtechDot11WIDSPermitVendorTable=_QtechDot11WIDSPermitVendorTable_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,1))
if mibBuilder.loadTexts:qtechDot11WIDSPermitVendorTable.setStatus(_A)
_QtechDot11WIDSPermitVendorEntry_Object=MibTableRow
qtechDot11WIDSPermitVendorEntry=_QtechDot11WIDSPermitVendorEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,1,1))
qtechDot11WIDSPermitVendorEntry.setIndexNames((0,_B,_W))
if mibBuilder.loadTexts:qtechDot11WIDSPermitVendorEntry.setStatus(_A)
_QtechDot11VendorOUI_Type=Integer32
_QtechDot11VendorOUI_Object=MibTableColumn
qtechDot11VendorOUI=_QtechDot11VendorOUI_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,1,1,1),_QtechDot11VendorOUI_Type())
qtechDot11VendorOUI.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechDot11VendorOUI.setStatus(_A)
_QtechDot11VendorOper_Type=Integer32
_QtechDot11VendorOper_Object=MibTableColumn
qtechDot11VendorOper=_QtechDot11VendorOper_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,1,1,2),_QtechDot11VendorOper_Type())
qtechDot11VendorOper.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDot11VendorOper.setStatus(_A)
_QtechDot11VendorName_Type=MacAddress
_QtechDot11VendorName_Object=MibTableColumn
qtechDot11VendorName=_QtechDot11VendorName_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,1,1,3),_QtechDot11VendorName_Type())
qtechDot11VendorName.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDot11VendorName.setStatus(_A)
_QtechDot11WIDSPermitSSIDTable_Object=MibTable
qtechDot11WIDSPermitSSIDTable=_QtechDot11WIDSPermitSSIDTable_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,2))
if mibBuilder.loadTexts:qtechDot11WIDSPermitSSIDTable.setStatus(_A)
_QtechDot11WIDSPermitSSIDEntry_Object=MibTableRow
qtechDot11WIDSPermitSSIDEntry=_QtechDot11WIDSPermitSSIDEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,2,1))
qtechDot11WIDSPermitSSIDEntry.setIndexNames((0,_B,_X))
if mibBuilder.loadTexts:qtechDot11WIDSPermitSSIDEntry.setStatus(_A)
_QtechDot11PermitNum_Type=Integer32
_QtechDot11PermitNum_Object=MibTableColumn
qtechDot11PermitNum=_QtechDot11PermitNum_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,2,1,1),_QtechDot11PermitNum_Type())
qtechDot11PermitNum.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechDot11PermitNum.setStatus(_A)
_QtechDot11PermitOper_Type=Integer32
_QtechDot11PermitOper_Object=MibTableColumn
qtechDot11PermitOper=_QtechDot11PermitOper_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,2,1,2),_QtechDot11PermitOper_Type())
qtechDot11PermitOper.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDot11PermitOper.setStatus(_A)
class _QtechDot11PermitSSID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_QtechDot11PermitSSID_Type.__name__=_F
_QtechDot11PermitSSID_Object=MibTableColumn
qtechDot11PermitSSID=_QtechDot11PermitSSID_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,2,1,3),_QtechDot11PermitSSID_Type())
qtechDot11PermitSSID.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDot11PermitSSID.setStatus(_A)
_QtechDot11WIDSDeviceAttackMacaddressListTable_Object=MibTable
qtechDot11WIDSDeviceAttackMacaddressListTable=_QtechDot11WIDSDeviceAttackMacaddressListTable_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,3))
if mibBuilder.loadTexts:qtechDot11WIDSDeviceAttackMacaddressListTable.setStatus(_A)
_QtechDot11WIDSDeviceAttackMacaddressListEntry_Object=MibTableRow
qtechDot11WIDSDeviceAttackMacaddressListEntry=_QtechDot11WIDSDeviceAttackMacaddressListEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,3,1))
qtechDot11WIDSDeviceAttackMacaddressListEntry.setIndexNames((0,_B,_Y))
if mibBuilder.loadTexts:qtechDot11WIDSDeviceAttackMacaddressListEntry.setStatus(_A)
_QtechDot11AttackNum_Type=Integer32
_QtechDot11AttackNum_Object=MibTableColumn
qtechDot11AttackNum=_QtechDot11AttackNum_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,3,1,1),_QtechDot11AttackNum_Type())
qtechDot11AttackNum.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechDot11AttackNum.setStatus(_A)
_QtechDot11AttackOper_Type=Integer32
_QtechDot11AttackOper_Object=MibTableColumn
qtechDot11AttackOper=_QtechDot11AttackOper_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,3,1,2),_QtechDot11AttackOper_Type())
qtechDot11AttackOper.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDot11AttackOper.setStatus(_A)
_QtechDot11AttackMAC_Type=MacAddress
_QtechDot11AttackMAC_Object=MibTableColumn
qtechDot11AttackMAC=_QtechDot11AttackMAC_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,3,1,3),_QtechDot11AttackMAC_Type())
qtechDot11AttackMAC.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDot11AttackMAC.setStatus(_A)
class _QtechDot11AttackInfo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_QtechDot11AttackInfo_Type.__name__=_F
_QtechDot11AttackInfo_Object=MibTableColumn
qtechDot11AttackInfo=_QtechDot11AttackInfo_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,3,1,4),_QtechDot11AttackInfo_Type())
qtechDot11AttackInfo.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechDot11AttackInfo.setStatus(_A)
_QtechDot11WIDSDevicePermitMacaddressListTable_Object=MibTable
qtechDot11WIDSDevicePermitMacaddressListTable=_QtechDot11WIDSDevicePermitMacaddressListTable_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,4))
if mibBuilder.loadTexts:qtechDot11WIDSDevicePermitMacaddressListTable.setStatus(_A)
_QtechDot11WIDSDevicePermitMacaddressListEntry_Object=MibTableRow
qtechDot11WIDSDevicePermitMacaddressListEntry=_QtechDot11WIDSDevicePermitMacaddressListEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,4,1))
qtechDot11WIDSDevicePermitMacaddressListEntry.setIndexNames((0,_B,_Z))
if mibBuilder.loadTexts:qtechDot11WIDSDevicePermitMacaddressListEntry.setStatus(_A)
_QtechDot11PermitMACNum_Type=Integer32
_QtechDot11PermitMACNum_Object=MibTableColumn
qtechDot11PermitMACNum=_QtechDot11PermitMACNum_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,4,1,1),_QtechDot11PermitMACNum_Type())
qtechDot11PermitMACNum.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechDot11PermitMACNum.setStatus(_A)
_QtechDot11PermitMACOper_Type=Integer32
_QtechDot11PermitMACOper_Object=MibTableColumn
qtechDot11PermitMACOper=_QtechDot11PermitMACOper_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,4,1,2),_QtechDot11PermitMACOper_Type())
qtechDot11PermitMACOper.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDot11PermitMACOper.setStatus(_A)
_QtechDot11PermitMACAddr_Type=MacAddress
_QtechDot11PermitMACAddr_Object=MibTableColumn
qtechDot11PermitMACAddr=_QtechDot11PermitMACAddr_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,4,1,3),_QtechDot11PermitMACAddr_Type())
qtechDot11PermitMACAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDot11PermitMACAddr.setStatus(_A)
_QtechDot11WIDSDeviceagingDuration_Type=Integer32
_QtechDot11WIDSDeviceagingDuration_Object=MibScalar
qtechDot11WIDSDeviceagingDuration=_QtechDot11WIDSDeviceagingDuration_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,5),_QtechDot11WIDSDeviceagingDuration_Type())
qtechDot11WIDSDeviceagingDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDot11WIDSDeviceagingDuration.setStatus(_A)
_QtechDot11WIDSCountermeasuresMode_Type=Integer32
_QtechDot11WIDSCountermeasuresMode_Object=MibScalar
qtechDot11WIDSCountermeasuresMode=_QtechDot11WIDSCountermeasuresMode_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,6),_QtechDot11WIDSCountermeasuresMode_Type())
qtechDot11WIDSCountermeasuresMode.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDot11WIDSCountermeasuresMode.setStatus(_A)
_QtechDot11WIDSCountermeasureSet_Type=Integer32
_QtechDot11WIDSCountermeasureSet_Object=MibScalar
qtechDot11WIDSCountermeasureSet=_QtechDot11WIDSCountermeasureSet_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,7),_QtechDot11WIDSCountermeasureSet_Type())
qtechDot11WIDSCountermeasureSet.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDot11WIDSCountermeasureSet.setStatus(_A)
_QtechDot11WIDSModeTable_Object=MibTable
qtechDot11WIDSModeTable=_QtechDot11WIDSModeTable_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,8))
if mibBuilder.loadTexts:qtechDot11WIDSModeTable.setStatus(_A)
_QtechDot11WIDSModeEntry_Object=MibTableRow
qtechDot11WIDSModeEntry=_QtechDot11WIDSModeEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,8,1))
qtechDot11WIDSModeEntry.setIndexNames((0,_B,_a))
if mibBuilder.loadTexts:qtechDot11WIDSModeEntry.setStatus(_A)
_QtechDot11WIDSAPID_Type=Integer32
_QtechDot11WIDSAPID_Object=MibTableColumn
qtechDot11WIDSAPID=_QtechDot11WIDSAPID_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,8,1,1),_QtechDot11WIDSAPID_Type())
qtechDot11WIDSAPID.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechDot11WIDSAPID.setStatus(_A)
_QtechDot11WIDSDeviceMode_Type=Integer32
_QtechDot11WIDSDeviceMode_Object=MibTableColumn
qtechDot11WIDSDeviceMode=_QtechDot11WIDSDeviceMode_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,8,1,2),_QtechDot11WIDSDeviceMode_Type())
qtechDot11WIDSDeviceMode.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDot11WIDSDeviceMode.setStatus(_A)
_QtechDot11WIDSWhitelistMacaddressListTable_Object=MibTable
qtechDot11WIDSWhitelistMacaddressListTable=_QtechDot11WIDSWhitelistMacaddressListTable_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,9))
if mibBuilder.loadTexts:qtechDot11WIDSWhitelistMacaddressListTable.setStatus(_A)
_QtechDot11WIDSWhitelistMacaddressListEntry_Object=MibTableRow
qtechDot11WIDSWhitelistMacaddressListEntry=_QtechDot11WIDSWhitelistMacaddressListEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,9,1))
qtechDot11WIDSWhitelistMacaddressListEntry.setIndexNames((0,_B,_b))
if mibBuilder.loadTexts:qtechDot11WIDSWhitelistMacaddressListEntry.setStatus(_A)
_QtechDot11WhitelistNum_Type=Integer32
_QtechDot11WhitelistNum_Object=MibTableColumn
qtechDot11WhitelistNum=_QtechDot11WhitelistNum_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,9,1,1),_QtechDot11WhitelistNum_Type())
qtechDot11WhitelistNum.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechDot11WhitelistNum.setStatus(_A)
_QtechDot11WhitelistOper_Type=Integer32
_QtechDot11WhitelistOper_Object=MibTableColumn
qtechDot11WhitelistOper=_QtechDot11WhitelistOper_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,9,1,2),_QtechDot11WhitelistOper_Type())
qtechDot11WhitelistOper.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDot11WhitelistOper.setStatus(_A)
_QtechDot11WhitelistMAC_Type=MacAddress
_QtechDot11WhitelistMAC_Object=MibTableColumn
qtechDot11WhitelistMAC=_QtechDot11WhitelistMAC_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,9,1,3),_QtechDot11WhitelistMAC_Type())
qtechDot11WhitelistMAC.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDot11WhitelistMAC.setStatus(_A)
_QtechDot11WIDSStaticblackListTable_Object=MibTable
qtechDot11WIDSStaticblackListTable=_QtechDot11WIDSStaticblackListTable_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,10))
if mibBuilder.loadTexts:qtechDot11WIDSStaticblackListTable.setStatus(_A)
_QtechDot11WIDSStaticblackListEntry_Object=MibTableRow
qtechDot11WIDSStaticblackListEntry=_QtechDot11WIDSStaticblackListEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,10,1))
qtechDot11WIDSStaticblackListEntry.setIndexNames((0,_B,_c))
if mibBuilder.loadTexts:qtechDot11WIDSStaticblackListEntry.setStatus(_A)
_QtechDot11StaticblacklistNum_Type=Integer32
_QtechDot11StaticblacklistNum_Object=MibTableColumn
qtechDot11StaticblacklistNum=_QtechDot11StaticblacklistNum_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,10,1,1),_QtechDot11StaticblacklistNum_Type())
qtechDot11StaticblacklistNum.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechDot11StaticblacklistNum.setStatus(_A)
_QtechDot11StaticblacklistOper_Type=Integer32
_QtechDot11StaticblacklistOper_Object=MibTableColumn
qtechDot11StaticblacklistOper=_QtechDot11StaticblacklistOper_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,10,1,2),_QtechDot11StaticblacklistOper_Type())
qtechDot11StaticblacklistOper.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDot11StaticblacklistOper.setStatus(_A)
_QtechDot11StaticblacklistMAC_Type=MacAddress
_QtechDot11StaticblacklistMAC_Object=MibTableColumn
qtechDot11StaticblacklistMAC=_QtechDot11StaticblacklistMAC_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,10,1,3),_QtechDot11StaticblacklistMAC_Type())
qtechDot11StaticblacklistMAC.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDot11StaticblacklistMAC.setStatus(_A)
_QtechDot11WIDSDynamicblacklistEnable_Type=TruthValue
_QtechDot11WIDSDynamicblacklistEnable_Object=MibScalar
qtechDot11WIDSDynamicblacklistEnable=_QtechDot11WIDSDynamicblacklistEnable_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,11),_QtechDot11WIDSDynamicblacklistEnable_Type())
qtechDot11WIDSDynamicblacklistEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDot11WIDSDynamicblacklistEnable.setStatus(_A)
_QtechDot11WIDSDynamicblacklistLifetime_Type=Integer32
_QtechDot11WIDSDynamicblacklistLifetime_Object=MibScalar
qtechDot11WIDSDynamicblacklistLifetime=_QtechDot11WIDSDynamicblacklistLifetime_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,12),_QtechDot11WIDSDynamicblacklistLifetime_Type())
qtechDot11WIDSDynamicblacklistLifetime.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDot11WIDSDynamicblacklistLifetime.setStatus(_A)
_QtechDot11WIDSAttackDetectionMode_Type=Integer32
_QtechDot11WIDSAttackDetectionMode_Object=MibScalar
qtechDot11WIDSAttackDetectionMode=_QtechDot11WIDSAttackDetectionMode_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,13),_QtechDot11WIDSAttackDetectionMode_Type())
qtechDot11WIDSAttackDetectionMode.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDot11WIDSAttackDetectionMode.setStatus(_A)
_QtechDot11WIDSRogueInfoTable_Object=MibTable
qtechDot11WIDSRogueInfoTable=_QtechDot11WIDSRogueInfoTable_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,14))
if mibBuilder.loadTexts:qtechDot11WIDSRogueInfoTable.setStatus(_A)
_QtechDot11WIDSRogueInfoEntry_Object=MibTableRow
qtechDot11WIDSRogueInfoEntry=_QtechDot11WIDSRogueInfoEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,14,1))
qtechDot11WIDSRogueInfoEntry.setIndexNames((0,_B,_d),(0,_B,_e))
if mibBuilder.loadTexts:qtechDot11WIDSRogueInfoEntry.setStatus(_A)
_QtechDot11WIDSRogueInfoNUM_Type=Integer32
_QtechDot11WIDSRogueInfoNUM_Object=MibTableColumn
qtechDot11WIDSRogueInfoNUM=_QtechDot11WIDSRogueInfoNUM_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,14,1,1),_QtechDot11WIDSRogueInfoNUM_Type())
qtechDot11WIDSRogueInfoNUM.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechDot11WIDSRogueInfoNUM.setStatus(_A)
_QtechDot11WIDSRogueInfoTYPE_Type=Integer32
_QtechDot11WIDSRogueInfoTYPE_Object=MibTableColumn
qtechDot11WIDSRogueInfoTYPE=_QtechDot11WIDSRogueInfoTYPE_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,14,1,2),_QtechDot11WIDSRogueInfoTYPE_Type())
qtechDot11WIDSRogueInfoTYPE.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechDot11WIDSRogueInfoTYPE.setStatus(_A)
_QtechDot11WIDSRogueInfoOper_Type=Integer32
_QtechDot11WIDSRogueInfoOper_Object=MibTableColumn
qtechDot11WIDSRogueInfoOper=_QtechDot11WIDSRogueInfoOper_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,14,1,3),_QtechDot11WIDSRogueInfoOper_Type())
qtechDot11WIDSRogueInfoOper.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDot11WIDSRogueInfoOper.setStatus(_A)
_QtechDot11WIDSRogueInfoMAC_Type=MacAddress
_QtechDot11WIDSRogueInfoMAC_Object=MibTableColumn
qtechDot11WIDSRogueInfoMAC=_QtechDot11WIDSRogueInfoMAC_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,14,1,4),_QtechDot11WIDSRogueInfoMAC_Type())
qtechDot11WIDSRogueInfoMAC.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDot11WIDSRogueInfoMAC.setStatus(_A)
_QtechDot11WIDSRogueInfoString_Type=DisplayString
_QtechDot11WIDSRogueInfoString_Object=MibTableColumn
qtechDot11WIDSRogueInfoString=_QtechDot11WIDSRogueInfoString_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,14,1,5),_QtechDot11WIDSRogueInfoString_Type())
qtechDot11WIDSRogueInfoString.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDot11WIDSRogueInfoString.setStatus(_A)
_QtechDot11WIDSPermitmaclistEnableTable_Object=MibTable
qtechDot11WIDSPermitmaclistEnableTable=_QtechDot11WIDSPermitmaclistEnableTable_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,15))
if mibBuilder.loadTexts:qtechDot11WIDSPermitmaclistEnableTable.setStatus(_A)
_QtechDot11WIDSPermitmaclistEnableEntry_Object=MibTableRow
qtechDot11WIDSPermitmaclistEnableEntry=_QtechDot11WIDSPermitmaclistEnableEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,15,1))
qtechDot11WIDSPermitmaclistEnableEntry.setIndexNames((0,_B,_f))
if mibBuilder.loadTexts:qtechDot11WIDSPermitmaclistEnableEntry.setStatus(_A)
_QtechDot11WIDSEnableVlanPermitmaclistNum_Type=Integer32
_QtechDot11WIDSEnableVlanPermitmaclistNum_Object=MibTableColumn
qtechDot11WIDSEnableVlanPermitmaclistNum=_QtechDot11WIDSEnableVlanPermitmaclistNum_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,15,1,1),_QtechDot11WIDSEnableVlanPermitmaclistNum_Type())
qtechDot11WIDSEnableVlanPermitmaclistNum.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechDot11WIDSEnableVlanPermitmaclistNum.setStatus(_A)
_QtechDot11WIDSEnableVlanPermitmaclistOper_Type=Integer32
_QtechDot11WIDSEnableVlanPermitmaclistOper_Object=MibTableColumn
qtechDot11WIDSEnableVlanPermitmaclistOper=_QtechDot11WIDSEnableVlanPermitmaclistOper_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,15,1,2),_QtechDot11WIDSEnableVlanPermitmaclistOper_Type())
qtechDot11WIDSEnableVlanPermitmaclistOper.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDot11WIDSEnableVlanPermitmaclistOper.setStatus(_A)
_QtechDot11WIDSEnableVlanPermitmaclist_Type=MacAddress
_QtechDot11WIDSEnableVlanPermitmaclist_Object=MibTableColumn
qtechDot11WIDSEnableVlanPermitmaclist=_QtechDot11WIDSEnableVlanPermitmaclist_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,15,1,3),_QtechDot11WIDSEnableVlanPermitmaclist_Type())
qtechDot11WIDSEnableVlanPermitmaclist.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDot11WIDSEnableVlanPermitmaclist.setStatus(_A)
_QtechDot11WIDSResetStatistics_Type=TruthValue
_QtechDot11WIDSResetStatistics_Object=MibScalar
qtechDot11WIDSResetStatistics=_QtechDot11WIDSResetStatistics_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,18),_QtechDot11WIDSResetStatistics_Type())
qtechDot11WIDSResetStatistics.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDot11WIDSResetStatistics.setStatus(_A)
_QtechDot11WIDSResetRoguehistoryStatistics_Type=Integer32
_QtechDot11WIDSResetRoguehistoryStatistics_Object=MibScalar
qtechDot11WIDSResetRoguehistoryStatistics=_QtechDot11WIDSResetRoguehistoryStatistics_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,19),_QtechDot11WIDSResetRoguehistoryStatistics_Type())
qtechDot11WIDSResetRoguehistoryStatistics.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDot11WIDSResetRoguehistoryStatistics.setStatus(_A)
_QtechDot11WIDSResethistory_Type=Integer32
_QtechDot11WIDSResethistory_Object=MibScalar
qtechDot11WIDSResethistory=_QtechDot11WIDSResethistory_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,20),_QtechDot11WIDSResethistory_Type())
qtechDot11WIDSResethistory.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDot11WIDSResethistory.setStatus(_A)
_QtechDot11WIDSResetDynamicBlacklistTable_Object=MibTable
qtechDot11WIDSResetDynamicBlacklistTable=_QtechDot11WIDSResetDynamicBlacklistTable_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,21))
if mibBuilder.loadTexts:qtechDot11WIDSResetDynamicBlacklistTable.setStatus(_A)
_QtechDot11WIDSResetDynamicBlacklistEntry_Object=MibTableRow
qtechDot11WIDSResetDynamicBlacklistEntry=_QtechDot11WIDSResetDynamicBlacklistEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,21,1))
qtechDot11WIDSResetDynamicBlacklistEntry.setIndexNames((0,_B,_g))
if mibBuilder.loadTexts:qtechDot11WIDSResetDynamicBlacklistEntry.setStatus(_A)
_QtechDot11WIDSResetDynamicBlacklistMac_Type=MacAddress
_QtechDot11WIDSResetDynamicBlacklistMac_Object=MibTableColumn
qtechDot11WIDSResetDynamicBlacklistMac=_QtechDot11WIDSResetDynamicBlacklistMac_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,21,1,1),_QtechDot11WIDSResetDynamicBlacklistMac_Type())
qtechDot11WIDSResetDynamicBlacklistMac.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechDot11WIDSResetDynamicBlacklistMac.setStatus(_A)
_QtechDot11WIDSResetDynamicBlacklistType_Type=Integer32
_QtechDot11WIDSResetDynamicBlacklistType_Object=MibTableColumn
qtechDot11WIDSResetDynamicBlacklistType=_QtechDot11WIDSResetDynamicBlacklistType_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,21,1,2),_QtechDot11WIDSResetDynamicBlacklistType_Type())
qtechDot11WIDSResetDynamicBlacklistType.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDot11WIDSResetDynamicBlacklistType.setStatus(_A)
_QtechDot11WIDResetUserisolationStatistics_Type=Integer32
_QtechDot11WIDResetUserisolationStatistics_Object=MibScalar
qtechDot11WIDResetUserisolationStatistics=_QtechDot11WIDResetUserisolationStatistics_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,22),_QtechDot11WIDResetUserisolationStatistics_Type())
qtechDot11WIDResetUserisolationStatistics.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDot11WIDResetUserisolationStatistics.setStatus(_A)
_QtechDot11WIDUserisolationAC_Type=Integer32
_QtechDot11WIDUserisolationAC_Object=MibScalar
qtechDot11WIDUserisolationAC=_QtechDot11WIDUserisolationAC_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,23),_QtechDot11WIDUserisolationAC_Type())
qtechDot11WIDUserisolationAC.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDot11WIDUserisolationAC.setStatus(_A)
_QtechDot11WIDUserisolationAP_Type=Integer32
_QtechDot11WIDUserisolationAP_Object=MibScalar
qtechDot11WIDUserisolationAP=_QtechDot11WIDUserisolationAP_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,24),_QtechDot11WIDUserisolationAP_Type())
qtechDot11WIDUserisolationAP.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDot11WIDUserisolationAP.setStatus(_A)
_QtechDot11WIDSShowStaticsTable_Object=MibTable
qtechDot11WIDSShowStaticsTable=_QtechDot11WIDSShowStaticsTable_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,25))
if mibBuilder.loadTexts:qtechDot11WIDSShowStaticsTable.setStatus(_A)
_QtechDot11WIDSShowStaticsEntry_Object=MibTableRow
qtechDot11WIDSShowStaticsEntry=_QtechDot11WIDSShowStaticsEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,25,1))
qtechDot11WIDSShowStaticsEntry.setIndexNames((0,_B,_h))
if mibBuilder.loadTexts:qtechDot11WIDSShowStaticsEntry.setStatus(_A)
_QtechDot11WIDSShowStaticsNum_Type=Integer32
_QtechDot11WIDSShowStaticsNum_Object=MibTableColumn
qtechDot11WIDSShowStaticsNum=_QtechDot11WIDSShowStaticsNum_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,25,1,1),_QtechDot11WIDSShowStaticsNum_Type())
qtechDot11WIDSShowStaticsNum.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechDot11WIDSShowStaticsNum.setStatus(_A)
_QtechDot11WIDSShowStaticsOper_Type=Integer32
_QtechDot11WIDSShowStaticsOper_Object=MibTableColumn
qtechDot11WIDSShowStaticsOper=_QtechDot11WIDSShowStaticsOper_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,25,1,2),_QtechDot11WIDSShowStaticsOper_Type())
qtechDot11WIDSShowStaticsOper.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDot11WIDSShowStaticsOper.setStatus(_A)
_QtechDot11WIDSShowStaticsMac_Type=MacAddress
_QtechDot11WIDSShowStaticsMac_Object=MibTableColumn
qtechDot11WIDSShowStaticsMac=_QtechDot11WIDSShowStaticsMac_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,25,1,3),_QtechDot11WIDSShowStaticsMac_Type())
qtechDot11WIDSShowStaticsMac.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDot11WIDSShowStaticsMac.setStatus(_A)
class _QtechDot11WIDSShowStaticsInfo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_QtechDot11WIDSShowStaticsInfo_Type.__name__=_F
_QtechDot11WIDSShowStaticsInfo_Object=MibTableColumn
qtechDot11WIDSShowStaticsInfo=_QtechDot11WIDSShowStaticsInfo_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,25,1,4),_QtechDot11WIDSShowStaticsInfo_Type())
qtechDot11WIDSShowStaticsInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDot11WIDSShowStaticsInfo.setStatus(_A)
_QtechDot11WIDSAssociationFailureTotalTimes_Type=Integer32
_QtechDot11WIDSAssociationFailureTotalTimes_Object=MibScalar
qtechDot11WIDSAssociationFailureTotalTimes=_QtechDot11WIDSAssociationFailureTotalTimes_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,26),_QtechDot11WIDSAssociationFailureTotalTimes_Type())
qtechDot11WIDSAssociationFailureTotalTimes.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechDot11WIDSAssociationFailureTotalTimes.setStatus(_A)
_QtechDot11WIDSSuspiciousAPInfoTable_Object=MibTable
qtechDot11WIDSSuspiciousAPInfoTable=_QtechDot11WIDSSuspiciousAPInfoTable_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,27))
if mibBuilder.loadTexts:qtechDot11WIDSSuspiciousAPInfoTable.setStatus(_A)
_QtechDot11WIDSSuspiciousAPInfoEntry_Object=MibTableRow
qtechDot11WIDSSuspiciousAPInfoEntry=_QtechDot11WIDSSuspiciousAPInfoEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,27,1))
qtechDot11WIDSSuspiciousAPInfoEntry.setIndexNames((0,_B,_i))
if mibBuilder.loadTexts:qtechDot11WIDSSuspiciousAPInfoEntry.setStatus(_A)
_QtechDot11WIDSSuspiciousAPBSS_Type=MacAddress
_QtechDot11WIDSSuspiciousAPBSS_Object=MibTableColumn
qtechDot11WIDSSuspiciousAPBSS=_QtechDot11WIDSSuspiciousAPBSS_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,27,1,1),_QtechDot11WIDSSuspiciousAPBSS_Type())
qtechDot11WIDSSuspiciousAPBSS.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechDot11WIDSSuspiciousAPBSS.setStatus(_A)
_QtechDot11WIDSSuspiciousAPCount_Type=Integer32
_QtechDot11WIDSSuspiciousAPCount_Object=MibTableColumn
qtechDot11WIDSSuspiciousAPCount=_QtechDot11WIDSSuspiciousAPCount_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,27,1,2),_QtechDot11WIDSSuspiciousAPCount_Type())
qtechDot11WIDSSuspiciousAPCount.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechDot11WIDSSuspiciousAPCount.setStatus(_A)
_QtechDot11WIDSMomentFirstTimeDetectedSusAP_Type=TimeTicks
_QtechDot11WIDSMomentFirstTimeDetectedSusAP_Object=MibTableColumn
qtechDot11WIDSMomentFirstTimeDetectedSusAP=_QtechDot11WIDSMomentFirstTimeDetectedSusAP_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,27,1,3),_QtechDot11WIDSMomentFirstTimeDetectedSusAP_Type())
qtechDot11WIDSMomentFirstTimeDetectedSusAP.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechDot11WIDSMomentFirstTimeDetectedSusAP.setStatus(_A)
_QtechDot11WIDSMomentLastTimeDetectedSusAP_Type=TimeTicks
_QtechDot11WIDSMomentLastTimeDetectedSusAP_Object=MibTableColumn
qtechDot11WIDSMomentLastTimeDetectedSusAP=_QtechDot11WIDSMomentLastTimeDetectedSusAP_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,27,1,4),_QtechDot11WIDSMomentLastTimeDetectedSusAP_Type())
qtechDot11WIDSMomentLastTimeDetectedSusAP.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechDot11WIDSMomentLastTimeDetectedSusAP.setStatus(_A)
_QtechDot11WIDSSuspiciousAPSSID_Type=DisplayString
_QtechDot11WIDSSuspiciousAPSSID_Object=MibTableColumn
qtechDot11WIDSSuspiciousAPSSID=_QtechDot11WIDSSuspiciousAPSSID_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,27,1,5),_QtechDot11WIDSSuspiciousAPSSID_Type())
qtechDot11WIDSSuspiciousAPSSID.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechDot11WIDSSuspiciousAPSSID.setStatus(_A)
_QtechDot11WIDSSuspiciousAPMaxSignalStrength_Type=Integer32
_QtechDot11WIDSSuspiciousAPMaxSignalStrength_Object=MibTableColumn
qtechDot11WIDSSuspiciousAPMaxSignalStrength=_QtechDot11WIDSSuspiciousAPMaxSignalStrength_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,27,1,6),_QtechDot11WIDSSuspiciousAPMaxSignalStrength_Type())
qtechDot11WIDSSuspiciousAPMaxSignalStrength.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechDot11WIDSSuspiciousAPMaxSignalStrength.setStatus(_A)
_QtechDot11WIDSSuspiciousAPUsingChannel_Type=Integer32
_QtechDot11WIDSSuspiciousAPUsingChannel_Object=MibTableColumn
qtechDot11WIDSSuspiciousAPUsingChannel=_QtechDot11WIDSSuspiciousAPUsingChannel_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,27,1,7),_QtechDot11WIDSSuspiciousAPUsingChannel_Type())
qtechDot11WIDSSuspiciousAPUsingChannel.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechDot11WIDSSuspiciousAPUsingChannel.setStatus(_A)
_QtechDot11WIDSSuspiciousAPFrameEncrption_Type=Integer32
_QtechDot11WIDSSuspiciousAPFrameEncrption_Object=MibTableColumn
qtechDot11WIDSSuspiciousAPFrameEncrption=_QtechDot11WIDSSuspiciousAPFrameEncrption_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,27,1,8),_QtechDot11WIDSSuspiciousAPFrameEncrption_Type())
qtechDot11WIDSSuspiciousAPFrameEncrption.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechDot11WIDSSuspiciousAPFrameEncrption.setStatus(_A)
_QtechDot11WIDSSuspiciousAPNeedsDealingTag_Type=TruthValue
_QtechDot11WIDSSuspiciousAPNeedsDealingTag_Object=MibTableColumn
qtechDot11WIDSSuspiciousAPNeedsDealingTag=_QtechDot11WIDSSuspiciousAPNeedsDealingTag_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,27,1,9),_QtechDot11WIDSSuspiciousAPNeedsDealingTag_Type())
qtechDot11WIDSSuspiciousAPNeedsDealingTag.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechDot11WIDSSuspiciousAPNeedsDealingTag.setStatus(_A)
_QtechDot11WIDSSuspiciousAPIgnoredTag_Type=TruthValue
_QtechDot11WIDSSuspiciousAPIgnoredTag_Object=MibTableColumn
qtechDot11WIDSSuspiciousAPIgnoredTag=_QtechDot11WIDSSuspiciousAPIgnoredTag_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,27,1,10),_QtechDot11WIDSSuspiciousAPIgnoredTag_Type())
qtechDot11WIDSSuspiciousAPIgnoredTag.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechDot11WIDSSuspiciousAPIgnoredTag.setStatus(_A)
_QtechDot11WIDSSuspiciousSTAInfoTable_Object=MibTable
qtechDot11WIDSSuspiciousSTAInfoTable=_QtechDot11WIDSSuspiciousSTAInfoTable_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,28))
if mibBuilder.loadTexts:qtechDot11WIDSSuspiciousSTAInfoTable.setStatus(_A)
_QtechDot11WIDSSuspiciousSTAInfoEntry_Object=MibTableRow
qtechDot11WIDSSuspiciousSTAInfoEntry=_QtechDot11WIDSSuspiciousSTAInfoEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,28,1))
qtechDot11WIDSSuspiciousSTAInfoEntry.setIndexNames((0,_B,_j))
if mibBuilder.loadTexts:qtechDot11WIDSSuspiciousSTAInfoEntry.setStatus(_A)
_QtechDot11WIDSSuspiciousSTAMAC_Type=MacAddress
_QtechDot11WIDSSuspiciousSTAMAC_Object=MibTableColumn
qtechDot11WIDSSuspiciousSTAMAC=_QtechDot11WIDSSuspiciousSTAMAC_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,28,1,1),_QtechDot11WIDSSuspiciousSTAMAC_Type())
qtechDot11WIDSSuspiciousSTAMAC.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechDot11WIDSSuspiciousSTAMAC.setStatus(_A)
_QtechDot11WIDSAPCountDetectingSuspiciousSTA_Type=Integer32
_QtechDot11WIDSAPCountDetectingSuspiciousSTA_Object=MibTableColumn
qtechDot11WIDSAPCountDetectingSuspiciousSTA=_QtechDot11WIDSAPCountDetectingSuspiciousSTA_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,28,1,2),_QtechDot11WIDSAPCountDetectingSuspiciousSTA_Type())
qtechDot11WIDSAPCountDetectingSuspiciousSTA.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechDot11WIDSAPCountDetectingSuspiciousSTA.setStatus(_A)
_QtechDot11WIDSMomentFirstTimeDetectedSusSTA_Type=TimeTicks
_QtechDot11WIDSMomentFirstTimeDetectedSusSTA_Object=MibTableColumn
qtechDot11WIDSMomentFirstTimeDetectedSusSTA=_QtechDot11WIDSMomentFirstTimeDetectedSusSTA_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,28,1,3),_QtechDot11WIDSMomentFirstTimeDetectedSusSTA_Type())
qtechDot11WIDSMomentFirstTimeDetectedSusSTA.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechDot11WIDSMomentFirstTimeDetectedSusSTA.setStatus(_A)
_QtechDot11WIDSMomentLastTimeDetectedSusSTA_Type=TimeTicks
_QtechDot11WIDSMomentLastTimeDetectedSusSTA_Object=MibTableColumn
qtechDot11WIDSMomentLastTimeDetectedSusSTA=_QtechDot11WIDSMomentLastTimeDetectedSusSTA_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,28,1,4),_QtechDot11WIDSMomentLastTimeDetectedSusSTA_Type())
qtechDot11WIDSMomentLastTimeDetectedSusSTA.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechDot11WIDSMomentLastTimeDetectedSusSTA.setStatus(_A)
_QtechDot11WIDSBSSIDSuspiciousSTAAccessing_Type=MacAddress
_QtechDot11WIDSBSSIDSuspiciousSTAAccessing_Object=MibTableColumn
qtechDot11WIDSBSSIDSuspiciousSTAAccessing=_QtechDot11WIDSBSSIDSuspiciousSTAAccessing_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,28,1,5),_QtechDot11WIDSBSSIDSuspiciousSTAAccessing_Type())
qtechDot11WIDSBSSIDSuspiciousSTAAccessing.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechDot11WIDSBSSIDSuspiciousSTAAccessing.setStatus(_A)
_QtechDot11WIDSSuspiciousSTAMaxSignalStrength_Type=Integer32
_QtechDot11WIDSSuspiciousSTAMaxSignalStrength_Object=MibTableColumn
qtechDot11WIDSSuspiciousSTAMaxSignalStrength=_QtechDot11WIDSSuspiciousSTAMaxSignalStrength_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,28,1,6),_QtechDot11WIDSSuspiciousSTAMaxSignalStrength_Type())
qtechDot11WIDSSuspiciousSTAMaxSignalStrength.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechDot11WIDSSuspiciousSTAMaxSignalStrength.setStatus(_A)
_QtechDot11WIDSSuspiciousSTAUsingChannel_Type=Integer32
_QtechDot11WIDSSuspiciousSTAUsingChannel_Object=MibTableColumn
qtechDot11WIDSSuspiciousSTAUsingChannel=_QtechDot11WIDSSuspiciousSTAUsingChannel_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,28,1,7),_QtechDot11WIDSSuspiciousSTAUsingChannel_Type())
qtechDot11WIDSSuspiciousSTAUsingChannel.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechDot11WIDSSuspiciousSTAUsingChannel.setStatus(_A)
_QtechDot11WIDSSuspiciousSTAWorksInAdhocMode_Type=TruthValue
_QtechDot11WIDSSuspiciousSTAWorksInAdhocMode_Object=MibTableColumn
qtechDot11WIDSSuspiciousSTAWorksInAdhocMode=_QtechDot11WIDSSuspiciousSTAWorksInAdhocMode_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,28,1,8),_QtechDot11WIDSSuspiciousSTAWorksInAdhocMode_Type())
qtechDot11WIDSSuspiciousSTAWorksInAdhocMode.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechDot11WIDSSuspiciousSTAWorksInAdhocMode.setStatus(_A)
_QtechDot11WIDSSuspiciousSTANeedsDealingTag_Type=TruthValue
_QtechDot11WIDSSuspiciousSTANeedsDealingTag_Object=MibTableColumn
qtechDot11WIDSSuspiciousSTANeedsDealingTag=_QtechDot11WIDSSuspiciousSTANeedsDealingTag_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,28,1,9),_QtechDot11WIDSSuspiciousSTANeedsDealingTag_Type())
qtechDot11WIDSSuspiciousSTANeedsDealingTag.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechDot11WIDSSuspiciousSTANeedsDealingTag.setStatus(_A)
_QtechDot11WIDSSuspiciousSTAIgnoredTag_Type=TruthValue
_QtechDot11WIDSSuspiciousSTAIgnoredTag_Object=MibTableColumn
qtechDot11WIDSSuspiciousSTAIgnoredTag=_QtechDot11WIDSSuspiciousSTAIgnoredTag_Object((1,3,6,1,4,1,27514,1,1,10,2,62,1,28,1,10),_QtechDot11WIDSSuspiciousSTAIgnoredTag_Type())
qtechDot11WIDSSuspiciousSTAIgnoredTag.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDot11WIDSSuspiciousSTAIgnoredTag.setStatus(_A)
_QtechDot11WIDSDetectObjects_ObjectIdentity=ObjectIdentity
qtechDot11WIDSDetectObjects=_QtechDot11WIDSDetectObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,62,2))
_QtechDot11WIDSShowDot11IdsAttacklistTable_Object=MibTable
qtechDot11WIDSShowDot11IdsAttacklistTable=_QtechDot11WIDSShowDot11IdsAttacklistTable_Object((1,3,6,1,4,1,27514,1,1,10,2,62,2,1))
if mibBuilder.loadTexts:qtechDot11WIDSShowDot11IdsAttacklistTable.setStatus(_A)
_QtechDot11WIDSShowDot11IdsAttacklistEntry_Object=MibTableRow
qtechDot11WIDSShowDot11IdsAttacklistEntry=_QtechDot11WIDSShowDot11IdsAttacklistEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,62,2,1,1))
qtechDot11WIDSShowDot11IdsAttacklistEntry.setIndexNames((0,_B,_k))
if mibBuilder.loadTexts:qtechDot11WIDSShowDot11IdsAttacklistEntry.setStatus(_A)
_QtechDot11WIDSShowDot11IdsAttacklistNum_Type=Integer32
_QtechDot11WIDSShowDot11IdsAttacklistNum_Object=MibTableColumn
qtechDot11WIDSShowDot11IdsAttacklistNum=_QtechDot11WIDSShowDot11IdsAttacklistNum_Object((1,3,6,1,4,1,27514,1,1,10,2,62,2,1,1,1),_QtechDot11WIDSShowDot11IdsAttacklistNum_Type())
qtechDot11WIDSShowDot11IdsAttacklistNum.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechDot11WIDSShowDot11IdsAttacklistNum.setStatus(_A)
_QtechDot11WIDSShowDot11IdsAttacklistOper_Type=Integer32
_QtechDot11WIDSShowDot11IdsAttacklistOper_Object=MibTableColumn
qtechDot11WIDSShowDot11IdsAttacklistOper=_QtechDot11WIDSShowDot11IdsAttacklistOper_Object((1,3,6,1,4,1,27514,1,1,10,2,62,2,1,1,2),_QtechDot11WIDSShowDot11IdsAttacklistOper_Type())
qtechDot11WIDSShowDot11IdsAttacklistOper.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDot11WIDSShowDot11IdsAttacklistOper.setStatus(_A)
_QtechDot11WIDSShowDot11IdsAttacklistMac_Type=MacAddress
_QtechDot11WIDSShowDot11IdsAttacklistMac_Object=MibTableColumn
qtechDot11WIDSShowDot11IdsAttacklistMac=_QtechDot11WIDSShowDot11IdsAttacklistMac_Object((1,3,6,1,4,1,27514,1,1,10,2,62,2,1,1,3),_QtechDot11WIDSShowDot11IdsAttacklistMac_Type())
qtechDot11WIDSShowDot11IdsAttacklistMac.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDot11WIDSShowDot11IdsAttacklistMac.setStatus(_A)
class _QtechDot11WIDSShowDot11IdsAttacklistInfo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_QtechDot11WIDSShowDot11IdsAttacklistInfo_Type.__name__=_F
_QtechDot11WIDSShowDot11IdsAttacklistInfo_Object=MibTableColumn
qtechDot11WIDSShowDot11IdsAttacklistInfo=_QtechDot11WIDSShowDot11IdsAttacklistInfo_Object((1,3,6,1,4,1,27514,1,1,10,2,62,2,1,1,4),_QtechDot11WIDSShowDot11IdsAttacklistInfo_Type())
qtechDot11WIDSShowDot11IdsAttacklistInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDot11WIDSShowDot11IdsAttacklistInfo.setStatus(_A)
_QtechDot11WIDSTrapsObjects_ObjectIdentity=ObjectIdentity
qtechDot11WIDSTrapsObjects=_QtechDot11WIDSTrapsObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,62,3))
_QtechDot11WIDSSTAMAC_Type=MacAddress
_QtechDot11WIDSSTAMAC_Object=MibScalar
qtechDot11WIDSSTAMAC=_QtechDot11WIDSSTAMAC_Object((1,3,6,1,4,1,27514,1,1,10,2,62,3,1),_QtechDot11WIDSSTAMAC_Type())
qtechDot11WIDSSTAMAC.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDot11WIDSSTAMAC.setStatus(_A)
class _QtechDot11WIDSAPBSSID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_QtechDot11WIDSAPBSSID_Type.__name__=_F
_QtechDot11WIDSAPBSSID_Object=MibScalar
qtechDot11WIDSAPBSSID=_QtechDot11WIDSAPBSSID_Object((1,3,6,1,4,1,27514,1,1,10,2,62,3,2),_QtechDot11WIDSAPBSSID_Type())
qtechDot11WIDSAPBSSID.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDot11WIDSAPBSSID.setStatus(_A)
class _QtechDot11WIDSInformation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_QtechDot11WIDSInformation_Type.__name__=_F
_QtechDot11WIDSInformation_Object=MibScalar
qtechDot11WIDSInformation=_QtechDot11WIDSInformation_Object((1,3,6,1,4,1,27514,1,1,10,2,62,3,3),_QtechDot11WIDSInformation_Type())
qtechDot11WIDSInformation.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDot11WIDSInformation.setStatus(_A)
class _QtechDot11WIDSextinfo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_QtechDot11WIDSextinfo_Type.__name__=_F
_QtechDot11WIDSextinfo_Object=MibScalar
qtechDot11WIDSextinfo=_QtechDot11WIDSextinfo_Object((1,3,6,1,4,1,27514,1,1,10,2,62,3,4),_QtechDot11WIDSextinfo_Type())
qtechDot11WIDSextinfo.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDot11WIDSextinfo.setStatus(_A)
_QtechDot11WIDSDeviceInfoNUM_Type=Integer32
_QtechDot11WIDSDeviceInfoNUM_Object=MibScalar
qtechDot11WIDSDeviceInfoNUM=_QtechDot11WIDSDeviceInfoNUM_Object((1,3,6,1,4,1,27514,1,1,10,2,62,3,5),_QtechDot11WIDSDeviceInfoNUM_Type())
qtechDot11WIDSDeviceInfoNUM.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDot11WIDSDeviceInfoNUM.setStatus(_A)
_QtechDot11WIDSDeviceInfoTYPE_Type=Integer32
_QtechDot11WIDSDeviceInfoTYPE_Object=MibScalar
qtechDot11WIDSDeviceInfoTYPE=_QtechDot11WIDSDeviceInfoTYPE_Object((1,3,6,1,4,1,27514,1,1,10,2,62,3,6),_QtechDot11WIDSDeviceInfoTYPE_Type())
qtechDot11WIDSDeviceInfoTYPE.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDot11WIDSDeviceInfoTYPE.setStatus(_A)
_QtechDot11WIDSDeviceInfoOper_Type=Integer32
_QtechDot11WIDSDeviceInfoOper_Object=MibScalar
qtechDot11WIDSDeviceInfoOper=_QtechDot11WIDSDeviceInfoOper_Object((1,3,6,1,4,1,27514,1,1,10,2,62,3,7),_QtechDot11WIDSDeviceInfoOper_Type())
qtechDot11WIDSDeviceInfoOper.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDot11WIDSDeviceInfoOper.setStatus(_A)
_QtechDot11WIDSDeviceInfoMAC_Type=MacAddress
_QtechDot11WIDSDeviceInfoMAC_Object=MibScalar
qtechDot11WIDSDeviceInfoMAC=_QtechDot11WIDSDeviceInfoMAC_Object((1,3,6,1,4,1,27514,1,1,10,2,62,3,8),_QtechDot11WIDSDeviceInfoMAC_Type())
qtechDot11WIDSDeviceInfoMAC.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDot11WIDSDeviceInfoMAC.setStatus(_A)
class _QtechDot11WIDSDeviceInfoString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_QtechDot11WIDSDeviceInfoString_Type.__name__=_F
_QtechDot11WIDSDeviceInfoString_Object=MibScalar
qtechDot11WIDSDeviceInfoString=_QtechDot11WIDSDeviceInfoString_Object((1,3,6,1,4,1,27514,1,1,10,2,62,3,9),_QtechDot11WIDSDeviceInfoString_Type())
qtechDot11WIDSDeviceInfoString.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDot11WIDSDeviceInfoString.setStatus(_A)
_QtechDot11WIDSSuspiciousDeviceMac_Type=MacAddress
_QtechDot11WIDSSuspiciousDeviceMac_Object=MibScalar
qtechDot11WIDSSuspiciousDeviceMac=_QtechDot11WIDSSuspiciousDeviceMac_Object((1,3,6,1,4,1,27514,1,1,10,2,62,3,10),_QtechDot11WIDSSuspiciousDeviceMac_Type())
qtechDot11WIDSSuspiciousDeviceMac.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDot11WIDSSuspiciousDeviceMac.setStatus(_A)
_QtechDot11WIDSSuspiciousDeviceExtensionInfo_Type=DisplayString
_QtechDot11WIDSSuspiciousDeviceExtensionInfo_Object=MibScalar
qtechDot11WIDSSuspiciousDeviceExtensionInfo=_QtechDot11WIDSSuspiciousDeviceExtensionInfo_Object((1,3,6,1,4,1,27514,1,1,10,2,62,3,11),_QtechDot11WIDSSuspiciousDeviceExtensionInfo_Type())
qtechDot11WIDSSuspiciousDeviceExtensionInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDot11WIDSSuspiciousDeviceExtensionInfo.setStatus(_A)
_QtechDot11WIDSUnauthorizedSSID_Type=DisplayString
_QtechDot11WIDSUnauthorizedSSID_Object=MibScalar
qtechDot11WIDSUnauthorizedSSID=_QtechDot11WIDSUnauthorizedSSID_Object((1,3,6,1,4,1,27514,1,1,10,2,62,3,12),_QtechDot11WIDSUnauthorizedSSID_Type())
qtechDot11WIDSUnauthorizedSSID.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDot11WIDSUnauthorizedSSID.setStatus(_A)
_QtechDot11WIDSSUnauthorizedSSIDExtensionInfo_Type=DisplayString
_QtechDot11WIDSSUnauthorizedSSIDExtensionInfo_Object=MibScalar
qtechDot11WIDSSUnauthorizedSSIDExtensionInfo=_QtechDot11WIDSSUnauthorizedSSIDExtensionInfo_Object((1,3,6,1,4,1,27514,1,1,10,2,62,3,13),_QtechDot11WIDSSUnauthorizedSSIDExtensionInfo_Type())
qtechDot11WIDSSUnauthorizedSSIDExtensionInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDot11WIDSSUnauthorizedSSIDExtensionInfo.setStatus(_A)
_QtechDot11WIDSAttackingDeviceMac_Type=MacAddress
_QtechDot11WIDSAttackingDeviceMac_Object=MibScalar
qtechDot11WIDSAttackingDeviceMac=_QtechDot11WIDSAttackingDeviceMac_Object((1,3,6,1,4,1,27514,1,1,10,2,62,3,14),_QtechDot11WIDSAttackingDeviceMac_Type())
qtechDot11WIDSAttackingDeviceMac.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDot11WIDSAttackingDeviceMac.setStatus(_A)
_QtechDot11WIDSAttackType_Type=Integer32
_QtechDot11WIDSAttackType_Object=MibScalar
qtechDot11WIDSAttackType=_QtechDot11WIDSAttackType_Object((1,3,6,1,4,1,27514,1,1,10,2,62,3,15),_QtechDot11WIDSAttackType_Type())
qtechDot11WIDSAttackType.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDot11WIDSAttackType.setStatus(_A)
_QtechDot11WIDSAttackExtensionInfo_Type=DisplayString
_QtechDot11WIDSAttackExtensionInfo_Object=MibScalar
qtechDot11WIDSAttackExtensionInfo=_QtechDot11WIDSAttackExtensionInfo_Object((1,3,6,1,4,1,27514,1,1,10,2,62,3,16),_QtechDot11WIDSAttackExtensionInfo_Type())
qtechDot11WIDSAttackExtensionInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDot11WIDSAttackExtensionInfo.setStatus(_A)
_QtechDot11WIDSMIBConform_ObjectIdentity=ObjectIdentity
qtechDot11WIDSMIBConform=_QtechDot11WIDSMIBConform_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,62,4))
_QtechDot11WIDSMIBCompliances_ObjectIdentity=ObjectIdentity
qtechDot11WIDSMIBCompliances=_QtechDot11WIDSMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,62,4,1))
_QtechDot11WIDSMIBGroups_ObjectIdentity=ObjectIdentity
qtechDot11WIDSMIBGroups=_QtechDot11WIDSMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,62,4,2))
qtechDot11WIDSMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,62,4,2,1))
qtechDot11WIDSMIBGroup.setObjects(*((_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:qtechDot11WIDSMIBGroup.setStatus(_A)
qtechDot11WIDSWirelessUserConnect=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,62,0,1))
qtechDot11WIDSWirelessUserConnect.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:qtechDot11WIDSWirelessUserConnect.setStatus(_A)
qtechDot11WIDSWirelessUserDisconnect=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,62,0,2))
qtechDot11WIDSWirelessUserDisconnect.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:qtechDot11WIDSWirelessUserDisconnect.setStatus(_A)
qtechDot11WIDSWirelessUserReauthentication=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,62,0,3))
qtechDot11WIDSWirelessUserReauthentication.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:qtechDot11WIDSWirelessUserReauthentication.setStatus(_A)
qtechDot11WIDSWirelessUserAuthenticationFailure=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,62,0,4))
qtechDot11WIDSWirelessUserAuthenticationFailure.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:qtechDot11WIDSWirelessUserAuthenticationFailure.setStatus(_A)
qtechDot11WIDSWirelessUserConnectFailure=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,62,0,5))
qtechDot11WIDSWirelessUserConnectFailure.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:qtechDot11WIDSWirelessUserConnectFailure.setStatus(_A)
qtechDot11WIDSDevice=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,62,0,6))
qtechDot11WIDSDevice.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:qtechDot11WIDSDevice.setStatus(_A)
qtechDot11WIDSSuspiciousDeviceTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,62,0,7))
qtechDot11WIDSSuspiciousDeviceTrap.setObjects(*((_B,_K),(_B,_L)))
if mibBuilder.loadTexts:qtechDot11WIDSSuspiciousDeviceTrap.setStatus(_A)
qtechDot11WIDSUnauthorizedSSIDTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,62,0,8))
qtechDot11WIDSUnauthorizedSSIDTrap.setObjects(*((_B,_M),(_B,_N)))
if mibBuilder.loadTexts:qtechDot11WIDSUnauthorizedSSIDTrap.setStatus(_A)
qtechDot11WIDSDetectingAttackTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,62,0,9))
qtechDot11WIDSDetectingAttackTrap.setObjects(*((_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:qtechDot11WIDSDetectingAttackTrap.setStatus(_A)
qtechDot11WIDSMIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,62,4,1,1))
qtechDot11WIDSMIBCompliance.setObjects((_B,_Ag))
if mibBuilder.loadTexts:qtechDot11WIDSMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'qtechDot11WIDSMIB':qtechDot11WIDSMIB,'qtechDot11WIDSTraps':qtechDot11WIDSTraps,'qtechDot11WIDSWirelessUserConnect':qtechDot11WIDSWirelessUserConnect,'qtechDot11WIDSWirelessUserDisconnect':qtechDot11WIDSWirelessUserDisconnect,'qtechDot11WIDSWirelessUserReauthentication':qtechDot11WIDSWirelessUserReauthentication,'qtechDot11WIDSWirelessUserAuthenticationFailure':qtechDot11WIDSWirelessUserAuthenticationFailure,'qtechDot11WIDSWirelessUserConnectFailure':qtechDot11WIDSWirelessUserConnectFailure,'qtechDot11WIDSDevice':qtechDot11WIDSDevice,'qtechDot11WIDSSuspiciousDeviceTrap':qtechDot11WIDSSuspiciousDeviceTrap,'qtechDot11WIDSUnauthorizedSSIDTrap':qtechDot11WIDSUnauthorizedSSIDTrap,'qtechDot11WIDSDetectingAttackTrap':qtechDot11WIDSDetectingAttackTrap,'qtechDot11WIDSConfigObjects':qtechDot11WIDSConfigObjects,'qtechDot11WIDSPermitVendorTable':qtechDot11WIDSPermitVendorTable,'qtechDot11WIDSPermitVendorEntry':qtechDot11WIDSPermitVendorEntry,_W:qtechDot11VendorOUI,_l:qtechDot11VendorOper,_m:qtechDot11VendorName,'qtechDot11WIDSPermitSSIDTable':qtechDot11WIDSPermitSSIDTable,'qtechDot11WIDSPermitSSIDEntry':qtechDot11WIDSPermitSSIDEntry,_X:qtechDot11PermitNum,_n:qtechDot11PermitOper,_o:qtechDot11PermitSSID,'qtechDot11WIDSDeviceAttackMacaddressListTable':qtechDot11WIDSDeviceAttackMacaddressListTable,'qtechDot11WIDSDeviceAttackMacaddressListEntry':qtechDot11WIDSDeviceAttackMacaddressListEntry,_Y:qtechDot11AttackNum,_p:qtechDot11AttackOper,_q:qtechDot11AttackMAC,_r:qtechDot11AttackInfo,'qtechDot11WIDSDevicePermitMacaddressListTable':qtechDot11WIDSDevicePermitMacaddressListTable,'qtechDot11WIDSDevicePermitMacaddressListEntry':qtechDot11WIDSDevicePermitMacaddressListEntry,_Z:qtechDot11PermitMACNum,_s:qtechDot11PermitMACOper,_t:qtechDot11PermitMACAddr,_u:qtechDot11WIDSDeviceagingDuration,_v:qtechDot11WIDSCountermeasuresMode,_w:qtechDot11WIDSCountermeasureSet,'qtechDot11WIDSModeTable':qtechDot11WIDSModeTable,'qtechDot11WIDSModeEntry':qtechDot11WIDSModeEntry,_a:qtechDot11WIDSAPID,_x:qtechDot11WIDSDeviceMode,'qtechDot11WIDSWhitelistMacaddressListTable':qtechDot11WIDSWhitelistMacaddressListTable,'qtechDot11WIDSWhitelistMacaddressListEntry':qtechDot11WIDSWhitelistMacaddressListEntry,_b:qtechDot11WhitelistNum,_y:qtechDot11WhitelistOper,_z:qtechDot11WhitelistMAC,'qtechDot11WIDSStaticblackListTable':qtechDot11WIDSStaticblackListTable,'qtechDot11WIDSStaticblackListEntry':qtechDot11WIDSStaticblackListEntry,_c:qtechDot11StaticblacklistNum,_A0:qtechDot11StaticblacklistOper,_A1:qtechDot11StaticblacklistMAC,_A2:qtechDot11WIDSDynamicblacklistEnable,_A3:qtechDot11WIDSDynamicblacklistLifetime,_A4:qtechDot11WIDSAttackDetectionMode,'qtechDot11WIDSRogueInfoTable':qtechDot11WIDSRogueInfoTable,'qtechDot11WIDSRogueInfoEntry':qtechDot11WIDSRogueInfoEntry,_d:qtechDot11WIDSRogueInfoNUM,_e:qtechDot11WIDSRogueInfoTYPE,_A5:qtechDot11WIDSRogueInfoOper,_A6:qtechDot11WIDSRogueInfoMAC,_A7:qtechDot11WIDSRogueInfoString,'qtechDot11WIDSPermitmaclistEnableTable':qtechDot11WIDSPermitmaclistEnableTable,'qtechDot11WIDSPermitmaclistEnableEntry':qtechDot11WIDSPermitmaclistEnableEntry,_f:qtechDot11WIDSEnableVlanPermitmaclistNum,_A8:qtechDot11WIDSEnableVlanPermitmaclistOper,_A9:qtechDot11WIDSEnableVlanPermitmaclist,_AA:qtechDot11WIDSResetStatistics,_AB:qtechDot11WIDSResetRoguehistoryStatistics,_AC:qtechDot11WIDSResethistory,'qtechDot11WIDSResetDynamicBlacklistTable':qtechDot11WIDSResetDynamicBlacklistTable,'qtechDot11WIDSResetDynamicBlacklistEntry':qtechDot11WIDSResetDynamicBlacklistEntry,_g:qtechDot11WIDSResetDynamicBlacklistMac,_AD:qtechDot11WIDSResetDynamicBlacklistType,_AE:qtechDot11WIDResetUserisolationStatistics,_AI:qtechDot11WIDUserisolationAC,_AJ:qtechDot11WIDUserisolationAP,'qtechDot11WIDSShowStaticsTable':qtechDot11WIDSShowStaticsTable,'qtechDot11WIDSShowStaticsEntry':qtechDot11WIDSShowStaticsEntry,_h:qtechDot11WIDSShowStaticsNum,_AK:qtechDot11WIDSShowStaticsOper,_AL:qtechDot11WIDSShowStaticsMac,_AM:qtechDot11WIDSShowStaticsInfo,_AN:qtechDot11WIDSAssociationFailureTotalTimes,'qtechDot11WIDSSuspiciousAPInfoTable':qtechDot11WIDSSuspiciousAPInfoTable,'qtechDot11WIDSSuspiciousAPInfoEntry':qtechDot11WIDSSuspiciousAPInfoEntry,_i:qtechDot11WIDSSuspiciousAPBSS,_AO:qtechDot11WIDSSuspiciousAPCount,_AP:qtechDot11WIDSMomentFirstTimeDetectedSusAP,_AQ:qtechDot11WIDSMomentLastTimeDetectedSusAP,_AR:qtechDot11WIDSSuspiciousAPSSID,_AS:qtechDot11WIDSSuspiciousAPMaxSignalStrength,_AT:qtechDot11WIDSSuspiciousAPUsingChannel,_AU:qtechDot11WIDSSuspiciousAPFrameEncrption,_AV:qtechDot11WIDSSuspiciousAPNeedsDealingTag,_AW:qtechDot11WIDSSuspiciousAPIgnoredTag,'qtechDot11WIDSSuspiciousSTAInfoTable':qtechDot11WIDSSuspiciousSTAInfoTable,'qtechDot11WIDSSuspiciousSTAInfoEntry':qtechDot11WIDSSuspiciousSTAInfoEntry,_j:qtechDot11WIDSSuspiciousSTAMAC,_AX:qtechDot11WIDSAPCountDetectingSuspiciousSTA,_AY:qtechDot11WIDSMomentFirstTimeDetectedSusSTA,_AZ:qtechDot11WIDSMomentLastTimeDetectedSusSTA,_Aa:qtechDot11WIDSBSSIDSuspiciousSTAAccessing,_Ab:qtechDot11WIDSSuspiciousSTAMaxSignalStrength,_Ac:qtechDot11WIDSSuspiciousSTAUsingChannel,_Ad:qtechDot11WIDSSuspiciousSTAWorksInAdhocMode,_Ae:qtechDot11WIDSSuspiciousSTANeedsDealingTag,_Af:qtechDot11WIDSSuspiciousSTAIgnoredTag,'qtechDot11WIDSDetectObjects':qtechDot11WIDSDetectObjects,'qtechDot11WIDSShowDot11IdsAttacklistTable':qtechDot11WIDSShowDot11IdsAttacklistTable,'qtechDot11WIDSShowDot11IdsAttacklistEntry':qtechDot11WIDSShowDot11IdsAttacklistEntry,_k:qtechDot11WIDSShowDot11IdsAttacklistNum,_AF:qtechDot11WIDSShowDot11IdsAttacklistOper,_AG:qtechDot11WIDSShowDot11IdsAttacklistMac,_AH:qtechDot11WIDSShowDot11IdsAttacklistInfo,'qtechDot11WIDSTrapsObjects':qtechDot11WIDSTrapsObjects,_G:qtechDot11WIDSSTAMAC,_H:qtechDot11WIDSAPBSSID,_I:qtechDot11WIDSInformation,_J:qtechDot11WIDSextinfo,_R:qtechDot11WIDSDeviceInfoNUM,_S:qtechDot11WIDSDeviceInfoTYPE,_T:qtechDot11WIDSDeviceInfoOper,_U:qtechDot11WIDSDeviceInfoMAC,_V:qtechDot11WIDSDeviceInfoString,_K:qtechDot11WIDSSuspiciousDeviceMac,_L:qtechDot11WIDSSuspiciousDeviceExtensionInfo,_M:qtechDot11WIDSUnauthorizedSSID,_N:qtechDot11WIDSSUnauthorizedSSIDExtensionInfo,_O:qtechDot11WIDSAttackingDeviceMac,_P:qtechDot11WIDSAttackType,_Q:qtechDot11WIDSAttackExtensionInfo,'qtechDot11WIDSMIBConform':qtechDot11WIDSMIBConform,'qtechDot11WIDSMIBCompliances':qtechDot11WIDSMIBCompliances,'qtechDot11WIDSMIBCompliance':qtechDot11WIDSMIBCompliance,'qtechDot11WIDSMIBGroups':qtechDot11WIDSMIBGroups,_Ag:qtechDot11WIDSMIBGroup})