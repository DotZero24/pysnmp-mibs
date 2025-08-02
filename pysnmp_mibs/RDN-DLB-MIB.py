_K='rdnLoadBalanceDnstreamModemCount'
_J='rdnLoadBalanceUpstreamModemCount'
_I='Load-Balance Group ID [0-255]'
_H='read-write'
_G='rdnLoadBalBasicRuleId'
_F='2004-09-15 00:00'
_E='Integer32'
_D='RDN-DLB-MIB'
_C='read-create'
_B='Unsigned32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
riverdelta,=mibBuilder.importSymbols('RDN-MIB','riverdelta')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_B,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
rdnLoadBalance=ModuleIdentity((1,3,6,1,4,1,4981,8))
if mibBuilder.loadTexts:rdnLoadBalance.setRevisions(('2008-08-08 00:00',_F,_F))
_RdnLoadBalBasicRuleTable_Object=MibTable
rdnLoadBalBasicRuleTable=_RdnLoadBalBasicRuleTable_Object((1,3,6,1,4,1,4981,8,1))
if mibBuilder.loadTexts:rdnLoadBalBasicRuleTable.setStatus(_A)
_RdnLoadBalBasicRuleEntry_Object=MibTableRow
rdnLoadBalBasicRuleEntry=_RdnLoadBalBasicRuleEntry_Object((1,3,6,1,4,1,4981,8,1,1))
rdnLoadBalBasicRuleEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:rdnLoadBalBasicRuleEntry.setStatus(_A)
class _RdnLoadBalBasicRuleId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_RdnLoadBalBasicRuleId_Type.__name__=_B
_RdnLoadBalBasicRuleId_Object=MibTableColumn
rdnLoadBalBasicRuleId=_RdnLoadBalBasicRuleId_Object((1,3,6,1,4,1,4981,8,1,1,1),_RdnLoadBalBasicRuleId_Type())
rdnLoadBalBasicRuleId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:rdnLoadBalBasicRuleId.setStatus(_A)
class _RdnLoadBalBasicRuleEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('upstream',1),('downstream',2),('interval',3),('registration',4),('rem-dsx',5),('spec-trig',6),('ds-reg',7),('us-reg-bonding',8),('ds-reg-bonding',9)))
_RdnLoadBalBasicRuleEnable_Type.__name__=_E
_RdnLoadBalBasicRuleEnable_Object=MibTableColumn
rdnLoadBalBasicRuleEnable=_RdnLoadBalBasicRuleEnable_Object((1,3,6,1,4,1,4981,8,1,1,2),_RdnLoadBalBasicRuleEnable_Type())
rdnLoadBalBasicRuleEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rdnLoadBalBasicRuleEnable.setStatus(_A)
class _RdnLoadBalBasicRuleMinThres_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_RdnLoadBalBasicRuleMinThres_Type.__name__=_B
_RdnLoadBalBasicRuleMinThres_Object=MibTableColumn
rdnLoadBalBasicRuleMinThres=_RdnLoadBalBasicRuleMinThres_Object((1,3,6,1,4,1,4981,8,1,1,3),_RdnLoadBalBasicRuleMinThres_Type())
rdnLoadBalBasicRuleMinThres.setMaxAccess(_C)
if mibBuilder.loadTexts:rdnLoadBalBasicRuleMinThres.setStatus(_A)
class _RdnLoadBalBasicRuleDeltaThres_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_RdnLoadBalBasicRuleDeltaThres_Type.__name__=_B
_RdnLoadBalBasicRuleDeltaThres_Object=MibTableColumn
rdnLoadBalBasicRuleDeltaThres=_RdnLoadBalBasicRuleDeltaThres_Object((1,3,6,1,4,1,4981,8,1,1,4),_RdnLoadBalBasicRuleDeltaThres_Type())
rdnLoadBalBasicRuleDeltaThres.setMaxAccess(_C)
if mibBuilder.loadTexts:rdnLoadBalBasicRuleDeltaThres.setStatus(_A)
class _RdnLoadBalBasicRuleStopThres_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_RdnLoadBalBasicRuleStopThres_Type.__name__=_B
_RdnLoadBalBasicRuleStopThres_Object=MibTableColumn
rdnLoadBalBasicRuleStopThres=_RdnLoadBalBasicRuleStopThres_Object((1,3,6,1,4,1,4981,8,1,1,5),_RdnLoadBalBasicRuleStopThres_Type())
rdnLoadBalBasicRuleStopThres.setMaxAccess(_C)
if mibBuilder.loadTexts:rdnLoadBalBasicRuleStopThres.setStatus(_A)
_RdnLoadBalBasicRuleRowStatus_Type=RowStatus
_RdnLoadBalBasicRuleRowStatus_Object=MibTableColumn
rdnLoadBalBasicRuleRowStatus=_RdnLoadBalBasicRuleRowStatus_Object((1,3,6,1,4,1,4981,8,1,1,7),_RdnLoadBalBasicRuleRowStatus_Type())
rdnLoadBalBasicRuleRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rdnLoadBalBasicRuleRowStatus.setStatus(_A)
class _RdnLoadBalBasicRuleModemCountThres_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_RdnLoadBalBasicRuleModemCountThres_Type.__name__=_B
_RdnLoadBalBasicRuleModemCountThres_Object=MibTableColumn
rdnLoadBalBasicRuleModemCountThres=_RdnLoadBalBasicRuleModemCountThres_Object((1,3,6,1,4,1,4981,8,1,1,8),_RdnLoadBalBasicRuleModemCountThres_Type())
rdnLoadBalBasicRuleModemCountThres.setMaxAccess(_C)
if mibBuilder.loadTexts:rdnLoadBalBasicRuleModemCountThres.setStatus(_A)
class _RdnLoadBalanceUpstreamModemCount_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RdnLoadBalanceUpstreamModemCount_Type.__name__=_B
_RdnLoadBalanceUpstreamModemCount_Object=MibScalar
rdnLoadBalanceUpstreamModemCount=_RdnLoadBalanceUpstreamModemCount_Object((1,3,6,1,4,1,4981,8,2,1),_RdnLoadBalanceUpstreamModemCount_Type())
rdnLoadBalanceUpstreamModemCount.setMaxAccess(_H)
if mibBuilder.loadTexts:rdnLoadBalanceUpstreamModemCount.setStatus(_A)
if mibBuilder.loadTexts:rdnLoadBalanceUpstreamModemCount.setUnits(_I)
class _RdnLoadBalanceDnstreamModemCount_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RdnLoadBalanceDnstreamModemCount_Type.__name__=_B
_RdnLoadBalanceDnstreamModemCount_Object=MibScalar
rdnLoadBalanceDnstreamModemCount=_RdnLoadBalanceDnstreamModemCount_Object((1,3,6,1,4,1,4981,8,2,2),_RdnLoadBalanceDnstreamModemCount_Type())
rdnLoadBalanceDnstreamModemCount.setMaxAccess(_H)
if mibBuilder.loadTexts:rdnLoadBalanceDnstreamModemCount.setStatus(_A)
if mibBuilder.loadTexts:rdnLoadBalanceDnstreamModemCount.setUnits(_I)
class _RdnLoadBalGroupInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,480))
_RdnLoadBalGroupInterval_Type.__name__=_B
_RdnLoadBalGroupInterval_Object=MibScalar
rdnLoadBalGroupInterval=_RdnLoadBalGroupInterval_Object((1,3,6,1,4,1,4981,8,3),_RdnLoadBalGroupInterval_Type())
rdnLoadBalGroupInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:rdnLoadBalGroupInterval.setStatus(_A)
if mibBuilder.loadTexts:rdnLoadBalGroupInterval.setUnits('minutes')
rdnLoadBalOperations=ObjectGroup((1,3,6,1,4,1,4981,8,2))
rdnLoadBalOperations.setObjects(*((_D,_J),(_D,_K)))
if mibBuilder.loadTexts:rdnLoadBalOperations.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'rdnLoadBalance':rdnLoadBalance,'rdnLoadBalBasicRuleTable':rdnLoadBalBasicRuleTable,'rdnLoadBalBasicRuleEntry':rdnLoadBalBasicRuleEntry,_G:rdnLoadBalBasicRuleId,'rdnLoadBalBasicRuleEnable':rdnLoadBalBasicRuleEnable,'rdnLoadBalBasicRuleMinThres':rdnLoadBalBasicRuleMinThres,'rdnLoadBalBasicRuleDeltaThres':rdnLoadBalBasicRuleDeltaThres,'rdnLoadBalBasicRuleStopThres':rdnLoadBalBasicRuleStopThres,'rdnLoadBalBasicRuleRowStatus':rdnLoadBalBasicRuleRowStatus,'rdnLoadBalBasicRuleModemCountThres':rdnLoadBalBasicRuleModemCountThres,'rdnLoadBalOperations':rdnLoadBalOperations,_J:rdnLoadBalanceUpstreamModemCount,_K:rdnLoadBalanceDnstreamModemCount,'rdnLoadBalGroupInterval':rdnLoadBalGroupInterval})