# SNMP MIB module (ADTRAN-GENESCU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GENESCU-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:30:17 2025
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

(adGenSlotInfoIndex,) = mibBuilder.importSymbols(
    "ADTRAN-GENSLOT-MIB",
    "adGenSlotInfoIndex")

(adShared,) = mibBuilder.importSymbols(
    "ADTRAN-MIB",
    "adShared")

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

adGenESCUmg = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 17)
)
if mibBuilder.loadTexts:
    adGenESCUmg.setRevisions(
        ("2010-02-24 13:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenESCUConfig_ObjectIdentity = ObjectIdentity
adGenESCUConfig = _AdGenESCUConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 17, 1)
)
_AdGenESCUProv_ObjectIdentity = ObjectIdentity
adGenESCUProv = _AdGenESCUProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 17, 2)
)
_AdGenESCUProvTable_Object = MibTable
adGenESCUProvTable = _AdGenESCUProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 17, 2, 1)
)
if mibBuilder.loadTexts:
    adGenESCUProvTable.setStatus("current")
_AdGenESCUProvEntry_Object = MibTableRow
adGenESCUProvEntry = _AdGenESCUProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 17, 2, 1, 1)
)
adGenESCUProvEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenESCUProvEntry.setStatus("current")


class _AdGenESCUadminPortRate_Type(Integer32):
    """Custom type adGenESCUadminPortRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("baud9600", 1),
          ("baud19200", 2),
          ("baud38400", 3),
          ("baud57600", 4),
          ("baud115200", 5))
    )


_AdGenESCUadminPortRate_Type.__name__ = "Integer32"
_AdGenESCUadminPortRate_Object = MibTableColumn
adGenESCUadminPortRate = _AdGenESCUadminPortRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 17, 2, 1, 1, 1),
    _AdGenESCUadminPortRate_Type()
)
adGenESCUadminPortRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenESCUadminPortRate.setStatus("current")


class _AdGenESCUautoLogoff_Type(Integer32):
    """Custom type adGenESCUautoLogoff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_AdGenESCUautoLogoff_Type.__name__ = "Integer32"
_AdGenESCUautoLogoff_Object = MibTableColumn
adGenESCUautoLogoff = _AdGenESCUautoLogoff_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 17, 2, 1, 1, 2),
    _AdGenESCUautoLogoff_Type()
)
adGenESCUautoLogoff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenESCUautoLogoff.setStatus("current")


class _AdGenESCUautoLogoffTimer_Type(Integer32):
    """Custom type adGenESCUautoLogoffTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_AdGenESCUautoLogoffTimer_Type.__name__ = "Integer32"
_AdGenESCUautoLogoffTimer_Object = MibTableColumn
adGenESCUautoLogoffTimer = _AdGenESCUautoLogoffTimer_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 17, 2, 1, 1, 3),
    _AdGenESCUautoLogoffTimer_Type()
)
adGenESCUautoLogoffTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenESCUautoLogoffTimer.setStatus("current")


class _AdGenESCUmoduleAutoProv_Type(Integer32):
    """Custom type adGenESCUmoduleAutoProv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_AdGenESCUmoduleAutoProv_Type.__name__ = "Integer32"
_AdGenESCUmoduleAutoProv_Object = MibTableColumn
adGenESCUmoduleAutoProv = _AdGenESCUmoduleAutoProv_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 17, 2, 1, 1, 4),
    _AdGenESCUmoduleAutoProv_Type()
)
adGenESCUmoduleAutoProv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenESCUmoduleAutoProv.setStatus("current")


class _AdGenESCUmuxAutoProv_Type(Integer32):
    """Custom type adGenESCUmuxAutoProv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_AdGenESCUmuxAutoProv_Type.__name__ = "Integer32"
_AdGenESCUmuxAutoProv_Object = MibTableColumn
adGenESCUmuxAutoProv = _AdGenESCUmuxAutoProv_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 17, 2, 1, 1, 5),
    _AdGenESCUmuxAutoProv_Type()
)
adGenESCUmuxAutoProv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenESCUmuxAutoProv.setStatus("current")


class _AdGenESCUrestoreFactoryDefaults_Type(Integer32):
    """Custom type adGenESCUrestoreFactoryDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("restoreFactoryDefaults", 1)
    )


_AdGenESCUrestoreFactoryDefaults_Type.__name__ = "Integer32"
_AdGenESCUrestoreFactoryDefaults_Object = MibTableColumn
adGenESCUrestoreFactoryDefaults = _AdGenESCUrestoreFactoryDefaults_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 17, 2, 1, 1, 6),
    _AdGenESCUrestoreFactoryDefaults_Type()
)
adGenESCUrestoreFactoryDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenESCUrestoreFactoryDefaults.setStatus("current")


class _AdGenESCUadminPortMode_Type(Integer32):
    """Custom type adGenESCUadminPortMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("menus", 1),
          ("tl1", 2))
    )


_AdGenESCUadminPortMode_Type.__name__ = "Integer32"
_AdGenESCUadminPortMode_Object = MibTableColumn
adGenESCUadminPortMode = _AdGenESCUadminPortMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 17, 2, 1, 1, 7),
    _AdGenESCUadminPortMode_Type()
)
adGenESCUadminPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenESCUadminPortMode.setStatus("current")


class _AdGenESCUcraftPortRate_Type(Integer32):
    """Custom type adGenESCUcraftPortRate based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("baud9600", 1),
          ("baud19200", 2),
          ("baud38400", 3),
          ("baud57600", 4),
          ("baud115200", 5))
    )


_AdGenESCUcraftPortRate_Type.__name__ = "Integer32"
_AdGenESCUcraftPortRate_Object = MibTableColumn
adGenESCUcraftPortRate = _AdGenESCUcraftPortRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 17, 2, 1, 1, 8),
    _AdGenESCUcraftPortRate_Type()
)
adGenESCUcraftPortRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenESCUcraftPortRate.setStatus("current")


class _AdGenESCUadminSecurityEnable_Type(Integer32):
    """Custom type adGenESCUadminSecurityEnable based on Integer32"""
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


_AdGenESCUadminSecurityEnable_Type.__name__ = "Integer32"
_AdGenESCUadminSecurityEnable_Object = MibTableColumn
adGenESCUadminSecurityEnable = _AdGenESCUadminSecurityEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 17, 2, 1, 1, 9),
    _AdGenESCUadminSecurityEnable_Type()
)
adGenESCUadminSecurityEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenESCUadminSecurityEnable.setStatus("current")
_AdGenESCUStatus_ObjectIdentity = ObjectIdentity
adGenESCUStatus = _AdGenESCUStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 17, 3)
)
_AdGenESCUStatusTable_Object = MibTable
adGenESCUStatusTable = _AdGenESCUStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 17, 3, 1)
)
if mibBuilder.loadTexts:
    adGenESCUStatusTable.setStatus("current")
_AdGenESCUStatusEntry_Object = MibTableRow
adGenESCUStatusEntry = _AdGenESCUStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 17, 3, 1, 1)
)
adGenESCUStatusEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenESCUStatusEntry.setStatus("current")


class _AdGenESCUacoStatus_Type(Integer32):
    """Custom type adGenESCUacoStatus based on Integer32"""
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


_AdGenESCUacoStatus_Type.__name__ = "Integer32"
_AdGenESCUacoStatus_Object = MibTableColumn
adGenESCUacoStatus = _AdGenESCUacoStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 17, 3, 1, 1, 1),
    _AdGenESCUacoStatus_Type()
)
adGenESCUacoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenESCUacoStatus.setStatus("current")


class _AdGenESCUacoinStatus_Type(Integer32):
    """Custom type adGenESCUacoinStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("active", 2))
    )


_AdGenESCUacoinStatus_Type.__name__ = "Integer32"
_AdGenESCUacoinStatus_Object = MibTableColumn
adGenESCUacoinStatus = _AdGenESCUacoinStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 17, 3, 1, 1, 2),
    _AdGenESCUacoinStatus_Type()
)
adGenESCUacoinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenESCUacoinStatus.setStatus("current")


class _AdGenESCUrmtinStatus_Type(Integer32):
    """Custom type adGenESCUrmtinStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("active", 2))
    )


_AdGenESCUrmtinStatus_Type.__name__ = "Integer32"
_AdGenESCUrmtinStatus_Object = MibTableColumn
adGenESCUrmtinStatus = _AdGenESCUrmtinStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 17, 3, 1, 1, 3),
    _AdGenESCUrmtinStatus_Type()
)
adGenESCUrmtinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenESCUrmtinStatus.setStatus("current")


class _AdGenESCUextin1Status_Type(Integer32):
    """Custom type adGenESCUextin1Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("active", 2))
    )


_AdGenESCUextin1Status_Type.__name__ = "Integer32"
_AdGenESCUextin1Status_Object = MibTableColumn
adGenESCUextin1Status = _AdGenESCUextin1Status_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 17, 3, 1, 1, 4),
    _AdGenESCUextin1Status_Type()
)
adGenESCUextin1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenESCUextin1Status.setStatus("current")


class _AdGenESCUextin2Status_Type(Integer32):
    """Custom type adGenESCUextin2Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("active", 2))
    )


_AdGenESCUextin2Status_Type.__name__ = "Integer32"
_AdGenESCUextin2Status_Object = MibTableColumn
adGenESCUextin2Status = _AdGenESCUextin2Status_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 17, 3, 1, 1, 5),
    _AdGenESCUextin2Status_Type()
)
adGenESCUextin2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenESCUextin2Status.setStatus("current")


class _AdGenESCUminus48PowerAStatus_Type(Integer32):
    """Custom type adGenESCUminus48PowerAStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("active", 2))
    )


_AdGenESCUminus48PowerAStatus_Type.__name__ = "Integer32"
_AdGenESCUminus48PowerAStatus_Object = MibTableColumn
adGenESCUminus48PowerAStatus = _AdGenESCUminus48PowerAStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 17, 3, 1, 1, 6),
    _AdGenESCUminus48PowerAStatus_Type()
)
adGenESCUminus48PowerAStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenESCUminus48PowerAStatus.setStatus("current")


class _AdGenESCUminus48PowerBStatus_Type(Integer32):
    """Custom type adGenESCUminus48PowerBStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("active", 2))
    )


_AdGenESCUminus48PowerBStatus_Type.__name__ = "Integer32"
_AdGenESCUminus48PowerBStatus_Object = MibTableColumn
adGenESCUminus48PowerBStatus = _AdGenESCUminus48PowerBStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 17, 3, 1, 1, 7),
    _AdGenESCUminus48PowerBStatus_Type()
)
adGenESCUminus48PowerBStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenESCUminus48PowerBStatus.setStatus("current")


class _AdGenESCUopenFuseStatus_Type(Integer32):
    """Custom type adGenESCUopenFuseStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("open", 2))
    )


_AdGenESCUopenFuseStatus_Type.__name__ = "Integer32"
_AdGenESCUopenFuseStatus_Object = MibTableColumn
adGenESCUopenFuseStatus = _AdGenESCUopenFuseStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 17, 3, 1, 1, 8),
    _AdGenESCUopenFuseStatus_Type()
)
adGenESCUopenFuseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenESCUopenFuseStatus.setStatus("current")


class _AdGenESCUCLLI_Type(DisplayString):
    """Custom type adGenESCUCLLI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AdGenESCUCLLI_Type.__name__ = "DisplayString"
_AdGenESCUCLLI_Object = MibTableColumn
adGenESCUCLLI = _AdGenESCUCLLI_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 17, 3, 1, 1, 9),
    _AdGenESCUCLLI_Type()
)
adGenESCUCLLI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenESCUCLLI.setStatus("current")


class _AdGenESCUTIRKSID_Type(Integer32):
    """Custom type adGenESCUTIRKSID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_AdGenESCUTIRKSID_Type.__name__ = "Integer32"
_AdGenESCUTIRKSID_Object = MibTableColumn
adGenESCUTIRKSID = _AdGenESCUTIRKSID_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 17, 3, 1, 1, 10),
    _AdGenESCUTIRKSID_Type()
)
adGenESCUTIRKSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenESCUTIRKSID.setStatus("current")
_AdGenESCUTest_ObjectIdentity = ObjectIdentity
adGenESCUTest = _AdGenESCUTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 17, 4)
)
_AdGenESCUTestTable_Object = MibTable
adGenESCUTestTable = _AdGenESCUTestTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 17, 4, 1)
)
if mibBuilder.loadTexts:
    adGenESCUTestTable.setStatus("current")
_AdGenESCUTestEntry_Object = MibTableRow
adGenESCUTestEntry = _AdGenESCUTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 17, 4, 1, 1)
)
adGenESCUTestEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenESCUTestEntry.setStatus("current")


class _AdGenESCUReset_Type(Integer32):
    """Custom type adGenESCUReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_AdGenESCUReset_Type.__name__ = "Integer32"
_AdGenESCUReset_Object = MibTableColumn
adGenESCUReset = _AdGenESCUReset_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 17, 4, 1, 1, 1),
    _AdGenESCUReset_Type()
)
adGenESCUReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenESCUReset.setStatus("current")
_AdGenESCUselfTestResults_Type = DisplayString
_AdGenESCUselfTestResults_Object = MibTableColumn
adGenESCUselfTestResults = _AdGenESCUselfTestResults_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 17, 4, 1, 1, 2),
    _AdGenESCUselfTestResults_Type()
)
adGenESCUselfTestResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenESCUselfTestResults.setStatus("current")


class _AdGenESCUChassisLampTest_Type(Integer32):
    """Custom type adGenESCUChassisLampTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("initiate", 1)
    )


_AdGenESCUChassisLampTest_Type.__name__ = "Integer32"
_AdGenESCUChassisLampTest_Object = MibTableColumn
adGenESCUChassisLampTest = _AdGenESCUChassisLampTest_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 17, 4, 1, 1, 3),
    _AdGenESCUChassisLampTest_Type()
)
adGenESCUChassisLampTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenESCUChassisLampTest.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GENESCU-MIB",
    **{"adGenESCUmg": adGenESCUmg,
       "adGenESCUConfig": adGenESCUConfig,
       "adGenESCUProv": adGenESCUProv,
       "adGenESCUProvTable": adGenESCUProvTable,
       "adGenESCUProvEntry": adGenESCUProvEntry,
       "adGenESCUadminPortRate": adGenESCUadminPortRate,
       "adGenESCUautoLogoff": adGenESCUautoLogoff,
       "adGenESCUautoLogoffTimer": adGenESCUautoLogoffTimer,
       "adGenESCUmoduleAutoProv": adGenESCUmoduleAutoProv,
       "adGenESCUmuxAutoProv": adGenESCUmuxAutoProv,
       "adGenESCUrestoreFactoryDefaults": adGenESCUrestoreFactoryDefaults,
       "adGenESCUadminPortMode": adGenESCUadminPortMode,
       "adGenESCUcraftPortRate": adGenESCUcraftPortRate,
       "adGenESCUadminSecurityEnable": adGenESCUadminSecurityEnable,
       "adGenESCUStatus": adGenESCUStatus,
       "adGenESCUStatusTable": adGenESCUStatusTable,
       "adGenESCUStatusEntry": adGenESCUStatusEntry,
       "adGenESCUacoStatus": adGenESCUacoStatus,
       "adGenESCUacoinStatus": adGenESCUacoinStatus,
       "adGenESCUrmtinStatus": adGenESCUrmtinStatus,
       "adGenESCUextin1Status": adGenESCUextin1Status,
       "adGenESCUextin2Status": adGenESCUextin2Status,
       "adGenESCUminus48PowerAStatus": adGenESCUminus48PowerAStatus,
       "adGenESCUminus48PowerBStatus": adGenESCUminus48PowerBStatus,
       "adGenESCUopenFuseStatus": adGenESCUopenFuseStatus,
       "adGenESCUCLLI": adGenESCUCLLI,
       "adGenESCUTIRKSID": adGenESCUTIRKSID,
       "adGenESCUTest": adGenESCUTest,
       "adGenESCUTestTable": adGenESCUTestTable,
       "adGenESCUTestEntry": adGenESCUTestEntry,
       "adGenESCUReset": adGenESCUReset,
       "adGenESCUselfTestResults": adGenESCUselfTestResults,
       "adGenESCUChassisLampTest": adGenESCUChassisLampTest}
)
