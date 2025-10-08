#
# PySNMP MIB module CISCO-DMN-DSG-SESSIONCONTROL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-DMN-DSG-SESSIONCONTROL-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:11:54 2025
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
ciscoDSGSessionControl = ModuleIdentity((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 6))
ciscoDSGSessionControl.setRevisions(('2010-08-30 11:00', '2009-11-22 15:00',))
if mibBuilder.loadTexts: ciscoDSGSessionControl.setLastUpdated('201008301100Z')
if mibBuilder.loadTexts: ciscoDSGSessionControl.setOrganization('Cisco Systems, Inc.')
sessionControlOpen = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 6, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("open", 1), ("writeOnly", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sessionControlOpen.setStatus('current')
sessionControlClose = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 6, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("saveAndClose", 1), ("ignoreAndClose", 2), ("writeOnly", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sessionControlClose.setStatus('current')
sessionControlStatus = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 6, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("open", 1), ("closed", 2), ("expired", 3), ("openWithInvalidConfig", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sessionControlStatus.setStatus('current')
sessionControlValidateStatus = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 6, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 250))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sessionControlValidateStatus.setStatus('current')
mibBuilder.exportSymbols("CISCO-DMN-DSG-SESSIONCONTROL-MIB", sessionControlClose=sessionControlClose, sessionControlValidateStatus=sessionControlValidateStatus, sessionControlStatus=sessionControlStatus, sessionControlOpen=sessionControlOpen, PYSNMP_MODULE_ID=ciscoDSGSessionControl, ciscoDSGSessionControl=ciscoDSGSessionControl)
