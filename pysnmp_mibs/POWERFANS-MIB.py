# SNMP MIB module (POWERFANS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/POWERFANS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:45:23 2025
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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso,
 mgmt) = mibBuilder.importSymbols(
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso",
    "mgmt")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class FanStatus(Integer32):
    """Custom type FanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fan-online", 0),
          ("fan-offline", 1))
    )





class PowerStatus(Integer32):
    """Custom type PowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("power-work", 0),
          ("power-online", 1),
          ("power-offline", 2))
    )





class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Zte_ObjectIdentity = ObjectIdentity
zte = _Zte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902)
)
_Zxr10_ObjectIdentity = ObjectIdentity
zxr10 = _Zxr10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3)
)
_Zxr10systemconfig_ObjectIdentity = ObjectIdentity
zxr10systemconfig = _Zxr10systemconfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 1)
)
_Enviorment_ObjectIdentity = ObjectIdentity
enviorment = _Enviorment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 200)
)
_FanTable_Object = MibTable
fanTable = _FanTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 200, 1)
)
if mibBuilder.loadTexts:
    fanTable.setStatus("current")
_FanEntry_Object = MibTableRow
fanEntry = _FanEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 200, 1, 1)
)
fanEntry.setIndexNames(
    (0, "POWERFANS-MIB", "fanNo"),
)
if mibBuilder.loadTexts:
    fanEntry.setStatus("current")
_FanNo_Type = Integer32
_FanNo_Object = MibTableColumn
fanNo = _FanNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 200, 1, 1, 1),
    _FanNo_Type()
)
fanNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanNo.setStatus("current")
_FanStat_Type = FanStatus
_FanStat_Object = MibTableColumn
fanStat = _FanStat_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 200, 1, 1, 2),
    _FanStat_Type()
)
fanStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanStat.setStatus("current")
_FanRotateSpeed_Type = Integer32
_FanRotateSpeed_Object = MibTableColumn
fanRotateSpeed = _FanRotateSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 200, 1, 1, 3),
    _FanRotateSpeed_Type()
)
fanRotateSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanRotateSpeed.setStatus("current")
_PowerTable_Object = MibTable
powerTable = _PowerTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 200, 2)
)
if mibBuilder.loadTexts:
    powerTable.setStatus("current")
_PowerEntry_Object = MibTableRow
powerEntry = _PowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 200, 2, 1)
)
powerEntry.setIndexNames(
    (0, "POWERFANS-MIB", "powerNo"),
)
if mibBuilder.loadTexts:
    powerEntry.setStatus("current")
_PowerNo_Type = Integer32
_PowerNo_Object = MibTableColumn
powerNo = _PowerNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 200, 2, 1, 1),
    _PowerNo_Type()
)
powerNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerNo.setStatus("current")
_PowerStat_Type = PowerStatus
_PowerStat_Object = MibTableColumn
powerStat = _PowerStat_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 200, 2, 1, 2),
    _PowerStat_Type()
)
powerStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerStat.setStatus("current")
_PowerTemperature_Type = Integer32
_PowerTemperature_Object = MibTableColumn
powerTemperature = _PowerTemperature_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 200, 2, 1, 3),
    _PowerTemperature_Type()
)
powerTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerTemperature.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "POWERFANS-MIB",
    **{"FanStatus": FanStatus,
       "PowerStatus": PowerStatus,
       "DisplayString": DisplayString,
       "zte": zte,
       "zxr10": zxr10,
       "zxr10systemconfig": zxr10systemconfig,
       "enviorment": enviorment,
       "fanTable": fanTable,
       "fanEntry": fanEntry,
       "fanNo": fanNo,
       "fanStat": fanStat,
       "fanRotateSpeed": fanRotateSpeed,
       "powerTable": powerTable,
       "powerEntry": powerEntry,
       "powerNo": powerNo,
       "powerStat": powerStat,
       "powerTemperature": powerTemperature}
)
