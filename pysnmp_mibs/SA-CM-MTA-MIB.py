_F='read-write'
_E='disable'
_D='SnmpAdminString'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_D)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
saCmMta=ModuleIdentity((1,3,6,1,4,1,1429,78,1))
if mibBuilder.loadTexts:saCmMta.setRevisions(('2016-12-23 00:00',))
_Sa_ObjectIdentity=ObjectIdentity
sa=_Sa_ObjectIdentity((1,3,6,1,4,1,1429))
_SaVoip_ObjectIdentity=ObjectIdentity
saVoip=_SaVoip_ObjectIdentity((1,3,6,1,4,1,1429,78))
class _SaCmMtaDevice_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),('enable',1)))
_SaCmMtaDevice_Type.__name__=_B
_SaCmMtaDevice_Object=MibScalar
saCmMtaDevice=_SaCmMtaDevice_Object((1,3,6,1,4,1,1429,78,1,1),_SaCmMtaDevice_Type())
saCmMtaDevice.setMaxAccess(_C)
if mibBuilder.loadTexts:saCmMtaDevice.setStatus(_A)
class _SaCmMtaIpFilters_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('perSpec',0),('openMta',1)))
_SaCmMtaIpFilters_Type.__name__=_B
_SaCmMtaIpFilters_Object=MibScalar
saCmMtaIpFilters=_SaCmMtaIpFilters_Object((1,3,6,1,4,1,1429,78,1,3),_SaCmMtaIpFilters_Type())
saCmMtaIpFilters.setMaxAccess(_F)
if mibBuilder.loadTexts:saCmMtaIpFilters.setStatus(_A)
class _SaCmMtaSidCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,4),ValueRangeConstraint(16,16))
_SaCmMtaSidCount_Type.__name__=_B
_SaCmMtaSidCount_Object=MibScalar
saCmMtaSidCount=_SaCmMtaSidCount_Object((1,3,6,1,4,1,1429,78,1,5),_SaCmMtaSidCount_Type())
saCmMtaSidCount.setMaxAccess(_C)
if mibBuilder.loadTexts:saCmMtaSidCount.setStatus(_A)
class _SaCmMtaProvisioningMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('packetCable',0),('oneConfigFile',1),('twoConfigFilesDHCP',2),('twoConfigFilesSNMP',3),('twoConfigFilesDHCPmacAddress',4),('twoConfigFilesMacAddressOnly',5),('webPage',6)))
_SaCmMtaProvisioningMode_Type.__name__=_B
_SaCmMtaProvisioningMode_Object=MibScalar
saCmMtaProvisioningMode=_SaCmMtaProvisioningMode_Object((1,3,6,1,4,1,1429,78,1,7),_SaCmMtaProvisioningMode_Type())
saCmMtaProvisioningMode.setMaxAccess(_C)
if mibBuilder.loadTexts:saCmMtaProvisioningMode.setStatus(_A)
class _SaCmMtaDhcpPktcOption_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('require122',0),('requireNone',1),('require177',2)))
_SaCmMtaDhcpPktcOption_Type.__name__=_B
_SaCmMtaDhcpPktcOption_Object=MibScalar
saCmMtaDhcpPktcOption=_SaCmMtaDhcpPktcOption_Object((1,3,6,1,4,1,1429,78,1,8),_SaCmMtaDhcpPktcOption_Type())
saCmMtaDhcpPktcOption.setMaxAccess(_C)
if mibBuilder.loadTexts:saCmMtaDhcpPktcOption.setStatus(_A)
class _SaCmMtaRequireTod_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('false',0),('true',1)))
_SaCmMtaRequireTod_Type.__name__=_B
_SaCmMtaRequireTod_Object=MibScalar
saCmMtaRequireTod=_SaCmMtaRequireTod_Object((1,3,6,1,4,1,1429,78,1,10),_SaCmMtaRequireTod_Type())
saCmMtaRequireTod.setMaxAccess(_C)
if mibBuilder.loadTexts:saCmMtaRequireTod.setStatus(_A)
class _SaCmMtaDecryptMtaConfigFile_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),('RSA-CM-cert',2)))
_SaCmMtaDecryptMtaConfigFile_Type.__name__=_B
_SaCmMtaDecryptMtaConfigFile_Object=MibScalar
saCmMtaDecryptMtaConfigFile=_SaCmMtaDecryptMtaConfigFile_Object((1,3,6,1,4,1,1429,78,1,13),_SaCmMtaDecryptMtaConfigFile_Type())
saCmMtaDecryptMtaConfigFile.setMaxAccess(_C)
if mibBuilder.loadTexts:saCmMtaDecryptMtaConfigFile.setStatus(_A)
class _SaCmMtaSwUpgradeControlTimer_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7200))
_SaCmMtaSwUpgradeControlTimer_Type.__name__=_B
_SaCmMtaSwUpgradeControlTimer_Object=MibScalar
saCmMtaSwUpgradeControlTimer=_SaCmMtaSwUpgradeControlTimer_Object((1,3,6,1,4,1,1429,78,1,14),_SaCmMtaSwUpgradeControlTimer_Type())
saCmMtaSwUpgradeControlTimer.setMaxAccess(_F)
if mibBuilder.loadTexts:saCmMtaSwUpgradeControlTimer.setStatus(_A)
if mibBuilder.loadTexts:saCmMtaSwUpgradeControlTimer.setUnits('seconds')
class _SaCmMtaDhcpOptionSixty_Type(SnmpAdminString):defaultValue=OctetString('pktc1.0')
_SaCmMtaDhcpOptionSixty_Type.__name__=_D
_SaCmMtaDhcpOptionSixty_Object=MibScalar
saCmMtaDhcpOptionSixty=_SaCmMtaDhcpOptionSixty_Object((1,3,6,1,4,1,1429,78,1,20),_SaCmMtaDhcpOptionSixty_Type())
saCmMtaDhcpOptionSixty.setMaxAccess(_C)
if mibBuilder.loadTexts:saCmMtaDhcpOptionSixty.setStatus(_A)
class _SaCmMtaProvSnmpSetCommunityString_Type(SnmpAdminString):defaultValue=OctetString('public')
_SaCmMtaProvSnmpSetCommunityString_Type.__name__=_D
_SaCmMtaProvSnmpSetCommunityString_Object=MibScalar
saCmMtaProvSnmpSetCommunityString=_SaCmMtaProvSnmpSetCommunityString_Object((1,3,6,1,4,1,1429,78,1,26),_SaCmMtaProvSnmpSetCommunityString_Type())
saCmMtaProvSnmpSetCommunityString.setMaxAccess(_C)
if mibBuilder.loadTexts:saCmMtaProvSnmpSetCommunityString.setStatus(_A)
_SaCmMtaCliAccess_ObjectIdentity=ObjectIdentity
saCmMtaCliAccess=_SaCmMtaCliAccess_ObjectIdentity((1,3,6,1,4,1,1429,78,1,1001))
class _SaCmMtaCliAccessPasswordType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('plain',0),('md5',1),('pod',2)))
_SaCmMtaCliAccessPasswordType_Type.__name__=_B
_SaCmMtaCliAccessPasswordType_Object=MibScalar
saCmMtaCliAccessPasswordType=_SaCmMtaCliAccessPasswordType_Object((1,3,6,1,4,1,1429,78,1,1001,5),_SaCmMtaCliAccessPasswordType_Type())
saCmMtaCliAccessPasswordType.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:saCmMtaCliAccessPasswordType.setStatus(_A)
mibBuilder.exportSymbols('SA-CM-MTA-MIB',**{'sa':sa,'saVoip':saVoip,'saCmMta':saCmMta,'saCmMtaDevice':saCmMtaDevice,'saCmMtaIpFilters':saCmMtaIpFilters,'saCmMtaSidCount':saCmMtaSidCount,'saCmMtaProvisioningMode':saCmMtaProvisioningMode,'saCmMtaDhcpPktcOption':saCmMtaDhcpPktcOption,'saCmMtaRequireTod':saCmMtaRequireTod,'saCmMtaDecryptMtaConfigFile':saCmMtaDecryptMtaConfigFile,'saCmMtaSwUpgradeControlTimer':saCmMtaSwUpgradeControlTimer,'saCmMtaDhcpOptionSixty':saCmMtaDhcpOptionSixty,'saCmMtaProvSnmpSetCommunityString':saCmMtaProvSnmpSetCommunityString,'saCmMtaCliAccess':saCmMtaCliAccess,'saCmMtaCliAccessPasswordType':saCmMtaCliAccessPasswordType})