_v='cpAtmIfHCIngressStatMIBGroup'
_u='cpAtmIfHCEgressIntervalMIBGroup'
_t='cpAtmIfHCEgressStatMIBGroup'
_s='cpAtmIfIngressStatMIBGroup'
_r='cpAtmIfEgressIntervalMIBGroup'
_q='cpAtmIfEgressStatMIBGroup'
_p='cpAtmIfConfigGroup'
_o='cpAtmIfHCIngXmtOAMCells'
_n='cpAtmIfHCIngXmtEFCICells'
_m='cpAtmIfHCIngXmtClp1Cells'
_l='cpAtmIfHCIngXmtClp0Cells'
_k='cpAtmIfHCIntEgrRcvEFCICells'
_j='cpAtmIfHCIntEgrRcvOAMCells'
_i='cpAtmIfHCIntEgrClp1DiscCells'
_h='cpAtmIfHCIntEgrClp0DiscCells'
_g='cpAtmIfHCIntEgrRcvClp1Cells'
_f='cpAtmIfHCIntEgrRcvClp0Cells'
_e='cpAtmIfHCEgrRcvEFCICells'
_d='cpAtmIfHCEgrRcvOAMCells'
_c='cpAtmIfHCEgrClp1DiscCells'
_b='cpAtmIfHCEgrClp0DiscCells'
_a='cpAtmIfHCEgrRcvClp1Cells'
_Z='cpAtmIfHCEgrRcvClp0Cells'
_Y='cpAtmIfIngXmtOAMCells'
_X='cpAtmIfIngXmtEFCICells'
_W='cpAtmIfIngXmtClp1Cells'
_V='cpAtmIfIngXmtClp0Cells'
_U='cpAtmIfIntEgrRcvEFCICells'
_T='cpAtmIfIntEgrRcvOAMCells'
_S='cpAtmIfIntEgrClp1DiscCells'
_R='cpAtmIfIntEgrClp0DiscCells'
_Q='cpAtmIfIntEgrRcvClp1Cells'
_P='cpAtmIfIntEgrRcvClp0Cells'
_O='cpAtmIfEgrRcvEFCICells'
_N='cpAtmIfEgrRcvOAMCells'
_M='cpAtmIfEgrClp1DiscCells'
_L='cpAtmIfEgrClp0DiscCells'
_K='cpAtmIfEgrRcvClp1Cells'
_J='cpAtmIfEgrRcvClp0Cells'
_I='cpAtmIfMaxBandwidth'
_H='cpAtmIfEgressIntervalNumber'
_G='Unsigned32'
_F='Integer32'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='CISCO-PROP-ATM-IF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoPropAtmIfMIB=ModuleIdentity((1,3,6,1,4,1,9,9,319))
if mibBuilder.loadTexts:ciscoPropAtmIfMIB.setRevisions(('2002-12-04 00:00',))
_CiscoPropAtmIfMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoPropAtmIfMIBNotifs=_CiscoPropAtmIfMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,319,0))
_CiscoPropAtmIfMIBObjects_ObjectIdentity=ObjectIdentity
ciscoPropAtmIfMIBObjects=_CiscoPropAtmIfMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,319,1))
_CpAtmIfConfig_ObjectIdentity=ObjectIdentity
cpAtmIfConfig=_CpAtmIfConfig_ObjectIdentity((1,3,6,1,4,1,9,9,319,1,1))
_CpAtmIfConfigTable_Object=MibTable
cpAtmIfConfigTable=_CpAtmIfConfigTable_Object((1,3,6,1,4,1,9,9,319,1,1,1))
if mibBuilder.loadTexts:cpAtmIfConfigTable.setStatus(_A)
_CpAtmIfConfigEntry_Object=MibTableRow
cpAtmIfConfigEntry=_CpAtmIfConfigEntry_Object((1,3,6,1,4,1,9,9,319,1,1,1,1))
cpAtmIfConfigEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cpAtmIfConfigEntry.setStatus(_A)
class _CpAtmIfMaxBandwidth_Type(Unsigned32):defaultValue=7000000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CpAtmIfMaxBandwidth_Type.__name__=_G
_CpAtmIfMaxBandwidth_Object=MibTableColumn
cpAtmIfMaxBandwidth=_CpAtmIfMaxBandwidth_Object((1,3,6,1,4,1,9,9,319,1,1,1,1,1),_CpAtmIfMaxBandwidth_Type())
cpAtmIfMaxBandwidth.setMaxAccess('read-write')
if mibBuilder.loadTexts:cpAtmIfMaxBandwidth.setStatus(_A)
if mibBuilder.loadTexts:cpAtmIfMaxBandwidth.setUnits('cells-per-second')
_CpAtmIfVirtualPortStats_ObjectIdentity=ObjectIdentity
cpAtmIfVirtualPortStats=_CpAtmIfVirtualPortStats_ObjectIdentity((1,3,6,1,4,1,9,9,319,1,2))
_CpAtmIfStatsEgressTable_Object=MibTable
cpAtmIfStatsEgressTable=_CpAtmIfStatsEgressTable_Object((1,3,6,1,4,1,9,9,319,1,2,1))
if mibBuilder.loadTexts:cpAtmIfStatsEgressTable.setStatus(_A)
_CpAtmIfStatsEgressEntry_Object=MibTableRow
cpAtmIfStatsEgressEntry=_CpAtmIfStatsEgressEntry_Object((1,3,6,1,4,1,9,9,319,1,2,1,1))
cpAtmIfStatsEgressEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cpAtmIfStatsEgressEntry.setStatus(_A)
_CpAtmIfEgrRcvClp0Cells_Type=Counter32
_CpAtmIfEgrRcvClp0Cells_Object=MibTableColumn
cpAtmIfEgrRcvClp0Cells=_CpAtmIfEgrRcvClp0Cells_Object((1,3,6,1,4,1,9,9,319,1,2,1,1,1),_CpAtmIfEgrRcvClp0Cells_Type())
cpAtmIfEgrRcvClp0Cells.setMaxAccess(_C)
if mibBuilder.loadTexts:cpAtmIfEgrRcvClp0Cells.setStatus(_A)
_CpAtmIfEgrRcvClp1Cells_Type=Counter32
_CpAtmIfEgrRcvClp1Cells_Object=MibTableColumn
cpAtmIfEgrRcvClp1Cells=_CpAtmIfEgrRcvClp1Cells_Object((1,3,6,1,4,1,9,9,319,1,2,1,1,2),_CpAtmIfEgrRcvClp1Cells_Type())
cpAtmIfEgrRcvClp1Cells.setMaxAccess(_C)
if mibBuilder.loadTexts:cpAtmIfEgrRcvClp1Cells.setStatus(_A)
_CpAtmIfEgrClp0DiscCells_Type=Counter32
_CpAtmIfEgrClp0DiscCells_Object=MibTableColumn
cpAtmIfEgrClp0DiscCells=_CpAtmIfEgrClp0DiscCells_Object((1,3,6,1,4,1,9,9,319,1,2,1,1,3),_CpAtmIfEgrClp0DiscCells_Type())
cpAtmIfEgrClp0DiscCells.setMaxAccess(_C)
if mibBuilder.loadTexts:cpAtmIfEgrClp0DiscCells.setStatus(_A)
_CpAtmIfEgrClp1DiscCells_Type=Counter32
_CpAtmIfEgrClp1DiscCells_Object=MibTableColumn
cpAtmIfEgrClp1DiscCells=_CpAtmIfEgrClp1DiscCells_Object((1,3,6,1,4,1,9,9,319,1,2,1,1,4),_CpAtmIfEgrClp1DiscCells_Type())
cpAtmIfEgrClp1DiscCells.setMaxAccess(_C)
if mibBuilder.loadTexts:cpAtmIfEgrClp1DiscCells.setStatus(_A)
_CpAtmIfEgrRcvOAMCells_Type=Counter32
_CpAtmIfEgrRcvOAMCells_Object=MibTableColumn
cpAtmIfEgrRcvOAMCells=_CpAtmIfEgrRcvOAMCells_Object((1,3,6,1,4,1,9,9,319,1,2,1,1,5),_CpAtmIfEgrRcvOAMCells_Type())
cpAtmIfEgrRcvOAMCells.setMaxAccess(_C)
if mibBuilder.loadTexts:cpAtmIfEgrRcvOAMCells.setStatus(_A)
_CpAtmIfEgrRcvEFCICells_Type=Counter32
_CpAtmIfEgrRcvEFCICells_Object=MibTableColumn
cpAtmIfEgrRcvEFCICells=_CpAtmIfEgrRcvEFCICells_Object((1,3,6,1,4,1,9,9,319,1,2,1,1,6),_CpAtmIfEgrRcvEFCICells_Type())
cpAtmIfEgrRcvEFCICells.setMaxAccess(_C)
if mibBuilder.loadTexts:cpAtmIfEgrRcvEFCICells.setStatus(_A)
_CpAtmIfHCEgrRcvClp0Cells_Type=Counter64
_CpAtmIfHCEgrRcvClp0Cells_Object=MibTableColumn
cpAtmIfHCEgrRcvClp0Cells=_CpAtmIfHCEgrRcvClp0Cells_Object((1,3,6,1,4,1,9,9,319,1,2,1,1,7),_CpAtmIfHCEgrRcvClp0Cells_Type())
cpAtmIfHCEgrRcvClp0Cells.setMaxAccess(_C)
if mibBuilder.loadTexts:cpAtmIfHCEgrRcvClp0Cells.setStatus(_A)
_CpAtmIfHCEgrRcvClp1Cells_Type=Counter64
_CpAtmIfHCEgrRcvClp1Cells_Object=MibTableColumn
cpAtmIfHCEgrRcvClp1Cells=_CpAtmIfHCEgrRcvClp1Cells_Object((1,3,6,1,4,1,9,9,319,1,2,1,1,8),_CpAtmIfHCEgrRcvClp1Cells_Type())
cpAtmIfHCEgrRcvClp1Cells.setMaxAccess(_C)
if mibBuilder.loadTexts:cpAtmIfHCEgrRcvClp1Cells.setStatus(_A)
_CpAtmIfHCEgrClp0DiscCells_Type=Counter64
_CpAtmIfHCEgrClp0DiscCells_Object=MibTableColumn
cpAtmIfHCEgrClp0DiscCells=_CpAtmIfHCEgrClp0DiscCells_Object((1,3,6,1,4,1,9,9,319,1,2,1,1,9),_CpAtmIfHCEgrClp0DiscCells_Type())
cpAtmIfHCEgrClp0DiscCells.setMaxAccess(_C)
if mibBuilder.loadTexts:cpAtmIfHCEgrClp0DiscCells.setStatus(_A)
_CpAtmIfHCEgrClp1DiscCells_Type=Counter64
_CpAtmIfHCEgrClp1DiscCells_Object=MibTableColumn
cpAtmIfHCEgrClp1DiscCells=_CpAtmIfHCEgrClp1DiscCells_Object((1,3,6,1,4,1,9,9,319,1,2,1,1,10),_CpAtmIfHCEgrClp1DiscCells_Type())
cpAtmIfHCEgrClp1DiscCells.setMaxAccess(_C)
if mibBuilder.loadTexts:cpAtmIfHCEgrClp1DiscCells.setStatus(_A)
_CpAtmIfHCEgrRcvOAMCells_Type=Counter64
_CpAtmIfHCEgrRcvOAMCells_Object=MibTableColumn
cpAtmIfHCEgrRcvOAMCells=_CpAtmIfHCEgrRcvOAMCells_Object((1,3,6,1,4,1,9,9,319,1,2,1,1,11),_CpAtmIfHCEgrRcvOAMCells_Type())
cpAtmIfHCEgrRcvOAMCells.setMaxAccess(_C)
if mibBuilder.loadTexts:cpAtmIfHCEgrRcvOAMCells.setStatus(_A)
_CpAtmIfHCEgrRcvEFCICells_Type=Counter64
_CpAtmIfHCEgrRcvEFCICells_Object=MibTableColumn
cpAtmIfHCEgrRcvEFCICells=_CpAtmIfHCEgrRcvEFCICells_Object((1,3,6,1,4,1,9,9,319,1,2,1,1,12),_CpAtmIfHCEgrRcvEFCICells_Type())
cpAtmIfHCEgrRcvEFCICells.setMaxAccess(_C)
if mibBuilder.loadTexts:cpAtmIfHCEgrRcvEFCICells.setStatus(_A)
_CpAtmIfEgressIntervalTable_Object=MibTable
cpAtmIfEgressIntervalTable=_CpAtmIfEgressIntervalTable_Object((1,3,6,1,4,1,9,9,319,1,2,2))
if mibBuilder.loadTexts:cpAtmIfEgressIntervalTable.setStatus(_A)
_CpAtmIfEgressIntervalEntry_Object=MibTableRow
cpAtmIfEgressIntervalEntry=_CpAtmIfEgressIntervalEntry_Object((1,3,6,1,4,1,9,9,319,1,2,2,1))
cpAtmIfEgressIntervalEntry.setIndexNames((0,_D,_E),(0,_B,_H))
if mibBuilder.loadTexts:cpAtmIfEgressIntervalEntry.setStatus(_A)
class _CpAtmIfEgressIntervalNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_CpAtmIfEgressIntervalNumber_Type.__name__=_F
_CpAtmIfEgressIntervalNumber_Object=MibTableColumn
cpAtmIfEgressIntervalNumber=_CpAtmIfEgressIntervalNumber_Object((1,3,6,1,4,1,9,9,319,1,2,2,1,1),_CpAtmIfEgressIntervalNumber_Type())
cpAtmIfEgressIntervalNumber.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cpAtmIfEgressIntervalNumber.setStatus(_A)
_CpAtmIfIntEgrRcvClp0Cells_Type=Counter32
_CpAtmIfIntEgrRcvClp0Cells_Object=MibTableColumn
cpAtmIfIntEgrRcvClp0Cells=_CpAtmIfIntEgrRcvClp0Cells_Object((1,3,6,1,4,1,9,9,319,1,2,2,1,2),_CpAtmIfIntEgrRcvClp0Cells_Type())
cpAtmIfIntEgrRcvClp0Cells.setMaxAccess(_C)
if mibBuilder.loadTexts:cpAtmIfIntEgrRcvClp0Cells.setStatus(_A)
_CpAtmIfIntEgrRcvClp1Cells_Type=Counter32
_CpAtmIfIntEgrRcvClp1Cells_Object=MibTableColumn
cpAtmIfIntEgrRcvClp1Cells=_CpAtmIfIntEgrRcvClp1Cells_Object((1,3,6,1,4,1,9,9,319,1,2,2,1,3),_CpAtmIfIntEgrRcvClp1Cells_Type())
cpAtmIfIntEgrRcvClp1Cells.setMaxAccess(_C)
if mibBuilder.loadTexts:cpAtmIfIntEgrRcvClp1Cells.setStatus(_A)
_CpAtmIfIntEgrClp0DiscCells_Type=Counter32
_CpAtmIfIntEgrClp0DiscCells_Object=MibTableColumn
cpAtmIfIntEgrClp0DiscCells=_CpAtmIfIntEgrClp0DiscCells_Object((1,3,6,1,4,1,9,9,319,1,2,2,1,4),_CpAtmIfIntEgrClp0DiscCells_Type())
cpAtmIfIntEgrClp0DiscCells.setMaxAccess(_C)
if mibBuilder.loadTexts:cpAtmIfIntEgrClp0DiscCells.setStatus(_A)
_CpAtmIfIntEgrClp1DiscCells_Type=Counter32
_CpAtmIfIntEgrClp1DiscCells_Object=MibTableColumn
cpAtmIfIntEgrClp1DiscCells=_CpAtmIfIntEgrClp1DiscCells_Object((1,3,6,1,4,1,9,9,319,1,2,2,1,5),_CpAtmIfIntEgrClp1DiscCells_Type())
cpAtmIfIntEgrClp1DiscCells.setMaxAccess(_C)
if mibBuilder.loadTexts:cpAtmIfIntEgrClp1DiscCells.setStatus(_A)
_CpAtmIfIntEgrRcvOAMCells_Type=Counter32
_CpAtmIfIntEgrRcvOAMCells_Object=MibTableColumn
cpAtmIfIntEgrRcvOAMCells=_CpAtmIfIntEgrRcvOAMCells_Object((1,3,6,1,4,1,9,9,319,1,2,2,1,6),_CpAtmIfIntEgrRcvOAMCells_Type())
cpAtmIfIntEgrRcvOAMCells.setMaxAccess(_C)
if mibBuilder.loadTexts:cpAtmIfIntEgrRcvOAMCells.setStatus(_A)
_CpAtmIfIntEgrRcvEFCICells_Type=Counter32
_CpAtmIfIntEgrRcvEFCICells_Object=MibTableColumn
cpAtmIfIntEgrRcvEFCICells=_CpAtmIfIntEgrRcvEFCICells_Object((1,3,6,1,4,1,9,9,319,1,2,2,1,7),_CpAtmIfIntEgrRcvEFCICells_Type())
cpAtmIfIntEgrRcvEFCICells.setMaxAccess(_C)
if mibBuilder.loadTexts:cpAtmIfIntEgrRcvEFCICells.setStatus(_A)
_CpAtmIfHCIntEgrRcvClp0Cells_Type=Counter64
_CpAtmIfHCIntEgrRcvClp0Cells_Object=MibTableColumn
cpAtmIfHCIntEgrRcvClp0Cells=_CpAtmIfHCIntEgrRcvClp0Cells_Object((1,3,6,1,4,1,9,9,319,1,2,2,1,8),_CpAtmIfHCIntEgrRcvClp0Cells_Type())
cpAtmIfHCIntEgrRcvClp0Cells.setMaxAccess(_C)
if mibBuilder.loadTexts:cpAtmIfHCIntEgrRcvClp0Cells.setStatus(_A)
_CpAtmIfHCIntEgrRcvClp1Cells_Type=Counter64
_CpAtmIfHCIntEgrRcvClp1Cells_Object=MibTableColumn
cpAtmIfHCIntEgrRcvClp1Cells=_CpAtmIfHCIntEgrRcvClp1Cells_Object((1,3,6,1,4,1,9,9,319,1,2,2,1,9),_CpAtmIfHCIntEgrRcvClp1Cells_Type())
cpAtmIfHCIntEgrRcvClp1Cells.setMaxAccess(_C)
if mibBuilder.loadTexts:cpAtmIfHCIntEgrRcvClp1Cells.setStatus(_A)
_CpAtmIfHCIntEgrClp0DiscCells_Type=Counter64
_CpAtmIfHCIntEgrClp0DiscCells_Object=MibTableColumn
cpAtmIfHCIntEgrClp0DiscCells=_CpAtmIfHCIntEgrClp0DiscCells_Object((1,3,6,1,4,1,9,9,319,1,2,2,1,10),_CpAtmIfHCIntEgrClp0DiscCells_Type())
cpAtmIfHCIntEgrClp0DiscCells.setMaxAccess(_C)
if mibBuilder.loadTexts:cpAtmIfHCIntEgrClp0DiscCells.setStatus(_A)
_CpAtmIfHCIntEgrClp1DiscCells_Type=Counter64
_CpAtmIfHCIntEgrClp1DiscCells_Object=MibTableColumn
cpAtmIfHCIntEgrClp1DiscCells=_CpAtmIfHCIntEgrClp1DiscCells_Object((1,3,6,1,4,1,9,9,319,1,2,2,1,11),_CpAtmIfHCIntEgrClp1DiscCells_Type())
cpAtmIfHCIntEgrClp1DiscCells.setMaxAccess(_C)
if mibBuilder.loadTexts:cpAtmIfHCIntEgrClp1DiscCells.setStatus(_A)
_CpAtmIfHCIntEgrRcvOAMCells_Type=Counter64
_CpAtmIfHCIntEgrRcvOAMCells_Object=MibTableColumn
cpAtmIfHCIntEgrRcvOAMCells=_CpAtmIfHCIntEgrRcvOAMCells_Object((1,3,6,1,4,1,9,9,319,1,2,2,1,12),_CpAtmIfHCIntEgrRcvOAMCells_Type())
cpAtmIfHCIntEgrRcvOAMCells.setMaxAccess(_C)
if mibBuilder.loadTexts:cpAtmIfHCIntEgrRcvOAMCells.setStatus(_A)
_CpAtmIfHCIntEgrRcvEFCICells_Type=Counter64
_CpAtmIfHCIntEgrRcvEFCICells_Object=MibTableColumn
cpAtmIfHCIntEgrRcvEFCICells=_CpAtmIfHCIntEgrRcvEFCICells_Object((1,3,6,1,4,1,9,9,319,1,2,2,1,13),_CpAtmIfHCIntEgrRcvEFCICells_Type())
cpAtmIfHCIntEgrRcvEFCICells.setMaxAccess(_C)
if mibBuilder.loadTexts:cpAtmIfHCIntEgrRcvEFCICells.setStatus(_A)
_CpAtmIfStatsIngressTable_Object=MibTable
cpAtmIfStatsIngressTable=_CpAtmIfStatsIngressTable_Object((1,3,6,1,4,1,9,9,319,1,2,3))
if mibBuilder.loadTexts:cpAtmIfStatsIngressTable.setStatus(_A)
_CpAtmIfStatsIngressEntry_Object=MibTableRow
cpAtmIfStatsIngressEntry=_CpAtmIfStatsIngressEntry_Object((1,3,6,1,4,1,9,9,319,1,2,3,1))
cpAtmIfStatsIngressEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cpAtmIfStatsIngressEntry.setStatus(_A)
_CpAtmIfIngXmtClp0Cells_Type=Counter32
_CpAtmIfIngXmtClp0Cells_Object=MibTableColumn
cpAtmIfIngXmtClp0Cells=_CpAtmIfIngXmtClp0Cells_Object((1,3,6,1,4,1,9,9,319,1,2,3,1,1),_CpAtmIfIngXmtClp0Cells_Type())
cpAtmIfIngXmtClp0Cells.setMaxAccess(_C)
if mibBuilder.loadTexts:cpAtmIfIngXmtClp0Cells.setStatus(_A)
_CpAtmIfIngXmtClp1Cells_Type=Counter32
_CpAtmIfIngXmtClp1Cells_Object=MibTableColumn
cpAtmIfIngXmtClp1Cells=_CpAtmIfIngXmtClp1Cells_Object((1,3,6,1,4,1,9,9,319,1,2,3,1,2),_CpAtmIfIngXmtClp1Cells_Type())
cpAtmIfIngXmtClp1Cells.setMaxAccess(_C)
if mibBuilder.loadTexts:cpAtmIfIngXmtClp1Cells.setStatus(_A)
_CpAtmIfIngXmtEFCICells_Type=Counter32
_CpAtmIfIngXmtEFCICells_Object=MibTableColumn
cpAtmIfIngXmtEFCICells=_CpAtmIfIngXmtEFCICells_Object((1,3,6,1,4,1,9,9,319,1,2,3,1,3),_CpAtmIfIngXmtEFCICells_Type())
cpAtmIfIngXmtEFCICells.setMaxAccess(_C)
if mibBuilder.loadTexts:cpAtmIfIngXmtEFCICells.setStatus(_A)
_CpAtmIfIngXmtOAMCells_Type=Counter32
_CpAtmIfIngXmtOAMCells_Object=MibTableColumn
cpAtmIfIngXmtOAMCells=_CpAtmIfIngXmtOAMCells_Object((1,3,6,1,4,1,9,9,319,1,2,3,1,4),_CpAtmIfIngXmtOAMCells_Type())
cpAtmIfIngXmtOAMCells.setMaxAccess(_C)
if mibBuilder.loadTexts:cpAtmIfIngXmtOAMCells.setStatus(_A)
_CpAtmIfHCIngXmtClp0Cells_Type=Counter64
_CpAtmIfHCIngXmtClp0Cells_Object=MibTableColumn
cpAtmIfHCIngXmtClp0Cells=_CpAtmIfHCIngXmtClp0Cells_Object((1,3,6,1,4,1,9,9,319,1,2,3,1,5),_CpAtmIfHCIngXmtClp0Cells_Type())
cpAtmIfHCIngXmtClp0Cells.setMaxAccess(_C)
if mibBuilder.loadTexts:cpAtmIfHCIngXmtClp0Cells.setStatus(_A)
_CpAtmIfHCIngXmtClp1Cells_Type=Counter64
_CpAtmIfHCIngXmtClp1Cells_Object=MibTableColumn
cpAtmIfHCIngXmtClp1Cells=_CpAtmIfHCIngXmtClp1Cells_Object((1,3,6,1,4,1,9,9,319,1,2,3,1,6),_CpAtmIfHCIngXmtClp1Cells_Type())
cpAtmIfHCIngXmtClp1Cells.setMaxAccess(_C)
if mibBuilder.loadTexts:cpAtmIfHCIngXmtClp1Cells.setStatus(_A)
_CpAtmIfHCIngXmtEFCICells_Type=Counter64
_CpAtmIfHCIngXmtEFCICells_Object=MibTableColumn
cpAtmIfHCIngXmtEFCICells=_CpAtmIfHCIngXmtEFCICells_Object((1,3,6,1,4,1,9,9,319,1,2,3,1,7),_CpAtmIfHCIngXmtEFCICells_Type())
cpAtmIfHCIngXmtEFCICells.setMaxAccess(_C)
if mibBuilder.loadTexts:cpAtmIfHCIngXmtEFCICells.setStatus(_A)
_CpAtmIfHCIngXmtOAMCells_Type=Counter64
_CpAtmIfHCIngXmtOAMCells_Object=MibTableColumn
cpAtmIfHCIngXmtOAMCells=_CpAtmIfHCIngXmtOAMCells_Object((1,3,6,1,4,1,9,9,319,1,2,3,1,8),_CpAtmIfHCIngXmtOAMCells_Type())
cpAtmIfHCIngXmtOAMCells.setMaxAccess(_C)
if mibBuilder.loadTexts:cpAtmIfHCIngXmtOAMCells.setStatus(_A)
_CpAtmIfMIBConformance_ObjectIdentity=ObjectIdentity
cpAtmIfMIBConformance=_CpAtmIfMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,319,2))
_CpAtmIfMIBCompliances_ObjectIdentity=ObjectIdentity
cpAtmIfMIBCompliances=_CpAtmIfMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,319,2,1))
_CpAtmIfMIBGroups_ObjectIdentity=ObjectIdentity
cpAtmIfMIBGroups=_CpAtmIfMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,319,2,2))
cpAtmIfConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,319,2,2,1))
cpAtmIfConfigGroup.setObjects((_B,_I))
if mibBuilder.loadTexts:cpAtmIfConfigGroup.setStatus(_A)
cpAtmIfEgressStatMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,319,2,2,2))
cpAtmIfEgressStatMIBGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:cpAtmIfEgressStatMIBGroup.setStatus(_A)
cpAtmIfEgressIntervalMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,319,2,2,3))
cpAtmIfEgressIntervalMIBGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:cpAtmIfEgressIntervalMIBGroup.setStatus(_A)
cpAtmIfIngressStatMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,319,2,2,4))
cpAtmIfIngressStatMIBGroup.setObjects(*((_B,_V),(_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:cpAtmIfIngressStatMIBGroup.setStatus(_A)
cpAtmIfHCEgressStatMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,319,2,2,5))
cpAtmIfHCEgressStatMIBGroup.setObjects(*((_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:cpAtmIfHCEgressStatMIBGroup.setStatus(_A)
cpAtmIfHCEgressIntervalMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,319,2,2,6))
cpAtmIfHCEgressIntervalMIBGroup.setObjects(*((_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k)))
if mibBuilder.loadTexts:cpAtmIfHCEgressIntervalMIBGroup.setStatus(_A)
cpAtmIfHCIngressStatMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,319,2,2,7))
cpAtmIfHCIngressStatMIBGroup.setObjects(*((_B,_l),(_B,_m),(_B,_n),(_B,_o)))
if mibBuilder.loadTexts:cpAtmIfHCIngressStatMIBGroup.setStatus(_A)
cpAtmIfMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,319,2,1,1))
cpAtmIfMIBCompliance.setObjects(*((_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v)))
if mibBuilder.loadTexts:cpAtmIfMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoPropAtmIfMIB':ciscoPropAtmIfMIB,'ciscoPropAtmIfMIBNotifs':ciscoPropAtmIfMIBNotifs,'ciscoPropAtmIfMIBObjects':ciscoPropAtmIfMIBObjects,'cpAtmIfConfig':cpAtmIfConfig,'cpAtmIfConfigTable':cpAtmIfConfigTable,'cpAtmIfConfigEntry':cpAtmIfConfigEntry,_I:cpAtmIfMaxBandwidth,'cpAtmIfVirtualPortStats':cpAtmIfVirtualPortStats,'cpAtmIfStatsEgressTable':cpAtmIfStatsEgressTable,'cpAtmIfStatsEgressEntry':cpAtmIfStatsEgressEntry,_J:cpAtmIfEgrRcvClp0Cells,_K:cpAtmIfEgrRcvClp1Cells,_L:cpAtmIfEgrClp0DiscCells,_M:cpAtmIfEgrClp1DiscCells,_N:cpAtmIfEgrRcvOAMCells,_O:cpAtmIfEgrRcvEFCICells,_Z:cpAtmIfHCEgrRcvClp0Cells,_a:cpAtmIfHCEgrRcvClp1Cells,_b:cpAtmIfHCEgrClp0DiscCells,_c:cpAtmIfHCEgrClp1DiscCells,_d:cpAtmIfHCEgrRcvOAMCells,_e:cpAtmIfHCEgrRcvEFCICells,'cpAtmIfEgressIntervalTable':cpAtmIfEgressIntervalTable,'cpAtmIfEgressIntervalEntry':cpAtmIfEgressIntervalEntry,_H:cpAtmIfEgressIntervalNumber,_P:cpAtmIfIntEgrRcvClp0Cells,_Q:cpAtmIfIntEgrRcvClp1Cells,_R:cpAtmIfIntEgrClp0DiscCells,_S:cpAtmIfIntEgrClp1DiscCells,_T:cpAtmIfIntEgrRcvOAMCells,_U:cpAtmIfIntEgrRcvEFCICells,_f:cpAtmIfHCIntEgrRcvClp0Cells,_g:cpAtmIfHCIntEgrRcvClp1Cells,_h:cpAtmIfHCIntEgrClp0DiscCells,_i:cpAtmIfHCIntEgrClp1DiscCells,_j:cpAtmIfHCIntEgrRcvOAMCells,_k:cpAtmIfHCIntEgrRcvEFCICells,'cpAtmIfStatsIngressTable':cpAtmIfStatsIngressTable,'cpAtmIfStatsIngressEntry':cpAtmIfStatsIngressEntry,_V:cpAtmIfIngXmtClp0Cells,_W:cpAtmIfIngXmtClp1Cells,_X:cpAtmIfIngXmtEFCICells,_Y:cpAtmIfIngXmtOAMCells,_l:cpAtmIfHCIngXmtClp0Cells,_m:cpAtmIfHCIngXmtClp1Cells,_n:cpAtmIfHCIngXmtEFCICells,_o:cpAtmIfHCIngXmtOAMCells,'cpAtmIfMIBConformance':cpAtmIfMIBConformance,'cpAtmIfMIBCompliances':cpAtmIfMIBCompliances,'cpAtmIfMIBCompliance':cpAtmIfMIBCompliance,'cpAtmIfMIBGroups':cpAtmIfMIBGroups,_p:cpAtmIfConfigGroup,_q:cpAtmIfEgressStatMIBGroup,_r:cpAtmIfEgressIntervalMIBGroup,_s:cpAtmIfIngressStatMIBGroup,_t:cpAtmIfHCEgressStatMIBGroup,_u:cpAtmIfHCEgressIntervalMIBGroup,_v:cpAtmIfHCIngressStatMIBGroup})