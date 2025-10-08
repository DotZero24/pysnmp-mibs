#
# PySNMP MIB module CPQSANAPP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hp/CPQSANAPP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:02:19 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, NotificationType, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("CPQSANAPP-MIB", cpqSanAppliance=cpqSanAppliance, swEventName=swEventName, swFailure=swFailure, swInformationTrap=swInformationTrap, swWarningTrap=swWarningTrap, resourceMonitor=resourceMonitor, swSystemName=swSystemName, swSystemType=swSystemType, compaq=compaq, swSequence=swSequence, swFailureTrap=swFailureTrap)
