_D='read-write'
_C='extremeVlanIfIndex'
_B='EXTREME-VLAN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
extremeAgent,=mibBuilder.importSymbols('EXTREME-BASE-MIB','extremeAgent')
extremeVlanIfIndex,=mibBuilder.importSymbols(_B,_C)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
extremeOspf=ModuleIdentity((1,3,6,1,4,1,1916,1,15))
_ExtremeOspfInterfaceTable_Object=MibTable
extremeOspfInterfaceTable=_ExtremeOspfInterfaceTable_Object((1,3,6,1,4,1,1916,1,15,1))
if mibBuilder.loadTexts:extremeOspfInterfaceTable.setStatus(_A)
_ExtremeOspfInterfaceEntry_Object=MibTableRow
extremeOspfInterfaceEntry=_ExtremeOspfInterfaceEntry_Object((1,3,6,1,4,1,1916,1,15,1,1))
extremeOspfInterfaceEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:extremeOspfInterfaceEntry.setStatus(_A)
_ExtremeOspfAreaId_Type=IpAddress
_ExtremeOspfAreaId_Object=MibTableColumn
extremeOspfAreaId=_ExtremeOspfAreaId_Object((1,3,6,1,4,1,1916,1,15,1,1,1),_ExtremeOspfAreaId_Type())
extremeOspfAreaId.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeOspfAreaId.setStatus(_A)
_ExtremeOspfInterfacePassive_Type=TruthValue
_ExtremeOspfInterfacePassive_Object=MibTableColumn
extremeOspfInterfacePassive=_ExtremeOspfInterfacePassive_Object((1,3,6,1,4,1,1916,1,15,1,1,2),_ExtremeOspfInterfacePassive_Type())
extremeOspfInterfacePassive.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeOspfInterfacePassive.setStatus(_A)
_ExtremeOspfInterfaceStatus_Type=RowStatus
_ExtremeOspfInterfaceStatus_Object=MibTableColumn
extremeOspfInterfaceStatus=_ExtremeOspfInterfaceStatus_Object((1,3,6,1,4,1,1916,1,15,1,1,3),_ExtremeOspfInterfaceStatus_Type())
extremeOspfInterfaceStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:extremeOspfInterfaceStatus.setStatus(_A)
mibBuilder.exportSymbols('EXTREME-OSPF-MIB',**{'extremeOspf':extremeOspf,'extremeOspfInterfaceTable':extremeOspfInterfaceTable,'extremeOspfInterfaceEntry':extremeOspfInterfaceEntry,'extremeOspfAreaId':extremeOspfAreaId,'extremeOspfInterfacePassive':extremeOspfInterfacePassive,'extremeOspfInterfaceStatus':extremeOspfInterfaceStatus})