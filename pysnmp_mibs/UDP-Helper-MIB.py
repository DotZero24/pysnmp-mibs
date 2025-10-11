# SNMP MIB module (UDP-Helper-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/UDP-Helper-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:51:28 2025
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

swUDPHelperMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 99)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwUDPHelperMIBObjects_ObjectIdentity = ObjectIdentity
swUDPHelperMIBObjects = _SwUDPHelperMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 99, 1)
)
_SwUDPHelperGeneralGroup_ObjectIdentity = ObjectIdentity
swUDPHelperGeneralGroup = _SwUDPHelperGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 99, 1, 1)
)


class _SwUDPHelperState_Type(Integer32):
    """Custom type swUDPHelperState based on Integer32"""
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


_SwUDPHelperState_Type.__name__ = "Integer32"
_SwUDPHelperState_Object = MibScalar
swUDPHelperState = _SwUDPHelperState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 99, 1, 1, 1),
    _SwUDPHelperState_Type()
)
swUDPHelperState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swUDPHelperState.setStatus("current")
_SwUDPHelperPortCtrlTable_Object = MibTable
swUDPHelperPortCtrlTable = _SwUDPHelperPortCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 99, 1, 2)
)
if mibBuilder.loadTexts:
    swUDPHelperPortCtrlTable.setStatus("current")
_SwUDPHelperPortCtrlEntry_Object = MibTableRow
swUDPHelperPortCtrlEntry = _SwUDPHelperPortCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 99, 1, 2, 1)
)
swUDPHelperPortCtrlEntry.setIndexNames(
    (0, "UDP-Helper-MIB", "swUDPHelperPortNumber"),
)
if mibBuilder.loadTexts:
    swUDPHelperPortCtrlEntry.setStatus("current")
_SwUDPHelperPortNumber_Type = Integer32
_SwUDPHelperPortNumber_Object = MibTableColumn
swUDPHelperPortNumber = _SwUDPHelperPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 99, 1, 2, 1, 1),
    _SwUDPHelperPortNumber_Type()
)
swUDPHelperPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swUDPHelperPortNumber.setStatus("current")
_SwUDPHelperPortCtrlRowStatus_Type = RowStatus
_SwUDPHelperPortCtrlRowStatus_Object = MibTableColumn
swUDPHelperPortCtrlRowStatus = _SwUDPHelperPortCtrlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 99, 1, 2, 1, 2),
    _SwUDPHelperPortCtrlRowStatus_Type()
)
swUDPHelperPortCtrlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swUDPHelperPortCtrlRowStatus.setStatus("current")
_SwUDPHelperServerCtrlTable_Object = MibTable
swUDPHelperServerCtrlTable = _SwUDPHelperServerCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 99, 1, 3)
)
if mibBuilder.loadTexts:
    swUDPHelperServerCtrlTable.setStatus("current")
_SwUDPHelperServerCtrlEntry_Object = MibTableRow
swUDPHelperServerCtrlEntry = _SwUDPHelperServerCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 99, 1, 3, 1)
)
swUDPHelperServerCtrlEntry.setIndexNames(
    (0, "UDP-Helper-MIB", "swUDPHelperServerCtrlInterfaceName"),
    (0, "UDP-Helper-MIB", "swUDPHelperServerCtrlServer"),
)
if mibBuilder.loadTexts:
    swUDPHelperServerCtrlEntry.setStatus("current")


class _SwUDPHelperServerCtrlInterfaceName_Type(DisplayString):
    """Custom type swUDPHelperServerCtrlInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_SwUDPHelperServerCtrlInterfaceName_Type.__name__ = "DisplayString"
_SwUDPHelperServerCtrlInterfaceName_Object = MibTableColumn
swUDPHelperServerCtrlInterfaceName = _SwUDPHelperServerCtrlInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 99, 1, 3, 1, 1),
    _SwUDPHelperServerCtrlInterfaceName_Type()
)
swUDPHelperServerCtrlInterfaceName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swUDPHelperServerCtrlInterfaceName.setStatus("current")
_SwUDPHelperServerCtrlServer_Type = IpAddress
_SwUDPHelperServerCtrlServer_Object = MibTableColumn
swUDPHelperServerCtrlServer = _SwUDPHelperServerCtrlServer_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 99, 1, 3, 1, 2),
    _SwUDPHelperServerCtrlServer_Type()
)
swUDPHelperServerCtrlServer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swUDPHelperServerCtrlServer.setStatus("current")
_SwUDPHelperServerCtrlRowStatus_Type = RowStatus
_SwUDPHelperServerCtrlRowStatus_Object = MibTableColumn
swUDPHelperServerCtrlRowStatus = _SwUDPHelperServerCtrlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 99, 1, 3, 1, 3),
    _SwUDPHelperServerCtrlRowStatus_Type()
)
swUDPHelperServerCtrlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swUDPHelperServerCtrlRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UDP-Helper-MIB",
    **{"swUDPHelperMIB": swUDPHelperMIB,
       "swUDPHelperMIBObjects": swUDPHelperMIBObjects,
       "swUDPHelperGeneralGroup": swUDPHelperGeneralGroup,
       "swUDPHelperState": swUDPHelperState,
       "swUDPHelperPortCtrlTable": swUDPHelperPortCtrlTable,
       "swUDPHelperPortCtrlEntry": swUDPHelperPortCtrlEntry,
       "swUDPHelperPortNumber": swUDPHelperPortNumber,
       "swUDPHelperPortCtrlRowStatus": swUDPHelperPortCtrlRowStatus,
       "swUDPHelperServerCtrlTable": swUDPHelperServerCtrlTable,
       "swUDPHelperServerCtrlEntry": swUDPHelperServerCtrlEntry,
       "swUDPHelperServerCtrlInterfaceName": swUDPHelperServerCtrlInterfaceName,
       "swUDPHelperServerCtrlServer": swUDPHelperServerCtrlServer,
       "swUDPHelperServerCtrlRowStatus": swUDPHelperServerCtrlRowStatus}
)
