_E='RAGuardPolicy'
_D='cnRAGuardIfCfgIfIndex'
_C='CAMBIUM-NETWORKS-IPV6-ND-RA-GUARD-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
PortList,VlanIdOrNone,dot1qStaticUnicastEntry,dot1qTpFdbEntry,dot1qTpFdbPort,dot1qVlanStaticEntry=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList','VlanIdOrNone','dot1qStaticUnicastEntry','dot1qTpFdbEntry','dot1qTpFdbPort','dot1qVlanStaticEntry')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
cnRAGuardMib=ModuleIdentity((1,3,6,1,4,1,17713,24,9))
if mibBuilder.loadTexts:cnRAGuardMib.setRevisions(('2021-11-28 00:00','2021-04-09 00:00'))
class RAGuardPolicy(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('router',0),('host',1)))
_CnRAGuardIfCfg_ObjectIdentity=ObjectIdentity
cnRAGuardIfCfg=_CnRAGuardIfCfg_ObjectIdentity((1,3,6,1,4,1,17713,24,9,1))
_CnRAGuardIfCfgTable_Object=MibTable
cnRAGuardIfCfgTable=_CnRAGuardIfCfgTable_Object((1,3,6,1,4,1,17713,24,9,1,1))
if mibBuilder.loadTexts:cnRAGuardIfCfgTable.setStatus(_A)
_CnRAGuardIfCfgEntry_Object=MibTableRow
cnRAGuardIfCfgEntry=_CnRAGuardIfCfgEntry_Object((1,3,6,1,4,1,17713,24,9,1,1,1))
cnRAGuardIfCfgEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:cnRAGuardIfCfgEntry.setStatus(_A)
class _CnRAGuardIfCfgIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,52))
_CnRAGuardIfCfgIfIndex_Type.__name__=_B
_CnRAGuardIfCfgIfIndex_Object=MibTableColumn
cnRAGuardIfCfgIfIndex=_CnRAGuardIfCfgIfIndex_Object((1,3,6,1,4,1,17713,24,9,1,1,1,1),_CnRAGuardIfCfgIfIndex_Type())
cnRAGuardIfCfgIfIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cnRAGuardIfCfgIfIndex.setStatus(_A)
class _CnRAGuardIfCfgPolicy_Type(RAGuardPolicy):defaultValue=0
_CnRAGuardIfCfgPolicy_Type.__name__=_E
_CnRAGuardIfCfgPolicy_Object=MibTableColumn
cnRAGuardIfCfgPolicy=_CnRAGuardIfCfgPolicy_Object((1,3,6,1,4,1,17713,24,9,1,1,1,2),_CnRAGuardIfCfgPolicy_Type())
cnRAGuardIfCfgPolicy.setMaxAccess('read-write')
if mibBuilder.loadTexts:cnRAGuardIfCfgPolicy.setStatus(_A)
_CnRAGuardIfCounter_Type=Gauge32
_CnRAGuardIfCounter_Object=MibTableColumn
cnRAGuardIfCounter=_CnRAGuardIfCounter_Object((1,3,6,1,4,1,17713,24,9,1,1,1,3),_CnRAGuardIfCounter_Type())
cnRAGuardIfCounter.setMaxAccess('read-only')
if mibBuilder.loadTexts:cnRAGuardIfCounter.setStatus(_A)
mibBuilder.exportSymbols(_C,**{_E:RAGuardPolicy,'cnRAGuardMib':cnRAGuardMib,'cnRAGuardIfCfg':cnRAGuardIfCfg,'cnRAGuardIfCfgTable':cnRAGuardIfCfgTable,'cnRAGuardIfCfgEntry':cnRAGuardIfCfgEntry,_D:cnRAGuardIfCfgIfIndex,'cnRAGuardIfCfgPolicy':cnRAGuardIfCfgPolicy,'cnRAGuardIfCounter':cnRAGuardIfCounter})