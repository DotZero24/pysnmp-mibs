_F='read-create'
_E='not-accessible'
_D='rcL3IpSubnetFilterIPAclNumber'
_C='rcL3IpSubnetFilterIfIndex'
_B='SWITCH-L3FILTER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
iscomSwitch,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','iscomSwitch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
PortList,=mibBuilder.importSymbols('SWITCH-TC','PortList')
rcL3Filter=ModuleIdentity((1,3,6,1,4,1,8886,6,1,15))
_RcL3IpSubnetFilter_ObjectIdentity=ObjectIdentity
rcL3IpSubnetFilter=_RcL3IpSubnetFilter_ObjectIdentity((1,3,6,1,4,1,8886,6,1,15,1))
_RcL3IpSubnetFilterTable_Object=MibTable
rcL3IpSubnetFilterTable=_RcL3IpSubnetFilterTable_Object((1,3,6,1,4,1,8886,6,1,15,1,1))
if mibBuilder.loadTexts:rcL3IpSubnetFilterTable.setStatus(_A)
_RcL3IpSubnetFilterEntry_Object=MibTableRow
rcL3IpSubnetFilterEntry=_RcL3IpSubnetFilterEntry_Object((1,3,6,1,4,1,8886,6,1,15,1,1,1))
rcL3IpSubnetFilterEntry.setIndexNames((0,_B,_C),(0,_B,_D))
if mibBuilder.loadTexts:rcL3IpSubnetFilterEntry.setStatus(_A)
_RcL3IpSubnetFilterIfIndex_Type=Integer32
_RcL3IpSubnetFilterIfIndex_Object=MibTableColumn
rcL3IpSubnetFilterIfIndex=_RcL3IpSubnetFilterIfIndex_Object((1,3,6,1,4,1,8886,6,1,15,1,1,1,1),_RcL3IpSubnetFilterIfIndex_Type())
rcL3IpSubnetFilterIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:rcL3IpSubnetFilterIfIndex.setStatus(_A)
_RcL3IpSubnetFilterIPAclNumber_Type=Integer32
_RcL3IpSubnetFilterIPAclNumber_Object=MibTableColumn
rcL3IpSubnetFilterIPAclNumber=_RcL3IpSubnetFilterIPAclNumber_Object((1,3,6,1,4,1,8886,6,1,15,1,1,1,2),_RcL3IpSubnetFilterIPAclNumber_Type())
rcL3IpSubnetFilterIPAclNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:rcL3IpSubnetFilterIPAclNumber.setStatus(_A)
_RcL3IpSubnetFilterStatus_Type=RowStatus
_RcL3IpSubnetFilterStatus_Object=MibTableColumn
rcL3IpSubnetFilterStatus=_RcL3IpSubnetFilterStatus_Object((1,3,6,1,4,1,8886,6,1,15,1,1,1,3),_RcL3IpSubnetFilterStatus_Type())
rcL3IpSubnetFilterStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:rcL3IpSubnetFilterStatus.setStatus(_A)
_RcL3IpSubnetFilterPorts_Type=PortList
_RcL3IpSubnetFilterPorts_Object=MibTableColumn
rcL3IpSubnetFilterPorts=_RcL3IpSubnetFilterPorts_Object((1,3,6,1,4,1,8886,6,1,15,1,1,1,4),_RcL3IpSubnetFilterPorts_Type())
rcL3IpSubnetFilterPorts.setMaxAccess(_F)
if mibBuilder.loadTexts:rcL3IpSubnetFilterPorts.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'rcL3Filter':rcL3Filter,'rcL3IpSubnetFilter':rcL3IpSubnetFilter,'rcL3IpSubnetFilterTable':rcL3IpSubnetFilterTable,'rcL3IpSubnetFilterEntry':rcL3IpSubnetFilterEntry,_C:rcL3IpSubnetFilterIfIndex,_D:rcL3IpSubnetFilterIPAclNumber,'rcL3IpSubnetFilterStatus':rcL3IpSubnetFilterStatus,'rcL3IpSubnetFilterPorts':rcL3IpSubnetFilterPorts})