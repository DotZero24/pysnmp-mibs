# SNMP MIB module (NSCRTV-HFCEMS-OPTICALSWITCH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nscrtv/NSCRTV-HFCEMS-OPTICALSWITCH-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:21:35 2025
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

(commonNELogicalID,
 commonPhysAddress) = mibBuilder.importSymbols(
    "NSCRTV-HFCEMS-COMMON-MIB",
    "commonNELogicalID",
    "commonPhysAddress")

(nscrtvHFCemsTree,) = mibBuilder.importSymbols(
    "NSCRTV-ROOT",
    "nscrtvHFCemsTree")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OsIdent_ObjectIdentity = ObjectIdentity
osIdent = _OsIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 1, 8686)
)
_OsVendorOID_Type = ObjectIdentifier
_OsVendorOID_Object = MibScalar
osVendorOID = _OsVendorOID_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 8686, 1),
    _OsVendorOID_Type()
)
osVendorOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osVendorOID.setStatus("optional")


class _OsWavelength_Type(Integer32):
    """Custom type osWavelength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("1310nm", 1),
          ("1490nm", 2),
          ("1550nm", 3))
    )


_OsWavelength_Type.__name__ = "Integer32"
_OsWavelength_Object = MibScalar
osWavelength = _OsWavelength_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 8686, 2),
    _OsWavelength_Type()
)
osWavelength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osWavelength.setStatus("mandatory")


class _OsAutoControl_Type(Integer32):
    """Custom type osAutoControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_OsAutoControl_Type.__name__ = "Integer32"
_OsAutoControl_Object = MibScalar
osAutoControl = _OsAutoControl_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 8686, 3),
    _OsAutoControl_Type()
)
osAutoControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osAutoControl.setStatus("mandatory")


class _OsCurrentWorkChannel_Type(Integer32):
    """Custom type osCurrentWorkChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("A", 1),
          ("B", 2))
    )


_OsCurrentWorkChannel_Type.__name__ = "Integer32"
_OsCurrentWorkChannel_Object = MibScalar
osCurrentWorkChannel = _OsCurrentWorkChannel_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 8686, 4),
    _OsCurrentWorkChannel_Type()
)
osCurrentWorkChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osCurrentWorkChannel.setStatus("mandatory")


class _OsSwitchReference_Type(Integer32):
    """Custom type osSwitchReference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200, 300),
    )


_OsSwitchReference_Type.__name__ = "Integer32"
_OsSwitchReference_Object = MibScalar
osSwitchReference = _OsSwitchReference_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 8686, 5),
    _OsSwitchReference_Type()
)
osSwitchReference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osSwitchReference.setStatus("mandatory")


class _OsInputOpticalPowerA_Type(Integer32):
    """Custom type osInputOpticalPowerA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_OsInputOpticalPowerA_Type.__name__ = "Integer32"
_OsInputOpticalPowerA_Object = MibScalar
osInputOpticalPowerA = _OsInputOpticalPowerA_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 8686, 6),
    _OsInputOpticalPowerA_Type()
)
osInputOpticalPowerA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osInputOpticalPowerA.setStatus("mandatory")


class _OsInputOpticalPowerB_Type(Integer32):
    """Custom type osInputOpticalPowerB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_OsInputOpticalPowerB_Type.__name__ = "Integer32"
_OsInputOpticalPowerB_Object = MibScalar
osInputOpticalPowerB = _OsInputOpticalPowerB_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 8686, 7),
    _OsInputOpticalPowerB_Type()
)
osInputOpticalPowerB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osInputOpticalPowerB.setStatus("mandatory")

# Managed Objects groups


# Notification objects

osSwitchEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 17409, 1, 0, 8686)
)
osSwitchEvent.setObjects(
      *(("NSCRTV-HFCEMS-COMMON-MIB", "commonPhysAddress"),
        ("NSCRTV-HFCEMS-COMMON-MIB", "commonNELogicalID"),
        ("NSCRTV-HFCEMS-OPTICALSWITCH-MIB", "osCurrentWorkChannel"))
)
if mibBuilder.loadTexts:
    osSwitchEvent.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NSCRTV-HFCEMS-OPTICALSWITCH-MIB",
    **{"osSwitchEvent": osSwitchEvent,
       "osIdent": osIdent,
       "osVendorOID": osVendorOID,
       "osWavelength": osWavelength,
       "osAutoControl": osAutoControl,
       "osCurrentWorkChannel": osCurrentWorkChannel,
       "osSwitchReference": osSwitchReference,
       "osInputOpticalPowerA": osInputOpticalPowerA,
       "osInputOpticalPowerB": osInputOpticalPowerB}
)
