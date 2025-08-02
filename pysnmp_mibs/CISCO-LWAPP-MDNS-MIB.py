_A1='cLMdnsServiceGroup'
_A0='cLMdnsMonitorGroup'
_z='cLMdnsConfigGroup'
_y='cLMdnsServiceGroupRuleRowStatus'
_x='cLMdnsRuleUserId'
_w='cLMdnsRuleRole'
_v='cLMdnsServiceGroupDeviceMacRowStatus'
_u='cLMdnsServiceGroupLocationType'
_t='cLMdnsServiceGroupLocationName'
_s='cLMdnsServiceGroupDeviceName'
_r='cLMdnsServiceGroupRowStatus'
_q='cLMdnsServiceGroupDescription'
_p='clMdnsDomainEntryTimeLeft'
_o='clMdnsDomainEntryTtl'
_n='clMdnsDomainType'
_m='clMdnsDomainVlan'
_l='clMdnsDomainIpAddress'
_k='clMdnsDomainIpAddressType'
_j='clMdnsDomainMacAddress'
_i='clMdnsServiceProviderTimeLeft'
_h='clMdnsServiceProviderTtl'
_g='clMdnsServiceProviderType'
_f='clMdnsServiceProviderVlan'
_e='clMdnsServiceProviderName'
_d='clMdnsServiceProviderMacAddress'
_c='clMdnsProfileInterfaceGrpCount'
_b='clMdnsProfileInterfaceCount'
_a='clMdnsProfileWlanCount'
_Z='clMdnsProfileServiceRowStatus'
_Y='clMdnsProfileRowStatus'
_X='clMdnsServiceRowStatus'
_W='clMdnsServiceQueryStatus'
_V='clMdnsServiceString'
_U='clMdnsQueryInterval'
_T='clMdnsSnoopingEnabled'
_S='cLMdnsRuleName'
_R='cLMdnsServiceGroupDeviceMac'
_Q='clMdnsDomainName'
_P='wireless'
_O='clMdnsServiceProviderIndex'
_N='read-write'
_M='Unsigned32'
_L='clMdnsProfileName'
_K='TruthValue'
_J='cLMdnsServiceGroupName'
_I='seconds'
_H='clMdnsServiceName'
_G='Integer32'
_F='not-accessible'
_E='OctetString'
_D='read-create'
_C='read-only'
_B='CISCO-LWAPP-MDNS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_M,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_K)
ciscoLwappMdnsMIB=ModuleIdentity((1,3,6,1,4,1,9,9,842))
if mibBuilder.loadTexts:ciscoLwappMdnsMIB.setRevisions(('2017-04-27 00:00',))
_CiscoLwappMdnsMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoLwappMdnsMIBNotifs=_CiscoLwappMdnsMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,842,0))
_CiscoLwappMdnsMIBObjects_ObjectIdentity=ObjectIdentity
ciscoLwappMdnsMIBObjects=_CiscoLwappMdnsMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,842,1))
_ClMdnsConfigObjects_ObjectIdentity=ObjectIdentity
clMdnsConfigObjects=_ClMdnsConfigObjects_ObjectIdentity((1,3,6,1,4,1,9,9,842,1,1))
_ClMdnsGlobalConfig_ObjectIdentity=ObjectIdentity
clMdnsGlobalConfig=_ClMdnsGlobalConfig_ObjectIdentity((1,3,6,1,4,1,9,9,842,1,1,1))
class _ClMdnsSnoopingEnabled_Type(TruthValue):defaultValue=2
_ClMdnsSnoopingEnabled_Type.__name__=_K
_ClMdnsSnoopingEnabled_Object=MibScalar
clMdnsSnoopingEnabled=_ClMdnsSnoopingEnabled_Object((1,3,6,1,4,1,9,9,842,1,1,1,1),_ClMdnsSnoopingEnabled_Type())
clMdnsSnoopingEnabled.setMaxAccess(_N)
if mibBuilder.loadTexts:clMdnsSnoopingEnabled.setStatus(_A)
class _ClMdnsQueryInterval_Type(Unsigned32):defaultValue=15
_ClMdnsQueryInterval_Type.__name__=_M
_ClMdnsQueryInterval_Object=MibScalar
clMdnsQueryInterval=_ClMdnsQueryInterval_Object((1,3,6,1,4,1,9,9,842,1,1,1,2),_ClMdnsQueryInterval_Type())
clMdnsQueryInterval.setMaxAccess(_N)
if mibBuilder.loadTexts:clMdnsQueryInterval.setStatus(_A)
if mibBuilder.loadTexts:clMdnsQueryInterval.setUnits('minutes')
_ClMdnsMasterServiceTable_Object=MibTable
clMdnsMasterServiceTable=_ClMdnsMasterServiceTable_Object((1,3,6,1,4,1,9,9,842,1,1,2))
if mibBuilder.loadTexts:clMdnsMasterServiceTable.setStatus(_A)
_ClMdnsMasterServiceEntry_Object=MibTableRow
clMdnsMasterServiceEntry=_ClMdnsMasterServiceEntry_Object((1,3,6,1,4,1,9,9,842,1,1,2,1))
clMdnsMasterServiceEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:clMdnsMasterServiceEntry.setStatus(_A)
_ClMdnsServiceName_Type=SnmpAdminString
_ClMdnsServiceName_Object=MibTableColumn
clMdnsServiceName=_ClMdnsServiceName_Object((1,3,6,1,4,1,9,9,842,1,1,2,1,1),_ClMdnsServiceName_Type())
clMdnsServiceName.setMaxAccess(_F)
if mibBuilder.loadTexts:clMdnsServiceName.setStatus(_A)
_ClMdnsServiceString_Type=SnmpAdminString
_ClMdnsServiceString_Object=MibTableColumn
clMdnsServiceString=_ClMdnsServiceString_Object((1,3,6,1,4,1,9,9,842,1,1,2,1,2),_ClMdnsServiceString_Type())
clMdnsServiceString.setMaxAccess(_D)
if mibBuilder.loadTexts:clMdnsServiceString.setStatus(_A)
class _ClMdnsServiceQueryStatus_Type(TruthValue):defaultValue=2
_ClMdnsServiceQueryStatus_Type.__name__=_K
_ClMdnsServiceQueryStatus_Object=MibTableColumn
clMdnsServiceQueryStatus=_ClMdnsServiceQueryStatus_Object((1,3,6,1,4,1,9,9,842,1,1,2,1,3),_ClMdnsServiceQueryStatus_Type())
clMdnsServiceQueryStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:clMdnsServiceQueryStatus.setStatus(_A)
_ClMdnsServiceRowStatus_Type=RowStatus
_ClMdnsServiceRowStatus_Object=MibTableColumn
clMdnsServiceRowStatus=_ClMdnsServiceRowStatus_Object((1,3,6,1,4,1,9,9,842,1,1,2,1,4),_ClMdnsServiceRowStatus_Type())
clMdnsServiceRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:clMdnsServiceRowStatus.setStatus(_A)
_ClMdnsProfileTable_Object=MibTable
clMdnsProfileTable=_ClMdnsProfileTable_Object((1,3,6,1,4,1,9,9,842,1,1,3))
if mibBuilder.loadTexts:clMdnsProfileTable.setStatus(_A)
_ClMdnsProfileEntry_Object=MibTableRow
clMdnsProfileEntry=_ClMdnsProfileEntry_Object((1,3,6,1,4,1,9,9,842,1,1,3,1))
clMdnsProfileEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:clMdnsProfileEntry.setStatus(_A)
_ClMdnsProfileName_Type=SnmpAdminString
_ClMdnsProfileName_Object=MibTableColumn
clMdnsProfileName=_ClMdnsProfileName_Object((1,3,6,1,4,1,9,9,842,1,1,3,1,1),_ClMdnsProfileName_Type())
clMdnsProfileName.setMaxAccess(_F)
if mibBuilder.loadTexts:clMdnsProfileName.setStatus(_A)
_ClMdnsProfileRowStatus_Type=RowStatus
_ClMdnsProfileRowStatus_Object=MibTableColumn
clMdnsProfileRowStatus=_ClMdnsProfileRowStatus_Object((1,3,6,1,4,1,9,9,842,1,1,3,1,2),_ClMdnsProfileRowStatus_Type())
clMdnsProfileRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:clMdnsProfileRowStatus.setStatus(_A)
_ClMdnsProfileWlanCount_Type=Unsigned32
_ClMdnsProfileWlanCount_Object=MibTableColumn
clMdnsProfileWlanCount=_ClMdnsProfileWlanCount_Object((1,3,6,1,4,1,9,9,842,1,1,3,1,3),_ClMdnsProfileWlanCount_Type())
clMdnsProfileWlanCount.setMaxAccess(_C)
if mibBuilder.loadTexts:clMdnsProfileWlanCount.setStatus(_A)
_ClMdnsProfileInterfaceCount_Type=Unsigned32
_ClMdnsProfileInterfaceCount_Object=MibTableColumn
clMdnsProfileInterfaceCount=_ClMdnsProfileInterfaceCount_Object((1,3,6,1,4,1,9,9,842,1,1,3,1,4),_ClMdnsProfileInterfaceCount_Type())
clMdnsProfileInterfaceCount.setMaxAccess(_C)
if mibBuilder.loadTexts:clMdnsProfileInterfaceCount.setStatus(_A)
_ClMdnsProfileInterfaceGrpCount_Type=Unsigned32
_ClMdnsProfileInterfaceGrpCount_Object=MibTableColumn
clMdnsProfileInterfaceGrpCount=_ClMdnsProfileInterfaceGrpCount_Object((1,3,6,1,4,1,9,9,842,1,1,3,1,5),_ClMdnsProfileInterfaceGrpCount_Type())
clMdnsProfileInterfaceGrpCount.setMaxAccess(_C)
if mibBuilder.loadTexts:clMdnsProfileInterfaceGrpCount.setStatus(_A)
_ClMdnsProfileServiceTable_Object=MibTable
clMdnsProfileServiceTable=_ClMdnsProfileServiceTable_Object((1,3,6,1,4,1,9,9,842,1,1,4))
if mibBuilder.loadTexts:clMdnsProfileServiceTable.setStatus(_A)
_ClMdnsProfileServiceEntry_Object=MibTableRow
clMdnsProfileServiceEntry=_ClMdnsProfileServiceEntry_Object((1,3,6,1,4,1,9,9,842,1,1,4,1))
clMdnsProfileServiceEntry.setIndexNames((0,_B,_L),(0,_B,_H))
if mibBuilder.loadTexts:clMdnsProfileServiceEntry.setStatus(_A)
_ClMdnsProfileServiceRowStatus_Type=RowStatus
_ClMdnsProfileServiceRowStatus_Object=MibTableColumn
clMdnsProfileServiceRowStatus=_ClMdnsProfileServiceRowStatus_Object((1,3,6,1,4,1,9,9,842,1,1,4,1,1),_ClMdnsProfileServiceRowStatus_Type())
clMdnsProfileServiceRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:clMdnsProfileServiceRowStatus.setStatus(_A)
_ClMdnsServiceProviderTable_Object=MibTable
clMdnsServiceProviderTable=_ClMdnsServiceProviderTable_Object((1,3,6,1,4,1,9,9,842,1,1,5))
if mibBuilder.loadTexts:clMdnsServiceProviderTable.setStatus(_A)
_ClMdnsServiceProviderEntry_Object=MibTableRow
clMdnsServiceProviderEntry=_ClMdnsServiceProviderEntry_Object((1,3,6,1,4,1,9,9,842,1,1,5,1))
clMdnsServiceProviderEntry.setIndexNames((0,_B,_H),(0,_B,_O))
if mibBuilder.loadTexts:clMdnsServiceProviderEntry.setStatus(_A)
_ClMdnsServiceProviderIndex_Type=Unsigned32
_ClMdnsServiceProviderIndex_Object=MibTableColumn
clMdnsServiceProviderIndex=_ClMdnsServiceProviderIndex_Object((1,3,6,1,4,1,9,9,842,1,1,5,1,1),_ClMdnsServiceProviderIndex_Type())
clMdnsServiceProviderIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:clMdnsServiceProviderIndex.setStatus(_A)
_ClMdnsServiceProviderMacAddress_Type=MacAddress
_ClMdnsServiceProviderMacAddress_Object=MibTableColumn
clMdnsServiceProviderMacAddress=_ClMdnsServiceProviderMacAddress_Object((1,3,6,1,4,1,9,9,842,1,1,5,1,2),_ClMdnsServiceProviderMacAddress_Type())
clMdnsServiceProviderMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:clMdnsServiceProviderMacAddress.setStatus(_A)
_ClMdnsServiceProviderName_Type=SnmpAdminString
_ClMdnsServiceProviderName_Object=MibTableColumn
clMdnsServiceProviderName=_ClMdnsServiceProviderName_Object((1,3,6,1,4,1,9,9,842,1,1,5,1,3),_ClMdnsServiceProviderName_Type())
clMdnsServiceProviderName.setMaxAccess(_C)
if mibBuilder.loadTexts:clMdnsServiceProviderName.setStatus(_A)
_ClMdnsServiceProviderVlan_Type=Unsigned32
_ClMdnsServiceProviderVlan_Object=MibTableColumn
clMdnsServiceProviderVlan=_ClMdnsServiceProviderVlan_Object((1,3,6,1,4,1,9,9,842,1,1,5,1,4),_ClMdnsServiceProviderVlan_Type())
clMdnsServiceProviderVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:clMdnsServiceProviderVlan.setStatus(_A)
class _ClMdnsServiceProviderType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_P,1),('wired',2),('both',3)))
_ClMdnsServiceProviderType_Type.__name__=_G
_ClMdnsServiceProviderType_Object=MibTableColumn
clMdnsServiceProviderType=_ClMdnsServiceProviderType_Object((1,3,6,1,4,1,9,9,842,1,1,5,1,5),_ClMdnsServiceProviderType_Type())
clMdnsServiceProviderType.setMaxAccess(_C)
if mibBuilder.loadTexts:clMdnsServiceProviderType.setStatus(_A)
_ClMdnsServiceProviderTtl_Type=Unsigned32
_ClMdnsServiceProviderTtl_Object=MibTableColumn
clMdnsServiceProviderTtl=_ClMdnsServiceProviderTtl_Object((1,3,6,1,4,1,9,9,842,1,1,5,1,6),_ClMdnsServiceProviderTtl_Type())
clMdnsServiceProviderTtl.setMaxAccess(_C)
if mibBuilder.loadTexts:clMdnsServiceProviderTtl.setStatus(_A)
if mibBuilder.loadTexts:clMdnsServiceProviderTtl.setUnits(_I)
_ClMdnsServiceProviderTimeLeft_Type=Unsigned32
_ClMdnsServiceProviderTimeLeft_Object=MibTableColumn
clMdnsServiceProviderTimeLeft=_ClMdnsServiceProviderTimeLeft_Object((1,3,6,1,4,1,9,9,842,1,1,5,1,7),_ClMdnsServiceProviderTimeLeft_Type())
clMdnsServiceProviderTimeLeft.setMaxAccess(_C)
if mibBuilder.loadTexts:clMdnsServiceProviderTimeLeft.setStatus(_A)
if mibBuilder.loadTexts:clMdnsServiceProviderTimeLeft.setUnits(_I)
_ClMdnsDnipTable_Object=MibTable
clMdnsDnipTable=_ClMdnsDnipTable_Object((1,3,6,1,4,1,9,9,842,1,1,6))
if mibBuilder.loadTexts:clMdnsDnipTable.setStatus(_A)
_ClMdnsDnipEntry_Object=MibTableRow
clMdnsDnipEntry=_ClMdnsDnipEntry_Object((1,3,6,1,4,1,9,9,842,1,1,6,1))
clMdnsDnipEntry.setIndexNames((0,_B,_Q))
if mibBuilder.loadTexts:clMdnsDnipEntry.setStatus(_A)
_ClMdnsDomainName_Type=SnmpAdminString
_ClMdnsDomainName_Object=MibTableColumn
clMdnsDomainName=_ClMdnsDomainName_Object((1,3,6,1,4,1,9,9,842,1,1,6,1,1),_ClMdnsDomainName_Type())
clMdnsDomainName.setMaxAccess(_F)
if mibBuilder.loadTexts:clMdnsDomainName.setStatus(_A)
_ClMdnsDomainMacAddress_Type=MacAddress
_ClMdnsDomainMacAddress_Object=MibTableColumn
clMdnsDomainMacAddress=_ClMdnsDomainMacAddress_Object((1,3,6,1,4,1,9,9,842,1,1,6,1,2),_ClMdnsDomainMacAddress_Type())
clMdnsDomainMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:clMdnsDomainMacAddress.setStatus(_A)
_ClMdnsDomainIpAddressType_Type=InetAddressType
_ClMdnsDomainIpAddressType_Object=MibTableColumn
clMdnsDomainIpAddressType=_ClMdnsDomainIpAddressType_Object((1,3,6,1,4,1,9,9,842,1,1,6,1,3),_ClMdnsDomainIpAddressType_Type())
clMdnsDomainIpAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:clMdnsDomainIpAddressType.setStatus(_A)
_ClMdnsDomainIpAddress_Type=InetAddress
_ClMdnsDomainIpAddress_Object=MibTableColumn
clMdnsDomainIpAddress=_ClMdnsDomainIpAddress_Object((1,3,6,1,4,1,9,9,842,1,1,6,1,4),_ClMdnsDomainIpAddress_Type())
clMdnsDomainIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:clMdnsDomainIpAddress.setStatus(_A)
_ClMdnsDomainVlan_Type=Unsigned32
_ClMdnsDomainVlan_Object=MibTableColumn
clMdnsDomainVlan=_ClMdnsDomainVlan_Object((1,3,6,1,4,1,9,9,842,1,1,6,1,5),_ClMdnsDomainVlan_Type())
clMdnsDomainVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:clMdnsDomainVlan.setStatus(_A)
class _ClMdnsDomainType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_P,1),('wired',2),('both',3)))
_ClMdnsDomainType_Type.__name__=_G
_ClMdnsDomainType_Object=MibTableColumn
clMdnsDomainType=_ClMdnsDomainType_Object((1,3,6,1,4,1,9,9,842,1,1,6,1,6),_ClMdnsDomainType_Type())
clMdnsDomainType.setMaxAccess(_C)
if mibBuilder.loadTexts:clMdnsDomainType.setStatus(_A)
_ClMdnsDomainEntryTtl_Type=Unsigned32
_ClMdnsDomainEntryTtl_Object=MibTableColumn
clMdnsDomainEntryTtl=_ClMdnsDomainEntryTtl_Object((1,3,6,1,4,1,9,9,842,1,1,6,1,7),_ClMdnsDomainEntryTtl_Type())
clMdnsDomainEntryTtl.setMaxAccess(_C)
if mibBuilder.loadTexts:clMdnsDomainEntryTtl.setStatus(_A)
if mibBuilder.loadTexts:clMdnsDomainEntryTtl.setUnits(_I)
_ClMdnsDomainEntryTimeLeft_Type=Unsigned32
_ClMdnsDomainEntryTimeLeft_Object=MibTableColumn
clMdnsDomainEntryTimeLeft=_ClMdnsDomainEntryTimeLeft_Object((1,3,6,1,4,1,9,9,842,1,1,6,1,8),_ClMdnsDomainEntryTimeLeft_Type())
clMdnsDomainEntryTimeLeft.setMaxAccess(_C)
if mibBuilder.loadTexts:clMdnsDomainEntryTimeLeft.setStatus(_A)
if mibBuilder.loadTexts:clMdnsDomainEntryTimeLeft.setUnits(_I)
_CLMdnsServiceGroupTable_Object=MibTable
cLMdnsServiceGroupTable=_CLMdnsServiceGroupTable_Object((1,3,6,1,4,1,9,9,842,1,1,7))
if mibBuilder.loadTexts:cLMdnsServiceGroupTable.setStatus(_A)
_CLMdnsServiceGroupEntry_Object=MibTableRow
cLMdnsServiceGroupEntry=_CLMdnsServiceGroupEntry_Object((1,3,6,1,4,1,9,9,842,1,1,7,1))
cLMdnsServiceGroupEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:cLMdnsServiceGroupEntry.setStatus(_A)
class _CLMdnsServiceGroupName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,256))
_CLMdnsServiceGroupName_Type.__name__=_E
_CLMdnsServiceGroupName_Object=MibTableColumn
cLMdnsServiceGroupName=_CLMdnsServiceGroupName_Object((1,3,6,1,4,1,9,9,842,1,1,7,1,1),_CLMdnsServiceGroupName_Type())
cLMdnsServiceGroupName.setMaxAccess(_F)
if mibBuilder.loadTexts:cLMdnsServiceGroupName.setStatus(_A)
class _CLMdnsServiceGroupDescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_CLMdnsServiceGroupDescription_Type.__name__=_E
_CLMdnsServiceGroupDescription_Object=MibTableColumn
cLMdnsServiceGroupDescription=_CLMdnsServiceGroupDescription_Object((1,3,6,1,4,1,9,9,842,1,1,7,1,2),_CLMdnsServiceGroupDescription_Type())
cLMdnsServiceGroupDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:cLMdnsServiceGroupDescription.setStatus(_A)
_CLMdnsServiceGroupRowStatus_Type=RowStatus
_CLMdnsServiceGroupRowStatus_Object=MibTableColumn
cLMdnsServiceGroupRowStatus=_CLMdnsServiceGroupRowStatus_Object((1,3,6,1,4,1,9,9,842,1,1,7,1,3),_CLMdnsServiceGroupRowStatus_Type())
cLMdnsServiceGroupRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cLMdnsServiceGroupRowStatus.setStatus(_A)
_CLMdnsServiceGroupDeviceMacTable_Object=MibTable
cLMdnsServiceGroupDeviceMacTable=_CLMdnsServiceGroupDeviceMacTable_Object((1,3,6,1,4,1,9,9,842,1,1,8))
if mibBuilder.loadTexts:cLMdnsServiceGroupDeviceMacTable.setStatus(_A)
_CLMdnsServiceGroupDeviceMacEntry_Object=MibTableRow
cLMdnsServiceGroupDeviceMacEntry=_CLMdnsServiceGroupDeviceMacEntry_Object((1,3,6,1,4,1,9,9,842,1,1,8,1))
cLMdnsServiceGroupDeviceMacEntry.setIndexNames((0,_B,_J),(0,_B,_R))
if mibBuilder.loadTexts:cLMdnsServiceGroupDeviceMacEntry.setStatus(_A)
_CLMdnsServiceGroupDeviceMac_Type=MacAddress
_CLMdnsServiceGroupDeviceMac_Object=MibTableColumn
cLMdnsServiceGroupDeviceMac=_CLMdnsServiceGroupDeviceMac_Object((1,3,6,1,4,1,9,9,842,1,1,8,1,1),_CLMdnsServiceGroupDeviceMac_Type())
cLMdnsServiceGroupDeviceMac.setMaxAccess(_F)
if mibBuilder.loadTexts:cLMdnsServiceGroupDeviceMac.setStatus(_A)
class _CLMdnsServiceGroupDeviceName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_CLMdnsServiceGroupDeviceName_Type.__name__=_E
_CLMdnsServiceGroupDeviceName_Object=MibTableColumn
cLMdnsServiceGroupDeviceName=_CLMdnsServiceGroupDeviceName_Object((1,3,6,1,4,1,9,9,842,1,1,8,1,2),_CLMdnsServiceGroupDeviceName_Type())
cLMdnsServiceGroupDeviceName.setMaxAccess(_D)
if mibBuilder.loadTexts:cLMdnsServiceGroupDeviceName.setStatus(_A)
class _CLMdnsServiceGroupLocationName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_CLMdnsServiceGroupLocationName_Type.__name__=_E
_CLMdnsServiceGroupLocationName_Object=MibTableColumn
cLMdnsServiceGroupLocationName=_CLMdnsServiceGroupLocationName_Object((1,3,6,1,4,1,9,9,842,1,1,8,1,3),_CLMdnsServiceGroupLocationName_Type())
cLMdnsServiceGroupLocationName.setMaxAccess(_D)
if mibBuilder.loadTexts:cLMdnsServiceGroupLocationName.setStatus(_A)
class _CLMdnsServiceGroupLocationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('apName',1),('apGroup',2),('apLocation',3)))
_CLMdnsServiceGroupLocationType_Type.__name__=_G
_CLMdnsServiceGroupLocationType_Object=MibTableColumn
cLMdnsServiceGroupLocationType=_CLMdnsServiceGroupLocationType_Object((1,3,6,1,4,1,9,9,842,1,1,8,1,4),_CLMdnsServiceGroupLocationType_Type())
cLMdnsServiceGroupLocationType.setMaxAccess(_D)
if mibBuilder.loadTexts:cLMdnsServiceGroupLocationType.setStatus(_A)
_CLMdnsServiceGroupDeviceMacRowStatus_Type=RowStatus
_CLMdnsServiceGroupDeviceMacRowStatus_Object=MibTableColumn
cLMdnsServiceGroupDeviceMacRowStatus=_CLMdnsServiceGroupDeviceMacRowStatus_Object((1,3,6,1,4,1,9,9,842,1,1,8,1,5),_CLMdnsServiceGroupDeviceMacRowStatus_Type())
cLMdnsServiceGroupDeviceMacRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cLMdnsServiceGroupDeviceMacRowStatus.setStatus(_A)
_CLMdnsServiceGroupRuleTable_Object=MibTable
cLMdnsServiceGroupRuleTable=_CLMdnsServiceGroupRuleTable_Object((1,3,6,1,4,1,9,9,842,1,1,9))
if mibBuilder.loadTexts:cLMdnsServiceGroupRuleTable.setStatus(_A)
_CLMdnsServiceGroupRuleEntry_Object=MibTableRow
cLMdnsServiceGroupRuleEntry=_CLMdnsServiceGroupRuleEntry_Object((1,3,6,1,4,1,9,9,842,1,1,9,1))
cLMdnsServiceGroupRuleEntry.setIndexNames((0,_B,_J),(0,_B,_S))
if mibBuilder.loadTexts:cLMdnsServiceGroupRuleEntry.setStatus(_A)
class _CLMdnsRuleName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,266))
_CLMdnsRuleName_Type.__name__=_E
_CLMdnsRuleName_Object=MibTableColumn
cLMdnsRuleName=_CLMdnsRuleName_Object((1,3,6,1,4,1,9,9,842,1,1,9,1,1),_CLMdnsRuleName_Type())
cLMdnsRuleName.setMaxAccess(_F)
if mibBuilder.loadTexts:cLMdnsRuleName.setStatus(_A)
class _CLMdnsRuleRole_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_CLMdnsRuleRole_Type.__name__=_E
_CLMdnsRuleRole_Object=MibTableColumn
cLMdnsRuleRole=_CLMdnsRuleRole_Object((1,3,6,1,4,1,9,9,842,1,1,9,1,2),_CLMdnsRuleRole_Type())
cLMdnsRuleRole.setMaxAccess(_D)
if mibBuilder.loadTexts:cLMdnsRuleRole.setStatus(_A)
class _CLMdnsRuleUserId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_CLMdnsRuleUserId_Type.__name__=_E
_CLMdnsRuleUserId_Object=MibTableColumn
cLMdnsRuleUserId=_CLMdnsRuleUserId_Object((1,3,6,1,4,1,9,9,842,1,1,9,1,3),_CLMdnsRuleUserId_Type())
cLMdnsRuleUserId.setMaxAccess(_D)
if mibBuilder.loadTexts:cLMdnsRuleUserId.setStatus(_A)
_CLMdnsServiceGroupRuleRowStatus_Type=RowStatus
_CLMdnsServiceGroupRuleRowStatus_Object=MibTableColumn
cLMdnsServiceGroupRuleRowStatus=_CLMdnsServiceGroupRuleRowStatus_Object((1,3,6,1,4,1,9,9,842,1,1,9,1,4),_CLMdnsServiceGroupRuleRowStatus_Type())
cLMdnsServiceGroupRuleRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cLMdnsServiceGroupRuleRowStatus.setStatus(_A)
_CiscoLwappMdnsMIBConform_ObjectIdentity=ObjectIdentity
ciscoLwappMdnsMIBConform=_CiscoLwappMdnsMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,842,2))
_CiscoLwappMdnsMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoLwappMdnsMIBCompliances=_CiscoLwappMdnsMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,842,2,1))
_CiscoLwappMdnsMIBGroups_ObjectIdentity=ObjectIdentity
ciscoLwappMdnsMIBGroups=_CiscoLwappMdnsMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,842,2,2))
cLMdnsConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,842,2,2,1))
cLMdnsConfigGroup.setObjects(*((_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:cLMdnsConfigGroup.setStatus(_A)
cLMdnsMonitorGroup=ObjectGroup((1,3,6,1,4,1,9,9,842,2,2,2))
cLMdnsMonitorGroup.setObjects(*((_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p)))
if mibBuilder.loadTexts:cLMdnsMonitorGroup.setStatus(_A)
cLMdnsServiceGroup=ObjectGroup((1,3,6,1,4,1,9,9,842,2,2,3))
cLMdnsServiceGroup.setObjects(*((_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y)))
if mibBuilder.loadTexts:cLMdnsServiceGroup.setStatus(_A)
ciscoLwappMdnsMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,842,2,1,1))
ciscoLwappMdnsMIBCompliance.setObjects(*((_B,_z),(_B,_A0),(_B,_A1)))
if mibBuilder.loadTexts:ciscoLwappMdnsMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoLwappMdnsMIB':ciscoLwappMdnsMIB,'ciscoLwappMdnsMIBNotifs':ciscoLwappMdnsMIBNotifs,'ciscoLwappMdnsMIBObjects':ciscoLwappMdnsMIBObjects,'clMdnsConfigObjects':clMdnsConfigObjects,'clMdnsGlobalConfig':clMdnsGlobalConfig,_T:clMdnsSnoopingEnabled,_U:clMdnsQueryInterval,'clMdnsMasterServiceTable':clMdnsMasterServiceTable,'clMdnsMasterServiceEntry':clMdnsMasterServiceEntry,_H:clMdnsServiceName,_V:clMdnsServiceString,_W:clMdnsServiceQueryStatus,_X:clMdnsServiceRowStatus,'clMdnsProfileTable':clMdnsProfileTable,'clMdnsProfileEntry':clMdnsProfileEntry,_L:clMdnsProfileName,_Y:clMdnsProfileRowStatus,_a:clMdnsProfileWlanCount,_b:clMdnsProfileInterfaceCount,_c:clMdnsProfileInterfaceGrpCount,'clMdnsProfileServiceTable':clMdnsProfileServiceTable,'clMdnsProfileServiceEntry':clMdnsProfileServiceEntry,_Z:clMdnsProfileServiceRowStatus,'clMdnsServiceProviderTable':clMdnsServiceProviderTable,'clMdnsServiceProviderEntry':clMdnsServiceProviderEntry,_O:clMdnsServiceProviderIndex,_d:clMdnsServiceProviderMacAddress,_e:clMdnsServiceProviderName,_f:clMdnsServiceProviderVlan,_g:clMdnsServiceProviderType,_h:clMdnsServiceProviderTtl,_i:clMdnsServiceProviderTimeLeft,'clMdnsDnipTable':clMdnsDnipTable,'clMdnsDnipEntry':clMdnsDnipEntry,_Q:clMdnsDomainName,_j:clMdnsDomainMacAddress,_k:clMdnsDomainIpAddressType,_l:clMdnsDomainIpAddress,_m:clMdnsDomainVlan,_n:clMdnsDomainType,_o:clMdnsDomainEntryTtl,_p:clMdnsDomainEntryTimeLeft,'cLMdnsServiceGroupTable':cLMdnsServiceGroupTable,'cLMdnsServiceGroupEntry':cLMdnsServiceGroupEntry,_J:cLMdnsServiceGroupName,_q:cLMdnsServiceGroupDescription,_r:cLMdnsServiceGroupRowStatus,'cLMdnsServiceGroupDeviceMacTable':cLMdnsServiceGroupDeviceMacTable,'cLMdnsServiceGroupDeviceMacEntry':cLMdnsServiceGroupDeviceMacEntry,_R:cLMdnsServiceGroupDeviceMac,_s:cLMdnsServiceGroupDeviceName,_t:cLMdnsServiceGroupLocationName,_u:cLMdnsServiceGroupLocationType,_v:cLMdnsServiceGroupDeviceMacRowStatus,'cLMdnsServiceGroupRuleTable':cLMdnsServiceGroupRuleTable,'cLMdnsServiceGroupRuleEntry':cLMdnsServiceGroupRuleEntry,_S:cLMdnsRuleName,_w:cLMdnsRuleRole,_x:cLMdnsRuleUserId,_y:cLMdnsServiceGroupRuleRowStatus,'ciscoLwappMdnsMIBConform':ciscoLwappMdnsMIBConform,'ciscoLwappMdnsMIBCompliances':ciscoLwappMdnsMIBCompliances,'ciscoLwappMdnsMIBCompliance':ciscoLwappMdnsMIBCompliance,'ciscoLwappMdnsMIBGroups':ciscoLwappMdnsMIBGroups,_z:cLMdnsConfigGroup,_A0:cLMdnsMonitorGroup,_A1:cLMdnsServiceGroup})