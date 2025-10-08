#
# PySNMP MIB module CISCO-DMN-DSG-SESSIONCONTROL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-DMN-DSG-SESSIONCONTROL-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:24:08 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoDSGUtilities, = mibBuilder.importSymbols("CISCO-DMN-DSG-ROOT-MIB", "ciscoDSGUtilities")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("CISCO-DMN-DSG-SESSIONCONTROL-MIB", sessionControlOpen=sessionControlOpen, sessionControlStatus=sessionControlStatus, PYSNMP_MODULE_ID=ciscoDSGSessionControl, ciscoDSGSessionControl=ciscoDSGSessionControl, sessionControlValidateStatus=sessionControlValidateStatus, sessionControlClose=sessionControlClose)
