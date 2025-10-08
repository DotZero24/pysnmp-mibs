#
# PySNMP MIB module ELTEX-MES-ISS-SNTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/eltex/ELTEX-MES-ISS-SNTP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:04:49 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
eltMesIss, = mibBuilder.importSymbols("ELTEX-MES-ISS-MIB", "eltMesIss")
fsSntpUnicastServerEntry, = mibBuilder.importSymbols("FSSNTP-MIB", "fsSntpUnicastServerEntry")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
eltMesIssSntpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1, 139, 16))
eltMesIssSntpMIB.setRevisions(('2019-08-15 00:00', '2020-12-11 00:00',))
if mibBuilder.loadTexts: eltMesIssSntpMIB.setLastUpdated('202012110000Z')
if mibBuilder.loadTexts: eltMesIssSntpMIB.setOrganization('Eltex Enterprise, Ltd.')
class NtpStratumType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

eltMesIssSntpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 139, 16, 1))
eltMesIssSntpUnicast = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 139, 16, 1, 1))
eltMesIssSntpUnicastServerTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 139, 16, 1, 1, 1), )
if mibBuilder.loadTexts: eltMesIssSntpUnicastServerTable.setStatus('current')
eltMesIssSntpUnicastServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 139, 16, 1, 1, 1, 1), )
fsSntpUnicastServerEntry.registerAugmentions(("ELTEX-MES-ISS-SNTP-MIB", "eltMesIssSntpUnicastServerEntry"))
eltMesIssSntpUnicastServerEntry.setIndexNames(*fsSntpUnicastServerEntry.getIndexNames())
if mibBuilder.loadTexts: eltMesIssSntpUnicastServerEntry.setStatus('current')
eltMesIssSntpUnicastServerStratum = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 139, 16, 1, 1, 1, 1, 1), NtpStratumType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltMesIssSntpUnicastServerStratum.setStatus('current')
eltMesIssSntpUnicastServerPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 139, 16, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltMesIssSntpUnicastServerPriority.setStatus('current')
mibBuilder.exportSymbols("ELTEX-MES-ISS-SNTP-MIB", eltMesIssSntpMIB=eltMesIssSntpMIB, eltMesIssSntpUnicastServerPriority=eltMesIssSntpUnicastServerPriority, eltMesIssSntpUnicast=eltMesIssSntpUnicast, eltMesIssSntpUnicastServerTable=eltMesIssSntpUnicastServerTable, eltMesIssSntpUnicastServerStratum=eltMesIssSntpUnicastServerStratum, PYSNMP_MODULE_ID=eltMesIssSntpMIB, NtpStratumType=NtpStratumType, eltMesIssSntpObjects=eltMesIssSntpObjects, eltMesIssSntpUnicastServerEntry=eltMesIssSntpUnicastServerEntry)
