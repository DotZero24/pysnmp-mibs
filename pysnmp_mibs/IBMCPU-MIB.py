#
# PySNMP MIB module IBMCPU-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/ibm/IBMCPU-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:24:37 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ibm = MibIdentifier((1, 3, 6, 1, 4, 1, 2))
ibmProd = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6))
ibm6611 = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 2))
ibmsystem = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 2, 4))
netView6000SubAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 4))
nv6saComputerSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 4, 5))
nv6saComputerSystemLoad = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 4, 5, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nv6saComputerSystemLoad.setStatus('mandatory')
ibmMainProcessorLoadTable = MibTable((1, 3, 6, 1, 4, 1, 2, 6, 2, 4, 1), )
if mibBuilder.loadTexts: ibmMainProcessorLoadTable.setStatus('mandatory')
ibmMainProcessorLoadEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2, 6, 2, 4, 1, 1), ).setIndexNames((0, "IBMCPU-MIB", "ibmMainProcessorLoadIndex"))
if mibBuilder.loadTexts: ibmMainProcessorLoadEntry.setStatus('mandatory')
ibmMainProcessorLoadIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 2, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 60))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmMainProcessorLoadIndex.setStatus('mandatory')
ibmMainProcessorLoad = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 2, 4, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmMainProcessorLoad.setStatus('mandatory')
mibBuilder.exportSymbols("IBMCPU-MIB", ibmProd=ibmProd, netView6000SubAgent=netView6000SubAgent, ibmMainProcessorLoadTable=ibmMainProcessorLoadTable, nv6saComputerSystemLoad=nv6saComputerSystemLoad, ibmMainProcessorLoadEntry=ibmMainProcessorLoadEntry, ibmMainProcessorLoadIndex=ibmMainProcessorLoadIndex, ibm6611=ibm6611, ibmMainProcessorLoad=ibmMainProcessorLoad, ibm=ibm, nv6saComputerSystem=nv6saComputerSystem, ibmsystem=ibmsystem)
