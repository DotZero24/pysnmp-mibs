#
# PySNMP MIB module BIANCA-BRICK-HIDDENVPN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/bintec/BIANCA-BRICK-HIDDENVPN-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:57:23 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Integer32, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, TimeTicks, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Integer32", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "TimeTicks", "Bits", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
bintec = MibIdentifier((1, 3, 6, 1, 4, 1, 272))
bibo = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4))
admin = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 1))
biboAdmLed = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 253))
biboAdmLedStatus = MibScalar((1, 3, 6, 1, 4, 1, 272, 253, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("off", 1), ("on", 2), ("blink", 3), ("flash", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: biboAdmLedStatus.setStatus('mandatory')
biboAdmLedMgmt = MibScalar((1, 3, 6, 1, 4, 1, 272, 253, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("off", 1), ("on", 2), ("blink", 3), ("flash", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: biboAdmLedMgmt.setStatus('mandatory')
biboAdmLedHA = MibScalar((1, 3, 6, 1, 4, 1, 272, 253, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("off", 1), ("on", 2), ("blink", 3), ("flash", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: biboAdmLedHA.setStatus('mandatory')
biboAdmLedInternet = MibScalar((1, 3, 6, 1, 4, 1, 272, 253, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("off", 1), ("on", 2), ("blink", 3), ("flash", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: biboAdmLedInternet.setStatus('mandatory')
biboAdmLedSwitch = MibScalar((1, 3, 6, 1, 4, 1, 272, 253, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("off", 1), ("on", 2), ("blink", 3), ("linkact", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: biboAdmLedSwitch.setStatus('mandatory')
biboAdmLedMeter = MibScalar((1, 3, 6, 1, 4, 1, 272, 253, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: biboAdmLedMeter.setStatus('mandatory')
mibBuilder.exportSymbols("BIANCA-BRICK-HIDDENVPN-MIB", biboAdmLedStatus=biboAdmLedStatus, biboAdmLedHA=biboAdmLedHA, biboAdmLedMeter=biboAdmLedMeter, biboAdmLedInternet=biboAdmLedInternet, bintec=bintec, bibo=bibo, biboAdmLedSwitch=biboAdmLedSwitch, biboAdmLedMgmt=biboAdmLedMgmt, admin=admin, biboAdmLed=biboAdmLed)
