# SNMP MIB module (TPDIN2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/tycon/TPDIN2-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:07:50 2025
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

tpdin2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45621, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Tenths(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-1"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )



# MIB Managed Objects in the order of their OIDs

_Tycon_ObjectIdentity = ObjectIdentity
tycon = _Tycon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45621)
)
_Product_ObjectIdentity = ObjectIdentity
product = _Product_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45621, 2, 1)
)
_Name_Type = DisplayString
_Name_Object = MibScalar
name = _Name_Object(
    (1, 3, 6, 1, 4, 1, 45621, 2, 1, 1),
    _Name_Type()
)
name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    name.setStatus("current")
_Version_Type = DisplayString
_Version_Object = MibScalar
version = _Version_Object(
    (1, 3, 6, 1, 4, 1, 45621, 2, 1, 2),
    _Version_Type()
)
version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    version.setStatus("current")
_Builddate_Type = DisplayString
_Builddate_Object = MibScalar
builddate = _Builddate_Object(
    (1, 3, 6, 1, 4, 1, 45621, 2, 1, 3),
    _Builddate_Type()
)
builddate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    builddate.setStatus("current")
_Monitor_ObjectIdentity = ObjectIdentity
monitor = _Monitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45621, 2, 2)
)
_Relay1_Type = Integer32
_Relay1_Object = MibScalar
relay1 = _Relay1_Object(
    (1, 3, 6, 1, 4, 1, 45621, 2, 2, 1),
    _Relay1_Type()
)
relay1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay1.setStatus("current")
_Relay2_Type = Integer32
_Relay2_Object = MibScalar
relay2 = _Relay2_Object(
    (1, 3, 6, 1, 4, 1, 45621, 2, 2, 2),
    _Relay2_Type()
)
relay2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay2.setStatus("current")
_Relay3_Type = Integer32
_Relay3_Object = MibScalar
relay3 = _Relay3_Object(
    (1, 3, 6, 1, 4, 1, 45621, 2, 2, 3),
    _Relay3_Type()
)
relay3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay3.setStatus("current")
_Relay4_Type = Integer32
_Relay4_Object = MibScalar
relay4 = _Relay4_Object(
    (1, 3, 6, 1, 4, 1, 45621, 2, 2, 4),
    _Relay4_Type()
)
relay4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay4.setStatus("current")
_Voltage1_Type = Tenths
_Voltage1_Object = MibScalar
voltage1 = _Voltage1_Object(
    (1, 3, 6, 1, 4, 1, 45621, 2, 2, 5),
    _Voltage1_Type()
)
voltage1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltage1.setStatus("current")
_Voltage2_Type = Tenths
_Voltage2_Object = MibScalar
voltage2 = _Voltage2_Object(
    (1, 3, 6, 1, 4, 1, 45621, 2, 2, 6),
    _Voltage2_Type()
)
voltage2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltage2.setStatus("current")
_Voltage3_Type = Tenths
_Voltage3_Object = MibScalar
voltage3 = _Voltage3_Object(
    (1, 3, 6, 1, 4, 1, 45621, 2, 2, 7),
    _Voltage3_Type()
)
voltage3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltage3.setStatus("current")
_Voltage4_Type = Tenths
_Voltage4_Object = MibScalar
voltage4 = _Voltage4_Object(
    (1, 3, 6, 1, 4, 1, 45621, 2, 2, 8),
    _Voltage4_Type()
)
voltage4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltage4.setStatus("current")
_Current1_Type = Tenths
_Current1_Object = MibScalar
current1 = _Current1_Object(
    (1, 3, 6, 1, 4, 1, 45621, 2, 2, 9),
    _Current1_Type()
)
current1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    current1.setStatus("current")
_Current2_Type = Tenths
_Current2_Object = MibScalar
current2 = _Current2_Object(
    (1, 3, 6, 1, 4, 1, 45621, 2, 2, 10),
    _Current2_Type()
)
current2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    current2.setStatus("current")
_Current3_Type = Tenths
_Current3_Object = MibScalar
current3 = _Current3_Object(
    (1, 3, 6, 1, 4, 1, 45621, 2, 2, 11),
    _Current3_Type()
)
current3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    current3.setStatus("current")
_Current4_Type = Tenths
_Current4_Object = MibScalar
current4 = _Current4_Object(
    (1, 3, 6, 1, 4, 1, 45621, 2, 2, 12),
    _Current4_Type()
)
current4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    current4.setStatus("current")
_Temperature1_Type = Tenths
_Temperature1_Object = MibScalar
temperature1 = _Temperature1_Object(
    (1, 3, 6, 1, 4, 1, 45621, 2, 2, 13),
    _Temperature1_Type()
)
temperature1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature1.setStatus("current")
_Temperature2_Type = Tenths
_Temperature2_Object = MibScalar
temperature2 = _Temperature2_Object(
    (1, 3, 6, 1, 4, 1, 45621, 2, 2, 14),
    _Temperature2_Type()
)
temperature2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature2.setStatus("current")


class _Voltage1String_Type(DisplayString):
    """Custom type voltage1String based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_Voltage1String_Type.__name__ = "DisplayString"
_Voltage1String_Object = MibScalar
voltage1String = _Voltage1String_Object(
    (1, 3, 6, 1, 4, 1, 45621, 2, 2, 15),
    _Voltage1String_Type()
)
voltage1String.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltage1String.setStatus("current")


class _Voltage2String_Type(DisplayString):
    """Custom type voltage2String based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_Voltage2String_Type.__name__ = "DisplayString"
_Voltage2String_Object = MibScalar
voltage2String = _Voltage2String_Object(
    (1, 3, 6, 1, 4, 1, 45621, 2, 2, 16),
    _Voltage2String_Type()
)
voltage2String.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltage2String.setStatus("current")


class _Voltage3String_Type(DisplayString):
    """Custom type voltage3String based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_Voltage3String_Type.__name__ = "DisplayString"
_Voltage3String_Object = MibScalar
voltage3String = _Voltage3String_Object(
    (1, 3, 6, 1, 4, 1, 45621, 2, 2, 17),
    _Voltage3String_Type()
)
voltage3String.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltage3String.setStatus("current")


class _Voltage4String_Type(DisplayString):
    """Custom type voltage4String based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_Voltage4String_Type.__name__ = "DisplayString"
_Voltage4String_Object = MibScalar
voltage4String = _Voltage4String_Object(
    (1, 3, 6, 1, 4, 1, 45621, 2, 2, 18),
    _Voltage4String_Type()
)
voltage4String.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltage4String.setStatus("current")


class _Current1String_Type(DisplayString):
    """Custom type current1String based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_Current1String_Type.__name__ = "DisplayString"
_Current1String_Object = MibScalar
current1String = _Current1String_Object(
    (1, 3, 6, 1, 4, 1, 45621, 2, 2, 19),
    _Current1String_Type()
)
current1String.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    current1String.setStatus("current")


class _Current2String_Type(DisplayString):
    """Custom type current2String based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_Current2String_Type.__name__ = "DisplayString"
_Current2String_Object = MibScalar
current2String = _Current2String_Object(
    (1, 3, 6, 1, 4, 1, 45621, 2, 2, 20),
    _Current2String_Type()
)
current2String.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    current2String.setStatus("current")


class _Current3String_Type(DisplayString):
    """Custom type current3String based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_Current3String_Type.__name__ = "DisplayString"
_Current3String_Object = MibScalar
current3String = _Current3String_Object(
    (1, 3, 6, 1, 4, 1, 45621, 2, 2, 21),
    _Current3String_Type()
)
current3String.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    current3String.setStatus("current")


class _Current4String_Type(DisplayString):
    """Custom type current4String based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_Current4String_Type.__name__ = "DisplayString"
_Current4String_Object = MibScalar
current4String = _Current4String_Object(
    (1, 3, 6, 1, 4, 1, 45621, 2, 2, 22),
    _Current4String_Type()
)
current4String.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    current4String.setStatus("current")


class _Temp1String_Type(DisplayString):
    """Custom type temp1String based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_Temp1String_Type.__name__ = "DisplayString"
_Temp1String_Object = MibScalar
temp1String = _Temp1String_Object(
    (1, 3, 6, 1, 4, 1, 45621, 2, 2, 23),
    _Temp1String_Type()
)
temp1String.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temp1String.setStatus("current")


class _Temp2String_Type(DisplayString):
    """Custom type temp2String based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_Temp2String_Type.__name__ = "DisplayString"
_Temp2String_Object = MibScalar
temp2String = _Temp2String_Object(
    (1, 3, 6, 1, 4, 1, 45621, 2, 2, 24),
    _Temp2String_Type()
)
temp2String.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temp2String.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPDIN2-MIB",
    **{"Tenths": Tenths,
       "tycon": tycon,
       "tpdin2": tpdin2,
       "product": product,
       "name": name,
       "version": version,
       "builddate": builddate,
       "monitor": monitor,
       "relay1": relay1,
       "relay2": relay2,
       "relay3": relay3,
       "relay4": relay4,
       "voltage1": voltage1,
       "voltage2": voltage2,
       "voltage3": voltage3,
       "voltage4": voltage4,
       "current1": current1,
       "current2": current2,
       "current3": current3,
       "current4": current4,
       "temperature1": temperature1,
       "temperature2": temperature2,
       "voltage1String": voltage1String,
       "voltage2String": voltage2String,
       "voltage3String": voltage3String,
       "voltage4String": voltage4String,
       "current1String": current1String,
       "current2String": current2String,
       "current3String": current3String,
       "current4String": current4String,
       "temp1String": temp1String,
       "temp2String": temp2String}
)
