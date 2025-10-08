#
# PySNMP MIB module CPQSANAPP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hp/CPQSANAPP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:08:03 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
compaq = MibIdentifier((1, 3, 6, 1, 4, 1, 232))
cpqSanAppliance = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 151))
resourceMonitor = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 151, 11))
swSystemName = MibScalar((1, 3, 6, 1, 4, 1, 232, 151, 11, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(255, 255)).setFixedLength(255)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSystemName.setStatus('mandatory')
swSystemType = MibScalar((1, 3, 6, 1, 4, 1, 232, 151, 11, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("hsg80", 1), ("switch", 2), ("appliance", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSystemType.setStatus('mandatory')
swEventName = MibScalar((1, 3, 6, 1, 4, 1, 232, 151, 11, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(255, 255)).setFixedLength(255)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swEventName.setStatus('mandatory')
swFailure = MibScalar((1, 3, 6, 1, 4, 1, 232, 151, 11, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(255, 255)).setFixedLength(255)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swFailure.setStatus('mandatory')
swSequence = MibScalar((1, 3, 6, 1, 4, 1, 232, 151, 11, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSequence.setStatus('mandatory')
swFailureTrap = NotificationType((1, 3, 6, 1, 4, 1, 232, 151, 11) + (0,1)).setObjects(("CPQSANAPP-MIB", "swSystemName"), ("CPQSANAPP-MIB", "swSystemType"), ("CPQSANAPP-MIB", "swEventName"), ("CPQSANAPP-MIB", "swFailure"), ("CPQSANAPP-MIB", "swSequence"))
swWarningTrap = NotificationType((1, 3, 6, 1, 4, 1, 232, 151, 11) + (0,2)).setObjects(("CPQSANAPP-MIB", "swSystemName"), ("CPQSANAPP-MIB", "swSystemType"), ("CPQSANAPP-MIB", "swEventName"), ("CPQSANAPP-MIB", "swFailure"), ("CPQSANAPP-MIB", "swSequence"))
swInformationTrap = NotificationType((1, 3, 6, 1, 4, 1, 232, 151, 11) + (0,4)).setObjects(("CPQSANAPP-MIB", "swSystemName"), ("CPQSANAPP-MIB", "swSystemType"), ("CPQSANAPP-MIB", "swEventName"), ("CPQSANAPP-MIB", "swFailure"), ("CPQSANAPP-MIB", "swSequence"))
mibBuilder.exportSymbols("CPQSANAPP-MIB", swFailure=swFailure, resourceMonitor=resourceMonitor, compaq=compaq, swSystemType=swSystemType, cpqSanAppliance=cpqSanAppliance, swEventName=swEventName, swSequence=swSequence, swWarningTrap=swWarningTrap, swFailureTrap=swFailureTrap, swSystemName=swSystemName, swInformationTrap=swInformationTrap)
