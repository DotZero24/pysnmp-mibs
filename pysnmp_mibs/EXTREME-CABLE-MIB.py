_U='extremeDiagPortCfgStatus'
_T='extremeDiagPortStatsPortIfIndex'
_S='noswap'
_R='extremeDiagPortDiagMode'
_Q='extremeDiagPortDiagPortIfIndex'
_P='manual'
_O='extremeDiagPortCfgMode'
_N='extremeDiagPortCfgPortIfIndex'
_M='read-write'
_L='DisplayString'
_K='imperror'
_J='terminated'
_I='short'
_H='open'
_G='negative'
_F='positive'
_E='EXTREME-CABLE-MIB'
_D='unknown'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
extremeAgent,extremeV2Traps,extremenetworks=mibBuilder.importSymbols('EXTREME-BASE-MIB','extremeAgent','extremeV2Traps','extremenetworks')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_L,'PhysAddress','TextualConvention','TruthValue')
extremeCable=ModuleIdentity((1,3,6,1,4,1,1916,1,24))
_ExtremeDiagConfigGroup_ObjectIdentity=ObjectIdentity
extremeDiagConfigGroup=_ExtremeDiagConfigGroup_ObjectIdentity((1,3,6,1,4,1,1916,1,24,1))
class _ExtremeDiagConfigTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_ExtremeDiagConfigTime_Type.__name__=_L
_ExtremeDiagConfigTime_Object=MibScalar
extremeDiagConfigTime=_ExtremeDiagConfigTime_Object((1,3,6,1,4,1,1916,1,24,1,1),_ExtremeDiagConfigTime_Type())
extremeDiagConfigTime.setMaxAccess(_M)
if mibBuilder.loadTexts:extremeDiagConfigTime.setStatus(_A)
class _ExtremeDiagConfigRoF_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_ExtremeDiagConfigRoF_Type.__name__=_C
_ExtremeDiagConfigRoF_Object=MibScalar
extremeDiagConfigRoF=_ExtremeDiagConfigRoF_Object((1,3,6,1,4,1,1916,1,24,1,2),_ExtremeDiagConfigRoF_Type())
extremeDiagConfigRoF.setMaxAccess(_M)
if mibBuilder.loadTexts:extremeDiagConfigRoF.setStatus(_A)
_ExtremeDiagPortConfigTable_Object=MibTable
extremeDiagPortConfigTable=_ExtremeDiagPortConfigTable_Object((1,3,6,1,4,1,1916,1,24,2))
if mibBuilder.loadTexts:extremeDiagPortConfigTable.setStatus(_A)
_ExtremeDiagPortConfigEntry_Object=MibTableRow
extremeDiagPortConfigEntry=_ExtremeDiagPortConfigEntry_Object((1,3,6,1,4,1,1916,1,24,2,1))
extremeDiagPortConfigEntry.setIndexNames((0,_E,_N),(0,_E,_O))
if mibBuilder.loadTexts:extremeDiagPortConfigEntry.setStatus(_A)
_ExtremeDiagPortCfgPortIfIndex_Type=Integer32
_ExtremeDiagPortCfgPortIfIndex_Object=MibTableColumn
extremeDiagPortCfgPortIfIndex=_ExtremeDiagPortCfgPortIfIndex_Object((1,3,6,1,4,1,1916,1,24,2,1,1),_ExtremeDiagPortCfgPortIfIndex_Type())
extremeDiagPortCfgPortIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeDiagPortCfgPortIfIndex.setStatus(_A)
class _ExtremeDiagPortCfgMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('auto',1),(_P,2)))
_ExtremeDiagPortCfgMode_Type.__name__=_C
_ExtremeDiagPortCfgMode_Object=MibTableColumn
extremeDiagPortCfgMode=_ExtremeDiagPortCfgMode_Object((1,3,6,1,4,1,1916,1,24,2,1,2),_ExtremeDiagPortCfgMode_Type())
extremeDiagPortCfgMode.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeDiagPortCfgMode.setStatus(_A)
class _ExtremeDiagPortCfgStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('enable',1),('disable',2),('run',3),('diagfail',4)))
_ExtremeDiagPortCfgStatus_Type.__name__=_C
_ExtremeDiagPortCfgStatus_Object=MibTableColumn
extremeDiagPortCfgStatus=_ExtremeDiagPortCfgStatus_Object((1,3,6,1,4,1,1916,1,24,2,1,3),_ExtremeDiagPortCfgStatus_Type())
extremeDiagPortCfgStatus.setMaxAccess(_M)
if mibBuilder.loadTexts:extremeDiagPortCfgStatus.setStatus(_A)
_ExtremeDiagPortDiagTable_Object=MibTable
extremeDiagPortDiagTable=_ExtremeDiagPortDiagTable_Object((1,3,6,1,4,1,1916,1,24,3))
if mibBuilder.loadTexts:extremeDiagPortDiagTable.setStatus(_A)
_ExtremeDiagPortDiagEntry_Object=MibTableRow
extremeDiagPortDiagEntry=_ExtremeDiagPortDiagEntry_Object((1,3,6,1,4,1,1916,1,24,3,1))
extremeDiagPortDiagEntry.setIndexNames((0,_E,_Q),(0,_E,_R))
if mibBuilder.loadTexts:extremeDiagPortDiagEntry.setStatus(_A)
_ExtremeDiagPortDiagPortIfIndex_Type=Integer32
_ExtremeDiagPortDiagPortIfIndex_Object=MibTableColumn
extremeDiagPortDiagPortIfIndex=_ExtremeDiagPortDiagPortIfIndex_Object((1,3,6,1,4,1,1916,1,24,3,1,1),_ExtremeDiagPortDiagPortIfIndex_Type())
extremeDiagPortDiagPortIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeDiagPortDiagPortIfIndex.setStatus(_A)
class _ExtremeDiagPortDiagMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('auto',1),(_P,2)))
_ExtremeDiagPortDiagMode_Type.__name__=_C
_ExtremeDiagPortDiagMode_Object=MibTableColumn
extremeDiagPortDiagMode=_ExtremeDiagPortDiagMode_Object((1,3,6,1,4,1,1916,1,24,3,1,2),_ExtremeDiagPortDiagMode_Type())
extremeDiagPortDiagMode.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeDiagPortDiagMode.setStatus(_A)
class _ExtremeDiagPortSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('speed10',1),('speed100',2),('speed1000',3),(_D,4)))
_ExtremeDiagPortSpeed_Type.__name__=_C
_ExtremeDiagPortSpeed_Object=MibTableColumn
extremeDiagPortSpeed=_ExtremeDiagPortSpeed_Object((1,3,6,1,4,1,1916,1,24,3,1,3),_ExtremeDiagPortSpeed_Type())
extremeDiagPortSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeDiagPortSpeed.setStatus(_A)
class _ExtremeDiagPortSwapAB_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('swap',1),(_S,2),(_D,3)))
_ExtremeDiagPortSwapAB_Type.__name__=_C
_ExtremeDiagPortSwapAB_Object=MibTableColumn
extremeDiagPortSwapAB=_ExtremeDiagPortSwapAB_Object((1,3,6,1,4,1,1916,1,24,3,1,4),_ExtremeDiagPortSwapAB_Type())
extremeDiagPortSwapAB.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeDiagPortSwapAB.setStatus(_A)
class _ExtremeDiagPortSwapCD_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('swap',1),(_S,2),(_D,3)))
_ExtremeDiagPortSwapCD_Type.__name__=_C
_ExtremeDiagPortSwapCD_Object=MibTableColumn
extremeDiagPortSwapCD=_ExtremeDiagPortSwapCD_Object((1,3,6,1,4,1,1916,1,24,3,1,5),_ExtremeDiagPortSwapCD_Type())
extremeDiagPortSwapCD.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeDiagPortSwapCD.setStatus(_A)
class _ExtremeDiagPortPairAPol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_D,3)))
_ExtremeDiagPortPairAPol_Type.__name__=_C
_ExtremeDiagPortPairAPol_Object=MibTableColumn
extremeDiagPortPairAPol=_ExtremeDiagPortPairAPol_Object((1,3,6,1,4,1,1916,1,24,3,1,6),_ExtremeDiagPortPairAPol_Type())
extremeDiagPortPairAPol.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeDiagPortPairAPol.setStatus(_A)
_ExtremeDiagPortPairAFlen_Type=Integer32
_ExtremeDiagPortPairAFlen_Object=MibTableColumn
extremeDiagPortPairAFlen=_ExtremeDiagPortPairAFlen_Object((1,3,6,1,4,1,1916,1,24,3,1,7),_ExtremeDiagPortPairAFlen_Type())
extremeDiagPortPairAFlen.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeDiagPortPairAFlen.setStatus(_A)
_ExtremeDiagPortPairALen_Type=Integer32
_ExtremeDiagPortPairALen_Object=MibTableColumn
extremeDiagPortPairALen=_ExtremeDiagPortPairALen_Object((1,3,6,1,4,1,1916,1,24,3,1,8),_ExtremeDiagPortPairALen_Type())
extremeDiagPortPairALen.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeDiagPortPairALen.setStatus(_A)
_ExtremeDiagPortPairASkew_Type=Integer32
_ExtremeDiagPortPairASkew_Object=MibTableColumn
extremeDiagPortPairASkew=_ExtremeDiagPortPairASkew_Object((1,3,6,1,4,1,1916,1,24,3,1,9),_ExtremeDiagPortPairASkew_Type())
extremeDiagPortPairASkew.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeDiagPortPairASkew.setStatus(_A)
class _ExtremeDiagPortPairAStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_H,1),(_I,2),(_J,3),(_K,4),(_D,5)))
_ExtremeDiagPortPairAStatus_Type.__name__=_C
_ExtremeDiagPortPairAStatus_Object=MibTableColumn
extremeDiagPortPairAStatus=_ExtremeDiagPortPairAStatus_Object((1,3,6,1,4,1,1916,1,24,3,1,10),_ExtremeDiagPortPairAStatus_Type())
extremeDiagPortPairAStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeDiagPortPairAStatus.setStatus(_A)
class _ExtremeDiagPortPairBPol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_D,3)))
_ExtremeDiagPortPairBPol_Type.__name__=_C
_ExtremeDiagPortPairBPol_Object=MibTableColumn
extremeDiagPortPairBPol=_ExtremeDiagPortPairBPol_Object((1,3,6,1,4,1,1916,1,24,3,1,11),_ExtremeDiagPortPairBPol_Type())
extremeDiagPortPairBPol.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeDiagPortPairBPol.setStatus(_A)
_ExtremeDiagPortPairBFlen_Type=Integer32
_ExtremeDiagPortPairBFlen_Object=MibTableColumn
extremeDiagPortPairBFlen=_ExtremeDiagPortPairBFlen_Object((1,3,6,1,4,1,1916,1,24,3,1,12),_ExtremeDiagPortPairBFlen_Type())
extremeDiagPortPairBFlen.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeDiagPortPairBFlen.setStatus(_A)
_ExtremeDiagPortPairBLen_Type=Integer32
_ExtremeDiagPortPairBLen_Object=MibTableColumn
extremeDiagPortPairBLen=_ExtremeDiagPortPairBLen_Object((1,3,6,1,4,1,1916,1,24,3,1,13),_ExtremeDiagPortPairBLen_Type())
extremeDiagPortPairBLen.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeDiagPortPairBLen.setStatus(_A)
_ExtremeDiagPortPairBSkew_Type=Integer32
_ExtremeDiagPortPairBSkew_Object=MibTableColumn
extremeDiagPortPairBSkew=_ExtremeDiagPortPairBSkew_Object((1,3,6,1,4,1,1916,1,24,3,1,14),_ExtremeDiagPortPairBSkew_Type())
extremeDiagPortPairBSkew.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeDiagPortPairBSkew.setStatus(_A)
class _ExtremeDiagPortPairBStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_H,1),(_I,2),(_J,3),(_K,4),(_D,5)))
_ExtremeDiagPortPairBStatus_Type.__name__=_C
_ExtremeDiagPortPairBStatus_Object=MibTableColumn
extremeDiagPortPairBStatus=_ExtremeDiagPortPairBStatus_Object((1,3,6,1,4,1,1916,1,24,3,1,15),_ExtremeDiagPortPairBStatus_Type())
extremeDiagPortPairBStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeDiagPortPairBStatus.setStatus(_A)
class _ExtremeDiagPortPairCPol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_D,3)))
_ExtremeDiagPortPairCPol_Type.__name__=_C
_ExtremeDiagPortPairCPol_Object=MibTableColumn
extremeDiagPortPairCPol=_ExtremeDiagPortPairCPol_Object((1,3,6,1,4,1,1916,1,24,3,1,16),_ExtremeDiagPortPairCPol_Type())
extremeDiagPortPairCPol.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeDiagPortPairCPol.setStatus(_A)
_ExtremeDiagPortPairCFlen_Type=Integer32
_ExtremeDiagPortPairCFlen_Object=MibTableColumn
extremeDiagPortPairCFlen=_ExtremeDiagPortPairCFlen_Object((1,3,6,1,4,1,1916,1,24,3,1,17),_ExtremeDiagPortPairCFlen_Type())
extremeDiagPortPairCFlen.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeDiagPortPairCFlen.setStatus(_A)
_ExtremeDiagPortPairCLen_Type=Integer32
_ExtremeDiagPortPairCLen_Object=MibTableColumn
extremeDiagPortPairCLen=_ExtremeDiagPortPairCLen_Object((1,3,6,1,4,1,1916,1,24,3,1,18),_ExtremeDiagPortPairCLen_Type())
extremeDiagPortPairCLen.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeDiagPortPairCLen.setStatus(_A)
_ExtremeDiagPortPairCSkew_Type=Integer32
_ExtremeDiagPortPairCSkew_Object=MibTableColumn
extremeDiagPortPairCSkew=_ExtremeDiagPortPairCSkew_Object((1,3,6,1,4,1,1916,1,24,3,1,19),_ExtremeDiagPortPairCSkew_Type())
extremeDiagPortPairCSkew.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeDiagPortPairCSkew.setStatus(_A)
class _ExtremeDiagPortPairCStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_H,1),(_I,2),(_J,3),(_K,4),(_D,5)))
_ExtremeDiagPortPairCStatus_Type.__name__=_C
_ExtremeDiagPortPairCStatus_Object=MibTableColumn
extremeDiagPortPairCStatus=_ExtremeDiagPortPairCStatus_Object((1,3,6,1,4,1,1916,1,24,3,1,20),_ExtremeDiagPortPairCStatus_Type())
extremeDiagPortPairCStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeDiagPortPairCStatus.setStatus(_A)
class _ExtremeDiagPortPairDPol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_D,3)))
_ExtremeDiagPortPairDPol_Type.__name__=_C
_ExtremeDiagPortPairDPol_Object=MibTableColumn
extremeDiagPortPairDPol=_ExtremeDiagPortPairDPol_Object((1,3,6,1,4,1,1916,1,24,3,1,21),_ExtremeDiagPortPairDPol_Type())
extremeDiagPortPairDPol.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeDiagPortPairDPol.setStatus(_A)
_ExtremeDiagPortPairDFlen_Type=Integer32
_ExtremeDiagPortPairDFlen_Object=MibTableColumn
extremeDiagPortPairDFlen=_ExtremeDiagPortPairDFlen_Object((1,3,6,1,4,1,1916,1,24,3,1,22),_ExtremeDiagPortPairDFlen_Type())
extremeDiagPortPairDFlen.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeDiagPortPairDFlen.setStatus(_A)
_ExtremeDiagPortPairDLen_Type=Integer32
_ExtremeDiagPortPairDLen_Object=MibTableColumn
extremeDiagPortPairDLen=_ExtremeDiagPortPairDLen_Object((1,3,6,1,4,1,1916,1,24,3,1,23),_ExtremeDiagPortPairDLen_Type())
extremeDiagPortPairDLen.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeDiagPortPairDLen.setStatus(_A)
_ExtremeDiagPortPairDSkew_Type=Integer32
_ExtremeDiagPortPairDSkew_Object=MibTableColumn
extremeDiagPortPairDSkew=_ExtremeDiagPortPairDSkew_Object((1,3,6,1,4,1,1916,1,24,3,1,24),_ExtremeDiagPortPairDSkew_Type())
extremeDiagPortPairDSkew.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeDiagPortPairDSkew.setStatus(_A)
class _ExtremeDiagPortPairDStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_H,1),(_I,2),(_J,3),(_K,4),(_D,5)))
_ExtremeDiagPortPairDStatus_Type.__name__=_C
_ExtremeDiagPortPairDStatus_Object=MibTableColumn
extremeDiagPortPairDStatus=_ExtremeDiagPortPairDStatus_Object((1,3,6,1,4,1,1916,1,24,3,1,25),_ExtremeDiagPortPairDStatus_Type())
extremeDiagPortPairDStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeDiagPortPairDStatus.setStatus(_A)
class _ExtremeDiagPortDateTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_ExtremeDiagPortDateTime_Type.__name__=_L
_ExtremeDiagPortDateTime_Object=MibTableColumn
extremeDiagPortDateTime=_ExtremeDiagPortDateTime_Object((1,3,6,1,4,1,1916,1,24,3,1,26),_ExtremeDiagPortDateTime_Type())
extremeDiagPortDateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeDiagPortDateTime.setStatus(_A)
_ExtremeDiagPortStatsTable_Object=MibTable
extremeDiagPortStatsTable=_ExtremeDiagPortStatsTable_Object((1,3,6,1,4,1,1916,1,24,4))
if mibBuilder.loadTexts:extremeDiagPortStatsTable.setStatus(_A)
_ExtremeDiagPortStatsEntry_Object=MibTableRow
extremeDiagPortStatsEntry=_ExtremeDiagPortStatsEntry_Object((1,3,6,1,4,1,1916,1,24,4,1))
extremeDiagPortStatsEntry.setIndexNames((0,_E,_T))
if mibBuilder.loadTexts:extremeDiagPortStatsEntry.setStatus(_A)
_ExtremeDiagPortStatsPortIfIndex_Type=Integer32
_ExtremeDiagPortStatsPortIfIndex_Object=MibTableColumn
extremeDiagPortStatsPortIfIndex=_ExtremeDiagPortStatsPortIfIndex_Object((1,3,6,1,4,1,1916,1,24,4,1,1),_ExtremeDiagPortStatsPortIfIndex_Type())
extremeDiagPortStatsPortIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeDiagPortStatsPortIfIndex.setStatus(_A)
_ExtremeDiagPortStatsNumDiag_Type=Integer32
_ExtremeDiagPortStatsNumDiag_Object=MibTableColumn
extremeDiagPortStatsNumDiag=_ExtremeDiagPortStatsNumDiag_Object((1,3,6,1,4,1,1916,1,24,4,1,2),_ExtremeDiagPortStatsNumDiag_Type())
extremeDiagPortStatsNumDiag.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeDiagPortStatsNumDiag.setStatus(_A)
_ExtremeDiagPortStatsNumSuccess_Type=Integer32
_ExtremeDiagPortStatsNumSuccess_Object=MibTableColumn
extremeDiagPortStatsNumSuccess=_ExtremeDiagPortStatsNumSuccess_Object((1,3,6,1,4,1,1916,1,24,4,1,3),_ExtremeDiagPortStatsNumSuccess_Type())
extremeDiagPortStatsNumSuccess.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeDiagPortStatsNumSuccess.setStatus(_A)
_ExtremeDiagPortStatsNumFail_Type=Integer32
_ExtremeDiagPortStatsNumFail_Object=MibTableColumn
extremeDiagPortStatsNumFail=_ExtremeDiagPortStatsNumFail_Object((1,3,6,1,4,1,1916,1,24,4,1,4),_ExtremeDiagPortStatsNumFail_Type())
extremeDiagPortStatsNumFail.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeDiagPortStatsNumFail.setStatus(_A)
_ExtremeDiagPortStatsNumChange_Type=Integer32
_ExtremeDiagPortStatsNumChange_Object=MibTableColumn
extremeDiagPortStatsNumChange=_ExtremeDiagPortStatsNumChange_Object((1,3,6,1,4,1,1916,1,24,4,1,5),_ExtremeDiagPortStatsNumChange_Type())
extremeDiagPortStatsNumChange.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeDiagPortStatsNumChange.setStatus(_A)
_ExtremeDiagPortStatsNumAbort_Type=Integer32
_ExtremeDiagPortStatsNumAbort_Object=MibTableColumn
extremeDiagPortStatsNumAbort=_ExtremeDiagPortStatsNumAbort_Object((1,3,6,1,4,1,1916,1,24,4,1,6),_ExtremeDiagPortStatsNumAbort_Type())
extremeDiagPortStatsNumAbort.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeDiagPortStatsNumAbort.setStatus(_A)
_ExtremeCableTraps_ObjectIdentity=ObjectIdentity
extremeCableTraps=_ExtremeCableTraps_ObjectIdentity((1,3,6,1,4,1,1916,1,24,5))
_ExtremeCableTrapsPrefix_ObjectIdentity=ObjectIdentity
extremeCableTrapsPrefix=_ExtremeCableTrapsPrefix_ObjectIdentity((1,3,6,1,4,1,1916,1,24,5,0))
extremeTrapDiagPortDiagnostics=NotificationType((1,3,6,1,4,1,1916,1,24,5,0,1))
extremeTrapDiagPortDiagnostics.setObjects(*((_E,_N),(_E,_O),(_E,_U)))
if mibBuilder.loadTexts:extremeTrapDiagPortDiagnostics.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'extremeCable':extremeCable,'extremeDiagConfigGroup':extremeDiagConfigGroup,'extremeDiagConfigTime':extremeDiagConfigTime,'extremeDiagConfigRoF':extremeDiagConfigRoF,'extremeDiagPortConfigTable':extremeDiagPortConfigTable,'extremeDiagPortConfigEntry':extremeDiagPortConfigEntry,_N:extremeDiagPortCfgPortIfIndex,_O:extremeDiagPortCfgMode,_U:extremeDiagPortCfgStatus,'extremeDiagPortDiagTable':extremeDiagPortDiagTable,'extremeDiagPortDiagEntry':extremeDiagPortDiagEntry,_Q:extremeDiagPortDiagPortIfIndex,_R:extremeDiagPortDiagMode,'extremeDiagPortSpeed':extremeDiagPortSpeed,'extremeDiagPortSwapAB':extremeDiagPortSwapAB,'extremeDiagPortSwapCD':extremeDiagPortSwapCD,'extremeDiagPortPairAPol':extremeDiagPortPairAPol,'extremeDiagPortPairAFlen':extremeDiagPortPairAFlen,'extremeDiagPortPairALen':extremeDiagPortPairALen,'extremeDiagPortPairASkew':extremeDiagPortPairASkew,'extremeDiagPortPairAStatus':extremeDiagPortPairAStatus,'extremeDiagPortPairBPol':extremeDiagPortPairBPol,'extremeDiagPortPairBFlen':extremeDiagPortPairBFlen,'extremeDiagPortPairBLen':extremeDiagPortPairBLen,'extremeDiagPortPairBSkew':extremeDiagPortPairBSkew,'extremeDiagPortPairBStatus':extremeDiagPortPairBStatus,'extremeDiagPortPairCPol':extremeDiagPortPairCPol,'extremeDiagPortPairCFlen':extremeDiagPortPairCFlen,'extremeDiagPortPairCLen':extremeDiagPortPairCLen,'extremeDiagPortPairCSkew':extremeDiagPortPairCSkew,'extremeDiagPortPairCStatus':extremeDiagPortPairCStatus,'extremeDiagPortPairDPol':extremeDiagPortPairDPol,'extremeDiagPortPairDFlen':extremeDiagPortPairDFlen,'extremeDiagPortPairDLen':extremeDiagPortPairDLen,'extremeDiagPortPairDSkew':extremeDiagPortPairDSkew,'extremeDiagPortPairDStatus':extremeDiagPortPairDStatus,'extremeDiagPortDateTime':extremeDiagPortDateTime,'extremeDiagPortStatsTable':extremeDiagPortStatsTable,'extremeDiagPortStatsEntry':extremeDiagPortStatsEntry,_T:extremeDiagPortStatsPortIfIndex,'extremeDiagPortStatsNumDiag':extremeDiagPortStatsNumDiag,'extremeDiagPortStatsNumSuccess':extremeDiagPortStatsNumSuccess,'extremeDiagPortStatsNumFail':extremeDiagPortStatsNumFail,'extremeDiagPortStatsNumChange':extremeDiagPortStatsNumChange,'extremeDiagPortStatsNumAbort':extremeDiagPortStatsNumAbort,'extremeCableTraps':extremeCableTraps,'extremeCableTrapsPrefix':extremeCableTrapsPrefix,'extremeTrapDiagPortDiagnostics':extremeTrapDiagPortDiagnostics})