_G='rcRstpPortStatsEntry'
_F='rcRstpPortConfigEntry'
_E='TruthValue'
_D='SWITCH-RSTP-MIB'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dStpPortEntry,=mibBuilder.importSymbols('BRIDGE-MIB','dot1dStpPortEntry')
iscomSwitch,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','iscomSwitch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_E)
rcRstp=ModuleIdentity((1,3,6,1,4,1,8886,6,1,9))
if mibBuilder.loadTexts:rcRstp.setRevisions(('1991-03-31 00:00',))
_RcRstpConfig_ObjectIdentity=ObjectIdentity
rcRstpConfig=_RcRstpConfig_ObjectIdentity((1,3,6,1,4,1,8886,6,1,9,1))
class _RcRstpEnable_Type(TruthValue):defaultValue=1
_RcRstpEnable_Type.__name__=_E
_RcRstpEnable_Object=MibScalar
rcRstpEnable=_RcRstpEnable_Object((1,3,6,1,4,1,8886,6,1,9,1,1),_RcRstpEnable_Type())
rcRstpEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rcRstpEnable.setStatus(_A)
_RcRstpPortConfigTable_Object=MibTable
rcRstpPortConfigTable=_RcRstpPortConfigTable_Object((1,3,6,1,4,1,8886,6,1,9,1,2))
if mibBuilder.loadTexts:rcRstpPortConfigTable.setStatus(_A)
_RcRstpPortConfigEntry_Object=MibTableRow
rcRstpPortConfigEntry=_RcRstpPortConfigEntry_Object((1,3,6,1,4,1,8886,6,1,9,1,2,1))
if mibBuilder.loadTexts:rcRstpPortConfigEntry.setStatus(_A)
_RcRstpPortRstpEnable_Type=TruthValue
_RcRstpPortRstpEnable_Object=MibTableColumn
rcRstpPortRstpEnable=_RcRstpPortRstpEnable_Object((1,3,6,1,4,1,8886,6,1,9,1,2,1,1),_RcRstpPortRstpEnable_Type())
rcRstpPortRstpEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rcRstpPortRstpEnable.setStatus(_A)
_RcRstpPortOperEnable_Type=TruthValue
_RcRstpPortOperEnable_Object=MibTableColumn
rcRstpPortOperEnable=_RcRstpPortOperEnable_Object((1,3,6,1,4,1,8886,6,1,9,1,2,1,2),_RcRstpPortOperEnable_Type())
rcRstpPortOperEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:rcRstpPortOperEnable.setStatus(_A)
_RcRstpStatistics_ObjectIdentity=ObjectIdentity
rcRstpStatistics=_RcRstpStatistics_ObjectIdentity((1,3,6,1,4,1,8886,6,1,9,2))
_RcRstpPortStatsTable_Object=MibTable
rcRstpPortStatsTable=_RcRstpPortStatsTable_Object((1,3,6,1,4,1,8886,6,1,9,2,1))
if mibBuilder.loadTexts:rcRstpPortStatsTable.setStatus(_A)
_RcRstpPortStatsEntry_Object=MibTableRow
rcRstpPortStatsEntry=_RcRstpPortStatsEntry_Object((1,3,6,1,4,1,8886,6,1,9,2,1,1))
if mibBuilder.loadTexts:rcRstpPortStatsEntry.setStatus(_A)
_RcRstpPortRxStpBPDUs_Type=Counter32
_RcRstpPortRxStpBPDUs_Object=MibTableColumn
rcRstpPortRxStpBPDUs=_RcRstpPortRxStpBPDUs_Object((1,3,6,1,4,1,8886,6,1,9,2,1,1,1),_RcRstpPortRxStpBPDUs_Type())
rcRstpPortRxStpBPDUs.setMaxAccess(_B)
if mibBuilder.loadTexts:rcRstpPortRxStpBPDUs.setStatus(_A)
_RcRstpPortRxTCNs_Type=Counter32
_RcRstpPortRxTCNs_Object=MibTableColumn
rcRstpPortRxTCNs=_RcRstpPortRxTCNs_Object((1,3,6,1,4,1,8886,6,1,9,2,1,1,2),_RcRstpPortRxTCNs_Type())
rcRstpPortRxTCNs.setMaxAccess(_B)
if mibBuilder.loadTexts:rcRstpPortRxTCNs.setStatus(_A)
_RcRstpPortRxRstpBPDUs_Type=Counter32
_RcRstpPortRxRstpBPDUs_Object=MibTableColumn
rcRstpPortRxRstpBPDUs=_RcRstpPortRxRstpBPDUs_Object((1,3,6,1,4,1,8886,6,1,9,2,1,1,3),_RcRstpPortRxRstpBPDUs_Type())
rcRstpPortRxRstpBPDUs.setMaxAccess(_B)
if mibBuilder.loadTexts:rcRstpPortRxRstpBPDUs.setStatus(_A)
_RcRstpPortTxStpBPDUs_Type=Counter32
_RcRstpPortTxStpBPDUs_Object=MibTableColumn
rcRstpPortTxStpBPDUs=_RcRstpPortTxStpBPDUs_Object((1,3,6,1,4,1,8886,6,1,9,2,1,1,4),_RcRstpPortTxStpBPDUs_Type())
rcRstpPortTxStpBPDUs.setMaxAccess(_B)
if mibBuilder.loadTexts:rcRstpPortTxStpBPDUs.setStatus(_A)
_RcRstpPortTxTCNs_Type=Counter32
_RcRstpPortTxTCNs_Object=MibTableColumn
rcRstpPortTxTCNs=_RcRstpPortTxTCNs_Object((1,3,6,1,4,1,8886,6,1,9,2,1,1,5),_RcRstpPortTxTCNs_Type())
rcRstpPortTxTCNs.setMaxAccess(_B)
if mibBuilder.loadTexts:rcRstpPortTxTCNs.setStatus(_A)
_RcRstpPortTxRstpBPDUs_Type=Counter32
_RcRstpPortTxRstpBPDUs_Object=MibTableColumn
rcRstpPortTxRstpBPDUs=_RcRstpPortTxRstpBPDUs_Object((1,3,6,1,4,1,8886,6,1,9,2,1,1,6),_RcRstpPortTxRstpBPDUs_Type())
rcRstpPortTxRstpBPDUs.setMaxAccess(_B)
if mibBuilder.loadTexts:rcRstpPortTxRstpBPDUs.setStatus(_A)
_RcRstpPortStatisticsClear_Type=TruthValue
_RcRstpPortStatisticsClear_Object=MibTableColumn
rcRstpPortStatisticsClear=_RcRstpPortStatisticsClear_Object((1,3,6,1,4,1,8886,6,1,9,2,1,1,7),_RcRstpPortStatisticsClear_Type())
rcRstpPortStatisticsClear.setMaxAccess(_C)
if mibBuilder.loadTexts:rcRstpPortStatisticsClear.setStatus(_A)
dot1dStpPortEntry.registerAugmentions((_D,_F))
rcRstpPortConfigEntry.setIndexNames(*dot1dStpPortEntry.getIndexNames())
dot1dStpPortEntry.registerAugmentions((_D,_G))
rcRstpPortStatsEntry.setIndexNames(*dot1dStpPortEntry.getIndexNames())
mibBuilder.exportSymbols(_D,**{'rcRstp':rcRstp,'rcRstpConfig':rcRstpConfig,'rcRstpEnable':rcRstpEnable,'rcRstpPortConfigTable':rcRstpPortConfigTable,_F:rcRstpPortConfigEntry,'rcRstpPortRstpEnable':rcRstpPortRstpEnable,'rcRstpPortOperEnable':rcRstpPortOperEnable,'rcRstpStatistics':rcRstpStatistics,'rcRstpPortStatsTable':rcRstpPortStatsTable,_G:rcRstpPortStatsEntry,'rcRstpPortRxStpBPDUs':rcRstpPortRxStpBPDUs,'rcRstpPortRxTCNs':rcRstpPortRxTCNs,'rcRstpPortRxRstpBPDUs':rcRstpPortRxRstpBPDUs,'rcRstpPortTxStpBPDUs':rcRstpPortTxStpBPDUs,'rcRstpPortTxTCNs':rcRstpPortTxTCNs,'rcRstpPortTxRstpBPDUs':rcRstpPortTxRstpBPDUs,'rcRstpPortStatisticsClear':rcRstpPortStatisticsClear})