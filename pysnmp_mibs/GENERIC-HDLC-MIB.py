_F='read-write'
_E='Integer32'
_D='nnbundleId'
_C='BUNDLE-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
nnbundleId,=mibBuilder.importSymbols(_C,_D)
ntEnterpriseDataTasmanMgmt,=mibBuilder.importSymbols('NT-ENTERPRISE-DATA-MIB','ntEnterpriseDataTasmanMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
nngenHdlcMib=ModuleIdentity((1,3,6,1,4,1,562,73,1,1,1,15))
_NngenHdlcTable_Object=MibTable
nngenHdlcTable=_NngenHdlcTable_Object((1,3,6,1,4,1,562,73,1,1,1,15,1))
if mibBuilder.loadTexts:nngenHdlcTable.setStatus(_A)
_NngenHdlcTableEntry_Object=MibTableRow
nngenHdlcTableEntry=_NngenHdlcTableEntry_Object((1,3,6,1,4,1,562,73,1,1,1,15,1,1))
nngenHdlcTableEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:nngenHdlcTableEntry.setStatus(_A)
class _NngenHdlcKeepAlive_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,120))
_NngenHdlcKeepAlive_Type.__name__=_E
_NngenHdlcKeepAlive_Object=MibTableColumn
nngenHdlcKeepAlive=_NngenHdlcKeepAlive_Object((1,3,6,1,4,1,562,73,1,1,1,15,1,1,1),_NngenHdlcKeepAlive_Type())
nngenHdlcKeepAlive.setMaxAccess(_F)
if mibBuilder.loadTexts:nngenHdlcKeepAlive.setStatus(_A)
if mibBuilder.loadTexts:nngenHdlcKeepAlive.setUnits('seconds')
class _NngenHdlcMtu_Type(Integer32):defaultValue=1500
_NngenHdlcMtu_Type.__name__=_E
_NngenHdlcMtu_Object=MibTableColumn
nngenHdlcMtu=_NngenHdlcMtu_Object((1,3,6,1,4,1,562,73,1,1,1,15,1,1,2),_NngenHdlcMtu_Type())
nngenHdlcMtu.setMaxAccess(_F)
if mibBuilder.loadTexts:nngenHdlcMtu.setStatus(_A)
_NngenHdlcStatsTable_Object=MibTable
nngenHdlcStatsTable=_NngenHdlcStatsTable_Object((1,3,6,1,4,1,562,73,1,1,1,15,2))
if mibBuilder.loadTexts:nngenHdlcStatsTable.setStatus(_A)
_NngenHdlcStatsTableEntry_Object=MibTableRow
nngenHdlcStatsTableEntry=_NngenHdlcStatsTableEntry_Object((1,3,6,1,4,1,562,73,1,1,1,15,2,1))
nngenHdlcStatsTableEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:nngenHdlcStatsTableEntry.setStatus(_A)
_NngenHdlcStatsBytesRxLastBootClear_Type=Counter32
_NngenHdlcStatsBytesRxLastBootClear_Object=MibTableColumn
nngenHdlcStatsBytesRxLastBootClear=_NngenHdlcStatsBytesRxLastBootClear_Object((1,3,6,1,4,1,562,73,1,1,1,15,2,1,1),_NngenHdlcStatsBytesRxLastBootClear_Type())
nngenHdlcStatsBytesRxLastBootClear.setMaxAccess(_B)
if mibBuilder.loadTexts:nngenHdlcStatsBytesRxLastBootClear.setStatus(_A)
_NngenHdlcStatsBytesTxLastBootClear_Type=Counter32
_NngenHdlcStatsBytesTxLastBootClear_Object=MibTableColumn
nngenHdlcStatsBytesTxLastBootClear=_NngenHdlcStatsBytesTxLastBootClear_Object((1,3,6,1,4,1,562,73,1,1,1,15,2,1,2),_NngenHdlcStatsBytesTxLastBootClear_Type())
nngenHdlcStatsBytesTxLastBootClear.setMaxAccess(_B)
if mibBuilder.loadTexts:nngenHdlcStatsBytesTxLastBootClear.setStatus(_A)
_NngenHdlcStatsPktsRxLastBootClear_Type=Counter32
_NngenHdlcStatsPktsRxLastBootClear_Object=MibTableColumn
nngenHdlcStatsPktsRxLastBootClear=_NngenHdlcStatsPktsRxLastBootClear_Object((1,3,6,1,4,1,562,73,1,1,1,15,2,1,3),_NngenHdlcStatsPktsRxLastBootClear_Type())
nngenHdlcStatsPktsRxLastBootClear.setMaxAccess(_B)
if mibBuilder.loadTexts:nngenHdlcStatsPktsRxLastBootClear.setStatus(_A)
_NngenHdlcStatsPktsTxLastBootClear_Type=Counter32
_NngenHdlcStatsPktsTxLastBootClear_Object=MibTableColumn
nngenHdlcStatsPktsTxLastBootClear=_NngenHdlcStatsPktsTxLastBootClear_Object((1,3,6,1,4,1,562,73,1,1,1,15,2,1,4),_NngenHdlcStatsPktsTxLastBootClear_Type())
nngenHdlcStatsPktsTxLastBootClear.setMaxAccess(_B)
if mibBuilder.loadTexts:nngenHdlcStatsPktsTxLastBootClear.setStatus(_A)
_NngenHdlcStatsErrPktsRxLastBootClear_Type=Counter32
_NngenHdlcStatsErrPktsRxLastBootClear_Object=MibTableColumn
nngenHdlcStatsErrPktsRxLastBootClear=_NngenHdlcStatsErrPktsRxLastBootClear_Object((1,3,6,1,4,1,562,73,1,1,1,15,2,1,5),_NngenHdlcStatsErrPktsRxLastBootClear_Type())
nngenHdlcStatsErrPktsRxLastBootClear.setMaxAccess(_B)
if mibBuilder.loadTexts:nngenHdlcStatsErrPktsRxLastBootClear.setStatus(_A)
_NngenHdlcStatsUpDownStatesLastBootClear_Type=Counter32
_NngenHdlcStatsUpDownStatesLastBootClear_Object=MibTableColumn
nngenHdlcStatsUpDownStatesLastBootClear=_NngenHdlcStatsUpDownStatesLastBootClear_Object((1,3,6,1,4,1,562,73,1,1,1,15,2,1,6),_NngenHdlcStatsUpDownStatesLastBootClear_Type())
nngenHdlcStatsUpDownStatesLastBootClear.setMaxAccess(_B)
if mibBuilder.loadTexts:nngenHdlcStatsUpDownStatesLastBootClear.setStatus(_A)
_NngenHdlcStatsBytesRxLastFiveMins_Type=Counter32
_NngenHdlcStatsBytesRxLastFiveMins_Object=MibTableColumn
nngenHdlcStatsBytesRxLastFiveMins=_NngenHdlcStatsBytesRxLastFiveMins_Object((1,3,6,1,4,1,562,73,1,1,1,15,2,1,7),_NngenHdlcStatsBytesRxLastFiveMins_Type())
nngenHdlcStatsBytesRxLastFiveMins.setMaxAccess(_B)
if mibBuilder.loadTexts:nngenHdlcStatsBytesRxLastFiveMins.setStatus(_A)
_NngenHdlcStatsBytesTxLastFiveMins_Type=Counter32
_NngenHdlcStatsBytesTxLastFiveMins_Object=MibTableColumn
nngenHdlcStatsBytesTxLastFiveMins=_NngenHdlcStatsBytesTxLastFiveMins_Object((1,3,6,1,4,1,562,73,1,1,1,15,2,1,8),_NngenHdlcStatsBytesTxLastFiveMins_Type())
nngenHdlcStatsBytesTxLastFiveMins.setMaxAccess(_B)
if mibBuilder.loadTexts:nngenHdlcStatsBytesTxLastFiveMins.setStatus(_A)
_NngenHdlcStatsPktsRxLastFiveMins_Type=Counter32
_NngenHdlcStatsPktsRxLastFiveMins_Object=MibTableColumn
nngenHdlcStatsPktsRxLastFiveMins=_NngenHdlcStatsPktsRxLastFiveMins_Object((1,3,6,1,4,1,562,73,1,1,1,15,2,1,9),_NngenHdlcStatsPktsRxLastFiveMins_Type())
nngenHdlcStatsPktsRxLastFiveMins.setMaxAccess(_B)
if mibBuilder.loadTexts:nngenHdlcStatsPktsRxLastFiveMins.setStatus(_A)
_NngenHdlcStatsPktsTxLastFiveMins_Type=Counter32
_NngenHdlcStatsPktsTxLastFiveMins_Object=MibTableColumn
nngenHdlcStatsPktsTxLastFiveMins=_NngenHdlcStatsPktsTxLastFiveMins_Object((1,3,6,1,4,1,562,73,1,1,1,15,2,1,10),_NngenHdlcStatsPktsTxLastFiveMins_Type())
nngenHdlcStatsPktsTxLastFiveMins.setMaxAccess(_B)
if mibBuilder.loadTexts:nngenHdlcStatsPktsTxLastFiveMins.setStatus(_A)
_NngenHdlcStatsErrPktsRxLastFiveMins_Type=Counter32
_NngenHdlcStatsErrPktsRxLastFiveMins_Object=MibTableColumn
nngenHdlcStatsErrPktsRxLastFiveMins=_NngenHdlcStatsErrPktsRxLastFiveMins_Object((1,3,6,1,4,1,562,73,1,1,1,15,2,1,11),_NngenHdlcStatsErrPktsRxLastFiveMins_Type())
nngenHdlcStatsErrPktsRxLastFiveMins.setMaxAccess(_B)
if mibBuilder.loadTexts:nngenHdlcStatsErrPktsRxLastFiveMins.setStatus(_A)
_NngenHdlcStatsUpDownStatesLastFiveMins_Type=Counter32
_NngenHdlcStatsUpDownStatesLastFiveMins_Object=MibTableColumn
nngenHdlcStatsUpDownStatesLastFiveMins=_NngenHdlcStatsUpDownStatesLastFiveMins_Object((1,3,6,1,4,1,562,73,1,1,1,15,2,1,12),_NngenHdlcStatsUpDownStatesLastFiveMins_Type())
nngenHdlcStatsUpDownStatesLastFiveMins.setMaxAccess(_B)
if mibBuilder.loadTexts:nngenHdlcStatsUpDownStatesLastFiveMins.setStatus(_A)
mibBuilder.exportSymbols('GENERIC-HDLC-MIB',**{'nngenHdlcMib':nngenHdlcMib,'nngenHdlcTable':nngenHdlcTable,'nngenHdlcTableEntry':nngenHdlcTableEntry,'nngenHdlcKeepAlive':nngenHdlcKeepAlive,'nngenHdlcMtu':nngenHdlcMtu,'nngenHdlcStatsTable':nngenHdlcStatsTable,'nngenHdlcStatsTableEntry':nngenHdlcStatsTableEntry,'nngenHdlcStatsBytesRxLastBootClear':nngenHdlcStatsBytesRxLastBootClear,'nngenHdlcStatsBytesTxLastBootClear':nngenHdlcStatsBytesTxLastBootClear,'nngenHdlcStatsPktsRxLastBootClear':nngenHdlcStatsPktsRxLastBootClear,'nngenHdlcStatsPktsTxLastBootClear':nngenHdlcStatsPktsTxLastBootClear,'nngenHdlcStatsErrPktsRxLastBootClear':nngenHdlcStatsErrPktsRxLastBootClear,'nngenHdlcStatsUpDownStatesLastBootClear':nngenHdlcStatsUpDownStatesLastBootClear,'nngenHdlcStatsBytesRxLastFiveMins':nngenHdlcStatsBytesRxLastFiveMins,'nngenHdlcStatsBytesTxLastFiveMins':nngenHdlcStatsBytesTxLastFiveMins,'nngenHdlcStatsPktsRxLastFiveMins':nngenHdlcStatsPktsRxLastFiveMins,'nngenHdlcStatsPktsTxLastFiveMins':nngenHdlcStatsPktsTxLastFiveMins,'nngenHdlcStatsErrPktsRxLastFiveMins':nngenHdlcStatsErrPktsRxLastFiveMins,'nngenHdlcStatsUpDownStatesLastFiveMins':nngenHdlcStatsUpDownStatesLastFiveMins})