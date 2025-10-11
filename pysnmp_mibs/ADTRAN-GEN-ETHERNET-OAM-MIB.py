# SNMP MIB module (ADTRAN-GEN-ETHERNET-OAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GEN-ETHERNET-OAM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:32:42 2025
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

adGenEthernetOAMIdentity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 75)
)
if mibBuilder.loadTexts:
    adGenEthernetOAMIdentity.setRevisions(
        ("2011-06-10 08:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenEthernetOAM_ObjectIdentity = ObjectIdentity
adGenEthernetOAM = _AdGenEthernetOAM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 75)
)
_AdGenEthernetCfm_ObjectIdentity = ObjectIdentity
adGenEthernetCfm = _AdGenEthernetCfm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1)
)
_AdGenY1731_ObjectIdentity = ObjectIdentity
adGenY1731 = _AdGenY1731_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 2)
)
_AdGenEthernetCfmID_ObjectIdentity = ObjectIdentity
adGenEthernetCfmID = _AdGenEthernetCfmID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 75, 1)
)
_AdGenY1731ID_ObjectIdentity = ObjectIdentity
adGenY1731ID = _AdGenY1731ID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 75, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GEN-ETHERNET-OAM-MIB",
    **{"adGenEthernetOAM": adGenEthernetOAM,
       "adGenEthernetCfm": adGenEthernetCfm,
       "adGenY1731": adGenY1731,
       "adGenEthernetOAMIdentity": adGenEthernetOAMIdentity,
       "adGenEthernetCfmID": adGenEthernetCfmID,
       "adGenY1731ID": adGenY1731ID}
)
