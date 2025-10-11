# SNMP MIB module (CYCLADES-ACS-ADM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/vertiv/CYCLADES-ACS-ADM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:05:42 2025
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

(cyACSMgmt,) = mibBuilder.importSymbols(
    "CYCLADES-ACS-MIB",
    "cyACSMgmt")

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

cyACSAdm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2925, 4, 4)
)
if mibBuilder.loadTexts:
    cyACSAdm.setRevisions(
        ("2005-08-29 00:00",
         "2002-09-20 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _CyACSSave_Type(Integer32):
    """Custom type cyACSSave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nosave", 0),
          ("save", 1))
    )


_CyACSSave_Type.__name__ = "Integer32"
_CyACSSave_Object = MibScalar
cyACSSave = _CyACSSave_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 4, 1),
    _CyACSSave_Type()
)
cyACSSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cyACSSave.setStatus("current")


class _CyACSSerialHUP_Type(Integer32):
    """Custom type cyACSSerialHUP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("norestartportslave", 0),
          ("restartportslave", 1))
    )


_CyACSSerialHUP_Type.__name__ = "Integer32"
_CyACSSerialHUP_Object = MibScalar
cyACSSerialHUP = _CyACSSerialHUP_Object(
    (1, 3, 6, 1, 4, 1, 2925, 4, 4, 2),
    _CyACSSerialHUP_Type()
)
cyACSSerialHUP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cyACSSerialHUP.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CYCLADES-ACS-ADM-MIB",
    **{"cyACSAdm": cyACSAdm,
       "cyACSSave": cyACSSave,
       "cyACSSerialHUP": cyACSSerialHUP}
)
