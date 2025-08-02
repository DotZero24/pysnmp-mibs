_A5='etsysConvEndPointGlobalConfigGroup2'
_A4='etsysConvEndPointCiscoVoiceVLANGroup'
_A3='etsysConvEndPointPortConfigGroup'
_A2='etsysConvEndPointDetectionGroup'
_A1='etsysConvEndPointStatusGroup'
_A0='etsysConvEndPointGlobalConfigAccountEnable'
_z='etsysCEPCiscoCDPVoicePortVlan'
_y='etsysCEPPortClearUsers'
_x='etsysConvEndPointDetectionMaxEntries'
_w='etsysCEPConnMacInetAddress'
_v='etsysCEPConnMacInetAddressType'
_u='etsysCEPConnMacFirmwareVersion'
_t='etsysCEPConnMacDiscoveryTime'
_s='etsysCEPConnMacPolicyIndex'
_r='etsysCEPConnMacEndPointType'
_q='etsysConvEndPointConnMacInetAddress'
_p='etsysConvEndPointConnMacInetAddressType'
_o='etsysConvEndPointConnMacFirmwareVersion'
_n='etsysConvEndPointConnMacDiscoveryTime'
_m='etsysConvEndPointConnMacPolicyIndex'
_l='etsysConvEndPointConnMacEndPointType'
_k='etsysConvEndPointConnMacPortNumber'
_j='etsysConvEndPointProtocolEnable'
_i='etsysConvEndPointDetectionRuleIndex'
_h='etsysConvEndPointConnMacMacAddress'
_g='etsysConvEndPointProtocolEndPointType'
_f='etsysConvEndPointGlobalEndPointType'
_e='TruthValue'
_d='etsysConvEndPointDetectionGroup2'
_c='etsysConvEndPointStatusGroup2'
_b='etsysConvEndPointGlobalConfigGroup'
_a='etsysConvEndPointDetectionRowStatus'
_Z='etsysConvEndPointDetectionAddrMask'
_Y='etsysConvEndPointDetectionAddrMaskType'
_X='etsysConvEndPointDetectionAddr'
_W='etsysConvEndPointDetectionAddrType'
_V='etsysConvEndPointDetectionPortHigh'
_U='etsysConvEndPointDetectionPortLow'
_T='etsysConvEndPointDetectionProtocol'
_S='etsysConvEndPointDetectionEndPointType'
_R='etsysConvEndPointGlobalDefaultPolicyIndex'
_Q='etsysConvEndPointGlobalConfigEnable'
_P='SnmpAdminString'
_O='etsysConvEndPointConfigGroup'
_N='not-accessible'
_M='EnabledStatus'
_L='etsysConvEndPointConnPortMacAddress'
_K='InetAddressType'
_J='InetAddress'
_I='read-write'
_H='ifIndex'
_G='IF-MIB'
_F='Integer32'
_E='read-create'
_D='read-only'
_C='deprecated'
_B='current'
_A='ENTERASYS-CONVERGENCE-END-POINT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_G,'InterfaceIndex',_H)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_J,_K)
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_M)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_P)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_e)
etsysConvergenceEndPointMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,40))
if mibBuilder.loadTexts:etsysConvergenceEndPointMIB.setRevisions(('2013-08-08 14:05','2013-03-04 13:37','2005-11-18 13:25','2005-10-19 15:49','2005-08-16 12:33','2005-06-16 14:27','2005-03-31 16:10','2003-11-05 19:42'))
class ConvEndPointTypes(TextualConvention,Bits):status=_B;namedValues=NamedValues(*(('ciscoIPphone',0),('siemensIPphone',1),('avayaCLan',2),('avayaMedPro',3),('genericH323',4),('sip',5),('lldpMed',6)))
_EtsysConvEndPointObjects_ObjectIdentity=ObjectIdentity
etsysConvEndPointObjects=_EtsysConvEndPointObjects_ObjectIdentity((1,3,6,1,4,1,5624,1,2,40,1))
_EtsysConvEndPointConfig_ObjectIdentity=ObjectIdentity
etsysConvEndPointConfig=_EtsysConvEndPointConfig_ObjectIdentity((1,3,6,1,4,1,5624,1,2,40,1,1))
class _EtsysConvEndPointGlobalConfigEnable_Type(EnabledStatus):defaultValue=2
_EtsysConvEndPointGlobalConfigEnable_Type.__name__=_M
_EtsysConvEndPointGlobalConfigEnable_Object=MibScalar
etsysConvEndPointGlobalConfigEnable=_EtsysConvEndPointGlobalConfigEnable_Object((1,3,6,1,4,1,5624,1,2,40,1,1,1),_EtsysConvEndPointGlobalConfigEnable_Type())
etsysConvEndPointGlobalConfigEnable.setMaxAccess(_I)
if mibBuilder.loadTexts:etsysConvEndPointGlobalConfigEnable.setStatus(_B)
_EtsysConvEndPointGlobalConfigTable_Object=MibTable
etsysConvEndPointGlobalConfigTable=_EtsysConvEndPointGlobalConfigTable_Object((1,3,6,1,4,1,5624,1,2,40,1,1,2))
if mibBuilder.loadTexts:etsysConvEndPointGlobalConfigTable.setStatus(_B)
_EtsysConvEndPointGlobalConfigEntry_Object=MibTableRow
etsysConvEndPointGlobalConfigEntry=_EtsysConvEndPointGlobalConfigEntry_Object((1,3,6,1,4,1,5624,1,2,40,1,1,2,1))
etsysConvEndPointGlobalConfigEntry.setIndexNames((0,_A,_f))
if mibBuilder.loadTexts:etsysConvEndPointGlobalConfigEntry.setStatus(_B)
_EtsysConvEndPointGlobalEndPointType_Type=ConvEndPointTypes
_EtsysConvEndPointGlobalEndPointType_Object=MibTableColumn
etsysConvEndPointGlobalEndPointType=_EtsysConvEndPointGlobalEndPointType_Object((1,3,6,1,4,1,5624,1,2,40,1,1,2,1,1),_EtsysConvEndPointGlobalEndPointType_Type())
etsysConvEndPointGlobalEndPointType.setMaxAccess(_N)
if mibBuilder.loadTexts:etsysConvEndPointGlobalEndPointType.setStatus(_B)
class _EtsysConvEndPointGlobalDefaultPolicyIndex_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,65535))
_EtsysConvEndPointGlobalDefaultPolicyIndex_Type.__name__=_F
_EtsysConvEndPointGlobalDefaultPolicyIndex_Object=MibTableColumn
etsysConvEndPointGlobalDefaultPolicyIndex=_EtsysConvEndPointGlobalDefaultPolicyIndex_Object((1,3,6,1,4,1,5624,1,2,40,1,1,2,1,2),_EtsysConvEndPointGlobalDefaultPolicyIndex_Type())
etsysConvEndPointGlobalDefaultPolicyIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:etsysConvEndPointGlobalDefaultPolicyIndex.setStatus(_B)
_EtsysConvEndPointProtocolConfigTable_Object=MibTable
etsysConvEndPointProtocolConfigTable=_EtsysConvEndPointProtocolConfigTable_Object((1,3,6,1,4,1,5624,1,2,40,1,1,3))
if mibBuilder.loadTexts:etsysConvEndPointProtocolConfigTable.setStatus(_B)
_EtsysConvEndPointProtocolConfigEntry_Object=MibTableRow
etsysConvEndPointProtocolConfigEntry=_EtsysConvEndPointProtocolConfigEntry_Object((1,3,6,1,4,1,5624,1,2,40,1,1,3,1))
etsysConvEndPointProtocolConfigEntry.setIndexNames((0,_G,_H),(0,_A,_g))
if mibBuilder.loadTexts:etsysConvEndPointProtocolConfigEntry.setStatus(_B)
_EtsysConvEndPointProtocolEndPointType_Type=ConvEndPointTypes
_EtsysConvEndPointProtocolEndPointType_Object=MibTableColumn
etsysConvEndPointProtocolEndPointType=_EtsysConvEndPointProtocolEndPointType_Object((1,3,6,1,4,1,5624,1,2,40,1,1,3,1,1),_EtsysConvEndPointProtocolEndPointType_Type())
etsysConvEndPointProtocolEndPointType.setMaxAccess(_N)
if mibBuilder.loadTexts:etsysConvEndPointProtocolEndPointType.setStatus(_B)
class _EtsysConvEndPointProtocolEnable_Type(EnabledStatus):defaultValue=2
_EtsysConvEndPointProtocolEnable_Type.__name__=_M
_EtsysConvEndPointProtocolEnable_Object=MibTableColumn
etsysConvEndPointProtocolEnable=_EtsysConvEndPointProtocolEnable_Object((1,3,6,1,4,1,5624,1,2,40,1,1,3,1,2),_EtsysConvEndPointProtocolEnable_Type())
etsysConvEndPointProtocolEnable.setMaxAccess(_I)
if mibBuilder.loadTexts:etsysConvEndPointProtocolEnable.setStatus(_B)
class _EtsysConvEndPointGlobalConfigAccountEnable_Type(EnabledStatus):defaultValue=2
_EtsysConvEndPointGlobalConfigAccountEnable_Type.__name__=_M
_EtsysConvEndPointGlobalConfigAccountEnable_Object=MibScalar
etsysConvEndPointGlobalConfigAccountEnable=_EtsysConvEndPointGlobalConfigAccountEnable_Object((1,3,6,1,4,1,5624,1,2,40,1,1,4),_EtsysConvEndPointGlobalConfigAccountEnable_Type())
etsysConvEndPointGlobalConfigAccountEnable.setMaxAccess(_I)
if mibBuilder.loadTexts:etsysConvEndPointGlobalConfigAccountEnable.setStatus(_B)
_EtsysConvEndPointStatus_ObjectIdentity=ObjectIdentity
etsysConvEndPointStatus=_EtsysConvEndPointStatus_ObjectIdentity((1,3,6,1,4,1,5624,1,2,40,1,2))
_EtsysConvEndPointConnMacTable_Object=MibTable
etsysConvEndPointConnMacTable=_EtsysConvEndPointConnMacTable_Object((1,3,6,1,4,1,5624,1,2,40,1,2,1))
if mibBuilder.loadTexts:etsysConvEndPointConnMacTable.setStatus(_C)
_EtsysConvEndPointConnMacEntry_Object=MibTableRow
etsysConvEndPointConnMacEntry=_EtsysConvEndPointConnMacEntry_Object((1,3,6,1,4,1,5624,1,2,40,1,2,1,1))
etsysConvEndPointConnMacEntry.setIndexNames((0,_A,_h))
if mibBuilder.loadTexts:etsysConvEndPointConnMacEntry.setStatus(_C)
_EtsysConvEndPointConnMacMacAddress_Type=MacAddress
_EtsysConvEndPointConnMacMacAddress_Object=MibTableColumn
etsysConvEndPointConnMacMacAddress=_EtsysConvEndPointConnMacMacAddress_Object((1,3,6,1,4,1,5624,1,2,40,1,2,1,1,1),_EtsysConvEndPointConnMacMacAddress_Type())
etsysConvEndPointConnMacMacAddress.setMaxAccess(_N)
if mibBuilder.loadTexts:etsysConvEndPointConnMacMacAddress.setStatus(_C)
_EtsysConvEndPointConnMacPortNumber_Type=InterfaceIndex
_EtsysConvEndPointConnMacPortNumber_Object=MibTableColumn
etsysConvEndPointConnMacPortNumber=_EtsysConvEndPointConnMacPortNumber_Object((1,3,6,1,4,1,5624,1,2,40,1,2,1,1,2),_EtsysConvEndPointConnMacPortNumber_Type())
etsysConvEndPointConnMacPortNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysConvEndPointConnMacPortNumber.setStatus(_C)
_EtsysConvEndPointConnMacEndPointType_Type=ConvEndPointTypes
_EtsysConvEndPointConnMacEndPointType_Object=MibTableColumn
etsysConvEndPointConnMacEndPointType=_EtsysConvEndPointConnMacEndPointType_Object((1,3,6,1,4,1,5624,1,2,40,1,2,1,1,3),_EtsysConvEndPointConnMacEndPointType_Type())
etsysConvEndPointConnMacEndPointType.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysConvEndPointConnMacEndPointType.setStatus(_C)
_EtsysConvEndPointConnMacPolicyIndex_Type=Integer32
_EtsysConvEndPointConnMacPolicyIndex_Object=MibTableColumn
etsysConvEndPointConnMacPolicyIndex=_EtsysConvEndPointConnMacPolicyIndex_Object((1,3,6,1,4,1,5624,1,2,40,1,2,1,1,4),_EtsysConvEndPointConnMacPolicyIndex_Type())
etsysConvEndPointConnMacPolicyIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysConvEndPointConnMacPolicyIndex.setStatus(_C)
_EtsysConvEndPointConnMacDiscoveryTime_Type=DateAndTime
_EtsysConvEndPointConnMacDiscoveryTime_Object=MibTableColumn
etsysConvEndPointConnMacDiscoveryTime=_EtsysConvEndPointConnMacDiscoveryTime_Object((1,3,6,1,4,1,5624,1,2,40,1,2,1,1,5),_EtsysConvEndPointConnMacDiscoveryTime_Type())
etsysConvEndPointConnMacDiscoveryTime.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysConvEndPointConnMacDiscoveryTime.setStatus(_C)
class _EtsysConvEndPointConnMacFirmwareVersion_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_EtsysConvEndPointConnMacFirmwareVersion_Type.__name__=_P
_EtsysConvEndPointConnMacFirmwareVersion_Object=MibTableColumn
etsysConvEndPointConnMacFirmwareVersion=_EtsysConvEndPointConnMacFirmwareVersion_Object((1,3,6,1,4,1,5624,1,2,40,1,2,1,1,6),_EtsysConvEndPointConnMacFirmwareVersion_Type())
etsysConvEndPointConnMacFirmwareVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysConvEndPointConnMacFirmwareVersion.setStatus(_C)
class _EtsysConvEndPointConnMacInetAddressType_Type(InetAddressType):defaultValue=0
_EtsysConvEndPointConnMacInetAddressType_Type.__name__=_K
_EtsysConvEndPointConnMacInetAddressType_Object=MibTableColumn
etsysConvEndPointConnMacInetAddressType=_EtsysConvEndPointConnMacInetAddressType_Object((1,3,6,1,4,1,5624,1,2,40,1,2,1,1,7),_EtsysConvEndPointConnMacInetAddressType_Type())
etsysConvEndPointConnMacInetAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysConvEndPointConnMacInetAddressType.setStatus(_C)
class _EtsysConvEndPointConnMacInetAddress_Type(InetAddress):defaultValue=OctetString('')
_EtsysConvEndPointConnMacInetAddress_Type.__name__=_J
_EtsysConvEndPointConnMacInetAddress_Object=MibTableColumn
etsysConvEndPointConnMacInetAddress=_EtsysConvEndPointConnMacInetAddress_Object((1,3,6,1,4,1,5624,1,2,40,1,2,1,1,8),_EtsysConvEndPointConnMacInetAddress_Type())
etsysConvEndPointConnMacInetAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysConvEndPointConnMacInetAddress.setStatus(_C)
_EtsysConvEndPointConnPortTable_Object=MibTable
etsysConvEndPointConnPortTable=_EtsysConvEndPointConnPortTable_Object((1,3,6,1,4,1,5624,1,2,40,1,2,2))
if mibBuilder.loadTexts:etsysConvEndPointConnPortTable.setStatus(_B)
_EtsysConvEndPointConnPortEntry_Object=MibTableRow
etsysConvEndPointConnPortEntry=_EtsysConvEndPointConnPortEntry_Object((1,3,6,1,4,1,5624,1,2,40,1,2,2,1))
etsysConvEndPointConnPortEntry.setIndexNames((0,_G,_H),(0,_A,_L))
if mibBuilder.loadTexts:etsysConvEndPointConnPortEntry.setStatus(_B)
_EtsysConvEndPointConnPortMacAddress_Type=MacAddress
_EtsysConvEndPointConnPortMacAddress_Object=MibTableColumn
etsysConvEndPointConnPortMacAddress=_EtsysConvEndPointConnPortMacAddress_Object((1,3,6,1,4,1,5624,1,2,40,1,2,2,1,1),_EtsysConvEndPointConnPortMacAddress_Type())
etsysConvEndPointConnPortMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysConvEndPointConnPortMacAddress.setStatus(_B)
_EtsysCEPConnMacTable_Object=MibTable
etsysCEPConnMacTable=_EtsysCEPConnMacTable_Object((1,3,6,1,4,1,5624,1,2,40,1,2,3))
if mibBuilder.loadTexts:etsysCEPConnMacTable.setStatus(_B)
_EtsysCEPConnMacEntry_Object=MibTableRow
etsysCEPConnMacEntry=_EtsysCEPConnMacEntry_Object((1,3,6,1,4,1,5624,1,2,40,1,2,3,1))
etsysCEPConnMacEntry.setIndexNames((0,_A,_L),(0,_G,_H))
if mibBuilder.loadTexts:etsysCEPConnMacEntry.setStatus(_B)
_EtsysCEPConnMacEndPointType_Type=ConvEndPointTypes
_EtsysCEPConnMacEndPointType_Object=MibTableColumn
etsysCEPConnMacEndPointType=_EtsysCEPConnMacEndPointType_Object((1,3,6,1,4,1,5624,1,2,40,1,2,3,1,1),_EtsysCEPConnMacEndPointType_Type())
etsysCEPConnMacEndPointType.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysCEPConnMacEndPointType.setStatus(_B)
class _EtsysCEPConnMacPolicyIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,65535))
_EtsysCEPConnMacPolicyIndex_Type.__name__=_F
_EtsysCEPConnMacPolicyIndex_Object=MibTableColumn
etsysCEPConnMacPolicyIndex=_EtsysCEPConnMacPolicyIndex_Object((1,3,6,1,4,1,5624,1,2,40,1,2,3,1,2),_EtsysCEPConnMacPolicyIndex_Type())
etsysCEPConnMacPolicyIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysCEPConnMacPolicyIndex.setStatus(_B)
_EtsysCEPConnMacDiscoveryTime_Type=DateAndTime
_EtsysCEPConnMacDiscoveryTime_Object=MibTableColumn
etsysCEPConnMacDiscoveryTime=_EtsysCEPConnMacDiscoveryTime_Object((1,3,6,1,4,1,5624,1,2,40,1,2,3,1,3),_EtsysCEPConnMacDiscoveryTime_Type())
etsysCEPConnMacDiscoveryTime.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysCEPConnMacDiscoveryTime.setStatus(_B)
class _EtsysCEPConnMacFirmwareVersion_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_EtsysCEPConnMacFirmwareVersion_Type.__name__=_P
_EtsysCEPConnMacFirmwareVersion_Object=MibTableColumn
etsysCEPConnMacFirmwareVersion=_EtsysCEPConnMacFirmwareVersion_Object((1,3,6,1,4,1,5624,1,2,40,1,2,3,1,4),_EtsysCEPConnMacFirmwareVersion_Type())
etsysCEPConnMacFirmwareVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysCEPConnMacFirmwareVersion.setStatus(_B)
class _EtsysCEPConnMacInetAddressType_Type(InetAddressType):defaultValue=0
_EtsysCEPConnMacInetAddressType_Type.__name__=_K
_EtsysCEPConnMacInetAddressType_Object=MibTableColumn
etsysCEPConnMacInetAddressType=_EtsysCEPConnMacInetAddressType_Object((1,3,6,1,4,1,5624,1,2,40,1,2,3,1,5),_EtsysCEPConnMacInetAddressType_Type())
etsysCEPConnMacInetAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysCEPConnMacInetAddressType.setStatus(_B)
class _EtsysCEPConnMacInetAddress_Type(InetAddress):defaultValue=OctetString('')
_EtsysCEPConnMacInetAddress_Type.__name__=_J
_EtsysCEPConnMacInetAddress_Object=MibTableColumn
etsysCEPConnMacInetAddress=_EtsysCEPConnMacInetAddress_Object((1,3,6,1,4,1,5624,1,2,40,1,2,3,1,6),_EtsysCEPConnMacInetAddress_Type())
etsysCEPConnMacInetAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysCEPConnMacInetAddress.setStatus(_B)
_EtsysConvEndPointDetection_ObjectIdentity=ObjectIdentity
etsysConvEndPointDetection=_EtsysConvEndPointDetection_ObjectIdentity((1,3,6,1,4,1,5624,1,2,40,1,3))
_EtsysConvEndPointDetectionMaxEntries_Type=Integer32
_EtsysConvEndPointDetectionMaxEntries_Object=MibScalar
etsysConvEndPointDetectionMaxEntries=_EtsysConvEndPointDetectionMaxEntries_Object((1,3,6,1,4,1,5624,1,2,40,1,3,1),_EtsysConvEndPointDetectionMaxEntries_Type())
etsysConvEndPointDetectionMaxEntries.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysConvEndPointDetectionMaxEntries.setStatus(_B)
_EtsysConvEndPointDetectionTable_Object=MibTable
etsysConvEndPointDetectionTable=_EtsysConvEndPointDetectionTable_Object((1,3,6,1,4,1,5624,1,2,40,1,3,2))
if mibBuilder.loadTexts:etsysConvEndPointDetectionTable.setStatus(_B)
_EtsysConvEndPointDetectionEntry_Object=MibTableRow
etsysConvEndPointDetectionEntry=_EtsysConvEndPointDetectionEntry_Object((1,3,6,1,4,1,5624,1,2,40,1,3,2,1))
etsysConvEndPointDetectionEntry.setIndexNames((0,_A,_i))
if mibBuilder.loadTexts:etsysConvEndPointDetectionEntry.setStatus(_B)
class _EtsysConvEndPointDetectionRuleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_EtsysConvEndPointDetectionRuleIndex_Type.__name__=_F
_EtsysConvEndPointDetectionRuleIndex_Object=MibTableColumn
etsysConvEndPointDetectionRuleIndex=_EtsysConvEndPointDetectionRuleIndex_Object((1,3,6,1,4,1,5624,1,2,40,1,3,2,1,1),_EtsysConvEndPointDetectionRuleIndex_Type())
etsysConvEndPointDetectionRuleIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:etsysConvEndPointDetectionRuleIndex.setStatus(_B)
class _EtsysConvEndPointDetectionEndPointType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('h323',0),('siemens',1),('sip',2)))
_EtsysConvEndPointDetectionEndPointType_Type.__name__=_F
_EtsysConvEndPointDetectionEndPointType_Object=MibTableColumn
etsysConvEndPointDetectionEndPointType=_EtsysConvEndPointDetectionEndPointType_Object((1,3,6,1,4,1,5624,1,2,40,1,3,2,1,2),_EtsysConvEndPointDetectionEndPointType_Type())
etsysConvEndPointDetectionEndPointType.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysConvEndPointDetectionEndPointType.setStatus(_B)
class _EtsysConvEndPointDetectionProtocol_Type(Bits):defaultBinValue='11';namedValues=NamedValues(*(('udp',0),('tcp',1)))
_EtsysConvEndPointDetectionProtocol_Type.__name__='Bits'
_EtsysConvEndPointDetectionProtocol_Object=MibTableColumn
etsysConvEndPointDetectionProtocol=_EtsysConvEndPointDetectionProtocol_Object((1,3,6,1,4,1,5624,1,2,40,1,3,2,1,3),_EtsysConvEndPointDetectionProtocol_Type())
etsysConvEndPointDetectionProtocol.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysConvEndPointDetectionProtocol.setStatus(_B)
class _EtsysConvEndPointDetectionPortLow_Type(Integer32):defaultValue=4060;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_EtsysConvEndPointDetectionPortLow_Type.__name__=_F
_EtsysConvEndPointDetectionPortLow_Object=MibTableColumn
etsysConvEndPointDetectionPortLow=_EtsysConvEndPointDetectionPortLow_Object((1,3,6,1,4,1,5624,1,2,40,1,3,2,1,4),_EtsysConvEndPointDetectionPortLow_Type())
etsysConvEndPointDetectionPortLow.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysConvEndPointDetectionPortLow.setStatus(_B)
class _EtsysConvEndPointDetectionPortHigh_Type(Integer32):defaultValue=4060;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_EtsysConvEndPointDetectionPortHigh_Type.__name__=_F
_EtsysConvEndPointDetectionPortHigh_Object=MibTableColumn
etsysConvEndPointDetectionPortHigh=_EtsysConvEndPointDetectionPortHigh_Object((1,3,6,1,4,1,5624,1,2,40,1,3,2,1,5),_EtsysConvEndPointDetectionPortHigh_Type())
etsysConvEndPointDetectionPortHigh.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysConvEndPointDetectionPortHigh.setStatus(_B)
class _EtsysConvEndPointDetectionAddrType_Type(InetAddressType):defaultValue=0
_EtsysConvEndPointDetectionAddrType_Type.__name__=_K
_EtsysConvEndPointDetectionAddrType_Object=MibTableColumn
etsysConvEndPointDetectionAddrType=_EtsysConvEndPointDetectionAddrType_Object((1,3,6,1,4,1,5624,1,2,40,1,3,2,1,6),_EtsysConvEndPointDetectionAddrType_Type())
etsysConvEndPointDetectionAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysConvEndPointDetectionAddrType.setStatus(_B)
class _EtsysConvEndPointDetectionAddr_Type(InetAddress):defaultValue=OctetString('')
_EtsysConvEndPointDetectionAddr_Type.__name__=_J
_EtsysConvEndPointDetectionAddr_Object=MibTableColumn
etsysConvEndPointDetectionAddr=_EtsysConvEndPointDetectionAddr_Object((1,3,6,1,4,1,5624,1,2,40,1,3,2,1,7),_EtsysConvEndPointDetectionAddr_Type())
etsysConvEndPointDetectionAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysConvEndPointDetectionAddr.setStatus(_B)
class _EtsysConvEndPointDetectionAddrMaskType_Type(InetAddressType):defaultValue=0
_EtsysConvEndPointDetectionAddrMaskType_Type.__name__=_K
_EtsysConvEndPointDetectionAddrMaskType_Object=MibTableColumn
etsysConvEndPointDetectionAddrMaskType=_EtsysConvEndPointDetectionAddrMaskType_Object((1,3,6,1,4,1,5624,1,2,40,1,3,2,1,8),_EtsysConvEndPointDetectionAddrMaskType_Type())
etsysConvEndPointDetectionAddrMaskType.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysConvEndPointDetectionAddrMaskType.setStatus(_B)
class _EtsysConvEndPointDetectionAddrMask_Type(InetAddress):defaultValue=OctetString('')
_EtsysConvEndPointDetectionAddrMask_Type.__name__=_J
_EtsysConvEndPointDetectionAddrMask_Object=MibTableColumn
etsysConvEndPointDetectionAddrMask=_EtsysConvEndPointDetectionAddrMask_Object((1,3,6,1,4,1,5624,1,2,40,1,3,2,1,9),_EtsysConvEndPointDetectionAddrMask_Type())
etsysConvEndPointDetectionAddrMask.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysConvEndPointDetectionAddrMask.setStatus(_B)
_EtsysConvEndPointDetectionRowStatus_Type=RowStatus
_EtsysConvEndPointDetectionRowStatus_Object=MibTableColumn
etsysConvEndPointDetectionRowStatus=_EtsysConvEndPointDetectionRowStatus_Object((1,3,6,1,4,1,5624,1,2,40,1,3,2,1,10),_EtsysConvEndPointDetectionRowStatus_Type())
etsysConvEndPointDetectionRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysConvEndPointDetectionRowStatus.setStatus(_B)
_EtsysCEPDetectionPortConfigTable_Object=MibTable
etsysCEPDetectionPortConfigTable=_EtsysCEPDetectionPortConfigTable_Object((1,3,6,1,4,1,5624,1,2,40,1,3,3))
if mibBuilder.loadTexts:etsysCEPDetectionPortConfigTable.setStatus(_B)
_EtsysCEPDetectionPortConfigEntry_Object=MibTableRow
etsysCEPDetectionPortConfigEntry=_EtsysCEPDetectionPortConfigEntry_Object((1,3,6,1,4,1,5624,1,2,40,1,3,3,1))
etsysCEPDetectionPortConfigEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:etsysCEPDetectionPortConfigEntry.setStatus(_B)
class _EtsysCEPPortClearUsers_Type(TruthValue):defaultValue=2
_EtsysCEPPortClearUsers_Type.__name__=_e
_EtsysCEPPortClearUsers_Object=MibTableColumn
etsysCEPPortClearUsers=_EtsysCEPPortClearUsers_Object((1,3,6,1,4,1,5624,1,2,40,1,3,3,1,1),_EtsysCEPPortClearUsers_Type())
etsysCEPPortClearUsers.setMaxAccess(_I)
if mibBuilder.loadTexts:etsysCEPPortClearUsers.setStatus(_B)
_EtsysCEPCdpPortConfigTable_Object=MibTable
etsysCEPCdpPortConfigTable=_EtsysCEPCdpPortConfigTable_Object((1,3,6,1,4,1,5624,1,2,40,1,3,4))
if mibBuilder.loadTexts:etsysCEPCdpPortConfigTable.setStatus(_B)
_EtsysCEPCdpPortConfigEntry_Object=MibTableRow
etsysCEPCdpPortConfigEntry=_EtsysCEPCdpPortConfigEntry_Object((1,3,6,1,4,1,5624,1,2,40,1,3,4,1))
etsysCEPCdpPortConfigEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:etsysCEPCdpPortConfigEntry.setStatus(_B)
class _EtsysCEPCiscoCDPVoicePortVlan_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,0),ValueRangeConstraint(1,4094),ValueRangeConstraint(4095,4095))
_EtsysCEPCiscoCDPVoicePortVlan_Type.__name__=_F
_EtsysCEPCiscoCDPVoicePortVlan_Object=MibTableColumn
etsysCEPCiscoCDPVoicePortVlan=_EtsysCEPCiscoCDPVoicePortVlan_Object((1,3,6,1,4,1,5624,1,2,40,1,3,4,1,1),_EtsysCEPCiscoCDPVoicePortVlan_Type())
etsysCEPCiscoCDPVoicePortVlan.setMaxAccess(_I)
if mibBuilder.loadTexts:etsysCEPCiscoCDPVoicePortVlan.setStatus(_B)
_EtsysConvEndPointConformance_ObjectIdentity=ObjectIdentity
etsysConvEndPointConformance=_EtsysConvEndPointConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,40,2))
_EtsysConvEndPointGroups_ObjectIdentity=ObjectIdentity
etsysConvEndPointGroups=_EtsysConvEndPointGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,40,2,1))
_EtsysConvEndPointCompliances_ObjectIdentity=ObjectIdentity
etsysConvEndPointCompliances=_EtsysConvEndPointCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,40,2,2))
etsysConvEndPointGlobalConfigGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,40,2,1,1))
etsysConvEndPointGlobalConfigGroup.setObjects(*((_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:etsysConvEndPointGlobalConfigGroup.setStatus(_C)
etsysConvEndPointConfigGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,40,2,1,2))
etsysConvEndPointConfigGroup.setObjects((_A,_j))
if mibBuilder.loadTexts:etsysConvEndPointConfigGroup.setStatus(_B)
etsysConvEndPointDetectionGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,40,2,1,3))
etsysConvEndPointDetectionGroup.setObjects(*((_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:etsysConvEndPointDetectionGroup.setStatus(_C)
etsysConvEndPointStatusGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,40,2,1,4))
etsysConvEndPointStatusGroup.setObjects(*((_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_L)))
if mibBuilder.loadTexts:etsysConvEndPointStatusGroup.setStatus(_C)
etsysConvEndPointStatusGroup2=ObjectGroup((1,3,6,1,4,1,5624,1,2,40,2,1,5))
etsysConvEndPointStatusGroup2.setObjects(*((_A,_L),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w)))
if mibBuilder.loadTexts:etsysConvEndPointStatusGroup2.setStatus(_B)
etsysConvEndPointDetectionGroup2=ObjectGroup((1,3,6,1,4,1,5624,1,2,40,2,1,6))
etsysConvEndPointDetectionGroup2.setObjects(*((_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_x)))
if mibBuilder.loadTexts:etsysConvEndPointDetectionGroup2.setStatus(_B)
etsysConvEndPointPortConfigGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,40,2,1,7))
etsysConvEndPointPortConfigGroup.setObjects((_A,_y))
if mibBuilder.loadTexts:etsysConvEndPointPortConfigGroup.setStatus(_B)
etsysConvEndPointCiscoVoiceVLANGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,40,2,1,8))
etsysConvEndPointCiscoVoiceVLANGroup.setObjects((_A,_z))
if mibBuilder.loadTexts:etsysConvEndPointCiscoVoiceVLANGroup.setStatus(_B)
etsysConvEndPointGlobalConfigGroup2=ObjectGroup((1,3,6,1,4,1,5624,1,2,40,2,1,9))
etsysConvEndPointGlobalConfigGroup2.setObjects(*((_A,_Q),(_A,_R),(_A,_A0)))
if mibBuilder.loadTexts:etsysConvEndPointGlobalConfigGroup2.setStatus(_B)
etsysConvEndPointCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,40,2,2,1))
etsysConvEndPointCompliance.setObjects(*((_A,_b),(_A,_A1),(_A,_O),(_A,_A2)))
if mibBuilder.loadTexts:etsysConvEndPointCompliance.setStatus(_C)
etsysConvEndPointCompliance2=ModuleCompliance((1,3,6,1,4,1,5624,1,2,40,2,2,2))
etsysConvEndPointCompliance2.setObjects(*((_A,_b),(_A,_c),(_A,_O),(_A,_d)))
if mibBuilder.loadTexts:etsysConvEndPointCompliance2.setStatus(_C)
etsysConvEndPointPortConfigCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,40,2,2,3))
etsysConvEndPointPortConfigCompliance.setObjects((_A,_A3))
if mibBuilder.loadTexts:etsysConvEndPointPortConfigCompliance.setStatus(_B)
etsysConvEndPointCiscoVoiceVLANCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,40,2,2,4))
etsysConvEndPointCiscoVoiceVLANCompliance.setObjects((_A,_A4))
if mibBuilder.loadTexts:etsysConvEndPointCiscoVoiceVLANCompliance.setStatus(_B)
etsysConvEndPointCompliance3=ModuleCompliance((1,3,6,1,4,1,5624,1,2,40,2,2,5))
etsysConvEndPointCompliance3.setObjects(*((_A,_A5),(_A,_c),(_A,_O),(_A,_d)))
if mibBuilder.loadTexts:etsysConvEndPointCompliance3.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ConvEndPointTypes':ConvEndPointTypes,'etsysConvergenceEndPointMIB':etsysConvergenceEndPointMIB,'etsysConvEndPointObjects':etsysConvEndPointObjects,'etsysConvEndPointConfig':etsysConvEndPointConfig,_Q:etsysConvEndPointGlobalConfigEnable,'etsysConvEndPointGlobalConfigTable':etsysConvEndPointGlobalConfigTable,'etsysConvEndPointGlobalConfigEntry':etsysConvEndPointGlobalConfigEntry,_f:etsysConvEndPointGlobalEndPointType,_R:etsysConvEndPointGlobalDefaultPolicyIndex,'etsysConvEndPointProtocolConfigTable':etsysConvEndPointProtocolConfigTable,'etsysConvEndPointProtocolConfigEntry':etsysConvEndPointProtocolConfigEntry,_g:etsysConvEndPointProtocolEndPointType,_j:etsysConvEndPointProtocolEnable,_A0:etsysConvEndPointGlobalConfigAccountEnable,'etsysConvEndPointStatus':etsysConvEndPointStatus,'etsysConvEndPointConnMacTable':etsysConvEndPointConnMacTable,'etsysConvEndPointConnMacEntry':etsysConvEndPointConnMacEntry,_h:etsysConvEndPointConnMacMacAddress,_k:etsysConvEndPointConnMacPortNumber,_l:etsysConvEndPointConnMacEndPointType,_m:etsysConvEndPointConnMacPolicyIndex,_n:etsysConvEndPointConnMacDiscoveryTime,_o:etsysConvEndPointConnMacFirmwareVersion,_p:etsysConvEndPointConnMacInetAddressType,_q:etsysConvEndPointConnMacInetAddress,'etsysConvEndPointConnPortTable':etsysConvEndPointConnPortTable,'etsysConvEndPointConnPortEntry':etsysConvEndPointConnPortEntry,_L:etsysConvEndPointConnPortMacAddress,'etsysCEPConnMacTable':etsysCEPConnMacTable,'etsysCEPConnMacEntry':etsysCEPConnMacEntry,_r:etsysCEPConnMacEndPointType,_s:etsysCEPConnMacPolicyIndex,_t:etsysCEPConnMacDiscoveryTime,_u:etsysCEPConnMacFirmwareVersion,_v:etsysCEPConnMacInetAddressType,_w:etsysCEPConnMacInetAddress,'etsysConvEndPointDetection':etsysConvEndPointDetection,_x:etsysConvEndPointDetectionMaxEntries,'etsysConvEndPointDetectionTable':etsysConvEndPointDetectionTable,'etsysConvEndPointDetectionEntry':etsysConvEndPointDetectionEntry,_i:etsysConvEndPointDetectionRuleIndex,_S:etsysConvEndPointDetectionEndPointType,_T:etsysConvEndPointDetectionProtocol,_U:etsysConvEndPointDetectionPortLow,_V:etsysConvEndPointDetectionPortHigh,_W:etsysConvEndPointDetectionAddrType,_X:etsysConvEndPointDetectionAddr,_Y:etsysConvEndPointDetectionAddrMaskType,_Z:etsysConvEndPointDetectionAddrMask,_a:etsysConvEndPointDetectionRowStatus,'etsysCEPDetectionPortConfigTable':etsysCEPDetectionPortConfigTable,'etsysCEPDetectionPortConfigEntry':etsysCEPDetectionPortConfigEntry,_y:etsysCEPPortClearUsers,'etsysCEPCdpPortConfigTable':etsysCEPCdpPortConfigTable,'etsysCEPCdpPortConfigEntry':etsysCEPCdpPortConfigEntry,_z:etsysCEPCiscoCDPVoicePortVlan,'etsysConvEndPointConformance':etsysConvEndPointConformance,'etsysConvEndPointGroups':etsysConvEndPointGroups,_b:etsysConvEndPointGlobalConfigGroup,_O:etsysConvEndPointConfigGroup,_A2:etsysConvEndPointDetectionGroup,_A1:etsysConvEndPointStatusGroup,_c:etsysConvEndPointStatusGroup2,_d:etsysConvEndPointDetectionGroup2,_A3:etsysConvEndPointPortConfigGroup,_A4:etsysConvEndPointCiscoVoiceVLANGroup,_A5:etsysConvEndPointGlobalConfigGroup2,'etsysConvEndPointCompliances':etsysConvEndPointCompliances,'etsysConvEndPointCompliance':etsysConvEndPointCompliance,'etsysConvEndPointCompliance2':etsysConvEndPointCompliance2,'etsysConvEndPointPortConfigCompliance':etsysConvEndPointPortConfigCompliance,'etsysConvEndPointCiscoVoiceVLANCompliance':etsysConvEndPointCiscoVoiceVLANCompliance,'etsysConvEndPointCompliance3':etsysConvEndPointCompliance3})