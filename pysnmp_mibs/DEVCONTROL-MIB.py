#
# PySNMP MIB module DEVCONTROL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/aperto/DEVCONTROL-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:17:19 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
device, = mibBuilder.importSymbols("ANIROOT-MIB", "device")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("DEVCONTROL-MIB", PYSNMP_MODULE_ID=aniDevControl, aniDevControlUploadState=aniDevControlUploadState, aniDevControlSetFactoryDefaults=aniDevControlSetFactoryDefaults, aniDevControlStartUpload=aniDevControlStartUpload, aniDevControl=aniDevControl, aniDevControlResetDevice=aniDevControlResetDevice)
