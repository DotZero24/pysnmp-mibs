# SNMP MIB module (H3C-SLBG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-SLBG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:19:38 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

h3cSlbg = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 130)
)
if mibBuilder.loadTexts:
    h3cSlbg.setRevisions(
        ("2012-10-16 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cSlbgMibTable_ObjectIdentity = ObjectIdentity
h3cSlbgMibTable = _H3cSlbgMibTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 130, 1)
)
_H3cSlbgGroupTable_Object = MibTable
h3cSlbgGroupTable = _H3cSlbgGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 130, 1, 1)
)
if mibBuilder.loadTexts:
    h3cSlbgGroupTable.setStatus("current")
_H3cSlbgGroupEntry_Object = MibTableRow
h3cSlbgGroupEntry = _H3cSlbgGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 130, 1, 1, 1)
)
h3cSlbgGroupEntry.setIndexNames(
    (0, "H3C-SLBG-MIB", "h3cSlbgGroupNumber"),
)
if mibBuilder.loadTexts:
    h3cSlbgGroupEntry.setStatus("current")
_H3cSlbgGroupNumber_Type = Unsigned32
_H3cSlbgGroupNumber_Object = MibTableColumn
h3cSlbgGroupNumber = _H3cSlbgGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 130, 1, 1, 1, 1),
    _H3cSlbgGroupNumber_Type()
)
h3cSlbgGroupNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cSlbgGroupNumber.setStatus("current")


class _H3cSlbgGroupSrvType_Type(Bits):
    """Custom type h3cSlbgGroupSrvType based on Bits"""
    namedValues = NamedValues(
        *(("ipv6", 0),
          ("ipv6mc", 1),
          ("tunnel", 2),
          ("multicastTunnel", 3),
          ("mpls", 4))
    )

_H3cSlbgGroupSrvType_Type.__name__ = "Bits"
_H3cSlbgGroupSrvType_Object = MibTableColumn
h3cSlbgGroupSrvType = _H3cSlbgGroupSrvType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 130, 1, 1, 1, 2),
    _H3cSlbgGroupSrvType_Type()
)
h3cSlbgGroupSrvType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSlbgGroupSrvType.setStatus("current")
_H3cSlbgGroupRowStatus_Type = RowStatus
_H3cSlbgGroupRowStatus_Object = MibTableColumn
h3cSlbgGroupRowStatus = _H3cSlbgGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 130, 1, 1, 1, 3),
    _H3cSlbgGroupRowStatus_Type()
)
h3cSlbgGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSlbgGroupRowStatus.setStatus("current")
_H3cSlbgPortTable_Object = MibTable
h3cSlbgPortTable = _H3cSlbgPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 130, 1, 2)
)
if mibBuilder.loadTexts:
    h3cSlbgPortTable.setStatus("current")
_H3cSlbgPortEntry_Object = MibTableRow
h3cSlbgPortEntry = _H3cSlbgPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 130, 1, 2, 1)
)
h3cSlbgPortEntry.setIndexNames(
    (0, "H3C-SLBG-MIB", "h3cSlbgPortIndex"),
)
if mibBuilder.loadTexts:
    h3cSlbgPortEntry.setStatus("current")
_H3cSlbgPortIndex_Type = InterfaceIndex
_H3cSlbgPortIndex_Object = MibTableColumn
h3cSlbgPortIndex = _H3cSlbgPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 130, 1, 2, 1, 1),
    _H3cSlbgPortIndex_Type()
)
h3cSlbgPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cSlbgPortIndex.setStatus("current")
_H3cSlbgPortAttachedGroupNumber_Type = Unsigned32
_H3cSlbgPortAttachedGroupNumber_Object = MibTableColumn
h3cSlbgPortAttachedGroupNumber = _H3cSlbgPortAttachedGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 130, 1, 2, 1, 2),
    _H3cSlbgPortAttachedGroupNumber_Type()
)
h3cSlbgPortAttachedGroupNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSlbgPortAttachedGroupNumber.setStatus("current")
_H3cSlbgPortSelectedGroupNumber_Type = Unsigned32
_H3cSlbgPortSelectedGroupNumber_Object = MibTableColumn
h3cSlbgPortSelectedGroupNumber = _H3cSlbgPortSelectedGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 130, 1, 2, 1, 3),
    _H3cSlbgPortSelectedGroupNumber_Type()
)
h3cSlbgPortSelectedGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSlbgPortSelectedGroupNumber.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-SLBG-MIB",
    **{"h3cSlbg": h3cSlbg,
       "h3cSlbgMibTable": h3cSlbgMibTable,
       "h3cSlbgGroupTable": h3cSlbgGroupTable,
       "h3cSlbgGroupEntry": h3cSlbgGroupEntry,
       "h3cSlbgGroupNumber": h3cSlbgGroupNumber,
       "h3cSlbgGroupSrvType": h3cSlbgGroupSrvType,
       "h3cSlbgGroupRowStatus": h3cSlbgGroupRowStatus,
       "h3cSlbgPortTable": h3cSlbgPortTable,
       "h3cSlbgPortEntry": h3cSlbgPortEntry,
       "h3cSlbgPortIndex": h3cSlbgPortIndex,
       "h3cSlbgPortAttachedGroupNumber": h3cSlbgPortAttachedGroupNumber,
       "h3cSlbgPortSelectedGroupNumber": h3cSlbgPortSelectedGroupNumber}
)
