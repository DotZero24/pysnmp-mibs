# SNMP MIB module (TROPIC-1830VWM-CAPABILITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/TROPIC-1830VWM-CAPABILITY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:55:01 2025
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

(tnVwmMsAgentCapability,) = mibBuilder.importSymbols(
    "TROPIC-VWMMS-MIB",
    "tnVwmMsAgentCapability")


# MODULE-IDENTITY

tn1830VwmCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 100, 1)
)
if mibBuilder.loadTexts:
    tn1830VwmCapability.setRevisions(
        ("2019-05-09 00:00",
         "2019-04-30 00:00",
         "2019-04-11 00:00",
         "2019-03-11 00:00",
         "2019-03-08 00:00",
         "2019-01-31 00:00",
         "2018-12-07 00:00",
         "2018-11-30 00:00",
         "2018-11-15 00:00",
         "2018-11-05 00:00",
         "2018-10-03 00:00",
         "2018-09-12 00:00",
         "2018-09-05 00:00",
         "2018-08-20 00:00",
         "2018-07-09 00:00",
         "2018-06-22 00:00",
         "2018-06-06 00:00",
         "2018-06-01 00:00",
         "2018-05-15 00:00",
         "2018-03-16 00:00",
         "2018-03-08 00:00",
         "2018-02-27 00:00",
         "2018-02-23 12:00",
         "2018-02-08 00:00",
         "2018-01-12 00:00",
         "2017-12-13 00:00",
         "2017-11-21 00:00",
         "2017-11-01 00:00",
         "2017-10-13 00:00",
         "2017-09-29 00:00",
         "2017-07-14 00:00",
         "2017-07-05 00:00",
         "2017-06-16 00:00",
         "2017-04-24 00:00",
         "2017-04-06 00:00",
         "2017-02-06 00:00",
         "2017-01-13 00:00",
         "2016-12-16 00:00",
         "2016-11-04 00:00",
         "2016-10-28 00:00",
         "2016-09-26 00:00",
         "2016-08-17 00:00",
         "2016-08-11 00:00",
         "2016-06-16 00:00",
         "2016-05-31 00:00",
         "2016-05-13 00:00",
         "2016-04-15 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

tn1830VwmCapabilityR901 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 100, 1, 2)
)
if mibBuilder.loadTexts:
    tn1830VwmCapabilityR901.setProductRelease("Release 9.0.1.")
if mibBuilder.loadTexts:
    tn1830VwmCapabilityR901.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TROPIC-1830VWM-CAPABILITY-MIB",
    **{"tn1830VwmCapability": tn1830VwmCapability,
       "tn1830VwmCapabilityR901": tn1830VwmCapabilityR901}
)
