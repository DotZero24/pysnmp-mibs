# SNMP MIB module (ZTE-DSL-SSH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-DSL-SSH-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:45:15 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

zxDslSshMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 35)
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
_ZxDslSshglobal_ObjectIdentity = ObjectIdentity
zxDslSshglobal = _ZxDslSshglobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 35, 1)
)


class _ZxDslSshGlobalState_Type(Integer32):
    """Custom type zxDslSshGlobalState based on Integer32"""
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


_ZxDslSshGlobalState_Type.__name__ = "Integer32"
_ZxDslSshGlobalState_Object = MibScalar
zxDslSshGlobalState = _ZxDslSshGlobalState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 35, 1, 1),
    _ZxDslSshGlobalState_Type()
)
zxDslSshGlobalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslSshGlobalState.setStatus("current")


class _ZxDslSshAuthMode_Type(Integer32):
    """Custom type zxDslSshAuthMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("radius", 2))
    )


_ZxDslSshAuthMode_Type.__name__ = "Integer32"
_ZxDslSshAuthMode_Object = MibScalar
zxDslSshAuthMode = _ZxDslSshAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 35, 1, 2),
    _ZxDslSshAuthMode_Type()
)
zxDslSshAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslSshAuthMode.setStatus("current")


class _ZxDslSshAuthType_Type(Integer32):
    """Custom type zxDslSshAuthType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pap", 1),
          ("chap", 2))
    )


_ZxDslSshAuthType_Type.__name__ = "Integer32"
_ZxDslSshAuthType_Object = MibScalar
zxDslSshAuthType = _ZxDslSshAuthType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 35, 1, 3),
    _ZxDslSshAuthType_Type()
)
zxDslSshAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslSshAuthType.setStatus("current")


class _ZxDslSshGenKey_Type(Integer32):
    """Custom type zxDslSshGenKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("value", 1)
    )


_ZxDslSshGenKey_Type.__name__ = "Integer32"
_ZxDslSshGenKey_Object = MibScalar
zxDslSshGenKey = _ZxDslSshGenKey_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 35, 1, 4),
    _ZxDslSshGenKey_Type()
)
zxDslSshGenKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslSshGenKey.setStatus("current")


class _ZxDslSshServOnly_Type(Integer32):
    """Custom type zxDslSshServOnly based on Integer32"""
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


_ZxDslSshServOnly_Type.__name__ = "Integer32"
_ZxDslSshServOnly_Object = MibScalar
zxDslSshServOnly = _ZxDslSshServOnly_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 35, 1, 5),
    _ZxDslSshServOnly_Type()
)
zxDslSshServOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslSshServOnly.setStatus("current")


class _ZxDslSshVersion_Type(Integer32):
    """Custom type zxDslSshVersion based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sshv1", 1),
          ("sshv2", 2))
    )


_ZxDslSshVersion_Type.__name__ = "Integer32"
_ZxDslSshVersion_Object = MibScalar
zxDslSshVersion = _ZxDslSshVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 35, 1, 6),
    _ZxDslSshVersion_Type()
)
zxDslSshVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslSshVersion.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-DSL-SSH-MIB",
    **{"zte": zte,
       "zxDsl": zxDsl,
       "zxDslSshMib": zxDslSshMib,
       "zxDslSshglobal": zxDslSshglobal,
       "zxDslSshGlobalState": zxDslSshGlobalState,
       "zxDslSshAuthMode": zxDslSshAuthMode,
       "zxDslSshAuthType": zxDslSshAuthType,
       "zxDslSshGenKey": zxDslSshGenKey,
       "zxDslSshServOnly": zxDslSshServOnly,
       "zxDslSshVersion": zxDslSshVersion}
)
