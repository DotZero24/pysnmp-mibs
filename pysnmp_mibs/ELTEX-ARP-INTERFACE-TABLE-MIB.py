_D='eltArpInterfaceEntry'
_C='ELTEX-ARP-INTERFACE-TABLE-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltMesArpSpec,=mibBuilder.importSymbols('ELTEX-MES-IP','eltMesArpSpec')
rsArpInterfaceEntry,=mibBuilder.importSymbols('RADLAN-IP','rsArpInterfaceEntry')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_EltArpInterfaceTable_Object=MibTable
eltArpInterfaceTable=_EltArpInterfaceTable_Object((1,3,6,1,4,1,35265,1,23,91,3,1))
if mibBuilder.loadTexts:eltArpInterfaceTable.setStatus(_A)
_EltArpInterfaceEntry_Object=MibTableRow
eltArpInterfaceEntry=_EltArpInterfaceEntry_Object((1,3,6,1,4,1,35265,1,23,91,3,1,1))
if mibBuilder.loadTexts:eltArpInterfaceEntry.setStatus(_A)
class _EltArpInterfaceArpLocalProxy_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_EltArpInterfaceArpLocalProxy_Type.__name__=_B
_EltArpInterfaceArpLocalProxy_Object=MibTableColumn
eltArpInterfaceArpLocalProxy=_EltArpInterfaceArpLocalProxy_Object((1,3,6,1,4,1,35265,1,23,91,3,1,1,1),_EltArpInterfaceArpLocalProxy_Type())
eltArpInterfaceArpLocalProxy.setMaxAccess('read-write')
if mibBuilder.loadTexts:eltArpInterfaceArpLocalProxy.setStatus(_A)
rsArpInterfaceEntry.registerAugmentions((_C,_D))
eltArpInterfaceEntry.setIndexNames(*rsArpInterfaceEntry.getIndexNames())
mibBuilder.exportSymbols(_C,**{'eltArpInterfaceTable':eltArpInterfaceTable,_D:eltArpInterfaceEntry,'eltArpInterfaceArpLocalProxy':eltArpInterfaceArpLocalProxy})