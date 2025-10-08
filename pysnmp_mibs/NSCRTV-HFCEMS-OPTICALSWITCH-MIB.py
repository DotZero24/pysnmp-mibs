#
# PySNMP MIB module NSCRTV-HFCEMS-OPTICALSWITCH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/nscrtv/NSCRTV-HFCEMS-OPTICALSWITCH-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:43:51 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
commonNELogicalID, commonPhysAddress = mibBuilder.importSymbols("NSCRTV-HFCEMS-COMMON-MIB", "commonNELogicalID", "commonPhysAddress")
nscrtvHFCemsTree, = mibBuilder.importSymbols("NSCRTV-ROOT", "nscrtvHFCemsTree")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
osIdent = MibIdentifier((1, 3, 6, 1, 4, 1, 17409, 1, 8686))
osVendorOID = MibScalar((1, 3, 6, 1, 4, 1, 17409, 1, 8686, 1), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: osVendorOID.setStatus('optional')
osWavelength = MibScalar((1, 3, 6, 1, 4, 1, 17409, 1, 8686, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("1310nm", 1), ("1490nm", 2), ("1550nm", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: osWavelength.setStatus('mandatory')
osAutoControl = MibScalar((1, 3, 6, 1, 4, 1, 17409, 1, 8686, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: osAutoControl.setStatus('mandatory')
osCurrentWorkChannel = MibScalar((1, 3, 6, 1, 4, 1, 17409, 1, 8686, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("A", 1), ("B", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: osCurrentWorkChannel.setStatus('mandatory')
osSwitchReference = MibScalar((1, 3, 6, 1, 4, 1, 17409, 1, 8686, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-200, 300))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: osSwitchReference.setStatus('mandatory')
osInputOpticalPowerA = MibScalar((1, 3, 6, 1, 4, 1, 17409, 1, 8686, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-32768, 32767))).setMaxAccess("readonly")
if mibBuilder.loadTexts: osInputOpticalPowerA.setStatus('mandatory')
osInputOpticalPowerB = MibScalar((1, 3, 6, 1, 4, 1, 17409, 1, 8686, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-32768, 32767))).setMaxAccess("readonly")
if mibBuilder.loadTexts: osInputOpticalPowerB.setStatus('mandatory')
osSwitchEvent = NotificationType((1, 3, 6, 1, 4, 1, 17409, 1) + (0,8686)).setObjects(("NSCRTV-HFCEMS-COMMON-MIB", "commonPhysAddress"), ("NSCRTV-HFCEMS-COMMON-MIB", "commonNELogicalID"), ("NSCRTV-HFCEMS-OPTICALSWITCH-MIB", "osCurrentWorkChannel"))
mibBuilder.exportSymbols("NSCRTV-HFCEMS-OPTICALSWITCH-MIB", osSwitchReference=osSwitchReference, osWavelength=osWavelength, osIdent=osIdent, osCurrentWorkChannel=osCurrentWorkChannel, osVendorOID=osVendorOID, osInputOpticalPowerB=osInputOpticalPowerB, osSwitchEvent=osSwitchEvent, osAutoControl=osAutoControl, osInputOpticalPowerA=osInputOpticalPowerA)
