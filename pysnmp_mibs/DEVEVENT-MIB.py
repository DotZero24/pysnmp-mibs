#
# PySNMP MIB module DEVEVENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/aperto/DEVEVENT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:17:20 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
device, = mibBuilder.importSymbols("ANIROOT-MIB", "device")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
aniDevEvent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4325, 2, 6))
if mibBuilder.loadTexts: aniDevEvent.setLastUpdated('0012111753Z')
if mibBuilder.loadTexts: aniDevEvent.setOrganization('Aperto Networks')
aniDevEvNotify = MibIdentifier((1, 3, 6, 1, 4, 1, 4325, 2, 6, 2))
aniDevEmailSending = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 6, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aniDevEmailSending.setStatus('current')
aniDevEmailSender = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 6, 2, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aniDevEmailSender.setStatus('current')
aniDevDomainName = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 6, 2, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aniDevDomainName.setStatus('current')
aniDevEmailReceiver1 = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 6, 2, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aniDevEmailReceiver1.setStatus('current')
aniDevEmailReceiver2 = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 6, 2, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aniDevEmailReceiver2.setStatus('current')
mibBuilder.exportSymbols("DEVEVENT-MIB", aniDevEmailSender=aniDevEmailSender, aniDevEmailReceiver2=aniDevEmailReceiver2, aniDevDomainName=aniDevDomainName, aniDevEmailReceiver1=aniDevEmailReceiver1, aniDevEvNotify=aniDevEvNotify, aniDevEmailSending=aniDevEmailSending, PYSNMP_MODULE_ID=aniDevEvent, aniDevEvent=aniDevEvent)
