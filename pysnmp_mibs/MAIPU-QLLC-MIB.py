# SNMP MIB module (MAIPU-QLLC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/maipu/MAIPU-QLLC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:11:14 2025
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

(mpMgmt,) = mibBuilder.importSymbols(
    "MAIPU-SMI",
    "mpMgmt")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

mpQllcMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 100)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QllcConfTable_Object = MibTable
qllcConfTable = _QllcConfTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 100, 1)
)
if mibBuilder.loadTexts:
    qllcConfTable.setStatus("current")
_QllcConfEntry_Object = MibTableRow
qllcConfEntry = _QllcConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 100, 1, 1)
)
qllcConfEntry.setIndexNames(
    (0, "MAIPU-QLLC-MIB", "qllcIndex"),
)
if mibBuilder.loadTexts:
    qllcConfEntry.setStatus("current")
_QllcIndex_Type = Integer32
_QllcIndex_Object = MibTableColumn
qllcIndex = _QllcIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 100, 1, 1, 1),
    _QllcIndex_Type()
)
qllcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qllcIndex.setStatus("current")


class _QllcFlag_Type(Integer32):
    """Custom type qllcFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("pvc", 2),
          ("vmacaddr", 3))
    )


_QllcFlag_Type.__name__ = "Integer32"
_QllcFlag_Object = MibTableColumn
qllcFlag = _QllcFlag_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 100, 1, 1, 2),
    _QllcFlag_Type()
)
qllcFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qllcFlag.setStatus("current")


class _QllcPartner_Type(OctetString):
    """Custom type qllcPartner based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(14, 14),
    )
    fixed_length = 14


_QllcPartner_Type.__name__ = "OctetString"
_QllcPartner_Object = MibTableColumn
qllcPartner = _QllcPartner_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 100, 1, 1, 3),
    _QllcPartner_Type()
)
qllcPartner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qllcPartner.setStatus("current")


class _QllcXidDivert_Type(Integer32):
    """Custom type qllcXidDivert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("divert", 2))
    )


_QllcXidDivert_Type.__name__ = "Integer32"
_QllcXidDivert_Object = MibTableColumn
qllcXidDivert = _QllcXidDivert_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 100, 1, 1, 4),
    _QllcXidDivert_Type()
)
qllcXidDivert.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qllcXidDivert.setStatus("current")


class _QllcPvc_Type(Integer32):
    """Custom type qllcPvc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_QllcPvc_Type.__name__ = "Integer32"
_QllcPvc_Object = MibTableColumn
qllcPvc = _QllcPvc_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 100, 1, 1, 5),
    _QllcPvc_Type()
)
qllcPvc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qllcPvc.setStatus("current")


class _QllcOrigin_Type(OctetString):
    """Custom type qllcOrigin based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(14, 14),
    )
    fixed_length = 14


_QllcOrigin_Type.__name__ = "OctetString"
_QllcOrigin_Object = MibTableColumn
qllcOrigin = _QllcOrigin_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 100, 1, 1, 6),
    _QllcOrigin_Type()
)
qllcOrigin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qllcOrigin.setStatus("current")
_QllcStatus_Type = RowStatus
_QllcStatus_Object = MibTableColumn
qllcStatus = _QllcStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 100, 1, 1, 7),
    _QllcStatus_Type()
)
qllcStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qllcStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MAIPU-QLLC-MIB",
    **{"mpQllcMib": mpQllcMib,
       "qllcConfTable": qllcConfTable,
       "qllcConfEntry": qllcConfEntry,
       "qllcIndex": qllcIndex,
       "qllcFlag": qllcFlag,
       "qllcPartner": qllcPartner,
       "qllcXidDivert": qllcXidDivert,
       "qllcPvc": qllcPvc,
       "qllcOrigin": qllcOrigin,
       "qllcStatus": qllcStatus}
)
