#
# PySNMP MIB module NTNTECH-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/zhone/NTNTECH-ROOT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:19:55 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("NTNTECH-ROOT-MIB", ntntechRootMIB=ntntechRootMIB, NtnCounter32=NtnCounter32, NtnSubnetMask=NtnSubnetMask, ntntechQoSMIB=ntntechQoSMIB, ntntechNamingTree=ntntechNamingTree, NtnTimeTicks=NtnTimeTicks, ntntechNMSTraps=ntntechNMSTraps, ntntechNMSTrapsMIB=ntntechNMSTrapsMIB, ntntechChassisStatusMIB=ntntechChassisStatusMIB, ntntechSystemObjectsIdentifierMIB=ntntechSystemObjectsIdentifierMIB, ntntechSystemObjects=ntntechSystemObjects, NtnMacAddress=NtnMacAddress, ntntechInterfaceModuleConfigurationMIB=ntntechInterfaceModuleConfigurationMIB, ntntechInterfaceModuleStatusMIB=ntntechInterfaceModuleStatusMIB, ntntechChassisConfigurationMIB=ntntechChassisConfigurationMIB, NtnTruthValue=NtnTruthValue, NtnIpAddress=NtnIpAddress, NtnGauge32=NtnGauge32, NtnDefaultGateway=NtnDefaultGateway, ntntechInterfaceModule=ntntechInterfaceModule, ntntechChassis=ntntechChassis, NtnDisplayString=NtnDisplayString, PYSNMP_MODULE_ID=ntntechRootMIB)
