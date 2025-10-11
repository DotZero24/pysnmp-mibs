# SNMP MIB module (VMWARE-VRNI-AGENTCAP-OLD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/vmware/VMWARE-VRNI-AGENTCAP-OLD-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:23:21 2025
# On host Robs-Air.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(AgentCapabilities,
 ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "AgentCapabilities",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(vmwareAgentCapabilities,) = mibBuilder.importSymbols(
    "VMWARE-ROOT-MIB",
    "vmwareAgentCapabilities")


# MODULE-IDENTITY

vmwVRNIAgentCapabilityMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 70, 125)
)
if mibBuilder.loadTexts:
    vmwVRNIAgentCapabilityMIB.setRevisions(
        ("2017-10-13 00:00",
         "2017-09-05 00:00",
         "2017-06-01 00:00",
         "2017-03-02 00:00",
         "2016-11-22 00:01")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VmwVRNICapability_ObjectIdentity = ObjectIdentity
vmwVRNICapability = _VmwVRNICapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 70, 125, 10)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

vmwVRNIAgent2016v320 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 6876, 70, 125, 10, 6)
)
if mibBuilder.loadTexts:
    vmwVRNIAgent2016v320.setProductRelease("3.2.0")
if mibBuilder.loadTexts:
    vmwVRNIAgent2016v320.setStatus(
        "obsolete"
    )

vmwVRNIAgent2017v330 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 6876, 70, 125, 10, 7)
)
if mibBuilder.loadTexts:
    vmwVRNIAgent2017v330.setProductRelease("3.3.0")
if mibBuilder.loadTexts:
    vmwVRNIAgent2017v330.setStatus(
        "obsolete"
    )

vmwVRNIAgent2017v340 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 6876, 70, 125, 10, 8)
)
if mibBuilder.loadTexts:
    vmwVRNIAgent2017v340.setProductRelease("3.4.0")
if mibBuilder.loadTexts:
    vmwVRNIAgent2017v340.setStatus(
        "obsolete"
    )

vmwVRNIAgent2016v350 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 6876, 70, 125, 10, 9)
)
if mibBuilder.loadTexts:
    vmwVRNIAgent2016v350.setProductRelease("3.5.0")
if mibBuilder.loadTexts:
    vmwVRNIAgent2016v350.setStatus(
        "obsolete"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VMWARE-VRNI-AGENTCAP-OLD-MIB",
    **{"vmwVRNIAgentCapabilityMIB": vmwVRNIAgentCapabilityMIB,
       "vmwVRNICapability": vmwVRNICapability,
       "vmwVRNIAgent2016v320": vmwVRNIAgent2016v320,
       "vmwVRNIAgent2017v330": vmwVRNIAgent2017v330,
       "vmwVRNIAgent2017v340": vmwVRNIAgent2017v340,
       "vmwVRNIAgent2016v350": vmwVRNIAgent2016v350}
)
