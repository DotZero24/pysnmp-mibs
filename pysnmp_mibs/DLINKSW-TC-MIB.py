#
# PySNMP MIB module DLINKSW-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/d-link/DLINKSW-TC-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:34:03 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dlinkIndustrialCommon, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlinkIndustrialCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dlinkSwTextualConvention = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 14, 1))
dlinkSwTextualConvention.setRevisions(('2012-11-19 00:00',))
if mibBuilder.loadTexts: dlinkSwTextualConvention.setLastUpdated('201211190000Z')
if mibBuilder.loadTexts: dlinkSwTextualConvention.setOrganization('D-Link Corp.')
class DlinkTrigger(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("none", 1), ("action", 2))

class Dlink2kVlanList(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

mibBuilder.exportSymbols("DLINKSW-TC-MIB", PYSNMP_MODULE_ID=dlinkSwTextualConvention, Dlink2kVlanList=Dlink2kVlanList, DlinkTrigger=DlinkTrigger, dlinkSwTextualConvention=dlinkSwTextualConvention)
