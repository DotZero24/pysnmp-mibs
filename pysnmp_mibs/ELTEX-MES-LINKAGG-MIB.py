_F='eltAggBalanceEntry'
_E='eltAggPortEntry'
_D='read-write'
_C='TruthValue'
_B='ELTEX-MES-LINKAGG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltMesLinkAgg,=mibBuilder.importSymbols('ELTEX-MES','eltMesLinkAgg')
dot3adAggPortEntry,=mibBuilder.importSymbols('IEEE8023-LAG-MIB','dot3adAggPortEntry')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList')
rlDot3adAggBalanceEntry,=mibBuilder.importSymbols('RADLAN-TRUNK-MIB','rlDot3adAggBalanceEntry')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention',_C)
eltMesLagMIB=ModuleIdentity((1,3,6,1,4,1,35265,1,23,9,1))
_EltMesLagMIBObjects_ObjectIdentity=ObjectIdentity
eltMesLagMIBObjects=_EltMesLagMIBObjects_ObjectIdentity((1,3,6,1,4,1,35265,1,23,9,1,1))
_EltMesLinkAggGlobal_ObjectIdentity=ObjectIdentity
eltMesLinkAggGlobal=_EltMesLinkAggGlobal_ObjectIdentity((1,3,6,1,4,1,35265,1,23,9,1,1,1))
_EltMesLinkAggPort_ObjectIdentity=ObjectIdentity
eltMesLinkAggPort=_EltMesLinkAggPort_ObjectIdentity((1,3,6,1,4,1,35265,1,23,9,1,1,2))
_EltAggPortTable_Object=MibTable
eltAggPortTable=_EltAggPortTable_Object((1,3,6,1,4,1,35265,1,23,9,1,1,2,1))
if mibBuilder.loadTexts:eltAggPortTable.setStatus(_A)
_EltAggPortEntry_Object=MibTableRow
eltAggPortEntry=_EltAggPortEntry_Object((1,3,6,1,4,1,35265,1,23,9,1,1,2,1,1))
if mibBuilder.loadTexts:eltAggPortEntry.setStatus(_A)
_EltAggPortPassive_Type=TruthValue
_EltAggPortPassive_Object=MibTableColumn
eltAggPortPassive=_EltAggPortPassive_Object((1,3,6,1,4,1,35265,1,23,9,1,1,2,1,1,1),_EltAggPortPassive_Type())
eltAggPortPassive.setMaxAccess(_D)
if mibBuilder.loadTexts:eltAggPortPassive.setStatus(_A)
_EltAggBalanceTable_Object=MibTable
eltAggBalanceTable=_EltAggBalanceTable_Object((1,3,6,1,4,1,35265,1,23,9,1,1,2,2))
if mibBuilder.loadTexts:eltAggBalanceTable.setStatus(_A)
_EltAggBalanceEntry_Object=MibTableRow
eltAggBalanceEntry=_EltAggBalanceEntry_Object((1,3,6,1,4,1,35265,1,23,9,1,1,2,2,1))
if mibBuilder.loadTexts:eltAggBalanceEntry.setStatus(_A)
class _EltAggBalanceMplsAware_Type(TruthValue):defaultValue=2
_EltAggBalanceMplsAware_Type.__name__=_C
_EltAggBalanceMplsAware_Object=MibTableColumn
eltAggBalanceMplsAware=_EltAggBalanceMplsAware_Object((1,3,6,1,4,1,35265,1,23,9,1,1,2,2,1,1),_EltAggBalanceMplsAware_Type())
eltAggBalanceMplsAware.setMaxAccess(_D)
if mibBuilder.loadTexts:eltAggBalanceMplsAware.setStatus(_A)
dot3adAggPortEntry.registerAugmentions((_B,_E))
eltAggPortEntry.setIndexNames(*dot3adAggPortEntry.getIndexNames())
rlDot3adAggBalanceEntry.registerAugmentions((_B,_F))
eltAggBalanceEntry.setIndexNames(*rlDot3adAggBalanceEntry.getIndexNames())
mibBuilder.exportSymbols(_B,**{'eltMesLagMIB':eltMesLagMIB,'eltMesLagMIBObjects':eltMesLagMIBObjects,'eltMesLinkAggGlobal':eltMesLinkAggGlobal,'eltMesLinkAggPort':eltMesLinkAggPort,'eltAggPortTable':eltAggPortTable,_E:eltAggPortEntry,'eltAggPortPassive':eltAggPortPassive,'eltAggBalanceTable':eltAggBalanceTable,_F:eltAggBalanceEntry,'eltAggBalanceMplsAware':eltAggBalanceMplsAware})