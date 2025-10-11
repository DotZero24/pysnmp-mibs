# SNMP MIB module (ZET-DSL-RADIUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZET-DSL-RADIUS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:44:08 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

zxDslRadiusMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 34)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Zte_ObjectIdentity = ObjectIdentity
zte = _Zte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902)
)
_ZxDsl_ObjectIdentity = ObjectIdentity
zxDsl = _ZxDsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004)
)
_ZxDslRadiusClient_ObjectIdentity = ObjectIdentity
zxDslRadiusClient = _ZxDslRadiusClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 34, 1)
)
_ZxDslRadiusClientAuthSvrTable_Object = MibTable
zxDslRadiusClientAuthSvrTable = _ZxDslRadiusClientAuthSvrTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 34, 1, 1)
)
if mibBuilder.loadTexts:
    zxDslRadiusClientAuthSvrTable.setStatus("current")
_ZxDslRadiusClientAuthSvrEntry_Object = MibTableRow
zxDslRadiusClientAuthSvrEntry = _ZxDslRadiusClientAuthSvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 34, 1, 1, 1)
)
zxDslRadiusClientAuthSvrEntry.setIndexNames(
    (0, "ZET-DSL-RADIUS-MIB", "zxDslRadiusClientAuthSvrIndex"),
)
if mibBuilder.loadTexts:
    zxDslRadiusClientAuthSvrEntry.setStatus("current")
_ZxDslRadiusClientAuthSvrIndex_Type = Integer32
_ZxDslRadiusClientAuthSvrIndex_Object = MibTableColumn
zxDslRadiusClientAuthSvrIndex = _ZxDslRadiusClientAuthSvrIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 34, 1, 1, 1, 1),
    _ZxDslRadiusClientAuthSvrIndex_Type()
)
zxDslRadiusClientAuthSvrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxDslRadiusClientAuthSvrIndex.setStatus("current")
_ZxDslRadiusClientAuthAddress_Type = IpAddress
_ZxDslRadiusClientAuthAddress_Object = MibTableColumn
zxDslRadiusClientAuthAddress = _ZxDslRadiusClientAuthAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 34, 1, 1, 1, 2),
    _ZxDslRadiusClientAuthAddress_Type()
)
zxDslRadiusClientAuthAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslRadiusClientAuthAddress.setStatus("current")
_ZxDslRadiusClientAuthPortNumber_Type = Integer32
_ZxDslRadiusClientAuthPortNumber_Object = MibTableColumn
zxDslRadiusClientAuthPortNumber = _ZxDslRadiusClientAuthPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 34, 1, 1, 1, 3),
    _ZxDslRadiusClientAuthPortNumber_Type()
)
zxDslRadiusClientAuthPortNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslRadiusClientAuthPortNumber.setStatus("current")


class _ZxDslRadiusClientAuthSecret_Type(DisplayString):
    """Custom type zxDslRadiusClientAuthSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxDslRadiusClientAuthSecret_Type.__name__ = "DisplayString"
_ZxDslRadiusClientAuthSecret_Object = MibTableColumn
zxDslRadiusClientAuthSecret = _ZxDslRadiusClientAuthSecret_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 34, 1, 1, 1, 4),
    _ZxDslRadiusClientAuthSecret_Type()
)
zxDslRadiusClientAuthSecret.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslRadiusClientAuthSecret.setStatus("current")
_ZxDslRadiusClientAuthRowStatus_Type = RowStatus
_ZxDslRadiusClientAuthRowStatus_Object = MibTableColumn
zxDslRadiusClientAuthRowStatus = _ZxDslRadiusClientAuthRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 34, 1, 1, 1, 5),
    _ZxDslRadiusClientAuthRowStatus_Type()
)
zxDslRadiusClientAuthRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslRadiusClientAuthRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZET-DSL-RADIUS-MIB",
    **{"zte": zte,
       "zxDsl": zxDsl,
       "zxDslRadiusMib": zxDslRadiusMib,
       "zxDslRadiusClient": zxDslRadiusClient,
       "zxDslRadiusClientAuthSvrTable": zxDslRadiusClientAuthSvrTable,
       "zxDslRadiusClientAuthSvrEntry": zxDslRadiusClientAuthSvrEntry,
       "zxDslRadiusClientAuthSvrIndex": zxDslRadiusClientAuthSvrIndex,
       "zxDslRadiusClientAuthAddress": zxDslRadiusClientAuthAddress,
       "zxDslRadiusClientAuthPortNumber": zxDslRadiusClientAuthPortNumber,
       "zxDslRadiusClientAuthSecret": zxDslRadiusClientAuthSecret,
       "zxDslRadiusClientAuthRowStatus": zxDslRadiusClientAuthRowStatus}
)
