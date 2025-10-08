#
# PySNMP MIB module HPNSAASR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hp/HPNSAASR-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:02:46 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hp = MibIdentifier((1, 3, 6, 1, 4, 1, 11))
nm = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2))
hpnsa = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 23))
hpnsaASR = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 23, 25))
hpnsaASRMibRev = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 23, 25, 1))
hpnsaASRParms = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 23, 25, 2))
hpnsaASRMibRevMajor = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 23, 25, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaASRMibRevMajor.setStatus('mandatory')
hpnsaASRMibRevMinor = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 23, 25, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaASRMibRevMinor.setStatus('mandatory')
hpnsaASRMaxConsecutiveASR = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 23, 25, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnsaASRMaxConsecutiveASR.setStatus('mandatory')
hpnsaASRCurrentConsecutiveASR = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 23, 25, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaASRCurrentConsecutiveASR.setStatus('mandatory')
hpnsaASRTimeOutInterval = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 23, 25, 2, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnsaASRTimeOutInterval.setStatus('mandatory')
hpnsaASRKickInterval = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 23, 25, 2, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaASRKickInterval.setStatus('mandatory')
hpnsaASRTimeoutAction = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 23, 25, 2, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnsaASRTimeoutAction.setStatus('mandatory')
mibBuilder.exportSymbols("HPNSAASR-MIB", hp=hp, nm=nm, hpnsaASRKickInterval=hpnsaASRKickInterval, hpnsaASRTimeoutAction=hpnsaASRTimeoutAction, hpnsaASRMibRevMinor=hpnsaASRMibRevMinor, hpnsaASRMibRevMajor=hpnsaASRMibRevMajor, hpnsaASR=hpnsaASR, hpnsaASRMaxConsecutiveASR=hpnsaASRMaxConsecutiveASR, hpnsaASRMibRev=hpnsaASRMibRev, hpnsaASRParms=hpnsaASRParms, hpnsaASRCurrentConsecutiveASR=hpnsaASRCurrentConsecutiveASR, hpnsa=hpnsa, hpnsaASRTimeOutInterval=hpnsaASRTimeOutInterval)
