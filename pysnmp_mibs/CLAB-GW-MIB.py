_Ac='clabGWMAPGroup'
_Ab='clabGWDNSGroup'
_Aa='clabGWGroup'
_AZ='clabGWMAPDomainIfStatsInvV4Pkts'
_AY='clabGWMAPDomainIfStatsUkwnProtoPkt'
_AX='clabGWMAPDomainIfStatsBcastPktRcvd'
_AW='clabGWMAPDomainIfStatsBcastPktSent'
_AV='clabGWMAPDomainIfStatsMcastPktRcvd'
_AU='clabGWMAPDomainIfStatsMcastPktSent'
_AT='clabGWMAPDomainIfStatsDcardPktRcvd'
_AS='clabGWMAPDomainIfStatsDcardPktSent'
_AR='clabGWMAPDomainIfStatsUcastPktRcvd'
_AQ='clabGWMAPDomainIfStatsUcastPktSent'
_AP='clabGWMAPDomainIfStatsErrsRcvd'
_AO='clabGWMAPDomainIfStatsErrorsSent'
_AN='clabGWMAPDomainIfStatsPktRcvd'
_AM='clabGWMAPDomainIfStatsPktSent'
_AL='clabGWMAPDomainIfStatsBytesRcvd'
_AK='clabGWMAPDomainIfStatsBytesSent'
_AJ='clabGWMAPDomainIfRowStatus'
_AI='clabGWMAPDomainIfLowerLayers'
_AH='clabGWMAPDomainIfLastChange'
_AG='clabGWMAPDomainIfName'
_AF='clabGWMAPDomainIfAlias'
_AE='clabGWMAPDomainIfStatus'
_AD='clabGWMAPDomainIfEnable'
_AC='clabGWMAPDomainRuleRowStatus'
_AB='clabGWMAPDomainRulePSID'
_AA='clabGWMAPDomainRulePSIDLength'
_A9='clabGWMAPDomainRulePSIDOffset'
_A8='clabGWMAPDomainRuleIsFMR'
_A7='clabGWMAPDomainRuleEABitsLength'
_A6='clabGWMAPDomainRuleIPv4PrefixLen'
_A5='clabGWMAPDomainRuleIPv4Prefix'
_A4='clabGWMAPDomainRuleIPv6PrefixLen'
_A3='clabGWMAPDomainRuleIPv6Prefix'
_A2='clabGWMAPDomainRuleOrigin'
_A1='clabGWMAPDomainRuleAlias'
_A0='clabGWMAPDomainRuleStatus'
_z='clabGWMAPDomainRuleEnable'
_y='clabGWMAPDomainRowStatus'
_x='clabGWMAPDomainRuleNumEntries'
_w='clabGWMAPDomainIncludeSystemPorts'
_v='clabGWMAPDomainDSCPMarkPolicy'
_u='clabGWMAPDomainBRIPv6PrefixLen'
_t='clabGWMAPDomainBRIPv6Prefix'
_s='clabGWMAPDomainIPv6PrefixLen'
_r='clabGWMAPDomainIPv6Prefix'
_q='clabGWMAPDomainWANInterface'
_p='clabGWMAPDomainTransportMode'
_o='clabGWMAPDomainAlias'
_n='clabGWMAPDomainStatus'
_m='clabGWMAPDomainEnable'
_l='clabGWMAPTunnelDomainNumEntries'
_k='clabGWMAPEnable'
_j='clabGWDeviceDNSIpv6QueryForDualMode'
_i='clabGWDevicePublicAccessEnabled'
_h='clabGWDeviceInfoFirstUseDate'
_g='clabGWDeviceInfoUpTime'
_f='clabGWDeviceInfoProvisioningCode'
_e='clabGWDeviceInfoAdditonalSoftwareVersion'
_d='clabGWDeviceInfoAdditionalHardwareVersion'
_c='clabGWDeviceInfoSoftwareVersion'
_b='clabGWDeviceInfoHardwareVersion'
_a='clabGWDeviceInfoSerialNumber'
_Z='clabGWDeviceInfoProductClass'
_Y='clabGWDeviceInfoDescription'
_X='clabGWDeviceInfoModelNumber'
_W='clabGWDeviceInfoModelName'
_V='clabGWDeviceInfoDeviceCategory'
_U='clabGWDeviceInfoManufacturerOUI'
_T='clabGWDeviceInfoManufacturer'
_S='clabGWMAPDomainRuleIndex'
_R='enabled'
_Q='disabled'
_P='InetAddressIPv4'
_O='error'
_N='not-accessible'
_M='read-write'
_L='clabGWMAPDomainIndex'
_K='InetAddressPrefixLength'
_J='Integer32'
_I='OctetString'
_H='TruthValue'
_G='Unsigned32'
_F='packets'
_E='SnmpAdminString'
_D='read-create'
_C='read-only'
_B='CLAB-GW-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
clabCommonMibs,=mibBuilder.importSymbols('CLAB-DEF-MIB','clabCommonMibs')
InetAddressIPv4,InetAddressIPv6,InetAddressPrefixLength=mibBuilder.importSymbols('INET-ADDRESS-MIB',_P,'InetAddressIPv6',_K)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TextualConvention',_H)
clabGWMib=ModuleIdentity((1,3,6,1,4,1,4491,4,6))
if mibBuilder.loadTexts:clabGWMib.setRevisions(('2016-08-04 00:00','2016-02-24 00:00'))
_ClabGWNotifications_ObjectIdentity=ObjectIdentity
clabGWNotifications=_ClabGWNotifications_ObjectIdentity((1,3,6,1,4,1,4491,4,6,0))
_ClabGWMibObjects_ObjectIdentity=ObjectIdentity
clabGWMibObjects=_ClabGWMibObjects_ObjectIdentity((1,3,6,1,4,1,4491,4,6,1))
_ClabGWDeviceInfoObjects_ObjectIdentity=ObjectIdentity
clabGWDeviceInfoObjects=_ClabGWDeviceInfoObjects_ObjectIdentity((1,3,6,1,4,1,4491,4,6,1,1))
class _ClabGWDeviceInfoManufacturer_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_ClabGWDeviceInfoManufacturer_Type.__name__=_E
_ClabGWDeviceInfoManufacturer_Object=MibScalar
clabGWDeviceInfoManufacturer=_ClabGWDeviceInfoManufacturer_Object((1,3,6,1,4,1,4491,4,6,1,1,1),_ClabGWDeviceInfoManufacturer_Type())
clabGWDeviceInfoManufacturer.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGWDeviceInfoManufacturer.setStatus(_A)
class _ClabGWDeviceInfoManufacturerOUI_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_ClabGWDeviceInfoManufacturerOUI_Type.__name__=_E
_ClabGWDeviceInfoManufacturerOUI_Object=MibScalar
clabGWDeviceInfoManufacturerOUI=_ClabGWDeviceInfoManufacturerOUI_Object((1,3,6,1,4,1,4491,4,6,1,1,2),_ClabGWDeviceInfoManufacturerOUI_Type())
clabGWDeviceInfoManufacturerOUI.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGWDeviceInfoManufacturerOUI.setStatus(_A)
class _ClabGWDeviceInfoDeviceCategory_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(127,127));fixedLength=127
_ClabGWDeviceInfoDeviceCategory_Type.__name__=_E
_ClabGWDeviceInfoDeviceCategory_Object=MibScalar
clabGWDeviceInfoDeviceCategory=_ClabGWDeviceInfoDeviceCategory_Object((1,3,6,1,4,1,4491,4,6,1,1,3),_ClabGWDeviceInfoDeviceCategory_Type())
clabGWDeviceInfoDeviceCategory.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGWDeviceInfoDeviceCategory.setStatus(_A)
class _ClabGWDeviceInfoModelName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_ClabGWDeviceInfoModelName_Type.__name__=_E
_ClabGWDeviceInfoModelName_Object=MibScalar
clabGWDeviceInfoModelName=_ClabGWDeviceInfoModelName_Object((1,3,6,1,4,1,4491,4,6,1,1,4),_ClabGWDeviceInfoModelName_Type())
clabGWDeviceInfoModelName.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGWDeviceInfoModelName.setStatus(_A)
class _ClabGWDeviceInfoModelNumber_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_ClabGWDeviceInfoModelNumber_Type.__name__=_E
_ClabGWDeviceInfoModelNumber_Object=MibScalar
clabGWDeviceInfoModelNumber=_ClabGWDeviceInfoModelNumber_Object((1,3,6,1,4,1,4491,4,6,1,1,5),_ClabGWDeviceInfoModelNumber_Type())
clabGWDeviceInfoModelNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGWDeviceInfoModelNumber.setStatus(_A)
class _ClabGWDeviceInfoDescription_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(255,255));fixedLength=255
_ClabGWDeviceInfoDescription_Type.__name__=_E
_ClabGWDeviceInfoDescription_Object=MibScalar
clabGWDeviceInfoDescription=_ClabGWDeviceInfoDescription_Object((1,3,6,1,4,1,4491,4,6,1,1,6),_ClabGWDeviceInfoDescription_Type())
clabGWDeviceInfoDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGWDeviceInfoDescription.setStatus(_A)
class _ClabGWDeviceInfoProductClass_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_ClabGWDeviceInfoProductClass_Type.__name__=_E
_ClabGWDeviceInfoProductClass_Object=MibScalar
clabGWDeviceInfoProductClass=_ClabGWDeviceInfoProductClass_Object((1,3,6,1,4,1,4491,4,6,1,1,7),_ClabGWDeviceInfoProductClass_Type())
clabGWDeviceInfoProductClass.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGWDeviceInfoProductClass.setStatus(_A)
class _ClabGWDeviceInfoSerialNumber_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_ClabGWDeviceInfoSerialNumber_Type.__name__=_E
_ClabGWDeviceInfoSerialNumber_Object=MibScalar
clabGWDeviceInfoSerialNumber=_ClabGWDeviceInfoSerialNumber_Object((1,3,6,1,4,1,4491,4,6,1,1,8),_ClabGWDeviceInfoSerialNumber_Type())
clabGWDeviceInfoSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGWDeviceInfoSerialNumber.setStatus(_A)
class _ClabGWDeviceInfoHardwareVersion_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_ClabGWDeviceInfoHardwareVersion_Type.__name__=_E
_ClabGWDeviceInfoHardwareVersion_Object=MibScalar
clabGWDeviceInfoHardwareVersion=_ClabGWDeviceInfoHardwareVersion_Object((1,3,6,1,4,1,4491,4,6,1,1,9),_ClabGWDeviceInfoHardwareVersion_Type())
clabGWDeviceInfoHardwareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGWDeviceInfoHardwareVersion.setStatus(_A)
class _ClabGWDeviceInfoSoftwareVersion_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_ClabGWDeviceInfoSoftwareVersion_Type.__name__=_E
_ClabGWDeviceInfoSoftwareVersion_Object=MibScalar
clabGWDeviceInfoSoftwareVersion=_ClabGWDeviceInfoSoftwareVersion_Object((1,3,6,1,4,1,4491,4,6,1,1,10),_ClabGWDeviceInfoSoftwareVersion_Type())
clabGWDeviceInfoSoftwareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGWDeviceInfoSoftwareVersion.setStatus(_A)
class _ClabGWDeviceInfoAdditionalHardwareVersion_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_ClabGWDeviceInfoAdditionalHardwareVersion_Type.__name__=_E
_ClabGWDeviceInfoAdditionalHardwareVersion_Object=MibScalar
clabGWDeviceInfoAdditionalHardwareVersion=_ClabGWDeviceInfoAdditionalHardwareVersion_Object((1,3,6,1,4,1,4491,4,6,1,1,11),_ClabGWDeviceInfoAdditionalHardwareVersion_Type())
clabGWDeviceInfoAdditionalHardwareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGWDeviceInfoAdditionalHardwareVersion.setStatus(_A)
class _ClabGWDeviceInfoAdditonalSoftwareVersion_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_ClabGWDeviceInfoAdditonalSoftwareVersion_Type.__name__=_E
_ClabGWDeviceInfoAdditonalSoftwareVersion_Object=MibScalar
clabGWDeviceInfoAdditonalSoftwareVersion=_ClabGWDeviceInfoAdditonalSoftwareVersion_Object((1,3,6,1,4,1,4491,4,6,1,1,12),_ClabGWDeviceInfoAdditonalSoftwareVersion_Type())
clabGWDeviceInfoAdditonalSoftwareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGWDeviceInfoAdditonalSoftwareVersion.setStatus(_A)
class _ClabGWDeviceInfoProvisioningCode_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_ClabGWDeviceInfoProvisioningCode_Type.__name__=_E
_ClabGWDeviceInfoProvisioningCode_Object=MibScalar
clabGWDeviceInfoProvisioningCode=_ClabGWDeviceInfoProvisioningCode_Object((1,3,6,1,4,1,4491,4,6,1,1,13),_ClabGWDeviceInfoProvisioningCode_Type())
clabGWDeviceInfoProvisioningCode.setMaxAccess(_M)
if mibBuilder.loadTexts:clabGWDeviceInfoProvisioningCode.setStatus(_A)
_ClabGWDeviceInfoUpTime_Type=TimeTicks
_ClabGWDeviceInfoUpTime_Object=MibScalar
clabGWDeviceInfoUpTime=_ClabGWDeviceInfoUpTime_Object((1,3,6,1,4,1,4491,4,6,1,1,14),_ClabGWDeviceInfoUpTime_Type())
clabGWDeviceInfoUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGWDeviceInfoUpTime.setStatus(_A)
_ClabGWDeviceInfoFirstUseDate_Type=DateAndTime
_ClabGWDeviceInfoFirstUseDate_Object=MibScalar
clabGWDeviceInfoFirstUseDate=_ClabGWDeviceInfoFirstUseDate_Object((1,3,6,1,4,1,4491,4,6,1,1,15),_ClabGWDeviceInfoFirstUseDate_Type())
clabGWDeviceInfoFirstUseDate.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGWDeviceInfoFirstUseDate.setStatus(_A)
class _ClabGWDevicePublicAccessEnabled_Type(TruthValue):defaultValue=2
_ClabGWDevicePublicAccessEnabled_Type.__name__=_H
_ClabGWDevicePublicAccessEnabled_Object=MibScalar
clabGWDevicePublicAccessEnabled=_ClabGWDevicePublicAccessEnabled_Object((1,3,6,1,4,1,4491,4,6,1,1,16),_ClabGWDevicePublicAccessEnabled_Type())
clabGWDevicePublicAccessEnabled.setMaxAccess(_M)
if mibBuilder.loadTexts:clabGWDevicePublicAccessEnabled.setStatus(_A)
_ClabGWDNSObjects_ObjectIdentity=ObjectIdentity
clabGWDNSObjects=_ClabGWDNSObjects_ObjectIdentity((1,3,6,1,4,1,4491,4,6,1,2))
class _ClabGWDeviceDNSIpv6QueryForDualMode_Type(TruthValue):defaultValue=2
_ClabGWDeviceDNSIpv6QueryForDualMode_Type.__name__=_H
_ClabGWDeviceDNSIpv6QueryForDualMode_Object=MibScalar
clabGWDeviceDNSIpv6QueryForDualMode=_ClabGWDeviceDNSIpv6QueryForDualMode_Object((1,3,6,1,4,1,4491,4,6,1,2,1),_ClabGWDeviceDNSIpv6QueryForDualMode_Type())
clabGWDeviceDNSIpv6QueryForDualMode.setMaxAccess(_M)
if mibBuilder.loadTexts:clabGWDeviceDNSIpv6QueryForDualMode.setStatus(_A)
_ClabGWMAPObjects_ObjectIdentity=ObjectIdentity
clabGWMAPObjects=_ClabGWMAPObjects_ObjectIdentity((1,3,6,1,4,1,4491,4,6,1,3))
class _ClabGWMAPEnable_Type(TruthValue):defaultValue=2
_ClabGWMAPEnable_Type.__name__=_H
_ClabGWMAPEnable_Object=MibScalar
clabGWMAPEnable=_ClabGWMAPEnable_Object((1,3,6,1,4,1,4491,4,6,1,3,1),_ClabGWMAPEnable_Type())
clabGWMAPEnable.setMaxAccess(_M)
if mibBuilder.loadTexts:clabGWMAPEnable.setStatus(_A)
class _ClabGWMAPTunnelDomainNumEntries_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_ClabGWMAPTunnelDomainNumEntries_Type.__name__=_G
_ClabGWMAPTunnelDomainNumEntries_Object=MibScalar
clabGWMAPTunnelDomainNumEntries=_ClabGWMAPTunnelDomainNumEntries_Object((1,3,6,1,4,1,4491,4,6,1,3,2),_ClabGWMAPTunnelDomainNumEntries_Type())
clabGWMAPTunnelDomainNumEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGWMAPTunnelDomainNumEntries.setStatus(_A)
_ClabGWMAPDomainTable_Object=MibTable
clabGWMAPDomainTable=_ClabGWMAPDomainTable_Object((1,3,6,1,4,1,4491,4,6,1,3,3))
if mibBuilder.loadTexts:clabGWMAPDomainTable.setStatus(_A)
_ClabGWMAPDomainEntry_Object=MibTableRow
clabGWMAPDomainEntry=_ClabGWMAPDomainEntry_Object((1,3,6,1,4,1,4491,4,6,1,3,3,1))
clabGWMAPDomainEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:clabGWMAPDomainEntry.setStatus(_A)
class _ClabGWMAPDomainIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_ClabGWMAPDomainIndex_Type.__name__=_G
_ClabGWMAPDomainIndex_Object=MibTableColumn
clabGWMAPDomainIndex=_ClabGWMAPDomainIndex_Object((1,3,6,1,4,1,4491,4,6,1,3,3,1,1),_ClabGWMAPDomainIndex_Type())
clabGWMAPDomainIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:clabGWMAPDomainIndex.setStatus(_A)
class _ClabGWMAPDomainEnable_Type(TruthValue):defaultValue=2
_ClabGWMAPDomainEnable_Type.__name__=_H
_ClabGWMAPDomainEnable_Object=MibTableColumn
clabGWMAPDomainEnable=_ClabGWMAPDomainEnable_Object((1,3,6,1,4,1,4491,4,6,1,3,3,1,2),_ClabGWMAPDomainEnable_Type())
clabGWMAPDomainEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:clabGWMAPDomainEnable.setStatus(_A)
class _ClabGWMAPDomainStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_Q,1),(_R,2),('errorMisconfigured',3),(_O,4)))
_ClabGWMAPDomainStatus_Type.__name__=_J
_ClabGWMAPDomainStatus_Object=MibTableColumn
clabGWMAPDomainStatus=_ClabGWMAPDomainStatus_Object((1,3,6,1,4,1,4491,4,6,1,3,3,1,3),_ClabGWMAPDomainStatus_Type())
clabGWMAPDomainStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGWMAPDomainStatus.setStatus(_A)
class _ClabGWMAPDomainAlias_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ClabGWMAPDomainAlias_Type.__name__=_I
_ClabGWMAPDomainAlias_Object=MibTableColumn
clabGWMAPDomainAlias=_ClabGWMAPDomainAlias_Object((1,3,6,1,4,1,4491,4,6,1,3,3,1,4),_ClabGWMAPDomainAlias_Type())
clabGWMAPDomainAlias.setMaxAccess(_D)
if mibBuilder.loadTexts:clabGWMAPDomainAlias.setStatus(_A)
class _ClabGWMAPDomainTransportMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('encapsulation',1),('translation',2)))
_ClabGWMAPDomainTransportMode_Type.__name__=_J
_ClabGWMAPDomainTransportMode_Object=MibTableColumn
clabGWMAPDomainTransportMode=_ClabGWMAPDomainTransportMode_Object((1,3,6,1,4,1,4491,4,6,1,3,3,1,5),_ClabGWMAPDomainTransportMode_Type())
clabGWMAPDomainTransportMode.setMaxAccess(_D)
if mibBuilder.loadTexts:clabGWMAPDomainTransportMode.setStatus(_A)
class _ClabGWMAPDomainWANInterface_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_ClabGWMAPDomainWANInterface_Type.__name__=_I
_ClabGWMAPDomainWANInterface_Object=MibTableColumn
clabGWMAPDomainWANInterface=_ClabGWMAPDomainWANInterface_Object((1,3,6,1,4,1,4491,4,6,1,3,3,1,6),_ClabGWMAPDomainWANInterface_Type())
clabGWMAPDomainWANInterface.setMaxAccess(_D)
if mibBuilder.loadTexts:clabGWMAPDomainWANInterface.setStatus(_A)
_ClabGWMAPDomainIPv6Prefix_Type=InetAddressIPv6
_ClabGWMAPDomainIPv6Prefix_Object=MibTableColumn
clabGWMAPDomainIPv6Prefix=_ClabGWMAPDomainIPv6Prefix_Object((1,3,6,1,4,1,4491,4,6,1,3,3,1,7),_ClabGWMAPDomainIPv6Prefix_Type())
clabGWMAPDomainIPv6Prefix.setMaxAccess(_D)
if mibBuilder.loadTexts:clabGWMAPDomainIPv6Prefix.setStatus(_A)
class _ClabGWMAPDomainIPv6PrefixLen_Type(InetAddressPrefixLength):defaultValue=0
_ClabGWMAPDomainIPv6PrefixLen_Type.__name__=_K
_ClabGWMAPDomainIPv6PrefixLen_Object=MibTableColumn
clabGWMAPDomainIPv6PrefixLen=_ClabGWMAPDomainIPv6PrefixLen_Object((1,3,6,1,4,1,4491,4,6,1,3,3,1,8),_ClabGWMAPDomainIPv6PrefixLen_Type())
clabGWMAPDomainIPv6PrefixLen.setMaxAccess(_D)
if mibBuilder.loadTexts:clabGWMAPDomainIPv6PrefixLen.setStatus(_A)
_ClabGWMAPDomainBRIPv6Prefix_Type=InetAddressIPv6
_ClabGWMAPDomainBRIPv6Prefix_Object=MibTableColumn
clabGWMAPDomainBRIPv6Prefix=_ClabGWMAPDomainBRIPv6Prefix_Object((1,3,6,1,4,1,4491,4,6,1,3,3,1,9),_ClabGWMAPDomainBRIPv6Prefix_Type())
clabGWMAPDomainBRIPv6Prefix.setMaxAccess(_D)
if mibBuilder.loadTexts:clabGWMAPDomainBRIPv6Prefix.setStatus(_A)
class _ClabGWMAPDomainBRIPv6PrefixLen_Type(InetAddressPrefixLength):defaultValue=64
_ClabGWMAPDomainBRIPv6PrefixLen_Type.__name__=_K
_ClabGWMAPDomainBRIPv6PrefixLen_Object=MibTableColumn
clabGWMAPDomainBRIPv6PrefixLen=_ClabGWMAPDomainBRIPv6PrefixLen_Object((1,3,6,1,4,1,4491,4,6,1,3,3,1,10),_ClabGWMAPDomainBRIPv6PrefixLen_Type())
clabGWMAPDomainBRIPv6PrefixLen.setMaxAccess(_D)
if mibBuilder.loadTexts:clabGWMAPDomainBRIPv6PrefixLen.setStatus(_A)
class _ClabGWMAPDomainDSCPMarkPolicy_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,63))
_ClabGWMAPDomainDSCPMarkPolicy_Type.__name__=_J
_ClabGWMAPDomainDSCPMarkPolicy_Object=MibTableColumn
clabGWMAPDomainDSCPMarkPolicy=_ClabGWMAPDomainDSCPMarkPolicy_Object((1,3,6,1,4,1,4491,4,6,1,3,3,1,11),_ClabGWMAPDomainDSCPMarkPolicy_Type())
clabGWMAPDomainDSCPMarkPolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:clabGWMAPDomainDSCPMarkPolicy.setStatus(_A)
class _ClabGWMAPDomainIncludeSystemPorts_Type(TruthValue):defaultValue=2
_ClabGWMAPDomainIncludeSystemPorts_Type.__name__=_H
_ClabGWMAPDomainIncludeSystemPorts_Object=MibTableColumn
clabGWMAPDomainIncludeSystemPorts=_ClabGWMAPDomainIncludeSystemPorts_Object((1,3,6,1,4,1,4491,4,6,1,3,3,1,12),_ClabGWMAPDomainIncludeSystemPorts_Type())
clabGWMAPDomainIncludeSystemPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:clabGWMAPDomainIncludeSystemPorts.setStatus(_A)
class _ClabGWMAPDomainRuleNumEntries_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ClabGWMAPDomainRuleNumEntries_Type.__name__=_G
_ClabGWMAPDomainRuleNumEntries_Object=MibTableColumn
clabGWMAPDomainRuleNumEntries=_ClabGWMAPDomainRuleNumEntries_Object((1,3,6,1,4,1,4491,4,6,1,3,3,1,13),_ClabGWMAPDomainRuleNumEntries_Type())
clabGWMAPDomainRuleNumEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGWMAPDomainRuleNumEntries.setStatus(_A)
_ClabGWMAPDomainRowStatus_Type=RowStatus
_ClabGWMAPDomainRowStatus_Object=MibTableColumn
clabGWMAPDomainRowStatus=_ClabGWMAPDomainRowStatus_Object((1,3,6,1,4,1,4491,4,6,1,3,3,1,14),_ClabGWMAPDomainRowStatus_Type())
clabGWMAPDomainRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:clabGWMAPDomainRowStatus.setStatus(_A)
_ClabGWMAPDomainRuleTable_Object=MibTable
clabGWMAPDomainRuleTable=_ClabGWMAPDomainRuleTable_Object((1,3,6,1,4,1,4491,4,6,1,3,4))
if mibBuilder.loadTexts:clabGWMAPDomainRuleTable.setStatus(_A)
_ClabGWMAPDomainRuleEntry_Object=MibTableRow
clabGWMAPDomainRuleEntry=_ClabGWMAPDomainRuleEntry_Object((1,3,6,1,4,1,4491,4,6,1,3,4,1))
clabGWMAPDomainRuleEntry.setIndexNames((0,_B,_L),(0,_B,_S))
if mibBuilder.loadTexts:clabGWMAPDomainRuleEntry.setStatus(_A)
class _ClabGWMAPDomainRuleIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_ClabGWMAPDomainRuleIndex_Type.__name__=_G
_ClabGWMAPDomainRuleIndex_Object=MibTableColumn
clabGWMAPDomainRuleIndex=_ClabGWMAPDomainRuleIndex_Object((1,3,6,1,4,1,4491,4,6,1,3,4,1,1),_ClabGWMAPDomainRuleIndex_Type())
clabGWMAPDomainRuleIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:clabGWMAPDomainRuleIndex.setStatus(_A)
class _ClabGWMAPDomainRuleEnable_Type(TruthValue):defaultValue=2
_ClabGWMAPDomainRuleEnable_Type.__name__=_H
_ClabGWMAPDomainRuleEnable_Object=MibTableColumn
clabGWMAPDomainRuleEnable=_ClabGWMAPDomainRuleEnable_Object((1,3,6,1,4,1,4491,4,6,1,3,4,1,2),_ClabGWMAPDomainRuleEnable_Type())
clabGWMAPDomainRuleEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:clabGWMAPDomainRuleEnable.setStatus(_A)
class _ClabGWMAPDomainRuleStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Q,1),(_R,2),(_O,3)))
_ClabGWMAPDomainRuleStatus_Type.__name__=_J
_ClabGWMAPDomainRuleStatus_Object=MibTableColumn
clabGWMAPDomainRuleStatus=_ClabGWMAPDomainRuleStatus_Object((1,3,6,1,4,1,4491,4,6,1,3,4,1,3),_ClabGWMAPDomainRuleStatus_Type())
clabGWMAPDomainRuleStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGWMAPDomainRuleStatus.setStatus(_A)
class _ClabGWMAPDomainRuleAlias_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ClabGWMAPDomainRuleAlias_Type.__name__=_I
_ClabGWMAPDomainRuleAlias_Object=MibTableColumn
clabGWMAPDomainRuleAlias=_ClabGWMAPDomainRuleAlias_Object((1,3,6,1,4,1,4491,4,6,1,3,4,1,4),_ClabGWMAPDomainRuleAlias_Type())
clabGWMAPDomainRuleAlias.setMaxAccess(_D)
if mibBuilder.loadTexts:clabGWMAPDomainRuleAlias.setStatus(_A)
class _ClabGWMAPDomainRuleOrigin_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dhcpv6',1),('static',2)))
_ClabGWMAPDomainRuleOrigin_Type.__name__=_J
_ClabGWMAPDomainRuleOrigin_Object=MibTableColumn
clabGWMAPDomainRuleOrigin=_ClabGWMAPDomainRuleOrigin_Object((1,3,6,1,4,1,4491,4,6,1,3,4,1,5),_ClabGWMAPDomainRuleOrigin_Type())
clabGWMAPDomainRuleOrigin.setMaxAccess(_D)
if mibBuilder.loadTexts:clabGWMAPDomainRuleOrigin.setStatus(_A)
_ClabGWMAPDomainRuleIPv6Prefix_Type=InetAddressIPv6
_ClabGWMAPDomainRuleIPv6Prefix_Object=MibTableColumn
clabGWMAPDomainRuleIPv6Prefix=_ClabGWMAPDomainRuleIPv6Prefix_Object((1,3,6,1,4,1,4491,4,6,1,3,4,1,6),_ClabGWMAPDomainRuleIPv6Prefix_Type())
clabGWMAPDomainRuleIPv6Prefix.setMaxAccess(_D)
if mibBuilder.loadTexts:clabGWMAPDomainRuleIPv6Prefix.setStatus(_A)
class _ClabGWMAPDomainRuleIPv6PrefixLen_Type(InetAddressPrefixLength):defaultValue=0
_ClabGWMAPDomainRuleIPv6PrefixLen_Type.__name__=_K
_ClabGWMAPDomainRuleIPv6PrefixLen_Object=MibTableColumn
clabGWMAPDomainRuleIPv6PrefixLen=_ClabGWMAPDomainRuleIPv6PrefixLen_Object((1,3,6,1,4,1,4491,4,6,1,3,4,1,7),_ClabGWMAPDomainRuleIPv6PrefixLen_Type())
clabGWMAPDomainRuleIPv6PrefixLen.setMaxAccess(_D)
if mibBuilder.loadTexts:clabGWMAPDomainRuleIPv6PrefixLen.setStatus(_A)
class _ClabGWMAPDomainRuleIPv4Prefix_Type(InetAddressIPv4):defaultHexValue='00000000'
_ClabGWMAPDomainRuleIPv4Prefix_Type.__name__=_P
_ClabGWMAPDomainRuleIPv4Prefix_Object=MibTableColumn
clabGWMAPDomainRuleIPv4Prefix=_ClabGWMAPDomainRuleIPv4Prefix_Object((1,3,6,1,4,1,4491,4,6,1,3,4,1,8),_ClabGWMAPDomainRuleIPv4Prefix_Type())
clabGWMAPDomainRuleIPv4Prefix.setMaxAccess(_D)
if mibBuilder.loadTexts:clabGWMAPDomainRuleIPv4Prefix.setStatus(_A)
class _ClabGWMAPDomainRuleIPv4PrefixLen_Type(InetAddressPrefixLength):defaultValue=0
_ClabGWMAPDomainRuleIPv4PrefixLen_Type.__name__=_K
_ClabGWMAPDomainRuleIPv4PrefixLen_Object=MibTableColumn
clabGWMAPDomainRuleIPv4PrefixLen=_ClabGWMAPDomainRuleIPv4PrefixLen_Object((1,3,6,1,4,1,4491,4,6,1,3,4,1,9),_ClabGWMAPDomainRuleIPv4PrefixLen_Type())
clabGWMAPDomainRuleIPv4PrefixLen.setMaxAccess(_D)
if mibBuilder.loadTexts:clabGWMAPDomainRuleIPv4PrefixLen.setStatus(_A)
class _ClabGWMAPDomainRuleEABitsLength_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,48))
_ClabGWMAPDomainRuleEABitsLength_Type.__name__=_G
_ClabGWMAPDomainRuleEABitsLength_Object=MibTableColumn
clabGWMAPDomainRuleEABitsLength=_ClabGWMAPDomainRuleEABitsLength_Object((1,3,6,1,4,1,4491,4,6,1,3,4,1,10),_ClabGWMAPDomainRuleEABitsLength_Type())
clabGWMAPDomainRuleEABitsLength.setMaxAccess(_D)
if mibBuilder.loadTexts:clabGWMAPDomainRuleEABitsLength.setStatus(_A)
class _ClabGWMAPDomainRuleIsFMR_Type(TruthValue):defaultValue=2
_ClabGWMAPDomainRuleIsFMR_Type.__name__=_H
_ClabGWMAPDomainRuleIsFMR_Object=MibTableColumn
clabGWMAPDomainRuleIsFMR=_ClabGWMAPDomainRuleIsFMR_Object((1,3,6,1,4,1,4491,4,6,1,3,4,1,11),_ClabGWMAPDomainRuleIsFMR_Type())
clabGWMAPDomainRuleIsFMR.setMaxAccess(_D)
if mibBuilder.loadTexts:clabGWMAPDomainRuleIsFMR.setStatus(_A)
class _ClabGWMAPDomainRulePSIDOffset_Type(Unsigned32):defaultValue=6;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_ClabGWMAPDomainRulePSIDOffset_Type.__name__=_G
_ClabGWMAPDomainRulePSIDOffset_Object=MibTableColumn
clabGWMAPDomainRulePSIDOffset=_ClabGWMAPDomainRulePSIDOffset_Object((1,3,6,1,4,1,4491,4,6,1,3,4,1,12),_ClabGWMAPDomainRulePSIDOffset_Type())
clabGWMAPDomainRulePSIDOffset.setMaxAccess(_D)
if mibBuilder.loadTexts:clabGWMAPDomainRulePSIDOffset.setStatus(_A)
class _ClabGWMAPDomainRulePSIDLength_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_ClabGWMAPDomainRulePSIDLength_Type.__name__=_G
_ClabGWMAPDomainRulePSIDLength_Object=MibTableColumn
clabGWMAPDomainRulePSIDLength=_ClabGWMAPDomainRulePSIDLength_Object((1,3,6,1,4,1,4491,4,6,1,3,4,1,13),_ClabGWMAPDomainRulePSIDLength_Type())
clabGWMAPDomainRulePSIDLength.setMaxAccess(_D)
if mibBuilder.loadTexts:clabGWMAPDomainRulePSIDLength.setStatus(_A)
class _ClabGWMAPDomainRulePSID_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ClabGWMAPDomainRulePSID_Type.__name__=_G
_ClabGWMAPDomainRulePSID_Object=MibTableColumn
clabGWMAPDomainRulePSID=_ClabGWMAPDomainRulePSID_Object((1,3,6,1,4,1,4491,4,6,1,3,4,1,14),_ClabGWMAPDomainRulePSID_Type())
clabGWMAPDomainRulePSID.setMaxAccess(_D)
if mibBuilder.loadTexts:clabGWMAPDomainRulePSID.setStatus(_A)
_ClabGWMAPDomainRuleRowStatus_Type=RowStatus
_ClabGWMAPDomainRuleRowStatus_Object=MibTableColumn
clabGWMAPDomainRuleRowStatus=_ClabGWMAPDomainRuleRowStatus_Object((1,3,6,1,4,1,4491,4,6,1,3,4,1,15),_ClabGWMAPDomainRuleRowStatus_Type())
clabGWMAPDomainRuleRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:clabGWMAPDomainRuleRowStatus.setStatus(_A)
_ClabGWMAPDomainIfTable_Object=MibTable
clabGWMAPDomainIfTable=_ClabGWMAPDomainIfTable_Object((1,3,6,1,4,1,4491,4,6,1,3,5))
if mibBuilder.loadTexts:clabGWMAPDomainIfTable.setStatus(_A)
_ClabGWMAPDomainIfEntry_Object=MibTableRow
clabGWMAPDomainIfEntry=_ClabGWMAPDomainIfEntry_Object((1,3,6,1,4,1,4491,4,6,1,3,5,1))
clabGWMAPDomainIfEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:clabGWMAPDomainIfEntry.setStatus(_A)
class _ClabGWMAPDomainIfIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_ClabGWMAPDomainIfIndex_Type.__name__=_G
_ClabGWMAPDomainIfIndex_Object=MibTableColumn
clabGWMAPDomainIfIndex=_ClabGWMAPDomainIfIndex_Object((1,3,6,1,4,1,4491,4,6,1,3,5,1,1),_ClabGWMAPDomainIfIndex_Type())
clabGWMAPDomainIfIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:clabGWMAPDomainIfIndex.setStatus(_A)
class _ClabGWMAPDomainIfEnable_Type(TruthValue):defaultValue=2
_ClabGWMAPDomainIfEnable_Type.__name__=_H
_ClabGWMAPDomainIfEnable_Object=MibTableColumn
clabGWMAPDomainIfEnable=_ClabGWMAPDomainIfEnable_Object((1,3,6,1,4,1,4491,4,6,1,3,5,1,2),_ClabGWMAPDomainIfEnable_Type())
clabGWMAPDomainIfEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:clabGWMAPDomainIfEnable.setStatus(_A)
class _ClabGWMAPDomainIfStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('up',1),('down',2),('unknown',3),('dormant',4),('notPresent',5),('lowerLayerDown',6),(_O,7)))
_ClabGWMAPDomainIfStatus_Type.__name__=_J
_ClabGWMAPDomainIfStatus_Object=MibTableColumn
clabGWMAPDomainIfStatus=_ClabGWMAPDomainIfStatus_Object((1,3,6,1,4,1,4491,4,6,1,3,5,1,3),_ClabGWMAPDomainIfStatus_Type())
clabGWMAPDomainIfStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGWMAPDomainIfStatus.setStatus(_A)
class _ClabGWMAPDomainIfAlias_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ClabGWMAPDomainIfAlias_Type.__name__=_I
_ClabGWMAPDomainIfAlias_Object=MibTableColumn
clabGWMAPDomainIfAlias=_ClabGWMAPDomainIfAlias_Object((1,3,6,1,4,1,4491,4,6,1,3,5,1,4),_ClabGWMAPDomainIfAlias_Type())
clabGWMAPDomainIfAlias.setMaxAccess(_D)
if mibBuilder.loadTexts:clabGWMAPDomainIfAlias.setStatus(_A)
class _ClabGWMAPDomainIfName_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ClabGWMAPDomainIfName_Type.__name__=_I
_ClabGWMAPDomainIfName_Object=MibTableColumn
clabGWMAPDomainIfName=_ClabGWMAPDomainIfName_Object((1,3,6,1,4,1,4491,4,6,1,3,5,1,5),_ClabGWMAPDomainIfName_Type())
clabGWMAPDomainIfName.setMaxAccess(_D)
if mibBuilder.loadTexts:clabGWMAPDomainIfName.setStatus(_A)
_ClabGWMAPDomainIfLastChange_Type=Unsigned32
_ClabGWMAPDomainIfLastChange_Object=MibTableColumn
clabGWMAPDomainIfLastChange=_ClabGWMAPDomainIfLastChange_Object((1,3,6,1,4,1,4491,4,6,1,3,5,1,6),_ClabGWMAPDomainIfLastChange_Type())
clabGWMAPDomainIfLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGWMAPDomainIfLastChange.setStatus(_A)
if mibBuilder.loadTexts:clabGWMAPDomainIfLastChange.setUnits('seconds')
class _ClabGWMAPDomainIfLowerLayers_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_ClabGWMAPDomainIfLowerLayers_Type.__name__=_I
_ClabGWMAPDomainIfLowerLayers_Object=MibTableColumn
clabGWMAPDomainIfLowerLayers=_ClabGWMAPDomainIfLowerLayers_Object((1,3,6,1,4,1,4491,4,6,1,3,5,1,7),_ClabGWMAPDomainIfLowerLayers_Type())
clabGWMAPDomainIfLowerLayers.setMaxAccess(_D)
if mibBuilder.loadTexts:clabGWMAPDomainIfLowerLayers.setStatus(_A)
_ClabGWMAPDomainIfRowStatus_Type=RowStatus
_ClabGWMAPDomainIfRowStatus_Object=MibTableColumn
clabGWMAPDomainIfRowStatus=_ClabGWMAPDomainIfRowStatus_Object((1,3,6,1,4,1,4491,4,6,1,3,5,1,8),_ClabGWMAPDomainIfRowStatus_Type())
clabGWMAPDomainIfRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:clabGWMAPDomainIfRowStatus.setStatus(_A)
_ClabGWMAPDomainIfStatsTable_Object=MibTable
clabGWMAPDomainIfStatsTable=_ClabGWMAPDomainIfStatsTable_Object((1,3,6,1,4,1,4491,4,6,1,3,6))
if mibBuilder.loadTexts:clabGWMAPDomainIfStatsTable.setStatus(_A)
_ClabGWMAPDomainIfStatsEntry_Object=MibTableRow
clabGWMAPDomainIfStatsEntry=_ClabGWMAPDomainIfStatsEntry_Object((1,3,6,1,4,1,4491,4,6,1,3,6,1))
clabGWMAPDomainIfStatsEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:clabGWMAPDomainIfStatsEntry.setStatus(_A)
_ClabGWMAPDomainIfStatsBytesSent_Type=Counter64
_ClabGWMAPDomainIfStatsBytesSent_Object=MibTableColumn
clabGWMAPDomainIfStatsBytesSent=_ClabGWMAPDomainIfStatsBytesSent_Object((1,3,6,1,4,1,4491,4,6,1,3,6,1,1),_ClabGWMAPDomainIfStatsBytesSent_Type())
clabGWMAPDomainIfStatsBytesSent.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGWMAPDomainIfStatsBytesSent.setStatus(_A)
if mibBuilder.loadTexts:clabGWMAPDomainIfStatsBytesSent.setUnits('bytes')
_ClabGWMAPDomainIfStatsBytesRcvd_Type=Counter64
_ClabGWMAPDomainIfStatsBytesRcvd_Object=MibTableColumn
clabGWMAPDomainIfStatsBytesRcvd=_ClabGWMAPDomainIfStatsBytesRcvd_Object((1,3,6,1,4,1,4491,4,6,1,3,6,1,2),_ClabGWMAPDomainIfStatsBytesRcvd_Type())
clabGWMAPDomainIfStatsBytesRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGWMAPDomainIfStatsBytesRcvd.setStatus(_A)
if mibBuilder.loadTexts:clabGWMAPDomainIfStatsBytesRcvd.setUnits('bytes')
_ClabGWMAPDomainIfStatsPktSent_Type=Counter64
_ClabGWMAPDomainIfStatsPktSent_Object=MibTableColumn
clabGWMAPDomainIfStatsPktSent=_ClabGWMAPDomainIfStatsPktSent_Object((1,3,6,1,4,1,4491,4,6,1,3,6,1,3),_ClabGWMAPDomainIfStatsPktSent_Type())
clabGWMAPDomainIfStatsPktSent.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGWMAPDomainIfStatsPktSent.setStatus(_A)
if mibBuilder.loadTexts:clabGWMAPDomainIfStatsPktSent.setUnits(_F)
_ClabGWMAPDomainIfStatsPktRcvd_Type=Counter64
_ClabGWMAPDomainIfStatsPktRcvd_Object=MibTableColumn
clabGWMAPDomainIfStatsPktRcvd=_ClabGWMAPDomainIfStatsPktRcvd_Object((1,3,6,1,4,1,4491,4,6,1,3,6,1,4),_ClabGWMAPDomainIfStatsPktRcvd_Type())
clabGWMAPDomainIfStatsPktRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGWMAPDomainIfStatsPktRcvd.setStatus(_A)
if mibBuilder.loadTexts:clabGWMAPDomainIfStatsPktRcvd.setUnits(_F)
_ClabGWMAPDomainIfStatsErrorsSent_Type=Counter64
_ClabGWMAPDomainIfStatsErrorsSent_Object=MibTableColumn
clabGWMAPDomainIfStatsErrorsSent=_ClabGWMAPDomainIfStatsErrorsSent_Object((1,3,6,1,4,1,4491,4,6,1,3,6,1,5),_ClabGWMAPDomainIfStatsErrorsSent_Type())
clabGWMAPDomainIfStatsErrorsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGWMAPDomainIfStatsErrorsSent.setStatus(_A)
if mibBuilder.loadTexts:clabGWMAPDomainIfStatsErrorsSent.setUnits(_F)
_ClabGWMAPDomainIfStatsErrsRcvd_Type=Counter64
_ClabGWMAPDomainIfStatsErrsRcvd_Object=MibTableColumn
clabGWMAPDomainIfStatsErrsRcvd=_ClabGWMAPDomainIfStatsErrsRcvd_Object((1,3,6,1,4,1,4491,4,6,1,3,6,1,6),_ClabGWMAPDomainIfStatsErrsRcvd_Type())
clabGWMAPDomainIfStatsErrsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGWMAPDomainIfStatsErrsRcvd.setStatus(_A)
if mibBuilder.loadTexts:clabGWMAPDomainIfStatsErrsRcvd.setUnits(_F)
_ClabGWMAPDomainIfStatsUcastPktSent_Type=Counter64
_ClabGWMAPDomainIfStatsUcastPktSent_Object=MibTableColumn
clabGWMAPDomainIfStatsUcastPktSent=_ClabGWMAPDomainIfStatsUcastPktSent_Object((1,3,6,1,4,1,4491,4,6,1,3,6,1,7),_ClabGWMAPDomainIfStatsUcastPktSent_Type())
clabGWMAPDomainIfStatsUcastPktSent.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGWMAPDomainIfStatsUcastPktSent.setStatus(_A)
if mibBuilder.loadTexts:clabGWMAPDomainIfStatsUcastPktSent.setUnits(_F)
_ClabGWMAPDomainIfStatsUcastPktRcvd_Type=Counter64
_ClabGWMAPDomainIfStatsUcastPktRcvd_Object=MibTableColumn
clabGWMAPDomainIfStatsUcastPktRcvd=_ClabGWMAPDomainIfStatsUcastPktRcvd_Object((1,3,6,1,4,1,4491,4,6,1,3,6,1,8),_ClabGWMAPDomainIfStatsUcastPktRcvd_Type())
clabGWMAPDomainIfStatsUcastPktRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGWMAPDomainIfStatsUcastPktRcvd.setStatus(_A)
if mibBuilder.loadTexts:clabGWMAPDomainIfStatsUcastPktRcvd.setUnits(_F)
_ClabGWMAPDomainIfStatsDcardPktSent_Type=Counter64
_ClabGWMAPDomainIfStatsDcardPktSent_Object=MibTableColumn
clabGWMAPDomainIfStatsDcardPktSent=_ClabGWMAPDomainIfStatsDcardPktSent_Object((1,3,6,1,4,1,4491,4,6,1,3,6,1,9),_ClabGWMAPDomainIfStatsDcardPktSent_Type())
clabGWMAPDomainIfStatsDcardPktSent.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGWMAPDomainIfStatsDcardPktSent.setStatus(_A)
if mibBuilder.loadTexts:clabGWMAPDomainIfStatsDcardPktSent.setUnits(_F)
_ClabGWMAPDomainIfStatsDcardPktRcvd_Type=Counter64
_ClabGWMAPDomainIfStatsDcardPktRcvd_Object=MibTableColumn
clabGWMAPDomainIfStatsDcardPktRcvd=_ClabGWMAPDomainIfStatsDcardPktRcvd_Object((1,3,6,1,4,1,4491,4,6,1,3,6,1,10),_ClabGWMAPDomainIfStatsDcardPktRcvd_Type())
clabGWMAPDomainIfStatsDcardPktRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGWMAPDomainIfStatsDcardPktRcvd.setStatus(_A)
if mibBuilder.loadTexts:clabGWMAPDomainIfStatsDcardPktRcvd.setUnits(_F)
_ClabGWMAPDomainIfStatsMcastPktSent_Type=Counter64
_ClabGWMAPDomainIfStatsMcastPktSent_Object=MibTableColumn
clabGWMAPDomainIfStatsMcastPktSent=_ClabGWMAPDomainIfStatsMcastPktSent_Object((1,3,6,1,4,1,4491,4,6,1,3,6,1,11),_ClabGWMAPDomainIfStatsMcastPktSent_Type())
clabGWMAPDomainIfStatsMcastPktSent.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGWMAPDomainIfStatsMcastPktSent.setStatus(_A)
if mibBuilder.loadTexts:clabGWMAPDomainIfStatsMcastPktSent.setUnits(_F)
_ClabGWMAPDomainIfStatsMcastPktRcvd_Type=Counter64
_ClabGWMAPDomainIfStatsMcastPktRcvd_Object=MibTableColumn
clabGWMAPDomainIfStatsMcastPktRcvd=_ClabGWMAPDomainIfStatsMcastPktRcvd_Object((1,3,6,1,4,1,4491,4,6,1,3,6,1,12),_ClabGWMAPDomainIfStatsMcastPktRcvd_Type())
clabGWMAPDomainIfStatsMcastPktRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGWMAPDomainIfStatsMcastPktRcvd.setStatus(_A)
if mibBuilder.loadTexts:clabGWMAPDomainIfStatsMcastPktRcvd.setUnits(_F)
_ClabGWMAPDomainIfStatsBcastPktSent_Type=Counter64
_ClabGWMAPDomainIfStatsBcastPktSent_Object=MibTableColumn
clabGWMAPDomainIfStatsBcastPktSent=_ClabGWMAPDomainIfStatsBcastPktSent_Object((1,3,6,1,4,1,4491,4,6,1,3,6,1,13),_ClabGWMAPDomainIfStatsBcastPktSent_Type())
clabGWMAPDomainIfStatsBcastPktSent.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGWMAPDomainIfStatsBcastPktSent.setStatus(_A)
if mibBuilder.loadTexts:clabGWMAPDomainIfStatsBcastPktSent.setUnits(_F)
_ClabGWMAPDomainIfStatsBcastPktRcvd_Type=Counter64
_ClabGWMAPDomainIfStatsBcastPktRcvd_Object=MibTableColumn
clabGWMAPDomainIfStatsBcastPktRcvd=_ClabGWMAPDomainIfStatsBcastPktRcvd_Object((1,3,6,1,4,1,4491,4,6,1,3,6,1,14),_ClabGWMAPDomainIfStatsBcastPktRcvd_Type())
clabGWMAPDomainIfStatsBcastPktRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGWMAPDomainIfStatsBcastPktRcvd.setStatus(_A)
if mibBuilder.loadTexts:clabGWMAPDomainIfStatsBcastPktRcvd.setUnits(_F)
_ClabGWMAPDomainIfStatsUkwnProtoPkt_Type=Counter64
_ClabGWMAPDomainIfStatsUkwnProtoPkt_Object=MibTableColumn
clabGWMAPDomainIfStatsUkwnProtoPkt=_ClabGWMAPDomainIfStatsUkwnProtoPkt_Object((1,3,6,1,4,1,4491,4,6,1,3,6,1,15),_ClabGWMAPDomainIfStatsUkwnProtoPkt_Type())
clabGWMAPDomainIfStatsUkwnProtoPkt.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGWMAPDomainIfStatsUkwnProtoPkt.setStatus(_A)
if mibBuilder.loadTexts:clabGWMAPDomainIfStatsUkwnProtoPkt.setUnits(_F)
_ClabGWMAPDomainIfStatsInvV4Pkts_Type=Counter64
_ClabGWMAPDomainIfStatsInvV4Pkts_Object=MibTableColumn
clabGWMAPDomainIfStatsInvV4Pkts=_ClabGWMAPDomainIfStatsInvV4Pkts_Object((1,3,6,1,4,1,4491,4,6,1,3,6,1,16),_ClabGWMAPDomainIfStatsInvV4Pkts_Type())
clabGWMAPDomainIfStatsInvV4Pkts.setMaxAccess(_C)
if mibBuilder.loadTexts:clabGWMAPDomainIfStatsInvV4Pkts.setStatus(_A)
if mibBuilder.loadTexts:clabGWMAPDomainIfStatsInvV4Pkts.setUnits(_F)
_ClabGWMibConformance_ObjectIdentity=ObjectIdentity
clabGWMibConformance=_ClabGWMibConformance_ObjectIdentity((1,3,6,1,4,1,4491,4,6,2))
_ClabGWMibCompliances_ObjectIdentity=ObjectIdentity
clabGWMibCompliances=_ClabGWMibCompliances_ObjectIdentity((1,3,6,1,4,1,4491,4,6,2,1))
_ClabGWMibGroups_ObjectIdentity=ObjectIdentity
clabGWMibGroups=_ClabGWMibGroups_ObjectIdentity((1,3,6,1,4,1,4491,4,6,2,2))
clabGWGroup=ObjectGroup((1,3,6,1,4,1,4491,4,6,2,2,1))
clabGWGroup.setObjects(*((_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i)))
if mibBuilder.loadTexts:clabGWGroup.setStatus(_A)
clabGWDNSGroup=ObjectGroup((1,3,6,1,4,1,4491,4,6,2,2,3))
clabGWDNSGroup.setObjects((_B,_j))
if mibBuilder.loadTexts:clabGWDNSGroup.setStatus(_A)
clabGWMAPGroup=ObjectGroup((1,3,6,1,4,1,4491,4,6,2,2,4))
clabGWMAPGroup.setObjects(*((_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ)))
if mibBuilder.loadTexts:clabGWMAPGroup.setStatus(_A)
clabGWCompliance=ModuleCompliance((1,3,6,1,4,1,4491,4,6,2,1,1))
clabGWCompliance.setObjects(*((_B,_Aa),(_B,_Ab),(_B,_Ac)))
if mibBuilder.loadTexts:clabGWCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'clabGWMib':clabGWMib,'clabGWNotifications':clabGWNotifications,'clabGWMibObjects':clabGWMibObjects,'clabGWDeviceInfoObjects':clabGWDeviceInfoObjects,_T:clabGWDeviceInfoManufacturer,_U:clabGWDeviceInfoManufacturerOUI,_V:clabGWDeviceInfoDeviceCategory,_W:clabGWDeviceInfoModelName,_X:clabGWDeviceInfoModelNumber,_Y:clabGWDeviceInfoDescription,_Z:clabGWDeviceInfoProductClass,_a:clabGWDeviceInfoSerialNumber,_b:clabGWDeviceInfoHardwareVersion,_c:clabGWDeviceInfoSoftwareVersion,_d:clabGWDeviceInfoAdditionalHardwareVersion,_e:clabGWDeviceInfoAdditonalSoftwareVersion,_f:clabGWDeviceInfoProvisioningCode,_g:clabGWDeviceInfoUpTime,_h:clabGWDeviceInfoFirstUseDate,_i:clabGWDevicePublicAccessEnabled,'clabGWDNSObjects':clabGWDNSObjects,_j:clabGWDeviceDNSIpv6QueryForDualMode,'clabGWMAPObjects':clabGWMAPObjects,_k:clabGWMAPEnable,_l:clabGWMAPTunnelDomainNumEntries,'clabGWMAPDomainTable':clabGWMAPDomainTable,'clabGWMAPDomainEntry':clabGWMAPDomainEntry,_L:clabGWMAPDomainIndex,_m:clabGWMAPDomainEnable,_n:clabGWMAPDomainStatus,_o:clabGWMAPDomainAlias,_p:clabGWMAPDomainTransportMode,_q:clabGWMAPDomainWANInterface,_r:clabGWMAPDomainIPv6Prefix,_s:clabGWMAPDomainIPv6PrefixLen,_t:clabGWMAPDomainBRIPv6Prefix,_u:clabGWMAPDomainBRIPv6PrefixLen,_v:clabGWMAPDomainDSCPMarkPolicy,_w:clabGWMAPDomainIncludeSystemPorts,_x:clabGWMAPDomainRuleNumEntries,_y:clabGWMAPDomainRowStatus,'clabGWMAPDomainRuleTable':clabGWMAPDomainRuleTable,'clabGWMAPDomainRuleEntry':clabGWMAPDomainRuleEntry,_S:clabGWMAPDomainRuleIndex,_z:clabGWMAPDomainRuleEnable,_A0:clabGWMAPDomainRuleStatus,_A1:clabGWMAPDomainRuleAlias,_A2:clabGWMAPDomainRuleOrigin,_A3:clabGWMAPDomainRuleIPv6Prefix,_A4:clabGWMAPDomainRuleIPv6PrefixLen,_A5:clabGWMAPDomainRuleIPv4Prefix,_A6:clabGWMAPDomainRuleIPv4PrefixLen,_A7:clabGWMAPDomainRuleEABitsLength,_A8:clabGWMAPDomainRuleIsFMR,_A9:clabGWMAPDomainRulePSIDOffset,_AA:clabGWMAPDomainRulePSIDLength,_AB:clabGWMAPDomainRulePSID,_AC:clabGWMAPDomainRuleRowStatus,'clabGWMAPDomainIfTable':clabGWMAPDomainIfTable,'clabGWMAPDomainIfEntry':clabGWMAPDomainIfEntry,'clabGWMAPDomainIfIndex':clabGWMAPDomainIfIndex,_AD:clabGWMAPDomainIfEnable,_AE:clabGWMAPDomainIfStatus,_AF:clabGWMAPDomainIfAlias,_AG:clabGWMAPDomainIfName,_AH:clabGWMAPDomainIfLastChange,_AI:clabGWMAPDomainIfLowerLayers,_AJ:clabGWMAPDomainIfRowStatus,'clabGWMAPDomainIfStatsTable':clabGWMAPDomainIfStatsTable,'clabGWMAPDomainIfStatsEntry':clabGWMAPDomainIfStatsEntry,_AK:clabGWMAPDomainIfStatsBytesSent,_AL:clabGWMAPDomainIfStatsBytesRcvd,_AM:clabGWMAPDomainIfStatsPktSent,_AN:clabGWMAPDomainIfStatsPktRcvd,_AO:clabGWMAPDomainIfStatsErrorsSent,_AP:clabGWMAPDomainIfStatsErrsRcvd,_AQ:clabGWMAPDomainIfStatsUcastPktSent,_AR:clabGWMAPDomainIfStatsUcastPktRcvd,_AS:clabGWMAPDomainIfStatsDcardPktSent,_AT:clabGWMAPDomainIfStatsDcardPktRcvd,_AU:clabGWMAPDomainIfStatsMcastPktSent,_AV:clabGWMAPDomainIfStatsMcastPktRcvd,_AW:clabGWMAPDomainIfStatsBcastPktSent,_AX:clabGWMAPDomainIfStatsBcastPktRcvd,_AY:clabGWMAPDomainIfStatsUkwnProtoPkt,_AZ:clabGWMAPDomainIfStatsInvV4Pkts,'clabGWMibConformance':clabGWMibConformance,'clabGWMibCompliances':clabGWMibCompliances,'clabGWCompliance':clabGWCompliance,'clabGWMibGroups':clabGWMibGroups,_Aa:clabGWGroup,_Ab:clabGWDNSGroup,_Ac:clabGWMAPGroup})