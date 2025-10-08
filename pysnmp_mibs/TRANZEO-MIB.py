#
# PySNMP MIB module TRANZEO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/tranzeo/TRANZEO-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:53:45 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("TRANZEO-MIB", noiselow=noiselow, signal=signal, noisehigh=noisehigh, noiseaverage=noiseaverage, rssi=rssi, signallow=signallow, tranzeo=tranzeo, signalhigh=signalhigh, signalaverage=signalaverage, noise=noise)
