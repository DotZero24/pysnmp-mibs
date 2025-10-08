#
# PySNMP MIB module CISCO-DMN-DSG-LOCKLEVEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-DMN-DSG-LOCKLEVEL-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:15:49 2025
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
ciscoDSGLockLevel = ModuleIdentity((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 22))
ciscoDSGLockLevel.setRevisions(('2010-08-30 11:00', '2010-06-28 06:00', '2010-05-24 06:30', '2009-12-20 12:00',))
if mibBuilder.loadTexts: ciscoDSGLockLevel.setLastUpdated('201008301100Z')
if mibBuilder.loadTexts: ciscoDSGLockLevel.setOrganization('Cisco Systems, Inc.')
lockLevel = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 22, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lockLevel.setStatus('current')
lockLevelPWD = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 22, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 4))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lockLevelPWD.setStatus('current')
lockLevelPWDCUR = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 22, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 4))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lockLevelPWDCUR.setStatus('current')
lockLevelPWDNEW = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 22, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 4))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lockLevelPWDNEW.setStatus('current')
lockLevelPWDCONF = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 22, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 4))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lockLevelPWDCONF.setStatus('current')
mibBuilder.exportSymbols("CISCO-DMN-DSG-LOCKLEVEL-MIB", PYSNMP_MODULE_ID=ciscoDSGLockLevel, lockLevelPWDNEW=lockLevelPWDNEW, lockLevelPWD=lockLevelPWD, ciscoDSGLockLevel=ciscoDSGLockLevel, lockLevelPWDCONF=lockLevelPWDCONF, lockLevel=lockLevel, lockLevelPWDCUR=lockLevelPWDCUR)
