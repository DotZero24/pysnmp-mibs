# SNMP MIB module (CISCO-VOICE-APPLICATIONS-OID-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/cisco/CISCO-VOICE-APPLICATIONS-OID-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:27:55 2025
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

(ciscoModules,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoModules")

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

ciscoVoiceApplicationsOIDMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 12, 5)
)
if mibBuilder.loadTexts:
    ciscoVoiceApplicationsOIDMIB.setRevisions(
        ("2004-06-17 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CvaMIBOids_ObjectIdentity = ObjectIdentity
cvaMIBOids = _CvaMIBOids_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 12, 5, 1)
)
_CiscoCallManager_ObjectIdentity = ObjectIdentity
ciscoCallManager = _CiscoCallManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 12, 5, 1, 1)
)
_CiscoCallManagerExpress_ObjectIdentity = ObjectIdentity
ciscoCallManagerExpress = _CiscoCallManagerExpress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 12, 5, 1, 2)
)
_CiscoSRST_ObjectIdentity = ObjectIdentity
ciscoSRST = _CiscoSRST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 12, 5, 1, 3)
)
_CiscoBTS_ObjectIdentity = ObjectIdentity
ciscoBTS = _CiscoBTS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 12, 5, 1, 4)
)
_CiscoCSPS_ObjectIdentity = ObjectIdentity
ciscoCSPS = _CiscoCSPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 12, 5, 1, 5)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VOICE-APPLICATIONS-OID-MIB",
    **{"ciscoVoiceApplicationsOIDMIB": ciscoVoiceApplicationsOIDMIB,
       "cvaMIBOids": cvaMIBOids,
       "ciscoCallManager": ciscoCallManager,
       "ciscoCallManagerExpress": ciscoCallManagerExpress,
       "ciscoSRST": ciscoSRST,
       "ciscoBTS": ciscoBTS,
       "ciscoCSPS": ciscoCSPS}
)
