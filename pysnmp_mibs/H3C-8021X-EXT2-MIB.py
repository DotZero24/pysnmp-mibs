# SNMP MIB module (H3C-8021X-EXT2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-8021X-EXT2-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:20:21 2025
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

(dot1xPaePortNumber,) = mibBuilder.importSymbols(
    "IEEE8021-PAE-MIB",
    "dot1xPaePortNumber")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

h3c8021XExt2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 153)
)
if mibBuilder.loadTexts:
    h3c8021XExt2.setRevisions(
        ("2014-03-27 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3c8021XExt2MibObjects_ObjectIdentity = ObjectIdentity
h3c8021XExt2MibObjects = _H3c8021XExt2MibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 153, 1)
)
_H3c8021XExt2System_ObjectIdentity = ObjectIdentity
h3c8021XExt2System = _H3c8021XExt2System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 153, 1, 1)
)


class _H3c8021XExt2AuthQuietPeriod_Type(Unsigned32):
    """Custom type h3c8021XExt2AuthQuietPeriod based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 120),
    )


_H3c8021XExt2AuthQuietPeriod_Type.__name__ = "Unsigned32"
_H3c8021XExt2AuthQuietPeriod_Object = MibScalar
h3c8021XExt2AuthQuietPeriod = _H3c8021XExt2AuthQuietPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 153, 1, 1, 1),
    _H3c8021XExt2AuthQuietPeriod_Type()
)
h3c8021XExt2AuthQuietPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3c8021XExt2AuthQuietPeriod.setStatus("current")


class _H3c8021XExt2AuthTxPeriod_Type(Unsigned32):
    """Custom type h3c8021XExt2AuthTxPeriod based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 120),
    )


_H3c8021XExt2AuthTxPeriod_Type.__name__ = "Unsigned32"
_H3c8021XExt2AuthTxPeriod_Object = MibScalar
h3c8021XExt2AuthTxPeriod = _H3c8021XExt2AuthTxPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 153, 1, 1, 2),
    _H3c8021XExt2AuthTxPeriod_Type()
)
h3c8021XExt2AuthTxPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3c8021XExt2AuthTxPeriod.setStatus("current")


class _H3c8021XExt2AuthSuppTimeout_Type(Unsigned32):
    """Custom type h3c8021XExt2AuthSuppTimeout based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_H3c8021XExt2AuthSuppTimeout_Type.__name__ = "Unsigned32"
_H3c8021XExt2AuthSuppTimeout_Object = MibScalar
h3c8021XExt2AuthSuppTimeout = _H3c8021XExt2AuthSuppTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 153, 1, 1, 3),
    _H3c8021XExt2AuthSuppTimeout_Type()
)
h3c8021XExt2AuthSuppTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3c8021XExt2AuthSuppTimeout.setStatus("current")


class _H3c8021XExt2AuthServerTimeout_Type(Unsigned32):
    """Custom type h3c8021XExt2AuthServerTimeout based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 300),
    )


_H3c8021XExt2AuthServerTimeout_Type.__name__ = "Unsigned32"
_H3c8021XExt2AuthServerTimeout_Object = MibScalar
h3c8021XExt2AuthServerTimeout = _H3c8021XExt2AuthServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 153, 1, 1, 4),
    _H3c8021XExt2AuthServerTimeout_Type()
)
h3c8021XExt2AuthServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3c8021XExt2AuthServerTimeout.setStatus("current")


class _H3c8021XExt2AuthMaxReq_Type(Unsigned32):
    """Custom type h3c8021XExt2AuthMaxReq based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_H3c8021XExt2AuthMaxReq_Type.__name__ = "Unsigned32"
_H3c8021XExt2AuthMaxReq_Object = MibScalar
h3c8021XExt2AuthMaxReq = _H3c8021XExt2AuthMaxReq_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 153, 1, 1, 5),
    _H3c8021XExt2AuthMaxReq_Type()
)
h3c8021XExt2AuthMaxReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3c8021XExt2AuthMaxReq.setStatus("current")


class _H3c8021XExt2AuthReAuthPeriod_Type(Unsigned32):
    """Custom type h3c8021XExt2AuthReAuthPeriod based on Unsigned32"""
    defaultValue = 3600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 7200),
    )


_H3c8021XExt2AuthReAuthPeriod_Type.__name__ = "Unsigned32"
_H3c8021XExt2AuthReAuthPeriod_Object = MibScalar
h3c8021XExt2AuthReAuthPeriod = _H3c8021XExt2AuthReAuthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 153, 1, 1, 6),
    _H3c8021XExt2AuthReAuthPeriod_Type()
)
h3c8021XExt2AuthReAuthPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3c8021XExt2AuthReAuthPeriod.setStatus("current")


class _H3c8021XExt2AuthMethod_Type(Integer32):
    """Custom type h3c8021XExt2AuthMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("chap", 1),
          ("pap", 2),
          ("eap", 3))
    )


_H3c8021XExt2AuthMethod_Type.__name__ = "Integer32"
_H3c8021XExt2AuthMethod_Object = MibScalar
h3c8021XExt2AuthMethod = _H3c8021XExt2AuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 153, 1, 1, 7),
    _H3c8021XExt2AuthMethod_Type()
)
h3c8021XExt2AuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3c8021XExt2AuthMethod.setStatus("current")
_H3c8021XExt2Authenticator_ObjectIdentity = ObjectIdentity
h3c8021XExt2Authenticator = _H3c8021XExt2Authenticator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 153, 1, 2)
)
_H3c8021XExt2AuthConfigExtTable_Object = MibTable
h3c8021XExt2AuthConfigExtTable = _H3c8021XExt2AuthConfigExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 153, 1, 2, 1)
)
if mibBuilder.loadTexts:
    h3c8021XExt2AuthConfigExtTable.setStatus("current")
_H3c8021XExt2AuthConfigExtEntry_Object = MibTableRow
h3c8021XExt2AuthConfigExtEntry = _H3c8021XExt2AuthConfigExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 153, 1, 2, 1, 1)
)
h3c8021XExt2AuthConfigExtEntry.setIndexNames(
    (0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"),
)
if mibBuilder.loadTexts:
    h3c8021XExt2AuthConfigExtEntry.setStatus("current")


class _H3c8021XExt2PaePortAuthAdminStatus_Type(TruthValue):
    """Custom type h3c8021XExt2PaePortAuthAdminStatus based on TruthValue"""
    defaultValue = 2


_H3c8021XExt2PaePortAuthAdminStatus_Type.__name__ = "TruthValue"
_H3c8021XExt2PaePortAuthAdminStatus_Object = MibTableColumn
h3c8021XExt2PaePortAuthAdminStatus = _H3c8021XExt2PaePortAuthAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 153, 1, 2, 1, 1, 1),
    _H3c8021XExt2PaePortAuthAdminStatus_Type()
)
h3c8021XExt2PaePortAuthAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3c8021XExt2PaePortAuthAdminStatus.setStatus("current")


class _H3c8021XExt2PaePortControlledType_Type(Integer32):
    """Custom type h3c8021XExt2PaePortControlledType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("portbased", 1),
          ("macbased", 2))
    )


_H3c8021XExt2PaePortControlledType_Type.__name__ = "Integer32"
_H3c8021XExt2PaePortControlledType_Object = MibTableColumn
h3c8021XExt2PaePortControlledType = _H3c8021XExt2PaePortControlledType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 153, 1, 2, 1, 1, 2),
    _H3c8021XExt2PaePortControlledType_Type()
)
h3c8021XExt2PaePortControlledType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3c8021XExt2PaePortControlledType.setStatus("current")


class _H3c8021XExt2PaePortMaxUserNum_Type(Unsigned32):
    """Custom type h3c8021XExt2PaePortMaxUserNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_H3c8021XExt2PaePortMaxUserNum_Type.__name__ = "Unsigned32"
_H3c8021XExt2PaePortMaxUserNum_Object = MibTableColumn
h3c8021XExt2PaePortMaxUserNum = _H3c8021XExt2PaePortMaxUserNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 153, 1, 2, 1, 1, 3),
    _H3c8021XExt2PaePortMaxUserNum_Type()
)
h3c8021XExt2PaePortMaxUserNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3c8021XExt2PaePortMaxUserNum.setStatus("current")
_H3c8021XExt2PaePortUserNumNow_Type = Unsigned32
_H3c8021XExt2PaePortUserNumNow_Object = MibTableColumn
h3c8021XExt2PaePortUserNumNow = _H3c8021XExt2PaePortUserNumNow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 153, 1, 2, 1, 1, 4),
    _H3c8021XExt2PaePortUserNumNow_Type()
)
h3c8021XExt2PaePortUserNumNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3c8021XExt2PaePortUserNumNow.setStatus("current")


class _H3c8021XExt2PaePortClearStatistics_Type(Integer32):
    """Custom type h3c8021XExt2PaePortClearStatistics based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noClear", 0),
          ("clear", 1))
    )


_H3c8021XExt2PaePortClearStatistics_Type.__name__ = "Integer32"
_H3c8021XExt2PaePortClearStatistics_Object = MibTableColumn
h3c8021XExt2PaePortClearStatistics = _H3c8021XExt2PaePortClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 153, 1, 2, 1, 1, 5),
    _H3c8021XExt2PaePortClearStatistics_Type()
)
h3c8021XExt2PaePortClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3c8021XExt2PaePortClearStatistics.setStatus("current")


class _H3c8021XExt2PaePortMcastTrigStatus_Type(TruthValue):
    """Custom type h3c8021XExt2PaePortMcastTrigStatus based on TruthValue"""
    defaultValue = 1


_H3c8021XExt2PaePortMcastTrigStatus_Type.__name__ = "TruthValue"
_H3c8021XExt2PaePortMcastTrigStatus_Object = MibTableColumn
h3c8021XExt2PaePortMcastTrigStatus = _H3c8021XExt2PaePortMcastTrigStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 153, 1, 2, 1, 1, 6),
    _H3c8021XExt2PaePortMcastTrigStatus_Type()
)
h3c8021XExt2PaePortMcastTrigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3c8021XExt2PaePortMcastTrigStatus.setStatus("current")


class _H3c8021XExt2PaePortHandshakeStatus_Type(TruthValue):
    """Custom type h3c8021XExt2PaePortHandshakeStatus based on TruthValue"""
    defaultValue = 1


_H3c8021XExt2PaePortHandshakeStatus_Type.__name__ = "TruthValue"
_H3c8021XExt2PaePortHandshakeStatus_Object = MibTableColumn
h3c8021XExt2PaePortHandshakeStatus = _H3c8021XExt2PaePortHandshakeStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 153, 1, 2, 1, 1, 7),
    _H3c8021XExt2PaePortHandshakeStatus_Type()
)
h3c8021XExt2PaePortHandshakeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3c8021XExt2PaePortHandshakeStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-8021X-EXT2-MIB",
    **{"h3c8021XExt2": h3c8021XExt2,
       "h3c8021XExt2MibObjects": h3c8021XExt2MibObjects,
       "h3c8021XExt2System": h3c8021XExt2System,
       "h3c8021XExt2AuthQuietPeriod": h3c8021XExt2AuthQuietPeriod,
       "h3c8021XExt2AuthTxPeriod": h3c8021XExt2AuthTxPeriod,
       "h3c8021XExt2AuthSuppTimeout": h3c8021XExt2AuthSuppTimeout,
       "h3c8021XExt2AuthServerTimeout": h3c8021XExt2AuthServerTimeout,
       "h3c8021XExt2AuthMaxReq": h3c8021XExt2AuthMaxReq,
       "h3c8021XExt2AuthReAuthPeriod": h3c8021XExt2AuthReAuthPeriod,
       "h3c8021XExt2AuthMethod": h3c8021XExt2AuthMethod,
       "h3c8021XExt2Authenticator": h3c8021XExt2Authenticator,
       "h3c8021XExt2AuthConfigExtTable": h3c8021XExt2AuthConfigExtTable,
       "h3c8021XExt2AuthConfigExtEntry": h3c8021XExt2AuthConfigExtEntry,
       "h3c8021XExt2PaePortAuthAdminStatus": h3c8021XExt2PaePortAuthAdminStatus,
       "h3c8021XExt2PaePortControlledType": h3c8021XExt2PaePortControlledType,
       "h3c8021XExt2PaePortMaxUserNum": h3c8021XExt2PaePortMaxUserNum,
       "h3c8021XExt2PaePortUserNumNow": h3c8021XExt2PaePortUserNumNow,
       "h3c8021XExt2PaePortClearStatistics": h3c8021XExt2PaePortClearStatistics,
       "h3c8021XExt2PaePortMcastTrigStatus": h3c8021XExt2PaePortMcastTrigStatus,
       "h3c8021XExt2PaePortHandshakeStatus": h3c8021XExt2PaePortHandshakeStatus}
)
