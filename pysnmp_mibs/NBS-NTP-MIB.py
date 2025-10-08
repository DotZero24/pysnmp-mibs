#
# PySNMP MIB module NBS-NTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/mrv/NBS-NTP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:16:21 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
nbsCmmcNtpGrp, = mibBuilder.importSymbols("NBS-CMMC-MIB", "nbsCmmcNtpGrp")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("NBS-NTP-MIB", nbsNtpEnable=nbsNtpEnable, nbsNtpServerStatus=nbsNtpServerStatus, nbsNtpServerTableSize=nbsNtpServerTableSize, nbsNtpServerTable=nbsNtpServerTable, nbsNtpServerIpAddr=nbsNtpServerIpAddr, nbsNtpServerEntry=nbsNtpServerEntry, nbsNtpMib=nbsNtpMib, PYSNMP_MODULE_ID=nbsNtpMib)
