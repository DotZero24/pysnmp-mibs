# SNMP MIB module (CPQNODE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/CPQNODE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:38:37 2025
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

(cpqHeTemperatureChassis,
 cpqHeTemperatureLocale,
 cpqHeThermalDegradedAction) = mibBuilder.importSymbols(
    "CPQHLTH-MIB",
    "cpqHeTemperatureChassis",
    "cpqHeTemperatureLocale",
    "cpqHeThermalDegradedAction")

(compaq,
 cpqHoTrapFlags) = mibBuilder.importSymbols(
    "CPQHOST-MIB",
    "compaq",
    "cpqHoTrapFlags")

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
 NotificationType,
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
    "NotificationType",
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

_CpqNode_ObjectIdentity = ObjectIdentity
cpqNode = _CpqNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 20)
)
_CpqNodeFix_ObjectIdentity = ObjectIdentity
cpqNodeFix = _CpqNodeFix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 20, 2)
)
_CpqNodeComponent_ObjectIdentity = ObjectIdentity
cpqNodeComponent = _CpqNodeComponent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 20, 2, 1)
)
_CpqNodeCart_Type = Integer32
_CpqNodeCart_Object = MibScalar
cpqNodeCart = _CpqNodeCart_Object(
    (1, 3, 6, 1, 4, 1, 232, 20, 2, 1, 1),
    _CpqNodeCart_Type()
)
cpqNodeCart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNodeCart.setStatus("mandatory")
_CpqNodeNode_Type = Integer32
_CpqNodeNode_Object = MibScalar
cpqNodeNode = _CpqNodeNode_Object(
    (1, 3, 6, 1, 4, 1, 232, 20, 2, 1, 2),
    _CpqNodeNode_Type()
)
cpqNodeNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNodeNode.setStatus("mandatory")


class _CpqNodeType_Type(Integer32):
    """Custom type cpqNodeType based on Integer32"""
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
        *(("cartridge", 0),
          ("node", 1),
          ("switch", 2),
          ("unknown", 3))
    )


_CpqNodeType_Type.__name__ = "Integer32"
_CpqNodeType_Object = MibScalar
cpqNodeType = _CpqNodeType_Object(
    (1, 3, 6, 1, 4, 1, 232, 20, 2, 1, 3),
    _CpqNodeType_Type()
)
cpqNodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNodeType.setStatus("mandatory")


class _CpqNodeUUID_Type(DisplayString):
    """Custom type cpqNodeUUID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 36),
    )


_CpqNodeUUID_Type.__name__ = "DisplayString"
_CpqNodeUUID_Object = MibScalar
cpqNodeUUID = _CpqNodeUUID_Object(
    (1, 3, 6, 1, 4, 1, 232, 20, 2, 1, 4),
    _CpqNodeUUID_Type()
)
cpqNodeUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNodeUUID.setStatus("mandatory")


class _CpqNodeSerial_Type(DisplayString):
    """Custom type cpqNodeSerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CpqNodeSerial_Type.__name__ = "DisplayString"
_CpqNodeSerial_Object = MibScalar
cpqNodeSerial = _CpqNodeSerial_Object(
    (1, 3, 6, 1, 4, 1, 232, 20, 2, 1, 5),
    _CpqNodeSerial_Type()
)
cpqNodeSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNodeSerial.setStatus("mandatory")
_CpqNodeMac1_Type = DisplayString
_CpqNodeMac1_Object = MibScalar
cpqNodeMac1 = _CpqNodeMac1_Object(
    (1, 3, 6, 1, 4, 1, 232, 20, 2, 1, 6),
    _CpqNodeMac1_Type()
)
cpqNodeMac1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNodeMac1.setStatus("deprecated")
_CpqNodeMac2_Type = DisplayString
_CpqNodeMac2_Object = MibScalar
cpqNodeMac2 = _CpqNodeMac2_Object(
    (1, 3, 6, 1, 4, 1, 232, 20, 2, 1, 7),
    _CpqNodeMac2_Type()
)
cpqNodeMac2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNodeMac2.setStatus("deprecated")
_CpqNodeMac3_Type = DisplayString
_CpqNodeMac3_Object = MibScalar
cpqNodeMac3 = _CpqNodeMac3_Object(
    (1, 3, 6, 1, 4, 1, 232, 20, 2, 1, 8),
    _CpqNodeMac3_Type()
)
cpqNodeMac3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNodeMac3.setStatus("deprecated")
_CpqNodeMac4_Type = DisplayString
_CpqNodeMac4_Object = MibScalar
cpqNodeMac4 = _CpqNodeMac4_Object(
    (1, 3, 6, 1, 4, 1, 232, 20, 2, 1, 9),
    _CpqNodeMac4_Type()
)
cpqNodeMac4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNodeMac4.setStatus("deprecated")


class _CpqNodeErrorMessage_Type(DisplayString):
    """Custom type cpqNodeErrorMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CpqNodeErrorMessage_Type.__name__ = "DisplayString"
_CpqNodeErrorMessage_Object = MibScalar
cpqNodeErrorMessage = _CpqNodeErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 232, 20, 2, 1, 10),
    _CpqNodeErrorMessage_Type()
)
cpqNodeErrorMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqNodeErrorMessage.setStatus("mandatory")

# Managed Objects groups


# Notification objects

cpqNodeTemperatureDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 23001)
)
cpqNodeTemperatureDegraded.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQHLTH-MIB", "cpqHeThermalDegradedAction"),
        ("CPQHLTH-MIB", "cpqHeTemperatureChassis"),
        ("CPQHLTH-MIB", "cpqHeTemperatureLocale"),
        ("CPQNODE-MIB", "cpqNodeCart"),
        ("CPQNODE-MIB", "cpqNodeNode"),
        ("CPQNODE-MIB", "cpqNodeType"),
        ("CPQNODE-MIB", "cpqNodeUUID"),
        ("CPQNODE-MIB", "cpqNodeSerial"),
        ("CPQNODE-MIB", "cpqNodeMac1"),
        ("CPQNODE-MIB", "cpqNodeMac2"),
        ("CPQNODE-MIB", "cpqNodeMac3"),
        ("CPQNODE-MIB", "cpqNodeMac4"))
)
if mibBuilder.loadTexts:
    cpqNodeTemperatureDegraded.setStatus(
        ""
    )

cpqNodeTemperatureOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 23002)
)
cpqNodeTemperatureOk.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQHLTH-MIB", "cpqHeTemperatureChassis"),
        ("CPQHLTH-MIB", "cpqHeTemperatureLocale"),
        ("CPQNODE-MIB", "cpqNodeCart"),
        ("CPQNODE-MIB", "cpqNodeNode"),
        ("CPQNODE-MIB", "cpqNodeType"),
        ("CPQNODE-MIB", "cpqNodeUUID"),
        ("CPQNODE-MIB", "cpqNodeSerial"),
        ("CPQNODE-MIB", "cpqNodeMac1"),
        ("CPQNODE-MIB", "cpqNodeMac2"),
        ("CPQNODE-MIB", "cpqNodeMac3"),
        ("CPQNODE-MIB", "cpqNodeMac4"))
)
if mibBuilder.loadTexts:
    cpqNodeTemperatureOk.setStatus(
        ""
    )

cpqNodeTemperatureFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 23003)
)
cpqNodeTemperatureFailed.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQHLTH-MIB", "cpqHeThermalDegradedAction"),
        ("CPQHLTH-MIB", "cpqHeTemperatureChassis"),
        ("CPQHLTH-MIB", "cpqHeTemperatureLocale"),
        ("CPQNODE-MIB", "cpqNodeCart"),
        ("CPQNODE-MIB", "cpqNodeNode"),
        ("CPQNODE-MIB", "cpqNodeType"),
        ("CPQNODE-MIB", "cpqNodeUUID"),
        ("CPQNODE-MIB", "cpqNodeSerial"),
        ("CPQNODE-MIB", "cpqNodeMac1"),
        ("CPQNODE-MIB", "cpqNodeMac2"),
        ("CPQNODE-MIB", "cpqNodeMac3"),
        ("CPQNODE-MIB", "cpqNodeMac4"))
)
if mibBuilder.loadTexts:
    cpqNodeTemperatureFailed.setStatus(
        ""
    )

cpqNodeErrorEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 23004)
)
cpqNodeErrorEvent.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQNODE-MIB", "cpqNodeErrorMessage"),
        ("CPQNODE-MIB", "cpqNodeCart"),
        ("CPQNODE-MIB", "cpqNodeNode"),
        ("CPQNODE-MIB", "cpqNodeType"),
        ("CPQNODE-MIB", "cpqNodeUUID"),
        ("CPQNODE-MIB", "cpqNodeSerial"),
        ("CPQNODE-MIB", "cpqNodeMac1"),
        ("CPQNODE-MIB", "cpqNodeMac2"),
        ("CPQNODE-MIB", "cpqNodeMac3"),
        ("CPQNODE-MIB", "cpqNodeMac4"))
)
if mibBuilder.loadTexts:
    cpqNodeErrorEvent.setStatus(
        ""
    )

cpqNodePowerOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 23010)
)
cpqNodePowerOn.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQNODE-MIB", "cpqNodeCart"),
        ("CPQNODE-MIB", "cpqNodeNode"),
        ("CPQNODE-MIB", "cpqNodeType"),
        ("CPQNODE-MIB", "cpqNodeUUID"),
        ("CPQNODE-MIB", "cpqNodeSerial"),
        ("CPQNODE-MIB", "cpqNodeMac1"),
        ("CPQNODE-MIB", "cpqNodeMac2"),
        ("CPQNODE-MIB", "cpqNodeMac3"),
        ("CPQNODE-MIB", "cpqNodeMac4"))
)
if mibBuilder.loadTexts:
    cpqNodePowerOn.setStatus(
        ""
    )

cpqNodePowerOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 23011)
)
cpqNodePowerOff.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQNODE-MIB", "cpqNodeCart"),
        ("CPQNODE-MIB", "cpqNodeNode"),
        ("CPQNODE-MIB", "cpqNodeType"),
        ("CPQNODE-MIB", "cpqNodeUUID"),
        ("CPQNODE-MIB", "cpqNodeSerial"),
        ("CPQNODE-MIB", "cpqNodeMac1"),
        ("CPQNODE-MIB", "cpqNodeMac2"),
        ("CPQNODE-MIB", "cpqNodeMac3"),
        ("CPQNODE-MIB", "cpqNodeMac4"))
)
if mibBuilder.loadTexts:
    cpqNodePowerOff.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CPQNODE-MIB",
    **{"cpqNodeTemperatureDegraded": cpqNodeTemperatureDegraded,
       "cpqNodeTemperatureOk": cpqNodeTemperatureOk,
       "cpqNodeTemperatureFailed": cpqNodeTemperatureFailed,
       "cpqNodeErrorEvent": cpqNodeErrorEvent,
       "cpqNodePowerOn": cpqNodePowerOn,
       "cpqNodePowerOff": cpqNodePowerOff,
       "cpqNode": cpqNode,
       "cpqNodeFix": cpqNodeFix,
       "cpqNodeComponent": cpqNodeComponent,
       "cpqNodeCart": cpqNodeCart,
       "cpqNodeNode": cpqNodeNode,
       "cpqNodeType": cpqNodeType,
       "cpqNodeUUID": cpqNodeUUID,
       "cpqNodeSerial": cpqNodeSerial,
       "cpqNodeMac1": cpqNodeMac1,
       "cpqNodeMac2": cpqNodeMac2,
       "cpqNodeMac3": cpqNodeMac3,
       "cpqNodeMac4": cpqNodeMac4,
       "cpqNodeErrorMessage": cpqNodeErrorMessage}
)
