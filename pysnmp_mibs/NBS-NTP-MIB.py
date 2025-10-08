#
# PySNMP MIB module NBS-NTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/mrv/NBS-NTP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:07:26 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
nbsCmmcNtpGrp, = mibBuilder.importSymbols("NBS-CMMC-MIB", "nbsCmmcNtpGrp")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nbsNtpMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 200, 9, 1))
if mibBuilder.loadTexts: nbsNtpMib.setLastUpdated('200711210000Z')
if mibBuilder.loadTexts: nbsNtpMib.setOrganization('NBS')
nbsNtpEnable = MibScalar((1, 3, 6, 1, 4, 1, 629, 200, 9, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSupported", 1), ("no", 2), ("yes", 3))).clone('no')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsNtpEnable.setStatus('current')
nbsNtpServerTableSize = MibScalar((1, 3, 6, 1, 4, 1, 629, 200, 9, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsNtpServerTableSize.setStatus('current')
nbsNtpServerTable = MibTable((1, 3, 6, 1, 4, 1, 629, 200, 9, 1, 3), )
if mibBuilder.loadTexts: nbsNtpServerTable.setStatus('current')
nbsNtpServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 200, 9, 1, 3, 1), ).setIndexNames((0, "NBS-NTP-MIB", "nbsNtpServerIpAddr"))
if mibBuilder.loadTexts: nbsNtpServerEntry.setStatus('current')
nbsNtpServerIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 200, 9, 1, 3, 1, 1), IpAddress())
if mibBuilder.loadTexts: nbsNtpServerIpAddr.setStatus('current')
nbsNtpServerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 200, 9, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("invalid", 1), ("active", 2))).clone('invalid')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsNtpServerStatus.setStatus('current')
mibBuilder.exportSymbols("NBS-NTP-MIB", nbsNtpServerTable=nbsNtpServerTable, nbsNtpServerTableSize=nbsNtpServerTableSize, nbsNtpServerIpAddr=nbsNtpServerIpAddr, nbsNtpServerStatus=nbsNtpServerStatus, nbsNtpServerEntry=nbsNtpServerEntry, nbsNtpMib=nbsNtpMib, nbsNtpEnable=nbsNtpEnable, PYSNMP_MODULE_ID=nbsNtpMib)
