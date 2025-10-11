# SNMP MIB module (SAMSUNG-DIAGNOSTICS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/samsung/SAMSUNG-DIAGNOSTICS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:12:35 2025
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

(samsungCommonMIB,) = mibBuilder.importSymbols(
    "SAMSUNG-COMMON-MIB",
    "samsungCommonMIB")

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

scmDiagnostics = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 64)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ScmDiagnosticsDevice_ObjectIdentity = ObjectIdentity
scmDiagnosticsDevice = _ScmDiagnosticsDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 64, 1)
)
_ScmDiagnosticsDeviceTable_Object = MibTable
scmDiagnosticsDeviceTable = _ScmDiagnosticsDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 64, 1, 2)
)
if mibBuilder.loadTexts:
    scmDiagnosticsDeviceTable.setStatus("current")
_ScmDiagnosticsDeviceEntry_Object = MibTableRow
scmDiagnosticsDeviceEntry = _ScmDiagnosticsDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 64, 1, 2, 1)
)
scmDiagnosticsDeviceEntry.setIndexNames(
    (0, "SAMSUNG-DIAGNOSTICS-MIB", "scmDiagnosticsDeviceIndex"),
)
if mibBuilder.loadTexts:
    scmDiagnosticsDeviceEntry.setStatus("current")


class _ScmDiagnosticsDeviceIndex_Type(Integer32):
    """Custom type scmDiagnosticsDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ScmDiagnosticsDeviceIndex_Type.__name__ = "Integer32"
_ScmDiagnosticsDeviceIndex_Object = MibTableColumn
scmDiagnosticsDeviceIndex = _ScmDiagnosticsDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 64, 1, 2, 1, 1),
    _ScmDiagnosticsDeviceIndex_Type()
)
scmDiagnosticsDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmDiagnosticsDeviceIndex.setStatus("current")


class _ScmDiagnosticsDeviceItem_Type(DisplayString):
    """Custom type scmDiagnosticsDeviceItem based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ScmDiagnosticsDeviceItem_Type.__name__ = "DisplayString"
_ScmDiagnosticsDeviceItem_Object = MibTableColumn
scmDiagnosticsDeviceItem = _ScmDiagnosticsDeviceItem_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 64, 1, 2, 1, 2),
    _ScmDiagnosticsDeviceItem_Type()
)
scmDiagnosticsDeviceItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmDiagnosticsDeviceItem.setStatus("current")


class _ScmDiagnosticsDeviceType_Type(Integer32):
    """Custom type scmDiagnosticsDeviceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              21,
              22,
              23,
              24,
              25,
              26,
              41,
              42,
              43)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("output", 2),
          ("cover", 3),
          ("geeralPrinter", 4),
          ("mediaPath", 5),
          ("marker", 6),
          ("markerSupplies", 7),
          ("markerColorant", 8),
          ("fax", 21),
          ("scanner", 22),
          ("network", 23),
          ("usb", 24),
          ("parallel", 25),
          ("finisher", 26),
          ("motor", 41),
          ("smps", 42),
          ("memory", 43))
    )


_ScmDiagnosticsDeviceType_Type.__name__ = "Integer32"
_ScmDiagnosticsDeviceType_Object = MibTableColumn
scmDiagnosticsDeviceType = _ScmDiagnosticsDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 64, 1, 2, 1, 3),
    _ScmDiagnosticsDeviceType_Type()
)
scmDiagnosticsDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmDiagnosticsDeviceType.setStatus("current")


class _ScmDiagnosticsDeviceDescr_Type(DisplayString):
    """Custom type scmDiagnosticsDeviceDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ScmDiagnosticsDeviceDescr_Type.__name__ = "DisplayString"
_ScmDiagnosticsDeviceDescr_Object = MibTableColumn
scmDiagnosticsDeviceDescr = _ScmDiagnosticsDeviceDescr_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 64, 1, 2, 1, 4),
    _ScmDiagnosticsDeviceDescr_Type()
)
scmDiagnosticsDeviceDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmDiagnosticsDeviceDescr.setStatus("current")


class _ScmDiagnosticsDeviceID_Type(Integer32):
    """Custom type scmDiagnosticsDeviceID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ScmDiagnosticsDeviceID_Type.__name__ = "Integer32"
_ScmDiagnosticsDeviceID_Object = MibTableColumn
scmDiagnosticsDeviceID = _ScmDiagnosticsDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 64, 1, 2, 1, 5),
    _ScmDiagnosticsDeviceID_Type()
)
scmDiagnosticsDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmDiagnosticsDeviceID.setStatus("current")


class _ScmDiagnosticsDeviceStatus_Type(Integer32):
    """Custom type scmDiagnosticsDeviceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("running", 2),
          ("warning", 3),
          ("testing", 4),
          ("down", 5),
          ("printing", 6))
    )


_ScmDiagnosticsDeviceStatus_Type.__name__ = "Integer32"
_ScmDiagnosticsDeviceStatus_Object = MibTableColumn
scmDiagnosticsDeviceStatus = _ScmDiagnosticsDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 64, 1, 2, 1, 6),
    _ScmDiagnosticsDeviceStatus_Type()
)
scmDiagnosticsDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmDiagnosticsDeviceStatus.setStatus("current")
_ScmDiagnosticsDeviceErrors_Type = Counter32
_ScmDiagnosticsDeviceErrors_Object = MibTableColumn
scmDiagnosticsDeviceErrors = _ScmDiagnosticsDeviceErrors_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 64, 1, 2, 1, 7),
    _ScmDiagnosticsDeviceErrors_Type()
)
scmDiagnosticsDeviceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmDiagnosticsDeviceErrors.setStatus("current")


class _ScmDiagnosticsRequest_Type(Integer32):
    """Custom type scmDiagnosticsRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_ScmDiagnosticsRequest_Type.__name__ = "Integer32"
_ScmDiagnosticsRequest_Object = MibTableColumn
scmDiagnosticsRequest = _ScmDiagnosticsRequest_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 64, 1, 2, 1, 8),
    _ScmDiagnosticsRequest_Type()
)
scmDiagnosticsRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmDiagnosticsRequest.setStatus("current")


class _ScmGenBaseDeviceImageFileName_Type(DisplayString):
    """Custom type scmGenBaseDeviceImageFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ScmGenBaseDeviceImageFileName_Type.__name__ = "DisplayString"
_ScmGenBaseDeviceImageFileName_Object = MibTableColumn
scmGenBaseDeviceImageFileName = _ScmGenBaseDeviceImageFileName_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 64, 1, 2, 1, 999),
    _ScmGenBaseDeviceImageFileName_Type()
)
scmGenBaseDeviceImageFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmGenBaseDeviceImageFileName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SAMSUNG-DIAGNOSTICS-MIB",
    **{"scmDiagnostics": scmDiagnostics,
       "scmDiagnosticsDevice": scmDiagnosticsDevice,
       "scmDiagnosticsDeviceTable": scmDiagnosticsDeviceTable,
       "scmDiagnosticsDeviceEntry": scmDiagnosticsDeviceEntry,
       "scmDiagnosticsDeviceIndex": scmDiagnosticsDeviceIndex,
       "scmDiagnosticsDeviceItem": scmDiagnosticsDeviceItem,
       "scmDiagnosticsDeviceType": scmDiagnosticsDeviceType,
       "scmDiagnosticsDeviceDescr": scmDiagnosticsDeviceDescr,
       "scmDiagnosticsDeviceID": scmDiagnosticsDeviceID,
       "scmDiagnosticsDeviceStatus": scmDiagnosticsDeviceStatus,
       "scmDiagnosticsDeviceErrors": scmDiagnosticsDeviceErrors,
       "scmDiagnosticsRequest": scmDiagnosticsRequest,
       "scmGenBaseDeviceImageFileName": scmGenBaseDeviceImageFileName}
)
