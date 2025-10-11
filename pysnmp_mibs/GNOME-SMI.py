# SNMP MIB module (GNOME-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/gnome/GNOME-SMI
# Produced by pysmi-1.6.2 at Fri Oct 10 20:12:42 2025
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

gnome = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3319)
)
if mibBuilder.loadTexts:
    gnome.setRevisions(
        ("2007-09-07 00:00",
         "2005-05-07 00:00",
         "2003-12-07 00:00",
         "1998-09-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_GnomeProducts_ObjectIdentity = ObjectIdentity
gnomeProducts = _GnomeProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3319, 1)
)
if mibBuilder.loadTexts:
    gnomeProducts.setStatus("current")
_GnomeMgmt_ObjectIdentity = ObjectIdentity
gnomeMgmt = _GnomeMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3319, 2)
)
if mibBuilder.loadTexts:
    gnomeMgmt.setStatus("current")
_GnomeTest_ObjectIdentity = ObjectIdentity
gnomeTest = _GnomeTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3319, 3)
)
if mibBuilder.loadTexts:
    gnomeTest.setStatus("current")
_GnomeSysadmin_ObjectIdentity = ObjectIdentity
gnomeSysadmin = _GnomeSysadmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3319, 4)
)
if mibBuilder.loadTexts:
    gnomeSysadmin.setStatus("current")
_GnomeLDAP_ObjectIdentity = ObjectIdentity
gnomeLDAP = _GnomeLDAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3319, 5)
)
if mibBuilder.loadTexts:
    gnomeLDAP.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GNOME-SMI",
    **{"gnome": gnome,
       "gnomeProducts": gnomeProducts,
       "gnomeMgmt": gnomeMgmt,
       "gnomeTest": gnomeTest,
       "gnomeSysadmin": gnomeSysadmin,
       "gnomeLDAP": gnomeLDAP}
)
