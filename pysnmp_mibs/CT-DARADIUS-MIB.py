# SNMP MIB module (CT-DARADIUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/cabletron/CT-DARADIUS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:55:31 2025
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

(cabletron,) = mibBuilder.importSymbols(
    "CTRON-OIDS",
    "cabletron")

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

_CtSSA_ObjectIdentity = ObjectIdentity
ctSSA = _CtSSA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4497)
)
_DaRadius_ObjectIdentity = ObjectIdentity
daRadius = _DaRadius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4497, 24)
)
_DaRadiusConfig_ObjectIdentity = ObjectIdentity
daRadiusConfig = _DaRadiusConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4497, 24, 1)
)
_DaRadiusGeneralConfig_ObjectIdentity = ObjectIdentity
daRadiusGeneralConfig = _DaRadiusGeneralConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4497, 24, 1, 1)
)


class _DaRadiusgcEnabled_Type(Integer32):
    """Custom type daRadiusgcEnabled based on Integer32"""
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


_DaRadiusgcEnabled_Type.__name__ = "Integer32"
_DaRadiusgcEnabled_Object = MibScalar
daRadiusgcEnabled = _DaRadiusgcEnabled_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 24, 1, 1, 1),
    _DaRadiusgcEnabled_Type()
)
daRadiusgcEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daRadiusgcEnabled.setStatus("mandatory")
_DaRadiusgcAuthNumRetries_Type = Integer32
_DaRadiusgcAuthNumRetries_Object = MibScalar
daRadiusgcAuthNumRetries = _DaRadiusgcAuthNumRetries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 24, 1, 1, 2),
    _DaRadiusgcAuthNumRetries_Type()
)
daRadiusgcAuthNumRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daRadiusgcAuthNumRetries.setStatus("mandatory")
_DaRadiusgcAuthSecsBtwnRetries_Type = Integer32
_DaRadiusgcAuthSecsBtwnRetries_Object = MibScalar
daRadiusgcAuthSecsBtwnRetries = _DaRadiusgcAuthSecsBtwnRetries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 24, 1, 1, 3),
    _DaRadiusgcAuthSecsBtwnRetries_Type()
)
daRadiusgcAuthSecsBtwnRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daRadiusgcAuthSecsBtwnRetries.setStatus("mandatory")
_DaRadiusgcAcctNumRetries_Type = Integer32
_DaRadiusgcAcctNumRetries_Object = MibScalar
daRadiusgcAcctNumRetries = _DaRadiusgcAcctNumRetries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 24, 1, 1, 4),
    _DaRadiusgcAcctNumRetries_Type()
)
daRadiusgcAcctNumRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daRadiusgcAcctNumRetries.setStatus("mandatory")
_GcAcctSecsBtwnRetries_Type = Integer32
_GcAcctSecsBtwnRetries_Object = MibScalar
gcAcctSecsBtwnRetries = _GcAcctSecsBtwnRetries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 24, 1, 1, 5),
    _GcAcctSecsBtwnRetries_Type()
)
gcAcctSecsBtwnRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gcAcctSecsBtwnRetries.setStatus("mandatory")
_DaRadiusServerCfgTable_Object = MibTable
daRadiusServerCfgTable = _DaRadiusServerCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 24, 1, 2)
)
if mibBuilder.loadTexts:
    daRadiusServerCfgTable.setStatus("mandatory")
_DaRadiusServerCfgEntry_Object = MibTableRow
daRadiusServerCfgEntry = _DaRadiusServerCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 24, 1, 2, 1)
)
daRadiusServerCfgEntry.setIndexNames(
    (0, "CT-DARADIUS-MIB", "scIndex"),
)
if mibBuilder.loadTexts:
    daRadiusServerCfgEntry.setStatus("mandatory")


class _ScIndex_Type(Integer32):
    """Custom type scIndex based on Integer32"""
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
        *(("primaryAuthentication", 1),
          ("secondaryAuthentication", 2),
          ("primaryAccounting", 3),
          ("secondaryAccounting", 4))
    )


_ScIndex_Type.__name__ = "Integer32"
_ScIndex_Object = MibTableColumn
scIndex = _ScIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 24, 1, 2, 1, 1),
    _ScIndex_Type()
)
scIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scIndex.setStatus("mandatory")


class _ScStatus_Type(Integer32):
    """Custom type scStatus based on Integer32"""
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


_ScStatus_Type.__name__ = "Integer32"
_ScStatus_Object = MibTableColumn
scStatus = _ScStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 24, 1, 2, 1, 2),
    _ScStatus_Type()
)
scStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scStatus.setStatus("mandatory")
_ScIpAddress_Type = IpAddress
_ScIpAddress_Object = MibTableColumn
scIpAddress = _ScIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 24, 1, 2, 1, 3),
    _ScIpAddress_Type()
)
scIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scIpAddress.setStatus("mandatory")
_ScSharedSecret_Type = DisplayString
_ScSharedSecret_Object = MibTableColumn
scSharedSecret = _ScSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 24, 1, 2, 1, 4),
    _ScSharedSecret_Type()
)
scSharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scSharedSecret.setStatus("mandatory")
_ScUdpPort_Type = Integer32
_ScUdpPort_Object = MibTableColumn
scUdpPort = _ScUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 24, 1, 2, 1, 5),
    _ScUdpPort_Type()
)
scUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scUdpPort.setStatus("mandatory")
_DaRadiusStats_ObjectIdentity = ObjectIdentity
daRadiusStats = _DaRadiusStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4497, 24, 2)
)
_DaRadiusGeneralStats_ObjectIdentity = ObjectIdentity
daRadiusGeneralStats = _DaRadiusGeneralStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4497, 24, 2, 1)
)
_GsInDiscards_Type = Integer32
_GsInDiscards_Object = MibScalar
gsInDiscards = _GsInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 24, 2, 1, 1),
    _GsInDiscards_Type()
)
gsInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsInDiscards.setStatus("mandatory")
_GsInErrors_Type = Integer32
_GsInErrors_Object = MibScalar
gsInErrors = _GsInErrors_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 24, 2, 1, 2),
    _GsInErrors_Type()
)
gsInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsInErrors.setStatus("mandatory")
_DaRadiusServerStatsTable_Object = MibTable
daRadiusServerStatsTable = _DaRadiusServerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 24, 2, 2)
)
if mibBuilder.loadTexts:
    daRadiusServerStatsTable.setStatus("mandatory")
_DaRadiusServerStatsEntry_Object = MibTableRow
daRadiusServerStatsEntry = _DaRadiusServerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 24, 2, 2, 1)
)
daRadiusServerStatsEntry.setIndexNames(
    (0, "CT-DARADIUS-MIB", "ssIndex"),
)
if mibBuilder.loadTexts:
    daRadiusServerStatsEntry.setStatus("mandatory")


class _SsIndex_Type(Integer32):
    """Custom type ssIndex based on Integer32"""
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
        *(("primaryAuthentication", 1),
          ("secondaryAuthentication", 2),
          ("primaryAccounting", 3),
          ("secondaryAccounting", 4))
    )


_SsIndex_Type.__name__ = "Integer32"
_SsIndex_Object = MibTableColumn
ssIndex = _SsIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 24, 2, 2, 1, 1),
    _SsIndex_Type()
)
ssIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssIndex.setStatus("mandatory")
_SsInPkts_Type = Integer32
_SsInPkts_Object = MibTableColumn
ssInPkts = _SsInPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 24, 2, 2, 1, 2),
    _SsInPkts_Type()
)
ssInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssInPkts.setStatus("mandatory")
_SsInDiscards_Type = Integer32
_SsInDiscards_Object = MibTableColumn
ssInDiscards = _SsInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 24, 2, 2, 1, 3),
    _SsInDiscards_Type()
)
ssInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssInDiscards.setStatus("mandatory")
_SsInErrors_Type = Integer32
_SsInErrors_Object = MibTableColumn
ssInErrors = _SsInErrors_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 24, 2, 2, 1, 4),
    _SsInErrors_Type()
)
ssInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssInErrors.setStatus("mandatory")
_SsOutPkts_Type = Integer32
_SsOutPkts_Object = MibTableColumn
ssOutPkts = _SsOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 24, 2, 2, 1, 5),
    _SsOutPkts_Type()
)
ssOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssOutPkts.setStatus("mandatory")
_SsOutErrors_Type = Integer32
_SsOutErrors_Object = MibTableColumn
ssOutErrors = _SsOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 24, 2, 2, 1, 6),
    _SsOutErrors_Type()
)
ssOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssOutErrors.setStatus("mandatory")
_SsResponseTimeouts_Type = Integer32
_SsResponseTimeouts_Object = MibTableColumn
ssResponseTimeouts = _SsResponseTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 24, 2, 2, 1, 7),
    _SsResponseTimeouts_Type()
)
ssResponseTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssResponseTimeouts.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CT-DARADIUS-MIB",
    **{"ctSSA": ctSSA,
       "daRadius": daRadius,
       "daRadiusConfig": daRadiusConfig,
       "daRadiusGeneralConfig": daRadiusGeneralConfig,
       "daRadiusgcEnabled": daRadiusgcEnabled,
       "daRadiusgcAuthNumRetries": daRadiusgcAuthNumRetries,
       "daRadiusgcAuthSecsBtwnRetries": daRadiusgcAuthSecsBtwnRetries,
       "daRadiusgcAcctNumRetries": daRadiusgcAcctNumRetries,
       "gcAcctSecsBtwnRetries": gcAcctSecsBtwnRetries,
       "daRadiusServerCfgTable": daRadiusServerCfgTable,
       "daRadiusServerCfgEntry": daRadiusServerCfgEntry,
       "scIndex": scIndex,
       "scStatus": scStatus,
       "scIpAddress": scIpAddress,
       "scSharedSecret": scSharedSecret,
       "scUdpPort": scUdpPort,
       "daRadiusStats": daRadiusStats,
       "daRadiusGeneralStats": daRadiusGeneralStats,
       "gsInDiscards": gsInDiscards,
       "gsInErrors": gsInErrors,
       "daRadiusServerStatsTable": daRadiusServerStatsTable,
       "daRadiusServerStatsEntry": daRadiusServerStatsEntry,
       "ssIndex": ssIndex,
       "ssInPkts": ssInPkts,
       "ssInDiscards": ssInDiscards,
       "ssInErrors": ssInErrors,
       "ssOutPkts": ssOutPkts,
       "ssOutErrors": ssOutErrors,
       "ssResponseTimeouts": ssResponseTimeouts}
)
