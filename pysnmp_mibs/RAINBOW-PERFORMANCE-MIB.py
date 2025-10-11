# SNMP MIB module (RAINBOW-PERFORMANCE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/alvarion/RAINBOW-PERFORMANCE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:07:02 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(Modulation,
 rainbow) = mibBuilder.importSymbols(
    "RAINBOW-MIB",
    "Modulation",
    "rainbow")

(rbServiceID,) = mibBuilder.importSymbols(
    "RAINBOW-SERVICES-MIB",
    "rbServiceID")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

rbPerformance = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4)
)
if mibBuilder.loadTexts:
    rbPerformance.setRevisions(
        ("2006-06-06 15:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RbPMServ_ObjectIdentity = ObjectIdentity
rbPMServ = _RbPMServ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 1)
)
_RbPMCGServConnTable_Object = MibTable
rbPMCGServConnTable = _RbPMCGServConnTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 1, 1)
)
if mibBuilder.loadTexts:
    rbPMCGServConnTable.setStatus("deprecated")
_RbPMCGServConnEntry_Object = MibTableRow
rbPMCGServConnEntry = _RbPMCGServConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 1, 1, 1)
)
rbPMCGServConnEntry.setIndexNames(
    (0, "RAINBOW-SERVICES-MIB", "rbServiceID"),
    (0, "RAINBOW-PERFORMANCE-MIB", "rbPMCGConnDirection"),
)
if mibBuilder.loadTexts:
    rbPMCGServConnEntry.setStatus("deprecated")


class _RbPMCGConnDirection_Type(Integer32):
    """Custom type rbPMCGConnDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("downLink", 1),
          ("upLink", 2))
    )


_RbPMCGConnDirection_Type.__name__ = "Integer32"
_RbPMCGConnDirection_Object = MibTableColumn
rbPMCGConnDirection = _RbPMCGConnDirection_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 1, 1, 1, 1),
    _RbPMCGConnDirection_Type()
)
rbPMCGConnDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPMCGConnDirection.setStatus("deprecated")
_RbPMCGConnByteReq_Type = Counter32
_RbPMCGConnByteReq_Object = MibTableColumn
rbPMCGConnByteReq = _RbPMCGConnByteReq_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 1, 1, 1, 2),
    _RbPMCGConnByteReq_Type()
)
rbPMCGConnByteReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPMCGConnByteReq.setStatus("deprecated")
_RbPMCGConnByteTx_Type = Counter32
_RbPMCGConnByteTx_Object = MibTableColumn
rbPMCGConnByteTx = _RbPMCGConnByteTx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 1, 1, 1, 3),
    _RbPMCGConnByteTx_Type()
)
rbPMCGConnByteTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPMCGConnByteTx.setStatus("deprecated")
_RbPMCGConnByteRetTx_Type = Counter32
_RbPMCGConnByteRetTx_Object = MibTableColumn
rbPMCGConnByteRetTx = _RbPMCGConnByteRetTx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 1, 1, 1, 4),
    _RbPMCGConnByteRetTx_Type()
)
rbPMCGConnByteRetTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPMCGConnByteRetTx.setStatus("deprecated")
_RbPMCGConnByteDropped_Type = Counter32
_RbPMCGConnByteDropped_Object = MibTableColumn
rbPMCGConnByteDropped = _RbPMCGConnByteDropped_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 1, 1, 1, 5),
    _RbPMCGConnByteDropped_Type()
)
rbPMCGConnByteDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPMCGConnByteDropped.setStatus("deprecated")
_RbPMCGConnByteDiscarded_Type = Counter32
_RbPMCGConnByteDiscarded_Object = MibTableColumn
rbPMCGConnByteDiscarded = _RbPMCGConnByteDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 1, 1, 1, 6),
    _RbPMCGConnByteDiscarded_Type()
)
rbPMCGConnByteDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPMCGConnByteDiscarded.setStatus("deprecated")
_RbPMCGConnPktsReq_Type = Counter32
_RbPMCGConnPktsReq_Object = MibTableColumn
rbPMCGConnPktsReq = _RbPMCGConnPktsReq_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 1, 1, 1, 7),
    _RbPMCGConnPktsReq_Type()
)
rbPMCGConnPktsReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPMCGConnPktsReq.setStatus("deprecated")
_RbPMCGConnPktsTx_Type = Counter32
_RbPMCGConnPktsTx_Object = MibTableColumn
rbPMCGConnPktsTx = _RbPMCGConnPktsTx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 1, 1, 1, 8),
    _RbPMCGConnPktsTx_Type()
)
rbPMCGConnPktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPMCGConnPktsTx.setStatus("deprecated")
_RbPMCGConnPktsDropped_Type = Counter32
_RbPMCGConnPktsDropped_Object = MibTableColumn
rbPMCGConnPktsDropped = _RbPMCGConnPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 1, 1, 1, 9),
    _RbPMCGConnPktsDropped_Type()
)
rbPMCGConnPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPMCGConnPktsDropped.setStatus("deprecated")
_RbPMCGConnPktsDiscarded_Type = Counter32
_RbPMCGConnPktsDiscarded_Object = MibTableColumn
rbPMCGConnPktsDiscarded = _RbPMCGConnPktsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 1, 1, 1, 10),
    _RbPMCGConnPktsDiscarded_Type()
)
rbPMCGConnPktsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPMCGConnPktsDiscarded.setStatus("deprecated")
_RbPMCGConnAvarageDelay_Type = Integer32
_RbPMCGConnAvarageDelay_Object = MibTableColumn
rbPMCGConnAvarageDelay = _RbPMCGConnAvarageDelay_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 1, 1, 1, 11),
    _RbPMCGConnAvarageDelay_Type()
)
rbPMCGConnAvarageDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPMCGConnAvarageDelay.setStatus("deprecated")
_RbPMCGConnStandardDeviationDelay_Type = Integer32
_RbPMCGConnStandardDeviationDelay_Object = MibTableColumn
rbPMCGConnStandardDeviationDelay = _RbPMCGConnStandardDeviationDelay_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 1, 1, 1, 12),
    _RbPMCGConnStandardDeviationDelay_Type()
)
rbPMCGConnStandardDeviationDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPMCGConnStandardDeviationDelay.setStatus("deprecated")
_RbPMCGConnMaxDelay_Type = Integer32
_RbPMCGConnMaxDelay_Object = MibTableColumn
rbPMCGConnMaxDelay = _RbPMCGConnMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 1, 1, 1, 13),
    _RbPMCGConnMaxDelay_Type()
)
rbPMCGConnMaxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPMCGConnMaxDelay.setStatus("deprecated")
_RbPMCGConnPerSucsGrant_Type = Counter32
_RbPMCGConnPerSucsGrant_Object = MibTableColumn
rbPMCGConnPerSucsGrant = _RbPMCGConnPerSucsGrant_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 1, 1, 1, 14),
    _RbPMCGConnPerSucsGrant_Type()
)
rbPMCGConnPerSucsGrant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPMCGConnPerSucsGrant.setStatus("deprecated")
_RbPMCGConnAvgGrantInt_Type = Counter32
_RbPMCGConnAvgGrantInt_Object = MibTableColumn
rbPMCGConnAvgGrantInt = _RbPMCGConnAvgGrantInt_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 1, 1, 1, 15),
    _RbPMCGConnAvgGrantInt_Type()
)
rbPMCGConnAvgGrantInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPMCGConnAvgGrantInt.setStatus("deprecated")
_RbPMCGConnMaxGrantInt_Type = Counter32
_RbPMCGConnMaxGrantInt_Object = MibTableColumn
rbPMCGConnMaxGrantInt = _RbPMCGConnMaxGrantInt_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 1, 1, 1, 16),
    _RbPMCGConnMaxGrantInt_Type()
)
rbPMCGConnMaxGrantInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPMCGConnMaxGrantInt.setStatus("deprecated")
_RbPMCGConnAvgIntArvTime_Type = Counter32
_RbPMCGConnAvgIntArvTime_Object = MibTableColumn
rbPMCGConnAvgIntArvTime = _RbPMCGConnAvgIntArvTime_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 1, 1, 1, 17),
    _RbPMCGConnAvgIntArvTime_Type()
)
rbPMCGConnAvgIntArvTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPMCGConnAvgIntArvTime.setStatus("deprecated")
_RbPMCGConnMaxIntArvTime_Type = Counter32
_RbPMCGConnMaxIntArvTime_Object = MibTableColumn
rbPMCGConnMaxIntArvTime = _RbPMCGConnMaxIntArvTime_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 1, 1, 1, 18),
    _RbPMCGConnMaxIntArvTime_Type()
)
rbPMCGConnMaxIntArvTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPMCGConnMaxIntArvTime.setStatus("deprecated")
_RbPMCGConnMinIntArvTime_Type = Counter32
_RbPMCGConnMinIntArvTime_Object = MibTableColumn
rbPMCGConnMinIntArvTime = _RbPMCGConnMinIntArvTime_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 1, 1, 1, 19),
    _RbPMCGConnMinIntArvTime_Type()
)
rbPMCGConnMinIntArvTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPMCGConnMinIntArvTime.setStatus("deprecated")
_RbPMCGConnAvgSDUDropRate_Type = Counter32
_RbPMCGConnAvgSDUDropRate_Object = MibTableColumn
rbPMCGConnAvgSDUDropRate = _RbPMCGConnAvgSDUDropRate_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 1, 1, 1, 20),
    _RbPMCGConnAvgSDUDropRate_Type()
)
rbPMCGConnAvgSDUDropRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPMCGConnAvgSDUDropRate.setStatus("deprecated")
_RbPMCGConnResetCounters_Type = Integer32
_RbPMCGConnResetCounters_Object = MibTableColumn
rbPMCGConnResetCounters = _RbPMCGConnResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 1, 1, 1, 21),
    _RbPMCGConnResetCounters_Type()
)
rbPMCGConnResetCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbPMCGConnResetCounters.setStatus("deprecated")
_RbPMServConnTable_Object = MibTable
rbPMServConnTable = _RbPMServConnTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 1, 2)
)
if mibBuilder.loadTexts:
    rbPMServConnTable.setStatus("current")
_RbPMServConnEntry_Object = MibTableRow
rbPMServConnEntry = _RbPMServConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 1, 2, 1)
)
rbPMServConnEntry.setIndexNames(
    (0, "RAINBOW-SERVICES-MIB", "rbServiceID"),
    (0, "RAINBOW-PERFORMANCE-MIB", "rbPMConnDirection"),
    (0, "RAINBOW-PERFORMANCE-MIB", "rbPMConnQoSPipeIdx"),
)
if mibBuilder.loadTexts:
    rbPMServConnEntry.setStatus("current")


class _RbPMConnDirection_Type(Integer32):
    """Custom type rbPMConnDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("downLink", 1),
          ("upLink", 2))
    )


_RbPMConnDirection_Type.__name__ = "Integer32"
_RbPMConnDirection_Object = MibTableColumn
rbPMConnDirection = _RbPMConnDirection_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 1, 2, 1, 1),
    _RbPMConnDirection_Type()
)
rbPMConnDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPMConnDirection.setStatus("current")


class _RbPMConnQoSPipeIdx_Type(Integer32):
    """Custom type rbPMConnQoSPipeIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_RbPMConnQoSPipeIdx_Type.__name__ = "Integer32"
_RbPMConnQoSPipeIdx_Object = MibTableColumn
rbPMConnQoSPipeIdx = _RbPMConnQoSPipeIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 1, 2, 1, 2),
    _RbPMConnQoSPipeIdx_Type()
)
rbPMConnQoSPipeIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPMConnQoSPipeIdx.setStatus("current")
_RbPMConnByteReq_Type = Counter32
_RbPMConnByteReq_Object = MibTableColumn
rbPMConnByteReq = _RbPMConnByteReq_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 1, 2, 1, 3),
    _RbPMConnByteReq_Type()
)
rbPMConnByteReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPMConnByteReq.setStatus("current")
_RbPMConnByteTx_Type = Counter32
_RbPMConnByteTx_Object = MibTableColumn
rbPMConnByteTx = _RbPMConnByteTx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 1, 2, 1, 4),
    _RbPMConnByteTx_Type()
)
rbPMConnByteTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPMConnByteTx.setStatus("current")
_RbPMConnByteRetTx_Type = Counter32
_RbPMConnByteRetTx_Object = MibTableColumn
rbPMConnByteRetTx = _RbPMConnByteRetTx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 1, 2, 1, 5),
    _RbPMConnByteRetTx_Type()
)
rbPMConnByteRetTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPMConnByteRetTx.setStatus("current")
_RbPMConnByteDropped_Type = Counter32
_RbPMConnByteDropped_Object = MibTableColumn
rbPMConnByteDropped = _RbPMConnByteDropped_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 1, 2, 1, 6),
    _RbPMConnByteDropped_Type()
)
rbPMConnByteDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPMConnByteDropped.setStatus("current")
_RbPMConnByteDiscarded_Type = Counter32
_RbPMConnByteDiscarded_Object = MibTableColumn
rbPMConnByteDiscarded = _RbPMConnByteDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 1, 2, 1, 7),
    _RbPMConnByteDiscarded_Type()
)
rbPMConnByteDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPMConnByteDiscarded.setStatus("current")
_RbPMConnPktsReq_Type = Counter32
_RbPMConnPktsReq_Object = MibTableColumn
rbPMConnPktsReq = _RbPMConnPktsReq_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 1, 2, 1, 8),
    _RbPMConnPktsReq_Type()
)
rbPMConnPktsReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPMConnPktsReq.setStatus("current")
_RbPMConnPktsTx_Type = Counter32
_RbPMConnPktsTx_Object = MibTableColumn
rbPMConnPktsTx = _RbPMConnPktsTx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 1, 2, 1, 9),
    _RbPMConnPktsTx_Type()
)
rbPMConnPktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPMConnPktsTx.setStatus("current")
_RbPMConnPktsDropped_Type = Counter32
_RbPMConnPktsDropped_Object = MibTableColumn
rbPMConnPktsDropped = _RbPMConnPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 1, 2, 1, 10),
    _RbPMConnPktsDropped_Type()
)
rbPMConnPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPMConnPktsDropped.setStatus("current")
_RbPMConnPktsDiscarded_Type = Counter32
_RbPMConnPktsDiscarded_Object = MibTableColumn
rbPMConnPktsDiscarded = _RbPMConnPktsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 1, 2, 1, 11),
    _RbPMConnPktsDiscarded_Type()
)
rbPMConnPktsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPMConnPktsDiscarded.setStatus("current")
_RbPMConnAvarageDelay_Type = Integer32
_RbPMConnAvarageDelay_Object = MibTableColumn
rbPMConnAvarageDelay = _RbPMConnAvarageDelay_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 1, 2, 1, 12),
    _RbPMConnAvarageDelay_Type()
)
rbPMConnAvarageDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPMConnAvarageDelay.setStatus("current")
_RbPMConnStandardDeviationDelay_Type = Integer32
_RbPMConnStandardDeviationDelay_Object = MibTableColumn
rbPMConnStandardDeviationDelay = _RbPMConnStandardDeviationDelay_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 1, 2, 1, 13),
    _RbPMConnStandardDeviationDelay_Type()
)
rbPMConnStandardDeviationDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPMConnStandardDeviationDelay.setStatus("current")
_RbPMConnMaxDelay_Type = Integer32
_RbPMConnMaxDelay_Object = MibTableColumn
rbPMConnMaxDelay = _RbPMConnMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 1, 2, 1, 14),
    _RbPMConnMaxDelay_Type()
)
rbPMConnMaxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPMConnMaxDelay.setStatus("current")
_RbPMConnCBP_Type = Gauge32
_RbPMConnCBP_Object = MibTableColumn
rbPMConnCBP = _RbPMConnCBP_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 1, 2, 1, 15),
    _RbPMConnCBP_Type()
)
rbPMConnCBP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPMConnCBP.setStatus("current")
_RbPMConnDLI_Type = Gauge32
_RbPMConnDLI_Object = MibTableColumn
rbPMConnDLI = _RbPMConnDLI_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 1, 2, 1, 16),
    _RbPMConnDLI_Type()
)
rbPMConnDLI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPMConnDLI.setStatus("current")
_RbPMConnExBurst_Type = Gauge32
_RbPMConnExBurst_Object = MibTableColumn
rbPMConnExBurst = _RbPMConnExBurst_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 1, 2, 1, 17),
    _RbPMConnExBurst_Type()
)
rbPMConnExBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPMConnExBurst.setStatus("current")
_RbPMConnAvgThroughput_Type = Gauge32
_RbPMConnAvgThroughput_Object = MibTableColumn
rbPMConnAvgThroughput = _RbPMConnAvgThroughput_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 1, 2, 1, 18),
    _RbPMConnAvgThroughput_Type()
)
rbPMConnAvgThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPMConnAvgThroughput.setStatus("current")


class _RbPMConnResetCounters_Type(Integer32):
    """Custom type rbPMConnResetCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 0),
          ("reset", 1))
    )


_RbPMConnResetCounters_Type.__name__ = "Integer32"
_RbPMConnResetCounters_Object = MibTableColumn
rbPMConnResetCounters = _RbPMConnResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 1, 2, 1, 19),
    _RbPMConnResetCounters_Type()
)
rbPMConnResetCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbPMConnResetCounters.setStatus("current")
_RbPMConnServiceIdx_Type = Unsigned32
_RbPMConnServiceIdx_Object = MibTableColumn
rbPMConnServiceIdx = _RbPMConnServiceIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 1, 2, 1, 20),
    _RbPMConnServiceIdx_Type()
)
rbPMConnServiceIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPMConnServiceIdx.setStatus("current")


class _RbPMConnQoSType_Type(Integer32):
    """Custom type rbPMConnQoSType based on Integer32"""
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
        *(("rbCG", 1),
          ("rbRT", 2),
          ("rbNRT", 3),
          ("rbBE", 4))
    )


_RbPMConnQoSType_Type.__name__ = "Integer32"
_RbPMConnQoSType_Object = MibTableColumn
rbPMConnQoSType = _RbPMConnQoSType_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 1, 2, 1, 21),
    _RbPMConnQoSType_Type()
)
rbPMConnQoSType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPMConnQoSType.setStatus("current")
_RbPMConnQosParam1_Type = Unsigned32
_RbPMConnQosParam1_Object = MibTableColumn
rbPMConnQosParam1 = _RbPMConnQosParam1_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 1, 2, 1, 22),
    _RbPMConnQosParam1_Type()
)
rbPMConnQosParam1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPMConnQosParam1.setStatus("current")
_RbPMConnQosParam2_Type = Unsigned32
_RbPMConnQosParam2_Object = MibTableColumn
rbPMConnQosParam2 = _RbPMConnQosParam2_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 1, 2, 1, 23),
    _RbPMConnQosParam2_Type()
)
rbPMConnQosParam2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPMConnQosParam2.setStatus("current")


class _RbPMConnQosParamTime_Type(Integer32):
    """Custom type rbPMConnQosParamTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("short", 1),
          ("medium", 2),
          ("long", 3))
    )


_RbPMConnQosParamTime_Type.__name__ = "Integer32"
_RbPMConnQosParamTime_Object = MibTableColumn
rbPMConnQosParamTime = _RbPMConnQosParamTime_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 1, 2, 1, 24),
    _RbPMConnQosParamTime_Type()
)
rbPMConnQosParamTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPMConnQosParamTime.setStatus("current")
_RbPMPacketErrorRateTable_Object = MibTable
rbPMPacketErrorRateTable = _RbPMPacketErrorRateTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 4)
)
if mibBuilder.loadTexts:
    rbPMPacketErrorRateTable.setStatus("deprecated")
_RbPMPacketErrorRateEntry_Object = MibTableRow
rbPMPacketErrorRateEntry = _RbPMPacketErrorRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 4, 1)
)
rbPMPacketErrorRateEntry.setIndexNames(
    (0, "RAINBOW-PERFORMANCE-MIB", "rbPMDirection"),
)
if mibBuilder.loadTexts:
    rbPMPacketErrorRateEntry.setStatus("deprecated")


class _RbPMDirection_Type(Integer32):
    """Custom type rbPMDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("downLink", 1),
          ("upLink", 2))
    )


_RbPMDirection_Type.__name__ = "Integer32"
_RbPMDirection_Object = MibTableColumn
rbPMDirection = _RbPMDirection_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 4, 1, 1),
    _RbPMDirection_Type()
)
rbPMDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPMDirection.setStatus("deprecated")
_RbPMTotalBursts_Type = Counter32
_RbPMTotalBursts_Object = MibTableColumn
rbPMTotalBursts = _RbPMTotalBursts_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 4, 1, 2),
    _RbPMTotalBursts_Type()
)
rbPMTotalBursts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPMTotalBursts.setStatus("deprecated")
_RbPMErrorBursts_Type = Counter32
_RbPMErrorBursts_Object = MibTableColumn
rbPMErrorBursts = _RbPMErrorBursts_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 4, 1, 3),
    _RbPMErrorBursts_Type()
)
rbPMErrorBursts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPMErrorBursts.setStatus("deprecated")


class _RbPMResetCounters_Type(Integer32):
    """Custom type rbPMResetCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 0),
          ("reset", 1))
    )


_RbPMResetCounters_Type.__name__ = "Integer32"
_RbPMResetCounters_Object = MibTableColumn
rbPMResetCounters = _RbPMResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 4, 1, 4),
    _RbPMResetCounters_Type()
)
rbPMResetCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbPMResetCounters.setStatus("deprecated")
_RbPMIfCountersTable_Object = MibTable
rbPMIfCountersTable = _RbPMIfCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 5)
)
if mibBuilder.loadTexts:
    rbPMIfCountersTable.setStatus("deprecated")
_RbPMIfCountersEntry_Object = MibTableRow
rbPMIfCountersEntry = _RbPMIfCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 5, 1)
)
rbPMIfCountersEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rbPMIfCountersEntry.setStatus("deprecated")


class _RbPMIfInResetCounters_Type(Integer32):
    """Custom type rbPMIfInResetCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 0),
          ("reset", 1))
    )


_RbPMIfInResetCounters_Type.__name__ = "Integer32"
_RbPMIfInResetCounters_Object = MibTableColumn
rbPMIfInResetCounters = _RbPMIfInResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 5, 1, 1),
    _RbPMIfInResetCounters_Type()
)
rbPMIfInResetCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbPMIfInResetCounters.setStatus("deprecated")
_RbPMIfInForwardedBytes_Type = Counter32
_RbPMIfInForwardedBytes_Object = MibTableColumn
rbPMIfInForwardedBytes = _RbPMIfInForwardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 5, 1, 2),
    _RbPMIfInForwardedBytes_Type()
)
rbPMIfInForwardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPMIfInForwardedBytes.setStatus("deprecated")
_RbPMIfInInternalBytes_Type = Counter32
_RbPMIfInInternalBytes_Object = MibTableColumn
rbPMIfInInternalBytes = _RbPMIfInInternalBytes_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 5, 1, 3),
    _RbPMIfInInternalBytes_Type()
)
rbPMIfInInternalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPMIfInInternalBytes.setStatus("deprecated")
_RbPMIfInDiscardedBytes_Type = Counter32
_RbPMIfInDiscardedBytes_Object = MibTableColumn
rbPMIfInDiscardedBytes = _RbPMIfInDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 5, 1, 4),
    _RbPMIfInDiscardedBytes_Type()
)
rbPMIfInDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPMIfInDiscardedBytes.setStatus("deprecated")
_RbPMIfOutInternalPackets_Type = Counter32
_RbPMIfOutInternalPackets_Object = MibTableColumn
rbPMIfOutInternalPackets = _RbPMIfOutInternalPackets_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 5, 1, 5),
    _RbPMIfOutInternalPackets_Type()
)
rbPMIfOutInternalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPMIfOutInternalPackets.setStatus("deprecated")


class _RbPMIfOutResetCounters_Type(Integer32):
    """Custom type rbPMIfOutResetCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 0),
          ("reset", 1))
    )


_RbPMIfOutResetCounters_Type.__name__ = "Integer32"
_RbPMIfOutResetCounters_Object = MibTableColumn
rbPMIfOutResetCounters = _RbPMIfOutResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 5, 1, 6),
    _RbPMIfOutResetCounters_Type()
)
rbPMIfOutResetCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbPMIfOutResetCounters.setStatus("deprecated")
_RbPMIfOutSubmittedBytes_Type = Counter32
_RbPMIfOutSubmittedBytes_Object = MibTableColumn
rbPMIfOutSubmittedBytes = _RbPMIfOutSubmittedBytes_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 5, 1, 7),
    _RbPMIfOutSubmittedBytes_Type()
)
rbPMIfOutSubmittedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPMIfOutSubmittedBytes.setStatus("deprecated")
_RbPMIfOutInternalBytes_Type = Counter32
_RbPMIfOutInternalBytes_Object = MibTableColumn
rbPMIfOutInternalBytes = _RbPMIfOutInternalBytes_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 5, 1, 8),
    _RbPMIfOutInternalBytes_Type()
)
rbPMIfOutInternalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPMIfOutInternalBytes.setStatus("deprecated")
_RbPMIfOutDiscardedBytes_Type = Counter32
_RbPMIfOutDiscardedBytes_Object = MibTableColumn
rbPMIfOutDiscardedBytes = _RbPMIfOutDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 5, 1, 9),
    _RbPMIfOutDiscardedBytes_Type()
)
rbPMIfOutDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPMIfOutDiscardedBytes.setStatus("deprecated")
_RbPMBurstErrRateCounters_ObjectIdentity = ObjectIdentity
rbPMBurstErrRateCounters = _RbPMBurstErrRateCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 6)
)
_RbPMBurstErrorRateTable_Object = MibTable
rbPMBurstErrorRateTable = _RbPMBurstErrorRateTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 6, 1)
)
if mibBuilder.loadTexts:
    rbPMBurstErrorRateTable.setStatus("current")
_RbPMBurstErrorRateEntry_Object = MibTableRow
rbPMBurstErrorRateEntry = _RbPMBurstErrorRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 6, 1, 1)
)
rbPMBurstErrorRateEntry.setIndexNames(
    (0, "RAINBOW-PERFORMANCE-MIB", "rbPMBurstSuMacAddr"),
    (0, "RAINBOW-PERFORMANCE-MIB", "rbPMBurstDirection"),
    (0, "RAINBOW-PERFORMANCE-MIB", "rbPMBurstRate"),
)
if mibBuilder.loadTexts:
    rbPMBurstErrorRateEntry.setStatus("current")
_RbPMBurstSuMacAddr_Type = MacAddress
_RbPMBurstSuMacAddr_Object = MibTableColumn
rbPMBurstSuMacAddr = _RbPMBurstSuMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 6, 1, 1, 1),
    _RbPMBurstSuMacAddr_Type()
)
rbPMBurstSuMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPMBurstSuMacAddr.setStatus("current")


class _RbPMBurstDirection_Type(Integer32):
    """Custom type rbPMBurstDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("downLink", 1),
          ("upLink", 2))
    )


_RbPMBurstDirection_Type.__name__ = "Integer32"
_RbPMBurstDirection_Object = MibTableColumn
rbPMBurstDirection = _RbPMBurstDirection_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 6, 1, 1, 2),
    _RbPMBurstDirection_Type()
)
rbPMBurstDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPMBurstDirection.setStatus("current")


class _RbPMBurstRate_Type(Modulation):
    """Custom type rbPMBurstRate based on Modulation"""
    defaultValue = 1


_RbPMBurstRate_Type.__name__ = "Modulation"
_RbPMBurstRate_Object = MibTableColumn
rbPMBurstRate = _RbPMBurstRate_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 6, 1, 1, 3),
    _RbPMBurstRate_Type()
)
rbPMBurstRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPMBurstRate.setStatus("current")


class _RbPMBurstCountersReset_Type(Integer32):
    """Custom type rbPMBurstCountersReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 0),
          ("reset", 1))
    )


_RbPMBurstCountersReset_Type.__name__ = "Integer32"
_RbPMBurstCountersReset_Object = MibTableColumn
rbPMBurstCountersReset = _RbPMBurstCountersReset_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 6, 1, 1, 4),
    _RbPMBurstCountersReset_Type()
)
rbPMBurstCountersReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbPMBurstCountersReset.setStatus("current")
_RbPMBurstTotal_Type = Counter32
_RbPMBurstTotal_Object = MibTableColumn
rbPMBurstTotal = _RbPMBurstTotal_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 6, 1, 1, 5),
    _RbPMBurstTotal_Type()
)
rbPMBurstTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPMBurstTotal.setStatus("current")
_RbPMBurstError_Type = Counter32
_RbPMBurstError_Object = MibTableColumn
rbPMBurstError = _RbPMBurstError_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 6, 1, 1, 6),
    _RbPMBurstError_Type()
)
rbPMBurstError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPMBurstError.setStatus("current")
_RbPMBurstErrorRate_Type = DisplayString
_RbPMBurstErrorRate_Object = MibTableColumn
rbPMBurstErrorRate = _RbPMBurstErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 6, 1, 1, 7),
    _RbPMBurstErrorRate_Type()
)
rbPMBurstErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPMBurstErrorRate.setStatus("current")
_RbPMIfCounters_ObjectIdentity = ObjectIdentity
rbPMIfCounters = _RbPMIfCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7)
)
_RbNPUDataPortCounters_ObjectIdentity = ObjectIdentity
rbNPUDataPortCounters = _RbNPUDataPortCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 1)
)
_RbNPUDataPortCountersTable_Object = MibTable
rbNPUDataPortCountersTable = _RbNPUDataPortCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 1, 1)
)
if mibBuilder.loadTexts:
    rbNPUDataPortCountersTable.setStatus("current")
_RbNPUDataPortCountersEntry_Object = MibTableRow
rbNPUDataPortCountersEntry = _RbNPUDataPortCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 1, 1, 1)
)
rbNPUDataPortCountersEntry.setIndexNames(
    (0, "RAINBOW-PERFORMANCE-MIB", "rbPMIfSlot"),
)
if mibBuilder.loadTexts:
    rbNPUDataPortCountersEntry.setStatus("current")


class _RbPMIfSlot_Type(Integer32):
    """Custom type rbPMIfSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 6),
    )


_RbPMIfSlot_Type.__name__ = "Integer32"
_RbPMIfSlot_Object = MibTableColumn
rbPMIfSlot = _RbPMIfSlot_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 1, 1, 1, 1),
    _RbPMIfSlot_Type()
)
rbPMIfSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPMIfSlot.setStatus("current")


class _RbNpuDataPortResetCounters_Type(Integer32):
    """Custom type rbNpuDataPortResetCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 0),
          ("reset", 1))
    )


_RbNpuDataPortResetCounters_Type.__name__ = "Integer32"
_RbNpuDataPortResetCounters_Object = MibTableColumn
rbNpuDataPortResetCounters = _RbNpuDataPortResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 1, 1, 1, 2),
    _RbNpuDataPortResetCounters_Type()
)
rbNpuDataPortResetCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbNpuDataPortResetCounters.setStatus("current")
_RbNpuDataPortTotalPacketsRx_Type = Counter32
_RbNpuDataPortTotalPacketsRx_Object = MibTableColumn
rbNpuDataPortTotalPacketsRx = _RbNpuDataPortTotalPacketsRx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 1, 1, 1, 3),
    _RbNpuDataPortTotalPacketsRx_Type()
)
rbNpuDataPortTotalPacketsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbNpuDataPortTotalPacketsRx.setStatus("current")
_RbNpuDataPortMangementPacketsFw_Type = Counter32
_RbNpuDataPortMangementPacketsFw_Object = MibTableColumn
rbNpuDataPortMangementPacketsFw = _RbNpuDataPortMangementPacketsFw_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 1, 1, 1, 4),
    _RbNpuDataPortMangementPacketsFw_Type()
)
rbNpuDataPortMangementPacketsFw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbNpuDataPortMangementPacketsFw.setStatus("current")
_RbNpuDataPortPacketsFwToSlot1_Type = Counter32
_RbNpuDataPortPacketsFwToSlot1_Object = MibTableColumn
rbNpuDataPortPacketsFwToSlot1 = _RbNpuDataPortPacketsFwToSlot1_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 1, 1, 1, 5),
    _RbNpuDataPortPacketsFwToSlot1_Type()
)
rbNpuDataPortPacketsFwToSlot1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbNpuDataPortPacketsFwToSlot1.setStatus("current")
_RbNpuDataPortPacketsFwToSlot2_Type = Counter32
_RbNpuDataPortPacketsFwToSlot2_Object = MibTableColumn
rbNpuDataPortPacketsFwToSlot2 = _RbNpuDataPortPacketsFwToSlot2_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 1, 1, 1, 6),
    _RbNpuDataPortPacketsFwToSlot2_Type()
)
rbNpuDataPortPacketsFwToSlot2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbNpuDataPortPacketsFwToSlot2.setStatus("current")
_RbNpuDataPortPacketsFwToSlot3_Type = Counter32
_RbNpuDataPortPacketsFwToSlot3_Object = MibTableColumn
rbNpuDataPortPacketsFwToSlot3 = _RbNpuDataPortPacketsFwToSlot3_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 1, 1, 1, 7),
    _RbNpuDataPortPacketsFwToSlot3_Type()
)
rbNpuDataPortPacketsFwToSlot3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbNpuDataPortPacketsFwToSlot3.setStatus("current")
_RbNpuDataPortPacketsFwToSlot4_Type = Counter32
_RbNpuDataPortPacketsFwToSlot4_Object = MibTableColumn
rbNpuDataPortPacketsFwToSlot4 = _RbNpuDataPortPacketsFwToSlot4_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 1, 1, 1, 8),
    _RbNpuDataPortPacketsFwToSlot4_Type()
)
rbNpuDataPortPacketsFwToSlot4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbNpuDataPortPacketsFwToSlot4.setStatus("current")
_RbNpuDataPortPacketsFwToSlot7_Type = Counter32
_RbNpuDataPortPacketsFwToSlot7_Object = MibTableColumn
rbNpuDataPortPacketsFwToSlot7 = _RbNpuDataPortPacketsFwToSlot7_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 1, 1, 1, 9),
    _RbNpuDataPortPacketsFwToSlot7_Type()
)
rbNpuDataPortPacketsFwToSlot7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbNpuDataPortPacketsFwToSlot7.setStatus("current")
_RbNpuDataPortPacketsFwToSlot8_Type = Counter32
_RbNpuDataPortPacketsFwToSlot8_Object = MibTableColumn
rbNpuDataPortPacketsFwToSlot8 = _RbNpuDataPortPacketsFwToSlot8_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 1, 1, 1, 10),
    _RbNpuDataPortPacketsFwToSlot8_Type()
)
rbNpuDataPortPacketsFwToSlot8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbNpuDataPortPacketsFwToSlot8.setStatus("current")
_RbNpuDataPortPacketsFwToSlot9_Type = Counter32
_RbNpuDataPortPacketsFwToSlot9_Object = MibTableColumn
rbNpuDataPortPacketsFwToSlot9 = _RbNpuDataPortPacketsFwToSlot9_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 1, 1, 1, 11),
    _RbNpuDataPortPacketsFwToSlot9_Type()
)
rbNpuDataPortPacketsFwToSlot9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbNpuDataPortPacketsFwToSlot9.setStatus("current")
_RbNpuDataPortPacketsDiscardedOnRx_Type = Counter32
_RbNpuDataPortPacketsDiscardedOnRx_Object = MibTableColumn
rbNpuDataPortPacketsDiscardedOnRx = _RbNpuDataPortPacketsDiscardedOnRx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 1, 1, 1, 12),
    _RbNpuDataPortPacketsDiscardedOnRx_Type()
)
rbNpuDataPortPacketsDiscardedOnRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbNpuDataPortPacketsDiscardedOnRx.setStatus("current")
_RbNpuDataPortTotalPacketsTx_Type = Counter32
_RbNpuDataPortTotalPacketsTx_Object = MibTableColumn
rbNpuDataPortTotalPacketsTx = _RbNpuDataPortTotalPacketsTx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 1, 1, 1, 13),
    _RbNpuDataPortTotalPacketsTx_Type()
)
rbNpuDataPortTotalPacketsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbNpuDataPortTotalPacketsTx.setStatus("current")
_RbNpuDataPortMangementPacketsSbmt_Type = Counter32
_RbNpuDataPortMangementPacketsSbmt_Object = MibTableColumn
rbNpuDataPortMangementPacketsSbmt = _RbNpuDataPortMangementPacketsSbmt_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 1, 1, 1, 14),
    _RbNpuDataPortMangementPacketsSbmt_Type()
)
rbNpuDataPortMangementPacketsSbmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbNpuDataPortMangementPacketsSbmt.setStatus("current")
_RbNpuDataPortPacketsSbmtFromSlot1_Type = Counter32
_RbNpuDataPortPacketsSbmtFromSlot1_Object = MibTableColumn
rbNpuDataPortPacketsSbmtFromSlot1 = _RbNpuDataPortPacketsSbmtFromSlot1_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 1, 1, 1, 15),
    _RbNpuDataPortPacketsSbmtFromSlot1_Type()
)
rbNpuDataPortPacketsSbmtFromSlot1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbNpuDataPortPacketsSbmtFromSlot1.setStatus("current")
_RbNpuDataPortPacketsSbmtFromSlot2_Type = Counter32
_RbNpuDataPortPacketsSbmtFromSlot2_Object = MibTableColumn
rbNpuDataPortPacketsSbmtFromSlot2 = _RbNpuDataPortPacketsSbmtFromSlot2_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 1, 1, 1, 16),
    _RbNpuDataPortPacketsSbmtFromSlot2_Type()
)
rbNpuDataPortPacketsSbmtFromSlot2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbNpuDataPortPacketsSbmtFromSlot2.setStatus("current")
_RbNpuDataPortPacketsSbmtFromSlot3_Type = Counter32
_RbNpuDataPortPacketsSbmtFromSlot3_Object = MibTableColumn
rbNpuDataPortPacketsSbmtFromSlot3 = _RbNpuDataPortPacketsSbmtFromSlot3_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 1, 1, 1, 17),
    _RbNpuDataPortPacketsSbmtFromSlot3_Type()
)
rbNpuDataPortPacketsSbmtFromSlot3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbNpuDataPortPacketsSbmtFromSlot3.setStatus("current")
_RbNpuDataPortPacketsSbmtFromSlot4_Type = Counter32
_RbNpuDataPortPacketsSbmtFromSlot4_Object = MibTableColumn
rbNpuDataPortPacketsSbmtFromSlot4 = _RbNpuDataPortPacketsSbmtFromSlot4_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 1, 1, 1, 18),
    _RbNpuDataPortPacketsSbmtFromSlot4_Type()
)
rbNpuDataPortPacketsSbmtFromSlot4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbNpuDataPortPacketsSbmtFromSlot4.setStatus("current")
_RbNpuDataPortPacketsSbmtFromSlot7_Type = Counter32
_RbNpuDataPortPacketsSbmtFromSlot7_Object = MibTableColumn
rbNpuDataPortPacketsSbmtFromSlot7 = _RbNpuDataPortPacketsSbmtFromSlot7_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 1, 1, 1, 19),
    _RbNpuDataPortPacketsSbmtFromSlot7_Type()
)
rbNpuDataPortPacketsSbmtFromSlot7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbNpuDataPortPacketsSbmtFromSlot7.setStatus("current")
_RbNpuDataPortPacketsSbmtFromSlot8_Type = Counter32
_RbNpuDataPortPacketsSbmtFromSlot8_Object = MibTableColumn
rbNpuDataPortPacketsSbmtFromSlot8 = _RbNpuDataPortPacketsSbmtFromSlot8_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 1, 1, 1, 20),
    _RbNpuDataPortPacketsSbmtFromSlot8_Type()
)
rbNpuDataPortPacketsSbmtFromSlot8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbNpuDataPortPacketsSbmtFromSlot8.setStatus("current")
_RbNpuDataPortPacketsSbmtFromSlot9_Type = Counter32
_RbNpuDataPortPacketsSbmtFromSlot9_Object = MibTableColumn
rbNpuDataPortPacketsSbmtFromSlot9 = _RbNpuDataPortPacketsSbmtFromSlot9_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 1, 1, 1, 21),
    _RbNpuDataPortPacketsSbmtFromSlot9_Type()
)
rbNpuDataPortPacketsSbmtFromSlot9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbNpuDataPortPacketsSbmtFromSlot9.setStatus("current")
_RbNpuDataPortPacketsDiscardedOnTx_Type = Counter32
_RbNpuDataPortPacketsDiscardedOnTx_Object = MibTableColumn
rbNpuDataPortPacketsDiscardedOnTx = _RbNpuDataPortPacketsDiscardedOnTx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 1, 1, 1, 22),
    _RbNpuDataPortPacketsDiscardedOnTx_Type()
)
rbNpuDataPortPacketsDiscardedOnTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbNpuDataPortPacketsDiscardedOnTx.setStatus("current")
_RbMBSTDataPortCounters_ObjectIdentity = ObjectIdentity
rbMBSTDataPortCounters = _RbMBSTDataPortCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 2)
)
_RbMBSTDataPortCountersTable_Object = MibTable
rbMBSTDataPortCountersTable = _RbMBSTDataPortCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 2, 1)
)
if mibBuilder.loadTexts:
    rbMBSTDataPortCountersTable.setStatus("current")
_RbMBSTDataPortCountersEntry_Object = MibTableRow
rbMBSTDataPortCountersEntry = _RbMBSTDataPortCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 2, 1, 1)
)
rbMBSTDataPortCountersEntry.setIndexNames(
    (0, "RAINBOW-PERFORMANCE-MIB", "rbMBSTDataPortIfSlot"),
)
if mibBuilder.loadTexts:
    rbMBSTDataPortCountersEntry.setStatus("current")


class _RbMBSTDataPortIfSlot_Type(Integer32):
    """Custom type rbMBSTDataPortIfSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_RbMBSTDataPortIfSlot_Type.__name__ = "Integer32"
_RbMBSTDataPortIfSlot_Object = MibTableColumn
rbMBSTDataPortIfSlot = _RbMBSTDataPortIfSlot_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 2, 1, 1, 1),
    _RbMBSTDataPortIfSlot_Type()
)
rbMBSTDataPortIfSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbMBSTDataPortIfSlot.setStatus("current")


class _RbMBSTDataPortResetCounters_Type(Integer32):
    """Custom type rbMBSTDataPortResetCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 0),
          ("reset", 1))
    )


_RbMBSTDataPortResetCounters_Type.__name__ = "Integer32"
_RbMBSTDataPortResetCounters_Object = MibTableColumn
rbMBSTDataPortResetCounters = _RbMBSTDataPortResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 2, 1, 1, 2),
    _RbMBSTDataPortResetCounters_Type()
)
rbMBSTDataPortResetCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbMBSTDataPortResetCounters.setStatus("current")
_RbMBSTDataPortTotalBytesRx_Type = Counter32
_RbMBSTDataPortTotalBytesRx_Object = MibTableColumn
rbMBSTDataPortTotalBytesRx = _RbMBSTDataPortTotalBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 2, 1, 1, 3),
    _RbMBSTDataPortTotalBytesRx_Type()
)
rbMBSTDataPortTotalBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbMBSTDataPortTotalBytesRx.setStatus("current")
_RbMBSTDataPortDataBytesRx_Type = Counter32
_RbMBSTDataPortDataBytesRx_Object = MibTableColumn
rbMBSTDataPortDataBytesRx = _RbMBSTDataPortDataBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 2, 1, 1, 4),
    _RbMBSTDataPortDataBytesRx_Type()
)
rbMBSTDataPortDataBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbMBSTDataPortDataBytesRx.setStatus("current")
_RbMBSTDataPortDataBytesDiscardedOnRx_Type = Counter32
_RbMBSTDataPortDataBytesDiscardedOnRx_Object = MibTableColumn
rbMBSTDataPortDataBytesDiscardedOnRx = _RbMBSTDataPortDataBytesDiscardedOnRx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 2, 1, 1, 5),
    _RbMBSTDataPortDataBytesDiscardedOnRx_Type()
)
rbMBSTDataPortDataBytesDiscardedOnRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbMBSTDataPortDataBytesDiscardedOnRx.setStatus("current")
_RbMBSTDataPortTotalBytesTx_Type = Counter32
_RbMBSTDataPortTotalBytesTx_Object = MibTableColumn
rbMBSTDataPortTotalBytesTx = _RbMBSTDataPortTotalBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 2, 1, 1, 6),
    _RbMBSTDataPortTotalBytesTx_Type()
)
rbMBSTDataPortTotalBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbMBSTDataPortTotalBytesTx.setStatus("current")
_RbMBSTDataPortDataBytesTx_Type = Counter32
_RbMBSTDataPortDataBytesTx_Object = MibTableColumn
rbMBSTDataPortDataBytesTx = _RbMBSTDataPortDataBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 2, 1, 1, 7),
    _RbMBSTDataPortDataBytesTx_Type()
)
rbMBSTDataPortDataBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbMBSTDataPortDataBytesTx.setStatus("current")
_RbMBSTDataPortDataBytesDiscardedOnTx_Type = Counter32
_RbMBSTDataPortDataBytesDiscardedOnTx_Object = MibTableColumn
rbMBSTDataPortDataBytesDiscardedOnTx = _RbMBSTDataPortDataBytesDiscardedOnTx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 2, 1, 1, 8),
    _RbMBSTDataPortDataBytesDiscardedOnTx_Type()
)
rbMBSTDataPortDataBytesDiscardedOnTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbMBSTDataPortDataBytesDiscardedOnTx.setStatus("current")
_RbManagementPortCounters_ObjectIdentity = ObjectIdentity
rbManagementPortCounters = _RbManagementPortCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 10)
)
_RbMngmntPortCountersTable_Object = MibTable
rbMngmntPortCountersTable = _RbMngmntPortCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 10, 1)
)
if mibBuilder.loadTexts:
    rbMngmntPortCountersTable.setStatus("current")
_RbMngmntPortCountersEntry_Object = MibTableRow
rbMngmntPortCountersEntry = _RbMngmntPortCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 10, 1, 1)
)
rbMngmntPortCountersEntry.setIndexNames(
    (0, "RAINBOW-PERFORMANCE-MIB", "rbMngmntPortIfSlot"),
)
if mibBuilder.loadTexts:
    rbMngmntPortCountersEntry.setStatus("current")


class _RbMngmntPortResetCounters_Type(Integer32):
    """Custom type rbMngmntPortResetCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 0),
          ("reset", 1))
    )


_RbMngmntPortResetCounters_Type.__name__ = "Integer32"
_RbMngmntPortResetCounters_Object = MibTableColumn
rbMngmntPortResetCounters = _RbMngmntPortResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 10, 1, 1, 1),
    _RbMngmntPortResetCounters_Type()
)
rbMngmntPortResetCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbMngmntPortResetCounters.setStatus("current")
_RbMngmntPortPacketsRx_Type = Counter32
_RbMngmntPortPacketsRx_Object = MibTableColumn
rbMngmntPortPacketsRx = _RbMngmntPortPacketsRx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 10, 1, 1, 2),
    _RbMngmntPortPacketsRx_Type()
)
rbMngmntPortPacketsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbMngmntPortPacketsRx.setStatus("current")
_RbMngmntPortPacketsDiscardedOnRx_Type = Counter32
_RbMngmntPortPacketsDiscardedOnRx_Object = MibTableColumn
rbMngmntPortPacketsDiscardedOnRx = _RbMngmntPortPacketsDiscardedOnRx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 10, 1, 1, 3),
    _RbMngmntPortPacketsDiscardedOnRx_Type()
)
rbMngmntPortPacketsDiscardedOnRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbMngmntPortPacketsDiscardedOnRx.setStatus("current")
_RbMngmntPortPacketsTx_Type = Counter32
_RbMngmntPortPacketsTx_Object = MibTableColumn
rbMngmntPortPacketsTx = _RbMngmntPortPacketsTx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 10, 1, 1, 4),
    _RbMngmntPortPacketsTx_Type()
)
rbMngmntPortPacketsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbMngmntPortPacketsTx.setStatus("current")
_RbMngmntPortPacketsDiscardedOnTx_Type = Counter32
_RbMngmntPortPacketsDiscardedOnTx_Object = MibTableColumn
rbMngmntPortPacketsDiscardedOnTx = _RbMngmntPortPacketsDiscardedOnTx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 10, 1, 1, 5),
    _RbMngmntPortPacketsDiscardedOnTx_Type()
)
rbMngmntPortPacketsDiscardedOnTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbMngmntPortPacketsDiscardedOnTx.setStatus("current")


class _RbMngmntPortIfSlot_Type(Integer32):
    """Custom type rbMngmntPortIfSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_RbMngmntPortIfSlot_Type.__name__ = "Integer32"
_RbMngmntPortIfSlot_Object = MibTableColumn
rbMngmntPortIfSlot = _RbMngmntPortIfSlot_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 10, 1, 1, 6),
    _RbMngmntPortIfSlot_Type()
)
rbMngmntPortIfSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbMngmntPortIfSlot.setStatus("current")
_RbSUEthernetCounters_ObjectIdentity = ObjectIdentity
rbSUEthernetCounters = _RbSUEthernetCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 20)
)
_RbSUEthernetCountersTable_Object = MibTable
rbSUEthernetCountersTable = _RbSUEthernetCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 20, 1)
)
if mibBuilder.loadTexts:
    rbSUEthernetCountersTable.setStatus("current")
_RbSUEthernetCountersEntry_Object = MibTableRow
rbSUEthernetCountersEntry = _RbSUEthernetCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 20, 1, 1)
)
rbSUEthernetCountersEntry.setIndexNames(
    (0, "RAINBOW-PERFORMANCE-MIB", "rbPMIfSuMacAddr"),
)
if mibBuilder.loadTexts:
    rbSUEthernetCountersEntry.setStatus("current")
_RbPMIfSuMacAddr_Type = MacAddress
_RbPMIfSuMacAddr_Object = MibTableColumn
rbPMIfSuMacAddr = _RbPMIfSuMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 20, 1, 1, 1),
    _RbPMIfSuMacAddr_Type()
)
rbPMIfSuMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPMIfSuMacAddr.setStatus("current")


class _RbSUEthernetResetCounters_Type(Integer32):
    """Custom type rbSUEthernetResetCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 0),
          ("reset", 1))
    )


_RbSUEthernetResetCounters_Type.__name__ = "Integer32"
_RbSUEthernetResetCounters_Object = MibTableColumn
rbSUEthernetResetCounters = _RbSUEthernetResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 20, 1, 1, 2),
    _RbSUEthernetResetCounters_Type()
)
rbSUEthernetResetCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSUEthernetResetCounters.setStatus("current")
_RbSUEthernetDataBytesRx_Type = Counter32
_RbSUEthernetDataBytesRx_Object = MibTableColumn
rbSUEthernetDataBytesRx = _RbSUEthernetDataBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 20, 1, 1, 3),
    _RbSUEthernetDataBytesRx_Type()
)
rbSUEthernetDataBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSUEthernetDataBytesRx.setStatus("current")
_RbSUEthernetDataBytesDiscardedOnRx_Type = Counter32
_RbSUEthernetDataBytesDiscardedOnRx_Object = MibTableColumn
rbSUEthernetDataBytesDiscardedOnRx = _RbSUEthernetDataBytesDiscardedOnRx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 20, 1, 1, 4),
    _RbSUEthernetDataBytesDiscardedOnRx_Type()
)
rbSUEthernetDataBytesDiscardedOnRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSUEthernetDataBytesDiscardedOnRx.setStatus("current")
_RbSUEthernetDataBytesTx_Type = Counter32
_RbSUEthernetDataBytesTx_Object = MibTableColumn
rbSUEthernetDataBytesTx = _RbSUEthernetDataBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 20, 1, 1, 5),
    _RbSUEthernetDataBytesTx_Type()
)
rbSUEthernetDataBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSUEthernetDataBytesTx.setStatus("current")
_RbSUEthernetDataBytesDiscardedOnTx_Type = Counter32
_RbSUEthernetDataBytesDiscardedOnTx_Object = MibTableColumn
rbSUEthernetDataBytesDiscardedOnTx = _RbSUEthernetDataBytesDiscardedOnTx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 20, 1, 1, 6),
    _RbSUEthernetDataBytesDiscardedOnTx_Type()
)
rbSUEthernetDataBytesDiscardedOnTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSUEthernetDataBytesDiscardedOnTx.setStatus("current")
_RbSUWirelessCounters_ObjectIdentity = ObjectIdentity
rbSUWirelessCounters = _RbSUWirelessCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 21)
)
_RbSUWirelessCountersTable_Object = MibTable
rbSUWirelessCountersTable = _RbSUWirelessCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 21, 1)
)
if mibBuilder.loadTexts:
    rbSUWirelessCountersTable.setStatus("current")
_RbSUWirelessCountersEntry_Object = MibTableRow
rbSUWirelessCountersEntry = _RbSUWirelessCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 21, 1, 1)
)
rbSUWirelessCountersEntry.setIndexNames(
    (0, "RAINBOW-PERFORMANCE-MIB", "rbPMIfSuMacAddr"),
)
if mibBuilder.loadTexts:
    rbSUWirelessCountersEntry.setStatus("current")


class _RbSUWirelessResetCounters_Type(Integer32):
    """Custom type rbSUWirelessResetCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 0),
          ("reset", 1))
    )


_RbSUWirelessResetCounters_Type.__name__ = "Integer32"
_RbSUWirelessResetCounters_Object = MibTableColumn
rbSUWirelessResetCounters = _RbSUWirelessResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 21, 1, 1, 1),
    _RbSUWirelessResetCounters_Type()
)
rbSUWirelessResetCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSUWirelessResetCounters.setStatus("current")
_RbSUWirelessDataBytesRx_Type = Counter32
_RbSUWirelessDataBytesRx_Object = MibTableColumn
rbSUWirelessDataBytesRx = _RbSUWirelessDataBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 21, 1, 1, 2),
    _RbSUWirelessDataBytesRx_Type()
)
rbSUWirelessDataBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSUWirelessDataBytesRx.setStatus("current")
_RbSUWirelessDataBytesDiscardedOnRx_Type = Counter32
_RbSUWirelessDataBytesDiscardedOnRx_Object = MibTableColumn
rbSUWirelessDataBytesDiscardedOnRx = _RbSUWirelessDataBytesDiscardedOnRx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 21, 1, 1, 3),
    _RbSUWirelessDataBytesDiscardedOnRx_Type()
)
rbSUWirelessDataBytesDiscardedOnRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSUWirelessDataBytesDiscardedOnRx.setStatus("current")
_RbSUWirelessDataBytesTx_Type = Counter32
_RbSUWirelessDataBytesTx_Object = MibTableColumn
rbSUWirelessDataBytesTx = _RbSUWirelessDataBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 21, 1, 1, 4),
    _RbSUWirelessDataBytesTx_Type()
)
rbSUWirelessDataBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSUWirelessDataBytesTx.setStatus("current")
_RbSUWirelessDataBytesDiscardedOnTx_Type = Counter32
_RbSUWirelessDataBytesDiscardedOnTx_Object = MibTableColumn
rbSUWirelessDataBytesDiscardedOnTx = _RbSUWirelessDataBytesDiscardedOnTx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 21, 1, 1, 5),
    _RbSUWirelessDataBytesDiscardedOnTx_Type()
)
rbSUWirelessDataBytesDiscardedOnTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSUWirelessDataBytesDiscardedOnTx.setStatus("current")
_RbSUWirelessARQEnabledBytesTx_Type = Counter32
_RbSUWirelessARQEnabledBytesTx_Object = MibTableColumn
rbSUWirelessARQEnabledBytesTx = _RbSUWirelessARQEnabledBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 21, 1, 1, 6),
    _RbSUWirelessARQEnabledBytesTx_Type()
)
rbSUWirelessARQEnabledBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSUWirelessARQEnabledBytesTx.setStatus("current")
_RbSUWirelessRTxBytes_Type = Counter32
_RbSUWirelessRTxBytes_Object = MibTableColumn
rbSUWirelessRTxBytes = _RbSUWirelessRTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 21, 1, 1, 7),
    _RbSUWirelessRTxBytes_Type()
)
rbSUWirelessRTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSUWirelessRTxBytes.setStatus("current")
_RbSUWirelessRTxRate_Type = Gauge32
_RbSUWirelessRTxRate_Object = MibTableColumn
rbSUWirelessRTxRate = _RbSUWirelessRTxRate_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 21, 1, 1, 8),
    _RbSUWirelessRTxRate_Type()
)
rbSUWirelessRTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSUWirelessRTxRate.setStatus("current")
_RbAUBackplaneCounters_ObjectIdentity = ObjectIdentity
rbAUBackplaneCounters = _RbAUBackplaneCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 30)
)
_RbAUBackplaneCountersTable_Object = MibTable
rbAUBackplaneCountersTable = _RbAUBackplaneCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 30, 1)
)
if mibBuilder.loadTexts:
    rbAUBackplaneCountersTable.setStatus("current")
_RbAUBackplaneCountersEntry_Object = MibTableRow
rbAUBackplaneCountersEntry = _RbAUBackplaneCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 30, 1, 1)
)
rbAUBackplaneCountersEntry.setIndexNames(
    (0, "RAINBOW-PERFORMANCE-MIB", "rbPMIfAUSlot"),
)
if mibBuilder.loadTexts:
    rbAUBackplaneCountersEntry.setStatus("current")


class _RbPMIfAUSlot_Type(Integer32):
    """Custom type rbPMIfAUSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_RbPMIfAUSlot_Type.__name__ = "Integer32"
_RbPMIfAUSlot_Object = MibTableColumn
rbPMIfAUSlot = _RbPMIfAUSlot_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 30, 1, 1, 1),
    _RbPMIfAUSlot_Type()
)
rbPMIfAUSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPMIfAUSlot.setStatus("current")


class _RbAUBackplaneResetCounters_Type(Integer32):
    """Custom type rbAUBackplaneResetCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 0),
          ("reset", 1))
    )


_RbAUBackplaneResetCounters_Type.__name__ = "Integer32"
_RbAUBackplaneResetCounters_Object = MibTableColumn
rbAUBackplaneResetCounters = _RbAUBackplaneResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 30, 1, 1, 2),
    _RbAUBackplaneResetCounters_Type()
)
rbAUBackplaneResetCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAUBackplaneResetCounters.setStatus("current")
_RbAUBackplaneDataBytesRx_Type = Counter32
_RbAUBackplaneDataBytesRx_Object = MibTableColumn
rbAUBackplaneDataBytesRx = _RbAUBackplaneDataBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 30, 1, 1, 3),
    _RbAUBackplaneDataBytesRx_Type()
)
rbAUBackplaneDataBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbAUBackplaneDataBytesRx.setStatus("current")
_RbAUBackplaneDataBytesDiscardedOnRx_Type = Counter32
_RbAUBackplaneDataBytesDiscardedOnRx_Object = MibTableColumn
rbAUBackplaneDataBytesDiscardedOnRx = _RbAUBackplaneDataBytesDiscardedOnRx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 30, 1, 1, 4),
    _RbAUBackplaneDataBytesDiscardedOnRx_Type()
)
rbAUBackplaneDataBytesDiscardedOnRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbAUBackplaneDataBytesDiscardedOnRx.setStatus("current")
_RbAUBackplaneDataBytesTx_Type = Counter32
_RbAUBackplaneDataBytesTx_Object = MibTableColumn
rbAUBackplaneDataBytesTx = _RbAUBackplaneDataBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 30, 1, 1, 5),
    _RbAUBackplaneDataBytesTx_Type()
)
rbAUBackplaneDataBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbAUBackplaneDataBytesTx.setStatus("current")
_RbAUBackplaneDataBytesDiscardedOnTx_Type = Counter32
_RbAUBackplaneDataBytesDiscardedOnTx_Object = MibTableColumn
rbAUBackplaneDataBytesDiscardedOnTx = _RbAUBackplaneDataBytesDiscardedOnTx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 30, 1, 1, 6),
    _RbAUBackplaneDataBytesDiscardedOnTx_Type()
)
rbAUBackplaneDataBytesDiscardedOnTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbAUBackplaneDataBytesDiscardedOnTx.setStatus("current")
_RbAUWirelessCounters_ObjectIdentity = ObjectIdentity
rbAUWirelessCounters = _RbAUWirelessCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 31)
)
_RbAUWirelessCountersTable_Object = MibTable
rbAUWirelessCountersTable = _RbAUWirelessCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 31, 1)
)
if mibBuilder.loadTexts:
    rbAUWirelessCountersTable.setStatus("current")
_RbAUWirelessCountersEntry_Object = MibTableRow
rbAUWirelessCountersEntry = _RbAUWirelessCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 31, 1, 1)
)
rbAUWirelessCountersEntry.setIndexNames(
    (0, "RAINBOW-PERFORMANCE-MIB", "rbAUWirelessAUSlot"),
)
if mibBuilder.loadTexts:
    rbAUWirelessCountersEntry.setStatus("current")


class _RbAUWirelessResetCounters_Type(Integer32):
    """Custom type rbAUWirelessResetCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 0),
          ("reset", 1))
    )


_RbAUWirelessResetCounters_Type.__name__ = "Integer32"
_RbAUWirelessResetCounters_Object = MibTableColumn
rbAUWirelessResetCounters = _RbAUWirelessResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 31, 1, 1, 1),
    _RbAUWirelessResetCounters_Type()
)
rbAUWirelessResetCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAUWirelessResetCounters.setStatus("current")
_RbAUWirelessDataBytesRx_Type = Counter32
_RbAUWirelessDataBytesRx_Object = MibTableColumn
rbAUWirelessDataBytesRx = _RbAUWirelessDataBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 31, 1, 1, 2),
    _RbAUWirelessDataBytesRx_Type()
)
rbAUWirelessDataBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbAUWirelessDataBytesRx.setStatus("current")
_RbAUWirelessDataBytesDiscardedOnRx_Type = Counter32
_RbAUWirelessDataBytesDiscardedOnRx_Object = MibTableColumn
rbAUWirelessDataBytesDiscardedOnRx = _RbAUWirelessDataBytesDiscardedOnRx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 31, 1, 1, 3),
    _RbAUWirelessDataBytesDiscardedOnRx_Type()
)
rbAUWirelessDataBytesDiscardedOnRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbAUWirelessDataBytesDiscardedOnRx.setStatus("current")
_RbAUWirelessDataBytesTx_Type = Counter32
_RbAUWirelessDataBytesTx_Object = MibTableColumn
rbAUWirelessDataBytesTx = _RbAUWirelessDataBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 31, 1, 1, 4),
    _RbAUWirelessDataBytesTx_Type()
)
rbAUWirelessDataBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbAUWirelessDataBytesTx.setStatus("current")
_RbAUWirelessDataBytesDiscardedOnTx_Type = Counter32
_RbAUWirelessDataBytesDiscardedOnTx_Object = MibTableColumn
rbAUWirelessDataBytesDiscardedOnTx = _RbAUWirelessDataBytesDiscardedOnTx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 31, 1, 1, 5),
    _RbAUWirelessDataBytesDiscardedOnTx_Type()
)
rbAUWirelessDataBytesDiscardedOnTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbAUWirelessDataBytesDiscardedOnTx.setStatus("current")
_RbAUWirelessARQEnabledBytesTx_Type = Counter32
_RbAUWirelessARQEnabledBytesTx_Object = MibTableColumn
rbAUWirelessARQEnabledBytesTx = _RbAUWirelessARQEnabledBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 31, 1, 1, 6),
    _RbAUWirelessARQEnabledBytesTx_Type()
)
rbAUWirelessARQEnabledBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbAUWirelessARQEnabledBytesTx.setStatus("current")
_RbAUWirelessRTxBytes_Type = Counter32
_RbAUWirelessRTxBytes_Object = MibTableColumn
rbAUWirelessRTxBytes = _RbAUWirelessRTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 31, 1, 1, 7),
    _RbAUWirelessRTxBytes_Type()
)
rbAUWirelessRTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbAUWirelessRTxBytes.setStatus("current")
_RbAUWirelessRTxRate_Type = Gauge32
_RbAUWirelessRTxRate_Object = MibTableColumn
rbAUWirelessRTxRate = _RbAUWirelessRTxRate_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 31, 1, 1, 8),
    _RbAUWirelessRTxRate_Type()
)
rbAUWirelessRTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbAUWirelessRTxRate.setStatus("current")


class _RbAUWirelessAUSlot_Type(Integer32):
    """Custom type rbAUWirelessAUSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_RbAUWirelessAUSlot_Type.__name__ = "Integer32"
_RbAUWirelessAUSlot_Object = MibTableColumn
rbAUWirelessAUSlot = _RbAUWirelessAUSlot_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 4, 7, 31, 1, 1, 9),
    _RbAUWirelessAUSlot_Type()
)
rbAUWirelessAUSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbAUWirelessAUSlot.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAINBOW-PERFORMANCE-MIB",
    **{"rbPerformance": rbPerformance,
       "rbPMServ": rbPMServ,
       "rbPMCGServConnTable": rbPMCGServConnTable,
       "rbPMCGServConnEntry": rbPMCGServConnEntry,
       "rbPMCGConnDirection": rbPMCGConnDirection,
       "rbPMCGConnByteReq": rbPMCGConnByteReq,
       "rbPMCGConnByteTx": rbPMCGConnByteTx,
       "rbPMCGConnByteRetTx": rbPMCGConnByteRetTx,
       "rbPMCGConnByteDropped": rbPMCGConnByteDropped,
       "rbPMCGConnByteDiscarded": rbPMCGConnByteDiscarded,
       "rbPMCGConnPktsReq": rbPMCGConnPktsReq,
       "rbPMCGConnPktsTx": rbPMCGConnPktsTx,
       "rbPMCGConnPktsDropped": rbPMCGConnPktsDropped,
       "rbPMCGConnPktsDiscarded": rbPMCGConnPktsDiscarded,
       "rbPMCGConnAvarageDelay": rbPMCGConnAvarageDelay,
       "rbPMCGConnStandardDeviationDelay": rbPMCGConnStandardDeviationDelay,
       "rbPMCGConnMaxDelay": rbPMCGConnMaxDelay,
       "rbPMCGConnPerSucsGrant": rbPMCGConnPerSucsGrant,
       "rbPMCGConnAvgGrantInt": rbPMCGConnAvgGrantInt,
       "rbPMCGConnMaxGrantInt": rbPMCGConnMaxGrantInt,
       "rbPMCGConnAvgIntArvTime": rbPMCGConnAvgIntArvTime,
       "rbPMCGConnMaxIntArvTime": rbPMCGConnMaxIntArvTime,
       "rbPMCGConnMinIntArvTime": rbPMCGConnMinIntArvTime,
       "rbPMCGConnAvgSDUDropRate": rbPMCGConnAvgSDUDropRate,
       "rbPMCGConnResetCounters": rbPMCGConnResetCounters,
       "rbPMServConnTable": rbPMServConnTable,
       "rbPMServConnEntry": rbPMServConnEntry,
       "rbPMConnDirection": rbPMConnDirection,
       "rbPMConnQoSPipeIdx": rbPMConnQoSPipeIdx,
       "rbPMConnByteReq": rbPMConnByteReq,
       "rbPMConnByteTx": rbPMConnByteTx,
       "rbPMConnByteRetTx": rbPMConnByteRetTx,
       "rbPMConnByteDropped": rbPMConnByteDropped,
       "rbPMConnByteDiscarded": rbPMConnByteDiscarded,
       "rbPMConnPktsReq": rbPMConnPktsReq,
       "rbPMConnPktsTx": rbPMConnPktsTx,
       "rbPMConnPktsDropped": rbPMConnPktsDropped,
       "rbPMConnPktsDiscarded": rbPMConnPktsDiscarded,
       "rbPMConnAvarageDelay": rbPMConnAvarageDelay,
       "rbPMConnStandardDeviationDelay": rbPMConnStandardDeviationDelay,
       "rbPMConnMaxDelay": rbPMConnMaxDelay,
       "rbPMConnCBP": rbPMConnCBP,
       "rbPMConnDLI": rbPMConnDLI,
       "rbPMConnExBurst": rbPMConnExBurst,
       "rbPMConnAvgThroughput": rbPMConnAvgThroughput,
       "rbPMConnResetCounters": rbPMConnResetCounters,
       "rbPMConnServiceIdx": rbPMConnServiceIdx,
       "rbPMConnQoSType": rbPMConnQoSType,
       "rbPMConnQosParam1": rbPMConnQosParam1,
       "rbPMConnQosParam2": rbPMConnQosParam2,
       "rbPMConnQosParamTime": rbPMConnQosParamTime,
       "rbPMPacketErrorRateTable": rbPMPacketErrorRateTable,
       "rbPMPacketErrorRateEntry": rbPMPacketErrorRateEntry,
       "rbPMDirection": rbPMDirection,
       "rbPMTotalBursts": rbPMTotalBursts,
       "rbPMErrorBursts": rbPMErrorBursts,
       "rbPMResetCounters": rbPMResetCounters,
       "rbPMIfCountersTable": rbPMIfCountersTable,
       "rbPMIfCountersEntry": rbPMIfCountersEntry,
       "rbPMIfInResetCounters": rbPMIfInResetCounters,
       "rbPMIfInForwardedBytes": rbPMIfInForwardedBytes,
       "rbPMIfInInternalBytes": rbPMIfInInternalBytes,
       "rbPMIfInDiscardedBytes": rbPMIfInDiscardedBytes,
       "rbPMIfOutInternalPackets": rbPMIfOutInternalPackets,
       "rbPMIfOutResetCounters": rbPMIfOutResetCounters,
       "rbPMIfOutSubmittedBytes": rbPMIfOutSubmittedBytes,
       "rbPMIfOutInternalBytes": rbPMIfOutInternalBytes,
       "rbPMIfOutDiscardedBytes": rbPMIfOutDiscardedBytes,
       "rbPMBurstErrRateCounters": rbPMBurstErrRateCounters,
       "rbPMBurstErrorRateTable": rbPMBurstErrorRateTable,
       "rbPMBurstErrorRateEntry": rbPMBurstErrorRateEntry,
       "rbPMBurstSuMacAddr": rbPMBurstSuMacAddr,
       "rbPMBurstDirection": rbPMBurstDirection,
       "rbPMBurstRate": rbPMBurstRate,
       "rbPMBurstCountersReset": rbPMBurstCountersReset,
       "rbPMBurstTotal": rbPMBurstTotal,
       "rbPMBurstError": rbPMBurstError,
       "rbPMBurstErrorRate": rbPMBurstErrorRate,
       "rbPMIfCounters": rbPMIfCounters,
       "rbNPUDataPortCounters": rbNPUDataPortCounters,
       "rbNPUDataPortCountersTable": rbNPUDataPortCountersTable,
       "rbNPUDataPortCountersEntry": rbNPUDataPortCountersEntry,
       "rbPMIfSlot": rbPMIfSlot,
       "rbNpuDataPortResetCounters": rbNpuDataPortResetCounters,
       "rbNpuDataPortTotalPacketsRx": rbNpuDataPortTotalPacketsRx,
       "rbNpuDataPortMangementPacketsFw": rbNpuDataPortMangementPacketsFw,
       "rbNpuDataPortPacketsFwToSlot1": rbNpuDataPortPacketsFwToSlot1,
       "rbNpuDataPortPacketsFwToSlot2": rbNpuDataPortPacketsFwToSlot2,
       "rbNpuDataPortPacketsFwToSlot3": rbNpuDataPortPacketsFwToSlot3,
       "rbNpuDataPortPacketsFwToSlot4": rbNpuDataPortPacketsFwToSlot4,
       "rbNpuDataPortPacketsFwToSlot7": rbNpuDataPortPacketsFwToSlot7,
       "rbNpuDataPortPacketsFwToSlot8": rbNpuDataPortPacketsFwToSlot8,
       "rbNpuDataPortPacketsFwToSlot9": rbNpuDataPortPacketsFwToSlot9,
       "rbNpuDataPortPacketsDiscardedOnRx": rbNpuDataPortPacketsDiscardedOnRx,
       "rbNpuDataPortTotalPacketsTx": rbNpuDataPortTotalPacketsTx,
       "rbNpuDataPortMangementPacketsSbmt": rbNpuDataPortMangementPacketsSbmt,
       "rbNpuDataPortPacketsSbmtFromSlot1": rbNpuDataPortPacketsSbmtFromSlot1,
       "rbNpuDataPortPacketsSbmtFromSlot2": rbNpuDataPortPacketsSbmtFromSlot2,
       "rbNpuDataPortPacketsSbmtFromSlot3": rbNpuDataPortPacketsSbmtFromSlot3,
       "rbNpuDataPortPacketsSbmtFromSlot4": rbNpuDataPortPacketsSbmtFromSlot4,
       "rbNpuDataPortPacketsSbmtFromSlot7": rbNpuDataPortPacketsSbmtFromSlot7,
       "rbNpuDataPortPacketsSbmtFromSlot8": rbNpuDataPortPacketsSbmtFromSlot8,
       "rbNpuDataPortPacketsSbmtFromSlot9": rbNpuDataPortPacketsSbmtFromSlot9,
       "rbNpuDataPortPacketsDiscardedOnTx": rbNpuDataPortPacketsDiscardedOnTx,
       "rbMBSTDataPortCounters": rbMBSTDataPortCounters,
       "rbMBSTDataPortCountersTable": rbMBSTDataPortCountersTable,
       "rbMBSTDataPortCountersEntry": rbMBSTDataPortCountersEntry,
       "rbMBSTDataPortIfSlot": rbMBSTDataPortIfSlot,
       "rbMBSTDataPortResetCounters": rbMBSTDataPortResetCounters,
       "rbMBSTDataPortTotalBytesRx": rbMBSTDataPortTotalBytesRx,
       "rbMBSTDataPortDataBytesRx": rbMBSTDataPortDataBytesRx,
       "rbMBSTDataPortDataBytesDiscardedOnRx": rbMBSTDataPortDataBytesDiscardedOnRx,
       "rbMBSTDataPortTotalBytesTx": rbMBSTDataPortTotalBytesTx,
       "rbMBSTDataPortDataBytesTx": rbMBSTDataPortDataBytesTx,
       "rbMBSTDataPortDataBytesDiscardedOnTx": rbMBSTDataPortDataBytesDiscardedOnTx,
       "rbManagementPortCounters": rbManagementPortCounters,
       "rbMngmntPortCountersTable": rbMngmntPortCountersTable,
       "rbMngmntPortCountersEntry": rbMngmntPortCountersEntry,
       "rbMngmntPortResetCounters": rbMngmntPortResetCounters,
       "rbMngmntPortPacketsRx": rbMngmntPortPacketsRx,
       "rbMngmntPortPacketsDiscardedOnRx": rbMngmntPortPacketsDiscardedOnRx,
       "rbMngmntPortPacketsTx": rbMngmntPortPacketsTx,
       "rbMngmntPortPacketsDiscardedOnTx": rbMngmntPortPacketsDiscardedOnTx,
       "rbMngmntPortIfSlot": rbMngmntPortIfSlot,
       "rbSUEthernetCounters": rbSUEthernetCounters,
       "rbSUEthernetCountersTable": rbSUEthernetCountersTable,
       "rbSUEthernetCountersEntry": rbSUEthernetCountersEntry,
       "rbPMIfSuMacAddr": rbPMIfSuMacAddr,
       "rbSUEthernetResetCounters": rbSUEthernetResetCounters,
       "rbSUEthernetDataBytesRx": rbSUEthernetDataBytesRx,
       "rbSUEthernetDataBytesDiscardedOnRx": rbSUEthernetDataBytesDiscardedOnRx,
       "rbSUEthernetDataBytesTx": rbSUEthernetDataBytesTx,
       "rbSUEthernetDataBytesDiscardedOnTx": rbSUEthernetDataBytesDiscardedOnTx,
       "rbSUWirelessCounters": rbSUWirelessCounters,
       "rbSUWirelessCountersTable": rbSUWirelessCountersTable,
       "rbSUWirelessCountersEntry": rbSUWirelessCountersEntry,
       "rbSUWirelessResetCounters": rbSUWirelessResetCounters,
       "rbSUWirelessDataBytesRx": rbSUWirelessDataBytesRx,
       "rbSUWirelessDataBytesDiscardedOnRx": rbSUWirelessDataBytesDiscardedOnRx,
       "rbSUWirelessDataBytesTx": rbSUWirelessDataBytesTx,
       "rbSUWirelessDataBytesDiscardedOnTx": rbSUWirelessDataBytesDiscardedOnTx,
       "rbSUWirelessARQEnabledBytesTx": rbSUWirelessARQEnabledBytesTx,
       "rbSUWirelessRTxBytes": rbSUWirelessRTxBytes,
       "rbSUWirelessRTxRate": rbSUWirelessRTxRate,
       "rbAUBackplaneCounters": rbAUBackplaneCounters,
       "rbAUBackplaneCountersTable": rbAUBackplaneCountersTable,
       "rbAUBackplaneCountersEntry": rbAUBackplaneCountersEntry,
       "rbPMIfAUSlot": rbPMIfAUSlot,
       "rbAUBackplaneResetCounters": rbAUBackplaneResetCounters,
       "rbAUBackplaneDataBytesRx": rbAUBackplaneDataBytesRx,
       "rbAUBackplaneDataBytesDiscardedOnRx": rbAUBackplaneDataBytesDiscardedOnRx,
       "rbAUBackplaneDataBytesTx": rbAUBackplaneDataBytesTx,
       "rbAUBackplaneDataBytesDiscardedOnTx": rbAUBackplaneDataBytesDiscardedOnTx,
       "rbAUWirelessCounters": rbAUWirelessCounters,
       "rbAUWirelessCountersTable": rbAUWirelessCountersTable,
       "rbAUWirelessCountersEntry": rbAUWirelessCountersEntry,
       "rbAUWirelessResetCounters": rbAUWirelessResetCounters,
       "rbAUWirelessDataBytesRx": rbAUWirelessDataBytesRx,
       "rbAUWirelessDataBytesDiscardedOnRx": rbAUWirelessDataBytesDiscardedOnRx,
       "rbAUWirelessDataBytesTx": rbAUWirelessDataBytesTx,
       "rbAUWirelessDataBytesDiscardedOnTx": rbAUWirelessDataBytesDiscardedOnTx,
       "rbAUWirelessARQEnabledBytesTx": rbAUWirelessARQEnabledBytesTx,
       "rbAUWirelessRTxBytes": rbAUWirelessRTxBytes,
       "rbAUWirelessRTxRate": rbAUWirelessRTxRate,
       "rbAUWirelessAUSlot": rbAUWirelessAUSlot}
)
