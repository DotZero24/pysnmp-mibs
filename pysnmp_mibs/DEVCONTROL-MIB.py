#
# PySNMP MIB module DEVCONTROL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/aperto/DEVCONTROL-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:07:55 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
device, = mibBuilder.importSymbols("ANIROOT-MIB", "device")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
aniDevControl = ModuleIdentity((1, 3, 6, 1, 4, 1, 4325, 2, 4))
if mibBuilder.loadTexts: aniDevControl.setLastUpdated('0105091130Z')
if mibBuilder.loadTexts: aniDevControl.setOrganization('Aperto Networks')
aniDevControlResetDevice = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 4, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aniDevControlResetDevice.setStatus('current')
aniDevControlSetFactoryDefaults = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 4, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniDevControlSetFactoryDefaults.setStatus('current')
aniDevControlStartUpload = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 4, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aniDevControlStartUpload.setStatus('current')
aniDevControlUploadState = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 4, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("successful", 1), ("failed", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniDevControlUploadState.setStatus('current')
mibBuilder.exportSymbols("DEVCONTROL-MIB", aniDevControlStartUpload=aniDevControlStartUpload, aniDevControlResetDevice=aniDevControlResetDevice, aniDevControlUploadState=aniDevControlUploadState, PYSNMP_MODULE_ID=aniDevControl, aniDevControl=aniDevControl, aniDevControlSetFactoryDefaults=aniDevControlSetFactoryDefaults)
