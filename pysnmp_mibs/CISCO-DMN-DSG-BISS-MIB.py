#
# PySNMP MIB module CISCO-DMN-DSG-BISS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-DMN-DSG-BISS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:14:25 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoDSGUtilities, = mibBuilder.importSymbols("CISCO-DMN-DSG-ROOT-MIB", "ciscoDSGUtilities")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoDSGBISS = ModuleIdentity((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 38))
ciscoDSGBISS.setRevisions(('2010-08-02 07:00',))
if mibBuilder.loadTexts: ciscoDSGBISS.setLastUpdated('201008020700Z')
if mibBuilder.loadTexts: ciscoDSGBISS.setOrganization('Cisco Systems, Inc.')
bissMode = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 38, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("mode1", 1), ("modeE", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bissMode.setStatus('current')
bissMode1SessionWord = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 38, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 13))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bissMode1SessionWord.setStatus('current')
bissModeESessionWord = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 38, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 17))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bissModeESessionWord.setStatus('current')
bissModeEInjectedId = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 38, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bissModeEInjectedId.setStatus('current')
mibBuilder.exportSymbols("CISCO-DMN-DSG-BISS-MIB", PYSNMP_MODULE_ID=ciscoDSGBISS, bissModeESessionWord=bissModeESessionWord, bissModeEInjectedId=bissModeEInjectedId, ciscoDSGBISS=ciscoDSGBISS, bissMode=bissMode, bissMode1SessionWord=bissMode1SessionWord)
