_A8='hcPrio100mbPlusGroup'
_A7='hcPrioTo100mbGroup'
_A6='hcVlan100mbPlusGroup'
_A5='hcVlanTo100mbGroup'
_A4='smonHc100mbPlusGroup'
_A3='smonHcTo100mbGroup'
_A2='portCopyStatus'
_A1='portCopyDirection'
_A0='portCopyDestDropEvents'
_z='smonCapabilities'
_y='smonVlanIdStatsNUcastHCOctets'
_x='smonVlanIdStatsNUcastOverflowOctets'
_w='smonVlanIdStatsNUcastOctets'
_v='smonPrioStatsOctets'
_u='smonPrioStatsPkts'
_t='smonPrioStatsControlStatus'
_s='smonPrioStatsControlOwner'
_r='smonPrioStatsControlCreateTime'
_q='smonPrioStatsControlDataSource'
_p='smonVlanIdStatsCreateTime'
_o='smonVlanIdStatsNUcastPkts'
_n='smonVlanIdStatsTotalOctets'
_m='smonVlanIdStatsTotalPkts'
_l='smonVlanStatsControlStatus'
_k='smonVlanStatsControlOwner'
_j='smonVlanStatsControlCreateTime'
_i='smonVlanStatsControlDataSource'
_h='dataSourceCapsIfIndex'
_g='dataSourceCopyCaps'
_f='dataSourceRmonCaps'
_e='portCopyDest'
_d='portCopySource'
_c='smonPrioStatsId'
_b='smonVlanIdStatsId'
_a='dataSourceCapsObject'
_Z='portCopyConfigGroup'
_Y='smonPrioStatsGroup'
_X='smonVlanStatsGroup'
_W='smonPrioStatsHCPkts'
_V='smonPrioStatsOverflowPkts'
_U='smonVlanIdStatsNUcastHCPkts'
_T='smonVlanIdStatsNUcastOverflowPkts'
_S='smonVlanIdStatsTotalHCPkts'
_R='smonVlanIdStatsTotalOverflowPkts'
_Q='smonPrioStatsControlIndex'
_P='smonVlanStatsControlIndex'
_O='Bits'
_N='smonInformationGroup'
_M='dataSourceCapsGroup'
_L='smonPrioStatsHCOctets'
_K='smonPrioStatsOverflowOctets'
_J='smonVlanIdStatsTotalHCOctets'
_I='smonVlanIdStatsTotalOverflowOctets'
_H='Integer32'
_G='not-accessible'
_F='read-create'
_E='octets'
_D='packets'
_C='read-only'
_B='current'
_A='SMON-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
OwnerString,rmon=mibBuilder.importSymbols('RMON-MIB','OwnerString','rmon')
DataSource,LastCreateTime,probeConfig,rmonConformance=mibBuilder.importSymbols('RMON2-MIB','DataSource','LastCreateTime','probeConfig','rmonConformance')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_O,'Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
switchRMON=ModuleIdentity((1,3,6,1,2,1,16,22))
if mibBuilder.loadTexts:switchRMON.setRevisions(('1998-12-16 00:00',))
class SmonDataSource(TextualConvention,ObjectIdentifier):status=_B
class _SmonCapabilities_Type(Bits):namedValues=NamedValues(*(('smonVlanStats',0),('smonPrioStats',1),('dataSource',2),('smonUnusedBit',3),('portCopy',4)))
_SmonCapabilities_Type.__name__=_O
_SmonCapabilities_Object=MibScalar
smonCapabilities=_SmonCapabilities_Object((1,3,6,1,2,1,16,19,15),_SmonCapabilities_Type())
smonCapabilities.setMaxAccess(_C)
if mibBuilder.loadTexts:smonCapabilities.setStatus(_B)
_SmonMIBCompliances_ObjectIdentity=ObjectIdentity
smonMIBCompliances=_SmonMIBCompliances_ObjectIdentity((1,3,6,1,2,1,16,20,3))
_SmonMIBGroups_ObjectIdentity=ObjectIdentity
smonMIBGroups=_SmonMIBGroups_ObjectIdentity((1,3,6,1,2,1,16,20,4))
_SmonMIBObjects_ObjectIdentity=ObjectIdentity
smonMIBObjects=_SmonMIBObjects_ObjectIdentity((1,3,6,1,2,1,16,22,1))
_DataSourceCaps_ObjectIdentity=ObjectIdentity
dataSourceCaps=_DataSourceCaps_ObjectIdentity((1,3,6,1,2,1,16,22,1,1))
_DataSourceCapsTable_Object=MibTable
dataSourceCapsTable=_DataSourceCapsTable_Object((1,3,6,1,2,1,16,22,1,1,1))
if mibBuilder.loadTexts:dataSourceCapsTable.setStatus(_B)
_DataSourceCapsEntry_Object=MibTableRow
dataSourceCapsEntry=_DataSourceCapsEntry_Object((1,3,6,1,2,1,16,22,1,1,1,1))
dataSourceCapsEntry.setIndexNames((1,_A,_a))
if mibBuilder.loadTexts:dataSourceCapsEntry.setStatus(_B)
_DataSourceCapsObject_Type=SmonDataSource
_DataSourceCapsObject_Object=MibTableColumn
dataSourceCapsObject=_DataSourceCapsObject_Object((1,3,6,1,2,1,16,22,1,1,1,1,1),_DataSourceCapsObject_Type())
dataSourceCapsObject.setMaxAccess(_G)
if mibBuilder.loadTexts:dataSourceCapsObject.setStatus(_B)
class _DataSourceRmonCaps_Type(Bits):namedValues=NamedValues(*(('countErrFrames',0),('countAllGoodFrames',1),('countAnyRmonTables',2),('babyGiantsCountAsGood',3)))
_DataSourceRmonCaps_Type.__name__=_O
_DataSourceRmonCaps_Object=MibTableColumn
dataSourceRmonCaps=_DataSourceRmonCaps_Object((1,3,6,1,2,1,16,22,1,1,1,1,2),_DataSourceRmonCaps_Type())
dataSourceRmonCaps.setMaxAccess(_C)
if mibBuilder.loadTexts:dataSourceRmonCaps.setStatus(_B)
class _DataSourceCopyCaps_Type(Bits):namedValues=NamedValues(*(('copySourcePort',0),('copyDestPort',1),('copySrcTxTraffic',2),('copySrcRxTraffic',3),('countDestDropEvents',4),('copyErrFrames',5),('copyUnalteredFrames',6),('copyAllGoodFrames',7)))
_DataSourceCopyCaps_Type.__name__=_O
_DataSourceCopyCaps_Object=MibTableColumn
dataSourceCopyCaps=_DataSourceCopyCaps_Object((1,3,6,1,2,1,16,22,1,1,1,1,3),_DataSourceCopyCaps_Type())
dataSourceCopyCaps.setMaxAccess(_C)
if mibBuilder.loadTexts:dataSourceCopyCaps.setStatus(_B)
_DataSourceCapsIfIndex_Type=InterfaceIndex
_DataSourceCapsIfIndex_Object=MibTableColumn
dataSourceCapsIfIndex=_DataSourceCapsIfIndex_Object((1,3,6,1,2,1,16,22,1,1,1,1,4),_DataSourceCapsIfIndex_Type())
dataSourceCapsIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:dataSourceCapsIfIndex.setStatus(_B)
_SmonStats_ObjectIdentity=ObjectIdentity
smonStats=_SmonStats_ObjectIdentity((1,3,6,1,2,1,16,22,1,2))
_SmonVlanStatsControlTable_Object=MibTable
smonVlanStatsControlTable=_SmonVlanStatsControlTable_Object((1,3,6,1,2,1,16,22,1,2,1))
if mibBuilder.loadTexts:smonVlanStatsControlTable.setStatus(_B)
_SmonVlanStatsControlEntry_Object=MibTableRow
smonVlanStatsControlEntry=_SmonVlanStatsControlEntry_Object((1,3,6,1,2,1,16,22,1,2,1,1))
smonVlanStatsControlEntry.setIndexNames((0,_A,_P))
if mibBuilder.loadTexts:smonVlanStatsControlEntry.setStatus(_B)
class _SmonVlanStatsControlIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SmonVlanStatsControlIndex_Type.__name__=_H
_SmonVlanStatsControlIndex_Object=MibTableColumn
smonVlanStatsControlIndex=_SmonVlanStatsControlIndex_Object((1,3,6,1,2,1,16,22,1,2,1,1,1),_SmonVlanStatsControlIndex_Type())
smonVlanStatsControlIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:smonVlanStatsControlIndex.setStatus(_B)
_SmonVlanStatsControlDataSource_Type=DataSource
_SmonVlanStatsControlDataSource_Object=MibTableColumn
smonVlanStatsControlDataSource=_SmonVlanStatsControlDataSource_Object((1,3,6,1,2,1,16,22,1,2,1,1,2),_SmonVlanStatsControlDataSource_Type())
smonVlanStatsControlDataSource.setMaxAccess(_F)
if mibBuilder.loadTexts:smonVlanStatsControlDataSource.setStatus(_B)
_SmonVlanStatsControlCreateTime_Type=LastCreateTime
_SmonVlanStatsControlCreateTime_Object=MibTableColumn
smonVlanStatsControlCreateTime=_SmonVlanStatsControlCreateTime_Object((1,3,6,1,2,1,16,22,1,2,1,1,3),_SmonVlanStatsControlCreateTime_Type())
smonVlanStatsControlCreateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:smonVlanStatsControlCreateTime.setStatus(_B)
_SmonVlanStatsControlOwner_Type=OwnerString
_SmonVlanStatsControlOwner_Object=MibTableColumn
smonVlanStatsControlOwner=_SmonVlanStatsControlOwner_Object((1,3,6,1,2,1,16,22,1,2,1,1,4),_SmonVlanStatsControlOwner_Type())
smonVlanStatsControlOwner.setMaxAccess(_F)
if mibBuilder.loadTexts:smonVlanStatsControlOwner.setStatus(_B)
_SmonVlanStatsControlStatus_Type=RowStatus
_SmonVlanStatsControlStatus_Object=MibTableColumn
smonVlanStatsControlStatus=_SmonVlanStatsControlStatus_Object((1,3,6,1,2,1,16,22,1,2,1,1,5),_SmonVlanStatsControlStatus_Type())
smonVlanStatsControlStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:smonVlanStatsControlStatus.setStatus(_B)
_SmonVlanIdStatsTable_Object=MibTable
smonVlanIdStatsTable=_SmonVlanIdStatsTable_Object((1,3,6,1,2,1,16,22,1,2,2))
if mibBuilder.loadTexts:smonVlanIdStatsTable.setStatus(_B)
_SmonVlanIdStatsEntry_Object=MibTableRow
smonVlanIdStatsEntry=_SmonVlanIdStatsEntry_Object((1,3,6,1,2,1,16,22,1,2,2,1))
smonVlanIdStatsEntry.setIndexNames((0,_A,_P),(0,_A,_b))
if mibBuilder.loadTexts:smonVlanIdStatsEntry.setStatus(_B)
class _SmonVlanIdStatsId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_SmonVlanIdStatsId_Type.__name__=_H
_SmonVlanIdStatsId_Object=MibTableColumn
smonVlanIdStatsId=_SmonVlanIdStatsId_Object((1,3,6,1,2,1,16,22,1,2,2,1,1),_SmonVlanIdStatsId_Type())
smonVlanIdStatsId.setMaxAccess(_G)
if mibBuilder.loadTexts:smonVlanIdStatsId.setStatus(_B)
_SmonVlanIdStatsTotalPkts_Type=Counter32
_SmonVlanIdStatsTotalPkts_Object=MibTableColumn
smonVlanIdStatsTotalPkts=_SmonVlanIdStatsTotalPkts_Object((1,3,6,1,2,1,16,22,1,2,2,1,2),_SmonVlanIdStatsTotalPkts_Type())
smonVlanIdStatsTotalPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:smonVlanIdStatsTotalPkts.setStatus(_B)
if mibBuilder.loadTexts:smonVlanIdStatsTotalPkts.setUnits(_D)
_SmonVlanIdStatsTotalOverflowPkts_Type=Counter32
_SmonVlanIdStatsTotalOverflowPkts_Object=MibTableColumn
smonVlanIdStatsTotalOverflowPkts=_SmonVlanIdStatsTotalOverflowPkts_Object((1,3,6,1,2,1,16,22,1,2,2,1,3),_SmonVlanIdStatsTotalOverflowPkts_Type())
smonVlanIdStatsTotalOverflowPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:smonVlanIdStatsTotalOverflowPkts.setStatus(_B)
if mibBuilder.loadTexts:smonVlanIdStatsTotalOverflowPkts.setUnits(_D)
_SmonVlanIdStatsTotalHCPkts_Type=Counter64
_SmonVlanIdStatsTotalHCPkts_Object=MibTableColumn
smonVlanIdStatsTotalHCPkts=_SmonVlanIdStatsTotalHCPkts_Object((1,3,6,1,2,1,16,22,1,2,2,1,4),_SmonVlanIdStatsTotalHCPkts_Type())
smonVlanIdStatsTotalHCPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:smonVlanIdStatsTotalHCPkts.setStatus(_B)
if mibBuilder.loadTexts:smonVlanIdStatsTotalHCPkts.setUnits(_D)
_SmonVlanIdStatsTotalOctets_Type=Counter32
_SmonVlanIdStatsTotalOctets_Object=MibTableColumn
smonVlanIdStatsTotalOctets=_SmonVlanIdStatsTotalOctets_Object((1,3,6,1,2,1,16,22,1,2,2,1,5),_SmonVlanIdStatsTotalOctets_Type())
smonVlanIdStatsTotalOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:smonVlanIdStatsTotalOctets.setStatus(_B)
if mibBuilder.loadTexts:smonVlanIdStatsTotalOctets.setUnits(_E)
_SmonVlanIdStatsTotalOverflowOctets_Type=Counter32
_SmonVlanIdStatsTotalOverflowOctets_Object=MibTableColumn
smonVlanIdStatsTotalOverflowOctets=_SmonVlanIdStatsTotalOverflowOctets_Object((1,3,6,1,2,1,16,22,1,2,2,1,6),_SmonVlanIdStatsTotalOverflowOctets_Type())
smonVlanIdStatsTotalOverflowOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:smonVlanIdStatsTotalOverflowOctets.setStatus(_B)
if mibBuilder.loadTexts:smonVlanIdStatsTotalOverflowOctets.setUnits(_E)
_SmonVlanIdStatsTotalHCOctets_Type=Counter64
_SmonVlanIdStatsTotalHCOctets_Object=MibTableColumn
smonVlanIdStatsTotalHCOctets=_SmonVlanIdStatsTotalHCOctets_Object((1,3,6,1,2,1,16,22,1,2,2,1,7),_SmonVlanIdStatsTotalHCOctets_Type())
smonVlanIdStatsTotalHCOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:smonVlanIdStatsTotalHCOctets.setStatus(_B)
if mibBuilder.loadTexts:smonVlanIdStatsTotalHCOctets.setUnits(_E)
_SmonVlanIdStatsNUcastPkts_Type=Counter32
_SmonVlanIdStatsNUcastPkts_Object=MibTableColumn
smonVlanIdStatsNUcastPkts=_SmonVlanIdStatsNUcastPkts_Object((1,3,6,1,2,1,16,22,1,2,2,1,8),_SmonVlanIdStatsNUcastPkts_Type())
smonVlanIdStatsNUcastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:smonVlanIdStatsNUcastPkts.setStatus(_B)
if mibBuilder.loadTexts:smonVlanIdStatsNUcastPkts.setUnits(_D)
_SmonVlanIdStatsNUcastOverflowPkts_Type=Counter32
_SmonVlanIdStatsNUcastOverflowPkts_Object=MibTableColumn
smonVlanIdStatsNUcastOverflowPkts=_SmonVlanIdStatsNUcastOverflowPkts_Object((1,3,6,1,2,1,16,22,1,2,2,1,9),_SmonVlanIdStatsNUcastOverflowPkts_Type())
smonVlanIdStatsNUcastOverflowPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:smonVlanIdStatsNUcastOverflowPkts.setStatus(_B)
if mibBuilder.loadTexts:smonVlanIdStatsNUcastOverflowPkts.setUnits(_D)
_SmonVlanIdStatsNUcastHCPkts_Type=Counter64
_SmonVlanIdStatsNUcastHCPkts_Object=MibTableColumn
smonVlanIdStatsNUcastHCPkts=_SmonVlanIdStatsNUcastHCPkts_Object((1,3,6,1,2,1,16,22,1,2,2,1,10),_SmonVlanIdStatsNUcastHCPkts_Type())
smonVlanIdStatsNUcastHCPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:smonVlanIdStatsNUcastHCPkts.setStatus(_B)
if mibBuilder.loadTexts:smonVlanIdStatsNUcastHCPkts.setUnits(_D)
_SmonVlanIdStatsNUcastOctets_Type=Counter32
_SmonVlanIdStatsNUcastOctets_Object=MibTableColumn
smonVlanIdStatsNUcastOctets=_SmonVlanIdStatsNUcastOctets_Object((1,3,6,1,2,1,16,22,1,2,2,1,11),_SmonVlanIdStatsNUcastOctets_Type())
smonVlanIdStatsNUcastOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:smonVlanIdStatsNUcastOctets.setStatus(_B)
if mibBuilder.loadTexts:smonVlanIdStatsNUcastOctets.setUnits(_E)
_SmonVlanIdStatsNUcastOverflowOctets_Type=Counter32
_SmonVlanIdStatsNUcastOverflowOctets_Object=MibTableColumn
smonVlanIdStatsNUcastOverflowOctets=_SmonVlanIdStatsNUcastOverflowOctets_Object((1,3,6,1,2,1,16,22,1,2,2,1,12),_SmonVlanIdStatsNUcastOverflowOctets_Type())
smonVlanIdStatsNUcastOverflowOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:smonVlanIdStatsNUcastOverflowOctets.setStatus(_B)
if mibBuilder.loadTexts:smonVlanIdStatsNUcastOverflowOctets.setUnits(_E)
_SmonVlanIdStatsNUcastHCOctets_Type=Counter64
_SmonVlanIdStatsNUcastHCOctets_Object=MibTableColumn
smonVlanIdStatsNUcastHCOctets=_SmonVlanIdStatsNUcastHCOctets_Object((1,3,6,1,2,1,16,22,1,2,2,1,13),_SmonVlanIdStatsNUcastHCOctets_Type())
smonVlanIdStatsNUcastHCOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:smonVlanIdStatsNUcastHCOctets.setStatus(_B)
if mibBuilder.loadTexts:smonVlanIdStatsNUcastHCOctets.setUnits(_E)
_SmonVlanIdStatsCreateTime_Type=LastCreateTime
_SmonVlanIdStatsCreateTime_Object=MibTableColumn
smonVlanIdStatsCreateTime=_SmonVlanIdStatsCreateTime_Object((1,3,6,1,2,1,16,22,1,2,2,1,14),_SmonVlanIdStatsCreateTime_Type())
smonVlanIdStatsCreateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:smonVlanIdStatsCreateTime.setStatus(_B)
_SmonPrioStatsControlTable_Object=MibTable
smonPrioStatsControlTable=_SmonPrioStatsControlTable_Object((1,3,6,1,2,1,16,22,1,2,3))
if mibBuilder.loadTexts:smonPrioStatsControlTable.setStatus(_B)
_SmonPrioStatsControlEntry_Object=MibTableRow
smonPrioStatsControlEntry=_SmonPrioStatsControlEntry_Object((1,3,6,1,2,1,16,22,1,2,3,1))
smonPrioStatsControlEntry.setIndexNames((0,_A,_Q))
if mibBuilder.loadTexts:smonPrioStatsControlEntry.setStatus(_B)
class _SmonPrioStatsControlIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SmonPrioStatsControlIndex_Type.__name__=_H
_SmonPrioStatsControlIndex_Object=MibTableColumn
smonPrioStatsControlIndex=_SmonPrioStatsControlIndex_Object((1,3,6,1,2,1,16,22,1,2,3,1,1),_SmonPrioStatsControlIndex_Type())
smonPrioStatsControlIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:smonPrioStatsControlIndex.setStatus(_B)
_SmonPrioStatsControlDataSource_Type=DataSource
_SmonPrioStatsControlDataSource_Object=MibTableColumn
smonPrioStatsControlDataSource=_SmonPrioStatsControlDataSource_Object((1,3,6,1,2,1,16,22,1,2,3,1,2),_SmonPrioStatsControlDataSource_Type())
smonPrioStatsControlDataSource.setMaxAccess(_F)
if mibBuilder.loadTexts:smonPrioStatsControlDataSource.setStatus(_B)
_SmonPrioStatsControlCreateTime_Type=LastCreateTime
_SmonPrioStatsControlCreateTime_Object=MibTableColumn
smonPrioStatsControlCreateTime=_SmonPrioStatsControlCreateTime_Object((1,3,6,1,2,1,16,22,1,2,3,1,3),_SmonPrioStatsControlCreateTime_Type())
smonPrioStatsControlCreateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:smonPrioStatsControlCreateTime.setStatus(_B)
_SmonPrioStatsControlOwner_Type=OwnerString
_SmonPrioStatsControlOwner_Object=MibTableColumn
smonPrioStatsControlOwner=_SmonPrioStatsControlOwner_Object((1,3,6,1,2,1,16,22,1,2,3,1,4),_SmonPrioStatsControlOwner_Type())
smonPrioStatsControlOwner.setMaxAccess(_F)
if mibBuilder.loadTexts:smonPrioStatsControlOwner.setStatus(_B)
_SmonPrioStatsControlStatus_Type=RowStatus
_SmonPrioStatsControlStatus_Object=MibTableColumn
smonPrioStatsControlStatus=_SmonPrioStatsControlStatus_Object((1,3,6,1,2,1,16,22,1,2,3,1,5),_SmonPrioStatsControlStatus_Type())
smonPrioStatsControlStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:smonPrioStatsControlStatus.setStatus(_B)
_SmonPrioStatsTable_Object=MibTable
smonPrioStatsTable=_SmonPrioStatsTable_Object((1,3,6,1,2,1,16,22,1,2,4))
if mibBuilder.loadTexts:smonPrioStatsTable.setStatus(_B)
_SmonPrioStatsEntry_Object=MibTableRow
smonPrioStatsEntry=_SmonPrioStatsEntry_Object((1,3,6,1,2,1,16,22,1,2,4,1))
smonPrioStatsEntry.setIndexNames((0,_A,_Q),(0,_A,_c))
if mibBuilder.loadTexts:smonPrioStatsEntry.setStatus(_B)
class _SmonPrioStatsId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_SmonPrioStatsId_Type.__name__=_H
_SmonPrioStatsId_Object=MibTableColumn
smonPrioStatsId=_SmonPrioStatsId_Object((1,3,6,1,2,1,16,22,1,2,4,1,1),_SmonPrioStatsId_Type())
smonPrioStatsId.setMaxAccess(_G)
if mibBuilder.loadTexts:smonPrioStatsId.setStatus(_B)
_SmonPrioStatsPkts_Type=Counter32
_SmonPrioStatsPkts_Object=MibTableColumn
smonPrioStatsPkts=_SmonPrioStatsPkts_Object((1,3,6,1,2,1,16,22,1,2,4,1,2),_SmonPrioStatsPkts_Type())
smonPrioStatsPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:smonPrioStatsPkts.setStatus(_B)
if mibBuilder.loadTexts:smonPrioStatsPkts.setUnits(_D)
_SmonPrioStatsOverflowPkts_Type=Counter32
_SmonPrioStatsOverflowPkts_Object=MibTableColumn
smonPrioStatsOverflowPkts=_SmonPrioStatsOverflowPkts_Object((1,3,6,1,2,1,16,22,1,2,4,1,3),_SmonPrioStatsOverflowPkts_Type())
smonPrioStatsOverflowPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:smonPrioStatsOverflowPkts.setStatus(_B)
if mibBuilder.loadTexts:smonPrioStatsOverflowPkts.setUnits(_D)
_SmonPrioStatsHCPkts_Type=Counter64
_SmonPrioStatsHCPkts_Object=MibTableColumn
smonPrioStatsHCPkts=_SmonPrioStatsHCPkts_Object((1,3,6,1,2,1,16,22,1,2,4,1,4),_SmonPrioStatsHCPkts_Type())
smonPrioStatsHCPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:smonPrioStatsHCPkts.setStatus(_B)
if mibBuilder.loadTexts:smonPrioStatsHCPkts.setUnits(_D)
_SmonPrioStatsOctets_Type=Counter32
_SmonPrioStatsOctets_Object=MibTableColumn
smonPrioStatsOctets=_SmonPrioStatsOctets_Object((1,3,6,1,2,1,16,22,1,2,4,1,5),_SmonPrioStatsOctets_Type())
smonPrioStatsOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:smonPrioStatsOctets.setStatus(_B)
if mibBuilder.loadTexts:smonPrioStatsOctets.setUnits(_E)
_SmonPrioStatsOverflowOctets_Type=Counter32
_SmonPrioStatsOverflowOctets_Object=MibTableColumn
smonPrioStatsOverflowOctets=_SmonPrioStatsOverflowOctets_Object((1,3,6,1,2,1,16,22,1,2,4,1,6),_SmonPrioStatsOverflowOctets_Type())
smonPrioStatsOverflowOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:smonPrioStatsOverflowOctets.setStatus(_B)
if mibBuilder.loadTexts:smonPrioStatsOverflowOctets.setUnits(_E)
_SmonPrioStatsHCOctets_Type=Counter64
_SmonPrioStatsHCOctets_Object=MibTableColumn
smonPrioStatsHCOctets=_SmonPrioStatsHCOctets_Object((1,3,6,1,2,1,16,22,1,2,4,1,7),_SmonPrioStatsHCOctets_Type())
smonPrioStatsHCOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:smonPrioStatsHCOctets.setStatus(_B)
if mibBuilder.loadTexts:smonPrioStatsHCOctets.setUnits(_E)
_PortCopyConfig_ObjectIdentity=ObjectIdentity
portCopyConfig=_PortCopyConfig_ObjectIdentity((1,3,6,1,2,1,16,22,1,3))
_PortCopyTable_Object=MibTable
portCopyTable=_PortCopyTable_Object((1,3,6,1,2,1,16,22,1,3,1))
if mibBuilder.loadTexts:portCopyTable.setStatus(_B)
_PortCopyEntry_Object=MibTableRow
portCopyEntry=_PortCopyEntry_Object((1,3,6,1,2,1,16,22,1,3,1,1))
portCopyEntry.setIndexNames((0,_A,_d),(0,_A,_e))
if mibBuilder.loadTexts:portCopyEntry.setStatus(_B)
_PortCopySource_Type=InterfaceIndex
_PortCopySource_Object=MibTableColumn
portCopySource=_PortCopySource_Object((1,3,6,1,2,1,16,22,1,3,1,1,1),_PortCopySource_Type())
portCopySource.setMaxAccess(_G)
if mibBuilder.loadTexts:portCopySource.setStatus(_B)
_PortCopyDest_Type=InterfaceIndex
_PortCopyDest_Object=MibTableColumn
portCopyDest=_PortCopyDest_Object((1,3,6,1,2,1,16,22,1,3,1,1,2),_PortCopyDest_Type())
portCopyDest.setMaxAccess(_G)
if mibBuilder.loadTexts:portCopyDest.setStatus(_B)
_PortCopyDestDropEvents_Type=Counter32
_PortCopyDestDropEvents_Object=MibTableColumn
portCopyDestDropEvents=_PortCopyDestDropEvents_Object((1,3,6,1,2,1,16,22,1,3,1,1,3),_PortCopyDestDropEvents_Type())
portCopyDestDropEvents.setMaxAccess(_C)
if mibBuilder.loadTexts:portCopyDestDropEvents.setStatus(_B)
if mibBuilder.loadTexts:portCopyDestDropEvents.setUnits('events')
class _PortCopyDirection_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('copyRxOnly',1),('copyTxOnly',2),('copyBoth',3)))
_PortCopyDirection_Type.__name__=_H
_PortCopyDirection_Object=MibTableColumn
portCopyDirection=_PortCopyDirection_Object((1,3,6,1,2,1,16,22,1,3,1,1,4),_PortCopyDirection_Type())
portCopyDirection.setMaxAccess(_F)
if mibBuilder.loadTexts:portCopyDirection.setStatus(_B)
_PortCopyStatus_Type=RowStatus
_PortCopyStatus_Object=MibTableColumn
portCopyStatus=_PortCopyStatus_Object((1,3,6,1,2,1,16,22,1,3,1,1,5),_PortCopyStatus_Type())
portCopyStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:portCopyStatus.setStatus(_B)
_SmonRegistrationPoints_ObjectIdentity=ObjectIdentity
smonRegistrationPoints=_SmonRegistrationPoints_ObjectIdentity((1,3,6,1,2,1,16,22,1,4))
_SmonVlanDataSource_ObjectIdentity=ObjectIdentity
smonVlanDataSource=_SmonVlanDataSource_ObjectIdentity((1,3,6,1,2,1,16,22,1,4,1))
dataSourceCapsGroup=ObjectGroup((1,3,6,1,2,1,16,20,4,1))
dataSourceCapsGroup.setObjects(*((_A,_f),(_A,_g),(_A,_h)))
if mibBuilder.loadTexts:dataSourceCapsGroup.setStatus(_B)
smonVlanStatsGroup=ObjectGroup((1,3,6,1,2,1,16,20,4,2))
smonVlanStatsGroup.setObjects(*((_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p)))
if mibBuilder.loadTexts:smonVlanStatsGroup.setStatus(_B)
smonPrioStatsGroup=ObjectGroup((1,3,6,1,2,1,16,20,4,3))
smonPrioStatsGroup.setObjects(*((_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v)))
if mibBuilder.loadTexts:smonPrioStatsGroup.setStatus(_B)
smonHcTo100mbGroup=ObjectGroup((1,3,6,1,2,1,16,20,4,4))
smonHcTo100mbGroup.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:smonHcTo100mbGroup.setStatus(_B)
smonHc100mbPlusGroup=ObjectGroup((1,3,6,1,2,1,16,20,4,5))
smonHc100mbPlusGroup.setObjects(*((_A,_R),(_A,_S),(_A,_I),(_A,_J),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:smonHc100mbPlusGroup.setStatus(_B)
hcVlanTo100mbGroup=ObjectGroup((1,3,6,1,2,1,16,20,4,6))
hcVlanTo100mbGroup.setObjects(*((_A,_I),(_A,_J)))
if mibBuilder.loadTexts:hcVlanTo100mbGroup.setStatus(_B)
hcVlan100mbPlusGroup=ObjectGroup((1,3,6,1,2,1,16,20,4,7))
hcVlan100mbPlusGroup.setObjects(*((_A,_R),(_A,_S),(_A,_I),(_A,_J),(_A,_T),(_A,_U)))
if mibBuilder.loadTexts:hcVlan100mbPlusGroup.setStatus(_B)
hcPrioTo100mbGroup=ObjectGroup((1,3,6,1,2,1,16,20,4,8))
hcPrioTo100mbGroup.setObjects(*((_A,_K),(_A,_L)))
if mibBuilder.loadTexts:hcPrioTo100mbGroup.setStatus(_B)
hcPrio100mbPlusGroup=ObjectGroup((1,3,6,1,2,1,16,20,4,9))
hcPrio100mbPlusGroup.setObjects(*((_A,_V),(_A,_W),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:hcPrio100mbPlusGroup.setStatus(_B)
smonVlanStatsExtGroup=ObjectGroup((1,3,6,1,2,1,16,20,4,10))
smonVlanStatsExtGroup.setObjects(*((_A,_w),(_A,_x),(_A,_y)))
if mibBuilder.loadTexts:smonVlanStatsExtGroup.setStatus(_B)
smonInformationGroup=ObjectGroup((1,3,6,1,2,1,16,20,4,11))
smonInformationGroup.setObjects((_A,_z))
if mibBuilder.loadTexts:smonInformationGroup.setStatus(_B)
portCopyConfigGroup=ObjectGroup((1,3,6,1,2,1,16,20,4,12))
portCopyConfigGroup.setObjects(*((_A,_A0),(_A,_A1),(_A,_A2)))
if mibBuilder.loadTexts:portCopyConfigGroup.setStatus(_B)
smonMIBCompliance=ModuleCompliance((1,3,6,1,2,1,16,20,3,1))
smonMIBCompliance.setObjects(*((_A,_M),(_A,_X),(_A,_Y),(_A,_Z),(_A,_N),(_A,_A3),(_A,_A4)))
if mibBuilder.loadTexts:smonMIBCompliance.setStatus(_B)
smonMIBVlanStatsCompliance=ModuleCompliance((1,3,6,1,2,1,16,20,3,2))
smonMIBVlanStatsCompliance.setObjects(*((_A,_M),(_A,_X),(_A,_N),(_A,_A5),(_A,_A6)))
if mibBuilder.loadTexts:smonMIBVlanStatsCompliance.setStatus(_B)
smonMIBPrioStatsCompliance=ModuleCompliance((1,3,6,1,2,1,16,20,3,3))
smonMIBPrioStatsCompliance.setObjects(*((_A,_M),(_A,_Y),(_A,_N),(_A,_A7),(_A,_A8)))
if mibBuilder.loadTexts:smonMIBPrioStatsCompliance.setStatus(_B)
portCopyCompliance=ModuleCompliance((1,3,6,1,2,1,16,20,3,4))
portCopyCompliance.setObjects(*((_A,_M),(_A,_Z),(_A,_N)))
if mibBuilder.loadTexts:portCopyCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'SmonDataSource':SmonDataSource,_z:smonCapabilities,'smonMIBCompliances':smonMIBCompliances,'smonMIBCompliance':smonMIBCompliance,'smonMIBVlanStatsCompliance':smonMIBVlanStatsCompliance,'smonMIBPrioStatsCompliance':smonMIBPrioStatsCompliance,'portCopyCompliance':portCopyCompliance,'smonMIBGroups':smonMIBGroups,_M:dataSourceCapsGroup,_X:smonVlanStatsGroup,_Y:smonPrioStatsGroup,_A3:smonHcTo100mbGroup,_A4:smonHc100mbPlusGroup,_A5:hcVlanTo100mbGroup,_A6:hcVlan100mbPlusGroup,_A7:hcPrioTo100mbGroup,_A8:hcPrio100mbPlusGroup,'smonVlanStatsExtGroup':smonVlanStatsExtGroup,_N:smonInformationGroup,_Z:portCopyConfigGroup,'switchRMON':switchRMON,'smonMIBObjects':smonMIBObjects,'dataSourceCaps':dataSourceCaps,'dataSourceCapsTable':dataSourceCapsTable,'dataSourceCapsEntry':dataSourceCapsEntry,_a:dataSourceCapsObject,_f:dataSourceRmonCaps,_g:dataSourceCopyCaps,_h:dataSourceCapsIfIndex,'smonStats':smonStats,'smonVlanStatsControlTable':smonVlanStatsControlTable,'smonVlanStatsControlEntry':smonVlanStatsControlEntry,_P:smonVlanStatsControlIndex,_i:smonVlanStatsControlDataSource,_j:smonVlanStatsControlCreateTime,_k:smonVlanStatsControlOwner,_l:smonVlanStatsControlStatus,'smonVlanIdStatsTable':smonVlanIdStatsTable,'smonVlanIdStatsEntry':smonVlanIdStatsEntry,_b:smonVlanIdStatsId,_m:smonVlanIdStatsTotalPkts,_R:smonVlanIdStatsTotalOverflowPkts,_S:smonVlanIdStatsTotalHCPkts,_n:smonVlanIdStatsTotalOctets,_I:smonVlanIdStatsTotalOverflowOctets,_J:smonVlanIdStatsTotalHCOctets,_o:smonVlanIdStatsNUcastPkts,_T:smonVlanIdStatsNUcastOverflowPkts,_U:smonVlanIdStatsNUcastHCPkts,_w:smonVlanIdStatsNUcastOctets,_x:smonVlanIdStatsNUcastOverflowOctets,_y:smonVlanIdStatsNUcastHCOctets,_p:smonVlanIdStatsCreateTime,'smonPrioStatsControlTable':smonPrioStatsControlTable,'smonPrioStatsControlEntry':smonPrioStatsControlEntry,_Q:smonPrioStatsControlIndex,_q:smonPrioStatsControlDataSource,_r:smonPrioStatsControlCreateTime,_s:smonPrioStatsControlOwner,_t:smonPrioStatsControlStatus,'smonPrioStatsTable':smonPrioStatsTable,'smonPrioStatsEntry':smonPrioStatsEntry,_c:smonPrioStatsId,_u:smonPrioStatsPkts,_V:smonPrioStatsOverflowPkts,_W:smonPrioStatsHCPkts,_v:smonPrioStatsOctets,_K:smonPrioStatsOverflowOctets,_L:smonPrioStatsHCOctets,'portCopyConfig':portCopyConfig,'portCopyTable':portCopyTable,'portCopyEntry':portCopyEntry,_d:portCopySource,_e:portCopyDest,_A0:portCopyDestDropEvents,_A1:portCopyDirection,_A2:portCopyStatus,'smonRegistrationPoints':smonRegistrationPoints,'smonVlanDataSource':smonVlanDataSource})