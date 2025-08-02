_G='read-write'
_F='rlCpuCountersTarget'
_E='NETGEAR-RADLAN-CPU-COUNTERS-MIB'
_D='Integer32'
_C='TruthValue'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rnd,=mibBuilder.importSymbols('NETGEAR-RADLAN-MIB','rnd')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_C)
rlCpuCounters=ModuleIdentity((1,3,6,1,4,1,4526,17,124))
if mibBuilder.loadTexts:rlCpuCounters.setRevisions(('2007-05-15 00:00',))
_RlCpuCountersTable_Object=MibTable
rlCpuCountersTable=_RlCpuCountersTable_Object((1,3,6,1,4,1,4526,17,124,1))
if mibBuilder.loadTexts:rlCpuCountersTable.setStatus(_A)
_RlCpuCountersEntry_Object=MibTableRow
rlCpuCountersEntry=_RlCpuCountersEntry_Object((1,3,6,1,4,1,4526,17,124,1,1))
rlCpuCountersEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:rlCpuCountersEntry.setStatus(_A)
class _RlCpuCountersTarget_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(0));namedValues=NamedValues(('cpuCounters',0))
_RlCpuCountersTarget_Type.__name__=_D
_RlCpuCountersTarget_Object=MibTableColumn
rlCpuCountersTarget=_RlCpuCountersTarget_Object((1,3,6,1,4,1,4526,17,124,1,1,1),_RlCpuCountersTarget_Type())
rlCpuCountersTarget.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:rlCpuCountersTarget.setStatus(_A)
_RlCpuCountersTxBC_Type=Counter32
_RlCpuCountersTxBC_Object=MibTableColumn
rlCpuCountersTxBC=_RlCpuCountersTxBC_Object((1,3,6,1,4,1,4526,17,124,1,1,2),_RlCpuCountersTxBC_Type())
rlCpuCountersTxBC.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCpuCountersTxBC.setStatus(_A)
_RlCpuCountersTxMC_Type=Counter32
_RlCpuCountersTxMC_Object=MibTableColumn
rlCpuCountersTxMC=_RlCpuCountersTxMC_Object((1,3,6,1,4,1,4526,17,124,1,1,3),_RlCpuCountersTxMC_Type())
rlCpuCountersTxMC.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCpuCountersTxMC.setStatus(_A)
_RlCpuCountersTxUC_Type=Counter32
_RlCpuCountersTxUC_Object=MibTableColumn
rlCpuCountersTxUC=_RlCpuCountersTxUC_Object((1,3,6,1,4,1,4526,17,124,1,1,4),_RlCpuCountersTxUC_Type())
rlCpuCountersTxUC.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCpuCountersTxUC.setStatus(_A)
_RlCpuCountersTxOctets_Type=Counter32
_RlCpuCountersTxOctets_Object=MibTableColumn
rlCpuCountersTxOctets=_RlCpuCountersTxOctets_Object((1,3,6,1,4,1,4526,17,124,1,1,5),_RlCpuCountersTxOctets_Type())
rlCpuCountersTxOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCpuCountersTxOctets.setStatus(_A)
_RlCpuCountersRxBC_Type=Counter32
_RlCpuCountersRxBC_Object=MibTableColumn
rlCpuCountersRxBC=_RlCpuCountersRxBC_Object((1,3,6,1,4,1,4526,17,124,1,1,6),_RlCpuCountersRxBC_Type())
rlCpuCountersRxBC.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCpuCountersRxBC.setStatus(_A)
_RlCpuCountersRxMC_Type=Counter32
_RlCpuCountersRxMC_Object=MibTableColumn
rlCpuCountersRxMC=_RlCpuCountersRxMC_Object((1,3,6,1,4,1,4526,17,124,1,1,7),_RlCpuCountersRxMC_Type())
rlCpuCountersRxMC.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCpuCountersRxMC.setStatus(_A)
_RlCpuCountersRxUC_Type=Counter32
_RlCpuCountersRxUC_Object=MibTableColumn
rlCpuCountersRxUC=_RlCpuCountersRxUC_Object((1,3,6,1,4,1,4526,17,124,1,1,8),_RlCpuCountersRxUC_Type())
rlCpuCountersRxUC.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCpuCountersRxUC.setStatus(_A)
_RlCpuCountersRxOctets_Type=Counter32
_RlCpuCountersRxOctets_Object=MibTableColumn
rlCpuCountersRxOctets=_RlCpuCountersRxOctets_Object((1,3,6,1,4,1,4526,17,124,1,1,9),_RlCpuCountersRxOctets_Type())
rlCpuCountersRxOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:rlCpuCountersRxOctets.setStatus(_A)
class _RlCpuCountersReset_Type(TruthValue):defaultValue=2
_RlCpuCountersReset_Type.__name__=_C
_RlCpuCountersReset_Object=MibScalar
rlCpuCountersReset=_RlCpuCountersReset_Object((1,3,6,1,4,1,4526,17,124,2),_RlCpuCountersReset_Type())
rlCpuCountersReset.setMaxAccess(_G)
if mibBuilder.loadTexts:rlCpuCountersReset.setStatus(_A)
class _RlCpuCountersEnabled_Type(TruthValue):defaultValue=2
_RlCpuCountersEnabled_Type.__name__=_C
_RlCpuCountersEnabled_Object=MibScalar
rlCpuCountersEnabled=_RlCpuCountersEnabled_Object((1,3,6,1,4,1,4526,17,124,3),_RlCpuCountersEnabled_Type())
rlCpuCountersEnabled.setMaxAccess(_G)
if mibBuilder.loadTexts:rlCpuCountersEnabled.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'rlCpuCounters':rlCpuCounters,'rlCpuCountersTable':rlCpuCountersTable,'rlCpuCountersEntry':rlCpuCountersEntry,_F:rlCpuCountersTarget,'rlCpuCountersTxBC':rlCpuCountersTxBC,'rlCpuCountersTxMC':rlCpuCountersTxMC,'rlCpuCountersTxUC':rlCpuCountersTxUC,'rlCpuCountersTxOctets':rlCpuCountersTxOctets,'rlCpuCountersRxBC':rlCpuCountersRxBC,'rlCpuCountersRxMC':rlCpuCountersRxMC,'rlCpuCountersRxUC':rlCpuCountersRxUC,'rlCpuCountersRxOctets':rlCpuCountersRxOctets,'rlCpuCountersReset':rlCpuCountersReset,'rlCpuCountersEnabled':rlCpuCountersEnabled})