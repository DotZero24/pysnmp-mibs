_H='hpeStormControlIfStatus'
_G='HPE-STORMCONTROL-MIB'
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
hpVCSE_40Gb_F8_Module,=mibBuilder.importSymbols('HPSVRMGMT-OID','hpVCSE-40Gb-F8-Module')
ifIndex,=mibBuilder.importSymbols(_D,_E)
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
hpeStormControl=ModuleIdentity((1,3,6,1,4,1,11,5,7,5,8,1,4110))
if mibBuilder.loadTexts:hpeStormControl.setRevisions(('2015-06-26 00:00',))
_HpeSynergyVCMIBObjects_ObjectIdentity=ObjectIdentity
hpeSynergyVCMIBObjects=_HpeSynergyVCMIBObjects_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,8,1))
_HpeStormControlGroup_ObjectIdentity=ObjectIdentity
hpeStormControlGroup=_HpeStormControlGroup_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,8,1,1))
class _HpeStormControlSystemStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disable',0),('enable',1)))
_HpeStormControlSystemStatus_Type.__name__=_B
_HpeStormControlSystemStatus_Object=MibScalar
hpeStormControlSystemStatus=_HpeStormControlSystemStatus_Object((1,3,6,1,4,1,11,5,7,5,8,1,1,1),_HpeStormControlSystemStatus_Type())
hpeStormControlSystemStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:hpeStormControlSystemStatus.setStatus(_A)
class _HpeStormControlSystemRateLimitInPps_Type(Integer32):defaultValue=0
_HpeStormControlSystemRateLimitInPps_Type.__name__=_B
_HpeStormControlSystemRateLimitInPps_Object=MibScalar
hpeStormControlSystemRateLimitInPps=_HpeStormControlSystemRateLimitInPps_Object((1,3,6,1,4,1,11,5,7,5,8,1,1,2),_HpeStormControlSystemRateLimitInPps_Type())
hpeStormControlSystemRateLimitInPps.setMaxAccess(_F)
if mibBuilder.loadTexts:hpeStormControlSystemRateLimitInPps.setStatus(_A)
class _HpeStormControlSystemPollingInterval_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,300))
_HpeStormControlSystemPollingInterval_Type.__name__=_B
_HpeStormControlSystemPollingInterval_Object=MibScalar
hpeStormControlSystemPollingInterval=_HpeStormControlSystemPollingInterval_Object((1,3,6,1,4,1,11,5,7,5,8,1,1,3),_HpeStormControlSystemPollingInterval_Type())
hpeStormControlSystemPollingInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:hpeStormControlSystemPollingInterval.setStatus(_A)
if mibBuilder.loadTexts:hpeStormControlSystemPollingInterval.setUnits('Seconds')
_HpeStormControlStatsTable_Object=MibTable
hpeStormControlStatsTable=_HpeStormControlStatsTable_Object((1,3,6,1,4,1,11,5,7,5,8,1,1,4))
if mibBuilder.loadTexts:hpeStormControlStatsTable.setStatus(_A)
_HpeStormControlStatsEntry_Object=MibTableRow
hpeStormControlStatsEntry=_HpeStormControlStatsEntry_Object((1,3,6,1,4,1,11,5,7,5,8,1,1,4,1))
hpeStormControlStatsEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:hpeStormControlStatsEntry.setStatus(_A)
_HpeStormControlDLFDropCounters_Type=Counter32
_HpeStormControlDLFDropCounters_Object=MibTableColumn
hpeStormControlDLFDropCounters=_HpeStormControlDLFDropCounters_Object((1,3,6,1,4,1,11,5,7,5,8,1,1,4,1,1),_HpeStormControlDLFDropCounters_Type())
hpeStormControlDLFDropCounters.setMaxAccess(_C)
if mibBuilder.loadTexts:hpeStormControlDLFDropCounters.setStatus(_A)
_HpeStormControlMCASTDropCounters_Type=Counter32
_HpeStormControlMCASTDropCounters_Object=MibTableColumn
hpeStormControlMCASTDropCounters=_HpeStormControlMCASTDropCounters_Object((1,3,6,1,4,1,11,5,7,5,8,1,1,4,1,2),_HpeStormControlMCASTDropCounters_Type())
hpeStormControlMCASTDropCounters.setMaxAccess(_C)
if mibBuilder.loadTexts:hpeStormControlMCASTDropCounters.setStatus(_A)
_HpeStormControlBCASTDropCounters_Type=Counter32
_HpeStormControlBCASTDropCounters_Object=MibTableColumn
hpeStormControlBCASTDropCounters=_HpeStormControlBCASTDropCounters_Object((1,3,6,1,4,1,11,5,7,5,8,1,1,4,1,3),_HpeStormControlBCASTDropCounters_Type())
hpeStormControlBCASTDropCounters.setMaxAccess(_C)
if mibBuilder.loadTexts:hpeStormControlBCASTDropCounters.setStatus(_A)
class _HpeStormControlIfStatus_Type(Integer32):defaultValue=0
_HpeStormControlIfStatus_Type.__name__=_B
_HpeStormControlIfStatus_Object=MibTableColumn
hpeStormControlIfStatus=_HpeStormControlIfStatus_Object((1,3,6,1,4,1,11,5,7,5,8,1,1,4,1,4),_HpeStormControlIfStatus_Type())
hpeStormControlIfStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpeStormControlIfStatus.setStatus(_A)
_HpeStormControlTrap_ObjectIdentity=ObjectIdentity
hpeStormControlTrap=_HpeStormControlTrap_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,8,1,4110,2))
hpestormControlTrap=NotificationType((1,3,6,1,4,1,11,5,7,5,8,1,4110,2,1))
hpestormControlTrap.setObjects(*((_D,_E),(_G,_H)))
if mibBuilder.loadTexts:hpestormControlTrap.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'hpeSynergyVCMIBObjects':hpeSynergyVCMIBObjects,'hpeStormControlGroup':hpeStormControlGroup,'hpeStormControlSystemStatus':hpeStormControlSystemStatus,'hpeStormControlSystemRateLimitInPps':hpeStormControlSystemRateLimitInPps,'hpeStormControlSystemPollingInterval':hpeStormControlSystemPollingInterval,'hpeStormControlStatsTable':hpeStormControlStatsTable,'hpeStormControlStatsEntry':hpeStormControlStatsEntry,'hpeStormControlDLFDropCounters':hpeStormControlDLFDropCounters,'hpeStormControlMCASTDropCounters':hpeStormControlMCASTDropCounters,'hpeStormControlBCASTDropCounters':hpeStormControlBCASTDropCounters,_H:hpeStormControlIfStatus,'hpeStormControl':hpeStormControl,'hpeStormControlTrap':hpeStormControlTrap,'hpestormControlTrap':hpestormControlTrap})