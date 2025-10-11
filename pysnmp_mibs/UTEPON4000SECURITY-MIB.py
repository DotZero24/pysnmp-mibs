# SNMP MIB module (UTEPON4000SECURITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/utstarcom/UTEPON4000SECURITY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:46:45 2025
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

(BridgeId,
 MacAddress,
 Timeout) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "BridgeId",
    "MacAddress",
    "Timeout")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(utsGeponBBS4000,) = mibBuilder.importSymbols(
    "UTS-BBS-COMMON-MIB",
    "utsGeponBBS4000")


# MODULE-IDENTITY

utsGeponBBS4000Security = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1949, 1, 3, 10, 200, 6, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UtsEfmPonSecurityExt_ObjectIdentity = ObjectIdentity
utsEfmPonSecurityExt = _UtsEfmPonSecurityExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1949, 1, 3, 10, 200, 6, 5, 1)
)
_UtsEponSecExtObjects_ObjectIdentity = ObjectIdentity
utsEponSecExtObjects = _UtsEponSecExtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1949, 1, 3, 10, 200, 6, 5, 1, 1)
)
_UtsDot3SecurityMIB_ObjectIdentity = ObjectIdentity
utsDot3SecurityMIB = _UtsDot3SecurityMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1949, 1, 3, 10, 200, 6, 5, 1, 1, 1)
)
_UtsDot3SecurityObjects_ObjectIdentity = ObjectIdentity
utsDot3SecurityObjects = _UtsDot3SecurityObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1949, 1, 3, 10, 200, 6, 5, 1, 1, 1, 1)
)
_UtsDot3SecurityOltObjects_ObjectIdentity = ObjectIdentity
utsDot3SecurityOltObjects = _UtsDot3SecurityOltObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1949, 1, 3, 10, 200, 6, 5, 1, 1, 1, 1, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UTEPON4000SECURITY-MIB",
    **{"utsGeponBBS4000Security": utsGeponBBS4000Security,
       "utsEfmPonSecurityExt": utsEfmPonSecurityExt,
       "utsEponSecExtObjects": utsEponSecExtObjects,
       "utsDot3SecurityMIB": utsDot3SecurityMIB,
       "utsDot3SecurityObjects": utsDot3SecurityObjects,
       "utsDot3SecurityOltObjects": utsDot3SecurityOltObjects}
)
