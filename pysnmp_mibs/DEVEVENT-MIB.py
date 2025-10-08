#
# PySNMP MIB module DEVEVENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/aperto/DEVEVENT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:07:55 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
device, = mibBuilder.importSymbols("ANIROOT-MIB", "device")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("DEVEVENT-MIB", aniDevEmailReceiver2=aniDevEmailReceiver2, aniDevEvent=aniDevEvent, aniDevDomainName=aniDevDomainName, aniDevEmailReceiver1=aniDevEmailReceiver1, aniDevEvNotify=aniDevEvNotify, aniDevEmailSending=aniDevEmailSending, PYSNMP_MODULE_ID=aniDevEvent, aniDevEmailSender=aniDevEmailSender)
