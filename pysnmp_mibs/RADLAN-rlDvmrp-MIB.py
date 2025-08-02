_J='rlDvmrpRouteDesignatedForwarderExtEntry'
_I='RADLAN-rlDvmrp-MIB'
_H='read-only'
_G='rndErrorSeverity'
_F='rndErrorDesc'
_E='RADLAN-DEVICEPARAMS-MIB'
_D='seconds'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dvmrpRouteNextHopEntry,dvmrpRouteNextHopIfIndex,dvmrpRouteNextHopSource,dvmrpRouteNextHopSourceMask=mibBuilder.importSymbols('DVMRP-STD-MIB','dvmrpRouteNextHopEntry','dvmrpRouteNextHopIfIndex','dvmrpRouteNextHopSource','dvmrpRouteNextHopSourceMask')
rndErrorDesc,rndErrorSeverity=mibBuilder.importSymbols(_E,_F,_G)
rnd,rndNotifications=mibBuilder.importSymbols('RADLAN-MIB','rnd','rndNotifications')
rlIPmulticast,=mibBuilder.importSymbols('RADLAN-rlIPMulticast-MIB','rlIPmulticast')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
rlDvmrp=ModuleIdentity((1,3,6,1,4,1,89,46,4))
if mibBuilder.loadTexts:rlDvmrp.setRevisions(('2004-04-19 00:00',))
_RlDvmrpMibVersion_Type=Integer32
_RlDvmrpMibVersion_Object=MibScalar
rlDvmrpMibVersion=_RlDvmrpMibVersion_Object((1,3,6,1,4,1,89,46,4,2),_RlDvmrpMibVersion_Type())
rlDvmrpMibVersion.setMaxAccess(_H)
if mibBuilder.loadTexts:rlDvmrpMibVersion.setStatus(_A)
class _RlDvmrpEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_RlDvmrpEnable_Type.__name__=_B
_RlDvmrpEnable_Object=MibScalar
rlDvmrpEnable=_RlDvmrpEnable_Object((1,3,6,1,4,1,89,46,4,3),_RlDvmrpEnable_Type())
rlDvmrpEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDvmrpEnable.setStatus(_A)
class _RlDvmrpProbeInterval_Type(Integer32):defaultValue=10
_RlDvmrpProbeInterval_Type.__name__=_B
_RlDvmrpProbeInterval_Object=MibScalar
rlDvmrpProbeInterval=_RlDvmrpProbeInterval_Object((1,3,6,1,4,1,89,46,4,4),_RlDvmrpProbeInterval_Type())
rlDvmrpProbeInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDvmrpProbeInterval.setStatus(_A)
if mibBuilder.loadTexts:rlDvmrpProbeInterval.setUnits(_D)
class _RlDvmrpNeighborTimeOutInterval_Type(Integer32):defaultValue=35;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(25,400))
_RlDvmrpNeighborTimeOutInterval_Type.__name__=_B
_RlDvmrpNeighborTimeOutInterval_Object=MibScalar
rlDvmrpNeighborTimeOutInterval=_RlDvmrpNeighborTimeOutInterval_Object((1,3,6,1,4,1,89,46,4,5),_RlDvmrpNeighborTimeOutInterval_Type())
rlDvmrpNeighborTimeOutInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDvmrpNeighborTimeOutInterval.setStatus(_A)
if mibBuilder.loadTexts:rlDvmrpNeighborTimeOutInterval.setUnits(_D)
class _RlDvmrpMinFlashUpdateInterval_Type(Integer32):defaultValue=5
_RlDvmrpMinFlashUpdateInterval_Type.__name__=_B
_RlDvmrpMinFlashUpdateInterval_Object=MibScalar
rlDvmrpMinFlashUpdateInterval=_RlDvmrpMinFlashUpdateInterval_Object((1,3,6,1,4,1,89,46,4,6),_RlDvmrpMinFlashUpdateInterval_Type())
rlDvmrpMinFlashUpdateInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDvmrpMinFlashUpdateInterval.setStatus(_A)
if mibBuilder.loadTexts:rlDvmrpMinFlashUpdateInterval.setUnits(_D)
class _RlDvmrpRouteReportInterval_Type(Integer32):defaultValue=60
_RlDvmrpRouteReportInterval_Type.__name__=_B
_RlDvmrpRouteReportInterval_Object=MibScalar
rlDvmrpRouteReportInterval=_RlDvmrpRouteReportInterval_Object((1,3,6,1,4,1,89,46,4,7),_RlDvmrpRouteReportInterval_Type())
rlDvmrpRouteReportInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDvmrpRouteReportInterval.setStatus(_A)
if mibBuilder.loadTexts:rlDvmrpRouteReportInterval.setUnits(_D)
class _RlDvmrpRouteExpirationTime_Type(Integer32):defaultValue=140
_RlDvmrpRouteExpirationTime_Type.__name__=_B
_RlDvmrpRouteExpirationTime_Object=MibScalar
rlDvmrpRouteExpirationTime=_RlDvmrpRouteExpirationTime_Object((1,3,6,1,4,1,89,46,4,8),_RlDvmrpRouteExpirationTime_Type())
rlDvmrpRouteExpirationTime.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDvmrpRouteExpirationTime.setStatus(_A)
if mibBuilder.loadTexts:rlDvmrpRouteExpirationTime.setUnits(_D)
class _RlDvmrpPruneLifetime_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(200,7200))
_RlDvmrpPruneLifetime_Type.__name__=_B
_RlDvmrpPruneLifetime_Object=MibScalar
rlDvmrpPruneLifetime=_RlDvmrpPruneLifetime_Object((1,3,6,1,4,1,89,46,4,9),_RlDvmrpPruneLifetime_Type())
rlDvmrpPruneLifetime.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDvmrpPruneLifetime.setStatus(_A)
if mibBuilder.loadTexts:rlDvmrpPruneLifetime.setUnits(_D)
_RlDvmrpRouteDesignatedForwarderExtTable_Object=MibTable
rlDvmrpRouteDesignatedForwarderExtTable=_RlDvmrpRouteDesignatedForwarderExtTable_Object((1,3,6,1,4,1,89,46,4,10))
if mibBuilder.loadTexts:rlDvmrpRouteDesignatedForwarderExtTable.setStatus(_A)
_RlDvmrpRouteDesignatedForwarderExtEntry_Object=MibTableRow
rlDvmrpRouteDesignatedForwarderExtEntry=_RlDvmrpRouteDesignatedForwarderExtEntry_Object((1,3,6,1,4,1,89,46,4,10,1))
if mibBuilder.loadTexts:rlDvmrpRouteDesignatedForwarderExtEntry.setStatus(_A)
_RlDvmrpRouteDesignatedForwarder_Type=IpAddress
_RlDvmrpRouteDesignatedForwarder_Object=MibTableColumn
rlDvmrpRouteDesignatedForwarder=_RlDvmrpRouteDesignatedForwarder_Object((1,3,6,1,4,1,89,46,4,10,1,1),_RlDvmrpRouteDesignatedForwarder_Type())
rlDvmrpRouteDesignatedForwarder.setMaxAccess(_H)
if mibBuilder.loadTexts:rlDvmrpRouteDesignatedForwarder.setStatus(_A)
dvmrpRouteNextHopEntry.registerAugmentions((_I,_J))
rlDvmrpRouteDesignatedForwarderExtEntry.setIndexNames(*dvmrpRouteNextHopEntry.getIndexNames())
rlDvmrpTableOverflow=NotificationType((1,3,6,1,4,1,89,0,155))
rlDvmrpTableOverflow.setObjects(*((_E,_F),(_E,_G)))
if mibBuilder.loadTexts:rlDvmrpTableOverflow.setStatus(_A)
mibBuilder.exportSymbols(_I,**{'rlDvmrpTableOverflow':rlDvmrpTableOverflow,'rlDvmrp':rlDvmrp,'rlDvmrpMibVersion':rlDvmrpMibVersion,'rlDvmrpEnable':rlDvmrpEnable,'rlDvmrpProbeInterval':rlDvmrpProbeInterval,'rlDvmrpNeighborTimeOutInterval':rlDvmrpNeighborTimeOutInterval,'rlDvmrpMinFlashUpdateInterval':rlDvmrpMinFlashUpdateInterval,'rlDvmrpRouteReportInterval':rlDvmrpRouteReportInterval,'rlDvmrpRouteExpirationTime':rlDvmrpRouteExpirationTime,'rlDvmrpPruneLifetime':rlDvmrpPruneLifetime,'rlDvmrpRouteDesignatedForwarderExtTable':rlDvmrpRouteDesignatedForwarderExtTable,_J:rlDvmrpRouteDesignatedForwarderExtEntry,'rlDvmrpRouteDesignatedForwarder':rlDvmrpRouteDesignatedForwarder})