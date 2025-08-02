_L='snmpAgtConfigGroup'
_K='snmpAgtSourceIpConfig'
_J='snmpAgtSourceIp'
_I='snmpAgtCommunityMode'
_H='snmpAgtSecurityLevel'
_G='deprecated'
_F='read-only'
_E='read-write'
_D='SnmpAgtSecurityLevel'
_C='Integer32'
_B='ALCATEL-ENT1-SNMP-AGENT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
softentIND1SnmpAgt,=mibBuilder.importSymbols('ALCATEL-ENT1-BASE','softentIND1SnmpAgt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
alcatelIND1SNMPAgentMIB=ModuleIdentity((1,3,6,1,4,1,6486,801,1,2,1,1,1))
if mibBuilder.loadTexts:alcatelIND1SNMPAgentMIB.setRevisions(('2014-07-15 00:00',))
class SnmpAgtSecurityLevel(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('noSec',1),('authSet',2),('authAll',3),('privSet',4),('privAll',5),('trapOnly',6)))
_AlcatelIND1SNMPAgentMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1SNMPAgentMIBObjects=_AlcatelIND1SNMPAgentMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,1,1,1))
if mibBuilder.loadTexts:alcatelIND1SNMPAgentMIBObjects.setStatus(_A)
_SnmpAgtConfig_ObjectIdentity=ObjectIdentity
snmpAgtConfig=_SnmpAgtConfig_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,1,1,1,1))
class _SnmpAgtSecurityLevel_Type(SnmpAgtSecurityLevel):defaultValue=1
_SnmpAgtSecurityLevel_Type.__name__=_D
_SnmpAgtSecurityLevel_Object=MibScalar
snmpAgtSecurityLevel=_SnmpAgtSecurityLevel_Object((1,3,6,1,4,1,6486,801,1,2,1,1,1,1,1,1),_SnmpAgtSecurityLevel_Type())
snmpAgtSecurityLevel.setMaxAccess(_E)
if mibBuilder.loadTexts:snmpAgtSecurityLevel.setStatus(_A)
class _SnmpAgtCommunityMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_SnmpAgtCommunityMode_Type.__name__=_C
_SnmpAgtCommunityMode_Object=MibScalar
snmpAgtCommunityMode=_SnmpAgtCommunityMode_Object((1,3,6,1,4,1,6486,801,1,2,1,1,1,1,1,2),_SnmpAgtCommunityMode_Type())
snmpAgtCommunityMode.setMaxAccess(_E)
if mibBuilder.loadTexts:snmpAgtCommunityMode.setStatus(_A)
_SnmpAgtCtlFiles_ObjectIdentity=ObjectIdentity
snmpAgtCtlFiles=_SnmpAgtCtlFiles_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,1,1,1,3))
if mibBuilder.loadTexts:snmpAgtCtlFiles.setStatus(_A)
class _SnmpAgtSourceIpConfig_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('default',1),('noLoopback0',2),('ipInterface',3)))
_SnmpAgtSourceIpConfig_Type.__name__=_C
_SnmpAgtSourceIpConfig_Object=MibScalar
snmpAgtSourceIpConfig=_SnmpAgtSourceIpConfig_Object((1,3,6,1,4,1,6486,801,1,2,1,1,1,1,4),_SnmpAgtSourceIpConfig_Type())
snmpAgtSourceIpConfig.setMaxAccess(_F)
if mibBuilder.loadTexts:snmpAgtSourceIpConfig.setStatus(_G)
_SnmpAgtSourceIp_Type=IpAddress
_SnmpAgtSourceIp_Object=MibScalar
snmpAgtSourceIp=_SnmpAgtSourceIp_Object((1,3,6,1,4,1,6486,801,1,2,1,1,1,1,5),_SnmpAgtSourceIp_Type())
snmpAgtSourceIp.setMaxAccess(_F)
if mibBuilder.loadTexts:snmpAgtSourceIp.setStatus(_G)
_AlcatelIND1SNMPAgentMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1SNMPAgentMIBConformance=_AlcatelIND1SNMPAgentMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,1,1,2))
if mibBuilder.loadTexts:alcatelIND1SNMPAgentMIBConformance.setStatus(_A)
_AlcatelIND1SNMPAgentMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1SNMPAgentMIBGroups=_AlcatelIND1SNMPAgentMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,1,1,2,1))
if mibBuilder.loadTexts:alcatelIND1SNMPAgentMIBGroups.setStatus(_A)
_AlcatelIND1SNMPAgentMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1SNMPAgentMIBCompliances=_AlcatelIND1SNMPAgentMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,1,1,2,2))
if mibBuilder.loadTexts:alcatelIND1SNMPAgentMIBCompliances.setStatus(_A)
snmpAgtConfigGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,1,1,2,1,1))
snmpAgtConfigGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:snmpAgtConfigGroup.setStatus(_A)
alcatelIND1SNMPAgentMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6486,801,1,2,1,1,1,2,2,1))
alcatelIND1SNMPAgentMIBCompliance.setObjects((_B,_L))
if mibBuilder.loadTexts:alcatelIND1SNMPAgentMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_D:SnmpAgtSecurityLevel,'alcatelIND1SNMPAgentMIB':alcatelIND1SNMPAgentMIB,'alcatelIND1SNMPAgentMIBObjects':alcatelIND1SNMPAgentMIBObjects,'snmpAgtConfig':snmpAgtConfig,_H:snmpAgtSecurityLevel,_I:snmpAgtCommunityMode,'snmpAgtCtlFiles':snmpAgtCtlFiles,_K:snmpAgtSourceIpConfig,_J:snmpAgtSourceIp,'alcatelIND1SNMPAgentMIBConformance':alcatelIND1SNMPAgentMIBConformance,'alcatelIND1SNMPAgentMIBGroups':alcatelIND1SNMPAgentMIBGroups,_L:snmpAgtConfigGroup,'alcatelIND1SNMPAgentMIBCompliances':alcatelIND1SNMPAgentMIBCompliances,'alcatelIND1SNMPAgentMIBCompliance':alcatelIND1SNMPAgentMIBCompliance})