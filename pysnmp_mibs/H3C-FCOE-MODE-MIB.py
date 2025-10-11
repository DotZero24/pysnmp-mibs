# SNMP MIB module (H3C-FCOE-MODE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-FCOE-MODE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:20:20 2025
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

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

h3cFcoeMode = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 135)
)
if mibBuilder.loadTexts:
    h3cFcoeMode.setRevisions(
        ("2013-03-08 11:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cFcoeModeMibObjects_ObjectIdentity = ObjectIdentity
h3cFcoeModeMibObjects = _H3cFcoeModeMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 135, 1)
)
_H3cFcoeModeCfgMode_Type = Integer32
_H3cFcoeModeCfgMode_Object = MibScalar
h3cFcoeModeCfgMode = _H3cFcoeModeCfgMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 135, 1, 1),
    _H3cFcoeModeCfgMode_Type()
)
h3cFcoeModeCfgMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cFcoeModeCfgMode.setStatus("current")


class _H3cFcoeModeCfgLastResult_Type(Integer32):
    """Custom type h3cFcoeModeCfgLastResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("success", 1),
          ("noLicence", 2),
          ("needReset", 3),
          ("unknownFault", 4))
    )


_H3cFcoeModeCfgLastResult_Type.__name__ = "Integer32"
_H3cFcoeModeCfgLastResult_Object = MibScalar
h3cFcoeModeCfgLastResult = _H3cFcoeModeCfgLastResult_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 135, 1, 2),
    _H3cFcoeModeCfgLastResult_Type()
)
h3cFcoeModeCfgLastResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcoeModeCfgLastResult.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-FCOE-MODE-MIB",
    **{"h3cFcoeMode": h3cFcoeMode,
       "h3cFcoeModeMibObjects": h3cFcoeModeMibObjects,
       "h3cFcoeModeCfgMode": h3cFcoeModeCfgMode,
       "h3cFcoeModeCfgLastResult": h3cFcoeModeCfgLastResult}
)
