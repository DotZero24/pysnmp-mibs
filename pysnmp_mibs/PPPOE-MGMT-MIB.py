# SNMP MIB module (PPPOE-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/PPPOE-MGMT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:52:05 2025
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

(dlink_common_mgmt,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-common-mgmt")

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

swPPPoEMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 79)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwPPPoEMgmtCtrl_ObjectIdentity = ObjectIdentity
swPPPoEMgmtCtrl = _SwPPPoEMgmtCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 79, 1)
)


class _SwPPPoECirIDInsertState_Type(Integer32):
    """Custom type swPPPoECirIDInsertState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SwPPPoECirIDInsertState_Type.__name__ = "Integer32"
_SwPPPoECirIDInsertState_Object = MibScalar
swPPPoECirIDInsertState = _SwPPPoECirIDInsertState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 79, 1, 1),
    _SwPPPoECirIDInsertState_Type()
)
swPPPoECirIDInsertState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPPPoECirIDInsertState.setStatus("current")
_SwPPPoECirIDInsertPortMgmt_ObjectIdentity = ObjectIdentity
swPPPoECirIDInsertPortMgmt = _SwPPPoECirIDInsertPortMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 79, 1, 2)
)
_SwPPPoECirIDInsertPortTable_Object = MibTable
swPPPoECirIDInsertPortTable = _SwPPPoECirIDInsertPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 79, 1, 2, 1)
)
if mibBuilder.loadTexts:
    swPPPoECirIDInsertPortTable.setStatus("current")
_SwPPPoECirIDInsertPortEntry_Object = MibTableRow
swPPPoECirIDInsertPortEntry = _SwPPPoECirIDInsertPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 79, 1, 2, 1, 1)
)
swPPPoECirIDInsertPortEntry.setIndexNames(
    (0, "PPPOE-MGMT-MIB", "swPPPoECirIDInsertPortIndex"),
)
if mibBuilder.loadTexts:
    swPPPoECirIDInsertPortEntry.setStatus("current")


class _SwPPPoECirIDInsertPortIndex_Type(Integer32):
    """Custom type swPPPoECirIDInsertPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwPPPoECirIDInsertPortIndex_Type.__name__ = "Integer32"
_SwPPPoECirIDInsertPortIndex_Object = MibTableColumn
swPPPoECirIDInsertPortIndex = _SwPPPoECirIDInsertPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 79, 1, 2, 1, 1, 1),
    _SwPPPoECirIDInsertPortIndex_Type()
)
swPPPoECirIDInsertPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swPPPoECirIDInsertPortIndex.setStatus("current")


class _SwPPPoECirIDInsertPortState_Type(Integer32):
    """Custom type swPPPoECirIDInsertPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SwPPPoECirIDInsertPortState_Type.__name__ = "Integer32"
_SwPPPoECirIDInsertPortState_Object = MibTableColumn
swPPPoECirIDInsertPortState = _SwPPPoECirIDInsertPortState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 79, 1, 2, 1, 1, 2),
    _SwPPPoECirIDInsertPortState_Type()
)
swPPPoECirIDInsertPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPPPoECirIDInsertPortState.setStatus("current")


class _SwPPPoECirIDInsertPortCirID_Type(Integer32):
    """Custom type swPPPoECirIDInsertPortCirID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("switch-ip", 1),
          ("switch-mac", 2),
          ("udf-string", 3))
    )


_SwPPPoECirIDInsertPortCirID_Type.__name__ = "Integer32"
_SwPPPoECirIDInsertPortCirID_Object = MibTableColumn
swPPPoECirIDInsertPortCirID = _SwPPPoECirIDInsertPortCirID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 79, 1, 2, 1, 1, 3),
    _SwPPPoECirIDInsertPortCirID_Type()
)
swPPPoECirIDInsertPortCirID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPPPoECirIDInsertPortCirID.setStatus("current")
_SwPPPoECirIDInsertPortUDFString_Type = DisplayString
_SwPPPoECirIDInsertPortUDFString_Object = MibTableColumn
swPPPoECirIDInsertPortUDFString = _SwPPPoECirIDInsertPortUDFString_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 79, 1, 2, 1, 1, 4),
    _SwPPPoECirIDInsertPortUDFString_Type()
)
swPPPoECirIDInsertPortUDFString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPPPoECirIDInsertPortUDFString.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PPPOE-MGMT-MIB",
    **{"swPPPoEMIB": swPPPoEMIB,
       "swPPPoEMgmtCtrl": swPPPoEMgmtCtrl,
       "swPPPoECirIDInsertState": swPPPoECirIDInsertState,
       "swPPPoECirIDInsertPortMgmt": swPPPoECirIDInsertPortMgmt,
       "swPPPoECirIDInsertPortTable": swPPPoECirIDInsertPortTable,
       "swPPPoECirIDInsertPortEntry": swPPPoECirIDInsertPortEntry,
       "swPPPoECirIDInsertPortIndex": swPPPoECirIDInsertPortIndex,
       "swPPPoECirIDInsertPortState": swPPPoECirIDInsertPortState,
       "swPPPoECirIDInsertPortCirID": swPPPoECirIDInsertPortCirID,
       "swPPPoECirIDInsertPortUDFString": swPPPoECirIDInsertPortUDFString}
)
