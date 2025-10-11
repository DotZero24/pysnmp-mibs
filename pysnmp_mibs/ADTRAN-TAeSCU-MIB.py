# SNMP MIB module (ADTRAN-TAeSCU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-TAeSCU-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:33:50 2025
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

(adTrapInformSeqNum,) = mibBuilder.importSymbols(
    "ADTRAN-GENTRAPINFORM-MIB",
    "adTrapInformSeqNum")

(adMgmt,
 adProducts) = mibBuilder.importSymbols(
    "ADTRAN-MIB",
    "adMgmt",
    "adProducts")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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

adTAeSCUmg = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 241)
)
if mibBuilder.loadTexts:
    adTAeSCUmg.setRevisions(
        ("2016-12-07 00:00",
         "2016-09-20 00:00",
         "2016-06-13 00:00",
         "2014-06-10 00:00",
         "2012-08-14 13:00",
         "2012-07-12 00:00",
         "2012-04-23 16:00",
         "2011-06-27 00:00",
         "2007-05-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdTAeSCU_ObjectIdentity = ObjectIdentity
adTAeSCU = _AdTAeSCU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 1, 241)
)
_AdTAeSCUmgNotificationEvents_ObjectIdentity = ObjectIdentity
adTAeSCUmgNotificationEvents = _AdTAeSCUmgNotificationEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 1, 241, 0)
)
if mibBuilder.loadTexts:
    adTAeSCUmgNotificationEvents.setStatus("current")
_AdTAeSCUConfig_ObjectIdentity = ObjectIdentity
adTAeSCUConfig = _AdTAeSCUConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 1)
)
_AdTAeSCUConfigTable_Object = MibTable
adTAeSCUConfigTable = _AdTAeSCUConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 1, 1)
)
if mibBuilder.loadTexts:
    adTAeSCUConfigTable.setStatus("current")
_AdTAeSCUConfigEntry_Object = MibTableRow
adTAeSCUConfigEntry = _AdTAeSCUConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 1, 1, 1)
)
adTAeSCUConfigEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adTAeSCUConfigEntry.setStatus("current")
_AdTAeSCUBootVersion_Type = DisplayString
_AdTAeSCUBootVersion_Object = MibTableColumn
adTAeSCUBootVersion = _AdTAeSCUBootVersion_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 1, 1, 1, 1),
    _AdTAeSCUBootVersion_Type()
)
adTAeSCUBootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeSCUBootVersion.setStatus("current")
_AdTAeSCUCardProv_ObjectIdentity = ObjectIdentity
adTAeSCUCardProv = _AdTAeSCUCardProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 2)
)
_AdTAeSCUCardProvTable_Object = MibTable
adTAeSCUCardProvTable = _AdTAeSCUCardProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 2, 1)
)
if mibBuilder.loadTexts:
    adTAeSCUCardProvTable.setStatus("current")
_AdTAeSCUCardProvEntry_Object = MibTableRow
adTAeSCUCardProvEntry = _AdTAeSCUCardProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 2, 1, 1)
)
adTAeSCUCardProvEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adTAeSCUCardProvEntry.setStatus("current")


class _AdTAeSCUDefaultRouteInterface_Type(Integer32):
    """Custom type adTAeSCUDefaultRouteInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("in-band", 2))
    )


_AdTAeSCUDefaultRouteInterface_Type.__name__ = "Integer32"
_AdTAeSCUDefaultRouteInterface_Object = MibTableColumn
adTAeSCUDefaultRouteInterface = _AdTAeSCUDefaultRouteInterface_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 2, 1, 1, 1),
    _AdTAeSCUDefaultRouteInterface_Type()
)
adTAeSCUDefaultRouteInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUDefaultRouteInterface.setStatus("deprecated")


class _AdTAeSCUIpForwarding_Type(Integer32):
    """Custom type adTAeSCUIpForwarding based on Integer32"""
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


_AdTAeSCUIpForwarding_Type.__name__ = "Integer32"
_AdTAeSCUIpForwarding_Object = MibTableColumn
adTAeSCUIpForwarding = _AdTAeSCUIpForwarding_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 2, 1, 1, 2),
    _AdTAeSCUIpForwarding_Type()
)
adTAeSCUIpForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUIpForwarding.setStatus("current")


class _AdTAeSCURestoreNetProvFromMUX_Type(Integer32):
    """Custom type adTAeSCURestoreNetProvFromMUX based on Integer32"""
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


_AdTAeSCURestoreNetProvFromMUX_Type.__name__ = "Integer32"
_AdTAeSCURestoreNetProvFromMUX_Object = MibTableColumn
adTAeSCURestoreNetProvFromMUX = _AdTAeSCURestoreNetProvFromMUX_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 2, 1, 1, 3),
    _AdTAeSCURestoreNetProvFromMUX_Type()
)
adTAeSCURestoreNetProvFromMUX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCURestoreNetProvFromMUX.setStatus("current")


class _AdTAeSCUDefaultRouteInterfaceEx_Type(Integer32):
    """Custom type adTAeSCUDefaultRouteInterfaceEx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              999)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("in-band", 2),
          ("local-PPP", 3),
          ("osiTunnel", 4),
          ("pppDCC0", 5),
          ("ethernet2", 6),
          ("none", 999))
    )


_AdTAeSCUDefaultRouteInterfaceEx_Type.__name__ = "Integer32"
_AdTAeSCUDefaultRouteInterfaceEx_Object = MibTableColumn
adTAeSCUDefaultRouteInterfaceEx = _AdTAeSCUDefaultRouteInterfaceEx_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 2, 1, 1, 4),
    _AdTAeSCUDefaultRouteInterfaceEx_Type()
)
adTAeSCUDefaultRouteInterfaceEx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUDefaultRouteInterfaceEx.setStatus("current")


class _AdTAeSCULogoffCraftDTRLoss_Type(Integer32):
    """Custom type adTAeSCULogoffCraftDTRLoss based on Integer32"""
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


_AdTAeSCULogoffCraftDTRLoss_Type.__name__ = "Integer32"
_AdTAeSCULogoffCraftDTRLoss_Object = MibTableColumn
adTAeSCULogoffCraftDTRLoss = _AdTAeSCULogoffCraftDTRLoss_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 2, 1, 1, 5),
    _AdTAeSCULogoffCraftDTRLoss_Type()
)
adTAeSCULogoffCraftDTRLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCULogoffCraftDTRLoss.setStatus("current")


class _AdTAeSCUMinMenuRefresh_Type(Integer32):
    """Custom type adTAeSCUMinMenuRefresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("seconds1", 2),
          ("seconds5", 3),
          ("seconds15", 4),
          ("seconds60", 5),
          ("never", 6))
    )


_AdTAeSCUMinMenuRefresh_Type.__name__ = "Integer32"
_AdTAeSCUMinMenuRefresh_Object = MibTableColumn
adTAeSCUMinMenuRefresh = _AdTAeSCUMinMenuRefresh_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 2, 1, 1, 6),
    _AdTAeSCUMinMenuRefresh_Type()
)
adTAeSCUMinMenuRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUMinMenuRefresh.setStatus("current")
_AdTAeSCUInterfaceStatus_ObjectIdentity = ObjectIdentity
adTAeSCUInterfaceStatus = _AdTAeSCUInterfaceStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 4)
)
_AdTAeSCUInterfaceStatusTable_Object = MibTable
adTAeSCUInterfaceStatusTable = _AdTAeSCUInterfaceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 4, 1)
)
if mibBuilder.loadTexts:
    adTAeSCUInterfaceStatusTable.setStatus("current")
_AdTAeSCUInterfaceStatusEntry_Object = MibTableRow
adTAeSCUInterfaceStatusEntry = _AdTAeSCUInterfaceStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 4, 1, 1)
)
adTAeSCUInterfaceStatusEntry.setIndexNames(
    (0, "ADTRAN-TAeSCU-MIB", "adTAeSCUIfNumber"),
)
if mibBuilder.loadTexts:
    adTAeSCUInterfaceStatusEntry.setStatus("current")
_AdTAeSCUIfNumber_Type = Integer32
_AdTAeSCUIfNumber_Object = MibTableColumn
adTAeSCUIfNumber = _AdTAeSCUIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 4, 1, 1, 1),
    _AdTAeSCUIfNumber_Type()
)
adTAeSCUIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeSCUIfNumber.setStatus("current")
_AdTAeSCUIfIndex_Type = Integer32
_AdTAeSCUIfIndex_Object = MibTableColumn
adTAeSCUIfIndex = _AdTAeSCUIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 4, 1, 1, 2),
    _AdTAeSCUIfIndex_Type()
)
adTAeSCUIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeSCUIfIndex.setStatus("current")
_AdTAeSCUIfIPAddress_Type = IpAddress
_AdTAeSCUIfIPAddress_Object = MibTableColumn
adTAeSCUIfIPAddress = _AdTAeSCUIfIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 4, 1, 1, 3),
    _AdTAeSCUIfIPAddress_Type()
)
adTAeSCUIfIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeSCUIfIPAddress.setStatus("current")
_AdTAeSCUIfSubnetMask_Type = IpAddress
_AdTAeSCUIfSubnetMask_Object = MibTableColumn
adTAeSCUIfSubnetMask = _AdTAeSCUIfSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 4, 1, 1, 4),
    _AdTAeSCUIfSubnetMask_Type()
)
adTAeSCUIfSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeSCUIfSubnetMask.setStatus("current")
_AdTAeSCUIfDefaultGateway_Type = IpAddress
_AdTAeSCUIfDefaultGateway_Object = MibTableColumn
adTAeSCUIfDefaultGateway = _AdTAeSCUIfDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 4, 1, 1, 5),
    _AdTAeSCUIfDefaultGateway_Type()
)
adTAeSCUIfDefaultGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeSCUIfDefaultGateway.setStatus("current")


class _AdTAeSCUIfSpeed_Type(Integer32):
    """Custom type adTAeSCUIfSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("bt-10", 2),
          ("bt-100", 3))
    )


_AdTAeSCUIfSpeed_Type.__name__ = "Integer32"
_AdTAeSCUIfSpeed_Object = MibTableColumn
adTAeSCUIfSpeed = _AdTAeSCUIfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 4, 1, 1, 6),
    _AdTAeSCUIfSpeed_Type()
)
adTAeSCUIfSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeSCUIfSpeed.setStatus("current")


class _AdTAeSCUIfXoverCorrection_Type(Integer32):
    """Custom type adTAeSCUIfXoverCorrection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("straight", 2),
          ("crossover", 3))
    )


_AdTAeSCUIfXoverCorrection_Type.__name__ = "Integer32"
_AdTAeSCUIfXoverCorrection_Object = MibTableColumn
adTAeSCUIfXoverCorrection = _AdTAeSCUIfXoverCorrection_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 4, 1, 1, 7),
    _AdTAeSCUIfXoverCorrection_Type()
)
adTAeSCUIfXoverCorrection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeSCUIfXoverCorrection.setStatus("current")


class _AdTAeSCUIfLEDmode_Type(Integer32):
    """Custom type adTAeSCUIfLEDmode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("link", 1),
          ("blinkactivity", 2))
    )


_AdTAeSCUIfLEDmode_Type.__name__ = "Integer32"
_AdTAeSCUIfLEDmode_Object = MibTableColumn
adTAeSCUIfLEDmode = _AdTAeSCUIfLEDmode_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 4, 1, 1, 8),
    _AdTAeSCUIfLEDmode_Type()
)
adTAeSCUIfLEDmode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeSCUIfLEDmode.setStatus("current")


class _AdTAeSCUIfLinkStatus_Type(Integer32):
    """Custom type adTAeSCUIfLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_AdTAeSCUIfLinkStatus_Type.__name__ = "Integer32"
_AdTAeSCUIfLinkStatus_Object = MibTableColumn
adTAeSCUIfLinkStatus = _AdTAeSCUIfLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 4, 1, 1, 9),
    _AdTAeSCUIfLinkStatus_Type()
)
adTAeSCUIfLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeSCUIfLinkStatus.setStatus("current")


class _AdTAeSCUIfLinkRate_Type(Integer32):
    """Custom type adTAeSCUIfLinkRate based on Integer32"""
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
        *(("unknown", 1),
          ("half-duplex-10bt", 2),
          ("half-duplex-100bt", 3),
          ("full-duplex-10bt", 4),
          ("full-duplex-100bt", 5))
    )


_AdTAeSCUIfLinkRate_Type.__name__ = "Integer32"
_AdTAeSCUIfLinkRate_Object = MibTableColumn
adTAeSCUIfLinkRate = _AdTAeSCUIfLinkRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 4, 1, 1, 10),
    _AdTAeSCUIfLinkRate_Type()
)
adTAeSCUIfLinkRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeSCUIfLinkRate.setStatus("current")
_AdTAeSCUSecurityAccountMg_ObjectIdentity = ObjectIdentity
adTAeSCUSecurityAccountMg = _AdTAeSCUSecurityAccountMg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5)
)


class _AdTAeSCUSecurityAccountEnabled_Type(Integer32):
    """Custom type adTAeSCUSecurityAccountEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("scuSNMPSecurityManagementEnabled", 1),
          ("scuSNMPSecurityManagementDisabled", 2))
    )


_AdTAeSCUSecurityAccountEnabled_Type.__name__ = "Integer32"
_AdTAeSCUSecurityAccountEnabled_Object = MibScalar
adTAeSCUSecurityAccountEnabled = _AdTAeSCUSecurityAccountEnabled_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 1),
    _AdTAeSCUSecurityAccountEnabled_Type()
)
adTAeSCUSecurityAccountEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeSCUSecurityAccountEnabled.setStatus("current")
_AdTAeSCUSecAgingGlobalSettings_ObjectIdentity = ObjectIdentity
adTAeSCUSecAgingGlobalSettings = _AdTAeSCUSecAgingGlobalSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 2)
)


class _AdTAeSCUSecAllAccountExpirationTimer_Type(Integer32):
    """Custom type adTAeSCUSecAllAccountExpirationTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 365),
    )


_AdTAeSCUSecAllAccountExpirationTimer_Type.__name__ = "Integer32"
_AdTAeSCUSecAllAccountExpirationTimer_Object = MibScalar
adTAeSCUSecAllAccountExpirationTimer = _AdTAeSCUSecAllAccountExpirationTimer_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 2, 1),
    _AdTAeSCUSecAllAccountExpirationTimer_Type()
)
adTAeSCUSecAllAccountExpirationTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUSecAllAccountExpirationTimer.setStatus("current")


class _AdTAeSCUSecReadOnlyAccountExpirationTimer_Type(Integer32):
    """Custom type adTAeSCUSecReadOnlyAccountExpirationTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 365),
    )


_AdTAeSCUSecReadOnlyAccountExpirationTimer_Type.__name__ = "Integer32"
_AdTAeSCUSecReadOnlyAccountExpirationTimer_Object = MibScalar
adTAeSCUSecReadOnlyAccountExpirationTimer = _AdTAeSCUSecReadOnlyAccountExpirationTimer_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 2, 2),
    _AdTAeSCUSecReadOnlyAccountExpirationTimer_Type()
)
adTAeSCUSecReadOnlyAccountExpirationTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUSecReadOnlyAccountExpirationTimer.setStatus("current")


class _AdTAeSCUSecReadWriteAccountExpirationTimer_Type(Integer32):
    """Custom type adTAeSCUSecReadWriteAccountExpirationTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 365),
    )


_AdTAeSCUSecReadWriteAccountExpirationTimer_Type.__name__ = "Integer32"
_AdTAeSCUSecReadWriteAccountExpirationTimer_Object = MibScalar
adTAeSCUSecReadWriteAccountExpirationTimer = _AdTAeSCUSecReadWriteAccountExpirationTimer_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 2, 3),
    _AdTAeSCUSecReadWriteAccountExpirationTimer_Type()
)
adTAeSCUSecReadWriteAccountExpirationTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUSecReadWriteAccountExpirationTimer.setStatus("current")


class _AdTAeSCUSecTestAccountExpirationTimer_Type(Integer32):
    """Custom type adTAeSCUSecTestAccountExpirationTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 365),
    )


_AdTAeSCUSecTestAccountExpirationTimer_Type.__name__ = "Integer32"
_AdTAeSCUSecTestAccountExpirationTimer_Object = MibScalar
adTAeSCUSecTestAccountExpirationTimer = _AdTAeSCUSecTestAccountExpirationTimer_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 2, 4),
    _AdTAeSCUSecTestAccountExpirationTimer_Type()
)
adTAeSCUSecTestAccountExpirationTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUSecTestAccountExpirationTimer.setStatus("current")


class _AdTAeSCUSecConfigAccountExpirationTimer_Type(Integer32):
    """Custom type adTAeSCUSecConfigAccountExpirationTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 365),
    )


_AdTAeSCUSecConfigAccountExpirationTimer_Type.__name__ = "Integer32"
_AdTAeSCUSecConfigAccountExpirationTimer_Object = MibScalar
adTAeSCUSecConfigAccountExpirationTimer = _AdTAeSCUSecConfigAccountExpirationTimer_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 2, 5),
    _AdTAeSCUSecConfigAccountExpirationTimer_Type()
)
adTAeSCUSecConfigAccountExpirationTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUSecConfigAccountExpirationTimer.setStatus("current")


class _AdTAeSCUSecAdminAccountExpirationTimer_Type(Integer32):
    """Custom type adTAeSCUSecAdminAccountExpirationTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 365),
    )


_AdTAeSCUSecAdminAccountExpirationTimer_Type.__name__ = "Integer32"
_AdTAeSCUSecAdminAccountExpirationTimer_Object = MibScalar
adTAeSCUSecAdminAccountExpirationTimer = _AdTAeSCUSecAdminAccountExpirationTimer_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 2, 6),
    _AdTAeSCUSecAdminAccountExpirationTimer_Type()
)
adTAeSCUSecAdminAccountExpirationTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUSecAdminAccountExpirationTimer.setStatus("current")


class _AdTAeSCUSecSendAcctExpAlarm_Type(Integer32):
    """Custom type adTAeSCUSecSendAcctExpAlarm based on Integer32"""
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


_AdTAeSCUSecSendAcctExpAlarm_Type.__name__ = "Integer32"
_AdTAeSCUSecSendAcctExpAlarm_Object = MibScalar
adTAeSCUSecSendAcctExpAlarm = _AdTAeSCUSecSendAcctExpAlarm_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 2, 7),
    _AdTAeSCUSecSendAcctExpAlarm_Type()
)
adTAeSCUSecSendAcctExpAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUSecSendAcctExpAlarm.setStatus("current")


class _AdTAeSCUSecResetAllAccountAge_Type(Integer32):
    """Custom type adTAeSCUSecResetAllAccountAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_AdTAeSCUSecResetAllAccountAge_Type.__name__ = "Integer32"
_AdTAeSCUSecResetAllAccountAge_Object = MibScalar
adTAeSCUSecResetAllAccountAge = _AdTAeSCUSecResetAllAccountAge_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 2, 8),
    _AdTAeSCUSecResetAllAccountAge_Type()
)
adTAeSCUSecResetAllAccountAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUSecResetAllAccountAge.setStatus("current")


class _AdTAeSCUSecAllPasswordExpirationTimer_Type(Integer32):
    """Custom type adTAeSCUSecAllPasswordExpirationTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 365),
    )


_AdTAeSCUSecAllPasswordExpirationTimer_Type.__name__ = "Integer32"
_AdTAeSCUSecAllPasswordExpirationTimer_Object = MibScalar
adTAeSCUSecAllPasswordExpirationTimer = _AdTAeSCUSecAllPasswordExpirationTimer_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 2, 10),
    _AdTAeSCUSecAllPasswordExpirationTimer_Type()
)
adTAeSCUSecAllPasswordExpirationTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUSecAllPasswordExpirationTimer.setStatus("current")


class _AdTAeSCUSecReadOnlyPasswordExpirationTimer_Type(Integer32):
    """Custom type adTAeSCUSecReadOnlyPasswordExpirationTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 365),
    )


_AdTAeSCUSecReadOnlyPasswordExpirationTimer_Type.__name__ = "Integer32"
_AdTAeSCUSecReadOnlyPasswordExpirationTimer_Object = MibScalar
adTAeSCUSecReadOnlyPasswordExpirationTimer = _AdTAeSCUSecReadOnlyPasswordExpirationTimer_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 2, 11),
    _AdTAeSCUSecReadOnlyPasswordExpirationTimer_Type()
)
adTAeSCUSecReadOnlyPasswordExpirationTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUSecReadOnlyPasswordExpirationTimer.setStatus("current")


class _AdTAeSCUSecReadWritePasswordExpirationTimer_Type(Integer32):
    """Custom type adTAeSCUSecReadWritePasswordExpirationTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 365),
    )


_AdTAeSCUSecReadWritePasswordExpirationTimer_Type.__name__ = "Integer32"
_AdTAeSCUSecReadWritePasswordExpirationTimer_Object = MibScalar
adTAeSCUSecReadWritePasswordExpirationTimer = _AdTAeSCUSecReadWritePasswordExpirationTimer_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 2, 12),
    _AdTAeSCUSecReadWritePasswordExpirationTimer_Type()
)
adTAeSCUSecReadWritePasswordExpirationTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUSecReadWritePasswordExpirationTimer.setStatus("current")


class _AdTAeSCUSecTestPasswordExpirationTimer_Type(Integer32):
    """Custom type adTAeSCUSecTestPasswordExpirationTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 365),
    )


_AdTAeSCUSecTestPasswordExpirationTimer_Type.__name__ = "Integer32"
_AdTAeSCUSecTestPasswordExpirationTimer_Object = MibScalar
adTAeSCUSecTestPasswordExpirationTimer = _AdTAeSCUSecTestPasswordExpirationTimer_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 2, 13),
    _AdTAeSCUSecTestPasswordExpirationTimer_Type()
)
adTAeSCUSecTestPasswordExpirationTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUSecTestPasswordExpirationTimer.setStatus("current")


class _AdTAeSCUSecConfigPasswordExpirationTimer_Type(Integer32):
    """Custom type adTAeSCUSecConfigPasswordExpirationTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 365),
    )


_AdTAeSCUSecConfigPasswordExpirationTimer_Type.__name__ = "Integer32"
_AdTAeSCUSecConfigPasswordExpirationTimer_Object = MibScalar
adTAeSCUSecConfigPasswordExpirationTimer = _AdTAeSCUSecConfigPasswordExpirationTimer_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 2, 14),
    _AdTAeSCUSecConfigPasswordExpirationTimer_Type()
)
adTAeSCUSecConfigPasswordExpirationTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUSecConfigPasswordExpirationTimer.setStatus("current")


class _AdTAeSCUSecAdminPasswordExpirationTimer_Type(Integer32):
    """Custom type adTAeSCUSecAdminPasswordExpirationTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 365),
    )


_AdTAeSCUSecAdminPasswordExpirationTimer_Type.__name__ = "Integer32"
_AdTAeSCUSecAdminPasswordExpirationTimer_Object = MibScalar
adTAeSCUSecAdminPasswordExpirationTimer = _AdTAeSCUSecAdminPasswordExpirationTimer_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 2, 15),
    _AdTAeSCUSecAdminPasswordExpirationTimer_Type()
)
adTAeSCUSecAdminPasswordExpirationTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUSecAdminPasswordExpirationTimer.setStatus("current")


class _AdTAeSCUSecPasswordExpirationWarning_Type(Integer32):
    """Custom type adTAeSCUSecPasswordExpirationWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AdTAeSCUSecPasswordExpirationWarning_Type.__name__ = "Integer32"
_AdTAeSCUSecPasswordExpirationWarning_Object = MibScalar
adTAeSCUSecPasswordExpirationWarning = _AdTAeSCUSecPasswordExpirationWarning_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 2, 20),
    _AdTAeSCUSecPasswordExpirationWarning_Type()
)
adTAeSCUSecPasswordExpirationWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUSecPasswordExpirationWarning.setStatus("current")


class _AdTAeSCUSecResetAllPasswordAge_Type(Integer32):
    """Custom type adTAeSCUSecResetAllPasswordAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_AdTAeSCUSecResetAllPasswordAge_Type.__name__ = "Integer32"
_AdTAeSCUSecResetAllPasswordAge_Object = MibScalar
adTAeSCUSecResetAllPasswordAge = _AdTAeSCUSecResetAllPasswordAge_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 2, 21),
    _AdTAeSCUSecResetAllPasswordAge_Type()
)
adTAeSCUSecResetAllPasswordAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUSecResetAllPasswordAge.setStatus("current")
_AdTAeSCUSecAccountTable_Object = MibTable
adTAeSCUSecAccountTable = _AdTAeSCUSecAccountTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 3)
)
if mibBuilder.loadTexts:
    adTAeSCUSecAccountTable.setStatus("current")
_AdTAeSCUSecAccountEntry_Object = MibTableRow
adTAeSCUSecAccountEntry = _AdTAeSCUSecAccountEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 3, 1)
)
adTAeSCUSecAccountEntry.setIndexNames(
    (0, "ADTRAN-TAeSCU-MIB", "adTAeSCUSecAccountIndex"),
)
if mibBuilder.loadTexts:
    adTAeSCUSecAccountEntry.setStatus("current")


class _AdTAeSCUSecAccountIndex_Type(Integer32):
    """Custom type adTAeSCUSecAccountIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AdTAeSCUSecAccountIndex_Type.__name__ = "Integer32"
_AdTAeSCUSecAccountIndex_Object = MibTableColumn
adTAeSCUSecAccountIndex = _AdTAeSCUSecAccountIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 3, 1, 1),
    _AdTAeSCUSecAccountIndex_Type()
)
adTAeSCUSecAccountIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeSCUSecAccountIndex.setStatus("current")


class _AdTAeSCUSecAccountUserID_Type(DisplayString):
    """Custom type adTAeSCUSecAccountUserID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AdTAeSCUSecAccountUserID_Type.__name__ = "DisplayString"
_AdTAeSCUSecAccountUserID_Object = MibTableColumn
adTAeSCUSecAccountUserID = _AdTAeSCUSecAccountUserID_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 3, 1, 2),
    _AdTAeSCUSecAccountUserID_Type()
)
adTAeSCUSecAccountUserID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUSecAccountUserID.setStatus("current")


class _AdTAeSCUSecAccountStatus_Type(Integer32):
    """Custom type adTAeSCUSecAccountStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createdEnabled", 1),
          ("createdDisabled", 2),
          ("deleted", 3))
    )


_AdTAeSCUSecAccountStatus_Type.__name__ = "Integer32"
_AdTAeSCUSecAccountStatus_Object = MibTableColumn
adTAeSCUSecAccountStatus = _AdTAeSCUSecAccountStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 3, 1, 3),
    _AdTAeSCUSecAccountStatus_Type()
)
adTAeSCUSecAccountStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUSecAccountStatus.setStatus("current")
_AdTAeSCUSecNumAccountLogin_Type = Integer32
_AdTAeSCUSecNumAccountLogin_Object = MibTableColumn
adTAeSCUSecNumAccountLogin = _AdTAeSCUSecNumAccountLogin_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 3, 1, 4),
    _AdTAeSCUSecNumAccountLogin_Type()
)
adTAeSCUSecNumAccountLogin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeSCUSecNumAccountLogin.setStatus("current")


class _AdTAeSCUSecAccountAccessRights_Type(Integer32):
    """Custom type adTAeSCUSecAccountAccessRights based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("readOnlyAccess", 1),
          ("readWriteAccess", 2),
          ("testAccess", 3),
          ("adminAccess", 4),
          ("fronPanelAccess", 5),
          ("techSupportAccess", 6),
          ("configAccess", 7))
    )


_AdTAeSCUSecAccountAccessRights_Type.__name__ = "Integer32"
_AdTAeSCUSecAccountAccessRights_Object = MibTableColumn
adTAeSCUSecAccountAccessRights = _AdTAeSCUSecAccountAccessRights_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 3, 1, 5),
    _AdTAeSCUSecAccountAccessRights_Type()
)
adTAeSCUSecAccountAccessRights.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUSecAccountAccessRights.setStatus("current")


class _AdTAESCUSecChangeAccountPassword_Type(DisplayString):
    """Custom type adTAESCUSecChangeAccountPassword based on DisplayString"""
    defaultValue = OctetString("********")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 33),
    )


_AdTAESCUSecChangeAccountPassword_Type.__name__ = "DisplayString"
_AdTAESCUSecChangeAccountPassword_Object = MibTableColumn
adTAESCUSecChangeAccountPassword = _AdTAESCUSecChangeAccountPassword_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 3, 1, 7),
    _AdTAESCUSecChangeAccountPassword_Type()
)
adTAESCUSecChangeAccountPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAESCUSecChangeAccountPassword.setStatus("current")


class _AdTAeSCUSecAccStatusExt_Type(Integer32):
    """Custom type adTAeSCUSecAccStatusExt based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("deleted", 1),
          ("enabled", 2),
          ("disabled", 3),
          ("enabledExpired", 4),
          ("disabledExpired", 5),
          ("enabledLocked", 6),
          ("disabledLocked", 7),
          ("enabledExpiredLocked", 8),
          ("disabledExpiredLocked", 9))
    )


_AdTAeSCUSecAccStatusExt_Type.__name__ = "Integer32"
_AdTAeSCUSecAccStatusExt_Object = MibTableColumn
adTAeSCUSecAccStatusExt = _AdTAeSCUSecAccStatusExt_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 3, 1, 8),
    _AdTAeSCUSecAccStatusExt_Type()
)
adTAeSCUSecAccStatusExt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUSecAccStatusExt.setStatus("current")


class _AdTAeSCUSecAccExpTime_Type(Integer32):
    """Custom type adTAeSCUSecAccExpTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 365),
    )


_AdTAeSCUSecAccExpTime_Type.__name__ = "Integer32"
_AdTAeSCUSecAccExpTime_Object = MibTableColumn
adTAeSCUSecAccExpTime = _AdTAeSCUSecAccExpTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 3, 1, 9),
    _AdTAeSCUSecAccExpTime_Type()
)
adTAeSCUSecAccExpTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUSecAccExpTime.setStatus("current")


class _AdTAeSCUSecAccPasswordExpTime_Type(Integer32):
    """Custom type adTAeSCUSecAccPasswordExpTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 365),
    )


_AdTAeSCUSecAccPasswordExpTime_Type.__name__ = "Integer32"
_AdTAeSCUSecAccPasswordExpTime_Object = MibTableColumn
adTAeSCUSecAccPasswordExpTime = _AdTAeSCUSecAccPasswordExpTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 3, 1, 10),
    _AdTAeSCUSecAccPasswordExpTime_Type()
)
adTAeSCUSecAccPasswordExpTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUSecAccPasswordExpTime.setStatus("current")
_AdTAeSCUSecAccountAge_Type = Integer32
_AdTAeSCUSecAccountAge_Object = MibTableColumn
adTAeSCUSecAccountAge = _AdTAeSCUSecAccountAge_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 3, 1, 11),
    _AdTAeSCUSecAccountAge_Type()
)
adTAeSCUSecAccountAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeSCUSecAccountAge.setStatus("current")
_AdTAeSCUSecAccPasswordAge_Type = Integer32
_AdTAeSCUSecAccPasswordAge_Object = MibTableColumn
adTAeSCUSecAccPasswordAge = _AdTAeSCUSecAccPasswordAge_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 3, 1, 12),
    _AdTAeSCUSecAccPasswordAge_Type()
)
adTAeSCUSecAccPasswordAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeSCUSecAccPasswordAge.setStatus("current")


class _AdTAeSCUSecResetAccountAge_Type(Integer32):
    """Custom type adTAeSCUSecResetAccountAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("resetAccountAge", 1)
    )


_AdTAeSCUSecResetAccountAge_Type.__name__ = "Integer32"
_AdTAeSCUSecResetAccountAge_Object = MibTableColumn
adTAeSCUSecResetAccountAge = _AdTAeSCUSecResetAccountAge_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 3, 1, 13),
    _AdTAeSCUSecResetAccountAge_Type()
)
adTAeSCUSecResetAccountAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUSecResetAccountAge.setStatus("current")


class _AdTAeSCUSecResetAccPasswordAge_Type(Integer32):
    """Custom type adTAeSCUSecResetAccPasswordAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("resetPasswordAge", 1)
    )


_AdTAeSCUSecResetAccPasswordAge_Type.__name__ = "Integer32"
_AdTAeSCUSecResetAccPasswordAge_Object = MibTableColumn
adTAeSCUSecResetAccPasswordAge = _AdTAeSCUSecResetAccPasswordAge_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 3, 1, 14),
    _AdTAeSCUSecResetAccPasswordAge_Type()
)
adTAeSCUSecResetAccPasswordAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUSecResetAccPasswordAge.setStatus("current")


class _AdTAeSCUAccExpirationEnabled_Type(Integer32):
    """Custom type adTAeSCUAccExpirationEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accountExpirationEnabled", 1),
          ("accountExpirationDisabled", 2))
    )


_AdTAeSCUAccExpirationEnabled_Type.__name__ = "Integer32"
_AdTAeSCUAccExpirationEnabled_Object = MibTableColumn
adTAeSCUAccExpirationEnabled = _AdTAeSCUAccExpirationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 3, 1, 15),
    _AdTAeSCUAccExpirationEnabled_Type()
)
adTAeSCUAccExpirationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUAccExpirationEnabled.setStatus("current")


class _AdTAeSCUAccPasswordAccAgingEnabled_Type(Integer32):
    """Custom type adTAeSCUAccPasswordAccAgingEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("passwordAgingEnabled", 1),
          ("passwordAgingDisabled", 2))
    )


_AdTAeSCUAccPasswordAccAgingEnabled_Type.__name__ = "Integer32"
_AdTAeSCUAccPasswordAccAgingEnabled_Object = MibTableColumn
adTAeSCUAccPasswordAccAgingEnabled = _AdTAeSCUAccPasswordAccAgingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 3, 1, 16),
    _AdTAeSCUAccPasswordAccAgingEnabled_Type()
)
adTAeSCUAccPasswordAccAgingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUAccPasswordAccAgingEnabled.setStatus("current")


class _AdTAeSCUSecForcePasswordReset_Type(Integer32):
    """Custom type adTAeSCUSecForcePasswordReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forcedreset", 1),
          ("clearforcedreset", 2))
    )


_AdTAeSCUSecForcePasswordReset_Type.__name__ = "Integer32"
_AdTAeSCUSecForcePasswordReset_Object = MibTableColumn
adTAeSCUSecForcePasswordReset = _AdTAeSCUSecForcePasswordReset_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 3, 1, 17),
    _AdTAeSCUSecForcePasswordReset_Type()
)
adTAeSCUSecForcePasswordReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUSecForcePasswordReset.setStatus("current")
_AdTAeSCUSecAccountLoggedInTable_Object = MibTable
adTAeSCUSecAccountLoggedInTable = _AdTAeSCUSecAccountLoggedInTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 4)
)
if mibBuilder.loadTexts:
    adTAeSCUSecAccountLoggedInTable.setStatus("current")
_AdTAeSCUSecAccountLoggedInEntry_Object = MibTableRow
adTAeSCUSecAccountLoggedInEntry = _AdTAeSCUSecAccountLoggedInEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 4, 1)
)
adTAeSCUSecAccountLoggedInEntry.setIndexNames(
    (0, "ADTRAN-TAeSCU-MIB", "adTAeSCUSecAccountloginIndex"),
)
if mibBuilder.loadTexts:
    adTAeSCUSecAccountLoggedInEntry.setStatus("current")


class _AdTAeSCUSecAccountloginIndex_Type(Integer32):
    """Custom type adTAeSCUSecAccountloginIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AdTAeSCUSecAccountloginIndex_Type.__name__ = "Integer32"
_AdTAeSCUSecAccountloginIndex_Object = MibTableColumn
adTAeSCUSecAccountloginIndex = _AdTAeSCUSecAccountloginIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 4, 1, 1),
    _AdTAeSCUSecAccountloginIndex_Type()
)
adTAeSCUSecAccountloginIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeSCUSecAccountloginIndex.setStatus("current")


class _AdTAeSCUSecAccountLoginUserIDIndex_Type(Integer32):
    """Custom type adTAeSCUSecAccountLoginUserIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AdTAeSCUSecAccountLoginUserIDIndex_Type.__name__ = "Integer32"
_AdTAeSCUSecAccountLoginUserIDIndex_Object = MibTableColumn
adTAeSCUSecAccountLoginUserIDIndex = _AdTAeSCUSecAccountLoginUserIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 4, 1, 2),
    _AdTAeSCUSecAccountLoginUserIDIndex_Type()
)
adTAeSCUSecAccountLoginUserIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeSCUSecAccountLoginUserIDIndex.setStatus("current")


class _AdTAeSCUSecAccountLoginUserID_Type(DisplayString):
    """Custom type adTAeSCUSecAccountLoginUserID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AdTAeSCUSecAccountLoginUserID_Type.__name__ = "DisplayString"
_AdTAeSCUSecAccountLoginUserID_Object = MibTableColumn
adTAeSCUSecAccountLoginUserID = _AdTAeSCUSecAccountLoginUserID_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 4, 1, 3),
    _AdTAeSCUSecAccountLoginUserID_Type()
)
adTAeSCUSecAccountLoginUserID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeSCUSecAccountLoginUserID.setStatus("current")


class _AdTAeSCUSecAccountConnectionType_Type(Integer32):
    """Custom type adTAeSCUSecAccountConnectionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("craft", 1),
          ("adminPort", 2),
          ("ip", 3),
          ("x25", 4),
          ("rs485", 5),
          ("dcc", 6),
          ("fcd", 7),
          ("invalidConnection", 8))
    )


_AdTAeSCUSecAccountConnectionType_Type.__name__ = "Integer32"
_AdTAeSCUSecAccountConnectionType_Object = MibTableColumn
adTAeSCUSecAccountConnectionType = _AdTAeSCUSecAccountConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 4, 1, 4),
    _AdTAeSCUSecAccountConnectionType_Type()
)
adTAeSCUSecAccountConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeSCUSecAccountConnectionType.setStatus("current")


class _AdTAeSCUSecAccountSessionType_Type(Integer32):
    """Custom type adTAeSCUSecAccountSessionType based on Integer32"""
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
        *(("menu", 1),
          ("tl1", 2),
          ("fcd", 3),
          ("ftp", 4),
          ("invalidSession", 5))
    )


_AdTAeSCUSecAccountSessionType_Type.__name__ = "Integer32"
_AdTAeSCUSecAccountSessionType_Object = MibTableColumn
adTAeSCUSecAccountSessionType = _AdTAeSCUSecAccountSessionType_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 4, 1, 5),
    _AdTAeSCUSecAccountSessionType_Type()
)
adTAeSCUSecAccountSessionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeSCUSecAccountSessionType.setStatus("current")


class _AdTAeSCUSecAccountLoginConnectionSource_Type(DisplayString):
    """Custom type adTAeSCUSecAccountLoginConnectionSource based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_AdTAeSCUSecAccountLoginConnectionSource_Type.__name__ = "DisplayString"
_AdTAeSCUSecAccountLoginConnectionSource_Object = MibTableColumn
adTAeSCUSecAccountLoginConnectionSource = _AdTAeSCUSecAccountLoginConnectionSource_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 4, 1, 6),
    _AdTAeSCUSecAccountLoginConnectionSource_Type()
)
adTAeSCUSecAccountLoginConnectionSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeSCUSecAccountLoginConnectionSource.setStatus("current")


class _AdTAeSCUSecAccountLoginDateTime_Type(DisplayString):
    """Custom type adTAeSCUSecAccountLoginDateTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_AdTAeSCUSecAccountLoginDateTime_Type.__name__ = "DisplayString"
_AdTAeSCUSecAccountLoginDateTime_Object = MibTableColumn
adTAeSCUSecAccountLoginDateTime = _AdTAeSCUSecAccountLoginDateTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 4, 1, 7),
    _AdTAeSCUSecAccountLoginDateTime_Type()
)
adTAeSCUSecAccountLoginDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeSCUSecAccountLoginDateTime.setStatus("current")
_AdTAeSCUSecAccountConnectionPort_Type = Integer32
_AdTAeSCUSecAccountConnectionPort_Object = MibTableColumn
adTAeSCUSecAccountConnectionPort = _AdTAeSCUSecAccountConnectionPort_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 4, 1, 8),
    _AdTAeSCUSecAccountConnectionPort_Type()
)
adTAeSCUSecAccountConnectionPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeSCUSecAccountConnectionPort.setStatus("current")


class _AdTAeSCUSecAccountDisconnectSession_Type(Integer32):
    """Custom type adTAeSCUSecAccountDisconnectSession based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AdTAeSCUSecAccountDisconnectSession_Type.__name__ = "Integer32"
_AdTAeSCUSecAccountDisconnectSession_Object = MibTableColumn
adTAeSCUSecAccountDisconnectSession = _AdTAeSCUSecAccountDisconnectSession_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 4, 1, 9),
    _AdTAeSCUSecAccountDisconnectSession_Type()
)
adTAeSCUSecAccountDisconnectSession.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUSecAccountDisconnectSession.setStatus("current")


class _AdTAeSCUAccountExpirationEnabled_Type(Integer32):
    """Custom type adTAeSCUAccountExpirationEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accountExpirationEnabled", 1),
          ("accountExpirationDisabled", 2))
    )


_AdTAeSCUAccountExpirationEnabled_Type.__name__ = "Integer32"
_AdTAeSCUAccountExpirationEnabled_Object = MibScalar
adTAeSCUAccountExpirationEnabled = _AdTAeSCUAccountExpirationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 5),
    _AdTAeSCUAccountExpirationEnabled_Type()
)
adTAeSCUAccountExpirationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUAccountExpirationEnabled.setStatus("current")


class _AdTAeSCUPasswordAgingEnabled_Type(Integer32):
    """Custom type adTAeSCUPasswordAgingEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("passwordAgingEnabled", 1),
          ("passwordAgingDisabled", 2))
    )


_AdTAeSCUPasswordAgingEnabled_Type.__name__ = "Integer32"
_AdTAeSCUPasswordAgingEnabled_Object = MibScalar
adTAeSCUPasswordAgingEnabled = _AdTAeSCUPasswordAgingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 6),
    _AdTAeSCUPasswordAgingEnabled_Type()
)
adTAeSCUPasswordAgingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUPasswordAgingEnabled.setStatus("current")


class _AdTAeSCUSecuritySnmpAccountMgEnableDisable_Type(DisplayString):
    """Custom type adTAeSCUSecuritySnmpAccountMgEnableDisable based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 255),
    )


_AdTAeSCUSecuritySnmpAccountMgEnableDisable_Type.__name__ = "DisplayString"
_AdTAeSCUSecuritySnmpAccountMgEnableDisable_Object = MibScalar
adTAeSCUSecuritySnmpAccountMgEnableDisable = _AdTAeSCUSecuritySnmpAccountMgEnableDisable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 7),
    _AdTAeSCUSecuritySnmpAccountMgEnableDisable_Type()
)
adTAeSCUSecuritySnmpAccountMgEnableDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUSecuritySnmpAccountMgEnableDisable.setStatus("current")


class _AdTAeSCUSecAccountAuthenticationMethod_Type(Integer32):
    """Custom type adTAeSCUSecAccountAuthenticationMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("rADIUS", 2),
          ("rADIUSorLocal", 3),
          ("tACACS", 4),
          ("tACACSorLocal", 5),
          ("tACACSorRADIUS", 6),
          ("tACACSorRADIUSorLOCAL", 7))
    )


_AdTAeSCUSecAccountAuthenticationMethod_Type.__name__ = "Integer32"
_AdTAeSCUSecAccountAuthenticationMethod_Object = MibScalar
adTAeSCUSecAccountAuthenticationMethod = _AdTAeSCUSecAccountAuthenticationMethod_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 8),
    _AdTAeSCUSecAccountAuthenticationMethod_Type()
)
adTAeSCUSecAccountAuthenticationMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUSecAccountAuthenticationMethod.setStatus("current")
_AdTAeSCUSysRADIUsConfig_ObjectIdentity = ObjectIdentity
adTAeSCUSysRADIUsConfig = _AdTAeSCUSysRADIUsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 9)
)


class _AdTAeScuRADIUSServAuthentication_Type(Integer32):
    """Custom type adTAeScuRADIUSServAuthentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enableRADIUSAuthentication", 1),
          ("enableLocalAccountAuthentication", 2))
    )


_AdTAeScuRADIUSServAuthentication_Type.__name__ = "Integer32"
_AdTAeScuRADIUSServAuthentication_Object = MibScalar
adTAeScuRADIUSServAuthentication = _AdTAeScuRADIUSServAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 9, 2),
    _AdTAeScuRADIUSServAuthentication_Type()
)
adTAeScuRADIUSServAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuRADIUSServAuthentication.setStatus("deprecated")


class _AdTAeScuRadiusTL1Authentication_Type(Integer32):
    """Custom type adTAeScuRadiusTL1Authentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enableRADIUSAuthentication", 1),
          ("enableLocalAccountAuthentication", 2))
    )


_AdTAeScuRadiusTL1Authentication_Type.__name__ = "Integer32"
_AdTAeScuRadiusTL1Authentication_Object = MibScalar
adTAeScuRadiusTL1Authentication = _AdTAeScuRadiusTL1Authentication_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 9, 3),
    _AdTAeScuRadiusTL1Authentication_Type()
)
adTAeScuRadiusTL1Authentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuRadiusTL1Authentication.setStatus("current")


class _AdTAeScuRadiusAccountAccessLevel_Type(Integer32):
    """Custom type adTAeScuRadiusAccountAccessLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("noneRejectLogin", 1),
          ("readOnlyAccess", 2),
          ("readWriteAccess", 3),
          ("testAccess", 4),
          ("configAccess", 5),
          ("adminAccess", 6))
    )


_AdTAeScuRadiusAccountAccessLevel_Type.__name__ = "Integer32"
_AdTAeScuRadiusAccountAccessLevel_Object = MibScalar
adTAeScuRadiusAccountAccessLevel = _AdTAeScuRadiusAccountAccessLevel_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 9, 4),
    _AdTAeScuRadiusAccountAccessLevel_Type()
)
adTAeScuRadiusAccountAccessLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuRadiusAccountAccessLevel.setStatus("current")


class _AdTAeScuRADIUSFallbackMode_Type(Integer32):
    """Custom type adTAeScuRADIUSFallbackMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("retryRADIUSAuthentication", 1),
          ("fallbackToLocalAccountAuthentication", 2))
    )


_AdTAeScuRADIUSFallbackMode_Type.__name__ = "Integer32"
_AdTAeScuRADIUSFallbackMode_Object = MibScalar
adTAeScuRADIUSFallbackMode = _AdTAeScuRADIUSFallbackMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 9, 5),
    _AdTAeScuRADIUSFallbackMode_Type()
)
adTAeScuRADIUSFallbackMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuRADIUSFallbackMode.setStatus("deprecated")
_AdTAeScuRADIUSServerTable_Object = MibTable
adTAeScuRADIUSServerTable = _AdTAeScuRADIUSServerTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 9, 6)
)
if mibBuilder.loadTexts:
    adTAeScuRADIUSServerTable.setStatus("current")
_AdTAeScuRADIUSServerEntry_Object = MibTableRow
adTAeScuRADIUSServerEntry = _AdTAeScuRADIUSServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 9, 6, 1)
)
adTAeScuRADIUSServerEntry.setIndexNames(
    (0, "ADTRAN-TAeSCU-MIB", "adTAeScuRadiusCfgIndex"),
)
if mibBuilder.loadTexts:
    adTAeScuRADIUSServerEntry.setStatus("current")
_AdTAeScuRadiusCfgIndex_Type = Integer32
_AdTAeScuRadiusCfgIndex_Object = MibTableColumn
adTAeScuRadiusCfgIndex = _AdTAeScuRadiusCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 9, 6, 1, 1),
    _AdTAeScuRadiusCfgIndex_Type()
)
adTAeScuRadiusCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeScuRadiusCfgIndex.setStatus("current")
_AdTAeScuRadiusServerAddress_Type = DisplayString
_AdTAeScuRadiusServerAddress_Object = MibTableColumn
adTAeScuRadiusServerAddress = _AdTAeScuRadiusServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 9, 6, 1, 2),
    _AdTAeScuRadiusServerAddress_Type()
)
adTAeScuRadiusServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuRadiusServerAddress.setStatus("deprecated")
_AdTAeScuRadiusServerPortNumber_Type = Integer32
_AdTAeScuRadiusServerPortNumber_Object = MibTableColumn
adTAeScuRadiusServerPortNumber = _AdTAeScuRadiusServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 9, 6, 1, 3),
    _AdTAeScuRadiusServerPortNumber_Type()
)
adTAeScuRadiusServerPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuRadiusServerPortNumber.setStatus("current")
_AdTAeScuRadiusServerSecret_Type = DisplayString
_AdTAeScuRadiusServerSecret_Object = MibTableColumn
adTAeScuRadiusServerSecret = _AdTAeScuRadiusServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 9, 6, 1, 4),
    _AdTAeScuRadiusServerSecret_Type()
)
adTAeScuRadiusServerSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuRadiusServerSecret.setStatus("current")


class _AdTAeScuRADIUSServRetries_Type(Integer32):
    """Custom type adTAeScuRADIUSServRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AdTAeScuRADIUSServRetries_Type.__name__ = "Integer32"
_AdTAeScuRADIUSServRetries_Object = MibTableColumn
adTAeScuRADIUSServRetries = _AdTAeScuRADIUSServRetries_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 9, 6, 1, 5),
    _AdTAeScuRADIUSServRetries_Type()
)
adTAeScuRADIUSServRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuRADIUSServRetries.setStatus("current")


class _AdTAeScuRADIUSServContactTimeOut_Type(Integer32):
    """Custom type adTAeScuRADIUSServContactTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 30000),
    )


_AdTAeScuRADIUSServContactTimeOut_Type.__name__ = "Integer32"
_AdTAeScuRADIUSServContactTimeOut_Object = MibTableColumn
adTAeScuRADIUSServContactTimeOut = _AdTAeScuRADIUSServContactTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 9, 6, 1, 6),
    _AdTAeScuRADIUSServContactTimeOut_Type()
)
adTAeScuRADIUSServContactTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuRADIUSServContactTimeOut.setStatus("current")


class _AdTAeScuRadiusServerSequence_Type(Integer32):
    """Custom type adTAeScuRadiusServerSequence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_AdTAeScuRadiusServerSequence_Type.__name__ = "Integer32"
_AdTAeScuRadiusServerSequence_Object = MibTableColumn
adTAeScuRadiusServerSequence = _AdTAeScuRadiusServerSequence_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 9, 6, 1, 7),
    _AdTAeScuRadiusServerSequence_Type()
)
adTAeScuRadiusServerSequence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuRadiusServerSequence.setStatus("current")
_AdTAeScuRadiusServerName_Type = DisplayString
_AdTAeScuRadiusServerName_Object = MibTableColumn
adTAeScuRadiusServerName = _AdTAeScuRadiusServerName_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 9, 6, 1, 8),
    _AdTAeScuRadiusServerName_Type()
)
adTAeScuRadiusServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuRadiusServerName.setStatus("current")
_AdTAeScuRadiusServerAddressType_Type = InetAddressType
_AdTAeScuRadiusServerAddressType_Object = MibTableColumn
adTAeScuRadiusServerAddressType = _AdTAeScuRadiusServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 9, 6, 1, 9),
    _AdTAeScuRadiusServerAddressType_Type()
)
adTAeScuRadiusServerAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeScuRadiusServerAddressType.setStatus("current")
_AdTAeScuRadiusServerInetAddress_Type = InetAddress
_AdTAeScuRadiusServerInetAddress_Object = MibTableColumn
adTAeScuRadiusServerInetAddress = _AdTAeScuRadiusServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 9, 6, 1, 10),
    _AdTAeScuRadiusServerInetAddress_Type()
)
adTAeScuRadiusServerInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuRadiusServerInetAddress.setStatus("current")
_AdTAeSCUSysPasswordComplexity_ObjectIdentity = ObjectIdentity
adTAeSCUSysPasswordComplexity = _AdTAeSCUSysPasswordComplexity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 10)
)


class _AdTAeSCUSysEnablePswdComplexity_Type(Integer32):
    """Custom type adTAeSCUSysEnablePswdComplexity based on Integer32"""
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


_AdTAeSCUSysEnablePswdComplexity_Type.__name__ = "Integer32"
_AdTAeSCUSysEnablePswdComplexity_Object = MibScalar
adTAeSCUSysEnablePswdComplexity = _AdTAeSCUSysEnablePswdComplexity_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 10, 1),
    _AdTAeSCUSysEnablePswdComplexity_Type()
)
adTAeSCUSysEnablePswdComplexity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUSysEnablePswdComplexity.setStatus("current")


class _AdTAeSCUSysMinPasswordLength_Type(Integer32):
    """Custom type adTAeSCUSysMinPasswordLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 15),
    )


_AdTAeSCUSysMinPasswordLength_Type.__name__ = "Integer32"
_AdTAeSCUSysMinPasswordLength_Object = MibScalar
adTAeSCUSysMinPasswordLength = _AdTAeSCUSysMinPasswordLength_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 10, 2),
    _AdTAeSCUSysMinPasswordLength_Type()
)
adTAeSCUSysMinPasswordLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUSysMinPasswordLength.setStatus("current")


class _AdTAeSCUSysUpperCaseRequired_Type(Integer32):
    """Custom type adTAeSCUSysUpperCaseRequired based on Integer32"""
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


_AdTAeSCUSysUpperCaseRequired_Type.__name__ = "Integer32"
_AdTAeSCUSysUpperCaseRequired_Object = MibScalar
adTAeSCUSysUpperCaseRequired = _AdTAeSCUSysUpperCaseRequired_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 10, 3),
    _AdTAeSCUSysUpperCaseRequired_Type()
)
adTAeSCUSysUpperCaseRequired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUSysUpperCaseRequired.setStatus("current")


class _AdTAeSCUSysLowerCaseRequired_Type(Integer32):
    """Custom type adTAeSCUSysLowerCaseRequired based on Integer32"""
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


_AdTAeSCUSysLowerCaseRequired_Type.__name__ = "Integer32"
_AdTAeSCUSysLowerCaseRequired_Object = MibScalar
adTAeSCUSysLowerCaseRequired = _AdTAeSCUSysLowerCaseRequired_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 10, 4),
    _AdTAeSCUSysLowerCaseRequired_Type()
)
adTAeSCUSysLowerCaseRequired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUSysLowerCaseRequired.setStatus("current")


class _AdTAeSCUSysDigitRequired_Type(Integer32):
    """Custom type adTAeSCUSysDigitRequired based on Integer32"""
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


_AdTAeSCUSysDigitRequired_Type.__name__ = "Integer32"
_AdTAeSCUSysDigitRequired_Object = MibScalar
adTAeSCUSysDigitRequired = _AdTAeSCUSysDigitRequired_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 10, 5),
    _AdTAeSCUSysDigitRequired_Type()
)
adTAeSCUSysDigitRequired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUSysDigitRequired.setStatus("current")


class _AdTAeSCUSysSpecialCharacterRequired_Type(Integer32):
    """Custom type adTAeSCUSysSpecialCharacterRequired based on Integer32"""
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


_AdTAeSCUSysSpecialCharacterRequired_Type.__name__ = "Integer32"
_AdTAeSCUSysSpecialCharacterRequired_Object = MibScalar
adTAeSCUSysSpecialCharacterRequired = _AdTAeSCUSysSpecialCharacterRequired_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 10, 6),
    _AdTAeSCUSysSpecialCharacterRequired_Type()
)
adTAeSCUSysSpecialCharacterRequired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUSysSpecialCharacterRequired.setStatus("current")


class _AdTAeSCUSysCaseSensitivePassword_Type(Integer32):
    """Custom type adTAeSCUSysCaseSensitivePassword based on Integer32"""
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


_AdTAeSCUSysCaseSensitivePassword_Type.__name__ = "Integer32"
_AdTAeSCUSysCaseSensitivePassword_Object = MibScalar
adTAeSCUSysCaseSensitivePassword = _AdTAeSCUSysCaseSensitivePassword_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 10, 7),
    _AdTAeSCUSysCaseSensitivePassword_Type()
)
adTAeSCUSysCaseSensitivePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUSysCaseSensitivePassword.setStatus("current")


class _AdTAeSCUSysNullPasswordAccepted_Type(Integer32):
    """Custom type adTAeSCUSysNullPasswordAccepted based on Integer32"""
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


_AdTAeSCUSysNullPasswordAccepted_Type.__name__ = "Integer32"
_AdTAeSCUSysNullPasswordAccepted_Object = MibScalar
adTAeSCUSysNullPasswordAccepted = _AdTAeSCUSysNullPasswordAccepted_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 10, 8),
    _AdTAeSCUSysNullPasswordAccepted_Type()
)
adTAeSCUSysNullPasswordAccepted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUSysNullPasswordAccepted.setStatus("deprecated")


class _AdTAeSCUSecPasswordStartEndDigitCheck_Type(Integer32):
    """Custom type adTAeSCUSecPasswordStartEndDigitCheck based on Integer32"""
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


_AdTAeSCUSecPasswordStartEndDigitCheck_Type.__name__ = "Integer32"
_AdTAeSCUSecPasswordStartEndDigitCheck_Object = MibScalar
adTAeSCUSecPasswordStartEndDigitCheck = _AdTAeSCUSecPasswordStartEndDigitCheck_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 10, 10),
    _AdTAeSCUSecPasswordStartEndDigitCheck_Type()
)
adTAeSCUSecPasswordStartEndDigitCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUSecPasswordStartEndDigitCheck.setStatus("current")


class _AdTAeSCUSecLastSixPasswordCheck_Type(Integer32):
    """Custom type adTAeSCUSecLastSixPasswordCheck based on Integer32"""
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


_AdTAeSCUSecLastSixPasswordCheck_Type.__name__ = "Integer32"
_AdTAeSCUSecLastSixPasswordCheck_Object = MibScalar
adTAeSCUSecLastSixPasswordCheck = _AdTAeSCUSecLastSixPasswordCheck_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 10, 12),
    _AdTAeSCUSecLastSixPasswordCheck_Type()
)
adTAeSCUSecLastSixPasswordCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUSecLastSixPasswordCheck.setStatus("current")
_AdTAeScuAccLockOutSettings_ObjectIdentity = ObjectIdentity
adTAeScuAccLockOutSettings = _AdTAeScuAccLockOutSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 12)
)


class _AdTAeScuEnableAccLoginFailureLockOut_Type(Integer32):
    """Custom type adTAeScuEnableAccLoginFailureLockOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AdTAeScuEnableAccLoginFailureLockOut_Type.__name__ = "Integer32"
_AdTAeScuEnableAccLoginFailureLockOut_Object = MibScalar
adTAeScuEnableAccLoginFailureLockOut = _AdTAeScuEnableAccLoginFailureLockOut_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 12, 1),
    _AdTAeScuEnableAccLoginFailureLockOut_Type()
)
adTAeScuEnableAccLoginFailureLockOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuEnableAccLoginFailureLockOut.setStatus("current")


class _AdTAeScuEnableLockOutAlarm_Type(Integer32):
    """Custom type adTAeScuEnableLockOutAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AdTAeScuEnableLockOutAlarm_Type.__name__ = "Integer32"
_AdTAeScuEnableLockOutAlarm_Object = MibScalar
adTAeScuEnableLockOutAlarm = _AdTAeScuEnableLockOutAlarm_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 12, 2),
    _AdTAeScuEnableLockOutAlarm_Type()
)
adTAeScuEnableLockOutAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuEnableLockOutAlarm.setStatus("current")


class _AdTAeScuEnableIndefLockOut_Type(Integer32):
    """Custom type adTAeScuEnableIndefLockOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AdTAeScuEnableIndefLockOut_Type.__name__ = "Integer32"
_AdTAeScuEnableIndefLockOut_Object = MibScalar
adTAeScuEnableIndefLockOut = _AdTAeScuEnableIndefLockOut_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 12, 3),
    _AdTAeScuEnableIndefLockOut_Type()
)
adTAeScuEnableIndefLockOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuEnableIndefLockOut.setStatus("current")


class _AdTAeScuNumLockOutLoginAttempts_Type(Integer32):
    """Custom type adTAeScuNumLockOutLoginAttempts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 15),
    )


_AdTAeScuNumLockOutLoginAttempts_Type.__name__ = "Integer32"
_AdTAeScuNumLockOutLoginAttempts_Object = MibScalar
adTAeScuNumLockOutLoginAttempts = _AdTAeScuNumLockOutLoginAttempts_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 12, 4),
    _AdTAeScuNumLockOutLoginAttempts_Type()
)
adTAeScuNumLockOutLoginAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuNumLockOutLoginAttempts.setStatus("current")


class _AdTAeScuLockOutDuration_Type(Integer32):
    """Custom type adTAeScuLockOutDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_AdTAeScuLockOutDuration_Type.__name__ = "Integer32"
_AdTAeScuLockOutDuration_Object = MibScalar
adTAeScuLockOutDuration = _AdTAeScuLockOutDuration_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 12, 5),
    _AdTAeScuLockOutDuration_Type()
)
adTAeScuLockOutDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuLockOutDuration.setStatus("current")
_AdTAeTrustedClientConfig_ObjectIdentity = ObjectIdentity
adTAeTrustedClientConfig = _AdTAeTrustedClientConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 13)
)


class _AdTAeTrustedIPClientAccessControl_Type(Integer32):
    """Custom type adTAeTrustedIPClientAccessControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enableTrustedClientAccessControl", 1),
          ("disableTrustedClientAccessControl", 2))
    )


_AdTAeTrustedIPClientAccessControl_Type.__name__ = "Integer32"
_AdTAeTrustedIPClientAccessControl_Object = MibScalar
adTAeTrustedIPClientAccessControl = _AdTAeTrustedIPClientAccessControl_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 13, 3),
    _AdTAeTrustedIPClientAccessControl_Type()
)
adTAeTrustedIPClientAccessControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeTrustedIPClientAccessControl.setStatus("current")


class _AdTAeTrustedIPClientAccessName_Type(DisplayString):
    """Custom type adTAeTrustedIPClientAccessName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_AdTAeTrustedIPClientAccessName_Type.__name__ = "DisplayString"
_AdTAeTrustedIPClientAccessName_Object = MibScalar
adTAeTrustedIPClientAccessName = _AdTAeTrustedIPClientAccessName_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 13, 4),
    _AdTAeTrustedIPClientAccessName_Type()
)
adTAeTrustedIPClientAccessName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeTrustedIPClientAccessName.setStatus("current")
_AdTAeTrustedIPClientTable_Object = MibTable
adTAeTrustedIPClientTable = _AdTAeTrustedIPClientTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 13, 6)
)
if mibBuilder.loadTexts:
    adTAeTrustedIPClientTable.setStatus("current")
_AdTAeTrustedIPClientEntry_Object = MibTableRow
adTAeTrustedIPClientEntry = _AdTAeTrustedIPClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 13, 6, 1)
)
adTAeTrustedIPClientEntry.setIndexNames(
    (0, "ADTRAN-TAeSCU-MIB", "adTAeTrustedIPAddress"),
    (0, "ADTRAN-TAeSCU-MIB", "adTAeTrustedIPNetworkBits"),
)
if mibBuilder.loadTexts:
    adTAeTrustedIPClientEntry.setStatus("current")


class _AdTAeTrustedClientStatus_Type(Integer32):
    """Custom type adTAeTrustedClientStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createTrustedClient", 2),
          ("deleteTrustedClient", 3))
    )


_AdTAeTrustedClientStatus_Type.__name__ = "Integer32"
_AdTAeTrustedClientStatus_Object = MibTableColumn
adTAeTrustedClientStatus = _AdTAeTrustedClientStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 13, 6, 1, 1),
    _AdTAeTrustedClientStatus_Type()
)
adTAeTrustedClientStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeTrustedClientStatus.setStatus("current")
_AdTAeTrustedIPAddress_Type = IpAddress
_AdTAeTrustedIPAddress_Object = MibTableColumn
adTAeTrustedIPAddress = _AdTAeTrustedIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 13, 6, 1, 2),
    _AdTAeTrustedIPAddress_Type()
)
adTAeTrustedIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeTrustedIPAddress.setStatus("current")


class _AdTAeTrustedIPNetworkBits_Type(Integer32):
    """Custom type adTAeTrustedIPNetworkBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AdTAeTrustedIPNetworkBits_Type.__name__ = "Integer32"
_AdTAeTrustedIPNetworkBits_Object = MibTableColumn
adTAeTrustedIPNetworkBits = _AdTAeTrustedIPNetworkBits_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 13, 6, 1, 3),
    _AdTAeTrustedIPNetworkBits_Type()
)
adTAeTrustedIPNetworkBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeTrustedIPNetworkBits.setStatus("current")


class _AdTAeTrustedClientResource_Type(Integer32):
    """Custom type adTAeTrustedClientResource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("allPorts", 1),
          ("snmpPorts", 2),
          ("menuPorts", 3),
          ("tL1Ports", 4),
          ("snmpMenuPorts", 5),
          ("snmpTL1Ports", 6),
          ("menuTL1Ports", 7))
    )


_AdTAeTrustedClientResource_Type.__name__ = "Integer32"
_AdTAeTrustedClientResource_Object = MibTableColumn
adTAeTrustedClientResource = _AdTAeTrustedClientResource_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 13, 6, 1, 4),
    _AdTAeTrustedClientResource_Type()
)
adTAeTrustedClientResource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeTrustedClientResource.setStatus("current")
_AdTAeTrustedInetClientTable_Object = MibTable
adTAeTrustedInetClientTable = _AdTAeTrustedInetClientTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 13, 8)
)
if mibBuilder.loadTexts:
    adTAeTrustedInetClientTable.setStatus("current")
_AdTAeTrustedInetClientEntry_Object = MibTableRow
adTAeTrustedInetClientEntry = _AdTAeTrustedInetClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 13, 8, 1)
)
adTAeTrustedInetClientEntry.setIndexNames(
    (0, "ADTRAN-TAeSCU-MIB", "adTAeTrustedInetAddressType"),
    (0, "ADTRAN-TAeSCU-MIB", "adTAeTrustedInetNetworkBits"),
    (0, "ADTRAN-TAeSCU-MIB", "adTAeTrustedInetAddress"),
)
if mibBuilder.loadTexts:
    adTAeTrustedInetClientEntry.setStatus("current")


class _AdTAeTrustedInetClientStatus_Type(Integer32):
    """Custom type adTAeTrustedInetClientStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createTrustedClient", 2),
          ("deleteTrustedClient", 3))
    )


_AdTAeTrustedInetClientStatus_Type.__name__ = "Integer32"
_AdTAeTrustedInetClientStatus_Object = MibTableColumn
adTAeTrustedInetClientStatus = _AdTAeTrustedInetClientStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 13, 8, 1, 1),
    _AdTAeTrustedInetClientStatus_Type()
)
adTAeTrustedInetClientStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeTrustedInetClientStatus.setStatus("current")
_AdTAeTrustedInetAddressType_Type = InetAddressType
_AdTAeTrustedInetAddressType_Object = MibTableColumn
adTAeTrustedInetAddressType = _AdTAeTrustedInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 13, 8, 1, 2),
    _AdTAeTrustedInetAddressType_Type()
)
adTAeTrustedInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeTrustedInetAddressType.setStatus("current")


class _AdTAeTrustedInetNetworkBits_Type(Integer32):
    """Custom type adTAeTrustedInetNetworkBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_AdTAeTrustedInetNetworkBits_Type.__name__ = "Integer32"
_AdTAeTrustedInetNetworkBits_Object = MibTableColumn
adTAeTrustedInetNetworkBits = _AdTAeTrustedInetNetworkBits_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 13, 8, 1, 3),
    _AdTAeTrustedInetNetworkBits_Type()
)
adTAeTrustedInetNetworkBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeTrustedInetNetworkBits.setStatus("current")
_AdTAeTrustedInetAddress_Type = InetAddress
_AdTAeTrustedInetAddress_Object = MibTableColumn
adTAeTrustedInetAddress = _AdTAeTrustedInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 13, 8, 1, 4),
    _AdTAeTrustedInetAddress_Type()
)
adTAeTrustedInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeTrustedInetAddress.setStatus("current")


class _AdTAeTrustedInetClientResource_Type(Integer32):
    """Custom type adTAeTrustedInetClientResource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("allPorts", 1),
          ("snmpPorts", 2),
          ("tL1Ports", 3),
          ("snmpTL1Ports", 4))
    )


_AdTAeTrustedInetClientResource_Type.__name__ = "Integer32"
_AdTAeTrustedInetClientResource_Object = MibTableColumn
adTAeTrustedInetClientResource = _AdTAeTrustedInetClientResource_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 13, 8, 1, 5),
    _AdTAeTrustedInetClientResource_Type()
)
adTAeTrustedInetClientResource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeTrustedInetClientResource.setStatus("current")
_AdTAeSCUSysAdvisoryConfig_ObjectIdentity = ObjectIdentity
adTAeSCUSysAdvisoryConfig = _AdTAeSCUSysAdvisoryConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 20)
)


class _AdTAeScuEnableMenuAdvisoryWarningMsg_Type(Integer32):
    """Custom type adTAeScuEnableMenuAdvisoryWarningMsg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enableAdvisoryWarningMsg", 1),
          ("disableAdvisoryWarniningMsg", 2))
    )


_AdTAeScuEnableMenuAdvisoryWarningMsg_Type.__name__ = "Integer32"
_AdTAeScuEnableMenuAdvisoryWarningMsg_Object = MibScalar
adTAeScuEnableMenuAdvisoryWarningMsg = _AdTAeScuEnableMenuAdvisoryWarningMsg_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 20, 1),
    _AdTAeScuEnableMenuAdvisoryWarningMsg_Type()
)
adTAeScuEnableMenuAdvisoryWarningMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuEnableMenuAdvisoryWarningMsg.setStatus("current")


class _AdTAeScuEnableTL1AdvisoryWarningMsg_Type(Integer32):
    """Custom type adTAeScuEnableTL1AdvisoryWarningMsg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enableAdvisoryWarningMsg", 1),
          ("disableAdvisoryWarningMsg", 2))
    )


_AdTAeScuEnableTL1AdvisoryWarningMsg_Type.__name__ = "Integer32"
_AdTAeScuEnableTL1AdvisoryWarningMsg_Object = MibScalar
adTAeScuEnableTL1AdvisoryWarningMsg = _AdTAeScuEnableTL1AdvisoryWarningMsg_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 20, 2),
    _AdTAeScuEnableTL1AdvisoryWarningMsg_Type()
)
adTAeScuEnableTL1AdvisoryWarningMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuEnableTL1AdvisoryWarningMsg.setStatus("current")


class _AdTAeScuSysSavedTextJustification_Type(Integer32):
    """Custom type adTAeScuSysSavedTextJustification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("leftJustification", 1),
          ("rightJustification", 2),
          ("centerJustification", 3))
    )


_AdTAeScuSysSavedTextJustification_Type.__name__ = "Integer32"
_AdTAeScuSysSavedTextJustification_Object = MibScalar
adTAeScuSysSavedTextJustification = _AdTAeScuSysSavedTextJustification_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 20, 3),
    _AdTAeScuSysSavedTextJustification_Type()
)
adTAeScuSysSavedTextJustification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeScuSysSavedTextJustification.setStatus("current")
_AdTAeScuSavedAdvisoryTable_Object = MibTable
adTAeScuSavedAdvisoryTable = _AdTAeScuSavedAdvisoryTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 20, 6)
)
if mibBuilder.loadTexts:
    adTAeScuSavedAdvisoryTable.setStatus("current")
_AdTAeScuSavedAdvisoryEntry_Object = MibTableRow
adTAeScuSavedAdvisoryEntry = _AdTAeScuSavedAdvisoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 20, 6, 1)
)
adTAeScuSavedAdvisoryEntry.setIndexNames(
    (0, "ADTRAN-TAeSCU-MIB", "adTAeScuAdvisoryLineIndex"),
)
if mibBuilder.loadTexts:
    adTAeScuSavedAdvisoryEntry.setStatus("current")


class _AdTAeScuAdvisoryLineIndex_Type(Integer32):
    """Custom type adTAeScuAdvisoryLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_AdTAeScuAdvisoryLineIndex_Type.__name__ = "Integer32"
_AdTAeScuAdvisoryLineIndex_Object = MibTableColumn
adTAeScuAdvisoryLineIndex = _AdTAeScuAdvisoryLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 20, 6, 1, 1),
    _AdTAeScuAdvisoryLineIndex_Type()
)
adTAeScuAdvisoryLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeScuAdvisoryLineIndex.setStatus("current")
_AdTAeScuSavedAdvisoryWarning_Type = DisplayString
_AdTAeScuSavedAdvisoryWarning_Object = MibTableColumn
adTAeScuSavedAdvisoryWarning = _AdTAeScuSavedAdvisoryWarning_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 20, 6, 1, 2),
    _AdTAeScuSavedAdvisoryWarning_Type()
)
adTAeScuSavedAdvisoryWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeScuSavedAdvisoryWarning.setStatus("current")


class _AdTAeScuSysSaveOrResetEditAdvisoryWarning_Type(Integer32):
    """Custom type adTAeScuSysSaveOrResetEditAdvisoryWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              999)
        )
    )
    namedValues = NamedValues(
        *(("saveAdvisoryWarningChanges", 1),
          ("resetAdvisoryWarning", 2),
          ("defaultGetValue", 999))
    )


_AdTAeScuSysSaveOrResetEditAdvisoryWarning_Type.__name__ = "Integer32"
_AdTAeScuSysSaveOrResetEditAdvisoryWarning_Object = MibScalar
adTAeScuSysSaveOrResetEditAdvisoryWarning = _AdTAeScuSysSaveOrResetEditAdvisoryWarning_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 20, 10),
    _AdTAeScuSysSaveOrResetEditAdvisoryWarning_Type()
)
adTAeScuSysSaveOrResetEditAdvisoryWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuSysSaveOrResetEditAdvisoryWarning.setStatus("current")


class _AdTAeScuSysEditTextJustification_Type(Integer32):
    """Custom type adTAeScuSysEditTextJustification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("leftJustification", 1),
          ("rightJustification", 2),
          ("centerJustification", 3))
    )


_AdTAeScuSysEditTextJustification_Type.__name__ = "Integer32"
_AdTAeScuSysEditTextJustification_Object = MibScalar
adTAeScuSysEditTextJustification = _AdTAeScuSysEditTextJustification_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 20, 11),
    _AdTAeScuSysEditTextJustification_Type()
)
adTAeScuSysEditTextJustification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuSysEditTextJustification.setStatus("current")
_AdTAeScuEditedAdvisoryTable_Object = MibTable
adTAeScuEditedAdvisoryTable = _AdTAeScuEditedAdvisoryTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 20, 15)
)
if mibBuilder.loadTexts:
    adTAeScuEditedAdvisoryTable.setStatus("current")
_AdTAeScuEditedAdvisoryEntry_Object = MibTableRow
adTAeScuEditedAdvisoryEntry = _AdTAeScuEditedAdvisoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 20, 15, 1)
)
adTAeScuEditedAdvisoryEntry.setIndexNames(
    (0, "ADTRAN-TAeSCU-MIB", "adTAeScuAdvisoryLineIndex"),
)
if mibBuilder.loadTexts:
    adTAeScuEditedAdvisoryEntry.setStatus("current")
_AdTAeScuEditedAdvisoryWarning_Type = DisplayString
_AdTAeScuEditedAdvisoryWarning_Object = MibTableColumn
adTAeScuEditedAdvisoryWarning = _AdTAeScuEditedAdvisoryWarning_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 20, 15, 1, 2),
    _AdTAeScuEditedAdvisoryWarning_Type()
)
adTAeScuEditedAdvisoryWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuEditedAdvisoryWarning.setStatus("current")
_AdTAeSCUSysBulkDataExportServerConfig_ObjectIdentity = ObjectIdentity
adTAeSCUSysBulkDataExportServerConfig = _AdTAeSCUSysBulkDataExportServerConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 21)
)
_AdTAeSCUSysBulkDataExportHost_Type = IpAddress
_AdTAeSCUSysBulkDataExportHost_Object = MibScalar
adTAeSCUSysBulkDataExportHost = _AdTAeSCUSysBulkDataExportHost_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 21, 1),
    _AdTAeSCUSysBulkDataExportHost_Type()
)
adTAeSCUSysBulkDataExportHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUSysBulkDataExportHost.setStatus("current")
_AdTAeSCUSysBulkDataExportUserName_Type = DisplayString
_AdTAeSCUSysBulkDataExportUserName_Object = MibScalar
adTAeSCUSysBulkDataExportUserName = _AdTAeSCUSysBulkDataExportUserName_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 21, 2),
    _AdTAeSCUSysBulkDataExportUserName_Type()
)
adTAeSCUSysBulkDataExportUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUSysBulkDataExportUserName.setStatus("current")
_AdTAeSCUSysBulkDataExportPassword_Type = DisplayString
_AdTAeSCUSysBulkDataExportPassword_Object = MibScalar
adTAeSCUSysBulkDataExportPassword = _AdTAeSCUSysBulkDataExportPassword_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 21, 3),
    _AdTAeSCUSysBulkDataExportPassword_Type()
)
adTAeSCUSysBulkDataExportPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUSysBulkDataExportPassword.setStatus("current")


class _AdTAeSCUSysBulkDataExportProtocol_Type(Integer32):
    """Custom type adTAeSCUSysBulkDataExportProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("tftp", 1),
          ("ftp", 3),
          ("sftp", 4))
    )


_AdTAeSCUSysBulkDataExportProtocol_Type.__name__ = "Integer32"
_AdTAeSCUSysBulkDataExportProtocol_Object = MibScalar
adTAeSCUSysBulkDataExportProtocol = _AdTAeSCUSysBulkDataExportProtocol_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 21, 4),
    _AdTAeSCUSysBulkDataExportProtocol_Type()
)
adTAeSCUSysBulkDataExportProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUSysBulkDataExportProtocol.setStatus("current")
_AdTAeSCUSysBulkDataExportPort_Type = Integer32
_AdTAeSCUSysBulkDataExportPort_Object = MibScalar
adTAeSCUSysBulkDataExportPort = _AdTAeSCUSysBulkDataExportPort_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 21, 5),
    _AdTAeSCUSysBulkDataExportPort_Type()
)
adTAeSCUSysBulkDataExportPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUSysBulkDataExportPort.setStatus("current")
_AdTAeSCUSysBulkDataExportPath_Type = DisplayString
_AdTAeSCUSysBulkDataExportPath_Object = MibScalar
adTAeSCUSysBulkDataExportPath = _AdTAeSCUSysBulkDataExportPath_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 21, 6),
    _AdTAeSCUSysBulkDataExportPath_Type()
)
adTAeSCUSysBulkDataExportPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUSysBulkDataExportPath.setStatus("current")
_AdTAeSCUSecLoginStatTable_Object = MibTable
adTAeSCUSecLoginStatTable = _AdTAeSCUSecLoginStatTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 25)
)
if mibBuilder.loadTexts:
    adTAeSCUSecLoginStatTable.setStatus("current")
_AdTAeSCUSecLoginStatEntry_Object = MibTableRow
adTAeSCUSecLoginStatEntry = _AdTAeSCUSecLoginStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 25, 1)
)
adTAeSCUSecLoginStatEntry.setIndexNames(
    (0, "ADTRAN-TAeSCU-MIB", "adTAeSCUSecAccountIndex"),
)
if mibBuilder.loadTexts:
    adTAeSCUSecLoginStatEntry.setStatus("current")


class _AdTAeSCUSecLoginStatUserID_Type(DisplayString):
    """Custom type adTAeSCUSecLoginStatUserID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AdTAeSCUSecLoginStatUserID_Type.__name__ = "DisplayString"
_AdTAeSCUSecLoginStatUserID_Object = MibTableColumn
adTAeSCUSecLoginStatUserID = _AdTAeSCUSecLoginStatUserID_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 25, 1, 3),
    _AdTAeSCUSecLoginStatUserID_Type()
)
adTAeSCUSecLoginStatUserID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeSCUSecLoginStatUserID.setStatus("current")
_AdTAeSCUSecNumberOfLogins_Type = Integer32
_AdTAeSCUSecNumberOfLogins_Object = MibTableColumn
adTAeSCUSecNumberOfLogins = _AdTAeSCUSecNumberOfLogins_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 25, 1, 5),
    _AdTAeSCUSecNumberOfLogins_Type()
)
adTAeSCUSecNumberOfLogins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeSCUSecNumberOfLogins.setStatus("current")
_AdTAeSCUSecTotalNumLoginFailures_Type = Integer32
_AdTAeSCUSecTotalNumLoginFailures_Object = MibTableColumn
adTAeSCUSecTotalNumLoginFailures = _AdTAeSCUSecTotalNumLoginFailures_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 25, 1, 7),
    _AdTAeSCUSecTotalNumLoginFailures_Type()
)
adTAeSCUSecTotalNumLoginFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeSCUSecTotalNumLoginFailures.setStatus("current")
_AdTAeSCUSecNumFailuresSinceLastLogin_Type = Integer32
_AdTAeSCUSecNumFailuresSinceLastLogin_Object = MibTableColumn
adTAeSCUSecNumFailuresSinceLastLogin = _AdTAeSCUSecNumFailuresSinceLastLogin_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 25, 1, 9),
    _AdTAeSCUSecNumFailuresSinceLastLogin_Type()
)
adTAeSCUSecNumFailuresSinceLastLogin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeSCUSecNumFailuresSinceLastLogin.setStatus("current")


class _AdTAeSCUSecLastLoginDateTime_Type(DisplayString):
    """Custom type adTAeSCUSecLastLoginDateTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_AdTAeSCUSecLastLoginDateTime_Type.__name__ = "DisplayString"
_AdTAeSCUSecLastLoginDateTime_Object = MibTableColumn
adTAeSCUSecLastLoginDateTime = _AdTAeSCUSecLastLoginDateTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 25, 1, 13),
    _AdTAeSCUSecLastLoginDateTime_Type()
)
adTAeSCUSecLastLoginDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeSCUSecLastLoginDateTime.setStatus("current")


class _AdTAeSCUSecLastConnectionType_Type(Integer32):
    """Custom type adTAeSCUSecLastConnectionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("craftConnection", 1),
          ("adminConnection", 2),
          ("ntwkmgmtConnection", 3),
          ("ipConnection", 4),
          ("x25Connection", 5),
          ("rS485Connection", 6),
          ("dccConnection", 7),
          ("fCDConnection", 8),
          ("snmpConnection", 9),
          ("unknown1", 10),
          ("unknown2", 11),
          ("unknown3", 12))
    )


_AdTAeSCUSecLastConnectionType_Type.__name__ = "Integer32"
_AdTAeSCUSecLastConnectionType_Object = MibTableColumn
adTAeSCUSecLastConnectionType = _AdTAeSCUSecLastConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 25, 1, 14),
    _AdTAeSCUSecLastConnectionType_Type()
)
adTAeSCUSecLastConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeSCUSecLastConnectionType.setStatus("current")


class _AdTAeSCUSecLastSessionType_Type(Integer32):
    """Custom type adTAeSCUSecLastSessionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("menuSessionType", 1),
          ("tL1SessionType", 2),
          ("fcdSessionType", 3),
          ("ftpSessionType", 4),
          ("fsSessionType", 5),
          ("webSessionType", 6),
          ("cliSessionType", 7),
          ("unknown1", 8),
          ("unknown2", 9),
          ("unknown3", 10))
    )


_AdTAeSCUSecLastSessionType_Type.__name__ = "Integer32"
_AdTAeSCUSecLastSessionType_Object = MibTableColumn
adTAeSCUSecLastSessionType = _AdTAeSCUSecLastSessionType_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 25, 1, 15),
    _AdTAeSCUSecLastSessionType_Type()
)
adTAeSCUSecLastSessionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeSCUSecLastSessionType.setStatus("current")
_AdTAeSCUSecLastIPAddress_Type = IpAddress
_AdTAeSCUSecLastIPAddress_Object = MibTableColumn
adTAeSCUSecLastIPAddress = _AdTAeSCUSecLastIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 25, 1, 16),
    _AdTAeSCUSecLastIPAddress_Type()
)
adTAeSCUSecLastIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeSCUSecLastIPAddress.setStatus("current")
_AdTAeSCUSecAdvancedLoginOptions_ObjectIdentity = ObjectIdentity
adTAeSCUSecAdvancedLoginOptions = _AdTAeSCUSecAdvancedLoginOptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 26)
)


class _AdTAeSCUSecChallengeKey_Type(Integer32):
    """Custom type adTAeSCUSecChallengeKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AdTAeSCUSecChallengeKey_Type.__name__ = "Integer32"
_AdTAeSCUSecChallengeKey_Object = MibScalar
adTAeSCUSecChallengeKey = _AdTAeSCUSecChallengeKey_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 26, 1),
    _AdTAeSCUSecChallengeKey_Type()
)
adTAeSCUSecChallengeKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUSecChallengeKey.setStatus("current")


class _AdTAeSCUSecMultiLoginAcct_Type(Integer32):
    """Custom type adTAeSCUSecMultiLoginAcct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AdTAeSCUSecMultiLoginAcct_Type.__name__ = "Integer32"
_AdTAeSCUSecMultiLoginAcct_Object = MibScalar
adTAeSCUSecMultiLoginAcct = _AdTAeSCUSecMultiLoginAcct_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 26, 2),
    _AdTAeSCUSecMultiLoginAcct_Type()
)
adTAeSCUSecMultiLoginAcct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUSecMultiLoginAcct.setStatus("current")


class _AdTAeSCUSecRemoteMenuAccessRequired_Type(Integer32):
    """Custom type adTAeSCUSecRemoteMenuAccessRequired based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AdTAeSCUSecRemoteMenuAccessRequired_Type.__name__ = "Integer32"
_AdTAeSCUSecRemoteMenuAccessRequired_Object = MibScalar
adTAeSCUSecRemoteMenuAccessRequired = _AdTAeSCUSecRemoteMenuAccessRequired_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 26, 3),
    _AdTAeSCUSecRemoteMenuAccessRequired_Type()
)
adTAeSCUSecRemoteMenuAccessRequired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUSecRemoteMenuAccessRequired.setStatus("current")
_AdTAeSCUSysTACACSPlusConfig_ObjectIdentity = ObjectIdentity
adTAeSCUSysTACACSPlusConfig = _AdTAeSCUSysTACACSPlusConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 30)
)


class _AdTAeScuTACACSPlusTL1Authentication_Type(Integer32):
    """Custom type adTAeScuTACACSPlusTL1Authentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enableTACACSAuthentication", 1),
          ("disableTACACSAuthentication", 2))
    )


_AdTAeScuTACACSPlusTL1Authentication_Type.__name__ = "Integer32"
_AdTAeScuTACACSPlusTL1Authentication_Object = MibScalar
adTAeScuTACACSPlusTL1Authentication = _AdTAeScuTACACSPlusTL1Authentication_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 30, 3),
    _AdTAeScuTACACSPlusTL1Authentication_Type()
)
adTAeScuTACACSPlusTL1Authentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuTACACSPlusTL1Authentication.setStatus("current")
_AdTAeScuTACACSPlusServerTable_Object = MibTable
adTAeScuTACACSPlusServerTable = _AdTAeScuTACACSPlusServerTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 30, 6)
)
if mibBuilder.loadTexts:
    adTAeScuTACACSPlusServerTable.setStatus("current")
_AdTAeScuTACACSPlusServerEntry_Object = MibTableRow
adTAeScuTACACSPlusServerEntry = _AdTAeScuTACACSPlusServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 30, 6, 1)
)
adTAeScuTACACSPlusServerEntry.setIndexNames(
    (0, "ADTRAN-TAeSCU-MIB", "adTAeScuTACACSPlusCfgIndex"),
)
if mibBuilder.loadTexts:
    adTAeScuTACACSPlusServerEntry.setStatus("current")
_AdTAeScuTACACSPlusCfgIndex_Type = Integer32
_AdTAeScuTACACSPlusCfgIndex_Object = MibTableColumn
adTAeScuTACACSPlusCfgIndex = _AdTAeScuTACACSPlusCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 30, 6, 1, 1),
    _AdTAeScuTACACSPlusCfgIndex_Type()
)
adTAeScuTACACSPlusCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeScuTACACSPlusCfgIndex.setStatus("current")
_AdTAeScuTACACSPlusServerAddress_Type = DisplayString
_AdTAeScuTACACSPlusServerAddress_Object = MibTableColumn
adTAeScuTACACSPlusServerAddress = _AdTAeScuTACACSPlusServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 30, 6, 1, 2),
    _AdTAeScuTACACSPlusServerAddress_Type()
)
adTAeScuTACACSPlusServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuTACACSPlusServerAddress.setStatus("deprecated")
_AdTAeScuTACACSPlusServerName_Type = DisplayString
_AdTAeScuTACACSPlusServerName_Object = MibTableColumn
adTAeScuTACACSPlusServerName = _AdTAeScuTACACSPlusServerName_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 30, 6, 1, 3),
    _AdTAeScuTACACSPlusServerName_Type()
)
adTAeScuTACACSPlusServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuTACACSPlusServerName.setStatus("current")
_AdTAeScuTACACSPlusServerSecret_Type = DisplayString
_AdTAeScuTACACSPlusServerSecret_Object = MibTableColumn
adTAeScuTACACSPlusServerSecret = _AdTAeScuTACACSPlusServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 30, 6, 1, 4),
    _AdTAeScuTACACSPlusServerSecret_Type()
)
adTAeScuTACACSPlusServerSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuTACACSPlusServerSecret.setStatus("current")


class _AdTAeScuTACACSPlusServerSequence_Type(Integer32):
    """Custom type adTAeScuTACACSPlusServerSequence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_AdTAeScuTACACSPlusServerSequence_Type.__name__ = "Integer32"
_AdTAeScuTACACSPlusServerSequence_Object = MibTableColumn
adTAeScuTACACSPlusServerSequence = _AdTAeScuTACACSPlusServerSequence_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 30, 6, 1, 5),
    _AdTAeScuTACACSPlusServerSequence_Type()
)
adTAeScuTACACSPlusServerSequence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuTACACSPlusServerSequence.setStatus("current")


class _AdTAeScuTACACSPlusServContactTimeOut_Type(Integer32):
    """Custom type adTAeScuTACACSPlusServContactTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 30000),
    )


_AdTAeScuTACACSPlusServContactTimeOut_Type.__name__ = "Integer32"
_AdTAeScuTACACSPlusServContactTimeOut_Object = MibTableColumn
adTAeScuTACACSPlusServContactTimeOut = _AdTAeScuTACACSPlusServContactTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 30, 6, 1, 6),
    _AdTAeScuTACACSPlusServContactTimeOut_Type()
)
adTAeScuTACACSPlusServContactTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuTACACSPlusServContactTimeOut.setStatus("current")


class _AdTAeScuTACACSPlusServerPort_Type(Integer32):
    """Custom type adTAeScuTACACSPlusServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AdTAeScuTACACSPlusServerPort_Type.__name__ = "Integer32"
_AdTAeScuTACACSPlusServerPort_Object = MibTableColumn
adTAeScuTACACSPlusServerPort = _AdTAeScuTACACSPlusServerPort_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 30, 6, 1, 8),
    _AdTAeScuTACACSPlusServerPort_Type()
)
adTAeScuTACACSPlusServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuTACACSPlusServerPort.setStatus("current")
_AdTAeScuTACACSPlusServerAddressType_Type = InetAddressType
_AdTAeScuTACACSPlusServerAddressType_Object = MibTableColumn
adTAeScuTACACSPlusServerAddressType = _AdTAeScuTACACSPlusServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 30, 6, 1, 9),
    _AdTAeScuTACACSPlusServerAddressType_Type()
)
adTAeScuTACACSPlusServerAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeScuTACACSPlusServerAddressType.setStatus("current")
_AdTAeScuTACACSPlusServerInetAddress_Type = InetAddress
_AdTAeScuTACACSPlusServerInetAddress_Object = MibTableColumn
adTAeScuTACACSPlusServerInetAddress = _AdTAeScuTACACSPlusServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 5, 30, 6, 1, 10),
    _AdTAeScuTACACSPlusServerInetAddress_Type()
)
adTAeScuTACACSPlusServerInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuTACACSPlusServerInetAddress.setStatus("current")
_AdTAeSCUNetworkMgmt_ObjectIdentity = ObjectIdentity
adTAeSCUNetworkMgmt = _AdTAeSCUNetworkMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 6)
)


class _AdTAeSCUNetworkMgmtPortBaudRate_Type(Integer32):
    """Custom type adTAeSCUNetworkMgmtPortBaudRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("baud1200", 1),
          ("baud2400", 2),
          ("baud4800", 3),
          ("baud9600", 4),
          ("baud19200", 5),
          ("baud38400", 6),
          ("baud57600", 7),
          ("baud115200", 8))
    )


_AdTAeSCUNetworkMgmtPortBaudRate_Type.__name__ = "Integer32"
_AdTAeSCUNetworkMgmtPortBaudRate_Object = MibScalar
adTAeSCUNetworkMgmtPortBaudRate = _AdTAeSCUNetworkMgmtPortBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 6, 1),
    _AdTAeSCUNetworkMgmtPortBaudRate_Type()
)
adTAeSCUNetworkMgmtPortBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUNetworkMgmtPortBaudRate.setStatus("current")


class _AdTAeSCUNetworkMgmtPortComMode_Type(Integer32):
    """Custom type adTAeSCUNetworkMgmtPortComMode based on Integer32"""
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
        *(("x25", 1),
          ("terminalServer", 2),
          ("pPP", 3),
          ("accessoryOption", 4),
          ("cLI", 5))
    )


_AdTAeSCUNetworkMgmtPortComMode_Type.__name__ = "Integer32"
_AdTAeSCUNetworkMgmtPortComMode_Object = MibScalar
adTAeSCUNetworkMgmtPortComMode = _AdTAeSCUNetworkMgmtPortComMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 6, 2),
    _AdTAeSCUNetworkMgmtPortComMode_Type()
)
adTAeSCUNetworkMgmtPortComMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUNetworkMgmtPortComMode.setStatus("current")


class _AdTAeSCUNetworkMgmtPPPSerialPortMode_Type(Integer32):
    """Custom type adTAeSCUNetworkMgmtPPPSerialPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("async", 1),
          ("sync", 2))
    )


_AdTAeSCUNetworkMgmtPPPSerialPortMode_Type.__name__ = "Integer32"
_AdTAeSCUNetworkMgmtPPPSerialPortMode_Object = MibScalar
adTAeSCUNetworkMgmtPPPSerialPortMode = _AdTAeSCUNetworkMgmtPPPSerialPortMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 6, 3),
    _AdTAeSCUNetworkMgmtPPPSerialPortMode_Type()
)
adTAeSCUNetworkMgmtPPPSerialPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUNetworkMgmtPPPSerialPortMode.setStatus("current")


class _AdTAeSCUNetworkMgmtInterbankComMode_Type(Integer32):
    """Custom type adTAeSCUNetworkMgmtInterbankComMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("host", 1),
          ("client", 2))
    )


_AdTAeSCUNetworkMgmtInterbankComMode_Type.__name__ = "Integer32"
_AdTAeSCUNetworkMgmtInterbankComMode_Object = MibScalar
adTAeSCUNetworkMgmtInterbankComMode = _AdTAeSCUNetworkMgmtInterbankComMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 6, 4),
    _AdTAeSCUNetworkMgmtInterbankComMode_Type()
)
adTAeSCUNetworkMgmtInterbankComMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUNetworkMgmtInterbankComMode.setStatus("current")


class _AdTAeSCUNetworkMgmtInterbankComModeWritable_Type(Integer32):
    """Custom type adTAeSCUNetworkMgmtInterbankComModeWritable based on Integer32"""
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


_AdTAeSCUNetworkMgmtInterbankComModeWritable_Type.__name__ = "Integer32"
_AdTAeSCUNetworkMgmtInterbankComModeWritable_Object = MibScalar
adTAeSCUNetworkMgmtInterbankComModeWritable = _AdTAeSCUNetworkMgmtInterbankComModeWritable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 6, 5),
    _AdTAeSCUNetworkMgmtInterbankComModeWritable_Type()
)
adTAeSCUNetworkMgmtInterbankComModeWritable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeSCUNetworkMgmtInterbankComModeWritable.setStatus("current")


class _AdTAeSCUNetworkMgmtSecurityEnable_Type(Integer32):
    """Custom type adTAeSCUNetworkMgmtSecurityEnable based on Integer32"""
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


_AdTAeSCUNetworkMgmtSecurityEnable_Type.__name__ = "Integer32"
_AdTAeSCUNetworkMgmtSecurityEnable_Object = MibScalar
adTAeSCUNetworkMgmtSecurityEnable = _AdTAeSCUNetworkMgmtSecurityEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 6, 6),
    _AdTAeSCUNetworkMgmtSecurityEnable_Type()
)
adTAeSCUNetworkMgmtSecurityEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUNetworkMgmtSecurityEnable.setStatus("current")
_AdTAeSCUsDNS_ObjectIdentity = ObjectIdentity
adTAeSCUsDNS = _AdTAeSCUsDNS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 7)
)


class _AdTAeScuDNSlookupService_Type(Integer32):
    """Custom type adTAeScuDNSlookupService based on Integer32"""
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


_AdTAeScuDNSlookupService_Type.__name__ = "Integer32"
_AdTAeScuDNSlookupService_Object = MibScalar
adTAeScuDNSlookupService = _AdTAeScuDNSlookupService_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 7, 1),
    _AdTAeScuDNSlookupService_Type()
)
adTAeScuDNSlookupService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuDNSlookupService.setStatus("current")
_AdTAeScuDNSprimaryIP_Type = IpAddress
_AdTAeScuDNSprimaryIP_Object = MibScalar
adTAeScuDNSprimaryIP = _AdTAeScuDNSprimaryIP_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 7, 2),
    _AdTAeScuDNSprimaryIP_Type()
)
adTAeScuDNSprimaryIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuDNSprimaryIP.setStatus("deprecated")
_AdTAeScuDNSsecondaryIP_Type = IpAddress
_AdTAeScuDNSsecondaryIP_Object = MibScalar
adTAeScuDNSsecondaryIP = _AdTAeScuDNSsecondaryIP_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 7, 3),
    _AdTAeScuDNSsecondaryIP_Type()
)
adTAeScuDNSsecondaryIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuDNSsecondaryIP.setStatus("deprecated")


class _AdTAeScuDNSsearchList_Type(DisplayString):
    """Custom type adTAeScuDNSsearchList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AdTAeScuDNSsearchList_Type.__name__ = "DisplayString"
_AdTAeScuDNSsearchList_Object = MibScalar
adTAeScuDNSsearchList = _AdTAeScuDNSsearchList_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 7, 4),
    _AdTAeScuDNSsearchList_Type()
)
adTAeScuDNSsearchList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuDNSsearchList.setStatus("current")
_IpDNSLookupIpTable_Object = MibTable
ipDNSLookupIpTable = _IpDNSLookupIpTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 7, 5)
)
if mibBuilder.loadTexts:
    ipDNSLookupIpTable.setStatus("current")
_IpDNSLookupIpTableEntry_Object = MibTableRow
ipDNSLookupIpTableEntry = _IpDNSLookupIpTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 7, 5, 1)
)
ipDNSLookupIpTableEntry.setIndexNames(
    (0, "ADTRAN-TAeSCU-MIB", "ipDNSLookupIpIndex"),
)
if mibBuilder.loadTexts:
    ipDNSLookupIpTableEntry.setStatus("current")
_IpDNSLookupIpIndex_Type = Integer32
_IpDNSLookupIpIndex_Object = MibTableColumn
ipDNSLookupIpIndex = _IpDNSLookupIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 7, 5, 1, 1),
    _IpDNSLookupIpIndex_Type()
)
ipDNSLookupIpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipDNSLookupIpIndex.setStatus("current")
_IpDNSLookupIpInetAddressType_Type = InetAddressType
_IpDNSLookupIpInetAddressType_Object = MibTableColumn
ipDNSLookupIpInetAddressType = _IpDNSLookupIpInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 7, 5, 1, 2),
    _IpDNSLookupIpInetAddressType_Type()
)
ipDNSLookupIpInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipDNSLookupIpInetAddressType.setStatus("current")
_IpDNSLookupIpInetAddress_Type = InetAddress
_IpDNSLookupIpInetAddress_Object = MibTableColumn
ipDNSLookupIpInetAddress = _IpDNSLookupIpInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 7, 5, 1, 3),
    _IpDNSLookupIpInetAddress_Type()
)
ipDNSLookupIpInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipDNSLookupIpInetAddress.setStatus("current")
_AdTAeSCUFirmwareTFTPConfigMgmt_ObjectIdentity = ObjectIdentity
adTAeSCUFirmwareTFTPConfigMgmt = _AdTAeSCUFirmwareTFTPConfigMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 8)
)


class _AdTAeScuFirmwareTftpRemoteFileName_Type(DisplayString):
    """Custom type adTAeScuFirmwareTftpRemoteFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AdTAeScuFirmwareTftpRemoteFileName_Type.__name__ = "DisplayString"
_AdTAeScuFirmwareTftpRemoteFileName_Object = MibScalar
adTAeScuFirmwareTftpRemoteFileName = _AdTAeScuFirmwareTftpRemoteFileName_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 8, 1),
    _AdTAeScuFirmwareTftpRemoteFileName_Type()
)
adTAeScuFirmwareTftpRemoteFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuFirmwareTftpRemoteFileName.setStatus("current")


class _AdTAeScuFirmwareTftpServerHostName_Type(DisplayString):
    """Custom type adTAeScuFirmwareTftpServerHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AdTAeScuFirmwareTftpServerHostName_Type.__name__ = "DisplayString"
_AdTAeScuFirmwareTftpServerHostName_Object = MibScalar
adTAeScuFirmwareTftpServerHostName = _AdTAeScuFirmwareTftpServerHostName_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 8, 2),
    _AdTAeScuFirmwareTftpServerHostName_Type()
)
adTAeScuFirmwareTftpServerHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuFirmwareTftpServerHostName.setStatus("deprecated")
_AdTAeScuFirmwareTftpServerIP_Type = IpAddress
_AdTAeScuFirmwareTftpServerIP_Object = MibScalar
adTAeScuFirmwareTftpServerIP = _AdTAeScuFirmwareTftpServerIP_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 8, 3),
    _AdTAeScuFirmwareTftpServerIP_Type()
)
adTAeScuFirmwareTftpServerIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeScuFirmwareTftpServerIP.setStatus("deprecated")


class _AdTAeScuFirmwareTftpCacheExpire_Type(Integer32):
    """Custom type adTAeScuFirmwareTftpCacheExpire based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_AdTAeScuFirmwareTftpCacheExpire_Type.__name__ = "Integer32"
_AdTAeScuFirmwareTftpCacheExpire_Object = MibScalar
adTAeScuFirmwareTftpCacheExpire = _AdTAeScuFirmwareTftpCacheExpire_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 8, 4),
    _AdTAeScuFirmwareTftpCacheExpire_Type()
)
adTAeScuFirmwareTftpCacheExpire.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuFirmwareTftpCacheExpire.setStatus("current")


class _AdTAeScuFirmwareTftpInvalidate_Type(Integer32):
    """Custom type adTAeScuFirmwareTftpInvalidate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("discardCurrentConfigInfo", 1)
    )


_AdTAeScuFirmwareTftpInvalidate_Type.__name__ = "Integer32"
_AdTAeScuFirmwareTftpInvalidate_Object = MibScalar
adTAeScuFirmwareTftpInvalidate = _AdTAeScuFirmwareTftpInvalidate_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 8, 5),
    _AdTAeScuFirmwareTftpInvalidate_Type()
)
adTAeScuFirmwareTftpInvalidate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuFirmwareTftpInvalidate.setStatus("current")
_AdTAeScmFirmwareTftpServerInetAddressType_Type = InetAddressType
_AdTAeScmFirmwareTftpServerInetAddressType_Object = MibScalar
adTAeScmFirmwareTftpServerInetAddressType = _AdTAeScmFirmwareTftpServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 8, 6),
    _AdTAeScmFirmwareTftpServerInetAddressType_Type()
)
adTAeScmFirmwareTftpServerInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeScmFirmwareTftpServerInetAddressType.setStatus("current")
_AdTAeScmFirmwareTftpServerIPInetAddress_Type = InetAddress
_AdTAeScmFirmwareTftpServerIPInetAddress_Object = MibScalar
adTAeScmFirmwareTftpServerIPInetAddress = _AdTAeScmFirmwareTftpServerIPInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 8, 7),
    _AdTAeScmFirmwareTftpServerIPInetAddress_Type()
)
adTAeScmFirmwareTftpServerIPInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScmFirmwareTftpServerIPInetAddress.setStatus("current")
_AdTAeSCUSystemConfigArchiveMgmt_ObjectIdentity = ObjectIdentity
adTAeSCUSystemConfigArchiveMgmt = _AdTAeSCUSystemConfigArchiveMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 9)
)


class _AdTAeScuSCATftpServerHostName_Type(DisplayString):
    """Custom type adTAeScuSCATftpServerHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AdTAeScuSCATftpServerHostName_Type.__name__ = "DisplayString"
_AdTAeScuSCATftpServerHostName_Object = MibScalar
adTAeScuSCATftpServerHostName = _AdTAeScuSCATftpServerHostName_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 9, 1),
    _AdTAeScuSCATftpServerHostName_Type()
)
adTAeScuSCATftpServerHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuSCATftpServerHostName.setStatus("deprecated")
_AdTAeScuSCATftpServerIP_Type = IpAddress
_AdTAeScuSCATftpServerIP_Object = MibScalar
adTAeScuSCATftpServerIP = _AdTAeScuSCATftpServerIP_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 9, 2),
    _AdTAeScuSCATftpServerIP_Type()
)
adTAeScuSCATftpServerIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeScuSCATftpServerIP.setStatus("current")
_AdTAeScuSCATftpServerIPInetAddressType_Type = InetAddressType
_AdTAeScuSCATftpServerIPInetAddressType_Object = MibScalar
adTAeScuSCATftpServerIPInetAddressType = _AdTAeScuSCATftpServerIPInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 9, 3),
    _AdTAeScuSCATftpServerIPInetAddressType_Type()
)
adTAeScuSCATftpServerIPInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeScuSCATftpServerIPInetAddressType.setStatus("current")
_AdTAeScuSCATftpServerHostNameInetAddress_Type = InetAddress
_AdTAeScuSCATftpServerHostNameInetAddress_Object = MibScalar
adTAeScuSCATftpServerHostNameInetAddress = _AdTAeScuSCATftpServerHostNameInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 9, 4),
    _AdTAeScuSCATftpServerHostNameInetAddress_Type()
)
adTAeScuSCATftpServerHostNameInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuSCATftpServerHostNameInetAddress.setStatus("current")
_AdTAeSCUSCAControl_ObjectIdentity = ObjectIdentity
adTAeSCUSCAControl = _AdTAeSCUSCAControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 9, 10)
)


class _AdTAeScuSCAFileName_Type(DisplayString):
    """Custom type adTAeScuSCAFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AdTAeScuSCAFileName_Type.__name__ = "DisplayString"
_AdTAeScuSCAFileName_Object = MibScalar
adTAeScuSCAFileName = _AdTAeScuSCAFileName_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 9, 10, 1),
    _AdTAeScuSCAFileName_Type()
)
adTAeScuSCAFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuSCAFileName.setStatus("current")


class _AdTAeScuSCAInitiateSave_Type(Integer32):
    """Custom type adTAeScuSCAInitiateSave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("initiate", 1)
    )


_AdTAeScuSCAInitiateSave_Type.__name__ = "Integer32"
_AdTAeScuSCAInitiateSave_Object = MibScalar
adTAeScuSCAInitiateSave = _AdTAeScuSCAInitiateSave_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 9, 10, 2),
    _AdTAeScuSCAInitiateSave_Type()
)
adTAeScuSCAInitiateSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuSCAInitiateSave.setStatus("current")


class _AdTAeScuSCAInitiateRestore_Type(Integer32):
    """Custom type adTAeScuSCAInitiateRestore based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("initiate", 1)
    )


_AdTAeScuSCAInitiateRestore_Type.__name__ = "Integer32"
_AdTAeScuSCAInitiateRestore_Object = MibScalar
adTAeScuSCAInitiateRestore = _AdTAeScuSCAInitiateRestore_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 9, 10, 3),
    _AdTAeScuSCAInitiateRestore_Type()
)
adTAeScuSCAInitiateRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuSCAInitiateRestore.setStatus("current")
_AdTAeScuSCAProvItemChanged_Type = Integer32
_AdTAeScuSCAProvItemChanged_Object = MibScalar
adTAeScuSCAProvItemChanged = _AdTAeScuSCAProvItemChanged_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 9, 10, 4),
    _AdTAeScuSCAProvItemChanged_Type()
)
adTAeScuSCAProvItemChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeScuSCAProvItemChanged.setStatus("current")
_AdTAeScuSCAPresentCards_Type = Integer32
_AdTAeScuSCAPresentCards_Object = MibScalar
adTAeScuSCAPresentCards = _AdTAeScuSCAPresentCards_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 9, 10, 5),
    _AdTAeScuSCAPresentCards_Type()
)
adTAeScuSCAPresentCards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeScuSCAPresentCards.setStatus("current")
_AdTAeScuSCASlotsWithProvData_Type = Integer32
_AdTAeScuSCASlotsWithProvData_Object = MibScalar
adTAeScuSCASlotsWithProvData = _AdTAeScuSCASlotsWithProvData_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 9, 10, 6),
    _AdTAeScuSCASlotsWithProvData_Type()
)
adTAeScuSCASlotsWithProvData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeScuSCASlotsWithProvData.setStatus("current")
_AdTAeScuSCASlotsInSCA_Type = Integer32
_AdTAeScuSCASlotsInSCA_Object = MibScalar
adTAeScuSCASlotsInSCA = _AdTAeScuSCASlotsInSCA_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 9, 10, 7),
    _AdTAeScuSCASlotsInSCA_Type()
)
adTAeScuSCASlotsInSCA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeScuSCASlotsInSCA.setStatus("current")
_AdTAeScuSCASlotsWithProvDataInSCA_Type = Integer32
_AdTAeScuSCASlotsWithProvDataInSCA_Object = MibScalar
adTAeScuSCASlotsWithProvDataInSCA = _AdTAeScuSCASlotsWithProvDataInSCA_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 9, 10, 8),
    _AdTAeScuSCASlotsWithProvDataInSCA_Type()
)
adTAeScuSCASlotsWithProvDataInSCA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeScuSCASlotsWithProvDataInSCA.setStatus("current")
_AdTAeSCUSCAOperationStatusTable_Object = MibTable
adTAeSCUSCAOperationStatusTable = _AdTAeSCUSCAOperationStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 9, 10, 10)
)
if mibBuilder.loadTexts:
    adTAeSCUSCAOperationStatusTable.setStatus("current")
_AdTAeSCUSCAOperationStatusEntry_Object = MibTableRow
adTAeSCUSCAOperationStatusEntry = _AdTAeSCUSCAOperationStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 9, 10, 10, 1)
)
adTAeSCUSCAOperationStatusEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adTAeSCUSCAOperationStatusEntry.setStatus("current")


class _AdTAeScuSCAOperationStatus_Type(DisplayString):
    """Custom type adTAeScuSCAOperationStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AdTAeScuSCAOperationStatus_Type.__name__ = "DisplayString"
_AdTAeScuSCAOperationStatus_Object = MibTableColumn
adTAeScuSCAOperationStatus = _AdTAeScuSCAOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 9, 10, 10, 1, 1),
    _AdTAeScuSCAOperationStatus_Type()
)
adTAeScuSCAOperationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeScuSCAOperationStatus.setStatus("current")
_AdTAeSCUSCAAutoSaveMgmt_ObjectIdentity = ObjectIdentity
adTAeSCUSCAAutoSaveMgmt = _AdTAeSCUSCAAutoSaveMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 9, 11)
)


class _AdTAeScuSCAAutoSave_Type(Integer32):
    """Custom type adTAeScuSCAAutoSave based on Integer32"""
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


_AdTAeScuSCAAutoSave_Type.__name__ = "Integer32"
_AdTAeScuSCAAutoSave_Object = MibScalar
adTAeScuSCAAutoSave = _AdTAeScuSCAAutoSave_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 9, 11, 1),
    _AdTAeScuSCAAutoSave_Type()
)
adTAeScuSCAAutoSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuSCAAutoSave.setStatus("current")


class _AdTAeScuSCAAutoSaveRetries_Type(Integer32):
    """Custom type adTAeScuSCAAutoSaveRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_AdTAeScuSCAAutoSaveRetries_Type.__name__ = "Integer32"
_AdTAeScuSCAAutoSaveRetries_Object = MibScalar
adTAeScuSCAAutoSaveRetries = _AdTAeScuSCAAutoSaveRetries_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 9, 11, 3),
    _AdTAeScuSCAAutoSaveRetries_Type()
)
adTAeScuSCAAutoSaveRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuSCAAutoSaveRetries.setStatus("current")


class _AdTAeScuSCAAutoSaveIfChanged_Type(Integer32):
    """Custom type adTAeScuSCAAutoSaveIfChanged based on Integer32"""
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


_AdTAeScuSCAAutoSaveIfChanged_Type.__name__ = "Integer32"
_AdTAeScuSCAAutoSaveIfChanged_Object = MibScalar
adTAeScuSCAAutoSaveIfChanged = _AdTAeScuSCAAutoSaveIfChanged_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 9, 11, 5),
    _AdTAeScuSCAAutoSaveIfChanged_Type()
)
adTAeScuSCAAutoSaveIfChanged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuSCAAutoSaveIfChanged.setStatus("current")


class _AdTAeScuSCAAutoSaveFileNamePrefix_Type(DisplayString):
    """Custom type adTAeScuSCAAutoSaveFileNamePrefix based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_AdTAeScuSCAAutoSaveFileNamePrefix_Type.__name__ = "DisplayString"
_AdTAeScuSCAAutoSaveFileNamePrefix_Object = MibScalar
adTAeScuSCAAutoSaveFileNamePrefix = _AdTAeScuSCAAutoSaveFileNamePrefix_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 9, 11, 7),
    _AdTAeScuSCAAutoSaveFileNamePrefix_Type()
)
adTAeScuSCAAutoSaveFileNamePrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuSCAAutoSaveFileNamePrefix.setStatus("current")


class _AdTAeScuSCAAutoSaveFileNameSuffix_Type(DisplayString):
    """Custom type adTAeScuSCAAutoSaveFileNameSuffix based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AdTAeScuSCAAutoSaveFileNameSuffix_Type.__name__ = "DisplayString"
_AdTAeScuSCAAutoSaveFileNameSuffix_Object = MibScalar
adTAeScuSCAAutoSaveFileNameSuffix = _AdTAeScuSCAAutoSaveFileNameSuffix_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 9, 11, 9),
    _AdTAeScuSCAAutoSaveFileNameSuffix_Type()
)
adTAeScuSCAAutoSaveFileNameSuffix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuSCAAutoSaveFileNameSuffix.setStatus("current")


class _AdTAeScuSCAAutoSaveInstances_Type(Integer32):
    """Custom type adTAeScuSCAAutoSaveInstances based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AdTAeScuSCAAutoSaveInstances_Type.__name__ = "Integer32"
_AdTAeScuSCAAutoSaveInstances_Object = MibScalar
adTAeScuSCAAutoSaveInstances = _AdTAeScuSCAAutoSaveInstances_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 9, 11, 11),
    _AdTAeScuSCAAutoSaveInstances_Type()
)
adTAeScuSCAAutoSaveInstances.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuSCAAutoSaveInstances.setStatus("current")


class _AdTAeScuSCAAutoSaveHoursAfter_Type(Integer32):
    """Custom type adTAeScuSCAAutoSaveHoursAfter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_AdTAeScuSCAAutoSaveHoursAfter_Type.__name__ = "Integer32"
_AdTAeScuSCAAutoSaveHoursAfter_Object = MibScalar
adTAeScuSCAAutoSaveHoursAfter = _AdTAeScuSCAAutoSaveHoursAfter_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 9, 11, 13),
    _AdTAeScuSCAAutoSaveHoursAfter_Type()
)
adTAeScuSCAAutoSaveHoursAfter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuSCAAutoSaveHoursAfter.setStatus("current")


class _AdTAeScuSCAAutoSaveMinutesAfter_Type(Integer32):
    """Custom type adTAeScuSCAAutoSaveMinutesAfter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_AdTAeScuSCAAutoSaveMinutesAfter_Type.__name__ = "Integer32"
_AdTAeScuSCAAutoSaveMinutesAfter_Object = MibScalar
adTAeScuSCAAutoSaveMinutesAfter = _AdTAeScuSCAAutoSaveMinutesAfter_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 9, 11, 15),
    _AdTAeScuSCAAutoSaveMinutesAfter_Type()
)
adTAeScuSCAAutoSaveMinutesAfter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuSCAAutoSaveMinutesAfter.setStatus("current")


class _AdTAeScuSCADateTimeLastAutoSave_Type(DisplayString):
    """Custom type adTAeScuSCADateTimeLastAutoSave based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AdTAeScuSCADateTimeLastAutoSave_Type.__name__ = "DisplayString"
_AdTAeScuSCADateTimeLastAutoSave_Object = MibScalar
adTAeScuSCADateTimeLastAutoSave = _AdTAeScuSCADateTimeLastAutoSave_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 9, 11, 17),
    _AdTAeScuSCADateTimeLastAutoSave_Type()
)
adTAeScuSCADateTimeLastAutoSave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeScuSCADateTimeLastAutoSave.setStatus("current")


class _AdTAeScuSCADateTimeNextAutoSave_Type(DisplayString):
    """Custom type adTAeScuSCADateTimeNextAutoSave based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AdTAeScuSCADateTimeNextAutoSave_Type.__name__ = "DisplayString"
_AdTAeScuSCADateTimeNextAutoSave_Object = MibScalar
adTAeScuSCADateTimeNextAutoSave = _AdTAeScuSCADateTimeNextAutoSave_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 9, 11, 18),
    _AdTAeScuSCADateTimeNextAutoSave_Type()
)
adTAeScuSCADateTimeNextAutoSave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeScuSCADateTimeNextAutoSave.setStatus("current")
_AdTAeSCUSCARestoreMgmt_ObjectIdentity = ObjectIdentity
adTAeSCUSCARestoreMgmt = _AdTAeSCUSCARestoreMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 9, 12)
)


class _AdTAeScuSCAoptRestoreESCU_Type(Integer32):
    """Custom type adTAeScuSCAoptRestoreESCU based on Integer32"""
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


_AdTAeScuSCAoptRestoreESCU_Type.__name__ = "Integer32"
_AdTAeScuSCAoptRestoreESCU_Object = MibScalar
adTAeScuSCAoptRestoreESCU = _AdTAeScuSCAoptRestoreESCU_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 9, 12, 1),
    _AdTAeScuSCAoptRestoreESCU_Type()
)
adTAeScuSCAoptRestoreESCU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuSCAoptRestoreESCU.setStatus("current")


class _AdTAeScuSCAoptRestoreSCA_Type(Integer32):
    """Custom type adTAeScuSCAoptRestoreSCA based on Integer32"""
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


_AdTAeScuSCAoptRestoreSCA_Type.__name__ = "Integer32"
_AdTAeScuSCAoptRestoreSCA_Object = MibScalar
adTAeScuSCAoptRestoreSCA = _AdTAeScuSCAoptRestoreSCA_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 9, 12, 2),
    _AdTAeScuSCAoptRestoreSCA_Type()
)
adTAeScuSCAoptRestoreSCA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuSCAoptRestoreSCA.setStatus("current")


class _AdTAeScuSCAoptRestoreNetwork_Type(Integer32):
    """Custom type adTAeScuSCAoptRestoreNetwork based on Integer32"""
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


_AdTAeScuSCAoptRestoreNetwork_Type.__name__ = "Integer32"
_AdTAeScuSCAoptRestoreNetwork_Object = MibScalar
adTAeScuSCAoptRestoreNetwork = _AdTAeScuSCAoptRestoreNetwork_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 9, 12, 3),
    _AdTAeScuSCAoptRestoreNetwork_Type()
)
adTAeScuSCAoptRestoreNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuSCAoptRestoreNetwork.setStatus("current")


class _AdTAeScuSCAoptRestoreNetworkInterface_Type(Integer32):
    """Custom type adTAeScuSCAoptRestoreNetworkInterface based on Integer32"""
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


_AdTAeScuSCAoptRestoreNetworkInterface_Type.__name__ = "Integer32"
_AdTAeScuSCAoptRestoreNetworkInterface_Object = MibScalar
adTAeScuSCAoptRestoreNetworkInterface = _AdTAeScuSCAoptRestoreNetworkInterface_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 9, 12, 4),
    _AdTAeScuSCAoptRestoreNetworkInterface_Type()
)
adTAeScuSCAoptRestoreNetworkInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuSCAoptRestoreNetworkInterface.setStatus("current")


class _AdTAeScuSCAoptRestoreSNMP_Type(Integer32):
    """Custom type adTAeScuSCAoptRestoreSNMP based on Integer32"""
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


_AdTAeScuSCAoptRestoreSNMP_Type.__name__ = "Integer32"
_AdTAeScuSCAoptRestoreSNMP_Object = MibScalar
adTAeScuSCAoptRestoreSNMP = _AdTAeScuSCAoptRestoreSNMP_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 9, 12, 5),
    _AdTAeScuSCAoptRestoreSNMP_Type()
)
adTAeScuSCAoptRestoreSNMP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuSCAoptRestoreSNMP.setStatus("current")


class _AdTAeScuSCAoptRestoreSecurity_Type(Integer32):
    """Custom type adTAeScuSCAoptRestoreSecurity based on Integer32"""
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


_AdTAeScuSCAoptRestoreSecurity_Type.__name__ = "Integer32"
_AdTAeScuSCAoptRestoreSecurity_Object = MibScalar
adTAeScuSCAoptRestoreSecurity = _AdTAeScuSCAoptRestoreSecurity_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 9, 12, 6),
    _AdTAeScuSCAoptRestoreSecurity_Type()
)
adTAeScuSCAoptRestoreSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuSCAoptRestoreSecurity.setStatus("current")


class _AdTAeScuSCAoptRestoreLineCard_Type(Integer32):
    """Custom type adTAeScuSCAoptRestoreLineCard based on Integer32"""
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


_AdTAeScuSCAoptRestoreLineCard_Type.__name__ = "Integer32"
_AdTAeScuSCAoptRestoreLineCard_Object = MibScalar
adTAeScuSCAoptRestoreLineCard = _AdTAeScuSCAoptRestoreLineCard_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 9, 12, 7),
    _AdTAeScuSCAoptRestoreLineCard_Type()
)
adTAeScuSCAoptRestoreLineCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuSCAoptRestoreLineCard.setStatus("current")


class _AdTAeScuSCAoptRestoreInServiceLineCard_Type(Integer32):
    """Custom type adTAeScuSCAoptRestoreInServiceLineCard based on Integer32"""
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


_AdTAeScuSCAoptRestoreInServiceLineCard_Type.__name__ = "Integer32"
_AdTAeScuSCAoptRestoreInServiceLineCard_Object = MibScalar
adTAeScuSCAoptRestoreInServiceLineCard = _AdTAeScuSCAoptRestoreInServiceLineCard_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 9, 12, 8),
    _AdTAeScuSCAoptRestoreInServiceLineCard_Type()
)
adTAeScuSCAoptRestoreInServiceLineCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuSCAoptRestoreInServiceLineCard.setStatus("current")


class _AdTAeScuSCAoptRestoreEmptySlot_Type(Integer32):
    """Custom type adTAeScuSCAoptRestoreEmptySlot based on Integer32"""
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


_AdTAeScuSCAoptRestoreEmptySlot_Type.__name__ = "Integer32"
_AdTAeScuSCAoptRestoreEmptySlot_Object = MibScalar
adTAeScuSCAoptRestoreEmptySlot = _AdTAeScuSCAoptRestoreEmptySlot_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 9, 12, 9),
    _AdTAeScuSCAoptRestoreEmptySlot_Type()
)
adTAeScuSCAoptRestoreEmptySlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuSCAoptRestoreEmptySlot.setStatus("current")
_AdTAeScuSCAoptRestoreCardBitmask_Type = Integer32
_AdTAeScuSCAoptRestoreCardBitmask_Object = MibScalar
adTAeScuSCAoptRestoreCardBitmask = _AdTAeScuSCAoptRestoreCardBitmask_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 9, 12, 12),
    _AdTAeScuSCAoptRestoreCardBitmask_Type()
)
adTAeScuSCAoptRestoreCardBitmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuSCAoptRestoreCardBitmask.setStatus("current")


class _AdTAeScuSCADateTimeSaveInvoked_Type(DisplayString):
    """Custom type adTAeScuSCADateTimeSaveInvoked based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AdTAeScuSCADateTimeSaveInvoked_Type.__name__ = "DisplayString"
_AdTAeScuSCADateTimeSaveInvoked_Object = MibScalar
adTAeScuSCADateTimeSaveInvoked = _AdTAeScuSCADateTimeSaveInvoked_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 9, 12, 13),
    _AdTAeScuSCADateTimeSaveInvoked_Type()
)
adTAeScuSCADateTimeSaveInvoked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeScuSCADateTimeSaveInvoked.setStatus("current")
_AdTAeScuSCACardsRestoredBitmask_Type = Integer32
_AdTAeScuSCACardsRestoredBitmask_Object = MibScalar
adTAeScuSCACardsRestoredBitmask = _AdTAeScuSCACardsRestoredBitmask_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 9, 12, 14),
    _AdTAeScuSCACardsRestoredBitmask_Type()
)
adTAeScuSCACardsRestoredBitmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeScuSCACardsRestoredBitmask.setStatus("current")
_AdTAeScuSCACardsNotRestoredBitmask_Type = Integer32
_AdTAeScuSCACardsNotRestoredBitmask_Object = MibScalar
adTAeScuSCACardsNotRestoredBitmask = _AdTAeScuSCACardsNotRestoredBitmask_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 9, 12, 15),
    _AdTAeScuSCACardsNotRestoredBitmask_Type()
)
adTAeScuSCACardsNotRestoredBitmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeScuSCACardsNotRestoredBitmask.setStatus("current")
_AdTAeScuSCACardsExcludedBitmask_Type = Integer32
_AdTAeScuSCACardsExcludedBitmask_Object = MibScalar
adTAeScuSCACardsExcludedBitmask = _AdTAeScuSCACardsExcludedBitmask_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 9, 12, 16),
    _AdTAeScuSCACardsExcludedBitmask_Type()
)
adTAeScuSCACardsExcludedBitmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeScuSCACardsExcludedBitmask.setStatus("current")
_AdTAeScuSCARestoreCardErrorsBitmask_Type = Integer32
_AdTAeScuSCARestoreCardErrorsBitmask_Object = MibScalar
adTAeScuSCARestoreCardErrorsBitmask = _AdTAeScuSCARestoreCardErrorsBitmask_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 9, 12, 17),
    _AdTAeScuSCARestoreCardErrorsBitmask_Type()
)
adTAeScuSCARestoreCardErrorsBitmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeScuSCARestoreCardErrorsBitmask.setStatus("current")
_AdTAeSCUSystemLog_ObjectIdentity = ObjectIdentity
adTAeSCUSystemLog = _AdTAeSCUSystemLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 14)
)


class _AdTAeSCUSystemLogAlarm_Type(Integer32):
    """Custom type adTAeSCUSystemLogAlarm based on Integer32"""
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


_AdTAeSCUSystemLogAlarm_Type.__name__ = "Integer32"
_AdTAeSCUSystemLogAlarm_Object = MibScalar
adTAeSCUSystemLogAlarm = _AdTAeSCUSystemLogAlarm_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 14, 3),
    _AdTAeSCUSystemLogAlarm_Type()
)
adTAeSCUSystemLogAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUSystemLogAlarm.setStatus("current")
_AdTAeSCUSystemLogPercentFull_Type = Integer32
_AdTAeSCUSystemLogPercentFull_Object = MibScalar
adTAeSCUSystemLogPercentFull = _AdTAeSCUSystemLogPercentFull_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 14, 5),
    _AdTAeSCUSystemLogPercentFull_Type()
)
adTAeSCUSystemLogPercentFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeSCUSystemLogPercentFull.setStatus("current")
_AdTAeSCUSystemLogCount_Type = Integer32
_AdTAeSCUSystemLogCount_Object = MibScalar
adTAeSCUSystemLogCount = _AdTAeSCUSystemLogCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 14, 7),
    _AdTAeSCUSystemLogCount_Type()
)
adTAeSCUSystemLogCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeSCUSystemLogCount.setStatus("current")


class _AdTAeSCUSystemSummReport_Type(Integer32):
    """Custom type adTAeSCUSystemSummReport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("allEvents", 1),
          ("loginAndLogoutEvents", 2),
          ("accountChangesEvents", 3),
          ("snmpProvisioning", 4),
          ("networkProvisioning", 5),
          ("tftpYmodemUpdates", 6),
          ("scaEvents", 7),
          ("securityOptionsProv", 8),
          ("dateAndTimeProv", 9))
    )


_AdTAeSCUSystemSummReport_Type.__name__ = "Integer32"
_AdTAeSCUSystemSummReport_Object = MibScalar
adTAeSCUSystemSummReport = _AdTAeSCUSystemSummReport_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 14, 8),
    _AdTAeSCUSystemSummReport_Type()
)
adTAeSCUSystemSummReport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUSystemSummReport.setStatus("current")


class _AdTAeSCUSystemEnableDetail_Type(Integer32):
    """Custom type adTAeSCUSystemEnableDetail based on Integer32"""
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


_AdTAeSCUSystemEnableDetail_Type.__name__ = "Integer32"
_AdTAeSCUSystemEnableDetail_Object = MibScalar
adTAeSCUSystemEnableDetail = _AdTAeSCUSystemEnableDetail_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 14, 9),
    _AdTAeSCUSystemEnableDetail_Type()
)
adTAeSCUSystemEnableDetail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeSCUSystemEnableDetail.setStatus("current")
_AdTAeSCUSystemLogFailureDescription_Type = DisplayString
_AdTAeSCUSystemLogFailureDescription_Object = MibScalar
adTAeSCUSystemLogFailureDescription = _AdTAeSCUSystemLogFailureDescription_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 14, 10),
    _AdTAeSCUSystemLogFailureDescription_Type()
)
adTAeSCUSystemLogFailureDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeSCUSystemLogFailureDescription.setStatus("current")
_AdTAeSCUSystemLogTable_Object = MibTable
adTAeSCUSystemLogTable = _AdTAeSCUSystemLogTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 14, 15)
)
if mibBuilder.loadTexts:
    adTAeSCUSystemLogTable.setStatus("current")
_AdTAeSCUSystemLogEntry_Object = MibTableRow
adTAeSCUSystemLogEntry = _AdTAeSCUSystemLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 14, 15, 1)
)
adTAeSCUSystemLogEntry.setIndexNames(
    (0, "ADTRAN-TAeSCU-MIB", "adTAeSCUSystemLogIndex"),
)
if mibBuilder.loadTexts:
    adTAeSCUSystemLogEntry.setStatus("current")
_AdTAeSCUSystemLogIndex_Type = Integer32
_AdTAeSCUSystemLogIndex_Object = MibTableColumn
adTAeSCUSystemLogIndex = _AdTAeSCUSystemLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 14, 15, 1, 1),
    _AdTAeSCUSystemLogIndex_Type()
)
adTAeSCUSystemLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeSCUSystemLogIndex.setStatus("current")
_AdTAeSCUSystemLogDescription_Type = DisplayString
_AdTAeSCUSystemLogDescription_Object = MibTableColumn
adTAeSCUSystemLogDescription = _AdTAeSCUSystemLogDescription_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 14, 15, 1, 5),
    _AdTAeSCUSystemLogDescription_Type()
)
adTAeSCUSystemLogDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeSCUSystemLogDescription.setStatus("current")
_AdTAeScuTL1ActivityLog_ObjectIdentity = ObjectIdentity
adTAeScuTL1ActivityLog = _AdTAeScuTL1ActivityLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 15)
)


class _AdTAeScuResetTL1Log_Type(Integer32):
    """Custom type adTAeScuResetTL1Log based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("resetTL1Log", 1)
    )


_AdTAeScuResetTL1Log_Type.__name__ = "Integer32"
_AdTAeScuResetTL1Log_Object = MibScalar
adTAeScuResetTL1Log = _AdTAeScuResetTL1Log_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 15, 2),
    _AdTAeScuResetTL1Log_Type()
)
adTAeScuResetTL1Log.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAeScuResetTL1Log.setStatus("current")
_AdTAeScuTL1ActivityLogTable_Object = MibTable
adTAeScuTL1ActivityLogTable = _AdTAeScuTL1ActivityLogTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 15, 6)
)
if mibBuilder.loadTexts:
    adTAeScuTL1ActivityLogTable.setStatus("current")
_AdTAeScuTL1ActivityLogEntry_Object = MibTableRow
adTAeScuTL1ActivityLogEntry = _AdTAeScuTL1ActivityLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 15, 6, 1)
)
adTAeScuTL1ActivityLogEntry.setIndexNames(
    (0, "ADTRAN-TAeSCU-MIB", "adTAeSCUTL1LogIndex"),
)
if mibBuilder.loadTexts:
    adTAeScuTL1ActivityLogEntry.setStatus("current")
_AdTAeSCUTL1LogIndex_Type = Integer32
_AdTAeSCUTL1LogIndex_Object = MibTableColumn
adTAeSCUTL1LogIndex = _AdTAeSCUTL1LogIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 15, 6, 1, 1),
    _AdTAeSCUTL1LogIndex_Type()
)
adTAeSCUTL1LogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeSCUTL1LogIndex.setStatus("current")
_AdTAeScuTL1ActivityLogDescription_Type = DisplayString
_AdTAeScuTL1ActivityLogDescription_Object = MibTableColumn
adTAeScuTL1ActivityLogDescription = _AdTAeScuTL1ActivityLogDescription_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 241, 15, 6, 1, 2),
    _AdTAeScuTL1ActivityLogDescription_Type()
)
adTAeScuTL1ActivityLogDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAeScuTL1ActivityLogDescription.setStatus("current")

# Managed Objects groups


# Notification objects

adTAeSCUSystemLogFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 241, 0, 24101)
)
adTAeSCUSystemLogFull.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-TAeSCU-MIB", "adTAeSCUSystemLogPercentFull"))
)
if mibBuilder.loadTexts:
    adTAeSCUSystemLogFull.setStatus(
        "current"
    )

adTAeSCUSystemLogInvalidAuthentAtt = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 241, 0, 24103)
)
adTAeSCUSystemLogInvalidAuthentAtt.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    adTAeSCUSystemLogInvalidAuthentAtt.setStatus(
        "current"
    )

adTAeSCUSystemLogFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 241, 0, 24105)
)
adTAeSCUSystemLogFailure.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-TAeSCU-MIB", "adTAeSCUSystemLogPercentFull"),
        ("ADTRAN-TAeSCU-MIB", "adTAeSCUSystemLogCount"),
        ("ADTRAN-TAeSCU-MIB", "adTAeSCUSystemLogFailureDescription"))
)
if mibBuilder.loadTexts:
    adTAeSCUSystemLogFailure.setStatus(
        "current"
    )

adTAeSCUSystemInactiveAccountExpiration = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 241, 0, 24163)
)
adTAeSCUSystemInactiveAccountExpiration.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-TAeSCU-MIB", "adTAeSCUSecAccountUserID"),
        ("ADTRAN-TAeSCU-MIB", "adTAeSCUSecAccountAge"))
)
if mibBuilder.loadTexts:
    adTAeSCUSystemInactiveAccountExpiration.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-TAeSCU-MIB",
    **{"adTAeSCU": adTAeSCU,
       "adTAeSCUmgNotificationEvents": adTAeSCUmgNotificationEvents,
       "adTAeSCUSystemLogFull": adTAeSCUSystemLogFull,
       "adTAeSCUSystemLogInvalidAuthentAtt": adTAeSCUSystemLogInvalidAuthentAtt,
       "adTAeSCUSystemLogFailure": adTAeSCUSystemLogFailure,
       "adTAeSCUSystemInactiveAccountExpiration": adTAeSCUSystemInactiveAccountExpiration,
       "adTAeSCUmg": adTAeSCUmg,
       "adTAeSCUConfig": adTAeSCUConfig,
       "adTAeSCUConfigTable": adTAeSCUConfigTable,
       "adTAeSCUConfigEntry": adTAeSCUConfigEntry,
       "adTAeSCUBootVersion": adTAeSCUBootVersion,
       "adTAeSCUCardProv": adTAeSCUCardProv,
       "adTAeSCUCardProvTable": adTAeSCUCardProvTable,
       "adTAeSCUCardProvEntry": adTAeSCUCardProvEntry,
       "adTAeSCUDefaultRouteInterface": adTAeSCUDefaultRouteInterface,
       "adTAeSCUIpForwarding": adTAeSCUIpForwarding,
       "adTAeSCURestoreNetProvFromMUX": adTAeSCURestoreNetProvFromMUX,
       "adTAeSCUDefaultRouteInterfaceEx": adTAeSCUDefaultRouteInterfaceEx,
       "adTAeSCULogoffCraftDTRLoss": adTAeSCULogoffCraftDTRLoss,
       "adTAeSCUMinMenuRefresh": adTAeSCUMinMenuRefresh,
       "adTAeSCUInterfaceStatus": adTAeSCUInterfaceStatus,
       "adTAeSCUInterfaceStatusTable": adTAeSCUInterfaceStatusTable,
       "adTAeSCUInterfaceStatusEntry": adTAeSCUInterfaceStatusEntry,
       "adTAeSCUIfNumber": adTAeSCUIfNumber,
       "adTAeSCUIfIndex": adTAeSCUIfIndex,
       "adTAeSCUIfIPAddress": adTAeSCUIfIPAddress,
       "adTAeSCUIfSubnetMask": adTAeSCUIfSubnetMask,
       "adTAeSCUIfDefaultGateway": adTAeSCUIfDefaultGateway,
       "adTAeSCUIfSpeed": adTAeSCUIfSpeed,
       "adTAeSCUIfXoverCorrection": adTAeSCUIfXoverCorrection,
       "adTAeSCUIfLEDmode": adTAeSCUIfLEDmode,
       "adTAeSCUIfLinkStatus": adTAeSCUIfLinkStatus,
       "adTAeSCUIfLinkRate": adTAeSCUIfLinkRate,
       "adTAeSCUSecurityAccountMg": adTAeSCUSecurityAccountMg,
       "adTAeSCUSecurityAccountEnabled": adTAeSCUSecurityAccountEnabled,
       "adTAeSCUSecAgingGlobalSettings": adTAeSCUSecAgingGlobalSettings,
       "adTAeSCUSecAllAccountExpirationTimer": adTAeSCUSecAllAccountExpirationTimer,
       "adTAeSCUSecReadOnlyAccountExpirationTimer": adTAeSCUSecReadOnlyAccountExpirationTimer,
       "adTAeSCUSecReadWriteAccountExpirationTimer": adTAeSCUSecReadWriteAccountExpirationTimer,
       "adTAeSCUSecTestAccountExpirationTimer": adTAeSCUSecTestAccountExpirationTimer,
       "adTAeSCUSecConfigAccountExpirationTimer": adTAeSCUSecConfigAccountExpirationTimer,
       "adTAeSCUSecAdminAccountExpirationTimer": adTAeSCUSecAdminAccountExpirationTimer,
       "adTAeSCUSecSendAcctExpAlarm": adTAeSCUSecSendAcctExpAlarm,
       "adTAeSCUSecResetAllAccountAge": adTAeSCUSecResetAllAccountAge,
       "adTAeSCUSecAllPasswordExpirationTimer": adTAeSCUSecAllPasswordExpirationTimer,
       "adTAeSCUSecReadOnlyPasswordExpirationTimer": adTAeSCUSecReadOnlyPasswordExpirationTimer,
       "adTAeSCUSecReadWritePasswordExpirationTimer": adTAeSCUSecReadWritePasswordExpirationTimer,
       "adTAeSCUSecTestPasswordExpirationTimer": adTAeSCUSecTestPasswordExpirationTimer,
       "adTAeSCUSecConfigPasswordExpirationTimer": adTAeSCUSecConfigPasswordExpirationTimer,
       "adTAeSCUSecAdminPasswordExpirationTimer": adTAeSCUSecAdminPasswordExpirationTimer,
       "adTAeSCUSecPasswordExpirationWarning": adTAeSCUSecPasswordExpirationWarning,
       "adTAeSCUSecResetAllPasswordAge": adTAeSCUSecResetAllPasswordAge,
       "adTAeSCUSecAccountTable": adTAeSCUSecAccountTable,
       "adTAeSCUSecAccountEntry": adTAeSCUSecAccountEntry,
       "adTAeSCUSecAccountIndex": adTAeSCUSecAccountIndex,
       "adTAeSCUSecAccountUserID": adTAeSCUSecAccountUserID,
       "adTAeSCUSecAccountStatus": adTAeSCUSecAccountStatus,
       "adTAeSCUSecNumAccountLogin": adTAeSCUSecNumAccountLogin,
       "adTAeSCUSecAccountAccessRights": adTAeSCUSecAccountAccessRights,
       "adTAESCUSecChangeAccountPassword": adTAESCUSecChangeAccountPassword,
       "adTAeSCUSecAccStatusExt": adTAeSCUSecAccStatusExt,
       "adTAeSCUSecAccExpTime": adTAeSCUSecAccExpTime,
       "adTAeSCUSecAccPasswordExpTime": adTAeSCUSecAccPasswordExpTime,
       "adTAeSCUSecAccountAge": adTAeSCUSecAccountAge,
       "adTAeSCUSecAccPasswordAge": adTAeSCUSecAccPasswordAge,
       "adTAeSCUSecResetAccountAge": adTAeSCUSecResetAccountAge,
       "adTAeSCUSecResetAccPasswordAge": adTAeSCUSecResetAccPasswordAge,
       "adTAeSCUAccExpirationEnabled": adTAeSCUAccExpirationEnabled,
       "adTAeSCUAccPasswordAccAgingEnabled": adTAeSCUAccPasswordAccAgingEnabled,
       "adTAeSCUSecForcePasswordReset": adTAeSCUSecForcePasswordReset,
       "adTAeSCUSecAccountLoggedInTable": adTAeSCUSecAccountLoggedInTable,
       "adTAeSCUSecAccountLoggedInEntry": adTAeSCUSecAccountLoggedInEntry,
       "adTAeSCUSecAccountloginIndex": adTAeSCUSecAccountloginIndex,
       "adTAeSCUSecAccountLoginUserIDIndex": adTAeSCUSecAccountLoginUserIDIndex,
       "adTAeSCUSecAccountLoginUserID": adTAeSCUSecAccountLoginUserID,
       "adTAeSCUSecAccountConnectionType": adTAeSCUSecAccountConnectionType,
       "adTAeSCUSecAccountSessionType": adTAeSCUSecAccountSessionType,
       "adTAeSCUSecAccountLoginConnectionSource": adTAeSCUSecAccountLoginConnectionSource,
       "adTAeSCUSecAccountLoginDateTime": adTAeSCUSecAccountLoginDateTime,
       "adTAeSCUSecAccountConnectionPort": adTAeSCUSecAccountConnectionPort,
       "adTAeSCUSecAccountDisconnectSession": adTAeSCUSecAccountDisconnectSession,
       "adTAeSCUAccountExpirationEnabled": adTAeSCUAccountExpirationEnabled,
       "adTAeSCUPasswordAgingEnabled": adTAeSCUPasswordAgingEnabled,
       "adTAeSCUSecuritySnmpAccountMgEnableDisable": adTAeSCUSecuritySnmpAccountMgEnableDisable,
       "adTAeSCUSecAccountAuthenticationMethod": adTAeSCUSecAccountAuthenticationMethod,
       "adTAeSCUSysRADIUsConfig": adTAeSCUSysRADIUsConfig,
       "adTAeScuRADIUSServAuthentication": adTAeScuRADIUSServAuthentication,
       "adTAeScuRadiusTL1Authentication": adTAeScuRadiusTL1Authentication,
       "adTAeScuRadiusAccountAccessLevel": adTAeScuRadiusAccountAccessLevel,
       "adTAeScuRADIUSFallbackMode": adTAeScuRADIUSFallbackMode,
       "adTAeScuRADIUSServerTable": adTAeScuRADIUSServerTable,
       "adTAeScuRADIUSServerEntry": adTAeScuRADIUSServerEntry,
       "adTAeScuRadiusCfgIndex": adTAeScuRadiusCfgIndex,
       "adTAeScuRadiusServerAddress": adTAeScuRadiusServerAddress,
       "adTAeScuRadiusServerPortNumber": adTAeScuRadiusServerPortNumber,
       "adTAeScuRadiusServerSecret": adTAeScuRadiusServerSecret,
       "adTAeScuRADIUSServRetries": adTAeScuRADIUSServRetries,
       "adTAeScuRADIUSServContactTimeOut": adTAeScuRADIUSServContactTimeOut,
       "adTAeScuRadiusServerSequence": adTAeScuRadiusServerSequence,
       "adTAeScuRadiusServerName": adTAeScuRadiusServerName,
       "adTAeScuRadiusServerAddressType": adTAeScuRadiusServerAddressType,
       "adTAeScuRadiusServerInetAddress": adTAeScuRadiusServerInetAddress,
       "adTAeSCUSysPasswordComplexity": adTAeSCUSysPasswordComplexity,
       "adTAeSCUSysEnablePswdComplexity": adTAeSCUSysEnablePswdComplexity,
       "adTAeSCUSysMinPasswordLength": adTAeSCUSysMinPasswordLength,
       "adTAeSCUSysUpperCaseRequired": adTAeSCUSysUpperCaseRequired,
       "adTAeSCUSysLowerCaseRequired": adTAeSCUSysLowerCaseRequired,
       "adTAeSCUSysDigitRequired": adTAeSCUSysDigitRequired,
       "adTAeSCUSysSpecialCharacterRequired": adTAeSCUSysSpecialCharacterRequired,
       "adTAeSCUSysCaseSensitivePassword": adTAeSCUSysCaseSensitivePassword,
       "adTAeSCUSysNullPasswordAccepted": adTAeSCUSysNullPasswordAccepted,
       "adTAeSCUSecPasswordStartEndDigitCheck": adTAeSCUSecPasswordStartEndDigitCheck,
       "adTAeSCUSecLastSixPasswordCheck": adTAeSCUSecLastSixPasswordCheck,
       "adTAeScuAccLockOutSettings": adTAeScuAccLockOutSettings,
       "adTAeScuEnableAccLoginFailureLockOut": adTAeScuEnableAccLoginFailureLockOut,
       "adTAeScuEnableLockOutAlarm": adTAeScuEnableLockOutAlarm,
       "adTAeScuEnableIndefLockOut": adTAeScuEnableIndefLockOut,
       "adTAeScuNumLockOutLoginAttempts": adTAeScuNumLockOutLoginAttempts,
       "adTAeScuLockOutDuration": adTAeScuLockOutDuration,
       "adTAeTrustedClientConfig": adTAeTrustedClientConfig,
       "adTAeTrustedIPClientAccessControl": adTAeTrustedIPClientAccessControl,
       "adTAeTrustedIPClientAccessName": adTAeTrustedIPClientAccessName,
       "adTAeTrustedIPClientTable": adTAeTrustedIPClientTable,
       "adTAeTrustedIPClientEntry": adTAeTrustedIPClientEntry,
       "adTAeTrustedClientStatus": adTAeTrustedClientStatus,
       "adTAeTrustedIPAddress": adTAeTrustedIPAddress,
       "adTAeTrustedIPNetworkBits": adTAeTrustedIPNetworkBits,
       "adTAeTrustedClientResource": adTAeTrustedClientResource,
       "adTAeTrustedInetClientTable": adTAeTrustedInetClientTable,
       "adTAeTrustedInetClientEntry": adTAeTrustedInetClientEntry,
       "adTAeTrustedInetClientStatus": adTAeTrustedInetClientStatus,
       "adTAeTrustedInetAddressType": adTAeTrustedInetAddressType,
       "adTAeTrustedInetNetworkBits": adTAeTrustedInetNetworkBits,
       "adTAeTrustedInetAddress": adTAeTrustedInetAddress,
       "adTAeTrustedInetClientResource": adTAeTrustedInetClientResource,
       "adTAeSCUSysAdvisoryConfig": adTAeSCUSysAdvisoryConfig,
       "adTAeScuEnableMenuAdvisoryWarningMsg": adTAeScuEnableMenuAdvisoryWarningMsg,
       "adTAeScuEnableTL1AdvisoryWarningMsg": adTAeScuEnableTL1AdvisoryWarningMsg,
       "adTAeScuSysSavedTextJustification": adTAeScuSysSavedTextJustification,
       "adTAeScuSavedAdvisoryTable": adTAeScuSavedAdvisoryTable,
       "adTAeScuSavedAdvisoryEntry": adTAeScuSavedAdvisoryEntry,
       "adTAeScuAdvisoryLineIndex": adTAeScuAdvisoryLineIndex,
       "adTAeScuSavedAdvisoryWarning": adTAeScuSavedAdvisoryWarning,
       "adTAeScuSysSaveOrResetEditAdvisoryWarning": adTAeScuSysSaveOrResetEditAdvisoryWarning,
       "adTAeScuSysEditTextJustification": adTAeScuSysEditTextJustification,
       "adTAeScuEditedAdvisoryTable": adTAeScuEditedAdvisoryTable,
       "adTAeScuEditedAdvisoryEntry": adTAeScuEditedAdvisoryEntry,
       "adTAeScuEditedAdvisoryWarning": adTAeScuEditedAdvisoryWarning,
       "adTAeSCUSysBulkDataExportServerConfig": adTAeSCUSysBulkDataExportServerConfig,
       "adTAeSCUSysBulkDataExportHost": adTAeSCUSysBulkDataExportHost,
       "adTAeSCUSysBulkDataExportUserName": adTAeSCUSysBulkDataExportUserName,
       "adTAeSCUSysBulkDataExportPassword": adTAeSCUSysBulkDataExportPassword,
       "adTAeSCUSysBulkDataExportProtocol": adTAeSCUSysBulkDataExportProtocol,
       "adTAeSCUSysBulkDataExportPort": adTAeSCUSysBulkDataExportPort,
       "adTAeSCUSysBulkDataExportPath": adTAeSCUSysBulkDataExportPath,
       "adTAeSCUSecLoginStatTable": adTAeSCUSecLoginStatTable,
       "adTAeSCUSecLoginStatEntry": adTAeSCUSecLoginStatEntry,
       "adTAeSCUSecLoginStatUserID": adTAeSCUSecLoginStatUserID,
       "adTAeSCUSecNumberOfLogins": adTAeSCUSecNumberOfLogins,
       "adTAeSCUSecTotalNumLoginFailures": adTAeSCUSecTotalNumLoginFailures,
       "adTAeSCUSecNumFailuresSinceLastLogin": adTAeSCUSecNumFailuresSinceLastLogin,
       "adTAeSCUSecLastLoginDateTime": adTAeSCUSecLastLoginDateTime,
       "adTAeSCUSecLastConnectionType": adTAeSCUSecLastConnectionType,
       "adTAeSCUSecLastSessionType": adTAeSCUSecLastSessionType,
       "adTAeSCUSecLastIPAddress": adTAeSCUSecLastIPAddress,
       "adTAeSCUSecAdvancedLoginOptions": adTAeSCUSecAdvancedLoginOptions,
       "adTAeSCUSecChallengeKey": adTAeSCUSecChallengeKey,
       "adTAeSCUSecMultiLoginAcct": adTAeSCUSecMultiLoginAcct,
       "adTAeSCUSecRemoteMenuAccessRequired": adTAeSCUSecRemoteMenuAccessRequired,
       "adTAeSCUSysTACACSPlusConfig": adTAeSCUSysTACACSPlusConfig,
       "adTAeScuTACACSPlusTL1Authentication": adTAeScuTACACSPlusTL1Authentication,
       "adTAeScuTACACSPlusServerTable": adTAeScuTACACSPlusServerTable,
       "adTAeScuTACACSPlusServerEntry": adTAeScuTACACSPlusServerEntry,
       "adTAeScuTACACSPlusCfgIndex": adTAeScuTACACSPlusCfgIndex,
       "adTAeScuTACACSPlusServerAddress": adTAeScuTACACSPlusServerAddress,
       "adTAeScuTACACSPlusServerName": adTAeScuTACACSPlusServerName,
       "adTAeScuTACACSPlusServerSecret": adTAeScuTACACSPlusServerSecret,
       "adTAeScuTACACSPlusServerSequence": adTAeScuTACACSPlusServerSequence,
       "adTAeScuTACACSPlusServContactTimeOut": adTAeScuTACACSPlusServContactTimeOut,
       "adTAeScuTACACSPlusServerPort": adTAeScuTACACSPlusServerPort,
       "adTAeScuTACACSPlusServerAddressType": adTAeScuTACACSPlusServerAddressType,
       "adTAeScuTACACSPlusServerInetAddress": adTAeScuTACACSPlusServerInetAddress,
       "adTAeSCUNetworkMgmt": adTAeSCUNetworkMgmt,
       "adTAeSCUNetworkMgmtPortBaudRate": adTAeSCUNetworkMgmtPortBaudRate,
       "adTAeSCUNetworkMgmtPortComMode": adTAeSCUNetworkMgmtPortComMode,
       "adTAeSCUNetworkMgmtPPPSerialPortMode": adTAeSCUNetworkMgmtPPPSerialPortMode,
       "adTAeSCUNetworkMgmtInterbankComMode": adTAeSCUNetworkMgmtInterbankComMode,
       "adTAeSCUNetworkMgmtInterbankComModeWritable": adTAeSCUNetworkMgmtInterbankComModeWritable,
       "adTAeSCUNetworkMgmtSecurityEnable": adTAeSCUNetworkMgmtSecurityEnable,
       "adTAeSCUsDNS": adTAeSCUsDNS,
       "adTAeScuDNSlookupService": adTAeScuDNSlookupService,
       "adTAeScuDNSprimaryIP": adTAeScuDNSprimaryIP,
       "adTAeScuDNSsecondaryIP": adTAeScuDNSsecondaryIP,
       "adTAeScuDNSsearchList": adTAeScuDNSsearchList,
       "ipDNSLookupIpTable": ipDNSLookupIpTable,
       "ipDNSLookupIpTableEntry": ipDNSLookupIpTableEntry,
       "ipDNSLookupIpIndex": ipDNSLookupIpIndex,
       "ipDNSLookupIpInetAddressType": ipDNSLookupIpInetAddressType,
       "ipDNSLookupIpInetAddress": ipDNSLookupIpInetAddress,
       "adTAeSCUFirmwareTFTPConfigMgmt": adTAeSCUFirmwareTFTPConfigMgmt,
       "adTAeScuFirmwareTftpRemoteFileName": adTAeScuFirmwareTftpRemoteFileName,
       "adTAeScuFirmwareTftpServerHostName": adTAeScuFirmwareTftpServerHostName,
       "adTAeScuFirmwareTftpServerIP": adTAeScuFirmwareTftpServerIP,
       "adTAeScuFirmwareTftpCacheExpire": adTAeScuFirmwareTftpCacheExpire,
       "adTAeScuFirmwareTftpInvalidate": adTAeScuFirmwareTftpInvalidate,
       "adTAeScmFirmwareTftpServerInetAddressType": adTAeScmFirmwareTftpServerInetAddressType,
       "adTAeScmFirmwareTftpServerIPInetAddress": adTAeScmFirmwareTftpServerIPInetAddress,
       "adTAeSCUSystemConfigArchiveMgmt": adTAeSCUSystemConfigArchiveMgmt,
       "adTAeScuSCATftpServerHostName": adTAeScuSCATftpServerHostName,
       "adTAeScuSCATftpServerIP": adTAeScuSCATftpServerIP,
       "adTAeScuSCATftpServerIPInetAddressType": adTAeScuSCATftpServerIPInetAddressType,
       "adTAeScuSCATftpServerHostNameInetAddress": adTAeScuSCATftpServerHostNameInetAddress,
       "adTAeSCUSCAControl": adTAeSCUSCAControl,
       "adTAeScuSCAFileName": adTAeScuSCAFileName,
       "adTAeScuSCAInitiateSave": adTAeScuSCAInitiateSave,
       "adTAeScuSCAInitiateRestore": adTAeScuSCAInitiateRestore,
       "adTAeScuSCAProvItemChanged": adTAeScuSCAProvItemChanged,
       "adTAeScuSCAPresentCards": adTAeScuSCAPresentCards,
       "adTAeScuSCASlotsWithProvData": adTAeScuSCASlotsWithProvData,
       "adTAeScuSCASlotsInSCA": adTAeScuSCASlotsInSCA,
       "adTAeScuSCASlotsWithProvDataInSCA": adTAeScuSCASlotsWithProvDataInSCA,
       "adTAeSCUSCAOperationStatusTable": adTAeSCUSCAOperationStatusTable,
       "adTAeSCUSCAOperationStatusEntry": adTAeSCUSCAOperationStatusEntry,
       "adTAeScuSCAOperationStatus": adTAeScuSCAOperationStatus,
       "adTAeSCUSCAAutoSaveMgmt": adTAeSCUSCAAutoSaveMgmt,
       "adTAeScuSCAAutoSave": adTAeScuSCAAutoSave,
       "adTAeScuSCAAutoSaveRetries": adTAeScuSCAAutoSaveRetries,
       "adTAeScuSCAAutoSaveIfChanged": adTAeScuSCAAutoSaveIfChanged,
       "adTAeScuSCAAutoSaveFileNamePrefix": adTAeScuSCAAutoSaveFileNamePrefix,
       "adTAeScuSCAAutoSaveFileNameSuffix": adTAeScuSCAAutoSaveFileNameSuffix,
       "adTAeScuSCAAutoSaveInstances": adTAeScuSCAAutoSaveInstances,
       "adTAeScuSCAAutoSaveHoursAfter": adTAeScuSCAAutoSaveHoursAfter,
       "adTAeScuSCAAutoSaveMinutesAfter": adTAeScuSCAAutoSaveMinutesAfter,
       "adTAeScuSCADateTimeLastAutoSave": adTAeScuSCADateTimeLastAutoSave,
       "adTAeScuSCADateTimeNextAutoSave": adTAeScuSCADateTimeNextAutoSave,
       "adTAeSCUSCARestoreMgmt": adTAeSCUSCARestoreMgmt,
       "adTAeScuSCAoptRestoreESCU": adTAeScuSCAoptRestoreESCU,
       "adTAeScuSCAoptRestoreSCA": adTAeScuSCAoptRestoreSCA,
       "adTAeScuSCAoptRestoreNetwork": adTAeScuSCAoptRestoreNetwork,
       "adTAeScuSCAoptRestoreNetworkInterface": adTAeScuSCAoptRestoreNetworkInterface,
       "adTAeScuSCAoptRestoreSNMP": adTAeScuSCAoptRestoreSNMP,
       "adTAeScuSCAoptRestoreSecurity": adTAeScuSCAoptRestoreSecurity,
       "adTAeScuSCAoptRestoreLineCard": adTAeScuSCAoptRestoreLineCard,
       "adTAeScuSCAoptRestoreInServiceLineCard": adTAeScuSCAoptRestoreInServiceLineCard,
       "adTAeScuSCAoptRestoreEmptySlot": adTAeScuSCAoptRestoreEmptySlot,
       "adTAeScuSCAoptRestoreCardBitmask": adTAeScuSCAoptRestoreCardBitmask,
       "adTAeScuSCADateTimeSaveInvoked": adTAeScuSCADateTimeSaveInvoked,
       "adTAeScuSCACardsRestoredBitmask": adTAeScuSCACardsRestoredBitmask,
       "adTAeScuSCACardsNotRestoredBitmask": adTAeScuSCACardsNotRestoredBitmask,
       "adTAeScuSCACardsExcludedBitmask": adTAeScuSCACardsExcludedBitmask,
       "adTAeScuSCARestoreCardErrorsBitmask": adTAeScuSCARestoreCardErrorsBitmask,
       "adTAeSCUSystemLog": adTAeSCUSystemLog,
       "adTAeSCUSystemLogAlarm": adTAeSCUSystemLogAlarm,
       "adTAeSCUSystemLogPercentFull": adTAeSCUSystemLogPercentFull,
       "adTAeSCUSystemLogCount": adTAeSCUSystemLogCount,
       "adTAeSCUSystemSummReport": adTAeSCUSystemSummReport,
       "adTAeSCUSystemEnableDetail": adTAeSCUSystemEnableDetail,
       "adTAeSCUSystemLogFailureDescription": adTAeSCUSystemLogFailureDescription,
       "adTAeSCUSystemLogTable": adTAeSCUSystemLogTable,
       "adTAeSCUSystemLogEntry": adTAeSCUSystemLogEntry,
       "adTAeSCUSystemLogIndex": adTAeSCUSystemLogIndex,
       "adTAeSCUSystemLogDescription": adTAeSCUSystemLogDescription,
       "adTAeScuTL1ActivityLog": adTAeScuTL1ActivityLog,
       "adTAeScuResetTL1Log": adTAeScuResetTL1Log,
       "adTAeScuTL1ActivityLogTable": adTAeScuTL1ActivityLogTable,
       "adTAeScuTL1ActivityLogEntry": adTAeScuTL1ActivityLogEntry,
       "adTAeSCUTL1LogIndex": adTAeSCUTL1LogIndex,
       "adTAeScuTL1ActivityLogDescription": adTAeScuTL1ActivityLogDescription}
)
