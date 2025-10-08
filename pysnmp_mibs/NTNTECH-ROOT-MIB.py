#
# PySNMP MIB module NTNTECH-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/zhone/NTNTECH-ROOT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:09:13 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ntntechRootMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8059))
ntntechRootMIB.setRevisions(('1902-08-28 11:57', '1902-10-22 02:00', '1904-10-11 01:01', '1904-11-17 10:09',))
if mibBuilder.loadTexts: ntntechRootMIB.setLastUpdated('0411170200Z')
if mibBuilder.loadTexts: ntntechRootMIB.setOrganization('Paradyne Corporation')
class NtnIpAddress(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x:2x:3x:4x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class NtnDefaultGateway(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x:2x:3x:4x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class NtnSubnetMask(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x:2x:3x:4x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class NtnDisplayString(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 127)

class NtnMacAddress(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class NtnTimeTicks(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class NtnCounter32(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class NtnGauge32(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class NtnTruthValue(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("yes", 1), ("no", 2))

ntntechNamingTree = MibIdentifier((1, 3, 6, 1, 4, 1, 8059, 1))
ntntechChassis = MibIdentifier((1, 3, 6, 1, 4, 1, 8059, 1, 1))
ntntechChassisConfigurationMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1))
ntntechChassisStatusMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 8059, 1, 1, 2))
ntntechInterfaceModule = MibIdentifier((1, 3, 6, 1, 4, 1, 8059, 1, 2))
ntntechInterfaceModuleConfigurationMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 8059, 1, 2, 1))
ntntechInterfaceModuleStatusMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 8059, 1, 2, 2))
ntntechQoSMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 8059, 1, 2, 3))
ntntechNMSTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 8059, 1, 3))
ntntechNMSTrapsMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 8059, 1, 3, 1))
ntntechSystemObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8059, 1, 4))
ntntechSystemObjectsIdentifierMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 8059, 1, 4, 1))
mibBuilder.exportSymbols("NTNTECH-ROOT-MIB", NtnCounter32=NtnCounter32, PYSNMP_MODULE_ID=ntntechRootMIB, ntntechInterfaceModuleStatusMIB=ntntechInterfaceModuleStatusMIB, ntntechRootMIB=ntntechRootMIB, ntntechNamingTree=ntntechNamingTree, NtnTimeTicks=NtnTimeTicks, NtnTruthValue=NtnTruthValue, NtnMacAddress=NtnMacAddress, ntntechQoSMIB=ntntechQoSMIB, ntntechChassisStatusMIB=ntntechChassisStatusMIB, ntntechNMSTrapsMIB=ntntechNMSTrapsMIB, ntntechInterfaceModuleConfigurationMIB=ntntechInterfaceModuleConfigurationMIB, NtnDisplayString=NtnDisplayString, NtnSubnetMask=NtnSubnetMask, ntntechChassisConfigurationMIB=ntntechChassisConfigurationMIB, NtnIpAddress=NtnIpAddress, NtnDefaultGateway=NtnDefaultGateway, ntntechChassis=ntntechChassis, NtnGauge32=NtnGauge32, ntntechSystemObjects=ntntechSystemObjects, ntntechInterfaceModule=ntntechInterfaceModule, ntntechSystemObjectsIdentifierMIB=ntntechSystemObjectsIdentifierMIB, ntntechNMSTraps=ntntechNMSTraps)
