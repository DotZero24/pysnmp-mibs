# SNMP MIB module (AGFEO-PBX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/agfeo/AGFEO-PBX-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:05:07 2025
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
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

agfeoMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 53023)
)
if mibBuilder.loadTexts:
    agfeoMib.setRevisions(
        ("2020-03-27 00:00",
         "2018-10-25 00:00",
         "2018-10-14 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AgfeoMibObjects_ObjectIdentity = ObjectIdentity
agfeoMibObjects = _AgfeoMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 53023, 1)
)
if mibBuilder.loadTexts:
    agfeoMibObjects.setStatus("current")
_AgfeoCommon_ObjectIdentity = ObjectIdentity
agfeoCommon = _AgfeoCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 53023, 1, 1)
)
if mibBuilder.loadTexts:
    agfeoCommon.setStatus("current")
_AgfeoCommonCfg_ObjectIdentity = ObjectIdentity
agfeoCommonCfg = _AgfeoCommonCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 53023, 1, 1, 1)
)
if mibBuilder.loadTexts:
    agfeoCommonCfg.setStatus("current")
_AgfeoCCfgSip_ObjectIdentity = ObjectIdentity
agfeoCCfgSip = _AgfeoCCfgSip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 53023, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    agfeoCCfgSip.setStatus("current")
_AgfeoCCfgSipAccountTable_Object = MibTable
agfeoCCfgSipAccountTable = _AgfeoCCfgSipAccountTable_Object(
    (1, 3, 6, 1, 4, 1, 53023, 1, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    agfeoCCfgSipAccountTable.setStatus("current")
_AgfeoCCfgSipAccountEntry_Object = MibTableRow
agfeoCCfgSipAccountEntry = _AgfeoCCfgSipAccountEntry_Object(
    (1, 3, 6, 1, 4, 1, 53023, 1, 1, 1, 1, 1, 1)
)
agfeoCCfgSipAccountEntry.setIndexNames(
    (0, "AGFEO-PBX-MIB", "agfeoCCfgSipAccountIndex"),
)
if mibBuilder.loadTexts:
    agfeoCCfgSipAccountEntry.setStatus("current")


class _AgfeoCCfgSipAccountIndex_Type(Integer32):
    """Custom type agfeoCCfgSipAccountIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_AgfeoCCfgSipAccountIndex_Type.__name__ = "Integer32"
_AgfeoCCfgSipAccountIndex_Object = MibTableColumn
agfeoCCfgSipAccountIndex = _AgfeoCCfgSipAccountIndex_Object(
    (1, 3, 6, 1, 4, 1, 53023, 1, 1, 1, 1, 1, 1, 1),
    _AgfeoCCfgSipAccountIndex_Type()
)
agfeoCCfgSipAccountIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agfeoCCfgSipAccountIndex.setStatus("current")
_AgfeoCCfgSipAccountName_Type = OctetString
_AgfeoCCfgSipAccountName_Object = MibTableColumn
agfeoCCfgSipAccountName = _AgfeoCCfgSipAccountName_Object(
    (1, 3, 6, 1, 4, 1, 53023, 1, 1, 1, 1, 1, 1, 2),
    _AgfeoCCfgSipAccountName_Type()
)
agfeoCCfgSipAccountName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agfeoCCfgSipAccountName.setStatus("current")


class _AgfeoCCfgSipAccountActive_Type(Integer32):
    """Custom type agfeoCCfgSipAccountActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_AgfeoCCfgSipAccountActive_Type.__name__ = "Integer32"
_AgfeoCCfgSipAccountActive_Object = MibTableColumn
agfeoCCfgSipAccountActive = _AgfeoCCfgSipAccountActive_Object(
    (1, 3, 6, 1, 4, 1, 53023, 1, 1, 1, 1, 1, 1, 3),
    _AgfeoCCfgSipAccountActive_Type()
)
agfeoCCfgSipAccountActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agfeoCCfgSipAccountActive.setStatus("current")
_AgfeoCommonStats_ObjectIdentity = ObjectIdentity
agfeoCommonStats = _AgfeoCommonStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 53023, 1, 1, 2)
)
if mibBuilder.loadTexts:
    agfeoCommonStats.setStatus("current")
_AgfeoCStaGeneral_ObjectIdentity = ObjectIdentity
agfeoCStaGeneral = _AgfeoCStaGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 53023, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    agfeoCStaGeneral.setStatus("current")
_AgfeoCStaPbxProduct_Type = OctetString
_AgfeoCStaPbxProduct_Object = MibScalar
agfeoCStaPbxProduct = _AgfeoCStaPbxProduct_Object(
    (1, 3, 6, 1, 4, 1, 53023, 1, 1, 2, 1, 1),
    _AgfeoCStaPbxProduct_Type()
)
agfeoCStaPbxProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agfeoCStaPbxProduct.setStatus("current")
_AgfeoCStaPbxProductId_Type = OctetString
_AgfeoCStaPbxProductId_Object = MibScalar
agfeoCStaPbxProductId = _AgfeoCStaPbxProductId_Object(
    (1, 3, 6, 1, 4, 1, 53023, 1, 1, 2, 1, 2),
    _AgfeoCStaPbxProductId_Type()
)
agfeoCStaPbxProductId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agfeoCStaPbxProductId.setStatus("current")
_AgfeoCStaPbxFirmware_Type = OctetString
_AgfeoCStaPbxFirmware_Object = MibScalar
agfeoCStaPbxFirmware = _AgfeoCStaPbxFirmware_Object(
    (1, 3, 6, 1, 4, 1, 53023, 1, 1, 2, 1, 3),
    _AgfeoCStaPbxFirmware_Type()
)
agfeoCStaPbxFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agfeoCStaPbxFirmware.setStatus("current")
_AgfeoCStaPbxAppUpTime_Type = OctetString
_AgfeoCStaPbxAppUpTime_Object = MibScalar
agfeoCStaPbxAppUpTime = _AgfeoCStaPbxAppUpTime_Object(
    (1, 3, 6, 1, 4, 1, 53023, 1, 1, 2, 1, 4),
    _AgfeoCStaPbxAppUpTime_Type()
)
agfeoCStaPbxAppUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agfeoCStaPbxAppUpTime.setStatus("current")
_AgfeoCStaSip_ObjectIdentity = ObjectIdentity
agfeoCStaSip = _AgfeoCStaSip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 53023, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    agfeoCStaSip.setStatus("current")
_AgfeoCStaSipTest_ObjectIdentity = ObjectIdentity
agfeoCStaSipTest = _AgfeoCStaSipTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 53023, 1, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    agfeoCStaSipTest.setStatus("current")
_AgfeoCStaSipTestInteger_Type = Integer32
_AgfeoCStaSipTestInteger_Object = MibScalar
agfeoCStaSipTestInteger = _AgfeoCStaSipTestInteger_Object(
    (1, 3, 6, 1, 4, 1, 53023, 1, 1, 2, 2, 1, 1),
    _AgfeoCStaSipTestInteger_Type()
)
agfeoCStaSipTestInteger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agfeoCStaSipTestInteger.setStatus("current")
_AgfeoCStaSipAccountTable_Object = MibTable
agfeoCStaSipAccountTable = _AgfeoCStaSipAccountTable_Object(
    (1, 3, 6, 1, 4, 1, 53023, 1, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    agfeoCStaSipAccountTable.setStatus("current")
_AgfeoCStaSipAccountEntry_Object = MibTableRow
agfeoCStaSipAccountEntry = _AgfeoCStaSipAccountEntry_Object(
    (1, 3, 6, 1, 4, 1, 53023, 1, 1, 2, 2, 2, 1)
)
agfeoCStaSipAccountEntry.setIndexNames(
    (0, "AGFEO-PBX-MIB", "agfeoCStaSipAccountIndex"),
)
if mibBuilder.loadTexts:
    agfeoCStaSipAccountEntry.setStatus("current")


class _AgfeoCStaSipAccountIndex_Type(Integer32):
    """Custom type agfeoCStaSipAccountIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_AgfeoCStaSipAccountIndex_Type.__name__ = "Integer32"
_AgfeoCStaSipAccountIndex_Object = MibTableColumn
agfeoCStaSipAccountIndex = _AgfeoCStaSipAccountIndex_Object(
    (1, 3, 6, 1, 4, 1, 53023, 1, 1, 2, 2, 2, 1, 1),
    _AgfeoCStaSipAccountIndex_Type()
)
agfeoCStaSipAccountIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agfeoCStaSipAccountIndex.setStatus("current")


class _AgfeoCStaSipAccountStatus_Type(Integer32):
    """Custom type agfeoCStaSipAccountStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_AgfeoCStaSipAccountStatus_Type.__name__ = "Integer32"
_AgfeoCStaSipAccountStatus_Object = MibTableColumn
agfeoCStaSipAccountStatus = _AgfeoCStaSipAccountStatus_Object(
    (1, 3, 6, 1, 4, 1, 53023, 1, 1, 2, 2, 2, 1, 2),
    _AgfeoCStaSipAccountStatus_Type()
)
agfeoCStaSipAccountStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agfeoCStaSipAccountStatus.setStatus("current")
_AgfeoCStaSipAccountCause_Type = OctetString
_AgfeoCStaSipAccountCause_Object = MibTableColumn
agfeoCStaSipAccountCause = _AgfeoCStaSipAccountCause_Object(
    (1, 3, 6, 1, 4, 1, 53023, 1, 1, 2, 2, 2, 1, 3),
    _AgfeoCStaSipAccountCause_Type()
)
agfeoCStaSipAccountCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agfeoCStaSipAccountCause.setStatus("current")
_AgfeoCStaIpChannel_ObjectIdentity = ObjectIdentity
agfeoCStaIpChannel = _AgfeoCStaIpChannel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 53023, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    agfeoCStaIpChannel.setStatus("current")
_AgfeoCStaIpChannelAvailActual_Type = Integer32
_AgfeoCStaIpChannelAvailActual_Object = MibScalar
agfeoCStaIpChannelAvailActual = _AgfeoCStaIpChannelAvailActual_Object(
    (1, 3, 6, 1, 4, 1, 53023, 1, 1, 2, 3, 1),
    _AgfeoCStaIpChannelAvailActual_Type()
)
agfeoCStaIpChannelAvailActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agfeoCStaIpChannelAvailActual.setStatus("current")
_AgfeoCStaIpChannelAvailMax_Type = Integer32
_AgfeoCStaIpChannelAvailMax_Object = MibScalar
agfeoCStaIpChannelAvailMax = _AgfeoCStaIpChannelAvailMax_Object(
    (1, 3, 6, 1, 4, 1, 53023, 1, 1, 2, 3, 2),
    _AgfeoCStaIpChannelAvailMax_Type()
)
agfeoCStaIpChannelAvailMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agfeoCStaIpChannelAvailMax.setStatus("current")
_AgfeoCStaIpChannelLoadActual_Type = Integer32
_AgfeoCStaIpChannelLoadActual_Object = MibScalar
agfeoCStaIpChannelLoadActual = _AgfeoCStaIpChannelLoadActual_Object(
    (1, 3, 6, 1, 4, 1, 53023, 1, 1, 2, 3, 3),
    _AgfeoCStaIpChannelLoadActual_Type()
)
agfeoCStaIpChannelLoadActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agfeoCStaIpChannelLoadActual.setStatus("current")
_AgfeoCStaIpChannelLoadMax_Type = Integer32
_AgfeoCStaIpChannelLoadMax_Object = MibScalar
agfeoCStaIpChannelLoadMax = _AgfeoCStaIpChannelLoadMax_Object(
    (1, 3, 6, 1, 4, 1, 53023, 1, 1, 2, 3, 4),
    _AgfeoCStaIpChannelLoadMax_Type()
)
agfeoCStaIpChannelLoadMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agfeoCStaIpChannelLoadMax.setStatus("current")
_AgfeoCStaCalls_ObjectIdentity = ObjectIdentity
agfeoCStaCalls = _AgfeoCStaCalls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 53023, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    agfeoCStaCalls.setStatus("current")
_AgfeoCStaCallsAvailActual_Type = Integer32
_AgfeoCStaCallsAvailActual_Object = MibScalar
agfeoCStaCallsAvailActual = _AgfeoCStaCallsAvailActual_Object(
    (1, 3, 6, 1, 4, 1, 53023, 1, 1, 2, 4, 1),
    _AgfeoCStaCallsAvailActual_Type()
)
agfeoCStaCallsAvailActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agfeoCStaCallsAvailActual.setStatus("current")
_AgfeoCStaCallsAvailMax_Type = Integer32
_AgfeoCStaCallsAvailMax_Object = MibScalar
agfeoCStaCallsAvailMax = _AgfeoCStaCallsAvailMax_Object(
    (1, 3, 6, 1, 4, 1, 53023, 1, 1, 2, 4, 2),
    _AgfeoCStaCallsAvailMax_Type()
)
agfeoCStaCallsAvailMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agfeoCStaCallsAvailMax.setStatus("current")
_AgfeoCStaCallsLoadActual_Type = Integer32
_AgfeoCStaCallsLoadActual_Object = MibScalar
agfeoCStaCallsLoadActual = _AgfeoCStaCallsLoadActual_Object(
    (1, 3, 6, 1, 4, 1, 53023, 1, 1, 2, 4, 3),
    _AgfeoCStaCallsLoadActual_Type()
)
agfeoCStaCallsLoadActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agfeoCStaCallsLoadActual.setStatus("current")
_AgfeoCStaCallsLoadMax_Type = Integer32
_AgfeoCStaCallsLoadMax_Object = MibScalar
agfeoCStaCallsLoadMax = _AgfeoCStaCallsLoadMax_Object(
    (1, 3, 6, 1, 4, 1, 53023, 1, 1, 2, 4, 4),
    _AgfeoCStaCallsLoadMax_Type()
)
agfeoCStaCallsLoadMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agfeoCStaCallsLoadMax.setStatus("current")
_AgfeoCommonLicence_ObjectIdentity = ObjectIdentity
agfeoCommonLicence = _AgfeoCommonLicence_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 53023, 1, 1, 3)
)
if mibBuilder.loadTexts:
    agfeoCommonLicence.setStatus("current")
_AgfeoCLicenceTable_Object = MibTable
agfeoCLicenceTable = _AgfeoCLicenceTable_Object(
    (1, 3, 6, 1, 4, 1, 53023, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    agfeoCLicenceTable.setStatus("current")
_AgfeoCLicenceEntry_Object = MibTableRow
agfeoCLicenceEntry = _AgfeoCLicenceEntry_Object(
    (1, 3, 6, 1, 4, 1, 53023, 1, 1, 3, 1, 1)
)
agfeoCLicenceEntry.setIndexNames(
    (0, "AGFEO-PBX-MIB", "agfeoCLicenceIndex"),
)
if mibBuilder.loadTexts:
    agfeoCLicenceEntry.setStatus("current")


class _AgfeoCLicenceIndex_Type(Integer32):
    """Custom type agfeoCLicenceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_AgfeoCLicenceIndex_Type.__name__ = "Integer32"
_AgfeoCLicenceIndex_Object = MibTableColumn
agfeoCLicenceIndex = _AgfeoCLicenceIndex_Object(
    (1, 3, 6, 1, 4, 1, 53023, 1, 1, 3, 1, 1, 1),
    _AgfeoCLicenceIndex_Type()
)
agfeoCLicenceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agfeoCLicenceIndex.setStatus("current")
_AgfeoCLicenceVersion_Type = OctetString
_AgfeoCLicenceVersion_Object = MibTableColumn
agfeoCLicenceVersion = _AgfeoCLicenceVersion_Object(
    (1, 3, 6, 1, 4, 1, 53023, 1, 1, 3, 1, 1, 2),
    _AgfeoCLicenceVersion_Type()
)
agfeoCLicenceVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agfeoCLicenceVersion.setStatus("current")
_AgfeoCLicenceIssue_Type = OctetString
_AgfeoCLicenceIssue_Object = MibTableColumn
agfeoCLicenceIssue = _AgfeoCLicenceIssue_Object(
    (1, 3, 6, 1, 4, 1, 53023, 1, 1, 3, 1, 1, 3),
    _AgfeoCLicenceIssue_Type()
)
agfeoCLicenceIssue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agfeoCLicenceIssue.setStatus("current")
_AgfeoCLicenceUUID_Type = OctetString
_AgfeoCLicenceUUID_Object = MibTableColumn
agfeoCLicenceUUID = _AgfeoCLicenceUUID_Object(
    (1, 3, 6, 1, 4, 1, 53023, 1, 1, 3, 1, 1, 4),
    _AgfeoCLicenceUUID_Type()
)
agfeoCLicenceUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agfeoCLicenceUUID.setStatus("current")
_AgfeoCLicenceSerial_Type = OctetString
_AgfeoCLicenceSerial_Object = MibTableColumn
agfeoCLicenceSerial = _AgfeoCLicenceSerial_Object(
    (1, 3, 6, 1, 4, 1, 53023, 1, 1, 3, 1, 1, 5),
    _AgfeoCLicenceSerial_Type()
)
agfeoCLicenceSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agfeoCLicenceSerial.setStatus("current")
_AgfeoCLicenceCode_Type = OctetString
_AgfeoCLicenceCode_Object = MibTableColumn
agfeoCLicenceCode = _AgfeoCLicenceCode_Object(
    (1, 3, 6, 1, 4, 1, 53023, 1, 1, 3, 1, 1, 6),
    _AgfeoCLicenceCode_Type()
)
agfeoCLicenceCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agfeoCLicenceCode.setStatus("current")
_AgfeoCLicenceAmount_Type = Integer32
_AgfeoCLicenceAmount_Object = MibTableColumn
agfeoCLicenceAmount = _AgfeoCLicenceAmount_Object(
    (1, 3, 6, 1, 4, 1, 53023, 1, 1, 3, 1, 1, 7),
    _AgfeoCLicenceAmount_Type()
)
agfeoCLicenceAmount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agfeoCLicenceAmount.setStatus("current")
_AgfeoCLicenceStart_Type = OctetString
_AgfeoCLicenceStart_Object = MibTableColumn
agfeoCLicenceStart = _AgfeoCLicenceStart_Object(
    (1, 3, 6, 1, 4, 1, 53023, 1, 1, 3, 1, 1, 8),
    _AgfeoCLicenceStart_Type()
)
agfeoCLicenceStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agfeoCLicenceStart.setStatus("current")
_AgfeoCLicenceEnd_Type = OctetString
_AgfeoCLicenceEnd_Object = MibTableColumn
agfeoCLicenceEnd = _AgfeoCLicenceEnd_Object(
    (1, 3, 6, 1, 4, 1, 53023, 1, 1, 3, 1, 1, 9),
    _AgfeoCLicenceEnd_Type()
)
agfeoCLicenceEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agfeoCLicenceEnd.setStatus("current")
_AgfeoCLicenceStatus_Type = OctetString
_AgfeoCLicenceStatus_Object = MibTableColumn
agfeoCLicenceStatus = _AgfeoCLicenceStatus_Object(
    (1, 3, 6, 1, 4, 1, 53023, 1, 1, 3, 1, 1, 10),
    _AgfeoCLicenceStatus_Type()
)
agfeoCLicenceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agfeoCLicenceStatus.setStatus("current")
_AgfeoMibNotify_ObjectIdentity = ObjectIdentity
agfeoMibNotify = _AgfeoMibNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 53023, 2)
)
if mibBuilder.loadTexts:
    agfeoMibNotify.setStatus("current")
_AgfeoEventList_ObjectIdentity = ObjectIdentity
agfeoEventList = _AgfeoEventList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 53023, 2, 0)
)
if mibBuilder.loadTexts:
    agfeoEventList.setStatus("current")
_AgfeoEventProperties_ObjectIdentity = ObjectIdentity
agfeoEventProperties = _AgfeoEventProperties_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 53023, 2, 1)
)
if mibBuilder.loadTexts:
    agfeoEventProperties.setStatus("current")


class _AgfeoEventPropType_Type(Integer32):
    """Custom type agfeoEventPropType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("type0", 0),
          ("type1", 1),
          ("sipaccount", 2),
          ("type3", 3))
    )


_AgfeoEventPropType_Type.__name__ = "Integer32"
_AgfeoEventPropType_Object = MibScalar
agfeoEventPropType = _AgfeoEventPropType_Object(
    (1, 3, 6, 1, 4, 1, 53023, 2, 1, 1),
    _AgfeoEventPropType_Type()
)
agfeoEventPropType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agfeoEventPropType.setStatus("current")


class _AgfeoEventPropSeverity_Type(Integer32):
    """Custom type agfeoEventPropSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("emergency", 0),
          ("alert", 1),
          ("critical", 2),
          ("error", 3),
          ("warning", 4),
          ("notice", 5),
          ("informational", 6),
          ("debug", 7))
    )


_AgfeoEventPropSeverity_Type.__name__ = "Integer32"
_AgfeoEventPropSeverity_Object = MibScalar
agfeoEventPropSeverity = _AgfeoEventPropSeverity_Object(
    (1, 3, 6, 1, 4, 1, 53023, 2, 1, 2),
    _AgfeoEventPropSeverity_Type()
)
agfeoEventPropSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agfeoEventPropSeverity.setStatus("current")
_AgfeoEventPropText_Type = OctetString
_AgfeoEventPropText_Object = MibScalar
agfeoEventPropText = _AgfeoEventPropText_Object(
    (1, 3, 6, 1, 4, 1, 53023, 2, 1, 3),
    _AgfeoEventPropText_Type()
)
agfeoEventPropText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agfeoEventPropText.setStatus("current")
_AgfeoMIBConformance_ObjectIdentity = ObjectIdentity
agfeoMIBConformance = _AgfeoMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 53023, 3)
)
_AgfeoCompliances_ObjectIdentity = ObjectIdentity
agfeoCompliances = _AgfeoCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 53023, 3, 1)
)
_AgfeoGroups_ObjectIdentity = ObjectIdentity
agfeoGroups = _AgfeoGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 53023, 3, 2)
)

# Managed Objects groups

agfeoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 53023, 3, 2, 1)
)
agfeoGroup.setObjects(
      *(("AGFEO-PBX-MIB", "agfeoCStaPbxProduct"),
        ("AGFEO-PBX-MIB", "agfeoCStaPbxProductId"),
        ("AGFEO-PBX-MIB", "agfeoCStaPbxFirmware"),
        ("AGFEO-PBX-MIB", "agfeoCStaPbxAppUpTime"))
)
if mibBuilder.loadTexts:
    agfeoGroup.setStatus("current")

agfeoAccountGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 53023, 3, 2, 2)
)
agfeoAccountGroup.setObjects(
      *(("AGFEO-PBX-MIB", "agfeoCStaSipTestInteger"),
        ("AGFEO-PBX-MIB", "agfeoCCfgSipAccountName"),
        ("AGFEO-PBX-MIB", "agfeoCCfgSipAccountActive"),
        ("AGFEO-PBX-MIB", "agfeoCStaSipAccountStatus"),
        ("AGFEO-PBX-MIB", "agfeoCStaSipAccountCause"))
)
if mibBuilder.loadTexts:
    agfeoAccountGroup.setStatus("current")

agfeoPropGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 53023, 3, 2, 3)
)
agfeoPropGroup.setObjects(
      *(("AGFEO-PBX-MIB", "agfeoEventPropType"),
        ("AGFEO-PBX-MIB", "agfeoEventPropSeverity"),
        ("AGFEO-PBX-MIB", "agfeoEventPropText"))
)
if mibBuilder.loadTexts:
    agfeoPropGroup.setStatus("current")


# Notification objects

agfeoEventGeneric = NotificationType(
    (1, 3, 6, 1, 4, 1, 53023, 2, 0, 1)
)
agfeoEventGeneric.setObjects(
      *(("AGFEO-PBX-MIB", "agfeoEventPropType"),
        ("AGFEO-PBX-MIB", "agfeoEventPropSeverity"),
        ("AGFEO-PBX-MIB", "agfeoEventPropText"))
)
if mibBuilder.loadTexts:
    agfeoEventGeneric.setStatus(
        "current"
    )


# Notifications groups

agfeoBasicNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 53023, 3, 2, 4)
)
agfeoBasicNotificationGroup.setObjects(
    ("AGFEO-PBX-MIB", "agfeoEventGeneric")
)
if mibBuilder.loadTexts:
    agfeoBasicNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

agfeoCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 53023, 3, 1, 1)
)
agfeoCompliance.setObjects(
      *(("AGFEO-PBX-MIB", "agfeoGroup"),
        ("AGFEO-PBX-MIB", "agfeoAccountGroup"),
        ("AGFEO-PBX-MIB", "agfeoPropGroup"),
        ("AGFEO-PBX-MIB", "agfeoBasicNotificationGroup"))
)
if mibBuilder.loadTexts:
    agfeoCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AGFEO-PBX-MIB",
    **{"agfeoMib": agfeoMib,
       "agfeoMibObjects": agfeoMibObjects,
       "agfeoCommon": agfeoCommon,
       "agfeoCommonCfg": agfeoCommonCfg,
       "agfeoCCfgSip": agfeoCCfgSip,
       "agfeoCCfgSipAccountTable": agfeoCCfgSipAccountTable,
       "agfeoCCfgSipAccountEntry": agfeoCCfgSipAccountEntry,
       "agfeoCCfgSipAccountIndex": agfeoCCfgSipAccountIndex,
       "agfeoCCfgSipAccountName": agfeoCCfgSipAccountName,
       "agfeoCCfgSipAccountActive": agfeoCCfgSipAccountActive,
       "agfeoCommonStats": agfeoCommonStats,
       "agfeoCStaGeneral": agfeoCStaGeneral,
       "agfeoCStaPbxProduct": agfeoCStaPbxProduct,
       "agfeoCStaPbxProductId": agfeoCStaPbxProductId,
       "agfeoCStaPbxFirmware": agfeoCStaPbxFirmware,
       "agfeoCStaPbxAppUpTime": agfeoCStaPbxAppUpTime,
       "agfeoCStaSip": agfeoCStaSip,
       "agfeoCStaSipTest": agfeoCStaSipTest,
       "agfeoCStaSipTestInteger": agfeoCStaSipTestInteger,
       "agfeoCStaSipAccountTable": agfeoCStaSipAccountTable,
       "agfeoCStaSipAccountEntry": agfeoCStaSipAccountEntry,
       "agfeoCStaSipAccountIndex": agfeoCStaSipAccountIndex,
       "agfeoCStaSipAccountStatus": agfeoCStaSipAccountStatus,
       "agfeoCStaSipAccountCause": agfeoCStaSipAccountCause,
       "agfeoCStaIpChannel": agfeoCStaIpChannel,
       "agfeoCStaIpChannelAvailActual": agfeoCStaIpChannelAvailActual,
       "agfeoCStaIpChannelAvailMax": agfeoCStaIpChannelAvailMax,
       "agfeoCStaIpChannelLoadActual": agfeoCStaIpChannelLoadActual,
       "agfeoCStaIpChannelLoadMax": agfeoCStaIpChannelLoadMax,
       "agfeoCStaCalls": agfeoCStaCalls,
       "agfeoCStaCallsAvailActual": agfeoCStaCallsAvailActual,
       "agfeoCStaCallsAvailMax": agfeoCStaCallsAvailMax,
       "agfeoCStaCallsLoadActual": agfeoCStaCallsLoadActual,
       "agfeoCStaCallsLoadMax": agfeoCStaCallsLoadMax,
       "agfeoCommonLicence": agfeoCommonLicence,
       "agfeoCLicenceTable": agfeoCLicenceTable,
       "agfeoCLicenceEntry": agfeoCLicenceEntry,
       "agfeoCLicenceIndex": agfeoCLicenceIndex,
       "agfeoCLicenceVersion": agfeoCLicenceVersion,
       "agfeoCLicenceIssue": agfeoCLicenceIssue,
       "agfeoCLicenceUUID": agfeoCLicenceUUID,
       "agfeoCLicenceSerial": agfeoCLicenceSerial,
       "agfeoCLicenceCode": agfeoCLicenceCode,
       "agfeoCLicenceAmount": agfeoCLicenceAmount,
       "agfeoCLicenceStart": agfeoCLicenceStart,
       "agfeoCLicenceEnd": agfeoCLicenceEnd,
       "agfeoCLicenceStatus": agfeoCLicenceStatus,
       "agfeoMibNotify": agfeoMibNotify,
       "agfeoEventList": agfeoEventList,
       "agfeoEventGeneric": agfeoEventGeneric,
       "agfeoEventProperties": agfeoEventProperties,
       "agfeoEventPropType": agfeoEventPropType,
       "agfeoEventPropSeverity": agfeoEventPropSeverity,
       "agfeoEventPropText": agfeoEventPropText,
       "agfeoMIBConformance": agfeoMIBConformance,
       "agfeoCompliances": agfeoCompliances,
       "agfeoCompliance": agfeoCompliance,
       "agfeoGroups": agfeoGroups,
       "agfeoGroup": agfeoGroup,
       "agfeoAccountGroup": agfeoAccountGroup,
       "agfeoPropGroup": agfeoPropGroup,
       "agfeoBasicNotificationGroup": agfeoBasicNotificationGroup}
)
