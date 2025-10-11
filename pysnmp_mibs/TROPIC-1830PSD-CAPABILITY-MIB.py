# SNMP MIB module (TROPIC-1830PSD-CAPABILITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/TROPIC-1830PSD-CAPABILITY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:55:09 2025
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

(tnPsdAgentCapability,) = mibBuilder.importSymbols(
    "TROPIC-PSD-MIB",
    "tnPsdAgentCapability")


# MODULE-IDENTITY

tn1830PsdCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 100, 1)
)
if mibBuilder.loadTexts:
    tn1830PsdCapability.setRevisions(
        ("2021-08-11 00:00",
         "2021-07-01 00:00",
         "2021-06-17 00:00",
         "2021-01-28 12:00",
         "2021-01-24 12:00",
         "2021-01-14 12:00",
         "2020-12-14 12:00",
         "2020-12-09 12:00",
         "2020-12-03 12:00",
         "2020-11-18 12:00",
         "2020-10-26 12:00",
         "2020-10-23 12:00",
         "2020-06-15 12:00",
         "2020-06-09 12:00",
         "2020-04-15 12:00",
         "2020-04-06 12:00",
         "2020-03-11 12:00",
         "2020-02-25 12:00",
         "2020-01-13 12:00",
         "2019-09-16 12:00",
         "2018-05-25 12:00",
         "2018-04-30 12:00",
         "2018-03-19 12:00",
         "2018-02-23 12:00",
         "2018-02-14 12:00",
         "2017-12-07 12:00",
         "2017-09-25 12:00",
         "2017-08-18 12:00",
         "2017-07-07 12:00",
         "2017-05-05 12:00",
         "2017-03-13 12:00",
         "2017-02-06 12:00",
         "2016-12-21 12:00",
         "2016-10-28 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

tn1830Capability = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 100, 1, 1)
)
if mibBuilder.loadTexts:
    tn1830Capability.setProductRelease("Release 4.0.0.")
if mibBuilder.loadTexts:
    tn1830Capability.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TROPIC-1830PSD-CAPABILITY-MIB",
    **{"tn1830PsdCapability": tn1830PsdCapability,
       "tn1830Capability": tn1830Capability}
)
