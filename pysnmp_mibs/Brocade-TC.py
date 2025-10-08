#
# PySNMP MIB module Brocade-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/brocade/Brocade-TC
# Produced by pysmi-1.1.12 at Wed Oct  8 10:15:43 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
bcsiModules, = mibBuilder.importSymbols("Brocade-REG-MIB", "bcsiModules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
bcsiModuleTC = ModuleIdentity((1, 3, 6, 1, 4, 1, 1588, 3, 1, 2))
bcsiModuleTC.setRevisions(('2003-01-13 14:30',))
if mibBuilder.loadTexts: bcsiModuleTC.setLastUpdated('200301131430Z')
if mibBuilder.loadTexts: bcsiModuleTC.setOrganization('Brocade Communications Systems, Inc.,')
class FcWwn(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class SwDomainIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 239)

class SwNbIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2048)

class SwSensorIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 1024)

class SwPortIndex(TextualConvention, Integer32):
    status = 'current'

class SwTrunkMaster(TextualConvention, Integer32):
    status = 'current'

mibBuilder.exportSymbols("Brocade-TC", SwDomainIndex=SwDomainIndex, SwTrunkMaster=SwTrunkMaster, SwSensorIndex=SwSensorIndex, PYSNMP_MODULE_ID=bcsiModuleTC, bcsiModuleTC=bcsiModuleTC, SwPortIndex=SwPortIndex, SwNbIndex=SwNbIndex, FcWwn=FcWwn)
