#
# PySNMP MIB module CISCO-DMN-DSG-FPUI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-DMN-DSG-FPUI-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:12:41 2025
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
ciscoDSGFPUI = ModuleIdentity((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 24))
ciscoDSGFPUI.setRevisions(('2010-08-30 11:00', '2010-03-22 05:00', '2009-12-20 12:00',))
if mibBuilder.loadTexts: ciscoDSGFPUI.setLastUpdated('201008301100Z')
if mibBuilder.loadTexts: ciscoDSGFPUI.setOrganization('Cisco Systems, Inc.')
fpuiKBLock = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 24, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fpuiKBLock.setStatus('current')
fpuiKBLockTimeout = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 24, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1800))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fpuiKBLockTimeout.setStatus('current')
fpuiLCDContrast = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 24, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 30))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fpuiLCDContrast.setStatus('current')
fpuiAWReminder = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 24, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fpuiAWReminder.setStatus('current')
mibBuilder.exportSymbols("CISCO-DMN-DSG-FPUI-MIB", fpuiKBLockTimeout=fpuiKBLockTimeout, PYSNMP_MODULE_ID=ciscoDSGFPUI, fpuiAWReminder=fpuiAWReminder, ciscoDSGFPUI=ciscoDSGFPUI, fpuiLCDContrast=fpuiLCDContrast, fpuiKBLock=fpuiKBLock)
