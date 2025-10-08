#
# PySNMP MIB module AUTOMATION-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/siemens/AUTOMATION-TC
# Produced by pysmi-1.1.12 at Wed Oct  8 10:17:30 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
automationModules, = mibBuilder.importSymbols("AUTOMATION-SMI", "automationModules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
automationTcModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 4329, 6, 2, 1))
automationTcModule.setRevisions(('2013-06-30 00:00', '2012-09-19 00:00', '2012-07-27 00:00', '2008-11-10 00:00', '2008-04-29 00:00', '2005-01-12 00:00',))
if mibBuilder.loadTexts: automationTcModule.setLastUpdated('201306300000Z')
if mibBuilder.loadTexts: automationTcModule.setOrganization('Siemens AG')
class AutomationOrderNumberTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(16, 32)

class AutomationSerialNumberTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(32, 32)
    fixedLength = 32

class AutomationVersionNumberTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class AutomationMacAddressTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class AutomationIpAddressTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1a'

class AutomationStatusTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("invalid", 0), ("enable", 1), ("disable", 2))

class AutomationTriggerTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("trigger", 1), ("notTriggered", 2))

class AutomationFunctionStringTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(32, 32)
    fixedLength = 32

class AutomationLocationStringTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '22a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(22, 22)
    fixedLength = 22

mibBuilder.exportSymbols("AUTOMATION-TC", AutomationOrderNumberTC=AutomationOrderNumberTC, AutomationFunctionStringTC=AutomationFunctionStringTC, automationTcModule=automationTcModule, PYSNMP_MODULE_ID=automationTcModule, AutomationVersionNumberTC=AutomationVersionNumberTC, AutomationMacAddressTC=AutomationMacAddressTC, AutomationSerialNumberTC=AutomationSerialNumberTC, AutomationIpAddressTC=AutomationIpAddressTC, AutomationTriggerTC=AutomationTriggerTC, AutomationStatusTC=AutomationStatusTC, AutomationLocationStringTC=AutomationLocationStringTC)
