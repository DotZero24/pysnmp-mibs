# SNMP MIB module (EOAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/EOAM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:44:33 2025
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

fseoam = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 121)
)
if mibBuilder.loadTexts:
    fseoam.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EoamOui(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3



# MIB Managed Objects in the order of their OIDs

_FsEoamSystem_ObjectIdentity = ObjectIdentity
fsEoamSystem = _FsEoamSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 121, 1)
)


class _FsEoamSystemControl_Type(Integer32):
    """Custom type fsEoamSystemControl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("shutdown", 2))
    )


_FsEoamSystemControl_Type.__name__ = "Integer32"
_FsEoamSystemControl_Object = MibScalar
fsEoamSystemControl = _FsEoamSystemControl_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 121, 1, 1),
    _FsEoamSystemControl_Type()
)
fsEoamSystemControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEoamSystemControl.setStatus("current")


class _FsEoamModuleStatus_Type(Integer32):
    """Custom type fsEoamModuleStatus based on Integer32"""
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


_FsEoamModuleStatus_Type.__name__ = "Integer32"
_FsEoamModuleStatus_Object = MibScalar
fsEoamModuleStatus = _FsEoamModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 121, 1, 2),
    _FsEoamModuleStatus_Type()
)
fsEoamModuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEoamModuleStatus.setStatus("current")


class _FsEoamErrorEventResend_Type(Unsigned32):
    """Custom type fsEoamErrorEventResend based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FsEoamErrorEventResend_Type.__name__ = "Unsigned32"
_FsEoamErrorEventResend_Object = MibScalar
fsEoamErrorEventResend = _FsEoamErrorEventResend_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 121, 1, 3),
    _FsEoamErrorEventResend_Type()
)
fsEoamErrorEventResend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEoamErrorEventResend.setStatus("current")
_FsEoamOui_Type = EoamOui
_FsEoamOui_Object = MibScalar
fsEoamOui = _FsEoamOui_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 121, 1, 4),
    _FsEoamOui_Type()
)
fsEoamOui.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEoamOui.setStatus("current")


class _FsEoamTraceOption_Type(Integer32):
    """Custom type fsEoamTraceOption based on Integer32"""
    defaultValue = 262144


_FsEoamTraceOption_Type.__name__ = "Integer32"
_FsEoamTraceOption_Object = MibScalar
fsEoamTraceOption = _FsEoamTraceOption_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 121, 1, 5),
    _FsEoamTraceOption_Type()
)
fsEoamTraceOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEoamTraceOption.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EOAM-MIB",
    **{"EoamOui": EoamOui,
       "fseoam": fseoam,
       "fsEoamSystem": fsEoamSystem,
       "fsEoamSystemControl": fsEoamSystemControl,
       "fsEoamModuleStatus": fsEoamModuleStatus,
       "fsEoamErrorEventResend": fsEoamErrorEventResend,
       "fsEoamOui": fsEoamOui,
       "fsEoamTraceOption": fsEoamTraceOption}
)
