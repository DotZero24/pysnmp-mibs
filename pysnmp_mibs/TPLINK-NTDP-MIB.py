_F='TPLINK-NTDP-MIB'
_E='enable'
_D='disable'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ntdpManage,=mibBuilder.importSymbols('TPLINK-CLUSTER-MIB','ntdpManage')
_NtdpGlobalConfig_ObjectIdentity=ObjectIdentity
ntdpGlobalConfig=_NtdpGlobalConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,33,1,1,2,1))
class _NtdpStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NtdpStatus_Type.__name__=_B
_NtdpStatus_Object=MibScalar
ntdpStatus=_NtdpStatus_Object((1,3,6,1,4,1,11863,6,33,1,1,2,1,1),_NtdpStatus_Type())
ntdpStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ntdpStatus.setStatus(_A)
class _NtdpIntervalTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_NtdpIntervalTime_Type.__name__=_B
_NtdpIntervalTime_Object=MibScalar
ntdpIntervalTime=_NtdpIntervalTime_Object((1,3,6,1,4,1,11863,6,33,1,1,2,1,2),_NtdpIntervalTime_Type())
ntdpIntervalTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ntdpIntervalTime.setStatus(_A)
class _NtdpHop_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_NtdpHop_Type.__name__=_B
_NtdpHop_Object=MibScalar
ntdpHop=_NtdpHop_Object((1,3,6,1,4,1,11863,6,33,1,1,2,1,3),_NtdpHop_Type())
ntdpHop.setMaxAccess(_C)
if mibBuilder.loadTexts:ntdpHop.setStatus(_A)
class _NtdpHopDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_NtdpHopDelay_Type.__name__=_B
_NtdpHopDelay_Object=MibScalar
ntdpHopDelay=_NtdpHopDelay_Object((1,3,6,1,4,1,11863,6,33,1,1,2,1,4),_NtdpHopDelay_Type())
ntdpHopDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:ntdpHopDelay.setStatus(_A)
class _NtpdPortDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_NtpdPortDelay_Type.__name__=_B
_NtpdPortDelay_Object=MibScalar
ntpdPortDelay=_NtpdPortDelay_Object((1,3,6,1,4,1,11863,6,33,1,1,2,1,5),_NtpdPortDelay_Type())
ntpdPortDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:ntpdPortDelay.setStatus(_A)
_NtdpPortTable_Object=MibTable
ntdpPortTable=_NtdpPortTable_Object((1,3,6,1,4,1,11863,6,33,1,1,2,2))
if mibBuilder.loadTexts:ntdpPortTable.setStatus(_A)
_NtdpPortEntry_Object=MibTableRow
ntdpPortEntry=_NtdpPortEntry_Object((1,3,6,1,4,1,11863,6,33,1,1,2,2,1))
ntdpPortEntry.setIndexNames((0,_F,'ifIndex'))
if mibBuilder.loadTexts:ntdpPortEntry.setStatus(_A)
class _NtdpPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NtdpPortStatus_Type.__name__=_B
_NtdpPortStatus_Object=MibTableColumn
ntdpPortStatus=_NtdpPortStatus_Object((1,3,6,1,4,1,11863,6,33,1,1,2,2,1,2),_NtdpPortStatus_Type())
ntdpPortStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ntdpPortStatus.setStatus(_A)
class _NtdpCollectTopo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('commit',1))
_NtdpCollectTopo_Type.__name__=_B
_NtdpCollectTopo_Object=MibScalar
ntdpCollectTopo=_NtdpCollectTopo_Object((1,3,6,1,4,1,11863,6,33,1,1,2,4),_NtdpCollectTopo_Type())
ntdpCollectTopo.setMaxAccess(_C)
if mibBuilder.loadTexts:ntdpCollectTopo.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'ntdpGlobalConfig':ntdpGlobalConfig,'ntdpStatus':ntdpStatus,'ntdpIntervalTime':ntdpIntervalTime,'ntdpHop':ntdpHop,'ntdpHopDelay':ntdpHopDelay,'ntpdPortDelay':ntpdPortDelay,'ntdpPortTable':ntdpPortTable,'ntdpPortEntry':ntdpPortEntry,'ntdpPortStatus':ntdpPortStatus,'ntdpCollectTopo':ntdpCollectTopo})