#
# PySNMP MIB module CISCO-DYNAMIC-TEMPLATE-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-DYNAMIC-TEMPLATE-TC-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:16:11 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoDynamicTemplateTcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 783))
ciscoDynamicTemplateTcMIB.setRevisions(('2007-09-06 00:00',))
if mibBuilder.loadTexts: ciscoDynamicTemplateTcMIB.setLastUpdated('201201270000Z')
if mibBuilder.loadTexts: ciscoDynamicTemplateTcMIB.setOrganization('Cisco Systems, Inc.')
class DynamicTemplateName(TextualConvention, OctetString):
    reference = "D. Harrington, R. Resuhn, B. Wijnen, 'An Architecture for Describing Simple Network Management Protocol (SNMP) Management Frameworks', RFC-3411, December 2002."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 64)

class DynamicTemplateType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("other", 1), ("derived", 2), ("ppp", 3), ("ethernet", 4), ("ipSubscriber", 5), ("service", 6))

class DynamicTemplateTargetType(TextualConvention, Integer32):
    reference = "K. McCloghrie and F. Kastenholtz, 'The Interfaces Group MIB', RFC-2863, June 2000."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("other", 1), ("interface", 2))

class DynamicTemplateTargetId(TextualConvention, OctetString):
    reference = "K. McCloghrie and F. Kastenholtz, 'The Interfaces Group MIB', RFC-2863, June 2000."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 20)

mibBuilder.exportSymbols("CISCO-DYNAMIC-TEMPLATE-TC-MIB", PYSNMP_MODULE_ID=ciscoDynamicTemplateTcMIB, DynamicTemplateTargetId=DynamicTemplateTargetId, DynamicTemplateTargetType=DynamicTemplateTargetType, DynamicTemplateName=DynamicTemplateName, ciscoDynamicTemplateTcMIB=ciscoDynamicTemplateTcMIB, DynamicTemplateType=DynamicTemplateType)
