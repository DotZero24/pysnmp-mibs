_AS='cmdot11plusBaseGroup'
_AR='cmdot11plusRemoteRadiusKey'
_AQ='cmdot11plusRemoteRadiusPort'
_AP='cmdot11plusRemoteRadiusIp'
_AO='cmdot11plusRemoteRadiusIpType'
_AN='cmdot11plusLocalPreSharedKey'
_AM='cmdot11plusWpaGroupRekeyInterval'
_AL='cmdot11plusWpaAuthMode'
_AK='cmdot11plusWpaEncryptionMode'
_AJ='cmdot11plusPhyOperatingMode'
_AI='cmdot11plusShortPreambleEnable'
_AH='cmdot11plusBasicRates'
_AG='cmdot11plusApplySettings'
_AF='cmdot11plusSecurityMode'
_AE='cmdot11plusGenerateWepKeys'
_AD='cmdot11plusWepPassPhrase'
_AC='cmdot11plusTxOutputPower'
_AB='cmdot11plusCountersReset'
_AA='cmdot11plusSsidBroadcastEnable'
_A9='cmdot11plusAclRowStatus'
_A8='cmdot11plusAclAddress'
_A7='cmdot11plusAclEnable'
_A6='cmdot11plusWep128DefaultKeyValue'
_A5='cmdot11plusWepMode'
_A4='cmdot11plusInterfaceEnable'
_A3='cmdot11plusSetToFactory'
_A2='cmdot11l2ogreSourceIfInstance'
_A1='cmdot11l2ogreStatsIndex'
_A0='cmdot11wifiHotspotIf'
_z='cmdot11plusClientIndex'
_y='cmdot11BssAccessIndex'
_x='cmdot11BssWep128BitKeyIndex'
_w='cmdot11BssWep64BitKeyIndex'
_v='disabled'
_u='milliseconds'
_t='rate54Mbps'
_s='rate48Mbps'
_r='rate36Mbps'
_q='rate24Mbps'
_p='rate18Mbps'
_o='rate12Mbps'
_n='rate11Mbps'
_m='rate9Mbps'
_l='rate6Mbps'
_k='rate5dot5Mbps'
_j='rate2Mbps'
_i='rate1Mbps'
_h='rateAuto'
_g='width-20MHz'
_f='band-5G'
_e='band-2-4G'
_d='legacy'
_c='mode54gLRS'
_b='mode54gPerformance'
_a='mode54gAuto'
_Z='mode54g11bOnly'
_Y='enable'
_X='cmdot11plusAclIndex'
_W='cmdot11plusWep128Index'
_V='2012-12-13 00:00'
_U='InetPortNumber'
_T='DisplayString'
_S='off'
_R='seconds'
_Q='none'
_P='disable'
_O='InetAddressType'
_N='auto'
_M='TruthValue'
_L='not-accessible'
_K='OctetString'
_J='Unsigned32'
_I='ifIndex'
_H='IF-MIB'
_G='read-create'
_F='read-only'
_E='CM-dot11plus-MIB'
_D='deprecated'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_H,_I)
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress',_O,_U)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'enterprises','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,StorageType,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_T,'MacAddress','PhysAddress','RowStatus','StorageType','TextualConvention',_M)
cmdot11plus=ModuleIdentity((1,3,6,1,4,1,1166,1,19,51))
if mibBuilder.loadTexts:cmdot11plus.setRevisions(('2014-06-12 00:00','2014-06-05 00:00','2013-08-01 00:00',_V,_V,'2012-04-10 00:00','2012-02-23 00:00','2011-05-24 00:00','2010-06-01 00:00','2009-11-16 00:00','2009-09-09 00:00','2009-08-11 00:00','2009-05-27 00:00','2008-12-19 00:00','2008-09-11 00:00','2004-02-13 00:00','2003-10-30 00:00','2003-07-15 00:00','2003-03-03 00:00','2002-10-08 00:00'))
_Gi_ObjectIdentity=ObjectIdentity
gi=_Gi_ObjectIdentity((1,3,6,1,4,1,1166))
_Giproducts_ObjectIdentity=ObjectIdentity
giproducts=_Giproducts_ObjectIdentity((1,3,6,1,4,1,1166,1))
_Cm_ObjectIdentity=ObjectIdentity
cm=_Cm_ObjectIdentity((1,3,6,1,4,1,1166,1,19))
_Cmdot11plusObjects_ObjectIdentity=ObjectIdentity
cmdot11plusObjects=_Cmdot11plusObjects_ObjectIdentity((1,3,6,1,4,1,1166,1,19,51,1))
_Cmdot11plusMgmt_ObjectIdentity=ObjectIdentity
cmdot11plusMgmt=_Cmdot11plusMgmt_ObjectIdentity((1,3,6,1,4,1,1166,1,19,51,1,1))
_Cmdot11plusMgmtObjects_ObjectIdentity=ObjectIdentity
cmdot11plusMgmtObjects=_Cmdot11plusMgmtObjects_ObjectIdentity((1,3,6,1,4,1,1166,1,19,51,1,1,1))
class _Cmdot11plusWepMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_P,1),('bit64',2),('bit128',3)))
_Cmdot11plusWepMode_Type.__name__=_C
_Cmdot11plusWepMode_Object=MibScalar
cmdot11plusWepMode=_Cmdot11plusWepMode_Object((1,3,6,1,4,1,1166,1,19,51,1,1,1,1),_Cmdot11plusWepMode_Type())
cmdot11plusWepMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11plusWepMode.setStatus(_D)
_Cmdot11plusWep128DefaultKeysTable_Object=MibTable
cmdot11plusWep128DefaultKeysTable=_Cmdot11plusWep128DefaultKeysTable_Object((1,3,6,1,4,1,1166,1,19,51,1,1,1,2))
if mibBuilder.loadTexts:cmdot11plusWep128DefaultKeysTable.setStatus(_D)
_Cmdot11plusWep128DefaultKeysEntry_Object=MibTableRow
cmdot11plusWep128DefaultKeysEntry=_Cmdot11plusWep128DefaultKeysEntry_Object((1,3,6,1,4,1,1166,1,19,51,1,1,1,2,1))
cmdot11plusWep128DefaultKeysEntry.setIndexNames((0,_E,_W))
if mibBuilder.loadTexts:cmdot11plusWep128DefaultKeysEntry.setStatus(_D)
class _Cmdot11plusWep128Index_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_Cmdot11plusWep128Index_Type.__name__=_C
_Cmdot11plusWep128Index_Object=MibTableColumn
cmdot11plusWep128Index=_Cmdot11plusWep128Index_Object((1,3,6,1,4,1,1166,1,19,51,1,1,1,2,1,1),_Cmdot11plusWep128Index_Type())
cmdot11plusWep128Index.setMaxAccess(_L)
if mibBuilder.loadTexts:cmdot11plusWep128Index.setStatus(_D)
class _Cmdot11plusWep128DefaultKeyValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(13,13));fixedLength=13
_Cmdot11plusWep128DefaultKeyValue_Type.__name__=_K
_Cmdot11plusWep128DefaultKeyValue_Object=MibTableColumn
cmdot11plusWep128DefaultKeyValue=_Cmdot11plusWep128DefaultKeyValue_Object((1,3,6,1,4,1,1166,1,19,51,1,1,1,2,1,2),_Cmdot11plusWep128DefaultKeyValue_Type())
cmdot11plusWep128DefaultKeyValue.setMaxAccess(_G)
if mibBuilder.loadTexts:cmdot11plusWep128DefaultKeyValue.setStatus(_D)
class _Cmdot11plusAclEnable_Type(TruthValue):defaultValue=2
_Cmdot11plusAclEnable_Type.__name__=_M
_Cmdot11plusAclEnable_Object=MibScalar
cmdot11plusAclEnable=_Cmdot11plusAclEnable_Object((1,3,6,1,4,1,1166,1,19,51,1,1,1,3),_Cmdot11plusAclEnable_Type())
cmdot11plusAclEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11plusAclEnable.setStatus(_D)
_Cmdot11plusAclTable_Object=MibTable
cmdot11plusAclTable=_Cmdot11plusAclTable_Object((1,3,6,1,4,1,1166,1,19,51,1,1,1,4))
if mibBuilder.loadTexts:cmdot11plusAclTable.setStatus(_D)
_Cmdot11plusAclEntry_Object=MibTableRow
cmdot11plusAclEntry=_Cmdot11plusAclEntry_Object((1,3,6,1,4,1,1166,1,19,51,1,1,1,4,1))
cmdot11plusAclEntry.setIndexNames((0,_E,_X))
if mibBuilder.loadTexts:cmdot11plusAclEntry.setStatus(_D)
class _Cmdot11plusAclIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_Cmdot11plusAclIndex_Type.__name__=_C
_Cmdot11plusAclIndex_Object=MibTableColumn
cmdot11plusAclIndex=_Cmdot11plusAclIndex_Object((1,3,6,1,4,1,1166,1,19,51,1,1,1,4,1,1),_Cmdot11plusAclIndex_Type())
cmdot11plusAclIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:cmdot11plusAclIndex.setStatus(_D)
_Cmdot11plusAclAddress_Type=MacAddress
_Cmdot11plusAclAddress_Object=MibTableColumn
cmdot11plusAclAddress=_Cmdot11plusAclAddress_Object((1,3,6,1,4,1,1166,1,19,51,1,1,1,4,1,2),_Cmdot11plusAclAddress_Type())
cmdot11plusAclAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:cmdot11plusAclAddress.setStatus(_D)
_Cmdot11plusAclRowStatus_Type=RowStatus
_Cmdot11plusAclRowStatus_Object=MibTableColumn
cmdot11plusAclRowStatus=_Cmdot11plusAclRowStatus_Object((1,3,6,1,4,1,1166,1,19,51,1,1,1,4,1,3),_Cmdot11plusAclRowStatus_Type())
cmdot11plusAclRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:cmdot11plusAclRowStatus.setStatus(_D)
class _Cmdot11plusSsidBroadcastEnable_Type(TruthValue):defaultValue=1
_Cmdot11plusSsidBroadcastEnable_Type.__name__=_M
_Cmdot11plusSsidBroadcastEnable_Object=MibScalar
cmdot11plusSsidBroadcastEnable=_Cmdot11plusSsidBroadcastEnable_Object((1,3,6,1,4,1,1166,1,19,51,1,1,1,5),_Cmdot11plusSsidBroadcastEnable_Type())
cmdot11plusSsidBroadcastEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11plusSsidBroadcastEnable.setStatus(_D)
class _Cmdot11plusBasicRates_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('low',1),('high',2)))
_Cmdot11plusBasicRates_Type.__name__=_C
_Cmdot11plusBasicRates_Object=MibScalar
cmdot11plusBasicRates=_Cmdot11plusBasicRates_Object((1,3,6,1,4,1,1166,1,19,51,1,1,1,6),_Cmdot11plusBasicRates_Type())
cmdot11plusBasicRates.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11plusBasicRates.setStatus(_D)
class _Cmdot11plusShortPreambleEnable_Type(TruthValue):defaultValue=2
_Cmdot11plusShortPreambleEnable_Type.__name__=_M
_Cmdot11plusShortPreambleEnable_Object=MibScalar
cmdot11plusShortPreambleEnable=_Cmdot11plusShortPreambleEnable_Object((1,3,6,1,4,1,1166,1,19,51,1,1,1,7),_Cmdot11plusShortPreambleEnable_Type())
cmdot11plusShortPreambleEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11plusShortPreambleEnable.setStatus(_D)
_Cmdot11plusCountersReset_Type=TruthValue
_Cmdot11plusCountersReset_Object=MibScalar
cmdot11plusCountersReset=_Cmdot11plusCountersReset_Object((1,3,6,1,4,1,1166,1,19,51,1,1,1,8),_Cmdot11plusCountersReset_Type())
cmdot11plusCountersReset.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11plusCountersReset.setStatus(_D)
class _Cmdot11plusPhyOperatingMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('standard',1),('enhanced',2)))
_Cmdot11plusPhyOperatingMode_Type.__name__=_C
_Cmdot11plusPhyOperatingMode_Object=MibScalar
cmdot11plusPhyOperatingMode=_Cmdot11plusPhyOperatingMode_Object((1,3,6,1,4,1,1166,1,19,51,1,1,1,9),_Cmdot11plusPhyOperatingMode_Type())
cmdot11plusPhyOperatingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11plusPhyOperatingMode.setStatus(_D)
class _Cmdot11plusTxOutputPower_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,100),ValueRangeConstraint(75,75),ValueRangeConstraint(50,50),ValueRangeConstraint(25,25),ValueRangeConstraint(12,12),ValueRangeConstraint(6,6),ValueRangeConstraint(3,3))
_Cmdot11plusTxOutputPower_Type.__name__=_C
_Cmdot11plusTxOutputPower_Object=MibScalar
cmdot11plusTxOutputPower=_Cmdot11plusTxOutputPower_Object((1,3,6,1,4,1,1166,1,19,51,1,1,1,10),_Cmdot11plusTxOutputPower_Type())
cmdot11plusTxOutputPower.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11plusTxOutputPower.setStatus(_D)
class _Cmdot11plusWepPassPhrase_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,31))
_Cmdot11plusWepPassPhrase_Type.__name__=_T
_Cmdot11plusWepPassPhrase_Object=MibScalar
cmdot11plusWepPassPhrase=_Cmdot11plusWepPassPhrase_Object((1,3,6,1,4,1,1166,1,19,51,1,1,1,11),_Cmdot11plusWepPassPhrase_Type())
cmdot11plusWepPassPhrase.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11plusWepPassPhrase.setStatus(_D)
_Cmdot11plusGenerateWepKeys_Type=TruthValue
_Cmdot11plusGenerateWepKeys_Object=MibScalar
cmdot11plusGenerateWepKeys=_Cmdot11plusGenerateWepKeys_Object((1,3,6,1,4,1,1166,1,19,51,1,1,1,12),_Cmdot11plusGenerateWepKeys_Type())
cmdot11plusGenerateWepKeys.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11plusGenerateWepKeys.setStatus(_D)
class _Cmdot11plusSecurityMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Q,1),('wep',2),('wpa',3)))
_Cmdot11plusSecurityMode_Type.__name__=_C
_Cmdot11plusSecurityMode_Object=MibScalar
cmdot11plusSecurityMode=_Cmdot11plusSecurityMode_Object((1,3,6,1,4,1,1166,1,19,51,1,1,1,13),_Cmdot11plusSecurityMode_Type())
cmdot11plusSecurityMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11plusSecurityMode.setStatus(_D)
_Cmdot11plusWpaObjects_ObjectIdentity=ObjectIdentity
cmdot11plusWpaObjects=_Cmdot11plusWpaObjects_ObjectIdentity((1,3,6,1,4,1,1166,1,19,51,1,1,2))
class _Cmdot11plusWpaAuthMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('local',1),('remote',2)))
_Cmdot11plusWpaAuthMode_Type.__name__=_C
_Cmdot11plusWpaAuthMode_Object=MibScalar
cmdot11plusWpaAuthMode=_Cmdot11plusWpaAuthMode_Object((1,3,6,1,4,1,1166,1,19,51,1,1,2,1),_Cmdot11plusWpaAuthMode_Type())
cmdot11plusWpaAuthMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11plusWpaAuthMode.setStatus(_D)
class _Cmdot11plusWpaGroupRekeyInterval_Type(Unsigned32):defaultValue=300
_Cmdot11plusWpaGroupRekeyInterval_Type.__name__=_J
_Cmdot11plusWpaGroupRekeyInterval_Object=MibScalar
cmdot11plusWpaGroupRekeyInterval=_Cmdot11plusWpaGroupRekeyInterval_Object((1,3,6,1,4,1,1166,1,19,51,1,1,2,2),_Cmdot11plusWpaGroupRekeyInterval_Type())
cmdot11plusWpaGroupRekeyInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11plusWpaGroupRekeyInterval.setStatus(_D)
if mibBuilder.loadTexts:cmdot11plusWpaGroupRekeyInterval.setUnits(_R)
class _Cmdot11plusWpaEncryptionMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('tkip',1),('aes',2)))
_Cmdot11plusWpaEncryptionMode_Type.__name__=_C
_Cmdot11plusWpaEncryptionMode_Object=MibScalar
cmdot11plusWpaEncryptionMode=_Cmdot11plusWpaEncryptionMode_Object((1,3,6,1,4,1,1166,1,19,51,1,1,2,3),_Cmdot11plusWpaEncryptionMode_Type())
cmdot11plusWpaEncryptionMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11plusWpaEncryptionMode.setStatus(_D)
class _Cmdot11plusLocalPreSharedKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,63))
_Cmdot11plusLocalPreSharedKey_Type.__name__=_K
_Cmdot11plusLocalPreSharedKey_Object=MibScalar
cmdot11plusLocalPreSharedKey=_Cmdot11plusLocalPreSharedKey_Object((1,3,6,1,4,1,1166,1,19,51,1,1,2,4),_Cmdot11plusLocalPreSharedKey_Type())
cmdot11plusLocalPreSharedKey.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11plusLocalPreSharedKey.setStatus(_D)
class _Cmdot11plusRemoteRadiusIpType_Type(InetAddressType):defaultValue=1
_Cmdot11plusRemoteRadiusIpType_Type.__name__=_O
_Cmdot11plusRemoteRadiusIpType_Object=MibScalar
cmdot11plusRemoteRadiusIpType=_Cmdot11plusRemoteRadiusIpType_Object((1,3,6,1,4,1,1166,1,19,51,1,1,2,5),_Cmdot11plusRemoteRadiusIpType_Type())
cmdot11plusRemoteRadiusIpType.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11plusRemoteRadiusIpType.setStatus(_D)
class _Cmdot11plusRemoteRadiusIp_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_Cmdot11plusRemoteRadiusIp_Type.__name__=_K
_Cmdot11plusRemoteRadiusIp_Object=MibScalar
cmdot11plusRemoteRadiusIp=_Cmdot11plusRemoteRadiusIp_Object((1,3,6,1,4,1,1166,1,19,51,1,1,2,6),_Cmdot11plusRemoteRadiusIp_Type())
cmdot11plusRemoteRadiusIp.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11plusRemoteRadiusIp.setStatus(_D)
class _Cmdot11plusRemoteRadiusPort_Type(InetPortNumber):defaultValue=1812
_Cmdot11plusRemoteRadiusPort_Type.__name__=_U
_Cmdot11plusRemoteRadiusPort_Object=MibScalar
cmdot11plusRemoteRadiusPort=_Cmdot11plusRemoteRadiusPort_Object((1,3,6,1,4,1,1166,1,19,51,1,1,2,7),_Cmdot11plusRemoteRadiusPort_Type())
cmdot11plusRemoteRadiusPort.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11plusRemoteRadiusPort.setStatus(_D)
class _Cmdot11plusRemoteRadiusKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Cmdot11plusRemoteRadiusKey_Type.__name__=_K
_Cmdot11plusRemoteRadiusKey_Object=MibScalar
cmdot11plusRemoteRadiusKey=_Cmdot11plusRemoteRadiusKey_Object((1,3,6,1,4,1,1166,1,19,51,1,1,2,8),_Cmdot11plusRemoteRadiusKey_Type())
cmdot11plusRemoteRadiusKey.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11plusRemoteRadiusKey.setStatus(_D)
_Cmdot11plusBaseObjects_ObjectIdentity=ObjectIdentity
cmdot11plusBaseObjects=_Cmdot11plusBaseObjects_ObjectIdentity((1,3,6,1,4,1,1166,1,19,51,1,2))
_Cmdot11plusSetToFactory_Type=TruthValue
_Cmdot11plusSetToFactory_Object=MibScalar
cmdot11plusSetToFactory=_Cmdot11plusSetToFactory_Object((1,3,6,1,4,1,1166,1,19,51,1,2,1),_Cmdot11plusSetToFactory_Type())
cmdot11plusSetToFactory.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11plusSetToFactory.setStatus(_D)
class _Cmdot11plusInterfaceEnable_Type(TruthValue):defaultValue=1
_Cmdot11plusInterfaceEnable_Type.__name__=_M
_Cmdot11plusInterfaceEnable_Object=MibScalar
cmdot11plusInterfaceEnable=_Cmdot11plusInterfaceEnable_Object((1,3,6,1,4,1,1166,1,19,51,1,2,2),_Cmdot11plusInterfaceEnable_Type())
cmdot11plusInterfaceEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11plusInterfaceEnable.setStatus(_D)
_Cmdot11plusApplySettings_Type=TruthValue
_Cmdot11plusApplySettings_Object=MibScalar
cmdot11plusApplySettings=_Cmdot11plusApplySettings_Object((1,3,6,1,4,1,1166,1,19,51,1,2,3),_Cmdot11plusApplySettings_Type())
cmdot11plusApplySettings.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11plusApplySettings.setStatus(_D)
_Cmdot11plusMgmtv2_ObjectIdentity=ObjectIdentity
cmdot11plusMgmtv2=_Cmdot11plusMgmtv2_ObjectIdentity((1,3,6,1,4,1,1166,1,19,51,1,5))
_Cmdot11MgmtBase_ObjectIdentity=ObjectIdentity
cmdot11MgmtBase=_Cmdot11MgmtBase_ObjectIdentity((1,3,6,1,4,1,1166,1,19,51,1,5,1))
class _Cmdot11OperMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Y,1),(_P,2)))
_Cmdot11OperMode_Type.__name__=_C
_Cmdot11OperMode_Object=MibScalar
cmdot11OperMode=_Cmdot11OperMode_Object((1,3,6,1,4,1,1166,1,19,51,1,5,1,1),_Cmdot11OperMode_Type())
cmdot11OperMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11OperMode.setStatus(_D)
_Cmdot11CurrentChannel_Type=Unsigned32
_Cmdot11CurrentChannel_Object=MibScalar
cmdot11CurrentChannel=_Cmdot11CurrentChannel_Object((1,3,6,1,4,1,1166,1,19,51,1,5,1,2),_Cmdot11CurrentChannel_Type())
cmdot11CurrentChannel.setMaxAccess(_F)
if mibBuilder.loadTexts:cmdot11CurrentChannel.setStatus(_D)
class _Cmdot11ChannelSetting_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,216))
_Cmdot11ChannelSetting_Type.__name__=_J
_Cmdot11ChannelSetting_Object=MibScalar
cmdot11ChannelSetting=_Cmdot11ChannelSetting_Object((1,3,6,1,4,1,1166,1,19,51,1,5,1,3),_Cmdot11ChannelSetting_Type())
cmdot11ChannelSetting.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11ChannelSetting.setStatus(_D)
class _Cmdot1154gNetMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,4,5)));namedValues=NamedValues(*((_Z,0),(_a,1),(_b,4),(_c,5)))
_Cmdot1154gNetMode_Type.__name__=_C
_Cmdot1154gNetMode_Object=MibScalar
cmdot1154gNetMode=_Cmdot1154gNetMode_Object((1,3,6,1,4,1,1166,1,19,51,1,5,1,10),_Cmdot1154gNetMode_Type())
cmdot1154gNetMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot1154gNetMode.setStatus(_D)
class _Cmdot11NMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_S,2)))
_Cmdot11NMode_Type.__name__=_C
_Cmdot11NMode_Object=MibScalar
cmdot11NMode=_Cmdot11NMode_Object((1,3,6,1,4,1,1166,1,19,51,1,5,1,16),_Cmdot11NMode_Type())
cmdot11NMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11NMode.setStatus(_D)
class _Cmdot11NPhyRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)));namedValues=NamedValues(*((_N,0),(_d,1),('mcs0',2),('mcs1',3),('mcs2',4),('mcs3',5),('mcs4',6),('mcs5',7),('mcs6',8),('mcs7',9),('mcs8',10),('mcs9',11),('mcs10',12),('mcs11',13),('mcs12',14),('mcs13',15),('mcs14',16),('mcs15',17)))
_Cmdot11NPhyRate_Type.__name__=_C
_Cmdot11NPhyRate_Object=MibScalar
cmdot11NPhyRate=_Cmdot11NPhyRate_Object((1,3,6,1,4,1,1166,1,19,51,1,5,1,17),_Cmdot11NPhyRate_Type())
cmdot11NPhyRate.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11NPhyRate.setStatus(_D)
class _Cmdot11NBand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_e,1),(_f,2)))
_Cmdot11NBand_Type.__name__=_C
_Cmdot11NBand_Object=MibScalar
cmdot11NBand=_Cmdot11NBand_Object((1,3,6,1,4,1,1166,1,19,51,1,5,1,18),_Cmdot11NBand_Type())
cmdot11NBand.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11NBand.setStatus(_D)
class _Cmdot11NBandWidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_g,1),('width-20-40MHz',2)))
_Cmdot11NBandWidth_Type.__name__=_C
_Cmdot11NBandWidth_Object=MibScalar
cmdot11NBandWidth=_Cmdot11NBandWidth_Object((1,3,6,1,4,1,1166,1,19,51,1,5,1,19),_Cmdot11NBandWidth_Type())
cmdot11NBandWidth.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11NBandWidth.setStatus(_D)
class _Cmdot11NSideBand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('upper',1),('lower',2)))
_Cmdot11NSideBand_Type.__name__=_C
_Cmdot11NSideBand_Object=MibScalar
cmdot11NSideBand=_Cmdot11NSideBand_Object((1,3,6,1,4,1,1166,1,19,51,1,5,1,20),_Cmdot11NSideBand_Type())
cmdot11NSideBand.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11NSideBand.setStatus(_D)
class _Cmdot11NProtection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_S,2)))
_Cmdot11NProtection_Type.__name__=_C
_Cmdot11NProtection_Object=MibScalar
cmdot11NProtection=_Cmdot11NProtection_Object((1,3,6,1,4,1,1166,1,19,51,1,5,1,21),_Cmdot11NProtection_Type())
cmdot11NProtection.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11NProtection.setStatus(_D)
class _Cmdot11MulticastRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*((_h,1),(_i,2),(_j,3),(_k,4),(_l,5),(_m,6),(_n,7),(_o,8),(_p,9),(_q,10),(_r,11),(_s,12),(_t,13)))
_Cmdot11MulticastRate_Type.__name__=_C
_Cmdot11MulticastRate_Object=MibScalar
cmdot11MulticastRate=_Cmdot11MulticastRate_Object((1,3,6,1,4,1,1166,1,19,51,1,5,1,100),_Cmdot11MulticastRate_Type())
cmdot11MulticastRate.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11MulticastRate.setStatus(_D)
_Cmdot11MgmtInterfaceTables_ObjectIdentity=ObjectIdentity
cmdot11MgmtInterfaceTables=_Cmdot11MgmtInterfaceTables_ObjectIdentity((1,3,6,1,4,1,1166,1,19,51,1,5,2))
_Cmdot11BaseTable_Object=MibTable
cmdot11BaseTable=_Cmdot11BaseTable_Object((1,3,6,1,4,1,1166,1,19,51,1,5,2,1))
if mibBuilder.loadTexts:cmdot11BaseTable.setStatus(_A)
_Cmdot11BaseEntry_Object=MibTableRow
cmdot11BaseEntry=_Cmdot11BaseEntry_Object((1,3,6,1,4,1,1166,1,19,51,1,5,2,1,1))
cmdot11BaseEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:cmdot11BaseEntry.setStatus(_A)
class _Cmdot11WifiOperMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Y,1),(_P,2)))
_Cmdot11WifiOperMode_Type.__name__=_C
_Cmdot11WifiOperMode_Object=MibTableColumn
cmdot11WifiOperMode=_Cmdot11WifiOperMode_Object((1,3,6,1,4,1,1166,1,19,51,1,5,2,1,1,1),_Cmdot11WifiOperMode_Type())
cmdot11WifiOperMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11WifiOperMode.setStatus(_A)
class _Cmdot11WifiCurrentChannel_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,216))
_Cmdot11WifiCurrentChannel_Type.__name__=_J
_Cmdot11WifiCurrentChannel_Object=MibTableColumn
cmdot11WifiCurrentChannel=_Cmdot11WifiCurrentChannel_Object((1,3,6,1,4,1,1166,1,19,51,1,5,2,1,1,2),_Cmdot11WifiCurrentChannel_Type())
cmdot11WifiCurrentChannel.setMaxAccess(_F)
if mibBuilder.loadTexts:cmdot11WifiCurrentChannel.setStatus(_A)
class _Cmdot11WifiBeaconInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Cmdot11WifiBeaconInterval_Type.__name__=_J
_Cmdot11WifiBeaconInterval_Object=MibTableColumn
cmdot11WifiBeaconInterval=_Cmdot11WifiBeaconInterval_Object((1,3,6,1,4,1,1166,1,19,51,1,5,2,1,1,3),_Cmdot11WifiBeaconInterval_Type())
cmdot11WifiBeaconInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11WifiBeaconInterval.setStatus(_A)
if mibBuilder.loadTexts:cmdot11WifiBeaconInterval.setUnits(_u)
class _Cmdot11WifiDTIMInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_Cmdot11WifiDTIMInterval_Type.__name__=_J
_Cmdot11WifiDTIMInterval_Object=MibTableColumn
cmdot11WifiDTIMInterval=_Cmdot11WifiDTIMInterval_Object((1,3,6,1,4,1,1166,1,19,51,1,5,2,1,1,4),_Cmdot11WifiDTIMInterval_Type())
cmdot11WifiDTIMInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11WifiDTIMInterval.setStatus(_A)
if mibBuilder.loadTexts:cmdot11WifiDTIMInterval.setUnits(_u)
class _Cmdot11WifiFragThresh_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(256,2346))
_Cmdot11WifiFragThresh_Type.__name__=_J
_Cmdot11WifiFragThresh_Object=MibTableColumn
cmdot11WifiFragThresh=_Cmdot11WifiFragThresh_Object((1,3,6,1,4,1,1166,1,19,51,1,5,2,1,1,5),_Cmdot11WifiFragThresh_Type())
cmdot11WifiFragThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11WifiFragThresh.setStatus(_A)
if mibBuilder.loadTexts:cmdot11WifiFragThresh.setUnits('bytes')
class _Cmdot11WifiRTSThresh_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2347))
_Cmdot11WifiRTSThresh_Type.__name__=_J
_Cmdot11WifiRTSThresh_Object=MibTableColumn
cmdot11WifiRTSThresh=_Cmdot11WifiRTSThresh_Object((1,3,6,1,4,1,1166,1,19,51,1,5,2,1,1,6),_Cmdot11WifiRTSThresh_Type())
cmdot11WifiRTSThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11WifiRTSThresh.setStatus(_A)
class _Cmdot11WifiShortRetryLimit_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_Cmdot11WifiShortRetryLimit_Type.__name__=_J
_Cmdot11WifiShortRetryLimit_Object=MibTableColumn
cmdot11WifiShortRetryLimit=_Cmdot11WifiShortRetryLimit_Object((1,3,6,1,4,1,1166,1,19,51,1,5,2,1,1,7),_Cmdot11WifiShortRetryLimit_Type())
cmdot11WifiShortRetryLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11WifiShortRetryLimit.setStatus(_A)
class _Cmdot11WifiLongRetryLimit_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_Cmdot11WifiLongRetryLimit_Type.__name__=_J
_Cmdot11WifiLongRetryLimit_Object=MibTableColumn
cmdot11WifiLongRetryLimit=_Cmdot11WifiLongRetryLimit_Object((1,3,6,1,4,1,1166,1,19,51,1,5,2,1,1,8),_Cmdot11WifiLongRetryLimit_Type())
cmdot11WifiLongRetryLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11WifiLongRetryLimit.setStatus(_A)
class _Cmdot11WifiMulticastRate_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*((_h,1),(_i,2),(_j,3),(_k,4),(_l,5),(_m,6),(_n,7),(_o,8),(_p,9),(_q,10),(_r,11),(_s,12),(_t,13)))
_Cmdot11WifiMulticastRate_Type.__name__=_C
_Cmdot11WifiMulticastRate_Object=MibTableColumn
cmdot11WifiMulticastRate=_Cmdot11WifiMulticastRate_Object((1,3,6,1,4,1,1166,1,19,51,1,5,2,1,1,9),_Cmdot11WifiMulticastRate_Type())
cmdot11WifiMulticastRate.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11WifiMulticastRate.setStatus(_A)
class _Cmdot11WifiOutputPower_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(25,50,75,100)));namedValues=NamedValues(*(('percent25',25),('percent50',50),('percent75',75),('percent100',100)))
_Cmdot11WifiOutputPower_Type.__name__=_C
_Cmdot11WifiOutputPower_Object=MibTableColumn
cmdot11WifiOutputPower=_Cmdot11WifiOutputPower_Object((1,3,6,1,4,1,1166,1,19,51,1,5,2,1,1,10),_Cmdot11WifiOutputPower_Type())
cmdot11WifiOutputPower.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11WifiOutputPower.setStatus(_A)
_Cmdot11WifiResetToDefaults_Type=TruthValue
_Cmdot11WifiResetToDefaults_Object=MibTableColumn
cmdot11WifiResetToDefaults=_Cmdot11WifiResetToDefaults_Object((1,3,6,1,4,1,1166,1,19,51,1,5,2,1,1,11),_Cmdot11WifiResetToDefaults_Type())
cmdot11WifiResetToDefaults.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11WifiResetToDefaults.setStatus(_A)
class _Cmdot11WifiChannelSetting_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,216))
_Cmdot11WifiChannelSetting_Type.__name__=_J
_Cmdot11WifiChannelSetting_Object=MibTableColumn
cmdot11WifiChannelSetting=_Cmdot11WifiChannelSetting_Object((1,3,6,1,4,1,1166,1,19,51,1,5,2,1,1,12),_Cmdot11WifiChannelSetting_Type())
cmdot11WifiChannelSetting.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11WifiChannelSetting.setStatus(_A)
_Cmdot11WifiApsScan_Type=TruthValue
_Cmdot11WifiApsScan_Object=MibTableColumn
cmdot11WifiApsScan=_Cmdot11WifiApsScan_Object((1,3,6,1,4,1,1166,1,19,51,1,5,2,1,1,13),_Cmdot11WifiApsScan_Type())
cmdot11WifiApsScan.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11WifiApsScan.setStatus(_A)
_Cmdot11WifiObssCoexMode_Type=TruthValue
_Cmdot11WifiObssCoexMode_Object=MibTableColumn
cmdot11WifiObssCoexMode=_Cmdot11WifiObssCoexMode_Object((1,3,6,1,4,1,1166,1,19,51,1,5,2,1,1,14),_Cmdot11WifiObssCoexMode_Type())
cmdot11WifiObssCoexMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11WifiObssCoexMode.setStatus(_A)
class _Cmdot11WifiAcsdScanTimer_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,268435454))
_Cmdot11WifiAcsdScanTimer_Type.__name__=_J
_Cmdot11WifiAcsdScanTimer_Object=MibTableColumn
cmdot11WifiAcsdScanTimer=_Cmdot11WifiAcsdScanTimer_Object((1,3,6,1,4,1,1166,1,19,51,1,5,2,1,1,15),_Cmdot11WifiAcsdScanTimer_Type())
cmdot11WifiAcsdScanTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11WifiAcsdScanTimer.setStatus(_A)
if mibBuilder.loadTexts:cmdot11WifiAcsdScanTimer.setUnits(_R)
_Cmdot11WifiWMFEnable_Type=TruthValue
_Cmdot11WifiWMFEnable_Object=MibTableColumn
cmdot11WifiWMFEnable=_Cmdot11WifiWMFEnable_Object((1,3,6,1,4,1,1166,1,19,51,1,5,2,1,1,16),_Cmdot11WifiWMFEnable_Type())
cmdot11WifiWMFEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11WifiWMFEnable.setStatus(_A)
_Cmdot11WifiBSEnable_Type=TruthValue
_Cmdot11WifiBSEnable_Object=MibTableColumn
cmdot11WifiBSEnable=_Cmdot11WifiBSEnable_Object((1,3,6,1,4,1,1166,1,19,51,1,5,2,1,1,17),_Cmdot11WifiBSEnable_Type())
cmdot11WifiBSEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11WifiBSEnable.setStatus(_A)
_Cmdot11WifiATFEnable_Type=TruthValue
_Cmdot11WifiATFEnable_Object=MibTableColumn
cmdot11WifiATFEnable=_Cmdot11WifiATFEnable_Object((1,3,6,1,4,1,1166,1,19,51,1,5,2,1,1,18),_Cmdot11WifiATFEnable_Type())
cmdot11WifiATFEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11WifiATFEnable.setStatus(_A)
_Cmdot11WifiTrafficSchedulerEnable_Type=TruthValue
_Cmdot11WifiTrafficSchedulerEnable_Object=MibTableColumn
cmdot11WifiTrafficSchedulerEnable=_Cmdot11WifiTrafficSchedulerEnable_Object((1,3,6,1,4,1,1166,1,19,51,1,5,2,1,1,19),_Cmdot11WifiTrafficSchedulerEnable_Type())
cmdot11WifiTrafficSchedulerEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11WifiTrafficSchedulerEnable.setStatus(_A)
_Cmdot11WifiEbosEnable_Type=TruthValue
_Cmdot11WifiEbosEnable_Object=MibTableColumn
cmdot11WifiEbosEnable=_Cmdot11WifiEbosEnable_Object((1,3,6,1,4,1,1166,1,19,51,1,5,2,1,1,20),_Cmdot11WifiEbosEnable_Type())
cmdot11WifiEbosEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11WifiEbosEnable.setStatus(_A)
_Cmdot11gTable_Object=MibTable
cmdot11gTable=_Cmdot11gTable_Object((1,3,6,1,4,1,1166,1,19,51,1,5,2,2))
if mibBuilder.loadTexts:cmdot11gTable.setStatus(_A)
_Cmdot11gEntry_Object=MibTableRow
cmdot11gEntry=_Cmdot11gEntry_Object((1,3,6,1,4,1,1166,1,19,51,1,5,2,2,1))
cmdot11gEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:cmdot11gEntry.setStatus(_A)
class _Cmdot11Wifi54gNetMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4,5)));namedValues=NamedValues(*((_Z,0),(_a,1),('mode54gOnly',2),(_b,4),(_c,5)))
_Cmdot11Wifi54gNetMode_Type.__name__=_C
_Cmdot11Wifi54gNetMode_Object=MibTableColumn
cmdot11Wifi54gNetMode=_Cmdot11Wifi54gNetMode_Object((1,3,6,1,4,1,1166,1,19,51,1,5,2,2,1,1),_Cmdot11Wifi54gNetMode_Type())
cmdot11Wifi54gNetMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11Wifi54gNetMode.setStatus(_A)
class _Cmdot11Wifi54gProtectionEnable_Type(TruthValue):defaultValue=2
_Cmdot11Wifi54gProtectionEnable_Type.__name__=_M
_Cmdot11Wifi54gProtectionEnable_Object=MibTableColumn
cmdot11Wifi54gProtectionEnable=_Cmdot11Wifi54gProtectionEnable_Object((1,3,6,1,4,1,1166,1,19,51,1,5,2,2,1,2),_Cmdot11Wifi54gProtectionEnable_Type())
cmdot11Wifi54gProtectionEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11Wifi54gProtectionEnable.setStatus(_A)
class _Cmdot11Wifi54gBasicRateSet_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('default',1),('all',2)))
_Cmdot11Wifi54gBasicRateSet_Type.__name__=_C
_Cmdot11Wifi54gBasicRateSet_Object=MibTableColumn
cmdot11Wifi54gBasicRateSet=_Cmdot11Wifi54gBasicRateSet_Object((1,3,6,1,4,1,1166,1,19,51,1,5,2,2,1,3),_Cmdot11Wifi54gBasicRateSet_Type())
cmdot11Wifi54gBasicRateSet.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11Wifi54gBasicRateSet.setStatus(_A)
_Cmdot11nTable_Object=MibTable
cmdot11nTable=_Cmdot11nTable_Object((1,3,6,1,4,1,1166,1,19,51,1,5,2,3))
if mibBuilder.loadTexts:cmdot11nTable.setStatus(_A)
_Cmdot11nEntry_Object=MibTableRow
cmdot11nEntry=_Cmdot11nEntry_Object((1,3,6,1,4,1,1166,1,19,51,1,5,2,3,1))
cmdot11nEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:cmdot11nEntry.setStatus(_A)
class _Cmdot11WifiNMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),(_S,2),('nOnly',3)))
_Cmdot11WifiNMode_Type.__name__=_C
_Cmdot11WifiNMode_Object=MibTableColumn
cmdot11WifiNMode=_Cmdot11WifiNMode_Object((1,3,6,1,4,1,1166,1,19,51,1,5,2,3,1,1),_Cmdot11WifiNMode_Type())
cmdot11WifiNMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11WifiNMode.setStatus(_A)
class _Cmdot11WifiNPhyRate_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)));namedValues=NamedValues(*((_N,0),(_d,1),('mcs0',2),('mcs1',3),('mcs2',4),('mcs3',5),('mcs4',6),('mcs5',7),('mcs6',8),('mcs7',9),('mcs8',10),('mcs9',11),('mcs10',12),('mcs11',13),('mcs12',14),('mcs13',15),('mcs14',16),('mcs15',17)))
_Cmdot11WifiNPhyRate_Type.__name__=_C
_Cmdot11WifiNPhyRate_Object=MibTableColumn
cmdot11WifiNPhyRate=_Cmdot11WifiNPhyRate_Object((1,3,6,1,4,1,1166,1,19,51,1,5,2,3,1,2),_Cmdot11WifiNPhyRate_Type())
cmdot11WifiNPhyRate.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11WifiNPhyRate.setStatus(_A)
class _Cmdot11WifiNBand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_e,1),(_f,2)))
_Cmdot11WifiNBand_Type.__name__=_C
_Cmdot11WifiNBand_Object=MibTableColumn
cmdot11WifiNBand=_Cmdot11WifiNBand_Object((1,3,6,1,4,1,1166,1,19,51,1,5,2,3,1,3),_Cmdot11WifiNBand_Type())
cmdot11WifiNBand.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11WifiNBand.setStatus(_A)
class _Cmdot11WifiNBandWidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_Q,0),(_g,1),('width-40MHz',2)))
_Cmdot11WifiNBandWidth_Type.__name__=_C
_Cmdot11WifiNBandWidth_Object=MibTableColumn
cmdot11WifiNBandWidth=_Cmdot11WifiNBandWidth_Object((1,3,6,1,4,1,1166,1,19,51,1,5,2,3,1,4),_Cmdot11WifiNBandWidth_Type())
cmdot11WifiNBandWidth.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11WifiNBandWidth.setStatus(_A)
class _Cmdot11WifiNSideBand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_Q,0),('upper',1),('lower',2)))
_Cmdot11WifiNSideBand_Type.__name__=_C
_Cmdot11WifiNSideBand_Object=MibTableColumn
cmdot11WifiNSideBand=_Cmdot11WifiNSideBand_Object((1,3,6,1,4,1,1166,1,19,51,1,5,2,3,1,5),_Cmdot11WifiNSideBand_Type())
cmdot11WifiNSideBand.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11WifiNSideBand.setStatus(_A)
class _Cmdot11WifiNProtection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_S,2)))
_Cmdot11WifiNProtection_Type.__name__=_C
_Cmdot11WifiNProtection_Object=MibTableColumn
cmdot11WifiNProtection=_Cmdot11WifiNProtection_Object((1,3,6,1,4,1,1166,1,19,51,1,5,2,3,1,6),_Cmdot11WifiNProtection_Type())
cmdot11WifiNProtection.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11WifiNProtection.setStatus(_A)
_Cmdot11ApsScanResultsTable_Object=MibTable
cmdot11ApsScanResultsTable=_Cmdot11ApsScanResultsTable_Object((1,3,6,1,4,1,1166,1,19,51,1,5,2,4))
if mibBuilder.loadTexts:cmdot11ApsScanResultsTable.setStatus(_A)
_Cmdot11ApsScanResultsEntry_Object=MibTableRow
cmdot11ApsScanResultsEntry=_Cmdot11ApsScanResultsEntry_Object((1,3,6,1,4,1,1166,1,19,51,1,5,2,4,1))
cmdot11ApsScanResultsEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:cmdot11ApsScanResultsEntry.setStatus(_A)
class _Cmdot11ValidEntry_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('invalid',0),('valid',1)))
_Cmdot11ValidEntry_Type.__name__=_C
_Cmdot11ValidEntry_Object=MibTableColumn
cmdot11ValidEntry=_Cmdot11ValidEntry_Object((1,3,6,1,4,1,1166,1,19,51,1,5,2,4,1,1),_Cmdot11ValidEntry_Type())
cmdot11ValidEntry.setMaxAccess(_F)
if mibBuilder.loadTexts:cmdot11ValidEntry.setStatus(_A)
_Cmdot11NetworkName_Type=OctetString
_Cmdot11NetworkName_Object=MibTableColumn
cmdot11NetworkName=_Cmdot11NetworkName_Object((1,3,6,1,4,1,1166,1,19,51,1,5,2,4,1,2),_Cmdot11NetworkName_Type())
cmdot11NetworkName.setMaxAccess(_F)
if mibBuilder.loadTexts:cmdot11NetworkName.setStatus(_A)
_Cmdot11SecurityMode_Type=OctetString
_Cmdot11SecurityMode_Object=MibTableColumn
cmdot11SecurityMode=_Cmdot11SecurityMode_Object((1,3,6,1,4,1,1166,1,19,51,1,5,2,4,1,3),_Cmdot11SecurityMode_Type())
cmdot11SecurityMode.setMaxAccess(_F)
if mibBuilder.loadTexts:cmdot11SecurityMode.setStatus(_A)
_Cmdot11PhyMode_Type=OctetString
_Cmdot11PhyMode_Object=MibTableColumn
cmdot11PhyMode=_Cmdot11PhyMode_Object((1,3,6,1,4,1,1166,1,19,51,1,5,2,4,1,4),_Cmdot11PhyMode_Type())
cmdot11PhyMode.setMaxAccess(_F)
if mibBuilder.loadTexts:cmdot11PhyMode.setStatus(_A)
_Cmdot11Rssi_Type=Integer32
_Cmdot11Rssi_Object=MibTableColumn
cmdot11Rssi=_Cmdot11Rssi_Object((1,3,6,1,4,1,1166,1,19,51,1,5,2,4,1,5),_Cmdot11Rssi_Type())
cmdot11Rssi.setMaxAccess(_F)
if mibBuilder.loadTexts:cmdot11Rssi.setStatus(_A)
_Cmdot11Channel_Type=Integer32
_Cmdot11Channel_Object=MibTableColumn
cmdot11Channel=_Cmdot11Channel_Object((1,3,6,1,4,1,1166,1,19,51,1,5,2,4,1,6),_Cmdot11Channel_Type())
cmdot11Channel.setMaxAccess(_F)
if mibBuilder.loadTexts:cmdot11Channel.setStatus(_A)
_Cmdot11MacAddress_Type=PhysAddress
_Cmdot11MacAddress_Object=MibTableColumn
cmdot11MacAddress=_Cmdot11MacAddress_Object((1,3,6,1,4,1,1166,1,19,51,1,5,2,4,1,7),_Cmdot11MacAddress_Type())
cmdot11MacAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:cmdot11MacAddress.setStatus(_A)
_Cmdot1180211acInterfaceTable_Object=MibTable
cmdot1180211acInterfaceTable=_Cmdot1180211acInterfaceTable_Object((1,3,6,1,4,1,1166,1,19,51,1,5,2,5))
if mibBuilder.loadTexts:cmdot1180211acInterfaceTable.setStatus(_A)
_Cmdot1180211acInterfaceEntry_Object=MibTableRow
cmdot1180211acInterfaceEntry=_Cmdot1180211acInterfaceEntry_Object((1,3,6,1,4,1,1166,1,19,51,1,5,2,5,1))
cmdot1180211acInterfaceEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:cmdot1180211acInterfaceEntry.setStatus(_A)
class _Cmdot11ACBandWidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('width20MHz',1),('width40MHz',2),('width80MHz',3)))
_Cmdot11ACBandWidth_Type.__name__=_C
_Cmdot11ACBandWidth_Object=MibTableColumn
cmdot11ACBandWidth=_Cmdot11ACBandWidth_Object((1,3,6,1,4,1,1166,1,19,51,1,5,2,5,1,1),_Cmdot11ACBandWidth_Type())
cmdot11ACBandWidth.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11ACBandWidth.setStatus(_A)
class _Cmdot11ACChannelSpec_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_Cmdot11ACChannelSpec_Type.__name__=_K
_Cmdot11ACChannelSpec_Object=MibTableColumn
cmdot11ACChannelSpec=_Cmdot11ACChannelSpec_Object((1,3,6,1,4,1,1166,1,19,51,1,5,2,5,1,2),_Cmdot11ACChannelSpec_Type())
cmdot11ACChannelSpec.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11ACChannelSpec.setStatus(_A)
_Cmdot11ACTxbfBFRCap_Type=TruthValue
_Cmdot11ACTxbfBFRCap_Object=MibTableColumn
cmdot11ACTxbfBFRCap=_Cmdot11ACTxbfBFRCap_Object((1,3,6,1,4,1,1166,1,19,51,1,5,2,5,1,3),_Cmdot11ACTxbfBFRCap_Type())
cmdot11ACTxbfBFRCap.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11ACTxbfBFRCap.setStatus(_A)
_Cmdot11ACTxbfBFECap_Type=TruthValue
_Cmdot11ACTxbfBFECap_Object=MibTableColumn
cmdot11ACTxbfBFECap=_Cmdot11ACTxbfBFECap_Object((1,3,6,1,4,1,1166,1,19,51,1,5,2,5,1,4),_Cmdot11ACTxbfBFECap_Type())
cmdot11ACTxbfBFECap.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11ACTxbfBFECap.setStatus(_A)
_Cmdot11MgmtMbss_ObjectIdentity=ObjectIdentity
cmdot11MgmtMbss=_Cmdot11MgmtMbss_ObjectIdentity((1,3,6,1,4,1,1166,1,19,51,1,5,4))
_Cmdot11MbssBase_ObjectIdentity=ObjectIdentity
cmdot11MbssBase=_Cmdot11MbssBase_ObjectIdentity((1,3,6,1,4,1,1166,1,19,51,1,5,4,1))
_Cmdot11BssTable_Object=MibTable
cmdot11BssTable=_Cmdot11BssTable_Object((1,3,6,1,4,1,1166,1,19,51,1,5,4,1,14))
if mibBuilder.loadTexts:cmdot11BssTable.setStatus(_A)
_Cmdot11BssEntry_Object=MibTableRow
cmdot11BssEntry=_Cmdot11BssEntry_Object((1,3,6,1,4,1,1166,1,19,51,1,5,4,1,14,1))
cmdot11BssEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:cmdot11BssEntry.setStatus(_A)
_Cmdot11BssId_Type=PhysAddress
_Cmdot11BssId_Object=MibTableColumn
cmdot11BssId=_Cmdot11BssId_Object((1,3,6,1,4,1,1166,1,19,51,1,5,4,1,14,1,1),_Cmdot11BssId_Type())
cmdot11BssId.setMaxAccess(_F)
if mibBuilder.loadTexts:cmdot11BssId.setStatus(_A)
_Cmdot11BssEnable_Type=TruthValue
_Cmdot11BssEnable_Object=MibTableColumn
cmdot11BssEnable=_Cmdot11BssEnable_Object((1,3,6,1,4,1,1166,1,19,51,1,5,4,1,14,1,2),_Cmdot11BssEnable_Type())
cmdot11BssEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11BssEnable.setStatus(_A)
class _Cmdot11BssSsid_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Cmdot11BssSsid_Type.__name__=_K
_Cmdot11BssSsid_Object=MibTableColumn
cmdot11BssSsid=_Cmdot11BssSsid_Object((1,3,6,1,4,1,1166,1,19,51,1,5,4,1,14,1,3),_Cmdot11BssSsid_Type())
cmdot11BssSsid.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11BssSsid.setStatus(_A)
class _Cmdot11BssNetworkBridge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('lan',1),('guest',2)))
_Cmdot11BssNetworkBridge_Type.__name__=_C
_Cmdot11BssNetworkBridge_Object=MibTableColumn
cmdot11BssNetworkBridge=_Cmdot11BssNetworkBridge_Object((1,3,6,1,4,1,1166,1,19,51,1,5,4,1,14,1,4),_Cmdot11BssNetworkBridge_Type())
cmdot11BssNetworkBridge.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11BssNetworkBridge.setStatus('obsolete')
class _Cmdot11BssSecurityMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_v,0),('wep',1),('wpaPsk',2),('wpa2Psk',3),('wpaEnterprise',4),('wpa2Enterprise',5),('radiusWep',6),('wpaPsk-wpa2Psk',7),('wpaEnterprise-wpa2Enterprise',8)))
_Cmdot11BssSecurityMode_Type.__name__=_C
_Cmdot11BssSecurityMode_Object=MibTableColumn
cmdot11BssSecurityMode=_Cmdot11BssSecurityMode_Object((1,3,6,1,4,1,1166,1,19,51,1,5,4,1,14,1,5),_Cmdot11BssSecurityMode_Type())
cmdot11BssSecurityMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11BssSecurityMode.setStatus(_A)
_Cmdot11BssClosedNetwork_Type=TruthValue
_Cmdot11BssClosedNetwork_Object=MibTableColumn
cmdot11BssClosedNetwork=_Cmdot11BssClosedNetwork_Object((1,3,6,1,4,1,1166,1,19,51,1,5,4,1,14,1,6),_Cmdot11BssClosedNetwork_Type())
cmdot11BssClosedNetwork.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11BssClosedNetwork.setStatus(_A)
class _Cmdot11BssAccessMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('allowAny',1),('allowList',2),('denyList',3)))
_Cmdot11BssAccessMode_Type.__name__=_C
_Cmdot11BssAccessMode_Object=MibTableColumn
cmdot11BssAccessMode=_Cmdot11BssAccessMode_Object((1,3,6,1,4,1,1166,1,19,51,1,5,4,1,14,1,7),_Cmdot11BssAccessMode_Type())
cmdot11BssAccessMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11BssAccessMode.setStatus(_A)
class _Cmdot11BssMaxAssociationsLimit_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_Cmdot11BssMaxAssociationsLimit_Type.__name__=_J
_Cmdot11BssMaxAssociationsLimit_Object=MibTableColumn
cmdot11BssMaxAssociationsLimit=_Cmdot11BssMaxAssociationsLimit_Object((1,3,6,1,4,1,1166,1,19,51,1,5,4,1,14,1,8),_Cmdot11BssMaxAssociationsLimit_Type())
cmdot11BssMaxAssociationsLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11BssMaxAssociationsLimit.setStatus(_A)
class _Cmdot11BssOpmodeCapRequired_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_Q,0),('erp',1),('ht',2),('vht',3)))
_Cmdot11BssOpmodeCapRequired_Type.__name__=_C
_Cmdot11BssOpmodeCapRequired_Object=MibTableColumn
cmdot11BssOpmodeCapRequired=_Cmdot11BssOpmodeCapRequired_Object((1,3,6,1,4,1,1166,1,19,51,1,5,4,1,14,1,9),_Cmdot11BssOpmodeCapRequired_Type())
cmdot11BssOpmodeCapRequired.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11BssOpmodeCapRequired.setStatus(_A)
_Cmdot11MbssSecurity_ObjectIdentity=ObjectIdentity
cmdot11MbssSecurity=_Cmdot11MbssSecurity_ObjectIdentity((1,3,6,1,4,1,1166,1,19,51,1,5,4,2))
_Cmdot11BssWepTable_Object=MibTable
cmdot11BssWepTable=_Cmdot11BssWepTable_Object((1,3,6,1,4,1,1166,1,19,51,1,5,4,2,1))
if mibBuilder.loadTexts:cmdot11BssWepTable.setStatus(_A)
_Cmdot11BssWepEntry_Object=MibTableRow
cmdot11BssWepEntry=_Cmdot11BssWepEntry_Object((1,3,6,1,4,1,1166,1,19,51,1,5,4,2,1,1))
cmdot11BssWepEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:cmdot11BssWepEntry.setStatus(_A)
_Cmdot11BssWepDefaultKey_Type=Unsigned32
_Cmdot11BssWepDefaultKey_Object=MibTableColumn
cmdot11BssWepDefaultKey=_Cmdot11BssWepDefaultKey_Object((1,3,6,1,4,1,1166,1,19,51,1,5,4,2,1,1,1),_Cmdot11BssWepDefaultKey_Type())
cmdot11BssWepDefaultKey.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11BssWepDefaultKey.setStatus(_A)
class _Cmdot11BssWepEncryptionMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('wep64',1),('wep128',2)))
_Cmdot11BssWepEncryptionMode_Type.__name__=_C
_Cmdot11BssWepEncryptionMode_Object=MibTableColumn
cmdot11BssWepEncryptionMode=_Cmdot11BssWepEncryptionMode_Object((1,3,6,1,4,1,1166,1,19,51,1,5,4,2,1,1,2),_Cmdot11BssWepEncryptionMode_Type())
cmdot11BssWepEncryptionMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11BssWepEncryptionMode.setStatus(_A)
class _Cmdot11BssWepPassPhrase_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Cmdot11BssWepPassPhrase_Type.__name__=_T
_Cmdot11BssWepPassPhrase_Object=MibTableColumn
cmdot11BssWepPassPhrase=_Cmdot11BssWepPassPhrase_Object((1,3,6,1,4,1,1166,1,19,51,1,5,4,2,1,1,3),_Cmdot11BssWepPassPhrase_Type())
cmdot11BssWepPassPhrase.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11BssWepPassPhrase.setStatus(_A)
class _Cmdot11BssWepSharedKeyAuthentication_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('optional',1),('required',2)))
_Cmdot11BssWepSharedKeyAuthentication_Type.__name__=_C
_Cmdot11BssWepSharedKeyAuthentication_Object=MibTableColumn
cmdot11BssWepSharedKeyAuthentication=_Cmdot11BssWepSharedKeyAuthentication_Object((1,3,6,1,4,1,1166,1,19,51,1,5,4,2,1,1,4),_Cmdot11BssWepSharedKeyAuthentication_Type())
cmdot11BssWepSharedKeyAuthentication.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11BssWepSharedKeyAuthentication.setStatus(_A)
_Cmdot11BssWep64BitKeyTable_Object=MibTable
cmdot11BssWep64BitKeyTable=_Cmdot11BssWep64BitKeyTable_Object((1,3,6,1,4,1,1166,1,19,51,1,5,4,2,2))
if mibBuilder.loadTexts:cmdot11BssWep64BitKeyTable.setStatus(_A)
_Cmdot11BssWep64BitKeyEntry_Object=MibTableRow
cmdot11BssWep64BitKeyEntry=_Cmdot11BssWep64BitKeyEntry_Object((1,3,6,1,4,1,1166,1,19,51,1,5,4,2,2,1))
cmdot11BssWep64BitKeyEntry.setIndexNames((0,_H,_I),(0,_E,_w))
if mibBuilder.loadTexts:cmdot11BssWep64BitKeyEntry.setStatus(_A)
class _Cmdot11BssWep64BitKeyIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_Cmdot11BssWep64BitKeyIndex_Type.__name__=_C
_Cmdot11BssWep64BitKeyIndex_Object=MibTableColumn
cmdot11BssWep64BitKeyIndex=_Cmdot11BssWep64BitKeyIndex_Object((1,3,6,1,4,1,1166,1,19,51,1,5,4,2,2,1,1),_Cmdot11BssWep64BitKeyIndex_Type())
cmdot11BssWep64BitKeyIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:cmdot11BssWep64BitKeyIndex.setStatus(_A)
class _Cmdot11BssWep64BitKeyValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(5,5));fixedLength=5
_Cmdot11BssWep64BitKeyValue_Type.__name__=_K
_Cmdot11BssWep64BitKeyValue_Object=MibTableColumn
cmdot11BssWep64BitKeyValue=_Cmdot11BssWep64BitKeyValue_Object((1,3,6,1,4,1,1166,1,19,51,1,5,4,2,2,1,2),_Cmdot11BssWep64BitKeyValue_Type())
cmdot11BssWep64BitKeyValue.setMaxAccess(_G)
if mibBuilder.loadTexts:cmdot11BssWep64BitKeyValue.setStatus(_A)
_Cmdot11BssWep64BitKeyStatus_Type=RowStatus
_Cmdot11BssWep64BitKeyStatus_Object=MibTableColumn
cmdot11BssWep64BitKeyStatus=_Cmdot11BssWep64BitKeyStatus_Object((1,3,6,1,4,1,1166,1,19,51,1,5,4,2,2,1,3),_Cmdot11BssWep64BitKeyStatus_Type())
cmdot11BssWep64BitKeyStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:cmdot11BssWep64BitKeyStatus.setStatus(_A)
_Cmdot11BssWep128BitKeyTable_Object=MibTable
cmdot11BssWep128BitKeyTable=_Cmdot11BssWep128BitKeyTable_Object((1,3,6,1,4,1,1166,1,19,51,1,5,4,2,3))
if mibBuilder.loadTexts:cmdot11BssWep128BitKeyTable.setStatus(_A)
_Cmdot11BssWep128BitKeyEntry_Object=MibTableRow
cmdot11BssWep128BitKeyEntry=_Cmdot11BssWep128BitKeyEntry_Object((1,3,6,1,4,1,1166,1,19,51,1,5,4,2,3,1))
cmdot11BssWep128BitKeyEntry.setIndexNames((0,_H,_I),(0,_E,_x))
if mibBuilder.loadTexts:cmdot11BssWep128BitKeyEntry.setStatus(_A)
class _Cmdot11BssWep128BitKeyIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_Cmdot11BssWep128BitKeyIndex_Type.__name__=_C
_Cmdot11BssWep128BitKeyIndex_Object=MibTableColumn
cmdot11BssWep128BitKeyIndex=_Cmdot11BssWep128BitKeyIndex_Object((1,3,6,1,4,1,1166,1,19,51,1,5,4,2,3,1,1),_Cmdot11BssWep128BitKeyIndex_Type())
cmdot11BssWep128BitKeyIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:cmdot11BssWep128BitKeyIndex.setStatus(_A)
class _Cmdot11BssWep128BitKeyValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(13,13));fixedLength=13
_Cmdot11BssWep128BitKeyValue_Type.__name__=_K
_Cmdot11BssWep128BitKeyValue_Object=MibTableColumn
cmdot11BssWep128BitKeyValue=_Cmdot11BssWep128BitKeyValue_Object((1,3,6,1,4,1,1166,1,19,51,1,5,4,2,3,1,2),_Cmdot11BssWep128BitKeyValue_Type())
cmdot11BssWep128BitKeyValue.setMaxAccess(_G)
if mibBuilder.loadTexts:cmdot11BssWep128BitKeyValue.setStatus(_A)
_Cmdot11BssWep128BitKeyStatus_Type=RowStatus
_Cmdot11BssWep128BitKeyStatus_Object=MibTableColumn
cmdot11BssWep128BitKeyStatus=_Cmdot11BssWep128BitKeyStatus_Object((1,3,6,1,4,1,1166,1,19,51,1,5,4,2,3,1,3),_Cmdot11BssWep128BitKeyStatus_Type())
cmdot11BssWep128BitKeyStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:cmdot11BssWep128BitKeyStatus.setStatus(_A)
_Cmdot11BssWpaTable_Object=MibTable
cmdot11BssWpaTable=_Cmdot11BssWpaTable_Object((1,3,6,1,4,1,1166,1,19,51,1,5,4,2,4))
if mibBuilder.loadTexts:cmdot11BssWpaTable.setStatus(_A)
_Cmdot11BssWpaEntry_Object=MibTableRow
cmdot11BssWpaEntry=_Cmdot11BssWpaEntry_Object((1,3,6,1,4,1,1166,1,19,51,1,5,4,2,4,1))
cmdot11BssWpaEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:cmdot11BssWpaEntry.setStatus(_A)
class _Cmdot11BssWpaAlgorithm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('tkip',1),('aes',2),('tkipPlusAes',3)))
_Cmdot11BssWpaAlgorithm_Type.__name__=_C
_Cmdot11BssWpaAlgorithm_Object=MibTableColumn
cmdot11BssWpaAlgorithm=_Cmdot11BssWpaAlgorithm_Object((1,3,6,1,4,1,1166,1,19,51,1,5,4,2,4,1,1),_Cmdot11BssWpaAlgorithm_Type())
cmdot11BssWpaAlgorithm.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11BssWpaAlgorithm.setStatus(_A)
class _Cmdot11BssWpaPreSharedKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,64))
_Cmdot11BssWpaPreSharedKey_Type.__name__=_K
_Cmdot11BssWpaPreSharedKey_Object=MibTableColumn
cmdot11BssWpaPreSharedKey=_Cmdot11BssWpaPreSharedKey_Object((1,3,6,1,4,1,1166,1,19,51,1,5,4,2,4,1,2),_Cmdot11BssWpaPreSharedKey_Type())
cmdot11BssWpaPreSharedKey.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11BssWpaPreSharedKey.setStatus(_A)
_Cmdot11BssWpaGroupRekeyInterval_Type=Unsigned32
_Cmdot11BssWpaGroupRekeyInterval_Object=MibTableColumn
cmdot11BssWpaGroupRekeyInterval=_Cmdot11BssWpaGroupRekeyInterval_Object((1,3,6,1,4,1,1166,1,19,51,1,5,4,2,4,1,3),_Cmdot11BssWpaGroupRekeyInterval_Type())
cmdot11BssWpaGroupRekeyInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11BssWpaGroupRekeyInterval.setStatus(_A)
if mibBuilder.loadTexts:cmdot11BssWpaGroupRekeyInterval.setUnits(_R)
_Cmdot11BssRadiusTable_Object=MibTable
cmdot11BssRadiusTable=_Cmdot11BssRadiusTable_Object((1,3,6,1,4,1,1166,1,19,51,1,5,4,2,5))
if mibBuilder.loadTexts:cmdot11BssRadiusTable.setStatus(_A)
_Cmdot11BssRadiusEntry_Object=MibTableRow
cmdot11BssRadiusEntry=_Cmdot11BssRadiusEntry_Object((1,3,6,1,4,1,1166,1,19,51,1,5,4,2,5,1))
cmdot11BssRadiusEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:cmdot11BssRadiusEntry.setStatus(_A)
_Cmdot11BssRadiusAddressType_Type=InetAddressType
_Cmdot11BssRadiusAddressType_Object=MibTableColumn
cmdot11BssRadiusAddressType=_Cmdot11BssRadiusAddressType_Object((1,3,6,1,4,1,1166,1,19,51,1,5,4,2,5,1,1),_Cmdot11BssRadiusAddressType_Type())
cmdot11BssRadiusAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11BssRadiusAddressType.setStatus(_A)
_Cmdot11BssRadiusAddress_Type=InetAddress
_Cmdot11BssRadiusAddress_Object=MibTableColumn
cmdot11BssRadiusAddress=_Cmdot11BssRadiusAddress_Object((1,3,6,1,4,1,1166,1,19,51,1,5,4,2,5,1,2),_Cmdot11BssRadiusAddress_Type())
cmdot11BssRadiusAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11BssRadiusAddress.setStatus(_A)
_Cmdot11BssRadiusPort_Type=Unsigned32
_Cmdot11BssRadiusPort_Object=MibTableColumn
cmdot11BssRadiusPort=_Cmdot11BssRadiusPort_Object((1,3,6,1,4,1,1166,1,19,51,1,5,4,2,5,1,3),_Cmdot11BssRadiusPort_Type())
cmdot11BssRadiusPort.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11BssRadiusPort.setStatus(_A)
_Cmdot11BssRadiusKey_Type=DisplayString
_Cmdot11BssRadiusKey_Object=MibTableColumn
cmdot11BssRadiusKey=_Cmdot11BssRadiusKey_Object((1,3,6,1,4,1,1166,1,19,51,1,5,4,2,5,1,4),_Cmdot11BssRadiusKey_Type())
cmdot11BssRadiusKey.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11BssRadiusKey.setStatus(_A)
_Cmdot11BssRadiusReAuthInterval_Type=Unsigned32
_Cmdot11BssRadiusReAuthInterval_Object=MibTableColumn
cmdot11BssRadiusReAuthInterval=_Cmdot11BssRadiusReAuthInterval_Object((1,3,6,1,4,1,1166,1,19,51,1,5,4,2,5,1,5),_Cmdot11BssRadiusReAuthInterval_Type())
cmdot11BssRadiusReAuthInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11BssRadiusReAuthInterval.setStatus(_A)
if mibBuilder.loadTexts:cmdot11BssRadiusReAuthInterval.setUnits(_R)
class _Cmdot11BssWpaPasscode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Cmdot11BssWpaPasscode_Type.__name__=_K
_Cmdot11BssWpaPasscode_Object=MibScalar
cmdot11BssWpaPasscode=_Cmdot11BssWpaPasscode_Object((1,3,6,1,4,1,1166,1,19,51,1,5,4,2,100),_Cmdot11BssWpaPasscode_Type())
cmdot11BssWpaPasscode.setMaxAccess(_F)
if mibBuilder.loadTexts:cmdot11BssWpaPasscode.setStatus(_A)
_Cmdot11MbssAccess_ObjectIdentity=ObjectIdentity
cmdot11MbssAccess=_Cmdot11MbssAccess_ObjectIdentity((1,3,6,1,4,1,1166,1,19,51,1,5,4,3))
_Cmdot11BssAccessTable_Object=MibTable
cmdot11BssAccessTable=_Cmdot11BssAccessTable_Object((1,3,6,1,4,1,1166,1,19,51,1,5,4,3,1))
if mibBuilder.loadTexts:cmdot11BssAccessTable.setStatus(_A)
_Cmdot11BssAccessEntry_Object=MibTableRow
cmdot11BssAccessEntry=_Cmdot11BssAccessEntry_Object((1,3,6,1,4,1,1166,1,19,51,1,5,4,3,1,1))
cmdot11BssAccessEntry.setIndexNames((0,_H,_I),(0,_E,_y))
if mibBuilder.loadTexts:cmdot11BssAccessEntry.setStatus(_A)
class _Cmdot11BssAccessIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_Cmdot11BssAccessIndex_Type.__name__=_C
_Cmdot11BssAccessIndex_Object=MibTableColumn
cmdot11BssAccessIndex=_Cmdot11BssAccessIndex_Object((1,3,6,1,4,1,1166,1,19,51,1,5,4,3,1,1,1),_Cmdot11BssAccessIndex_Type())
cmdot11BssAccessIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:cmdot11BssAccessIndex.setStatus(_A)
_Cmdot11BssAccessStation_Type=PhysAddress
_Cmdot11BssAccessStation_Object=MibTableColumn
cmdot11BssAccessStation=_Cmdot11BssAccessStation_Object((1,3,6,1,4,1,1166,1,19,51,1,5,4,3,1,1,2),_Cmdot11BssAccessStation_Type())
cmdot11BssAccessStation.setMaxAccess(_G)
if mibBuilder.loadTexts:cmdot11BssAccessStation.setStatus(_A)
_Cmdot11BssAccessStatus_Type=RowStatus
_Cmdot11BssAccessStatus_Object=MibTableColumn
cmdot11BssAccessStatus=_Cmdot11BssAccessStatus_Object((1,3,6,1,4,1,1166,1,19,51,1,5,4,3,1,1,3),_Cmdot11BssAccessStatus_Type())
cmdot11BssAccessStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:cmdot11BssAccessStatus.setStatus(_A)
_Cmdot11ApplySettings_Type=TruthValue
_Cmdot11ApplySettings_Object=MibScalar
cmdot11ApplySettings=_Cmdot11ApplySettings_Object((1,3,6,1,4,1,1166,1,19,51,1,5,100),_Cmdot11ApplySettings_Type())
cmdot11ApplySettings.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11ApplySettings.setStatus(_A)
_Cmdot11ResetToDefaults_Type=TruthValue
_Cmdot11ResetToDefaults_Object=MibScalar
cmdot11ResetToDefaults=_Cmdot11ResetToDefaults_Object((1,3,6,1,4,1,1166,1,19,51,1,5,101),_Cmdot11ResetToDefaults_Type())
cmdot11ResetToDefaults.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11ResetToDefaults.setStatus(_A)
_Cmdot11plusWps_ObjectIdentity=ObjectIdentity
cmdot11plusWps=_Cmdot11plusWps_ObjectIdentity((1,3,6,1,4,1,1166,1,19,51,1,6))
_Cmdot11WpsEnable_Type=TruthValue
_Cmdot11WpsEnable_Object=MibScalar
cmdot11WpsEnable=_Cmdot11WpsEnable_Object((1,3,6,1,4,1,1166,1,19,51,1,6,1),_Cmdot11WpsEnable_Type())
cmdot11WpsEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11WpsEnable.setStatus(_A)
class _Cmdot11WpsMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('wpsPBC',1),('wpsPIN',2)))
_Cmdot11WpsMethod_Type.__name__=_C
_Cmdot11WpsMethod_Object=MibScalar
cmdot11WpsMethod=_Cmdot11WpsMethod_Object((1,3,6,1,4,1,1166,1,19,51,1,6,2),_Cmdot11WpsMethod_Type())
cmdot11WpsMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11WpsMethod.setStatus(_A)
_Cmdot11WpsPinNumber_Type=Unsigned32
_Cmdot11WpsPinNumber_Object=MibScalar
cmdot11WpsPinNumber=_Cmdot11WpsPinNumber_Object((1,3,6,1,4,1,1166,1,19,51,1,6,3),_Cmdot11WpsPinNumber_Type())
cmdot11WpsPinNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11WpsPinNumber.setStatus(_A)
_Cmdot11WpsAddClient_Type=TruthValue
_Cmdot11WpsAddClient_Object=MibScalar
cmdot11WpsAddClient=_Cmdot11WpsAddClient_Object((1,3,6,1,4,1,1166,1,19,51,1,6,4),_Cmdot11WpsAddClient_Type())
cmdot11WpsAddClient.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11WpsAddClient.setStatus(_A)
_Cmdot11plusDiag_ObjectIdentity=ObjectIdentity
cmdot11plusDiag=_Cmdot11plusDiag_ObjectIdentity((1,3,6,1,4,1,1166,1,19,51,1,7))
class _Cmdot11WlRevInfo_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,511))
_Cmdot11WlRevInfo_Type.__name__=_K
_Cmdot11WlRevInfo_Object=MibScalar
cmdot11WlRevInfo=_Cmdot11WlRevInfo_Object((1,3,6,1,4,1,1166,1,19,51,1,7,1),_Cmdot11WlRevInfo_Type())
cmdot11WlRevInfo.setMaxAccess(_F)
if mibBuilder.loadTexts:cmdot11WlRevInfo.setStatus(_A)
_Cmdot11plusConnectedClientsTable_Object=MibTable
cmdot11plusConnectedClientsTable=_Cmdot11plusConnectedClientsTable_Object((1,3,6,1,4,1,1166,1,19,51,1,8))
if mibBuilder.loadTexts:cmdot11plusConnectedClientsTable.setStatus(_A)
_Cmdot11plusConnectedClientsEntry_Object=MibTableRow
cmdot11plusConnectedClientsEntry=_Cmdot11plusConnectedClientsEntry_Object((1,3,6,1,4,1,1166,1,19,51,1,8,1))
cmdot11plusConnectedClientsEntry.setIndexNames((0,_E,_z))
if mibBuilder.loadTexts:cmdot11plusConnectedClientsEntry.setStatus(_A)
_Cmdot11plusClientIndex_Type=Integer32
_Cmdot11plusClientIndex_Object=MibTableColumn
cmdot11plusClientIndex=_Cmdot11plusClientIndex_Object((1,3,6,1,4,1,1166,1,19,51,1,8,1,1),_Cmdot11plusClientIndex_Type())
cmdot11plusClientIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:cmdot11plusClientIndex.setStatus(_A)
_Cmdot11plusClientIpAddr_Type=IpAddress
_Cmdot11plusClientIpAddr_Object=MibTableColumn
cmdot11plusClientIpAddr=_Cmdot11plusClientIpAddr_Object((1,3,6,1,4,1,1166,1,19,51,1,8,1,2),_Cmdot11plusClientIpAddr_Type())
cmdot11plusClientIpAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:cmdot11plusClientIpAddr.setStatus(_A)
_Cmdot11plusClientID_Type=MacAddress
_Cmdot11plusClientID_Object=MibTableColumn
cmdot11plusClientID=_Cmdot11plusClientID_Object((1,3,6,1,4,1,1166,1,19,51,1,8,1,3),_Cmdot11plusClientID_Type())
cmdot11plusClientID.setMaxAccess(_F)
if mibBuilder.loadTexts:cmdot11plusClientID.setStatus(_A)
_Cmdot11plusClientHostName_Type=OctetString
_Cmdot11plusClientHostName_Object=MibTableColumn
cmdot11plusClientHostName=_Cmdot11plusClientHostName_Object((1,3,6,1,4,1,1166,1,19,51,1,8,1,4),_Cmdot11plusClientHostName_Type())
cmdot11plusClientHostName.setMaxAccess(_F)
if mibBuilder.loadTexts:cmdot11plusClientHostName.setStatus(_A)
_Cmdot11plusClientAge_Type=Integer32
_Cmdot11plusClientAge_Object=MibTableColumn
cmdot11plusClientAge=_Cmdot11plusClientAge_Object((1,3,6,1,4,1,1166,1,19,51,1,8,1,5),_Cmdot11plusClientAge_Type())
cmdot11plusClientAge.setMaxAccess(_F)
if mibBuilder.loadTexts:cmdot11plusClientAge.setStatus(_A)
class _Cmdot11plusClientMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('a',1),('g',2),('n',3)))
_Cmdot11plusClientMode_Type.__name__=_C
_Cmdot11plusClientMode_Object=MibTableColumn
cmdot11plusClientMode=_Cmdot11plusClientMode_Object((1,3,6,1,4,1,1166,1,19,51,1,8,1,6),_Cmdot11plusClientMode_Type())
cmdot11plusClientMode.setMaxAccess(_F)
if mibBuilder.loadTexts:cmdot11plusClientMode.setStatus(_A)
_Cmdot11plusClientRssi_Type=Integer32
_Cmdot11plusClientRssi_Object=MibTableColumn
cmdot11plusClientRssi=_Cmdot11plusClientRssi_Object((1,3,6,1,4,1,1166,1,19,51,1,8,1,7),_Cmdot11plusClientRssi_Type())
cmdot11plusClientRssi.setMaxAccess(_F)
if mibBuilder.loadTexts:cmdot11plusClientRssi.setStatus(_A)
_Cmdot11plusClientSpeed_Type=Integer32
_Cmdot11plusClientSpeed_Object=MibTableColumn
cmdot11plusClientSpeed=_Cmdot11plusClientSpeed_Object((1,3,6,1,4,1,1166,1,19,51,1,8,1,8),_Cmdot11plusClientSpeed_Type())
cmdot11plusClientSpeed.setMaxAccess(_F)
if mibBuilder.loadTexts:cmdot11plusClientSpeed.setStatus(_A)
_Cmdot11plusClientConnectedSSID_Type=OctetString
_Cmdot11plusClientConnectedSSID_Object=MibTableColumn
cmdot11plusClientConnectedSSID=_Cmdot11plusClientConnectedSSID_Object((1,3,6,1,4,1,1166,1,19,51,1,8,1,9),_Cmdot11plusClientConnectedSSID_Type())
cmdot11plusClientConnectedSSID.setMaxAccess(_F)
if mibBuilder.loadTexts:cmdot11plusClientConnectedSSID.setStatus(_A)
_Cmdot11plusConformance_ObjectIdentity=ObjectIdentity
cmdot11plusConformance=_Cmdot11plusConformance_ObjectIdentity((1,3,6,1,4,1,1166,1,19,51,2))
_Cmdot11plusCompliances_ObjectIdentity=ObjectIdentity
cmdot11plusCompliances=_Cmdot11plusCompliances_ObjectIdentity((1,3,6,1,4,1,1166,1,19,51,2,1))
_Cmdot11plusGroups_ObjectIdentity=ObjectIdentity
cmdot11plusGroups=_Cmdot11plusGroups_ObjectIdentity((1,3,6,1,4,1,1166,1,19,51,2,2))
_Cmdot11wifiHotspotMib_ObjectIdentity=ObjectIdentity
cmdot11wifiHotspotMib=_Cmdot11wifiHotspotMib_ObjectIdentity((1,3,6,1,4,1,1166,1,19,51,3))
_Cmdot11wifiHotspotBase_ObjectIdentity=ObjectIdentity
cmdot11wifiHotspotBase=_Cmdot11wifiHotspotBase_ObjectIdentity((1,3,6,1,4,1,1166,1,19,51,3,1))
_Cmdot11wifiHotspotEnabled_Type=TruthValue
_Cmdot11wifiHotspotEnabled_Object=MibScalar
cmdot11wifiHotspotEnabled=_Cmdot11wifiHotspotEnabled_Object((1,3,6,1,4,1,1166,1,19,51,3,1,1),_Cmdot11wifiHotspotEnabled_Type())
cmdot11wifiHotspotEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11wifiHotspotEnabled.setStatus(_A)
_Cmdot11wifiHotspotTable_Object=MibTable
cmdot11wifiHotspotTable=_Cmdot11wifiHotspotTable_Object((1,3,6,1,4,1,1166,1,19,51,3,1,2))
if mibBuilder.loadTexts:cmdot11wifiHotspotTable.setStatus(_A)
_Cmdot11wifiHotspotIfEntry_Object=MibTableRow
cmdot11wifiHotspotIfEntry=_Cmdot11wifiHotspotIfEntry_Object((1,3,6,1,4,1,1166,1,19,51,3,1,2,1))
cmdot11wifiHotspotIfEntry.setIndexNames((0,_E,_A0))
if mibBuilder.loadTexts:cmdot11wifiHotspotIfEntry.setStatus(_A)
_Cmdot11wifiHotspotInstance_Type=Unsigned32
_Cmdot11wifiHotspotInstance_Object=MibTableColumn
cmdot11wifiHotspotInstance=_Cmdot11wifiHotspotInstance_Object((1,3,6,1,4,1,1166,1,19,51,3,1,2,1,1),_Cmdot11wifiHotspotInstance_Type())
cmdot11wifiHotspotInstance.setMaxAccess(_L)
if mibBuilder.loadTexts:cmdot11wifiHotspotInstance.setStatus(_A)
class _Cmdot11wifiHotspotIf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*(('wifi1-0',1),('wifi1-1',2),('wifi1-2',3),('wifi1-3',4),('wifi1-4',5),('wifi1-5',6),('wifi1-6',7),('wifi1-7',8),('wifi2-0',9),('wifi2-1',10),('wifi2-2',11),('wifi2-3',12),('wifi2-4',13),('wifi2-5',14),('wifi2-6',15),('wifi2-7',16)))
_Cmdot11wifiHotspotIf_Type.__name__=_C
_Cmdot11wifiHotspotIf_Object=MibTableColumn
cmdot11wifiHotspotIf=_Cmdot11wifiHotspotIf_Object((1,3,6,1,4,1,1166,1,19,51,3,1,2,1,2),_Cmdot11wifiHotspotIf_Type())
cmdot11wifiHotspotIf.setMaxAccess(_G)
if mibBuilder.loadTexts:cmdot11wifiHotspotIf.setStatus(_A)
class _Cmdot11wifiHotspotMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_P,1),('enableBridge',2),('enableCmdot11l2ogre',3)))
_Cmdot11wifiHotspotMode_Type.__name__=_C
_Cmdot11wifiHotspotMode_Object=MibTableColumn
cmdot11wifiHotspotMode=_Cmdot11wifiHotspotMode_Object((1,3,6,1,4,1,1166,1,19,51,3,1,2,1,3),_Cmdot11wifiHotspotMode_Type())
cmdot11wifiHotspotMode.setMaxAccess(_G)
if mibBuilder.loadTexts:cmdot11wifiHotspotMode.setStatus(_A)
_Cmdot11wifiHotspotCpeIdleTimeout_Type=Unsigned32
_Cmdot11wifiHotspotCpeIdleTimeout_Object=MibTableColumn
cmdot11wifiHotspotCpeIdleTimeout=_Cmdot11wifiHotspotCpeIdleTimeout_Object((1,3,6,1,4,1,1166,1,19,51,3,1,2,1,4),_Cmdot11wifiHotspotCpeIdleTimeout_Type())
cmdot11wifiHotspotCpeIdleTimeout.setMaxAccess(_G)
if mibBuilder.loadTexts:cmdot11wifiHotspotCpeIdleTimeout.setStatus(_A)
_Cmdot11wifiHotspotCpeSessionTimeout_Type=Unsigned32
_Cmdot11wifiHotspotCpeSessionTimeout_Object=MibTableColumn
cmdot11wifiHotspotCpeSessionTimeout=_Cmdot11wifiHotspotCpeSessionTimeout_Object((1,3,6,1,4,1,1166,1,19,51,3,1,2,1,5),_Cmdot11wifiHotspotCpeSessionTimeout_Type())
cmdot11wifiHotspotCpeSessionTimeout.setMaxAccess(_G)
if mibBuilder.loadTexts:cmdot11wifiHotspotCpeSessionTimeout.setStatus(_A)
_Cmdot11wifiHotspotRadiusAccAddressType_Type=InetAddressType
_Cmdot11wifiHotspotRadiusAccAddressType_Object=MibTableColumn
cmdot11wifiHotspotRadiusAccAddressType=_Cmdot11wifiHotspotRadiusAccAddressType_Object((1,3,6,1,4,1,1166,1,19,51,3,1,2,1,6),_Cmdot11wifiHotspotRadiusAccAddressType_Type())
cmdot11wifiHotspotRadiusAccAddressType.setMaxAccess(_G)
if mibBuilder.loadTexts:cmdot11wifiHotspotRadiusAccAddressType.setStatus(_A)
_Cmdot11wifiHotspotRadiusAccAddress_Type=InetAddress
_Cmdot11wifiHotspotRadiusAccAddress_Object=MibTableColumn
cmdot11wifiHotspotRadiusAccAddress=_Cmdot11wifiHotspotRadiusAccAddress_Object((1,3,6,1,4,1,1166,1,19,51,3,1,2,1,7),_Cmdot11wifiHotspotRadiusAccAddress_Type())
cmdot11wifiHotspotRadiusAccAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:cmdot11wifiHotspotRadiusAccAddress.setStatus(_A)
_Cmdot11wifiHotspotRadiusAccPort_Type=InetPortNumber
_Cmdot11wifiHotspotRadiusAccPort_Object=MibTableColumn
cmdot11wifiHotspotRadiusAccPort=_Cmdot11wifiHotspotRadiusAccPort_Object((1,3,6,1,4,1,1166,1,19,51,3,1,2,1,8),_Cmdot11wifiHotspotRadiusAccPort_Type())
cmdot11wifiHotspotRadiusAccPort.setMaxAccess(_G)
if mibBuilder.loadTexts:cmdot11wifiHotspotRadiusAccPort.setStatus(_A)
_Cmdot11wifiHotspotRadiusAccKey_Type=DisplayString
_Cmdot11wifiHotspotRadiusAccKey_Object=MibTableColumn
cmdot11wifiHotspotRadiusAccKey=_Cmdot11wifiHotspotRadiusAccKey_Object((1,3,6,1,4,1,1166,1,19,51,3,1,2,1,9),_Cmdot11wifiHotspotRadiusAccKey_Type())
cmdot11wifiHotspotRadiusAccKey.setMaxAccess(_G)
if mibBuilder.loadTexts:cmdot11wifiHotspotRadiusAccKey.setStatus(_A)
_Cmdot11wifiHotspotPacketFilterMask_Type=Unsigned32
_Cmdot11wifiHotspotPacketFilterMask_Object=MibTableColumn
cmdot11wifiHotspotPacketFilterMask=_Cmdot11wifiHotspotPacketFilterMask_Object((1,3,6,1,4,1,1166,1,19,51,3,1,2,1,10),_Cmdot11wifiHotspotPacketFilterMask_Type())
cmdot11wifiHotspotPacketFilterMask.setMaxAccess(_G)
if mibBuilder.loadTexts:cmdot11wifiHotspotPacketFilterMask.setStatus(_A)
_Cmdot11wifiHotspotInsertDhcpOptionsMask_Type=Unsigned32
_Cmdot11wifiHotspotInsertDhcpOptionsMask_Object=MibTableColumn
cmdot11wifiHotspotInsertDhcpOptionsMask=_Cmdot11wifiHotspotInsertDhcpOptionsMask_Object((1,3,6,1,4,1,1166,1,19,51,3,1,2,1,11),_Cmdot11wifiHotspotInsertDhcpOptionsMask_Type())
cmdot11wifiHotspotInsertDhcpOptionsMask.setMaxAccess(_G)
if mibBuilder.loadTexts:cmdot11wifiHotspotInsertDhcpOptionsMask.setStatus(_A)
_Cmdot11wifiHotspotRowStatus_Type=RowStatus
_Cmdot11wifiHotspotRowStatus_Object=MibTableColumn
cmdot11wifiHotspotRowStatus=_Cmdot11wifiHotspotRowStatus_Object((1,3,6,1,4,1,1166,1,19,51,3,1,2,1,12),_Cmdot11wifiHotspotRowStatus_Type())
cmdot11wifiHotspotRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:cmdot11wifiHotspotRowStatus.setStatus(_A)
_Cmdot11wifiHotspotAutRateLimit_Type=Unsigned32
_Cmdot11wifiHotspotAutRateLimit_Object=MibScalar
cmdot11wifiHotspotAutRateLimit=_Cmdot11wifiHotspotAutRateLimit_Object((1,3,6,1,4,1,1166,1,19,51,3,1,3),_Cmdot11wifiHotspotAutRateLimit_Type())
cmdot11wifiHotspotAutRateLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11wifiHotspotAutRateLimit.setStatus(_A)
_Cmdot11wifiHotspotAutDenialTimeout_Type=Unsigned32
_Cmdot11wifiHotspotAutDenialTimeout_Object=MibScalar
cmdot11wifiHotspotAutDenialTimeout=_Cmdot11wifiHotspotAutDenialTimeout_Object((1,3,6,1,4,1,1166,1,19,51,3,1,4),_Cmdot11wifiHotspotAutDenialTimeout_Type())
cmdot11wifiHotspotAutDenialTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11wifiHotspotAutDenialTimeout.setStatus(_A)
class _Cmdot11wifiHotspotRadiusOrigIf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('eRouter',1),('cm',2)))
_Cmdot11wifiHotspotRadiusOrigIf_Type.__name__=_C
_Cmdot11wifiHotspotRadiusOrigIf_Object=MibScalar
cmdot11wifiHotspotRadiusOrigIf=_Cmdot11wifiHotspotRadiusOrigIf_Object((1,3,6,1,4,1,1166,1,19,51,3,1,5),_Cmdot11wifiHotspotRadiusOrigIf_Type())
cmdot11wifiHotspotRadiusOrigIf.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11wifiHotspotRadiusOrigIf.setStatus(_A)
_Cmdot11wifiHotspotIgnoreMaxCpeSetting_Type=TruthValue
_Cmdot11wifiHotspotIgnoreMaxCpeSetting_Object=MibScalar
cmdot11wifiHotspotIgnoreMaxCpeSetting=_Cmdot11wifiHotspotIgnoreMaxCpeSetting_Object((1,3,6,1,4,1,1166,1,19,51,3,1,6),_Cmdot11wifiHotspotIgnoreMaxCpeSetting_Type())
cmdot11wifiHotspotIgnoreMaxCpeSetting.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11wifiHotspotIgnoreMaxCpeSetting.setStatus(_A)
_Cmdot11wifiHotspotDisablePMKCaching_Type=TruthValue
_Cmdot11wifiHotspotDisablePMKCaching_Object=MibScalar
cmdot11wifiHotspotDisablePMKCaching=_Cmdot11wifiHotspotDisablePMKCaching_Object((1,3,6,1,4,1,1166,1,19,51,3,1,7),_Cmdot11wifiHotspotDisablePMKCaching_Type())
cmdot11wifiHotspotDisablePMKCaching.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11wifiHotspotDisablePMKCaching.setStatus(_A)
_Cmdot11wifiHotspotConnectionSpeedMin_Type=Unsigned32
_Cmdot11wifiHotspotConnectionSpeedMin_Object=MibScalar
cmdot11wifiHotspotConnectionSpeedMin=_Cmdot11wifiHotspotConnectionSpeedMin_Object((1,3,6,1,4,1,1166,1,19,51,3,1,8),_Cmdot11wifiHotspotConnectionSpeedMin_Type())
cmdot11wifiHotspotConnectionSpeedMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11wifiHotspotConnectionSpeedMin.setStatus(_A)
_Cmdot11wifiHotspotConnectionSpeedTimeout_Type=Unsigned32
_Cmdot11wifiHotspotConnectionSpeedTimeout_Object=MibScalar
cmdot11wifiHotspotConnectionSpeedTimeout=_Cmdot11wifiHotspotConnectionSpeedTimeout_Object((1,3,6,1,4,1,1166,1,19,51,3,1,9),_Cmdot11wifiHotspotConnectionSpeedTimeout_Type())
cmdot11wifiHotspotConnectionSpeedTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11wifiHotspotConnectionSpeedTimeout.setStatus(_A)
_Cmdot11l2ogreMib_ObjectIdentity=ObjectIdentity
cmdot11l2ogreMib=_Cmdot11l2ogreMib_ObjectIdentity((1,3,6,1,4,1,1166,1,19,51,4))
_Cmdot11l2ogreBase_ObjectIdentity=ObjectIdentity
cmdot11l2ogreBase=_Cmdot11l2ogreBase_ObjectIdentity((1,3,6,1,4,1,1166,1,19,51,4,1))
_Cmdot11l2ogreEnabled_Type=TruthValue
_Cmdot11l2ogreEnabled_Object=MibScalar
cmdot11l2ogreEnabled=_Cmdot11l2ogreEnabled_Object((1,3,6,1,4,1,1166,1,19,51,4,1,1),_Cmdot11l2ogreEnabled_Type())
cmdot11l2ogreEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11l2ogreEnabled.setStatus(_A)
class _Cmdot11l2ogrePriRemoteAddressType_Type(InetAddressType):defaultValue=1
_Cmdot11l2ogrePriRemoteAddressType_Type.__name__=_O
_Cmdot11l2ogrePriRemoteAddressType_Object=MibScalar
cmdot11l2ogrePriRemoteAddressType=_Cmdot11l2ogrePriRemoteAddressType_Object((1,3,6,1,4,1,1166,1,19,51,4,1,2),_Cmdot11l2ogrePriRemoteAddressType_Type())
cmdot11l2ogrePriRemoteAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11l2ogrePriRemoteAddressType.setStatus(_A)
_Cmdot11l2ogrePriRemoteAddress_Type=InetAddress
_Cmdot11l2ogrePriRemoteAddress_Object=MibScalar
cmdot11l2ogrePriRemoteAddress=_Cmdot11l2ogrePriRemoteAddress_Object((1,3,6,1,4,1,1166,1,19,51,4,1,3),_Cmdot11l2ogrePriRemoteAddress_Type())
cmdot11l2ogrePriRemoteAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11l2ogrePriRemoteAddress.setStatus(_A)
class _Cmdot11l2ogreSecRemoteAddressType_Type(InetAddressType):defaultValue=1
_Cmdot11l2ogreSecRemoteAddressType_Type.__name__=_O
_Cmdot11l2ogreSecRemoteAddressType_Object=MibScalar
cmdot11l2ogreSecRemoteAddressType=_Cmdot11l2ogreSecRemoteAddressType_Object((1,3,6,1,4,1,1166,1,19,51,4,1,4),_Cmdot11l2ogreSecRemoteAddressType_Type())
cmdot11l2ogreSecRemoteAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11l2ogreSecRemoteAddressType.setStatus(_A)
_Cmdot11l2ogreSecRemoteAddress_Type=InetAddress
_Cmdot11l2ogreSecRemoteAddress_Object=MibScalar
cmdot11l2ogreSecRemoteAddress=_Cmdot11l2ogreSecRemoteAddress_Object((1,3,6,1,4,1,1166,1,19,51,4,1,5),_Cmdot11l2ogreSecRemoteAddress_Type())
cmdot11l2ogreSecRemoteAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11l2ogreSecRemoteAddress.setStatus(_A)
class _Cmdot11l2ogreDSCP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_Cmdot11l2ogreDSCP_Type.__name__=_C
_Cmdot11l2ogreDSCP_Object=MibScalar
cmdot11l2ogreDSCP=_Cmdot11l2ogreDSCP_Object((1,3,6,1,4,1,1166,1,19,51,4,1,6),_Cmdot11l2ogreDSCP_Type())
cmdot11l2ogreDSCP.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11l2ogreDSCP.setStatus(_A)
class _Cmdot11l2ogreKeepAliveMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_v,1),('ping',2),('ping-noswitchover',3)))
_Cmdot11l2ogreKeepAliveMode_Type.__name__=_C
_Cmdot11l2ogreKeepAliveMode_Object=MibScalar
cmdot11l2ogreKeepAliveMode=_Cmdot11l2ogreKeepAliveMode_Object((1,3,6,1,4,1,1166,1,19,51,4,1,7),_Cmdot11l2ogreKeepAliveMode_Type())
cmdot11l2ogreKeepAliveMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11l2ogreKeepAliveMode.setStatus(_A)
_Cmdot11l2ogreKeepAliveCount_Type=Integer32
_Cmdot11l2ogreKeepAliveCount_Object=MibScalar
cmdot11l2ogreKeepAliveCount=_Cmdot11l2ogreKeepAliveCount_Object((1,3,6,1,4,1,1166,1,19,51,4,1,8),_Cmdot11l2ogreKeepAliveCount_Type())
cmdot11l2ogreKeepAliveCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11l2ogreKeepAliveCount.setStatus(_A)
_Cmdot11l2ogreKeepAliveInterval_Type=Integer32
_Cmdot11l2ogreKeepAliveInterval_Object=MibScalar
cmdot11l2ogreKeepAliveInterval=_Cmdot11l2ogreKeepAliveInterval_Object((1,3,6,1,4,1,1166,1,19,51,4,1,9),_Cmdot11l2ogreKeepAliveInterval_Type())
cmdot11l2ogreKeepAliveInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11l2ogreKeepAliveInterval.setStatus(_A)
_Cmdot11l2ogreKeepAliveFailureThreshold_Type=Integer32
_Cmdot11l2ogreKeepAliveFailureThreshold_Object=MibScalar
cmdot11l2ogreKeepAliveFailureThreshold=_Cmdot11l2ogreKeepAliveFailureThreshold_Object((1,3,6,1,4,1,1166,1,19,51,4,1,10),_Cmdot11l2ogreKeepAliveFailureThreshold_Type())
cmdot11l2ogreKeepAliveFailureThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11l2ogreKeepAliveFailureThreshold.setStatus(_A)
_Cmdot11l2ogreStatsTable_Object=MibTable
cmdot11l2ogreStatsTable=_Cmdot11l2ogreStatsTable_Object((1,3,6,1,4,1,1166,1,19,51,4,1,11))
if mibBuilder.loadTexts:cmdot11l2ogreStatsTable.setStatus(_A)
_Cmdot11l2ogreStatsEntry_Object=MibTableRow
cmdot11l2ogreStatsEntry=_Cmdot11l2ogreStatsEntry_Object((1,3,6,1,4,1,1166,1,19,51,4,1,11,1))
cmdot11l2ogreStatsEntry.setIndexNames((0,_E,_A1))
if mibBuilder.loadTexts:cmdot11l2ogreStatsEntry.setStatus(_A)
class _Cmdot11l2ogreStatsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_Cmdot11l2ogreStatsIndex_Type.__name__=_C
_Cmdot11l2ogreStatsIndex_Object=MibTableColumn
cmdot11l2ogreStatsIndex=_Cmdot11l2ogreStatsIndex_Object((1,3,6,1,4,1,1166,1,19,51,4,1,11,1,1),_Cmdot11l2ogreStatsIndex_Type())
cmdot11l2ogreStatsIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:cmdot11l2ogreStatsIndex.setStatus(_A)
_Cmdot11l2ogreStatsBytesSent_Type=Counter64
_Cmdot11l2ogreStatsBytesSent_Object=MibTableColumn
cmdot11l2ogreStatsBytesSent=_Cmdot11l2ogreStatsBytesSent_Object((1,3,6,1,4,1,1166,1,19,51,4,1,11,1,2),_Cmdot11l2ogreStatsBytesSent_Type())
cmdot11l2ogreStatsBytesSent.setMaxAccess(_F)
if mibBuilder.loadTexts:cmdot11l2ogreStatsBytesSent.setStatus(_A)
_Cmdot11l2ogreStatsBytesReceived_Type=Counter64
_Cmdot11l2ogreStatsBytesReceived_Object=MibTableColumn
cmdot11l2ogreStatsBytesReceived=_Cmdot11l2ogreStatsBytesReceived_Object((1,3,6,1,4,1,1166,1,19,51,4,1,11,1,3),_Cmdot11l2ogreStatsBytesReceived_Type())
cmdot11l2ogreStatsBytesReceived.setMaxAccess(_F)
if mibBuilder.loadTexts:cmdot11l2ogreStatsBytesReceived.setStatus(_A)
_Cmdot11l2ogreStatsPacketsSent_Type=Counter64
_Cmdot11l2ogreStatsPacketsSent_Object=MibTableColumn
cmdot11l2ogreStatsPacketsSent=_Cmdot11l2ogreStatsPacketsSent_Object((1,3,6,1,4,1,1166,1,19,51,4,1,11,1,4),_Cmdot11l2ogreStatsPacketsSent_Type())
cmdot11l2ogreStatsPacketsSent.setMaxAccess(_F)
if mibBuilder.loadTexts:cmdot11l2ogreStatsPacketsSent.setStatus(_A)
_Cmdot11l2ogreStatsPacketsReceived_Type=Counter64
_Cmdot11l2ogreStatsPacketsReceived_Object=MibTableColumn
cmdot11l2ogreStatsPacketsReceived=_Cmdot11l2ogreStatsPacketsReceived_Object((1,3,6,1,4,1,1166,1,19,51,4,1,11,1,5),_Cmdot11l2ogreStatsPacketsReceived_Type())
cmdot11l2ogreStatsPacketsReceived.setMaxAccess(_F)
if mibBuilder.loadTexts:cmdot11l2ogreStatsPacketsReceived.setStatus(_A)
_Cmdot11l2ogreStatsDiscardPacketsReceived_Type=Counter64
_Cmdot11l2ogreStatsDiscardPacketsReceived_Object=MibTableColumn
cmdot11l2ogreStatsDiscardPacketsReceived=_Cmdot11l2ogreStatsDiscardPacketsReceived_Object((1,3,6,1,4,1,1166,1,19,51,4,1,11,1,6),_Cmdot11l2ogreStatsDiscardPacketsReceived_Type())
cmdot11l2ogreStatsDiscardPacketsReceived.setMaxAccess(_F)
if mibBuilder.loadTexts:cmdot11l2ogreStatsDiscardPacketsReceived.setStatus(_A)
_Cmdot11l2ogreStatsErrorPacketsReceived_Type=Counter64
_Cmdot11l2ogreStatsErrorPacketsReceived_Object=MibTableColumn
cmdot11l2ogreStatsErrorPacketsReceived=_Cmdot11l2ogreStatsErrorPacketsReceived_Object((1,3,6,1,4,1,1166,1,19,51,4,1,11,1,7),_Cmdot11l2ogreStatsErrorPacketsReceived_Type())
cmdot11l2ogreStatsErrorPacketsReceived.setMaxAccess(_F)
if mibBuilder.loadTexts:cmdot11l2ogreStatsErrorPacketsReceived.setStatus(_A)
_Cmdot11l2ogreStatsKeepAliveSent_Type=Counter64
_Cmdot11l2ogreStatsKeepAliveSent_Object=MibTableColumn
cmdot11l2ogreStatsKeepAliveSent=_Cmdot11l2ogreStatsKeepAliveSent_Object((1,3,6,1,4,1,1166,1,19,51,4,1,11,1,8),_Cmdot11l2ogreStatsKeepAliveSent_Type())
cmdot11l2ogreStatsKeepAliveSent.setMaxAccess(_F)
if mibBuilder.loadTexts:cmdot11l2ogreStatsKeepAliveSent.setStatus(_A)
_Cmdot11l2ogreStatsKeepAliveReceived_Type=Counter64
_Cmdot11l2ogreStatsKeepAliveReceived_Object=MibTableColumn
cmdot11l2ogreStatsKeepAliveReceived=_Cmdot11l2ogreStatsKeepAliveReceived_Object((1,3,6,1,4,1,1166,1,19,51,4,1,11,1,9),_Cmdot11l2ogreStatsKeepAliveReceived_Type())
cmdot11l2ogreStatsKeepAliveReceived.setMaxAccess(_F)
if mibBuilder.loadTexts:cmdot11l2ogreStatsKeepAliveReceived.setStatus(_A)
_Cmdot11l2ogreStatsRowStatus_Type=RowStatus
_Cmdot11l2ogreStatsRowStatus_Object=MibTableColumn
cmdot11l2ogreStatsRowStatus=_Cmdot11l2ogreStatsRowStatus_Object((1,3,6,1,4,1,1166,1,19,51,4,1,11,1,10),_Cmdot11l2ogreStatsRowStatus_Type())
cmdot11l2ogreStatsRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:cmdot11l2ogreStatsRowStatus.setStatus(_A)
_Cmdot11l2ogreSourceIfTable_Object=MibTable
cmdot11l2ogreSourceIfTable=_Cmdot11l2ogreSourceIfTable_Object((1,3,6,1,4,1,1166,1,19,51,4,1,12))
if mibBuilder.loadTexts:cmdot11l2ogreSourceIfTable.setStatus(_A)
_Cmdot11l2ogreSourceIfEntry_Object=MibTableRow
cmdot11l2ogreSourceIfEntry=_Cmdot11l2ogreSourceIfEntry_Object((1,3,6,1,4,1,1166,1,19,51,4,1,12,1))
cmdot11l2ogreSourceIfEntry.setIndexNames((0,_E,_A2))
if mibBuilder.loadTexts:cmdot11l2ogreSourceIfEntry.setStatus(_A)
_Cmdot11l2ogreSourceIfInstance_Type=Unsigned32
_Cmdot11l2ogreSourceIfInstance_Object=MibTableColumn
cmdot11l2ogreSourceIfInstance=_Cmdot11l2ogreSourceIfInstance_Object((1,3,6,1,4,1,1166,1,19,51,4,1,12,1,1),_Cmdot11l2ogreSourceIfInstance_Type())
cmdot11l2ogreSourceIfInstance.setMaxAccess(_L)
if mibBuilder.loadTexts:cmdot11l2ogreSourceIfInstance.setStatus(_A)
class _Cmdot11l2ogreSourceIf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*(('wifi1-0',1),('wifi1-1',2),('wifi1-2',3),('wifi1-3',4),('wifi1-4',5),('wifi1-5',6),('wifi1-6',7),('wifi1-7',8),('wifi2-0',9),('wifi2-1',10),('wifi2-2',11),('wifi2-3',12),('wifi2-4',13),('wifi2-5',14),('wifi2-6',15),('wifi2-7',16)))
_Cmdot11l2ogreSourceIf_Type.__name__=_C
_Cmdot11l2ogreSourceIf_Object=MibTableColumn
cmdot11l2ogreSourceIf=_Cmdot11l2ogreSourceIf_Object((1,3,6,1,4,1,1166,1,19,51,4,1,12,1,2),_Cmdot11l2ogreSourceIf_Type())
cmdot11l2ogreSourceIf.setMaxAccess(_G)
if mibBuilder.loadTexts:cmdot11l2ogreSourceIf.setStatus(_A)
_Cmdot11l2ogreSourceIfEnabled_Type=TruthValue
_Cmdot11l2ogreSourceIfEnabled_Object=MibTableColumn
cmdot11l2ogreSourceIfEnabled=_Cmdot11l2ogreSourceIfEnabled_Object((1,3,6,1,4,1,1166,1,19,51,4,1,12,1,3),_Cmdot11l2ogreSourceIfEnabled_Type())
cmdot11l2ogreSourceIfEnabled.setMaxAccess(_G)
if mibBuilder.loadTexts:cmdot11l2ogreSourceIfEnabled.setStatus(_A)
_Cmdot11l2ogreSourceIfVlanTag_Type=Integer32
_Cmdot11l2ogreSourceIfVlanTag_Object=MibTableColumn
cmdot11l2ogreSourceIfVlanTag=_Cmdot11l2ogreSourceIfVlanTag_Object((1,3,6,1,4,1,1166,1,19,51,4,1,12,1,4),_Cmdot11l2ogreSourceIfVlanTag_Type())
cmdot11l2ogreSourceIfVlanTag.setMaxAccess(_G)
if mibBuilder.loadTexts:cmdot11l2ogreSourceIfVlanTag.setStatus(_A)
_Cmdot11l2ogreSourceIfMplsHeader_Type=Integer32
_Cmdot11l2ogreSourceIfMplsHeader_Object=MibTableColumn
cmdot11l2ogreSourceIfMplsHeader=_Cmdot11l2ogreSourceIfMplsHeader_Object((1,3,6,1,4,1,1166,1,19,51,4,1,12,1,5),_Cmdot11l2ogreSourceIfMplsHeader_Type())
cmdot11l2ogreSourceIfMplsHeader.setMaxAccess(_G)
if mibBuilder.loadTexts:cmdot11l2ogreSourceIfMplsHeader.setStatus(_A)
_Cmdot11l2ogreSourceIfRowStatus_Type=RowStatus
_Cmdot11l2ogreSourceIfRowStatus_Object=MibTableColumn
cmdot11l2ogreSourceIfRowStatus=_Cmdot11l2ogreSourceIfRowStatus_Object((1,3,6,1,4,1,1166,1,19,51,4,1,12,1,6),_Cmdot11l2ogreSourceIfRowStatus_Type())
cmdot11l2ogreSourceIfRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:cmdot11l2ogreSourceIfRowStatus.setStatus(_A)
class _Cmdot11l2ogreOrigIf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('eRouter',1))
_Cmdot11l2ogreOrigIf_Type.__name__=_C
_Cmdot11l2ogreOrigIf_Object=MibScalar
cmdot11l2ogreOrigIf=_Cmdot11l2ogreOrigIf_Object((1,3,6,1,4,1,1166,1,19,51,4,1,13),_Cmdot11l2ogreOrigIf_Type())
cmdot11l2ogreOrigIf.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11l2ogreOrigIf.setStatus(_A)
_Cmdot11l2ogreConcentratorServiceName_Type=DisplayString
_Cmdot11l2ogreConcentratorServiceName_Object=MibScalar
cmdot11l2ogreConcentratorServiceName=_Cmdot11l2ogreConcentratorServiceName_Object((1,3,6,1,4,1,1166,1,19,51,4,1,14),_Cmdot11l2ogreConcentratorServiceName_Type())
cmdot11l2ogreConcentratorServiceName.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11l2ogreConcentratorServiceName.setStatus(_A)
_Cmdot11l2ogreDnsResolverRetryTimerMin_Type=Unsigned32
_Cmdot11l2ogreDnsResolverRetryTimerMin_Object=MibScalar
cmdot11l2ogreDnsResolverRetryTimerMin=_Cmdot11l2ogreDnsResolverRetryTimerMin_Object((1,3,6,1,4,1,1166,1,19,51,4,1,15),_Cmdot11l2ogreDnsResolverRetryTimerMin_Type())
cmdot11l2ogreDnsResolverRetryTimerMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11l2ogreDnsResolverRetryTimerMin.setStatus(_A)
_Cmdot11l2ogreDnsResolverRetryTimerMax_Type=Unsigned32
_Cmdot11l2ogreDnsResolverRetryTimerMax_Object=MibScalar
cmdot11l2ogreDnsResolverRetryTimerMax=_Cmdot11l2ogreDnsResolverRetryTimerMax_Object((1,3,6,1,4,1,1166,1,19,51,4,1,16),_Cmdot11l2ogreDnsResolverRetryTimerMax_Type())
cmdot11l2ogreDnsResolverRetryTimerMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cmdot11l2ogreDnsResolverRetryTimerMax.setStatus(_A)
cmdot11plusBaseGroup=ObjectGroup((1,3,6,1,4,1,1166,1,19,51,2,2,1))
cmdot11plusBaseGroup.setObjects(*((_E,_A3),(_E,_A4),(_E,_A5),(_E,_A6),(_E,_A7),(_E,_A8),(_E,_A9),(_E,_AA),(_E,_AB),(_E,_AC),(_E,_AD),(_E,_AE),(_E,_AF),(_E,_AG)))
if mibBuilder.loadTexts:cmdot11plusBaseGroup.setStatus(_D)
cmdot11BplusGroup=ObjectGroup((1,3,6,1,4,1,1166,1,19,51,2,2,2))
cmdot11BplusGroup.setObjects(*((_E,_AH),(_E,_AI)))
if mibBuilder.loadTexts:cmdot11BplusGroup.setStatus(_D)
cmdot11GplusGroup=ObjectGroup((1,3,6,1,4,1,1166,1,19,51,2,2,3))
cmdot11GplusGroup.setObjects(*((_E,_AJ),(_E,_AK)))
if mibBuilder.loadTexts:cmdot11GplusGroup.setStatus(_D)
cmdot11plusWpaGroup=ObjectGroup((1,3,6,1,4,1,1166,1,19,51,2,2,4))
cmdot11plusWpaGroup.setObjects(*((_E,_AL),(_E,_AM),(_E,_AN),(_E,_AO),(_E,_AP),(_E,_AQ),(_E,_AR)))
if mibBuilder.loadTexts:cmdot11plusWpaGroup.setStatus(_D)
cmdot11plusCompliance=ModuleCompliance((1,3,6,1,4,1,1166,1,19,51,2,1,1))
cmdot11plusCompliance.setObjects((_E,_AS))
if mibBuilder.loadTexts:cmdot11plusCompliance.setStatus(_D)
mibBuilder.exportSymbols(_E,**{'gi':gi,'giproducts':giproducts,'cm':cm,'cmdot11plus':cmdot11plus,'cmdot11plusObjects':cmdot11plusObjects,'cmdot11plusMgmt':cmdot11plusMgmt,'cmdot11plusMgmtObjects':cmdot11plusMgmtObjects,_A5:cmdot11plusWepMode,'cmdot11plusWep128DefaultKeysTable':cmdot11plusWep128DefaultKeysTable,'cmdot11plusWep128DefaultKeysEntry':cmdot11plusWep128DefaultKeysEntry,_W:cmdot11plusWep128Index,_A6:cmdot11plusWep128DefaultKeyValue,_A7:cmdot11plusAclEnable,'cmdot11plusAclTable':cmdot11plusAclTable,'cmdot11plusAclEntry':cmdot11plusAclEntry,_X:cmdot11plusAclIndex,_A8:cmdot11plusAclAddress,_A9:cmdot11plusAclRowStatus,_AA:cmdot11plusSsidBroadcastEnable,_AH:cmdot11plusBasicRates,_AI:cmdot11plusShortPreambleEnable,_AB:cmdot11plusCountersReset,_AJ:cmdot11plusPhyOperatingMode,_AC:cmdot11plusTxOutputPower,_AD:cmdot11plusWepPassPhrase,_AE:cmdot11plusGenerateWepKeys,_AF:cmdot11plusSecurityMode,'cmdot11plusWpaObjects':cmdot11plusWpaObjects,_AL:cmdot11plusWpaAuthMode,_AM:cmdot11plusWpaGroupRekeyInterval,_AK:cmdot11plusWpaEncryptionMode,_AN:cmdot11plusLocalPreSharedKey,_AO:cmdot11plusRemoteRadiusIpType,_AP:cmdot11plusRemoteRadiusIp,_AQ:cmdot11plusRemoteRadiusPort,_AR:cmdot11plusRemoteRadiusKey,'cmdot11plusBaseObjects':cmdot11plusBaseObjects,_A3:cmdot11plusSetToFactory,_A4:cmdot11plusInterfaceEnable,_AG:cmdot11plusApplySettings,'cmdot11plusMgmtv2':cmdot11plusMgmtv2,'cmdot11MgmtBase':cmdot11MgmtBase,'cmdot11OperMode':cmdot11OperMode,'cmdot11CurrentChannel':cmdot11CurrentChannel,'cmdot11ChannelSetting':cmdot11ChannelSetting,'cmdot1154gNetMode':cmdot1154gNetMode,'cmdot11NMode':cmdot11NMode,'cmdot11NPhyRate':cmdot11NPhyRate,'cmdot11NBand':cmdot11NBand,'cmdot11NBandWidth':cmdot11NBandWidth,'cmdot11NSideBand':cmdot11NSideBand,'cmdot11NProtection':cmdot11NProtection,'cmdot11MulticastRate':cmdot11MulticastRate,'cmdot11MgmtInterfaceTables':cmdot11MgmtInterfaceTables,'cmdot11BaseTable':cmdot11BaseTable,'cmdot11BaseEntry':cmdot11BaseEntry,'cmdot11WifiOperMode':cmdot11WifiOperMode,'cmdot11WifiCurrentChannel':cmdot11WifiCurrentChannel,'cmdot11WifiBeaconInterval':cmdot11WifiBeaconInterval,'cmdot11WifiDTIMInterval':cmdot11WifiDTIMInterval,'cmdot11WifiFragThresh':cmdot11WifiFragThresh,'cmdot11WifiRTSThresh':cmdot11WifiRTSThresh,'cmdot11WifiShortRetryLimit':cmdot11WifiShortRetryLimit,'cmdot11WifiLongRetryLimit':cmdot11WifiLongRetryLimit,'cmdot11WifiMulticastRate':cmdot11WifiMulticastRate,'cmdot11WifiOutputPower':cmdot11WifiOutputPower,'cmdot11WifiResetToDefaults':cmdot11WifiResetToDefaults,'cmdot11WifiChannelSetting':cmdot11WifiChannelSetting,'cmdot11WifiApsScan':cmdot11WifiApsScan,'cmdot11WifiObssCoexMode':cmdot11WifiObssCoexMode,'cmdot11WifiAcsdScanTimer':cmdot11WifiAcsdScanTimer,'cmdot11WifiWMFEnable':cmdot11WifiWMFEnable,'cmdot11WifiBSEnable':cmdot11WifiBSEnable,'cmdot11WifiATFEnable':cmdot11WifiATFEnable,'cmdot11WifiTrafficSchedulerEnable':cmdot11WifiTrafficSchedulerEnable,'cmdot11WifiEbosEnable':cmdot11WifiEbosEnable,'cmdot11gTable':cmdot11gTable,'cmdot11gEntry':cmdot11gEntry,'cmdot11Wifi54gNetMode':cmdot11Wifi54gNetMode,'cmdot11Wifi54gProtectionEnable':cmdot11Wifi54gProtectionEnable,'cmdot11Wifi54gBasicRateSet':cmdot11Wifi54gBasicRateSet,'cmdot11nTable':cmdot11nTable,'cmdot11nEntry':cmdot11nEntry,'cmdot11WifiNMode':cmdot11WifiNMode,'cmdot11WifiNPhyRate':cmdot11WifiNPhyRate,'cmdot11WifiNBand':cmdot11WifiNBand,'cmdot11WifiNBandWidth':cmdot11WifiNBandWidth,'cmdot11WifiNSideBand':cmdot11WifiNSideBand,'cmdot11WifiNProtection':cmdot11WifiNProtection,'cmdot11ApsScanResultsTable':cmdot11ApsScanResultsTable,'cmdot11ApsScanResultsEntry':cmdot11ApsScanResultsEntry,'cmdot11ValidEntry':cmdot11ValidEntry,'cmdot11NetworkName':cmdot11NetworkName,'cmdot11SecurityMode':cmdot11SecurityMode,'cmdot11PhyMode':cmdot11PhyMode,'cmdot11Rssi':cmdot11Rssi,'cmdot11Channel':cmdot11Channel,'cmdot11MacAddress':cmdot11MacAddress,'cmdot1180211acInterfaceTable':cmdot1180211acInterfaceTable,'cmdot1180211acInterfaceEntry':cmdot1180211acInterfaceEntry,'cmdot11ACBandWidth':cmdot11ACBandWidth,'cmdot11ACChannelSpec':cmdot11ACChannelSpec,'cmdot11ACTxbfBFRCap':cmdot11ACTxbfBFRCap,'cmdot11ACTxbfBFECap':cmdot11ACTxbfBFECap,'cmdot11MgmtMbss':cmdot11MgmtMbss,'cmdot11MbssBase':cmdot11MbssBase,'cmdot11BssTable':cmdot11BssTable,'cmdot11BssEntry':cmdot11BssEntry,'cmdot11BssId':cmdot11BssId,'cmdot11BssEnable':cmdot11BssEnable,'cmdot11BssSsid':cmdot11BssSsid,'cmdot11BssNetworkBridge':cmdot11BssNetworkBridge,'cmdot11BssSecurityMode':cmdot11BssSecurityMode,'cmdot11BssClosedNetwork':cmdot11BssClosedNetwork,'cmdot11BssAccessMode':cmdot11BssAccessMode,'cmdot11BssMaxAssociationsLimit':cmdot11BssMaxAssociationsLimit,'cmdot11BssOpmodeCapRequired':cmdot11BssOpmodeCapRequired,'cmdot11MbssSecurity':cmdot11MbssSecurity,'cmdot11BssWepTable':cmdot11BssWepTable,'cmdot11BssWepEntry':cmdot11BssWepEntry,'cmdot11BssWepDefaultKey':cmdot11BssWepDefaultKey,'cmdot11BssWepEncryptionMode':cmdot11BssWepEncryptionMode,'cmdot11BssWepPassPhrase':cmdot11BssWepPassPhrase,'cmdot11BssWepSharedKeyAuthentication':cmdot11BssWepSharedKeyAuthentication,'cmdot11BssWep64BitKeyTable':cmdot11BssWep64BitKeyTable,'cmdot11BssWep64BitKeyEntry':cmdot11BssWep64BitKeyEntry,_w:cmdot11BssWep64BitKeyIndex,'cmdot11BssWep64BitKeyValue':cmdot11BssWep64BitKeyValue,'cmdot11BssWep64BitKeyStatus':cmdot11BssWep64BitKeyStatus,'cmdot11BssWep128BitKeyTable':cmdot11BssWep128BitKeyTable,'cmdot11BssWep128BitKeyEntry':cmdot11BssWep128BitKeyEntry,_x:cmdot11BssWep128BitKeyIndex,'cmdot11BssWep128BitKeyValue':cmdot11BssWep128BitKeyValue,'cmdot11BssWep128BitKeyStatus':cmdot11BssWep128BitKeyStatus,'cmdot11BssWpaTable':cmdot11BssWpaTable,'cmdot11BssWpaEntry':cmdot11BssWpaEntry,'cmdot11BssWpaAlgorithm':cmdot11BssWpaAlgorithm,'cmdot11BssWpaPreSharedKey':cmdot11BssWpaPreSharedKey,'cmdot11BssWpaGroupRekeyInterval':cmdot11BssWpaGroupRekeyInterval,'cmdot11BssRadiusTable':cmdot11BssRadiusTable,'cmdot11BssRadiusEntry':cmdot11BssRadiusEntry,'cmdot11BssRadiusAddressType':cmdot11BssRadiusAddressType,'cmdot11BssRadiusAddress':cmdot11BssRadiusAddress,'cmdot11BssRadiusPort':cmdot11BssRadiusPort,'cmdot11BssRadiusKey':cmdot11BssRadiusKey,'cmdot11BssRadiusReAuthInterval':cmdot11BssRadiusReAuthInterval,'cmdot11BssWpaPasscode':cmdot11BssWpaPasscode,'cmdot11MbssAccess':cmdot11MbssAccess,'cmdot11BssAccessTable':cmdot11BssAccessTable,'cmdot11BssAccessEntry':cmdot11BssAccessEntry,_y:cmdot11BssAccessIndex,'cmdot11BssAccessStation':cmdot11BssAccessStation,'cmdot11BssAccessStatus':cmdot11BssAccessStatus,'cmdot11ApplySettings':cmdot11ApplySettings,'cmdot11ResetToDefaults':cmdot11ResetToDefaults,'cmdot11plusWps':cmdot11plusWps,'cmdot11WpsEnable':cmdot11WpsEnable,'cmdot11WpsMethod':cmdot11WpsMethod,'cmdot11WpsPinNumber':cmdot11WpsPinNumber,'cmdot11WpsAddClient':cmdot11WpsAddClient,'cmdot11plusDiag':cmdot11plusDiag,'cmdot11WlRevInfo':cmdot11WlRevInfo,'cmdot11plusConnectedClientsTable':cmdot11plusConnectedClientsTable,'cmdot11plusConnectedClientsEntry':cmdot11plusConnectedClientsEntry,_z:cmdot11plusClientIndex,'cmdot11plusClientIpAddr':cmdot11plusClientIpAddr,'cmdot11plusClientID':cmdot11plusClientID,'cmdot11plusClientHostName':cmdot11plusClientHostName,'cmdot11plusClientAge':cmdot11plusClientAge,'cmdot11plusClientMode':cmdot11plusClientMode,'cmdot11plusClientRssi':cmdot11plusClientRssi,'cmdot11plusClientSpeed':cmdot11plusClientSpeed,'cmdot11plusClientConnectedSSID':cmdot11plusClientConnectedSSID,'cmdot11plusConformance':cmdot11plusConformance,'cmdot11plusCompliances':cmdot11plusCompliances,'cmdot11plusCompliance':cmdot11plusCompliance,'cmdot11plusGroups':cmdot11plusGroups,_AS:cmdot11plusBaseGroup,'cmdot11BplusGroup':cmdot11BplusGroup,'cmdot11GplusGroup':cmdot11GplusGroup,'cmdot11plusWpaGroup':cmdot11plusWpaGroup,'cmdot11wifiHotspotMib':cmdot11wifiHotspotMib,'cmdot11wifiHotspotBase':cmdot11wifiHotspotBase,'cmdot11wifiHotspotEnabled':cmdot11wifiHotspotEnabled,'cmdot11wifiHotspotTable':cmdot11wifiHotspotTable,'cmdot11wifiHotspotIfEntry':cmdot11wifiHotspotIfEntry,'cmdot11wifiHotspotInstance':cmdot11wifiHotspotInstance,_A0:cmdot11wifiHotspotIf,'cmdot11wifiHotspotMode':cmdot11wifiHotspotMode,'cmdot11wifiHotspotCpeIdleTimeout':cmdot11wifiHotspotCpeIdleTimeout,'cmdot11wifiHotspotCpeSessionTimeout':cmdot11wifiHotspotCpeSessionTimeout,'cmdot11wifiHotspotRadiusAccAddressType':cmdot11wifiHotspotRadiusAccAddressType,'cmdot11wifiHotspotRadiusAccAddress':cmdot11wifiHotspotRadiusAccAddress,'cmdot11wifiHotspotRadiusAccPort':cmdot11wifiHotspotRadiusAccPort,'cmdot11wifiHotspotRadiusAccKey':cmdot11wifiHotspotRadiusAccKey,'cmdot11wifiHotspotPacketFilterMask':cmdot11wifiHotspotPacketFilterMask,'cmdot11wifiHotspotInsertDhcpOptionsMask':cmdot11wifiHotspotInsertDhcpOptionsMask,'cmdot11wifiHotspotRowStatus':cmdot11wifiHotspotRowStatus,'cmdot11wifiHotspotAutRateLimit':cmdot11wifiHotspotAutRateLimit,'cmdot11wifiHotspotAutDenialTimeout':cmdot11wifiHotspotAutDenialTimeout,'cmdot11wifiHotspotRadiusOrigIf':cmdot11wifiHotspotRadiusOrigIf,'cmdot11wifiHotspotIgnoreMaxCpeSetting':cmdot11wifiHotspotIgnoreMaxCpeSetting,'cmdot11wifiHotspotDisablePMKCaching':cmdot11wifiHotspotDisablePMKCaching,'cmdot11wifiHotspotConnectionSpeedMin':cmdot11wifiHotspotConnectionSpeedMin,'cmdot11wifiHotspotConnectionSpeedTimeout':cmdot11wifiHotspotConnectionSpeedTimeout,'cmdot11l2ogreMib':cmdot11l2ogreMib,'cmdot11l2ogreBase':cmdot11l2ogreBase,'cmdot11l2ogreEnabled':cmdot11l2ogreEnabled,'cmdot11l2ogrePriRemoteAddressType':cmdot11l2ogrePriRemoteAddressType,'cmdot11l2ogrePriRemoteAddress':cmdot11l2ogrePriRemoteAddress,'cmdot11l2ogreSecRemoteAddressType':cmdot11l2ogreSecRemoteAddressType,'cmdot11l2ogreSecRemoteAddress':cmdot11l2ogreSecRemoteAddress,'cmdot11l2ogreDSCP':cmdot11l2ogreDSCP,'cmdot11l2ogreKeepAliveMode':cmdot11l2ogreKeepAliveMode,'cmdot11l2ogreKeepAliveCount':cmdot11l2ogreKeepAliveCount,'cmdot11l2ogreKeepAliveInterval':cmdot11l2ogreKeepAliveInterval,'cmdot11l2ogreKeepAliveFailureThreshold':cmdot11l2ogreKeepAliveFailureThreshold,'cmdot11l2ogreStatsTable':cmdot11l2ogreStatsTable,'cmdot11l2ogreStatsEntry':cmdot11l2ogreStatsEntry,_A1:cmdot11l2ogreStatsIndex,'cmdot11l2ogreStatsBytesSent':cmdot11l2ogreStatsBytesSent,'cmdot11l2ogreStatsBytesReceived':cmdot11l2ogreStatsBytesReceived,'cmdot11l2ogreStatsPacketsSent':cmdot11l2ogreStatsPacketsSent,'cmdot11l2ogreStatsPacketsReceived':cmdot11l2ogreStatsPacketsReceived,'cmdot11l2ogreStatsDiscardPacketsReceived':cmdot11l2ogreStatsDiscardPacketsReceived,'cmdot11l2ogreStatsErrorPacketsReceived':cmdot11l2ogreStatsErrorPacketsReceived,'cmdot11l2ogreStatsKeepAliveSent':cmdot11l2ogreStatsKeepAliveSent,'cmdot11l2ogreStatsKeepAliveReceived':cmdot11l2ogreStatsKeepAliveReceived,'cmdot11l2ogreStatsRowStatus':cmdot11l2ogreStatsRowStatus,'cmdot11l2ogreSourceIfTable':cmdot11l2ogreSourceIfTable,'cmdot11l2ogreSourceIfEntry':cmdot11l2ogreSourceIfEntry,_A2:cmdot11l2ogreSourceIfInstance,'cmdot11l2ogreSourceIf':cmdot11l2ogreSourceIf,'cmdot11l2ogreSourceIfEnabled':cmdot11l2ogreSourceIfEnabled,'cmdot11l2ogreSourceIfVlanTag':cmdot11l2ogreSourceIfVlanTag,'cmdot11l2ogreSourceIfMplsHeader':cmdot11l2ogreSourceIfMplsHeader,'cmdot11l2ogreSourceIfRowStatus':cmdot11l2ogreSourceIfRowStatus,'cmdot11l2ogreOrigIf':cmdot11l2ogreOrigIf,'cmdot11l2ogreConcentratorServiceName':cmdot11l2ogreConcentratorServiceName,'cmdot11l2ogreDnsResolverRetryTimerMin':cmdot11l2ogreDnsResolverRetryTimerMin,'cmdot11l2ogreDnsResolverRetryTimerMax':cmdot11l2ogreDnsResolverRetryTimerMax})