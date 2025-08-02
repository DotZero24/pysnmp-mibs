_D='read-create'
_C='ifIndex'
_B='IF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltexLtd,=mibBuilder.importSymbols('ELTEX-SMI-ACTUAL','eltexLtd')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_B,'InterfaceIndex',_C)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
eltexIpUnnumberedMIB=ModuleIdentity((1,3,6,1,4,1,35265,42))
if mibBuilder.loadTexts:eltexIpUnnumberedMIB.setRevisions(('2017-10-16 00:00',))
_EltexIpUnnumberedMIBObjects_ObjectIdentity=ObjectIdentity
eltexIpUnnumberedMIBObjects=_EltexIpUnnumberedMIBObjects_ObjectIdentity((1,3,6,1,4,1,35265,42,1))
_EltexIpUnnumberedInterfaceTable_Object=MibTable
eltexIpUnnumberedInterfaceTable=_EltexIpUnnumberedInterfaceTable_Object((1,3,6,1,4,1,35265,42,1,1))
if mibBuilder.loadTexts:eltexIpUnnumberedInterfaceTable.setStatus(_A)
_EltexIpUnnumberedInterfaceEntry_Object=MibTableRow
eltexIpUnnumberedInterfaceEntry=_EltexIpUnnumberedInterfaceEntry_Object((1,3,6,1,4,1,35265,42,1,1,1))
eltexIpUnnumberedInterfaceEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:eltexIpUnnumberedInterfaceEntry.setStatus(_A)
_EltexIpUnnumberedParentIfIndex_Type=InterfaceIndex
_EltexIpUnnumberedParentIfIndex_Object=MibTableColumn
eltexIpUnnumberedParentIfIndex=_EltexIpUnnumberedParentIfIndex_Object((1,3,6,1,4,1,35265,42,1,1,1,1),_EltexIpUnnumberedParentIfIndex_Type())
eltexIpUnnumberedParentIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:eltexIpUnnumberedParentIfIndex.setStatus(_A)
_EltexIpUnnumberedRowStatus_Type=RowStatus
_EltexIpUnnumberedRowStatus_Object=MibTableColumn
eltexIpUnnumberedRowStatus=_EltexIpUnnumberedRowStatus_Object((1,3,6,1,4,1,35265,42,1,1,1,2),_EltexIpUnnumberedRowStatus_Type())
eltexIpUnnumberedRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:eltexIpUnnumberedRowStatus.setStatus(_A)
mibBuilder.exportSymbols('ELTEX-IP-UNNUMBERED-MIB',**{'eltexIpUnnumberedMIB':eltexIpUnnumberedMIB,'eltexIpUnnumberedMIBObjects':eltexIpUnnumberedMIBObjects,'eltexIpUnnumberedInterfaceTable':eltexIpUnnumberedInterfaceTable,'eltexIpUnnumberedInterfaceEntry':eltexIpUnnumberedInterfaceEntry,'eltexIpUnnumberedParentIfIndex':eltexIpUnnumberedParentIfIndex,'eltexIpUnnumberedRowStatus':eltexIpUnnumberedRowStatus})