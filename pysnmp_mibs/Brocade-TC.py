#
# PySNMP MIB module Brocade-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/brocade/Brocade-TC
# Produced by pysmi-1.1.12 at Thu Sep 11 10:07:06 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
bcsiModules, = mibBuilder.importSymbols("Brocade-REG-MIB", "bcsiModules")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Integer32, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, TimeTicks, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Integer32", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "TimeTicks", "Bits", "IpAddress")
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

mibBuilder.exportSymbols("Brocade-TC", SwNbIndex=SwNbIndex, PYSNMP_MODULE_ID=bcsiModuleTC, SwTrunkMaster=SwTrunkMaster, SwDomainIndex=SwDomainIndex, SwPortIndex=SwPortIndex, bcsiModuleTC=bcsiModuleTC, FcWwn=FcWwn, SwSensorIndex=SwSensorIndex)
