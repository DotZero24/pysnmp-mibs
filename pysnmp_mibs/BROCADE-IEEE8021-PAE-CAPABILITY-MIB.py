#
# PySNMP MIB module BROCADE-IEEE8021-PAE-CAPABILITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/brocade/BROCADE-IEEE8021-PAE-CAPABILITY-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:15:41 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
brocadeAgentCapability, = mibBuilder.importSymbols("Brocade-REG-MIB", "brocadeAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
brocadeIeee8021PaeCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 1588, 3, 2, 1))
brocadeIeee8021PaeCapability.setRevisions(('2012-06-01 00:00',))
if mibBuilder.loadTexts: brocadeIeee8021PaeCapability.setLastUpdated('201206010000Z')
if mibBuilder.loadTexts: brocadeIeee8021PaeCapability.setOrganization('Brocade Communications Systems, Inc.,')
brocadeIeee8021PaeVdx300R1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 1588, 3, 2, 1, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    brocadeIeee8021PaeVdx300R1 = brocadeIeee8021PaeVdx300R1.setProductRelease('NOS3.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    brocadeIeee8021PaeVdx300R1 = brocadeIeee8021PaeVdx300R1.setStatus('current')
mibBuilder.exportSymbols("BROCADE-IEEE8021-PAE-CAPABILITY-MIB", PYSNMP_MODULE_ID=brocadeIeee8021PaeCapability, brocadeIeee8021PaeVdx300R1=brocadeIeee8021PaeVdx300R1, brocadeIeee8021PaeCapability=brocadeIeee8021PaeCapability)
