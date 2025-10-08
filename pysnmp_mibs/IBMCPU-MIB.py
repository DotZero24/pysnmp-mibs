#
# PySNMP MIB module IBMCPU-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/ibm/IBMCPU-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:45:34 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("IBMCPU-MIB", ibm=ibm, ibmMainProcessorLoadTable=ibmMainProcessorLoadTable, nv6saComputerSystem=nv6saComputerSystem, netView6000SubAgent=netView6000SubAgent, ibmsystem=ibmsystem, ibmProd=ibmProd, ibmMainProcessorLoadIndex=ibmMainProcessorLoadIndex, ibmMainProcessorLoad=ibmMainProcessorLoad, ibmMainProcessorLoadEntry=ibmMainProcessorLoadEntry, ibm6611=ibm6611, nv6saComputerSystemLoad=nv6saComputerSystemLoad)
