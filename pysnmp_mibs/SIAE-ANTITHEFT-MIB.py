# SNMP MIB module (SIAE-ANTITHEFT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/siaemic/SIAE-ANTITHEFT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:13:19 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(siaeMib,) = mibBuilder.importSymbols(
    "SIAE-TREE-MIB",
    "siaeMib")

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

antiTheft = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 105)
)
if mibBuilder.loadTexts:
    antiTheft.setRevisions(
        ("2019-03-25 00:00",
         "2018-09-14 00:00",
         "2018-03-15 00:00",
         "2017-01-09 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _AntiTheftMibVersion_Type(Integer32):
    """Custom type antiTheftMibVersion based on Integer32"""
    defaultValue = 1


_AntiTheftMibVersion_Type.__name__ = "Integer32"
_AntiTheftMibVersion_Object = MibScalar
antiTheftMibVersion = _AntiTheftMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 105, 1),
    _AntiTheftMibVersion_Type()
)
antiTheftMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    antiTheftMibVersion.setStatus("current")


class _AntiTheftEnable_Type(Integer32):
    """Custom type antiTheftEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AntiTheftEnable_Type.__name__ = "Integer32"
_AntiTheftEnable_Object = MibScalar
antiTheftEnable = _AntiTheftEnable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 105, 2),
    _AntiTheftEnable_Type()
)
antiTheftEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    antiTheftEnable.setStatus("current")
_AntiTheftLicense_Type = OctetString
_AntiTheftLicense_Object = MibScalar
antiTheftLicense = _AntiTheftLicense_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 105, 3),
    _AntiTheftLicense_Type()
)
antiTheftLicense.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    antiTheftLicense.setStatus("current")


class _AntiTheftStatus_Type(Integer32):
    """Custom type antiTheftStatus based on Integer32"""
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
        *(("unlockedUnbound", 1),
          ("unlockedBound", 2),
          ("locked", 3),
          ("notAvailable", 4))
    )


_AntiTheftStatus_Type.__name__ = "Integer32"
_AntiTheftStatus_Object = MibScalar
antiTheftStatus = _AntiTheftStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 105, 4),
    _AntiTheftStatus_Type()
)
antiTheftStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    antiTheftStatus.setStatus("current")


class _AntiTheftTimeout_Type(Integer32):
    """Custom type antiTheftTimeout based on Integer32"""
    defaultValue = 4320

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 43200),
    )


_AntiTheftTimeout_Type.__name__ = "Integer32"
_AntiTheftTimeout_Object = MibScalar
antiTheftTimeout = _AntiTheftTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 105, 5),
    _AntiTheftTimeout_Type()
)
antiTheftTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    antiTheftTimeout.setStatus("current")
if mibBuilder.loadTexts:
    antiTheftTimeout.setUnits("min")


class _AntiTheftCountdown_Type(Integer32):
    """Custom type antiTheftCountdown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 43200),
    )


_AntiTheftCountdown_Type.__name__ = "Integer32"
_AntiTheftCountdown_Object = MibScalar
antiTheftCountdown = _AntiTheftCountdown_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 105, 6),
    _AntiTheftCountdown_Type()
)
antiTheftCountdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    antiTheftCountdown.setStatus("current")
if mibBuilder.loadTexts:
    antiTheftCountdown.setUnits("min")


class _AntiTheftCustomer_Type(DisplayString):
    """Custom type antiTheftCustomer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 7),
    )


_AntiTheftCustomer_Type.__name__ = "DisplayString"
_AntiTheftCustomer_Object = MibScalar
antiTheftCustomer = _AntiTheftCustomer_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 105, 7),
    _AntiTheftCustomer_Type()
)
antiTheftCustomer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    antiTheftCustomer.setStatus("current")
_AntitheftPortMgtTable_Object = MibTable
antitheftPortMgtTable = _AntitheftPortMgtTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 105, 8)
)
if mibBuilder.loadTexts:
    antitheftPortMgtTable.setStatus("current")
_AntitheftPortMgtEntry_Object = MibTableRow
antitheftPortMgtEntry = _AntitheftPortMgtEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 105, 8, 1)
)
antitheftPortMgtEntry.setIndexNames(
    (0, "SIAE-ANTITHEFT-MIB", "antitheftPortIfIndex"),
)
if mibBuilder.loadTexts:
    antitheftPortMgtEntry.setStatus("current")
_AntitheftPortIfIndex_Type = InterfaceIndex
_AntitheftPortIfIndex_Object = MibTableColumn
antitheftPortIfIndex = _AntitheftPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 105, 8, 1, 1),
    _AntitheftPortIfIndex_Type()
)
antitheftPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    antitheftPortIfIndex.setStatus("current")


class _AntitheftPortLock_Type(Integer32):
    """Custom type antitheftPortLock based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2))
    )


_AntitheftPortLock_Type.__name__ = "Integer32"
_AntitheftPortLock_Object = MibTableColumn
antitheftPortLock = _AntitheftPortLock_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 105, 8, 1, 2),
    _AntitheftPortLock_Type()
)
antitheftPortLock.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    antitheftPortLock.setStatus("current")
_AntitheftPortRowStatus_Type = RowStatus
_AntitheftPortRowStatus_Object = MibTableColumn
antitheftPortRowStatus = _AntitheftPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 105, 8, 1, 3),
    _AntitheftPortRowStatus_Type()
)
antitheftPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    antitheftPortRowStatus.setStatus("current")


class _AntiTheftReconnectionTimeout_Type(Integer32):
    """Custom type antiTheftReconnectionTimeout based on Integer32"""
    defaultValue = 4320

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1440, 43200),
    )


_AntiTheftReconnectionTimeout_Type.__name__ = "Integer32"
_AntiTheftReconnectionTimeout_Object = MibScalar
antiTheftReconnectionTimeout = _AntiTheftReconnectionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 105, 9),
    _AntiTheftReconnectionTimeout_Type()
)
antiTheftReconnectionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    antiTheftReconnectionTimeout.setStatus("current")
if mibBuilder.loadTexts:
    antiTheftReconnectionTimeout.setUnits("min")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SIAE-ANTITHEFT-MIB",
    **{"antiTheft": antiTheft,
       "antiTheftMibVersion": antiTheftMibVersion,
       "antiTheftEnable": antiTheftEnable,
       "antiTheftLicense": antiTheftLicense,
       "antiTheftStatus": antiTheftStatus,
       "antiTheftTimeout": antiTheftTimeout,
       "antiTheftCountdown": antiTheftCountdown,
       "antiTheftCustomer": antiTheftCustomer,
       "antitheftPortMgtTable": antitheftPortMgtTable,
       "antitheftPortMgtEntry": antitheftPortMgtEntry,
       "antitheftPortIfIndex": antitheftPortIfIndex,
       "antitheftPortLock": antitheftPortLock,
       "antitheftPortRowStatus": antitheftPortRowStatus,
       "antiTheftReconnectionTimeout": antiTheftReconnectionTimeout}
)
