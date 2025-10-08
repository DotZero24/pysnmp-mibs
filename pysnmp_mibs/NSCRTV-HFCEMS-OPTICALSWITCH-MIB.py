#
# PySNMP MIB module NSCRTV-HFCEMS-OPTICALSWITCH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/nscrtv/NSCRTV-HFCEMS-OPTICALSWITCH-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:11:53 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
commonNELogicalID, commonPhysAddress = mibBuilder.importSymbols("NSCRTV-HFCEMS-COMMON-MIB", "commonNELogicalID", "commonPhysAddress")
nscrtvHFCemsTree, = mibBuilder.importSymbols("NSCRTV-ROOT", "nscrtvHFCemsTree")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("NSCRTV-HFCEMS-OPTICALSWITCH-MIB", osInputOpticalPowerB=osInputOpticalPowerB, osSwitchReference=osSwitchReference, osIdent=osIdent, osInputOpticalPowerA=osInputOpticalPowerA, osSwitchEvent=osSwitchEvent, osWavelength=osWavelength, osVendorOID=osVendorOID, osAutoControl=osAutoControl, osCurrentWorkChannel=osCurrentWorkChannel)
