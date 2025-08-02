_H='syn100GhpeStormControlIfStatus'
_G='SYNERGY100G-HPE-STORMCONTROL-MIB'
_F='read-write'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpVCSE_100Gb_F32_Module,=mibBuilder.importSymbols('HPSVRMGMT-OID','hpVCSE-100Gb-F32-Module')
ifIndex,=mibBuilder.importSymbols(_D,_E)
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
syn100GhpeStormControl=ModuleIdentity((1,3,6,1,4,1,11,5,7,5,9,1,4110))
if mibBuilder.loadTexts:syn100GhpeStormControl.setRevisions(('2015-06-26 00:00',))
_Syn100GhpeSynergyStormControlMIBObjects_ObjectIdentity=ObjectIdentity
syn100GhpeSynergyStormControlMIBObjects=_Syn100GhpeSynergyStormControlMIBObjects_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,9,1))
_Syn100GhpeStormControlGroup_ObjectIdentity=ObjectIdentity
syn100GhpeStormControlGroup=_Syn100GhpeStormControlGroup_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,9,1,1))
class _Syn100GhpeStormControlSystemStatus_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disable',0),('enable',1)))
_Syn100GhpeStormControlSystemStatus_Type.__name__=_B
_Syn100GhpeStormControlSystemStatus_Object=MibScalar
syn100GhpeStormControlSystemStatus=_Syn100GhpeStormControlSystemStatus_Object((1,3,6,1,4,1,11,5,7,5,9,1,1,1),_Syn100GhpeStormControlSystemStatus_Type())
syn100GhpeStormControlSystemStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:syn100GhpeStormControlSystemStatus.setStatus(_A)
class _Syn100GhpeStormControlSystemRateLimitInPps_Type(Integer32):defaultValue=0
_Syn100GhpeStormControlSystemRateLimitInPps_Type.__name__=_B
_Syn100GhpeStormControlSystemRateLimitInPps_Object=MibScalar
syn100GhpeStormControlSystemRateLimitInPps=_Syn100GhpeStormControlSystemRateLimitInPps_Object((1,3,6,1,4,1,11,5,7,5,9,1,1,2),_Syn100GhpeStormControlSystemRateLimitInPps_Type())
syn100GhpeStormControlSystemRateLimitInPps.setMaxAccess(_F)
if mibBuilder.loadTexts:syn100GhpeStormControlSystemRateLimitInPps.setStatus(_A)
class _Syn100GhpeStormControlSystemPollingInterval_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,300))
_Syn100GhpeStormControlSystemPollingInterval_Type.__name__=_B
_Syn100GhpeStormControlSystemPollingInterval_Object=MibScalar
syn100GhpeStormControlSystemPollingInterval=_Syn100GhpeStormControlSystemPollingInterval_Object((1,3,6,1,4,1,11,5,7,5,9,1,1,3),_Syn100GhpeStormControlSystemPollingInterval_Type())
syn100GhpeStormControlSystemPollingInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:syn100GhpeStormControlSystemPollingInterval.setStatus(_A)
if mibBuilder.loadTexts:syn100GhpeStormControlSystemPollingInterval.setUnits('Seconds')
_Syn100GhpeStormControlStatsTable_Object=MibTable
syn100GhpeStormControlStatsTable=_Syn100GhpeStormControlStatsTable_Object((1,3,6,1,4,1,11,5,7,5,9,1,1,4))
if mibBuilder.loadTexts:syn100GhpeStormControlStatsTable.setStatus(_A)
_Syn100GhpeStormControlStatsEntry_Object=MibTableRow
syn100GhpeStormControlStatsEntry=_Syn100GhpeStormControlStatsEntry_Object((1,3,6,1,4,1,11,5,7,5,9,1,1,4,1))
syn100GhpeStormControlStatsEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:syn100GhpeStormControlStatsEntry.setStatus(_A)
_Syn100GhpeStormControlDLFDropCounters_Type=Counter32
_Syn100GhpeStormControlDLFDropCounters_Object=MibTableColumn
syn100GhpeStormControlDLFDropCounters=_Syn100GhpeStormControlDLFDropCounters_Object((1,3,6,1,4,1,11,5,7,5,9,1,1,4,1,1),_Syn100GhpeStormControlDLFDropCounters_Type())
syn100GhpeStormControlDLFDropCounters.setMaxAccess(_C)
if mibBuilder.loadTexts:syn100GhpeStormControlDLFDropCounters.setStatus(_A)
_Syn100GhpeStormControlMCASTDropCounters_Type=Counter32
_Syn100GhpeStormControlMCASTDropCounters_Object=MibTableColumn
syn100GhpeStormControlMCASTDropCounters=_Syn100GhpeStormControlMCASTDropCounters_Object((1,3,6,1,4,1,11,5,7,5,9,1,1,4,1,2),_Syn100GhpeStormControlMCASTDropCounters_Type())
syn100GhpeStormControlMCASTDropCounters.setMaxAccess(_C)
if mibBuilder.loadTexts:syn100GhpeStormControlMCASTDropCounters.setStatus(_A)
_Syn100GhpeStormControlBCASTDropCounters_Type=Counter32
_Syn100GhpeStormControlBCASTDropCounters_Object=MibTableColumn
syn100GhpeStormControlBCASTDropCounters=_Syn100GhpeStormControlBCASTDropCounters_Object((1,3,6,1,4,1,11,5,7,5,9,1,1,4,1,3),_Syn100GhpeStormControlBCASTDropCounters_Type())
syn100GhpeStormControlBCASTDropCounters.setMaxAccess(_C)
if mibBuilder.loadTexts:syn100GhpeStormControlBCASTDropCounters.setStatus(_A)
class _Syn100GhpeStormControlIfStatus_Type(Integer32):defaultValue=0
_Syn100GhpeStormControlIfStatus_Type.__name__=_B
_Syn100GhpeStormControlIfStatus_Object=MibTableColumn
syn100GhpeStormControlIfStatus=_Syn100GhpeStormControlIfStatus_Object((1,3,6,1,4,1,11,5,7,5,9,1,1,4,1,4),_Syn100GhpeStormControlIfStatus_Type())
syn100GhpeStormControlIfStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:syn100GhpeStormControlIfStatus.setStatus(_A)
_Syn100GhpeStormControlTrap_ObjectIdentity=ObjectIdentity
syn100GhpeStormControlTrap=_Syn100GhpeStormControlTrap_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,9,1,4110,2))
syn100GhpestormControlTrap=NotificationType((1,3,6,1,4,1,11,5,7,5,9,1,4110,2,1))
syn100GhpestormControlTrap.setObjects(*((_D,_E),(_G,_H)))
if mibBuilder.loadTexts:syn100GhpestormControlTrap.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'syn100GhpeSynergyStormControlMIBObjects':syn100GhpeSynergyStormControlMIBObjects,'syn100GhpeStormControlGroup':syn100GhpeStormControlGroup,'syn100GhpeStormControlSystemStatus':syn100GhpeStormControlSystemStatus,'syn100GhpeStormControlSystemRateLimitInPps':syn100GhpeStormControlSystemRateLimitInPps,'syn100GhpeStormControlSystemPollingInterval':syn100GhpeStormControlSystemPollingInterval,'syn100GhpeStormControlStatsTable':syn100GhpeStormControlStatsTable,'syn100GhpeStormControlStatsEntry':syn100GhpeStormControlStatsEntry,'syn100GhpeStormControlDLFDropCounters':syn100GhpeStormControlDLFDropCounters,'syn100GhpeStormControlMCASTDropCounters':syn100GhpeStormControlMCASTDropCounters,'syn100GhpeStormControlBCASTDropCounters':syn100GhpeStormControlBCASTDropCounters,_H:syn100GhpeStormControlIfStatus,'syn100GhpeStormControl':syn100GhpeStormControl,'syn100GhpeStormControlTrap':syn100GhpeStormControlTrap,'syn100GhpestormControlTrap':syn100GhpestormControlTrap})