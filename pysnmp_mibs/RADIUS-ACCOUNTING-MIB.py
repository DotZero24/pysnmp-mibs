# SNMP MIB module (RADIUS-ACCOUNTING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/RADIUS-ACCOUNTING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:52:31 2025
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

swRadiusAccountMGMTMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 55)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RadiusAccountCtrl_ObjectIdentity = ObjectIdentity
radiusAccountCtrl = _RadiusAccountCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 55, 1)
)


class _AccountingShellState_Type(Integer32):
    """Custom type accountingShellState based on Integer32"""
    defaultValue = 2

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


_AccountingShellState_Type.__name__ = "Integer32"
_AccountingShellState_Object = MibScalar
accountingShellState = _AccountingShellState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 55, 1, 1),
    _AccountingShellState_Type()
)
accountingShellState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accountingShellState.setStatus("current")


class _AccountingSystemState_Type(Integer32):
    """Custom type accountingSystemState based on Integer32"""
    defaultValue = 2

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


_AccountingSystemState_Type.__name__ = "Integer32"
_AccountingSystemState_Object = MibScalar
accountingSystemState = _AccountingSystemState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 55, 1, 2),
    _AccountingSystemState_Type()
)
accountingSystemState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accountingSystemState.setStatus("current")


class _AccountingNetworkState_Type(Integer32):
    """Custom type accountingNetworkState based on Integer32"""
    defaultValue = 2

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


_AccountingNetworkState_Type.__name__ = "Integer32"
_AccountingNetworkState_Object = MibScalar
accountingNetworkState = _AccountingNetworkState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 55, 1, 3),
    _AccountingNetworkState_Type()
)
accountingNetworkState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accountingNetworkState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADIUS-ACCOUNTING-MIB",
    **{"swRadiusAccountMGMTMIB": swRadiusAccountMGMTMIB,
       "radiusAccountCtrl": radiusAccountCtrl,
       "accountingShellState": accountingShellState,
       "accountingSystemState": accountingSystemState,
       "accountingNetworkState": accountingNetworkState}
)
