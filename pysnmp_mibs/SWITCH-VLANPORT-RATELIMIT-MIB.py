_H='rcVlanPortRateLimitVlanIndex'
_G='rcVlanPortRateLimitPortRule'
_F='rcVlanPortRateLimitPortIndex'
_E='read-create'
_D='not-accessible'
_C='Integer32'
_B='SWITCH-VLANPORT-RATELIMIT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
iscomSwitch,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','iscomSwitch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
EnableVar,=mibBuilder.importSymbols('SWITCH-TC','EnableVar')
rcRateLimit=ModuleIdentity((1,3,6,1,4,1,8886,6,1,2))
_RcVlanPortRateLimitTable_Object=MibTable
rcVlanPortRateLimitTable=_RcVlanPortRateLimitTable_Object((1,3,6,1,4,1,8886,6,1,2,5))
if mibBuilder.loadTexts:rcVlanPortRateLimitTable.setStatus(_A)
_RcVlanPortRateLimitEntry_Object=MibTableRow
rcVlanPortRateLimitEntry=_RcVlanPortRateLimitEntry_Object((1,3,6,1,4,1,8886,6,1,2,5,1))
rcVlanPortRateLimitEntry.setIndexNames((0,_B,_F),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:rcVlanPortRateLimitEntry.setStatus(_A)
_RcVlanPortRateLimitPortIndex_Type=Integer32
_RcVlanPortRateLimitPortIndex_Object=MibTableColumn
rcVlanPortRateLimitPortIndex=_RcVlanPortRateLimitPortIndex_Object((1,3,6,1,4,1,8886,6,1,2,5,1,1),_RcVlanPortRateLimitPortIndex_Type())
rcVlanPortRateLimitPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:rcVlanPortRateLimitPortIndex.setStatus(_A)
class _RcVlanPortRateLimitPortRule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ingress',1),('egress',2)))
_RcVlanPortRateLimitPortRule_Type.__name__=_C
_RcVlanPortRateLimitPortRule_Object=MibTableColumn
rcVlanPortRateLimitPortRule=_RcVlanPortRateLimitPortRule_Object((1,3,6,1,4,1,8886,6,1,2,5,1,2),_RcVlanPortRateLimitPortRule_Type())
rcVlanPortRateLimitPortRule.setMaxAccess(_D)
if mibBuilder.loadTexts:rcVlanPortRateLimitPortRule.setStatus(_A)
class _RcVlanPortRateLimitVlanIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_RcVlanPortRateLimitVlanIndex_Type.__name__=_C
_RcVlanPortRateLimitVlanIndex_Object=MibTableColumn
rcVlanPortRateLimitVlanIndex=_RcVlanPortRateLimitVlanIndex_Object((1,3,6,1,4,1,8886,6,1,2,5,1,3),_RcVlanPortRateLimitVlanIndex_Type())
rcVlanPortRateLimitVlanIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:rcVlanPortRateLimitVlanIndex.setStatus(_A)
_RcVlanPortRateLimitRate_Type=Integer32
_RcVlanPortRateLimitRate_Object=MibTableColumn
rcVlanPortRateLimitRate=_RcVlanPortRateLimitRate_Object((1,3,6,1,4,1,8886,6,1,2,5,1,4),_RcVlanPortRateLimitRate_Type())
rcVlanPortRateLimitRate.setMaxAccess(_E)
if mibBuilder.loadTexts:rcVlanPortRateLimitRate.setStatus(_A)
if mibBuilder.loadTexts:rcVlanPortRateLimitRate.setUnits('kbps')
_RcVlanPortRateLimitBurst_Type=Integer32
_RcVlanPortRateLimitBurst_Object=MibTableColumn
rcVlanPortRateLimitBurst=_RcVlanPortRateLimitBurst_Object((1,3,6,1,4,1,8886,6,1,2,5,1,5),_RcVlanPortRateLimitBurst_Type())
rcVlanPortRateLimitBurst.setMaxAccess(_E)
if mibBuilder.loadTexts:rcVlanPortRateLimitBurst.setStatus(_A)
if mibBuilder.loadTexts:rcVlanPortRateLimitBurst.setUnits('kB')
_RcVlanPortRateLimitRowStatus_Type=RowStatus
_RcVlanPortRateLimitRowStatus_Object=MibTableColumn
rcVlanPortRateLimitRowStatus=_RcVlanPortRateLimitRowStatus_Object((1,3,6,1,4,1,8886,6,1,2,5,1,6),_RcVlanPortRateLimitRowStatus_Type())
rcVlanPortRateLimitRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:rcVlanPortRateLimitRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'rcRateLimit':rcRateLimit,'rcVlanPortRateLimitTable':rcVlanPortRateLimitTable,'rcVlanPortRateLimitEntry':rcVlanPortRateLimitEntry,_F:rcVlanPortRateLimitPortIndex,_G:rcVlanPortRateLimitPortRule,_H:rcVlanPortRateLimitVlanIndex,'rcVlanPortRateLimitRate':rcVlanPortRateLimitRate,'rcVlanPortRateLimitBurst':rcVlanPortRateLimitBurst,'rcVlanPortRateLimitRowStatus':rcVlanPortRateLimitRowStatus})