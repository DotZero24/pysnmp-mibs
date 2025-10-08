#
# PySNMP MIB module BROCADE-IEEE8021-PAE-CAPABILITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/brocade/BROCADE-IEEE8021-PAE-CAPABILITY-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:07:04 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
brocadeAgentCapability, = mibBuilder.importSymbols("Brocade-REG-MIB", "brocadeAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
brocadeIeee8021PaeCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 1588, 3, 2, 1))
brocadeIeee8021PaeCapability.setRevisions(('2012-06-01 00:00',))
if mibBuilder.loadTexts: brocadeIeee8021PaeCapability.setLastUpdated('201206010000Z')
if mibBuilder.loadTexts: brocadeIeee8021PaeCapability.setOrganization('Brocade Communications Systems, Inc.,')
brocadeIeee8021PaeVdx300R1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 1588, 3, 2, 1, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    brocadeIeee8021PaeVdx300R1 = brocadeIeee8021PaeVdx300R1.setProductRelease('NOS3.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    brocadeIeee8021PaeVdx300R1 = brocadeIeee8021PaeVdx300R1.setStatus('current')
mibBuilder.exportSymbols("BROCADE-IEEE8021-PAE-CAPABILITY-MIB", brocadeIeee8021PaeCapability=brocadeIeee8021PaeCapability, PYSNMP_MODULE_ID=brocadeIeee8021PaeCapability, brocadeIeee8021PaeVdx300R1=brocadeIeee8021PaeVdx300R1)
