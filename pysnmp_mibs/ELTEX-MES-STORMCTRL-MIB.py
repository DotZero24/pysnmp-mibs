_E='eltStormCtrlRateLimCfgEntry'
_D='ELTEX-MES-STORMCTRL-MIB'
_C='read-write'
_B='Unsigned32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltMes,=mibBuilder.importSymbols('ELTEX-MES','eltMes')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
rlStormCtrlRateLimCfgEntry,=mibBuilder.importSymbols('RADLAN-STORMCTRL-MIB','rlStormCtrlRateLimCfgEntry')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_B,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
eltMesStormCtrl=ModuleIdentity((1,3,6,1,4,1,35265,1,23,77))
if mibBuilder.loadTexts:eltMesStormCtrl.setRevisions(('2015-10-29 00:00','2014-12-30 00:00'))
class EltStormCtrlActionType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('trap',2),('shutdown',3),('trapAndShutdown',4)))
_EltMesStormCtrlMIBObjects_ObjectIdentity=ObjectIdentity
eltMesStormCtrlMIBObjects=_EltMesStormCtrlMIBObjects_ObjectIdentity((1,3,6,1,4,1,35265,1,23,77,1))
_EltMesStormCtrlConfig_ObjectIdentity=ObjectIdentity
eltMesStormCtrlConfig=_EltMesStormCtrlConfig_ObjectIdentity((1,3,6,1,4,1,35265,1,23,77,1,1))
_EltStormCtrlRateLimCfgTable_Object=MibTable
eltStormCtrlRateLimCfgTable=_EltStormCtrlRateLimCfgTable_Object((1,3,6,1,4,1,35265,1,23,77,1,1,3))
if mibBuilder.loadTexts:eltStormCtrlRateLimCfgTable.setStatus(_A)
_EltStormCtrlRateLimCfgEntry_Object=MibTableRow
eltStormCtrlRateLimCfgEntry=_EltStormCtrlRateLimCfgEntry_Object((1,3,6,1,4,1,35265,1,23,77,1,1,3,1))
if mibBuilder.loadTexts:eltStormCtrlRateLimCfgEntry.setStatus(_A)
_EltStormCtrlRateLimCfgPpsAction_Type=EltStormCtrlActionType
_EltStormCtrlRateLimCfgPpsAction_Object=MibTableColumn
eltStormCtrlRateLimCfgPpsAction=_EltStormCtrlRateLimCfgPpsAction_Object((1,3,6,1,4,1,35265,1,23,77,1,1,3,1,1),_EltStormCtrlRateLimCfgPpsAction_Type())
eltStormCtrlRateLimCfgPpsAction.setMaxAccess(_C)
if mibBuilder.loadTexts:eltStormCtrlRateLimCfgPpsAction.setStatus(_A)
class _EltStormCtrlRateLimCfgRatePps_Type(Unsigned32):defaultValue=0
_EltStormCtrlRateLimCfgRatePps_Type.__name__=_B
_EltStormCtrlRateLimCfgRatePps_Object=MibTableColumn
eltStormCtrlRateLimCfgRatePps=_EltStormCtrlRateLimCfgRatePps_Object((1,3,6,1,4,1,35265,1,23,77,1,1,3,1,2),_EltStormCtrlRateLimCfgRatePps_Type())
eltStormCtrlRateLimCfgRatePps.setMaxAccess(_C)
if mibBuilder.loadTexts:eltStormCtrlRateLimCfgRatePps.setStatus(_A)
class _EltStormCtrlRateLimCfgBurstSizePackets_Type(Unsigned32):defaultValue=0
_EltStormCtrlRateLimCfgBurstSizePackets_Type.__name__=_B
_EltStormCtrlRateLimCfgBurstSizePackets_Object=MibTableColumn
eltStormCtrlRateLimCfgBurstSizePackets=_EltStormCtrlRateLimCfgBurstSizePackets_Object((1,3,6,1,4,1,35265,1,23,77,1,1,3,1,3),_EltStormCtrlRateLimCfgBurstSizePackets_Type())
eltStormCtrlRateLimCfgBurstSizePackets.setMaxAccess(_C)
if mibBuilder.loadTexts:eltStormCtrlRateLimCfgBurstSizePackets.setStatus(_A)
rlStormCtrlRateLimCfgEntry.registerAugmentions((_D,_E))
eltStormCtrlRateLimCfgEntry.setIndexNames(*rlStormCtrlRateLimCfgEntry.getIndexNames())
mibBuilder.exportSymbols(_D,**{'EltStormCtrlActionType':EltStormCtrlActionType,'eltMesStormCtrl':eltMesStormCtrl,'eltMesStormCtrlMIBObjects':eltMesStormCtrlMIBObjects,'eltMesStormCtrlConfig':eltMesStormCtrlConfig,'eltStormCtrlRateLimCfgTable':eltStormCtrlRateLimCfgTable,_E:eltStormCtrlRateLimCfgEntry,'eltStormCtrlRateLimCfgPpsAction':eltStormCtrlRateLimCfgPpsAction,'eltStormCtrlRateLimCfgRatePps':eltStormCtrlRateLimCfgRatePps,'eltStormCtrlRateLimCfgBurstSizePackets':eltStormCtrlRateLimCfgBurstSizePackets})