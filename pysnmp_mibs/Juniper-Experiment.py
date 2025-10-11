# SNMP MIB module (Juniper-Experiment) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/junose/Juniper-Experiment
# Produced by pysmi-1.6.2 at Fri Oct 10 21:06:44 2025
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

(juniperUniExperiment,) = mibBuilder.importSymbols(
    "Juniper-UNI-SMI",
    "juniperUniExperiment")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
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


# MODULE-IDENTITY

juniExperiment = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2)
)
if mibBuilder.loadTexts:
    juniExperiment.setRevisions(
        ("2002-11-13 20:58",
         "2001-06-20 20:36",
         "2000-10-24 21:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JuniDvmrpExperiment_ObjectIdentity = ObjectIdentity
juniDvmrpExperiment = _JuniDvmrpExperiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 1)
)
if mibBuilder.loadTexts:
    juniDvmrpExperiment.setStatus("current")
_JuniSonetApsExperiment_ObjectIdentity = ObjectIdentity
juniSonetApsExperiment = _JuniSonetApsExperiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2)
)
if mibBuilder.loadTexts:
    juniSonetApsExperiment.setStatus("current")
_JuniMplsExperiment_ObjectIdentity = ObjectIdentity
juniMplsExperiment = _JuniMplsExperiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 3)
)
if mibBuilder.loadTexts:
    juniMplsExperiment.setStatus("current")
_JuniMplsVPNExperiment_ObjectIdentity = ObjectIdentity
juniMplsVPNExperiment = _JuniMplsVPNExperiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 4)
)
if mibBuilder.loadTexts:
    juniMplsVPNExperiment.setStatus("current")
_JuniBFDExperiment_ObjectIdentity = ObjectIdentity
juniBFDExperiment = _JuniBFDExperiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 5)
)
if mibBuilder.loadTexts:
    juniBFDExperiment.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-Experiment",
    **{"juniExperiment": juniExperiment,
       "juniDvmrpExperiment": juniDvmrpExperiment,
       "juniSonetApsExperiment": juniSonetApsExperiment,
       "juniMplsExperiment": juniMplsExperiment,
       "juniMplsVPNExperiment": juniMplsVPNExperiment,
       "juniBFDExperiment": juniBFDExperiment}
)
