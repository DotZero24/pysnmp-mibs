# SNMP MIB module (WV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/tycon/WV-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:07:49 2025
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

webvoltmeter = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3)
)


# Types definitions



class ON_OFF(Integer32):
    """Custom type ON_OFF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("OFF", 0),
          ("ON", 1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Tycon_ObjectIdentity = ObjectIdentity
tycon = _Tycon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095)
)
_Product_ObjectIdentity = ObjectIdentity
product = _Product_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 1)
)
_Name_Type = DisplayString
_Name_Object = MibScalar
name = _Name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 1, 1),
    _Name_Type()
)
name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    name.setStatus("current")
_Version_Type = DisplayString
_Version_Object = MibScalar
version = _Version_Object(
    (1, 3, 6, 1, 4, 1, 17095, 1, 2),
    _Version_Type()
)
version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    version.setStatus("current")
_Builddate_Type = DisplayString
_Builddate_Object = MibScalar
builddate = _Builddate_Object(
    (1, 3, 6, 1, 4, 1, 17095, 1, 3),
    _Builddate_Type()
)
builddate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    builddate.setStatus("current")
_Control_ObjectIdentity = ObjectIdentity
control = _Control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 3)
)


class _Relay1_Type(Integer32):
    """Custom type relay1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("OFF", 0),
          ("ON", 1))
    )


_Relay1_Type.__name__ = "Integer32"
_Relay1_Object = MibScalar
relay1 = _Relay1_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 1),
    _Relay1_Type()
)
relay1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay1.setStatus("current")


class _Relay2_Type(Integer32):
    """Custom type relay2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("OFF", 0),
          ("ON", 1))
    )


_Relay2_Type.__name__ = "Integer32"
_Relay2_Object = MibScalar
relay2 = _Relay2_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 2),
    _Relay2_Type()
)
relay2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay2.setStatus("current")


class _Relay3_Type(Integer32):
    """Custom type relay3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("OFF", 0),
          ("ON", 1))
    )


_Relay3_Type.__name__ = "Integer32"
_Relay3_Object = MibScalar
relay3 = _Relay3_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 3),
    _Relay3_Type()
)
relay3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay3.setStatus("current")


class _Relay4_Type(Integer32):
    """Custom type relay4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("OFF", 0),
          ("ON", 1))
    )


_Relay4_Type.__name__ = "Integer32"
_Relay4_Object = MibScalar
relay4 = _Relay4_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 4),
    _Relay4_Type()
)
relay4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay4.setStatus("current")


class _Volt1_Type(DisplayString):
    """Custom type volt1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_Volt1_Type.__name__ = "DisplayString"
_Volt1_Object = MibScalar
volt1 = _Volt1_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 5),
    _Volt1_Type()
)
volt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volt1.setStatus("current")


class _Volt2_Type(DisplayString):
    """Custom type volt2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_Volt2_Type.__name__ = "DisplayString"
_Volt2_Object = MibScalar
volt2 = _Volt2_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 6),
    _Volt2_Type()
)
volt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volt2.setStatus("current")


class _Volt3_Type(DisplayString):
    """Custom type volt3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_Volt3_Type.__name__ = "DisplayString"
_Volt3_Object = MibScalar
volt3 = _Volt3_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 7),
    _Volt3_Type()
)
volt3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volt3.setStatus("current")


class _Volt4_Type(DisplayString):
    """Custom type volt4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_Volt4_Type.__name__ = "DisplayString"
_Volt4_Object = MibScalar
volt4 = _Volt4_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 8),
    _Volt4_Type()
)
volt4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volt4.setStatus("current")


class _Amp1_Type(DisplayString):
    """Custom type amp1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_Amp1_Type.__name__ = "DisplayString"
_Amp1_Object = MibScalar
amp1 = _Amp1_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 9),
    _Amp1_Type()
)
amp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amp1.setStatus("current")


class _Amp2_Type(DisplayString):
    """Custom type amp2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_Amp2_Type.__name__ = "DisplayString"
_Amp2_Object = MibScalar
amp2 = _Amp2_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 10),
    _Amp2_Type()
)
amp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amp2.setStatus("current")


class _Amp3_Type(DisplayString):
    """Custom type amp3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_Amp3_Type.__name__ = "DisplayString"
_Amp3_Object = MibScalar
amp3 = _Amp3_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 11),
    _Amp3_Type()
)
amp3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amp3.setStatus("current")


class _Amp4_Type(DisplayString):
    """Custom type amp4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_Amp4_Type.__name__ = "DisplayString"
_Amp4_Object = MibScalar
amp4 = _Amp4_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 12),
    _Amp4_Type()
)
amp4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amp4.setStatus("current")


class _Temp1_Type(DisplayString):
    """Custom type temp1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_Temp1_Type.__name__ = "DisplayString"
_Temp1_Object = MibScalar
temp1 = _Temp1_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 13),
    _Temp1_Type()
)
temp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temp1.setStatus("current")


class _Temp2_Type(DisplayString):
    """Custom type temp2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_Temp2_Type.__name__ = "DisplayString"
_Temp2_Object = MibScalar
temp2 = _Temp2_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 14),
    _Temp2_Type()
)
temp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temp2.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WV-MIB",
    **{"ON-OFF": ON_OFF,
       "webvoltmeter": webvoltmeter,
       "tycon": tycon,
       "product": product,
       "name": name,
       "version": version,
       "builddate": builddate,
       "control": control,
       "relay1": relay1,
       "relay2": relay2,
       "relay3": relay3,
       "relay4": relay4,
       "volt1": volt1,
       "volt2": volt2,
       "volt3": volt3,
       "volt4": volt4,
       "amp1": amp1,
       "amp2": amp2,
       "amp3": amp3,
       "amp4": amp4,
       "temp1": temp1,
       "temp2": temp2}
)
