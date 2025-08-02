_B='1x:2x:3x:4x'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ntntechRootMIB=ModuleIdentity((1,3,6,1,4,1,8059))
if mibBuilder.loadTexts:ntntechRootMIB.setRevisions(('1902-08-28 11:57','1902-10-22 02:00','1904-10-11 01:01','1904-11-17 10:09'))
class NtnIpAddress(TextualConvention,OctetString):status=_A;displayHint=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
class NtnDefaultGateway(TextualConvention,OctetString):status=_A;displayHint=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
class NtnSubnetMask(TextualConvention,OctetString):status=_A;displayHint=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
class NtnDisplayString(TextualConvention,OctetString):status=_A;displayHint='255a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
class NtnMacAddress(TextualConvention,OctetString):status=_A;displayHint='1x:';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
class NtnTimeTicks(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
class NtnCounter32(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
class NtnGauge32(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
class NtnTruthValue(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_NtntechNamingTree_ObjectIdentity=ObjectIdentity
ntntechNamingTree=_NtntechNamingTree_ObjectIdentity((1,3,6,1,4,1,8059,1))
_NtntechChassis_ObjectIdentity=ObjectIdentity
ntntechChassis=_NtntechChassis_ObjectIdentity((1,3,6,1,4,1,8059,1,1))
_NtntechChassisConfigurationMIB_ObjectIdentity=ObjectIdentity
ntntechChassisConfigurationMIB=_NtntechChassisConfigurationMIB_ObjectIdentity((1,3,6,1,4,1,8059,1,1,1))
_NtntechChassisStatusMIB_ObjectIdentity=ObjectIdentity
ntntechChassisStatusMIB=_NtntechChassisStatusMIB_ObjectIdentity((1,3,6,1,4,1,8059,1,1,2))
_NtntechInterfaceModule_ObjectIdentity=ObjectIdentity
ntntechInterfaceModule=_NtntechInterfaceModule_ObjectIdentity((1,3,6,1,4,1,8059,1,2))
_NtntechInterfaceModuleConfigurationMIB_ObjectIdentity=ObjectIdentity
ntntechInterfaceModuleConfigurationMIB=_NtntechInterfaceModuleConfigurationMIB_ObjectIdentity((1,3,6,1,4,1,8059,1,2,1))
_NtntechInterfaceModuleStatusMIB_ObjectIdentity=ObjectIdentity
ntntechInterfaceModuleStatusMIB=_NtntechInterfaceModuleStatusMIB_ObjectIdentity((1,3,6,1,4,1,8059,1,2,2))
_NtntechQoSMIB_ObjectIdentity=ObjectIdentity
ntntechQoSMIB=_NtntechQoSMIB_ObjectIdentity((1,3,6,1,4,1,8059,1,2,3))
_NtntechNMSTraps_ObjectIdentity=ObjectIdentity
ntntechNMSTraps=_NtntechNMSTraps_ObjectIdentity((1,3,6,1,4,1,8059,1,3))
_NtntechNMSTrapsMIB_ObjectIdentity=ObjectIdentity
ntntechNMSTrapsMIB=_NtntechNMSTrapsMIB_ObjectIdentity((1,3,6,1,4,1,8059,1,3,1))
_NtntechSystemObjects_ObjectIdentity=ObjectIdentity
ntntechSystemObjects=_NtntechSystemObjects_ObjectIdentity((1,3,6,1,4,1,8059,1,4))
_NtntechSystemObjectsIdentifierMIB_ObjectIdentity=ObjectIdentity
ntntechSystemObjectsIdentifierMIB=_NtntechSystemObjectsIdentifierMIB_ObjectIdentity((1,3,6,1,4,1,8059,1,4,1))
mibBuilder.exportSymbols('NTNTECH-ROOT-MIB',**{'NtnIpAddress':NtnIpAddress,'NtnDefaultGateway':NtnDefaultGateway,'NtnSubnetMask':NtnSubnetMask,'NtnDisplayString':NtnDisplayString,'NtnMacAddress':NtnMacAddress,'NtnTimeTicks':NtnTimeTicks,'NtnCounter32':NtnCounter32,'NtnGauge32':NtnGauge32,'NtnTruthValue':NtnTruthValue,'ntntechRootMIB':ntntechRootMIB,'ntntechNamingTree':ntntechNamingTree,'ntntechChassis':ntntechChassis,'ntntechChassisConfigurationMIB':ntntechChassisConfigurationMIB,'ntntechChassisStatusMIB':ntntechChassisStatusMIB,'ntntechInterfaceModule':ntntechInterfaceModule,'ntntechInterfaceModuleConfigurationMIB':ntntechInterfaceModuleConfigurationMIB,'ntntechInterfaceModuleStatusMIB':ntntechInterfaceModuleStatusMIB,'ntntechQoSMIB':ntntechQoSMIB,'ntntechNMSTraps':ntntechNMSTraps,'ntntechNMSTrapsMIB':ntntechNMSTrapsMIB,'ntntechSystemObjects':ntntechSystemObjects,'ntntechSystemObjectsIdentifierMIB':ntntechSystemObjectsIdentifierMIB})