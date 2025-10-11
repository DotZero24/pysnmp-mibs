# SNMP MIB module (CPQHOST2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/CPQHOST2-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:42:41 2025
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

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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
 NotificationType,
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
    "NotificationType",
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Compaq_ObjectIdentity = ObjectIdentity
compaq = _Compaq_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232)
)
_CpqHostOs_ObjectIdentity = ObjectIdentity
cpqHostOs = _CpqHostOs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 11)
)
_CpqHoComponent_ObjectIdentity = ObjectIdentity
cpqHoComponent = _CpqHoComponent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 11, 2)
)
_CpqHoClients_ObjectIdentity = ObjectIdentity
cpqHoClients = _CpqHoClients_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 12)
)


class _CpqHoClientLastModified_Type(OctetString):
    """Custom type cpqHoClientLastModified based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )
    fixed_length = 7


_CpqHoClientLastModified_Type.__name__ = "OctetString"
_CpqHoClientLastModified_Object = MibScalar
cpqHoClientLastModified = _CpqHoClientLastModified_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 12, 1),
    _CpqHoClientLastModified_Type()
)
cpqHoClientLastModified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoClientLastModified.setStatus("mandatory")


class _CpqHoClientDelete_Type(DisplayString):
    """Custom type cpqHoClientDelete based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CpqHoClientDelete_Type.__name__ = "DisplayString"
_CpqHoClientDelete_Object = MibScalar
cpqHoClientDelete = _CpqHoClientDelete_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 12, 2),
    _CpqHoClientDelete_Type()
)
cpqHoClientDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqHoClientDelete.setStatus("mandatory")
_CpqHoClientTable_Object = MibTable
cpqHoClientTable = _CpqHoClientTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 12, 3)
)
if mibBuilder.loadTexts:
    cpqHoClientTable.setStatus("mandatory")
_CpqHoClientEntry_Object = MibTableRow
cpqHoClientEntry = _CpqHoClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 12, 3, 1)
)
cpqHoClientEntry.setIndexNames(
    (0, "CPQHOST2-MIB", "cpqHoClientIndex"),
)
if mibBuilder.loadTexts:
    cpqHoClientEntry.setStatus("mandatory")


class _CpqHoClientIndex_Type(Integer32):
    """Custom type cpqHoClientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqHoClientIndex_Type.__name__ = "Integer32"
_CpqHoClientIndex_Object = MibTableColumn
cpqHoClientIndex = _CpqHoClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 12, 3, 1, 1),
    _CpqHoClientIndex_Type()
)
cpqHoClientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoClientIndex.setStatus("mandatory")


class _CpqHoClientName_Type(DisplayString):
    """Custom type cpqHoClientName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CpqHoClientName_Type.__name__ = "DisplayString"
_CpqHoClientName_Object = MibTableColumn
cpqHoClientName = _CpqHoClientName_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 12, 3, 1, 2),
    _CpqHoClientName_Type()
)
cpqHoClientName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoClientName.setStatus("mandatory")


class _CpqHoClientIpxAddress_Type(OctetString):
    """Custom type cpqHoClientIpxAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_CpqHoClientIpxAddress_Type.__name__ = "OctetString"
_CpqHoClientIpxAddress_Object = MibTableColumn
cpqHoClientIpxAddress = _CpqHoClientIpxAddress_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 12, 3, 1, 3),
    _CpqHoClientIpxAddress_Type()
)
cpqHoClientIpxAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoClientIpxAddress.setStatus("mandatory")
_CpqHoClientIpAddress_Type = IpAddress
_CpqHoClientIpAddress_Object = MibTableColumn
cpqHoClientIpAddress = _CpqHoClientIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 12, 3, 1, 4),
    _CpqHoClientIpAddress_Type()
)
cpqHoClientIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoClientIpAddress.setStatus("mandatory")


class _CpqHoClientCommunity_Type(DisplayString):
    """Custom type cpqHoClientCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_CpqHoClientCommunity_Type.__name__ = "DisplayString"
_CpqHoClientCommunity_Object = MibTableColumn
cpqHoClientCommunity = _CpqHoClientCommunity_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 12, 3, 1, 5),
    _CpqHoClientCommunity_Type()
)
cpqHoClientCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoClientCommunity.setStatus("mandatory")


class _CpqHoClientID_Type(OctetString):
    """Custom type cpqHoClientID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_CpqHoClientID_Type.__name__ = "OctetString"
_CpqHoClientID_Object = MibTableColumn
cpqHoClientID = _CpqHoClientID_Object(
    (1, 3, 6, 1, 4, 1, 232, 11, 2, 12, 3, 1, 6),
    _CpqHoClientID_Type()
)
cpqHoClientID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqHoClientID.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CPQHOST2-MIB",
    **{"compaq": compaq,
       "cpqHostOs": cpqHostOs,
       "cpqHoComponent": cpqHoComponent,
       "cpqHoClients": cpqHoClients,
       "cpqHoClientLastModified": cpqHoClientLastModified,
       "cpqHoClientDelete": cpqHoClientDelete,
       "cpqHoClientTable": cpqHoClientTable,
       "cpqHoClientEntry": cpqHoClientEntry,
       "cpqHoClientIndex": cpqHoClientIndex,
       "cpqHoClientName": cpqHoClientName,
       "cpqHoClientIpxAddress": cpqHoClientIpxAddress,
       "cpqHoClientIpAddress": cpqHoClientIpAddress,
       "cpqHoClientCommunity": cpqHoClientCommunity,
       "cpqHoClientID": cpqHoClientID}
)
