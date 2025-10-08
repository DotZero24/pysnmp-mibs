#
# PySNMP MIB module ELTEX-MES-ISS-SNTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/eltex/ELTEX-MES-ISS-SNTP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:12:12 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
eltMesIss, = mibBuilder.importSymbols("ELTEX-MES-ISS-MIB", "eltMesIss")
fsSntpUnicastServerEntry, = mibBuilder.importSymbols("FSSNTP-MIB", "fsSntpUnicastServerEntry")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
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
mibBuilder.exportSymbols("ELTEX-MES-ISS-SNTP-MIB", eltMesIssSntpMIB=eltMesIssSntpMIB, eltMesIssSntpUnicastServerEntry=eltMesIssSntpUnicastServerEntry, eltMesIssSntpUnicast=eltMesIssSntpUnicast, NtpStratumType=NtpStratumType, PYSNMP_MODULE_ID=eltMesIssSntpMIB, eltMesIssSntpUnicastServerTable=eltMesIssSntpUnicastServerTable, eltMesIssSntpUnicastServerStratum=eltMesIssSntpUnicastServerStratum, eltMesIssSntpObjects=eltMesIssSntpObjects, eltMesIssSntpUnicastServerPriority=eltMesIssSntpUnicastServerPriority)
