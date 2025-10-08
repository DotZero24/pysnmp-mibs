#
# PySNMP MIB module TRANZEO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/tranzeo/TRANZEO-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:30:10 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tranzeo = MibIdentifier((1, 3, 6, 1, 4, 1, 24575))
signal = MibIdentifier((1, 3, 6, 1, 4, 1, 24575, 1))
rssi = MibScalar((1, 3, 6, 1, 4, 1, 24575, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-110, 0))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rssi.setStatus('mandatory')
signallow = MibScalar((1, 3, 6, 1, 4, 1, 24575, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-110, 0))).setMaxAccess("readonly")
if mibBuilder.loadTexts: signallow.setStatus('mandatory')
signalaverage = MibScalar((1, 3, 6, 1, 4, 1, 24575, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-110, 0))).setMaxAccess("readonly")
if mibBuilder.loadTexts: signalaverage.setStatus('mandatory')
signalhigh = MibScalar((1, 3, 6, 1, 4, 1, 24575, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-110, 0))).setMaxAccess("readonly")
if mibBuilder.loadTexts: signalhigh.setStatus('mandatory')
noise = MibScalar((1, 3, 6, 1, 4, 1, 24575, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-110, 0))).setMaxAccess("readonly")
if mibBuilder.loadTexts: noise.setStatus('mandatory')
noiselow = MibScalar((1, 3, 6, 1, 4, 1, 24575, 1, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-110, 0))).setMaxAccess("readonly")
if mibBuilder.loadTexts: noiselow.setStatus('mandatory')
noiseaverage = MibScalar((1, 3, 6, 1, 4, 1, 24575, 1, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-110, 0))).setMaxAccess("readonly")
if mibBuilder.loadTexts: noiseaverage.setStatus('mandatory')
noisehigh = MibScalar((1, 3, 6, 1, 4, 1, 24575, 1, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-110, 0))).setMaxAccess("readonly")
if mibBuilder.loadTexts: noisehigh.setStatus('mandatory')
mibBuilder.exportSymbols("TRANZEO-MIB", signalaverage=signalaverage, signallow=signallow, noiseaverage=noiseaverage, signalhigh=signalhigh, signal=signal, rssi=rssi, noise=noise, noisehigh=noisehigh, tranzeo=tranzeo, noiselow=noiselow)
