# SNMP MIB module (ADTRAN-GENMINIDSLAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GENMINIDSLAM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:33:32 2025
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

(adIdentityShared,
 adShared) = mibBuilder.importSymbols(
    "ADTRAN-MIB",
    "adIdentityShared",
    "adShared")

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

adGENMINIDSLAMID = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenMiniDslam_ObjectIdentity = ObjectIdentity
adGenMiniDslam = _AdGenMiniDslam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 61)
)
_AdTAMiniDslam2g_ObjectIdentity = ObjectIdentity
adTAMiniDslam2g = _AdTAMiniDslam2g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 61, 1)
)
_AdTAMiniDslam2gmg_ObjectIdentity = ObjectIdentity
adTAMiniDslam2gmg = _AdTAMiniDslam2gmg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 61, 1, 1)
)
_AdGenBondingID_ObjectIdentity = ObjectIdentity
adGenBondingID = _AdGenBondingID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 4)
)
_AdTAMiniDslam3gID_ObjectIdentity = ObjectIdentity
adTAMiniDslam3gID = _AdTAMiniDslam3gID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GENMINIDSLAM-MIB",
    **{"adGenMiniDslam": adGenMiniDslam,
       "adTAMiniDslam2g": adTAMiniDslam2g,
       "adTAMiniDslam2gmg": adTAMiniDslam2gmg,
       "adGENMINIDSLAMID": adGENMINIDSLAMID,
       "adGenBondingID": adGenBondingID,
       "adTAMiniDslam3gID": adTAMiniDslam3gID}
)
